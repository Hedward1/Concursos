# Apostila de Estudo - Semana 3

> **Execução:** use `semana_03_jornada.md` como cronograma vigente. Esta apostila ensina o conteúdo na ordem necessária para a prática; o banco completo é distribuído entre D0, D+2, D+7, D+21 e ciclos de aprofundamento ou simulado.

## CRA-PR 2026 - Analista de Sistemas

- **Período:** 27/07/2026 a 01/08/2026.
- **Foco técnico:** Banco de Dados avançado, modelagem, SQL e Sistemas de Gerência de Banco de Dados.
- **Banca:** Instituto Consulplan.
- **Situação do material:** Material aprovado para execução em 19/07/2026; execução do candidato pendente.
- **Execução do candidato:** não presumida.

## Versão do edital utilizada

O recorte foi conferido no edital consolidado conforme Retificação I, preservado em `../edital/edital_cra_pr_2026_analista_sistemas_retificacao_1.pdf`, especialmente na página 28, itens 6, 7 e 8 de Conhecimentos do Cargo.

Esta semana cobre literalmente:

- conceitos e princípios de banco de dados;
- administração e independência de dados;
- dicionário de dados e níveis da arquitetura;
- modelo e bancos relacionais, álgebra relacional e modelagem;
- normalização, MER e mapeamento MER-relacional;
- SQL ANSI para definição, consulta e manipulação de dados;
- Transact-SQL e sistemas de suporte à inteligência de negócio;
- segurança, transações, concorrência, recuperação e integridade em SGBD;
- stored procedures, views, triggers, índices, otimização e transações distribuídas;
- SQL Server, MySQL e PostgreSQL.

O perfil do Instituto Consulplan orienta o modo de treinar, mas não amplia esse rol. Questões autorais usam comandos precisos, alternativas do mesmo domínio, resultados de consultas, cenários de administração de dados e decisões técnicas com requisitos explícitos.

## Prioridade na prova

Conhecimentos do Cargo possuem 15 questões e valem 30 pontos, a maior parcela técnica da objetiva. Banco de Dados forma um bloco extenso e interligado: uma única questão pode exigir modelo, restrição, SQL e consequência transacional. Por isso, o tema principal recebe 4h30 líquidas por dia, sem abandonar as revisões do núcleo comum.

## Como usar esta apostila

1. abra a jornada e siga apenas as âncoras do dia;
2. execute os Blocos 1, 2 e 3 e entregue o produto prático antes das revisões;
3. cumpra os Blocos 4 e 5 somente depois da teoria principal;
4. use o Bloco 6 apenas para recuperar conteúdo já ensinado;
5. resolva seis questões principais Essenciais no D0 e avance até dez somente quando couber correção integral A-D;
6. marque confiança de 0 a 3 antes de consultar o gabarito;
7. registre no caderno de erros a regra, o motivo do erro, um contraexemplo e as datas D+2, D+7 e D+21;
8. deixe Aprofundamento, Revisão e Simulado para as filas próprias; o tamanho do banco não aumenta as seis horas do dia.

## Rotina diária fixa - 6h líquidas

| Etapa | Tempo | Função |
|---|---:|---|
| Sessão A | 170 min | Blocos 1–3: aquisição, contraste, exemplos e produto prático |
| Sessão B | 170 min | Blocos 4–6, seis Essenciais, correção e fechamento |
| Consolidação | 20 min | caderno de erros, confiança e agendamento |
| **Total** | **360 min** | pausas fora da carga líquida |

A ordem física é obrigatória: teoria-base, aprofundamento, prática guiada, revisão fixa, Português/discursiva, recuperação ativa, mini revisão, mapa, checklist, questões e correção.

## Mapa da Semana 3

| Dia | Blocos 1–3 | Bloco 4 | Bloco 5 | Bloco 6 |
|---:|---|---|---|---|
| 1 | SGBD, administração de dados, três esquemas, independência e dicionário | D+2/D+7 da Semana 2, Legislação e Google Documentos | Português e recorte/tese | recuperação do Dia 1 |
| 2 | modelo relacional, MER, mapeamento, álgebra e normalização | D+7 da Semana 2, Administração Pública e Google Planilhas | Português e desenvolvimento 1 | recuperação dos Dias 1–2 |
| 3 | SQL ANSI: consulta, filtros, NULL, junções, grupos e subconsultas | D+2 do Dia 1, D+7 da Semana 2, Legislação e RLM | Português e desenvolvimento 2 | recuperação de modelagem e SQL |
| 4 | DDL, DML, Transact-SQL, views, procedures e triggers | D+2 do Dia 2, D+7 da Semana 2 e Administração Pública | Português, introdução e conclusão | recuperação dos Dias 3–4 |
| 5 | transações, concorrência, recuperação, integridade, segurança e distribuição | D+2 do Dia 3, D+7 da Semana 2, Legislação e internet | Português e plano integral | recuperação transacional |
| 6 | índices, otimização, SQL Server, MySQL, PostgreSQL e BI | D+2 do Dia 4, D+7 da Semana 2, RLM e Informática | texto integral manuscrito | recuperação integrada |

## Mapa das 120 questões extras

| Dia | Revisões que sustentam as 20 extras | Divisão declarada |
|---:|---|---|
| 1 | Legislação CRA/CFA, Google Documentos e Português | 8 + 8 + 4, intercaladas por uso |
| 2 | Administração Pública, Google Planilhas e Português | 7 + 7 + 6, intercaladas por uso |
| 3 | Legislação CRA/CFA, RLM e Português | 10 + 5 + 5 |
| 4 | Administração Pública e Português | 12 + 8 |
| 5 | Legislação CRA/CFA, Português e internet | 10 + 5 + 5 |
| 6 | RLM, revisão Google Documentos/Planilhas/internet e Português/discursiva | 5 + 10 + 5 |

O Bloco 6 possui entrega prática e nenhuma questão objetiva própria: ele recupera os conceitos cobrados nos Blocos 1–5 e alimenta o caderno acumulado. As extras Essenciais 1–5 de cada dia abrem pela primeira vez no D+7; as demais respeitam o uso indicado.

## Matriz de rastreabilidade da cobertura

| Tópico do edital | Dia e seção de teoria | Questões principais | Extras | Estado de produção |
|---|---|---|---|---|
| conceitos, SGBD, administração e dicionário | Dia 1 | S3D1Q001–S3D1Q050 | revisões do Dia 1 | coberto |
| modelo relacional, álgebra, MER, mapeamento e normalização | Dia 2 | S3D2Q051–S3D2Q100 | revisões do Dia 2 | coberto |
| SQL ANSI: consulta e manipulação por consulta | Dia 3 | S3D3Q101–S3D3Q150 | revisões do Dia 3 | coberto |
| definição/manipulação, T-SQL, views, procedures e triggers | Dia 4 | S3D4Q151–S3D4Q200 | revisões do Dia 4 | coberto |
| segurança, transações, concorrência, recuperação, integridade e distribuição | Dia 5 | S3D5Q201–S3D5Q250 | revisões do Dia 5 | coberto |
| índices, otimização, SGBDs e inteligência de negócio | Dia 6 | S3D6Q251–S3D6Q300 | revisões do Dia 6 | coberto |

O estado desta matriz será alterado para `coberto` somente depois de a teoria, os exemplos e as 420 referências passarem pela auditoria. Tópicos das Semanas 4–9 não serão antecipados para completar questões.

## Delimitação da cobertura

Esta semana encerra o primeiro contato pesado com os itens 6, 7 e 8. Integração por XML/Web Services, nuvem, backup como tópico autônomo, IA, UML, engenharia de software, programação, DevOps, governança e contratações de TIC permanecem nas semanas previstas no Plano Mestre.

Recursos de fornecedores aparecem apenas quando necessários para comparar os três SGBDs expressamente nomeados. Sintaxe ou comportamento dependente de versão é identificado como tal; não se transforma uma particularidade de produto em regra universal do SQL.

---
