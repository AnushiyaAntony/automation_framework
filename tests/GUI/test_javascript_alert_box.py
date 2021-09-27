import time
import pytest
import os
from lib.pages.javascript_alerts import JavascriptAlerts


@pytest.fixture(scope="function")
def setup_teardown(driver_data):
    driver, logger = driver_data
    pytest.test_pass = False
    yield driver, logger
    if not pytest.test_pass:
        logger.error("Teardown: Saving failure screenshot")
        driver.get_screenshot_as_file(os.path.join(os.getcwd(), "screenshots",
                                                   os.path.basename(__file__).split(".")[0]+".png"))


def test_javascript_alert_box(setup_teardown):
    """Testcase to verify javascript alert box is shown"""

    driver, logger = setup_teardown

    logger.info("STEP 1: Navigate to javascript alerts section")
    javascript_alert_page = JavascriptAlerts(driver)

    logger.info("STEP 2: Click alert box and verify alert is shown")
    javascript_alert_page.click_javascript_alert_box()
    assert javascript_alert_page.verify_alert_is_shown(), "Alert is not present in UI"
    javascript_alert_page.close_alert()

    pytest.test_pass = True

