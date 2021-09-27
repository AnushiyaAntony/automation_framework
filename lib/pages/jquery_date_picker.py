from lib.pages.home_page import HomePage
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class JqueryDatePicker(HomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.click_menu_date_pickers()
        self.click_jquery_date_picker()
        self.is_page_loaded()

    @property
    def from_date_element(self):
        return self.driver.find_element_by_id("from")

    @property
    def to_date_element(self):
        return self.driver.find_element_by_id("to")

    @property
    def select_month_element(self):
        return Select(self.driver.find_element_by_xpath("//*[@data-handler='selectMonth']"))

    def find_date_element(self, date):
        return self.driver.find_element_by_xpath(f"//td[@data-handler='selectDay']/a[text()={date}]")

    def click_from_date(self):
        self.from_date_element.click()

    def click_to_date(self):
        self.to_date_element.click()

    def click_selected_date(self, date):
        self.find_date_element(date).click()

    def select_month_date_in_picker(self, month, date):
        self.select_month_element.select_by_visible_text(month)
        self.click_selected_date(date)

    def open_date_picker(self, date_type):
        if date_type == "From":
            self.click_from_date()
        else:
            self.click_to_date()

    def enter_month_date_in_picker(self, month, date, date_type="From"):
        self.open_date_picker(date_type)
        self.select_month_date_in_picker(month, date)

    # def enter_from_date(self,month,date):
    #     self.click_from_date()
    #     self.select_month_date_in_picker(month, date)
    #
    # def enter_to_date(self, month, date):
    #     self.click_to_date()
    #     self.select_month_date_in_picker(month, date)

    def verify_given_date_enabled(self, month, date, date_type="From"):
        self.open_date_picker(date_type)
        try:
            self.select_month_element.select_by_visible_text(month)
            self.click_selected_date(date)
            return True
        except NoSuchElementException:
            return False






