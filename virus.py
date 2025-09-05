import os
import time
import pyautogui
import pynput
import ctypes

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

ctypes.windll.user32.MessageBoxW(0, "Hi, do you love minji or not?", "Virus", 1)


if result == 1:
    ctypes.windll.user32.MessageBoxW(0, "Nice", "Di na virus", 0x40)
else:
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

    for i in range(3):
        os.system("start notepad.exe")
        os.system("start calc.exe")
        
    for i in range(20):
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x,y, duration = 0.2)
        time.sleep(0.30)
