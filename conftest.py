import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from config import bot, chat_id, daily, host_stage

load_dotenv()


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    if os.getenv("HEADLESS") == "True":
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 4000)
    # driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.hookimpl(trylast=True)
# def pytest_sessionfinish(session, exitstatus):
#     bot.send_message(chat_id, "О какие то тесты на стэйдж прошли, посмотри, вдруг они в отчете - https://101internettests.github.io/autotests/")