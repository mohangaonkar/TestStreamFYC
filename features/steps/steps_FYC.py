from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigating to URL                              #1
@given("I navigate to the FYC platform")
def step_navigate_to_fyc_platform(context):
    context.driver.get("https://indeedemo-fyc.watch.indee.tv/login")

#Entering credentials and sign-up                 #2
@when("I sign in with the provided PIN")
def step_sign_in(context):
    pin_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='access-code']"))
    )
    pin_input.send_keys("WVMVHWBS")
    sign_in_button = context.driver.find_element(By.XPATH, "//span[normalize-space()='Sign In']")  # Adjust selector
    sign_in_button.click()

#Verifying the page title                         #3
@then("I should be logged into the platform")
def step_logged_in(context):
    page_title = context.driver.title
    print(f"The title of the page is: {page_title}")

#Scrooling to all titles                           #4
@when("I scroll to All Titles")
def step_scroll_to_all_titles(context):
    # all_titles = context.driver.find_element(By.XPATH, "//p[text()=' All Titles ']")
    all_titles=WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,"//p[text()=' All Titles ']")))
    context.driver.execute_script("arguments[0].scrollIntoView();", all_titles)

#clicking on test automation project               #5
@when('I click on the "Test Automation Project"')
def step_click_project(context):
    test = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@alt='Test automation project']")))
    actions = ActionChains(context.driver)
    actions.move_to_element(test).click().perform()

#verifying the page title                          #6
@then("I should be navigated to the project page")
def step_navigate_to_project_page(context):
    page_title2 = context.driver.title
    print(f"The title of the page is: {page_title2}")

#Scrolling to test automation(videos/details)      #7
@when("I scroll to Test Automation Project")
def step_scroll_to_project(context):
    wait = WebDriverWait(context.driver, 10)
    scroll = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Test automation project']")))
    context.driver.execute_script("arguments[0].scrollIntoView();", scroll)

# Switching to details tab                         #8
@when("I switch to the \"Details\" tab")
def step_switch_to_details_tab(context):
    wait = WebDriverWait(context.driver, 10)
    details_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='detailsSection']")))  # Replace "detailsTab" with the actual locator
    details_tab.click()
    time.sleep(5)

#Switching to Videos tab                           #9
@when("I return to the \"Videos\" tab")
def step_return_to_videos_tab(context):
    wait = WebDriverWait(context.driver, 10)
    videos_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='videosSection']")))  # Replace "videosTab" with the actual locator
    videos_tab.click()
    time.sleep(5)

#Playing the video                                #10
@when("I play the video")
def step_play_video(context):
    play = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play Video']//*[name()='svg']")))
    actions = ActionChains(context.driver)
    actions.move_to_element(play).click().perform()

#Let the video play for 10 secs                   #11
@then("the video should play for 10 seconds")
def step_video_play(context):
    time.sleep(10)

#Pause the video                                  #12
@when('I click the "Pause" button') #12
def step_pause_button(context):
    frame=WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.ID,"video_player")))
    context.driver.switch_to.frame(frame)
    # hover over the screen
    mouse_hover=context.driver.find_element(By.XPATH,"//*[@id='media-player']")
    actions=ActionChains(context.driver)
    actions.move_to_element(mouse_hover).perform()
    pause = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Pause' and contains(@class, 'jw-icon-playback')]")))
    actions=ActionChains(context.driver)
    actions.move_to_element(pause).click().perform()
    # switching back to default_content
    context.driver.switch_to.default_content()

#Continued to play the video                      #13
@when('I click the "Continue Watching" button')
def step_continue_video(context):
    continue_watching = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue Watching']")))
    actions=ActionChains(context.driver)
    actions.move_to_element(continue_watching).click().perform()
    time.sleep(20)

#Adjusting the volume to 50%                      #14
@when('I adjust the volume to 50%')
def step_adjust_volume(context):
    frame = context.driver.find_element(By.ID, "video_player")
    context.driver.switch_to.frame(frame)
    volume_slider = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Volume' and @class='jw-overlay jw-reset']"))
    )
    #JavaScript to set the volume to 50%
    desired_volume = 50  # Desired volume value
    context.driver.execute_script("arguments[0].setAttribute('aria-valuenow', arguments[1]);", volume_slider, desired_volume)

#Verifying the volume to 50%                      #15
@then('the volume level should be set to 50%')
def step_adjusted_volume(context):
    # Verify the volume change by fetching the updated value
    volume_slider = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Volume' and @class='jw-overlay jw-reset']"))
    )
    updated_volume = volume_slider.get_attribute("aria-valuenow")
    print(f"Updated Volume: {updated_volume}%")

#Click on setting and set resolution to 480p       #16
@when('I open the settings menu and change the resolution to 480')
def step_click_setting(context):
    settings = context.driver.find_element(By.XPATH, "//div[@aria-label='Settings' and @aria-controls='jw-settings-menu']")
    actions=ActionChains(context.driver)
    actions.move_to_element(settings).click().perform()
    pixel480 = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='480p']")))
    actions = ActionChains(context.driver)
    actions.move_to_element(pixel480).click().perform()

#Verifying resolution to 480p                       #17
@then('the resolution should be updated to "480p"')
def step_vrifying_480(context):
    selected_quality = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='480p' and contains(@class, 'item-active')]"))
    )
    if selected_quality:
        print("480p quality successfully switched.")
    else:
        print("Failed to switch to 480p quality.")

#Click on setting and set resolution to 720p       #18
@when('I change the video resolution to "720p"')
def step_resolution_720(context):
    settings = context.driver.find_element(By.XPATH, "//div[@aria-label='Settings' and @aria-controls='jw-settings-menu']")
    actions = ActionChains(context.driver)
    actions.move_to_element(settings).click().perform()
    # switching to 720px
    pixel720 = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='720p']")))
    actions.move_to_element(pixel720).click().perform()

#Verifying resolution to 720p                      #19
@then('the resolution should be updated to "720p"')
def step_verifying_720(context):
    selected_quality = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='720p' and contains(@class, 'item-active')]"))
    )
    if selected_quality:
        print("720p quality successfully switched.")
    else:
        print("Failed to switch to 720p quality.")

#Pause the video                                  #20
@when('I click on the Pause video')
def step_pause_video(context):
    pause = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Pause' and contains(@class, 'jw-icon-playback')]")))
    actions=ActionChains(context.driver)
    actions.move_to_element(pause).click().perform()
    #switching to default content
    context.driver.switch_to.default_content()

#Click on back button                            #21
@when('I click on the Back button')
def step_back_button(context):
    back_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go Back and continue playing video']")))
    back_button.click()

#Verifying the page title                        #22
@then('I should be redirected to the previous screen')
def step_verifying_page_title(context):
    context.driver.implicitly_wait(10)
    page_title = context.driver.title
    print(f"The title of the page is: {page_title}")

#Signout                                          #23
@when('I click on the Signout button')
def step_signout(context):
    signout=WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='signOutSideBar']")))
    signout.click()
    time.sleep(2)

#Verifying signout                                 #24
@then('I should be logged out successfully')
def step_verifying_signout(context):
    time.sleep(2)
    page_title = context.driver.title
    print(f"The title of the page is: {page_title}")