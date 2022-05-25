import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
def sell(driver,i):
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div:nth-child(29) > div > div > div > div.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.gWXeYL.jYqxGr > button > i")))
        driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(29) > div > div > div > div.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.gWXeYL.jYqxGr > button > i").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Sell']")))
        driver.find_element(By.XPATH, "//*[text() = 'Sell']").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, 'price')))
        driver.find_element(By.NAME, 'price').send_keys(raa(a))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Complete listing']")))
        driver.find_element(By.XPATH, "//*[text() = 'Complete listing']").click()
        WebDriverWait(driver, 30).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Подписать']")))
        driver.find_element(By.XPATH, "//*[text() = 'Подписать']").click()
        driver.switch_to.window(driver.window_handles[0])
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'View Item']")))
    except NoSuchElementException:
        print("продажа нет кнопки",i)
        return
    except ElementClickInterceptedException:
        print("продажа кликнул",i)
        return
    except TimeoutException:
        print("продажа время",i)
        return
    return

def addpic(driver,i,a1):
    try:
        b = text_file2.readline()
        c = b[:b.find(")"):]
        b = b[b.find(")") + 1:]
        b = list(map(str, b.split("_")))
        driver.get('https://opensea.io/asset/create')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(((By.ID, 'collection'))))
        driver.find_element(By.ID, 'collection').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(((By.XPATH, "//*[text() = 'Dangerous Octopuses Club']"))))
        driver.find_element(By.XPATH, "//*[text() = 'Dangerous Octopuses Club']").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(((By.ID, 'name'))))
        driver.find_element(By.ID, 'name').send_keys("dangerous octopus№"+c)
        driver.find_element(By.ID, 'description').send_keys("Dangerous octopuses are 9999 unique octopuses living in the blockchain world. They seek to undermine the foundations of society. If you keep more dangerous octopuses, then your gang will be stronger. Dangerous octopuses rule the world!")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(((By.XPATH, "//*[text() = 'add']"))))
        driver.find_element(By.XPATH, "//*[text() = 'add']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add more']").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/section/table/tbody/tr/td[1]/div/div/input").send_keys(a1[0])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[2]/td[1]/div/div/input").send_keys(a1[1])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[3]/td[1]/div/div/input").send_keys(a1[2])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[4]/td[1]/div/div/input").send_keys(a1[3])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[5]/td[1]/div/div/input").send_keys(a1[4])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[6]/td[1]/div/div/input").send_keys(a1[5])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[7]/td[1]/div/div/input").send_keys(a1[6])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[8]/td[1]/div/div/input").send_keys(a1[7])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[9]/td[1]/div/div/input").send_keys(a1[8])


        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[1]/td[2]/div/div/input").send_keys(b[0])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[2]/td[2]/div/div/input").send_keys(b[1])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[3]/td[2]/div/div/input").send_keys(b[2])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[4]/td[2]/div/div/input").send_keys(b[3])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[5]/td[2]/div/div/input").send_keys(b[4])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[6]/td[2]/div/div/input").send_keys(b[5])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[7]/td[2]/div/div/input").send_keys(b[6])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[8]/td[2]/div/div/input").send_keys(b[7])
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/section/table/tbody/tr[9]/td[2]/div/div/input").send_keys(b[8])

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(((By.XPATH, "//*[text() = 'Save']"))))
        driver.find_element(By.XPATH, "//*[text() = 'Save']").click()
        driver.find_element(By.ID, 'media').send_keys('C:/Users/danmo/Desktop/nft/' + c + '.png')
        driver.find_element(By.ID, 'chain').click()
        driver.execute_script("window.scrollTo (0, document.body.scrollHeight); ")
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div/form/div[9]/div[1]/span/button').click()
        time.sleep(7)
    except NoSuchElementException:
        print("добавление нет кнопки",c)
        return
    except ElementClickInterceptedException:
        print("добавление кликнул",c)
        return
    except TimeoutException:
        print("добавление время",c)
        return
    return
def raa(a):
    return a[random.randint(0,2)]
a = ["0.002","0.003","0.004"]


options = webdriver.ChromeOptions()
#options.add_argument(f"--user-data-dir=C:\\Users\\danmo\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_extension(r"C:\Users\danmo\PycharmProjects\pythonProject1\metamaskExtension.crx")
chrome_driver_binary = r'C:\bin\chromedriver.exe'
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
chromedriver = ChromeDriverManager(chrome_type=ChromeType.GOOGLE, log_level=0, print_first_line=False).install()
driver = webdriver.Chrome(chromedriver, options=options,service_log_path=None)

time.sleep(2)
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div/div/button').click()
driver.find_element(By.XPATH,"//*[text() = 'Импортировать кошелек']").click()
driver.find_element(By.XPATH,"//*[text() = 'Я согласен']").click()
time.sleep(2)
inputs = driver.find_elements(By.XPATH,'//input')
inputs[0].send_keys("")
inputs[1].send_keys("")
inputs[2].send_keys("")
driver.find_element(By.CSS_SELECTOR,'.first-time-flow__terms').click()
driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div/form/button').click()
time.sleep(1)
driver.get('https://opensea.io')
WebDriverWait(driver, 30).until(EC.element_to_be_clickable(((By.XPATH, "//*[text() = 'account_balance_wallet']"))))
driver.find_element(By.XPATH,"//*[text() = 'account_balance_wallet']").click()
text_file2 = open('C:/Users/danmo/Desktop/nft/ListId.txt','r')
text_file2.readline()
a1 = list(map(str, text_file2.readline().split()))
if 4 == int(input()):
    for i in range(0, 200):
        for i in range(0,10):
            addpic(driver,i,a1)
            sell(driver,i)

        time.sleep(3)


