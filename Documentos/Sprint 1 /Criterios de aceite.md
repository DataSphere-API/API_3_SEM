<div align="center">
  <img src="../logo_datasphere.png" width="180" alt="DataSphere Logo"/>
  <h2>Critérios de Aceite — Sprint 1</h2>
</div>

---

### 🩺 User Story 1 — Envio do Espelho de Fatura

> **Como** clínica/OCS,  
> **Quero** enviar digitalmente o espelho de fatura,  
> **Para** agilizar o recebimento das faturas pela seção FUSEX.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que um atendimento foi realizado, **então** a clínica/OCS deve conseguir registrar os insumos utilizados pelo beneficiário. |
| **02** | **Quando** um insumo for registrado, **então** ele deve ficar associado ao beneficiário e ao respectivo atendimento. |
| **03** | **Quando** as informações necessárias estiverem registradas, **então** o sistema deve permitir o envio dessas informações para a seção FUSEX. |
| **04** | **Dado** que o envio automático está configurado, **então** o sistema deve realizar o envio no intervalo previamente estabelecido. |
| **05** | **Após** um envio realizado com sucesso, **então** o sistema deve identificar as informações como enviadas. |
| **06** | **Quando** todas as informações necessárias forem enviadas, **então** a guia deve poder avançar para o estado *Faturada*. |

---

### 🔍 User Story 2 — Auditoria de Faturas

> **Como** auditor,  
> **Quero** comparar os valores apresentados na fatura com os valores do contrato,  
> **Para** identificar divergências antes da aprovação.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que existe uma fatura para auditoria, **quando** o auditor acessá-la, o sistema deve apresentar os valores registrados. |
| **02** | O sistema deve apresentar, para cada item da fatura, o valor correspondente previsto na tabela ou contrato cadastrado. |
| **03** | **Quando** os valores forem apresentados, **então** o sistema deve realizar a comparação entre o valor faturado e o valor previsto. |
| **04** | **Dado** que existe diferença entre os valores, **então** o sistema deve destacar o item como divergente. |
| **05** | O auditor deve conseguir alterar ou corrigir os dados da fatura antes do envio para aprovação. |
| **06** | **Após** concluir a análise, **quando** o auditor encaminhar a fatura, **então** o sistema deve permitir seu envio para aprovação. |