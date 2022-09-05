from re import I
from bs4 import BeautifulSoup
import requests
import time
from playsound import playsound

url = 'https://courses.students.ubc.ca/cs/courseschedule?tname=subj-section&course='
def urlMaker(courseName, courseNumber, courseSection):
    return url + str(courseNumber) + '&section=' + str(courseSection) + '&campuscd=UBCO&dept=' + str(courseName)+ '&pname=subjarea'
    # keep campuscd=UBCV if you want to keep track of courses offered in UBCV
def seatFinder(cou):
    url = urlMaker(cou[:4],cou[5:8],cou[9:12])
    ua={'User-Agent':'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_2) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/26.0.869.0 Safari/531.2'}
    r = requests.get(url, headers=ua)
    course = BeautifulSoup(r.text, features="lxml")
    tab = course.find('table',class_ = "'table")
    lol = tab.find('tr').find_all('td')[-1].text
    if int(lol) != 0:
        playsound(r'C:\Users\ANMA\Desktop\beep.mp3')
        print(f'Seat found in {cou}!! Hurry Up!')
    ans.append(f'Number of general seats left in {cou} are {lol}')

myInterest = ['DATA 101 101', 'DATA 101 002'] # enter courses you wanna keep track of
def final():
    for cour in myInterest:
        seatFinder(cour)
    print('=================')
    for i in ans:
        print(i)
    print('==================')
    print('')


while True:
    ans = []
    final()
    time.sleep(5)