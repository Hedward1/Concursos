# Dia 3 - Componentes, implementação e ferramentas de apoio

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. A matriz inicial é 20/20/10 nas principais e 8/8/4 nas extras. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais - S4D3Q101 a S4D3Q150

### S4D3Q101 — Componente e servidor

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Em uma revisão arquitetural, a equipe precisa representar o módulo lógico de Cadastro, independentemente do servidor em que será executado. Qual elemento é adequado?

A) Um componente Cadastro.

B) Um nó Cadastro.

C) Um caminho de comunicação.

D) Um artefato de configuração.


### S4D3Q102 — Granularidade do componente

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

A pergunta do modelo é quais módulos entregáveis oferecem serviços ao Portal. As classes Serviço, Repositório e Validador pertencem ao mesmo módulo Processos. Qual representação atende à pergunta?

A) Um componente para cada classe, todos com contratos próprios.

B) Um componente Processos, com as classes internas e o contrato do módulo.

C) Um artefato Processos, sem representar o contrato oferecido.

D) Um componente Portal, contendo as três classes e seus métodos.


### S4D3Q103 — Responsabilidade modular

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

No cenário do CRA-PR, o módulo Notificações deve poder mudar de provedor sem alterar a regra de Registro. Qual decisão favorece esse objetivo?

A) Unir toda a lógica em Registro para reduzir elementos.

B) Representar o provedor como porta UML de Registro.

C) Separar Notificações e fazê-lo cumprir um contrato consumido por Registro.

D) Substituir o contrato por um caminho físico entre servidores.


### S4D3Q104 — Contrato externo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Um diagrama deve mostrar o que Cobrança oferece sem revelar suas classes internas. O que deve ser enfatizado?

A) A porta do nó que hospeda Cobrança.

B) A classe pública que inicia Cobrança.

C) O artefato que manifesta Cobrança.

D) A interface fornecida por Cobrança.


### S4D3Q105 — Coesão e substituição

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Dois módulos misturam envio de mensagem, cálculo de taxa e persistência. Qual ação é coerente?

A) Separar por tecnologia e manter contratos implícitos.

B) Separar responsabilidades e explicitar dependências por interfaces.

C) Separar por servidor e duplicar as regras compartilhadas.

D) Manter os módulos e ocultar dependências no diagrama.


### S4D3Q106 — Visão adequada

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Qual pergunta é respondida principalmente por um diagrama de componentes?

A) Em qual endereço físico cada pacote está instalado?

B) Qual sequência temporal ocorre entre objetos?

C) Qual estado interno segue um evento?

D) Quais módulos oferecem ou requerem contratos?


### S4D3Q107 — Módulo e classes internas

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Um analista concluiu que toda classe pública constitui necessariamente um componente separado. Assinale a avaliação correta.

A) Não; a classe pode integrar a realização interna de um componente.

B) Sim; a visibilidade pública define a fronteira de cada componente.

C) Sim; uma classe pública realiza obrigatoriamente uma interface.

D) Não; toda classe pública deve ser representada como artefato.


### S4D3Q108 — Responsabilidade observável

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Relatórios aparece no modelo, mas não possui responsabilidade nem contrato identificáveis. Qual correção é mais útil?

A) Definir primeiro as dependências entre Relatórios e os demais módulos.

B) Modelar Relatórios como nó e depois alocar seus artefatos.

C) Definir a capacidade de Relatórios e seus serviços externos.

D) Detalhar as classes internas antes de identificar seu contrato.


### S4D3Q109 — Substituição por contrato

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Cobrança requer Repositório; RepositórioSQL e RepositórioMemória cumprem o contrato. O que permite substituição em testes?

A) Dependência direta de Cobrança para cada classe concreta.

B) Dependência de Cobrança para contratos distintos de cada repositório.

C) Dependência de Cobrança para o contrato, realizado pelas alternativas.

D) Realização de Repositório pela própria Cobrança, sem alternativas externas.


### S4D3Q110 — Impacto da mudança

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Portal e Aplicativo requerem Autenticação; Auditoria usa outro contrato. Se uma operação de Autenticação for removida, quais são candidatos imediatos ao impacto?

A) Portal e Aplicativo.

B) Somente Auditoria, por proximidade visual.

C) Todos os nós físicos.

D) Apenas a interface.


### S4D3Q111 — Encapsulamento do componente

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Sobre o conteúdo interno de um componente, assinale a alternativa correta.

A) Deve expor sua realização interna para permitir a substituição.

B) Pode conter classificadores, mas não apresentar interfaces externas.

C) É determinado pelo nó em que seus artefatos serão implantados.

D) Pode encapsular a realização e expor somente os contratos externos.


### S4D3Q112 — Limite do diagrama de componentes

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Portal requer Consulta e Cadastro a fornece. Qual conclusão NÃO pode ser garantida apenas pelo desenho?

A) Portal aparece como consumidor do contrato Consulta.

B) A integração cumprirá disponibilidade e desempenho em produção.

C) Cadastro aparece como fornecedor do contrato Consulta.

D) A relação arquitetural deverá ser verificada por testes.


### S4D3Q113 — Fornecedor da interface

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Cadastro implementa consultar e Relatórios a invoca. Quem fornece ConsultaCadastral?

A) Cadastro.

B) Relatórios.

C) Ambos, pois um implementa e o outro invoca.

D) A própria interface, pois ela define as operações.


### S4D3Q114 — Interface requerida

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Portal não conclui solicitação sem ValidarRegistro. Como representar a necessidade?

A) Como interface fornecida por Portal.

B) Como dispositivo contido em Portal.

C) Como interface requerida por Portal.

D) Como manifestação de Portal.


### S4D3Q115 — Sentido da porta UML

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Uma porta na fronteira de Atendimento representa:

A) um ponto de rede que identifica a porta TCP usada pelo componente.

B) um ponto de interação que agrupa contratos da fronteira.

C) um artefato que materializa as interfaces do componente.

D) um nó interno que executa os serviços do componente.


### S4D3Q116 — Conector de montagem

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Uma interface requerida de Portal liga-se à fornecida compatível de Cadastro. Isso indica:

A) manifestação do Portal no código.

B) implantação no mesmo nó.

C) herança obrigatória.

D) montagem entre consumidor e fornecedor.


### S4D3Q117 — Realização de interface

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Qual relação descreve que RepositórioSQL cumpre as operações de Repositório?

A) Caminho de comunicação.

B) Deployment.

C) Dependência genérica.

D) Realização de interface.


### S4D3Q118 — Direção da dependência

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

A utiliza serviço exposto por B. A seta tracejada de dependência parte de:

A) B e aponta para A.

B) A e aponta para B.

C) ambos simultaneamente.

D) um nó físico.


### S4D3Q119 — Dependência e caminho físico

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Qual distinção está correta?

A) Dependência liga cliente e fornecedor; caminho liga artefato e nó.

B) Dependência e caminho representam conexões lógicas equivalentes.

C) Dependência mostra uso lógico; caminho mostra comunicação entre nós.

D) Dependência mostra implantação; caminho mostra realização de contrato.


### S4D3Q120 — Comando negativo sobre interfaces

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Sobre interfaces e portas, assinale a alternativa INCORRETA.

A) Porta UML designa necessariamente um endpoint TCP ou UDP.

B) Interface fornecida especifica serviço oferecido pelo componente.

C) Interface requerida especifica serviço do qual o componente depende.

D) Porta organiza interfaces expostas em um ponto da fronteira.


### S4D3Q121 — Dois fornecedores substituíveis

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Portal requer Pagamento; ProvedorA e ProvedorB realizam o contrato, mas só um é selecionado por ambiente. Qual desenho preserva substituição?

A) Portal depende diretamente de ProvedorA e troca a classe por configuração.

B) Portal requer Pagamento, mas cada provedor expõe contrato próprio.

C) Portal requer Pagamento; ambos o realizam; a configuração escolhe um.

D) Portal depende de ambos os provedores e ativa somente um por ambiente.


### S4D3Q122 — Mudança interna sem quebra externa

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Cadastro refatora classes, preservando interface e comportamento contratado. Qual efeito é coerente?

A) O contrato preservado evita mudança obrigatória nos consumidores.

B) O componente deve ser movido para outro nó antes da refatoração.

C) As interfaces requeridas passam a ser fornecidas após a refatoração.

D) A realização da interface precisa ser removida durante a refatoração.


### S4D3Q123 — Compatibilidade declarada e teste

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Interfaces têm o mesmo nome, mas discordam no formato e significado de campo. Qual avaliação é correta?

A) A montagem garante compatibilidade quando as interfaces têm o mesmo nome.

B) A assinatura igual basta, mesmo que a semântica dos campos seja distinta.

C) A co-localização no mesmo nó resolve divergências de formato e significado.

D) A compatibilidade semântica ainda precisa ser especificada e testada.


### S4D3Q124 — Visão lógica não prova execução

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

O modelo mostra componentes, mas é preciso decidir isolamento de ambientes e caminhos. Qual ação é apropriada?

A) Detalhar portas e interfaces no diagrama de componentes existente.

B) Adicionar uma visão de deployment ligada aos artefatos dos componentes.

C) Substituir cada componente por uma classe associada ao servidor.

D) Distribuir os componentes por endereços anotados na visão lógica.


### S4D3Q125 — Portas para canais distintos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Atendimento recebe API e lote por contratos diferentes, com mesma lógica interna. Qual solução é expressiva?

A) Usar duas portas, cada qual associada ao contrato do respectivo canal.

B) Usar dois componentes idênticos, ambos com os dois contratos.

C) Usar um caminho físico distinto para representar cada contrato.

D) Usar um único contrato e indicar os canais apenas nos artefatos.


### S4D3Q126 — Impacto multiconsumidor

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Uma interface ganha parâmetro obrigatório. Três consumidores a requerem; dois usam a operação e um usa outra. Qual análise é precisa?

A) Revisar somente os dois consumidores que usam a operação alterada.

B) Revisar os três consumidores e alterar todos antes de qualquer teste.

C) Revisar os três; priorizar os dois usos e confirmar o terceiro.

D) Revisar apenas o fornecedor, pois o contrato preserva os consumidores.


### S4D3Q127 — Uso e realização

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

ServiçoRelatorio requer Consulta; Cadastro realiza Consulta. Qual leitura está correta?

A) ServiçoRelatorio realiza por iniciar chamada.

B) ServiçoRelatorio é cliente; Cadastro é implementador.

C) Cadastro requer por receber chamada.

D) Ambos manifestam a interface.


### S4D3Q128 — Estrutura interna e contrato

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Um componente contém partes internas e oferece interface externa. Qual afirmação é adequada?

A) A estrutura interna deve ser exposta para o componente continuar substituível.

B) A interface externa deve enumerar todas as partes usadas na realização.

C) As partes internas precisam ser representadas como nós de execução.

D) A estrutura interna pode ser modelada sem romper o encapsulamento.


### S4D3Q129 — Transição da visão lógica para física

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Para ligar Cadastro ao deployment, qual sequência é coerente?

A) Cadastro é implantado diretamente no nó, sem artefato intermediário.

B) Um artefato realiza Cadastro e o nó manifesta esse artefato.

C) O ambiente manifesta Cadastro e o artefato realiza o ambiente.

D) Um artefato manifesta Cadastro e é implantado em ambiente de execução.


### S4D3Q130 — Nó de execução

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Em deployment, nó representa:

A) um contrato lógico oferecido por um componente.

B) um recurso computacional que hospeda ou executa artefatos.

C) uma sequência de mensagens entre objetos em execução.

D) uma unidade modular responsável por regra de negócio.


### S4D3Q131 — Dispositivo e ambiente

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Servidor físico contém JVM que executa api.jar. Qual classificação é coerente?

A) Servidor é componente; JVM é interface; jar é nó.

B) Servidor é artefato; JVM é dependência; jar é porta.

C) Servidor é dispositivo; JVM é ambiente; api.jar é artefato.

D) Servidor é interface; JVM é componente; jar é caminho.


### S4D3Q132 — Caminho de comunicação

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

A associação entre nó Aplicação e nó Dados que permite interação representa:

A) um caminho de comunicação.

B) realização de interface.

C) manifestação do servidor.

D) generalização de dispositivos.


### S4D3Q133 — Cliente sem acesso direto ao banco

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

A arquitetura exige Cliente→Aplicação e Aplicação→Dados, vedando Cliente→Dados. Qual diagrama traduz isso?

A) Um componente com três interfaces, sem nós.

B) Um caminho direto rotulado como proibido, mas usado.

C) Três artefatos por realizações.

D) Três nós ligados apenas por Cliente–Aplicação e Aplicação–Dados.


### S4D3Q134 — Ambientes aninhados

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Um dispositivo hospeda duas VMs, cada qual com artefatos próprios. Qual modelagem preserva níveis?

A) Um dispositivo para cada VM, ambos contidos em um componente.

B) Um dispositivo contendo duas VMs modeladas como artefatos.

C) Um ambiente contendo dois dispositivos ligados por caminhos.

D) Um dispositivo contendo dois ambientes, cada qual com seus artefatos.


### S4D3Q135 — Restrição em três camadas

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Portal acessa Cadastro; Cadastro acessa Dados; o banco fica isolado. Qual combinação é correta?

A) Manifestar os componentes em artefatos, implantá-los nos nós e limitar os caminhos.

B) Implantar os componentes diretamente e usar interfaces como caminhos entre nós.

C) Manifestar os nós em artefatos e ligar cada componente ao banco por dependência.

D) Implantar todas as peças no mesmo nó e registrar isolamento apenas no contrato.


### S4D3Q136 — Limite do deployment

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

O diagrama mostra caminho Aplicação–Dados. O que ainda exige verificação externa?

A) Os nós e os papéis de cada um na topologia representada.

B) A existência da comunicação prevista entre Aplicação e Dados.

C) Os protocolos e atributos operacionais exigidos para essa comunicação.

D) Os artefatos implantados em cada nó e as relações de manifestação.


### S4D3Q137 — Escala com instâncias

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

O mesmo artefato da API é implantado em dois nós. Qual leitura é adequada?

A) Cada deployment cria uma nova interface lógica para a API.

B) Cada deployment exige um componente lógico diferente.

C) Há duas implantações do artefato e pode haver um só componente lógico.

D) Há um artefato por nó e a manifestação deixa de existir.


### S4D3Q138 — Posicionamento do artefato

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

cadastro-api.jar deve executar na JVM de Aplicação-1. Qual relação responde ao posicionamento?

A) Dependência do nó para interface.

B) Realização do dispositivo.

C) Generalização da JVM.

D) Deployment do artefato no ambiente.


### S4D3Q139 — Comando negativo sobre nós

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Sobre deployment, assinale a alternativa INCORRETA.

A) Todo nó representa necessariamente um componente do domínio.

B) Um dispositivo pode conter um ou mais ambientes de execução.

C) Um artefato pode ser implantado em dispositivo ou ambiente.

D) Um caminho de comunicação pode conectar nós da topologia.


### S4D3Q140 — Manifestação e implantação combinadas

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

relatorios.jar concretiza Relatórios e é instalado na JVM do servidor B. Qual conjunto é correto?

A) Manifestação entre componente e jar; deployment entre componente e JVM.

B) Manifestação entre jar e componente; deployment entre jar e JVM.

C) Realização entre jar e componente; manifestação entre jar e JVM.

D) Deployment entre jar e componente; realização entre jar e JVM.


### S4D3Q141 — Pacote comum e configurações distintas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

O mesmo pacote vai a homologação e produção com configurações próprias. Qual modelo é preciso?

A) Criar um componente para homologação e outro para produção, com o mesmo pacote.

B) Implantar o pacote nos dois ambientes, cada qual com sua configuração.

C) Manifestar cada ambiente em sua configuração e implantar o nó.

D) Usar uma configuração externa sem registrar a diferença entre ambientes.


### S4D3Q142 — Tipos de artefato

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

Qual conjunto contém apenas exemplos coerentes de artefatos?

A) Componente, interface, executável e caso de uso.

B) Servidor, roteador, script e caminho de comunicação.

C) Biblioteca, componente, configuração e ambiente de execução.

D) Executável, biblioteca, script e arquivo de configuração.


### S4D3Q143 — Três camadas sem mistura

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

Considere Cadastro, cadastro.jar e JVM. Assinale a cadeia correta.

A) cadastro.jar manifesta Cadastro e é implantado na JVM.

B) Cadastro manifesta cadastro.jar e a JVM é implantada no arquivo.

C) A JVM manifesta Cadastro e cadastro.jar é implantado no componente.

D) cadastro.jar realiza Cadastro e a JVM manifesta o arquivo.


### S4D3Q144 — Ferramenta para rastreabilidade

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Requisitos, commits e testes estão desconectados. Qual prioridade trata a causa?

A) Modelador que gere diagramas e mantenha a ligação apenas por nomes.

B) IDE que associe commits ao autor, sem vínculo com requisito ou teste.

C) Repositório integrado a versão e testes, com IDs e vínculos rastreáveis.

D) Gerador que produza código e registre o build, sem relacionar o requisito.


### S4D3Q145 — Limite da engenharia reversa

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Uma ferramenta extrai diagrama do legado. Qual uso é responsável?

A) Tratá-lo como registro fiel dos requisitos que originaram o sistema.

B) Usá-lo como baseline estrutural e validar as decisões ausentes.

C) Tratá-lo como prova da arquitetura planejada, inclusive das decisões erodidas.

D) Usá-lo para substituir testes, pois a estrutura extraída comprova comportamento.


### S4D3Q146 — Limite da engenharia direta

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Modelador gera esqueletos de classes. Qual afirmação é correta?

A) Garante os requisitos não funcionais descritos no modelo de origem.

B) Automatiza a estrutura, mas comportamento e qualidade ainda exigem verificação.

C) Dispensa versionar o código gerado quando o modelo já possui histórico.

D) Mantém modelo e código sincronizados depois de qualquer alteração manual.


### S4D3Q147 — Round-trip sem falsa garantia

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Modelo e código são sincronizados, mas alterados sem precedência. Qual risco permanece?

A) O modelo sempre prevalece, mesmo quando o código contém a correção validada.

B) O código sempre prevalece, ainda que o modelo contenha decisão não implementada.

C) Conflitos desaparecem se modelo e código estiverem no mesmo repositório.

D) Persistem conflitos; fonte de verdade, fluxo e revisão precisam ser definidos.


### S4D3Q148 — Cadeia de ferramentas e evidência

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

O órgão quer saber se cada requisito chegou ao pacote implantado e passou no teste. Qual cadeia é adequada?

A) Requisito → diagrama sem versão → arquivo local → implantação manual.

B) Requisito → tarefa sem commit → build local → teste sem versão → deployment.

C) Requisito → commit → build versionado → teste → deployment registrado.

D) Requisito → código gerado → build versionado → nó, presumindo aceite.


### S4D3Q149 — Cenário integrado de arquitetura e ferramentas

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Cadastro fornece Consulta; Portal a requer; cadastro.jar roda em dois nós. Uma mudança deve chegar controladamente. Qual plano é completo?

A) Alterar o jar, copiar aos dois nós e atualizar o modelo depois da implantação.

B) Versionar contrato e código, rastrear consumidores, testar o build e registrar ambos os deployments.

C) Versionar só o modelo, gerar dois builds locais e validar apenas o primeiro nó.

D) Criar um novo servidor, manter o contrato e presumir compatibilidade dos consumidores.


### S4D3Q150 — Auditoria de ferramenta e implantação

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

A ferramenta afirma round-trip, o build não é identificável e um dos dois nós executa pacote antigo. Qual resposta reúne três controles?

A) Sincronizar modelo e código, manter builds locais e comparar os nós manualmente.

B) Fixar a versão do modelo, recompilar sem ID e atualizar apenas o nó antigo.

C) Versionar somente o código, gerar build mutável e registrar o ambiente, não o nó.

D) Fixar modelo/código, gerar build imutável identificado e verificar cada nó.


## Questões extras - Dia 3

#### Extra Dia 3.1 — Lei e decreto

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Qual relação entre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967 foi revisada?

A) A lei define a base; o decreto disciplina sua execução nos limites legais.

B) O decreto detalha a execução e pode afastar a lei quando for posterior.

C) A lei organiza apenas o CRA-PR; o decreto estrutura o sistema nacional.

D) As duas fontes têm o mesmo nível e prevalece a mais específica.


#### Extra Dia 3.2 — Âmbito do CFA e CRA

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Assinale a divisão coerente de atuação.

A) O CRA-PR aplica orientação nacional e substitui o CFA quando o fato é paranaense.

B) O CFA orienta nacionalmente e também executa sozinho todas as atribuições regionais.

C) O CFA atua nacionalmente; o CRA-PR exerce atribuições em sua jurisdição.

D) CFA e CRA-PR têm âmbitos distintos e não integram o mesmo sistema.


#### Extra Dia 3.3 — Função do Regimento

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

O Regimento Interno serve principalmente para:

A) organizar os órgãos internos e ampliar suas competências além da lei.

B) organizar órgãos, competências e funcionamento conforme as fontes superiores.

C) definir orientação nacional e substituir as competências reservadas ao CFA.

D) disciplinar a profissão e afastar o decreto nos assuntos internos.


#### Extra Dia 3.4 — Autonomia integrada

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

A autonomia do CRA-PR significa:

A) gerir o âmbito regional sem observar orientações do sistema nacional.

B) editar decisões regionais com força superior às fontes federais.

C) exercer todas as competências nacionais quando o fato ocorrer no Paraná.

D) gerir seu âmbito, preservando integração e competências do sistema.


#### Extra Dia 3.5 — Método de leitura normativa

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Qual sequência reduz erros?

A) Identificar primeiro o território e presumir a competência do órgão local.

B) Identificar a fonte e aplicar sempre a norma mais recente ao caso.

C) Identificar a finalidade e afastar a competência quando houver eficiência.

D) Identificar fonte, âmbito, sujeito, conduta e competência.


#### Extra Dia 3.6 — Detalhamento por resolução

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Uma resolução detalha procedimento, mas alternativa diz que revogou lei. Avalie.

A) Prevalece sobre a lei se for mais recente e tratar de procedimento específico.

B) Pode detalhar a execução em sua competência, sem revogar a lei.

C) Suspende a lei apenas na jurisdição regional em que o procedimento se aplica.

D) Vincula a Administração mesmo se contrariar a base legal que regulamenta.


#### Extra Dia 3.7 — Comando negativo institucional

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Assinale a alternativa INCORRETA.

A) O decreto disciplina a execução da lei sem poder contrariá-la.

B) O CFA exerce atribuições nacionais de orientação e supervisão do sistema.

C) A autonomia do CRA-PR permite afastar orientação federal incompatível com sua gestão.

D) O CRA-PR exerce registro, orientação e fiscalização em sua jurisdição.


#### Extra Dia 3.8 — Competência e território

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Fato no Paraná possui orientação nacional. Qual análise é adequada?

A) Aplicar a orientação nacional e conferir a competência regional para executar ou fiscalizar.

B) Aplicar apenas a orientação regional, pois o território desloca a competência normativa.

C) Transferir a orientação nacional ao CRA-PR, que passa a defini-la para o caso.

D) Aplicar a orientação nacional sem conferir qual órgão tem competência executória.


#### Extra Dia 3.9 — Hierarquia e jurisdição

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Qual distinção está correta?

A) Jurisdição define força normativa; hierarquia define o território de aplicação.

B) Jurisdição delimita território; hierarquia ordena a força das fontes.

C) Jurisdição e hierarquia indicam, ambas, o órgão que praticará o ato.

D) Jurisdição e hierarquia são filtros equivalentes para o mesmo problema.


#### Extra Dia 3.10 — Caso integrado de fonte

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Decisão regional contraria lei alegando autonomia e eficiência. Qual resposta é correta?

A) Manter a decisão, pois eficiência permite flexibilizar competência no caso concreto.

B) Revogar a lei no âmbito regional, pois autonomia transfere força normativa.

C) Tratar a lei como orientação nacional, sem efeito sobre a decisão executória.

D) Reconhecer que autonomia e eficiência não afastam legalidade nem competência.


#### Extra Dia 3.11 — Referente inequívoco

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“Cadastro notificou Cobrança quando ele falhou.” Se Cobrança falhou, qual revisão elimina ambiguidade?

A) Quando ele falhou, Cadastro notificou Cobrança.

B) Quando Cobrança falhou, Cadastro enviou a notificação.

C) Quando Cadastro falhou, enviou a notificação a Cobrança.

D) Quando Cobrança falhou, enviou a notificação a Cadastro.


#### Extra Dia 3.12 — Paralelismo verbal

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Qual enumeração mantém paralelismo?

A) Modelar, a geração e que testes sejam.

B) Componentes modelados, gerar e rastreabilidade.

C) A modelagem, gerar e testes que rastreiam.

D) Modelar componentes, gerar código e rastrear testes.


#### Extra Dia 3.13 — Restritiva e explicativa

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Em “Os módulos que falharam serão reimplantados”, a oração:

A) restringe o conjunto aos módulos que falharam.

B) explica que todos os módulos falharam.

C) atribui à falha a causa da reimplantação.

D) informa que a reimplantação causou as falhas.


#### Extra Dia 3.14 — Conector conclusivo

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Qual conector introduz conclusão?

A) Embora.

B) Porque.

C) Portanto.

D) Contudo.


#### Extra Dia 3.15 — Escopo da negação

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“Nem todos os artefatos foram implantados” significa:

A) nenhum foi implantado.

B) alguns foram implantados e alguns não.

C) existe ao menos um não implantado.

D) exatamente um não foi implantado.


#### Extra Dia 3.16 — Possibilidade e garantia

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Um teste mostrou que a configuração pode funcionar no cenário. Qual reescrita preserva a força?

A) O resultado indica possibilidade no cenário avaliado, sem garantia para os demais.

B) O resultado recomenda uso nos demais ambientes, embora ainda precisem ser testados.

C) O resultado comprova funcionamento nos ambientes equivalentes ao cenário testado.

D) O resultado garante funcionamento sempre que o cenário se repete.


#### Extra Dia 3.17 — Ambiguidade técnica

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“O artefato foi enviado ao nó com sua configuração.” Se a configuração é do artefato, qual revisão é precisa?

A) O artefato e sua configuração foram enviados pelo nó de destino.

B) O nó recebeu o artefato acompanhado de sua própria configuração.

C) A configuração do nó foi enviada juntamente com o artefato.

D) O artefato, com a configuração correspondente, foi enviado ao nó.


#### Extra Dia 3.18 — Reescrita paralela

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

A instrução exige três ações da equipe: versionar o modelo, revisar o código e registrar o teste. Qual redação preserva agente, obrigação e paralelismo?

A) A equipe deve versionar o modelo, revisar o código e talvez registrar o teste.

B) A equipe deve versionar o modelo, revisar o código e registrar o teste.

C) À equipe cabem o versionamento do modelo, revisar o código e o registro do teste.

D) O modelo deve versionar a equipe, revisar o código e registrar o teste.


#### Extra Dia 3.19 — Três filtros de reescrita

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“Embora o build tenha passado, isso não garante todos os ambientes.” Qual versão preserva concessão, referente e força?

A) Embora o build tenha passado, o resultado não assegura a correção de todos os ambientes.

B) Como o build passou, o resultado assegura a correção em todos os ambientes.

C) Embora o build tenha passado, todos os ambientes dispensam nova validação.

D) Apesar de isso ter passado, eles não garantem a correção do ambiente.


#### Extra Dia 3.20 — Justificativa técnica precisa

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues) e [artefatos e deployment](semana_04_estudo.md#s4-d3-artefatos).

Qual justificativa distingue manifestação e deployment?

A) O arquivo concretiza o nó e, por isso, o componente passa a funcionar.

B) O nó manifesta o arquivo, enquanto o componente é implantado no ambiente.

C) O arquivo manifesta o componente e é implantado no nó de execução.

D) O deployment realiza a interface e dispensa o teste do componente.


## Gabarito - Dia 3

### Principais

| S4D3Q101 | S4D3Q102 | S4D3Q103 | S4D3Q104 | S4D3Q105 | S4D3Q106 | S4D3Q107 | S4D3Q108 | S4D3Q109 | S4D3Q110 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | B | C | D | B | D | A | C | C | A |

| S4D3Q111 | S4D3Q112 | S4D3Q113 | S4D3Q114 | S4D3Q115 | S4D3Q116 | S4D3Q117 | S4D3Q118 | S4D3Q119 | S4D3Q120 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | A | C | B | D | D | B | C | A |

| S4D3Q121 | S4D3Q122 | S4D3Q123 | S4D3Q124 | S4D3Q125 | S4D3Q126 | S4D3Q127 | S4D3Q128 | S4D3Q129 | S4D3Q130 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | B | A | C | B | D | D | B |

| S4D3Q131 | S4D3Q132 | S4D3Q133 | S4D3Q134 | S4D3Q135 | S4D3Q136 | S4D3Q137 | S4D3Q138 | S4D3Q139 | S4D3Q140 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | D | A | C | C | D | A | B |

| S4D3Q141 | S4D3Q142 | S4D3Q143 | S4D3Q144 | S4D3Q145 | S4D3Q146 | S4D3Q147 | S4D3Q148 | S4D3Q149 | S4D3Q150 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | B | B | D | C | B | D |

### Extras

| 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | B | D | D | B | C | A | B | D |

| 3.11 | 3.12 | 3.13 | 3.14 | 3.15 | 3.16 | 3.17 | 3.18 | 3.19 | 3.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | C | A | D | B | A | C |

## Comentários - Dia 3

### Comentário S4D3Q101

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O componente representa a unidade modular e não fixa o recurso de execução.
- **B)** Incorreta. Nó responde à arquitetura de execução, não à responsabilidade modular.
- **C)** Incorreta. Caminho representa comunicação entre nós, não um módulo.
- **D)** Incorreta. Artefato é peça física de informação, não a capacidade lógica.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q102

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A pergunta pede o módulo entregável, não um componente por classe interna.
- **B)** Correta. A granularidade modular concentra as classes internas sob um componente.
- **C)** Incorreta. Artefato não substitui a unidade modular nem seu contrato.
- **D)** Incorreta. As classes pertencem a Processos, não ao componente Portal.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q103

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A fusão aumenta acoplamento e dificulta a troca do provedor.
- **B)** Incorreta. Porta é ponto de interação, não fornecedor externo.
- **C)** Correta. A separação com contrato explícito limita o acoplamento à abstração.
- **D)** Incorreta. Topologia física não define a abstração lógica necessária.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q104

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Porta de nó pertence à visão de execução, não ao contrato oferecido.
- **B)** Incorreta. Classe iniciadora não define, por si, o serviço externo do componente.
- **C)** Incorreta. O artefato concretiza informação; não descreve o serviço oferecido.
- **D)** Correta. A interface explicita o serviço externo preservando encapsulamento.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q105

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Separação por tecnologia não cria responsabilidades coesas nem contratos explícitos.
- **B)** Correta. A solução melhora coesão sem ocultar integrações legítimas.
- **C)** Incorreta. Separação física com duplicação não resolve a mistura de responsabilidades.
- **D)** Incorreta. Ocultar dependências no desenho não reduz seu impacto real.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q106

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Essa é pergunta de deployment.
- **B)** Incorreta. Interação temporal é própria de sequência.
- **C)** Incorreta. Essa pergunta é tratada por estados.
- **D)** Correta. A visão organiza módulos e seus contratos.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q107

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Não há correspondência obrigatória um-para-um.
- **B)** Incorreta. Visibilidade pública não fixa a fronteira modular.
- **C)** Incorreta. Ser pública não torna a classe realizadora obrigatória de interface.
- **D)** Incorreta. Classe é classificador, não artefato implantável por definição.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q108

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Dependências só ganham sentido depois de existir responsabilidade e contrato reconhecíveis.
- **B)** Incorreta. Misturar a visão lógica com nó e artefato não define a capacidade modular.
- **C)** Correta. Responsabilidade e contrato tornam o elemento verificável.
- **D)** Incorreta. Detalhar realização interna antes do contrato não corrige a lacuna externa.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q109

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Isso acopla a regra às implementações.
- **B)** Incorreta. Contratos distintos não permitem trocar realizações sob a mesma abstração.
- **C)** Correta. O consumidor permanece estável enquanto a realização varia.
- **D)** Incorreta. Cobrança é consumidora do contrato, não sua realização substituta.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q110

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A análise segue os consumidores da interface afetada.
- **B)** Incorreta. Posição não estabelece dependência.
- **C)** Incorreta. Mudança lógica não afeta automaticamente todo recurso.
- **D)** Incorreta. Clientes que usam a operação podem quebrar.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q111

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Expor a realização reduz encapsulamento e não é requisito para substituição.
- **B)** Incorreta. Componente pode conter classificadores e também expor contratos.
- **C)** Incorreta. O nó posiciona execução, mas não determina a responsabilidade lógica.
- **D)** Correta. Encapsulamento controla exposição, não elimina estrutura interna.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q112

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Gabarito:** B (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. A requerida expressa Portal como consumidor dessa necessidade.
- **B)** Incorreta (gabarito). O diagrama declara contrato, mas não prova atributos operacionais.
- **C)** Correta. A fornecida expressa Cadastro como fornecedor do serviço.
- **D)** Correta. A montagem declara uma relação que deverá ser verificada.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** Limites da modelagem.

**Pegadinha:** Transformar relação declarada em prova de qualidade.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q113

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É quem cumpre o contrato.
- **B)** Incorreta. Relatórios requer o serviço, embora inicie a chamada.
- **C)** Incorreta. Invocar o contrato não torna Relatórios fornecedor junto com Cadastro.
- **D)** Incorreta. A interface define operações, mas quem as cumpre e fornece é Cadastro.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q114

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Isso afirmaria que Portal oferece o serviço.
- **B)** Incorreta. Necessidade não é recurso físico.
- **C)** Correta. A requerida explicita serviço necessário ao consumidor.
- **D)** Incorreta. Manifestação não expressa consumo.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q115

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Porta UML não identifica necessariamente porta TCP.
- **B)** Correta. A porta organiza comunicação na fronteira.
- **C)** Incorreta. Artefato pode manifestar elemento lógico, mas não é porta.
- **D)** Incorreta. Nó é recurso de execução, não ponto da fronteira do componente.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q116

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Manifestação envolve artefato.
- **B)** Incorreta. Ligação lógica não determina co-localização.
- **C)** Incorreta. Montagem não é generalização.
- **D)** Correta. A conexão casa necessidade e oferta compatíveis.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q117

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Une nós.
- **B)** Incorreta. Posiciona artefato em nó.
- **C)** Incorreta. Não expressa implementação do contrato.
- **D)** Correta. Associa implementador ao contrato.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q118

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Fornecedor não é cliente nessa relação.
- **B)** Correta. Parte do cliente dependente para o fornecedor.
- **C)** Incorreta. Dependência não é sempre bidirecional.
- **D)** Incorreta. Não é a relação lógica descrita.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q119

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Caminho conecta nós, não artefato e nó; esta última é implantação.
- **B)** Incorreta. As relações pertencem a perguntas e visões distintas.
- **C)** Correta. As relações respondem a visões distintas.
- **D)** Incorreta. Implantação e realização são relações diferentes das duas comparadas.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q120

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Porta UML é ponto de interação de um elemento, não endpoint de transporte TCP ou UDP.
- **B)** Correta. A interface fornecida formaliza um serviço que o componente oferece a seus consumidores.
- **C)** Correta. A interface requerida formaliza um serviço de que o componente depende para operar.
- **D)** Correta. A porta pode agrupar interfaces e explicitar um ponto de interação na fronteira do elemento.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q121

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A dependência concreta acopla Portal a uma implementação.
- **B)** Incorreta. Contratos diferentes não sustentam a mesma substituição transparente.
- **C)** Correta. Separa contrato, realizações e decisão de ambiente.
- **D)** Incorreta. Ativar apenas um não elimina o acoplamento direto a ambos.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Aplique direção do consumidor e realização pelas alternativas.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q122

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Encapsulamento protege clientes quando o contrato permanece.
- **B)** Incorreta. Refatoração lógica não exige migração física.
- **C)** Incorreta. Refatorar não inverte papéis de interfaces.
- **D)** Incorreta. A realização pode continuar vinculada ao contrato preservado.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Verifique primeiro se o contrato observável mudou.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q123

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Montagem não prova compatibilidade pelo nome.
- **B)** Incorreta. Assinatura aparente não resolve divergência semântica.
- **C)** Incorreta. Co-localização não corrige formato nem significado.
- **D)** Correta. Contrato envolve significado, não só aparência.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Cheque assinatura, significado e teste.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q124

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Detalhar a visão lógica não mostra ambientes nem caminhos físicos.
- **B)** Correta. A visão acrescenta onde e como executar.
- **C)** Incorreta. Classe associada a servidor mistura responsabilidade lógica e execução.
- **D)** Incorreta. Anotar endereços na visão lógica não substitui uma topologia de deployment.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Separe o que a visão atual responde e complemente-a.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q125

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Distingue interações sem duplicar responsabilidade.
- **B)** Incorreta. Duplica a responsabilidade e não separa adequadamente os canais.
- **C)** Incorreta. Caminho físico conecta nós, não representa contrato do canal.
- **D)** Incorreta. Um único contrato ocultaria a diferença entre os canais exigida no cenário.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Distinga responsabilidade, ponto e contrato.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q126

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O terceiro continua candidato porque depende da mesma interface e precisa ser confirmado.
- **B)** Incorreta. Revisar todos não significa alterar quem usa operação compatível.
- **C)** Correta. Dependência aponta candidatos; uso refina impacto.
- **D)** Incorreta. Alterar apenas o fornecedor não trata consumidores afetados pela assinatura.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Use dependência, operação usada e versionamento.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q127

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Consumo não é implementação.
- **B)** Correta. Requerer e realizar são papéis distintos.
- **C)** Incorreta. Receber e executar caracteriza fornecimento.
- **D)** Incorreta. Interface não é artefato.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Identifique consumidor, contrato e implementador.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q128

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Modelar estrutura interna não obriga expô-la aos consumidores.
- **B)** Incorreta. O contrato expõe apenas o necessário, não toda a realização.
- **C)** Incorreta. Parte lógica interna não se torna nó de execução.
- **D)** Correta. Detalhamento interno não obriga exposição total.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Separe detalhamento interno de exposição ao cliente.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q129

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O componente lógico não é implantado diretamente; um artefato faz a ponte.
- **B)** Incorreta. Artefato manifesta componente, e nó não manifesta artefato.
- **C)** Incorreta. Ambiente não manifesta componente, e artefato não realiza ambiente.
- **D)** Correta. Manifestação liga lógico a físico; deployment posiciona.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Componente lógico → artefato → nó.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q130

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Contrato lógico é interface, não nó.
- **B)** Correta. Essa é sua função.
- **C)** Incorreta. Sequência de mensagens pertence à visão de interação.
- **D)** Incorreta. Unidade modular com regra é componente, não nó.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Localize dispositivo, ambiente, artefato e caminho; só então avalie a topologia.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q131

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Troca as semânticas.
- **B)** Incorreta. Nenhuma classificação corresponde.
- **C)** Correta. Cada elemento ocupa a camada adequada.
- **D)** Incorreta. Não representa o cenário.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Classifique hardware, plataforma e peça.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q132

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Declara conectividade relevante entre nós.
- **B)** Incorreta. Liga implementador a contrato.
- **C)** Incorreta. Envolve artefato e elemento lógico.
- **D)** Incorreta. Não há especialização.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Localize dispositivo, ambiente, artefato e caminho; só então avalie a topologia.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q133

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não mostra conectividade.
- **B)** Incorreta. Contradiz a restrição.
- **C)** Incorreta. Realização não é caminho.
- **D)** Correta. Registra a mediação exigida.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Materialize apenas caminhos autorizados.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q134

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. As VMs são ambientes no dispositivo, não dispositivos contidos em componente.
- **B)** Incorreta. VM é ambiente de execução, não artefato.
- **C)** Incorreta. A contenção está invertida e caminho não substitui os ambientes.
- **D)** Correta. Separa hardware comum e contextos de execução.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Aplique recurso físico, virtualização e posicionamento.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q135

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra lógico, físico e conectividade.
- **B)** Incorreta. Componentes não são implantados diretamente e interfaces não são caminhos físicos.
- **C)** Incorreta. Nós não são manifestados por artefatos, e dependência não representa isolamento físico.
- **D)** Incorreta. Co-localização contradiz o isolamento e contrato não configura a topologia.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Verifique manifestação, destino e conectividade.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q136

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Os nós representados e seus papéis podem ser lidos no próprio diagrama.
- **B)** Incorreta. O caminho já declara a comunicação prevista.
- **C)** Correta. Caminho não prova todos os atributos.
- **D)** Incorreta. Artefatos e manifestação são outra pergunta, não os atributos do caminho declarado.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Separe conectividade de atributos verificáveis.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q137

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Uma implantação adicional não cria interface lógica.
- **B)** Incorreta. Um mesmo componente pode ser concretizado pelo artefato implantado em vários nós.
- **C)** Correta. Multiplicidade física pode cumprir a mesma responsabilidade.
- **D)** Incorreta. Pode ser o mesmo artefato nos dois nós, e a manifestação permanece válida.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Separe identidade lógica, pacote e multiplicidade.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q138

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não posiciona arquivo.
- **B)** Incorreta. Dispositivo não é interface.
- **C)** Incorreta. Não há especialização.
- **D)** Correta. Registra onde a peça é instalada/executada.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Pergunte se a relação explica o que o arquivo concretiza ou onde ele é instalado.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q139

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Nó é recurso; componente é módulo lógico.
- **B)** Correta. Dispositivo pode conter ambientes de execução.
- **C)** Correta. Artefato pode ser implantado em dispositivo ou ambiente.
- **D)** Correta. Caminho de comunicação conecta nós da topologia.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Localize dispositivo, ambiente, artefato e caminho; só então avalie a topologia.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q140

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A direção da manifestação e o elemento implantado estão trocados.
- **B)** Correta. Uma explica concretização; outra posicionamento.
- **C)** Incorreta. Artefato não realiza componente, e manifestação não posiciona o jar na JVM.
- **D)** Incorreta. Deployment não liga jar a componente e JVM não realiza artefato.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Filtre lógico, peça física e destino.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q141

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Variação de ambiente não cria responsabilidades lógicas distintas.
- **B)** Correta. Separa o comum do variável.
- **C)** Incorreta. Ambiente não é manifestado por configuração, e nó não é o item implantado.
- **D)** Incorreta. O modelo precisa registrar a configuração variável de cada ambiente.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Distinga componente, pacote e configuração.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q142

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mistura elementos lógicos com um artefato.
- **B)** Incorreta. Mistura nós e relação com um artefato.
- **C)** Incorreta. Mistura artefatos com componente e ambiente de execução.
- **D)** Correta. São peças físicas de informação.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Procure peças de informação concretas.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q143

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Conserva lógico, físico e destino.
- **B)** Incorreta. Componente não manifesta artefato, e JVM não é implantada no arquivo.
- **C)** Incorreta. JVM não manifesta componente, e artefato não é implantado em componente.
- **D)** Incorreta. Artefato manifesta componente, não o realiza; JVM não manifesta arquivo.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Classifique os elementos antes das relações.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q144

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Ligação apenas por nomes não cria cadeia rastreável entre evidências.
- **B)** Incorreta. Autoria do commit não o vincula ao requisito e ao teste.
- **C)** Correta. Cria a cadeia de evidências ausente.
- **D)** Incorreta. Build sem vínculo com requisito não resolve a causa da desconexão.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Use lacuna, vínculo e evidência.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q145

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Código não revela integralmente os requisitos que o originaram.
- **B)** Correta. Extrai estrutura, não toda a intenção.
- **C)** Incorreta. A estrutura atual pode divergir da arquitetura planejada.
- **D)** Incorreta. Estrutura extraída não comprova comportamento nem substitui testes.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Avalie observação, inferência e validação.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q146

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Esqueleto estrutural não prova requisitos não funcionais.
- **B)** Correta. Automação não substitui verificação.
- **C)** Incorreta. Código gerado também precisa de histórico próprio e rastreável.
- **D)** Incorreta. Alteração manual pode romper a sincronização.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Separe estrutura, comportamento e evidência.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q147

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Precedência fixa do modelo pode descartar correção válida do código.
- **B)** Incorreta. Precedência fixa do código pode ignorar decisão ainda não implementada.
- **C)** Incorreta. Compartilhar repositório não resolve conflito sem governança.
- **D)** Correta. Sincronização não resolve governança.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Combine sincronização, autoridade e revisão.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q148

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Faltam histórico de mudança, build versionado, teste e destino registrado.
- **B)** Incorreta. Tarefa sem commit, build local e teste sem versão quebram a cadeia.
- **C)** Correta. Cobre intenção, mudança, produto, verificação e destino.
- **D)** Incorreta. Código gerado e build não substituem teste nem registro de aceite/deployment.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Exija origem, mudança, build, teste e implantação.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q149

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Falta versionar antes da cópia, testar compatibilidade e registrar os destinos.
- **B)** Correta. Integra contrato, impacto, artefato, teste e topologia.
- **C)** Incorreta. Builds locais e validação de um único nó não controlam a mudança completa.
- **D)** Incorreta. Novo servidor não corrige contrato nem comprova compatibilidade.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Percorra contrato, consumidores, implementação, artefato, teste e destinos.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q150

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Builds locais continuam sem identidade reprodutível e a comparação manual não prova cada deployment.
- **B)** Incorreta. Recompilar sem ID não cria artefato imutável nem verifica ambos os nós.
- **C)** Incorreta. Build mutável e registro apenas do ambiente não controlam a deriva por nó.
- **D)** Correta. Trata coerência, reprodutibilidade e deriva operacional.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Aplique controle de fonte, identidade do artefato e evidência por destino.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


#### Comentário Extra Dia 3.1

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A lei dá a base e o decreto disciplina sua execução nos limites legais.
- **B)** Incorreta. Posterioridade do decreto não lhe permite afastar a lei.
- **C)** Incorreta. A lei federal não organiza apenas o conselho regional.
- **D)** Incorreta. Lei e decreto não têm o mesmo nível hierárquico.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.2

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O fato regional não transfere ao CRA-PR toda competência nacional.
- **B)** Incorreta. Atuação nacional não concentra no CFA toda execução regional.
- **C)** Correta. Combina integração e âmbito.
- **D)** Incorreta. Âmbitos distintos coexistem dentro do sistema integrado.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.3

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Regimento não amplia competência interna além da lei.
- **B)** Correta. Estrutura atuação interna sem superar lei.
- **C)** Incorreta. Regimento regional não substitui competências nacionais do CFA.
- **D)** Incorreta. Fonte interna não disciplina a profissão nem afasta decreto superior.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.4

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Autonomia regional continua integrada ao sistema nacional.
- **B)** Incorreta. Gestão regional não altera a hierarquia das fontes.
- **C)** Incorreta. Local do fato não transfere todas as competências nacionais.
- **D)** Correta. Autonomia e integração coexistem.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.5

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Território isolado não permite presumir competência.
- **B)** Incorreta. Fonte mais recente não prevalece automaticamente sobre superior.
- **C)** Incorreta. Finalidade e eficiência não afastam competência.
- **D)** Correta. Os filtros evitam transferências indevidas.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.6

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Cronologia e especialidade não tornam resolução superior à lei.
- **B)** Correta. Regulamentação é limitada pela hierarquia.
- **C)** Incorreta. Resolução não suspende lei no território regional.
- **D)** Incorreta. Procedimento administrativo continua vinculado à base legal.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.7

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Gabarito:** C (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. O Decreto nº 61.934/1967 disciplina a execução da Lei nº 4.769/1965.
- **B)** Correta. A atuação nacional do CFA integra a divisão institucional revisada.
- **C)** Incorreta (gabarito). Autonomia de gestão não permite afastar orientação federal válida.
- **D)** Correta. O CRA-PR exerce atribuições dentro de sua jurisdição e competência.

**Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.8

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A orientação nacional e a competência executória regional são filtros distintos.
- **B)** Incorreta. Território não desloca competência normativa nacional.
- **C)** Incorreta. Execução regional não transfere ao CRA-PR a definição da orientação nacional.
- **D)** Incorreta. Aplicar orientação sem conferir competência executória omite filtro indispensável.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.9

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte os papéis dos dois filtros.
- **B)** Correta. São dimensões diferentes.
- **C)** Incorreta. Nenhum dos filtros, isoladamente, identifica sempre o agente competente.
- **D)** Incorreta. Território e força da fonte são problemas distintos.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.10

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Eficiência não flexibiliza competência contra a lei.
- **B)** Incorreta. Autonomia não permite revogar lei em âmbito regional.
- **C)** Incorreta. Lei federal aplicável não se reduz a orientação sem efeito.
- **D)** Correta. Os filtros convergem.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.11

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O pronome continua com referente ambíguo.
- **B)** Correta. O nome fixa o referente.
- **C)** Incorreta. Torna Cadastro, e não Cobrança, o elemento que falhou.
- **D)** Incorreta. Torna Cobrança agente da notificação e muda o sentido.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.12

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mistura estruturas.
- **B)** Incorreta. Não é paralela.
- **C)** Incorreta. Mistura categorias.
- **D)** Correta. Três verbos no infinitivo.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.13

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Delimita o referente.
- **B)** Incorreta. A leitura de todos os módulos dependeria de oração explicativa.
- **C)** Incorreta. A oração delimita o conjunto; não estabelece, por si, relação causal.
- **D)** Incorreta. A oração não torna a reimplantação causa das falhas.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.14

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Marca concessão.
- **B)** Incorreta. Marca causa.
- **C)** Correta. Marca consequência/conclusão.
- **D)** Incorreta. Marca contraste.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.15

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. É mais forte.
- **B)** Incorreta. A frase admite que nenhum tenha sido implantado; não garante os dois grupos.
- **C)** Correta. Nega o universal por contraexemplo.
- **D)** Incorreta. A quantidade de não implantados não é determinada.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.16

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Mantém escopo e modalidade.
- **B)** Incorreta. Introduz recomendação de uso que o resultado não sustenta.
- **C)** Incorreta. Amplia a evidência para ambientes apenas considerados equivalentes.
- **D)** Incorreta. Transforma possibilidade observada em garantia repetível.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.17

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Torna o nó agente do envio e altera o sentido.
- **B)** Incorreta. “Sua” passa a ligar a configuração ao nó.
- **C)** Incorreta. Atribui a configuração ao nó, não ao artefato.
- **D)** Correta. A posse fica explícita.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.18

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. “Talvez” enfraquece apenas a terceira obrigação.
- **B)** Correta. Três deveres paralelos.
- **C)** Incorreta. Mistura construções nominais e verbais sem paralelismo.
- **D)** Incorreta. Atribui ao modelo a ação reservada à equipe.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.19

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. `Embora` mantém a concessão; `o resultado` explicita o referente; `não assegura` preserva a força.
- **B)** Incorreta. Troca concessão por causa e cria garantia geral.
- **C)** Incorreta. Mantém a concessão, mas conclui dispensa indevida de validação.
- **D)** Incorreta. Referentes vagos e escopo singular impedem preservar o sentido.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.20

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues) e [artefatos e deployment](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Artefato não concretiza nó, e funcionamento não decorre apenas da relação.
- **B)** Incorreta. Nó não manifesta arquivo, e componente não é implantado diretamente.
- **C)** Correta. Nomeia elementos e relações corretamente.
- **D)** Incorreta. Deployment não realiza interface nem elimina testes.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues) e [artefatos e deployment](semana_04_estudo.md#s4-d3-artefatos).


---
# Dia 4 - Engenharia de software, ciclos de vida e gerenciamento de projetos

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. A matriz inicial é 20/20/10 nas principais e 8/8/4 nas extras. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais - S4D4Q151 a S4D4Q200

### S4D4Q151 — Finalidade da engenharia

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Qual descrição melhor caracteriza engenharia de software?

A) Disciplina que aplica processo, método e controle ao desenvolvimento e à evolução.

B) Disciplina que concentra o desenvolvimento na produção e aprovação de modelos.

C) Automação que transforma requisitos informais em software validado.

D) Processo que congela requisitos para impedir mudanças durante o desenvolvimento.


### S4D4Q152 — Processo e produto

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

No fluxo “validar requisito”, qual é um produto observável?

A) Ata que comprova apenas a presença dos participantes.

B) Registro versionado da decisão e de seu resultado.

C) Relatório que informa somente a duração da reunião.

D) Histórico da ferramenta usada para projetar o requisito.


### S4D4Q153 — Método e ferramenta

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Assinale a distinção correta.

A) Método registra a execução; ferramenta define como executar.

B) Método organiza atividades; ferramenta decide quais são necessárias.

C) Método orienta a execução; ferramenta automatiza ou registra parte dela.

D) Método e ferramenta são produtos observáveis gerados pelo processo.


### S4D4Q154 — Adaptação proporcional

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Correção textual e integração de pagamentos usam controles idênticos e pesados. Qual decisão é coerente?

A) Usar o mesmo fluxo, mas dispensar versão na correção textual.

B) Reduzir controles da integração porque o prazo torna o risco aceitável.

C) Aplicar controles idênticos, pois proporcionalidade compromete auditoria.

D) Preservar controles mínimos e ampliá-los conforme risco e evidência exigida.


### S4D4Q155 — Evidência de validação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Houve reunião de requisitos, sem decisão nem versão. O que falta?

A) Um registro dos participantes, ainda que não informe a decisão.

B) Uma saída rastreável que registre critério e resultado da validação.

C) Uma nova reunião, desta vez sem interessados externos.

D) Uma ferramenta diferente, capaz de substituir a decisão humana.


### S4D4Q156 — Processo em cenário público

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Em sistema público sujeito a auditoria, qual prática combina adaptação e controle?

A) Registrar todas as atividades, ainda que decisões e versões não se relacionem.

B) Reduzir evidências nas mudanças críticas para acelerar a aprovação formal.

C) Aplicar o mesmo volume documental a toda mudança, sem classificar o risco.

D) Definir evidências pelo risco e rastrear decisões até teste e aceite.


### S4D4Q157 — Ênfase da cascata

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

A cascata enfatiza:

A) fases predominantemente sequenciais, com produtos e marcos definidos.

B) ciclos que priorizam os maiores riscos antes de planejar a volta seguinte.

C) entregas funcionais sucessivas que ampliam a capacidade do produto.

D) composição do sistema a partir de ativos previamente avaliados.


### S4D4Q158 — Núcleo da espiral

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual elemento distingue a espiral?

A) Sequência sem análise de incerteza.

B) Geração automática como marco.

C) Ciclos guiados pela identificação e redução de riscos.

D) Entrega integral antes de consultar usuários.


### S4D4Q159 — Reuso avaliado

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Antes de reutilizar componente pronto, deve-se avaliar:

A) adequação funcional, ignorando custos de adaptação já estimados.

B) preço de aquisição e prazo, transferindo o risco ao fornecedor.

C) adequação, adaptação, integração, teste, dependência e custo total.

D) compatibilidade técnica, sem considerar suporte e dependência futura.


### S4D4Q160 — Protótipo descartável

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Protótipo usa dados fixos e não tem segurança; valida navegação. O tratamento adequado é:

A) Registrar o aprendizado e reimplementar conforme arquitetura e controles produtivos.

B) Evoluir o mesmo código, ainda que seus atalhos não tenham sido avaliados.

C) Entregá-lo como incremento, limitando o aceite ao fluxo de navegação.

D) Mantê-lo como solução paralela para obter novo feedback em produção.


### S4D4Q161 — Protótipo evolutivo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Se o protótipo evoluirá até o produto, qual condição é essencial?

A) Manter os atalhos, desde que o protótipo já tenha validado a interface.

B) Adiar testes não funcionais até a primeira versão usada em produção.

C) Tratar o código como descartável, mesmo após decidir que será mantido.

D) Sustentar arquitetura, qualidade e critérios de evolução desde o início.


### S4D4Q162 — Condições para RAD

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual contexto favorece RAD?

A) Sistema acoplado, tecnologia inédita e validações esporádicas dos usuários.

B) Escopo modular, tecnologia conhecida e usuários disponíveis para decisões rápidas.

C) Escopo amplo, arquitetura incerta e equipe sem poder de decisão.

D) Sistema crítico integrado, prazo curto e indisponibilidade de especialistas.


### S4D4Q163 — Desenvolvimento evolutivo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

O desenvolvimento evolutivo caracteriza-se por:

A) amadurecer a solução em versões sucessivas orientadas por uso e feedback.

B) fechar a solução antes da primeira versão e preservar o escopo inicial.

C) compor a solução apenas com ativos existentes e evitar desenvolvimento novo.

D) prototipar a interface, descartar o resultado e manter requisitos estáveis.


### S4D4Q164 — Incremento funcional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual exemplo constitui incremento?

A) Reorganizar a implementação da consulta sem ampliar a função do portal.

B) Corrigir o desempenho interno da consulta mantendo a mesma capacidade.

C) Adicionar emissão de certificado ao portal que já oferece consulta.

D) Reexecutar os testes da consulta depois de atualizar a infraestrutura.


### S4D4Q165 — Iteração e incremento

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Assinale a distinção correta.

A) Iteração acrescenta capacidade; incremento apenas revisa trabalho existente.

B) Iteração refina trabalho; incremento acrescenta capacidade; ambos podem coexistir.

C) Iteração e incremento são sinônimos quando há mais de uma entrega.

D) Iteração ocorre na análise; incremento, exclusivamente na construção.


### S4D4Q166 — Cenário estável e marcos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Escopo regulatório estável, tecnologia conhecida e aprovações formais. Qual escolha é defensável?

A) Espiral com protótipos para reduzir a incerteza de tecnologia já conhecida.

B) Prototipação descartável promovida a produto após a aprovação do fluxo.

C) RAD sem participação de usuários, pois o escopo já está estável.

D) Cascata adaptada, com marcos, validações e controle de mudanças.


### S4D4Q167 — Cenário de alto risco

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Biometria inédita, integração instável e requisitos incertos dominam. Qual abordagem é alinhada?

A) Cascata com prova técnica adiada até o encerramento da construção.

B) Reuso do primeiro componente disponível, sem avaliar integração.

C) Incrementos funcionais, deixando o risco técnico para a entrega final.

D) Espiral com experimentos voltados à redução dos riscos dominantes.


### S4D4Q168 — Incerteza de interação

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Usuários não descrevem o fluxo, mas avaliam telas simuladas. Qual estratégia ajuda?

A) Cascata com aprovação da descrição incompleta antes de mostrar as telas.

B) Prototipação para aprender com as telas e registrar as decisões obtidas.

C) RAD sem participação dos usuários até a implantação da primeira versão.

D) Build automatizado para substituir a elicitação do fluxo desconhecido.


### S4D4Q169 — Custo total do reuso

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Componente gratuito exige adaptação, infraestrutura e suporte. A decisão considera:

A) preço de licença, pois custo zero torna a integração economicamente neutra.

B) tempo de procura, sem considerar a adaptação posterior do componente.

C) custo total e risco de integração, incluindo adaptação e suporte.

D) quantidade de funções, ainda que infraestrutura e suporte sejam incompatíveis.


### S4D4Q170 — Comando negativo sobre ciclos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Assinale a alternativa INCORRETA.

A) RAD dispensa arquitetura e aceite quando a velocidade é prioritária.

B) Espiral organiza os ciclos segundo os riscos que devem ser reduzidos.

C) Desenvolvimento incremental amplia a capacidade em partes utilizáveis.

D) Prototipação antecipa uma representação para apoiar a aprendizagem.


### S4D4Q171 — RAD sem atalho

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Módulo independente tem prazo curto e usuários disponíveis. Qual plano usa RAD adequadamente?

A) Prototipar rapidamente e deixar integração e aceite para a entrega final.

B) Componentizar sem limitar o escopo, aproveitando a disponibilidade dos usuários.

C) Prototipar e componentizar, com testes de integração e aceite frequentes.

D) Aplicar o mesmo plano ao sistema crítico, pois o prazo curto justifica RAD.


### S4D4Q172 — Reuso com incompatibilidade

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Biblioteca cobre 80%, mas protocolo, auditoria e suporte divergem. Qual decisão é madura?

A) Comparar adaptação, integração, testes, dependência e construção alternativa.

B) Adotar a biblioteca, pois cobertura de 80% compensa requisitos não atendidos.

C) Descartá-la, pois qualquer incompatibilidade impede reuso economicamente viável.

D) Adotá-la e transferir ao fornecedor a aceitação das lacunas restantes.


### S4D4Q173 — Mudança tardia em cascata

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Requisito muda durante construção em projeto sequencial. Qual resposta é adequada?

A) Recusar a mudança, pois o marco sequencial torna a baseline imutável.

B) Alterar o código e manter especificação e testes como referência original.

C) Reiniciar o projeto na concepção, independentemente do impacto apurado.

D) Analisar o impacto, decidir a mudança e atualizar produtos e baselines.


### S4D4Q174 — Volta da espiral

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

A equipe repete tarefas sem identificar nem tratar riscos. Qual avaliação é correta?

A) A repetição basta, pois a forma cíclica define o modelo espiral.

B) Falta orientar cada volta pela identificação e redução de riscos.

C) A repetição transforma o processo em cascata com retornos controlados.

D) A ausência de registro indica que os riscos já foram reduzidos.


### S4D4Q175 — Fatia incremental

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Como entregar valor cedo sem produzir camada técnica inutilizável isoladamente?

A) Entregar uma capacidade utilizável que atravesse as camadas necessárias.

B) Concluir a camada de dados inteira antes de iniciar qualquer função.

C) Entregar componentes técnicos isolados e integrá-los apenas ao final.

D) Dividir o trabalho pelo tamanho dos arquivos, sem critério de uso.


### S4D4Q176 — Iteração sem incremento

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual situação é iteração sem novo incremento?

A) Adicionar emissão de documento à versão que já permitia consulta.

B) Implantar uma nova função de consulta após o aceite dos usuários.

C) Revisar arquitetura e testes do mesmo incremento antes de entregá-lo.

D) Liberar uma segunda capacidade em versão posterior do produto.


### S4D4Q177 — Combinação contextual

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Projeto usa protótipo, espiral e incrementos. Isso é incoerente?

A) Sim; cada projeto precisa adotar um único modelo durante todo o ciclo.

B) Não; estratégias podem cumprir objetivos distintos sob controle comum.

C) Sim; prototipação e incremento sempre produzem artefatos incompatíveis.

D) Não; combinar estratégias torna desnecessário definir critérios de passagem.


### S4D4Q178 — Protótipo e segurança

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Protótipo evolutivo usará dados reais. Como evitar fragilidade?

A) Adiar segurança até a transição, mantendo apenas controles de usabilidade.

B) Definir segurança, arquitetura sustentável e gates de qualidade desde o início.

C) Tratar o código como descartável até a data de entrada em produção.

D) Usar a aprovação da interface como evidência de confidencialidade.


### S4D4Q179 — Incrementos e arquitetura

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Incrementos acumulam duplicação e dependências frágeis. Qual ação preserva evolução?

A) Proibir refatoração para preservar a velocidade de cada incremento isolado.

B) Adiar a integração até o fim, quando todas as capacidades estiverem prontas.

C) Tratar os incrementos como produtos separados, cada qual com sua arquitetura.

D) Refinar arquitetura, executar regressão e controlar dívida a cada ciclo.


### S4D4Q180 — Escolha por quatro critérios

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Escopo muda; valor é fatiável; integração tem alto risco; usuários estão disponíveis. Qual plano é defensável?

A) Usar cascata com teste final, pois a integração recomenda estabilizar o escopo.

B) Combinar incrementos e feedback com experimentos sobre o risco e controle arquitetural.

C) Usar RAD para acelerar, deixando a arquitetura emergir após os primeiros módulos.

D) Priorizar reuso para reduzir construção, mesmo sem ativos avaliados para a integração.


### S4D4Q181 — Finalidade da concepção

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Qual pergunta predomina na concepção?

A) A capacidade planejada foi integrada e verificada?

B) A solução está apta ao uso no ambiente-alvo?

C) A visão e o escopo inicial justificam o projeto?

D) A arquitetura reduziu os riscos centrais?


### S4D4Q182 — Finalidade da elaboração

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

A elaboração enfatiza:

A) arquitetura-base, riscos centrais e requisitos significativos.

B) visão inicial, caso de negócio e limites preliminares.

C) incrementos integrados, testes e documentação da solução.

D) migração, treinamento e aceite no ambiente operacional.


### S4D4Q183 — Finalidade da construção

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Na construção predomina:

A) delimitar visão, escopo inicial e viabilidade do esforço.

B) implementar, integrar e verificar a capacidade planejada.

C) preparar migração, treinamento e aceite no ambiente-alvo.

D) estabilizar arquitetura-base e reduzir os riscos centrais.


### S4D4Q184 — Finalidade da transição

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Qual conjunto associa-se à transição?

A) visão, atores, riscos iniciais e caso de negócio.

B) arquitetura-base, requisitos significativos e prova de risco.

C) código, incrementos integrados e testes da capacidade.

D) implantação, migração, treinamento e aceite operacional.


### S4D4Q185 — Atividades sobrepostas

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Código de protótipo aparece na elaboração para reduzir risco. Isso contradiz as fases?

A) Não; o código pode servir à redução do risco arquitetural dominante.

B) Sim; qualquer produção de código pertence exclusivamente à construção.

C) Não; as quatro fases têm a mesma finalidade e podem se substituir.

D) Sim; na elaboração só se admitem requisitos e diagramas conceituais.


### S4D4Q186 — Marco de elaboração

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Há muitos requisitos, mas arquitetura e integração crítica estão incertas. A elaboração acabou?

A) Sim; o volume de requisitos demonstra maturidade suficiente para o marco.

B) Sim; arquitetura e integração devem ser verificadas apenas na construção.

C) Não; ainda faltam evidências sobre arquitetura e riscos centrais.

D) Não; requisitos significativos não fazem parte dos produtos da elaboração.


### S4D4Q187 — Transição completa

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Pacote foi copiado; migração, treinamento e monitoramento faltam. Avalie.

A) A transição terminou, pois o pacote já está no ambiente de destino.

B) A transição deve ser reiniciada, descartando o deployment já executado.

C) O deployment ocorreu, mas a prontidão operacional ainda não foi demonstrada.

D) A construção não terminou, pois migração e treinamento pertencem a ela.


### S4D4Q188 — Fases sem rigidez

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Assinale a alternativa INCORRETA.

A) Elaboração prioriza riscos arquiteturais antes da construção predominante.

B) Construção implementa e integra a capacidade definida para a iteração.

C) Transição busca uso efetivo da solução no ambiente-alvo.

D) Requisitos só podem ser discutidos durante a fase de concepção.


### S4D4Q189 — Cadeia de evidências

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Há visão aceita, prova arquitetural, incrementos testados e plano de migração não executado. Qual leitura?

A) Há evidências das três primeiras fases; a transição ainda requer execução e validação.

B) Há apenas concepção; as demais evidências são planos sem resultado observável.

C) Há transição concluída; o plano de migração basta como evidência operacional.

D) Há elaboração e transição, mas os incrementos testados não provam construção.


### S4D4Q190 — Comando negativo sobre fases

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Assinale a alternativa INCORRETA.

A) Transição termina com a cópia do artefato para o ambiente-alvo.

B) Concepção delimita visão, escopo inicial e justificativa do projeto.

C) Elaboração trata arquitetura-base e riscos centrais do projeto.

D) Construção implementa, integra e verifica a capacidade planejada.


### S4D4Q191 — Fases do projeto e operação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

O CRA autoriza um portal após aprovar a justificativa; a equipe detalha as baselines, produz entregas enquanto mede desvios e decide correções, obtém o aceite e transfere o resultado. Depois começa o suporte mensal. Qual leitura é correta?

A) Autorização é planejamento; baselines são iniciação; produção é controle; aceite é execução; suporte é encerramento.

B) Autorização é iniciação; baselines são planejamento; execução convive com acompanhamento e controle; aceite e transferência encerram; suporte é operação.

C) Autorização é execução; baselines são controle; produção é encerramento; aceite inicia a operação; suporte mantém o projeto permanente.

D) Autorização é concepção do RUP; baselines são elaboração; produção dispensa controle; aceite é transição; suporte integra o mesmo projeto.


### S4D4Q192 — Planejar, acompanhar e controlar

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

Há cronograma-base; relatório mostra atraso; gerente analisa e aprova replanejamento. Qual sequência?

A) Planejamento definiu a baseline; acompanhamento aprovou o replanejamento.

B) Planejamento definiu e mediu; controle apenas registrou o atraso observado.

C) Acompanhamento definiu a baseline; controle mediu e planejou a resposta.

D) Planejamento definiu; acompanhamento mediu; controle decidiu e atualizou.


### S4D4Q193 — WBS e cronograma

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

WBS lista entregas hierárquicas; cronograma, atividades e datas. Conclui-se que:

A) WBS decompõe o escopo; cronograma organiza o trabalho no tempo.

B) WBS ordena atividades; cronograma decompõe as entregas do escopo.

C) WBS distribui pessoas; cronograma define os pacotes de trabalho.

D) WBS e cronograma representam a mesma estrutura, com níveis distintos.


### S4D4Q194 — Mudança de escopo integrada

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

Solicita-se novo módulo sem alterar prazo, equipe, orçamento ou qualidade. Qual conduta?

A) Aceitar e acrescentar o módulo à WBS, preservando as demais baselines.

B) Rejeitar, pois uma baseline aprovada torna qualquer mudança inadmissível.

C) Avaliar efeitos em escopo, prazo, custo, qualidade, recursos e riscos.

D) Alterar apenas escopo e orçamento, pois prazo e qualidade foram fixados.


### S4D4Q195 — Tempo, custo e dependência

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

Fornecedor atrasa atividade crítica dez dias e gera ociosidade. Qual análise é completa?

A) Recalcular prazo e custo, executar a resposta ao risco e controlar a mudança.

B) Atualizar o cronograma e manter o orçamento, pois a ociosidade não gera custo.

C) Cobrar o fornecedor e manter as baselines até a atividade voltar ao plano.

D) Remover a dependência crítica do cronograma para preservar o marco original.


### S4D4Q196 — Qualidade e comunicação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas e comunicação](semana_04_estudo.md#s4-d4-qualidade-pessoas-comunicacao).

Requisito diz “rápido”; direção recebe relatório técnico sem decisão clara. Qual plano resolve ambos?

A) Quantificar “rápido” e manter o mesmo relatório técnico para todos os públicos.

B) Definir medida e teste; adaptar a comunicação à decisão, preservando os fatos.

C) Manter “rápido” e resumir o relatório, retirando resultados desfavoráveis.

D) Usar ausência de reclamações como medida e enviar o painel sem contexto.


### S4D4Q197 — Pessoas, comunicação e risco

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Especialista ficará indisponível antes de integração crítica. Qual resposta integrada?

A) Esperar a indisponibilidade e então redistribuir as tarefas da integração.

B) Adicionar pessoas no último dia e manter papéis e comunicação inalterados.

C) Registrar o risco sem resposta, para não antecipar mudança de responsabilidade.

D) Tratar o risco, transferir conhecimento, ajustar papéis e comunicar marcos.


### S4D4Q198 — Aquisição não transfere tudo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Serviço externo será contratado, sem interface e aceite definidos. Qual afirmação é correta?

A) Contratar por preço e prazo, deixando integração e aceite sob risco do fornecedor.

B) Definir o aceite depois da entrega, quando a interface real estiver disponível.

C) Definir escopo, aceite, riscos, responsáveis e integração antes da contratação.

D) Tratar a integração após o encerramento, quando o serviço já estiver transferido.


### S4D4Q199 — Mudança com cinco impactos

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Mudança amplia usuários, exige fornecedor, eleva carga e altera data. Qual decisão integra?

A) Atualizar WBS, prazo e custo, mantendo capacidade e comunicação já aprovadas.

B) Reavaliar escopo, prazo, custo, qualidade, comunicação, riscos e aquisição.

C) Aprovar a mudança e registrar apenas os impactos que alterarem a data final.

D) Rejeitar a mudança, pois fornecedor e aumento de carga impedem análise integrada.


### S4D4Q200 — Cenário integrado de controle

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Painel mostra atraso; risco virou problema; aquisição depende de integração fora da WBS; teste não tem limite. Qual ação é completa?

A) Tratar o atraso, manter a WBS e aceitar o teste qualitativo até nova medição.

B) Cobrar o fornecedor, incluir a integração na WBS e manter o limite de teste aberto.

C) Tratar problema e risco residual, corrigir WBS e aceite, replanejar e comunicar.

D) Replanejar o prazo, encerrar o risco ocorrido e comunicar somente após o aceite.


## Questões extras - Dia 4

#### Extra Dia 4.1 — Legalidade e eficiência

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Eficiência administrativa:

A) deve ser buscada dentro da legalidade e da competência administrativa.

B) permite flexibilizar procedimento sempre que houver ganho mensurável.

C) supre ausência de competência quando o resultado atende ao interesse público.

D) converte ato lento em inválido, ainda que praticado conforme a lei.


#### Extra Dia 4.2 — Impessoalidade

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Publicidade com promoção pessoal conflita principalmente com:

A) descentralização administrativa e controle de resultados.

B) autotutela administrativa e revisão dos próprios atos.

C) impessoalidade administrativa e finalidade pública.

D) especialidade administrativa e definição de competência.


#### Extra Dia 4.3 — Publicidade e proteção

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Qual afirmação é coerente?

A) A publicidade exige publicar dados pessoais ligados a qualquer ato administrativo.

B) A publicidade favorece transparência, respeitados sigilo legal e proteção de dados.

C) A proteção de dados afasta a publicidade sempre que houver identificação pessoal.

D) A publicidade permite promoção pessoal quando a informação institucional é verdadeira.


#### Extra Dia 4.4 — Desconcentração

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Criar coordenação na mesma pessoa jurídica é:

A) descentralização pela criação de nova entidade.

B) descentralização pela delegação a um particular.

C) desconcentração com criação de nova pessoa jurídica.

D) desconcentração dentro da mesma pessoa jurídica.


#### Extra Dia 4.5 — Autarquia

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Autarquia integra:

A) Administração Direta, como órgão sem personalidade jurídica própria.

B) Administração Indireta, como pessoa jurídica de direito privado.

C) Administração Direta, como entidade com autonomia apenas financeira.

D) Administração Indireta, como pessoa jurídica de direito público.


#### Extra Dia 4.6 — Anulação e revogação

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Ato ilegal; ato válido inconveniente são retirados, respectivamente, por:

A) revogação; anulação.

B) anulação; revogação.

C) desconcentração; descentralização.

D) delegação; avocação.


#### Extra Dia 4.7 — Controle e decisão

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Indicador revela desvio, mas ninguém age. Avalie.

A) Houve controle completo, pois o painel tornou o desvio visível.

B) Houve decisão de controle, mas faltou medir o resultado obtido.

C) Houve acompanhamento, mas faltou decisão para completar o controle.

D) Não houve acompanhamento, pois nenhum ato corretivo foi executado.


#### Extra Dia 4.8 — Cenário organizacional

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Distribuir atribuições entre unidades internas sem nova pessoa caracteriza:

A) desconcentração administrativa.

B) descentralização por outorga.

C) descentralização por delegação.

D) centralização administrativa.


#### Extra Dia 4.9 — Comando negativo administrativo

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Assinale a alternativa INCORRETA.

A) A eficiência administrativa deve permanecer dentro da legalidade.

B) A publicidade exige divulgar dado pessoal sempre que o ato for público.

C) A impessoalidade impede usar a atuação institucional para promoção pessoal.

D) A autarquia integra a Administração Indireta e possui personalidade própria.


#### Extra Dia 4.10 — Caso integrado administrativo

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Ato ilegal é eficiente e popular. Qual providência conceitual?

A) Revogar o ato por inconveniência, pois a eficiência não foi suficiente.

B) Convalidar o ato, pois resultado popular permite superar vícios de competência.

C) Manter o ato, pois eficiência e popularidade compensam a ilegalidade.

D) Tratar a ilegalidade pela anulação, verificando competência e limites aplicáveis.


#### Extra Dia 4.11 — Implicação

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

“Se marco atrasar, custo aumentará” é falsa somente quando:

A) marco não atrasa e custo aumenta.

B) marco atrasa e custo não aumenta.

C) ambos ocorrem.

D) nenhum ocorre.


#### Extra Dia 4.12 — Contrapositiva

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Contrapositiva de “se teste passou, build foi gerado”:

A) se build foi gerado, teste passou.

B) se teste não passou, build não gerou.

C) teste passou e build não gerou.

D) se build não foi gerado, teste não passou.


#### Extra Dia 4.13 — Negação de conjunção

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Negar “escopo aprovado e risco tratado” resulta em:

A) escopo não aprovado ou risco não tratado.

B) escopo não aprovado e risco não tratado.

C) escopo aprovado ou risco tratado.

D) se escopo aprovado, então risco tratado.


#### Extra Dia 4.14 — Negação universal

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Negar “todo incremento foi testado” é:

A) nenhum foi testado.

B) exatamente um foi testado.

C) existe ao menos um não testado.

D) todos foram testados duas vezes.


#### Extra Dia 4.15 — Aumento percentual

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Custo passou de 80 para 100 mil. O aumento foi:

A) 20%.

B) 80%.

C) 25%.

D) 125%.


#### Extra Dia 4.16 — Exposição simples

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Probabilidade 20% e impacto R$ 50.000 produzem:

A) R$ 10.000.

B) R$ 2.500.

C) R$ 50.020.

D) R$ 250.000.


#### Extra Dia 4.17 — Base percentual reversa

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Após aumento de 25%, custo é 100 mil. Base era:

A) R$ 75 mil.

B) R$ 125 mil.

C) R$ 25 mil.

D) R$ 80 mil.


#### Extra Dia 4.18 — Comparação de riscos

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

A: 10%×100 mil; B: 40%×20 mil. Pelo valor esperado:

A) A vale 1 mil e B vale 80 mil; B é maior.

B) A vale 10 mil e B vale 8 mil; A é maior.

C) B deve ser priorizado porque sua probabilidade isolada é maior.

D) A e B têm a mesma exposição após ponderar probabilidade e impacto.


#### Extra Dia 4.19 — Implicação e percentual

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Se risco ocorrer, custo cresce 25%. O risco ocorreu e base era 80 mil. Conclui-se:

A) novo custo de 100 mil.

B) custo de 20 mil.

C) nada pode ser concluído.

D) custo de 60 mil.


#### Extra Dia 4.20 — Cálculo e limite

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Riscos: 20%×50 mil e 10%×30 mil. Avalie.

A) Exposições de R$ 70 mil; a soma dos impactos define a prioridade.

B) Exposições de R$ 10 mil e R$ 30 mil; a maior probabilidade define a prioridade.

C) Exposições de R$ 10 mil e R$ 3 mil; o cálculo não substitui análise qualitativa.

D) Exposições de R$ 50 mil e R$ 30 mil; esses valores ocorrerão com certeza.


## Gabarito - Dia 4

### Principais

| S4D4Q151 | S4D4Q152 | S4D4Q153 | S4D4Q154 | S4D4Q155 | S4D4Q156 | S4D4Q157 | S4D4Q158 | S4D4Q159 | S4D4Q160 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | B | C | D | B | D | A | C | C | A |

| S4D4Q161 | S4D4Q162 | S4D4Q163 | S4D4Q164 | S4D4Q165 | S4D4Q166 | S4D4Q167 | S4D4Q168 | S4D4Q169 | S4D4Q170 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | A | C | B | D | D | B | C | A |

| S4D4Q171 | S4D4Q172 | S4D4Q173 | S4D4Q174 | S4D4Q175 | S4D4Q176 | S4D4Q177 | S4D4Q178 | S4D4Q179 | S4D4Q180 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | B | A | C | B | B | D | B |

| S4D4Q181 | S4D4Q182 | S4D4Q183 | S4D4Q184 | S4D4Q185 | S4D4Q186 | S4D4Q187 | S4D4Q188 | S4D4Q189 | S4D4Q190 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | B | D | A | C | C | D | A | A |

| S4D4Q191 | S4D4Q192 | S4D4Q193 | S4D4Q194 | S4D4Q195 | S4D4Q196 | S4D4Q197 | S4D4Q198 | S4D4Q199 | S4D4Q200 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | A | B | D | C | B | C |

### Extras

| 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 4.6 | 4.7 | 4.8 | 4.9 | 4.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | B | D | D | B | C | A | B | D |

| 4.11 | 4.12 | 4.13 | 4.14 | 4.15 | 4.16 | 4.17 | 4.18 | 4.19 | 4.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | C | A | D | B | A | C |

## Comentários - Dia 4

### Comentário S4D4Q151

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra produção, qualidade, mudança e evidência.
- **B)** Incorreta. Engenharia não se concentra apenas na produção e aprovação de modelos.
- **C)** Incorreta. Automação não transforma requisito informal em produto validado sem trabalho humano.
- **D)** Incorreta. Engenharia administra mudanças; não se define por impedi-las.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q152

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Presença dos participantes não registra a decisão de validação.
- **B)** Correta. Documenta o resultado da validação.
- **C)** Incorreta. Duração da reunião não é o resultado da validação.
- **D)** Incorreta. Histórico da ferramenta não substitui a decisão sobre o requisito.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q153

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte orientação do método e registro da ferramenta.
- **B)** Incorreta. Ferramenta não decide sozinha as atividades necessárias.
- **C)** Correta. Os papéis são complementares.
- **D)** Incorreta. Método e ferramenta apoiam a execução; não são produtos do processo por definição.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q154

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mudança simples ainda precisa de versionamento mínimo.
- **B)** Incorreta. Prazo urgente não torna aceitável reduzir controle de integração crítica.
- **C)** Incorreta. Proporcionalidade por risco é compatível com auditoria quando produz evidência adequada.
- **D)** Correta. Adapta disciplina sem removê-la.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q155

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Lista de participantes não informa qual decisão foi tomada.
- **B)** Correta. Sem ela não se sabe o que foi aceito.
- **C)** Incorreta. Nova reunião sem interessados não cria a evidência ausente.
- **D)** Incorreta. Ferramenta diferente não substitui decisão humana rastreável.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q156

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Volume sem vínculo entre decisão e versão não garante rastreabilidade.
- **B)** Incorreta. Mudanças críticas exigem mais evidência proporcional, não menos.
- **C)** Incorreta. Controle idêntico sem classificar risco ignora a adaptação proporcional.
- **D)** Correta. Oferece proporcionalidade e auditabilidade.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q157

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Progressão organizada é seu traço central.
- **B)** Incorreta. Ciclos guiados por riscos caracterizam a espiral.
- **C)** Incorreta. Entregas funcionais sucessivas caracterizam desenvolvimento incremental.
- **D)** Incorreta. Composição com ativos avaliados caracteriza desenvolvimento baseado em reuso.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q158

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Contraria a espiral.
- **B)** Incorreta. Ferramenta não define modelo.
- **C)** Correta. Risco orienta objetivo e próximo passo.
- **D)** Incorreta. Há avaliação por ciclo.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q159

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Adequação funcional isolada não elimina custos de adaptação.
- **B)** Incorreta. Preço e prazo não transferem ao fornecedor todo o risco.
- **C)** Correta. Reuso é decisão técnica e econômica.
- **D)** Incorreta. Compatibilidade técnica isolada ignora suporte e dependência futura.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q160

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Preserva conhecimento sem promover atalhos.
- **B)** Incorreta. Evoluir atalhos não avaliados transforma dívida exploratória em risco de produto.
- **C)** Incorreta. Aceite de navegação não torna o protótipo incremento produtivo.
- **D)** Incorreta. Colocar solução frágil em produção não é condição para obter novo feedback.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q161

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Validação da interface não torna aceitável conservar todos os atalhos.
- **B)** Incorreta. Código destinado à produção precisa considerar qualidade não funcional desde cedo.
- **C)** Incorreta. Depois da decisão de mantê-lo, tratá-lo como descartável orienta controles inadequados.
- **D)** Correta. O código mantido precisa ser sustentável.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q162

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Acoplamento, tecnologia inédita e feedback esporádico não sustentam RAD.
- **B)** Correta. Condições sustentam rapidez com feedback.
- **C)** Incorreta. Escopo amplo e decisões indisponíveis impedem ciclos rápidos controlados.
- **D)** Incorreta. Criticidade integrada e especialistas indisponíveis elevam risco para adoção direta de RAD.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q163

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Entendimento e solução evoluem.
- **B)** Incorreta. Fechar solução antes da primeira versão contraria a evolução por feedback.
- **C)** Incorreta. Uso exclusivo de ativos existentes caracteriza reuso, não evolução.
- **D)** Incorreta. Protótipo descartável com requisitos estáveis não descreve amadurecimento do produto.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q164

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Reorganização interna sem nova função não agrega capacidade utilizável.
- **B)** Incorreta. Melhoria interna de desempenho, no cenário, não adiciona função ao produto.
- **C)** Correta. Amplia capacidade utilizável.
- **D)** Incorreta. Reexecutar testes é verificação, não nova capacidade.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q165

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte refinamento iterativo e acréscimo incremental.
- **B)** Correta. São conceitos independentes.
- **C)** Incorreta. Repetição de entrega não torna os dois conceitos sinônimos.
- **D)** Incorreta. Iteração não se limita à análise nem incremento exclusivamente à construção.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q166

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Tecnologia conhecida reduz a justificativa para experimento orientado a risco como eixo.
- **B)** Incorreta. Protótipo descartável não deve ser promovido a produto apenas pelo fluxo aprovado.
- **C)** Incorreta. RAD exige participação e decisões rápidas dos usuários.
- **D)** Correta. As condições favorecem sequência planejada.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q167

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Adiar prova técnica conserva o risco dominante.
- **B)** Incorreta. Disponibilidade do primeiro componente não prova adequação.
- **C)** Incorreta. Entrega incremental não reduz, sozinha, o risco técnico adiado.
- **D)** Correta. Risco define objetivos.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q168

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Aprovar descrição incompleta antes das telas preserva a incerteza.
- **B)** Correta. Torna feedback concreto.
- **C)** Incorreta. Excluir usuários até a implantação adia a aprendizagem necessária.
- **D)** Incorreta. Build automatizado não elicita fluxo desconhecido.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q169

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Licença gratuita não neutraliza adaptação, infraestrutura e suporte.
- **B)** Incorreta. Tempo de procura isolado não representa o custo total futuro.
- **C)** Correta. Custos indiretos podem dominar.
- **D)** Incorreta. Quantidade de funções não resolve incompatibilidade de infraestrutura e suporte.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q170

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Velocidade não permite dispensar arquitetura e aceite.
- **B)** Correta. A espiral organiza ciclos em torno da identificação e redução de riscos.
- **C)** Correta. Desenvolvimento incremental amplia a capacidade em partes utilizáveis.
- **D)** Correta. Prototipação pode tornar requisitos incertos concretos para aprendizagem.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q171

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Deixar integração e aceite para o final remove feedback e evidência frequentes.
- **B)** Incorreta. Escopo ilimitado elimina o recorte que favorece RAD.
- **C)** Correta. Rapidez não remove qualidade.
- **D)** Incorreta. Prazo curto não autoriza generalizar o plano a sistema crítico sem análise.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque modularidade, feedback e controles.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q172

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cobertura parcial não resolve críticos.
- **B)** Incorreta. Cobertura de 80% não compensa automaticamente requisitos críticos ausentes.
- **C)** Incorreta. Incompatibilidade pode ser tratável por adaptação economicamente viável.
- **D)** Incorreta. O órgão conserva a responsabilidade de aceitar o resultado.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Combine adequação, restrições e custo/risco.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q173

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Baseline sequencial pode ser alterada pela governança competente.
- **B)** Incorreta. Alterar só o código cria divergência com especificação e testes.
- **C)** Incorreta. Retorno à concepção depende do impacto, não é automático.
- **D)** Correta. Preserva coerência entre fases.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Verifique produtos, restrições e decisão.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q174

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Forma cíclica sem orientação por risco não basta.
- **B)** Correta. O ciclo deve ser dirigido por risco.
- **C)** Incorreta. Repetição sem risco não transforma necessariamente o processo em cascata.
- **D)** Incorreta. Ausência de registro não demonstra redução de riscos.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Diferencie forma circular de finalidade.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q175

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Entrega resultado utilizável.
- **B)** Incorreta. Camada técnica completa, isoladamente, não entrega a função utilizável.
- **C)** Incorreta. Componentes técnicos isolados adiam o valor até a integração final.
- **D)** Incorreta. Tamanho de arquivo não corresponde a capacidade de uso.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque valor, integração mínima e aceite.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q176

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Emissão de documento adiciona nova capacidade.
- **B)** Incorreta. Nova função de consulta entregue é incremento.
- **C)** Correta. Há refinamento sem nova capacidade entregue.
- **D)** Incorreta. Segunda capacidade liberada também é incremento.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Separe refinamento de capacidade entregue.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q177

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não há obrigação de exclusividade de um modelo por todo o ciclo.
- **B)** Correta. Ênfases podem compor abordagem contextual.
- **C)** Incorreta. Protótipo e incremento podem produzir artefatos com papéis compatíveis.
- **D)** Incorreta. Combinação aumenta, não elimina, a necessidade de critérios de passagem.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Verifique finalidade, compatibilidade e governança.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q178

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Dados reais tornam segurança relevante antes da transição.
- **B)** Correta. Código permanente precisa de controles.
- **C)** Incorreta. Código destinado a evoluir não deve ser tratado como descartável até a produção.
- **D)** Incorreta. Usabilidade e confidencialidade são dimensões distintas.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Integre permanência, exposição e qualidade.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q179

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Proibir refatoração preserva dívida e degrada capacidade futura.
- **B)** Incorreta. Adiar integração posterga incompatibilidades entre incrementos.
- **C)** Incorreta. O produto acumulado exige coerência arquitetural comum.
- **D)** Correta. Combina valor e integridade.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque valor, arquitetura e regressão.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q180

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Teste final e estabilização forçada não respondem à mudança nem ao risco alto.
- **B)** Correta. Atende aos quatro condicionantes.
- **C)** Incorreta. RAD sem controle arquitetural atende prazo, mas ignora risco e evolução.
- **D)** Incorreta. Reuso sem ativos avaliados não responde à integração de alto risco.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Aplique mudança, valor, risco e feedback.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q181

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Capacidade integrada e verificada é pergunta de construção.
- **B)** Incorreta. Aptidão no ambiente-alvo é pergunta de transição.
- **C)** Correta. Delimita propósito e viabilidade.
- **D)** Incorreta. Redução de riscos arquiteturais é pergunta de elaboração.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q182

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Reduz incerteza arquitetural.
- **B)** Incorreta. Visão e caso de negócio predominam na concepção.
- **C)** Incorreta. Incrementos integrados e testes predominam na construção.
- **D)** Incorreta. Migração, treinamento e aceite predominam na transição.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q183

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Visão, escopo e viabilidade predominam na concepção.
- **B)** Correta. O produto é desenvolvido e testado.
- **C)** Incorreta. Migração, treinamento e aceite predominam na transição.
- **D)** Incorreta. Arquitetura-base e riscos predominam na elaboração.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q184

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Visão, atores e caso de negócio são evidências de concepção.
- **B)** Incorreta. Arquitetura-base e prova de risco são evidências de elaboração.
- **C)** Incorreta. Código e testes são evidências de construção, não de uso operacional.
- **D)** Correta. Busca aptidão ao uso.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q185

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Atividade não é proibida fora da fase dominante.
- **B)** Incorreta. Restringir todo código à construção transforma ênfase em proibição.
- **C)** Incorreta. As fases possuem finalidades predominantes distintas.
- **D)** Incorreta. Elaboração também pode usar código exploratório para reduzir risco.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Distinga atividade de finalidade predominante.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q186

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Volume documental não substitui evidência sobre arquitetura e risco.
- **B)** Incorreta. Arquitetura e integração crítica devem ser tratadas na elaboração.
- **C)** Correta. O marco reflete a finalidade.
- **D)** Incorreta. Requisitos significativos participam dos produtos da elaboração.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Cheque arquitetura, riscos e plano.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q187

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Pacote no destino não demonstra migração, treinamento e monitoramento.
- **B)** Incorreta. Não é preciso descartar o deployment para completar a transição.
- **C)** Correta. Instalação é apenas parte.
- **D)** Incorreta. Migração e treinamento pertencem à transição, não provam falta de construção.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Separe instalação, prontidão e aceite.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q188

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Gabarito:** D (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. Elaboração enfatiza arquitetura-base e riscos centrais.
- **B)** Correta. Construção implementa, integra e verifica a capacidade planejada.
- **C)** Correta. Transição busca colocar a solução em uso no ambiente-alvo.
- **D)** Incorreta (gabarito). Requisitos podem ser refinados em fases posteriores; concepção indica uma ênfase, não uma exclusividade.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Identifique absoluto que transforma ênfase em proibição.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q189

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Plano sozinho não conclui a última.
- **B)** Incorreta. Prova arquitetural e incrementos testados são resultados observáveis das fases seguintes.
- **C)** Incorreta. Plano de migração sem execução não conclui a transição.
- **D)** Incorreta. Incrementos testados são evidência de construção, e a transição ainda não ocorreu.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Mapeie evidência e diferencie plano de resultado.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q190

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Cópia do artefato não basta para demonstrar prontidão operacional.
- **B)** Correta. Concepção delimita visão, escopo inicial e viabilidade.
- **C)** Correta. Elaboração enfrenta riscos arquiteturais relevantes.
- **D)** Correta. Construção produz e verifica incrementos da solução.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q191

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Troca iniciação por planejamento, inverte a função das baselines e desloca execução, encerramento e operação.
- **B)** Correta. A autorização inicia; as baselines planejam; entrega e medição coexistem; aceite e transferência encerram; suporte recorrente é operação.
- **C)** Incorreta. A autorização não é execução, e a continuidade do suporte não transforma o esforço temporário em projeto permanente.
- **D)** Incorreta. Mistura fases do processo de desenvolvimento com fases de gerenciamento e elimina indevidamente o controle durante a execução.

**Conceito:** Fases de projeto e distinção entre projeto, processo de desenvolvimento e operação.

**Pegadinha:** Confundir fases de projeto com fases do RUP e tratar execução e controle como compartimentos incompatíveis.

**Como pensar:** Associe cada evidência à sua finalidade: autorizar, planejar, produzir, medir/decidir, aceitar/transferir e operar.

**Referência à apostila de estudo:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).


### Comentário S4D4Q192

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Acompanhamento mede; não aprova, por si, o replanejamento.
- **B)** Incorreta. Medição pertence ao acompanhamento, não ao planejamento.
- **C)** Incorreta. Planejamento define baseline e acompanhamento mede antes do controle.
- **D)** Correta. As funções aparecem com evidência.

**Conceito:** Gerenciamento de projetos.

**Pegadinha:** Confundir medição com controle ou projeto com operação.

**Como pensar:** Localize baseline, dado real e decisão.

**Referência à apostila de estudo:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).


### Comentário S4D4Q193

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Respondem a perguntas diferentes.
- **B)** Incorreta. A alternativa inverte decomposição de escopo e ordenação temporal.
- **C)** Incorreta. Distribuição de pessoas não é WBS, e cronograma não define pacotes.
- **D)** Incorreta. Os artefatos respondem a perguntas diferentes, não a níveis da mesma estrutura.

**Conceito:** Escopo, decomposição e restrições.

**Pegadinha:** Usar WBS como cronograma ou tratar mudança isoladamente.

**Como pensar:** Separe o que entregar de quando executar.

**Referência à apostila de estudo:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).


### Comentário S4D4Q194

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Preservar demais baselines ignora impactos cruzados da mudança.
- **B)** Incorreta. Baseline aprovada admite mudança por governança informada.
- **C)** Correta. Mudança atravessa áreas.
- **D)** Incorreta. Alterar apenas escopo e orçamento cria divergência com prazo e qualidade.

**Conceito:** Escopo, decomposição e restrições.

**Pegadinha:** Usar WBS como cronograma ou tratar mudança isoladamente.

**Como pensar:** Aplique trabalho, restrições e riscos.

**Referência à apostila de estudo:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).


### Comentário S4D4Q195

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Conecta tempo, custo, risco e decisão.
- **B)** Incorreta. Ociosidade pode gerar custo e deve entrar na análise integrada.
- **C)** Incorreta. Cobrança sem atualizar baselines posterga o controle do impacto.
- **D)** Incorreta. Remover a dependência do cronograma não remove a dependência real.

**Conceito:** Escopo, decomposição e restrições.

**Pegadinha:** Usar WBS como cronograma ou tratar mudança isoladamente.

**Como pensar:** Causa → dependência → prazo → custo → resposta.

**Referência à apostila de estudo:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).


### Comentário S4D4Q196

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas e comunicação](semana_04_estudo.md#s4-d4-qualidade-pessoas-comunicacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Quantificar ajuda a qualidade, mas a mesma comunicação não atende todos os públicos.
- **B)** Correta. Cria evidência e comunicação útil.
- **C)** Incorreta. “Rápido” continua vago e retirar resultado desfavorável distorce os fatos.
- **D)** Incorreta. Ausência de reclamação não mede desempenho, e painel sem contexto não orienta decisão.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Combine medida, teste, interessado e decisão.

**Referência à apostila de estudo:** [Qualidade, pessoas e comunicação](semana_04_estudo.md#s4-d4-qualidade-pessoas-comunicacao).


### Comentário S4D4Q197

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Esperar a indisponibilidade perde a oportunidade de prevenir impacto.
- **B)** Incorreta. Pessoas sem preparo não garantem competência, e papéis permanecem frágeis.
- **C)** Incorreta. Registro sem resposta não trata a exposição identificada.
- **D)** Correta. Trata probabilidade, capacidade e interessados.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Integre risco, competência, responsável e comunicação.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


### Comentário S4D4Q198

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O órgão mantém responsabilidade por integração e aceite.
- **B)** Incorreta. Definir aceite depois da entrega posterga um critério contratual essencial.
- **C)** Correta. Fornecedor não absorve tudo.
- **D)** Incorreta. Integração deve ser planejada e acompanhada durante o projeto.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Cheque compra, aceite, integração e responsabilidade.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


### Comentário S4D4Q199

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Mantém sem revisão capacidade e comunicação afetadas pela ampliação de usuários.
- **B)** Correta. Todos os efeitos entram.
- **C)** Incorreta. Registrar apenas impactos de data ignora os demais efeitos integrados.
- **D)** Incorreta. Fornecedor e carga exigem análise; não impedem toda mudança automaticamente.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Percorra efeitos e exija baselines coerentes.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


### Comentário S4D4Q200

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Mantém a lacuna de WBS e aceita critério de teste sem limite.
- **B)** Incorreta. Inclui integração na WBS, mas não define limite de aceite nem trata o problema completo.
- **C)** Correta. Corrige os pontos integrados.
- **D)** Incorreta. Risco ocorrido vira problema; não deve ser simplesmente encerrado sem risco residual.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Meça, trate, atualize escopo, defina qualidade e controle.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


#### Comentário Extra Dia 4.1

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Princípios convivem.
- **B)** Incorreta. Ganho mensurável não autoriza flexibilizar procedimento aplicável por si só.
- **C)** Incorreta. Resultado útil não supre ausência de competência.
- **D)** Incorreta. Lentidão não transforma automaticamente ato legal em inválido.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.2

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Descentralização e controle não tratam promoção pessoal.
- **B)** Incorreta. Autotutela e revisão de atos não são o princípio violado no caso.
- **C)** Correta. Comunicação institucional não serve à promoção.
- **D)** Incorreta. Especialidade e competência não são o eixo da promoção pessoal.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.3

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Publicidade de ato não torna todo dado pessoal publicável.
- **B)** Correta. Não é absoluta.
- **C)** Incorreta. Proteção de dados e publicidade precisam ser compatibilizadas no caso concreto.
- **D)** Incorreta. Verdade da informação não autoriza promoção pessoal.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.4

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A criação de nova entidade caracteriza descentralização, o que não ocorreu.
- **B)** Incorreta. Não houve delegação a particular.
- **C)** Incorreta. Desconcentração não cria nova pessoa jurídica.
- **D)** Correta. Distribui competências internamente.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.5

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Autarquia não integra a Administração Direta e possui personalidade própria.
- **B)** Incorreta. Autarquia é pessoa jurídica de direito público, não privado.
- **C)** Incorreta. Não integra a Administração Direta nem possui apenas autonomia financeira.
- **D)** Correta. É a classificação revisada.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.6

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Ordem invertida.
- **B)** Correta. Legalidade e mérito distinguem.
- **C)** Incorreta. São organizacionais.
- **D)** Incorreta. Não correspondem.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.7

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Visibilidade do desvio não completa o controle sem decisão.
- **B)** Incorreta. O cenário contém medição; o que falta é decisão de controle.
- **C)** Correta. Informação precisa gerar ação.
- **D)** Incorreta. O desvio foi medido, portanto houve acompanhamento.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.8

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Mantém a mesma pessoa.
- **B)** Incorreta. Não houve outorga a nova entidade.
- **C)** Incorreta. Não houve delegação da execução a outra pessoa.
- **D)** Incorreta. Distribuir atribuições internas não concentra competências.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.9

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Gabarito:** B (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. A eficiência administrativa deve permanecer dentro da legalidade.
- **B)** Incorreta (gabarito). Interesse público do ato não elimina limites à divulgação de dados pessoais.
- **C)** Correta. Impessoalidade veda o uso da atuação institucional para promoção pessoal.
- **D)** Correta. Autarquia integra a Administração Indireta e possui personalidade de direito público.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.10

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ilegalidade conduz à análise de anulação, não de revogação por mérito.
- **B)** Incorreta. Resultado popular não torna todo vício de competência convalidável.
- **C)** Incorreta. Eficiência e popularidade não prevalecem sobre a legalidade.
- **D)** Correta. Legalidade precede mérito.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.11

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Antecedente falso.
- **B)** Correta. É verdadeiro→falso.
- **C)** Incorreta. V→V é verdadeiro.
- **D)** Incorreta. F→F é verdadeiro.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.12

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Recíproca.
- **B)** Incorreta. Inversa.
- **C)** Incorreta. Negação.
- **D)** Correta. Nega e inverte.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.13

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. De Morgan.
- **B)** Incorreta. Exigir ambas as negações é mais forte que negar a conjunção.
- **C)** Incorreta. A disjunção das afirmações positivas não nega a conjunção.
- **D)** Incorreta. A implicação muda o conectivo e não é a negação pedida.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.14

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Mais forte.
- **B)** Incorreta. Não decorre.
- **C)** Correta. Contraexemplo nega universal.
- **D)** Incorreta. Contradiz.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.15

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Usa base final.
- **B)** Incorreta. Confunde base.
- **C)** Correta. 20/80 = 25%.
- **D)** Incorreta. É razão final/base.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.16

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. 0,20×50.000.
- **B)** Incorreta. Multiplicação errada.
- **C)** Incorreta. Soma grandezas.
- **D)** Incorreta. Divisão indevida.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.17

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Subtrai percentual do final.
- **B)** Incorreta. Direção inversa.
- **C)** Incorreta. Confunde percentual e base.
- **D)** Correta. 100/1,25=80.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.18

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Os produtos corretos são 10% de 100 mil = 10 mil e 40% de 20 mil = 8 mil.
- **B)** Correta. As exposições são 10 mil para A e 8 mil para B; portanto, A é maior.
- **C)** Incorreta. A comparação exige probabilidade e impacto, não apenas a probabilidade isolada.
- **D)** Incorreta. As exposições calculadas são diferentes: 10 mil e 8 mil.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.19

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. 80×1,25.
- **B)** Incorreta. É só acréscimo.
- **C)** Incorreta. Antecedente confirmado.
- **D)** Incorreta. Sinal oposto.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.20

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Soma impactos sem multiplicar pelas probabilidades.
- **B)** Incorreta. O segundo produto correto é R$ 3 mil, e probabilidade isolada não define prioridade.
- **C)** Correta. Produtos e limite corretos.
- **D)** Incorreta. Usa impactos como exposições e transforma incerteza em certeza.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


---
