# Apostila de Estudo - Semana 2

## CRA-PR 2026 - Analista de Sistemas

**Versão 1.0**

Esta apostila organiza a segunda semana de preparação para o concurso do CRA-PR 2026. O foco principal é construir domínio operacional de redes de computadores, segurança de redes e sistemas operacionais avançados, sem abandonar as revisões recorrentes de Legislação CRA/CFA, Língua Portuguesa, Administração Pública e Raciocínio Lógico-Matemático.

A teoria, os exemplos e as práticas foram planejados para sustentar integralmente a resolução da apostila de questões da mesma semana.

## Versão do edital utilizada

- Concurso: CRA-PR, Edital de Concurso Público nº 1/2026.
- Cargo: Analista de Sistemas.
- Banca: Instituto Consulplan.
- Arquivo local preservado como recebido: `../edital/edital_cra_pr_2026_analista_sistemas_retificacao_1.pdf`.
- Situação documental: apesar do nome do arquivo local, seu conteúdo corresponde ao edital anterior à Retificação I e ainda menciona a RN CFA nº 640/2024.
- Fonte normativa vigente adotada: edital oficial consolidado conforme Retificação I, publicado pela banca, que substitui a RN CFA nº 640/2024 pela RN CFA nº 671/2025.
- Data provável da prova: 13/09/2026, sujeita à confirmação nas publicações posteriores da banca e no Cartão de Confirmação de Inscrição.

Para Analista de Sistemas, a Retificação I não alterou os tópicos técnicos, a estrutura da prova nem a data provável. Na disciplina Legislação CRA-PR/CFA, o escopo aplicável ao cargo compreende a Lei nº 4.769/1965, o Decreto nº 61.934/1967, o Regimento Interno do CRA-PR e o Código de Ética da RN CFA nº 671/2025.

## Mapa de pontuação e prioridade

| Disciplina | Questões | Pontos | Prioridade na semana |
|---|---:|---:|---|
| Conhecimentos do Cargo | 15 | 30 | Muito alta |
| Legislação CRA-PR/CFA | 10 | 20 | Muito alta |
| Língua Portuguesa | 10 | 20 | Muito alta |
| Administração Pública e Legislação Correlata | 5 | 10 | Média |
| Raciocínio Lógico-Matemático | 5 | 10 | Média |
| Informática | 5 | 10 | Menor, mas obrigatória |

Conhecimentos do Cargo, Legislação CRA-PR/CFA e Língua Portuguesa somam 70 pontos. Por isso, o tema técnico ocupa 4h30 por dia, e as matérias de revisão permanecem distribuídas ao longo da semana.

## Como usar esta apostila

1. Leia o objetivo e os resultados esperados antes de iniciar o dia.
2. Siga o cronograma de 6h líquidas e mantenha as pausas fora dessa contagem.
3. Estude os mecanismos, não apenas os nomes: desenhe redes, calcule sub-redes, acompanhe encapsulamentos e simule incidentes.
4. Resolva a prática guiada sem consultar a explicação e depois compare o raciocínio.
5. Use as tabelas rápidas somente após estudar a teoria completa.
6. Registre no caderno de erros a causa do erro, a regra correta, um exemplo próprio e a data da próxima revisão.
7. Ao resolver as questões, volte à subseção teórica indicada em cada comentário.

## Rotina diária fixa de 6h líquidas

| Bloco | Tempo líquido | Atividade |
|---|---:|---|
| Bloco principal 1 | 2h | Teoria central e construção do mapa conceitual |
| Bloco principal 2 | 1h30 | Aprofundamento, comparações e exemplos resolvidos |
| Bloco principal 3 | 1h | Prática guiada e questões principais |
| Revisão fixa | 40min | Legislação CRA/CFA, Administração Pública ou RLM, conforme o dia |
| Português | 30min | Interpretação, semântica, reescrita ou gramática aplicada |
| Caderno de erros | 20min | Recuperação ativa e registro das lacunas |
| **Total** | **6h** | **360 minutos líquidos** |

Pausas sugeridas: 10 minutos após o primeiro bloco, 15 minutos após o segundo, 10 minutos após o terceiro e 5 minutos antes do caderno de erros. As pausas não integram as 6h líquidas.

## Mapa da Semana 2

| Dia | Tema principal | Revisão fixa | Entrega do dia |
|---|---|---|---|
| 1 | Topologias, LAN/WAN, meios e equipamentos | Legislação CRA/CFA + Português | mapa de topologias, equipamentos e domínios |
| 2 | OSI, TCP/IP, endereçamento e CIDR | Administração Pública + Português | quadro de camadas e folha de cálculos IPv4 |
| 3 | Protocolos e serviços de rede | Legislação CRA/CFA + Português | mapa de portas, transportes e fluxos de serviço |
| 4 | Segurança de redes | Administração Pública + RLM + Português curto | matriz ameaça-controle e roteiro de incidente |
| 5 | Sistemas operacionais avançados | Legislação CRA/CFA + Português | mapa de sincronização, deadlock, E/S e arquivos |
| 6 | Revisão integrada e estudo de caso | Português + caderno de erros | diagnóstico e plano técnico para um conselho profissional |

## Delimitação da cobertura

O edital menciona expressamente redes, topologias, componentes, comunicação de dados, meios de transmissão, LAN/WAN, OSI, TCP/IP, serviços e protocolos, equipamentos, ataques, firewall, DMZ, redes sem fio, VPN, gerência de rede, concorrência, sincronização, deadlock, dispositivos, sistemas de arquivos e aspectos práticos de Windows/Linux.

Esta semana aprofunda esses núcleos e seus desdobramentos necessários, como IPv4/IPv6, CIDR, sub-redes, NAT/PAT, criptografia, certificados, TLS, IDS/IPS e mecanismos clássicos de sincronização. Padrões W3C e gerência de rede aparecem apenas de modo contextual; permanecem para aprofundamento nas semanas posteriores.

---

# Dia 1 - Redes: topologias, LAN/WAN e equipamentos

<a id="s2-d1-objetivo"></a>
## Objetivo do dia

Construir uma visão funcional de redes de computadores, relacionando comunicação de dados, topologias, alcance geográfico, meios de transmissão e equipamentos. O foco não é decorar uma lista de nomes, mas entender o que cada elemento recebe, examina, repete, filtra ou encaminha e quais efeitos produz nos domínios de colisão e de broadcast.

<a id="s2-d1-resultados"></a>
## Resultados esperados

Ao final do dia, você deve conseguir:

- explicar os componentes básicos de uma comunicação de dados;
- diferenciar topologia física de topologia lógica;
- reconhecer barramento, estrela, anel, malha e topologia híbrida;
- diferenciar PAN, LAN, MAN e WAN sem depender apenas de distância;
- comparar meios guiados e não guiados;
- escolher, em cenário simples, entre par trançado, fibra óptica e comunicação sem fio;
- explicar o papel de placa de rede, repetidor, hub, bridge, switch, roteador, gateway e access point;
- distinguir bridge de switch, hub de switch, roteador de gateway e access point de roteador sem fio;
- contar corretamente domínios de colisão e de broadcast em topologias básicas;
- interpretar alternativas que misturam função física, função lógica e produto multifuncional;
- revisar os pontos de Legislação CRA/CFA e Português necessários às questões extras do dia.

<a id="s2-d1-importancia"></a>
## Por que esse assunto importa para a prova

Redes de computadores integram os Conhecimentos do Cargo e servem de base para os próximos dias da Semana 2. Protocolos, endereçamento, segurança, serviços e diagnóstico só ficam claros quando você entende o caminho físico e lógico dos dados.

Para o Analista de Sistemas, o tema também é prático. Uma falha descrita como "a rede caiu" pode estar em uma placa de rede, em um enlace, em uma porta de switch, no access point, no roteamento ou no provedor WAN. Saber separar essas funções evita diagnósticos imprecisos.

As questões de prova costumam explorar pares semelhantes. Uma alternativa pode acertar a descrição do equipamento, mas trocar a camada de atuação, afirmar que ele interrompe broadcast quando não interrompe ou atribuir roteamento a um equipamento que apenas faz bridging.

<a id="s2-d1-estilo-consulplan"></a>
## Como pode ser cobrado no estilo Instituto Consulplan

São formatos compatíveis com o estilo de cobrança:

- cenário de uma repartição que precisa interligar estações, servidores e rede sem fio;
- associação entre equipamento e função;
- identificação da topologia física ou lógica;
- comparação de alcance e finalidade entre LAN, MAN, WAN e PAN;
- afirmações I, II e III sobre meios de transmissão;
- contagem de domínios de colisão e broadcast em um diagrama;
- alternativa incorreta que chama switch de repetidor ou access point de roteador;
- troca entre largura de banda, throughput, latência e jitter;
- uso de termos absolutos, como "sempre", "somente" e "elimina qualquer colisão", sem considerar a topologia ou o modo duplex.

Estratégia de leitura: identifique primeiro a função exigida pelo enunciado. Depois verifique qual informação o equipamento precisa examinar para executá-la — sinal, endereço MAC, endereço IP ou protocolo de aplicação.

<a id="s2-d1-cronograma"></a>
## Cronograma de 6h líquidas com pausas sugeridas

| Bloco | Tempo líquido | Atividade |
|---|---:|---|
| 1 | 2h | Fundamentos, comunicação de dados, topologias, PAN/LAN/MAN/WAN e meios de transmissão |
| 2 | 1h30 | Placas de rede, repetidores, hubs, bridges, switches, roteadores, gateways e access points |
| 3 | 1h | Domínios de colisão e broadcast, diferenças entre equipamentos e exemplos guiados |
| 4 | 40min | Revisão fixa de Legislação CRA/CFA |
| 5 | 30min | Português e interpretação de enunciados |
| 6 | 20min | Caderno de erros e recuperação ativa |
| **Total** | **6h** | **360 minutos líquidos** |

Pausas sugeridas, fora das 6h líquidas: 10min após o Bloco 1, 15min após o Bloco 2, 10min após o Bloco 3 e 5min antes do caderno de erros.

<a id="s2-d1-teoria"></a>
## Teoria explicada de forma didática

<a id="s2-d1-fundamentos"></a>
### 1. Conceitos fundamentais de redes

Uma rede de computadores é um conjunto de sistemas e dispositivos capazes de trocar dados por enlaces e protocolos. A rede não se resume ao cabo ou ao Wi-Fi. Ela reúne elementos físicos, regras lógicas, endereços, serviços e mecanismos de controle.

Conceitos básicos:

- **nó:** qualquer elemento conectado que participe da comunicação, como estação, servidor, impressora, switch ou roteador;
- **host:** sistema final que origina ou consome comunicação, como computador, celular ou servidor;
- **interface de rede:** ponto lógico e físico pelo qual um dispositivo se conecta à rede;
- **enlace:** meio de comunicação entre interfaces ou nós diretamente conectados;
- **protocolo:** conjunto de regras sobre formato, sequência e significado das mensagens;
- **serviço:** capacidade oferecida a outra camada ou aplicação, como transportar dados ou resolver nomes;
- **recurso compartilhado:** impressora, armazenamento, aplicação ou conexão que pode ser acessada pela rede;
- **internetwork:** conjunto de redes interligadas por roteadores — a Internet é a maior internetwork pública.

Redes permitem compartilhamento, comunicação, centralização de serviços, redundância e administração. Esses benefícios trazem custos: dependência de infraestrutura, necessidade de segurança, monitoramento, capacidade e disponibilidade.

#### Rede, Internet e Web

- **Rede** é o conceito geral de sistemas interconectados.
- **Internet** é uma rede mundial de redes baseada na suíte de protocolos da Internet.
- **Web** é um serviço de aplicação que utiliza a Internet, normalmente por HTTP ou HTTPS.

A Internet pode transportar e-mail, voz, arquivos e vários outros serviços. Portanto, Internet e Web não são sinônimos.

<a id="s2-d1-comunicacao-dados"></a>
### 2. Comunicação de dados

Uma comunicação de dados depende de cinco elementos conceituais:

1. **Emissor:** origina os dados.
2. **Receptor:** recebe os dados.
3. **Mensagem:** conteúdo transmitido.
4. **Meio:** caminho físico ou sem fio.
5. **Protocolo:** regras que permitem interpretar a troca.

Se dois equipamentos estão fisicamente conectados, mas usam parâmetros ou protocolos incompatíveis, a comunicação pode falhar. Conectividade física é necessária, mas não é suficiente.

#### Direção da comunicação

| Modo | Funcionamento | Exemplo didático |
|---|---|---|
| Simplex | dados seguem em uma direção | transmissão de um sensor que apenas envia |
| Half-duplex | ambos os lados podem transmitir, mas não ao mesmo tempo | rádio comunicador |
| Full-duplex | ambos transmitem simultaneamente | enlace Ethernet comutado em full-duplex |

Não confunda duplex com quantidade de dispositivos. Duplex descreve a possibilidade de transmissão nos dois sentidos, simultânea ou alternada.

#### Medidas de desempenho

- **Largura de banda:** capacidade nominal ou faixa disponível do enlace.
- **Throughput ou vazão:** quantidade efetivamente entregue por unidade de tempo.
- **Goodput:** parcela útil percebida pela aplicação, descontadas sobrecargas e retransmissões.
- **Latência:** tempo para os dados percorrerem o caminho.
- **Jitter:** variação da latência entre entregas.
- **Perda:** dados que não chegam ao destino.

Um enlace de 1 Gbit/s não garante goodput de 1 Gbit/s. Cabeçalhos, contenção, processamento, retransmissões e capacidade do destino podem reduzir a taxa útil. A distância aumenta a latência e, conforme o protocolo, o tamanho das janelas e as perdas do caminho, também pode reduzir a vazão efetiva.

<a id="s2-d1-topologias"></a>
### 3. Topologia física e topologia lógica

**Topologia física** descreve como cabos, rádios, portas e dispositivos estão dispostos. **Topologia lógica** descreve como os dados circulam e como o acesso ao meio é organizado.

As duas topologias podem divergir. Uma rede fisicamente em estrela com hub funciona logicamente como meio compartilhado, semelhante a um barramento: o hub retransmite o sinal recebido às demais portas. Uma estrela com switch cria enlaces ponto a ponto entre cada estação e sua porta, e o switch decide se deve encaminhar, inundar ou filtrar um quadro.

#### Barramento

Todos os nós compartilham um meio principal. Nas formas Ethernet históricas, uma transmissão podia ser percebida ao longo do segmento e colisões eram possíveis.

- Vantagem histórica: pouco cabeamento.
- Limitação: compartilhamento do meio, dificuldade de isolamento de falhas e dependência do segmento principal.
- Pegadinha: chamar qualquer rede Ethernet de barramento. Ethernet moderna costuma usar estrela física com switches.

#### Estrela

Cada nó possui enlace com um ponto central.

- Com switch, é a organização dominante de LANs Ethernet.
- A falha de um cabo de acesso tende a afetar apenas o nó ligado a ele.
- A falha do equipamento central pode afetar toda a estrela.
- A presença de um centro não informa, sozinha, o comportamento lógico — um hub e um switch produzem comportamentos diferentes.

#### Anel

Cada nó se conecta conceitualmente ao seguinte, formando caminho fechado. O tráfego pode circular em um sentido ou em sentidos controlados, conforme a tecnologia.

- Pode usar passagem de token para ordenar o acesso.
- Um anel sem redundância ou mecanismos de contorno pode ser sensível a falhas.
- Anel físico e anel lógico também podem divergir em implementações específicas.

#### Malha

Há múltiplos caminhos entre os nós.

- **Malha completa:** cada nó possui ligação direta com todos os outros.
- **Malha parcial:** apenas alguns pares possuem ligações diretas redundantes.
- Vantagem: redundância e caminhos alternativos.
- Custo: mais enlaces, portas e complexidade de controle.

Em uma malha completa com `n` nós, o número de enlaces ponto a ponto é:

`n x (n - 1) / 2`.

Para 5 nós: `5 x 4 / 2 = 10` enlaces.

#### Híbrida

Combina duas ou mais topologias. Uma organização pode ter estrelas de acesso em cada andar, interligadas por um anel ou por enlaces redundantes entre switches centrais.

| Topologia | Organização principal | Ponto forte | Atenção de prova |
|---|---|---|---|
| Barramento | meio compartilhado linear | simplicidade histórica | falha e contenção afetam o segmento |
| Estrela | enlaces convergem para centro | isolamento dos enlaces de acesso | o centro pode ser ponto crítico |
| Anel | caminho fechado entre nós | acesso ordenado em certas tecnologias | falha pode interromper o ciclo sem proteção |
| Malha | múltiplos enlaces entre nós | redundância | custo e complexidade crescem |
| Híbrida | combinação de topologias | adaptação ao projeto | deve ser analisada por partes |

<a id="s2-d1-alcance"></a>
### 4. PAN, LAN, MAN e WAN

As classificações por alcance ajudam, mas não são medidas rígidas em quilômetros. Também importam finalidade, administração e tecnologia.

| Tipo | Escopo típico | Exemplo | Observação |
|---|---|---|---|
| PAN | entorno pessoal | celular, relógio e fone conectados | pode usar Bluetooth ou outra tecnologia de curto alcance |
| LAN | residência, sala, prédio ou campus administrado localmente | rede do edifício do CRA-PR | pode ser cabeada ou sem fio |
| MAN | região metropolitana | interligação de unidades em uma cidade | costuma usar infraestrutura de operadora ou rede metropolitana própria |
| WAN | cidades, estados, países ou continentes | conexão entre matriz e unidades distantes | agrega enlaces de longa distância e redes intermediárias |

Uma WLAN continua sendo LAN, apenas com acesso sem fio. Wi-Fi não é sinônimo de Internet: é possível ter Wi-Fi local funcionando e não ter acesso à Internet.

<a id="s2-d1-meios"></a>
### 5. Meios guiados e não guiados

Nos **meios guiados**, o sinal percorre um caminho físico, como cobre ou fibra. Nos **meios não guiados**, propaga-se pelo espaço, como ondas de rádio.

#### Par trançado

O par trançado usa pares de condutores de cobre. O trançamento ajuda a reduzir interferência e diafonia.

- **UTP:** sem blindagem adicional.
- **STP e variantes blindadas:** acrescentam proteção contra interferência, mas exigem instalação e aterramento adequados.
- É comum no acesso Ethernet de estações, telefones IP e access points.
- Distância, categoria, conectores e padrão Ethernet precisam ser compatíveis.

O par trançado não é imune a interferência eletromagnética. A blindagem não transforma cobre em fibra.

#### Fibra óptica

A fibra transmite luz por núcleo óptico.

- **Monomodo:** núcleo menor e propagação adequada a distâncias maiores, conforme óptica e padrão usados.
- **Multimodo:** vários modos de propagação, comum em enlaces internos e datacenters, conforme distância e velocidade projetadas.
- É imune a interferência eletromagnética por não conduzir o sinal como corrente elétrica.
- Oferece alta capacidade e alcance, mas requer transceptores, conectores, limpeza e projeto compatíveis.

Fibra não é "sempre mais rápida" em qualquer instalação. A velocidade efetiva depende do padrão, dos transceptores e dos equipamentos nas extremidades.

#### Cabo coaxial

É meio guiado com condutor central, isolante e blindagem. Teve uso marcante em Ethernet de barramento e continua presente em outras tecnologias de telecomunicações. Não deve ser confundido com par trançado.

#### Comunicação sem fio

Usa ondas eletromagnéticas no espaço.

- Facilita mobilidade e expansão.
- O meio é compartilhado e sujeito a interferência, obstáculos, potência, canais e densidade de clientes.
- Exige planejamento de cobertura, capacidade e segurança.
- Um sinal forte não garante, sozinho, alto throughput — interferência e contenção podem degradar a rede.

| Critério | Par trançado | Fibra óptica | Sem fio |
|---|---|---|---|
| Meio | cobre guiado | luz em meio guiado | ondas no espaço |
| Interferência eletromagnética | pode sofrer | imune no enlace óptico | pode sofrer interferência de rádio |
| Mobilidade | baixa | baixa | alta |
| Alcance e capacidade | dependem da categoria e padrão | elevados com projeto adequado | dependem de padrão, canal e ambiente |
| Uso comum | acesso de estações | backbone e longas distâncias | acesso de dispositivos móveis |

<a id="s2-d1-nic"></a>
### 6. Placa de rede

A placa de rede, também chamada NIC, fornece a interface de comunicação do host com o enlace. Pode ser integrada à placa-mãe, uma placa adicional, um adaptador USB ou uma interface virtual implementada por software.

Funções associadas à NIC, conforme tecnologia e implementação:

- transmissão e recepção de quadros;
- codificação e decodificação do sinal em conjunto com a camada física;
- uso de endereço MAC na rede local;
- negociação de velocidade e duplex em Ethernet;
- detecção de erros de quadro;
- descarregamento de tarefas para hardware, quando suportado.

Uma máquina pode ter várias interfaces e vários endereços. O endereço MAC pertence à interface no contexto da camada de enlace, não ao usuário nem ao computador como identidade absoluta.

<a id="s2-d1-repetidor-hub"></a>
### 7. Repetidores e hubs

#### Repetidor

O repetidor atua sobre o sinal. Ele regenera ou retransmite bits para ampliar o alcance do enlace compatível.

- Não aprende endereços MAC.
- Não escolhe rota IP.
- Não filtra broadcast.
- Não separa, por si só, domínios de broadcast.

#### Hub

O hub Ethernet clássico é um repetidor multiporta. O sinal recebido em uma porta é retransmitido às demais portas, sem consulta a endereço MAC e sem escolha seletiva de saída.

- Atua na camada física.
- Compartilha a capacidade entre os dispositivos.
- Opera no modelo legado de meio compartilhado e half-duplex.
- Forma um único domínio de colisão entre os participantes conectados.
- Não mantém tabela MAC.
- Não encaminha unicast apenas à porta correta.

Hubs são hoje equipamentos legados, mas continuam frequentes em questões porque contrastam bem com switches.

<a id="s2-d1-bridge-switch"></a>
### 8. Bridges e switches

#### Bridge

A bridge conecta segmentos de LAN na camada de enlace. Ela aprende endereços MAC de origem e associa cada endereço ao segmento ou porta de entrada.

Ao receber um quadro, pode:

- **filtrar:** não enviar o quadro a outra porta quando o destino conhecido está no mesmo segmento ou na própria porta de entrada;
- **encaminhar:** enviar ao segmento em que o destino foi aprendido;
- **inundar:** enviar por outras portas quando o destino é desconhecido, quando é broadcast ou quando o tratamento de multicast assim exigir.

A bridge separa domínios de colisão por seus segmentos, mas não interrompe broadcasts da mesma LAN por padrão.

#### Switch

O switch de camada 2 é, funcionalmente, uma bridge multiporta de alto desempenho. Ele aprende MACs de origem e consulta sua tabela de encaminhamento para decidir a porta de saída.

Comportamentos essenciais:

- unicast conhecido em outra porta — encaminha somente à porta associada ao MAC de destino;
- unicast conhecido na própria porta de entrada — filtra o quadro, pois não há motivo para devolvê-lo ao mesmo segmento;
- unicast desconhecido — inunda pelas portas pertinentes, exceto a de entrada;
- broadcast — inunda no mesmo domínio de broadcast;
- VLAN — cria separação lógica de domínios de broadcast;
- enlaces full-duplex ponto a ponto — não têm colisões Ethernet.

A frase didática "cada porta do switch é um domínio de colisão" descreve a capacidade de segmentação em comparação ao hub. Tecnicamente, em enlace full-duplex moderno não ocorrem colisões. A formulação mais precisa é: cada porta isola o segmento dos demais e, se houver operação half-duplex, cada segmento constitui domínio de colisão separado.

Switch de camada 3 pode também rotear, mas isso não torna todo switch um roteador. A função depende do equipamento e da configuração.

<a id="s2-d1-roteador-gateway-ap"></a>
### 9. Roteadores, gateways e access points

#### Roteador

O roteador encaminha pacotes IP entre redes. Ele examina o cabeçalho IP, consulta uma tabela de roteamento e seleciona o próximo salto e a interface de saída.

- Interliga sub-redes.
- Cada interface de camada 3 pertence, em regra, a uma rede ou sub-rede.
- Não encaminha broadcast local de camada 2 entre interfaces por padrão.
- Separa domínios de broadcast.
- Pode executar funções adicionais, como NAT, filtragem ou VPN, mas essas funções não definem o roteamento em si.

#### Gateway

Gateway é termo dependente de contexto:

- **gateway padrão:** próximo salto usado por um host para destinos fora da rede local, normalmente uma interface de roteador;
- **gateway de aplicação ou protocolo:** sistema que traduz ou intermedeia protocolos e formatos diferentes;
- documentos históricos da Internet também usaram "gateway" como nome de roteador.

Por isso, a afirmação "gateway atua sempre em uma camada específica" é arriscada. Primeiro identifique o contexto.

#### Access point

O access point conecta estações sem fio a uma rede de distribuição, normalmente fazendo bridging entre o meio IEEE 802.11 e a LAN Ethernet.

- Gerencia associação e acesso das estações sem fio.
- Não precisa executar roteamento, NAT ou DHCP.
- Pode ser autônomo ou controlado centralmente.
- Estende acesso lógico à LAN, mas não é sinônimo de repetidor sem fio.

Um AP em modo bridge não separa, sozinho, o domínio de broadcast. Estações associadas a um SSID mapeado para a mesma VLAN e portas cabeadas dessa VLAN normalmente pertencem ao mesmo domínio de broadcast. O AP encaminha broadcasts entre os lados sem fio e cabeado conforme a VLAN e sua configuração. Mapeamento de SSIDs para VLANs diferentes, isolamento de clientes, filtros ou túneis podem alterar esse alcance — SSID, por si só, não é prova suficiente de um novo domínio de broadcast.

O rádio Wi-Fi também é meio compartilhado. As estações disputam tempo de transmissão segundo mecanismos IEEE 802.11, associados didaticamente a CSMA/CA. Elas não usam CSMA/CD do Ethernet compartilhado e não detectam colisões da mesma forma que o Ethernet half-duplex legado. Portanto, contenção no Wi-Fi não deve ser descrita como domínio de colisão Ethernet de hub.

Um "roteador Wi-Fi" doméstico costuma combinar roteador, switch, access point, firewall, NAT e servidor DHCP em um único gabinete. A prova pode descrever o produto físico e pedir a função lógica — separe cada função.

<a id="s2-d1-dominios"></a>
### 10. Domínio de colisão e domínio de broadcast

**Domínio de colisão** é o conjunto de interfaces que compartilham um meio half-duplex no qual transmissões simultâneas podem colidir.

**Domínio de broadcast** é o conjunto de interfaces que recebe uma transmissão de broadcast da camada de enlace dentro da mesma LAN ou VLAN.

Regras práticas:

- repetidores e hubs não dividem domínio de colisão nem domínio de broadcast;
- bridges e switches dividem segmentos de colisão, mas mantêm o mesmo domínio de broadcast enquanto tudo permanece na mesma VLAN;
- um access point em bridge normalmente estende a VLAN e seu domínio de broadcast ao meio sem fio, salvo segmentação ou filtragem configurada;
- cada VLAN representa um domínio de broadcast distinto;
- roteadores separam domínios de broadcast entre interfaces;
- enlaces Ethernet full-duplex modernos são livres de colisão, embora a segmentação por porta continue sendo cobrada;
- broadcast de camada 2 e broadcast IPv4 não são a mesma unidade, embora um broadcast IPv4 local seja transportado por quadro de broadcast no enlace Ethernet;
- IPv6 não utiliza endereço de broadcast — esse ponto será aprofundado no Dia 2.

#### Exemplo de contagem

Considere 6 computadores ligados diretamente a um switch, todos na VLAN 10, e o switch ligado a uma interface de roteador.

- Domínios de broadcast: 1 para a VLAN 10.
- Segmentos isolados pelo switch: 7 enlaces — 6 acessos e 1 enlace com o roteador.
- Em full-duplex, não há colisões nesses enlaces.
- Em linguagem didática tradicional, seriam 7 domínios de colisão separados.

Se metade dos computadores for colocada na VLAN 20, passam a existir 2 domínios de broadcast. Para que VLAN 10 e VLAN 20 se comuniquem, é preciso roteamento entre elas.

<a id="s2-d1-exemplos"></a>
## Exemplos práticos e resolvidos

### Exemplo 1 — Estrela física com comportamentos diferentes

Quatro computadores estão ligados a um equipamento central.

- Se o centro é um hub, a topologia é estrela física, mas o meio lógico é compartilhado. Uma transmissão recebida é repetida às demais portas e todos disputam o mesmo domínio de colisão.
- Se o centro é um switch, cada acesso é um enlace segmentado. O switch aprende MACs, envia unicast conhecido à porta de destino quando ela difere da entrada e filtra quando o destino está aprendido na própria porta de entrada.

Conclusão: olhar apenas o desenho físico não basta.

### Exemplo 2 — Escolha do meio

Um órgão precisa interligar dois prédios, com forte interferência eletromagnética no trajeto e necessidade de alta capacidade.

Raciocínio:

1. Par trançado de cobre pode sofrer interferência e possui limites de alcance conforme padrão.
2. Comunicação sem fio depende de visada, espectro, obstáculos e segurança.
3. Fibra não conduz interferência eletromagnética e atende bem a backbone, desde que ópticas e distância sejam compatíveis.

Escolha tecnicamente coerente: fibra óptica com projeto adequado. Isso não significa que toda fibra ou todo transceptor serve para qualquer distância.

### Exemplo 3 — Switch não encontrou o MAC

O switch recebe quadro unicast cujo MAC de destino ainda não existe em sua tabela.

1. Aprende o MAC de origem na porta de entrada.
2. Trata o destino como unicast desconhecido.
3. Inunda o quadro pelas portas pertinentes da mesma VLAN, exceto a porta de entrada.
4. Quando a resposta chega, aprende o segundo MAC.

Pegadinha: inundação de unicast desconhecido não transforma o quadro em broadcast. O endereço de destino continua unicast.

Se, em outro quadro, o MAC de destino já estiver aprendido na mesma porta pela qual o quadro entrou, o switch filtra esse quadro em vez de encaminhá-lo de volta à própria porta. Isso ocorre, por exemplo, quando dois hosts estão atrás do mesmo segmento conectado a uma porta do switch.

### Exemplo 4 — Destino em outra rede

Uma estação precisa enviar dados a um servidor fora de sua sub-rede.

1. A estação identifica que o destino não é local.
2. Envia o quadro ao MAC do gateway padrão.
3. O pacote IP mantém como destino o servidor remoto.
4. O roteador remove o cabeçalho de enlace recebido, consulta a rota e cria novo quadro para o próximo enlace.

Conclusão: switch decide com MAC dentro da LAN; roteador decide o próximo salto com endereço IP e tabela de rotas.

### Exemplo 5 — Equipamento doméstico multifuncional

Um aparelho possui uma porta WAN, quatro portas LAN e Wi-Fi.

- A porta WAN e a LAN são interligadas pela função de roteamento.
- As quatro portas LAN são fornecidas pela função de switch.
- O Wi-Fi é fornecido pela função de access point.
- NAT, DHCP e firewall podem estar presentes como serviços adicionais.

O gabinete é um só, mas as funções de rede são várias.

### Exemplo 6 — Malha completa

Uma rede de 6 roteadores exige enlace direto entre todos os pares.

`6 x (6 - 1) / 2 = 6 x 5 / 2 = 15`.

São necessários 15 enlaces. Se existirem apenas conexões redundantes entre alguns pares, a malha é parcial.

<a id="s2-d1-diferencas"></a>
## Diferenças entre conceitos parecidos

| Conceitos | Diferença central |
|---|---|
| Topologia física x lógica | disposição de cabos e rádios x caminho e regra de circulação dos dados |
| Largura de banda x throughput | capacidade nominal x taxa efetivamente entregue |
| Latência x jitter | atraso x variação do atraso |
| LAN x WLAN | LAN é rede local; WLAN é uma LAN com acesso sem fio |
| Repetidor x bridge | repetidor regenera sinais; bridge examina MAC e filtra quadros |
| Hub x switch | hub retransmite bits às demais portas; switch aprende MAC e encaminha ou filtra quadros |
| Bridge x switch | ambos fazem bridging; switch é tipicamente uma bridge multiporta otimizada |
| Switch x roteador | switch de camada 2 encaminha por MAC dentro da LAN; roteador encaminha por IP entre redes |
| Roteador x gateway | roteador é função de encaminhamento IP; gateway pode ser próximo salto ou tradutor de protocolo |
| Access point x roteador sem fio | AP fornece acesso à WLAN; roteador sem fio combina AP com roteamento e outros serviços |
| Repetidor sem fio x access point | repetidor retransmite cobertura existente; AP conecta estações a uma rede de distribuição |
| Domínio de colisão x broadcast | colisão envolve meio half-duplex compartilhado; broadcast envolve alcance de uma transmissão para toda a LAN ou VLAN |

<a id="s2-d1-revisao-fixa"></a>
## Revisão fixa do Dia 1

**Distribuição das extras:** 15 questões de Legislação CRA/CFA e 5 questões de Português.

| Núcleo | Origem do conteúdo | Tratamento nesta semana |
|---|---|---|
| Lei nº 4.769/1965 e Decreto nº 61.934/1967 | revisão da Semana 1 | recuperação ativa da função de cada norma |
| CFA x CRA-PR e estrutura regimental | revisão com aprofundamento | aplicação a competências, Plenário, Ouvidoria, sede e jurisdição |
| Código de Ética — RN CFA nº 671/2025 | revisão com aprofundamento | sujeitos, deveres, condutas, sanções, multa e pessoa jurídica |
| Comando, inferência e conectores | revisão da Semana 1 | aplicação aos enunciados técnicos de redes |
| Palavras absolutas e interpretação técnica | aprofundamento da Semana 2 | controle de generalizações em alternativas de prova |

O conhecimento anterior necessário está na Semana 1, especialmente nos Dias 4 e 5. Aqui ele é retomado de modo ativo, com os detalhes adicionais efetivamente usados nas 20 questões extras do Dia 1.

<a id="s2-d1-revisao-legislacao"></a>
### Legislação CRA/CFA — 15 questões extras

Esta revisão sustenta as 20 questões extras do Dia 1. O foco é reconhecer a norma, o sujeito e a competência, sem atribuir ao CRA uma função nacional nem ao CFA uma função meramente regional.

<a id="s2-d1-revisao-base-legal"></a>
#### Base legal e relação entre as normas

- **Lei nº 4.769/1965:** regula o exercício profissional e estabelece o Sistema CFA/CRAs.
- **Decreto nº 61.934/1967:** regulamenta a Lei nº 4.769/1965.
- **RN CFA nº 649/2024:** aprova o Regulamento de Registro do Sistema CFA/CRAs.
- **RN CFA nº 670/2025:** altera pontos da RN CFA nº 649/2024 — deve ser lida em conjunto com ela.
- **RN CFA nº 651/2024:** aprova o Regimento do CRA-PR.
- **RN CFA nº 671/2025:** aprova o Código de Ética e Disciplina e revoga expressamente a RN CFA nº 640/2024.

Lei e decreto não são substituídos por uma resolução normativa. As resoluções detalham matérias dentro da competência normativa do CFA e devem respeitar as normas superiores.

**Delimitação para Analista de Sistemas:** o conteúdo específico do cargo no edital consolidado abrange Lei nº 4.769/1965, Decreto nº 61.934/1967, Regimento Interno do CRA-PR e RN CFA nº 671/2025. As RNs nº 649/2024 e nº 670/2025 aparecem aqui somente como contexto para compreender a atividade registral do Sistema CFA/CRAs; não serão cobradas autonomamente nas questões extras desta semana.

<a id="s2-d1-revisao-cfa-cra"></a>
#### CFA x CRA-PR

| Entidade | Âmbito | Função central | Pegadinha |
|---|---|---|---|
| CFA | nacional | orientar, disciplinar e formular diretrizes e normas do sistema | tratá-lo como conselho regional do Distrito Federal |
| CRA-PR | estado do Paraná | executar diretrizes, registrar, fiscalizar e julgar infrações em sua jurisdição | atribuir-lhe jurisdição nacional |

O Regimento aprovado pela RN CFA nº 651/2024 afirma que o CRA-PR:

- é autarquia com personalidade jurídica de direito público;
- possui autonomia técnica, administrativa e financeira;
- tem sede na capital do Paraná;
- tem jurisdição em todo o estado do Paraná;
- executa diretrizes e normas do CFA;
- fiscaliza atividades abrangidas pela legislação profissional;
- organiza e mantém registros de pessoas físicas e jurídicas sujeitas à inscrição;
- julga infrações e impõe penalidades nos limites legais.

Seus órgãos regimentais incluem Plenário, Diretoria Executiva, Ouvidoria, Comissões Permanentes, Especiais e Grupos de Trabalho e Órgãos de Representação. O Plenário é órgão colegiado de deliberação superior e primeira instância de julgamento no âmbito de sua jurisdição. A Ouvidoria tem natureza mediadora e não possui caráter administrativo, executivo, deliberativo ou decisório.

<a id="s2-d1-revisao-registro"></a>
#### Registro e fiscalização

Registro e fiscalização são atividades centrais dos CRAs. Em contexto complementar, o regulamento aprovado pela RN CFA nº 649/2024, alterado pela RN nº 670/2025, diferencia situações registrais. Esses detalhes ajudam a entender a atuação do conselho, mas não integram autonomamente o programa específico de Analista de Sistemas.

Ideias para fixação:

- registro no CRA constitui habilitação profissional dentro das atribuições concedidas;
- atuação em jurisdição diversa pode envolver providência registral conforme o regulamento aplicável;
- situações de licença, cancelamento e transferência têm efeitos distintos e não devem ser tratadas como sinônimos;
- pessoa jurídica pode estar sujeita a registro e responsabilidade técnica conforme sua atividade básica ou a natureza dos serviços prestados;
- diploma e registro profissional cumprem funções diferentes — não suponha que um substitui automaticamente o outro.

Se uma fonte complementar citar requisito específico de registro, ela deve considerar a alteração promovida pela RN CFA nº 670/2025 e não apenas a versão original da RN nº 649/2024. Nesta apostila, esse ponto serve para estudo contextual e controle de fonte, não para ampliar o edital do cargo.

<a id="s2-d1-revisao-etica"></a>
#### Código de Ética vigente

A RN CFA nº 671/2025 alcança profissionais de Administração e pessoas jurídicas registradas, observadas as especificidades das pessoas jurídicas.

Deveres centrais:

- atuar com zelo, dedicação, comprometimento, responsabilidade e honestidade;
- defender direitos e interesses de quem recebe os serviços;
- guardar sigilo sobre informação conhecida em razão do exercício profissional lícito;
- manter independência técnica;
- buscar aperfeiçoamento;
- zelar pela reputação pessoal, profissional e institucional;
- colaborar com o Sistema CFA/CRAs e tratar seus representantes com urbanidade.

Condutas de risco ético:

- assinar documento elaborado por terceiro sem orientação ou supervisão efetiva;
- emprestar nome ou registro para facilitar exercício irregular;
- violar sigilo sem justa causa;
- dificultar fiscalização;
- praticar assédio no exercício da atividade;
- usar artifício enganoso para obter vantagem indevida.

Sanções previstas no Código:

- advertência escrita e reservada;
- censura pública;
- suspensão do exercício profissional;
- cancelamento do registro profissional.

As sanções de suspensão e cancelamento não se aplicam à pessoa jurídica. Não conclua, porém, que pessoa jurídica está fora do Código — ela pode sofrer as sanções compatíveis com sua natureza.

O art. 13 da RN CFA nº 671/2025 estabelece que as sanções são acompanhadas de multa pecuniária conforme as regras do art. 18. Para pessoa jurídica, suspensão e cancelamento continuam inaplicáveis; advertência e censura podem ser aplicadas com a faixa de multa específica prevista no art. 18, § 2º. A banca pode tornar a alternativa errada ao afirmar que a pessoa jurídica não recebe sanção alguma ou, no extremo oposto, que recebe suspensão do exercício profissional.

<a id="s2-d1-revisao-exemplo-legal"></a>
#### Mini aplicação legislativa

Uma empresa de consultoria atua no campo da Administração no Paraná e dificulta a entrega de documentos ao fiscal.

Raciocínio:

1. A natureza da atividade pode atrair registro e fiscalização.
2. O CRA-PR atua em sua jurisdição regional.
3. Dificultar fiscalização pode ter repercussão ética e administrativa.
4. O enquadramento e a sanção dependem do processo e da norma aplicável — não se escolhe penalidade por intuição.

<a id="s2-d1-revisao-portugues"></a>
### Português e interpretação — 5 questões extras

<a id="s2-d1-revisao-comando"></a>
#### Comando da questão

Antes de ler alternativas, marque o núcleo do comando:

- correta;
- incorreta;
- exceto;
- de acordo com o texto;
- infere-se;
- não se pode concluir.

Em comandos negativos, escreva mentalmente: "procuro a exceção". Muitos erros ocorrem porque o candidato sabe o conteúdo, mas responde ao comando oposto.

<a id="s2-d1-revisao-inferencia"></a>
#### Inferência x extrapolação

- **Inferência:** conclusão autorizada pelas informações do texto.
- **Extrapolação:** acrescenta generalização, causa, consequência ou certeza que o texto não sustentou.

Trecho: "A fibra reduz a exposição à interferência eletromagnética no enlace óptico, mas sua implantação exige componentes compatíveis."

Inferência válida: a escolha da fibra não elimina a necessidade de projeto. Extrapolação: toda rede de fibra é mais barata e mais rápida que qualquer rede de cobre.

<a id="s2-d1-revisao-conectores"></a>
#### Conectores

| Relação | Conectores comuns | Efeito |
|---|---|---|
| oposição | mas, porém, contudo | quebra expectativa |
| concessão | embora, ainda que | admite obstáculo sem impedir a ideia principal |
| conclusão | portanto, logo, assim | apresenta resultado lógico |
| causa | porque, visto que | apresenta motivo |
| condição | se, caso, desde que | estabelece requisito |

<a id="s2-d1-revisao-absolutas"></a>
#### Palavras absolutas

`Sempre`, `nunca`, `somente`, `todos` e `necessariamente` ampliam o alcance de uma afirmação. Não são automaticamente erradas, mas exigem apoio integral do texto ou da regra técnica.

<a id="s2-d1-revisao-pratica-interpretacao"></a>
#### Prática breve de interpretação

Trecho: "O switch reduz a propagação de colisões entre seus segmentos; contudo, não separa broadcasts entre portas pertencentes à mesma VLAN."

- Ideia principal: segmentação de colisões e domínio de broadcast são efeitos diferentes.
- `Contudo` introduz ressalva ou oposição.
- Não se pode concluir que o switch bloqueia todo broadcast.
- Trocar `mesma VLAN` por `qualquer VLAN` altera o sentido técnico.

<a id="s2-d1-revisao-tabela"></a>
### Diferenças, pegadinhas e tabela rápida da revisão fixa

| Conceito | Regra curta | Diferença ou pegadinha | Exemplo |
|---|---|---|---|
| Lei x decreto | a lei disciplina; o decreto regulamenta | decreto não revoga nem substitui a lei | Lei nº 4.769/1965 x Decreto nº 61.934/1967 |
| CFA x CRA-PR | orientação nacional x execução regional | autonomia regional não cria jurisdição nacional | CFA uniformiza; CRA-PR fiscaliza no Paraná |
| Plenário x Ouvidoria | deliberação/julgamento x mediação | Ouvidoria não decide nem substitui o Plenário | reclamação mediada x decisão colegiada |
| pessoa física x pessoa jurídica | ambas podem estar no alcance do Código | suspensão e cancelamento não se aplicam à pessoa jurídica | advertência/censura compatíveis com PJ |
| sanção x multa | consequência disciplinar x efeito pecuniário associado | multa não substitui automaticamente o processo ou a sanção | arts. 13 e 18 da RN nº 671/2025 |
| inferência x extrapolação | conclusão sustentada x acréscimo não autorizado | vantagem técnica não vira superioridade absoluta | fibra exige projeto compatível |
| oposição x conclusão | ressalva x resultado lógico | `contudo` não equivale a `portanto` | enlace ativo; contudo, serviço indisponível |
| palavra absoluta x falsidade | alcance máximo x valor lógico | `sempre` exige prova total, mas não é automaticamente falso | “switch sempre bloqueia broadcast” |

Pegadinhas prioritárias: inverter CFA e CRA-PR; transformar a Ouvidoria em órgão decisório; excluir a pessoa jurídica do Código; escolher sanção por intuição; ignorar comando negativo; e trocar possibilidade ou ressalva por certeza universal.

<a id="s2-d1-tabela-rapida"></a>
## Tabela de revisão rápida do Dia 1

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| Rede | nós interligados por meios e protocolos | confundir com Internet | LAN interna do conselho |
| Protocolo | regras de comunicação | confundir com equipamento | Ethernet e IP |
| Topologia física | disposição dos enlaces | deduzir o fluxo apenas pelo desenho | estrela com equipamento central |
| Topologia lógica | forma de circulação e acesso | tratá-la como cabeamento | meio compartilhado em hub |
| PAN | rede de entorno pessoal | chamar toda rede sem fio de PAN | relógio e celular |
| LAN | rede local administrada | achar que precisa ser cabeada | WLAN do escritório |
| MAN | rede metropolitana | definir por número rígido de quilômetros | unidades na mesma cidade |
| WAN | interliga redes a longa distância | confundir com Internet | matriz e filial em estados distintos |
| Par trançado | cobre com pares trançados | dizer que é imune a interferência | acesso Ethernet de estação |
| Fibra | transmissão óptica guiada | garantir qualquer velocidade sem olhar ópticas | backbone entre prédios |
| Sem fio | transmissão não guiada | sinal forte garantir vazão | WLAN corporativa |
| NIC | interface do host com o enlace | tratar MAC como identidade do usuário | adaptador Ethernet |
| Repetidor | regenera sinal | atribuir filtragem MAC | extensão de enlace compatível |
| Hub | repetidor multiporta | dizer que aprende endereços | meio Ethernet legado compartilhado |
| Bridge | interliga segmentos por MAC | dizer que roteia IP | ponte entre duas LANs |
| Switch | bridge multiporta que aprende MACs | esquecer filtragem quando o destino conhecido está na porta de entrada | acesso de estações |
| Roteador | encaminha IP entre redes | dizer que encaminha todo broadcast local | ligação LAN-WAN |
| Gateway | próximo salto ou tradutor | impor uma única camada em todo contexto | gateway padrão da estação |
| Access point | integra estações sem fio à LAN | confundir com roteador completo | AP corporativo |
| Domínio de colisão | meio half-duplex sujeito a colisões | ignorar full-duplex | dispositivos em hub |
| Domínio de broadcast | alcance de broadcast na LAN/VLAN | confundir com colisão | uma VLAN |
| VLAN | segmentação lógica de LAN | achar que é apenas grupo de portas sem efeito | VLAN 10 e VLAN 20 |

<a id="s2-d1-pegadinhas"></a>
## Pegadinhas do Dia 1

- Estrela física com hub não tem o mesmo comportamento lógico de estrela com switch.
- Hub não aprende MAC e não escolhe porta de destino.
- Switch filtra quadro destinado a MAC conhecido na própria porta de entrada; não o devolve ao mesmo segmento.
- Switch de camada 2 não separa broadcast entre portas da mesma VLAN.
- Cada VLAN é um domínio de broadcast separado.
- Em full-duplex Ethernet não há colisões — a frase "uma colisão por porta" deve ser entendida como segmentação do domínio no modelo tradicional.
- Bridge e switch trabalham com quadros e endereços MAC, não com a escolha de rotas IP, salvo equipamento multicamada exercendo função adicional.
- Roteador separa redes e domínios de broadcast, mas um produto comercial pode acumular switch, AP, NAT e DHCP.
- Access point não é necessariamente roteador, servidor DHCP ou repetidor.
- AP em bridge pode estender o mesmo domínio de broadcast da VLAN entre rede cabeada e WLAN; Wi-Fi disputa o meio, mas não usa CSMA/CD Ethernet.
- Gateway é termo contextual e não pertence obrigatoriamente a uma única camada.
- Wi-Fi pode funcionar sem Internet.
- Fibra é imune a interferência eletromagnética no enlace, mas não dispensa transceptores e projeto compatíveis.
- Largura de banda nominal não é throughput nem goodput.
- MAC identifica uma interface no enlace e pode ser localmente administrado ou alterado — não é identidade imutável da pessoa.
- RN CFA nº 651/2024 aprova o Regimento do CRA-PR; RN CFA nº 671/2025 aprova o Código de Ética.
- A RN CFA nº 671/2025 revogou a RN CFA nº 640/2024.
- CRA-PR tem jurisdição no Paraná; CFA exerce papel nacional e normativo.
- No Português, `contudo` indica oposição, não conclusão.

<a id="s2-d1-pratica"></a>
## Prática guiada

### Roteiro 1 — Mapear uma LAN de órgão público

Desenhe uma rede com:

- 12 estações;
- 2 impressoras;
- 2 access points;
- 1 servidor;
- 1 switch de acesso;
- 1 roteador para a WAN.

Depois, execute:

1. Marque os hosts e os equipamentos intermediários.
2. Identifique a estrela física formada no switch.
3. Marque quais enlaces podem operar em full-duplex.
4. Considere todos na mesma VLAN e anote 1 domínio de broadcast.
5. Divida usuários e servidores em duas VLANs e anote 2 domínios de broadcast.
6. Indique onde o roteamento entre VLANs deve ocorrer.

### Roteiro 2 — Acompanhar um quadro

Cenário: estação A envia dados à estação B na mesma VLAN.

1. A NIC de A prepara o quadro com MAC de origem A e MAC de destino B.
2. O switch aprende o MAC A na porta de entrada.
3. Se B já estiver na tabela em porta diferente da entrada, encaminha apenas à porta de B; se o destino estiver aprendido na própria porta de entrada, filtra.
4. Se B não estiver na tabela, inunda o unicast desconhecido dentro da VLAN.
5. A resposta permite aprender o MAC B.

Acrescente um hub ou outro segmento com dois hosts atrás da mesma porta. Se o switch receber por essa porta um quadro cujo MAC de destino também está aprendido nela, marque a ação **filtrar** — o quadro não deve ser devolvido à própria porta.

Repita o roteiro colocando B em outra sub-rede. Agora A entrega o quadro ao MAC do gateway, e o roteador encaminha o pacote IP.

### Roteiro 3 — Selecionar meio sem usar regra absoluta

Preencha uma matriz com necessidade de alcance, interferência, mobilidade, capacidade, segurança física e custo. Compare:

- mesa de usuário a 30 metros — par trançado é candidato natural;
- backbone entre prédios — fibra é candidata forte;
- tablets em sala de reunião — comunicação sem fio atende mobilidade;
- ambiente com interferência — fibra reduz esse risco no enlace.

Registre a justificativa, não apenas o nome do meio.

### Roteiro 4 — Recuperação ativa da revisão fixa

Sem consultar a teoria, escreva em até 10 minutos:

- três diferenças entre CFA e CRA-PR;
- a função das RN CFA nº 649, 651, 670 e 671;
- quatro deveres éticos;
- a diferença entre inferência e extrapolação;
- três conectores e suas relações de sentido.

Confira e corrija com outra cor.

<a id="s2-d1-checklist"></a>
## Checklist de domínio

- [ ] Explico rede, host, nó, interface, enlace, protocolo e serviço.
- [ ] Diferencio largura de banda, throughput, goodput, latência e jitter.
- [ ] Diferencio simplex, half-duplex e full-duplex.
- [ ] Diferencio topologia física e lógica.
- [ ] Reconheço barramento, estrela, anel, malha e híbrida.
- [ ] Calculo enlaces de uma malha completa.
- [ ] Diferencio PAN, LAN, MAN e WAN.
- [ ] Comparo par trançado, fibra e comunicação sem fio.
- [ ] Sei o papel da placa de rede.
- [ ] Diferencio repetidor e hub.
- [ ] Explico aprendizagem, encaminhamento, inundação e filtragem de uma bridge ou switch.
- [ ] Sei que destino conhecido na própria porta de entrada é filtrado.
- [ ] Diferencio switch e roteador.
- [ ] Diferencio gateway padrão e gateway de aplicação.
- [ ] Sei por que access point não é sinônimo de roteador sem fio.
- [ ] Explico como AP, VLAN e configuração definem o alcance de broadcast na WLAN.
- [ ] Diferencio contenção Wi-Fi de colisão Ethernet e não atribuo CSMA/CD ao IEEE 802.11.
- [ ] Conto domínios de broadcast por VLAN.
- [ ] Explico a ressalva de colisões em enlaces full-duplex.
- [ ] Diferencio CFA e CRA-PR.
- [ ] Associo corretamente RN CFA nº 651/2024 e RN CFA nº 671/2025.
- [ ] Reconheço deveres e condutas de risco ético.
- [ ] Sei que as sanções da RN CFA nº 671/2025 são acompanhadas por multa e reconheço a regra própria da pessoa jurídica.
- [ ] Identifico comando negativo, inferência, extrapolação e conectores.

<a id="s2-d1-caderno-erros"></a>
## Orientações para o caderno de erros

Crie a página **Dia 1 — Redes físicas, equipamentos e domínios** com cinco quadros:

1. **Termos confundidos:** anote pares como hub/switch, bridge/roteador e AP/roteador sem fio.
2. **Domínios:** desenhe a topologia errada e, ao lado, marque colisão e broadcast corretamente.
3. **Regra com ressalva:** registre por que full-duplex não tem colisões e por que gateway depende do contexto.
4. **Legislação:** escreva a norma que você trocou e a função correta.
5. **Português:** copie o comando que você leu de forma invertida e circule a palavra decisiva.

Para cada erro, use este formato:

- afirmação que pareceu correta;
- palavra que tornou a afirmação errada;
- explicação correta em até três linhas;
- exemplo próprio;
- data da revisão no início da Semana 3.

<a id="s2-d1-fontes"></a>
## Fontes utilizadas no Dia 1

Fontes técnicas e institucionais primárias ou oficiais consultadas:

- IEEE 802 LAN/MAN Standards Committee — https://www.ieee802.org/
- IEEE 802.3 Ethernet Working Group — https://www.ieee802.org/3/
- IEEE/ISO/IEC 8802-1Q-2024 — Bridges and Bridged Networks — https://standards.ieee.org/ieee/8802-1Q/11825/
- IEEE 802.11 Wireless LAN Working Group — https://www.ieee802.org/11/
- IEEE 802.15.4-2024 — IEEE Standard for Low-Rate Wireless Networks — https://standards.ieee.org/ieee/802.15.4/11041/
- IEEE Registration Authority — endereços MAC — https://standards.ieee.org/products-programs/regauth/mac/
- RFC 1812 — Requirements for IP Version 4 Routers — https://www.rfc-editor.org/rfc/rfc1812.html
- Cisco — fundamentos de switches, roteadores e access points — https://www.cisco.com/c/pt_br/solutions/small-business/resource-center/networking/networking-basics.html
- Cisco — funcionamento Ethernet, repetidores e full-duplex — https://www.cisco.com/en/US/docs/internetworking/troubleshooting/guide/tr1904.html
- Lei Federal nº 4.769/1965 — https://www.planalto.gov.br/ccivil_03/leis/l4769.htm
- Decreto Federal nº 61.934/1967 — https://www.planalto.gov.br/ccivil_03/decreto/Antigos/D61934.htm
- Lei Federal nº 6.839/1980 — registro de empresas conforme atividade básica ou serviço prestado — https://www.planalto.gov.br/ccivil_03/Leis/L6839.htm
- RN CFA nº 649/2024 — https://documentos.cfa.org.br/?a=show&c=documento&id=951
- RN CFA nº 670/2025 — https://documentos.cfa.org.br/?a=show&c=documento&id=1033
- RN CFA nº 651/2024 — https://documentos.cfa.org.br/?a=show&c=documento&id=955
- RN CFA nº 671/2025 — https://documentos.cfa.org.br/?a=show&c=documento&id=1038
- Manual de Redação da Presidência da República — https://www.gov.br/pt-br/servicos/consultar-o-manual-de-redacao-da-presidencia-da-republica

---

# Dia 2 - Modelos OSI e TCP/IP, endereçamento e CIDR

<a id="s2-d2-objetivo"></a>
## Objetivo do dia

Compreender como os modelos em camadas organizam a comunicação e aplicar endereçamento IPv4 e IPv6 com segurança. Ao final, o estudante deve conseguir acompanhar o encapsulamento de uma mensagem, relacionar PDUs e endereços às camadas corretas e calcular rede, broadcast, faixa de hosts, máscara e prefixo CIDR sem depender de tentativa.

<a id="s2-d2-resultados"></a>
## Resultados esperados

Ao final do dia, você deve conseguir:

- nomear e explicar as sete camadas do modelo OSI;
- descrever as quatro camadas usuais do modelo TCP/IP e compará-las ao OSI;
- acompanhar encapsulamento e desencapsulamento de ponta a ponta;
- associar dados, segmento ou datagrama, pacote, quadro e bits às camadas pertinentes;
- diferenciar endereço MAC, endereço IP e porta de transporte;
- interpretar endereços IPv4 e IPv6;
- converter máscara decimal contígua em prefixo CIDR e fazer o caminho inverso;
- calcular endereço de rede, broadcast e hosts válidos em IPv4;
- calcular quantidade convencional de hosts e tratar corretamente as exceções `/31` e `/32`;
- dividir uma rede em sub-redes e identificar o bloco que contém um endereço;
- reconhecer faixas IPv4 privadas, loopback e link-local/APIPA;
- explicar gateway padrão, ARP, ICMP e ICMPv6;
- lembrar que IPv6 não possui endereço de broadcast;
- revisar Administração Pública e Português em nível suficiente para as questões extras do dia.

<a id="s2-d2-importancia"></a>
## Por que esse assunto importa para a prova

Modelos em camadas fornecem o vocabulário usado em redes. Sem eles, expressões como quadro, pacote, MAC, gateway, ARP e ICMP parecem uma lista desconexa. Com o modelo, cada conceito ganha função e escopo.

Endereçamento e CIDR combinam teoria e cálculo, formato muito produtivo para bancas. Um único cenário permite cobrar máscara, operação binária, rede, broadcast, hosts, gateway e comunicação local ou remota.

No trabalho do Analista de Sistemas, esses conhecimentos sustentam configuração de servidores, VLANs, firewalls, rotas, monitoramento e diagnóstico. Um erro de prefixo pode colocar o gateway fora da rede lógica, gerar sobreposição de sub-redes ou tornar hosts aparentemente próximos incapazes de se comunicar.

<a id="s2-d2-estilo-consulplan"></a>
## Como pode ser cobrado no estilo Instituto Consulplan

Formatos prováveis:

- associação entre camada, protocolo, equipamento e PDU;
- comparação entre OSI e TCP/IP;
- ordem correta do encapsulamento;
- cenário em que o MAC muda a cada enlace e o IP identifica a comunicação de ponta a ponta;
- cálculo de rede e broadcast a partir de IPv4 e prefixo;
- conversão entre máscara decimal e CIDR;
- identificação de endereço privado, loopback ou link-local;
- alternativa que aplica a fórmula `2^h - 2` indevidamente a `/31`;
- alternativa que inventa broadcast em IPv6;
- cenário em que ARP resolve o MAC do gateway, não o MAC do servidor remoto;
- afirmação que trata ICMP como protocolo de transporte ou associa uma porta TCP/UDP a ele.

Na resolução, separe três planos:

1. **Camada:** qual função está sendo executada.
2. **Escopo:** enlace local, caminho entre redes ou comunicação da aplicação.
3. **Cálculo:** quantos bits são de rede e quantos são de host.

<a id="s2-d2-cronograma"></a>
## Cronograma de 6h líquidas com pausas sugeridas

| Bloco | Tempo líquido | Atividade |
|---|---:|---|
| 1 | 2h | OSI, TCP/IP, encapsulamento, PDUs e endereços MAC |
| 2 | 1h30 | IPv4, IPv6, máscaras, CIDR, rede, broadcast, hosts e sub-redes |
| 3 | 1h | Exemplos resolvidos, gateway padrão, ARP, ICMP e comparação dos modelos |
| 4 | 40min | Revisão fixa de Administração Pública |
| 5 | 30min | Português e interpretação de enunciados técnicos |
| 6 | 20min | Caderno de erros e revisão ativa dos cálculos |
| **Total** | **6h** | **360 minutos líquidos** |

Pausas sugeridas, fora das 6h líquidas: 10min após o Bloco 1, 15min após o Bloco 2, 10min após o Bloco 3 e 5min antes do caderno de erros.

<a id="s2-d2-teoria"></a>
## Teoria explicada de forma didática

<a id="s2-d2-osi"></a>
### 1. Modelo OSI e suas sete camadas

O modelo de referência OSI organiza funções de comunicação em sete camadas. A ISO esclarece que o modelo oferece uma base comum para coordenar padrões e colocar tecnologias em perspectiva — ele não é, por si só, uma implementação completa.

Da camada superior para a inferior:

| Nº | Camada | Responsabilidade didática | Exemplos de conceitos |
|---:|---|---|---|
| 7 | Aplicação | serviços de rede usados pelas aplicações | HTTP, DNS, SMTP |
| 6 | Apresentação | representação, codificação, compressão e proteção dos dados | formatos, codificação, criptografia em sentido funcional |
| 5 | Sessão | estabelecimento, manutenção e sincronização de diálogos | controle de sessão e pontos de sincronização |
| 4 | Transporte | comunicação fim a fim entre processos | TCP, UDP, portas, segmentação |
| 3 | Rede | endereçamento lógico e encaminhamento entre redes | IPv4, IPv6, ICMP, roteadores |
| 2 | Enlace de dados | quadros e entrega no enlace local | Ethernet, Wi-Fi, MAC, switches |
| 1 | Física | transmissão de bits como sinais | cabos, fibras, rádio, conectores e repetidores |

#### Camada 7 — Aplicação

É a camada mais próxima dos processos de usuário. Oferece protocolos para funções como navegação, resolução de nomes, transferência de arquivos e e-mail.

Pegadinha: camada de aplicação não é o programa inteiro. O navegador é aplicação; HTTP é um protocolo de aplicação usado por ele.

#### Camada 6 — Apresentação

Trata como a informação é representada para que sistemas diferentes consigam interpretá-la. Inclui, no modelo didático, tradução de formatos, codificação, serialização, compressão e criptografia.

Pegadinha: nem toda implementação real possui um módulo separado chamado "camada de apresentação". A função pode estar na biblioteca ou na aplicação.

#### Camada 5 — Sessão

Organiza diálogos entre aplicações, incluindo estabelecimento, manutenção, encerramento e sincronização. Em pilhas reais, várias funções de sessão aparecem incorporadas a protocolos de aplicação ou bibliotecas.

#### Camada 4 — Transporte

Fornece comunicação entre processos finais. Pode incluir portas, multiplexação, segmentação, controle de fluxo, confirmação e retransmissão, conforme o protocolo.

- TCP oferece serviço orientado à conexão e confiável.
- UDP oferece serviço de datagramas sem conexão e sem garantia de entrega.

Não atribua ao IP a confiabilidade oferecida pelo TCP. O IP fornece serviço de datagramas sem garantia de entrega fim a fim.

#### Camada 3 — Rede

Cuida de endereçamento lógico e encaminhamento entre redes. Roteadores analisam o cabeçalho IP e escolhem o próximo salto.

O endereço IP identifica uma interface no contexto da rede lógica. A rota pode atravessar vários enlaces de camada 2.

#### Camada 2 — Enlace de dados

Organiza a transmissão em quadros dentro de um enlace ou domínio de camada 2. Usa endereços MAC em tecnologias IEEE 802 e inclui detecção de erros no quadro.

Switches de camada 2 aprendem endereços de origem e encaminham quadros. A entrega de enlace alcança o próximo nó no caminho, não necessariamente o destino IP final.

#### Camada 1 — Física

Representa bits por sinais elétricos, ópticos ou de rádio. Define aspectos como codificação do sinal, conectores, frequências e características do meio.

Repetidores e hubs clássicos atuam aqui. A camada física não interpreta endereço MAC nem endereço IP.

<a id="s2-d2-tcpip"></a>
### 2. Modelo TCP/IP

A arquitetura da Internet é normalmente apresentada em quatro camadas:

1. **Aplicação**
2. **Transporte**
3. **Internet**
4. **Enlace**

A RFC 1122 descreve enlace, IP e transporte; a RFC 1123 trata de protocolos de aplicação e suporte. Alguns livros usam um modelo didático de cinco camadas, separando física e enlace. Essa variação não altera a suíte de protocolos — muda apenas a forma pedagógica de agrupar funções.

| Modelo OSI | Modelo TCP/IP de quatro camadas | Exemplo |
|---|---|---|
| Aplicação, Apresentação e Sessão | Aplicação | HTTP, DNS, formatos e sessões da aplicação |
| Transporte | Transporte | TCP e UDP |
| Rede | Internet | IPv4, IPv6 e ICMP |
| Enlace e Física | Enlace | Ethernet, Wi-Fi e meios físicos |

O OSI tem sete camadas conceituais. O TCP/IP descreve a arquitetura efetivamente usada na Internet. Não force correspondência perfeita: protocolos reais podem atravessar limites didáticos e executar várias funções.

<a id="s2-d2-encapsulamento"></a>
### 3. Encapsulamento e desencapsulamento

No emissor, cada camada recebe dados da camada superior e acrescenta informações de controle.

Fluxo simplificado:

`dados da aplicação -> cabeçalho de transporte -> cabeçalho IP -> cabeçalho e trailer de enlace -> bits e sinais`

No receptor, ocorre o caminho inverso:

`sinais e bits -> quadro -> pacote IP -> unidade de transporte -> dados da aplicação`

#### O que muda a cada salto

Considere estação A enviando dados a servidor B por dois roteadores:

- o quadro do primeiro enlace tem MAC de origem de A e MAC de destino do primeiro roteador;
- o primeiro roteador remove o quadro e cria outro para o enlace seguinte;
- os endereços MAC mudam conforme o enlace;
- os endereços IP de origem e destino normalmente permanecem de A a B;
- campos do cabeçalho IP podem mudar, como TTL no IPv4 ou Hop Limit no IPv6;
- NAT, quando presente, é uma exceção operacional que pode alterar endereços e portas — será estudado no Dia 3.

Pegadinha: o MAC de destino de um quadro não precisa ser o MAC do host IP remoto. Quando o destino está fora da rede local, normalmente é o MAC do gateway do próximo salto.

<a id="s2-d2-pdus"></a>
### 4. PDUs

PDU significa unidade de dados de protocolo. O nome depende da camada e do protocolo.

| Camada | Nome didático da PDU | Observação |
|---|---|---|
| Aplicação, Apresentação, Sessão | dados ou mensagem | nome varia com o protocolo |
| Transporte com TCP | segmento | cabeçalho TCP mais dados |
| Transporte com UDP | datagrama UDP | não confundir com datagrama IP |
| Rede/Internet | pacote ou datagrama IP | unidade do IP |
| Enlace | quadro | possui cabeçalho e, em Ethernet, trailer de verificação |
| Física | bits e sinais | representação no meio |

Não use "pacote" como resposta automática para qualquer camada quando a questão exige nomenclatura específica. Em linguagem cotidiana, pacote pode aparecer genericamente, mas a prova costuma cobrar a distinção didática.

<a id="s2-d2-mac"></a>
### 5. Endereço MAC

Em redes IEEE 802, o endereço MAC identifica interfaces na camada de enlace. Endereços de 48 bits são comuns e representados por seis octetos hexadecimais, por exemplo `AC-DE-48-23-45-67`.

Pontos essenciais:

- o quadro possui MAC de origem e MAC de destino;
- switches aprendem MAC de origem;
- o MAC tem alcance local ao enlace ou domínio de camada 2;
- roteadores removem o quadro recebido e criam novo quadro para o enlace seguinte;
- endereço MAC não substitui endereço IP;
- existem endereços universalmente administrados e localmente administrados;
- tecnologias atuais podem usar MAC aleatório ou mutável para privacidade.

Logo, não trate MAC como número necessariamente gravado, globalmente único e imutável em todos os contextos.

<a id="s2-d2-ipv4"></a>
### 6. IPv4

Um endereço IPv4 possui 32 bits, normalmente escritos em quatro octetos decimais de 0 a 255, como `192.168.10.77`.

O prefixo divide o endereço em:

- **bits de rede:** parte inicial comum aos endereços da sub-rede;
- **bits de host:** parte restante, usada para identificar posições dentro do bloco.

Em `192.168.10.77/26`:

- 26 bits pertencem ao prefixo;
- 6 bits restam para a parte de host;
- o bloco possui `2^6 = 64` endereços.

O endereçamento moderno é classless. Classes A, B e C têm valor histórico e ainda aparecem em questões, mas CIDR e prefixos explícitos determinam a rede. Não deduza máscara apenas pelo primeiro octeto quando o prefixo foi informado.

<a id="s2-d2-mascara"></a>
### 7. Máscara de rede e prefixo CIDR

A máscara IPv4 usa bits `1` contíguos para a parte de rede e bits `0` para a parte de host.

Exemplo `/26`:

`11111111.11111111.11111111.11000000`

Em decimal:

`255.255.255.192`

Tabela de valores válidos para um octeto de máscara contígua:

| Bits 1 no octeto | Binário | Decimal |
|---:|---|---:|
| 0 | 00000000 | 0 |
| 1 | 10000000 | 128 |
| 2 | 11000000 | 192 |
| 3 | 11100000 | 224 |
| 4 | 11110000 | 240 |
| 5 | 11111000 | 248 |
| 6 | 11111100 | 252 |
| 7 | 11111110 | 254 |
| 8 | 11111111 | 255 |

#### Conversão de máscara decimal para prefixo

Máscara `255.255.252.0`:

- primeiro octeto: 8 bits `1`;
- segundo: 8;
- terceiro, valor 252: 6;
- quarto: 0.

Total: `8 + 8 + 6 = 22`. Prefixo `/22`.

#### Conversão de prefixo para máscara

Prefixo `/20`:

- 16 bits preenchem dois octetos: `255.255`;
- restam 4 bits `1` no terceiro octeto: `240`;
- último octeto: `0`.

Máscara: `255.255.240.0`.

Uma máscara como `255.0.255.0` tem bits `1` não contíguos e não representa um prefixo CIDR IPv4 normal.

<a id="s2-d2-rede-broadcast-hosts"></a>
### 8. Endereço de rede, broadcast e hosts válidos

No IPv4 tradicional:

- **endereço de rede:** todos os bits de host em `0`;
- **endereço de broadcast dirigido da sub-rede:** todos os bits de host em `1`;
- **hosts válidos:** endereços entre rede e broadcast;
- **total de endereços:** `2^h`, em que `h` é a quantidade de bits de host;
- **hosts utilizáveis convencionais:** `2^h - 2`, para prefixos de sub-rede em que rede e broadcast são reservados.

Há exceções importantes:

- `/31` em enlace IPv4 ponto a ponto pode usar os dois endereços conforme a RFC 3021 — não se aplica a sub-rede multiacesso comum;
- `/32` representa um único endereço ou rota de host — não há faixa de hosts, rede e broadcast no sentido convencional;
- IPv6 não tem endereço de broadcast.

#### Método 1 — Operação AND

Endereço de rede é o resultado de `IP AND máscara` bit a bit.

Para um bit:

- `1 AND 1 = 1`;
- qualquer combinação com `0` resulta em `0`.

A operação preserva os bits protegidos pela máscara e zera os bits de host.

#### Método 2 — Tamanho do bloco

No octeto interessante, calcule:

`tamanho do bloco = 256 - valor do octeto da máscara`.

Para `/26`, máscara `255.255.255.192`:

`256 - 192 = 64`.

As redes no último octeto começam em 0, 64, 128 e 192.

<a id="s2-d2-calculos"></a>
### 9. Exemplos resolvidos de IPv4 e CIDR

#### Exemplo A — Rede, broadcast e hosts em `/26`

IP: `192.168.10.77/26`.

1. Máscara: `255.255.255.192`.
2. Bits de host: `32 - 26 = 6`.
3. Tamanho do bloco: `2^6 = 64`, ou `256 - 192 = 64`.
4. Inícios de bloco: 0, 64, 128 e 192.
5. O número 77 está no intervalo 64 a 127.

Resultado:

- rede: `192.168.10.64`;
- broadcast: `192.168.10.127`;
- primeiro host: `192.168.10.65`;
- último host: `192.168.10.126`;
- hosts convencionais: `2^6 - 2 = 62`.

#### Exemplo B — Bloco `/27`

IP: `10.20.30.200/27`.

1. Máscara: `255.255.255.224`.
2. Bits de host: `5`.
3. Bloco: `256 - 224 = 32`.
4. Inícios: 0, 32, 64, 96, 128, 160, 192 e 224.
5. O número 200 está no bloco 192 a 223.

Resultado:

- rede: `10.20.30.192`;
- broadcast: `10.20.30.223`;
- hosts: `10.20.30.193` a `10.20.30.222`;
- hosts convencionais: `2^5 - 2 = 30`.

#### Exemplo C — Prefixo no terceiro octeto

IP: `172.16.37.90/20`.

1. Máscara: `255.255.240.0`.
2. O octeto interessante é o terceiro.
3. Bloco: `256 - 240 = 16`.
4. Inícios do terceiro octeto: 0, 16, 32, 48 e assim por diante.
5. O valor 37 está no bloco 32 a 47.

Resultado:

- rede: `172.16.32.0`;
- broadcast: `172.16.47.255`;
- primeiro host: `172.16.32.1`;
- último host: `172.16.47.254`;
- bits de host: `12`;
- hosts convencionais: `2^12 - 2 = 4094`.

#### Exemplo D — Máscara para CIDR

Máscara: `255.255.255.240`.

- 24 bits nos três primeiros octetos;
- 4 bits no valor 240;
- prefixo `/28`;
- bits de host: 4;
- total: `2^4 = 16` endereços;
- hosts convencionais: 14.

#### Exemplo E — `/31` ponto a ponto

Bloco: `192.0.2.10/31`.

Os dois endereços são:

- `192.0.2.10`;
- `192.0.2.11`.

Em enlace ponto a ponto que implementa RFC 3021, ambos representam as duas extremidades. Não subtraia rede e broadcast. Fora desse contexto, não generalize `/31` para uma LAN multiacesso.

#### Exemplo F — `/32`

`203.0.113.9/32` identifica exatamente um endereço. A RFC 4632 o descreve como rota de host. Não existe intervalo de hosts nem broadcast de sub-rede a calcular.

#### Exemplo G — Divisão de `/24` em `/27`

Rede original: `192.168.50.0/24`.

Novo prefixo: `/27`.

- bits emprestados: `27 - 24 = 3`;
- sub-redes iguais: `2^3 = 8`;
- bits de host por sub-rede: `32 - 27 = 5`;
- endereços por sub-rede: `2^5 = 32`;
- hosts convencionais por sub-rede: 30;
- incremento: 32.

Redes resultantes:

| Sub-rede | Broadcast | Hosts válidos |
|---|---|---|
| `192.168.50.0/27` | `192.168.50.31` | `.1` a `.30` |
| `192.168.50.32/27` | `192.168.50.63` | `.33` a `.62` |
| `192.168.50.64/27` | `192.168.50.95` | `.65` a `.94` |
| `192.168.50.96/27` | `192.168.50.127` | `.97` a `.126` |
| `192.168.50.128/27` | `192.168.50.159` | `.129` a `.158` |
| `192.168.50.160/27` | `192.168.50.191` | `.161` a `.190` |
| `192.168.50.192/27` | `192.168.50.223` | `.193` a `.222` |
| `192.168.50.224/27` | `192.168.50.255` | `.225` a `.254` |

<a id="s2-d2-publicos-privados-especiais"></a>
### 10. Redes públicas, privadas e endereços especiais

#### IPv4 privado

A RFC 1918 reserva três blocos para uso privado:

| Bloco | Faixa completa |
|---|---|
| `10.0.0.0/8` | `10.0.0.0` a `10.255.255.255` |
| `172.16.0.0/12` | `172.16.0.0` a `172.31.255.255` |
| `192.168.0.0/16` | `192.168.0.0` a `192.168.255.255` |

Pegadinhas frequentes:

- `172.15.0.1` não pertence ao bloco privado;
- `172.32.0.1` também não;
- privado não significa automaticamente seguro;
- NAT é comum para conectar redes privadas à Internet, mas endereço privado e NAT são conceitos diferentes;
- os mesmos endereços privados podem ser reutilizados por organizações diferentes.

#### IPv4 público

Em abordagem de prova, endereço público é globalmente único e potencialmente roteável na Internet. A palavra "potencialmente" importa: nem todo endereço fora da RFC 1918 é utilizável como unicast público. A IANA mantém vários blocos especiais, de documentação, multicast, compartilhados ou reservados.

Assim, o teste correto não é apenas "não está na faixa privada". Primeiro exclua também os blocos de finalidade especial.

#### Loopback

- IPv4 reserva `127.0.0.0/8` para loopback.
- `127.0.0.1` é o endereço mais conhecido, mas não é o único do bloco.
- Esses endereços representam o próprio host e não devem aparecer fora dele.
- IPv6 usa `::1/128` para loopback.

#### IPv4 link-local e APIPA

O bloco IPv4 link-local reservado é `169.254.0.0/16`. Dentro dele, a faixa selecionável pela autoconfiguração da RFC 3927 vai de `169.254.1.0` a `169.254.254.255`; o primeiro e o último `/24` do bloco ficam reservados para uso futuro. A máscara usada nesse enlace é `/16`.

Em sistemas Microsoft, a configuração automática dessa natureza é conhecida como APIPA. Segundo a documentação Microsoft, um computador Windows configurado para DHCP pode atribuir a si próprio um endereço APIPA quando o servidor DHCP não existe ou não está disponível.

Consequências:

- permite comunicação apenas no enlace local, quando os demais parâmetros são compatíveis;
- não fornece, por si só, acesso roteado à Internet;
- costuma indicar falha ou ausência de DHCP em uma rede que esperava configuração dinâmica;
- não deve ser confundida com loopback nem com faixa privada RFC 1918.

#### Outros endereços que merecem reconhecimento

| Endereço ou bloco | Uso |
|---|---|
| `0.0.0.0` | endereço não especificado em contextos definidos pelo protocolo |
| `255.255.255.255` | broadcast limitado IPv4 no enlace local |
| `192.0.2.0/24` | documentação — TEST-NET-1 |
| `198.51.100.0/24` | documentação — TEST-NET-2 |
| `203.0.113.0/24` | documentação — TEST-NET-3 |

Os exemplos desta apostila usam blocos privados ou de documentação para evitar representar endereços públicos reais.

<a id="s2-d2-subredes"></a>
### 11. Sub-redes e planejamento de prefixos

Subnetting divide um bloco em prefixos menores. Ao aumentar o prefixo, bits antes disponíveis para hosts passam a identificar sub-redes.

Exemplo: `/24` dividido em `/26`.

- bits emprestados: 2;
- sub-redes iguais: `2^2 = 4`;
- bits de host: 6;
- endereços por sub-rede: 64;
- hosts convencionais por sub-rede: 62.

Os blocos começam em 0, 64, 128 e 192.

#### Quantidade de sub-redes

Se um prefixo original `/p` é dividido em novo prefixo `/q`, com `q > p`:

`quantidade de sub-redes iguais = 2^(q - p)`.

Essa fórmula pressupõe divisão completa em blocos do mesmo tamanho. Em VLSM, sub-redes de tamanhos diferentes podem coexistir, desde que não se sobreponham e respeitem alinhamento de prefixo.

#### Verificação de pertencimento

Em uma configuração coerente, dois IPv4 pertencem à mesma sub-rede quando usam a mesma máscara ou o mesmo comprimento de prefixo e, ao aplicar essa máscara aos dois endereços, produzem o mesmo endereço de rede — em outras palavras, compartilham o mesmo prefixo de rede.

Se as máscaras divergem, não basta calcular cada endereço apenas com sua própria máscara e comparar dois resultados. O teste precisa ser feito da perspectiva de cada host:

- A considera B local se `A AND máscara de A = B AND máscara de A`;
- B considera A local se `B AND máscara de B = A AND máscara de B`.

Os resultados podem ser diferentes e criar alcance assimétrico — A tenta entrega direta enquanto B tenta usar gateway, ou o inverso. Para afirmar simplesmente que ambos integram a mesma sub-rede lógica, a prova normalmente deve fornecer um prefixo comum e um mesmo identificador de rede.

Não basta comparar os primeiros três octetos. Em `/23`, `/26` ou outro prefixo, a fronteira pode estar dentro de um octeto.

<a id="s2-d2-gateway"></a>
### 12. Gateway padrão

O gateway padrão é o próximo salto usado quando a tabela do host não possui rota mais específica para o destino.

Processo simplificado:

1. O host aplica sua máscara ao próprio IP e ao IP de destino.
2. Se as redes coincidem, tenta entrega direta no enlace.
3. Se não coincidem, procura uma rota — normalmente a rota padrão.
4. No IPv4 Ethernet, usa ARP para descobrir o MAC do próximo salto.
5. Envia quadro ao gateway, mantendo no pacote IP o endereço do destino remoto.

Em uma sub-rede IPv4 convencional, o gateway configurado na interface do host precisa ser alcançável no enlace local e usar endereço válido daquela sub-rede. Endereço de rede ou broadcast não pode ser gateway de hosts comuns.

Gateway padrão não é obrigatoriamente o primeiro endereço utilizável. Usar `.1` é convenção de projeto, não regra do protocolo.

<a id="s2-d2-arp"></a>
### 13. ARP

ARP resolve endereço de protocolo em endereço de hardware no enlace local. Embora a RFC 826 tenha formato generalizável, nas redes IP atuais ARP é normalmente associado ao IPv4 — em IPv4 sobre Ethernet, relaciona endereço IPv4 e endereço MAC. O IPv6 não usa ARP para essa função.

Fluxo:

1. O host consulta o cache ARP.
2. Se não encontra a associação, transmite ARP Request em broadcast de camada 2.
3. O dispositivo que possui o IPv4 procurado responde, normalmente por unicast, com seu MAC.
4. A associação é armazenada temporariamente no cache.

Destino local:

- ARP procura o MAC do próprio host de destino.

Destino remoto:

- ARP procura o MAC do gateway ou próximo salto, não o MAC do servidor remoto.

ARP não atravessa roteadores e não usa porta TCP ou UDP. No IPv6, funções equivalentes e adicionais são executadas pelo Neighbor Discovery, baseado em ICMPv6, não pelo ARP tradicional.

<a id="s2-d2-icmp"></a>
### 14. ICMP e ICMPv6

ICMP transporta mensagens de controle, erro e diagnóstico relacionadas ao IP.

Exemplos no IPv4:

- Echo Request e Echo Reply, usados por `ping`;
- Destination Unreachable;
- Time Exceeded, útil para diagnóstico de saltos;
- Redirect, sob condições específicas.

ICMP:

- não torna o IP confiável;
- não substitui TCP;
- não usa porta TCP nem UDP;
- é carregado pelo IP e integra funcionalmente a camada Internet;
- pode ser filtrado, mas bloquear tudo indiscriminadamente pode prejudicar diagnóstico e funções da rede.

ICMPv6 é especificado separadamente e tem papel ainda mais central no IPv6. Além de erros e diagnóstico, dá suporte a mecanismos como Neighbor Discovery. Uma questão que trata ICMPv6 como simples cópia opcional do `ping` IPv4 está incompleta.

#### Neighbor Discovery, NS e NA

A RFC 4861 define o Neighbor Discovery do IPv6. Entre suas funções estão descoberta de roteadores e prefixos, resolução de endereço de enlace, detecção de vizinho inalcançável e apoio à detecção de endereço duplicado.

- **Neighbor Solicitation — NS:** solicitação ICMPv6 enviada para descobrir endereço de enlace, verificar alcançabilidade ou apoiar detecção de duplicidade. Na resolução inicial, é enviada ao endereço multicast solicited-node derivado do endereço-alvo.
- **Neighbor Advertisement — NA:** anúncio ICMPv6 que responde a uma NS ou comunica informação de vizinhança. Uma resposta solicitada normalmente retorna por unicast quando as condições da RFC permitem.
- **Router Solicitation — RS:** host solicita rapidamente anúncios de roteadores.
- **Router Advertisement — RA:** roteador anuncia sua presença e pode informar prefixos e parâmetros do enlace.

NS/NA não são "ARP com outro nome" em todos os detalhes — pertencem ao ICMPv6 e integram um conjunto maior de descoberta e manutenção de vizinhança. O uso de multicast solicited-node evita transmitir uma consulta a todos os nós como faria um broadcast IPv4 de ARP.

<a id="s2-d2-ipv6"></a>
### 15. IPv6

O IPv6 possui endereços de 128 bits. A representação normal usa oito grupos de 16 bits em hexadecimal:

`2001:0db8:0000:0000:0000:ff00:0042:8329`

Regras de abreviação:

- zeros à esquerda de um grupo podem ser omitidos;
- uma sequência contínua de grupos zero pode ser comprimida com `::`;
- `::` só pode aparecer uma vez no endereço, pois uma segunda ocorrência tornaria a expansão ambígua.

Forma abreviada do exemplo:

`2001:db8::ff00:42:8329`.

#### Tipos de endereço

- **Unicast:** identifica uma interface; o pacote é entregue a uma interface.
- **Multicast:** identifica grupo de interfaces; o pacote é entregue aos membros pertinentes.
- **Anycast:** o mesmo endereço é atribuído a mais de uma interface; o roteamento entrega a uma delas, normalmente a considerada mais próxima pela métrica.

**IPv6 não possui endereço de broadcast.** A RFC 4291 afirma que a função de broadcast é substituída por multicast.

Isso não obriga toda aplicação destinada a vários receptores a usar multicast. O emissor pode enviar cópias unicast separadas, uma para cada destino. Multicast é um mecanismo de endereçamento e entrega em grupo quando protocolo, aplicação e rede o utilizam — não uma exigência universal para qualquer comunicação com vários nós.

#### Prefixo e escopo multicast

Endereços multicast IPv6 pertencem a `ff00::/8`. No segundo octeto, bits indicam flags e um valor de escopo que limita onde o grupo é válido e até onde o tráfego deve se propagar.

Escopos frequentes:

| Valor de escopo | Escopo | Exemplo de interpretação |
|---:|---|---|
| `1` | interface-local | limitado a uma interface do próprio nó |
| `2` | link-local | limitado ao enlace |
| `4` | admin-local | região definida administrativamente |
| `5` | site-local | limitado a um site |
| `8` | organization-local | abrange sites de uma organização |
| `E` | global | escopo global |

Em `ff02::1`, o `2` representa escopo link-local e o grupo identifica todos os nós IPv6 do enlace. Roteadores não devem tratar esse grupo como broadcast nem encaminhá-lo além do escopo indicado.

#### Blocos especiais importantes

| Bloco | Uso |
|---|---|
| `::/128` | endereço não especificado |
| `::1/128` | loopback |
| `fe80::/10` | unicast link-local |
| `fc00::/7` | unique-local, com alta probabilidade de prefixo único e uso local conforme RFC 4193 |
| `2001:db8::/32` | documentação |

Unique-local não é chamado simplesmente de "IPv6 privado" em toda formulação técnica, embora cumpra finalidade local semelhante em vários projetos. A RFC 4193 define `fc00::/7`; prefixos localmente atribuídos usam o bit L igual a 1 e aparecem, na prática, em `fd00::/8`. Eles não são esperados na Internet global, mas podem ser roteados dentro de um site ou entre sites sob acordo explícito. Link-local é limitado ao enlace e não equivale a unique-local.

#### Prefixo IPv6

IPv6 usa notação CIDR, como `/64`, e não máscara decimal pontuada.

Exemplo:

`2001:db8:abcd:1200:1234:5678:9abc:def0/64`.

Prefixo da rede:

`2001:db8:abcd:1200::/64`.

Os 64 primeiros bits formam o prefixo e os demais identificam a interface conforme o método de endereçamento empregado. `/64` é tamanho muito comum em sub-redes IPv6, mas há outros prefixos para finalidades específicas.

Não aplique automaticamente `2^h - 2` ao IPv6. Não há reserva de endereço de rede e broadcast nos moldes do IPv4.

<a id="s2-d2-exemplos-praticos"></a>
## Exemplos práticos e resolvidos

### Exemplo 1 — Encapsulamento até servidor remoto

Uma estação abre conexão com servidor em outra rede.

1. A aplicação produz dados.
2. TCP acrescenta cabeçalho e forma segmentos.
3. IPv4 ou IPv6 acrescenta cabeçalho e forma pacote.
4. A estação identifica que o destino é remoto.
5. No IPv4 Ethernet, ARP resolve o MAC do gateway.
6. Ethernet cria quadro destinado ao MAC do gateway.
7. O roteador remove o quadro, reduz TTL ou Hop Limit e cria quadro adequado ao enlace seguinte.
8. O servidor desencapsula até entregar dados à aplicação.

### Exemplo 2 — Mesmo endereço, prefixos diferentes

Considere `192.168.1.130`.

- Em `/24`, rede `192.168.1.0` e broadcast `192.168.1.255`.
- Em `/26`, o valor 130 pertence ao bloco 128 a 191 — rede `192.168.1.128` e broadcast `192.168.1.191`.

Conclusão: endereço sem máscara ou prefixo não basta para determinar a sub-rede.

### Exemplo 3 — Endereço inválido para host convencional

Configuração pretendida: `10.0.5.64/26`.

Blocos `/26`: 0 a 63, 64 a 127, 128 a 191 e 192 a 255.

`10.0.5.64` é o endereço de rede do segundo bloco, não host convencional. A primeira opção de host desse bloco é `10.0.5.65` e o broadcast é `10.0.5.127`.

### Exemplo 4 — Gateway fora da sub-rede

Host: `192.168.20.70/27`.

- Bloco: 64 a 95.
- Hosts: 65 a 94.
- Gateway configurado: `192.168.20.97`.

O gateway está no bloco seguinte, 96 a 127. Sem mecanismo adicional, o host não o alcança diretamente no enlace como gateway da própria sub-rede. Um gateway válido poderia ser `192.168.20.65`, desde que essa interface exista e o projeto a tenha escolhido.

### Exemplo 5 — ARP para destino remoto

Host A: `192.168.10.20/24`.

Servidor B: `198.51.100.10`.

Gateway: `192.168.10.1`.

A percebe que B não pertence a `192.168.10.0/24`. Portanto, não procura o MAC de B por ARP. Procura o MAC de `192.168.10.1` e entrega o quadro ao roteador. O endereço IP de destino continua `198.51.100.10`.

### Exemplo 6 — IPv6 sem broadcast

Uma aplicação precisa alcançar um grupo de nós IPv6. Se o protocolo e a rede oferecem o grupo adequado, ela pode usar multicast; alternativamente, pode enviar vários unicasts, um para cada destino. O que não existe é um endereço de broadcast IPv6. `ff02::1`, por exemplo, é multicast de todos os nós com escopo link-local — não deve ser chamado de broadcast.

Na resolução de vizinho, um nó não envia `ff02::1` indiscriminadamente. Ele usa uma Neighbor Solicitation para o multicast solicited-node do alvo, e o alvo pode responder com Neighbor Advertisement. Esse fluxo é parte do Neighbor Discovery da RFC 4861.

<a id="s2-d2-diferencas"></a>
## Diferenças entre conceitos parecidos

| Conceitos | Diferença central |
|---|---|
| OSI x TCP/IP | OSI é referência de sete camadas; TCP/IP é arquitetura da suíte da Internet, normalmente apresentada em quatro |
| Aplicação x protocolo de aplicação | programa completo x regras de comunicação usadas pelo programa |
| Segmento TCP x datagrama UDP | PDUs de dois protocolos de transporte diferentes |
| Datagrama UDP x datagrama IP | unidade de transporte x unidade da camada Internet |
| Quadro x pacote | PDU do enlace x PDU de rede/Internet |
| MAC x IP | endereço de enlace local x endereço lógico usado entre redes |
| IP x porta | interface na rede x processo ou serviço de transporte |
| Máscara x gateway | separa prefixo e host x próximo salto para destinos remotos |
| Rede x broadcast | bits de host em zero x bits de host em um no IPv4 convencional |
| Privado x link-local | bloco RFC 1918 reutilizável em redes privadas x bloco limitado ao enlace |
| APIPA x loopback | autoconfiguração link-local x comunicação interna do próprio host |
| ARP x DNS | resolve IPv4 em MAC no enlace x resolve nomes em dados de DNS, frequentemente endereços IP |
| ARP x Neighbor Discovery | resolução normalmente usada pelo IPv4 x conjunto de mecanismos IPv6 baseados em ICMPv6, incluindo NS e NA |
| ICMP x TCP/UDP | controle e erro da camada Internet x protocolos de transporte |
| Broadcast x multicast | entrega a todos no domínio x entrega ao grupo interessado |
| IPv4 x IPv6 | 32 bits com broadcast x 128 bits sem broadcast |
| `/31` x `/32` | duas extremidades em enlace IPv4 ponto a ponto x um endereço ou rota de host |

<a id="s2-d2-revisao-fixa"></a>
## Revisão fixa do Dia 2

**Distribuição das extras:** 15 questões de Administração Pública e 5 questões de Português.

| Núcleo | Origem do conteúdo | Tratamento nesta semana |
|---|---|---|
| LIMPE, organização, atos, LAI/LGPD, licitação e responsabilidade civil | revisão da Semana 1 | aplicação em cenários curtos de órgão público |
| Atributos, convalidação e decadência administrativa | aprofundamento novo da Semana 2 | requisitos, limites e art. 54 da Lei nº 9.784/1999 |
| Improbidade dolosa e tipificada | revisão com aprofundamento | atualização da precisão conceitual |
| Quantificadores, conectores, pontuação, crase e reescrita | revisão da Semana 1 | aplicação à linguagem técnica de endereçamento |
| Modalidade verbal em contexto `/31` | aplicação nova da Semana 2 | distinção entre possibilidade, obrigação e recorte contextual |

O ponto de partida está nos Dias 5 e 6 da Semana 1. Esta seção seleciona apenas as regras necessárias às 20 extras do Dia 2 e explicita o que foi acrescentado nesta semana.

<a id="s2-d2-revisao-administracao"></a>
### Administração Pública — 15 questões extras

Esta revisão fornece base para as 20 questões extras do Dia 2. O objetivo é reconhecer a regra e aplicar a distinção em cenário curto.

<a id="s2-d2-revisao-principios"></a>
#### Princípios do art. 37 — LIMPE

| Princípio | Ideia operacional | Erro comum |
|---|---|---|
| Legalidade | Administração atua segundo o ordenamento e a competência atribuída | eficiência autorizar descumprir a lei |
| Impessoalidade | finalidade pública e vedação a favorecimento ou promoção pessoal | confundir com ausência de identificação do agente |
| Moralidade | padrão jurídico de probidade, lealdade e boa-fé | reduzir a moralidade a opinião pessoal |
| Publicidade | transparência e divulgação como regra, ressalvado sigilo legal | divulgar indiscriminadamente dado pessoal |
| Eficiência | resultado adequado, qualidade e bom uso de recursos | buscar velocidade a qualquer custo |

Eficiência não se sobrepõe à legalidade. Publicidade convive com sigilo legal e proteção de dados.

O art. 37, § 1º, da Constituição determina que a publicidade de atos, programas, obras, serviços e campanhas dos órgãos públicos tenha caráter educativo, informativo ou de orientação social, sem nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores. A regra torna concreta a cobrança de impessoalidade em campanhas institucionais.

<a id="s2-d2-revisao-organizacao"></a>
#### Administração Direta e Indireta

- **Administração Direta:** serviços integrados à estrutura dos entes políticos e de seus órgãos.
- **Administração Indireta:** autarquias, fundações públicas, empresas públicas e sociedades de economia mista, com personalidade jurídica própria.
- **Órgão:** centro de competências sem personalidade jurídica própria.
- **Entidade:** pessoa jurídica própria.
- **Autarquia:** pessoa jurídica de direito público criada por lei para desempenhar atividade administrativa típica.

O CRA-PR é autarquia e integra a Administração Indireta. Não é órgão da Administração Direta, sindicato ou associação privada.

<a id="s2-d2-revisao-atos"></a>
#### Elementos e atributos do ato administrativo

Elementos clássicos:

| Elemento | Pergunta de controle |
|---|---|
| Competência | quem pode praticar o ato? |
| Finalidade | qual interesse público legal deve ser alcançado? |
| Forma | como o ato se exterioriza? |
| Motivo | quais fatos e fundamentos justificam o ato? |
| Objeto | qual efeito jurídico é produzido? |

Atributos frequentemente cobrados:

- **presunção de legitimidade e veracidade:** presume-se, de forma relativa, que o ato esteja conforme o Direito e que os fatos declarados pela Administração sejam verdadeiros;
- **imperatividade:** pode impor obrigações independentemente da concordância do destinatário, quando cabível;
- **autoexecutoriedade:** permite execução direta em hipóteses legais ou urgentes — não existe em todo ato;
- **tipicidade:** o ato deve corresponder a figura prevista no ordenamento.

<a id="s2-d2-revisao-desfazimento"></a>
#### Anulação, revogação e convalidação

- **Anulação:** retira ato ilegal. A Lei nº 9.784/1999 determina que a Administração anule seus atos com vício de legalidade.
- **Revogação:** retira ato válido por conveniência ou oportunidade, respeitados direitos adquiridos.
- **Convalidação:** corrige vício sanável quando não houver lesão ao interesse público nem prejuízo a terceiros.

Não se revoga ato ilegal para "corrigi-lo". Não se anula ato apenas porque deixou de ser conveniente.

O poder de anular também possui limite temporal. Pelo art. 54 da Lei nº 9.784/1999, o direito da Administração de anular atos que geraram efeitos favoráveis aos destinatários decai em cinco anos, contados da prática do ato, salvo comprovada má-fé. Em efeitos patrimoniais contínuos, o prazo é contado da percepção do primeiro pagamento. Portanto, a frase "ato ilegal pode ser anulado a qualquer tempo, sem exceção" está errada no âmbito dessa lei.

<a id="s2-d2-revisao-lai-lgpd"></a>
#### LAI x LGPD

- A LAI concretiza acesso à informação pública — publicidade é a regra e restrição exige fundamento.
- A LGPD disciplina tratamento de dados pessoais, inclusive pelo Poder Público, segundo finalidade pública, interesse público, necessidade, transparência e segurança.
- As leis convivem. Transparência não autoriza exposição irrestrita de dados pessoais, e proteção de dados não cria sigilo automático para toda informação pública.

<a id="s2-d2-revisao-improbidade"></a>
#### Improbidade administrativa

A Lei nº 8.429/1992, na redação vigente, trata como improbidade as condutas dolosas tipificadas nos arts. 9º, 10 e 11. Mera voluntariedade ou simples ilegalidade não basta. É preciso enquadramento legal e dolo nos termos da lei.

Categorias centrais:

- enriquecimento ilícito;
- lesão ao erário;
- atos contra princípios, nos tipos previstos.

<a id="s2-d2-revisao-licitacao"></a>
#### Licitação e contratação direta

- **Dispensa:** competição é possível em tese, mas a lei autoriza contratação direta em hipótese definida.
- **Inexigibilidade:** competição é inviável.
- Contratação direta não significa ausência de processo, motivação, justificativa ou controle.

Modalidades da Lei nº 14.133/2021: pregão, concorrência, concurso, leilão e diálogo competitivo. Não confunda modalidade com critério de julgamento.

<a id="s2-d2-revisao-responsabilidade"></a>
#### Responsabilidade civil do Estado

O art. 37, § 6º, da Constituição fundamenta a responsabilidade das pessoas jurídicas de direito público e das prestadoras de serviços públicos pelos danos causados por seus agentes nessa qualidade, assegurado regresso contra o agente em caso de dolo ou culpa.

Na responsabilidade objetiva perante a vítima, ainda são necessários conduta estatal, dano e nexo causal. "Objetiva" não significa indenização automática.

<a id="s2-d2-revisao-exemplos-adm"></a>
#### Mini aplicações administrativas

- Autoridade usa publicidade institucional para promoção pessoal — risco de violação à impessoalidade.
- Administração retira ato válido porque se tornou inconveniente — revogação.
- Administração retira ato ilegal — anulação.
- Órgão divulga planilha com dados pessoais sem necessidade — publicidade não afasta a LGPD.
- Contratação tem fornecedor exclusivo comprovado e competição inviável — possível inexigibilidade, conforme requisitos legais.
- Um erro formal isolado, sem dolo tipificado — não se transforma automaticamente em improbidade.

<a id="s2-d2-revisao-portugues"></a>
### Português e interpretação — 5 questões extras

<a id="s2-d2-revisao-quantificadores"></a>
#### Quantificadores e alcance

- `Todo A é B` não significa `Todo B é A`.
- `Alguns` não autoriza concluir `todos`.
- `Pode` expressa possibilidade ou permissão, não obrigatoriedade.
- `Deve` e `é obrigatório` impõem sentido mais forte.
- `Em regra` admite exceção; `sempre` tende a eliminá-la.

Trecho: "Em enlaces IPv4 ponto a ponto, um prefixo `/31` pode usar os dois endereços."

Reescrita inadequada: "Toda rede IPv4 `/31` deve operar como LAN multiacesso com dois hosts." A reescrita troca contexto, possibilidade e modalidade de enlace.

<a id="s2-d2-revisao-coesao"></a>
#### Coesão e relação lógica

Trecho: "O IPv6 amplia o espaço de endereçamento; entretanto, esse fato não elimina a necessidade de planejamento."

- `Entretanto` indica oposição ou ressalva.
- O pronome demonstrativo `esse` retoma a ampliação do espaço.
- Não se pode inferir que planejamento deixa de ser necessário.

<a id="s2-d2-revisao-pontuacao"></a>
#### Pontuação

Não separe sujeito e verbo:

- errado: `Os endereços privados, podem ser reutilizados.`
- correto: `Os endereços privados podem ser reutilizados.`

Use vírgula para isolar expressão explicativa:

- `O ARP, no IPv4 sobre Ethernet, resolve endereço IP em MAC.`

A vírgula não deve alterar o vínculo essencial entre verbo e complemento.

<a id="s2-d2-revisao-crase"></a>
#### Crase aplicada

Há crase quando preposição `a` encontra artigo feminino `a`:

- `O pacote foi entregue à interface correta.`
- `A regra se aplica às sub-redes convencionais.`

Não há crase antes de verbo:

- `O roteador começou a encaminhar os pacotes.`

<a id="s2-d2-revisao-reescrita"></a>
#### Reescrita técnica

Ao avaliar equivalência, confira:

1. sujeito;
2. negação;
3. quantificador;
4. relação do conector;
5. condição ou exceção;
6. tempo verbal.

Original: "Embora o endereço esteja fora dos blocos privados definidos pela RFC 1918, ele pode pertencer a um bloco especial."

Equivalente: "Ainda que o endereço não pertença aos blocos privados definidos pela RFC 1918, é possível que integre um bloco especial."

Não equivalente: "Como o endereço está fora dos blocos privados definidos pela RFC 1918, ele é público e jamais integra um bloco especial."

<a id="s2-d2-revisao-tabela"></a>
### Diferenças, pegadinhas e tabela rápida da revisão fixa

| Conceito | Regra curta | Diferença ou pegadinha | Exemplo |
|---|---|---|---|
| órgão x entidade | centro sem personalidade x pessoa jurídica | chamar autarquia de órgão da Direta | secretaria x CRA-PR |
| Direta x Indireta | entes/órgãos x entidades próprias | autonomia não retira vinculação legal | ministério x autarquia |
| anulação x revogação x convalidação | ilegalidade x mérito x correção de vício sanável | ato inconveniente não se torna ilegal | retirar ato ilegal; revogar ato válido |
| dispensa x inexigibilidade | competição possível x inviável | contratação direta não elimina processo | hipótese legal x fornecedor exclusivo |
| modalidade x critério | procedimento licitatório x forma de julgar | pregão não é “menor preço” | pregão x menor preço |
| LAI x LGPD | transparência x proteção de dados | nenhuma delas elimina automaticamente a outra | documento público com dado pessoal |
| responsabilidade objetiva x automática | dispensa prova de culpa estatal x ainda exige dano e nexo | objetiva não significa indenização sem requisitos | dano causado por agente nessa qualidade |
| `pode` x `deve` | possibilidade/permissão x obrigação | trocar modalidade muda o alcance | `/31` pode ser usado em ponto a ponto |
| oposição x concessão x causa | contraste x obstáculo admitido x motivo | `entretanto`, `embora` e `porque` não são equivalentes | serviço responde; entretanto, há falha |

Pegadinhas prioritárias: usar eficiência contra a lei; promover agente em publicidade; confundir órgão e entidade; anular por conveniência; revogar ilegalidade; convalidar vício insanável; esquecer decadência e má-fé; tratar contratação direta como escolha livre; separar sujeito e verbo; e inserir crase antes de verbo.

<a id="s2-d2-tabela-rapida"></a>
## Tabela de revisão rápida do Dia 2

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| OSI | modelo de referência com sete camadas | tratá-lo como protocolo único | camada 3 — Rede |
| TCP/IP | arquitetura da suíte da Internet | exigir correspondência perfeita com OSI | aplicação, transporte, Internet, enlace |
| Encapsulamento | adição de informações por camada | inverter emissor e receptor | dados viram segmento, pacote e quadro |
| PDU | unidade de dados de protocolo | chamar toda PDU de pacote | quadro no enlace |
| Segmento | PDU TCP | usar para UDP em resposta específica | segmento TCP |
| Datagrama UDP | PDU UDP | confundir com datagrama IP | cabeçalho UDP e dados |
| Pacote IP | unidade da camada Internet | dizer que switch L2 roteia pelo IP | IPv4 entre hosts |
| Quadro | unidade da camada de enlace | dizer que atravessa intacto todos os roteadores | quadro Ethernet local |
| MAC | endereço de enlace | tratá-lo como imutável | MAC da NIC |
| IPv4 | endereço lógico de 32 bits | deduzir rede sem máscara | `192.168.10.77/26` |
| IPv6 | endereço lógico de 128 bits | criar broadcast IPv6 | `2001:db8::1` |
| Máscara | separa prefixo e host no IPv4 | aceitar bits 1 não contíguos | `255.255.255.192` |
| CIDR | prefixo escrito após barra | confundir `/24` com 24 hosts | `/24` tem 8 bits de host |
| Rede | bits de host zerados | atribuir a host convencional | `192.168.10.64/26` |
| Broadcast IPv4 | bits de host em um | aplicar ao IPv6 | `192.168.10.127/26` |
| Host válido | endereço entre rede e broadcast | esquecer `/31` e `/32` | `.65` a `.126` no bloco `/26` |
| `/31` | prefixo IPv4 para ponto a ponto | aplicar `2^h - 2` | duas extremidades conforme RFC 3021 |
| `/32` | um endereço ou rota de host | procurar faixa e broadcast | `203.0.113.9/32` |
| IPv4 privado | bloco RFC 1918 | incluir todo `172.0.0.0/8` | `172.16.0.0/12` |
| Loopback | comunicação do próprio host | dizer que é só `127.0.0.1` | `127.0.0.0/8` |
| Link-local IPv4 | comunicação limitada ao enlace | chamar de endereço público | `169.254.0.0/16` |
| APIPA | autoconfiguração IPv4 link-local | usar o primeiro ou último `/24` reservado como faixa selecionável | `169.254.1.0` a `169.254.254.255` |
| Gateway padrão | próximo salto da rota padrão | exigir que seja sempre `.1` | `192.168.10.1` |
| ARP | normalmente mapeia IPv4 em MAC no enlace | buscar MAC do servidor remoto ou atribuí-lo ao IPv6 | ARP do gateway IPv4 |
| ICMP | controle, erro e diagnóstico do IP | atribuir porta TCP | Echo e Time Exceeded |
| ICMPv6 | controle do IPv6 | reduzi-lo a ping | Neighbor Discovery com NS e NA |
| Unicast IPv6 | entrega a uma interface | confundir com grupo | endereço global de host |
| Multicast IPv6 | entrega a grupo em escopo definido | chamar de broadcast ou torná-lo obrigatório | `ff00::/8`; `ff02::1` é link-local |
| Anycast IPv6 | entrega a uma das interfaces | dizer que entrega a todas | serviço replicado |
| Prefixo IPv6 | parte inicial do endereço | usar máscara decimal pontuada | `2001:db8:abcd::/48` |

<a id="s2-d2-pegadinhas"></a>
## Pegadinhas do Dia 2

- OSI é modelo de referência, não uma pilha única que toda implementação reproduz literalmente.
- No modelo TCP/IP de quatro camadas, enlace e física do OSI ficam agrupados na camada de enlace.
- UDP usa datagrama; TCP usa segmento.
- Roteadores recriam o quadro em cada enlace — os MACs não permanecem de ponta a ponta.
- O IP de destino normalmente continua sendo o host remoto, mesmo quando o quadro vai ao MAC do gateway.
- Endereço IPv4 sem máscara não determina sozinho a sub-rede.
- Para afirmar pertencimento simétrico à mesma sub-rede, use prefixo comum; se as máscaras divergem, faça o teste da perspectiva de cada host com ambas as máscaras.
- `/24` significa 24 bits de prefixo, não 24 hosts.
- `255.255.255.192` é `/26`, não `/24`.
- A fórmula `2^h - 2` vale para hosts convencionais, mas não deve ser aplicada mecanicamente a `/31` e `/32`.
- `/31` usa os dois endereços apenas no contexto de enlace IPv4 ponto a ponto compatível.
- `/32` é um único endereço ou rota de host.
- IPv6 não possui endereço de broadcast.
- IPv6 usa prefixo, não máscara decimal pontuada.
- O bloco privado `172.16.0.0/12` termina em `172.31.255.255`.
- Nem todo IPv4 fora da RFC 1918 é público — há blocos especiais.
- `127.0.0.0/8` é loopback; `169.254.0.0/16` é link-local.
- APIPA não comprova funcionamento do DHCP — frequentemente indica que a configuração esperada não foi obtida; a faixa selecionável pela RFC 3927 vai de `169.254.1.0` a `169.254.254.255`.
- ARP não atravessa roteadores e não usa porta.
- ARP é normalmente associado ao IPv4; IPv6 usa Neighbor Discovery baseado em ICMPv6, com mensagens como NS e NA.
- Multicast IPv6 usa `ff00::/8` e possui escopos; uma aplicação também pode alcançar vários destinos com múltiplos unicasts.
- ICMP não garante entrega e não é protocolo TCP ou UDP.
- Publicidade administrativa não autoriza divulgação irrestrita de dados pessoais.
- Revogação atinge ato válido por mérito; anulação atinge ilegalidade.
- Pelo art. 54 da Lei nº 9.784/1999, a anulação de ato com efeitos favoráveis está sujeita, em regra, à decadência de cinco anos, salvo comprovada má-fé.
- Improbidade não é sinônimo de qualquer erro ou ilegalidade.
- No Português, `embora` indica concessão e `entretanto` indica oposição.

<a id="s2-d2-pratica"></a>
## Prática guiada

### Roteiro 1 — Decorar camadas por função, não só por nome

Monte uma tabela em branco com as sete camadas. Para cada uma, preencha:

- função principal;
- uma PDU, quando houver nome específico;
- um endereço ou identificador pertinente;
- um protocolo ou tecnologia;
- um equipamento associado, sem tratar a associação como exclusividade absoluta.

Depois trace uma requisição da aplicação até a camada física e o retorno até a aplicação remota.

### Roteiro 2 — Procedimento universal de cálculo IPv4

Use o endereço `192.168.44.178/27`.

1. Máscara: `/27 = 255.255.255.224`.
2. Bits de host: `5`.
3. Bloco: `256 - 224 = 32`.
4. Inícios: 0, 32, 64, 96, 128, 160, 192 e 224.
5. O valor 178 está no bloco 160 a 191.

Conferência:

- rede: `192.168.44.160`;
- broadcast: `192.168.44.191`;
- hosts: `.161` a `.190`;
- hosts convencionais: 30.

Repita o mesmo algoritmo para `10.10.14.3/23`:

- máscara: `255.255.254.0`;
- bloco no terceiro octeto: 2;
- 14 está no bloco 14 a 15;
- rede: `10.10.14.0`;
- broadcast: `10.10.15.255`;
- hosts: `10.10.14.1` a `10.10.15.254`;
- hosts convencionais: `2^9 - 2 = 510`.

### Roteiro 3 — Converter máscaras sem adivinhar

Transforme cada octeto pela tabela de bits:

- `255.255.248.0` — `8 + 8 + 5 = /21`;
- `255.255.255.252` — `8 + 8 + 8 + 6 = /30`;
- `/18` — `255.255.192.0`;
- `/29` — `255.255.255.248`.

Marque como inválida para CIDR normal a máscara `255.255.240.255`, pois os bits `1` não são contíguos.

### Roteiro 4 — Entrega local e remota

Desenhe host A, switch, roteador e host B remoto.

- Na entrega local, escreva MAC e IP do destino local.
- Na entrega remota, escreva MAC do gateway no quadro e IP de B no pacote.
- Em cada roteador, risque o quadro antigo e desenhe o novo.
- Anote que TTL ou Hop Limit é atualizado.

### Roteiro 5 — Exceções e IPv6

Crie três cartões de recuperação ativa:

- `/31` — duas extremidades em enlace ponto a ponto, sem subtração de rede e broadcast;
- `/32` — um endereço ou rota de host;
- IPv6 — 128 bits e nenhum endereço de broadcast.

No verso, escreva a fonte técnica: RFC 3021, RFC 4632 e RFC 4291.

### Roteiro 6 — Revisões fixas

Sem consulta, escreva:

- LIMPE e uma aplicação concreta de cada princípio;
- Administração Direta x Indireta;
- órgão x entidade;
- anulação x revogação x convalidação;
- LAI x LGPD;
- dispensa x inexigibilidade;
- inferência x extrapolação;
- oposição x concessão x conclusão.

Corrija a lista com base nas seções correspondentes.

<a id="s2-d2-checklist"></a>
## Checklist de domínio

- [ ] Nomeio e explico as sete camadas do OSI.
- [ ] Explico as quatro camadas usuais do TCP/IP.
- [ ] Faço o mapeamento OSI x TCP/IP sem exigir equivalência perfeita.
- [ ] Acompanho encapsulamento e desencapsulamento.
- [ ] Diferencio dados, segmento TCP, datagrama UDP, pacote IP, quadro e bits.
- [ ] Diferencio MAC, IP e porta.
- [ ] Sei por que os MACs mudam entre enlaces roteados.
- [ ] Interpreto IPv4 de 32 bits e prefixo CIDR.
- [ ] Converto máscara decimal em prefixo.
- [ ] Converto prefixo em máscara decimal.
- [ ] Calculo endereço de rede por bloco ou AND.
- [ ] Calculo broadcast IPv4.
- [ ] Calculo primeiro e último host convencionais.
- [ ] Calculo quantidade de endereços e hosts.
- [ ] Trato `/31` como exceção ponto a ponto.
- [ ] Trato `/32` como endereço ou rota de host.
- [ ] Divido uma rede em sub-redes iguais.
- [ ] Testo pertencimento com prefixo comum e, se as máscaras divergem, avalio a perspectiva de cada host.
- [ ] Reconheço as três faixas RFC 1918.
- [ ] Diferencio público, privado, loopback e link-local.
- [ ] Reconheço APIPA e sua limitação ao enlace.
- [ ] Sei que a faixa APIPA selecionável vai de `169.254.1.0` a `169.254.254.255`.
- [ ] Explico o papel do gateway padrão.
- [ ] Explico ARP para destino local e remoto.
- [ ] Diferencio ARP normalmente usado no IPv4 de Neighbor Discovery no IPv6.
- [ ] Explico ICMP e sei que ele não usa porta TCP/UDP.
- [ ] Reconheço endereço IPv6 de 128 bits e suas abreviações.
- [ ] Sei que `::` só pode comprimir uma sequência uma vez.
- [ ] Diferencio unicast, multicast e anycast no IPv6.
- [ ] Reconheço `ff00::/8`, os principais escopos multicast e as funções de NS e NA.
- [ ] Sei que multicast não é obrigatório quando múltiplos unicasts atendem à aplicação.
- [ ] Sei que IPv6 não possui broadcast.
- [ ] Reconheço `::1/128`, `fe80::/10`, `fc00::/7` e `2001:db8::/32`.
- [ ] Diferencio LIMPE, Administração Direta/Indireta e órgão/entidade.
- [ ] Diferencio anulação, revogação e convalidação.
- [ ] Aplico a decadência do art. 54 da Lei nº 9.784/1999 aos atos favoráveis, ressalvada má-fé.
- [ ] Diferencio LAI e LGPD.
- [ ] Interpreto quantificadores, conectores, pontuação e crase em enunciados técnicos.

<a id="s2-d2-caderno-erros"></a>
## Orientações para o caderno de erros

Crie a página **Dia 2 — Camadas, endereços e CIDR**.

Para cada cálculo errado, registre obrigatoriamente:

- IP e prefixo originais;
- máscara decimal;
- octeto interessante;
- tamanho do bloco;
- endereço de rede;
- broadcast;
- faixa de hosts;
- fórmula usada;
- etapa exata em que ocorreu o erro.

Separe ainda quatro quadros:

1. **Camadas e PDUs:** registre trocas como quadro/pacote e segmento/datagrama.
2. **Escopo de endereços:** MAC local, IP lógico e porta de processo.
3. **Exceções:** `/31`, `/32`, IPv6 sem broadcast, ARP normalmente no IPv4 e Neighbor Discovery no IPv6.
4. **Revisões fixas:** norma administrativa ou regra de Português que alterou a resposta.

Frase de verificação para todo cálculo IPv4:

Para um endereço de host convencional em prefixos IPv4 de `/0` a `/30`, use a verificação:

`rede < IP do host < broadcast`.

Ela não descreve um endereço que seja a própria rede ou o próprio broadcast e não se aplica às semânticas especiais de `/31` e `/32`.

Agende nova resolução dos mesmos cálculos para 24 horas e 7 dias depois, sem consultar a resposta anterior.

<a id="s2-d2-fontes"></a>
## Fontes utilizadas no Dia 2

Fontes técnicas e institucionais primárias ou oficiais consultadas:

- ISO/IEC 7498-1:1994 — modelo de referência OSI — https://www.iso.org/standard/20269.html
- RFC 1122 — camadas de comunicação da arquitetura da Internet — https://www.rfc-editor.org/rfc/rfc1122.html
- RFC 1123 — protocolos de aplicação e suporte — https://www.rfc-editor.org/rfc/rfc1123.html
- RFC 791 — Internet Protocol IPv4 — https://www.rfc-editor.org/rfc/rfc791.html
- RFC 8200 — Internet Protocol Version 6 — https://www.rfc-editor.org/rfc/rfc8200.html
- RFC 4291 — arquitetura de endereçamento IPv6 e ausência de broadcast — https://www.rfc-editor.org/rfc/rfc4291.html
- RFC 4632 — CIDR e prefixos `/31` e `/32` — https://www.rfc-editor.org/rfc/rfc4632.html
- RFC 3021 — uso de `/31` em enlaces IPv4 ponto a ponto — https://www.rfc-editor.org/rfc/rfc3021.html
- RFC 1918 — endereços IPv4 privados — https://www.rfc-editor.org/rfc/rfc1918.html
- RFC 3927 — IPv4 link-local — https://www.rfc-editor.org/rfc/rfc3927.html
- RFC 826 — ARP — https://www.rfc-editor.org/rfc/rfc826.html
- RFC 792 — ICMP para IPv4 — https://www.rfc-editor.org/rfc/rfc792.html
- RFC 4443 — ICMPv6 — https://www.rfc-editor.org/rfc/rfc4443.html
- RFC 4861 — Neighbor Discovery for IPv6 — https://www.rfc-editor.org/rfc/rfc4861.html
- RFC 4193 — Unique Local IPv6 Unicast Addresses — https://www.rfc-editor.org/rfc/rfc4193.html
- Microsoft Learn — Automatic Private IP Addressing — https://learn.microsoft.com/en-us/windows-server/troubleshoot/how-to-use-automatic-tcpip-addressing-without-a-dh
- IANA — registro de endereços IPv4 de finalidade especial — https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
- IANA — registro de endereços IPv6 de finalidade especial — https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml
- IEEE Registration Authority — endereços MAC e EUI-48 — https://standards.ieee.org/products-programs/regauth/mac/
- Constituição Federal de 1988 — art. 37 — https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm
- Decreto-Lei nº 200/1967 — Administração Direta e Indireta — https://www.planalto.gov.br/ccivil_03/decreto-lei/del0200.htm
- Lei nº 9.784/1999 — processo administrativo, anulação, revogação e convalidação — https://www.planalto.gov.br/ccivil_03/leis/l9784.htm
- Lei nº 12.527/2011 — Lei de Acesso à Informação — https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm
- Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais, texto compilado — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- Lei nº 8.429/1992 — Lei de Improbidade Administrativa, texto compilado — https://www.planalto.gov.br/ccivil_03/leis/l8429compilada.htm
- Lei nº 14.133/2021 — Licitações e Contratos Administrativos — https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm
- RN CFA nº 651/2024 — Regimento do CRA-PR e natureza autárquica — https://documentos.cfa.org.br/?a=show&c=documento&id=955
- Manual de Redação da Presidência da República — https://www.gov.br/pt-br/servicos/consultar-o-manual-de-redacao-da-presidencia-da-republica
# Dia 3 — Protocolos e Serviços de Rede

## Objetivo do dia

Compreender como os principais protocolos e serviços de rede funcionam, em que camada lógica atuam, quais transportes e portas utilizam e como se relacionam em um acesso real a sistemas. Ao final do dia, o estudante deve ser capaz de seguir o caminho completo entre a configuração de um cliente, a resolução de um nome, a criação de uma conexão, a proteção do canal e a entrega do serviço de aplicação.

O foco não é decorar uma lista isolada de siglas. É entender:

- o problema que cada protocolo resolve;
- quem inicia a comunicação;
- qual transporte é usado;
- quais garantias pertencem ao protocolo e quais dependem de outra camada;
- quais portas são valores padrão, sem tratá-las como regra imutável;
- quais conceitos parecidos a banca pode trocar em uma alternativa.

## Resultados esperados

Ao concluir as 6 horas líquidas, o estudante deverá conseguir:

- diferenciar protocolo, serviço, porta, cliente e servidor;
- explicar TCP e UDP sem dizer que UDP é simplesmente “ruim” ou que TCP garante sucesso da operação de negócio;
- relacionar HTTP, HTTPS, DNS, DHCP, SMTP, POP3, IMAP, FTP, SFTP, SSH, Telnet, SNMP, LDAP, proxy, NAT, PAT e NTP às suas funções;
- reconhecer as portas conhecidas mais cobradas e o transporte típico;
- descrever resolução recursiva e iterativa de nomes e o papel do cache DNS;
- descrever a concessão DHCP e a sequência DORA;
- explicar o envio e o acesso a correio eletrônico;
- distinguir FTP, FTPS e SFTP, sem apresentar SFTP como FTP sobre TLS;
- diferenciar proxy direto, proxy reverso, NAT básico e PAT/NAPT;
- interpretar um fluxo integrado de acesso a um serviço público;
- revisar o núcleo de Legislação CRA/CFA e pontos recorrentes de Português.

## Por que esse assunto importa para a prova

Protocolos e serviços aparecem no edital como conteúdo direto de redes, mas também sustentam segurança, sistemas operacionais, aplicações web e administração de infraestrutura. Uma única situação pode exigir várias associações: DHCP entrega parâmetros ao cliente, DNS resolve o nome, TCP ou UDP transporta dados, TLS protege o canal, NAT/PAT traduz o fluxo e NTP mantém relógios coerentes para logs e certificados.

Em provas objetivas, a dificuldade costuma estar menos na definição isolada e mais na troca de uma propriedade entre protocolos. Exemplos clássicos:

- atribuir resolução de nomes ao DHCP;
- dizer que DNS usa somente UDP;
- trocar SMTP por POP3 ou IMAP;
- tratar SFTP como FTP protegido por TLS;
- confundir proxy com NAT;
- dizer que porta conhecida identifica, por si só, tráfego legítimo ou criptografado;
- afirmar que TCP confirma que a transação da aplicação foi concluída.

## Como o Instituto Consulplan pode cobrar

O estilo esperado combina:

- associação entre protocolo, função e porta;
- cenário de usuário que não recebe endereço, não resolve nomes ou não acessa um serviço;
- comparação entre TCP e UDP;
- análise de sequência de mensagens DHCP;
- interpretação de registros DNS;
- distinção entre envio e acesso a correio;
- escolha do protocolo correto para administração remota ou transferência segura;
- cenário de vários hosts privados compartilhando um endereço público;
- identificação de afirmação absoluta, como “DNS sempre usa UDP”;
- caso de órgão público em que logs possuem horários divergentes por falha de sincronização.

Palavras como “sempre”, “somente”, “garante”, “substitui” e “é sinônimo” merecem atenção. Elas frequentemente transformam uma ideia parcialmente correta em alternativa errada.

## Cronograma de 6h líquidas

As pausas não entram na soma. Sugestão: pausa de 10 a 15 minutos após cada bloco longo.

| Bloco | Atividade | Tempo |
|---|---|---:|
| 1 | Recuperação ativa: camadas, encapsulamento, IP e portas | 25 min |
| 2 | TCP × UDP, portas e modelo cliente-servidor | 45 min |
| 3 | HTTP/HTTPS, DNS e DHCP | 80 min |
| 4 | SMTP, POP3, IMAP, FTP, SFTP, SSH e Telnet | 65 min |
| 5 | SNMP, LDAP, proxy, NAT básico, PAT/NAPT e NTP | 55 min |
| 6 | Exemplos integrados e diferenças entre conceitos | 30 min |
| 7 | Revisão fixa: Legislação CRA/CFA | 30 min |
| 8 | Revisão fixa: Português e interpretação | 15 min |
| 9 | Prática guiada, checklist e caderno de erros | 15 min |
| **Total líquido** |  | **360 min** |

## Teoria aprofundada

<a id="s2-d3-protocolo-porta"></a>
### 1. Protocolo, serviço, porta e socket

Um **protocolo** define regras de comunicação: formato das mensagens, ordem esperada, significado dos campos e comportamento diante de eventos. Um **serviço** é a capacidade oferecida por uma aplicação ou equipamento, como resolver nomes, entregar endereços ou receber páginas web.

Uma **porta de transporte** é um identificador de 16 bits usado por TCP ou UDP para encaminhar dados à aplicação adequada no host. A porta não é física e não pertence ao roteador como um conector. O par endereço IP + protocolo de transporte + porta ajuda o sistema operacional a entregar o tráfego ao processo correto.

Um **socket**, em sentido prático, é uma extremidade de comunicação mantida pelo sistema operacional. Uma conexão TCP costuma ser identificada pelo conjunto:

- IP de origem;
- porta de origem;
- IP de destino;
- porta de destino;
- protocolo TCP.

Dois clientes podem acessar simultaneamente o mesmo servidor na porta 443 porque usam endereços e/ou portas de origem diferentes.

#### Portas conhecidas não são uma garantia

As portas de 0 a 1023 formam a faixa de portas de sistema ou bem conhecidas no registro da IANA. Isso não impede:

- executar HTTP em 8080;
- executar SSH em porta diferente de 22;
- transportar conteúdo malicioso pela porta 443;
- configurar um serviço incorreto na porta tradicional de outro protocolo.

Em prova, associe a porta ao **padrão normalmente cobrado**, mas não conclua que a porta determina sozinha o protocolo, a legitimidade ou a segurança do conteúdo.

<a id="s2-d3-tcp-udp"></a>
### 2. TCP × UDP

#### 2.1 TCP: orientado à conexão e confiável

O TCP fornece à aplicação um **fluxo de bytes confiável e ordenado**. Antes da troca normal de dados, cliente e servidor estabelecem estado de conexão. A abertura clássica usa:

1. **SYN:** cliente propõe iniciar e apresenta seu número inicial de sequência;
2. **SYN-ACK:** servidor reconhece o SYN e apresenta seu próprio número;
3. **ACK:** cliente confirma a resposta.

Durante a transferência, o TCP usa números de sequência, confirmações, temporizadores e retransmissões para detectar perdas e reconstruir o fluxo na ordem. Também possui controle de fluxo e mecanismos de controle de congestionamento.

Pontos essenciais:

- TCP preserva a ordem dos bytes;
- TCP detecta perdas e pode retransmitir;
- TCP não preserva fronteiras de mensagens da aplicação: a aplicação recebe um fluxo;
- o ACK confirma recebimento no nível TCP, não aprovação de pagamento, gravação definitiva em banco ou sucesso semântico;
- conexão estabelecida não significa que o servidor esteja autorizado ou que o conteúdo esteja criptografado.

#### 2.2 UDP: datagramas sem conexão

O UDP envia **datagramas independentes**, sem estabelecer conexão no próprio protocolo. O cabeçalho é pequeno e não oferece, por si só:

- confirmação de entrega;
- retransmissão;
- ordenação;
- eliminação de duplicatas;
- controle de fluxo equivalente ao TCP.

Isso não significa que uma aplicação sobre UDP seja necessariamente não confiável. A própria aplicação pode implementar confirmações, controle de perda, criptografia e outras funções. O DNS tradicional usa frequentemente UDP; o NTP usa UDP; o DHCP usa UDP; o SNMP normalmente usa UDP. O HTTP/3 usa QUIC sobre UDP e implementa confiabilidade acima do UDP.

#### 2.3 Escolha do transporte

TCP é apropriado quando a aplicação precisa de fluxo ordenado e prefere delegar confiabilidade ao transporte. UDP é útil quando:

- mensagens são curtas e independentes;
- baixa latência é relevante;
- multicast ou broadcast é necessário;
- a aplicação controla sua própria recuperação;
- perder uma atualização antiga pode ser melhor do que atrasar as seguintes.

Não use a fórmula “TCP é lento; UDP é rápido” como definição. Desempenho depende do protocolo de aplicação, rede, implementação, congestionamento, tamanho das mensagens e requisitos de confiabilidade.

<a id="s2-d3-http-https"></a>
### 3. HTTP e HTTPS

#### 3.1 HTTP

HTTP é um protocolo de aplicação baseado em requisições e respostas. Em uma transação simplificada:

1. o cliente envia método, alvo, cabeçalhos e, quando aplicável, corpo;
2. o servidor processa a requisição;
3. o servidor devolve código de estado, cabeçalhos e corpo.

Métodos frequentes:

- **GET:** obter uma representação;
- **HEAD:** obter cabeçalhos sem o corpo da resposta;
- **POST:** submeter dados para processamento;
- **PUT:** criar ou substituir a representação no alvo indicado, conforme a semântica da aplicação;
- **DELETE:** solicitar remoção do recurso;
- **PATCH:** solicitar alteração parcial, conforme especificação aplicável.

Classes de status:

- 1xx: informação;
- 2xx: sucesso no nível HTTP;
- 3xx: redirecionamento;
- 4xx: erro associado à requisição do cliente;
- 5xx: falha do servidor ao atender.

HTTP é descrito como **stateless** porque cada requisição possui semântica própria e o protocolo não exige que o servidor retenha uma sessão de usuário entre requisições. Aplicações podem criar estado com cookies, tokens, sessões no servidor ou outros mecanismos.

Porta padrão mais cobrada: **80/TCP**. HTTP/1.1 e HTTP/2 usam TCP. HTTP/3 é uma exceção moderna relevante: usa QUIC sobre UDP, normalmente na porta 443.

#### 3.2 HTTPS

HTTPS é HTTP protegido por TLS. Em implementações usuais, o TLS:

- negocia parâmetros criptográficos;
- autentica o servidor por certificado, desde que o cliente valide corretamente a cadeia e o nome;
- estabelece chaves de sessão;
- protege confidencialidade e integridade dos dados em trânsito.

Porta padrão: **443**, com TCP para HTTP/1.1 e HTTP/2 e UDP/QUIC no caso de HTTP/3.

HTTPS não garante:

- que o conteúdo publicado seja verdadeiro;
- que a aplicação não tenha vulnerabilidades;
- que o dispositivo cliente esteja livre de malware;
- que o usuário esteja autorizado a acessar todo recurso;
- anonimato completo, pois metadados de rede ainda podem ser observáveis.

<a id="s2-d3-dns"></a>
### 4. DNS — sistema distribuído de nomes e dados

DNS é um sistema distribuído e hierárquico que associa nomes de domínio a diferentes tipos de dados. O uso mais conhecido é obter endereços IP a partir de um nome fictício como portal.example, mas DNS não se resume a “converter nome em IP”: também publica, por exemplo, servidores de correio, servidores autoritativos, aliases, textos e informações de zona.

#### 4.1 Componentes

- **Stub resolver:** componente do host que encaminha a consulta;
- **resolvedor recursivo:** recebe a consulta do cliente e busca ou recupera a resposta em cache;
- **servidor raiz:** indica servidores do domínio de topo;
- **servidor de TLD:** indica servidores autoritativos da zona;
- **servidor autoritativo:** responde com os dados publicados para a zona pela qual possui autoridade; “autoritativo” não garante que a configuração esteja factual ou operacionalmente correta.

#### 4.2 Recursão, iteração e cache

Na consulta recursiva, o cliente pede ao resolvedor que entregue uma resposta final ou um erro. O resolvedor pode usar respostas iterativas: cada servidor informa a melhor referência que conhece até que o autoritativo seja encontrado.

O cache reduz latência e tráfego. O **TTL** indica por quanto tempo o registro pode ser reutilizado em cache. TTL não significa tempo de vida do domínio nem prazo de funcionamento do servidor.

#### 4.3 Registros frequentes

- **A:** nome para endereço IPv4;
- **AAAA:** nome para endereço IPv6;
- **CNAME:** alias para outro nome canônico;
- **MX:** servidores de correio do domínio;
- **NS:** servidores autoritativos da zona;
- **SOA:** informações administrativas fundamentais da zona;
- **PTR:** resolução reversa de endereço para nome;
- **TXT:** texto associado ao domínio, usado também por mecanismos de validação e políticas.

#### 4.4 Transportes do DNS clássico

O DNS clássico, sem encapsulamento em outro protocolo, usa **53/UDP e 53/TCP**.

- UDP é comum em consultas e respostas curtas;
- TCP é usado em transferências de zona e também quando tamanho, truncamento ou outras condições exigem;
- implementações modernas de DNS devem suportar TCP, portanto “DNS usa somente UDP” é falso.

DNS tradicional em porta 53 não oferece, sozinho, confidencialidade nem autenticação criptográfica das respostas. DNSSEC busca autenticidade e integridade dos dados, não confidencialidade. DNS sobre TLS usa, por padrão, a porta 853; DNS sobre HTTPS usa HTTPS, normalmente na porta 443. Portanto, “DNS usa a porta 53” deve ser entendido como a convenção do DNS clássico, não como descrição de todo transporte DNS possível.

<a id="s2-d3-dhcp"></a>
### 5. DHCP — atribuição dinâmica de configuração

DHCP entrega parâmetros de configuração ao cliente, como:

- endereço IP;
- máscara/prefixo;
- gateway padrão;
- servidores DNS;
- duração da concessão;
- outras opções definidas.

O cliente que ainda não possui configuração utilizável não consegue simplesmente enviar unicast a um servidor distante. Por isso, o processo inicial pode usar broadcast e um agente relay.

#### 5.1 Sequência DORA

1. **DHCPDISCOVER:** cliente procura servidores;
2. **DHCPOFFER:** servidor oferece configuração;
3. **DHCPREQUEST:** cliente solicita formalmente a oferta escolhida;
4. **DHCPACK:** servidor confirma a concessão.

Portas clássicas:

- servidor: **67/UDP**;
- cliente: **68/UDP**.

O **lease** é temporário. O cliente tenta renová-lo antes do vencimento. Um **DHCP relay** encaminha mensagens entre segmentos, permitindo servidor central sem colocar um servidor em cada VLAN.

DHCP não resolve nomes como função principal, não traduz endereços e não comprova identidade do usuário.

<a id="s2-d3-email"></a>
### 6. Correio eletrônico: SMTP, POP3 e IMAP

#### 6.1 SMTP

SMTP é usado para **submissão e transferência de mensagens**. Ele movimenta correio do cliente para o servidor de submissão e entre servidores de correio.

Portas importantes:

- **25/TCP:** transferência entre servidores;
- **587/TCP:** submissão de mensagens pelo cliente, normalmente com autenticação e possibilidade de STARTTLS;
- **465/TCP:** submissão com TLS implícito.

SMTP não é o protocolo típico para o usuário organizar pastas e ler mensagens já armazenadas.

#### 6.2 POP3

POP3 é um protocolo de acesso com modelo mais simples, tradicionalmente associado ao download de mensagens para o cliente. Pode manter cópia no servidor conforme configuração, portanto “POP3 sempre apaga a mensagem do servidor” é uma generalização errada.

Portas:

- **110/TCP:** POP3;
- **995/TCP:** POP3 com TLS implícito.

#### 6.3 IMAP

IMAP mantém a caixa postal e seu estado no servidor, permitindo sincronização de pastas, mensagens, marcadores e múltiplos clientes.

Portas:

- **143/TCP:** IMAP, com possibilidade de STARTTLS;
- **993/TCP:** IMAP com TLS implícito.

#### 6.4 Fluxo integrado de e-mail

Um cliente submete a mensagem por SMTP. O servidor consulta registros MX do domínio de destino, entrega a outro servidor por SMTP e o destinatário acessa a caixa por IMAP ou POP3. TLS de transporte protege trechos da comunicação, mas não equivale automaticamente a criptografia ponta a ponta do conteúdo.

<a id="s2-d3-transferencia-remota"></a>
### 7. FTP, FTPS, SFTP, SSH e Telnet

#### 7.1 FTP

FTP é um protocolo de transferência de arquivos que separa:

- **conexão de controle:** normalmente 21/TCP;
- **conexão de dados:** separada da conexão de controle.

No modo ativo, a porta 20/TCP é tradicionalmente associada ao lado servidor da conexão de dados. No modo passivo, o servidor informa outra porta para que o cliente inicie a conexão de dados. Por isso, dizer que toda transferência FTP usa apenas as portas 20 e 21 ignora o modo passivo.

FTP clássico não protege credenciais e conteúdo contra leitura na rede.

#### 7.2 FTPS

FTPS é FTP protegido por TLS. Ele preserva os comandos e a arquitetura do FTP, inclusive a separação entre **canal de controle** e **conexões de dados**.

No **FTPS explícito**, método padronizado pelo RFC 4217, o cliente inicia a sessão na porta normal de controle do FTP, **21/TCP**, envia `AUTH TLS` e negocia TLS para o canal de controle. Proteger o controle não protege automaticamente a conexão de dados. Para solicitar TLS nos dados, o cliente envia `PBSZ 0` e depois **`PROT P`**; `PROT C` deixa a conexão de dados em claro.

No uso chamado **FTPS implícito**, TLS começa imediatamente ao abrir a conexão, sem `AUTH TLS`. A IANA registra **990/TCP** para o controle FTPS e **989/TCP** para dados FTPS. Essa modalidade é uma convenção distinta do mecanismo explícito do RFC 4217 e não elimina a arquitetura de canais separados.

Nos modos ativo e passivo, a conexão de dados pode usar portas negociadas. Assim, nem `PROT P` significa “uma única conexão”, nem a existência do registro 989 permite afirmar que toda transferência FTPS usa necessariamente essa porta. Política do servidor, modo ativo/passivo, regras de firewall e validação de certificado continuam relevantes.

#### 7.3 SFTP

SFTP é o **SSH File Transfer Protocol**, executado como subsistema ou protocolo sobre um transporte SSH criptografado, normalmente na porta **22/TCP**.

Regra essencial:

> SFTP não é FTP sobre TLS.

SFTP e FTP são protocolos distintos. SFTP costuma usar um único transporte SSH e pode aproveitar autenticação por senha, chave pública e demais recursos do SSH.

#### 7.4 SSH

SSH oferece administração remota protegida, autenticação, integridade, confidencialidade, execução de comandos e encaminhamento de portas. Porta padrão: **22/TCP**.

O uso seguro depende de configuração: validação da chave do host, proteção de chaves privadas, algoritmos atuais, limitação de acesso e autenticação forte.

#### 7.5 Telnet

Telnet oferece terminal remoto, mas não fornece a proteção criptográfica esperada para credenciais e conteúdo. Porta padrão: **23/TCP**. Em redes modernas, SSH deve ser preferido para administração. Telnet pode aparecer em laboratório ou teste controlado de conectividade, sem ser opção adequada para administração sensível.

<a id="s2-d3-snmp"></a>
### 8. SNMP — gerenciamento e monitoramento

SNMP organiza a comunicação entre:

- **gerente:** sistema que consulta e recebe eventos;
- **agente:** software no equipamento monitorado;
- **MIB:** estrutura lógica de objetos gerenciados;
- **OID:** identificador de um objeto.

Operações típicas:

- GET e GETNEXT/GETBULK para leitura;
- SET para alteração autorizada;
- TRAP para notificação sem confirmação no modelo clássico;
- INFORM para notificação com confirmação no protocolo que a suporta.

Portas tradicionais:

- **161/UDP:** consultas e respostas ao agente;
- **162/UDP:** traps e informs recebidos pelo gerente.

SNMPv1 e SNMPv2c usam community strings e não oferecem proteção equivalente à do SNMPv3. SNMPv3 pode fornecer autenticação e privacidade, conforme nível e configuração. “Usar SNMPv3” não basta se credenciais, chaves e permissões forem fracas.

<a id="s2-d3-ldap"></a>
### 9. LDAP — acesso a diretórios

LDAP é um protocolo para acessar serviços de diretório. Um diretório organiza entradas hierarquicamente, com:

- **DN:** nome distinto que identifica a entrada;
- atributos, como nome, e-mail e unidade;
- operações como bind, search, add, modify e delete.

Portas mais cobradas:

- **389/TCP:** LDAP, podendo iniciar TLS por STARTTLS;
- **636/TCP:** LDAP com TLS implícito, usualmente chamado LDAPS.

LDAP não é sinônimo de banco relacional. Também não é, isoladamente, “o sistema de autenticação”: ele pode armazenar identidades e participar de um fluxo de autenticação, mas autorização, política, sessão e aplicação envolvem outras camadas.

<a id="s2-d3-proxy"></a>
### 10. Proxy direto e proxy reverso

#### 10.1 Proxy direto

O proxy direto atua em nome do cliente. Pode:

- aplicar política de navegação;
- autenticar usuários;
- registrar acessos;
- filtrar conteúdo;
- armazenar cache;
- ocultar do servidor a conexão direta do cliente, conforme arquitetura.

Ele pode ser configurado explicitamente no cliente ou inserido pela arquitetura de rede. Usar proxy não assegura anonimato: cabeçalhos, autenticação, logs e outros metadados podem identificar o cliente.

#### 10.2 Proxy reverso

O proxy reverso fica diante dos servidores e recebe conexões em nome deles. Pode:

- distribuir carga;
- terminar TLS;
- fazer cache;
- ocultar a topologia interna;
- aplicar controles como limitação de taxa ou firewall de aplicação.

“Direto” e “reverso” descrevem o papel lógico visto pelos extremos, não um conjunto obrigatório de funções. Muitos proxies terminam ou compreendem um protocolo de aplicação; outros apenas retransmitem bytes ou criam túneis, como pode ocorrer com HTTP `CONNECT`, sem enxergar o conteúdo protegido ponta a ponta.

Proxy não é sinônimo de NAT. Em geral, o proxy estabelece ou intermedeia comunicação em nome de um extremo, enquanto NAT traduz campos de endereçamento no tráfego encaminhado sem terminar a sessão de aplicação. A diferença deve ser usada como modelo conceitual, não como afirmação de que todo proxy sempre inspeciona semanticamente a aplicação.

<a id="s2-d3-nat-pat"></a>
### 11. NAT básico e PAT/NAPT

**NAT** é o nome geral da tradução entre espaços de endereçamento. Na terminologia do RFC 2663, o NAT tradicional possui duas variantes que a prova pode contrastar:

- **NAT básico:** traduz endereços IP entre os domínios, sem traduzir os identificadores de transporte. Pode usar associação estática, previsível, ou alocação dinâmica a partir de um conjunto de endereços externos;
- **NAPT — Network Address Port Translation:** estende a tradução aos identificadores de transporte, como portas TCP/UDP. Isso permite multiplexar fluxos de vários hosts em um único endereço externo.

**PAT** é o nome corrente para essa tradução de endereços e portas, frequentemente chamada de NAPT ou sobrecarga de NAT. No uso cotidiano, “NAT” muitas vezes é empregado como termo guarda-chuva inclusive para PAT; quando a banca opuser os conceitos, a diferença decisiva é **somente endereço no NAT básico** versus **endereço e porta no PAT/NAPT**.

Exemplo de tabela PAT/NAPT:

| Origem interna | Origem pública traduzida | Destino |
|---|---|---|
| 10.0.10.25:51500 | 203.0.113.10:40001 | 198.51.100.20:443 |
| 10.0.10.30:51500 | 203.0.113.10:40002 | 198.51.100.20:443 |

As portas públicas diferentes permitem devolver cada resposta ao host correto.

NAT/PAT:

- não criptografa o tráfego;
- não substitui firewall;
- não autentica usuários;
- não resolve nomes;
- pode dificultar conexões recebidas sem mapeamento, mas isso não deve ser tratado como garantia absoluta de segurança.

<a id="s2-d3-ntp"></a>
### 12. NTP — sincronização de tempo

NTP sincroniza relógios em rede. Porta padrão: **123/UDP**.

O protocolo usa uma hierarquia de fontes de tempo, frequentemente descrita por estratos. Estrato menor indica proximidade lógica de uma fonte de referência; não significa automaticamente “servidor mais seguro”.

Tempo coerente é especialmente importante para:

- correlação de logs;
- validade de certificados;
- autenticação dependente de horário;
- auditoria;
- investigação de incidentes;
- ordenação de eventos distribuídos.

NTP não define o fuso horário apresentado ao usuário. Ele sincroniza uma referência temporal; fuso e horário de verão são tratados por configuração local.

Fontes NTP devem ser selecionadas e protegidas. Respostas falsas ou grandes desvios podem prejudicar autenticação e análise de eventos.

<a id="s2-d3-portas"></a>
### 13. Portas conhecidas mais cobradas

| Serviço | Porta padrão mais cobrada | Transporte típico | Observação de prova |
|---|---:|---|---|
| HTTP | 80 | TCP | HTTP/3 é exceção sobre QUIC/UDP |
| HTTPS | 443 | TCP; UDP no HTTP/3 | HTTPS é HTTP protegido por TLS |
| DNS clássico | 53 | UDP e TCP | formas encapsuladas, como DoT/DoH, usam outros transportes/portas |
| DHCP servidor | 67 | UDP | recebe pedidos de clientes/relays |
| DHCP cliente | 68 | UDP | recebe configuração |
| SMTP relay | 25 | TCP | transferência entre servidores |
| SMTP submission | 587 | TCP | submissão do cliente |
| Submission TLS implícito | 465 | TCP | não chamar genericamente de relay SMTP |
| POP3 | 110 | TCP | acesso à caixa |
| POP3S | 995 | TCP | TLS implícito |
| IMAP | 143 | TCP | sincronização da caixa |
| IMAPS | 993 | TCP | TLS implícito |
| FTP controle | 21 | TCP | dados usam conexão separada |
| FTP dados ativo | 20 | TCP | passivo usa porta informada pelo servidor |
| FTPS explícito | 21 | TCP | `AUTH TLS`; dados exigem `PBSZ 0` + `PROT P` para TLS |
| FTPS implícito (controle) | 990 | TCP | TLS desde a abertura; convenção distinta do RFC 4217 |
| FTPS implícito (dados) | 989 | TCP | porta registrada; ativo/passivo pode negociar outras portas |
| SSH/SFTP | 22 | TCP | SFTP opera sobre SSH |
| Telnet | 23 | TCP | sem proteção criptográfica adequada |
| SNMP agente | 161 | UDP | consultas e respostas |
| SNMP notificações | 162 | UDP | traps/informs |
| LDAP | 389 | TCP | pode usar STARTTLS |
| LDAPS | 636 | TCP | TLS implícito |
| NTP | 123 | UDP | sincronização de relógio |

<a id="s2-d3-fluxo-integrado"></a>
### 14. Fluxo integrado de acesso a um portal

Considere uma estação do CRA-PR recém-conectada:

1. DHCP entrega IP, prefixo, gateway e servidor DNS.
2. O usuário informa o nome do portal.
3. O stub resolver consulta o resolvedor DNS.
4. O resolvedor usa cache ou percorre a hierarquia até obter A/AAAA.
5. A estação encaminha pacotes ao gateway quando o destino não está na rede local.
6. PAT pode trocar IP e porta privados por IP e porta públicos.
7. Para HTTPS tradicional, o cliente abre TCP para 443.
8. TLS negocia o canal e valida o certificado apresentado.
9. HTTP trafega protegido dentro do TLS.
10. Proxy reverso pode encaminhar a requisição a um servidor de aplicação.
11. NTP ajuda a manter relógios coerentes para certificado e logs.

Esse fluxo mostra por que “a internet caiu” é diagnóstico insuficiente. A falha pode estar em configuração DHCP, DNS, rota, NAT/PAT, transporte, TLS, proxy ou aplicação.

## Exemplos práticos e resolvidos

### Exemplo resolvido 1 — Nome não resolve, mas o IP responde

**Cenário:** a estação alcança 198.51.100.40, mas não abre portal.example.

**Raciocínio:**

1. A conectividade IP até o destino existe.
2. A falha aparece quando um nome precisa ser convertido.
3. O primeiro foco é DNS: servidor configurado, resposta, cache e registros.
4. Alterar a porta HTTPS não corrige uma resolução DNS ausente.

**Conclusão:** o sintoma aponta prioritariamente para DNS, sem provar que o servidor autoritativo é a única causa possível.

### Exemplo resolvido 2 — Concessão DHCP entre VLANs

**Cenário:** clientes da VLAN 20 não recebem endereços; o servidor DHCP está na VLAN 10.

**Raciocínio:**

1. Broadcast local não atravessa roteadores por padrão.
2. Um relay na interface da VLAN 20 pode encaminhar as mensagens ao servidor.
3. O servidor deve possuir escopo compatível com a VLAN 20.
4. A resposta retorna pelo relay ao cliente.

**Conclusão:** servidor central é possível, mas exige relay, roteamento e escopo corretos.

### Exemplo resolvido 3 — Dois usuários compartilham um IP público

**Cenário:** 10.10.1.11:52000 e 10.10.1.12:52000 acessam o mesmo site.

**Resolução:** o PAT pode traduzir os fluxos para 203.0.113.8:41001 e 203.0.113.8:41002. A tabela associa cada retorno ao host privado correto. A porta de origem externa não precisa ser igual à interna.

### Exemplo resolvido 4 — Escolha de transferência segura

**Cenário:** uma rotina precisa transferir arquivos e já existe infraestrutura SSH com autenticação por chave.

**Resolução:** SFTP é coerente porque opera sobre SSH e pode reutilizar autenticação por chave. FTPS também pode proteger FTP por TLS, mas é outra solução, com arquitetura de controle/dados do FTP. A escolha não deve ser descrita como “SFTP é FTP sobre TLS”.

### Exemplo resolvido 5 — Envio e leitura de mensagem

**Cenário:** um usuário envia uma mensagem e depois a lê no telefone e no notebook, mantendo pastas sincronizadas.

**Resolução:** SMTP cuida da submissão/transferência; IMAP mantém caixa e estado no servidor para múltiplos clientes. POP3 não é protocolo de envio.

### Exemplo resolvido 6 — Monitoramento sem proteção adequada

**Cenário:** switches respondem a consultas SNMPv2c usando community padrão.

**Resolução:** há risco de leitura ou alteração indevida, conforme permissões e exposição. A medida adequada inclui restringir origem, trocar credenciais, aplicar menor privilégio e, quando suportado, usar SNMPv3 com autenticação e privacidade. O simples bloqueio externo não corrige exposição dentro da rede.

## Diferenças entre conceitos parecidos

| Conceito 1 | Conceito 2 | Diferença decisiva |
|---|---|---|
| TCP | UDP | TCP oferece fluxo ordenado e confiável; UDP entrega datagramas sem essas garantias nativas |
| HTTP | HTTPS | HTTPS é HTTP em canal TLS |
| DNS | DHCP | DNS resolve nomes/dados; DHCP entrega configuração de rede |
| SMTP | POP3/IMAP | SMTP envia/transfere; POP3 e IMAP acessam caixa postal |
| POP3 | IMAP | POP3 tem acesso mais simples/download; IMAP sincroniza estado no servidor |
| FTP | FTPS | FTPS preserva os canais FTP e negocia TLS; no explícito, dados protegidos requerem `PROT P` |
| FTP | SFTP | SFTP é protocolo de arquivos sobre SSH, não uma variação TLS do FTP |
| SSH | Telnet | SSH protege e autentica o canal; Telnet clássico transmite sem essa proteção |
| SNMP polling | SNMP trap | polling parte do gerente; trap é notificação iniciada pelo agente |
| LDAP | banco relacional | LDAP acessa diretório hierárquico; SQL trabalha com modelo relacional |
| proxy direto | proxy reverso | o direto representa clientes; o reverso representa servidores |
| proxy | NAT | proxy atua em nome de um extremo; NAT traduz cabeçalhos sem terminar a sessão de aplicação |
| NAT básico | PAT/NAPT | NAT básico traduz endereço; PAT/NAPT também traduz portas para multiplexar fluxos |
| NTP | fuso horário | NTP sincroniza referência de tempo; fuso define exibição local |
| porta conhecida | protocolo efetivo | porta sugere convenção, mas não comprova conteúdo nem segurança |

<a id="s2-d3-revisao-fixa"></a>
## Revisão fixa do Dia 3

Este bloco fornece a base teórica das **15 questões extras de Legislação CRA/CFA** e das **5 questões extras de Língua Portuguesa** do Dia 3. Os identificadores e os títulos abaixo são estáveis: os comentários das questões devem citar o título da seção e, quando útil, o respectivo identificador.

**Revisão da Semana 1:** associação entre as quatro normas do edital, distinção CFA × CRA-PR, noções gerais de registro, fiscalização, deveres, infrações e leitura de conectores.

**Aprofundamento da Semana 2:** literalidade orientada dos artigos indicados, separação entre dever e direito, delimitação subjetiva do Código de Ética, aplicação em casos concretos e regras gramaticais necessárias às cinco extras.

<a id="s2-d3-rf-topicos"></a>
### Tópicos estudados

- Lei nº 4.769/1965: campo profissional, estrutura CFA/CRAs, competências e registro;
- Decreto nº 61.934/1967: detalhamento das atividades, documentos profissionais, exercício e fiscalização;
- Regimento do CRA-PR, aprovado pela RN CFA nº 651/2024: natureza, finalidade, jurisdição e posição do Plenário;
- Código de Ética e Disciplina, aprovado pela RN CFA nº 671/2025: sujeitos alcançados, deveres, direitos, infrações e noções de sanção;
- Português: conectores, referência pronominal, concordância com verbos impessoais, crase e pontuação.

<a id="s2-d3-rf-escopo"></a>
### Delimitação obrigatória do escopo

As 15 extras de Legislação do Dia 3 devem ser respondidas somente com estas quatro bases:

1. Lei nº 4.769/1965 e suas alterações;
2. Decreto nº 61.934/1967 e suas alterações;
3. Regimento Interno do CRA-PR, aprovado pela RN CFA nº 651/2024;
4. Código de Ética e Disciplina, aprovado pela RN CFA nº 671/2025.

A **Lei nº 12.514/2011** e as **RNs CFA nº 589/2020, nº 649/2024 e nº 670/2025** pertencem a outros recortes normativos. Podem ser lembradas apenas como contexto externo de contribuições, fiscalização ou registro, mas estão **fora do escopo autônomo do cargo de Analista de Sistemas adotado nesta semana**. Nenhuma questão extra do Dia 3 deve depender de artigo, prazo, requisito ou procedimento dessas normas.

Também não se deve usar a RN CFA nº 640/2024 como Código vigente para este concurso: a Retificação I indica a RN CFA nº 671/2025, que revogou expressamente a nº 640/2024.

<a id="s2-d3-rf-resumo"></a>
<a id="s2-d3-revisao-legislacao"></a>
### Resumo teórico: como as quatro normas se relacionam

| Base | Função no estudo | Pergunta de controle |
|---|---|---|
| Lei nº 4.769/1965 | disciplina o exercício profissional e estrutura o CFA e os CRAs | quem exerce, qual é o campo e o que compete a cada conselho? |
| Decreto nº 61.934/1967 | regulamenta a Lei e detalha sua execução | como a atividade, os documentos, o registro e a fiscalização se operacionalizam? |
| Regimento/RN CFA nº 651/2024 | organiza o CRA-PR | qual órgão regional decide, executa ou atende e qual é sua jurisdição? |
| Código/RN CFA nº 671/2025 | disciplina conduta ética e sanções | quem é alcançado e qual conduta é dever, direito ou infração? |

O decreto regulamenta a lei; não a substitui nem pode contrariá-la. O Regimento organiza internamente o CRA-PR, mas não cria competência nacional. O Código disciplina conduta ética dentro de seu âmbito subjetivo e material; ele não transforma toda conduta de qualquer trabalhador de TI em infração profissional.

O texto oficial consolidado da Lei e do Decreto ainda contém, em alguns dispositivos, a denominação histórica “Técnico de Administração”. Nas questões, associe esses dispositivos às denominações atuais do profissional e do Sistema CFA/CRAs, sem alterar o conteúdo da regra.

<a id="s2-d3-rf-lei-4769"></a>
### Lei nº 4.769/1965: campo, sistema, competências e registro

**Revisão da Semana 1:** a Lei é a base do exercício da profissão e da estrutura CFA/CRAs.

**Aprofundamento da Semana 2 — artigos relevantes:**

- **Art. 2º:** inclui pareceres, relatórios, planos, projetos, arbitragens, laudos, assessoria em geral, **chefia intermediária e direção superior**, além de pesquisa, estudo, análise, planejamento, implantação, coordenação e controle nos campos da Administração. A lista não se reduz a uma única área funcional.
- **Arts. 3º e 4º:** tratam da habilitação para o exercício e da apresentação do diploma para o provimento e o exercício de **cargo técnico de Administração** na Administração Pública abrangida pela Lei, preservadas as situações ressalvadas pelo próprio texto. O § 2º do art. 4º deixa claro que apresentar diploma **não dispensa concurso**, quando ele for exigido.
- **Art. 6º:** o Conselho Federal e os Conselhos Regionais constituem, em conjunto, autarquia com personalidade jurídica de direito público e autonomia técnica, administrativa e financeira.
- **Art. 7º:** atribui ao CFA, entre outros pontos, orientar e disciplinar o exercício profissional, dirimir dúvidas suscitadas nos Regionais, **examinar, modificar e aprovar** os regimentos internos dos Regionais, julgar em última instância os recursos de penalidades e **votar e alterar** o Código de Deontologia Administrativa, zelando por sua fiel execução e ouvindo os CRAs.
- **Art. 8º:** atribui aos CRAs executar as diretrizes do CFA, fiscalizar na respectiva jurisdição, manter registros, julgar infrações e impor penalidades legais, expedir carteiras e elaborar o regimento regional para exame e aprovação pelo CFA.
- **Art. 14:** exige registro para o exercício profissional; a falta torna o exercício ilegal e punível. A carteira expedida pelo Regional prova o exercício profissional, serve como identidade e tem fé em todo o território nacional.
- **Art. 15:** prevê registro obrigatório das empresas, entidades e escritórios técnicos que explorem as atividades profissionais enunciadas na Lei.
- **Art. 16:** prevê, no catálogo legal, multa de 5% a 50% do maior salário-mínimo vigente no País ao infrator de qualquer artigo; suspensão de seis meses a um ano ao profissional que demonstrar incapacidade técnica no exercício da profissão, assegurada ampla defesa; e suspensão de um a cinco anos ao profissional que, no âmbito de sua atuação, for responsável, na parte técnica, por falsidade de documento ou por dolo em parecer ou outro documento que assinar. Pelo § 2º, a reincidência **da mesma infração**, praticada dentro de cinco anos após a primeira, acarreta multa em dobro e cancelamento do registro profissional. Não confunda esse catálogo da Lei com a gradação ético-disciplinar específica da RN CFA nº 671/2025.

#### CFA × CRA-PR

| Situação | CFA | CRA-PR |
|---|---|---|
| alcance | nacional/sistêmico | regional, no Paraná |
| diretrizes | formula e uniformiza | executa na jurisdição |
| regimento regional | examina, modifica e aprova | elabora e submete |
| penalidade regional | julga recurso em última instância, nos termos legais | julga a infração em sua esfera e aplica a penalidade cabível |
| registro e carteira | disciplina o sistema | mantém registro e expede carteira ao inscrito de sua jurisdição |

<a id="s2-d3-rf-decreto-61934"></a>
### Decreto nº 61.934/1967: execução da Lei

**Revisão da Semana 1:** o Decreto regulamenta a Lei nº 4.769/1965.

**Aprofundamento da Semana 2 — artigos relevantes:**

- **Art. 3º:** detalha as atividades profissionais, incluindo elaboração de documentos técnicos, pesquisa, planejamento, implantação, coordenação e controle, funções e cargos técnicos, chefia, direção, assessoramento, consultoria e magistério nas matérias do campo profissional.
- **Art. 4º e parágrafo único:** exige a habilitação prevista para o provimento e o exercício de **cargo técnico de Administração**, mas a apresentação do diploma não dispensa concurso quando a lei o exigir.
- **Art. 6º e parágrafo único:** os documentos referentes à ação profissional indicada no art. 3º devem ser elaborados e assinados por profissional devidamente registrado, salvo no caso de exercício de cargo público; depois da assinatura, é obrigatória a citação do número de registro no CRA.
- **Art. 7º:** autoridades federais, estaduais e municipais e empresas privadas devem exigir a assinatura do profissional devidamente registrado nos documentos mencionados no art. 3º, exceto quando se tratar de documento oficial assinado pelo ocupante do respectivo cargo público.
- **Art. 9º:** para o exercício profissional, exige a apresentação da Carteira de Identidade Profissional expedida pelo CRA juntamente com prova de que o profissional está em pleno gozo de seus direitos sociais.
- **Art. 10:** a falta de registro torna ilegal e punível o exercício da profissão.
- **Art. 11:** a fiscalização cabe ao CRA competente e ao CFA, aos quais incumbem a orientação e a disciplina do exercício profissional em todo o território nacional.
- **Art. 39:** reproduz, no plano regulamentar, o núcleo regional: executar diretrizes, fiscalizar, manter registro, julgar infrações, aplicar penalidades, expedir carteiras e elaborar regimento para aprovação federal.

**Diferença importante:** diploma comprova formação; registro habilita o exercício profissional sujeito ao Conselho; carteira identifica o profissional registrado; concurso é o procedimento de provimento quando exigido. Um elemento não substitui automaticamente o outro.

<a id="s2-d3-rf-regimento-651"></a>
### Regimento do CRA-PR: natureza, jurisdição e Plenário

**Revisão da Semana 1:** a RN CFA nº 651/2024 aprova o Regimento do CRA-PR; ela não é o Código de Ética.

**Aprofundamento da Semana 2 — artigos relevantes:**

- **Art. 1º:** caracteriza o CRA-PR como autarquia de direito público, com autonomia técnica, administrativa e financeira, sede na capital do Paraná. Suas finalidades incluem executar diretrizes do CFA, fiscalizar, manter registros, julgar infrações, impor penalidades, expedir carteiras e submeter seu Regimento ao CFA.
- **Art. 2º:** fixa jurisdição em todo o estado do Paraná, nas matérias de sua competência.
- **Art. 3º:** enumera Plenário, Diretoria Executiva, Ouvidoria, Comissões Permanentes e Especiais e Grupos de Trabalho, além dos Órgãos de Representação.
- **Art. 4º:** define o Plenário como órgão colegiado de deliberação superior e primeira instância de julgamento no âmbito da jurisdição regional.

Autonomia regional não significa soberania nem independência normativa absoluta. O CRA-PR continua inserido no Sistema CFA/CRAs, executa diretrizes federais e submete seu Regimento ao CFA.

<a id="s2-d3-rf-etica-671"></a>
### Código de Ética/RN CFA nº 671/2025: sujeitos, deveres, direitos e infrações

**Revisão da Semana 1:** zelo, honestidade, sigilo, independência técnica, vedação ao uso de registro de fachada e possibilidade de incidência sobre pessoa jurídica.

**Aprofundamento da Semana 2 — artigos relevantes:**

- **Art. 4º, § 1º:** empregado, profissional liberal, servidor ou empregado público não abdica de dignidade, prerrogativas e independência profissional.
- **Art. 4º, § 2º:** o Código aplica-se às pessoas físicas e jurídicas registradas no CRA da respectiva jurisdição, no exercício das atividades abrangidas pela Lei nº 4.769/1965 e pelo Decreto nº 61.934/1967, observadas as especificidades da pessoa jurídica.
- **Art. 4º, § 3º:** o exercício de mandato eletivo no CFA ou nos CRAs também é atividade profissional para fins do Código.
- **Art. 5º:** deveres incluem zelo, dedicação, comprometimento, responsabilidade e honestidade; defesa dos interesses de quem recebe o serviço; sigilo sobre o conhecido em razão do exercício profissional lícito; independência técnica; aperfeiçoamento; zelo pela reputação; e comunicação **imediata** ao CRA da mudança de domicílio ou endereço, inclusive eletrônico, do profissional e da pessoa jurídica sob sua responsabilidade técnica, bem como de outros fatos necessários ao controle e à fiscalização profissional.
- **Art. 6º:** infrações incluem assinar documento de terceiro sem orientação ou supervisão; publicar trabalho de que não participou; violar sigilo sem justa causa; dificultar fiscalização; permitir uso do nome ou registro onde não atua; facilitar exercício a não habilitado; praticar, **no exercício da atividade profissional**, assédio moral ou sexual; exercer a profissão com comprovada incapacidade técnica em serviço de Administração para o qual não esteja capacitado, colocando em risco o **patrimônio de terceiros**; obter vantagem por artifício enganoso; agir de má-fé com potencial de dano; usar posição no Sistema para proveito pessoal; praticar, **no exercício da atividade profissional**, ato contrário à lei ou destinado a fraudá-la, ou contribuir para ilícito penal; e exercer a profissão durante suspensão.
- **Art. 7º:** direitos incluem exercício sem discriminação; apontar falhas em regulamentos e normas das instituições quando consideradas indignas do exercício profissional ou prejudiciais ao cliente ou ao prestador de serviço, dirigindo-se nesse caso ao Sistema CFA/CRAs; exigir justa remuneração; recusar condições degradantes; participar de eventos; e competir honestamente, com proteção da propriedade intelectual.
- **Arts. 13, 18, 22 e 23:** reconhecem advertência escrita e reservada, censura pública, suspensão e cancelamento; as sanções vêm acompanhadas de multa segundo o art. 18. Para pessoa física, o art. 22 torna o cancelamento aplicável ao exercício durante suspensão e à reincidência ali definida, sempre depois do trânsito em julgado administrativo exigido pelo art. 23. Suspensão e cancelamento não se aplicam à pessoa jurídica.

#### Dever × direito × infração

| Categoria | Pergunta para reconhecer | Exemplo |
|---|---|---|
| dever | o Código manda agir ou preservar algo? | guardar sigilo e manter independência técnica |
| direito | o Código protege uma faculdade ou prerrogativa? | recusar condições degradantes e exigir remuneração justa |
| infração | o Código proíbe ou tipifica uma conduta? | ceder o registro, dificultar fiscalização ou assinar trabalho alheio |
| sanção | é consequência apurada em processo? | advertência, censura, suspensão ou cancelamento, conforme o caso |

Sigilo não é absoluto: o art. 6º tipifica a violação **sem justa causa**. Independência técnica também não autoriza desobediência arbitrária; ela impede que vínculo de emprego ou pressão comercial elimine a responsabilidade profissional.

<a id="s2-d3-rf-diferencas"></a>
### Diferenças entre conceitos próximos

| Conceitos | Distinção correta |
|---|---|
| Lei × Decreto | a Lei estrutura e disciplina; o Decreto regulamenta sua execução |
| CFA × CRA-PR | direção sistêmica/nacional × execução e fiscalização regional |
| autonomia × soberania | capacidade técnica, administrativa e financeira × inexistência de subordinação normativa; o CRA possui a primeira, não a segunda |
| diploma × registro | formação acadêmica × habilitação perante o Conselho para o exercício sujeito a registro |
| registro × carteira | inscrição/habilitação × documento expedido ao inscrito |
| regimento × código de ética | organização interna do CRA-PR × conduta, infrações e sanções ético-disciplinares |
| dever × direito | obrigação de conduta × prerrogativa protegida |
| infração × sanção | conduta tipificada × consequência definida após o processo |
| pessoa física × pessoa jurídica | ambas podem estar no âmbito do Código, mas as especificidades da PJ impedem suspensão do exercício e cancelamento como sanções éticas |

<a id="s2-d3-rf-exemplos"></a>
### Exemplos resolvidos

**Exemplo 1 — competência institucional.** O CRA-PR elabora proposta de alteração de seu Regimento e afirma que a mudança dispensa exame do CFA porque o Regional possui autonomia administrativa. A conclusão está errada: autonomia não elimina a regra legal e regimental de submissão do Regimento ao CFA.

**Exemplo 2 — diploma e concurso.** Um candidato apresenta diploma exigido para cargo técnico de Administração e sustenta estar dispensado do concurso. A conclusão está errada: a Lei nº 4.769/1965, art. 4º, § 2º, e o Decreto nº 61.934/1967, art. 4º, parágrafo único, preservam a exigência de concurso quando prevista.

**Exemplo 3 — documento técnico.** Um profissional apenas empresta a assinatura para relatório elaborado por terceiro, sem orientação nem supervisão. A conduta configura a infração do art. 6º, III, do Código. Esse fato, sozinho, não permite afirmar violação dos arts. 6º e 7º do Decreto sem saber se o documento foi elaborado e assinado por profissional registrado e se incide alguma ressalva relativa a cargo público.

**Exemplo 4 — acesso privilegiado em TI.** Pessoa registrada, no exercício de atividade abrangida, consulta dados sigilosos obtidos profissionalmente e os divulga por conveniência comercial. O caso envolve o dever de sigilo do art. 5º e a infração de violação sem justa causa do art. 6º.

**Exemplo 5 — pessoa jurídica.** Uma pessoa jurídica registrada está sujeita aos deveres e às infrações compatíveis com sua natureza. Isso não permite aplicar-lhe suspensão do exercício profissional nem cancelamento como sanções éticas, vedados pelo art. 13, § 3º.

<a id="s2-d3-rf-portugues"></a>
<a id="s2-d3-revisao-portugues"></a>
### Língua Portuguesa — base das 5 questões extras

**Revisão da Semana 1:** interpretação objetiva, conectores, concordância, crase e pontuação.

**Aprofundamento da Semana 2:** aplicação das regras a enunciados normativos e técnicos, com atenção ao alcance de palavras e à manutenção do sentido em reescritas.

#### 1. Conectores e relação lógica

- `mas`, `porém`, `contudo`: oposição ou ressalva;
- `portanto`, `logo`, `assim`: conclusão;
- `porque`, `visto que`, `uma vez que`: causa ou explicação, conforme o contexto;
- `embora`, `ainda que`: concessão;
- `se`, `caso`, `desde que`: condição;
- `para que`, `a fim de que`: finalidade.

Em “O CRA-PR possui autonomia administrativa, **mas** deve submeter o Regimento ao CFA”, `mas` opõe a conclusão indevida de independência absoluta. Substituí-lo por `portanto` inverteria a relação lógica.

#### 2. Referência e ambiguidade

Pronome deve ter antecedente identificável. Em “O diretor entregou ao conselheiro seu relatório”, `seu` pode retomar o diretor ou o conselheiro. A reescrita precisa explicitar: “o relatório do diretor” ou “o relatório do conselheiro”.

Não atribua automaticamente ao termo mais próximo aquilo que a coerência e a gramática não autorizam. Em texto normativo, identifique o sujeito de cada verbo e o referente de `ele`, `isso`, `tal medida`, `respectivo` e `cujo`.

#### 3. `haver`, `existir` e concordância

- `haver` com sentido de existir é impessoal e fica no singular: “**Havia** três infrações no relatório.”
- `existir` é pessoal e concorda com o sujeito: “**Existiam** três infrações no relatório.”
- em locução com `haver` impessoal, o auxiliar também fica no singular: “**Deve haver** providências.”
- `fazer` indicando tempo decorrido também é impessoal: “**Faz** dois anos que o processo começou.”

#### 4. Crase

Crase exige a fusão da preposição `a` com artigo ou pronome iniciado por `a`.

- “encaminhou a manifestação **à Ouvidoria**”: quem encaminha, encaminha algo `a`; `Ouvidoria` admite artigo `a`;
- “começou **a analisar**”: não há crase antes de verbo;
- “referiu-se **àquela** decisão”: preposição `a` + `aquela`;
- “submeteu o Regimento **ao CFA**”: a forma é masculina, sem crase.

Teste prático: troque o termo feminino por masculino. Se surgir `ao`, normalmente haverá `à` no feminino: “dirigiu-se ao Plenário” → “dirigiu-se à Ouvidoria”.

#### 5. Pontuação

- não se separa sujeito de verbo: “Os membros do Plenário deliberaram”, sem vírgula depois de `Plenário`;
- aposto explicativo fica isolado: “O Plenário, órgão de deliberação superior, decidiu”;
- oração adverbial deslocada costuma ser separada: “Embora haja autonomia, o Regimento é submetido ao CFA”;
- a vírgula antes de `mas` separa orações coordenadas: “O CRA executa as diretrizes, mas não possui jurisdição nacional.”

<a id="s2-d3-rf-pegadinhas"></a>
### Pegadinhas do Dia 3

1. Transformar o CRA-PR em órgão de jurisdição nacional.
2. Tratar a autonomia regional como independência normativa absoluta.
3. Dizer que o Decreto substitui ou revoga a Lei que regulamenta.
4. Confundir diploma, registro, carteira e concurso.
5. Atribuir ao CFA a expedição ordinária da carteira regional ou ao CRA a aprovação final de seu próprio Regimento.
6. Usar RN CFA nº 649/2024, nº 670/2025, nº 589/2020 ou Lei nº 12.514/2011 como fundamento autônomo das extras do Analista.
7. Usar a RN CFA nº 640/2024 em lugar da nº 671/2025.
8. Afirmar que o Código alcança toda pessoa que trabalha com TI, independentemente de registro e de atividade abrangida.
9. Confundir um dever ético com um direito ou uma infração com a sanção.
10. Dizer que pessoa jurídica está fora do Código ou, no extremo oposto, aplicar-lhe suspensão/cancelamento éticos.
11. Tornar o sigilo absoluto, apagando a expressão normativa “sem justa causa”.
12. Trocar `mas` por `portanto` e alegar preservação de sentido.
13. Flexionar `haver` impessoal: “haviam infrações”.
14. Inserir crase antes de verbo ou separar sujeito e verbo por vírgula.

<a id="s2-d3-rf-tabela"></a>
### Tabela de revisão rápida da revisão fixa do Dia 3

| ID de cobertura | Disciplina | Assunto cobrível | Regra-chave | Seção-base | Origem |
|---|---|---|---|---|---|
| D3-LEG-01 | Legislação | função e hierarquia das quatro bases | Lei estrutura; Decreto regulamenta; Regimento organiza; Código disciplina ética | `s2-d3-rf-resumo` | revisão S1 + aprofundamento S2 |
| D3-LEG-02 | Legislação | atividades profissionais | art. 2º da Lei: assessoria em geral, chefia intermediária, direção superior, documentos, pesquisa, planejamento e controle | `s2-d3-rf-lei-4769` | aprofundamento S2 |
| D3-LEG-03 | Legislação | habilitação, diploma e concurso | diploma não dispensa concurso quando exigido | `s2-d3-rf-lei-4769` | aprofundamento S2 |
| D3-LEG-04 | Legislação | natureza do Sistema | CFA e CRAs constituem autarquia de direito público com autonomia | `s2-d3-rf-lei-4769` | revisão S1 + artigo S2 |
| D3-LEG-05 | Legislação | competências do CFA | orientar; examinar, modificar e aprovar regimentos; votar e alterar o Código; julgar recursos | `s2-d3-rf-lei-4769` | aprofundamento S2 |
| D3-LEG-06 | Legislação | competências dos CRAs | execução, fiscalização, registro, julgamento e carteira | `s2-d3-rf-lei-4769` | revisão S1 + artigo S2 |
| D3-LEG-07 | Legislação | registro e carteira | registro habilita; carteira prova o exercício e identifica | `s2-d3-rf-lei-4769` | aprofundamento S2 |
| D3-LEG-08 | Legislação | pessoa jurídica e penalidade legal | art. 15 prevê registro; art. 16 traz multa, suspensões e reincidência da mesma infração em cinco anos | `s2-d3-rf-lei-4769` | aprofundamento S2 |
| D3-LEG-09 | Legislação | detalhamento da atividade | art. 3º do Decreto operacionaliza o campo profissional | `s2-d3-rf-decreto-61934` | aprofundamento S2 |
| D3-LEG-10 | Legislação | documento e assinatura | art. 6º: elaboração/assinatura por registrado e número do registro; art. 7º: exigência e ressalva do documento oficial | `s2-d3-rf-decreto-61934` | aprofundamento S2 |
| D3-LEG-11 | Legislação | exercício e fiscalização | carteira + pleno gozo dos direitos sociais; fiscalização pelo CRA competente e pelo CFA | `s2-d3-rf-decreto-61934` | aprofundamento S2 |
| D3-LEG-12 | Legislação | natureza e jurisdição do CRA-PR | autarquia, sede na capital e jurisdição estadual | `s2-d3-rf-regimento-651` | revisão S1 + artigo S2 |
| D3-LEG-13 | Legislação | âmbito do Código | PF/PJ registradas em atividade abrangida; mandato eletivo incluído | `s2-d3-rf-etica-671` | aprofundamento S2 |
| D3-LEG-14 | Legislação | dever × direito | arts. 5º e 7º têm funções diferentes | `s2-d3-rf-etica-671` | revisão S1 + aprofundamento S2 |
| D3-LEG-15 | Legislação | infração e noção de sanção | art. 6º tipifica; sanção depende de processo e trânsito administrativo | `s2-d3-rf-etica-671` | revisão S1 + aprofundamento S2 |
| D3-PORT-01 | Português | conectores | reconhecer oposição, conclusão, causa, concessão, condição e finalidade | `s2-d3-rf-portugues` | revisão S1 aplicada |
| D3-PORT-02 | Português | referência | explicitar antecedente e eliminar ambiguidade | `s2-d3-rf-portugues` | revisão S1 aplicada |
| D3-PORT-03 | Português | concordância | `haver` existencial e `fazer` temporal são impessoais; `existir` concorda | `s2-d3-rf-portugues` | revisão S1 aprofundada |
| D3-PORT-04 | Português | crase | preposição `a` + termo que admita artigo/pronome iniciado por `a` | `s2-d3-rf-portugues` | revisão S1 aplicada |
| D3-PORT-05 | Português | pontuação | não separar sujeito/verbo; isolar aposto e oração deslocada | `s2-d3-rf-portugues` | revisão S1 aplicada |

## Tabela de revisão rápida do Dia 3

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| TCP | fluxo confiável, ordenado e orientado à conexão | ACK como confirmação de negócio | HTTPS tradicional sobre TCP |
| UDP | transporte de datagramas sem confiabilidade nativa | “UDP nunca é confiável” | DHCP e NTP |
| HTTP | protocolo de requisição/resposta | stateless como ausência de sessão na aplicação | GET seguido de resposta 200 |
| HTTPS | HTTP protegido por TLS | certificado como garantia de site honesto | portal na porta 443 |
| DNS | sistema hierárquico de nomes e dados | reduzir a nome→IP ou somente UDP | consulta clássica A/AAAA na porta 53 |
| DHCP | entrega parâmetros de rede | confundir com DNS | DORA em UDP 67/68 |
| SMTP | submissão e transferência de e-mail | usar para ler caixa postal | servidor envia para MX |
| POP3 | acesso simples à caixa | dizer que sempre apaga do servidor | porta 110/995 |
| IMAP | caixa e estado sincronizados no servidor | tratar como envio de mensagem | porta 143/993 |
| FTP | transferência com controle e dados separados | considerar sempre seguro | controle em 21/TCP |
| FTPS | FTP protegido por TLS, com controle e dados separados | achar que TLS no controle protege automaticamente os dados | explícito 21 + `AUTH TLS`/`PROT P`; implícito 990 no controle |
| SFTP | transferência de arquivos sobre SSH | chamar de FTP sobre TLS | subsistema SSH na 22/TCP |
| SSH | terminal e serviços remotos protegidos | confundir com Telnet | administração na 22/TCP |
| Telnet | terminal remoto sem proteção criptográfica moderna | usar para credenciais sensíveis | porta 23/TCP |
| SNMP | gerenciamento por gerente, agente, MIB e OID | achar que toda versão cifra | consultas 161, traps 162 |
| LDAP | acesso a diretórios | tratar como SQL | bind e search na 389 |
| proxy direto | atua em nome de clientes | presumir anonimato ou inspeção total | política de navegação |
| proxy reverso | atua em nome de servidores | confundir com gateway padrão | balanceamento e TLS |
| NAT básico | tradução de endereço sem porta | tratar como firewall ou PAT | associação entre endereços |
| PAT/NAPT | tradução de endereço e porta | achar que um público atende um único host | várias origens em um IP |
| NTP | sincronização de relógio | confundir com fuso | UDP 123 |

## Pegadinhas do Dia 3

- DNS clássico usa UDP **e** TCP na porta 53; formas como DoT e DoH usam outros encapsulamentos e portas.
- DHCP entrega servidor DNS como opção, mas não realiza a resolução de nomes.
- TCP oferece entrega confiável do fluxo; não comprova sucesso da aplicação.
- UDP não possui conexão nativa, mas aplicações podem implementar confiabilidade.
- HTTPS não é “outro conteúdo”: é HTTP protegido por TLS.
- A porta 443 não prova que o tráfego seja legítimo.
- SMTP envia; POP3 e IMAP acessam mensagens.
- POP3 não apaga obrigatoriamente toda mensagem do servidor.
- SFTP é protocolo sobre SSH; FTPS é FTP protegido por TLS.
- No FTPS explícito, `AUTH TLS` protege o controle; o canal de dados usa `PBSZ 0` e `PROT P` para solicitar proteção privada.
- FTPS continua separando controle e dados; portas de dados podem ser negociadas nos modos ativo e passivo.
- FTP passivo não limita a conexão de dados à porta 20.
- SNMPv3 pode oferecer autenticação e privacidade, conforme configuração.
- LDAP pode participar da autenticação, mas não é sinônimo de autorização.
- Proxy reverso representa o servidor, não o cliente.
- NAT/PAT não criptografa e não substitui firewall.
- NTP sincroniza tempo, não fuso horário.
- Porta padrão é convenção, não vínculo obrigatório.

## Prática guiada

### Caso — Atendimento digital do CRA-PR

Uma estação na VLAN de atendimento recebe 10.20.30.25/24, gateway 10.20.30.1 e DNS 10.20.10.53 por DHCP. O usuário acessa o nome reservado servicos.cra-pr.example. O nome resolve para 198.51.100.50. O firewall de borda aplica PAT, o portal é publicado por proxy reverso e os logs são enviados ao monitoramento.

#### Etapa 1 — Reconstrução do fluxo

Registre no caderno, nesta ordem:

1. DHCPDISCOVER, DHCPOFFER, DHCPREQUEST e DHCPACK;
2. consulta ao resolvedor DNS;
3. encaminhamento ao gateway;
4. tradução PAT;
5. abertura TCP e negociação TLS;
6. requisição HTTP protegida;
7. recepção pelo proxy reverso;
8. sincronização temporal necessária aos logs.

#### Etapa 2 — Diagnóstico por sintoma

Associe cada sintoma ao primeiro bloco de investigação:

| Sintoma | Primeiro foco |
|---|---|
| endereço 169.254.x.x e ausência de gateway | concessão DHCP/relay/escopo |
| IP responde, nome não resolve | DNS |
| nome resolve, porta 443 não abre | rota, firewall, NAT/PAT ou serviço |
| alerta de nome inválido no certificado | validação TLS/certificado/DNS |
| horários divergentes nos logs | NTP e configuração de tempo |
| página chega, mas login falha | aplicação, identidade e autorização |

#### Etapa 3 — Resultado esperado

O diagnóstico deve separar camada e serviço. Evite “culpar a internet” ou trocar DNS por DHCP. Registre evidências: endereço recebido, servidor consultado, resposta DNS, rota, estado da porta, certificado e horário.

## Checklist de domínio

- [ ] Diferencio protocolo, serviço, porta e socket.
- [ ] Explico o handshake e as garantias do TCP.
- [ ] Explico o que o UDP não oferece nativamente.
- [ ] Sei que DNS clássico usa TCP e UDP e que DNS não se limita a nome→IP.
- [ ] Descrevo recursão, iteração, cache, TTL e registros principais.
- [ ] Reproduzo a sequência DORA e as portas 67/68.
- [ ] Distingo SMTP, POP3 e IMAP.
- [ ] Distingo FTP, FTPS e SFTP.
- [ ] Explico FTPS explícito/implícito, canais separados e `PROT P`.
- [ ] Associo SSH e Telnet às suas propriedades.
- [ ] Explico gerente, agente, MIB, OID e traps no SNMP.
- [ ] Explico LDAP e suas portas.
- [ ] Distingo proxy direto/reverso, NAT básico e PAT/NAPT.
- [ ] Associo NTP à porta 123 e à coerência de logs.
- [ ] Reconheço as portas conhecidas sem tratá-las como obrigatórias.
- [ ] Relembrei CFA × CRA, registro, fiscalização e ética.
- [ ] Revi conectores, concordância, crase e ambiguidade.

## Orientações para o caderno de erros

Para cada erro, use cinco campos:

1. **Tema específico:** por exemplo, DNS sobre TCP.
2. **Afirmação que pareceu correta:** “DNS usa apenas UDP”.
3. **Correção técnica:** DNS clássico usa 53/UDP e 53/TCP; DNS encapsulado pode usar outros transportes.
4. **Pista do enunciado:** presença de palavra absoluta.
5. **Exemplo próprio:** transferência de zona ou resposta truncada.

Separe os erros em quatro grupos:

- função do protocolo;
- transporte/porta;
- fluxo operacional;
- comparação entre conceitos.

Não registre apenas a letra de uma alternativa. O objetivo é impedir que o mesmo raciocínio errado reapareça com outra redação.

## Fontes oficiais utilizadas — Dia 3

Fontes primárias e registros oficiais consultados em 10 de julho de 2026:

- Edital CRA-PR 2026, conforme Retificação I: https://cdnsite.institutoconsulplan.org.br/concursos/1330/b2c07c473c9749fea22728da3c964c06.pdf
- IANA — Service Name and Transport Protocol Port Number Registry: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
- RFC 9293 — Transmission Control Protocol: https://www.rfc-editor.org/rfc/rfc9293
- RFC 768 — User Datagram Protocol: https://www.rfc-editor.org/rfc/rfc768
- RFC 9110 — HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- RFC 1034 e RFC 1035 — DNS: https://www.rfc-editor.org/rfc/rfc1034 e https://www.rfc-editor.org/rfc/rfc1035
- RFC 2606 — nomes reservados para documentação: https://www.rfc-editor.org/rfc/rfc2606
- RFC 5737 — blocos IPv4 reservados para documentação: https://www.rfc-editor.org/rfc/rfc5737
- RFC 7766 — DNS Transport over TCP: https://www.rfc-editor.org/rfc/rfc7766
- RFC 2131 — DHCP: https://www.rfc-editor.org/rfc/rfc2131
- RFC 5321 — SMTP: https://www.rfc-editor.org/rfc/rfc5321
- RFC 1939 — POP3: https://www.rfc-editor.org/rfc/rfc1939
- RFC 9051 — IMAP4rev2: https://www.rfc-editor.org/rfc/rfc9051
- RFC 8314 — TLS para submissão e acesso a e-mail: https://www.rfc-editor.org/rfc/rfc8314
- RFC 959 — FTP: https://www.rfc-editor.org/rfc/rfc959
- RFC 4217 — FTP protegido por TLS, `AUTH TLS` e `PROT`: https://www.rfc-editor.org/rfc/rfc4217
- RFC 4251 — arquitetura SSH: https://www.rfc-editor.org/rfc/rfc4251
- OpenSSH — manual oficial do SFTP: https://man.openbsd.org/sftp
- RFC 854 — Telnet: https://www.rfc-editor.org/rfc/rfc854
- RFC 3411 — arquitetura SNMP: https://www.rfc-editor.org/rfc/rfc3411
- RFC 4511 — LDAP: https://www.rfc-editor.org/rfc/rfc4511
- RFC 2663 — terminologia de NAT básico e NAPT: https://www.rfc-editor.org/rfc/rfc2663
- RFC 3022 — NAT tradicional: https://www.rfc-editor.org/rfc/rfc3022
- RFC 5905 — NTPv4: https://www.rfc-editor.org/rfc/rfc5905
- Lei nº 4.769/1965: https://www.planalto.gov.br/ccivil_03/leis/l4769.htm
- Decreto nº 61.934/1967: https://www.planalto.gov.br/ccivil_03/decreto/Antigos/D61934.htm
- Lei nº 12.514/2011: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12514.htm
- RN CFA nº 649/2024: https://documentos.cfa.org.br/?a=show&c=documento&id=951
- RN CFA nº 670/2025: https://documentos.cfa.org.br/?a=show&c=documento&id=1033
- RN CFA nº 589/2020: https://documentos.cfa.org.br/arquivos/resolucao_normativa_589_2020_745.pdf
- RN CFA nº 651/2024: https://documentos.cfa.org.br/?a=show&c=documento&id=955
- RN CFA nº 671/2025: https://documentos.cfa.org.br/?a=show&c=documento&id=1038
- Manual de Redação da Presidência da República, 3ª edição: https://www.gov.br/pt-br/servicos/consultar-o-manual-de-redacao-da-presidencia-da-republica
- ABL — Vocabulário Ortográfico da Língua Portuguesa 2025–2026: https://www.academia.org.br/nossa-lingua/vocabulario-ortografico

---

# Dia 4 — Segurança de Redes

## Objetivo do dia

Construir uma visão integrada de segurança de redes: objetivos de proteção, identidade e acesso, ameaças e ataques, controles preventivos/detectivos/corretivos, criptografia, segurança Wi-Fi, resposta a incidentes e recuperação por backup.

O estudante deve sair do modelo de “produto mágico”. Firewall, IDS, IPS, VPN, criptografia e backup reduzem riscos específicos, mas nenhum deles garante segurança absoluta. Segurança resulta de governança, pessoas, processos, arquitetura, configuração, monitoramento e melhoria contínua.

## Resultados esperados

Ao concluir as 6 horas líquidas, o estudante deverá conseguir:

- explicar confidencialidade, integridade e disponibilidade com controles e incidentes distintos;
- diferenciar autenticação, autorização, auditoria/accounting e não repúdio;
- separar ativo, ameaça, vulnerabilidade, risco, evento e incidente;
- reconhecer malware, phishing, engenharia social, spoofing, sniffing, ataque on-path, força bruta, DoS e DDoS;
- classificar controles por natureza e função;
- explicar as funções e limitações de firewall, IDS, IPS, DMZ, VPN e segmentação;
- aplicar menor privilégio e controle de acesso a um cenário de órgão público;
- diferenciar criptografia simétrica, assimétrica, hash, MAC, assinatura e certificado;
- descrever, em nível conceitual, o funcionamento do TLS;
- comparar WPA2 e WPA3 sem tratá-los como invulneráveis;
- organizar resposta a incidente conforme a integração atual do NIST CSF 2.0;
- planejar backups com RPO, RTO, cópias protegidas e testes de restauração;
- revisar Administração Pública, RLM e um bloco curto de Português.

## Por que esse assunto importa para a prova

Segurança de redes permite integrar praticamente toda a Semana 2. Um ataque pode explorar DNS, credenciais, Wi-Fi, acesso remoto, serviço web ou configuração de firewall. A resposta exige endereçamento, protocolos, logs, segmentação, identidade, disponibilidade e backup.

A banca pode apresentar um controle verdadeiro e exagerar seu alcance. Exemplos:

- “HTTPS impede phishing”;
- “IDS bloqueia automaticamente todo ataque”;
- “IPS não produz falso positivo”;
- “VPN torna confiável qualquer dispositivo remoto”;
- “NAT substitui firewall”;
- “hash garante confidencialidade”;
- “certificado digital prova que a empresa é honesta”;
- “backup impede indisponibilidade”;
- “WPA3 elimina ataques a Wi-Fi”.

Em todos esses casos, a palavra absoluta é o problema.

## Como o Instituto Consulplan pode cobrar

Formatos prováveis:

- caso de vazamento, alteração indevida ou indisponibilidade para identificar o princípio CIA afetado;
- sequência de autenticação seguida de autorização;
- classificação de ameaça, vulnerabilidade, risco ou incidente;
- comparação IDS × IPS;
- arquitetura com DMZ, rede interna e banco de dados;
- escolha entre criptografia simétrica e assimétrica;
- diferença entre hash, HMAC e assinatura;
- validação de certificado durante TLS;
- cenário WPA2/WPA3 com senha fraca ou modo de transição;
- ordem de ações diante de ransomware;
- cálculo simples de RPO/RTO;
- distinção entre backup, redundância e alta disponibilidade;
- controle que reduz risco, sem eliminá-lo.

## Cronograma de 6h líquidas

As pausas são adicionais e não entram na soma.

| Bloco | Atividade | Tempo |
|---|---|---:|
| 1 | Recuperação ativa de redes, serviços e pontos de exposição | 20 min |
| 2 | CIA, identidade, AAA, não repúdio e conceitos de risco | 45 min |
| 3 | Ameaças, malware, engenharia social e ataques de rede | 55 min |
| 4 | Firewall, IDS/IPS, DMZ, VPN, segmentação e acesso | 60 min |
| 5 | Criptografia, hash, assinatura, certificados, TLS e Wi-Fi | 65 min |
| 6 | Resposta a incidentes, continuidade e backup | 45 min |
| 7 | Revisão fixa: Administração Pública | 25 min |
| 8 | Revisão fixa: Raciocínio Lógico-Matemático | 15 min |
| 9 | Revisão fixa: Português em bloco curto | 10 min |
| 10 | Prática guiada, checklist e caderno de erros | 20 min |
| **Total líquido** |  | **360 min** |

## Teoria aprofundada

<a id="s2-d4-gestao-risco"></a>
### 1. Segurança como gestão de risco

Segurança da informação não é um estado binário de “seguro” ou “inseguro”. É um processo de gestão de riscos que:

1. identifica ativos e necessidades da missão;
2. reconhece ameaças e vulnerabilidades;
3. estima probabilidade e impacto;
4. seleciona controles proporcionais;
5. monitora eficácia e mudanças;
6. aceita, evita, transfere ou trata o risco residual.

Um controle pode reduzir probabilidade, impacto ou ambos. O risco que permanece depois da aplicação dos controles é chamado **risco residual**. Ele deve ser reavaliado: conforme o contexto e a capacidade de medição, pode ser aceito, submetido a tratamento adicional ou estimado como muito baixo. Não se deve prometer “risco zero”, mas também não é necessário afirmar, como absoluto, que todo cenário sempre terá risco residual mensurável e positivo.

<a id="s2-d4-cia"></a>
### 2. Tríade CIA

#### 2.1 Confidencialidade

Confidencialidade busca impedir divulgação a pessoas, processos ou sistemas não autorizados.

Exemplos de violação:

- captura de credenciais em canal sem criptografia;
- servidor expondo processos administrativos;
- funcionário consultando cadastro sem necessidade funcional;
- backup não cifrado perdido em transporte.

Controles relacionados:

- autenticação e autorização;
- criptografia em trânsito e em repouso;
- classificação da informação;
- menor privilégio;
- segmentação;
- prevenção contra vazamento;
- descarte seguro.

#### 2.2 Integridade

Integridade busca impedir alteração ou destruição não autorizada e permitir detectar mudanças indevidas.

Exemplos de violação:

- alteração de dados de registro profissional;
- modificação de rota ou resposta DNS;
- troca de arquivo de atualização;
- adulteração de log.

Controles relacionados:

- hash, MAC e assinatura, conforme a finalidade;
- controle de mudanças;
- validação de entrada;
- permissões;
- logs protegidos;
- versionamento;
- transações e reconciliação.

Integridade não significa que o dado seja verdadeiro desde a origem. A correspondência com um resumo hash de referência confiável pode indicar que o conteúdo não mudou desde aquela referência, mesmo que o arquivo já contivesse informação errada; isso não prova sua veracidade factual.

Integridade também não é sinônimo de **imutabilidade**. Alterações autorizadas e corretamente registradas podem preservar a integridade; armazenamento imutável é um controle específico que impede ou restringe mudanças durante certo período, não a definição completa do princípio.

#### 2.3 Disponibilidade

Disponibilidade busca assegurar acesso oportuno e confiável a sistemas e dados por usuários autorizados.

Exemplos de violação:

- DDoS esgotando capacidade;
- ransomware indisponibilizando arquivos;
- falha de energia;
- exclusão acidental;
- dependência única de equipamento ou provedor.

Controles relacionados:

- redundância;
- tolerância a falhas;
- capacidade e proteção contra DDoS;
- monitoramento;
- planos de continuidade;
- backup e restauração;
- atualização e manutenção;
- rotas e serviços alternativos.

Backup apoia recuperação, mas normalmente não impede a interrupção inicial.

#### 2.4 Um incidente pode atingir mais de um princípio

Ransomware moderno pode:

- exfiltrar dados: confidencialidade;
- alterar ou cifrar arquivos: integridade;
- interromper serviços: disponibilidade.

Não force todo cenário a apenas uma letra da tríade quando há múltiplos efeitos.

<a id="s2-d4-identidade-auditoria"></a>
### 3. Autenticação, autorização, auditoria e não repúdio

#### 3.1 Autenticação

Autenticação estabelece confiança na identidade alegada. Exemplos de fatores:

- algo que o usuário sabe: senha ou PIN;
- algo que possui: token, cartão, chave criptográfica;
- algo que é: característica biométrica.

MFA exige fatores de categorias diferentes. Senha + outra senha não constitui autenticação multifator.

A autenticação pode envolver usuários, máquinas, serviços e dispositivos. Um certificado de servidor em TLS autentica o servidor quando a validação é correta; isso não autoriza o cliente a acessar todos os recursos.

#### 3.2 Autorização

Autorização determina o que a identidade autenticada pode fazer.

Modelos:

- **RBAC:** permissão por papel ou função;
- **ABAC:** decisão por atributos do sujeito, recurso, ação e contexto;
- listas de controle de acesso;
- políticas baseadas em grupos.

Princípios:

- menor privilégio;
- necessidade de conhecer;
- separação de funções;
- revisão periódica;
- remoção tempestiva de acesso.

Autenticar vem logicamente antes de autorizar em muitos fluxos, mas possuir identidade válida não implica permissão.

#### 3.3 Auditoria e accounting

**Accounting** registra consumo, sessões e ações para responsabilização e controle. **Auditoria** examina e analisa registros, controles e conformidade. Um registro útil a essas atividades deve permitir responder:

- quem;
- fez o quê;
- quando;
- de onde;
- sobre qual recurso;
- com qual resultado.

Logs precisam de:

- relógios sincronizados;
- retenção definida;
- controle de acesso;
- integridade;
- centralização quando apropriado;
- monitoramento e alertas;
- contexto suficiente para investigação.

Registrar tudo sem capacidade de análise não produz segurança eficaz. Logs também podem conter dados pessoais e precisam de proteção.

#### 3.4 Não repúdio

Não repúdio oferece evidências para dificultar a negação falsa de uma ação. Assinaturas digitais podem apoiar integridade, origem e prova perante terceiro.

O resultado depende de:

- proteção da chave privada;
- vínculo confiável entre identidade e chave;
- certificado válido;
- carimbo temporal ou evidência de tempo, quando necessário;
- política e procedimento;
- trilha de auditoria;
- contexto jurídico.

Hash isolado não oferece não repúdio, pois qualquer pessoa pode calcular o mesmo hash.

#### 3.5 Modelo AAA

No uso técnico tradicional, **AAA** significa:

- **Authentication:** confirmar a identidade;
- **Authorization:** aplicar as permissões;
- **Accounting:** registrar consumo, sessões e ações para responsabilização e controle.

Accounting fornece insumos para auditoria, mas os termos não são sinônimos perfeitos. Auditoria é o processo mais amplo de examinar registros, controles e conformidade. Em material que apresente o terceiro A como “auditoria”, preserve a ideia funcional de rastreabilidade, mas reconheça que protocolos clássicos de AAA usam o termo accounting.

<a id="s2-d4-conceitos-risco"></a>
### 4. Ativo, ameaça, vulnerabilidade, risco, evento e incidente

| Termo | Sentido operacional |
|---|---|
| Ativo | informação, sistema, pessoa, serviço ou recurso com valor |
| Ameaça | circunstância ou agente capaz de causar dano |
| Vulnerabilidade | fraqueza que pode ser explorada ou acionada |
| Risco | combinação de probabilidade e impacto adverso |
| Evento | ocorrência observável em sistema ou rede |
| Incidente | ocorrência que compromete ou ameaça comprometer segurança/política |
| Controle | medida para modificar o risco |

Exemplo:

- ativo: portal de serviços;
- ameaça: grupo criminoso;
- vulnerabilidade: gateway VPN com falha conhecida e correção disponível ainda não aplicada;
- evento: milhares de tentativas de login;
- incidente: acesso indevido confirmado;
- risco: perda de dados e interrupção, considerada probabilidade e impacto;
- controle: correção, MFA, restrição de origem e monitoramento.

Uma vulnerabilidade sem ameaça relevante ainda deve ser gerida, mas risco não é sinônimo de vulnerabilidade.

<a id="s2-d4-malware"></a>
### 5. Malware

Malware é software ou código malicioso. Categorias podem se sobrepor.

#### 5.1 Vírus

Vincula-se a arquivo ou programa hospedeiro e depende de execução/propagação associada. Não é correto chamar todo malware de vírus.

#### 5.2 Worm

Propaga-se automaticamente por redes ou sistemas, explorando falhas ou credenciais. Pode consumir recursos e instalar cargas adicionais.

#### 5.3 Cavalo de Troia

Apresenta-se como software legítimo ou desejável para induzir execução. A ideia central é disfarce, não autorreplicação obrigatória.

#### 5.4 Ransomware

Busca negar acesso a dados ou sistemas, frequentemente cifrando arquivos. Campanhas podem combinar exfiltração, alteração/destruição e interrupção, comprometendo simultaneamente **confidencialidade, integridade e disponibilidade**. Backup reduz impacto de recuperação, mas não impede vazamento nem elimina a necessidade de conter e erradicar a presença do atacante.

#### 5.5 Spyware, rootkit, bot e botnet

- spyware coleta informações;
- rootkit busca ocultar presença ou manter privilégio;
- bot é um programa ou agente que executa comandos sob controle remoto; por extensão, o host ou dispositivo comprometido que o executa também pode ser chamado de bot;
- botnet é conjunto de bots, usado inclusive em DDoS.

Controles incluem atualização, proteção de endpoint, allowlisting, menor privilégio, filtros, segmentação, MFA, monitoramento e treinamento. Nenhum antivírus detecta toda ameaça.

<a id="s2-d4-phishing"></a>
### 6. Phishing e engenharia social

**Engenharia social** manipula pessoas para obter informação, acesso ou ação.

Técnicas:

- urgência falsa;
- autoridade aparente;
- curiosidade ou recompensa;
- pretexto;
- ligação telefônica;
- entrada física acompanhando pessoa autorizada;
- mídia removível como isca.

**Phishing** usa mensagem ou página fraudulenta para induzir clique, envio de credenciais, pagamento ou execução.

Variações:

- spear phishing: alvo específico;
- whaling: pessoa de alta relevância;
- smishing: SMS/mensagem;
- vishing: voz.

Controles:

- treinamento e canal simples de denúncia;
- verificação por canal independente;
- filtros e autenticação de e-mail;
- MFA resistente a phishing quando viável;
- bloqueio de macros e conteúdo perigoso;
- proteção de navegador/endpoint;
- simulações acompanhadas de educação.

MFA reduz impacto de senha roubada, mas certos ataques podem capturar sessão, induzir aprovação ou explorar recuperação de conta.

<a id="s2-d4-ataques-rede"></a>
### 7. Ataques de rede

#### 7.1 Spoofing

Spoofing falsifica identidade ou origem aparente. Pode envolver:

- IP;
- ARP;
- DNS;
- e-mail;
- ponto de acesso Wi-Fi;
- identificador de chamada.

O efeito depende do protocolo. IP spoofing não garante receber respostas; ARP spoofing em rede local pode redirecionar tráfego; DNS spoofing pode induzir resolução falsa.

#### 7.2 Sniffing

Sniffing é captura e análise de tráfego. Pode ser legítimo em diagnóstico autorizado ou malicioso. Em rede com switches, o invasor pode precisar de posição privilegiada, espelhamento indevido, spoofing ou comprometimento de equipamento.

Criptografia protege conteúdo em trânsito, mas não esconde todos os metadados.

#### 7.3 Man-in-the-middle ou ataque on-path

O atacante posiciona-se no caminho para observar e potencialmente alterar a comunicação.

Mitigações:

- TLS com validação correta;
- VPN autenticada;
- proteção de rede local;
- certificados;
- DNS protegido conforme arquitetura;
- evitar ignorar alertas;
- redes Wi-Fi adequadamente protegidas.

Não basta “haver criptografia”: se o cliente aceita certificado falso ou a chave foi comprometida, a proteção pode falhar.

#### 7.4 Força bruta e ataques a credenciais

- força bruta testa combinações;
- ataque de dicionário usa candidatos prováveis;
- password spraying testa poucas senhas comuns em muitas contas;
- credential stuffing reutiliza credenciais vazadas.

Controles:

- MFA;
- senhas únicas;
- gerenciador de senhas;
- limitação e detecção de tentativas;
- bloqueio adaptativo;
- monitoramento;
- armazenamento de senha com KDF apropriada e salt.

Bloqueio fixo agressivo pode ser explorado para negação de serviço contra contas.

#### 7.5 DoS e DDoS

DoS busca degradar ou impedir serviço. DDoS distribui a origem entre múltiplos sistemas.

Categorias de efeito:

- saturação de banda;
- esgotamento de estado em firewall/servidor;
- consumo de CPU/memória;
- exploração de custo alto na aplicação;
- amplificação/reflexão.

Mitigações podem envolver filtragem, rate limiting, capacidade, CDN/serviço anti-DDoS, anycast, proteção de aplicação e coordenação com provedor. Um firewall local não absorve ataque que já saturou o enlace.

<a id="s2-d4-controles"></a>
### 8. Controles e defesa em profundidade

#### 8.1 Por natureza

- administrativos: políticas, treinamento, contratos, avaliação de risco;
- técnicos: firewall, MFA, criptografia, EDR, ACL;
- físicos: fechaduras, vigilância, controle ambiental.

#### 8.2 Por função

- preventivos: procuram evitar;
- detectivos: identificam;
- corretivos: corrigem;
- de recuperação: restauram;
- dissuasórios: desencorajam;
- compensatórios: reduzem risco quando o controle principal não é viável.

Um mesmo controle pode exercer mais de uma função.

#### 8.3 Defesa em profundidade

Defesa em profundidade usa camadas independentes e complementares. Exemplo:

1. treinamento reduz clique;
2. filtro bloqueia mensagem;
3. MFA dificulta uso da senha;
4. segmentação limita movimento;
5. EDR detecta execução;
6. backup permite recuperação.

Se todas as camadas dependem da mesma credencial administrativa, há uma falha comum que reduz a profundidade.

<a id="s2-d4-firewall"></a>
### 9. Firewall

Firewall controla fluxo entre redes ou hosts de posturas diferentes, conforme política.

Tipos e capacidades:

- filtragem sem estado: avalia campos de cada pacote;
- stateful: acompanha estado da conexão;
- proxy/application gateway: termina e intermedeia a aplicação;
- host-based: protege o próprio equipamento;
- recursos de próxima geração: identificação de aplicação, inspeção e integração com ameaças, conforme produto.

Boas práticas:

- política de negação por padrão quando adequada;
- somente portas, origens e destinos necessários;
- regras documentadas;
- revisão periódica;
- logs de eventos relevantes;
- controle de saída;
- administração por rede protegida;
- teste após mudança.

Limitações:

- porta permitida pode transportar ataque;
- tráfego cifrado pode reduzir visibilidade sem terminação autorizada;
- regra excessivamente ampla neutraliza o controle;
- ameaça interna pode não cruzar o firewall observado;
- firewall não corrige vulnerabilidade da aplicação.

<a id="s2-d4-ids-ips"></a>
### 10. IDS × IPS

#### 10.1 IDS

IDS monitora e gera alerta. Em rede, costuma ficar fora do caminho direto, recebendo cópia do tráfego. Pode detectar por:

- assinatura;
- anomalia;
- comportamento;
- combinação de métodos.

#### 10.2 IPS

IPS atua em linha ou em posição capaz de prevenir, podendo descartar, bloquear ou interromper tráfego.

#### 10.3 Limitações obrigatórias

IDS e IPS:

- podem gerar falso positivo;
- podem deixar passar ataque, produzindo falso negativo;
- exigem atualização e ajuste;
- têm visibilidade limitada sobre tráfego cifrado;
- podem sofrer evasão ou sobrecarga;
- não substituem correção, segmentação, autenticação e resposta.

IPS não “garante bloqueio”. Uma política muito agressiva pode afetar disponibilidade; uma política permissiva pode não conter o ataque.

<a id="s2-d4-dmz"></a>
### 11. DMZ

DMZ é segmento intermediário para serviços expostos, reduzindo acesso direto da internet à rede interna.

Arquitetura simplificada:

- internet;
- firewall/perímetro;
- DMZ com proxy reverso, DNS público ou servidor web;
- controle adicional;
- rede interna;
- banco de dados em segmento restrito.

Princípios:

- permitir somente fluxos necessários;
- evitar banco sensível diretamente na DMZ;
- separar administração;
- monitorar comunicações da DMZ para dentro;
- presumir que um serviço exposto pode ser comprometido.

DMZ não torna o servidor confiável nem é sinônimo de “rede sem firewall”.

<a id="s2-d4-vpn"></a>
### 12. VPN

VPN cria túnel protegido sobre rede não confiável.

Modelos:

- site-to-site: conecta redes;
- acesso remoto: conecta usuário/dispositivo à organização;
- IPsec: proteção na camada IP;
- TLS VPN: proteção baseada em TLS, conforme solução e escopo.

Benefícios:

- confidencialidade e integridade do tráfego;
- autenticação dos pares;
- acesso remoto controlado.

Limitações:

- dispositivo comprometido continua perigoso;
- VPN não autoriza acesso irrestrito;
- credencial roubada pode abrir o túnel;
- gateway VPN exposto e sem correção pode ser explorado antes mesmo da autenticação do usuário, comprometendo credenciais, sessões ou o próprio perímetro;
- tráfego já decifrado precisa de controles internos.

Inventarie e reduza a exposição do gateway, acompanhe avisos do fornecedor, aplique correções tempestivamente ou mitigações documentadas quando a atualização imediata não for possível. Combine isso com MFA, postura de dispositivo, menor privilégio, segmentação e logs. O túnel pode estar criptograficamente correto e ainda terminar em um gateway vulnerável ou em um endpoint comprometido.

<a id="s2-d4-segmentacao"></a>
### 13. Segmentação e controle de acesso

Segmentação divide ambientes por função, sensibilidade ou risco:

- usuários;
- servidores;
- gestão;
- convidados;
- IoT;
- backup;
- desenvolvimento;
- DMZ.

Mecanismos:

- VLANs e sub-redes;
- ACLs;
- firewalls internos;
- VRFs;
- controle de acesso à rede;
- microsegmentação.

VLAN separa domínios de camada 2 e de broadcast, o que continua tendo valor operacional e restringe certos ataques locais. Porém, VLAN não substitui política de controle entre segmentos. Se o roteamento inter-VLAN permitir fluxos amplos, um invasor pode realizar **movimento lateral roteado** entre sub-redes. ACLs, firewalls internos, identidade e menor privilégio devem limitar esse caminho.

Regras devem considerar:

- origem;
- destino;
- porta/protocolo;
- identidade;
- dispositivo;
- horário/contexto;
- necessidade da missão.

Menor privilégio deve alcançar usuários, serviços e contas administrativas.

<a id="s2-d4-criptografia"></a>
### 14. Criptografia simétrica e assimétrica

#### 14.1 Criptografia simétrica

Usa chave secreta compartilhada para cifrar e decifrar. É eficiente para grande volume de dados. AES é exemplo de cifra simétrica de bloco.

Desafio principal: distribuir, armazenar, rotacionar e revogar chaves com segurança.

#### 14.2 Criptografia assimétrica

Usa par de chaves matematicamente relacionado:

- pública;
- privada.

Aplicações:

- assinatura digital;
- estabelecimento de chaves;
- autenticação;
- cifração em esquemas apropriados.

É mais custosa e não costuma substituir cifra simétrica no tráfego volumoso.

#### 14.3 Criptografia híbrida

Protocolos como TLS usam mecanismos assimétricos ou PSK para autenticação/estabelecimento e chaves simétricas para proteger dados da sessão. Não se deve afirmar que HTTPS cifra todo o conteúdo diretamente com a chave privada do servidor.

<a id="s2-d4-hash-hmac-senhas"></a>
### 15. Hash, MAC e armazenamento de senhas

#### 15.1 Hash

Função hash transforma entrada de tamanho variável em resumo de tamanho fixo. Propriedades desejadas incluem resistência a:

- encontrar entrada para determinado resumo;
- encontrar segunda entrada com o mesmo resumo;
- encontrar qualquer colisão.

Uso:

- detectar alteração ao comparar o resumo calculado com uma referência obtida por canal confiável ou protegida por mecanismo adequado;
- compor assinaturas;
- identificação de arquivo;
- estruturas de integridade.

Hash:

- não é criptografia reversível;
- não fornece confidencialidade;
- sem segredo, não autentica a origem;
- não prova sozinho quem calculou o resumo.

Se um atacante puder substituir tanto o arquivo quanto o resumo publicado ao lado dele, a comparação de hashes não revela a adulteração. A referência precisa ser confiável, assinada, autenticada ou recebida por canal independente; quando há segredo compartilhado, HMAC oferece autenticação e integridade da mensagem.

#### 15.2 MAC e HMAC

MAC usa segredo compartilhado para oferecer integridade e autenticação da mensagem entre quem conhece a chave. HMAC constrói MAC com função hash de modo padronizado.

MAC não oferece não repúdio forte entre partes que compartilham a mesma chave, pois ambas poderiam produzi-lo.

#### 15.3 Senhas

Senhas não devem ser armazenadas por criptografia reversível quando basta verificar conhecimento. Use função de derivação de chave para senha, com:

- salt único;
- custo configurável;
- algoritmo apropriado;
- parâmetros e migração documentados.

Hash rápido genérico, sem salt, facilita ataques com bases pré-computadas e alto volume de tentativas.

<a id="s2-d4-assinatura-certificado"></a>
### 16. Assinatura digital e certificado digital

#### 16.1 Assinatura digital

Em modelo simplificado:

1. calcula-se resumo da mensagem;
2. o signatário usa a chave privada no algoritmo de assinatura;
3. o verificador usa a chave pública;
4. alteração da mensagem invalida a verificação.

Pode apoiar:

- integridade;
- autenticidade de origem;
- não repúdio.

Não fornece confidencialidade por si só.

#### 16.2 Certificado digital

Certificado X.509 associa identidade ou nome a uma chave pública, com assinatura de uma autoridade certificadora.

Validação envolve:

- cadeia até âncora confiável;
- assinatura;
- prazo de validade;
- nome esperado;
- uso autorizado da chave;
- políticas;
- situação de revogação, conforme mecanismo e contexto.

Certificado válido prova o vínculo que foi validado e a posse da chave no protocolo; não prova ausência de malware, qualidade da aplicação ou honestidade comercial.

<a id="s2-d4-tls"></a>
### 17. TLS

TLS estabelece canal protegido para protocolos de aplicação.

Fluxo conceitual do TLS 1.3:

1. cliente anuncia versões, algoritmos e material de estabelecimento;
2. servidor seleciona parâmetros;
3. as partes derivam segredos compartilhados;
4. servidor apresenta certificado quando esse modo é usado;
5. cliente valida cadeia, nome e prova de posse da chave;
6. mensagens Finished confirmam integridade do handshake;
7. dados da aplicação usam chaves simétricas de sessão e AEAD.

Propriedades pretendidas:

- autenticação do servidor;
- autenticação opcional do cliente;
- confidencialidade;
- integridade.

TLS não protege:

- dado antes de entrar no canal ou depois de sair;
- endpoint comprometido;
- aplicação vulnerável;
- usuário enganado que aceita alerta;
- chave privada exposta;
- metadados que o protocolo não oculta.

HTTPS é HTTP sobre TLS. TLS não é sinônimo de certificado, embora certificados sejam mecanismo central em muitos usos.

<a id="s2-d4-wifi"></a>
### 18. Segurança Wi-Fi: WPA2 e WPA3

#### 18.1 Riscos do meio sem fio

O sinal pode ultrapassar limites físicos. Riscos:

- escuta de tráfego desprotegido;
- ponto de acesso falso;
- senha compartilhada;
- desautenticação e interferência;
- dispositivo não autorizado;
- configuração fraca;
- administração exposta.

#### 18.2 WPA2

WPA2 implementa segurança baseada em IEEE 802.11i e usa proteção robusta como AES-CCMP em configurações adequadas.

Modos:

- Personal: segredo pré-compartilhado;
- Enterprise: autenticação 802.1X/EAP com infraestrutura de identidade.

Uma senha Personal fraca ainda é risco. Enterprise exige validar corretamente o servidor de autenticação para evitar entrega de credenciais a infraestrutura falsa.

#### 18.3 WPA3

**WPA3-Personal usa SAE — Simultaneous Authentication of Equals**, uma troca autenticada por senha, em lugar da autenticação WPA2-Personal baseada em PSK. O usuário ainda pode informar uma senha, mas a captura passiva de uma associação não fornece o mesmo verificador reutilizável para tentativas de dicionário offline. Cada tentativa de adivinhação contra SAE exige interação, sujeita a controles e observação da rede.

Isso não torna senha fraca recomendável nem elimina falhas de implementação, tentativas online, engenharia social ou comprometimento do dispositivo. Em **modo de transição WPA2/WPA3**, clientes legados ainda podem usar WPA2-Personal; portanto, as garantias do conjunto dependem do modo realmente negociado. WPA3 também reforça proteção de quadros de gerenciamento em perfis certificados.

WPA3-Enterprise oferece perfis empresariais e algoritmos mais fortes conforme certificação e configuração.

WPA3 não elimina:

- phishing;
- endpoint comprometido;
- senha fraca em sistemas externos;
- ponto de acesso mal configurado;
- vulnerabilidade de firmware;
- risco de modo de transição;
- engenharia social.

#### 18.4 Boas práticas Wi-Fi

- preferir WPA3 quando ecossistema e política suportarem;
- usar WPA2 com configuração forte quando necessário;
- desativar WEP e WPA legado;
- usar senha longa e única no modo Personal;
- preferir Enterprise em ambiente institucional;
- validar certificados do EAP;
- desabilitar WPS quando não necessário;
- separar convidados e dispositivos;
- atualizar firmware;
- monitorar pontos de acesso não autorizados;
- limitar administração a rede de gestão.

<a id="s2-d4-resposta-incidentes"></a>
### 19. Resposta a incidentes

O NIST SP 800-61 Rev. 3, publicado em abril de 2025, integra resposta a incidentes ao NIST CSF 2.0 e substitui a Rev. 2. A resposta não deve ser vista como tarefa isolada iniciada apenas após o ataque.

#### 19.1 Preparação e lições aprendidas

As funções **Govern, Identify e Protect** apoiam preparação:

- papéis e autoridade;
- inventário;
- classificação de ativos;
- contatos e comunicação;
- playbooks;
- logging;
- ferramentas;
- backups;
- exercícios;
- fornecedores e obrigações;
- critérios de severidade.

Lições aprendidas retroalimentam políticas e controles.

#### 19.2 Detecção

Em **Detect**:

- coletar alertas e contexto;
- validar se há incidente;
- correlacionar fontes;
- delimitar ativos, contas, dados e tempo;
- priorizar por impacto e urgência;
- preservar evidência volátil quando apropriado.

Alerta não é sinônimo de incidente confirmado.

#### 19.3 Resposta e contenção

No NIST CSF 2.0 usado pelo SP 800-61 Rev. 3, **Respond** inclui análise, coordenação, comunicação e mitigação do incidente. Dentro de mitigação, **contenção** e **erradicação** aparecem como resultados distintos.

Conter significa impedir ou limitar a expansão do incidente. Exemplos:

- isolar host em rede de remediação;
- bloquear indicador ou fluxo;
- desabilitar ou limitar conta comprometida;
- separar temporariamente um segmento;
- proteger backups ainda não afetados.

Desligar imediatamente pode destruir evidência volátil ou interromper serviço crítico. A decisão depende do playbook, do risco de propagação, do impacto operacional e da capacidade forense.

#### 19.4 Erradicação

Erradicar significa remover mecanismos de persistência e pontos de entrada depois que a expansão foi contida em grau suficiente. Pode envolver:

- eliminar malware e tarefas persistentes;
- identificar todos os hosts e serviços afetados;
- corrigir vulnerabilidades exploradas;
- desabilitar contas criadas ou violadas;
- rotacionar credenciais e chaves comprometidas;
- reconstruir componentes quando não houver confiança no estado existente.

Contenção ganha tempo; erradicação trata causa, persistência e fraquezas exploradas. Uma ação temporária de bloqueio não deve ser confundida com remoção completa do problema.

#### 19.5 Recuperação

Em **Recover**, ativos e operações afetados são restaurados para estado conhecido e validado:

- restaurar ou reconstruir por prioridade;
- verificar integridade e funcionamento;
- confirmar que persistência e entradas exploradas foram tratadas;
- monitorar recorrência;
- comunicar o retorno;
- validar controles e acompanhar impactos;
- documentar lições.

As atividades podem se sobrepor conforme o incidente, mas os objetivos não são iguais. Recuperar backup sem contenção e erradicação suficientes pode reinfectar o ambiente.

#### 19.6 Preservação e comunicação

Registre:

- linha do tempo;
- decisões;
- responsáveis;
- evidências;
- hash e cadeia de custódia, quando aplicável;
- notificações;
- impacto em dados pessoais;
- critérios de encerramento.

Resposta técnica, comunicação institucional, assessoria jurídica, proteção de dados e continuidade devem trabalhar juntas.

<a id="s2-d4-backup"></a>
### 20. Backup e disponibilidade

#### 20.1 Tipos

- **completo:** copia todo o conjunto selecionado;
- **incremental:** copia alterações desde o último backup de qualquer tipo;
- **diferencial:** copia alterações desde o último completo.

Em restauração típica:

- completo: restaura um conjunto;
- incremental: último completo + cadeia de incrementais;
- diferencial: último completo + último diferencial.

Implementações variam; valide documentação da ferramenta.

#### 20.2 RPO e RTO

- **RPO — Recovery Point Objective:** objetivo temporal que define o ponto no tempo para o qual os dados devem ser recuperados após a interrupção. Em termos operacionais, expressa a janela máxima de perda de dados que o plano pretende tolerar;
- **RTO — Recovery Time Objective:** objetivo de tempo para restabelecer o serviço ou capacidade definida.

Backup diário pode ser compatível com RPO de 24 horas, mas não com RPO de 15 minutos. RPO é meta definida previamente, não sinônimo da perda efetivamente observada no incidente. Ter cópia não garante RTO curto se a restauração leva dias.

#### 20.3 Proteção contra ransomware

- cópias offline ou logicamente isoladas;
- armazenamento imutável quando adequado;
- credenciais separadas;
- criptografia;
- múltiplas versões;
- monitoramento de falhas;
- teste periódico de restauração;
- cópia de configurações e chaves necessárias;
- prioridade de recuperação definida.

#### 20.4 Backup × redundância × alta disponibilidade

- backup recupera estado anterior;
- redundância mantém componente alternativo;
- alta disponibilidade reduz interrupção por arquitetura e automação.

Replicação pode copiar exclusão ou cifração maliciosa. RAID não substitui backup. Backup não substitui redundância para serviço que não pode parar.

## Exemplos práticos e resolvidos

### Exemplo resolvido 1 — Classificação CIA

**Cenário:** invasor copia a base, altera registros e cifra o servidor.

**Resolução:**

- cópia indevida: confidencialidade;
- alteração: integridade;
- cifração/indisponibilidade: disponibilidade.

O incidente afeta toda a tríade.

### Exemplo resolvido 2 — Autenticação não implica autorização

**Cenário:** servidor autentica com MFA, mas consulta cadastro fora de sua unidade.

**Resolução:** a identidade foi autenticada; a autorização está excessiva. Corrigir RBAC/ABAC, revisar grupos e registrar o acesso. MFA não corrige permissão indevida.

### Exemplo resolvido 3 — IDS ou IPS

**Cenário:** a organização quer observar tráfego sem risco de bloquear produção durante a fase inicial.

**Resolução:** IDS fora de banda é adequado para começar a detectar e ajustar regras. Após testes, controles preventivos podem ser ativados. Mesmo então, falso positivo e falso negativo continuam possíveis.

### Exemplo resolvido 4 — Publicação em DMZ

**Cenário:** portal público acessa banco de registrados.

**Arquitetura recomendada:**

1. proxy reverso/web na DMZ;
2. aplicação em segmento próprio;
3. banco em segmento interno;
4. somente fluxos necessários entre camadas;
5. administração por rede de gestão;
6. logs centralizados;
7. autenticação forte.

Colocar web e banco na mesma DMZ aumenta impacto de comprometimento.

### Exemplo resolvido 5 — TLS em uma conexão

**Cenário:** navegador recebe certificado válido para nome diferente.

**Resolução:** cadeia válida não basta; o nome deve corresponder ao destino esperado. Ignorar o alerta abre possibilidade de conexão ao servidor errado ou ataque on-path.

### Exemplo resolvido 6 — Ransomware

**Cenário:** várias estações cifram compartilhamento às 10h; último backup íntegro é de 2h.

**Sequência:**

1. resposta: ativar plano e classificar impacto;
2. contenção: isolar sistemas/contas comprometidos e limitar expansão;
3. preservação: coletar as evidências necessárias;
4. erradicação: identificar vetor, alcance e persistência;
5. erradicação: remover persistência e corrigir causas exploradas;
6. recuperação: validar backup limpo;
7. recuperação: restaurar por prioridade;
8. recuperação: monitorar recorrência;
9. melhoria: comunicar e incorporar lições.

Se a restauração termina às 18h, a perda potencial é de oito horas de dados e o tempo decorrido até a recuperação é de oito horas. Esses valores observados não são automaticamente o RPO e o RTO: RPO/RTO são objetivos definidos pela organização, usados para avaliar se o resultado ficou dentro da meta.

### Exemplo resolvido 7 — Wi-Fi institucional

**Cenário:** todos os usuários e dispositivos da rede Wi-Fi institucional compartilham a mesma senha WPA2-Personal.

**Risco:** segredo compartilhado, revogação difícil e pouca responsabilização individual.

**Melhoria:** WPA2/WPA3-Enterprise com 802.1X, identidade individual, validação de certificado, rede de convidados separada, atualização e monitoramento. WPA3-Personal com senha forte melhora segurança doméstica/pequena, mas não oferece a mesma identidade individual de Enterprise.

## Diferenças entre conceitos parecidos

| Conceito 1 | Conceito 2 | Diferença decisiva |
|---|---|---|
| confidencialidade | integridade | divulgação indevida × alteração indevida |
| integridade | disponibilidade | proteção contra alteração/destruição indevida × acesso oportuno |
| autenticação | autorização | comprovar identidade × definir permissão |
| accounting | auditoria | registrar uso/sessões para responsabilização × examinar registros, controles e conformidade |
| auditoria | não repúdio | registrar/analisar ações × produzir evidência contra negação falsa |
| ameaça | vulnerabilidade | causa potencial × fraqueza explorável |
| risco | incidente | possibilidade avaliada × ocorrência que compromete/ameaça comprometer |
| vírus | worm | depende de hospedeiro/execução × autopropagação |
| phishing | engenharia social | técnica por mensagem/página × categoria ampla de manipulação |
| spoofing | sniffing | falsificação × captura/observação |
| sniffing | on-path | observação pode ser passiva × posição ativa para interceptar/alterar |
| força bruta | credential stuffing | gera tentativas × reutiliza credenciais vazadas |
| DoS | DDoS | uma ou poucas origens lógicas × muitas origens distribuídas |
| firewall | IDS | controla fluxo × detecta e alerta |
| IDS | IPS | fora de banda/alerta × em linha/prevenção |
| DMZ | rede interna | exposição controlada × ativos internos restritos |
| VPN | TLS de aplicação | túnel de escopo amplo × proteção de protocolo/aplicação |
| VLAN | firewall interno | separação de camada 2 × aplicação de política inclusive ao movimento lateral roteado |
| cifra simétrica | assimétrica | segredo compartilhado e eficiência × par de chaves |
| hash | criptografia | resumo unidirecional × transformação reversível com chave |
| hash | HMAC | sem segredo × autenticação com segredo compartilhado |
| HMAC | assinatura digital | segredo compartilhado × chave privada verificável por pública |
| assinatura | certificado | prova sobre dado × vínculo identidade-chave |
| TLS | HTTPS | canal seguro genérico × HTTP sobre TLS |
| WPA2-Personal | WPA3-Personal | autenticação baseada em PSK × troca autenticada por senha com SAE |
| backup | redundância | recuperar passado × manter componente alternativo |
| RPO | RTO | ponto temporal objetivo para recuperar dados × prazo objetivo para restabelecer serviço |

## Revisão fixa do Dia 4

<a id="rf4-visao-geral"></a>

Este bloco sustenta as **20 questões extras do Dia 4**: dez de Administração Pública, cinco de Raciocínio Lógico-Matemático e cinco de Língua Portuguesa. Os identificadores `RF4-ADM-01` a `RF4-PT-05` são estáveis e devem ser usados nos comentários das questões. Assim, o comentário deve indicar, por exemplo, **“Revisão fixa do Dia 4 — RF4-ADM-06: anulação, revogação, convalidação e decadência”**, em vez de empregar uma referência genérica à teoria.

### Como distinguir revisão e aprofundamento

- **[S1 — revisão ativa]**: conteúdo já estudado na Semana 1. Aqui ele reaparece de forma condensada, com recuperação da regra, contraste entre conceitos próximos e aplicação a casos. O conhecimento anterior necessário é a definição básica do instituto indicado.
- **[S2 — aprofundamento]**: detalhe, exceção, fundamento legal ou aplicação que recebe explicação adicional nesta semana e pode ser cobrado nas questões extras.
- Quando as duas marcas aparecem juntas, a definição central vem da Semana 1, mas o alcance da regra ou a resolução do caso é aprofundado na Semana 2.

### Roteiro dos tópicos estudados

| Faixa | Disciplina | Conteúdo deste bloco |
|---|---|---|
| `RF4-ADM-01` a `RF4-ADM-10` | Administração Pública | LIMPE; publicidade institucional; órgão e entidade; Administração Direta e Indireta; autarquia; elementos e atributos do ato; anulação, revogação, convalidação e decadência; LAI e LGPD; improbidade; licitações, modalidades, dispensa e inexigibilidade; responsabilidade civil do Estado e regresso |
| `RF4-RLM-01` a `RF4-RLM-05` | RLM | negações de conectivos e quantificadores; inclusão-exclusão; porcentagem reversa; proporção direta e inversa |
| `RF4-PT-01` a `RF4-PT-05` | Português | conectores; inferência; referência; concordância de `haver` e `existir`; pontuação; crase; reescrita e clareza |

---

### Administração Pública — 10 questões extras

<a id="rf4-adm-01"></a>

#### RF4-ADM-01 — Princípios do art. 37: LIMPE

**Origem:** **[S1 — revisão ativa]** significado básico dos cinco princípios. **[S2 — aprofundamento]** aplicação conjunta e limites de eficiência e publicidade.

O caput do art. 37 da Constituição submete a Administração Pública direta e indireta de todos os Poderes e entes federativos aos princípios da **legalidade, impessoalidade, moralidade, publicidade e eficiência** — o conhecido acrônimo **LIMPE**.

| Princípio | Regra operacional | Aplicação típica | Pegadinha |
|---|---|---|---|
| Legalidade | o agente público atua nos limites autorizados pelo ordenamento | conceder vantagem apenas se houver fundamento normativo | a Administração não tem a mesma liberdade do particular |
| Impessoalidade | a atuação busca a finalidade pública, sem favorecimento, perseguição ou promoção pessoal | critérios objetivos para atendimento e seleção | impessoalidade não significa anonimato do agente nem ausência de autoria |
| Moralidade | a conduta deve ser juridicamente ética, leal e de boa-fé | impedir expediente formalmente aparente, mas desleal | moralidade administrativa não é mera moral privada |
| Publicidade | os atos devem ser transparentes, salvo sigilo legalmente justificável | divulgar decisão e permitir controle | publicidade não torna público todo dado pessoal e não elimina sigilos legais |
| Eficiência | a Administração deve buscar qualidade, produtividade e bom uso dos recursos | simplificar fluxo sem perder controles necessários | eficiência não autoriza desobedecer à lei |

Os princípios devem ser aplicados **em conjunto**. Uma solução rápida, mas ilegal, viola a legalidade; uma divulgação ampla, mas com exposição desnecessária de dados pessoais, pode contrariar a proteção de dados; uma decisão formalmente legal, mas tomada para perseguir alguém, ofende a impessoalidade e a finalidade.

**Exemplo resolvido.** Um gestor elimina uma etapa exigida por lei para concluir uma contratação mais depressa e invoca a eficiência. A justificativa não procede: eficiência orienta a melhor atuação **dentro da legalidade**, não afasta requisito legal.

**Diferenças decisivas:**

- legalidade pergunta **“há autorização jurídica para agir?”**;
- moralidade pergunta **“a conduta é leal, proba e compatível com a ética administrativa?”**;
- impessoalidade pergunta **“o ato atende à finalidade pública sem promoção, perseguição ou favoritismo?”**;
- publicidade pergunta **“o ato pode ser conhecido e controlado, respeitados os sigilos legais?”**;
- eficiência pergunta **“o resultado foi buscado com qualidade e uso adequado dos recursos?”**.

<a id="rf4-adm-02"></a>

#### RF4-ADM-02 — Publicidade institucional e vedação à promoção pessoal

**Origem:** **[S1 — revisão ativa]** impessoalidade e publicidade. **[S2 — aprofundamento]** conteúdo específico do art. 37, § 1º, da Constituição.

Segundo o art. 37, § 1º, a publicidade de atos, programas, obras, serviços e campanhas dos órgãos públicos deve ter caráter **educativo, informativo ou de orientação social**. Ela não pode conter nomes, símbolos ou imagens que caracterizem **promoção pessoal de autoridades ou servidores públicos**.

A regra não proíbe toda identificação institucional. Brasão, nome do órgão, canal oficial e informações necessárias podem aparecer. O que se veda é utilizar a comunicação custeada ou produzida pelo poder público para construir prestígio pessoal do agente.

**Exemplo resolvido.** Uma campanha de vacinação apresenta datas, locais, público-alvo, brasão do município e telefone da secretaria. Seu caráter é informativo. Se o material destaca foto, nome e slogan pessoal do prefeito com finalidade promocional, surge ofensa ao art. 37, § 1º, ainda que a campanha trate de serviço real.

**Pegadinhas:**

- publicidade institucional não se confunde com propaganda eleitoral;
- a informação pode ser verdadeira e, mesmo assim, assumir caráter de promoção pessoal;
- a proibição alcança promoção de **autoridade ou servidor**, não apenas de agente eleito;
- transparência e publicidade não autorizam expor dado protegido por sigilo ou sem necessidade.

<a id="rf4-adm-03"></a>

#### RF4-ADM-03 — Órgão, entidade, Administração Direta, Indireta e autarquia

**Origem:** **[S1 — revisão ativa]** Direta e Indireta. **[S2 — aprofundamento]** personalidade jurídica, desconcentração, descentralização e regime da autarquia.

**Órgão** é um centro de competências integrado à estrutura de uma pessoa jurídica. Em regra, não tem personalidade jurídica própria: sua atuação é imputada à entidade a que pertence. Ministério, secretaria e departamento são exemplos usuais.

**Entidade administrativa** é a pessoa jurídica que integra a organização administrativa e possui personalidade própria, patrimônio e capacidade para assumir direitos e obrigações nos limites de sua lei instituidora.

| Estrutura | Composição | Personalidade própria? | Exemplo típico |
|---|---|---:|---|
| Administração Direta | órgãos da União, dos estados, do Distrito Federal e dos municípios | os órgãos, não; a pessoa política, sim | ministério ou secretaria estadual |
| Administração Indireta | autarquias, fundações públicas, empresas públicas e sociedades de economia mista | sim | autarquia federal |

A criação de órgãos dentro da mesma pessoa jurídica representa **desconcentração**: distribuem-se competências internamente, sem criar nova pessoa. A atribuição de atividade a outra pessoa — jurídica ou, nas hipóteses admitidas pelo ordenamento, física — representa **descentralização**.

**Autarquia** é pessoa jurídica de direito público integrante da Administração Indireta, criada diretamente por lei específica para desempenhar atividade típica de Estado de modo descentralizado. Possui patrimônio e capacidade administrativa próprios, mas permanece vinculada à Administração Direta para controle finalístico; **vinculação não é subordinação hierárquica**.

Pelo art. 37, XIX, da Constituição, a autarquia é **criada por lei específica**. Para empresa pública, sociedade de economia mista e fundação, a lei específica **autoriza a instituição**; no caso da fundação, cabe à lei complementar definir as áreas de sua atuação. A diferença entre criação e autorização é frequente em prova.

**Exemplo resolvido.** Um ministério cria dois departamentos para dividir funções: houve desconcentração, pois continuam dentro da União. Uma lei cria uma autarquia com personalidade própria para executar atividade administrativa: houve descentralização e formação de entidade da Administração Indireta.

**Diferenças decisivas:**

- órgão × entidade: centro de competência sem personalidade própria × pessoa jurídica;
- Direta × Indireta: pessoas políticas e seus órgãos × entidades administrativas vinculadas;
- desconcentração × descentralização: repartição interna × atribuição da atividade a outra pessoa jurídica ou, conforme a hipótese legal, física;
- subordinação × vinculação: hierarquia interna × controle finalístico sem hierarquia entre as pessoas.

<a id="rf4-adm-04"></a>

#### RF4-ADM-04 — Elementos do ato administrativo

**Origem:** **[S1 — revisão ativa]** lista dos elementos. **[S2 — aprofundamento]** distinção entre motivo e motivação e identificação do vício.

Os cinco elementos clássicos do ato administrativo são **competência, finalidade, forma, motivo e objeto**.

| Elemento | Pergunta de controle | Exemplo de vício |
|---|---|---|
| Competência | quem tinha poder legal para praticar o ato? | autoridade sem atribuição aplica sanção |
| Finalidade | para qual fim público previsto o poder foi conferido? | remoção usada para perseguir servidor |
| Forma | qual exteriorização ou procedimento a lei exige? | ato oral quando a lei exige forma escrita |
| Motivo | quais fatos e fundamentos jurídicos sustentam o ato? | punição baseada em fato inexistente |
| Objeto | qual efeito jurídico o ato produz? | ordem de conteúdo proibido pela lei |

**Motivo** é a situação de fato e de direito que fundamenta o ato. **Motivação** é a exposição desses motivos. Um motivo pode existir no mundo dos fatos, mas a decisão deixar de explicá-lo quando a lei exige motivação; inversamente, uma motivação escrita pode mencionar fato inexistente, tornando defeituoso o suporte do ato.

Competência e finalidade são, em regra, vinculadas. Nem todo vício de competência é sanável: competência **exclusiva** não pode ser delegada nem convalidada. A forma pode ser sanável quando não for essencial e quando a correção não prejudicar o interesse público ou terceiros.

**Exemplo resolvido.** A autoridade competente aplica multa prevista em lei, mas afirma que houve inspeção em data na qual nenhuma inspeção ocorreu. O problema central está no **motivo**, porque o fato invocado é inexistente.

**Pegadinhas:**

- finalidade não é o resultado material imediato; esse resultado pertence ao objeto;
- motivo não é sinônimo de motivação;
- discricionariedade não elimina competência, finalidade e controle de legalidade;
- a lista `competência, finalidade, forma, motivo e objeto` trata de elementos, não de atributos.

<a id="rf4-adm-05"></a>

#### RF4-ADM-05 — Atributos do ato administrativo

**Origem:** **[S1 — revisão ativa]** presunção de legitimidade. **[S2 — aprofundamento]** imperatividade, autoexecutoriedade, tipicidade e ausência de universalidade dos atributos.

Os atributos mais cobrados são:

- **presunção de legitimidade e de veracidade:** presume-se, de forma relativa, que o ato está conforme o direito e que os fatos declarados pela Administração são verdadeiros. Por ser presunção `juris tantum`, admite prova em contrário;
- **imperatividade:** o ato pode impor obrigação independentemente da concordância do destinatário. Não está presente em todo ato, como nos atos meramente enunciativos ou em certos atos negociais;
- **autoexecutoriedade:** em hipóteses autorizadas por lei ou diante de situação urgente admitida pelo ordenamento, a Administração pode executar materialmente a decisão sem ordem judicial prévia. Não significa liberdade para agir sem base jurídica;
- **tipicidade:** o ato deve corresponder a figura prevista no ordenamento, impedindo que a Administração invente unilateralmente espécies de atos e efeitos sem base legal.

**Exemplo resolvido.** A Administração interdita imediatamente instalação que apresenta perigo grave, quando a lei autoriza a medida. A execução sem autorização judicial prévia evidencia autoexecutoriedade. Se apenas emite certidão que informa situação existente, não se deve presumir imperatividade, pois a certidão não impõe obrigação ao particular.

**Diferenças decisivas:**

- imperatividade × autoexecutoriedade: **impor obrigação** × **executar materialmente sem ordem judicial prévia**;
- legitimidade × veracidade: conformidade jurídica do ato × veracidade dos fatos declarados;
- presunção relativa × certeza absoluta: o ato produz efeitos desde logo, mas pode ser impugnado e invalidado;
- atributo × elemento: qualidade do ato × componente necessário à sua formação.

<a id="rf4-adm-06"></a>

#### RF4-ADM-06 — Anulação, revogação, convalidação e art. 54 da Lei nº 9.784/1999

**Origem:** **[S1 — revisão ativa]** ilegalidade × mérito. **[S2 — aprofundamento]** arts. 53 a 55, decadência quinquenal, efeitos e limites da convalidação.

A Lei nº 9.784/1999 estabelece, no âmbito federal:

- **art. 53:** a Administração **deve anular** seus atos com vício de legalidade e **pode revogar** atos por conveniência ou oportunidade, respeitados os direitos adquiridos;
- **art. 54:** o direito de anular atos dos quais decorram efeitos favoráveis aos destinatários decai em **cinco anos**, contados da prática do ato, salvo comprovada má-fé;
- **art. 54, § 1º:** em efeitos patrimoniais contínuos, o prazo conta da percepção do primeiro pagamento;
- **art. 54, § 2º:** qualquer medida de autoridade administrativa que importe impugnação à validade do ato constitui exercício do direito de anular;
- **art. 55:** defeitos sanáveis podem ser convalidados pela própria Administração quando a correção não lesar o interesse público nem prejudicar terceiros.

| Instituto | Causa | Natureza do ato atingido | Efeito temporal típico | Quem pratica/decide |
|---|---|---|---|---|
| Anulação | ilegalidade | ato inválido | em regra, retroativo (`ex tunc`), com proteção cabível à boa-fé | Administração e Poder Judiciário, quando provocado |
| Revogação | conveniência ou oportunidade | ato válido, mas não mais conveniente | prospectivo (`ex nunc`) | Administração, no exercício do mérito administrativo |
| Convalidação | defeito sanável | ato corrigível | em regra, retroage para preservar efeitos válidos | Administração, atendidos os requisitos legais |

A revogação não serve para corrigir ilegalidade e não cabe ao Judiciário revogar ato administrativo de outro Poder com base em mérito. Atos vinculados não são revogados por conveniência; também devem ser observados direitos adquiridos, atos consumados e outras limitações reconhecidas pelo ordenamento.

Em abordagem de prova, vícios de **competência não exclusiva** e de **forma não essencial** são os exemplos clássicos de defeitos potencialmente convalidáveis. Vício de finalidade, motivo ou objeto normalmente não é tratado como sanável. Mesmo um defeito formalmente corrigível não pode ser convalidado se houver lesão ao interesse público ou prejuízo a terceiro.

**Exemplo resolvido 1.** Um ato válido deixou de ser útil para a Administração e ainda pode ser retirado sem violar direito adquirido. O fundamento é mérito administrativo: cabe **revogação**, com efeitos prospectivos.

**Exemplo resolvido 2.** A Administração descobre, após seis anos, irregularidade em ato favorável cujo destinatário agiu de boa-fé. Aplica-se a decadência do art. 54; não se pode responder automaticamente que “todo ato ilegal deve ser anulado a qualquer tempo”. Se houver má-fé comprovada, a ressalva legal altera a conclusão.

**Pegadinhas:**

- `deve anular` × `pode revogar`;
- cinco anos é prazo referente ao direito administrativo de anular **ato favorável**, ressalvada má-fé, e não regra universal sobre qualquer ato;
- convalidação não é perdão irrestrito de ilegalidade;
- anulação controla legalidade; revogação controla mérito;
- a existência de ilegalidade não transforma revogação em instrumento adequado.

<a id="rf4-adm-07"></a>

#### RF4-ADM-07 — LAI e LGPD: transparência com proteção de dados

**Origem:** **[S1 — revisão ativa]** publicidade como regra e proteção de dados. **[S2 — aprofundamento]** compatibilização prática entre LAI e LGPD.

A Lei de Acesso à Informação — **Lei nº 12.527/2011 (LAI)** — adota, entre suas diretrizes do art. 3º, a publicidade como preceito geral e o sigilo como exceção, a divulgação de informações de interesse público independentemente de solicitação e o estímulo ao controle social.

A **LGPD — Lei nº 13.709/2018** — disciplina o tratamento de dados pessoais, inclusive pelo poder público. Entre os princípios do art. 6º estão finalidade, adequação, necessidade, livre acesso, qualidade, transparência, segurança, prevenção, não discriminação e responsabilização/prestação de contas. Pelo art. 23, o tratamento pelo poder público deve atender à finalidade pública e à persecução do interesse público, com o objetivo de executar competências legais ou cumprir atribuições legais do serviço público, observadas as exigências de transparência próprias. O art. 7º, § 3º, determina que o tratamento de dados pessoais cujo acesso seja público considere a finalidade, a boa-fé e o interesse público que justificaram sua disponibilização.

As duas leis são **compatíveis**. A pergunta correta não é “qual delas sempre vence?”, mas:

1. a informação possui interesse público e há dever jurídico de transparência?
2. há dado pessoal ou dado pessoal sensível envolvido?
3. qual é a finalidade concreta da divulgação ou do tratamento?
4. todos os dados divulgados são necessários para essa finalidade?
5. existe hipótese legal de restrição, sigilo, anonimização ou acesso limitado?

O art. 31, § 1º, I, da LAI determina que informações pessoais relativas à intimidade, vida privada, honra e imagem tenham acesso restrito, independentemente de classificação de sigilo, pelo prazo máximo de **100 anos a contar da data de sua produção**, a agentes públicos legalmente autorizados e à pessoa a que se referem, ressalvadas as hipóteses legais de divulgação ou acesso. Isso não significa que todo documento que contenha algum dado pessoal seja integralmente secreto: quando não for autorizado acesso integral por existir parte sigilosa, o art. 7º, § 2º, assegura acesso à parte não sigilosa por certidão, extrato ou cópia com ocultação do trecho protegido.

**Exemplo resolvido.** Para demonstrar a execução de um contrato, o órgão pode divulgar objeto, valor e fornecedor conforme o dever de transparência. A publicação indiscriminada de CPF completo, telefone particular e endereço residencial de pessoas vinculadas ao processo exige finalidade e necessidade específicas; se esses campos não forem necessários, devem ser protegidos ou tarjados.

**Diferenças decisivas:**

- transparência ativa × passiva: divulgação por iniciativa do órgão × resposta a pedido;
- informação pública × dado pessoal: conteúdo sujeito ao controle social × informação relacionada a pessoa natural identificada ou identificável;
- dado pessoal × dado pessoal sensível: categoria geral × dado sobre origem racial ou étnica, convicção religiosa, opinião política, **filiação a sindicato ou a organização de caráter religioso, filosófico ou político**, dado referente à saúde ou à vida sexual e dado genético ou biométrico, quando vinculado a uma pessoa natural;
- sigilo × ocultação parcial: restrição do acesso ao conteúdo protegido × fornecimento do restante após resguardo do campo protegido.

**Pegadinhas:**

- LGPD não revogou a LAI;
- LAI não torna todo dado mantido pelo Estado automaticamente público;
- dado acessível publicamente continua sujeito a finalidade, boa-fé e demais princípios aplicáveis;
- transparência não é autorização para coleta ou exposição ilimitada;
- negar todo o documento quando apenas parte é protegida pode ser medida excessiva.

<a id="rf4-adm-08"></a>

#### RF4-ADM-08 — Improbidade administrativa

**Origem:** **[S1 — revisão ativa]** distinção entre ilegalidade e improbidade. **[S2 — aprofundamento]** dolo e categorias dos arts. 9º, 10 e 11 após a Lei nº 14.230/2021.

Nos termos do art. 1º, §§ 1º a 3º, da Lei nº 8.429/1992, consideram-se atos de improbidade as **condutas dolosas tipificadas** nos arts. 9º, 10 e 11, ressalvados tipos previstos em leis especiais. Dolo é a vontade livre e consciente de alcançar o resultado ilícito tipificado; a mera voluntariedade do agente não basta. O simples exercício da função, sem comprovação de ato doloso com fim ilícito, afasta a responsabilidade por improbidade.

As três categorias centrais são:

| Dispositivo | Categoria | Núcleo para reconhecer em prova |
|---|---|---|
| art. 9º | enriquecimento ilícito | vantagem patrimonial indevida em razão da função |
| art. 10 | prejuízo ao erário | ação ou omissão dolosa com perda patrimonial efetiva e comprovada |
| art. 11 | atentado contra princípios da Administração | ação ou omissão dolosa enquadrada nas condutas legalmente tipificadas |

Para as condutas do art. 11, seu § 1º acrescenta requisito específico: somente haverá improbidade administrativa quando ficar comprovado, na conduta funcional do agente público, o **fim de obter proveito ou benefício indevido para si ou para outra pessoa ou entidade**.

Uma ilegalidade pode gerar anulação do ato, responsabilidade disciplinar, ressarcimento ou outra consequência e, ainda assim, não preencher o tipo de improbidade. É indispensável identificar **conduta tipificada, dolo exigido e demais requisitos da categoria**. Também é erro concluir que todo prejuízo financeiro decorre necessariamente de improbidade: o art. 10 exige, além do dolo, lesão efetiva e comprovada ao erário.

**Exemplo resolvido.** Um servidor comete falha procedimental por desatenção, sem vontade consciente de alcançar resultado ilícito. O fato pode demandar correção e apuração em outras esferas, mas não deve ser qualificado automaticamente como improbidade, porque a lei exige conduta dolosa tipificada.

**Pegadinhas:**

- improbidade não é sinônimo de mera ilegalidade;
- voluntariedade não equivale ao dolo definido pela lei;
- dano presumido não substitui a perda efetiva e comprovada exigida no art. 10;
- as categorias dos arts. 9º, 10 e 11 não devem ser trocadas: vantagem pessoal, prejuízo patrimonial e atentado tipificado a princípios têm núcleos diferentes;
- a resolução da questão exige examinar todos os requisitos, não apenas afirmar que a conduta “parece imoral”.

<a id="rf4-adm-09"></a>

#### RF4-ADM-09 — Modalidades, dispensa e inexigibilidade na Lei nº 14.133/2021

**Origem:** **[S1 — revisão ativa]** licitação como regra e contratação direta como exceção legal. **[S2 — aprofundamento]** modalidades atuais, critério para o pregão e instrução da contratação direta.

O art. 28 da Lei nº 14.133/2021 prevê cinco modalidades: **pregão, concorrência, concurso, leilão e diálogo competitivo**.

| Modalidade | Uso característico | Critério(s) de julgamento vinculado(s) pela lei | Pegadinha |
|---|---|---|---|
| Pregão | aquisição de bens e serviços comuns, inclusive serviço comum de engenharia, quando os padrões de desempenho e qualidade podem ser definidos objetivamente por especificações usuais de mercado | menor preço ou maior desconto | modalidade não é definida apenas pelo valor; não se aplica a serviço técnico especializado de natureza predominantemente intelectual nem a obra, ressalvado o serviço comum de engenharia |
| Concorrência | contratação de bens e serviços especiais e de obras e serviços comuns ou especiais de engenharia, nos termos legais | menor preço; melhor técnica ou conteúdo artístico; técnica e preço; maior retorno econômico; ou maior desconto, conforme o art. 6º, XXXVIII | não é modalidade reservada apenas a contratos de “alto valor” |
| Concurso | escolha de trabalho técnico, científico ou artístico, com prêmio ou remuneração | melhor técnica ou conteúdo artístico | não é concurso para provimento de cargo público |
| Leilão | alienação de bens imóveis ou de bens móveis inservíveis ou legalmente apreendidos | maior lance | não confundir com pregão |
| Diálogo competitivo | contratação complexa na qual a Administração dialoga com licitantes previamente selecionados para desenvolver alternativa capaz de atender à necessidade, antes das propostas finais | critérios divulgados no início da fase competitiva, nos termos do art. 32 | não é conversa informal que substitui edital ou competição |

`Convite` e `tomada de preços` não integram o rol de modalidades da Lei nº 14.133/2021. Também não se deve confundir **modalidade** com **critério de julgamento**: menor preço, maior desconto, melhor técnica ou conteúdo artístico, técnica e preço, maior lance e maior retorno econômico são critérios do art. 33, não modalidades. A lei, porém, vincula cada modalidade aos critérios cabíveis: no pregão, menor preço ou maior desconto; no concurso, melhor técnica ou conteúdo artístico; no leilão, maior lance; e, na concorrência, os critérios enumerados no art. 6º, XXXVIII.

Há **contratação direta** quando a lei admite que o contrato seja celebrado sem licitação, mas isso não significa contratação sem processo.

- **Inexigibilidade (art. 74):** a competição é inviável. O artigo apresenta hipóteses como fornecedor exclusivo, profissional do setor artístico consagrado, determinados serviços técnicos especializados de natureza predominantemente intelectual com profissional ou empresa de notória especialização, credenciamento e aquisição ou locação de imóvel cujas características e localização tornem necessária a escolha. A lista é exemplificativa, pois o núcleo é a inviabilidade de competição.
- **Dispensa (art. 75):** decorre de **hipótese taxativa** e, em regra, a competição seria viável em tese, mas a lei autoriza a contratação direta, como em determinadas contratações de pequeno valor, emergência ou calamidade e nas demais situações expressamente previstas. Os limites monetários são atualizados periodicamente; uma questão deve indicar o valor vigente ou concentrar-se na estrutura jurídica.

O processo de contratação direta deve ser instruído conforme o art. 72, com documentos como formalização da demanda e, quando cabíveis, estudos, análise de riscos, termo de referência/projeto, estimativa de despesa, pareceres, demonstração de recursos orçamentários, comprovação de habilitação, razão da escolha do contratado, justificativa de preço e autorização da autoridade competente. O ato autorizador ou extrato deve ser divulgado e mantido à disposição do público em sítio eletrônico oficial.

**Exemplo resolvido 1.** Vários fornecedores conseguem entregar bem comum com especificações usuais de mercado. Não há inviabilidade de competição; a regra é licitar, e o pregão é a modalidade apropriada quando presentes seus requisitos.

**Exemplo resolvido 2.** Só há um fornecedor capaz de atender, e a exclusividade é adequadamente demonstrada. O fundamento pode ser inexigibilidade, porque falta viabilidade de competição; ainda assim, devem existir processo, justificativa de preço e razão da escolha.

**Exemplo resolvido 3.** Uma emergência real enquadra-se em hipótese taxativa de dispensa. A urgência não elimina planejamento mínimo, motivação, pesquisa/justificativa de preço, habilitação exigível nem limite do objeto ao necessário para enfrentar a situação.

**Diferenças decisivas:**

- dispensa × inexigibilidade: hipótese taxativa em que, em regra, a competição seria viável em tese × competição inviável;
- licitação dispensada × dispensável: a primeira expressão refere-se às hipóteses de alienação do art. 76; a segunda, às hipóteses taxativas do art. 75;
- modalidade × critério: procedimento competitivo escolhido × método de julgamento da proposta;
- pregão × leilão: contratação de bem/serviço comum × alienação pelo maior lance;
- contratação direta × ausência de procedimento: contratação sem licitação × ilegal supressão da instrução.

<a id="rf4-adm-10"></a>

#### RF4-ADM-10 — Responsabilidade civil objetiva do Estado e direito de regresso

**Origem:** **[S1 — revisão ativa]** teoria do risco administrativo. **[S2 — aprofundamento]** requisitos, causas que interferem no nexo e responsabilidade regressiva do agente.

O art. 37, § 6º, da Constituição dispõe que as pessoas jurídicas de direito público e as pessoas jurídicas de direito privado prestadoras de serviços públicos respondem pelos danos que seus agentes, **nessa qualidade**, causarem a terceiros, assegurado o direito de regresso contra o agente nos casos de **dolo ou culpa**.

Na responsabilidade objetiva, a vítima deve demonstrar, em síntese:

1. conduta administrativa atribuível ao agente nessa qualidade;
2. dano;
3. nexo causal entre a conduta e o dano.

Não se exige da vítima prova de culpa do agente para responsabilizar a pessoa jurídica. Isso não transforma o Estado em segurador universal: se o nexo causal for rompido por culpa exclusiva da vítima, fato exclusivo de terceiro ou caso fortuito/força maior inteiramente estranho à atuação estatal, a responsabilidade pode ser afastada; se houver contribuição concorrente da vítima, a indenização pode ser reduzida conforme o caso. Essa é a lógica da **teoria do risco administrativo**, distinta do risco integral.

A relação regressiva tem outra estrutura: depois de suportar a reparação, a pessoa jurídica pode buscar o ressarcimento do agente se demonstrar **dolo ou culpa**. Logo:

- Estado perante a vítima: responsabilidade objetiva, presentes dano e nexo;
- agente perante o Estado, em regresso: responsabilidade subjetiva, dependente de dolo ou culpa.

**Exemplo resolvido.** Motorista de autarquia, em serviço, causa acidente e dano a terceiro. A vítima não precisa provar culpa do motorista para acionar a pessoa jurídica, mas deve provar dano e nexo com a atuação funcional. Para obter regressivamente do agente o valor pago, a entidade deverá demonstrar dolo ou culpa dele.

**Pegadinhas:**

- objetiva não significa automática;
- a Constituição menciona pessoas privadas **prestadoras de serviço público**, não toda empresa que contrata com o Estado;
- o regresso não é objetivo: exige dolo ou culpa;
- dano sem nexo causal não basta;
- risco administrativo admite causas que afastam ou atenuam a responsabilidade; risco integral é excepcional.

---

### Raciocínio Lógico-Matemático — 5 questões extras

<a id="rf4-rlm-01"></a>

#### RF4-RLM-01 — Negação de conjunção e disjunção

**Origem:** **[S1 — revisão ativa]** conectivos `e`/`ou`. **[S2 — aprofundamento]** aplicação das leis de De Morgan sem trocar indevidamente o quantificador lógico.

Pelas leis de De Morgan:

- negação de `P e Q`: `não P ou não Q`;
- negação de `P ou Q`: `não P e não Q`.

Ao negar, troca-se `e` por `ou` — ou `ou` por `e` — e nega-se **cada parcela**.

**Exemplo resolvido.** Negar “o firewall está ativo **e** os registros estão íntegros” produz “o firewall não está ativo **ou** os registros não estão íntegros”. Basta uma das condições falhar para que a conjunção original seja falsa.

**Pegadinha:** a negação de `P e Q` não é `não P e não Q`. Essa última afirma que ambas falham e é mais forte do que a negação correta.

<a id="rf4-rlm-02"></a>

#### RF4-RLM-02 — Negação da condicional e de quantificadores

**Origem:** **[S1 — revisão ativa]** estrutura `se... então`. **[S2 — aprofundamento]** testemunho lógico e quantificadores.

A proposição `se P, então Q` só é falsa quando `P` é verdadeira e `Q` é falsa. Por isso:

- negação de `P → Q`: `P e não Q`;
- negação de “todo A é B”: “existe pelo menos um A que não é B”;
- negação de “existe algum A que é B”: “nenhum A é B” ou “não existe A que seja B”;
- negação de “nenhum A é B”: “existe pelo menos um A que é B”.

**Exemplo resolvido 1.** A negação de “se o incidente é crítico, então a equipe aciona o plano” é “o incidente é crítico **e** a equipe não aciona o plano”. Não basta inverter a ordem nem escrever outra condicional.

**Exemplo resolvido 2.** A negação de “todos os 40 relatórios foram assinados” é “pelo menos um dos 40 relatórios não foi assinado”. Não é necessário afirmar que nenhum foi assinado.

**Pegadinhas:**

- negar “todo” produz “existe ao menos um... não”; não produz “nenhum”;
- a contrapositiva `não Q → não P` é equivalente à condicional, não sua negação;
- “algum” em lógica significa “pelo menos um”, não necessariamente “apenas um”.

<a id="rf4-rlm-03"></a>

#### RF4-RLM-03 — Princípio da inclusão-exclusão

**Origem:** **[S1 — revisão ativa]** união de dois conjuntos. **[S2 — aprofundamento]** cálculo de somente um grupo, nenhum grupo e validação do total.

Para dois conjuntos `A` e `B`:

`n(A ∪ B) = n(A) + n(B) - n(A ∩ B)`.

A interseção é subtraída uma vez porque foi contada em `A` e novamente em `B`.

**Exemplo resolvido.** Entre 80 servidores, 46 fizeram o curso A, 38 fizeram o curso B e 14 fizeram ambos.

1. Pelo menos um: `46 + 38 - 14 = 70`.
2. Somente A: `46 - 14 = 32`.
3. Somente B: `38 - 14 = 24`.
4. Exatamente um: `32 + 24 = 56`.
5. Nenhum: `80 - 70 = 10`.

**Verificação:** `32` somente A + `24` somente B + `14` ambos + `10` nenhum = `80`.

**Pegadinhas:**

- “pelo menos um” inclui a interseção;
- “exatamente um” exclui quem pertence aos dois;
- “somente A” é `A - interseção`, não `A - B total`;
- o cálculo de “nenhum” exige conhecer o universo.

<a id="rf4-rlm-04"></a>

#### RF4-RLM-04 — Porcentagem reversa e variações sucessivas

**Origem:** **[S1 — revisão ativa]** cálculo direto de porcentagem. **[S2 — aprofundamento]** recuperação do valor original e composição de taxas.

Se um valor inicial `V` sofre aumento de `p%`, o valor final é `V × (1 + p)`, com `p` escrito em forma decimal. Se sofre desconto de `p%`, o final é `V × (1 - p)`.

Para recuperar o valor original, **divide-se pelo fator**, em vez de aplicar a taxa inversa sobre o valor final.

**Exemplo resolvido 1 — desconto reverso.** Após desconto de 15%, um item custa R$ 340,00.

`final = inicial × 0,85`

`inicial = 340 / 0,85 = 400`

Somar 15% de R$ 340,00 produziria R$ 391,00 e estaria errado, porque a base do desconto era R$ 400,00.

**Exemplo resolvido 2 — aumento reverso.** Após aumento de 20%, um valor chega a 600.

`inicial = 600 / 1,20 = 500`.

**Exemplo resolvido 3 — taxas sucessivas.** Um valor de 1.000 aumenta 10% e depois diminui 10%:

`1.000 × 1,10 × 0,90 = 990`.

O resultado representa queda líquida de 1%, pois as porcentagens incidem sobre bases diferentes.

**Pegadinhas:**

- para desfazer desconto de 20%, dividir por `0,80`; não aumentar o final em 20%;
- taxas sucessivas são multiplicadas por fatores, não simplesmente somadas;
- aumento e desconto de mesma taxa não se anulam, salvo taxa zero;
- identifique sempre a base sobre a qual a porcentagem incide.

<a id="rf4-rlm-05"></a>

#### RF4-RLM-05 — Proporção direta, inversa e produtividade

**Origem:** **[S1 — revisão ativa]** regra de três. **[S2 — aprofundamento]** grandezas compostas e teste da direção da proporcionalidade.

Duas grandezas são **diretamente proporcionais** quando uma aumenta e a outra, mantidas as demais condições, aumenta na mesma razão. São **inversamente proporcionais** quando uma aumenta e a outra diminui na razão inversa.

Em problemas de produção uniforme:

`produção = trabalhadores × tempo × produtividade por trabalhador-tempo`.

**Exemplo resolvido 1 — relação direta.** Três técnicos, em quatro horas, processam 36 solicitações. A produtividade é:

`36 / (3 × 4) = 3 solicitações por técnico-hora`.

Seis técnicos, em cinco horas, processarão:

`6 × 5 × 3 = 90 solicitações`.

**Exemplo resolvido 2 — relação inversa.** Oito técnicos concluem uma tarefa em seis dias. Com a mesma produtividade e carga diária, quantos dias seriam necessários para 12 técnicos?

O trabalho total equivale a `8 × 6 = 48 técnicos-dia`.

`dias = 48 / 12 = 4`.

Mais técnicos implicam menos dias: a relação é inversa.

**Roteiro de cálculo:**

1. identifique o resultado pedido;
2. mantenha constantes as condições não mencionadas;
3. decida se cada grandeza é direta ou inversa em relação ao resultado;
4. calcule por taxa unitária ou produto constante;
5. verifique se a direção do resultado faz sentido.

**Pegadinhas:**

- mais trabalhadores só aumentam a produção se o tempo for mantido; para trabalho fixo, mais trabalhadores reduzem o tempo;
- a proporcionalidade pressupõe produtividade constante;
- não inverta automaticamente todas as razões de uma regra de três composta;
- unidade incompatível — horas de um lado e dias do outro — deve ser convertida antes do cálculo.

---

### Língua Portuguesa — 5 questões extras

<a id="rf4-pt-01"></a>

#### RF4-PT-01 — Conectores e relações de sentido

**Origem:** **[S1 — revisão ativa]** relações básicas entre orações. **[S2 — aprofundamento]** substituição de conectores com preservação do sentido.

Conectores orientam a relação lógica entre trechos. A substituição só preserva o sentido quando mantém essa relação e se ajusta à construção sintática.

| Relação | Conectores frequentes | Exemplo |
|---|---|---|
| adição | `e`, `além disso`, `bem como` | o sistema registra **e** alerta |
| oposição/adversidade | `mas`, `porém`, `contudo`, `entretanto` | o controle existe, **mas** falhou |
| concessão | `embora`, `ainda que`, `mesmo que` | **embora** houvesse alerta, a equipe não agiu |
| causa | `porque`, `já que`, `visto que` | o acesso foi bloqueado **porque** excedeu o limite |
| consequência/conclusão | `portanto`, `por isso`, `logo`, `pois` deslocado ou posposto ao verbo | houve vazamento; iniciou-se, **pois**, a resposta |
| condição | `se`, `caso`, `desde que` | o acesso será liberado **se** houver autorização |
| finalidade | `para`, `a fim de que` | segmentou-se a rede **para** reduzir o risco |
| explicação | `porque`, `que`, `pois` antes do verbo da oração que introduz | revise o registro, **pois** há inconsistência |

**Exemplo resolvido.** Em “Embora o firewall estivesse ativo, o ataque alcançou o servidor”, `embora` introduz concessão: o fato da primeira oração criava expectativa contrária ao fato principal, mas não o impediu. Trocar por `portanto` mudaria a relação para conclusão e alteraria o sentido.

**Pegadinhas:**

- `contudo` é adversativo, não conclusivo;
- `embora` é concessivo e normalmente pede verbo no subjuntivo;
- `pois`, antes do verbo da oração que introduz, tende a ser explicativo; deslocado ou posposto ao verbo, geralmente entre vírgulas, pode ser conclusivo;
- conectores próximos semanticamente podem exigir pontuação ou construção diferente;
- a presença de `e` não garante mera adição: o contexto pode sugerir sequência ou consequência, mas a inferência deve permanecer apoiada no texto.

<a id="rf4-pt-02"></a>

#### RF4-PT-02 — Inferência, extrapolação e referência textual

**Origem:** **[S1 — revisão ativa]** compreensão literal. **[S2 — aprofundamento]** inferência necessária e resolução de referentes.

**Informação explícita** aparece declarada no texto. **Inferência válida** decorre das informações e das relações textuais sem acrescentar premissa estranha. **Extrapolação** vai além do que o texto permite, frequentemente por usar generalizações como “sempre”, “nunca”, “somente” ou “todos” sem suporte.

**Exemplo resolvido — inferência.** “O portal permaneceu indisponível das 9h às 11h; durante esse intervalo, os requerimentos eletrônicos não puderam ser enviados.” Pode-se inferir que houve impedimento de envio durante duas horas. Não se pode inferir que nenhum requerimento foi enviado durante todo o dia nem que a causa foi um ataque, pois o trecho não oferece essas informações.

Na **referência anafórica**, uma expressão retoma elemento anterior: “A equipe isolou o servidor. **Essa medida** conteve o tráfego.” `Essa medida` retoma o isolamento. Na **referência catafórica**, a expressão anuncia conteúdo posterior: “O problema era **este**: faltavam cópias válidas.”

Para encontrar o referente:

1. localize candidatos próximos;
2. confira concordância de gênero e número, quando houver;
3. teste a compatibilidade semântica;
4. substitua a expressão pelo candidato e releia a frase;
5. rejeite interpretação que gere contradição ou ambiguidade desnecessária.

**Exemplo resolvido — ambiguidade.** “O analista informou ao gestor que **seu** acesso expirara.” O possessivo pode referir-se ao analista ou ao gestor. Uma reescrita clara é “O analista informou ao gestor que o acesso **do gestor** expirara”, se esse for o sentido pretendido.

**Diferenças decisivas:**

- pressuposto × inferência livre: conteúdo acionado pela construção linguística × conclusão elaborada pelo leitor;
- anáfora × catáfora: retomada do que veio antes × anúncio do que virá depois;
- referência gramatical × compatibilidade semântica: concordância ajuda, mas o sentido do contexto decide entre candidatos possíveis;
- inferência × opinião: conclusão sustentada pelo texto × avaliação pessoal sem base textual.

<a id="rf4-pt-03"></a>

#### RF4-PT-03 — `Haver` existencial e `existir`

**Origem:** **[S1 — revisão ativa]** concordância verbal. **[S2 — aprofundamento]** locução verbal, valor auxiliar e contraste entre verbos.

No sentido de **existir, ocorrer ou acontecer**, o verbo `haver` é impessoal: não possui sujeito e permanece na **terceira pessoa do singular**.

- correto: **Havia** falhas no relatório.
- correto: **Houve** dois incidentes.
- correto: **Deve haver** alternativas.
- inadequado na norma-padrão: “Haviam falhas” ou “Devem haver alternativas” com sentido existencial.

Em locução com `haver` impessoal, a impessoalidade alcança o auxiliar: `pode haver`, `deve haver`, `vai haver`.

O verbo `existir` é pessoal e concorda com o sujeito:

- **Existia** uma falha.
- **Existiam** várias falhas.
- **Devem existir** alternativas.

`Haver` também pode funcionar como auxiliar e, nesse caso, flexiona-se normalmente: “Os técnicos **haviam concluído** a análise.” Aqui não significa existir; participa da formação do tempo composto, e o sujeito é `os técnicos`.

**Exemplo resolvido.** Na reescrita de “Devem existir controles adicionais” por uma forma com `haver`, obtém-se “**Deve haver** controles adicionais”. O plural de `controles` comanda `existir`, mas não transforma o complemento de `haver` em sujeito.

**Pegadinhas:**

- `haver` existencial fica no singular mesmo quando o termo posterior está no plural;
- `existir` concorda com o sujeito;
- a forma `houveram problemas` é inadequada quando `haver` significa ocorrer/existir;
- `haver` auxiliar não é impessoal: “eles haviam chegado” está correto;
- em indicação de tempo decorrido, `há` também é impessoal: “há três dias”. Evite redundância em “há três dias atrás”.

<a id="rf4-pt-04"></a>

#### RF4-PT-04 — Pontuação e crase

**Origem:** **[S1 — revisão ativa]** vírgula e fusão `a + a`. **[S2 — aprofundamento]** mudança de sentido por pontuação e teste completo de regência.

##### Pontuação

A vírgula **não separa sujeito de verbo nem verbo de complemento** apenas porque o trecho é longo:

- correto: “Os relatórios produzidos pela equipe **foram arquivados**.”
- inadequado: “Os relatórios produzidos pela equipe, **foram arquivados**.”

Usos frequentes da vírgula:

- isolar adjunto adverbial deslocado, sobretudo quando longo: “Após a contenção do incidente, a equipe restaurou o serviço”;
- separar orações coordenadas e marcar conectores deslocados: “O controle falhou; a equipe, portanto, reviu o processo”;
- isolar aposto explicativo: “A autarquia, pessoa jurídica de direito público, integra a Administração Indireta”;
- isolar oração adjetiva explicativa: “Os servidores, que concluíram o curso, receberam certificado”. Nesse caso, a frase sugere que todos os servidores referidos concluíram o curso.

Sem vírgulas, a oração adjetiva pode ser restritiva: “Os servidores que concluíram o curso receberam certificado” seleciona apenas o grupo que concluiu. A pontuação, portanto, pode alterar o alcance da informação.

##### Crase

Crase é a fusão da preposição `a`, exigida pelo termo anterior, com o artigo feminino `a/as` ou com o `a` inicial de certos demonstrativos (`aquele`, `aquela`, `aquilo`). O teste deve verificar **as duas parcelas**.

- “A equipe se dirigiu **à sala**”: quem se dirige, dirige-se **a** algum lugar; `sala` admite artigo `a`.
- “A equipe começou **a revisar**”: há preposição antes de verbo, mas verbo não admite artigo; não há crase.
- “O relatório foi entregue **ao diretor** / **à diretora**”: o masculino `ao` confirma a combinação `a + o`; no feminino, ocorre `à`.
- “A norma aplica-se **àquela situação**”: `aplicar-se a` + `aquela`.

Casos frequentes:

- locuções adverbiais, prepositivas e conjuntivas femininas: `às pressas`, `à medida que`, `à procura de`;
- indicação de horas determinadas: `às 14h`, mas `daqui a duas horas` indica tempo futuro, sem artigo;
- antes de palavra masculina ou verbo, em regra, não há crase;
- antes de pronomes que não admitem artigo, em regra, não há crase: `a ela`, `a Vossa Senhoria`;
- com nomes de lugar, use o teste `volto da` → crase; `volto de` → sem crase: `vou à Bahia`, `vou a Brasília`, ressalvado o uso contextual de determinante.

**Exemplo resolvido.** “A equipe encaminhou a resposta à autoridade e começou a revisar os anexos.” Há crase antes de `autoridade` porque `encaminhar algo a alguém` exige preposição e o substantivo admite artigo. Não há crase antes de `revisar`, pois não existe artigo antes de verbo.

**Pegadinhas:**

- acento grave não é sinônimo de tonicidade; ele sinaliza a crase;
- palavra feminina, sozinha, não basta: é preciso preposição e artigo/demonstrativo;
- vírgula não é pausa respiratória livre; sua função é sintática e discursiva;
- retirar vírgulas de oração explicativa pode transformar explicação em restrição e mudar o sentido;
- expressão adverbial curta deslocada pode admitir vírgula facultativa em certos contextos, mas sujeito e verbo não devem ser separados.

<a id="rf4-pt-05"></a>

#### RF4-PT-05 — Reescrita, clareza e preservação do sentido

**Origem:** **[S1 — revisão ativa]** ordem direta e correção gramatical. **[S2 — aprofundamento]** controle simultâneo de sentido, referência, paralelismo e relação lógica.

Uma reescrita adequada deve preservar o núcleo de sentido e manter correção, coesão e clareza. A equivalência não depende de repetir as mesmas palavras; depende de conservar relações como causa, oposição, condição, tempo, agente e alcance dos quantificadores.

**Checklist de reescrita:**

1. o agente e o paciente da ação permaneceram os mesmos?
2. tempo, modo, negação e grau de certeza foram preservados?
3. o conector mantém a mesma relação lógica?
4. pronomes e elipses têm referente inequívoco?
5. a concordância e a regência continuam corretas?
6. a pontuação preserva o alcance restritivo ou explicativo?
7. itens coordenados apresentam paralelismo?

**Exemplo resolvido 1 — voz verbal.** “A equipe restaurou o serviço após a análise” pode ser reescrita como “O serviço foi restaurado pela equipe após a análise”. O objeto da ativa torna-se sujeito paciente; o agente e a relação temporal são preservados.

**Exemplo resolvido 2 — causa e conclusão.** “Como havia risco imediato, a equipe isolou o servidor” pode tornar-se “Havia risco imediato; por isso, a equipe isolou o servidor”. `Como`, no contexto, indica causa; `por isso` introduz a consequência correspondente.

**Exemplo resolvido 3 — clareza.** “O diretor comunicou ao analista sua substituição” é ambígua. Se o substituído é o analista, escreva: “O diretor comunicou ao analista **a substituição deste**” ou, com maior naturalidade, “O diretor informou ao analista que **ele seria substituído**”, desde que o contexto elimine o referente concorrente; a forma mais explícita é “...que **o analista seria substituído**”.

**Paralelismo.** Em uma enumeração, mantenha estruturas equivalentes: “O plano busca **reduzir falhas, acelerar respostas e proteger dados**”. A forma “reduzir falhas, a aceleração das respostas e que os dados sejam protegidos” mistura estruturas e prejudica a clareza.

**Concisão não é supressão de informação necessária.** “Em razão do fato de que” pode virar “porque”; “realizar a análise de” pode, em muitos contextos, virar “analisar”. Porém, cortar qualificadores como `apenas`, `possivelmente`, `todos` ou `alguns` pode mudar o alcance da afirmação.

**Pegadinhas:**

- trocar `embora` por `portanto` altera a relação lógica;
- voz ativa e passiva podem preservar o conteúdo proposicional, mas a mudança de foco deve ser observada;
- sinônimos não são intercambiáveis em qualquer contexto;
- uma frase gramaticalmente correta pode não ser semanticamente equivalente;
- eliminar pronome ou repetição não melhora o texto se criar ambiguidade;
- alterar `alguns` para `todos`, ou possibilidade para certeza, invalida a equivalência.

---

### Diferenças entre conceitos próximos — recuperação ativa

| Conceito 1 | Conceito 2 | Diferença que decide a questão | ID teórico |
|---|---|---|---|
| legalidade | eficiência | autorização jurídica × qualidade e bom uso de recursos dentro da lei | `RF4-ADM-01` |
| publicidade | promoção pessoal | transparência institucional × construção de prestígio do agente | `RF4-ADM-02` |
| órgão | entidade | centro de competência sem personalidade × pessoa jurídica | `RF4-ADM-03` |
| desconcentração | descentralização | distribuição interna × atribuição da atividade a outra pessoa jurídica ou, conforme a hipótese legal, física | `RF4-ADM-03` |
| motivo | motivação | pressuposto fático/jurídico × exposição das razões | `RF4-ADM-04` |
| imperatividade | autoexecutoriedade | imposição unilateral × execução material sem ordem judicial prévia nas hipóteses admitidas | `RF4-ADM-05` |
| anulação | revogação | ilegalidade × mérito de ato válido | `RF4-ADM-06` |
| anulação | convalidação | retirada do ato inválido × correção de defeito sanável | `RF4-ADM-06` |
| LAI | LGPD | acesso e transparência × disciplina do tratamento de dados pessoais; aplicação compatível | `RF4-ADM-07` |
| ilegalidade | improbidade | desconformidade jurídica × conduta dolosa tipificada com requisitos legais | `RF4-ADM-08` |
| modalidade | critério de julgamento | espécie de procedimento × método para avaliar proposta | `RF4-ADM-09` |
| dispensa | inexigibilidade | hipótese taxativa, em regra com competição viável em tese × competição inviável | `RF4-ADM-09` |
| responsabilidade do Estado | regresso contra agente | objetiva perante vítima × subjetiva por dolo ou culpa | `RF4-ADM-10` |
| “não (P e Q)” | “não P e não Q” | `não P ou não Q` × ambas necessariamente falsas | `RF4-RLM-01` |
| pelo menos um | exatamente um | inclui interseção × exclui interseção | `RF4-RLM-03` |
| percentual direto | percentual reverso | multiplicar pelo fator × dividir pelo fator | `RF4-RLM-04` |
| proporção direta | inversa | grandezas variam no mesmo sentido × em sentidos opostos | `RF4-RLM-05` |
| oposição | concessão | contraste direto × fato que não impede o resultado contrário à expectativa | `RF4-PT-01` |
| inferência | extrapolação | conclusão sustentada × acréscimo sem base textual | `RF4-PT-02` |
| `haver` existencial | `existir` | impessoal e singular × pessoal e concordante | `RF4-PT-03` |
| oração explicativa | restritiva | comentário sobre o conjunto × seleção de subconjunto | `RF4-PT-04` |
| correção gramatical | equivalência semântica | obediência à norma × preservação do sentido | `RF4-PT-05` |

### Pegadinhas consolidadas da revisão fixa do Dia 4

1. Eficiência não afasta legalidade.
2. Publicidade institucional pode identificar o órgão, mas não promover pessoalmente autoridade ou servidor.
3. Órgão não se torna entidade apenas por possuir competências próprias.
4. Autarquia é criada por lei específica; empresa pública, sociedade de economia mista e fundação têm instituição autorizada por lei específica, e lei complementar define as áreas de atuação da fundação.
5. Vinculação entre entidade e Administração Direta não cria hierarquia entre pessoas jurídicas.
6. Motivo é o suporte fático e jurídico; motivação é sua exteriorização.
7. Presunção de legitimidade é relativa.
8. Nem todo ato possui imperatividade ou autoexecutoriedade.
9. Anulação atinge ilegalidade; revogação atinge mérito de ato válido.
10. O prazo de cinco anos do art. 54 exige ato favorável e ressalva a má-fé comprovada.
11. Convalidação exige defeito sanável e ausência de lesão ao interesse público e de prejuízo a terceiros.
12. LAI e LGPD devem ser compatibilizadas; nenhuma autoriza solução automática de divulgação total ou sigilo total.
13. Mera ilegalidade ou voluntariedade não basta para improbidade.
14. Pregão, concorrência, concurso, leilão e diálogo competitivo são modalidades; menor preço e maior desconto são critérios.
15. Contratação direta não significa contratação sem processo.
16. Dispensa decorre de hipótese taxativa e, em regra, pressupõe competição viável em tese; inexigibilidade decorre de inviabilidade de competição.
17. Responsabilidade objetiva dispensa prova de culpa, mas não dispensa dano e nexo causal.
18. O direito de regresso contra o agente exige dolo ou culpa.
19. A negação de “todo” é “existe pelo menos um... não”, não “nenhum”.
20. Na inclusão-exclusão, a interseção é subtraída uma vez.
21. Para encontrar o valor anterior a um desconto, divide-se pelo fator restante.
22. Grandezas só são tratadas como proporcionais se as demais condições relevantes permanecerem constantes.
23. `Contudo` indica oposição; `embora`, concessão; `portanto`, conclusão.
24. Inferência válida não acrescenta causa, universalidade ou certeza que o texto não forneceu.
25. `Deve haver falhas` fica no singular; `devem existir falhas` concorda com o sujeito.
26. Vírgula não separa sujeito e verbo.
27. Palavra feminina não basta para haver crase; são necessárias preposição e artigo/demonstrativo compatível.
28. Reescrita gramaticalmente correta pode estar errada se alterar referente, quantificador ou relação lógica.

### Tabela de revisão rápida e vinculação das 20 questões extras

| Questão extra | Disciplina | Assunto nuclear | Regra-relâmpago | Seção/ID da teoria | Origem |
|---|---|---|---|---|---|
| Extra 4.1 | Administração Pública | LIMPE | eficiência opera dentro da legalidade | `RF4-ADM-01` | S1 + aprofundamento S2 |
| Extra 4.2 | Administração Pública | art. 37, § 1º | publicidade institucional informa; não promove agente | `RF4-ADM-02` | S1 + aprofundamento S2 |
| Extra 4.3 | Administração Pública | órgão, entidade e autarquia | órgão não tem personalidade; autarquia é entidade de direito público criada por lei | `RF4-ADM-03` | S1 + aprofundamento S2 |
| Extra 4.4 | Administração Pública | elementos do ato | competência, finalidade, forma, motivo e objeto | `RF4-ADM-04` | S1 + aprofundamento S2 |
| Extra 4.5 | Administração Pública | atributos do ato | presunção é relativa; nem todo ato é imperativo ou autoexecutório | `RF4-ADM-05` | S1 + aprofundamento S2 |
| Extra 4.6 | Administração Pública | retirada e correção do ato | anula-se por ilegalidade, revoga-se por mérito e convalida-se defeito sanável | `RF4-ADM-06` | S1 + aprofundamento S2 |
| Extra 4.7 | Administração Pública | LAI e LGPD | transparência e proteção de dados são compatibilizadas por finalidade e necessidade | `RF4-ADM-07` | S1 + aprofundamento S2 |
| Extra 4.8 | Administração Pública | improbidade | exige conduta dolosa tipificada e requisitos legais | `RF4-ADM-08` | S1 + aprofundamento S2 |
| Extra 4.9 | Administração Pública | modalidades e contratação direta | dispensa: hipótese taxativa, em regra com competição viável em tese; inexigibilidade: competição inviável; ambas exigem processo | `RF4-ADM-09` | S1 + aprofundamento S2 |
| Extra 4.10 | Administração Pública | responsabilidade do Estado | objetiva perante a vítima; regresso subjetivo por dolo ou culpa | `RF4-ADM-10` | S1 + aprofundamento S2 |
| Extra 4.11 | RLM | De Morgan | nega cada parcela e troca `e`/`ou` | `RF4-RLM-01` | S1 + aprofundamento S2 |
| Extra 4.12 | RLM | condicional e quantificadores | `não(P→Q) = P e não Q`; negar todo produz contraexemplo | `RF4-RLM-02` | S1 + aprofundamento S2 |
| Extra 4.13 | RLM | inclusão-exclusão | some os conjuntos e subtraia a interseção | `RF4-RLM-03` | S1 + aprofundamento S2 |
| Extra 4.14 | RLM | porcentagem reversa | recupere o original dividindo pelo fator | `RF4-RLM-04` | S1 + aprofundamento S2 |
| Extra 4.15 | RLM | proporção | identifique primeiro se a relação é direta ou inversa | `RF4-RLM-05` | S1 + aprofundamento S2 |
| Extra 4.16 | Português | conectores | preserve oposição, concessão, causa ou conclusão | `RF4-PT-01` | S1 + aprofundamento S2 |
| Extra 4.17 | Português | inferência e referência | conclua apenas o sustentado e teste o referente no contexto | `RF4-PT-02` | S1 + aprofundamento S2 |
| Extra 4.18 | Português | `haver` e `existir` | `haver` existencial é singular; `existir` concorda | `RF4-PT-03` | S1 + aprofundamento S2 |
| Extra 4.19 | Português | pontuação e crase | não separe sujeito e verbo; confirme preposição + artigo | `RF4-PT-04` | S1 + aprofundamento S2 |
| Extra 4.20 | Português | reescrita e clareza | correção formal não basta: preserve sentido, referente e alcance | `RF4-PT-05` | S1 + aprofundamento S2 |

### Base normativa para conferência

- Constituição Federal: art. 37, caput, §§ 1º e 6º, e inciso XIX.
- Decreto-Lei nº 200/1967: arts. 4º e 5º, especialmente a organização da Administração Federal e o conceito de autarquia.
- Lei nº 9.784/1999: arts. 50 e 53 a 55.
- Lei nº 12.527/2011: art. 3º; art. 7º, § 2º; e art. 31.
- Lei nº 13.709/2018: arts. 5º e 6º; art. 7º, § 3º; e art. 23.
- Lei nº 8.429/1992, com as alterações da Lei nº 14.230/2021: art. 1º, §§ 1º a 4º, e arts. 9º a 11.
- Lei nº 14.133/2021: arts. 6º, 28, 29, 32, 33, 72, 74, 75 e 76.

### Fechamento do bloco

Antes das questões extras, o estudante deve conseguir explicar sem consulta:

- por que eficiência não permite descumprir a lei e por que publicidade não permite promoção pessoal;
- a diferença entre órgão, entidade, desconcentração, descentralização e autarquia;
- os cinco elementos e os quatro atributos mais cobrados do ato administrativo;
- quando anular, revogar ou convalidar e como funciona o prazo do art. 54;
- como conciliar LAI e LGPD sem transformar publicidade ou sigilo em regra absoluta;
- por que ilegalidade não basta para caracterizar improbidade;
- as cinco modalidades atuais e a diferença entre dispensa e inexigibilidade;
- por que a responsabilidade estatal é objetiva e o regresso contra o agente é subjetivo;
- as negações lógicas, a inclusão-exclusão, a porcentagem reversa e a direção de uma proporção;
- o valor dos conectores, o limite da inferência, o referente textual, a concordância de `haver`/`existir`, os testes de pontuação e crase e os critérios de uma reescrita clara.

## Tabela de revisão rápida do Dia 4

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| Confidencialidade | impedir divulgação não autorizada | confundir com integridade | base copiada |
| Integridade | impedir/detectar alteração indevida | achar que hash prova veracidade | registro adulterado |
| Disponibilidade | acesso oportuno ao serviço | dizer que backup impede falha | portal fora do ar |
| Autenticação | provar identidade | confundir com permissão | MFA no login |
| Autorização | definir ações permitidas | usuário autenticado pode tudo | RBAC por função |
| AAA/accounting | autenticar, autorizar e registrar uso/sessões | terceiro A como sinônimo perfeito de auditoria | RADIUS Accounting |
| Auditoria | registrar e analisar ações | logs sem proteção bastam | trilha de acesso |
| Não repúdio | evidência contra negação falsa | hash isolado | assinatura digital |
| Ameaça | causa potencial de dano | confundir com fraqueza | criminoso/ransomware |
| Vulnerabilidade | fraqueza explorável | confundir com incidente | software sem correção |
| Risco | probabilidade e impacto | tratar como certeza | risco de indisponibilidade |
| Incidente | comprometimento ou ameaça concreta | todo alerta é incidente | acesso indevido confirmado |
| Ransomware | extorsão com cifração, bloqueio ou exfiltração | limitar o efeito à disponibilidade | afeta múltiplos princípios CIA |
| Phishing | fraude por mensagem/página | achar que MFA elimina | página falsa |
| Spoofing | falsificação de identidade/origem | confundir com captura | ARP falso |
| Sniffing | captura de tráfego | sempre altera dados | analisador em modo passivo |
| Ataque on-path | intercepta e pode alterar | basta haver criptografia | certificado falso aceito |
| DoS/DDoS | negação de serviço | firewall local resolve tudo | saturação de enlace |
| Firewall | aplica política de tráfego | porta liberada é segura | bloquear origem indevida |
| IDS | detecta e alerta | bloqueia sempre | sensor fora de banda |
| IPS | tenta prevenir em linha | não tem falso positivo | descarte automático |
| DMZ | segmento para serviços expostos | rede confiável | proxy web separado |
| VPN | túnel protegido | gateway sem patch continua seguro | acesso remoto IPsec/TLS |
| Segmentação | separa ambientes e fluxos | VLAN impede movimento lateral roteado | usuários × servidores |
| Cifra simétrica | mesma chave secreta | resolve distribuição de chave | AES |
| Cifra assimétrica | par pública/privada | cifrar todo tráfego com privada | assinatura/estabelecimento |
| Hash | resumo unidirecional comparado a referência confiável | resumo ao lado do arquivo basta | SHA-256 assinado/publicado por canal seguro |
| HMAC | integridade/autenticidade com segredo | oferece não repúdio | mensagem entre sistemas |
| Assinatura digital | privada assina, pública verifica | cifra conteúdo | documento assinado |
| Certificado | vincula identidade e chave pública | prova honestidade | certificado de servidor |
| TLS | canal autenticado, íntegro e confidencial | protege endpoint | HTTPS |
| WPA2 | segurança Wi-Fi robusta quando bem configurada | senha compartilhada fraca | WPA2-Enterprise |
| WPA3-Personal | usa SAE para troca autenticada por senha | invulnerabilidade ou transição igual a WPA3 puro | SAE negociado pelo cliente |
| Resposta | conter, erradicar e recuperar com objetivos distintos | restaurar antes de tratar persistência | playbook de ransomware |
| Backup | cópia para recuperação | RAID é backup | cópia offline testada |
| RPO | ponto temporal objetivo para recuperar dados | confundir meta com perda observada | recuperar dados até o ponto de 1h antes da falha |
| RTO | objetivo de tempo para restabelecimento | confundir com frequência de backup | meta de retorno em 4h |

## Pegadinhas do Dia 4

- CIA não é lista de produtos; são objetivos de proteção.
- Autenticação não concede automaticamente autorização.
- Em AAA, o terceiro A é accounting; ele fornece registros para auditoria, mas não é sinônimo de todo o processo de auditoria.
- MFA exige fatores diferentes.
- Log sem tempo correto, integridade e análise pode ter pouco valor.
- Hash não cifra e não autentica origem sem mecanismo adicional; a detecção depende de resumo de referência confiável.
- Assinatura digital não fornece confidencialidade.
- Certificado válido não prova que o conteúdo seja benigno.
- TLS protege o canal, não os endpoints.
- Ameaça, vulnerabilidade, risco e incidente não são sinônimos.
- Ransomware pode afetar confidencialidade, integridade e disponibilidade no mesmo incidente.
- Phishing é espécie de engenharia social.
- Sniffing pode ser passivo; ataque on-path pode alterar.
- DDoS pode saturar o enlace antes do firewall local.
- Firewall não corrige aplicação vulnerável.
- IDS normalmente alerta; IPS pode bloquear.
- IDS/IPS têm falsos positivos e falsos negativos.
- DMZ não é rede livre nem totalmente confiável.
- VPN não torna dispositivo remoto seguro, e gateway VPN sem correção continua sendo superfície de ataque.
- VLAN separa camada 2, mas sem política inter-VLAN não impede movimento lateral roteado.
- NAT não substitui firewall.
- WPA2 com senha fraca continua vulnerável.
- WPA3-Personal usa SAE, mas não elimina engenharia social, falha de firmware ou tentativa online; modo de transição ainda pode negociar WPA2.
- Backup não substitui redundância, e redundância não substitui backup.
- Restaurar sem erradicar persistência pode reinfectar o ambiente.
- Controles reduzem risco; não prometem segurança absoluta.
- Risco residual é o que resta após controles; evite tanto prometer risco zero quanto afirmar valor positivo mensurável em todo cenário.

## Prática guiada

### Caso — Incidente no portal de fiscalização

O portal público está em DMZ. A aplicação consulta banco interno. Às 8h20, o SIEM registra login administrativo de país incomum; às 8h23, há criação de conta privilegiada; às 8h30, grande volume de dados sai do servidor; às 8h40, compartilhamentos começam a ser cifrados. A conta usava apenas senha. O último backup offline validado terminou à 1h.

#### Etapa 1 — Classificação

- ameaça: agente externo;
- vulnerabilidades: autenticação sem MFA, possível exposição de credencial e permissões amplas;
- incidentes: conta privilegiada indevida, exfiltração e cifração;
- CIA: confidencialidade, integridade e disponibilidade;
- evidências: logs de identidade, firewall, proxy, aplicação, banco, endpoint e fluxo.

#### Etapa 2 — Contenção inicial

1. ativar equipe e autoridade;
2. desabilitar/limitar contas comprometidas;
3. isolar hosts afetados e bloquear indicadores;
4. preservar evidências voláteis conforme playbook;
5. impedir movimento da DMZ para segmentos internos;
6. proteger infraestrutura de backup;
7. comunicar áreas responsáveis.

#### Etapa 3 — Erradicação

1. identificar vetor inicial, persistência e todos os ativos afetados;
2. remover malware, contas e tarefas persistentes;
3. corrigir vulnerabilidades exploradas;
4. rotacionar credenciais e chaves comprometidas;
5. reconstruir componentes cujo estado não seja confiável;
6. confirmar que os pontos de entrada conhecidos foram tratados.

#### Etapa 4 — Recuperação

1. selecionar e validar backup anterior ao comprometimento;
2. restaurar serviços por prioridade em ambiente controlado;
3. verificar integridade, função e controles antes da reconexão ampla;
4. monitorar recorrência;
5. revisar segmentação, MFA, privilégios e regras;
6. registrar lições e cumprir obrigações de comunicação.

#### Resultado esperado

A solução não deve resumir-se a “ligar o firewall” ou “restaurar o backup”. Ela precisa combinar identidade, contenção, evidência, correção da causa, recuperação segura e melhoria dos controles.

## Checklist de domínio

- [ ] Explico confidencialidade, integridade e disponibilidade.
- [ ] Reconheço incidentes que atingem mais de um princípio CIA.
- [ ] Distingo autenticação, autorização, auditoria e não repúdio.
- [ ] Explico AAA e distingo accounting do processo mais amplo de auditoria.
- [ ] Distingo ameaça, vulnerabilidade, risco, evento e incidente.
- [ ] Reconheço categorias de malware sem chamar tudo de vírus.
- [ ] Explico phishing como engenharia social.
- [ ] Distingo spoofing, sniffing e ataque on-path.
- [ ] Distingo força bruta, spraying e credential stuffing.
- [ ] Explico DoS e DDoS e limites do firewall local.
- [ ] Classifico controles por natureza e função.
- [ ] Explico firewall e suas limitações.
- [ ] Distingo IDS e IPS, inclusive falsos positivos/negativos.
- [ ] Sei posicionar DMZ, aplicação e banco.
- [ ] Explico benefícios e limites da VPN.
- [ ] Aplico segmentação e menor privilégio.
- [ ] Distingo criptografia simétrica e assimétrica.
- [ ] Distingo hash, HMAC e assinatura e exijo referência confiável para comparar hashes.
- [ ] Explico certificado e validação de cadeia/nome.
- [ ] Descrevo o TLS em nível conceitual.
- [ ] Comparo WPA2-Personal, WPA3-Personal/SAE e modo de transição sem absolutismos.
- [ ] Separo contenção, erradicação e recuperação conforme seus objetivos.
- [ ] Distingo backup, redundância, RPO como objetivo temporal e RTO.
- [ ] Revi Administração, RLM e Português.

## Orientações para o caderno de erros

Use a estrutura:

1. **Ativo e objetivo afetado:** CIA.
2. **Conceitos confundidos:** por exemplo, autenticação × autorização.
3. **Controle sugerido e limite:** “IPS pode bloquear, mas pode falhar”.
4. **Evidência do cenário:** log, fluxo, conta ou arquivo.
5. **Ação correta:** prevenção, detecção, resposta ou recuperação.
6. **Frase antídoto:** uma sentença curta que elimine o absolutismo.

Exemplos de frases antídoto:

- “TLS protege o canal, não corrige o endpoint.”
- “IDS detecta; IPS tenta prevenir; nenhum garante.”
- “Hash só evidencia alteração quando comparado a uma referência confiável; ele não cifra.”
- “Backup recupera; não impede o incidente.”
- “VPN cria túnel; não concede confiança irrestrita.”

Revise o caderno em 24 horas e novamente no Dia 6.

## Fontes oficiais utilizadas — Dia 4

Fontes primárias e orientações oficiais consultadas em 10 de julho de 2026:

- Edital CRA-PR 2026, conforme Retificação I: https://cdnsite.institutoconsulplan.org.br/concursos/1330/b2c07c473c9749fea22728da3c964c06.pdf
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- NIST SP 800-34 Rev. 1 — Contingency Planning Guide, fonte da definição de RPO: https://csrc.nist.gov/pubs/sp/800/34/r1/final
- NIST CSRC Glossary: https://csrc.nist.gov/glossary
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- NIST SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy: https://csrc.nist.gov/pubs/sp/800/41/r1/final
- NIST SP 800-94 — Guide to Intrusion Detection and Prevention Systems: https://csrc.nist.gov/pubs/sp/800/94/final
- NIST SP 800-153 — Guidelines for Securing Wireless Local Area Networks: https://csrc.nist.gov/pubs/sp/800/153/final
- NIST SP 800-52 Rev. 2 — Guidelines for TLS Implementations: https://csrc.nist.gov/pubs/sp/800/52/r2/final
- NIST SP 800-57 Part 1 Rev. 5 — Key Management: https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final
- FIPS 197 — Advanced Encryption Standard: https://csrc.nist.gov/pubs/fips/197/final
- FIPS 180-4 — Secure Hash Standard: https://csrc.nist.gov/pubs/fips/180-4/upd1/final
- FIPS 186-5 — Digital Signature Standard: https://csrc.nist.gov/pubs/fips/186-5/final
- RFC 2104 — HMAC, autenticação de mensagem baseada em hash: https://www.rfc-editor.org/rfc/rfc2104
- RFC 2865 — RADIUS Authentication e Authorization: https://www.rfc-editor.org/rfc/rfc2865
- RFC 2866 — RADIUS Accounting: https://www.rfc-editor.org/rfc/rfc2866
- RFC 8446 — TLS 1.3: https://www.rfc-editor.org/rfc/rfc8446
- RFC 5280 — perfil de certificados X.509: https://www.rfc-editor.org/rfc/rfc5280
- RFC 4301 — arquitetura IPsec: https://www.rfc-editor.org/rfc/rfc4301
- RFC 8018 — criptografia baseada em senha e PBKDF2: https://www.rfc-editor.org/rfc/rfc8018
- CISA — #StopRansomware Guide: https://www.cisa.gov/stopransomware/ransomware-guide
- CISA — Enhanced Visibility and Hardening Guidance for Communications Infrastructure: https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure
- CISA — Modern Approaches to Network Access Security: https://www.cisa.gov/resources-tools/resources/modern-approaches-network-access-security
- Wi-Fi Alliance — Security: https://www.wi-fi.org/discover-wi-fi/security
- Constituição Federal, art. 37: https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm
- Lei nº 14.133/2021: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm
- Lei nº 12.527/2011: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm
- Lei nº 13.709/2018, texto compilado: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- Lei nº 8.429/1992, texto compilado: https://www.planalto.gov.br/ccivil_03/leis/l8429compilada.htm
- Manual de Redação da Presidência da República, 3ª edição: https://www.gov.br/pt-br/servicos/consultar-o-manual-de-redacao-da-presidencia-da-republica

---
# Dia 5 — Sistemas Operacionais Avançados

## Objetivo do dia

Aprofundar os mecanismos pelos quais um sistema operacional compartilha processadores, memória, dispositivos e arquivos entre fluxos de execução concorrentes. Ao final do dia, o estudante deverá conseguir raciocinar sobre processos e threads, localizar condições de corrida, escolher primitivas de sincronização, reconhecer e tratar deadlocks, interpretar políticas de escalonamento e relacionar drivers, interrupções, DMA, polling, sistemas de arquivos, journaling e permissões às práticas de Windows e Linux exigidas pelo edital.

Este dia aprofunda o item 2 do conteúdo de Analista de Sistemas: gerenciamento de processos e dispositivos, concorrência, esquemas de sincronização, deadlock, sistema de arquivos e aspectos práticos e teóricos de Windows/Linux. A Retificação I não alterou esse bloco técnico.

## Resultados esperados

Ao concluir as 6 horas líquidas, o estudante deverá ser capaz de:

- distinguir concorrência de paralelismo e explicar por que pode existir concorrência em uma única CPU;
- diferenciar programa, processo e thread, incluindo recursos compartilhados e contexto próprio;
- identificar seção crítica e demonstrar uma condição de corrida por meio de uma intercalação de operações;
- comparar mutex, semáforo binário, semáforo contador, monitor, variável de condição e spinlock;
- selecionar um mecanismo de comunicação entre processos conforme isolamento, volume de dados e necessidade de sincronização;
- reconhecer as quatro condições necessárias de Coffman e separar prevenção, evitação, detecção e recuperação de deadlock;
- diferenciar deadlock, starvation, livelock e inversão de prioridade;
- comparar FCFS, SJF, SRTF, prioridade, Round Robin, filas multinível e filas multinível com realimentação;
- explicar o papel do controlador, do driver, da interrupção, do DMA e do polling em uma operação de entrada/saída;
- explicar abstrações de sistemas de arquivos, journaling e permissões em Linux e Windows;
- interpretar comandos administrativos básicos sem confundir observação com alteração de estado;
- revisar corretamente o escopo de Legislação CRA/CFA aplicável ao Analista após a Retificação I;
- aplicar interpretação textual e relações de causa, oposição e conclusão em enunciados técnicos.

## Por que o assunto importa para a prova

O edital nomeia expressamente concorrência, esquemas de sincronização e deadlock. Esses termos costumam ser cobrados em conjunto: uma alternativa descreve uma condição de corrida, mas a chama de deadlock; outra troca mutex por semáforo contador; uma terceira afirma que duas tarefas somente são concorrentes quando executam ao mesmo tempo em núcleos distintos.

O assunto também se conecta às atribuições reais do cargo. Servidores de aplicação, bancos de dados, rotinas de backup, atendimento simultâneo a usuários e resposta a incidentes dependem de escalonamento, E/S, exclusão mútua e recuperação. Um travamento que parece ser “rede lenta” pode ser espera por disco, esgotamento do pool de threads ou ciclo de dependências entre locks.

Conhecimentos do Cargo representam 30 pontos da objetiva e são o primeiro critério acadêmico de desempate depois da discursiva. A banca ainda pode integrar mais de uma habilidade no mesmo item, conforme o próprio edital. Portanto, memorizar definições isoladas é insuficiente: é necessário reconstruir o fluxo de execução.

## Como pode ser cobrado no estilo Instituto Consulplan

O edital autoriza cobrança de compreensão, aplicação e análise. Neste bloco, espere especialmente:

- cenário com dois fluxos incrementando a mesma variável e resultado final aparentemente impossível;
- sequência de aquisição de recursos para identificar espera circular;
- comparação conceitual, com apenas uma palavra alterando a correção da alternativa;
- cálculo simples de tempo de espera, retorno ou resposta em uma fila de processos;
- escolha entre mutex e semáforo conforme o recurso tenha uma ou várias instâncias;
- análise de prioridade, quantum, preempção e starvation;
- distinção entre polling, interrupção e DMA;
- afirmação de que journaling equivale a backup, que deve ser rejeitada;
- interpretação de permissões rwx ou de uma DACL do Windows;
- leitura de saída de ps, tasklist ou Get-Process, sem exigir memorização de opções obscuras;
- integração de Linux e Windows: os nomes e comandos diferem, mas os conceitos de processo, thread, ACL, serviço e sistema de arquivos permanecem.

Um método seguro é sublinhar no enunciado: recurso compartilhado, ordem das operações, possibilidade de preempção, número de instâncias, forma de espera e garantia pretendida. Essas palavras revelam o conceito testado.

## Cronograma de 6h líquidas — 360 minutos

| Bloco | Tempo líquido | Atividade |
|---|---:|---|
| Ativação e diagnóstico | 20 min | Recuperar processo, thread, estados e troca de contexto sem consultar a teoria |
| Concorrência, paralelismo, processos e threads | 60 min | Teoria, diagramas de intercalação e exemplos |
| Seção crítica, sincronização e IPC | 65 min | Mutex, semáforos, monitores, variáveis de condição, spinlocks e comunicação |
| Deadlock e problemas de progresso | 65 min | Quatro condições, estratégias de tratamento, starvation, livelock e inversão |
| Escalonamento | 45 min | Métricas, algoritmos, preempção, quantum e prioridades |
| Dispositivos e sistemas de arquivos | 45 min | Drivers, interrupções, DMA, polling, VFS, journaling e permissões |
| Laboratório conceitual Windows/Linux | 30 min | Interpretar comandos e saídas sem executar alterações perigosas |
| Revisão fixa — Legislação CRA/CFA | 20 min | Lei, Decreto, Regimento e RN CFA nº 671/2025 |
| Revisão fixa — Português e interpretação | 10 min | Conectores, referente pronominal e inferência em texto técnico |
| **Total** | **360 min** | **6 horas líquidas** |

## Teoria explicada de forma didática

<a id="s2-d5-concorrencia-paralelismo"></a>
### 1. Concorrência e paralelismo

Concorrência é a existência de mais de uma tarefa em progresso durante um intervalo de tempo. Paralelismo é a execução efetivamente simultânea de duas ou mais tarefas. Em um único núcleo, o sistema pode alternar rapidamente entre tarefas: elas são concorrentes, embora apenas uma execute a cada instante. Em vários núcleos, tarefas concorrentes também podem executar em paralelo.

Essa distinção elimina duas confusões frequentes:

- concorrência é uma propriedade da organização temporal e das possíveis intercalações;
- paralelismo depende de recursos capazes de executar simultaneamente.

Uma aplicação pode usar múltiplas threads por responsividade mesmo sem ganhar desempenho de CPU. Enquanto uma thread aguarda disco ou rede, outra pode atender a interface ou outra requisição. Para trabalho estritamente CPU-bound, o ganho paralelo exige núcleos disponíveis e ausência de gargalo serial dominante.

#### Intercalação

Considere duas tarefas, A e B. Em uma CPU:

~~~text
tempo:  1  2  3  4  5  6
CPU:    A  A  B  B  A  B
~~~

Não houve simultaneidade, mas ambas avançaram no intervalo. Em duas CPUs, A e B podem ocupar processadores diferentes no mesmo instante.

<a id="s2-d5-processo-thread"></a>
### 2. Programa, processo e thread

Programa é o conjunto passivo de instruções armazenadas. Processo é uma instância em execução, com espaço de endereçamento virtual, recursos, descritores ou handles, credenciais, estado e pelo menos um fluxo de execução. Thread é o fluxo que o escalonador coloca na CPU.

Threads de um mesmo processo normalmente compartilham código, dados globais, heap e recursos abertos. Cada thread precisa preservar contexto próprio, como registradores, contador de programa, pilha e estado de escalonamento. A documentação da Microsoft descreve a thread como a entidade escalonável e registra que threads do mesmo processo compartilham o espaço de endereçamento e os recursos do processo.

Processos oferecem maior isolamento: uma falha de memória em um processo não deve escrever livremente no espaço virtual de outro. Threads são mais leves para comunicação por memória compartilhada, mas exigem disciplina de sincronização.

#### Estados conceituais

- novo: estruturas estão sendo criadas;
- pronto: pode executar, mas aguarda CPU;
- executando: ocupa um processador;
- bloqueado ou em espera: aguarda evento, E/S, lock ou tempo;
- terminado: concluiu ou foi encerrado.

Uma thread bloqueada por E/S não está pronta. Aumentar sua prioridade não elimina o evento que ainda não ocorreu.

#### Troca de contexto

Na troca de contexto, o sistema salva o estado do fluxo que sai e restaura o do que entra. É trabalho necessário para multiplexar a CPU, mas não produz resultado de negócio. Quantum pequeno pode melhorar resposta interativa e, ao mesmo tempo, elevar o custo de trocas. Quantum grande aproxima Round Robin de FCFS.

<a id="s2-d5-corrida-atomicidade"></a>
### 3. Seção crítica, condição de corrida e atomicidade

Seção crítica é o trecho que acessa um recurso compartilhado cujo estado precisa permanecer consistente. Condição de corrida ocorre quando o resultado depende da ordem temporal não controlada de acessos concorrentes conflitantes.

Suponha saldo = 100 e duas threads executando saldo = saldo + 10. A expressão não é necessariamente uma única operação indivisível:

~~~text
T1 lê 100
T2 lê 100
T1 calcula 110
T2 calcula 110
T1 grava 110
T2 grava 110
~~~

O resultado é 110, e não 120. Houve atualização perdida. A linha de alto nível parecia simples, mas continha leitura, cálculo e escrita.

Atomicidade significa que a operação relevante aparece como indivisível para os demais fluxos. Atomicidade de uma instrução não garante atomicidade de uma sequência. Visibilidade também importa: uma gravação precisa tornar-se observável conforme o modelo de memória. Ordenação importa porque compilador e processador podem reorganizar operações dentro das garantias permitidas.

Uma solução correta para a seção crítica busca:

- exclusão mútua: no máximo um fluxo na região protegida quando isso for necessário;
- progresso: se a seção está livre e há interessados, a escolha não pode ser adiada indefinidamente;
- espera limitada ou justiça, quando exigida: um participante não deve ser ultrapassado para sempre.

<a id="s2-d5-sincronizacao"></a>
### 4. Mutex, semáforos, monitores e variáveis de condição

#### Mutex

Mutex modela propriedade exclusiva: um fluxo adquire, entra na seção crítica e libera. Em desenho convencional, quem adquire deve liberar. O lock deve proteger o menor estado coerente possível; manter mutex durante E/S lenta aumenta contenção e pode compor deadlock.

Um mutex não “torna todo o programa atômico”. Ele ordena apenas participantes que respeitam o mesmo protocolo de proteção.

#### Semáforo binário e contador

Semáforo mantém um contador manipulado atomicamente:

- wait, P ou down: tenta decrementar; se não houver unidade disponível, aguarda;
- post, V ou up: incrementa e pode despertar um aguardando.

Semáforo binário assume valores equivalentes a 0 e 1 e pode controlar passagem. Semáforo contador representa N unidades, como 20 conexões em um pool. Embora um semáforo binário possa produzir exclusão, mutex expressa melhor propriedade do lock; não se deve dizer que são sempre idênticos.

#### Monitor e variável de condição

Monitor encapsula estado compartilhado, operações e exclusão mútua. Uma variável de condição permite aguardar até que um predicado se torne verdadeiro. A espera condicionada deve liberar atomicamente o lock enquanto a thread dorme e readquiri-lo antes de retornar; caso contrário, o produtor nunca conseguiria alterar o estado necessário.

O padrão seguro verifica a condição em laço, porque a thread pode acordar e descobrir que outra consumiu o recurso ou que houve despertar espúrio:

~~~text
adquirir(mutex)
enquanto fila_vazia:
    esperar(condicao, mutex)
retirar_item()
liberar(mutex)
~~~

A especificação Java associa um monitor a cada objeto e define lock, unlock, conjunto de espera e notificações. POSIX trata mutex e variável de condição como primitivas complementares de sincronização entre threads.

#### Spinlock

Spinlock espera ativamente, verificando o lock em laço. Pode ser adequado no kernel ou em trechos curtíssimos quando dormir e despertar custaria mais, sobretudo em multiprocessadores. É inadequado para espera longa: consome CPU. Em um único núcleo não preemptível, girar esperando quem não pode executar é especialmente problemático.

<a id="s2-d5-ipc"></a>
### 5. Comunicação entre processos — IPC

Processos isolados precisam de mecanismos explícitos. A escolha considera direção, persistência, volume, cópia de dados, localidade e necessidade de sincronização.

- pipe anônimo: fluxo de bytes normalmente entre processos relacionados; simples e geralmente unidirecional por descritor;
- FIFO ou named pipe: nome conhecido permite comunicação entre processos sem parentesco direto;
- fila de mensagens: preserva unidades de mensagem e desacopla remetente de destinatário;
- memória compartilhada: alto desempenho por evitar cópias repetidas, mas exige mutex, semáforo ou outro protocolo;
- socket: comunicação local ou em rede; abstração bidirecional adequada a cliente-servidor;
- sinais ou eventos: notificam ocorrências, mas carregam pouca informação;
- RPC: apresenta uma chamada remota como operação de mais alto nível, ocultando serialização e transporte, sem eliminar falhas distribuídas.

Memória compartilhada não é automaticamente segura. Ela remove parte do custo de transporte e transfere ao projeto a responsabilidade de sincronizar acesso e visibilidade.

<a id="s2-d5-deadlock"></a>
### 6. Deadlock

Deadlock é um estado em que um conjunto de fluxos permanece bloqueado porque cada um aguarda evento ou recurso que somente outro integrante do conjunto pode produzir ou liberar.

#### As quatro condições necessárias de Coffman

As quatro devem coexistir para o deadlock clássico de recursos reutilizáveis:

1. exclusão mútua: pelo menos um recurso não pode ser usado simultaneamente;
2. posse e espera: um fluxo mantém recurso enquanto espera outro;
3. não preempção: o recurso não é retirado compulsoriamente; é liberado voluntariamente;
4. espera circular: existe ciclo P1 espera por P2, P2 por P3 e, ao final, algum processo espera por P1.

São condições necessárias em conjunto, não a definição isolada de deadlock. Existir exclusão mútua não basta.

#### Exemplo de ciclo

~~~text
T1: adquire A; tenta adquirir B
T2: adquire B; tenta adquirir A
~~~

Se as duas primeiras aquisições ocorrerem antes das segundas, T1 espera B e T2 espera A indefinidamente.

#### Prevenção

Prevenção projeta o sistema para quebrar ao menos uma condição necessária:

- reduzir exclusão quando o recurso puder ser compartilhado de forma segura;
- exigir aquisição de todos os recursos de uma vez, quebrando posse e espera, com possível baixa utilização;
- liberar recursos já obtidos quando uma nova aquisição falhar, aproximando preempção lógica;
- impor ordem global de locks, como sempre adquirir A antes de B, quebrando espera circular.

Ordem global é uma técnica prática forte, mas precisa valer em todos os caminhos, inclusive tratamento de erro.

#### Evitação

Evitação examina cada solicitação e concede somente se o estado resultante permanecer seguro. Estado seguro é aquele em que existe alguma sequência de conclusão para todos os participantes. O algoritmo do banqueiro é o exemplo clássico para múltiplas instâncias e requer conhecer demandas máximas. Estado inseguro não significa que o deadlock já ocorreu; significa que a garantia de uma sequência segura foi perdida.

#### Detecção

Detecção permite a alocação e procura ciclos ou processos que não conseguem progredir. Quando há uma única instância de cada tipo de recurso, um ciclo no grafo de espera é condição necessária e suficiente para deadlock: cada vértice representa processo e cada aresta P → Q indica que P espera recurso mantido por Q. Com várias instâncias por tipo, é necessário considerar disponíveis, alocados e requisições pendentes; nesse caso, um ciclo continua sendo sinal de dependência, mas sozinho não é condição suficiente para concluir deadlock.

#### Recuperação

Após detectar, o sistema pode:

- abortar um ou mais participantes;
- selecionar uma vítima por custo, prioridade, trabalho já feito e recursos mantidos;
- preemptar recurso quando houver estado restaurável;
- realizar rollback para checkpoint consistente;
- usar timeout e nova tentativa quando a operação for idempotente e o timeout representar política, não mera ocultação do problema.

Encerrar aleatoriamente pode corromper estado. Recuperação precisa respeitar transações e invariantes.

<a id="s2-d5-starvation-livelock"></a>
### 7. Starvation, livelock e inversão de prioridade

Starvation é adiamento indefinido: um fluxo está apto ou tenta obter recurso, mas outros são continuamente favorecidos. Pode ocorrer em escalonamento por prioridade sem aging, lock injusto ou fila permanentemente ocupada.

Aging aumenta gradualmente a prioridade de quem espera e reduz starvation. Justiça estrita, porém, pode custar throughput; é uma escolha de projeto.

Livelock ocorre quando fluxos continuam ativos e mudando de estado, mas não produzem progresso útil. Duas pessoas desviando para o mesmo lado repetidamente ilustram a ideia. Backoff aleatório pode quebrar a simetria.

Inversão de prioridade ocorre quando uma thread de alta prioridade aguarda lock mantido por uma de baixa prioridade, enquanto threads intermediárias impedem a baixa de executar e liberar. Herança de prioridade eleva temporariamente a detentora do lock; teto de prioridade é outra política.

Deadlock implica espera permanente sem progresso do conjunto; starvation pode afetar um fluxo enquanto outros progridem; livelock tem atividade sem avanço útil.

<a id="s2-d5-escalonamento"></a>
### 8. Escalonamento de CPU

O escalonador escolhe entre threads prontas. Critérios usuais:

- utilização da CPU e throughput;
- tempo de retorno: conclusão menos chegada;
- tempo de espera: tempo acumulado na fila de prontos;
- tempo de resposta: primeiro atendimento menos chegada;
- justiça, previsibilidade e cumprimento de prazos.

#### Algoritmos clássicos

- FCFS: ordem de chegada, não preemptivo; simples, sujeito ao efeito comboio;
- SJF: menor próximo burst primeiro, não preemptivo; minimiza espera média sob hipóteses ideais, mas exige estimativa e pode deixar tarefas longas em starvation;
- SRTF: versão preemptiva do SJF; nova tarefa curta pode preemptar a atual;
- prioridade: executa maior prioridade; pode ser preemptivo ou não e precisa tratar starvation;
- Round Robin: cada pronto recebe quantum; adequado a tempo compartilhado;
- filas multinível: classes em filas separadas com regras próprias, sem migração como característica básica;
- filas multinível com realimentação: processos mudam de fila conforme comportamento e uso de CPU, favorecendo resposta de tarefas interativas;
- tempo real: políticas como FIFO e RR de prioridade fixa ou deadline tratam requisitos diferentes dos algoritmos didáticos gerais.

Linux documenta SCHED_OTHER para compartilhamento normal, SCHED_FIFO e SCHED_RR para tempo real e SCHED_DEADLINE para parâmetros de runtime, deadline e período. Windows usa escalonamento preemptivo por prioridade e Round Robin entre threads prontas de mesma prioridade; uma thread de prioridade superior pronta pode preemptar outra inferior.

<a id="s2-d5-dispositivos-e-s"></a>
### 9. Dispositivos, drivers, interrupções, polling e DMA

Um dispositivo físico contém lógica controladora e registradores. O driver traduz operações do sistema operacional para comandos do dispositivo, administra filas, buffers, erros e conclusão. O aplicativo normalmente usa chamadas padronizadas; não precisa conhecer detalhes elétricos.

#### Polling

No polling, CPU ou driver consulta repetidamente o estado: “terminou?”. É simples e pode ser útil quando o evento é extremamente frequente, previsível ou a espera é curtíssima. Em espera longa, desperdiça ciclos e aumenta consumo. Polling não é sinônimo de E/S síncrona, embora apareçam juntos com frequência.

#### Interrupções

O dispositivo sinaliza que precisa de atenção ou concluiu. A CPU suspende o fluxo conforme prioridade, salva contexto necessário e executa uma ISR curta. Trabalho demorado deve ser diferido para contexto apropriado. A documentação de drivers Windows orienta a ISR a reconhecer o dispositivo, salvar o mínimo e agendar processamento posterior, retornando rapidamente.

Interrupção evita consulta contínua, mas tem custo de entrada, sincronização e possível tempestade de interrupções.

#### DMA

DMA permite transferência de blocos entre dispositivo e memória com menor participação da CPU em cada palavra. A CPU configura origem, destino, tamanho e direção; o mecanismo realiza a transferência e, em geral, uma interrupção sinaliza conclusão. DMA não significa “sem CPU”: há configuração, mapeamento, coerência de cache, proteção e tratamento de término.

#### Comparação operacional

~~~text
Polling: CPU pergunta repetidamente pelo estado.
Interrupção: dispositivo avisa quando requer serviço.
DMA: mecanismo transfere o bloco; interrupção pode anunciar o fim.
~~~

Os três não são mutuamente exclusivos. Um driver pode configurar DMA e receber interrupção de conclusão; pode usar polling em fase inicial e interrupções em operação normal.

<a id="s2-d5-sistemas-arquivos"></a>
### 10. Sistemas de arquivos e journaling

Sistema de arquivos organiza nomes, diretórios, metadados, conteúdo, alocação de blocos, espaço livre, proteção e recuperação. O VFS do Linux fornece uma interface comum para implementações diferentes. Conceitos centrais:

- arquivo: sequência de dados associada a metadados;
- diretório: estrutura que relaciona nomes a objetos;
- inode ou registro equivalente: metadados e referência ao conteúdo, sem ser simplesmente “o nome do arquivo”;
- descritor ou handle: referência aberta pertencente a um processo;
- montagem: associação de uma instância de sistema de arquivos ao namespace;
- cache: acelera acesso, exigindo política de sincronização com armazenamento.

#### Journaling

Journaling registra operações ou metadados em log transacional antes de consolidá-los nas estruturas principais. Após queda, o sistema pode reproduzir transações confirmadas e descartar incompletas, reduzindo o tempo e o risco de inconsistência estrutural. No ext4/JBD2, uma transação concluída termina com registro de commit; transação sem commit válido é descartada no replay.

No ext4, o modo padrão data=ordered registra no journal os metadados e força os blocos de dados associados ao sistema de arquivos principal antes de confirmar os metadados correspondentes. Isso reduz o risco de, após queda, um arquivo recém-alocado apontar para conteúdo antigo, mas não registra todo o conteúdo do arquivo no journal. Em data=journal, dados e metadados passam pelo journal antes de chegar à localização final; tende a oferecer a garantia mais forte contra inconsistência decorrente de queda, com custo maior de escrita. Há ainda data=writeback, no qual os dados podem alcançar o disco depois dos metadados; ele oferece ordenação mais fraca. Nenhum desses modos equivale a backup nem promete persistência de uma alteração que a aplicação não sincronizou conforme o contrato de E/S.

Journaling não garante que a versão desejada do documento exista, não protege contra exclusão autorizada, ransomware, incêndio ou falha simultânea da mídia. Logo, journaling não substitui backup.

<a id="s2-d5-permissoes"></a>
### 11. Permissões em Linux e Windows

#### Linux

O modelo clássico separa proprietário, grupo e outros, com bits:

- r: ler conteúdo de arquivo; em diretório, listar nomes, sujeito a detalhes de acesso;
- w: alterar arquivo; em diretório, criar/remover entradas quando combinado com acesso adequado;
- x: executar arquivo; em diretório, atravessar ou pesquisar componentes do caminho.

Cada tríade pode ser representada em octal: r = 4, w = 2, x = 1. Assim, 750 significa:

- proprietário: 7 = rwx;
- grupo: 5 = r-x;
- outros: 0 = ---.

ACLs estendidas refinam o modelo. Usuário root ou capacidades não tornam irrelevante toda política de segurança; controles adicionais podem existir.

#### Windows

Windows usa descritores de segurança e listas de controle de acesso. Uma DACL contém ACEs de permissão ou negação, podendo herdar regras de pastas. NTFS distingue direitos como leitura, gravação, modificação e controle total. Compartilhamento e NTFS podem ser avaliados em conjunto no acesso remoto; a permissão efetiva não é simplesmente “a mais alta”. O comando icacls exibe ou modifica DACLs e substitui o antigo cacls, hoje depreciado.

<a id="s2-d5-comandos"></a>
### 12. Windows e Linux — comandos pertinentes

O objetivo é compreender função e saída, não decorar opções raras nem executar comandos destrutivos.

| Finalidade | Linux | Windows |
|---|---|---|
| Processos | ps -ef, ps -eLf, top | tasklist, Get-Process, Gerenciador de Tarefas |
| Encerrar processo | kill PID; kill -TERM PID antes de -KILL | taskkill /PID; Stop-Process |
| Serviços | systemctl status NOME | Get-Service; sc query |
| Espaço e sistemas montados | df -h, findmnt | Get-Volume; Get-PSDrive |
| Memória | free -h, vmstat | Get-Counter; Gerenciador de Tarefas |
| Permissões | ls -l, chmod, chown, getfacl | icacls, Get-Acl |
| Logs | journalctl | Get-WinEvent; Visualizador de Eventos |
| Rede útil ao diagnóstico | ip addr, ip route, ss -tulpn | ipconfig, route print, Get-NetTCPConnection |

TERM solicita encerramento tratável; KILL não pode ser tratado pelo processo em sistemas POSIX. Não se conclui que KILL seja sempre melhor. Antes de encerrar um serviço corporativo, verifique dependências, transações e impacto.

## Exemplos práticos e resolvidos

### Exemplo 1 — corrida em contador

Dois workers recebem o mesmo valor 40, incrementam e gravam 41. O sistema esperava 42.

Resolução: a operação composta ler-calcular-gravar foi intercalada. Proteja o contador com mutex comum a todos os workers ou use operação atômica adequada. Criar um mutex diferente por worker não resolve, pois os participantes não se coordenam pelo mesmo objeto.

### Exemplo 2 — escolha da primitiva

Há oito slots disponíveis para processamento de relatórios. Centenas de threads podem solicitar um slot.

Resolução: semáforo contador inicializado com 8 representa diretamente a quantidade. Cada thread faz wait antes de usar e post ao sair, inclusive em erro. Um mutex permitiria uma thread, subutilizando sete slots.

### Exemplo 3 — deadlock e prevenção

O módulo de Registro bloqueia cadastro e depois cobrança. O módulo Financeiro bloqueia cobrança e depois cadastro.

Resolução: existe potencial de espera circular. Defina ordem global, por exemplo cadastro antes de cobrança, e faça ambos os módulos segui-la. Alternativamente, use tentativa de aquisição com liberação e nova tentativa controlada, transações curtas e detecção no gerenciador.

### Exemplo 4 — cálculo de Round Robin

Três processos chegam no instante 0, com bursts A = 5, B = 3 e C = 1, quantum 2 e custo de troca desprezado. A fila inicial de prontos está, por hipótese, na ordem A, B, C.

~~~text
0–2 A; 2–4 B; 4–5 C termina; 5–7 A; 7–8 B termina; 8–9 A termina
~~~

Como todos chegaram em 0, os tempos de retorno, conclusão menos chegada, são A = 9, B = 8 e C = 5. Os tempos de espera, retorno menos burst de CPU, são A = 9 − 5 = 4, B = 8 − 3 = 5 e C = 5 − 1 = 4. Os tempos de resposta, primeiro atendimento menos chegada, são A = 0, B = 2 e C = 4. A ordem não é a de conclusão do FCFS, e processo que termina antes do quantum não conserva o restante para a próxima rodada.

### Exemplo 5 — interrupção e DMA

Um adaptador precisa receber 4 MiB. A CPU configura buffers e descritores; o controlador transfere os dados diretamente para memória e sinaliza conclusão.

Resolução: o mecanismo dominante de transferência é DMA; a notificação final pode ser interrupção. Dizer que “foi interrupção, logo não houve DMA” cria falsa exclusão.

### Exemplo 6 — journaling após queda

O journal contém uma transação com descritores e dados, mas sem commit válido.

Resolução: no replay, ela deve ser tratada como incompleta e descartada. Isso preserva consistência estrutural; não prova que todo conteúdo de usuário mais recente foi persistido.

### Exemplo 7 — permissão 640

Em arquivo regular Linux, modo 640 significa proprietário rw-, grupo r-- e outros ---. Não há execução para ninguém. Em diretório, os mesmos bits teriam semântica operacional distinta, sobretudo porque ausência de x impede atravessar o caminho.

### Exemplo 8 — diagnóstico de processo

ps -eLf mostra múltiplas linhas associadas ao mesmo processo e diferentes identificadores de thread.

Resolução: a saída evidencia múltiplos fluxos no processo; não significa necessariamente múltiplos espaços de endereçamento. Para visão instantânea usa-se ps; para atualização contínua, ferramenta como top.

## Diferenças entre conceitos parecidos

| Conceitos | Diferença decisiva |
|---|---|
| Concorrência × paralelismo | Sobreposição no progresso × execução simultânea |
| Processo × thread | Contêiner isolado de recursos × fluxo escalonável que compartilha recursos do processo |
| Condição de corrida × seção crítica | Falha dependente de intercalação × trecho que precisa de proteção |
| Mutex × semáforo contador | Propriedade exclusiva × contabilização de N permissões/recursos |
| Semáforo × variável de condição | Contador com estado próprio × espera por predicado protegido por lock |
| Bloqueio × espera ativa | Thread dorme/cede CPU × thread consome CPU verificando |
| Deadlock × starvation | Ciclo ou conjunto sem progresso × participante adiado enquanto outros avançam |
| Deadlock × livelock | Participantes bloqueados × participantes ativos sem progresso útil |
| Prevenção × evitação | Quebra condição estrutural × decide concessão mantendo estado seguro |
| Detecção × recuperação | Descobre ocorrência × rompe o impasse e restaura consistência |
| FCFS × Round Robin | Ordem de chegada até bloquear/concluir × fatias de quantum em rodadas |
| Interrupção × polling | Dispositivo sinaliza × CPU consulta repetidamente |
| Interrupção × DMA | Notificação/transferência de controle × transferência de dados com menor intervenção por unidade |
| Journaling × backup | Recuperação de consistência do FS × cópia recuperável independente |
| Permissão Linux × DACL Windows | Tríades básicas e ACL POSIX × ACEs em descritor de segurança e herança NTFS |

<a id="s2-d5-revisao-fixa"></a>
## Revisão fixa do Dia 5

Este bloco sustenta as **15 questões extras de Legislação CRA/CFA** e as **5 questões extras de Língua Portuguesa** do Dia 5. O foco é aprofundar organização e funcionamento do CRA-PR e aplicar com precisão a gradação ético-disciplinar, sem repetir os eixos centrais do Dia 3.

**Revisão da Semana 1:** identificação das quatro normas, noção de Plenário, lista geral de deveres/infrações e regras de interpretação.

**Aprofundamento da Semana 2:** competências e funcionamento dos órgãos regimentais, reuniões, Ouvidoria, comissões, prazos, catálogo de infrações por faixa de sanção, diferenças PF × PJ e efeitos processuais.

<a id="s2-d5-rf-topicos"></a>
### Tópicos estudados

- delimitação normativa do cargo após a Retificação I;
- órgãos do CRA-PR e distribuição de competências;
- Plenário, Diretoria Executiva e Presidência;
- reuniões, quórum, Ouvidoria, comissões e grupos de trabalho;
- deveres, infrações, sanções, multas e garantias processuais do Código;
- Português: quantificadores, inferência, reescrita, regência do relativo, crase, pontuação e paralelismo.

<a id="s2-d5-rf-escopo"></a>
### Escopo e controle de versão

As 15 extras de Legislação do Dia 5 permanecem restritas à **Lei nº 4.769/1965**, ao **Decreto nº 61.934/1967**, ao **Regimento do CRA-PR/RN CFA nº 651/2024** e ao **Código de Ética/RN CFA nº 671/2025**.

A Retificação I substituiu, no conteúdo do concurso, a referência ao Código da RN CFA nº 640/2024 pela RN CFA nº 671/2025. As RNs CFA nº 589/2020, nº 649/2024 e nº 670/2025 e a Lei nº 12.514/2011 ficam apenas como contexto externo e **não podem servir de base material às extras deste bloco**.

<a id="s2-d5-rf-resumo"></a>
<a id="s2-d5-revisao-legislacao"></a>
### Resumo teórico: quem faz o quê no CRA-PR

| Estrutura | Função central | Limite que evita erro |
|---|---|---|
| Plenário | deliberação superior e julgamento regional | não executa sozinho toda a gestão cotidiana |
| Diretoria Executiva | direção, administração e execução das decisões | submete ao Plenário matérias que excedem sua competência |
| Presidente | representa, convoca, preside e pratica atos de gestão previstos | decisão urgente `ad referendum` volta ao colegiado competente |
| Ouvidoria | media, recebe, trata e acompanha manifestações | não possui caráter executivo, deliberativo ou decisório |
| Comissões | estudam, analisam e produzem pareceres/proposições | auxiliam; a deliberação continua com o órgão competente |
| Grupos de Trabalho | coletam dados e estudam tema específico temporariamente | não são órgãos permanentes de decisão |

<a id="s2-d5-rf-regimento-orgaos"></a>
### Regimento/RN CFA nº 651/2024: órgãos e Plenário

**Revisão da Semana 1:** CRA-PR é autarquia de direito público, tem sede na capital e jurisdição no Paraná; o Plenário é o órgão colegiado superior.

**Aprofundamento da Semana 2 — artigos relevantes:**

- **Arts. 1º e 2º:** autonomia técnica, administrativa e financeira não elimina o vínculo sistêmico; a jurisdição alcança todo o Paraná somente nas matérias da competência do CRA-PR.
- **Art. 3º:** são órgãos Plenário; Diretoria Executiva; Ouvidoria; Comissões Permanentes, Especiais e Grupos de Trabalho; e Órgãos de Representação.
- **Art. 4º:** o Plenário decide assuntos ligados às competências do CRA-PR e constitui primeira instância de julgamento em sua jurisdição.
- **Art. 5º:** o Plenário é composto por nove Conselheiros Regionais Efetivos e respectivos Suplentes; a composição renova-se, a cada dois anos, em um terço e dois terços alternadamente.
- **Art. 6º:** o mandato de Conselheiro efetivo ou suplente é de quatro anos, permitida apenas uma reeleição.
- **Art. 8º:** entre as competências do Plenário estão aprovar os Planos Anuais de Fiscalização e de Trabalho; **eleger os membros** da Diretoria Executiva e das Comissões Permanentes e empossar os membros da Diretoria; julgar processos de registro e fiscalização; julgar em primeira instância infrações profissionais; deliberar sobre orçamento e contas; apreciar pedidos de reconsideração e encaminhar recursos ao CFA; e resolver matérias regimentais de sua competência.

**Primeira instância não é última instância.** O Plenário do CRA-PR julga em primeiro grau regional nos casos previstos, enquanto o CFA exerce as funções recursais que a Lei lhe atribui. A banca costuma trocar essas posições.

<a id="s2-d5-rf-diretoria-presidente"></a>
### Diretoria Executiva e Presidente

- **Art. 17:** a Diretoria Executiva é órgão de direção do Plenário no desempenho de suas atribuições.
- **Art. 18:** sua composição inclui Presidente, Vice-Presidente, Diretor de Administração e Finanças, Diretor de Fiscalização e Registro e Diretor de Relações Institucionais.
- **Art. 20:** os Diretores são eleitos entre os Conselheiros efetivos, por escrutínio secreto e maioria absoluta, para mandato de dois anos; Presidente e Vice-Presidente concorrem em chapa conjunta.
- **Art. 23:** a Diretoria cumpre decisões do Plenário, promove administração e gestão, **homologa a instituição e a composição das Comissões Especiais e dos Grupos de Trabalho**, acompanha trabalhos técnicos e administrativos, analisa os Planos Anuais de Trabalho e de Fiscalização e os encaminha à **apreciação** do Plenário, examina orçamento, balancetes e contas antes de submetê-los ao Plenário e delibera nos limites de sua competência.
- **Art. 25:** o Presidente administra e representa legalmente o CRA-PR, convoca e preside Plenário e Diretoria, distribui processos, **institui Comissões Especiais e Grupos de Trabalho, ouvida a Diretoria Executiva**, e pratica os atos financeiros na forma compartilhada prevista no Regimento. A instituição presidencial não elimina a homologação da Diretoria prevista no art. 23.
- **Art. 25, XVIII:** assunto urgente ou inadiável pode ser resolvido `ad referendum`; isso significa decisão sujeita à apreciação posterior do colegiado competente, não substituição permanente do colegiado.

#### Plenário × Diretoria × Presidente

| Ato | Responsável predominante |
|---|---|
| aprovar Plano Anual de Fiscalização | Plenário |
| analisar o Plano e encaminhá-lo à apreciação do Plenário | Diretoria Executiva |
| convocar e presidir a sessão | Presidente |
| julgar em primeira instância infração profissional | Plenário |
| acompanhar a execução dos trabalhos administrativos | Diretoria Executiva |
| representar legalmente o CRA-PR | Presidente |
| instituir Comissão Especial ou GT, ouvida a Diretoria | Presidente |
| homologar a instituição e a composição de Comissão Especial ou GT | Diretoria Executiva |

<a id="s2-d5-rf-reunioes"></a>
### Reuniões e quórum

- **Art. 30:** Plenário e Diretoria reúnem-se ordinariamente, mediante convocação do Presidente, no mínimo uma e no máximo quatro vezes por mês.
- **Art. 31:** reunião extraordinária exige justificativa e pauta previamente definidas; pode ser convocada pelo Presidente ou requerida pela maioria absoluta do colegiado.
- **Art. 32:** reuniões podem ocorrer presencialmente ou por videoconferência, ouvido o respectivo colegiado.
- **Art. 33:** o quórum de instalação e funcionamento corresponde à maioria absoluta dos membros.

Maioria absoluta é calculada sobre o total de membros do órgão, e não apenas sobre os presentes. Não confunda quórum de instalação com maioria de votos para cada deliberação específica.

<a id="s2-d5-rf-ouvidoria-comissoes"></a>
### Ouvidoria, Comissões e Grupos de Trabalho

- **Art. 43:** o Ouvidor é eleito pelo Plenário entre os Conselheiros Regionais Efetivos, para mandato de dois anos condicionado ao mandato de Conselheiro.
- **Arts. 44 a 46:** a Ouvidoria busca melhorar serviços e interlocução; é unidade mediadora, sem caráter administrativo, executivo, deliberativo ou decisório; recebe, analisa, encaminha e acompanha manifestações e avalia a satisfação dos usuários.
- **Art. 47:** manifestações podem chegar por carta, a termo ou comunicação eletrônica.
- **Arts. 49 e 50:** Comissões auxiliam o Plenário e elaboram estudos, análises, pareceres, apresentações e proposições sujeitas à deliberação.
- **Art. 51:** são permanentes a Comissão de Análise de Contas, a Comissão Eleitoral e a Comissão de Ética e Disciplina. Salvo disposição específica, as **Comissões Permanentes têm três membros**; o Coordenador deve ser Conselheiro Efetivo. Membro da Diretoria Executiva não pode integrar a Comissão Permanente de Análise de Contas.
- **Art. 52:** Comissão Especial atende demanda específica e transitória.
- **Art. 53:** Grupo de Trabalho é temporário, coleta dados e estuda tema específico para orientar soluções e entendimentos.
- **Art. 54:** as **Comissões Especiais e os Grupos de Trabalho têm, no máximo, cinco membros**, designados pelo Presidente, ouvida a Diretoria; o ato de instituição deve indicar justificativa, competências e prazo de funcionamento.

**Ouvir não é decidir.** A Ouvidoria encaminha e acompanha; a Comissão estuda e propõe; o órgão competente delibera.

<a id="s2-d5-rf-prazos-omissoes"></a>
### Contagem de prazo e casos omissos

- **Art. 58:** salvo disposição contrária, exclui-se o dia do início e inclui-se o do vencimento; o prazo somente se inicia ou vence em dia de expediente normal do CRA-PR.
- **Art. 60:** os casos omissos no Regimento são resolvidos pelo Plenário do CRA-PR.

Não transfira automaticamente ao Presidente, à Ouvidoria ou ao CFA a competência regimental para resolver toda omissão interna.

<a id="s2-d5-rf-etica-deveres-infracoes"></a>
### Código/RN CFA nº 671/2025: deveres e catálogo de infrações

**Revisão da Semana 1:** deveres de zelo, honestidade, sigilo e independência; infrações como assinatura de fachada, obstrução da fiscalização e uso indevido do registro.

**Aprofundamento da Semana 2:** classificação pelos incisos do art. 6º, necessária para localizar a faixa de sanção.

| Faixa do art. 6º | Exemplos de infrações | Sanção-base indicada pelos arts. 19 a 22 para pessoa física |
|---|---|---|
| I a XI | falta de urbanidade; sociedade sem registro; assinar trabalho alheio sem supervisão; violar sigilo sem justa causa; dificultar fiscalização; ceder nome/registro | advertência escrita e reservada |
| XII a XVI | facilitar exercício a não habilitado; não prestar contas; descumprir normas/intimações; assédio moral ou sexual no exercício da atividade; incapacidade técnica comprovada em serviço para o qual não esteja capacitado, com risco ao patrimônio de terceiros | censura pública |
| XVII e XVIII | erros reiterados que **denotem inépcia** profissional; artifícios enganosos para vantagem indevida | suspensão de seis meses a um ano |
| XIX a XXI | ato técnico de má-fé com potencial de dano; uso de posição no Sistema para proveito pessoal; no exercício profissional, ato contrário à lei, destinado a fraudá-la ou contribuição para ilícito penal | suspensão de um a cinco anos |
| XXII | exercício da profissão durante suspensão | cancelamento do registro da pessoa física, após trânsito em julgado administrativo; inaplicável à PJ |

O art. 5º descreve deveres; o art. 6º tipifica infrações. Pode existir relação temática entre ambos, mas não se deve inventar inciso nem sanção por analogia. A gradação segue o texto do Código e o processo aplicável.

<a id="s2-d5-rf-etica-sancoes"></a>
### Sanções, PF × PJ, multas e garantias processuais

- **Art. 13:** prevê advertência escrita e reservada, censura pública, suspensão e cancelamento. Decisões de CRA que apliquem suspensão ou cancelamento são reexaminadas de ofício pelo CFA.
- **Art. 13, § 3º:** suspensão e cancelamento não se aplicam à pessoa jurídica.
- **Art. 14:** as atenuantes são taxativas e aplicáveis exclusivamente à censura e à suspensão: ausência de punição anterior; infração sob coação ou em cumprimento de ordem superior; e retratação voluntária proporcional ao ato. O Código lista uma única agravante: sanção ético-disciplinar anterior no Sistema CFA/CRAs nos últimos cinco anos.
- **Art. 15:** censura, suspensão e cancelamento, com multas, são publicados no DOU e nos sítios do CFA e do CRA competente. Advertência reservada não integra essa lista de publicação.
- **Art. 16:** suspensão ou cancelamento obriga a pessoa física a devolver a carteira; terminado o prazo de suspensão, a devolução é solicitada ao CRA e condicionada ao pagamento da multa.
- **Art. 17:** sanções constam do processo de registro. Censura e suspensão constam das certidões durante a penalidade; a advertência deve ser redigida e enviada em até quinze dias do trânsito em julgado.
- **Art. 18:** multa é aplicada conjuntamente com a sanção. Para pessoa física, as faixas são de uma a três anuidades na advertência, três a cinco na censura, cinco a dez na suspensão e dez a quinze no cancelamento. Para pessoa jurídica, advertência e censura têm a faixa própria de duas a trinta anuidades.
- **Arts. 19 a 22:** ligam os grupos de incisos do art. 6º às sanções e aos prazos correspondentes. Para pessoa física, o art. 22 torna o cancelamento aplicável ao inciso XXII e à reincidência por infração praticada dentro de cinco anos após a primeira penalização; a reincidência pressupõe nova infração depois do trânsito em julgado administrativo. O art. 13, § 3º, impede aplicar cancelamento à pessoa jurídica.
- **Art. 23:** sanção somente pode ser aplicada após o trânsito em julgado administrativo.

#### Pessoa física × pessoa jurídica

| Ponto | Pessoa física | Pessoa jurídica |
|---|---|---|
| incidência do Código | registrada e em atividade abrangida | registrada e em atividade abrangida, observadas especificidades |
| advertência/censura | aplicáveis conforme o Código | aplicáveis, com faixa própria de multa |
| suspensão/cancelamento éticos | podem ser aplicados conforme a tipificação e o processo | não se aplicam |
| carteira profissional | devolução em suspensão/cancelamento | regra incompatível com sua natureza |
| processo e trânsito | necessários | também necessários |

Não conclua que a pessoa jurídica está fora do Código porque duas sanções são incompatíveis. Também não transplante automaticamente para a PJ toda consequência concebida para o exercício individual.

<a id="s2-d5-rf-diferencas"></a>
### Diferenças entre conceitos próximos

| Conceitos | Distinção correta |
|---|---|
| primeira instância × última instância | julgamento inicial regional × apreciação recursal atribuída ao CFA |
| Plenário × Diretoria | deliberação superior/julgamento × direção e gestão executiva |
| Diretoria × Presidente | órgão colegiado de direção × agente que representa, convoca e pratica atos regimentais |
| decisão `ad referendum` × competência definitiva | providência imediata sujeita a confirmação × deliberação final do órgão competente |
| Ouvidoria × Plenário | media e encaminha × decide e julga |
| Comissão Permanente × Especial | atuação estável prevista no Regimento × demanda específica e transitória |
| Comissão × Grupo de Trabalho | analisa e produz parecer/proposição × coleta dados e estuda tema temporário |
| advertência × censura | escrita e reservada × pública |
| erros reiterados × reincidência | erros reiterados que denotem inépcia profissional (art. 6º, XVII) × nova infração após trânsito administrativo, no recorte do art. 22 |
| atenuantes × agravante | três atenuantes taxativas, só para censura/suspensão × única agravante: sanção ético-disciplinar anterior nos últimos cinco anos |

<a id="s2-d5-rf-exemplos"></a>
### Exemplos resolvidos

**Exemplo 1 — Ouvidoria.** Um usuário pede que a Ouvidoria anule decisão do Plenário. A Ouvidoria pode receber, tratar, encaminhar e acompanhar a manifestação, mas não anular a decisão, pois não tem caráter deliberativo nem decisório.

**Exemplo 2 — plano anual.** A Diretoria analisa o Plano Anual de Fiscalização e o encaminha à apreciação do Plenário; o Plenário o aprova. Trocar esses verbos desloca a competência regimental.

**Exemplo 3 — urgência.** O Presidente decide matéria inadiável `ad referendum`. A providência não elimina a posterior apreciação do colegiado competente.

**Exemplo 4 — assinatura de trabalho alheio.** Assinar documento de terceiro sem orientação ou supervisão enquadra-se no art. 6º, III. Para pessoa física, os arts. 19 e 18 vinculam a infração à advertência escrita e reservada, acompanhada da multa aplicável, após o processo.

**Exemplo 5 — vantagem fraudulenta.** Usar artifício enganoso para obter vantagem indevida corresponde ao art. 6º, XVIII; para pessoa física, a faixa é suspensão de seis meses a um ano, modulável nos termos do Código.

**Exemplo 6 — exercício durante suspensão.** Para pessoa física, voltar a exercer a profissão enquanto vigente a suspensão configura o inciso XXII e torna aplicável o cancelamento pelo art. 22, sempre após trânsito em julgado administrativo. Cancelamento não se aplica à pessoa jurídica.

**Exemplo 7 — pessoa jurídica.** Uma empresa registrada pode receber advertência ou censura e multa própria; não pode receber suspensão do exercício profissional nem cancelamento como sanções éticas.

<a id="s2-d5-rf-portugues"></a>
<a id="s2-d5-revisao-portugues"></a>
### Língua Portuguesa — base das 5 questões extras

**Revisão da Semana 1:** inferência, coesão, regência, crase, pontuação e reescrita.

**Aprofundamento da Semana 2:** alcance de quantificadores, equivalência lógica em reescritas, regência de pronome relativo, mudança de sentido por pontuação e paralelismo sintático.

#### 1. Inferência, quantificadores e palavras absolutas

- `alguns` não significa `todos` nem `somente alguns`;
- `nem todos` equivale a “pelo menos um não”, e não a `nenhum`;
- `pode` expressa possibilidade, não obrigação;
- `em regra` admite exceção; `sempre` e `sem exceção` eliminam-na;
- `até`, `apenas`, `inclusive` e `respectivamente` alteram o alcance da frase.

De “As reuniões **podem** ocorrer por videoconferência” não se infere que toda reunião deva ser remota. De “as sanções de suspensão e cancelamento não se aplicam à PJ” não se infere que nenhuma sanção ética se aplique à PJ.

#### 2. Reescrita com preservação de relação lógica

Para preservar sentido, mantenha negação, modalidade, condição e relação entre orações.

- “Embora seja mediadora, a Ouvidoria não decide” → “A Ouvidoria é mediadora, **mas** não decide.”
- “Se houver urgência, o Presidente poderá agir” não equivale a “Como há urgência, o Presidente deverá agir”.
- na voz passiva, preserve agentes e concordância: “O Plenário aprovou os planos” → “Os planos foram aprovados pelo Plenário”.

#### 3. Regência do pronome relativo e crase

A preposição exigida pelo verbo deve anteceder o relativo:

- “o órgão **a que** o processo foi encaminhado”;
- “a Ouvidoria **à qual** o cidadão se dirigiu” (`dirigir-se a` + `a qual`);
- “a decisão **de que** o usuário discordou” (`discordar de`);
- “o tema **sobre o qual** a Comissão se manifestou”.

`Cujo` indica posse, concorda com o termo posterior e não admite artigo depois: “a comissão **cujos membros** foram eleitos”, não “cujos os membros”.

#### 4. Pontuação e mudança de sentido

- oração adjetiva **restritiva**, sem vírgulas, seleciona: “Os conselheiros **que participaram da comissão** votaram.” Apenas o subconjunto indicado votou.
- oração adjetiva **explicativa**, com vírgulas, apresenta a informação como referente ao conjunto: “Os conselheiros, **que participaram da comissão**, votaram.” A leitura engloba todos os conselheiros mencionados.
- dois-pontos podem introduzir explicação ou enumeração; ponto e vírgula organiza itens complexos; vírgula não substitui livremente ponto entre orações independentes.

#### 5. Paralelismo e clareza

Elementos coordenados devem conservar forma compatível. Prefira “receber manifestações, **analisá-las e encaminhá-las**” a “receber manifestações, **análise e encaminhá-las**”.

Evite comparação incompleta: “A competência do Plenário é maior **que a Diretoria**” compara competência com órgão. Redação clara: “A competência do Plenário é mais ampla **que a da Diretoria nesse assunto**”.

<a id="s2-d5-rf-pegadinhas"></a>
### Pegadinhas do Dia 5

1. Tratar Ouvidoria ou Comissão como órgão decisório.
2. Dizer que o Plenário do CRA-PR julga sempre em última instância.
3. Trocar `analisar e encaminhar` da Diretoria por `aprovar`, competência do Plenário nos casos indicados.
4. Fazer da decisão `ad referendum` uma substituição definitiva do colegiado.
5. Confundir mandato de Conselheiro, de quatro anos, com mandato de Diretor ou Ouvidor, de dois anos.
6. Calcular maioria absoluta somente sobre os presentes.
7. Transformar Comissão Especial ou Grupo de Trabalho em estrutura permanente.
8. Afirmar que membro da Diretoria pode integrar a Comissão de Análise de Contas.
9. Incluir o dia inicial e excluir o vencimento na regra geral de prazo.
10. Publicar a advertência reservada como se integrasse a lista do art. 15.
11. Aplicar suspensão ou cancelamento éticos à pessoa jurídica.
12. Esquecer que sanção e multa são conjuntas e dependem de trânsito em julgado administrativo.
13. Confundir erros reiterados que denotem inépcia profissional com reincidência definida pelo art. 22.
14. Trocar `pode` por `deve`, `nem todos` por `nenhum` ou oração concessiva por causal.
15. Retirar preposição exigida antes do relativo: “a decisão que discordou”.
16. Inserir vírgulas em oração restritiva e afirmar que o sentido foi preservado.

<a id="s2-d5-rf-tabela"></a>
### Tabela de revisão rápida da revisão fixa do Dia 5

| ID de cobertura | Disciplina | Assunto cobrível | Regra-chave | Seção-base | Origem |
|---|---|---|---|---|---|
| D5-LEG-01 | Legislação | versão e escopo | quatro bases; RN 671 substitui a 640 no edital; normas contextuais fora das extras | `s2-d5-rf-escopo` | revisão S1 atualizada |
| D5-LEG-02 | Legislação | autonomia e jurisdição | autonomia não é soberania; jurisdição estadual e material | `s2-d5-rf-regimento-orgaos` | revisão S1 aprofundada |
| D5-LEG-03 | Legislação | órgãos do CRA-PR | lista fechada do art. 3º para a cobrança | `s2-d5-rf-regimento-orgaos` | revisão S1 + literalidade S2 |
| D5-LEG-04 | Legislação | função do Plenário | deliberação superior e primeira instância regional | `s2-d5-rf-regimento-orgaos` | aprofundamento S2 |
| D5-LEG-05 | Legislação | composição e mandatos | nove efetivos/suplentes; renovação alternada; mandato de quatro anos | `s2-d5-rf-regimento-orgaos` | aprofundamento S2 |
| D5-LEG-06 | Legislação | competências do Plenário | aprovar planos, julgar processos, deliberar sobre orçamento e contas | `s2-d5-rf-regimento-orgaos` | aprofundamento S2 |
| D5-LEG-07 | Legislação | composição da Diretoria | cinco funções regimentais e direção do Plenário | `s2-d5-rf-diretoria-presidente` | aprofundamento S2 |
| D5-LEG-08 | Legislação | Diretoria × Plenário | Diretoria analisa planos e encaminha à apreciação; Plenário aprova; Diretoria também homologa Comissão Especial/GT | `s2-d5-rf-diretoria-presidente` | aprofundamento S2 |
| D5-LEG-09 | Legislação | competências do Presidente | representação, convocação, distribuição, instituição de Comissão/GT ouvida a Diretoria e `ad referendum` | `s2-d5-rf-diretoria-presidente` | aprofundamento S2 |
| D5-LEG-10 | Legislação | reuniões e quórum | frequência, extraordinária, videoconferência e maioria absoluta | `s2-d5-rf-reunioes` | aprofundamento S2 |
| D5-LEG-11 | Legislação | Ouvidoria | media e acompanha; não decide | `s2-d5-rf-ouvidoria-comissoes` | revisão S1 aprofundada |
| D5-LEG-12 | Legislação | comissões e GT | Permanentes: três membros, salvo norma específica; Especiais/GT: máximo de cinco | `s2-d5-rf-ouvidoria-comissoes` | aprofundamento S2 |
| D5-LEG-13 | Legislação | prazo e omissão | exclui início, inclui vencimento; Plenário resolve omissão | `s2-d5-rf-prazos-omissoes` | aprofundamento S2 |
| D5-LEG-14 | Legislação | catálogo de infrações e gradação | grupos I–XI, XII–XVI, XVII–XVIII, XIX–XXI e XXII; erros que denotem inépcia | `s2-d5-rf-etica-deveres-infracoes` | revisão S1 + literalidade S2 |
| D5-LEG-15 | Legislação | PF/PJ, multa e processo | cancelamento do art. 22 só para PF; PJ sem suspensão/cancelamento; multa conjunta; trânsito administrativo; atenuantes taxativas | `s2-d5-rf-etica-sancoes` | aprofundamento S2 |
| D5-PORT-01 | Português | inferência e quantificadores | possibilidade não é obrigação; `nem todos` não é `nenhum` | `s2-d5-rf-portugues` | revisão S1 aprofundada |
| D5-PORT-02 | Português | reescrita | preservar negação, modalidade, condição, voz e agente | `s2-d5-rf-portugues` | aprofundamento S2 |
| D5-PORT-03 | Português | relativo, regência e crase | manter preposição exigida; `à qual` pode resultar em crase | `s2-d5-rf-portugues` | revisão S1 aprofundada |
| D5-PORT-04 | Português | pontuação e sentido | restritiva sem vírgulas × explicativa com vírgulas | `s2-d5-rf-portugues` | aprofundamento S2 |
| D5-PORT-05 | Português | paralelismo e clareza | coordenar estruturas equivalentes e completar comparações | `s2-d5-rf-portugues` | aprofundamento S2 |

## Tabela de revisão rápida do Dia 5

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| Concorrência | Tarefas progridem no mesmo intervalo | Exigir duas CPUs | Intercalação A-B-A em um núcleo |
| Paralelismo | Execução simultânea | Tratar como sinônimo de concorrência | A e B em núcleos distintos |
| Processo | Instância com recursos e endereço virtual | Confundir com arquivo executável | Servidor web em execução |
| Thread | Fluxo escalonável dentro do processo | Afirmar que tem heap totalmente isolado | Worker de requisição |
| Corrida | Resultado depende da intercalação | Chamar toda concorrência de corrida | Atualização perdida |
| Mutex | Exclusão com propriedade | Usá-lo para representar oito unidades | Lock de saldo |
| Semáforo | Contador atômico de permissões | Afirmar que sempre tem dono | Pool de oito conexões |
| Monitor | Estado + exclusão + condição | Reduzir a “um semáforo” | synchronized + wait/notify |
| Deadlock | Espera permanente dentro de dependência | Confundir com lentidão | A espera B; B espera A |
| Estado seguro | Existe sequência de conclusão | Dizer que todo inseguro já está morto | Banqueiro aceita ou adia pedido |
| Starvation | Adiamento indefinido individual | Exigir ciclo | Baixa prioridade nunca executa |
| Aging | Prioridade cresce com espera | Tratar como causa de starvation | Elevação gradual |
| Round Robin | Quantum em fila circular | Ignorar efeito do tamanho do quantum | Fatias de 2 ms |
| Driver | Intermedia SO e dispositivo | Confundir com controlador físico | Driver de rede |
| Interrupção | Evento desvia controle para tratamento | Dizer que transfere todo o bloco | ISR de conclusão |
| DMA | Transfere bloco com menor intervenção da CPU | Dizer que dispensa configuração | Disco para RAM |
| Journaling | Log para recuperar consistência | Chamar de backup | Replay após queda |
| 750 | rwx r-x --- | Somar bits entre tríades | Diretório privado ao grupo |

## Pegadinhas do Dia 5

1. Concorrência não exige paralelismo.
2. Threads compartilham recursos do processo, mas não compartilham a mesma pilha como regra.
3. Uma expressão de alto nível não é necessariamente atômica.
4. Volatile, sozinho, não transforma incremento composto em operação atômica.
5. Mutex diferente por thread não protege o mesmo recurso.
6. Semáforo binário e mutex não são semanticamente idênticos em todos os sistemas.
7. Espera por condição deve reavaliar o predicado após acordar.
8. As quatro condições de Coffman são necessárias em conjunto.
9. Estado inseguro não é sinônimo de deadlock consumado.
10. Timeout pode romper espera, mas não prova ausência da causa estrutural.
11. Starvation permite que o sistema continue produzindo trabalho para outros.
12. Quantum muito grande aproxima Round Robin de FCFS.
13. Prioridade alta não desbloqueia E/S inexistente.
14. Interrupção e DMA podem participar da mesma operação.
15. Polling não é sempre proibido; é inadequado quando o custo de girar supera o benefício.
16. Driver é software; controlador é hardware ou lógica de dispositivo.
17. Journaling recupera consistência, não versões apagadas.
18. Permissão de diretório não tem exatamente a mesma leitura operacional da permissão de arquivo.
19. kill -KILL não é a primeira opção administrativa normal.
20. A norma ética vigente para este concurso é a RN CFA nº 671/2025, conforme Retificação I.

## Prática guiada

### Atividade 1 — desenhar a corrida

Use as três micro-operações ler, somar e gravar para dois workers incrementando um contador inicialmente igual a 7. Produza uma intercalação que termine em 8. Depois acrescente um mutex único envolvendo as três operações e verifique que qualquer ordem serial termina em 9.

### Atividade 2 — mapa de recursos

Desenhe dois nós de thread e dois nós de recurso. Represente T1 possuindo A e pedindo B; T2 possuindo B e pedindo A. Marque as quatro condições de Coffman no próprio desenho. Em seguida, imponha A < B como ordem global e elimine a aresta capaz de fechar o ciclo.

### Atividade 3 — escolher sincronização

Classifique três casos:

- alteração de um cadastro único: mutex;
- limite de vinte tarefas simultâneas: semáforo contador;
- consumidor aguardando fila deixar de estar vazia: mutex + variável de condição.

Registre por que as duas alternativas rejeitadas seriam menos expressivas em cada caso.

### Atividade 4 — escalonamento manual

Monte uma linha do tempo para A = 4, B = 2 e C = 3, todos chegando em zero, sob FCFS e Round Robin com quantum 1. Calcule resposta e conclusão. Compare: RR melhora o primeiro atendimento de B e C, mas insere mais trocas.

### Atividade 5 — diagnóstico seguro

Interprete, sem executar encerramentos:

- ps -eLf: processos com threads;
- tasklist: processos Windows;
- systemctl status e Get-Service: estado de serviços;
- ls -l e icacls: permissões.

Para cada saída, anote o que ela permite concluir e o que não permite. Uma fotografia de CPU alta, por exemplo, não prova a causa raiz.

## Checklist do Dia 5

- [ ] Expliquei concorrência sem usar a palavra simultâneo como requisito.
- [ ] Diferenciei programa, processo e thread.
- [ ] Sei quais recursos threads compartilham e quais contextos mantêm separados.
- [ ] Demonstrei uma atualização perdida por intercalação.
- [ ] Comparei mutex, semáforo, monitor, condição e spinlock.
- [ ] Associei pipes, filas, memória compartilhada e sockets a casos adequados.
- [ ] Recitei e reconheci as quatro condições de Coffman.
- [ ] Separei prevenção, evitação, detecção e recuperação.
- [ ] Diferenciei deadlock, starvation, livelock e inversão de prioridade.
- [ ] Calculei uma linha do tempo de Round Robin.
- [ ] Comparei FCFS, SJF/SRTF, prioridade e MLFQ.
- [ ] Expliquei driver, polling, interrupção e DMA.
- [ ] Expliquei por que journaling não é backup.
- [ ] Converti permissões rwx para octal e vice-versa.
- [ ] Reconheci os comandos básicos de Windows e Linux sem confundir consulta e alteração.
- [ ] Revisei apenas o escopo CRA/CFA aplicável ao Analista.
- [ ] Corrigi inferências absolutas indevidas em texto técnico.

## Orientações para o caderno de erros

Registre cada erro com cinco campos:

1. categoria: conceito, intercalação, cálculo, comando, legislação ou leitura;
2. afirmação que levou ao erro;
3. regra correta em uma frase verificável;
4. contraexemplo mínimo;
5. gatilho de revisão.

Exemplo:

| Campo | Registro |
|---|---|
| Categoria | Conceito |
| Erro | “Concorrência exige dois núcleos” |
| Correção | Concorrência exige sobreposição de progresso no intervalo; uma CPU pode intercalar |
| Contraexemplo | A-A-B-B-A em um núcleo |
| Gatilho | Ao ler simultaneamente, verificar se o enunciado fala de progresso ou execução física |

Use marcações D1, D7 e D30 para recuperar o erro em 1, 7 e 30 dias. Não copie parágrafos inteiros; registre a distinção que faltou.

## Fontes oficiais do Dia 5

### Edital e normas

- Edital local anterior à Retificação I, preservado no projeto: ../edital/edital_cra_pr_2026_analista_sistemas_retificacao_1.pdf
- Edital oficial consolidado conforme Retificação I: https://cdnsite.institutoconsulplan.org.br/concursos/1330/b2c07c473c9749fea22728da3c964c06.pdf
- Ato oficial da Retificação I, de 22/06/2026: https://cdnsite.institutoconsulplan.org.br/concursos/1330/f8d7af1d6393470e8b6b46a4834f8e21.pdf
- Lei Federal nº 4.769/1965: https://www.planalto.gov.br/ccivil_03/leis/l4769.htm
- Decreto Federal nº 61.934/1967: https://www.planalto.gov.br/ccivil_03/decreto/Antigos/D61934.htm
- RN CFA nº 651/2024, que aprova o Regimento do CRA-PR: https://documentos.cfa.org.br/?a=show&c=documento&id=955
- RN CFA nº 671/2025, Código de Ética: https://documentos.cfa.org.br/?a=show&c=documento&id=1038

### Sistemas operacionais e padrões

- Microsoft — processos e threads: https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads
- Microsoft — prioridades de escalonamento: https://learn.microsoft.com/en-us/windows/win32/procthread/scheduling-priorities
- Microsoft — escrita de ISR: https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/writing-an-isr
- Microsoft — icacls: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls
- Microsoft — tasklist: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist
- Microsoft PowerShell — Get-Process: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process
- Linux man-pages — escalonamento: https://man7.org/linux/man-pages/man7/sched.7.html
- Linux man-pages — ps: https://man7.org/linux/man-pages/man1/ps.1.html
- Linux man-pages — chmod: https://man7.org/linux/man-pages/man1/chmod.1.html
- Linux Kernel — locking: https://kernel.org/doc/html/latest/kernel-hacking/locking.html
- Linux Kernel — visão geral do VFS: https://www.kernel.org/doc/html/latest/filesystems/vfs.html
- Linux Kernel — journal do ext4/JBD2: https://www.kernel.org/doc/html/latest/filesystems/ext4/journal.html
- Linux Kernel — DMA API: https://www.kernel.org/doc/html/latest/core-api/dma-api.html
- POSIX/Open Group — fundamentos de sincronização: https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_xsh_chap02.html
- Java Language Specification — threads, locks e monitores: https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html

---

# Dia 6 — Revisão Integrada e Estudo de Caso

## Objetivo do dia

Integrar redes, modelos OSI/TCP-IP, endereçamento, protocolos, segurança e sistemas operacionais em uma única cadeia de raciocínio. O estudante deixará de responder por “caixas” isoladas e passará a acompanhar uma requisição desde o dispositivo do usuário até o serviço, identificando em cada etapa endereço, protocolo, equipamento, controle de segurança, recurso do sistema operacional e possível falha.

O segundo objetivo é resolver um estudo de caso de conselho profissional, com rede interna, servidores, autenticação, acesso remoto, firewall, segmentação, indisponibilidade, incidente de segurança, backup e um problema de concorrência/deadlock em sistema corporativo.

## Resultados esperados

Ao final do dia, o estudante deverá ser capaz de:

- reconstruir o caminho de uma requisição da camada de aplicação ao meio físico e de volta;
- mapear as sete camadas OSI para a pilha TCP/IP sem forçar correspondência perfeita;
- identificar PDUs, endereços e equipamentos predominantes em cada camada;
- calcular rede, broadcast, faixa de hosts e capacidade a partir de máscara ou prefixo;
- distinguir MAC, IPv4, IPv6, gateway padrão, ARP e ICMP;
- associar serviços aos protocolos, transportes e portas usuais, entendendo que porta registrada não prova a aplicação real;
- comparar TCP e UDP quanto a conexão, confiabilidade, ordenação e overhead;
- aplicar confidencialidade, integridade, disponibilidade, autenticação, autorização, auditoria e não repúdio;
- distinguir ameaça, vulnerabilidade, risco e incidente;
- selecionar firewall, IDS, IPS, DMZ, VPN, TLS, segmentação, controle de acesso e backup para um cenário;
- revisar concorrência, sincronização, deadlock, escalonamento, E/S e sistemas de arquivos;
- produzir uma arquitetura técnica coerente para um órgão público sem confiar apenas na posição do equipamento na rede;
- transformar erros dos Dias 1 a 5 em um plano de recuperação ativo;
- interpretar enunciados longos, referentes, restrições e conectores sem extrapolar o texto.

## Por que o assunto importa para a prova

O próprio edital informa que cada item pode contemplar mais de uma habilidade e conhecimentos de mais de uma área. Redes e sistemas operacionais se conectam naturalmente: DNS pode responder, mas o processo web estar bloqueado; o enlace pode funcionar, mas o gateway estar errado; a conexão TCP pode abrir, mas a autorização negar acesso; o firewall pode permitir 443, mas o certificado estar inválido; o backup pode existir, mas a restauração nunca ter sido testada.

A revisão integrada também reduz erros de diagnóstico. “Sem Internet” não identifica uma camada. Pode ser associação Wi-Fi, VLAN, DHCP, ARP, rota, DNS, proxy, TLS ou aplicação. A prova explora exatamente essa troca indevida de causa por sintoma.

O estudo de caso aproxima o conteúdo das atribuições do Analista de Sistemas no CRA-PR, que incluem configuração de WAN, LAN e Wi-Fi, servidores, segurança, controle de acesso, conectividade, política de backup, auditoria, vulnerabilidades e resposta a incidentes.

## Como pode ser cobrado no estilo Instituto Consulplan

Na revisão integrada, a banca pode apresentar:

- diagrama de rede e solicitar o efeito da troca de hub, switch ou roteador;
- host, máscara e prefixo para localizar rede e broadcast;
- falha de resolução de nomes com conectividade por IP preservada;
- serviço e porta para distinguir transporte e finalidade;
- captura simplificada com ARP, ICMP, SYN ou resposta DNS;
- política de firewall e movimento entre VLANs;
- incidente de credencial comprometida com autenticação válida, mas atividade indevida;
- comparação entre hash, criptografia e assinatura;
- indisponibilidade em que backup, redundância e journaling têm papéis diferentes;
- aplicação multithread travada por lock, confundida com saturação da rede;
- assertivas I, II e III em que duas são tecnicamente verdadeiras, mas não justificam a conclusão uma da outra.

Ao ler um cenário, organize os fatos em cinco colunas: sintoma, camada, evidência, hipótese e teste. Não escolha a tecnologia apenas porque seu nome aparece no enunciado.

## Cronograma de 6h líquidas — 360 minutos

| Bloco | Tempo líquido | Atividade |
|---|---:|---|
| Diagnóstico de abertura | 15 min | Reproduzir de memória o caminho de uma requisição HTTPS |
| Fundamentos, topologias e equipamentos | 45 min | LAN/WAN, meios, domínios, switch, roteador, gateway e AP |
| OSI/TCP-IP e endereçamento | 55 min | Encapsulamento, PDUs, IPv4, IPv6, CIDR, ARP, ICMP e gateway |
| Protocolos e portas | 45 min | Serviços, TCP/UDP, DNS, DHCP, correio, administração e tradução |
| Segurança integrada | 50 min | Princípios, ataques, firewall, IDS/IPS, DMZ, VPN, TLS, Wi-Fi e backup |
| Sistemas operacionais | 45 min | Processos, sincronização, deadlock, E/S, arquivos e diagnóstico |
| Estudo de caso do conselho profissional | 75 min | Arquitetura, incidente, continuidade e deadlock corporativo |
| Revisão fixa — Português | 15 min | Interpretação, coesão, pontuação e reescrita |
| Caderno de erros | 10 min | Priorizar conceitos mais errados e planejar recuperação |
| Fechamento | 5 min | Checklist e três compromissos para a próxima semana |
| **Total** | **360 min** | **6 horas líquidas** |

## Teoria explicada de forma didática

### 1. O caminho integrado de uma requisição

Um usuário digita https://portal.exemplo.org. Uma visão simplificada:

1. a aplicação interpreta a URI e consulta DNS para obter endereço IP;
2. o host verifica sua máscara e tabela de rotas para decidir se o destino é local ou remoto;
3. se remoto, escolhe o gateway padrão como próximo salto;
4. no IPv4/Ethernet, ARP resolve o IPv4 do próximo salto em endereço MAC;
5. a camada de transporte cria conexão TCP com o destino, normalmente porta 443;
6. TLS autentica o servidor por certificado e negocia proteção criptográfica;
7. HTTP transmite a requisição sobre o canal protegido;
8. switches encaminham quadros dentro dos domínios de camada 2; roteadores encaminham pacotes entre redes;
9. firewall, proxy reverso, balanceador e aplicação aplicam políticas em pontos diferentes;
10. no servidor, processo e threads recebem a conexão, usam memória, arquivos, banco e dispositivos;
11. a resposta percorre a pilha inversa, sem obrigação de usar exatamente o mesmo caminho físico na Internet.

Cada passo oferece evidência diagnóstica. Falha de DNS não equivale a falha de roteamento. TCP estabelecido não prova que HTTP retornará sucesso. Certificado válido não autoriza o usuário na aplicação.

### 2. Redes, topologias, meios e equipamentos

Rede conecta nós para troca de dados e compartilhamento de serviços segundo protocolos. Comunicação de dados envolve emissor, receptor, mensagem, meio e regras.

#### Abrangência

- PAN: alcance pessoal, como periféricos próximos;
- LAN: área local sob administração comum;
- MAN: escala metropolitana;
- WAN: longa distância, interligando localidades;
- WLAN: LAN com enlace sem fio.

O edital nomeia redes locais e de longa distância; PAN e MAN são detalhamento didático.

#### Topologia física e lógica

Topologia física descreve cabos, portas e disposição. Topologia lógica descreve como os dados circulam e quem compartilha o meio. Uma rede pode ter estrela física em torno de equipamento central e comportamento lógico diferente conforme esse equipamento seja hub ou switch.

- barramento: meio compartilhado e falha no tronco afeta o conjunto;
- estrela: enlaces convergem ao centro; falha de enlace isola um nó, falha do centro pode afetar todos;
- anel: nós formam circuito; mecanismos de redundância podem mitigar uma ruptura;
- malha: múltiplos caminhos elevam resiliência e custo;
- híbrida: combinação de modelos.

#### Meios e interface de rede

Meios guiados confinam o sinal a um caminho físico. Par trançado e cabo coaxial conduzem sinais elétricos; o par trançado é comum em LAN. Fibra conduz luz, oferece alta capacidade, alcance e imunidade a interferência eletromagnética, mas exige transceptores, conectores e instalação adequados. Meios não guiados propagam ondas pelo espaço, como rádio, micro-ondas e infravermelho; favorecem mobilidade, mas enfrentam meio compartilhado, interferência, alcance e requisitos de autenticação e criptografia.

A placa ou interface de rede, NIC, conecta o host ao enlace. Ela transmite e recebe unidades do enlace, possui interface com o driver e pode executar funções como cálculo de checksum, filas e offload. Em Ethernet e Wi-Fi, normalmente opera com endereço MAC; isso não significa que toda tecnologia física use Ethernet nem que a NIC substitua switch, access point ou roteador.

#### Equipamentos e domínios

- repetidor regenera sinal; não interpreta endereços para separar tráfego;
- hub repete bits para as portas; todos compartilham o domínio de colisão;
- bridge filtra quadros por MAC e separa segmentos de colisão;
- switch é bridge multiporta: cada porta forma domínio de colisão próprio em operação normal; uma VLAN ainda é domínio de broadcast;
- roteador decide por endereço de camada 3 e separa domínios de broadcast;
- gateway é função de interligação ou tradução entre contextos; o gateway padrão de um host é normalmente um roteador para redes remotas;
- access point conecta estações sem fio à infraestrutura de distribuição; não é sinônimo necessário de roteador;
- firewall controla fluxo por política; pode operar em várias camadas;
- proxy atua em nome de cliente ou servidor e conhece protocolo de aplicação conforme o tipo.

VLAN cria segmentação lógica de camada 2. Comunicação entre VLANs requer função de camada 3 e política explícita.

### 3. Modelos OSI e TCP/IP

Modelos em camadas separam responsabilidades e favorecem interoperabilidade. Não se deve tratar OSI e TCP/IP como pilhas com correspondência biunívoca perfeita.

| OSI | Função principal | PDU usual | Exemplo |
|---:|---|---|---|
| 7 Aplicação | Serviços às aplicações | Dados | HTTP, DNS, SMTP |
| 6 Apresentação | Sintaxe, codificação, proteção | Dados | Formatos, transformação criptográfica |
| 5 Sessão | Diálogo e checkpoints | Dados | Controle de sessão conceitual |
| 4 Transporte | Comunicação fim a fim, portas | Segmento/datagrama | TCP, UDP |
| 3 Rede | Endereçamento e roteamento | Pacote | IPv4, IPv6, ICMP |
| 2 Enlace | Quadros no enlace e MAC | Quadro | Ethernet, Wi-Fi |
| 1 Física | Sinal e transmissão | Bits | Cabo, fibra, rádio |

Na pilha TCP/IP didática:

- aplicação agrega funções das camadas superiores do OSI;
- transporte corresponde aproximadamente à camada 4;
- internet corresponde aproximadamente à camada 3;
- acesso à rede ou enlace agrega camadas 1 e 2.

#### Encapsulamento

A aplicação produz dados. Transporte acrescenta cabeçalho TCP ou UDP. IP acrescenta cabeçalho de rede. Ethernet ou Wi-Fi cria quadro para o próximo enlace. A camada física transmite sinais. No destino, ocorre desencapsulamento.

Não existe um único quadro Ethernet que percorre todos os roteadores e apenas tem seus MACs “alterados”. Em cada salto roteado, o roteador recebe e encerra a unidade de camada 2 do enlace anterior, retira o pacote IP e cria uma nova unidade de enlace apropriada ao próximo meio. Se o próximo enlace for Ethernet ou Wi-Fi, o novo quadro usa MAC de origem da interface de saída e MAC de destino do próximo salto. Outros tipos de enlace podem usar identificadores ou encapsulamentos diferentes, sem MAC. Endereços IP identificam origem e destino de camada 3 ao longo do caminho, ressalvadas traduções como NAT; portas identificam endpoints de transporte no host.

### 4. IPv4, máscara, CIDR e sub-redes

IPv4 tem 32 bits. Máscara marca bits de rede com 1 e bits de host com 0. Prefixo /n informa quantos bits iniciais pertencem à rede.

Máscaras frequentes:

| Prefixo | Máscara | Endereços | Hosts IPv4 usuais |
|---:|---|---:|---:|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

Para sub-redes IPv4 tradicionais, hosts = 2 elevado ao número de bits de host, menos rede e broadcast. Há exceções de uso específico, como enlaces /31; não aplique a fórmula mecanicamente fora do contexto comum.

#### Cálculo resolvido — 192.168.50.77/27

O último octeto da máscara é 224. O tamanho do bloco é 256 − 224 = 32. Blocos: 0, 32, 64, 96... O valor 77 cai no bloco 64–95.

- rede: 192.168.50.64;
- broadcast: 192.168.50.95;
- hosts: 192.168.50.65 a 192.168.50.94;
- capacidade usual: 30 hosts.

#### Conversão resolvida — 255.255.255.240

Três octetos completos fornecem 24 bits. 240 em binário é 11110000, quatro bits 1. Prefixo /28.

#### Faixas importantes

- privadas RFC 1918: 10.0.0.0/8, 172.16.0.0/12 e 192.168.0.0/16;
- loopback IPv4: bloco 127.0.0.0/8, com 127.0.0.1 muito usado;
- link-local IPv4: 169.254.0.0/16, frequentemente chamada APIPA no Windows;
- endereço de rede: bits de host em zero no modelo tradicional;
- broadcast dirigido da sub-rede: bits de host em um.

Rede privada não é sinônimo de rede segura e não é roteada globalmente como endereço público sem tradução ou mecanismo apropriado.

### 5. IPv6

IPv6 tem 128 bits e representação hexadecimal. Zeros à esquerda de cada hexteto podem ser omitidos; uma única sequência contínua de hextetos zero pode ser comprimida por :: em uma representação.

Exemplo:

~~~text
2001:0db8:0000:0000:0000:0000:0000:0025
2001:db8::25
~~~

Características úteis:

- ::1 é loopback;
- fe80::/10 identifica link-local;
- não há broadcast IPv6; multicast e anycast atendem funções específicas;
- Neighbor Discovery usa ICMPv6 e não é simplesmente ARP com endereços maiores;
- /64 é prefixo comum de sub-rede, mas isso não autoriza inventar regra universal para todo contexto.

### 6. Gateway, ARP e ICMP

O host aplica a máscara para decidir se destino está no mesmo prefixo. Se local, resolve o endereço de enlace do destino. Se remoto, envia o quadro ao MAC do gateway; o pacote IP continua destinado ao host remoto.

ARP mapeia IPv4 conhecido para endereço de enlace em redes compatíveis. A solicitação costuma ser broadcast local; a resposta alimenta cache. ARP não atravessa roteadores como mecanismo geral.

ICMP transporta controle e diagnóstico, como destino inalcançável, tempo excedido e echo. Ping normalmente usa ICMP, não TCP ou UDP. Bloquear todo ICMP pode prejudicar diagnóstico e mecanismos de rede; política deve ser seletiva.

### 7. Protocolos, serviços e portas

Porta identifica serviço de transporte esperado, não garante que o tráfego observado seja benigno nem que a aplicação registrada esteja realmente ali. A IANA separa portas de sistema 0–1023, de usuário 1024–49151 e dinâmicas/privadas 49152–65535.

| Serviço | Porta usual | Transporte predominante | Função |
|---|---:|---|---|
| HTTP | 80 | TCP | Transferência de representações web sem TLS inerente |
| HTTPS | 443 | TCP; HTTP/3 usa normalmente 443/UDP via QUIC | HTTP protegido por TLS no uso clássico |
| DNS | 53 | UDP e TCP | Resolução de nomes e outros registros |
| DHCPv4 servidor/cliente | 67/68 | UDP | Configuração dinâmica de rede |
| SMTP | 25 | TCP | Transferência de correio entre servidores |
| Submission | 587 | TCP | Submissão autenticada de mensagens |
| POP3 / POP3S | 110 / 995 | TCP | Recuperação de correio, versão protegida por TLS |
| IMAP / IMAPS | 143 / 993 | TCP | Acesso e sincronização de caixas, versão protegida |
| FTP controle/dados | 21 / 20 no modo ativo clássico | TCP | Transferência de arquivos sem proteção inerente |
| SSH e SFTP | 22 | TCP | Administração segura e transferência via subsistema SSH |
| Telnet | 23 | TCP | Terminal remoto sem proteção criptográfica inerente |
| SNMP agente/trap | 161 / 162 | UDP usual | Gerência e notificações de rede |
| LDAP / LDAPS | 389 / 636 | TCP usual | Serviço de diretório; proteção conforme configuração |
| NTP | 123 | UDP | Sincronização de tempo |

Proxy não tem uma única porta obrigatória universal. Produtos usam portas configuráveis. Não transforme valores comuns, como 3128 ou 8080, em definição do protocolo.

#### DNS

DNS é base distribuída e hierárquica. Registros comuns: A para IPv4, AAAA para IPv6, CNAME para alias, MX para correio, NS para servidores autoritativos e PTR para resolução reversa. Resolver recursivo consulta em nome do cliente; servidor autoritativo responde pela zona que serve. Cache reduz latência e respeita TTL.

#### DHCPv4

No fluxo didático do DHCPv4, DORA significa Discover, Offer, Request, Acknowledgment. O cliente inicialmente pode não ter endereço utilizável, por isso usa broadcast e UDP nas portas 68/67. Relay permite atender sub-redes diferentes sem colocar servidor em cada domínio de broadcast. DHCPv6 usa outra troca de mensagens e outras portas; não se deve transportar DORA e 67/68 mecanicamente para ele.

#### Correio eletrônico

SMTP envia ou transfere mensagens. POP3 e IMAP dão acesso à caixa; IMAP mantém modelo mais rico de sincronização e pastas no servidor. “E-mail usa SMTP” não significa que SMTP seja o protocolo de leitura da caixa.

#### NAT e PAT

NAT traduz endereços. PAT ou NAPT distingue múltiplos fluxos também por portas, permitindo que muitos hosts compartilhem um endereço externo. NAT não é firewall por definição, não fornece criptografia e altera a transparência fim a fim.

#### Padrões W3C e gerência de rede

O edital também nomeia Padrões W3C e gerência de rede. O W3C publica padrões e recomendações para a plataforma Web, como famílias relacionadas a HTML, CSS, acessibilidade e arquitetura da Web. Não o confunda com a IETF, responsável por muitos protocolos formalizados em RFCs, nem com a IANA, que mantém registros de parâmetros e portas.

Gerência de rede combina inventário, configuração, desempenho, falhas, segurança e contabilização. No modelo SNMP, um gerente consulta ou recebe notificações de agentes; objetos são organizados em MIB. Trap informa evento sem confirmação no modelo tradicional, enquanto Inform oferece confirmação em versões que o suportam. Monitorar interface “up” não comprova que DNS, TLS e aplicação estejam saudáveis; observabilidade precisa correlacionar camadas.

### 8. TCP e UDP

TCP oferece fluxo de bytes orientado à conexão, confiabilidade, ordenação, detecção de perdas, retransmissão, controle de fluxo e controle de congestionamento. Usa números de sequência e confirmações. O estabelecimento clássico envolve SYN, SYN-ACK e ACK.

UDP oferece datagramas sem estabelecimento de conexão no protocolo, sem garantia de entrega, ordem ou retransmissão. Tem menor overhead básico e preserva fronteiras de datagrama. Uma aplicação sobre UDP pode implementar confiabilidade própria; portanto, “usa UDP” não significa “é necessariamente pouco confiável” no resultado da aplicação.

TCP não preserva mensagens: duas escritas podem chegar agrupadas ou fragmentadas no fluxo. A aplicação precisa delimitar seu protocolo.

### 9. Segurança de redes

#### Princípios e serviços

- confidencialidade: impedir divulgação não autorizada;
- integridade: impedir ou detectar alteração indevida;
- disponibilidade: assegurar acesso confiável e oportuno;
- autenticação: estabelecer confiança na identidade alegada;
- autorização: decidir o que a identidade autenticada pode fazer;
- auditoria/accounting: registrar ações para rastreabilidade e análise;
- não repúdio: produzir evidência verificável que dificulte negar uma ação, usualmente com assinatura e controles associados.

Autenticação vem antes da decisão de autorização no fluxo lógico, mas usuário autenticado ainda pode não ter permissão.

#### Ameaça, vulnerabilidade, risco e incidente

- ameaça: circunstância ou agente com potencial de causar dano;
- vulnerabilidade: fraqueza explorável;
- risco: combinação contextual de probabilidade e impacto;
- incidente: ocorrência que compromete ou ameaça operações ou segurança segundo os critérios organizacionais.

Uma vulnerabilidade sem exploração confirmada não é automaticamente incidente consumado, embora exija tratamento de risco.

#### Ataques

- malware: software malicioso; vírus depende de hospedeiro, worm se propaga autonomamente, ransomware busca indisponibilizar por cifragem/extorsão;
- phishing: mensagem ou página fraudulenta que induz ação;
- engenharia social: manipulação de pessoas, categoria mais ampla que phishing;
- spoofing: falsificação de identidade ou origem, como IP, ARP ou DNS conforme a técnica;
- sniffing: captura de tráfego; proteção criptográfica reduz exposição de conteúdo, não necessariamente de metadados;
- man-in-the-middle: adversário se posiciona entre partes, interceptando e possivelmente alterando;
- força bruta: tentativa sistemática de combinações; rate limiting e MFA reduzem risco;
- DoS/DDoS: esgotamento ou interrupção de serviço por uma ou várias fontes.

#### Controles

Firewall aplica política ao fluxo. Stateful acompanha estado de conexões; filtragem simples usa campos; proxy de aplicação interpreta protocolo. Regra permissiva “any-any” contradiz mínimo privilégio.

IDS detecta e alerta. IPS fica em caminho ou atua para bloquear. Assinaturas reconhecem padrões conhecidos; análise comportamental busca desvios e pode aumentar falsos positivos. Nenhum substitui correção de vulnerabilidade.

DMZ hospeda serviços expostos em segmento controlado, reduzindo acesso direto à rede interna. DMZ não é uma “zona sem segurança”. Deve ter fluxos mínimos para backend e administração.

VPN cria canal protegido sobre rede não confiável. Não torna o endpoint saudável nem concede autorização ilimitada. Acesso remoto deve combinar VPN ou mecanismo equivalente, MFA, dispositivo gerenciado, política por identidade e registro.

Segmentação limita caminhos e movimento lateral. VLAN sozinha não impõe política de camada 3; ACL ou firewall entre segmentos aplica autorização de fluxo.

#### Criptografia, hash, certificado e TLS

Criptografia simétrica usa segredo compartilhado e é eficiente para volume. Assimétrica usa par de chaves e apoia troca, assinatura e autenticação, mas não deve ser descrita como “sempre cifrar com a chave privada”. Assinatura normalmente aplica operação com chave privada sobre representação derivada; verificação usa a pública.

Hash produz resumo de tamanho fixo e não é reversível como mecanismo normal. Para senhas, use função específica com salt e custo, não hash rápido simples.

Certificado vincula identidade a chave pública por assinatura de emissor confiável. TLS negocia algoritmos, autentica conforme certificados e protege confidencialidade e integridade do canal. HTTPS não garante que o conteúdo ou negócio seja legítimo; garante propriedades do canal e identidade conforme validação.

#### Wi-Fi

WPA2 e WPA3 possuem modos Personal e Enterprise, e é importante separar autenticação/estabelecimento de chaves da cifra que protege os quadros:

- WPA2-Personal usa uma senha compartilhada, PSK, da qual se deriva material de chave; compartilhar a mesma credencial entre muitos usuários reduz individualização e torna a troca de senha operacionalmente difícil;
- WPA2-Enterprise usa 802.1X/EAP, normalmente com servidor de autenticação como RADIUS, permitindo credenciais individuais e chaves de sessão; o método EAP e a validação correta do servidor são parte da segurança;
- CCMP baseado em AES é o mecanismo de proteção de dados de referência do WPA2; TKIP é legado e não deve ser tratado como equivalente em configuração moderna;
- WPA3-Personal substitui a autenticação baseada em PSK por SAE para estabelecer o segredo compartilhado. Continua podendo usar senha, mas o SAE melhora a resistência a adivinhação offline; depois desse estabelecimento, o handshake de quatro vias deriva as chaves de tráfego;
- WPA3-Enterprise mantém 802.1X/EAP e oferece um modo de segurança de 192 bits para ambientes sensíveis, além do modo empresarial comum;
- Protected Management Frames, PMF, é obrigatório em WPA3 e protege categorias selecionadas de quadros de gerenciamento; não protege todo e qualquer quadro nem corrige credencial fraca;
- modo de transição permite clientes WPA2 e WPA3 no mesmo ambiente durante migração, mas um cliente que conecta por WPA2 não recebe automaticamente as garantias de SAE e PMF do WPA3. A compatibilidade legada amplia a superfície e precisa de prazo de retirada.

A Wi-Fi Alliance define esses perfis e certificações; portanto, WPA3 não é apenas “WPA2 com senha maior”. Segurança efetiva ainda depende de atualização de APs e clientes, configuração do EAP, credenciais, desativação de mecanismos legados, monitoramento e isolamento da rede de visitantes.

#### Backup e disponibilidade

- completo: copia todo o conjunto definido;
- incremental: copia mudanças desde o último backup de qualquer tipo; restauração exige cadeia;
- diferencial: copia mudanças desde o último completo; cresce até o próximo completo e simplifica a cadeia em relação ao incremental.

RPO é a janela máxima tolerável de perda de dados, expressa pelo ponto mais antigo aceitável de recuperação. RTO é o tempo-alvo de recuperação do serviço. Backup precisa ter cópias protegidas contra credenciais de produção, retenção, verificação de integridade e testes de restauração. Redundância mantém serviço diante de certas falhas; backup recupera estado e histórico. Um não substitui o outro.

### 10. Sistemas operacionais na cadeia de rede

Ao receber conexão, o kernel associa pacotes a socket, acorda thread ou mecanismo assíncrono, agenda CPU, aloca buffers e realiza E/S. A aplicação pode falhar mesmo quando rede está íntegra:

- pool de threads esgotado;
- deadlock entre locks;
- fila de conexões pendentes, listen backlog, saturada antes de a aplicação aceitar novas conexões;
- tabela ou limite de descritores/handles esgotado, impedindo abrir novos sockets, arquivos ou pipes;
- memória pressionada e paginação excessiva;
- disco saturado;
- permissão negada;
- sistema de arquivos somente leitura após erro;
- serviço parado ou bloqueado.

Backlog e descritores são falhas diferentes. O backlog pertence ao socket em escuta e contém conexões pendentes conforme a implementação; ele pode saturar mesmo com descritores ainda disponíveis quando a aplicação aceita devagar. Esgotamento de descritores é um limite de referências abertas por processo ou sistema e pode afetar, ao mesmo tempo, sockets, arquivos e outros objetos.

#### Escalonamento visto pelo serviço de rede

| Política didática | Preempção | Vantagem | Risco ou sintoma operacional |
|---|---|---|---|
| FCFS | Não, no modelo clássico | Simplicidade e ordem de chegada | Efeito comboio: requisição longa retarda as curtas |
| SJF | Não | Baixa espera média se o próximo burst for conhecido | Estimativa difícil e starvation de tarefas longas |
| SRTF | Sim | Favorece trabalho de curta duração | Muitas preempções e adiamento de tarefas longas |
| Prioridade | Pode ser | Atende classes críticas | Starvation; aging reduz adiamento indefinido |
| Round Robin | Sim, ao fim do quantum | Boa resposta em tempo compartilhado | Quantum pequeno eleva trocas; grande aproxima FCFS |
| Filas com realimentação | Sim | Adapta prioridade ao comportamento | Parâmetros ruins geram oscilação ou injustiça |
| Tempo real | Depende da política | Busca prazo e previsibilidade | Não significa “mais rápido”; requer admissão e parâmetros corretos |

Em diagnóstico, CPU a 100% não prova falta de capacidade: pode haver spinlock, loop de polling ou retry. CPU baixa também não prova saúde: threads podem estar bloqueadas em mutex, variável de condição, E/S ou deadlock. Latência deve ser relacionada aos estados pronto, executando, bloqueado e ao tempo de fila.

#### Sincronização e IPC na aplicação

| Mecanismo | Uso apropriado | Erro típico |
|---|---|---|
| Mutex | Proteger uma seção crítica com propriedade exclusiva | Manter o lock durante E/S remota ou usar locks em ordens distintas |
| Semáforo binário ou contador | Controlar passagem ou representar N permissões, buffers ou conexões por wait/post atômicos | Tratar como se sempre tivesse proprietário de mutex |
| Monitor + variável de condição | Encapsular estado e dormir até um predicado mudar | Testar a condição com if em vez de revalidá-la em laço sob o lock |
| Spinlock | Espera curtíssima em contexto no qual dormir é inadequado | Girar por tempo longo e consumir um núcleo |

IPC cruza fronteiras de processo: pipe/FIFO transporta fluxo de bytes; fila de mensagens preserva mensagens; memória compartilhada reduz cópia, mas exige sincronização; socket atende comunicação local ou remota; sinais/eventos notificam; RPC combina serialização e transporte, sem eliminar timeout, duplicação ou falha parcial. Monitor e variável de condição, por sua vez, são abstrações de sincronização de threads e não devem ser confundidos com um canal IPC.

#### Driver, polling, interrupção e DMA

| Elemento | Papel | Cuidado de prova e diagnóstico |
|---|---|---|
| Driver | Traduz a interface do SO para comandos, filas e buffers do dispositivo | Driver defeituoso pode causar perda mesmo com cabo e IP corretos |
| Polling | CPU ou driver consulta o estado repetidamente | Útil em espera curtíssima; prolongado consome CPU |
| Interrupção | Dispositivo notifica evento e transfere controle para tratamento curto | Tempestade de interrupções eleva custo; trabalho longo deve ser diferido |
| DMA | Controlador transfere blocos entre dispositivo e memória | CPU configura e finaliza; uma interrupção pode anunciar a conclusão |

Os mecanismos combinam-se: a NIC, por meio do driver, pode preencher buffers com DMA e gerar interrupção; sob alta taxa, o driver pode alternar para polling para amortizar interrupções. Interrupção é notificação, DMA é transferência e driver é software de controle.

#### Permissões e comandos de verificação

No Linux, rwx para proprietário, grupo e outros e ACLs controlam objetos; chmod 640 arquivo concede rw- ao dono, r-- ao grupo e nada aos demais, enquanto chown altera titularidade e getfacl/setfacl inspecionam ou ajustam ACLs. ps -eLf e top ajudam a observar processos/threads; ss -lntp relaciona sockets de escuta a processos; df -h e findmnt verificam espaço e montagem; journalctl consulta eventos. Antes de mudar permissão, confirme se o processo usa o usuário, grupo e caminho esperados.

No Windows, descritores de segurança e DACLs contêm ACEs, inclusive herdadas. icacls e Get-Acl inspecionam permissões, enquanto Set-Acl ou icacls podem alterá-las; tasklist e Get-Process mostram processos, Get-NetTCPConnection mostra conexões e Get-WinEvent consulta eventos. Em acesso remoto a arquivo, permissões de compartilhamento e NTFS participam do resultado. Conceder controle total para “testar” pode mascarar a causa e criar vulnerabilidade; primeiro compare identidade efetiva, herança e direito solicitado.

O diagnóstico deve cruzar:

- rede: link, endereço, rota, DNS, porta e perda;
- processo: estado, CPU, memória, threads e handles;
- aplicação: logs, fila, latência e erros;
- armazenamento: espaço, IOPS, integridade e permissões;
- segurança: eventos de autenticação, bloqueios e alterações.

Deadlock em aplicação pode manter conexões TCP abertas e, mesmo assim, não responder. Portanto, socket estabelecido não prova progresso do processo.

## Exemplos práticos e resolvidos

### Exemplo 1 — domínio de broadcast

Um hub é trocado por switch sem criar VLANs.

Resolução: cada porta passa a ter domínio de colisão próprio, mas o domínio de broadcast permanece, em regra, o mesmo. Para separá-lo, use VLANs e roteamento entre elas conforme política.

### Exemplo 2 — destino remoto

Host 10.10.8.20/24 acessa 10.10.9.30. Ele não faz ARP diretamente pelo MAC de 10.10.9.30; considera o destino remoto e resolve o MAC do gateway local. O endereço IP de destino do pacote continua 10.10.9.30, salvo tradução posterior.

### Exemplo 3 — DNS falho

Ping por IP ao servidor funciona, mas portal.exemplo.org não resolve.

Resolução: conectividade IP básica existe; investigue configuração do resolver, alcance ao DNS, zona, registro, cache e DNSSEC quando aplicável. Não conclua imediatamente que “a Internet caiu”.

### Exemplo 4 — porta não prova serviço

Uma captura mostra TCP destino 443.

Resolução: 443 é registrada para HTTPS, mas o número sozinho não prova conteúdo legítimo, TLS válido ou aplicação correta. Inspecione handshake, certificado e comportamento conforme autorização.

### Exemplo 5 — CIDR

Para 10.20.30.130/26, bloco = 64. Faixas no último octeto: 0–63, 64–127, 128–191, 192–255.

- rede: 10.20.30.128;
- broadcast: 10.20.30.191;
- hosts: 10.20.30.129–190;
- capacidade: 62.

### Exemplo 6 — IDS e IPS

Um sensor recebe cópia do tráfego e gera alerta sem bloquear.

Resolução: comportamento de IDS. Se estivesse em linha e descartasse o fluxo por política, seria função de IPS. Gerar alerta não corrige a vulnerabilidade explorada.

### Exemplo 7 — hash e criptografia

O órgão precisa verificar se um arquivo de backup mudou e também preservar sigilo.

Resolução: hash autenticado ou assinatura apoia integridade/autenticidade; criptografia protege confidencialidade. Só cifrar não fornece, por si, toda evidência necessária de origem; só gerar hash não oculta conteúdo.

### Exemplo 8 — indisponibilidade sem falha de rede

TCP conecta, mas requisições expiram; todas as threads aguardam dois locks em ordem oposta.

Resolução: o enlace, IP e transporte podem estar funcionais. A causa está no progresso interno da aplicação. Examine dump de threads, grafo de espera e ordem de aquisição.

## Estudo de caso — Conselho Regional de Gestão Profissional

### Cenário

Um conselho profissional fictício mantém:

- portal público e protocolo eletrônico;
- sistema interno de registro de profissionais;
- módulo financeiro de anuidades;
- diretório central de identidades;
- banco de dados e servidor de arquivos;
- acesso remoto de empregados e prestadores;
- Wi-Fi corporativo e de visitantes;
- cópias de segurança locais e externas.

Após uma manhã de alta demanda, usuários internos relatam lentidão. O portal público continua abrindo a página inicial, mas operações de atualização expiram. Minutos depois, o monitoramento detecta grande volume de autenticações VPN originadas de local incomum com credencial válida de prestador. Estações do Financeiro começam a criar arquivos com extensão desconhecida. O último relatório automático diz que os backups “concluíram”, mas não há teste de restauração recente.

No sistema corporativo, duas rotinas usam locks:

~~~text
Rotina Registro:
  lock(cadastro)
  lock(cobranca)

Rotina Financeiro:
  lock(cobranca)
  lock(cadastro)
~~~

### Arquitetura proposta

#### Segmentação e endereçamento

| Segmento | Prefixo de exemplo | Finalidade | Política essencial |
|---|---|---|---|
| VLAN 10 | 10.20.10.0/24 | Usuários administrativos | Acesso somente aos serviços necessários |
| VLAN 20 | 10.20.20.0/27 | Aplicações internas | Recebe conexões dos usuários e inicia somente fluxos definidos ao backend |
| VLAN 25 | 10.20.25.0/28 | Dados e SGBD | Aceita porta do SGBD apenas dos nós de aplicação e de administração autorizados |
| VLAN 30 | 10.20.30.0/28 | Administração de TI | Origem exclusiva de SSH/RDP/administração |
| VLAN 40 | 10.20.40.0/24 | Voz, impressoras e IoT | Sem acesso geral a servidores sensíveis |
| VLAN 50 | 10.20.50.0/24 | Visitantes | Apenas Internet, isolamento entre clientes |
| VLAN 60 | 10.20.60.0/28 | Backup | Fluxos restritos, credenciais separadas e repositório protegido |
| DMZ | 10.20.100.0/28 | Proxy reverso e portal público | Sem início de sessão livre para rede interna |

Os prefixos pertencem ao espaço privado RFC 1918. Endereços reais devem ser planejados para crescimento, sumarização e ausência de sobreposição com VPNs e filiais.

Switches gerenciáveis aplicam VLANs; roteamento inter-VLAN passa por firewall ou política de camada 3. A VLAN de visitantes não alcança recursos internos. A DMZ recebe tráfego público somente nas portas publicadas. O proxy reverso encaminha à aplicação interna em fluxo explícito; o banco fica na VLAN 25 e não é publicado na DMZ.

O firewall controla alcançabilidade de rede por origem, destino, protocolo, porta e, conforme a tecnologia, estado ou aplicação. Permitir aplicação → banco na porta do SGBD não autoriza uma consulta dentro do banco. O SGBD deve autenticar uma conta de serviço própria, autorizar apenas bancos, esquemas, tabelas e operações necessárias, proteger o canal com TLS conforme o risco e registrar acessos. Portanto, há duas decisões independentes e cumulativas: o firewall permite chegar ao serviço; o SGBD decide o que a identidade autenticada pode fazer. Uma porta aberta não equivale a GRANT, e um GRANT não deve dispensar segmentação.

#### Serviços de infraestrutura

- DHCP entrega endereço, máscara, gateway, DNS e tempo de concessão por segmento, com relay quando necessário.
- DNS interno separa nomes corporativos; resolução externa não expõe registros internos.
- NTP fornece tempo consistente, essencial para logs, certificados e correlação de incidentes.
- diretório LDAP/AD centraliza identidades, grupos e ciclo de vida;
- logs de firewall, VPN, endpoints, servidores e aplicação seguem para repositório central com controle de acesso e retenção.

#### Autenticação e autorização

Autenticação remota exige MFA. Contas de prestador têm validade, horário e recursos limitados. Autorização usa grupos e menor privilégio. Administração de servidores parte somente da VLAN 30 por bastion ou estação protegida. Contas administrativas não são usadas para e-mail e navegação cotidiana.

Não se concede confiança implícita porque a origem está “dentro” da LAN. Identidade, saúde do dispositivo, recurso solicitado e contexto participam da decisão, em linha com princípios de zero trust.

#### Acesso remoto e VPN

A VPN termina em zona controlada e não entrega acesso irrestrito. Política associa identidade a rotas ou aplicações necessárias. MFA, certificado do dispositivo, atualização, EDR e registro de sessão reduzem risco. RDP, SSH e banco não ficam expostos diretamente à Internet.

#### Firewall, IDS/IPS e DMZ

Política padrão nega o que não foi autorizado. Exemplos de fluxos:

- Internet → proxy na DMZ: TCP 443;
- proxy DMZ → aplicação: porta de backend definida, somente IPs necessários;
- aplicação → banco: porta do SGBD, somente a partir dos IPs de aplicação necessários; a conta de serviço e seus privilégios são validados separadamente pelo SGBD;
- usuários → aplicação: HTTPS interno;
- administração → servidores: portas administrativas restritas, MFA e registro;
- visitantes → Internet: permitido conforme política; visitantes → RFC1918 interno: negado;
- backup → servidores ou servidores → repositório: sentido e portas definidos; administração do backup separada.

IDS/IPS observa tentativas, anomalias e assinaturas. Regras precisam de teste e tratamento de falso positivo. Firewall não substitui patch, EDR, autenticação ou validação da aplicação.

### Diagnóstico da indisponibilidade

Há dois problemas simultâneos, e a equipe não deve forçar causa única:

1. incidente de segurança com provável uso indevido de credencial VPN e propagação de malware/ransomware;
2. deadlock entre rotinas de Registro e Financeiro, causando expiração de operações mesmo com rede disponível.

Evidências para separar:

- página inicial abre: parte do caminho HTTP/TLS e do serviço permanece;
- atualizações expiram: backend, banco, fila ou locks são suspeitos;
- autenticação VPN válida em local incomum: credencial pode estar comprometida; “válida” não significa legítima;
- extensões desconhecidas: possível cifragem maliciosa, exigindo isolamento;
- dumps de threads com ciclo cadastro ↔ cobrança: prova do deadlock;
- backups concluídos sem teste: existência lógica não prova recuperabilidade.

### Resposta ao incidente

A NIST SP 800-61 Rev. 3 apresenta recomendações de resposta a incidentes como um Community Profile do NIST Cybersecurity Framework 2.0, e não como uma sequência normativa de apenas quatro fases. O perfil distribui resultados pelas seis Funções do CSF 2.0: Govern, Identify, Protect, Detect, Respond e Recover. Govern, Identify e Protect sustentam governança, conhecimento do risco e preparação/redução de impacto; Detect, Respond e Recover tratam a descoberta, a atuação e a restauração. As subseções operacionais abaixo — contenção, análise/erradicação e recuperação — são uma organização didática do caso, não uma citação literal de fases da revisão 3.

#### Contenção inicial

1. declarar o incidente e acionar responsáveis técnicos, gestão, jurídico/LGPD e comunicação conforme critérios;
2. isolar endpoints afetados por controle de rede/EDR sem apagá-los impulsivamente;
3. bloquear a conta do prestador, encerrar sessões e revogar tokens/certificados comprometidos;
4. restringir temporariamente fluxos laterais e preservar serviços essenciais seguros;
5. proteger repositórios de backup contra credenciais e hosts comprometidos;
6. preservar logs, linha do tempo e evidências com cadeia de custódia organizacional.

Desligar tudo pode destruir evidência e ampliar indisponibilidade; manter tudo conectado pode ampliar propagação. A decisão é orientada por risco e plano.

#### Análise e erradicação

- identificar vetor inicial, escopo, contas, persistência e dados atingidos;
- comparar indicadores em VPN, firewall, diretório, EDR e servidores;
- remover persistência, corrigir vulnerabilidade e atualizar sistemas;
- rotacionar segredos afetados, começando por credenciais privilegiadas e de serviço;
- verificar se o atacante alcançou console ou chaves de backup;
- avaliar obrigações legais e comunicação com titulares/autoridades conforme fatos, não por suposição.

#### Recuperação

- reconstruir sistemas críticos a partir de base conhecida e confiável, seguindo mapa documentado de dependências e uma sequência de bootstrap;
- restabelecer primeiro infraestrutura indispensável, como energia, conectividade controlada, firewall e tempo; depois os serviços fundacionais na ordem exigida pelo ambiente, como armazenamento, DNS e identidade, tratando explicitamente dependências circulares;
- restaurar dados e SGBD de cópia anterior ao comprometimento, após verificar integridade, antes dos serviços de aplicação que deles dependem;
- recuperar backends e aplicações, depois proxy/portal e canais de usuário, salvo quando o mapa real demonstrar ordem diferente;
- testar em cada etapa funcionalidade, segurança, resolução de nomes, autenticação, sincronização e consistência antes de abrir o próximo fluxo;
- retornar por etapas, com monitoramento reforçado e possibilidade de reversão;
- medir RPO real, RTO real e lacunas;
- realizar lições aprendidas, atualizar arquitetura, playbooks e treinamento.

### Estratégia de backup

Defina:

- dados e configurações incluídos;
- completo periódico e incrementais ou diferenciais conforme RPO/RTO;
- múltiplas cópias em falhas independentes;
- ao menos uma cópia isolada, offline ou imutável conforme risco;
- conta administrativa separada da produção;
- criptografia e controle de chaves;
- retenção capaz de alcançar ponto anterior ao incidente;
- restaurações amostrais frequentes e exercício completo periódico.

Journaling ajuda o sistema de arquivos após queda, mas não recupera arquivos cifrados maliciosamente para uma versão anterior. RAID e replicação podem copiar rapidamente a corrupção. Backup versionado e protegido atende outro objetivo.

### Solução do deadlock corporativo

As quatro condições estão presentes:

- cadastro e cobrança são protegidos com exclusão;
- cada rotina mantém um lock enquanto pede o outro;
- não há retirada compulsória segura;
- a ordem oposta cria ciclo.

Correções combinadas:

1. impor ordem global: cadastro antes de cobrança em todas as rotinas;
2. reduzir duração da seção crítica e nunca fazer chamada remota lenta mantendo ambos os locks;
3. adquirir por operação transacional de mais alto nível quando possível;
4. detectar ciclo por grafo/dump e abortar vítima com rollback consistente;
5. aplicar timeout como limite operacional, seguido de rollback e retry com backoff, somente para operação idempotente ou protegida contra duplicação;
6. instrumentar tempo de espera, detentor, fila e correlação de requisição;
7. testar concorrência com caminhos de erro, cancelamento e alta carga.

Retry sem idempotência pode duplicar cobrança. A solução precisa incluir chave idempotente ou verificação transacional.

### Plano de continuidade priorizado

1. preservar pessoas, evidências e serviços essenciais;
2. isolar propagação;
3. manter portal informativo estático se transações estiverem suspensas;
4. disponibilizar procedimento contingencial aprovado para prazos críticos;
5. consultar o mapa de dependências e definir o bootstrap, incluindo infraestrutura, tempo, armazenamento, DNS e identidade sem supor que uma ordem fixa serve para todo ambiente;
6. validar a cópia antes de restaurar dados/SGBD e, então, subir aplicações, proxy e acesso de usuários conforme suas dependências;
7. validar segurança e consistência em cada estágio antes de liberar fluxos;
8. comunicar indisponibilidade com precisão, sem atribuir causa ainda não confirmada;
9. medir e corrigir lacunas de RTO/RPO e do próprio mapa de dependências.

## Diferenças entre conceitos parecidos

| Conceitos | Diferença decisiva |
|---|---|
| MAC × IP × porta | Enlace local × endereçamento roteável × endpoint de transporte |
| Switch × roteador | Encaminha quadros por MAC × encaminha pacotes e separa broadcasts |
| AP × roteador Wi-Fi | Ponte de acesso sem fio × equipamento que pode acumular AP, roteamento, NAT e firewall |
| Gateway × DNS | Próximo salto/tradução × resolução de nomes |
| OSI × TCP/IP | Modelo de referência de sete camadas × arquitetura/protocolos da Internet |
| Rede × broadcast × host | Primeiro endereço lógico × destino de todos no IPv4 tradicional × endereços atribuíveis usuais |
| IPv4 privado × link-local | Espaço interno planejável × autoconfiguração limitada ao enlace |
| ARP × DNS | IPv4 para endereço de enlace × nome para registros como IP |
| ICMP × ping | Protocolo de controle amplo × ferramenta que usa echo, entre outros testes |
| TCP × UDP | Fluxo confiável orientado à conexão × datagramas sem garantias do transporte |
| SMTP × IMAP/POP3 | Transferência/envio × acesso à caixa |
| FTP × SFTP | Protocolo FTP × subsistema de transferência sobre SSH |
| NAT × PAT | Tradução de endereço × tradução que inclui portas |
| Firewall × IDS × IPS | Controla fluxo × detecta/alerta × detecta e bloqueia em linha |
| DMZ × rede interna | Zona exposta controlada × recursos não publicados diretamente |
| Autenticação × autorização | Quem é × o que pode fazer |
| Hash × criptografia × assinatura | Resumo × confidencialidade reversível por chave × integridade/autoria verificável |
| VPN × MFA | Canal protegido × prova com múltiplos fatores |
| Redundância × backup | Continuidade imediata × recuperação de estado/histórico |
| RPO × RTO | Janela máxima tolerável de perda/ponto mais antigo aceitável × tempo-alvo de recuperação |
| Falha de rede × deadlock | Caminho de comunicação falha × aplicação não progride apesar do caminho possível |

<a id="s2-d6-revisao-fixa"></a>
## Revisão fixa do Dia 6

Esta revisão sustenta as **20 questões extras do Dia 6**: 10 de Português e 10 de revisão mista dos conteúdos e dos erros dos Dias 1 a 5. Ela não cria um novo bloco técnico autônomo. Seu papel é recuperar regras, localizar rapidamente a teoria aprofundada e transformar erros da semana em contrastes verificáveis.

Use as marcas abaixo:

- **[S1 — revisão ativa]:** conteúdo já estudado na Semana 1; aqui aparece em forma resumida, sem repetição integral da apostila anterior.
- **[S2 — aplicação/aprofundamento]:** uso novo da base anterior em textos técnicos ou conteúdo técnico desenvolvido nos Dias 1 a 5 da Semana 2.
- **[S2 — consolidação]:** integração de conteúdos da própria Semana 2, guiada pelo caderno de erros.

Tópicos deste bloco:

1. Português: ideia central; inferência e extrapolação; conectores; referentes e ambiguidade; quantificadores e termos absolutos; reescrita; concordância com `haver` e `existir`; regência e crase; pontuação; paralelismo e linguagem clara.
2. Revisão mista: redes e métricas; OSI/TCP-IP, CIDR, IPv6, ARP e ICMP; protocolos e serviços; segurança, ataques, criptografia, Wi-Fi, resposta a incidentes, RPO e RTO; concorrência, deadlock, escalonamento, entrada/saída, sistemas de arquivos e permissões.

### Bloco A — Português aplicado — 10 questões extras

A base gramatical e interpretativa está na **Semana 1, Dia 5 — Língua Portuguesa e Discursiva**, especialmente em [Interpretação de texto](../semana_01/semana_01_estudo.md#1-interpretação-de-texto), [Semântica e coesão](../semana_01/semana_01_estudo.md#2-semântica-e-coesão), [Sintaxe, concordância e regência](../semana_01/semana_01_estudo.md#3-sintaxe-concordância-e-regência), [Crase](../semana_01/semana_01_estudo.md#4-crase), [Pontuação](../semana_01/semana_01_estudo.md#5-pontuação) e [Reforço de alinhamento com as questões — Dia 5](../semana_01/semana_01_estudo.md#reforço-de-alinhamento-com-as-questões---dia-5). Na Semana 2, a novidade é aplicar essas regras a protocolos, segurança e sistemas operacionais, sem deixar o vocabulário técnico encobrir a estrutura linguística.

<a id="s2-d6-rf-pt-01"></a>
#### D6-RF-PT-01 — Ideia central

**Origem:** [S1 — revisão ativa] conceito de ideia central; [S2 — aplicação] textos técnicos com ressalvas e condições.

A ideia central combina **assunto + afirmação principal do autor**. Um detalhe verdadeiro, um exemplo ou uma consequência secundária não substitui a tese do trecho. Método:

1. elimine exemplos, números e explicações acessórios;
2. identifique o que se repete ou organiza as demais frases;
3. preserve condições e ressalvas presentes no texto;
4. formule o núcleo em uma frase que abranja o trecho inteiro.

Exemplo: “A segmentação reduz o alcance de certos fluxos; contudo, não substitui autenticação, correções e monitoramento.” A ideia central é que **segmentação reduz parte do risco, mas integra um conjunto de controles**. “A segmentação reduz fluxos” é detalhe incompleto; “segmentação garante segurança” contradiz a ressalva.

**Pegadinha:** escolher uma afirmação tecnicamente verdadeira, porém periférica, ou eliminar o limite introduzido por `contudo`.

<a id="s2-d6-rf-pt-02"></a>
#### D6-RF-PT-02 — Inferência e extrapolação

**Origem:** [S1 — revisão ativa] diferença entre inferir e acrescentar opinião; [S2 — aplicação] limites de garantias técnicas.

- **Inferência:** conclusão necessária ou razoavelmente autorizada pelas premissas textuais.
- **Extrapolação:** introdução de causa, certeza, universalidade, finalidade ou consequência não sustentada.

Exemplo: “O UDP não oferece retransmissão no transporte; a aplicação pode implementar recuperação.” É válido inferir que **a ausência de retransmissão nativa do UDP não impede recuperação em outra camada**. É extrapolação afirmar que “toda aplicação UDP recupera perdas” ou que “UDP sempre supera TCP”.

Teste de segurança: a conclusão continua válida se forem removidos seus conhecimentos externos? Se depender de uma suposição que o texto não forneceu, é extrapolação.

**Pegadinha:** transformar `pode` em `deve`, `reduz` em `elimina` ou um caso particular em regra universal.

<a id="s2-d6-rf-pt-03"></a>
#### D6-RF-PT-03 — Conectores e relação lógica

**Origem:** [S1 — revisão ativa] coesão sequencial; [S2 — aplicação] encadeamento de diagnóstico e resposta.

| Relação | Conectores frequentes | Regra de leitura | Troca que altera o sentido |
|---|---|---|---|
| oposição/ressalva | mas, porém, contudo, entretanto | a segunda ideia limita ou contrasta a primeira | trocar por `portanto` |
| concessão | embora, ainda que, mesmo que | admite um obstáculo que não impede o fato principal | trocar por `porque` |
| causa/explicação | porque, visto que, uma vez que | apresenta motivo ou justificativa | trocar por `apesar de` |
| conclusão | portanto, logo, assim, por isso | deriva resultado do que veio antes | trocar por `contudo` |
| condição | se, caso, desde que | estabelece requisito ou hipótese | trocar por causa certa |
| finalidade | para que, a fim de que | apresenta objetivo | trocar por consequência já ocorrida |
| adição | além disso, também, bem como | soma argumentos compatíveis | tratar como oposição |

Exemplo: “Embora o ping respondesse, o serviço permaneceu indisponível, porque as threads estavam em deadlock; portanto, a equipe investigou a aplicação.” `Embora` é concessivo; `porque` introduz a causa apresentada; `portanto` anuncia a conclusão operacional.

**Pegadinha:** aceitar a substituição porque os conectores parecem formais, sem verificar a relação lógica.

<a id="s2-d6-rf-pt-04"></a>
#### D6-RF-PT-04 — Referentes, coesão e ambiguidade

**Origem:** [S1 — revisão ativa] coesão referencial; [S2 — aplicação] relatórios técnicos com vários agentes e objetos.

Pronomes, elipses e expressões como `isso`, `tal medida`, `ele`, `seu` e `o qual` devem retomar um antecedente compatível em gênero, número e sentido. Proximidade ajuda, mas não decide sozinha: o contexto precisa produzir uma leitura coerente e única.

Frase ambígua: “O analista informou ao gestor que seu acesso seria revogado.” `Seu` pode retomar o analista ou o gestor.

Reescritas claras:

- “O analista informou ao gestor que **o acesso do gestor** seria revogado.”
- “O analista informou ao gestor que **o próprio analista perderia o acesso**.”

Em “O IPS bloqueou a conexão, e isso reduziu a exposição”, `isso` retoma o bloqueio da conexão, e não necessariamente o IPS como equipamento.

**Pegadinha:** presumir que `seu` sempre retoma o termo mais próximo ou aceitar uma reescrita que troca o responsável pela ação.

<a id="s2-d6-rf-pt-05"></a>
#### D6-RF-PT-05 — Quantificadores, modalidade e palavras absolutas

**Origem:** [S1 — revisão ativa] alcance lógico; [S2 — aplicação] garantias e exceções técnicas.

| Forma | Alcance correto | Inferência proibida frequente |
|---|---|---|
| todo A é B | A está contido em B | todo B é A |
| algum A é B | existe ao menos um A que é B | todo A é B |
| nenhum A é B | não existe elemento que seja simultaneamente A e B | nenhum A existe |
| nem todo A é B | existe ao menos um A que não é B | nenhum A é B |
| pode | possibilidade ou permissão, conforme o contexto | obrigatoriedade ou ocorrência certa |
| deve | obrigação ou forte expectativa, conforme o contexto | mera possibilidade |
| em regra | regra geral com possibilidade de exceção | sempre, sem exceção |
| somente/apenas | restrição do conjunto ou da condição | relação recíproca não expressa |

Termos como `sempre`, `nunca`, `todos`, `somente`, `garante`, `elimina` e `necessariamente` não são errados por natureza; exigem apoio integral da teoria ou do texto.

Exemplo: “Um IDS **pode** alertar sobre atividade maliciosa” não equivale a “todo IDS **sempre** bloqueia a atividade”.

**Pegadinha:** converter possibilidade em certeza, regra em universal ou negação parcial em negação total.

<a id="s2-d6-rf-pt-06"></a>
#### D6-RF-PT-06 — Reescrita sem alteração de sentido

**Origem:** [S1 — revisão ativa] equivalência semântica; [S2 — aplicação] períodos técnicos com condições e negações.

Uma reescrita equivalente deve preservar:

1. sujeito e responsável pela ação;
2. afirmação ou negação;
3. tempo e modalidade verbal;
4. quantificadores e exceções;
5. relação do conector;
6. condição, causa e consequência;
7. referente dos pronomes;
8. correção gramatical.

Original: “Ainda que o backup esteja íntegro, a restauração precisa ser testada.”

Equivalente: “Embora o backup esteja íntegro, é necessário testar a restauração.”

Não equivalente: “Como o backup está íntegro, é desnecessário testar a restauração.” A concessão virou causa e a necessidade foi negada.

**Pegadinha:** manter quase todas as palavras, mas trocar `não elimina` por `elimina`, `pode` por `deve` ou concessão por causa.

<a id="s2-d6-rf-pt-07"></a>
#### D6-RF-PT-07 — Concordância: `haver` e `existir`

**Origem:** [S1 — revisão ativa] concordância verbal; [S2 — aplicação] inventários de falhas e incidentes.

- `Haver` com sentido de **existir, ocorrer ou tempo decorrido** é impessoal e fica na terceira pessoa do singular: `havia falhas`, `houve incidentes`, `há dois dias`.
- Em locução verbal com `haver` impessoal, o auxiliar também permanece no singular: `deve haver registros`; `pode ter havido tentativas`.
- `Existir`, `ocorrer` e `acontecer` possuem sujeito e concordam com ele: `existiam falhas`; `ocorreram incidentes`.
- Como auxiliar, `haver` não segue a regra da impessoalidade: `os servidores haviam concluído o backup`.

Comparação:

- correta: “**Havia** duas vulnerabilidades no serviço.”
- correta: “**Existiam** duas vulnerabilidades no serviço.”
- incorreta no sentido existencial: “**Haviam** duas vulnerabilidades no serviço.”

**Pegadinha:** concordar o `haver` existencial com o termo plural posposto ou manter `existir` no singular diante de sujeito plural.

<a id="s2-d6-rf-pt-08"></a>
#### D6-RF-PT-08 — Regência e crase

**Origem:** [S1 — revisão ativa] regência nominal/verbal e fusão de preposição com artigo; [S2 — aplicação] linguagem administrativa e de segurança.

A crase ocorre quando o termo anterior exige preposição `a` e o termo posterior admite artigo feminino `a/as` ou integra pronome demonstrativo iniciado por `a`.

Regências úteis:

- obedecer **a** uma regra → obedecer **à** regra;
- referir-se **a** uma política → referir-se **à** política;
- visar **a** um objetivo, no sentido de pretender;
- acesso **a** dados → acesso **aos** dados / acesso **às** informações;
- compatível **com** o protocolo, e não `compatível ao protocolo` na construção padrão aqui adotada.

Testes práticos:

- troque o feminino por masculino: `referiu-se ao regulamento` → `referiu-se à norma`;
- use a volta: `vou à diretoria, volto da diretoria`; `vou a Curitiba, volto de Curitiba`;
- antes de verbo, não há artigo: `começou a restaurar`, sem crase.

Exemplos: “A política se aplica **às redes** internas”; “o relatório foi entregue **àquela equipe**”; “o técnico começou **a analisar** os logs”.

**Pegadinha:** inserir crase apenas porque a palavra seguinte é feminina ou omiti-la quando regência e artigo coexistem.

<a id="s2-d6-rf-pt-09"></a>
#### D6-RF-PT-09 — Pontuação e mudança de sentido

**Origem:** [S1 — revisão ativa] usos e proibições da vírgula; [S2 — aplicação] enumerações e orações técnicas.

Não separe por vírgula:

- sujeito e verbo: `Os logs do firewall permitiram a correlação`;
- verbo e complemento essencial: `A equipe preservou os registros`;
- nome e complemento essencial: `a necessidade de restauração`.

Use vírgula, entre outros casos, para:

- adjunto adverbial deslocado: `Após a contenção, a equipe preservou a imagem`;
- aposto explicativo: `O DNS, sistema distribuído de nomes, usa registros de vários tipos`;
- oração adverbial anteposta: `Embora o host respondesse, a aplicação falhava`;
- itens de enumeração: `conter, erradicar, recuperar e aprender`.

A pontuação pode mudar o conjunto referido: `Os servidores que estavam vulneráveis foram isolados` restringe o isolamento aos vulneráveis; `Os servidores, que estavam vulneráveis, foram isolados` apresenta a vulnerabilidade como explicação atribuída a todos os servidores mencionados.

**Pegadinha:** tratar toda pausa da fala como vírgula ou afirmar que retirar vírgulas explicativas nunca altera o sentido.

<a id="s2-d6-rf-pt-10"></a>
#### D6-RF-PT-10 — Paralelismo e linguagem técnica clara

**Origem:** [S1 — revisão ativa] coesão, correção e organização textual; [S2 — aprofundamento] redação de procedimentos e relatórios técnicos.

Elementos coordenados devem manter forma sintática equivalente.

- sem paralelismo: “A equipe deve **isolar os hosts**, **a revogação das credenciais** e **que preserve os logs**.”
- com paralelismo: “A equipe deve **isolar os hosts, revogar as credenciais e preservar os logs**.”

Clareza técnica exige agente identificável, verbo preciso, referente inequívoco e ordem operacional compreensível. Linguagem clara não é linguagem imprecisa nem necessariamente a mais curta.

- vago: “Foi feita uma verificação e isso foi resolvido.”
- claro: “A equipe de infraestrutura validou o certificado do servidor e corrigiu a cadeia intermediária.”

Evite nominalizações e redundâncias quando escondem a ação: `realizar a execução da restauração` pode ser `restaurar`; `planejamento prévio antecipado` repete a ideia.

**Pegadinha:** considerar correta uma enumeração que mistura substantivos, infinitivos e orações, ou preferir frase rebuscada que deixa agente e referente incertos.

<a id="s2-d6-rf-pt-tabela"></a>
#### Tabela de revisão rápida — Português

| ID estável | Núcleo | Regra decisiva | Diferença próxima | Pegadinha de prova | Origem |
|---|---|---|---|---|---|
| D6-RF-PT-01 | ideia central | assunto + afirmação que organiza o trecho | ideia central × detalhe verdadeiro | escolher exemplo periférico | S1 revisado; aplicação técnica S2 |
| D6-RF-PT-02 | inferência | conclusão autorizada pelas premissas | inferência × extrapolação | acrescentar certeza ou causa | S1 revisado; limites técnicos S2 |
| D6-RF-PT-03 | conectores | preservar a relação lógica | concessão × causa; oposição × conclusão | trocar conector por aparência formal | S1 revisado; diagnóstico S2 |
| D6-RF-PT-04 | referente | antecedente compatível e inequívoco | proximidade × coerência referencial | `seu` com dois antecedentes | S1 revisado; relatório técnico S2 |
| D6-RF-PT-05 | quantificador | conservar alcance e modalidade | `nem todo` × `nenhum`; `pode` × `deve` | universalização indevida | S1 revisado; garantias S2 |
| D6-RF-PT-06 | reescrita | preservar agente, negação, relação e condição | forma diferente × sentido diferente | concessão virar causa | S1 revisado; períodos técnicos S2 |
| D6-RF-PT-07 | concordância | `haver` existencial é impessoal; `existir` concorda | `havia falhas` × `existiam falhas` | `haviam falhas` | S1 revisado; inventário S2 |
| D6-RF-PT-08 | crase/regência | preposição `a` + artigo `a/as` | `à norma` × `a analisar` | crase por mera feminilidade | S1 revisado; texto administrativo S2 |
| D6-RF-PT-09 | pontuação | não separar termos essenciais; isolar deslocamentos/explicações | restritiva × explicativa | vírgula entre sujeito e verbo | S1 revisado; texto técnico S2 |
| D6-RF-PT-10 | paralelismo/clareza | coordenar formas equivalentes e explicitar agente | concisão × vagueza | mistura de infinitivo, nome e oração | S1 revisado; procedimento S2 |

Recuperação de 30 segundos antes de cada questão de Português: **comando → quantificadores → conectores → referentes → regra gramatical → sentido preservado**.

### Bloco B — Revisão mista e caderno de erros — 10 questões extras

As questões D6-RF-MX-01 a D6-RF-MX-10 devem usar conteúdos já explicados nos Dias 1 a 5. O mapa abaixo é a base obrigatória do comentário: cada comentário deve citar ao menos o **ID do núcleo** e a **seção real indicada**, além de explicar a regra que decide a resposta.

<a id="s2-d6-rf-mapa"></a>
#### Mapa localizador dos Dias 1 a 5

| ID / núcleo ou erro recorrente | Dia | Seção/âncora real da teoria | Regra-chave | Pegadinha prioritária | Origem S1/S2 |
|---|---:|---|---|---|---|
| **D6-RF-MX-01 — redes, métricas, topologias, alcance, meios, equipamentos e domínios** | 1 | [Comunicação de dados](#s2-d1-comunicacao-dados); [Topologias](#s2-d1-topologias); [PAN/LAN/MAN/WAN](#s2-d1-alcance); [Meios](#s2-d1-meios); [NIC](#s2-d1-nic); [Repetidor e hub](#s2-d1-repetidor-hub); [Bridge e switch](#s2-d1-bridge-switch); [Roteador, gateway e AP](#s2-d1-roteador-gateway-ap); [Domínios de colisão e broadcast](#s2-d1-dominios) | largura de banda é capacidade; throughput é vazão efetiva; goodput é carga útil; latência é atraso; jitter é sua variação. A NIC conecta o host ao enlace; repetidor regenera sinal e hub o repete a todas as demais portas. Topologia física não determina sozinha a lógica. Switch separa colisões por porta; VLAN/roteamento delimitam broadcasts. | “1 Gbit/s garante goodput de 1 Gbit/s”; “NIC identifica o usuário”; “hub aprende MAC”; “estrela sempre tem o mesmo comportamento”; “switch elimina broadcast”. | S2 — conteúdo novo do Dia 1 |
| **D6-RF-MX-02 — OSI/TCP-IP, encapsulamento, PDU e endereço por camada** | 2 | [Modelo OSI](#s2-d2-osi); [Modelo TCP/IP](#s2-d2-tcpip); [Encapsulamento](#s2-d2-encapsulamento); [PDUs](#s2-d2-pdus); [MAC](#s2-d2-mac) | OSI é modelo de referência; TCP/IP é arquitetura/suíte. Dados recebem controles por camada. Quadro e MAC valem no enlace local; pacote IP é roteado; TCP entrega segmento/fluxo e UDP, datagramas. | correspondência perfeita entre modelos; chamar toda PDU de pacote; dizer que o quadro atravessa roteadores intacto. | S2 — conteúdo novo do Dia 2 |
| **D6-RF-MX-03 — IPv4, máscara, CIDR e sub-redes** | 2 | [IPv4](#s2-d2-ipv4); [Máscara e CIDR](#s2-d2-mascara); [Rede, broadcast e hosts](#s2-d2-rede-broadcast-hosts); [Cálculos resolvidos](#s2-d2-calculos); [Sub-redes](#s2-d2-subredes) | no modelo didático convencional, em `/n`, `n` bits são de prefixo. Para `/1`–`/30`, localize o primeiro octeto da máscara diferente de `255` — inclusive `0` — e use bloco = `256 − esse octeto`; rede tem bits de host 0 e broadcast, 1. Hosts usuais = `2^(32−n)−2`. `/0` (`0.0.0.0/0`) representa a rota padrão que corresponde a qualquer destino IPv4; `/31` e `/32` têm semânticas especiais. | confundir quantidade de endereços com hosts; ignorar octeto relevante igual a `0`; tratar `/0` como LAN comum; somar no octeto errado; aplicar `−2` mecanicamente a `/31` e `/32`. | S2 — conteúdo novo e cálculo do Dia 2 |
| **D6-RF-MX-04 — IPv6, gateway, ARP, ICMP e Neighbor Discovery** | 2 | [Gateway padrão](#s2-d2-gateway); [ARP](#s2-d2-arp); [ICMP e ICMPv6](#s2-d2-icmp); [IPv6](#s2-d2-ipv6); [Endereços especiais](#s2-d2-publicos-privados-especiais) | destino local é entregue diretamente; destino remoto usa o próximo salto. ARP associa IPv4 a endereço de enlace no contexto estudado. ICMP é controle/erro/diagnóstico; `ping` é apenas um uso. IPv6 tem 128 bits, não usa broadcast e emprega ICMPv6/Neighbor Discovery. | ARP resolver nome; gateway ser usado para todo destino; ICMP ser sinônimo de ping; criar broadcast IPv6; chamar ND de ARP puro. | S2 — conteúdo novo do Dia 2 |
| **D6-RF-MX-05 — protocolo/serviço/porta, TCP/UDP, HTTP(S), DNS e DHCPv4** | 3 | [Protocolo, serviço, porta e socket](#s2-d3-protocolo-porta); [TCP × UDP](#s2-d3-tcp-udp); [HTTP e HTTPS](#s2-d3-http-https); [DNS](#s2-d3-dns); [DHCP](#s2-d3-dhcp) | porta é convenção de endpoint, não prova de conteúdo. TCP entrega fluxo ordenado e confiável, não sucesso da aplicação; UDP entrega datagramas sem garantias nativas. HTTPS é HTTP sobre TLS; HTTP/3 usa normalmente `443/UDP` via QUIC. DNS resolve/publica dados e usa UDP e TCP; DHCPv4 entrega configuração pela sequência DORA e usa 67/68 UDP. | “porta 443 torna tudo seguro”; “UDP impede confiabilidade na aplicação”; “DNS somente UDP”; “DHCPv4 resolve nomes”. | S2 — conteúdo novo do Dia 3 |
| **D6-RF-MX-06 — correio, arquivos/acesso remoto, SNMP, LDAP, proxy, NAT/PAT e NTP** | 3 | [Correio eletrônico](#s2-d3-email); [FTP, FTPS, SFTP, SSH e Telnet](#s2-d3-transferencia-remota); [SNMP](#s2-d3-snmp); [LDAP](#s2-d3-ldap); [Proxy](#s2-d3-proxy); [NAT e PAT](#s2-d3-nat-pat); [NTP](#s2-d3-ntp); [Portas conhecidas](#s2-d3-portas) | SMTP envia/transfere; POP3/IMAP acessam. FTPS é FTP+TLS; SFTP usa SSH. SNMP gerencia objetos; LDAP acessa diretórios; proxy representa extremo; NAT traduz endereço e PAT também porta; NTP sincroniza relógio. | SMTP para leitura; SFTP como FTP+TLS; SNMPv3 automaticamente seguro; LDAP como SQL; proxy como NAT; NAT como firewall; NTP como fuso. | S2 — conteúdo novo do Dia 3 |
| **D6-RF-MX-07 — gestão de risco, CIA, AAA, malware e ataques** | 4 | [Gestão de risco](#s2-d4-gestao-risco); [Tríade CIA](#s2-d4-cia); [identidade e auditoria](#s2-d4-identidade-auditoria); [conceitos de risco](#s2-d4-conceitos-risco); [malware](#s2-d4-malware); [phishing](#s2-d4-phishing); [ataques de rede](#s2-d4-ataques-rede) | risco deve ser identificado, analisado, tratado e monitorado conforme contexto, probabilidade e impacto; nenhum produto isolado o elimina. Confidencialidade limita divulgação; integridade limita alteração; disponibilidade garante acesso oportuno. Autenticar é provar identidade; autorizar é conceder ação. Ameaça pode explorar vulnerabilidade e gerar impacto; incidente é ocorrência concreta. Spoofing falsifica, sniffing observa, on-path intercepta/altera, DoS/DDoS afeta disponibilidade. | risco zero por produto único; autenticação implicar autorização; ameaça ser igual a vulnerabilidade; vírus ser igual a worm; sniffing sempre alterar; DDoS ter uma única origem. | S2 — conteúdo novo do Dia 4 |
| **D6-RF-MX-08 — controles, firewall/IDS/IPS/DMZ/VPN, criptografia e Wi-Fi** | 4 | [Controles](#s2-d4-controles); [firewall](#s2-d4-firewall); [IDS/IPS](#s2-d4-ids-ips); [DMZ](#s2-d4-dmz); [VPN](#s2-d4-vpn); [segmentação](#s2-d4-segmentacao); [criptografia](#s2-d4-criptografia); [hash/HMAC](#s2-d4-hash-hmac-senhas); [assinatura/certificado](#s2-d4-assinatura-certificado); [TLS](#s2-d4-tls); [Wi-Fi](#s2-d4-wifi) | defesa é composta. Firewall aplica política; IDS detecta/alerta; IPS atua em linha; DMZ contém exposição; VPN protege canal, não endpoint. Cifra é reversível com chave; hash é resumo; HMAC usa segredo; assinatura usa chave privada e é verificada com a pública; certificado vincula identidade e chave. WPA3-Personal usa SAE, mas configuração e senha ainda importam. | controle único como garantia absoluta; IDS bloquear sempre; DMZ ser confiável; hash cifrar; assinatura esconder conteúdo; certificado provar honestidade; modo de transição equivaler a WPA3 puro. | S2 — conteúdo novo do Dia 4 |
| **D6-RF-MX-09 — resposta a incidentes, backup, RPO e RTO** | 4 | [Resposta a incidentes](#s2-d4-resposta-incidentes); [backup e disponibilidade](#s2-d4-backup) | preparar/detectar/analisar, conter, erradicar e recuperar são objetivos distintos; preserve evidências e registre lições. RPO é a janela máxima tolerável de perda de dados, expressa pelo ponto mais antigo aceitável de recuperação; RTO é o prazo desejado para restabelecer o serviço. Backup recupera estado; redundância/alta disponibilidade reduzem interrupção. | restaurar antes de remover persistência; apagar evidência na contenção; chamar RAID de backup; confundir RPO com duração e RTO com frequência de cópia. | S2 — conteúdo novo do Dia 4 |
| **D6-RF-MX-10 — concorrência, deadlock, escalonamento, E/S, sistemas de arquivos, permissões e comandos** | 5 | [Concorrência](#s2-d5-concorrencia-paralelismo); [processo/thread](#s2-d5-processo-thread); [corrida](#s2-d5-corrida-atomicidade); [sincronização](#s2-d5-sincronizacao); [IPC](#s2-d5-ipc); [deadlock](#s2-d5-deadlock); [starvation/livelock](#s2-d5-starvation-livelock); [escalonamento](#s2-d5-escalonamento); [E/S](#s2-d5-dispositivos-e-s); [sistemas de arquivos](#s2-d5-sistemas-arquivos); [permissões](#s2-d5-permissoes); [comandos Windows/Linux](#s2-d5-comandos) | concorrência não exige simultaneidade; corrida depende de intercalação; sincronização protege invariantes. Deadlock é um impasse conjunto sem progresso causado por dependências entre participantes; as quatro condições de Coffman devem coexistir no caso clássico. Escalonamento distingue espera, retorno e resposta. Polling consulta; interrupção sinaliza; DMA transfere blocos com menor intervenção da CPU. Journaling recupera consistência, não dados históricos. Permissões e saídas de comandos devem ser lidas por sujeito, direito e finalidade. | corrida como deadlock; semáforo contador como mutex idêntico; estado inseguro como deadlock ocorrido; quantum ignorado; DMA eliminar CPU; journaling ser backup; somar bits entre tríades Linux; tratar comando de observação como alteração. | S1 — base de processos, threads, escalonamento, concorrência, deadlock, E/S, sistemas de arquivos e Windows/Linux no Dia 2; S2 — aprofundamento e comandos aplicados no Dia 5 |

As referências do mapa usam âncoras explícitas dos Dias 1 a 5. Os IDs `D6-RF-MX-*` são estáveis e devem acompanhar questões, gabaritos e registros no caderno de erros, ainda que a posição das seções mude no arquivo.

<a id="s2-d6-rf-mapa-revisoes-fixas"></a>
#### Mapa complementar — revisões fixas dos Dias 1 a 5

Este mapa recupera as disciplinas recorrentes que não pertencem ao núcleo técnico das dez questões mistas. Português já está consolidado no **Bloco A**; as linhas abaixo localizam Legislação CRA/CFA, Administração Pública e RLM.

| Dia / disciplina | Seção e âncoras reais | Regra-chave para recuperação | Pegadinhas prioritárias | Origem S1/S2 |
|---|---|---|---|---|
| **Dia 1 — Legislação CRA/CFA** | [Revisão fixa do Dia 1](#s2-d1-revisao-fixa); [núcleo de Legislação](#s2-d1-revisao-legislacao); [base legal](#s2-d1-revisao-base-legal); [CFA × CRA](#s2-d1-revisao-cfa-cra); [registro e fiscalização](#s2-d1-revisao-registro); [ética](#s2-d1-revisao-etica) | A Lei nº 4.769/1965 estrutura o exercício profissional e o Sistema CFA/CRAs; o Decreto nº 61.934/1967 a regulamenta. O CFA exerce função nacional normativa/orientadora; o CRA atua regionalmente no registro, orientação e fiscalização. Registro, dever ético e sanção dependem do sujeito, da atividade, da competência, da norma e do processo aplicável. | decreto substituir a lei; autonomia do CRA significar independência normativa; CNPJ substituir registro exigível; sigilo ser absoluto ou opcional; inventar penalidade ou prazo. | S1 — base legislativa do Dia 4; S2 — revisão ativa e atualização normativa do Dia 1 |
| **Dia 2 — Administração Pública** | [Revisão fixa do Dia 2](#s2-d2-revisao-fixa); [núcleo administrativo](#s2-d2-revisao-administracao); [LIMPE](#s2-d2-revisao-principios); [organização](#s2-d2-revisao-organizacao); [atos](#s2-d2-revisao-atos); [anulação, revogação e convalidação](#s2-d2-revisao-desfazimento); [LAI × LGPD](#s2-d2-revisao-lai-lgpd); [improbidade](#s2-d2-revisao-improbidade); [licitação](#s2-d2-revisao-licitacao); [responsabilidade estatal](#s2-d2-revisao-responsabilidade) | LIMPE aplica-se conjuntamente; autarquia integra a Administração Indireta e possui personalidade de direito público. Anulação combate ilegalidade, revogação trata mérito e convalidação alcança apenas vício sanável nos limites legais. LAI e LGPD devem ser compatibilizadas; contratação direta exige hipótese e instrução; responsabilidade objetiva do Estado não elimina dano e nexo. | eficiência afastar legalidade; órgão possuir personalidade própria; revogar ato ilegal; LAI eliminar proteção de dados; toda ilegalidade ser improbidade; dispensa ser igual a inexigibilidade; responsabilidade objetiva ser automática. | S1 — Administração Pública do Dia 6; S2 — síntese e aplicação do Dia 2 |
| **Dia 3 — Legislação CRA/CFA** | [Legislação do Dia 3](#s2-d3-revisao-legislacao) | Identifique sujeito, objeto, jurisdição e norma-base. Lei, Decreto, Regimento, regras de registro/fiscalização e Código de Ética têm funções distintas; as alterações normativas devem ser lidas junto ao ato consolidado aplicável. CFA uniformiza nacionalmente; CRA-PR executa competências em sua jurisdição. | trocar CFA por CRA; aplicar norma a sujeito fora de seu âmbito; tratar responsabilidade técnica como assinatura de fachada; obstruir fiscalização sob alegação de defesa; escolher sanção por intuição. | S1 — núcleo legal do Dia 4; S2 — registro, fiscalização, ética e aplicação institucional do Dia 3 |
| **Dia 4 — Administração Pública** | [Visão geral](#rf4-visao-geral); [LIMPE](#rf4-adm-01); [publicidade institucional](#rf4-adm-02); [órgão, entidade e autarquia](#rf4-adm-03); [elementos](#rf4-adm-04); [atributos](#rf4-adm-05); [anulação, revogação e convalidação](#rf4-adm-06); [LAI e LGPD](#rf4-adm-07); [improbidade](#rf4-adm-08); [licitação](#rf4-adm-09); [responsabilidade civil](#rf4-adm-10) | Aplique cada instituto pelos seus requisitos: elemento não é atributo; motivo não é motivação; publicidade não autoriza promoção pessoal nem exposição ilimitada; autarquia é criada por lei específica; anulação, revogação e convalidação possuem causas e efeitos diferentes; dispensa pressupõe hipótese legal e inexigibilidade, inviabilidade de competição. | promoção pessoal em publicidade verdadeira; vinculação como subordinação; presunção de legitimidade como certeza absoluta; autoexecutoriedade em todo ato; decadência quinquenal como regra universal; dolo presumido na improbidade; regresso objetivo contra o agente. | S1 — revisão ativa de Administração; S2 — fundamentos legais, exceções e casos aprofundados no Dia 4 |
| **Dia 4 — RLM** | [negação de conjunção/disjunção](#rf4-rlm-01); [condicional e quantificadores](#rf4-rlm-02); [inclusão-exclusão](#rf4-rlm-03); [porcentagem reversa](#rf4-rlm-04); [proporção](#rf4-rlm-05) | De Morgan: `¬(P ∧ Q) = ¬P ∨ ¬Q` e `¬(P ∨ Q) = ¬P ∧ ¬Q`; `¬(P → Q) = P ∧ ¬Q`. Em conjuntos, subtraia a interseção uma vez; em variações sucessivas, multiplique fatores; em proporção, determine antes se cada grandeza varia direta ou inversamente. | negar `todo` como `nenhum`; confundir contrapositiva com negação; contar interseção duas vezes; somar percentuais sucessivos; desfazer desconto acrescentando a mesma taxa; inverter razões automaticamente. | S1 — RLM do Dia 6; S2 — aplicação e aprofundamento do Dia 4 |
| **Dia 5 — Legislação CRA/CFA** | [Legislação do Dia 5](#revisão-fixa--legislação-cracfa-1) | Para Analista de Sistemas, separe Lei nº 4.769/1965, Decreto nº 61.934/1967, Regimento do CRA-PR e Código aprovado pela RN CFA nº 671/2025. Lei disciplina, Decreto regulamenta, Regimento organiza e Código fixa deveres no seu âmbito subjetivo. CFA exerce direção normativa nacional; CRA executa e fiscaliza regionalmente. | usar a RN nº 640/2024 revogada em vez da RN nº 671/2025; importar normas exclusivas de outro cargo; tratar Código como universal para todo profissional de TI; inverter competências CFA/CRA; confundir Regimento com Código. | S1 — legislação do Dia 4; S2 — alinhamento à Retificação I e aplicação ética em TI no Dia 5 |

As revisões de Português que alimentam o Bloco A podem ser conferidas em [Dia 1](#s2-d1-revisao-portugues), [Dia 2](#s2-d2-revisao-portugues), [Dia 3](#s2-d3-revisao-portugues), [Dia 4](#rf4-pt-01) e [Dia 5](#revisão-fixa--português-e-interpretação-1). No Dia 6, elas deixam de ser cinco listas separadas e passam a usar os IDs estáveis `D6-RF-PT-01` a `D6-RF-PT-10`.

<a id="s2-d6-rf-mx-01"></a>
#### D6-RF-MX-01 — Recuperação ativa de redes e métricas

Resumo decisivo:

- `largura de banda ≥ throughput ≥ goodput` é uma relação didática usual quando as grandezas são medidas no mesmo intervalo e ponto; sobrecarga e retransmissão separam vazão efetiva de carga útil;
- latência mede atraso; jitter mede variação desse atraso; perda mede dados que não chegaram;
- topologia física descreve disposição; topologia lógica descreve circulação e acesso;
- NIC conecta o host ao enlace e possui identidade de enlace, mas não identifica, por si, a pessoa usuária; repetidor regenera sinal; hub é repetidor multiporta que replica bits e não aprende MAC; switch aprende MAC e cria um domínio de colisão por porta; roteador encaminha entre redes e delimita broadcast; AP integra o acesso sem fio à LAN;
- LAN, MAN e WAN descrevem escopo/organização, não limites universais de quilômetros;
- fibra é resistente à interferência eletromagnética no enlace óptico, mas não torna toda implantação automaticamente mais barata ou rápida.

Exemplo: um enlace nominal de 1 Gbit/s entrega 780 Mbit/s de throughput e 720 Mbit/s de dados úteis. A largura nominal continua 1 Gbit/s; a diferença de 60 Mbit/s entre throughput e goodput pode refletir cabeçalhos e retransmissões. Não é correto chamar os 720 Mbit/s de latência.

<a id="s2-d6-rf-mx-02"></a>
#### D6-RF-MX-02 — Camadas, encapsulamento e evidência

Use a cadeia:

`aplicação/dados → transporte/segmento TCP ou datagrama UDP → Internet/rede/pacote IP → enlace/quadro → bits/sinais`.

No destino, ocorre desencapsulamento. A cada roteador, o pacote IP é examinado e normalmente inserido em **novo quadro para o próximo enlace**; MAC não é identidade fim a fim. A correspondência entre OSI e TCP/IP é funcional e aproximada, não uma igualdade perfeita de número e nomes de camadas.

Exemplo: o switch L2 usa MAC para encaminhar o quadro local; o roteador usa o destino IP para escolher o próximo salto; o sistema operacional usa protocolo e porta para entregar o conteúdo ao processo.

<a id="s2-d6-rf-mx-03"></a>
#### D6-RF-MX-03 — Algoritmo seguro de CIDR

No **modelo didático convencional de sub-redes IPv4**, aplique este roteiro a prefixos de `/1` a `/30`:

1. converta o prefixo em máscara;
2. localize o **primeiro octeto da máscara diferente de `255`**; ele é o octeto relevante e pode inclusive valer `0`, como em máscaras de fronteira `/8`, `/16` e `/24`;
3. calcule o tamanho do bloco: `256 − octeto relevante da máscara`;
4. encontre o múltiplo do bloco que contém o octeto do IP; para a rede, mantenha esse múltiplo e zere os octetos seguintes;
5. para o broadcast, use o próximo múltiplo menos um no octeto relevante e preencha os octetos seguintes com `255`;
6. os hosts usuais ficam estritamente entre rede e broadcast;
7. confira com `2^(32−prefixo)` endereços e, nesse modelo convencional, `2^(32−prefixo)−2` hosts.

Exemplo: `192.168.10.77/27` usa máscara `255.255.255.224`, bloco 32, rede `.64`, broadcast `.95` e hosts `.65` a `.94`.

Trate os limites separadamente: `/0`, escrito como `0.0.0.0/0`, é a **rota padrão** que corresponde a qualquer destino IPv4 e não deve ser resolvido como uma LAN comum; `/31` pode usar os dois endereços em enlace ponto a ponto; `/32` identifica um único endereço ou rota de host. Não aplique `−2` mecanicamente fora do modelo convencional de `/1` a `/30`.

<a id="s2-d6-rf-mx-04"></a>
#### D6-RF-MX-04 — IPv6, próximo salto e protocolos de controle

- Se o destino IPv4/IPv6 está no mesmo prefixo local, o host procura entrega direta; se está fora, envia ao gateway configurado.
- ARP resolve, no cenário estudado, o **IPv4 do próximo salto** em endereço de enlace. Para destino remoto, procura-se o MAC do gateway, não o MAC do host final.
- ICMP comunica erros e informações de controle; `ping` usa Echo Request/Reply, mas ICMP também inclui mensagens como Destination Unreachable e Time Exceeded.
- IPv6 usa 128 bits, representação hexadecimal e **não possui broadcast**. Multicast e Neighbor Discovery, baseado em ICMPv6, cumprem funções específicas.
- Link-local possui escopo de enlace; não equivale a endereço global. `::1` é loopback; `::` é endereço não especificado; `2001:db8::/32` é documentação.

Exemplo: para alcançar servidor IPv6 remoto, a estação usa Neighbor Discovery para descobrir o endereço de enlace do roteador local. Isso não cria “ARPv6” como protocolo separado nem busca o MAC do servidor remoto através de todos os roteadores.

<a id="s2-d6-rf-mx-05"></a>
#### D6-RF-MX-05 — Protocolos: transporte, Web, nomes e configuração

Regra de integração: DHCPv4 configura o cliente no fluxo DORA; DNS resolve/publica dados; TCP ou UDP transporta; TLS pode proteger o canal; HTTP expressa a requisição/resposta. Falha em uma etapa não prova falha nas demais.

- **TCP:** conexão e fluxo ordenado/confiável; ACK não confirma sucesso de negócio nem preserva fronteiras de mensagem.
- **UDP:** datagramas sem confirmação/retransmissão/ordenação nativas; a aplicação pode acrescentar confiabilidade.
- **HTTP:** requisição/resposta; `stateless` não impede cookies ou sessão na aplicação. HTTP/3 usa normalmente `443/UDP` por meio do QUIC.
- **HTTPS:** HTTP sobre TLS; protege o canal validado, não garante honestidade do conteúdo nem endpoint limpo. HTTP/1.1 e HTTP/2 usam tipicamente `443/TCP`; HTTP/3 usa normalmente `443/UDP` via QUIC.
- **DNS:** sistema hierárquico de registros; A, AAAA, CNAME, MX, NS, SOA, PTR e TXT têm funções diferentes; DNS clássico usa 53/UDP e 53/TCP.
- **DHCPv4:** entrega IPv4, máscara/prefixo, gateway, DNS e lease; DORA = Discover, Offer, Request, ACK; usa 67/UDP no servidor e 68/UDP no cliente. Essas portas e a sequência DORA, neste resumo, referem-se especificamente ao DHCPv4.

<a id="s2-d6-rf-mx-06"></a>
#### D6-RF-MX-06 — Inventário obrigatório de protocolos e serviços

| Protocolo/serviço | Função e transporte/porta padrão mais cobrada | Diferença ou pegadinha decisiva | Seção real |
|---|---|---|---|
| TCP | fluxo confiável e ordenado; portas dependem da aplicação | não confirma regra de negócio nem preserva mensagens | [TCP × UDP](#s2-d3-tcp-udp) |
| UDP | datagramas; portas dependem da aplicação | ausência de garantia nativa não proíbe recuperação na aplicação | [TCP × UDP](#s2-d3-tcp-udp) |
| HTTP | Web por requisição/resposta; 80/TCP no uso clássico | HTTP/3 usa normalmente `443/UDP` via QUIC; `stateless` não proíbe sessão de aplicação | [HTTP e HTTPS](#s2-d3-http-https) |
| HTTPS | HTTP sobre TLS; `443/TCP` em HTTP/1.1 e HTTP/2; normalmente `443/UDP` via QUIC no HTTP/3 | certificado/canal válido não prova conteúdo honesto | [HTTP e HTTPS](#s2-d3-http-https) |
| DNS | nomes e registros; 53/UDP e 53/TCP no DNS clássico | não é só nome→IP nem usa somente UDP | [DNS](#s2-d3-dns) |
| DHCPv4 | configuração IPv4 dinâmica; servidor 67/UDP, cliente 68/UDP; sequência DORA | entrega DNS como opção, mas não resolve nomes; não transportar essas portas mecanicamente para DHCPv6 | [DHCP](#s2-d3-dhcp) |
| SMTP | submissão/transferência; 25, 587 e 465/TCP conforme papel/TLS | não é protocolo de leitura da caixa | [Correio eletrônico](#s2-d3-email) |
| POP3 | acesso simples à caixa; 110/995 TCP | não apaga sempre do servidor | [Correio eletrônico](#s2-d3-email) |
| IMAP | sincronização de caixa/pastas; 143/993 TCP | acessa caixa; não envia entre servidores | [Correio eletrônico](#s2-d3-email) |
| FTP | controle em 21/TCP e dados separados; 20 tradicional no modo ativo | modo passivo negocia porta de dados; FTP clássico não cifra | [Transferência e acesso remoto](#s2-d3-transferencia-remota) |
| FTPS | FTP protegido por TLS; explícito inicia em 21; implícito usa 990 no controle | controle protegido não protege dados sem configuração como `PROT P`; continua sendo FTP | [Transferência e acesso remoto](#s2-d3-transferencia-remota) |
| SFTP | transferência como subsistema SSH; 22/TCP | não é FTP sobre TLS | [Transferência e acesso remoto](#s2-d3-transferencia-remota) |
| SSH | administração remota protegida; 22/TCP | segurança depende de validar host, proteger chaves e restringir acesso | [Transferência e acesso remoto](#s2-d3-transferencia-remota) |
| Telnet | terminal remoto; 23/TCP | não oferece proteção criptográfica adequada a credenciais | [Transferência e acesso remoto](#s2-d3-transferencia-remota) |
| SNMP | gerência: 161/UDP consultas; 162/UDP traps/informs | v1/v2c não equivalem a v3 com autenticação e privacidade; configuração ainda importa | [SNMP](#s2-d3-snmp) |
| LDAP | diretório hierárquico; 389/TCP e 636/TCP com TLS implícito | não é SQL nem, isoladamente, toda a autenticação/autorização | [LDAP](#s2-d3-ldap) |
| proxy direto | representa clientes | não garante anonimato | [Proxy](#s2-d3-proxy) |
| proxy reverso | representa servidores; pode terminar TLS/balancear | não é gateway padrão nem sinônimo de NAT | [Proxy](#s2-d3-proxy) |
| NAT básico | traduz endereços | não traduz porta quando a questão opõe NAT básico a PAT; não é firewall | [NAT e PAT](#s2-d3-nat-pat) |
| PAT/NAPT | traduz endereços e portas | permite multiplexar fluxos em um IP público; não cifra | [NAT e PAT](#s2-d3-nat-pat) |
| NTP | sincroniza relógios; 123/UDP | não define fuso horário nem torna relógio perfeito | [NTP](#s2-d3-ntp) |

Porta conhecida é **padrão de serviço**, não prova de protocolo efetivo, legitimidade, autenticação ou criptografia.

<a id="s2-d6-rf-mx-07"></a>
#### D6-RF-MX-07 — Segurança: objetivo, identidade, risco e ataque

Gestão de risco começa pelo contexto e pelos ativos, identifica ameaças e vulnerabilidades, analisa probabilidade e impacto, seleciona tratamento e monitora o risco residual. Evitar, mitigar, transferir/compartilhar ou aceitar um risco são decisões justificadas; instalar um produto isolado não produz “risco zero”.

Classifique primeiro o **efeito**, depois o mecanismo:

- confidencialidade: divulgação indevida;
- integridade: alteração ou destruição indevida;
- disponibilidade: acesso oportuno ao serviço/dado;
- autenticação: quem é; autorização: o que pode fazer; auditoria/accounting: o que fez; não repúdio: evidência contra negação falsa;
- ativo é o que tem valor; ameaça é causa potencial; vulnerabilidade é fraqueza; risco combina possibilidade/impacto; evento é ocorrência observável; incidente compromete ou ameaça concretamente operações/ativos.

Ataques e diferenças:

- vírus depende de hospedeiro/execução; worm se autopropaga; trojan se disfarça; ransomware extorque por cifração, bloqueio e/ou exfiltração;
- phishing é técnica de engenharia social; engenharia social é a categoria ampla;
- spoofing falsifica identidade/origem; sniffing captura; on-path se posiciona para interceptar e possivelmente alterar;
- força bruta testa combinações; credential stuffing reutiliza credenciais vazadas;
- DoS degrada/impede serviço; DDoS distribui a origem. Firewall local não recupera enlace já saturado.

<a id="s2-d6-rf-mx-08"></a>
#### D6-RF-MX-08 — Controles, criptografia e Wi-Fi

| Conceitos próximos | Diferença decisiva |
|---|---|
| firewall × IDS × IPS | controla fluxos × detecta/alerta × detecta e tenta bloquear em linha |
| DMZ × rede interna | segmento de exposição controlada × ambiente restrito; DMZ não é “confiável” |
| VLAN × firewall interno | separação lógica de L2 × autorização de fluxos roteados |
| VPN × proteção do endpoint | protege túnel/canal × não remove malware nem corrige o dispositivo |
| cifra simétrica × assimétrica | mesma chave secreta e eficiência × par pública/privada e maior custo |
| hash × criptografia | resumo unidirecional × transformação reversível com chave |
| HMAC × assinatura digital | segredo compartilhado × chave privada verificável com a pública |
| assinatura × certificado | prova sobre dado × vínculo entre identidade/nome e chave pública |
| TLS × HTTPS | protocolo de canal seguro × HTTP sobre esse canal |
| WPA2-Personal × WPA3-Personal | PSK × SAE; ambos dependem de configuração e credencial adequadas |

Exemplo integrado: TLS pode usar mecanismos assimétricos para autenticação/estabelecimento e chaves simétricas de sessão para o volume de dados. Não se “cifra todo o tráfego com a chave privada”. Hash isolado ao lado de um arquivo não prova integridade se o invasor puder substituir ambos. Em modo de transição WPA2/WPA3, um cliente legado pode negociar WPA2; avalie o modo efetivo.

<a id="s2-d6-rf-mx-09"></a>
#### D6-RF-MX-09 — Resposta, continuidade e objetivos de recuperação

Mapa de decisão:

1. **preparar:** inventário, contatos, logs, playbooks, backups e exercícios;
2. **detectar/analisar:** validar sinais, escopo, impacto e evidências;
3. **conter:** limitar propagação e dano sem destruir evidência necessária;
4. **erradicar:** remover persistência, vulnerabilidade explorada e artefatos maliciosos;
5. **recuperar:** restaurar de fonte confiável, validar, monitorar e retornar gradualmente;
6. **aprender/comunicar:** registrar decisões, cumprir comunicações e corrigir causas.

Diferenças:

- **RPO:** janela máxima tolerável de perda de dados, expressa pelo ponto mais antigo aceitável de recuperação. Se o incidente ocorre às 14h e o RPO é 30 minutos, o ponto recuperado deve ser, no máximo, de 13h30; recuperar apenas até 13h excederia a perda tolerada.
- **RTO:** tempo-alvo para restabelecer o serviço após a interrupção considerada.
- **Backup:** cópia recuperável de estado/histórico.
- **Redundância/alta disponibilidade:** componentes/arquitetura para manter ou retomar operação rapidamente.

Exemplo: cópia a cada 24 horas não atende, em regra, RPO de 15 minutos. RAID pode manter serviço diante da falha de um disco, mas replica corrupção e não substitui backup versionado, protegido e testado.

<a id="s2-d6-rf-mx-10"></a>
#### D6-RF-MX-10 — Sistemas operacionais: progresso, E/S e persistência

**Origem:** **[S1 — revisão ativa]** processos, threads, escalonamento, sistemas de arquivos, dispositivos, concorrência, sincronização, deadlock e Windows/Linux estudados no Dia 2 da Semana 1. **[S2 — aprofundamento]** intercalações, primitivas, métricas, estratégias de deadlock, DMA, journaling, permissões e leitura de comandos desenvolvidos no Dia 5.

| Núcleo | Regra-chave | Erro recorrente | Seção real do Dia 5 |
|---|---|---|---|
| concorrência/paralelismo | progresso sobreposto não exige simultaneidade; paralelismo exige execução simultânea | exigir dois núcleos para concorrência | `### 1. Concorrência e paralelismo` |
| processo/thread | processo isola recursos; threads compartilham recursos do processo e mantêm contexto/pilha próprios | dizer que threads têm heap totalmente isolado | `### 2. Programa, processo e thread` |
| corrida/atomicidade | resultado depende de intercalação; expressão de alto nível pode conter ler-calcular-gravar | chamar toda concorrência de corrida | `### 3. Seção crítica, condição de corrida e atomicidade` |
| mutex/semáforo/monitor | mutex expressa propriedade exclusiva; semáforo contador representa N unidades; condição espera predicado sob lock | tratar todas as primitivas como sinônimas | `### 4. Mutex, semáforos, monitores e variáveis de condição` |
| IPC | pipe, fila, memória compartilhada e socket têm isolamento, formato e sincronização distintos | achar que memória compartilhada é automaticamente segura | `### 5. Comunicação entre processos — IPC` |
| deadlock | impasse conjunto sem progresso porque os participantes aguardam recursos ou eventos dependentes entre si; no caso clássico, Coffman: exclusão mútua + posse e espera + não preempção + espera circular | uma condição isolada provar deadlock; estado inseguro já ser deadlock | [Deadlock](#s2-d5-deadlock) |
| starvation/livelock | starvation adia um participante enquanto outros avançam; livelock tem atividade sem progresso útil | exigir ciclo de recursos em ambos | `### 7. Starvation, livelock e inversão de prioridade` |
| escalonamento | retorno = conclusão−chegada; resposta = primeiro atendimento−chegada; espera é tempo na fila de prontos | ignorar preempção, chegadas ou quantum | `### 8. Escalonamento de CPU` |
| polling/interrupção/DMA | polling consulta; interrupção sinaliza evento; DMA move bloco com menor intervenção por unidade e pode interromper ao final | DMA eliminar toda participação da CPU | `### 9. Dispositivos, drivers, interrupções, polling e DMA` |
| sistema de arquivos/journaling | journaling registra metadados e/ou dados conforme o FS para recuperar consistência após falha | tratar journal como cópia histórica | `### 10. Sistemas de arquivos e journaling` |
| permissões | Linux lê `rwx` em tríades usuário/grupo/outros; Windows usa DACL/ACEs, negações e herança | somar bits entre tríades ou igualar DACL a modo Unix | `### 11. Permissões em Linux e Windows` |
| comandos de observação e ação | `ps`, `top`, `tasklist` e `Get-Process` observam processos; `kill`, `taskkill` e `Stop-Process` alteram estado; valide dependências antes de encerrar | deduzir que listar encerra; tratar `KILL` como sempre preferível a `TERM`; decorar opção sem entender finalidade | [Windows e Linux — comandos pertinentes](#s2-d5-comandos) |

Exemplos de recuperação:

- `640` = proprietário `rw-`, grupo `r--`, outros `---`;
- em Round Robin, quantum muito grande aproxima o comportamento de FCFS; quantum pequeno aumenta preempções e custo de trocas;
- impor ordem global de aquisição de locks quebra a espera circular quando todos os caminhos obedecem à ordem;
- journaling pode restaurar consistência estrutural após queda, mas não recupera, por si, versão antiga apagada pelo usuário.
- `ps`, `top`, `tasklist` e `Get-Process` fornecem observação; já `kill`, `taskkill` e `Stop-Process` solicitam ou forçam alteração do estado do processo, conforme comando e sinal.

<a id="s2-d6-rf-caderno-erros"></a>
#### Protocolo do caderno de erros para as 10 questões mistas

Para cada erro, registre:

| Campo | Preenchimento obrigatório |
|---|---|
| ID | um entre `D6-RF-MX-01` e `D6-RF-MX-10` |
| disciplina/núcleo | redes, endereçamento, protocolos, segurança ou sistemas operacionais |
| seção real | título e âncora do mapa localizador |
| tipo do erro | conceitual, cálculo/procedimento, leitura, memória ou integração |
| regra correta | uma frase verificável, sem “conforme visto na teoria” |
| contraste | conceito confundido e diferença decisiva |
| evidência/exemplo | cálculo, fluxo, porta, cenário ou comando que confirma a regra |
| nova tentativa | 24 horas e 7 dias, sem consultar a resposta anterior |

Exemplo de registro adequado:

> **D6-RF-MX-04 — erro conceitual.** Marquei que ARP encontra o MAC do servidor remoto. Em [ARP](#s2-d2-arp), a regra é: para destino fora da sub-rede, o host usa ARP para obter o endereço de enlace do **gateway local**; os roteadores seguintes constroem novos quadros em seus próprios enlaces.

Registro inadequado: “Errei ARP; revisar depois.” Ele não identifica a regra, o contraste nem a seção.

<a id="s2-d6-rf-tabela-final"></a>
#### Tabela de revisão rápida — revisão mista

| ID | Pergunta de recuperação | Resposta mínima esperada |
|---|---|---|
| D6-RF-MX-01 | capacidade, vazão útil, atraso e variação são o quê? | largura de banda, goodput, latência e jitter, respectivamente |
| D6-RF-MX-02 | o que muda em cada salto roteado? | o quadro/endereço de enlace; o pacote IP segue a lógica fim a fim, salvo funções intermediárias específicas |
| D6-RF-MX-03 | como localizar rede e broadcast? | no modelo convencional `/1`–`/30`: máscara, primeiro octeto diferente de 255 — inclusive 0 —, bloco, múltiplo inferior e próximo bloco menos um; `/0` é rota padrão e `/31`–`/32` exigem tratamento próprio |
| D6-RF-MX-04 | ARP, ICMP e ND fazem a mesma coisa? | não; ARP mapeia IPv4–enlace, ICMP controla/diagnostica, ND atende funções de vizinhança no IPv6 |
| D6-RF-MX-05 | DNS, DHCPv4 e HTTPS resolvem quais problemas? | nomes/dados; configuração IPv4 por DORA em 67/68 UDP; HTTP protegido por TLS, inclusive HTTP/3 normalmente em 443/UDP via QUIC |
| D6-RF-MX-06 | SMTP, IMAP, SFTP, SNMP, LDAP, PAT e NTP? | envio; acesso à caixa; arquivos sobre SSH; gerência; diretório; endereço+porta; tempo |
| D6-RF-MX-07 | spoofing, sniffing e on-path? | falsificação; captura; interceptação com possibilidade de alteração |
| D6-RF-MX-08 | hash, HMAC e assinatura? | resumo; autenticação com segredo; prova verificável com chave pública |
| D6-RF-MX-09 | RPO e RTO? | janela máxima tolerável de perda/ponto mais antigo aceitável; prazo de restabelecimento |
| D6-RF-MX-10 | deadlock, starvation e livelock? | impasse conjunto sem progresso por dependência; adiamento individual; atividade sem progresso útil |

Pegadinhas finais do bloco:

1. Um acerto técnico não compensa leitura errada de `incorreta`, `exceto` ou `não se pode concluir`.
2. Porta, resposta a `ping`, certificado ou autenticação isolada não provam saúde, legitimidade ou autorização do serviço.
3. Prefixo maior representa rede menor dentro do mesmo espaço de endereços.
4. IPv6 não possui broadcast; Neighbor Discovery não deve ser reduzido a “ARP com outro nome”.
5. DNS pode usar UDP e TCP; SFTP não é FTP protegido por TLS.
6. NAT/PAT não é firewall, VPN nem criptografia.
7. IDS não bloqueia necessariamente; IPS em linha pode bloquear e também produzir falso positivo.
8. Hash não oferece confidencialidade; certificado não prova honestidade; VPN não corrige endpoint comprometido.
9. Backup, redundância, journaling, RPO e RTO respondem a perguntas diferentes.
10. Concorrência não exige paralelismo; corrida, deadlock, starvation e livelock não são sinônimos.

## Tabela de revisão rápida do Dia 6

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| VLAN | Domínio lógico de camada 2 | Achar que cifra tráfego | Visitantes separados |
| Roteador | Encaminha entre redes | Confundir com switch | Gateway inter-VLAN |
| Encapsulamento | Cada camada adiciona controle | Dizer que MAC é fim a fim | Quadro muda por salto |
| /27 | 27 bits de rede | Responder 32 hosts úteis | 30 hosts usuais |
| ARP | IPv4 para endereço de enlace | Dizer que resolve DNS | Gateway para MAC |
| ICMP | Controle e diagnóstico IP | Reduzir a ping | Time Exceeded |
| DNS | Sistema de nomes e registros | Confundir com DHCP | A/AAAA/MX |
| DHCPv4 | Configuração IPv4 dinâmica | Dizer que roteia ou aplicar DORA ao DHCPv6 | DORA em 67/68 UDP |
| TCP | Fluxo confiável e ordenado | Preservar mensagens | HTTPS clássico |
| UDP | Datagramas sem garantia do transporte | Dizer que aplicação não pode recuperar | DNS usual |
| NAT/PAT | Tradução de endereço/porta | Chamar de firewall | Muitos hosts, um IP |
| Firewall | Política de fluxo | Achar que remove malware | Permitir 443 à DMZ |
| IDS/IPS | Detecta / detecta e bloqueia | Tratar como patch | Assinatura de ataque |
| DMZ | Segmento exposto controlado | Rede sem controles | Proxy reverso |
| TLS | Proteção do canal | Garantir conteúdo benigno | HTTPS |
| MFA | Mais de um fator | Duas senhas serem dois fatores | Senha + token |
| Backup | Cópia para recuperação | Confundir com RAID | Restauração versionada |
| RPO | Janela máxima tolerável de perda; ponto mais antigo aceitável | Confundir com duração ou RTO | Até 15 min de dados |
| RTO | Tempo-alvo de retorno | Confundir com retenção | Serviço em 2 h |
| Deadlock | Impasse conjunto sem progresso por dependência | Chamar timeout de solução completa | Locks inversos |

## Pegadinhas do Dia 6

1. Switch não elimina broadcast sem VLAN ou outra separação lógica.
2. Roteador encaminha pacote, mas o quadro é reconstruído por enlace.
3. Gateway padrão é usado para destino remoto, não para todo pacote local.
4. Prefixo maior significa rede menor e menos hosts, no mesmo espaço de endereços.
5. IPv6 não usa broadcast.
6. ARP não é resolução de nome e Neighbor Discovery não é ARP puro.
7. DNS pode usar UDP e TCP.
8. Porta conhecida não autentica aplicação nem torna tráfego seguro.
9. HTTPS é HTTP protegido por TLS; não significa site honesto.
10. SFTP não é “FTP com S” e usa SSH.
11. TCP confirma bytes do fluxo, não o sucesso da regra de negócio.
12. UDP não estabelece conexão no transporte, mas aplicações podem manter estado.
13. NAT não implementa mínimo privilégio por definição.
14. VLAN segmenta domínio; firewall autoriza fluxos entre segmentos.
15. IDS fora de linha não bloqueia automaticamente.
16. Usuário autenticado ainda precisa de autorização.
17. Criptografia simétrica e assimétrica não diferem por uma ser “segura” e outra não.
18. Hash não substitui criptografia e certificado não contém chave privada do titular.
19. VPN protege o canal, não um dispositivo já comprometido.
20. Backup concluído sem restauração testada não comprova recuperabilidade.
21. RAID replica exclusão e corrupção; não é histórico de backup.
22. TCP aberto com aplicação travada é possível.
23. Retry de operação não idempotente pode duplicar efeito.
24. Isolar incidente não significa destruir evidência.
25. No edital vigente, a RN CFA nº 671/2025 substitui a nº 640/2024.

## Prática guiada

### Atividade 1 — narrar o pacote

Escolha um acesso HTTPS de uma estação a um portal remoto. Escreva, em ordem: DNS, decisão local/remota, ARP do próximo salto, quadro, pacote IP, conexão TCP, TLS e HTTP. Ao lado, indique equipamento e evidência observável. Compare com o roteiro da seção 1.

### Atividade 2 — plano de sub-redes

Parta de 10.50.0.0/24 e reserve, sem sobreposição:

- /25 para usuários;
- /27 para servidores;
- /28 para administração;
- /28 para backup.

Uma solução válida:

- usuários: 10.50.0.0/25, hosts 1–126, broadcast 127;
- servidores: 10.50.0.128/27, hosts 129–158, broadcast 159;
- administração: 10.50.0.160/28, hosts 161–174, broadcast 175;
- backup: 10.50.0.176/28, hosts 177–190, broadcast 191.

O espaço 192–255 permanece para expansão, desde que dividido corretamente.

### Atividade 3 — matriz de firewall

Monte tabela origem, destino, serviço, justificativa, responsável e validade. Comece negando tudo e acrescente somente os fluxos do estudo de caso. Evite regra baseada apenas em “é rede interna”.

### Atividade 4 — separar dois incidentes

Crie duas linhas do tempo: segurança e deadlock. Associe evidências exclusivas e compartilhadas. O objetivo é impedir que a equipe atribua todo timeout ao ransomware ou todo arquivo alterado ao deadlock.

### Atividade 5 — restauração

Escolha um RPO de 15 minutos e RTO de 2 horas. Descreva frequência de cópias, dependências, ordem de recuperação, validação de integridade e teste de negócio. Registre o que precisa estar fora do domínio administrativo comprometido.

### Atividade 6 — recuperação do caderno de erros

Selecione os cinco erros de maior prioridade. Sem consultar, explique cada um em 60 segundos. Consulte somente depois, marque lacunas e repita em formulação menor. Agende D1, D7 e D30.

## Checklist do Dia 6

- [ ] Narrei uma requisição completa de DNS a aplicação.
- [ ] Diferenciei topologia física e lógica.
- [ ] Diferenciei meios guiados e não guiados e expliquei o papel da NIC.
- [ ] Expliquei domínios de colisão e broadcast.
- [ ] Mapeei OSI e TCP/IP sem correspondência forçada.
- [ ] Associei PDU, endereço e equipamento à camada.
- [ ] Calculei rede, broadcast, hosts e prefixo CIDR.
- [ ] Reconheci faixas privadas, loopback e link-local.
- [ ] Diferenciei ARP, ICMP, DNS, DHCP e gateway.
- [ ] Revisei portas conhecidas com o transporte correto.
- [ ] Diferenciei TCP e UDP sem absolutos indevidos.
- [ ] Expliquei NAT e PAT sem chamá-los de firewall.
- [ ] Diferenciei autenticação, autorização, auditoria e não repúdio.
- [ ] Classifiquei ameaça, vulnerabilidade, risco e incidente.
- [ ] Comparei firewall, IDS, IPS, DMZ, VPN e segmentação.
- [ ] Diferenciei hash, criptografia, assinatura, certificado e TLS.
- [ ] Comparei WPA2/WPA3 Personal e Enterprise, PSK/802.1X, CCMP, SAE, PMF e modo de transição.
- [ ] Diferenciei completo, incremental e diferencial.
- [ ] Expliquei RPO, RTO, redundância, journaling e backup.
- [ ] Relacionei falhas de processo/SO a sintomas de rede.
- [ ] Separei saturação do listen backlog de esgotamento de descritores/handles.
- [ ] Revisei escalonamento, mutex, semáforo, monitor/condição, spinlock, IPC, driver, polling, interrupção e DMA.
- [ ] Separei permissão de fluxo no firewall de autenticação e autorização no SGBD.
- [ ] Resolvi o deadlock do estudo de caso com ordem, detecção e rollback.
- [ ] Criei resposta ao incidente com contenção, erradicação e recuperação.
- [ ] Revisei os cinco conceitos mais errados do caderno.
- [ ] Corrigi pontuação, conectores e extrapolações no texto técnico.

## Orientações para o caderno de erros

Feche a semana com uma página de síntese, não com transcrição da apostila:

~~~text
Erro mais frequente:
Regra correta:
Par que eu confundo:
Evidência que separa os dois:
Exemplo mínimo:
Data D1:
Data D7:
Data D30:
~~~

Crie ainda um “mapa de escalada”: camada física → enlace → IP → transporte → aplicação → processo → armazenamento → segurança. Posicione cada erro no mapa. Isso permite revisar pelo fluxo, não pela ordem em que o material foi escrito.

## Fontes oficiais do Dia 6

### Edital

- Edital local anterior à Retificação I, preservado no projeto: ../edital/edital_cra_pr_2026_analista_sistemas_retificacao_1.pdf
- Página oficial do concurso: https://www.institutoconsulplan.org.br/Concurso/crapr2026
- Edital consolidado conforme Retificação I: https://cdnsite.institutoconsulplan.org.br/concursos/1330/b2c07c473c9749fea22728da3c964c06.pdf
- Retificação I: https://cdnsite.institutoconsulplan.org.br/concursos/1330/f8d7af1d6393470e8b6b46a4834f8e21.pdf

### Arquitetura e protocolos de Internet

- RFC 1122 — requisitos das camadas de comunicação: https://www.rfc-editor.org/info/rfc1122
- RFC 1918 — endereços IPv4 privados: https://www.rfc-editor.org/info/rfc1918
- RFC 3927 — IPv4 link-local: https://www.rfc-editor.org/info/rfc3927
- RFC 4632 — CIDR: https://www.rfc-editor.org/info/rfc4632
- RFC 8200 — IPv6: https://www.rfc-editor.org/info/rfc8200
- RFC 826 — ARP: https://www.rfc-editor.org/info/rfc826
- RFC 792 — ICMPv4: https://www.rfc-editor.org/info/rfc792
- RFC 4443 — ICMPv6: https://www.rfc-editor.org/info/rfc4443
- RFC 9293 — TCP: https://www.rfc-editor.org/info/rfc9293
- RFC 768 — UDP: https://www.rfc-editor.org/info/rfc768
- RFC 1034 e RFC 1035 — DNS: https://www.rfc-editor.org/info/rfc1034 e https://www.rfc-editor.org/info/rfc1035
- RFC 2131 — DHCP: https://www.rfc-editor.org/info/rfc2131
- RFC 9110 — semântica HTTP: https://www.rfc-editor.org/info/rfc9110
- RFC 5321 — SMTP: https://www.rfc-editor.org/info/rfc5321
- RFC 9051 — IMAP4rev2: https://www.rfc-editor.org/info/rfc9051
- RFC 1939 — POP3: https://www.rfc-editor.org/info/rfc1939
- RFC 4251 — arquitetura SSH: https://www.rfc-editor.org/info/rfc4251
- RFC 8446 — TLS 1.3: https://www.rfc-editor.org/info/rfc8446
- RFC 3411 — arquitetura SNMP: https://www.rfc-editor.org/info/rfc3411
- RFC 4511 — LDAP: https://www.rfc-editor.org/info/rfc4511
- RFC 5905 — NTPv4: https://www.rfc-editor.org/info/rfc5905
- RFC 3022 — NAT tradicional: https://www.rfc-editor.org/info/rfc3022
- IANA — registro oficial de serviços e portas: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
- W3C — catálogo oficial de padrões Web: https://www.w3.org/TR/

### Segurança e continuidade

- NIST SP 800-41 Rev. 1 — firewalls e políticas: https://csrc.nist.gov/pubs/sp/800/41/r1/final
- NIST SP 800-61 Rev. 3 — resposta a incidentes: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- NIST CSF 2.0 — Govern, Identify, Protect, Detect, Respond e Recover: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
- NIST SP 800-153 — segurança de WLAN: https://csrc.nist.gov/pubs/sp/800/153/final
- NIST SP 800-34 Rev. 1 — contingência e recuperação: https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final
- NIST SP 800-207 — arquitetura zero trust: https://csrc.nist.gov/pubs/sp/800/207/final
- NIST SP 1800-35 — implementações de zero trust: https://csrc.nist.gov/pubs/sp/1800/35/final
- NIST IR 7298 Rev. 3 — glossário de segurança: https://csrc.nist.gov/pubs/ir/7298/r3/final
- Wi-Fi Alliance — visão oficial de segurança Wi-Fi: https://www.wi-fi.org/security
- Wi-Fi Alliance — lançamento e propriedades do WPA3: https://www.wi-fi.org/news-events/newsroom/wi-fi-alliance-introduces-wi-fi-certified-wpa3-security
- PostgreSQL — autenticação de clientes: https://www.postgresql.org/docs/current/client-authentication.html
- PostgreSQL — privilégios sobre objetos do SGBD: https://www.postgresql.org/docs/current/ddl-priv.html

### Sistemas operacionais usados na integração

- Microsoft — processos e threads: https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads
- Microsoft — prioridades e preempção: https://learn.microsoft.com/en-us/windows/win32/procthread/scheduling-priorities
- Microsoft — objetos de sincronização: https://learn.microsoft.com/en-us/windows/win32/sync/about-synchronization
- Microsoft — icacls e DACLs: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls
- Microsoft PowerShell — Get-Acl: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-acl
- Linux man-pages — políticas de escalonamento: https://man7.org/linux/man-pages/man7/sched.7.html
- Linux man-pages — listen e fila de conexões pendentes: https://man7.org/linux/man-pages/man2/listen.2.html
- Linux man-pages — limites de descritores: https://man7.org/linux/man-pages/man2/getrlimit.2.html
- Linux man-pages — visão geral de semáforos POSIX: https://man7.org/linux/man-pages/man7/sem_overview.7.html
- Linux man-pages — visão geral de memória compartilhada POSIX: https://man7.org/linux/man-pages/man7/shm_overview.7.html
- Linux man-pages — pipes e FIFOs: https://man7.org/linux/man-pages/man7/pipe.7.html
- Linux Kernel — interfaces e drivers de rede: https://www.kernel.org/doc/html/latest/networking/netdevices.html
- Linux Kernel — VFS: https://www.kernel.org/doc/html/latest/filesystems/vfs.html
- Linux Kernel — journaling ext4/JBD2: https://www.kernel.org/doc/html/latest/filesystems/ext4/journal.html

---

# Revisão Final da Semana 2

## Objetivo da revisão

Conectar infraestrutura, protocolos, segurança e sistema operacional em um único fluxo de diagnóstico. Ao final da semana, o estudante deve conseguir localizar um problema por camada, justificar a escolha de um controle e distinguir causa, sintoma e consequência.

## Roteiro de revisão de 60 minutos, se houver tempo extra

| Tempo | Atividade |
|---:|---|
| 10min | Desenhe uma LAN com VLANs, switch, roteador, firewall, DMZ e AP |
| 10min | Refaça um cálculo `/26` e converta duas máscaras em prefixos |
| 10min | Associe 12 serviços às portas e ao transporte predominante |
| 10min | Relacione cinco ataques aos controles que reduzem seu risco |
| 10min | Explique corrida, mutex, semáforo, starvation e deadlock |
| 10min | Releia os cinco erros mais frequentes e agende D1, D7 e D30 |

## Entrega final da semana

Ao concluir a Semana 2, produza:

- mapa de topologias, equipamentos e domínios;
- quadro OSI x TCP/IP e folha de cálculo CIDR;
- mapa de serviços, portas e transportes;
- matriz ameaça, vulnerabilidade, risco e controle;
- quadro de concorrência, sincronização, deadlock e escalonamento;
- solução comentada do estudo de caso;
- lista dos dez erros mais frequentes, com causa e regra corretiva.

## Cobertura efetiva e pontos pendentes

Foram aprofundados redes, topologias, componentes, meios, LAN/WAN, OSI, TCP/IP, endereçamento, protocolos, equipamentos, redes sem fio, VPN, ataques, firewall, DMZ, segurança, concorrência, sincronização, deadlock, dispositivos, sistemas de arquivos e aspectos práticos de Windows/Linux.

Padrões W3C e gerência de rede foram contextualizados, mas não esgotados. Permanecem pendentes para aprofundamento posterior, especialmente arquitetura de gerenciamento, MIB, operações SNMP em maior detalhe, métricas, observabilidade, HTML/CSS e padrões de acessibilidade e interoperabilidade do W3C.
