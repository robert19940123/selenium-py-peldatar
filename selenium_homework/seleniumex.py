from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/")


def nope(exc):
    try:
        w = driver.find_element_by_id(exc)
        w.click()
    except:
        print("ID isn't available")


try:
    q = driver.find_element_by_id("nemletezik")
    q.click()
except:
    print("Tényleg nem létezik")

nope("user")


driver.close()









