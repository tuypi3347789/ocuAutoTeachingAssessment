import time
import accountAndPassword
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("https://cc3.ocu.edu.tw/eval/student.php")

def openTab(self, url):
    self.execute_script("window.open('%s');" %url)
    self.switch_to.window(self.window_handles[1])

def clickRadio(self):
    radioInputs = self.find_elements_by_tag_name('input')
    textAreaArray = self.find_elements_by_tag_name('textarea')
    for item in textAreaArray:
        item.send_keys('老師上課認真，學習到非常多東西')
    for item in radioInputs:
        value = item.get_attribute('value')
        if value == '5':
            item.click()
def close_current_tab(self):
    self.close()
    self.switch_to.window(self.window_handles[0])



time.sleep(3)

button = driver.find_element_by_tag_name('a')
button.click()

time.sleep(3)

account = driver.find_element_by_id('pid')
password = driver.find_element_by_id('pwd')
account.send_keys(accountAndPassword.account)
password.send_keys(accountAndPassword.password)

loginButton = driver.find_element_by_id('ok')
loginButton.click()

time.sleep(3)

table = driver.find_element_by_tag_name('table')
array = table.find_elements_by_tag_name('a')

for item in array:
    val = item.get_attribute('href')
    openTab(driver, val)
    clickRadio(driver)
    sent = driver.find_element_by_id('ok')
    sent.click()
    close_current_tab(driver)
