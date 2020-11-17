import random
from tkinter import *
import tkinter.ttk as ttk
import criptografia as cript


#Funções    

def plus_click():
    global key
    if key < 55294:
        key += 1
    else:
        key = key
    keylabel['text'] = key


def minus_click():
    global key
    if key > 1:
        key -= 1
    else:
        key = key
    keylabel['text'] = key

def plus_click1():
    global key1
    if key1 < 55294:
        key1 += 1
    else:
        key1 = key1
    keylabel1['text'] = key1


def minus_click1():
    global key1
    if key1 > 1:
        key1 -= 1
    else:
        key1 = key1
    keylabel1['text'] = key1


def encrypt():
     if(variable.get() == 'Criptografia não linear'):
          texto = cript.non_linear_cypher(get_text(crip1), key)
          render_text(result1, texto)
     else: 
          texto = cript.ceasar_cypher(get_text(crip1), key)
          render_text(result1, texto)

 
def decrypt():
     if(variable.get() == 'Criptografia não linear'):
          texto1: str = cript.reverse_non_linear_cypher(get_text(crip2), key1)
          render_text(result2, texto1)
     else:
          texto1: str = cript.ceasar_cypher(get_text(crip2), key1*-1)
          render_text(result2, texto1)

def get_text(reference: object) -> str:
     return reference.get('1.0', END).strip()

def render_text(reference: object, value: str) -> None:
     reference.delete('1.0', END)
     reference.insert('1.0', value)

    
#Main window
root = Tk()
root.geometry('720x650')
root.resizable(False,False)
root.title('Tela de Criptografia')


#Variáveis
texto = ' '
texto1 = ' '
final_message = ''
key = 3
key1 = 3
options = ['Criptografia linear', 'Criptografia não linear', 'Criptografia linear']

#Abas
abas = ttk.Notebook()
aba1 = Frame(abas)
aba2 = Frame(abas)


aba1.configure(background = '#add8e6')
aba2.configure(background = '#add8e6')


abas.add(aba1, text = 'Criptografar')
abas.add(aba2, text = 'Descriptografar')


abas.place(relx=0, rely=0,relwidth=0.98, relheight=0.98)



"""Editar Chave """
#Button +
mButton = ttk.Button(aba1, width = 10, text = "+", command = plus_click, cursor = 'hand2')
mButton.place(x = 205, y = 320)

#Texto Chave
keylabelM = Label(aba1, width = 10, height = 1, text = "Chave", bg = '#add8e6')
keylabelM.place(x = 115, y = 280)
keylabel = Label(aba1, width = 10, height = 1, text = key, relief = 'solid', bg = 'white')
keylabel.place(x = 115, y = 300)

#Button -
pButton = ttk.Button(aba1, width = 10, text = "-", command = minus_click, cursor = 'hand2')
pButton.place(x = 30, y = 320)

"""Editar Chave Aba 2"""
#Button +
mButton1 = ttk.Button(aba2, width = 10, text = "+", command = plus_click1, cursor = 'hand2')
mButton1.place(x = 205, y = 320)

#Texto Chave
keylabelM1 = Label(aba2, width = 10, height = 1, text = "Chave", bg = '#add8e6')
keylabelM1.place(x = 115, y = 280)
keylabel1 = Label(aba2, width = 10, height = 1, text = key1, relief = 'solid', bg = 'white')
keylabel1.place(x = 115, y = 300)

#Button -
pButton = ttk.Button(aba2, width = 10, text = "-", command = minus_click1, cursor = 'hand2')
pButton.place(x = 30, y = 320)


"""Criptografar"""
#Title
title = Label (aba1, text = "Joséfa Criptografias", bg = '#add8e6')
title.place(bordermode = OUTSIDE, height = 60, x = 30, y = 1)
title.config(font=("Courier", 40))

#Label
label1 = Label(aba1, text = "Criptografar Texto", bg = '#add8e6')
label1.place(bordermode = OUTSIDE, height = 30, x = 320, y = 75 )

#Text
crip1 = Text(aba1, width = 40, height = 15)
crip1.place(bordermode = OUTSIDE, height = 150, width = 550, x = 80, y = 120)

#Botão
button1 = ttk.Button(aba1, text = 'Criptografar', command = encrypt, cursor = 'hand2')
button1.place(bordermode = INSIDE, height = 30, width = 100, x = 510, y = 320)

#Label
label2 = Label(aba1, text = 'Texto Criptografado', bg = '#add8e6')
label2.place(bordermode = INSIDE, height = 30, x = 308, y = 360)
    
#Resultado
result1 = Text(aba1, width = 40, height = 15)
result1.place(bordermode = INSIDE, height = 150, width = 550, x = 80, y = 400)

#Seleção de Criptografia
variable = StringVar(aba1)   
variable.set('Criptografia Não Linear')
select = ttk.OptionMenu(aba1, variable, *options)
select.place(x = 315, y = 320)

     
    
"""Descriptografar"""
#Title
title1 = Label (aba2, text = "Joséfa Criptografias", bg = '#add8e6')
title1.place(bordermode = OUTSIDE, height = 60, x = 30, y = 1)
title1.config(font=("Courier", 40))

#Label
label3 = Label(aba2, text = "Descriptografar Texto", bg = '#add8e6')
label3.place(bordermode = INSIDE,height = 30 , x = 310, y = 75)

#Text
crip2 = Text(aba2, width=40, height=15)
crip2.place(bordermode = INSIDE, height = 150, width = 550, x = 80, y = 120)

#Button
button2 = ttk.Button(aba2, text='Descriptografar', command = decrypt, cursor = 'hand2')
button2.place(bordermode = INSIDE, height = 30, width = 100, x = 510, y = 320)

#Label
label4 = Label(aba2, text = 'Texto Descriptografado', bg = '#add8e6')
label4.place(bordermode = INSIDE, height = 30, x = 308, y = 360)

#Resultado
result2 = Text(aba2, width = 40, height = 15)
result2.place(bordermode = INSIDE, height = 150, width = 550, x = 80, y = 400)


#Seleção de Criptografia
variable1 = StringVar(aba2)   
variable1.set('Criptografia Não Linear')
select1 = ttk.OptionMenu(aba2, variable, *options)
select1.place(x = 315, y = 320)

"""Runs main window"""
root.mainloop()
