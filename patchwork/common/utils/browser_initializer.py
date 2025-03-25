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


async def close_current_tab(browser: BrowserContext):
    await browser.close_current_tab()
    msg = "🔄  Closed current tab"
    logger.info(msg)
    return ActionResult(extracted_content=msg, include_in_memory=True)


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
    def init_browser_context(cls, config: Optional[BrowserConfig], downloads_path: Optional[str] = None):
        """
        Initialize and cache the BrowserContext instance.

        Returns:
            BrowserContext: BrowserContext instance for managing browser context
        """
        if cls._browser_context is not None:
            return cls._browser_context

        if downloads_path and not os.path.exists(downloads_path):
            os.makedirs(downloads_path)

        context_config = BrowserContextConfig(
            # cookies_file=cookies_file,
            browser_window_size={"width": 1920, "height": 1080},
        )
        browser = cls.init_browser(config=config)

        class BrowserContextWithDownloadHandling(BrowserContext):
            async def handle_download(self, download):
                suggested_filename = download.suggested_filename
                unique_filename = await self._get_unique_filename(downloads_path, suggested_filename)
                download_path = os.path.join(downloads_path, unique_filename)
                await download.save_as(download_path)
                logger.info(f"Downloaded file saved to {download_path}")

            async def _initialize_session(self):
                async def _download_listener(download):
                    logger.info("[BUD] Download event triggered")
                    await self.handle_download(download)
                    return download

                def _new_page_listener(page):
                    logger.info("[BUD] Adding download event listener to page")
                    page.on("download", _download_listener)
                    return page

                await super()._initialize_session()

                logger.info("[BUD] Adding page event listener to context")
                self.session.context.on("page", _new_page_listener)

                logger.info(f"[BUD] Adding download event listener to {len(self.session.context.pages)} existing pages")
                for page in self.session.context.pages:
                    page.on("download", _download_listener)

        cls._browser_context = (
            BrowserContextWithDownloadHandling(browser=browser, config=context_config)
            if downloads_path
            else BrowserContext(browser=browser, config=context_config)
        )
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

        controller.action(
            "Set the value of a file input to the given path or list of paths",
        )(set_file_input)

        controller.action(
            description="Close the tab that is currently active",
        )(close_current_tab)

        cls._controller = controller
        return cls._controller
