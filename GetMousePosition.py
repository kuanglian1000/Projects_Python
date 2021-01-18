import pyautogui
print('Press Ctrl-C to quit.')

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr,end='')
        print('\b'*len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\nDone.')