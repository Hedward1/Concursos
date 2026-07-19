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
