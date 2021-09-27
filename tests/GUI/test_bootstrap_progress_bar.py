import time
from lib.pages.bootstrap_progress_bar import BootstrapProgressBar


def test_bootstrap_progress_bar(driver_data):
    """Testcase to log time taken for download using progress bar percentage"""

    driver, logger = driver_data

    logger.info("STEP 1: Navigate to Bootstrap progress bar section")
    progress_bar = BootstrapProgressBar(driver)

    logger.info("STEP 2: Click on submit")

    progress_bar.click_submit_button()
    logger.info("STEP 3: Log time taken for download")

    initial_time = time.time()
    percentage = 0
    while int(percentage) < 100:
        percentage = progress_bar.get_percentage_text()
        logger.info(f"Percentage downloaded is {percentage}")
        time.sleep(2)
    final_time = time.time()
    time_taken = int(final_time - initial_time)
    logger.info(f"Total time taken for download is {time_taken} seconds")
