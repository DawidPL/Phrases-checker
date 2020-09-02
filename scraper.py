from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import datetime
import re
from typing import Tuple


def get_phrase(*args: Tuple[str, ...]) -> None:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    phrase_list = {}
    for a in args:
        driver.get(f'http://www.google.com/search?q={a}')
        title = driver.find_element_by_xpath('//*[@id="result-stats"]')
        regex = re.search(r'(\s)(([0-9]+)\s)+', title.text)
        phrase_list[a] = regex.group().strip()
    driver.quit()
    save_phrase_to_file(get_current_time(), phrase_list)


def get_current_time():
    present_time = datetime.datetime.now()
    converted_present_time = present_time.strftime("%d-%m-%Y %X").replace(':', '_')
    return converted_present_time


def save_phrase_to_file(time, phrase):
    # with open(f'C:/Users/{os.getlogin()}/Desktop/frazy_{time}.txt', 'w+') as f:
    with open(f'frazy_{time}.txt', 'w+') as f:
        for i, (items) in enumerate(phrase.items()):
            key, value = items
            # print(f'{i+1}. {key}: {value}')
            f.write(f'{i + 1}. {key}: {value}\n')
