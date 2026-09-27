import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ==========================================
# 1. CONFIGURAÇÕES DA SPRINT
# ==========================================
DATA_INICIO = '2026-09-06'
DATA_FIM = '2026-09-27'

# ==========================================
# 2. MAPEAMENTO MANUAL (SUA BASE DE DADOS)
# ==========================================
tarefas = {
    # US000 - Technical Tasks
    "US000-1":  {"pontos": 6, "data_conclusao": '2026-09-14'},
    "US000-2":  {"pontos": 4, "data_conclusao": '2026-09-09'},
    "US000-3":  {"pontos": 3, "data_conclusao": '2026-09-09'},
    "US000-4":  {"pontos": 3, "data_conclusao": '2026-09-09'},
    "US000-5":  {"pontos": 5, "data_conclusao": '2026-09-14'},
    "US000-6":  {"pontos": 8, "data_conclusao": None},
    "US000-7":  {"pontos": 6, "data_conclusao": None},
    "US000-8":  {"pontos": 6, "data_conclusao": '2026-09-09'},
    "US000-9":  {"pontos": 8, "data_conclusao": '2026-09-14'},
    "US000-10": {"pontos": 6, "data_conclusao": '2026-09-27'},

    # US001 - Como clínica/OCS...
    "US001-1":  {"pontos": 6,  "data_conclusao": '2026-09-21'},
    "US001-2":  {"pontos": 6,  "data_conclusao": '2026-09-18'},
    "US001-3":  {"pontos": 6,  "data_conclusao": '2026-09-23'},
    "US001-4":  {"pontos": 8,  "data_conclusao": '2026-09-24'},
    "US001-5":  {"pontos": 8,  "data_conclusao": '2026-09-24'},
    "US001-6":  {"pontos": 8,  "data_conclusao": '2026-09-25'},
    "US001-7":  {"pontos": 6,  "data_conclusao": '2026-09-25'},
    "US001-8":  {"pontos": 10, "data_conclusao": '2026-09-26'},
    "US001-9":  {"pontos": 8,  "data_conclusao": '2026-09-26'},

    # US002 - Como auditor...
    "US002-1":  {"pontos": 8, "data_conclusao": None},
    "US002-2":  {"pontos": 6, "data_conclusao": None},
    "US002-3":  {"pontos": 6, "data_conclusao": None},
    "US002-4":  {"pontos": 6, "data_conclusao": None}
}

# ==========================================
# 3. PROCESSAMENTO DOS DADOS
# ==========================================
total_pontos = sum(t["pontos"] for t in tarefas.values())

data_inicial = datetime.strptime(DATA_INICIO, '%Y-%m-%d').date()
data_final = datetime.strptime(DATA_FIM, '%Y-%m-%d').date()
dias_sprint = (data_final - data_inicial).days + 1

datas_eixo_x = [data_inicial + timedelta(days=i) for i in range(dias_sprint)]

taxa_ideal = total_pontos / (dias_sprint - 1)
pontos_ideal = [total_pontos - (i * taxa_ideal) for i in range(dias_sprint)]

pontos_real = []
pontos_restantes = total_pontos

conclusoes_validas = {}
for us, info in tarefas.items():
    if info["data_conclusao"] and info["data_conclusao"] != 'AAAA-MM-DD':
        conclusoes_validas[us] = datetime.strptime(info["data_conclusao"], '%Y-%m-%d').date()

for data_atual in datas_eixo_x:
    pontos_entregues_no_dia = sum(
        tarefas[us]["pontos"] for us, data_conc in conclusoes_validas.items() if data_conc == data_atual
    )
    pontos_restantes -= pontos_entregues_no_dia
    pontos_real.append(pontos_restantes)

# ==========================================
# 4. PLOTAGEM DO GRÁFICO (EQUILÍBRIO VISUAL)
# ==========================================
fig, ax = plt.subplots(figsize=(11, 6))

datas_formatadas = [d.strftime('%d/%m') for d in datas_eixo_x]

cor_ideal = '#8C8C8C'
cor_real = '#1A73E8'
cor_semana = '#FB8C00'
cor_eixos = '#5A5A5A'    # Tom equilibrado: nem muito claro, nem muito escuro/pesado

# Linhas principais
ax.plot(datas_formatadas, pontos_ideal, linestyle='--', color=cor_ideal, label='Ritmo Ideal', marker='o', markersize=4, linewidth=1.5)
ax.plot(datas_formatadas, pontos_real, color=cor_real, label='Realizado', marker='o', markersize=6, linewidth=2.5)

# Adicionando marcadores semanais (a cada 7 dias)
legend_added = False
for i in range(7, dias_sprint, 7):
    if i < len(datas_formatadas):
        ax.axvline(x=i, color=cor_semana, linestyle=':', linewidth=1.8, alpha=0.85,
                   label='Fim de Semana (Ciclo)' if not legend_added else "")
        legend_added = True

# Rótulos limpos e posicionados acima da linha
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

# Estilização das bordas com o novo tom equilibrado
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#A0A0A0')
ax.spines['bottom'].set_color('#A0A0A0')

# Títulos e eixos
ax.set_title('DataSphere - Burndown Chart (Sprint 1)', fontsize=14, fontweight='bold', color='#202124', pad=20)
ax.set_ylabel('Story Points Restantes', fontsize=10, color=cor_eixos, labelpad=10)
ax.set_xlabel('Dias da Sprint', fontsize=10, color=cor_eixos, labelpad=10)

# Margem superior estendida
ax.set_ylim(-2, total_pontos + 15)

# Eixos e grades
plt.xticks(rotation=45, ha='right', fontsize=9, color=cor_eixos)
plt.yticks(fontsize=9, color=cor_eixos)
ax.yaxis.grid(True, linestyle='-', alpha=0.3, color='#CCCCCC')
ax.xaxis.grid(False)

# Legenda
ax.legend(frameon=True, facecolor='white', edgecolor='#A0A0A0', fontsize=9, loc='upper right')

plt.tight_layout()
plt.show()