import datetime
from abc import ABC, abstractmethod

from playwright.sync_api import sync_playwright, Playwright, Page

MSEC_TIMEOUT=15 * 1000
SEC_WAIT_PAGE=5
PATH_TRACE=f"log/trace{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.zip"
PATH_DOWNLOADS="download"

class AutomationBase(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def script(self):
        raise NotImplementedError()

    def run(self):
        with sync_playwright() as playwright:
            self.chromium = playwright.chromium
            self.browser = self.chromium.launch(downloads_path=PATH_DOWNLOADS)
            self.context = self.browser.new_context()
            self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
            self.context.set_default_timeout(MSEC_TIMEOUT)
            self.page = self.context.new_page()
            try:
                self.script()
            except Exception as e:
                print(e)
                if hasattr(e, 'trace'):
                    print(e.trace)
                
            self.context.tracing.stop(path = PATH_TRACE)
            self.browser.close()

    def wait_for_page(self, title: str) -> bool:
        for sec in range(SEC_WAIT_PAGE):
            if self.page.locator("title").inner_text() == title:
                return True
            self.page.wait_for_timeout(1000)
        return False
