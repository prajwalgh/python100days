from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path="C:\devlopmentAppBr\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.in/gp/product/B08372ZPVS/ref=ewc_pr_img_1?smid=A14CZOWI0VEHLG&psc=1")
#driver.get("https://selenium-python.readthedocs.io/locating-elements.html")
#price=driver.find_elements_by_class_name("a-offscreen")
#price=driver.find_element(By.CLASS_NAME, "a-offscreen")
price=driver.find_element(By.CLASS_NAME,"a-price-whole")
print(price.text)
print("this is working")



#this is not working in current version
#xPathExample=driver.find_element_by_xpath('//*[@id="navFooter"]/div[4]/ul/li[17]/a')
xPathExample=driver.find_element(By.XPATH,'//*[@id="navFooter"]/div[4]/ul/li[17]/a')

print(xPathExample.text)
##stops a tab on browser
driver.close()
#close chrome
driver.quit()