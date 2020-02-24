import webbrowser
import time
import pyautogui as gui


interval = 2
position = 730,190
numbers={917025674097, 919048525224}

message="Automated message"

for i in numbers:
 url = 'https://wa.me/{}?text={}'.format(i, message)
 webbrowser.open(url)
 time.sleep(3)
 gui.click(position)
 time.sleep(3)
 gui.press('enter')
 time.sleep(interval)