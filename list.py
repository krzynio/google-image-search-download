from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep

# class name of element with "There is no more results"
end_element_class_name = "Yu2Dnd"

# class name of "get more results" button
get_more_results_button_class_name = "mye4qd"

# picture preview class name
big_picture_on_the_left_class_name = "n3VNCb"

start_url = "https://www.google.com/search?q=Python&hl=en&source=lnms&tbm=isch&sa=X"

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)
driver.get(start_url)
driver.find_element_by_tag_name('body').send_keys(Keys.HOME)

assert "Search" in driver.title

end_element = driver.find_element_by_class_name(end_element_class_name)

for i in range(100):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    try:
        driver.find_element_by_class_name(get_more_results_button_class_name).click()
    except:
        pass
    
    if end_element.is_displayed():
        break


driver.find_element_by_tag_name('body').send_keys(Keys.END)

images_to_click = driver.find_elements_by_class_name("rg_i")

for image in images_to_click:
    image.location_once_scrolled_into_view
    image.click()
    sleep (0.1)
    big_images = driver.find_elements_by_class_name(big_picture_on_the_left_class_name)
    
    clean_source = None    
    for big_image in big_images:
        for i in range(5):
            src = big_image.get_attribute("src")
            if src.startswith("http") and not "://encrypted" in src:
                clean_source = src
            if clean_source:
                break
            else:
                sleep(0.1)
    if clean_source:
        print (clean_source)

driver.quit()

