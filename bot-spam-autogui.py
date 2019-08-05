import pyautogui
import time


pyautogui.setKeyboardLayout("azerty")


# BOT avec recherche d'image statique:
x, y = pyautogui.locateCenterOnScreen("discord_field.PNG")
print(x)
print(y)

with open("dico_jeux_discord.txt", "r") as f:
	jeux = []
	for j in f:
		jeux = j.split(" ")
	for g in jeux:
		pyautogui.click(x, y)
		pyautogui.typewrite(g)
		pyautogui.press("enter")
		time.sleep(2)





# BOT avec recherche d'image en mouvement:
with open("dico_jeux_discord.txt", "r") as f:
	jeux = []
	for j in f:
		jeux = j.split(" ")
	for g in jeux:
		coords = pyautogui.locateOnScreen("discord_field.PNG")

		while coords == None: # Vérifier si l'image a été trouvé !!
			coords = pyautogui.locateOnScreen("discord_field.PNG")
			print(coords)

		x, y = pyautogui.center(coords)
		print(x)
		print(y)
		pyautogui.click(x, y)
		pyautogui.typewrite(g)
		pyautogui.press("enter")

