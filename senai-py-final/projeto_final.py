import sqlite3 # banco de dados
import tkinter as tk # interface basica
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb

def conectar():
    return sqlite3.connect('teste.db')


def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        nome TEXT NOT NULL,            
        idade REAL NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        imc FLOAT NOT NULL             
        )       
    ''')
    conn.commit()
    conn.close()
def calc_imc():
    nome = entry_nome.get()
    idade = entry_idade.get()
    peso =  float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / (altura **2)
    return imc

# CREATE
def inserir_usuario():
    nome = entry_nome.get()
    idade = entry_idade.get()
    peso =  float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / (altura **2)
    
    if nome and idade:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(nome,idade,peso,altura,imc) VALUES(?,?,?,?,?)', (nome,idade,peso,altura,imc))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 
    

# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2],usuario[3],usuario[4]))
    conn.close()    


# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       nome = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE nome = ? ',(nome,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()

    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  

# UPDATE 
       
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_idade = entry_idade.get()
         novo_peso = entry_peso.get()
         novo_altura = entry_altura.get()
         if novo_nome and novo_idade:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , SET idade = ? , SET peso = ? , SET altura = ?, SET imc = ? WHERE id = ? ',(novo_nome,novo_idade,novo_altura,novo_peso,user_id,),)
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')


janela = tk.Tk()
janela.geometry('1230x600')
janela.title('calculator IMC')


label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=1, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text = 'idade:')
label_idade.grid(row=2, column=0, padx=10, pady=10)

entry_idade = tk.Entry(janela, text = 'idade:')
entry_idade.grid(row=2, column=1, padx=10, pady=10)


label_peso = tk.Label(janela, text = 'peso:')
label_peso.grid(row=3, column=0, padx=10, pady=10)

entry_peso = tk.Entry(janela, text = 'peso:')
entry_peso.grid(row=3, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text = 'altura:')
label_altura.grid(row=4,column=0,padx=10,pady=10)

entry_altura = tk.Entry(janela , text = 'altura:')
entry_altura.grid(row=4,column=1,padx=10,pady=10)

btn_salvar = tk.Button(janela, text='Salvar e Concluir', command=inserir_usuario )
btn_salvar.grid(row=5, column=1, padx=10, pady=10)

btn_deletar = tk.Button(janela, text='deletar', command=delete_usuario )
btn_deletar.grid(row=30, column=0, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text='atualizar', command=editar)
btn_atualizar.grid(row=25, column=0, padx=10, pady=10)



columns = ('NOME', 'IDADE', 'ALTURA', 'PESO','IMC')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=10,column=0,columnspan=2,padx=10, pady=10)


for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()


janela.mainloop()