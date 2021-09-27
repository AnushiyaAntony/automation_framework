import time
import pytest
import os
from lib.pages.window_popup_modal import WindowPopupModal


@pytest.fixture(scope="function")
def setup_teardown(driver_data):
    driver, logger = driver_data
    pytest.test_pass = False
    yield driver, logger
    if not pytest.test_pass:
        logger.error("Teardown: Saving failure screenshot")
        driver.get_screenshot_as_file(os.path.join(os.getcwd(), "screenshots",
                                                   os.path.basename(__file__).split(".")[0]+".png"))


def test_multiple_window_popup_modal(setup_teardown):
    """Testcase to verify multiple popups shown"""
    driver, logger = setup_teardown

    logger.info("STEP 1: Launch window popup modal section")
    window_popup_page = WindowPopupModal(driver)

    logger.info("STEP 2: Verify 2 popups are present")
    window_popup_page.click_follow_twitter_facebook_button()
    all_windows, current_window = window_popup_page.get_all_window_handles()
    all_windows.remove(current_window)
    assert len(all_windows) == 2, "Popups are not equal to 2"

    logger.info("STEP 3: Log the title of popups and test page")
    for window in all_windows:
        title = window_popup_page.switch_and_get_title_of_window(window)
        logger.info(f"Page of popup window is {title}")
    title = window_popup_page.switch_and_get_title_of_window(current_window)
    logger.info(f"Page of test page is {title}")

    pytest.test_pass = True
