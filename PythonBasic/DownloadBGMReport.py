import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.alert('Wait',timeout=5)

pyautogui.click(561,652,button='left')

# moveTo (561,652) & click #移至號碼
# type BGM number #輸入BGM查詢條件
# click PageDown
# moveTo (1000,385) & click #開始查詢
# click PageDown
# moveTo (1141,530) & click #下載報表
# type BGM number #輸入報表檔名
# ALT + S #存檔

