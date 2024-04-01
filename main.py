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
print(' ')

#custom 'figlet' text
figlet =  '''\n           
               / /                                 /
              / /                                 /
             / /         ___     /___      ___   /  ___
            / /        //   ) ) //   ) ) //   ) / //   ) )
           / /        //   / / //   / / //   / / //   / /
made by:  / /____/ / ((___/ / //   / / ((___/ / ((___/ /

\n\n'''
#prints figlet text and gives it a random colour
for line in figlet.splitlines():
	print(colored(line, AL))

imageFileName = input("Enter the name of the image file: ")
print(" ")

#path of image
#path = "test.jpg"
path = imageFileName
#correlates 'image' to 'path'
Image(filename = path)

#analyzes image given & looks for the atribrutes(actions) requested
objs = DeepFace.analyze(
	img_path=path,
	actions=['age', 'gender', 'race', 'emotion']
)

#sleeps the program for 3sec
time.sleep(3)

#spacer for looks
print(' ')
print(' ')
print("--------------")
print(' ')


# Analyze the temporary image using DeepFace
for obj in objs:
	a = obj['gender']
	b = obj['age']
	c = obj['emotion']
	d = obj['race']

	# Determine the correct pronoun based on gender
	genda = "he" if max(a, key=a.get) == "Man" else "she"

	# print(colored(f"I think the photo contains a {a}", AL))
	print(f"I think the photo contains a", max(a, key=a.get))

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print(' ')

	#prints age
	print(f"I think {genda} is {b}")

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print(' ')

	#prints emotion
	print(f"I think {genda} is", max(c, key=c.get))

	#sleeps the program for 1 sec
	time.sleep(1)

	#spacer for looks
	print(' ')

	#prints race
	print(f"I think {genda} is", max(d, key=d.get))

	#sleeps the program for 1.5 sec
	time.sleep(1.5)

	#spacer for looks
	print(' ')
	print(' ')

	#pauses cmd
	os.system("pause")
