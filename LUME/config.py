import customtkinter as ctk

class TelaConfig(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Cabeçalho
        ctk.CTkLabel(self, text="Configurações", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame principal
        corpo = ctk.CTkFrame(self, fg_color="#162447", corner_radius=8)
        corpo.pack(fill="both", expand=True, padx=20, pady=(0,10))

        # Nome do usuário
        ctk.CTkLabel(corpo, text="Nome de Usuário", text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(12,4))
        self.campo_nome = ctk.CTkEntry(corpo, placeholder_text="Digite seu nome")
        self.campo_nome.pack(fill="x", padx=12, pady=4)

        # Email
        ctk.CTkLabel(corpo, text="Email", text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(12,4))
        self.campo_email = ctk.CTkEntry(corpo, placeholder_text="Digite seu email")
        self.campo_email.pack(fill="x", padx=12, pady=4)

        # Senha
        ctk.CTkLabel(corpo, text="Senha", text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(12,4))
        self.campo_senha = ctk.CTkEntry(corpo, placeholder_text="Digite sua senha", show="*")
        self.campo_senha.pack(fill="x", padx=12, pady=4)

        # Tema (Escuro ou Claro)
        ctk.CTkLabel(corpo, text="Tema", text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(12,4))
        self.tema_var = ctk.StringVar(value="dark")
        ctk.CTkRadioButton(corpo, text="Modo Escuro", variable=self.tema_var, value="dark").pack(anchor="w", padx=20, pady=2)
        ctk.CTkRadioButton(corpo, text="Modo Claro", variable=self.tema_var, value="light").pack(anchor="w", padx=20, pady=2)

        # Mensagem de status
        self.status_label = ctk.CTkLabel(self, text="", text_color="#FFFFFF")
        self.status_label.pack(pady=6)

        # Botões
        botoes_frame = ctk.CTkFrame(self, fg_color="#162447")
        botoes_frame.pack(fill="x", padx=20, pady=(10,20))

        ctk.CTkButton(
            botoes_frame,
            text="Salvar Alterações",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.salvar_alteracoes
        ).pack(side="left", padx=10, pady=10)

        ctk.CTkButton(
            botoes_frame,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(side="right", padx=10, pady=10)

        # Preenche campos se houver usuário salvo
        if hasattr(master, "usuario"):
            user = master.usuario
            self.campo_nome.insert(0, user.get("nome", ""))
            self.campo_email.insert(0, user.get("email", ""))
            self.campo_senha.insert(0, user.get("senha", ""))
            self.tema_var.set(user.get("aparencia", "dark"))

    def salvar_alteracoes(self):
        # Salva informações no master.usuario
        if not hasattr(self.master, "usuario"):
            self.master.usuario = {}

        self.master.usuario["nome"] = self.campo_nome.get().strip()
        self.master.usuario["email"] = self.campo_email.get().strip()
        self.master.usuario["senha"] = self.campo_senha.get().strip()
        self.master.usuario["aparencia"] = self.tema_var.get()

        # Atualiza modo de aparência
        ctk.set_appearance_mode(self.tema_var.get())

        self.status_label.configure(text="Alterações salvas com sucesso!", text_color="#7CFC00")