import time
from lib.pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC


class JavascriptAlerts(HomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.click_alerts_modals()
        self.click_javascript_alerts()
        self.is_page_loaded()

    @property
    def javascript_alert_box_click_element(self):
        return self.driver.find_element_by_xpath("//button[@class='btn btn-default' and contains(text(),'Click me!')]")

    def click_javascript_alert_box(self):
        self.javascript_alert_box_click_element.click()

    def verify_alert_is_shown(self):
        return self.wait.until(EC.alert_is_present())

    def close_alert(self):
        alert = self.driver.switch_to.alert
        time.sleep(10)
        alert.accept()



