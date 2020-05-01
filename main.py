from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request

# Scrolling to the bottom


def scroll(SCROLL_PAUSE_TIME):
    print('Started Scrolling..')
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print('Reached to the end of page')


chrome_options = Options()
# Uncomment two lines down if you don't want chrome window to popup and go headless
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.minimize_window()
# Enter tiktok username here
username = str(input('Enter instagram username : '))


driver.get('https://www.instagram.com/' + username + '/')
scroll(1)
posts = []
links = driver.find_elements_by_tag_name('img')
for link in links:
    post = link.get_attribute('src')
    posts.append(post)

# for removing last instagram image link
posts.pop()

# closing webdriver
driver.quit()

print("Links are here \n links Start :: \n")
for i in range(len(posts)):
    sleep(2)
    urllib.request.urlretrieve(posts[i], 'media' + str(i) + '.jpg')
    print('Media' + str(i) + '.jpg downloaded.')
