import customtkinter as ctk

class TelaVendas(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Título
        ctk.CTkLabel(self, text="Vendas Realizadas", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame principal
        corpo = ctk.CTkScrollableFrame(self, fg_color="#162447", height=400)
        corpo.pack(fill="both", expand=True, padx=20, pady=(0,10))

        # Lista de vendas
        self.vendas_frame = corpo
        self.atualizar_vendas()

        # Botão voltar
        ctk.CTkButton(
            self,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(pady=(0,20))

    def atualizar_vendas(self):
        # Limpa frame
        for widget in self.vendas_frame.winfo_children():
            widget.destroy()

        vendas = getattr(self.master, "orders", [])
        if not vendas:
            ctk.CTkLabel(self.vendas_frame, text="Nenhuma venda realizada.", text_color="#FFFFFF", font=("Arial", 12)).pack(pady=10)
            return

        # Lista as vendas
        for idx, venda in enumerate(vendas, start=1):
            frame_venda = ctk.CTkFrame(self.vendas_frame, fg_color="#1F4068", corner_radius=8)
            frame_venda.pack(fill="x", padx=12, pady=6)

            produtos_texto = ", ".join([p.get("nome", "Produto") if isinstance(p, dict) else str(p) for p in venda])
            ctk.CTkLabel(frame_venda, text=f"Venda {idx}: {produtos_texto}", text_color="#FFFFFF", font=("Arial", 12)).pack(anchor="w", padx=12, pady=4)