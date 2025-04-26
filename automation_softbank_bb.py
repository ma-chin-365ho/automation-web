import os

from playwright.sync_api import expect

from automation_base import AutomationBase, PATH_DOWNLOADS
from personal_info import personal_info

class AutomationSoftBankBB(AutomationBase):

    def script(self):
        self.login()
        self.download_invoice()

    def login(self):
        self.page.goto(personal_info.URL_MY_SOFTBANK_BB_LOGIN)
        self.page.wait_for_load_state()

        self.page.locator('input[name="sid"]').fill(personal_info.ID_MY_SOFTBANK_BB)
        self.page.locator('input[name="spw"]').fill(personal_info.PW_MY_SOFTBANK_BB)
        self.page.get_by_text("ログインする", exact=True).first.dispatch_event("click")
        self.page.wait_for_load_state()
        # self.verify_ident()

    def security_check(self):
        if self.wait_for_page("セキュリティチェック | お客様専用ページ | ソフトバンク"):
            self.page.get_by_text("送信する", exact=True).click()
            self.page.wait_for_load_state()
            auth_code = input("Input Auth Code:")
            self.page.locator('input[name="securityNo"]').fill(auth_code)
            self.page.get_by_text("本人確認をする", exact=True).click()
            self.page.wait_for_load_state()
    
    def download_invoice(self):
        self.page.get_by_role("link", name="料金確認").first.click()
        self.page.wait_for_load_state()
        self.page.get_by_role("link", name="請求書の印刷").click()
        self.page.wait_for_load_state()
        self.security_check()
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="請求書PDFファイル").click()
        download = download_info.value
        download.save_as(os.path.join(PATH_DOWNLOADS, download.suggested_filename))

if __name__ == '__main__':
    a = AutomationSoftBankBB()
    a.run()