<p align="center">
  <img src="../assets/logo_datasphere.png" width="200"/>
  <h2 align="center"> Datasphere </h2>
</p>

---

### 🧾 User Story 6 — Geração da Guia de Encaminhamento no SIRE

> **Como** emissor de guia,  
> **Quero** gerar a Guia de Encaminhamento FUSEX no SIRE com os dados coletados no app,  
> **Para** evitar preenchimento manual duplicado.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que a Pré Guia recebeu a aprovação do médico responsável ou do chefe do FUSEx, **quando** o emissor consultá-la, **então** a emissão deve estar disponível. |
| **02** | **Quando** o pacote destinado ao SIRE for consultado, **então** ele deve reunir os dados já cadastrados do beneficiário, médico, aprovações, procedimentos, OCS, quantidades e valores, sem exigir sua redigitação para montar o pacote. |
| **03** | **Dado** que a Pré Guia ainda não foi aprovada, **quando** houver tentativa de emissão ou consulta do pacote SIRE, **então** o sistema deve bloquear a operação e informar o motivo. |
| **04** | **Quando** a emissão local for concluída, **então** a guia deve possuir identificação própria, vínculo com a Pré Guia e validade de 60 dias a partir da emissão. |
| **05** | **Após** a emissão, **então** a Pré Guia deve apresentar o status *EMITIDA*, e o documento da guia deve estar disponível para consulta. |
| **06** | **Dado** que a Pré Guia já originou uma guia, **quando** houver nova tentativa de emissão, **então** o sistema deve impedir a duplicação e informar que a guia já foi emitida. |

O código consultado prepara o pacote SIRE e emite a guia localmente. Estes cenários validam esse fluxo; a geração efetiva no sistema externo ainda precisa ser demonstrada para concluir integralmente a US006.

---

### 🔎 User Story 7 — Histórico Completo da Guia

> **Como** auditor,  
> **Quero** visualizar o histórico completo de cada guia,  
> **Para** garantir a rastreabilidade do processo.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que existem guias cadastradas, **quando** o auditor realizar uma consulta, **então** o sistema deve permitir selecionar uma guia para análise. |
| **02** | **Quando** o histórico da guia for acessado, **então** o sistema deve apresentar os eventos de solicitação, emissão, atendimento, faturamento e aprovação, quando disponíveis. |
| **03** | Cada evento do histórico deve apresentar a entidade relacionada, data e hora, status anterior, novo status, origem da alteração e responsável pela ação quando disponível, conforme os dados registrados pelo sistema. |
| **04** | **Quando** houver alteração de status da guia, **então** o sistema deve registrar essa alteração no histórico sem apagar os eventos anteriores. |
| **05** | **Dado** que uma etapa não possui evento registrado, **então** a consulta deve indicar a ausência do registro, sem atribuir data ou conclusão à etapa. |
| **06** | **Quando** o auditor consultar novamente uma guia, **então** o histórico deve permanecer organizado em ordem cronológica e apresentar os dados atualizados. |

---

### 📝 User Story 8 — Registro da Solicitação e Geração da Pré Guia

> **Como** emissor de guia,  
> **Quero** registrar a solicitação de exame gerando uma Pré Guia,  
> **Para** que o processo de encaminhamento já comece padronizado.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Quando** o emissor iniciar uma solicitação, **então** o formulário deve permitir selecionar o beneficiário, o médico responsável e pelo menos um procedimento associado à OCS e ao contrato correspondente. |
| **02** | **Dado** que os campos obrigatórios foram preenchidos, **quando** o emissor confirmar o registro, **então** o sistema deve gerar uma Pré Guia com identificador próprio. |
| **03** | **Quando** a Pré Guia for criada, **então** ela deve ficar associada ao beneficiário e à solicitação de exame correspondente. |
| **04** | **Quando** o emissor salvar sem enviar para aprovação, **então** a Pré Guia deve permanecer como rascunho (*PRE_GUIA*), disponível para consulta e edição. |
| **05** | **Dado** que faltem beneficiário, médico ou procedimentos, ou que uma quantidade seja menor ou igual a zero, **quando** o emissor tentar salvar, **então** o formulário deve apontar os campos inválidos e impedir o registro. |
| **06** | **Quando** o emissor enviar a Pré Guia para aprovação, **então** a validação deve encaminhá-la como *VALIDADA* se não houver pendências, ou apresentá-la como *COM_PENDENCIAS* com os motivos para correção. |
| **07** | **Quando** um procedimento contratado e sua quantidade forem selecionados, **então** o formulário deve apresentar o valor correspondente e atualizar o total da solicitação. |

---

### 📊 User Story 9 — Painel de Status das Guias

> **Como** beneficiário,  
> **Quero** acessar um painel com o status de cada guia,  
> **Para** acompanhar o andamento sem precisar consultar múltiplas fontes.

| # | Critério de Aceite |
| :-: | :--- |
| **01** | **Dado** que o beneficiário possui guias cadastradas, **quando** acessar o painel, **então** o sistema deve listar somente as guias vinculadas ao seu cadastro. |
| **02** | **Quando** uma guia emitida for exibida, **então** o painel deve apresentar sua identificação, os procedimentos, a data de emissão e o prazo restante de validade. |
| **03** | As etapas *Solicitada*, *Emitida*, *Realizada*, *Faturada*, *Aprovada* e *Liquidada* devem corresponder aos registros da solicitação, do atendimento e do processo financeiro; a aprovação da Pré Guia não deve ser apresentada como aprovação do pagamento. |
| **04** | **Quando** o status de uma guia for atualizado no sistema, **então** o painel deve apresentar a nova situação na próxima consulta do beneficiário. |
| **05** | **Dado** que o beneficiário não possua guias cadastradas, **então** o sistema deve informar que não existem guias para acompanhamento. |
| **06** | **Quando** o beneficiário tentar acessar dados de uma guia que não está vinculada ao seu cadastro, **então** o sistema deve impedir a visualização dessas informações. |
| **07** | **Dado** que apenas parte dos procedimentos ou sessões foi realizada, **quando** o beneficiário consultar a guia, **então** o painel deve indicar a realização parcial e apresentar o progresso dos procedimentos. |
| **08** | **Dado** que a guia esteja expirada, **quando** for exibida, **então** o painel deve identificar essa situação sem apresentá-la como disponível para novos atendimentos. |

As etapas financeiras do painel devem refletir os registros das faturas vinculadas aos procedimentos. A indicação de liquidação representa o registro dessa etapa no sistema.
