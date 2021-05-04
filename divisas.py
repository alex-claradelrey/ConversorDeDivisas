import os
import time
import Datos

datos = Datos.Datos()

driver = datos.get_driver()


def btc_dollar():
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=btc+dollar&oq=btc+dollar&aqs=chrome..69i57j0l4j0i10i433l2j0i10j0l2.1607j1j7&sourceid=chrome&ie=UTF-8')
        time.sleep(2)
        btc_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = btc_txt.replace('.', '')
        btc = aux.replace(',', '.')
        return float(btc)


def euro_dollar():
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=euro+dollar&sxsrf=ALeKk013NH6_jkqMjykudAIz0EUTAqZ0ig%3A1619628422154&ei=hpGJYNz9COmFhbIPrKOa-AM&oq=euro+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQywEyBAgAEEMyBQgAEMsBMgUIABDLATIECAAQQzIGCAAQBxAeMgIIADICCAAyBQgAEMsBOgcIIxCxAhAnOgcIABAKEMsBOgQIABAKUJ3MP1jW1z9g1dk_aABwAngAgAGoAYgB3QSSAQMyLjOYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwjc2JSGsqHwAhXpQkEAHayRBj8Q4dUDCA4&uact=5')
        time.sleep(2)
        euro_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = euro_txt.replace('.', '')
        euro = aux.replace(',', '.')
        return float(euro)


def libra_dollar():
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=libra+dollar&sxsrf=ALeKk03c7cKLFrWpH3w8Psx6q2JBIFy6vg%3A1619629466496&ei=mpWJYOH9HciX8gLmpangDQ&oq=libra+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEAoyBQgAEMsBMggIABAHEAoQHjIGCAAQBxAeMgYIABAHEB4yCAgAEAcQChAeMgYIABAHEB4yBggAEAcQHjIICAAQBxAKEB4yBggAEAcQHjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQsQIQJzoKCAAQsQMQgwEQQzoECAAQQzoECAAQDVC7twpYx7wKYP6_CmgEcAJ4AIABeYgBmAWSAQM2LjGYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz&ved=0ahUKEwjhspL4taHwAhXIi1wKHeZSCtwQ4dUDCA4&uact=5')
        time.sleep(2)
        libra_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = libra_txt.replace('.', '')
        libra = aux.replace(',', '.')
        return float(libra)

