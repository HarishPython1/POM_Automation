from pages.LoginPage import Login


def test_jenkinslogin():
   lp= Login()
   lp.login_jenkins()

   # global driver
   # # Launch browser and navigate to url- section 1 >>S1
   # driver = webdriver.Chrome(
   #     executable_path="C:/Users/btm-fac/PycharmProjects/POM_Automation/drivers/chromedriver.exe")
   # driver.get("http://localhost:8081/login")
   # # Logint to application - section 2 >>S2
   # driver.find_element_by_id("j_username").send_keys("admin")
   # driver.find_element_by_name("j_password").send_keys("manager")
   # driver.find_element_by_name("Submit").click()

# def test_logout():
#     #Logout from application - section 3 >>S3
#     driver.find_element_by_xpath("//b[text()='log out']").click()