import customtkinter as ctk

class TelaClientes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Inicializa lista de clientes no app principal
        if not hasattr(master, "clientes"):
            master.clientes = []

        # Título
        ctk.CTkLabel(self, text="Clientes", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame de clientes cadastrados
        self.clientes_frame = ctk.CTkScrollableFrame(self, fg_color="#162447", height=300)
        self.clientes_frame.pack(fill="both", expand=True, padx=20, pady=(0,10))

        # Formulário adicionar cliente
        form_frame = ctk.CTkFrame(self, fg_color="#162447", corner_radius=8)
        form_frame.pack(fill="x", padx=20, pady=(0,10))

        ctk.CTkLabel(form_frame, text="Nome:", text_color="#FFFFFF").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nome_entry = ctk.CTkEntry(form_frame, placeholder_text="Digite o nome do cliente")
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Email:", text_color="#FFFFFF").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = ctk.CTkEntry(form_frame, placeholder_text="Digite o email do cliente")
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkButton(
            form_frame,
            text="Adicionar Cliente",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.adicionar_cliente
        ).grid(row=2, column=0, columnspan=2, pady=10)

        # Botão voltar
        ctk.CTkButton(
            self,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(pady=(0,20))

        self.atualizar_clientes()

    def adicionar_cliente(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()

        if nome and email:
            self.master.clientes.append({"nome": nome, "email": email})
            self.nome_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.atualizar_clientes()

    def atualizar_clientes(self):
        # Limpa frame
        for widget in self.clientes_frame.winfo_children():
            widget.destroy()

        if not self.master.clientes:
            ctk.CTkLabel(self.clientes_frame, text="Nenhum cliente cadastrado.", text_color="#FFFFFF").pack(pady=10)
            return

        # Lista clientes
        for idx, cliente in enumerate(self.master.clientes, start=1):
            frame_cliente = ctk.CTkFrame(self.clientes_frame, fg_color="#1F4068", corner_radius=8)
            frame_cliente.pack(fill="x", padx=12, pady=6)

            ctk.CTkLabel(
                frame_cliente,
                text=f"{idx}. {cliente['nome']} - {cliente['email']}",
                text_color="#FFFFFF",
                font=("Arial", 12),
                wraplength=500,
                justify="left"
            ).pack(anchor="w", padx=10, pady=4)