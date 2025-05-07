import tkinter as tk
from tkinter import messagebox, font

class CaixaRegistradora:
    def _init_(self, root):
        self.root = root
        self.root.title("Caixa Registradora - Supermercado")

        self.root.geometry("1024x768")
        self.root.configure(bg="gray")

        self.itens = []
        self.desconto = 0  # percentual de desconto (ex: 0.1 para 10%)

        self.fonte = ("Arial", 16, "bold")
        self.fg_color = "white"
        self.bg_color = "gray"

        # Nome do produto
        tk.Label(root, text="Nome do produto:", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.nome_entry = tk.Entry(root, font=self.fonte)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        # Preço
        tk.Label(root, text="Preço (R$):", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.preco_entry = tk.Entry(root, font=self.fonte)
        self.preco_entry.grid(row=1, column=1, padx=10, pady=10)

        # Quantidade
        tk.Label(root, text="Quantidade:", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.qtd_entry = tk.Entry(root, font=self.fonte)
        self.qtd_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botão adicionar
        self.add_button = tk.Button(root, text="Adicionar item", font=self.fonte, command=self.adicionar_item, bg="darkgreen", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Lista de produtos
        self.lista_box = tk.Listbox(root, width=80, height=15, font=self.fonte, bg="white", fg="black")
        self.lista_box.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

        # Campo de cupom
        tk.Label(root, text="Cupom de desconto:", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=5, column=0, sticky="e", padx=10, pady=10)
        self.cupom_entry = tk.Entry(root, font=self.fonte)
        self.cupom_entry.grid(row=5, column=1, padx=10, pady=10)

        # Botão aplicar cupom
        self.cupom_button = tk.Button(root, text="Aplicar cupom", font=self.fonte, command=self.aplicar_cupom, bg="blue", fg="white")
        self.cupom_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Total
        self.total_label = tk.Label(root, text="Total: R$ 0.00", font=self.fonte, fg=self.fg_color, bg=self.bg_color)
        self.total_label.grid(row=7, column=0, columnspan=2, pady=10)

        # Finalizar compra
        self.finalizar_button = tk.Button(root, text="Finalizar compra", font=self.fonte, command=self.finalizar_compra, bg="darkred", fg="white")
        self.finalizar_button.grid(row=8, column=0, columnspan=2, pady=20)

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
        total_bruto = sum(preco * qtd for _, preco, qtd in self.itens)
        total_com_desconto = total_bruto * (1 - self.desconto)
        self.total_label.config(text=f"Total: R$ {total_com_desconto:.2f} (Desconto: {int(self.desconto*100)}%)")

    def aplicar_cupom(self):
        cupom = self.cupom_entry.get().strip().upper()
        if cupom == "DESCONTO10%":
            self.desconto = 0.10
        elif cupom == "DESCONTO50%":
            self.desconto = 0.50
        elif cupom == "DESCONTO100%":
            self.desconto = 1.00
        else:
            messagebox.showwarning("Cupom inválido", "Cupom não reconhecido. Use: DESCONTO10%, DESCONTO50% ou DESCONTO100%.")
            return
        messagebox.showinfo("Cupom aplicado", f"Cupom {cupom} aplicado com sucesso!")
        self.atualizar_total()

    def finalizar_compra(self):
        if self.itens:
            total_bruto = sum(preco * qtd for _, preco, qtd in self.itens)
            total_final = total_bruto * (1 - self.desconto)
            messagebox.showinfo("Compra finalizada", f"Total da compra: R$ {total_final:.2f}")
            self.itens.clear()
            self.lista_box.delete(0, tk.END)
            self.desconto = 0
            self.cupom_entry.delete(0, tk.END)
            self.atualizar_total()
        else:
            messagebox.showinfo("Nenhum item", "Nenhum item foi adicionado.")

# Executar
if __name__ == "_main_":
    root = tk.Tk()
    app = CaixaRegistradora(root)
    root.mainloop()