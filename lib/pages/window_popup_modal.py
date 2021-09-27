from lib.pages.home_page import HomePage


class WindowPopupModal(HomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.click_alerts_modals()
        self.click_windows_popup_modal()
        self.is_page_loaded()

    @property
    def follow_twitter_facebook_button_element(self):
        return self.driver.find_element_by_xpath("//div[@class='two-windows']/a[@title='Follow @seleniumeasy'] ")

    def click_follow_twitter_facebook_button(self):
        self.follow_twitter_facebook_button_element.click()

    def get_all_window_handles(self):
        return self.driver.window_handles, self.driver.current_window_handle

    def switch_and_get_title_of_window(self, element):
        self.driver.switch_to.window(element)
        return self.driver.title

