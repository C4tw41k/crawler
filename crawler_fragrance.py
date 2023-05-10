import requests
from bs4 import BeautifulSoup

from selenium import webdriver

import openpyxl as op
import time


excelpath = "D:/aheadfour/Fragrance.xlsx"
book = op.load_workbook(excelpath)
sheet = book.active


driver=webdriver.Firefox()

for count in range(1,11):

    driver.get("https://www.fragrancenet.cn/category/1246.html?search=%7B%22page%22%3A"+ str(count) +"%2C%22cid%22%3A246%2C%22sort%22%3A%22top%22%2C%22attr%22%3A%7B%7D%7D")

    # driver.find_element_by_id("kw").send_keys('python 知识学堂')

    # driver.find_element_by_id("su").click()

    # test = driver.find_element_by_class_name("product-container")

    # driver.implicitly_wait(10)
    time.sleep(7)

    html = driver.execute_script("return document.documentElement.outerHTML")



    soup = BeautifulSoup(html, "html.parser")



    all_products = soup.find_all("div", attrs={"sel-id":"list-link-product"})



    for product in all_products:
        
        final_price = "$" + product.find("span", attrs={"role":"final-price"}).string

        try:
            p_off = product.find("span", attrs={"class":"p-off"}).string
        except:
            p_off = "无折扣"

        name = product.find("div", attrs={"class":"m-product-name cls-product-no-tags"}).string

        data = final_price, p_off, name

        sheet.append(data)

    book.save(excelpath)










    

