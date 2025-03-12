import time
from pathlib import Path
from typing import Callable, Dict, Optional

import requests
import yaml


class ZohoTokenManager:
    """Utility class to manage Zoho Desk API tokens with configurable save callback."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: Optional[str] = None,
        access_token: Optional[str] = None,
        grant_token: Optional[str] = None,
        expires_at: Optional[int] = None,
        on_save: Optional[Callable[[Dict], None]] = None,
    ):
        """Initialize the token manager with client credentials.

        Args:
            client_id: Zoho API client ID
            client_secret: Zoho API client secret
            grant_token: Grant token for initial authorization if access_token and refresh_token aren't initialized
            refresh_token: Issued refresh token for token renewal
            access_token: Last issued access token if available
            expires_at: Optional timestamp when the token expires
            on_save: Optional callback function to save token updates
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.grant_token = grant_token
        self.expires_at = expires_at
        self._on_save = on_save

    def _save_tokens(self, token_data: Dict):
        """Save token updates using the provided callback.

        Args:
            token_data: Dictionary containing token information to save
        """
        if self._on_save:
            try:
                self._on_save(token_data)
            except Exception as e:
                print(f"Error in token save callback: {e}")

    def get_access_token_from_grant(self, grant_token: Optional[str] = None) -> Dict:
        """Get access and refresh tokens using a grant token.

        Args:
            grant_token: The grant token obtained from Zoho authorization.
                         If None, uses the grant_token from initialization.

        Returns:
            Dict containing access_token, refresh_token and other details
        """
        if not grant_token and not self.grant_token:
            raise ValueError("No grant token provided")

        token_to_use = grant_token or self.grant_token

        url = "https://accounts.zoho.com/oauth/v2/token"
        params = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": token_to_use,
        }

        response = requests.post(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to get access token: {response.text}")

        token_data = response.json()
        self.access_token = token_data.get("access_token")
        self.refresh_token = token_data.get("refresh_token")
        self.expires_at = time.time() + token_data.get("expires_in", 3600)

        # Prepare token data for saving
        save_data = {
            "zoho_access_token": self.access_token,
            "zoho_refresh_token": self.refresh_token,
            "zoho_expires_at": self.expires_at,
            "zoho_grant_token": "",  # Clear grant token after use
        }
        self._save_tokens(save_data)

        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
        }

    def refresh_access_token(self) -> Dict:
        """Refresh the access token using the refresh token.

        Returns:
            Dict containing the new access_token and other details
        """
        if not self.refresh_token:
            raise ValueError("No refresh token available")

        url = "https://accounts.zoho.com/oauth/v2/token"
        params = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
        }

        response = requests.post(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to refresh access token: {response.text}")

        token_data = response.json()
        self.access_token = token_data.get("access_token")
        self.expires_at = time.time() + token_data.get("expires_in", 3600)

        # Prepare token data for saving
        save_data = {
            "zoho_access_token": self.access_token,
            "zoho_expires_at": self.expires_at,
        }
        self._save_tokens(save_data)

        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
        }

    def get_valid_access_token(self) -> str:
        """Get a valid access token, refreshing if necessary.

        If no refresh token is available but a grant token is, it will
        attempt to get a new access token using the grant token.

        Returns:
            A valid access token string
        """
        # If no refresh token but grant token is available, get tokens from grant
        if not self.refresh_token and self.grant_token:
            self.get_access_token_from_grant()
            return self.access_token

        if not self.access_token:
            raise ValueError("No access token available")

        if not self.refresh_token:
            raise ValueError("No refresh token available")

        # If token is expired or will expire in the next 5 minutes, refresh it
        if time.time() > (self.expires_at - 300):
            self.refresh_access_token()

        return self.access_token


def create_yml_save_callback(config_path: Path) -> Callable[[Dict], None]:
    """Create a callback function to save token updates to a YAML file.

    Args:
        config_path: Path to the YAML configuration file

    Returns:
        A callable that can be used as an on_save callback
    """

    def save_callback(token_updates: Dict):
        """Save token updates to the YAML configuration file.

        Args:
            token_updates: Dictionary of token updates to save
        """
        # Load existing configuration
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        # Update configuration with token updates
        config.update(token_updates)

        # Save updated configuration
        with open(config_path, "w") as f:
            yaml.dump(config, f)

    return save_callback
