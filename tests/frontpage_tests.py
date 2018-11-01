from selenium import webdriver
from selenium.webdriver.common.by import By

def test_raceday_timeline_heading_is_correct(selenium):
    selenium.get("https://beta.rikstoto.no")
    element = selenium.find_element(By.CLASS_NAME, "race-day-timeline__header__content__title")
    assert element.text == "Bane- og løpsoversikt"

def test_raceday_timeline_is_not_empty(selenium):
    selenium.get("https://beta.rikstoto.no")
    elements = selenium.find_elements(By.CLASS_NAME, "timeline-race-cell__race-number")
    assert len(elements) > 0

def test_can_navigate_via_top_menu_to_spill(selenium):
    selenium.get("https://beta.rikstoto.no")
    selenium.find_element(By.CSS_SELECTOR, "product-menu").click()
    selenium.find_element(By.PARTIAL_LINK_TEXT , "Løpsoversikt").click()
    headings = selenium.find_elements(By.CSS_SELECTOR, "h3")
    assert any('Baneoversikt' in element.text for element in headings)
