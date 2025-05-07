import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Classe principal da aplicação
class CaixaRegistradora:
    def __init__(self, root):
        # Configuração da janela principal
        self.root = root
        self.root.title("Caixa Registradora - Supermercado")
        self.root.attributes('-fullscreen', True)  # Tela cheia inicial
        self.root.configure(bg="gray")

        # Variáveis de controle
        self.itens = []  # Lista de itens adicionados
        self.total_sem_desconto = 0
        self.desconto_aplicado = 0

        # Estilo visual
        self.fonte = ("Arial", 16, "bold")
        self.fg_color = "white"
        self.bg_color = "gray"

        # ---------- LOGO ----------
        # Carrega e exibe a imagem do logo
        imagem_logo = Image.open("C:\\Users\\erick\\Documents\\Projeto-Pratico\\logo.png")
        imagem_logo = imagem_logo.resize((150, 150), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(imagem_logo)
        self.logo_label = tk.Label(root, image=self.logo_img, bg=self.bg_color)
        self.logo_label.grid(row=0, column=3, rowspan=3, padx=20, pady=20, sticky="ne")

        # ---------- ENTRADAS DE DADOS ----------
        # Nome do produto
        tk.Label(root, text="Nome do produto:", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.nome_entry = tk.Entry(root, font=self.fonte)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        # Preço do produto
        tk.Label(root, text="Preço (R$):", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.preco_entry = tk.Entry(root, font=self.fonte)
        self.preco_entry.grid(row=1, column=1, padx=10, pady=10)

        # Quantidade do produto
        tk.Label(root, text="Quantidade", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.qtd_entry = tk.Entry(root, font=self.fonte)
        self.qtd_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botão para adicionar o item
        self.add_button = tk.Button(root, text="Adicionar item", font=self.fonte, command=self.adicionar_item, bg="darkgreen", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # ---------- LISTA DE ITENS ----------
        self.lista_box = tk.Listbox(root, width=80, height=20, font=self.fonte, bg="white", fg="black")
        self.lista_box.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

        # ---------- CUPOM DE DESCONTO ----------
        tk.Label(root, text="Cupom de desconto:", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=5, column=0, padx=10, pady=10)
        self.cupom_entry = tk.Entry(root, font=self.fonte)
        self.cupom_entry.grid(row=5, column=1, padx=10, pady=10)

        self.aplicar_cupom_button = tk.Button(root, text="Aplicar Cupom", font=self.fonte, command=self.aplicar_cupom, bg="blue", fg="white")
        self.aplicar_cupom_button.grid(row=6, column=0, columnspan=2, pady=10)

        # ---------- TOTAL ----------
        self.total_label = tk.Label(root, text="Total: R$ 0.00", font=self.fonte, fg=self.fg_color, bg=self.bg_color)
        self.total_label.grid(row=7, column=0, columnspan=2, pady=10)

        # ---------- FINALIZAR COMPRA ----------
        self.finalizar_button = tk.Button(root, text="Finalizar compra", font=self.fonte, command=self.finalizar_compra, bg="darkred", fg="white")
        self.finalizar_button.grid(row=8, column=0, columnspan=2, pady=20)

        # ---------- ALTERNAR FULLSCREEN ----------
        self.fullscreen_button = tk.Button(root, text="Alternar Fullscreen", font=self.fonte, command=self.toggle_fullscreen, bg="gray", fg="white")
        self.fullscreen_button.grid(row=9, column=0, columnspan=2, pady=10)

        # Atalho para sair com Esc
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Redefine o comportamento de fechar a janela para minimizar
        self.root.protocol("WM_DELETE_WINDOW", self.minimizar)

    # ---------- FUNÇÕES DE CONTROLE DA JANELA ----------

    def toggle_fullscreen(self):
        # Alterna entre modo tela cheia e modo janela
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)

    def minimizar(self):
        # Minimiza a janela principal
        self.root.iconify()

    # ---------- LÓGICA DE ADIÇÃO E CÁLCULO ----------

    def adicionar_item(self):
        # Lê os dados das entradas, valida e adiciona o item à lista de compras
        nome = self.nome_entry.get()
        try:
            preco = float(self.preco_entry.get())
            qtd = int(self.qtd_entry.get())
            if nome:
                subtotal = preco * qtd
                self.itens.append((nome, preco, qtd))
                self.lista_box.insert(
                    tk.END,
                    f"{nome} x {qtd} - R$ {preco:.2f} cada (Subtotal: R$ {subtotal:.2f})"
                )
                self.atualizar_total()
                self.nome_entry.delete(0, tk.END)
                self.preco_entry.delete(0, tk.END)
                self.qtd_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Por favor, insira o nome do produto.")
        except ValueError:
            messagebox.showerror("Erro", "Preço ou quantidade inválidos. Use apenas números.")

    def atualizar_total(self):
        # Recalcula o total dos itens considerando o desconto
        self.total_sem_desconto = sum(preco * qtd for _, preco, qtd in self.itens)
        total_com_desconto = self.total_sem_desconto * (1 - self.desconto_aplicado)
        self.total_label.config(text=f"Total: R$ {total_com_desconto:.2f}")

    def aplicar_cupom(self):
        # Aplica um cupom de desconto se válido
        cupom = self.cupom_entry.get().strip().upper()
        cupons_validos = {
            "DESCONTO10%": 0.10,
            "DESCONTO50%": 0.50,
            "DESCONTO100%": 1.00
        }
        if cupom in cupons_validos:
            self.desconto_aplicado = cupons_validos[cupom]
            self.atualizar_total()
            messagebox.showinfo("Cupom aplicado", f"Cupom {cupom} aplicado com sucesso!")
        else:
            messagebox.showerror("Cupom inválido", "Cupom não reconhecido.")
        self.cupom_entry.delete(0, tk.END)

    def finalizar_compra(self):
        # Finaliza a compra, exibe o valor final e o popup com o código PIX
        if self.itens:
            total = self.total_sem_desconto * (1 - self.desconto_aplicado)
            messagebox.showinfo("Compra finalizada", f"Total da compra: R$ {total:.2f}")
            self.exibir_popup_imagem()
            self.itens.clear()
            self.lista_box.delete(0, tk.END)
            self.desconto_aplicado = 0
            self.atualizar_total()
        else:
            messagebox.showinfo("Nenhum item", "Nenhum item foi adicionado.")

    def exibir_popup_imagem(self):
        # Mostra um popup com o código QR do PIX
        popup = tk.Toplevel(self.root)
        popup.title("Pagamento PIX")
        popup.configure(bg="white")

        imagem_popup = Image.open("C:\\Users\\erick\\Documents\\Projeto-Pratico\\codigo pix.png")
        imagem_popup = imagem_popup.resize((400, 400), Image.Resampling.LANCZOS)
        self.popup_img = ImageTk.PhotoImage(imagem_popup)

        label_imagem = tk.Label(popup, image=self.popup_img, bg="white")
        label_imagem.pack(padx=20, pady=20)

        fechar_button = tk.Button(popup, text="Fechar", font=self.fonte, command=popup.destroy, bg="darkred", fg="white")
        fechar_button.pack(pady=10)

# ---------- EXECUÇÃO DA APLICAÇÃO ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = CaixaRegistradora(root)
    root.mainloop()
