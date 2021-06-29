from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/trickyelements.html")

random = driver.find_element_by_id("randomized")
diff = driver.find_element_by_id("difficulty")
tricky = driver.find_element_by_id("trickyForm")
element1 = driver.find_element_by_id("element1")
element2 = driver.find_element_by_id("element2")
element3 = driver.find_element_by_id("element3")
element4 = driver.find_element_by_id("element4")
element5 = driver.find_element_by_id("element5")
result = driver.find_element_by_id("result")

# ------

# ids = driver.find_elements_by_xpath('//*[@id]')
# for i_d in ids:
#     final = i_d.get_attribute('id')
#     print(final)

# -------

try:
    first = driver.find_element_by_css_selector("button")
    first.click()

    if (first.text + " was clicked") == result.text:
        print("Acceptable")
    else:
        print("Error")

    driver.close()

except:
    print("Button type cannot be found")
    driver.close()
