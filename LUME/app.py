import customtkinter as ctk

# Importando todas as telas
from tela_inicial import TelaInicial   # nova tela inicial
from login import TelaLogin
from menu import TelaMenu
from catalogo import TelaCatalogo
from carrinho import TelaCarrinho
from pagamento import TelaPagamento
from relatorios import TelaRelatorios
from admin import TelaAdmin
from clientes import TelaClientes
from vendas import TelaVendas
from cadastro_jogo import TelaCadastroJogo
from config import TelaConfig
from sobre import TelaSobre
from suporte import TelaSuporte


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Loja de Games")
        self.geometry("500x600")

        # Dicionário para armazenar as telas
        self.telas = {}

        # Inicializar telas
        self.inicializar_telas()

        # Mostrar tela inicial (Splash) primeiro
        self.mostrar_tela("TelaInicial")

        # Depois de 3 segundos, muda para Login automaticamente
        self.after(3000, lambda: self.mostrar_tela("TelaLogin"))

    def inicializar_telas(self):
        # Criar instâncias de cada tela e armazenar no dicionário
        self.telas["TelaInicial"] = TelaInicial(self)   # nova tela
        self.telas["TelaLogin"] = TelaLogin(self)
        self.telas["TelaMenu"] = TelaMenu(self)
        self.telas["TelaCatalogo"] = TelaCatalogo(self)
        self.telas["TelaCarrinho"] = TelaCarrinho(self)
        self.telas["TelaPagamento"] = TelaPagamento(self)
        self.telas["TelaRelatorios"] = TelaRelatorios(self)
        self.telas["TelaAdmin"] = TelaAdmin(self)
        self.telas["TelaClientes"] = TelaClientes(self)
        self.telas["TelaVendas"] = TelaVendas(self)
        self.telas["TelaCadastroJogo"] = TelaCadastroJogo(self)
        self.telas["TelaConfig"] = TelaConfig(self)
        self.telas["TelaSobre"] = TelaSobre(self)
        self.telas["TelaSuporte"] = TelaSuporte(self)

        # Posicionar todas as telas (empilhadas, mas escondidas)
        for tela in self.telas.values():
            tela.pack(fill="both", expand=True)

    def mostrar_tela(self, nome_tela):
        # Esconder todas as telas
        for tela in self.telas.values():
            tela.pack_forget()
        # Mostrar a tela desejada
        self.telas[nome_tela].pack(fill="both", expand=True)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Tema escuro
    app = App()
    app.mainloop()
