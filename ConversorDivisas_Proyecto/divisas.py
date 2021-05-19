import os
import time
import Datos

datos = Datos.Datos()

driver = datos.get_driver()

# conversion de dollar
def btc_dollar(): #un Bitcoin equivale a X dolares
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=btc+dollar&oq=btc+dollar&aqs=chrome..69i57j0l4j0i10i433l2j0i10j0l2.1607j1j7&sourceid=chrome&ie=UTF-8')
        time.sleep(2)
        btc_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = btc_txt.replace('.', '')
        btc = aux.replace(',', '.')
        return float(btc)


def euro_dollar(): #un euro equivale a X dolares
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=euro+dollar&sxsrf=ALeKk013NH6_jkqMjykudAIz0EUTAqZ0ig%3A1619628422154&ei=hpGJYNz9COmFhbIPrKOa-AM&oq=euro+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQywEyBAgAEEMyBQgAEMsBMgUIABDLATIECAAQQzIGCAAQBxAeMgIIADICCAAyBQgAEMsBOgcIIxCxAhAnOgcIABAKEMsBOgQIABAKUJ3MP1jW1z9g1dk_aABwAngAgAGoAYgB3QSSAQMyLjOYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwjc2JSGsqHwAhXpQkEAHayRBj8Q4dUDCA4&uact=5')
        time.sleep(2)
        euro_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = euro_txt.replace('.', '')
        euro = aux.replace(',', '.')
        return float(euro)


def libra_dollar(): #una libra equivale a X dolares
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=libra+dollar&sxsrf=ALeKk03c7cKLFrWpH3w8Psx6q2JBIFy6vg%3A1619629466496&ei=mpWJYOH9HciX8gLmpangDQ&oq=libra+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEAoyBQgAEMsBMggIABAHEAoQHjIGCAAQBxAeMgYIABAHEB4yCAgAEAcQChAeMgYIABAHEB4yBggAEAcQHjIICAAQBxAKEB4yBggAEAcQHjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQsQIQJzoKCAAQsQMQgwEQQzoECAAQQzoECAAQDVC7twpYx7wKYP6_CmgEcAJ4AIABeYgBmAWSAQM2LjGYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz&ved=0ahUKEwjhspL4taHwAhXIi1wKHeZSCtwQ4dUDCA4&uact=5')
        time.sleep(2)
        libra_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = libra_txt.replace('.', '')
        libra = aux.replace(',', '.')
        return float(libra)

# conversion de euro
def btc_euro(): #un Bitcoin equivale a X euros
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=btc+euro&rlz=1C1CHZN_esES935ES935&sxsrf=ALeKk02URTu83KSOQzuQBkIZWNrR6vZacg%3A1621362108003&ei=uwWkYI3vPI-QlwSw8oWQCw&oq=btc+euro&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBwgAEIcCEBQyAggAMgIIADICCAAyAggAMgIIADICCAAyBAgAEAoyAggAOgYIABAHEB46CAgAEAcQChAeUKu5CFjMuwhg_cAIaABwAngAgAFziAGkA5IBAzEuM5gBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwjNuP_D7NPwAhUPyIUKHTB5AbIQ4dUDCA4&uact=5')
        time.sleep(2)
        btc_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = btc_txt.replace('.', '')
        btc = aux.replace(',', '.')
        return float(btc)

def dollar_euro(): #un dollar equivale a X euros
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=dollar+euro&rlz=1C1CHZN_esES935ES935&sxsrf=ALeKk00vE_vsvvcQYVfYrizlgwNnGDzz4w%3A1621362692159&ei=BAikYMyZCcqkaeeQmpAL&oq=dollar+euro&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCCMQJxBGEIICMgcIABCHAhAUMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyCAgAEMkDEMsBMgQIABAKMgUIABDLAToHCAAQRxCwAzoFCAAQsQM6AggAOgcIABDJAxAKOgQIIxAnUK21MliOuDJgs9cyaAFwAXgAgAFqiAHaA5IBAzMuMpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=gws-wiz')
        time.sleep(2)
        dollar_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = dollar_txt.replace('.', '')
        dollar = aux.replace(',', '.')
        return float(dollar)

def libra_euro(): #una libra equivale a X euros
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=libra+euro&rlz=1C1CHZN_esES935ES935&sxsrf=ALeKk03PlGW6YkLR6Bpmt-ka7HSytO-ZNg%3A1621362102508&ei=tgWkYODJHpDClwSow6b4Cg&oq=libra+euro&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIcCELEDEBQyAggAMgIIADICCAAyBQgAEMkDMgIIADICCAAyAggAMgIIADICCAA6BwgAEEcQsAM6BwgAELADEEM6BQgAELEDOgcIABCHAhAUUKAcWJEgYMEhaAFwAngAgAF5iAH2A5IBAzQuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwjg_K_B7NPwAhUQ4YUKHaihCa8Q4dUDCA4&uact=5')
        time.sleep(2)
        libra_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = libra_txt.replace('.', '')
        libra = aux.replace(',', '.')
        return float(libra)

#conversion de libra

def btc_libra(): #un Bitcoin equivale a X libras
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=btc+gbp&rlz=1C1CHZN_esES935ES935&sxsrf=ALeKk01uChaj9Zqj-LK2HPk1dtQbjdvBWA%3A1621362398339&ei=3gakYJ6iFIaVlwSih5OACw&oq=btc+gbp&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMsBMgUIABDLATICCAAyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBOgcIABBHELADOgQIABBDOggIABDHARCvAVD4UFi5U2D1XGgBcAJ4AIABcogB9QKSAQMzLjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwieibjO7dPwAhWGyoUKHaLDBLAQ4dUDCA4&uact=5')
        time.sleep(2)
        btc_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = btc_txt.replace('.', '')
        btc = aux.replace(',', '.')
        return float(btc)

def dollar_libra(): #un dolar equivale a X libras
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=dollar+gpb&rlz=1C1CHZN_esES935ES935&sxsrf=ALeKk03V4AW32-tTTtiRtwtLbok12F5SEg%3A1621362605914&ei=rQekYK2cN8qsaaC8jYgL&oq=dollar+gpb&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEA0yCAgAEAcQChAeMggIABAHEAoQHjIICAAQBxAKEB4yBAgAEA0yCAgAEAcQChAeMggIABAHEAoQHjIGCAAQDRAeMgYIABANEB4yBggAEA0QHjoGCAAQBxAeOgoIABAHEAUQChAeOggIABAHEAUQHlCqlQVY35kFYPebBWgAcAF4AIABpwGIAcYFkgEDNS4ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz&ved=0ahUKEwjtprWx7tPwAhVKVhoKHSBeA7EQ4dUDCA4&uact=5')
        time.sleep(2)
        btc_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = btc_txt.replace('.', '')
        btc = aux.replace(',', '.')
        return float(btc)

def euro_libra(): #un euro equivale a X libras
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=euro+gpb&rlz=1C1CHZN_esES935ES935&sxsrf=ALeKk00ZenEKix6-fcov2DyVIH_SqLaL9w%3A1621362410895&ei=6gakYJqgNqKVlwTVw7K4Cg&oq=euro+gpb&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAo6BAgjECc6BAgAEEM6BwgAEIcCEBQ6CQgjECcQRhCCAjoKCAAQsQMQgwEQQzoHCAAQsQMQQzoICAAQsQMQgwE6DQgAEIcCELEDEIMBEBQ6AggAOgcIABAKEMsBOgUIABDLAToICAAQFhAKEB5Q8t8LWN_nC2D17gtoAHACeACAAYcBiAGGCJIBAzIuN5gBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwiavbbU7dPwAhWiyoUKHdWhDKcQ4dUDCA4&uact=5')
        time.sleep(2)
        euro_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = euro_txt.replace('.', '')
        euro = aux.replace(',', '.')
        return float(euro)

