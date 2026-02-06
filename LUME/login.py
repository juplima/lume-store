import customtkinter as ctk

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configurações gerais da tela
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Título e slogan
        ctk.CTkLabel(
            self,
            text="LUME",
            font=("Arial", 32, "bold"),
            text_color="#FFD700"  # Amarelo
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            self,
            text="Onde cada clique é uma nova conquista!",
            font=("Arial", 14),
            text_color="#FFFFFF"
        ).pack(pady=(0, 30))

        # Campo de usuário
        ctk.CTkLabel(self, text="Usuário", text_color="#FFFFFF").pack(pady=(10, 5))
        self.campo_usuario = ctk.CTkEntry(self, placeholder_text="Digite seu usuário", width=300)
        self.campo_usuario.pack(pady=5)

        # Campo de senha
        ctk.CTkLabel(self, text="Senha", text_color="#FFFFFF").pack(pady=(10, 5))
        self.campo_senha = ctk.CTkEntry(self, placeholder_text="Digite sua senha", show="*", width=300)
        self.campo_senha.pack(pady=5)

        # Botão login
        ctk.CTkButton(
            self,
            text="Entrar",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            width=200,
            command=self.validar_login
        ).pack(pady=20)

        # Label de resultado
        self.resultado_login = ctk.CTkLabel(self, text="", text_color="#FF0000")
        self.resultado_login.pack(pady=10)

    def validar_login(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()

        # Usuário de exemplo
        if usuario == "admin" and senha == "123":
            self.resultado_login.configure(text="Login feito com sucesso!", text_color="#00FF00")
            self.master.mostrar_tela("TelaMenu")  # Chama o menu
        else:
            self.resultado_login.configure(text="Usuário ou senha incorretos", text_color="#FF0000")