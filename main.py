import tkinter as tk
from tkinter import messagebox, font

class CaixaRegistradora:
    def __init__(self, root):
        self.root = root
        self.root.title("Caixa Registradora - Supermercado")

        # Tela cheia
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="gray")

        self.itens = []

        # Fonte de alto contraste
        self.fonte = ("Arial", 16, "bold")
        self.fg_color = "white"
        self.bg_color = "gray"

        # Nome do produto
        tk.Label(root, text="Nome do produto:", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.nome_entry = tk.Entry(root, font=self.fonte)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        # Preço do produto
        tk.Label(root, text="Preço (R$):", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.preco_entry = tk.Entry(root, font=self.fonte)
        self.preco_entry.grid(row=1, column=1, padx=10, pady=10)

        # Botão de adicionar
        self.add_button = tk.Button(root, text="Adicionar item", font=self.fonte, command=self.adicionar_item, bg="darkgreen", fg="white")
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista de produtos
        self.lista_box = tk.Listbox(root, width=80, height=20, font=self.fonte, bg="white", fg="black")
        self.lista_box.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

        # Total
        self.total_label = tk.Label(root, text="Total: R$ 0.00", font=self.fonte, fg=self.fg_color, bg=self.bg_color)
        self.total_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Botão finalizar compra
        self.finalizar_button = tk.Button(root, text="Finalizar compra", font=self.fonte, command=self.finalizar_compra, bg="darkred", fg="white")
        self.finalizar_button.grid(row=5, column=0, columnspan=2, pady=20)

        # Tecla Esc para sair
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def adicionar_item(self):
        nome = self.nome_entry.get()
        try:
            preco = float(self.preco_entry.get())
            if nome:
                self.itens.append((nome, preco))
                self.lista_box.insert(tk.END, f"{nome} - R$ {preco:.2f}")
                self.atualizar_total()
                self.nome_entry.delete(0, tk.END)
                self.preco_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Por favor, insira o nome do produto.")
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido. Use apenas números.")

    def atualizar_total(self):
        total = sum(preco for _, preco in self.itens)
        self.total_label.config(text=f"Total: R$ {total:.2f}")

    def finalizar_compra(self):
        if self.itens:
            total = sum(preco for _, preco in self.itens)
            messagebox.showinfo("Compra finalizada", f"Total da compra: R$ {total:.2f}")
            self.itens.clear()
            self.lista_box.delete(0, tk.END)
            self.atualizar_total()
        else:
            messagebox.showinfo("Nenhum item", "Nenhum item foi adicionado.")

# Executar
if __name__ == "__main__":
    root = tk.Tk()
    app = CaixaRegistradora(root)
    root.mainloop()
