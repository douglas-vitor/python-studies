import RPi.GPIO as gpio
import time
import pyautogui

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
gpio.setup(18, gpio.IN)


print("=====START=====")
try:
  print("Start script in 5 seconds.....")
  time.sleep(5)
  pyautogui.press('space')      #Start game
  while True:
    if gpio.input(17) == 1:
      print("DIREITA")
      pyautogui.press('right')
      pyautogui.press('space')
      time.sleep(0.5)
    elif gpio.input(18) == 1:
      print("ESQUERDA")
      pyautogui.press('left')
      pyautogui.press('space')
      time.sleep(0.5)
    else:
      print("MEIO")
      pyautogui.press('space')
      time.sleep(0.5)

except KeyboardInterrupt:
  print("=====STOP=====")
  gpio.cleanup()
  pass