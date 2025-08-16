from typing import Literal

from playwright.sync_api import expect

from automation_base import AutomationBase
from personal_info import personal_info

class AutomationYmobile(AutomationBase):

    def script(self):
        self.login()
        self.download_invoice()

    def login(self):
        self.page.goto(personal_info.URL_MY_YMOBILE_LOGIN)
        self.page.wait_for_load_state()

        self.page.locator('input[name="telnum"]').fill(personal_info.ID_MY_YMOBILE)
        self.page.locator('input[name="password"]').fill(personal_info.PW_MY_YMOBILE)
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("Tab")
        self.page.get_by_role("button", name="ログインする").click()
        self.page.wait_for_load_state()
        self.verify_ident("softbank")

    def verify_ident(self, displayType: Literal["softbank", "ymobile"]):
        title = "本人確認 | ワイモバイル"
        if displayType == "softbank":
            title = "本人確認 | My SoftBank | ソフトバンク"

        if self.wait_for_page(title):
            auth_code = input("Input Auth Code:")
            self.page.locator('input[name="password"]').fill(auth_code)
            self.page.wait_for_timeout(1000)
            self.page.keyboard.press("Tab")
            self.page.get_by_role("button", name="本人確認する").click()
            self.page.wait_for_load_state()
            self.page.wait_for_timeout(2000)
    
    def download_invoice(self):
        self.page.get_by_role("link", name="料金案内").locator("..").click()
        self.page.wait_for_load_state()
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("link", name="書面発行").click()
        self.page.wait_for_load_state()
        self.page.get_by_text("自分で印刷する（無料）").first.click()
        self.page.wait_for_load_state()
        self.verify_ident("ymobile")
        self.page.get_by_role("link", name="一括印刷用PDFファイル").click()
        # NOTE: イベント待ちのままタイムアウトになる。
        # self.page.wait_for_load_state()


if __name__ == '__main__':
    a = AutomationYmobile()
    a.run()