import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import info
from selenium.webdriver.common.action_chains import ActionChains
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'

options = Options()
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument(f'user-agent={user_agent}')
#options.add_argument("--remote-debugging-port=9222")
#options.add_argument("--headless")
#chrome_options.binary_location = (r"C:\Users\dkael\AppData\Local\Google\Chrome SxS\Application\chrome.exe")
#chrome_options.add_argument('start-maximized')


def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper
@timeme

def bot(k):

    i = 0
    while i < 5:
        running = True
        while running:
            try:
                driver = webdriver.Chrome(executable_path="/home/davekaesen/PycharmProjects/nikebot/chromedriver", options=options)
                wait = WebDriverWait(driver, 10)
                driver.get(k["product_url"])
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'US M 10.5 / W 12')]"))).click()
                element = driver.find_element_by_xpath("//button[@class='ncss-brand ncss-btn-black pb3-sm prl5-sm pt3-sm u-uppercase u-full-width']")
                action = ActionChains(driver)
                action.move_to_element(element).double_click().perform()
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div")))
                driver.get(k["product_cart"])
                print("Adding to bag --- Successful")
                running = False

            except:
                driver.quit()
                i = i + 1
                if i == 5:
                    print("MAX TRIES --- Aborting Operation")
                    running = False
                else:
                    running = True
                    print("TRY --- " + str(i))
            else:
                i = 5
                print("Successful Operation!")



    print("Operation Finished")
    driver.quit()
    '''
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='css-1agp7ao e1tnxv7e4'][contains(text(),'Guest Checkout')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Shipping_FirstName"]'))).send_keys(k["FirstName"])
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Shipping_LastName"]'))).send_keys(k["LasteName"])
    driver.find_element_by_xpath('//*[@id="Shipping_Address1"]').send_keys(k["Address"])
    driver.find_element_by_xpath('//*[@id="Shipping_Address3"]').send_keys(k["City"])
    driver.find_element_by_xpath('//*[@id="Shipping_PostCode"]').send_keys(k["Postal"])
    driver.find_element_by_xpath('//*[@id="Shipping_phonenumber"]').send_keys(k["ShippingPhone"])
    driver.find_element_by_xpath('//*[@id="shipping_Email"]').send_keys(k["Email"])
    driver.find_element_by_xpath('//*[@id="gdprSection"]/div[1]/label[1]/span').click()
    driver.find_element_by_xpath('//*[@id="shippingSubmit"]').click()
    driver.find_element_by_xpath('//*[@id="billingSubmit"]').click()
    driver.save_screenshot("test2.png")

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="paymentIFrame"]')))
    wait.until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "CreditCardHolder"]'))).send_keys(k["cardname"])
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="KKnr"]'))).send_keys(k["creditcrdno"])
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="KKMonth"]/option[4]'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "KKYear"] / option[6]'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "CCCVC"]'))).send_keys(k["cvv"])
    wait.until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "BtnPurchase"]'))).click()
    driver.save_screenshot("test3.png")
    driver.quit()
    '''

if __name__ == '__main__':
    bot(info)


