import customtkinter as ctk

class TelaCadastroJogo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Título da tela
        ctk.CTkLabel(self, text="Cadastro de Jogos", font=("Arial", 20)).pack(pady=20)

        # Campos para cadastro
        ctk.CTkLabel(self, text="Nome do Jogo").pack(pady=5)
        self.campo_nome = ctk.CTkEntry(self, placeholder_text="Digite o nome do jogo")
        self.campo_nome.pack(pady=5)

        ctk.CTkLabel(self, text="Preço").pack(pady=5)
        self.campo_preco = ctk.CTkEntry(self, placeholder_text="Digite o preço")
        self.campo_preco.pack(pady=5)

        # Botão cadastrar (exemplo)
        ctk.CTkButton(
            self,
            text="Cadastrar",
            command=self.cadastrar_jogo
        ).pack(pady=10)

        # Botão voltar ao menu
        ctk.CTkButton(
            self,
            text="Voltar ao Menu",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(pady=10)

    def cadastrar_jogo(self):
        nome = self.campo_nome.get()
        preco = self.campo_preco.get()
        ctk.CTkLabel(self, text=f"Jogo {nome} cadastrado por R${preco}", text_color="green").pack(pady=5)