# Revisão semântica — Semana 4, Dia 1

## Resultado

Auditoria concluída em **70/70 questões** do Dia 1: S4D1Q001–S4D1Q050 e Extras Dia 1.1–1.20, com leitura individual dos enunciados, das 280 alternativas e dos 70 comentários completos. Após as correções abaixo, não permanece bloqueio semântico, gabarito duplo, conteúdo sem teoria anterior ou referência quebrada.

O recorte do Dia 2 não foi editado nesta auditoria.

## Bases confrontadas

- edital local, página 28 de 43, item 13: análise e projeto orientado a objetos com UML e diagramas de casos de uso;
- OMG UML 2.5.1, especialmente §§ 18.1.3.2–18.1.3.3 e descrições de `Extend`/`Include` nas páginas 640–648: https://www.omg.org/spec/UML/2.5.1;
- ISO/IEC/IEEE 29148:2018, edição publicada e confirmada em 2024, ainda corrente na consulta de 19/07/2026, embora já marcada para revisão: https://www.iso.org/standard/72089.html;
- Lei nº 4.769/1965, Decreto nº 61.934/1967, RN CFA nº 651/2024 e RN CFA nº 671/2025, nas fontes oficiais já ligadas pela teoria;
- perfil interno do Instituto Consulplan e amostra oficial local da Câmara Municipal de Belo Horizonte de 2018, especialmente as questões 32, 35, 42 e 47 do cargo de Analista de TI, com gabarito pós-recursos. A comparação confirmou comandos diretos/negativos visíveis, enunciado suficiente e alternativas paralelas; o banco do projeto conserva aplicação e integração maiores sem atribuir percentuais inexistentes à banca.

## Diagnóstico e correções na teoria

1. A matriz de rastreabilidade atribuía Q001–Q014 a fundamentos e Q015–Q030 ao processo de requisitos; os intervalos corretos são Q001–Q010 e Q011–Q030.
2. Verificabilidade foi explicitada como obtenção de evidência objetiva por inspeção, análise, demonstração ou teste, sem reduzir todo requisito a teste executável.
3. A definição de partes interessadas passou a distinguir pessoas, grupos e organizações de normas, componentes e sistemas externos, que são fontes ou elementos do contexto; seus responsáveis podem ser partes interessadas.
4. `extend` foi alinhado à UML 2.5.1: um ou mais pontos de extensão, base significativa de modo independente e condição opcional; sem condição, a extensão é incondicional nos pontos especificados.
5. A revisão normativa passou a identificar expressamente a RN CFA nº 651/2024 para o Regimento do CRA-PR e a RN CFA nº 671/2025 para o Código de Ética, ambas vigentes na consulta oficial de 19/07/2026.
6. A tabela rápida, a mini revisão e o roteiro de questões foram sincronizados com essas correções; Q005, Q006 e Q010 deixaram de aparecer com núcleos trocados.

## Alterações por ID

| ID | Alteração aplicada | Gabarito |
|---|---|---:|
| S4D1Q003 | completou ambiente, carga, operação, estatística e limiar; equilibrou os distratores | D, mantido |
| S4D1Q007 | tornou explícitos o caminho autorizado com persistência e o bloqueio sem decisão | D, mantido |
| S4D1Q009 | retirou norma/sistema da categoria de parte interessada e aproximou os distratores | B, mantido |
| S4D1Q010 | substituiu “não há teste” por ausência de qualquer método de evidência objetiva | C, mantido |
| S4D1Q018 | restaurou paralelismo gramatical entre as alternativas | B, mantido |
| S4D1Q021 | trocou distratores artificiais por verificações formais plausíveis, preservando validação da necessidade | C, mantido |
| S4D1Q026 | delimitou o ponto de partida e colocou todos os distratores no domínio da rastreabilidade para a frente | A, mantido |
| S4D1Q030 | substituiu o comando subjetivo “decisão madura” por priorização multicritério justificável | C, mantido |
| S4D1Q037 | substituiu opções absurdas por candidatos/valores plausíveis do domínio | C, mantido |
| S4D1Q045 | tornou os três distratores parcialmente corretos, mas insuficientes em filtros distintos | D, mantido |
| S4D1Q047 | corrigiu a condição opcional de `extend`, comentário e nível de Médio para Difícil | C, mantido |
| S4D1Q050 | explicitou ponto de extensão e condição e trocou “sequência” por “combinação de relações” | A, mantido |
| Extra Dia 1.3 | aproximou os erros plausíveis sobre lei, decreto, hierarquia e posterioridade | A, mantido |
| Extra Dia 1.4 | tornou os distratores comparáveis por objeto normativo | B, mantido |
| Extra Dia 1.5 | fez cada distrator falhar em território, função ou hierarquia, sem caricatura | B, mantido |
| Extra Dia 1.7 | substituiu alternativa sem sentido por erros parciais de objeto, competência e vigência | B, mantido |
| Extra Dia 1.10 | cada distrator agora corrige dois filtros e falha no terceiro | A, mantido |
| Extra Dia 1.15 | preservou frases gramaticais e isolou erros de concessão, modalidade ou conclusão | C, mantido |
| Extra Dia 1.17 | corrigiu “alguns” para existência sem cardinalidade exata nem exclusão automática de “todos” | C, mantido |
| Extra Dia 1.19 | substituiu frases agramaticais por reescritas claras que alteram proprietário ou papéis | A, mantido |
| Extra Dia 1.20 | cada paráfrase incorreta passou a falhar em filtros linguísticos identificáveis | D, mantido |

Os outros 49 itens foram preservados após leitura individual porque mantinham resposta única, comentário coerente e cobertura anterior suficiente.

## Distribuição final

### Níveis

| Banco | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Principais | 32 | 11 | 7 | 50 |
| Extras | 12 | 4 | 4 | 20 |
| **Total** | **44** | **15** | **11** | **70** |

A matriz 20/20/10 e 8/8/4 é referência de produção, não cota de aceite. A distribuição final foi mantida fora dela para não inflar recuperação literal ou aplicação direta. Houve uma única recalibração: S4D1Q047 passou de Médio para Difícil porque exige avaliar direção, autonomia da base, ponto de extensão e a exceção normativa da condição opcional.

Principais difíceis: Q004, Q007, Q010, Q012, Q014, Q017, Q022, Q024, Q035, Q040 e Q047. Principais muito difíceis: Q005, Q015, Q020, Q025, Q030, Q045 e Q050. Extras difíceis: 1.2, 1.7, 1.9 e 1.19. Extras muito difíceis: 1.5, 1.10, 1.15 e 1.20. Os demais itens foram confirmados como Médios.

### Uso operacional

| Banco | Essenciais | Aprofundamento | Revisão | Simulado | Total |
|---|---:|---:|---:|---:|---:|
| Principais | 10 | 20 | 10 | 10 | 50 |
| Extras | 5 | 5 | 5 | 5 | 20 |
| **Total** | **15** | **25** | **15** | **15** | **70** |

### Gabaritos

| Banco | A | B | C | D | Total |
|---|---:|---:|---:|---:|---:|
| Principais | 12 | 11 | 13 | 14 | 50 |
| Extras | 6 | 6 | 5 | 3 | 20 |
| **Total** | **18** | **17** | **18** | **17** | **70** |

Não houve alteração de gabarito. Não há três letras iguais consecutivas nem motivo de 2–4 letras repetido três vezes em sequência, tanto nas principais quanto nas extras.

## Revalidação objetiva

- 50 principais + 20 extras: **70/70**;
- quatro alternativas por questão: **280/280**;
- comentários com análise A–D: **70/70**;
- conceito, pegadinha, como pensar e referência: **70/70**;
- nível, uso e referência idênticos entre item e comentário: **70/70**;
- referências das questões para âncoras existentes na teoria: **70/70**;
- comandos negativos destacados e com observação de correção: **10/10**;
- alertas de comprimento da alternativa correta fora da faixa 0,70–1,30: **0**;
- gabarito ambíguo, teoria posterior à cobrança ou literalidade normativa inventada: **0**.

## Risco residual

Não há risco semântico bloqueante. O único risco externo é temporal: resoluções e o status da ISO/IEC/IEEE 29148 podem mudar depois de 19/07/2026; por isso, futuras semanas que cobrem literalidade normativa devem reconferir as páginas oficiais antes de criar artigo, prazo, sanção ou regra nova.

**Status final:** Dia 1 aprovado e congelado para consolidação.
