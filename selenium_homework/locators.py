from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/kitchensink.html")

ids = driver.find_element_by_id("radio-btn-example")
print(ids.text)

names = driver.find_element_by_name("multiple-select-example")
print(names.get_attribute("id"))

xpath_s = driver.find_element_by_xpath('//*[@id="product"]')
print(xpath_s.get_attribute("id"))
print(xpath_s.text)


driver.close()

