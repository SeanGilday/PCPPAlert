from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# main method
def main():
    # url = input("Paste the URL the parts list you want to track\n")
    url = "https://pcpartpicker.com/user/SeanGilday/saved/#view=Dzps8d"
    scrape(url)

# scrape the webpage for parts
def scrape(url: str):
    driver = webdriver.Chrome()
    driver.get("https://pcpartpicker.com/user/SeanGilday/saved/#view=Dzps8d")
    driver.implicitly_wait(0.5)

    items = driver.find_elements(by=By.CLASS_NAME, value="td__name")
    prices = driver.find_elements(by=By.CLASS_NAME, value="td__price")
    total = float(prices[-1].text[1:])

    shoppingList = dict()
    for x in range(len(items)):
        try:
            shoppingList[items[x].text] = float(prices[x].text[1:])
        except:
            shoppingList[items[x].text] = 0
    
    driver.quit()

# check price of part
def checkPrice():
    return

# send mail notification to user
def sendMail():
    return

if __name__ == "__main__":
    main()