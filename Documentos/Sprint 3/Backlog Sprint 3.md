<p align="center">
  <img src="../assets/logo_datasphere.png" width="200"/>
  <h2 align="center"> Datasphere </h2>
</p>

#### **Meta da Sprint:** 18 pontos (US006 - US009)

Conectar a solicitação e a emissão das guias ao acompanhamento do processo, reaproveitando os dados cadastrados e preservando a rastreabilidade entre as etapas.

<div align="center">
  <table>
    <tr>
      <th> Id </th>
      <th>User Stories</th>
      <th>Prioridade</th>
      <th>Estimativa</th>
      <th>Sprint</th>
    </tr>
    <tr>
      <td align="center"> <b> US006 </b> </td>
      <td> Como emissor de guia, quero gerar a Guia de Encaminhamento FUSEX no SIRE com os dados coletados no app, para evitar preenchimento manual duplicado. </td>
      <td align="center"> MÉDIA </td>
      <td align="center"> 3 </td>
      <td align="center"> 3 </td>
    </tr>
    <tr>
      <td align="center"> <b> US007 </b> </td>
      <td> Como auditor, quero visualizar o histórico completo de cada guia (solicitação, emissão, atendimento, fatura, aprovação), para garantir rastreabilidade do processo. </td>
      <td align="center"> MÉDIA </td>
      <td align="center"> 8 </td>
      <td align="center"> 3 </td>
    </tr>
    <tr>
      <td align="center"> <b> US008 </b> </td>
      <td> Como emissor de guia, quero registrar a solicitação de exame gerando uma Pré Guia, para que o processo de encaminhamento já comece padronizado. </td>
      <td align="center"> BAIXA </td>
      <td align="center"> 2 </td>
      <td align="center"> 3 </td>
    </tr>
    <tr>
      <td align="center"> <b> US009 </b> </td>
      <td> Como beneficiário, quero acessar um painel com o status de cada guia (solicitada, emitida, realizada, faturada, aprovada, liquidada), para acompanhar o andamento sem precisar consultar múltiplas fontes. </td>
      <td align="center"> BAIXA </td>
      <td align="center"> 5 </td>
      <td align="center"> 3 </td>
    </tr>
  </table>
</div>

#### ✅ Definition of Ready (DoR) — US006 <a id="dor-us006"></a>

- A dependência de uma aprovação pelo médico responsável ou pelo chefe do FUSEx, prevista no fluxo atual da US005, está identificada como condição para emissão.
- Os campos do pacote destinado ao SIRE estão definidos, incluindo beneficiário (PrecCP), médico, aprovações, procedimentos, OCS, quantidades e valores contratuais.
- Está delimitado o uso do pacote de dados já disponível no projeto e como ele será utilizado no SIRE, distinguindo a preparação das informações de uma transmissão automática ao sistema externo.
- As regras de numeração, vínculo com a Pré Guia, validade de 60 dias e impedimento de emissão duplicada estão especificadas.
- O fluxo da tela de emissão está definido, incluindo conferência dos dados, confirmação da operação e acesso ao documento gerado.
- Os cenários de Pré Guia sem aprovação ou já emitida estão previstos para validação da história.

#### ✅ Definition of Ready (DoR) — US007 <a id="dor-us007"></a>

- Estão mapeados os vínculos necessários para reunir os registros da Pré Guia, da guia, dos atendimentos, do espelho e da fatura em uma mesma consulta.
- Os dados de cada evento estão definidos a partir do histórico existente: entidade, data e hora, status anterior, novo status e origem da alteração.
- A ordenação cronológica e a preservação das alterações anteriores estão especificadas para manter a rastreabilidade da solicitação à aprovação da fatura.
- As permissões do auditor e a apresentação de etapas ainda sem registro estão definidas.
- O protótipo da consulta permite distinguir a aprovação da Pré Guia da aprovação financeira, sem confundir eventos de entidades diferentes.

#### ✅ Definition of Ready (DoR) — US008 <a id="dor-us008"></a>

- Os cadastros necessários estão identificados: beneficiário, médico responsável, procedimentos, OCS e contratos correspondentes.
- O formulário está especificado com seleção do beneficiário e do médico, pelo menos um procedimento e quantidade maior que zero por item.
- Está definida a consulta aos contratos para associar cada procedimento à OCS e apresentar seus valores, evitando preenchimento livre de preços.
- O fluxo diferencia salvar como rascunho (PRE_GUIA) de validar e encaminhar para aprovação (VALIDADA), incluindo a situação COM_PENDENCIAS para correção.
- As permissões de criação pelo emissor e as regras de edição de rascunhos, solicitações com pendências ou reprovadas estão estabelecidas.
- O vínculo da solicitação com as aprovações da US005 e com a emissão da US006 está documentado, preservando o identificador da Pré Guia.

#### ✅ Definition of Ready (DoR) — US009 <a id="dor-us009"></a>

- Está definido o mapeamento das etapas solicitada, emitida, realizada, faturada, aprovada e liquidada para os registros da Pré Guia, da guia, dos procedimentos e do processo financeiro.
- As fontes de cada etapa estão identificadas; a liquidação depende de confirmação financeira e não pode ser deduzida apenas da emissão ou da aprovação da Pré Guia.
- As informações do painel estão especificadas com identificação da guia, procedimentos, situação do atendimento, data de emissão e validade de 60 dias, quando aplicáveis.
- O acesso está vinculado ao beneficiário autenticado, com cenários de consulta sem guias e tentativa de acesso a registros de outra pessoa.
- O protótipo prevê procedimentos parcialmente realizados, guias expiradas e atualização na próxima consulta, aproveitando a estrutura da tela Minhas Guias.

#### Observações da revisão

- O DoR descreve as condições necessárias para iniciar cada história; os itens acima devem ser conferidos pela equipe e não representam uma declaração de implementação concluída.
- A US006 possui preparação de pacote para o SIRE e emissão local no código consultado; o envio automático ao sistema externo não foi identificado.
- Na US007, a linha do tempo integrada reúne os eventos das entidades vinculadas à guia e identifica o responsável pela ação quando disponível.
- Na US009, o painel utiliza os registros da solicitação, dos procedimentos e das faturas para apresentar as etapas, incluindo aprovação e liquidação financeira.
