'''Os valores e os texto solicidados serão mostrados no próprio terminal ou saída e não serão salvos em um banco de dados '''

from tkinter import *

janela = Tk()
janela.title('Cadastro')
janela['bg'] = '#dde'


def gravarDados():
    print(f'Nome......:{nome.get()}')
    print(f'Telefone..:{telefone.get()}')
    print(f'E-mail....:{email.get()}')
    print(f'Observação:{obs.get(1.0,END)}')

Label(janela, text= 'Nome',bg= 'white', fg= 'blue', anchor=W ).place(x=10, y=10, width=100, height=20)
nome = Entry(janela)
nome.place(x= 10, y= 30, width=200, height=20)

Label(janela, text= 'Telefone',bg= 'white', fg= 'blue', anchor=W ).place(x=10, y=60, width=150, height=20)
telefone = Entry(janela)
telefone.place(x= 10, y= 80, width=100, height=20)

Label(janela, text= 'E-mail',bg= 'white', fg= 'blue', anchor=W ).place(x=10, y=120, width=100, height=20)
email = Entry(janela)
email.place(x= 10, y= 140, width=250, height=20)

Label(janela, text= 'Observação:',bg= 'white', fg= 'blue', anchor=W ).place(x=10, y=170, width=100, height=20)
obs = Text(janela)
obs.place(x= 10, y= 190, width=250, height=100)

Button(janela, text= 'Gravar',bg= 'white', fg= 'blue', anchor=CENTER, command=gravarDados ).place(x=10, y=300, width=100, height=20)

janela.geometry('500x400')
janela.mainloop()
