from pages.base_page import BasePage
from utils.mail_utils import TempMail


class SignInPage(BasePage):

    def sign_up(self, email):
        self.page.get_by_role("tab", name="Sign up").click()
        self.page.get_by_role("textbox", name="Enter your email").fill(email)
        self.page.get_by_role("checkbox", name="I have read and agree to the").click()
        self.page.get_by_role("button", name="Sign up", exact=True).click()

    def sign_in(self, email, password):
        self.page.get_by_role("banner").get_by_role("button", name="Build for free").click()
        self.page.get_by_role("tab", name="Sign in").click()
        self.page.get_by_role("textbox", name="Enter your email or phone").fill(email)
        self.page.get_by_role("textbox", name="Enter password").fill(password)
        self.page.get_by_role("button", name="Sign in", exact=True).click()

    def log_out(self):
        self.page.get_by_role("button", name="Account avatar").click()
        self.page.get_by_text("Log Out").click()
        self.page.get_by_role("button", name="Log Out").click()
        self.page.get_by_role("alert", name="Logged Out!").click()

    def get_alert_text_after_log_out(self):
        text = self.page.get_by_role("alert", name="Logged Out!").text_content()
        return text

    def generate_email(self):
        self.page.goto('https://events.shooters.global/sign-in#get-started')
        temp_mail = TempMail()
        self.sign_up(temp_mail.address)
        email_data = temp_mail.wait_for_email()
        password = temp_mail.extract_password_from_email(email_data)

        return temp_mail.address, password