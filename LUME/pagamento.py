import customtkinter as ctk

class TelaPagamento(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")  # Fundo azul escuro

        # Cabeçalho
        ctk.CTkLabel(self, text="Pagamento", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame resumo (itens e total)
        resumo_frame = ctk.CTkFrame(self, fg_color="#162447", corner_radius=8)
        resumo_frame.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(resumo_frame, text="Resumo do Pedido", font=("Arial", 16, "bold"), text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(10,5))
        self.resumo_lista = ctk.CTkFrame(resumo_frame, fg_color="#162447")
        self.resumo_lista.pack(fill="x", padx=12, pady=(0,10))

        self.total_label = ctk.CTkLabel(resumo_frame, text="Total: R$0,00", font=("Arial", 16, "bold"), text_color="#FFFFFF")
        self.total_label.pack(anchor="e", padx=12, pady=(0,12))

        # Frame dados do cartão
        dados_frame = ctk.CTkFrame(self, fg_color="#162447", corner_radius=8)
        dados_frame.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(dados_frame, text="Nome no cartão", text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(10,5))
        self.campo_nome = ctk.CTkEntry(dados_frame, placeholder_text="Nome completo")
        self.campo_nome.pack(fill="x", padx=12, pady=5)

        ctk.CTkLabel(dados_frame, text="Número do cartão", text_color="#FFFFFF").pack(anchor="w", padx=12, pady=(10,5))
        self.campo_numero = ctk.CTkEntry(dados_frame, placeholder_text="0000 0000 0000 0000")
        self.campo_numero.pack(fill="x", padx=12, pady=5)

        meio_frame = ctk.CTkFrame(dados_frame, fg_color="#162447")
        meio_frame.pack(fill="x", padx=12, pady=5)

        ctk.CTkLabel(meio_frame, text="Validade (MM/AA)", text_color="#FFFFFF").grid(row=0, column=0, sticky="w", padx=(0,10))
        ctk.CTkLabel(meio_frame, text="CVV", text_color="#FFFFFF").grid(row=0, column=1, sticky="w")

        self.campo_validade = ctk.CTkEntry(meio_frame, placeholder_text="MM/AA", width=120)
        self.campo_validade.grid(row=1, column=0, padx=(0,10), pady=5, sticky="w")
        self.campo_cvv = ctk.CTkEntry(meio_frame, placeholder_text="CVV", width=80, show="*")
        self.campo_cvv.grid(row=1, column=1, pady=5, sticky="w")

        # Mensagem de status
        self.status_label = ctk.CTkLabel(self, text="", text_color="#FFFFFF")
        self.status_label.pack(pady=6)

        # Botões (Voltar / Confirmar)
        botoes_frame = ctk.CTkFrame(self, fg_color="#162447")
        botoes_frame.pack(fill="x", padx=20, pady=(10,20))

        ctk.CTkButton(
            botoes_frame,
            text="Voltar ao Carrinho",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=lambda: master.mostrar_tela("TelaCarrinho")
        ).pack(side="left", padx=10, pady=10)

        ctk.CTkButton(
            botoes_frame,
            text="Confirmar Pagamento",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            command=self.confirmar_pagamento
        ).pack(side="right", padx=10, pady=10)

        # Popula o resumo inicial
        self.refresh()

    # --- utilitários para preço ---
    def _parse_price(self, preco):
        if preco is None:
            return 0.0
        if isinstance(preco, (int, float)):
            return float(preco)
        s = str(preco).strip()
        s = s.replace("R$", "").replace(" ", "")
        s = s.replace(".", "").replace(",", ".")
        try:
            return float(s)
        except:
            return 0.0

    def _format_brl(self, valor):
        return f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    # Atualiza o resumo dos itens + total
    def refresh(self):
        # limpa lista visual
        for w in self.resumo_lista.winfo_children():
            w.destroy()

        items = getattr(self.master, "checkout_items", None)
        if not items:
            # fallback para master.cart se checkout_items não existir
            items = getattr(self.master, "cart", [])

        if not items:
            ctk.CTkLabel(self.resumo_lista, text="Nenhum item para pagamento.", text_color="#FFFFFF").pack(pady=15)
            self.total_label.configure(text="Total: R$0,00")
            return

        total = 0.0
        for prod in items:
            nome = prod.get("nome") if isinstance(prod, dict) else str(prod)
            preco_raw = prod.get("preco") if isinstance(prod, dict) else 0
            preco_val = self._parse_price(preco_raw)
            total += preco_val

            linha = ctk.CTkFrame(self.resumo_lista, fg_color="#1F4068")
            linha.pack(fill="x", pady=6, padx=4)

            ctk.CTkLabel(linha, text=nome, text_color="#FFD700", font=("Arial", 13, "bold")).pack(side="left", padx=8, pady=6)
            ctk.CTkLabel(linha, text=self._format_brl(preco_val), text_color="#FFFFFF", font=("Arial", 12)).pack(side="right", padx=8, pady=6)

        self.total_label.configure(text=f"Total: {self._format_brl(total)}")

    # Validação simples dos dados do cartão
    def _validar_campos_cartao(self):
        nome = self.campo_nome.get().strip()
        numero = self.campo_numero.get().replace(" ", "")
        validade = self.campo_validade.get().strip()
        cvv = self.campo_cvv.get().strip()

        if not nome:
            return False, "Preencha o nome do titular."
        if len(numero) < 12 or not numero.isdigit():
            return False, "Número do cartão inválido."
        if len(validade) != 5 or "/" not in validade:
            return False, "Validade deve ser no formato MM/AA."
        if not cvv.isdigit() or not (3 <= len(cvv) <= 4):
            return False, "CVV inválido."
        return True, ""

    def confirmar_pagamento(self):
        ok, msg = self._validar_campos_cartao()
        if not ok:
            self.status_label.configure(text=msg, text_color="#FF6B6B")
            return

        # Simula processar o pagamento (aqui só limpamos os dados)
        items = getattr(self.master, "checkout_items", None) or getattr(self.master, "cart", [])
        if not items:
            self.status_label.configure(text="Nenhum item para pagar.", text_color="#FF6B6B")
            return

        # Calcula total (apenas para exibir)
        total = sum(self._parse_price(p.get("preco") if isinstance(p, dict) else 0) for p in items)

        # Limpa carrinho e checkout no master
        try:
            self.master.cart = []
        except:
            self.master.cart = []
        try:
            self.master.checkout_items = []
        except:
            self.master.checkout_items = []

        # Atualiza tela do carrinho se disponível
        if self.master.telas.get("TelaCarrinho"):
            try:
                self.master.telas["TelaCarrinho"].refresh()
            except:
                pass

        # Mensagem de sucesso e redirecionamento para o menu
        self.status_label.configure(text=f"Pagamento de {self._format_brl(total)} confirmado. Obrigado!", text_color="#7CFC00")
        # Navega para o menu principal
        self.master.mostrar_tela("TelaMenu")