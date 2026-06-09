from unittest.mock import MagicMock, patch

from patchwork.common.client.llm.litellm_ import LiteLLMClient


def test_litellm_client_is_model_supported():
    client = LiteLLMClient(api_key="test-key")
    assert client.is_model_supported("anthropic/claude-sonnet-4-6") is True
    assert client.is_model_supported("openai/gpt-4o") is True
    assert client.is_model_supported("any-model") is True


def test_litellm_client_chat_completion():
    client = LiteLLMClient(api_key="test-key")

    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="4"))]

    with patch("litellm.completion", return_value=mock_response) as mock_completion:
        response = client.chat_completion(
            messages=[{"role": "user", "content": "What is 2+2?"}],
            model="anthropic/claude-sonnet-4-6",
        )

        mock_completion.assert_called_once()
        call_kwargs = mock_completion.call_args
        assert call_kwargs.kwargs["model"] == "anthropic/claude-sonnet-4-6"
        assert call_kwargs.kwargs["drop_params"] is True
        assert call_kwargs.kwargs["api_key"] == "test-key"
        assert response.choices[0].message.content == "4"


def test_litellm_client_drop_params_default():
    client = LiteLLMClient(api_key="test-key")

    mock_response = MagicMock()
    with patch("litellm.completion", return_value=mock_response) as mock_completion:
        client.chat_completion(
            messages=[{"role": "user", "content": "test"}],
            model="openai/gpt-4o",
        )

        call_kwargs = mock_completion.call_args.kwargs
        assert call_kwargs["drop_params"] is True
