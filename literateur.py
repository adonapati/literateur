

#modules
import ety
import json
from dictapi import DictionaryAPI
import certifi
import ssl
import urllib.request
from playsound import playsound
from tkinter import *
from tkmacosx import Button


#the app window
window = Tk()
window.title('Literateur')
window.geometry('1000x700')
window.configure(bg='black')
window.resizable(True,True)




def origin():
    word = text.get()
    word_origin = ety.origins(word)
    txt_output.insert(END,word_origin)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def tree():
    word = text.get()
    word_tree = ety.tree(word)
    txt_output.insert(END,word_tree)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def meaning():
    word = text.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    word_meaning = api.get_definition(response)
    txt_output.insert(END,word_meaning)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def synonyms():
    word = text.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    word_synonyms = api.get_synonyms(response)
    txt_output.insert(END,word_synonyms)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def pos():
    word = text.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    word_pos = api.get_pos(response)
    txt_output.insert(END,word_pos)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def antonym():
    word = text.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    word_antonym = api.get_antonym(response)
    txt_output.insert(END,word_antonym)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def phonetic():
    word = text.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    word_antonym = api.get_phonetic(response)
    txt_output.insert(END,word_antonym)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def audio():
    word = text.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    word_antonym = api.get_audio(response)
    context = ssl.create_default_context(cafile=certifi.where())
    result = urllib.request.urlopen(word_antonym, context=context)
    txt_output.insert(END,'speaking...')
    with open("./test.mp3","wb") as output:
        output.write(result.read())
    playsound("./test.mp3")
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')


def example():
    word = text.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    word_example = api.get_example(response)
    txt_output.insert(END,word_example)
    txt_output.insert(END,'\n')
    txt_output.insert(END,'\n')



#text box
txt_output = Text(height=15, width=80)
txt_output.place(x=210,y=430)


#frame window
frame = Frame(window, width=800,height=350,bg='black')
frame.place(x=100,y=50)


#heading and subheading
heading = Label(frame,text='Literateur',fg='white',bg='black',font=('Mukta',35,'bold'))
heading.place(x=320,y=20)
subheading = Label(frame,text = 'An English language tool for better understanding.',fg='white',bg='black',font=('Annai MN',15))
subheading.place(x=210,y=80)


#word in the searchbar
def on_entry(e):
    text.delete(0,'end')

def on_leave(e):
    if text.get()=='':
        text.insert(0,'Enter a Word')


#searchbar
text = Entry(frame,width=40,fg='grey',bg='black',font=('Microsoft YaHei UI Light',30))
text.place(x=20,y=140)
text.insert(0,'Enter a Word')
text.bind("<FocusIn>",on_entry)
text.bind("<FocusOut>",on_leave)


#buttons
Button(frame,width=150,pady=2,text='Meaning',bg='grey',fg='black',border=0,command=meaning).place(x=20,y=230)
Button(frame,width=150,pady=2,text='Origin',bg='grey',fg='black',border=0,command=origin).place(x=230,y=230)
Button(frame,width=150,pady=2,text='Etymological Tree',bg='grey',fg='black',border=0,command=tree).place(x=440,y=230)
Button(frame,width=150,pady=2,text='Synonyms',bg='grey',fg='black',border=0,command=synonyms).place(x=650,y=230)
Button(frame,width=150,pady=2,text='Parts of Speech',bg='grey',fg='black',border=0,command=pos).place(x=20,y=270)
Button(frame,width=150,pady=2,text='Antonyms',bg='grey',fg='black',border=0,command=antonym).place(x=230,y=270)
Button(frame,width=150,pady=2,text='Phonetics',bg='grey',fg='black',border=0,command=phonetic).place(x=440,y=270)
Button(frame,width=150,pady=2,text='Pronounciation',bg='grey',fg='black',border=0,command=audio).place(x=650,y=270)
Button(frame,width=150,pady=2,text='Example in Sentence',bg='grey',fg='black',border=0,command=example).place(x=335,y=320)


#to run the main loop
window.mainloop()


