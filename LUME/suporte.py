import customtkinter as ctk

class TelaSuporte(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Título
        ctk.CTkLabel(self, text="Suporte LUME", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame principal
        corpo = ctk.CTkFrame(self, fg_color="#162447", corner_radius=8)
        corpo.pack(fill="both", expand=True, padx=20, pady=(0,10))

        # Campo de mensagem
        ctk.CTkLabel(corpo, text="Digite sua dúvida ou mensagem:", text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(12,4))
        self.campo_mensagem = ctk.CTkEntry(corpo, placeholder_text="Digite aqui sua mensagem...")
        self.campo_mensagem.pack(fill="x", padx=12, pady=4)

        # Botão enviar
        ctk.CTkButton(
            corpo,
            text="Enviar",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.enviar_mensagem
        ).pack(pady=10)

        # Área de mensagens enviadas
        self.mensagens_frame = ctk.CTkScrollableFrame(corpo, fg_color="#1F4068", height=200)
        self.mensagens_frame.pack(fill="both", expand=True, padx=12, pady=10)

        # Botão voltar
        ctk.CTkButton(
            self,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(pady=(0,20))

        # Inicializa lista de mensagens se não existir
        if not hasattr(master, "suporte_msgs"):
            master.suporte_msgs = []

        self.atualizar_mensagens()

    def enviar_mensagem(self):
        msg = self.campo_mensagem.get().strip()
        if msg:
            self.master.suporte_msgs.append(msg)
            self.campo_mensagem.delete(0, "end")
            self.atualizar_mensagens()

    def atualizar_mensagens(self):
        # Limpa frame
        for widget in self.mensagens_frame.winfo_children():
            widget.destroy()

        # Adiciona mensagens
        for idx, msg in enumerate(self.master.suporte_msgs, start=1):
            ctk.CTkLabel(
                self.mensagens_frame,
                text=f"{idx}. {msg}",
                text_color="#FFFFFF",
                font=("Arial", 12),
                wraplength=500,
                justify="left"
            ).pack(anchor="w", padx=10, pady=4)