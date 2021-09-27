import time

from lib.pages.home_page import HomePage
from selenium.webdriver.common.action_chains import ActionChains


class DragDropSliders(HomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.click_progress_bars_sliders()
        self.click_drag_drop_sliders()
        self.is_page_loaded()
        self.action_chain = ActionChains(driver)
        self.json_values = {"slider1": {"input": "range", "output": "range"},
                            "slider2": {"input": "range range-primary", "output": "rangePrimary"},
                            "slider3": {"input": "range range-success", "output": "rangeSuccess"},
                            "slider4": {"input": "range range-info", "output": "rangeInfo"},
                            "slider5": {"input": "range range-warning", "output": "rangeWarning"},
                            "slider6": {"input": "range range-danger", "output": "rangeDanger"}}

    @property
    def get_slider_elements(self):
        return self.driver.find_elements_by_xpath("//div[contains(@id,'slider')]")

    def get_slider_input_element(self, num):
        data = self.json_values["slider"+str(num)]["input"]
        return self.driver.find_element_by_xpath(f"//div[@class='{data}']/input[@type='range']")

    def get_slider_output_element(self, num):
        data = self.json_values["slider"+str(num)]["output"]
        return self.driver.find_element_by_id(data)

    def drag_drop_slider(self, slider):
        self.get_slider_input_element(slider)
        self.action_chain.drag_and_drop_by_offset(self.get_slider_input_element(slider), 0, 0).perform()

    def get_slider_output_value(self, slider):
        return self.get_slider_output_element(slider).text
