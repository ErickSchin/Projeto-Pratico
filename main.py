import tkinter as tk
from tkinter import messagebox
from typing import Self
from PIL import Image, ImageTk

# ---------- VARIÁVEIS GLOBAIS ----------
itens = []
total_sem_desconto = 0
desconto_aplicado = 0
valor_desconto_exibido = 0 # Nova variável para exibir o valor do desconto

# ---------- FUNÇÕES PRINCIPAIS ----------
def toggle_fullscreen():
    """Alterna o modo de tela cheia da janela."""
    current_state = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not current_state)

def minimizar():
    """Minimiza a janela principal."""
    root.iconify()

def atualizar_total():
    """Atualiza o total da compra e o valor do desconto."""
    global total_sem_desconto, valor_desconto_exibido
    total_sem_desconto = sum(preco * qtd for _, preco, qtd in itens)
    valor_desconto_exibido = total_sem_desconto * desconto_aplicado
    total_com_desconto = total_sem_desconto - valor_desconto_exibido

    total_label.config(text=f"Total: R$ {total_com_desconto:.2f}")
    desconto_label.config(text=f"Desconto: R$ {valor_desconto_exibido:.2f}")

        # Preço do produto
        tk.Label(root, text="Preço (R$):", font=Self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.preco_entry = tk.Entry(root, font=self.fonte)
        self.preco_entry.grid(row=1, column=1, padx=10, pady=10)

        # Quantidade do produto
        tk.Label(root, text="Quantidade", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.qtd_entry = tk.Entry(root, font=self.fonte)
        self.qtd_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botão de adicionar
        self.add_button = tk.Button(root, text="Adicionar item", font=self.fonte, command=self.adicionar_item, bg="darkgreen", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Lista de produtos
        self.lista_box = tk.Listbox(root, width=80, height=20, font=self.fonte, bg="white", fg="black")
        self.lista_box.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

        # Total
        self.total_label = tk.Label(root, text="Total: R$ 0.00", font=self.fonte, fg=self.fg_color, bg=self.bg_color)
        self.total_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Botão finalizar compra
        self.finalizar_button = tk.Button(root, text="Finalizar compra", font=self.fonte, command=self.finalizar_compra, bg="darkred", fg="white")
        self.finalizar_button.grid(row=6, column=0, columnspan=2, pady=20)

        # Tecla Esc para sair
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def adicionar_item(self):
        nome = self.nome_entry.get()
        try:
            preco = float(self.preco_entry.get())
            qtd = int(self.qtd_entry.get())
            if nome:
                subtotal = preco * qtd
                self.itens.append((nome, preco, qtd))
                self.lista_box.insert(tk.END, f"{nome} x {qtd} - R$ {preco:.2f} cada (Subtotal: R$ {subtotal:.2f})")
                self.atualizar_total()
                self.nome_entry.delete(0, tk.END)
                self.preco_entry.delete(0, tk.END)
                self.qtd_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Por favor, insira o nome do produto.")
        except ValueError:
            messagebox.showerror("Erro", "Preço ou quantidade inválidos. Use apenas números.")

    def atualizar_total(self):
        total = sum(preco * qtd for _, preco, qtd in self.itens)
        self.total_label.config(text=f"Total: R$ {total:.2f}")

    def finalizar_compra(self):
        if self.itens:
            total = sum(preco * qtd for _, preco, qtd in self.itens)
            messagebox.showinfo("Compra finalizada", f"Total da compra: R$ {total:.2f}")
            self.itens.clear()
            self.lista_box.delete(0, tk.END)
            self.atualizar_total()
        else:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do produto.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}. Preço ou quantidade devem ser números positivos.")

def remover_item():
    """Remove o item selecionado da lista de compras."""
    try:
        selected_index = lista_box.curselection()
        if selected_index:
            index_to_remove = selected_index[0]
            itens.pop(index_to_remove)
            lista_box.delete(index_to_remove)
            atualizar_total()
        else:
            messagebox.showwarning("Aviso", "Selecione um item para remover.")
    except IndexError:
        messagebox.showwarning("Aviso", "Nenhum item selecionado ou lista vazia.")

def limpar_lista():
    """Limpa todos os itens da lista de compras."""
    if messagebox.askyesno("Confirmação", "Deseja realmente limpar toda a lista de compras?"):
        global itens, desconto_aplicado
        itens.clear()
        lista_box.delete(0, tk.END)
        desconto_aplicado = 0
        atualizar_total()
        messagebox.showinfo("Lista Limpa", "A lista de compras foi esvaziada.")

def aplicar_cupom():
    """Aplica um cupom de desconto à compra."""
    global desconto_aplicado
    cupom = cupom_entry.get().strip().upper()
    cupons_validos = {
        "DESCONTO10%": 0.10,
        "DESCONTO50%": 0.50,
        "DESCONTO100%": 1.00 # Cuidado: 100% de desconto!
    }
    if cupom in cupons_validos:
        desconto_aplicado = cupons_validos[cupom]
        atualizar_total()
        messagebox.showinfo("Cupom Aplicado", f"Cupom '{cupom}' aplicado com sucesso! Desconto de {desconto_aplicado*100:.0f}%.")
    else:
        messagebox.showerror("Cupom Inválido", "Cupom não reconhecido ou expirado.")
    cupom_entry.delete(0, tk.END)

def exibir_popup_imagem():
    """Exibe um popup com a imagem do código PIX."""
    popup = tk.Toplevel(root)
    popup.title("Pagamento PIX")
    popup.configure(bg="#F0F0F0") # Cor de fundo mais clara para o popup

    try:
        imagem_popup = Image.open("C:\\Users\\erick\\Documents\\Projeto-Pratico\\codigo pix.png")
        imagem_popup = imagem_popup.resize((300, 300), Image.Resampling.LANCZOS)
        popup_img = ImageTk.PhotoImage(imagem_popup)

        label_imagem = tk.Label(popup, image=popup_img, bg="#F0F0F0")
        label_imagem.image = popup_img # Manter referência para evitar garbage collection
        label_imagem.pack(padx=20, pady=20)
    except FileNotFoundError:
        messagebox.showerror("Erro de Imagem", "Não foi possível carregar a imagem do código PIX. Verifique o caminho.")
        popup.destroy()
        return

    fechar_button = tk.Button(popup, text="Fechar", font=("Arial", 12, "bold"), command=popup.destroy, bg="#E74C3C", fg="white", activebackground="#C0392B")
    fechar_button.pack(pady=10)

def finalizar_compra():
    """Finaliza a compra, exibe o total e o popup de pagamento."""
    global itens, desconto_aplicado
    if itens:
        if messagebox.askyesno("Confirmar Compra", "Deseja finalizar a compra?"):
            total = total_sem_desconto * (1 - desconto_aplicado)
            messagebox.showinfo("Compra Finalizada", f"Total da compra: R$ {total:.2f}")
            exibir_popup_imagem()
            itens.clear()
            lista_box.delete(0, tk.END)
            desconto_aplicado = 0
            atualizar_total()
    else:
        messagebox.showinfo("Nenhum Item", "Nenhum item foi adicionado à lista de compras.")

def buscar_item():
    """Busca e destaca itens na lista."""
    termo_busca = busca_entry.get().strip().lower()
    lista_box.selection_clear(0, tk.END) # Limpa seleções anteriores

    if not termo_busca:
        return

    for i, (nome, _, _) in enumerate(itens):
        if termo_busca in nome.lower():
            lista_box.selection_set(i)
            lista_box.see(i) # Rola para o item encontrado
            # Você pode adicionar um highlight visual aqui se desejar, como mudar a cor do fundo do item

# ---------- INTERFACE GRÁFICA ----------
root = tk.Tk()
root.title("Caixa Registradora - Supermercado XYZ")
root.configure(bg="#2C3E50") # Azul escuro para o fundo

largura_janela = 1200
altura_janela = 800
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
root.resizable(True, True) # Permite redimensionar a janela

# Definindo fontes e cores
fonte_titulo = ("Arial", 24, "bold")
fonte_labels = ("Arial", 14)
fonte_entries = ("Arial", 14)
fonte_botoes = ("Arial", 14, "bold")

cor_texto_claro = "#ECF0F1" # Cinza claro
cor_fundo_escuro = "#34495E" # Cinza azulado escuro
cor_fundo_claro = "#F0F0F0" # Cinza muito claro
cor_botao_add = "#27AE60" # Verde esmeralda
cor_botao_remover = "#E74C3C" # Vermelho tijolo
cor_botao_limpar = "#F39C12" # Laranja
cor_botao_cupom = "#3498DB" # Azul brilhante
cor_botao_finalizar = "#C0392B" # Vermelho escuro
cor_lista_fundo = "#FFFFFF" # Branco puro

# ---------- TÍTULO ----------
title_label = tk.Label(root, text="Caixa Registradora - Supermercado XYZ", font=fonte_titulo, fg=cor_texto_claro, bg=root["bg"])
title_label.grid(row=0, column=0, columnspan=4, pady=20, sticky="n")

# ---------- LOGO ----------
try:
    imagem_logo = Image.open("C:\\Users\\erick\\Documents\\Projeto-Pratico\\logo.png")
    imagem_logo = imagem_logo.resize((120, 120), Image.Resampling.LANCZOS)
    logo_img = ImageTk.PhotoImage(imagem_logo)
    logo_label = tk.Label(root, image=logo_img, bg=root["bg"])
    logo_label.grid(row=0, column=3, rowspan=3, padx=20, pady=20, sticky="ne")
except FileNotFoundError:
    messagebox.showwarning("Erro de Imagem", "Não foi possível carregar a imagem do logo. Verifique o caminho.")
    logo_label = tk.Label(root, text="LOGO", font=fonte_labels, fg=cor_texto_claro, bg=root["bg"])
    logo_label.grid(row=0, column=3, rowspan=3, padx=20, pady=20, sticky="ne")


# ---------- FRAME DE ENTRADAS E BOTÕES DE AÇÃO ----------
input_frame = tk.Frame(root, bg=cor_fundo_escuro, padx=15, pady=15, relief="raised", bd=2)
input_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nw")

tk.Label(input_frame, text="Nome do produto:", font=fonte_labels, fg=cor_texto_claro, bg=input_frame["bg"]).grid(row=0, column=0, sticky="w", pady=5)
nome_entry = tk.Entry(input_frame, font=fonte_entries, width=30)
nome_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Preço (R$):", font=fonte_labels, fg=cor_texto_claro, bg=input_frame["bg"]).grid(row=1, column=0, sticky="w", pady=5)
preco_entry = tk.Entry(input_frame, font=fonte_entries, width=30)
preco_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Quantidade:", font=fonte_labels, fg=cor_texto_claro, bg=input_frame["bg"]).grid(row=2, column=0, sticky="w", pady=5)
qtd_entry = tk.Entry(input_frame, font=fonte_entries, width=30)
qtd_entry.grid(row=2, column=1, pady=5)

add_button = tk.Button(input_frame, text="Adicionar Item", font=fonte_botoes, command=adicionar_item, bg=cor_botao_add, fg="white", activebackground="#229954", relief="flat")
add_button.grid(row=3, column=0, columnspan=2, pady=15, ipadx=10, ipady=5)

# ---------- LISTA DE ITENS ----------
lista_frame = tk.Frame(root, bg=cor_fundo_escuro, padx=15, pady=15, relief="raised", bd=2)
lista_frame.grid(row=1, column=2, rowspan=5, padx=20, pady=10, sticky="nsew") # Ajustado para ocupar mais espaço

lista_box = tk.Listbox(lista_frame, width=60, height=20, font=fonte_labels, bg=cor_lista_fundo, fg="black", selectbackground="#A9CCE3", selectforeground="black")
lista_box.pack(expand=True, fill="both")

# ---------- BOTÕES DE MANIPULAÇÃO DA LISTA ----------
list_buttons_frame = tk.Frame(root, bg=root["bg"])
list_buttons_frame.grid(row=6, column=2, padx=20, pady=10, sticky="ew")

remover_button = tk.Button(list_buttons_frame, text="Remover Item", font=fonte_botoes, command=remover_item, bg=cor_botao_remover, fg="white", activebackground="#CB4335", relief="flat")
remover_button.pack(side="left", padx=5, pady=5, expand=True, fill="x")

limpar_button = tk.Button(list_buttons_frame, text="Limpar Lista", font=fonte_botoes, command=limpar_lista, bg=cor_botao_limpar, fg="white", activebackground="#D68910", relief="flat")
limpar_button.pack(side="left", padx=5, pady=5, expand=True, fill="x")

# ---------- ÁREA DE CUPOM E TOTAIS ----------
finance_frame = tk.Frame(root, bg=cor_fundo_escuro, padx=15, pady=15, relief="raised", bd=2)
finance_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="sew")

tk.Label(finance_frame, text="Cupom de desconto:", font=fonte_labels, fg=cor_texto_claro, bg=finance_frame["bg"]).grid(row=0, column=0, sticky="w", pady=5)
cupom_entry = tk.Entry(finance_frame, font=fonte_entries, width=20)
cupom_entry.grid(row=0, column=1, pady=5, sticky="ew")

aplicar_cupom_button = tk.Button(finance_frame, text="Aplicar Cupom", font=fonte_botoes, command=aplicar_cupom, bg=cor_botao_cupom, fg="white", activebackground="#2874A6", relief="flat")
aplicar_cupom_button.grid(row=1, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

desconto_label = tk.Label(finance_frame, text="Desconto: R$ 0.00", font=fonte_labels, fg=cor_texto_claro, bg=finance_frame["bg"])
desconto_label.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

total_label = tk.Label(finance_frame, text="Total: R$ 0.00", font=("Arial", 18, "bold"), fg="#2ECC71", bg=finance_frame["bg"]) # Verde para o total
total_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

finalizar_button = tk.Button(root, text="Finalizar Compra", font=fonte_botoes, command=finalizar_compra, bg=cor_botao_finalizar, fg="white", activebackground="#943126", relief="flat")
finalizar_button.grid(row=7, column=0, columnspan=2, pady=20, ipadx=20, ipady=10, sticky="ew")

# ---------- BUSCA DE ITENS ----------
busca_frame = tk.Frame(root, bg=cor_fundo_escuro, padx=15, pady=15, relief="raised", bd=2)
busca_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nw")

tk.Label(busca_frame, text="Buscar Item:", font=fonte_labels, fg=cor_texto_claro, bg=busca_frame["bg"]).grid(row=0, column=0, sticky="w", pady=5)
busca_entry = tk.Entry(busca_frame, font=fonte_entries, width=30)
busca_entry.grid(row=0, column=1, pady=5)

busca_button = tk.Button(busca_frame, text="Buscar", font=fonte_botoes, command=buscar_item, bg=cor_botao_cupom, fg="white", activebackground="#2874A6", relief="flat")
busca_button.grid(row=1, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

# ---------- BOTÕES DE CONTROLE DA JANELA ----------
control_buttons_frame = tk.Frame(root, bg=root["bg"])
control_buttons_frame.grid(row=8, column=0, columnspan=4, pady=10)

fullscreen_button = tk.Button(control_buttons_frame, text="Alternar Tela Cheia", font=fonte_botoes, command=toggle_fullscreen, bg="#5D6D7E", fg="white", activebackground="#4A5868", relief="flat")
fullscreen_button.pack(side="left", padx=10)

minimizar_button = tk.Button(control_buttons_frame, text="Minimizar", font=fonte_botoes, command=minimizar, bg="#5D6D7E", fg="white", activebackground="#4A5868", relief="flat")
minimizar_button.pack(side="left", padx=10)

# Configurações de peso das colunas e linhas para redimensionamento
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=2) # Lista ocupa mais espaço
root.grid_columnconfigure(3, weight=0) # Logo fixo

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=0)
root.grid_rowconfigure(7, weight=0)
root.grid_rowconfigure(8, weight=0)

# Atalhos de teclado
root.bind("<Escape>", lambda e: root.destroy())
root.protocol("WM_DELETE_WINDOW", minimizar)

root.mainloop()