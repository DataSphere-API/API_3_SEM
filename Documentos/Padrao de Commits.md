<p align="center">
  <img src="../logo_datasphere.png" width="200"/>
  <h2 align="center"> Padrão de Commits </h2>
</p>

Este padrão segue o critério **G.3 — Padrão de Mensagem dos Commits** do Guia de Avaliação API: toda mensagem deve conter *tipo de alteração*, *tarefa* e *breve descrição*. Aplicado em 100% dos commits, garante nível 4 (nota máxima) no critério.

#### 📌 Formato

```
<tipo>(<tarefa>): <descrição breve, no imperativo>
```

- **tipo** — categoria da alteração (lista abaixo)
- **tarefa** — código da task/US no board (número da issue do GitHub, ex: `#12`)
- **descrição** — o que foi feito, curto, no imperativo, minúsculo, sem ponto final

#### ✅ Tipos permitidos <a id="tipos"></a>

<div align="center">
  <table>
    <tr>
      <th> Tipo </th>
      <th> Quando usar </th>
    </tr>
    <tr>
      <td align="center"> <b> feat </b> </td>
      <td> nova funcionalidade </td>
    </tr>
    <tr>
      <td align="center"> <b> fix </b> </td>
      <td> correção de bug </td>
    </tr>
    <tr>
      <td align="center"> <b> docs </b> </td>
      <td> alteração em documentação (README, manuais, etc.) </td>
    </tr>
    <tr>
      <td align="center"> <b> style </b> </td>
      <td> formatação, indentação, sem mudança de lógica </td>
    </tr>
    <tr>
      <td align="center"> <b> refactor </b> </td>
      <td> refatoração sem mudar comportamento </td>
    </tr>
    <tr>
      <td align="center"> <b> test </b> </td>
      <td> criação/ajuste de testes </td>
    </tr>
    <tr>
      <td align="center"> <b> chore </b> </td>
      <td> tarefas de manutenção (configs, dependências, build) </td>
    </tr>
    <tr>
      <td align="center"> <b> perf </b> </td>
      <td> melhoria de performance </td>
    </tr>
    <tr>
      <td align="center"> <b> db </b> </td>
      <td> alteração em schema/migração de banco de dados </td>
    </tr>
  </table>
</div>

#### 📝 Exemplos

```
feat(FUSEX-12): implementa cadastro de guia de encaminhamento
fix(FUSEX-15): corrige cálculo de valor conferido na Lisura
docs(FUSEX-3): atualiza manual de instalação com passos do banco
db(FUSEX-8): cria tabela de faturas e relacionamento com guias
chore(FUSEX-1): configura estrutura inicial do projeto Java Web
test(FUSEX-20): adiciona testes unitários para o serviço de aprovação
```

#### 📋 Regras da equipe <a id="regras"></a>

1. Sempre referenciar a tarefa do board — sem commit "solto" sem tarefa vinculada.
2. Um commit = uma mudança lógica. Evitar commits gigantes que misturam feat + fix + docs.
3. Mensagens em português, no imperativo ("cria", "corrige", "remove") — não no gerúndio ou passado.
4. Squash de commits de "WIP" antes do Pull Request, se a estratégia de branch adotada exigir histórico limpo.