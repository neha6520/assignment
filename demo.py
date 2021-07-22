import csv
from selenium import webdriver


driver = webdriver.Chrome('/home/neha/Downloads/chromedriver')
driver.maximize_window()
driver.get('https://agritimes.co.in/crops')
driver.implicitly_wait(30)


results1 = driver.find_elements_by_class_name('row')

with open('output.csv', 'w', newline='') as news_file:
    writer = csv.writer(news_file)
    for news_elem in results1:
        x = news_elem.find_element_by_tag_name('h2')
        print(x.get_attribute('title'))
        y = news_elem.find_element_by_tag_name('a')
        print(y.get_attribute('href'))
        writer.writerow([y.get_attribute('href'), x.get_attribute('title')])

driver.quit()