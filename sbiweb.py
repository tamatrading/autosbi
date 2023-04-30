#selenium起動

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#gmail
from gmail import sendGmail

# 指定時間待機
import time
import re

# マウスやキーボード操作に利用
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

# セレクトボックスの選択に利用
from selenium.webdriver.support.ui import Select

#-----------------------------
#SBI証券の口座でIPOのBB申込を行なう
#-----------------------------
def sbiIpoOrder(driver, in_data):
    # サイトを開く
    driver.get("https://www.sbisec.co.jp/ETGate")
    time.sleep(3)

    # ユーザIDを入力
    userID = driver.find_element(by=By.NAME, value="user_id")
    userID.send_keys(in_data["g_username"])

    # パスワードを入力
    userpass = driver.find_element(by=By.NAME, value="user_password")
    userpass.send_keys(in_data["g_username"])

    # ログインをクリック
    login = driver.find_element(by=By.NAME, value="ACT_login")
    login.click()

    time.sleep(3)

    # name属性で指定
    try:
        moneyTag = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[1]/td[1]/div[2]/div[1]/div/div/div/div/table/tbody/tr/td[1]/span")
    except NoSuchElementException:
        tmp = driver.find_elements(by=By.XPATH, value="//b[contains(text(),'重要なお知らせ')]")
        if len(tmp) >= 1:
            ii = -1
        else:
            ii = -2
        return ii

    money = int(moneyTag.text.replace(",", ""))
    print(money)


