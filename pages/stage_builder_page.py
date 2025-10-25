from pages.base_page import BasePage


class StagePage(BasePage):

    def wait_for_load_page(self):
        try:
            self.page.get_by_role("button", name="Ok").click(timeout=5000)

        except Exception:
            print("Pop up is not displayed")
        self.page.wait_for_selector(r".float-start.ml-1.mt-\[21px\].text-sm.text-zinc-500")
