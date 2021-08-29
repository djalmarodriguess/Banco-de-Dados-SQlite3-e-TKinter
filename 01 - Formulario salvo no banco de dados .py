'''Os valores e os texto solicidados serão salvos no em um banco de dados '''

from tkinter import *
import sqlite3

janela = Tk()
janela.title('Cadastro')
#janela['bg'] = '#dde'

con = sqlite3.connect('agenda.db')
cursor = con.cursor()

#Criar tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS agenda (
    nome TEXT, 
    telefone INTEGER, 
    email TEXT, 
    observação TEXT)""")

con.commit()
con.close()

#Criar função adicionar 
def adicionar():

    #Criar banco de dados e cursor
    con = sqlite3.connect('agenda.db')
    cursor = con.cursor()

    #Inserir dados no banco
    cursor.execute("INSERT INTO agenda VALUES (:nome, :telefone, :email, :observacao)",
                    {
                        'nome': nome.get(),
                        'telefone': telefone.get(),
                        'email': email.get(),
                        'observacao': observacao.get(),
                    }
             )
    
    con.commit()
    con.close()

    #Limpar os dados após serem adicionados
    nome.delete(0,END)
    telefone.delete(0,END)
    email.delete(0,END)
    observacao.delete(0,END)


#Criar função Consulta(query)
def consulta():
    #Criar banco de dados e cursor
    con = sqlite3.connect('agenda.db')
    cursor = con.cursor()

    #Consulta ao banco de dados
    cursor.execute("SELECT *,oid FROM agenda")
    registro  = cursor.fetchall()

    #Loop mostrar registros
    imprimir_registro = ''
    for i in registro:
        imprimir_registro = imprimir_registro + str(i[0]) + '\n'

    lb_consulta = Label(janela, text = imprimir_registro)
    lb_consulta.grid(row=6, column=0, columnspan=2)

    con.commit()
    con.close()

#Criar caixa de texto Label
lb_nome = Label(janela, text= 'Nome')
lb_nome.grid(row= 0 , column=0)

lb_telefone = Label(janela, text= 'Telefone')
lb_telefone.grid(row= 1 , column=0)

lb_email = Label(janela, text= 'E-mail')
lb_email.grid(row= 2 , column=0)

lb_observacao = Label(janela, text= 'Observação')
lb_observacao.grid(row= 3 , column=0)

#Caixa de texto
nome = Entry(janela, width=30)
nome.grid(row=0, column=1, padx=20)

telefone = Entry(janela, width=30)
telefone.grid(row=1, column=1, padx=20)

email = Entry(janela, width=30)
email.grid(row=2, column=1, padx=20)

observacao = Text(janela, width=23, height=5 )
observacao.grid(row=3, column=1, padx=20)

#Botão para adicionar os dados 
adicionar = Button(janela, text= 'Adicionar dados', command=adicionar)
adicionar.grid(row = 4, column=0, columnspan=2, pady=10, padx =10, ipadx=100  )

#Botão para consultar(query) os dados 
consultar = Button(janela, text= 'Mostrar Dados', command=consulta)
consultar.grid(row = 5, column=0, columnspan=2, pady=10, padx =10, ipadx=137  )

janela.geometry('400x400')

janela.mainloop()