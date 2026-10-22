 <p align="center">
  <img src="Documentos/assets/logo_datasphere.png" width="200"/>
  <h2 align="center"> Datasphere </h2>
</p>

---

### 📱 User Story 3 — Apresentação da Guia com QR Code

> **Como** beneficiário,  
> **Quero** apresentar a guia com QR Code na clínica,  
> **Para** que o atendimento seja validado de forma segura.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que o beneficiário possui uma guia emitida, **quando** acessar os dados da guia, **então** o sistema deve disponibilizar o QR Code correspondente. |
| **02** | **Dado** que o QR Code foi gerado, **então** ele deve estar associado à guia correta e permitir sua identificação. |
| **03** | **Quando** o beneficiário apresentar o QR Code na clínica, **então** ele deve estar disponível para leitura pelo responsável pelo atendimento. |
| **04** | **Dado** que a guia possui um QR Code válido, **quando** ele for lido, **então** o sistema deve permitir a consulta das informações necessárias para sua identificação. |
| **05** | **Quando** o beneficiário tentar apresentar uma guia sem QR Code disponível, **então** o sistema deve informar que não foi possível apresentar o código. |

---

### 🏥 User Story 4 — Validação da Guia por QR Code

> **Como** clínica/OCS,  
> **Quero** validar a guia por QR Code no momento do atendimento,  
> **Para** confirmar que o procedimento está autorizado.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que o beneficiário apresentou o QR Code, **quando** a clínica realizar a leitura, **então** o sistema deve consultar a guia correspondente. |
| **02** | **Quando** uma guia válida for identificada, **então** o sistema deve apresentar as informações necessárias para conferência do atendimento. |
| **03** | **Dado** que a guia está autorizada, **quando** a validação for realizada, **então** o sistema deve informar que o procedimento pode ser realizado. |
| **04** | **Dado** que a guia é inválida, inexistente ou não autorizada, **quando** a clínica tentar validá-la, **então** o sistema deve informar que o atendimento não pode ser confirmado. |
| **05** | **Quando** ocorrer uma tentativa de validação, **então** o sistema deve apresentar o resultado da consulta de forma clara para o responsável pelo atendimento. |

---

### 📋 User Story 5 — Aprovação da Pré-guia pelo FUSEx

> **Como** chefe do FUSEx,  
> **Quero** poder visualizar e aprovar a pré-guia,  
> **Para** que a guia definitiva seja emitida com mais rapidez.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que existem pré-guias pendentes, **quando** o chefe do FUSEx acessar o sistema, **então** ele deve conseguir visualizar as pré-guias disponíveis para análise. |
| **02** | **Quando** uma pré-guia for selecionada, **então** o sistema deve apresentar os dados do beneficiário, os procedimentos solicitados e as informações do atendimento. |
| **03** | **Dado** que a pré-guia foi analisada, **quando** o chefe do FUSEx aprová-la, **então** o sistema deve registrar a aprovação. |
| **04** | **Após** a aprovação da pré-guia, **então** o sistema deve permitir a emissão da guia definitiva conforme as regras de negócio estabelecidas. |
| **05** | **Dado** que uma pré-guia já foi aprovada, **quando** ela for consultada novamente, **então** o sistema deve apresentar seu status atualizado. |
| **06** | **Quando** o chefe do FUSEx não possuir permissão para aprovar uma pré-guia, **então** o sistema deve impedir a realização dessa ação. |