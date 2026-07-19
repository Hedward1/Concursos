# Revisão semântica independente — Super Simulado da Semana 3

## Escopo e método cego

Esta revisão auditou exclusivamente `semana_03_super_simulado.md`. O simulado não foi editado.

A execução ocorreu em duas passagens separadas:

1. foram lidos somente os 60 enunciados e suas alternativas, com interrupção antes de `## Gabarito`;
2. o gabarito independente foi então confrontado com a tabela oficial, os 60 comentários, níveis, distratores, delimitação de produto/dialeto e referências.

Para o único ponto dependente de produto, a verificação foi confirmada nas fontes primárias [Microsoft Learn — triggers DML multirregistro](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/create-dml-triggers-to-handle-multiple-rows-of-data?view=sql-server-ver17) e [MySQL 8.4 — Using Triggers](https://dev.mysql.com/doc/refman/8.4/en/triggers.html).

## Resultado da resolução independente

| Dia | Intervalo | Respostas obtidas sem consultar o gabarito | Concordância oficial |
|---:|---|---|---:|
| 1 | `S3S001–S3S010` | B, D, A, C, C, A, D, B, A, B | 10/10 |
| 2 | `S3S011–S3S020` | C, A, D, B, B, D, C, A, C, D | 10/10 |
| 3 | `S3S021–S3S030` | A, C, B, D, D, B, A, C, A, C | 10/10 |
| 4 | `S3S031–S3S040` | D, B, C, A, A, C, B, D, B, D | 10/10 |
| 5 | `S3S041–S3S050` | B, A, D, C, C, D, A, B, A, D | 10/10 |
| 6 | `S3S051–S3S060` | C, D, B, A, B, A, D, C, B, C | 10/10 |
| **Total** | `S3S001–S3S060` | — | **60/60** |

Não foi encontrada resposta oficial incorreta no contexto SQL Server sustentado pela referência, dupla resposta defensável, comentário que invertesse o mérito de uma alternativa ou divergência entre a tabela e o campo `Alternativa correta`.

## Métricas objetivas

| Verificação | Resultado |
|---|---|
| questões e comentários | 60 questões e 60 comentários |
| alternativas | 240 alternativas; exatamente A–D em cada questão |
| gabarito | 60 células, todas idênticas ao comentário e à resolução cega |
| distribuição global | A = 15, B = 15, C = 15 e D = 15 |
| níveis declarados | 24 Médio, 33 Difícil e 3 Muito difícil |
| equilíbrio por nível | Médio: 6 de cada letra; Difícil: A 8, B 9, C 8, D 8; Muito difícil: A 1, B 0, C 1, D 1 |
| metadados espelhados | 60/60 níveis e 60/60 referências idênticos entre questão e comentário |
| análises A–D | 240/240 presentes e coerentes com o gabarito |
| referências | 45 fragmentos distintos usados; nenhum fragmento ausente na apostila |
| padrões de resposta | nenhuma trinca da mesma letra e nenhum motivo de 2 a 4 letras repetido três vezes consecutivas |
| comprimento | nenhum sinal pela regra canônica de 70%–130% |

## Divergência de produto/dialeto

### `S3S036` — Trigger multirregistro

**Prioridade:** alta.

O gabarito C e seu comentário estão corretos **para SQL Server**: nesse produto, `inserted` e `deleted` são conjuntos lógicos e uma única instrução pode alimentar uma única execução da trigger com muitas linhas. O enunciado, porém, diz apenas “uma trigger” e não fixa o produto.

Essa omissão é material porque a semântica não é universal. No MySQL 8.4, por exemplo, triggers são `FOR EACH ROW` e usam `OLD`/`NEW`, não os conjuntos `inserted`/`deleted`. A própria teoria referenciada distingue os dois modelos, mas a referência não substitui a delimitação no enunciado de uma questão autônoma.

**Correção recomendada:** iniciar o caso com “No SQL Server, uma única instrução atualiza 200 linhas...” e, no comentário, manter explicitamente o mesmo produto. A resposta permanece C.

Não foi encontrada outra dependência de produto capaz de mudar o mérito. `S3S035` separa corretamente `GO` da linguagem enviada ao mecanismo, e `S3S052` já manda adaptar literal, limites e tipos ao dialeto.

## Recalibração de nível

O critério independente foi cognitivo: **Médio** para lembrança ou aplicação direta de uma regra; **Difícil** para encadeamento de ao menos dois filtros relevantes ou nuance não resolvida por associação nominal; **Muito difícil** para três ou mais restrições interdependentes.

Dezenove itens classificados como Difícil são resolvidos por uma definição, contraste direto, regra única ou cálculo elementar e devem ser reclassificados como Médio:

| Grupo | IDs | Motivo concreto |
|---|---|---|
| arquitetura e metadados | `S3S006`, `S3S007`, `S3S008` | identificação direta de catálogo, sistema de banco de dados e independência lógica |
| normalização | `S3S015`, `S3S016`, `S3S017`, `S3S018` | aplicação literal de 2FN/3FN ou lembrança nominal das propriedades de decomposição e BCNF |
| SQL ANSI | `S3S025`, `S3S026`, `S3S027` | uma única regra sobre `NULL`, posição do filtro em outer join ou duplicatas no `UNION` |
| T-SQL, DML e acesso | `S3S035`, `S3S037`, `S3S038` | reconhecimento direto de `GO`, prévia com o mesmo predicado e limite de segurança de view |
| concorrência e transações distribuídas | `S3S045`, `S3S047`, `S3S048` | associação direta de deadlock, limites do MVCC e estado preparado do 2PC |
| índices e BI | `S3S056`, `S3S057`, `S3S058` | regra direta de custo do índice, expansão conceitual de ETL/ELT e média ponderada de uma etapa |

Os três itens Muito difíceis permanecem defensáveis: `S3S020` integra dependência parcial, transitiva e preservação dos vínculos; `S3S029` combina preservação de ausência, filtro em `ON`, `COUNT(coluna)` e `HAVING`; `S3S030` combina grão, agregação, paginação e desempate único.

Se as 19 reclassificações forem adotadas sem alterar enunciados, a distribuição passará a 43 Médio, 14 Difícil e 3 Muito difícil.

## Distratores com baixa força discriminativa

Não há distrator que crie segunda resposta correta. Cinco conjuntos, contudo, deixam a correta sobressair porque ao menos duas erradas são extremas ou se afastam do mecanismo cobrado:

| ID | Diagnóstico |
|---|---|
| `S3S017` | Índices, eliminação automática de junções e ordem física desviam do par conceitual “sem perda × preservação de dependências”. |
| `S3S045` | As erradas combinam o nome de outra anomalia com medidas manifestamente inadequadas; somente o par deadlock/ordem de locks forma uma solução tecnicamente coerente. |
| `S3S056` | “Remover todos os índices” e substituir índice por `ORDER BY` são extremos; apenas B funciona como erro próximo do trade-off real. |
| `S3S057` | B e C inventam proibições incompatíveis com as próprias siglas; D praticamente apenas expande a ordem de ETL/ELT. |
| `S3S058` | Somar médias ou descartar o grupo menor são pouco plausíveis; somente a média simples de médias funciona como distrator competitivo. |

**Recomendação:** preservar o gabarito e substituir as opções fracas por erros próximos: confundir preservação com dependência verificável após junção, prevenção com detecção de deadlock, benefício local com custo total, local predominante de transformação e escolha incorreta do denominador.

## Referências e comentários

As 60 referências apontam para conteúdo semanticamente pertinente. Foram encontrados 45 fragmentos distintos, todos existentes em `semana_03_estudo.md`; não há referência quebrada nem diferença entre questão e comentário.

Os 60 comentários identificam corretamente a alternativa, justificam A–D e apresentam conceito, pegadinha e estratégia de resolução compatíveis. Não foi detectada justificativa que sustentasse o oposto do gabarito.

## Conclusão

O super simulado está **correto quanto às 60 respostas e aos 60 comentários**, mas ainda não está semanticamente limpo em todos os critérios solicitados. Permanecem:

- 1 delimitação de produto de prioridade alta (`S3S036`);
- 19 níveis inflados;
- 5 conjuntos de distratores com baixa discriminação, todos sobrepostos aos 19 itens de nível.

São 25 ocorrências em 20 IDs únicos. Não há necessidade de trocar qualquer gabarito; as correções propostas limitam-se ao escopo de produto, à calibração pedagógica e à qualidade dos distratores.

## Fechamento dos achados

Após a auditoria independente acima, todos os achados foram implementados diretamente em `semana_03_super_simulado.md`. Esta seção registra a situação posterior e substitui, como estado atual, as pendências descritas na conclusão original da auditoria.

| Categoria | Achados independentes | Pendências finais |
|---|---:|---:|
| delimitação de produto/dialeto | 1 | 0 |
| níveis inflados | 19 | 0 |
| conjuntos de distratores com baixa discriminação | 5 | 0 |
| **IDs únicos afetados** | **20** | **0** |

`S3S036` agora fixa SQL Server no enunciado, na justificativa da alternativa C, no conceito e na estratégia de resolução. Assim, `inserted`/`deleted` e a semântica multirregistro não são mais apresentados como regra universal de triggers.

Os 19 itens indicados foram reclassificados de Difícil para Médio tanto na questão quanto no comentário. O cabeçalho conserva a matriz inicial 24/24/12 e registra a distribuição efetiva final de **43 Médio, 14 Difícil e 3 Muito difícil**.

Os quatro distratores e as quatro análises A–D de `S3S017`, `S3S045`, `S3S056`, `S3S057` e `S3S058` foram reescritos. As novas erradas representam falhas próximas — garantia parcial de decomposição, detecção versus prevenção de deadlock, avaliação local versus custo total de índice, inversão do fluxo ETL/ELT e erro de ponderação/denominador — sem criar segunda resposta defensável.

### Métricas finais

| Verificação | Resultado pós-correção |
|---|---|
| questões, comentários e tabela | 60 questões, 60 comentários e 60 respostas de tabela |
| resolução independente | 60/60 soluções semânticas coincidentes; 54 letras permaneceram e seis foram remapeadas apenas por posição na integração final |
| alternativas e análises | 240 alternativas A–D e 240 análises sincronizadas |
| níveis | 43 Médio, 14 Difícil e 3 Muito difícil; 60/60 espelhados no comentário |
| letras globais | A = 15, B = 15, C = 15 e D = 15 |
| letras por nível | Médio: A 10, B 11, C 11, D 11; Difícil: A 4, B 3, C 3, D 4; Muito difícil: A 1, B 1, C 1, D 0 |
| referências | 45 fragmentos distintos; nenhum ausente e 60/60 metadados espelhados |
| comprimento | nenhum sinal pela regra canônica de 70%–130% |
| sequência | nenhuma trinca da mesma letra e nenhum motivo de 2 a 4 letras repetido três vezes consecutivas |
| escopo editorial | IDs, ordem, enunciados e respostas conceituais preservados; seis letras posicionais permutadas com suas análises e tabela |

O equilíbrio global e a ausência de sequências problemáticas foram preservados. Depois da reclassificação dos 19 IDs, a integração permutou seis posições A–D para equilibrar também cada nível, sempre movendo alternativa correta, análise e tabela em conjunto.

Com isso, as 25 ocorrências distribuídas pelos 20 IDs foram encerradas, sem pendência remanescente nos critérios da auditoria independente.

### Integração final das posições A–D

Depois do fechamento semântico, o integrador permutou apenas a posição A–D de seis respostas para equilibrar as letras dentro dos níveis: `S3S012` A→C, `S3S020` D→B, `S3S035` A→C, `S3S036` C→A, `S3S059` B→A e `S3S060` C→D. Em cada caso, a alternativa, sua análise e a linha da tabela foram movidas juntas; a resposta conceitual, o ID, o enunciado, o nível e a referência não mudaram.

As métricas definitivas substituem somente as duas linhas posicionais da tabela anterior: globalmente, A=15, B=15, C=15 e D=15; por nível, Médio = A 10, B 11, C 11, D 11; Difícil = A 4, B 3, C 3, D 4; Muito difícil = A 1, B 1, C 1, D 0. Não há diferença superior a uma ocorrência dentro de qualquer nível, trinca de letra igual ou divergência entre questão, comentário e tabela.
