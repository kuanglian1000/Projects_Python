import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# get screent resolution #
width , height = pyautogui.size()
print("width="+str(width));print("height="+str(height))

# moving the mouse(absoulte position) #
for i in range(10):
    y = i * 20
    pyautogui.dragTo(822+y,264+y,duration=0.25)
    pyautogui.dragTo(822+y,550-y,duration=0.25)
    pyautogui.dragTo(1200-y,550-y,duration=0.25)
    pyautogui.dragTo(1200-y,264+y,duration=0.25)
    print(pyautogui.position())
