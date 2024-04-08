driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
# //a[contained(@href, 'shop)]   a[href*='shop'] - can use incomplete value sometimes

driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")


for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("rus")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Russia")))
driver.find_element(By.LINK_TEXT, "Russia").click()


driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

successText = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in successText

time.sleep(3)
driver.close()