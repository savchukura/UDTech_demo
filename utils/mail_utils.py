import requests
import time
import re


class TempMail:
    BASE_URL = "https://api.mail.tm"

    def __init__(self):
        self.address, self.password, self.token = self._create_account()

    def _create_account(self):
        password = "TestPass123!"
        domain = requests.get(f"{self.BASE_URL}/domains").json()["hydra:member"][0]["domain"]
        email = f"test_{int(time.time())}@{domain}"

        data = {"address": email, "password": password}
        resp = requests.post(f"{self.BASE_URL}/accounts", json=data)
        if resp.status_code not in (200, 201):
            raise Exception(f"❌ Account creation failed: {resp.text}")

        token_resp = requests.post(f"{self.BASE_URL}/token", json=data)
        token = token_resp.json()["token"]
        return email, password, token

    def get_messages(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        resp = requests.get(f"{self.BASE_URL}/messages", headers=headers)
        return resp.json()["hydra:member"]

    def wait_for_email(self, subject_filter= "Password for Shooters Global", timeout=60):
        start = time.time()
        while time.time() - start < timeout:
            messages = self.get_messages()
            if messages:
                for msg in messages:
                    if not subject_filter or subject_filter.lower() in msg["subject"].lower():
                        return self.get_message_content(msg["id"])
            time.sleep(3)
        raise TimeoutError("Email not received within timeout.")

    def get_message_content(self, message_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        resp = requests.get(f"{self.BASE_URL}/messages/{message_id}", headers=headers)
        return resp.json()

    def extract_password_from_email(self, email_data: dict) -> str:
        html_content = email_data.get("text", "")
        if not html_content:
            raise ValueError("❌ email have not any text")

        matches = re.findall(r'<div[^>]*>([^<>]+)</div>', html_content)

        for text in matches:
            clean = text.strip()
            if re.fullmatch(r'[A-Za-z0-9]{6,}', clean):
                return clean

        fallback = re.search(r'\b[A-Za-z0-9]{8,}\b', html_content)
        if fallback:
            return fallback.group(0)

        raise ValueError("❌ Emai not detected")
