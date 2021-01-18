import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Python32\selenium\webdriver\chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('how to write program.')
search_box.submit()
time.sleep(10) # Let the user actually see something!
driver.quit()