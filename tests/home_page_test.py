from pages.homePage import HomePage

def test(driver):
    homePage = HomePage(driver)
    homePage.go_to("https://www.saucedemo.com/")
    homePage.test_standard_user_login()
    homePage.test_adding_to_cart()
    homePage.test_standard_user_info()
    homePage.test_check_products()
    homePage.test_menu_button()
    homePage.test_verify_loginPage()