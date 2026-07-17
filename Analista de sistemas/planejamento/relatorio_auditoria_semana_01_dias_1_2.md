# Relatório de Auditoria Pedagógica — Semana 1, Dias 1 e 2

## Estado do lote

- **Baseline:** commit 1fcfbe3.
- **Abertura e fechamento técnico:** 15/07/2026.
- **Escopo:** Dia 1 — Arquitetura e Organização de Computadores; Dia 2 — Sistemas Operacionais; 50 questões principais e 20 complementares por dia.
- **Situação:** **Aprovado tecnicamente**, sem bloqueadores semânticos ou mecânicos.
- **Publicação:** [PR #7](https://github.com/Hedward1/Concursos/pull/7) aberto em rascunho contra a `main`, sem merge.
- **Modelo pedagógico:** Dias 3 e 4, aprovados no baseline e preservados sem alteração.
- **Fora do escopo:** Dias 5 e 6, super simulado e relatórios históricos; o lote seguinte não foi iniciado.

## Arquivos do lote

- [Apostila de estudo](../semana_01/semana_01_estudo.md): reorganização somente dos Dias 1 e 2.
- [Apostila de questões](../semana_01/semana_01_questoes.md): auditoria dos 140 itens dos Dias 1 e 2.
- [Padrão semanal](padrao_semanal.md): método permanente para semanas futuras.
- [Plano mestre](plano_mestre_cra_pr_2026.md): jornada e status incremental.
- [README de Analista de Sistemas](../README.md): índice e estado do material.
- Este relatório.

## Cobertura inicial e correção

A coluna Não cobertas inclui a subcategoria Cobradas antes de ser ensinadas. O quadro auxiliar separa ausência real e teoria localizada depois do ponto de cobrança.

| Dia | Principais | Extras | Cobertas | Parciais | Não cobertas | Ambíguas | Corrigidas |
| --- | ---------: | -----: | -------: | -------: | -----------: | ---------: | ---------: |
| Dia 1 | 50 | 20 | 42 | 9 | 19 | 0 | 70 |
| Dia 2 | 50 | 20 | 24 | 24 | 21 | 1 | 70 |
| **Total** | **100** | **40** | **66** | **33** | **40** | **1** | **140** |

| Dia | Não cobertas totais | Ausência real | Cobradas antes de ser ensinadas |
| --- | -------------------: | ------------: | --------------------------------: |
| Dia 1 | 19 | 3 | 16 |
| Dia 2 | 21 | 4 | 17 |

Falhas iniciais corrigidas:

- Blocos 4–6 apareciam antes da teoria principal;
- o Dia 2 continha seção-remendo posterior à revisão e ao checklist;
- 33 itens dependiam de conteúdo colocado depois da cobrança ou em dia futuro;
- nenhum dos 140 itens apresentava junto à questão Nível, Uso e Referência precisa;
- o banco completo não estava distribuído entre primeira passagem, D+2, D+7 e ciclo seguinte;
- a Q45 do Dia 2 admitia leitura ambígua; a E17 do Dia 1 recebeu clarificação adicional durante a revisão final.

## Teoria adicionada ou reorganizada

### Dia 1

- sistemas de numeração, complemento de dois, hexadecimal, arquitetura de von Neumann, CPU, memória, firmware, cache, pipeline, interrupções, polling, DMA, endereçamento e tradução de programas;
- Lei nº 4.769/1965, Decreto nº 61.934/1967, CFA versus CRA, natureza e jurisdição do CRA-PR, registro, regimento, ética, fiscalização, contribuições e normas dirigidas antes da cobrança;
- pontos de Português ensinados antes das questões; Bloco 6 limitado a recuperação e caderno de erros.

### Dia 2

- kernel, processos, escalonamento, memória virtual, thrashing, IPC, arquivos, backup, dispositivos, spooling, permissões, serviços, concorrência, deadlock, Windows, Linux e virtualização antes da prática;
- LIMPE, organização administrativa, atos, LAI, LGPD, improbidade e Lei nº 14.133/2021 antes da cobrança;
- pontos de Português ensinados antes das questões; seção-remendo removida e Bloco 6 sem conteúdo novo.

## Jornada executável da primeira passagem

| Sessão | Tempo | Conteúdo | Questões | Entrega |
| ------ | ----: | -------- | -------: | ------- |
| Dia 1 — A | 2h50 | abertura, orientação e Bloco 1 | 0 | conversões e mapa CPU–memória |
| Dia 1 — B | 2h50 | Blocos 2 e 3 | 0 | três casos técnicos explicados |
| Dia 1 — C | 3h | Blocos 4–6, mini revisão, fixação, checklist, banco e correção | 10 | primeira passagem corrigida e caderno de erros |
| Dia 2 — A | 2h50 | abertura, orientação e Bloco 1 | 0 | mapa kernel–processo–memória |
| Dia 2 — B | 2h50 | Blocos 2 e 3 | 0 | três diagnósticos de SO explicados |
| Dia 2 — C | 3h | Blocos 4–6, mini revisão, fixação, checklist, banco e correção | 10 | primeira passagem corrigida e caderno de erros |

Pausas ficam fora do tempo líquido. Não existem Sessões D, E ou F para concluir o banco.

## Calendário do banco

| Dia | Etapa | Itens | Regra |
| --- | --- | --- | --- |
| Dia 1 | Primeira passagem | Q1, Q2, Q3, Q5, Q6, Q7, Q11, Q13, E1, E16 | exatamente 10 Essenciais, com correção integral na Sessão C |
| Dia 1 | D+2 | Q9, Q12, Q16, Q17, Q25, E2, E3, E8, E13, E19 | concluir Essenciais antes de abrir Aprofundamento |
| Dia 2 | Primeira passagem | Q1, Q2, Q3, Q6, Q9, Q13, Q15, Q18, E3, E20 | exatamente 10 Essenciais, com correção integral na Sessão C |
| Dia 2 | D+2 | Q4, Q5, Q7, Q12, Q14, Q16, Q22, E1, E5, E16 | concluir Essenciais antes de abrir Aprofundamento |
| Ambos | antes de D+7 | saldo de Aprofundamento | concluir em ciclos próprios |
| Ambos | D+7 | itens de Revisão | recuperação espaçada, sem consulta |
| Ambos | ciclo seguinte | itens de Simulado | tempo marcado e correção posterior |

## Distribuição final

| Dia | Médias | Difíceis | Muito difíceis |
| --- | -----: | -------: | -------------: |
| Dia 1 | 50 | 16 | 4 |
| Dia 2 | 50 | 15 | 5 |

| Dia | Essenciais | Aprofundamento | Revisão | Simulado |
| --- | ---------: | -------------: | ------: | -------: |
| Dia 1 | 20 | 18 | 18 | 14 |
| Dia 2 | 20 | 18 | 17 | 15 |

Os rótulos finais decorrem do raciocínio exigido: Médio aplica ou compara diretamente; Difícil exige ao menos duas decisões; Muito difícil exige três ou mais filtros independentes.

## Reformulações, substituições e movimentação

- **Dia 1 — substituídas:** Q34, Q46, Q50, E7 e E15.
- **Dia 1 — reformuladas:** Q8, Q15, Q17, Q20, Q23, Q25, Q31, Q35, Q37, Q41, Q44, Q49, E3, E5, E9, E10, E11, E14 e E17.
- **Dia 1 — ajustes de ordem ou referência:** Q9, Q18, Q26, Q38, Q47, E8 e E20.
- **Dia 2 — reformuladas:** Q5, Q13, Q17, Q20, Q23, Q25, Q28, Q29, Q30, Q31, Q34, Q35, Q36, Q38, Q43, Q45, Q47 e E1–E15.
- **Dia 2 — ajuste de ordem:** E16.
- **Removidas:** nenhuma.
- **Movidas fisicamente ou renumeradas:** nenhuma; a movimentação pedagógica ocorreu por Uso e calendário.
- **Níveis antigos superestimados ou subestimados:** não havia Nível no baseline; os 140 itens receberam calibração semântica.
- **Usos operacionais alterados:** os 140 itens receberam classificação individual; somente 10 por dia ficaram na primeira passagem.

## Fontes oficiais conferidas

| Fonte | Objeto e relação normativa registrada |
| --- | --- |
| [Lei nº 4.769/1965](https://www.planalto.gov.br/ccivil_03/leis/l4769.htm) | exercício profissional e competências do Sistema CFA/CRAs; texto consolidado |
| [Decreto nº 61.934/1967](https://www.planalto.gov.br/ccivil_03/decreto/Antigos/D61934.htm) | regulamenta a Lei nº 4.769/1965 sem superá-la |
| [Lei nº 12.514/2011](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12514.htm) | contribuições devidas aos conselhos; texto compilado |
| [Lei nº 6.839/1980](https://www.planalto.gov.br/ccivil_03/leis/l6839.htm) | registro de empresas conforme atividade básica ou serviço a terceiros |
| [RN CFA nº 651/2024](https://documentos.cfa.org.br/?a=show&c=documento&id=955) | Regimento do CRA-PR; revoga a RN nº 263/2001 |
| [RN CFA nº 671/2025](https://documentos.cfa.org.br/?a=show&c=documento&id=1038) | Código de Ética vigente; revoga a RN nº 640/2024 |
| [RN CFA nº 649/2024](https://documentos.cfa.org.br/?a=show&c=documento&id=951) e [RN nº 670/2025](https://documentos.cfa.org.br/?a=show&c=documento&id=1033) | norma-base de registro e alteração pontual do art. 11; sem revogação integral da RN nº 649 |
| [RN CFA nº 589/2020](https://documentos.cfa.org.br/?a=show&c=documento&id=745) | fiscalização; revoga as RNs nº 446 e 449/2014 |
| [RN CFA nº 546/2018](https://documentos.cfa.org.br/?a=show&c=documento&id=700) | isenção de débitos; revoga a RN nº 510/2017 |
| [RN CFA nº 626/2023](https://documentos.cfa.org.br/?a=show&c=documento&id=803) | PERC temporal de 2023, alterado pela RN nº 627/2023; não tratado como programa atual |
| [CF, art. 37](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), [DL nº 200/1967](https://www.planalto.gov.br/ccivil_03/decreto-lei/del0200.htm) e [Lei nº 9.784/1999](https://www.planalto.gov.br/ccivil_03/leis/l9784.htm) | princípios, organização, autarquia e processo administrativo |
| [LAI](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm) e [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm) | transparência e proteção de dados coexistem |
| [Lei de Improbidade](https://www.planalto.gov.br/ccivil_03/leis/l8429compilada.htm) e [Lei nº 14.133/2021](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14133-1-abril-2021-791222-normaatualizada-pl.html) | improbidade compilada; licitação, pregão e contratação direta |

## Matriz nominal dos 140 itens

| Dia | ID | Categoria inicial | Ação | Nível final | Uso final | Gabarito | Âncora final | Resultado |
| --- | --- | --- | --- | --- | --- | :---: | --- | --- |
| 1 | Q1 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d1-numeracao | Aprovada |
| 1 | Q2 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | B | #s1-d1-numeracao | Aprovada |
| 1 | Q3 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | A | #s1-d1-representacao-dados | Aprovada |
| 1 | Q4 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | B | #s1-d1-hierarquia-memoria | Aprovada |
| 1 | Q5 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d1-cpu-componentes | Aprovada |
| 1 | Q6 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | B | #s1-d1-hierarquia-memoria | Aprovada |
| 1 | Q7 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | A | #s1-d1-interrupcoes-io | Aprovada |
| 1 | Q8 | Coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | B | #s1-d1-polling-dma | Aprovada |
| 1 | Q9 | Coberta | Alternativas reordenadas; classificada | Médio | Essenciais | A | #s1-d1-enderecamento | Aprovada |
| 1 | Q10 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | B | #s1-d1-enderecamento | Aprovada |
| 1 | Q11 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | A | #s1-d1-traducao-programas | Aprovada |
| 1 | Q12 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d1-traducao-programas | Aprovada |
| 1 | Q13 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d1-cache-localidade | Aprovada |
| 1 | Q14 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | B | #s1-d1-representacao-dados | Aprovada |
| 1 | Q15 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | D | #s1-d1-arquitetura-32-64 | Aprovada |
| 1 | Q16 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d1-cpu-componentes | Aprovada |
| 1 | Q17 | Coberta | Reformulada; classificada e rastreada | Difícil | Essenciais | A | #s1-d1-pipeline-desempenho | Aprovada |
| 1 | Q18 | Não coberta | Alternativas reordenadas; classificada | Médio | Aprofundamento | C | #s1-d1-cache-localidade | Aprovada |
| 1 | Q19 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | A | #s1-d1-representacao-dados | Aprovada |
| 1 | Q20 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | D | #s1-d1-representacao-dados | Aprovada |
| 1 | Q21 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d1-traducao-programas | Aprovada |
| 1 | Q22 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | B | #s1-d1-representacao-dados | Aprovada |
| 1 | Q23 | Coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | B | #s1-d1-pipeline-desempenho | Aprovada |
| 1 | Q24 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | D | #s1-d1-enderecamento | Aprovada |
| 1 | Q25 | Coberta | Reformulada; classificada e rastreada | Difícil | Essenciais | C | #s1-d1-polling-dma | Aprovada |
| 1 | Q26 | Coberta | Referência corrigida; classificada | Médio | Revisão | B | #s1-d1-firmware | Aprovada |
| 1 | Q27 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | A | #s1-d1-hierarquia-memoria | Aprovada |
| 1 | Q28 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | D | #s1-d1-representacao-dados | Aprovada |
| 1 | Q29 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Aprofundamento | C | #s1-d1-arquitetura-32-64 | Aprovada |
| 1 | Q30 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | A | #s1-d1-von-neumann-ciclo | Aprovada |
| 1 | Q31 | Coberta | Reformulada; classificada e rastreada | Médio | Revisão | D | #s1-d1-cache-localidade | Aprovada |
| 1 | Q32 | Não coberta | Preservada; classificada e rastreada | Médio | Simulado | D | #s1-d1-von-neumann-ciclo | Aprovada |
| 1 | Q33 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | C | #s1-d1-traducao-programas | Aprovada |
| 1 | Q34 | Cobrada antes de ser ensinada | Substituída; classificada e rastreada | Muito difícil | Aprofundamento | A | #s1-d1-arquitetura-32-64 | Aprovada |
| 1 | Q35 | Coberta | Reformulada; classificada e rastreada | Médio | Revisão | A | #s1-d1-cpu-componentes | Aprovada |
| 1 | Q36 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | D | #s1-d1-hierarquia-memoria | Aprovada |
| 1 | Q37 | Não coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | D | #s1-d1-interrupcoes-io | Aprovada |
| 1 | Q38 | Parcialmente coberta | Referência corrigida; classificada | Médio | Aprofundamento | B | #s1-d1-arquitetura-32-64 | Aprovada |
| 1 | Q39 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | A | #s1-d1-numeracao | Aprovada |
| 1 | Q40 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | D | #s1-d1-polling-dma | Aprovada |
| 1 | Q41 | Coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | A | #s1-d1-cache-escrita | Aprovada |
| 1 | Q42 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Simulado | B | #s1-d1-arquitetura-32-64 | Aprovada |
| 1 | Q43 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | A | #s1-d1-representacao-dados | Aprovada |
| 1 | Q44 | Coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | C | #s1-d1-traducao-programas | Aprovada |
| 1 | Q45 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d1-hierarquia-memoria | Aprovada |
| 1 | Q46 | Cobrada antes de ser ensinada | Substituída; classificada e rastreada | Muito difícil | Aprofundamento | D | #s1-d1-pipeline-desempenho | Aprovada |
| 1 | Q47 | Coberta | Referência corrigida; classificada | Médio | Simulado | A | #s1-d1-firmware | Aprovada |
| 1 | Q48 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | D | #s1-d1-cpu-componentes | Aprovada |
| 1 | Q49 | Coberta | Reformulada; classificada e rastreada | Muito difícil | Aprofundamento | B | #s1-d1-polling-dma | Aprovada |
| 1 | Q50 | Coberta | Substituída; classificada e rastreada | Difícil | Simulado | C | #s1-d1-representacao-dados | Aprovada |
| 1 | E1 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Essenciais | B | #s1-d1-cfa-cra | Aprovada |
| 1 | E2 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d1-lei-decreto | Aprovada |
| 1 | E3 | Parcialmente coberta | Reformulada; classificada e rastreada | Médio | Essenciais | B | #s1-d1-lei-decreto | Aprovada |
| 1 | E4 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d1-regimento-natureza | Aprovada |
| 1 | E5 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Aprofundamento | B | #s1-d1-regimento-natureza | Aprovada |
| 1 | E6 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Revisão | A | #s1-d1-regimento-natureza | Aprovada |
| 1 | E7 | Cobrada antes de ser ensinada | Substituída; classificada e rastreada | Difícil | Simulado | D | #s1-d1-etica | Aprovada |
| 1 | E8 | Cobrada antes de ser ensinada | Alternativas reordenadas; classificada | Médio | Essenciais | B | #s1-d1-registro-pj | Aprovada |
| 1 | E9 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Aprofundamento | A | #s1-d1-etica | Aprovada |
| 1 | E10 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Aprofundamento | C | #s1-d1-etica | Aprovada |
| 1 | E11 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Aprofundamento | B | #s1-d1-fiscalizacao-processo | Aprovada |
| 1 | E12 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Revisão | D | #s1-d1-contribuicoes | Aprovada |
| 1 | E13 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d1-registro-rn649-670 | Aprovada |
| 1 | E14 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Aprofundamento | A | #s1-d1-registro-rn649-670 | Aprovada |
| 1 | E15 | Cobrada antes de ser ensinada | Substituída; classificada e rastreada | Muito difícil | Simulado | C | #s1-d1-normas-dirigidas | Aprovada |
| 1 | E16 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d1-portugues-conectores | Aprovada |
| 1 | E17 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Médio | Revisão | A | #s1-d1-portugues-referencia | Aprovada |
| 1 | E18 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d1-portugues-reescrita | Aprovada |
| 1 | E19 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d1-portugues-crase | Aprovada |
| 1 | E20 | Coberta | Alternativas reordenadas; classificada | Médio | Revisão | C | #s1-d1-portugues-conectores | Aprovada |
| 2 | Q1 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d2-so-kernel | Aprovada |
| 2 | Q2 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | A | #s1-d2-processos-estados | Aprovada |
| 2 | Q3 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d2-processos-estados | Aprovada |
| 2 | Q4 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | B | #s1-d2-escalonamento | Aprovada |
| 2 | Q5 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Essenciais | C | #s1-d2-memoria-virtual | Aprovada |
| 2 | Q6 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | A | #s1-d2-memoria-virtual | Aprovada |
| 2 | Q7 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | A | #s1-d2-memoria-virtual | Aprovada |
| 2 | Q8 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d2-arquivos-backup | Aprovada |
| 2 | Q9 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | B | #s1-d2-arquivos-backup | Aprovada |
| 2 | Q10 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Revisão | A | #s1-d2-seguranca-permissoes | Aprovada |
| 2 | Q11 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Revisão | D | #s1-d2-servicos-logs | Aprovada |
| 2 | Q12 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d2-dispositivos-spooling | Aprovada |
| 2 | Q13 | Coberta | Reformulada; classificada e rastreada | Médio | Essenciais | B | #s1-d2-concorrencia | Aprovada |
| 2 | Q14 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | A | #s1-d2-concorrencia | Aprovada |
| 2 | Q15 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d2-concorrencia | Aprovada |
| 2 | Q16 | Coberta | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d2-concorrencia | Aprovada |
| 2 | Q17 | Não coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | D | #s1-d2-processos-estados | Aprovada |
| 2 | Q18 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d2-so-kernel | Aprovada |
| 2 | Q19 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d2-servicos-logs | Aprovada |
| 2 | Q20 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | A | #s1-d2-escalonamento | Aprovada |
| 2 | Q21 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d2-escalonamento | Aprovada |
| 2 | Q22 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Essenciais | D | #s1-d2-seguranca-permissoes | Aprovada |
| 2 | Q23 | Não coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | C | #s1-d2-servicos-logs | Aprovada |
| 2 | Q24 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Simulado | C | #s1-d2-servicos-logs | Aprovada |
| 2 | Q25 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | D | #s1-d2-processos-estados | Aprovada |
| 2 | Q26 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | A | #s1-d2-arquivos-backup | Aprovada |
| 2 | Q27 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | D | #s1-d2-seguranca-permissoes | Aprovada |
| 2 | Q28 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | A | #s1-d2-escalonamento | Aprovada |
| 2 | Q29 | Não coberta | Reformulada; classificada e rastreada | Muito difícil | Aprofundamento | D | #s1-d2-virtualizacao | Aprovada |
| 2 | Q30 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | C | #s1-d2-memoria-virtual | Aprovada |
| 2 | Q31 | Parcialmente coberta | Reformulada; classificada e rastreada | Médio | Revisão | D | #s1-d2-dispositivos-spooling | Aprovada |
| 2 | Q32 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | C | #s1-d2-windows-linux | Aprovada |
| 2 | Q33 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Simulado | B | #s1-d2-processos-estados | Aprovada |
| 2 | Q34 | Parcialmente coberta | Reformulada; classificada e rastreada | Muito difícil | Aprofundamento | C | #s1-d2-concorrencia | Aprovada |
| 2 | Q35 | Parcialmente coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | B | #s1-d2-arquivos-backup | Aprovada |
| 2 | Q36 | Coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | A | #s1-d2-memoria-virtual | Aprovada |
| 2 | Q37 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Simulado | B | #s1-d2-escalonamento | Aprovada |
| 2 | Q38 | Parcialmente coberta | Reformulada; classificada e rastreada | Muito difícil | Aprofundamento | B | #s1-d2-concorrencia | Aprovada |
| 2 | Q39 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Revisão | D | #s1-d2-seguranca-permissoes | Aprovada |
| 2 | Q40 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | C | #s1-d2-processos-estados | Aprovada |
| 2 | Q41 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Simulado | B | #s1-d2-seguranca-permissoes | Aprovada |
| 2 | Q42 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Simulado | A | #s1-d2-so-kernel | Aprovada |
| 2 | Q43 | Não coberta | Reformulada; classificada e rastreada | Difícil | Aprofundamento | B | #s1-d2-processos-estados | Aprovada |
| 2 | Q44 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Revisão | B | #s1-d2-memoria-virtual | Aprovada |
| 2 | Q45 | Ambígua | Reformulada; classificada e rastreada | Difícil | Aprofundamento | C | #s1-d2-servicos-logs | Aprovada |
| 2 | Q46 | Parcialmente coberta | Preservada; classificada e rastreada | Médio | Aprofundamento | A | #s1-d2-seguranca-permissoes | Aprovada |
| 2 | Q47 | Parcialmente coberta | Reformulada; classificada e rastreada | Médio | Simulado | D | #s1-d2-escalonamento | Aprovada |
| 2 | Q48 | Coberta | Preservada; classificada e rastreada | Médio | Revisão | C | #s1-d2-concorrencia | Aprovada |
| 2 | Q49 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | B | #s1-d2-arquivos-backup | Aprovada |
| 2 | Q50 | Coberta | Preservada; classificada e rastreada | Médio | Simulado | A | #s1-d2-concorrencia | Aprovada |
| 2 | E1 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Médio | Essenciais | C | #s1-d2-limpe-organizacao | Aprovada |
| 2 | E2 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Médio | Revisão | A | #s1-d2-limpe-organizacao | Aprovada |
| 2 | E3 | Coberta | Reformulada; classificada e rastreada | Médio | Essenciais | D | #s1-d2-limpe-organizacao | Aprovada |
| 2 | E4 | Coberta | Reformulada; classificada e rastreada | Médio | Simulado | B | #s1-d2-limpe-organizacao | Aprovada |
| 2 | E5 | Coberta | Reformulada; classificada e rastreada | Médio | Essenciais | B | #s1-d2-limpe-organizacao | Aprovada |
| 2 | E6 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Aprofundamento | D | #s1-d2-atos-controle | Aprovada |
| 2 | E7 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Médio | Revisão | A | #s1-d2-atos-controle | Aprovada |
| 2 | E8 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Aprofundamento | B | #s1-d2-atos-controle | Aprovada |
| 2 | E9 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Médio | Revisão | D | #s1-d2-lai-lgpd | Aprovada |
| 2 | E10 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Muito difícil | Aprofundamento | A | #s1-d2-lai-lgpd | Aprovada |
| 2 | E11 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Revisão | B | #s1-d2-improbidade | Aprovada |
| 2 | E12 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Médio | Simulado | C | #s1-d2-improbidade | Aprovada |
| 2 | E13 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Difícil | Simulado | D | #s1-d2-licitacoes | Aprovada |
| 2 | E14 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Muito difícil | Aprofundamento | A | #s1-d2-licitacoes | Aprovada |
| 2 | E15 | Cobrada antes de ser ensinada | Reformulada; classificada e rastreada | Médio | Simulado | B | #s1-d2-licitacoes | Aprovada |
| 2 | E16 | Cobrada antes de ser ensinada | Alternativas reordenadas; classificada | Médio | Essenciais | A | #s1-d2-portugues-concordancia | Aprovada |
| 2 | E17 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Revisão | B | #s1-d2-portugues-ambiguidade-onde | Aprovada |
| 2 | E18 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Revisão | A | #s1-d2-portugues-ambiguidade-onde | Aprovada |
| 2 | E19 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Revisão | D | #s1-d2-portugues-pontuacao | Aprovada |
| 2 | E20 | Cobrada antes de ser ensinada | Preservada; classificada e rastreada | Médio | Essenciais | C | #s1-d2-portugues-comando | Aprovada |

## Evidências de validação final

| Controle | Dia 1 | Dia 2 |
| --- | ---: | ---: |
| Questões / gabaritos / comentários | 70 / 70 / 70 | 70 / 70 / 70 |
| Falhas de sincronismo | 0 | 0 |
| Referências ou âncoras ausentes | 0 | 0 |
| Alertas de comprimento 0,70–1,30 | 0 | 0 |
| Respostas globais A/B/C/D | 18/17/18/17 | 18/17/18/17 |
| Médio A/B/C/D | 13/12/13/12 | 13/12/13/12 |
| Difícil A/B/C/D | 4/4/4/4 | 3/4/4/4 |
| Muito difícil A/B/C/D | 1/1/1/1 | 2/1/1/1 |
| Primeira passagem A/B/C/D | 3/3/3/1 | 2/2/3/3 |
| D+2 A/B/C/D | 2/2/3/3 | 3/2/3/2 |

Validações independentes confirmaram resposta única, comentários A–D, dificuldade substantiva e teoria anterior suficiente. Nenhuma questão depende de conteúdo posterior.

## Preservação e escopo

- Estudo dos Dias 3–6: SHA-256 normalizado c91bbd2a222ff65fe2f2db8a7b476f3288e2c21c2cfb45d7491b8aaf1bdfb6bf no baseline e no lote.
- Questões dos Dias 3–6: SHA-256 normalizado 8fdc736f9e947066cad958b3670c37514c8e2b9240f9a1296297f105123c502d no baseline e no lote.
- Quatro âncoras de compatibilidade foram mantidas nos Dias 1–2 para que referências congeladas dos Dias 5–6 continuem válidas.
- Super simulado e relatórios históricos: sem diff contra 1fcfbe3.
- Alterações restritas aos seis arquivos autorizados.
- git diff --check: sem erros.

## Critérios de aceite

- [x] os 100 itens principais e 40 complementares foram auditados individualmente;
- [x] a matriz possui categoria inicial, ação, nível, uso, gabarito, âncora e resultado nas 140 linhas;
- [x] a ordem física segue abertura, Blocos 1–6, mini revisão, fixação, checklist, roteiro e correção;
- [x] nenhuma teoria resolutiva ou seção-remendo aparece depois da cobrança;
- [x] cada dia termina em três sessões de 2h30 a 3h;
- [x] a primeira passagem exige 10 Essenciais e correção integral;
- [x] D+2, Aprofundamento antes de D+7, Revisão D+7 e Simulado seguinte estão definidos;
- [x] item e comentário possuem Nível, Uso e Referência válidos e sincronizados;
- [x] cada questão possui resposta única e comentário de A–D;
- [x] dificuldade decorre de decisões reais;
- [x] gabaritos, paralelismo, duplicidades e comprimento foram recalculados;
- [x] fontes oficiais, objeto, alteração, revogação e temporalidade foram registrados;
- [x] o Bloco 6 não introduz conteúdo novo;
- [x] Dias 3–6 e arquivos históricos foram preservados;
- [x] git diff --check terminou sem erro;
- [x] o PR em rascunho deste lote foi publicado, sem merge.

## Veredito

| Item | Resultado |
| --- | --- |
| Status técnico | **Aprovado, sem bloqueadores** |
| Questões corrigidas | 140 de 140 |
| Dependências de conteúdo posterior | 0 |
| Ambiguidades remanescentes | 0 |
| Sessões acima do limite | 0 |
| Próximo lote | não iniciado; aguarda revisão do PR #7 |
| Publicação | [PR #7 em rascunho](https://github.com/Hedward1/Concursos/pull/7), sem merge |
