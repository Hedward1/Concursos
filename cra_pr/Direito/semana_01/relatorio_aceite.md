# Relatório de aceite - Semana 1

## Resultado

| Item | Resultado |
|---|---|
| Escopo | Direito Constitucional, itens 1.1 a 4.6 do edital, e primeira volta da Lei nº 4.769/1965 |
| Período planejado | 13/07/2026 a 18/07/2026 |
| Aceite de produção | **Aprovado - 97/100** |
| Falhas eliminatórias de conteúdo ou estrutura | **0** |
| Aceite operacional | **Pendente** |
| Status | **Material aprovado para execução; auditoria operacional pendente** |

O material está pronto para uso, mas a semana ainda não está `Concluída`. A conclusão depende da execução do ciclo pelo candidato, do preenchimento das métricas, da correção dos erros e da produção manuscrita e cronometrada do parecer diagnóstico.

## Base documental e conferência

- edital-base: Concurso Público CRA-PR nº 1/2026, consolidado conforme Retificação I;
- arquivo local: `../edital/edital_cra_pr_2026_advogado_analista_juridico_retificacao_1.pdf`;
- SHA-256 do edital: `10B3B012F3B68149B4E4EA8A0CD6489B934D65C5D3E8F5FE12565FE91CAA168E`;
- data da conferência do edital, das fontes e dos atos publicados pela banca: **13/07/2026**;
- situação verificada na página oficial nessa data: Edital de Abertura e Retificação I, sem retificação posterior listada;
- matriz de controle: `../fontes/matriz_edital_fontes.md`.

### Alertas de vigência preservados

- a RN CFA nº 640/2024 está revogada e não foi tratada como norma vigente; a referência atual do edital consolidado é a RN CFA nº 671/2025;
- a Resolução CNJ nº 115/2010 permanece identificada como referência histórica do edital e como ato revogado pela Resolução CNJ nº 303/2019;
- a Convenção nº 87 da OIT permanece identificada como não ratificada pelo Brasil;
- Constituição, emendas, leis e precedentes utilizados na Semana 1 estão registrados por fonte oficial na matriz.

## Cobertura e integridade

| Evidência | Resultado |
|---|---:|
| Tópicos previstos para a Semana 1 | 10/10 linhas cobertas |
| Dias didáticos completos | 6 |
| Casos resolvidos | 21 |
| Campos obrigatórios dos casos | 21/21 com pergunta, norma, raciocínio, solução, consequência, erro provável e variação |
| Mapas de conexões | 6 |
| Blocos diários de fontes | 6 |
| Questões principais | 300 |
| Questões extras CRA/CFA | 120 |
| Banco principal total | 420 |
| Alternativas A a D no banco | 1.680 |
| Gabaritos | 420/420 |
| Comentários individualizados | 420/420 |
| Referências à teoria | 420/420 |
| Questões órfãs | 0 |
| Lacunas ou duplicações na faixa Q001-Q420 | 0 |
| Alternativas E | 0 |
| Super simulado | 60 questões, 240 alternativas, 60 gabaritos, 60 comentários e 60 referências |
| Pareceres | 5 exercícios progressivos + 1 caso completo com espelho, rubrica e resposta-modelo |

## Auditoria do banco de questões

| Fragmento | Faixa | Itens | A | B | C | D | Correta como única mais longa |
|---|---:|---:|---:|---:|---:|---:|---:|
| `questoes/dias_01_e_02.md` | Q001-Q140 | 140 | 35 | 35 | 35 | 35 | 34 |
| `questoes/dias_03_e_04.md` | Q141-Q280 | 140 | 36 | 36 | 34 | 34 | 35 |
| `questoes/dias_05_e_06.md` | Q281-Q420 | 140 | 35 | 35 | 35 | 35 | 34 |
| **Total** | **Q001-Q420** | **420** | **106** | **106** | **104** | **104** | **103 (24,52%)** |

A varredura estrutural confirmou quatro alternativas e uma chave por item. A leitura semântica verificou comando, resposta, plausibilidade dos distratores, comentário de A a D e correspondência com a seção indicada da apostila.

Na checagem de repetição, houve zero enunciado exatamente duplicado e zero par com similaridade de Jaccard igual ou superior a 0,72 no banco principal. O resultado não substitui revisão humana, mas reduz o risco de variações apenas cosméticas.

## Auditoria do super simulado

- 60 questões inéditas em relação ao banco principal;
- distribuição do gabarito: A = 15, B = 15, C = 15 e D = 15;
- 15 respostas corretas como única alternativa mais longa, equivalentes a 25%;
- 60 comentários com análise individual de A, B, C e D;
- 60 referências específicas a seções existentes da apostila;
- zero alternativa E, lacuna de numeração ou divergência entre resposta e comentário;
- zero par com similaridade de Jaccard igual ou superior a 0,50 em comparação com o banco principal.

## Rubrica de produção

| Dimensão | Nota | Justificativa |
|---|---:|---|
| Fidelidade ao edital, vigência e fontes | 20/20 | edital consolidado identificado por hash e fontes oficiais registradas |
| Cobertura e profundidade da teoria | 10/10 | seis dias autossuficientes, com conceitos, distinções, efeitos e aplicação |
| Lei seca, jurisprudência e distinção de fontes | 10/10 | etiquetas e referências específicas, sem conflito de vigência não declarado |
| Casos e exemplos resolvidos | 10/10 | 21 casos completos com os sete campos do padrão |
| Alinhamento teoria-questões | 10/10 | 420/420 referências específicas e seções existentes |
| Qualidade das questões | 9/10 | variedade e equilíbrio auditados; itens autorais ainda não têm calibração empírica de banca |
| Qualidade dos comentários | 14/15 | A a D analisadas em todos os itens; comentários simples são necessariamente mais concisos |
| Parecer jurídico | 9/10 | material completo; falta a execução manuscrita, cronometrada e corrigida pelo candidato |
| Organização pedagógica | 5/5 | navegação, banco modular, revisões e caderno de erros integrados |
| **Total** | **97/100** | **aceite de produção aprovado** |

A nota avalia o material produzido. Ela não mede domínio do candidato e não antecipa o aceite operacional.

## Integridade dos arquivos

Hashes SHA-256 calculados após a auditoria final:

| Arquivo | SHA-256 |
|---|---|
| `../fontes/matriz_edital_fontes.md` | `FE304CF410A1A65851D9AD0B664541671EB8E34E64ADB7B823482C035BF32819` |
| `README.md` | `820BD43324D26B74334391064BB846F6C6267DC5EAC3B709EE6E52FBDFB38864` |
| `semana_01_estudo.md` | `8EBB50B03589717246A23379EC797F7200597C00C4F6AABB86AEF51921319C68` |
| `semana_01_questoes.md` | `5577A9D1796083E6C9F01219B77E7960A76884885DEA170ACC63B673E0D65A38` |
| `questoes/dias_01_e_02.md` | `B1DCFF1CAC6C4A9A8A64B67E0EB9ACFA5461173EBBD33173E548C2389A42CAB4` |
| `questoes/dias_03_e_04.md` | `5B5355040642C71CA9E331D35FCCED23F412AB7C5B5846B843CA2588F52610A0` |
| `questoes/dias_05_e_06.md` | `0C412C609E065B53BE0682B4A3B75B9284535448AAAC32E4E2445C2A46B7A936` |
| `semana_01_pareceres.md` | `5F06ED033DBC73373B0A635FCE5B6B080BA477722F2B800CF38465621244FD5D` |
| `semana_01_super_simulado.md` | `0FF63A53CDC90386B18F1C21C394389B69A7B51A0032A64442F99C9B232CEA01` |
| `semana_01_caderno_erros.md` | `D2C50F9586C632E4E001C39ACA82689DDB0A084D8EF88A3C4CBDE808DEAFBD52` |

O próprio relatório não integra a tabela porque incluir seu hash no conteúdo alteraria novamente o arquivo.

## Pendências para o aceite operacional

- [ ] executar os seis núcleos diários e registrar tempo e confiança;
- [ ] preencher a folha de desempenho do banco de questões;
- [ ] corrigir erros e acertos inseguros e alimentar `semana_01_caderno_erros.md`;
- [ ] escrever à mão o parecer do Dia 6, sem consulta, em 30 a 60 linhas e no limite de 60 minutos;
- [ ] corrigir o parecer com o espelho de 15 pontos e a rubrica linguística de 5 pontos;
- [ ] reescrever os trechos deficientes;
- [ ] resolver e corrigir o super simulado;
- [ ] programar e executar as revisões D7 e D21.

Quando todos esses itens tiverem evidência registrada, o aceite operacional deverá ser calculado e o status poderá mudar para `Concluída` se permanecer sem falha eliminatória.
