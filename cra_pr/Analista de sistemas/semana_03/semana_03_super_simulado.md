# Super Simulado — Semana 3

**Finalidade:** 60 questões autorais e integradoras de Banco de Dados, SQL, transações, otimização e Business Intelligence, calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão oficial.

**Aplicação sugerida:** 2h30 sem consulta. Marque também as questões em que houve dúvida; a correção integral deve ocorrer em sessão posterior, com retorno à seção indicada da apostila.

## Cobertura programática auditada

Há exatamente dez itens por dia. A matriz inicial previa 24 questões médias, 24 difíceis e 12 muito difíceis; após as auditorias semânticas e a recalibração da complexidade efetiva dos itens, a distribuição final passou a **43 médias, 14 difíceis e 3 muito difíceis**, sem alteração dos IDs nem dos gabaritos.

| Dia | Conteúdo predominante | Questões |
|---:|---|---|
| 1 | Arquitetura de banco de dados, independência e metadados | S3S001–S3S010 |
| 2 | Modelo relacional, MER, mapeamento e normalização | S3S011–S3S020 |
| 3 | SQL ANSI, junções, agrupamento e subconsultas | S3S021–S3S030 |
| 4 | DDL, DML, T-SQL, views, procedures e triggers | S3S031–S3S040 |
| 5 | Transações, concorrência, recuperação, integridade e segurança | S3S041–S3S050 |
| 6 | Índices, otimização, SGBDs e Business Intelligence | S3S051–S3S060 |

## Questões — Dia 1

### S3S001 — Responsabilidade central do SGBD

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Funções centrais de um SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

Em um sistema corporativo, qual atividade pertence diretamente ao SGBD?

A) Definir sozinho as regras estratégicas de atendimento do órgão.

B) Controlar concorrência, integridade, autorização e recuperação dos dados.

C) Substituir os usuários responsáveis por interpretar os relatórios.

D) Elaborar o modelo de negócio sem participação da Administração de Dados.

### S3S002 — Esquema e instância

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

Às 9h, a tabela `profissional` contém 800 linhas; às 17h, contém 830, sem alteração de colunas ou restrições. O que mudou?

A) O esquema externo, pois toda inclusão de linha cria uma nova visão.

B) O esquema conceitual, pois a cardinalidade faz parte da definição estável.

C) O catálogo, que deixa de registrar a estrutura quando entram novos dados.

D) A instância do banco, enquanto o esquema permaneceu o mesmo.

### S3S003 — Administração de Dados e DBA

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

Assinale a divisão de responsabilidades mais adequada.

A) A AD governa significados e padrões; o DBA administra a implementação e a operação do SGBD.

B) A AD executa backups diários; o DBA define sozinho o significado corporativo dos dados.

C) A AD cuida apenas de hardware; o DBA limita-se a redigir glossários de negócio.

D) A AD e o DBA são denominações obrigatoriamente idênticas para a mesma função.

### S3S004 — Independência física

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Independência física e lógica de dados](semana_03_estudo.md#s3-d1-independencia-dados).

Qual mudança exemplifica independência física de dados quando não exige alteração das aplicações?

A) Dividir uma entidade conceitual em duas relações visíveis aos usuários.

B) Renomear um atributo conceitual usado por todas as visões externas.

C) Reorganizar arquivos e índices, preservando os esquemas conceitual e externo.

D) Remover uma coluna pública e exigir ajuste imediato de cada relatório.

### S3S005 — Falha na separação de níveis

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

Após o DBA trocar a organização de arquivos e reconstruir índices, um relatório passou a exigir mudanças em seu código, embora a estrutura conceitual não tenha sido alterada. O diagnóstico mais preciso é:

A) houve falha de independência lógica entre os esquemas externo e conceitual.

B) ocorreu mudança de instância, que sempre obriga recompilar as aplicações.

C) a independência física não foi preservada entre os níveis interno e conceitual.

D) o catálogo deixou de ser metadado e passou a integrar a instância do usuário.

### S3S006 — Consulta ao catálogo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Uma ferramenta precisa listar tabelas, colunas, tipos, chaves e privilégios sem examinar cada linha de negócio. A fonte apropriada é:

A) o catálogo do sistema, porque reúne metadados sobre estruturas e autorizações.

B) a instância operacional, porque cada tupla descreve formalmente sua própria coluna.

C) o log de aplicação, porque mensagens de execução substituem o dicionário de dados.

D) a visão externa de um usuário, porque ela contém necessariamente todos os objetos.

### S3S007 — Sistema de banco de dados

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

Ao auditar uma solução, a equipe identificou base armazenada, software gerenciador, aplicações, usuários e procedimentos operacionais. Esse conjunto corresponde:

A) apenas ao banco de dados, pois software e pessoas são atributos das relações.

B) somente ao SGBD, pois aplicações e procedimentos são módulos internos obrigatórios.

C) ao catálogo de dados, pois ele contém fisicamente todos os componentes da solução.

D) ao sistema de banco de dados, conceito mais amplo que o banco e o SGBD isolados.

### S3S008 — Independência lógica

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Independência física e lógica de dados](semana_03_estudo.md#s3-d1-independencia).

Uma entidade conceitual foi decomposta, mas uma visão externa compatível evitou mudanças no relatório legado. O caso demonstra principalmente:

A) mudança exclusiva da instância, sem relação com os níveis arquiteturais.

B) independência lógica, pois a visão protegeu o usuário da mudança conceitual.

C) independência física, pois toda decomposição modifica apenas arquivos e índices.

D) ausência de esquema externo, pois a compatibilidade foi mantida pelo catálogo.

### S3S009 — Classificação integrada de mudanças

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Contrastes decisivos](semana_03_estudo.md#s3-d1-contrastes).

Considere quatro ações: I. reconstruir um índice; II. incluir um atributo no modelo corporativo; III. manter uma visão com os nomes antigos; IV. consultar tipos e restrições registrados pelo SGBD. A classificação correta é:

A) I interna/física; II conceitual; III externa; IV consulta a metadados.

B) I externa; II interna/física; III conceitual; IV consulta à instância.

C) I conceitual; II externa; III interna; IV atualização de dados de negócio.

D) I instância; II catálogo; III recuperação; IV independência exclusivamente física.

### S3S010 — Governança, operação e transparência arquitetural

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba), com apoio de [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-arquitetura-bd).

O órgão quer padronizar o significado de “registro ativo”, reorganizar o armazenamento e manter relatórios legados estáveis. Qual plano articula corretamente papéis e níveis?

A) A AD governa o significado e o DBA reorganiza o armazenamento, mas todos os relatórios são reescritos para refletir a mudança interna.

B) A AD governa o significado; o DBA executa a mudança física; mapeamentos preservam as visões externas.

C) O DBA fixa o significado corporativo, a AD reconstrói os índices e a estabilidade externa fica a cargo de cada usuário.

D) AD e DBA alinham conceito e armazenamento, mas removem os mapeamentos e fazem os relatórios consultar diretamente a organização interna.

## Questões — Dia 2

### S3S011 — Chaves candidatas

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

Uma relação possui duas identificações mínimas e únicas: `id` e `cpf`. Se `id` for escolhida como chave primária, `cpf` permanece:

A) chave estrangeira, ainda que não referencie outra relação.

B) atributo não chave, pois somente a primária pode identificar tuplas.

C) chave candidata alternativa, por continuar mínima e única.

D) superchave não mínima, pois toda chave não escolhida recebe atributos extras.

### S3S012 — Entidade fraca

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

No MER, `Parcela` só é identificada pelo número da parcela em conjunto com o contrato proprietário. Isso caracteriza:

A) atributo multivalorado, convertido diretamente em uma coluna repetida.

B) entidade associativa, obrigatoriamente independente de qualquer proprietário.

C) entidade fraca, com identificação dependente da chave do proprietário.

D) relacionamento ternário, pois toda identificação composta exige três entidades.

### S3S013 — Mapeamento de relacionamento 1:N

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Regras de mapeamento MER–relacional](semana_03_estudo.md#s3-d2-mapeamento).

No relacionamento 1:N entre `Unidade` e `Profissional`, cada profissional pertence a uma unidade. O mapeamento usual coloca:

A) a chave de `Profissional` em `Unidade`, permitindo um único profissional por unidade.

B) uma tabela de junção obrigatória, ainda que o relacionamento não possua atributos.

C) as duas chaves como colunas repetidas em ambas as relações participantes.

D) a chave de `Unidade` como chave estrangeira no lado N, em `Profissional`.

### S3S014 — Primeira Forma Normal

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Primeira Forma Normal — 1FN](semana_03_estudo.md#s3-d2-1fn).

Uma coluna `telefones` armazena vários números separados por vírgula. A correção alinhada à 1FN é:

A) manter a lista e criar um índice textual para cada posição do conteúdo.

B) representar cada ocorrência de telefone de forma atômica em estrutura própria.

C) mover a lista para outra coluna da mesma tabela, preservando o separador.

D) duplicar a linha principal inteira para cada número, sem chave que os distinga.

### S3S015 — Dependência parcial e 2FN

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Segunda Forma Normal — 2FN](semana_03_estudo.md#s3-d2-2fn).

Em `ItemPedido(pedido_id, produto_id, data_pedido, quantidade)`, a chave é composta e `pedido_id → data_pedido`. Qual ação elimina a violação de 2FN?

A) Remover `quantidade`, pois todo atributo numérico depende parcialmente da chave.

B) Levar `data_pedido` para a relação de pedido, onde depende da chave completa.

C) Manter a estrutura e declarar `data_pedido` como `NOT NULL` e `UNIQUE`.

D) Acrescentar `data_pedido` à chave de item, sem separar os fatos descritos.

### S3S016 — Dependência transitiva e 3FN

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Terceira Forma Normal — 3FN](semana_03_estudo.md#s3-d2-3fn).

Em `Profissional(id, unidade_id, nome_unidade)`, valem `id → unidade_id` e `unidade_id → nome_unidade`. Para atingir 3FN, deve-se:

A) excluir `unidade_id` e usar apenas o nome textual como ligação entre as tabelas.

B) repetir `nome_unidade` em cada linha e criar um índice para ocultar a redundância.

C) tornar `nome_unidade` parte da chave primária da relação `Profissional`.

D) separar os dados da unidade e manter em `Profissional` a referência à sua chave.

### S3S017 — Qualidade de uma decomposição

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Decomposição sem perda e preservação de dependências](semana_03_estudo.md#s3-d2-decomposicao).

Ao decompor uma relação, quais propriedades devem ser avaliadas separadamente?

A) Junção sem perda e redução do número de tabelas, ainda que alguma dependência deixe de ser verificável sem recomposição.

B) Preservação de dependências e eliminação de redundância, mesmo que a junção das partes produza tuplas espúrias.

C) Junção sem perda, para reconstruir a relação original sem tuplas espúrias, e preservação das dependências relevantes para validação.

D) Ausência de redundância e uso de chaves estrangeiras, supondo que esses critérios já garantam a reconstrução correta.

### S3S018 — BCNF

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Forma Normal de Boyce–Codd — BCNF](semana_03_estudo.md#s3-d2-bcnf).

Qual condição sintetiza a BCNF para toda dependência funcional não trivial `X → Y`?

A) `X` deve ser superchave da relação em que a dependência é considerada.

B) `Y` deve ser sempre atributo primo, mesmo quando `X` não identifica tuplas.

C) `X` e `Y` devem pertencer obrigatoriamente à chave primária escolhida.

D) A relação deve possuir apenas uma chave candidata e nenhum atributo nulo.

### S3S019 — Caso integrado de mapeamento

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Entidades, atributos e relacionamentos](semana_03_estudo.md#s3-d2-mer), com apoio de [Regras de mapeamento](semana_03_estudo.md#s3-d2-mapeamento).

Um profissional pode possuir várias certificações; uma certificação pode pertencer a vários profissionais; a associação registra `data_validacao`. Qual desenho relacional preserva cardinalidade, identificação e atributo do relacionamento?

A) Coluna multivalorada `certificacoes` em `Profissional`, contendo também todas as datas.

B) Chave de `Profissional` em `Certificacao`, permitindo apenas um titular por certificação.

C) Relação associativa com as duas chaves estrangeiras, chave adequada e `data_validacao`.

D) Cópia integral de `Certificacao` para cada profissional, sem vínculo entre registros iguais.

### S3S020 — Normalização orientada pelas dependências

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Dependências funcionais e anomalias](semana_03_estudo.md#s3-d2-dependencias), com apoio de [2FN](semana_03_estudo.md#s3-d2-2fn) e [3FN](semana_03_estudo.md#s3-d2-3fn).

Uma planilha migrada usa chave `(protocolo, item)`; `protocolo → data_abertura` e `setor_id → nome_setor`, enquanto cada protocolo possui um setor. Qual sequência trata as duas redundâncias sem perder o vínculo do item?

A) Manter tudo junto, pois uma chave composta impede dependências parciais e transitivas.

B) Separar protocolo dos itens e setor de seus dados, preservando as chaves estrangeiras necessárias.

C) Criar apenas uma tabela de setores e repetir `data_abertura` em todos os itens do protocolo.

D) Remover `protocolo` da chave e usar `nome_setor` como identificador único de cada item.

## Questões — Dia 3

### S3S021 — Ordem lógica da consulta

**Nível:** Médio

**Uso:** Simulado

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

Em uma consulta agrupada, qual etapa lógica ocorre antes de `GROUP BY`?

A) `WHERE`, que filtra as linhas produzidas por `FROM` e `JOIN`.

B) `SELECT`, que cria os aliases usados por qualquer cláusula anterior.

C) `ORDER BY`, que define primeiro a ordem física de todos os registros.

D) `HAVING`, que elimina linhas individuais antes de existir agrupamento.

### S3S022 — Preservação no LEFT JOIN

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

Um relatório deve listar todas as unidades, inclusive as que não possuem profissionais ativos. Qual construção preserva esse requisito?

A) `INNER JOIN profissional p ON p.unidade_id=u.id AND p.ativo='S'`.

B) `CROSS JOIN profissional p WHERE p.ativo='S' AND p.unidade_id=u.id`.

C) `LEFT JOIN profissional p ON p.unidade_id=u.id AND p.ativo='S'`.

D) `LEFT JOIN profissional p ON p.unidade_id=u.id WHERE p.ativo='S'`.

### S3S023 — Filtro de grupos

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

Para manter apenas unidades com pelo menos cinco profissionais, a condição apropriada é:

A) `WHERE COUNT(*) >= 5`, antes de qualquer agrupamento.

B) `HAVING COUNT(*) >= 5`, depois de agrupar por unidade.

C) `ON COUNT(*) >= 5`, sem relacionar as tabelas participantes.

D) `ORDER BY COUNT(*) >= 5`, usando a ordenação como filtro.

### S3S024 — Semântica de EXISTS

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

Em uma subconsulta usada por `EXISTS`, o que determina o valor verdadeiro?

A) A primeira coluna projetada possuir valor numérico diferente de zero.

B) A subconsulta retornar exatamente uma coluna e uma linha não nula.

C) Todas as colunas projetadas terem valores conhecidos e distintos.

D) A existência de ao menos uma linha, independentemente do valor projetado.

### S3S025 — NOT IN e valor nulo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

Uma antijunção escrita com `id NOT IN (SELECT profissional_id FROM bloqueio)` deixou de retornar linhas quando a subconsulta passou a conter `NULL`. A correção conceitualmente segura é:

A) trocar `NOT IN` por `IN`, mantendo o mesmo sentido de exclusão.

B) comparar `id <> NULL`, tornando a ausência uma condição verdadeira.

C) aplicar `DISTINCT`, pois ele converte automaticamente `NULL` em zero.

D) usar `NOT EXISTS` correlacionado ou excluir explicitamente nulos da subconsulta.

### S3S026 — ON versus WHERE

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplo de filtro em ON versus WHERE](semana_03_estudo.md#s3-d3-exemplos-b2).

Considere `unidade u LEFT JOIN profissional p`. O filtro `p.ativo='S'` foi movido de `ON` para `WHERE`. Qual consequência pode ocorrer?

A) O resultado ganha unidades sem correspondência, pois `WHERE` cria linhas nulas.

B) Unidades sem profissional ativo podem desaparecer, aproximando o efeito de `INNER JOIN`.

C) A cardinalidade fica obrigatoriamente igual, porque `ON` e `WHERE` são intercambiáveis.

D) O SGBD rejeita a consulta, pois filtros de colunas juntadas só podem aparecer em `ON`.

### S3S027 — UNION e duplicatas

**Nível:** Médio

**Uso:** Simulado

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

Duas consultas compatíveis retornam, respectivamente, `{PR, SC}` e `{PR, RS}`. Qual resultado corresponde a `UNION`, e não a `UNION ALL`?

A) `{PR, SC, RS}`, com eliminação da ocorrência repetida de `PR`.

B) `{PR, PR}`, mantendo somente o elemento presente nas duas entradas.

C) `{SC, RS}`, removendo todos os valores que aparecem na primeira consulta.

D) `{PR, SC, PR, RS}`, preservando integralmente as quatro ocorrências.

### S3S028 — Máximo por grupo com empate

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Exemplo de máximo correlacionado com empate](semana_03_estudo.md#s3-d3-exemplos-b2).

Para listar todos os pagamentos de maior valor de cada profissional, inclusive empates, qual predicado é adequado?

A) `pg.valor > (SELECT MAX(valor) FROM pagamento)`, sem correlação.

B) `pg.id = (SELECT MAX(id) FROM pagamento)`, usando identificador como valor.

C) `pg.valor = (SELECT MAX(x.valor) FROM pagamento x WHERE x.profissional_id=pg.profissional_id)`.

D) `pg.valor IN (SELECT MIN(valor) FROM pagamento GROUP BY status)`, agrupando outro critério.

### S3S029 — Relatório integrado com ausência

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Junções](semana_03_estudo.md#s3-d3-joins), com apoio de [Agregação](semana_03_estudo.md#s3-d3-agrupamento-having).

O relatório deve exibir cada unidade, contar apenas profissionais ativos e manter unidades com contagem zero; depois, deve conservar somente as unidades cuja contagem seja menor que dois. Qual desenho atende aos três filtros?

A) `LEFT JOIN` com `ativo='S'` em `ON`, `COUNT(p.id)` e `HAVING COUNT(p.id)<2`.

B) `INNER JOIN` com ativos em `WHERE`, `COUNT(*)` e `WHERE COUNT(*)<2`.

C) `LEFT JOIN` sem condição de chave, `COUNT(*)` e `ORDER BY COUNT(*)<2`.

D) `CROSS JOIN` com ativos em `HAVING`, `COUNT(u.id)` e ausência de agrupamento.

### S3S030 — Paginação estável e granularidade

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ordenação total e paginação estável](semana_03_estudo.md#s3-d3-exemplos-b2), com apoio de [Granularidade do agrupamento](semana_03_estudo.md#s3-d3-agrupamento-having).

Uma consulta agrupa pagamentos por profissional e pagina o resultado. Vários profissionais têm o mesmo total. Para impedir repetição ou salto entre páginas e preservar uma linha por profissional, deve-se:

A) incluir `pagamento.id` no `GROUP BY` e ordenar somente pelo total agregado.

B) remover o agrupamento e aplicar `DISTINCT` depois da paginação.

C) agrupar pela chave do profissional e ordenar por total mais uma chave única de desempate.

D) ordenar apenas pelo nome exibido, ainda que nomes e totais possam empatar.

## Questões — Dia 4

### S3S031 — Classes de comandos

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Classes por finalidade](semana_03_estudo.md#s3-d4-classes-comando).

Qual associação entre comando e finalidade está correta?

A) `GRANT` — alteração das linhas armazenadas por DML.

B) `COMMIT` — definição estrutural de tabelas por DDL.

C) `UPDATE` — controle de privilégios de usuários por DCL.

D) `ALTER TABLE` — modificação da estrutura por DDL.

### S3S032 — Integridade declarativa

**Nível:** Médio

**Uso:** Simulado

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Uma coluna `uf` deve aceitar somente `PR`, `SC` ou `RS`. Qual mecanismo expressa diretamente a regra no esquema?

A) `DEFAULT`, pois ele corrige qualquer valor inválido informado pelo usuário.

B) `CHECK`, com predicado que limita a coluna ao conjunto permitido.

C) `INDEX`, pois a ordenação física impede valores fora do domínio.

D) `VIEW`, pois toda visão valida automaticamente as inserções na base.

### S3S033 — Natureza de uma view

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

Uma view comum consulta profissionais ativos. Depois que Ana é desativada, uma nova consulta à view deixa de exibi-la. Isso ocorre porque:

A) a view armazena uma cópia permanente e apaga fisicamente a linha desativada.

B) toda view possui trigger automática que replica alterações para uma tabela própria.

C) a definição é reaplicada aos dados atuais, não sendo cópia materializada por padrão.

D) a view revoga o acesso à linha da tabela base quando o predicado deixa de ser atendido.

### S3S034 — Escolha de stored procedure

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

Uma operação deve ser chamada explicitamente, receber `@id`, atualizar dados e devolver um código de resultado. O primeiro candidato é:

A) uma stored procedure parametrizada.

B) uma trigger vinculada a qualquer leitura.

C) uma constraint `UNIQUE` sobre o identificador.

D) uma view sem parâmetros e sem comando de atualização.

### S3S035 — Separador GO

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-transact-sql).

Em scripts do ecossistema SQL Server, a interpretação adequada de `GO` é:

A) cláusula de `CREATE PROCEDURE` que executa automaticamente a rotina recém-criada.

B) instrução DML que confirma definitivamente todas as transações abertas no servidor.

C) separador de lotes reconhecido pela ferramenta cliente, não comando T-SQL enviado ao mecanismo.

D) função escalar do padrão SQL que reinicia variáveis sem encerrar o lote corrente.

### S3S036 — Trigger multirregistro

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

No SQL Server, uma única instrução atualiza 200 linhas e a trigger precisa auditar somente mudanças reais de `ativo`. Qual desenho é seguro?

A) Unir `deleted` e `inserted` pela chave, filtrar diferenças e inserir o conjunto na auditoria.

B) Executar a trigger manualmente 200 vezes, passando uma chave a cada chamada.

C) Ler uma linha arbitrária de `inserted` em variável escalar e ignorar as demais.

D) Pressupor que a trigger será disparada uma vez por linha e usar o último valor disponível.

### S3S037 — Prévia antes do UPDATE

**Nível:** Médio

**Uso:** Simulado

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

Antes de um `UPDATE` em lote, qual prática reduz o risco de alcançar linhas indevidas?

A) Executar primeiro o `UPDATE` em transação e avaliar somente depois a contagem de linhas afetadas.

B) Executar `SELECT` com o mesmo predicado e conferir quantidade, chaves e escopo.

C) Consultar uma amostra com predicado mais amplo e inferir dela quais linhas o `UPDATE` alcançará.

D) Usar apenas a cardinalidade estimada do plano como substituta da conferência das chaves reais.

### S3S038 — View e controle de acesso

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplo de view e privilégio sobre a base](semana_03_estudo.md#s3-d4-exemplos-b2).

Uma view omite CPF, mas o mesmo usuário conserva `SELECT` direto na tabela base. Qual conclusão é correta?

A) A view anonimiza definitivamente a coluna, mesmo por outros caminhos de acesso.

B) A omissão revoga de modo implícito todos os privilégios concedidos sobre a base.

C) O usuário só verá a view, porque objetos derivados sempre prevalecem sobre tabelas.

D) A view não basta; também é necessário controlar os privilégios e caminhos alternativos.

### S3S039 — Migração para FK obrigatória

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Migração para NOT NULL](semana_03_estudo.md#s3-d4-exemplos-b1), com apoio de [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

Uma coluna opcional passará a ser `NOT NULL` e chave estrangeira, mas há nulos e referências órfãs. Qual plano preserva dados e permite reversão?

A) Criar primeiro a FK com a coluna ainda anulável e depois impor `NOT NULL`, sem sanear referências órfãs.

B) Inventariar, definir tratamento, sanear, validar a tabela pai, aplicar constraints e manter rollback.

C) Corrigir apenas os nulos, criar `NOT NULL` e FK e deixar as referências órfãs para tratamento posterior.

D) Excluir automaticamente nulos e órfãos sem regra aprovada e aplicar as constraints sem plano de reversão.

### S3S040 — Procedure com atomicidade explícita

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Exemplo de procedure e atomicidade](semana_03_estudo.md#s3-d4-exemplos-b2), com apoio de [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

Uma procedure desativa um cadastro, grava auditoria e deve deixar ambas as ações concluídas ou nenhuma. Qual desenho atende ao requisito?

A) Executar os dois comandos sem transação, pois o módulo já garante atomicidade implícita.

B) Confirmar após a primeira atualização e tentar compensar a auditoria se houver erro.

C) Abrir transação, mas registrar o erro e confirmar mesmo quando a auditoria falhar.

D) Validar parâmetros, abrir transação, executar ambas as ações, confirmar ao fim e reverter no erro.

## Questões — Dia 5

### S3S041 — Atomicidade e durabilidade

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Transação e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Em uma transferência, débito e crédito devem ocorrer juntos; depois do `COMMIT`, devem sobreviver à queda. As propriedades destacadas são, respectivamente:

A) consistência e isolamento.

B) atomicidade e durabilidade.

C) isolamento e atomicidade.

D) durabilidade e consistência.

### S3S042 — Leitura suja

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Concorrência e níveis de isolamento](semana_03_estudo.md#s3-d5-concorrencia).

T1 altera um saldo sem confirmar; T2 lê esse novo valor; depois T1 executa `ROLLBACK`. T2 realizou:

A) leitura suja, pois observou dado ainda não confirmado.

B) leitura fantasma, pois surgiu uma nova linha no predicado.

C) leitura não repetível, pois releu a mesma linha após `COMMIT`.

D) atualização perdida, pois sobrescreveu a gravação de T1.

### S3S043 — Função do SAVEPOINT

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplos de transação e savepoint](semana_03_estudo.md#s3-d5-exemplos-b1).

Em uma transação, um `SAVEPOINT` permite:

A) tornar durável tudo o que ocorreu antes dele, mesmo sem `COMMIT`.

B) liberar permanentemente todos os locks e encerrar a unidade de trabalho.

C) substituir o log de recuperação por uma cópia completa do banco.

D) reverter parte do trabalho sem confirmar automaticamente o restante.

### S3S044 — Menor privilégio e parâmetros

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Integridade, segurança e menor privilégio](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma aplicação apenas consulta uma view e pesquisa por CPF informado pelo usuário. Qual combinação reduz exposição e injeção?

A) Conceder papel de administrador e concatenar o CPF no SQL para ganhar flexibilidade.

B) Liberar acesso à tabela base e confiar que a interface ocultará as demais colunas.

C) Conceder somente o acesso necessário à view e enviar o CPF como parâmetro.

D) Usar uma constraint de integridade como substituta de autorização e parametrização.

### S3S045 — Ciclo de deadlock

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Deadlock, espera e starvation](semana_03_estudo.md#s3-d5-concorrencia).

T1 mantém lock em A e espera B; T2 mantém lock em B e espera A. O estado e uma prevenção típica são:

A) starvation; adotar fila justa de concessão, pois a espera decorre apenas de adiamento repetido.

B) deadlock; aumentar o timeout de ambas as transações, garantindo que o ciclo termine sem abortar nenhuma delas.

C) deadlock; adotar uma ordem global e consistente de aquisição de A e B para impedir a formação do ciclo.

D) deadlock; elevar o isolamento para `SERIALIZABLE`, que por si eliminaria qualquer espera circular.

### S3S046 — WAL, undo e redo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log/WAL, checkpoint, undo e redo](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Após uma queda, há alterações de T1 confirmada ainda não refletidas nas páginas e alterações de T2 não confirmada já gravadas. A recuperação deve:

A) desfazer T1 e manter T2, porque somente páginas gravadas são consideradas válidas.

B) reaplicar ambas, pois o log elimina a diferença entre transação confirmada e ativa.

C) ignorar ambas, pois o checkpoint anterior encerrou toda necessidade de recuperação.

D) refazer T1 quando necessário e desfazer os efeitos não confirmados de T2.

### S3S047 — MVCC e isolamento

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Locks e MVCC](semana_03_estudo.md#s3-d5-concorrencia).

Sobre MVCC, assinale a interpretação correta.

A) Leitores podem usar versões coerentes, mas as garantias dependem do nível e do SGBD.

B) Toda leitura passa a ver automaticamente as gravações não confirmadas mais recentes.

C) Conflitos entre escritores deixam de existir porque cada versão é sempre independente.

D) O mecanismo torna desnecessários log, controle de transações e detecção de falhas.

### S3S048 — Estado preparado no 2PC

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Commit em duas fases — 2PC](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

No 2PC, um participante votou “sim”, registrou o estado preparado e perdeu contato com o coordenador antes da decisão. Nesse intervalo, ele:

A) deve confirmar sozinho, pois o voto positivo já equivale à decisão global.

B) pode ficar bloqueado aguardando a decisão coordenada de commit ou abort.

C) deve apagar seu log, liberar recursos e escolher depois qualquer resultado.

D) converte automaticamente a transação distribuída em operação local durável.

### S3S049 — Transferência concorrente e recuperação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Transações e ACID](semana_03_estudo.md#s3-d5-transacoes-acid), com apoio de [Concorrência](semana_03_estudo.md#s3-d5-concorrencia) e [Recuperação](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Duas sessões transferem valores das mesmas contas; uma falha após o débito, e o servidor cai logo depois do commit da outra. Qual combinação atende atomicidade, concorrência e recuperação?

A) Transações delimitadas, controle de conflito e log capaz de undo/redo conforme o estado de commit.

B) Uma transação para débito e crédito, mas sem detectar conflito entre sessões e com recuperação baseada apenas em backup diário.

C) Transação e controle de conflito, mas descarte do log antes de a decisão de commit tornar-se durável.

D) Autocommit nos dois comandos, ordem consistente de locks e checkpoint tratado como substituto do log de recuperação.

### S3S050 — Validade, acesso e unidade de trabalho

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integridade e segurança](semana_03_estudo.md#s3-d5-integridade-seguranca), com apoio de [Transações](semana_03_estudo.md#s3-d5-transacoes-acid).

Um serviço registra pagamento e auditoria. Deve rejeitar status fora do domínio, impedir acesso direto da conta da aplicação às tabelas e reverter tudo se a auditoria falhar. O desenho adequado combina:

A) índice para o domínio, papel administrador e confirmação antes da auditoria.

B) view sem controle de base, SQL concatenado e dois commits independentes.

C) validação apenas na interface, acesso irrestrito e compensação manual posterior.

D) constraint, menor privilégio e transação única com tratamento de erro e rollback.

## Questões — Dia 6

### S3S051 — Prefixo de índice composto

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Índices, composição e prefixo à esquerda](semana_03_estudo.md#s3-d6-indices).

Existe índice B-tree `(uf, ativo, nome)`. Qual filtro aproveita diretamente seu prefixo inicial?

A) `WHERE ativo='S'`, sem condição sobre `uf`.

B) `WHERE nome='Ana'`, sem condição sobre colunas anteriores.

C) `WHERE uf='PR' AND ativo='S'`, usando as duas colunas iniciais.

D) `WHERE UPPER(nome)='ANA'`, sem índice funcional compatível.

### S3S052 — Predicado sargável por data

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Sargabilidade](semana_03_estudo.md#s3-d6-indices).

Em SQL conceitual, adaptando limites e tipos ao dialeto do produto, qual predicado tende a ser mais sargável para buscar registros de julho de 2026 com índice em `data_evento`?

A) `WHERE YEAR(data_evento)=2026 AND MONTH(data_evento)=7`.

B) `WHERE CAST(data_evento AS VARCHAR) LIKE '2026-07%'`.

C) `WHERE EXTRACT(YEAR FROM data_evento)=2026`.

D) `WHERE data_evento>='2026-07-01' AND data_evento<'2026-08-01'`.

### S3S053 — OLTP e OLAP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [BI, OLTP, OLAP, data warehouse e data mart](semana_03_estudo.md#s3-d6-bi).

Qual contraste está correto?

A) OLTP prioriza análises históricas amplas; OLAP registra transações curtas concorrentes.

B) OLTP sustenta operações correntes; OLAP favorece análise agregada e histórica.

C) OLTP e OLAP exigem o mesmo esquema e a mesma granularidade em qualquer contexto.

D) OLAP substitui sistemas de origem e elimina a necessidade de integração de dados.

### S3S054 — Fato, dimensão e grão

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Fato, dimensão, estrela, floco e granularidade](semana_03_estudo.md#s3-d6-bi).

Em um modelo com grão “um atendimento por linha”, `tempo_espera` é medida e `unidade` descreve o contexto. Logo, são candidatos a:

A) fato para a medida e dimensão para a unidade.

B) dimensão para a medida e fato para a unidade.

C) duas dimensões, pois nenhum valor numérico pertence a fatos.

D) dois fatos independentes, pois descrições não integram dimensões.

### S3S055 — Estimativa de cardinalidade

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Estatísticas, otimizador e cardinalidade](semana_03_estudo.md#s3-d6-otimizacao).

O plano estima 10 linhas e processa 500 mil; duas colunas filtradas são fortemente correlacionadas. A primeira hipótese técnica é:

A) estatísticas individuais atualizadas impedem qualquer erro causado pela dependência entre as colunas.

B) estatísticas ou pressupostos de seletividade não representam adequadamente a correlação.

C) o grande volume real torna a estimativa irrelevante e confirma automaticamente o método escolhido.

D) forçar outro método de junção corrige a estimativa do filtro sem revisar estatísticas ou seletividade.

### S3S056 — Custo de manutenção de índice

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Índice é caminho de acesso com custo](semana_03_estudo.md#s3-d6-indices).

Um novo índice acelerou uma consulta rara, mas aumentou muito o custo de inserções frequentes. Qual decisão é tecnicamente responsável?

A) Medir o benefício total na carga e manter, ajustar ou remover o índice conforme leituras e escritas reais.

B) Manter o índice se a consulta isolada melhorar, sem ponderar a frequência e o custo acumulado das inserções.

C) Remover o índice sempre que a latência de escrita subir, mesmo que ele sustente consultas críticas frequentes.

D) Reordenar suas colunas apenas para reduzir manutenção, sem retestar seletividade nem consultas beneficiadas.

### S3S057 — ETL e ELT

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ETL e ELT](semana_03_estudo.md#s3-d6-bi).

Qual afirmação distingue corretamente os dois fluxos?

A) ETL carrega os dados brutos e transforma no destino; ELT transforma na origem e carrega o resultado.

B) ETL e ELT podem transformar em qualquer etapa; as siglas distinguem apenas o fornecedor da ferramenta.

C) ETL transforma antes da carga, enquanto ELT apenas adia a validação, mas mantém a transformação na origem.

D) No ETL, a transformação precede a carga no destino; no ELT, os dados são carregados e a transformação principal ocorre no destino.

### S3S058 — Média ponderada no grão correto

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplos resolvidos de BI](semana_03_estudo.md#s3-d6-exemplos-bi).

Duas unidades têm 10 atendimentos com média de 2 minutos e 90 atendimentos com média de 8 minutos. A média global correta é:

A) 5 minutos, atribuindo o mesmo peso às médias das duas unidades apesar dos tamanhos diferentes.

B) 6,73 minutos, dividindo a soma ponderada 740 por 110 e contando dez atendimentos duas vezes no denominador.

C) 7,4 minutos, pois `10×2 + 90×8 = 740` e o denominador correto é o total de 100 atendimentos.

D) Não é possível calcular a média global apenas com médias e quantidades; seriam necessários os 100 tempos individuais.

### S3S059 — Diagnóstico antes de criar índice

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Protocolo de otimização](semana_03_estudo.md#s3-d6-otimizacao), com apoio de [Índices](semana_03_estudo.md#s3-d6-indices).

Uma consulta ficou lenta após crescimento e mudança na distribuição dos dados. O plano estima poucas linhas, executa scan amplo e o predicado aplica função à coluna indexada. Qual sequência de diagnóstico é mais completa?

A) Medir baseline, conferir estimado versus real, revisar estatísticas e sargabilidade, testar e medir regressões.

B) Criar vários índices semelhantes, alterar o SQL e comparar apenas o tempo de uma execução.

C) Forçar sempre index seek, ignorar distribuição e considerar concluído se a primeira execução melhorar.

D) Atualizar estatísticas e encerrar o teste, sem revisar a função na coluna nem medir a nova execução.

### S3S060 — Pipeline analítico coerente

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Business Intelligence](semana_03_estudo.md#s3-d6-bi), com apoio de [Exemplos de BI](semana_03_estudo.md#s3-d6-exemplos-bi).

O órgão quer analisar tempo médio por unidade e mês sem distorcer volumes. Qual plano respeita origem, integração, grão e medida?

A) Integrar e validar as fontes, mas deixar o grão implícito e armazenar somente médias mensais para promediá-las depois.

B) Modelar fatos e dimensões antes de declarar o grão e agregar médias de origem sem conservar seus denominadores.

C) Adotar uma linha por interação quando a medida é por atendimento e depois somar médias mensais entre unidades.

D) Integrar e validar fontes, declarar o grão, modelar fatos/dimensões e calcular razão entre somas.

## Gabarito

| Questão | Resposta |
|---|:---:|
| S3S001 | B |
| S3S002 | D |
| S3S003 | A |
| S3S004 | C |
| S3S005 | C |
| S3S006 | A |
| S3S007 | D |
| S3S008 | B |
| S3S009 | A |
| S3S010 | B |
| S3S011 | C |
| S3S012 | C |
| S3S013 | D |
| S3S014 | B |
| S3S015 | B |
| S3S016 | D |
| S3S017 | C |
| S3S018 | A |
| S3S019 | C |
| S3S020 | B |
| S3S021 | A |
| S3S022 | C |
| S3S023 | B |
| S3S024 | D |
| S3S025 | D |
| S3S026 | B |
| S3S027 | A |
| S3S028 | C |
| S3S029 | A |
| S3S030 | C |
| S3S031 | D |
| S3S032 | B |
| S3S033 | C |
| S3S034 | A |
| S3S035 | C |
| S3S036 | A |
| S3S037 | B |
| S3S038 | D |
| S3S039 | B |
| S3S040 | D |
| S3S041 | B |
| S3S042 | A |
| S3S043 | D |
| S3S044 | C |
| S3S045 | C |
| S3S046 | D |
| S3S047 | A |
| S3S048 | B |
| S3S049 | A |
| S3S050 | D |
| S3S051 | C |
| S3S052 | D |
| S3S053 | B |
| S3S054 | A |
| S3S055 | B |
| S3S056 | A |
| S3S057 | D |
| S3S058 | C |
| S3S059 | A |
| S3S060 | D |

## Comentários

### Comentário S3S001

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Funções centrais de um SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Regras estratégicas dependem da governança e do negócio, não são decididas autonomamente pelo software.
- **B)** Correta. Concorrência, integridade, autorização e recuperação integram as funções clássicas de gerenciamento do SGBD.
- **C)** Incorreta. O SGBD produz e protege dados, mas não substitui a interpretação humana e institucional.
- **D)** Incorreta. O modelo de negócio exige participação dos responsáveis pelos significados corporativos.

**Conceito:** Funções centrais do SGBD.

**Pegadinha:** Confundir gerenciamento técnico dos dados com decisão estratégica do órgão.

**Como pensar:** Separe o que o software controla do que depende de governança e interpretação humana.

### Comentário S3S002

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Inclusões de linhas não criam, por si, novas visões externas.
- **B)** Incorreta. A definição de colunas e restrições permaneceu estável; mudou o conteúdo em um instante.
- **C)** Incorreta. O catálogo continua descrevendo a estrutura mesmo quando os valores armazenados se alteram.
- **D)** Correta. Instância é o estado corrente dos dados; esquema é sua definição relativamente estável.

**Conceito:** Diferença entre esquema e instância.

**Pegadinha:** Tratar qualquer mudança quantitativa nas linhas como alteração estrutural do esquema.

**Como pensar:** Pergunte se mudou a definição da tabela ou apenas o conjunto de valores armazenados.

### Comentário S3S003

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A AD governa semântica e padrões; o DBA cuida da implementação, disponibilidade e operação técnica.
- **B)** Incorreta. A alternativa troca as atribuições típicas e concentra no DBA a semântica corporativa.
- **C)** Incorreta. Hardware não resume AD, e glossário não resume a atuação do DBA.
- **D)** Incorreta. Os papéis podem cooperar ou acumular-se, mas não são conceitos obrigatoriamente idênticos.

**Conceito:** Separação entre governança de dados e administração técnica.

**Pegadinha:** Inverter AD e DBA com base apenas na palavra “administração”.

**Como pensar:** Associe significado e padrão à AD; associe SGBD, desempenho e operação ao DBA.

### Comentário S3S004

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Independência física e lógica de dados](semana_03_estudo.md#s3-d1-independencia-dados).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A decomposição visível altera o nível conceitual e pode exigir independência lógica.
- **B)** Incorreta. Renomear atributo conceitual usado externamente não é simples mudança física.
- **C)** Correta. Arquivos e índices pertencem ao nível interno e podem mudar sem afetar os níveis superiores.
- **D)** Incorreta. Remoção de coluna pública rompe a interface externa e exige adaptação.

**Conceito:** Independência física de dados.

**Observação:** A expressão “sem alteração” descreve o cenário; o comando continua pedindo a alternativa correta.

**Pegadinha:** Classificar toda alteração técnica como física, mesmo quando muda a estrutura percebida.

**Como pensar:** Verifique se a mudança alcança somente armazenamento e caminhos de acesso internos.

### Comentário S3S005

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A estrutura conceitual foi preservada; o problema nasceu da alteração no nível interno.
- **B)** Incorreta. Mudança de instância é alteração de valores, não reconstrução de arquivos e índices.
- **C)** Correta. Se uma mudança interna exige reescrever a aplicação sem mudar o conceitual, a separação física falhou.
- **D)** Incorreta. Metadados continuam metadados; a falha não transforma catálogo em dados do usuário.

**Conceito:** Mapeamento interno–conceitual e independência física.

**Observação:** A ocorrência de “não” integra a narrativa; o item não pede alternativa incorreta.

**Pegadinha:** Escolher independência lógica apenas porque o efeito apareceu em uma aplicação externa.

**Como pensar:** Localize primeiro o nível que mudou; depois identifique qual fronteira deveria absorver a alteração.

### Comentário S3S006

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Catálogos expõem metadados de objetos, tipos, restrições e autorizações mantidos pelo SGBD.
- **B)** Incorreta. Tuplas guardam valores do domínio de negócio, não descrevem formalmente cada coluna.
- **C)** Incorreta. Logs de aplicação registram eventos, mas não substituem o dicionário estrutural.
- **D)** Incorreta. Uma visão externa costuma mostrar um recorte e não necessariamente todos os objetos.

**Conceito:** Catálogo e metadados.

**Pegadinha:** Confundir registro de execução, dados operacionais e descrição formal da estrutura.

**Como pensar:** Quando a pergunta é “como o banco está definido”, procure o catálogo, não as linhas de negócio.

### Comentário S3S007

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Banco de dados designa a coleção organizada, não todo o ecossistema humano e técnico.
- **B)** Incorreta. O SGBD é o gerenciador; aplicações, usuários e processos não são todos módulos internos dele.
- **C)** Incorreta. O catálogo descreve objetos, mas não contém fisicamente todas as pessoas e aplicações.
- **D)** Correta. Sistema de banco de dados abrange dados, SGBD, aplicações, pessoas e procedimentos.

**Conceito:** Amplitude do sistema de banco de dados.

**Pegadinha:** Usar “banco”, “SGBD” e “sistema de banco” como sinônimos perfeitos.

**Como pensar:** Ordene os conceitos do componente mais restrito ao ecossistema completo da solução.

### Comentário S3S008

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Independência física e lógica de dados](semana_03_estudo.md#s3-d1-independencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Houve mudança na estrutura conceitual, não apenas nos valores correntes.
- **B)** Correta. A visão externa conservou a interface apesar da decomposição do esquema conceitual.
- **C)** Incorreta. Decompor entidade não é, em regra, apenas reorganizar arquivos e índices.
- **D)** Incorreta. A compatibilidade decorreu justamente de uma visão externa, não de sua ausência.

**Conceito:** Independência lógica de dados.

**Pegadinha:** Chamar de física qualquer mudança executada tecnicamente pelo DBA.

**Como pensar:** Se o conceitual mudou e a visão do usuário permaneceu, reconheça independência lógica.

### Comentário S3S009

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Contrastes decisivos](semana_03_estudo.md#s3-d1-contrastes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Índice é interno; atributo corporativo é conceitual; visão é externa; tipos e restrições são metadados.
- **B)** Incorreta. Reconstrução de índice não é externa, e novo atributo não é simples mudança física.
- **C)** Incorreta. A sequência desloca todos os níveis e trata consulta estrutural como atualização de negócio.
- **D)** Incorreta. Índice não é instância, atributo não é catálogo isolado e visão não é mecanismo de recuperação.

**Conceito:** Classificação coordenada de níveis e metadados.

**Pegadinha:** Classificar pelo executor da ação, em vez do objeto arquitetural realmente alterado.

**Como pensar:** Para cada ação, identifique separadamente armazenamento, modelo global, interface e descrição estrutural.

### Comentário S3S010

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba), com apoio de [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-arquitetura-bd).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Os papéis estão corretos, mas reescrever relatórios por mudança interna abandona a independência física.
- **B)** Correta. O plano combina governança semântica, operação física e proteção das interfaces externas.
- **C)** Incorreta. A alternativa troca governança semântica e operação técnica e não garante compatibilidade externa.
- **D)** Incorreta. Retirar mapeamentos faz a organização física vazar para relatórios, ainda que AD e DBA cooperem.

**Conceito:** Integração entre papéis e arquitetura em níveis.

**Pegadinha:** Misturar autoridade de negócio, execução técnica e mecanismo de independência.

**Como pensar:** Resolva em três passos: quem define o significado, quem muda o armazenamento e quem preserva a interface.

### Comentário S3S011

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Chave estrangeira depende de referência a outra relação, o que não foi informado.
- **B)** Incorreta. A escolha da primária não retira de outra identificação mínima sua capacidade de identificar.
- **C)** Correta. `cpf` continua chave candidata e passa a ser uma chave alternativa à primária escolhida.
- **D)** Incorreta. Minimalidade foi declarada; logo, `cpf` não é uma superchave não mínima.

**Conceito:** Chave candidata, primária e alternativa.

**Pegadinha:** Imaginar que a escolha da chave primária destrói as demais chaves candidatas.

**Como pensar:** Primeiro identifique todas as chaves mínimas; só depois marque qual delas foi escolhida como primária.

### Comentário S3S012

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Parcela é uma entidade com ocorrências próprias, não simples atributo multivalorado.
- **B)** Incorreta. Entidade associativa representa relacionamento, mas não é a descrição dada para dependência de identificação.
- **C)** Correta. O número da parcela é discriminador parcial e precisa da chave do contrato proprietário.
- **D)** Incorreta. Chave composta não implica automaticamente relacionamento ternário.

**Conceito:** Identificação de entidade fraca.

**Pegadinha:** Confundir composição da chave com quantidade de entidades participantes do relacionamento.

**Como pensar:** Verifique se a ocorrência pode ser identificada sem incorporar a chave de um proprietário.

### Comentário S3S013

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Regras de mapeamento MER–relacional](semana_03_estudo.md#s3-d2-mapeamento).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Colocar a chave do lado N no lado 1 não representa vários profissionais por unidade.
- **B)** Incorreta. Tabela associativa é típica de N:M ou de necessidade específica, não requisito geral do 1:N simples.
- **C)** Incorreta. Repetição bilateral cria redundância e não é a regra usual de mapeamento.
- **D)** Correta. A chave estrangeira do lado 1 é armazenada no lado N, que possui cada ocorrência profissional.

**Conceito:** Mapeamento relacional de 1:N.

**Pegadinha:** Colocar a chave estrangeira no lado que possui menor cardinalidade.

**Como pensar:** Pergunte qual lado possui várias linhas; é nele que cada linha aponta para a ocorrência do lado 1.

### Comentário S3S014

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Primeira Forma Normal — 1FN](semana_03_estudo.md#s3-d2-1fn).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Índice não torna atômico o valor composto armazenado na célula.
- **B)** Correta. Cada telefone deve ser representado como ocorrência atômica, normalmente em relação vinculada.
- **C)** Incorreta. Mudar a lista de coluna preserva a mesma violação de atomicidade.
- **D)** Incorreta. Duplicar a linha principal sem identificação adequada cria redundância e anomalias.

**Conceito:** Atomicidade exigida pela 1FN.

**Pegadinha:** Tentar corrigir grupo repetitivo com formatação, índice ou outro separador.

**Como pensar:** Procure células com listas ou grupos e transforme cada valor em ocorrência relacional identificável.

### Comentário S3S015

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Segunda Forma Normal — 2FN](semana_03_estudo.md#s3-d2-2fn).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. `quantidade` descreve o item e pode depender da chave composta completa.
- **B)** Correta. `data_pedido` depende apenas de `pedido_id`, devendo ficar na relação que representa o pedido.
- **C)** Incorreta. `NOT NULL` e `UNIQUE` não eliminam a dependência parcial indicada.
- **D)** Incorreta. Inflar a chave não separa os fatos nem remove a redundância semântica.

**Conceito:** Dependência parcial e Segunda Forma Normal.

**Pegadinha:** Tentar resolver dependência funcional acrescentando constraints ou atributos à chave.

**Como pensar:** Com chave composta, teste cada atributo não chave contra cada parte da chave separadamente.

### Comentário S3S016

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Terceira Forma Normal — 3FN](semana_03_estudo.md#s3-d2-3fn).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Remover a chave da unidade troca identificação estável por descrição textual.
- **B)** Incorreta. Índice não elimina a repetição nem a dependência transitiva.
- **C)** Incorreta. Tornar a descrição parte da chave agrava o modelo e não representa o fato.
- **D)** Correta. Os dados da unidade ficam em relação própria e `Profissional` conserva a referência.

**Conceito:** Dependência transitiva e Terceira Forma Normal.

**Pegadinha:** Tratar índice ou ampliação da chave como substitutos de decomposição semântica.

**Como pensar:** Siga a cadeia chave → atributo intermediário → descrição e separe o fato intermediário.

### Comentário S3S017

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Decomposição sem perda e preservação de dependências](semana_03_estudo.md#s3-d2-decomposicao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Junção sem perda é necessária, mas reduzir tabelas não substitui a avaliação independente da preservação de dependências.
- **B)** Incorreta. Preservar dependências não compensa uma decomposição cuja junção produz tuplas espúrias.
- **C)** Correta. Sem perda assegura reconstrução sem linhas espúrias; preservação permite validar dependências sem recomposição excessiva.
- **D)** Incorreta. Menor redundância e chaves estrangeiras não provam, isoladamente, junção sem perda nem preservação das dependências.

**Conceito:** Propriedades de uma decomposição relacional.

**Pegadinha:** Avaliar decomposição apenas por desempenho ou pelo número de tabelas resultantes.

**Como pensar:** Faça duas perguntas independentes: recupero a relação original e consigo impor as dependências?

### Comentário S3S018

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Forma Normal de Boyce–Codd — BCNF](semana_03_estudo.md#s3-d2-bcnf).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Na BCNF, todo determinante de dependência não trivial deve ser superchave.
- **B)** Incorreta. A condição não é satisfeita apenas porque o dependente é atributo primo.
- **C)** Incorreta. A análise considera todas as chaves candidatas, não só a primária escolhida.
- **D)** Incorreta. BCNF não exige chave candidata única nem proíbe nulos por essa definição.

**Conceito:** Determinantes na BCNF.

**Observação:** “Não trivial” é termo técnico da dependência funcional; o comando permanece positivo.

**Pegadinha:** Reduzir BCNF a uma regra sobre a chave primária ou sobre atributos primos.

**Como pensar:** Para cada `X → Y` não trivial, teste se `X` identifica todas as tuplas da relação.

### Comentário S3S019

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Entidades, atributos e relacionamentos](semana_03_estudo.md#s3-d2-mer), com apoio de [Regras de mapeamento](semana_03_estudo.md#s3-d2-mapeamento).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Lista multivalorada viola a representação relacional e mistura datas de associações distintas.
- **B)** Incorreta. Uma única FK em `Certificacao` reduziria indevidamente a cardinalidade para 1:N.
- **C)** Correta. A relação associativa representa N:M e recebe o atributo próprio `data_validacao`.
- **D)** Incorreta. Cópias desconectadas criam redundância e perdem a identidade compartilhada da certificação.

**Conceito:** Mapeamento de N:M com atributo do relacionamento.

**Pegadinha:** Colocar atributo da associação em uma entidade ou serializar múltiplos vínculos numa coluna.

**Como pensar:** Identifique cardinalidade, chaves participantes e atributos que existem apenas para o vínculo.

### Comentário S3S020

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Dependências funcionais e anomalias](semana_03_estudo.md#s3-d2-dependencias), com apoio de [2FN](semana_03_estudo.md#s3-d2-2fn) e [3FN](semana_03_estudo.md#s3-d2-3fn).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Chave composta é precisamente o contexto em que dependência parcial deve ser testada.
- **B)** Correta. O plano separa o fato do protocolo, seus itens e a descrição do setor, preservando referências.
- **C)** Incorreta. Separar setor sem retirar `data_abertura` repetida corrige apenas parte do problema.
- **D)** Incorreta. Nome de setor não substitui a identificação de protocolo ou item.

**Conceito:** Integração de 2FN, 3FN e chaves estrangeiras.

**Pegadinha:** Corrigir uma dependência e deixar outra redundância no mesmo conjunto de dados.

**Como pensar:** Liste as dependências, classifique parcial e transitiva, depois conserve os vínculos por chaves.

### Comentário S3S021

**Nível:** Médio

**Uso:** Simulado

**Referência:** [SELECT, ordem escrita e ordem lógica](semana_03_estudo.md#s3-d3-select-ordem).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Depois de `FROM/JOIN`, `WHERE` filtra linhas antes da formação dos grupos.
- **B)** Incorreta. `SELECT` é avaliado logicamente após agrupamento e `HAVING`.
- **C)** Incorreta. `ORDER BY` atua próximo ao final, sobre o resultado projetado.
- **D)** Incorreta. `HAVING` filtra grupos já formados, não linhas individuais antes deles.

**Conceito:** Ordem lógica de processamento do SELECT.

**Pegadinha:** Confundir a ordem em que as cláusulas são escritas com sua ordem lógica.

**Como pensar:** Reconstrua a sequência `FROM/ON`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY`.

### Comentário S3S022

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Tipos de junção](semana_03_estudo.md#s3-d3-joins).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. `INNER JOIN` remove unidades sem correspondência ativa.
- **B)** Incorreta. O produto cartesiano filtrado também exige correspondência e não preserva a ausência.
- **C)** Correta. O filtro em `ON` restringe as correspondências, enquanto o `LEFT JOIN` mantém todas as unidades.
- **D)** Incorreta. O predicado em `WHERE` rejeita a linha estendida com valor nulo.

**Conceito:** Preservação de linhas em junção externa.

**Observação:** A ausência de profissionais faz parte do requisito; a questão pede a construção correta.

**Pegadinha:** Mover o filtro do lado opcional de `ON` para `WHERE` sem perceber a perda.

**Como pensar:** Defina primeiro qual lado deve sobreviver sem par e mantenha filtros do lado opcional em `ON`.

### Comentário S3S023

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Agregação, GROUP BY e HAVING](semana_03_estudo.md#s3-d3-agregacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. `WHERE` não recebe agregação do grupo que ainda não foi formado.
- **B)** Correta. `HAVING` aplica o predicado à contagem resultante de cada unidade agrupada.
- **C)** Incorreta. `ON` define correspondência de junção, não filtra resultado agregado final.
- **D)** Incorreta. Ordenação não substitui o filtro e não elimina grupos.

**Conceito:** Diferença entre WHERE e HAVING.

**Pegadinha:** Usar `WHERE` para qualquer condição sem observar se ela depende de agregação.

**Como pensar:** Se a condição usa o valor de um grupo, aplique-a depois do `GROUP BY`, em `HAVING`.

### Comentário S3S024

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O valor numérico projetado não determina o resultado do `EXISTS`.
- **B)** Incorreta. Não há exigência de exatamente uma linha nem de valor não nulo.
- **C)** Incorreta. Distinção e ausência de nulos nas colunas projetadas são irrelevantes.
- **D)** Correta. `EXISTS` testa se a subconsulta produz pelo menos uma linha.

**Conceito:** Semântica existencial de subconsulta.

**Pegadinha:** Interpretar o conteúdo do `SELECT` interno em vez da existência de linhas.

**Como pensar:** Ignore a projeção e pergunte apenas se a correlação permite alguma ocorrência na subconsulta.

### Comentário S3S025

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Subconsultas, IN, EXISTS e correlação](semana_03_estudo.md#s3-d3-subconsultas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. `IN` procura pertencimento e inverte o requisito da antijunção.
- **B)** Incorreta. Comparação comum com `NULL` produz desconhecido, não verdadeiro.
- **C)** Incorreta. `DISTINCT` elimina duplicatas, mas não converte nulo em zero.
- **D)** Correta. `NOT EXISTS` correlacionado evita a armadilha, e filtrar nulos também torna o conjunto comparável.

**Conceito:** Lógica de três valores em antijunção.

**Pegadinha:** Tratar `NULL` como valor comum dentro de `NOT IN`.

**Como pensar:** Antes de usar `NOT IN`, verifique nulabilidade; para ausência correlacionada, prefira `NOT EXISTS`.

### Comentário S3S026

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplo de filtro em ON versus WHERE](semana_03_estudo.md#s3-d3-exemplos-b2).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. `WHERE` não cria as linhas nulas; ele pode justamente rejeitá-las.
- **B)** Correta. Nas linhas sem correspondência, `p.ativo` é nulo e não satisfaz o filtro do `WHERE`.
- **C)** Incorreta. A equivalência não vale quando a posição do predicado muda a preservação da junção externa.
- **D)** Incorreta. O SQL permite filtros no `WHERE`; o problema é semântico, não sintático.

**Conceito:** Local do predicado em LEFT JOIN.

**Pegadinha:** Assumir que predicados idênticos em `ON` e `WHERE` preservam a mesma cardinalidade.

**Como pensar:** Simule uma linha sem par e acompanhe o valor nulo até o predicado que vem depois da junção.

### Comentário S3S027

**Nível:** Médio

**Uso:** Simulado

**Referência:** [UNION, INTERSECT e EXCEPT](semana_03_estudo.md#s3-d3-conjuntos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. `UNION` combina os resultados compatíveis e elimina duplicatas.
- **B)** Incorreta. Manter somente o elemento comum descreve uma interseção, não a união.
- **C)** Incorreta. Remover elementos da primeira entrada aproxima-se de diferença de conjuntos.
- **D)** Incorreta. As quatro ocorrências seriam preservadas por `UNION ALL`.

**Conceito:** Operações de conjunto e duplicatas.

**Observação:** O contraste com `UNION ALL` delimita o objeto; o gabarito identifica o resultado de `UNION`.

**Pegadinha:** Confundir união distinta com concatenação integral ou interseção.

**Como pensar:** Determine primeiro a operação de conjuntos; depois verifique se ela mantém ou elimina duplicatas.

### Comentário S3S028

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Exemplo de máximo correlacionado com empate](semana_03_estudo.md#s3-d3-exemplos-b2).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Nenhum valor pode ser maior que o máximo global, e falta correlação por profissional.
- **B)** Incorreta. Maior identificador não significa maior pagamento nem preserva empates de valor.
- **C)** Correta. O máximo é calculado dentro do grupo da linha externa e a igualdade mantém todos os empates.
- **D)** Incorreta. A alternativa usa mínimo e agrupa por status, critérios distintos do enunciado.

**Conceito:** Subconsulta correlacionada para máximo por grupo.

**Pegadinha:** Substituir valor máximo por maior ID ou esquecer a correlação com o grupo externo.

**Como pensar:** Calcule o máximo do grupo corrente e compare por igualdade para não eliminar empates.

### Comentário S3S029

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Junções](semana_03_estudo.md#s3-d3-joins), com apoio de [Agregação](semana_03_estudo.md#s3-d3-agrupamento-having).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A junção externa preserva unidades, `ON` limita ativos, `COUNT(p.id)` produz zero e `HAVING` filtra grupos.
- **B)** Incorreta. `INNER JOIN` perde ausências, e agregação não pode ser filtrada em `WHERE` dessa forma.
- **C)** Incorreta. Sem chave ocorre produto indevido; `COUNT(*)` conta a linha preservada e `ORDER BY` não filtra.
- **D)** Incorreta. O produto cartesiano e a falta de agrupamento impedem cumprir a granularidade pedida.

**Conceito:** Junção externa, contagem de coluna e HAVING.

**Pegadinha:** Cumprir dois requisitos e falhar justamente na contagem zero das unidades sem correspondência.

**Como pensar:** Resolva em ordem: preserve o lado obrigatório, limite pares, conte a chave opcional e filtre o grupo.

### Comentário S3S030

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ordenação total e paginação estável](semana_03_estudo.md#s3-d3-exemplos-b2), com apoio de [Granularidade do agrupamento](semana_03_estudo.md#s3-d3-agrupamento-having).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Agrupar por pagamento fragmenta a granularidade e ordenar só pelo total mantém empates sem desempate.
- **B)** Incorreta. Remover o agrupamento perde a medida por profissional, e paginação anterior não é corrigida por `DISTINCT`.
- **C)** Correta. A chave do profissional fixa o grão e o segundo critério único produz ordenação total estável.
- **D)** Incorreta. Nome e total podem empatar, então o resultado entre páginas continua indeterminado.

**Conceito:** Granularidade e paginação determinística.

**Pegadinha:** Considerar ordenação por uma coluna não única suficiente para paginação repetível.

**Como pensar:** Garanta uma linha por entidade e finalize o `ORDER BY` com uma chave única de desempate.

### Comentário S3S031

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Classes por finalidade](semana_03_estudo.md#s3-d4-classes-comando).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. `GRANT` controla privilégios e pertence à finalidade DCL.
- **B)** Incorreta. `COMMIT` controla a transação e é classificado como TCL.
- **C)** Incorreta. `UPDATE` manipula linhas e pertence à DML.
- **D)** Correta. `ALTER TABLE` modifica a definição estrutural e pertence à DDL.

**Conceito:** Classes de comandos SQL por finalidade.

**Pegadinha:** Classificar pelo impacto percebido, não pelo objeto sobre o qual o comando atua.

**Como pensar:** Pergunte se o comando define estrutura, manipula dados, controla privilégios ou controla transação.

### Comentário S3S032

**Nível:** Médio

**Uso:** Simulado

**Referência:** [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. `DEFAULT` supre omissão, mas não corrige valor inválido informado explicitamente.
- **B)** Correta. `CHECK` declara o predicado de domínio que cada linha deve satisfazer.
- **C)** Incorreta. Índice organiza caminho de acesso e não impõe esse conjunto de valores.
- **D)** Incorreta. Uma view comum não transforma automaticamente seu predicado em validação universal da base.

**Conceito:** Restrição CHECK e domínio.

**Pegadinha:** Atribuir a `DEFAULT`, índice ou view a função de validação declarativa.

**Como pensar:** Quando a regra é “o valor deve pertencer a um conjunto”, procure uma constraint de predicado.

### Comentário S3S033

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Views](semana_03_estudo.md#s3-d4-views).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Uma view comum não guarda cópia permanente nem apaga a linha da tabela base.
- **B)** Incorreta. A atualização do resultado não depende de trigger automática criada para toda view.
- **C)** Correta. A consulta definida pela view é avaliada sobre o estado atual e reaplica o filtro.
- **D)** Incorreta. Não aparecer no resultado não equivale a revogar privilégios sobre a base.

**Conceito:** View como consulta armazenada.

**Pegadinha:** Tratar view comum como tabela materializada ou como mecanismo completo de autorização.

**Como pensar:** Diferencie definição lógica, armazenamento físico e privilégio de acesso a cada objeto.

### Comentário S3S034

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Procedure atende chamada explícita, parâmetros, múltiplos comandos e retorno operacional.
- **B)** Incorreta. Trigger responde a evento associado ao objeto e não é chamada como operação parametrizada comum.
- **C)** Incorreta. `UNIQUE` impõe unicidade e não executa o fluxo descrito.
- **D)** Incorreta. View representa consulta e não oferece, por si, a operação parametrizada solicitada.

**Conceito:** Escolha de objeto programável.

**Pegadinha:** Escolher trigger apenas porque existe atualização no interior do requisito.

**Como pensar:** Comece pelo modo de acionamento: chamada explícita favorece procedure; evento automático favorece trigger.

### Comentário S3S035

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Transact-SQL](semana_03_estudo.md#s3-d4-transact-sql).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Ele delimita lotes, mas não executa automaticamente a procedure criada.
- **B)** Incorreta. `GO` não é DML nem substitui `COMMIT`.
- **C)** Correta. Ferramentas como clientes de SQL Server interpretam `GO` para dividir lotes antes do envio.
- **D)** Incorreta. Não é função do padrão SQL nem apenas reinicialização de variáveis.

**Conceito:** Lote de cliente e comando T-SQL.

**Pegadinha:** Ler tudo que aparece em um script como instrução enviada ao mecanismo do banco.

**Como pensar:** Identifique quem interpreta o token: ferramenta cliente ou servidor SQL.

### Comentário S3S036

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Triggers](semana_03_estudo.md#s3-d4-triggers).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. No SQL Server, a junção entre os conjuntos `deleted` e `inserted` preserva correspondência e filtra apenas mudanças reais.
- **B)** Incorreta. Trigger é disparada pelo evento, não chamada manualmente uma vez para cada linha.
- **C)** Incorreta. Variável escalar perde 199 linhas e não representa o conjunto afetado.
- **D)** Incorreta. No SQL Server, o disparo é por instrução e pode conter várias linhas.

**Conceito:** Trigger orientada a conjuntos no SQL Server.

**Pegadinha:** Programar a trigger como se `inserted` e `deleted` contivessem uma única linha.

**Como pensar:** No SQL Server, teste mentalmente a trigger com zero, uma e muitas linhas afetadas pela mesma instrução.

### Comentário S3S037

**Nível:** Médio

**Uso:** Simulado

**Referência:** [INSERT, UPDATE e DELETE](semana_03_estudo.md#s3-d4-dml).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Transação ajuda na reversão, mas a conferência posterior não substitui conhecer previamente o alcance.
- **B)** Correta. A prévia com predicado idêntico torna visíveis alcance, chaves e volume antes da escrita.
- **C)** Incorreta. Amostra e predicado mais amplo não comprovam o conjunto exato que será alterado.
- **D)** Incorreta. Estimativa do plano não substitui a inspeção das chaves reais produzidas pelo mesmo predicado.

**Conceito:** Validação prévia do alcance de DML.

**Pegadinha:** Confiar no comando de escrita sem reproduzir e conferir exatamente seu conjunto-alvo.

**Como pensar:** Transforme temporariamente a escrita em leitura com o mesmo `FROM` e `WHERE`, e confira as chaves.

### Comentário S3S038

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplo de view e privilégio sobre a base](semana_03_estudo.md#s3-d4-exemplos-b2).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O usuário ainda pode alcançar CPF pelo privilégio direto na tabela.
- **B)** Incorreta. Criar ou conceder view não revoga automaticamente privilégios existentes.
- **C)** Incorreta. A existência de objeto derivado não bloqueia o caminho para a base.
- **D)** Correta. Segurança depende do conjunto de privilégios e caminhos, não apenas da definição da view.

**Conceito:** View como interface e controle de privilégios.

**Pegadinha:** Confundir ocultação em uma consulta com anonimização ou revogação completa.

**Como pensar:** Enumere todos os caminhos pelos quais o principal pode alcançar o dado sensível.

### Comentário S3S039

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Migração para NOT NULL](semana_03_estudo.md#s3-d4-exemplos-b1), com apoio de [CREATE TABLE e restrições](semana_03_estudo.md#s3-d4-ddl-restricoes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A coluna anulável pode receber FK, mas órfãos existentes ainda impedem validação e não foram tratados.
- **B)** Correta. O plano verifica nulos, órfãos, regra de negócio, pai, ordem de constraints e reversão.
- **C)** Incorreta. Sanear somente nulos deixa referências órfãs incompatíveis com a FK.
- **D)** Incorreta. Exclusão sem regra aprovada e sem rollback pode perder dados válidos de forma irreversível.

**Conceito:** Migração controlada de integridade referencial.

**Pegadinha:** Aplicar a constraint antes de tornar o estado existente compatível com ela.

**Como pensar:** Inventarie, decida, saneie, valide, aplique em ordem e mantenha um caminho de retorno.

### Comentário S3S040

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Exemplo de procedure e atomicidade](semana_03_estudo.md#s3-d4-exemplos-b2), com apoio de [Stored procedures](semana_03_estudo.md#s3-d4-procedures).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Estar dentro de procedure não torna múltiplos comandos automaticamente atômicos.
- **B)** Incorreta. Confirmar a primeira ação impede rollback conjunto e deixa compensação incerta.
- **C)** Incorreta. Confirmar depois da falha de auditoria preserva efeito parcial e viola o requisito de tudo ou nada.
- **D)** Correta. Validação, transação única, confirmação final e rollback preservam a unidade de trabalho.

**Conceito:** Atomicidade explícita em stored procedure.

**Pegadinha:** Atribuir atomicidade ao contêiner procedure, em vez de delimitá-la e tratar falhas.

**Como pensar:** Localize o ponto único de confirmação e garanta que todo caminho de erro chegue ao rollback.

### Comentário S3S041

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Transação e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Consistência trata regras válidas e isolamento trata interferência concorrente.
- **B)** Correta. Atomicidade reúne débito e crédito; durabilidade conserva o resultado confirmado após falha.
- **C)** Incorreta. A ordem e as propriedades não correspondem aos dois requisitos descritos.
- **D)** Incorreta. Durabilidade não expressa “tudo ou nada”, e consistência não é persistência pós-commit.

**Conceito:** Atomicidade e durabilidade no ACID.

**Pegadinha:** Trocar propriedades ACID porque todas parecem qualidades gerais da transação.

**Como pensar:** Associe “tudo ou nada” à atomicidade e “sobrevive após confirmar” à durabilidade.

### Comentário S3S042

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Concorrência e níveis de isolamento](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. T2 observou uma escrita que ainda podia ser desfeita e de fato foi revertida.
- **B)** Incorreta. Fantasma envolve mudança no conjunto de linhas de um predicado entre leituras.
- **C)** Incorreta. Não houve duas leituras confirmadas da mesma linha com valores diferentes.
- **D)** Incorreta. T2 somente leu e não sobrescreveu a atualização de T1.

**Conceito:** Anomalia de leitura suja.

**Pegadinha:** Classificar qualquer interferência concorrente como fantasma ou atualização perdida.

**Como pensar:** Verifique se o dado lido já havia recebido `COMMIT`; se não, suspeite de leitura suja.

### Comentário S3S043

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplos de transação e savepoint](semana_03_estudo.md#s3-d5-exemplos-b1).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Savepoint marca posição interna, mas não produz durabilidade sem confirmação.
- **B)** Incorreta. Ele não encerra a transação nem necessariamente libera todos os locks.
- **C)** Incorreta. Log e recuperação permanecem necessários para a unidade de trabalho.
- **D)** Correta. É possível voltar ao marco e continuar ou decidir posteriormente sobre a transação.

**Conceito:** Rollback parcial por savepoint.

**Pegadinha:** Interpretar savepoint como commit parcial e definitivo.

**Como pensar:** Diferencie três ações: marcar posição, desfazer até a posição e confirmar toda a transação.

### Comentário S3S044

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Integridade, segurança e menor privilégio](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Administração amplia privilégios e concatenação expõe a consulta a injeção.
- **B)** Incorreta. Ocultar na interface não impede o acesso direto concedido à tabela.
- **C)** Correta. Menor privilégio reduz alcance, e parâmetro mantém a entrada como dado.
- **D)** Incorreta. Constraint valida estado, mas não substitui autorização nem parametrização.

**Conceito:** Menor privilégio e prevenção de injeção SQL.

**Pegadinha:** Usar controle visual ou integridade como se fossem mecanismos de segurança equivalentes.

**Como pensar:** Trate separadamente “quem pode acessar” e “como a entrada chega à instrução SQL”.

### Comentário S3S045

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Deadlock, espera e starvation](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O caso forma espera circular, não mero adiamento repetido; justiça de fila não rompe o ciclo já criado.
- **B)** Incorreta. Timeout pode ajudar a detectar e abortar uma vítima, mas não previne o ciclo nem garante término sem aborto.
- **C)** Correta. Há espera circular, e uma ordem global de recursos impede aquisições em sentidos opostos.
- **D)** Incorreta. `SERIALIZABLE` não impõe ordem global de aquisição e pode ampliar a disputa por locks.

**Conceito:** Deadlock e prevenção por ordenação.

**Pegadinha:** Confundir espera prolongada, starvation e ciclo formal de deadlock.

**Como pensar:** Desenhe o grafo: T1 espera recurso de T2 e T2 espera recurso de T1.

### Comentário S3S046

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log/WAL, checkpoint, undo e redo](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. T1 foi confirmada e deve sobreviver; T2 não confirmada não pode permanecer.
- **B)** Incorreta. O status de commit no log é decisivo para escolher redo ou undo.
- **C)** Incorreta. Checkpoint reduz trabalho, mas não elimina automaticamente a recuperação posterior.
- **D)** Correta. Redo garante durabilidade de T1, e undo restaura atomicidade diante de T2.

**Conceito:** Recuperação por redo e undo.

**Observação:** Os estados “confirmada” e “não confirmada” integram o caso; o comando é positivo.

**Pegadinha:** Decidir apenas pela página estar ou não no disco, ignorando o estado transacional.

**Como pensar:** Para cada transação, marque `COMMIT`; confirmada pode exigir redo, não confirmada pode exigir undo.

### Comentário S3S047

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Locks e MVCC](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. MVCC oferece versões para leitura, mas a visibilidade concreta depende da implementação e do isolamento.
- **B)** Incorreta. Expor automaticamente escritas não confirmadas contrariaria garantias usuais.
- **C)** Incorreta. Escritores ainda podem disputar a mesma linha ou restrição.
- **D)** Incorreta. Versionamento não elimina log, transações ou mecanismos de recuperação.

**Conceito:** Alcance e limites do MVCC.

**Pegadinha:** Tratar MVCC como ausência total de bloqueios, conflitos e regras de isolamento.

**Como pensar:** Separe conflito leitor–escritor de conflito escritor–escritor e confira o nível de visibilidade.

### Comentário S3S048

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Commit em duas fases — 2PC](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Voto positivo informa capacidade de confirmar, mas não é a decisão global.
- **B)** Correta. Preparado, o participante preserva recursos e aguarda a decisão, podendo ficar bloqueado.
- **C)** Incorreta. Apagar o log tornaria impossível honrar a decisão coordenada após recuperação.
- **D)** Incorreta. O protocolo não converte automaticamente a operação distribuída em transação local.

**Conceito:** Estado preparado e bloqueio no 2PC.

**Pegadinha:** Confundir voto da primeira fase com commit definitivo da segunda.

**Como pensar:** Distinga “posso confirmar” de “o coordenador decidiu confirmar”.

### Comentário S3S049

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Transações e ACID](semana_03_estudo.md#s3-d5-transacoes-acid), com apoio de [Concorrência](semana_03_estudo.md#s3-d5-concorrencia) e [Recuperação](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Delimitação protege o par débito/crédito, controle de conflito ordena concorrência e log trata a queda.
- **B)** Incorreta. A unidade local existe, mas faltam controle do conflito concorrente e log transacional para a queda recente.
- **C)** Incorreta. Sem tornar o log e a decisão duráveis antes do descarte, a recuperação pode perder uma transação confirmada.
- **D)** Incorreta. Ordem de locks ajuda no deadlock, mas autocommit quebra a unidade e checkpoint não substitui log.

**Conceito:** Integração de atomicidade, isolamento e recuperação.

**Pegadinha:** Escolher uma solução que cobre a queda, mas ignora falha intermediária ou conflito concorrente.

**Como pensar:** Teste a proposta contra três eventos separados: erro no meio, outra sessão simultânea e queda após commit.

### Comentário S3S050

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integridade e segurança](semana_03_estudo.md#s3-d5-integridade-seguranca), com apoio de [Transações](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Índice não valida o domínio; administrador viola menor privilégio; commit precoce quebra atomicidade.
- **B)** Incorreta. Acesso alternativo, concatenação e commits separados falham nos três requisitos.
- **C)** Incorreta. Validação só na interface é contornável, e compensação manual não garante rollback.
- **D)** Correta. Constraint protege validade, privilégio mínimo protege acesso e transação une pagamento e auditoria.

**Conceito:** Integridade, segurança e atomicidade como controles distintos.

**Pegadinha:** Usar um único mecanismo para problemas diferentes de validade, autorização e unidade de trabalho.

**Como pensar:** Mapeie cada requisito a seu controle: constraint, privilégio e transação com tratamento de erro.

### Comentário S3S051

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Índices, composição e prefixo à esquerda](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O filtro ignora a primeira coluna do índice composto.
- **B)** Incorreta. `nome` é a terceira coluna e não forma o prefixo inicial sozinho.
- **C)** Correta. As condições usam `uf` e `ativo` como as duas colunas iniciais contíguas do índice.
- **D)** Incorreta. Além de saltar o prefixo, a função pode impedir uso direto sem índice compatível.

**Conceito:** Prefixo à esquerda de índice composto.

**Pegadinha:** Achar que qualquer coluna presente no índice é igualmente acessível de forma isolada.

**Como pensar:** Leia a definição do índice da esquerda para a direita e identifique o primeiro prefixo contínuo filtrado.

### Comentário S3S052

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Aplicar funções à coluna pode impedir busca direta pelo índice simples.
- **B)** Incorreta. Conversão textual altera o lado indexado e adiciona custo e dependência de formato.
- **C)** Incorreta. A extração do ano ainda transforma cada valor da coluna.
- **D)** Correta. O intervalo semiaberto compara a coluna diretamente com limites, cuja escrita e tipo devem ser adaptados ao dialeto.

**Conceito:** Predicado sargável de intervalo temporal.

**Pegadinha:** Preferir a expressão que parece mais legível, mas envolve a coluna indexada em função.

**Como pensar:** Mantenha a coluna sem transformação, converta o período em limites e alinhe-os ao tipo temporal do produto.

### Comentário S3S053

**Nível:** Médio

**Uso:** Simulado

**Referência:** [BI, OLTP, OLAP, data warehouse e data mart](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa troca as finalidades típicas de OLTP e OLAP.
- **B)** Correta. OLTP atende transações operacionais; OLAP sustenta exploração histórica e agregada.
- **C)** Incorreta. Os modelos são orientados por cargas e granularidades diferentes.
- **D)** Incorreta. Ambiente analítico depende de integração e não elimina necessariamente sistemas operacionais.

**Conceito:** Contraste entre OLTP e OLAP.

**Pegadinha:** Definir as categorias apenas pelo volume, sem observar finalidade e padrão de consulta.

**Como pensar:** Associe registro corrente e concorrente a OLTP; associe análise histórica multidimensional a OLAP.

### Comentário S3S054

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Fato, dimensão, estrela, floco e granularidade](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A medida pertence ao fato no grão declarado, e unidade oferece eixo descritivo de análise.
- **B)** Incorreta. A alternativa inverte os papéis analítico e descritivo.
- **C)** Incorreta. Medidas numéricas são candidatas naturais a fatos, embora nem todo número seja medida.
- **D)** Incorreta. A descrição de unidade é dimensão e não um fato independente.

**Conceito:** Tabela fato, dimensão e granularidade.

**Pegadinha:** Classificar uma coluna apenas por ser numérica ou textual, sem considerar sua função.

**Como pensar:** Declare o evento representado por cada linha; depois separe medidas do evento e contexto descritivo.

### Comentário S3S055

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Estatísticas, otimizador e cardinalidade](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Estatísticas por coluna podem estar atuais e ainda não representar dependência entre colunas.
- **B)** Correta. Estatísticas desatualizadas ou modelo de independência podem subestimar colunas correlacionadas.
- **C)** Incorreta. Volume real não torna irrelevante a estimativa que orientou a escolha do plano.
- **D)** Incorreta. Mudar o join atua depois do filtro e não corrige sua cardinalidade estimada.

**Conceito:** Estimativa de cardinalidade e correlação.

**Pegadinha:** Culpar imediatamente o índice ou o SGBD sem investigar a qualidade da estimativa.

**Como pensar:** Compare estimado e real por operador, depois examine estatísticas, correlação e seletividade.

### Comentário S3S056

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Índice é caminho de acesso com custo](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Índice é escolha de custo total: benefício das leituras deve ser comparado à escrita, manutenção e frequência da carga.
- **B)** Incorreta. Ganho isolado não demonstra benefício global quando inserções frequentes acumulam o custo de manutenção.
- **C)** Incorreta. Penalidade de escrita, sozinha, não decide contra um índice que pode sustentar consultas críticas recorrentes.
- **D)** Incorreta. Reordenar colunas altera prefixos e seletividade; a hipótese precisa ser retestada e não garante menor manutenção.

**Conceito:** Benefício e custo de manutenção de índice.

**Pegadinha:** Considerar apenas o tempo da consulta-alvo e ignorar toda a carga de escrita.

**Como pensar:** Meça frequência, redução de leitura, custo de escrita, espaço e efeito no conjunto da carga.

### Comentário S3S057

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ETL e ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte os fluxos: descreve ELT como ETL e ETL como ELT.
- **B)** Incorreta. A ordem indicada pelas siglas distingue os fluxos; não é simples marca de fornecedor.
- **C)** Incorreta. No ELT, a transformação principal ocorre depois da carga no ambiente de destino, não permanece na origem.
- **D)** Correta. ETL transforma antes de carregar; ELT carrega primeiro e explora a capacidade de transformação do destino.

**Conceito:** Ordem das etapas em ETL e ELT.

**Pegadinha:** Definir o fluxo pelo tipo de dado, em vez da sequência entre transformação e carga.

**Como pensar:** Expanda as siglas na ordem literal e localize onde ocorre a transformação principal.

### Comentário S3S058

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplos resolvidos de BI](semana_03_estudo.md#s3-d6-exemplos-bi).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Média simples dá o mesmo peso a grupos com 10 e 90 ocorrências.
- **B)** Incorreta. A soma ponderada é 740, mas o universo possui 100 atendimentos; usar 110 duplica parte do denominador.
- **C)** Correta. A soma ponderada é 740 minutos e o total é 100 atendimentos, resultando em 7,4.
- **D)** Incorreta. Médias e quantidades bastam para reconstruir as somas dos grupos e calcular a razão global.

**Conceito:** Média ponderada e medida no grão correto.

**Pegadinha:** Calcular média de médias sem considerar o tamanho diferente dos grupos.

**Como pensar:** Recupere a soma de cada grupo por média × quantidade; depois divida pela quantidade total.

### Comentário S3S059

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Protocolo de otimização](semana_03_estudo.md#s3-d6-otimizacao), com apoio de [Índices](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A sequência estabelece baseline, diagnostica cardinalidade e predicado, testa hipótese e mede efeitos.
- **B)** Incorreta. Mudanças simultâneas e uma execução isolada impedem atribuir causa e medir regressão.
- **C)** Incorreta. Forçar método ignora distribuição e pode melhorar um caso enquanto piora outros.
- **D)** Incorreta. Atualizar estatísticas trata apenas uma hipótese e deixa sem teste a função não sargável e as regressões.

**Conceito:** Protocolo evidencial de otimização.

**Pegadinha:** Pular diagnóstico e transformar a primeira intervenção disponível em solução definitiva.

**Como pensar:** Meça antes, localize o operador divergente, formule uma hipótese, altere uma variável e meça novamente.

### Comentário S3S060

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Business Intelligence](semana_03_estudo.md#s3-d6-bi), com apoio de [Exemplos de BI](semana_03_estudo.md#s3-d6-exemplos-bi).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Sem grão explícito e denominadores, médias mensais não podem ser agregadas corretamente.
- **B)** Incorreta. Modelar antes do grão e perder denominadores torna fatos e médias semanticamente instáveis.
- **C)** Incorreta. Grão de interação duplica atendimentos e soma de médias continua distorcendo grupos.
- **D)** Correta. O plano controla qualidade, unidade analítica, modelo dimensional e cálculo ponderado.

**Conceito:** Pipeline de BI orientado por grão e medida.

**Pegadinha:** Começar pela visualização ou pelo agregado antes de validar fonte, grão e semântica.

**Como pensar:** Siga a cadeia fonte → qualidade → grão → fato/dimensão → medida calculada no denominador correto.
