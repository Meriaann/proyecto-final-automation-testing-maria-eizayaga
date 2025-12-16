import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime
import requests
import pytest

@pytest.fixture(scope="function")
def driver(request):
    
    chrome_options = Options()
    prefs = {"credentials_enable_service": False,
             "profile.password_manager_enabled": False}
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options) 
    
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "pytest-api-client"
        }

    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params
        )

    def post(self, endpoint, json=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=json
        )

    def put(self, endpoint, json=None):
        return requests.put(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=json
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )

@pytest.fixture(scope="session")
def api_client():
    return APIClient("https://jsonplaceholder.typicode.com")



