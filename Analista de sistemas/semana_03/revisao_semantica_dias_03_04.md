# Revisão semântica dos Dias 3 e 4

## Escopo e método

Esta auditoria é somente leitura sobre o banco original. Foram confrontados, individualmente:

- 100 questões principais e 40 extras;
- 100 comentários principais e 40 comentários de extras;
- enunciado, quatro alternativas, gabarito, análise A–D, conceito, pegadinha e referência;
- teoria anterior dos Dias 3 e 4 em `partes/estudo_dias_03_04.md`.

Não houve edição em `partes/questoes_dias_03_04.md`.

A verificação estrutural encontrou 140 itens, 140 comentários, 140 alternativas de cada letra A–D e 23 fragmentos de referência existentes na teoria. A distribuição declarada é 72 itens de nível Médio, 58 de nível Difícil e 10 de nível Muito difícil.

As contagens abaixo são independentes: o mesmo item pode aparecer em mais de uma categoria.

| Categoria | Ocorrências | Prioridade |
|---|---:|---|
| resposta incorreta ou redação/comentário inconsistente | 3 | bloqueadora |
| teoria anterior insuficiente | 3 | alta |
| nível inflado | 19 | média |
| distrator fraco | 11 | média |
| referência imprecisa | 17 | alta |
| dependência de produto/ferramenta mal delimitada | 2 | alta |
| **itens únicos com ao menos um achado** | **49** | — |
| itens sem achado nos critérios auditados | 91 | — |

## Achados bloqueadores

| ID | Diagnóstico concreto | Correção recomendada |
|---|---|---|
| `S3D4Q162` | O gabarito marca **D**, mas D afirma que `DECLARE` transforma o bloco em trigger e é falsa. A própria justificativa de D — “declaração de variável não cria evento automático” — demonstra sua falsidade. A alternativa semanticamente correta é **B**: `@uf` é variável local, `TOP (10)` limita a saída e a seleção pretendida depende de ordenação. | Trocar gabarito para B e permutar/sincronizar as linhas B e D do comentário e da tabela. |
| `Extra 4.20` | D continua sendo a única opção defensável, mas o comentário diz que ela “usa `à sociedade`”; essa expressão aparece em A, não em D. Além disso, D satisfaz o filtro de crase apenas de modo vazio, pois não contém crase. | Preferencialmente reescrever D para “Relatórios claros permitem **à sociedade** exercer controle social; a conclusão retoma transparência e fiscalização, sem eixo novo” e manter D. Alternativamente, corrigir o comentário e tornar explícito no enunciado que a ausência de crase indevida também atende ao filtro. |
| `S3D4Q187` | O enunciado pergunta “quais **duas** verificações”, mas B reúne validação do parâmetro/linha afetada, transação e tratamento de erro — três dimensões. Não há segundo gabarito plausível, porém a contagem anunciada não coincide com a alternativa. | Trocar “quais duas verificações” por “quais cuidados” ou enumerar claramente três verificações. |

## Teoria anterior insuficiente

| ID | Lacuna | Ajuste sugerido |
|---|---|---|
| `S3D3Q131` | A teoria explica `WHERE` e projeção, mas não apresenta explicitamente o termo relacional **seleção** nem o contraste nominal seleção × projeção cobrado pelo item. | Acrescentar uma definição curta antes da questão ou reescrever o item usando “filtragem de linhas”. |
| `S3D4Q194` | A teoria informa que `GO` separa lotes no cliente, mas não ensina expressamente que a variável local termina no limite do lote. | Incluir escopo de variável por lote e nomear uma ferramenta que interprete `GO`. |
| `S3D4Q198` | O terceiro filtro — “outros caminhos de inferência/acesso” — vai além do que a seção de views explica. A teoria cobre projeção e acesso direto à tabela, mas não desenvolve inferência. | Ensinar o conceito com exemplo e fonte ou retirar “inferência” do enunciado. |

## Níveis inflados

O critério usado foi: item classificado como Difícil, mas solucionável por lembrança direta de uma única regra, associação nominal ou operação elementar, sem encadeamento relevante de filtros. Os dez itens Muito difíceis possuem, em geral, três ou mais filtros reais e não foram rebaixados nesta auditoria.

| Grupo | IDs | Motivo |
|---|---|---|
| SQL: resultado ou regra de uma etapa | `S3D3Q108`, `S3D3Q116`, `S3D3Q121`, `S3D3Q122`, `S3D3Q123`, `S3D3Q124`, `S3D3Q131`, `S3D3Q140` | Contagem direta, definição de agregado, operações elementares de conjunto ou definição nominal. |
| RLM/argumentação: aplicação literal da regra | `Extras 3.11`, `3.12` e `3.17` | Negação já fornecida na teoria ou reconhecimento direto de que correlação não prova causalidade. |
| Objetos SQL/T-SQL: definição ou associação direta | `S3D4Q163`, `S3D4Q165`, `S3D4Q171`, `S3D4Q172`, `S3D4Q180`, `S3D4Q181`, `S3D4Q182`, `S3D4Q192` | Definição de `GO`, view, trigger, pseudo-tabelas, nome de constraint, `DEFAULT/CHECK` ou classe de comando. |

**Recomendação:** reclassificar esses 19 itens como Médio ou aumentar a complexidade do enunciado e dos distratores. Não basta manter o rótulo Difícil por causa do vocabulário técnico.

## Distratores fracos

O achado foi marcado quando dois ou mais distratores são manifestamente absurdos, alheios ao objeto ou absolutos demais, fazendo a correta — muitas vezes quase literal à teoria — sobressair sem domínio real.

| IDs | Evidência |
|---|---|
| `Extras 3.1, 3.3, 3.4, 3.5, 3.6 e 3.7` | Várias erradas atribuem a regimento, autonomia ou conselho regional efeitos juridicamente extremos, como revogar lei, romper todo o sistema ou converter a natureza institucional. |
| `Extra 3.8` | Três sequências usam “alternativa mais longa”, “preferência pessoal” ou “tamanho do órgão”, pistas caricatas que não competem com o método correto. |
| `S3D4Q180` | Os distratores afirmam que nomear constraint cria índice universal, permite violação ou desativa validação em lotes; nenhum é uma confusão próxima do benefício real de manutenção. |
| `Extras 4.1, 4.2 e 4.8` | As erradas são formulações extremas — competência opcional, favorecimento pessoal ou revogação total de uma lei pela outra — e reduzem a discriminação. |

**Recomendação:** substituir absolutos caricatos por erros próximos: competência parcialmente deslocada, conflito aparente de princípios, alcance subjetivo incorreto, exceção aplicada fora de hipótese ou efeito válido atribuído à fonte errada.

## Referências imprecisas

Todos os fragmentos existem; o problema é de precisão pedagógica, não de link quebrado.

| IDs | Problema | Referência adicional sugerida |
|---|---|---|
| `S3D3Q108` | O link aponta apenas para os dados, embora a solução também dependa da semântica de `COUNT(*)` e `WHERE`. | `#s3-d3-agregacao` e, se mantido, `#s3-d3-esquema-treino`. |
| `S3D3Q109`, `S3D3Q110`, `S3D3Q114`, `S3D3Q117`, `S3D3Q118`, `S3D3Q128`, `S3D3Q130`, `S3D3Q137`, `S3D3Q139`, `S3D3Q141`, `S3D3Q148`, `S3D3Q149` e `S3D3Q150` | A resposta nominal ou numérica depende dos registros do esquema de treino, mas o item aponta somente para o conceito de join, agregado, subconsulta, conjunto ou prática. | Acrescentar `#s3-d3-esquema-treino`, preservando também a âncora conceitual atual. |
| `S3D4Q187` | O comentário exige validação do alcance/linha afetada além de parâmetro, transação e erro, mas aponta somente para procedures. | Acrescentar `#s3-d4-dml`. |
| `S3D4Q193` | A solução combina evolução estrutural com `FOREIGN KEY` e `NOT NULL`. | Acrescentar `#s3-d4-ddl-restricoes` à âncora de evolução. |
| `S3D4Q198` | A referência de views sustenta projeção e privilégio direto, mas não o filtro de inferência. | Criar âncora teórica específica para caminhos alternativos/inferência ou remover esse filtro. |

## Dependência de produto ou ferramenta

| ID | Risco | Delimitação recomendada |
|---|---|---|
| `S3D4Q164` | “`LIMIT` é construção do PostgreSQL” pode soar como exclusividade, embora outros produtos também adotem `LIMIT` e o padrão possua `FETCH`. | Escrever “`LIMIT` é aceito no dialeto do PostgreSQL; `TOP` é T-SQL; portabilidade deve ser verificada”. |
| `S3D4Q194` | `GO` não é enviado ao mecanismo; seu reconhecimento e a formação do lote dependem da ferramenta cliente. “Ecossistema SQL Server” é amplo demais para afirmar o comportamento sem nomear o processador de script. | Fixar SSMS/sqlcmd ou dizer “em ferramenta que reconheça `GO`”; então explicar que a variável local não atravessa o lote. |

As questões explicitamente delimitadas ao SQL Server — por exemplo, `S3D4Q172`, `S3D4Q173`, `S3D4Q188`, `S3D4Q190` e `S3D4Q197` — não foram marcadas, pois o produto está claro e a teoria correspondente dá suporte.

## Ordem de correção recomendada

1. Corrigir `S3D4Q162`, pois hoje o material ensina uma alternativa falsa como correta.
2. Corrigir `Extra 4.20` e `S3D4Q187` para eliminar contradição entre enunciado, alternativa e comentário.
3. Completar a teoria de `S3D3Q131`, `S3D4Q194` e `S3D4Q198`.
4. Tornar as 17 referências compostas e precisas.
5. Recalibrar os 19 níveis e fortalecer os 11 conjuntos de distratores.
6. Reexecutar a auditoria de gabarito/comentário e uma leitura cega antes de liberar o lote.

## Conclusão

Dos 140 itens, 91 não apresentaram achado nos seis critérios auditados. Há um erro de gabarito inequívoco, duas inconsistências relevantes e 46 outros itens únicos com achados pedagógicos ou de precisão. O banco pode ser aproveitado, mas não deve ser considerado congelado antes das três correções bloqueadoras.

## Fechamento dos achados

Após a fase de auditoria somente leitura registrada acima, foi executada a remediação nos arquivos-fonte `partes/estudo_dias_03_04.md` e `partes/questoes_dias_03_04.md`. Os arquivos consolidados não foram alterados nesta etapa.

| Categoria auditada | Achados iniciais | Pendências após correção |
|---|---:|---:|
| resposta incorreta ou redação/comentário inconsistente | 3 | 0 |
| teoria anterior insuficiente | 3 | 0 |
| nível inflado | 19 | 0 |
| distrator fraco | 11 | 0 |
| referência imprecisa | 17 | 0 |
| dependência de produto/ferramenta mal delimitada | 2 | 0 |
| **itens únicos com ao menos um achado pendente** | **49** | **0** |

As três correções bloqueadoras foram concluídas: `S3D4Q162` passou a ter B como resposta correta, com alternativa, comentário e tabela sincronizados; `Extra 4.20` passou a conter o emprego efetivo de `à sociedade`; e `S3D4Q187` deixou de anunciar uma quantidade incompatível de verificações.

As três lacunas teóricas receberam explicação e âncora específica: seleção × projeção em `#s3-d3-selecao-projecao`, escopo por lote reconhecido pelo SSMS/`sqlcmd` em `#s3-d4-go-lotes-escopo` e caminhos alternativos de acesso/inferência em `#s3-d4-views-seguranca`. As 17 referências imprecisas foram tornadas compostas ou direcionadas à nova âncora pertinente, sem fragmentos ausentes.

Os 19 itens indicados foram reclassificados de Difícil para Médio. Os 11 conjuntos de distratores foram reescritos com erros próximos e plausíveis, preservando o conteúdo cobrado. `S3D4Q164` agora informa que `LIMIT` é aceito pelo PostgreSQL sem lhe atribuir exclusividade, e `S3D4Q194` fixa expressamente o contexto de SSMS/`sqlcmd`.

Para manter o balanceamento após a correção substantiva de `S3D4Q162`, as posições das alternativas foram permutadas, sem mudança da resposta semântica, em `Extra 3.4`, `S3D4Q194` e `Extra 4.2`; comentário e gabarito foram atualizados em conjunto.

### Métricas finais da revalidação

| Verificação | Resultado |
|---|---|
| questões e comentários | 140 questões e 140 comentários, com IDs preservados |
| alternativas | 560 alternativas; exatamente A–D em cada item; nenhuma alternativa E |
| gabaritos | 140 respostas de comentário e 140 células de tabela, sem divergência |
| níveis | 91 Médio, 39 Difícil e 10 Muito difícil; metadados espelhados nos comentários |
| letras globais | A = 35, B = 35, C = 35 e D = 35 |
| letras por nível | Médio: A 23, B 23, C 23, D 22; Difícil: A 10, B 9, C 10, D 10; Muito difícil: A 2, B 3, C 2, D 3 |
| padrão de respostas | nenhuma trinca da mesma letra e nenhum motivo de 2 a 4 letras repetido três vezes consecutivas |
| comprimento das alternativas | 6 sinais pela regra canônica; todos possuem justificativa específica, sem exceção não documentada |
| referências | metadados de questão/comentário idênticos e nenhum fragmento inexistente na teoria |
| análises A–D | 560 análises presentes e coerentes com o gabarito, inclusive nos cinco comandos negativos |
| resíduos editoriais | nenhum `TODO`, `TBD`, placeholder, “a definir”, “preencher” ou texto de preenchimento |

Com isso, os 49 itens inicialmente afetados foram saneados e o banco dos Dias 3–4 encerra a revisão sem pendência nos seis critérios auditados.

### Nota de integração global

O balanceamento posterior dos 420 itens permutou a posição de uma alternativa de nível Muito difícil neste lote, sem alterar a resposta semântica. Questão, comentário e tabela foram movidos em conjunto. A distribuição local passou a Médio A=23, B=23, C=23, D=22; Difícil A=10, B=9, C=10, D=10; Muito difícil A=2, B=2, C=2, D=4. O aceite usa o equilíbrio **global por nível**, que ficou com diferença máxima de uma letra; esta nota substitui apenas a métrica local de letras, não a auditoria de conteúdo.
