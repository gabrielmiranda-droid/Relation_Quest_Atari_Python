"""Tela de fliperama do Relation Quest. Não exige instalações extras."""

import tkinter as tk
from motor import ler_entrada, verificar

# Paleta inspirada em monitores de fliperama antigos.
FUNDO = "#101019"
TELA = "#06140D"
OURO = "#F6C958"
VERDE = "#8AF6AD"
VERMELHO = "#FF738A"
TEXTO = "#E9F4E9"
APAGADO = "#90A596"
BORDA = "#346748"
FONTE = "Courier New"


class RelationQuest:
    def __init__(self, janela):
        self.janela = janela
        janela.title("RELATION QUEST — Atari Verifier 1984")
        janela.geometry("1000x710")
        janela.minsize(920, 680)
        janela.configure(bg=FUNDO)

        moldura = tk.Frame(janela, bg=OURO, padx=5, pady=5)
        moldura.pack(fill="both", expand=True, padx=16, pady=16)
        tela = tk.Frame(moldura, bg=TELA, padx=25, pady=18)
        tela.pack(fill="both", expand=True)

        topo = tk.Frame(tela, bg=TELA)
        topo.pack(fill="x")
        self.rotulo(topo, "1UP 008400", OURO, 12).pack(side="left")
        self.rotulo(topo, "★  GRUPO 08  ★", OURO, 12).pack(side="left", expand=True)
        self.rotulo(topo, "1984", OURO, 12).pack(side="right")

        self.rotulo(tela, "RELATION QUEST", OURO, 37, True).pack(pady=(13, 0))
        self.rotulo(tela, "★  A T A R I   V E R I F I E R  ★", VERDE, 12).pack(pady=(0, 12))
        tk.Frame(tela, bg=BORDA, height=2).pack(fill="x", pady=4)

        colunas = tk.Frame(tela, bg=TELA)
        colunas.pack(fill="both", expand=True, pady=(12, 0))
        colunas.grid_columnconfigure(0, weight=1, uniform="colunas")
        colunas.grid_columnconfigure(1, weight=1, uniform="colunas")
        colunas.grid_rowconfigure(0, weight=1)
        esquerda = tk.Frame(colunas, bg=TELA)
        esquerda.grid(row=0, column=0, sticky="nsew", padx=(0, 14))
        direita = tk.Frame(colunas, bg=TELA)
        direita.grid(row=0, column=1, sticky="nsew")

        self.rotulo(esquerda, "● INSERT DATA TO START ●", OURO, 12, True).pack(pady=(2, 22))
        self.rotulo(esquerda, "01 / CONJUNTO A", OURO, 12, True, "w").pack(fill="x")
        self.campo_a = tk.Entry(esquerda, font=(FONTE, 15), bg="#0C2415", fg=VERDE,
                                insertbackground=OURO, relief="flat", highlightthickness=1,
                                highlightbackground=BORDA, highlightcolor=OURO)
        self.campo_a.pack(fill="x", ipady=12, pady=(8, 5))
        self.rotulo(esquerda, "Exemplo: {1,2,3}", APAGADO, 10, alinhamento="w").pack(fill="x")

        self.rotulo(esquerda, "02 / RELAÇÃO R", OURO, 12, True, "w").pack(fill="x", pady=(25, 0))
        self.campo_r = tk.Text(esquerda, height=3, wrap="word", font=(FONTE, 13), bg="#0C2415",
                              fg=VERDE, insertbackground=OURO, relief="flat", padx=10, pady=10,
                              highlightthickness=1, highlightbackground=BORDA, highlightcolor=OURO)
        self.campo_r.pack(fill="x", pady=(8, 5))
        self.rotulo(esquerda, "Exemplo: {(1,1),(2,2),(1,2)}", APAGADO, 10, alinhamento="w").pack(fill="x")

        self.botao(esquerda, "▶  VERIFICAR RELAÇÃO", OURO, "#281B0B", self.analisar,
                   15).pack(fill="x", pady=(28, 12), ipady=11)

        exemplos = tk.Frame(esquerda, bg=TELA)
        exemplos.pack(fill="x")
        self.botao(exemplos, "DEMO 01", "#244F35", VERDE, self.demo_1, 10).pack(side="left", expand=True, fill="x", padx=(0, 6), ipady=8)
        self.botao(exemplos, "DEMO 02", "#244F35", VERDE, self.demo_2, 10).pack(side="left", expand=True, fill="x", padx=3, ipady=8)
        self.botao(exemplos, "LIMPAR", "#244F35", VERDE, self.limpar, 10).pack(side="left", expand=True, fill="x", padx=(6, 0), ipady=8)

        self.rotulo(direita, "◈ SYSTEM ANALYSIS ◈", OURO, 15, True).pack(pady=(0, 12))
        self.situacao = self.rotulo(direita, "AGUARDANDO COMANDO...", APAGADO, 11)
        self.situacao.pack(fill="x", pady=(2, 8))
        self.lista_resultados = tk.Frame(direita, bg=TELA)
        self.lista_resultados.pack(fill="both", expand=True)
        self.rotulo(direita, "4 PROPRIEDADES  •  1 MOTOR PYTHON", APAGADO, 10).pack(pady=5)

        tk.Frame(tela, bg=BORDA, height=2).pack(fill="x", pady=(10, 7))
        rodape = tk.Frame(tela, bg=TELA)
        rodape.pack(fill="x")
        self.rotulo(rodape, "PRESS VERIFY TO CONTINUE", VERDE, 10).pack(side="left")
        self.rotulo(rodape, "MATEMÁTICA DISCRETA", APAGADO, 10).pack(side="right")

        self.demo_1()

    def rotulo(self, pai, mensagem, cor, tamanho, negrito=False, alinhamento="center"):
        estilo = "bold" if negrito else "normal"
        return tk.Label(pai, text=mensagem, bg=TELA, fg=cor,
                        font=(FONTE, tamanho, estilo), anchor=alinhamento,
                        justify="left" if alinhamento == "w" else "center")

    def botao(self, pai, mensagem, fundo, cor, comando, tamanho):
        return tk.Button(pai, text=mensagem, command=comando, bg=fundo, fg=cor,
                         activebackground=OURO, activeforeground="#281B0B",
                         font=(FONTE, tamanho, "bold"), borderwidth=0,
                         cursor="hand2", relief="flat")

    def preencher(self, A, R):
        self.campo_a.delete(0, "end")
        self.campo_a.insert(0, A)
        self.campo_r.delete("1.0", "end")
        self.campo_r.insert("1.0", R)
        self.analisar()

    def demo_1(self):
        self.preencher("{1,2,3}", "{(1,1),(2,2),(3,3),(1,2),(2,1)}")

    def demo_2(self):
        self.preencher("{1,2,3}", "{(1,2),(2,3)}")

    def limpar(self):
        self.campo_a.delete(0, "end")
        self.campo_r.delete("1.0", "end")
        for item in self.lista_resultados.winfo_children():
            item.destroy()
        self.situacao.config(text="AGUARDANDO COMANDO...", fg=APAGADO)

    def analisar(self):
        for item in self.lista_resultados.winfo_children():
            item.destroy()
        try:
            A, R = ler_entrada(self.campo_a.get(), self.campo_r.get("1.0", "end"))
            resultados = verificar(A, R)
        except ValueError as erro:
            self.situacao.config(text="INPUT ERROR", fg=VERMELHO)
            tk.Label(self.lista_resultados, text=str(erro), bg=TELA, fg=VERMELHO,
                     font=(FONTE, 12), wraplength=410, justify="left").pack(anchor="w", pady=15)
            return

        self.situacao.config(text=f"SCAN COMPLETE  •  {len(A)} ELEMENTOS  •  {len(R)} PARES", fg=OURO)
        for propriedade, (valida, explicacao) in resultados.items():
            cartao = tk.Frame(self.lista_resultados, bg="#0B2216", padx=12, pady=10,
                              highlightbackground=BORDA, highlightthickness=1)
            cartao.pack(fill="x", pady=6)
            cabecalho = tk.Frame(cartao, bg="#0B2216")
            cabecalho.pack(fill="x")
            tk.Label(cabecalho, text=propriedade, bg="#0B2216", fg=TEXTO,
                     font=(FONTE, 12, "bold")).pack(side="left")
            tk.Label(cabecalho, text="✓ SIM" if valida else "✕ NÃO",
                     bg="#0B2216", fg=VERDE if valida else VERMELHO,
                     font=(FONTE, 12, "bold")).pack(side="right")
            tk.Label(cartao, text=explicacao, bg="#0B2216", fg=APAGADO,
                     font=(FONTE, 10), anchor="w", justify="left", wraplength=395).pack(fill="x", pady=(7, 0))


if __name__ == "__main__":
    janela = tk.Tk()
    RelationQuest(janela)
    janela.mainloop()
