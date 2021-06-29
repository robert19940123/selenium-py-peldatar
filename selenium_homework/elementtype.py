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

# -------

try:
    first = driver.find_element_by_css_selector("button")
    first.click()

    result = driver.find_element_by_id("result")

    if (first.text + " was clicked") == result.text:
        print("Acceptable")
    else:
        print("Error")

    driver.close()

except:
    print("Button type cannot be found")
    driver.close()
