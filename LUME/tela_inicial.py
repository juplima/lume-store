import customtkinter as ctk
from PIL import Image

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Exemplo de logo (se não tiver imagem, só vai mostrar o texto)
        try:
            logo = ctk.CTkImage(
                light_image=Image.open("imagens/logo.png"),  # substitua pela sua logo
                dark_image=Image.open("imagens/logo.png"),
                size=(120, 120)
            )
            ctk.CTkLabel(self, image=logo, text="").pack(pady=(80,20))
        except:
            ctk.CTkLabel(
                self, text="LOGO",
                font=("Arial", 36, "bold"), text_color="#FFD700"
            ).pack(pady=(80,20))

        # Nome do app
        ctk.CTkLabel(
            self, text="LUME STORE",
            font=("Arial", 32, "bold"), text_color="#FFD700"
        ).pack(pady=(10,40))

        # Mensagem de carregamento
        ctk.CTkLabel(
            self, text="Carregando...",
            font=("Arial", 14), text_color="#FFFFFF"
        ).pack()

        # Depois de 5 segundos, vai para o Login
        self.after(3000, lambda: master.mostrar_tela("TelaLogin"))