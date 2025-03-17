import logging
import os
from typing import List, Optional

from browser_use import Browser, BrowserConfig, BrowserContextConfig, Controller
from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext

logger = logging.getLogger(__name__)


async def set_file_input(index: int, paths: str | List[str], browser: BrowserContext):
    """
    Set the file input value to the given path or list of paths.

    Args:
        index: The DOM element index to target
        paths: Local file path or list of local file paths to upload
        browser: Browser context for interaction

    Returns:
        ActionResult: Result of the upload operation
    """
    if isinstance(paths, str):
        paths = [paths]

    for path in paths:
        if not os.path.exists(path):
            return ActionResult(error=f"File {path} does not exist")

    dom_el = await browser.get_dom_element_by_index(index)
    file_upload_dom_el = dom_el.get_file_upload_element()

    if file_upload_dom_el is None:
        msg = f"No file upload element found at index {index}. The element may be hidden or not an input type file"
        logger.info(msg)
        return ActionResult(error=msg)

    file_upload_el = await browser.get_locate_element(file_upload_dom_el)

    if file_upload_el is None:
        msg = f"No file upload element found at index {index}. The element may be hidden or not an input type file"
        logger.info(msg)
        return ActionResult(error=msg)

    try:
        await file_upload_el.set_input_files(paths)
        msg = f"Successfully set file input value to {paths}"
        logger.info(msg)
        return ActionResult(extracted_content=msg, include_in_memory=True)
    except Exception as e:
        msg = f"Failed to upload file to index {index}: {str(e)}"
        logger.info(msg)
        return ActionResult(error=msg)


class BrowserInitializer:
    """
    Initialize and cache browser and controller instances.

    This class uses a singleton pattern to ensure we only create one browser
    instance throughout the application lifecycle, which saves resources.
    """

    _browser = None
    _controller = None
    _browser_context = None

    @classmethod
    def init_browser(cls, config=BrowserConfig()):
        """
        Initialize and cache the Browser instance.

        Returns:
            Browser: Browser instance for web automation
        """
        if cls._browser is not None:
            return cls._browser

        cls._browser = Browser(config=config)
        return cls._browser

    @classmethod
    def init_browser_context(cls, config: Optional[BrowserContextConfig]):
        """
        Initialize and cache the BrowserContext instance.

        Returns:
            BrowserContext: BrowserContext instance for managing browser context
        """
        if cls._browser_context is not None:
            return cls._browser_context

        downloads_path = os.path.join(os.getcwd(), "tmp", "downloads")
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)

        cookies_file = os.path.join(os.getcwd(), "tmp", "cookies.json")

        context_config = BrowserContextConfig(
            save_downloads_path=downloads_path, cookies_file=cookies_file, _force_keep_context_alive=True
        )
        browser = cls.init_browser(config=config)
        cls._browser_context = BrowserContext(browser=browser, config=context_config)
        return cls._browser_context

    @classmethod
    def init_controller(cls):
        """
        Initialize and cache the Controller instance.

        Returns:
            Controller: Controller instance for managing browser actions
        """
        if cls._controller is not None:
            return cls._controller

        controller = Controller()

        cls._controller = controller
        return cls._controller
