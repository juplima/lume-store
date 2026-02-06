import customtkinter as ctk

class TelaAdmin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # fundo azul escuro

        # Título
        ctk.CTkLabel(self, text="Painel Administrativo", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame principal
        corpo = ctk.CTkFrame(self, fg_color="#162447", corner_radius=8)
        corpo.pack(fill="both", expand=True, padx=20, pady=(0,10))

        # Botões administrativos
        botoes_frame = ctk.CTkFrame(corpo, fg_color="#162447")
        botoes_frame.pack(fill="x", padx=12, pady=12)

        ctk.CTkButton(
            botoes_frame,
            text="Adicionar Produto",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.adicionar_produto
        ).pack(side="left", padx=8, pady=8)

        ctk.CTkButton(
            botoes_frame,
            text="Remover Produto",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.remover_produto
        ).pack(side="left", padx=8, pady=8)

        ctk.CTkButton(
            botoes_frame,
            text="Ver Pedidos",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.ver_pedidos
        ).pack(side="left", padx=8, pady=8)

        # Área de logs / informações
        self.log_frame = ctk.CTkScrollableFrame(corpo, fg_color="#1F4068", height=300)
        self.log_frame.pack(fill="both", expand=True, padx=12, pady=10)

        # Botão voltar
        ctk.CTkButton(
            self,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(pady=(0,20))

        self.refresh_log()

    # --- Funções de exemplo ---
    def adicionar_produto(self):
        if not hasattr(self.master, "produtos"):
            self.master.produtos = []

        # exemplo: adiciona produto genérico
        novo_produto = {"nome": "Produto Novo", "preco": "R$100,00", "tipo": "Outro"}
        self.master.produtos.append(novo_produto)
        self.refresh_log()

    def remover_produto(self):
        if hasattr(self.master, "produtos") and self.master.produtos:
            self.master.produtos.pop()
        self.refresh_log()

    def ver_pedidos(self):
        if not hasattr(self.master, "orders"):
            self.master.orders = []
        self.refresh_log(ver_pedidos=True)

    # --- Atualiza log_frame ---
    def refresh_log(self, ver_pedidos=False):
        for w in self.log_frame.winfo_children():
            w.destroy()

        if ver_pedidos:
            orders = getattr(self.master, "orders", [])
            if not orders:
                ctk.CTkLabel(self.log_frame, text="Nenhum pedido registrado.", text_color="#FFFFFF").pack(pady=10)
                return
            for idx, pedido in enumerate(orders, start=1):
                text = f"Pedido {idx}: "
                produtos_str = ", ".join([p.get("nome","Produto") if isinstance(p, dict) else str(p) for p in pedido])
                ctk.CTkLabel(self.log_frame, text=text + produtos_str, text_color="#FFFFFF", font=("Arial", 12)).pack(anchor="w", padx=10, pady=4)
        else:
            produtos = getattr(self.master, "produtos", [])
            if not produtos:
                ctk.CTkLabel(self.log_frame, text="Nenhum produto cadastrado.", text_color="#FFFFFF").pack(pady=10)
                return
            for idx, p in enumerate(produtos, start=1):
                nome = p.get("nome", "Produto") if isinstance(p, dict) else str(p)
                preco = p.get("preco", "R$0,00") if isinstance(p, dict) else "R$0,00"
                tipo = p.get("tipo", "Outro") if isinstance(p, dict) else "Outro"
                ctk.CTkLabel(self.log_frame, text=f"{idx}. {nome} - {tipo} - {preco}", text_color="#FFFFFF", font=("Arial", 12)).pack(anchor="w", padx=10, pady=4)