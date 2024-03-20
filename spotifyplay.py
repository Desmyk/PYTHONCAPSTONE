# import modules
import pyautogui
import time
import psutil

# pressing the 'win' key to open windows bar
pyautogui.press('win')
time.sleep(1)
# writing "Spotify"
pyautogui.write('Spotify')
time.sleep(1)
# pressing the 'enter' key to open Spotify
pyautogui.press('enter')

# defining the name of program
program_name = 'Spotify.exe'

# set timeout
timeout = time.time() + 120 #120 secs
while True:
    # check to see if Spotify is open
    for process in psutil.process_iter():
        try:
            if process.name() == program_name:
                # print message that "spotify is open"
                print("Spotify is Open!")
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # NoSuchProcess is raised when the process is not found
            # AccessDenied is raised when there is no permission to access the process 
            pass
    else:
        # if program is not open, check for timeout
        if time.time() > timeout:
            print("Timed Out!")
            break
        else:
            # wait for a while before rechecking
            time.sleep(1)
            continue
    # break loop cause at this point, the program is open!
    break

time.sleep(5)
# play music
pyautogui.press('space') 

### The above code generally accesses ypur OS and opens the program
### NB: IF APP NOT INSTALLED ON THE DEVICE, IT'LL RETURN ERROR!!!

