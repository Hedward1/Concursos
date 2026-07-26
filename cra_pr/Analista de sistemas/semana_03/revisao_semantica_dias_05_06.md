# Revisão semântica — questões dos Dias 5 e 6

## Escopo e regra de trabalho

Arquivo auditado: `partes/questoes_dias_05_06.md`.

Foram lidos os **140 itens** e seus **140 comentários individualizados**:

- Dia 5: 50 questões principais e 20 extras;
- Dia 6: 50 questões principais e 20 extras;
- 560 alternativas e as 560 análises correspondentes.

O banco foi tratado como **congelado**: esta revisão não altera enunciado, alternativa, gabarito, comentário ou metadado. O objetivo é indicar, por ID, o que convém corrigir quando houver autorização para descongelá-lo.

Critérios semânticos usados:

1. existência de mais de uma alternativa defensável ou de gabarito tecnicamente incorreto;
2. suficiência da teoria apontada pela referência;
3. compatibilidade entre o raciocínio exigido e o nível declarado;
4. competitividade dos distratores;
5. precisão do link interno de teoria;
6. dependência de produto, versão, engine, configuração ou dialeto.

## Resultado executivo

| Verificação | Resultado |
|---|---:|
| Gabaritos incorretos | **0** |
| Itens com duas respostas defensáveis | **0** |
| Comentários que contradizem o gabarito | **0** |
| Formulações com ressalva técnica/teoria a completar | **3 IDs** |
| Referência interna a trocar | **1 ID** |
| Itens sensíveis a produto/configuração | **19 IDs** |
| Desses, itens que pedem delimitação adicional | **5 IDs** |
| Classificações “Muito difícil” claramente infladas | **8 IDs** |
| Itens com dois ou mais distratores pouco competitivos | **13 IDs** |

**Conclusão:** o banco está semanticamente utilizável e os gabaritos podem ser preservados. Antes da versão final, recomenda-se corrigir prioritariamente `S3D6Q257`, `S3D6Q258`, `S3D6Q264`, `S3D6Q280`, `S3D6Q293` e a referência de `S3D6Q270`. Os demais apontamentos melhoram calibração e qualidade de prova, mas não invalidam respostas.

## 1. Gabarito ambíguo ou incorreto

**Nenhum caso encontrado.**

As 140 respostas indicadas são únicas dentro das alternativas oferecidas, e as respectivas análises explicam corretamente por que a chave vence. Isso inclui os itens conceitualmente mais sensíveis:

- `S3D5Q203` distingue término do último comando de confirmação definitiva;
- `S3D5Q210` trata corretamente o resultado transacional desconhecido depois de perda de conexão;
- `S3D5Q216` e `S3D5Q217` delimitam expressamente o modelo clássico dos níveis de isolamento;
- `S3D5Q230` reconhece aborto como mecanismo compatível com `Serializable`;
- `S3D5Q242`–`S3D5Q250` preservam a distinção entre WAL, checkpoint, undo, redo e 2PC;
- `S3D6Q254`, `S3D6Q255` e `S3D6Q269` evitam absolutos indevidos sobre uso de índice;
- `S3D6Q280`, `S3D6Q292`, `S3D6Q294` e `S3D6Q295` mantêm respostas corretas no recorte de produtos estudado.

## 2. Ressalvas técnicas e teoria a completar

### `S3D6Q257` e `S3D6Q258` — literal de data e portabilidade

O raciocínio correto é sólido: intervalo semiaberto sobre a coluna tende a ser mais sargável e evita perder horários do último dia. Contudo, o código usa o literal tipado `DATE '2026-01-01'` sem indicar dialeto.

Esse literal funciona no recorte SQL usado pela teoria, mas não deve parecer uma instrução executável sem mudança nos três produtos. Em T-SQL, a documentação apresenta literais de cadeia, `CAST`/`CONVERT` e formatos próprios; portanto, o item precisa de uma destas soluções:

- declarar que o trecho está em “SQL conceitual/compatível com literal tipado”; ou
- usar parâmetros `:inicio` e `:fim`; ou
- apresentar variantes por produto.

O gabarito de ambos permanece correto. A lacuna está na delimitação, não no conceito.

### `S3D6Q293` — organização física do InnoDB

A alternativa B e a teoria afirmam, de forma resumida, que “InnoDB organiza dados pela primary key”. Isso é correto **quando há chave primária explícita**, mas não descreve todos os casos:

1. com `PRIMARY KEY`, ela é o índice clustered;
2. sem PK, o InnoDB usa o primeiro índice `UNIQUE NOT NULL` adequado;
3. sem ambos, cria o índice clustered oculto `GEN_CLUST_INDEX`.

O item não passa a ter outra resposta correta, porque B ainda é a única alternativa compatível com o quadro ensinado. Porém, convém corrigir teoria, alternativa e comentário com “quando definida; na ausência, aplica-se o fallback do InnoDB”. A regra completa consta na [documentação oficial do MySQL 9.7 sobre índices clustered e secundários](https://dev.mysql.com/doc/refman/9.7/en/innodb-index-types.html).

## 3. Referência interna imprecisa

### `S3D6Q270`

O enunciado reproduz o caso de otimização que compara ganho de leitura com aumento do custo da carga (`8 s → 900 ms` e `20 s → 38 s`). Esse caso está desenvolvido no **Exemplo 6 do Bloco 2**, sob `#s3-d6-otimizacao`, mas a questão aponta para `#s3-d6-indices`.

**Ajuste recomendado:** trocar somente o alvo da referência para `semana_03_estudo.md#s3-d6-otimizacao`.

Os demais 139 itens apontam para uma seção que contém a base necessária. As referências amplas das extras (`#s3-d5-b4`, `#s3-d5-b5`, `#s3-d6-b4` e `#s3-d6-b5`) são menos granulares, mas semanticamente corretas.

## 4. Dependência de produto, versão ou configuração

Foram marcados **19 itens sensíveis a produto**:

`S3D5Q237`, `S3D5Q240`, `S3D6Q252`, `S3D6Q254`, `S3D6Q255`, `S3D6Q257`, `S3D6Q258`, `S3D6Q260`, `S3D6Q264`, `S3D6Q266`, `S3D6Q268`, `S3D6Q280`, `S3D6Q281`, `S3D6Q284`, `S3D6Q291`, `S3D6Q292`, `S3D6Q293`, `S3D6Q294` e `S3D6Q295`.

### Sensibilidade já controlada — 14 itens

Não exigem correção semântica: `S3D5Q237`, `S3D5Q240`, `S3D6Q252`, `S3D6Q254`, `S3D6Q255`, `S3D6Q260`, `S3D6Q266`, `S3D6Q268`, `S3D6Q281`, `S3D6Q284`, `S3D6Q291`, `S3D6Q292`, `S3D6Q294` e `S3D6Q295`.

Esses itens usam salvaguardas adequadas, como “pode”, “tende”, “conforme o produto”, engine explícito ou versões fixadas. As afirmações sobre plano real também estão coerentes: PostgreSQL executa o comando com `ANALYZE`, MySQL 9.7 oferece `EXPLAIN ANALYZE`, e o plano real do SQL Server contém dados obtidos da execução. Fontes primárias: [PostgreSQL 18 — EXPLAIN](https://www.postgresql.org/docs/18/sql-explain.html), [MySQL 9.7 — EXPLAIN](https://dev.mysql.com/doc/refman/9.7/en/explain.html) e [SQL Server — plano real](https://learn.microsoft.com/en-us/sql/relational-databases/performance/analyze-an-actual-execution-plan?view=sql-server-ver17).

### Delimitação adicional recomendada — 5 itens

| ID | Dependência | Ajuste sugerido |
|---|---|---|
| `S3D6Q257` | literal de data e forma sargável variam por dialeto/recurso | declarar SQL conceitual ou usar parâmetros |
| `S3D6Q258` | tipo temporal, precisão e sintaxe do literal variam | manter o intervalo semiaberto, delimitando o tipo/dialeto |
| `S3D6Q264` | `INCLUDE` não é sintaxe uniforme nos três SGBDs | dizer “em produto que suporte `INCLUDE`” ou descrever apenas as colunas contidas |
| `S3D6Q280` | “MySQL atuais” envelhece e contrasta com a regra de versionamento do próprio Dia 6 | substituir por PostgreSQL 18.4 e MySQL 9.7 LTS |
| `S3D6Q293` | clustered index do InnoDB depende da existência de PK/unique adequado | acrescentar a regra de fallback |

## 5. Nível inflado

Entre os dez itens classificados como **Muito difícil**, dois estão bem calibrados e foram preservados nessa faixa:

- `S3D5Q210`: exige reconhecer desfecho desconhecido, evitar repetição cega e pensar em idempotência;
- `S3D5Q246`: integra decisão de commit, estado físico das páginas, undo e redo.

Os outros **oito** estão acima do raciocínio efetivamente exigido:

| ID | Por que a classificação está inflada | Faixa sugerida |
|---|---|---|
| `S3D5Q245` | reconhecimento direto da definição de checkpoint; três alternativas usam absolutos fáceis de eliminar | Difícil |
| `S3D5Q250` | reproduz diretamente a lista do que o 2PC não oferece | Difícil |
| `Extra 5.10` | integração simples de fonte ética, sujeito e jurisdição, com três extremos | Difícil |
| `Extra 5.20` | a chave reproduz literalmente a arquitetura do plano integral | Difícil |
| `S3D6Q265` | repete quase integralmente o Exemplo 1 de índice composto | Difícil |
| `S3D6Q270` | repete os números e a conclusão do Exemplo 6 | Difícil |
| `Extra 6.11` | deslocamento mecânico de duas referências mistas | Difícil |
| `Extra 6.19` | só uma alternativa é sintaticamente íntegra e coerente; as demais denunciam o erro | Médio ou Difícil |

Não se recomenda rebaixar automaticamente todos os itens “Difícil”: vários deles exigem distinção fina ou integração legítima. O problema mais claro está na faixa “Muito difícil”, usada em itens cuja resposta acabou de ser dada por quadro ou exemplo praticamente idêntico.

## 6. Distratores fracos

Aplicou-se um critério conservador: o item só foi marcado quando **dois ou mais** distratores são ruído de outra categoria, formulação manifestamente absurda ou pista que permite acertar sem dominar o conceito. Foram encontrados **13 itens**:

| Grupo | IDs | Diagnóstico |
|---|---|---|
| Transações e concorrência | `S3D5Q206`, `S3D5Q226`, `S3D5Q229` | sigilo, privilégio administrativo, tipo textual ou retirada de constraint aparecem onde seriam melhores erros próximos sobre commit, locks ou validação de versão |
| Legislação | `Extra 5.4`, `Extra 5.8` | cache/aparência do portal e heurísticas como “alternativa mais longa” não competem com uma rota normativa real |
| Índices e otimização | `S3D6Q256`, `S3D6Q266`, `S3D6Q272`, `S3D6Q273`, `S3D6Q279`, `S3D6Q285`, `S3D6Q287` | PK aleatória, transação distribuída, privilégio, injeção, cor de ícone e tamanho do nome permitem descarte por categoria |
| Ferramentas | `Extra 6.7` | converter comentário em fórmula e substituir estilo de título são funções sem proximidade com histórico de versões |

Sugestão de reescrita futura: trocar o ruído por **erros de fronteira**. Exemplos:

- autocommit de cada comando × transação explícita × savepoint;
- espera longa × ciclo de deadlock × starvation;
- converter o parâmetro × converter a coluna × índice por expressão;
- estatística desatualizada × correlação não modelada × parâmetro não representativo;
- versão atual × versão nomeada × cópia restaurada no histórico.

Assim, a questão continua com uma única chave, mas passa a medir conhecimento em vez de eliminação por absurdo.

## 7. Conferência dos comentários

Os 140 comentários foram confrontados com os respectivos enunciados, alternativas e chaves. Não foi encontrada:

- análise que declare correta uma alternativa diferente do gabarito;
- justificativa circular que dependa apenas de “é a resposta estudada”;
- explicação tecnicamente incompatível com o conceito central;
- troca entre leitura suja, não repetível, fantasma e atualização perdida;
- troca entre atomicidade, consistência, isolamento e durabilidade;
- troca entre constraint, índice, autenticação, autorização e auditoria;
- inversão de undo/redo ou das fases do 2PC;
- inversão de ETL/ELT, OLTP/OLAP ou referência relativa/absoluta.

Há apenas uma melhoria de redação recomendável, sem efeito no gabarito: em `Extra 6.17`, “deu ... respeito aos direitos” é gramaticalmente analisável, porém pouco natural. Uma formulação mais limpa seria “deu transparência às decisões e garantiu respeito aos direitos”.

## 8. Ordem recomendada de correção após o descongelamento

1. **Precisão técnica:** `S3D6Q257`, `S3D6Q258` e `S3D6Q293`, incluindo as mesmas ressalvas na teoria e nos comentários.
2. **Escopo de produto:** `S3D6Q264` e `S3D6Q280`.
3. **Navegação:** referência de `S3D6Q270`.
4. **Calibração:** reclassificar os oito itens de nível inflado.
5. **Qualidade de banca:** substituir os distratores fracos dos 13 IDs, preservando as chaves e o equilíbrio global de letras.
6. Rodar novamente as validações estruturais depois de qualquer troca de alternativa para confirmar gabarito, comentários, comprimentos e distribuição.

## Parecer final

**Aprovado com ajustes localizados.** Não há motivo semântico para descartar ou refazer o banco dos Dias 5 e 6. O conteúdo cobre a teoria, as respostas estão corretas e os comentários ensinam o raciocínio. As intervenções propostas servem para aumentar precisão entre produtos e aproximar a dificuldade real do padrão de uma prova bem construída.

## Fechamento dos achados

Os achados acima foram implementados posteriormente nos arquivos-fonte `partes/questoes_dias_05_06.md` e `partes/estudo_dias_05_06.md`, sem editar os consolidados durante esta etapa.

### Correções concluídas

- `S3D6Q257` e `S3D6Q258`: item, comentário, exemplo e teoria agora declaram SQL conceitual e exigem adaptação do literal/tipo ao dialeto;
- `S3D6Q264`: o suporte a `INCLUDE` passou a ser condição expressa no item e na teoria;
- `S3D6Q280`: “versões atuais” foi substituído pelo recorte PostgreSQL 18.4, MySQL 9.7 LTS e SQL Server 2025 17.x;
- `S3D6Q293`: item, comentário e quadro teórico passaram a registrar PK, `UNIQUE NOT NULL` adequado e `GEN_CLUST_INDEX` como fallback do InnoDB;
- `S3D6Q270`: questão e comentário agora apontam para `#s3-d6-otimizacao`;
- os oito níveis inflados foram alterados de “Muito difícil” para “Difícil”: `S3D5Q245`, `S3D5Q250`, Extras 5.10 e 5.20, `S3D6Q265`, `S3D6Q270`, Extras 6.11 e 6.19;
- os 13 conjuntos de distratores marcados foram efetivamente reescritos como erros próximos, e suas 52 análises foram sincronizadas;
- a Extra 6.17 passou a usar “deu transparência às decisões e garantiu respeito aos direitos”, com comentário correspondente.

### Revalidação posterior

| Controle | Resultado |
|---|---:|
| Questões principais | 100/100 |
| Extras | 40/40 |
| Comentários principais | 100/100 |
| Comentários de extras | 40/40 |
| Itens com A–D exatamente uma vez | 140/140 |
| Comentários com análises A–D exatamente uma vez | 140/140 |
| Gabarito da tabela igual ao comentário | 140/140 |
| Nível do item igual ao comentário | 140/140 |
| Distribuição final por nível | 57 Médios, 81 Difíceis, 2 Muito difíceis |

**Estado final:** todos os achados estão encerrados; os dois únicos itens mantidos como “Muito difícil” são `S3D5Q210` e `S3D5Q246`, pelos motivos registrados na auditoria.

### Nota de integração global

O balanceamento posterior dos 420 itens permutou uma posição de alternativa no nível Difícil deste lote, mantendo conteúdo, comentário A–D e tabela sincronizados. A distribuição final de letras dos Dias 5–6 ficou: Médio A=15, B=14, C=14, D=14; Difícil A=19, B=21, C=21, D=20; Muito difícil A=1, B=0, C=1, D=0. O controle de equilíbrio é aplicado ao banco semanal integrado, e não como cota artificial por lote.
