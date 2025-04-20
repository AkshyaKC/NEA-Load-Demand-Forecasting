import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver=webdriver.Chrome()
base_url="https://www.nea.org.np/dailyOperationalReports"


driver.get(base_url)
WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-body')))

list_groups = driver.find_elements(By.CSS_SELECTOR, ".card-body .list-group")
pdf_links=[]

for group in list_groups:
    try:
        a_tag = group.find_element(By.TAG_NAME, "a")
        pdf_links.append(a_tag.get_attribute("href"))
    except:
        continue  # skip if <a> not found

driver.quit()
os.makedirs("pdfs", exist_ok=True)
for link in pdf_links:
    filename = link.split("/")[-1]
    filepath = os.path.join("pdfs", filename)
    try:
        response = requests.get(link)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
