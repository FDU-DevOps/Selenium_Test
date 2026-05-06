import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
df = pd.read_csv(r"C:\Users\antma\Documents\Test_Case_Sheet.csv")
for i in range(0, len(df)):
 Column_value = df.loc[i , 'Columns'] + 2
 Row_value = df.at[i, 'Rows'] + 1
 urls = [
    'http://localhost:8090/battleship/'
 ]
 s = Service(r"C:\Users\antma\Downloads\chromedriver-win32\chromedriver.exe")
 for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)
 time.sleep(5)
 for J in range(2, 7):
     full_xpath = "/html/body/div[2]/div[1]/div/table/tbody/tr["+ str(J) +"]/td[1]"
     driver.find_element(By.XPATH, full_xpath).click()
     time.sleep(1)
 full_xpath = "/html/body/div[1]/button[2]"
 driver.find_element(By.XPATH, full_xpath).click()
 time.sleep(5)
 Hits = 0
 Miss = 0
 Sunk = 0
 Comp_Hits = 0
 Hit_Areas = " "
 for M in range(2, Column_value):
  if Column_value == 13:
     break
  for N in range(1, Row_value):
    if Row_value == 12:
     break
    full_xpath = "/html/body/div[2]/div[2]/div/table/tbody/tr["+ str(M) +"]/td["+str(N)+"]"
    driver.find_element(By.XPATH, full_xpath).click()
    time.sleep(1)
    element = driver.find_element(By.XPATH,"/html/body/div/div[2]/p")
    outer_html_result = element.get_attribute("outerHTML")
    comp_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/p")
    comp_outer_html_result = comp_element.get_attribute("outerHTML")
    if "Miss!" in outer_html_result:
     Miss = Miss + 1
    if "Hit!" in outer_html_result:
     Hits = Hits + 1
     Hit_Cord = str(chr(ord('@')+N))+ str(M-1)
     Hit_Areas =  Hit_Areas + Hit_Cord + " "
    if "sunk!" in outer_html_result:
     Sunk  = Sunk  + 1
     Hits = Hits + 1
     Hit_Cord = str(chr(ord('@')+N))+ str(M-1)
     Hit_Areas =  Hit_Areas + Hit_Cord + " "
    if "hit" in comp_outer_html_result or "sunk!" in comp_outer_html_result:
     Comp_Hits = Comp_Hits + 1
    time.sleep(1)
    try:
     element = driver.find_element(By.ID, "guesses-left")
     outer_html = element.get_attribute("outerHTML")
     element2 = driver.find_element(By.ID, "message")
     outer_html2 = element2.get_attribute("outerHTML")
     if "Guesses left: 0" in outer_html or "win!" in outer_html2 or "lose!" in outer_html2 :
      print("No More Guesses")
      Column_value = 13
      Row_value = 12
      print ("Total Hits:")
      print (Hits)
      print ("Total Hit Areas")
      print (Hit_Areas)
      print ("Total Misses:")
      print (Miss)
      print ("Total Ships Sunk:")
      print (Sunk)
      print ("Total Hits Taken:")
      print (Comp_Hits)
      df.at[i,"Total Hits"] = Hits 
      df.at[i,"Total Misses"] = Miss
      df.at[i,"Total Ships Sunk"] = Sunk
      df.at[i,"Total Hits Taken"] = Comp_Hits
      df.at[i,"Hit Areas"] = Hit_Areas
      df.to_csv('output.csv', encoding='utf-8', index=False)
      break
    except:
     time.sleep(5)
 print("Loop #" + str(i + 1) + " Is Completed")
 print(df)
 driver.quit()
print(df)
df.to_csv(r"C:\Users\antma\Documents\Test_Case_Sheet.csv", index=False)
print("Test over ")