from selenium import webdriver

def before_all(context):
    # Initialize WebDriver only once for all scenarios
    context.driver = webdriver.Edge()
    context.driver.maximize_window()

def after_all(context):
    # Close the WebDriver session after all scenarios are done
    context.driver.quit()


