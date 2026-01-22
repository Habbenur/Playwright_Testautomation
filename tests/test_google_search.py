import playwright
import pytest
import re
from playwright.sync_api import Page, expect, sync_playwright, Playwright

BASE_URL = "https://test-379574553568.us-central1.run.app"
frans_api_key = "habbe_testar_with_playwright"

def test_manstrom_io(page: Page):
    page.goto("https://manstrom.github.io")
    expect(page).to_have_title("Manstrom.io - Accelerate your software development with AI-powered tools")

def test_frans_ui_has_title(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Frank's API test")

#Om man har problem med att använda pytest.ini för att köra med UI
'''def test_frans_ui_with():
    browser = sync_playwright().start().chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto(BASE_URL)
    expect(page).to_have_title("Frank's API test")
    browser.close()
    '''


def test_create_student_in_ui(page: Page):
    page.goto(BASE_URL)
    page.get_by_test_id("api_key_input").fill(frans_api_key)
    page.get_by_test_id("name_input").fill("Playwright")
    page.get_by_test_id("age_input").fill("24")
    page.get_by_test_id("grade_input").fill("A")
    page.get_by_test_id("submit_student").click()

def test_create_student_with_placeholder_in_ui(page: Page):
    page.goto(BASE_URL)
    page.get_by_placeholder("Enter your API key").fill(frans_api_key)
    page.get_by_placeholder("Enter name").fill("Playwright_Placeholder")
    page.get_by_placeholder("Enter age").fill("25")
    page.get_by_placeholder("Enter grade").fill("A+")
    page.get_by_test_id("submit_student").click()

    # ---------------------

def test_delete_student_in_ui(page: Page):
    page.goto(BASE_URL)
    page.get_by_test_id("api_key_input").fill(frans_api_key)
    page.get_by_test_id("refresh_button").click()
    page.get_by_test_id("student_3_delete_button").click()

def test_edit_student_in_ui(page: Page):
    page.goto(BASE_URL)
    page.get_by_test_id("api_key_input").fill(frans_api_key)
    page.get_by_test_id("refresh_button").click()
    page.get_by_test_id("student_2_edit_button").click()
    page.get_by_test_id("name_input").fill("Edited_Playwright")
    page.get_by_test_id("age_input").fill("30")
    page.get_by_test_id("grade_input").fill("B")
    page.get_by_test_id("submit_student").click()
    # ---------------------







#alternative way to create a page
#def test_creating_page():
#    Playwright.page = browser("chrome")