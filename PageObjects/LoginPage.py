from selenium import webdriver


class LoginPage:
    loginbtn_Click_xpath = "(//a[contains(.,'Login')])[1]"
    emailfield_send_id = "email"
    passfield_send_id = "password"
    dologinclick_xpath = "//button[contains(.,'Login')]"
    AccountAssert_xpath = "(//h4[contains(.,'Purna')])[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickloginbutton(self):
        self.driver.find_element_by_xpath(self.loginbtn_Click_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.emailfield_send_id).send_key(email)

    def setPasswoed(self, password):
        self.driver.find_element_by_id(self.passfield_send_id).send_key(password)

    def clickDologinbutton(self):
        self.driver.find_element_by_xpath(self.dologinclick_xpath).click()

    def loginAssert(self):
        self.driver.find_element_by_xpath(self.AccountAssert_xpath).gettext()
