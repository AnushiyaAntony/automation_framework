from lib.pages.home_page import HomePage


class BootstrapProgressBar(HomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.click_progress_bars_sliders()
        self.click_bootstrap_progress_bar()
        self.is_page_loaded()

    @property
    def submit_button_element(self):
        return self.driver.find_element_by_id("cricle-btn")

    @property
    def percentage_element(self):
        return self.driver.find_element_by_xpath("//div[@class='percenttext']")

    def click_submit_button(self):
        return self.submit_button_element.click()

    def get_percentage_text(self):
        percentage = self.percentage_element.text
        return percentage.split("%")[0]

