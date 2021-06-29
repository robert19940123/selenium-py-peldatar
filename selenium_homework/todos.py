from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/todo.html")

#this_list = []
this = driver.find_element_by_class_name("unstyled")
print(this.text)
#this_list.append(this.text)
#print(this_list)

driver.close()