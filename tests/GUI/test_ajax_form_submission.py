import pytest
import os
from lib.pages.ajax_form_submit import AjaxFormSubmit


@pytest.fixture(scope="function")
def setup_teardown(driver_data):
    driver, logger = driver_data
    pytest.test_pass = False
    yield driver, logger
    if not pytest.test_pass:
        logger.error("Teardown: Saving failure screenshot")
        driver.get_screenshot_as_file(os.path.join(os.getcwd(), "screenshots",
                                                   os.path.basename(__file__).split(".")[0]+".png"))


def test_ajax_form_submission(setup_teardown):
    """ Testcase to check if loading spinner and success message is shown while submitting ajax form"""

    driver, logger = setup_teardown

    logger.info("STEP 1: Launch url and navigate to Ajax form submit section")
    ajax_form_page = AjaxFormSubmit(driver)

    logger.info("STEP 2: Enter name and comment in form and submit")
    ajax_form_page.enter_name("Anushiya")
    ajax_form_page.enter_comment("Automation Framework development")
    ajax_form_page.click_form_submit_button()

    logger.info("STEP 3: Verify loading spinner is shown")
    assert ajax_form_page.is_loading_spinner_shown(), "Loading spinner not available"

    logger.info("STEP 4: Verify success message is shown")
    assert ajax_form_page.success_message_displayed(), "Success message is not seen"

    pytest.test_pass = True
