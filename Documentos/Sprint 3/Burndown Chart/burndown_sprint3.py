import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ==========================================
# 1. CONFIGURAÇÕES DA SPRINT
# ==========================================
DATA_INICIO = '2026-11-02'
DATA_FIM = '2026-11-23'

# ==========================================
# 2. MAPEAMENTO MANUAL (SUA BASE DE DADOS)
# ==========================================
DATA_ADICAO = '2026-11-17'  # dia em que os cards novos entraram na sprint

# Datas simuladas: 10 entregas na 1ª semana, 9 na 2ª e 10 + 12 adicionados na 3ª
tarefas = {
    # US000 - Technical Tasks
    "US000-16": {"pontos": 8, "data_conclusao": '2026-11-04'},
    "US000-17": {"pontos": 8, "data_conclusao": '2026-11-10'},
    "US000-18": {"pontos": 5, "data_conclusao": '2026-11-05'},
    "US000-19": {"pontos": 8, "data_conclusao": '2026-11-12'},
    "US000-20": {"pontos": 8, "data_conclusao": '2026-11-03'},

    # US001 - Espelho da OCS
    "US001-10": {"pontos": 8, "data_conclusao": '2026-11-06'},
    "US001-11": {"pontos": 6, "data_conclusao": '2026-11-11'},
    "US001-12": {"pontos": 5, "data_conclusao": '2026-11-17'},

    # US002 - Auditor e fatura
    "US002-7":  {"pontos": 8, "data_conclusao": '2026-11-12'},
    "US002-8":  {"pontos": 8, "data_conclusao": '2026-11-17'},
    "US002-9":  {"pontos": 6, "data_conclusao": '2026-11-19'},
    "US002-10": {"pontos": 4, "data_conclusao": '2026-11-03'},
    "US002-11": {"pontos": 8, "data_conclusao": '2026-11-20'},

    # US003 - QR Code e número da guia
    "US003-5":  {"pontos": 6, "data_conclusao": '2026-11-07'},
    "US003-6":  {"pontos": 5, "data_conclusao": '2026-11-06'},
    "US003-7":  {"pontos": 4, "data_conclusao": '2026-11-14'},

    # US004 - Baixa final por QR
    "US004-8":  {"pontos": 6, "data_conclusao": '2026-11-11'},
    "US004-9":  {"pontos": 8, "data_conclusao": '2026-11-18'},

    # US005 - Aprovação da pré-guia
    "US005-8":  {"pontos": 5, "data_conclusao": '2026-11-07'},
    "US005-9":  {"pontos": 5, "data_conclusao": '2026-11-13'},

    # US006 - Emissão, pacote SIRE e PDF
    "US006-6":  {"pontos": 6, "data_conclusao": '2026-11-05'},
    "US006-7":  {"pontos": 5, "data_conclusao": '2026-11-06'},

    # US007 - Histórico e linha do tempo
    "US007-1":  {"pontos": 8, "data_conclusao": '2026-11-14'},
    "US007-2":  {"pontos": 5, "data_conclusao": '2026-11-18'},
    "US007-3":  {"pontos": 5, "data_conclusao": '2026-11-20'},

    # US008 - Solicitação da pré-guia
    "US008-1":  {"pontos": 8, "data_conclusao": '2026-11-13'},
    "US008-2":  {"pontos": 5, "data_conclusao": '2026-11-19'},

    # US009 - Painel do beneficiário
    "US009-1":  {"pontos": 8, "data_conclusao": '2026-11-19'},
    "US009-2":  {"pontos": 5, "data_conclusao": '2026-11-20'},

    # Cards adicionados na última semana
    "US000-21": {"pontos": 2, "data_conclusao": '2026-11-17', "data_adicao": DATA_ADICAO},
    "US000-29": {"pontos": 2, "data_conclusao": '2026-11-18', "data_adicao": DATA_ADICAO},
    "US001-13": {"pontos": 8, "data_conclusao": '2026-11-19', "data_adicao": DATA_ADICAO},
    "US002-14": {"pontos": 6, "data_conclusao": '2026-11-19', "data_adicao": DATA_ADICAO},
    "US007-6":  {"pontos": 5, "data_conclusao": '2026-11-20', "data_adicao": DATA_ADICAO},
    "US005-11": {"pontos": 3, "data_conclusao": '2026-11-20', "data_adicao": DATA_ADICAO},
    "US000-30": {"pontos": 4, "data_conclusao": '2026-11-20', "data_adicao": DATA_ADICAO},
    "US000-31": {"pontos": 2, "data_conclusao": '2026-11-21', "data_adicao": DATA_ADICAO},
    "US005-12": {"pontos": 3, "data_conclusao": '2026-11-21', "data_adicao": DATA_ADICAO},
    "US006-10": {"pontos": 4, "data_conclusao": '2026-11-21', "data_adicao": DATA_ADICAO},
    "US007-7":  {"pontos": 3, "data_conclusao": '2026-11-22', "data_adicao": DATA_ADICAO},
    "US000-32": {"pontos": 4, "data_conclusao": '2026-11-23', "data_adicao": DATA_ADICAO}
}

# ==========================================
# 3. PROCESSAMENTO DOS DADOS
# ==========================================
def para_data(texto):
    return datetime.strptime(texto, '%Y-%m-%d').date()

data_inicial = para_data(DATA_INICIO)
data_final = para_data(DATA_FIM)
dias_sprint = (data_final - data_inicial).days + 1

datas_eixo_x = [data_inicial + timedelta(days=i) for i in range(dias_sprint)]

# Dia em que cada card entrou (sem data_adicao = início da sprint)
adicoes = {us: para_data(info.get("data_adicao", DATA_INICIO)) for us, info in tarefas.items()}

conclusoes_validas = {}
for us, info in tarefas.items():
    if info["data_conclusao"] and info["data_conclusao"] != 'AAAA-MM-DD':
        conclusoes_validas[us] = para_data(info["data_conclusao"])

total_pontos = sum(t["pontos"] for t in tarefas.values())
pontos_iniciais = sum(tarefas[us]["pontos"] for us, d in adicoes.items() if d == data_inicial)

pontos_ideal = []
pontos_real = []
pontos_restantes = 0
ideal_atual = 0
taxa_ideal = 0
for i, data_atual in enumerate(datas_eixo_x):
    adicionados_no_dia = sum(tarefas[us]["pontos"] for us, d in adicoes.items() if d == data_atual)
    entregues_no_dia = sum(tarefas[us]["pontos"] for us, d in conclusoes_validas.items() if d == data_atual)

    # Ritmo ideal: escopo novo entra no dia e é redistribuído até o fim da sprint
    if i == 0:
        ideal_atual = adicionados_no_dia
        taxa_ideal = ideal_atual / (dias_sprint - 1)
    else:
        ideal_atual -= taxa_ideal
        if adicionados_no_dia > 0:
            ideal_atual += adicionados_no_dia
            taxa_ideal = ideal_atual / (dias_sprint - 1 - i)
    pontos_ideal.append(ideal_atual)

    pontos_restantes += adicionados_no_dia - entregues_no_dia
    pontos_real.append(pontos_restantes)

# ==========================================
# 4. PLOTAGEM DO GRÁFICO (EQUILÍBRIO VISUAL)
# ==========================================
fig, ax = plt.subplots(figsize=(11, 6))

datas_formatadas = [d.strftime('%d/%m') for d in datas_eixo_x]

cor_ideal = '#8C8C8C'
cor_real = '#1A73E8'
cor_semana = '#FB8C00'
cor_eixos = '#5A5A5A'

# Linhas principais
ax.plot(datas_formatadas, pontos_ideal, linestyle='--', color=cor_ideal, label='Ritmo Ideal', marker='o', markersize=4, linewidth=1.5)
ax.plot(datas_formatadas, pontos_real, color=cor_real, label='Realizado', marker='o', markersize=6, linewidth=2.5)

# Marcadores semanais (a cada 7 dias)
legend_added = False
for i in range(7, dias_sprint, 7):
    if i < len(datas_formatadas):
        ax.axvline(x=i, color=cor_semana, linestyle=':', linewidth=1.8, alpha=0.85,
                   label='Fim de Semana (Ciclo)' if not legend_added else "")
        legend_added = True

# Rótulos posicionados acima da linha
for i, valor in enumerate(pontos_real):
    if i == 0 or pontos_real[i] != pontos_real[i-1] or i == len(pontos_real) - 1:
        ax.annotate(str(valor),
                    (datas_formatadas[i], pontos_real[i]),
                    textcoords="offset points",
                    xytext=(0, 10),
                    ha='center',
                    fontsize=8.5,
                    color=cor_real,
                    fontweight='bold')

# Bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#A0A0A0')
ax.spines['bottom'].set_color('#A0A0A0')

# Títulos e eixos
ax.set_title('DataSphere - Burndown Chart (Sprint 3)', fontsize=14, fontweight='bold', color='#202124', pad=20)
ax.set_ylabel('Story Points Restantes', fontsize=10, color=cor_eixos, labelpad=10)
ax.set_xlabel('Dias da Sprint', fontsize=10, color=cor_eixos, labelpad=10)

# Margem superior estendida
ax.set_ylim(-2, max(max(pontos_real), max(pontos_ideal)) + 15)

# Eixos e grades
plt.xticks(rotation=45, ha='right', fontsize=9, color=cor_eixos)
plt.yticks(fontsize=9, color=cor_eixos)
ax.yaxis.grid(True, linestyle='-', alpha=0.3, color='#CCCCCC')
ax.xaxis.grid(False)

# Legenda
ax.legend(frameon=True, facecolor='white', edgecolor='#A0A0A0', fontsize=9, loc='upper right')

plt.tight_layout()
plt.savefig('burndown_sprint3.png', dpi=150)
plt.show()
