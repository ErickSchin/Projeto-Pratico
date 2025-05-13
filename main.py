import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ---------- VARIÁVEIS GLOBAIS ----------
itens = []
total_sem_desconto = 0
desconto_aplicado = 0

# ---------- FUNÇÕES PRINCIPAIS ----------
def toggle_fullscreen():
    current_state = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not current_state)

def minimizar():
    root.iconify()

def atualizar_total():
    global total_sem_desconto
    total_sem_desconto = sum(preco * qtd for _, preco, qtd in itens)
    total_com_desconto = total_sem_desconto * (1 - desconto_aplicado)
    total_label.config(text=f"Total: R$ {total_com_desconto:.2f}")

def adicionar_item():
    nome = nome_entry.get()
    try:
        preco = float(preco_entry.get())
        qtd = int(qtd_entry.get())
        if preco <= 0 or qtd <= 0:
            raise ValueError
        if nome:
            subtotal = preco * qtd
            itens.append((nome, preco, qtd))
            lista_box.insert(tk.END, f"{nome} x {qtd} - R$ {preco:.2f} cada (Subtotal: R$ {subtotal:.2f})")
            atualizar_total()
            nome_entry.delete(0, tk.END)
            preco_entry.delete(0, tk.END)
            qtd_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do produto.")
    except ValueError:
        messagebox.showerror("Erro", "Preço ou quantidade inválidos. Use apenas números positivos.")

def aplicar_cupom():
    global desconto_aplicado
    cupom = cupom_entry.get().strip().upper()
    cupons_validos = {
        "DESCONTO10%": 0.10,
        "DESCONTO50%": 0.50,
        "DESCONTO100%": 1.00
    }
    if cupom in cupons_validos:
        desconto_aplicado = cupons_validos[cupom]
        atualizar_total()
        messagebox.showinfo("Cupom aplicado", f"Cupom {cupom} aplicado com sucesso!")
    else:
        messagebox.showerror("Cupom inválido", "Cupom não reconhecido.")
    cupom_entry.delete(0, tk.END)

def exibir_popup_imagem():
    popup = tk.Toplevel(root)
    popup.title("Pagamento PIX")
    popup.configure(bg="white")

    imagem_popup = Image.open("C:\\Users\\erick\\Documents\\Projeto-Pratico\\codigo pix.png")
    imagem_popup = imagem_popup.resize((400, 400), Image.Resampling.LANCZOS)
    popup_img = ImageTk.PhotoImage(imagem_popup)

    label_imagem = tk.Label(popup, image=popup_img, bg="white")
    label_imagem.image = popup_img
    label_imagem.pack(padx=20, pady=20)

    fechar_button = tk.Button(popup, text="Fechar", font=fonte, command=popup.destroy, bg="darkred", fg="white")
    fechar_button.pack(pady=10)

def finalizar_compra():
    global itens, desconto_aplicado
    if itens:
        total = total_sem_desconto * (1 - desconto_aplicado)
        messagebox.showinfo("Compra finalizada", f"Total da compra: R$ {total:.2f}")
        exibir_popup_imagem()
        itens.clear()
        lista_box.delete(0, tk.END)
        desconto_aplicado = 0
        atualizar_total()
    else:
        messagebox.showinfo("Nenhum item", "Nenhum item foi adicionado.")

# ---------- INTERFACE ----------
root = tk.Tk()
root.title("Caixa Registradora - Supermercado")
root.configure(bg="gray")

largura_janela = 1000
altura_janela = 700
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

fonte = ("Arial", 16, "bold")
fg_color = "white"
bg_color = "gray"

# ---------- LOGO ----------
imagem_logo = Image.open("C:\\Users\\erick\\Documents\\Projeto-Pratico\\logo.png")
imagem_logo = imagem_logo.resize((150, 150), Image.Resampling.LANCZOS)
logo_img = ImageTk.PhotoImage(imagem_logo)
logo_label = tk.Label(root, image=logo_img, bg=bg_color)
logo_label.grid(row=0, column=3, rowspan=3, padx=20, pady=20, sticky="ne")

# ---------- ENTRADAS ----------
tk.Label(root, text="Nome do produto:", font=fonte, fg=fg_color, bg=bg_color).grid(row=0, column=0, sticky="e", padx=10, pady=10)
nome_entry = tk.Entry(root, font=fonte)
nome_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Preço (R$):", font=fonte, fg=fg_color, bg=bg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
preco_entry = tk.Entry(root, font=fonte)
preco_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Quantidade", font=fonte, fg=fg_color, bg=bg_color).grid(row=2, column=0, sticky="e", padx=10, pady=10)
qtd_entry = tk.Entry(root, font=fonte)
qtd_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Adicionar item", font=fonte, command=adicionar_item, bg="darkgreen", fg="white")
add_button.grid(row=3, column=0, columnspan=2, pady=10)

lista_box = tk.Listbox(root, width=80, height=20, font=fonte, bg="white", fg="black")
lista_box.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

tk.Label(root, text="Cupom de desconto:", font=fonte, fg=fg_color, bg=bg_color).grid(row=5, column=0, padx=10, pady=10)
cupom_entry = tk.Entry(root, font=fonte)
cupom_entry.grid(row=5, column=1, padx=10, pady=10)

aplicar_cupom_button = tk.Button(root, text="Aplicar Cupom", font=fonte, command=aplicar_cupom, bg="blue", fg="white")
aplicar_cupom_button.grid(row=6, column=0, columnspan=2, pady=10)

total_label = tk.Label(root, text="Total: R$ 0.00", font=fonte, fg=fg_color, bg=bg_color)
total_label.grid(row=7, column=0, columnspan=2, pady=10)

finalizar_button = tk.Button(root, text="Finalizar compra", font=fonte, command=finalizar_compra, bg="darkred", fg="white")
finalizar_button.grid(row=8, column=0, columnspan=2, pady=20)

fullscreen_button = tk.Button(root, text="Alternar Fullscreen", font=fonte, command=toggle_fullscreen, bg="gray", fg="white")
fullscreen_button.grid(row=9, column=0, columnspan=2, pady=10)

root.bind("<Escape>", lambda e: root.destroy())
root.protocol("WM_DELETE_WINDOW", minimizar)

root.mainloop()
