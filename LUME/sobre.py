import customtkinter as ctk

class TelaSobre(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Título
        ctk.CTkLabel(
            self,
            text="Sobre o Sistema",
            font=("Arial", 28, "bold"),
            text_color="#FFD700"
        ).pack(pady=(20,10))

        # Texto de descrição
        descricao = (
            "📌 Sistema LUME - Gestão de Ativos Fixos\n\n"
            "O LUME foi desenvolvido para auxiliar pequenas empresas na gestão eficiente\n"
            "de seus ativos, oferecendo funcionalidades como:\n"
            "✔ Cadastro e controle de ativos\n"
            "✔ Cálculo de depreciação\n"
            "✔ Relatórios e insights\n"
            "✔ Metodologia PRINCE2 aplicada\n\n"
            "Este sistema foi construído em Python com interface gráfica moderna\n"
            "utilizando a biblioteca CustomTkinter."
        )

        ctk.CTkLabel(
            self,
            text=descricao,
            text_color="#FFFFFF",
            font=("Arial", 14),
            justify="left",
            wraplength=600
        ).pack(padx=20, pady=20)

        # Créditos
        ctk.CTkLabel(
            self,
            text="👩‍💻 Desenvolvido por: Equipe LUME\n📅 Ano: 2025",
            text_color="#FFD700",
            font=("Arial", 12, "italic")
        ).pack(pady=(0,20))

        # Botão voltar
        ctk.CTkButton(
            self,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(pady=10)