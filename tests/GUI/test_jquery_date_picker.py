import pytest
import os
from lib.pages.jquery_date_picker import JqueryDatePicker


@pytest.fixture(scope="function")
def setup_teardown(driver_data):
    driver, logger = driver_data
    pytest.test_pass = False
    yield driver, logger
    if not pytest.test_pass:
        logger.error("Teardown: Saving failure screenshot")
        driver.get_screenshot_as_file(os.path.join(os.getcwd(), "screenshots", os.path.basename(__file__).split(".")[0]+".png"))


def test_jquery_date_picker(setup_teardown):
    """Testcase to verify jquery date picker functionality"""
    driver, logger = setup_teardown

    logger.info("STEP 1: Launch Jquery date picker section")
    jquery_date_picker_page = JqueryDatePicker(driver)

    logger.info("STEP 2: Verify not able to set from and to date above/beyond entered date")
    jquery_date_picker_page.enter_month_date_in_picker("Sep", 24)
    jquery_date_picker_page.enter_month_date_in_picker("Oct", 24, "To")
    assert not jquery_date_picker_page.verify_given_date_enabled("Oct", 25), \
        "Able to provide from date beyond set to date"
    assert not jquery_date_picker_page.verify_given_date_enabled("Aug", 25, "To"), \
        "Able to enter to date earlier than from date"

    pytest.test_pass = True
