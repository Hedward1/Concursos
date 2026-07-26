# Dia 3 - SQL ANSI: consulta, junções, agrupamento e subconsultas

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais - S3D3Q101 a S3D3Q150

### S3D3Q101 — Ordem lógica de uma consulta

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

Considere uma consulta com junção, filtro de linhas, agrupamento, filtro de grupos, projeção e ordenação. Qual sequência representa corretamente o modelo mental de processamento ensinado?

A) `FROM/JOIN` → `SELECT` → `ORDER BY` → `WHERE` → `GROUP BY` → `HAVING`.

B) `FROM/JOIN` e `ON` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`.

C) `SELECT` → `WHERE` → `FROM/JOIN` → `HAVING` → `GROUP BY` → `ORDER BY`.

D) `WHERE` → `SELECT` → `GROUP BY` → `ON` → `HAVING` → `ORDER BY`.

### S3D3Q102 — Resultado de DISTINCT após filtro

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

No esquema de treino, qual é o resultado de `SELECT DISTINCT uf FROM profissional WHERE ativo = 'S' ORDER BY uf;`?

A) Uma linha, apenas `PR`.

B) Três linhas: `PR`, `PR` e `PR`.

C) Nenhuma linha, porque `DISTINCT` não pode ser usado com `WHERE`.

D) Duas linhas: `PR` e `SC`.

### S3D3Q103 — Teste correto de ausência

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

Qual consulta localiza o profissional sem unidade no conjunto de treino?

A) `SELECT nome FROM profissional WHERE NULL = NULL;`

B) `SELECT nome FROM profissional WHERE unidade_id = NULL;`

C) `SELECT nome FROM profissional WHERE unidade_id <> NULL;`

D) `SELECT nome FROM profissional WHERE unidade_id IS NULL;`

### S3D3Q104 — Limites de BETWEEN

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

Sobre o predicado `valor BETWEEN 120 AND 150`, assinale a alternativa correta.

A) Ele inclui os dois limites, equivalendo a `valor >= 120 AND valor <= 150` para valores comparáveis.

B) Ele seleciona apenas valores estritamente maiores que 120 e menores que 150.

C) Ele equivale a `valor > 120 OR valor < 150`.

D) Ele exclui 120 e inclui 150.

### S3D3Q105 — Alias da projeção no WHERE

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

Uma consulta define `valor * 1.1 AS reajustado` na lista `SELECT` e tenta usar `WHERE reajustado > 150` no mesmo nível. Qual diagnóstico é o mais adequado?

A) O problema é que `WHERE` aceita somente colunas inteiras, não expressões numéricas.

B) Basta mover o alias para `GROUP BY`, ainda que não haja agrupamento.

C) O alias nasce após o `WHERE`; repita a expressão ou use outra consulta.

D) O alias sempre pode ser usado porque `SELECT` aparece primeiro na escrita.

### S3D3Q106 — Diferença e ausência no mesmo filtro

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

No conjunto de treino, qual resultado produz `WHERE unidade_id <> 10 OR unidade_id IS NULL`?

A) Somente Carla.

B) Carla e Davi.

C) Ana, Bruno e Davi.

D) Somente Davi.

### S3D3Q107 — Precedência entre AND e OR

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

Sem parênteses, como deve ser lido o predicado `ativo = 'N' OR uf = 'PR' AND unidade_id = 10`?

A) `(ativo = 'N' AND uf = 'PR') OR unidade_id = 10`.

B) `(ativo = 'N' OR uf = 'PR') AND unidade_id = 10`.

C) `ativo = 'N' AND (uf = 'PR' OR unidade_id = 10)`.

D) `ativo = 'N' OR (uf = 'PR' AND unidade_id = 10)`.

### S3D3Q108 — Contagem de pagamentos pagos

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Esquema e dados de treino](semana_03_estudo.md#s3-d3-esquema-treino) e [agregação](semana_03_estudo.md#s3-d3-agregacao).

Qual resultado produz `SELECT COUNT(*) FROM pagamento WHERE status = 'PAGO';` no conjunto de treino?

A) 3.

B) 1.

C) 2.

D) 4.

### S3D3Q109 — Cardinalidade de INNER JOIN

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Quantas linhas produz `profissional INNER JOIN pagamento ON pagamento.profissional_id = profissional.id` no conjunto de treino?

A) 5.

B) 1.

C) 4.

D) 3.

### S3D3Q110 — LEFT JOIN e contagem de detalhes

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Uma `LEFT JOIN` agrupa cada profissional e calcula `COUNT(pg.id)`. Qual conjunto de totais está correto?

A) Ana 2, Bruno 1, Carla 1 e Davi 1.

B) Ana 1, Bruno 1, Carla 1 e Davi 0.

C) Ana 2, Bruno 1, Carla 1; Davi não aparece.

D) Ana 2, Bruno 1, Carla 1 e Davi 0.

### S3D3Q111 — Filtro de linha opcional em ON

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

O relatório deve listar todos os profissionais e mostrar valor apenas de pagamento `ABERTO`. Qual desenho mantém o requisito?

A) `LEFT JOIN pagamento pg ON pg.profissional_id=p.id WHERE pg.status='ABERTO'`.

B) `LEFT JOIN pagamento pg ON pg.profissional_id=p.id AND pg.status='ABERTO'`.

C) `CROSS JOIN pagamento pg WHERE pg.status='ABERTO'`.

D) `INNER JOIN pagamento pg ON pg.profissional_id=p.id WHERE pg.status='ABERTO'`.

### S3D3Q112 — Produto cartesiano controlado

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

Se quatro profissionais forem combinados com três unidades por `CROSS JOIN`, sem filtro posterior, quantas linhas surgem?

A) 7 linhas.

B) 12 linhas.

C) 3 linhas.

D) 4 linhas.

### S3D3Q113 — COUNT(*) e COUNT da coluna

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Após `LEFT JOIN` de profissionais com pagamentos, o grupo de Davi contém uma linha estendida com `pg.id = NULL`. Qual par é correto?

A) `COUNT(*) = 0` e `COUNT(pg.id) = 0`.

B) `COUNT(*) = 1` e `COUNT(pg.id) = 1`.

C) Ambas as contagens resultam em `NULL`.

D) `COUNT(*) = 1` e `COUNT(pg.id) = 0`.

### S3D3Q114 — Grupo com pelo menos dois ativos

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Uma consulta junta unidade a profissional, filtra `ativo='S'`, agrupa por unidade e exige `HAVING COUNT(*) >= 2`. Qual unidade aparece?

A) Registro, com 1.

B) Fiscalização, com 2.

C) Tecnologia, com 1.

D) Nenhuma unidade.

### S3D3Q115 — Granularidade inválida na seleção

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Em SQL estrito, qual é o problema de `SELECT uf, nome, COUNT(*) FROM profissional GROUP BY uf;`?

A) `nome` não é agregado nem consta do `GROUP BY`.

B) Toda consulta agrupada precisa de `HAVING`.

C) `COUNT(*)` exige obrigatoriamente `DISTINCT`.

D) `uf` não pode aparecer em `GROUP BY`.

### S3D3Q116 — Agregados e valores nulos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Assinale a alternativa correta sobre `SUM` e `AVG`.

A) Incluem `NULL` no denominador de `AVG`.

B) Falham sempre que a expressão contém ao menos um nulo.

C) Ignoram nulos da expressão, sem convertê-los em zero.

D) Tratam todo `NULL` como zero antes do cálculo.

### S3D3Q117 — EXISTS correlacionado

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Qual profissional é retornado pela consulta que exige `EXISTS` de pagamento com o mesmo `profissional_id` e `status='ABERTO'`?

A) Carla.

B) Davi.

C) Ana.

D) Bruno.

### S3D3Q118 — Antijunção com NOT EXISTS

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Quem satisfaz uma consulta `NOT EXISTS` que procura ausência de qualquer pagamento correlato?

A) Davi.

B) Bruno.

C) Ana.

D) Carla.

### S3D3Q119 — Armadilha de NOT IN com nulo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

Por que `NOT IN (subconsulta)` exige cuidado quando a subconsulta pode retornar `NULL`?

A) `NULL` pode tornar a comparação desconhecida; `NOT EXISTS` expressa a antijunção com segurança.

B) Porque subconsultas não podem ser usadas com `NOT IN`.

C) Porque `NOT IN` elimina duplicatas antes da comparação e sempre fica falso.

D) Porque `NULL` é convertido em zero dentro de `IN`.

### S3D3Q120 — Subconsulta correlacionada

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

Qual característica torna uma subconsulta correlacionada?

A) Retornar exatamente uma coluna.

B) Referenciar coluna externa, como `pg.profissional_id = p.id`.

C) Conter obrigatoriamente uma função agregada.

D) Ser executada apenas uma vez antes da consulta externa.

### S3D3Q121 — UNION e duplicatas

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

Uma consulta produz `PR, PR, SC` e outra produz `PR`. Qual saída decorre de `UNION`?

A) Somente `SC`.

B) `PR` e `SC`.

C) `PR, PR, SC, PR`.

D) Somente `PR`.

### S3D3Q122 — UNION ALL e multiplicidades

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

Com as mesmas entradas `PR, PR, SC` e `PR`, quantas linhas produz `UNION ALL`?

A) 1.

B) 2.

C) 4.

D) 3.

### S3D3Q123 — Interseção de resultados

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

Se o primeiro resultado distinto é `{PR, SC}` e o segundo é `{PR}`, o que `INTERSECT` retorna?

A) Conjunto vazio.

B) `SC`.

C) `PR, SC`.

D) `PR`.

### S3D3Q124 — Diferença orientada por EXCEPT

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

Considerando `{PR, SC} EXCEPT {PR}`, qual é o resultado?

A) `SC`.

B) `PR`.

C) `PR, SC`.

D) Conjunto vazio.

### S3D3Q125 — Garantia de ordenação

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

Qual cláusula estabelece a ordem solicitada da saída de uma consulta?

A) `DISTINCT`.

B) `GROUP BY`.

C) A ordem física aparente da tabela.

D) `ORDER BY`.

### S3D3Q126 — Efeito de AS na projeção

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

Em `SELECT valor * 1.1 AS reajustado`, o que `AS reajustado` faz?

A) Filtra linhas cujo valor reajustado é nulo.

B) Altera definitivamente o nome da coluna armazenada.

C) Nomeia a expressão apenas na saída da consulta.

D) Cria automaticamente uma coluna física calculada.

### S3D3Q127 — Escopo de DISTINCT

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

Em `SELECT DISTINCT uf, ativo FROM profissional`, como são identificadas duplicatas?

A) Pelo identificador da linha original, ainda que não projetado.

B) Somente pelo primeiro atributo, `uf`.

C) Somente pelo último atributo, `ativo`.

D) Pela combinação completa `(uf, ativo)` projetada.

### S3D3Q128 — IN sobre os status existentes

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

No conjunto de treino, quantas linhas satisfazem `status IN ('PAGO','ABERTO')`?

A) 4.

B) 1.

C) 2.

D) 3.

### S3D3Q129 — WHERE e HAVING no lugar certo

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Para encontrar profissionais com pelo menos dois pagamentos `PAGO`, qual estrutura expressa melhor as duas etapas?

A) Agrupar primeiro, projetar e depois usar `ON COUNT(*) >= 2`.

B) Usar apenas `DISTINCT`, pois ele calcula quantidades.

C) `WHERE status='PAGO'`, grupo por profissional e `HAVING COUNT(*)>=2`.

D) Usar `WHERE COUNT(*) >= 2` e `HAVING pg.status='PAGO'`.

### S3D3Q130 — Rastreamento de LEFT JOIN agrupada

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Roteiro de rastreamento manual](semana_03_estudo.md#s3-d3-pratica) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Considere `SELECT p.uf, COUNT(pg.id) FROM profissional p LEFT JOIN pagamento pg ON pg.profissional_id=p.id WHERE p.ativo='S' GROUP BY p.uf;`. Qual resultado é produzido?

A) `PR | 3`.

B) `PR | 2` e `SC | 1`.

C) `PR | 4` e `SC | 0`.

D) `PR | 4`.

### S3D3Q131 — Seleção e projeção

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Seleção e projeção](semana_03_estudo.md#s3-d3-selecao-projecao).

Assinale a alternativa que distingue corretamente seleção de projeção no uso didático adotado.

A) Seleção elimina duplicatas; projeção executa junções.

B) Seleção ordena linhas; projeção agrupa linhas.

C) Seleção cria tabelas; projeção apaga tabelas.

D) Seleção filtra linhas; projeção escolhe ou calcula colunas.

### S3D3Q132 — Cardinalidade antes de filtrar

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

Uma consulta faz `CROSS JOIN` entre 4 profissionais e 3 unidades e, depois, filtra duas combinações. Quantas linhas havia imediatamente após a junção e antes do `WHERE`?

A) 10.

B) 12.

C) 2.

D) 5.

### S3D3Q133 — Finalidade de self-join

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

Uma self-join é caracterizada por:

A) uma operação exclusiva de tabelas sem chave.

B) um produto cartesiano que não admite condição `ON`.

C) duas referências lógicas, com aliases distintos, à mesma relação.

D) uma junção que obrigatoriamente compara a linha consigo mesma.

### S3D3Q134 — Risco de NATURAL JOIN

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

Por que `NATURAL JOIN` é considerado arriscado em código crítico?

A) Porque nunca permite correspondência entre colunas.

B) Infere colunas por nomes iguais e muda se o esquema evoluir.

C) Porque sempre produz produto cartesiano.

D) Porque elimina todas as colunas usadas na junção.

### S3D3Q135 — Contagem nula após junção externa

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Para Davi, sem pagamentos, qual resultado tem `COUNT(pg.valor)` em uma `LEFT JOIN` agrupada por profissional?

A) 0.

B) A consulta falha.

C) `NULL`.

D) 1.

### S3D3Q136 — Ausência não é soma zero automática

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Qual afirmação respeita a regra ensinada para agregação?

A) `SUM` converte todo nulo em zero antes de somar.

B) `AVG` conta nulos no denominador.

C) A ausência de linhas sempre produz zero em qualquer agregado.

D) `SUM` e `AVG` ignoram nulos; zero exige regra explícita.

### S3D3Q137 — Outer join com filtro compensado

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

No conjunto de treino, uma consulta usa `LEFT JOIN pagamento pg ON pg.profissional_id=p.id` e `WHERE pg.status='PAGO' OR pg.id IS NULL`. Quais profissionais permanecem?

A) Ana e Davi.

B) Ana, Bruno, Carla e Davi.

C) Somente Ana, Bruno e Carla.

D) Somente Davi.

### S3D3Q138 — Antijunção por LEFT JOIN

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

Supondo `pagamento.id` não nulo nas linhas reais, qual padrão encontra profissionais sem pagamento?

A) `INNER JOIN pagamento pg ... WHERE pg.id IS NULL`.

B) `CROSS JOIN pagamento pg ... WHERE pg.id IS NULL`.

C) `LEFT JOIN pagamento pg ... WHERE p.id IS NULL`.

D) `LEFT JOIN pagamento pg ... WHERE pg.id IS NULL`.

### S3D3Q139 — Multiplicação de linhas antes da contagem

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Roteiro de rastreamento manual](semana_03_estudo.md#s3-d3-pratica) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Uma consulta junta UNIDADE a PROFISSIONAL e depois a PAGAMENTO, agrupa Fiscalização e calcula `COUNT(p.id)`. Qual valor obtém para essa unidade?

A) 3: duas linhas de Ana e uma de Bruno.

B) 1, porque o grupo representa uma unidade.

C) 2, porque existem dois profissionais distintos.

D) 4, porque existem quatro pagamentos no banco.

### S3D3Q140 — Compatibilidade em operações de conjunto

**Nível:** Médio

**Uso:** Revisão

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

Qual requisito estrutural é necessário para combinar duas consultas com `UNION`, `INTERSECT` ou `EXCEPT`?

A) As colunas precisam ter os mesmos nomes de alias.

B) Cada lado deve possuir a mesma quantidade de linhas.

C) Mesmo número de colunas e tipos compatíveis por posição.

D) As duas consultas devem ler a mesma tabela.

### S3D3Q141 — Unidades sem profissional ativo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Qual consulta identifica unidades sem profissional ativo, preservando também unidade sem qualquer profissional?

A) `SELECT u.nome FROM unidade u CROSS JOIN profissional p WHERE p.ativo='N';`

B) `SELECT u.nome FROM unidade u LEFT JOIN profissional p ON p.unidade_id=u.id AND p.ativo='S' WHERE p.id IS NULL;`

C) `SELECT u.nome FROM unidade u JOIN profissional p ON p.unidade_id=u.id WHERE p.ativo<>'S';`

D) `SELECT u.nome FROM unidade u LEFT JOIN profissional p ON p.unidade_id=u.id WHERE p.ativo='N';`

### S3D3Q142 — Total pago preservando profissionais

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Qual desenho calcula a soma de pagamentos `PAGO` por profissional sem eliminar Davi, aceitando resultado nulo para quem não pagou?

A) `CROSS JOIN pagamento pg WHERE pg.status='PAGO' GROUP BY p.id`.

B) `JOIN pagamento pg ON pg.profissional_id=p.id WHERE pg.status='PAGO' GROUP BY p.id`.

C) `LEFT JOIN pagamento pg ON pg.profissional_id=p.id AND pg.status='PAGO' GROUP BY p.id`.

D) `LEFT JOIN pagamento pg ON pg.profissional_id=p.id WHERE pg.status='PAGO' GROUP BY p.id`.

### S3D3Q143 — Comando negativo sobre NULL

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

Assinale a alternativa **INCORRETA** sobre `NULL` em filtros SQL.

A) `coluna <> 10 OR coluna IS NULL` pode incluir valores diferentes e ausências.

B) `WHERE` conserva somente predicados verdadeiros; falso e desconhecido são removidos.

C) `IS NOT NULL` testa a presença de valor.

D) `coluna = NULL` é a forma correta de localizar ausência.

### S3D3Q144 — Assertivas sobre etapas lógicas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

Analise: I. `WHERE` filtra linhas antes de `GROUP BY`. II. `HAVING` filtra linhas brutas antes da junção. III. Alias criado no `SELECT` normalmente não está disponível no `WHERE` do mesmo nível. IV. `ORDER BY` garante a ordem solicitada. Está correto o que se afirma em:

A) I, III e IV apenas.

B) I e II apenas.

C) II e III apenas.

D) I, II e IV apenas.

### S3D3Q145 — Contagens em unidade vazia

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Uma `LEFT JOIN` parte de UNIDADE, agrupa Tecnologia, que não possui profissionais, e calcula `COUNT(*)` e `COUNT(p.id)`. Qual par surge?

A) `NULL` e `NULL`.

B) 1 e 0.

C) 0 e 0.

D) 1 e 1.

### S3D3Q146 — Projeção dentro de EXISTS

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

Por que é comum escrever `SELECT 1` dentro de `EXISTS`?

A) Porque `SELECT *` mudaria obrigatoriamente o número de linhas externas.

B) Porque `EXISTS` soma o valor literal e compara com um.

C) Importa existir alguma linha, não o valor projetado pela subconsulta.

D) Porque `EXISTS` aceita somente constantes.

### S3D3Q147 — Três filtros em agregação por unidade

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Roteiro de rastreamento manual](semana_03_estudo.md#s3-d3-pratica).

Uma unidade deve ser listada somente se possuir: (1) ao menos dois profissionais ativos distintos; (2) ao menos dois pagamentos `PAGO` desses profissionais; e (3) agrupamento no nível da unidade. Qual alternativa atende aos três filtros sem contar Ana duas vezes como profissional?

A) Agrupar por unidade e usar apenas `HAVING COUNT(*)>=2`, pois cada linha representa um profissional.

B) Juntar tudo, usar `WHERE p.ativo='S'` e `HAVING COUNT(p.id)>=2`, sem filtrar pagamento nem usar distinção.

C) Agrupar por profissional e exigir `COUNT(DISTINCT u.id)>=2 AND COUNT(pg.id)>=2`.

D) Agrupar por unidade, filtrar ativos/pagos e exigir `COUNT(DISTINCT p.id)>=2` e `COUNT(pg.id)>=2`.

### S3D3Q148 — Existência paga e ausência aberta

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Procura-se profissional que seja (1) ativo, (2) do PR, (3) possua pagamento `PAGO` e (4) não possua pagamento `ABERTO`. No conjunto de treino, qual alternativa é correta?

A) Ana, pois é a única com pagamento aberto.

B) Bruno: `EXISTS` para PAGO e `NOT EXISTS` para ABERTO.

C) Ana e Bruno, pois ambos possuem pagamento pago.

D) Davi, pois não tem pagamento aberto.

### S3D3Q149 — Comparação completa de ON e WHERE

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Compare: Q1 usa `LEFT JOIN pagamento pg ON pg.profissional_id=p.id AND pg.status='PAGO'`; Q2 usa `LEFT JOIN ... ON pg.profissional_id=p.id WHERE pg.status='PAGO'`. Sem agrupamento, qual afirmação considera preservação, filtro e cardinalidade?

A) Q1 produz três e Q2 quatro, pois `WHERE` restaura a linha externa.

B) As duas produzem cinco linhas, contando também o pagamento aberto de Ana.

C) Q1 gera quatro linhas, incluindo Davi nulo; Q2 elimina Davi e gera três.

D) As duas produzem quatro linhas porque ambas começam com `LEFT JOIN`.

### S3D3Q150 — Diferença de conjuntos com filtros

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

Considere o conjunto A de UFs distintas com profissional ativo e o conjunto B de UFs distintas com algum pagamento `ABERTO`. Qual resultado produz `A EXCEPT B` no conjunto de treino?

A) 0 linha.

B) `SC`.

C) `PR, SC`.

D) `PR`.

## Questões extras - Dia 3

#### Extra Dia 3.1 — Lei e criação do sistema

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Lei nº 4.769/1965
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Qual afirmação corresponde à base revisada?

A) A Lei nº 4.769/1965 apenas reconheceu a profissão; os Conselhos foram criados exclusivamente pelo decreto regulamentar.

B) O Decreto nº 61.934/1967 é a fonte originária do sistema, e a lei posterior apenas detalha sua execução.

C) A Lei nº 4.769/1965 disciplina a profissão, mas o Sistema CFA/CRAs surgiu somente de resoluções posteriores do CFA.

D) A Lei nº 4.769/1965 disciplina a profissão e cria o Sistema CFA/CRAs.

#### Extra Dia 3.2 — Âmbito do CFA e do CRA

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Competência institucional
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Assinale a divisão de atuação compatível com a revisão.

A) O CRA-PR pode afastar lei federal quando o fato ocorre no Paraná.

B) O CRA-PR edita toda orientação normativa nacional e o CFA apenas registra no Paraná.

C) O CFA orienta e supervisiona nacionalmente; o CRA-PR registra e fiscaliza na sua jurisdição.

D) CFA e CRA-PR são órgãos sem qualquer integração funcional.

#### Extra Dia 3.3 — Função do Regimento Interno

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Regimento Interno
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

O Regimento Interno do CRA-PR tem como função central:

A) disciplinar, com alcance nacional, todas as infrações éticas, substituindo o Código de Ética.

B) regulamentar a execução da Lei nº 4.769/1965 em todo o território nacional.

C) exercer a orientação normativa nacional em lugar do CFA.

D) organizar órgãos, competências e funcionamento interno do CRA-PR.

#### Extra Dia 3.4 — Autonomia e integração

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Natureza do CRA-PR
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

A autonomia técnica, administrativa e financeira do CRA-PR:

A) afasta a supervisão normativa do CFA, embora preserve a integração financeira ao sistema.

B) torna facultativa a observância das diretrizes do CFA quando elas geram custo administrativo regional.

C) permite que regras regionais prevaleçam, em matéria administrativa local, sobre a orientação nacional do sistema.

D) não o torna entidade privada nem rompe integração ao sistema.

#### Extra Dia 3.5 — Alcance do Código de Ética

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Código de Ética
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Segundo a base revisada, o Código de Ética previsto no recorte vigente:

A) define deveres, direitos e infrações para os sujeitos que alcança.

B) dirige-se apenas a empregados e conselheiros do sistema, excluindo os profissionais registrados.

C) define padrões de conduta, mas deixa a classificação das infrações a cada regimento regional.

D) transfere aos regimentos regionais a determinação dos deveres e direitos éticos.

#### Extra Dia 3.6 — Fato regional e competência nacional

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Âmbito institucional
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Um fato fiscalizatório ocorre no Paraná. Qual conclusão é adequada?

A) A localização do fato confere ao CRA-PR competência normativa nacional apenas para aquele processo.

B) A orientação nacional do CFA fica suspensa enquanto o CRA-PR conduz a apuração regional.

C) O CRA-PR atua regionalmente, sem assumir a orientação normativa nacional.

D) O Regimento regional define o mérito do caso ainda que seja incompatível com a legislação e a regulamentação federais.

#### Extra Dia 3.7 — Hierarquia entre resolução e lei

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Hierarquia normativa
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Uma resolução administrativa posterior contraria diretamente a Lei nº 4.769/1965. Com base na revisão, deve-se concluir que:

A) a resolução mais recente pode detalhar e, por especialidade, afastar o ponto incompatível da lei.

B) o conflito deve ser resolvido somente pela cronologia entre os textos.

C) a resolução deve respeitar a lei e a competência normativa.

D) a autonomia regional permite escolher o texto aplicável aos fatos locais.

#### Extra Dia 3.8 — Método de leitura institucional

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Método de resolução
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Qual sequência reduz erros em questão de competência CFA/CRA?

A) Fonte → data → território → alternativa mais detalhada.

B) Fonte → âmbito → sujeito → competência.

C) Sujeito → território → prática institucional → analogia, sem revisar a hierarquia.

D) Âmbito territorial → órgão emissor → cronologia, deixando sujeito e competência em plano secundário.

#### Extra Dia 3.9 — Comando negativo sobre autonomia

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Autonomia e competência
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Assinale a alternativa **INCORRETA**.

A) A autonomia permite ao CRA-PR substituir a orientação nacional do CFA no Paraná.

B) O CRA-PR atua dentro de sua jurisdição e de suas competências.

C) Autonomia financeira não transforma o conselho em associação privada.

D) Lei, decreto e regimento possuem objetos e posições normativas diferentes.

#### Extra Dia 3.10 — Caso integrado de fonte e competência

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Aplicação institucional
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

Em processo regional, um argumento afirma que o Regimento pode afastar o decreto e que o CRA-PR assume orientação nacional por atuar no caso concreto. Qual avaliação é a melhor?

A) Somente a segunda é correta, pois toda fiscalização regional gera competência normativa nacional.

B) Ambas as afirmações são corretas pela autonomia regional.

C) Ambas confundem fonte e âmbito: regimento não afasta norma superior, e caso regional não transfere função nacional.

D) Somente a primeira é correta, pois regimento sempre prevalece dentro do órgão.

#### Extra Dia 3.11 — Negação de conjunção

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Leis de De Morgan
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

A negação de “o cadastro está íntegro e o relatório está publicado” é:

A) o cadastro está íntegro ou o relatório está publicado.

B) o cadastro não está íntegro e o relatório não está publicado.

C) se o cadastro está íntegro, o relatório não está publicado.

D) o cadastro não está íntegro ou o relatório não está publicado.

#### Extra Dia 3.12 — Negação da implicação

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Implicação
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

A negação de “se o profissional está ativo, então possui unidade” é:

A) o profissional está ativo e não possui unidade.

B) o profissional não está ativo e não possui unidade.

C) se o profissional não está ativo, então não possui unidade.

D) o profissional está ativo ou não possui unidade.

#### Extra Dia 3.13 — Negação de quantificador universal

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Quantificadores
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

A negação de “todos os profissionais ativos possuem pagamento” é:

A) nenhum profissional ativo possui pagamento.

B) todos os inativos não possuem pagamento.

C) existe pagamento sem profissional ativo.

D) existe ao menos um ativo sem pagamento.

#### Extra Dia 3.14 — Negação de nenhum

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Quantificadores
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

A negação de “nenhum relatório contém erro” é:

A) existe ao menos um relatório que contém erro.

B) existe ao menos um relatório sem erro.

C) alguns relatórios talvez contenham erro.

D) todo relatório contém erro.

#### Extra Dia 3.15 — Negação de disjunção

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Leis de De Morgan
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

A negação de “o filtro usa `WHERE` ou usa `HAVING`” é:

A) não usa `WHERE` ou não usa `HAVING`.

B) usa `WHERE` e usa `HAVING`.

C) não usa `WHERE` e não usa `HAVING`.

D) se não usa `WHERE`, então usa `HAVING`.

#### Extra Dia 3.16 — Valor concessivo de embora

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Conectores
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

Em “Embora os dados sejam úteis, não bastam para provar causalidade”, o conector destacado exprime:

A) conclusão.

B) concessão.

C) causa.

D) consequência.

#### Extra Dia 3.17 — Correlação e causalidade

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Força da evidência
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

Duas medidas cresceram no mesmo período. Qual conclusão é argumentativamente segura?

A) Não existe qualquer relação possível entre elas.

B) A correlação, sozinha, não prova causalidade.

C) A primeira necessariamente causou a segunda.

D) A segunda necessariamente causou a primeira.

#### Extra Dia 3.18 — Referente inequívoco

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Coesão referencial
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

Na frase “A equipe revisou a base com a comissão, mas ela não publicou o resultado”, qual reescrita elimina a ambiguidade se quem não publicou foi a comissão?

A) A equipe, que revisou a base com a comissão, não publicou isso.

B) A revisão ocorreu, e aquela não publicou o resultado.

C) A equipe revisou a base com a comissão, mas ela não o publicou.

D) A equipe revisou a base com a comissão, mas a comissão não publicou o resultado.

#### Extra Dia 3.19 — Conector de consequência

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Relação lógica
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

Qual conector introduz adequadamente uma consequência?

A) por isso.

B) uma vez que.

C) embora.

D) contudo.

#### Extra Dia 3.20 — Reescrita com três controles

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Coesão, concessão e causalidade
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

Texto-base: “Embora a coleta tenha aumentado, os registros não representam todos os usuários; por isso, não se pode afirmar que a política causou a melhora.” Qual reescrita preserva simultaneamente a concessão, o referente e o limite causal?

A) Os registros não representam todos os usuários, porque a política necessariamente causou a melhora apesar da coleta.

B) Embora a coleta tenha crescido, a falta de representatividade dos registros impede atribuir a melhora à política sem evidências adicionais.

C) Como a coleta aumentou, os registros representam todos; logo, a política causou a melhora.

D) A coleta aumentou, contudo isso prova que ela causou a melhora, ainda que os usuários não existam.

## Gabarito - Dia 3

### Principais

| S3D3Q101 | S3D3Q102 | S3D3Q103 | S3D3Q104 | S3D3Q105 | S3D3Q106 | S3D3Q107 | S3D3Q108 | S3D3Q109 | S3D3Q110 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | A | D | A | C | B | D | A | C | D |

| S3D3Q111 | S3D3Q112 | S3D3Q113 | S3D3Q114 | S3D3Q115 | S3D3Q116 | S3D3Q117 | S3D3Q118 | S3D3Q119 | S3D3Q120 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | B | D | B | A | C | C | A | A | B |

| S3D3Q121 | S3D3Q122 | S3D3Q123 | S3D3Q124 | S3D3Q125 | S3D3Q126 | S3D3Q127 | S3D3Q128 | S3D3Q129 | S3D3Q130 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | C | D | A | D | C | D | A | C | A |

| S3D3Q131 | S3D3Q132 | S3D3Q133 | S3D3Q134 | S3D3Q135 | S3D3Q136 | S3D3Q137 | S3D3Q138 | S3D3Q139 | S3D3Q140 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | C | B | A | D | B | D | A | C |

| S3D3Q141 | S3D3Q142 | S3D3Q143 | S3D3Q144 | S3D3Q145 | S3D3Q146 | S3D3Q147 | S3D3Q148 | S3D3Q149 | S3D3Q150 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | C | D | A | B | C | D | B | C | A |

### Extras

| 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | C | D | D | A | C | C | B | A | C |

| 3.11 | 3.12 | 3.13 | 3.14 | 3.15 | 3.16 | 3.17 | 3.18 | 3.19 | 3.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | A | D | A | C | B | B | D | A | B |

## Comentários - Dia 3

### Comentário S3D3Q101

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Projeta e ordena antes dos filtros, o que não descreve a ordem lógica.
- **B)** Correta. Constrói e relaciona as linhas, filtra linhas, forma e filtra grupos, projeta e só então ordena.
- **C)** Incorreta. Coloca a projeção antes da construção da tabela lógica e troca `GROUP BY` com `HAVING`.
- **D)** Incorreta. Filtra antes de construir a entrada e posiciona `ON` depois do agrupamento.

**Conceito:** Ordem lógica de processamento.

**Pegadinha:** Confundir a ordem escrita, que começa em `SELECT`, com a ordem lógica.

**Como pensar:** Comece pela tabela produzida por `FROM/JOIN`; depois acompanhe linha, grupo, projeção e ordenação.

### Comentário S3D3Q102

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Ana, Bruno e Davi passam pelo `WHERE`; as três ocorrências de PR tornam-se uma por `DISTINCT`.
- **B)** Incorreta. Essa é a projeção antes de eliminar duplicatas, não o resultado final.
- **C)** Incorreta. `DISTINCT` pode atuar depois do filtro e sobre a lista projetada.
- **D)** Incorreta. SC pertence a Carla, eliminada pelo filtro de ativos.

**Conceito:** Projeção distinta.

**Pegadinha:** Manter UF de linha filtrada ou preservar duplicatas depois de `DISTINCT`.

**Como pensar:** Filtre Ana, Bruno e Davi; projete suas UFs; elimine repetições e ordene.

### Comentário S3D3Q103

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A expressão não é um teste de coluna e a comparação ordinária de nulos não é verdadeira.
- **B)** Incorreta. A comparação ordinária com `NULL` resulta em desconhecido e não é conservada pelo `WHERE`.
- **C)** Incorreta. Também produz desconhecido; não significa “diferente de valor conhecido”.
- **D)** Correta. `IS NULL` testa a ausência e retorna Davi.

**Conceito:** Predicado `IS NULL`.

**Pegadinha:** Tratar `NULL` como valor comparável por `=` ou `<>`.

**Como pensar:** Quando a pergunta for ausência, procure `IS NULL`; no conjunto, a única linha correspondente é Davi.

### Comentário S3D3Q104

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Essa é a expansão inclusiva ensinada.
- **B)** Incorreta. `BETWEEN` é inclusivo nas duas extremidades.
- **C)** Incorreta. O intervalo exige conjunção, não disjunção.
- **D)** Incorreta. 120 também integra o intervalo.

**Conceito:** Predicado `BETWEEN`.

**Pegadinha:** Importar a ideia de intervalo aberto sem ler a regra.

**Como pensar:** Substitua mentalmente `BETWEEN a AND b` por duas comparações inclusivas ligadas por `AND`.

### Comentário S3D3Q105

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. `WHERE` aceita expressões booleanas construídas com cálculos.
- **B)** Incorreta. `GROUP BY` não corrige a visibilidade do alias nem é necessário sem agrupamento.
- **C)** Correta. Relaciona corretamente a indisponibilidade do alias à ordem lógica.
- **D)** Incorreta. Confunde posição textual com momento lógico de avaliação.

**Conceito:** Alias e ordem lógica.

**Pegadinha:** Tomar a ordem escrita como prova de que o alias já foi calculado.

**Como pensar:** Localize a etapa que cria o alias (`SELECT`) e compare-a com a etapa que tenta lê-lo (`WHERE`).

### Comentário S3D3Q106

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Carla satisfaz a diferença, mas Davi satisfaz o segundo termo.
- **B)** Correta. Carla tem unidade 20; Davi tem ausência explicitamente aceita; Ana e Bruno têm 10.
- **C)** Incorreta. Ana e Bruno falham em ambos os termos; não são incluídos por Davi ser nulo.
- **D)** Incorreta. Davi é incluído, mas Carla também satisfaz `20 <> 10`.

**Conceito:** Lógica de três valores com tratamento explícito.

**Pegadinha:** Esperar que `NULL <> 10` seja verdadeiro ou esquecer o segundo termo.

**Como pensar:** Avalie cada termo por linha: diferença verdadeira inclui Carla; `IS NULL` inclui Davi.

### Comentário S3D3Q107

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Muda a expressão e permitiria qualquer linha da unidade 10.
- **B)** Incorreta. Dá precedência indevida ao `OR`.
- **C)** Incorreta. Troca o primeiro operador e agrupa outra expressão.
- **D)** Correta. `AND` tem precedência sobre `OR`; Carla entra por estar inativa e Ana/Bruno entram pelo segundo conjunto.

**Conceito:** Precedência de operadores lógicos.

**Pegadinha:** Ler operadores apenas da esquerda para a direita.

**Como pensar:** Agrupe primeiro o `AND`; depois una seu resultado ao termo ligado por `OR`.

### Comentário S3D3Q108

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Esquema e dados de treino](semana_03_estudo.md#s3-d3-esquema-treino) e [agregação](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. As linhas 101, 103 e 104 passam pelo `WHERE`, logo a contagem é 3.
- **B)** Incorreta. Há três linhas pagas, não apenas a de Ana.
- **C)** Incorreta. Ana, Bruno e Carla possuem uma linha paga cada.
- **D)** Incorreta. Quatro é o total de pagamentos antes do filtro.

**Conceito:** Filtragem seguida de contagem.

**Pegadinha:** Contar profissionais ou pagamentos totais em vez das linhas filtradas.

**Como pensar:** Liste as linhas com status PAGO e só então aplique `COUNT(*)`: 101, 103 e 104.

### Comentário S3D3Q109

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não há pagamento sem profissional que crie quinta correspondência.
- **B)** Incorreta. Uma junção não reduz todos os pares a um único resultado.
- **C)** Correta. Cada uma das quatro linhas de pagamento encontra exatamente um profissional; Ana aparece duas vezes.
- **D)** Incorreta. Três é o número de profissionais com pagamento, não o número de pares.

**Conceito:** Cardinalidade de junção.

**Pegadinha:** Contar entidades distintas quando a granularidade da saída é pagamento.

**Como pensar:** Parta da tabela de detalhe: cada pagamento encontra um profissional, totalizando quatro pares.

### Comentário S3D3Q110

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. `COUNT(pg.id)` ignora o nulo; somente `COUNT(*)` contaria a linha estendida.
- **B)** Incorreta. Ana possui duas ocorrências de pagamento.
- **C)** Incorreta. A junção externa preserva Davi.
- **D)** Correta. As três correspondências são contadas e o identificador nulo da linha estendida de Davi não é contado.

**Conceito:** LEFT JOIN com `COUNT(coluna)`.

**Pegadinha:** Confundir linha preservada com detalhe existente.

**Como pensar:** Preserve os quatro profissionais; conte somente `pg.id` não nulo em cada grupo.

### Comentário S3D3Q111

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O filtro posterior remove as linhas estendidas com nulos e desfaz a preservação.
- **B)** Correta. Restringe a correspondência em `ON` e preserva toda linha da esquerda; Ana recebe 120 e os demais, nulo.
- **C)** Incorreta. Cria produto cartesiano com o pagamento aberto.
- **D)** Incorreta. Elimina profissionais sem correspondência aberta.

**Conceito:** Filtro em `ON` versus `WHERE`.

**Pegadinha:** Escolher `LEFT` no texto, mas neutralizá-lo com filtro direito em `WHERE`.

**Como pensar:** Identifique o lado obrigatório; condições do detalhe opcional ficam em `ON`.

### Comentário S3D3Q112

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Soma as cardinalidades em vez de multiplicá-las.
- **B)** Correta. O produto cartesiano combina cada um dos 4 profissionais com cada uma das 3 unidades: 4 × 3 = 12.
- **C)** Incorreta. Considera apenas um lado.
- **D)** Incorreta. Considera apenas o outro lado.

**Conceito:** `CROSS JOIN`.

**Pegadinha:** Somar tamanhos de conjuntos quando a operação produz pares.

**Como pensar:** Multiplique as quantidades dos dois lados quando não houver filtro.

### Comentário S3D3Q113

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A linha externa existe e é contada por estrela.
- **B)** Incorreta. O identificador direito é nulo e não entra em `COUNT(pg.id)`.
- **C)** Incorreta. Contagens retornam número, não nulo nesse agrupamento.
- **D)** Correta. A primeira conta a linha preservada; a segunda ignora o valor nulo.

**Conceito:** Contagem de linhas e valores.

**Pegadinha:** Equiparar linha estendida a ocorrência real da tabela direita.

**Como pensar:** Pergunte primeiro se a linha existe; depois se a expressão contada tem valor não nulo.

### Comentário S3D3Q114

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Carla está em Registro, mas é inativa e sai no `WHERE`.
- **B)** Correta. Ana e Bruno são ativos da Fiscalização; o grupo tem duas linhas e passa no `HAVING`.
- **C)** Incorreta. Tecnologia não possui profissional no conjunto e a junção interna não cria linha.
- **D)** Incorreta. O grupo Fiscalização satisfaz a condição.

**Conceito:** Filtro de linhas e filtro de grupos.

**Pegadinha:** Contar Carla antes do `WHERE` ou inventar linha em unidade vazia.

**Como pensar:** Filtre ativos; forme grupos por unidade; conte e aplique o limite.

### Comentário S3D3Q115

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Um grupo por UF pode conter vários nomes; não existe um único nome definido para projetar.
- **B)** Incorreta. `HAVING` é opcional quando nenhum grupo precisa ser filtrado.
- **C)** Incorreta. Contagem não exige `DISTINCT`.
- **D)** Incorreta. `uf` é justamente a chave de agrupamento usada.

**Conceito:** Granularidade de agrupamento.

**Pegadinha:** Projetar detalhe sem decidir como reduzi-lo ao nível do grupo.

**Como pensar:** Para cada coluna do `SELECT`, pergunte se ela identifica o grupo ou se foi agregada.

### Comentário S3D3Q116

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Valores nulos não compõem a média como observações zero.
- **B)** Incorreta. Agregados podem operar sobre conjunto que contenha valores e nulos.
- **C)** Correta. A formulação preserva a diferença entre ausência e valor zero.
- **D)** Incorreta. A teoria proíbe presumir conversão automática de nulo em zero.

**Conceito:** Agregação e nulidade.

**Pegadinha:** Converter ausência em zero sem regra de negócio.

**Como pensar:** Separe “não participar do cálculo” de “participar com valor zero”.

### Comentário S3D3Q117

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Carla possui apenas pagamento pago.
- **B)** Incorreta. Davi não possui pagamento.
- **C)** Correta. Ana possui a linha 102 aberta, então sua subconsulta correlacionada encontra uma ocorrência.
- **D)** Incorreta. Bruno possui apenas pagamento pago.

**Conceito:** `EXISTS` correlacionado.

**Pegadinha:** Olhar qualquer pagamento aberto sem correlacioná-lo ao profissional externo.

**Como pensar:** Para cada profissional, procure ao menos uma linha com a mesma chave e o status exigido.

### Comentário S3D3Q118

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Davi não tem linha em PAGAMENTO e passa pela negação da existência.
- **B)** Incorreta. Bruno possui o pagamento 103.
- **C)** Incorreta. Ana possui dois pagamentos.
- **D)** Incorreta. Carla possui o pagamento 104.

**Conceito:** Antijunção.

**Pegadinha:** Confundir “sem pagamento aberto” com “sem qualquer pagamento”.

**Como pensar:** Teste a subconsulta para cada chave; somente Davi produz conjunto vazio.

### Comentário S3D3Q119

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A presença de nulo pode contaminar a conjunção de desigualdades; a correlação de `NOT EXISTS` evita essa armadilha.
- **B)** Incorreta. A construção é válida, desde que a nulidade seja compreendida/controlada.
- **C)** Incorreta. Duplicatas não explicam o problema central.
- **D)** Incorreta. Não existe essa conversão automática.

**Conceito:** `NOT IN` e lógica de três valores.

**Pegadinha:** Aplicar intuição de conjuntos clássicos sem considerar desconhecido.

**Como pensar:** Antes de usar `NOT IN`, prove que a saída é não nula; caso contrário, formule ausência com `NOT EXISTS`.

### Comentário S3D3Q120

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Número de colunas não define correlação.
- **B)** Correta. A referência externa cria a dependência que caracteriza a correlação.
- **C)** Incorreta. Agregação pode existir em subconsulta correlacionada ou não.
- **D)** Incorreta. Uma não correlacionada pode ser independente; a correlacionada depende da linha externa no modelo lógico.

**Conceito:** Correlação de subconsulta.

**Pegadinha:** Definir correlação pela forma ou tamanho do resultado.

**Como pensar:** Procure um alias da consulta externa dentro da subconsulta.

### Comentário S3D3Q121

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. `EXCEPT`, não `UNION`, poderia remover PR do primeiro conjunto.
- **B)** Correta. `UNION` reúne os resultados e elimina ocorrências duplicadas.
- **C)** Incorreta. Essa é a multiplicidade de `UNION ALL`.
- **D)** Incorreta. SC também pertence ao primeiro resultado.

**Conceito:** Operação `UNION`.

**Pegadinha:** Tratar `UNION` como concatenação que preserva multiplicidades.

**Como pensar:** Concatene conceitualmente e depois retenha uma ocorrência de cada linha.

### Comentário S3D3Q122

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não há redução a uma linha.
- **B)** Incorreta. Dois seria o resultado distinto.
- **C)** Correta. `ALL` preserva as três ocorrências da primeira consulta e a ocorrência da segunda.
- **D)** Incorreta. Três desconsidera a segunda ocorrência de PR.

**Conceito:** `UNION ALL`.

**Pegadinha:** Achar que `ALL` altera apenas desempenho.

**Como pensar:** Conte todas as ocorrências de ambos os lados: 3 + 1.

### Comentário S3D3Q123

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Há uma ocorrência comum.
- **B)** Incorreta. SC não está no segundo conjunto.
- **C)** Incorreta. Essa seria a união.
- **D)** Correta. PR é a única linha presente nos dois resultados.

**Conceito:** `INTERSECT`.

**Pegadinha:** Inverter interseção com diferença.

**Como pensar:** Marque apenas elementos presentes simultaneamente nos dois lados.

### Comentário S3D3Q124

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. `EXCEPT` conserva linhas do primeiro resultado ausentes no segundo.
- **B)** Incorreta. PR é removido porque aparece no segundo conjunto.
- **C)** Incorreta. Não é uma união.
- **D)** Incorreta. SC permanece, portanto o resultado não é vazio.

**Conceito:** `EXCEPT`.

**Pegadinha:** Esquecer que a diferença tem direção.

**Como pensar:** Comece pelo primeiro conjunto e risque tudo que também aparece no segundo.

### Comentário S3D3Q125

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Remove duplicatas, não define ordem final.
- **B)** Incorreta. Forma grupos, mas não garante a sequência de apresentação.
- **C)** Incorreta. Plano e armazenamento podem mudar; aparência observada não é garantia.
- **D)** Correta. É a cláusula contratual de ordenação do resultado.

**Conceito:** Ordenação de resultado.

**Pegadinha:** Confiar na ordem em que linhas apareceram em uma execução.

**Como pensar:** Se a ordem importa para o requisito, procure `ORDER BY` explícito.

### Comentário S3D3Q126

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Alias não é predicado.
- **B)** Incorreta. Renomear estrutura exigiria DDL, não um alias de consulta.
- **C)** Correta. O alias pertence ao resultado daquela consulta.
- **D)** Incorreta. A projeção não materializa coluna física por si só.

**Conceito:** Alias de expressão.

**Pegadinha:** Confundir nome de saída com mudança de esquema.

**Como pensar:** Separe metadado do resultado temporário de definição persistente da tabela.

### Comentário S3D3Q127

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Projeção, DISTINCT e ORDER BY](semana_03_estudo.md#s3-d3-projecao-distinct-order).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Coluna não projetada não define duplicidade dessa saída.
- **B)** Incorreta. O segundo atributo também participa.
- **C)** Incorreta. O primeiro atributo também participa.
- **D)** Correta. Duas linhas são duplicadas na saída apenas se a dupla projetada coincidir.

**Conceito:** `DISTINCT` sobre múltiplas expressões.

**Pegadinha:** Aplicar distinção separadamente a cada coluna.

**Como pensar:** Escreva a tupla de saída e compare a tupla inteira.

### Comentário S3D3Q128

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Todas as quatro linhas possuem um dos dois status listados.
- **B)** Incorreta. Há mais de um pagamento pago.
- **C)** Incorreta. Além dos pagos, existe uma linha aberta.
- **D)** Incorreta. Três conta apenas os pagos.

**Conceito:** Predicado `IN`.

**Pegadinha:** Contar somente o primeiro valor da lista.

**Como pensar:** Avalie cada status como igualdade com qualquer membro do conjunto.

### Comentário S3D3Q129

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. `ON` decide correspondências da junção, não filtra agregado dessa forma.
- **B)** Incorreta. `DISTINCT` não substitui contagem e limite.
- **C)** Correta. O status é condição de linha; a quantidade é condição do grupo.
- **D)** Incorreta. Agregado não pertence ao `WHERE`, e o status não precisa esperar o grupo.

**Conceito:** Filtro de linha e de grupo.

**Pegadinha:** Trocar `WHERE` e `HAVING` porque ambos eliminam resultados.

**Como pensar:** Pergunte se a condição conhece uma linha individual ou depende do grupo já calculado.

### Comentário S3D3Q130

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Roteiro de rastreamento manual](semana_03_estudo.md#s3-d3-pratica) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O `WHERE` mantém Ana, Bruno e Davi; os pagamentos não nulos são dois de Ana e um de Bruno: 3.
- **B)** Incorreta. Carla é inativa e SC não forma grupo.
- **C)** Incorreta. SC desaparece no filtro; PR não conta linha nula de Davi.
- **D)** Incorreta. Quatro é a quantidade de linhas antes de eliminar Carla; Davi não adiciona `pg.id`.

**Conceito:** Rastreamento de junção, filtro e agrupamento.

**Pegadinha:** Contar linhas da tabela base ou `COUNT(*)` sem acompanhar a expressão contada.

**Como pensar:** Materialize: junção → retire Carla → forme PR → conte os três `pg.id` não nulos.

### Comentário S3D3Q131

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Seleção e projeção](semana_03_estudo.md#s3-d3-selecao-projecao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Duplicidade e junção são dimensões distintas.
- **B)** Incorreta. Ordenação é função de `ORDER BY`.
- **C)** Incorreta. São operações de consulta, não DDL destrutiva.
- **D)** Correta. `WHERE` realiza seleção de linhas e `SELECT` define a projeção da saída.

**Conceito:** Seleção e projeção.

**Pegadinha:** Confundir os nomes pela cláusula `SELECT`.

**Como pensar:** Associe predicado a linhas e lista de saída a colunas.

### Comentário S3D3Q132

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não decorre de 4 × 3.
- **B)** Correta. O estágio `FROM/CROSS JOIN` cria 12 combinações; o `WHERE` atua depois.
- **C)** Incorreta. Duas é a quantidade após o filtro informado.
- **D)** Incorreta. Soma não modela produto cartesiano.

**Conceito:** Ordem lógica e produto cartesiano.

**Pegadinha:** Responder com a cardinalidade final quando a pergunta pede tabela intermediária.

**Como pensar:** Congele o processamento na etapa indicada: antes do filtro, multiplique 4 por 3.

### Comentário S3D3Q133

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Chaves ajudam, mas sua ausência não define self-join.
- **B)** Incorreta. Pode haver condição explícita.
- **C)** Correta. Aliases permitem atribuir papéis diferentes à mesma tabela, como empregado e supervisor.
- **D)** Incorreta. A condição costuma relacionar linhas diferentes da mesma relação.

**Conceito:** Self-join.

**Pegadinha:** Interpretar “self” como comparar cada linha apenas com ela própria.

**Como pensar:** Procure a mesma tabela citada duas vezes com papéis e aliases diferentes.

### Comentário S3D3Q134

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A operação pode encontrar nomes comuns.
- **B)** Correta. Uma nova coluna homônima pode alterar silenciosamente o critério de junção.
- **C)** Incorreta. Havendo nomes comuns, não é produto cartesiano.
- **D)** Incorreta. A projeção não é descrita por essa afirmação absoluta.

**Conceito:** `NATURAL JOIN`.

**Pegadinha:** Confundir concisão sintática com estabilidade semântica.

**Como pensar:** Prefira listar chaves em `ON` e pergunte o que aconteceria se surgisse nova coluna de mesmo nome.

### Comentário S3D3Q135

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Nenhum valor de pagamento participa da contagem.
- **B)** Incorreta. A construção é válida.
- **C)** Incorreta. `COUNT` retorna número de valores não nulos.
- **D)** Incorreta. A linha externa existe, mas `pg.valor` é nulo.

**Conceito:** `COUNT(expressão)`.

**Pegadinha:** Confundir a linha estendida com um valor existente.

**Como pensar:** Conte somente valores não nulos da expressão escolhida.

### Comentário S3D3Q136

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não há conversão geral ensinada.
- **B)** Incorreta. Nulos não entram como observações zero.
- **C)** Incorreta. Agregados diferem; a teoria alerta contra essa generalização.
- **D)** Correta. A alternativa preserva a semântica entre ausência e zero.

**Conceito:** Semântica de agregados.

**Pegadinha:** Usar zero como substituto universal de desconhecido/ausente.

**Como pensar:** Declare primeiro a regra de negócio; só então decida se ausência deve ser convertida.

### Comentário S3D3Q137

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Bruno e Carla também possuem pagamento pago.
- **B)** Correta. Ana, Bruno e Carla têm linha paga; Davi tem a linha preservada com `pg.id` nulo. A linha aberta de Ana é eliminada, mas sua linha paga permanece.
- **C)** Incorreta. Esquece que o segundo termo preserva Davi.
- **D)** Incorreta. Esquece as linhas pagas.

**Conceito:** Filtro posterior com preservação explícita.

**Pegadinha:** Achar que todo `WHERE` sobre a direita elimina necessariamente a linha nula, mesmo quando ela é aceita.

**Como pensar:** Materialize as linhas da junção; aplique cada lado do `OR` a cada ocorrência.

### Comentário S3D3Q138

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A junção interna elimina a ausência antes do filtro.
- **B)** Incorreta. Produto cartesiano não cria linha direita nula.
- **C)** Incorreta. A linha esquerda sempre possui seu identificador.
- **D)** Correta. A ausência de correspondência gera nulos nas colunas da direita; testar a chave direita identifica Davi.

**Conceito:** Antijunção com outer join.

**Pegadinha:** Testar a chave do lado preservado ou usar junção que elimina ausências.

**Como pensar:** Preserve a esquerda e teste uma coluna direita garantidamente não nula nas correspondências reais.

### Comentário S3D3Q139

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Roteiro de rastreamento manual](semana_03_estudo.md#s3-d3-pratica) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A granularidade após as duas junções é pagamento; Ana duplica e Bruno aparece uma vez.
- **B)** Incorreta. Agrupamento produz uma linha de saída, mas o agregado conta linhas de entrada.
- **C)** Incorreta. Seria necessário `COUNT(DISTINCT p.id)` para contar profissionais distintos.
- **D)** Incorreta. O pagamento de Carla pertence a Registro, não Fiscalização.

**Conceito:** Explosão de cardinalidade em junções.

**Pegadinha:** Contar entidades conceituais sem observar a granularidade intermediária.

**Como pensar:** Desenhe as linhas após cada junção; só depois escolha entre `COUNT` e `COUNT(DISTINCT ...)`.

### Comentário S3D3Q140

**Nível:** Médio

**Uso:** Revisão

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Aliases não precisam ser idênticos para compatibilidade.
- **B)** Incorreta. Quantidade de linhas pode variar.
- **C)** Correta. A compatibilidade é definida pela aridade e pelos tipos posicionais.
- **D)** Incorreta. Fontes diferentes podem ser combinadas.

**Conceito:** Compatibilidade de conjuntos.

**Pegadinha:** Comparar nomes ou número de linhas em vez da estrutura projetada.

**Como pensar:** Alinhe primeira coluna com primeira, segunda com segunda, verificando quantidade e tipo.

### Comentário S3D3Q141

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Produto cartesiano não relaciona profissional à unidade.
- **B)** Correta. O filtro de ativo restringe correspondências em `ON`; o teste da chave direita seleciona Registro e Tecnologia, que não têm ativo correspondente.
- **C)** Incorreta. Encontra unidade com inativo, mas perde unidade vazia e não prova ausência de ativo.
- **D)** Incorreta. O `WHERE` elimina unidade vazia e seleciona apenas linha inativa.

**Conceito:** Antijunção com condição de correspondência.

**Pegadinha:** Confundir “tem inativo” com “não tem ativo”.

**Como pensar:** Defina a correspondência proibida (profissional ativo), preserve unidades e conserve as que não encontraram essa linha.

### Comentário S3D3Q142

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O produto cartesiano atribui pagamentos a profissionais errados.
- **B)** Incorreta. A junção interna elimina Davi.
- **C)** Correta. A condição em `ON` aceita somente pagos como correspondência e mantém cada profissional; `SUM(pg.valor)` resulta 120, 200, 150 e nulo.
- **D)** Incorreta. O filtro posterior remove a linha nula de Davi.

**Conceito:** Agregação sobre detalhe opcional.

**Pegadinha:** Usar `LEFT` e depois desfazer sua preservação no `WHERE`.

**Como pensar:** Coloque a condição do detalhe opcional em `ON`, agrupe pela chave esquerda e interprete o nulo separadamente de zero.

### Comentário S3D3Q143

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [WHERE, predicados e lógica de três valores](semana_03_estudo.md#s3-d3-where-null).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Correta. Está correta: os dois termos tratam casos distintos.
- **B)** Correta. Está correta: essa é a regra de seleção do `WHERE`.
- **C)** Correta. Está correta: é o predicado próprio de presença.
- **D)** Incorreta. Está incorreta: comparação ordinária com `NULL` resulta em desconhecido; usa-se `IS NULL`.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** Lógica de três valores.

**Pegadinha:** No comando negativo, marcar uma afirmação verdadeira por hábito de procurar a correta.

**Como pensar:** Teste cada afirmação; a única que trata nulo como valor comparável é a incorreta.

### Comentário S3D3Q144

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. I, III e IV seguem a ordem lógica; II é falsa porque `HAVING` atua sobre grupos.
- **B)** Incorreta. II é falsa e III é verdadeira.
- **C)** Incorreta. II é falsa e I também é verdadeira.
- **D)** Incorreta. Inclui II, que situa `HAVING` antes da junção.

**Conceito:** Ordem lógica integrada.

**Pegadinha:** Validar cada cláusula isoladamente sem posicioná-la no fluxo.

**Como pensar:** Desenhe o fluxo completo e teste as quatro afirmações nele.

### Comentário S3D3Q145

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Contagens resultam em números.
- **B)** Correta. A linha de Tecnologia é preservada; estrela conta a linha estendida e `p.id` nulo não é contado.
- **C)** Incorreta. A primeira contagem ignora que há linha preservada.
- **D)** Incorreta. A segunda contagem não inclui chave nula.

**Conceito:** Contagem após preservação.

**Pegadinha:** Confundir ausência de detalhe com ausência da linha esquerda.

**Como pensar:** Materialize uma linha de Tecnologia com colunas direitas nulas e aplique cada contagem.

### Comentário S3D3Q146

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A cardinalidade externa depende da correlação/predicado, não de `*` por si só.
- **B)** Incorreta. Não há soma.
- **C)** Correta. A condição termina quando encontra linha correlata; a projeção não define a verdade da existência.
- **D)** Incorreta. Outras projeções são sintaticamente possíveis.

**Conceito:** Semântica de `EXISTS`.

**Pegadinha:** Atribuir significado aritmético ao literal 1.

**Como pensar:** Ignore o valor selecionado e pergunte apenas se a subconsulta encontra alguma linha.

### Comentário S3D3Q147

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Roteiro de rastreamento manual](semana_03_estudo.md#s3-d3-pratica).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Após a junção com pagamentos, cada linha representa ocorrência de pagamento, não necessariamente profissional distinto.
- **B)** Incorreta. Falha no filtro de status e permite duplicação do profissional.
- **C)** Incorreta. A granularidade é profissional e a contagem de unidades não representa o requisito.
- **D)** Correta. Aplica os filtros de atividade e status, fixa a unidade como grão e distingue profissionais antes de contar pagamentos; Fiscalização satisfaz o caso.

**Conceito:** Agregação multifiltro e granularidade.

**Pegadinha:** Usar a mesma contagem para entidades e ocorrências em uma junção 1:N.

**Como pensar:** Verifique separadamente: linhas elegíveis, grão do grupo, profissionais distintos e pagamentos.

### Comentário S3D3Q148

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O requisito exige ausência de aberto, não presença.
- **B)** Correta. Bruno é ativo, PR, possui a linha 103 paga e nenhuma linha aberta; os dois testes de existência devem usar sua chave.
- **C)** Incorreta. Ana falha no quarto filtro porque possui a linha 102 aberta.
- **D)** Incorreta. Davi falha no terceiro filtro, pois não possui pagamento pago.

**Conceito:** Combinação de `EXISTS` e `NOT EXISTS`.

**Pegadinha:** Interpretar ausência de um status como prova de presença do outro.

**Como pensar:** Aplique os quatro filtros em sequência e não una existência e ausência em uma única negação ambígua.

### Comentário S3D3Q149

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Inverte os efeitos das etapas.
- **B)** Incorreta. A condição PAGO elimina a linha aberta nas duas formas.
- **C)** Correta. Q1 restringe correspondências antes de preservar Davi; Q2 filtra depois e remove a linha nula. O pagamento aberto não casa em Q1 nem passa em Q2.
- **D)** Incorreta. Ignora o efeito do filtro posterior.

**Conceito:** Outer join, posição do filtro e cardinalidade.

**Pegadinha:** Parar a análise na palavra `LEFT` sem percorrer o `WHERE`.

**Como pensar:** Materialize Q1 e Q2 separadamente: correspondência, linha estendida e filtro posterior.

### Comentário S3D3Q150

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos) e [esquema de treino](semana_03_estudo.md#s3-d3-esquema-treino).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A contém somente PR; B contém PR; a diferença elimina a única linha.
- **B)** Incorreta. SC não pertence a A porque Carla é inativa.
- **C)** Incorreta. A não contém SC, e PR não sobrevive à diferença.
- **D)** Incorreta. PR pertence a A, mas também a B por causa de Ana e é removido.

**Conceito:** Filtros, duplicatas e diferença de conjuntos.

**Pegadinha:** Calcular os conjuntos sem aplicar seus filtros ou inverter a direção do `EXCEPT`.

**Como pensar:** Construa A e B separadamente, aplique `DISTINCT` e só então risque de A o que aparece em B.

#### Comentário Extra Dia 3.1

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Separa artificialmente o reconhecimento profissional da criação legal dos Conselhos.
- **B)** Incorreta. Inverte a hierarquia e a cronologia: o decreto regulamenta a lei, não a origina.
- **C)** Incorreta. Resoluções podem detalhar a atuação, mas não substituem a fonte legal de criação do sistema.
- **D)** Correta. Reproduz o papel normativo indicado na revisão.

**Conceito:** Fonte legal do sistema.

**Pegadinha:** Trocar a função de lei, decreto e regimento.

**Como pensar:** Classifique a fonte antes de atribuir seu objeto.

**Justificativa de comprimento:** A correta sintetiza a atribuição legal; os distratores precisam explicitar trocas plausíveis entre lei, decreto e resolução.

#### Comentário Extra Dia 3.2

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Competência regional não prevalece sobre lei.
- **B)** Incorreta. Inverte âmbitos.
- **C)** Correta. Distingue o alcance nacional do conselho federal e a atuação regional.
- **D)** Incorreta. Ignora o sistema integrado.

**Conceito:** Âmbito e competência.

**Pegadinha:** Atribuir função nacional ao órgão regional.

**Como pensar:** Pergunte primeiro se a atuação é nacional ou territorialmente regional.

#### Comentário Extra Dia 3.3

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O Código de Ética, e não o regimento interno regional, disciplina o recorte ético nacional.
- **B)** Incorreta. A regulamentação nacional da lei não é a função central do regimento do CRA-PR.
- **C)** Incorreta. A orientação normativa nacional cabe ao CFA; o regimento organiza o órgão regional.
- **D)** Correta. Esse é o objeto indicado na revisão.

**Conceito:** Objeto do regimento.

**Pegadinha:** Superestimar a hierarquia de norma interna.

**Como pensar:** Associe regimento a estrutura, competências e funcionamento do próprio órgão.

#### Comentário Extra Dia 3.4

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Autonomia administrativa e financeira não afasta a orientação e a supervisão nacionais.
- **B)** Incorreta. Custo administrativo não torna facultativa uma diretriz nacional válida.
- **C)** Incorreta. A gestão regional continua sujeita ao ordenamento e à integração normativa do sistema.
- **D)** Correta. A alternativa preserva autonomia e integração sem criar consequência indevida.

**Conceito:** Autonomia institucional.

**Pegadinha:** Tratar autonomia como soberania.

**Como pensar:** Separe capacidade de gestão própria de ruptura com a ordem jurídica e institucional.

**Justificativa de comprimento:** A correta enuncia diretamente a coexistência entre autonomia e integração; os distratores detalham falsas exceções à supervisão nacional.

#### Comentário Extra Dia 3.5

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É a função registrada na teoria.
- **B)** Incorreta. Restringe indevidamente o alcance e exclui os profissionais submetidos ao código.
- **C)** Incorreta. O próprio código disciplina deveres e infrações no âmbito que alcança.
- **D)** Incorreta. Regimentos internos não substituem a disciplina ética comum do sistema.

**Conceito:** Âmbito subjetivo da ética.

**Pegadinha:** Ignorar quem é o sujeito alcançado pela norma.

**Como pensar:** Antes do mérito, identifique a quem a regra ética se aplica.

#### Comentário Extra Dia 3.6

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Competência para fiscalizar o caso regional não transfere ao CRA-PR a orientação normativa nacional.
- **B)** Incorreta. A apuração regional convive com a função nacional do CFA; não a suspende.
- **C)** Correta. Distingue local do fato e nível da competência.
- **D)** Incorreta. O local do fato não autoriza regimento regional incompatível com normas superiores.

**Conceito:** Jurisdição regional.

**Pegadinha:** Confundir local do fato com titularidade de toda competência.

**Como pensar:** Classifique separadamente território do caso e alcance da atribuição.

#### Comentário Extra Dia 3.7

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Especialidade e data não autorizam ato administrativo inferior a afastar lei incompatível.
- **B)** Incorreta. Cronologia isolada não resolve conflito entre espécies de hierarquia diferente.
- **C)** Correta. A solução começa pela fonte e hierarquia.
- **D)** Incorreta. Autonomia regional não cria liberdade para escolher entre lei e resolução conflitantes.

**Conceito:** Hierarquia normativa.

**Pegadinha:** Aplicar apenas cronologia sem considerar a espécie normativa.

**Como pensar:** Compare fonte, competência e hierarquia antes da data.

#### Comentário Extra Dia 3.8

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Data e extensão da alternativa não substituem a identificação do sujeito e da competência.
- **B)** Correta. A sequência reproduz o método ensinado e filtra dimensões independentes.
- **C)** Incorreta. Prática e analogia não dispensam a verificação da fonte e da hierarquia.
- **D)** Incorreta. Deixar sujeito e competência em segundo plano impede concluir quem pode fazer o quê.

**Conceito:** Método de classificação.

**Pegadinha:** Escolher pelo nome do órgão sem examinar fonte e sujeito.

**Como pensar:** Percorra os quatro filtros antes de avaliar a consequência.

#### Comentário Extra Dia 3.9

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Incorreta. Está incorreta: autonomia regional não transfere automaticamente a função normativa nacional.
- **B)** Correta. Está correta e limita a atuação regional.
- **C)** Correta. Está correta conforme a revisão.
- **D)** Correta. Está correta; distinguir fontes evita inversão de hierarquia.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Autonomia, âmbito e competência.

**Pegadinha:** No comando negativo, escolher a frase verdadeira mais específica.

**Como pensar:** Teste se a autonomia altera âmbito, hierarquia e função; somente a afirmação de substituição da competência nacional extrapola os três.

#### Comentário Extra Dia 3.10

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_03_estudo.md#s3-d3-b4-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Fiscalização regional não altera automaticamente o âmbito do CFA.
- **B)** Incorreta. Autonomia não produz os dois efeitos.
- **C)** Correta. Aplica os filtros de hierarquia e competência a cada proposição.
- **D)** Incorreta. Norma interna não recebe prevalência absoluta.

**Conceito:** Hierarquia e competência integradas.

**Pegadinha:** Aceitar duas conclusões porque compartilham a palavra “regional”.

**Como pensar:** Resolva cada eixo: posição da fonte e alcance da atribuição.

#### Comentário Extra Dia 3.11

**Nível:** Médio

**Uso:** Revisão

**Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mantém proposições positivas.
- **B)** Incorreta. Exige que ambos falhem, mais forte que a negação.
- **C)** Incorreta. Transforma a conjunção em implicação.
- **D)** Correta. Pela lei de De Morgan, negar `p e q` resulta em `não p ou não q`.

**Conceito:** Negação de conjunção.

**Pegadinha:** Trocar `e` por `e` após negar os termos.

**Como pensar:** Negue cada termo e troque `e` por `ou`.

#### Comentário Extra Dia 3.12

**Nível:** Médio

**Uso:** Revisão

**Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Uma implicação é falsa exatamente quando o antecedente ocorre e o consequente não.
- **B)** Incorreta. Nega também o antecedente e não caracteriza a falha da implicação.
- **C)** Incorreta. É uma nova implicação.
- **D)** Incorreta. A disjunção não fixa o contraexemplo.

**Conceito:** Negação de implicação.

**Pegadinha:** Usar contrapositiva ou negar os dois termos.

**Como pensar:** Construa o único contraexemplo: `p` verdadeiro e `q` falso.

#### Comentário Extra Dia 3.13

**Nível:** Médio

**Uso:** Revisão

**Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Afirma ausência total, muito mais forte.
- **B)** Incorreta. Muda o universo e a propriedade.
- **C)** Incorreta. Inverte a relação, sem negar a sentença.
- **D)** Correta. Basta um contraexemplo ao universal.

**Conceito:** Negação de universal.

**Pegadinha:** Trocar “todos” por “nenhum”.

**Como pensar:** Negue o universal com um existencial e negue a propriedade.

#### Comentário Extra Dia 3.14

**Nível:** Médio

**Uso:** Revisão

**Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Um único relatório com erro refuta “nenhum”.
- **B)** Incorreta. Essa sentença é compatível com a original e não a nega.
- **C)** Incorreta. Modalidade vaga não é a negação lógica.
- **D)** Incorreta. Universal positivo é mais forte que o necessário.

**Conceito:** Negação de quantificador negativo.

**Pegadinha:** Converter “nenhum” em “todos”.

**Como pensar:** Procure um contraexemplo existente à ausência total.

#### Comentário Extra Dia 3.15

**Nível:** Médio

**Uso:** Revisão

**Referência:** [RLM](semana_03_estudo.md#s3-d3-b4-rlm).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Mantém disjunção e permite que um termo continue verdadeiro.
- **B)** Incorreta. É a conjunção positiva.
- **C)** Correta. Negar `p ou q` resulta em `não p e não q`.
- **D)** Incorreta. Cria implicação diferente.

**Conceito:** Negação de disjunção.

**Pegadinha:** Negar os termos sem trocar o conectivo.

**Como pensar:** Troque `ou` por `e` e negue ambos.

#### Comentário Extra Dia 3.16

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não encerra o raciocínio.
- **B)** Correta. Reconhece uma informação que não impede a conclusão principal.
- **C)** Incorreta. Não explica a causa do segundo fato.
- **D)** Incorreta. Não apresenta efeito.

**Conceito:** Relação concessiva.

**Pegadinha:** Ler toda relação entre orações como causa.

**Como pensar:** Pergunte se o primeiro fato é admitido apesar de a conclusão seguir em outra direção.

#### Comentário Extra Dia 3.17

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Descarta relação possível sem base.
- **B)** Correta. Mantém o limite da evidência sem negar investigação posterior.
- **C)** Incorreta. Salta de associação para causa.
- **D)** Incorreta. Inverte e mantém o mesmo salto.

**Conceito:** Correlação versus causalidade.

**Pegadinha:** Transformar simultaneidade em causa comprovada.

**Como pensar:** Separe observação conjunta de mecanismo causal demonstrado.

#### Comentário Extra Dia 3.18

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Muda o sujeito responsável pela não publicação.
- **B)** Incorreta. “Aquela” ainda depende de inferência e “resultado” desaparece.
- **C)** Incorreta. O pronome continua podendo retomar equipe ou comissão.
- **D)** Correta. Nomeia explicitamente o referente e preserva o fato.

**Conceito:** Coesão referencial.

**Pegadinha:** Trocar um pronome ambíguo por outro pronome igualmente ambíguo.

**Como pensar:** Repita o núcleo nominal quando a economia prejudicar a identificação.

#### Comentário Extra Dia 3.19

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Apresenta efeito ou conclusão decorrente.
- **B)** Incorreta. Introduz causa ou explicação.
- **C)** Incorreta. Marca concessão.
- **D)** Incorreta. Marca oposição.

**Conceito:** Conector consequencial.

**Pegadinha:** Escolher conector pelo tom, sem identificar a relação.

**Como pensar:** Nomeie a relação desejada antes de selecionar a expressão.

#### Comentário Extra Dia 3.20

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português e progressão discursiva](semana_03_estudo.md#s3-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Cria causa contraditória e conclusão absoluta.
- **B)** Correta. Mantém concessão, explicita o referente relevante e evita inferência causal além das evidências.
- **C)** Incorreta. Converte concessão em causa e inverte a representatividade.
- **D)** Incorreta. Usa referente vago e transforma correlação em prova causal.

**Conceito:** Reescrita multifiltro.

**Pegadinha:** Preservar palavras do original, mas alterar relação lógica ou força da conclusão.

**Como pensar:** Cheque três filtros independentes: relação concessiva, referente claro e ausência de salto causal.

---

# Dia 4 - DDL, DML, Transact-SQL, views, procedures e triggers

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais - S3D4Q151 a S3D4Q200

### S3D4Q151 — Finalidade de DDL

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

Qual comando pertence à classe DDL pela finalidade apresentada na teoria?

A) `GRANT SELECT`.

B) `ROLLBACK TRANSACTION`.

C) `CREATE TABLE`.

D) `UPDATE cadastro`.

### S3D4Q152 — Operações de DML

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

Assinale o conjunto formado por comandos de manipulação/consulta de dados no recorte didático.

A) `GRANT`, `REVOKE`, `COMMIT`.

B) `ROLLBACK`, `SAVEPOINT`, `CREATE`.

C) `CREATE`, `ALTER`, `DROP`.

D) `SELECT`, `INSERT`, `UPDATE`, `DELETE`.

### S3D4Q153 — Garantia da chave primária

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Qual combinação descreve uma `PRIMARY KEY`?

A) Liga obrigatoriamente a tabela a outra relação.

B) Aceita duplicatas, mas não aceita nulos.

C) Impõe somente valor padrão.

D) Identifica cada linha, reunindo unicidade e não nulidade.

### S3D4Q154 — Chave estrangeira anulável

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Uma coluna `unidade_id` admite `NULL` e possui `FOREIGN KEY` para `unidade(id)`. Qual valor satisfaz a restrição referencial?

A) Apenas um identificador já excluído da tabela pai.

B) Chave existente no pai ou `NULL`, pois a coluna é opcional.

C) Qualquer número, mesmo sem unidade correspondente.

D) Somente `0`, usado como ausência.

### S3D4Q155 — DEFAULT e CHECK

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

A coluna `ativo` possui `DEFAULT 'S'` e `CHECK (ativo IN ('S','N'))`. O que ocorre conceitualmente quando um `INSERT` omite `ativo` e quando informa `'X'`?

A) Ambos recebem `'S'`, porque `DEFAULT` substitui qualquer valor inválido.

B) A omissão gera sempre `NULL`, e `'X'` é aceito pela chave primária.

C) O check escolhe automaticamente o valor mais próximo.

D) Omissão recebe `'S'`; `'X'` explícito é rejeitado pelo `CHECK`.

### S3D4Q156 — UNIQUE e nulidade

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Em questão sem SGBD definido, qual afirmação sobre `UNIQUE` e `NULL` é tecnicamente segura?

A) `UNIQUE` impõe unicidade; o tratamento de nulos varia por SGBD.

B) `UNIQUE` equivale sempre a `PRIMARY KEY`.

C) `UNIQUE` aceita obrigatoriamente infinitos nulos em qualquer SGBD.

D) `UNIQUE` sempre proíbe qualquer nulo em todos os produtos.

### S3D4Q157 — Migração segura para NOT NULL

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

Há linhas antigas com `unidade_id = NULL`, e a coluna passará a `NOT NULL`. Qual sequência é a mais segura?

A) Alterar primeiro e decidir depois o que fazer com as falhas.

B) Apagar todas as linhas nulas e aplicar a alteração sem validar dependências.

C) Localizar e tratar nulos, validar referências, alterar a coluna e preservar rollback.

D) Criar uma view com filtro e considerar a tabela corrigida.

### S3D4Q158 — Cautela com TRUNCATE

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

Por que não se deve afirmar, sem indicar o produto, que `TRUNCATE` é apenas um `DELETE` mais rápido?

A) Porque os dois são idênticos por definição ANSI.

B) Remove todas as linhas; efeitos internos variam por SGBD.

C) Porque `TRUNCATE` sempre aceita `WHERE`.

D) Porque `DELETE` nunca registra alterações.

### S3D4Q159 — UPDATE sem WHERE

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

Qual é o alcance de `UPDATE profissional SET ativo='N';`, sem cláusula `WHERE`?

A) Somente linhas que já eram inativas.

B) Nenhuma linha, porque `WHERE` é obrigatório.

C) Todas as linhas alcançadas recebem o novo valor.

D) Somente a primeira linha física.

### S3D4Q160 — Prévia com o mesmo predicado

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

Antes de excluir pagamentos cancelados anteriores a 2025, qual prática reduz o risco de alcance indevido?

A) Executar `SELECT` com o mesmo predicado e conferir quantidade e chaves.

B) Remover o `WHERE` para simplificar o rollback.

C) Criar uma trigger que aprove qualquer exclusão sem testar lotes.

D) Executar `DROP TABLE` para testar dependências.

### S3D4Q161 — DCL e TCL

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

Qual par associa corretamente classe e exemplos?

A) DDL — `GRANT` e `REVOKE`.

B) DML — `COMMIT` e `ROLLBACK`.

C) DCL: `GRANT`; TCL: `COMMIT`.

D) TCL — `CREATE`/`ALTER`.

### S3D4Q162 — Elementos reconhecíveis de T-SQL

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

No trecho `DECLARE @uf char(2)='PR'; SELECT TOP (10) ...`, qual leitura é adequada?

A) `@uf` é nome de tabela temporária ANSI e `TOP` ordena automaticamente.

B) `@uf` é variável local e `TOP (10)` limita a saída; quais dez linhas são escolhidas de modo determinístico depende de uma ordenação total em `ORDER BY`.

C) `TOP` é obrigatório em toda consulta SQL Server.

D) `DECLARE` transforma o bloco em trigger.

### S3D4Q163 — Natureza do GO

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

Em scripts do ecossistema SQL Server, `GO` é:

A) uma função ANSI de limitação de linhas.

B) separador de lotes do cliente, não comando T-SQL.

C) um comando DML que confirma a transação.

D) uma constraint que encerra `CREATE TABLE`.

### S3D4Q164 — Dialeto e portabilidade

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

Qual afirmação evita universalizar o Transact-SQL?

A) `dbo` é esquema obrigatório em qualquer banco SQL.

B) `GO` faz parte do SQL ANSI.

C) Todo SGBD usa `TOP` e variáveis iniciadas por `@`.

D) T-SQL é do SQL Server; `LIMIT` é aceito no dialeto do PostgreSQL, sem ser exclusivo dele.

### S3D4Q165 — O que uma view armazena

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

Uma view comum, conforme a teoria, armazena primariamente:

A) a definição de uma consulta que apresenta uma relação virtual.

B) um arquivo de backup das tabelas referenciadas.

C) uma cópia congelada de todas as linhas.

D) um índice independente que acelera qualquer filtro.

### S3D4Q166 — Limites de segurança da view

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

Uma view omite coluna sensível, mas o mesmo usuário possui acesso direto à tabela base. Qual conclusão é correta?

A) A criação da view revoga automaticamente o acesso à base.

B) A coluna deixa de existir fisicamente.

C) A view não basta: também é preciso controlar acesso à tabela base.

D) A view anonimiza irreversivelmente a coluna.

### S3D4Q167 — Atualização por view

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

Sobre modificar dados por meio de uma view, assinale a alternativa correta.

A) Atualizar a view sempre cria cópia independente.

B) Depende da definição da view e do SGBD; não é universal.

C) Toda view com junção é sempre atualizável.

D) Nenhuma view pode ser atualizada.

### S3D4Q168 — Invocação de procedure

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

Uma stored procedure é caracterizada principalmente como:

A) módulo armazenado, invocado com parâmetros para executar vários comandos.

B) relação virtual usada apenas em `SELECT`.

C) restrição declarativa de domínio.

D) objeto executado automaticamente a cada mudança, sem chamada.

### S3D4Q169 — Procedure e atomicidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

Uma procedure atualiza duas tabelas, e a segunda operação falha. Qual afirmação é segura?

A) A segunda falha é ignorada por toda procedure.

B) Procedure não garante atomicidade; defina transação e tratamento de erro.

C) A procedure transforma as tabelas em views.

D) O primeiro `UPDATE` é sempre revertido só porque o código está armazenado.

### S3D4Q170 — Função e procedure

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

Qual contraste é adequado no nível ensinado?

A) Procedure só pode retornar uma linha; função sempre retorna arquivo.

B) Os dois objetos têm regras idênticas em todos os produtos.

C) Função retorna valor/tabela como expressão; procedure é chamada como operação.

D) Função sempre altera tabelas e procedure nunca recebe parâmetros.

### S3D4Q171 — Evento de trigger

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

Uma trigger é executada:

A) apenas durante `SELECT`.

B) uma vez por banco, independentemente de eventos.

C) automaticamente em resposta ao evento definido.

D) somente quando o usuário chama seu nome como procedure.

### S3D4Q172 — Inserted e deleted como conjuntos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

Em trigger DML do SQL Server, `inserted` e `deleted` devem ser tratadas como:

A) conjuntos lógicos de zero, uma ou várias linhas.

B) tabelas permanentes acessíveis fora do evento.

C) sinônimos de `COMMIT` e `ROLLBACK`.

D) variáveis escalares com uma linha garantida.

### S3D4Q173 — Auditoria de atualização em lote

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

`UPDATE profissional SET ativo='N' WHERE uf='PR'` altera três linhas. Uma trigger junta `deleted d` a `inserted i` por `id` e insere uma auditoria por mudança. Quantos registros deve produzir?

A) 2, porque somente duas tabelas lógicas participam.

B) 3, um para cada par antigo/novo cuja situação mudou.

C) 6, somando as linhas de `inserted` e `deleted`.

D) 1, porque a trigger executa uma vez.

### S3D4Q174 — Constraint antes de trigger

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

O requisito é impedir `ativo` fora de `('S','N')` em qualquer escrita. Qual primeiro mecanismo é o mais simples e declarativo?

A) Uma view sem a coluna.

B) Uma procedure opcional usada por uma única aplicação.

C) Uma trigger que corrige silenciosamente o valor.

D) Uma constraint `CHECK`.

### S3D4Q175 — Uso justificável de trigger

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

Qual requisito é candidato plausível a trigger, depois de confirmar que não cabe em constraint simples?

A) Registrar automaticamente valores anterior e novo em auditoria.

B) Garantir que `uf` pertença a três valores fixos.

C) Exibir uma consulta recorrente com poucas colunas.

D) Executar operação explicitamente solicitada com parâmetro.

### S3D4Q176 — Custos de uma trigger

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

Qual risco acompanha triggers e deve entrar no projeto?

A) Elas sempre executam fora da transação.

B) Elas processam exatamente uma linha por comando.

C) Elas não podem acessar dados do evento.

D) Podem aumentar acoplamento, efeitos implícitos e recursão.

### S3D4Q177 — Consulta estável e limitada

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

Qual objeto é o primeiro candidato para oferecer uma consulta estável que exponha apenas profissionais ativos e colunas necessárias?

A) `CHECK`.

B) View.

C) `SAVEPOINT`.

D) Trigger.

### S3D4Q178 — Operação explícita parametrizada

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

O sistema precisa executar, sob chamada explícita, uma operação de desativação recebendo `@id` e tratando erros. Qual primeiro candidato?

A) Trigger.

B) `UNIQUE`.

C) Procedure.

D) View.

### S3D4Q179 — Dependências em mudança estrutural

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

Antes de alterar o tipo ou remover coluna usada por outros objetos, o plano deve considerar:

A) apenas o espaço em disco disponível.

B) nenhuma aplicação, porque DDL é isolado.

C) dados, dependências, compatibilidade e reversão.

D) somente o novo nome da coluna.

### S3D4Q180 — Nome de constraint

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Qual benefício decorre de nomear constraints como `pk_unidade` ou `fk_profissional_unidade`?

A) Padroniza o nome e garante que todo SGBD preserve o mesmo identificador em qualquer esquema.

B) Faz a constraint nomeada ser avaliada antes das demais restrições da tabela.

C) Permite que a aplicação identifique qualquer violação sem depender de códigos ou mensagens do produto.

D) Facilita diagnóstico, manutenção e referência ao objeto.

### S3D4Q181 — Valor explícito inválido e DEFAULT

**Nível:** Médio

**Uso:** Revisão

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

A coluna `ativo` tem `DEFAULT 'S'` e `CHECK (ativo IN ('S','N'))`. O comando informa explicitamente `ativo='X'`. Qual efeito é esperado?

A) X é aceito porque todo texto satisfaz o default.

B) O `DEFAULT` não corrige `'X'`; o `CHECK` deve rejeitá-lo.

C) A chave estrangeira transforma X em N.

D) O default substitui X por S.

### S3D4Q182 — Regra declarada por CHECK

**Nível:** Médio

**Uso:** Revisão

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Qual requisito é expresso diretamente por `CHECK (uf IN ('PR','SC','RS'))`?

A) A UF deve pertencer ao conjunto; nulabilidade é regra separada.

B) Cada UF deve ser única na tabela.

C) Toda UF deve existir como linha em uma tabela pai.

D) A coluna nunca pode ser nula, por si só.

### S3D4Q183 — Correspondência de FOREIGN KEY

**Nível:** Médio

**Uso:** Revisão

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Para um `unidade_id` não nulo sujeito a FK, o que deve existir?

A) Chave existente na tabela pai.

B) Uma view com o mesmo nome.

C) Uma procedure que aprove a linha.

D) Um `DEFAULT` na tabela filha.

### S3D4Q184 — DROP e objetos dependentes

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

Uma coluna é referenciada por uma view. Ao tentar removê-la, qual afirmação é prudente?

A) A view vira automaticamente tabela.

B) A coluna permanece acessível sob outro nome sem migração.

C) `DROP` ignora toda dependência por definição.

D) Dependências podem impedir a operação ou ser removidas de forma explícita.

### S3D4Q185 — Transação não substitui validação

**Nível:** Médio

**Uso:** Revisão

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

Por que iniciar uma transação não basta para tornar seguro um `DELETE` amplo?

A) Porque transações nunca permitem rollback.

B) Porque `DELETE` não participa de transações.

C) Validar o alcance e garantir rollback antes do `COMMIT`.

D) Porque `WHERE` é proibido dentro de transação.

### S3D4Q186 — TOP e determinismo

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

Em T-SQL, o que torna significativa a seleção dos “dez primeiros” por nome?

A) `TOP (10)` com `ORDER BY` explícito.

B) Usar `TOP (10)` sem qualquer ordem.

C) Usar `DISTINCT` sem projeção.

D) Colocar `GO` após o `SELECT`.

### S3D4Q187 — Procedure parametrizada e escopo

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures) e [DML e validação de alcance](semana_03_estudo.md#s3-d4-dml).

A procedure recebe `@id` e executa `UPDATE profissional SET ativo='N' WHERE id=@id`. Quais cuidados são essenciais?

A) Substituir `@id` por variável global não inicializada.

B) Validar parâmetro/linha afetada, transação e tratamento de erro.

C) Remover o `WHERE` e confiar no nome da procedure.

D) Adicionar `TOP` ao `UPDATE` sem critério.

### S3D4Q188 — Trigger orientada a conjuntos

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

Qual núcleo é adequado para auditar mudança de estado em lote no SQL Server?

A) Ignorar `deleted` e inventar o valor anterior.

B) Selecionar um valor arbitrário de `inserted` para variável e gravar uma linha.

C) `INSERT ... SELECT` de `deleted JOIN inserted`, filtrando valores alterados.

D) Executar cursor que presume exatamente uma linha.

### S3D4Q189 — Reflexo da tabela em view comum

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

A view `v_profissional_ativo` filtra `ativo='S'`. Ana é desativada na tabela base. O que ocorre na consulta seguinte à view comum?

A) Ana desaparece porque a view volta a consultar a base e reaplica o filtro.

B) Ana é apagada fisicamente da tabela.

C) Ana permanece para sempre porque a view congelou a linha.

D) A view falha até ser recriada.

### S3D4Q190 — Comando negativo sobre trigger

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

Assinale a alternativa **INCORRETA** sobre triggers DML no SQL Server.

A) Um único comando pode afetar várias linhas.

B) `inserted` e `deleted` são conjuntos lógicos.

C) Uma trigger pode aumentar acoplamento e produzir efeitos implícitos.

D) A trigger roda uma vez por linha; variáveis escalares são sempre seguras.

### S3D4Q191 — Escolha integrada de quatro mecanismos

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

Associe: I. impedir UF fora do domínio; II. expor consulta limitada; III. executar desativação chamada com parâmetro; IV. auditar automaticamente mudança de estado. Qual sequência é a mais simples e adequada?

A) I `CHECK`; II view; III procedure; IV trigger set-based.

B) I trigger; II procedure; III view; IV `CHECK`.

C) I view; II `CHECK`; III trigger; IV procedure.

D) I procedure; II trigger; III `UNIQUE`; IV view.

### S3D4Q192 — Comando negativo sobre classes

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

Assinale a alternativa **INCORRETA**.

A) `ALTER TABLE` é DDL pela finalidade de modificar definição.

B) `COMMIT` é comando DML porque grava linhas novas.

C) `REVOKE` pertence à administração de privilégios, classificada como DCL.

D) `ROLLBACK` pertence ao controle de transações, classificado como TCL.

### S3D4Q193 — Migração com dados, FK e reversão

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate) e [restrições declarativas](semana_03_estudo.md#s3-d4-ddl-restricoes).

A coluna `unidade_id` contém nulos e alguns valores sem pai; passará a `NOT NULL` com FK validada. Qual plano atende simultaneamente estado dos dados, integridade e reversão?

A) Executar `TRUNCATE` e recriar o banco sem dependências.

B) Adicionar ambas as constraints imediatamente e apagar depois o que falhar.

C) Criar somente uma view que esconda linhas problemáticas.

D) Inventariar e sanear nulos/órfãos, validar, aplicar FK/NOT NULL e preservar rollback.

### S3D4Q194 — Lotes separados por GO

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [GO, lotes e escopo](semana_03_estudo.md#s3-d4-go-lotes-escopo).

Em um script executado no SSMS ou no `sqlcmd`, uma variável local é declarada antes de `GO` e referenciada no lote seguinte. Qual análise é adequada?

A) A ferramenta encerra o lote em `GO`; a variável local T-SQL não alcança o lote seguinte.

B) O mecanismo recebe `GO` como função que copia o estado.

C) `GO` confirma automaticamente a transação e preserva todas as variáveis.

D) A variável é coluna permanente e continua disponível.

### S3D4Q195 — Mecanismo mais simples

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

O requisito pode ser expresso integralmente por `FOREIGN KEY`. Qual decisão segue a matriz?

A) Criar trigger e remover a FK.

B) Exigir que cada aplicação valide por conta própria.

C) Usar view para impedir inserções inválidas em toda rota.

D) Preferir constraint declarativa; trigger seria desnecessária.

### S3D4Q196 — Efeito de DELETE com predicado

**Nível:** Médio

**Uso:** Simulado

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

O comando `DELETE FROM pagamento WHERE status='CANCELADO' AND competencia<'2025-01';` remove:

A) todos os pagamentos anteriores a 2025, qualquer que seja o status.

B) linhas que satisfazem ambos: cancelado e competência anterior ao limite.

C) somente a primeira linha cancelada.

D) a estrutura da tabela PAGAMENTO.

### S3D4Q197 — Trigger de auditoria com três garantias

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

Uma trigger deve (1) auditar lote de qualquer tamanho, (2) registrar somente mudança real de `ativo` e (3) manter correspondência entre valor anterior e novo. Qual desenho satisfaz os três filtros?

A) Fazer produto cartesiano entre `inserted` e `deleted` e gravar todos os pares.

B) Ler um valor escalar de `inserted`, gravar uma linha e ignorar `deleted`.

C) Executar uma chamada externa por linha sem transação.

D) Unir `deleted` e `inserted`, filtrar a alteração e usar `INSERT ... SELECT`.

### S3D4Q198 — View e segurança por três caminhos

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Views e caminhos de acesso](semana_03_estudo.md#s3-d4-views-seguranca).

Uma view omite dado sensível. Para que ela componha uma política efetiva, é preciso verificar: (1) colunas/linhas projetadas, (2) privilégios diretos sobre a base e (3) outros caminhos de inferência/acesso. Qual alternativa é correta?

A) Basta renomear a coluna sensível na view.

B) Conceder acesso à view e à tabela base é equivalente a restringir a coluna.

C) A view limita a consulta, mas não anonimiza nem revoga acessos alternativos.

D) A criação da view resolve os três pontos automaticamente.

### S3D4Q199 — DDL com compatibilidade, dependências e retorno

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

Uma coluna usada por view e procedure mudará de tipo, e há dados incompatíveis. Qual plano cobre os três filtros críticos?

A) Inventariar dados/dependências, migrar, adaptar consumidores, testar e preservar reversão.

B) Alterar a coluna primeiro, pois views e procedures se ajustam necessariamente.

C) Remover consumidores com `DROP` e dispensar plano de retorno.

D) Criar trigger para converter qualquer valor sem testar perda.

### S3D4Q200 — Procedure transacional e escopo seguro

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

Uma procedure deve desativar um profissional e registrar auditoria. O requisito exige (1) uma única chave validada, (2) atomicidade das duas escritas e (3) tratamento que reverta em falha. Qual desenho é o melhor?

A) Usar trigger escalar sem parâmetro e sem verificar lote.

B) Executar `GO` entre as duas escritas para proteger a unidade.

C) Dois `UPDATE/INSERT` soltos; o nome da procedure garante atomicidade.

D) Validar, abrir transação, atualizar e auditar; confirmar ao fim e reverter no erro.

## Questões extras - Dia 4

#### Extra Dia 4.1 — Legalidade e eficiência

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios administrativos
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Um gestor invoca eficiência para ignorar competência definida no ordenamento. Qual avaliação é correta?

A) Eficiência permite assumir competência de outro órgão quando a medida reduz custo e prazo.

B) Eficiência não afasta legalidade, competência ou procedimento.

C) Legalidade só incide quando a eficiência não oferecer solução menos onerosa.

D) Eficiência autoriza qualquer procedimento que não esteja expressamente proibido ao gestor.

#### Extra Dia 4.2 — Impessoalidade

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípio da impessoalidade
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Qual conduta é compatível com a impessoalidade?

A) Atribuir nominalmente ao dirigente os resultados de campanha institucional, desde que o serviço seja público.

B) Priorizar usuário conhecido quando o agente considere que isso tornará o atendimento mais rápido.

C) Comunicar o serviço com finalidade pública, sem promoção pessoal.

D) Tratar todos de modo idêntico, mesmo quando a lei estabelece prioridades objetivas de atendimento.

#### Extra Dia 4.3 — Publicidade e proteção

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Publicidade, sigilo e dados
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Sobre o princípio da publicidade, assinale a alternativa correta.

A) Exige divulgação irrestrita de todo dado pessoal.

B) Autoriza ignorar sigilo legal.

C) Favorece transparência, com limites de sigilo e proteção de dados.

D) Impede a publicação de qualquer relatório estatístico.

#### Extra Dia 4.4 — Anulação e revogação

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Controle dos atos
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Qual distinção está correta?

A) Todo ato inconveniente é anulado por ilegalidade.

B) Ato ilegal é revogado; ato válido é anulado.

C) Anulação e revogação são sempre sinônimas.

D) Anula-se ato ilegal; revoga-se o válido inconveniente.

#### Extra Dia 4.5 — Convalidação

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Vício sanável
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

A convalidação, na síntese estudada:

A) equivale à revogação por conveniência.

B) atinge vício sanável sem lesão ao interesse público ou a terceiros.

C) corrige qualquer ilegalidade, inclusive vício insanável.

D) depende apenas da vontade do beneficiário.

#### Extra Dia 4.6 — Descentralização e desconcentração

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Organização administrativa
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Assinale a alternativa correta.

A) Desconcentração interna; descentralização transfere execução/titularidade.

B) Descentralização ocorre apenas dentro do mesmo órgão.

C) Os conceitos são sinônimos.

D) Desconcentração cria necessariamente nova pessoa jurídica.

#### Extra Dia 4.7 — Natureza da autarquia

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Administração Indireta
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Uma autarquia:

A) é sempre associação privada.

B) integra a Administração Indireta como pessoa jurídica de direito público.

C) é órgão interno sem personalidade própria.

D) integra a Administração Direta e não possui personalidade.

#### Extra Dia 4.8 — LAI e LGPD

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Transparência e dados
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Qual afirmação é compatível com a revisão?

A) LAI e LGPD devem ser compatibilizadas no caso concreto.

B) A LGPD prevalece sempre que houver dado pessoal, tornando a LAI inaplicável ao pedido.

C) A LAI prevalece para órgãos públicos, enquanto a LGPD regula apenas agentes privados.

D) Aplica-se isoladamente a lei considerada mais específica, sem compatibilizar finalidade, transparência e proteção.

#### Extra Dia 4.9 — Responsabilidade objetiva e regresso

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Responsabilidade civil do Estado
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

O Estado indeniza vítima por dano imputável à atuação pública. Isso torna automática a ação regressiva contra o agente?

A) Sim, ainda que nenhum agente tenha agido com culpa.

B) Não, porque o Estado nunca responde objetivamente.

C) Não: regresso contra o agente exige dolo ou culpa.

D) Sim. Toda indenização prova dolo do agente.

#### Extra Dia 4.10 — Relatório público e dados individuais

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Publicidade e proteção de dados
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Um órgão pretende demonstrar desempenho. Qual alternativa melhor compatibiliza publicidade e proteção?

A) Não publicar nenhum resultado para evitar qualquer risco.

B) Divulgar a base integral e pedir retirada posterior a quem reclamar.

C) Publicar nomes e detalhes pessoais de todos porque publicidade é absoluta.

D) Publicar indicadores agregados e justificar dado individual por base e necessidade.

#### Extra Dia 4.11 — Comando negativo sobre organização

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios e organização
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Assinale a alternativa **INCORRETA**.

A) Desconcentração distribui competências dentro da mesma pessoa jurídica.

B) Autarquia possui personalidade de direito público e integra a Administração Indireta.

C) Eficiência autoriza órgão incompetente a praticar ato quando houver economia de tempo.

D) Impessoalidade exige finalidade pública e veda promoção pessoal.

#### Extra Dia 4.12 — Ato válido, dado protegido e competência

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Decisão administrativa integrada
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

Um órgão competente editou ato válido, mas depois o considerou inconveniente; ao divulgar a decisão, há dados pessoais sem necessidade pública. Qual conduta combina os filtros corretos?

A) Avaliar a revogação e publicar a decisão, omitindo dados pessoais desnecessários.

B) Anular o ato por inconveniência e divulgar tudo por publicidade.

C) Convalidar o ato válido e ocultar toda a decisão.

D) Manter o ato obrigatoriamente e publicar nomes para demonstrar eficiência.

#### Extra Dia 4.13 — Vírgula entre sujeito e verbo

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Pontuação
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Assinale a frase corretamente pontuada.

A) Os relatórios consolidados, orientam a decisão pública.

B) Os relatórios, consolidados orientam, a decisão pública.

C) Os relatórios consolidados orientam, a decisão pública.

D) Os relatórios consolidados orientam a decisão pública.

#### Extra Dia 4.14 — Restritiva e explicativa

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Orações adjetivas
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Em “Os relatórios que preservam dados pessoais podem ser publicados”, a oração sem vírgulas:

A) é conclusiva.

B) explica uma característica de todos os relatórios.

C) restringe o conjunto aos relatórios que preservam dados pessoais.

D) é causal.

#### Extra Dia 4.15 — Condição para crase

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Crase
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Em qual alternativa a crase decorre da combinação de preposição e artigo?

A) Os servidores passaram a atuar.

B) O relatório foi entregue a uma comissão.

C) A equipe começou a revisar os dados.

D) O documento foi encaminhado à unidade responsável.

#### Extra Dia 4.16 — Haver impessoal

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Concordância
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Assinale a forma correta para indicar existência.

A) Havia falhas no relatório.

B) Houveram falhas no relatório.

C) Haviam muitos dados inconsistentes.

D) Devem haver soluções adequadas.

#### Extra Dia 4.17 — Reescrita e relação lógica

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Reescrita argumentativa
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Original: “Embora a publicação amplie o controle social, dados pessoais desnecessários devem ser protegidos.” Qual reescrita preserva concessão e escopo?

A) Se os dados são protegidos, a publicação jamais amplia o controle.

B) A publicação amplia o controle social; ainda assim, devem ser protegidos os dados pessoais desnecessários.

C) Porque a publicação amplia o controle, nenhum dado deve ser protegido.

D) A publicação amplia o controle, portanto todos os dados pessoais devem ser expostos.

#### Extra Dia 4.18 — Função da conclusão

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Estrutura discursiva
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Em uma dissertação, a conclusão deve prioritariamente:

A) apresentar dados técnicos sem relação com o tema.

B) abrir um terceiro argumento não desenvolvido.

C) retomar a tese e sintetizar os eixos, sem argumento novo.

D) copiar literalmente toda a introdução.

#### Extra Dia 4.19 — Escopo da negação

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Reescrita e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Qual reescrita preserva “O órgão não divulgou dados pessoais desnecessários”?

A) Não foi o órgão que divulgou todos os dados necessários.

B) O órgão omitiu dados pessoais desnecessários à finalidade.

C) O órgão não divulgou nenhum dado, pessoal ou estatístico.

D) O órgão divulgou dados pessoais, mas eles não eram necessários.

#### Extra Dia 4.20 — Reescrita com três filtros gramaticais

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Sintaxe, crase e coerência
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

Escolha a frase que atende simultaneamente a: (1) não separar sujeito e verbo; (2) usar crase apenas com regência e artigo; (3) manter conclusão coerente, sem argumento novo.

A) Os relatórios públicos, permitem à sociedade fiscalizar; portanto, um novo tema sem relação deve ser debatido.

B) A transparência conduz a sociedade à fiscalizar os órgãos, e por isso, haviam controles.

C) As informações que orientam à gestão, devem ser claras; contudo isso prova toda política.

D) Relatórios claros permitem à sociedade exercer controle social; a conclusão retoma transparência e fiscalização, sem eixo novo.

## Gabarito - Dia 4

### Principais

| S3D4Q151 | S3D4Q152 | S3D4Q153 | S3D4Q154 | S3D4Q155 | S3D4Q156 | S3D4Q157 | S3D4Q158 | S3D4Q159 | S3D4Q160 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | D | D | B | D | A | C | B | C | A |

| S3D4Q161 | S3D4Q162 | S3D4Q163 | S3D4Q164 | S3D4Q165 | S3D4Q166 | S3D4Q167 | S3D4Q168 | S3D4Q169 | S3D4Q170 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | B | B | D | A | C | B | A | B | C |

| S3D4Q171 | S3D4Q172 | S3D4Q173 | S3D4Q174 | S3D4Q175 | S3D4Q176 | S3D4Q177 | S3D4Q178 | S3D4Q179 | S3D4Q180 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | B | D | A | D | B | C | C | D |

| S3D4Q181 | S3D4Q182 | S3D4Q183 | S3D4Q184 | S3D4Q185 | S3D4Q186 | S3D4Q187 | S3D4Q188 | S3D4Q189 | S3D4Q190 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | A | A | D | C | A | B | C | A | D |

| S3D4Q191 | S3D4Q192 | S3D4Q193 | S3D4Q194 | S3D4Q195 | S3D4Q196 | S3D4Q197 | S3D4Q198 | S3D4Q199 | S3D4Q200 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | B | D | A | D | B | D | C | A | D |

### Extras

| 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 4.6 | 4.7 | 4.8 | 4.9 | 4.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | C | C | D | B | A | B | A | C | D |

| 4.11 | 4.12 | 4.13 | 4.14 | 4.15 | 4.16 | 4.17 | 4.18 | 4.19 | 4.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | C | D | A | B | C | B | D |

## Comentários - Dia 4

### Comentário S3D4Q151

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Administra privilégio, sendo DCL.
- **B)** Incorreta. Controla transação, sendo TCL.
- **C)** Correta. Define um objeto e sua estrutura.
- **D)** Incorreta. Modifica dados, sendo DML.

**Conceito:** Classificação por finalidade.

**Pegadinha:** Classificar pelo tamanho ou risco do comando, não pelo objeto de sua ação.

**Como pensar:** Pergunte se o comando define estrutura, manipula dados, autoriza ou controla transação.

### Comentário S3D4Q152

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mistura DCL e TCL.
- **B)** Incorreta. Mistura TCL e DDL.
- **C)** Incorreta. É o núcleo DDL.
- **D)** Correta. Os quatro leem ou modificam dados e foram classificados como DML.

**Conceito:** Classe DML.

**Pegadinha:** Memorizar siglas sem relacioná-las à finalidade.

**Como pensar:** Associe cada verbo ao alvo: linhas/dados ou definição persistente.

### Comentário S3D4Q153

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ligação entre tabelas é função de `FOREIGN KEY`.
- **B)** Incorreta. Chave primária não admite duplicatas.
- **C)** Incorreta. Valor padrão é função de `DEFAULT`.
- **D)** Correta. As duas garantias sustentam a identificação de cada linha.

**Conceito:** `PRIMARY KEY`.

**Pegadinha:** Confundir identificação interna com referência externa.

**Como pensar:** Cheque duas propriedades: valor único e presente para cada linha.

### Comentário S3D4Q154

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Valor excluído não possui correspondência.
- **B)** Correta. A FK verifica não nulos; a nulabilidade permite ausência.
- **C)** Incorreta. Valor não nulo precisa corresponder.
- **D)** Incorreta. Zero não é ausência automática e exigiria pai 0.

**Conceito:** Integridade referencial.

**Pegadinha:** Tratar `0` como nulo ou exigir pai para uma ausência permitida.

**Como pensar:** Separe teste de nulabilidade do teste de correspondência da FK.

### Comentário S3D4Q155

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Default não é corretor geral de dados informados.
- **B)** Incorreta. PK não atua nessa coluna dessa forma.
- **C)** Incorreta. Constraint valida; não transforma valor arbitrariamente.
- **D)** Correta. Distingue fornecimento por omissão da validação do valor explícito.

**Conceito:** `DEFAULT` versus `CHECK`.

**Pegadinha:** Acreditar que valor padrão funciona como saneador universal.

**Como pensar:** Pergunte se houve omissão; depois valide o valor efetivo contra o domínio.

### Comentário S3D4Q156

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A teoria ressalva a variação entre produtos.
- **B)** Incorreta. Chave primária inclui não nulidade e papel identificador.
- **C)** Incorreta. Também universaliza comportamento variável.
- **D)** Incorreta. Confunde unicidade com `NOT NULL` universal.

**Conceito:** `UNIQUE` e variação de produto.

**Pegadinha:** Transformar comportamento observado em um fornecedor em regra ANSI absoluta.

**Como pensar:** Quando a teoria registra variação, escolha a afirmação que preserva a dependência do SGBD.

### Comentário S3D4Q157

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A definição pode falhar diante do estado atual.
- **B)** Incorreta. Exclusão indiscriminada não é requisito nem plano seguro.
- **C)** Correta. Compatibiliza dados, integridade, mudança estrutural e reversão.
- **D)** Incorreta. View oculta linhas, mas não altera a nulabilidade da base.

**Conceito:** Migração de restrição.

**Pegadinha:** Aplicar DDL como se o conteúdo existente fosse irrelevante.

**Como pensar:** Antes da nova regra, prove que todos os dados atuais a satisfazem e que a mudança pode ser revertida.

### Comentário S3D4Q158

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A teoria nega a sinonímia universal.
- **B)** Correta. A resposta combina o alcance sem filtro com dimensões dependentes do fornecedor.
- **C)** Incorreta. A ausência de predicado é justamente uma diferença relevante.
- **D)** Incorreta. O comportamento de registro não permite essa generalização.

**Conceito:** Semântica de `TRUNCATE`.

**Pegadinha:** Generalizar uma implementação específica ou reduzir tudo a desempenho.

**Como pensar:** Separe efeito lógico conhecido de detalhes de logging e transação dependentes do produto.

### Comentário S3D4Q159

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não há condição de estado anterior.
- **B)** Incorreta. `WHERE` é opcional sintaticamente, embora sua ausência seja perigosa.
- **C)** Correta. A ausência de predicado não limita o conjunto.
- **D)** Incorreta. SQL opera em conjuntos, não na primeira linha por padrão.

**Conceito:** Alcance de DML.

**Pegadinha:** Presumir limite implícito de uma linha.

**Como pensar:** Antes de executar, leia o conjunto alvo: sem predicado, ele é a tabela inteira.

### Comentário S3D4Q160

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A leitura prévia valida exatamente o conjunto que o DML pretende atingir.
- **B)** Incorreta. Amplia o risco ao conjunto total.
- **C)** Incorreta. Trigger genérica não substitui validação do predicado.
- **D)** Incorreta. Remove a estrutura e não é prévia.

**Conceito:** Validação de alcance.

**Pegadinha:** Acreditar que transação elimina a necessidade de saber o que será alterado.

**Como pensar:** Transforme o predicado do DML em consulta e confira as chaves antes de confirmar.

### Comentário S3D4Q161

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Privilégios pertencem a DCL.
- **B)** Incorreta. Confirmação/reversão pertencem a TCL.
- **C)** Correta. As duas associações seguem a finalidade ensinada.
- **D)** Incorreta. Definição estrutural é DDL.

**Conceito:** DCL e TCL.

**Pegadinha:** Agrupar todos os comandos administrativos em uma única sigla.

**Como pensar:** Pergunte se a ação muda autorização ou estado da unidade de trabalho.

### Comentário S3D4Q162

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. `@uf` é variável local, e `TOP` não cria ordenação automática.
- **B)** Correta. Distingue a quantidade limitada do critério que torna a escolha das dez linhas determinística.
- **C)** Incorreta. Limitação não é obrigatória.
- **D)** Incorreta. `DECLARE` apenas declara a variável; não cria nem transforma o bloco em trigger.

**Conceito:** Variável e `TOP` em T-SQL.

**Pegadinha:** Confundir limitação com garantia de ordem.

**Como pensar:** Identifique o dialeto, depois separe quantidade solicitada de critério de escolha.

**Justificativa de comprimento:** A correta precisa reunir três verificações — variável local, limite e ordenação total — enquanto cada distrator explora apenas uma confusão.

### Comentário S3D4Q163

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não pertence à sintaxe ANSI de limitação.
- **B)** Correta. É exatamente a distinção registrada na teoria.
- **C)** Incorreta. Confirmação é `COMMIT`, e `GO` não é DML.
- **D)** Incorreta. Não integra definição de constraint.

**Conceito:** `GO` e lote cliente.

**Pegadinha:** Tratar tudo que aparece em script como comando do mecanismo.

**Como pensar:** Pergunte quem interpreta o token: ferramenta cliente ou mecanismo SQL.

### Comentário S3D4Q164

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Esquemas e nomes variam.
- **B)** Incorreta. `GO` é interpretado por clientes específicos.
- **C)** Incorreta. São marcas de dialeto, não universais.
- **D)** Correta. Delimita T-SQL ao SQL Server e descreve suporte do PostgreSQL sem atribuir exclusividade a `LIMIT`.

**Conceito:** Dialeto versus padrão.

**Pegadinha:** Promover sintaxe de um produto a regra universal.

**Como pensar:** Marque cada elemento como padrão, extensão de fornecedor ou comando de ferramenta.

**Justificativa de comprimento:** A correta delimita simultaneamente o fornecedor do T-SQL e a não exclusividade de `LIMIT`; os distratores universalizam um único elemento.

### Comentário S3D4Q165

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A consulta é reaplicada sobre a base segundo a definição.
- **B)** Incorreta. Backup tem finalidade distinta.
- **C)** Incorreta. Isso descreveria materialização/cópia explícita, não view comum.
- **D)** Incorreta. View não implica índice ou ganho universal.

**Conceito:** View virtual.

**Pegadinha:** Associar objeto nomeado a armazenamento físico automático.

**Como pensar:** Pergunte se o objeto guarda dados ou a consulta; a view comum guarda a definição.

### Comentário S3D4Q166

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não há revogação automática.
- **B)** Incorreta. A base permanece com a coluna.
- **C)** Correta. Segurança depende do caminho de acesso efetivamente autorizado.
- **D)** Incorreta. Omissão na projeção não é anonimização irreversível.

**Conceito:** View e privilégios.

**Pegadinha:** Avaliar somente a definição da view e ignorar acesso alternativo.

**Como pensar:** Mapeie todos os caminhos: view limitada e tabela base; uma brecha no segundo anula o objetivo.

### Comentário S3D4Q167

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não há cópia automática.
- **B)** Correta. A teoria registra dependência da definição e do produto.
- **C)** Incorreta. Generalização absoluta é insegura.
- **D)** Incorreta. Algumas views são atualizáveis.

**Conceito:** Atualizabilidade de views.

**Pegadinha:** Escolher um “sempre” ou “nunca” onde há condições.

**Como pensar:** Procure a resposta que preserva definição e suporte do fornecedor.

### Comentário S3D4Q168

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Resume o contrato de procedure.
- **B)** Incorreta. Descreve view.
- **C)** Incorreta. Descreve `CHECK` ou restrição semelhante.
- **D)** Incorreta. Descreve trigger.

**Conceito:** Stored procedure.

**Pegadinha:** Confundir objetos programáveis pelo fato de todos ficarem no banco.

**Como pensar:** Pergunte se a execução é chamada, consultada ou disparada por evento.

### Comentário S3D4Q169

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Falha precisa ser tratada, não presumidamente ignorada.
- **B)** Correta. Separa módulo armazenado de contrato transacional.
- **C)** Incorreta. Não há transformação de objeto.
- **D)** Incorreta. Armazenamento do módulo não garante rollback.

**Conceito:** Atomicidade em procedure.

**Pegadinha:** Confundir “stored” com “automaticamente transacional”.

**Como pensar:** Liste as etapas, marque início/confirmação/reversão e caminho de erro.

### Comentário S3D4Q170

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Cria restrições inexistentes.
- **B)** Incorreta. A teoria ressalva diferenças de contrato e fornecedor.
- **C)** Correta. É o contraste prudente apresentado.
- **D)** Incorreta. Inverte e absolutiza comportamentos.

**Conceito:** Função versus procedure.

**Pegadinha:** Memorizar uma diferença absoluta fora do contexto do produto.

**Como pensar:** Compare modo de invocação e contrato de retorno, preservando variações do SGBD.

### Comentário S3D4Q171

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Triggers podem responder a DML definido, não apenas leitura.
- **B)** Incorreta. A execução depende de eventos.
- **C)** Correta. Essa reação automática a evento a distingue de procedure.
- **D)** Incorreta. Chamada explícita caracteriza procedure.

**Conceito:** Acionamento de trigger.

**Pegadinha:** Confundir armazenamento de código com modo de invocação.

**Como pensar:** Pergunte se há chamada explícita ou reação automática.

### Comentário S3D4Q172

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Essa propriedade exige lógica orientada a conjuntos.
- **B)** Incorreta. São estruturas lógicas do contexto da trigger.
- **C)** Incorreta. Não controlam transação por esses nomes.
- **D)** Incorreta. Um único comando pode afetar múltiplas linhas.

**Conceito:** Pseudo-tabelas de trigger.

**Pegadinha:** Programar como se o evento ocorresse uma vez por linha.

**Como pensar:** Teste a trigger com lote de várias chaves, não apenas com um registro.

### Comentário S3D4Q173

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Número de estruturas não define registros.
- **B)** Correta. O join emparelha três chaves; o `SELECT` insere três linhas de auditoria.
- **C)** Incorreta. Cada mudança usa um par, não duas auditorias.
- **D)** Incorreta. Uma execução pode processar três linhas, não apenas uma auditoria.

**Conceito:** Trigger set-based.

**Pegadinha:** Confundir número de execuções com número de linhas processadas.

**Como pensar:** Conte as chaves afetadas e acompanhe o `SELECT` do join até o `INSERT`.

### Comentário S3D4Q174

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não impede escrita direta inválida.
- **B)** Incorreta. Outros caminhos de escrita contornariam a procedure.
- **C)** Incorreta. Trigger é efeito implícito desnecessário para domínio simples.
- **D)** Correta. A constraint expressa o domínio e é aplicada pelo SGBD a toda escrita.

**Conceito:** Escolha de mecanismo.

**Pegadinha:** Usar objeto programável complexo para regra declarativa simples.

**Como pensar:** Tente PK/FK/UNIQUE/CHECK/NOT NULL antes de recorrer a reação automática.

### Comentário S3D4Q175

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Reage automaticamente ao evento e usa `inserted/deleted`.
- **B)** Incorreta. Cabe em `CHECK`.
- **C)** Incorreta. Cabe em view.
- **D)** Incorreta. Cabe em procedure.

**Conceito:** Escolha de trigger.

**Pegadinha:** Escolher trigger apenas porque o requisito está no banco.

**Como pensar:** Classifique o requisito: garantia declarativa, consulta, operação explícita ou reação a evento.

### Comentário S3D4Q176

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A semântica transacional depende do evento/produto; a teoria não autoriza “sempre fora”.
- **B)** Incorreta. Comando pode afetar muitas linhas.
- **C)** Incorreta. O evento fornece conjuntos lógicos.
- **D)** Correta. A reação invisível ao chamador exige requisito, testes e controle de recursão.

**Conceito:** Riscos de triggers.

**Pegadinha:** Avaliar apenas se o código funciona para um caso unitário.

**Como pensar:** Teste visibilidade do efeito, lote, falha, recursão e custo.

### Comentário S3D4Q177

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Check valida domínio/condição.
- **B)** Correta. View encapsula a consulta e sua projeção, com privilégios revisados.
- **C)** Incorreta. Savepoint pertence a controle transacional.
- **D)** Incorreta. Trigger reage a evento.

**Conceito:** Escolha de view.

**Pegadinha:** Tentar implementar interface de leitura com mecanismo de escrita.

**Como pensar:** Se o requisito é uma relação consultável, avalie view e depois os privilégios.

### Comentário S3D4Q178

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Trigger não é chamada explicitamente.
- **B)** Incorreta. Unicidade não executa operação.
- **C)** Correta. Procedure recebe parâmetros e centraliza a operação, desde que contrato transacional e erros sejam definidos.
- **D)** Incorreta. View descreve consulta.

**Conceito:** Escolha de procedure.

**Pegadinha:** Escolher trigger porque há alteração de dados, ignorando o modo de invocação.

**Como pensar:** A palavra decisiva é “chamada explícita com parâmetro”.

### Comentário S3D4Q179

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Capacidade é apenas uma dimensão possível.
- **B)** Incorreta. Views, procedures e aplicações podem depender da estrutura.
- **C)** Correta. Reúne os filtros de segurança da mudança estrutural.
- **D)** Incorreta. Nome não cobre impacto.

**Conceito:** Planejamento de DDL.

**Pegadinha:** Tratar alteração de catálogo como ato sem consumidores.

**Como pensar:** Inventarie dados e dependências antes de definir ordem e rollback.

### Comentário S3D4Q180

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Convenção de nomes ajuda a equipe, mas não garante portabilidade do identificador entre produtos e esquemas.
- **B)** Incorreta. O nome não define precedência de avaliação entre restrições.
- **C)** Incorreta. O identificador favorece o diagnóstico, mas códigos e mensagens continuam dependentes do produto e do driver.
- **D)** Correta. Mensagens e operações de manutenção tornam-se mais identificáveis.

**Conceito:** Nomeação de constraints.

**Pegadinha:** Atribuir ao nome um efeito de execução.

**Como pensar:** Distinga identificabilidade operacional de semântica da restrição.

### Comentário S3D4Q181

**Nível:** Médio

**Uso:** Revisão

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A presença de default não elimina validação.
- **B)** Correta. O valor efetivo viola o domínio permitido.
- **C)** Incorreta. FK não participa desse requisito.
- **D)** Incorreta. Default atua na omissão, não como corretor.

**Conceito:** Default e validação.

**Pegadinha:** Aplicar o valor padrão depois de qualquer erro.

**Como pensar:** Determine primeiro o valor fornecido; depois aplique a constraint correspondente.

### Comentário S3D4Q182

**Nível:** Médio

**Uso:** Revisão

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A alternativa separa domínio e presença.
- **B)** Incorreta. Unicidade seria `UNIQUE`.
- **C)** Incorreta. Referência seria FK.
- **D)** Incorreta. `CHECK` não substitui automaticamente `NOT NULL`.

**Conceito:** Constraint `CHECK`.

**Pegadinha:** Achar que uma constraint de domínio também impõe todas as demais garantias.

**Como pensar:** Liste cada garantia requerida e associe uma constraint específica.

### Comentário S3D4Q183

**Nível:** Médio

**Uso:** Revisão

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É a garantia referencial.
- **B)** Incorreta. View não cria correspondência.
- **C)** Incorreta. Procedure não substitui FK declarada.
- **D)** Incorreta. Valor padrão não prova existência do pai.

**Conceito:** Integridade referencial.

**Pegadinha:** Procurar objeto de código em vez da linha pai.

**Como pensar:** Siga a seta da coluna filha até a chave candidata referenciada.

### Comentário S3D4Q184

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não ocorre essa conversão.
- **B)** Incorreta. Renomeação/migração exige ação.
- **C)** Incorreta. Generalização insegura.
- **D)** Correta. A teoria exige inventário de dependências e atenção às opções do SGBD.

**Conceito:** DDL e dependências.

**Pegadinha:** Contar com remoção automática sem conhecer o produto.

**Como pensar:** Liste consumidores, escolha estratégia compatível e mantenha reversão.

### Comentário S3D4Q185

**Nível:** Médio

**Uso:** Revisão

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A teoria não autoriza esse absoluto.
- **B)** Incorreta. Comportamento transacional existe conforme o ambiente.
- **C)** Correta. Transação é mecanismo; decisão correta depende de conferir predicado, quantidade e chaves.
- **D)** Incorreta. Predicados são permitidos.

**Conceito:** Validação e transação.

**Pegadinha:** Tratar rollback potencial como substituto de prevenção.

**Como pensar:** Faça prévia, valide o conjunto, execute e só confirme depois da verificação.

### Comentário S3D4Q186

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-tsql).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O limite atua sobre uma saída cuja ordem solicitada foi definida.
- **B)** Incorreta. Limita quantidade, mas não define quais dez pelo requisito.
- **C)** Incorreta. Distinct não estabelece ordem.
- **D)** Incorreta. Separador de lote não ordena.

**Conceito:** `TOP` e `ORDER BY`.

**Pegadinha:** Confundir quantidade limitada com seleção determinística.

**Como pensar:** Primeiro declare a ordem; depois aplique o limite.

### Comentário S3D4Q187

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures) e [DML e validação de alcance](semana_03_estudo.md#s3-d4-dml).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Perde o contrato de entrada.
- **B)** Correta. Controla escopo e falha da operação explícita.
- **C)** Incorreta. Amplia o conjunto.
- **D)** Incorreta. Limite sem critério não garante chave correta.

**Conceito:** Procedure, parâmetro e transação.

**Pegadinha:** Achar que nome expressivo garante alcance e atomicidade.

**Como pensar:** Cheque entrada, predicado, quantidade afetada, erro, commit e rollback.

### Comentário S3D4Q188

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Sem `deleted`, não há evidência do estado anterior.
- **B)** Incorreta. Perde linhas quando o comando afeta várias.
- **C)** Correta. Processa todos os pares por chave e registra anterior/novo de cada mudança.
- **D)** Incorreta. A premissa de uma linha é defeituosa; cursor é desnecessário para o requisito.

**Conceito:** Trigger set-based.

**Pegadinha:** Programar pelo teste unitário de uma linha.

**Como pensar:** Modele `inserted/deleted` como relações e escreva uma única operação sobre o conjunto.

### Comentário S3D4Q189

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O novo estado não satisfaz a consulta da view.
- **B)** Incorreta. Desativação atualiza atributo; não exclui linha.
- **C)** Incorreta. View comum não é fotografia.
- **D)** Incorreta. Mudança de dados não exige recriar definição válida.

**Conceito:** View virtual e atualização da base.

**Pegadinha:** Confundir definição persistida com resultado materializado.

**Como pensar:** Reaplique mentalmente o `SELECT` da view ao estado atual da tabela.

### Comentário S3D4Q190

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Correta. Está correta: a cardinalidade do lote é variável.
- **B)** Correta. Está correta: as pseudo-tabelas representam o conjunto.
- **C)** Correta. Está correta: é um custo arquitetural relevante.
- **D)** Incorreta. Está incorreta: o evento pode abranger múltiplas linhas, e lógica escalar pode perder dados.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** Semântica multirregistro.

**Pegadinha:** No comando negativo, aceitar a frase que soa familiar a outros SGBDs ou modelos.

**Como pensar:** Teste a unidade do evento e a cardinalidade de `inserted/deleted`; a afirmação de execução obrigatoriamente por linha contradiz ambas.

### Comentário S3D4Q191

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cada requisito é atendido pelo mecanismo de menor complexidade compatível com sua forma de ativação.
- **B)** Incorreta. Inverte os quatro papéis.
- **C)** Incorreta. Não relaciona requisito e mecanismo.
- **D)** Incorreta. Mistura garantias sem aderência.

**Conceito:** Seleção integrada de objetos.

**Pegadinha:** Escolher todos os mecanismos programáveis sem testar alternativa declarativa.

**Como pensar:** Classifique cada requisito: regra, consulta, operação explícita ou reação automática.

### Comentário S3D4Q192

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Classes de comandos](semana_03_estudo.md#s3-d4-classes-comando).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Correta. Está correta.
- **B)** Incorreta. Está incorreta: `COMMIT` controla a unidade de trabalho e é classificado como TCL.
- **C)** Correta. Está correta.
- **D)** Correta. Está correta.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** Classificação de comandos.

**Pegadinha:** Associar “gravar” no sentido comum a manipulação de linhas.

**Como pensar:** Classifique o objeto direto do comando: `COMMIT` decide a transação, não cria linha.

### Comentário S3D4Q193

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate) e [restrições declarativas](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Destruição ampla não é plano de migração justificado.
- **B)** Incorreta. A mudança falha ou bloqueia antes do saneamento.
- **C)** Incorreta. Ocultar não corrige integridade.
- **D)** Correta. Percorre os filtros independentes: presença, referência, compatibilidade operacional e reversão.

**Conceito:** Migração multifiltro de constraints.

**Pegadinha:** Resolver apenas a nova definição sem considerar dados inválidos e dependências.

**Como pensar:** Valide primeiro presença e correspondência; depois implante cada garantia com teste e retorno.

### Comentário S3D4Q194

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [GO, lotes e escopo](semana_03_estudo.md#s3-d4-go-lotes-escopo).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. No SSMS e no `sqlcmd`, a ferramenta separa os lotes; por isso, a variável local T-SQL não atravessa `GO`.
- **B)** Incorreta. Não é função enviada ao mecanismo.
- **C)** Incorreta. `GO` não é `COMMIT` e não preserva o escopo da variável local entre lotes.
- **D)** Incorreta. Variável local não vira coluna.

**Conceito:** Lote cliente e escopo.

**Pegadinha:** Tratar separador visual como espaço em branco sem efeito de lote.

**Como pensar:** Identifique quem separa o texto e qual objeto tem escopo limitado ao lote.

### Comentário S3D4Q195

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Matriz de decisão](semana_03_estudo.md#s3-d4-escolha-objeto).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Aumenta complexidade e reduz clareza.
- **B)** Incorreta. Rotas diferentes podem divergir.
- **C)** Incorreta. View não substitui integridade referencial da base.
- **D)** Correta. A garantia declarativa é central e independe da aplicação.

**Conceito:** Princípio da menor complexidade.

**Pegadinha:** Associar maior quantidade de código a maior segurança.

**Como pensar:** Se a constraint expressa todo o requisito, ela é o primeiro candidato.

### Comentário S3D4Q196

**Nível:** Médio

**Uso:** Simulado

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Ignora o primeiro termo.
- **B)** Correta. O `AND` exige os dois predicados verdadeiros antes do DML.
- **C)** Incorreta. DML atua em conjunto, não apenas primeira linha.
- **D)** Incorreta. Remoção da estrutura seria DDL `DROP`.

**Conceito:** Predicado de DML.

**Pegadinha:** Ler condições como alternativas ligadas por `OR`.

**Como pensar:** Teste ambos os termos por linha e mantenha apenas a interseção.

### Comentário S3D4Q197

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mistura chaves e cria auditorias falsas.
- **B)** Incorreta. Falha em cardinalidade, estado anterior e cobertura.
- **C)** Incorreta. Introduz efeitos externos e não demonstra as garantias.
- **D)** Correta. O join preserva identidade, o filtro seleciona mudança e a operação set-based trata o lote.

**Conceito:** Trigger multirregistro, identidade e mudança.

**Pegadinha:** Resolver apenas um dos filtros — normalmente a cardinalidade — e esquecer pareamento ou diferença.

**Como pensar:** Valide três invariantes: todas as chaves, par antigo/novo correto e somente alterações reais.

### Comentário S3D4Q198

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Views e caminhos de acesso](semana_03_estudo.md#s3-d4-views-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Alias não remove o dado.
- **B)** Incorreta. Acesso direto contorna a projeção.
- **C)** Correta. A resposta percorre conteúdo exposto, autorização e caminhos alternativos.
- **D)** Incorreta. Não há ajuste automático de privilégios ou inferência.

**Conceito:** View, privilégio e exposição.

**Pegadinha:** Analisar apenas o SQL da view e declarar segurança concluída.

**Como pensar:** Desenhe quem pode consultar cada objeto e quais dados podem ser reconstruídos.

### Comentário S3D4Q199

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Evolução e remoção de estrutura](semana_03_estudo.md#s3-d4-alter-drop-truncate).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra estado, consumidores e recuperação operacional.
- **B)** Incorreta. Dependências podem quebrar.
- **C)** Incorreta. Excluir objetos não resolve o serviço nem a reversão.
- **D)** Incorreta. Conversão implícita pode perder dados e mantém dependências.

**Conceito:** Mudança estrutural multifiltro.

**Pegadinha:** Focar só na sintaxe do `ALTER` e ignorar dados e consumidores.

**Como pensar:** Antes do DDL, responda: os dados cabem, quem depende e como voltar?

### Comentário S3D4Q200

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não satisfaz chamada/escopo e pode perder linhas.
- **B)** Incorreta. Separador de lote não substitui transação e rompe o bloco.
- **C)** Incorreta. Módulo armazenado não é garantia transacional.
- **D)** Correta. Percorre escopo, unidade de trabalho e caminho de falha, mantendo as escritas juntas.

**Conceito:** Procedure com escopo, atomicidade e erro.

**Pegadinha:** Implementar o caminho feliz e presumir rollback automático.

**Como pensar:** Desenhe entrada e cardinalidade; depois BEGIN, duas escritas, COMMIT e caminho CATCH/ROLLBACK.

#### Comentário Extra Dia 4.1

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Eficiência não transfere competência atribuída pelo ordenamento a outro órgão.
- **B)** Correta. A revisão exige atuação eficiente dentro do ordenamento.
- **C)** Incorreta. Legalidade condiciona toda atuação administrativa, inclusive a opção mais econômica.
- **D)** Incorreta. Para a Administração, ausência de proibição não equivale a autorização de agir fora da competência e do procedimento.

**Conceito:** Legalidade e eficiência.

**Pegadinha:** Usar um princípio para anular outro.

**Como pensar:** Verifique primeiro competência e base jurídica; eficiência orienta o modo legítimo de agir.

#### Comentário Extra Dia 4.2

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Resultado institucional não autoriza promoção nominal do agente público.
- **B)** Incorreta. Conhecimento pessoal não é critério objetivo de prioridade, ainda que se invoque agilidade.
- **C)** Correta. Mantém foco no interesse e na finalidade pública.
- **D)** Incorreta. Impessoalidade admite diferenciações objetivas previstas em lei; não exige ignorar prioridades legítimas.

**Conceito:** Impessoalidade.

**Pegadinha:** Confundir divulgação do serviço com promoção do agente.

**Como pensar:** Pergunte quem é beneficiado pela mensagem: o público ou a imagem pessoal do gestor.

**Justificativa de comprimento:** A correta descreve a finalidade pública sem ressalvas; os distratores acrescentam condições destinadas a disfarçar favorecimento ou promoção pessoal.

#### Comentário Extra Dia 4.3

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Publicidade não é divulgação sem limites.
- **B)** Incorreta. Sigilo previsto continua relevante.
- **C)** Correta. A alternativa preserva transparência e limites jurídicos.
- **D)** Incorreta. Relatórios podem ser publicados com tratamento adequado.

**Conceito:** Publicidade com limites.

**Pegadinha:** Transformar regra de transparência em exposição irrestrita.

**Como pensar:** Separe informação de interesse público de dado individual protegido e verifique a base de divulgação.

#### Comentário Extra Dia 4.4

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Inconveniência de ato válido se relaciona à revogação.
- **B)** Incorreta. Inverte os fundamentos.
- **C)** Incorreta. Os institutos têm pressupostos diferentes.
- **D)** Correta. Aplica legalidade à anulação e mérito administrativo à revogação.

**Conceito:** Anulação versus revogação.

**Pegadinha:** Memorizar apenas que ambas retiram efeitos.

**Como pensar:** Pergunte se o problema está na validade ou na conveniência de ato válido.

#### Comentário Extra Dia 4.5

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não é controle de mérito.
- **B)** Correta. Reúne sanabilidade e limites.
- **C)** Incorreta. Generaliza indevidamente.
- **D)** Incorreta. Não basta vontade privada.

**Conceito:** Convalidação.

**Pegadinha:** Interpretar “corrigir” como poder ilimitado.

**Como pensar:** Teste sanabilidade, autorização e ausência de prejuízo.

#### Comentário Extra Dia 4.6

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Distingue organização interna de transferência para outro centro.
- **B)** Incorreta. Descreve desconcentração.
- **C)** Incorreta. A teoria separa os institutos.
- **D)** Incorreta. Nova pessoa não é requisito de desconcentração.

**Conceito:** Descentralização e desconcentração.

**Pegadinha:** Usar os prefixos sem observar personalidade/centro de competência.

**Como pensar:** Pergunte se continua na mesma pessoa jurídica.

#### Comentário Extra Dia 4.7

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não tem natureza associativa privada.
- **B)** Correta. É a classificação indicada.
- **C)** Incorreta. Órgão e entidade não se confundem.
- **D)** Incorreta. Autarquia não pertence à Direta.

**Conceito:** Autarquia.

**Pegadinha:** Confundir entidade descentralizada com órgão desconcentrado.

**Como pensar:** Identifique personalidade própria e vínculo com a Administração Indireta.

#### Comentário Extra Dia 4.8

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A solução exige compatibilização conforme informação, finalidade e base.
- **B)** Incorreta. A presença de dado pessoal exige análise, mas não elimina automaticamente o regime de acesso à informação.
- **C)** Incorreta. A LGPD também alcança o tratamento de dados por entes públicos.
- **D)** Incorreta. Especialidade não dispensa a leitura conjunta das finalidades e bases aplicáveis ao caso.

**Conceito:** LAI e LGPD.

**Pegadinha:** Tratar diplomas como mutuamente excludentes.

**Como pensar:** Identifique o dever de transparência e, simultaneamente, as condições do tratamento de dados.

**Justificativa de comprimento:** A correta resume a compatibilização exigida; os distratores precisam formular falsas regras de prevalência para parecerem juridicamente plausíveis.

#### Comentário Extra Dia 4.9

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Suprime requisito do regresso.
- **B)** Incorreta. Nega a premissa constitucional revisada.
- **C)** Correta. Distingue duas relações e seus requisitos.
- **D)** Incorreta. Indenização não prova elemento subjetivo do agente.

**Conceito:** Responsabilidade estatal e regressiva.

**Pegadinha:** Transferir automaticamente o regime da relação Estado-vítima para Estado-agente.

**Como pensar:** Separe sujeitos e requisitos de cada relação antes de concluir.

#### Comentário Extra Dia 4.10

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Sigilo total também pode violar transparência.
- **B)** Incorreta. Exposição primeiro não é proteção adequada.
- **C)** Incorreta. Ignora limites e necessidade.
- **D)** Correta. Permite controle social com redução de exposição e exige fundamento para individualização.

**Conceito:** Transparência proporcional.

**Pegadinha:** Escolher entre tudo ou nada.

**Como pensar:** Defina finalidade pública, dados mínimos e forma de divulgação antes de abrir informação individual.

#### Comentário Extra Dia 4.11

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Correta. Está correta.
- **B)** Correta. Está correta.
- **C)** Incorreta. Está incorreta: eficiência não cria competência nem afasta legalidade.
- **D)** Correta. Está correta.

**Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.

**Conceito:** Competência e princípios.

**Pegadinha:** No comando negativo, aceitar a solução “eficiente” sem testar validade.

**Como pensar:** Submeta a vantagem operacional ao filtro de competência e legalidade.

#### Comentário Extra Dia 4.12

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Administração Pública](semana_03_estudo.md#s3-d4-b4-administracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Aplica mérito/limites ao ato e compatibiliza transparência com proteção.
- **B)** Incorreta. Inconveniência de ato válido não é vício de legalidade.
- **C)** Incorreta. Convalidação corrige vício sanável, não mérito de ato válido; sigilo total é excessivo.
- **D)** Incorreta. Validade não impede toda revogação, e publicidade não exige nomes.

**Conceito:** Revogação e publicidade com limites.

**Pegadinha:** Resolver corretamente um eixo e errar o outro.

**Como pensar:** Separe destino do ato de forma de divulgação; aplique o regime próprio a cada decisão.

#### Comentário Extra Dia 4.13

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Separa sujeito do verbo sem intercalação.
- **B)** Incorreta. Emprega vírgulas sem pares/funções adequadas.
- **C)** Incorreta. Separa verbo do objeto direto.
- **D)** Correta. Não separa sujeito e verbo nem verbo e complemento.

**Conceito:** Pontuação da ordem direta.

**Pegadinha:** Inserir pausa oral entre sujeito longo e verbo.

**Como pensar:** Localize sujeito, verbo e complemento; não os separe sem elemento intercalado.

#### Comentário Extra Dia 4.14

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não fecha argumento.
- **B)** Incorreta. A explicativa seria isolada por vírgulas.
- **C)** Correta. A ausência de vírgulas delimita o referente.
- **D)** Incorreta. Não apresenta causa.

**Conceito:** Oração adjetiva restritiva.

**Pegadinha:** Ignorar que a pontuação altera o alcance do referente.

**Como pensar:** Pergunte se a oração seleciona parte do conjunto ou comenta todo ele.

#### Comentário Extra Dia 4.15

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Antes de infinitivo não ocorre o artigo feminino.
- **B)** Incorreta. Antes de artigo indefinido não há fusão `a+a`.
- **C)** Incorreta. O segundo `a` introduz infinitivo.
- **D)** Correta. `encaminhar a` exige preposição, e “a unidade” admite artigo: `a + a = à`.

**Conceito:** Crase.

**Pegadinha:** Usar acento apenas porque a palavra seguinte é feminina.

**Como pensar:** Teste regência do termo anterior e presença do artigo no termo seguinte.

#### Comentário Extra Dia 4.16

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A forma singular está correta.
- **B)** Incorreta. `Haver` existencial permanece singular.
- **C)** Incorreta. Também deveria estar no singular.
- **D)** Incorreta. Na locução, o auxiliar acompanha a impessoalidade: deve haver.

**Conceito:** `Haver` com sentido de existir.

**Pegadinha:** Fazer o verbo concordar com o termo plural posterior.

**Como pensar:** Substitua mentalmente por “existia”; mantenha `haver` no singular.

#### Comentário Extra Dia 4.17

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Cria condicional e negação ausentes.
- **B)** Correta. Mantém os dois fatos e a tensão concessiva.
- **C)** Incorreta. Troca concessão por causa e conclusão absoluta.
- **D)** Incorreta. Inverte a conclusão.

**Conceito:** Preservação de relação lógica.

**Pegadinha:** Preservar vocabulário, mas trocar o conectivo e a tese.

**Como pensar:** Compare os compromissos semânticos antes e depois: benefício reconhecido e limite mantido.

#### Comentário Extra Dia 4.18

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Jargão desconectado prejudica coerência.
- **B)** Incorreta. Ideia nova quebra o fechamento.
- **C)** Correta. Essa é a função descrita na revisão.
- **D)** Incorreta. Retomada não exige repetição literal.

**Conceito:** Conclusão discursiva.

**Pegadinha:** Usar o último parágrafo para compensar argumento ausente.

**Como pensar:** Confira se cada frase final decorre de eixo já desenvolvido.

#### Comentário Extra Dia 4.19

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Muda foco e quantificação.
- **B)** Correta. Mantém sujeito, negação do ato e recorte “desnecessários”.
- **C)** Incorreta. Amplia a negação para todo dado.
- **D)** Incorreta. Afirma a divulgação que o original nega.

**Conceito:** Escopo de negação.

**Pegadinha:** Mover `não` ou quantificador e alterar o conjunto negado.

**Como pensar:** Marque verbo negado, objeto e modificador antes de reescrever.

#### Comentário Extra Dia 4.20

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português, introdução e conclusão](semana_03_estudo.md#s3-d4-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Separa sujeito/verbo e anuncia argumento novo.
- **B)** Incorreta. Há crase indevida antes de infinitivo e `haver` existencial deveria ser singular.
- **C)** Incorreta. Crase indevida em “orientam a gestão”, vírgula entre sujeito e verbo e salto causal.
- **D)** Correta. Preserva sintaxe, usa `à sociedade` por regência e artigo e fecha os eixos já apresentados.

**Conceito:** Revisão multifiltro.

**Pegadinha:** Corrigir um ponto isolado e deixar dois desvios na mesma alternativa.

**Como pensar:** Audite em três passagens: estrutura sujeito-verbo, crase por dupla exigência e função argumentativa da conclusão.
