import time
import pytest
from lib.pages.drag_drop_sliders import DragDropSliders
import os


@pytest.fixture(scope="function")
def setup_teardown(driver_data):
    driver, logger = driver_data
    pytest.test_pass = False
    yield driver, logger
    if not pytest.test_pass:
        logger.error("Teardown: Saving failure screenshot")
        driver.get_screenshot_as_file(os.path.join(os.getcwd(), "screenshots", os.path.basename(__file__).split(".")[0]+".png"))


def test_sliders_drag_drop(setup_teardown):
    """ Testcase to test drag and drop functionality of sliders"""

    driver, logger = setup_teardown

    logger.info("***** STEP1: Navigate to Drag and Drop slider section from Menu *****")
    drag_drop_sliders = DragDropSliders(driver)

    logger.info("***** STEP2: Set all sliders to 50% *****")
    all_sliders = drag_drop_sliders.get_slider_elements
    for index in range(1, len(all_sliders)+1):
        drag_drop_sliders.drag_drop_slider(index)

    logger.info("***** STEP3: Verify all sliders are at 50% *****")
    for index in range(1, len(all_sliders)+1):
        assert drag_drop_sliders.get_slider_output_value(index) == '50', f"Slider{str(index)} is not set at 50%"

    pytest.test_pass = True
