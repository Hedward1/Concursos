# Banco de Questões — Semana 3

**Período:** 27/07/2026 a 01/08/2026.
**Cargo:** Analista de Sistemas.
**Banca de referência:** Instituto Consulplan.
**Status:** **Material aprovado para execução**.

Este banco reúne **420 questões autorais**, todas com quatro alternativas (`A–D`) e comentário integral: **300 principais** — cinquenta por dia — e **120 extras** — vinte por dia. Questões oficiais não são copiadas para cá; o índice de aplicação no caderno original está em [questões oficiais da Semana 3](../questoes_oficiais/semana_03.md).

## Como usar sem antecipar conteúdo

1. Estude os Blocos 1–3 do dia e conclua a prática prevista.
2. Em D0, resolva primeiro as seis Essenciais; somente avance até a décima se houver tempo para corrigir cada alternativa.
3. Use Aprofundamento depois da teoria correspondente; use Revisão e Simulado nas filas indicadas na jornada.
4. Abra as cinco extras Essenciais do dia apenas em D+7. As demais extras entram depois, conforme a fila.
5. Registre resposta, tempo e confiança antes de consultar o gabarito.
6. Na correção, explique por que a correta atende ao comando e por que cada distrator falha. Só então leia o comentário.

## Identificação e filas

| Conjunto | IDs | Uso planejado |
|---|---|---|
| Principais do Dia 1 | S3D1Q001–S3D1Q050 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 2 | S3D2Q051–S3D2Q100 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 3 | S3D3Q101–S3D3Q150 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 4 | S3D4Q151–S3D4Q200 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 5 | S3D5Q201–S3D5Q250 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 6 | S3D6Q251–S3D6Q300 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Extras de cada dia | Extra Dia N.1–N.20 | 5 Essenciais, 5 Aprofundamento, 5 Revisão e 5 Simulado |

O rótulo **Nível** descreve o esforço cognitivo real do item, não uma cota. O rótulo **Uso** controla a abertura da questão e não equivale à dificuldade. Uma questão Essencial pode ser difícil; uma questão de Simulado pode ser média.

## Critério de construção no estilo da banca

Os itens alternam conceito direto, associação, assertivas, cenário técnico, leitura de SQL e identificação do detalhe discriminador. O foco não é imitar frases: é treinar as operações que a Consulplan exige — leitura integral do comando, confronto de assertivas próximas, distinção entre padrão e produto, rastreamento de linhas e eliminação de absolutos indevidos.

Em comandos negativos (`INCORRETA`, `EXCETO` ou `NÃO`), o comentário contém uma observação explícita. Em temas dependentes de fornecedor, o enunciado delimita SQL Server, MySQL ou PostgreSQL. Cada referência aponta para uma âncora estudável da apostila da própria semana.

## Regra para o caderno de erros

Para cada erro ou acerto inseguro, registre:

- ID da questão e tema;
- causa do erro: conceito, leitura do comando, cálculo, sintaxe, pressuposto de produto ou pressa;
- regra decisiva em uma frase;
- alternativa escolhida e por que parecia plausível;
- data de reabertura em D+2, D+7 ou D+21.

Não memorize a letra. Na reabertura, cubra as alternativas e reconstrua a regra antes de responder.

# Dia 1 — Arquitetura de banco de dados, independência e metadados

## Questões principais

### S3D1Q001 — Dado, banco e SGBD

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

Assinale a alternativa que diferencia corretamente banco de dados e SGBD.

A) Banco de dados é o servidor físico, enquanto SGBD é qualquer arquivo nele armazenado.
B) Banco de dados é a aplicação de atendimento, enquanto SGBD é seu conjunto de usuários.
C) Banco de dados é a coleção organizada de dados; SGBD é o software que a define e gerencia.
D) Banco de dados e SGBD são expressões equivalentes sempre que houver acesso compartilhado.

### S3D1Q002 — Informação em contexto

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

No cadastro, o valor isolado `417` é interpretado como o identificador de um profissional com situação ativa na data consultada. Nesse caso:

A) `417` é dado, e a interpretação vinculada ao cadastro produz informação.
B) `417` é informação completa, ainda que não exista contexto ou atributo associado.
C) a situação ativa é metadado físico porque descreve onde o registro está armazenado.
D) somente textos, e não números, podem ser classificados como dados.

### S3D1Q003 — Sistema de banco de dados

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

O conceito de sistema de banco de dados abrange:

A) exclusivamente os arquivos físicos usados para persistência.
B) apenas o SGBD e suas rotinas internas de armazenamento.
C) somente banco, rede e servidor, sem pessoas ou procedimentos.
D) banco, SGBD, aplicações, usuários, regras, infraestrutura e responsáveis.

### S3D1Q004 — Catálogo como função do SGBD

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Funções centrais de um SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

Qual função permite ao ambiente descrever objetos, atributos e restrições reconhecidos pelo próprio SGBD?

A) glossário informal mantido apenas pelos usuários finais.
B) manutenção de catálogo de sistema com metadados técnicos.
C) conversão automática de qualquer valor em informação correta.
D) definição autônoma do significado institucional de cada indicador.

### S3D1Q005 — Autenticação e autorização

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Funções centrais de um SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

Uma usuária autenticada consulta registros, mas não pode alterá-los. A interpretação correta é:

A) autenticação e autorização são controles distintos, e a permissão pode limitar a usuária à leitura.
B) a autenticação falhou, pois qualquer usuário reconhecido recebe escrita integral.
C) os registros não existem, já que alteração e leitura devem produzir o mesmo resultado.
D) o catálogo substituiu o controle de acesso e bloqueou todas as operações.

### S3D1Q006 — Administração de Dados

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

Qual atividade pertence predominantemente à Administração de Dados?

A) substituir dispositivo de armazenamento com falha.
B) reiniciar o serviço do SGBD após manutenção.
C) executar restauração técnica de uma cópia validada.
D) definir significado, responsabilidade e qualidade do dado.

### S3D1Q007 — Atuação predominante do DBA

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

Assinale a tarefa predominantemente associada ao DBA.

A) escolher sozinho o significado jurídico de “registro regular”.
B) operar o ambiente, aplicar controles técnicos e executar recuperação planejada.
C) aprovar a política institucional sem participação das áreas responsáveis.
D) substituir o glossário corporativo pelo catálogo técnico do produto.

### S3D1Q008 — Cooperação entre AD e DBA

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

Sobre Administração de Dados e DBA, assinale a alternativa correta.

A) As funções são mutuamente excludentes e nunca podem ser acumuladas pela mesma pessoa.
B) O DBA determina o significado do dado porque controla tecnicamente o ambiente.
C) AD orienta governança e semântica, enquanto DBA implementa e opera controles técnicos em cooperação.
D) AD é apenas outro nome para rotina de cópia e restauração.

### S3D1Q009 — Centralização e governança

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Exemplos resolvidos — conceitos e funções do SGBD](semana_03_estudo.md#s3-d1-exemplos-sgbd) e [AD e DBA](semana_03_estudo.md#s3-d1-ad-dba).

Três setores mantêm cópias divergentes do mesmo cadastro. A organização decide adotar um SGBD central. Qual conclusão é tecnicamente adequada?

A) O SGBD centraliza estrutura e controles, mas semântica e responsabilidade pelo dado ainda exigem governança.
B) A centralização garante por si só que toda regra de negócio esteja correta e vigente.
C) O DBA passa a decidir sozinho qual cópia representa a verdade institucional.
D) A existência de catálogo elimina a necessidade de tratar integração e origem dos dados.

### S3D1Q010 — Distribuição de responsabilidades

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Exemplos resolvidos — AD e DBA](semana_03_estudo.md#s3-d1-exemplos-ad-dba).





























































Considere as atividades: I. definir “cadastro ativo”; II. configurar privilégio técnico; III. restaurar o ambiente; IV. atribuir responsável corporativo ao dado. A associação predominante correta é:

A) AD: II e III; DBA: I e IV.
B) AD: I e III; DBA: II e IV.
C) AD: I e IV; DBA: II e III.
D) AD: III e IV; DBA: I e II.

### S3D1Q011 — Mudança de instância

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

Sem alterar atributos ou restrições, foram cadastrados 300 novos profissionais. Houve mudança:

A) apenas do esquema interno.
B) do esquema conceitual e externo.
C) do catálogo, necessariamente.
D) da instância ou estado do banco.

### S3D1Q012 — Mudança de esquema

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

Qual evento altera o esquema?

A) corrigir o nome de uma pessoa cadastrada.
B) acrescentar atributo obrigatório e sua restrição.
C) incluir mais uma ocorrência compatível com a estrutura.
D) consultar o mesmo estado por outro usuário.

### S3D1Q013 — Uso contextual de instância

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

Em uma questão de arquitetura conceitual, “instância do banco” designa, predominantemente:

A) o modelo lógico relativamente estável.
B) o conjunto de definições do catálogo.
C) os valores existentes em determinado instante.
D) obrigatoriamente o processo do produto instalado no servidor.

### S3D1Q014 — Volume e estrutura

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — esquema e instância](semana_03_estudo.md#s3-d1-exemplos-esquema-instancia).

Uma relação passa de mil para dois milhões de tuplas sem alterar atributos, domínios ou restrições. Assinale a conclusão correta.

A) O volume mudou a instância, mas não demonstra alteração do esquema.
B) O número de tuplas integra o esquema externo e o redefine a cada inclusão.
C) Toda mudança quantitativa constitui independência lógica.
D) O crescimento transforma automaticamente o catálogo em glossário.

### S3D1Q015 — Nível externo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

Uma representação destinada ao atendimento exibe nome e situação, omitindo dados restritos. Ela pertence ao nível:

A) interno, porque protege dados internos.
B) externo, porque constitui recorte para um grupo consumidor.
C) físico, porque reduz a quantidade de atributos mostrados.
D) conceitual global, porque toda representação é global.

### S3D1Q016 — Nível conceitual

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

O esquema conceitual descreve:

A) a posição exata de cada página em disco.
B) apenas a tela usada por um departamento.
C) exclusivamente as linhas existentes no momento.
D) a estrutura lógica global integrada dos dados.

### S3D1Q017 — Nível interno

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

Arquivos, páginas e organização física pertencem predominantemente ao nível:

A) interno.
B) externo.
C) conceitual.
D) semântico de negócio.

### S3D1Q018 — Mapeamento arquitetural

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

O mapeamento externo–conceitual relaciona:

A) discos e arquivos ao catálogo do sistema.
B) duas instâncias temporais do mesmo banco.
C) um recorte de usuário à estrutura lógica global.
D) glossário de negócio à mídia de armazenamento.

### S3D1Q019 — Independência física

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Independência física e independência lógica de dados](semana_03_estudo.md#s3-d1-independencia).

O banco é deslocado para outro arranjo de armazenamento, preservando objetos lógicos e contratos externos. O caso exemplifica:

A) mudança de instância com independência lógica.
B) alteração interna absorvida por independência física.
C) alteração externa que redefine o esquema conceitual.
D) substituição do SGBD por um glossário de negócio.

### S3D1Q020 — Independência lógica

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Independência física e independência lógica de dados](semana_03_estudo.md#s3-d1-independencia).

O esquema conceitual passa a distinguir dois tipos de endereço, mas um relatório antigo conserva o campo “endereço de correspondência” por mapeamento explícito. Trata-se de:

A) mera mudança de instância.
B) independência física, pois o relatório não mudou.
C) alteração apenas do nível interno.
D) independência lógica entre os esquemas conceitual e externo.

### S3D1Q021 — Limite da independência

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Independência física e independência lógica de dados](semana_03_estudo.md#s3-d1-independencia).

Assinale a alternativa correta sobre independência de dados.

A) Torna toda alteração invisível, inclusive remoção de atributo exigido pela aplicação.
B) Dispensa mapeamentos entre os níveis arquiteturais.
C) Reduz impacto entre níveis, mas não garante compatibilidade automática com qualquer mudança de significado.
D) Existe somente quando não há esquema externo.

### S3D1Q022 — Classificação pelo nível alterado

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — independência de dados](semana_03_estudo.md#s3-d1-exemplos-independencia).

Uma aplicação permanece inalterada após reorganização de páginas. Por que o caso é físico, e não lógico?

A) Porque toda mudança que preserva aplicação é física.
B) Porque a alteração atingiu o nível interno e preservou o conceitual.
C) Porque páginas integram o esquema externo.
D) Porque independência lógica só ocorre com mudança de instância.

### S3D1Q023 — Três níveis e dois mapeamentos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas) e [Independência de dados](semana_03_estudo.md#s3-d1-independencia).

Analise as afirmações: I. nível externo pode ter vários recortes; II. nível interno trata realização física; III. mapeamentos ajudam a isolar mudanças entre níveis. Está correto o que se afirma em:

A) I, II e III.
B) I e II, apenas.
C) II e III, apenas.
D) I e III, apenas.

### S3D1Q024 — Alteração conceitual e consumidor

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas) e [Independência lógica](semana_03_estudo.md#s3-d1-independencia).

Uma alteração conceitual divide `nome` em componentes. Um consumidor ainda exige o nome completo. A medida coerente é:

A) alterar a organização física e esperar reconstrução automática.
B) apagar o esquema externo, pois ele não pode sobreviver à mudança lógica.
C) classificar a mudança como instância e não adaptar nada.
D) ajustar o mapeamento externo para recompor o valor exigido, se a regra permitir.

### S3D1Q025 — Metadado estrutural

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Nome do atributo, domínio, obrigatoriedade e chave são exemplos predominantes de metadados:

A) narrativos sem relação com estrutura.
B) metadados estruturais do esquema.
C) exclusivamente físicos de disco.
D) pertencentes à instância de cada tupla.

### S3D1Q026 — Metadado semântico

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

A definição institucional de “registro regular” e o critério que a sustenta constituem metadados predominantemente:

A) metadados semânticos.
B) de localização física.
C) da instância corrente.
D) de paginação do SGBD.

### S3D1Q027 — Catálogo de sistema

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Para descobrir quais atributos e restrições o SGBD reconhece em determinado objeto, a fonte técnica mais direta é:

A) uma amostra casual de cinco registros.
B) o texto de uma tela sem documentação.
C) o histórico de versões de um documento externo.
D) o catálogo técnico do SGBD.

### S3D1Q028 — Glossário de negócio

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

O artefato mais voltado a registrar termos, definições e significado corporativo é:

A) arquivo físico de dados.
B) instância do serviço do SGBD.
C) glossário de negócio.
D) esquema interno.

### S3D1Q029 — Proveniência

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — catálogo e metadados](semana_03_estudo.md#s3-d1-exemplos-catalogo).

Ao integrar dois atributos chamados `status`, o analista precisa saber sistema produtor, transformação e destino. Esse conjunto trata predominantemente de:

A) metadados de origem e proveniência.
B) cardinalidade da instância.
C) independência física.
D) autenticação do usuário final.

### S3D1Q030 — Homonímia de atributos

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — catálogo e metadados](semana_03_estudo.md#s3-d1-exemplos-catalogo).

Dois sistemas possuem a coluna `status`, mas usam domínios e significados distintos. Antes de combiná-las, deve-se:

A) uni-las pelo nome, pois homonímia prova equivalência.
B) conferir domínio, definição semântica e origem de cada atributo.
C) alterar apenas o armazenamento físico.
D) considerar os valores metadados e os nomes instâncias.

### S3D1Q031 — Limite do catálogo técnico

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

O catálogo informa que `situacao` é texto obrigatório, mas não esclarece quando alguém é considerado regular. A conclusão correta é:

A) obrigatoriedade técnica define automaticamente a regularidade jurídica.
B) o valor mais frequente deve virar a definição institucional.
C) não há metadado algum, pois o catálogo é inútil.
D) o catálogo cobre estrutura; a semântica precisa de dicionário/glossário e responsável.

### S3D1Q032 — Dicionário de dados

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Em uso amplo, um dicionário de dados pode reunir:

A) somente a ordem física das páginas.
B) apenas valores correntes de cada linha.
C) domínios, regras, significados e responsáveis.
D) unicamente senhas dos administradores.

### S3D1Q033 — Responsável e significado

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Administração de Dados](semana_03_estudo.md#s3-d1-ad-dba) e [Metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Uma área quer descobrir quem responde pelo indicador e qual definição vigente deve usar. A combinação mais adequada é:

A) DBA e metadado exclusivamente físico.
B) governança/AD e metadados semânticos.
C) usuário anônimo e estado da instância.
D) armazenamento e independência física.

### S3D1Q034 — Novo atributo de origem

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Esquema e instância](semana_03_estudo.md#s3-d1-esquema-instancia) e [Metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

O banco passa a registrar `sistema_origem`, inexistente no esquema anterior. Essa mudança:

A) altera apenas os valores, nunca a estrutura.
B) é física porque origem indica servidor.
C) elimina a necessidade de definição semântica.
D) altera o esquema e registra a proveniência dos dados.

### S3D1Q035 — Recorte, regra e armazenamento

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

Associe: I. tela do atendimento; II. modelo lógico integrado; III. organização de arquivos. A ordem correta dos níveis é:

A) externo, conceitual e interno.
B) conceitual, interno e externo.
C) interno, externo e conceitual.
D) externo, interno e conceitual.

### S3D1Q036 — Tipos de metadados

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Considere: I. tipo do atributo; II. sistema produtor; III. responsável pelo dado; IV. definição institucional. Eles correspondem, respectivamente, a metadados:

A) semântico, estrutural, físico e de instância.
B) operacional, externo, interno e físico.
C) estrutural, de origem, administrativo e semântico.
D) de instância, lógico, de segurança e de página.

### S3D1Q037 — Instância, catálogo e esquema

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Esquema, instância e estado](semana_03_estudo.md#s3-d1-esquema-instancia) e [Catálogo](semana_03_estudo.md#s3-d1-catalogo-metadados).

Qual sequência classifica corretamente: incluir uma pessoa; consultar a definição de uma chave; acrescentar uma restrição?

A) esquema, instância, nível externo.
B) catálogo, esquema, instância.
C) nível interno, glossário, estado.
D) instância, catálogo, esquema.

### S3D1Q038 — Duas mudanças distintas

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Esquema e instância](semana_03_estudo.md#s3-d1-esquema-instancia) e [Independência](semana_03_estudo.md#s3-d1-independencia).

Primeiro, são incluídas novas tuplas; depois, arquivos físicos são reorganizados sem mudar a lógica. As classificações são:

A) mudança de instância e mudança interna com independência física.
B) duas mudanças de esquema conceitual.
C) independência lógica e alteração do nível externo.
D) duas mudanças de instância.

### S3D1Q039 — Arquitetura e abstração

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

Analise: I. podem existir vários esquemas externos; II. o conceitual integra a estrutura lógica; III. o interno descreve recorte por usuário. Está correto o que se afirma em:

A) I, II e III.
B) I e III, apenas.
C) I e II, apenas.
D) II e III, apenas.

### S3D1Q040 — Comando negativo sobre metadados

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Assinale a alternativa **INCORRETA**.

A) Metadados estruturais podem descrever tipos e restrições.
B) Igualdade de nome garante igualdade semântica entre sistemas.
C) Proveniência pode registrar origem e transformação.
D) Glossário pode complementar o catálogo técnico.

### S3D1Q041 — Diagnóstico da fonte correta

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Contrastes decisivos](semana_03_estudo.md#s3-d1-contrastes).

Uma equipe precisa confirmar tipo técnico, significado institucional e responsável por `data_base`. Deve consultar, respectivamente:

A) catálogo técnico, glossário semântico e metadado administrativo.
B) apenas os valores mais recentes em três telas.
C) esquema interno, instância e dispositivo físico.
D) histórico de login, arquivo de paginação e nível externo.

### S3D1Q042 — Alteração com impacto controlado

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Independência física e independência lógica](semana_03_estudo.md#s3-d1-independencia).

Qual cenário exige independência lógica, e não apenas física?

A) deslocar arquivos preservando o esquema conceitual.
B) reorganizar páginas sem mudar atributos.
C) trocar mídia mantendo os mesmos objetos lógicos.
D) ampliar o conceitual e preservar recorte externo por mapeamento.

### S3D1Q043 — Caso integrado de governança e arquitetura

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Prática guiada — inventário de mudanças](semana_03_estudo.md#s3-d1-pratica).

O Conselho redefine “regular”, cria `fonte_atualizacao`, mantém uma tela antiga por mapeamento e reorganiza os arquivos. Qual classificação preserva os quatro fatos?

A) DBA/instância; instância; independência física; mudança conceitual.
B) AD/esquema interno; catálogo físico; mudança de instância; independência lógica.
C) AD/metadado semântico; mudança de esquema e proveniência; independência lógica; independência física.
D) glossário/instância; nível externo; independência física; mudança de instância.

### S3D1Q044 — Falha de integração por homonímia

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Exemplos resolvidos — catálogo e metadados](semana_03_estudo.md#s3-d1-exemplos-catalogo) e [AD e DBA](semana_03_estudo.md#s3-d1-ad-dba).

Dois `status` homônimos usam códigos distintos. A integração precisa preservar significado, origem e controle técnico. A ação coerente é:

A) atribuir equivalência pelo nome e pedir ao DBA apenas mais espaço.
B) definir a correspondência semântica e controlar a transformação.
C) converter os dois domínios para texto e dispensar glossário.
D) escolher o código mais frequente e tratá-lo como regra corporativa.

### S3D1Q045 — Três esquemas e segurança de recorte

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas) e [Funções do SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

Uma tela omite dados restritos, o modelo global mantém esses atributos e o armazenamento é reorganizado. Analise: I. a tela é externa; II. o modelo global é conceitual; III. reorganização é interna; IV. o recorte externo, sozinho, não substitui autorização. Está correto:

A) I e II, apenas.
B) II, III e IV, apenas.
C) I, III e IV, apenas.
D) I, II, III e IV.

### S3D1Q046 — Catálogo não prova regra de negócio

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Catálogo e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

O catálogo mostra `situacao CHAR(1)` e obrigatoriedade. Qual conclusão é defensável?

A) O caractere `A` significa “ativo” em qualquer sistema.
B) A obrigatoriedade prova regularidade jurídica.
C) A estrutura existe, mas domínio e regra exigem documentação.
D) O catálogo contém apenas valores da instância.

### S3D1Q047 — Papel predominante em sequência

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Administração de Dados versus DBA](semana_03_estudo.md#s3-d1-ad-dba).

A sequência “definir proprietário do dado → configurar privilégio → testar restauração” envolve, predominantemente:

A) DBA → AD → AD.
B) AD → DBA → DBA.
C) AD → AD → glossário.
D) DBA → DBA → AD.

### S3D1Q048 — Alteração de contrato externo

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Independência de dados](semana_03_estudo.md#s3-d1-independencia) e [Três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

O conceitual substitui `endereco` por duas estruturas. Uma aplicação exige o campo antigo; o armazenamento também muda. Qual plano separa corretamente os impactos?

A) mapear o campo externo à regra e tratar a mudança interna, testando ambos os contratos.
B) classificar tudo como independência física porque o usuário não vê arquivos.
C) preservar somente o armazenamento; o externo se recompõe sem regra.
D) alterar valores da instância e ignorar os esquemas.

### S3D1Q049 — Auditoria de metadados multifiltro

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

Para decidir se dois indicadores podem ser comparados, o analista verifica tipo/domínio, definição, sistema produtor e responsável. Esses filtros são, respectivamente:

A) físico, instância, externo e interno.
B) semântico, estrutural, autorização e catálogo.
C) estrutural, semântico, proveniência e administrativo.
D) catálogo, valor, esquema e página.

### S3D1Q050 — Caso final do Dia 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Prática guiada — inventário de mudanças](semana_03_estudo.md#s3-d1-pratica) e [Contrastes decisivos](semana_03_estudo.md#s3-d1-contrastes).

Uma área altera a definição de indicador; o DBA reorganiza arquivos; 500 registros são incluídos; e o atendimento recebe recorte limitado. A sequência correta é:

A) mudança interna; mudança semântica; esquema; nível conceitual.
B) instância; independência lógica; metadado físico; nível interno.
C) esquema externo; AD; independência física; catálogo.
D) AD/metadado semântico; independência física; instância; nível externo.

## Questões extras de revisão fixa do Dia 1

#### Extra Dia 1.1

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** CFA e CRA-PR
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

Uma notícia de exercício irregular refere-se a atividade realizada no Paraná. A atuação ordinária de registro e fiscalização na jurisdição compete predominantemente:

A) ao CFA, porque toda ocorrência regional exige execução federal direta.
B) ao CRA-PR, dentro de suas atribuições regionais.
C) ao sindicato, que substitui o conselho profissional.
D) ao governo estadual, porque o Regional integra a Administração Direta do estado.

#### Extra Dia 1.2

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** modo Sugestão
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

Para propor alteração que o responsável possa aceitar ou rejeitar antes de incorporar ao texto, deve-se usar:

A) modo de leitura.
B) download como PDF.
C) exclusão do histórico.
D) modo Sugestão.

#### Extra Dia 1.3

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** modalidade e generalização
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

Do enunciado “metadados podem reduzir erros” infere-se corretamente que:

A) existe possibilidade de redução, sem garantia universal de eliminação.
B) metadados sempre eliminam todos os erros.
C) a redução ocorre somente quando não há definição semântica.
D) a expressão “podem” equivale obrigatoriamente a “devem”.

#### Extra Dia 1.4

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** hierarquia normativa
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

Assinale a alternativa correta.

A) Resolução posterior revoga lei anterior sempre que tratar do mesmo tema.
B) Decreto regulamentador ocupa posição superior à lei regulamentada.
C) Ato inferior deve atuar dentro da competência e respeitar a norma legal superior.
D) O ano mais recente é o único critério para resolver conflito normativo.

#### Extra Dia 1.5

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** comentário e edição
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

Qual afirmação diferencia corretamente comentário e edição direta?

A) Comentário substitui automaticamente o trecho selecionado.
B) Edição direta nunca altera o conteúdo atual.
C) Comentário restaura uma versão anterior do arquivo.
D) Comentário registra discussão; edição direta altera o conteúdo autorizado.

#### Extra Dia 1.6

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** lei e decreto
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

A relação segura entre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967 é:

A) o decreto substitui integralmente a lei.
B) a lei dá a base, e o decreto a regulamenta nos limites legais.
C) ambos são resoluções internas de mesma natureza.
D) a lei trata apenas da rotina de edição de documentos.

#### Extra Dia 1.7

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** níveis de acesso
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

Qual papel permite adicionar comentários e sugestões, mas não editar diretamente o conteúdo como editor?

A) proprietário anônimo.
B) leitor.
C) comentador.
D) publicador obrigatório.

#### Extra Dia 1.8

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** conectores
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

Em “os critérios divergiam; portanto, o indicador não era comparável”, `portanto` introduz:

A) consequência.
B) condição ou hipótese.
C) concessão.
D) finalidade.

#### Extra Dia 1.9

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Regimento e Código de Ética
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

Assinale a associação correta.

A) RN nº 651/2024 — Código de Ética; RN nº 671/2025 — armazenamento físico.
B) RN nº 651/2024 — lei federal; RN nº 671/2025 — decreto.
C) RN nº 651/2024 — planilha; RN nº 671/2025 — documento colaborativo.
D) RN nº 651/2024 — Regimento do CRA-PR; RN nº 671/2025 — Código de Ética.

#### Extra Dia 1.10

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** estilos de título
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

Em documento longo, aplicar estilos de título é preferível a apenas aumentar a fonte porque:

A) impede qualquer edição futura.
B) transforma todo leitor em editor.
C) organiza e facilita a navegação.
D) apaga comentários resolvidos.

#### Extra Dia 1.11

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** autonomia do Regional
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

Autonomia técnica, administrativa e financeira do CRA-PR significa que o Regional:

A) atua com autonomia, mas dentro da lei e do sistema.
B) pode revogar lei federal em sua jurisdição.
C) integra a Administração Direta estadual.
D) substitui o CFA na orientação nacional.

#### Extra Dia 1.12

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** histórico de versões
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

Ao recuperar somente um parágrafo antigo sem perder mudanças posteriores válidas, uma estratégia prudente é:

A) apagar permanentemente o histórico.
B) localizar a versão e copiar o trecho útil.
C) conceder edição pública irrestrita.
D) converter todo comentário em título.

#### Extra Dia 1.13

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa e discursiva
- **Assunto:** estrutura da tese
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Discursiva — recorte e tese](semana_03_estudo.md#s3-d1-discursiva-tese).

Qual formulação apresenta posição e dois eixos desenvolvíveis?

A) “Dados são um assunto muito importante atualmente.”
B) “A tecnologia existe e possui muitas ferramentas modernas.”
C) “Dados melhoram serviços com qualidade, finalidade e responsabilização.”
D) “É preciso resolver tudo por meio de sistemas.”

#### Extra Dia 1.14

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** objeto da fonte
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

Um caso envolve organização interna do CRA-PR e, separadamente, possível infração ética. A consulta coerente é:

A) Regimento para organização e Código de Ética para conduta.
B) Código de Ética para arquivos físicos e Regimento para ortografia.
C) apenas a norma de ano mais recente, qualquer que seja seu objeto.
D) somente o Decreto, pois atos do CFA nunca tratam dessas matérias.

#### Extra Dia 1.15

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** menor privilégio
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

Uma pessoa precisa apenas revisar e sugerir mudanças. À luz do menor privilégio, a configuração adequada é:

A) torná-la proprietária do arquivo.
B) publicar o documento para edição anônima.
C) remover todos os controles de compartilhamento.
D) conceder comentário/sugestão, sem edição integral.

#### Extra Dia 1.16

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** competência e território
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

Um fato ocorre no Paraná, mas exige também orientação uniforme para todo o sistema. A distribuição correta é:

A) CRA-PR uniformiza nacionalmente e CFA apenas protocola a notícia local.
B) CRA-PR atua regionalmente no fato e CFA exerce orientação nacional em seu âmbito.
C) sindicato realiza registro e CFA executa toda fiscalização municipal.
D) qualquer CRA pode atuar sem considerar jurisdição.

#### Extra Dia 1.17

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** histórico e permissões
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Google Documentos](semana_03_estudo.md#s3-d1-exemplos-google-docs).

Assinale a conclusão tecnicamente precisa.

A) O histórico permite consultar versões; restaurá-las depende de permissão adequada.
B) Todo leitor pode restaurar qualquer versão e apagar mudanças de editores.
C) Sugestão aceita permanece para sempre fora do conteúdo.
D) Comentário e histórico são o mesmo recurso.

#### Extra Dia 1.18

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** comando negativo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

Em uma questão que pede a alternativa **INCORRETA**, o candidato deve:

A) marcar a primeira frase tecnicamente familiar.
B) escolher qualquer alternativa incompleta, ainda que verdadeira no contexto.
C) ignorar a palavra negativa e procurar a regra geral.
D) avaliar todas as opções e marcar a única afirmação falsa no escopo informado.

#### Extra Dia 1.19

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** cronologia e hierarquia
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_03_estudo.md#s3-d1-exemplos-legislacao).

Uma resolução recente parece contrariar requisito expresso da lei. Qual raciocínio deve prevalecer?

A) aplicar a resolução apenas porque possui número maior.
B) conferir objeto, competência e hierarquia, rejeitando afastamento automático da lei.
C) ignorar todas as normas anteriores a 2025.
D) tratar lei e resolução como documentos colaborativos de igual valor.

#### Extra Dia 1.20

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** sugestão, comentário e versão
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Google Documentos](semana_03_estudo.md#s3-d1-exemplos-google-docs).

Uma revisora deve propor mudança, explicar o motivo e permitir recuperação do estado anterior. A combinação coerente é:

A) edição pública, exclusão de comentários e remoção do histórico.
B) modo leitura, download e alteração do original fora do sistema.
C) sugestão, comentário associado e histórico de versões com permissões adequadas.
D) comentário convertido automaticamente em edição definitiva.

## Gabarito do Dia 1

### Gabarito das questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | C |
| 2 | A |
| 3 | D |
| 4 | B |
| 5 | A |
| 6 | D |
| 7 | B |
| 8 | C |
| 9 | A |
| 10 | C |
| 11 | D |
| 12 | B |
| 13 | C |
| 14 | A |
| 15 | B |
| 16 | D |
| 17 | A |
| 18 | C |
| 19 | B |
| 20 | D |
| 21 | C |
| 22 | B |
| 23 | A |
| 24 | D |
| 25 | B |
| 26 | A |
| 27 | D |
| 28 | C |
| 29 | A |
| 30 | B |
| 31 | D |
| 32 | C |
| 33 | B |
| 34 | D |
| 35 | A |
| 36 | C |
| 37 | D |
| 38 | A |
| 39 | C |
| 40 | B |
| 41 | A |
| 42 | D |
| 43 | C |
| 44 | B |
| 45 | D |
| 46 | C |
| 47 | B |
| 48 | A |
| 49 | C |
| 50 | D |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 1.1 | B |
| 1.2 | D |
| 1.3 | A |
| 1.4 | C |
| 1.5 | D |
| 1.6 | B |
| 1.7 | C |
| 1.8 | A |
| 1.9 | D |
| 1.10 | C |
| 1.11 | A |
| 1.12 | B |
| 1.13 | C |
| 1.14 | A |
| 1.15 | D |
| 1.16 | B |
| 1.17 | A |
| 1.18 | D |
| 1.19 | B |
| 1.20 | C |

## Comentários do Dia 1

### Comentário S3D1Q001

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Servidor é infraestrutura, e arquivo não é software gerenciador.
- **B)** Incorreta. Aplicação e usuários integram o sistema mais amplo, não definem banco e SGBD.
- **C)** Correta. Separa a coleção organizada do software que a administra.
- **D)** Incorreta. Compartilhamento não torna os conceitos sinônimos.

**Conceito:** banco de dados versus SGBD.

**Pegadinha:** chamar o equipamento ou a aplicação de SGBD.

**Como pensar:** identifique primeiro o conteúdo persistido e depois o software que o gerencia.

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

### Comentário S3D1Q002

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O valor ganha significado quando ligado ao atributo e ao estado consultado.
- **B)** Incorreta. Sem contexto, o número não comunica sozinho a informação descrita.
- **C)** Incorreta. Situação é dado do cadastro, não localização física.
- **D)** Incorreta. Números, textos, imagens e outros símbolos podem representar dados.

**Conceito:** dado e informação contextualizada.

**Pegadinha:** confundir valor isolado com interpretação completa.

**Como pensar:** pergunte o que o símbolo representa e sob qual regra ele é interpretado.

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

### Comentário S3D1Q003

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Arquivos físicos são apenas parte da infraestrutura.
- **B)** Incorreta. O SGBD é componente do sistema, não seu todo.
- **C)** Incorreta. Pessoas e procedimentos também integram o sistema.
- **D)** Correta. Reúne dados, software, consumidores, regras e meios de operação.

**Conceito:** abrangência do sistema de banco de dados.

**Pegadinha:** reduzir o sistema ao produto instalado.

**Como pensar:** liste tudo o que precisa cooperar para o dado produzir serviço utilizável.

**Referência:** [Dado, informação, banco de dados, SGBD e sistema de banco de dados](semana_03_estudo.md#s3-d1-conceitos-sgbd).

### Comentário S3D1Q004

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Glossário informal não é o mecanismo técnico mantido pelo SGBD.
- **B)** Correta. O catálogo registra metadados dos objetos reconhecidos pelo ambiente.
- **C)** Incorreta. Software não garante correção sem regra e dado adequados.
- **D)** Incorreta. Significado institucional exige governança, não decisão autônoma do produto.

**Conceito:** função de catálogo do SGBD.

**Pegadinha:** atribuir ao catálogo capacidade semântica que ele não possui sozinho.

**Como pensar:** se a pergunta é sobre objetos técnicos conhecidos pelo produto, procure o catálogo.

**Referência:** [Funções centrais de um SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

### Comentário S3D1Q005

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Identidade reconhecida não implica permissão para toda operação.
- **B)** Incorreta. A leitura comprova que a autenticação pode ter sido aceita.
- **C)** Incorreta. O registro foi consultado; bloqueio de escrita não prova inexistência.
- **D)** Incorreta. Catálogo descreve objetos; não substitui autorização.

**Conceito:** autenticação separada de autorização.

**Pegadinha:** tratar login válido como privilégio irrestrito.

**Como pensar:** separe “quem é” de “o que pode fazer”.

**Referência:** [Funções centrais de um SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

### Comentário S3D1Q006

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Substituição de mídia é operação técnica.
- **B)** Incorreta. Reinício do serviço pertence à administração do ambiente.
- **C)** Incorreta. Restauração é atividade técnica predominante do DBA.
- **D)** Correta. Significado, responsabilidade e qualidade pertencem à governança de dados.

**Conceito:** foco da Administração de Dados.

**Pegadinha:** escolher toda tarefa que menciona “dados” como AD.

**Como pensar:** diferencie decisão corporativa sobre o ativo da operação do ambiente.

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

### Comentário S3D1Q007

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Conceito jurídico/corporativo não é escolha técnica unilateral.
- **B)** Correta. Resume operação, proteção e recuperação do ambiente.
- **C)** Incorreta. Política institucional exige atores responsáveis pelo negócio.
- **D)** Incorreta. Catálogo e glossário possuem funções complementares.

**Conceito:** atuação predominante do DBA.

**Pegadinha:** converter domínio técnico em autoridade sobre significado institucional.

**Como pensar:** procure tarefas que exigem administrar plataforma e controles técnicos.

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

### Comentário S3D1Q008

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Uma pessoa pode acumular papéis, embora as tarefas continuem distintas.
- **B)** Incorreta. Controle técnico não transfere definição corporativa ao DBA.
- **C)** Correta. Expressa a cooperação entre governança e implementação.
- **D)** Incorreta. AD não se reduz a cópia e restauração.

**Conceito:** relação entre AD e DBA.

**Pegadinha:** transformar focos predominantes em fronteira pessoal absoluta.

**Como pensar:** classifique a natureza da tarefa, não apenas o cargo escrito no organograma.

**Referência:** [Administração de Dados versus Administração de Banco de Dados](semana_03_estudo.md#s3-d1-ad-dba).

### Comentário S3D1Q009

**Nível:** Difícil

**Uso:** Essenciais

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Une capacidade técnica e necessidade permanente de governança.
- **B)** Incorreta. Um SGBD também pode aplicar regra mal definida.
- **C)** Incorreta. Fonte institucional não é escolhida unilateralmente pelo DBA.
- **D)** Incorreta. Catálogo não resolve, sozinho, correspondência e proveniência.

**Conceito:** limite da centralização tecnológica.

**Pegadinha:** atribuir efeito automático de qualidade à adoção do SGBD.

**Como pensar:** separe o que o software impõe do que a organização precisa definir.

**Referência:** [Exemplos resolvidos — conceitos e funções do SGBD](semana_03_estudo.md#s3-d1-exemplos-sgbd) e [AD e DBA](semana_03_estudo.md#s3-d1-ad-dba).

### Comentário S3D1Q010

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Inverte significado/responsável com configuração/recuperação.
- **B)** Incorreta. Restauração é técnica e atribuição de responsável é governança.
- **C)** Correta. I e IV são de governança; II e III, de operação técnica.
- **D)** Incorreta. Definição corporativa não é tarefa predominante do DBA.

**Conceito:** classificação integrada de responsabilidades.

**Pegadinha:** decidir pelo verbo genérico sem observar o objeto da ação.

**Como pensar:** marque cada atividade como semântica/governança ou plataforma/operação.

**Referência:** [Exemplos resolvidos — AD e DBA](semana_03_estudo.md#s3-d1-exemplos-ad-dba).

### Comentário S3D1Q011

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Nenhuma organização física foi descrita.
- **B)** Incorreta. A estrutura lógica e os recortes permaneceram.
- **C)** Incorreta. Incluir linhas não obriga alterar o catálogo.
- **D)** Correta. Somente o estado corrente recebeu novas ocorrências.

**Conceito:** mudança de instância.

**Pegadinha:** confundir crescimento com alteração estrutural.

**Como pensar:** procure atributo, relacionamento ou restrição novos; se não houver, mudou o estado.

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

### Comentário S3D1Q012

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Correção troca valor da instância.
- **B)** Correta. Atributo e restrição integram o esquema.
- **C)** Incorreta. Nova ocorrência muda apenas o estado.
- **D)** Incorreta. Consulta não redefine estrutura.

**Conceito:** mudança de esquema.

**Pegadinha:** chamar preenchimento futuro de prova de mudança apenas da instância.

**Como pensar:** estrutura define quais valores podem existir; conteúdo mostra quais existem agora.

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

### Comentário S3D1Q013

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Modelo lógico corresponde ao esquema.
- **B)** Incorreta. Catálogo descreve definições.
- **C)** Correta. Instância conceitual é o estado dos valores no instante.
- **D)** Incorreta. Esse é outro uso operacional do termo, não o contexto dado.

**Conceito:** polissemia contextual de instância.

**Pegadinha:** importar a definição do produto para uma questão de arquitetura conceitual.

**Como pensar:** leia o contexto antes de escolher entre estado dos dados e instalação do serviço.

**Referência:** [Esquema, instância e estado do banco](semana_03_estudo.md#s3-d1-esquema-instancia).

### Comentário S3D1Q014

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Quantidade de tuplas pertence ao estado considerado.
- **B)** Incorreta. O esquema não é redefinido a cada inserção.
- **C)** Incorreta. Independência lógica envolve alteração conceitual.
- **D)** Incorreta. Volume não converte catálogo em artefato semântico.

**Conceito:** volume da instância versus estrutura.

**Pegadinha:** usar “cardinalidade aumentou” como sinônimo de esquema alterado.

**Como pensar:** volume é propriedade do estado; atributos e regras são propriedades do esquema.

**Referência:** [Exemplos resolvidos — esquema e instância](semana_03_estudo.md#s3-d1-exemplos-esquema-instancia).

### Comentário S3D1Q015

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Interno trata realização física, não confidencialidade.
- **B)** Correta. É um recorte adequado ao atendimento.
- **C)** Incorreta. Menos atributos visíveis não caracteriza nível físico.
- **D)** Incorreta. A representação é específica, não global.

**Conceito:** esquema externo.

**Pegadinha:** interpretar “interno” como dado reservado.

**Como pensar:** pergunte para qual grupo ou aplicação a representação foi construída.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

### Comentário S3D1Q016

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Posição física pertence ao nível interno.
- **B)** Incorreta. Tela departamental é externa.
- **C)** Incorreta. Linhas existentes formam a instância.
- **D)** Correta. O conceitual integra a estrutura lógica do domínio.

**Conceito:** nível conceitual.

**Pegadinha:** confundir o esquema global com um desenho de tela.

**Como pensar:** localize a descrição lógica comum aos diferentes consumidores.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

### Comentário S3D1Q017

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Arquivos e páginas materializam a organização física.
- **B)** Incorreta. Externo é recorte de consumidor.
- **C)** Incorreta. Conceitual é a lógica global.
- **D)** Incorreta. Semântica de negócio não descreve páginas.

**Conceito:** nível interno.

**Pegadinha:** trocar interno por conceitual devido a ambos não serem telas.

**Como pensar:** se a pergunta chega à forma de armazenamento, escolha o interno.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

### Comentário S3D1Q018

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Discos relacionam-se ao mapeamento conceitual–interno.
- **B)** Incorreta. Estados temporais não definem esse mapeamento.
- **C)** Correta. O recorte externo deriva da estrutura conceitual.
- **D)** Incorreta. Glossário e mídia não formam o par arquitetural.

**Conceito:** mapeamento externo–conceitual.

**Pegadinha:** relacionar níveis não adjacentes por palavras soltas.

**Como pensar:** siga a cadeia consumidor → lógica global → realização física.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

### Comentário S3D1Q019

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não houve alteração de valores nem do conceitual.
- **B)** Correta. Mudou a realização interna e preservou-se a lógica.
- **C)** Incorreta. Nenhum recorte externo foi redefinido.
- **D)** Incorreta. Glossário não substitui o SGBD.

**Conceito:** independência física.

**Pegadinha:** classificar pelo fato de a aplicação permanecer, em vez do nível alterado.

**Como pensar:** identifique o objeto modificado; armazenamento aponta para o nível interno.

**Referência:** [Independência física e independência lógica de dados](semana_03_estudo.md#s3-d1-independencia).

### Comentário S3D1Q020

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. A estrutura conceitual foi alterada.
- **B)** Incorreta. O nível modificado não é o interno.
- **C)** Incorreta. A mudança lógica não se limita ao armazenamento.
- **D)** Correta. O mapeamento preserva contrato externo diante da alteração conceitual.

**Conceito:** independência lógica.

**Pegadinha:** chamar toda preservação de relatório de independência física.

**Como pensar:** mudança conceitual com recorte externo preservado aponta para independência lógica.

**Referência:** [Independência física e independência lógica de dados](semana_03_estudo.md#s3-d1-independencia).

### Comentário S3D1Q021

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Remover dado exigido pode quebrar o contrato.
- **B)** Incorreta. Mapeamentos são parte do isolamento entre níveis.
- **C)** Correta. A independência reduz acoplamento, mas possui limites semânticos.
- **D)** Incorreta. Esquemas externos são justamente beneficiários do mecanismo.

**Conceito:** alcance não absoluto da independência.

**Pegadinha:** interpretar abstração como compatibilidade automática ilimitada.

**Como pensar:** teste se a informação consumida ainda pode ser derivada com o mesmo significado.

**Referência:** [Independência física e independência lógica de dados](semana_03_estudo.md#s3-d1-independencia).

### Comentário S3D1Q022

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Preservar aplicação também pode ocorrer em mudança conceitual mapeada.
- **B)** Correta. Páginas pertencem ao interno e o conceitual não mudou.
- **C)** Incorreta. Páginas não integram o esquema externo.
- **D)** Incorreta. Independência lógica não se define por instância.

**Conceito:** classificação pelo nível efetivamente alterado.

**Pegadinha:** usar somente o efeito percebido pela aplicação.

**Como pensar:** comece pela causa técnica da mudança, não pelo resultado comum de preservação.

**Referência:** [Exemplos resolvidos — independência de dados](semana_03_estudo.md#s3-d1-exemplos-independencia).

### Comentário S3D1Q023

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. As três afirmações correspondem à arquitetura apresentada.
- **B)** Incorreta. III também é verdadeira.
- **C)** Incorreta. I também é verdadeira.
- **D)** Incorreta. II também é verdadeira.

**Conceito:** níveis e mapeamentos da arquitetura.

**Pegadinha:** negar multiplicidade de esquemas externos ou função isoladora dos mapeamentos.

**Como pensar:** julgue separadamente recortes, armazenamento e relação entre os níveis.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas) e [Independência de dados](semana_03_estudo.md#s3-d1-independencia).

### Comentário S3D1Q024

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Organização física não recompõe significado lógico.
- **B)** Incorreta. O externo pode ser preservado por adaptação.
- **C)** Incorreta. Dividir atributo altera a estrutura conceitual.
- **D)** Correta. O mapeamento pode recompor o contrato antigo se a regra for definida.

**Conceito:** adaptação externo–conceitual.

**Pegadinha:** presumir recomposição automática sem regra de formação do nome.

**Como pensar:** verifique se o valor antigo pode ser derivado dos novos componentes.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas) e [Independência lógica](semana_03_estudo.md#s3-d1-independencia).

### Comentário S3D1Q025

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Os elementos listados descrevem estrutura concreta.
- **B)** Correta. Tipo, domínio e restrição são metadados estruturais.
- **C)** Incorreta. Não se limitam à disposição em disco.
- **D)** Incorreta. Não são valores das tuplas.

**Conceito:** metadados estruturais.

**Pegadinha:** confundir definição de atributo com seu conteúdo.

**Como pensar:** se descreve como o dado é definido, classifique como estrutural.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q026

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Definição e critério descrevem significado institucional.
- **B)** Incorreta. Não indicam posição de armazenamento.
- **C)** Incorreta. Não são valores correntes.
- **D)** Incorreta. Paginação é detalhe interno.

**Conceito:** metadados semânticos.

**Pegadinha:** chamar toda descrição de atributo de metadado físico.

**Como pensar:** pergunte se o metadado responde “o que significa?”.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q027

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Amostra não prova definição e restrições.
- **B)** Incorreta. Tela pode omitir ou transformar a estrutura.
- **C)** Incorreta. Histórico documental não é fonte direta do esquema reconhecido.
- **D)** Correta. O catálogo descreve objetos técnicos do SGBD.

**Conceito:** consulta ao catálogo de sistema.

**Pegadinha:** inferir obrigatoriedade pela ausência de nulos em poucos registros.

**Como pensar:** para regra estrutural, consulte a definição, não só ocorrências.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q028

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Arquivo físico não é artefato de definição corporativa.
- **B)** Incorreta. Processo do SGBD é componente operacional.
- **C)** Correta. O glossário organiza termos e significados do negócio.
- **D)** Incorreta. Esquema interno trata realização física.

**Conceito:** glossário de negócio.

**Pegadinha:** usar catálogo e glossário como sinônimos absolutos.

**Como pensar:** significado compartilhado entre áreas aponta para glossário.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q029

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Origem, transformação e destino compõem proveniência.
- **B)** Incorreta. Cardinalidade mede quantidade de tuplas.
- **C)** Incorreta. Independência física trata mudança interna.
- **D)** Incorreta. Identidade do usuário não descreve o fluxo do dado.

**Conceito:** metadados de proveniência.

**Pegadinha:** reduzir origem à localização física do servidor.

**Como pensar:** acompanhe o caminho do dado desde produtor até consumidor.

**Referência:** [Exemplos resolvidos — catálogo e metadados](semana_03_estudo.md#s3-d1-exemplos-catalogo).

### Comentário S3D1Q030

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Nome igual pode esconder conceitos diferentes.
- **B)** Correta. Os três filtros evitam integração semântica indevida.
- **C)** Incorreta. Armazenamento não resolve equivalência conceitual.
- **D)** Incorreta. Valores são dados; nomes e definições são metadados.

**Conceito:** homonímia e integração semântica.

**Pegadinha:** mapear colunas automaticamente pelo rótulo.

**Como pensar:** compare domínio, significado e proveniência antes de combinar.

**Referência:** [Exemplos resolvidos — catálogo e metadados](semana_03_estudo.md#s3-d1-exemplos-catalogo).

### Comentário S3D1Q031

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Obrigatoriedade técnica não define condição jurídica.
- **B)** Incorreta. Frequência não cria regra institucional.
- **C)** Incorreta. Há metadado estrutural útil, mas insuficiente.
- **D)** Correta. É necessário complementar estrutura com significado e responsabilidade.

**Conceito:** limite semântico do catálogo.

**Pegadinha:** transformar tipo e nulabilidade em definição de negócio.

**Como pensar:** se a pergunta contém “quando é considerado”, procure regra semântica.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q032

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. Dicionário não se restringe a armazenamento.
- **B)** Incorreta. Valores correntes não esgotam a descrição do dado.
- **C)** Correta. Reúne componentes técnicos e semânticos do uso amplo.
- **D)** Incorreta. Senhas não constituem o conteúdo definidor do artefato.

**Conceito:** abrangência do dicionário de dados.

**Pegadinha:** reduzir dicionário a lista de colunas.

**Como pensar:** procure o artefato que documenta forma, regra e interpretação.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q033

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Tipo físico não responde responsabilidade e definição.
- **B)** Correta. Governança usa metadados administrativos e semânticos.
- **C)** Incorreta. Usuário anônimo e estado não estabelecem autoridade.
- **D)** Incorreta. Armazenamento não resolve significado.

**Conceito:** governança apoiada em metadados.

**Pegadinha:** atribuir ao operador técnico toda decisão sobre o indicador.

**Como pensar:** “quem responde?” é administrativo; “o que significa?” é semântico.

**Referência:** [Administração de Dados](semana_03_estudo.md#s3-d1-ad-dba) e [Metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q034

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Um atributo inexistente foi acrescentado ao esquema.
- **B)** Incorreta. Origem do dado não significa organização física.
- **C)** Incorreta. Saber a origem não substitui saber o significado.
- **D)** Correta. Há mudança estrutural e registro de proveniência.

**Conceito:** esquema associado a metadado de origem.

**Pegadinha:** classificar “origem” sempre como nível interno.

**Como pensar:** diferencie origem informacional de localização em disco.

**Referência:** [Esquema e instância](semana_03_estudo.md#s3-d1-esquema-instancia) e [Metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q035

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Tela é externa, modelo global é conceitual e arquivos são internos.
- **B)** Incorreta. Desloca os três objetos para níveis errados.
- **C)** Incorreta. Tela não é interna e arquivos não são conceituais.
- **D)** Incorreta. Arquivos não pertencem ao nível externo.

**Conceito:** associação dos três níveis.

**Pegadinha:** classificar pela ordem em que os elementos aparecem no sistema.

**Como pensar:** consumidor, lógica e armazenamento formam a sequência correta.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

### Comentário S3D1Q036

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Tipo é estrutural, não semântico.
- **B)** Incorreta. As categorias não correspondem aos objetos listados.
- **C)** Correta. Mapeia definição técnica, fluxo, responsável e significado.
- **D)** Incorreta. Confunde valores com descrições.

**Conceito:** classificação multidimensional de metadados.

**Pegadinha:** chamar qualquer informação sobre o dado de estrutural.

**Como pensar:** associe cada pergunta: como é definido, de onde veio, quem responde, o que significa.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q037

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Inclusão muda instância e restrição muda esquema.
- **B)** Incorreta. Inverte conteúdo, descrição e estrutura.
- **C)** Incorreta. Nenhuma das três associações atende ao caso.
- **D)** Correta. Classifica valor novo, metadado técnico e regra estrutural.

**Conceito:** relação entre estado, catálogo e esquema.

**Pegadinha:** tratar consulta ao catálogo como mudança do esquema.

**Como pensar:** diferencie ação sobre valores, leitura de definição e alteração da definição.

**Referência:** [Esquema, instância e estado](semana_03_estudo.md#s3-d1-esquema-instancia) e [Catálogo](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q038

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A primeira muda o estado; a segunda, a realização física.
- **B)** Incorreta. Nenhuma mudança conceitual foi informada.
- **C)** Incorreta. Inclusão não é independência lógica e arquivos não são externos.
- **D)** Incorreta. Reorganização física não é mero valor da instância.

**Conceito:** classificação sequencial de mudanças.

**Pegadinha:** usar uma única categoria para eventos de níveis distintos.

**Como pensar:** classifique cada verbo e seu objeto separadamente.

**Referência:** [Esquema e instância](semana_03_estudo.md#s3-d1-esquema-instancia) e [Independência](semana_03_estudo.md#s3-d1-independencia).

### Comentário S3D1Q039

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. III é falsa: interno não é recorte de usuário.
- **B)** Incorreta. III é falsa.
- **C)** Correta. I e II descrevem adequadamente externo e conceitual.
- **D)** Incorreta. Inclui III e exclui I.

**Conceito:** propriedades dos níveis arquiteturais.

**Pegadinha:** associar “interno” a usuário interno.

**Como pensar:** nível interno responde como se armazena, não quem consulta.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

### Comentário S3D1Q040

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: B.**

**Observação:** o comando solicita a alternativa **INCORRETA**.

**Análise das alternativas:**

- **A)** Correta como afirmação. Tipos e restrições são estruturais.
- **B)** Incorreta e gabarito. Nome igual não garante o mesmo significado.
- **C)** Correta como afirmação. Proveniência descreve o fluxo do dado.
- **D)** Correta como afirmação. Glossário complementa descrição técnica.

**Conceito:** limites e categorias de metadados.

**Pegadinha:** esquecer a polaridade negativa ou confiar em homonímia.

**Como pensar:** marque V/F em cada alternativa e só depois aplique o comando.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q041

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Tipo técnico, significado institucional e responsável são metadados estrutural, semântico e administrativo, respectivamente.
- **B)** Incorreta. Valores exibidos não documentam definição nem responsabilidade.
- **C)** Incorreta. Instância e dispositivo físico não respondem às três perguntas propostas.
- **D)** Incorreta. Logs e paginação são evidências operacionais, não as fontes semânticas requeridas.

**Conceito:** seleção da fonte de metadados conforme a pergunta.

**Pegadinha:** procurar todas as respostas no catálogo técnico.

**Como pensar:** traduza cada necessidade em “como está definido?”, “o que significa?” e “quem responde?”.

**Referência:** [Contrastes decisivos](semana_03_estudo.md#s3-d1-contrastes).

### Comentário S3D1Q042

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Deslocamento de arquivos é mudança do nível interno.
- **B)** Incorreta. Reorganização de páginas preserva o conceitual e exige independência física.
- **C)** Incorreta. Troca de mídia também é alteração física.
- **D)** Correta. Muda o esquema conceitual e usa mapeamento para preservar a visão externa.

**Conceito:** distinção entre independência lógica e física.

**Pegadinha:** classificar pelo fato de o usuário não perceber a mudança.

**Como pensar:** identifique primeiro o esquema alterado; depois, o contrato preservado.

**Referência:** [Independência física e independência lógica](semana_03_estudo.md#s3-d1-independencia).

### Comentário S3D1Q043

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Redefinir conceito é governança/AD, e criar atributo não é mera mudança de instância.
- **B)** Incorreta. Regra corporativa não pertence ao esquema interno, e preservar tela após mudança conceitual caracteriza independência lógica.
- **C)** Correta. Classifica, na ordem, semântica, estrutura/proveniência, mapeamento lógico e organização física.
- **D)** Incorreta. Definição não é valor da instância, e reorganização de arquivos não é inclusão de registros.

**Conceito:** inventário integrado de mudanças em banco de dados.

**Pegadinha:** aplicar uma única categoria a quatro fatos de naturezas diferentes.

**Como pensar:** classifique cada verbo e seu objeto antes de analisar a sequência.

**Referência:** [Prática guiada — inventário de mudanças](semana_03_estudo.md#s3-d1-pratica).

### Comentário S3D1Q044

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Homonímia não prova equivalência semântica, e espaço não resolve o mapeamento.
- **B)** Correta. Une decisão semântica, registro de origem e implementação técnica controlada.
- **C)** Incorreta. Uniformizar o tipo físico não torna iguais domínios de negócio distintos.
- **D)** Incorreta. Frequência de uso não cria regra corporativa legítima.

**Conceito:** integração semântica com proveniência e governança.

**Pegadinha:** assumir que colunas de mesmo nome representam o mesmo conceito.

**Como pensar:** confirme significado, domínio e origem antes de implementar transformação.

**Referência:** [Exemplos resolvidos — catálogo e metadados](semana_03_estudo.md#s3-d1-exemplos-catalogo) e [AD e DBA](semana_03_estudo.md#s3-d1-ad-dba).

### Comentário S3D1Q045

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Omite as afirmações III e IV, ambas verdadeiras.
- **B)** Incorreta. Exclui I, embora a tela seja uma visão externa.
- **C)** Incorreta. Exclui II, embora o modelo global seja conceitual.
- **D)** Correta. As quatro afirmações distinguem adequadamente visão, modelo, armazenamento e autorização.

**Conceito:** três esquemas associados ao controle de acesso.

**Pegadinha:** considerar que ocultar um campo na tela substitui autorização no SGBD.

**Como pensar:** classifique cada artefato por nível e trate segurança como função adicional.

**Referência:** [Arquitetura em três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas) e [Funções do SGBD](semana_03_estudo.md#s3-d1-funcoes-sgbd).

### Comentário S3D1Q046

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. O significado de `A` depende do domínio documentado no sistema.
- **B)** Incorreta. Obrigatoriedade técnica não comprova situação jurídica.
- **C)** Correta. Tipo e nulabilidade são estruturais; interpretação e regra exigem metadados adicionais.
- **D)** Incorreta. O catálogo descreve objetos e restrições, não apenas valores correntes.

**Conceito:** limite probatório do catálogo técnico.

**Pegadinha:** transformar uma restrição estrutural em conclusão semântica.

**Como pensar:** pergunte o que o catálogo efetivamente mostra e o que ainda precisa de glossário/regra.

**Referência:** [Catálogo e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q047

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Proprietário do dado é decisão de governança, não tarefa predominantemente técnica.
- **B)** Correta. AD define responsabilidade; DBA configura acesso e testa recuperação.
- **C)** Incorreta. Configuração de privilégio e restauração não são funções de glossário.
- **D)** Incorreta. Inverte o primeiro e o último papéis.

**Conceito:** distribuição de responsabilidades entre AD e DBA.

**Pegadinha:** associar toda atividade que envolve banco ao DBA.

**Como pensar:** separe decisão corporativa de execução e controle técnico.

**Referência:** [Administração de Dados versus DBA](semana_03_estudo.md#s3-d1-ad-dba).

### Comentário S3D1Q048

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Trata separadamente a compatibilidade externo–conceitual e a mudança conceitual–interna.
- **B)** Incorreta. A alteração conceitual não se converte em física apenas por ocultar arquivos do usuário.
- **C)** Incorreta. O campo antigo precisa de regra explícita de mapeamento.
- **D)** Incorreta. O caso modifica estruturas, não somente valores da instância.

**Conceito:** coexistência de independência lógica e física.

**Pegadinha:** agrupar impactos de níveis diferentes sob uma única independência.

**Como pensar:** examine separadamente os dois mapeamentos da arquitetura em três esquemas.

**Referência:** [Independência de dados](semana_03_estudo.md#s3-d1-independencia) e [Três esquemas](semana_03_estudo.md#s3-d1-tres-esquemas).

### Comentário S3D1Q049

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. As categorias arquiteturais não correspondem aos quatro filtros informados.
- **B)** Incorreta. Inverte tipo e definição e chama origem de autorização.
- **C)** Correta. Tipo/domínio, definição, produtor e responsável mapeiam as quatro categorias na ordem.
- **D)** Incorreta. Valor, esquema e página não descrevem o conjunto da auditoria.

**Conceito:** auditoria multidimensional de metadados.

**Pegadinha:** confundir proveniência com localização física.

**Como pensar:** associe cada filtro à pergunta estrutural, semântica, de origem ou de responsabilidade.

**Referência:** [Catálogo de sistema, dicionário de dados e metadados](semana_03_estudo.md#s3-d1-catalogo-metadados).

### Comentário S3D1Q050

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Inverte a mudança semântica e a interna e chama inclusão de registros de esquema.
- **B)** Incorreta. Definição não é instância, e reorganização de arquivos não é independência lógica.
- **C)** Incorreta. A sequência não corresponde aos quatro eventos descritos.
- **D)** Correta. Associa definição a AD/semântica, arquivos a independência física, inclusões a instância e recorte a externo.

**Conceito:** síntese das classificações do Dia 1.

**Pegadinha:** decidir pela presença de uma palavra isolada sem seguir a ordem dos fatos.

**Como pensar:** construa uma tabela evento → objeto alterado → categoria antes de comparar opções.

**Referência:** [Prática guiada — inventário de mudanças](semana_03_estudo.md#s3-d1-pratica) e [Contrastes decisivos](semana_03_estudo.md#s3-d1-contrastes).

### Comentário Extra Dia 1.1

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** CFA e CRA-PR
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A orientação nacional do CFA não elimina a execução regional ordinária.
- **B)** Correta. O CRA-PR exerce registro e fiscalização no âmbito de sua jurisdição.
- **C)** Incorreta. Sindicato não substitui conselho profissional nessas atribuições legais.
- **D)** Incorreta. O Regional não integra a Administração Direta estadual.

**Conceito:** competência regional do CRA-PR.

**Pegadinha:** confundir coordenação nacional com execução direta de todo caso local.

**Como pensar:** identifique território e natureza da atribuição antes de escolher o órgão.

**Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

### Comentário Extra Dia 1.2

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** modo Sugestão
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Leitura não cria proposta incorporável ao texto.
- **B)** Incorreta. Exportar PDF não oferece fluxo de aceitar ou rejeitar mudança.
- **C)** Incorreta. Excluir histórico reduz rastreabilidade e não cria sugestão.
- **D)** Correta. O modo Sugestão registra a alteração para decisão posterior.

**Conceito:** revisão colaborativa no Google Documentos.

**Pegadinha:** confundir comentário genérico com alteração textual proposta.

**Como pensar:** procure o recurso cujo ciclo é propor → aceitar/rejeitar.

**Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

### Comentário Extra Dia 1.3

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** modalidade e generalização
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. “Podem” expressa possibilidade, não resultado necessário ou universal.
- **B)** Incorreta. “Sempre”, “todos” e “eliminam” ampliam indevidamente a afirmação.
- **C)** Incorreta. O enunciado não estabelece essa condição exclusiva.
- **D)** Incorreta. Possibilidade e obrigação têm valores modais diferentes.

**Conceito:** força modal e limites da inferência.

**Pegadinha:** trocar palavra modal por termo absoluto.

**Como pensar:** preserve intensidade, quantificação e escopo do enunciado original.

**Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

### Comentário Extra Dia 1.4

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** hierarquia normativa
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Resolução não revoga lei simplesmente por ser posterior.
- **B)** Incorreta. Decreto regulamenta a lei e deve respeitar seus limites.
- **C)** Correta. Competência e hierarquia condicionam a validade do ato inferior.
- **D)** Incorreta. Cronologia isolada não resolve conflitos entre espécies normativas distintas.

**Conceito:** hierarquia e competência normativa.

**Pegadinha:** usar a data mais recente como critério único.

**Como pensar:** examine espécie, competência, objeto e só então cronologia.

**Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

### Comentário Extra Dia 1.5

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** comentário e edição
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Comentário não substitui automaticamente o texto selecionado.
- **B)** Incorreta. Edição direta altera o conteúdo quando a permissão autoriza.
- **C)** Incorreta. Recuperação de estado anterior é função do histórico de versões.
- **D)** Correta. Comentário sustenta discussão; edição muda o documento.

**Conceito:** funções distintas de colaboração.

**Pegadinha:** tratar recursos de comunicação, edição e versionamento como equivalentes.

**Como pensar:** associe cada recurso ao efeito que produz sobre o conteúdo atual.

**Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

### Comentário Extra Dia 1.6

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** lei e decreto
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Regulamentação não substitui integralmente a fonte legal.
- **B)** Correta. A lei estabelece a base e o decreto detalha a execução dentro dela.
- **C)** Incorreta. Lei e decreto são espécies normativas diferentes de resolução interna.
- **D)** Incorreta. O objeto legal não é edição de documentos colaborativos.

**Conceito:** relação entre lei e decreto regulamentador.

**Pegadinha:** atribuir ao decreto poder autônomo de afastar a lei.

**Como pensar:** leia o decreto como execução subordinada ao marco legal.

**Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

### Comentário Extra Dia 1.7

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** níveis de acesso
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. “Proprietário anônimo” não é o papel intermediário descrito.
- **B)** Incorreta. Leitor normalmente não possui a capacidade de comentar pretendida.
- **C)** Correta. Comentador pode comentar e sugerir sem editar diretamente como editor.
- **D)** Incorreta. “Publicador obrigatório” não é um nível padrão de acesso do recurso.

**Conceito:** papéis de compartilhamento.

**Pegadinha:** supor que toda colaboração exige permissão de editor.

**Como pensar:** aplique menor privilégio ao efeito necessário.

**Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

### Comentário Extra Dia 1.8

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** conectores
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. “Portanto” introduz conclusão decorrente da oração anterior.
- **B)** Incorreta. Condição seria marcada por conectores como “se”.
- **C)** Incorreta. Concessão seria introduzida por “embora”, por exemplo.
- **D)** Incorreta. Finalidade costuma aparecer com “para que” ou expressão equivalente.

**Conceito:** valor lógico dos conectores.

**Pegadinha:** classificar o conector apenas pela posição na frase.

**Como pensar:** substitua-o por outro conector de mesmo valor e teste a relação.

**Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

### Comentário Extra Dia 1.9

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Regimento e Código de Ética
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Inverte ou desfigura os objetos das duas resoluções normativas.
- **B)** Incorreta. Resoluções normativas não se transformam em lei e decreto.
- **C)** Incorreta. Planilha e documento colaborativo não são seus objetos.
- **D)** Correta. Associa a RN nº 651/2024 ao Regimento e a RN nº 671/2025 ao Código de Ética.

**Conceito:** identificação da fonte pelo objeto.

**Pegadinha:** memorizar apenas número e ano sem vincular o conteúdo.

**Como pensar:** forme pares estáveis norma → objeto principal.

**Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

### Comentário Extra Dia 1.10

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** estilos de título
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. Estilos não bloqueiam edições futuras.
- **B)** Incorreta. Formatação não altera permissões de compartilhamento.
- **C)** Correta. Títulos identificam hierarquia e apoiam navegação e uniformidade.
- **D)** Incorreta. Aplicar estilo não elimina comentários resolvidos.

**Conceito:** estrutura semântica em documentos longos.

**Pegadinha:** reduzir estilo a mera aparência visual.

**Como pensar:** compare formatação manual com marcação estrutural reutilizável.

**Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

### Comentário Extra Dia 1.11

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** autonomia do Regional
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Autonomia viabiliza suas atribuições, mas permanece sujeita à lei e ao sistema CFA/CRAs.
- **B)** Incorreta. Conselho regional não possui competência para revogar lei federal.
- **C)** Incorreta. O Regional não se torna órgão da Administração Direta estadual.
- **D)** Incorreta. A orientação nacional continua pertencendo ao CFA em seu âmbito.

**Conceito:** alcance da autonomia regional.

**Pegadinha:** equiparar autonomia administrativa a soberania normativa.

**Como pensar:** autonomia sempre opera dentro de competências e limites jurídicos.

**Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

### Comentário Extra Dia 1.12

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** histórico de versões
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Apagar histórico prejudica a recuperação e a rastreabilidade.
- **B)** Correta. Copiar apenas o trecho recupera o conteúdo desejado sem sobrescrever mudanças posteriores.
- **C)** Incorreta. Edição pública amplia risco e não soluciona recuperação seletiva.
- **D)** Incorreta. Títulos não são mecanismo de restauração de conteúdo.

**Conceito:** recuperação seletiva com histórico de versões.

**Pegadinha:** restaurar uma versão inteira quando só um trecho é necessário.

**Como pensar:** preserve o estado atual e transporte apenas o conteúdo validado.

**Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

### Comentário Extra Dia 1.13

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa e discursiva
- **Assunto:** estrutura da tese
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Discursiva — recorte e tese](semana_03_estudo.md#s3-d1-discursiva-tese).

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. É avaliação genérica sem posição delimitada nem eixos argumentativos.
- **B)** Incorreta. Apenas constata a existência de tecnologia.
- **C)** Correta. Defende uma condição e oferece os eixos qualidade/finalidade e transparência/responsabilização.
- **D)** Incorreta. Generaliza a solução e não apresenta desenvolvimento verificável.

**Conceito:** tese recortada e desenvolvível.

**Pegadinha:** confundir tema amplo com tese argumentativa.

**Como pensar:** procure posição clara, condição e ao menos dois eixos sustentáveis.

**Referência:** [Discursiva — recorte e tese](semana_03_estudo.md#s3-d1-discursiva-tese).

### Comentário Extra Dia 1.14

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** objeto da fonte
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Cada fonte é consultada segundo seu objeto: organização ou conduta ética.
- **B)** Incorreta. Atribui objetos estranhos às duas normas.
- **C)** Incorreta. Atualidade não substitui pertinência temática.
- **D)** Incorreta. Atos normativos do CFA podem disciplinar essas matérias dentro da competência.

**Conceito:** escolha da norma pelo objeto do caso.

**Pegadinha:** eleger a norma mais recente sem verificar o assunto regulado.

**Como pensar:** decomponha o caso e relacione cada questão à fonte correspondente.

**Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

### Comentário Extra Dia 1.15

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** menor privilégio
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Propriedade concede poderes muito superiores à necessidade.
- **B)** Incorreta. Edição anônima cria exposição incompatível com menor privilégio.
- **C)** Incorreta. Remover controles amplia indevidamente o acesso.
- **D)** Correta. A permissão de comentar/sugerir atende à tarefa sem edição integral.

**Conceito:** princípio do menor privilégio em colaboração.

**Pegadinha:** conceder papel de editor por conveniência.

**Como pensar:** escolha a menor permissão que ainda permite cumprir o objetivo.

**Referência:** [Google Documentos — colaboração, sugestões e histórico](semana_03_estudo.md#s3-d1-google-documentos).

### Comentário Extra Dia 1.16

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** competência e território
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Inverte os âmbitos regional e nacional.
- **B)** Correta. O CRA-PR trata o fato em sua jurisdição e o CFA orienta o sistema nacionalmente.
- **C)** Incorreta. Sindicato não substitui o Regional no registro/fiscalização.
- **D)** Incorreta. A jurisdição continua relevante à atuação regional.

**Conceito:** coordenação entre competência territorial e orientação nacional.

**Pegadinha:** imaginar exclusão recíproca entre CFA e CRA-PR.

**Como pensar:** separe execução local do papel uniformizador nacional.

**Referência:** [Legislação CRA/CFA — mapa de fonte e competência](semana_03_estudo.md#s3-d1-revisao-legislacao).

### Comentário Extra Dia 1.17

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** histórico e permissões
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Google Documentos](semana_03_estudo.md#s3-d1-exemplos-google-docs).

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Versionamento existe, mas visualização e restauração respeitam controles de acesso.
- **B)** Incorreta. Leitura não implica poder universal de restauração ou exclusão.
- **C)** Incorreta. Sugestão aceita passa a integrar o conteúdo.
- **D)** Incorreta. Comentário registra discussão; histórico registra estados do arquivo.

**Conceito:** interação entre versionamento e permissões.

**Pegadinha:** reconhecer o recurso e ignorar o requisito de autorização.

**Como pensar:** nenhuma capacidade colaborativa deve ser analisada separada do papel de acesso.

**Referência:** [Exemplos resolvidos — Google Documentos](semana_03_estudo.md#s3-d1-exemplos-google-docs).

### Comentário Extra Dia 1.18

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** comando negativo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

**Alternativa correta: D.**

**Observação:** neste item, a alternativa correta descreve o procedimento adequado para responder a um comando que solicita a opção **INCORRETA**; não se deve inverter o gabarito deste exercício metacognitivo.

**Análise das alternativas:**

- **A)** Incorreta. Familiaridade não substitui análise de verdade e escopo.
- **B)** Incorreta. Uma formulação incompleta pode continuar verdadeira no recorte.
- **C)** Incorreta. Ignorar a polaridade conduz a marcar uma afirmação verdadeira.
- **D)** Correta. O candidato deve testar todas as opções e localizar a única falsa.

**Conceito:** leitura operacional de comando negativo.

**Pegadinha:** confundir a descrição do procedimento com um item negativo comum.

**Como pensar:** circule a polaridade, avalie V/F e só depois converta para a marcação.

**Referência:** [Comando, escopo e palavras absolutas](semana_03_estudo.md#s3-d1-portugues-comando).

### Comentário Extra Dia 1.19

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** cronologia e hierarquia
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_03_estudo.md#s3-d1-exemplos-legislacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Número ou data maior não autoriza contrariar a lei.
- **B)** Correta. Objeto, competência e hierarquia precedem a aplicação do critério cronológico.
- **C)** Incorreta. Norma anterior não perde validade apenas pela idade.
- **D)** Incorreta. Lei e resolução têm natureza e posição distintas.

**Conceito:** solução de aparente conflito normativo.

**Pegadinha:** privilegiar novidade sem controlar hierarquia.

**Como pensar:** verifique se o ato inferior cabe na moldura legal antes de comparar datas.

**Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_03_estudo.md#s3-d1-exemplos-legislacao).

### Comentário Extra Dia 1.20

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Documentos
- **Assunto:** sugestão, comentário e versão
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Google Documentos](semana_03_estudo.md#s3-d1-exemplos-google-docs).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Publicidade irrestrita e exclusão de rastros contrariam os requisitos.
- **B)** Incorreta. O modo leitura não permite propor a alteração no original.
- **C)** Correta. Cada recurso atende, na ordem, proposta, justificativa e recuperação.
- **D)** Incorreta. Comentário não se converte automaticamente em edição definitiva.

**Conceito:** composição de recursos colaborativos.

**Pegadinha:** exigir que um único recurso cumpra três finalidades distintas.

**Como pensar:** associe cada requisito ao recurso específico e valide as permissões.

**Referência:** [Exemplos resolvidos — Google Documentos](semana_03_estudo.md#s3-d1-exemplos-google-docs).


# Dia 2 — Modelo relacional, MER, álgebra e normalização

## Questões principais

### S3D2Q051 — Relação e tabela válida

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

No modelo relacional, uma relação é corretamente compreendida como:

A) um arquivo físico cuja ordem de linhas define a identidade dos registros.
B) um conjunto de tuplas sobre atributos definidos, sem relevância lógica para a ordem de linhas.
C) uma planilha que admite obrigatoriamente células com listas de valores.
D) um diagrama de entidades sem representação de estado.

### S3D2Q052 — Tupla e grau da relação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

Em `PROCESSO(id, assunto, ano)`, uma tupla e o grau da relação correspondem, respectivamente, a:

A) uma coluna e ao número de linhas.
B) um domínio e ao número de chaves.
C) o esquema inteiro e ao número de valores distintos.
D) uma linha válida e a três atributos.

### S3D2Q053 — Atributo e domínio

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

Assinale a associação correta entre atributo e domínio.

A) O atributo nomeia uma propriedade; o domínio delimita os valores admissíveis dessa propriedade.
B) O domínio é sempre o tipo físico escolhido pelo SGBD, sem conteúdo semântico.
C) O atributo é o conjunto de todas as tuplas já armazenadas.
D) Atributo e domínio são sinônimos de chave primária.

### S3D2Q054 — Esquema e estado relacional

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

A inclusão de 80 processos, sem alterar atributos ou restrições, modifica:

A) o esquema e o grau da relação.
B) a chave candidata e o domínio.
C) o estado da relação, mas não seu esquema.
D) a cardinalidade máxima do MER, obrigatoriamente.

### S3D2Q055 — Superchave e chave candidata

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

Qual afirmação diferencia corretamente superchave e chave candidata?

A) Toda superchave é mínima, mas candidata pode conter sobra.
B) Chave candidata é superchave mínima; superchave pode ter redundância.
C) Somente a chave primária identifica tuplas.
D) Chave candidata é sempre composta.

### S3D2Q056 — Escolha da chave primária

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

Uma relação possui duas chaves candidatas. A chave primária é:

A) a candidata escolhida como chave principal.
B) a união obrigatória de todas as candidatas.
C) qualquer chave estrangeira não nula.
D) o atributo com maior tamanho físico.

### S3D2Q057 — Chave composta

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

Em `ITEM_PEDIDO(id_pedido, id_produto, quantidade)`, se o mesmo produto ocorre no máximo uma vez por pedido, a identificação natural do item é:

A) somente `quantidade`.
B) somente `id_produto`, em toda a base.
C) qualquer coluna isolada, pois linhas não precisam ser identificadas.
D) o par `(id_pedido, id_produto)`.

### S3D2Q058 — Integridade de entidade e referencial

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Restrições de integridade](semana_03_estudo.md#s3-d2-restricoes).

Assinale a opção correta.

A) Chave primária admite nulo se houver índice.
B) Entidade veda nulo na PK; referencial valida a FK contra a chave referenciada.
C) Chave estrangeira deve sempre ser única.
D) Integridade referencial exige que toda tabela tenha chave composta.

### S3D2Q059 — Entidade, atributo e relacionamento

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelo Entidade-Relacionamento (MER)](semana_03_estudo.md#s3-d2-mer).

No MER de fiscalização, `FISCAL`, `nome_fiscal` e `atua_em` são, respectivamente:

A) entidade, atributo e relacionamento.
B) atributo, entidade e chave.
C) relacionamento, domínio e entidade fraca.
D) entidade, relacionamento e atributo composto.

### S3D2Q060 — Atributo do relacionamento

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelo Entidade-Relacionamento (MER)](semana_03_estudo.md#s3-d2-mer).

Em PROFISSIONAL participa de PROJETO, `horas_semanais` descreve cada participação. Esse atributo deve ser associado:

A) somente a PROFISSIONAL.
B) somente a PROJETO.
C) ao domínio físico do identificador.
D) ao relacionamento qualificado pelo atributo.

### S3D2Q061 — Cardinalidade máxima

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

Uma unidade pode lotar muitos servidores, e cada servidor está lotado em no máximo uma unidade. Quanto aos máximos, a relação é:

A) N:N.
B) 1:1.
C) 1:N da unidade para servidor.
D) 0:N, que substitui a notação 1:N.

### S3D2Q062 — Participação mínima

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

Se todo servidor deve estar em uma unidade, mas uma unidade pode existir sem servidores, a participação é:

A) parcial nos dois lados.
B) total em SERVIDOR e parcial em UNIDADE.
C) total em UNIDADE e parcial em SERVIDOR.
D) total nos dois lados porque o máximo é N.

### S3D2Q063 — Máximo não implica mínimo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

Assinale a afirmação correta sobre cardinalidade e participação.

A) Relacionamento 1:N obriga participação total do lado N.
B) Máximo N significa mínimo 1.
C) Participação parcial impede máximo N.
D) Máximo e mínimo são distintos; 1:N não impõe participação total.

### S3D2Q064 — Leitura de 0..1

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

A notação `0..1` ao lado de uma entidade indica:

A) participação opcional e no máximo uma ocorrência relacionada.
B) participação obrigatória em exatamente uma ocorrência.
C) participação opcional e obrigatoriamente muitas ocorrências.
D) entidade fraca com chave parcial.

### S3D2Q065 — Entidade fraca

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

Qual conjunto caracteriza uma entidade fraca?

A) Chave global própria, participação parcial e ausência de proprietário.
B) Somente dependência operacional de outro cadastro.
C) chave do proprietário mais chave parcial, com identificação e participação total.
D) Atributo multivalorado e relacionamento N:N.

### S3D2Q066 — Chave parcial

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

`sequencia` identifica DEPENDENTE apenas dentro de cada PROFISSIONAL. Logo, `sequencia` é:

A) chave estrangeira global de PROFISSIONAL.
B) chave parcial, completada pela chave do proprietário.
C) superchave isolada de DEPENDENTE.
D) atributo derivado sem função de identificação.

### S3D2Q067 — Dependência existencial e fraqueza

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

Uma entidade só pode existir enquanto outra existir, mas possui identificador global próprio. É correto concluir que:

A) dependência existencial não basta; a identificação deve depender do proprietário.
B) ela é necessariamente fraca e seu identificador deve ser descartado.
C) toda participação total cria chave parcial.
D) ela deve ser mapeada como atributo multivalorado.

### S3D2Q068 — Grau e atributo do vínculo

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelo Entidade-Relacionamento (MER)](semana_03_estudo.md#s3-d2-mer).

Três tipos de entidade participam de uma associação, e `data_decisao` descreve a ocorrência conjunta. A classificação adequada é:

A) três relações binárias equivalentes em qualquer regra.
B) entidade fraca com chave parcial temporal.
C) relacionamento ternário com atributo próprio, salvo regra diversa.
D) atributo composto de uma única entidade escolhida ao acaso.

### S3D2Q069 — Mapeamento de entidade forte

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

Ao mapear uma entidade forte com atributos simples para o modelo relacional, deve-se:

A) transformar todos os atributos em tabelas independentes.
B) eliminar seu identificador para evitar redundância.
C) guardar todas as propriedades em uma única lista textual.
D) criar relação própria e tornar o identificador sua chave primária.

### S3D2Q070 — Mapeamento de atributo composto

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

Um atributo composto `endereco` precisa ter cidade e CEP consultados e restringidos separadamente. O mapeamento básico é:

A) criar uma linha por caractere.
B) decompor o atributo nos componentes necessários.
C) tratá-lo obrigatoriamente como chave estrangeira.
D) armazenar lista de componentes em uma única célula.

### S3D2Q071 — Mapeamento de multivalorado

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

Vários telefones por profissional, cada qual com tipo e confirmação, devem ser mapeados por:

A) relação própria com a chave do profissional e os dados de cada telefone.
B) colunas `telefone1` a `telefone9`.
C) texto separado por ponto e vírgula.
D) uma chave estrangeira de telefone dentro de um único campo textual.

### S3D2Q072 — Mapeamento de 1:N

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

No relacionamento UNIDADE 1:N SERVIDOR, cada servidor pertence a uma unidade. A regra básica é:

A) levar a chave de UNIDADE para SERVIDOR como FK.
B) levar uma lista de servidores para UNIDADE.
C) criar sempre relação associativa com duas linhas por vínculo.
D) eliminar a chave de UNIDADE.

### S3D2Q073 — Mapeamento de N:N

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

PROFISSIONAL e PROJETO relacionam-se N:N e o vínculo possui `papel`. O mapeamento correto é:

A) incluir um único projeto em PROFISSIONAL.
B) criar relação associativa com as FKs e `papel`.
C) armazenar os profissionais como lista em PROJETO.
D) copiar `papel` para as duas entidades sem representar o vínculo.

### S3D2Q074 — Atributos do vínculo N:N

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos de mapeamento MER-relacional](semana_03_estudo.md#s3-d2-exemplos-mapeamento).

Na associação PARTICIPACAO entre profissional e projeto, `papel` e `horas_semanais` devem:

A) ficar apenas em PROJETO.
B) ser descartados por não serem identificadores.
C) ficar em PROFISSIONAL, mesmo com vários projetos.
D) permanecer na relação associativa que representa cada vínculo.

### S3D2Q075 — Mapeamento de 1:1

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

Em relação 1:1, CARTEIRA participa totalmente e PROFISSIONAL parcialmente. Uma solução coerente é:

A) FK obrigatória e UNIQUE de profissional em CARTEIRA.
B) FK não única em CARTEIRA, permitindo várias por profissional.
C) lista de carteiras em PROFISSIONAL.
D) relação sem qualquer chave ou restrição.

### S3D2Q076 — Mapeamento de entidade fraca

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

DOCUMENTO é identificado por `numero` apenas dentro de PROCESSO. Sua chave relacional deve conter:

A) somente `numero`, que passa a ser global.
B) somente a chave do processo.
C) a chave do processo combinada à chave parcial `numero`.
D) um texto com todos os números do processo.

### S3D2Q077 — Lista em célula no N:N

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

Guardar vários `id_projeto` em uma única célula de PROFISSIONAL é inadequado porque:

A) aumenta o número de relações do esquema.
B) torna toda FK uma chave primária.
C) converte automaticamente N:N em 1:1.
D) prejudica atomicidade, consultas e integridade.

### S3D2Q078 — Vínculos repetidos no tempo

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos de mapeamento MER-relacional](semana_03_estudo.md#s3-d2-exemplos-mapeamento).

Se o mesmo profissional pode entrar várias vezes no mesmo projeto em períodos distintos, a chave de PARTICIPACAO deve:

A) permanecer sempre apenas `id_profissional`.
B) incluir atributo que distinga cada período.
C) ser substituída por `horas_semanais`.
D) eliminar as FKs dos participantes.

### S3D2Q079 — Seleção

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

Na álgebra relacional, a seleção (`σ`) produz:

A) as tuplas que atendem ao predicado, com os mesmos atributos.
B) somente os atributos nomeados, sem filtrar tuplas.
C) a união automática de duas relações.
D) renomeação de todos os campos.

### S3D2Q080 — Projeção

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

A projeção (`π`) é usada para:

A) ordenar fisicamente as tuplas.
B) selecionar tuplas por condição.
C) escolher atributos sem duplicatas.
D) somar valores numéricos.

### S3D2Q081 — Compatibilidade para união

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

Para aplicar união entre duas relações, é necessário que elas:

A) possuam a mesma quantidade de tuplas.
B) tenham mesmo grau e domínios correspondentes.
C) tenham nomes físicos de tabela idênticos.
D) estejam ligadas por chave estrangeira.

### S3D2Q082 — Diferença relacional

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

A expressão `R − S`, quando válida, retorna:

A) todas as combinações de R com S.
B) os atributos comuns de R e S.
C) a subtração aritmética célula a célula.
D) tuplas de R ausentes em S, se compatíveis.

### S3D2Q083 — Junção

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

A junção entre duas relações pode ser entendida conceitualmente como:

A) projeção seguida de união.
B) diferença seguida de renomeação.
C) seleção sobre produto cartesiano.
D) ordenação física de duas tabelas.

### S3D2Q084 — Produto cartesiano

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

Se R possui 3 tuplas e S possui 4, sem considerar filtros, `R × S` possui:

A) 12 combinações de tuplas.
B) 7 tuplas.
C) 4 tuplas, pois S é maior.
D) uma tupla por atributo comum.

### S3D2Q085 — Ativos do Paraná

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Exemplos de álgebra relacional](semana_03_estudo.md#s3-d2-exemplos-algebra).

Para obter somente nomes de profissionais ativos do Paraná, a expressão conceitual adequada é:

A) selecionar `nome` antes de testar `uf` e `situacao`.
B) unir PROFISSIONAL consigo mesma.
C) aplicar diferença entre nome e UF.
D) selecionar UF/situação e depois projetar `nome`.

### S3D2Q086 — Profissionais sem anuidade

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Exemplos de álgebra relacional](semana_03_estudo.md#s3-d2-exemplos-algebra).

Para obter IDs de profissionais sem anuidade de 2026, deve-se:

A) usar produto cartesiano sem condição.
B) `π_id(PROFISSIONAL) − π_id(ANUIDADE_2026)`.
C) subtrair numericamente o ano de cada ID.
D) projetar apenas `ano` de PROFISSIONAL.

### S3D2Q087 — Dependência funcional não é coincidência

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Dependências funcionais e anomalias](semana_03_estudo.md#s3-d2-dependencias).

Em uma amostra atual, cada `cidade` aparece com um único `fiscal`, mas a regra permite fiscais diferentes na mesma cidade. Pode-se afirmar `cidade → fiscal`?

A) Sim, porque o estado atual basta para provar qualquer dependência.
B) Sim, desde que a tabela esteja em 1FN.
C) Não; a dependência deve valer para todos os estados admissíveis.
D) Não, porque nenhuma dependência pode usar atributo textual.

### S3D2Q088 — Primeira Forma Normal

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Primeira Forma Normal — 1FN](semana_03_estudo.md#s3-d2-1fn).

`telefones` guarda uma coleção separada por ponto e vírgula, e cada telefone tem tipo próprio. A correção alinhada à 1FN é:

A) criar relação TELEFONE ligada a PROFISSIONAL.
B) aumentar o tamanho do campo.
C) trocar ponto e vírgula por vírgula.
D) criar `telefone1`, `telefone2` e `telefone3`.

### S3D2Q089 — Dependência parcial e 2FN

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos de Segunda Forma Normal (2FN)](semana_03_estudo.md#s3-d2-exemplos-2fn).

Em MATRICULA, chave `(id_aluno,id_disciplina)`, vale `id_aluno → nome_aluno`. Essa dependência é:

A) transitiva em relação à chave simples.
B) parcial em parte da chave, violando a 2FN.
C) irrelevante porque nome é texto.
D) completa do par inteiro por definição.

### S3D2Q090 — Chave simples e Segunda Forma Normal

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Segunda Forma Normal — 2FN](semana_03_estudo.md#s3-d2-2fn).

Se uma relação está em 1FN e todas as suas chaves candidatas são simples, então:

A) ela está necessariamente em BCNF.
B) atende à 2FN nesse ponto, sem garantir a 3FN.
C) nenhuma dependência funcional pode existir.
D) ela está necessariamente em 3FN.

### S3D2Q091 — Dependência transitiva e 3FN

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplos de Terceira Forma Normal (3FN)](semana_03_estudo.md#s3-d2-exemplos-3fn).

Em SERVIDOR, `id_servidor → id_unidade` e `id_unidade → nome_unidade`. A solução típica é:

A) separar UNIDADE e manter `id_unidade` como referência em SERVIDOR.
B) remover `id_unidade` e juntar por nome.
C) mover `nome_unidade` para a chave primária de SERVIDOR.
D) repetir o nome mais vezes para reforçar a dependência.

### S3D2Q092 — Definição formal de 3FN

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Terceira Forma Normal — 3FN](semana_03_estudo.md#s3-d2-3fn).

Para toda DF não trivial `X → A`, uma relação está em 3FN quando:

A) X e A são obrigatoriamente não primos.
B) A é sempre chave estrangeira.
C) X é superchave ou A é atributo primo.
D) X possui somente um atributo.

### S3D2Q093 — 3FN versus BCNF

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Exemplos de Forma Normal de Boyce-Codd (BCNF)](semana_03_estudo.md#s3-d2-exemplos-bcnf).

Em ENSINO, vale `professor → disciplina`; professor não é superchave, mas disciplina é atributo primo. A conclusão coerente é:

A) viola 3FN e satisfaz BCNF.
B) satisfaz BCNF porque o lado direito é primo.
C) não pode possuir chaves candidatas sobrepostas.
D) pode cumprir 3FN pela exceção do primo e violar BCNF.

### S3D2Q094 — Determinante na BCNF

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Forma Normal de Boyce–Codd — BCNF](semana_03_estudo.md#s3-d2-bcnf).

A condição central da BCNF para toda dependência funcional não trivial é:

A) o dependente ser atributo textual.
B) o determinante ser superchave.
C) a relação possuir uma única chave candidata.
D) toda chave ser simples.

### S3D2Q095 — Anomalia de exclusão

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dependências funcionais e anomalias](semana_03_estudo.md#s3-d2-dependencias).

Uma tabela mistura curso e matrícula; ao excluir a última matrícula, perde-se também a única descrição do curso. Trata-se de:

A) anomalia de inserção.
B) independência lógica.
C) anomalia de exclusão.
D) projeção com duplicatas.

### S3D2Q096 — Junção sem perda

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Decomposição sem perda e preservação de dependências](semana_03_estudo.md#s3-d2-decomposicao).

Uma decomposição é considerada sem perda quando:

A) reduz obrigatoriamente o número de atributos.
B) elimina toda chave estrangeira.
C) cada parte possui o mesmo número de linhas.
D) permitem reconstrução sem gerar tuplas espúrias.

### S3D2Q097 — Decomposição que cria tuplas espúrias

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Exemplos de decomposição relacional](semana_03_estudo.md#s3-d2-exemplos-decomposicao).

PARTICIPACAO(profissional, projeto, papel) é dividida em PROF_PAPEL e PROJ_PAPEL e reunida apenas por `papel`, que se repete. O risco é:

A) combinar profissionais e projetos nunca associados.
B) violar 1FN por existir uma chave.
C) eliminar automaticamente todos os papéis.
D) transformar seleção em projeção.

### S3D2Q098 — Preservação de dependências

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Decomposição sem perda e preservação de dependências](semana_03_estudo.md#s3-d2-decomposicao).

Preservar dependências em uma decomposição significa, de modo geral:

A) manter todos os atributos na mesma relação.
B) verificar dependências nas partes sem recompor a relação.
C) aceitar qualquer divisão que reduza texto repetido.
D) dispensar chaves de ligação.

### S3D2Q099 — Normalização do cadastro misto

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Prática de banco de dados](semana_03_estudo.md#s3-d2-pratica).

Um cadastro repete `nome_profissional` em cada processo, e `id_profissional → nome_profissional`. A decomposição coerente é:

A) manter tudo e apenas criar índice no nome.
B) remover `id_profissional` de PROCESSO.
C) usar o nome como lista de processos.
D) separar PROFISSIONAL e referenciá-lo em PROCESSO.

### S3D2Q100 — Síntese relacional do caso de fiscalização

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Prática de banco de dados](semana_03_estudo.md#s3-d2-pratica).

No caso integrado, FISCAIS atuam em PROCESSOS N:N com `papel` e `data_inicio`, e DOCUMENTO é numerado dentro do processo. A modelagem coerente é:

A) FK única de processo em FISCAL e documento identificado só por número global.
B) listas de fiscais e documentos dentro de PROCESSO.
C) ATUACAO associativa com atributos do vínculo e DOCUMENTO com chave `(id_processo,numero_documento)`.
D) copiar nomes de fiscal para todos os processos e descartar identificadores.

## Questões extras de revisão fixa do Dia 2

#### Extra Dia 2.1

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** princípio da legalidade
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

Na Administração Pública, legalidade significa que o agente:

A) pode afastar a lei sempre que alegar eficiência.
B) atua somente conforme preferências pessoais não proibidas.
C) deve atuar vinculado ao ordenamento e às competências estabelecidas.
D) substitui requisito legal por costume administrativo.

#### Extra Dia 2.2

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** referência absoluta
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

Ao copiar `=B2*$F$1` para baixo, qual referência permanece integralmente fixa?

A) `$F$1`.
B) `B2`.
C) as duas referências.
D) nenhuma referência.

#### Extra Dia 2.3

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** consequência
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

Em “os critérios eram incompatíveis; por isso, o indicador falhou”, `por isso` expressa:

A) causa anterior à primeira oração.
B) concessão.
C) condição.
D) consequência ou conclusão.

#### Extra Dia 2.4

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Direta e Indireta
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

Assinale a distinção correta.

A) Órgão e entidade possuem sempre personalidade própria.
B) órgão é centro sem personalidade; entidade é pessoa jurídica.
C) Administração Indireta é formada somente por ministérios.
D) Autarquia integra a Administração Direta.

#### Extra Dia 2.5

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** filtrar e excluir
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

Aplicar filtro a uma tabela:

A) oculta linhas fora do critério sem as excluir.
B) apaga definitivamente as linhas não exibidas.
C) muda os valores das células ocultas.
D) transforma referências relativas em absolutas.

#### Extra Dia 2.6

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** referência pronominal
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

Para haver coesão referencial, um pronome deve:

A) apontar sempre para a palavra mais próxima.
B) ser eliminado de todo texto técnico.
C) ter referente recuperável sem ambiguidade indevida.
D) introduzir obrigatoriamente uma causa.

#### Extra Dia 2.7

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** publicidade e impessoalidade
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Exemplos de Administração Pública e CRM](semana_03_estudo.md#s3-d2-exemplos-adm).

Campanha informa serviço, mas centra nome e imagem do dirigente. É correto afirmar:

A) publicidade torna lícita qualquer promoção pessoal.
B) pode violar a impessoalidade apesar do caráter informativo.
C) eficiência elimina os demais princípios.
D) a promoção é obrigatória para identificar o órgão.

#### Extra Dia 2.8

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** visualização de filtro
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

Para cada colaborador analisar um recorte próprio sem impor a mesma visão a todos, é adequado usar:

A) exclusão das linhas.
B) ordenação de uma coluna isolada.
C) publicação de cópia sem controle.
D) visualização de filtro.

#### Extra Dia 2.9

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** conector condicional
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

Qual conector introduz condição?

A) Portanto.
B) Embora.
C) Caso.
D) Contudo.

#### Extra Dia 2.10

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** revogação
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

Revogação é, em regra, a retirada:

A) judicial de qualquer ato por conveniência.
B) administrativa de ato válido por conveniência e oportunidade, quando cabível.
C) de ato ilegal por vício insanável, chamada sempre de mérito.
D) automática de lei por resolução.

#### Extra Dia 2.11

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** COUNTIF
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

Para contar células de um intervalo que atendem a um critério, utiliza-se conceitualmente:

A) SUM.
B) AVERAGE.
C) IF sem teste.
D) COUNTIF.

#### Extra Dia 2.12

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa e discursiva
- **Assunto:** desenvolvimento argumentativo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Desenvolvimento da resposta discursiva](semana_03_estudo.md#s3-d2-discursiva-desenvolvimento).

Qual sequência organiza um parágrafo de desenvolvimento coerente?

A) tópico frasal, explicação, exemplo e consequência ligada à tese.
B) lista de tecnologias, nova tese e pergunta retórica.
C) exemplo isolado, título e bibliografia.
D) quatro definições sem relação causal.

#### Extra Dia 2.13

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** convalidação
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

Convalidação:

A) corrige toda ilegalidade, inclusive vício insanável.
B) corrige vício sanável quando presentes os requisitos legais.
C) é sinônimo de revogação por mérito.
D) é atribuição exclusiva do Poder Judiciário.

#### Extra Dia 2.14

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** ordenação segura
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Exemplos de Google Planilhas](semana_03_estudo.md#s3-d2-exemplos-sheets).

Ao ordenar tabela cujas colunas formam registros lógicos, deve-se:

A) ordenar somente a coluna de nomes, independentemente das demais.
B) converter tudo em texto antes.
C) apagar cabeçalhos e filtros.
D) ordenar o intervalo completo para manter os valores da mesma linha associados.

#### Extra Dia 2.15

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concessão
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

Em “Embora os dados existam, os critérios divergem”, `embora` introduz:

A) causa.
B) finalidade.
C) concessão.
D) conclusão.

#### Extra Dia 2.16

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** natureza do CRA-PR
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

Conforme o material, o CRA-PR é apresentado como:

A) autarquia de direito público integrante da Administração Indireta.
B) órgão sem personalidade da Administração Direta estadual.
C) entidade soberana sem sujeição legal.
D) sociedade privada substituta do CFA.

#### Extra Dia 2.17

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** função IF
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

A função IF é usada para:

A) somar um intervalo sem condição.
B) ordenar fisicamente uma planilha.
C) fixar linha e coluna de uma referência.
D) retornar um valor conforme um teste.

#### Extra Dia 2.18

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** ambiguidade referencial
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

Em “O fiscal avisou o gerente que seu relatório falhara”, o problema potencial é:

A) ausência de verbo.
B) uso obrigatório de concessão.
C) ambiguidade no referente de `seu`.
D) falta de relação matemática.

#### Extra Dia 2.19

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** anulação por ilegalidade
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos de Administração Pública e CRM](semana_03_estudo.md#s3-d2-exemplos-adm).

Ato praticado fora de competência legal exclusiva apresenta vício indicado como insanável no caso. A providência compatível é:

A) anulação por ilegalidade.
B) revogação por mera inconveniência.
C) convalidação automática.
D) manutenção obrigatória por presunção absoluta.

#### Extra Dia 2.20

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** referências mistas
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

Ao copiar fórmulas, qual descrição está correta?

A) `$B$2` deixa linha e coluna variarem.
B) `$B2` fixa a coluna e permite variar a linha.
C) `B$2` fixa a coluna e libera a linha.
D) `B2` permanece sempre integralmente fixo.

## Gabarito do Dia 2

### Questões principais

| ID | Resposta |
|---|:---:|
| S3D2Q051 | B |
| S3D2Q052 | D |
| S3D2Q053 | A |
| S3D2Q054 | C |
| S3D2Q055 | B |
| S3D2Q056 | A |
| S3D2Q057 | D |
| S3D2Q058 | B |
| S3D2Q059 | A |
| S3D2Q060 | D |
| S3D2Q061 | C |
| S3D2Q062 | B |
| S3D2Q063 | D |
| S3D2Q064 | A |
| S3D2Q065 | C |
| S3D2Q066 | B |
| S3D2Q067 | A |
| S3D2Q068 | C |
| S3D2Q069 | D |
| S3D2Q070 | B |
| S3D2Q071 | A |
| S3D2Q072 | A |
| S3D2Q073 | B |
| S3D2Q074 | D |
| S3D2Q075 | A |
| S3D2Q076 | C |
| S3D2Q077 | D |
| S3D2Q078 | B |
| S3D2Q079 | A |
| S3D2Q080 | C |
| S3D2Q081 | B |
| S3D2Q082 | D |
| S3D2Q083 | C |
| S3D2Q084 | A |
| S3D2Q085 | D |
| S3D2Q086 | B |
| S3D2Q087 | C |
| S3D2Q088 | A |
| S3D2Q089 | B |
| S3D2Q090 | B |
| S3D2Q091 | A |
| S3D2Q092 | C |
| S3D2Q093 | D |
| S3D2Q094 | B |
| S3D2Q095 | C |
| S3D2Q096 | D |
| S3D2Q097 | A |
| S3D2Q098 | B |
| S3D2Q099 | D |
| S3D2Q100 | C |

### Questões extras

| Extra | Resposta |
|---:|:---:|
| 2.1 | C |
| 2.2 | A |
| 2.3 | D |
| 2.4 | B |
| 2.5 | A |
| 2.6 | C |
| 2.7 | B |
| 2.8 | D |
| 2.9 | C |
| 2.10 | B |
| 2.11 | D |
| 2.12 | A |
| 2.13 | B |
| 2.14 | D |
| 2.15 | C |
| 2.16 | A |
| 2.17 | D |
| 2.18 | C |
| 2.19 | A |
| 2.20 | B |

## Comentários do Dia 2
### Comentário S3D2Q051

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Ordem física não compõe a definição lógica de relação.
- **B)** Correta. Relação é conjunto de tuplas definido por atributos.
- **C)** Incorreta. Listas multivaloradas não são requisito relacional.
- **D)** Incorreta. MER é modelo conceitual, não definição de relação.

**Conceito:** relação no modelo relacional.

**Pegadinha:** confundir tabela lógica com arquivo físico.

**Como pensar:** ignore ordem de exibição e identifique tuplas e atributos.

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

### Comentário S3D2Q052

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Tupla é linha, não coluna; grau não conta linhas.
- **B)** Incorreta. Domínio e número de chaves não formam o par pedido.
- **C)** Incorreta. Esquema não é ocorrência individual.
- **D)** Correta. Cada linha é tupla e o esquema possui três atributos.

**Conceito:** tupla e grau.

**Pegadinha:** trocar grau por cardinalidade da relação.

**Como pensar:** conte atributos para o grau e linhas para a cardinalidade.

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

### Comentário S3D2Q053

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Atributo nomeia a propriedade e domínio restringe valores válidos.
- **B)** Incorreta. Domínio possui dimensão semântica e não se reduz ao tipo físico.
- **C)** Incorreta. Conjunto de tuplas é o estado da relação.
- **D)** Incorreta. Nem todo atributo ou domínio é chave.

**Conceito:** atributo e domínio.

**Pegadinha:** igualar domínio semântico a tipo físico.

**Como pensar:** pergunte qual propriedade é descrita e quais valores ela admite.

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

### Comentário S3D2Q054

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Atributos e restrições não mudaram.
- **B)** Incorreta. A inclusão não altera candidatas nem domínio.
- **C)** Correta. Novas tuplas mudam o estado, preservando o esquema.
- **D)** Incorreta. Cardinalidade do MER é regra, não contagem corrente.

**Conceito:** esquema versus estado.

**Pegadinha:** confundir cardinalidade corrente com cardinalidade do MER.

**Como pensar:** classifique inclusão de linhas como mudança de estado.

**Referência:** [Modelo relacional](semana_03_estudo.md#s3-d2-modelo-relacional).

### Comentário S3D2Q055

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. A definição está invertida: superchave pode ter sobra.
- **B)** Correta. Candidata identifica minimamente; superchave pode ser não mínima.
- **C)** Incorreta. Outras chaves candidatas também identificam tuplas.
- **D)** Incorreta. Chave candidata pode ser simples ou composta.

**Conceito:** superchave e chave candidata.

**Pegadinha:** tratar toda superchave como mínima.

**Como pensar:** teste identificação e depois remova atributos para verificar minimalidade.

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

### Comentário S3D2Q056

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. A primária é uma candidata escolhida; as demais continuam alternativas.
- **B)** Incorreta. Unir candidatas costuma criar superchave com sobra.
- **C)** Incorreta. Chave estrangeira tem função referencial.
- **D)** Incorreta. Tamanho físico não define primazia lógica.

**Conceito:** chave primária.

**Pegadinha:** pensar que candidatas não escolhidas deixam de identificar.

**Como pensar:** separe existência de candidatas da escolha administrativa da primária.

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

### Comentário S3D2Q057

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Quantidade não identifica o item.
- **B)** Incorreta. Produto pode reaparecer em pedidos diferentes.
- **C)** Incorreta. Tuplas precisam de identificação coerente.
- **D)** Correta. O par distingue o produto dentro de cada pedido.

**Conceito:** chave composta.

**Pegadinha:** usar apenas uma parte da identificação contextual.

**Como pensar:** procure quais atributos juntos tornam o vínculo único.

**Referência:** [Superchaves, chaves candidatas e chave primária](semana_03_estudo.md#s3-d2-chaves).

### Comentário S3D2Q058

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Índice não autoriza nulo na chave primária.
- **B)** Correta. A opção distingue corretamente entidade e referência.
- **C)** Incorreta. FK não é necessariamente única; em 1:N ela se repete.
- **D)** Incorreta. Integridade referencial não exige chave composta.

**Conceito:** integridade de entidade e referencial.

**Pegadinha:** atribuir unicidade obrigatória a toda FK.

**Como pensar:** verifique separadamente identidade da própria linha e validade da referência.

**Referência:** [Restrições de integridade](semana_03_estudo.md#s3-d2-restricoes).

### Comentário S3D2Q059

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. FISCAL é objeto, nome é propriedade e atua_em é associação.
- **B)** Incorreta. A ordem das categorias foi trocada.
- **C)** Incorreta. Relacionamento não é entidade e nome não é domínio neste enunciado.
- **D)** Incorreta. atua_em representa associação, não atributo.

**Conceito:** elementos do MER.

**Pegadinha:** classificar pelo formato da palavra em vez de sua função.

**Como pensar:** pergunte quem existe, o que o descreve e como se associa.

**Referência:** [Modelo Entidade-Relacionamento (MER)](semana_03_estudo.md#s3-d2-mer).

### Comentário S3D2Q060

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Horas variam por participação, não apenas por profissional.
- **B)** Incorreta. O mesmo projeto recebe participações com horas distintas.
- **C)** Incorreta. Identificador físico não descreve carga do vínculo.
- **D)** Correta. O valor caracteriza cada par profissional–projeto.

**Conceito:** atributo de relacionamento.

**Pegadinha:** colocar atributo do vínculo em um participante.

**Como pensar:** teste se o valor muda quando muda somente o par relacionado.

**Referência:** [Modelo Entidade-Relacionamento (MER)](semana_03_estudo.md#s3-d2-mer).

### Comentário S3D2Q061

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Uma unidade pode relacionar-se a muitos servidores.
- **B)** Incorreta. Cada servidor tem no máximo uma unidade, logo não é 1:1.
- **C)** Correta. Os máximos formam 1:N da unidade para servidor.
- **D)** Incorreta. 0:N mistura mínimo com a classificação dos máximos.

**Conceito:** cardinalidade máxima.

**Pegadinha:** usar mínimo zero para renomear 1:N.

**Como pensar:** considere primeiro apenas o maior número possível de cada lado.

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

### Comentário S3D2Q062

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Servidor não pode ficar sem unidade.
- **B)** Correta. O mínimo é 1 para servidor e 0 para unidade.
- **C)** Incorreta. A associação está invertida.
- **D)** Incorreta. Máximo N não obriga mínimo 1.

**Conceito:** participação mínima.

**Pegadinha:** deduzir obrigatoriedade a partir do máximo.

**Como pensar:** traduza “deve” como mínimo 1 e “pode existir sem” como mínimo 0.

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

### Comentário S3D2Q063

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. 1:N informa máximos, não mínimos.
- **B)** Incorreta. Máximo N admite mínimo 0 ou 1.
- **C)** Incorreta. Participação parcial é compatível com máximo N.
- **D)** Correta. Máximo e participação são dimensões independentes.

**Conceito:** máximo versus participação.

**Pegadinha:** supor que muitos implica ao menos um.

**Como pensar:** anote mínimo e máximo separadamente.

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

### Comentário S3D2Q064

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Zero permite ausência e um limita o máximo.
- **B)** Incorreta. Obrigatoriedade seria 1..1.
- **C)** Incorreta. 0..1 não permite muitas ocorrências.
- **D)** Incorreta. A notação não define fraqueza.

**Conceito:** leitura min–máx.

**Pegadinha:** ler somente o número máximo.

**Como pensar:** verbalize cada limite: zero ou uma ocorrência.

**Referência:** [Cardinalidade e participação](semana_03_estudo.md#s3-d2-cardinalidade-participacao).

### Comentário S3D2Q065

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. Entidade fraca não possui identificação global completa própria.
- **B)** Incorreta. Dependência operacional isolada é insuficiente.
- **C)** Correta. Proprietário, chave parcial, vínculo identificador e totalidade formam o conjunto.
- **D)** Incorreta. Multivalorado e N:N não caracterizam fraqueza.

**Conceito:** entidade fraca.

**Pegadinha:** usar qualquer dependência como prova de fraqueza.

**Como pensar:** verifique de onde vem a identidade completa da ocorrência.

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

### Comentário S3D2Q066

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A sequência não referencia globalmente PROFISSIONAL.
- **B)** Correta. Ela distingue dependentes dentro do proprietário.
- **C)** Incorreta. Sozinha, a sequência se repete entre profissionais.
- **D)** Incorreta. A sequência participa diretamente da identificação.

**Conceito:** chave parcial.

**Pegadinha:** elevar identificador local a chave global.

**Como pensar:** combine a chave parcial com a chave do proprietário.

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

### Comentário S3D2Q067

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Fraqueza exige identificação dependente, não apenas existência dependente.
- **B)** Incorreta. Identificador global próprio afasta a conclusão automática.
- **C)** Incorreta. Participação total não cria chave parcial por si.
- **D)** Incorreta. Dependência não transforma entidade em atributo multivalorado.

**Conceito:** fraqueza versus dependência comum.

**Pegadinha:** confundir dependência existencial com identificação dependente.

**Como pensar:** procure se a chave do proprietário é necessária para identificar.

**Referência:** [Entidade fraca](semana_03_estudo.md#s3-d2-entidade-fraca).

### Comentário S3D2Q068

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. Decomposição binária pode perder a semântica ternária.
- **B)** Incorreta. Chave parcial não decorre de atributo temporal.
- **C)** Correta. Três participantes definem grau ternário e a data descreve o vínculo.
- **D)** Incorreta. Escolher uma entidade isolada perde a ocorrência conjunta.

**Conceito:** grau e atributo de relacionamento.

**Pegadinha:** decompor ternário automaticamente em binários.

**Como pensar:** identifique quantos tipos participam simultaneamente e o que o atributo descreve.

**Referência:** [Modelo Entidade-Relacionamento (MER)](semana_03_estudo.md#s3-d2-mer).

### Comentário S3D2Q069

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Atributos simples não exigem relações independentes.
- **B)** Incorreta. Eliminar identificador destrói a chave.
- **C)** Incorreta. Lista textual viola a estrutura relacional pretendida.
- **D)** Correta. Entidade forte vira relação e preserva seu identificador.

**Conceito:** mapeamento de entidade forte.

**Pegadinha:** fragmentar cada atributo sem necessidade.

**Como pensar:** crie a relação e mantenha o identificador como chave.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q070

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Caracteres não são as unidades semânticas desejadas.
- **B)** Correta. Cidade e CEP tornam-se componentes consultáveis.
- **C)** Incorreta. Atributo composto não é automaticamente FK.
- **D)** Incorreta. Lista única impede regras independentes.

**Conceito:** atributo composto.

**Pegadinha:** confundir decomposição semântica com divisão arbitrária.

**Como pensar:** decomponha nos componentes que possuem uso e regra próprios.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q071

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Uma relação própria representa cada telefone e suas propriedades.
- **B)** Incorreta. Colunas numeradas criam grupo repetitivo e limite artificial.
- **C)** Incorreta. Texto separado oculta ocorrências independentes.
- **D)** Incorreta. Uma célula não implementa referências individuais adequadamente.

**Conceito:** atributo multivalorado.

**Pegadinha:** trocar o separador e manter a coleção na célula.

**Como pensar:** modele cada ocorrência como tupla ligada ao proprietário.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q072

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A FK no lado N permite muitos servidores referirem a mesma unidade.
- **B)** Incorreta. Lista no lado 1 contraria atomicidade.
- **C)** Incorreta. Relação associativa é regra típica de N:N, não obrigatória aqui.
- **D)** Incorreta. A chave de unidade deve ser preservada.

**Conceito:** mapeamento 1:N.

**Pegadinha:** levar o lado N como lista para o lado 1.

**Como pensar:** coloque a chave do lado 1 em cada ocorrência do lado N.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q073

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Um único projeto limitaria indevidamente o N:N.
- **B)** Correta. A associativa preserva participantes e atributo do vínculo.
- **C)** Incorreta. Lista em célula prejudica integridade.
- **D)** Incorreta. Copiar papel não identifica a participação.

**Conceito:** mapeamento N:N.

**Pegadinha:** tentar resolver N:N com uma única FK.

**Como pensar:** transforme cada vínculo em tupla da relação associativa.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q074

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Papel e horas não descrevem o projeto isolado.
- **B)** Incorreta. Atributos não chave continuam necessários.
- **C)** Incorreta. Um profissional pode ter valores diferentes em cada projeto.
- **D)** Correta. A associativa é o local do fato sobre o par.

**Conceito:** atributos do vínculo N:N.

**Pegadinha:** mover atributo do relacionamento para uma entidade.

**Como pensar:** pergunte qual ocorrência determina o valor.

**Referência:** [Exemplos de mapeamento MER-relacional](semana_03_estudo.md#s3-d2-exemplos-mapeamento).

### Comentário S3D2Q075

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Obrigatoriedade preserva participação total e UNIQUE preserva máximo um.
- **B)** Incorreta. Sem UNIQUE, vários registros poderiam apontar para o mesmo profissional.
- **C)** Incorreta. Lista não é necessária para 1:1.
- **D)** Incorreta. Sem restrições, a cardinalidade não é garantida.

**Conceito:** mapeamento 1:1.

**Pegadinha:** esquecer a unicidade e implementar 1:N.

**Como pensar:** combine posição da FK, nulabilidade e unicidade.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q076

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Número isolado pode repetir em processos diferentes.
- **B)** Incorreta. Só a chave do processo não distingue seus documentos.
- **C)** Correta. O par proprietário–chave parcial completa a identificação.
- **D)** Incorreta. Lista textual não cria chave relacional.

**Conceito:** mapeamento de entidade fraca.

**Pegadinha:** usar a chave parcial como identificador global.

**Como pensar:** reproduza no relacional a identificação dependente do MER.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q077

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. A solução reduz, não aumenta, a representação relacional.
- **B)** Incorreta. FK e chave primária possuem funções distintas.
- **C)** Incorreta. Lista não altera corretamente a cardinalidade.
- **D)** Correta. Coleção em célula impede referências e operações por ocorrência.

**Conceito:** listas em células.

**Pegadinha:** aceitar texto delimitado como atalho para N:N.

**Como pensar:** exija uma tupla por vínculo e FKs verificáveis.

**Referência:** [Mapeamento MER-relacional](semana_03_estudo.md#s3-d2-mapeamento).

### Comentário S3D2Q078

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Um profissional participa de muitos vínculos.
- **B)** Correta. O atributo temporal diferencia ocorrências do mesmo par.
- **C)** Incorreta. Horas não identificam necessariamente uma ocorrência.
- **D)** Incorreta. As FKs continuam necessárias para representar os participantes.

**Conceito:** chave de relação associativa temporal.

**Pegadinha:** fixar sempre a chave no par de FKs.

**Como pensar:** confirme se o mesmo par pode reaparecer e acrescente o discriminador.

**Referência:** [Exemplos de mapeamento MER-relacional](semana_03_estudo.md#s3-d2-exemplos-mapeamento).

### Comentário S3D2Q079

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Seleção filtra tuplas pelo predicado.
- **B)** Incorreta. Escolha de atributos é projeção.
- **C)** Incorreta. União é operação binária diferente.
- **D)** Incorreta. Renomeação usa outra operação.

**Conceito:** seleção relacional.

**Pegadinha:** trocar linhas por colunas.

**Como pensar:** associe seleção a filtro de tuplas.

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

### Comentário S3D2Q080

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. Projeção não ordena fisicamente.
- **B)** Incorreta. Filtro por condição é seleção.
- **C)** Correta. Projeção escolhe atributos e o resultado relacional não mantém duplicatas.
- **D)** Incorreta. Soma não é operação de projeção.

**Conceito:** projeção relacional.

**Pegadinha:** transportar a semântica de SELECT SQL sem DISTINCT automaticamente.

**Como pensar:** pense no resultado como conjunto relacional de atributos escolhidos.

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

### Comentário S3D2Q081

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Quantidade de tuplas pode ser diferente.
- **B)** Correta. União exige esquemas correspondentes compatíveis.
- **C)** Incorreta. Nomes físicos das relações não precisam coincidir.
- **D)** Incorreta. FK não é requisito para união.

**Conceito:** compatibilidade de união.

**Pegadinha:** confundir união com junção por chave.

**Como pensar:** compare grau e domínios correspondentes dos operandos.

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

### Comentário S3D2Q082

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Todas as combinações definem produto cartesiano.
- **B)** Incorreta. Atributos comuns não são o resultado da diferença.
- **C)** Incorreta. Diferença é conjuntista, não aritmética.
- **D)** Correta. Mantêm-se tuplas do primeiro conjunto ausentes no segundo.

**Conceito:** diferença relacional.

**Pegadinha:** interpretar o símbolo como subtração numérica.

**Como pensar:** compatibilize os operandos e leia a ordem R menos S.

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

### Comentário S3D2Q083

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. Projeção e união não expressam correspondência entre tuplas.
- **B)** Incorreta. Diferença e renomeação não combinam participantes.
- **C)** Correta. Junção restringe o produto pela condição de ligação.
- **D)** Incorreta. Ordenação física não define junção.

**Conceito:** junção relacional.

**Pegadinha:** confundir junção com união.

**Como pensar:** imagine produto cartesiano e elimine pares que não satisfazem a condição.

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

### Comentário S3D2Q084

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Cada uma das 3 tuplas combina com as 4, totalizando 12.
- **B)** Incorreta. Somar cardinalidades não calcula produto.
- **C)** Incorreta. Escolher apenas a maior relação ignora combinações.
- **D)** Incorreta. Atributos comuns não limitam produto sem condição.

**Conceito:** cardinalidade do produto cartesiano.

**Pegadinha:** somar em vez de multiplicar as quantidades.

**Como pensar:** multiplique as cardinalidades quando não houver filtro.

**Referência:** [Operações da álgebra relacional](semana_03_estudo.md#s3-d2-algebra-relacional).

### Comentário S3D2Q085

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Projetar nome primeiro remove atributos ainda necessários ao predicado.
- **B)** Incorreta. Auto-união não atende ao filtro.
- **C)** Incorreta. Diferença não expressa as duas condições.
- **D)** Correta. Seleção aplica UF/situação e projeção reduz o resultado a nome.

**Conceito:** composição seleção–projeção.

**Pegadinha:** executar a projeção antes de usar seus atributos no filtro.

**Como pensar:** resolva da operação interna de seleção para a externa de projeção.

**Referência:** [Exemplos de álgebra relacional](semana_03_estudo.md#s3-d2-exemplos-algebra).

### Comentário S3D2Q086

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Produto sem condição cria combinações, não ausência.
- **B)** Correta. A diferença entre conjuntos compatíveis representa quem não aparece.
- **C)** Incorreta. Ano e ID não são números a subtrair semanticamente.
- **D)** Incorreta. PROFISSIONAL não possui o conjunto de anos pedido.

**Conceito:** diferença para ausência.

**Pegadinha:** subtrair relações incompatíveis.

**Como pensar:** projete e renomeie IDs para esquemas compatíveis antes da diferença.

**Referência:** [Exemplos de álgebra relacional](semana_03_estudo.md#s3-d2-exemplos-algebra).

### Comentário S3D2Q087

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. Um estado particular não prova regra universal.
- **B)** Incorreta. 1FN não transforma coincidência em dependência.
- **C)** Correta. A regra admite contraexemplo e invalida a DF proposta.
- **D)** Incorreta. Atributos textuais podem participar de DFs.

**Conceito:** semântica da dependência funcional.

**Pegadinha:** inferir DF pela amostra atual.

**Como pensar:** procure a regra do domínio e tente construir um estado válido contrário.

**Referência:** [Dependências funcionais e anomalias](semana_03_estudo.md#s3-d2-dependencias).

### Comentário S3D2Q088

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Cada telefone vira ocorrência identificável com propriedades próprias.
- **B)** Incorreta. Aumentar campo mantém a coleção na célula.
- **C)** Incorreta. Trocar separador não muda a estrutura.
- **D)** Incorreta. Colunas numeradas criam grupo repetitivo e limite artificial.

**Conceito:** Primeira Forma Normal.

**Pegadinha:** tratar mudança de formato como normalização.

**Como pensar:** represente cada valor multivalorado em tupla própria.

**Referência:** [Primeira Forma Normal — 1FN](semana_03_estudo.md#s3-d2-1fn).

### Comentário S3D2Q089

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. A chave é composta e a dependência usa uma parte, não uma cadeia transitiva.
- **B)** Correta. Nome depende apenas de parte da chave, caracterizando parcialidade.
- **C)** Incorreta. Tipo textual não altera a análise funcional.
- **D)** Incorreta. A regra mostra que o par completo não é necessário.

**Conceito:** dependência parcial e 2FN.

**Pegadinha:** achar que toda DF proveniente da chave composta é completa.

**Como pensar:** remova uma parte da chave e veja se o atributo continua determinado.

**Referência:** [Exemplos de Segunda Forma Normal (2FN)](semana_03_estudo.md#s3-d2-exemplos-2fn).

### Comentário S3D2Q090

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. 2FN não garante BCNF.
- **B)** Correta. Sem chave candidata composta não há dependência parcial de parte dela.
- **C)** Incorreta. Chaves simples não eliminam DFs.
- **D)** Incorreta. Ainda pode existir dependência transitiva que viole 3FN.

**Conceito:** 2FN com chaves simples.

**Pegadinha:** concluir formas superiores automaticamente.

**Como pensar:** separe ausência de parcialidade da análise de transitividade e determinantes.

**Referência:** [Segunda Forma Normal — 2FN](semana_03_estudo.md#s3-d2-2fn).

### Comentário S3D2Q091

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A unidade recebe seu nome e SERVIDOR preserva a referência.
- **B)** Incorreta. Remover a FK perde a associação e nome pode não identificar.
- **C)** Incorreta. Nome de unidade não integra a chave de servidor.
- **D)** Incorreta. Repetição agrava a anomalia de atualização.

**Conceito:** dependência transitiva.

**Pegadinha:** eliminar também a chave de ligação.

**Como pensar:** mova o fato para seu determinante real e mantenha a FK.

**Referência:** [Exemplos de Terceira Forma Normal (3FN)](semana_03_estudo.md#s3-d2-exemplos-3fn).

### Comentário S3D2Q092

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Essa combinação não é a condição formal.
- **B)** Incorreta. O dependente não precisa ser FK.
- **C)** Correta. 3FN admite determinante superchave ou dependente primo.
- **D)** Incorreta. Quantidade de atributos de X não decide a forma normal.

**Conceito:** definição formal de 3FN.

**Pegadinha:** usar apenas a regra prática e esquecer a exceção de atributo primo.

**Como pensar:** teste cada DF não trivial pelos dois ramos da definição.

**Referência:** [Terceira Forma Normal — 3FN](semana_03_estudo.md#s3-d2-3fn).

### Comentário S3D2Q093

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. A exceção de atributo primo pode preservar 3FN.
- **B)** Incorreta. BCNF não aceita determinante que não seja superchave.
- **C)** Incorreta. O caso clássico pode ter chaves candidatas sobrepostas.
- **D)** Correta. A DF passa em 3FN pelo lado direito primo e falha em BCNF.

**Conceito:** diferença entre 3FN e BCNF.

**Pegadinha:** considerar as duas formas equivalentes.

**Como pensar:** verifique primeiro a exceção de 3FN e depois a exigência estrita de BCNF.

**Referência:** [Exemplos de Forma Normal de Boyce-Codd (BCNF)](semana_03_estudo.md#s3-d2-exemplos-bcnf).

### Comentário S3D2Q094

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Tipo do dependente é irrelevante.
- **B)** Correta. Todo determinante de DF não trivial deve ser superchave.
- **C)** Incorreta. BCNF não exige candidata única.
- **D)** Incorreta. Chaves compostas são permitidas.

**Conceito:** regra da BCNF.

**Pegadinha:** analisar o lado direito como na exceção de 3FN.

**Como pensar:** olhe para o determinante e teste se identifica toda a relação.

**Referência:** [Forma Normal de Boyce–Codd — BCNF](semana_03_estudo.md#s3-d2-bcnf).

### Comentário S3D2Q095

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Inserção ocorre quando um fato não pode ser cadastrado isoladamente.
- **B)** Incorreta. Independência lógica trata esquemas, não perda de fato por remoção.
- **C)** Correta. A exclusão de uma ocorrência apaga informação que deveria permanecer.
- **D)** Incorreta. Projeção não descreve a anomalia.

**Conceito:** anomalia de exclusão.

**Pegadinha:** confundir o gatilho exclusão com atualização.

**Como pensar:** nomeie a anomalia pelo evento que causa a perda indevida.

**Referência:** [Dependências funcionais e anomalias](semana_03_estudo.md#s3-d2-dependencias).

### Comentário S3D2Q096

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Redução de atributos não prova qualidade.
- **B)** Incorreta. FKs podem ser necessárias à reconstrução.
- **C)** Incorreta. Partes não precisam ter cardinalidades iguais.
- **D)** Correta. Junção deve reconstruir fatos válidos sem inventar combinações.

**Conceito:** junção sem perda.

**Pegadinha:** considerar boa qualquer divisão que reduza repetição.

**Como pensar:** teste a recomposição e procure tuplas espúrias ou associações perdidas.

**Referência:** [Decomposição sem perda e preservação de dependências](semana_03_estudo.md#s3-d2-decomposicao).

### Comentário S3D2Q097

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Papel repetido vira elo não identificador e produz combinações espúrias.
- **B)** Incorreta. A presença de chave não causa violação de 1FN.
- **C)** Incorreta. A divisão não elimina automaticamente os valores.
- **D)** Incorreta. Seleção e projeção não são o problema descrito.

**Conceito:** tuplas espúrias.

**Pegadinha:** juntar partes por atributo comum que não preserva o vínculo.

**Como pensar:** construa duas pessoas e dois projetos com o mesmo papel e teste a junção.

**Referência:** [Exemplos de decomposição relacional](semana_03_estudo.md#s3-d2-exemplos-decomposicao).

### Comentário S3D2Q098

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Preservação não exige conservar a relação original inteira.
- **B)** Correta. As restrições devem poder ser verificadas localmente nas partes, em geral.
- **C)** Incorreta. Reduzir texto não comprova preservação.
- **D)** Incorreta. Chaves de ligação não são dispensáveis.

**Conceito:** preservação de dependências.

**Pegadinha:** confundir esse critério com junção sem perda.

**Como pensar:** pergunte onde cada DF será imposta após a decomposição.

**Referência:** [Decomposição sem perda e preservação de dependências](semana_03_estudo.md#s3-d2-decomposicao).

### Comentário S3D2Q099

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Índice não remove redundância lógica.
- **B)** Incorreta. Remover a FK perde o vínculo com profissional.
- **C)** Incorreta. Lista de nomes não resolve a DF.
- **D)** Correta. O nome fica com seu determinante e PROCESSO mantém a referência.

**Conceito:** normalização de cadastro misto.

**Pegadinha:** remover redundância e também o elo necessário.

**Como pensar:** coloque cada fato com seu determinante e preserve as chaves de ligação.

**Referência:** [Prática de banco de dados](semana_03_estudo.md#s3-d2-pratica).

### Comentário S3D2Q100

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. FK única em FISCAL limitaria N:N e número pode repetir por processo.
- **B)** Incorreta. Listas em PROCESSO violam a modelagem relacional.
- **C)** Correta. A associativa representa o vínculo e a chave composta identifica documento no proprietário.
- **D)** Incorreta. Copiar nomes aumenta redundância e perde identidade estável.

**Conceito:** síntese de MER, mapeamento e normalização.

**Pegadinha:** resolver vínculos múltiplos com listas ou cópias de nomes.

**Como pensar:** mapeie cada regra separadamente e combine FKs, chaves e atributos do vínculo.

**Referência:** [Prática de banco de dados](semana_03_estudo.md#s3-d2-pratica).

### Comentário Extra Dia 2.1

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** princípio da legalidade
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Eficiência não autoriza afastar requisito legal.
- **B)** Incorreta. Legalidade administrativa não é mera liberdade privada.
- **C)** Correta. Agente atua conforme ordenamento e competência.
- **D)** Incorreta. Costume não substitui norma aplicável.

**Conceito:** legalidade administrativa.

**Pegadinha:** opor legalidade e eficiência.

**Como pensar:** verifique se a ação possui fundamento e competência.

**Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

### Comentário Extra Dia 2.2

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** referência absoluta
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Cifrões fixam coluna F e linha 1.
- **B)** Incorreta. B2 é relativa e se ajusta na cópia.
- **C)** Incorreta. Somente F1 permanece integralmente fixa.
- **D)** Incorreta. Há, sim, referência absoluta na fórmula.

**Conceito:** referência absoluta.

**Pegadinha:** ler o cifrão como símbolo decorativo.

**Como pensar:** observe separadamente fixação de coluna e linha.

**Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

### Comentário Extra Dia 2.3

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** consequência
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A primeira oração fornece a causa.
- **B)** Incorreta. Não há concessão entre os fatos.
- **C)** Incorreta. Nenhuma hipótese é estabelecida.
- **D)** Correta. A falha aparece como efeito da incompatibilidade.

**Conceito:** relação de consequência.

**Pegadinha:** classificar todo conector interoracional como causa.

**Como pensar:** pergunte qual oração explica e qual resulta.

**Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

### Comentário Extra Dia 2.4

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Direta e Indireta
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Órgão não possui personalidade jurídica própria.
- **B)** Correta. A distinção entre centro de competências e pessoa jurídica está correta.
- **C)** Incorreta. Ministérios integram a Direta, e a Indireta inclui entidades.
- **D)** Incorreta. Autarquia é entidade da Administração Indireta.

**Conceito:** órgão e entidade.

**Pegadinha:** usar Direta e Indireta como sinônimos.

**Como pensar:** identifique se há personalidade jurídica própria.

**Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

### Comentário Extra Dia 2.5

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** filtrar e excluir
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. Filtro cria recorte visual e preserva linhas.
- **B)** Incorreta. Linhas fora do critério não são apagadas.
- **C)** Incorreta. Filtragem não altera os valores ocultos.
- **D)** Incorreta. Referências de fórmulas não mudam por aplicar filtro.

**Conceito:** filtragem.

**Pegadinha:** confundir não exibição com exclusão.

**Como pensar:** diferencie estado dos dados de visualização.

**Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

### Comentário Extra Dia 2.6

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** referência pronominal
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Proximidade não garante o referente correto.
- **B)** Incorreta. Pronomes são recursos legítimos de coesão.
- **C)** Correta. O leitor deve recuperar o antecedente sem ambiguidade indevida.
- **D)** Incorreta. Pronome não introduz necessariamente causa.

**Conceito:** coesão referencial.

**Pegadinha:** escolher referente apenas pela proximidade.

**Como pensar:** teste se existe mais de um antecedente plausível.

**Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

### Comentário Extra Dia 2.7

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** publicidade e impessoalidade
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Exemplos de Administração Pública e CRM](semana_03_estudo.md#s3-d2-exemplos-adm).

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Transparência não autoriza promoção pessoal.
- **B)** Correta. Divulgação pode violar impessoalidade pela personalização.
- **C)** Incorreta. Princípios devem ser observados conjuntamente.
- **D)** Incorreta. Identificação institucional não exige exaltação do dirigente.

**Conceito:** publicidade e impessoalidade.

**Pegadinha:** considerar válida toda campanha informativa.

**Como pensar:** separe finalidade pública da promoção da autoridade.

**Referência:** [Exemplos de Administração Pública e CRM](semana_03_estudo.md#s3-d2-exemplos-adm).

### Comentário Extra Dia 2.8

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** visualização de filtro
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Excluir linhas destrói dados fora do recorte.
- **B)** Incorreta. Ordenar coluna isolada pode desalojar registros.
- **C)** Incorreta. Cópia pública não preserva controle nem simultaneidade.
- **D)** Correta. Visualização de filtro permite recorte individual.

**Conceito:** visualização de filtro.

**Pegadinha:** usar filtro comum quando cada colaborador precisa de visão própria.

**Como pensar:** escolha o recurso que não impõe a visualização aos demais.

**Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

### Comentário Extra Dia 2.9

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** conector condicional
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Portanto expressa conclusão.
- **B)** Incorreta. Embora expressa concessão.
- **C)** Correta. Caso introduz hipótese condicional.
- **D)** Incorreta. Contudo marca oposição.

**Conceito:** conectores lógicos.

**Pegadinha:** memorizar conectores sem testar a relação.

**Como pensar:** substitua por “se” e verifique se o sentido se mantém.

**Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

### Comentário Extra Dia 2.10

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** revogação
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Judiciário não revoga por conveniência administrativa.
- **B)** Correta. Revogação pressupõe ato válido e juízo de mérito, quando cabível.
- **C)** Incorreta. Ilegalidade conduz à anulação, não à revogação por mérito.
- **D)** Incorreta. Resolução não revoga lei automaticamente.

**Conceito:** revogação.

**Pegadinha:** usar revogar como verbo genérico de retirada.

**Como pensar:** pergunte primeiro se o ato é válido ou ilegal.

**Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

### Comentário Extra Dia 2.11

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** COUNTIF
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. SUM soma valores.
- **B)** Incorreta. AVERAGE calcula média.
- **C)** Incorreta. IF escolhe resultado por teste, mas não é a função de contagem pedida.
- **D)** Correta. COUNTIF conta células que satisfazem critério.

**Conceito:** contagem condicional.

**Pegadinha:** confundir teste lógico com agregação condicional.

**Como pensar:** associe o verbo contar à função COUNTIF.

**Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

### Comentário Extra Dia 2.12

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa e discursiva
- **Assunto:** desenvolvimento argumentativo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Desenvolvimento da resposta discursiva](semana_03_estudo.md#s3-d2-discursiva-desenvolvimento).

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. A sequência apresenta argumento, explicação, concretização e retorno à tese.
- **B)** Incorreta. Inventário tecnológico não desenvolve causalidade.
- **C)** Incorreta. Exemplo isolado não constitui parágrafo completo.
- **D)** Incorreta. Definições desconectadas não formam progressão.

**Conceito:** estrutura do desenvolvimento.

**Pegadinha:** transformar o parágrafo em enumeração.

**Como pensar:** atribua uma função argumentativa a cada frase.

**Referência:** [Desenvolvimento da resposta discursiva](semana_03_estudo.md#s3-d2-discursiva-desenvolvimento).

### Comentário Extra Dia 2.13

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** convalidação
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

**Alternativa correta: B.**


**Análise das alternativas:**

- **A)** Incorreta. Vício insanável não é corrigido por simples convalidação.
- **B)** Correta. Convalidação depende de vício sanável e requisitos jurídicos.
- **C)** Incorreta. Revogação retira ato válido por mérito.
- **D)** Incorreta. A Administração também pode convalidar quando cabível.

**Conceito:** convalidação.

**Pegadinha:** imaginar que qualquer ilegalidade é sanável.

**Como pensar:** classifique o vício antes de escolher a providência.

**Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

### Comentário Extra Dia 2.14

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** ordenação segura
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Exemplos de Google Planilhas](semana_03_estudo.md#s3-d2-exemplos-sheets).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Ordenar uma coluna isolada pode romper as linhas lógicas.
- **B)** Incorreta. Conversão em texto não corrige o desalinhamento.
- **C)** Incorreta. Cabeçalhos e filtros não precisam ser apagados.
- **D)** Correta. O intervalo completo mantém cada registro associado.

**Conceito:** ordenação de tabelas.

**Pegadinha:** ordenar somente a coluna usada como chave visual.

**Como pensar:** expanda a ordenação a todas as colunas relacionadas.

**Referência:** [Exemplos de Google Planilhas](semana_03_estudo.md#s3-d2-exemplos-sheets).

### Comentário Extra Dia 2.15

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concessão
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Embora não apresenta causa neste período.
- **B)** Incorreta. Não há finalidade pretendida.
- **C)** Correta. Embora admite um fato que não impede a conclusão oposta.
- **D)** Incorreta. Conclusão seria marcada por portanto ou equivalente.

**Conceito:** concessão.

**Pegadinha:** confundir concessão com oposição simples.

**Como pensar:** reformule com “ainda que” e teste o vínculo.

**Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

### Comentário Extra Dia 2.16

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** natureza do CRA-PR
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

**Alternativa correta: A.**


**Análise das alternativas:**

- **A)** Correta. O material o caracteriza como autarquia de direito público com autonomia.
- **B)** Incorreta. Órgão não possui personalidade, ao contrário da autarquia descrita.
- **C)** Incorreta. Autonomia não equivale a soberania.
- **D)** Incorreta. Não se trata de sociedade privada.

**Conceito:** natureza jurídica do CRA-PR.

**Pegadinha:** transformar autonomia em independência do ordenamento.

**Como pensar:** distinga personalidade própria, vinculação sistêmica e soberania.

**Referência:** [Administração Pública — princípios, organização e atos](semana_03_estudo.md#s3-d2-administracao-publica).

### Comentário Extra Dia 2.17

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** função IF
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

**Alternativa correta: D.**


**Análise das alternativas:**

- **A)** Incorreta. Soma é função de SUM.
- **B)** Incorreta. Ordenação não é função de IF.
- **C)** Incorreta. Cifrões fixam referências; IF não faz isso.
- **D)** Correta. IF seleciona um de dois resultados conforme teste.

**Conceito:** função condicional IF.

**Pegadinha:** confundir função lógica com formatação ou referência.

**Como pensar:** identifique teste, valor verdadeiro e valor falso.

**Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

### Comentário Extra Dia 2.18

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** ambiguidade referencial
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

**Alternativa correta: C.**


**Análise das alternativas:**

- **A)** Incorreta. O período possui verbo.
- **B)** Incorreta. Nenhuma concessão é necessária.
- **C)** Correta. Seu pode retomar fiscal ou gerente.
- **D)** Incorreta. A questão é linguística, não matemática.

**Conceito:** ambiguidade pronominal.

**Pegadinha:** atribuir automaticamente o possessivo ao nome mais próximo.

**Como pensar:** reescreva nomeando explicitamente o titular do relatório.

**Referência:** [Coesão textual](semana_03_estudo.md#s3-d2-portugues-coesao).

### Comentário Extra Dia 2.19

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** anulação por ilegalidade
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Exemplos de Administração Pública e CRM](semana_03_estudo.md#s3-d2-exemplos-adm).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Vício de competência exclusiva indicado como insanável conduz à anulação.
- **B)** Incorreta. Revogação pressupõe validade e mérito.
- **C)** Incorreta. O caso afasta convalidação automática.
- **D)** Incorreta. Presunção de legitimidade não é absoluta e não salva ilegalidade.

**Conceito:** anulação.

**Pegadinha:** revogar ato ilegal por conveniência.

**Como pensar:** se o defeito é de legalidade insanável, pense em anulação.

**Referência:** [Exemplos de Administração Pública e CRM](semana_03_estudo.md#s3-d2-exemplos-adm).

### Comentário Extra Dia 2.20

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Informática — Google Planilhas
- **Assunto:** referências mistas
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. $B$2 fixa ambas as dimensões.
- **B)** Correta. $B2 fixa B e deixa a linha ajustar-se.
- **C)** Incorreta. B$2 fixa a linha, não a coluna.
- **D)** Incorreta. B2 é referência relativa.

**Conceito:** referências mistas.

**Pegadinha:** associar todo cifrão à célula inteira.

**Como pensar:** leia o cifrão imediatamente antes da dimensão fixada.

**Referência:** [Google Planilhas](semana_03_estudo.md#s3-d2-google-planilhas).

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

# Dia 5 — Transações, concorrência, integridade, segurança e recuperação

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais — S3D5Q201 a S3D5Q250

### S3D5Q201 — Unidade lógica de trabalho

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transferência exige débito em A e crédito em B. Qual delimitação atende ao conceito de transação?

A) Cada `UPDATE` deve ser confirmado isoladamente, porque atua em linha distinta.

B) A consulta do saldo e todos os relatórios posteriores devem entrar obrigatoriamente na mesma transação.

C) Débito e crédito devem integrar uma única unidade lógica, confirmada somente se o conjunto for válido.

D) O limite deve ser escolhido pela quantidade de comandos, não pelo requisito de negócio.

### S3D5Q202 — Savepoint e confirmação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transação cria um `SAVEPOINT`, executa mais dois comandos e faz rollback até esse ponto. Ainda não houve `COMMIT`. Assinale a interpretação correta.

A) Tudo o que antecede o savepoint já é durável.

B) O rollback até o ponto confirma automaticamente o trecho preservado.

C) O savepoint cria uma segunda transação independente.

D) O trecho preservado continua pertencendo à transação ativa e depende de commit.

### S3D5Q203 — Último comando concluído

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

O último `UPDATE` de uma transação terminou e retornou “1 linha afetada”, mas a confirmação ainda não se tornou definitiva. No modelo didático, a transação pode estar:

A) parcialmente confirmada, sem que a mensagem do comando prove durabilidade.

B) confirmada, porque qualquer mensagem de sucesso equivale a commit.

C) abortada, pois o último comando já foi executado.

D) encerrada, ainda que o contexto transacional permaneça aberto.

### S3D5Q204 — Atomicidade e consistência

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Um débito foi executado, o crédito correspondente falhou e nenhuma parte deve permanecer. Qual associação é tecnicamente adequada?

A) Isolamento exige o rollback; durabilidade preserva o total.

B) Atomicidade impede o efeito parcial; consistência descreve a preservação do estado válido.

C) Consistência desfaz comandos; isolamento define o saldo inicial.

D) Durabilidade impede o efeito parcial; atomicidade decide quem pode acessar.

### S3D5Q205 — Início da durabilidade

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Em relação à durabilidade, qual evidência é necessária para tratar o resultado como permanente?

A) A decisão de commit concluída segundo o protocolo do SGBD.

B) A execução bem-sucedida de pelo menos um comando.

C) A criação de um savepoint antes da última escrita.

D) A existência de duas sessões lendo o mesmo valor.

### S3D5Q206 — Autocommit em operação composta

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma aplicação deixa o autocommit ativo e executa separadamente o débito e o crédito de uma transferência. O segundo comando falha. Qual risco foi criado?

A) Um `ROLLBACK` emitido depois da falha desfaz também o débito já confirmado pelo autocommit.

B) Nenhum; o autocommit agrupa comandos consecutivos por regra.

C) O autocommit cria um savepoint comum aos dois comandos, permitindo desfazer o conjunto.

D) O débito pode já estar confirmado, rompendo a atomicidade da operação composta.

### S3D5Q207 — Mapeamento das propriedades ACID

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Assinale a associação correta.

A) Atomicidade — ocultar dados de usuários sem privilégio.

B) Isolamento — controlar interferências concorrentes dentro da garantia escolhida.

C) Consistência — garantir que todas as sessões vejam sempre o mesmo instante.

D) Durabilidade — manter cópia histórica independente de toda transação.

### S3D5Q208 — Rollback após commit

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transação alcançou o estado confirmado. O usuário percebe depois que aplicou uma regra errada. O que se conclui?

A) Um savepoint anterior desfaz o commit já encerrado.

B) Basta emitir `ROLLBACK` na mesma conexão para apagar a confirmação.

C) A correção exige nova operação compensatória ou procedimento próprio; rollback simples não desfaz commit concluído.

D) O SGBD deve ignorar a confirmação porque a regra de negócio estava errada.

### S3D5Q209 — Consistência e regra de negócio

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transferência atualiza as duas contas, mas a lógica soma R$ 100 em B e subtrai R$ 90 de A. Não existe restrição que represente o total. Qual diagnóstico é correto?

A) A atomicidade detectará sozinha a diferença de R$ 10.

B) O isolamento corrigirá a fórmula antes do commit.

C) A transação pode ser atômica e ainda produzir estado inconsistente, pois a regra foi implementada incorretamente.

D) A durabilidade impedirá o commit por ausência de backup.

### S3D5Q210 — Conexão perdida antes da confirmação

**Nível:** Muito difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma aplicação recebeu sucesso no último comando, perdeu a conexão antes de obter evidência de commit e não sabe a decisão final. Qual conduta é mais segura?

A) Não tratar a mensagem do comando como prova; verificar o estado de negócio ou a decisão antes de repetir a operação.

B) Repetir imediatamente o débito, pois a transação necessariamente abortou.

C) Considerar o resultado confirmado, porque a conexão caiu depois do `UPDATE`.

D) Usar um novo savepoint na conexão encerrada para consultar a decisão.

### S3D5Q211 — Leitura suja

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 altera um valor; T2 lê esse valor; depois T1 aborta. O que T2 realizou?

A) Leitura fantasma.

B) Atualização perdida.

C) Leitura não repetível de valor confirmado.

D) Leitura suja, pois consumiu dado que nunca se confirmou.

### S3D5Q212 — Leitura não repetível

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 lê a linha do profissional 17. T2 altera essa mesma linha e confirma. T1 a relê e encontra outro valor. A anomalia é:

A) leitura suja.

B) leitura não repetível.

C) fantasma, obrigatoriamente.

D) deadlock.

### S3D5Q213 — Fantasma

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 conta pedidos pendentes e obtém 4. T2 insere outro pedido pendente e confirma. T1 repete o mesmo predicado e obtém 5. Trata-se de:

A) fantasma.

B) leitura suja.

C) atualização perdida.

D) starvation.

### S3D5Q214 — Atualização perdida

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

O estoque é 10. T1 lê 10 e calcula 8; T2 lê 10 e calcula 7. T1 grava 8 e T2 grava 7. Qual conclusão é correta?

A) O resultado 7 equivale às duas vendas em qualquer ordem serial.

B) Houve leitura suja porque T2 leu 10.

C) A escrita de T2 eliminou o efeito de T1; o resultado serial esperado seria 5.

D) O fenômeno é fantasma, pois o estoque mudou.

### S3D5Q215 — Significado de serializável

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Duas transações têm operações intercaladas, mas o efeito final equivale integralmente à ordem serial T2 seguida de T1. Essa execução:

A) não pode ser serializável, porque houve intercalação.

B) pode ser serializável, pois equivalência de efeito não exige execução física uma por vez.

C) é necessariamente Read Uncommitted.

D) prova ausência de qualquer rollback possível.

### S3D5Q216 — Read Committed no modelo clássico

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Na tabela conceitual do padrão SQL usada no estudo, o nível Read Committed:

A) admite leitura suja, mas impede fantasma.

B) impede toda anomalia de leitura.

C) impede leitura suja, mas pode admitir leitura não repetível e fantasma.

D) impede leitura não repetível e admite apenas atualização perdida.

### S3D5Q217 — Repeatable Read no modelo clássico

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Considerando somente a referência conceitual clássica, Repeatable Read:

A) permite leitura suja e impede fantasma.

B) impede apenas atualização perdida.

C) é idêntico a Read Uncommitted.

D) impede leitura suja e não repetível, mas o fantasma ainda pode ocorrer.

### S3D5Q218 — Locks compartilhado e exclusivo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Qual afirmação resume corretamente os locks apresentados?

A) Todo lock compartilhado bloqueia qualquer outra leitura.

B) Lock exclusivo é usado apenas para autenticar o usuário.

C) Locks compartilhados podem admitir leituras compatíveis; lock exclusivo protege escrita contra acessos incompatíveis.

D) A granularidade de lock é sempre a tabela inteira.

### S3D5Q219 — Limites do MVCC

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Sobre MVCC, assinale a alternativa correta.

A) Elimina locks de escrita e todos os conflitos entre escritores.

B) Garante que qualquer leitor veja sempre a versão mais recente.

C) Pode permitir snapshot consistente a leitores, mas não elimina conflito entre escritas incompatíveis.

D) Dispensa gestão e limpeza de versões em qualquer produto.

### S3D5Q220 — Ciclo de espera

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 mantém lock em A e espera B. T2 mantém lock em B e espera A. Qual ação e diagnóstico são compatíveis?

A) Há deadlock; o SGBD pode escolher uma vítima, desfazê-la e liberar recursos.

B) Há somente espera normal; ambas necessariamente concluirão sem intervenção.

C) Há starvation sem ciclo; conceder mais locks resolve.

D) Há leitura suja; basta elevar para Read Committed.

### S3D5Q221 — Espera transitória

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T2 espera um lock mantido por T1, mas T1 não espera nenhum recurso de T2 e pode confirmar. Esse quadro caracteriza, por si só:

A) deadlock de dois vértices.

B) bloqueio normal ou espera transitória, sem ciclo demonstrado.

C) atualização perdida já consumada.

D) livelock obrigatório.

### S3D5Q222 — Starvation

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Uma transação é repetidamente preterida e permanece sem obter o recurso, embora não exista ciclo fixo de espera. O fenômeno é:

A) starvation.

B) leitura fantasma.

C) deadlock, necessariamente.

D) durabilidade.

### S3D5Q223 — Prevenção de deadlock

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Duas rotinas alteram sempre os mesmos pares de unidades. Qual medida reduz a chance de deadlock sem proibir toda concorrência?

A) Aumentar indefinidamente a duração das transações.

B) Fazer cada rotina escolher ordem aleatória de locks.

C) Substituir locks por permissões administrativas.

D) Adquirir os recursos em uma ordem global consistente e manter a transação curta.

### S3D5Q224 — Serial e concorrente

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Qual proposição distingue corretamente execução serial e concorrente?

A) Concorrente significa que nenhuma operação pode esperar.

B) Serializável significa que as operações nunca se intercalam.

C) Execução serial termina uma transação antes de iniciar outra; a concorrente pode intercalar e ainda produzir resultado aceitável.

D) Execução serial exige MVCC e a concorrente exige apenas lock exclusivo.

### S3D5Q225 — Snapshot não é visão mais recente

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 lê um snapshot consistente enquanto T2 confirma uma alteração. A leitura de T1 não mostra imediatamente a nova versão. Isso prova falha do MVCC?

A) Sim, porque consistência exige sempre a versão mais nova.

B) Sim, porque todo commit invalida snapshots existentes.

C) Não; snapshot consistente pode preservar uma visão anterior conforme a garantia, sem prometer máxima atualidade.

D) Não; MVCC torna todas as escritas incompatíveis invisíveis para sempre.

### S3D5Q226 — Duração e contenção

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Por que uma transação longa tende a aumentar contenção?

A) Porque a duração, por si só, transforma qualquer espera unilateral em deadlock.

B) Porque todo SGBD eleva obrigatoriamente os locks para a tabela depois de um tempo fixo.

C) Porque os recursos são liberados ao fim de cada comando, o que impede espera entre transações.

D) Porque retém recursos e amplia a janela em que outras operações podem bloquear ou formar ciclos.

### S3D5Q227 — Nova tentativa da vítima

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Após detectar deadlock, o SGBD aborta T2. Qual tratamento de aplicação é adequado?

A) Registrar o evento e refazer T2 de modo controlado, considerando idempotência e possível repetição do conflito.

B) Considerar que T2 confirmou parcialmente porque chegou a obter locks.

C) Repetir indefinidamente sem limite, espera ou verificação.

D) Forçar T1 e T2 a cometerem para preservar todas as escritas.

### S3D5Q228 — Mesma linha ou novo membro

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 primeiro relê a mesma linha e encontra valor alterado por T2; depois repete um predicado e encontra linha nova inserida por T3. As anomalias, na ordem, são:

A) leitura suja e atualização perdida.

B) leitura não repetível e fantasma.

C) fantasma e leitura não repetível.

D) deadlock e starvation.

### S3D5Q229 — Operação atômica sobre valor corrente

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Para reduzir o risco de duas vendas calcularem estoque a partir da mesma base desatualizada, qual ideia está alinhada ao estudo?

A) Ler em duas sessões e aceitar a última gravação.

B) Encerrar a transação logo após a leitura e gravar depois, sem validar se o estoque mudou.

C) Repetir o mesmo ciclo de ler, calcular e sobrescrever após conflito, sem versão ou trava apropriada.

D) Usar mecanismo que detecte conflito, validação de versão ou atualização atômica apropriada sobre o valor corrente.

### S3D5Q230 — Serializable e aborto

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Uma transação em Serializable é abortada pelo SGBD devido a conflito de serialização. A melhor interpretação é:

A) O nível falhou, pois Serializable deve confirmar toda transação.

B) O produto executou necessariamente todas as transações uma por vez.

C) O aborto pode ser o mecanismo usado para impedir um resultado sem ordem serial equivalente.

D) O evento prova leitura suja confirmada.

### S3D5Q231 — Integridade de entidade

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Qual controle atende diretamente à integridade de entidade?

A) `GRANT SELECT` para a equipe de relatório.

B) Chave primária única e não nula para identificar cada linha.

C) Log de auditoria das exclusões.

D) Parâmetro preparado para o valor de login.

### S3D5Q232 — Integridade referencial

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma coluna `pagamento.profissional_id` deve apontar para profissional existente, salvo quando a relação puder ser nula. O controle central é:

A) chave estrangeira com a regra de nulidade apropriada.

B) role com privilégio de escrita.

C) checkpoint periódico.

D) lock compartilhado.

### S3D5Q233 — Integridade de domínio

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Impedir que o percentual receba 130 quando a faixa válida é de 0 a 100 é exemplo de:

A) integridade de domínio, implementável por tipo e `CHECK` adequados.

B) autenticação multifator.

C) isolamento serializável.

D) auditoria de comando.

### S3D5Q234 — Autenticação e autorização

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma usuária prova sua identidade, mas recebe somente leitura em uma view. Isso significa que:

A) a autorização falhou, porque autenticados devem escrever.

B) autenticação respondeu quem ela é; autorização limitou o que pode fazer.

C) a integridade referencial substituiu a permissão.

D) o MVCC retirou os privilégios de escrita.

### S3D5Q235 — Finalidade da auditoria

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Qual pergunta é respondida prioritariamente pela auditoria?

A) O valor pertence ao domínio permitido?

B) A transação é equivalente a uma execução serial?

C) Quem fez qual ação, quando e sobre qual objeto?

D) A chave estrangeira aponta para um pai existente?

### S3D5Q236 — Menor privilégio no relatório

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

A equipe precisa somente de totais por unidade e não deve ver CPF nem alterar registros. Qual desenho melhor aplica menor privilégio?

A) Conceder poderes administrativos e ocultar botões na interface.

B) Dar `SELECT` e `UPDATE` em todas as tabelas para evitar erros de permissão.

C) Compartilhar a conta do DBA somente durante o expediente.

D) Conceder a uma role `SELECT` sobre view limitada aos dados necessários, sem acesso direto mais amplo.

### S3D5Q237 — Efeito de REVOKE

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Foi executado `REVOKE SELECT` de uma concessão direta, mas o usuário continua consultando a tabela. Qual hipótese é compatível?

A) `REVOKE` aumenta privilégios antes de removê-los.

B) O acesso pode vir de outra role, herança, propriedade ou concessão ainda válida.

C) Toda consulta já aberta concede leitura permanente.

D) A chave primária substitui o privilégio revogado.

### S3D5Q238 — View e exposição residual

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Conceder `SELECT` em uma view sem CPF reduz exposição somente se:

A) a view usar `ORDER BY`.

B) o usuário também receber acesso administrativo à tabela base.

C) o CPF estiver apenas oculto pela interface da aplicação.

D) não houver outro privilégio direto mais amplo que permita contornar a view.

### S3D5Q239 — Valor parametrizado

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

A entrada de login contém `' OR 1=1 --`. Em uma API parametrizada corretamente, essa entrada:

A) é transmitida como valor e não passa a compor a estrutura lógica da instrução.

B) concede automaticamente a role pública.

C) vira nome de tabela seguro.

D) obriga o SGBD a desabilitar autorização.

### S3D5Q240 — Identificador dinâmico

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma tela permite escolher a coluna de ordenação. Por que não basta tratá-la como parâmetro de valor?

A) Porque parâmetros só aceitam números.

B) Porque toda ordenação dinâmica é proibida.

C) Porque nomes de coluna integram a estrutura; devem ser escolhidos por lista permitida e composição própria do produto.

D) Porque `ORDER BY` elimina injeção por definição.

### S3D5Q241 — Parâmetro não substitui autorização

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma aplicação usa parâmetros em todas as consultas, mas sua conta possui privilégios administrativos desnecessários. Qual avaliação é correta?

A) O uso de parâmetros converte a conta em menor privilégio.

B) A autorização torna desnecessária a parametrização.

C) A injeção por valores foi reduzida, mas a superfície de dano continua ampliada pelos privilégios excessivos.

D) Privilégio administrativo impede qualquer entrada maliciosa.

### S3D5Q242 — Princípio write-ahead

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Qual ordem expressa o princípio write-ahead?

A) O registro de log pertinente deve alcançar armazenamento durável antes da página de dados correspondente ser considerada persistida.

B) A página de dados deve ser gravada e só depois o log pode registrar o evento.

C) O checkpoint substitui todos os registros anteriores antes de qualquer commit.

D) O backup deve ser concluído antes de cada `UPDATE`.

### S3D5Q243 — Função de redo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

T1 confirmou, mas sua página ainda não refletia a alteração persistida quando houve queda. Na recuperação, a operação típica é:

A) undo de T1.

B) redo de T1, se necessário.

C) revogação dos privilégios de T1.

D) rollback de todo o checkpoint.

### S3D5Q244 — Função de undo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

T2 alterou uma página, mas não confirmou antes da queda. Se o efeito não confirmado chegou ao armazenamento, a recuperação deve:

A) preservá-lo por durabilidade.

B) tratá-lo como backup mais recente.

C) transformá-lo em commit implícito.

D) desfazê-lo ou neutralizá-lo por undo, conforme o algoritmo.

### S3D5Q245 — Limites do checkpoint

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Assinale a interpretação correta do checkpoint.

A) Confirma automaticamente todas as transações ativas.

B) Garante que todas as páginas foram copiadas ao mesmo instante.

C) Substitui o log e a cópia autônoma.

D) Marca coordenação que reduz trabalho de recuperação, sem ser commit global nem prova isolada de confirmação.

### S3D5Q246 — Recuperação integrada

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Antes da queda, T1 confirmou e T2 não confirmou. Algumas páginas de ambas foram gravadas. Qual estado final é exigido?

A) Manter tudo que chegou à página, pois escrita física supera o log.

B) Desfazer T1 e confirmar T2 para equilibrar o sistema.

C) Garantir T1, com redo se necessário, e remover efeitos de T2, com undo se necessário.

D) Desfazer tudo desde o último checkpoint, sem consultar decisões.

### S3D5Q247 — Primeira fase do 2PC

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Na primeira fase do commit em duas fases, o coordenador:

A) solicita preparo e cada participante registra o necessário e vota se pode confirmar.

B) manda cada participante decidir sozinho entre commit e rollback.

C) replica automaticamente todos os dados entre os nós.

D) libera todos os recursos antes de conhecer os votos.

### S3D5Q248 — Decisão global no 2PC

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Três participantes votam “preparado”. No fluxo normal do 2PC, qual decisão pode ser tomada pelo coordenador?

A) Cada participante escolhe uma decisão local diferente.

B) Commit global, registrado e comunicado aos participantes.

C) Rollback obrigatório, porque unanimidade indica conflito.

D) Conversão da operação em replicação assíncrona.

### S3D5Q249 — Participante preparado e coordenador indisponível

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

A e B votaram preparado, mas o coordenador ficou indisponível antes de divulgar a decisão. Qual risco específico aparece?

A) Leitura suja inevitável em todos os bancos.

B) Os participantes podem ficar aguardando a decisão global e manter recursos, causando bloqueio.

C) Cada participante deve confirmar imediatamente para aumentar disponibilidade.

D) O log deixa de ser necessário porque houve voto.

### S3D5Q250 — O que o 2PC não oferece

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Qual afirmação avalia corretamente o 2PC?

A) Busca atomicidade entre participantes, mas não replica dados nem garante maior disponibilidade ou velocidade.

B) Torna toda transação distribuída não bloqueante.

C) Substitui autorização, log local e controle de concorrência.

D) Permite commit parcial quando um participante não prepara.

## Questões extras — Dia 5

#### Extra Dia 5.1 — Lei e base da profissão

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Lei nº 4.769/1965
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Ao identificar no enunciado a disciplina e a base legal da profissão, qual fonte deve ser examinada primeiro?

A) Lei nº 4.769/1965.

B) RN CFA nº 651/2024.

C) RN CFA nº 671/2025.

D) Histórico de navegação do portal.

#### Extra Dia 5.2 — Regulamentação da lei

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Decreto nº 61.934/1967
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual instrumento foi associado à regulamentação da Lei nº 4.769/1965?

A) Código de Ética de 2025.

B) Regimento Interno do CRA-PR.

C) Decreto nº 61.934/1967.

D) Certificado digital do portal.

#### Extra Dia 5.3 — Organização interna do CRA-PR

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 651/2024
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Uma questão trata de órgãos e competências internas do CRA-PR. A primeira fonte do recorte é:

A) Lei nº 4.769/1965 apenas, sem consultar o regimento.

B) RN CFA nº 651/2024.

C) RN CFA nº 671/2025.

D) Decreto nº 61.934/1967 como se fosse o regimento interno.

#### Extra Dia 5.4 — Dever e sanção ética

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 671/2025
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Para item sobre dever, sigilo, infração ou sanção ética no recorte, deve-se identificar sujeito e conduta e consultar prioritariamente:

A) a Lei nº 4.769/1965, tratando-a como fonte única mesmo para a conduta ética específica.

B) a RN CFA nº 651/2024, voltada ao recorte de organização interna do CRA-PR.

C) o Decreto nº 61.934/1967, por regulamentar a lei de base da profissão.

D) a RN CFA nº 671/2025, após identificar o sujeito, a conduta e a consequência ética aplicável.

#### Extra Dia 5.5 — CFA nacional e CRA regional

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Âmbito de competência
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual divisão de atuação é compatível com a revisão?

A) O CRA-PR exerce toda orientação normativa nacional porque fiscaliza no Paraná.

B) O CFA orienta o sistema dentro da competência normativa; o CRA-PR registra e fiscaliza em sua jurisdição.

C) O CFA executa sozinho toda diligência local no Paraná.

D) Autonomia regional elimina a integração ao sistema.

#### Extra Dia 5.6 — Resolução posterior e lei

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Hierarquia normativa
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Uma resolução administrativa posterior contradiz diretamente a Lei nº 4.769/1965. Qual conclusão decorre do método estudado?

A) A resolução não afasta a lei apenas por ser mais recente; hierarquia e competência devem ser respeitadas.

B) A resolução revoga automaticamente a lei por critério cronológico.

C) O CRA-PR escolhe livremente a norma mais conveniente.

D) As duas fontes viram recomendações sem força.

#### Extra Dia 5.7 — Autonomia sem ruptura

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Autonomia regional
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

A autonomia regional do CRA-PR permite:

A) contrariar lei federal em matéria profissional.

B) substituir toda orientação nacional do CFA.

C) atuar fora de sua jurisdição sempre que houver interesse.

D) organizar e exercer suas competências próprias sem romper limites e normas superiores.

#### Extra Dia 5.8 — Roteiro de leitura institucional

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Método de resolução
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual roteiro reduz melhor o erro em casos institucionais?

A) Objeto → norma mais recente → conclusão, sem conferir hierarquia ou competência.

B) Território → órgão regional → atribuição de todas as funções, sem separar fonte e limite.

C) Objeto → fonte → sujeito → território → verbo de competência → limite.

D) Fonte → sanção → sujeito, sem verificar território nem verbo de competência.

#### Extra Dia 5.9 — Publicidade e sigilo

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Limites de transparência
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual formulação preserva o equilíbrio apresentado?

A) Publicidade institucional autoriza divulgar qualquer dado pessoal.

B) Sigilo permite omitir toda prestação de contas.

C) A publicidade não elimina sigilo legal ou proteção de dados, e o sigilo não extingue toda transparência devida.

D) Transparência e sigilo são incompatíveis em qualquer caso.

#### Extra Dia 5.10 — Caso integrado de competência

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, território e verbo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Um fato fiscalizatório ocorre no Paraná e envolve possível infração ética. Qual caminho é tecnicamente mais responsável?

A) Aplicar só a lei de criação e ignorar a conduta ética.

B) Identificar sujeito e conduta na norma ética e a atuação fiscalizatória do CRA-PR em sua jurisdição, sem atribuir-lhe toda competência normativa nacional.

C) Transferir automaticamente a diligência local ao CFA porque a norma é nacional.

D) Usar o regimento interno para afastar lei e código de ética.

#### Extra Dia 5.11 — Partes de uma URL

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** URL
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Em `https://portal.exemplo.br/servicos?id=7#prazo`, qual decomposição está correta?

A) `https` é host; `portal.exemplo.br` é fragmento.

B) `/servicos` é consulta; `id=7` é esquema.

C) `prazo` é caminho e `https` é cookie.

D) `https` é esquema; `portal.exemplo.br` é host; `/servicos` é caminho; `id=7` é consulta; `prazo` é fragmento.

#### Extra Dia 5.12 — Alcance do HTTPS

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** HTTPS e certificado
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

O cadeado de HTTPS permite concluir que:

A) o trânsito está protegido e o servidor é autenticado conforme a cadeia, mas o conteúdo e a intenção do site não se tornam automaticamente confiáveis.

B) a instituição dona da marca controla necessariamente o domínio acessado.

C) qualquer oferta exibida é legítima.

D) a conexão é anônima para provedor e site.

#### Extra Dia 5.13 — Cache, cookie, histórico e download

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Artefatos de navegação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Assinale a associação correta.

A) Cache registra apenas a lista cronológica de páginas; histórico acelera conteúdo.

B) Cache guarda cópia para acelerar; cookie mantém estado ou preferência; histórico registra navegação; download grava arquivo.

C) Cookie cifra todo o tráfego; download mantém sessão.

D) Histórico autentica certificado; cache concede anonimato.

#### Extra Dia 5.14 — Navegação privada

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Privacidade local e rede
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Sobre navegação privada, assinale a alternativa correta.

A) Torna o computador invisível ao site.

B) Impede a organização de observar tráfego de sua rede.

C) Substitui VPN e autenticação.

D) Reduz certos registros locais da sessão, mas não cria anonimato perante rede, provedor, organização ou site.

#### Extra Dia 5.15 — Domínio parecido com cadeado

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Phishing e verificação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Um link leva a domínio parecido com o oficial, com certificado válido, e pede credencial. Qual conduta é adequada?

A) Não inserir a senha; conferir host completo, origem do link e canal oficial, pois o certificado pode autenticar o domínio falso acessado.

B) Inserir a senha porque o cadeado prova a titularidade institucional.

C) Confiar se as cores e o logotipo forem idênticos.

D) Ativar navegação privada e prosseguir, pois ela valida o destinatário.

#### Extra Dia 5.16 — Referente inequívoco

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coesão referencial
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Em “A administração explicou os critérios aos cidadãos, pois eles eram incompletos”, qual reescrita elimina a ambiguidade pretendendo afirmar que os critérios eram incompletos?

A) A administração explicou-os aos cidadãos, pois eles eram incompletos.

B) A administração explicou os critérios aos cidadãos, pois estes eram incompletos.

C) A administração explicou aos cidadãos os critérios utilizados, pois tais critérios eram incompletos.

D) A administração explicou aos cidadãos, pois os mesmos eram incompletos.

#### Extra Dia 5.17 — Relação do conector

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coerência entre orações
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

A frase deve admitir um benefício e, apesar dele, introduzir um risco. Qual conector realiza essa relação?

A) Portanto.

B) Porque.

C) Assim.

D) Embora.

#### Extra Dia 5.18 — Paralelismo em enumeração

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Paralelismo sintático
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Qual enumeração mantém paralelismo?

A) O plano exige medir resultados, transparência e que se protejam dados.

B) O plano exige medir resultados, explicar critérios e proteger dados.

C) O plano exige medição de resultados, explicar critérios e dados protegidos.

D) O plano exige que os resultados sejam medidos, transparência e proteger dados.

#### Extra Dia 5.19 — Força de termos absolutos

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Modalização
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Os dados disponíveis mostram melhoria em alguns serviços, sem controlar todas as variáveis. Qual conclusão tem força compatível?

A) O uso responsável de dados pode contribuir para melhorar serviços, desde que qualidade e contexto sejam avaliados.

B) Dados sempre eliminam ineficiência.

C) A melhoria prova que dados nunca geram riscos.

D) Qualquer coleta causa necessariamente o mesmo resultado.

#### Extra Dia 5.20 — Arquitetura do plano integral

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Planejamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Qual plano atende ao treino sobre uso responsável de dados em serviços públicos?

A) Introdução sem tese; dois exemplos técnicos; conclusão com argumento novo.

B) Tese absoluta de que dados eliminam riscos; um desenvolvimento; lista de ferramentas.

C) Definições de SQL e índices, sem relação compreensível com o tema geral.

D) Problema e tese condicionada; desenvolvimento sobre benefício e qualidade; desenvolvimento sobre risco, transparência e proteção; conclusão que reformula a tese sem argumento novo.

## Gabarito — Dia 5

### Principais

| S3D5Q201 | S3D5Q202 | S3D5Q203 | S3D5Q204 | S3D5Q205 | S3D5Q206 | S3D5Q207 | S3D5Q208 | S3D5Q209 | S3D5Q210 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | D | A | B | A | D | B | C | C | A |

| S3D5Q211 | S3D5Q212 | S3D5Q213 | S3D5Q214 | S3D5Q215 | S3D5Q216 | S3D5Q217 | S3D5Q218 | S3D5Q219 | S3D5Q220 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | A | C | B | C | D | C | C | A |

| S3D5Q221 | S3D5Q222 | S3D5Q223 | S3D5Q224 | S3D5Q225 | S3D5Q226 | S3D5Q227 | S3D5Q228 | S3D5Q229 | S3D5Q230 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | A | D | C | C | D | A | B | D | C |

| S3D5Q231 | S3D5Q232 | S3D5Q233 | S3D5Q234 | S3D5Q235 | S3D5Q236 | S3D5Q237 | S3D5Q238 | S3D5Q239 | S3D5Q240 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | A | A | B | C | D | B | D | A | C |

| S3D5Q241 | S3D5Q242 | S3D5Q243 | S3D5Q244 | S3D5Q245 | S3D5Q246 | S3D5Q247 | S3D5Q248 | S3D5Q249 | S3D5Q250 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | B | D | D | C | A | B | B | A |

### Extras

| 5.1 | 5.2 | 5.3 | 5.4 | 5.5 | 5.6 | 5.7 | 5.8 | 5.9 | 5.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | B | D | B | A | D | C | C | B |

| 5.11 | 5.12 | 5.13 | 5.14 | 5.15 | 5.16 | 5.17 | 5.18 | 5.19 | 5.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | A | B | D | A | C | D | B | A | D |

## Comentários — Dia 5

### Comentário S3D5Q201

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Separa a unidade em commits incompatíveis com a obrigação única.
- **B)** Incorreta. Inclui relatórios independentes sem necessidade.
- **C)** Correta. Une débito e crédito conforme o requisito lógico.
- **D)** Incorreta. Usa quantidade de comandos como critério, o que é incorreto.

**Conceito:** Transação como unidade lógica.

**Pegadinha:** Tomar comando isolado como fronteira automática.

**Como pensar:** Identifique o conjunto que só é válido quando concluído por inteiro.

### Comentário S3D5Q202

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Savepoint não gera durabilidade.
- **B)** Incorreta. Rollback parcial não confirma o trecho preservado.
- **C)** Incorreta. Não nasce uma transação independente.
- **D)** Correta. O trecho continua ativo e depende do commit.

**Conceito:** Savepoint e rollback parcial.

**Pegadinha:** Confundir ponto de retorno com commit.

**Como pensar:** Separe o que foi desfeito do que já foi confirmado.

### Comentário S3D5Q203

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É o estado didático compatível antes da confirmação definitiva.
- **B)** Incorreta. Mensagem de comando não equivale a commit.
- **C)** Incorreta. Não houve falha ou aborto informado.
- **D)** Incorreta. Encerramento exige commit ou aborto e liberação do contexto.

**Conceito:** Estados transacionais.

**Pegadinha:** Interpretar linha afetada como confirmação.

**Como pensar:** Procure a decisão de commit, não apenas o término do comando.

### Comentário S3D5Q204

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Troca atomicidade por isolamento.
- **B)** Correta. Atomicidade evita metade; consistência caracteriza o estado válido.
- **C)** Incorreta. Atribui a consistência o mecanismo de desfazimento.
- **D)** Incorreta. Durabilidade não decide acesso nem evita por si o efeito parcial.

**Conceito:** Atomicidade versus consistência.

**Pegadinha:** Escolher propriedade pela palavra “falha”.

**Como pensar:** Pergunte separadamente se ficou metade e se o estado final é válido.

### Comentário S3D5Q205

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A decisão confirmada inaugura a garantia de durabilidade.
- **B)** Incorreta. Comando bem-sucedido ainda pode estar em transação ativa.
- **C)** Incorreta. Savepoint não torna dados permanentes.
- **D)** Incorreta. Duas leituras não provam confirmação.

**Conceito:** Durabilidade após commit.

**Pegadinha:** Confundir execução com permanência.

**Como pensar:** Localize a fronteira da decisão transacional.

### Comentário S3D5Q206

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Rollback posterior não reabre nem desfaz automaticamente o commit já concluído pelo autocommit.
- **B)** Incorreta. Autocommit não agrupa comandos por proximidade.
- **C)** Incorreta. Autocommit não cria savepoint compartilhado entre comandos confirmados separadamente.
- **D)** Correta. O primeiro comando pode persistir sozinho e romper a atomicidade.

**Conceito:** Autocommit em operação composta.

**Pegadinha:** Acreditar que comandos consecutivos são uma unidade.

**Como pensar:** Desenhe um commit depois de cada comando e verifique o requisito.

### Comentário S3D5Q207

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Ocultação é segurança, não atomicidade.
- **B)** Correta. Isolamento controla interferências concorrentes dentro da garantia.
- **C)** Incorreta. Consistência não exige visão global instantânea.
- **D)** Incorreta. Durabilidade não é sinônimo de backup histórico.

**Conceito:** Propriedades ACID.

**Pegadinha:** Usar associação intuitiva em vez da definição.

**Como pensar:** Transforme cada propriedade em sua pergunta central.

### Comentário S3D5Q208

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Savepoint não sobrevive como desfazimento de commit encerrado.
- **B)** Incorreta. Rollback simples atua sobre transação ativa.
- **C)** Correta. Efeito confirmado exige nova correção ou compensação.
- **D)** Incorreta. O SGBD não invalida sozinho toda regra errada.

**Conceito:** Limite do rollback.

**Pegadinha:** Tratar rollback como reversão ilimitada.

**Como pensar:** Primeiro determine se a transação ainda está ativa.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Rollback após commit”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q209

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Atomicidade pode existir mesmo com fórmula errada.
- **B)** Incorreta. Isolamento não corrige regra de negócio.
- **C)** Correta. A operação inteira pode levar a estado semanticamente inválido.
- **D)** Incorreta. Durabilidade não depende de backup antes do commit.

**Conceito:** Consistência e lógica da transação.

**Pegadinha:** Supor que ACID descobre regras não representadas.

**Como pensar:** Teste integralidade e validade em etapas diferentes.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Consistência e regra de negócio”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q210

**Nível:** Muito difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A decisão desconhecida deve ser verificada antes de nova tentativa.
- **B)** Incorreta. A queda da conexão não prova aborto.
- **C)** Incorreta. Sucesso do update não prova commit.
- **D)** Incorreta. Savepoint não consulta decisão após perda da conexão.

**Conceito:** Resultado transacional incerto.

**Pegadinha:** Converter ausência de resposta em certeza.

**Como pensar:** Busque evidência idempotente do resultado antes de repetir.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Conexão perdida antes da confirmação”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q211

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Nenhum conjunto por predicado mudou.
- **B)** Incorreta. Não houve sobrescrita de escrita.
- **C)** Incorreta. O valor lido não chegou a ser confirmado.
- **D)** Correta. T2 consumiu dado de T1 que depois foi abortado.

**Conceito:** Leitura suja.

**Pegadinha:** Nomear toda mudança como não repetível.

**Como pensar:** Pergunte se o valor lido chegou a ser confirmado.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Leitura suja”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q212

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A alteração de T2 foi confirmada.
- **B)** Correta. A mesma linha mudou entre duas leituras de T1.
- **C)** Incorreta. Não houve nova linha no conjunto.
- **D)** Incorreta. Não existe ciclo de espera.

**Conceito:** Leitura não repetível.

**Pegadinha:** Confundir linha alterada com fantasma.

**Como pensar:** Sublinhe “mesma linha”.

### Comentário S3D5Q213

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Uma nova linha passou a satisfazer o mesmo predicado.
- **B)** Incorreta. O dado foi confirmado, portanto não é sujo.
- **C)** Incorreta. Nenhuma escrita foi apagada.
- **D)** Incorreta. Não há adiamento indefinido.

**Conceito:** Fantasma.

**Pegadinha:** Olhar apenas para a contagem.

**Como pensar:** Compare os membros do conjunto nas duas execuções.

### Comentário S3D5Q214

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. As duas reduções deveriam resultar em 5.
- **B)** Incorreta. O valor-base pode ser confirmado.
- **C)** Correta. A última escrita apagou a redução de T1.
- **D)** Incorreta. Não houve entrada ou saída de linha.

**Conceito:** Atualização perdida.

**Pegadinha:** Aceitar a última gravação como soma dos efeitos.

**Como pensar:** Calcule o resultado serial esperado e compare.

### Comentário S3D5Q215

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Intercalação não exclui equivalência serial.
- **B)** Correta. O efeito pode equivaler à ordem T2→T1.
- **C)** Incorreta. Não é possível inferir Read Uncommitted.
- **D)** Incorreta. Isolamento forte ainda pode exigir rollback.

**Conceito:** Serializabilidade.

**Pegadinha:** Confundir serial com serializável.

**Como pensar:** Avalie o efeito, não apenas a ordem física.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Significado de serializável”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q216

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Read Committed impede leitura suja no quadro clássico.
- **B)** Incorreta. Não impede todas as anomalias.
- **C)** Correta. É a linha conceitual correta, com ressalva de produto.
- **D)** Incorreta. Não repetível ainda pode ocorrer.

**Conceito:** Read Committed clássico.

**Pegadinha:** Importar comportamento de um fornecedor.

**Como pensar:** Identifique primeiro se a cobrança é conceitual ou específica.

### Comentário S3D5Q217

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Leitura suja não é admitida.
- **B)** Incorreta. O nível protege mais de uma anomalia.
- **C)** Incorreta. Não se iguala a Read Uncommitted.
- **D)** Correta. Impede suja e não repetível; fantasma pode ocorrer no modelo clássico.

**Conceito:** Repeatable Read clássico.

**Pegadinha:** Responder pelo produto sem ler o enquadramento.

**Como pensar:** Use a tabela conceitual quando o enunciado assim delimitar.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Repeatable Read no modelo clássico”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q218

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Compartilhados podem admitir leituras compatíveis.
- **B)** Incorreta. Lock não autentica usuário.
- **C)** Correta. Distingue leitura compatível e proteção de escrita.
- **D)** Incorreta. Granularidade não é sempre tabela.

**Conceito:** Locks compartilhado e exclusivo.

**Pegadinha:** Ler lock como bloqueio total.

**Como pensar:** Verifique recurso e compatibilidade da operação.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Locks compartilhado e exclusivo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q219

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. MVCC não elimina conflito entre escritores.
- **B)** Incorreta. Snapshot não garante máxima atualidade.
- **C)** Correta. Leitores podem ter visão consistente sem acabar com disputa de escrita.
- **D)** Incorreta. Versões ainda exigem gestão conforme o produto.

**Conceito:** MVCC e seus limites.

**Pegadinha:** Tratar MVCC como ausência de locks.

**Como pensar:** Separe leitor–escritor de escritor–escritor.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Limites do MVCC”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q220

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O grafo T1→T2→T1 contém ciclo e pode exigir rollback da vítima.
- **B)** Incorreta. A espera não é unilateral nem garantidamente transitória.
- **C)** Incorreta. Há ciclo, portanto não é apenas starvation.
- **D)** Incorreta. Nenhuma leitura suja foi descrita.

**Conceito:** Deadlock.

**Pegadinha:** Chamar todo bloqueio de deadlock ou ignorar o ciclo.

**Como pensar:** Desenhe as arestas de espera.

### Comentário S3D5Q221

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Falta aresta de retorno para ciclo.
- **B)** Correta. T1 pode terminar e liberar o recurso.
- **C)** Incorreta. Nenhuma sobrescrita ocorreu.
- **D)** Incorreta. Não há atividade repetida sem progresso.

**Conceito:** Espera normal.

**Pegadinha:** Inferir ciclo de uma única dependência.

**Como pensar:** Procure caminho que retorne à transação inicial.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Espera transitória”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q222

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Adiamento indefinido sem ciclo obrigatório é starvation.
- **B)** Incorreta. Fantasma altera conjunto de predicado.
- **C)** Incorreta. Deadlock precisaria de ciclo.
- **D)** Incorreta. Durabilidade não trata escalonamento de oportunidade.

**Conceito:** Starvation.

**Pegadinha:** Usar deadlock para todo atraso longo.

**Como pensar:** Pergunte se ninguém progride por ciclo ou se um participante é sempre preterido.

### Comentário S3D5Q223

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Transação longa amplia retenção.
- **B)** Incorreta. Ordem aleatória favorece inversões.
- **C)** Incorreta. Privilégios não resolvem espera por dados.
- **D)** Correta. Ordem global e curta duração reduzem formação de ciclo.

**Conceito:** Prevenção de deadlock.

**Pegadinha:** Aplicar segurança a problema de concorrência.

**Como pensar:** Impeça aquisições em ordens opostas.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Prevenção de deadlock”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q224

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Concorrência pode envolver espera.
- **B)** Incorreta. Serializável não proíbe intercalação física.
- **C)** Correta. A distinção usa término completo versus intercalação aceita.
- **D)** Incorreta. Mecanismos não definem por si os escalonamentos.

**Conceito:** Serial e concorrente.

**Pegadinha:** Confundir mecanismo com definição.

**Como pensar:** Defina a cronologia física antes da equivalência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Serial e concorrente”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q225

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Consistência do snapshot não implica dado mais novo.
- **B)** Incorreta. Commit alheio não torna todo snapshot falho.
- **C)** Correta. Uma visão anterior pode ser estável dentro da garantia.
- **D)** Incorreta. A invisibilidade não é permanente nem universal.

**Conceito:** Snapshot e atualidade.

**Pegadinha:** Exigir última versão de todo snapshot.

**Como pensar:** Descubra qual visão foi prometida pelo nível e pelo produto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Snapshot não é visão mais recente”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q226

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Uma espera unilateral continua podendo ser transitória; deadlock exige ciclo.
- **B)** Incorreta. Escalonamento de lock depende do produto e da carga, não de um tempo universal.
- **C)** Incorreta. Se os recursos fossem liberados após cada comando, a duração não explicaria maior retenção.
- **D)** Correta. Maior retenção amplia espera e janela de ciclo.

**Conceito:** Transação longa e contenção.

**Pegadinha:** Ignorar o tempo de posse do recurso.

**Como pensar:** Marque quando o primeiro lock é adquirido e liberado.

### Comentário S3D5Q227

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A vítima foi abortada e deve ser refeita com política controlada.
- **B)** Incorreta. Locks obtidos não equivalem a confirmação parcial.
- **C)** Incorreta. Repetição cega pode amplificar conflito e efeitos externos.
- **D)** Incorreta. Commit forçado não é solução para um ciclo detectado.

**Conceito:** Retry após deadlock.

**Pegadinha:** Delegar todo tratamento ao SGBD.

**Como pensar:** Trate a vítima como operação não concluída e preserve idempotência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Nova tentativa da vítima”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q228

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não há dado abortado nem escrita apagada.
- **B)** Correta. A mesma linha muda; depois muda o conjunto do predicado.
- **C)** Incorreta. A ordem dos conceitos está invertida.
- **D)** Incorreta. Nenhuma espera foi informada.

**Conceito:** Não repetível versus fantasma.

**Pegadinha:** Chamar ambos de “resultado diferente”.

**Como pensar:** Identifique se mudou valor de linha existente ou membros do conjunto.

### Comentário S3D5Q229

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Aceitar a última escrita causa perda da anterior.
- **B)** Incorreta. Separar leitura e gravação sem validar mudança amplia a janela de base desatualizada.
- **C)** Incorreta. Repetir o mesmo ciclo sem versão, lock ou operação atômica pode reproduzir a perda.
- **D)** Correta. Conflito, versão ou operação atômica preservam o valor corrente.

**Conceito:** Prevenção de atualização perdida.

**Pegadinha:** Mudar representação em vez de coordenar a escrita.

**Como pensar:** Exija que a gravação use ou valide a versão corrente.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Operação atômica sobre valor corrente”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q230

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Serializable não promete confirmar toda tentativa.
- **B)** Incorreta. Equivalência serial não exige execução física uma a uma.
- **C)** Correta. O aborto impede resultado incompatível com ordem serial.
- **D)** Incorreta. Leitura suja não foi demonstrada.

**Conceito:** Aborto de serialização.

**Pegadinha:** Tomar rollback como falha da garantia.

**Como pensar:** Pergunte qual resultado surgiria se ambas fossem confirmadas.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Serializable e aborto”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q231

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Grant trata autorização.
- **B)** Correta. Chave primária única e não nula identifica a entidade.
- **C)** Incorreta. Auditoria registra ações.
- **D)** Incorreta. Parâmetro protege a construção do comando.

**Conceito:** Integridade de entidade.

**Pegadinha:** Misturar integridade com segurança.

**Como pensar:** Procure o mecanismo que identifica cada ocorrência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Integridade de entidade”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q232

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. FK valida a relação com a linha pai.
- **B)** Incorreta. Role não prova existência do pai.
- **C)** Incorreta. Checkpoint pertence à recuperação.
- **D)** Incorreta. Lock não valida referência.

**Conceito:** Integridade referencial.

**Pegadinha:** Usar autorização para corrigir relação estrutural.

**Como pensar:** A expressão “aponta para existente” seleciona a FK.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Integridade referencial”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q233

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Tipo e check limitam o conjunto de valores.
- **B)** Incorreta. Autenticação valida identidade.
- **C)** Incorreta. Serializable controla concorrência.
- **D)** Incorreta. Auditoria evidencia, mas não define a faixa.

**Conceito:** Integridade de domínio.

**Pegadinha:** Trocar prevenção por registro posterior.

**Como pensar:** Escreva o conjunto permitido antes de escolher o controle.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Integridade de domínio”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q234

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Usuário autenticado não recebe poder total.
- **B)** Correta. Identidade e operações permitidas são controles distintos.
- **C)** Incorreta. FK não concede privilégios.
- **D)** Incorreta. MVCC não retira permissão.

**Conceito:** Autenticação e autorização.

**Pegadinha:** Tratar login válido como autorização ampla.

**Como pensar:** Faça as perguntas “quem?” e “pode fazer o quê?”.

### Comentário S3D5Q235

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Faixa válida pertence ao domínio.
- **B)** Incorreta. Equivalência serial pertence ao isolamento.
- **C)** Correta. Auditoria produz rastreabilidade de ação.
- **D)** Incorreta. Existência do pai pertence à referência.

**Conceito:** Auditoria.

**Pegadinha:** Esperar que auditoria impeça toda ação inválida.

**Como pensar:** Associe-a a evidência de quem, o quê, quando e objeto.

### Comentário S3D5Q236

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Poder administrativo não é neutralizado pela interface.
- **B)** Incorreta. Escrita e tabelas amplas excedem a necessidade.
- **C)** Incorreta. Compartilhar DBA amplia risco.
- **D)** Correta. Role e view limitam operações e dados à finalidade.

**Conceito:** Menor privilégio.

**Pegadinha:** Confundir ocultação visual com controle no banco.

**Como pensar:** Remova cada objeto e verbo que não seja necessário ao relatório.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Menor privilégio no relatório”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q237

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Revoke não concede temporariamente mais poder.
- **B)** Correta. Outro caminho de autorização pode manter o acesso.
- **C)** Incorreta. Consulta prévia não cria grant permanente.
- **D)** Incorreta. Chave primária não autoriza usuário.

**Conceito:** Privilégio efetivo.

**Pegadinha:** Avaliar apenas uma concessão direta.

**Como pensar:** Enumere roles, heranças, propriedade e outros grants.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Efeito de REVOKE”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q238

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ordenação não limita acesso.
- **B)** Incorreta. Privilégio administrativo contorna o recorte.
- **C)** Incorreta. Interface não impede consulta direta.
- **D)** Correta. A view só limita de fato sem rota paralela mais ampla.

**Conceito:** View de acesso limitado.

**Pegadinha:** Esquecer privilégios diretos sobre a base.

**Como pensar:** Faça um mapa de todos os caminhos do usuário até os dados.

### Comentário S3D5Q239

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A entrada segue como valor literal separado da instrução.
- **B)** Incorreta. Parâmetro não concede role.
- **C)** Incorreta. Valor não vira identificador seguro.
- **D)** Incorreta. Autorização continua independente.

**Conceito:** Parâmetros e injeção.

**Pegadinha:** Imaginar mera concatenação com escape.

**Como pensar:** Separe canal de código e canal de valor.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Valor parametrizado”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q240

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Parâmetros aceitam também texto e outros tipos.
- **B)** Incorreta. Ordenação dinâmica pode ser feita com controle.
- **C)** Correta. Identificador muda a estrutura e pede allowlist.
- **D)** Incorreta. Order by não neutraliza entrada maliciosa.

**Conceito:** Identificador dinâmico seguro.

**Pegadinha:** Tratar nome de coluna como valor comum.

**Como pensar:** Se a entrada altera a gramática, escolha-a de lista fechada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Identificador dinâmico”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q241

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Parâmetro não modifica privilégios.
- **B)** Incorreta. Autorização não substitui construção segura.
- **C)** Correta. Um controle reduz injeção; o outro ainda amplia impacto.
- **D)** Incorreta. Poder administrativo não filtra entrada.

**Conceito:** Defesa em profundidade.

**Pegadinha:** Considerar um controle como substituto universal.

**Como pensar:** Avalie separadamente estrutura do SQL e alcance da conta.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Parâmetro não substitui autorização”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q242

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O log durável precede a página correspondente.
- **B)** Incorreta. A ordem inversa enfraquece a recuperação.
- **C)** Incorreta. Checkpoint não substitui os registros necessários.
- **D)** Incorreta. Backup não antecede cada update transacional.

**Conceito:** Write-ahead logging.

**Pegadinha:** Priorizar a página e registrar depois.

**Como pensar:** Garanta primeiro a evidência que permitirá undo ou redo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Princípio write-ahead”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q243

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. T1 confirmou e não deve ser desfeita.
- **B)** Correta. Redo reaplica o efeito confirmado ausente da página.
- **C)** Incorreta. Privilégio não recupera dado.
- **D)** Incorreta. Checkpoint não é transação a ser revertida.

**Conceito:** Redo.

**Pegadinha:** Desfazer o que ainda não estava na página.

**Como pensar:** Confirmada e ausente pede reaplicação.

### Comentário S3D5Q244

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Sem commit, durabilidade não protege o efeito.
- **B)** Incorreta. Página gravada não é backup nem decisão.
- **C)** Incorreta. Queda não produz commit implícito.
- **D)** Correta. Undo remove efeito de transação não confirmada.

**Conceito:** Undo.

**Pegadinha:** Confundir persistência física com confirmação lógica.

**Como pensar:** Classifique pelo registro de decisão.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Função de undo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q245

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Checkpoint não confirma ativas.
- **B)** Incorreta. Não garante fotografia de todas as páginas.
- **C)** Incorreta. Não elimina log nem cópia autônoma.
- **D)** Correta. Coordena e reduz trabalho sem decidir commits.

**Conceito:** Checkpoint.

**Pegadinha:** Interpretá-lo como “salvar tudo”.

**Como pensar:** Use-o para orientar recuperação, não para classificar transações sozinho.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Limites do checkpoint”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q246

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Página gravada não supera a decisão do log.
- **B)** Incorreta. A alternativa inverte confirmada e ativa.
- **C)** Correta. Redo preserva T1; undo remove T2.
- **D)** Incorreta. Checkpoint não invalida commits posteriores.

**Conceito:** Recuperação integrada.

**Pegadinha:** Usar estado físico como único critério.

**Como pensar:** Faça duas listas: commits que devem aparecer e ativas que não podem ficar.

### Comentário S3D5Q247

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A fase prepare coleta votos duráveis de capacidade.
- **B)** Incorreta. Decisão local divergente quebra atomicidade.
- **C)** Incorreta. 2PC não replica dados.
- **D)** Incorreta. Participante preparado pode manter recursos.

**Conceito:** Primeira fase do 2PC.

**Pegadinha:** Confundir prepare com commit.

**Como pensar:** Fase 1 pergunta; fase 2 decide e comunica.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Primeira fase do 2PC”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q248

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Participantes não escolhem decisões divergentes.
- **B)** Correta. Unanimidade positiva permite commit global.
- **C)** Incorreta. Votos sim não obrigam rollback.
- **D)** Incorreta. O protocolo não vira replicação.

**Conceito:** Decisão global no 2PC.

**Pegadinha:** Tomar voto como decisão local definitiva.

**Como pensar:** Aplique unanimidade e uma decisão única.

### Comentário S3D5Q249

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Leitura suja não é consequência obrigatória.
- **B)** Correta. Sem decisão conhecida, preparados podem bloquear mantendo recursos.
- **C)** Incorreta. Commit unilateral ameaça atomicidade.
- **D)** Incorreta. Registro de preparo continua necessário.

**Conceito:** Bloqueio no 2PC.

**Pegadinha:** Associar distribuição a disponibilidade automática.

**Como pensar:** Pergunte o que o participante sabe depois de votar sim.

### Comentário S3D5Q250

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. 2PC coordena atomicidade, sem prometer replicação, velocidade ou disponibilidade.
- **B)** Incorreta. O protocolo pode bloquear.
- **C)** Incorreta. Não substitui controles locais.
- **D)** Incorreta. Falha no preparo conduz a rollback global.

**Conceito:** Objetivo e limites do 2PC.

**Pegadinha:** Dar ao protocolo benefícios não relacionados.

**Como pensar:** Separe decisão atômica de desempenho, cópia e segurança.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “O que o 2PC não oferece”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.1

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Lei nº 4.769/1965
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É a fonte indicada para disciplina e base da profissão.
- **B)** Incorreta. Trata da organização interna no recorte.
- **C)** Incorreta. É a referência ética indicada.
- **D)** Incorreta. Histórico não é fonte normativa.

**Conceito:** Objeto e fonte normativa.

**Pegadinha:** Escolher pela data.

**Como pensar:** Identifique primeiro o objeto jurídico.

#### Comentário Extra Dia 5.2

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Decreto nº 61.934/1967
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. É norma ética, não regulamentadora.
- **B)** Incorreta. Regimento e decreto têm objetos distintos.
- **C)** Correta. É o decreto associado à regulamentação da lei.
- **D)** Incorreta. Certificado não regulamenta profissão.

**Conceito:** Lei e decreto.

**Pegadinha:** Confundir espécies infralegais.

**Como pensar:** Associe o verbo “regulamentar” ao decreto indicado.

#### Comentário Extra Dia 5.3

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 651/2024
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A lei é base, mas não esgota o objeto interno específico.
- **B)** Correta. É a norma indicada para organização e competência interna.
- **C)** Incorreta. A RN nº 671/2025 é ética.
- **D)** Incorreta. Decreto regulamentador não é regimento.

**Conceito:** Organização interna.

**Pegadinha:** Ignorar o complemento do objeto.

**Como pensar:** Sublinhe “órgãos e competências internas”.

#### Comentário Extra Dia 5.4

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 671/2025
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A lei disciplina a profissão, mas não esgota a conduta ética específica cobrada.
- **B)** Incorreta. A RN nº 651/2024 trata do recorte de organização interna, não do código ético indicado.
- **C)** Incorreta. O decreto regulamenta a lei de base, mas não substitui a norma ética posterior do recorte.
- **D)** Correta. A RN nº 671/2025 é a fonte ética do recorte, aplicada depois de identificar sujeito, conduta e consequência.

**Conceito:** Regra ética.

**Pegadinha:** Pular direto para a sanção.

**Como pensar:** Faça sujeito → conduta → norma → consequência.

#### Comentário Extra Dia 5.5

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Âmbito de competência
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Fiscalização regional não transfere toda orientação nacional.
- **B)** Correta. A divisão respeita verbo, território e limite.
- **C)** Incorreta. CFA nacional não executa necessariamente toda diligência local.
- **D)** Incorreta. Autonomia não rompe a integração.

**Conceito:** CFA e CRA-PR.

**Pegadinha:** Confundir território com competência normativa total.

**Como pensar:** Separe órgão, verbo e âmbito.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “CFA nacional e CRA regional”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.6

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Hierarquia normativa
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Recência não supera sozinha lei e competência.
- **B)** Incorreta. Resolução não revoga lei automaticamente.
- **C)** Incorreta. Conveniência não é critério de validade.
- **D)** Incorreta. Conflito não transforma normas em meras recomendações.

**Conceito:** Hierarquia normativa.

**Pegadinha:** Aplicar cronologia isoladamente.

**Como pensar:** Compare hierarquia e competência antes da data.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Resolução posterior e lei”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.7

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Autonomia regional
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Autonomia não autoriza contrariar lei.
- **B)** Incorreta. O CRA não absorve toda orientação nacional.
- **C)** Incorreta. Jurisdição continua limitadora.
- **D)** Correta. A autonomia opera dentro das competências e normas superiores.

**Conceito:** Autonomia limitada.

**Pegadinha:** Confundir autonomia com soberania.

**Como pensar:** Complete a frase com competência e limite.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Autonomia sem ruptura”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.8

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Método de resolução
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Recência, sem hierarquia e competência, não resolve conflito entre fontes.
- **B)** Incorreta. O território não transfere ao órgão regional todas as funções do sistema.
- **C)** Correta. É a sequência de seis filtros ensinada.
- **D)** Incorreta. Começar pela sanção e omitir território e competência inverte o método.

**Conceito:** Roteiro institucional.

**Pegadinha:** Saltar do território para a resposta.

**Como pensar:** Preencha os seis campos antes de comparar alternativas.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Roteiro de leitura institucional”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.9

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Limites de transparência
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Publicidade não elimina proteção aplicável.
- **B)** Incorreta. Sigilo não apaga toda prestação de contas.
- **C)** Correta. A solução preserva ambos os deveres com limites.
- **D)** Incorreta. Não há incompatibilidade absoluta.

**Conceito:** Transparência e sigilo.

**Pegadinha:** Absolutizar um dos valores.

**Como pensar:** Procure compatibilização, não eliminação.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Publicidade e sigilo”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.10

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, território e verbo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A lei de base não esgota a conduta ética.
- **B)** Correta. Combina norma ética, sujeito e atuação regional limitada.
- **C)** Incorreta. Alcance nacional não impõe execução direta de toda diligência.
- **D)** Incorreta. Regimento não afasta fontes superiores.

**Conceito:** Caso normativo integrado.

**Pegadinha:** Buscar uma única fonte para objetos distintos.

**Como pensar:** Separe regra da conduta e órgão de aplicação.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Caso integrado de competência”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.11

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** URL
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Troca esquema, host e fragmento.
- **B)** Incorreta. Inverte caminho e consulta.
- **C)** Incorreta. Fragmento e esquema foram mal classificados.
- **D)** Correta. Identifica corretamente todos os componentes.

**Conceito:** Componentes de URL.

**Pegadinha:** Ignorar delimitadores.

**Como pensar:** Corte a URL em `://`, `?` e `#`.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Partes de uma URL”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.12

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** HTTPS e certificado
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cifra trânsito e autentica host conforme cadeia, sem garantir honestidade do conteúdo.
- **B)** Incorreta. Domínio parecido pode ser de terceiro.
- **C)** Incorreta. TLS não valida toda oferta.
- **D)** Incorreta. HTTPS não cria anonimato.

**Conceito:** Limites do HTTPS.

**Pegadinha:** Usar cadeado como selo de legitimidade.

**Como pensar:** Confira qual host foi autenticado.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Alcance do HTTPS”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.13

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Artefatos de navegação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Troca cache e histórico.
- **B)** Correta. A sequência associa acelerar, estado, registro e arquivo.
- **C)** Incorreta. Cookie não cifra tráfego.
- **D)** Incorreta. Histórico e cache não têm essas funções.

**Conceito:** Cache, cookie, histórico e download.

**Pegadinha:** Chamar tudo de temporário.

**Como pensar:** Associe cada artefato a um verbo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Cache, cookie, histórico e download”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.14

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Privacidade local e rede
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O site continua observando a conexão.
- **B)** Incorreta. A rede organizacional pode continuar visível.
- **C)** Incorreta. Modo privado não substitui túnel ou identidade.
- **D)** Correta. Reduz rastros locais sem gerar anonimato externo.

**Conceito:** Navegação privada.

**Pegadinha:** Confundir local com rede.

**Como pensar:** Liste separadamente dispositivo, rede, provedor e site.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Navegação privada”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.15

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Phishing e verificação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A conduta verifica domínio e canal antes de fornecer segredo.
- **B)** Incorreta. Cadeado não prova vínculo institucional esperado.
- **C)** Incorreta. A estética pode ser copiada.
- **D)** Incorreta. Modo privado não autentica destinatário.

**Conceito:** Verificação contra phishing.

**Pegadinha:** Confiar em aparência ou TLS isolado.

**Como pensar:** Valide o host por canal oficial independente.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Domínio parecido com cadeado”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.16

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coesão referencial
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. “Eles” continua ambíguo.
- **B)** Incorreta. “Estes” ainda pode retomar cidadãos.
- **C)** Correta. A repetição de “critérios” fixa o referente.
- **D)** Incorreta. “Os mesmos” não resolve a ambiguidade.

**Conceito:** Referente inequívoco.

**Pegadinha:** Trocar um pronome por outro.

**Como pensar:** Repita o núcleo nominal quando houver dois antecedentes.

#### Comentário Extra Dia 5.17

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coerência entre orações
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. “Portanto” é conclusão.
- **B)** Incorreta. “Porque” é causa ou explicação.
- **C)** Incorreta. “Assim” é consequência.
- **D)** Correta. “Embora” introduz concessão.

**Conceito:** Conector concessivo.

**Pegadinha:** Escolher pelo som.

**Como pensar:** Parafraseie com “apesar de”.

#### Comentário Extra Dia 5.18

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Paralelismo sintático
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Mistura verbo, substantivo e oração.
- **B)** Correta. Coordena três infinitivos.
- **C)** Incorreta. Combina estruturas diferentes.
- **D)** Incorreta. Também rompe a equivalência formal.

**Conceito:** Paralelismo.

**Pegadinha:** Olhar apenas o sentido.

**Como pensar:** Compare o núcleo gramatical de cada membro.

#### Comentário Extra Dia 5.19

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Modalização
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A conclusão condicionada respeita evidência parcial.
- **B)** Incorreta. “Sempre” e “elimina” excedem os dados.
- **C)** Incorreta. Um resultado não prova ausência universal de risco.
- **D)** Incorreta. Generaliza causalidade sem controle.

**Conceito:** Força da conclusão.

**Pegadinha:** Usar termos absolutos com evidência limitada.

**Como pensar:** Ajuste modalizadores à força da prova.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Força de termos absolutos”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.20

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Planejamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Faltam tese e progressão.
- **B)** Incorreta. A tese absoluta e a estrutura incompleta falham.
- **C)** Incorreta. Jargão técnico não sustenta o tema geral.
- **D)** Correta. Há problema, tese, dois eixos e conclusão sem novidade.

**Conceito:** Plano integral da discursiva.

**Pegadinha:** Confundir tecnicismo com argumento.

**Como pensar:** Confira uma função própria para cada parágrafo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Arquitetura do plano integral”; a extensão decorre dessa precisão técnica, não de pista formal.

---

# Dia 6 — Índices, otimização, SGBDs e Business Intelligence

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais — S3D6Q251 a S3D6Q300

### S3D6Q251 — Índice como caminho com custo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Um índice deve ser entendido como:

A) uma regra lógica que muda a resposta correta da consulta.

B) uma estrutura gratuita, sem efeito sobre escrita.

C) uma garantia de que o otimizador fará busca indexada.

D) uma estrutura auxiliar de acesso que pode reduzir leitura, mas consome espaço e manutenção.

### S3D6Q252 — B-tree e hash

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Qual comparação conceitual está correta?

A) Hash preserva ordem e atende faixas melhor que B-tree.

B) B-tree só pode ser usado para igualdade.

C) B-tree costuma apoiar igualdade e faixa; hash tende à igualdade da chave completa e não preserva ordem.

D) Hash criado pelo usuário possui sintaxe idêntica nos três SGBDs.

### S3D6Q253 — Prefixo à esquerda

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Dado o índice B-tree `(uf, status, nome)`, qual predicado usa um prefixo clássico de duas colunas?

A) `uf='PR' AND status='A'`.

B) `status='A' AND nome='Ana'`.

C) `nome='Ana'`.

D) `status='A'`.

### S3D6Q254 — Salto de coluna no índice composto

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Com índice `(uf, status, nome)`, a consulta filtra `uf='PR' AND nome='Ana'`, sem condição para `status`. Qual análise é responsável?

A) O índice é sempre impossível de ler.

B) `uf` oferece prefixo útil, mas o salto de `status` pode limitar o aproveitamento ordenado de `nome`; o plano final depende do custo.

C) Todas as três colunas formam busca de igualdade contínua.

D) O SGBD deve converter o índice em hash.

### S3D6Q255 — Cobertura depende da consulta

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Um índice contém todas as colunas necessárias para filtrar, juntar e retornar uma consulta específica. Nesse contexto, ele é:

A) clustered em qualquer produto.

B) cobridor para essa consulta, sem que isso implique cobrir todas as outras.

C) uma constraint de domínio.

D) obrigatoriamente escolhido pelo otimizador.

### S3D6Q256 — Baixa seletividade e scan

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Uma consulta retorna 96% de uma tabela larga ao filtrar `ativo='S'`. Qual decisão inicial é adequada?

A) Criar um índice isolado e forçar seu uso.

B) Preferir o índice porque a presença de qualquer `WHERE` torna a leitura seletiva.

C) Proibir índice nessa coluna em todos os cenários apenas por ela ter poucos valores distintos.

D) Comparar custos; um scan pode ser mais barato que percorrer índice e buscar quase todas as linhas.

### S3D6Q257 — Predicado sargável

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Em SQL conceitual com literal tipado — cuja escrita deve ser adaptada ao dialeto —, qual predicado tende a expor melhor a chave indexada `criado_em` para o ano de 2026?

A) `EXTRACT(YEAR FROM criado_em)=2026`.

B) `CAST(criado_em AS text) LIKE '2026%'`.

C) `criado_em >= DATE '2026-01-01' AND criado_em < DATE '2027-01-01'`.

D) `criado_em + INTERVAL '0 day' >= DATE '2026-01-01'`.

### S3D6Q258 — Limite superior exclusivo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

No mesmo SQL conceitual, por que o filtro anual usa `criado_em < DATE '2027-01-01'` em vez de terminar em `2026-12-31` sem horário?

A) O limite exclusivo inclui todo o último dia independentemente da precisão de horário.

B) B-tree não aceita data de dezembro.

C) O limite transforma faixa em igualdade.

D) `BETWEEN` nunca funciona com datas.

### S3D6Q259 — Custo colateral de índice

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Adicionar um índice a uma tabela muito atualizada tende a:

A) acrescentar trabalho de manutenção em inserções, alterações e exclusões, além de espaço.

B) eliminar qualquer custo de escrita porque só armazena chaves.

C) dispensar estatísticas.

D) alterar a resposta lógica do `SELECT`.

### S3D6Q260 — Constraint e índice

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Qual afirmação distingue corretamente constraint e índice?

A) São sempre sinônimos, pois ambos ocupam páginas.

B) Índice define a regra institucional; constraint serve apenas ao desempenho.

C) Constraint só existe quando não há estrutura física.

D) Constraint expressa regra lógica; índice é mecanismo físico que o produto pode usar para garanti-la ou acelerar acesso.

### S3D6Q261 — B-tree e ordenação

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Por preservar ordenação de chaves, uma B-tree pode ajudar:

A) somente em inserções sem leitura.

B) em faixas e em certos `ORDER BY` compatíveis com a ordem do índice.

C) a converter qualquer predicado não sargável.

D) a executar hash join sem ler entradas.

### S3D6Q262 — Hash e faixa

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Para `valor BETWEEN 100 AND 200`, por que um índice hash conceitual não é o candidato natural?

A) Porque hash só armazena textos.

B) Porque toda faixa exige scan de tabela.

C) Porque hash não preserva ordem para percorrer intervalo; seu uso típico é igualdade da chave completa.

D) Porque B-tree não aceita igualdade.

### S3D6Q263 — Coluna pouco seletiva em composição

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Uma coluna de dois valores possui baixa seletividade isolada. Isso permite concluir que ela:

A) jamais pode aparecer em índice.

B) deve ser sempre a primeira coluna.

C) pode ainda colaborar em índice composto, cobertura, ordenação ou subconjunto específico; é preciso medir.

D) transforma automaticamente o índice em constraint.

### S3D6Q264 — Cobertura relativa

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Em um produto que suporte `INCLUDE`, o índice `(unidade_id, status) INCLUDE (total)` cobre a Consulta A, que usa apenas essas colunas. A Consulta B também retorna `observacao`. Qual conclusão é correta?

A) O índice pode cobrir A e não B, pois cobertura é relação entre estrutura e consulta.

B) Se cobre uma consulta, cobre a tabela inteira.

C) `INCLUDE` torna obrigatória a escolha do índice.

D) Cobertura elimina todo custo de escrita.

### S3D6Q265 — Ordem de índice por carga real

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

A consulta crítica filtra unidade e status por igualdade, restringe período e ordena por data; raramente busca apenas status. Qual candidato inicial é mais coerente?

A) `(status, criado_em, unidade_id)` apenas porque status aparece no `WHERE`.

B) `(criado_em, status, unidade_id)` porque data possui muitos valores.

C) `(status)` e um índice separado em cada coluna, sem medir.

D) `(unidade_id, status, criado_em)`, seguido de medição do plano, projeção e custo de escrita.

### S3D6Q266 — Conversão implícita e busca

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Uma coluna numérica indexada é comparada a entrada textual de tipo incompatível, levando o produto a converter a coluna em cada linha. O risco é:

A) a conversão sobre a coluna ser inofensiva apenas porque os valores representam números equivalentes.

B) a conversão sobre a coluna prejudicar sargabilidade e o caminho de busca convencional.

C) a existência do índice obrigar o otimizador a converter a entrada, preservando sempre a busca.

D) acrescentar a mesma coluna a outro índice eliminar a conversão aplicada no predicado.

### S3D6Q267 — Curinga inicial

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Qual padrão tende a dificultar a busca convencional pelo prefixo de uma B-tree em `nome`?

A) `nome = 'Ana'`.

B) `nome >= 'M'`.

C) `nome LIKE 'Ana%'`.

D) `nome LIKE '%ana'`.

### S3D6Q268 — Índice por expressão

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

A consulta precisa manter exatamente `EXTRACT(YEAR FROM criado_em)=2026`. Qual ressalva evita afirmar que toda função torna índice inútil?

A) Função sempre vira chave primária.

B) O otimizador ignora todas as expressões.

C) Um índice por expressão ou recurso equivalente, criado e compatível, pode oferecer caminho adequado.

D) Qualquer índice em outra coluna resolve.

### S3D6Q269 — Índice não garante uso

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Existe índice compatível, mas a tabela tem 40 linhas e todas serão retornadas. O scan escolhido pelo otimizador:

A) pode ser correto, pois o custo de ler poucas páginas pode ser menor.

B) prova corrupção do índice.

C) deve ser substituído por dica sem medição.

D) altera a semântica da consulta.

### S3D6Q270 — Diagnóstico integrado de índice

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um relatório melhorou de 8 s para 900 ms após novo índice, mas a carga horária subiu de 20 s para 38 s. Qual decisão é tecnicamente completa?

A) Manter o índice porque qualquer leitura tem prioridade.

B) Avaliar frequência, criticidade, custo acumulado de escrita, espaço e alternativas antes de manter ou reverter.

C) Remover todas as constraints para compensar.

D) Declarar sucesso apenas pela menor latência do relatório.

### S3D6Q271 — Custo do otimizador

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

O número de custo mostrado em um plano deve ser lido como:

A) tempo garantido em milissegundos.

B) unidade interna comparativa usada para escolher entre planos, não cronômetro universal.

C) quantidade exata de linhas reais.

D) percentual de uso de CPU medido.

### S3D6Q272 — Estatísticas desatualizadas

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Estatísticas que não representam mais a distribuição podem levar o otimizador a:

A) manter necessariamente as mesmas cardinalidades, pois a distribuição não participa das estimativas.

B) afetar apenas o texto exibido no plano, sem influenciar a escolha de operadores.

C) substituir linhas reais por estimadas durante a execução, sem efeito sobre a ordem de junção.

D) estimar cardinalidades inadequadas e escolher ordem ou método de junção pouco apropriado.

### S3D6Q273 — Estimado versus real

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um nó estima 1 linha e produz 500 mil. Qual é o primeiro alvo do diagnóstico?

A) Entender a causa da estimativa incorreta antes de forçar operador aleatório.

B) Atualizar estatísticas e encerrar o diagnóstico sem conferir se a divergência desapareceu.

C) Forçar hash join apenas porque o volume real é grande, antes de localizar a origem da estimativa.

D) Criar índice para cada coluna do nó, sem analisar distribuição, correlação ou forma do predicado.

### S3D6Q274 — Nested loop contextual

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Quando um nested loop pode ser boa escolha?

A) Somente quando não há índice algum.

B) Sempre que as duas entradas são enormes.

C) Quando a entrada externa é pequena e há busca interna eficiente.

D) Apenas para condição sem igualdade.

### S3D6Q275 — Hash join

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual afirmação sobre hash join está correta?

A) Exige que exista índice hash nas duas tabelas.

B) Só funciona com dados previamente ordenados.

C) Pode ser adequado para igualdade e conjuntos relevantes, sem exigir índice hash criado pelo usuário.

D) É sempre superior a nested loop.

### S3D6Q276 — Merge join

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual cenário pode favorecer merge join?

A) Predicados sem condição compatível e entradas aleatórias obrigatoriamente.

B) Entradas já ordenadas ou ordenáveis de modo vantajoso e condição compatível.

C) Ausência total de relação entre tabelas.

D) Somente presença de índice hash.

### S3D6Q277 — Scan não é falha automática

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual situação justifica um scan?

A) Toda consulta com `WHERE`.

B) Somente tabela sem chave primária.

C) Apenas consulta não sargável.

D) Tabela pequena ou necessidade de grande parte das linhas, quando o custo global é menor.

### S3D6Q278 — Seek não garante rapidez

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um plano usa index seek/search, mas retorna milhões de linhas e executa acessos adicionais caros. Qual conclusão é correta?

A) O nome do operador não garante rapidez; é preciso avaliar cardinalidade, trabalho total e métricas.

B) Seek prova que o plano é ótimo.

C) O resultado lógico está errado.

D) Estatísticas deixam de ter importância.

### S3D6Q279 — Maior discrepância no plano

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Ao comparar plano estimado e real, qual pista merece prioridade?

A) Grande diferença entre linhas estimadas e reais em nó que influencia o restante da árvore.

B) O maior percentual de custo estimado, mesmo quando estimativa e execução desse nó coincidem.

C) A presença de qualquer scan, mesmo barato.

D) O último nó desenhado na ferramenta, por ser necessariamente a origem da primeira estimativa incorreta.

### S3D6Q280 — EXPLAIN nos três produtos

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Assinale a comparação correta.

A) SQL Server usa `EXPLAIN ANALYZE` como sintaxe T-SQL genérica.

B) PostgreSQL não executa a consulta com `EXPLAIN ANALYZE`.

C) PostgreSQL 18.4 e MySQL 9.7 LTS oferecem `EXPLAIN` e `EXPLAIN ANALYZE`; SQL Server 2025 17.x expõe planos estimado e real por suas ferramentas.

D) Os três apresentam plano real sem executar nada.

### S3D6Q281 — Plano real e DML

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Por que uma análise que executa DML deve ocorrer em ambiente controlado?

A) Porque DML nunca pode ter plano.

B) Porque obter métricas reais pode executar e modificar dados; reversão deve ser planejada quando apropriada.

C) Porque todo plano real concede `COMMIT` ao usuário.

D) Porque estatística desabilita rollback.

### S3D6Q282 — Protocolo de otimização

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual sequência representa o protocolo ensinado?

A) Criar índice → forçar plano → procurar consulta.

B) Escolher dica → mudar três fatores → medir outro parâmetro.

C) Medir depois → apagar estatísticas → aceitar.

D) Registrar cenário → obter plano → formular hipótese → mudar uma coisa → medir igual → comparar custos → decidir.

### S3D6Q283 — Uma mudança por vez

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual é a principal razão para alterar um fator por vez?

A) Reduzir a quantidade de alternativas do SQL padrão.

B) Garantir que toda mudança melhore.

C) Evitar a necessidade de plano real.

D) Atribuir o efeito observado à hipótese testada e permitir reversão com evidência.

### S3D6Q284 — Dicas de plano

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Por que uma dica não deve ser a primeira reação?

A) Pode envelhecer, esconder a causa da estimativa e piorar outros parâmetros.

B) Porque dicas sempre geram erro de sintaxe.

C) Porque nenhum SGBD possui recursos de controle de plano.

D) Porque a dica corrige automaticamente estatísticas.

### S3D6Q285 — Correlação entre colunas

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

O plano estima 50 mil linhas para `uf='PR' AND cidade='Curitiba'`, mas retorna 4 mil. A primeira hipótese responsável é:

A) As estatísticas estão necessariamente desatualizadas, ainda que não haja evidência de mudança recente nos dados.

B) Aumentar a amostra de estatísticas independentes sempre representa a dependência entre as duas colunas.

C) estatística ou modelo de seletividade que não representa a correlação entre UF e cidade.

D) Forçar o método de junção corrige por si a estimativa produzida no filtro correlacionado.

### S3D6Q286 — Tabela de 40 linhas

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Uma tabela de 40 linhas será lida integralmente. O otimizador escolhe scan. O que fazer?

A) Criar quatro índices até aparecer seek.

B) Aceitar que o scan pode ser o plano mais barato e verificar as métricas, sem “corrigir” pelo nome.

C) Forçar nested loop.

D) Desnormalizar a tabela.

### S3D6Q287 — Custo global do serviço

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um índice melhora relatório diário, mas piora carga horária. Qual métrica deve orientar a decisão?

A) Somente o menor tempo do relatório.

B) Impacto acumulado, frequência, criticidade, espaço e estabilidade nos dois fluxos.

C) Somar apenas a quantidade de execuções, ignorando duração, escrita, espaço e criticidade.

D) Considerar somente o fluxo mais frequente, mesmo que o relatório tenha requisito crítico de prazo.

### S3D6Q288 — Fluxo do otimizador

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Em um modelo simplificado, depois de gerar caminhos e estimar custos, o otimizador:

A) altera a regra de negócio.

B) garante o menor tempo possível em qualquer parâmetro.

C) escolhe um plano, que na execução produzirá métricas reais comparáveis às estimativas.

D) descarta as estatísticas.

### S3D6Q289 — Parâmetros representativos

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Para comparar antes e depois de uma mudança, deve-se:

A) usar parâmetros extremos diferentes para favorecer a versão nova.

B) comparar ambientes e volumes distintos.

C) olhar apenas o custo estimado.

D) manter cenário e parâmetros representativos, registrando tempo, buffers e demais métricas pertinentes.

### S3D6Q290 — Decisão baseada em evidência

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual registro encerra adequadamente um teste de otimização?

A) Hipótese, mudança única, medidas comparáveis, custo colateral e decisão de manter ou reverter.

B) “Ficou mais rápido” sem ambiente ou valor.

C) Um print do operador mais caro, sem contexto.

D) A quantidade de índices criados.

### S3D6Q291 — Comparação versionada

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Qual prática evita generalização incorreta ao comparar PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS?

A) Comparar nomes parecidos e presumir comportamento idêntico.

B) Usar a sintaxe de um produto como padrão dos demais.

C) Fixar versão, conceito, produto, configuração e engine quando relevante.

D) Ignorar documentação do fornecedor.

### S3D6Q292 — TOP e portabilidade

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

A afirmação “`SELECT TOP (10)` funciona sem mudança nos três SGBDs” é:

A) verdadeira, porque todos limitam linhas.

B) verdadeira apenas sem `ORDER BY`.

C) falsa porque nenhum dos três limita linhas.

D) falsa: `TOP` é T-SQL; PostgreSQL e MySQL normalmente usam `LIMIT`, com alternativas padronizadas conforme suporte.

### S3D6Q293 — Organização física principal

**Nível:** Médio

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Qual comparação corresponde ao quadro estudado?

A) Os três organizam obrigatoriamente os dados pela chave primária.

B) PostgreSQL usa heap com índices separados na forma comum; SQL Server pode ter heap ou clustered; no InnoDB, a PK definida é clustered, com fallback para `UNIQUE NOT NULL` adequado ou índice oculto quando ela não existe.

C) SQL Server não possui índice nonclustered.

D) InnoDB sempre usa heap sem relação com a chave primária.

### S3D6Q294 — Forma de obter plano

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Assinale a associação correta.

A) PostgreSQL e MySQL: `EXPLAIN [ANALYZE]`; SQL Server: planos estimado e real nas ferramentas.

B) SQL Server: apenas `EXPLAIN ANALYZE`; PostgreSQL: nenhum plano.

C) MySQL 9.7 LTS não oferece `EXPLAIN`.

D) Os três exigem a mesma sintaxe.

### S3D6Q295 — Engine no MySQL

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Por que registrar o engine ao descrever comportamento do MySQL?

A) Porque concorrência, organização e outros recursos podem depender do mecanismo; não se deve atribuir a todo MySQL uma propriedade específica do InnoDB.

B) Porque o engine muda a semântica do SQL padrão em todos os comandos.

C) Porque versão deixa de importar quando o engine é conhecido.

D) Porque PostgreSQL e SQL Server usam obrigatoriamente InnoDB.

### S3D6Q296 — Definição de BI

**Nível:** Médio

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Business Intelligence é melhor definido como:

A) sinônimo de dashboard.

B) combinação de processos, dados, modelos, pessoas e ferramentas para apoiar análise e decisão.

C) um único SGBD operacional.

D) a etapa de carga de um ETL.

### S3D6Q297 — OLTP e OLAP

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Qual par de perguntas exemplifica, respectivamente, OLTP e OLAP?

A) “Como evoluiu por mês?” e “qual pedido está aberto agora?”.

B) “Qual é a tendência anual?” e “qual a média histórica?”.

C) “Qual é o estado deste pedido?” e “como o tempo médio evoluiu por unidade e mês?”.

D) “Qual dashboard existe?” e “qual tabela possui PK?”.

### S3D6Q298 — Grão antes das medidas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Uma fonte possui várias interações por protocolo, mas o indicador deve contar atendimentos concluídos. Qual grão evita duplicidade?

A) Uma linha por arquivo recebido.

B) Uma linha por interação, somando todas como atendimento.

C) Uma linha por dimensão.

D) Uma linha por atendimento concluído, com medidas definidas nesse nível.

### S3D6Q299 — Média de médias

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

A unidade A tem 2 atendimentos com média de 10 min; B tem 18 com média de 20 min. A média global correta é:

A) 15 min, média simples das duas médias.

B) 19 min: `(2×10 + 18×20) / 20`.

C) 20 min, porque o maior grupo prevalece integralmente.

D) 30 min, soma das médias.

### S3D6Q300 — ETL e ELT

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Qual distinção é correta?

A) ETL carrega antes de transformar; ELT transforma antes de carregar.

B) ETL e ELT são nomes do data warehouse.

C) ETL transforma antes da carga no destino analítico final; ELT carrega e transforma no destino.

D) ELT dispensa qualidade, linhagem e reconciliação.

## Questões extras — Dia 6

#### Extra Dia 6.1 — Negação de conjunção

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Leis de De Morgan
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

A consulta é rápida e o índice é pequeno. Qual é a negação lógica?

A) A consulta não é rápida e o índice não é pequeno.

B) A consulta é rápida ou o índice é pequeno.

C) A consulta não é rápida ou o índice não é pequeno.

D) Se a consulta é rápida, o índice não é pequeno.

#### Extra Dia 6.2 — Negação da implicação

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Implicação
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Negue: “Se o plano usa índice, então o tempo diminui”.

A) O plano usa índice e o tempo não diminui.

B) O plano não usa índice e o tempo diminui.

C) Se o tempo não diminui, o plano não usa índice.

D) O plano não usa índice ou o tempo diminui.

#### Extra Dia 6.3 — Negação do universal

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Quantificadores
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Qual é a negação de “Todo relatório possui fonte identificada”?

A) Nenhum relatório possui fonte identificada.

B) Todo relatório não possui fonte identificada.

C) Algum relatório possui fonte identificada.

D) Existe pelo menos um relatório que não possui fonte identificada.

#### Extra Dia 6.4 — União de conjuntos

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Inclusão-exclusão
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Em 80 consultas, 50 usam filtro por data, 35 usam filtro por status e 20 usam ambos. Quantas usam ao menos um dos dois filtros?

A) 105.

B) 65.

C) 45.

D) 85.

#### Extra Dia 6.5 — Percentuais sucessivos

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Porcentagem
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Um tempo de 100 ms aumenta 20% e depois diminui 20%. O resultado é:

A) 100 ms, porque os percentuais se anulam.

B) 96 ms, pois `100×1,20×0,80=96`.

C) 80 ms.

D) 104 ms.

#### Extra Dia 6.6 — Sugestão, comentário e edição

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Modos de colaboração
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Qual distinção é correta?

A) Comentário altera diretamente o texto; edição apenas discute.

B) Sugestão e edição são sempre idênticas.

C) Histórico de versões é um tipo de comentário.

D) Sugestão propõe mudança sujeita a aceite; comentário discute; edição altera diretamente.

#### Extra Dia 6.7 — Histórico de versões

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Versões e permissões
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

O histórico de versões permite:

A) localizar estados anteriores a quem possui permissão adequada.

B) mostrar apenas a versão atual, sem permitir comparação com estados anteriores.

C) localizar estado anterior somente quando cada versão tiver sido renomeada ou copiada manualmente.

D) restaurar automaticamente uma versão antiga para todos os colaboradores assim que o histórico é aberto.

#### Extra Dia 6.8 — Título semântico

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Estilos
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Por que aplicar estilo de título é diferente de apenas aumentar a fonte?

A) Porque fonte grande bloqueia edição.

B) Porque estilo remove o texto do histórico.

C) Porque o estilo cria estrutura semântica; tamanho isolado muda aparência.

D) Porque título não pode ter fonte grande.

#### Extra Dia 6.9 — Referência relativa

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Ao copiar de C2 para D3 uma fórmula que contém `A2`, a referência relativa torna-se:

A) `$A$2`.

B) `A2`.

C) `B2`.

D) `B3`.

#### Extra Dia 6.10 — Referência absoluta

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Ao copiar uma fórmula, qual referência mantém coluna A e linha 2 fixas?

A) `A2`.

B) `$A$2`.

C) `$A2`.

D) `A$2`.

#### Extra Dia 6.11 — Referência mista copiada

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referência mista
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Em C2, `=$A2*B$1` é copiada para D3. Qual fórmula resulta?

A) `=$B3*C$2`.

B) `=$A2*B$1`.

C) `=$A3*C$1`.

D) `=A3*$C1`.

#### Extra Dia 6.12 — Ordenação segura

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Ordenação de tabela
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Uma planilha possui nome, matrícula e nota na mesma linha. Para ordenar por nota sem romper os registros, deve-se:

A) selecionar o intervalo ou tabela completo e ordenar as linhas pela coluna de nota.

B) ordenar somente as células da coluna nota.

C) copiar as notas para outra aba e apagar a origem.

D) fixar todas as referências com cifrão.

#### Extra Dia 6.13 — Função e configuração regional

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Localização de fórmulas
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Ao interpretar fórmula de outra configuração regional, é correto lembrar que:

A) nome de função e separador podem variar; finalidade e referências devem ser analisadas.

B) toda fórmula usa obrigatoriamente vírgula.

C) referências relativas deixam de existir.

D) o resultado depende apenas do idioma do navegador.

#### Extra Dia 6.14 — HTTPS e navegação privada

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Transporte e privacidade
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Qual afirmação é correta?

A) HTTPS garante que todo conteúdo é legítimo.

B) Navegação privada oculta a conexão do site.

C) Modo privado substitui certificado.

D) HTTPS protege o transporte, e modo privado reduz certos registros locais; nenhum dos dois garante legitimidade total ou anonimato.

#### Extra Dia 6.15 — Credencial e host

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Verificação de destino
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Um site visualmente idêntico ao oficial, em host diferente, pede senha e exibe cadeado. O usuário deve:

A) confiar no logotipo.

B) verificar host, origem e canal oficial antes de inserir credencial; TLS pode proteger conexão com o destinatário errado.

C) ativar histórico para validar a instituição.

D) limpar cache e inserir a senha.

#### Extra Dia 6.16 — Concordância com sujeito distante

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Concordância
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Assinale a frase com concordância adequada.

A) A análise dos indicadores demonstram avanços.

B) Os uso responsável dos dados melhora decisões.

C) A qualidade dos registros e a clareza dos critérios fortalecem a confiança.

D) Existe direitos que precisam ser preservado.

#### Extra Dia 6.17 — Crase e regência

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Regência e crase
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Assinale a frase adequada.

A) A política visa à melhorar os serviços.

B) A administração informou à todos os critérios.

C) Os gestores obedeceram as normas aplicáveis.

D) A instituição deu transparência às decisões e garantiu respeito aos direitos.

#### Extra Dia 6.18 — Vírgula entre sujeito e verbo

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Pontuação
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Qual frase evita separar indevidamente sujeito e verbo?

A) O uso responsável de dados pode elevar a eficiência sem reduzir a proteção de direitos.

B) A análise dos registros, permite corrigir falhas.

C) A transparência e a proteção, fortalecem a confiança.

D) Os critérios usados pela instituição, devem ser explicados.

#### Extra Dia 6.19 — Coerência e referência

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Progressão textual
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Qual reescrita mantém referente claro e relação de contraste?

A) A gestão ampliou a coleta, porque ela eliminou todo risco.

B) Os dados e a instituição melhoraram, pois eles era claros.

C) A coleta aumentou; contudo, esse aumento não dispensa critérios transparentes e proteção de direitos.

D) A gestão coletou dados, portanto eles talvez, mas nunca.

#### Extra Dia 6.20 — Conclusão da dissertação

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Fechamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Qual conclusão atende ao protocolo do texto integral?

A) Introduz uma terceira tese sobre aquisição de servidores.

B) Retoma a tese condicionada, sintetiza eficiência, direitos e confiança e fecha sem argumento novo.

C) Lista comandos SQL para demonstrar conhecimento técnico.

D) Afirma que todo risco será eliminado definitivamente.

## Gabarito — Dia 6

### Principais

| S3D6Q251 | S3D6Q252 | S3D6Q253 | S3D6Q254 | S3D6Q255 | S3D6Q256 | S3D6Q257 | S3D6Q258 | S3D6Q259 | S3D6Q260 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | C | A | B | B | D | C | A | A | D |

| S3D6Q261 | S3D6Q262 | S3D6Q263 | S3D6Q264 | S3D6Q265 | S3D6Q266 | S3D6Q267 | S3D6Q268 | S3D6Q269 | S3D6Q270 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | C | C | A | D | B | D | C | A | B |

| S3D6Q271 | S3D6Q272 | S3D6Q273 | S3D6Q274 | S3D6Q275 | S3D6Q276 | S3D6Q277 | S3D6Q278 | S3D6Q279 | S3D6Q280 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | C | B | D | A | A | C |

| S3D6Q281 | S3D6Q282 | S3D6Q283 | S3D6Q284 | S3D6Q285 | S3D6Q286 | S3D6Q287 | S3D6Q288 | S3D6Q289 | S3D6Q290 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | D | A | C | B | B | C | D | A |

| S3D6Q291 | S3D6Q292 | S3D6Q293 | S3D6Q294 | S3D6Q295 | S3D6Q296 | S3D6Q297 | S3D6Q298 | S3D6Q299 | S3D6Q300 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | D | B | A | A | B | C | D | B | C |

### Extras

| 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | 6.6 | 6.7 | 6.8 | 6.9 | 6.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | B | B | D | A | C | D | B |

| 6.11 | 6.12 | 6.13 | 6.14 | 6.15 | 6.16 | 6.17 | 6.18 | 6.19 | 6.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | A | D | B | C | D | A | C | B |

## Comentários — Dia 6

### Comentário S3D6Q251

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Constraint é regra, não definição de índice.
- **B)** Incorreta. Índice também custa manutenção.
- **C)** Incorreta. A escolha continua baseada em custo.
- **D)** Correta. Estrutura auxiliar troca menor trabalho de certas leituras por custos próprios.

**Conceito:** Índice como caminho de acesso.

**Pegadinha:** Tratá-lo como gratuito ou obrigatório.

**Como pensar:** Avalie benefício de leitura e custo de manter a estrutura.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Índice como caminho com custo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q252

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Hash não preserva ordem para faixa.
- **B)** Incorreta. B-tree também atende igualdade.
- **C)** Correta. B-tree apoia igualdade/faixa; hash tipicamente igualdade completa.
- **D)** Incorreta. Disponibilidade e sintaxe de hash variam por produto.

**Conceito:** B-tree versus hash.

**Pegadinha:** Universalizar comportamento de fornecedor.

**Como pensar:** Pergunte se o acesso exige ordem ou apenas igualdade exata.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “B-tree e hash”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q253

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Usa as duas primeiras colunas contínuas do índice.
- **B)** Incorreta. Ignora a coluna mais à esquerda.
- **C)** Incorreta. Usa apenas a terceira coluna.
- **D)** Incorreta. Começa na segunda coluna.

**Conceito:** Prefixo à esquerda.

**Pegadinha:** Contar condições sem olhar a ordem física.

**Como pensar:** Leia o índice da esquerda até a primeira lacuna.

### Comentário S3D6Q254

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O índice ainda pode oferecer algum caminho.
- **B)** Correta. Uf pode ajudar, e nome pode ter aproveitamento limitado; custo decide o plano.
- **C)** Incorreta. A lacuna em status quebra a continuidade completa.
- **D)** Incorreta. A estrutura não se converte automaticamente.

**Conceito:** Lacuna em índice composto.

**Pegadinha:** Declarar uso impossível ou completo em termos absolutos.

**Como pensar:** Separe ordem física útil de decisão final do otimizador.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Salto de coluna no índice composto”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q255

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Clustered depende do produto e não decorre da cobertura.
- **B)** Correta. Cobertura é relativa às colunas exigidas pela consulta.
- **C)** Incorreta. Não há regra de domínio.
- **D)** Incorreta. Cobrir não força o plano.

**Conceito:** Índice cobridor.

**Pegadinha:** Atribuir cobertura à tabela inteira.

**Como pensar:** Liste filtro, junção e saída daquela consulta.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Cobertura depende da consulta”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q256

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Forçar ignora custo e proporção.
- **B)** Incorreta. Um `WHERE` não torna o predicado seletivo; aqui ele preserva 96% das linhas.
- **C)** Incorreta. Baixa cardinalidade isolada não proíbe uso em composição, cobertura ou subconjunto raro.
- **D)** Correta. Ler quase tudo por scan pode custar menos que acessos dispersos.

**Conceito:** Seletividade e scan.

**Pegadinha:** Indexar toda coluna do where.

**Como pensar:** Estime a fração retornada e o custo para buscar a linha base.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Baixa seletividade e scan”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q257

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A função oculta a coluna na forma convencional.
- **B)** Incorreta. Conversão para texto também transforma a chave.
- **C)** Correta. No SQL conceitual, o intervalo expõe limites ordenados da coluna; a forma do literal deve ser adaptada ao dialeto.
- **D)** Incorreta. O cálculo ainda envolve a coluna.

**Conceito:** Sargabilidade por intervalo.

**Pegadinha:** Preservar função por parecer mais legível.

**Como pensar:** Reescreva o critério como limites inferior e superior da chave e alinhe seus tipos à sintaxe do produto.

### Comentário S3D6Q258

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O próximo ano exclusivo cobre todos os horários de 31/12 no tipo temporal delimitado, com sintaxe adaptada ao produto.
- **B)** Incorreta. B-tree aceita datas de qualquer mês.
- **C)** Incorreta. Faixa continua sendo faixa.
- **D)** Incorreta. Between funciona, mas um fim à meia-noite pode excluir horários.

**Conceito:** Limite superior exclusivo.

**Pegadinha:** Usar data final sem considerar tempo e precisão.

**Como pensar:** Feche o intervalo no primeiro instante que não pertence ao período e escreva o limite no tipo/dialeto correto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Limite superior exclusivo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q259

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cada escrita pode precisar manter a nova estrutura.
- **B)** Incorreta. Índice possui custo real.
- **C)** Incorreta. Estatísticas continuam relevantes.
- **D)** Incorreta. Índice não muda a semântica lógica correta.

**Conceito:** Custo de escrita do índice.

**Pegadinha:** Medir apenas select.

**Como pensar:** Inclua insert, update, delete, espaço e estatísticas na conta.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Custo colateral de índice”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q260

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Os conceitos podem se relacionar sem serem sinônimos.
- **B)** Incorreta. Inverte regra lógica e mecanismo.
- **C)** Incorreta. Constraints podem ser apoiadas por índices.
- **D)** Correta. Distingue intenção lógica e implementação física.

**Conceito:** Constraint versus índice.

**Pegadinha:** Inferir equivalência porque o produto cria índice para unique.

**Como pensar:** Pergunte o que deve ser verdadeiro e qual estrutura ajuda a garantir.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Constraint e índice”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q261

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. B-tree também serve a leituras.
- **B)** Correta. Ordem das chaves pode apoiar faixa e ordenação compatível.
- **C)** Incorreta. Não corrige qualquer expressão automaticamente.
- **D)** Incorreta. Não executa join sem ler dados.

**Conceito:** Ordenação em B-tree.

**Pegadinha:** Reduzir B-tree a igualdade.

**Como pensar:** Compare a ordem solicitada com a ordem das chaves.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “B-tree e ordenação”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q262

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Hash não se limita a texto.
- **B)** Incorreta. Faixa pode usar B-tree.
- **C)** Correta. Sem ordem, não há percurso natural do intervalo.
- **D)** Incorreta. B-tree também aceita igualdade.

**Conceito:** Hash e intervalos.

**Pegadinha:** Associar hash a rapidez universal.

**Como pensar:** Faixa exige relação de ordem entre as chaves.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Hash e faixa”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q263

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Baixa seletividade não cria proibição eterna.
- **B)** Incorreta. Posição depende da carga.
- **C)** Correta. A coluna pode contribuir no contexto da consulta.
- **D)** Incorreta. Índice não vira constraint por cardinalidade.

**Conceito:** Seletividade contextual.

**Pegadinha:** Julgar coluna isoladamente.

**Como pensar:** Avalie combinação, cobertura, ordenação e subconjunto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Coluna pouco seletiva em composição”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q264

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Observação ausente do índice pode exigir acesso à tabela em B.
- **B)** Incorreta. Cobrir uma consulta não significa cobrir todas.
- **C)** Incorreta. Mesmo em produto que suporte `INCLUDE`, a cláusula não obriga a escolha do índice.
- **D)** Incorreta. A estrutura ainda custa na escrita.

**Conceito:** Cobertura relativa à projeção.

**Pegadinha:** Esquecer colunas de saída.

**Como pensar:** Compare toda necessidade de A e B com as colunas do índice.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Cobertura relativa”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q265

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Começa por status sem considerar o padrão informado.
- **B)** Incorreta. Faixa antes das igualdades pode limitar o prefixo.
- **C)** Incorreta. Vários índices isolados não equivalem ao composto nem dispensam medição.
- **D)** Correta. Igualdades primeiro e data depois formam candidato coerente, ainda sujeito a teste.

**Conceito:** Desenho de índice composto.

**Pegadinha:** Ordenar apenas por cardinalidade.

**Como pensar:** Parta das consultas reais: igualdades conjuntas, depois faixa/ordem.

### Comentário S3D6Q266

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Equivalência dos valores não impede que converter a coluna esconda a chave do caminho convencional.
- **B)** Correta. Converter a chave em cada linha pode impedir busca eficiente.
- **C)** Incorreta. A existência do índice não obriga o produto a mover a conversão para a entrada.
- **D)** Incorreta. Outro índice não remove a expressão aplicada à coluna no predicado.

**Conceito:** Conversão implícita e sargabilidade.

**Pegadinha:** Ignorar tipos no predicado.

**Como pensar:** Alinhe o tipo do parâmetro ao tipo da coluna indexada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Conversão implícita e busca”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q267

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Igualdade oferece busca precisa.
- **B)** Incorreta. Faixa pode aproveitar ordem.
- **C)** Incorreta. Prefixo conhecido pode ser buscável.
- **D)** Correta. Curinga inicial esconde o começo necessário ao percurso convencional.

**Conceito:** LIKE e prefixo.

**Pegadinha:** Tratar todos os padrões LIKE igualmente.

**Como pensar:** Veja se a parte inicial da chave é conhecida.

### Comentário S3D6Q268

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Função não cria chave primária.
- **B)** Incorreta. Expressões podem ter suporte específico.
- **C)** Correta. Índice compatível com a expressão muda o cenário.
- **D)** Incorreta. Índice alheio não resolve automaticamente.

**Conceito:** Índice por expressão.

**Pegadinha:** Aplicar a heurística como lei universal.

**Como pensar:** Pergunte se existe estrutura criada para exatamente aquela expressão.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Índice por expressão”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q269

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Poucas páginas e retorno total podem tornar scan mais barato.
- **B)** Incorreta. Escolha de scan não prova corrupção.
- **C)** Incorreta. Dica sem evidência é prematura.
- **D)** Incorreta. Plano físico não muda resposta lógica.

**Conceito:** Escolha baseada em custo.

**Pegadinha:** Eliminar qualquer scan visual.

**Como pensar:** Compare número de páginas e fração de linhas necessárias.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Índice não garante uso”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q270

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Uma leitura isolada não domina todo o serviço.
- **B)** Correta. A decisão deve ponderar frequência e custos dos dois fluxos.
- **C)** Incorreta. Remover constraints troca desempenho por invalidade potencial.
- **D)** Incorreta. Uma métrica não encerra a otimização.

**Conceito:** Trade-off leitura e escrita.

**Pegadinha:** Celebrar o melhor número isolado.

**Como pensar:** Calcule impacto acumulado por frequência e criticidade.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Diagnóstico integrado de índice”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q271

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Custo não é cronômetro universal.
- **B)** Correta. É valor comparativo interno entre alternativas.
- **C)** Incorreta. Estimativa não é linha real exata.
- **D)** Incorreta. Não representa diretamente CPU medida.

**Conceito:** Custo estimado.

**Pegadinha:** Ler custo como milissegundo.

**Como pensar:** Use custo para comparar planos no mesmo contexto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Custo do otimizador”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q272

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Distribuição é insumo das estimativas; estatísticas antigas podem mudar cardinalidades previstas.
- **B)** Incorreta. O efeito não se limita à apresentação: estimativas orientam a escolha do plano.
- **C)** Incorreta. Linhas reais continuam sendo produzidas na execução; o problema está na previsão usada para planejar.
- **D)** Correta. Cardinalidade errada distorce ordem e método escolhidos.

**Conceito:** Estatísticas e estimativa.

**Pegadinha:** Olhar apenas para o operador final.

**Como pensar:** Rastreie de onde veio a primeira estimativa ruim.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Estatísticas desatualizadas”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q273

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A discrepância maciça pede investigar estatística, correlação ou predicado.
- **B)** Incorreta. Atualizar estatísticas é hipótese, não encerramento; a nova estimativa precisa ser conferida.
- **C)** Incorreta. Forçar hash join atua depois da estimativa e pode mascarar a causa sem corrigi-la.
- **D)** Incorreta. Índices indiscriminados não explicam nem necessariamente corrigem distribuição ou correlação.

**Conceito:** Estimado versus real.

**Pegadinha:** Forçar operador antes de corrigir a causa.

**Como pensar:** Comece no primeiro nó em que estimado e real divergem.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Estimado versus real”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q274

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Índice não é condição absoluta.
- **B)** Incorreta. Duas entradas enormes podem tornar o loop caro.
- **C)** Correta. Poucas linhas externas e acesso interno eficiente favorecem o método.
- **D)** Incorreta. Não se limita a condições sem igualdade.

**Conceito:** Nested loop contextual.

**Pegadinha:** Rotular loop como sempre lento.

**Como pensar:** Multiplique aproximadamente linhas externas pelo custo do acesso interno.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Nested loop contextual”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q275

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O operador pode construir sua própria estrutura em memória.
- **B)** Incorreta. Ordenação prévia caracteriza mais o merge.
- **C)** Correta. Igualdade e conjuntos relevantes podem favorecer hash sem índice hash.
- **D)** Incorreta. Nenhum método é sempre superior.

**Conceito:** Hash join.

**Pegadinha:** Confundir hash join com índice hash.

**Como pensar:** Separe estrutura transitória do operador e índice persistente.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Hash join”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q276

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Predicado incompatível não favorece o método.
- **B)** Correta. Ordem disponível e condição compatível podem torná-lo vantajoso.
- **C)** Incorreta. Sem relação não há junção significativa.
- **D)** Incorreta. Índice hash não é requisito.

**Conceito:** Merge join.

**Pegadinha:** Supor ordenação obrigatória durante toda execução.

**Como pensar:** Veja se as entradas já chegam na ordem necessária.

### Comentário S3D6Q277

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Where não torna índice obrigatório.
- **B)** Incorreta. Chave primária não impede scan.
- **C)** Incorreta. Sargabilidade não é o único fator.
- **D)** Correta. Tabela pequena ou retorno amplo podem favorecer leitura sequencial.

**Conceito:** Scan baseado em custo.

**Pegadinha:** Usar a palavra scan como diagnóstico completo.

**Como pensar:** Calcule tamanho e proporção visitada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Scan não é falha automática”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q278

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Operador seletivo no nome pode ainda processar volume e acessos caros.
- **B)** Incorreta. Seek não certifica plano ótimo.
- **C)** Incorreta. Plano físico não muda resultado lógico.
- **D)** Incorreta. Estatísticas continuam orientando estimativas.

**Conceito:** Seek e trabalho total.

**Pegadinha:** Avaliar plano por um único rótulo.

**Como pensar:** Siga linhas, loops e acessos até o custo acumulado.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Seek não garante rapidez”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q279

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A divergência cedo na árvore pode contaminar escolhas posteriores.
- **B)** Incorreta. Percentual estimado não supera uma divergência real que contamina os nós posteriores.
- **C)** Incorreta. Scan barato não é falha.
- **D)** Incorreta. Posição visual não garante que o nó seja a origem da primeira estimativa incorreta.

**Conceito:** Discrepância cardinal.

**Pegadinha:** Escolher operador visualmente chamativo.

**Como pensar:** Localize o primeiro grande desvio estimado-real.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Maior discrepância no plano”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q280

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. SQL Server não usa essa sintaxe genérica como os outros.
- **B)** Incorreta. Analyze executa para produzir métricas no PostgreSQL.
- **C)** Correta. A comparação fixa PostgreSQL 18.4, MySQL 9.7 LTS e SQL Server 2025 17.x e preserva suas interfaces próprias.
- **D)** Incorreta. Plano real exige execução do trabalho medido.

**Conceito:** Planos nos três SGBDs.

**Pegadinha:** Transportar sintaxe entre dialetos.

**Como pensar:** Fixe produto e distinga estimativa de execução.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “EXPLAIN nos três produtos”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q281

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. DML pode ter plano.
- **B)** Correta. Métrica real pode executar a alteração; o teste precisa de controle.
- **C)** Incorreta. Plano não concede commit automaticamente.
- **D)** Incorreta. Estatística não elimina rollback.

**Conceito:** Cuidado com plano real de DML.

**Pegadinha:** Tratar análise como leitura inofensiva.

**Como pensar:** Antes de medir, determine se a ferramenta executará a instrução.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Plano real e DML”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q282

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Começa pela solução sem diagnóstico.
- **B)** Incorreta. Muda fatores demais e cenário.
- **C)** Incorreta. Mede tarde e destrói evidência.
- **D)** Correta. A sequência preserva linha de base, hipótese e comparação.

**Conceito:** Protocolo de otimização.

**Pegadinha:** Criar índice antes de formular hipótese.

**Como pensar:** Registre o antes, mude uma coisa e repita a mesma medida.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Protocolo de otimização”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q283

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não é objetivo reduzir a linguagem.
- **B)** Incorreta. Nenhuma mudança garante ganho.
- **C)** Incorreta. Plano real ainda é necessário.
- **D)** Correta. Isola causalidade operacional e facilita reversão.

**Conceito:** Mudança controlada.

**Pegadinha:** Aplicar pacote de alterações e atribuir ganho a uma delas.

**Como pensar:** Faça experimento com uma variável.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Uma mudança por vez”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q284

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Dica pode cristalizar escolha e esconder estimativa ruim.
- **B)** Incorreta. Dicas não são sempre erro sintático.
- **C)** Incorreta. Produtos possuem recursos diversos.
- **D)** Incorreta. Dica não atualiza estatística.

**Conceito:** Uso responsável de hints.

**Pegadinha:** Forçar o operador desejado pelo olhar.

**Como pensar:** Investigue a causa antes de restringir o otimizador.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Dicas de plano”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q285

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Sem indício de mudança recente, não se pode declarar desatualização como causa necessária.
- **B)** Incorreta. Maior amostra por coluna não representa automaticamente a dependência entre UF e cidade.
- **C)** Correta. Dependência entre cidade e UF pode invalidar independência assumida.
- **D)** Incorreta. Mudar o join não corrige a cardinalidade já estimada no filtro correlacionado.

**Conceito:** Correlação estatística.

**Pegadinha:** Atacar operador posterior.

**Como pensar:** Corrija a estimativa na origem e então reavalie o plano.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Correlação entre colunas”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q286

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Índices adicionais podem custar mais que ler poucas páginas.
- **B)** Correta. Aceita o plano quando os dados justificam.
- **C)** Incorreta. Nested loop não substitui scan da entrada.
- **D)** Incorreta. Desnormalização não é resposta à palavra scan.

**Conceito:** Scan de tabela pequena.

**Pegadinha:** Otimizar aparência do plano.

**Como pensar:** Compare páginas totais com acessos alternativos.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Tabela de 40 linhas”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q287

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Relatório isolado não mede custo total.
- **B)** Correta. Frequência e criticidade convertem latências em impacto real.
- **C)** Incorreta. Quantidade de execuções sem duração, escrita, espaço e criticidade não mede impacto acumulado.
- **D)** Incorreta. Frequência não elimina o SLA do fluxo menos frequente e potencialmente crítico.

**Conceito:** Custo global.

**Pegadinha:** Escolher a métrica que mais melhorou.

**Como pensar:** Pondere cada fluxo por frequência e importância.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Custo global do serviço”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q288

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Otimizador não redefine negócio.
- **B)** Incorreta. Estimativa não garante ótimo universal.
- **C)** Correta. Plano escolhido produz dados reais para comparação.
- **D)** Incorreta. Estatísticas continuam sendo insumo.

**Conceito:** Fluxo de otimização.

**Pegadinha:** Confundir escolha estimada com certeza.

**Como pensar:** Compare a expectativa do plano com a execução observada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Fluxo do otimizador”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q289

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Parâmetros diferentes enviesam a comparação.
- **B)** Incorreta. Ambiente distinto destrói a linha de base.
- **C)** Incorreta. Custo estimado sozinho é insuficiente.
- **D)** Correta. Mesmo cenário e parâmetros tornam as métricas comparáveis.

**Conceito:** Experimento reproduzível.

**Pegadinha:** Mudar a carga junto da solução.

**Como pensar:** Congele o cenário antes e depois.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Parâmetros representativos”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q290

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O registro liga hipótese, evidência, efeito lateral e decisão.
- **B)** Incorreta. Frase sem medida não é reprodutível.
- **C)** Incorreta. Um nó isolado perde contexto.
- **D)** Incorreta. Quantidade de índices não indica qualidade.

**Conceito:** Decisão documentada.

**Pegadinha:** Encerrar com sensação subjetiva.

**Como pensar:** Escreva por que manteve ou reverteu com números comparáveis.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Decisão baseada em evidência”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q291

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Nomes semelhantes podem esconder garantias diferentes.
- **B)** Incorreta. Sintaxe não é automaticamente portátil.
- **C)** Correta. Versão e contexto limitam a afirmação de modo responsável.
- **D)** Incorreta. Fonte primária continua necessária.

**Conceito:** Comparação versionada.

**Pegadinha:** Universalizar experiência de um produto.

**Como pensar:** Escreva sempre produto, versão, conceito e configuração relevante.

### Comentário S3D6Q292

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Finalidade comum não torna sintaxe comum.
- **B)** Incorreta. Order by não torna TOP portátil.
- **C)** Incorreta. Os produtos limitam linhas.
- **D)** Correta. TOP identifica T-SQL; LIMIT é usual nos outros dois.

**Conceito:** Portabilidade de limitação.

**Pegadinha:** Confundir função equivalente com mesma gramática.

**Como pensar:** Reconheça o dialeto antes de validar a instrução.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “TOP e portabilidade”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q293

**Nível:** Médio

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A organização não é idêntica nos três.
- **B)** Correta. Resume heap comum, opção clustered e a regra completa do InnoDB: PK, `UNIQUE NOT NULL` adequado ou índice oculto.
- **C)** Incorreta. SQL Server possui nonclustered.
- **D)** Incorreta. InnoDB não é heap comum nesse sentido.

**Conceito:** Organização física comparada.

**Pegadinha:** Projetar o modelo clustered em todos.

**Como pensar:** Associe cada afirmação ao produto e ao engine e confira o fallback quando não houver PK explícita.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Organização física principal”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q294

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É a associação versionada ensinada.
- **B)** Incorreta. PostgreSQL oferece explain e SQL Server possui planos.
- **C)** Incorreta. MySQL atual oferece explain.
- **D)** Incorreta. A sintaxe e ferramentas não são idênticas.

**Conceito:** Obtenção de planos.

**Pegadinha:** Copiar comando entre dialetos.

**Como pensar:** Compare o mesmo conceito por interfaces próprias.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Forma de obter plano”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q295

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. InnoDB possui comportamentos que não devem ser atribuídos a qualquer engine.
- **B)** Incorreta. Engine não muda todo SQL padrão universalmente.
- **C)** Incorreta. Versão e engine são dimensões complementares.
- **D)** Incorreta. Os outros produtos não usam InnoDB.

**Conceito:** Escopo de afirmação no MySQL.

**Pegadinha:** Dizer “MySQL faz” quando a propriedade é do engine.

**Como pensar:** Registre versão e mecanismo antes de comparar organização ou concorrência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Engine no MySQL”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q296

**Nível:** Médio

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Dashboard é apenas uma possível interface.
- **B)** Correta. A definição inclui processo humano e técnico orientado à decisão.
- **C)** Incorreta. BI não é um banco operacional isolado.
- **D)** Incorreta. Carga é uma etapa, não o conceito inteiro.

**Conceito:** Business Intelligence.

**Pegadinha:** Reduzir BI à ferramenta visível.

**Como pensar:** Pergunte como dados se tornam análise útil para pessoas decidirem.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Definição de BI”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q297

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A ordem está invertida.
- **B)** Incorreta. Ambas são perguntas analíticas.
- **C)** Correta. Estado corrente é transacional; evolução agregada é analítica.
- **D)** Incorreta. As perguntas não distinguem as duas cargas.

**Conceito:** OLTP versus OLAP.

**Pegadinha:** Usar presença de banco como critério.

**Como pensar:** Classifique por registrar estado corrente ou analisar histórico.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “OLTP e OLAP”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q298

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Arquivo não corresponde ao evento medido.
- **B)** Incorreta. Interações duplicariam atendimentos.
- **C)** Incorreta. Dimensão não define a ocorrência do fato.
- **D)** Correta. Uma linha por atendimento concluído estabiliza contagem e espera.

**Conceito:** Granularidade da fato.

**Pegadinha:** Escolher colunas antes do grão.

**Como pensar:** Complete “uma linha representa...” antes de criar medidas.

### Comentário S3D6Q299

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Média simples dá peso igual a grupos de tamanhos distintos.
- **B)** Correta. Somar tempos 20+360 e dividir por 20 resulta em 19.
- **C)** Incorreta. O maior grupo pesa mais, mas não substitui o menor.
- **D)** Incorreta. Somar médias não produz média global.

**Conceito:** Média ponderada pelo número de fatos.

**Pegadinha:** Tratar média como plenamente aditiva.

**Como pensar:** Recupere soma e contagem de cada grupo.

### Comentário S3D6Q300

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A ordem foi invertida.
- **B)** Incorreta. Processo e repositório são conceitos diferentes.
- **C)** Correta. T antes de L define ETL; L antes de T define ELT.
- **D)** Incorreta. Ambos exigem qualidade, linhagem e reconciliação.

**Conceito:** ETL versus ELT.

**Pegadinha:** Definir pelo nome da plataforma.

**Como pensar:** Marque fisicamente onde a transformação ocorre em relação à carga final.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “ETL e ELT”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.1

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Leis de De Morgan
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Essa é a conjunção das duas negações, não a negação de uma conjunção.
- **B)** Incorreta. Mantém os termos positivos.
- **C)** Correta. Negar P e Q resulta em não P ou não Q.
- **D)** Incorreta. Cria implicação inexistente.

**Conceito:** Negação de conjunção.

**Pegadinha:** Negar termos sem trocar o conectivo.

**Como pensar:** Troque `e` por `ou` e negue ambos.

#### Comentário Extra Dia 6.2

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Implicação
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A implicação falha exatamente com antecedente verdadeiro e consequente falso.
- **B)** Incorreta. Não representa o caso de falha.
- **C)** Incorreta. É contraposição, não negação.
- **D)** Incorreta. Disjunção proposta equivale à implicação original.

**Conceito:** Negação da implicação.

**Pegadinha:** Negar os dois lados mecanicamente.

**Como pensar:** Use P e não Q.

#### Comentário Extra Dia 6.3

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Quantificadores
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. “Nenhum” é mais forte que a negação necessária.
- **B)** Incorreta. Universal negativo também é excessivo.
- **C)** Incorreta. Afirma caso positivo e não nega o universal.
- **D)** Correta. Um contraexemplo basta para negar “todo”.

**Conceito:** Negação de universal.

**Pegadinha:** Trocar todo por nenhum.

**Como pensar:** Procure um elemento da classe que não tenha a propriedade.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Negação do universal”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.4

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Inclusão-exclusão
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Soma simples conta a interseção duas vezes.
- **B)** Correta. `50+35−20=65`.
- **C)** Incorreta. Subtrai a interseção duas vezes.
- **D)** Incorreta. Ultrapassa o total do universo.

**Conceito:** União de conjuntos.

**Pegadinha:** Somar os grupos sem descontar repetição.

**Como pensar:** Some A e B e retire uma cópia da interseção.

#### Comentário Extra Dia 6.5

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Porcentagem
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Percentuais usam bases diferentes.
- **B)** Correta. Os fatores multiplicam para 0,96.
- **C)** Incorreta. O desconto não incide sobre 100.
- **D)** Incorreta. 104 corresponderia a outra combinação.

**Conceito:** Percentuais sucessivos.

**Pegadinha:** Somar +20 e −20.

**Como pensar:** Aplique cada fator ao resultado anterior.

#### Comentário Extra Dia 6.6

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Modos de colaboração
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Comentário discute e não edita diretamente.
- **B)** Incorreta. Sugestão e edição têm efeitos diferentes.
- **C)** Incorreta. Histórico não é comentário.
- **D)** Correta. A alternativa separa proposta, discussão e alteração direta.

**Conceito:** Colaboração no Documentos.

**Pegadinha:** Confundir intenção com efeito no texto.

**Como pensar:** Pergunte se o conteúdo mudou, aguarda aceite ou apenas recebeu debate.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Sugestão, comentário e edição”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.7

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Versões e permissões
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Permissão adequada permite localizar estados anteriores.
- **B)** Incorreta. A função do histórico é justamente comparar estados anteriores, não exibir só o atual.
- **C)** Incorreta. O registro de versões não depende de renomear ou copiar manualmente cada estado.
- **D)** Incorreta. Abrir o histórico não restaura versão nem impõe mudança automática aos colaboradores.

**Conceito:** Histórico de versões.

**Pegadinha:** Imaginar acesso irrestrito a qualquer pessoa.

**Como pensar:** Considere a função e a permissão do usuário.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Histórico de versões”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.8

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Estilos
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Fonte grande não bloqueia edição.
- **B)** Incorreta. Estilo não apaga histórico.
- **C)** Correta. Título cria estrutura; tamanho isolado é aparência.
- **D)** Incorreta. Título pode ter qualquer formatação compatível.

**Conceito:** Estilo semântico.

**Pegadinha:** Confundir visual com estrutura.

**Como pensar:** Veja se o recurso cria papel de título reconhecido.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Título semântico”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.9

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Isso seria referência absoluta.
- **B)** Incorreta. A referência relativa deve se deslocar.
- **C)** Incorreta. Apenas a coluna mudou, faltando a linha.
- **D)** Correta. Uma coluna e uma linha adiante levam A2 a B3.

**Conceito:** Referência relativa.

**Pegadinha:** Mover só um componente.

**Como pensar:** Aplique ao endereço o mesmo deslocamento da cópia.

#### Comentário Extra Dia 6.10

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Nenhum componente está fixo.
- **B)** Correta. Os dois cifrões fixam coluna e linha.
- **C)** Incorreta. Fixa apenas a coluna.
- **D)** Incorreta. Fixa apenas a linha.

**Conceito:** Referência absoluta.

**Pegadinha:** Tratar referência mista como absoluta.

**Como pensar:** Leia cada cifrão somente para o componente seguinte.

#### Comentário Extra Dia 6.11

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referência mista
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Move componentes que estavam fixos.
- **B)** Incorreta. Não move as partes relativas.
- **C)** Correta. A fica fixa, linha vira 3; B vira C, linha 1 fica fixa.
- **D)** Incorreta. Perde cifrões e desloca incorretamente.

**Conceito:** Cópia de referência mista.

**Pegadinha:** Mover tudo ou nada.

**Como pensar:** Resolva coluna e linha de cada termo separadamente.

#### Comentário Extra Dia 6.12

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Ordenação de tabela
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Ordenar o conjunto preserva a correspondência das linhas.
- **B)** Incorreta. Coluna isolada separa notas de nomes.
- **C)** Incorreta. Mover dados não é necessário.
- **D)** Incorreta. Cifrões afetam fórmulas, não proteção da ordenação.

**Conceito:** Ordenação de registros.

**Pegadinha:** Tratar coluna como lista independente.

**Como pensar:** Selecione todas as colunas que compõem cada registro.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Ordenação segura”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.13

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Localização de fórmulas
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Configuração pode alterar nomes e separadores sem mudar a finalidade.
- **B)** Incorreta. Vírgula não é universal.
- **C)** Incorreta. Referências relativas continuam existindo.
- **D)** Incorreta. Idioma não é o único determinante do resultado.

**Conceito:** Localização de fórmulas.

**Pegadinha:** Julgar fórmula apenas pela grafia.

**Como pensar:** Interprete operação e referências antes do separador.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Função e configuração regional”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.14

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Transporte e privacidade
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. TLS não certifica honestidade do conteúdo.
- **B)** Incorreta. O site continua recebendo a conexão.
- **C)** Incorreta. Modo privado não substitui certificado.
- **D)** Correta. Delimita proteção de trânsito e redução de rastros locais.

**Conceito:** HTTPS e modo privado.

**Pegadinha:** Somar dois controles e inferir anonimato.

**Como pensar:** Especifique o que cada controle protege e perante quem.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “HTTPS e navegação privada”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.15

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Verificação de destino
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Logotipo pode ser copiado.
- **B)** Correta. Host e canal oficial validam o destinatário esperado.
- **C)** Incorreta. Histórico não autentica instituição.
- **D)** Incorreta. Limpar cache não transforma domínio falso em oficial.

**Conceito:** Phishing e host.

**Pegadinha:** Confiar na aparência.

**Como pensar:** Cheque o domínio antes de qualquer segredo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Credencial e host”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.16

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Concordância
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O núcleo singular “análise” exige “demonstra”.
- **B)** Incorreta. Artigo e núcleo estão sem concordância.
- **C)** Correta. Sujeito composto plural concorda com “fortalecem”.
- **D)** Incorreta. Há erros em “existem” e “preservados”.

**Conceito:** Concordância verbal e nominal.

**Pegadinha:** Concordar com o termo plural mais próximo.

**Como pensar:** Localize os núcleos do sujeito antes do verbo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Concordância com sujeito distante”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.17

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Regência e crase
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não há crase antes de infinitivo nesse uso.
- **B)** Incorreta. “Todos” não admite artigo feminino.
- **C)** Incorreta. Obedecer rege preposição a: “às normas”.
- **D)** Correta. “Às decisões” recebe preposição e artigo; “respeito aos direitos” mantém a regência adequada.

**Conceito:** Regência e crase.

**Pegadinha:** Inserir acento grave diante de qualquer complemento.

**Como pensar:** Verifique primeiro a preposição exigida e depois o artigo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Crase e regência”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.18

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Pontuação
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Sujeito e verbo permanecem unidos.
- **B)** Incorreta. A vírgula separa “análise” de “permite”.
- **C)** Incorreta. Separa sujeito composto de “fortalecem”.
- **D)** Incorreta. Separa o sujeito longo de “devem” sem intercalação.

**Conceito:** Vírgula e estrutura sintática.

**Pegadinha:** Pausar oralmente e inserir vírgula entre sujeito e verbo.

**Como pensar:** Ache o verbo e seu sujeito antes de pontuar.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Vírgula entre sujeito e verbo”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.19

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Progressão textual
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Referente e absolutismo prejudicam a frase.
- **B)** Incorreta. Há erro de concordância e pronome ambíguo.
- **C)** Correta. “Esse aumento” fixa referente e “contudo” marca contraste.
- **D)** Incorreta. O período é truncado e sem relação lógica.

**Conceito:** Coesão e contraste.

**Pegadinha:** Preservar palavras sem preservar a lógica.

**Como pensar:** Cheque referente, conector e completude do período.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Coerência e referência”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.20

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Fechamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Abre argumento novo no fechamento.
- **B)** Correta. Retoma os três eixos do tema sem acrescentar razão inédita.
- **C)** Incorreta. Jargão técnico foge da função conclusiva.
- **D)** Incorreta. Promessa absoluta excede o que o texto pode sustentar.

**Conceito:** Conclusão da dissertação.

**Pegadinha:** Usar a conclusão para estrear ideia.

**Como pensar:** Reformule a tese e sintetize, sem inaugurar outro desenvolvimento.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Conclusão da dissertação”; a extensão decorre dessa precisão técnica, não de pista formal.

---
