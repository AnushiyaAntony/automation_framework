import time
import pytest
from lib.pages.file_download import FileDownload
import os


@pytest.fixture(scope="function")
def setup_teardown(driver_data):
    driver, logger = driver_data
    pytest.test_pass = False
    yield driver, logger
    if not pytest.test_pass:
        logger.error("Teardown: Saving failure screenshot")
        driver.get_screenshot_as_file(os.path.join(os.getcwd(), "screenshots",
                                                   os.path.basename(__file__).split(".")[0]+".png"))


def test_content_in_downloaded_file(setup_teardown):
    """Testcase to verify the data entered in UI is same as the content of downloaded file"""

    driver, logger = setup_teardown
    downloads = os.path.join(os.getcwd(), "downloads")

    logger.info("STEP 1: Navigate to file download section")
    file_download_page = FileDownload(driver)

    logger.info("STEP 2: Enter content in text box")
    data_entered = "Automation Framework Development"
    file_download_page.enter_given_data(data_entered)

    logger.info("STEP 3: Generate and download the file")
    file_download_page.click_generate_file()
    file_download_page.click_download()
    time.sleep(10)  # wait for download

    logger.info("STEP 4: Verify content in downloaded file is same as given in GUI")
    file_path = os.path.join(downloads, "easyinfo.txt")
    with open(file_path) as f:
        contents = f.readlines()
    os.remove(file_path)
    assert contents[0] == data_entered, "Content is not same"
    pytest.test_pass = True
