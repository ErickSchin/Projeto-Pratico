import tkinter as tk
from tkinter import messagebox

class CaixaRegistradora:
    def __init__(self, root):
        self.root = root
        self.root.title("Caixa Registradora - Supermercado")
        self.root.geometry("1024x768")
        self.root.configure(bg="gray")

        self.itens = []
        self.fonte = ("Arial", 16, "bold")
        self.fg_color = "white"
        self.bg_color = "gray"

        controle_frame = tk.Frame(self.root, bg="gray")
        controle_frame.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

        btn_min = tk.Button(controle_frame, text="_", font=self.fonte, width=3, command=self.minimizar, bg="lightgray")
        btn_min.grid(row=0, column=0)

        btn_max = tk.Button(controle_frame, text="🗖", font=self.fonte, width=3, command=self.toggle_fullscreen, bg="lightgray")
        btn_max.grid(row=0, column=1)

        btn_close = tk.Button(controle_frame, text="X", font=self.fonte, width=3, command=self.root.destroy, bg="red", fg="white")
        btn_close.grid(row=0, column=2)

        tk.Label(root, text="Nome do produto:", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.nome_entry = tk.Entry(root, font=self.fonte)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Preço (R$):", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.preco_entry = tk.Entry(root, font=self.fonte)
        self.preco_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(root, text="Quantidade", font=self.fonte, fg=self.fg_color, bg=self.bg_color).grid(row=3, column=0, sticky="e", padx=10, pady=10)
        self.qtd_entry = tk.Entry(root, font=self.fonte)
        self.qtd_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Adicionar item", font=self.fonte, command=self.adicionar_item, bg="darkgreen", fg="white")
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.lista_box = tk.Listbox(root, width=80, height=20, font=self.fonte, bg="white", fg="black")
        self.lista_box.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

        self.total_label = tk.Label(root, text="Total: R$ 0.00", font=self.fonte, fg=self.fg_color, bg=self.bg_color)
        self.total_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.finalizar_button = tk.Button(root, text="Finalizar compra", font=self.fonte, command=self.finalizar_compra, bg="darkred", fg="white")
        self.finalizar_button.grid(row=7, column=0, columnspan=2, pady=20)

        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def minimizar(self):
        self.root.iconify()

    def toggle_fullscreen(self):
        is_fullscreen = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not is_fullscreen)

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
            messagebox.showinfo("Nenhum item", "Nenhum item foi adicionado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaixaRegistradora(root)
    root.mainloop()
