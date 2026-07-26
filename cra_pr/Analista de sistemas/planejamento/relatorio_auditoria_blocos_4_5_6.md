# Relatório de Auditoria Pedagógica — Blocos 4, 5 e 6

**Trilha:** Analista de Sistemas
**Data da auditoria:** 14/07/2026
**Escopo inicial:** Semana 1, Dias 3–6
**Escopo de propagação:** Semana 2, única semana posterior já produzida
**Preservação obrigatória:** Semana 1, Dias 1–2

## Método

A auditoria foi concluída em modo somente leitura antes das correções. Para cada questão relacionada aos Blocos 4, 5 e 6, foram verificados:

1. ensino anterior à cobrança;
2. suficiência da explicação;
3. dependência de informação externa;
4. diferença entre assunto apenas citado e assunto realmente explicado;
5. existência de uma única melhor resposta;
6. sincronização entre enunciado e gabarito;
7. explicação individual de A, B, C e D;
8. validade e suficiência da referência interna.

Cada item recebeu um status primário: `Coberta`, `Parcialmente coberta`, `Não coberta`, `Cobrada antes do momento correto`, `Inadequada para o bloco` ou `Ambígua`.

## Diagnóstico anterior às correções

### Semana 1 — 80 extras dos Dias 3–6

| Status inicial | Quantidade |
|---|---:|
| Cobertas | 37 |
| Parcialmente cobertas | 5 |
| Não cobertas | 17 |
| Cobradas antes do momento correto | 18 |
| Inadequadas para o bloco | 2 |
| Ambíguas | 1 |
| **Total** | **80** |

Também foram encontradas 59 referências que apontavam para título genérico, assunto futuro, lista superficial ou pseudo-seção inexistente. Apesar dos problemas de cobertura, os 80 gabaritos já estavam sincronizados com o cabeçalho e a análise A–D dos respectivos comentários.

A validação semântica posterior refinou a primeira triagem mecânica: as Extras 6.3 e 6.9 passaram de `Coberta` para `Não coberta`, a Extra 6.13 passou de `Parcialmente coberta` para `Não coberta` e a Extra 5.4 passou de `Coberta` para `Parcialmente coberta`. A tabela acima já apresenta a classificação inicial consolidada depois desse refinamento, ainda sobre a versão anterior às correções.

Os 200 itens principais dos Dias 3–6 pertencem aos Blocos 1–3. Neste recorte, eles foram conferidos quanto à preservação e à sincronização entre tabela, cabeçalho e análise; a aceitação semântica registrada neste relatório é específica para as questões dos Blocos 4–6.

### Semana 2 — única semana posterior existente

As 120 extras estavam cobertas, eram cobradas depois da teoria e possuíam comentários com referências para âncoras existentes. O problema era estrutural:

- 0 de 120 informavam junto ao enunciado Bloco, Matéria, Assunto, Nível e Referência;
- os 420 itens da semana não possuíam nível;
- os Dias 3–6 deslocavam os blocos recorrentes para números entre 7 e 10;
- os 20 comentários das extras do Dia 6 usavam justificativas genéricas e repetitivas;
- README e Plano Mestre declaravam a semana concluída, em conflito com o padrão vigente.

## Tabela resumida da auditoria

Na Semana 1, `Problemas encontrados` conta o status pedagógico primário diferente de `Coberta`; metadados ausentes são tratados separadamente. Na Semana 2, como a cobertura era integral, a coluna registra a falha estrutural presente em cada item.

| Semana | Dia | Bloco | Matéria | Questões verificadas | Problemas encontrados | Correções |
|---|---|---:|---|---:|---:|---:|
| 1 | 3 | 4 | Legislação CRA/CFA | 15 | 12 | 12 |
| 1 | 3 | 5 | Português aplicado | 5 | 5 | 5 |
| 1 | 3 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 1 | 4 | 4 | Administração Pública e RLM | 15 | 8 | 8 |
| 1 | 4 | 5 | Português/discursiva | 5 | 3 | 3 |
| 1 | 4 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 1 | 5 | 4 | Legislação CRA/CFA | 20 | 5 | 5 |
| 1 | 5 | 5 | Prática discursiva | 0 | 0 | 0 |
| 1 | 5 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 1 | 6 | 4 | Legislação CRA/CFA | 10 | 4 | 4 |
| 1 | 6 | 5 | Planejamento discursivo | 0 | 0 | 0 |
| 1 | 6 | 6 | Revisão ativa | 10 | 6 | 6 |
| 2 | 1 | 4 | Legislação CRA/CFA | 15 | 15 | 15 |
| 2 | 1 | 5 | Português | 5 | 5 | 5 |
| 2 | 1 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 2 | 2 | 4 | Administração Pública | 15 | 15 | 15 |
| 2 | 2 | 5 | Português | 5 | 5 | 5 |
| 2 | 2 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 2 | 3 | 4 | Legislação CRA/CFA | 15 | 15 | 15 |
| 2 | 3 | 5 | Português | 5 | 5 | 5 |
| 2 | 3 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 2 | 4 | 4 | Administração Pública e RLM | 15 | 15 | 15 |
| 2 | 4 | 5 | Português | 5 | 5 | 5 |
| 2 | 4 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 2 | 5 | 4 | Legislação CRA/CFA | 15 | 15 | 15 |
| 2 | 5 | 5 | Português | 5 | 5 | 5 |
| 2 | 5 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |
| 2 | 6 | 4 | Revisão mista programada | 10 | 10 | 10 |
| 2 | 6 | 5 | Português | 10 | 10 | 10 |
| 2 | 6 | 6 | Revisão ativa e caderno de erros | 0 | 0 | 0 |

Nos blocos com zero questões próprias, a estrutura e a entrega prática foram auditadas separadamente: todos encerram com recuperação, registro de erro ou plano de revisão, sem introduzir teoria nova.

## Correções aplicadas

### Semana 1

- foram criadas âncoras únicas para os Blocos 4, 5 e 6 dos Dias 3–6;
- o Dia 3 passou a ensinar o núcleo de Legislação e de Português antes das extras;
- Administração Pública e a estrutura do parágrafo argumentativo foram antecipadas em nível suficiente no Dia 4;
- referências a teoria dos Dias 4, 5 e 6 foram retiradas dos dias anteriores;
- normas ainda pendentes deixaram de servir como fundamento de cobrança;
- o Bloco 6 foi limitado a recuperação ativa, correção de erro e entrega prática;
- as 80 extras receberam Dia, Bloco, Matéria, Assunto, Nível e Referência junto ao enunciado;
- 21 questões tiveram enunciado ou alternativas alterados: 19 reformuladas para o conteúdo do bloco e 2 substituídas por itens substantivos;
- reformuladas: Extras 3.13; 4.3, 4.6, 4.10, 4.11, 4.14 e 4.15; 5.4 e 5.16–5.20; 6.3, 6.9 e 6.11–6.14;
- substituídas: Extras 3.10 e 3.11;
- nenhuma questão foi movida e nenhuma letra de gabarito precisou ser alterada;
- comentários e referências dos itens alterados foram sincronizados.

### Semana 2

- o eixo técnico dos Dias 3–6 foi agrupado nos Blocos 1–3 e os blocos recorrentes foram normalizados como 4–6;
- as 120 extras receberam metadados completos e nível na matriz diária 8/8/4;
- os comentários repetem o nível e mantêm a referência já validada;
- as divergências de cabeçalho nos comentários da Questão 1 do Dia 1 e da Questão 3 do Dia 2 foram corrigidas sem alterar os gabaritos técnicos;
- os comentários das 20 extras do Dia 6 foram individualizados;
- o Bloco 6 passou a registrar recuperação e entrega, sem capítulo teórico novo;
- o status da semana foi corrigido para `Em migração`, pois a modernização geral das 300 principais permanece separada desta auditoria dos Blocos 4–6.

## Conteúdos acrescentados ou reposicionados

- competência nacional e regional, jurisdição, registro, ética, pessoas físicas e jurídicas, garantias de apuração e controle de fonte;
- leitura de comando, emprego dos porquês, regência, conectores, concordância e tese em texto técnico;
- princípios administrativos, publicidade e impessoalidade, noções de ato, nexo e responsabilidade e motivação objetiva;
- estrutura de tese, razão, evidência e consequência, com parágrafo completo comentado;
- mapas de origem para revisão ativa e protocolo de fechamento do caderno de erros;
- mapas das faixas de extras associadas a cada bloco.

## Cobranças antecipadas eliminadas

As 18 ocorrências classificadas especificamente como `Cobrada antes do momento correto` estavam concentradas nos seguintes itens:

- Dia 3: Extras 3.2, 3.3, 3.5, 3.9, 3.12 e 3.17–3.20;
- Dia 4: Extras 4.3, 4.10, 4.14, 4.16, 4.18 e 4.19;
- Dia 5: Extras 5.16–5.18.

Após a correção, nenhum item dos Blocos 4–6 depende de dia futuro.

A validação cruzada também identificou cinco lacunas de suficiência que não pertenciam a esse grupo de cobranças antecipadas: Extra 6.3 e Extras 6.11–6.14. Elas foram reformuladas para cobrar, respectivamente, a base legal consolidada, localidade espacial, vazão e latência de pipeline, Round Robin e `page fault`, todos assuntos ensinados antes da revisão.

A leitura final das fontes oficiais gerou ainda três correções de precisão: a Extra 3.13 passou a cobrar independência técnica expressamente ensinada; a Extra 5.4 deixou de atribuir o rito processual à RN CFA nº 671/2025; e a Extra 6.9 deixou de depender de regulamento de registro pendente. Nas Extras 6.11–6.20, a referência do item e do comentário passou a apontar diretamente para a seção anterior que contém a resposta, enquanto o campo `Bloco` continua identificando a recuperação ativa do Bloco 6.

## Resultado final da cobertura

| Semana | Questões B4–B6 verificadas | Cobertas | Parciais | Não cobertas | Antecipadas | Inadequadas | Ambíguas |
|---|---:|---:|---:|---:|---:|---:|---:|
| Semana 1, Dias 3–6 | 80 | 80 | 0 | 0 | 0 | 0 | 0 |
| Semana 2, Dias 1–6 | 120 | 120 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **200** | **200** | **0** | **0** | **0** | **0** | **0** |

## Arquivos alterados

- `semana_01/semana_01_estudo.md`;
- `semana_01/semana_01_questoes.md`;
- `semana_02/semana_02_estudo.md`;
- `semana_02/semana_02_questoes.md`;
- `planejamento/padrao_semanal.md`;
- `planejamento/plano_mestre_cra_pr_2026.md`;
- `README.md`;
- este relatório.

## Limite do aceite

Este relatório aceita a correspondência pedagógica dos Blocos 4, 5 e 6 no escopo descrito. Ele não transforma automaticamente as semanas inteiras em `Concluídas`: os Dias 1–2 da Semana 1 foram preservados, os bancos principais pertencentes aos Blocos 1–3 não recebem aceite semântico por este relatório, e a migração geral das questões principais da Semana 2 para o novo padrão de níveis e comentários continua organizada em lotes próprios.
