import requests
import json
from datetime import datetime

class InstagramBot:
    def __init__(self):
        self.session = {}

    def login(self, username: str, password: str) -> dict:
        url = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        time = int(datetime.now().timestamp())

        print("Fetching the initial CSRF token...")
        response = requests.get(url)
        csrf = response.cookies['csrftoken']
        print(f"CSRF token fetched: {csrf}")

        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        login_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/77.0.3865.120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf
        }

        print("Sending POST request to login...")
        login_response = requests.post(login_url, data=payload, headers=login_header)
        json_data = json.loads(login_response.text)

        print("Login response received...")
        if json_data.get("authenticated"):
            print("Authentication successful!")
            cookies = login_response.cookies
            cookie_jar = cookies.get_dict()

            self.session = {
                "csrf_token": cookie_jar['csrftoken'],
                "session_id": cookie_jar['sessionid']
            }
            print(f"Session info: {self.session}")
            return self.session
        else:
            print("Authentication failed.")
            return {"error": "Authentication failed"}
