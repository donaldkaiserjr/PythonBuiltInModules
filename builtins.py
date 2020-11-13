'''
Modules and What They Do

1.)   import glob:     Reads through a list of files (folder of files).  glob.iglob(“prop folder/*.txt”)

2.) import string:    for the alphabet

3.) import string, os  (use this to CREATE a folder with a bunch of files). ex:  
if not os.path.exists(“abcs”):
	os.makedirs(“abcs”)

4.) import time:    this could make a loop take a specified amount of time that you set
to loop.  ex:  time.sleep(i)

5.)  import requests:   for web urls txt files. ex:  requests = requests.get(“http://www.google.com, headers = {‘user-agent’: ‘customerUserAgent’})

6.) import emphem:   used for astronomy calculations


7) import webbrowser:  used to open a web browser. ex: webbrowser.open(“https://google.com)

8.) import tkinter:  working with GUIs

8.)  import pandas     creates dataframe objects. you can multiply the table by a number, for example, then export the calculated data to a text file in your local directory.

9.) import json:      this helps write dictionary content to a file.  json.dump(dict1, file, indent=4)   indent=4 will create 4 white spaces to indent the different levels of 
the dictionary items.

10.) zip (not a module). This iterates through a list.  ex:  zip(string.ascii_lowercase[0::2]

'''
