import random 
# @python.coder_
import pyautogui as pg 
import time 
car = ("lamborgini", "Ferrari", "Mustang")
time.sleep(8)
for i in range(500):
	a = random.choice(car)
	pg.write("I love  "+a)
	pg.press("enter")
