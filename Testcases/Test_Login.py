import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://brandhook.com.bd/"
    email = "pg.purnoghosh@gmail.com"
    password = "11111111"

    def loginwith_Valid(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Login = LoginPage(self.driver)
        self.Login.clickloginbutton()
        self.Login.setEmail(self.email)
        self.Login.setPasswoed(self.password)
        self.Login.clickloginbutton()
