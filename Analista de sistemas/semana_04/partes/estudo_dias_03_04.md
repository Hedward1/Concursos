<a id="s4-d3-inicio"></a>
# Dia 3 - Componentes, implementação e ferramentas de apoio orientadas a objetos

## Abertura e objetivos

Ao final do dia, você deverá:

- distinguir componente, interface, porta, dependência e artefato sem confundir estrutura lógica com instalação física;
- ler e produzir um diagrama de componentes com interfaces fornecidas e requeridas;
- reconhecer dependência, realização e montagem entre elementos de software;
- ler um diagrama de implementação/deployment com nós, dispositivos, ambientes de execução, caminhos de comunicação e artefatos;
- decidir em qual nó um artefato é implantado e quais relações precisam aparecer para responder a uma pergunta arquitetural;
- escolher ferramentas de apoio para modelagem, codificação, controle de versão, construção, testes e rastreabilidade;
- manter o modelo sincronizado com decisões verificáveis, sem tratar desenho desatualizado como fonte de verdade.

## Jornada executável e ponto de parada

### Sessão A - 170 minutos

- **Bloco 1 (55 min):** componentes, interfaces, portas, dependências e conectores.
- **Bloco 2 (55 min):** implementação/deployment, nós, ambientes de execução e artefatos.
- **Bloco 3 (60 min):** ferramentas de apoio, rastreabilidade e prática integrada em cenário do CRA-PR.

**Ponto de parada:** entregar dois diagramas textuais coerentes: um de componentes que mostre contratos fornecidos/requeridos e outro de deployment que associe artefatos a nós. Para cada relação, escrever a pergunta que ela ajuda a responder e uma limitação do diagrama.

### Sessão B - 170 minutos

- **Bloco 4 (60 min):** D+21 do Dia 3 da Semana 1, D+7 do Dia 3 da Semana 3, D+2 do Dia 1 da Semana 4 e Legislação CRA/CFA.
- **Bloco 5 (30 min):** Português aplicado à precisão de referentes e paralelismo.
- **Bloco 6 (15 min):** recuperação ativa de componentes, interfaces, deployment e ferramentas.
- **Mini revisão (10 min)**, **seis Essenciais (25 min)**, **correção A-D (25 min)** e **fechamento (5 min)**.

**Regra de carga:** pare a teoria nova ao completar os 170 minutos da Sessão A. A Sessão B recupera e aplica conteúdo já ensinado; não use seu tempo para abrir novo capítulo.

### Consolidação final - 20 minutos

- registrar confiança de 0 a 3 nas seis Essenciais;
- lançar no caderno a causa de cada erro, a regra correta e um contraexemplo;
- confirmar as filas D+2, D+7 e D+21 e encerrar ao atingir **360 minutos líquidos** no dia.

<a id="s4-d3-b1"></a>
## Bloco 1 - Componentes, interfaces e dependências

<a id="s4-d3-componentes"></a>
### 1. Componente como unidade modular substituível

Na UML, um componente representa uma parte modular do sistema que encapsula conteúdo e manifesta comportamento por contratos. Ele pode representar, conforme a pergunta do modelo, um serviço, módulo, biblioteca ou subsistema. O componente é lógico: não é automaticamente um servidor, processo em execução ou arquivo instalado.

Uma boa leitura separa três perguntas:

1. **responsabilidade:** que capacidade o componente concentra;
2. **contrato:** que serviços fornece e de quais serviços necessita;
3. **realização:** quais classificadores ou artefatos concretizam sua implementação.

Coesão favorece componentes com responsabilidade reconhecível; acoplamento desnecessário aumenta o impacto de mudanças. Isso não significa buscar independência absoluta: integração exige dependências, mas elas devem aparecer por contratos explícitos.

#### Exemplo completo 1 - separar Registro de Notificações

**Situação:** um portal do CRA-PR registra solicitações e envia avisos. A equipe quer trocar o provedor de mensagens sem alterar a regra de registro.

**Dados relevantes:** Registro decide quando avisar; Notificações executa o envio; o canal pode mudar.

**Raciocínio passo a passo:** primeiro separam-se as responsabilidades; depois define-se a interface EnvioDeAviso; Notificações fornece a interface; Registro a requer; a regra de registro não conhece detalhes do provedor.

**Resposta final:** modelar Registro e Notificações como componentes ligados pelo contrato EnvioDeAviso.

**Por que funciona:** a dependência permanece, mas aponta para um contrato estável e substituível.

**Erro provável:** desenhar o servidor de e-mail como componente e misturar arquitetura lógica com topologia física.

#### Exemplo completo 2 - componente não é classe isolada

**Situação:** o sistema possui as classes Processo, RepositórioProcesso e ServiçoProcesso. Pede-se uma visão de módulos entregáveis, não de estrutura interna.

**Dados relevantes:** as classes colaboram dentro do mesmo módulo de Processos; o interesse é o contrato externo.

**Raciocínio passo a passo:** identifica-se a granularidade solicitada; agrupam-se as classes sob o componente Processos; expõe-se apenas a interface ConsultaDeProcesso; detalhes de classes ficam no diagrama de classes.

**Resposta final:** um componente Processos com interface externa, sem promover cada classe a componente.

**Por que funciona:** o modelo responde à pergunta modular e evita duplicar outra visão UML.

**Erro provável:** supor correspondência obrigatória de uma classe para um componente.

<a id="s4-d3-interfaces"></a>
### 2. Interfaces fornecidas, requeridas e portas

Uma **interface fornecida** descreve serviços que o elemento se compromete a oferecer. Uma **interface requerida** descreve serviços necessários para cumprir sua responsabilidade. A notação popular usa um círculo para a fornecida e um semicírculo para a requerida; a ligação entre contratos compatíveis é frequentemente chamada de montagem.

Uma **porta** é um ponto de interação na fronteira de um classificador. Ela pode agrupar interfaces e explicitar por onde uma comunicação entra ou sai. Porta não é sinônimo de porta TCP/UDP; o significado aqui é de modelagem UML.

Perguntas de prova:

- quem fornece o contrato e quem o consome;
- se o acoplamento está dirigido ao contrato ou à implementação concreta;
- se o diagrama mostra estrutura interna, contrato externo ou apenas instalação;
- se uma porta organiza a interação na fronteira sem revelar o interior.

#### Exemplo completo 3 - direção do contrato

**Situação:** Relatórios consulta dados consolidados produzidos por Cadastro.

**Dados relevantes:** Cadastro sabe responder à consulta; Relatórios precisa dela.

**Raciocínio passo a passo:** nomeia-se o serviço ConsultaCadastral; atribui-se a interface fornecida a Cadastro; atribui-se a requerida a Relatórios; conecta-se a compatibilidade.

**Resposta final:** Cadastro fornece ConsultaCadastral e Relatórios a requer.

**Por que funciona:** fornecedor é quem implementa o contrato; consumidor é quem depende dele.

**Erro provável:** inverter fornecida e requerida porque Relatórios inicia a chamada.

#### Exemplo completo 4 - porta de integração

**Situação:** um componente Atendimento recebe solicitações pela API e também por importação em lote. O modelo precisa mostrar dois pontos de interação, preservando o interior.

**Dados relevantes:** há contratos e protocolos de entrada distintos; a lógica interna não é objeto da visão.

**Raciocínio passo a passo:** criam-se duas portas na fronteira; associa-se a cada uma sua interface requerida/fornecida pertinente; mantém-se a implementação interna encapsulada.

**Resposta final:** portas API e Lote na fronteira de Atendimento, cada qual com seus contratos.

**Por que funciona:** a porta organiza interações sem transformá-las em componentes separados.

**Erro provável:** interpretar a porta UML como número de transporte de rede.

<a id="s4-d3-dependencias"></a>
### 3. Dependência, realização e substituição

Uma **dependência** indica que a alteração no fornecedor pode afetar o cliente que o utiliza. A seta tracejada aponta do cliente dependente para o fornecedor. Uma **realização de interface** indica que um classificador cumpre o contrato descrito pela interface. Já uma conexão de montagem une uma interface requerida a uma fornecida compatível.

O desenho não garante por si só compatibilidade semântica, disponibilidade, segurança ou desempenho. Ele declara uma relação arquitetural que precisa ser confirmada por implementação, testes e operação.

#### Exemplo completo 5 - dependência invertida corretamente

**Situação:** Cobrança usa a interface Repositório, realizada por RepositórioSQL. A equipe quer permitir uma implementação em memória para testes.

**Dados relevantes:** a regra de Cobrança não deveria depender diretamente do banco.

**Raciocínio passo a passo:** Cobrança requer Repositório; RepositórioSQL realiza o contrato; RepositórioMemória pode realizar o mesmo contrato; a seleção da implementação é externa à regra.

**Resposta final:** dependência de Cobrança para a interface, com duas realizações possíveis.

**Por que funciona:** substituição ocorre no ponto de implementação do contrato, não na regra consumidora.

**Erro provável:** desenhar dependência obrigatória de Cobrança para cada implementação concreta.

#### Exemplo completo 6 - impacto de mudança

**Situação:** o contrato de Autenticação remove uma operação usada pelo Portal e pelo Aplicativo.

**Dados relevantes:** ambos requerem a interface; Auditoria apenas recebe eventos por outro contrato.

**Raciocínio passo a passo:** seguem-se as dependências requeridas; Portal e Aplicativo são candidatos a impacto; Auditoria não é incluída apenas por estar próxima no desenho.

**Resposta final:** revisar os dois consumidores do contrato alterado e suas integrações.

**Por que funciona:** análise de impacto segue relações modeladas, não posição visual.

**Erro provável:** concluir que todo componente do diagrama é afetado igualmente.

### Síntese e pegadinhas do Bloco 1

| Elemento | Pergunta respondida | Confusão frequente |
|---|---|---|
| componente | que módulo encapsula a capacidade | tratar como servidor ou classe obrigatória |
| interface fornecida | que serviço o elemento oferece | atribuí-la a quem apenas chama |
| interface requerida | de qual serviço o elemento necessita | tratá-la como implementação |
| porta | por onde ocorre a interação na fronteira | confundir com porta de rede |
| dependência | que cliente pode ser afetado pelo fornecedor | inverter a seta |
| realização | quem cumpre o contrato | confundir com simples uso |

<a id="s4-d3-b2"></a>
## Bloco 2 - Implementação/deployment e artefatos

<a id="s4-d3-deployment"></a>
### 4. Nós, dispositivos, ambientes e caminhos de comunicação

O diagrama de deployment mostra a arquitetura de execução: onde os elementos implantáveis são posicionados e como os nós se comunicam. Um **nó** é um recurso computacional. Ele pode ser especializado como:

- **dispositivo:** recurso físico, como servidor ou terminal;
- **ambiente de execução:** plataforma que hospeda ou executa artefatos, como uma máquina virtual de aplicação ou um SGBD dentro de um dispositivo;
- **caminho de comunicação:** associação entre nós capaz de transportar a interação pertinente.

O diagrama não substitui o diagrama de rede detalhado. Ele pode mostrar comunicação necessária à implantação sem especificar cada roteador, endereço ou regra de firewall.

#### Exemplo completo 7 - três camadas físicas

**Situação:** navegador acessa aplicação, e aplicação consulta banco. O banco não deve receber conexão direta do cliente.

**Dados relevantes:** existem dispositivo do usuário, nó de aplicação e nó de dados; apenas dois caminhos são necessários.

**Raciocínio passo a passo:** posiciona-se o navegador no dispositivo cliente; implanta-se o artefato da aplicação no ambiente de execução do servidor de aplicação; posiciona-se o esquema no SGBD; desenham-se Cliente–Aplicação e Aplicação–Dados, sem Cliente–Dados.

**Resposta final:** topologia em três nós com caminho intermediado pela aplicação.

**Por que funciona:** a visão torna explícita a restrição arquitetural relevante.

**Erro provável:** usar uma dependência de componentes para representar todo vínculo físico de comunicação.

#### Exemplo completo 8 - dispositivo e ambiente de execução

**Situação:** um servidor físico hospeda duas máquinas virtuais, uma para API e outra para tarefas agendadas.

**Dados relevantes:** o hardware é comum, mas os ambientes de execução e artefatos são distintos.

**Raciocínio passo a passo:** modela-se o servidor como dispositivo; aninham-se dois ambientes de execução; implanta-se api.war no primeiro e tarefas.jar no segundo.

**Resposta final:** um dispositivo contendo dois ambientes, cada qual com seu artefato.

**Por que funciona:** separa recurso físico de contexto de execução.

**Erro provável:** desenhar as máquinas virtuais como componentes lógicos do domínio.

<a id="s4-d3-artefatos"></a>
### 5. Artefatos, manifestação e implantação

Um **artefato** é uma peça de informação física utilizada ou produzida no desenvolvimento e na implantação, como executável, pacote, biblioteca, script, arquivo de configuração ou documento. A relação de **manifestação** liga o artefato ao elemento de modelo que ele concretiza. A relação de **deployment** associa o artefato ao nó em que é implantado.

As relações respondem a perguntas diferentes:

- manifestação: que elemento lógico este arquivo concretiza;
- deployment: onde este arquivo é colocado/executado;
- dependência: quem usa ou pode ser afetado por quem.

#### Exemplo completo 9 - pacote e componente

**Situação:** cadastro-api.jar implementa o componente Cadastro e é instalado no ambiente JVM do servidor Aplicação-1.

**Dados relevantes:** há elemento lógico, arquivo físico e destino de execução.

**Raciocínio passo a passo:** liga-se o artefato ao componente por manifestação; liga-se o artefato ao ambiente JVM por deployment; não se declara que o servidor realiza a interface de Cadastro.

**Resposta final:** Cadastro ← manifestação por cadastro-api.jar → implantado em JVM/Aplicação-1.

**Por que funciona:** cada relação conserva sua semântica.

**Erro provável:** substituir o componente pelo arquivo em todas as visões.

#### Exemplo completo 10 - configuração por ambiente

**Situação:** o mesmo pacote da aplicação é implantado em homologação e produção, mas cada ambiente usa configuração própria.

**Dados relevantes:** artefato executável é comum; artefatos de configuração diferem; nós também diferem.

**Raciocínio passo a passo:** modela-se o pacote em ambos os deployments; associa-se config-hml ao nó de homologação e config-prd ao de produção; registra-se a restrição de não misturar configurações.

**Resposta final:** dois destinos de implantação com pacote comum e configurações específicas.

**Por que funciona:** torna rastreável o que é reutilizado e o que varia.

**Erro provável:** concluir que configuração é detalhe incapaz de ser representado como artefato.

### Diferenças que a banca pode explorar

| Par | Distinção decisiva |
|---|---|
| componente x nó | módulo lógico x recurso de execução |
| componente x artefato | capacidade encapsulada x peça física de informação |
| dispositivo x ambiente | recurso físico x plataforma de execução |
| manifestação x deployment | concretiza elemento x posiciona artefato |
| dependência x caminho | impacto/uso lógico x comunicação entre nós |

<a id="s4-d3-b3"></a>
## Bloco 3 - Ferramentas de apoio e prática integrada

<a id="s4-d3-ferramentas"></a>
### 6. Ferramentas ao longo da análise, projeto e codificação

Ferramenta de apoio não substitui decisão técnica. Ela reduz trabalho mecânico, preserva histórico, automatiza verificações ou conecta artefatos. O critério de escolha deve começar pela necessidade:

| Necessidade | Classe de ferramenta | Evidência esperada |
|---|---|---|
| modelar e revisar UML | modelador/CASE | diagramas versionados e consistentes |
| rastrear requisito até código e teste | repositório de requisitos/ALM | vínculos e matriz de rastreabilidade |
| editar/refatorar código | IDE | navegação, análise e refatoração controlada |
| preservar versões e colaboração | controle de versão | commits, branches e revisão |
| produzir pacote repetível | automação de build | dependências e resultado reproduzível |
| verificar comportamento | framework/gestão de testes | casos, resultados e regressão |
| integrar verificações | integração contínua | execução automática e feedback |

Forward engineering transforma modelos ou definições em esqueletos/artefatos; reverse engineering extrai uma visão a partir da implementação; round-trip tenta manter ambos sincronizados. Nenhuma dessas operações garante que o modelo expresse a intenção correta. Código gerado precisa de revisão, teste e governança.

#### Exemplo completo 11 - ferramenta escolhida pela lacuna

**Situação:** requisitos estão em planilha, commits não indicam demanda e testes não apontam requisito coberto.

**Dados relevantes:** o problema principal é rastreabilidade, não desenho UML.

**Raciocínio passo a passo:** define-se identificador de requisito; liga-se requisito a tarefa, commit e caso de teste; escolhe-se ferramenta que preserve esses vínculos; mede-se cobertura e itens órfãos.

**Resposta final:** priorizar repositório de requisitos/ALM integrado a versão e testes.

**Por que funciona:** trata a perda de vínculo observada em vez de apenas produzir mais diagramas.

**Erro provável:** adquirir modelador sofisticado sem resolver a cadeia requisito–mudança–teste.

#### Exemplo completo 12 - engenharia reversa com limite

**Situação:** sistema legado possui código, mas a documentação de classes está desatualizada.

**Dados relevantes:** a ferramenta consegue ler estruturas, mas não conhece decisões de negócio implícitas.

**Raciocínio passo a passo:** extrai-se um diagrama inicial; validam-se nomes e relações com código e equipe; removem-se detalhes irrelevantes; registram-se decisões e responsabilidades ausentes.

**Resposta final:** usar engenharia reversa como ponto de partida auditável, não como documentação final automática.

**Por que funciona:** a ferramenta recupera estrutura; revisão humana recupera intenção e escopo.

**Erro provável:** declarar que o diagrama extraído prova requisitos e arquitetura planejada.

<a id="s4-d3-pratica"></a>
### Produto obrigatório do Bloco 3

Em cenário fictício do CRA-PR:

1. modele Portal, Cadastro, Cobrança e Notificações como componentes;
2. nomeie duas interfaces fornecidas e duas requeridas;
3. indique uma dependência e uma realização;
4. manifeste dois componentes em artefatos distintos;
5. implante os artefatos em nó de aplicação e nó de dados;
6. indique os caminhos de comunicação necessários;
7. escolha uma ferramenta para modelo, uma para versão e uma para teste;
8. crie três vínculos de rastreabilidade entre requisito, componente, artefato e teste.

**Critério de aceite:** cada seta deve ter origem, destino e significado verbalizados. Se o mesmo elemento representa simultaneamente módulo, arquivo e servidor, refaça a separação.

<a id="s4-d3-b4"></a>
## Bloco 4 - Revisão programada: Legislação CRA/CFA

### Precedência da fila

1. recuperar o D+21 do Dia 3 da Semana 1, com prioridade aos erros ainda ativos;
2. executar o D+7 do Dia 3 da Semana 3;
3. concluir até quatro Essenciais abertas do Dia 1 da Semana 4, correspondentes ao D+2;
4. preservar a recuperação curta de Legislação abaixo.

<a id="s4-d3-b4-legislacao"></a>
### Fonte, âmbito, competência e finalidade - base das Extras 3.1-3.10

- a Lei nº 4.769/1965 ocupa a base legal da profissão e do sistema profissional;
- o Decreto nº 61.934/1967 regulamenta a execução da lei sem poder contrariá-la;
- o CFA atua em âmbito nacional nas competências de orientação e supervisão do sistema;
- o CRA-PR exerce suas atribuições de registro, orientação e fiscalização na respectiva jurisdição;
- o Regimento Interno organiza órgãos, competências e funcionamento interno, sem criar poder contra a lei;
- autonomia administrativa, técnica e financeira não rompe a integração institucional do sistema;
- a análise de um caso deve separar fonte, território, sujeito, conduta e competência antes de concluir.

**Exemplo 1:** fato ocorrido no Paraná não autoriza o CRA-PR a afastar norma federal; o âmbito territorial não altera a hierarquia da fonte.

**Exemplo 2:** uma resolução administrativa pode detalhar execução dentro da competência, mas não revogar disposição legal por incompatibilidade pretendida.

**Pegadinha:** trocar autonomia por soberania normativa ou confundir competência nacional com execução regional.

<a id="s4-d3-b5"></a>
## Bloco 5 - Português: referente, paralelismo e escopo

<a id="s4-d3-b5-portugues"></a>
### Precisão na descrição técnica - base das Extras 3.11-3.20

- pronome deve possuir referente inequívoco; se dois substantivos puderem ocupar o lugar, repita o nome necessário;
- elementos coordenados devem manter paralelismo: verbos com verbos, nomes com nomes ou orações de estrutura compatível;
- uma oração explicativa acrescenta informação sobre todo o referente; a restritiva delimita o conjunto;
- conectores preservam relações: porque indica causa/explicação, portanto indica conclusão, embora indica concessão e contudo marca contraste;
- o escopo de apenas, não e todos muda a conclusão; reescrever exige conservar esse alcance;
- texto técnico preciso evita salto entre possibilidade, necessidade e garantia.

**Exemplo 1:** “O módulo consulta o serviço quando ele falha” é ambíguo. “Quando o serviço falha, o módulo consulta a réplica” fixa o referente.

**Exemplo 2:** “A solução permite modelar componentes, a geração de código e que testes sejam rastreados” perde paralelismo. Melhor: “modelar componentes, gerar código e rastrear testes”.

**Aplicação:** ao justificar um diagrama, nomeie o elemento, a relação e a consequência sem usar pronome vago.

<a id="s4-d3-b6"></a>
## Bloco 6 - Recuperação ativa e caderno de erros

Sem consulta:

- defina componente, interface fornecida, interface requerida e porta em uma frase cada;
- desenhe cliente, contrato e duas realizações substituíveis;
- diferencie nó, ambiente de execução e artefato;
- explique manifestação e deployment sem usar a palavra “ligação” como única justificativa;
- escolha a classe de ferramenta para cinco necessidades apresentadas;
- recupere um erro de UML dos Dias 1 ou 2 e conecte-o à visão de componentes.

**Entrega:** tabela com cinco linhas no formato “elemento confundido → distinção correta → consequência no diagrama → questão para D+2”. Nenhum conceito novo entra neste bloco.

<a id="s4-d3-mini-revisao"></a>
## Mini revisão e perguntas de fixação

- componente encapsula capacidade; interface explicita contrato;
- fornecedor realiza/oferece; consumidor requer;
- deployment mostra nós e posicionamento de artefatos;
- manifestação liga peça física ao elemento lógico que ela concretiza;
- ferramenta automatiza ou registra, mas não garante intenção correta.

1. Quem fornece uma interface: quem inicia a chamada ou quem cumpre o contrato?
2. Um componente é necessariamente um arquivo executável?
3. Qual elemento representa uma plataforma dentro de um dispositivo?
4. Que relação responde onde o artefato foi colocado?
5. Engenharia reversa recupera automaticamente decisões de negócio?

**Respostas:** 1. Quem cumpre o contrato. 2. Não; a manifestação pode ligá-lo a um artefato. 3. Ambiente de execução. 4. Deployment. 5. Não.

<a id="s4-d3-mapa"></a>
## Mapa de conexões do Dia 3

~~~mermaid
flowchart LR
  R[Responsabilidade] --> C[Componente]
  C --> F[Interface fornecida]
  C --> Q[Interface requerida]
  Q --> F
  C --> M[Manifestada por artefato]
  M --> N[Implantado em nó]
  N --> P[Caminho de comunicação]
  T[Requisito] --> V[Rastreabilidade]
  V --> C
  V --> X[Teste]
  P1{{Pegadinha: componente não é servidor}}
  P2{{Pegadinha: fornecida não é quem chama}}
  P3{{Pegadinha: manifestação não é deployment}}
  P4{{Pegadinha: ferramenta não prova intenção}}
  C -.-> P1
  F -.-> P2
  M -.-> P3
  V -.-> P4
~~~

<a id="s4-d3-rastreabilidade"></a>
## Matriz de rastreabilidade do Dia 3

| Tópico do edital | Seção da teoria | Exemplos/práticas guiadas | Questões principais | Extras | Status |
|---|---|---:|---|---|---|
| componentes e implementação | [Componentes](#s4-d3-componentes) | 1-2 | S4D3Q101-Q112 | — | Coberto |
| interfaces, portas e dependências | [Interfaces](#s4-d3-interfaces) e [Dependências](#s4-d3-dependencias) | 3-6 | S4D3Q113-Q128 | — | Coberto |
| deployment e nós | [Deployment](#s4-d3-deployment) | 7-8 | S4D3Q129-Q139 | — | Coberto |
| artefatos e manifestação | [Artefatos](#s4-d3-artefatos) | 9-10 | S4D3Q138-Q143 | — | Coberto |
| ferramentas de apoio | [Ferramentas](#s4-d3-ferramentas) | 11-12 | S4D3Q144-Q150 | — | Coberto |
| Legislação CRA/CFA | [Bloco 4](#s4-d3-b4-legislacao) | 2 | — | Extras 3.1-3.10 | Coberto |
| Português | [Bloco 5](#s4-d3-b5-portugues) | 2 | — | Extras 3.11-3.20 | Coberto |

<a id="s4-d3-checklist"></a>
## Checklist de domínio

- [ ] separo componente lógico, artefato físico e nó de execução;
- [ ] identifico fornecedor e consumidor de interface;
- [ ] leio portas e dependências sem inverter direção;
- [ ] distingo realização, manifestação e deployment;
- [ ] posiciono artefatos em ambientes coerentes;
- [ ] escolho ferramenta pela necessidade e evidência;
- [ ] construo rastreabilidade requisito–modelo–código–teste;
- [ ] explico limites do diagrama e da automação.

<a id="s4-d3-fila"></a>
## Fila ordenada de dez Essenciais e fechamento

| Ordem | ID | Título real e retorno | Momento |
|---:|---|---|---|
| 1 | S4D3Q101 | Componente e servidor — [teoria](#s4-d3-componentes) | D0 |
| 2 | S4D3Q102 | Granularidade do componente — [teoria](#s4-d3-componentes) | D0 |
| 3 | S4D3Q103 | Responsabilidade modular — [teoria](#s4-d3-componentes) | D0 |
| 4 | S4D3Q104 | Contrato externo — [teoria](#s4-d3-componentes) | D0 |
| 5 | S4D3Q105 | Coesão e substituição — [teoria](#s4-d3-componentes) | D0 |
| 6 | S4D3Q106 | Visão adequada — [teoria](#s4-d3-componentes) | D0 |
| 7 | S4D3Q107 | Módulo e classes internas — [teoria](#s4-d3-componentes) | D+2 |
| 8 | S4D3Q108 | Responsabilidade observável — [teoria](#s4-d3-componentes) | D+2 |
| 9 | S4D3Q109 | Substituição por contrato — [teoria](#s4-d3-dependencias) | D+2 |
| 10 | S4D3Q110 | Impacto da mudança — [teoria](#s4-d3-dependencias) | D+2 |

Resolva S4D3Q101-S4D3Q106 e avance até S4D3Q110 somente se houver tempo para corrigir A-D. Agende saldo D+2 para 05/08, D+7 para 10/08 e D+21 para 24/08.

## Fontes do Dia 3

- edital consolidado local, página 28, itens de análise e projeto orientados a objetos, componentes, implementação e ferramentas de apoio;
- Object Management Group, [UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF), especificação formal dos elementos de componentes, artefatos e deployment;
- perfil documentado do Instituto Consulplan deste projeto, usado apenas para forma, integração e nível das questões autorais.

---

<a id="s4-d4-inicio"></a>
# Dia 4 - Engenharia de software, ciclos de vida e gerenciamento de projetos

## Abertura e objetivos

Ao final do dia, você deverá:

- explicar engenharia de software como aplicação sistemática de processos, métodos, técnicas e controles;
- comparar cascata, espiral, reuso, prototipação, RAD, evolutivo e incremental por risco, feedback e entrega;
- distinguir iteração de incremento e protótipo exploratório de produto evoluído;
- reconhecer concepção, elaboração, construção e transição pela finalidade, sem tratá-las como etapas rígidas e sem retorno;
- definir projeto e separar planejamento, acompanhamento e controle;
- construir escopo e WBS/estrutura analítica do projeto orientados a entregas;
- integrar tempo, custos, qualidade, pessoas, comunicação, riscos, aquisições e integração em decisões iniciais;
- evitar atribuir ao edital uma edição específica de guia de gerenciamento que ele não declarou.

## Jornada executável e ponto de parada

### Sessão A - 170 minutos

- **Bloco 1 (55 min):** engenharia de software e modelos de ciclo de vida.
- **Bloco 2 (55 min):** fases de concepção, elaboração, construção e transição; comparação aplicada.
- **Bloco 3 (60 min):** gerenciamento de projetos, WBS, planejamento, acompanhamento e controle integrados.

**Ponto de parada:** entregar uma matriz de seleção de ciclo para três projetos públicos e uma WBS de três níveis para um deles, com risco, marco, responsável, comunicação e critério de qualidade associados.

### Sessão B - 170 minutos

- **Bloco 4 (60 min):** D+21 do Dia 4 da Semana 1, D+7 do Dia 4 da Semana 3, D+2 do Dia 2 da Semana 4, Administração Pública e RLM.
- **Bloco 5 (30 min):** Português e progressão discursiva, com reescrita de decisão técnica.
- **Bloco 6 (15 min):** recuperação ativa de ciclos e decisões de projeto.
- **Mini revisão (10 min)**, **seis Essenciais (25 min)**, **correção A-D (25 min)** e **fechamento (5 min)**.

**Regra de carga:** pare a teoria nova ao completar os 170 minutos da Sessão A. A Sessão B recupera conteúdos já ensinados e produz evidências; não prolongue o capítulo técnico.

### Consolidação final - 20 minutos

- registrar confiança de 0 a 3 nas seis Essenciais;
- lançar no caderno um erro de ciclo e um erro de gestão com contraexemplo;
- confirmar as filas D+2, D+7 e D+21 e encerrar ao atingir **360 minutos líquidos** no dia.

<a id="s4-d4-b1"></a>
## Bloco 1 - Engenharia de software e ciclos de vida

<a id="s4-d4-engenharia"></a>
### 1. Processo, método, técnica e produto

Engenharia de software organiza o desenvolvimento e a evolução de software com práticas sistemáticas, medição, verificação e controle. O objetivo não é produzir documentação por si só, mas tornar necessidades, decisões, implementação, qualidade e mudança administráveis.

- **processo:** organiza atividades, papéis, entradas, saídas e controles;
- **método/técnica:** orienta como executar uma atividade, como modelar ou testar;
- **ferramenta:** automatiza ou registra parte do trabalho;
- **produto/artefato:** resultado produzido, como requisito, modelo, código, pacote ou relatório de teste.

Processo adequado ao contexto não é ausência de disciplina. Projetos com alto risco, integração externa ou obrigação de auditoria podem exigir evidências mais fortes, ainda que trabalhem iterativamente.

#### Exemplo completo 1 - evidência proporcional

**Situação:** correção simples de texto e integração crítica de pagamentos usam o mesmo fluxo burocrático.

**Dados relevantes:** impacto, risco e necessidade de prova são diferentes.

**Raciocínio passo a passo:** classifica-se risco e reversibilidade; preservam-se requisitos mínimos de versão e teste; aumenta-se revisão, rastreabilidade e validação na integração crítica.

**Resposta final:** adaptar controles ao risco sem eliminar qualidade nem impor o mesmo peso a toda mudança.

**Por que funciona:** disciplina é proporcional e verificável.

**Erro provável:** confundir adaptação com inexistência de processo.

#### Exemplo completo 2 - atividade e artefato

**Situação:** “validar requisito” aparece na lista de entregas, mas não há resultado definido.

**Dados relevantes:** validar é atividade; aceite registrado é evidência.

**Raciocínio passo a passo:** separa-se ação de saída; define-se critério; registra-se decisão e pendência; liga-se o resultado à versão do requisito.

**Resposta final:** atividade de validação produz registro de aceite, ressalva ou rejeição rastreável.

**Por que funciona:** processo passa a ter saída observável.

**Erro provável:** chamar reunião de produto final sem decisão registrada.

<a id="s4-d4-ciclos"></a>
<a id="s4-d4-modelos"></a>
### 2. Cascata, espiral, reuso, prototipação, RAD, evolutivo e incremental

| Abordagem | Ideia central | Quando ajuda | Risco de interpretação |
|---|---|---|---|
| cascata | fases predominantemente sequenciais e marcos definidos | escopo estável e forte necessidade de aprovação | presumir que qualquer retorno é proibido ou barato |
| espiral | ciclos orientados à identificação e redução de riscos | grande incerteza técnica ou de solução | tratá-la como repetição sem análise de risco |
| baseado em reuso | compor/adaptar ativos existentes | componentes adequados reduzem construção | ignorar incompatibilidade e custo de integração |
| prototipação | aprender/validar por representação antecipada | requisito ou interação pouco compreendido | promover protótipo descartável sem saneamento |
| RAD | desenvolvimento rápido com forte participação e ferramentas/componentização | recorte modular e decisões rápidas | confundir rapidez com ausência de arquitetura/teste |
| evolutivo | solução muda e amadurece por versões sucessivas | necessidade emerge com uso e feedback | perder controle de arquitetura e dívida |
| incremental | entrega funcional em partes que ampliam capacidade | priorização por valor e entrega antecipada | chamar toda repetição de incremento |

**Iteração** revisita e aperfeiçoa trabalho. **Incremento** adiciona capacidade utilizável ao produto. Um ciclo pode ser iterativo, incremental ou ambos. Para antecipar valor, uma fatia incremental pode atravessar as camadas técnicas necessárias e terminar em uma capacidade vertical verificável; concluir apenas uma camada isolada não garante incremento utilizável. Prototipação é uma estratégia de aprendizagem; o protótipo pode ser descartável ou evolutivo, desde que a intenção e os critérios estejam explícitos.

#### Exemplo completo 3 - selecionar espiral

**Situação:** biometria para fiscalização depende de tecnologia não testada, integração externa e requisitos ainda incertos.

**Dados relevantes:** risco técnico e de integração domina o projeto.

**Raciocínio passo a passo:** identifica-se o risco prioritário; constrói-se experimento/protótipo para reduzi-lo; avaliam-se resultados com interessados; planeja-se o próximo ciclo segundo o risco residual.

**Resposta final:** abordagem espiral orientada a riscos, com protótipos de redução de incerteza.

**Por que funciona:** cada volta é decidida pelo risco, não apenas pelo calendário.

**Erro provável:** escolher cascata só porque o órgão deseja marcos formais.

#### Exemplo completo 4 - incremento real

**Situação:** a primeira entrega permite consulta; a segunda inclui atualização; a terceira adiciona auditoria.

**Dados relevantes:** cada versão amplia capacidade utilizável e testável.

**Raciocínio passo a passo:** prioriza-se valor; define-se critério de aceite de cada fatia; preserva-se arquitetura para extensões; integra-se feedback.

**Resposta final:** desenvolvimento incremental, possivelmente também iterativo dentro de cada entrega.

**Por que funciona:** há acréscimo funcional, não apenas repetição de análise.

**Erro provável:** chamar correções internas sem nova capacidade de “incremento”.

#### Exemplo completo 5 - reuso com avaliação

**Situação:** existe componente de autenticação pronto, mas ele usa protocolo incompatível e não registra eventos exigidos.

**Dados relevantes:** reuso reduz construção, porém exige adaptação e conformidade.

**Raciocínio passo a passo:** compara-se requisito com capacidade; estima-se adaptação, integração, teste e dependência; confronta-se custo total com construção; registra-se decisão.

**Resposta final:** reutilizar somente se a análise de adequação e custo total for favorável.

**Por que funciona:** reuso é decisão de engenharia, não sinônimo automático de economia.

**Erro provável:** contar apenas o preço de aquisição ou a existência do componente.

#### Exemplo completo 6 - protótipo descartável

**Situação:** tela experimental usa dados fixos e não contém controles de segurança, mas esclarece o fluxo com usuários.

**Dados relevantes:** objetivo é aprender; qualidade interna não atende produção.

**Raciocínio passo a passo:** declara-se protótipo descartável; valida-se navegação e terminologia; registra-se aprendizado; reimplementa-se segundo arquitetura e requisitos não funcionais.

**Resposta final:** descartar o código experimental e preservar decisões validadas.

**Por que funciona:** evita transformar dívida exploratória em produto sem revisão.

**Erro provável:** promover o protótipo porque a interface “já funciona”.

#### Exemplo completo 7 - RAD com limite explícito

**Situação:** módulo administrativo independente tem prazo curto, usuários disponíveis e tecnologia conhecida.

**Dados relevantes:** escopo modular, feedback rápido e baixa incerteza técnica favorecem rapidez controlada.

**Raciocínio passo a passo:** divide-se o módulo; utiliza-se prototipação e componentes; agenda-se validação frequente; mantém-se integração e testes de aceite.

**Resposta final:** RAD pode ser adequado ao módulo, sem eliminar controles de qualidade.

**Por que funciona:** as condições de rapidez estão presentes.

**Erro provável:** aplicar RAD a sistema crítico altamente acoplado apenas pelo prazo.

#### Exemplo completo 8 - cascata com mudança tardia

**Situação:** requisito aprovado muda após construção, e o plano possui marcos sequenciais.

**Dados relevantes:** mudança tardia afeta especificação, código, teste, custo e prazo.

**Raciocínio passo a passo:** analisa-se impacto; decide-se pela governança de mudança; atualizam-se baselines e plano; evita-se fingir que a mudança não existe.

**Resposta final:** controlar o retorno e seus impactos; sequencialidade não torna a alteração impossível nem gratuita.

**Por que funciona:** preserva coerência entre produtos das fases.

**Erro provável:** afirmar que cascata proíbe qualquer realimentação.

<a id="s4-d4-b2"></a>
## Bloco 2 - Fases de concepção, elaboração, construção e transição

<a id="s4-d4-fases"></a>
### 3. Finalidade predominante das fases

No recorte do edital, as fases podem ser entendidas pela finalidade predominante:

| Fase | Pergunta principal | Evidências típicas |
|---|---|---|
| concepção | vale realizar e qual é a visão/escopo inicial | visão, atores, riscos iniciais, caso de negócio e limites |
| elaboração | a arquitetura e os riscos centrais estão suficientemente tratados | arquitetura-base, requisitos significativos, protótipos de risco e plano refinado |
| construção | a capacidade planejada está implementada e verificada | incrementos integrados, código, testes e documentação necessária |
| transição | a solução está apta ao uso no ambiente-alvo | implantação, migração, treinamento, correções e aceite operacional |

São fases com ênfases, não caixas que impedem toda atividade das demais. Requisitos podem ser refinados na construção; código exploratório pode aparecer na elaboração; o que muda é a finalidade e o peso.

#### Exemplo completo 9 - saída da elaboração

**Situação:** há longa lista de requisitos, mas integração crítica nunca foi testada e arquitetura continua indefinida.

**Dados relevantes:** quantidade documental não reduziu o principal risco.

**Raciocínio passo a passo:** identifica-se o risco arquitetural; produz-se prova de conceito; estabilizam-se decisões essenciais; revisa-se plano e requisitos significativos.

**Resposta final:** não considerar elaboração encerrada apenas pela lista; tratar arquitetura e riscos centrais.

**Por que funciona:** o marco é aderente à finalidade da fase.

**Erro provável:** medir maturidade somente por volume de documentação.

#### Exemplo completo 10 - transição não é só entrega

**Situação:** pacote foi instalado, porém dados não migraram, usuários não foram orientados e monitoramento não existe.

**Dados relevantes:** instalação técnica não produz aptidão operacional completa.

**Raciocínio passo a passo:** planeja-se migração; valida-se ambiente; treina-se público; monitora-se; corrige-se; registra-se aceite e retorno.

**Resposta final:** concluir transição após evidências operacionais, não apenas cópia do pacote.

**Por que funciona:** uso real é o objetivo da fase.

**Erro provável:** reduzir transição a deploy instantâneo.

<a id="s4-d4-b3"></a>
## Bloco 3 - Gerenciamento de projetos em noções iniciais

<a id="s4-d4-projetos"></a>
### 4. Projeto, planejamento, acompanhamento e controle

Projeto é esforço temporário orientado à entrega de resultado único dentro de restrições e objetivos. Operação mantém atividades recorrentes; projeto cria ou altera capacidade. Gerenciar integra decisão, execução e evidência.

- **planejar:** definir objetivos, entregas, abordagem, responsáveis, estimativas, riscos e critérios;
- **acompanhar:** coletar e comparar informações reais de progresso, custo, qualidade e risco;
- **controlar:** decidir ações diante de variação, aprovar mudanças e atualizar referências autorizadas;
- **encerrar:** obter aceite, transferir resultados, organizar pendências e registrar aprendizado.

O edital cita áreas tradicionais de gerenciamento. Este material ensina os conceitos sem afirmar que uma edição específica do PMBOK é normativa para a prova.

#### Fases de projeto e leitura correta do PMBOK

Para o item 16.3 do edital, use o mapa operacional **iniciação → planejamento → execução → acompanhamento e controle → encerramento**:

| Fase | Pergunta central | Evidência típica |
|---|---|---|
| iniciação | por que o projeto deve existir e quem o autoriza? | justificativa, objetivo inicial, responsável e autorização |
| planejamento | como o resultado será produzido e medido? | escopo, EAP/WBS, cronograma, orçamento, riscos e critérios |
| execução | como os planos são convertidos em entregas? | trabalho realizado, equipe coordenada e entregas verificáveis |
| acompanhamento e controle | onde há variação e qual decisão será tomada? | medição, análise, ação corretiva/preventiva e mudança controlada |
| encerramento | o resultado foi aceito e transferido? | aceite, transição, pendências tratadas e lições registradas |

As fases orientam a leitura do trabalho, mas não são compartimentos necessariamente isolados: execução e acompanhamento/controle coexistem, e um projeto adaptativo pode repetir planejamento e entrega. Não confunda essas fases de gerenciamento com **concepção, elaboração, construção e transição** do processo de desenvolvimento estudado no Bloco 2.

O **PMBOK** é um corpo/guia de conhecimentos de gerenciamento de projetos, não uma metodologia única que imponha o mesmo ciclo a todo projeto. Em questão, primeiro identifique a função praticada e a evidência produzida; depois associe a fase ou área correspondente. A prova não autorizou presumir uma edição específica.

#### Exemplo completo 11 - acompanhamento sem controle

**Situação:** relatório semanal mostra atraso, mas ninguém decide prioridade, recurso ou mudança.

**Dados relevantes:** informação foi coletada, porém não houve resposta de gestão.

**Raciocínio passo a passo:** compara-se realizado com referência; analisa-se causa e impacto; escolhe-se ação; registra-se responsável e nova previsão quando autorizada.

**Resposta final:** converter acompanhamento em controle por decisão rastreável.

**Por que funciona:** medir não corrige desvio sozinho.

**Erro provável:** chamar painel de controle completo apenas porque exibe indicadores.

#### Exemplo completo 12 - projeto x operação

**Situação:** implantar novo sistema e depois atender chamados mensais.

**Dados relevantes:** implantação tem objetivo e término; suporte é recorrente.

**Raciocínio passo a passo:** separa-se o esforço temporário de transição da rotina permanente; definem-se critérios de passagem e responsabilidades.

**Resposta final:** implantação é projeto; suporte contínuo é operação, embora possa receber melhorias por projetos.

**Por que funciona:** temporalidade e unicidade distinguem os trabalhos.

**Erro provável:** classificar toda atividade de TI como projeto.

<a id="s4-d4-escopo-tempo-custos"></a>
### 5. Escopo, WBS/EAP, tempo e custos

Escopo define o trabalho e as entregas incluídas. A WBS/EAP decompõe o escopo total em partes gerenciáveis, preferencialmente orientadas a entregas. Ela não é apenas cronograma, organograma nem lista aleatória de atividades. O nível mais baixo planejado para gestão é o pacote de trabalho.

Tempo organiza atividades, dependências, durações, recursos e marcos. Custos estimam e agregam recursos financeiros, formando uma referência autorizada quando aplicável. Alterar escopo pode afetar tempo, custo, qualidade e risco; a decisão deve ser integrada.

#### Exemplo completo 13 - WBS orientada a entrega

**Situação:** a “WBS” contém reuniões, telefonemas e nomes de servidores, mas não representa o produto.

**Dados relevantes:** tarefas de coordenação não cobrem o escopo do sistema.

**Raciocínio passo a passo:** parte-se da entrega Sistema de Fiscalização; decompõe-se em Cadastro, Inspeção, Relatórios e Implantação; detalham-se pacotes verificáveis; depois derivam-se atividades.

**Resposta final:** estrutura hierárquica de entregas que cubra 100% do escopo acordado.

**Por que funciona:** cada pacote possui resultado verificável e evita lacunas.

**Erro provável:** usar sequência temporal como se fosse decomposição de escopo.

#### Exemplo completo 14 - mudança integrada

**Situação:** solicita-se novo módulo mantendo data, equipe, orçamento e critérios, sem análise.

**Dados relevantes:** capacidade adicional demanda trabalho e pode elevar risco.

**Raciocínio passo a passo:** descreve-se mudança; estima-se impacto em WBS, dependências, duração, custo, testes e risco; decide-se por aprovação, rejeição, troca de prioridade ou ajuste de referências.

**Resposta final:** nenhuma promessa automática; decisão integrada e registrada.

**Por que funciona:** restrições são interdependentes.

**Erro provável:** tratar escopo como área isolada sem consequência.

<a id="s4-d4-qualidade-pessoas-comunicacao"></a>
### 6. Qualidade, pessoas e comunicação

Qualidade combina planejamento de critérios e verificação de conformidade/adequação. Inspeção final não substitui prevenção. Pessoas envolvem papéis, competências, disponibilidade, colaboração e resolução de conflitos; aumentar pessoas tardiamente não garante aceleração automática. Comunicação define interessado, informação, frequência, formato, responsável e retorno esperado.

#### Exemplo completo 15 - qualidade verificável

**Situação:** requisito diz “o portal será rápido”.

**Dados relevantes:** não há medida nem condição.

**Raciocínio passo a passo:** identifica-se operação crítica; define-se carga, ambiente, percentil e limite; cria-se teste; liga-se resultado ao aceite.

**Resposta final:** critério mensurável e procedimento de verificação.

**Por que funciona:** qualidade deixa de depender de opinião vaga.

**Erro provável:** usar apenas ausência de defeitos conhecidos como prova de qualidade total.

#### Exemplo completo 16 - comunicação orientada ao interessado

**Situação:** equipe técnica recebe relatório detalhado; direção e usuários recebem a mesma mensagem, sem decisão clara.

**Dados relevantes:** necessidades e linguagem diferem.

**Raciocínio passo a passo:** mapeiam-se interessados; define-se decisão necessária; ajustam-se conteúdo e frequência; registra-se canal e responsável; colhe-se retorno.

**Resposta final:** plano de comunicação segmentado, sem esconder a mesma situação factual.

**Por que funciona:** comunicação serve à compreensão e decisão.

**Erro provável:** tratar envio massivo como comunicação eficaz.

<a id="s4-d4-riscos-aquisicoes-integracao"></a>
### 7. Riscos, aquisições e integração

Risco é evento ou condição incerta que, se ocorrer, afeta objetivos. Deve possuir causa, evento, impacto, probabilidade, responsável, resposta e gatilho compatíveis com a profundidade do projeto. Problema já ocorrido não é risco futuro; é questão a tratar.

Aquisições envolvem decidir o que obter externamente, especificar necessidade, selecionar, contratar e acompanhar, respeitando a legislação aplicável — cujo aprofundamento está reservado ao cronograma da Semana 6. Integração coordena decisões e mudanças entre áreas; não é apenas consolidar documentos.

#### Exemplo completo 17 - risco e resposta

**Situação:** “o fornecedor atrasou” aparece no registro de riscos.

**Dados relevantes:** o atraso já aconteceu; há impacto no marco de testes.

**Raciocínio passo a passo:** trata-se o atraso como problema; executa-se ação corretiva; registra-se risco residual, como novo atraso na entrega restante; define-se gatilho e resposta.

**Resposta final:** separar issue atual de risco futuro e gerir ambos.

**Por que funciona:** cada registro recebe tratamento temporal correto.

**Erro provável:** manter evento ocorrido apenas como probabilidade.

#### Exemplo completo 18 - aquisição integrada

**Situação:** contratar serviço externo parece reduzir prazo, mas a interface ainda não está especificada e a equipe não planejou aceite.

**Dados relevantes:** compra depende de escopo, cronograma, qualidade, risco e comunicação.

**Raciocínio passo a passo:** define-se resultado e interface; cria-se critério de aceite; estima-se dependência; atribui-se responsável; registra-se risco e plano de integração.

**Resposta final:** planejar aquisição como parte integrada do projeto antes da seleção.

**Por que funciona:** fornecedor externo não elimina responsabilidade de integração.

**Erro provável:** tratar contratação como transferência integral do risco.

<a id="s4-d4-pratica"></a>
### Produto obrigatório do Bloco 3

Para um projeto fictício de portal de serviços:

1. defina objetivo, resultado e critério de encerramento;
2. escolha ciclo e justifique por estabilidade, risco, feedback e entregas;
3. crie WBS/EAP com três níveis e ao menos seis pacotes verificáveis;
4. associe três marcos e duas dependências;
5. estime um custo por premissa e registre a incerteza;
6. defina dois critérios de qualidade;
7. atribua papéis e uma comunicação por interessado;
8. registre três riscos com resposta e gatilho;
9. identifique uma aquisição possível e seu critério de aceite;
10. analise uma solicitação de mudança sobre todas as áreas afetadas.

<a id="s4-d4-b4"></a>
## Bloco 4 - Revisão programada: Administração Pública e RLM

<a id="s4-d4-b4-administracao"></a>
### Princípios, organização e controle - base das Extras 4.1-4.10

- legalidade exige atuação conforme competência e ordenamento; eficiência não autoriza ignorar regra aplicável;
- impessoalidade direciona a finalidade pública e veda promoção pessoal;
- publicidade é regra de transparência, convivendo com hipóteses legais de sigilo e proteção de dados;
- descentralização envolve outra pessoa jurídica; desconcentração distribui competências dentro da mesma pessoa;
- autarquia integra a Administração Indireta e possui personalidade jurídica de direito público;
- anulação responde a ilegalidade; revogação incide sobre ato válido por conveniência e oportunidade, dentro dos limites;
- controle mede conformidade e resultado, mas o indicador não substitui decisão corretiva.

**Exemplo 1:** criar nova divisão dentro do CRA-PR é desconcentração, pois não surge outra pessoa jurídica.

**Exemplo 2:** ato ilegal não se torna revogável apenas porque também é inconveniente; a categoria central para retirar o vício é anulação.

<a id="s4-d4-b4-rlm"></a>
### Proposições, percentuais e valor esperado - base das Extras 4.11-4.20

- a implicação “se p, então q” é falsa somente quando p é verdadeira e q é falsa;
- sua contrapositiva “se não q, então não p” é equivalente; a recíproca não é automaticamente equivalente;
- negar “p e q” resulta em “não p ou não q”; negar “p ou q” resulta em “não p e não q”;
- variação percentual usa o valor inicial como base: de 80 para 100, aumento de 20/80 = 25%;
- impacto monetário esperado simples pode ser calculado como probabilidade × impacto, quando o enunciado adotar esse critério;
- comparar riscos apenas pelo impacto ignora probabilidade, e o valor esperado não substitui análise qualitativa ou de dependências.

**Exemplo 1:** risco de 20% e impacto de R$ 50.000 produz exposição simples de R$ 10.000.

**Exemplo 2:** negar “todo incremento foi testado” produz “existe ao menos um incremento que não foi testado”.

### Precedência da fila do Bloco 4

1. recuperar o D+21 do Dia 4 da Semana 1;
2. executar o D+7 do Dia 4 da Semana 3;
3. concluir até quatro Essenciais do Dia 2 da Semana 4, correspondentes ao D+2;
4. resolver a amostra fixa de Administração Pública e RLM sem abrir teoria inédita.

<a id="s4-d4-b5"></a>
## Bloco 5 - Português e progressão discursiva

<a id="s4-d4-b5-portugues"></a>
### Reescrita de decisão técnica

- a justificativa deve nomear problema, critério, decisão e consequência;
- conectores não são decorativos: “porque” apresenta fundamento, “portanto” introduz conclusão e “embora” limita sem apagar o argumento;
- possibilidade não equivale a garantia; recomendação não equivale a obrigação normativa;
- enumerações de impactos devem preservar paralelismo e o mesmo nível de abstração;
- a conclusão não pode introduzir risco ou requisito que não tenha sido desenvolvido.

**Modelo comentado:** “Embora a entrega incremental antecipe valor, o risco de integração permanece alto; por isso, recomenda-se um experimento técnico antes de comprometer o marco.” A concessão reconhece a vantagem, o segundo eixo delimita o risco e a conclusão deriva dos dois.

**Prática:** reescreva em 90 a 120 palavras a decisão de ciclo do Produto obrigatório. Explicite dois critérios, um risco e uma consequência. Faça a autocorreção por referente, conector, paralelismo e força modal. Esta prática não possui questão extra própria; ela prepara a produção discursiva da semana.

<a id="s4-d4-b6"></a>
## Bloco 6 - Recuperação ativa e caderno de erros

Sem consulta:

- compare sete modelos em uma frase discriminadora cada;
- dê um exemplo de iteração sem incremento e de incremento com iteração;
- associe concepção, elaboração, construção e transição às perguntas centrais;
- desenhe WBS de dois níveis e explique por que não é cronograma;
- diferencie planejar, acompanhar e controlar;
- escreva um risco no formato causa–evento–impacto–resposta;
- recupere um erro de ciclo ou gestão e defina sua revisão D+2.

**Entrega:** quadro “cenário → modelo escolhido → três critérios → risco dominante → evidência de controle”. Nenhum conceito novo entra neste bloco.

<a id="s4-d4-mini-revisao"></a>
## Mini revisão e perguntas de fixação

- cascata enfatiza sequência; espiral, risco; protótipo, aprendizagem; incremento, capacidade entregue;
- concepção trata viabilidade/visão; elaboração, arquitetura/risco; construção, solução; transição, uso;
- WBS/EAP decompõe escopo, enquanto cronograma ordena trabalho no tempo;
- acompanhamento mede; controle decide e age;
- integração avalia efeito cruzado de mudanças.

1. Toda iteração produz obrigatoriamente nova capacidade utilizável?
2. Reuso é sempre mais barato que construção?
3. Qual fase enfatiza riscos arquiteturais centrais?
4. Um problema já ocorrido permanece apenas como risco futuro?
5. O edital autoriza pressupor uma edição específica do PMBOK?

**Respostas:** 1. Não. 2. Não; adaptação e integração importam. 3. Elaboração. 4. Não; deve ser tratado como problema, sem apagar risco residual. 5. Não.

<a id="s4-d4-mapa"></a>
## Mapa de conexões do Dia 4

~~~mermaid
flowchart TD
  C[Contexto] --> E{Escopo estável?}
  E -->|alto| W[Cascata com marcos]
  E -->|baixo| R{Risco dominante?}
  R -->|alto| S[Espiral]
  R -->|aprendizagem| P[Prototipação/evolutivo]
  R -->|valor fatiável| I[Incremental]
  W --> G[Plano integrado]
  S --> G
  P --> G
  I --> G
  G --> A[Acompanhar]
  A --> K[Controlar mudança]
  K --> G
  P1{{Pegadinha: iteração não é incremento}}
  P2{{Pegadinha: WBS não é cronograma}}
  P3{{Pegadinha: medir não é controlar}}
  P4{{Pegadinha: compra não transfere todo risco}}
  I -.-> P1
  G -.-> P2
  A -.-> P3
  K -.-> P4
~~~

<a id="s4-d4-rastreabilidade"></a>
## Matriz de rastreabilidade do Dia 4

| Tópico do edital | Seção da teoria | Exemplos/práticas guiadas | Questões principais | Extras | Status |
|---|---|---:|---|---|---|
| engenharia de software | [Fundamentos](#s4-d4-engenharia) | 1-2 | S4D4Q151-Q156 | — | Coberto |
| modelos de ciclo de vida | [Modelos](#s4-d4-modelos) | 3-8 | S4D4Q157-Q180 | — | Coberto |
| concepção, elaboração, construção e transição | [Fases](#s4-d4-fases) | 9-10 | S4D4Q181-Q190 | — | Coberto |
| conceito, fases de projeto, PMBOK, planejamento, acompanhamento e controle | [Projetos](#s4-d4-projetos) | 11-12 | S4D4Q191-Q192 | — | Coberto |
| escopo, WBS, tempo e custos | [Escopo, tempo e custos](#s4-d4-escopo-tempo-custos) | 13-14 | S4D4Q193-Q195 | — | Coberto |
| qualidade, pessoas, comunicação, riscos, aquisições e integração | [Qualidade](#s4-d4-qualidade-pessoas-comunicacao) e [Riscos](#s4-d4-riscos-aquisicoes-integracao) | 15-18 | S4D4Q196-Q200 | — | Coberto |
| Administração Pública | [Bloco 4](#s4-d4-b4-administracao) | 2 | — | Extras 4.1-4.10 | Coberto |
| RLM | [Bloco 4](#s4-d4-b4-rlm) | 2 | — | Extras 4.11-4.20 | Coberto |
| Português/discursiva | [Bloco 5](#s4-d4-b5-portugues) | 1 modelo + 1 prática | — | — | Coberto |

<a id="s4-d4-checklist"></a>
## Checklist de domínio

- [ ] comparo ciclos pelo contexto, não por slogans;
- [ ] separo iteração, incremento e protótipo;
- [ ] reconheço finalidade predominante das quatro fases;
- [ ] diferencio projeto e operação;
- [ ] separo planejamento, acompanhamento e controle;
- [ ] construo WBS/EAP de entregas;
- [ ] analiso mudança em escopo, tempo, custo, qualidade e risco;
- [ ] defino papéis e comunicação verificável;
- [ ] separo risco futuro de problema ocorrido;
- [ ] integro aquisição ao restante do projeto.

<a id="s4-d4-fila"></a>
## Fila ordenada de dez Essenciais e fechamento

| Ordem | ID | Título real e retorno | Momento |
|---:|---|---|---|
| 1 | S4D4Q151 | Finalidade da engenharia — [teoria](#s4-d4-engenharia) | D0 |
| 2 | S4D4Q152 | Processo e produto — [teoria](#s4-d4-engenharia) | D0 |
| 3 | S4D4Q153 | Método e ferramenta — [teoria](#s4-d4-engenharia) | D0 |
| 4 | S4D4Q154 | Adaptação proporcional — [teoria](#s4-d4-engenharia) | D0 |
| 5 | S4D4Q155 | Evidência de validação — [teoria](#s4-d4-engenharia) | D0 |
| 6 | S4D4Q156 | Processo em cenário público — [teoria](#s4-d4-engenharia) | D0 |
| 7 | S4D4Q157 | Ênfase da cascata — [teoria](#s4-d4-modelos) | D+2 |
| 8 | S4D4Q158 | Núcleo da espiral — [teoria](#s4-d4-modelos) | D+2 |
| 9 | S4D4Q159 | Reuso avaliado — [teoria](#s4-d4-modelos) | D+2 |
| 10 | S4D4Q160 | Protótipo descartável — [teoria](#s4-d4-modelos) | D+2 |

Resolva S4D4Q151-S4D4Q156 e avance até S4D4Q160 somente com correção A-D. Agende saldo D+2 para 06/08, D+7 para 11/08 e D+21 para 25/08.

## Fontes do Dia 4

- edital consolidado local, página 28, itens de engenharia de software, modelos, fases e gerenciamento de projetos;
- [Project Management Institute — padrões e PMBOK](https://www.pmi.org/standards/pmbok), consultado como fonte primária e sem vincular a prova a uma edição não indicada no edital;
- plano mestre da trilha, que exige introdução de escopo/WBS, tempo, custos, qualidade, pessoas, comunicação, riscos, aquisições e integração sem fixar edição do PMBOK;
- perfil documentado do Instituto Consulplan deste projeto, usado apenas para calibrar comandos, cenários e dificuldade.

---
