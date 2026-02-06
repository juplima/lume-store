import customtkinter as ctk
from collections import Counter

class TelaRelatorios(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#1A1A2E")

        # Título
        ctk.CTkLabel(self, text="Relatórios", font=("Arial", 28, "bold"), text_color="#FFD700").pack(pady=(20,10))

        # Frame principal de conteúdo
        corpo = ctk.CTkFrame(self, fg_color="#162447", corner_radius=8)
        corpo.pack(fill="both", expand=True, padx=20, pady=(0,10))

        # Estatísticas rápidas (cards)
        stats_frame = ctk.CTkFrame(corpo, fg_color="#162447")
        stats_frame.pack(fill="x", padx=12, pady=12)

        self.label_total_vendas = ctk.CTkLabel(stats_frame, text="Total de vendas: 0", font=("Arial", 14, "bold"), text_color="#FFFFFF")
        self.label_total_vendas.pack(anchor="w", pady=4)

        self.label_total_receita = ctk.CTkLabel(stats_frame, text="Receita total: R$0,00", font=("Arial", 14, "bold"), text_color="#FFFFFF")
        self.label_total_receita.pack(anchor="w", pady=4)

        self.label_media_pedido = ctk.CTkLabel(stats_frame, text="Ticket médio: R$0,00", font=("Arial", 14, "bold"), text_color="#FFFFFF")
        self.label_media_pedido.pack(anchor="w", pady=4)

        # Lista dos produtos mais vendidos (scroll)
        ctk.CTkLabel(corpo, text="Produtos mais vendidos", font=("Arial", 16, "bold"), text_color="#FFD700").pack(anchor="w", padx=12)
        self.top_frame = ctk.CTkScrollableFrame(corpo, fg_color="#1F4068", height=180)
        self.top_frame.pack(fill="both", padx=12, pady=(8,12))

        # Botões de ação
        botoes = ctk.CTkFrame(self, fg_color="#162447")
        botoes.pack(fill="x", padx=20, pady=(0,20))

        ctk.CTkButton(
            botoes,
            text="Atualizar",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            width=140,
            command=self.refresh
        ).pack(side="left", padx=10, pady=10)

        ctk.CTkButton(
            botoes,
            text="Simular Venda",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            width=140,
            command=self.simular_venda
        ).pack(side="left", padx=10, pady=10)

        ctk.CTkButton(
            botoes,
            text="Voltar ao Menu",
            fg_color="#FFD700",
            hover_color="#FFC300",
            text_color="#1A1A2E",
            width=140,
            command=lambda: master.mostrar_tela("TelaMenu")
        ).pack(side="right", padx=10, pady=10)

        # Inicializa
        self.refresh()

    # utilitários de preço (compatível com outros módulos)
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

    # Recalcula e exibe as estatísticas
    def refresh(self):
        # recarrega orders do master (espera-se lista de pedidos, cada pedido = lista/dict com produtos)
        orders = getattr(self.master, "orders", None)

        # fallback: se não existe, usa dados de exemplo (vendas isoladas)
        if not orders:
            orders = [
                [{"nome": "Minecraft", "preco": "R$150,00"}],
                [{"nome": "Stardew Valley", "preco": "R$80,00"}],
                [{"nome": "Minecraft", "preco": "R$150,00"}],
                [{"nome": "One Shot", "preco": "R$120,00"}]
            ]

        # normaliza orders para lista de listas de produtos
        normalized = []
        for o in orders:
            if isinstance(o, dict):
                # se for um pedido único em formato dict
                normalized.append([o])
            elif isinstance(o, list):
                normalized.append(o)
            else:
                # ignorar formatos estranhos
                continue

        num_vendas = len(normalized)
        receita = 0.0
        produtos_flat = []

        for pedido in normalized:
            for item in pedido:
                # item pode ser dict ou string
                if isinstance(item, dict):
                    nome = item.get("nome", "Produto")
                    preco = item.get("preco", 0)
                else:
                    nome = str(item)
                    preco = 0
                produtos_flat.append(nome)
                receita += self._parse_price(preco)

        ticket_medio = (receita / num_vendas) if num_vendas else 0.0

        # Atualiza labels
        self.label_total_vendas.configure(text=f"Total de vendas: {num_vendas}")
        self.label_total_receita.configure(text=f"Receita total: {self._format_brl(receita)}")
        self.label_media_pedido.configure(text=f"Ticket médio: {self._format_brl(ticket_medio)}")

        # Mostra top vendidos
        for w in self.top_frame.winfo_children():
            w.destroy()

        counter = Counter(produtos_flat)
        most_common = counter.most_common(10)
        if not most_common:
            ctk.CTkLabel(self.top_frame, text="Nenhuma venda registrada.", text_color="#FFFFFF").pack(pady=12)
        else:
            for nome, qtd in most_common:
                linha = ctk.CTkFrame(self.top_frame, fg_color="#1F4068")
                linha.pack(fill="x", padx=8, pady=6)
                ctk.CTkLabel(linha, text=f"{nome}", text_color="#FFD700", font=("Arial", 13, "bold")).pack(side="left", padx=8, pady=6)
                ctk.CTkLabel(linha, text=f"Vendidos: {qtd}", text_color="#FFFFFF", font=("Arial", 12)).pack(side="right", padx=8, pady=6)

    # Botão de teste para adicionar uma venda ao master.orders
    def simular_venda(self):
        # cria um pedido exemplo
        pedido_ex = [{"nome": "Minecraft", "preco": "R$150,00"}, {"nome": "Teclado Mecânico", "preco": "R$350,00"}]
        if not hasattr(self.master, "orders"):
            self.master.orders = []
        self.master.orders.append(pedido_ex)
        # atualizar visual
        self.refresh()