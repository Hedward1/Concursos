# Revisão semântica cruzada — Semana 4, Dias 3 e 4

**Data da auditoria:** 19/07/2026
**Escopo exclusivo:** teoria dos Dias 3 e 4; 100 questões principais (`S4D3Q101–S4D3Q150` e `S4D4Q151–S4D4Q200`); 40 extras (`Extra Dia 3.1–3.20` e `Extra Dia 4.1–4.20`); tabelas de gabarito e comentários correspondentes.
**Fontes auditadas:** [`partes/estudo_dias_03_04.md`](partes/estudo_dias_03_04.md) e [`partes/questoes_dias_03_04.md`](partes/questoes_dias_03_04.md).
**Fora do escopo e preservado:** Dias 1–2, Dias 5–6, super simulado, jornada, dissertações e arquivos consolidados.

## Resultado executivo

Foi feita leitura individual dos 140 enunciados, das 560 alternativas e das 560 análises A–D. Cada resposta foi confrontada com teoria anterior, tabela e comentário. Depois da remediação, os dois dias têm resposta única, cobertura suficiente, comentários coerentes e nenhum bloqueio semântico.

| Verificação | Resultado final |
|---|---:|
| Questões lidas e resolvidas | 140/140 |
| Principais | 100/100 |
| Extras | 40/40 |
| Alternativas A–D completas | 560/560 |
| Comentários com análise A–D | 560/560 |
| Gabaritos únicos e semanticamente corretos | 140/140 |
| Células das tabelas de gabarito conferidas | 140/140 |
| Divergências item × tabela × comentário | 0 |
| Referências de item e comentário com âncora existente | 280/280 |
| Metadados divergentes entre item e comentário | 0 |
| Usos fora da faixa pedagógica prevista | 0 |
| Comandos negativos sem observação explícita | 0/8 |
| Alternativas E | 0 |
| Opções literais duplicadas | 0 |
| Padrões proibidos de gabarito | 0 |
| Alertas finais de extensão pelo padrão semanal | 0 |
| Alertas finais pela heurística auxiliar mais estrita | 0 |
| Gabaritos alterados pela auditoria | 0 |
| Critérios eliminatórios remanescentes | 0 |

**Status do recorte:** aprovado e congelado para consolidação.

## Método e bases confrontadas

A auditoria cruzou, para cada ID:

1. suficiência do enunciado e existência de uma única melhor resposta;
2. plausibilidade, paralelismo e proximidade semântica das quatro alternativas;
3. resposta resolvida × tabela × comentário;
4. explicação individual de A, B, C e D;
5. dificuldade substantiva, sem usar a matriz inicial como cota;
6. teoria anterior e suficiente na âncora indicada;
7. comandos negativos, absolutos, escopo e possíveis pistas de redação;
8. aderência qualitativa ao perfil documentado do Instituto Consulplan;
9. dependência de versão, literalidade normativa e atualidade da fonte;
10. distribuição e padrões curtos do gabarito.

Além do edital e das bases internas do projeto, foram reconferidas fontes primárias:

- Lei nº 4.769/1965 no Planalto: https://www.planalto.gov.br/ccivil_03/leis/l4769.htm;
- Decreto nº 61.934/1967 no Senado e na Câmara: https://legis.senado.leg.br/norma/484558 e https://www2.camara.leg.br/legin/fed/decret/1960-1969/decreto-61934-22-dezembro-1967-403171-norma-pe.html;
- UML 2.5.1 no catálogo oficial da OMG: https://www.omg.org/spec/UML/2.5.1/About-UML e https://www.omg.org/spec/.

A conferência confirmou a base legal do Sistema CFA/CRAs usada no recorte e a UML 2.5.1 como especificação formal publicada pela OMG. Os itens de Java/JVM, artefatos, implantação e processo foram mantidos independentes de produto. A teoria também evita atribuir o conteúdo do edital a uma edição específica do PMBOK quando a versão não é necessária para resolver a questão.

## Diagnóstico inicial

O banco já continha 50 principais e 20 extras em cada dia, sempre com A–D e comentário completo. Não havia gabarito errado, resposta dupla, alternativa E ou âncora inexistente. Os problemas reais estavam em quatro frentes:

- uma lacuna curta de teoria para a fatia incremental vertical cobrada por `S4D4Q175`;
- um comando sem base explícita em `Extra Dia 3.18`;
- referências estreitas ou imprecisas em `Extra Dia 3.20` e `S4D4Q196`;
- grande quantidade de alternativas com assimetria de extensão, especificidade exclusiva, absoluto caricatural ou distrator alheio ao domínio.

A declaração de produção registrava 107 alertas de extensão. Uma varredura independente sobre as 140 questões, aplicando literalmente a regra semanal à alternativa completa, encontrou **109**. A diferença de dois é de contagem/implementação, não de julgamento semântico. Os 109 casos foram relidos individualmente; nenhum foi “corrigido” por mero enchimento textual.

A distribuição inicial de dificuldade era 56 Médias, 56 Difíceis e 28 Muito difíceis. Ela inflava itens de recuperação direta. Sessenta e um rótulos foram recalibrados após resolver cada questão e contar os filtros cognitivos efetivamente necessários.

## Correções de conteúdo e comando

| ID ou trecho | Correção aplicada | Gabarito |
|---|---|:---:|
| Teoria do Dia 4 / `s4-d4-modelos` | explicitou que uma fatia incremental vertical atravessa as camadas técnicas necessárias e termina em capacidade verificável; camada isolada não garante incremento utilizável | — |
| `S4D4Q175` | passou a ter base teórica anterior e suficiente para distinguir fatia vertical de trabalho exclusivamente por camada | A, mantido |
| `Extra Dia 3.18` | o enunciado agora informa as três ações originais — versionar o modelo, revisar o código e registrar o teste — antes de pedir reescrita paralela | B, mantido |
| `Extra Dia 3.20` | item, comentário e referência passaram a cobrir conjuntamente Português, artefatos e implantação | C, mantido |
| `S4D4Q196` | referência corrigida para qualidade, pessoas e comunicação, exatamente o núcleo cobrado | B, mantido |
| `S4D3Q120` | alternativas paralelas e comentários A–D explicativos; removida pista auxiliar em comando negativo sobre porta/interface | A, mantido |
| `S4D4Q188` | alternativas passaram a comparar finalidades de fase com extensão equivalente; comentário de D explicita ênfase versus exclusividade | D, mantido |
| `Extra Dia 4.18` | quatro resultados de exposição de risco agora são alternativas completas e comparáveis; comentários mostram os dois cálculos | B, mantido |

Também foi corrigida a forma gráfica inadequada “Chamár-lo” em `S4D4Q160`.

## Remediação das alternativas

Os 109 sinais objetivos iniciais foram revisados nos seguintes conjuntos:

- **Dia 3, principais (35):** Q102, Q104–Q109, Q111–Q112, Q115, Q119, Q121–Q126, Q128, Q130, Q133–Q137, Q139–Q142, Q144–Q150;
- **Dia 3, extras (17):** 3.1–3.11, 3.13, 3.16–3.20;
- **Dia 4, principais (48):** Q151–Q157, Q159–Q187, Q189–Q200;
- **Dia 4, extras (9):** 4.1–4.3, 4.5, 4.7, 4.9–4.10, 4.13 e 4.20.

Além deles, seis conjuntos sem alerta numérico foram fortalecidos porque ainda traziam contraste fácil ou distrator pouco competitivo: `S4D3Q113`, `S4D3Q129`, `S4D3Q143`, `Extra Dia 3.15`, `Extra Dia 4.4` e `Extra Dia 4.8`.

As mudanças encurtaram respostas excessivamente explicativas, substituíram caricaturas por erros parciais plausíveis e sincronizaram a análise A–D. Não foram adicionadas palavras vazias apenas para igualar tamanhos. Na varredura final, tanto a regra semanal por caracteres quanto a heurística auxiliar por palavras retornaram zero alerta.

## Calibração de dificuldade

### Distribuição final

| Dia e banco | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Dia 3 — principais | 35 | 12 | 3 | 50 |
| Dia 3 — extras | 17 | 2 | 1 | 20 |
| **Dia 3** | **52** | **14** | **4** | **70** |
| Dia 4 — principais | 33 | 14 | 3 | 50 |
| Dia 4 — extras | 16 | 4 | 0 | 20 |
| **Dia 4** | **49** | **18** | **3** | **70** |
| **Total** | **101** | **32** | **7** | **140** |

A matriz 20/20/10 nas principais e 8/8/4 nas extras foi tratada como referência de produção, não como cota de aceite. Recuperação conceitual, leitura direta de notação e cálculo de uma etapa permanecem Médios. Itens Difíceis exigem normalmente dois filtros articulados; os sete Muito difíceis mantidos exigem integração de três ou mais decisões, análise de cadeia completa ou preservação simultânea de vários critérios.

## Uso pedagógico e gabaritos

### Uso

| Banco combinado | Essenciais | Aprofundamento | Revisão | Simulado | Total |
|---|---:|---:|---:|---:|---:|
| Principais | 20 | 40 | 20 | 20 | 100 |
| Extras | 10 | 10 | 10 | 10 | 40 |
| **Total** | **30** | **50** | **30** | **30** | **140** |

### Gabaritos

| Dia e banco | A | B | C | D | Total |
|---|---:|---:|---:|---:|---:|
| Dia 3 — principais | 12 | 13 | 12 | 13 | 50 |
| Dia 3 — extras | 5 | 5 | 5 | 5 | 20 |
| **Dia 3** | **17** | **18** | **17** | **18** | **70** |
| Dia 4 — principais | 12 | 13 | 12 | 13 | 50 |
| Dia 4 — extras | 5 | 5 | 5 | 5 | 20 |
| **Dia 4** | **17** | **18** | **17** | **18** | **70** |
| **Total** | **34** | **36** | **34** | **36** | **140** |

Nenhum gabarito precisou ser alterado. Não há três letras iguais consecutivas nem motivo de duas a quatro letras repetido três vezes. Eventual permutação global por nível pertence à integração mecânica da semana e não muda a validade semântica deste recorte.

## Aderência ao perfil Consulplan

O recorte mantém questões autorais, sem apresentar item como reprodução de prova oficial. A calibração conservou traços documentados no projeto: comandos diretos ou negativos claramente visíveis, casos curtos, cobrança de distinções próximas, alternativas no mesmo domínio e comentário que explica por que cada opção funciona ou falha.

Foram removidos sinais que facilitavam acertar sem dominar o conteúdo — resposta muito mais longa, única alternativa específica, absolutos gratuitos e opções manifestamente alheias. Ao mesmo tempo, não se inventaram percentuais estatísticos sobre a banca nem literalidade legal sem fonte oficial.

## Revalidação final

- 140 IDs de questão e 140 IDs de comentário: completos e correspondentes;
- 560 alternativas e 560 análises: A–D, sem E e sem duplicidade literal;
- 140 gabaritos das tabelas: idênticos aos comentários;
- 280 metadados de referência: sincronizados e com âncoras existentes;
- níveis e usos: idênticos entre item e comentário;
- polaridade dos comentários em comandos positivos e negativos: correta;
- oito comandos negativos: todos com gabarito e observação explícita;
- regra semanal de extensão fora da faixa 0,70–1,30: zero alerta;
- heurística auxiliar de correta destacada por palavras: zero alerta;
- placeholders e marcações provisórias: zero;
- gabarito duplo, conteúdo futuro indispensável ou literalidade normativa inventada: zero.

## Risco residual

Não há risco semântico bloqueante. Resta apenas o risco temporal normal de fontes externas: normas do Sistema CFA/CRAs e catálogos técnicos devem ser reconferidos antes de futuras cobranças de artigo, prazo, sanção ou versão específica. A distribuição global por letra e nível poderá ser ajustada pelo integrador sem mudar conteúdo, desde que alternativa, tabela e comentário sejam permutados juntos.

## Apêndice de integração global

Na auditoria operacional posterior, o item 16.3 do edital exigiu explicitação das fases de projeto. A teoria do Dia 4 recebeu o mapa `iniciação → planejamento → execução → acompanhamento e controle → encerramento`, a distinção em relação às fases de processo/RUP e a definição do PMBOK sem edição presumida. Para transformar essa cobertura também em decisão objetiva, `S4D4Q191` foi reescrita e resolvida novamente: permaneceu **Difícil**, com resposta semântica **B**, quatro alternativas plausíveis e comentário A–D sincronizado.

Depois de todos os lotes semânticos, o integrador permutou 14 posições A–D no banco completo para equilibrar letras dentro de cada nível. Alternativa, comentário e tabela foram movidos atomicamente; conteúdo, nível e resposta semântica não mudaram. Assim, as tabelas de letras acima documentam o estado da resolução cega anterior à permutação, e o banco consolidado registra as posições finais. A auditoria mecânica pós-integração confirmou equilíbrio por nível e ausência de trinca ou motivo curto proibido.

Uma última heurística bruta apontou `Extra Dia 3.19` pela extensão da correta. O item foi novamente resolvido, e apenas a redação da alternativa correta e sua análise foram condensadas de 16 para 15 palavras. Enunciado, distratores, gabarito A, nível, uso, referência e tabela foram preservados; o alerta caiu a zero.

**Status final:** Dias 3 e 4 aprovados e congelados para consolidação.
