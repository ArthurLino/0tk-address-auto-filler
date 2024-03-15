import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(options=opt)

# Colocar os ceps das ruas aqui
addresses = [
    "13294380",
    "13293150",
    "13290438",
    "13291434",
    "13290220",
    "13290038",
    "13294384",
    "13293010",
    "13293272",
    "13294334",
    "13290546",
    "13291004",
    "13294422",
    "13290020",
    "13294382",
    "13294392",
    "13294426",
    "13294424",
    "13294104",
    "13294504",
    "13294530",
    "13294620",
    "13294614",
    "13294600",
    "13294008",
    "13294102",
    "13294412",
    "13294400",
    "13294512",
    "13294362",
    "13294142",
    "13294148",
    "13294152",
    "13294150",
    "13294154",
    "13290330",
    "13294260",
    "13294100",
    "13291700",
    "13294219",
    "13294358",
    "13294350",
    "13294200",
    "13291006",
    "13294418"
]

for ad in addresses:

    try:
        i_date = [int(i) for i in "01092019"]
        e_date = [int(i) for i in "23082022"]

        cep = driver.find_element(By.NAME, "ctl00$ctl00$MainContent$ChildContent$UIMSKCEP")

        for _ in range(10):
            cep.send_keys(Keys.ARROW_LEFT)

        cep.send_keys(int(ad))
        cep.send_keys(Keys.TAB)

        time.sleep(2)

        comp = driver.find_element(By.NAME, "ctl00$ctl00$MainContent$ChildContent$txtCOMPLEMENTO")
        comp.send_keys("TODA EXTENSÃO")

        init_date = driver.find_element(By.NAME, "ctl00$ctl00$MainContent$ChildContent$txtDT_INICIO")
        for _ in range(10):
            init_date.send_keys(Keys.ARROW_LEFT)

        for e in range(len(i_date)):
            init_date.send_keys(i_date[e])

        end_date = driver.find_element(By.NAME, "ctl00$ctl00$MainContent$ChildContent$txtDT_PREV_TERMINO")
        for _ in range(10):
            end_date.send_keys(Keys.ARROW_LEFT)

        for e in range(len(e_date)):
            end_date.send_keys(e_date[e])

        sel = driver.find_element(By.NAME, "ctl00$ctl00$MainContent$ChildContent$ddlCD_FINAL")
        sel.send_keys("infraestrutura")

        continue_btn = driver.find_element(By.NAME, "ctl00$ctl00$MainContent$ChildContent$imbAdicionarObraServicoRodape")
        continue_btn.click()

        time.sleep(2)

    except:
        print(f"erro at: {ad}")
