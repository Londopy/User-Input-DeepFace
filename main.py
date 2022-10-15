#check each module to see if its on the users computer
try:
	from deepface import DeepFace
	from IPython.display import Image
	import webbrowser
	from termcolor import colored, cprint
	import sys
	import time
	import os
	import random
#if one or more modules is not on the computer it will auto install the module(s)
except ModuleNotFoundError:
	from subprocess import call
	#list of modules
	modules = ["ipython","deepface", "termcolor", "Flask"]
	#auto installs them
	call("pip install " + ' '.join(modules), shell=True)


#random list of colours
Alist = ["red", "blue", "magenta", "green", "cyan", "yellow"]
#picks a random colour from list
AL = random.choice(Alist)

#prints date
cmd = 'date'

#sleeps the program for 0.5sec
time.sleep(0.5)

#spacer for looks
print('\u3164')

#custom 'figlet' text
figlet =  '''\n
        	  / /
             / /         ___       __      ___   /  ___
            / /        //   ) ) //   ) ) //   ) / //   ) )
           / /        //   / / //   / / //   / / //   / /
made by:  / /____/ / ((___/ / //   / / ((___/ / ((___/ /

\n\n'''
#prints figlet text and gives it a random colour
for line in figlet.splitlines():
	print(colored(line, AL))

imageFileName = input("Enter the name of the image file: ")

#path of image
#path = "test.jpg"
path = imageFileName
#correlates 'image' to 'path'
Image(filename = path)

#analyzes image given & looks for the atribrutes(actions) requested
obj = DeepFace.analyze(
	img_path=path,
	actions=['age', 'gender', 'race', 'emotion'],
	prog_bar=False
)

#sleeps the program for 3sec
time.sleep(3)

#spacer for looks
print('\u3164')
print('\u3164')
print('\u3164')
print('\u3164')
print("--------------")
print('\u3164')
print('\u3164')
print('\u3164')

emotions = obj['emotion']
races = obj['race']

a = obj['gender']
b = obj['age']
c = obj['emotion']
d = obj['race']
#prints grender
print(colored(f"I think the photo contains a {a}", AL))

#if the picture contains a male, it will describe the person as 'he'
if a == "Man":

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print('\u3164')

	#prints age
	print(f"I think he is {b}")

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print('\u3164')

	#prints emotion
	print("I think he is", max(emotions, key=emotions.get))

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print('\u3164')

	#prints race
	print("I think he is", max(races, key=races.get))

	#sleeps the program for 1.5 sec
	time.sleep(1.5)

	#spacer for looks
	print('\u3164')
	print('\u3164')

	#pauses cmd
	os.system("pause")

#if the picture contains a female, it will describe the person as 'she'
else:

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print('\u3164')

	#prints age
	print(f"I think she is {b}")

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print('\u3164')

	#prints emotion
	print("I think she is ", max(emotions, key=emotions.get))

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print('\u3164')

	#prints race
	print("I think she is ", max(races, key=races.get))

	#sleeps the program for 1.5 sec
	time.sleep(1.5)

	#spacer for looks
	print('\u3164')
	print('\u3164')

	#pauses cmd
	os.system("pause")
