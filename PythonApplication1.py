import pyautogui
import time
import keyboard

def cautare_youtube():
    if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\cautareyoutube.png', confidence=0.7) !=None:
        camp_youtube = pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\cautareyoutube.png', confidence=0.7)
        pyautogui.click(camp_youtube)
        time.sleep(3)
        pyautogui.write("Zona IT")
        pyautogui.press('enter')
        print("Imaginea se afla pe ecran")
    else:
        print("Imaginea nu se afla pe ecran")
    


def cautare_google():
    if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\cautaregoogle.png', confidence=0.7) !=None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\cautaregoogle.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("https://youtube.com")
        pyautogui.press('enter')
        print("Imaginea se afla pe ecran")
    else:
        print("Imaginea nu se afla pe ecran")
#def sub_youtube():
    #pyautogui.press('pagedown')
    #if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\subscribe.png') !=None:
       #sub_youtube = pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\subscribe.png')
       #pyautogui.click(sub_youtube)
       #time.sleep(3)
       #print("imaginea se afla pe ecran")
    #else:
       #print("imaginea nu se afla pe ecran")


def video_click():
    if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\imagevideo.png', confidence=0.7) !=None:
       video = pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\imagevideo.png', confidence=0.7)
       pyautogui.click(video)
       time.sleep(3)

#def bar_click():
   # if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\scrollbar.png', confidence=0.7) !=None:
       # bar = pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\scrollbar.png', confidence=0.7)
       # pyautogui.click(bar)
       # pyautogui.moveRel(0, 300)
       # pyautogui.click()
       # time.sleep(3)


def coordonate():
    print(pyautogui.position())




time.sleep(2)
cautare_google()
time.sleep(3)
cautare_youtube()
time.sleep(3)
#sub_youtube()
video_click()
time.sleep(3)
coordonate()
