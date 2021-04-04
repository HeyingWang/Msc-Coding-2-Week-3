#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()                               # create the window
window.title('The longest word')
window.geometry('800x300')                     # Modify the size of the window frame


# Answers, Clue Tags

tk.Label(window, text='Answer ',font=('SourceSansPro-Regular', 14)).place(x=50, y=190)
tk.Label(window, text='Clue ',font=('SourceSansPro-Regular', 14)).place(x=400, y=190)
e2 = tk.Entry(window, show=None, font=('SourceSansPro-Regular', 14))     # Entry control for entering Answer
e2.place(x=110, y=190)
e3 = tk.Entry(window, show=None, font=('SourceSansPro-Regular', 14))     # Entry control for entering Get the clues
e3.place(x=450, y=190)



# Place the corresponding tabs and Entry controls on the window and position them well
tk.Label(window, text='Group A= hbacplpyd', font=('SourceSansPro-Regular', 14)).place(x=50, y=40)
tk.Label(window, text='Group B= remind you happy forever', font=('SourceSansPro-Regular',14)).place(x=50, y=80)
tk.Label(window, text='Find the longest word in the Group B that can be formed by deleting some characters of the Group A.', font=('SourceSansPro-Regular', 14)).place(x=50, y=120)
tk.Label(window, text='Attention: if you want to get the clues, try to input "clue"+"number"', font=('SourceSansPro-Light', 12)).place(x=50, y=160)


 # Answer Judgment

def puzzle():
    x = e2.get()
  
    
    if x == 'happy':      
        tkinter.messagebox.showinfo(title= ' Congratulations ' , message = 'You are right!' )
    else:
        tkinter.messagebox.showwarning(title='Sorry', message='Is that the answer? Think again.')
        
 # Clue Judgment        
        
def clue():
    x = e3.get()
    if x == 'clue1':      
        tkinter.messagebox.showinfo(title= ' Clue1 ' , message = 'Example:Group A= abpcpea,Group B= a b c,Answer=a' )
    elif x == 'clue2':      
        tkinter.messagebox.showinfo(title= ' Clue2 ' , message = 'If there are more than one possible results, return the longest word with the smallest lexicographical order. if there is no possible result, return the empty string.' )
    else:
        tkinter.messagebox.showwarning(title='Sorry', message='You should input correct commands')
        
       
 # Create two keys on the window
    
b_puzzle = tk.Button(window, text='Confirm', font=('SourceSansPro-Regular', 14), command=puzzle).place(x=110, y=230)
b_clue = tk.Button(window, text='Get the clues', font=('SourceSansPro-Regular', 14), command=clue).place(x=450, y=230)
window.mainloop()     # Main window cycling display





