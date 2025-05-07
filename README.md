📚 Apresentação do Projeto — Sistema de Caixa Registradora com Interface Gráfica
Nome do projeto: Sistema de Caixa Registradora – Supermercado
Tecnologia usada: Python com biblioteca Tkinter
Autor: Erick Schinneyder e Anna Machado
Curso: Ciência da Computação 
Disciplina: Programação de Computadores
Professor: Jeofton

🎯 Objetivo
O objetivo deste projeto foi desenvolver uma interface gráfica funcional para simular um sistema de caixa registradora de supermercado, capaz de registrar produtos, calcular totais automaticamente e finalizar compras de forma prática, acessível e intuitiva. O sistema foi projetado com foco em usabilidade, acessibilidade visual e responsividade.

⚙️ Tecnologias e funcionalidades implementadas
O sistema foi desenvolvido inteiramente em Python, utilizando a biblioteca Tkinter, que permite criar janelas gráficas de forma simples e eficiente.

1. Interface gráfica personalizada
Layout responsivo com uso de grid() para organização.

Estilo de alto contraste: fundo cinza com letras brancas, visando acessibilidade para pessoas com baixa visão.

Tela com botões de controle de janela (minimizar, maximizar/restaurar, fechar) integrados ao topo da interface.

2. Entrada de dados
Campos para inserir nome do produto, preço e quantidade.

Botão de "Adicionar item" que valida os dados e insere o item na lista de compras.

Verificações de entrada: o sistema emite alertas se houver campos vazios ou valores inválidos.

3. Listagem de produtos
Os produtos adicionados são exibidos dinamicamente em uma Listbox, com nome, quantidade, valor unitário e subtotal de cada item.

4. Cálculo automático do total
O sistema atualiza automaticamente o total da compra conforme os itens são adicionados.

Utiliza estrutura de dados (lista de tuplas) para armazenar as informações de cada item.

5. Finalização da compra
Ao clicar em “Finalizar compra”, o sistema:

Exibe o valor total em uma janela de confirmação.

Limpa a lista de produtos.

Reinicia o valor total.

6. Atalhos e usabilidade
A tecla Esc fecha a aplicação instantaneamente.

Os botões são destacados por cores:

Verde para adicionar item.

Vermelho para finalizar compra.

Cinza claro e vermelho para os botões de janela.

7. Integração com sons
Sons são reproduzidos:

Ao adicionar um item (beep.wav).

Ao finalizar a compra (checkout.wav).

O uso de playsound com multithreading garante que os sons não travem a interface.

💡 Considerações técnicas
O código é modular, com separação clara entre funções de interface e lógica de negócio.

As entradas são robustas contra erros, utilizando exceções (try/except) para garantir confiabilidade.

O uso de threading para tocar sons evita bloqueios na interface.

A interface é compatível com resolução de tela cheia, mas pode ser redimensionada.

📈 Aplicações e extensões futuras
Este sistema pode ser facilmente estendido para funcionalidades como:

Geração de cupom fiscal.

Integração com banco de dados (SQLite ou MySQL).

Login de operadores.

Controle de estoque.

Suporte a leitores de código de barras.

✅ Conclusão
O projeto alcança seu objetivo de demonstrar, de forma simples e funcional, o funcionamento de um sistema de PDV (Ponto de Venda). Ele reforça a importância do pensamento lógico, estruturação de interfaces gráficas, validação de dados e experiência do usuário, servindo como uma base sólida para aplicações comerciais mais complexas.

