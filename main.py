import tkinter as tk
from tkinter import messagebox

class CaixaRegistradora:
    def __init__(self, root):
        self.root = root
        self.root.title("Caixa Registradora - Supermercado")
        self.itens = []

        tk.Label(root, text="Nome do produto:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(root, text="Preço (R$):").grid(row=1, column=0)
        self.preco_entry = tk.Entry(root)
        self.preco_entry.grid(row=1, column=1)

    
        self.add_button = tk.Button(root, text="Adicionar item", command=self.adicionar_item)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=5)

     
        self.lista_box = tk.Listbox(root, width=40)
        self.lista_box.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

      
        self.total_label = tk.Label(root, text="Total: R$ 0.00")
        self.total_label.grid(row=4, column=0, columnspan=2)

        self.finalizar_button = tk.Button(root, text="Finalizar compra", command=self.finalizar_compra)
        self.finalizar_button.grid(row=5, column=0, columnspan=2, pady=10)

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


if __name__ == "__main__":
    root = tk.Tk()
    app = CaixaRegistradora(root)
    root.mainloop()
