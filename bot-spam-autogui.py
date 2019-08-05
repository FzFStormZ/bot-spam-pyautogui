import pyautogui
import time


pyautogui.setKeyboardLayout("azerty") # If you want "qwerty", delete this line !!


# BOT with static image search:
x, y = pyautogui.locateCenterOnScreen("IMAGE_SEARCH.PNG")
print(x)
print(y)

with open("WORDS_FILES.txt", "r") as f:
	jeux = []
	for j in f:
		jeux = j.split(" ")
	for g in jeux:
		pyautogui.click(x, y)
		pyautogui.typewrite(g)
		pyautogui.press("enter")
		time.sleep(2)





# BOT with moving image search:
with open("WORDS_FILES.tx", "r") as f:
	jeux = []
	for j in f:
		jeux = j.split(" ")
	for g in jeux:
		coords = pyautogui.locateOnScreen("IMAGE_SEARCH.PNG")

		while coords == None: # Check if the image has been found !!
			coords = pyautogui.locateOnScreen("IMAGE_SEARCH.PNG")
			print(coords)

		x, y = pyautogui.center(coords)
		print(x)
		print(y)
		pyautogui.click(x, y)
		pyautogui.typewrite(g)
		pyautogui.press("enter")

