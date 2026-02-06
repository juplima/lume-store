import customtkinter as ctk

class TelaCarrinho(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Garantir que exista uma "cart" no master (app)
        if not hasattr(master, "cart"):
            master.cart = []

        # Cabeçalho
        ctk.CTkLabel(self, text="Carrinho de Compras", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame rolável para itens
        self.scroll = ctk.CTkScrollableFrame(self, fg_color="#162447", width=760, height=360)
        self.scroll.pack(padx=20, pady=10, fill="both", expand=False)

        # Rodapé (total + botões)
        rodape = ctk.CTkFrame(self, fg_color="#162447")
        rodape.pack(fill="x", padx=20, pady=(5,20))

        self.total_label = ctk.CTkLabel(rodape, text="Total: R$0,00", font=("Arial", 16, "bold"), text_color="#FFFFFF")
        self.total_label.pack(side="left", padx=10)

        ctk.CTkButton(
            rodape,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(side="right", padx=10)

        ctk.CTkButton(
            rodape,
            text="Finalizar Compra",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.finalizar_compra
        ).pack(side="right", padx=10)

        # Se o master não tiver um helper para adicionar ao carrinho, cria um
        if not hasattr(master, "add_to_cart"):
            def add_to_cart(produto):
                """
                produto: dict com pelo menos {"nome": str, "preco": numero ou string "R$xxx,xx"}
                Ex.: {"nome":"Minecraft", "preco":"R$150,00"} ou {"nome":"Minecraft", "preco":150.0}
                """
                master.cart.append(produto)
                # se esta tela estiver visível, atualiza lista
                if isinstance(self.master.telas.get("TelaCarrinho"), TelaCarrinho):
                    self.refresh()
            master.add_to_cart = add_to_cart

        # Renderiza itens iniciais
        self.refresh()

    # --- utilitários ---
    def _parse_price(self, preco):
        """Tenta converter preço em float (aceita float/int ou strings tipo 'R$1.234,56' ou '1234.56')."""
        if preco is None:
            return 0.0
        if isinstance(preco, (int, float)):
            return float(preco)
        s = str(preco).strip()
        s = s.replace("R$", "").replace(" ", "")
        # transformar "1.234,56" -> "1234.56"
        s = s.replace(".", "").replace(",", ".")
        try:
            return float(s)
        except:
            return 0.0

    def _format_brl(self, valor):
        """Formata float em 'R$1.234,56' (estilo BR)."""
        return f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    # --- atualização da lista ---
    def refresh(self):
        # limpa scroll
        for w in self.scroll.winfo_children():
            w.destroy()

        if not getattr(self.master, "cart", []):
            ctk.CTkLabel(self.scroll, text="Seu carrinho está vazio.", text_color="#FFFFFF", font=("Arial", 14)).pack(pady=30)
            self.total_label.configure(text="Total: R$0,00")
            return

        total = 0.0
        for idx, produto in enumerate(self.master.cart):
            # criar card do item
            card = ctk.CTkFrame(self.scroll, fg_color="#1F4068", corner_radius=8)
            card.pack(fill="x", padx=10, pady=8)

            nome = produto.get("nome") if isinstance(produto, dict) else str(produto)
            preco_raw = produto.get("preco") if isinstance(produto, dict) else 0
            preco_val = self._parse_price(preco_raw)
            total += preco_val

            # Nome e preço
            ctk.CTkLabel(card, text=nome, font=("Arial", 14, "bold"), text_color="#FFD700").pack(side="left", padx=12, pady=10)
            ctk.CTkLabel(card, text=self._format_brl(preco_val), font=("Arial", 13), text_color="#FFFFFF").pack(side="left", padx=12)

            # Botão remover (à direita)
            ctk.CTkButton(
                card,
                text="Remover",
                fg_color="#FF6B6B",
                hover_color="#FF8787",
                text_color="#1A1A2E",
                width=100,
                command=lambda i=idx: self.remover_item(i)
            ).pack(side="right", padx=12, pady=8)

        # atualiza total
        self.total_label.configure(text=f"Total: {self._format_brl(total)}")

    def remover_item(self, index):
        try:
            self.master.cart.pop(index)
        except Exception:
            pass
        self.refresh()

    def finalizar_compra(self):
        if not getattr(self.master, "cart", []):
            info = ctk.CTkLabel(self, text="Carrinho vazio — adicione produtos antes de finalizar.", text_color="#FF0000")
            info.pack(pady=5)
            self.after(3000, info.destroy)
            return
        # copia itens para checkout (a TelaPagamento pode usar master.checkout_items)
        self.master.checkout_items = list(self.master.cart)
        # navegar para tela de pagamento
        self.master.mostrar_tela("TelaPagamento")