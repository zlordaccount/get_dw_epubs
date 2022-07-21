from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import time
import ebooklib


def get_new_chapters(chapterurl: str):
    path = "C:\\Program Files (x86)\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(chapterurl)
    chapters = 1
    attempts = 1
    currenturl = ''
    try:
        while chapters < 120:
            while attempts < 5:
                try:
                    search = driver.find_element(By.CSS_SELECTOR, "i[class='fas fa-chevron-circle-right']")
                    search.click()
                except:
                    attempts = attempts + 1
                    driver.refresh()
                else:
                    break

            if driver.current_url == chapterurl or driver.current_url == currenturl:
                print("No Additional Chapters, Sorry :(")
                return driver.current_url
            time.sleep(1)
            search = driver.find_element(By.CLASS_NAME, value="epub-btn-text")
            search.click()
            search = driver.find_element(By.CSS_SELECTOR, "img[src='/images/regaari.jpg']")
            search.click()
            search = driver.find_element(By.ID, "download-epub-add-label")
            search.click()
            time.sleep(1)
            search = driver.find_element(By.XPATH, "//div[contains(@class, 'download-epub-ok-btn epub-btn')]")
            search.click()
            time.sleep(1)
            attempts = 1
            currenturl = driver.current_url
    except:
        return chapterurl

    return currenturl


def main():
    chapter_file = open(r"latest_chapter.txt", 'r')
    chapterurl = chapter_file.read()
    chapter_file.close()


    chapter_file = open(r"latest_chapter.txt", 'w')
    # https://deathworlders.com/books/deathworlders/chapter-86-into-the-fold/
    try:
        chapter_file.write(get_new_chapters(chapterurl))
    except Exception as error:
        chapter_file.write(chapterurl)
        print(error)
    chapter_file.close()

if __name__ == '__main__':
    main()
