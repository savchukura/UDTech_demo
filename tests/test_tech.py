from pages.sign_in_page import SignInPage
from pages.stage_builder_page import StagePage


class TestTechPage:

    def test_sign_in_with_hardcoded_email(self, page):
        page.goto('https://events.shooters.global/')
        sign_in_page = SignInPage(page)
        sign_in_page.sign_in('pewana7577@hh7f.com', 'h6362Jo4aw')
        stage_page = StagePage(page)
        stage_page.wait_for_load_page()
        sign_in_page.log_out()
        alert_text = sign_in_page.get_alert_text_after_log_out()

        assert alert_text == 'Logged Out!You have been signed out successfully.'


    def test_sign_in_with_generated_email(self, page):
        sign_in_page = SignInPage(page)
        email, password = sign_in_page.generate_email()

        page.goto('https://events.shooters.global/')
        sign_in_page.sign_in(email, password)
        stage_page = StagePage(page)
        stage_page.wait_for_load_page()
        sign_in_page.log_out()
        alert_text = sign_in_page.get_alert_text_after_log_out()

        assert alert_text == 'Logged Out!You have been signed out successfully.'
