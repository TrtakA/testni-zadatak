from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    def verify_page_title(self,title):
        title_tekst = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class ='title']")))
        assert title_tekst.text == title
    
    def test_standard_user_login(self):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.click()
        username_field.send_keys("standard_user")
        password_field = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.clear()
        password_field.click()
        password_field.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click() 

    def test_adding_to_cart(self):
        self.verify_page_title("PRODUCTS")
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart_button.click()
        shoping_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        shoping_cart_button.click()
        self.verify_page_title("YOUR CART")
        product_in_cart_1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id ='item_4_title_link']")))
        assert product_in_cart_1.text == "Sauce Labs Backpack"
        product_in_cart_2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id ='item_0_title_link']")))
        assert product_in_cart_2.text == "Sauce Labs Bike Light"
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

    def test_standard_user_info(self):
        self.verify_page_title("CHECKOUT: YOUR INFORMATION")
        first_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name_field.clear()
        first_name_field.click()
        first_name_field.send_keys("Alma")
        last_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        last_name_field.clear()
        last_name_field.click()
        last_name_field.send_keys("Trtak")
        zip_code_field = self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        zip_code_field.clear()
        zip_code_field.click()
        zip_code_field.send_keys("71000")
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def test_check_products(self):
        self.verify_page_title("CHECKOUT: OVERVIEW")
        product_tekst_1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id ='item_4_title_link']")))
        assert product_tekst_1.text == "Sauce Labs Backpack"
        product_tekst_2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id ='item_0_title_link']")))
        assert product_tekst_2.text == "Sauce Labs Bike Light"
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

    def test_menu_button(self):
        self.verify_page_title("CHECKOUT: COMPLETE!")
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        logout_link = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()

    def test_verify_loginPage(self):
        login_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id ='login-button']")))
        assert login_page.get_attribute("value") =="Login"


        time.sleep(5)
        self.driver.quit()
