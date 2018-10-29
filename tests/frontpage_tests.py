from selenium import webdriver

def test_find_raceday_timeline(selenium):
    selenium.get("https://beta.rikstoto.no")
    element = selenium.find_element_by_class_name("race-day-timeline__header__content__title")
    assert element.text == "Bane- og løpsoversikt"

def test_there_are_elements_in_the_timeline(selenium):
    '''Make a test that verifies that the timeline is not empty'''
    assert False

def test_can_navigate_via_top_menu_to_spill(selenium):
    '''
    Make a test that verifies that the user 
    is able to navigate from the frontpage 
    to the "spill"-page (via the top-manu "spill" -> "Løpsoversikt") and
    verify by finding the text "Baneoversikt" '''
    assert False