import pyautogui as pg

from time import sleep 

# pg.mouseInfo()

pg.press('win')

pg.write('chrome', interval=0.2)

pg.press('enter')

pg.write('www.youtube.com', interval=0.3)

pg.press('enter')

sleep(2)

pg.press(';')

pg.write('neymar 2011', interval=0.2)

pg.press('enter')

sleep(2)

pg.click(854,448)









