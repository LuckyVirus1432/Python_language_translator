#Importing required python librarires for GUI Python Translator
from tkinter import *
from tkinter import ttk, messagebox   #ttk is like CSS in HTML which helps to style the tkinter gui & widgets.
from googletrans import LANGUAGES   # Importiong LANGUAGES from googletrans library.
import textblob


# Creating object of a tkinter class which is a gui window.
root = Tk()
# Setting a size of the window "width x height"
root.geometry("900x400")
# setting windows size unchangable or not resizable
root.resizable(0,0)
# Setting window background color
root['bg'] = 'black'
# Setting the title of the tkinter object/window
root.title('Python Translator by LuckyVirus')

Label(root, text="Language Translator", font="Arial 20 bold", fg='red', bg='black').pack()

'''*****************************************************************************************************************************'''

# Function to change label of choosen language in GUI.
def label_change():
    c1 = from_lang1.get()
    c2 = dest_lang.get()
    from_label.configure(text=c1)
    dest_label.configure(text=c2)
    root.after(1000, label_change)

# Function to translate the text into choosen language
def translateLang():
    global language     # Accesssing global variable inside the function
    try:                # To handle exceptions we use try-except block
        text_ = text1.get(1.0, END) # To get inputed text from text1.
        c3 = from_lang1.get()   # Get the language from which user want to convert his text.
        c4 =dest_lang.get()     # Get the language which is choosen by user to convert the text into.
        if(text_):
            words = textblob.TextBlob(text_)    
            lan = c3
            for i,j in language.items():
                if(j==c4):
                    lan_ = i
            words=words.translate(from_lang=lan, to=str(lan_))  # Translating the words into destination language
            text2.delete(1.0, END)  # Deleting already exixting text from output box.
            text2.insert(END, words) # Inserting the translated text into output box.
    except Exception as e:
        # If exception occurs in try block, will be handled here by showing an eroor message to the user.
        messagebox.showerror("Python Translator", "Can not translate, Please try again..!")


# LANGUAGES is the dictionary of all languages with key value pairs.
language = LANGUAGES
languageV = list(LANGUAGES.values())    # Will print the values which are present inside the LANGUAGES dictionary.
lang = language.keys()  # Will print all keys present inside the LANGUAGES dictionary.

'''*****************************************************************************************************************************'''

# Creating a combobox. Combobox widget combines a text field with a pop-down list of values.
from_lang1 = ttk.Combobox(root, values= languageV, width=30, state='r')
from_lang1.place(x=140, y=60)
from_lang1.set("From language")

# Creating a label. Label widget which can display text and bitmaps.
from_label = Label(root, text="English", font='segoe 13', bg='green2', width=30, bd=5, relief=GROOVE)
from_label.place(x=90, y=100)

# Creating a frame in a window. It is a special widget which may contain other widgets and can have a 3D border.
f = Frame(root, bg='aqua', bd=5)
f.place(x=50, y=150, width=380, height=210)

# Creting a text widget which can display text in various forms.
text1 = Text(f, font='arial 13', bg='white', relief=GROOVE, wrap=WORD, pady=10)
text1.place(x=0, y=0, width=370, height=200)

# Creating a scrollbar which display a slider in a frame to scroll the text.
scrollbar1 = Scrollbar(f)
scrollbar1.pack(side='right', fill='y')
scrollbar1.configure(command=text1.yview)
text1.config(yscrollcommand=scrollbar1.set)

'''****************************************************************************************************************************'''

dest_lang = ttk.Combobox(root, values= languageV, width=30, state='r')
dest_lang.place(x=550, y=60)
dest_lang.set("To language")

dest_label = Label(root, text="Choose Language", font='segoe 13', bg='green3', width=30, bd=5, relief=GROOVE)
dest_label.place(x=530, y=100)

f2 = Frame(root, bg='aqua', bd=5)
f2.place(x=450, y=150, width=380, height=210)

text2 = Text(f2, font='arial 13', bg='white', relief=GROOVE, wrap=WORD, pady=10)
text2.place(x=0, y=0, width=370, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side='right', fill='y')
scrollbar2.configure(command=text2.yview)
text2.config(yscrollcommand=scrollbar2.set)

'''*****************************************************************************************************************************'''
# Creating a button to translate the text. 
trans_btn = Button(root, text="Translate", font="arial 12", pady=5, bd=5, bg="orange", command= translateLang, activebackground="green", cursor='hand2')
trans_btn.place(x=410, y=100)

# Calling a funtion.
label_change()

'''
The mainloop() method is responsible for executing the script and displaying the output window.
However, mainloop() implies that it doesn't terminate automatically until the user remains in the window.
Whenever the user terminates the program, it gets closed automatically.
'''
root.mainloop()


