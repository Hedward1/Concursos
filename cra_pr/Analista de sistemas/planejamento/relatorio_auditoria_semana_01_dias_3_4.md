# Relatório de Auditoria Pedagógica — Semana 1, Dias 3 e 4

- **Trilha:** Analista de Sistemas
- **Data:** 14/07/2026
- **Versão auditada antes das correções:** `e9ba336`
- **Escopo de conteúdo:** Semana 1, Dia 3 — Banco de Dados e SQL; Dia 4 — Legislação CRA-PR/CFA
- **Escopo de padrão:** jornada do estudante, carga por sessão, rastreabilidade e níveis
- **Conteúdo congelado:** Dias 1–2 e corpo didático dos Dias 5–6; apenas o índice global de pendências e fontes foi sincronizado com a confirmação oficial do Dia 4

## Método

A auditoria das 100 questões principais foi concluída em modo somente leitura antes de qualquer reorganização. Para cada item, foram conferidos:

1. ensino anterior à cobrança;
2. suficiência de regra, funcionamento e exemplo;
3. eventual dependência de informação externa;
4. existência de uma única melhor resposta;
5. correspondência entre dificuldade real e nível declarado;
6. sincronização entre item, gabarito e comentário A–D;
7. existência e suficiência da referência interna.

Os status primários foram `Coberta`, `Parcialmente coberta`, `Não coberta`, `Cobrada antes de ser ensinada`, `Ambígua`, `Nível superestimado` e `Nível subestimado`.

## Diagnóstico anterior às correções

| Dia | Cobertas | Parciais | Não cobertas | Cobradas antes | Ambíguas | Nível superestimado | Nível subestimado | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dia 3 | 18 | 19 | 2 | 1 | 2 | 8 | 0 | 50 |
| Dia 4 | 14 | 7 | 11 | 0 | 0 | 18 | 0 | 50 |
| **Total** | **32** | **26** | **13** | **1** | **2** | **26** | **0** | **100** |

Esses números usam um status primário exclusivo por questão. A leitura complementar identificou problemas secundários de nível em itens parciais ou não cobertos; por isso, a correção final recalibrou 8 níveis no Dia 3 e 28 no Dia 4.

Também foram confirmados:

- 100/100 gabaritos sincronizados com o cabeçalho dos comentários;
- 100/100 níveis inicialmente sincronizados entre item e comentário;
- 50/50 referências principais do Dia 3 genéricas, sem âncora temática;
- referências do Dia 4 em texto simples e 18 títulos sem correspondência exata na teoria;
- Q2 e Q11 do Dia 3 com mais de uma leitura defensável;
- Q13–Q16, Q25, Q28 e Q36–Q38 do Dia 4 cobrando resoluções que a teoria declarava pendentes;
- Q45 do Dia 4 sem base oficial suficiente para a política de priorização descrita.

## Reorganização da apostila de estudo

Nos dois dias, a ordem física passou a ser:

1. objetivo e orientação;
2. cronograma por sessões;
3. Bloco 1 — teoria principal;
4. Bloco 2 — aprofundamento;
5. Bloco 3 — exemplos e prática guiada;
6. Bloco 4 — matéria fixa;
7. Bloco 5 — Português ou discursiva;
8. Bloco 6 — recuperação ativa, sem conteúdo novo;
9. mini revisão e fixação;
10. checklist;
11. roteiro das questões;
12. correção, caderno de erros e fechamento.

As antigas seções `Reforço de alinhamento com as questões` foram eliminadas. Seu conteúdo foi incorporado aos Blocos 1–3 antes da revisão, do checklist e da indicação de questões. Os Blocos 4, 5 e 6 foram preservados e deslocados para depois da teoria principal; o Bloco 6 continuou restrito à recuperação do que já havia sido estudado.

### Conteúdo integrado no Dia 3

- arquitetura em três níveis, catálogo e independência de dados;
- modelo relacional, chaves, participação e mapeamento MER–relacional;
- 1FN, 2FN, 3FN, dependências funcionais, decomposição sem perda e preservação de dependências;
- `SELECT`, `WHERE`, `DISTINCT`, `ORDER BY`, `FETCH FIRST`, `OFFSET`, agregações, `GROUP BY` e `HAVING`;
- `INNER JOIN`, `LEFT JOIN`, `NULL`, `IS NULL`, filtro no `ON` versus `WHERE` e contagens em junção externa;
- `INSERT`, `IDENTITY`, `DEFAULT`, omissão de coluna, `UPDATE`, `DELETE`, `TRUNCATE` e `DROP`;
- `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK` e ações referenciais;
- álgebra relacional, índices, views, procedures e triggers;
- ACID, níveis de isolamento, log, `undo`/`redo`, recuperação e backup consistente;
- segurança, menor privilégio e acesso por view;
- exemplos e pegadinhas suficientes antes das questões avançadas.

### Conteúdo integrado no Dia 4

- Lei nº 4.769/1965 e Decreto nº 61.934/1967;
- Regimento do CRA-PR aprovado pela RN CFA nº 651/2024;
- Código de Ética aprovado pela RN CFA nº 671/2025;
- CFA versus CRA, jurisdição, registro, fiscalização, pessoa física, pessoa jurídica e responsabilidade técnica;
- Plenário, Diretoria Executiva, sanções, gradação, abrangência funcional e independência técnica;
- Lei nº 12.514/2011, conselho profissional versus sindicato e hierarquia normativa;
- método de proveniência, vigência, relação entre norma-base e norma alteradora e limite de uso de fonte oficial;
- objeto, relação, exemplo e pegadinha das seis resoluções adicionais efetivamente cobradas.

## Resoluções oficiais confirmadas

| Norma | Conteúdo confirmado | Relação ensinada | Limite adotado |
|---|---|---|---|
| [RN CFA nº 649/2024](https://documentos.cfa.org.br/?a=show&c=documento&id=951) | aprova o Regulamento de Registro do Sistema CFA/CRAs | norma-base alterada pela RN nº 670/2025 | objeto e relação; nenhum requisito não ensinado decide item |
| [RN CFA nº 670/2025](https://documentos.cfa.org.br/?a=show&c=documento&id=1033) | altera o Regulamento aprovado pela RN nº 649/2024 | modifica o art. 11 da norma-base | alteração parcial não equivale a revogação total |
| [RN CFA nº 546/2018](https://documentos.cfa.org.br/?a=show&c=documento&id=700) | dispõe sobre isenção de débitos pelos CRAs | relaciona-se à Lei nº 12.514/2011 e revoga a RN nº 510/2017 | objeto e relação, sem criar hipótese nova |
| [RN CFA nº 626/2023](https://documentos.cfa.org.br/?a=show&c=documento&id=803) | institui o PERC | foi alterada pela RN nº 627/2023 e teve adesão temporal em 2023 | objeto histórico; não é apresentado como programa permanentemente aberto |
| [RN CFA nº 589/2020](https://documentos.cfa.org.br/?a=show&c=documento&id=745) | aprova o Regulamento de Fiscalização | revoga as RNs nº 446 e 449 | objeto e organização da fiscalização; sem inventar política de risco |
| [RN CFA nº 680/2025](https://documentos.cfa.org.br/?a=show&c=documento&id=1058) | aprova o Regulamento das Eleições | revoga a RN nº 633/2023 | objeto e relação, sem cobrança de prazo eleitoral não ensinado |

O detalhamento integral dessas normas não foi presumido. As questões usam apenas o núcleo oficial que passou a ser efetivamente explicado antes do banco.

## Questões corrigidas

### Reformuladas

- **Dia 3, Q2:** “total de anuidades” foi substituído por “quantidade de lançamentos de anuidade”, eliminando a disputa entre `COUNT(*)` e `SUM(valor)` e mantendo o gabarito A.
- **Dia 3, Q11:** o enunciado passou a pedir exclusivamente linhas cujo valor SQL seja `NULL`, eliminando a concorrência entre `COALESCE(email, '') = ''` e `email IS NULL` e mantendo o gabarito D.

### Substituída

- **Dia 4, Q45:** o item sobre priorização por risco social, não sustentado pela RN nº 589/2020, foi substituído por questão resolvível a partir da fonte oficial e da teoria anterior.

### Comentários corrigidos

- Dia 3, Q34 e Q49: a explicação de comandos negativos passou a distinguir “afirmação correta” de “alternativa que não é o gabarito”, sem polaridade contraditória;
- Dia 4, Q20, Q33 e Extra 4.12: os comentários de comandos negativos passaram a distinguir a veracidade da afirmação de sua condição de resposta;
- comentários de todas as 100 principais receberam a mesma referência precisa do respectivo item;
- nível, uso, referência, gabarito e comentário permaneceram sincronizados nos 140 itens dos dois dias.

Nenhuma questão foi removida ou movida para semana posterior. Nenhuma letra de gabarito precisou mudar.

## Níveis recalibrados

| Dia | Questões | Alteração | Distribuição após a auditoria inicial |
|---|---|---|---|
| Dia 3 | Q24, Q25, Q26, Q27 e Q40; Q41, Q46 e Q50 | cinco de Difícil para Médio; três de Muito difícil para Difícil | 25 Médias / 18 Difíceis / 7 Muito difíceis |
| Dia 4 | Q21–Q36, Q39–Q40 e Q41–Q50 | níveis ajustados conforme a cadeia real de raciocínio; Q37–Q38 permaneceram Difíceis | 42 Médias / 8 Difíceis / 0 Muito difíceis |

A distribuição planejada deixou de ser usada para inflar artificialmente questões de reconhecimento literal. A exceção pós-auditoria ficou registrada no padrão semanal e neste relatório. O banco do Dia 4 foi aprofundado posteriormente, conforme a seção de continuidade abaixo.

## Ajustes de continuidade após o veredito 8,5/10

O PR nº 5 permaneceu aceito e não foi desfeito. O ajuste posterior atacou apenas os dois limites identificados na revisão: excesso de sessões e ausência de dificuldade alta substantiva no Dia 4.

### Dificuldade real no Dia 4

A segunda auditoria confirmou cobertura, referência suficiente, resposta única e independência externa nas 50 principais, mas identificou repetição e reconhecimento literal em parte dos níveis altos. Foram adotadas estas ações:

- reescritas de Médio para Difícil: Q18, Q26, Q27, Q28, Q31, Q48 e Q49;
- reescritas de Médio para Muito difícil: Q21, Q22, Q35, Q42 e Q46;
- fortalecimento substantivo, sem mudança de nível: Q37, Q38, Q41, Q43, Q44, Q47 e Q50;
- preservação da Q45, já sustentada pelos arts. 28 e 29 da RN CFA nº 589/2020.

Os novos itens combinam regras anteriormente ensinadas sobre fonte, vigência, hierarquia, competência, jurisdição, sujeito, conduta, processo e consequência. A distribuição final do Dia 4 passou a **30 Médias / 15 Difíceis / 5 Muito difíceis**; nenhuma promoção decorre apenas de texto maior, quantidade de números ou troca de rótulo.

## Uso do banco e carga de estudo

Cada dia mantém 50 principais e 20 extras, mas o banco de 70 itens foi distribuído assim:

| Uso | Questões por dia | Momento |
|---|---:|---|
| Essenciais | Principais 1–15 + Extras 1–5 = 20 | 10 na Sessão C; as outras 10 abrem D+2 |
| Aprofundamento | Principais 16–30 + Extras 6–10 = 20 | após corrigir as Essenciais de D+2; ciclo próprio se necessário |
| Revisão | Principais 31–40 + Extras 11–15 = 15 | recuperação espaçada |
| Simulado | Principais 41–50 + Extras 16–20 = 15 | sem consulta, em ciclo posterior |

A classificação operacional não substitui o nível; ela indica quando resolver o item. Os 140 itens dos dois dias, inclusive os 40 extras, e seus respectivos comentários exibem a mesma categoria de uso.

| Dia | Sessões | Carga por sessão | Distribuição |
|---|---|---:|---|
| Dia 3 | A–C | 2h50 líquidas | teoria na ordem, Blocos 4–6 e amostra inicial de 10 Essenciais com correção integral |
| Dia 4 | A–C | 2h50 líquidas | teoria na ordem, Blocos 4–6 e amostra inicial de 10 Essenciais com correção integral |

No Dia 3, a amostra inicial é P1–P8 + E1–E2; no Dia 4, Principais 1–8 + Extras 4.1–4.2. As outras 10 Essenciais abrem D+2 e são corrigidas antes do Aprofundamento. Se o Aprofundamento não couber no tempo restante de D+2, ele continua em ciclo próprio antes de D+7. Revisão e Simulado permanecem reservados, respectivamente, para D+7 e para o ciclo seguinte.

Assim, teoria, 70 questões, comentários A–D, prática discursiva e caderno de erros não são apresentados como uma única sessão de estudo.

## Resultado final das questões principais

| Dia | Questões principais auditadas | Cobertas | Parciais | Não cobertas | Ambíguas | Reformuladas | Movidas |
| --- | ----------------------------: | -------: | -------: | -----------: | -------: | -----------: | ------: |
| Dia 3 | 50 | 50 | 0 | 0 | 0 | 2 | 0 |
| Dia 4 | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **100** | **100** | **0** | **0** | **0** | **2** | **0** |

A Q45 do Dia 4 aparece como uma substituição, e por isso não entra na coluna `Reformuladas`.

## Arquivos alterados

- `semana_01/semana_01_estudo.md`;
- `semana_01/semana_01_questoes.md`;
- `planejamento/padrao_semanal.md`;
- este relatório;
- `planejamento/plano_mestre_cra_pr_2026.md` e `README.md`, apenas para atualizar rastreabilidade e estado do lote.

## Limite do aceite

Este relatório aceita semanticamente as 100 questões principais e a jornada pedagógica dos Dias 3 e 4. Ele preserva o aceite anterior das extras dos Blocos 4–6, mas não declara toda a Semana 1 concluída: os Dias 1–2 ficaram fora do escopo e os bancos principais dos Dias 5–6 ainda exigem auditoria semântica própria.
