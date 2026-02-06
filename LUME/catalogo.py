import customtkinter as ctk
from PIL import Image

class TelaCatalogo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Título
        ctk.CTkLabel(
            self, text="Catálogo de Produtos",
            font=("Arial", 28, "bold"), text_color="#FFD700"
        ).pack(pady=(20,10))

        # Frame rolável
        corpo = ctk.CTkScrollableFrame(self, fg_color="#162447", height=400)
        corpo.pack(fill="both", expand=True, padx=20, pady=(0,10))

        # Lista de produtos
        self.produtos = [
            {"nome": "One Shot", "tipo": "Jogo", "preco": "R$120,00", "imagem": "imagens/oneshot.png"},
            {"nome": "Stardew Valley", "tipo": "Jogo", "preco": "R$80,00", "imagem": "imagens/stardew.png"},
            {"nome": "Minecraft", "tipo": "Jogo", "preco": "R$150,00", "imagem": "imagens/minecraft.png"},
            {"nome": "PS4", "tipo": "Console", "preco": "R$2.500,00", "imagem": "imagens/ps4.png"},
            {"nome": "Xbox", "tipo": "Console", "preco": "R$2.300,00", "imagem": "imagens/xbox.png"},
            {"nome": "Teclado Mecânico", "tipo": "Periférico", "preco": "R$350,00", "imagem": "imagens/teclado.png"},
        ]

        for produto in self.produtos:
            frame_prod = ctk.CTkFrame(corpo, fg_color="#1F4068", corner_radius=8)
            frame_prod.pack(fill="x", padx=12, pady=8)

            # Carregar imagem
            try:
                img = ctk.CTkImage(
                    light_image=Image.open(produto["imagem"]),
                    dark_image=Image.open(produto["imagem"]),
                    size=(60, 60)
                )
                ctk.CTkLabel(frame_prod, image=img, text="").pack(side="left", padx=10, pady=5)
            except Exception as e:
                print(f"Erro ao carregar imagem {produto['imagem']}: {e}")

            # Texto
            info_frame = ctk.CTkFrame(frame_prod, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, padx=5)

            ctk.CTkLabel(
                info_frame, text=produto["nome"],
                font=("Arial", 16, "bold"), text_color="#FFD700"
            ).pack(anchor="w", pady=2)

            ctk.CTkLabel(
                info_frame, text=f"Tipo: {produto['tipo']}  |  Preço: {produto['preco']}",
                text_color="#FFFFFF", font=("Arial", 12)
            ).pack(anchor="w", pady=2)

            # Botão comprar
            ctk.CTkButton(
                frame_prod,
                text="Comprar",
                fg_color="#FFD700",
                hover_color="#FFC300",
                text_color="#1A1A2E",
                width=100,
                command=lambda p=produto: self.comprar_produto(p)
            ).pack(side="right", padx=12, pady=10)

        # Botão voltar
        ctk.CTkButton(
            self,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(pady=(0,20))

    def comprar_produto(self, produto):
        # Usa o add_to_cart que está no master (vindo da TelaCarrinho)
        if hasattr(self.master, "add_to_cart"):
            self.master.add_to_cart(produto)

        # Mensagem temporária
        msg = ctk.CTkLabel(
            self, text=f"{produto['nome']} adicionado ao carrinho!",
            text_color="#7CFC00"
        )
        msg.pack(pady=5)
        self.after(2000, msg.destroy)  # desaparece após 2 segundos