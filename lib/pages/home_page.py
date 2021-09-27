from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.wait = WebDriverWait(self.driver, 5)
        self.is_page_loaded()

    def is_page_loaded(self):
        try:
            if self.driver.find_element_by_id("at-cv-lightbox-header").is_displayed():
                self.driver.find_element_by_id("at-cv-lightbox-close").click()
        except:
            pass
        return self.driver.title and self.driver.execute_script("return document.readyState == 'complete'")

    def get_title_text(self):
        return self.driver.title

    @property
    def input_forms_element(self):
        return self.driver.find_element_by_xpath("//li[@class='tree-branch']//a[text()='Input Forms']")

    @property
    def ajax_form_submit_element(self):
        return self.driver.find_element_by_xpath("//li[@style='display: list-item;']//a[contains(text(),"
                                                 "'Ajax Form Submit')]")

    @property
    def date_pickers_element(self):
        return self.driver.find_element_by_xpath("//li[@class='tree-branch']//a[text()='Date pickers']")

    @property
    def jquery_date_picker_element(self):
        return self.driver.find_element_by_xpath("//li[@style='display: list-item;']//a[contains(text(),"
                                                 "'JQuery Date Picker')]")

    @property
    def progress_bars_sliders_element(self):
        return self.driver.find_element_by_xpath("//li[@class='tree-branch']//a[text()='Progress Bars & Sliders']")

    @property
    def bootstrap_progress_bar_element(self):
        return self.driver.find_element_by_xpath("//li[@style='display: list-item;']//a[contains(text(),"
                                                 "'Bootstrap Progress bar')]")

    @property
    def drag_drop_sliders_element(self):
        return self.driver.find_element_by_xpath("//li[@style='display: list-item;']//a[contains(text(),"
                                                 "'Drag & Drop Sliders')]")
    
    @property
    def alerts_modals_element(self):
        return self.driver.find_element_by_xpath("//li[@class='tree-branch']//a[text()='Alerts & Modals']")

    @property
    def windows_popup_modal_element(self):
        # return self.driver.find_element_by_link_text("./bootstrap-modal-demo.html")
        return self.driver.find_element_by_xpath("//li[@style='display: list-item;']//a[contains(text(),"
                                                 "'Window Popup Modal')]")

    @property
    def javascript_alerts_element(self):
        # return self.driver.find_element_by_link_text("./bootstrap-modal-demo.html")
        return self.driver.find_element_by_xpath("//li[@style='display: list-item;']//a[contains(text(),"
                                                 "'Javascript Alerts')]")

    @property
    def file_download_element(self):
        # return self.driver.find_element_by_link_text("./bootstrap-modal-demo.html")
        return self.driver.find_element_by_xpath("//li[@style='display: list-item;']//a[contains(text(),"
                                                 "'File Download')]")

    def click_menu_input_forms(self):
        self.input_forms_element.click()

    def click_ajax_form_submit(self):
        self.ajax_form_submit_element.click()

    def click_menu_date_pickers(self):
        self.date_pickers_element.click()

    def click_jquery_date_picker(self):
        self.jquery_date_picker_element.click()

    def click_progress_bars_sliders(self):
        self.progress_bars_sliders_element.click()

    def click_bootstrap_progress_bar(self):
        self.bootstrap_progress_bar_element.click()

    def click_drag_drop_sliders(self):
        self.drag_drop_sliders_element.click()

    def click_alerts_modals(self):
        self.alerts_modals_element.click()

    def click_windows_popup_modal(self):
        self.windows_popup_modal_element.click()

    def click_javascript_alerts(self):
        self.javascript_alerts_element.click()

    def click_file_download(self):
        self.file_download_element.click()





