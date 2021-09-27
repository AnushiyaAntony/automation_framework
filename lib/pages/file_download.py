from lib.pages.home_page import HomePage


class FileDownload(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.click_alerts_modals()
        self.click_file_download()
        self.is_page_loaded()

    @property
    def text_data_element(self):
        return self.driver.find_element_by_id("textbox")

    @property
    def generate_file_element(self):
        return self.driver.find_element_by_id("create")

    @property
    def download_element(self):
        return self.driver.find_element_by_id("link-to-download")

    def enter_given_data(self, test_data):
        self.text_data_element.send_keys(test_data)

    def click_generate_file(self):
        # self.wait.until(EC.element_to_be_clickable(self.generate_file_element).click())
        self.generate_file_element.click()

    def click_download(self):
        self.download_element.click()
