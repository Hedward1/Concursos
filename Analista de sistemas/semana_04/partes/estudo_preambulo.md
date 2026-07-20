# Apostila de Estudo — Semana 4

> **Execução:** use `semana_04_jornada.md` como cronograma vigente. A apostila ensina antes de cobrar; o banco completo é distribuído entre D0, D+2, D+7, D+21, aprofundamento e simulado.

## CRA-PR 2026 — Analista de Sistemas

- **Período:** 03/08/2026 a 08/08/2026.
- **Foco técnico:** requisitos, análise e projeto orientados a objetos, UML, engenharia de software, testes, qualidade, manutenção, gerenciamento de projetos e gestão de recursos informacionais em primeiro contato.
- **Banca:** Instituto Consulplan.
- **Situação do material:** **Material aprovado para execução**; execução do candidato não presumida.

## Versão do edital e limite da cobertura

O recorte foi conferido no edital consolidado conforme Retificação I, preservado em `../edital/edital_cra_pr_2026_analista_sistemas_retificacao_1.pdf`, especialmente na página 28, itens 13 a 17 de Conhecimentos do Cargo.

Esta semana cobre ou inicia, conforme o Plano Mestre:

- análise e projeto orientados a objetos e casos de uso;
- UML: classes, objetos, estados, comunicação/colaboração, sequência, atividades, componentes e implementação/implantação;
- ferramentas de apoio à análise, ao projeto e à codificação;
- engenharia de software e modelos cascata, espiral, orientado a reuso, prototipação, RAD, evolucionário e incremental;
- fases de concepção, elaboração, construção e transição;
- testes, qualidade e manutenção como desdobramentos operacionais de engenharia de software previstos no cronograma;
- conceitos, planejamento, acompanhamento e controle de projetos, com primeiro contato em escopo, WBS/EAP, tempo, custos, qualidade, recursos humanos, comunicações, riscos, aquisições e integração;
- GED, workflow, BPM, ERP, CRM, ITIL e COBIT em visão inicial, preparando a retomada da Semana 7.

O edital cita `PMBOK`, `ITIL` e `COBIT` sem fixar edição. Por isso, o núcleo desta semana ensina conceitos duráveis e explicita qualquer detalhe dependente de versão; uma edição corrente não é presumida como recorte obrigatório da prova. Do mesmo modo, a teoria de testes, qualidade e manutenção não inventa norma ou versão ausente do edital.

## Fontes técnicas de controle

Para terminologia e atualização, a produção foi contrastada com fontes primárias:

- [especificação oficial UML 2.5.1 — OMG](https://www.omg.org/spec/UML/2.5.1);
- [página oficial do PMBOK — PMI](https://www.pmi.org/standards/pmbok), usada sem impor edição ao edital;
- [estrutura oficial do ITIL — PeopleCert](https://www.peoplecert.org/Frameworks-Professionals/ITIL-framework), usada apenas no nível introdutório previsto;
- [página oficial do COBIT — ISACA](https://www.isaca.org/resources/cobit), usada para distinguir governança e gestão de informação e tecnologia.

Essas fontes controlam precisão, mas não ampliam a cobrança. A aderência à Consulplan aparece no tipo de decisão exigida: comando preciso, alternativas do mesmo domínio, cenários curtos, associação de artefato a finalidade e atenção especial a `EXCETO`, `INCORRETA` e `NÃO`.

## Prioridade na prova

Conhecimentos do Cargo possuem 15 questões e valem 30 pontos, a maior parcela técnica da objetiva. Requisitos, UML e engenharia se encadeiam: uma mesma situação pode pedir a necessidade correta, o diagrama adequado, o modelo de ciclo de vida e o mecanismo de controle. Por isso, o tema principal ocupa os Blocos 1–3, enquanto as revisões acumuladas ficam dentro do Bloco 4, sem criar uma sessão extra.

## Como usar esta apostila

1. abra a jornada e siga apenas as âncoras do dia;
2. conclua Blocos 1–3 e o produto prático antes das questões principais;
3. cumpra Blocos 4–6 somente dentro dos tempos declarados;
4. resolva seis questões principais Essenciais em D0 e avance até dez apenas quando couber correção integral A–D;
5. marque confiança de 0 a 3 antes de consultar o gabarito;
6. registre regra, causa do erro, contraexemplo e datas D+2, D+7 e D+21;
7. deixe Aprofundamento, Revisão e Simulado nas filas próprias: 420 itens não significam 420 itens na primeira passagem;
8. use as questões oficiais somente no caderno original e como substituição de itens da fila Simulado.

## Rotina diária fixa — 6h líquidas

| Etapa | Tempo | Função |
|---|---:|---|
| Sessão A | 170 min | Blocos 1–3: aquisição, contraste, exemplo e produto prático |
| Sessão B | 170 min | Blocos 4–6, seis Essenciais, correção e fechamento |
| Consolidação | 20 min | caderno de erros, confiança e agendamento |
| **Total** | **360 min** | pausas fora da carga líquida |

A ordem física é obrigatória: teoria-base, aprofundamento, aplicação, revisão fixa, Português/discursiva, recuperação ativa, mini revisão, questões, correção e fechamento.

## Mapa da Semana 4

| Dia | Blocos 1–3 | Bloco 4 | Bloco 5 | Bloco 6 |
|---:|---|---|---|---|
| 1 | requisitos, análise orientada a objetos e casos de uso | Legislação CRA/CFA + D+21 da Semana 1 + saldos da Semana 3 | Português e recorte/tese | recuperação do Dia 1 |
| 2 | classes, objetos, sequência, comunicação, atividades e estados | Administração Pública + D+21 da Semana 1 + D+7 da Semana 3 | Português e desenvolvimento 1 | recuperação dos Dias 1–2 |
| 3 | componentes, implementação/implantação e ferramentas de apoio | Legislação CRA/CFA + D+21 da Semana 1 + D+7 da Semana 3 | Português e desenvolvimento 2 | recuperação de requisitos/UML |
| 4 | engenharia, modelos de ciclo de vida e projetos em primeiro contato | Administração Pública/RLM + D+21 da Semana 1 + D+7 da Semana 3 | Português e introdução/conclusão | recuperação dos Dias 3–4 |
| 5 | testes, qualidade, manutenção e fases do processo | Legislação CRA/CFA + D+21 da Semana 1 + D+7 da Semana 3 | Português e plano integral | recuperação de engenharia/testes |
| 6 | integração UML/engenharia e noções de GED, workflow, BPM, ERP, CRM, ITIL e COBIT | D+21 da Semana 1 + D+7 da Semana 3 | Português e texto integral | caderno de erros integrado |

## Matriz de rastreabilidade da cobertura

| Tópico do edital/cronograma | Dia e seção de teoria | Questões principais | Extras | Estado de produção |
|---|---|---|---|---|
| requisitos, OO e casos de uso | Dia 1 | S4D1Q001–S4D1Q050 | revisão fixa do Dia 1 | coberto |
| UML estrutural e comportamental do Dia 2 | Dia 2 | S4D2Q051–S4D2Q100 | revisão fixa do Dia 2 | coberto |
| componentes, implantação e ferramentas | Dia 3 | S4D3Q101–S4D3Q150 | revisão fixa do Dia 3 | coberto |
| engenharia, ciclos de vida e projetos inicial | Dia 4 | S4D4Q151–S4D4Q200 | revisão fixa do Dia 4 | coberto |
| testes, qualidade, manutenção e fases | Dia 5 | S4D5Q201–S4D5Q250 | revisão fixa do Dia 5 | coberto |
| integração e gestão de recursos informacionais inicial | Dia 6 | S4D6Q251–S4D6Q300 | revisão fixa do Dia 6 | coberto |

O estado `coberto` registra que teoria, exemplos, 420 itens e super simulado passaram pelas auditorias; não presume a execução pelo candidato. Programação, APIs, DevOps, contratação de TIC e aprofundamento de governança continuam nas semanas do Plano Mestre.

---
