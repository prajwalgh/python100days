#TODO print element from li tag and a tag inside a div and create a dictionary
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path="C:\devlopmentAppBr\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.python.org/")#[@id="content"]div/section/div[3]/div[2]/div/ul/li[1]/time/text()
GetTime=driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
GetName=driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')
a=[]
b=[]
for i in range(len(GetTime)):
    a.append(GetTime[i].text)
for i in range(len(GetName)):
    b.append(GetName[i].text)
print(a)
print(b)
dic1=dict()
j=0
for i in range(len(a)):
    dic1[j]={"time":a[i],"name":b[i]}
    j+=1
print(dic1)

#stops a tab on browser
driver.close()
#close chrome
driver.quit()

