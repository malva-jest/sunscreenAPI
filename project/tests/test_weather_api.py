import requests
import pytest
import os

from dotenv import load_dotenv
load_dotenv()

API_KEYYY = os.getenv('TEST_API_KEY')

def test_get_check_status_code_equals_200():
     response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=doha&units=imperial&appid={API_KEYYY}")
     assert response.status_code == 200

def test_get_check_content_type_equals_json():
     response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=doha&units=imperial&appid=ADD_PERSONAL_API_KEY")
     assert response.headers["Content-Type"] == "application/json; charset=utf-8"
