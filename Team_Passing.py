from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://fbref.com/en/comps/9/Premier-League-Stats")


time.sleep(3)


table = driver.find_element(By.ID, "stats_squads_passing_for")


rows = table.find_elements(By.TAG_NAME, "tr")


with open("Team_Passing.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_values = [cell.text for cell in cells]

        
        if cell_values:
            writer.writerow(cell_values)

print("CSV saved as: Team_Passing.csv")


driver.quit()