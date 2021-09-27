from selenium.webdriver.support import expected_conditions as EC
from lib.pages.home_page import HomePage


class AjaxFormSubmit(HomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.click_menu_input_forms()
        self.click_ajax_form_submit()
        self.is_page_loaded()


    @property
    def form_name_element(self):
        return self.driver.find_element_by_id("title")

    @property
    def form_comment_element(self):
        return self.driver.find_element_by_id("description")

    @property
    def form_submit_element(self):
        return self.driver.find_element_by_name("btn-submit")

    @property
    def spinner_element(self):
        return self.driver.find_element_by_xpath("//img[@src='LoaderIcon.gif']")

    @property
    def success_message_element(self):
        # return self.driver.find_element_by_xpath("//div[contains(text(),'submited Successfully')]")
        return self.driver.find_element_by_id('submit-control')

    def enter_name(self, name):
        self.form_name_element.send_keys(name)

    def enter_comment(self, description):
        self.form_comment_element.send_keys(description)

    def click_form_submit_button(self):
        self.form_submit_element.click()

    def is_loading_spinner_shown(self):
        return EC.visibility_of_element_located((self.spinner_element))

    def success_message_displayed(self):
        return self.success_message_element.is_displayed()
