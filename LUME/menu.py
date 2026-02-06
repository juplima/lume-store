import customtkinter as ctk

class TelaMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configurações gerais
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Título da tela
        ctk.CTkLabel(
            self,
            text="Menu Principal",
            font=("Arial", 28, "bold"),
            text_color="#FFD700"
        ).pack(pady=(40, 30))

        # Botões principais do menu
        botoes = [
            ("Catálogo de Jogos", "TelaCatalogo"),
            ("Carrinho", "TelaCarrinho"),
            ("Pagamentos", "TelaPagamento"),
            ("Clientes", "TelaClientes"),
            ("Vendas", "TelaVendas"),
            ("Administração", "TelaAdmin"),
            ("Configurações", "TelaConfig"),
            ("Sobre", "TelaSobre"),
            ("Suporte", "TelaSuporte")
        ]

        for texto, tela_destino in botoes:
            ctk.CTkButton(
                self,
                text=texto,
                fg_color="#FFD700",
                hover_color="#FFC300",
                text_color="#1A1A2E",
                font=("Arial", 16, "bold"),
                width=300,
                height=50,
                command=lambda t=tela_destino: master.mostrar_tela(t)
            ).pack(pady=10)
