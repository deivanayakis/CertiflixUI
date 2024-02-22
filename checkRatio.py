import os
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/kristy-solid-wood-almirah/p/itm4b57b1e1702bc?pid=CUPGUGYHYPURYY7Z&lid=LSTCUPGUGYHYPURYY7ZDUQFTC&marketplace=FLIPKART&q=almirah&store=wwe%2Ffc3%2Fdsw&srno=s_1_1&otracker=AS_QueryStore_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_7_na_na_na&fm=search-autosuggest&iid=en_5StWB1WCXvf6KMjjI01qlB1tOMqx4l2-_c_otwYaInSIQGq1bIOSw6L1kwJG8AvseaEGQzy0Yn-OWA7j3pcAnA%3D%3D&ppt=sp&ppn=sp&qH=845f0f712e418841"

# Set up the Selenium webdriver in headless mode with a specified user-agent for Chrome
options = webdriver.ChromeOptions()
options.add_argument("headless")  # Run Chrome in headless mode
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(options=options)

# Load the webpage
driver.get(url)

# Wait for the page to load (you might need to adjust the waiting time)
driver.implicitly_wait(10)

# Get the page source after it has been dynamically loaded
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the 'table' tags with the appropriate class
tables = soup.find_all('table', class_='_14cfVK')
target_table_index = None
for index, table in enumerate(tables):
    if "Width" in table.text and "Height" in table.text:
        target_table_index = index
        break

# Extract the width and height from the identified table
if target_table_index is not None:
    target_table = tables[target_table_index]

    # Find all rows in the table
    rows = target_table.find_all('tr')

    width1 = None
    height1 = None
 # Iterate through the rows to find width and height
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            attribute = cells[0].text.strip()
            value = cells[1].text.strip()

            if attribute.lower() == "width":
                width1 = value
            elif attribute.lower() == "height":
                height1 = value
        
        else:
            print("Target table not found.")
    print("Width:", width1)
    print("Height:", height1)

# Quit the webdriver
driver.quit()













import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import pickle
from rembg import remove
import matplotlib.pyplot as plt
from PIL import Image  
path = r"C:\Users\azhar\Downloads\almirah3.png"
img = Image.open(path)
img_arr = np.array(img)
plt.imshow(img)
plt.axis('off')  # Turn off axis labels
plt.show()
h, w, c = img_arr.shape
print(h,w,c)
op_img = remove(img_arr)
    #op_image = Image.fromarray(op_arr)
op_arr = np.array(op_img)

modified_arr = np.delete(op_arr, 3, axis=2)
modified_image = Image.fromarray(modified_arr)
plt.imshow(modified_image)
plt.axis('off')
plt.show()
def calculate_product_dimensions(image):
    # Find non-zero pixels in the mask
    non_zero_pixels = np.transpose(np.nonzero(image))

    min_values = np.min(non_zero_pixels, axis=0)
    max_values = np.max(non_zero_pixels, axis=0)

    min_row, min_col = min_values[0], min_values[1]
    max_row, max_col = max_values[0], max_values[1]


    # Calculate the differences
    height = max_row - min_row
    width = max_col - min_col

    return height, width
height2, width2 = calculate_product_dimensions(modified_image)

print(f"Product Height: {height2} pixels")
print(f"Product Width: {width2} pixels")
a=int(width1[:-3])
b=int(height1[:-3])
r1=a/b
r2=width2/height2
print(r1)
print(r2)
abs((r1-r2)/(r1+r2))*100