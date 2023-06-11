from tkinter import *
from bs4 import BeautifulSoup
import requests

web = requests.get("https://www.poetryfoundation.org/poems/poem-of-the-day")
#print(var.text)
webfront = BeautifulSoup(web.text,"html.parser")

#print(webfront.prettify())

class_tag = webfront.find(class_ = "c-txt c-txt_minimalCta" )
#print(class_tag)

url = class_tag['href']

var = requests.get(url)
#print(var.text)
soup = BeautifulSoup(var.text,"html.parser")
#print(soup.prettify())

data = soup.find(class_="o-poem") 
#print(data)

ls = []

for x in data:
#    print(x.text)
    ls.append(x.text)
#print(ls)

block = " "
for x in ls:
#    print(i)
    for y in x:
        if y == "\r":
            x = "\n" + "\n" + x[2:]
    block = block + x

print(block)

Poem = block

window = Tk()

window.title("Poem")

Head = Label(window,
        text = "Today's Poem",
        font = ("constantia",30,"bold"),
        fg = "white",
        bg = "red",
        )
Head.pack()

label = Label(window , 
        text = Poem,
        font = ("Constantia",15),
        bg= "white"
        )

label.pack()

window.mainloop()


