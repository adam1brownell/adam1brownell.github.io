from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import re
import csv

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome()

driver = webdriver.Chrome(options=chrome_options)
# Google Maps URL
GOOGLE_MAPS_URL = "https://www.google.com/maps"

# Function to fetch coordinates
def get_coordinates(search_query):
    try:
        driver.get(GOOGLE_MAPS_URL)

        # Search for location
        search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "searchboxinput"))
        )
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # Wait for URL to contain coordinates
        WebDriverWait(driver, 5).until(lambda d: re.search(r"@[-.\d]+,[-.\d]+", d.current_url))
        current_url = driver.current_url

        # Extract latitude and longitude
        lat_long_match = re.search(r"@([-.\d]+),([-.\d]+)", current_url)
        if lat_long_match:
            return lat_long_match.group(1), lat_long_match.group(2)
    except Exception as e:
        print(f"Error fetching coordinates for '{search_query}': {e}")
    return "N/A", "N/A"

# Main Script
locations_file = "food121824.txt"
results = []

try:
    with open(locations_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                print(f"/bad entry, {len(parts)} parts/")
                continue  # Skip invalid lines

            name, city, neighborhood = parts
            query = f"{name} {city} {neighborhood}"
            # print(f"Looking up: {query}")

            lat, lng = get_coordinates(query)
            results.append({"name": name, "latitude": lat, "longitude": lng})
            print(f"Result: {name} -> {lat}, {lng}")

finally:
    driver.quit()

# Output final results
print("\nFinal Results:")
for result in results:
    print(f"{result['name']}, {result['latitude']}, {result['longitude']}")