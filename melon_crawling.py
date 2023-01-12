from selenium import webdriver
from selenium.webdriver.common.by import By


def pageCrawl():
    musiclist = drive.find_elements(By.XPATH, "//table[@border=\"1\"]/tbody/tr")
    for music in musiclist:
        try:
            song, artist = music.find_elements(By.XPATH, "./td[@class=\"t_left\"]")[0:2]
            song = song.find_element(By.XPATH, "./div/div/button[@class=\"btn_icon play\"]")
            title = song.get_attribute('title')

            artist = artist.find_element(By.XPATH, "./div/div/a")
            artistName = artist.text

            f.write(title.split(" 재생 - 새창")[0] + "|" + artistName + '\n')
            print(title.split(" 재생 - 새창")[0] + "|" + artistName)
        except:
            print("error")


drive = webdriver.Chrome("C:\\Users\\dhals\\Downloads\\chromedriver.exe")
drive.get("https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey=17862859")

f = open("musicList.txt", "a", encoding="utf-8")

print("init setting end")


print("crawling")
pageCrawl()
print("end")

f.close()

