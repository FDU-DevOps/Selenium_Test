import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
df = pd.read_csv(r"C:\Users\###\Test_Case_Sheet.csv")  # Location of the Test Case Sheet and creates data frame
for i in range(0, len(df)):
 Column_value = df.loc[i , 'Columns'] + 1 #extract Column Numbers
 Row_value = df.at[i, 'Rows'] + 1 #extract Row Numbers
 urls = [
    'http://localhost:8090/battleship/'  # Host website for JAR
 ]
 s = Service(r"C:\Users\####\chromedriver.exe") # Location of the Chrome Driver
 for url in urls:
    driver = webdriver.Chrome(service=s) 
    driver.get(url) # Runs Chromedriver and goes to host website
 time.sleep(5)
 for J in range(2, 7):
     full_xpath = "/html/body/div[2]/div[1]/div/table/tbody/tr["+ str(J) +"]/td[1]" #clicks button for opening move
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
  if Column_value == 13:#Ends loop
     break
  for N in range(1, Row_value): #Ends loop
    if Row_value == 12:
     break
    full_xpath = "/html/body/div[2]/div[2]/div/table/tbody/tr["+ str(M) +"]/td["+str(N)+"]"#clicks on a location of the battleship map
    driver.find_element(By.XPATH, full_xpath).click()
    time.sleep(1)
    element = driver.find_element(By.XPATH,"/html/body/div/div[2]/p")
    outer_html_result = element.get_attribute("outerHTML")
    comp_element = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/p")
    comp_outer_html_result = comp_element.get_attribute("outerHTML")
    if "Miss!" in outer_html_result:  # sees if user misses ship
     Miss = Miss + 1
    if "Hit!" in outer_html_result:  # sees if user hits ship
     Hits = Hits + 1
     Hit_Cord = str(chr(ord('@')+N))+ str(M-1)
     Hit_Areas =  Hit_Areas + Hit_Cord + " "
    if "sunk!" in outer_html_result: # sees if user hits and sun a ship
     Sunk  = Sunk  + 1
     Hits = Hits + 1
     Hit_Cord = str(chr(ord('@')+N))+ str(M-1)
     Hit_Areas =  Hit_Areas + Hit_Cord + " "
    if "hit" in comp_outer_html_result or "sunk!" in comp_outer_html_result: # sees if comuputer hits user's ship
     Comp_Hits = Comp_Hits + 1
    time.sleep(1)
    try:
     element = driver.find_element(By.ID, "guesses-left")
     outer_html = element.get_attribute("outerHTML")
     element2 = driver.find_element(By.ID, "message")
     outer_html2 = element2.get_attribute("outerHTML")
     if "Guesses left: 0" in outer_html or "win!" in outer_html2 or "lose!" in outer_html2 : # when game is over 
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
      df.at[i,"Total Hits"] = Hits #adds column to testing sheet
      df.at[i,"Total Misses"] = Miss #adds column to testing sheet
      df.at[i,"Total Ships Sunk"] = Sunk #adds column to testing sheet
      df.at[i,"Total Hits Taken"] = Comp_Hits #adds column to testing sheet
      df.at[i,"Hit Areas"] = Hit_Areas #adds column to testing sheet
      df.to_csv('output.csv', encoding='utf-8', index=False) #Updates testing sheet
      break
    except:
     time.sleep(5)
 print("Loop #" + str(i + 1) + " Is Completed")
 print(df) # prints out dataframe
 driver.quit()
print(df)
df.to_csv(r"C:\Users\####\Test_Case_Sheet.csv", index=False) # Location of the Test Case Sheet
print("Test over ")
