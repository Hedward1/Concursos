# Apostila de Questões - Semana 2 v1.0

## CRA-PR 2026 - Analista de Sistemas

Arquivo de questões para acompanhar a `semana_02_estudo.md`.

**Critério de autoria:** todas as 300 questões principais e 120 questões extras desta apostila são autorais e foram elaboradas no estilo de cobrança do Instituto Consulplan. Provas públicas da banca foram consultadas apenas como referência de estilo. Nenhuma questão real foi reproduzida sem fonte confirmada.

**Formato:** todas as questões têm quatro alternativas, de A) a D), e exatamente uma resposta correta, em conformidade com o edital do CRA-PR 2026.

**Total planejado:** 420 questões, sendo 300 principais (50 por dia) e 120 extras de revisão fixa (20 por dia).

**Nível:** combinação de itens fáceis para fixação, predominância de dificuldade média e parcela difícil de integração. Os formatos incluem conceito direto, cenário prático, assertivas, alternativa correta/incorreta, comparação, cálculo CIDR, análise de incidente e interpretação de comandos.

**Correção comentada:** cada comentário identifica a resposta, analisa as quatro alternativas, explicita conceito, pegadinha e estratégia de resolução e remete à subseção correspondente da apostila teórica.

---

## Fontes oficiais e referências de estilo

- Edital oficial consolidado CRA-PR 2026 conforme Retificação I: https://cdnsite.institutoconsulplan.org.br/concursos/1330/b2c07c473c9749fea22728da3c964c06.pdf
- Página oficial do concurso: https://www.institutoconsulplan.org.br/Concurso/crapr2026
- RFC Editor - índice oficial das RFCs: https://www.rfc-editor.org/
- IANA - registro de nomes de serviços e portas: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
- NIST Cybersecurity Framework 2.0: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
- NIST SP 800-61 Rev. 3 - resposta a incidentes: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- Microsoft Learn - documentação oficial de Windows: https://learn.microsoft.com/windows/
- Linux Kernel Documentation: https://www.kernel.org/doc/html/latest/
- Lei nº 4.769/1965: https://www.planalto.gov.br/ccivil_03/leis/l4769.htm
- Decreto nº 61.934/1967: https://www.planalto.gov.br/ccivil_03/decreto/Antigos/D61934.htm
- RN CFA nº 651/2024 - Regimento Interno do CRA-PR: https://documentos.cfa.org.br/?a=show&c=documento&id=955
- RN CFA nº 671/2025 - Código de Ética: https://documentos.cfa.org.br/?a=show&c=documento&id=1038
- Constituição Federal, art. 37: https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm
- Provas públicas do Instituto Consulplan para cargos de Analista de Sistemas/TI foram usadas somente como referência de estilo, sem reprodução textual.

---

# Dia 1 — Redes: topologias, LAN/WAN e equipamentos

Base usada: `semana_02/semana_02_estudo.md`, seção `# Dia 1 - Redes: topologias, LAN/WAN e equipamentos`.

## Questões principais

### Questão 1

Em relação aos elementos fundamentais de uma rede de computadores, assinale a alternativa correta.

A) Nó designa o equipamento final que produz dados, excluindo switches e roteadores dessa classificação.
B) Host é equipamento intermediário que encaminha tráfego sem originar nem consumir comunicação.
C) Enlace é o conjunto de regras que define formato e sequência das mensagens trocadas entre aplicações.
D) Host é sistema final, interface o liga ao enlace e roteadores podem reunir redes em uma internetwork.

### Questão 2

O serviço de correio eletrônico do CRA-PR permanece disponível, embora o portal institucional esteja indisponível. A situação é compatível com a afirmação de que:

A) a Web inclui correio, voz e transferência de arquivos, de modo que sua indisponibilidade alcançaria esses serviços.
B) a Internet corresponde à infraestrutura física, enquanto a Web corresponde à totalidade dos protocolos de rede.
C) a Web é um serviço de aplicação utilizado sobre a Internet, que também pode transportar correio, voz e arquivos.
D) Internet e Web são denominações equivalentes quando o acesso ocorre em uma rede pública.

### Questão 3

Assinale a alternativa que diferencia corretamente protocolo de serviço.

A) Protocolo descreve a capacidade entregue ao usuário, enquanto serviço especifica o formato e a sequência das mensagens no enlace.
B) Protocolo define regras de comunicação, enquanto serviço é uma capacidade oferecida a outra camada ou aplicação.
C) Serviço existe apenas na camada de aplicação, enquanto protocolo existe apenas nas camadas física e de enlace.
D) Protocolo e serviço tornam-se conceitos equivalentes quando os dispositivos utilizam a suíte TCP/IP.

### Questão 4

Duas estações foram conectadas por um enlace funcional, mas não conseguem trocar informações porque utilizam parâmetros incompatíveis. Considerando os elementos da comunicação de dados, assinale a alternativa correta.

A) A existência de um meio funcional torna o protocolo opcional quando emissor e receptor usam o mesmo tipo de equipamento.
B) Emissor e receptor são necessários apenas em full-duplex; em simplex, o meio assume uma dessas funções.
C) Mensagem e meio podem ser tratados como o mesmo elemento quando o conteúdo transmitido é digital.
D) Conectividade física não assegura comunicação quando protocolos ou parâmetros são incompatíveis.

### Questão 5

Analise as associações a seguir.

I. Sensor que apenas envia medições: simplex.
II. Rádio comunicador em que os lados falam alternadamente: half-duplex.
III. Enlace Ethernet comutado em que os lados transmitem simultaneamente: full-duplex.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I, II e III.
D) I e II, apenas.

### Questão 6

Um enlace possui capacidade nominal de 100 Mbit/s. Em uma janela de 10 segundos, foram transportados 900 Mbit, dos quais 720 Mbit correspondiam ao conteúdo útil recebido pela aplicação. Desconsidere variações dentro da janela. Assinale os valores de largura de banda, throughput e goodput, respectivamente.

A) 100 Mbit/s, 90 Mbit/s e 72 Mbit/s.
B) 90 Mbit/s, 100 Mbit/s e 72 Mbit/s.
C) 100 Mbit/s, 72 Mbit/s e 90 Mbit/s.
D) 90 Mbit/s, 72 Mbit/s e 100 Mbit/s.

### Questão 7

Durante a transferência de um arquivo, a aplicação recebe 480 MB úteis, enquanto a rede transporta também cabeçalhos, confirmações e retransmissões. Nesse contexto, assinale a alternativa correta.

A) Goodput inclui cabeçalhos e retransmissões, ao passo que throughput considera apenas o arquivo útil entregue.
B) Throughput corresponde à capacidade nominal do enlace, enquanto goodput corresponde a toda a taxa transmitida no meio.
C) Retransmissões bem-sucedidas integram o goodput porque, ao final, seus dados também alcançam o receptor.
D) Goodput corresponde à parcela útil percebida pela aplicação e tende a ser menor ou igual ao throughput.

### Questão 8

Um sistema remoto responde de forma estável, mas cada interação leva cerca de 180 ms para percorrer o caminho e retornar. A medida diretamente associada a esse atraso é:

A) largura de banda.
B) latência.
C) goodput.
D) perda.

### Questão 9

Em uma chamada de voz, os pacotes chegam com intervalos muito variáveis e alguns não chegam ao destino. Assinale a descrição correta.

A) A variação dos intervalos é largura de banda, e a ausência de pacotes é goodput.
B) A variação dos intervalos é perda, e a ausência de pacotes é latência.
C) Jitter é variação da latência, enquanto perda é ausência de dados esperados.
D) Jitter e perda são sinônimos, pois ambos medem a capacidade nominal do enlace.

### Questão 10

Quatro computadores estão ligados individualmente a um hub central. Quanto às topologias física e lógica, essa rede apresenta:

A) malha física completa e estrela lógica com enlaces seletivos.
B) estrela física e comportamento lógico de meio compartilhado semelhante a barramento.
C) barramento físico e anel lógico com passagem obrigatória de token.
D) estrela física e lógica comutada, pois a presença de um equipamento central definiria ambos os comportamentos.

### Questão 11

Em uma topologia física em estrela, é correto afirmar que:

A) a falha de um enlace de acesso tende a afetar um nó; a do centro pode afetar a estrela inteira.
B) os nós compartilham um cabo linear principal, e o ponto central serve apenas para terminação.
C) cada nó mantém ligação direta com os demais, usando o equipamento central somente para redundância.
D) o tráfego deve percorrer um caminho fechado em um único sentido.

### Questão 12

Sobre as topologias de rede, assinale a alternativa INCORRETA.

A) Na estrela, os enlaces de acesso convergem para um ponto central.
B) No anel, os nós formam conceitualmente um caminho fechado.
C) No barramento, cada nó possui enlace exclusivo com um equipamento central.
D) A topologia híbrida combina duas ou mais organizações topológicas.

### Questão 13

Determinada tecnologia conecta conceitualmente cada nó ao seguinte, formando um caminho fechado, e pode empregar passagem de token para ordenar o acesso. Trata-se de topologia em:

A) barramento.
B) anel.
C) estrela.
D) árvore comutada.

### Questão 14

Um projeto possuía malha completa entre sete roteadores, com um enlace ponto a ponto para cada par. Após a remoção de exatamente um desses enlaces, sem criação de outro, assinale a quantidade de ligações diretas que permanece.

A) 14.
B) 18.
C) 20.
D) 21.

### Questão 15

Sobre malha completa e malha parcial, assinale a alternativa correta.

A) Na malha parcial, cada nó possui ligação direta com os demais, mas apenas um enlace fica ativo.
B) Na malha completa, todos os pares se ligam diretamente; na parcial, apenas alguns pares possuem ligação direta.
C) A malha completa utiliza menos portas que uma estrela com a mesma quantidade de nós.
D) A malha parcial trabalha com caminho único e, por isso, dispensa mecanismos de encaminhamento.

### Questão 16

Uma organização adota estrelas de acesso em cada andar e interliga os switches centrais por enlaces redundantes que formam outra organização topológica. A rede resultante é classificada como:

A) híbrida.
B) malha parcial, pois a redundância do núcleo também define a topologia dos enlaces de acesso.
C) estrela pura, pois a convergência nos andares impede outra classificação para o conjunto.
D) anel, pois a interligação redundante entre equipamentos centrais determina um único ciclo para o conjunto.

### Questão 17

Analise as afirmativas sobre topologia física e lógica.

I. Uma estrela física com hub pode apresentar meio lógico compartilhado.
II. A existência de um equipamento central prova que a circulação lógica é seletiva.
III. Implementações específicas podem apresentar anel lógico sem reproduzir exatamente um anel físico.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I e III, apenas.
D) I, II e III.

### Questão 18

Um relógio inteligente troca dados diretamente com o celular de seu usuário por tecnologia de curto alcance. Esse conjunto exemplifica, tipicamente, uma:

A) WAN.
B) MAN.
C) LAN metropolitana.
D) PAN.

### Questão 19

Durante uma falha do provedor, estações associam-se ao AP, obtêm acesso à impressora da mesma VLAN e não alcançam destinos externos. Assinale o diagnóstico conceitualmente correto.

A) O acesso à impressora comprova a conectividade local e também confirma o funcionamento do enlace com o provedor.
B) A falha externa altera o escopo da WLAN para PAN enquanto os clientes permanecem associados ao mesmo AP.
C) A comunicação local demonstra que o AP roteou entre sub-redes, ainda que clientes e impressora estejam na mesma VLAN.
D) O caminho local da WLAN pode funcionar sem Internet; o diagnóstico deve prosseguir no gateway, no enlace WAN ou no provedor.

### Questão 20

Um conselho interliga três unidades localizadas em diferentes bairros da mesma região metropolitana por infraestrutura de operadora. Quanto ao escopo típico, essa rede é melhor caracterizada como:

A) PAN.
B) MAN.
C) LAN limitada a uma sala.
D) barramento, pois utiliza infraestrutura compartilhada.

### Questão 21

A sede de um órgão em Curitiba é interligada a unidades em estados distintos por redes de longa distância. A classificação mais adequada é:

A) WAN.
B) PAN.
C) WLAN, ainda que nenhum enlace seja sem fio.
D) MAN, porque pertencer a uma única organização prevalece sobre a distribuição entre estados.

### Questão 22

Analise as afirmativas sobre meios de transmissão.

I. O par trançado é meio guiado.
II. A fibra continua sendo meio guiado, embora transporte luz.
III. A comunicação por rádio é meio não guiado.

Está correto o que se afirma em:

A) I, apenas.
B) I, II e III.
C) II e III, apenas.
D) I e III, apenas.

### Questão 23

Sobre cabos de par trançado UTP e versões blindadas, assinale a alternativa correta.

A) O trançamento elimina toda interferência eletromagnética, mesmo fora dos limites do padrão utilizado.
B) A blindagem torna irrelevantes o aterramento e a instalação, pois atua independentemente da continuidade do sistema de proteção.
C) Variantes blindadas podem reduzir interferência, mas exigem instalação e aterramento adequados; o cobre não se torna imune.
D) UTP é adequado apenas a redes half-duplex e não permite negociação de velocidade.

### Questão 24

Um órgão precisa interligar dois prédios com alta capacidade, e o trajeto possui forte interferência eletromagnética. A solução tecnicamente mais coerente, desde que ópticas e distâncias sejam compatíveis, é:

A) cabo coaxial escolhido apenas por possuir blindagem, sem verificar alcance, capacidade ou compatibilidade das extremidades.
B) par trançado blindado escolhido sem avaliar distância e aterramento, pois a blindagem garantiria imunidade completa.
C) enlace Wi-Fi escolhido pela taxa nominal e pela intensidade do sinal, desconsiderando interferência e planejamento de canal.
D) fibra óptica projetada para o enlace, pois não conduz o sinal como corrente elétrica.

### Questão 25

A respeito de fibras monomodo e multimodo, assinale a alternativa correta.

A) Fibra multimodo é a opção indicada para longas distâncias, sem depender dos transceptores empregados.
B) Fibra monomodo utiliza vários modos de propagação e, por definição, limita-se a enlaces internos curtos.
C) Monomodo favorece distâncias maiores; multimodo é comum em enlaces internos, conforme o projeto.
D) Ambas conduzem sinais elétricos e, por isso, sofrem a mesma interferência de um cabo de cobre.

### Questão 26

O meio guiado formado por condutor central, isolante e blindagem, historicamente empregado em formas de Ethernet em barramento, é o cabo:

A) de fibra multimodo.
B) de par trançado UTP.
C) coaxial.
D) óptico monomodo.

### Questão 27

Em uma sala, os clientes exibem sinal Wi-Fi forte, mas a vazão é baixa nos horários de maior uso. A explicação tecnicamente adequada é:

A) A intensidade do sinal basta para inferir goodput máximo, tornando suspeita a medição de baixa vazão.
B) Cada cliente recebe um canal exclusivo, razão pela qual a densidade de estações não reduz a vazão.
C) A distância explica a baixa vazão, enquanto canais, obstáculos e interferência não alteram o resultado.
D) Interferência, contenção e densidade de clientes podem reduzir o throughput mesmo com sinal forte.

### Questão 28

Assinale a alternativa que apresenta uma função compatível com a placa de rede de um host.

A) Transmitir e receber quadros, usar MAC no enlace e negociar velocidade e duplex.
B) Selecionar as rotas IP da organização a partir de uma tabela mantida pela própria interface.
C) Traduzir protocolos de aplicação antes de encapsular os dados em quadros.
D) Separar os domínios de broadcast associados ao host sem exercer roteamento.

### Questão 29

Um servidor possui duas interfaces físicas e uma interface virtual. A respeito dessas interfaces e de seus endereços, assinale a alternativa correta.

A) O servidor só pode ter um endereço MAC, pois o MAC identifica de forma absoluta o gabinete.
B) Cada interface pode ter endereçamento próprio; o MAC identifica a interface no enlace, não a pessoa.
C) Interfaces virtuais não participam de redes porque não correspondem a uma placa removível.
D) As interfaces de um mesmo servidor devem pertencer à mesma sub-rede e ao mesmo enlace.

### Questão 30

Um equipamento regenera o sinal para ampliar o alcance de um enlace compatível, sem aprender endereços MAC nem escolher rotas IP. Esse equipamento é um:

A) roteador.
B) gateway de aplicação.
C) switch de camada 3.
D) repetidor.

### Questão 31

Sobre o hub Ethernet clássico, assinale a alternativa correta.

A) É repetidor multiporta que retransmite bits e mantém um meio compartilhado em half-duplex.
B) Aprende os endereços MAC de origem e encaminha unicast conhecido pela porta associada ao destino.
C) Separa domínios de broadcast por porta e executa roteamento entre eles.
D) Mantém uma tabela IP para selecionar o próximo salto de cada quadro.

### Questão 32

Um setor substituiu um hub por um switch de camada 2 e manteve todos os dispositivos na mesma VLAN. Analise as afirmativas.

I. O switch isola os segmentos conectados às suas portas.
II. Unicast conhecido pode ser encaminhado seletivamente.
III. O switch de camada 2 cria um domínio de broadcast por porta, mesmo na mesma VLAN.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) III, apenas.
D) I e II, apenas.

### Questão 33

Uma bridge recebe um quadro por determinado segmento. O procedimento compatível com sua operação é:

A) aprender o MAC de origem no segmento de entrada e filtrar, encaminhar ou inundar conforme o destino.
B) aprender o endereço IP de destino e descartar unicast cujo destino ainda não tenha sido aprendido.
C) regenerar os bits nas portas de saída sem examinar endereços de enlace.
D) substituir o endereço IP do pacote para permitir comunicação entre redes privadas e públicas.

### Questão 34

Um switch recebe um quadro unicast cujo MAC de destino ainda não consta de sua tabela. Todos os enlaces pertencem à mesma VLAN. O switch deve:

A) aprender o MAC de origem e inundar o quadro pelas portas pertinentes, exceto a porta de entrada.
B) converter o quadro em broadcast, alterando o endereço MAC de destino para todos os bits iguais a 1.
C) tratar o destino desconhecido como remoto e encaminhar o quadro ao roteador da VLAN.
D) manter o quadro retido até que o destino se registre por um protocolo de controle da tabela MAC.

### Questão 35

Um switch recebe por uma porta um quadro cujo MAC de destino conhecido está associado à própria porta de entrada. A ação adequada é:

A) inundar o quadro em outras VLANs para confirmar a localização do destino.
B) encaminhar o quadro de volta pela mesma porta, duplicando sua entrega no segmento.
C) filtrar o quadro, pois não há motivo para devolvê-lo ao segmento de onde veio.
D) enviá-lo ao gateway padrão com base apenas na ausência de outra porta de saída.

### Questão 36

Ao receber um quadro de broadcast em uma porta de um switch de camada 2, sem filtros adicionais, o equipamento normalmente:

A) consulta a rota IP e encaminha o quadro para outra sub-rede.
B) inunda o quadro pelas portas pertinentes da mesma VLAN, exceto a de entrada.
C) entrega o quadro somente à porta que contém o MAC de destino em sua tabela.
D) descarta o quadro porque switches não encaminham broadcasts.

### Questão 37

Sobre portas de switch e colisões em Ethernet moderna, assinale a alternativa correta.

A) A porta isola o segmento; em full-duplex não há colisões, embora a contagem didática preserve essa segmentação.
B) Portas na mesma VLAN compartilham o meio half-duplex e o domínio de colisão, como em um hub.
C) A ausência de colisões reúne as VLANs em um domínio de broadcast comum ao equipamento.
D) Full-duplex permite transmissão em apenas um sentido por vez para prevenir colisões.

### Questão 38

A respeito de switches de camada 2 e de camada 3, assinale a alternativa INCORRETA.

A) Um switch de camada 2 pode aprender MACs de origem e encaminhar quadros dentro da LAN.
B) Um switch de camada 2 pode rotear entre sub-redes depois de aprender o MAC do gateway, mesmo sem função de camada 3.
C) Um switch multicamada compatível pode rotear quando essa função está habilitada e configurada.
D) Desativar o roteamento de um switch multicamada não o transforma em hub; a comutação de camada 2 pode permanecer.

### Questão 39

Uma estação envia dados a um servidor localizado em outra sub-rede. O equipamento responsável por selecionar o próximo salto com base no endereço IP e na tabela de rotas é o:

A) roteador.
B) hub.
C) repetidor.
D) access point em bridge.

### Questão 40

O termo gateway aparece em dois documentos: no primeiro, indica o próximo salto usado por uma estação; no segundo, indica um sistema que traduz protocolos de aplicação. A conclusão correta é:

A) o segundo documento usa o termo de forma inadequada, pois gateway designa uma interface física de saída.
B) gateway e hub são equivalentes quando o equipamento possui mais de uma porta de comunicação.
C) gateway pertence à camada de enlace e não pode designar uma interface de roteador.
D) gateway é contextual: pode indicar próximo salto ou intermediário que traduz protocolos.

### Questão 41

Um access point corporativo opera em modo bridge e conecta clientes IEEE 802.11 à LAN Ethernet. Nessa situação, o AP:

A) precisa executar NAT e DHCP para permitir a associação das estações ao rádio.
B) assume a escolha de rotas entre as sub-redes alcançadas pela rede de distribuição.
C) retransmite outro sinal Wi-Fi e dispensa conexão à rede de distribuição.
D) integra as estações sem fio à rede de distribuição e não precisa exercer roteamento, NAT ou DHCP.

### Questão 42

Estações sem fio associadas a um SSID e computadores cabeados pertencem à mesma VLAN. O AP opera em bridge. Analise as afirmativas.

I. Sem isolamento ou filtros, o AP pode estender o broadcast da VLAN aos clientes sem fio.
II. O nome do SSID cria, por si só, uma nova sub-rede e um novo domínio de broadcast.
III. Mapeamento para outra VLAN ou isolamento de clientes pode alterar o alcance da comunicação.

Está correto o que se afirma em:

A) I e III, apenas.
B) II, apenas.
C) I e II, apenas.
D) I, II e III.

### Questão 43

Quanto ao acesso ao meio em redes Wi-Fi, assinale a alternativa correta.

A) Estações IEEE 802.11 utilizam CSMA/CD exatamente como um hub Ethernet e detectam colisões da mesma forma.
B) Cada estação recebe um meio físico exclusivo e, por isso, não existe contenção entre clientes do mesmo rádio.
C) O rádio é compartilhado e o acesso é associado didaticamente a CSMA/CA, não ao CSMA/CD do Ethernet legado.
D) A VLAN reserva intervalos exclusivos de transmissão e afasta a contenção no canal de rádio.

### Questão 44

Um equipamento doméstico possui porta WAN, quatro portas LAN e rádio Wi-Fi, além de oferecer NAT e DHCP. Assinale a associação funcional INCORRETA.

A) As quatro portas LAN podem pertencer à função de switch integrada ao aparelho.
B) O access point realiza o NAT entre WAN e LAN, enquanto o roteador apenas controla o rádio.
C) A função de roteador pode interligar a rede LAN à interface WAN.
D) NAT e DHCP podem ser serviços adicionais do produto, sem definir isoladamente a função de access point.

### Questão 45

Seis computadores estão ligados diretamente a um switch, todos na VLAN 10, e uma sétima porta de acesso da VLAN 10 liga o switch a uma interface de roteador. Todos os enlaces operam em full-duplex. Assinale a alternativa correta.

A) Existem sete domínios de broadcast e um único enlace isolado pelo switch.
B) O switch passa a compartilhar um domínio de colisão entre os computadores porque pertencem à mesma VLAN.
C) Existe um domínio de broadcast, sete enlaces isolados e nenhuma colisão nos enlaces full-duplex.
D) Existem seis domínios de broadcast, pois a porta ligada ao roteador não participa da VLAN.

### Questão 46

Três computadores foram colocados na VLAN 10 e outros três na VLAN 20, no mesmo switch. Para que os grupos se comuniquem entre si, é correto afirmar que:

A) permanece um único domínio de broadcast, e o switch de camada 2 encaminha entre VLANs sem função adicional.
B) existem dois domínios de broadcast, e a comunicação entre eles exige roteamento.
C) existem seis domínios de broadcast, um para cada porta de acesso.
D) a criação de VLANs segmenta os enlaces, mas preserva um domínio de broadcast comum aos grupos.

### Questão 47

Em uma única VLAN, um switch conecta diretamente dois computadores, um roteador e um hub que atende três outros computadores. Para esta questão, adote a convenção didática tradicional: cada segmento isolado por uma porta do switch é contado como domínio de colisão, enquanto todos os equipamentos permanecem no mesmo domínio de broadcast. Assinale, respectivamente, as quantidades desses domínios.

A) 1 e 4.
B) 4 e 1.
C) 6 e 4.
D) 7 e 2.

### Questão 48

Um switch mantém usuários na VLAN 30 e servidores na VLAN 40. Um equipamento multicamada realiza a comunicação controlada entre elas. Analise as afirmativas.

I. Cada VLAN forma um domínio de broadcast distinto.
II. O roteamento não propaga broadcasts locais de camada 2 entre as VLANs por padrão.
III. Compartilhar o mesmo switch físico não reúne as duas VLANs em um único domínio de broadcast.

Está correto o que se afirma em:

A) I, II e III.
B) I, apenas.
C) II e III, apenas.
D) I e II, apenas.

### Questão 49

Um AP em bridge conecta clientes sem fio à mesma VLAN de estações cabeadas. Assinale a alternativa tecnicamente precisa.

A) O rádio constitui um domínio de colisão Ethernet idêntico ao de um hub e utiliza CSMA/CD.
B) O AP em bridge contém o broadcast na fronteira sem fio mesmo quando não há isolamento configurado.
C) A associação ao AP mapeia cada cliente para uma VLAN e uma sub-rede próprias.
D) O AP pode estender o broadcast da VLAN, mas contenção Wi-Fi não equivale à colisão Ethernet de um hub.

### Questão 50

Um órgão interliga por roteadores a LAN administrativa, a rede de um datacenter e uma unidade remota, oferecendo armazenamento aos usuários. Analise as afirmativas.

I. O conjunto de redes interligadas por roteadores forma uma internetwork.
II. O armazenamento acessível aos usuários é um recurso compartilhado.
III. Uma internetwork privada, por usar roteadores, constitui parte pública da Internet e da Web.

Está correto o que se afirma em:

A) I e II, apenas.
B) I e III, apenas.
C) II e III, apenas.
D) I, II e III.

## Questões extras de revisão fixa do Dia 1

#### Extra Dia 1.1

Sobre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967, assinale a alternativa correta.

A) A lei regula o exercício profissional e estrutura o Sistema CFA/CRAs, enquanto o decreto regulamenta a aplicação da lei.
B) O decreto possui função de conselho regional e limita sua aplicação ao estado em que foi publicado.
C) A lei trata apenas da organização interna do CRA-PR, e o decreto institui o Código de Ética vigente.
D) A regulamentação por decreto substitui integralmente a lei e permite afastar seus requisitos.

#### Extra Dia 1.2

Quanto à atuação do CFA e do CRA-PR no sistema profissional, assinale a alternativa correta.

A) O CRA-PR formula normas nacionais vinculantes para os demais conselhos regionais.
B) O CFA atua como conselho regional do Distrito Federal e não exerce orientação nacional.
C) CFA e CRA-PR possuem a mesma jurisdição territorial, diferenciando-se apenas pela sede.
D) O CFA exerce orientação e disciplina em âmbito nacional, e o CRA-PR executa, registra e fiscaliza em sua jurisdição.

#### Extra Dia 1.3

De acordo com o Regimento aprovado pela RN CFA nº 651/2024, o CRA-PR é:

A) associação privada sem autonomia financeira, subordinada administrativamente ao governo estadual.
B) autarquia com personalidade jurídica de direito público e autonomia técnica, administrativa e financeira.
C) órgão integrante da Administração Direta federal, sem personalidade jurídica própria.
D) empresa pública estadual encarregada exclusivamente de arrecadar anuidades profissionais.

#### Extra Dia 1.4

Sobre sede e jurisdição do CRA-PR, assinale a alternativa correta.

A) Sua sede fica no Distrito Federal, e sua jurisdição alcança os estados da Região Sul.
B) Sua sede pode ser fixada em qualquer município, e sua jurisdição limita-se à respectiva comarca.
C) Sua sede está na capital do Paraná, e sua jurisdição abrange todo o estado do Paraná.
D) Sua sede é definida pelo governo estadual, e sua jurisdição é nacional para fins de fiscalização.

#### Extra Dia 1.5

Entre as atribuições regimentais do CRA-PR, encontra-se:

A) editar leis federais sobre o exercício de todas as profissões regulamentadas.
B) executar diretrizes do CFA, manter registros, fiscalizar atividades e julgar infrações em sua jurisdição.
C) revisar decisões judiciais e aplicar sanções penais a quem exercer atividade irregular.
D) substituir o CFA na formulação das diretrizes nacionais sempre que o fato ocorrer no Paraná.

#### Extra Dia 1.6

Assinale a alternativa que apresenta apenas órgãos ou estruturas previstos no Regimento do CRA-PR.

A) Plenário, Senado Federal, Ouvidoria e Tribunal de Contas do Estado.
B) Diretoria Executiva, Ministério Público, Plenário e assembleia legislativa.
C) Plenário, Diretoria Executiva, Ouvidoria, comissões e órgãos de representação.
D) Ouvidoria, Poder Judiciário, grupos de trabalho e conselho municipal.

#### Extra Dia 1.7

No âmbito do CRA-PR, o Plenário é caracterizado como:

A) unidade de atendimento sem competência deliberativa ou de julgamento.
B) órgão consultivo externo que apenas recomenda decisões à Diretoria Executiva.
C) instância recursal nacional responsável por uniformizar decisões de todos os CRAs.
D) órgão colegiado de deliberação superior e primeira instância de julgamento em sua jurisdição.

#### Extra Dia 1.8

A respeito da Ouvidoria do CRA-PR, assinale a alternativa correta.

A) Possui caráter executivo e pode substituir a Diretoria na prática de atos administrativos.
B) Exerce função mediadora e não possui caráter administrativo, executivo, deliberativo ou decisório.
C) Atua como primeira instância de julgamento disciplinar e aplica diretamente as penalidades.
D) Formula as diretrizes nacionais do sistema e revisa as normas expedidas pelo CFA.

#### Extra Dia 1.9

Quanto ao alcance do Código de Ética aprovado pela RN CFA nº 671/2025, assinale a alternativa correta.

A) Alcança profissionais de Administração e pessoas jurídicas registradas, consideradas as especificidades destas.
B) Aplica-se apenas a pessoas físicas, pois pessoas jurídicas não se submetem a deveres ou sanções éticas.
C) Alcança qualquer empresa brasileira, ainda que sua atividade não se relacione ao sistema profissional.
D) Restringe-se aos conselheiros do CFA e dos CRAs durante o exercício de mandato eletivo.

#### Extra Dia 1.10

Constitui conjunto compatível com os deveres éticos previstos na RN CFA nº 671/2025:

A) publicidade irrestrita de informações, dependência técnica do contratante e recusa de aperfeiçoamento.
B) defesa de vantagem própria, empréstimo do registro e ocultação de documentos da fiscalização.
C) assinatura de documentos sem supervisão, divulgação de sigilo e tratamento hostil aos representantes do sistema.
D) zelo, honestidade, independência técnica, aperfeiçoamento e colaboração com o Sistema CFA/CRAs.

#### Extra Dia 1.11

Sobre o dever de sigilo profissional, assinale a alternativa correta.

A) O profissional deve guardar informação conhecida em razão do exercício profissional lícito, ressalvada situação juridicamente justificável.
B) O dever alcança apenas informação recebida por escrito e termina automaticamente com o contrato.
C) O profissional pode divulgar informação sigilosa para obter vantagem, desde que não haja dano financeiro imediato.
D) O sigilo impede o atendimento de qualquer obrigação legal ou determinação válida da autoridade competente.

#### Extra Dia 1.12

Um profissional assina relatório preparado por terceiro sem ter orientado nem supervisionado efetivamente o trabalho. Segundo o núcleo ético estudado, essa conduta:

A) é regular quando o terceiro possui experiência prática, ainda que não haja supervisão.
B) é obrigatória para preservar a continuidade do serviço contratado.
C) representa conduta de risco ético por atribuir chancela profissional sem orientação ou supervisão efetiva.
D) produz apenas consequência contratual, sem possível repercussão perante o sistema profissional.

#### Extra Dia 1.13

Assinale a alternativa que reúne as espécies de sanção previstas no Código de Ética estudado.

A) Recomendação verbal, multa administrativa isolada, prisão e perda de função pública.
B) Advertência pública, censura reservada, interdição do estabelecimento e detenção.
C) Censura privada, suspensão tributária, cancelamento empresarial e advertência oral.
D) Advertência escrita e reservada, censura pública, suspensão do exercício e cancelamento do registro profissional.

#### Extra Dia 1.14

Em relação às pessoas jurídicas registradas e às sanções éticas, assinale a alternativa correta.

A) Pessoas jurídicas não são alcançadas pelo Código e não podem receber medida ética ou multa.
B) Pessoas jurídicas recebem suspensão do exercício profissional nos mesmos termos aplicáveis à pessoa física.
C) Suspensão e cancelamento profissional não se aplicam à pessoa jurídica, que permanece sujeita às sanções compatíveis e à multa prevista.
D) A única consequência possível para pessoa jurídica é o cancelamento automático de sua inscrição, sem processo.

#### Extra Dia 1.15

Em processo ético, a equipe identifica uma possível infração praticada por pessoa registrada. A conclusão adequada é:

A) escolher imediatamente a sanção mais grave, pois a gravidade percebida dispensa enquadramento normativo.
B) aplicar apenas multa, porque o Código não prevê sanções disciplinares acompanhadas de consequência pecuniária.
C) arquivar o fato sempre que não houver prejuízo financeiro comprovado, independentemente da conduta.
D) realizar o enquadramento e observar o processo e as regras aplicáveis, inclusive a disciplina da multa que acompanha as sanções.

#### Extra Dia 1.16

Um enunciado determina: “Assinale a alternativa INCORRETA”. Para responder adequadamente, o candidato deve:

A) marcar a primeira afirmação tecnicamente verdadeira e encerrar a leitura.
B) identificar a opção que contraria o texto ou a regra, tratando-a como a exceção pedida.
C) desconsiderar a palavra destacada e procurar a síntese do conteúdo estudado.
D) selecionar a alternativa mais abrangente, ainda que extrapole o comando.

#### Extra Dia 1.17

Leia o trecho: “A fibra reduz a exposição à interferência eletromagnética no enlace óptico, mas sua implantação exige componentes compatíveis.” Assinale a inferência autorizada.

A) A escolha da fibra não elimina a necessidade de projeto e de compatibilidade entre os componentes.
B) Toda instalação de fibra oferece maior velocidade que qualquer instalação de cobre.
C) A fibra dispensa transceptores, conectores e procedimentos de instalação.
D) A ausência de interferência eletromagnética garante menor custo de implantação.

#### Extra Dia 1.18

No período “O switch segmenta os enlaces; contudo, mantém o broadcast dentro da mesma VLAN”, o conector “contudo” estabelece relação de:

A) causa.
B) oposição ou ressalva.
C) conclusão.
D) condição.

#### Extra Dia 1.19

Sobre palavras como “sempre”, “nunca”, “todos” e “necessariamente” em uma alternativa, assinale a orientação correta.

A) Elas ampliam o alcance da afirmação e exigem apoio integral do texto ou da regra, embora não sejam erradas por si mesmas.
B) Elas tornam a alternativa falsa em qualquer contexto, mesmo quando reproduzem literalmente uma regra sem exceção.
C) Elas devem ser ignoradas, pois não interferem no sentido nem no alcance da proposição.
D) Elas indicam conclusão lógica e podem substituir conectores como “portanto” e “logo”.

#### Extra Dia 1.20

Leia: “O switch reduz a propagação de colisões entre seus segmentos; contudo, não separa broadcasts entre portas da mesma VLAN.” A interpretação correta é:

A) A redução de colisões implica bloqueio dos broadcasts na mesma VLAN.
B) Colisão e broadcast designam o mesmo fenômeno, expresso por palavras diferentes.
C) Segmentação de colisões e alcance de broadcast são efeitos distintos da comutação.
D) O conector introduz conclusão de que o switch executa roteamento entre as portas.

## Gabarito do Dia 1

### Gabarito das questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | D |
| 2 | C |
| 3 | B |
| 4 | D |
| 5 | C |
| 6 | A |
| 7 | D |
| 8 | B |
| 9 | C |
| 10 | B |
| 11 | A |
| 12 | C |
| 13 | B |
| 14 | C |
| 15 | B |
| 16 | A |
| 17 | C |
| 18 | D |
| 19 | D |
| 20 | B |
| 21 | A |
| 22 | B |
| 23 | C |
| 24 | D |
| 25 | C |
| 26 | C |
| 27 | D |
| 28 | A |
| 29 | B |
| 30 | D |
| 31 | A |
| 32 | D |
| 33 | A |
| 34 | A |
| 35 | C |
| 36 | B |
| 37 | A |
| 38 | B |
| 39 | A |
| 40 | D |
| 41 | D |
| 42 | A |
| 43 | C |
| 44 | B |
| 45 | C |
| 46 | B |
| 47 | B |
| 48 | A |
| 49 | D |
| 50 | A |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 1.1 | A |
| 1.2 | D |
| 1.3 | B |
| 1.4 | C |
| 1.5 | B |
| 1.6 | C |
| 1.7 | D |
| 1.8 | B |
| 1.9 | A |
| 1.10 | D |
| 1.11 | A |
| 1.12 | C |
| 1.13 | D |
| 1.14 | C |
| 1.15 | D |
| 1.16 | B |
| 1.17 | A |
| 1.18 | B |
| 1.19 | A |
| 1.20 | C |

## Comentários do Dia 1

### Comentário da Questão 1

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Switches e roteadores também são nós, embora normalmente não sejam hosts finais da comunicação analisada.
- **B)** Incorreta. Host é o sistema final que origina ou consome a comunicação, não o intermediário definido apenas pelo encaminhamento.
- **C)** Incorreta. Enlace é a conexão direta entre interfaces; as regras de formato e sequência pertencem ao protocolo.
- **D)** Correta. A alternativa relaciona adequadamente host, interface, enlace e internetwork.

**Conceito:** elementos fundamentais de redes e interligação de redes.

**Pegadinha:** trocar equipamento intermediário por host ou chamar protocolo de enlace físico.

**Como pensar:** separe o participante final, seu ponto de conexão, o caminho direto e o conjunto de redes interligadas.

**Referência:** [1. Conceitos fundamentais de redes](semana_02_estudo.md#s2-d1-fundamentos).

### Comentário da Questão 2

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A indisponibilidade da Web não implica a interrupção de todos os demais serviços transportados pela Internet.
- **B)** Incorreta. Internet não é apenas infraestrutura física, e Web não corresponde à totalidade dos protocolos de rede.
- **C)** Correta. A Web é um serviço de aplicação, enquanto a Internet suporta também correio, voz, arquivos e outras aplicações.
- **D)** Incorreta. Os termos não se tornam sinônimos pelo fato de a rede ser pública.

**Conceito:** distinção entre rede, Internet e Web.

**Pegadinha:** usar o serviço mais visível, a Web, como se ele abrangesse toda a Internet.

**Como pensar:** verifique se o enunciado fala da infraestrutura de redes ou de uma aplicação executada sobre ela.

**Referência:** [1. Conceitos fundamentais de redes — Rede, Internet e Web](semana_02_estudo.md#s2-d1-fundamentos).

### Comentário da Questão 3

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A opção inverte as ideias: capacidade oferecida é serviço; formato e sequência das mensagens pertencem ao protocolo.
- **B)** Correta. Protocolo reúne regras da comunicação, e serviço descreve o que uma camada ou aplicação oferece.
- **C)** Incorreta. Protocolos e serviços aparecem em diferentes camadas, não apenas nas faixas rígidas indicadas.
- **D)** Incorreta. Utilizar TCP/IP não elimina a distinção entre as regras e a capacidade oferecida.

**Conceito:** protocolo em comparação com serviço.

**Pegadinha:** tratar os dois termos como nomes intercambiáveis porque atuam na mesma comunicação.

**Como pensar:** pergunte primeiro “como a troca é regida” e depois “qual capacidade é entregue”.

**Referência:** [1. Conceitos fundamentais de redes](semana_02_estudo.md#s2-d1-fundamentos).

### Comentário da Questão 4

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Equipamentos do mesmo tipo ainda precisam concordar sobre regras e parâmetros da troca.
- **B)** Incorreta. Emissor e receptor existem também em simplex; o meio não substitui nenhum deles.
- **C)** Incorreta. Mensagem é o conteúdo e meio é o caminho, mesmo quando ambos são representados digitalmente em algum estágio.
- **D)** Correta. Um enlace funcional não resolve incompatibilidade de protocolo ou de parâmetros.

**Conceito:** emissor, receptor, mensagem, meio e protocolo na comunicação de dados.

**Pegadinha:** concluir que presença de sinal ou cabo já comprova comunicação lógica válida.

**Como pensar:** percorra os cinco elementos e confirme se cada um cumpre uma função diferente.

**Referência:** [2. Comunicação de dados](semana_02_estudo.md#s2-d1-comunicacao-dados).

### Comentário da Questão 5

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmativa I está correta, mas II e III também estão.
- **B)** Incorreta. II e III são verdadeiras, porém a transmissão unilateral do sensor torna I verdadeira.
- **C)** Correta. Os exemplos representam, respectivamente, simplex, half-duplex e full-duplex.
- **D)** Incorreta. I e II estão corretas, mas o enlace com transmissão simultânea valida III.

**Conceito:** direção da comunicação.

**Pegadinha:** confundir duplex com número de equipamentos, em vez de observar o sentido e a simultaneidade.

**Como pensar:** marque se há um sentido, dois sentidos alternados ou dois sentidos simultâneos.

**Referência:** [2. Comunicação de dados — Direção da comunicação](semana_02_estudo.md#s2-d1-comunicacao-dados).

### Comentário da Questão 6

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A capacidade é 100 Mbit/s, o throughput é `900/10 = 90` Mbit/s e o goodput é `720/10 = 72` Mbit/s.
- **B)** Incorreta. Troca a capacidade nominal pelo volume efetivamente transportado por segundo.
- **C)** Incorreta. Inverte throughput e goodput; o total transportado não pode ser menor que sua parcela útil no cenário.
- **D)** Incorreta. Coloca a capacidade nominal como goodput e desloca as outras duas medidas.

**Conceito:** largura de banda, throughput e goodput.

**Pegadinha:** dividir corretamente os volumes pelo tempo e depois atribuir os resultados às métricas erradas.

**Como pensar:** fixe primeiro a capacidade nominal; calcule em seguida taxa total e, por último, taxa útil da aplicação.

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

### Comentário da Questão 7

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Cabeçalhos e retransmissões entram no tráfego transportado, não na parcela útil percebida pela aplicação.
- **B)** Incorreta. Capacidade nominal é largura de banda; throughput é a taxa efetivamente entregue.
- **C)** Incorreta. Uma retransmissão consome recursos, mas não cria conteúdo útil adicional para o arquivo.
- **D)** Correta. Goodput mede os dados úteis e, nesse modelo, não supera o throughput que os carrega.

**Conceito:** diferença entre vazão total e vazão útil.

**Pegadinha:** contar novamente como dado útil uma cópia retransmitida do mesmo conteúdo.

**Como pensar:** retire sobrecargas, confirmações e duplicações antes de calcular o que a aplicação realmente recebeu.

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

### Comentário da Questão 8

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Largura de banda expressa capacidade, não o tempo de resposta observado.
- **B)** Correta. Os 180 ms descrevem o atraso de percurso e retorno, relacionado à latência.
- **C)** Incorreta. Goodput mede a taxa útil entregue à aplicação.
- **D)** Incorreta. Perda é a ausência de dados esperados, não a demora estável na resposta.

**Conceito:** latência.

**Pegadinha:** associar toda experiência de lentidão a pouca largura de banda.

**Como pensar:** se o dado chega, mas demora, procure a medida de tempo; se não chega, examine perda.

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

### Comentário da Questão 9

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Variação temporal não é largura de banda, e ausência de pacotes não é goodput.
- **B)** Incorreta. A opção troca perda por jitter e latência.
- **C)** Correta. Jitter mede variação de latência; perda registra dados que não chegaram.
- **D)** Incorreta. As métricas são distintas e nenhuma delas representa capacidade nominal.

**Conceito:** jitter e perda em tráfego sensível a tempo.

**Pegadinha:** confundir o atraso variável de pacotes recebidos com o desaparecimento de pacotes.

**Como pensar:** observe duas perguntas separadas: “quando chegou” e “chegou ou não chegou”.

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

### Comentário da Questão 10

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não há ligação direta entre todos os pares, requisito da malha completa.
- **B)** Correta. Os cabos convergem para o hub, formando estrela física, mas o hub mantém o meio lógico compartilhado.
- **C)** Incorreta. O arranjo físico não é barramento e não há informação sobre token ou anel lógico.
- **D)** Incorreta. Um equipamento central pode ser hub ou switch; sua presença não prova comutação lógica.

**Conceito:** topologia física em contraste com topologia lógica.

**Pegadinha:** deduzir o comportamento da circulação apenas pelo desenho dos cabos.

**Como pensar:** identifique primeiro a disposição física e depois pergunte o que o equipamento central faz com o sinal ou quadro.

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Um enlace de acesso rompido costuma isolar seu nó, enquanto o centro é ponto comum da estrela.
- **B)** Incorreta. Cabo linear compartilhado caracteriza barramento, não estrela.
- **C)** Incorreta. Ligações diretas entre todos os pares descrevem malha completa.
- **D)** Incorreta. Caminho fechado remete ao anel.

**Conceito:** organização e pontos de falha da topologia em estrela.

**Pegadinha:** transferir para a estrela características de barramento, malha ou anel.

**Como pensar:** procure enlaces individuais convergindo para um centro e avalie separadamente falha de acesso e falha central.

**Referência:** [3. Topologia física e topologia lógica — Estrela](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 12

**Alternativa correta: C, pois o comando solicita a alternativa INCORRETA.**

**Análise das alternativas:**

- **A)** Correta quanto ao conteúdo. Convergência dos enlaces de acesso é característica da estrela.
- **B)** Correta quanto ao conteúdo. O anel forma conceitualmente um caminho fechado.
- **C)** Incorreta quanto ao conteúdo e, por isso, é o gabarito. Enlace exclusivo com equipamento central descreve estrela, não barramento.
- **D)** Correta quanto ao conteúdo. Uma topologia híbrida combina organizações distintas.

**Conceito:** reconhecimento comparado das topologias.

**Pegadinha:** saber a matéria e marcar uma afirmação verdadeira sem observar o comando negativo.

**Como pensar:** transforme mentalmente o enunciado em “procuro a exceção” e teste cada descrição.

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 13

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Barramento usa meio principal compartilhado, sem caminho fechado nó a nó.
- **B)** Correta. Conexão conceitual ao próximo nó e possível token são marcas do anel.
- **C)** Incorreta. Estrela exige convergência para ponto central.
- **D)** Incorreta. Árvore comutada não decorre da descrição de ciclo fechado.

**Conceito:** topologia em anel.

**Pegadinha:** associar token a qualquer rede compartilhada, ignorando o formato fechado.

**Como pensar:** combine as duas pistas: sequência entre vizinhos e retorno ao ponto inicial.

**Referência:** [3. Topologia física e topologia lógica — Anel](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 14

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Quatorze não resulta da contagem de todos os pares para sete nós.
- **B)** Incorreta. Dezoito subtrai quantidade indevida do total da malha completa.
- **C)** Correta. A malha completa teria `7 × 6 / 2 = 21` enlaces; retirado um, restam 20.
- **D)** Incorreta. Vinte e um é a quantidade anterior à remoção informada no enunciado.

**Conceito:** número de enlaces em malha completa.

**Pegadinha:** executar a fórmula e esquecer a alteração posterior do cenário.

**Como pensar:** calcule primeiro todos os pares não ordenados e só então aplique a remoção.

**Referência:** [3. Topologia física e topologia lógica — Malha](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 15

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Se cada nó se liga diretamente a todos, a malha é completa, não parcial.
- **B)** Correta. A diferença é a presença de ligação direta em todos os pares ou apenas em parte deles.
- **C)** Incorreta. Malha completa exige muito mais enlaces e portas que uma estrela, para quantidades usuais de nós.
- **D)** Incorreta. Redundância cria caminhos alternativos e não dispensa decisões de encaminhamento.

**Conceito:** malha completa e malha parcial.

**Pegadinha:** confundir “parcial” com enlace inativo em uma malha que fisicamente continua completa.

**Como pensar:** conte quais pares possuem ligação direta, sem considerar apenas o estado momentâneo do tráfego.

**Referência:** [3. Topologia física e topologia lógica — Malha](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 16

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O projeto reúne estrelas de acesso e outra organização no núcleo, formando topologia híbrida.
- **B)** Incorreta. Redundância central não transforma os enlaces em estrela dos andares em malha parcial.
- **C)** Incorreta. A classificação do conjunto não pode ignorar a organização diferente usada entre os centros.
- **D)** Incorreta. Redundância não prova a formação de um único anel.

**Conceito:** topologia híbrida.

**Pegadinha:** deixar uma parte mais visível do desenho determinar o nome de toda a rede.

**Como pensar:** decomponha o projeto em acesso e núcleo; se as organizações diferem, considere a combinação.

**Referência:** [3. Topologia física e topologia lógica — Híbrida](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 17

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. I é verdadeira, mas III também descreve uma divergência possível entre físico e lógico.
- **B)** Incorreta. II é falsa: centro físico pode ser hub ou switch; III é verdadeira.
- **C)** Correta. I e III são verdadeiras, enquanto II deduz indevidamente o comportamento lógico pelo centro.
- **D)** Incorreta. A falsidade de II impede que as três estejam corretas.

**Conceito:** independência relativa entre topologia física e lógica.

**Pegadinha:** usar a existência de um ponto central como prova de encaminhamento seletivo.

**Como pensar:** para cada afirmativa, separe a forma dos enlaces do método de circulação e acesso ao meio.

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

### Comentário da Questão 18

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. WAN interliga redes por grandes áreas, não o entorno imediato de uma pessoa.
- **B)** Incorreta. MAN corresponde ao escopo metropolitano.
- **C)** Incorreta. A expressão mistura LAN e alcance metropolitano sem representar o cenário pessoal.
- **D)** Correta. Relógio e celular em curto alcance formam exemplo típico de PAN.

**Conceito:** rede de área pessoal.

**Pegadinha:** classificar a rede apenas por ser sem fio, ignorando seu escopo e finalidade.

**Como pensar:** identifique quem administra a rede e qual ambiente ela pretende atender.

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

### Comentário da Questão 19

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Impressão local confirma parte da LAN, mas não comprova o enlace do provedor.
- **B)** Incorreta. Uma falha externa não altera o escopo da WLAN para PAN.
- **C)** Incorreta. Comunicação na mesma VLAN pode ocorrer por bridging, sem roteamento do AP.
- **D)** Correta. O caminho local está operacional e a investigação deve avançar para gateway, WAN ou provedor.

**Conceito:** WLAN como LAN independente do acesso à Internet.

**Pegadinha:** interpretar conectividade local bem-sucedida como prova de conectividade externa.

**Como pensar:** divida o percurso em associação sem fio, LAN/VLAN, gateway e enlace WAN; valide cada trecho.

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

### Comentário da Questão 20

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. PAN é restrita ao entorno pessoal.
- **B)** Correta. Unidades em bairros da mesma região metropolitana representam uso típico de MAN.
- **C)** Incorreta. O cenário ultrapassa uma sala, prédio ou campus local administrado como uma LAN.
- **D)** Incorreta. Barramento é topologia, não classificação geográfica; infraestrutura compartilhada não muda isso.

**Conceito:** rede de área metropolitana.

**Pegadinha:** misturar alcance da rede com sua topologia ou com a propriedade da infraestrutura.

**Como pensar:** escolha a classe pelo escopo funcional e administrativo, sem aplicar número rígido de quilômetros.

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

### Comentário da Questão 21

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A interligação entre unidades em estados distintos é exemplo típico de WAN.
- **B)** Incorreta. PAN atende o entorno pessoal, não sedes separadas geograficamente.
- **C)** Incorreta. WLAN exige acesso sem fio e continua sendo uma LAN, não uma classificação para qualquer rede extensa.
- **D)** Incorreta. Pertencer à mesma organização não transforma enlaces interestaduais em MAN.

**Conceito:** rede de longa distância.

**Pegadinha:** usar propriedade administrativa única para ignorar o escopo e as redes intermediárias.

**Como pensar:** avalie a finalidade e a abrangência; cidades, estados e países apontam para WAN.

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

### Comentário da Questão 22

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Afirmativa I é verdadeira, mas II e III também são.
- **B)** Correta. Par trançado e fibra confinam o sinal a um meio físico; rádio se propaga pelo espaço.
- **C)** Incorreta. Excluir I não se justifica, pois o par trançado é meio guiado.
- **D)** Incorreta. I e III são verdadeiras, mas a luz percorre a fibra, tornando II verdadeira.

**Conceito:** meios guiados e não guiados.

**Pegadinha:** classificar a fibra como não guiada apenas porque ela transporta luz.

**Como pensar:** pergunte se a energia segue um caminho físico delimitado ou se se propaga no espaço.

**Referência:** [5. Meios guiados e não guiados](semana_02_estudo.md#s2-d1-meios).

### Comentário da Questão 23

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O trançamento reduz interferência e diafonia, mas não produz imunidade completa.
- **B)** Incorreta. Blindagem mal instalada ou sem aterramento adequado pode não cumprir a proteção esperada.
- **C)** Correta. Versões blindadas exigem projeto e instalação coerentes e continuam sendo cobre.
- **D)** Incorreta. UTP pode operar em Ethernet full-duplex e negociar velocidade conforme interfaces e padrão.

**Conceito:** par trançado UTP e versões blindadas.

**Pegadinha:** transformar uma medida de mitigação de interferência em garantia absoluta.

**Como pensar:** compare material, blindagem, aterramento, categoria e padrão antes de concluir sobre desempenho.

**Referência:** [5. Meios guiados e não guiados — Par trançado](semana_02_estudo.md#s2-d1-meios).

### Comentário da Questão 24

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Blindagem do coaxial não dispensa análise de alcance, capacidade e compatibilidade.
- **B)** Incorreta. Par blindado ainda depende de distância, aterramento e padrão; não é imune.
- **C)** Incorreta. Taxa nominal e sinal não bastam diante de interferência e canais concorrentes.
- **D)** Correta. Fibra projetada para o enlace oferece alta capacidade e não sofre interferência eletromagnética no trecho óptico.

**Conceito:** seleção de meio por requisitos do cenário.

**Pegadinha:** escolher um meio por uma propriedade isolada sem validar o projeto das extremidades.

**Como pensar:** liste alcance, interferência, capacidade, mobilidade e compatibilidade; depois elimine soluções que ignoram um requisito crítico.

**Referência:** [5. Meios guiados e não guiados — Fibra óptica](semana_02_estudo.md#s2-d1-meios).

### Comentário da Questão 25

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Adequação a distância depende do tipo de fibra, ópticas e padrão; multimodo não é escolha automática para longas distâncias.
- **B)** Incorreta. Monomodo não utiliza vários modos e costuma ser associada a maiores alcances.
- **C)** Correta. A comparação respeita os usos típicos e preserva a ressalva do projeto.
- **D)** Incorreta. Fibra transporta luz e é imune à interferência eletromagnética no enlace óptico.

**Conceito:** fibra monomodo e multimodo.

**Pegadinha:** converter uma tendência de uso em regra universal independente dos transceptores.

**Como pensar:** nunca analise somente o núcleo; confirme padrão, óptica, velocidade e distância.

**Referência:** [5. Meios guiados e não guiados — Fibra óptica](semana_02_estudo.md#s2-d1-meios).

### Comentário da Questão 26

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Fibra multimodo possui núcleo e revestimentos ópticos, não condutor central metálico.
- **B)** Incorreta. UTP utiliza pares de condutores trançados.
- **C)** Correta. Condutor central, isolante e blindagem são a estrutura característica do coaxial.
- **D)** Incorreta. Monomodo também é fibra óptica e não corresponde à descrição metálica.

**Conceito:** cabo coaxial.

**Pegadinha:** associar toda blindagem a par trançado blindado e esquecer a construção coaxial.

**Como pensar:** visualize a seção transversal: um eixo condutor central envolvido por isolante e blindagem.

**Referência:** [5. Meios guiados e não guiados — Cabo coaxial](semana_02_estudo.md#s2-d1-meios).

### Comentário da Questão 27

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Intensidade de sinal é apenas uma variável e não comprova goodput máximo.
- **B)** Incorreta. Clientes do mesmo rádio disputam tempo no meio compartilhado.
- **C)** Incorreta. Canal, interferência, obstáculos e contenção alteram a vazão além da distância.
- **D)** Correta. O conjunto dessas variáveis explica throughput baixo mesmo com sinal forte.

**Conceito:** desempenho de comunicação sem fio.

**Pegadinha:** tratar barras de sinal como medição completa de capacidade e qualidade do canal.

**Como pensar:** diferencie cobertura de capacidade; investigue espectro, canal, densidade e ocupação do rádio.

**Referência:** [5. Meios guiados e não guiados — Comunicação sem fio](semana_02_estudo.md#s2-d1-meios).

### Comentário da Questão 28

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Transmissão de quadros, uso de MAC e negociação de velocidade e duplex são funções compatíveis com a NIC.
- **B)** Incorreta. Seleção de rotas da organização é função de roteamento, não da interface comum do host.
- **C)** Incorreta. NIC não traduz protocolos de aplicação antes de cada quadro.
- **D)** Incorreta. A interface, sozinha, não separa domínios de broadcast sem outra função de rede.

**Conceito:** placa ou interface de rede.

**Pegadinha:** atribuir à NIC todas as decisões tomadas pelos equipamentos intermediários.

**Como pensar:** limite a análise à conexão do host com o enlace e às tarefas de transmissão e recepção associadas.

**Referência:** [6. Placa de rede](semana_02_estudo.md#s2-d1-nic).

### Comentário da Questão 29

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Um sistema pode ter vários MACs, vinculados às suas interfaces no contexto de enlace.
- **B)** Correta. Interfaces físicas ou virtuais podem possuir configurações próprias, e MAC não identifica a pessoa.
- **C)** Incorreta. Interface virtual implementada por software pode participar normalmente da rede.
- **D)** Incorreta. Múltiplas interfaces podem pertencer a enlaces e sub-redes distintos.

**Conceito:** multiplicidade de interfaces e alcance do endereço MAC.

**Pegadinha:** usar MAC como identidade absoluta e imutável do computador ou usuário.

**Como pensar:** associe endereço de enlace à interface observada, não ao gabinete inteiro.

**Referência:** [6. Placa de rede](semana_02_estudo.md#s2-d1-nic).

### Comentário da Questão 30

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Roteador examina IP e tabela de rotas para interligar redes.
- **B)** Incorreta. Gateway de aplicação intermedeia ou traduz protocolos em contexto superior ao sinal bruto.
- **C)** Incorreta. Switch de camada 3 pode comutar e rotear, não apenas regenerar o sinal.
- **D)** Correta. Repetidor atua sobre bits ou sinal, sem aprendizagem MAC ou escolha de rota.

**Conceito:** repetidor.

**Pegadinha:** confundir ampliação de alcance físico com encaminhamento inteligente.

**Como pensar:** identifique a informação examinada; se o equipamento não lê MAC nem IP, a função é física.

**Referência:** [7. Repetidores e hubs — Repetidor](semana_02_estudo.md#s2-d1-repetidor-hub).

### Comentário da Questão 31

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Hub é repetidor multiporta e mantém o meio Ethernet legado compartilhado em half-duplex.
- **B)** Incorreta. Aprendizagem MAC e saída seletiva são características de bridge ou switch.
- **C)** Incorreta. Hub não separa broadcast nem executa roteamento.
- **D)** Incorreta. O equipamento não possui tabela IP para próximo salto.

**Conceito:** funcionamento do hub Ethernet clássico.

**Pegadinha:** imaginar que a existência de várias portas implica inteligência de encaminhamento.

**Como pensar:** trate o hub como repetidor: ele replica o sinal, sem consultar endereço.

**Referência:** [7. Repetidores e hubs — Hub](semana_02_estudo.md#s2-d1-repetidor-hub).

### Comentário da Questão 32

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. I é verdadeira, mas II também é; a resposta está incompleta.
- **B)** Incorreta. II é verdadeira, porém III é falsa porque a mesma VLAN preserva um domínio de broadcast.
- **C)** Incorreta. III atribui ao switch de camada 2 uma separação de broadcast que exige VLANs distintas ou roteamento.
- **D)** Correta. Substituir o hub isola segmentos e permite unicast seletivo sem dividir o broadcast da VLAN.

**Conceito:** efeitos da troca de hub por switch.

**Pegadinha:** concluir que segmentação de colisões cria automaticamente redes ou broadcasts separados por porta.

**Como pensar:** avalie dois eixos independentes: seletividade do unicast e alcance do broadcast.

**Referência:** [Diferenças entre conceitos parecidos — Hub x switch](semana_02_estudo.md#s2-d1-diferencas).

### Comentário da Questão 33

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A bridge aprende MAC de origem e usa o destino para filtrar, encaminhar ou inundar.
- **B)** Incorreta. Bridge de camada 2 não aprende IP como base dessa decisão nem descarta automaticamente unicast desconhecido.
- **C)** Incorreta. Replicar bits sem ler endereços descreve repetidor ou hub.
- **D)** Incorreta. Tradução de IP não integra a função básica de bridge.

**Conceito:** aprendizagem e decisão de uma bridge.

**Pegadinha:** atribuir à bridge a função do hub, roteador ou NAT porque todos intermediam tráfego.

**Como pensar:** procure o endereço de origem usado na aprendizagem e o MAC de destino usado na decisão.

**Referência:** [8. Bridges e switches — Bridge](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário da Questão 34

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O switch aprende a origem e inunda o unicast desconhecido nas portas pertinentes da VLAN, menos a entrada.
- **B)** Incorreta. Inundar não altera o MAC de destino nem transforma o quadro em broadcast.
- **C)** Incorreta. Desconhecido na tabela MAC não significa que o destino pertença a outra rede.
- **D)** Incorreta. O switch não depende de registro manual do destino para tentar a entrega inicial.

**Conceito:** tratamento de unicast desconhecido.

**Pegadinha:** confundir o modo de entrega por inundação com a natureza do endereço de destino.

**Como pensar:** preserve o quadro e varie somente as portas de saída; a resposta futura permitirá aprender o destino.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário da Questão 35

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Switch não inunda outras VLANs para confirmar um destino já conhecido.
- **B)** Incorreta. Devolver o quadro à porta de entrada seria redundante e contrariaria a filtragem.
- **C)** Correta. MAC de destino aprendido no próprio segmento de entrada leva o switch a filtrar o quadro.
- **D)** Incorreta. Gateway só participa quando o destino IP é remoto; a decisão proposta ignora essa verificação.

**Conceito:** filtragem de quadro na própria porta de entrada.

**Pegadinha:** decorar apenas “conhecido vai à porta do destino” e esquecer o caso em que essa porta é a entrada.

**Como pensar:** compare porta de entrada e porta associada ao destino; se forem iguais, não há saída útil.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário da Questão 36

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Switch de camada 2 não consulta rota para transportar broadcast local a outra sub-rede.
- **B)** Correta. O quadro é inundado nas portas pertinentes da mesma VLAN, exceto a entrada.
- **C)** Incorreta. Broadcast não possui uma única porta de destino na tabela MAC.
- **D)** Incorreta. Switches encaminham broadcasts dentro do domínio correspondente.

**Conceito:** propagação de broadcast por switch de camada 2.

**Pegadinha:** extrapolar a seletividade do unicast conhecido para todos os tipos de quadro.

**Como pensar:** classifique primeiro o destino como broadcast; depois limite a inundação à VLAN.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário da Questão 37

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A porta segmenta o enlace, mas full-duplex elimina colisões efetivas; a contagem por porta é ressalva didática.
- **B)** Incorreta. Mesma VLAN implica broadcast comum, não meio half-duplex comum entre portas do switch.
- **C)** Incorreta. Colisão e broadcast são domínios distintos; ausência da primeira não reúne VLANs.
- **D)** Incorreta. Full-duplex permite transmissão simultânea nos dois sentidos.

**Conceito:** segmentação por portas e ausência de colisões em full-duplex.

**Pegadinha:** repetir “uma colisão por porta” como ocorrência real em enlaces full-duplex modernos.

**Como pensar:** distinga capacidade de isolamento do segmento da existência efetiva de um meio sujeito a colisão.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário da Questão 38

**Alternativa correta: B, pois o comando solicita a alternativa INCORRETA.**

**Análise das alternativas:**

- **A)** Correta quanto ao conteúdo. Aprender MAC e encaminhar quadros são funções de camada 2.
- **B)** Incorreta quanto ao conteúdo e, portanto, é o gabarito. Aprender o MAC do gateway não concede função de roteamento a um switch de camada 2.
- **C)** Correta quanto ao conteúdo. Equipamento multicamada pode rotear quando compatível e configurado.
- **D)** Correta quanto ao conteúdo. Desabilitar a camada 3 não apaga necessariamente a comutação de camada 2.

**Conceito:** diferença entre switch de camada 2 e switch multicamada.

**Pegadinha:** confundir alcance do gateway aprendido em MAC com capacidade de consultar tabela de rotas.

**Como pensar:** confirme se o equipamento possui e exerce a função de camada 3; não a deduza da mera tabela MAC.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário da Questão 39

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Roteador consulta endereço IP e tabela de roteamento para selecionar o próximo salto.
- **B)** Incorreta. Hub apenas repete sinais no meio compartilhado.
- **C)** Incorreta. Repetidor atua no sinal e não interliga sub-redes por IP.
- **D)** Incorreta. AP em bridge integra meios na LAN, sem assumir a função de roteamento descrita.

**Conceito:** encaminhamento IP entre redes.

**Pegadinha:** escolher o equipamento presente no caminho sem observar qual campo ele precisa examinar.

**Como pensar:** se a decisão envolve rede remota, endereço IP e próximo salto, procure o roteador.

**Referência:** [9. Roteadores, gateways e access points — Roteador](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

### Comentário da Questão 40

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Gateway não se restringe a interface física e pode intermediar protocolos.
- **B)** Incorreta. Quantidade de portas não torna gateway equivalente a hub.
- **C)** Incorreta. O termo pode designar interface de roteador como gateway padrão.
- **D)** Correta. O contexto define se gateway é próximo salto ou tradutor e intermediário.

**Conceito:** significados contextuais de gateway.

**Pegadinha:** atribuir uma única camada ou função rígida a um termo polissêmico.

**Como pensar:** leia o complemento: “padrão” aponta ao próximo salto; “de aplicação” aponta à intermediação ou tradução.

**Referência:** [9. Roteadores, gateways e access points — Gateway](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

### Comentário da Questão 41

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Associação ao rádio não exige que o AP execute NAT ou DHCP.
- **B)** Incorreta. Escolha de rotas entre sub-redes é função de roteador ou equipamento multicamada.
- **C)** Incorreta. AP conectado à rede de distribuição não é, por definição, repetidor de outro sinal Wi-Fi.
- **D)** Correta. Em bridge, o AP integra IEEE 802.11 à LAN sem precisar exercer as funções citadas.

**Conceito:** access point em modo bridge.

**Pegadinha:** atribuir ao AP corporativo todas as funções reunidas em um roteador Wi-Fi doméstico.

**Como pensar:** decomponha o produto em rádio, comutação, roteamento e serviços auxiliares.

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

### Comentário da Questão 42

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. I e III reconhecem o bridging padrão e as configurações que podem alterar o alcance.
- **B)** Incorreta. II é falsa: o nome do SSID não cria, sozinho, VLAN ou sub-rede.
- **C)** Incorreta. I é verdadeira, mas II torna a combinação errada.
- **D)** Incorreta. A inclusão de II impede que as três afirmativas estejam corretas.

**Conceito:** relação entre AP, SSID, VLAN e domínio de broadcast.

**Pegadinha:** usar SSID como prova automática de segmentação lógica.

**Como pensar:** siga o mapeamento do SSID até a VLAN e procure isolamento, filtros ou túneis configurados.

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

### Comentário da Questão 43

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. IEEE 802.11 não usa CSMA/CD nem detecta colisões como Ethernet half-duplex legado.
- **B)** Incorreta. Clientes associados ao mesmo rádio compartilham o meio e disputam tempo de transmissão.
- **C)** Correta. O acesso Wi-Fi é associado didaticamente a CSMA/CA.
- **D)** Incorreta. VLAN segmenta logicamente tráfego, mas não reserva tempo exclusivo no canal de rádio.

**Conceito:** contenção e acesso ao meio sem fio.

**Pegadinha:** chamar o rádio compartilhado de domínio de colisão Ethernet e aplicar CSMA/CD.

**Como pensar:** lembre que Wi-Fi tenta evitar colisões; Ethernet compartilhado clássico procurava detectá-las.

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

### Comentário da Questão 44

**Alternativa correta: B, pois o comando solicita a associação INCORRETA.**

**Análise das alternativas:**

- **A)** Correta quanto ao conteúdo. As portas LAN podem compor um switch interno.
- **B)** Incorreta quanto ao conteúdo e, portanto, é o gabarito. Roteador interliga WAN e LAN; access point fornece o acesso de rádio.
- **C)** Correta quanto ao conteúdo. A função de roteamento pode encaminhar entre as interfaces LAN e WAN.
- **D)** Correta quanto ao conteúdo. NAT e DHCP são serviços adicionais e não definem um AP isolado.

**Conceito:** equipamento doméstico multifuncional.

**Pegadinha:** atribuir a função ao gabinete inteiro sem separar seus componentes lógicos.

**Como pensar:** desenhe caixas internas para switch, roteador, AP, NAT, firewall e DHCP.

**Referência:** [Exemplos práticos e resolvidos — Exemplo 5, equipamento doméstico multifuncional](semana_02_estudo.md#s2-d1-exemplos).

### Comentário da Questão 45

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Portas do switch não criam sete domínios de broadcast na mesma VLAN.
- **B)** Incorreta. Mesma VLAN preserva broadcast comum, mas não transforma portas comutadas em meio de colisão compartilhado.
- **C)** Correta. Há uma VLAN, sete enlaces isolados e ausência de colisões em full-duplex.
- **D)** Incorreta. O enunciado coloca expressamente a sétima porta de acesso na VLAN 10.

**Conceito:** contagem de broadcast e ressalva do full-duplex.

**Pegadinha:** usar a quantidade de portas tanto para colisão quanto para broadcast.

**Como pensar:** conte broadcasts por VLAN; depois verifique se os enlaces estão sujeitos a colisões reais.

**Referência:** [10. Domínio de colisão e domínio de broadcast — Exemplo de contagem](semana_02_estudo.md#s2-d1-dominios).

### Comentário da Questão 46

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Switch de camada 2 não encaminha diretamente entre VLANs e elas não compartilham broadcast.
- **B)** Correta. Cada VLAN forma um domínio de broadcast, e comunicação entre elas exige camada 3.
- **C)** Incorreta. Portas individuais não se tornam broadcasts separados quando pertencem à mesma VLAN.
- **D)** Incorreta. A finalidade central da VLAN no cenário é justamente separar os broadcasts dos grupos.

**Conceito:** VLAN e roteamento inter-VLAN.

**Pegadinha:** confundir segmentação por porta com separação lógica por VLAN.

**Como pensar:** conte os identificadores de VLAN e pergunte quem pode encaminhar pacotes de uma rede lógica à outra.

**Referência:** [10. Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios).

### Comentário da Questão 47

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Inverte as contagens e ignora a segmentação criada pelas portas do switch.
- **B)** Correta. Pela convenção declarada, há dois acessos diretos, o enlace do roteador e o segmento do hub: quatro; a VLAN forma um broadcast.
- **C)** Incorreta. Seis não corresponde aos segmentos isolados, e quatro broadcasts contrariariam a VLAN única.
- **D)** Incorreta. Sete contaria dispositivos em vez de segmentos, e não há segunda VLAN.

**Conceito:** contagem didática de segmentos de colisão e domínio de broadcast.

**Pegadinha:** contar cada host atrás do hub como domínio separado ou esquecer a convenção explicitada.

**Como pensar:** agrupe todos os participantes do hub em um segmento e conte cada outra porta usada do switch uma vez.

**Referência:** [10. Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios).

### Comentário da Questão 48

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. As três afirmativas descrevem corretamente a separação de broadcast por VLAN.
- **B)** Incorreta. I é verdadeira, mas II e III também são.
- **C)** Incorreta. II e III são verdadeiras, mas a combinação omite I.
- **D)** Incorreta. I e II estão corretas, porém III também está.

**Conceito:** independência lógica das VLANs no mesmo equipamento físico.

**Pegadinha:** imaginar que compartilhar o chassi do switch reúne novamente os broadcasts.

**Como pensar:** a fronteira relevante é o identificador da VLAN; o roteamento controla a passagem entre essas fronteiras.

**Referência:** [10. Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios).

### Comentário da Questão 49

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contenção 802.11 e CSMA/CA não equivalem ao domínio de colisão de um hub com CSMA/CD.
- **B)** Incorreta. AP em bridge pode encaminhar broadcasts da VLAN quando não há bloqueio configurado.
- **C)** Incorreta. Associação não cria por cliente uma VLAN e uma sub-rede próprias.
- **D)** Correta. A opção separa adequadamente alcance de broadcast e disputa pelo rádio.

**Conceito:** integração de broadcast cabeado e sem fio sem equiparar os meios.

**Pegadinha:** acertar que o rádio é compartilhado e, a partir disso, aplicar toda a terminologia do Ethernet legado.

**Como pensar:** trate bridging/VLAN para o alcance lógico e 802.11 para o acesso ao meio.

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

### Comentário da Questão 50

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. I define internetwork e II identifica o armazenamento acessível como recurso compartilhado.
- **B)** Incorreta. I é verdadeira, mas III confunde rede privada interligada com Internet e Web públicas.
- **C)** Incorreta. II é verdadeira, enquanto III é falsa.
- **D)** Incorreta. A falsidade de III impede que as três sejam aceitas.

**Conceito:** internetwork e recurso compartilhado.

**Pegadinha:** transformar qualquer conjunto roteado de redes em Internet ou Web.

**Como pensar:** diferencie o conceito genérico de redes interligadas do exemplo específico da Internet pública e de seus serviços.

**Referência:** [1. Conceitos fundamentais de redes](semana_02_estudo.md#s2-d1-fundamentos).

#### Comentário Extra Dia 1.1

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A Lei nº 4.769/1965 fornece a base legal do exercício profissional e do sistema, e o decreto a regulamenta.
- **B)** Incorreta. Decreto federal não exerce função de conselho regional nem possui aplicação limitada dessa forma.
- **C)** Incorreta. Regimento do CRA-PR e Código de Ética são objetos de normas próprias, não dessas descrições da lei e do decreto.
- **D)** Incorreta. Regulamentar não significa substituir ou afastar a lei regulamentada.

**Conceito:** relação entre lei e decreto regulamentador.

**Pegadinha:** inverter a hierarquia e atribuir ao decreto poder de revogação material da lei.

**Como pensar:** localize a norma-base e identifique a função de detalhamento exercida pelo regulamento.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Base legal e relação entre as normas](semana_02_estudo.md#s2-d1-revisao-base-legal).

#### Comentário Extra Dia 1.2

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. CRA-PR não edita normas nacionais para todos os regionais.
- **B)** Incorreta. CFA possui atuação nacional e não se reduz a um conselho regional do Distrito Federal.
- **C)** Incorreta. As jurisdições e os papéis institucionalmente atribuídos são diferentes.
- **D)** Correta. CFA orienta e disciplina nacionalmente; CRA-PR executa, registra e fiscaliza no Paraná.

**Conceito:** âmbito e função de CFA e CRA-PR.

**Pegadinha:** trocar “federal” por uma região específica e “regional” por jurisdição nacional.

**Como pensar:** associe CFA a diretrizes do sistema e CRA à execução e fiscalização em seu estado.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.3

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O CRA-PR não é associação privada nem se subordina administrativamente ao governo estadual nos termos descritos.
- **B)** Correta. A natureza autárquica, a personalidade de direito público e as três autonomias constam da revisão do Regimento.
- **C)** Incorreta. Autarquia possui personalidade jurídica e integra a Administração Indireta, não a Direta.
- **D)** Incorreta. O CRA-PR não é empresa pública nem possui a finalidade exclusiva indicada.

**Conceito:** natureza jurídica e autonomia do CRA-PR.

**Pegadinha:** misturar autarquia, órgão sem personalidade e empresa pública.

**Como pensar:** verifique personalidade, regime jurídico e posição na estrutura administrativa antes de olhar a atividade desempenhada.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A sede não fica no Distrito Federal e a jurisdição não abrange toda a Região Sul.
- **B)** Incorreta. O Regimento fixa sede na capital e jurisdição estadual, não municipal por escolha eventual.
- **C)** Correta. Curitiba, como capital, é a sede, e todo o Paraná integra a jurisdição do Conselho.
- **D)** Incorreta. Governo estadual não define sede dessa forma, e a fiscalização do CRA-PR não é nacional.

**Conceito:** sede e jurisdição do CRA-PR.

**Pegadinha:** confundir local da sede com limite municipal da atuação.

**Como pensar:** memorize o par: sede na capital, jurisdição em todo o estado.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.5

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Conselho regional não edita leis federais sobre todas as profissões.
- **B)** Correta. A alternativa reúne execução de diretrizes, registro, fiscalização e julgamento regional de infrações.
- **C)** Incorreta. CRA-PR não revisa decisões judiciais nem aplica sanções penais.
- **D)** Incorreta. Competência regional não autoriza substituir o CFA na formulação nacional.

**Conceito:** competências centrais do CRA-PR.

**Pegadinha:** ampliar poder fiscalizatório e disciplinar administrativo para função legislativa, judicial ou penal.

**Como pensar:** mantenha a resposta dentro da jurisdição profissional e dos limites legais do conselho.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.6

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Senado e Tribunal de Contas não são órgãos regimentais internos do CRA-PR.
- **B)** Incorreta. Ministério Público e assembleia legislativa são instituições externas ao rol.
- **C)** Correta. Plenário, Diretoria, Ouvidoria, comissões e órgãos de representação integram a estrutura estudada.
- **D)** Incorreta. Poder Judiciário e conselho municipal não compõem a organização regimental indicada.

**Conceito:** órgãos e estruturas do CRA-PR.

**Pegadinha:** inserir instituições públicas conhecidas em uma lista majoritariamente correta.

**Como pensar:** verifique se cada elemento pertence internamente ao conselho; um único intruso invalida o conjunto.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.7

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O Plenário possui competência deliberativa e participa de julgamentos.
- **B)** Incorreta. Não é mero consultor externo subordinado à Diretoria.
- **C)** Incorreta. Trata-se de órgão do CRA-PR, não instância nacional de todos os regionais.
- **D)** Correta. A definição reúne deliberação superior colegiada e primeira instância de julgamento regional.

**Conceito:** posição regimental do Plenário.

**Pegadinha:** trocar primeira instância regional por instância recursal nacional.

**Como pensar:** associe Plenário a colegialidade, deliberação superior e julgamento inicial na jurisdição.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.8

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Ouvidoria não substitui a Diretoria nem exerce caráter executivo.
- **B)** Correta. Sua natureza é mediadora, sem função administrativa, executiva, deliberativa ou decisória.
- **C)** Incorreta. Primeira instância de julgamento é atribuída ao Plenário, não à Ouvidoria.
- **D)** Incorreta. A formulação de diretrizes nacionais pertence ao âmbito do CFA.

**Conceito:** natureza e limites da Ouvidoria.

**Pegadinha:** confundir acolhimento e mediação com poder de decidir ou aplicar penalidade.

**Como pensar:** visualize a Ouvidoria como canal mediador, não como órgão de comando ou julgamento.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.9

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O Código alcança profissionais e pessoas jurídicas registradas, respeitando as particularidades destas.
- **B)** Incorreta. Pessoa jurídica não fica fora do Código por não ser pessoa natural.
- **C)** Incorreta. O alcance não é indiscriminado para qualquer empresa sem relação com o sistema.
- **D)** Incorreta. A norma não se restringe a conselheiros em mandato.

**Conceito:** sujeitos alcançados pelo Código de Ética.

**Pegadinha:** deduzir da inaplicabilidade de algumas sanções que a pessoa jurídica está integralmente excluída.

**Como pensar:** separe incidência do Código de compatibilidade de cada penalidade com a natureza do sujeito.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.10

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Publicidade irrestrita pode violar sigilo, e dependência técnica contraria a independência profissional.
- **B)** Incorreta. Empréstimo de registro e obstrução da fiscalização são condutas incompatíveis.
- **C)** Incorreta. Assinar sem supervisão, divulgar sigilo e agir sem urbanidade contrariam deveres estudados.
- **D)** Correta. Zelo, honestidade, independência, aperfeiçoamento e colaboração integram o núcleo dos deveres.

**Conceito:** deveres éticos dos profissionais de Administração.

**Pegadinha:** misturar um dever verdadeiro com comportamentos irregulares na mesma alternativa.

**Como pensar:** valide cada item da lista; em questão conjuntiva, um único comportamento vedado elimina a opção.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O sigilo alcança informação conhecida no exercício profissional lícito, sem afastar hipóteses juridicamente justificadas.
- **B)** Incorreta. O dever não depende apenas da forma escrita nem cessa automaticamente com o contrato.
- **C)** Incorreta. Vantagem própria não constitui autorização para divulgar informação protegida.
- **D)** Incorreta. Sigilo não impede, em termos absolutos, o cumprimento de obrigação legal válida.

**Conceito:** dever de sigilo profissional.

**Pegadinha:** transformar o dever em regra sem qualquer ressalva ou, no extremo oposto, liberá-lo por conveniência.

**Como pensar:** identifique a origem profissional da informação e procure justa causa ou fundamento jurídico para eventual revelação.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.12

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Experiência do terceiro não substitui orientação ou supervisão efetiva de quem assina.
- **B)** Incorreta. Continuidade contratual não cria dever de chancelar trabalho não supervisionado.
- **C)** Correta. A assinatura nessas condições constitui risco ético expressamente destacado na revisão.
- **D)** Incorreta. A conduta pode ultrapassar a relação contratual e repercutir no sistema profissional.

**Conceito:** responsabilidade por documento assinado.

**Pegadinha:** avaliar apenas a autoria material ou a qualidade do texto e ignorar a responsabilidade assumida pela assinatura.

**Como pensar:** pergunte se houve participação técnica suficiente para que o profissional responda pelo documento.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.13

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Prisão e perda de função pública não integram o rol ético apresentado.
- **B)** Incorreta. Inverte publicidade e reserva e inclui medidas não previstas no conjunto.
- **C)** Incorreta. As denominações e as espécies indicadas não reproduzem o Código.
- **D)** Correta. A alternativa enumera advertência reservada, censura pública, suspensão e cancelamento profissional.

**Conceito:** espécies de sanção ética.

**Pegadinha:** trocar os qualificadores “reservada” e “pública” ou inserir sanção penal no rol administrativo.

**Como pensar:** memorize os quatro degraus pelo nome completo, sem misturar multa como se fosse uma quinta espécie isolada.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.14

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Pessoa jurídica registrada pode ser alcançada pelo Código e pelas medidas compatíveis.
- **B)** Incorreta. Suspensão do exercício profissional não se aplica à pessoa jurídica.
- **C)** Correta. A opção combina a exceção de suspensão e cancelamento com a permanência das demais consequências cabíveis.
- **D)** Incorreta. Não há cancelamento automático sem processo como única resposta possível.

**Conceito:** aplicação de sanções à pessoa jurídica.

**Pegadinha:** concluir “nenhuma sanção” a partir de “suspensão e cancelamento não se aplicam”.

**Como pensar:** faça duas listas: sanções incompatíveis com pessoa jurídica e sanções que continuam possíveis.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.15

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Percepção de gravidade não elimina enquadramento, motivação e processo.
- **B)** Incorreta. A revisão prevê sanções disciplinares acompanhadas da multa nas condições normativas.
- **C)** Incorreta. Ausência de prejuízo financeiro não torna irrelevante qualquer violação ética.
- **D)** Correta. Enquadramento, procedimento e disciplina da multa devem ser observados em conjunto.

**Conceito:** aplicação processual e pecuniária das sanções.

**Pegadinha:** escolher a penalidade por intuição ou tratar a multa como substituta automática do regime disciplinar.

**Como pensar:** percorra fato, norma, enquadramento, processo e consequência, nessa ordem.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.16

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O comando pede a falsa, não a primeira afirmação verdadeira encontrada.
- **B)** Correta. “INCORRETA” inverte o critério e exige localizar a opção que foge à regra.
- **C)** Incorreta. Ignorar a palavra negativa leva a responder ao comando oposto.
- **D)** Incorreta. Abrangência não compensa extrapolação nem descumprimento do enunciado.

**Conceito:** leitura de comando negativo.

**Pegadinha:** aqui a alternativa correta explica como procurar a incorreta; o próprio item não pede que se marque uma afirmação materialmente falsa.

**Como pensar:** circule a palavra negativa e reescreva: “qual opção é a exceção”.

**Referência:** [Revisão fixa de Português e interpretação — Comando da questão](semana_02_estudo.md#s2-d1-revisao-comando).

#### Comentário Extra Dia 1.17

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O trecho afirma benefício contra interferência, mas conserva a exigência de componentes compatíveis.
- **B)** Incorreta. Não há comparação universal de velocidade entre todas as instalações.
- **C)** Incorreta. A exigência de componentes compatíveis contradiz a ideia de dispensa.
- **D)** Incorreta. O texto não autoriza concluir menor custo pela ausência de interferência.

**Conceito:** inferência autorizada e extrapolação.

**Pegadinha:** acrescentar preço, superioridade universal ou garantia que não aparecem no trecho.

**Como pensar:** aceite somente a conclusão que pode ser sustentada por palavras expressas ou relação necessária entre elas.

**Referência:** [Revisão fixa de Português e interpretação — Inferência x extrapolação](semana_02_estudo.md#s2-d1-revisao-inferencia).

#### Comentário Extra Dia 1.18

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. “Contudo” não apresenta motivo para a primeira oração.
- **B)** Correta. O conector introduz ressalva ou oposição ao efeito positivo antes mencionado.
- **C)** Incorreta. Conclusão seria marcada por conectores como “portanto” ou “logo”.
- **D)** Incorreta. Não há requisito condicional introduzido pelo conector.

**Conceito:** relação semântica de conectores.

**Pegadinha:** ler a segunda oração como consequência, quando ela limita a expectativa criada pela primeira.

**Como pensar:** substitua mentalmente por “porém”; se o sentido permanecer, a relação é adversativa.

**Referência:** [Revisão fixa de Português e interpretação — Conectores](semana_02_estudo.md#s2-d1-revisao-conectores).

#### Comentário Extra Dia 1.19

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Termos absolutos aumentam o compromisso lógico, mas podem ser verdadeiros quando a regra sustenta todo o alcance.
- **B)** Incorreta. Não existe proibição automática de palavras universais em alternativas.
- **C)** Incorreta. Ignorá-las altera o alcance e pode inverter o julgamento da frase.
- **D)** Incorreta. “Sempre” e “todos” não desempenham a função conclusiva de “portanto”.

**Conceito:** efeito lógico de palavras absolutas.

**Pegadinha:** adotar a heurística simplista de que todo absoluto é falso.

**Como pensar:** procure uma única exceção; se ela existir, a formulação universal cai, mas sem exceção a palavra pode estar correta.

**Referência:** [Revisão fixa de Português e interpretação — Palavras absolutas](semana_02_estudo.md#s2-d1-revisao-absolutas).

#### Comentário Extra Dia 1.20

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Reduzir colisões entre segmentos não implica bloquear broadcast na mesma VLAN.
- **B)** Incorreta. Colisão e broadcast possuem definições e alcances distintos.
- **C)** Correta. O trecho contrasta segmentação de colisões com manutenção do domínio de broadcast.
- **D)** Incorreta. “Contudo” introduz ressalva e o texto não atribui roteamento ao switch.

**Conceito:** interpretação integrada de uma ressalva técnica.

**Pegadinha:** apagar a oposição marcada pelo conector e fundir dois efeitos de rede diferentes.

**Como pensar:** divida o período antes e depois de “contudo”; preserve as duas afirmações sem transformar uma em causa da outra.

**Referência:** [Revisão fixa de Português e interpretação — Prática breve de interpretação](semana_02_estudo.md#s2-d1-revisao-pratica-interpretacao).


---
# Dia 2 — Modelos OSI e TCP/IP, endereçamento e CIDR

Base usada: `semana_02/semana_02_estudo.md`, seção `# Dia 2 - Modelos OSI e TCP/IP, endereçamento e CIDR`.

## Questões principais

### Questão 1

Da camada mais próxima do usuário para a camada responsável pela transmissão de sinais, a ordem correta das sete camadas do modelo OSI é:

A) Aplicação, Sessão, Apresentação, Rede, Transporte, Física e Enlace.
B) Aplicação, Apresentação, Transporte, Sessão, Rede, Física e Enlace.
C) Física, Enlace, Rede, Transporte, Sessão, Apresentação e Aplicação.
D) Aplicação, Apresentação, Sessão, Transporte, Rede, Enlace e Física.

### Questão 2

No modelo OSI, tradução de formatos, codificação, compressão e criptografia, em sentido funcional, são responsabilidades didaticamente associadas à camada de:

A) apresentação.
B) sessão.
C) transporte.
D) rede.

### Questão 3

Analise as afirmativas sobre as camadas do modelo OSI.

I. A camada de transporte oferece comunicação fim a fim entre processos e pode empregar portas.
II. A camada de rede trata do endereçamento lógico e do encaminhamento entre redes.
III. A camada de rede garante, por si própria, confirmação e retransmissão fim a fim para todo pacote IP.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I, II e III.
D) I e II, apenas.

### Questão 4

Um repetidor recebe sinais em uma interface e os regenera em outra, sem examinar endereços. No modelo OSI, essa atuação pertence à camada física porque ela:

A) seleciona rotas com base no endereço IP de destino.
B) organiza quadros e aprende endereços MAC de origem.
C) estabelece sessões e pontos de sincronização entre aplicações.
D) representa bits por sinais e não interpreta endereços MAC ou IP.

### Questão 5

Na comparação didática entre o OSI e o modelo TCP/IP de quatro camadas, assinale a alternativa correta.

A) As camadas de transporte e rede do OSI são reunidas na camada Internet do TCP/IP.
B) Aplicação, apresentação e sessão do OSI correspondem à camada de aplicação do TCP/IP.
C) A camada de enlace do OSI corresponde à camada de transporte do TCP/IP.
D) Física e enlace permanecem obrigatoriamente separadas no modelo TCP/IP de quatro camadas.

### Questão 6

Alguns livros apresentam a arquitetura TCP/IP em cinco camadas, separando física e enlace, enquanto outros a apresentam em quatro. Essa diferença significa que:

A) a versão de cinco camadas abandona os protocolos IP, TCP e UDP.
B) o modelo de quatro camadas não contempla meios físicos nem redes locais.
C) a suíte permanece a mesma; muda a forma pedagógica de agrupar as funções.
D) a versão de cinco camadas passa a ter correspondência perfeita com as sete camadas do OSI.

### Questão 7

Em uma comunicação que usa TCP, IP e Ethernet, qual sequência representa corretamente o encapsulamento no emissor?

A) Dados → pacote IP → segmento TCP → quadro Ethernet → bits.
B) Dados → segmento TCP → pacote IP → quadro Ethernet → bits.
C) Dados → quadro Ethernet → pacote IP → segmento TCP → bits.
D) Dados → segmento TCP → quadro Ethernet → pacote IP → bits.

### Questão 8

No receptor de uma comunicação Ethernet, IPv4 e TCP, o desencapsulamento ocorre, de forma simplificada, na seguinte ordem:

A) bits → segmento TCP → quadro Ethernet → pacote IPv4 → dados.
B) bits → quadro Ethernet → pacote IPv4 → segmento TCP → dados.
C) quadro Ethernet → bits → segmento TCP → pacote IPv4 → dados.
D) pacote IPv4 → quadro Ethernet → bits → dados → segmento TCP.

### Questão 9

Uma estação envia um pacote IPv4 a um servidor remoto por meio de dois roteadores, sem NAT. Durante o percurso:

A) os endereços MAC são adequados a cada enlace, os endereços IP normalmente permanecem de ponta a ponta e o TTL pode ser alterado.
B) o endereço MAC do servidor permanece como destino de todos os quadros, e os roteadores substituem o IP de destino a cada salto.
C) os endereços IP mudam em todo roteador, enquanto os endereços MAC permanecem inalterados até o servidor.
D) endereços MAC e IP permanecem necessariamente idênticos, pois ambos identificam o destino final.

### Questão 10

Assinale a associação correta entre protocolo ou camada e sua PDU didática.

A) TCP — quadro; IP — segmento; Ethernet — pacote; física — dados.
B) TCP — segmento; IP — pacote ou datagrama; Ethernet — quadro; física — bits.
C) TCP — pacote; IP — quadro; Ethernet — datagrama UDP; física — segmento.
D) TCP — bits; IP — dados; Ethernet — segmento; física — pacote.

### Questão 11

Sobre as expressões “datagrama UDP” e “datagrama IP”, assinale a alternativa correta.

A) São sinônimos, pois UDP e IP pertencem à mesma camada.
B) Datagrama UDP é uma PDU de enlace, enquanto datagrama IP é uma PDU física.
C) Datagrama IP fica encapsulado no datagrama UDP durante o envio.
D) Datagrama UDP é unidade de transporte e pode ser encapsulado em um datagrama IP, da camada Internet.

### Questão 12

Em relação aos endereços MAC usados em redes IEEE 802, assinale a alternativa correta.

A) Identificam processos de aplicação e são representados por números de porta de 16 bits.
B) Permanecem como origem e destino em todos os enlaces atravessados por um pacote, mesmo após roteamento.
C) Endereços de 48 bits, escritos em seis octetos hexadecimais, são comuns, mas podem ser localmente administrados ou mutáveis.
D) Substituem o endereço IP porque são necessariamente globais, únicos e imutáveis.

### Questão 13

Um switch recebe, pela porta 5, um quadro cujo MAC de origem ainda não consta em sua tabela. A ação de aprendizagem consiste em registrar:

A) o MAC de destino associado à porta 5, independentemente do local do destino.
B) o endereço IP de origem associado à rota padrão do switch.
C) o MAC de origem associado à porta 5.
D) os números de porta TCP de origem e destino associados ao MAC do gateway.

### Questão 14

Um endereço IPv4 possui:

A) 48 bits, divididos obrigatoriamente em 24 bits de rede e 24 de host.
B) 32 bits, e o prefixo informa quantos bits iniciais pertencem à parte de rede.
C) 64 bits, dos quais os quatro primeiros octetos identificam a rede.
D) 128 bits, representados por oito grupos hexadecimais.

### Questão 15

A máscara IPv4 `255.255.252.0` corresponde ao prefixo:

A) `/20`.
B) `/21`.
C) `/22`.
D) `/23`.

### Questão 16

Qual máscara decimal pontuada corresponde ao prefixo IPv4 `/20`?

A) `255.255.224.0`.
B) `255.255.248.0`.
C) `255.255.255.240`.
D) `255.255.240.0`.

### Questão 17

Assinale a sequência que NÃO representa uma máscara CIDR IPv4 normal, pois contém bits `1` não contíguos.

A) `255.255.255.192`.
B) `255.255.254.0`.
C) `255.248.0.0`.
D) `255.255.240.128`.

### Questão 18

Para o host `192.168.40.158/26`, os endereços de rede e de broadcast dirigido da sub-rede são, respectivamente:

A) `192.168.40.128` e `192.168.40.191`.
B) `192.168.40.128` e `192.168.40.190`.
C) `192.168.40.64` e `192.168.40.191`.
D) `192.168.40.152` e `192.168.40.159`.

### Questão 19

O endereço `10.12.7.222/27` pertence a uma sub-rede cuja faixa convencional de hosts válidos é:

A) `10.12.7.192` a `10.12.7.223`.
B) `10.12.7.193` a `10.12.7.222`.
C) `10.12.7.193` a `10.12.7.223`.
D) `10.12.7.201` a `10.12.7.230`.

### Questão 20

Considere o endereço `172.20.173.44/20`. Os endereços de rede e de broadcast dirigido são:

A) `172.20.160.0` e `172.20.175.255`.
B) `172.20.168.0` e `172.20.175.255`.
C) `172.20.173.0` e `172.20.173.255`.
D) `172.20.160.0` e `172.20.191.255`.

### Questão 21

Quantos endereços IPv4 de host são convencionalmente utilizáveis em uma sub-rede `/28`?

A) 8.
B) 12.
C) 14.
D) 16.

### Questão 22

O bloco `10.0.0.10/31` é empregado em um enlace IPv4 ponto a ponto compatível com a RFC 3021. Nesse contexto:

A) apenas `10.0.0.10` pode ser usado, porque `10.0.0.11` é sempre broadcast.
B) nenhum dos endereços pode ser usado, pois a fórmula `2^h - 2` resulta em zero.
C) `10.0.0.10` e `10.0.0.11` podem representar as duas extremidades do enlace.
D) o prefixo deve ser interpretado como uma rota para um único host.

### Questão 23

Em IPv4, o prefixo `/32`:

A) identifica exatamente um endereço ou uma rota de host, sem faixa convencional de hosts e broadcast de sub-rede.
B) reserva dois endereços utilizáveis para as extremidades de um enlace ponto a ponto.
C) equivale à máscara `255.255.255.254`.
D) fornece um endereço de rede, um broadcast e 254 hosts utilizáveis.

### Questão 24

Qual dos endereços abaixo pertence a um bloco privado definido pela RFC 1918?

A) `172.15.200.1`.
B) `172.32.0.10`.
C) `192.169.10.20`.
D) `172.31.200.5`.

### Questão 25

Sobre endereços de loopback, assinale a alternativa correta.

A) O IPv4 reserva `127.0.0.0/8`, e o IPv6 usa `::1/128`.
B) Apenas `127.0.0.1` é loopback; os demais endereços `127/8` são públicos.
C) Loopback identifica o gateway padrão que encaminha pacotes para a Internet.
D) O IPv6 utiliza `fe80::1` como seu único endereço de loopback.

### Questão 26

Um computador Windows configurado para DHCP atribuiu a si próprio `169.254.20.8/16` porque o servidor não respondeu. Essa configuração:

A) é loopback e permite testar apenas a pilha interna do próprio host.
B) pertence à RFC 1918 e, por isso, recebe automaticamente uma rota para a Internet.
C) é um endereço público provisório fornecido pela IANA.
D) é link-local/APIPA, está na faixa selecionável `169.254.1.0` a `169.254.254.255` com `/16`, pode permitir comunicação no enlace e costuma indicar falha de DHCP.

### Questão 27

Um analista concluiu que todo IPv4 fora dos três blocos privados da RFC 1918 é necessariamente unicast público utilizável na Internet. Assinale a avaliação correta.

A) A conclusão está correta, pois somente endereços privados têm finalidade especial.
B) A conclusão está correta, desde que o endereço não termine em `.0` ou `.255`.
C) A conclusão está incorreta: também existem blocos de loopback, link-local, documentação, multicast e outras finalidades especiais.
D) A conclusão está incorreta apenas para endereços IPv4 com prefixo maior que `/24`.

### Questão 28

Ao dividir integralmente `192.168.50.0/24` em sub-redes `/27` iguais, obtêm-se:

A) 8 sub-redes, cada uma com 32 endereços e 30 hosts convencionais.
B) 4 sub-redes, cada uma com 64 endereços e 62 hosts convencionais.
C) 8 sub-redes, cada uma com 30 endereços e 28 hosts convencionais.
D) 16 sub-redes, cada uma com 16 endereços e 14 hosts convencionais.

### Questão 29

Considere A=`192.168.10.250/23`, B=`192.168.11.200/23` e C=`192.168.12.1/23`. Analise as afirmativas.

I. A e B pertencem à mesma sub-rede.
II. A rede de A e B é `192.168.10.0/23`, com broadcast `192.168.11.255`.
III. C pertence à mesma sub-rede de A e B, porque `/23` abrange dois valores consecutivos do terceiro octeto.

Está correto o que se afirma em:

A) I, apenas.
B) I e II, apenas.
C) II e III, apenas.
D) I, II e III.

### Questão 30

Qual bloco `/26` contém o endereço `203.0.113.205`?

A) `203.0.113.128/26`.
B) `203.0.113.192/26`.
C) `203.0.113.200/26`.
D) `203.0.113.205/26`.

### Questão 31

Um host usa `192.168.70.78/27`. Sem mecanismos adicionais, qual endereço pode ser configurado como gateway válido e diretamente alcançável nessa sub-rede?

A) `192.168.70.64`.
B) `192.168.70.95`.
C) `192.168.70.97`.
D) `192.168.70.94`.

### Questão 32

Uma estação IPv4 Ethernet precisa enviar um pacote a um servidor fora de sua sub-rede e possui uma rota padrão válida. No primeiro enlace:

A) o endereço IP de destino passa a ser o do gateway, e o MAC de destino continua sendo o do servidor remoto.
B) o pacote conserva o IP do servidor como destino, enquanto o quadro usa o MAC do gateway ou próximo salto.
C) o quadro é enviado sem MAC de destino, pois o roteador toma a decisão apenas com a porta TCP.
D) a estação descobre por ARP o MAC do servidor remoto através de todos os roteadores.

### Questão 33

Dois hosts IPv4 estão no mesmo enlace Ethernet e o emissor não possui a associação do destino no cache ARP. Em condições normais, ele:

A) transmite um ARP Request em broadcast de camada 2, e o proprietário do IPv4 responde normalmente por unicast com seu MAC.
B) envia uma consulta ARP por TCP ao servidor DNS e recebe o endereço IP do destino.
C) encaminha o pedido ao roteador, pois mensagens ARP não circulam no enlace local.
D) envia um ICMP Echo Request para descobrir a porta física do switch.

### Questão 34

O host `192.168.10.20/24` enviará dados a `198.51.100.10` usando o gateway `192.168.10.1`. Nessa situação, o ARP do host procura:

A) o MAC de `198.51.100.10`, propagando a consulta por todos os roteadores.
B) a porta TCP do gateway, pois ARP relaciona IPv4 e serviço de transporte.
C) o endereço IPv6 equivalente ao servidor remoto.
D) o MAC de `192.168.10.1`, que é o próximo salto no enlace local.

### Questão 35

Sobre o ICMP, assinale a alternativa INCORRETA.

A) O ICMP usa uma porta TCP ou UDP própria, que precisa ser descoberta antes do envio de cada mensagem.
B) Echo Request e Echo Reply podem ser empregados pelo comando `ping`.
C) Time Exceeded e Destination Unreachable são exemplos de mensagens de controle ou erro.
D) Filtrar indiscriminadamente todo ICMP pode prejudicar diagnóstico e funções da rede.

### Questão 36

No IPv6, o Neighbor Discovery:

A) usa o ARP tradicional e transmite toda solicitação ao broadcast IPv6.
B) limita-se a converter nomes DNS em endereços IPv6.
C) funciona sobre TCP e emprega portas para Neighbor Solicitation e Neighbor Advertisement.
D) integra o ICMPv6, usa mensagens como NS e NA e também apoia descoberta e manutenção de vizinhança.

### Questão 37

Qual é a abreviação válida de `2001:0db8:0000:0000:0000:ff00:0042:8329`?

A) `2001::db8::ff00:42:8329`.
B) `2001:db8:0:0:ff00::42:8329`.
C) `2001:db8::ff00:42:8329`.
D) `2001:db8:ff00:42:8329::`.

### Questão 38

Em relação ao broadcast no IPv6, assinale a alternativa correta.

A) O IPv6 não possui endereço de broadcast; a entrega em grupo pode usar multicast.
B) `ff02::1` é o endereço de broadcast global de todos os dispositivos IPv6.
C) Todo prefixo IPv6 reserva o último endereço para broadcast dirigido.
D) O broadcast IPv6 existe apenas em sub-redes com prefixo `/64`.

### Questão 39

Assinale a alternativa que descreve corretamente tipos de endereço IPv6.

A) Unicast entrega obrigatoriamente a todos os nós, enquanto multicast entrega a uma única interface.
B) Anycast identifica um grupo e entrega uma cópia a todas as interfaces que possuem o endereço.
C) Unicast identifica uma interface; multicast, um grupo; anycast pode ser atribuído a várias interfaces e ser entregue a uma delas.
D) Multicast e broadcast são nomes equivalentes no IPv6.

### Questão 40

Qual é o prefixo de rede do endereço `2001:db8:abcd:12ef:1234:5678:9abc:def0/64`?

A) `2001:db8:abcd::/64`.
B) `2001:db8:abcd:1200::/64`.
C) `2001:db8:abcd:12ef::/64`.
D) `2001:db8:abcd:12ef:1234::/64`.

### Questão 41

Sobre blocos especiais do IPv6, assinale a alternativa correta.

A) `fe80::/10` é unicast link-local, `::1/128` é loopback e `2001:db8::/32` é reservado para documentação.
B) `fc00::/7` é link-local, equivale a `fe80::/10` e nunca pode ser roteado entre sites.
C) `::/128` identifica todos os roteadores do enlace.
D) `2001:db8::/32` é a faixa obrigatória de endereços públicos de produção.

### Questão 42

Analise as afirmativas sobre multicast e descoberta de vizinhos no IPv6.

I. `ff02::1` identifica todos os nós IPv6 do enlace, mas é multicast, não broadcast.
II. Na resolução inicial, uma NS é enviada ao multicast solicited-node derivado do endereço-alvo, em vez de consultar indiscriminadamente `ff02::1`.
III. Roteadores não devem encaminhar tráfego de escopo link-local para além do enlace.

Está correto o que se afirma em:

A) I, apenas.
B) I, II e III.
C) II e III, apenas.
D) I e III, apenas.

### Questão 43

Uma rede `192.168.8.0/24` deve ser dividida em sub-redes iguais, buscando a maior quantidade possível de sub-redes, com pelo menos 50 hosts convencionais em cada uma. Qual solução atende ao requisito?

A) Usar `/26`, obtendo 4 sub-redes com 62 hosts convencionais em cada uma.
B) Usar `/27`, obtendo 8 sub-redes com 62 hosts convencionais em cada uma.
C) Usar `/25`, obtendo 4 sub-redes com 126 hosts convencionais em cada uma.
D) Usar `/28`, obtendo 16 sub-redes com 50 hosts convencionais em cada uma.

### Questão 44

No bloco `10.0.0.0/24`, já foram alocados `10.0.0.0/26` e `10.0.0.128/27`. Qual prefixo adicional `/27` está corretamente alinhado e não se sobrepõe aos blocos existentes?

A) `10.0.0.32/27`.
B) `10.0.0.64/27`.
C) `10.0.0.128/27`.
D) `10.0.0.144/27`.

### Questão 45

O host A usa `192.168.1.10/24`, e o host B usa `192.168.1.200/25`. Considerando a decisão local de cada host e desconsiderando mecanismos adicionais, assinale a alternativa correta.

A) Ambos consideram o outro local, pois os três primeiros octetos coincidem.
B) Ambos consideram o outro remoto, pois os prefixos configurados são diferentes.
C) A considera B local, mas B considera A remoto, o que pode produzir alcance assimétrico.
D) B considera A local, mas A considera B remoto, porque `/25` abrange mais endereços que `/24`.

### Questão 46

Para o endereço `10.34.173.205/21`, assinale a alternativa que apresenta rede, broadcast dirigido e quantidade convencional de hosts utilizáveis.

A) `10.34.168.0`, `10.34.175.255` e 2046 hosts.
B) `10.34.172.0`, `10.34.175.255` e 1022 hosts.
C) `10.34.168.0`, `10.34.183.255` e 4094 hosts.
D) `10.34.173.0`, `10.34.173.255` e 254 hosts.

### Questão 47

A rede `192.168.60.0/24` foi dividida integralmente em sub-redes `/28`. Contando `192.168.60.0/28` como a primeira, quais são rede, broadcast e faixa de hosts da décima sub-rede?

A) Rede `.128`, broadcast `.143`, hosts `.129` a `.142`.
B) Rede `.144`, broadcast `.159`, hosts `.145` a `.158`.
C) Rede `.160`, broadcast `.175`, hosts `.161` a `.174`.
D) Rede `.144`, broadcast `.160`, hosts `.145` a `.159`.

### Questão 48

Analise as afirmativas sobre prefixos e exceções de endereçamento.

I. Em enlace IPv4 ponto a ponto compatível com a RFC 3021, os dois endereços de um `/31` podem representar as extremidades.
II. Um `/32` IPv4 representa um único endereço ou rota de host, sem intervalo convencional de hosts.
III. Como o IPv6 não possui broadcast, não se deve aplicar automaticamente a ele a fórmula IPv4 `2^h - 2`.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I e II, apenas.
D) I, II e III.

### Questão 49

Um host envia a um servidor remoto um pacote IPv4 com TTL igual a 1. Ao processá-lo, o primeiro roteador reduz esse campo a zero. Assinale a consequência compatível com o funcionamento do IP e do ICMP.

A) O roteador encaminha o pacote e envia ICMP Echo Reply ao destino, pois o TTL só é validado pelo servidor final.
B) O roteador descarta o pacote e pode enviar ICMP Time Exceeded à origem; a mensagem não usa porta TCP/UDP nem torna o IP confiável.
C) O roteador retransmite o pacote original de forma confiável depois de abrir uma conexão TCP com a origem.
D) O roteador converte o pacote em ARP Request e o difunde pelos enlaces restantes até localizar o servidor.

### Questão 50

Analise as afirmativas.

I. Um roteador normalmente remove o quadro recebido, examina o pacote IP e cria outro quadro para o enlace seguinte.
II. IPv4, IPv6 e ICMP associam-se à camada de rede/Internet, enquanto ARP atua no enlace local e não usa porta TCP ou UDP.
III. No TCP/IP de quatro camadas, funções das camadas OSI de aplicação, apresentação e sessão são agrupadas na camada de aplicação, sem correspondência necessariamente perfeita.

Está correto o que se afirma em:

A) I e II, apenas.
B) II e III, apenas.
C) I, II e III.
D) III, apenas.

## Questões extras de revisão fixa do Dia 2

#### Extra Dia 2.1

Um gestor decide ignorar requisito legal porque acredita que o procedimento alternativo será mais rápido e econômico. À luz dos princípios do art. 37, assinale a alternativa correta.

A) A eficiência autoriza afastar a legalidade sempre que houver redução de custos.
B) A busca de eficiência não permite descumprir o ordenamento nem atuar fora da competência atribuída.
C) A conduta é válida se receber publicidade depois de praticada, ainda que permaneça contrária à lei.
D) A legalidade vincula apenas particulares, enquanto a Administração atua por liberdade geral.

#### Extra Dia 2.2

Uma autoridade utiliza campanha institucional para destacar seu nome, imagem e realizações pessoais. O princípio mais diretamente comprometido é o da:

A) impessoalidade, pois a comunicação pública não deve servir à promoção pessoal do agente.
B) eficiência, porque toda publicidade institucional reduz necessariamente a qualidade do serviço.
C) legalidade, exclusivamente porque o agente se identificou perante os cidadãos.
D) moralidade, entendida apenas como opinião subjetiva sobre o comportamento da autoridade.

#### Extra Dia 2.3

Sobre publicidade administrativa e proteção de dados pessoais, assinale a alternativa correta.

A) A publicidade exige divulgação irrestrita de qualquer dado mantido pelo Poder Público.
B) Transparência é a regra, mas convive com sigilo legal, finalidade, necessidade e proteção de dados pessoais.
C) A LGPD transforma automaticamente toda informação pública em informação sigilosa.
D) A LAI deixa de produzir efeitos sempre que um documento contém qualquer dado pessoal.

#### Extra Dia 2.4

Assinale a alternativa que diferencia corretamente órgão e entidade e classifica o CRA-PR.

A) Órgão e entidade possuem personalidade jurídica própria; o CRA-PR é órgão da Administração Direta.
B) Órgão é pessoa jurídica autônoma; entidade é centro de competências sem personalidade própria.
C) Órgão não possui personalidade jurídica própria; entidade possui, e o CRA-PR é autarquia da Administração Indireta.
D) O CRA-PR é associação privada, pois conselhos profissionais não integram a Administração Pública.

#### Extra Dia 2.5

Na revisão estudada, autarquia é definida como:

A) pessoa jurídica de direito público criada por lei para desempenhar atividade administrativa típica.
B) órgão sem personalidade jurídica criado por ato interno para explorar atividade econômica.
C) sociedade privada formada livremente por agentes públicos e sem vínculo com a Administração Indireta.
D) modalidade de empresa pública que deve possuir capital privado majoritário.

#### Extra Dia 2.6

Servidor sem atribuição legal para decidir determinado processo pratica o ato mesmo assim. O elemento do ato administrativo diretamente afetado é:

A) o objeto, porque todo problema de autoria altera apenas o efeito jurídico produzido.
B) a forma, pois competência indica somente o modo pelo qual o ato se exterioriza.
C) a competência, que responde à pergunta sobre quem pode praticar o ato.
D) o motivo, que se confunde com a identidade funcional do agente responsável.

#### Extra Dia 2.7

Sobre os atributos do ato administrativo, assinale a alternativa correta.

A) A presunção de legitimidade e veracidade é relativa, e a autoexecutoriedade existe apenas quando admitida por lei ou por situação urgente.
B) A presunção de legitimidade impede qualquer contestação administrativa ou judicial.
C) A imperatividade está presente em todo ato e exige concordância prévia do destinatário.
D) A autoexecutoriedade permite execução direta de qualquer ato, independentemente de previsão ou urgência.

#### Extra Dia 2.8

A Administração identifica dois atos: o primeiro é ilegal; o segundo é válido, mas deixou de ser conveniente. A providência adequada, quanto à retirada de cada ato, é:

A) revogar ambos, porque ilegalidade e inconveniência são questões de mérito.
B) anular ambos, pois todo ato inconveniente passa a ser ilegal.
C) convalidar necessariamente o primeiro e anular o segundo.
D) anular o primeiro e, respeitados os direitos adquiridos, revogar o segundo.

#### Extra Dia 2.9

A convalidação de ato administrativo é cabível, segundo o núcleo revisado, quando:

A) o ato é válido, mas a Administração prefere substituí-lo por solução mais conveniente.
B) há vício sanável e a correção não causa lesão ao interesse público nem prejuízo a terceiros.
C) qualquer ilegalidade é constatada, inclusive vício insanável, independentemente de consequências.
D) ocorreu má-fé do destinatário e já transcorreu o prazo de cinco anos.

#### Extra Dia 2.10

No âmbito da Lei nº 9.784/1999, sobre a anulação de atos que geraram efeitos favoráveis aos destinatários, assinale a alternativa correta.

A) O direito de anular nunca sofre limite temporal quando existe qualquer vício.
B) O prazo é sempre contado do último pagamento, inclusive em efeitos patrimoniais contínuos.
C) A decadência ocorre em dois anos e não admite consideração da má-fé.
D) Em regra, o prazo é de cinco anos desde o ato; em efeitos patrimoniais contínuos, conta-se do primeiro pagamento, ressalvada comprovada má-fé.

#### Extra Dia 2.11

Quanto à relação entre LAI e LGPD, assinale a alternativa correta.

A) A LAI revoga a proteção de dados sempre que a informação estiver em documento público.
B) A LGPD impede o Poder Público de tratar dados pessoais para finalidade pública.
C) As duas leis convivem: acesso à informação não autoriza exposição irrestrita, e proteção de dados não cria sigilo automático.
D) A aplicação de uma delas exclui necessariamente a outra no mesmo caso concreto.

#### Extra Dia 2.12

Um agente comete irregularidade formal, mas não há demonstração de dolo nem enquadramento nas condutas tipificadas. Com base na revisão sobre improbidade, é correto afirmar que:

A) simples ilegalidade ou voluntariedade não basta; são necessários dolo e enquadramento legal nos termos da lei.
B) toda irregularidade administrativa configura automaticamente ato de improbidade contra princípios.
C) a ausência de dano ao erário torna impossível qualquer espécie de improbidade, ainda que exista outro tipo legal doloso.
D) culpa leve e resultado inconveniente bastam, sem necessidade de conduta tipificada.

#### Extra Dia 2.13

Uma contratação possui fornecedor exclusivo comprovado e competição inviável. Considerando apenas o núcleo estudado, a situação pode caracterizar:

A) dispensa, porque toda contratação direta pressupõe competição inviável.
B) pregão, pois fornecedor exclusivo é critério de julgamento dessa modalidade.
C) revogação da licitação, que elimina a necessidade de processo e motivação.
D) inexigibilidade, desde que observados os requisitos legais aplicáveis.

#### Extra Dia 2.14

Sobre licitação e contratação direta, assinale a alternativa correta.

A) Dispensa e inexigibilidade eliminam processo, motivação, justificativa e controle.
B) Critério de julgamento e modalidade são expressões equivalentes na Lei nº 14.133/2021.
C) Contratação direta continua sujeita a processo e controle; pregão e diálogo competitivo estão entre as modalidades estudadas.
D) Concurso e leilão não são modalidades, pois se aplicam apenas a relações privadas.

#### Extra Dia 2.15

Na responsabilidade civil objetiva do Estado perante a vítima, conforme a revisão, assinale a alternativa correta.

A) A vítima é indenizada automaticamente, mesmo sem dano ou nexo causal.
B) O direito de regresso contra o agente independe de dolo ou culpa.
C) Apenas sociedades de economia mista respondem objetivamente por atos de seus agentes.
D) Ainda se exigem conduta estatal, dano e nexo causal, assegurado regresso contra o agente em caso de dolo ou culpa.

#### Extra Dia 2.16

Leia: “Em enlaces IPv4 ponto a ponto, um prefixo `/31` pode usar os dois endereços.” Assinale a interpretação fiel ao alcance da frase.

A) Toda rede `/31` deve ser uma LAN multiacesso com dois hosts.
B) O uso dos dois endereços é apresentado como possibilidade no contexto específico de enlace ponto a ponto.
C) Nenhuma rede `/31` admite dois endereços, pois “pode” expressa proibição.
D) O enunciado obriga qualquer implementação IPv4 a empregar `/31`.

#### Extra Dia 2.17

No período “O IPv6 amplia o espaço de endereçamento; entretanto, esse fato não elimina a necessidade de planejamento”, assinale a alternativa correta.

A) “Entretanto” introduz causa, e “esse” antecipa uma informação ainda não apresentada.
B) “Entretanto” conclui o raciocínio, e “esse” retoma a necessidade de planejamento.
C) “Entretanto” marca oposição ou ressalva, e “esse fato” retoma a ampliação do espaço de endereçamento.
D) O período permite inferir que o planejamento se tornou desnecessário.

#### Extra Dia 2.18

Assinale a alternativa com pontuação adequada.

A) Os endereços privados, podem ser reutilizados por organizações diferentes.
B) O gateway padrão encaminha, destinos remotos quando não há rota mais específica.
C) O IPv6 que possui 128 bits não, utiliza endereço de broadcast.
D) O ARP, no IPv4 sobre Ethernet, resolve endereço IP em endereço MAC.

#### Extra Dia 2.19

Assinale a alternativa em que o emprego da crase está correto.

A) O roteador começou à encaminhar os pacotes para o próximo salto.
B) A regra se aplica às sub-redes IPv4 convencionais.
C) O pacote chegou à transmitir dados depois da configuração.
D) O analista entregou o relatório à revisar pelo gestor.

#### Extra Dia 2.20

Original: “Embora o endereço esteja fora dos blocos privados definidos pela RFC 1918, ele pode pertencer a um bloco especial.” Assinale a reescrita que preserva o sentido técnico e linguístico.

A) Ainda que o endereço não pertença aos blocos privados definidos pela RFC 1918, é possível que integre um bloco especial.
B) Como o endereço está fora dos blocos privados definidos pela RFC 1918, ele é obrigatoriamente público e jamais especial.
C) O endereço pertence à RFC 1918, portanto talvez não seja privado.
D) Se o endereço estiver em bloco especial, então necessariamente pertence à RFC 1918.

## Gabarito do Dia 2

### Gabarito das questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | D |
| 2 | A |
| 3 | D |
| 4 | D |
| 5 | B |
| 6 | C |
| 7 | B |
| 8 | B |
| 9 | A |
| 10 | B |
| 11 | D |
| 12 | C |
| 13 | C |
| 14 | B |
| 15 | C |
| 16 | D |
| 17 | D |
| 18 | A |
| 19 | B |
| 20 | A |
| 21 | C |
| 22 | C |
| 23 | A |
| 24 | D |
| 25 | A |
| 26 | D |
| 27 | C |
| 28 | A |
| 29 | B |
| 30 | B |
| 31 | D |
| 32 | B |
| 33 | A |
| 34 | D |
| 35 | A |
| 36 | D |
| 37 | C |
| 38 | A |
| 39 | C |
| 40 | C |
| 41 | A |
| 42 | B |
| 43 | A |
| 44 | B |
| 45 | C |
| 46 | A |
| 47 | B |
| 48 | D |
| 49 | B |
| 50 | C |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 2.1 | B |
| 2.2 | A |
| 2.3 | B |
| 2.4 | C |
| 2.5 | A |
| 2.6 | C |
| 2.7 | A |
| 2.8 | D |
| 2.9 | B |
| 2.10 | D |
| 2.11 | C |
| 2.12 | A |
| 2.13 | D |
| 2.14 | C |
| 2.15 | D |
| 2.16 | B |
| 2.17 | C |
| 2.18 | D |
| 2.19 | B |
| 2.20 | A |

## Comentários do Dia 2

### Comentário da Questão 1

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Sessão vem depois de Apresentação, Transporte precede Rede e Física é a camada inferior.
- **B)** Incorreta. A opção desloca Transporte para antes de Sessão e troca a ordem final entre Física e Enlace.
- **C)** Incorreta. A lista está na direção inferior para superior, contrária ao comando.
- **D)** Correta. A sequência desce de Aplicação até Física na ordem das sete camadas do OSI.

**Conceito:** ordem e organização funcional do modelo OSI.

**Pegadinha:** reconhecer os sete nomes, mas aceitar uma permutação ou a ordem inversa.

**Como pensar:** numere mentalmente Aplicação como 7 e Física como 1, verificando cada posição intermediária.

**Referência:** [1. Modelo OSI e suas sete camadas](semana_02_estudo.md#s2-d2-osi).

### Comentário da Questão 2

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Apresentação cuida didaticamente da representação, codificação, compressão e proteção dos dados.
- **B)** Incorreta. Sessão organiza diálogos, manutenção e sincronização, não a forma de representar os dados.
- **C)** Incorreta. Transporte atende processos finais, usando recursos como portas, segmentação e controle conforme o protocolo.
- **D)** Incorreta. Rede trata de endereçamento lógico e encaminhamento entre redes.

**Conceito:** função da camada de Apresentação.

**Pegadinha:** atribuir criptografia automaticamente ao Transporte por ela proteger uma comunicação fim a fim.

**Como pensar:** pergunte se a tarefa altera como a informação é representada ou como ela é encaminhada.

**Referência:** [1. Modelo OSI — Camada 6, Apresentação](semana_02_estudo.md#s2-d2-osi).

### Comentário da Questão 3

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmativa II também é verdadeira ao associar endereçamento lógico e encaminhamento à Rede.
- **B)** Incorreta. A III é falsa, pois o IP não garante confirmação e retransmissão fim a fim.
- **C)** Incorreta. Incluir a III transfere indevidamente ao IP uma confiabilidade que pode ser oferecida pelo TCP.
- **D)** Correta. Transporte comunica processos e pode usar portas; Rede cuida de IP e encaminhamento.

**Conceito:** distinção entre as funções das camadas de Transporte e Rede.

**Pegadinha:** tratar comunicação fim a fim como sinônimo de entrega confiável realizada pelo IP.

**Como pensar:** avalie cada assertiva isoladamente e separe processo, rota e mecanismo de confiabilidade.

**Referência:** [1. Modelo OSI — Camadas 4 e 3](semana_02_estudo.md#s2-d2-osi).

### Comentário da Questão 4

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Escolher rota pelo IP é função de Rede, não de um repetidor físico.
- **B)** Incorreta. Quadros e aprendizagem de MAC pertencem ao Enlace.
- **C)** Incorreta. Diálogo e sincronização são funções conceituais da Sessão.
- **D)** Correta. A Física transmite bits como sinais sem interpretar endereços MAC ou IP.

**Conceito:** atuação da camada Física e de repetidores.

**Pegadinha:** confundir regeneração do sinal com análise do conteúdo transportado.

**Como pensar:** se o dispositivo apenas trata sinal e bits, permaneça na camada 1.

**Referência:** [1. Modelo OSI — Camada 1, Física](semana_02_estudo.md#s2-d2-osi).

### Comentário da Questão 5

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Transporte e Rede do OSI correspondem, respectivamente, a Transporte e Internet no TCP/IP.
- **B)** Correta. Aplicação, Apresentação e Sessão são agrupadas na Aplicação do modelo TCP/IP de quatro camadas.
- **C)** Incorreta. Enlace do OSI integra o Enlace do TCP/IP, não o Transporte.
- **D)** Incorreta. No modelo de quatro camadas, funções de Enlace e Física ficam agrupadas.

**Conceito:** correspondência didática entre OSI e TCP/IP.

**Pegadinha:** exigir uma relação de uma camada para uma camada entre modelos com quantidades diferentes.

**Como pensar:** agrupe as três superiores e as duas inferiores do OSI antes de comparar.

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip).

### Comentário da Questão 6

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A apresentação em cinco camadas continua descrevendo a suíte IP, TCP e UDP.
- **B)** Incorreta. O modelo de quatro camadas inclui essas funções dentro de sua camada de Enlace.
- **C)** Correta. Separar Física de Enlace é uma escolha pedagógica, não uma troca de protocolos.
- **D)** Incorreta. Cinco camadas ainda não produzem correspondência perfeita com as sete do OSI.

**Conceito:** variações didáticas de quatro e cinco camadas do TCP/IP.

**Pegadinha:** interpretar mudança no desenho do modelo como mudança na arquitetura real da Internet.

**Como pensar:** diferencie a suíte empregada da maneira escolhida pelo livro para agrupar funções.

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip).

### Comentário da Questão 7

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O segmento TCP é formado antes de ser encapsulado pelo IP.
- **B)** Correta. Dados recebem cabeçalho TCP, depois IP, depois informações de Ethernet e seguem como bits.
- **C)** Incorreta. O quadro não antecede as unidades das camadas superiores no emissor.
- **D)** Incorreta. O pacote IP fica dentro do quadro, não depois dele.

**Conceito:** encapsulamento descendente no emissor.

**Pegadinha:** inverter a ordem física de inclusão dos cabeçalhos por começar a análise pelo meio.

**Como pensar:** acompanhe os dados da aplicação para baixo: Transporte, Internet, Enlace e Física.

**Referência:** [3. Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento).

### Comentário da Questão 8

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O receptor precisa reconhecer o quadro antes de alcançar o segmento encapsulado no pacote.
- **B)** Correta. Bits formam o quadro, do qual se extrai o pacote IPv4, depois o segmento TCP e os dados.
- **C)** Incorreta. Bits não são processados depois do quadro; constituem sua representação no meio.
- **D)** Incorreta. A ordem começa pelas camadas inferiores, e o segmento precede a entrega dos dados à aplicação.

**Conceito:** desencapsulamento ascendente no receptor.

**Pegadinha:** repetir a ordem do emissor, quando o receptor percorre o caminho inverso.

**Como pensar:** comece pelo que chega fisicamente e remova um invólucro de cada vez.

**Referência:** [3. Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento).

### Comentário da Questão 9

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Cada enlace recebe quadro próprio, os IPs normalmente persistem sem NAT e o TTL é reduzido no caminho.
- **B)** Incorreta. O primeiro quadro usa o MAC do próximo salto, não o MAC do servidor remoto.
- **C)** Incorreta. A opção inverte o comportamento usual de IP e MAC ao longo dos roteadores.
- **D)** Incorreta. MAC tem escopo de enlace, enquanto IP identifica a comunicação lógica entre as pontas.

**Conceito:** campos que permanecem ou mudam a cada salto.

**Pegadinha:** imaginar que o quadro Ethernet atravessa intacto todos os roteadores.

**Como pensar:** desenhe um quadro por enlace e um pacote IP percorrendo o caminho, ressalvadas exceções como NAT.

**Referência:** [3. Encapsulamento — O que muda a cada salto](semana_02_estudo.md#s2-d2-encapsulamento).

### Comentário da Questão 10

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A opção troca as PDUs de TCP, IP e Ethernet e chama os bits de dados genéricos.
- **B)** Correta. TCP usa segmento, IP pacote ou datagrama, Ethernet quadro e Física bits.
- **C)** Incorreta. Pacote, quadro e datagrama UDP foram associados às camadas erradas.
- **D)** Incorreta. Bits são da Física, não do TCP; pacote é da camada Internet, não da Física.

**Conceito:** nomenclatura específica das PDUs.

**Pegadinha:** usar “pacote” como nome universal quando a questão exige precisão por camada.

**Como pensar:** ligue Transporte a segmento ou datagrama, Internet a pacote, Enlace a quadro e Física a bits.

**Referência:** [4. PDUs](semana_02_estudo.md#s2-d2-pdus).

### Comentário da Questão 11

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. UDP pertence ao Transporte e IP à camada Internet, portanto os termos não são sinônimos.
- **B)** Incorreta. Nenhuma das duas unidades pertence à Física, e datagrama UDP não é quadro.
- **C)** Incorreta. A relação de encapsulamento está invertida: IP envolve UDP.
- **D)** Correta. O datagrama UDP de Transporte pode ser a carga de um datagrama IP.

**Conceito:** diferença entre datagrama UDP e datagrama IP.

**Pegadinha:** concluir que o mesmo substantivo “datagrama” indica a mesma camada.

**Como pensar:** identifique primeiro o protocolo que qualifica a PDU e depois sua posição no encapsulamento.

**Referência:** [4. PDUs](semana_02_estudo.md#s2-d2-pdus).

### Comentário da Questão 12

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Portas identificam processos no Transporte; MAC identifica interface no Enlace.
- **B)** Incorreta. Roteadores removem o quadro e criam outro com endereços adequados ao novo enlace.
- **C)** Correta. Seis octetos hexadecimais são comuns, sem implicar imutabilidade absoluta.
- **D)** Incorreta. MAC não substitui IP e pode ser localmente administrado ou alterado.

**Conceito:** formato, escopo e administração do endereço MAC.

**Pegadinha:** repetir a noção antiga de que todo MAC é gravado, único e permanente.

**Como pensar:** separe identidade local da interface, endereço lógico entre redes e identificador de processo.

**Referência:** [5. Endereço MAC](semana_02_estudo.md#s2-d2-mac).

### Comentário da Questão 13

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O switch aprende pela origem observada, não presume que o destino esteja na porta de entrada.
- **B)** Incorreta. A tabela de comutação de camada 2 relaciona MAC e porta, não IP e rota padrão.
- **C)** Correta. O quadro recebido comprova que o MAC de origem é alcançável pela porta 5.
- **D)** Incorreta. Números TCP não participam da aprendizagem de MAC do switch.

**Conceito:** aprendizagem de endereços pelo switch.

**Pegadinha:** trocar origem por destino ao descrever a atualização da tabela MAC.

**Como pensar:** o equipamento aprende com a informação cuja localização acabou de observar: a origem.

**Referência:** [5. Endereço MAC](semana_02_estudo.md#s2-d2-mac).

### Comentário da Questão 14

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Quarenta e oito bits é tamanho comum de MAC, não de IPv4.
- **B)** Correta. IPv4 tem 32 bits, e o prefixo conta os bits iniciais reservados à rede.
- **C)** Incorreta. IPv4 possui quatro octetos no total, não 64 bits.
- **D)** Incorreta. Cento e vinte e oito bits e oito grupos hexadecimais descrevem IPv6.

**Conceito:** tamanho e divisão lógica do endereço IPv4.

**Pegadinha:** misturar o tamanho do MAC ou do IPv6 com o do IPv4.

**Como pensar:** associe IPv4 a quatro octetos de oito bits e deixe o prefixo definir a fronteira.

**Referência:** [6. IPv4](semana_02_estudo.md#s2-d2-ipv4).

### Comentário da Questão 15

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. `/20` corresponderia a quatro bits 1 no terceiro octeto, cujo valor seria 240.
- **B)** Incorreta. `/21` usaria 248 no terceiro octeto, com cinco bits 1.
- **C)** Correta. `255` fornece 8 bits, outro `255` mais 8 e `252` fornece 6: `8 + 8 + 6 = 22`.
- **D)** Incorreta. `/23` exigiria sete bits 1 no terceiro octeto, isto é, 254.

**Conceito:** conversão de máscara decimal para prefixo CIDR.

**Pegadinha:** confundir os valores próximos 248, 252 e 254 no octeto interessante.

**Como pensar:** conte os bits 1 em cada octeto, usando `252 = 11111100`.

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

### Comentário da Questão 16

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. `224` possui três bits 1 e, após dois octetos completos, forma `/19`.
- **B)** Incorreta. `248` possui cinco bits 1, formando `/21`.
- **C)** Incorreta. `255.255.255.240` contém 28 bits 1, não 20.
- **D)** Correta. Dezesseis bits ocupam os dois primeiros octetos e quatro bits formam `240`: `16 + 4 = 20`.

**Conceito:** conversão de prefixo CIDR para máscara decimal.

**Pegadinha:** posicionar os quatro bits restantes no último octeto em vez do terceiro.

**Como pensar:** preencha octetos completos com 255 e converta apenas a sobra do prefixo.

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

### Comentário da Questão 17

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta como escolha. `255.255.255.192` tem 26 bits 1 contíguos e é máscara válida.
- **B)** Incorreta como escolha. `255.255.254.0` representa `/23` com contiguidade preservada.
- **C)** Incorreta como escolha. `255.248.0.0` representa `/13` e não volta a apresentar bits 1 após zeros.
- **D)** Correta. Em `255.255.240.128`, o terceiro octeto termina com zeros e o quarto reintroduz um bit 1.

**Conceito:** contiguidade dos bits da máscara CIDR IPv4.

**Pegadinha:** o comando pede a sequência que NÃO representa máscara normal.

**Como pensar:** depois do primeiro zero, percorra o restante e rejeite qualquer ocorrência posterior de 1.

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

### Comentário da Questão 18

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. `/26` usa máscara final 192, bloco `256 - 192 = 64`; 158 está em 128–191.
- **B)** Incorreta. `.190` é host válido, mas o broadcast tem todos os seis bits de host em 1 e vale `.191`.
- **C)** Incorreta. `.64` inicia o bloco anterior, que termina em `.127`.
- **D)** Incorreta. `.152` e `.159` não são as fronteiras de um bloco `/26`.

**Conceito:** cálculo de rede e broadcast pelo tamanho do bloco.

**Pegadinha:** usar o último host como broadcast ou ignorar o alinhamento em múltiplos de 64.

**Como pensar:** liste 0, 64, 128 e 192; escolha o início anterior a 158 e o endereço anterior ao próximo início.

**Referência:** [8. Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

### Comentário da Questão 19

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O intervalo inclui rede `.192` e broadcast `.223`, que não são hosts convencionais.
- **B)** Correta. `/27` deixa 5 bits, bloco `2^5 = 32`; 222 está em 192–223 e os hosts são 193–222.
- **C)** Incorreta. `.223` é o broadcast dirigido e não integra a faixa convencional de hosts.
- **D)** Incorreta. A faixa proposta atravessa a fronteira entre blocos `/27`.

**Conceito:** determinação da faixa de hosts em uma sub-rede `/27`.

**Pegadinha:** incluir uma ou ambas as extremidades reservadas no IPv4 convencional.

**Como pensar:** encontre primeiro rede e broadcast; só então retire a primeira e a última posições.

**Referência:** [9. Exemplos de IPv4 e CIDR — Bloco /27](semana_02_estudo.md#s2-d2-calculos).

### Comentário da Questão 20

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. `/20` tem máscara `255.255.240.0`, incremento 16 no terceiro octeto; 173 cai em 160–175.
- **B)** Incorreta. O início 168 não é múltiplo do bloco 16 exigido por `/20`.
- **C)** Incorreta. Zerar apenas o quarto octeto equivaleria ao raciocínio de `/24`.
- **D)** Incorreta. O final 191 pertence a um bloco maior que o `/20` informado.

**Conceito:** cálculo de rede e broadcast quando a fronteira está no terceiro octeto.

**Pegadinha:** aplicar o incremento apenas ao último octeto por hábito.

**Como pensar:** identifique o octeto interessante, calcule `256 - 240 = 16` e delimite o bloco que contém 173.

**Referência:** [9. Exemplos de IPv4 e CIDR — Prefixo no terceiro octeto](semana_02_estudo.md#s2-d2-calculos).

### Comentário da Questão 21

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Oito não corresponde nem ao total nem aos hosts convencionais de `/28`.
- **B)** Incorreta. Não se subtraem quatro posições do bloco.
- **C)** Correta. Restam `32 - 28 = 4` bits; `2^4 = 16` endereços e `16 - 2 = 14` hosts convencionais.
- **D)** Incorreta. Dezesseis é o total de endereços, incluindo rede e broadcast.

**Conceito:** quantidade convencional de hosts pelo prefixo.

**Pegadinha:** marcar o total do bloco sem reservar rede e broadcast.

**Como pensar:** calcule bits de host, eleve 2 e, no IPv4 convencional, subtraia as duas extremidades.

**Referência:** [8. Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

### Comentário da Questão 22

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. No contexto RFC 3021, `.11` não é tratado como broadcast convencional do enlace.
- **B)** Incorreta. Aplicar `2^h - 2` mecanicamente apagaria justamente a exceção do `/31` ponto a ponto.
- **C)** Correta. Os dois endereços do bloco podem identificar as duas extremidades do enlace compatível.
- **D)** Incorreta. Rota de um único host é a semântica de `/32`, não de `/31`.

**Conceito:** exceção do prefixo `/31` em enlace IPv4 ponto a ponto.

**Pegadinha:** generalizar a regra de rede e broadcast das sub-redes multiacesso.

**Como pensar:** antes da fórmula, verifique o contexto; `/31` só usa ambos os endereços na situação ponto a ponto compatível.

**Referência:** [9. Exemplos de IPv4 e CIDR — /31 ponto a ponto](semana_02_estudo.md#s2-d2-calculos).

### Comentário da Questão 23

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. `/32` fixa os 32 bits e representa exatamente um endereço ou rota de host.
- **B)** Incorreta. Duas extremidades é a aplicação especial de `/31`.
- **C)** Incorreta. `255.255.255.254` corresponde a `/31`; `/32` usa todos os bits em 1.
- **D)** Incorreta. A descrição de 254 hosts remete a `/24` convencional, não a `/32`.

**Conceito:** semântica excepcional do prefixo IPv4 `/32`.

**Pegadinha:** tentar calcular rede, broadcast e faixa onde existe apenas uma rota de host.

**Como pensar:** com zero bits de host, pare o método de sub-rede convencional e identifique o endereço único.

**Referência:** [9. Exemplos de IPv4 e CIDR — /32](semana_02_estudo.md#s2-d2-calculos).

### Comentário da Questão 24

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. `172.15.200.1` está abaixo do início `172.16.0.0` do bloco privado.
- **B)** Incorreta. `172.32.0.10` já ultrapassou o fim `172.31.255.255`.
- **C)** Incorreta. A faixa privada começa com `192.168`, não `192.169`.
- **D)** Correta. `172.31.200.5` está dentro de `172.16.0.0/12`.

**Conceito:** limites dos blocos privados RFC 1918.

**Pegadinha:** considerar privado todo o bloco cujo primeiro octeto é 172.

**Como pensar:** memorize o intervalo exato do segundo octeto: de 16 a 31, inclusive.

**Referência:** [10. Redes públicas, privadas e endereços especiais](semana_02_estudo.md#s2-d2-publicos-privados-especiais).

### Comentário da Questão 25

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. IPv4 reserva todo o bloco `127/8`, e IPv6 define `::1/128` para loopback.
- **B)** Incorreta. `127.0.0.1` é apenas o exemplo mais conhecido, não o único endereço do bloco.
- **C)** Incorreta. Loopback representa o próprio host e não funciona como gateway para a Internet.
- **D)** Incorreta. `fe80::/10` é link-local; o loopback IPv6 é `::1`.

**Conceito:** endereços de loopback em IPv4 e IPv6.

**Pegadinha:** reduzir o bloco IPv4 inteiro ao endereço usual `127.0.0.1`.

**Como pensar:** diferencie comunicação interna do próprio host de alcance limitado ao enlace.

**Referência:** [10. Redes públicas, privadas e endereços especiais — Loopback](semana_02_estudo.md#s2-d2-publicos-privados-especiais).

### Comentário da Questão 26

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. `169.254/16` é link-local; loopback IPv4 pertence a `127/8`.
- **B)** Incorreta. APIPA não integra os blocos privados RFC 1918 e não cria acesso roteado à Internet.
- **C)** Incorreta. O endereço não é público nem foi atribuído como concessão global provisória.
- **D)** Correta. `169.254.20.8` está na faixa selecionável APIPA e sugere que a configuração DHCP esperada não foi obtida.

**Conceito:** autoconfiguração IPv4 link-local/APIPA.

**Pegadinha:** confundir alcance local ao enlace com loopback ou com endereço privado roteável internamente.

**Como pensar:** confira a faixa selecionável `169.254.1.0`–`169.254.254.255`, a máscara `/16` e a ausência de rota automática à Internet.

**Referência:** [10. Redes especiais — IPv4 link-local e APIPA](semana_02_estudo.md#s2-d2-publicos-privados-especiais).

### Comentário da Questão 27

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Há diversas finalidades especiais além dos três blocos privados.
- **B)** Incorreta. A terminação decimal não determina se um endereço é globalmente utilizável, pois isso depende do prefixo e da finalidade do bloco.
- **C)** Correta. Loopback, link-local, documentação, multicast e outras reservas impedem a conclusão automática.
- **D)** Incorreta. A ressalva não depende apenas de o prefixo ser maior que `/24`.

**Conceito:** diferença entre “fora dos blocos privados da RFC 1918” e “unicast público utilizável”.

**Pegadinha:** usar um teste negativo de privacidade como prova suficiente de publicidade.

**Como pensar:** primeiro exclua os blocos privados e depois verifique todas as categorias de finalidade especial.

**Referência:** [10. Redes especiais — IPv4 público](semana_02_estudo.md#s2-d2-publicos-privados-especiais).

### Comentário da Questão 28

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. São `27 - 24 = 3` bits emprestados, logo `2^3 = 8` sub-redes; cada uma tem `2^5 = 32` endereços e 30 hosts.
- **B)** Incorreta. Quatro blocos de 64 e 62 hosts resultariam da divisão em `/26`.
- **C)** Incorreta. O bloco possui 32 endereços totais, não 30; 30 é a quantidade de hosts convencionais.
- **D)** Incorreta. Dezesseis blocos de 16 e 14 hosts correspondem a `/28`.

**Conceito:** divisão uniforme de um prefixo em sub-redes menores.

**Pegadinha:** trocar a quantidade total de endereços pela quantidade utilizável de hosts.

**Como pensar:** calcule separadamente bits emprestados e bits restantes: `2^(27-24)` e `2^(32-27) - 2`.

**Referência:** [9. Exemplos de IPv4 e CIDR — Divisão de /24 em /27](semana_02_estudo.md#s2-d2-calculos).

### Comentário da Questão 29

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmativa II também é verdadeira, pois explicita corretamente as fronteiras do bloco de A e B.
- **B)** Correta. `/23` agrupa 10–11 no bloco iniciado em 10; C inicia outro bloco, 12–13.
- **C)** Incorreta. A III é falsa: abranger pares de octetos não significa que qualquer par consecutivo pertença ao mesmo bloco.
- **D)** Incorreta. C produz rede `192.168.12.0/23`, diferente da rede `192.168.10.0/23` de A e B.

**Conceito:** alinhamento e pertencimento a uma sub-rede `/23`.

**Pegadinha:** observar que 11 e 12 são consecutivos e ignorar que os blocos começam em múltiplos de 2.

**Como pensar:** a máscara `/23` usa `255.255.254.0`; aplique incremento 2 ao terceiro octeto: 10–11 e 12–13.

**Referência:** [11. Sub-redes — Verificação de pertencimento](semana_02_estudo.md#s2-d2-subredes).

### Comentário da Questão 30

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O bloco iniciado em 128 termina em 191 e não contém 205.
- **B)** Correta. `/26` avança 64; 205 está entre 192 e 255, portanto a rede é `.192/26`.
- **C)** Incorreta. `.200` não é múltiplo de 64 e não pode identificar o início desse `/26`.
- **D)** Incorreta. `.205/26` descreve um endereço dentro do bloco, não o endereço alinhado da rede.

**Conceito:** identificação do bloco que contém um IPv4.

**Pegadinha:** repetir o endereço do host após a barra como se ele fosse automaticamente o identificador da rede.

**Como pensar:** com máscara final 192, calcule `256 - 192 = 64` e liste 0, 64, 128 e 192.

**Referência:** [8. Rede, broadcast e hosts — Tamanho do bloco](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

### Comentário da Questão 31

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. `.64` é o endereço de rede do bloco e não serve como gateway convencional.
- **B)** Incorreta. `.95` tem os cinco bits de host em 1 e é o broadcast dirigido.
- **C)** Incorreta. `.97` pertence ao bloco seguinte, iniciado em `.96`.
- **D)** Correta. `.94` é o último host válido do bloco 64–95 e pode ser a interface do gateway se o projeto assim definir.

**Conceito:** alcançabilidade e validade do gateway dentro da sub-rede.

**Pegadinha:** presumir que gateway precisa terminar em `.1` ou aceitar rede e broadcast como interface.

**Como pensar:** `/27` cria bloco de 32; para 78, delimite rede 64, broadcast 95 e hosts 65–94.

**Referência:** [12. Gateway padrão](semana_02_estudo.md#s2-d2-gateway).

### Comentário da Questão 32

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O IP de destino continua sendo o servidor; quem muda no primeiro quadro é o destino MAC.
- **B)** Correta. O pacote aponta ao destino remoto, mas o quadro alcança o gateway no enlace local.
- **C)** Incorreta. Um quadro Ethernet precisa de endereço de enlace, e porta TCP não substitui a decisão de camada 2.
- **D)** Incorreta. ARP não atravessa roteadores nem resolve diretamente o MAC de um servidor remoto.

**Conceito:** uso do gateway como próximo salto e separação entre IP e MAC.

**Pegadinha:** trocar o destino lógico final pelo destino local do quadro.

**Como pensar:** mantenha o pacote endereçado ao servidor e envolva-o em um quadro endereçado ao próximo salto.

**Referência:** [12. Gateway padrão](semana_02_estudo.md#s2-d2-gateway).

### Comentário da Questão 33

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O ARP Request é broadcast no enlace, e o detentor do IPv4 informa seu MAC normalmente por unicast.
- **B)** Incorreta. ARP não usa TCP nem DNS e parte de um IPv4 já conhecido.
- **C)** Incorreta. Para vizinho local, a consulta circula justamente no enlace e não depende de roteamento.
- **D)** Incorreta. ICMP Echo não descobre a porta física do switch nem substitui a resolução ARP.

**Conceito:** fluxo de resolução ARP para destino local.

**Pegadinha:** confundir resolução de nome por DNS com resolução de IPv4 em MAC por ARP.

**Como pensar:** se o IP é local e falta a associação, procure no enlace quem possui esse endereço.

**Referência:** [13. ARP](semana_02_estudo.md#s2-d2-arp).

### Comentário da Questão 34

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A consulta ARP não é encaminhada por roteadores até o servidor remoto.
- **B)** Incorreta. ARP associa endereço de protocolo e hardware, sem usar porta TCP.
- **C)** Incorreta. Não se procura um “IPv6 equivalente” para encaminhar esse pacote IPv4.
- **D)** Correta. O próximo salto local é `192.168.10.1`, por isso seu MAC é necessário no primeiro quadro.

**Conceito:** ARP para o gateway quando o destino IP é remoto.

**Pegadinha:** procurar o MAC do destino final em vez do dispositivo alcançável no enlace atual.

**Como pensar:** determine localidade com a máscara; se o destino for remoto, resolva o endereço de enlace do gateway.

**Referência:** [13. ARP — Destino remoto](semana_02_estudo.md#s2-d2-arp).

### Comentário da Questão 35

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta como resposta ao comando INCORRETA. ICMP não utiliza portas TCP ou UDP.
- **B)** Incorreta como escolha. Echo Request e Echo Reply são mensagens usadas pelo `ping`.
- **C)** Incorreta como escolha. Time Exceeded e Destination Unreachable pertencem ao conjunto de controle e erro.
- **D)** Incorreta como escolha. Bloqueio indiscriminado pode prejudicar diagnóstico e mecanismos necessários.

**Conceito:** função e transporte das mensagens ICMP.

**Pegadinha:** ignorar o comando negativo ou atribuir número de porta a todo protocolo conhecido.

**Como pensar:** procure a afirmação falsa e separe ICMP, integrado à camada Internet, de TCP e UDP.

**Referência:** [14. ICMP e ICMPv6](semana_02_estudo.md#s2-d2-icmp).

### Comentário da Questão 36

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. IPv6 não usa ARP tradicional e não possui broadcast.
- **B)** Incorreta. Converter nomes é função de DNS, muito mais estreita que Neighbor Discovery.
- **C)** Incorreta. NS e NA são mensagens ICMPv6, não serviços de porta TCP.
- **D)** Correta. Neighbor Discovery inclui resolução de endereço de enlace, descoberta e acompanhamento de vizinhos por ICMPv6.

**Conceito:** Neighbor Discovery e mensagens NS/NA.

**Pegadinha:** chamar o mecanismo de “ARP do IPv6” e transportar para ele broadcast e portas.

**Como pensar:** associe IPv4 a ARP e IPv6 a um conjunto mais amplo baseado em ICMPv6.

**Referência:** [14. ICMPv6 — Neighbor Discovery, NS e NA](semana_02_estudo.md#s2-d2-icmp).

### Comentário da Questão 37

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Duas ocorrências de `::` tornam impossível saber quantos grupos zero cada uma representa.
- **B)** Incorreta. A expansão posiciona `ff00` em grupo diferente do endereço original.
- **C)** Correta. Remove zeros à esquerda e comprime uma única sequência de três grupos zero.
- **D)** Incorreta. A compressão ao final deslocaria `ff00:42:8329` para posições diferentes.

**Conceito:** regras de abreviação textual de IPv6.

**Pegadinha:** aceitar qualquer forma com oito grupos aparentes sem conferir a expansão completa.

**Como pensar:** expanda cada alternativa para oito grupos e permita `::` somente uma vez.

**Referência:** [15. IPv6 — Regras de abreviação](semana_02_estudo.md#s2-d2-ipv6).

### Comentário da Questão 38

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. IPv6 não define endereço de broadcast e pode usar multicast para entrega em grupo.
- **B)** Incorreta. `ff02::1` é multicast de todos os nós com escopo de enlace, não broadcast global.
- **C)** Incorreta. Prefixos IPv6 não reservam a última posição como broadcast dirigido.
- **D)** Incorreta. A inexistência de broadcast não depende de o prefixo ser `/64`.

**Conceito:** ausência de broadcast no IPv6.

**Pegadinha:** transportar automaticamente para IPv6 as reservas de rede e broadcast do IPv4.

**Como pensar:** trate a ausência de broadcast como regra do IPv6; entrega coletiva usa multicast ou múltiplos unicasts.

**Referência:** [15. IPv6 — Tipos de endereço](semana_02_estudo.md#s2-d2-ipv6).

### Comentário da Questão 39

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A opção inverte unicast e multicast.
- **B)** Incorreta. Anycast entrega a uma das interfaces, não cópia a todas.
- **C)** Correta. A alternativa distingue destino individual, grupo e uma interface escolhida entre várias.
- **D)** Incorreta. IPv6 não possui broadcast, e multicast mantém identidade própria.

**Conceito:** unicast, multicast e anycast no IPv6.

**Pegadinha:** entender “mesmo endereço em várias interfaces” como entrega simultânea a todas.

**Como pensar:** associe “um”, “grupo” e “uma dentre várias” aos três tipos, nessa ordem.

**Referência:** [15. IPv6 — Tipos de endereço](semana_02_estudo.md#s2-d2-ipv6).

### Comentário da Questão 40

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Eliminar o quarto grupo preservaria apenas 48 bits, não os 64 informados.
- **B)** Incorreta. `/64` conserva integralmente `12ef`; não se zera sua parte final como em um prefixo menor.
- **C)** Correta. Quatro grupos de 16 bits totalizam 64, resultando em `2001:db8:abcd:12ef::/64`.
- **D)** Incorreta. Preservar parte do quinto grupo ultrapassaria os 64 bits de prefixo.

**Conceito:** determinação de prefixo IPv6 em fronteira de grupo.

**Pegadinha:** aplicar lógica de máscara decimal pontuada ou contar grupos em vez de bits.

**Como pensar:** some `4 × 16 = 64`, mantenha os quatro primeiros grupos e zere a parte de interface; IPv6 usa prefixo, não máscara pontuada.

**Referência:** [15. IPv6 — Prefixo IPv6](semana_02_estudo.md#s2-d2-ipv6).

### Comentário da Questão 41

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Os três prefixos correspondem a link-local, loopback e documentação.
- **B)** Incorreta. `fc00::/7` é unique-local, distinto de `fe80::/10`, e pode ser roteado em ambientes locais ou acordados.
- **C)** Incorreta. `::/128` é o endereço não especificado, não grupo de roteadores.
- **D)** Incorreta. `2001:db8::/32` serve a exemplos e documentação, não produção pública obrigatória.

**Conceito:** blocos especiais e escopos do IPv6.

**Pegadinha:** tratar unique-local e link-local como sinônimos por ambos não serem esperados na Internet global.

**Como pensar:** memorize a função de `::`, `::1`, `fe80`, `fc00` e `2001:db8` separadamente.

**Referência:** [15. IPv6 — Blocos especiais importantes](semana_02_estudo.md#s2-d2-ipv6).

### Comentário da Questão 42

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Além da I, as afirmativas II e III também descrevem corretamente o escopo e a resolução de vizinho.
- **B)** Correta. `ff02::1` é multicast link-local; NS usa solicited-node e o roteador respeita o limite desse escopo.
- **C)** Incorreta. Excluir a I chamaria implicitamente de falsa uma distinção expressa entre multicast e broadcast.
- **D)** Incorreta. A II também é verdadeira: a resolução inicial não consulta indiscriminadamente todos os nós.

**Conceito:** multicast IPv6, escopo link-local e solicited-node no Neighbor Discovery.

**Pegadinha:** chamar `ff02::1` de broadcast ou supor que toda NS seja enviada a todos os nós do enlace.

**Como pensar:** verifique separadamente tipo de endereço, grupo de destino da NS e limite de encaminhamento do escopo 2.

**Referência:** [15. IPv6 — Escopo multicast](semana_02_estudo.md#s2-d2-ipv6) e [14. ICMPv6 — Neighbor Discovery](semana_02_estudo.md#s2-d2-icmp).

### Comentário da Questão 43

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. São necessários 6 bits de host, pois `2^6 - 2 = 62 ≥ 50`; assim, o maior prefixo é `/26`, produzindo `2^(26-24) = 4` sub-redes.
- **B)** Incorreta. `/27` deixa 5 bits e oferece apenas `2^5 - 2 = 30` hosts.
- **C)** Incorreta. `/25` oferece 126 hosts, mas gera somente 2 sub-redes, não 4, e não maximiza a quantidade.
- **D)** Incorreta. `/28` fornece `2^4 - 2 = 14` hosts, muito abaixo de 50.

**Conceito:** escolha do prefixo a partir de requisito de hosts e maximização de sub-redes.

**Pegadinha:** selecionar um bloco que comporta os hosts, mas não usa o maior prefixo possível, ou confundir total com utilizável.

**Como pensar:** encontre o menor `h` com `2^h - 2 ≥ 50`; depois faça `32 - h` e conte os bits emprestados.

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

### Comentário da Questão 44

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Embora `.32` seja fronteira `/27`, o bloco 32–63 está contido no `/26` já alocado, 0–63.
- **B)** Correta. `.64/27` ocupa 64–95, respeita incremento 32 e não toca 0–63 nem 128–159.
- **C)** Incorreta. `.128/27` é exatamente um dos blocos já alocados.
- **D)** Incorreta. `.144` não é múltiplo de 32; normalizá-lo levaria ao bloco 128–159, também ocupado.

**Conceito:** alinhamento e não sobreposição em VLSM.

**Pegadinha:** verificar apenas se o número inicial parece livre, sem testar a fronteira válida e toda a faixa do bloco.

**Como pensar:** liste os inícios `/27` em 0, 32, 64, 96, 128 e compare cada intervalo com as alocações existentes.

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

### Comentário da Questão 45

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Coincidência de três octetos não substitui a aplicação das duas máscaras.
- **B)** Incorreta. Pela máscara `/24` de A, B está no mesmo prefixo de A.
- **C)** Correta. A vê ambos em `192.168.1.0/24`; B vê a si em `.128/25` e A em `.0/25`.
- **D)** Incorreta. `/25` abrange menos endereços que `/24`, e a direção da assimetria foi invertida.

**Conceito:** decisão de localidade com máscaras divergentes.

**Pegadinha:** calcular uma única rede e presumir que a percepção dos dois hosts será simétrica.

**Como pensar:** faça dois testes: aplique a máscara de A aos dois IPs e, depois, a máscara de B aos dois.

**Referência:** [11. Sub-redes — Verificação de pertencimento](semana_02_estudo.md#s2-d2-subredes).

### Comentário da Questão 46

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. `/21` usa `255.255.248.0`; incremento `256 - 248 = 8`, então 173 cai em 168–175, com `2^11 - 2 = 2046` hosts.
- **B)** Incorreta. `.172` não é fronteira de bloco 8, e 1022 hosts corresponderiam a 10 bits de host.
- **C)** Incorreta. O broadcast `.183` ultrapassa o bloco `/21`, e 4094 é quantidade de `/20` convencional.
- **D)** Incorreta. Rede e broadcast limitados ao mesmo terceiro octeto tratariam o endereço como `/24`.

**Conceito:** cálculo integrado de rede, broadcast e hosts em `/21`.

**Pegadinha:** combinar fronteiras de um prefixo com a quantidade de hosts de outro.

**Como pensar:** calcule máscara, bloco do terceiro octeto e `h = 32 - 21 = 11` em etapas separadas.

**Referência:** [8. Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

### Comentário da Questão 47

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. `.128/28` é a nona sub-rede quando a contagem começa em `.0` como primeira.
- **B)** Correta. `/28` avança 16; índice da décima é 9, logo `9 × 16 = 144`, broadcast 159 e hosts 145–158.
- **C)** Incorreta. `.160/28` é a décima primeira sub-rede.
- **D)** Incorreta. O broadcast é uma posição antes do próximo bloco, `.159`, e não `.160`.

**Conceito:** localização ordinal de sub-rede e respectivas fronteiras.

**Pegadinha:** usar 10 como índice em vez de 9 ou incluir o início da próxima sub-rede como broadcast.

**Como pensar:** converta a ordem humana em índice iniciado em zero e multiplique pelo incremento 16.

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

### Comentário da Questão 48

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. As afirmativas II e III também são verdadeiras.
- **B)** Incorreta. A I descreve corretamente a exceção RFC 3021 do `/31` ponto a ponto.
- **C)** Incorreta. A III também é correta, pois IPv6 não reserva broadcast nos moldes do IPv4.
- **D)** Correta. `/31`, `/32` e IPv6 exigem tratamento distinto da contagem IPv4 convencional.

**Conceito:** limites de aplicação da fórmula `2^h - 2`.

**Pegadinha:** decorar uma fórmula e aplicá-la sem verificar protocolo, prefixo e tipo de enlace.

**Como pensar:** `/31` pode usar duas pontas no ponto a ponto; `/32` é um endereço; IPv6 não tem broadcast e não recebe a subtração automática.

**Referência:** [8. Endereço de rede, broadcast e hosts válidos — Exceções](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

### Comentário da Questão 49

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Roteadores validam e reduzem TTL; Echo Reply não é mecanismo para encaminhar pacote expirado.
- **B)** Correta. Ao chegar a zero, o pacote é descartado e pode provocar Time Exceeded, sem portas ou garantia de entrega.
- **C)** Incorreta. ICMP não abre conexão TCP nem retransmite de modo confiável o pacote original.
- **D)** Incorreta. ARP tem escopo local e não substitui o tratamento do TTL ao longo da rota.

**Conceito:** TTL, descarte e mensagem ICMP Time Exceeded.

**Pegadinha:** interpretar mensagem de erro como correção automática ou retransmissão do tráfego perdido.

**Como pensar:** se o TTL zerou, encerre o encaminhamento; a resposta possível apenas informa a origem sobre o evento.

**Referência:** [14. ICMP e ICMPv6](semana_02_estudo.md#s2-d2-icmp).

### Comentário da Questão 50

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A III também é verdadeira ao descrever o agrupamento das camadas superiores no TCP/IP.
- **B)** Incorreta. A I também é verdadeira: o roteador recria a unidade de enlace para o próximo salto.
- **C)** Correta. As três assertivas preservam camada, escopo e comparação didática dos modelos.
- **D)** Incorreta. I e II não contêm as trocas de camada ou de protocolo sugeridas pelos distratores usuais.

**Conceito:** integração entre roteamento, protocolos e comparação OSI/TCP/IP.

**Pegadinha:** exigir correspondência rígida entre modelos ou imaginar que o mesmo quadro cruza toda a rota.

**Como pensar:** valide cada plano separadamente: quadro no enlace, IP/ICMP na Internet e funções superiores na Aplicação TCP/IP.

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip) e [3. Encapsulamento](semana_02_estudo.md#s2-d2-encapsulamento).

#### Comentário Extra Dia 2.1

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Eficiência busca bons resultados e uso adequado de recursos, mas não autoriza afastar a lei.
- **B)** Correta. Legalidade exige atuação conforme o ordenamento e dentro da competência, mesmo quando outro caminho pareça mais rápido.
- **C)** Incorreta. Publicidade posterior não sana, por si, uma atuação contrária ao ordenamento.
- **D)** Incorreta. Para a Administração, legalidade não significa liberdade geral de fazer o que não foi proibido.

**Conceito:** convivência entre legalidade e eficiência no art. 37.

**Pegadinha:** transformar eficiência em autorização para escolher resultado acima da norma.

**Como pensar:** verifique primeiro se a atuação é juridicamente permitida; só depois compare qualidade, custo e velocidade.

**Referência:** [Revisão de Administração Pública — Princípios do art. 37](semana_02_estudo.md#s2-d2-revisao-principios).

#### Comentário Extra Dia 2.2

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A finalidade pública da comunicação é incompatível com favorecimento ou promoção pessoal do agente.
- **B)** Incorreta. Publicidade institucional não reduz necessariamente a qualidade do serviço e o cenário não descreve esse problema.
- **C)** Incorreta. Impessoalidade não exige anonimato; o vício está no uso promocional da estrutura pública.
- **D)** Incorreta. Moralidade é padrão jurídico de probidade e boa-fé, não simples juízo subjetivo.

**Conceito:** princípio da impessoalidade e vedação à promoção pessoal.

**Pegadinha:** confundir impessoalidade com ausência de identificação de quem praticou o ato.

**Como pensar:** pergunte se a mensagem serve à finalidade pública ou à construção da imagem particular do agente.

**Referência:** [Revisão de Administração Pública — Princípios do art. 37](semana_02_estudo.md#s2-d2-revisao-principios).

#### Comentário Extra Dia 2.3

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Publicidade é regra, mas não elimina sigilo legal nem proteção de dados pessoais.
- **B)** Correta. Transparência deve conviver com fundamento jurídico, finalidade, necessidade e segurança.
- **C)** Incorreta. A LGPD não torna sigiloso todo conteúdo mantido pelo Poder Público.
- **D)** Incorreta. A presença de dado pessoal exige análise e tratamento adequado, não afastamento automático da LAI.

**Conceito:** publicidade administrativa em harmonia com proteção de dados.

**Pegadinha:** escolher um absoluto, divulgação total ou sigilo total, para resolver uma convivência normativa.

**Como pensar:** preserve o acesso devido e limite apenas o dado cuja exposição não possua fundamento ou necessidade.

**Referência:** [Revisão de Administração Pública — Princípios do art. 37 e LAI x LGPD](semana_02_estudo.md#s2-d2-revisao-lai-lgpd).

#### Comentário Extra Dia 2.4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Órgão não possui personalidade própria, e o CRA-PR não integra a Administração Direta.
- **B)** Incorreta. A alternativa inverte as definições de órgão e entidade.
- **C)** Correta. Entidade é pessoa jurídica, e o CRA-PR é autarquia integrante da Administração Indireta.
- **D)** Incorreta. A revisão afasta expressamente a classificação do conselho como associação privada.

**Conceito:** Administração Direta, Indireta, órgão, entidade e autarquia.

**Pegadinha:** usar “órgão público” em sentido cotidiano e ignorar a personalidade jurídica.

**Como pensar:** faça duas perguntas: há personalidade própria e a estrutura está no ente político ou em entidade da Indireta?

**Referência:** [Revisão de Administração Pública — Administração Direta e Indireta](semana_02_estudo.md#s2-d2-revisao-organizacao).

#### Comentário Extra Dia 2.5

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A definição reúne personalidade de direito público, criação por lei e atividade administrativa típica.
- **B)** Incorreta. Órgão sem personalidade não é autarquia, e exploração econômica não é a função descrita no núcleo.
- **C)** Incorreta. Autarquia pertence à Administração Indireta, não surge como associação privada livre.
- **D)** Incorreta. Autarquia não é modalidade de empresa pública nem depende de capital privado.

**Conceito:** definição de autarquia.

**Pegadinha:** misturar características de órgão, empresa estatal e associação numa única definição.

**Como pensar:** procure o trio “direito público, criada por lei, atividade administrativa típica”.

**Referência:** [Revisão de Administração Pública — Administração Direta e Indireta](semana_02_estudo.md#s2-d2-revisao-organizacao).

#### Comentário Extra Dia 2.6

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Objeto é o efeito jurídico produzido, não a habilitação do agente para decidir.
- **B)** Incorreta. Forma responde a como o ato se exterioriza.
- **C)** Correta. Competência identifica quem recebeu atribuição para praticar o ato.
- **D)** Incorreta. Motivo reúne fatos e fundamentos, não a identidade funcional do autor.

**Conceito:** elementos clássicos do ato administrativo.

**Pegadinha:** confundir a causa do ato, sua manifestação e o agente juridicamente autorizado.

**Como pensar:** transforme cada elemento em pergunta; “quem pode?” conduz diretamente à competência.

**Referência:** [Revisão de Administração Pública — Elementos e atributos do ato](semana_02_estudo.md#s2-d2-revisao-atos).

#### Comentário Extra Dia 2.7

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A presunção admite prova contrária, e execução direta depende de hipótese legal ou urgência.
- **B)** Incorreta. Presunção relativa não impede controle ou contestação.
- **C)** Incorreta. Imperatividade impõe obrigações quando cabível justamente sem depender de concordância.
- **D)** Incorreta. Autoexecutoriedade não acompanha todo ato administrativo.

**Conceito:** presunção de legitimidade, imperatividade e autoexecutoriedade.

**Pegadinha:** converter atributos condicionados ou relativos em poderes absolutos.

**Como pensar:** desconfie de “todo”, “qualquer” e “impede”; confira as ressalvas ensinadas para cada atributo.

**Referência:** [Revisão de Administração Pública — Elementos e atributos do ato](semana_02_estudo.md#s2-d2-revisao-atos).

#### Comentário Extra Dia 2.8

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Ilegalidade não é avaliação de conveniência e exige anulação.
- **B)** Incorreta. Ato válido não se torna ilegal apenas por perder utilidade administrativa.
- **C)** Incorreta. Nem todo vício é convalidável, e inconveniência não fundamenta anulação.
- **D)** Correta. Anulação enfrenta ilegalidade; revogação retira ato válido por mérito, respeitados direitos adquiridos.

**Conceito:** distinção entre anulação e revogação.

**Pegadinha:** trocar os institutos porque ambos produzem retirada do ato.

**Como pensar:** pergunte “há ilegalidade?”; se sim, anulação. Se o ato é válido e o problema é mérito, revogação.

**Referência:** [Revisão de Administração Pública — Anulação, revogação e convalidação](semana_02_estudo.md#s2-d2-revisao-desfazimento).

#### Comentário Extra Dia 2.9

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Retirada de ato válido por conveniência descreve revogação, não correção de vício.
- **B)** Correta. Convalidação pressupõe vício sanável e ausência de lesão ao interesse público e a terceiros.
- **C)** Incorreta. Vício insanável não pode ser corrigido por simples convalidação.
- **D)** Incorreta. Má-fé e decadência não constituem os requisitos ensinados para convalidar.

**Conceito:** pressupostos da convalidação.

**Pegadinha:** tratar convalidação como cura universal para qualquer ilegalidade.

**Como pensar:** teste três pontos: vício sanável, interesse público preservado e nenhum prejuízo a terceiro.

**Referência:** [Revisão de Administração Pública — Anulação, revogação e convalidação](semana_02_estudo.md#s2-d2-revisao-desfazimento).

#### Comentário Extra Dia 2.10

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A Lei nº 9.784/1999 estabelece limite temporal para atos favoráveis, ressalvada má-fé.
- **B)** Incorreta. Em efeitos patrimoniais contínuos, o marco ensinado é o primeiro pagamento.
- **C)** Incorreta. O prazo indicado na revisão é de cinco anos e a má-fé constitui ressalva.
- **D)** Correta. A opção reúne prazo, termo inicial comum, regra para efeitos contínuos e exceção de má-fé.

**Conceito:** decadência do direito de anular ato favorável no art. 54.

**Pegadinha:** aderir à frase absoluta de que todo ato ilegal pode ser anulado a qualquer tempo.

**Como pensar:** identifique efeito favorável, conte cinco anos do ato ou do primeiro pagamento e verifique má-fé comprovada.

**Referência:** [Revisão de Administração Pública — Anulação, revogação e convalidação](semana_02_estudo.md#s2-d2-revisao-desfazimento).

#### Comentário Extra Dia 2.11

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Acesso à informação não revoga os deveres de proteção de dados.
- **B)** Incorreta. A LGPD admite tratamento pelo Poder Público orientado a finalidade e interesse públicos.
- **C)** Correta. Transparência e proteção coexistem, afastando tanto exposição irrestrita quanto sigilo automático.
- **D)** Incorreta. Um caso pode demandar aplicação harmonizada das duas leis.

**Conceito:** articulação entre LAI e LGPD.

**Pegadinha:** apresentar as leis como comandos mutuamente excludentes.

**Como pensar:** localize a informação pública devida e proteja os dados pessoais além do necessário para essa finalidade.

**Referência:** [Revisão de Administração Pública — LAI x LGPD](semana_02_estudo.md#s2-d2-revisao-lai-lgpd).

#### Comentário Extra Dia 2.12

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A redação vigente exige conduta dolosa tipificada; mera irregularidade não completa esse enquadramento.
- **B)** Incorreta. Nem toda ilegalidade é improbidade contra princípios.
- **C)** Incorreta. A revisão também contempla enriquecimento ilícito e tipos contra princípios, não apenas lesão ao erário.
- **D)** Incorreta. Culpa leve e inconveniência, sem tipo doloso, não atendem ao núcleo estudado.

**Conceito:** dolo e tipicidade na improbidade administrativa.

**Pegadinha:** usar “improbidade” como rótulo automático para qualquer falha administrativa.

**Como pensar:** procure simultaneamente conduta prevista em lei e dolo; se faltar um deles, não conclua automaticamente pela improbidade.

**Referência:** [Revisão de Administração Pública — Improbidade administrativa](semana_02_estudo.md#s2-d2-revisao-improbidade).

#### Comentário Extra Dia 2.13

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Na dispensa, a competição é possível em tese, embora a lei autorize contratação direta.
- **B)** Incorreta. Pregão é modalidade, e exclusividade não é critério de julgamento.
- **C)** Incorreta. Retirar uma licitação não elimina processo, motivação e controle da contratação.
- **D)** Correta. Inviabilidade de competição caracteriza o núcleo da inexigibilidade, observados os requisitos legais.

**Conceito:** distinção entre dispensa e inexigibilidade.

**Pegadinha:** chamar toda contratação direta de dispensa.

**Como pensar:** pergunte se existe competição viável; se não existe, examine inexigibilidade, sem dispensar o processo.

**Referência:** [Revisão de Administração Pública — Licitação e contratação direta](semana_02_estudo.md#s2-d2-revisao-licitacao).

#### Comentário Extra Dia 2.14

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contratação direta não significa ausência de instrução, justificativa ou controle.
- **B)** Incorreta. Modalidade organiza o procedimento; critério de julgamento não é seu sinônimo.
- **C)** Correta. A alternativa preserva o processo e cita duas modalidades previstas no rol estudado.
- **D)** Incorreta. Concurso e leilão também aparecem entre as modalidades da Lei nº 14.133/2021.

**Conceito:** contratação direta e modalidades licitatórias.

**Pegadinha:** confundir ausência de competição no certame com ausência de procedimento administrativo.

**Como pensar:** separe três caixas: hipótese de contratação direta, modalidade e critério de julgamento.

**Referência:** [Revisão de Administração Pública — Licitação e contratação direta](semana_02_estudo.md#s2-d2-revisao-licitacao).

#### Comentário Extra Dia 2.15

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Responsabilidade objetiva não elimina a necessidade de dano e nexo causal.
- **B)** Incorreta. O regresso contra o agente exige dolo ou culpa segundo o núcleo constitucional revisado.
- **C)** Incorreta. A regra alcança pessoas jurídicas de direito público e prestadoras de serviço público, não apenas uma espécie societária.
- **D)** Correta. Conduta estatal, dano e nexo sustentam a pretensão da vítima, com regresso nas condições indicadas.

**Conceito:** responsabilidade civil objetiva do Estado e ação regressiva.

**Pegadinha:** traduzir “objetiva” como pagamento automático sem elementos causais.

**Como pensar:** retire apenas a necessidade de provar culpa estatal perante a vítima, não conduta, dano ou nexo.

**Referência:** [Revisão de Administração Pública — Responsabilidade civil do Estado](semana_02_estudo.md#s2-d2-revisao-responsabilidade).

#### Comentário Extra Dia 2.16

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A frase limita o contexto a ponto a ponto e usa possibilidade, não obrigação para toda rede.
- **B)** Correta. A interpretação conserva o alcance de “em enlaces” e a modalidade expressa por “pode”.
- **C)** Incorreta. “Pode” não indica proibição; expressa possibilidade ou permissão.
- **D)** Incorreta. O enunciado não transforma uma aplicação possível em dever universal.

**Conceito:** quantificadores, modalidade e alcance do enunciado.

**Pegadinha:** trocar “pode” por “deve” e retirar a condição ponto a ponto.

**Como pensar:** sublinhe contexto, quantificador e força verbal antes de avaliar cada paráfrase.

**Referência:** [Revisão de Português — Quantificadores e alcance](semana_02_estudo.md#s2-d2-revisao-quantificadores).

#### Comentário Extra Dia 2.17

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. “Entretanto” não indica causa, e “esse” recupera conteúdo anterior.
- **B)** Incorreta. O conector não conclui; o pronome retoma a ampliação, não o planejamento.
- **C)** Correta. Há ressalva entre maior espaço e manutenção do planejamento, com retomada coesiva adequada.
- **D)** Incorreta. O trecho afirma expressamente que a necessidade não foi eliminada.

**Conceito:** coesão referencial e relação adversativa.

**Pegadinha:** ler apenas a primeira oração e ignorar a negação introduzida após o conector.

**Como pensar:** identifique o valor de “entretanto” e substitua “esse fato” por seu antecedente para testar o sentido.

**Referência:** [Revisão de Português — Coesão e relação lógica](semana_02_estudo.md#s2-d2-revisao-coesao).

#### Comentário Extra Dia 2.18

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A vírgula separa indevidamente o sujeito “Os endereços privados” do verbo “podem”.
- **B)** Incorreta. A vírgula rompe o vínculo entre “encaminha” e seu complemento “destinos remotos”.
- **C)** Incorreta. A vírgula foi posicionada entre a negação e o verbo, sem função sintática legítima.
- **D)** Correta. As vírgulas isolam a expressão explicativa “no IPv4 sobre Ethernet”.

**Conceito:** pontuação de termos essenciais e expressões explicativas.

**Pegadinha:** inserir vírgula onde ocorre pausa oral, mesmo separando sujeito, verbo ou complemento.

**Como pensar:** preserve primeiro o esqueleto sujeito–verbo–complemento e isole apenas o trecho explicativo removível.

**Referência:** [Revisão de Português — Pontuação](semana_02_estudo.md#s2-d2-revisao-pontuacao).

#### Comentário Extra Dia 2.19

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não há crase antes do verbo “encaminhar”.
- **B)** Correta. A preposição exigida por “aplica-se a” encontra o artigo plural de “as sub-redes”, formando “às”.
- **C)** Incorreta. “Transmitir” é verbo e não admite artigo feminino que forme crase.
- **D)** Incorreta. “Revisar” também é verbo, logo o acento grave não se justifica.

**Conceito:** encontro entre preposição `a` e artigo feminino `a` ou `as`.

**Pegadinha:** colocar crase antes de infinitivo por perceber apenas o som da preposição.

**Como pensar:** substitua o termo posterior por um masculino; se surgir “ao”, há base para “à” diante do feminino nominal.

**Referência:** [Revisão de Português — Crase aplicada](semana_02_estudo.md#s2-d2-revisao-crase).

#### Comentário Extra Dia 2.20

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. “Ainda que” preserva a concessão, e “é possível” mantém a modalidade de “pode”.
- **B)** Incorreta. A opção troca concessão por causa e possibilidade por certeza absoluta.
- **C)** Incorreta. Afirma pertencimento à RFC 1918, invertendo a condição original.
- **D)** Incorreta. Cria implicação não autorizada e associa bloco especial necessariamente à RFC 1918.

**Conceito:** equivalência em reescrita técnica.

**Pegadinha:** conservar parte do vocabulário, mas alterar negação, conector ou força modal.

**Como pensar:** compare sujeito, negação, relação concessiva e grau de certeza em cada versão.

**Referência:** [Revisão de Português — Reescrita técnica](semana_02_estudo.md#s2-d2-revisao-reescrita).

---
# Dia 3 — Protocolos e serviços de rede

**Base usada:** `semana_02/semana_02_estudo.md`, Dia 3 — Protocolos e Serviços de Rede.

## Questões principais

### Questão 1

Sobre protocolo, porta e socket, assinale a afirmativa correta.

A) A porta de transporte é um identificador de 16 bits usado por TCP ou UDP para que o sistema operacional entregue os dados à aplicação adequada.
B) Uma porta de transporte é um conector físico pertencente ao roteador de borda.
C) Uma porta só pode ser usada por processos servidores; clientes não possuem portas de origem.
D) Um socket é identificado somente pelo endereço IP de destino, sem relação com porta ou transporte.

### Questão 2

Em uma compra realizada por meio de uma aplicação web, o cliente recebe um ACK TCP após enviar dados. Esse ACK significa que:

A) o TCP dispensou o estabelecimento de conexão antes do envio de dados.
B) a aplicação preservará obrigatoriamente as fronteiras de cada mensagem enviada.
C) o transporte confirmou o recebimento de bytes, mas não a aprovação semântica da compra pela aplicação.
D) o servidor concluiu que o usuário está autorizado a realizar a operação.

### Questão 3

Assinale a alternativa correta acerca do UDP.

A) O UDP ordena e retransmite datagramas automaticamente antes de entregá-los à aplicação.
B) O UDP não oferece conexão, confirmação ou retransmissão nativas, embora a aplicação possa construir mecanismos próprios.
C) O UDP inicia cada comunicação com o handshake SYN, SYN-ACK e ACK.
D) Nenhuma aplicação sobre UDP pode oferecer entrega confiável.

### Questão 4

Ao afirmar que HTTP é stateless, pretende-se dizer que:

A) uma requisição HTTP não pode conter cabeçalhos nem corpo.
B) HTTP não pode ser empregado com autenticação de usuários.
C) o servidor deve apagar todo dado da aplicação ao responder a uma requisição.
D) o protocolo não exige manter sessão entre requisições, embora a aplicação possa criar estado com cookies, tokens ou sessões.

### Questão 5

Assinale a afirmativa tecnicamente correta sobre HTTPS.

A) HTTPS garante que todo conteúdo publicado é verdadeiro e livre de vulnerabilidades.
B) HTTPS corresponde a HTTP protegido por TLS; a validação adequada do certificado ajuda a autenticar o servidor, sem garantir a qualidade do conteúdo da aplicação.
C) HTTPS substitui o controle de autorização da aplicação, pois o certificado identifica qualquer usuário.
D) HTTPS usa obrigatoriamente UDP e não pode operar sobre TCP.

### Questão 6

Sobre métodos e respostas HTTP, assinale a alternativa correta.

A) HEAD solicita os cabeçalhos de uma representação sem o corpo da resposta.
B) POST é reservado exclusivamente para obter uma representação, sem submeter dados.
C) Códigos 4xx indicam, necessariamente, falha interna do servidor.
D) Códigos 3xx significam sempre que o recurso foi removido definitivamente.

### Questão 7

No DNS, qual registro indica os servidores de correio de um domínio?

A) A
B) AAAA
C) CNAME
D) MX

### Questão 8

Uma estação envia uma consulta recursiva ao seu resolvedor DNS. Nessa situação, é correto afirmar que o resolvedor:

A) só pode responder depois de consultar diretamente todos os servidores autoritativos da Internet.
B) devolve ao cliente apenas a lista de servidores raiz, sem buscar resposta.
C) pode responder com dados válidos do cache, respeitado o TTL, ou buscar a resposta final usando referências iterativas.
D) transforma automaticamente qualquer registro A em um registro MX.

### Questão 9

Sobre o transporte do DNS clássico, assinale a alternativa correta.

A) DNS utiliza exclusivamente 53/UDP, inclusive em transferências de zona.
B) DNS utiliza exclusivamente 53/TCP, pois consultas não podem ser datagramas.
C) DNS clássico utiliza 53/UDP e 53/TCP; TCP pode ser necessário, por exemplo, em transferências de zona ou em determinadas respostas.
D) DNS clássico exige 443/TCP para consultas de nomes.

### Questão 10

Quanto a formas encapsuladas de DNS, assinale a afirmativa correta.

A) DNS sobre TLS elimina o uso de TLS e opera necessariamente em 53/UDP.
B) DNS sobre HTTPS é sinônimo de transferência de zona por TCP.
C) Todo DNS, sem exceção, deve usar a porta 53 para ser válido.
D) DNS sobre TLS usa, por padrão, a porta 853, e DNS sobre HTTPS usa HTTPS, normalmente na porta 443.

### Questão 11

Um cliente sem configuração de rede inicia a obtenção dinâmica de parâmetros por DHCP. A sequência clássica DORA é:

A) DHCPDISCOVER, DHCPOFFER, DHCPREQUEST e DHCPACK.
B) DHCPREQUEST, DHCPACK, DHCPDISCOVER e DHCPOFFER.
C) DHCPOFFER, DHCPDISCOVER, DHCPACK e DHCPREQUEST.
D) DHCPDISCOVER, DHCPACK, DHCPOFFER e DHCPREQUEST.

### Questão 12

Sobre as portas clássicas do DHCP, assinale a alternativa correta.

A) O servidor DHCP usa 68/TCP e o cliente usa 67/TCP.
B) O servidor DHCP usa 67/UDP e o cliente usa 68/UDP.
C) Cliente e servidor DHCP usam 53/UDP, pois o serviço resolve nomes.
D) O cliente DHCP recebe a concessão em 443/TCP, dentro de HTTPS.

### Questão 13

Em uma organização, o servidor DHCP está na VLAN 10 e os clientes da VLAN 20 não recebem endereços. Mantido o roteamento entre as VLANs, a medida compatível com a arquitetura é:

A) substituir o DHCP por um registro DNS A em cada estação.
B) configurar um proxy reverso para encaminhar broadcasts DHCP.
C) aplicar PAT no firewall para converter DHCP em HTTPS.
D) configurar um DHCP relay na rede dos clientes e um escopo compatível no servidor central.

### Questão 14

Assinale a associação correta entre protocolos de correio eletrônico.

A) POP3 é o protocolo típico para transferência de mensagens entre servidores de correio.
B) SMTP é usado na submissão e na transferência de mensagens, enquanto POP3 e IMAP são usados para acesso à caixa postal.
C) IMAP é o protocolo que resolve registros MX antes do envio de e-mail.
D) SMTP é destinado exclusivamente à leitura sincronizada de pastas pelo destinatário.

### Questão 15

Em relação às portas de SMTP, a associação correta é:

A) 25/TCP é a porta de acesso POP3 e 110/TCP é a de relay SMTP.
B) 587/UDP é a porta padrão de consultas SNMP.
C) 587/TCP é usada tipicamente para submissão pelo cliente, e 25/TCP para transferência entre servidores.
D) 465/UDP é a porta obrigatória de toda transferência entre servidores SMTP.

### Questão 16

Um usuário precisa ler suas mensagens no telefone e no notebook, mantendo pastas e marcações sincronizadas no servidor. O protocolo mais adequado é:

A) IMAP.
B) SMTP.
C) FTP.
D) Telnet.

### Questão 17

Uma pessoa redige uma mensagem, envia-a ao servidor de correio e depois a consulta em dois dispositivos, preservando o estado da caixa postal. A combinação coerente é:

A) SMTP para submissão/transferência e IMAP para acesso sincronizado à caixa postal.
B) POP3 para submissão e SMTP para sincronização de pastas.
C) DNS para submissão e DHCP para leitura das mensagens.
D) IMAP para transferência entre servidores e FTP para leitura da caixa postal.

### Questão 18

Sobre o FTP clássico, assinale a alternativa correta.

A) FTP protege automaticamente credenciais e conteúdo com TLS em qualquer modo.
B) FTP usa uma única conexão, obrigatoriamente em 21/TCP, tanto para controle quanto para dados.
C) FTP usa apenas UDP para reduzir latência de transferências.
D) FTP separa a conexão de controle, normalmente em 21/TCP, da conexão de dados; no modo passivo, a porta de dados é informada pelo servidor.

### Questão 19

No modo passivo de FTP, é correto afirmar que:

A) o servidor sempre inicia a conexão de dados a partir de 20/TCP para o cliente.
B) o cliente inicia a conexão de dados para uma porta informada pelo servidor; por isso, a transferência não fica limitada à porta 20.
C) a conexão de controle deixa de existir e é substituída por DNS.
D) o tráfego de dados passa obrigatoriamente a usar UDP/21.

### Questão 20

Uma equipe precisa configurar FTPS explícito com proteção também para o canal de dados. Qual procedimento está correto?

A) Conectar-se por SSH na porta 22, pois FTPS é o mesmo protocolo que SFTP.
B) Abrir 990/TCP e assumir que não haverá conexão de dados separada.
C) Iniciar o controle em 21/TCP, negociar `AUTH TLS` e usar `PBSZ 0` seguido de `PROT P` para solicitar proteção privada dos dados.
D) Usar apenas `PROT P` em 53/UDP, pois DNS fornece a criptografia do FTP.

### Questão 21

Sobre FTPS implícito, assinale a afirmativa tecnicamente adequada.

A) É outro nome para SFTP e, portanto, usa obrigatoriamente 22/TCP.
B) Transfere todos os dados somente por 989/TCP, independentemente de o modo ser ativo ou passivo.
C) A IANA registra 990/TCP para o controle e 989/TCP para dados, mas FTPS preserva canais separados e portas de dados podem ser negociadas conforme o modo e a configuração.
D) Exige `AUTH TLS` após a abertura de 21/TCP, exatamente como definição de FTPS implícito.

### Questão 22

Uma rotina de transferência de arquivos deve reutilizar uma infraestrutura SSH já configurada com autenticação por chave pública. A escolha coerente é:

A) SFTP, pois é o SSH File Transfer Protocol sobre SSH, normalmente em 22/TCP.
B) FTP clássico, pois já cifra os arquivos por padrão.
C) FTPS explícito, pois é o subsistema de arquivos do SSH.
D) Telnet, pois fornece canal criptografado para arquivos.

### Questão 23

Para administração remota de um servidor com autenticação, integridade e confidencialidade do canal, deve-se preferir:

A) HTTP na porta 80/TCP, pois substitui terminal remoto.
B) DNS em 53/UDP, pois registra o endereço do servidor.
C) Telnet em 23/TCP, pois cifra as credenciais nativamente.
D) SSH, normalmente em 22/TCP, com validação da chave do host e proteção das chaves privadas.

### Questão 24

Assinale a afirmativa correta sobre Telnet.

A) Telnet é um protocolo de transferência de arquivos protegido por TLS.
B) Telnet oferece terminal remoto, mas não fornece a proteção criptográfica esperada para credenciais e conteúdo; sua porta padrão é 23/TCP.
C) Telnet é a versão segura de LDAP em 636/TCP.
D) Telnet sincroniza relógios por 123/UDP.

### Questão 25

Na arquitetura SNMP, assinale a alternativa correta.

A) O agente consulta periodicamente o gerente para obter as regras de navegação web.
B) O gerente pode consultar objetos de um agente por meio de MIB/OID, e o agente pode emitir uma trap como notificação.
C) A MIB é a conexão de dados do FTP, e OID é a porta de origem do cliente.
D) Uma trap é, por definição, uma resposta confirmada a toda consulta GET.

### Questão 26

Sobre SNMP, assinale a alternativa correta.

A) Consultas a agentes ocorrem tipicamente em 162/TCP, e traps chegam em 161/TCP.
B) SNMPv1 e SNMPv2c oferecem, obrigatoriamente, a mesma proteção criptográfica de um SNMPv3 bem configurado.
C) SNMP serve apenas para transferir arquivos entre gerente e agente.
D) Consultas e respostas ao agente usam tradicionalmente 161/UDP, notificações chegam ao gerente em 162/UDP, e o SNMPv3 pode prover autenticação e privacidade conforme a configuração.

### Questão 27

Sobre LDAP, assinale a alternativa correta.

A) LDAP é um protocolo de banco relacional que exige consultas SQL.
B) LDAP resolve nomes de domínio por registros A e AAAA.
C) LDAP acessa diretórios hierárquicos com entradas identificadas por DN e atributos, permitindo operações como bind e search.
D) LDAP é um protocolo de sincronização de relógio sobre UDP.

### Questão 28

Assinale a afirmativa correta sobre LDAP e proteção do acesso.

A) LDAP pode participar de um fluxo de autenticação, mas não decide isoladamente toda a autorização; LDAP em 389/TCP pode usar STARTTLS e LDAPS usa usualmente 636/TCP.
B) LDAP em 389/TCP é sempre cifrado, mesmo sem negociação TLS.
C) LDAPS em 636/UDP é a única forma de consultar diretórios.
D) A existência de uma conta LDAP autoriza automaticamente qualquer ação em toda aplicação.

### Questão 29

Em uma rede corporativa, um componente recebe solicitações dos navegadores dos empregados e aplica política de navegação, autenticação e cache em nome desses clientes. Esse componente é um:

A) servidor DNS autoritativo.
B) NAT básico.
C) proxy reverso.
D) proxy direto.

### Questão 30

Um portal público coloca um componente diante dos servidores de aplicação para terminar TLS, distribuir carga e ocultar a topologia interna. Trata-se de:

A) proxy reverso.
B) proxy direto.
C) DHCP relay.
D) resolvedor DNS recursivo.

### Questão 31

Qual alternativa diferencia corretamente proxy e NAT?

A) NAT cria e interpreta obrigatoriamente sessões HTTP, enquanto proxy apenas troca endereços IP.
B) Um proxy pode intermediar a comunicação em nome de um extremo, enquanto NAT traduz campos de endereçamento no tráfego encaminhado sem necessariamente encerrar a sessão de aplicação.
C) Proxy e NAT são sinônimos e fornecem sempre a mesma proteção.
D) NAT cifra o conteúdo, enquanto proxy apenas converte nomes em endereços IP.

### Questão 32

Em uma questão que contrapõe NAT básico e PAT/NAPT, a diferença decisiva é que:

A) NAT básico resolve nomes e PAT/NAPT entrega endereços via broadcast.
B) PAT/NAPT opera somente em IPv6, enquanto NAT básico opera somente em IPv4.
C) NAT básico traduz endereços IP sem traduzir identificadores de transporte, enquanto PAT/NAPT também traduz portas para multiplexar fluxos.
D) PAT/NAPT substitui a necessidade de gateway padrão.

### Questão 33

Dois hosts privados usam a mesma porta de origem 52000 para acessar o mesmo site externo, mas compartilham um único endereço público. Como o PAT/NAPT pode distinguir os retornos?

A) Eliminando as portas de origem de ambos os fluxos antes de sair da rede.
B) Convertendo o endereço público em um registro MX para cada host.
C) Criando mapeamentos com portas públicas distintas e associando cada retorno ao fluxo interno correspondente.
D) Fazendo o resolvedor DNS escolher um endereço IPv6 privado para cada host.

### Questão 34

Assinale a afirmativa correta sobre NAT/PAT.

A) NAT/PAT cifra automaticamente os dados, dispensando TLS.
B) NAT/PAT não autentica usuários, não criptografa o tráfego e não substitui um firewall.
C) PAT/NAPT impede, por definição, todo acesso indevido vindo da Internet.
D) NAT básico é um sinônimo de proxy reverso de aplicação.

### Questão 35

Para corrigir horários divergentes em logs distribuídos e evitar problemas ligados à validade temporal de certificados, o serviço mais diretamente relacionado é:

A) NTP em 123/UDP, que sincroniza relógios, sem definir por si só o fuso horário exibido.
B) DNS em 53/UDP, que escolhe a hora do servidor autoritativo.
C) DHCP em 67/TCP, que determina o horário de verão.
D) FTP em 21/TCP, que transfere arquivos de log em ordem temporal.

### Questão 36

Sobre portas conhecidas e o registro da IANA, assinale a alternativa correta.

A) Um serviço HTTP não pode ser configurado na porta 8080, porque a IANA impede a abertura dessa porta.
B) Todo tráfego na porta 443 é necessariamente legítimo e criptografado de forma correta.
C) A porta 22 identifica de modo infalível SSH, independentemente da configuração do host.
D) O registro da IANA define associações convencionais de nomes e portas, mas serviços podem ser configurados em outras portas e a porta isolada não comprova conteúdo, legitimidade ou segurança.

### Questão 37

Uma estação recém-conectada depende de DHCP e acessará um portal pelo nome. Qual etapa deve ocorrer primeiro para que ela obtenha IP, prefixo, gateway e servidor DNS automaticamente?

A) A concessão DHCP.
B) A tradução PAT no firewall de borda.
C) A negociação TLS com o portal.
D) A consulta ao servidor autoritativo DNS externo.

### Questão 38

Uma estação consegue abrir `https://198.51.100.40`, mas falha ao tentar acessar `portal.example` porque o nome não é resolvido. O primeiro bloco de investigação mais indicado é:

A) NTP, pois o IP de destino foi alcançado.
B) FTP passivo, pois o navegador usa duas conexões.
C) DNS, verificando servidor configurado, respostas, cache e registros.
D) IMAP, verificando a sincronização de mensagens.

### Questão 39

Em um diagnóstico, o nome do portal é resolvido corretamente, mas a conexão tradicional para 443/TCP não é estabelecida. A conclusão inicial mais adequada é:

A) o DHCP é necessariamente o único componente defeituoso.
B) o registro MX do domínio está incorreto.
C) o DNS não conseguiu converter o nome em endereço.
D) devem ser verificados rota, firewall, NAT/PAT ou o próprio serviço, sem atribuir a falha automaticamente ao DNS.

### Questão 40

Considere o acesso tradicional a um portal HTTPS publicado por proxy reverso. Após a resolução do nome, a sequência tecnicamente compatível é:

A) HTTP em claro na porta 80, seguido de DHCPACK e, por fim, troca de endereço DNS.
B) abertura de TCP para 443, negociação TLS, tráfego HTTP dentro do canal protegido e possível encaminhamento pelo proxy reverso ao servidor de aplicação.
C) envio de uma trap SNMP, seguido de DHCPOFFER e abertura de Telnet.
D) negociação de FTP passivo, que substitui o TLS e o HTTP.

### Questão 41

Dois clientes podem acessar simultaneamente o mesmo servidor em 443/TCP porque:

A) a porta 443 só pode receber uma conexão por vez, e os clientes dividem o mesmo socket.
B) os clientes usam combinações distintas de IP e/ou porta de origem, que compõem com destino e protocolo a identificação da conexão TCP.
C) o servidor elimina os números de porta de origem antes de aceitar as conexões.
D) TCP identifica conexões somente pelo nome DNS consultado pelo cliente.

### Questão 42

Um analista observa pacotes destinados à porta 443. A inferência correta é:

A) há prova de que a aplicação está livre de vulnerabilidades.
B) está comprovado que todo conteúdo é legítimo e que o certificado foi validado pelo cliente.
C) o tráfego é obrigatoriamente HTTP/2 sobre TCP.
D) a porta sugere uma convenção de HTTPS, mas não prova sozinha o protocolo efetivo, a legitimidade do conteúdo nem a segurança da aplicação.

### Questão 43

Sobre HTTP/3, assinale a alternativa correta.

A) HTTP/3 utiliza QUIC sobre UDP, normalmente associado à porta 443, diferindo do uso de TCP por HTTP/1.1 e HTTP/2.
B) HTTP/3 é apenas FTP com outro nome e usa 21/TCP.
C) HTTP/3 elimina a necessidade de TLS ao usar UDP.
D) HTTP/3 só pode funcionar após uma concessão SNMP.

### Questão 44

Qual registro DNS é empregado tipicamente para resolução reversa, isto é, de um endereço para um nome?

A) NS
B) SOA
C) PTR
D) TXT

### Questão 45

Assinale a afirmativa correta sobre autoridade e cache DNS.

A) Um servidor autoritativo só pode responder com registros obtidos do cache de outro servidor.
B) O TTL define a data de expiração do domínio e a disponibilidade do servidor autoritativo.
C) Um servidor autoritativo responde pelos dados publicados na zona sob sua autoridade; um resolvedor pode reutilizar dados em cache durante o TTL aplicável.
D) Qualquer resposta armazenada em cache é automaticamente autoritativa para toda a Internet.

### Questão 46

Uma estação apresenta endereço 169.254.x.x, não possui gateway configurado e deveria receber configuração automaticamente. O primeiro foco de diagnóstico é:

A) a concessão DHCP, incluindo alcance do servidor/relay e escopo disponível.
B) a transferência de zona DNS por TCP.
C) a configuração de TLS implícito no IMAP.
D) o modo passivo do FTP.

### Questão 47

Qual cenário justifica de modo mais adequado a escolha de UDP, sem reduzir a decisão à frase “UDP é mais rápido”?

A) Uma aplicação precisa de um fluxo de bytes ordenado e quer que o transporte retransmita perdas nativamente.
B) Uma aplicação troca mensagens curtas e independentes, valoriza baixa latência ou multicast e pode tratar perdas conforme sua própria lógica.
C) Um serviço exige handshake SYN, SYN-ACK e ACK antes de cada datagrama.
D) Um sistema precisa que a camada de transporte preserve necessariamente as fronteiras de todas as mensagens em um fluxo TCP.

### Questão 48

Assinale a propriedade corretamente atribuída ao TCP.

A) O TCP envia datagramas independentes sem estado de conexão e sem confirmações.
B) O TCP garante que uma operação de negócio, como pagamento, foi gravada definitivamente no banco de dados.
C) O TCP é incompatível com controle de fluxo e de congestionamento.
D) O TCP fornece fluxo de bytes ordenado e confiável, usando sequência, confirmações, temporizadores e retransmissões, mas não preserva fronteiras de mensagens da aplicação.

### Questão 49

Em uma investigação, os logs de dois servidores têm horários incompatíveis e certificados passam a parecer inválidos em uma das máquinas. A ação mais diretamente relacionada ao problema é:

A) verificar a sincronização NTP e as fontes de tempo, pois NTP mantém referência temporal coerente para logs e validações dependentes de horário.
B) trocar o fuso horário no DNS para que os registros A sejam recalculados.
C) substituir DHCP por POP3, pois ambos usam mensagens de confirmação.
D) habilitar FTP ativo para ordenar os eventos registrados.

### Questão 50

Uma estação recém-conectada acessa um portal externo cujo endereço público é compartilhado por vários usuários internos e cuja publicação usa proxy reverso. Considerando o fluxo principal, assinale a sequência compatível.

A) DNS entrega IP e gateway; SMTP traduz portas; FTP negocia TLS; NTP publica o portal.
B) DHCP entrega parâmetros; DNS resolve o nome; o gateway encaminha o tráfego e o PAT pode traduzir IP/porta; TLS protege HTTP, que pode ser recebido por um proxy reverso.
C) IMAP entrega a máscara; LDAP resolve o nome; Telnet cifra o HTTP; NAT organiza a caixa postal.
D) SNMP atribui endereço IP; POP3 faz o roteamento; FTP substitui o proxy reverso.
## Gabarito do Dia 3

### Gabarito das questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | A |
| 2 | C |
| 3 | B |
| 4 | D |
| 5 | B |
| 6 | A |
| 7 | D |
| 8 | C |
| 9 | C |
| 10 | D |
| 11 | A |
| 12 | B |
| 13 | D |
| 14 | B |
| 15 | C |
| 16 | A |
| 17 | A |
| 18 | D |
| 19 | B |
| 20 | C |
| 21 | C |
| 22 | A |
| 23 | D |
| 24 | B |
| 25 | B |
| 26 | D |
| 27 | C |
| 28 | A |
| 29 | D |
| 30 | A |
| 31 | B |
| 32 | C |
| 33 | C |
| 34 | B |
| 35 | A |
| 36 | D |
| 37 | A |
| 38 | C |
| 39 | D |
| 40 | B |
| 41 | B |
| 42 | D |
| 43 | A |
| 44 | C |
| 45 | C |
| 46 | A |
| 47 | B |
| 48 | D |
| 49 | A |
| 50 | B |

## Comentários do Dia 3

### Comentário da Questão 1

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. TCP e UDP usam portas de 16 bits para permitir a entrega dos dados ao processo adequado no host.
- **B)** Incorreta. Porta de transporte é um identificador lógico, não um conector físico de roteador.
- **C)** Incorreta. Clientes também usam portas de origem, em geral escolhidas dinamicamente pelo sistema operacional.
- **D)** Incorreta. Um socket envolve endereço, porta e protocolo de transporte; não se reduz ao IP de destino.

**Conceito:** porta de transporte, demultiplexação e identificação de sockets.

**Pegadinha:** confundir porta lógica TCP/UDP com interface física ou omitir os identificadores da origem.

**Como pensar:** se a questão trata da entrega a uma aplicação, procure IP, protocolo de transporte e porta, não conectores do equipamento.

**Referência:** [1. Protocolo, serviço, porta e socket](semana_02_estudo.md#s2-d3-protocolo-porta).

### Comentário da Questão 2

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O TCP estabelece conexão antes da troca normal de dados.
- **B)** Incorreta. TCP entrega um fluxo de bytes e não preserva, por si só, as fronteiras das mensagens da aplicação.
- **C)** Correta. O ACK confirma bytes no nível de transporte, sem afirmar que a compra foi aprovada pela aplicação.
- **D)** Incorreta. Autorização é decisão da aplicação e não decorre de uma confirmação TCP.

**Conceito:** alcance da confiabilidade e das confirmações do TCP.

**Pegadinha:** atribuir ao ACK um significado de negócio que ele não possui.

**Como pensar:** identifique a camada: o TCP confirma transporte de bytes; a aplicação confirma o resultado da operação.

**Referência:** [2.1 TCP: orientado à conexão e confiável](semana_02_estudo.md#s2-d3-tcp-udp).

### Comentário da Questão 3

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. UDP não oferece ordenação nem retransmissão automáticas.
- **B)** Correta. O protocolo envia datagramas sem conexão e sem confirmação nativa, mas a aplicação pode acrescentar esses mecanismos.
- **C)** Incorreta. SYN, SYN-ACK e ACK formam o handshake clássico do TCP, não do UDP.
- **D)** Incorreta. Uma aplicação sobre UDP pode implementar confiabilidade acima do transporte.

**Conceito:** características do UDP e responsabilidades da aplicação.

**Pegadinha:** transformar a ausência de confiabilidade nativa em impossibilidade de obter confiabilidade na aplicação.

**Como pensar:** separe o que o UDP fornece diretamente do que pode ser implementado em uma camada superior.

**Referência:** [2.2 UDP: datagramas sem conexão](semana_02_estudo.md#s2-d3-tcp-udp).

### Comentário da Questão 4

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Requisições HTTP podem conter cabeçalhos e, quando aplicável, corpo.
- **B)** Incorreta. Aplicações HTTP podem usar autenticação e manter estado por mecanismos próprios.
- **C)** Incorreta. Stateless não exige apagar dados da aplicação após cada resposta.
- **D)** Correta. HTTP não exige sessão persistente entre requisições, embora cookies, tokens e sessões possam manter estado.

**Conceito:** ausência de estado obrigatório no protocolo HTTP.

**Pegadinha:** interpretar stateless como proibição absoluta de sessão ou de armazenamento pela aplicação.

**Como pensar:** diferencie a semântica independente das requisições HTTP do estado criado pela aplicação.

**Referência:** [3.1 HTTP](semana_02_estudo.md#s2-d3-http-https).

### Comentário da Questão 5

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. TLS protege o canal, mas não comprova a veracidade do conteúdo nem elimina vulnerabilidades da aplicação.
- **B)** Correta. HTTPS é HTTP sobre TLS, e a validação adequada do certificado ajuda a autenticar o servidor.
- **C)** Incorreta. Certificado do servidor não identifica automaticamente o usuário nem substitui autorização.
- **D)** Incorreta. HTTP/1.1 e HTTP/2 sobre HTTPS usam normalmente TCP; HTTP/3 é a exceção baseada em QUIC/UDP.

**Conceito:** garantias e limites do HTTPS.

**Pegadinha:** tratar canal criptografado como prova de legitimidade integral do conteúdo ou autorização do usuário.

**Como pensar:** associe TLS a autenticação do servidor, confidencialidade e integridade em trânsito, respeitando seus limites.

**Referência:** [3.2 HTTPS](semana_02_estudo.md#s2-d3-http-https).

### Comentário da Questão 6

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. HEAD solicita os cabeçalhos da representação sem o corpo da resposta.
- **B)** Incorreta. POST é usado para submeter dados para processamento, não exclusivamente para obter representação.
- **C)** Incorreta. Códigos 4xx se relacionam à requisição do cliente; falhas do servidor pertencem à classe 5xx.
- **D)** Incorreta. A classe 3xx indica redirecionamento e não significa sempre remoção definitiva.

**Conceito:** métodos HTTP e classes de códigos de estado.

**Pegadinha:** trocar as funções de HEAD e POST ou confundir as classes 3xx, 4xx e 5xx.

**Como pensar:** associe primeiro o método à ação e depois o primeiro algarismo do status à sua classe.

**Referência:** [3.1 HTTP](semana_02_estudo.md#s2-d3-http-https).

### Comentário da Questão 7

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O registro A associa um nome a um endereço IPv4.
- **B)** Incorreta. O registro AAAA associa um nome a um endereço IPv6.
- **C)** Incorreta. CNAME define um alias para outro nome canônico.
- **D)** Correta. MX indica os servidores responsáveis pelo correio de um domínio.

**Conceito:** tipos de registros DNS.

**Pegadinha:** escolher registros de endereço ou alias quando o enunciado pede infraestrutura de e-mail.

**Como pensar:** relacione a finalidade pedida à sigla: endereço, alias ou mail exchanger.

**Referência:** [4.3 Registros frequentes](semana_02_estudo.md#s2-d3-dns).

### Comentário da Questão 8

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Uma entrada válida em cache pode evitar novas consultas, e o resolvedor não precisa consultar diretamente todos os autoritativos da Internet.
- **B)** Incorreta. Na recursão, o cliente espera resposta final ou erro, não apenas uma referência à raiz.
- **C)** Correta. O resolvedor pode reutilizar cache dentro do TTL ou seguir referências iterativas até obter a resposta.
- **D)** Incorreta. Recursão não converte registros A em MX; cada tipo preserva sua finalidade.

**Conceito:** consulta recursiva, iteração, cache e TTL no DNS.

**Pegadinha:** confundir a resposta final esperada pelo cliente com as referências iterativas usadas pelo resolvedor.

**Como pensar:** observe quem assumiu a tarefa de buscar a resposta e verifique antes se o cache ainda é válido.

**Referência:** [4.2 Recursão, iteração e cache](semana_02_estudo.md#s2-d3-dns).

### Comentário da Questão 9

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. DNS clássico não usa exclusivamente UDP; transferências de zona empregam TCP.
- **B)** Incorreta. Consultas e respostas curtas usam frequentemente UDP.
- **C)** Correta. DNS clássico admite 53/UDP e 53/TCP, conforme a operação e as condições da resposta.
- **D)** Incorreta. A porta 443 é associada ao DNS sobre HTTPS, não ao DNS clássico.

**Conceito:** transportes do DNS clássico.

**Pegadinha:** decorar “DNS é UDP” e ignorar TCP, especialmente em transferência de zona ou resposta que o exija.

**Como pensar:** associe consultas usuais a UDP, mas mantenha TCP como parte obrigatória do repertório DNS.

**Referência:** [4.4 Transportes do DNS clássico](semana_02_estudo.md#s2-d3-dns).

### Comentário da Questão 10

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. DNS sobre TLS usa TLS e tem como porta padrão 853, não 53/UDP.
- **B)** Incorreta. DNS sobre HTTPS encapsula consultas DNS em HTTPS e não é transferência de zona.
- **C)** Incorreta. DoT e DoH demonstram que DNS não está universalmente limitado à porta 53.
- **D)** Correta. DoT usa por padrão a porta 853, enquanto DoH utiliza HTTPS, normalmente na 443.

**Conceito:** DNS sobre TLS e DNS sobre HTTPS.

**Pegadinha:** aplicar a porta 53 do DNS clássico a todas as formas de transporte DNS.

**Como pensar:** primeiro identifique se o enunciado trata de DNS clássico, DoT ou DoH; depois associe o transporte e a porta.

**Referência:** [4.4 Transportes do DNS clássico](semana_02_estudo.md#s2-d3-dns).

### Comentário da Questão 11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. DORA segue DHCPDISCOVER, DHCPOFFER, DHCPREQUEST e DHCPACK.
- **B)** Incorreta. A solicitação e a confirmação não antecedem a descoberta e a oferta.
- **C)** Incorreta. O servidor não oferece configuração antes de o cliente anunciar a descoberta.
- **D)** Incorreta. O ACK confirma a concessão após a oferta e o pedido, não imediatamente após o DISCOVER.

**Conceito:** sequência inicial de concessão DHCP.

**Pegadinha:** reconhecer as quatro mensagens, mas aceitar uma ordem incompatível com descoberta, oferta, pedido e confirmação.

**Como pensar:** traduza DORA literalmente e acompanhe o diálogo cliente-servidor em ordem cronológica.

**Referência:** [5.1 Sequência DORA](semana_02_estudo.md#s2-d3-dhcp).

### Comentário da Questão 12

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Além de inverter cliente e servidor, atribui TCP a um serviço que usa UDP nessas portas.
- **B)** Correta. O servidor DHCP usa 67/UDP e o cliente usa 68/UDP.
- **C)** Incorreta. A porta 53 pertence ao DNS, cuja função é distinta da atribuição de configuração.
- **D)** Incorreta. DHCP não entrega concessões por HTTPS em 443/TCP.

**Conceito:** portas e transporte do DHCP.

**Pegadinha:** inverter 67 e 68 ou misturar DHCP com as portas de DNS e HTTPS.

**Como pensar:** memorize o sentido do serviço: servidor em 67/UDP e cliente em 68/UDP.

**Referência:** [5. DHCP — atribuição dinâmica de configuração](semana_02_estudo.md#s2-d3-dhcp).

### Comentário da Questão 13

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Registro DNS A associa nome a IPv4 e não substitui a concessão de parâmetros DHCP.
- **B)** Incorreta. Proxy reverso representa servidores de aplicação; não encaminha broadcasts DHCP entre VLANs.
- **C)** Incorreta. PAT traduz endereços e portas, mas não converte DHCP em HTTPS.
- **D)** Correta. O relay encaminha as mensagens da VLAN dos clientes ao servidor, que deve possuir escopo compatível com essa rede.

**Conceito:** uso de DHCP relay entre segmentos roteados.

**Pegadinha:** tentar resolver uma limitação de broadcast com serviços de aplicação ou tradução de endereços.

**Como pensar:** se clientes e servidor DHCP estão em VLANs distintas, procure um relay no segmento dos clientes e um escopo correspondente.

**Referência:** [5.1 Sequência DORA — DHCP relay](semana_02_estudo.md#s2-d3-dhcp).

### Comentário da Questão 14

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A transferência típica entre servidores de correio usa SMTP, não POP3.
- **B)** Correta. SMTP realiza submissão e transferência; POP3 e IMAP dão acesso à caixa postal.
- **C)** Incorreta. A consulta a registros MX pertence ao DNS, não ao IMAP.
- **D)** Incorreta. SMTP envia mensagens e não é o protocolo de leitura sincronizada de pastas.

**Conceito:** divisão de funções entre SMTP, POP3 e IMAP.

**Pegadinha:** confundir o protocolo de envio com os protocolos de acesso à caixa postal.

**Como pensar:** siga o fluxo: SMTP movimenta a mensagem; POP3 ou IMAP permite ao destinatário acessá-la.

**Referência:** [6. Correio eletrônico: SMTP, POP3 e IMAP](semana_02_estudo.md#s2-d3-email).

### Comentário da Questão 15

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. 25/TCP é referência de SMTP entre servidores, enquanto 110/TCP é POP3.
- **B)** Incorreta. A submissão SMTP usa 587/TCP; SNMP utiliza tradicionalmente 161/UDP e 162/UDP.
- **C)** Correta. 587/TCP é típica para submissão pelo cliente e 25/TCP para transferência entre servidores.
- **D)** Incorreta. 465 usa TCP e se associa à submissão com TLS implícito, não a toda transferência entre servidores.

**Conceito:** portas de submissão e transferência SMTP.

**Pegadinha:** trocar 25 e 587 ou atribuir UDP às portas do SMTP.

**Como pensar:** diferencie o cliente submetendo mensagem, normalmente em 587, do servidor entregando a outro servidor em 25.

**Referência:** [6.1 SMTP](semana_02_estudo.md#s2-d3-email).

### Comentário da Questão 16

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. IMAP mantém no servidor o estado da caixa, incluindo pastas e marcações, facilitando a sincronização entre dispositivos.
- **B)** Incorreta. SMTP é usado para submissão e transferência, não para sincronizar a leitura da caixa postal.
- **C)** Incorreta. FTP transfere arquivos e não gerencia caixas de correio.
- **D)** Incorreta. Telnet oferece terminal remoto sem a proteção criptográfica esperada e não sincroniza e-mails.

**Conceito:** modelo de acesso e sincronização do IMAP.

**Pegadinha:** escolher SMTP por associação genérica com e-mail, ignorando que o pedido é de acesso sincronizado.

**Como pensar:** quando mensagens, pastas e marcadores devem permanecer coerentes em vários clientes, procure IMAP.

**Referência:** [6.3 IMAP](semana_02_estudo.md#s2-d3-email).

### Comentário da Questão 17

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. SMTP cuida do envio, e IMAP mantém o acesso sincronizado à caixa postal em vários dispositivos.
- **B)** Incorreta. POP3 não é protocolo de submissão, e SMTP não sincroniza pastas.
- **C)** Incorreta. DNS resolve e publica dados de nomes; DHCP entrega configuração de rede.
- **D)** Incorreta. IMAP acessa a caixa postal, enquanto FTP não é protocolo de leitura de e-mail.

**Conceito:** fluxo integrado de submissão, transferência e acesso ao e-mail.

**Pegadinha:** atribuir a um único protocolo todas as etapas ou inverter envio e acesso.

**Como pensar:** decomponha a jornada da mensagem: submissão e transferência por SMTP; leitura sincronizada por IMAP.

**Referência:** [6.4 Fluxo integrado de e-mail](semana_02_estudo.md#s2-d3-email).

### Comentário da Questão 18

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. FTP clássico não cifra automaticamente credenciais ou conteúdo; a proteção por TLS caracteriza FTPS.
- **B)** Incorreta. FTP mantém conexão de controle e conexão de dados separadas.
- **C)** Incorreta. O FTP clássico usa TCP, não apenas UDP.
- **D)** Correta. O controle usa normalmente 21/TCP e, no modo passivo, o servidor informa a porta à qual o cliente abrirá a conexão de dados.

**Conceito:** arquitetura de canais e modos do FTP.

**Pegadinha:** reduzir FTP a uma única conexão em 21/TCP ou presumir criptografia nativa.

**Como pensar:** sempre procure dois papéis distintos no FTP: controle persistente e dados em conexão separada.

**Referência:** [7.1 FTP](semana_02_estudo.md#s2-d3-transferencia-remota).

### Comentário da Questão 19

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A iniciativa do servidor a partir da porta 20 é associada ao modo ativo, não ao passivo.
- **B)** Correta. No modo passivo, o cliente inicia a conexão de dados para a porta indicada pelo servidor.
- **C)** Incorreta. A conexão de controle permanece ativa e não é substituída por DNS.
- **D)** Incorreta. FTP usa TCP, e a porta 21 é do controle, não um canal UDP obrigatório para dados.

**Conceito:** funcionamento do modo passivo do FTP.

**Pegadinha:** aplicar ao modo passivo a porta 20 e a iniciativa do servidor próprias do modelo ativo tradicional.

**Como pensar:** no passivo, o servidor informa onde está ouvindo e o cliente inicia também a conexão de dados.

**Referência:** [7.1 FTP](semana_02_estudo.md#s2-d3-transferencia-remota).

### Comentário da Questão 20

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. SFTP opera sobre SSH; FTPS é FTP protegido por TLS.
- **B)** Incorreta. 990/TCP se associa ao FTPS implícito, e a arquitetura ainda mantém conexão de dados separada.
- **C)** Correta. FTPS explícito começa em 21/TCP, negocia `AUTH TLS` e usa `PBSZ 0` seguido de `PROT P` para pedir proteção privada dos dados.
- **D)** Incorreta. `PROT P` é comando do FTPS e não depende de DNS nem opera em 53/UDP.

**Conceito:** negociação e proteção dos canais no FTPS explícito.

**Pegadinha:** confundir FTPS com SFTP ou imaginar que proteger o controle protege automaticamente os dados.

**Como pensar:** identifique o FTPS explícito por 21/TCP e `AUTH TLS`; depois confirme a proteção do canal de dados com `PROT P`.

**Referência:** [7.2 FTPS](semana_02_estudo.md#s2-d3-transferencia-remota).

### Comentário da Questão 21

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. SFTP é um protocolo sobre SSH e não outro nome para FTPS implícito.
- **B)** Incorreta. O registro 989/TCP não obriga toda conexão de dados, pois os modos ativo e passivo podem negociar outras portas.
- **C)** Correta. A IANA associa 990/TCP ao controle e 989/TCP aos dados, sem eliminar os canais separados nem a negociação de portas.
- **D)** Incorreta. `AUTH TLS` após conexão em 21/TCP caracteriza FTPS explícito; no implícito, TLS começa imediatamente.

**Conceito:** FTPS implícito, portas registradas e separação dos canais.

**Pegadinha:** transformar portas registradas em uso obrigatório para toda conexão de dados ou confundir os modos implícito e explícito.

**Como pensar:** no implícito, TLS começa na abertura; ainda assim, preserve mentalmente a arquitetura FTP de controle e dados separados.

**Referência:** [7.2 FTPS](semana_02_estudo.md#s2-d3-transferencia-remota) e [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas).

### Comentário da Questão 22

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. SFTP é o SSH File Transfer Protocol, normalmente em 22/TCP, e pode reutilizar autenticação por chave pública do SSH.
- **B)** Incorreta. FTP clássico não cifra arquivos e credenciais por padrão.
- **C)** Incorreta. FTPS explícito protege FTP com TLS e não constitui subsistema do SSH.
- **D)** Incorreta. Telnet não fornece canal criptografado nem é protocolo apropriado de transferência de arquivos.

**Conceito:** SFTP como protocolo de arquivos sobre SSH.

**Pegadinha:** considerar SFTP e FTPS nomes diferentes para a mesma tecnologia.

**Como pensar:** se a infraestrutura e as chaves são de SSH, escolha o protocolo de transferência que funciona sobre SSH.

**Referência:** [7.3 SFTP](semana_02_estudo.md#s2-d3-transferencia-remota).

### Comentário da Questão 23

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. HTTP entrega recursos de aplicação e não substitui um protocolo de terminal remoto seguro.
- **B)** Incorreta. DNS auxilia na resolução do nome, mas não fornece sessão administrativa protegida.
- **C)** Incorreta. Telnet não cifra nativamente credenciais e conteúdo.
- **D)** Correta. SSH oferece autenticação, integridade e confidencialidade, normalmente em 22/TCP, desde que chaves e validações sejam protegidas.

**Conceito:** administração remota segura com SSH.

**Pegadinha:** escolher Telnet por sua função de terminal e ignorar a ausência de proteção criptográfica.

**Como pensar:** para administração sensível, exija canal autenticado, íntegro e confidencial e verifique a chave do host.

**Referência:** [7.4 SSH](semana_02_estudo.md#s2-d3-transferencia-remota).

### Comentário da Questão 24

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Telnet é protocolo de terminal remoto e não transferência de arquivos protegida por TLS.
- **B)** Correta. Telnet usa por padrão 23/TCP e não fornece a proteção criptográfica esperada para credenciais e conteúdo.
- **C)** Incorreta. 636/TCP é associada a LDAPS, não a uma versão segura de Telnet.
- **D)** Incorreta. A sincronização de relógios é função do NTP, normalmente em 123/UDP.

**Conceito:** função, porta e limitação de segurança do Telnet.

**Pegadinha:** reconhecer o terminal remoto e concluir, sem fundamento, que o protocolo protege a sessão.

**Como pensar:** associe Telnet a 23/TCP e texto sem a proteção criptográfica que torna SSH preferível.

**Referência:** [7.5 Telnet](semana_02_estudo.md#s2-d3-transferencia-remota).

### Comentário da Questão 25

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O gerente consulta o agente para monitoramento; regras de navegação web não definem essa arquitetura.
- **B)** Correta. O gerente consulta objetos identificados por OIDs na MIB do agente, que também pode iniciar uma trap.
- **C)** Incorreta. MIB e OID pertencem ao modelo de gerenciamento SNMP, não aos canais ou portas do FTP.
- **D)** Incorreta. Trap é notificação iniciada pelo agente e, no modelo clássico, não exige confirmação; INFORM é a modalidade confirmada.

**Conceito:** gerente, agente, MIB, OID e notificações SNMP.

**Pegadinha:** inverter os papéis de gerente e agente ou confundir trap com resposta confirmada a GET.

**Como pensar:** associe consultas ao gerente, objetos ao agente por MIB/OID e eventos espontâneos a traps.

**Referência:** [8. SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp).

### Comentário da Questão 26

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. As portas e o transporte estão trocados: consultas e respostas usam tradicionalmente 161/UDP, enquanto notificações chegam ao gerente em 162/UDP.
- **B)** Incorreta. SNMPv1 e SNMPv2c usam community strings e não oferecem, obrigatoriamente, autenticação e privacidade equivalentes às de um SNMPv3 bem configurado.
- **C)** Incorreta. SNMP gerencia e monitora objetos de equipamentos; não é protocolo de transferência de arquivos.
- **D)** Correta. A alternativa associa corretamente 161/UDP ao agente, 162/UDP às notificações e a proteção configurável do SNMPv3.

**Conceito:** portas tradicionais e níveis de proteção do SNMP.

**Pegadinha:** inverter 161 e 162 ou supor que toda versão do SNMP possui criptografia equivalente.

**Como pensar:** separe o destino da comunicação: consultas vão ao agente em 161/UDP; traps e informs chegam ao gerente em 162/UDP.

**Referência:** [8. SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp) e [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas).

### Comentário da Questão 27

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. LDAP acessa serviços de diretório hierárquicos; não é um banco relacional dependente de SQL.
- **B)** Incorreta. A resolução de nomes por registros A e AAAA é função do DNS.
- **C)** Correta. Entradas organizadas hierarquicamente, DN, atributos, bind e search são elementos típicos do LDAP.
- **D)** Incorreta. A sincronização de relógios em rede é função do NTP.

**Conceito:** estrutura e operações de um diretório LDAP.

**Pegadinha:** tratar diretório como banco relacional ou confundir LDAP com DNS.

**Como pensar:** procure os termos que caracterizam diretório: entrada, DN, atributo, bind e search.

**Referência:** [9. LDAP — acesso a diretórios](semana_02_estudo.md#s2-d3-ldap).

### Comentário da Questão 28

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. LDAP pode integrar a autenticação, mas a autorização depende também de políticas e aplicações; 389/TCP admite STARTTLS e 636/TCP é a porta usual do LDAPS.
- **B)** Incorreta. O uso de 389/TCP não cifra automaticamente a sessão; é necessário negociar TLS, por exemplo com STARTTLS.
- **C)** Incorreta. LDAPS usa usualmente 636/TCP, e não é a única forma de acesso protegido ao diretório.
- **D)** Incorreta. A existência da identidade no diretório não concede autorização irrestrita nas aplicações.

**Conceito:** proteção do LDAP e distinção entre autenticação e autorização.

**Pegadinha:** presumir que a porta 389 já implica TLS ou que uma conta autenticada recebe qualquer permissão.

**Como pensar:** examine separadamente identidade, decisão de acesso e proteção do canal.

**Referência:** [9. LDAP — acesso a diretórios](semana_02_estudo.md#s2-d3-ldap).

### Comentário da Questão 29

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Servidor DNS autoritativo publica dados de uma zona; não representa navegadores em sua navegação.
- **B)** Incorreta. NAT básico traduz endereços e não oferece, por definição, autenticação, política HTTP e cache.
- **C)** Incorreta. Proxy reverso atua diante dos servidores e os representa perante os clientes.
- **D)** Correta. Proxy direto atua em nome dos clientes e pode autenticar, filtrar, registrar e armazenar conteúdo em cache.

**Conceito:** proxy direto.

**Pegadinha:** trocar o extremo representado pelo proxy direto e pelo proxy reverso.

**Como pensar:** se o componente recebe pedidos dos usuários para alcançar destinos externos, ele representa os clientes.

**Referência:** [10.1 Proxy direto](semana_02_estudo.md#s2-d3-proxy).

### Comentário da Questão 30

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Proxy reverso fica diante dos servidores e pode terminar TLS, distribuir carga e ocultar a topologia interna.
- **B)** Incorreta. Proxy direto representa clientes em seus acessos a destinos externos.
- **C)** Incorreta. DHCP relay encaminha mensagens DHCP entre segmentos e não publica aplicações web.
- **D)** Incorreta. Resolvedor DNS recursivo busca dados de nomes; não termina TLS nem distribui requisições entre servidores de aplicação.

**Conceito:** proxy reverso.

**Pegadinha:** associar a palavra “proxy” ao cliente sem observar qual extremo está sendo representado.

**Como pensar:** se o componente está na frente do portal e recebe conexões em nome dos servidores, é reverso.

**Referência:** [10.2 Proxy reverso](semana_02_estudo.md#s2-d3-proxy).

### Comentário da Questão 31

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmação inverte os papéis: NAT traduz campos de endereçamento, enquanto um proxy pode compreender ou intermediar a aplicação.
- **B)** Correta. Proxy atua em nome de um extremo; NAT pode traduzir o tráfego encaminhado sem encerrar a sessão de aplicação.
- **C)** Incorreta. São mecanismos distintos e nenhum deles garante sempre a mesma proteção.
- **D)** Incorreta. NAT não cifra conteúdo por definição, e resolução de nomes não é a função definidora de proxy.

**Conceito:** diferença entre proxy e NAT.

**Pegadinha:** considerar ambos sinônimos apenas porque podem ocultar endereços internos.

**Como pensar:** pergunte se há representação de um extremo ou tradução de cabeçalhos no encaminhamento.

**Referência:** [10. Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy).

### Comentário da Questão 32

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Resolver nomes é função do DNS, e entregar configuração por broadcast pode integrar o DHCP; isso não diferencia NAT e PAT.
- **B)** Incorreta. NAT básico e PAT/NAPT são conceitos associados principalmente à tradução no IPv4; a distinção não é uma separação IPv4 × IPv6.
- **C)** Correta. NAT básico traduz endereços IP; PAT/NAPT também traduz identificadores de transporte, como portas.
- **D)** Incorreta. PAT/NAPT não substitui o gateway usado para encaminhar tráfego a outras redes.

**Conceito:** NAT básico versus PAT/NAPT.

**Pegadinha:** usar NAT como termo guarda-chuva e ignorar a distinção específica pedida pela banca.

**Como pensar:** quando houver oposição expressa, associe NAT básico a endereço e PAT/NAPT a endereço mais porta.

**Referência:** [11. NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat).

### Comentário da Questão 33

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Eliminar as portas impediria distinguir adequadamente os fluxos TCP ou UDP multiplexados.
- **B)** Incorreta. Registro MX identifica servidores de correio de um domínio e não cria mapeamentos de tradução.
- **C)** Correta. Portas públicas distintas permitem que a tabela PAT associe cada resposta ao host e fluxo internos corretos.
- **D)** Incorreta. Resolução DNS e escolha de endereço IPv6 privado não realizam a demultiplexação do retorno pelo PAT.

**Conceito:** tabela de tradução e multiplexação do PAT/NAPT.

**Pegadinha:** imaginar que a coincidência das portas privadas impede o compartilhamento do mesmo endereço público.

**Como pensar:** acompanhe cada fluxo pela associação entre origem interna, origem pública traduzida e destino.

**Referência:** [11. NAT básico e PAT/NAPT — Exemplo resolvido 3: Dois usuários compartilham um IP público](semana_02_estudo.md#s2-d3-nat-pat).

### Comentário da Questão 34

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Tradução de endereços ou portas não fornece confidencialidade; TLS continua necessário quando se deseja proteger os dados em trânsito.
- **B)** Correta. NAT/PAT traduz campos de endereçamento, mas não autentica usuários, não cifra o conteúdo e não substitui firewall.
- **C)** Incorreta. A dificuldade de conexões recebidas sem mapeamento não constitui bloqueio absoluto nem garantia de segurança.
- **D)** Incorreta. NAT básico traduz endereços IP e não é um proxy reverso de aplicação.

**Conceito:** limites de segurança do NAT/PAT.

**Pegadinha:** confundir ocultação ou tradução de endereços com criptografia e filtragem de segurança.

**Como pensar:** identifique a função entregue pelo mecanismo; tradução não equivale a autenticação, cifra ou política de firewall.

**Referência:** [11. NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat).

### Comentário da Questão 35

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. NTP sincroniza referências de tempo em 123/UDP, favorecendo logs coerentes e validações temporais, sem definir o fuso exibido localmente.
- **B)** Incorreta. DNS publica e resolve dados de nomes; não escolhe a hora do servidor autoritativo.
- **C)** Incorreta. DHCP usa 67/UDP no servidor e entrega configuração de rede, não regras de horário de verão.
- **D)** Incorreta. FTP transfere arquivos e não sincroniza relógios nem ordena temporalmente os eventos registrados.

**Conceito:** finalidade, porta e limite do NTP.

**Pegadinha:** confundir sincronização da referência temporal com configuração de fuso horário.

**Como pensar:** problemas de coerência entre relógios, logs e certificados apontam primeiro para NTP e fontes de tempo.

**Referência:** [12. NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp).

### Comentário da Questão 36

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A associação registrada é convencional; um administrador pode configurar HTTP em 8080 ou em outra porta adequada.
- **B)** Incorreta. A porta 443 não comprova legitimidade, configuração criptográfica correta nem conteúdo seguro.
- **C)** Incorreta. Um serviço pode usar porta não convencional, e outro processo pode escutar na 22; a porta isolada não identifica infalivelmente o protocolo.
- **D)** Correta. O registro orienta associações padronizadas, mas não impede outras configurações nem prova o conteúdo efetivo do tráfego.

**Conceito:** alcance das associações de portas registradas pela IANA.

**Pegadinha:** transformar uma convenção de porta em garantia técnica ou de segurança.

**Como pensar:** use a porta como indício inicial e confirme protocolo, configuração e conteúdo por outras evidências.

**Referência:** [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas) e [1. Protocolo, serviço, porta e socket — Portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).

### Comentário da Questão 37

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A concessão DHCP fornece os parâmetros necessários antes das etapas normais de resolução do nome e acesso ao portal.
- **B)** Incorreta. A tradução PAT na borda pressupõe que a estação já consiga encaminhar tráfego ao gateway.
- **C)** Incorreta. A negociação TLS ocorre após haver configuração de rede, resolução ou endereço de destino e conectividade de transporte.
- **D)** Incorreta. Para consultar DNS externo, a estação dependente de configuração automática precisa antes conhecer IP, prefixo, gateway e servidor DNS.

**Conceito:** ordem do fluxo integrado de acesso à rede.

**Pegadinha:** começar pelo protocolo visível ao usuário e esquecer a configuração inicial do host.

**Como pensar:** siga as dependências: configuração local, resolução do nome, encaminhamento, transporte, TLS e aplicação.

**Referência:** [14. Fluxo integrado de acesso a um portal — etapas 1 a 4](semana_02_estudo.md#s2-d3-fluxo-integrado).

### Comentário da Questão 38

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. NTP trata de tempo; o acesso por IP demonstra conectividade ao destino e direciona a investigação para a resolução do nome.
- **B)** Incorreta. O modo passivo do FTP não participa do acesso HTTPS nem da resolução DNS.
- **C)** Correta. A diferença entre sucesso por IP e falha por nome indica verificar primeiro servidor DNS configurado, respostas, cache e registros.
- **D)** Incorreta. IMAP sincroniza caixas postais e não resolve nomes de portais.

**Conceito:** diagnóstico de falha de resolução DNS.

**Pegadinha:** interpretar qualquer falha de acesso como perda total de conectividade.

**Como pensar:** compare o que muda entre os testes: se o IP funciona e apenas o nome falha, isole a etapa DNS.

**Referência:** [4. DNS — Exemplo resolvido 1: Nome não resolve, mas o IP responde](semana_02_estudo.md#s2-d3-dns).

### Comentário da Questão 39

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A resolução correta e a tentativa de conexão não permitem atribuir a falha exclusivamente ao DHCP.
- **B)** Incorreta. Registro MX orienta correio eletrônico e não a conexão HTTPS do portal.
- **C)** Incorreta. O enunciado informa que o nome foi resolvido corretamente.
- **D)** Correta. Após o sucesso do DNS, a falha em 443/TCP deve ser localizada em etapas como rota, firewall, NAT/PAT ou serviço remoto.

**Conceito:** diagnóstico por etapas após a resolução DNS.

**Pegadinha:** culpar o DNS por toda falha que envolve um nome de domínio, mesmo quando a resolução já ocorreu.

**Como pensar:** marque a última etapa comprovadamente bem-sucedida e investigue os componentes seguintes do fluxo.

**Referência:** [14. Fluxo integrado de acesso a um portal — diagnóstico por sintoma](semana_02_estudo.md#s2-d3-fluxo-integrado).

### Comentário da Questão 40

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. DHCPACK integra a concessão inicial e não sucede normalmente o HTTP em claro como etapa do acesso HTTPS descrito.
- **B)** Correta. No HTTPS tradicional, abre-se TCP para 443, negocia-se TLS e transporta-se HTTP protegido; o proxy reverso pode encaminhar a requisição ao servidor interno.
- **C)** Incorreta. Trap SNMP, DHCPOFFER e Telnet não compõem o fluxo normal de publicação HTTPS.
- **D)** Incorreta. FTP passivo é mecanismo de transferência de arquivos e não substitui HTTP nem TLS.

**Conceito:** sequência de HTTPS com proxy reverso.

**Pegadinha:** misturar protocolos válidos, mas pertencentes a fluxos diferentes.

**Como pensar:** depois do DNS, siga transporte TCP, proteção TLS, protocolo HTTP e eventual intermediação do servidor.

**Referência:** [14. Fluxo integrado de acesso a um portal — etapas 7 a 10](semana_02_estudo.md#s2-d3-fluxo-integrado).

### Comentário da Questão 41

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Um servidor pode manter muitas conexões simultâneas na mesma porta de escuta; elas não compartilham um único socket de conexão.
- **B)** Correta. IP e porta de origem, IP e porta de destino e protocolo distinguem as conexões TCP.
- **C)** Incorreta. As portas de origem participam da identificação dos fluxos e não são eliminadas para aceitar conexões.
- **D)** Incorreta. O nome DNS não integra a identificação da conexão TCP depois de obtido o endereço de destino.

**Conceito:** identificação de conexões por seus extremos e protocolo.

**Pegadinha:** imaginar que uma porta de servidor aceita somente um cliente por vez.

**Como pensar:** a porta de destino pode ser igual; são as combinações completas de origem, destino e protocolo que se diferenciam.

**Referência:** [1. Protocolo, serviço, porta e socket](semana_02_estudo.md#s2-d3-protocolo-porta).

### Comentário da Questão 42

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O número da porta não avalia vulnerabilidades da aplicação.
- **B)** Incorreta. Observar tráfego na 443 não prova legitimidade do conteúdo nem validação do certificado pelo cliente.
- **C)** Incorreta. A porta 443 pode transportar diferentes usos; mesmo em HTTP, não comprova HTTP/2, e HTTP/3 usa QUIC sobre UDP.
- **D)** Correta. A porta sugere a convenção de HTTPS, mas não determina sozinha protocolo efetivo, legitimidade ou segurança.

**Conceito:** porta como indício, não como prova do protocolo.

**Pegadinha:** inferir segurança ou versão da aplicação apenas pela porta de destino.

**Como pensar:** trate a porta como metadado de triagem e procure evidências adicionais no transporte, handshake e aplicação.

**Referência:** [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas) e [1. Protocolo, serviço, porta e socket — Portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).

### Comentário da Questão 43

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. HTTP/3 usa QUIC sobre UDP, normalmente na porta 443, enquanto HTTP/1.1 e HTTP/2 usam TCP em seus usos usuais.
- **B)** Incorreta. HTTP/3 e FTP são protocolos distintos; 21/TCP é a porta clássica de controle do FTP.
- **C)** Incorreta. QUIC incorpora proteção criptográfica; o uso de UDP não elimina TLS do modelo de segurança do HTTP/3.
- **D)** Incorreta. Concessão é função do DHCP, e SNMP não constitui pré-requisito específico para HTTP/3.

**Conceito:** transporte do HTTP/3.

**Pegadinha:** concluir que todo HTTPS usa TCP ou que UDP significa ausência de proteção criptográfica.

**Como pensar:** memorize a exceção moderna: HTTP/3 usa QUIC/UDP; HTTP/1.1 e HTTP/2 usam TCP.

**Referência:** [3.1 HTTP e 3.2 HTTPS](semana_02_estudo.md#s2-d3-http-https).

### Comentário da Questão 44

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. NS indica os servidores autoritativos de uma zona.
- **B)** Incorreta. SOA reúne informações administrativas fundamentais da zona.
- **C)** Correta. PTR associa um endereço a um nome na resolução reversa.
- **D)** Incorreta. TXT armazena texto associado ao domínio, inclusive para validações e políticas.

**Conceito:** registro PTR e resolução DNS reversa.

**Pegadinha:** inverter registros de resolução direta, como A/AAAA, com o PTR da resolução reversa.

**Como pensar:** se a consulta parte do endereço para chegar ao nome, procure PTR.

**Referência:** [4.3 Registros frequentes do DNS](semana_02_estudo.md#s2-d3-dns).

### Comentário da Questão 45

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O autoritativo responde pelos dados publicados na zona sob sua autoridade, e não apenas por cache alheio.
- **B)** Incorreta. TTL limita o reaproveitamento do registro em cache; não é data de expiração do domínio nem garantia de disponibilidade.
- **C)** Correta. A alternativa distingue a origem autoritativa dos dados de seu reaproveitamento temporário por um resolvedor.
- **D)** Incorreta. Uma resposta em cache não torna o resolvedor autoridade da zona nem a resposta autoritativa para toda a Internet.

**Conceito:** servidor autoritativo, resolvedor e TTL de cache.

**Pegadinha:** interpretar “autoritativo” como “sempre correto” ou TTL como prazo de existência do domínio.

**Como pensar:** separe quem publica a zona de quem busca e reutiliza temporariamente a resposta.

**Referência:** [4.1 Componentes e 4.2 Recursão, iteração e cache do DNS](semana_02_estudo.md#s2-d3-dns).

### Comentário da Questão 46

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Endereço 169.254.x.x e ausência de gateway são indícios de que a concessão automática falhou; servidor ou relay alcançável e escopo disponível são os primeiros pontos a verificar.
- **B)** Incorreta. Transferência de zona DNS não fornece endereço, prefixo ou gateway ao cliente.
- **C)** Incorreta. TLS implícito no IMAP pertence à aplicação de correio e pressupõe conectividade de rede.
- **D)** Incorreta. FTP passivo trata da conexão de dados de uma transferência e não corrige configuração IP ausente.

**Conceito:** diagnóstico de falha na concessão DHCP.

**Pegadinha:** iniciar a análise por protocolos de aplicação quando a estação ainda não possui configuração básica utilizável.

**Como pensar:** valide primeiro IP, prefixo, gateway e DNS; um endereço link-local sem gateway direciona a investigação ao DHCP.

**Referência:** [5. DHCP — atribuição dinâmica de configuração e diagnóstico por sintoma](semana_02_estudo.md#s2-d3-dhcp).

### Comentário da Questão 47

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Fluxo de bytes ordenado com retransmissões nativas descreve o TCP.
- **B)** Correta. Mensagens independentes, baixa latência, multicast e recuperação controlada pela aplicação são critérios compatíveis com UDP.
- **C)** Incorreta. SYN, SYN-ACK e ACK formam a abertura clássica do TCP, não um requisito antes de cada datagrama UDP.
- **D)** Incorreta. TCP fornece fluxo de bytes e não preserva necessariamente as fronteiras das mensagens da aplicação.

**Conceito:** critérios para escolha de UDP.

**Pegadinha:** reduzir a comparação à máxima imprecisa “UDP é mais rápido”.

**Como pensar:** escolha pelo requisito da aplicação: formato das mensagens, latência, multicast e responsabilidade pela recuperação de perdas.

**Referência:** [2.3 Escolha do transporte](semana_02_estudo.md#s2-d3-tcp-udp).

### Comentário da Questão 48

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Datagramas independentes, sem conexão e sem confirmações nativas caracterizam UDP.
- **B)** Incorreta. Confirmação no transporte não garante a conclusão semântica de uma operação no banco de dados.
- **C)** Incorreta. TCP possui mecanismos de controle de fluxo e de congestionamento.
- **D)** Correta. TCP entrega fluxo confiável e ordenado por meio de sequência, ACKs, temporizadores e retransmissões, sem preservar fronteiras de mensagens.

**Conceito:** garantias e limites do TCP.

**Pegadinha:** extrapolar confiabilidade de transporte para sucesso da aplicação ou preservação de mensagens.

**Como pensar:** liste exatamente o que TCP garante no fluxo de bytes e mantenha fora dessa lista a semântica da aplicação.

**Referência:** [2.1 TCP: orientado à conexão e confiável](semana_02_estudo.md#s2-d3-tcp-udp).

### Comentário da Questão 49

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. NTP e suas fontes de tempo são o foco direto quando relógios divergentes prejudicam correlação de logs e validações de certificados.
- **B)** Incorreta. DNS não configura fuso horário nem recalcula registros A com base no relógio local.
- **C)** Incorreta. DHCP fornece configuração de rede, enquanto POP3 acessa mensagens; nenhum substitui o outro nem resolve sincronização temporal.
- **D)** Incorreta. O modo ativo do FTP não ordena eventos registrados em servidores distintos.

**Conceito:** impacto operacional da sincronização NTP.

**Pegadinha:** tentar corrigir apenas a exibição do horário ou usar um protocolo sem relação com a fonte temporal.

**Como pensar:** quando o mesmo evento aparece em instantes incompatíveis ou certificados falham por horário, verifique relógios e fontes NTP.

**Referência:** [12. NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp) e [14. Fluxo integrado de acesso a um portal — etapa 11](semana_02_estudo.md#s2-d3-fluxo-integrado).

### Comentário da Questão 50

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. DNS não entrega gateway; SMTP não traduz portas; FTP não é a etapa de TLS do portal; NTP não publica aplicações.
- **B)** Correta. A sequência reúne concessão DHCP, resolução DNS, encaminhamento e PAT, proteção TLS do HTTP e recepção eventual por proxy reverso.
- **C)** Incorreta. IMAP não entrega máscara, LDAP não resolve nomes DNS, Telnet não cifra HTTP e NAT não organiza caixa postal.
- **D)** Incorreta. SNMP não atribui IP, POP3 não roteia e FTP não substitui proxy reverso.

**Conceito:** integração dos serviços no acesso a um portal publicado.

**Pegadinha:** aceitar uma sequência porque contém protocolos reais, embora suas funções estejam trocadas.

**Como pensar:** acompanhe o fluxo pela dependência funcional: configurar, resolver, encaminhar/traduzir, proteger e entregar à aplicação.

**Referência:** [14. Fluxo integrado de acesso a um portal](semana_02_estudo.md#s2-d3-fluxo-integrado).

---

## Questões extras de revisão fixa do Dia 3

#### Extra Dia 3.1

Sobre as quatro bases normativas da revisão do Dia 3, assinale a alternativa correta.

A) A RN CFA nº 651/2024 aprova o Código de Ética, enquanto a RN CFA nº 671/2025 organiza internamente o CRA-PR.
B) O Decreto nº 61.934/1967 revoga a Lei nº 4.769/1965 sempre que detalha o exercício profissional.
C) A Lei nº 4.769/1965 disciplina o exercício e estrutura o sistema; o Decreto a regulamenta; o Regimento organiza o CRA-PR; e a RN CFA nº 671/2025 aprova o Código de Ética.
D) Lei, Decreto, Regimento e Código possuem o mesmo objeto e podem ser usados indistintamente para definir qualquer competência.

#### Extra Dia 3.2

De acordo com o art. 2º da Lei nº 4.769/1965, integra o campo da atividade profissional estudada:

A) a elaboração de pareceres, relatórios, planos, projetos, arbitragens e laudos, a assessoria em geral, a chefia intermediária, a direção superior e trabalhos de pesquisa, planejamento, implantação, coordenação e controle nos campos da Administração.
B) exclusivamente a direção superior de órgãos públicos federais, vedadas a assessoria, a pesquisa e a atuação em organizações privadas.
C) apenas a assinatura de documentos contábeis, sem atividades de planejamento, organização ou controle.
D) toda e qualquer atividade técnica existente, ainda que não guarde conexão com os campos da Administração.

#### Extra Dia 3.3

Um candidato apresenta o diploma exigido para o provimento de cargo técnico de Administração e afirma que, por isso, está dispensado do concurso previsto em lei. À luz da Lei nº 4.769/1965 e do Decreto nº 61.934/1967, a afirmação é:

A) correta, porque o diploma transforma o provimento em contratação direta.
B) correta, desde que o candidato ainda não possua registro no CRA.
C) incorreta apenas se o cargo estiver em empresa privada, pois concurso não se aplica à Administração Pública.
D) incorreta, porque a apresentação do diploma não dispensa a prestação de concurso quando este for exigido.

#### Extra Dia 3.4

Nos termos do art. 6º da Lei nº 4.769/1965, o CFA e os CRAs:

A) são associações privadas independentes, sem personalidade jurídica de direito público.
B) constituem, em conjunto, autarquia dotada de personalidade jurídica de direito público e autonomia técnica, administrativa e financeira.
C) integram a Administração Direta estadual e dependem de autorização do governador para exercer fiscalização.
D) formam empresa pública federal destinada exclusivamente à expedição de carteiras profissionais.

#### Extra Dia 3.5

Assinale a alternativa que apresenta competência atribuída pela Lei nº 4.769/1965 ao CFA.

A) Expedir ordinariamente as carteiras profissionais de todos os inscritos no CRA-PR e exercer a primeira instância regional.
B) Elaborar o Regimento do CRA-PR sem participação do próprio Conselho Regional.
C) Examinar, modificar e aprovar regimentos internos dos Regionais, julgar em última instância recursos de penalidades e votar e alterar o Código de Deontologia Administrativa.
D) Fiscalizar exclusivamente o exercício profissional no Paraná, sem função de orientação nacional.

#### Extra Dia 3.6

Constitui núcleo de finalidades legais dos Conselhos Regionais de Administração:

A) executar diretrizes do CFA, fiscalizar na respectiva jurisdição, manter registros, julgar infrações, impor penalidades legais, expedir carteiras e elaborar seu regimento para exame e aprovação pelo CFA.
B) votar leis federais sobre profissões regulamentadas e rever decisões judiciais em última instância.
C) modificar unilateralmente o Código nacional e aprovar definitivamente o próprio regimento, sem exame do CFA.
D) limitar-se à arrecadação de anuidades, sem competência para registro, fiscalização ou julgamento.

#### Extra Dia 3.7

Sobre registro e carteira profissional no art. 14 da Lei nº 4.769/1965, assinale a alternativa correta.

A) O diploma substitui o registro, e a carteira tem validade apenas no estado em que foi emitida.
B) A falta de registro produz somente irregularidade cadastral, sem repercussão sobre a legalidade do exercício.
C) A carteira é expedida pelo CFA e não pode servir como documento de identidade.
D) O exercício exige registro; sua falta o torna ilegal e punível, e a carteira profissional serve como prova do exercício, como identidade e tem fé em todo o território nacional.

#### Extra Dia 3.8

Quanto aos arts. 15 e 16 da Lei nº 4.769/1965, assinale a alternativa correta.

A) Empresas que explorem atividades profissionais nunca se sujeitam a registro, pois somente pessoas físicas são fiscalizadas.
B) Empresas, entidades e escritórios técnicos que explorem as atividades previstas estão sujeitos a registro; a Lei prevê multa e suspensões e, na reincidência da mesma infração dentro de cinco anos após a primeira, multa em dobro e cancelamento do registro.
C) A Lei prevê apenas advertência escrita e censura pública, sem multa, suspensão ou regra de reincidência.
D) O cancelamento legal é automático na primeira infração e dispensa ampla defesa ou enquadramento.

#### Extra Dia 3.9

O art. 3º do Decreto nº 61.934/1967 detalha a atividade profissional. Assinale a alternativa compatível com esse dispositivo.

A) O campo se restringe ao magistério, excluindo chefia, consultoria e documentos técnicos.
B) Funções de direção ou assessoramento nunca integram a atividade profissional, mesmo quando exigem técnicas de Administração.
C) O campo abrange documentos técnicos, pesquisas, planejamento, implantação, coordenação e controle, além de funções e cargos técnicos, chefia, direção, assessoramento, consultoria e magistério pertinente.
D) O Decreto trata somente da composição eleitoral dos Conselhos e não descreve atividades profissionais.

#### Extra Dia 3.10

Sobre documentos profissionais nos arts. 6º e 7º do Decreto nº 61.934/1967, assinale a alternativa correta.

A) Os documentos do art. 3º devem ser elaborados e assinados por profissional registrado, ressalvado o exercício de cargo público na forma do art. 6º; o número de registro deve constar após a assinatura, e o art. 7º ressalva o documento oficial assinado pelo ocupante do respectivo cargo público.
B) A citação do número de registro é facultativa, ainda que o documento esteja sujeito à regra do art. 6º.
C) Empresas privadas estão proibidas de exigir assinatura de profissional registrado em documentos técnicos.
D) Qualquer assinatura posterior regulariza documento elaborado por pessoa não registrada, independentemente das demais condições normativas.

#### Extra Dia 3.11

Considerando os arts. 9º a 11 do Decreto nº 61.934/1967, assinale a alternativa correta.

A) Para exercer a profissão basta apresentar diploma, sem carteira, registro ou prova de direitos sociais.
B) O exercício exige a Carteira de Identidade Profissional e prova do pleno gozo dos direitos sociais; a falta de registro torna o exercício ilegal e punível, e a fiscalização cabe ao CRA competente e ao CFA.
C) A fiscalização compete exclusivamente ao CFA, sendo vedada a atuação do CRA da jurisdição.
D) A falta de registro é sanada automaticamente pela experiência prática, sem providência perante o Conselho.

#### Extra Dia 3.12

Segundo o Regimento aprovado pela RN CFA nº 651/2024, assinale a alternativa correta.

A) O CRA-PR possui jurisdição nacional e o Plenário exerce função apenas consultiva.
B) O CRA-PR é associação privada, e a Ouvidoria constitui sua primeira instância de julgamento.
C) A autonomia do CRA-PR o dispensa de executar diretrizes do CFA e de submeter seu Regimento ao Conselho Federal.
D) O CRA-PR é autarquia de direito público, tem sede na capital e jurisdição em todo o Paraná; seu Plenário é órgão colegiado de deliberação superior e primeira instância de julgamento regional.

#### Extra Dia 3.13

Quanto ao âmbito de aplicação do Código aprovado pela RN CFA nº 671/2025, assinale a alternativa correta.

A) O Código alcança pessoas físicas e jurídicas registradas no CRA da respectiva jurisdição, no exercício das atividades abrangidas pela Lei e pelo Decreto, observadas as especificidades da pessoa jurídica; mandato eletivo no CFA ou nos CRAs também é considerado atividade profissional para esse fim.
B) O Código alcança qualquer trabalhador de tecnologia da informação, ainda que não registrado e fora das atividades profissionais abrangidas.
C) Pessoas jurídicas estão integralmente excluídas, pois somente pessoa natural pode praticar infração ética.
D) O exercício de mandato eletivo no Sistema é expressamente excluído da incidência do Código.

#### Extra Dia 3.14

Assinale a alternativa que relaciona corretamente um dever e um direito previstos na RN CFA nº 671/2025.

A) É dever divulgar informação sigilosa por conveniência comercial, e é direito dificultar a fiscalização do CRA.
B) É direito ceder o registro a terceiro não habilitado, e é dever aceitar condições degradantes de trabalho.
C) É dever comunicar imediatamente ao CRA alterações de domicílio ou endereço relevantes ao controle profissional; é direito apontar falhas institucionais consideradas indignas do exercício ou prejudiciais, dirigindo-se ao Sistema CFA/CRAs.
D) É dever abdicar da independência técnica quando houver vínculo de emprego, e é direito publicar em nome próprio trabalho de que não participou.

#### Extra Dia 3.15

À luz da RN CFA nº 671/2025, assinale a alternativa correta.

A) A sanção pode ser aplicada antes do trânsito em julgado administrativo quando a infração parecer grave.
B) Assinar documento de terceiro sem orientação ou supervisão constitui infração; sanções são acompanhadas de multa e dependem do processo e do trânsito em julgado, e suspensão e cancelamento não se aplicam à pessoa jurídica.
C) A violação de sigilo é infração mesmo quando existe justa causa reconhecida pela norma.
D) Pessoa jurídica registrada não se submete a dever, infração, advertência, censura ou multa ética alguma.

#### Extra Dia 3.16

Leia: “O CRA-PR possui autonomia administrativa; contudo, deve executar as diretrizes do CFA.” O conector “contudo” estabelece relação de:

A) causa.
B) conclusão.
C) finalidade.
D) oposição ou ressalva.

#### Extra Dia 3.17

No período “O diretor entregou ao conselheiro seu relatório”, assinale a alternativa correta.

A) O pronome “seu” pode retomar “diretor” ou “conselheiro”; para eliminar a ambiguidade, deve-se explicitar “o relatório do diretor” ou “o relatório do conselheiro”, conforme o sentido pretendido.
B) “Seu” retoma obrigatoriamente o termo mais próximo, sem possibilidade de outra leitura.
C) A frase é agramatical porque pronomes possessivos não podem retomar pessoas.
D) A ambiguidade desaparece se “seu” for retirado: “O diretor entregou ao conselheiro relatório”, sem necessidade de definir a posse.

#### Extra Dia 3.18

Assinale a alternativa redigida de acordo com as regras de concordância estudadas.

A) Haviam três infrações registradas e deve existirem providências imediatas.
B) Fazem dois anos que o processo começou e houveram novas manifestações.
C) Deve haver providências, existiam inconsistências no relatório e faz dois anos que o processo começou.
D) Devem haver providências, existia três inconsistências e fazem dois anos desde a decisão.

#### Extra Dia 3.19

Assinale a alternativa em que o emprego da crase está correto.

A) O conselheiro começou à analisar o processo recebido.
B) O cidadão encaminhou a manifestação à Ouvidoria do CRA-PR.
C) O CRA-PR submeteu o Regimento à CFA para exame.
D) A equipe entregou o relatório à revisar pelo diretor.

#### Extra Dia 3.20

Assinale a alternativa com pontuação adequada.

A) Os membros do Plenário, deliberaram sobre o processo.
B) O Presidente encaminhou, o relatório ao colegiado.
C) Embora o CRA-PR possua autonomia administrativa o Regimento, deve ser submetido ao CFA.
D) O Plenário, órgão colegiado de deliberação superior, decidiu o caso em primeira instância regional.

## Gabarito das questões extras do Dia 3

| Extra | Resposta |
|---:|:---:|
| 3.1 | C |
| 3.2 | A |
| 3.3 | D |
| 3.4 | B |
| 3.5 | C |
| 3.6 | A |
| 3.7 | D |
| 3.8 | B |
| 3.9 | C |
| 3.10 | A |
| 3.11 | B |
| 3.12 | D |
| 3.13 | A |
| 3.14 | C |
| 3.15 | B |
| 3.16 | D |
| 3.17 | A |
| 3.18 | C |
| 3.19 | B |
| 3.20 | D |

## Comentários das questões extras do Dia 3

#### Comentário Extra Dia 3.1

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A RN CFA nº 651/2024 aprova o Regimento do CRA-PR; a RN CFA nº 671/2025 aprova o Código de Ética.
- **B)** Incorreta. Decreto regulamentar detalha a aplicação da Lei, mas não a revoga nem a substitui.
- **C)** Correta. A alternativa associa cada base ao respectivo objeto estudado.
- **D)** Incorreta. As quatro bases se relacionam, mas possuem funções normativas diferentes.

**Conceito:** função da Lei, do Decreto, do Regimento e do Código de Ética.

**Pegadinha:** trocar as RNs nº 651 e nº 671 ou tratar regulamentação como revogação.

**Como pensar:** associe Lei à estrutura, Decreto à execução, Regimento à organização regional e Código à conduta ética.

**Referência:** [Revisão fixa do Dia 3 — Legislação: relação entre as normas](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.2

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A opção reúne atividades e níveis funcionais expressamente sintetizados a partir do art. 2º.
- **B)** Incorreta. A atividade não se limita à direção de órgãos federais nem exclui assessoria, pesquisa ou organizações privadas.
- **C)** Incorreta. O campo não se reduz a documentos contábeis e inclui planejamento, implantação, coordenação e controle.
- **D)** Incorreta. A Lei trata dos campos da Administração e de seus desdobramentos ou conexões, não de toda atividade técnica imaginável.

**Conceito:** campo da atividade profissional no art. 2º da Lei nº 4.769/1965.

**Pegadinha:** reduzir o campo a uma tarefa ou ampliá-lo sem qualquer conexão com Administração.

**Como pensar:** reconheça três grupos: documentos técnicos, funções de assessoria/chefia/direção e trabalhos de análise e gestão.

**Referência:** [Revisão fixa do Dia 3 — Legislação: Lei nº 4.769/1965](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.3

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Diploma não converte provimento público em contratação direta.
- **B)** Incorreta. Ausência de registro não cria dispensa de concurso.
- **C)** Incorreta. O enunciado trata justamente do cargo técnico na Administração Pública, em que o concurso permanece quando exigido.
- **D)** Correta. Lei e Decreto afirmam que a apresentação do diploma não afasta o concurso previsto.

**Conceito:** diferença entre requisito de formação e procedimento de provimento.

**Pegadinha:** presumir que diploma, registro e concurso são requisitos intercambiáveis.

**Como pensar:** pergunte separadamente: há formação exigida? há registro? há concurso legalmente previsto?

**Referência:** [Revisão fixa do Dia 3 — Legislação: habilitação, diploma e concurso](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.4

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A Lei atribui personalidade jurídica de direito público ao conjunto autárquico.
- **B)** Correta. A alternativa reproduz o núcleo de natureza jurídica e autonomia do art. 6º.
- **C)** Incorreta. Os Conselhos não são órgãos da Administração Direta estadual sujeitos à autorização cotidiana de governador.
- **D)** Incorreta. O sistema não é empresa pública nem se limita à emissão de carteiras.

**Conceito:** natureza do Sistema CFA/CRAs na Lei nº 4.769/1965.

**Pegadinha:** classificar conselho profissional como associação privada, órgão sem personalidade ou empresa estatal.

**Como pensar:** memorize o trio: direito público, autarquia e autonomia técnica, administrativa e financeira.

**Referência:** [Revisão fixa do Dia 3 — Legislação: natureza do Sistema](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.5

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Expedição ordinária de carteiras e primeira instância regional pertencem ao âmbito do CRA.
- **B)** Incorreta. O CRA elabora seu Regimento, que é examinado pelo CFA; o Conselho Federal não substitui integralmente a iniciativa regional.
- **C)** Correta. Examinar, modificar e aprovar regimentos, julgar recursos e votar ou alterar o Código estão no núcleo do art. 7º.
- **D)** Incorreta. O CFA possui orientação sistêmica nacional, não fiscalização exclusiva no Paraná.

**Conceito:** competências do CFA.

**Pegadinha:** inverter competência nacional e execução regional.

**Como pensar:** verbos de uniformização, exame de regimentos e última instância apontam para o CFA.

**Referência:** [Revisão fixa do Dia 3 — Legislação: CFA × CRA-PR](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.6

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A alternativa reúne as finalidades regionais dos arts. 8º da Lei e 39 do Decreto.
- **B)** Incorreta. Conselhos Regionais não exercem função legislativa federal nem revisão judicial.
- **C)** Incorreta. Alteração nacional do Código não é competência unilateral do CRA, e seu Regimento segue para exame e aprovação do CFA.
- **D)** Incorreta. Registro, fiscalização, julgamento e carteira integram expressamente as funções regionais.

**Conceito:** finalidades dos Conselhos Regionais.

**Pegadinha:** reduzir o CRA a arrecadação ou transferir-lhe atribuições nacionais e judiciais.

**Como pensar:** associe o Regional aos verbos executar, fiscalizar, registrar, julgar e expedir.

**Referência:** [Revisão fixa do Dia 3 — Legislação: competências dos CRAs](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.7

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Diploma e registro cumprem funções diferentes, e a carteira tem fé em todo o território nacional.
- **B)** Incorreta. A própria Lei caracteriza como ilegal e punível o exercício sem registro.
- **C)** Incorreta. A carteira é expedida pelo Conselho Regional e também serve como identidade.
- **D)** Correta. A opção reúne os efeitos do registro e as funções legais da carteira.

**Conceito:** registro e carteira profissional.

**Pegadinha:** limitar territorialmente a fé da carteira ou permitir que diploma substitua inscrição.

**Como pensar:** registro habilita; carteira comprova e identifica.

**Referência:** [Revisão fixa do Dia 3 — Legislação: registro e carteira](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.8

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O art. 15 prevê registro de empresas, entidades e escritórios técnicos que explorem as atividades alcançadas.
- **B)** Correta. A alternativa combina registro da pessoa jurídica com o catálogo legal de penalidades e a regra específica de reincidência.
- **C)** Incorreta. Advertência e censura pertencem ao catálogo ético; a Lei também prevê multa e suspensões.
- **D)** Incorreta. O cancelamento do art. 16 não é automático na primeira infração, e a ampla defesa é expressamente assegurada na hipótese de incapacidade técnica.

**Conceito:** registro de organizações e penalidades legais.

**Pegadinha:** misturar o art. 16 da Lei com a gradação própria do Código de Ética.

**Como pensar:** mantenha duas caixas: penalidades da Lei e sanções ético-disciplinares da RN CFA nº 671/2025.

**Referência:** [Revisão fixa do Dia 3 — Legislação: arts. 15 e 16 da Lei](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.9

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Magistério é uma das possibilidades, não o limite do campo.
- **B)** Incorreta. Chefia, direção, assessoramento e consultoria podem integrar a atividade quando exigem conhecimentos de Administração.
- **C)** Correta. A opção sintetiza os grupos de atividades detalhados no art. 3º do Decreto.
- **D)** Incorreta. O Decreto descreve expressamente o campo e a atividade profissional.

**Conceito:** detalhamento regulamentar da atividade profissional.

**Pegadinha:** selecionar apenas um exemplo do artigo e tratá-lo como rol exclusivo.

**Como pensar:** o Decreto operacionaliza a Lei mediante documentos, estudos, gestão, cargos e ensino pertinente.

**Referência:** [Revisão fixa do Dia 3 — Legislação: Decreto nº 61.934/1967](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.10

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A opção separa as regras dos arts. 6º e 7º e inclui a indicação obrigatória do registro após a assinatura.
- **B)** Incorreta. O parágrafo único do art. 6º torna obrigatória a citação do número de registro.
- **C)** Incorreta. O art. 7º dirige a exigência também às empresas privadas.
- **D)** Incorreta. A simples aposição posterior de assinatura não apaga exigências de elaboração, registro, responsabilidade e ressalvas aplicáveis.

**Conceito:** elaboração e assinatura de documentos profissionais.

**Pegadinha:** fundir as ressalvas dos arts. 6º e 7º ou esquecer o número de registro.

**Como pensar:** art. 6º disciplina documento e assinatura; art. 7º exige que autoridades e empresas cobrem a assinatura regular.

**Referência:** [Revisão fixa do Dia 3 — Legislação: documentos profissionais](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.11

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O art. 9º exige carteira e prova do pleno gozo dos direitos sociais.
- **B)** Correta. A alternativa articula corretamente os arts. 9º, 10 e 11 do Decreto.
- **C)** Incorreta. A fiscalização também cabe ao CRA competente.
- **D)** Incorreta. Experiência não produz regularização cadastral automática.

**Conceito:** exercício, registro e fiscalização no Decreto.

**Pegadinha:** retirar o CRA da fiscalização ou reduzir a exigência ao diploma.

**Como pensar:** carteira e direitos sociais habilitam a comprovação; registro ausente torna o exercício ilegal; CRA e CFA fiscalizam.

**Referência:** [Revisão fixa do Dia 3 — Legislação: arts. 9º a 11 do Decreto](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.12

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A jurisdição do CRA-PR é estadual, e o Plenário possui deliberação e julgamento.
- **B)** Incorreta. O CRA-PR é autarquia de direito público, e a Ouvidoria não é instância julgadora.
- **C)** Incorreta. Autonomia não equivale a soberania; o Regional executa diretrizes e submete seu Regimento ao CFA.
- **D)** Correta. A alternativa reúne natureza, sede, jurisdição e posição regimental do Plenário.

**Conceito:** natureza e organização básica do CRA-PR.

**Pegadinha:** transformar autonomia em independência normativa ou Ouvidoria em órgão decisório.

**Como pensar:** fixe quatro dados: autarquia, capital, Paraná e Plenário como deliberação superior/primeira instância.

**Referência:** [Revisão fixa do Dia 3 — Legislação: Regimento do CRA-PR](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.13

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A opção preserva registro, jurisdição, atividade abrangida, especificidades da pessoa jurídica e mandato eletivo.
- **B)** Incorreta. Trabalho em TI, sozinho, não basta para atrair o Código fora de seu âmbito subjetivo e material.
- **C)** Incorreta. Pessoas jurídicas registradas podem ser alcançadas, observadas suas particularidades.
- **D)** Incorreta. O art. 4º, § 3º, inclui o mandato eletivo no CFA e nos CRAs.

**Conceito:** âmbito subjetivo e material do Código de Ética.

**Pegadinha:** universalizar o Código para toda atividade tecnológica ou excluir pessoa jurídica e mandatário.

**Como pensar:** confira três filtros: registro, jurisdição e exercício de atividade abrangida; depois verifique a regra do mandato.

**Referência:** [Revisão fixa do Dia 3 — Legislação: sujeitos do Código](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.14

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Divulgação indevida e obstrução da fiscalização são incompatíveis com o Código.
- **B)** Incorreta. Cessão de registro não é direito, e o Código permite recusar condições degradantes.
- **C)** Correta. Comunicação cadastral imediata é dever; apontar determinadas falhas ao Sistema é direito.
- **D)** Incorreta. O vínculo de emprego não elimina a independência técnica, e publicar trabalho alheio constitui infração.

**Conceito:** distinção entre dever e direito ético.

**Pegadinha:** apresentar infração como prerrogativa ou inverter direito e obrigação.

**Como pensar:** dever manda agir; direito protege uma faculdade; infração tipifica conduta proibida.

**Referência:** [Revisão fixa do Dia 3 — Legislação: dever × direito × infração](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.15

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O art. 23 exige trânsito em julgado administrativo antes da sanção.
- **B)** Correta. A alternativa reúne infração expressa, multa conjunta, garantia processual e limite das sanções à pessoa jurídica.
- **C)** Incorreta. O Código tipifica a violação de sigilo sem justa causa, não toda revelação em qualquer circunstância.
- **D)** Incorreta. Pessoa jurídica pode estar no âmbito do Código e receber advertência, censura e multa compatíveis.

**Conceito:** infrações, sanções, multa, processo e pessoa jurídica.

**Pegadinha:** confundir incidência do Código com compatibilidade de suspensão e cancelamento.

**Como pensar:** siga a ordem fato → inciso → processo → trânsito → sanção compatível e multa.

**Referência:** [Revisão fixa do Dia 3 — Legislação: infrações e sanções](semana_02_estudo.md#s2-d3-revisao-legislacao).

#### Comentário Extra Dia 3.16

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. “Contudo” não apresenta motivo para a autonomia.
- **B)** Incorreta. Conclusão seria marcada por “portanto” ou “logo”.
- **C)** Incorreta. Finalidade seria introduzida por expressão como “para que”.
- **D)** Correta. O conector introduz ressalva à possível leitura de autonomia como independência absoluta.

**Conceito:** relação adversativa de conectores.

**Pegadinha:** interpretar a segunda oração como consequência, em vez de limite à expectativa criada pela primeira.

**Como pensar:** substitua por “porém”; preservado o sentido, a relação é de oposição ou ressalva.

**Referência:** [Revisão fixa do Dia 3 — Português: conectores](semana_02_estudo.md#s2-d3-revisao-portugues).

#### Comentário Extra Dia 3.17

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Há dois antecedentes masculinos possíveis, e a explicitação da posse elimina a ambiguidade.
- **B)** Incorreta. Pronome possessivo não retoma obrigatoriamente o antecedente mais próximo.
- **C)** Incorreta. O uso de possessivo com referente pessoal é gramatical.
- **D)** Incorreta. Retirar o possessivo deixa indefinida a relação de posse e não garante o sentido pretendido.

**Conceito:** coesão referencial e ambiguidade pronominal.

**Pegadinha:** adotar proximidade linear como regra absoluta de referência.

**Como pensar:** substitua o pronome por cada antecedente possível; se ambas as leituras funcionarem, explicite o referente.

**Referência:** [Revisão fixa do Dia 3 — Português: referência e ambiguidade](semana_02_estudo.md#s2-d3-revisao-portugues).

#### Comentário Extra Dia 3.18

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. `Haver` existencial fica no singular, e a locução correta seria “devem existir”, com concordância de `existir`.
- **B)** Incorreta. `Fazer` temporal e `haver` existencial são impessoais: “faz” e “houve”.
- **C)** Correta. “Deve haver” permanece no singular; “existiam” concorda com “inconsistências”; e “faz” é impessoal no tempo decorrido.
- **D)** Incorreta. O correto seria “deve haver”, “existiam três inconsistências” e “faz dois anos”.

**Conceito:** concordância com `haver`, `existir` e `fazer`.

**Pegadinha:** transportar para verbos impessoais a flexão que seria exigida por `existir`.

**Como pensar:** se `haver` significa existir ou `fazer` indica tempo, mantenha o singular; com `existir`, procure o sujeito.

**Referência:** [Revisão fixa do Dia 3 — Português: haver, existir e concordância](semana_02_estudo.md#s2-d3-revisao-portugues).

#### Comentário Extra Dia 3.19

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não ocorre crase antes do infinitivo “analisar”.
- **B)** Correta. A preposição exigida por “encaminhar a” encontra o artigo feminino de “a Ouvidoria”, formando “à”.
- **C)** Incorreta. Diante da sigla masculina CFA, usa-se “ao CFA”.
- **D)** Incorreta. “Revisar” é verbo e não admite artigo feminino formador de crase.

**Conceito:** fusão da preposição `a` com artigo feminino.

**Pegadinha:** empregar acento grave antes de verbo ou de termo masculino.

**Como pensar:** substitua o termo feminino por “Plenário”; “ao Plenário” confirma “à Ouvidoria”.

**Referência:** [Revisão fixa do Dia 3 — Português: crase](semana_02_estudo.md#s2-d3-revisao-portugues).

#### Comentário Extra Dia 3.20

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A vírgula separa indevidamente o sujeito “Os membros do Plenário” do verbo “deliberaram”.
- **B)** Incorreta. A vírgula separa o verbo “encaminhou” de seus complementos.
- **C)** Incorreta. Falta vírgula depois da oração concessiva deslocada, e a vírgula inserida separa o sujeito “o Regimento” do verbo.
- **D)** Correta. As vírgulas isolam o aposto explicativo “órgão colegiado de deliberação superior”.

**Conceito:** pontuação de termos essenciais, oração deslocada e aposto.

**Pegadinha:** reproduzir pausas de fala que rompem sujeito, verbo e complemento.

**Como pensar:** preserve o esqueleto sujeito–verbo–complemento e isole apenas trechos explicativos ou deslocados.

**Referência:** [Revisão fixa do Dia 3 — Português: pontuação](semana_02_estudo.md#s2-d3-revisao-portugues).


---

# Dia 4 — Segurança da Informação e Redes

## Questões principais

### Questão 1

Uma equipe afirma que a aquisição de uma ferramenta de segurança tornará o portal institucional definitivamente seguro. À luz da gestão de riscos, assinale a alternativa correta.

A) Segurança é um estado binário alcançado quando todos os ativos recebem o mesmo conjunto de controles.
B) A segurança exige identificar ativos, ameaças e vulnerabilidades, estimar probabilidade e impacto, selecionar controles proporcionais e monitorar sua eficácia.
C) A seleção de um controle eficaz elimina a necessidade de reavaliar mudanças no ambiente e no perfil de ameaças.
D) A gestão de riscos se limita a corrigir vulnerabilidades técnicas, pois pessoas, processos e fornecedores não alteram o risco.

### Questão 2

Após implantar MFA, segmentação e monitoramento, uma organização reavalia o risco de acesso indevido. Sobre o risco residual, assinale a alternativa correta.

A) Corresponde ao risco calculado antes da aplicação dos controles e deixa de existir assim que uma medida preventiva é implantada.
B) Deve ser obrigatoriamente igual a zero para que o serviço possa permanecer em operação.
C) Deve ser sempre transferido a terceiro, ainda que seja compatível com os critérios de aceitação da organização.
D) É o risco que permanece após os controles e deve ser reavaliado para aceitação ou tratamento adicional conforme o contexto.

### Questão 3

Durante o transporte, foi perdido um disco de backup não cifrado que continha dados pessoais. Não há evidência de modificação ou destruição dos arquivos. O objetivo de segurança diretamente ameaçado é a:

A) confidencialidade.
B) integridade.
C) disponibilidade.
D) autenticidade.

### Questão 4

Considere as afirmativas sobre um incidente de ransomware.

I. A exfiltração de uma base antes da cifração pode comprometer a confidencialidade.
II. A alteração ou cifração não autorizada de arquivos pode comprometer a integridade e a disponibilidade.
III. A existência de backup íntegro impede o vazamento e evita necessariamente a interrupção inicial.

Está correto o que se afirma em:

A) I, apenas.
B) III, apenas.
C) I e II, apenas.
D) I, II e III.

### Questão 5

Em um sistema do conselho, o usuário apresenta sua senha e um token válido. Depois, o sistema consulta o papel funcional para decidir se ele pode alterar um cadastro. As duas etapas correspondem, respectivamente, a:

A) autorização e autenticação.
B) autenticação e autorização.
C) accounting e não repúdio.
D) auditoria e accounting.

### Questão 6

Assinale a alternativa que apresenta autenticação multifator, considerando que os fatores devem pertencer a categorias diferentes.

A) Senha pessoal e PIN memorizado.
B) Duas senhas distintas cadastradas pelo mesmo usuário.
C) Impressão digital e reconhecimento facial.
D) Senha pessoal e token criptográfico sob posse do usuário.

### Questão 7

Uma política libera determinado relatório somente quando os atributos do usuário, do recurso, da ação, do dispositivo e do horário satisfazem as condições definidas. Esse modelo é característico de:

A) ABAC.
B) RBAC baseado exclusivamente no nome do cargo.
C) autenticação biométrica.
D) accounting de sessões.

### Questão 8

No modelo técnico tradicional AAA, o terceiro A corresponde a accounting. Assinale a interpretação correta desse componente.

A) Ele comprova a identidade alegada antes do acesso e substitui a autenticação.
B) Ele define, sozinho, todas as permissões associadas ao papel do usuário.
C) Ele registra consumo, sessões e ações para responsabilização e controle, fornecendo insumos para auditoria sem ser sinônimo de todo o processo de auditoria.
D) Ele produz não repúdio forte apenas por manter qualquer registro local, mesmo sem proteção ou contexto.

### Questão 9

Um documento eletrônico precisa oferecer evidência que dificulte a negação falsa da autoria perante terceiro. Qual alternativa descreve a solução mais adequada?

A) Publicar apenas um hash sem vínculo com identidade, pois qualquer pessoa poderá recalculá-lo.
B) Empregar assinatura digital, com proteção da chave privada, vínculo confiável entre identidade e chave e trilha de evidências apropriada.
C) Cifrar o documento com uma chave simétrica compartilhada entre todos os envolvidos, pois qualquer detentor da chave identifica exclusivamente o autor.
D) Registrar o nome declarado pelo usuário em arquivo de texto sem controle de integridade.

### Questão 10

Para que registros de segurança apoiem responsabilização e investigação, é adequado:

A) registrar somente o horário, pois identidade, origem e resultado podem ser inferidos posteriormente.
B) permitir alteração dos logs pelos mesmos administradores cujas ações serão examinadas, para facilitar correções.
C) coletar o maior volume possível e dispensar retenção, sincronização de relógios e análise.
D) registrar contexto como quem fez o quê, quando, de onde, sobre qual recurso e com qual resultado, além de proteger a integridade e sincronizar os relógios.

### Questão 11

Em um cenário de segurança, o portal de serviços tem valor para a missão; um grupo criminoso pode atacá-lo; o gateway possui falha conhecida ainda não corrigida; milhares de tentativas de login são observadas; e um acesso indevido é confirmado. A classificação correta é:

A) portal: ativo; grupo criminoso: ameaça; falha não corrigida: vulnerabilidade; tentativas observadas: evento; acesso indevido confirmado: incidente.
B) portal: ameaça; grupo criminoso: vulnerabilidade; falha não corrigida: risco; tentativas observadas: incidente; acesso indevido: evento.
C) portal: controle; grupo criminoso: ativo; falha não corrigida: incidente; tentativas observadas: risco; acesso indevido: ameaça.
D) portal: vulnerabilidade; grupo criminoso: evento; falha não corrigida: ativo; tentativas observadas: controle; acesso indevido: risco.

### Questão 12

Um serviço exposto utiliza versão de software com falha explorável. A equipe ainda está estimando a chance de exploração e o impacto sobre dados e operação. Nesse caso:

A) a falha explorável já é, por definição, um incidente confirmado.
B) a chance de exploração isolada é o ativo, e o impacto é a ameaça.
C) a falha é uma vulnerabilidade, enquanto o risco considera probabilidade e impacto adverso.
D) vulnerabilidade e risco são sinônimos, pois ambos existem antes do ataque.

### Questão 13

Um sensor gera alerta de tráfego incomum. Após correlação com registros de identidade e aplicação, confirma-se que uma conta foi usada para copiar dados sem autorização. Assinale a alternativa correta.

A) O alerta inicial já prova, necessariamente, a ocorrência e o alcance do incidente.
B) Tanto o alerta quanto a cópia confirmada são apenas vulnerabilidades.
C) A cópia não autorizada é uma ameaça potencial, mas não um incidente enquanto o atacante não for identificado.
D) O alerta é uma ocorrência observável a ser analisada; a cópia indevida confirmada caracteriza incidente.

### Questão 14

Em relação aos conceitos de ameaça, vulnerabilidade e controle, assinale a alternativa correta.

A) Um criminoso externo é vulnerabilidade porque explora sistemas, enquanto uma falha sem correção é ameaça.
B) Um criminoso capaz de causar dano é ameaça, uma falha explorável é vulnerabilidade e a aplicação de correção ou MFA pode atuar como controle.
C) Um controle é qualquer evento observado, mesmo que não modifique o risco.
D) A existência de vulnerabilidade implica que o dano já ocorreu e transforma automaticamente o risco em incidente.

### Questão 15

Sobre vírus e worm, assinale a alternativa correta.

A) O vírus se vincula a arquivo ou programa hospedeiro e depende de execução ou propagação associada; o worm pode se propagar automaticamente por redes ou sistemas.
B) O worm exige sempre que o usuário execute um arquivo hospedeiro, enquanto o vírus obrigatoriamente se propaga sem interação.
C) Ambos os termos designam qualquer software malicioso e podem ser usados como sinônimos.
D) A diferença está apenas no objetivo: vírus coleta informações, e worm cifra arquivos para extorsão.

### Questão 16

Um programa se apresenta como atualizador legítimo e induz o usuário a executá-lo. Depois de instalado, abre acesso remoto, mas não possui mecanismo obrigatório de autorreplicação. Essa descrição corresponde principalmente a:

A) worm.
B) vírus de setor de inicialização.
C) cavalo de Troia.
D) ataque DDoS.

### Questão 17

Uma campanha maliciosa copia documentos, cifra compartilhamentos e interrompe o portal. Sobre a classificação e os controles envolvidos, assinale a alternativa correta.

A) Trata-se necessariamente de spyware, porque ransomware afeta somente a disponibilidade.
B) O backup elimina a necessidade de conter o atacante e investigar eventual exfiltração.
C) A cifração autorizada pelo atacante preserva a integridade, pois o conteúdo original ainda pode existir em backup.
D) Ransomware pode combinar exfiltração, alteração ou cifração e interrupção, atingindo confidencialidade, integridade e disponibilidade.

### Questão 18

Assinale a associação correta entre categorias de malware.

A) Rootkit: conjunto distribuído de máquinas usado exclusivamente em DDoS; botnet: ferramenta que apenas oculta privilégios locais.
B) Spyware: coleta informações; rootkit: busca ocultar presença ou manter privilégio; botnet: conjunto de bots sob controle.
C) Bot: arquivo hospedeiro que só se propaga após execução manual; vírus: dispositivo comprometido controlado remotamente.
D) Spyware: cifra arquivos para extorsão; rootkit: mensagem fraudulenta enviada por SMS; botnet: falha de configuração.

### Questão 19

Sobre as variações de phishing, assinale a alternativa correta.

A) Smishing utiliza exclusivamente chamadas de voz, enquanto vishing usa mensagens SMS.
B) Whaling designa qualquer campanha genérica enviada em massa, sem considerar o perfil do alvo.
C) Spear phishing é direcionado a alvo específico; whaling mira pessoa de alta relevância; smishing usa mensagem ou SMS; e vishing usa voz.
D) Phishing exige sempre arquivo malicioso e não pode buscar somente credenciais ou pagamento.

### Questão 20

Um servidor recebe mensagem urgente, aparentemente enviada pela presidência, pedindo alteração imediata dos dados bancários de um fornecedor. A ação mais adequada é:

A) verificar a solicitação por canal independente e seguir o procedimento de autorização, mesmo que a mensagem use autoridade e urgência.
B) atender imediatamente, pois mensagens de alta autoridade dispensam confirmação.
C) responder à própria mensagem pedindo confirmação, pois isso garante que o remetente aparente controla a conta.
D) considerar a mensagem legítima se não houver anexo executável, já que engenharia social depende de malware.

### Questão 21

Quanto ao uso de MFA contra phishing, assinale a alternativa correta.

A) MFA impede todo phishing, porque elimina a possibilidade de o usuário acessar página falsa.
B) MFA protege a conta mesmo quando o atacante captura uma sessão autenticada ou controla a recuperação da conta.
C) Dois segredos do tipo senha constituem MFA e neutralizam qualquer reutilização de credenciais.
D) MFA reduz o impacto do roubo de senha, mas certos ataques podem capturar sessão, induzir aprovação ou explorar a recuperação da conta.

### Questão 22

Assinale a alternativa que caracteriza corretamente spoofing.

A) Consiste apenas na captura passiva de pacotes, sem falsificação de identidade ou origem.
B) Consiste na falsificação de identidade ou origem aparente; seus efeitos variam conforme o protocolo, e IP spoofing não garante o recebimento das respostas.
C) Exige sempre o comprometimento prévio de uma autoridade certificadora.
D) É sinônimo de DDoS, pois depende necessariamente de múltiplas origens distribuídas.

### Questão 23

Sobre sniffing e ataque on-path, também denominado man-in-the-middle (MITM), assinale a alternativa correta.

A) Sniffing é captura e análise de tráfego e pode ser passivo ou autorizado; no ataque on-path, o adversário se posiciona no caminho e pode observar e alterar a comunicação.
B) Sniffing sempre altera os pacotes capturados, enquanto o ataque on-path apenas registra metadados.
C) A presença de qualquer criptografia impede ataque on-path, mesmo quando o cliente aceita certificado falso.
D) Em rede com switches, a captura por agente malicioso é fisicamente impossível.

### Questão 24

Uma campanha testa a mesma pequena lista de senhas comuns em milhares de contas, evitando muitas tentativas consecutivas em uma única conta. Essa técnica e a distinção para credential stuffing estão corretamente descritas em:

A) força bruta; credential stuffing cria senhas aleatórias sem usar vazamentos.
B) ataque de dicionário; credential stuffing falsifica o endereço IP de origem.
C) password spraying; credential stuffing reutiliza pares de credenciais obtidos em vazamentos.
D) phishing; credential stuffing explora exclusivamente falhas de memória.

### Questão 25

Uma botnet envia tráfego suficiente para saturar o enlace de Internet do órgão antes que os pacotes alcancem o firewall local. Assinale a alternativa correta.

A) Trata-se de DoS obrigatoriamente originado por um único sistema, e o firewall local sempre absorverá o volume.
B) A distribuição das origens aumenta apenas a confidencialidade e não afeta a disponibilidade.
C) A troca do firewall por um IDS fora de banda restitui, por si só, a capacidade já esgotada do enlace.
D) Trata-se de cenário compatível com DDoS; a mitigação pode exigir capacidade e filtragem a montante, serviço anti-DDoS, CDN ou coordenação com o provedor.



### Questão 26

Um órgão adotou treinamento periódico contra phishing, um IDS para alertar sobre tráfego suspeito e cópias de segurança testadas para restaurar dados. Quanto à natureza e à função predominante desses controles, assinale a alternativa correta.

A) O treinamento é controle físico e corretivo; o IDS é administrativo e preventivo; o backup é técnico e dissuasório.
B) Os três controles são exclusivamente técnicos e preventivos, pois todos atuam antes do encerramento do incidente.
C) O treinamento é administrativo e predominantemente preventivo; o IDS é técnico e detectivo; o backup exerce função de recuperação.
D) O IDS é controle físico de recuperação, enquanto o treinamento e o backup são exclusivamente compensatórios.

### Questão 27

Uma arquitetura possui filtro de e-mail, MFA, segmentação, EDR e backup, mas todas essas camadas são administradas por uma única credencial compartilhada e sem proteção adicional. À luz da defesa em profundidade, é correto afirmar que:

A) a credencial comum constitui uma falha compartilhada capaz de enfraquecer várias camadas, apesar da diversidade aparente de controles.
B) a presença de cinco controles elimina o risco residual, ainda que todos dependam da mesma credencial.
C) defesa em profundidade exige que todas as camadas sejam do mesmo fabricante e tenham a mesma dependência administrativa.
D) o backup torna irrelevantes a segmentação e a proteção de identidade, pois permite desfazer qualquer incidente.

### Questão 28

Sobre firewalls, assinale a afirmativa correta.

A) Um firewall sem estado acompanha toda a sessão e decide com base no histórico completo da conexão.
B) Permitir uma porta conhecida garante que o conteúdo transportado por ela seja legítimo e que a aplicação esteja sem vulnerabilidades.
C) Um firewall de borda observa necessariamente todo ataque interno, mesmo quando o tráfego não cruza o ponto em que ele está instalado.
D) Um firewall stateful acompanha o estado das conexões, mas ainda depende de política adequada e não corrige vulnerabilidades da aplicação.

### Questão 29

Uma equipe revisará as regras do firewall que protege um serviço institucional. Qual conduta está mais alinhada a uma política segura?

A) Liberar qualquer origem para qualquer destino em portas altas, porque somente portas conhecidas oferecem risco.
B) Permitir apenas origens, destinos e serviços necessários, documentar e revisar regras, registrar eventos relevantes e reconhecer que a cifração pode reduzir a visibilidade do controle.
C) Desabilitar o controle de saída, pois apenas conexões iniciadas da internet podem causar incidente.
D) Considerar toda regra permanente depois do primeiro teste, para evitar que revisões afetem a disponibilidade.

### Questão 30

Durante uma fase inicial de observação, a organização deseja receber cópia do tráfego e gerar alertas sem inserir o sensor no caminho direto nem permitir bloqueios automáticos. O controle mais compatível é:

A) um IDS fora de banda.
B) um IPS em linha com descarte automático.
C) um firewall stateful configurado como servidor de backup.
D) uma VPN site-to-site sem mecanismos de detecção.

### Questão 31

Um IPS passou a bloquear requisições legítimas após uma regra nova classificá-las como maliciosas. Esse caso demonstra que:

A) todo alerta do IPS confirma um incidente e deve ser tratado como prova definitiva.
B) um IPS não pode afetar a disponibilidade, pois sua atuação é exclusivamente detectiva.
C) a ocorrência prova um falso negativo, porque o tráfego legítimo deixou de alcançar o serviço.
D) um falso positivo em controle preventivo em linha pode bloquear tráfego legítimo e prejudicar a disponibilidade, razão pela qual regras exigem ajuste e monitoramento.

### Questão 32

Um portal público consulta uma aplicação que, por sua vez, acessa uma base interna sensível. Qual desenho melhor aplica o conceito de DMZ?

A) Colocar portal, aplicação e banco na mesma DMZ e liberar qualquer comunicação entre eles.
B) Manter o componente exposto na DMZ, separar aplicação e banco em segmentos mais restritos e permitir somente os fluxos necessários entre as camadas.
C) Instalar o banco diretamente na internet e usar a DMZ apenas para estações administrativas.
D) Tratar todo servidor da DMZ como confiável, dispensando monitoramento das conexões para a rede interna.

### Questão 33

Um empregado acessa a rede institucional por VPN a partir de um notebook já comprometido por malware. Assinale a alternativa correta.

A) A VPN remove o malware do notebook assim que o túnel é estabelecido.
B) A cifração do túnel autoriza automaticamente o empregado a acessar qualquer segmento interno.
C) A VPN pode proteger o tráfego no percurso, mas não torna o endpoint confiável; postura do dispositivo, MFA, menor privilégio, segmentação e monitoramento continuam necessários.
D) O túnel impede que credenciais roubadas sejam usadas, ainda que não exista MFA e o gateway esteja desatualizado.

### Questão 34

Uma organização precisa conectar permanentemente as redes de duas unidades pela internet e, separadamente, permitir que analistas individuais trabalhem fora do escritório. Qual associação está correta?

A) Acesso remoto conecta as duas redes, enquanto site-to-site serve apenas a um usuário individual.
B) IPsec só pode proteger aplicações Web, e soluções baseadas em TLS operam obrigatoriamente na camada IP.
C) Qualquer dos modelos concede acesso irrestrito a toda a rede interna depois que o túnel é criado.
D) VPN site-to-site é apropriada para interligar redes; VPN de acesso remoto atende usuários ou dispositivos, e ambas exigem autenticação, correção do gateway e política de acesso.

### Questão 35

Uma empresa separou usuários e servidores em VLANs diferentes, mas configurou o roteamento inter-VLAN para permitir qualquer fluxo nos dois sentidos. A conclusão correta é:

A) a separação por VLAN impede, sozinha, todo movimento lateral, inclusive o roteado.
B) as VLANs separam domínios de camada 2 e de broadcast, mas ACLs ou firewalls internos ainda devem limitar o tráfego roteado entre os segmentos.
C) VLAN e firewall interno são controles idênticos, por isso aplicar ambos cria necessariamente um conflito.
D) a única forma de segmentar é instalar redes físicas sem qualquer roteamento entre elas.

### Questão 36

Para aplicar menor privilégio ao acesso de uma aplicação ao banco de dados, a equipe deve:

A) conceder à conta de serviço somente as operações e os objetos necessários, restringir origem e contexto e revisar periodicamente a permissão.
B) usar uma única conta administrativa compartilhada entre usuários, aplicações e rotinas de backup.
C) autorizar toda identidade autenticada, pois autenticação bem-sucedida já demonstra necessidade funcional.
D) liberar qualquer porta entre os segmentos, desde que cada servidor esteja em uma VLAN diferente.

### Questão 37

Sobre criptografia simétrica e assimétrica, assinale a alternativa correta.

A) A criptografia simétrica usa obrigatoriamente um par de chaves pública e privada e é a opção mais custosa para grandes volumes.
B) A criptografia assimétrica usa uma única chave secreta compartilhada e não pode apoiar assinaturas.
C) Cifras simétricas, como AES, são eficientes para grande volume, enquanto mecanismos assimétricos usam um par de chaves e podem apoiar assinatura, autenticação ou estabelecimento de chaves.
D) Toda operação feita com chave privada fornece confidencialidade, independentemente do algoritmo e da finalidade.

### Questão 38

Em um protocolo criptográfico híbrido, como ocorre conceitualmente no TLS, é correto afirmar que:

A) todos os dados da sessão são cifrados diretamente com a chave privada do servidor.
B) mecanismos assimétricos ou uma PSK podem participar da autenticação e do estabelecimento de segredos, enquanto chaves simétricas de sessão protegem o tráfego volumoso.
C) o hash substitui a troca de chaves e fornece, sozinho, confidencialidade ao canal.
D) a parte simétrica é dispensada sempre que o servidor possui certificado digital.

### Questão 39

Um fornecedor publica um arquivo de atualização e, na mesma página comprometida, publica o hash correspondente ao arquivo adulterado. Por que a simples comparação dos dois valores não detecta o ataque?

A) Porque funções hash só podem ser calculadas com a chave privada do fornecedor.
B) Porque um hash sempre cifra o arquivo e impede que ele seja substituído.
C) Porque hashes de arquivos diferentes são obrigatoriamente iguais quando têm o mesmo tamanho.
D) Porque o atacante conseguiu substituir tanto o arquivo quanto a referência; o resumo precisa vir de fonte confiável, ser autenticado ou estar assinado.

### Questão 40

Dois sistemas que compartilham um segredo precisam verificar integridade e autenticidade das mensagens trocadas. Não há requisito de não repúdio entre eles. O mecanismo mais diretamente adequado é:

A) hash simples sem segredo, publicado ao lado da mensagem.
B) criptografia reversível da senha usada pelos operadores.
C) HMAC com chave secreta compartilhada.
D) certificado digital sem prova de posse de chave e sem validação.

### Questão 41

Qual prática é mais adequada para armazenar senhas de usuários?

A) Aplicar função de derivação de chave própria para senhas, com salt único e custo configurável, mantendo parâmetros e migração documentados.
B) Cifrar reversivelmente todas as senhas com uma chave fixa compartilhada pela aplicação, mesmo quando só é necessário verificar o conhecimento.
C) Usar hash genérico rápido, sem salt, para reduzir o tempo disponível ao atacante.
D) Armazenar a senha em texto claro e proteger apenas o nome da coluna no banco.

### Questão 42

No modelo simplificado de assinatura digital, assinale a afirmativa correta.

A) O signatário usa a chave pública para assinar, e qualquer verificador precisa conhecer a chave privada.
B) A assinatura torna a mensagem confidencial e impede que o destinatário leia seu conteúdo.
C) Um hash isolado equivale a uma assinatura, porque identifica necessariamente quem o calculou.
D) O signatário usa sua chave privada no algoritmo de assinatura, e a chave pública permite verificar origem e integridade; a assinatura, sozinha, não cifra o conteúdo.

### Questão 43

Ao validar o certificado apresentado por um servidor TLS, o cliente deve verificar:

A) apenas se o certificado contém uma chave pública, independentemente do nome e do prazo.
B) somente se a empresa emissora do site é comercialmente conhecida e não possui reclamações.
C) cadeia até uma âncora confiável, assinaturas, validade, nome esperado, uso de chave e situação de revogação conforme o contexto.
D) apenas se a conexão usa a porta 443, pois a porta garante a identidade do servidor.

### Questão 44

Sobre o TLS 1.3 em nível conceitual, assinale a alternativa correta.

A) O protocolo protege automaticamente dados antes de entrarem no canal e depois de saírem dele, mesmo em endpoint comprometido.
B) Cliente e servidor negociam parâmetros e derivam segredos; o cliente valida a identidade apresentada e, após o handshake, dados da aplicação usam chaves simétricas de sessão e proteção autenticada.
C) O certificado cifra diretamente todo o conteúdo da aplicação com a chave privada do servidor.
D) As mensagens Finished são backups do certificado e substituem a verificação do nome do servidor.

### Questão 45

Sobre WPA2-Personal e WPA3-Personal, assinale a alternativa correta.

A) WPA3-Personal usa SAE; isso dificulta o reaproveitamento de uma captura passiva para tentativas offline como no WPA2-Personal, mas não elimina senha fraca, tentativa online, engenharia social ou falha de implementação.
B) WPA2-Personal usa obrigatoriamente identidade individual por 802.1X e nunca emprega segredo compartilhado.
C) WPA3 elimina a necessidade de atualizar firmware e proteger a administração do ponto de acesso.
D) Qualquer cliente em modo de transição negocia necessariamente WPA3, de modo que o suporte a WPA2 não altera as garantias.

### Questão 46

Em uma rede Wi-Fi institucional com muitos usuários, qual medida melhora a responsabilização individual sem criar uma promessa de invulnerabilidade?

A) Compartilhar uma única senha WPA2-Personal permanente entre todos e desabilitar registros de autenticação.
B) Manter WEP para dispositivos antigos, pois sua compatibilidade compensa a proteção mais fraca.
C) Usar WPA2/WPA3-Enterprise com 802.1X, identidades individuais e validação correta do servidor de autenticação, além de segmentação, atualização e monitoramento.
D) Ativar modo de transição e considerar todos os clientes protegidos exclusivamente por SAE.

### Questão 47

Após detectar indícios de ransomware em várias estações, qual sequência expressa corretamente objetivos distintos da resposta a incidentes?

A) Restaurar imediatamente todos os backups, apagar os logs e depois verificar se havia persistência.
B) Validar e delimitar o incidente, conter sua expansão preservando evidências quando apropriado, erradicar causas e persistência e recuperar para estado conhecido e monitorado.
C) Considerar todo alerta um incidente confirmado, desligar indiscriminadamente o ambiente e encerrar o caso após o bloqueio inicial.
D) Tratar contenção e erradicação como sinônimos e dispensar lições aprendidas quando o serviço voltar.

### Questão 48

Considere duas afirmações sobre recuperação:

I. Na restauração típica, backups incrementais exigem o último completo e a cadeia de incrementais posteriores; backups diferenciais exigem o último completo e o último diferencial.
II. Se um incidente ocorre às 14h, RPO de 30 minutos aponta para recuperação até um ponto não anterior a 13h30, enquanto RTO de 4 horas define a meta de restabelecimento do serviço, e não a frequência das cópias.

Assinale a alternativa correta.

A) Somente I está correta, pois RPO mede o tempo de restauração.
B) Somente II está correta, pois incremental e diferencial possuem a mesma cadeia de restauração.
C) As duas estão incorretas, pois RPO e RTO são valores observados apenas depois do incidente.
D) I e II estão corretas.

### Questão 49

Uma equipe quer tornar sua estratégia de cópias de segurança mais resistente a ransomware. Qual conjunto de medidas é o mais adequado?

A) Manter ao menos uma cópia offline ou logicamente isolada do domínio de produção, usar credenciais separadas e imutabilidade quando adequada, preservar versões e testar periodicamente a restauração.
B) Manter as três cópias on-line sob a mesma credencial administrativa, pois a quantidade impede alteração simultânea.
C) Substituir testes de restauração por comparação do tamanho dos arquivos, já que cópia existente é cópia recuperável.
D) Replicar instantaneamente toda exclusão para as três cópias e eliminar retenção de versões.

### Questão 50

Um portal não pode parar diante da falha de um único servidor e também precisa recuperar versões anteriores após exclusão acidental ou cifração maliciosa. Qual solução atende corretamente aos dois objetivos?

A) Combinar arquitetura redundante ou de alta disponibilidade para reduzir a interrupção com backups versionados, protegidos e testados para recuperar estado anterior.
B) Usar apenas RAID, pois redundância de disco preserva necessariamente qualquer versão excluída ou cifrada.
C) Usar apenas backup semanal, pois a existência de uma cópia garante continuidade sem interrupção e qualquer RTO.
D) Usar somente replicação síncrona, pois ela impede que exclusões e corrupção sejam propagadas ao segundo nó.



## Gabarito do Dia 4

### Questões principais 1–25


| Questão | Resposta |
|---:|:---:|
| 1 | B |
| 2 | D |
| 3 | A |
| 4 | C |
| 5 | B |
| 6 | D |
| 7 | A |
| 8 | C |
| 9 | B |
| 10 | D |
| 11 | A |
| 12 | C |
| 13 | D |
| 14 | B |
| 15 | A |
| 16 | C |
| 17 | D |
| 18 | B |
| 19 | C |
| 20 | A |
| 21 | D |
| 22 | B |
| 23 | A |
| 24 | C |
| 25 | D |



### Questões principais 26–50


| Questão | Gabarito |
|---:|:---:|
| 26 | C |
| 27 | A |
| 28 | D |
| 29 | B |
| 30 | A |
| 31 | D |
| 32 | B |
| 33 | C |
| 34 | D |
| 35 | B |
| 36 | A |
| 37 | C |
| 38 | B |
| 39 | D |
| 40 | C |
| 41 | A |
| 42 | D |
| 43 | C |
| 44 | B |
| 45 | A |
| 46 | C |
| 47 | B |
| 48 | D |
| 49 | A |
| 50 | A |



## Comentários do Dia 4


#### Comentário da Questão 1

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Segurança não é estado binário, e ativos com funções, exposições e impactos diferentes não recebem necessariamente controles idênticos.
- **B)** Correta. A alternativa reúne as etapas essenciais: conhecer ativos e missão, reconhecer ameaças e vulnerabilidades, avaliar probabilidade e impacto, tratar e monitorar o risco.
- **C)** Incorreta. Mudanças tecnológicas, operacionais e no cenário de ameaças exigem reavaliação contínua dos controles.
- **D)** Incorreta. Pessoas, processos, arquitetura, fornecedores e governança também influenciam o risco; ele não se reduz a falhas técnicas.

**Conceito:** segurança da informação como processo contínuo de gestão de riscos.

**Pegadinha:** acreditar em produto mágico ou aplicar a mesma proteção a todo ativo sem considerar contexto e impacto.

**Como pensar:** procure a alternativa que descreva um ciclo de identificação, análise, tratamento e monitoramento, sem prometer segurança absoluta.

**Referência:** [Segurança como gestão de risco](semana_02_estudo.md#s2-d4-gestao-risco).

#### Comentário da Questão 2

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O risco anterior aos controles é o risco inerente ou inicial no modelo considerado; residual é o que permanece depois do tratamento.
- **B)** Incorreta. Controles modificam o risco, mas a gestão não deve prometer risco zero como condição universal de operação.
- **C)** Incorreta. Transferência é uma opção de tratamento, não destino obrigatório; um risco compatível com os critérios organizacionais pode ser aceito.
- **D)** Correta. O risco remanescente precisa ser reavaliado para decidir entre aceitação, tratamento adicional, transferência ou outra resposta cabível.

**Conceito:** risco residual e decisão de tratamento após a aplicação de controles.

**Pegadinha:** confundir risco residual com risco inicial ou afirmar que seu valor deve ser sempre zero, positivo e mensurável, ou transferido.

**Como pensar:** localize primeiro o momento da avaliação: se os controles já foram aplicados, o que resta é residual e ainda exige decisão contextual.

**Referência:** [Segurança como gestão de risco](semana_02_estudo.md#s2-d4-gestao-risco).

#### Comentário da Questão 3

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A perda do suporte não cifrado cria possibilidade de divulgação a pessoa não autorizada, atingindo a confidencialidade.
- **B)** Incorreta. O enunciado não relata alteração ou destruição indevida do conteúdo, que caracterizaria problema de integridade.
- **C)** Incorreta. Não foi indicada impossibilidade de acesso oportuno ao dado ou ao serviço; o foco é a exposição da cópia.
- **D)** Incorreta. Autenticidade pode ser relevante em outros cenários, mas não é o objetivo diretamente descrito pela perda do backup legível.

**Conceito:** confidencialidade como prevenção da divulgação não autorizada.

**Pegadinha:** associar automaticamente qualquer problema com backup à disponibilidade, ignorando que uma cópia perdida pode causar vazamento.

**Como pensar:** identifique o verbo central do dano: copiar ou expor aponta para confidencialidade; alterar, para integridade; impedir acesso, para disponibilidade.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

#### Comentário da Questão 4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmativa I é verdadeira, mas a II também é: cifração não autorizada altera o estado dos arquivos e pode impedir seu uso.
- **B)** Incorreta. A III é falsa. Backup apoia recuperação, porém não impede exfiltração nem garante que não haverá interrupção inicial.
- **C)** Correta. Exfiltração afeta confidencialidade; alteração ou cifração indevida pode afetar integridade e disponibilidade.
- **D)** Incorreta. Inclui a afirmativa III, que exagera o alcance do backup.

**Conceito:** um único incidente pode comprometer simultaneamente os três objetivos da tríade CIA.

**Pegadinha:** limitar ransomware à disponibilidade ou tratar backup como controle capaz de impedir vazamento e interrupção.

**Como pensar:** decomponha o cenário por efeito: saída de dados, mudança indevida e indisponibilidade devem ser classificados separadamente.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia) e [Malware](semana_02_estudo.md#s2-d4-malware).

#### Comentário da Questão 5

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte a ordem: apresentar fatores prova a identidade; consultar permissões decide o que ela pode fazer.
- **B)** Correta. Senha e token participam da autenticação, enquanto o papel funcional é usado na autorização da ação.
- **C)** Incorreta. Accounting registra uso e sessões, e não repúdio oferece evidências contra negação falsa; nenhum dos dois descreve as etapas narradas.
- **D)** Incorreta. Auditoria examina registros e controles; accounting registra uso. O enunciado trata de identidade e permissão.

**Conceito:** autenticação comprova identidade; autorização determina ações permitidas.

**Pegadinha:** concluir que uma identidade validada está automaticamente autorizada a qualquer recurso.

**Como pensar:** faça duas perguntas em sequência: “quem é?” corresponde à autenticação; “o que pode fazer?” corresponde à autorização.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

#### Comentário da Questão 6

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Senha e PIN pertencem à mesma categoria: algo que o usuário sabe.
- **B)** Incorreta. Duas senhas continuam sendo dois elementos de conhecimento, e não fatores de categorias distintas.
- **C)** Incorreta. Impressão digital e reconhecimento facial são duas modalidades biométricas, ambas da categoria “algo que é”.
- **D)** Correta. A senha é algo que o usuário sabe, e o token é algo que possui.

**Conceito:** MFA requer fatores pertencentes a categorias diferentes de autenticação.

**Pegadinha:** contar o número de credenciais sem verificar a categoria de cada uma.

**Como pensar:** classifique cada elemento como conhecimento, posse ou inerência; só depois verifique se há diversidade de categorias.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

#### Comentário da Questão 7

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. ABAC toma decisões com base em atributos do sujeito, recurso, ação e contexto, como dispositivo e horário.
- **B)** Incorreta. RBAC associa permissões a papéis ou funções; a política descrita ultrapassa o uso exclusivo do cargo.
- **C)** Incorreta. Biometria é mecanismo possível de autenticação e não o modelo de autorização apresentado.
- **D)** Incorreta. Accounting registra sessões e ações; não é o mecanismo que decide o acesso pelos atributos mencionados.

**Conceito:** autorização baseada em atributos, em contraste com autorização baseada em papéis.

**Pegadinha:** chamar qualquer decisão vinculada ao usuário de RBAC, mesmo quando o contexto e os atributos do recurso participam da política.

**Como pensar:** se a decisão combina várias características do sujeito, objeto, ação e ambiente, reconheça ABAC; se gira em torno da função, pense em RBAC.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

#### Comentário da Questão 8

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confirmar identidade é função de Authentication, o primeiro A.
- **B)** Incorreta. Aplicar permissões é função de Authorization, o segundo A.
- **C)** Correta. Accounting registra consumo, sessões e ações e pode alimentar a auditoria, que é atividade mais ampla de exame de registros, controles e conformidade.
- **D)** Incorreta. Um registro local desprotegido não produz, por si só, não repúdio; são necessários integridade, identidade, tempo e contexto confiáveis.

**Conceito:** AAA significa Authentication, Authorization e Accounting.

**Pegadinha:** traduzir o terceiro A simplesmente como auditoria e tratar accounting e auditoria como sinônimos perfeitos.

**Como pensar:** associe os três verbos: identificar, permitir e registrar; depois lembre que auditoria analisa os registros e os controles.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

#### Comentário da Questão 9

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Hash isolado pode ser calculado por qualquer pessoa e não vincula o documento a uma identidade determinada.
- **B)** Correta. Assinatura digital pode apoiar integridade, autenticidade de origem e não repúdio, desde que chave, identidade, certificado, tempo e procedimentos sejam confiáveis.
- **C)** Incorreta. Como todos os participantes conhecem o mesmo segredo, qualquer um deles poderia produzir a proteção simétrica; não há atribuição exclusiva ao autor.
- **D)** Incorreta. Nome autodeclarado em arquivo alterável é evidência fraca e não assegura integridade nem vínculo confiável.

**Conceito:** não repúdio apoiado por assinatura digital e por uma cadeia adequada de evidências.

**Pegadinha:** imaginar que hash ou segredo compartilhado identifica de modo exclusivo quem praticou a ação.

**Como pensar:** pergunte se apenas o suposto autor controla o mecanismo de produção da prova e se terceiros conseguem verificar o vínculo de identidade.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

#### Comentário da Questão 10

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Horário isolado não permite atribuir a ação nem compreender origem, recurso e resultado.
- **B)** Incorreta. Permitir alteração irrestrita pelos próprios examinados compromete a integridade e o valor probatório dos registros.
- **C)** Incorreta. Volume sem sincronização, retenção, contexto e capacidade de análise não gera rastreabilidade eficaz.
- **D)** Correta. Logs úteis devem combinar contexto suficiente, relógios sincronizados, retenção, proteção de acesso e integridade, além de monitoramento ou análise.

**Conceito:** requisitos de registros úteis para accounting, auditoria e investigação.

**Pegadinha:** supor que registrar tudo basta, mesmo que os dados não possam ser correlacionados ou tenham sido alterados.

**Como pensar:** verifique se o log responde quem, o quê, quando, de onde, sobre qual recurso e com qual resultado, preservando sua confiabilidade.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

#### Comentário da Questão 11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A sequência atribui valor ao portal, capacidade de dano ao grupo, fraqueza ao gateway, observabilidade às tentativas e comprometimento confirmado ao acesso.
- **B)** Incorreta. Inverte quase todas as categorias: o portal não é ameaça, e o grupo criminoso não é vulnerabilidade.
- **C)** Incorreta. O portal é ativo, não controle; a falha é vulnerabilidade, não incidente por si só.
- **D)** Incorreta. A tentativa observada é evento, e o acesso indevido confirmado é incidente, não mero risco.

**Conceito:** distinção operacional entre ativo, ameaça, vulnerabilidade, evento e incidente.

**Pegadinha:** classificar o mesmo elemento pelo dano possível em vez de observar sua função concreta no cenário.

**Como pensar:** associe cada termo a uma pergunta: “o que tem valor?”, “quem ou o que pode causar dano?”, “qual é a fraqueza?”, “o que foi observado?” e “o que foi comprometido?”.

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

#### Comentário da Questão 12

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A presença de uma falha explorável não demonstra que houve exploração ou comprometimento.
- **B)** Incorreta. O serviço é o ativo; a chance e o impacto são componentes usados na avaliação do risco.
- **C)** Correta. A versão falha constitui vulnerabilidade, e o risco depende da combinação contextual de probabilidade e impacto adverso.
- **D)** Incorreta. Vulnerabilidade é a fraqueza; risco é a possibilidade avaliada de dano, e os conceitos não são sinônimos.

**Conceito:** vulnerabilidade como fraqueza e risco como combinação de probabilidade e impacto.

**Pegadinha:** transformar automaticamente toda vulnerabilidade em incidente ou usar vulnerabilidade e risco como termos intercambiáveis.

**Como pensar:** primeiro identifique a fraqueza; depois avalie a possibilidade e a consequência de ela ser explorada.

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

#### Comentário da Questão 13

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Um alerta pode ser falso positivo ou ter alcance diferente do inicialmente sugerido; precisa de validação e correlação.
- **B)** Incorreta. Vulnerabilidade é fraqueza explorável, não o alerta nem a ação de copiar dados.
- **C)** Incorreta. A identificação nominal do atacante não é condição para classificar uma cópia não autorizada confirmada como incidente.
- **D)** Correta. O alerta é evento observável; a comprovação do uso indevido e da cópia caracteriza comprometimento concreto.

**Conceito:** evento observado em contraste com incidente de segurança confirmado.

**Pegadinha:** chamar todo alerta de incidente ou exigir que o autor seja identificado para reconhecer o comprometimento.

**Como pensar:** se há somente sinal a validar, trate-o como evento; se a violação ou ameaça concreta à política foi confirmada, há incidente.

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

#### Comentário da Questão 14

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A alternativa troca os conceitos: o agente capaz de causar dano é ameaça, e a falha explorável é vulnerabilidade.
- **B)** Correta. O criminoso representa ameaça, a falha representa vulnerabilidade e a correção ou o MFA são medidas que modificam o risco.
- **C)** Incorreta. Evento é ocorrência observada; controle precisa atuar para modificar o risco, ainda que tenha funções variadas.
- **D)** Incorreta. Vulnerabilidade pode existir sem exploração; o incidente exige ocorrência concreta que comprometa ou ameace comprometer a segurança.

**Conceito:** controle como medida de modificação do risco e sua relação com ameaça e vulnerabilidade.

**Pegadinha:** confundir a causa potencial, a fraqueza e a medida de proteção por todos participarem do mesmo cenário.

**Como pensar:** leia o cenário como cadeia: ameaça explora vulnerabilidade; controles reduzem probabilidade, impacto ou ambos.

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

#### Comentário da Questão 15

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O vírus se associa a hospedeiro e à execução correspondente, enquanto o worm possui capacidade característica de autopropagação.
- **B)** Incorreta. Inverte as características centrais de vírus e worm.
- **C)** Incorreta. Malware é a categoria ampla; vírus e worm são categorias com comportamentos distintos, embora uma amostra possa combinar técnicas.
- **D)** Incorreta. Coleta de informações descreve spyware, e cifração extorsiva remete a ransomware; não são as diferenças definidoras entre vírus e worm.

**Conceito:** distinção entre vírus dependente de hospedeiro e worm com propagação automática.

**Pegadinha:** chamar todo malware de vírus ou definir as categorias apenas pela carga executada depois da infecção.

**Como pensar:** observe o mecanismo de propagação: vínculo a arquivo ou programa aponta para vírus; autopropagação pela rede aponta para worm.

**Referência:** [Malware](semana_02_estudo.md#s2-d4-malware).

#### Comentário da Questão 16

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Worm tem como característica marcante a propagação automática; o cenário enfatiza disfarce e indução à execução.
- **B)** Incorreta. Não há referência a infecção de setor de inicialização ou vínculo viral a hospedeiro.
- **C)** Correta. Cavalo de Troia se apresenta como software legítimo ou desejável para levar a vítima a executá-lo, sem exigir autorreplicação.
- **D)** Incorreta. DDoS é ataque distribuído à disponibilidade, não um programa disfarçado instalado pelo usuário.

**Conceito:** cavalo de Troia definido pelo disfarce e pela indução à execução.

**Pegadinha:** classificar qualquer programa que abre acesso remoto como worm, ainda que não exista autopropagação.

**Como pensar:** identifique a característica escolhida pelo enunciado: aparência legítima e execução induzida são sinais de Troia.

**Referência:** [Malware](semana_02_estudo.md#s2-d4-malware).

#### Comentário da Questão 17

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Spyware foca coleta de informações, e ransomware moderno não se limita à disponibilidade.
- **B)** Incorreta. Backup pode apoiar a recuperação, mas não contém o invasor, não remove persistência e não desfaz a exfiltração.
- **C)** Incorreta. A existência de outra cópia não torna autorizada a alteração dos arquivos em produção nem preserva sua integridade naquele ambiente.
- **D)** Correta. Campanhas de ransomware podem combinar roubo, alteração, cifração e interrupção, comprometendo toda a tríade CIA.

**Conceito:** alcance do ransomware e sobreposição de categorias e efeitos de malware.

**Pegadinha:** reduzir ransomware à cifração local ou acreditar que backup resolve confidencialidade e erradicação.

**Como pensar:** avalie separadamente o que saiu do ambiente, o que foi alterado e o que ficou indisponível.

**Referência:** [Malware](semana_02_estudo.md#s2-d4-malware) e [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

#### Comentário da Questão 18

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Rootkit busca ocultação ou manutenção de privilégio; o conjunto de máquinas ou agentes controlados é a botnet.
- **B)** Correta. A alternativa associa corretamente coleta a spyware, ocultação ou privilégio a rootkit e controle coletivo de bots a botnet.
- **C)** Incorreta. Bot é agente controlado remotamente ou, por extensão, o host que o executa; vírus é malware ligado a hospedeiro.
- **D)** Incorreta. Cifração extorsiva descreve ransomware, SMS fraudulento remete a smishing, e falha de configuração é vulnerabilidade.

**Conceito:** spyware, rootkit, bot e botnet como categorias distintas de malware.

**Pegadinha:** definir malware pelo uso posterior do host, como DDoS, em vez de reconhecer sua função ou mecanismo característico.

**Como pensar:** associe cada nome ao núcleo: spyware observa, rootkit oculta, bot recebe comandos e botnet reúne bots.

**Referência:** [Malware](semana_02_estudo.md#s2-d4-malware).

#### Comentário da Questão 19

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Inverte os canais: smishing emprega SMS ou mensagem; vishing emprega voz.
- **B)** Incorreta. Whaling é direcionado a pessoa de alta relevância, e não simples campanha genérica.
- **C)** Correta. A alternativa relaciona corretamente especificidade do alvo, relevância da vítima e canais usados.
- **D)** Incorreta. Phishing pode buscar credenciais, pagamento ou outra ação sem anexar ou executar malware.

**Conceito:** variações de phishing segundo alvo e canal.

**Pegadinha:** trocar smishing por vishing ou definir phishing pela presença obrigatória de arquivo malicioso.

**Como pensar:** separe duas dimensões: spear e whaling descrevem o alvo; smishing e vishing destacam o canal.

**Referência:** [Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing).

#### Comentário da Questão 20

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Autoridade aparente e urgência são gatilhos de engenharia social; a confirmação deve ocorrer por canal independente e pelo processo regular.
- **B)** Incorreta. A pressão por rapidez é justamente um motivo para não contornar controles de autorização.
- **C)** Incorreta. Responder à mesma conta não constitui canal independente, pois a conta pode estar falsificada ou comprometida.
- **D)** Incorreta. Engenharia social pode induzir pagamento ou alteração de cadastro sem usar malware.

**Conceito:** manipulação por autoridade, urgência e pretexto, com verificação por canal independente.

**Pegadinha:** validar uma solicitação pelo mesmo canal potencialmente comprometido ou procurar apenas anexos maliciosos.

**Como pensar:** quando a mensagem pede exceção urgente ou mudança sensível, interrompa o impulso e confirme identidade e autorização fora daquele fluxo.

**Referência:** [Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing).

#### Comentário da Questão 21

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. MFA não impede que uma página fraudulenta seja apresentada nem que o usuário seja manipulado.
- **B)** Incorreta. Sessão capturada ou recuperação de conta comprometida pode contornar a proteção esperada dos fatores.
- **C)** Incorreta. Duas senhas são dois elementos da mesma categoria de conhecimento e não constituem MFA.
- **D)** Correta. MFA reduz o impacto da senha roubada, mas não elimina captura de sessão, aprovação induzida e abuso de recuperação.

**Conceito:** alcance e limites do MFA diante de phishing.

**Pegadinha:** converter redução de risco em garantia absoluta ou contar duas credenciais de conhecimento como fatores distintos.

**Como pensar:** identifique qual etapa o ataque contorna: roubo apenas da senha é diferente de captura da sessão ou manipulação do segundo fator.

**Referência:** [Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing).

#### Comentário da Questão 22

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Captura de pacotes descreve sniffing; spoofing envolve falsificação de identidade ou origem aparente.
- **B)** Correta. Spoofing pode atingir IP, ARP, DNS, e-mail e outros identificadores, com efeitos dependentes do protocolo.
- **C)** Incorreta. O ataque não exige comprometimento de autoridade certificadora e pode ocorrer em protocolos sem certificados.
- **D)** Incorreta. DDoS caracteriza distribuição das origens e objetivo de indisponibilidade; não é sinônimo de falsificação.

**Conceito:** spoofing como falsificação de identidade ou origem aparente.

**Pegadinha:** confundir falsificação com observação do tráfego ou supor que um IP de origem falso assegura o recebimento das respostas.

**Como pensar:** procure o elemento enganoso do endereço ou da identidade apresentada; depois avalie o efeito conforme o protocolo envolvido.

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).

#### Comentário da Questão 23

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Sniffing captura e analisa tráfego, inclusive legitimamente; o atacante on-path ocupa o caminho e pode observar e modificar a troca.
- **B)** Incorreta. Sniffing pode ser passivo, e o ataque on-path não se limita a metadados.
- **C)** Incorreta. Criptografia mal validada pode falhar, como quando o cliente aceita certificado falso ou uma chave foi comprometida.
- **D)** Incorreta. Switches dificultam a escuta indiscriminada, mas um agente com posição privilegiada, spoofing, espelhamento indevido ou equipamento comprometido ainda pode capturar tráfego.

**Conceito:** captura por sniffing em contraste com interceptação ativa on-path ou man-in-the-middle (MITM).

**Pegadinha:** afirmar que sniffing sempre altera dados ou que a mera presença de criptografia resolve validação e confiança.

**Como pensar:** diferencie observar de ocupar o caminho; em seguida, verifique se o canal criptográfico também autentica corretamente o par.

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).

#### Comentário da Questão 24

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Credential stuffing reutiliza credenciais vazadas; força bruta testa combinações em busca da senha.
- **B)** Incorreta. Dicionário usa candidatos prováveis, mas o padrão de poucas senhas contra muitas contas é password spraying; stuffing não é spoofing de IP.
- **C)** Correta. Password spraying distribui poucas senhas comuns por muitas contas, enquanto credential stuffing testa pares já expostos em outros serviços.
- **D)** Incorreta. Phishing manipula a vítima, e credential stuffing não depende exclusivamente de falha de memória.

**Conceito:** força bruta, dicionário, password spraying e credential stuffing.

**Pegadinha:** olhar apenas para o uso de senhas comuns e ignorar se as tentativas se concentram em uma conta ou se distribuem entre muitas.

**Como pensar:** observe a origem dos candidatos e a distribuição: lista curta em muitas contas é spraying; pares vazados são stuffing.

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).

#### Comentário da Questão 25

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. DDoS utiliza múltiplas origens, e um firewall local não recupera um enlace que já chegou saturado.
- **B)** Incorreta. Negação de serviço compromete disponibilidade; distribuição das origens não aumenta confidencialidade.
- **C)** Incorreta. IDS fora de banda pode detectar e alertar, mas não cria capacidade no enlace nem bloqueia, sozinho, o volume a montante.
- **D)** Correta. Uma botnet caracteriza origem distribuída, e a mitigação pode precisar ocorrer no provedor ou em infraestrutura com capacidade anterior ao gargalo.

**Conceito:** DDoS e limites de controles instalados depois do ponto de saturação.

**Pegadinha:** acreditar que qualquer firewall local absorve tráfego que já esgotou o enlace de acesso.

**Como pensar:** localize o gargalo e o ponto de controle: se a saturação acontece antes do perímetro local, a resposta precisa começar a montante.

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).


### Comentário da Questão 26

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Treinamento é controle administrativo, IDS é técnico e backup não tem como função predominante dissuadir.
- **B)** Incorreta. Os controles têm naturezas e funções diferentes; backup testado atua principalmente na recuperação.
- **C)** Correta. A classificação associa adequadamente treinamento a prevenção administrativa, IDS à detecção técnica e backup à recuperação.
- **D)** Incorreta. IDS não é controle físico, e não há base para classificar treinamento e backup exclusivamente como compensatórios.

**Conceito:** classificação de controles por natureza e por função.

**Pegadinha:** presumir que todo controle ligado a sistemas seja técnico ou que um controle possa exercer apenas função preventiva.

**Como pensar:** faça duas perguntas separadas: de que natureza é a medida e em qual momento ou objetivo ela atua predominantemente.

**Referência:** [8. Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles), [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips) e [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).

### Comentário da Questão 27

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Uma única credencial comprometida pode atingir várias camadas e criar falha comum, reduzindo a independência prática da defesa.
- **B)** Incorreta. Quantidade de controles não elimina risco residual, especialmente quando todos compartilham a mesma dependência crítica.
- **C)** Incorreta. Defesa em profundidade busca camadas complementares; não exige fabricante único nem dependência administrativa comum.
- **D)** Incorreta. Backup apoia recuperação, mas não substitui prevenção, limitação de movimento lateral ou proteção de identidade.

**Conceito:** independência e complementaridade das camadas de defesa em profundidade.

**Pegadinha:** contar produtos sem investigar dependências compartilhadas e concluir que muitas camadas equivalem a risco zero.

**Como pensar:** procure o ponto cuja falha atravessaria várias barreiras; ele revela se a profundidade é real ou apenas aparente.

**Referência:** [8. Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles).

### Comentário da Questão 28

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A filtragem sem estado avalia pacotes individualmente; acompanhar o estado da conexão é característica do firewall stateful.
- **B)** Incorreta. Porta permitida pode transportar conteúdo malicioso, e o firewall não corrige falhas da aplicação.
- **C)** Incorreta. Uma ameaça interna pode não atravessar o ponto observado pelo firewall de borda.
- **D)** Correta. Stateful descreve o acompanhamento da conexão, sem transformar o controle em garantia contra toda vulnerabilidade ou política ruim.

**Conceito:** filtragem stateful e limites do firewall.

**Pegadinha:** converter uma capacidade verdadeira — acompanhar estado — em promessa de segurança completa para a aplicação.

**Como pensar:** separe a decisão sobre o fluxo da segurança do conteúdo e do software que recebe esse fluxo.

**Referência:** [9. Firewall](semana_02_estudo.md#s2-d4-firewall).

### Comentário da Questão 29

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Portas altas também podem transportar ataques; origem, destino, protocolo e necessidade devem orientar a regra.
- **B)** Correta. A alternativa reúne negação por padrão quando adequada, mínimo necessário, documentação, revisão, logs e consciência do limite de visibilidade.
- **C)** Incorreta. Controle de saída pode limitar comunicação indevida e exfiltração; ataques não se restringem a conexões iniciadas externamente.
- **D)** Incorreta. Regras precisam de revisão periódica e testes após mudanças; torná-las permanentes favorece excesso de permissão.

**Conceito:** elaboração e manutenção de política de firewall.

**Pegadinha:** confiar na numeração da porta ou no primeiro teste em vez de avaliar necessidade e ciclo de vida da regra.

**Como pensar:** valide quem fala com quem, por qual serviço, por qual necessidade, com qual registro e por quanto tempo.

**Referência:** [9. Firewall](semana_02_estudo.md#s2-d4-firewall).

### Comentário da Questão 30

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Um IDS de rede pode receber cópia do tráfego fora do caminho direto e gerar alertas sem bloquear a produção.
- **B)** Incorreta. IPS em linha atua em posição preventiva e pode descartar ou interromper tráfego.
- **C)** Incorreta. Firewall aplica política de fluxo; configurá-lo como backup não cria o sensor descrito.
- **D)** Incorreta. VPN protege um túnel, mas não cumpre por si a função de detecção solicitada.

**Conceito:** posicionamento e função de um IDS.

**Pegadinha:** confundir qualquer ferramenta que inspeciona tráfego com um controle de bloqueio em linha.

**Como pensar:** a expressão “receber cópia e alertar sem bloquear” aponta diretamente para detecção fora de banda.

**Referência:** [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips).

### Comentário da Questão 31

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Alerta ou classificação automatizada não constitui prova definitiva de incidente.
- **B)** Incorreta. Como atua em linha, um IPS pode afetar disponibilidade ao bloquear tráfego legítimo.
- **C)** Incorreta. Classificar tráfego legítimo como malicioso é falso positivo; falso negativo ocorre quando um ataque não é detectado ou impedido.
- **D)** Correta. A regra produziu falso positivo e o bloqueio preventivo atingiu a disponibilidade do serviço.

**Conceito:** falsos positivos, falsos negativos e impacto operacional de IPS.

**Pegadinha:** trocar falso positivo por falso negativo ou imaginar que prevenção automática não tem custo de disponibilidade.

**Como pensar:** pergunte primeiro se o evento era ataque; depois compare a realidade com a decisão do controle.

**Referência:** [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips).

### Comentário da Questão 32

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Reunir banco e serviço exposto no mesmo segmento amplia o impacto de um comprometimento.
- **B)** Correta. O componente público fica na DMZ, enquanto aplicação e banco recebem proteção adicional e somente fluxos necessários são liberados.
- **C)** Incorreta. Base interna sensível não deve ser publicada diretamente na internet; a DMZ destina-se aos serviços expostos.
- **D)** Incorreta. Deve-se presumir que o serviço exposto pode ser comprometido e monitorar rigorosamente seus fluxos para dentro.

**Conceito:** DMZ como segmento intermediário e contenção da exposição.

**Pegadinha:** interpretar DMZ como rede confiável, livre de controles ou apropriada para todos os componentes da aplicação.

**Como pensar:** aproxime da internet apenas o indispensável e imponha nova barreira antes dos dados sensíveis.

**Referência:** [11. DMZ](semana_02_estudo.md#s2-d4-dmz).

### Comentário da Questão 33

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O túnel não remove malware nem corrige o estado do equipamento remoto.
- **B)** Incorreta. Confidencialidade do canal não equivale a autorização irrestrita dentro da organização.
- **C)** Correta. A VPN protege o percurso, mas precisa ser combinada com identidade, postura, segmentação, privilégio mínimo e monitoramento.
- **D)** Incorreta. Credenciais podem ser roubadas, e gateway vulnerável pode ser explorado; MFA e correção continuam relevantes.

**Conceito:** benefícios e limites de uma VPN de acesso remoto.

**Pegadinha:** transferir a confiança criptográfica do túnel para o endpoint ou para todas as ações do usuário.

**Como pensar:** divida o cenário em canal, endpoint, identidade e autorização; a VPN resolve apenas parte desses problemas.

**Referência:** [12. VPN](semana_02_estudo.md#s2-d4-vpn).

### Comentário da Questão 34

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Os modelos foram invertidos: site-to-site conecta redes; acesso remoto atende usuário ou dispositivo.
- **B)** Incorreta. IPsec protege na camada IP, enquanto soluções TLS VPN têm escopo definido pela solução; a alternativa troca essas características.
- **C)** Incorreta. Criar túnel não elimina autorização, segmentação ou menor privilégio.
- **D)** Correta. A associação dos modelos está correta e reconhece os controles necessários ao redor do túnel.

**Conceito:** VPN site-to-site, VPN de acesso remoto e tecnologias de proteção.

**Pegadinha:** confundir alcance do túnel com autorização total ou inverter IPsec e TLS.

**Como pensar:** identifique primeiro os extremos: rede com rede indica site-to-site; usuário ou dispositivo com organização indica acesso remoto.

**Referência:** [12. VPN](semana_02_estudo.md#s2-d4-vpn).

### Comentário da Questão 35

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A VLAN restringe ataques locais de camada 2, mas não impede tráfego que o roteamento inter-VLAN autoriza.
- **B)** Correta. VLANs criam separação operacional e de broadcast; ACLs ou firewalls internos aplicam a política aos fluxos roteados.
- **C)** Incorreta. Os controles têm funções complementares, não idênticas, e podem ser usados em conjunto.
- **D)** Incorreta. Segmentação pode empregar VLANs, sub-redes, ACLs, VRFs, firewalls internos e microsegmentação.

**Conceito:** segmentação de camada 2 e controle do movimento lateral roteado.

**Pegadinha:** transformar a separação de broadcast em bloqueio automático de toda comunicação entre redes.

**Como pensar:** acompanhe o pacote: se há roteamento entre VLANs, verifique qual política limita esse novo caminho.

**Referência:** [13. Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao).

### Comentário da Questão 36

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Menor privilégio limita operação, recurso, origem e contexto ao necessário e requer revisão ao longo do tempo.
- **B)** Incorreta. Conta administrativa compartilhada amplia impacto, dificulta responsabilização e viola separação de funções.
- **C)** Incorreta. Autenticação comprova identidade; autorização ainda deve decidir o que essa identidade pode fazer.
- **D)** Incorreta. Estar em VLAN separada não justifica liberar portas e fluxos sem necessidade.

**Conceito:** menor privilégio aplicado a contas de serviço e fluxos entre segmentos.

**Pegadinha:** presumir que autenticação ou separação lógica já conceda qualquer permissão necessária.

**Como pensar:** restrinja simultaneamente sujeito, ação, objeto e contexto ao mínimo exigido pela missão.

**Referência:** [13. Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao) e [3. Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

### Comentário da Questão 37

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Uma cifra simétrica usa segredo compartilhado e costuma ser eficiente para dados volumosos.
- **B)** Incorreta. Par de chaves caracteriza criptografia assimétrica, que pode apoiar assinaturas.
- **C)** Correta. AES exemplifica cifra simétrica; mecanismos assimétricos empregam chaves pública e privada e atendem finalidades como assinatura e estabelecimento.
- **D)** Incorreta. O efeito depende do algoritmo e do esquema; assinar com chave privada não torna o conteúdo confidencial.

**Conceito:** chaves, eficiência e aplicações da criptografia simétrica e assimétrica.

**Pegadinha:** associar mecanicamente chave privada a confidencialidade ou trocar a quantidade de chaves dos modelos.

**Como pensar:** para volume, lembre a eficiência simétrica; para identidade, assinatura ou estabelecimento, avalie o par assimétrico.

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia).

### Comentário da Questão 38

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. TLS não cifra todo o tráfego diretamente com a chave privada do servidor.
- **B)** Correta. O desenho híbrido aproveita mecanismos assimétricos ou PSK para autenticação e estabelecimento e cifras simétricas para a sessão.
- **C)** Incorreta. Hash não é reversível e não fornece confidencialidade por si só.
- **D)** Incorreta. Certificado não elimina o uso eficiente de chaves simétricas após o handshake.

**Conceito:** criptografia híbrida e divisão de funções no TLS.

**Pegadinha:** imaginar que a chave do certificado cifra diretamente cada byte da aplicação.

**Como pensar:** separe a fase de estabelecer confiança e segredos da fase de transportar grande volume de dados.

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia) e [17. TLS](semana_02_estudo.md#s2-d4-tls).

### Comentário da Questão 39

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Funções hash comuns podem ser calculadas sem chave privada.
- **B)** Incorreta. Hash produz resumo e não cifra nem impede a substituição do arquivo.
- **C)** Incorreta. Tamanho igual de entrada não obriga hashes iguais; resistência a colisões é propriedade desejada.
- **D)** Correta. Se arquivo e referência são adulterados juntos, a comparação coincide; a referência precisa de origem confiável ou proteção autenticada.

**Conceito:** uso de hash para detectar alteração e necessidade de referência confiável.

**Pegadinha:** tratar a publicação do resumo ao lado do arquivo como prova autônoma de integridade.

**Como pensar:** antes de confiar no resultado da comparação, pergunte quem protegeu o valor de referência.

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas).

### Comentário da Questão 40

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Hash sem segredo pode detectar alteração diante de referência confiável, mas não autentica por si a origem da mensagem.
- **B)** Incorreta. Armazenamento reversível de senha não é o mecanismo de autenticação de mensagem solicitado.
- **C)** Correta. HMAC combina função hash e segredo compartilhado para oferecer integridade e autenticação entre quem conhece a chave.
- **D)** Incorreta. Certificado sem validação e sem prova de posse não satisfaz o requisito descrito.

**Conceito:** HMAC como código de autenticação de mensagem com segredo compartilhado.

**Pegadinha:** atribuir a hash simples autenticação de origem ou a HMAC não repúdio forte entre as partes.

**Como pensar:** havendo segredo compartilhado e necessidade de autenticar a mensagem, procure MAC ou HMAC; não repúdio exigiria outra estrutura.

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas).

### Comentário da Questão 41

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. KDF apropriada, salt único e custo configurável elevam o trabalho de tentativa e evitam reaproveitamento simples de bases pré-computadas.
- **B)** Incorreta. Criptografia reversível cria exposição desnecessária quando basta verificar o conhecimento da senha.
- **C)** Incorreta. Hash rápido sem salt favorece tentativas em massa e tabelas pré-computadas.
- **D)** Incorreta. Texto claro expõe imediatamente todas as credenciais em caso de acesso à base.

**Conceito:** armazenamento seguro de senhas com função de derivação, salt e custo.

**Pegadinha:** escolher algoritmo rápido por desempenho da aplicação, ignorando que rapidez também beneficia o atacante.

**Como pensar:** a verificação deve ser deliberadamente custosa e individualizada por senha, sem exigir recuperar o segredo original.

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas).

### Comentário da Questão 42

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. No modelo apresentado, o signatário usa a chave privada e o verificador usa a pública.
- **B)** Incorreta. Assinatura protege origem e integridade, mas não fornece confidencialidade sozinha.
- **C)** Incorreta. Qualquer pessoa pode calcular hash sem segredo; o resumo isolado não identifica o autor.
- **D)** Correta. A alternativa descreve corretamente as chaves e limita o alcance da assinatura.

**Conceito:** geração, verificação e propriedades da assinatura digital.

**Pegadinha:** inverter as chaves ou confundir assinatura de dados com cifração do conteúdo.

**Como pensar:** assinatura responde “quem vinculou sua chave privada a estes dados e eles mudaram?”, não “quem consegue lê-los?”.

**Referência:** [16. Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado).

### Comentário da Questão 43

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A mera presença de chave pública não valida identidade, prazo nem finalidade do certificado.
- **B)** Incorreta. Certificado não atesta honestidade comercial; ele vincula identidade ou nome à chave segundo a validação realizada.
- **C)** Correta. Cadeia, assinatura, validade, nome, uso da chave e revogação contextual compõem a validação de certificado X.509.
- **D)** Incorreta. Porta 443 é convenção de serviço, não prova criptográfica da identidade do servidor.

**Conceito:** validação de certificado X.509 usado por servidor.

**Pegadinha:** validar apenas a cadeia e esquecer o nome esperado, ou atribuir ao certificado uma garantia sobre comportamento comercial.

**Como pensar:** confira quem assinou, para qual nome, em qual período, para qual uso e se a credencial continua aceitável.

**Referência:** [16. Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado).

### Comentário da Questão 44

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. TLS protege o canal; não corrige o endpoint nem protege automaticamente dados fora desse canal.
- **B)** Correta. A alternativa resume negociação, derivação de segredos, validação de identidade e proteção simétrica autenticada dos dados.
- **C)** Incorreta. Certificado apresenta vínculo e chave para autenticação; ele não cifra diretamente todo o conteúdo com a chave privada.
- **D)** Incorreta. Finished confirma integridade do handshake, mas não substitui a validação do nome e da cadeia.

**Conceito:** fluxo conceitual e propriedades do TLS 1.3.

**Pegadinha:** reduzir TLS a certificado ou estender a proteção do canal aos endpoints e à aplicação inteira.

**Como pensar:** percorra o handshake: negociar, derivar, autenticar, confirmar e então transportar com chaves de sessão.

**Referência:** [17. TLS](semana_02_estudo.md#s2-d4-tls).

### Comentário da Questão 45

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. SAE muda a troca autenticada por senha e dificulta o uso passivo de captura como verificador offline, sem criar invulnerabilidade.
- **B)** Incorreta. WPA2-Personal usa segredo pré-compartilhado; identidade individual por 802.1X caracteriza o modo Enterprise.
- **C)** Incorreta. WPA3 não elimina falhas de firmware, configuração ou administração.
- **D)** Incorreta. No modo de transição, clientes legados ainda podem negociar WPA2-Personal.

**Conceito:** diferença entre WPA2-Personal e WPA3-Personal com SAE.

**Pegadinha:** concluir que SAE torna senha fraca segura ou que o modo de transição equivale a WPA3 puro.

**Como pensar:** identifique o modo realmente negociado e depois avalie senha, implementação, endpoint e configuração.

**Referência:** [18. Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi).

### Comentário da Questão 46

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Segredo permanente compartilhado dificulta revogação e responsabilização individual.
- **B)** Incorreta. WEP é legado e não deve ser mantido como solução de segurança.
- **C)** Correta. Enterprise com 802.1X e identidades individuais melhora controle e rastreabilidade, desde que a validação e os demais controles sejam corretos.
- **D)** Incorreta. Modo de transição pode negociar WPA2 com cliente legado; não garante SAE em toda associação.

**Conceito:** segurança Wi-Fi institucional em modo Enterprise.

**Pegadinha:** confundir compatibilidade com segurança ou presumir que o nome WPA3 no ponto de acesso revela o modo de todos os clientes.

**Como pensar:** para muitos usuários, procure identidade individual, validação do servidor e capacidade de revogar acesso sem trocar segredo coletivo.

**Referência:** [18. Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi).

### Comentário da Questão 47

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Restaurar antes de conter e erradicar pode reinfectar o ambiente, e apagar logs destrói evidências.
- **B)** Correta. A sequência distingue detecção e análise, contenção, erradicação e recuperação validada, preservando evidência conforme o caso.
- **C)** Incorreta. Alerta não é incidente confirmado, e desligamento indiscriminado pode destruir evidência ou ampliar o impacto operacional.
- **D)** Incorreta. Contenção limita expansão; erradicação remove causa e persistência; lições aprendidas retroalimentam os controles.

**Conceito:** objetivos distintos no ciclo de resposta a incidentes.

**Pegadinha:** tratar bloqueio temporário como remoção completa ou restaurar apenas porque há backup.

**Como pensar:** pergunte em ordem: o que ocorreu, como limitar, como remover a causa e como voltar com confiança.

**Referência:** [19. Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes).

### Comentário da Questão 48

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmação II também está correta; RPO trata do ponto de recuperação e da janela tolerada de perda.
- **B)** Incorreta. A cadeia típica difere: incrementais dependem de todos os incrementais posteriores ao completo; diferencial usa o mais recente.
- **C)** Incorreta. RPO e RTO são objetivos definidos previamente, usados depois para avaliar o resultado observado.
- **D)** Correta. As duas afirmações descrevem adequadamente restauração típica e os significados de RPO e RTO.

**Conceito:** backup incremental e diferencial, RPO e RTO.

**Pegadinha:** confundir a quantidade de conjuntos de restauração, chamar RPO de duração ou chamar RTO de frequência de cópia.

**Como pensar:** RPO olha para trás, ao ponto aceitável dos dados; RTO olha para a frente, ao prazo de retorno do serviço.

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).

### Comentário da Questão 49

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Cópia offline ou isolada, credenciais separadas, imutabilidade adequada, versionamento e testes reduzem a chance de perder simultaneamente produção e recuperação.
- **B)** Incorreta. A mesma credencial e exposição on-line constituem falha comum capaz de comprometer todas as cópias.
- **C)** Incorreta. Existência e tamanho não provam que a restauração seja íntegra, completa e operacional.
- **D)** Incorreta. Replicação pode propagar exclusão ou cifração; retenção de versões é importante para retornar a estado anterior.

**Conceito:** proteção de backups contra ransomware e validação de restauração.

**Pegadinha:** contar cópias sem avaliar isolamento administrativo, mutabilidade, histórico e capacidade real de restaurar.

**Como pensar:** imagine o atacante com credenciais de produção e pergunte quais cópias ele ainda não consegue alterar ou excluir.

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).

### Comentário da Questão 50

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Alta disponibilidade ou redundância atende à continuidade diante de falha; backup versionado atende à recuperação de estado anterior.
- **B)** Incorreta. RAID pode tolerar certas falhas de disco, mas replica exclusão e cifração e não preserva necessariamente versões.
- **C)** Incorreta. Backup semanal não evita a interrupção inicial nem garante qualquer RTO; frequência também pode ser incompatível com o RPO.
- **D)** Incorreta. Replicação síncrona pode copiar imediatamente corrupção ou exclusão para o segundo nó.

**Conceito:** diferença e complementaridade entre backup, redundância e alta disponibilidade.

**Pegadinha:** usar uma tecnologia de continuidade como se ela também preservasse histórico recuperável.

**Como pensar:** disponibilidade presente pede componente alternativo; recuperação do passado pede cópia versionada e protegida.

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).


---

## Questões extras de revisão fixa do Dia 4

#### Extra Dia 4.1

Um gestor elimina uma etapa exigida por lei porque acredita que o procedimento ficará mais rápido e econômico. À luz dos princípios do art. 37, assinale a alternativa correta.

A) A eficiência prevalece sobre a legalidade sempre que houver economia de recursos.
B) A eficiência orienta a busca de qualidade e produtividade dentro da legalidade, sem autorizar o descumprimento de requisito legal.
C) A publicidade posterior convalida automaticamente a medida ilegal.
D) A legalidade confere ao agente público a mesma liberdade geral de atuação atribuída ao particular.

#### Extra Dia 4.2

Uma campanha oficial apresenta foto, nome e slogan pessoal de determinada autoridade, com destaque destinado a associar a ela uma obra pública. Considerando o art. 37, § 1º, da Constituição, assinale a alternativa correta.

A) A campanha é válida porque toda publicidade de obra pública admite promoção pessoal.
B) A identificação do órgão é proibida, ainda que necessária à orientação do cidadão.
C) A veracidade das informações impede qualquer violação à impessoalidade.
D) A publicidade institucional deve ter caráter educativo, informativo ou de orientação social e não pode caracterizar promoção pessoal de autoridade ou servidor.

#### Extra Dia 4.3

Sobre órgão, entidade e autarquia, assinale a alternativa correta.

A) Órgão é centro de competências sem personalidade própria; autarquia é entidade de direito público da Administração Indireta, criada diretamente por lei específica.
B) Órgão e entidade possuem necessariamente personalidade jurídica própria e patrimônio autônomo.
C) A criação de departamentos dentro de um ministério constitui descentralização para nova pessoa jurídica.
D) Autarquia é empresa privada autorizada por decreto e subordinada hierarquicamente a um ministério.

#### Extra Dia 4.4

Uma autoridade aplica sanção afirmando que houve inspeção em certa data, mas a inspeção jamais ocorreu. O vício central e a distinção correta são:

A) objeto; motivação é o fato que ocorreu no mundo e motivo é apenas sua redação.
B) finalidade; todo erro sobre fatos corresponde necessariamente a desvio de finalidade.
C) motivo; motivo é o suporte fático e jurídico do ato, enquanto motivação é a exposição desses fundamentos.
D) competência; fato inexistente transforma automaticamente a atribuição legal da autoridade.

#### Extra Dia 4.5

Quanto aos atributos do ato administrativo, assinale a alternativa correta.

A) A presunção de legitimidade é absoluta e impede controle administrativo ou judicial.
B) A presunção de legitimidade e veracidade é relativa; a autoexecutoriedade depende de hipótese admitida em lei ou de urgência reconhecida pelo ordenamento.
C) A imperatividade está presente em todo ato e exige concordância do destinatário.
D) A autoexecutoriedade permite executar qualquer decisão sem base jurídica e sem controle posterior.

#### Extra Dia 4.6

Assinale a alternativa correta sobre anulação, revogação, convalidação e decadência na Lei nº 9.784/1999.

A) Revogação corrige ilegalidade e pode ser determinada pelo Judiciário com base em conveniência administrativa.
B) Todo vício é convalidável, ainda que haja lesão ao interesse público ou prejuízo a terceiro.
C) O direito de anular ato favorável nunca sofre limite temporal, mesmo diante de boa-fé comprovada.
D) A Administração anula ato ilegal e pode revogar ato válido por mérito; defeito sanável pode ser convalidado sem lesão ou prejuízo, e o art. 54 prevê decadência de cinco anos para anular ato favorável, salvo má-fé.

#### Extra Dia 4.7

Sobre a relação entre LAI e LGPD no Poder Público, assinale a alternativa correta.

A) Transparência e proteção de dados devem ser compatibilizadas segundo finalidade, necessidade, interesse público e eventuais restrições legais, sem divulgação total ou sigilo total automáticos.
B) A presença de qualquer dado pessoal torna todo documento público sigiloso por cem anos.
C) A LAI elimina os princípios de finalidade e necessidade sempre que houver interesse jornalístico.
D) A LGPD proíbe o tratamento de dados pessoais pelo Poder Público para executar competência legal.

#### Extra Dia 4.8

Um agente pratica irregularidade administrativa, mas não há demonstração de dolo nem enquadramento em conduta tipificada na Lei de Improbidade. Assinale a alternativa correta.

A) Toda ilegalidade constitui automaticamente improbidade contra princípios.
B) A voluntariedade do ato substitui o dolo e a tipicidade exigidos pela lei.
C) Mera ilegalidade não basta: o enquadramento por improbidade exige conduta dolosa tipificada e os demais requisitos legais.
D) A ausência de dano ao erário exclui qualquer modalidade de improbidade, mesmo quando exista outro tipo doloso.

#### Extra Dia 4.9

À luz da Lei nº 14.133/2021 e da revisão fixa, assinale a alternativa correta.

A) Menor preço, maior desconto e técnica e preço são modalidades de licitação.
B) Pregão, concorrência, concurso, leilão e diálogo competitivo são modalidades; dispensa decorre de hipótese legal e inexigibilidade de competição inviável, sem afastar processo e motivação.
C) Dispensa e inexigibilidade são sinônimos e eliminam a instrução do processo de contratação.
D) Tomada de preços e convite integram o rol de modalidades da Lei nº 14.133/2021.

#### Extra Dia 4.10

Na responsabilidade civil objetiva prevista no art. 37, § 6º, da Constituição, assinale a alternativa correta.

A) A vítima deve provar necessariamente dolo do agente para obter reparação do Estado.
B) Responsabilidade objetiva significa indenização sem dano ou nexo causal.
C) O direito de regresso contra o agente também é objetivo e independe de dolo ou culpa.
D) Perante a vítima, exigem-se conduta estatal, dano e nexo causal, sem prova de culpa; o regresso contra o agente depende de dolo ou culpa.

#### Extra Dia 4.11

Considere as proposições P: “o firewall bloqueou a origem” e Q: “o IPS conteve o ataque”. A negação de “P e Q” é:

A) “não P ou não Q”.
B) “não P e não Q”.
C) “P ou Q”.
D) “P se, e somente se, Q”.

#### Extra Dia 4.12

Assinale a alternativa que apresenta corretamente a negação de uma condicional e de um quantificador universal.

A) A negação de “P implica Q” é “não P implica não Q”, e a de “todo servidor tem backup” é “nenhum servidor tem backup”.
B) A negação de “P implica Q” é “não P e Q”, e a de “todo” preserva o quantificador universal.
C) A negação de “P implica Q” é “P e não Q”, e a de “todo servidor tem backup” é “existe pelo menos um servidor que não tem backup”.
D) A negação de “P implica Q” é “P ou Q”, e a de “todo” é “algum”, sem negar o predicado.

#### Extra Dia 4.13

Em uma auditoria, 42 ativos possuem o controle A, 35 possuem o controle B e 17 possuem ambos. Quantos possuem pelo menos um dos dois controles?

A) 77.
B) 60.
C) 94.
D) 24.

#### Extra Dia 4.14

Após desconto de 20%, uma licença passou a custar R$ 240,00. Qual era o preço anterior ao desconto?

A) R$ 192,00.
B) R$ 260,00.
C) R$ 288,00.
D) R$ 300,00.

#### Extra Dia 4.15

Se 6 analistas, com a mesma produtividade, concluem uma revisão em 12 horas, em quanto tempo 9 analistas concluiriam o mesmo trabalho, mantidas as demais condições?

A) 8 horas.
B) 18 horas.
C) 6 horas.
D) 27 horas.

#### Extra Dia 4.16

Leia: “Embora o controle reduzisse o risco, ocorreu um incidente; portanto, o plano de resposta foi acionado.” Os conectores destacados exprimem, respectivamente:

A) causa e oposição.
B) condição e finalidade.
C) concessão e conclusão.
D) conclusão e concessão.

#### Extra Dia 4.17

Leia: “A equipe isolou apenas o servidor comprometido. Essa medida conteve o tráfego, mas não comprovou a erradicação da ameaça.” Assinale a alternativa correta.

A) “Essa medida” anuncia uma providência ainda não mencionada, em referência catafórica.
B) “Essa medida” retoma o isolamento do servidor, e o texto não autoriza concluir que a ameaça foi erradicada.
C) O trecho permite inferir que todos os servidores foram isolados e restaurados.
D) A contenção do tráfego comprova necessariamente a eliminação da causa do incidente.

#### Extra Dia 4.18

Assinale a alternativa redigida de acordo com a norma-padrão.

A) Haviam vulnerabilidades e devem haver controles adicionais.
B) Houveram dois incidentes e existe várias evidências.
C) Deve existirem alternativas e havia sido registradas falhas.
D) Deve haver controles adicionais, e existem registros suficientes para a análise.

#### Extra Dia 4.19

Assinale a alternativa com pontuação e emprego da crase adequados.

A) Após a contenção do incidente, a equipe dirigiu-se à sala de crise.
B) Os relatórios produzidos pela equipe, foram entregues à revisar.
C) O analista encaminhou, a evidência a autoridade responsável.
D) A equipe começou à restaurar o serviço, e o gestor à acompanhou.

#### Extra Dia 4.20

Original: “Como havia risco imediato, a equipe isolou o servidor.” Assinale a reescrita que preserva o sentido e a correção.

A) Embora não houvesse risco, a equipe isolou necessariamente todos os servidores.
B) A equipe isolou o servidor; contudo, havia risco imediato como consequência.
C) Havia risco imediato; por isso, a equipe isolou o servidor.
D) Se a equipe isolou o servidor, então não poderia haver risco imediato.

### Gabarito das questões extras do Dia 4

| Extra | Resposta |
|---:|:---:|
| 4.1 | B |
| 4.2 | D |
| 4.3 | A |
| 4.4 | C |
| 4.5 | B |
| 4.6 | D |
| 4.7 | A |
| 4.8 | C |
| 4.9 | B |
| 4.10 | D |
| 4.11 | A |
| 4.12 | C |
| 4.13 | B |
| 4.14 | D |
| 4.15 | A |
| 4.16 | C |
| 4.17 | B |
| 4.18 | D |
| 4.19 | A |
| 4.20 | C |

### Comentários das questões extras do Dia 4

#### Comentário Extra Dia 4.1

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Eficiência não possui superioridade abstrata sobre a legalidade.
- **B)** Correta. Qualidade e economia devem ser buscadas nos limites autorizados pelo ordenamento.
- **C)** Incorreta. Publicidade não corrige automaticamente vício de legalidade.
- **D)** Incorreta. O agente público atua conforme competência e autorização jurídica, não por liberdade geral.

**Conceito:** aplicação conjunta de legalidade e eficiência.

**Pegadinha:** invocar um princípio verdadeiro para afastar outro princípio obrigatório.

**Como pensar:** primeiro verifique se a atuação é juridicamente permitida; depois avalie sua eficiência.

**Referência:** [RF4-ADM-01 — Princípios do art. 37: LIMPE](semana_02_estudo.md#rf4-adm-01).

#### Comentário Extra Dia 4.2

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Obra real não autoriza usar publicidade institucional para prestígio pessoal.
- **B)** Incorreta. Identificação institucional necessária não se confunde com promoção do agente.
- **C)** Incorreta. Informação verdadeira ainda pode ser apresentada com caráter promocional.
- **D)** Correta. A alternativa reproduz finalidade e vedação do art. 37, § 1º.

**Conceito:** publicidade institucional e impessoalidade.

**Pegadinha:** confundir informação sobre ato público com propaganda pessoal da autoridade.

**Como pensar:** observe o foco da mensagem: orientar o cidadão ou exaltar determinada pessoa.

**Referência:** [RF4-ADM-02 — Publicidade institucional](semana_02_estudo.md#rf4-adm-02).

#### Comentário Extra Dia 4.3

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Órgão não possui personalidade própria; autarquia é pessoa jurídica de direito público criada por lei.
- **B)** Incorreta. A ausência de personalidade própria é característica usual do órgão.
- **C)** Incorreta. Departamentos na mesma pessoa jurídica representam desconcentração.
- **D)** Incorreta. Autarquia não é empresa privada e vinculação não equivale a subordinação hierárquica.

**Conceito:** órgão, entidade, autarquia e desconcentração.

**Pegadinha:** transformar distribuição interna de competências em criação de nova pessoa jurídica.

**Como pensar:** pergunte se surgiu personalidade jurídica nova; se não, há organização interna.

**Referência:** [RF4-ADM-03 — Órgão, entidade e autarquia](semana_02_estudo.md#rf4-adm-03).

#### Comentário Extra Dia 4.4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Objeto é o efeito jurídico; além disso, a opção inverte motivo e motivação.
- **B)** Incorreta. Fato inexistente atinge diretamente o suporte do ato, sem provar por si só desvio de finalidade.
- **C)** Correta. A inspeção inexistente torna defeituoso o motivo; motivação é a exteriorização dos fundamentos.
- **D)** Incorreta. A atribuição legal da autoridade não muda pelo erro sobre o fato.

**Conceito:** motivo e motivação do ato administrativo.

**Pegadinha:** trocar o fato/fundamento por sua explicação escrita.

**Como pensar:** pergunte se o problema está no que ocorreu ou em como as razões foram expostas.

**Referência:** [RF4-ADM-04 — Elementos do ato administrativo](semana_02_estudo.md#rf4-adm-04).

#### Comentário Extra Dia 4.5

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A presunção é relativa e admite prova em contrário.
- **B)** Correta. A alternativa apresenta os limites de ambos os atributos.
- **C)** Incorreta. Nem todo ato possui imperatividade, que independe da concordância quando presente.
- **D)** Incorreta. Autoexecutoriedade não elimina base legal nem controle.

**Conceito:** presunção e autoexecutoriedade.

**Pegadinha:** transformar atributos condicionados ou relativos em poderes absolutos.

**Como pensar:** desconfie de “todo”, “qualquer” e “impede controle”.

**Referência:** [RF4-ADM-05 — Atributos do ato administrativo](semana_02_estudo.md#rf4-adm-05).

#### Comentário Extra Dia 4.6

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Ilegalidade conduz à anulação; Judiciário não revoga ato alheio por mérito.
- **B)** Incorreta. Só defeito sanável pode ser convalidado, sem lesão ao interesse público nem prejuízo a terceiro.
- **C)** Incorreta. O art. 54 estabelece decadência quinquenal para ato favorável, ressalvada má-fé.
- **D)** Correta. A opção diferencia os institutos e inclui os limites legais.

**Conceito:** anulação, revogação, convalidação e decadência.

**Pegadinha:** usar revogação para ilegalidade ou tratar convalidação como cura universal.

**Como pensar:** ilegalidade → anulação; mérito de ato válido → revogação; vício sanável → possível convalidação.

**Referência:** [RF4-ADM-06 — Anulação, revogação, convalidação e art. 54](semana_02_estudo.md#rf4-adm-06).

#### Comentário Extra Dia 4.7

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. LAI e LGPD coexistem e exigem análise concreta de finalidade e necessidade.
- **B)** Incorreta. Dado pessoal no documento não produz sigilo integral automático.
- **C)** Incorreta. Acesso público não apaga finalidade, boa-fé e proteção necessária.
- **D)** Incorreta. A LGPD admite tratamento público para finalidade e competência legais.

**Conceito:** compatibilização entre transparência e proteção de dados.

**Pegadinha:** procurar uma lei que sempre anule a outra.

**Como pensar:** identifique interesse público, dado pessoal, finalidade, necessidade e eventual restrição.

**Referência:** [RF4-ADM-07 — LAI e LGPD](semana_02_estudo.md#rf4-adm-07).

#### Comentário Extra Dia 4.8

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Ilegalidade é categoria mais ampla e não configura automaticamente improbidade.
- **B)** Incorreta. A lei exige dolo e enquadramento típico; voluntariedade isolada não basta.
- **C)** Correta. A opção conserva dolo, tipicidade e demais requisitos legais.
- **D)** Incorreta. Há tipos de improbidade além de lesão ao erário.

**Conceito:** dolo e tipicidade na improbidade administrativa.

**Pegadinha:** usar “improbidade” como sinônimo de qualquer irregularidade.

**Como pensar:** procure simultaneamente conduta tipificada e dolo antes de concluir.

**Referência:** [RF4-ADM-08 — Improbidade administrativa](semana_02_estudo.md#rf4-adm-08).

#### Comentário Extra Dia 4.9

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Os itens citados são critérios de julgamento, não modalidades.
- **B)** Correta. A opção reúne as cinco modalidades atuais e distingue as contratações diretas sem eliminar processo.
- **C)** Incorreta. Dispensa e inexigibilidade possuem fundamentos diferentes e exigem instrução.
- **D)** Incorreta. Convite e tomada de preços não integram o rol da Lei nº 14.133/2021.

**Conceito:** modalidades, dispensa e inexigibilidade.

**Pegadinha:** confundir modalidade com critério ou contratação direta com ausência de processo.

**Como pensar:** competição inviável aponta para inexigibilidade; hipótese legal com competição viável em tese aponta, em regra, para dispensa.

**Referência:** [RF4-ADM-09 — Modalidades, dispensa e inexigibilidade](semana_02_estudo.md#rf4-adm-09).

#### Comentário Extra Dia 4.10

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A vítima não precisa provar culpa ou dolo estatal na responsabilidade objetiva.
- **B)** Incorreta. Objetividade não elimina dano e nexo causal.
- **C)** Incorreta. A ação regressiva exige dolo ou culpa do agente.
- **D)** Correta. A alternativa separa corretamente a relação Estado-vítima da relação regressiva.

**Conceito:** responsabilidade objetiva e direito de regresso.

**Pegadinha:** interpretar “objetiva” como indenização automática ou estendê-la ao regresso.

**Como pensar:** perante a vítima, retire apenas a prova de culpa; mantenha conduta, dano e nexo.

**Referência:** [RF4-ADM-10 — Responsabilidade civil do Estado](semana_02_estudo.md#rf4-adm-10).

#### Comentário Extra Dia 4.11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Pela lei de De Morgan, nega-se cada parcela e troca-se `e` por `ou`.
- **B)** Incorreta. Exige que ambas sejam falsas, condição mais forte que a negação da conjunção.
- **C)** Incorreta. Mantém as proposições positivas e não nega a conjunção.
- **D)** Incorreta. Bicondicional expressa equivalência, não a negação pedida.

**Conceito:** negação da conjunção.

**Pegadinha:** negar cada parcela sem trocar o conectivo.

**Como pensar:** `não (P e Q)` transforma-se em `não P ou não Q`.

**Referência:** [RF4-RLM-01 — Negação de conjunção e disjunção](semana_02_estudo.md#rf4-rlm-01).

#### Comentário Extra Dia 4.12

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contrapositiva não é negação, e negar “todo” não produz “nenhum”.
- **B)** Incorreta. A condicional só é falsa com antecedente verdadeiro e consequente falso.
- **C)** Correta. A opção apresenta `P e não Q` e o contraexemplo existencial.
- **D)** Incorreta. Falta negar o predicado e a disjunção não é a negação da condicional.

**Conceito:** negação da condicional e do quantificador universal.

**Pegadinha:** confundir negação com contrapositiva ou trocar “todo” por “nenhum”.

**Como pensar:** para negar universal, encontre ao menos um caso que falhe.

**Referência:** [RF4-RLM-02 — Condicional e quantificadores](semana_02_estudo.md#rf4-rlm-02).

#### Comentário Extra Dia 4.13

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Somar 42 e 35 conta os 17 ativos da interseção duas vezes.
- **B)** Correta. Inclusão-exclusão: `42 + 35 - 17 = 60`.
- **C)** Incorreta. Somar novamente a interseção aumenta a duplicidade.
- **D)** Incorreta. Esse valor não corresponde à união dos conjuntos.

**Conceito:** princípio da inclusão-exclusão.

**Pegadinha:** esquecer de descontar a dupla contagem.

**Como pensar:** união de dois conjuntos = primeiro + segundo − ambos.

**Referência:** [RF4-RLM-03 — Princípio da inclusão-exclusão](semana_02_estudo.md#rf4-rlm-03).

#### Comentário Extra Dia 4.14

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Multiplica novamente por 0,8 em vez de recuperar o valor original.
- **B)** Incorreta. Somar 20 ao preço final não representa percentual sobre o original.
- **C)** Incorreta. Aplicar 20% de acréscimo a 240 não desfaz desconto de 20% sobre outra base.
- **D)** Correta. Se 240 corresponde a 80%, então `240 ÷ 0,8 = 300`.

**Conceito:** porcentagem reversa.

**Pegadinha:** somar ao valor final o mesmo percentual que foi retirado do original.

**Como pensar:** identifique o fator restante e divida por ele.

**Referência:** [RF4-RLM-04 — Porcentagem reversa](semana_02_estudo.md#rf4-rlm-04).

#### Comentário Extra Dia 4.15

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A quantidade de trabalho é `6 × 12 = 72` analista-horas; `72 ÷ 9 = 8` horas.
- **B)** Incorreta. Aumentar equipe não aumenta tempo quando produtividade e trabalho são constantes.
- **C)** Incorreta. Esse resultado não preserva o produto analistas × horas.
- **D)** Incorreta. Multiplica grandezas que, no cenário, são inversamente proporcionais.

**Conceito:** proporção inversa e produtividade.

**Pegadinha:** tratar número de trabalhadores e tempo como grandezas diretamente proporcionais.

**Como pensar:** mantenha constante o total de analista-horas.

**Referência:** [RF4-RLM-05 — Proporção e produtividade](semana_02_estudo.md#rf4-rlm-05).

#### Comentário Extra Dia 4.16

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. `Embora` não introduz causa, e `portanto` não marca oposição.
- **B)** Incorreta. Os conectores não exprimem condição nem finalidade.
- **C)** Correta. `Embora` introduz concessão; `portanto`, conclusão.
- **D)** Incorreta. A alternativa inverte os valores semânticos.

**Conceito:** relações de sentido dos conectores.

**Pegadinha:** chamar toda quebra de expectativa de oposição simples, ignorando a concessão.

**Como pensar:** concessão admite um fato que não impede o resultado; conclusão apresenta consequência lógica.

**Referência:** [RF4-PT-01 — Conectores](semana_02_estudo.md#rf4-pt-01).

#### Comentário Extra Dia 4.17

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A expressão retoma conteúdo anterior, portanto é anafórica.
- **B)** Correta. O referente é o isolamento, e o texto separa contenção de erradicação.
- **C)** Incorreta. `Apenas` restringe a medida ao servidor comprometido e não há restauração mencionada.
- **D)** Incorreta. Conter tráfego não prova eliminar a ameaça.

**Conceito:** referência anafórica e inferência autorizada.

**Pegadinha:** ignorar palavra restritiva ou acrescentar resultado não declarado.

**Como pensar:** substitua `essa medida` pelo antecedente e respeite a ressalva introduzida por `mas`.

**Referência:** [RF4-PT-02 — Inferência e referência](semana_02_estudo.md#rf4-pt-02).

#### Comentário Extra Dia 4.18

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. `Haver` existencial é impessoal: `havia` e `deve haver`.
- **B)** Incorreta. O correto seria `houve dois incidentes` e `existem várias evidências`.
- **C)** Incorreta. Com `existir`, a locução concorda: `devem existir`; a segunda concordância também está inadequada.
- **D)** Correta. `Deve haver` permanece no singular, enquanto `existem` concorda com `registros`.

**Conceito:** concordância de `haver` e `existir`.

**Pegadinha:** tratar o complemento de `haver` como sujeito.

**Como pensar:** `haver` existencial fica no singular; `existir` procura sujeito e concorda.

**Referência:** [RF4-PT-03 — Haver existencial e existir](semana_02_estudo.md#rf4-pt-03).

#### Comentário Extra Dia 4.19

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A vírgula separa o adjunto deslocado, e `dirigir-se a` + `a sala` produz crase.
- **B)** Incorreta. A vírgula separa sujeito e verbo, e não há crase antes de `revisar`.
- **C)** Incorreta. A vírgula separa verbo e complemento; diante de `autoridade`, caberia `à autoridade` no contexto.
- **D)** Incorreta. Não há crase antes de verbo nem antes de pronome pessoal oblíquo.

**Conceito:** pontuação e crase.

**Pegadinha:** usar vírgula como pausa livre e acento grave diante de qualquer palavra feminina ou verbo.

**Como pensar:** preserve sujeito-verbo-complemento e confirme simultaneamente preposição e artigo.

**Referência:** [RF4-PT-04 — Pontuação e crase](semana_02_estudo.md#rf4-pt-04).

#### Comentário Extra Dia 4.20

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Altera causa para concessão, nega o risco e amplia um servidor para todos.
- **B)** Incorreta. `Contudo` cria oposição e inverte a relação causal original.
- **C)** Correta. `Por isso` apresenta a consequência da causa expressa na primeira oração.
- **D)** Incorreta. Cria uma condicional e uma negação de risco inexistentes no original.

**Conceito:** reescrita com preservação de causa e consequência.

**Pegadinha:** manter vocabulário semelhante, mas trocar conector, alcance ou polaridade.

**Como pensar:** compare agente, ação, causa, consequência e grau de certeza.

**Referência:** [RF4-PT-05 — Reescrita e clareza](semana_02_estudo.md#rf4-pt-05).



---

# Dia 5 — Sistemas Operacionais Avançados

## Questões principais


### Questão 1

Em um computador com um único núcleo, o sistema operacional alterna a execução das tarefas A e B ao longo de certo intervalo, de modo que ambas avançam, embora apenas uma execute a cada instante. Nesse caso, ocorre

A) paralelismo sem concorrência, pois as tarefas não compartilham o mesmo instante de CPU.
B) concorrência sem paralelismo, pois há progresso intercalado, mas não execução simultânea.
C) paralelismo e concorrência, pois toda alternância de contexto equivale à simultaneidade.
D) ausência de concorrência, pois ela exige pelo menos dois núcleos físicos.

### Questão 2

Sobre programa, processo e thread, assinale a afirmativa correta.

A) Programa é uma instância ativa que já possui, necessariamente, contador de programa e pilha de execução.
B) Threads distintas de um mesmo processo possuem espaços de endereçamento totalmente isolados entre si.
C) Processo é apenas o arquivo executável armazenado, sem estado ou recursos associados à execução.
D) Threads do mesmo processo normalmente compartilham código, dados e recursos abertos, mas mantêm pilhas e registradores próprios.

### Questão 3

Uma thread solicitou a leitura de um bloco em disco e aguarda a conclusão da operação. Enquanto o evento não ocorre, ela se encontra conceitualmente no estado

A) bloqueado, e elevar sua prioridade não substitui a conclusão da E/S aguardada.
B) pronto, pois toda thread que não está usando a CPU disputa imediatamente o processador.
C) executando, pois a operação de disco foi iniciada em seu nome.
D) terminado, pois deixou de executar instruções no processador.

### Questão 4

Em um sistema que usa Round Robin, a equipe reduz bastante o quantum, mantendo inalteradas as demais condições. Um efeito plausível dessa decisão é

A) eliminar as trocas de contexto, já que cada tarefa permanecerá menos tempo na CPU.
B) transformar o algoritmo em FCFS, pois os processos passarão a executar até o fim.
C) melhorar a responsividade em alguns cenários, ao custo de mais trocas de contexto e maior sobrecarga.
D) fazer com que threads bloqueadas por E/S se tornem prontas a cada expiração do quantum.

### Questão 5

Duas threads executam, sem sincronização, a operação lógica `contador = contador + 1` sobre um contador inicialmente igual a 40. Ambas leem 40 antes de qualquer gravação e, depois, cada uma grava 41. O resultado observado caracteriza

A) deadlock, pois nenhuma thread concluiu sua operação.
B) starvation, pois uma das threads foi definitivamente impedida de usar a CPU.
C) livelock, pois as threads desfizeram repetidamente o trabalho uma da outra.
D) condição de corrida com atualização perdida, causada pela intercalação de leitura, cálculo e escrita.

### Questão 6

Quanto à atomicidade em programas concorrentes, assinale a afirmativa correta.

A) Se cada instrução de máquina for atômica, qualquer sequência formada por elas também será atômica.
B) A atomicidade de uma operação isolada não torna atômica uma sequência; visibilidade e ordenação também podem afetar a correção.
C) Uma atribuição escrita em uma única linha de linguagem de alto nível é necessariamente indivisível para todas as threads.
D) Atomicidade e exclusão mútua garantem, por si sós, que toda gravação seja imediatamente visível em qualquer arquitetura.

### Questão 7

Um mutex protege o saldo de uma conta compartilhada. Para que o protocolo de exclusão seja efetivo, é correto afirmar que

A) todos os participantes que acessam o saldo devem respeitar o mesmo protocolo de aquisição e liberação do mutex.
B) basta uma das threads usar o mutex, pois o sistema operacional bloqueará automaticamente acessos não cooperantes.
C) o mutex torna atômicas todas as operações do processo, inclusive as que não usam esse mecanismo.
D) a thread que adquiriu o mutex pode delegar livremente sua liberação a qualquer fluxo, pois mutex não expressa propriedade.

### Questão 8

Um servidor dispõe de oito conexões equivalentes em um pool e deve permitir, no máximo, oito usuários simultâneos desse recurso. O mecanismo mais diretamente adequado é

A) uma variável de condição sem estado e sem qualquer predicado associado.
B) um spinlock mantido durante toda a utilização externa de cada conexão.
C) um semáforo contador inicializado com oito unidades, decrementado na aquisição e incrementado na devolução.
D) um mutex único que permita a oito threads serem proprietárias simultaneamente.

### Questão 9

Uma consumidora retira itens de uma fila protegida por mutex e aguarda quando a fila está vazia. No padrão correto com variável de condição, a consumidora deve

A) manter o mutex enquanto dorme, impedindo que o produtor altere a fila até o despertar.
B) testar a fila uma única vez com `if`, pois notificações eliminam despertares espúrios e disputas após o despertar.
C) liberar o mutex, aguardar e continuar sem readquiri-lo, para evitar qualquer contenção.
D) verificar o predicado em laço; a espera libera atomicamente o mutex e o readquire antes de retornar.

### Questão 10

Sobre spinlocks, assinale a alternativa correta.

A) São indicados para esperas longas por E/S, pois a espera ativa economiza ciclos de CPU.
B) Podem ser úteis em trechos muito curtos, especialmente em multiprocessadores, mas desperdiçam CPU quando a espera se prolonga.
C) Colocam obrigatoriamente a thread para dormir até que o recurso seja liberado.
D) São sempre a melhor escolha em um único núcleo não preemptível, mesmo se o detentor do lock ainda precisar executar.

### Questão 11

Dois processos locais precisam trocar grande volume de dados com baixa sobrecarga de cópia. A equipe escolhe memória compartilhada. Essa escolha

A) pode favorecer o desempenho, mas exige um protocolo adicional de sincronização e visibilidade para acessos concorrentes.
B) elimina condições de corrida, pois o sistema serializa automaticamente toda leitura e gravação na área comum.
C) preserva unidades de mensagem e ordenação por prioridade de forma inerente, como uma fila de mensagens.
D) impede que os processos alterem a mesma região, preservando o isolamento integral entre eles.

### Questão 12

Considere mecanismos de comunicação entre processos. Assinale a associação correta.

A) Sinal — transporte de grandes blocos estruturados; socket — restrito a processos com relação de parentesco.
B) Pipe anônimo — necessariamente acessível por nome global; memória compartilhada — dispensa sincronização.
C) Fila de mensagens — preserva unidades de mensagem; socket — pode atender comunicação local ou em rede.
D) FIFO — exige que os processos sejam pai e filho; RPC — elimina falhas de transporte e serialização.

### Questão 13

Um deadlock ocorre quando

A) uma thread pronta perde a CPU uma única vez para outra de prioridade superior.
B) processos executam em paralelo e disputam uma variável, ainda que todos concluam normalmente.
C) um processo aguarda E/S externa que, embora lenta, continua avançando.
D) um conjunto permanece bloqueado porque cada integrante espera recurso ou evento que outro integrante do conjunto deve produzir ou liberar.

### Questão 14

No modelo clássico de Coffman para recursos reutilizáveis, as condições que devem coexistir para possibilitar deadlock são

A) paralelismo, preempção, memória compartilhada e escalonamento por prioridade.
B) exclusão mútua, posse e espera, não preempção e espera circular.
C) seção crítica, semáforo contador, inversão de prioridade e ausência de quantum.
D) espera ativa, comunicação síncrona, múltiplos núcleos e fila de mensagens.

### Questão 15

Uma aplicação impõe a regra de que todos os fluxos devem adquirir os locks `L1`, `L2` e `L3` sempre nessa ordem crescente, inclusive nos caminhos de erro. Essa é uma técnica de prevenção que atua diretamente contra a condição de

A) espera circular.
B) exclusão mútua.
C) não preempção.
D) posse e espera.

### Questão 16

Um sistema exige que cada processo solicite, antes de iniciar, todos os recursos de que precisará; se o conjunto completo não estiver disponível, nenhum deles é concedido. A estratégia previne o deadlock principalmente por romper

A) a exclusão mútua, pois todos os recursos passam a ser compartilháveis.
B) a não preempção, pois o sistema retira recursos já concedidos a qualquer momento.
C) a posse e espera, embora possa reduzir a utilização dos recursos.
D) a espera circular, sem produzir qualquer impacto sobre a eficiência.

### Questão 17

Na evitação de deadlock, um estado é considerado seguro quando

A) não há recurso alocado naquele instante, ainda que nenhuma demanda futura seja conhecida.
B) todos os processos conseguem concluir simultaneamente, sem precisar aguardar liberações.
C) não existe exclusão mútua para nenhum dos recursos utilizados pelo sistema.
D) existe ao menos uma sequência de conclusão que permite atender todos os participantes; estado inseguro não significa deadlock já ocorrido.

### Questão 18

O algoritmo do banqueiro é um exemplo clássico de evitação de deadlock. Para decidir se uma concessão preserva um estado seguro, ele pressupõe, entre outros dados,

A) apenas a prioridade atual de cada processo, sem informações sobre recursos.
B) as demandas máximas declaradas, as alocações correntes e os recursos disponíveis.
C) somente um grafo de espera com exatamente uma instância de cada recurso.
D) a interrupção compulsória de qualquer processo sempre que houver uma nova solicitação.

### Questão 19

Na detecção de deadlock por grafos e matrizes, é correto afirmar que

A) com uma instância de cada tipo de recurso, ciclo no grafo de espera caracteriza deadlock; com várias instâncias, o ciclo isolado pode não ser suficiente.
B) com várias instâncias, qualquer ciclo prova deadlock, sem necessidade de considerar recursos disponíveis e alocados.
C) a ausência de ciclo prova deadlock quando existe apenas uma instância de cada recurso.
D) ciclos são irrelevantes; basta haver ao menos um processo no estado bloqueado.

### Questão 20

Após detectar um deadlock em operações transacionais, o sistema precisa recuperar o progresso preservando a consistência. Uma ação tecnicamente adequada é

A) encerrar aleatoriamente todos os participantes, sem avaliar dados ou trabalho já realizado.
B) ignorar o ciclo, pois a detecção já rompe automaticamente uma das condições de Coffman.
C) escolher vítima por critérios de custo e, quando suportado, abortar ou restaurar um checkpoint consistente.
D) aumentar a prioridade de todos os processos, o que libera compulsoriamente os recursos mantidos.

### Questão 21

Em um escalonador de prioridade estrita, tarefas de baixa prioridade permanecem prontas, mas são continuamente ultrapassadas por novas tarefas de alta prioridade. O problema e uma mitigação compatível são, respectivamente,

A) deadlock e imposição de ordem global de locks.
B) livelock e redução do número de núcleos.
C) condição de corrida e uso de memória compartilhada.
D) starvation e aging gradual da prioridade de quem espera.

### Questão 22

Duas threads detectam conflito, liberam seus recursos, tentam novamente ao mesmo tempo e repetem indefinidamente esse comportamento. Elas continuam ativas, mas não concluem trabalho útil. Trata-se de

A) starvation, necessariamente causada por uma fila de prioridade estrita.
B) livelock, que pode ser mitigado por backoff aleatório para romper a simetria.
C) deadlock, pois ambas permanecem bloqueadas sem mudar de estado.
D) paralelismo, que se resolve substituindo threads por programas passivos.

### Questão 23

Uma thread de alta prioridade aguarda um mutex mantido por uma thread de baixa prioridade. Threads de prioridade intermediária preemptam repetidamente a detentora, retardando a liberação do mutex. O cenário descreve

A) inversão de prioridade, mitigável por herança temporária da prioridade pela detentora do mutex.
B) starvation da thread de baixa prioridade, resolvida necessariamente por aumentar o quantum de todas as threads.
C) deadlock clássico, pois as quatro condições de Coffman estão demonstradas no enunciado.
D) livelock, pois a thread de alta prioridade permanece executando e alterando o mutex.

### Questão 24

Analise as situações.

I. T1 mantém A e espera B, enquanto T2 mantém B e espera A.
II. Um fluxo pronto nunca é escolhido, embora outros concluam normalmente.
III. Dois fluxos reagem um ao outro continuamente, mas não avançam.

As situações I, II e III correspondem, respectivamente, a

A) starvation, deadlock e condição de corrida.
B) livelock, inversão de prioridade e deadlock.
C) deadlock, starvation e livelock.
D) condição de corrida, livelock e starvation.

### Questão 25

Uma thread adquire um mutex, inicia uma operação de rede potencialmente longa e mantém o lock até receber a resposta. À luz das boas práticas de sincronização, essa decisão

A) é obrigatória, pois toda E/S deve ocorrer dentro de uma seção crítica, mesmo que não acesse o estado protegido.
B) elimina contenção, já que a thread bloqueada deixa de ser proprietária do mutex automaticamente.
C) transforma o mutex em semáforo contador e permite que outros participantes entrem na seção protegida.
D) pode ampliar a contenção e participar de ciclos de dependência; convém proteger apenas o menor estado coerente necessário.



### Questão 26

Considere três processos submetidos ao escalonamento FCFS, sem custo de troca de contexto:

| Processo | Chegada | Burst de CPU |
|---|---:|---:|
| P1 | 0 | 6 |
| P2 | 1 | 2 |
| P3 | 2 | 1 |

Assinale a alternativa que apresenta, respectivamente, o tempo médio de espera e o tempo médio de retorno.

A) 3 e 6 unidades de tempo.
B) 11/3 e 20/3 unidades de tempo.
C) 13/3 e 7 unidades de tempo.
D) 5 e 20/3 unidades de tempo.

### Questão 27

Três processos A, B e C chegam no instante zero com bursts de CPU iguais a 7, 4 e 1, respectivamente. Aplicando SJF não preemptivo, sem custo de troca, é correto afirmar que:

A) a ordem será A, B, C, pois SJF preserva a ordem de chegada quando todos chegam juntos.
B) a ordem será C, A, B, e a espera média será 8/3 unidades.
C) a ordem será B, C, A, e a espera média será 3 unidades.
D) a ordem será C, B, A, e a espera média será 2 unidades.

### Questão 28

Considere o escalonamento SRTF dos processos abaixo, sem custo de troca de contexto:

| Processo | Chegada | Burst de CPU |
|---|---:|---:|
| A | 0 | 8 |
| B | 1 | 4 |
| C | 2 | 2 |

Qual alternativa descreve corretamente a execução e os tempos de espera?

A) A executa de 0 a 1; B, de 1 a 2; C, de 2 a 4; B, de 4 a 7; e A, de 7 a 14. As esperas de A, B e C são 6, 2 e 0.
B) A executa até terminar, pois SRTF não permite preempção; as esperas são 0, 7 e 10.
C) A executa de 0 a 1; B, de 1 a 5; C, de 5 a 7; e A, de 7 a 14. As esperas são 6, 0 e 3.
D) C executa primeiro no instante zero, porque possui o menor burst, ainda que só chegue no instante 2.

### Questão 29

Em um escalonador por prioridade, tarefas de alta prioridade chegam continuamente e uma tarefa pronta de baixa prioridade permanece sem CPU por tempo indefinido. A medida diretamente voltada a esse problema é:

A) aumentar indefinidamente o quantum apenas das tarefas de alta prioridade.
B) substituir toda interrupção de hardware por polling.
C) aplicar aging, elevando gradualmente a prioridade da tarefa conforme seu tempo de espera.
D) impor que a tarefa de baixa prioridade aguarde bloqueada por E/S.

### Questão 30

Três processos chegam no instante zero, na ordem A, B e C, com bursts 5, 3 e 1. Em Round Robin com quantum 2 e custo de troca desprezado, assinale a alternativa correta.

A) A, B e C terminam nos instantes 5, 8 e 9, pois o quantum não altera a ordem de conclusão do FCFS.
B) C, B e A terminam nos instantes 5, 8 e 9; os tempos de resposta de A, B e C são 0, 2 e 4.
C) B, C e A terminam nos instantes 6, 7 e 9; o quantum não utilizado por C é transferido a A.
D) C, A e B terminam nos instantes 1, 6 e 9, pois o menor burst sempre recebe a CPU primeiro.

### Questão 31

Sobre o tamanho do quantum no Round Robin, assinale a afirmativa correta.

A) Quantum muito pequeno tende a elevar preempções e trocas de contexto; quantum muito grande aproxima o comportamento de FCFS.
B) Quantum muito pequeno elimina o custo de troca de contexto e transforma o algoritmo em SJF.
C) Quantum muito grande melhora necessariamente o primeiro atendimento de todas as tarefas interativas.
D) O tamanho do quantum não afeta tempo de resposta nem sobrecarga, apenas a prioridade estática.

### Questão 32

Quanto à preempção nos algoritmos clássicos de escalonamento, assinale a alternativa correta.

A) FCFS e SRTF são necessariamente não preemptivos.
B) SJF e Round Robin somente preemptam quando chega uma tarefa de prioridade superior.
C) Prioridade é necessariamente não preemptiva, enquanto FCFS é necessariamente preemptivo.
D) FCFS e SJF clássicos são não preemptivos; SRTF é preemptivo; prioridade pode ser preemptiva ou não; Round Robin preempta ao fim do quantum.

### Questão 33

Em uma operação de entrada/saída, qual descrição distingue corretamente controlador e driver?

A) O driver é o circuito físico do dispositivo, e o controlador é um programa executado no espaço da aplicação.
B) O aplicativo precisa conhecer os registradores elétricos de cada dispositivo, pois o driver apenas define permissões de arquivo.
C) O controlador contém lógica e registradores do dispositivo; o driver traduz operações do sistema operacional, administra filas, buffers, erros e conclusão.
D) Driver e controlador são nomes equivalentes para o mecanismo que escalona processos na CPU.

### Questão 34

Sobre polling na entrada/saída, assinale a alternativa correta.

A) Consiste em consultar repetidamente o estado do dispositivo; pode ser adequado para espera curtíssima ou evento muito frequente, mas desperdiça ciclos em espera longa.
B) É uma notificação iniciada exclusivamente pelo dispositivo e, por isso, não consome ciclos de consulta.
C) Transfere blocos entre dispositivo e memória sem configuração pela CPU.
D) É sempre sinônimo de E/S síncrona e nunca pode coexistir com interrupções no mesmo driver.

### Questão 35

Um dispositivo gera uma interrupção ao concluir uma operação. Segundo o tratamento adequado, a rotina de serviço de interrupção deve, em regra:

A) executar todo o processamento demorado antes de devolver a CPU, ainda que bloqueie outras interrupções.
B) reiniciar o sistema para garantir que os registradores do dispositivo estejam consistentes.
C) copiar obrigatoriamente cada byte para a memória sem participação de controlador ou DMA.
D) reconhecer o dispositivo, salvar o mínimo necessário e diferir o trabalho demorado para contexto apropriado, retornando rapidamente.

### Questão 36

Uma controladora recebeu da CPU a origem, o destino, o tamanho e a direção de uma cópia de 8 MiB. Em seguida, transferiu o bloco do dispositivo para a memória e sinalizou a conclusão. O mecanismo predominante de transferência foi:

A) polling, porque a CPU precisou fornecer parâmetros antes da cópia.
B) DMA, que reduz a participação da CPU em cada unidade transferida, sem eliminar configuração e tratamento de término.
C) journaling, porque houve registro prévio de origem e destino.
D) Round Robin, porque o bloco foi dividido entre dispositivo e memória.

### Questão 37

Polling, interrupção e DMA são empregados em operações de E/S. Assinale a alternativa correta.

A) A presença de interrupção prova que DMA não participou da operação.
B) Um driver que usa DMA fica impedido de consultar o dispositivo por polling em qualquer fase.
C) O driver pode configurar DMA para transferir dados e receber uma interrupção de conclusão; os mecanismos não são mutuamente exclusivos.
D) DMA e interrupção têm a mesma função: ambos transferem todos os dados para a memória.

### Questão 38

Sobre abstrações de sistemas de arquivos, assinale a afirmativa correta.

A) O diretório relaciona nomes a objetos; inode ou registro equivalente guarda metadados e referência ao conteúdo; descritor ou handle é uma referência aberta pertencente a um processo.
B) O inode é apenas o texto que forma o nome do arquivo e deixa de existir quando o arquivo é aberto.
C) Montagem significa copiar integralmente todos os arquivos para o diretório escolhido.
D) Um descritor aberto pertence necessariamente a todos os processos do sistema e independe de controle de acesso.

### Questão 39

Após uma queda de energia, o journal de um sistema de arquivos contém uma transação sem registro de commit válido. No replay, a conduta compatível com a teoria de journaling é:

A) considerar a transação confirmada apenas porque seus descritores foram gravados.
B) tratá-la como incompleta e descartá-la, enquanto transações confirmadas podem ser reproduzidas.
C) restaurar automaticamente uma cópia histórica de todos os arquivos alterados.
D) converter a transação em backup completo antes de montar o sistema de arquivos.

### Questão 40

Acerca dos modos de journaling do ext4 apresentados na teoria, assinale a alternativa correta.

A) No modo data=ordered, todos os dados e metadados passam obrigatoriamente pelo journal antes de chegar ao destino final.
B) No modo data=journal, somente os metadados entram no journal, e os dados podem ser gravados depois sem ordenação.
C) O modo data=writeback oferece ordenação mais forte que data=journal e equivale a backup.
D) No padrão data=ordered, metadados são registrados no journal e os blocos de dados associados vão ao sistema principal antes do commit dos metadados; data=journal registra dados e metadados, com maior custo de escrita.

### Questão 41

Uma pessoa excluiu de forma autorizada um relatório e, dias depois, percebeu que precisava da versão anterior. O volume usa journaling e permaneceu estruturalmente consistente. É correto concluir que:

A) o journal necessariamente mantém todas as versões anteriores e dispensa retenção de backup.
B) a consistência estrutural prova que o arquivo excluído continua recuperável no mesmo volume.
C) journaling auxilia a recuperação de consistência após falhas, mas não substitui backup nem garante versão histórica após exclusão, ransomware ou perda da mídia.
D) todo sistema com journal replica automaticamente os dados em uma mídia independente.

### Questão 42

Em um arquivo regular Linux, o modo 750 concede:

A) leitura, gravação e execução ao proprietário; leitura e execução ao grupo; nenhuma permissão aos outros.
B) leitura e gravação ao proprietário; somente execução ao grupo; leitura aos outros.
C) controle total ao grupo e somente leitura ao proprietário.
D) leitura, gravação e execução a todos, porque os três algarismos devem ser somados.

### Questão 43

No modelo clássico de permissões Linux, os bits aplicados a diretórios possuem efeitos próprios. Assinale a alternativa correta.

A) Leitura em diretório autoriza executar qualquer arquivo nele, independentemente das permissões do arquivo.
B) Escrita em diretório altera automaticamente o conteúdo de todos os arquivos existentes.
C) Execução em diretório significa iniciar o diretório como se fosse um programa.
D) Leitura permite listar nomes, enquanto execução permite atravessar ou pesquisar componentes do caminho; criar ou remover entradas depende de escrita combinada com acesso adequado.

### Questão 44

Um administrador Linux precisa, respectivamente, alterar os bits de modo, trocar o proprietário e inspecionar uma ACL estendida. Quais comandos correspondem a essas finalidades?

A) ps, top e journalctl.
B) chmod, chown e getfacl.
C) ip, ss e systemctl.
D) df, findmnt e free.

### Questão 45

Sobre permissões no Windows, assinale a afirmativa correta.

A) A DACL armazena somente o nome do proprietário e não contém entradas de permissão ou negação.
B) Uma ACE herdada nunca participa da permissão efetiva de um objeto filho.
C) A DACL contém ACEs, inclusive permissões ou negações e possíveis regras herdadas; no acesso remoto, compartilhamento e NTFS podem atuar em conjunto.
D) A permissão efetiva no acesso remoto é sempre a mais alta encontrada entre compartilhamento e NTFS.

### Questão 46

No Windows, o comando icacls é utilizado para:

A) listar processos e suas threads, substituindo Get-Process.
B) exibir ou modificar DACLs de arquivos e diretórios; ele substitui o antigo cacls, hoje depreciado.
C) acompanhar continuamente consumo de CPU como o top.
D) consultar rotas e endereços IP, substituindo ipconfig.

### Questão 47

Uma equipe deseja primeiro obter uma fotografia dos processos e threads Linux e depois acompanhar continuamente o consumo de recursos. A associação adequada é:

A) ps -eLf para a visão pontual de processos e threads, e top para atualização contínua.
B) top para alterar DACLs, e ps -eLf para reiniciar serviços.
C) journalctl para enumerar threads, e chmod para medir consumo de CPU.
D) ip route para listar processos, e ss -tulpn para escaloná-los.

### Questão 48

Para verificar o estado de um serviço e consultar eventos de log relacionados, sem confundir observação com encerramento de processos, a associação correta é:

A) Linux: chmod e chown; Windows: icacls e Get-Acl.
B) Linux: ip addr e ss; Windows: Get-Process e Stop-Process.
C) Linux: kill -KILL e top; Windows: taskkill e Get-Service.
D) Linux: systemctl status NOME e journalctl; Windows: Get-Service e Get-WinEvent.

### Questão 49

Durante um diagnóstico Linux, é necessário verificar endereços e rotas e, em seguida, observar sockets de escuta associados a processos. A sequência mais pertinente é:

A) chmod, chown e getfacl.
B) ps, kill e free.
C) ip addr/ip route e ss -tulpn.
D) systemctl, journalctl e findmnt.

### Questão 50

Em uma estação Windows, o analista precisa, nessa ordem, listar processos, consultar serviços, inspecionar a configuração IP, examinar conexões de rede e verificar permissões NTFS. Qual conjunto associa corretamente as finalidades?

A) Get-Service; Get-Process; icacls; taskkill; journalctl.
B) Get-Process; Get-Service; ipconfig; Get-NetTCPConnection; icacls.
C) top; systemctl; ip addr; ss; chmod.
D) Stop-Process; sc delete; route delete; taskkill; cacls.



## Gabarito do Dia 5

### Questões principais 1–25


| Questão | Resposta |
|---:|:---:|
| 1 | B |
| 2 | D |
| 3 | A |
| 4 | C |
| 5 | D |
| 6 | B |
| 7 | A |
| 8 | C |
| 9 | D |
| 10 | B |
| 11 | A |
| 12 | C |
| 13 | D |
| 14 | B |
| 15 | A |
| 16 | C |
| 17 | D |
| 18 | B |
| 19 | A |
| 20 | C |
| 21 | D |
| 22 | B |
| 23 | A |
| 24 | C |
| 25 | D |



### Questões principais 26–50


| Questão | Gabarito |
|---:|:---:|
| 26 | B |
| 27 | D |
| 28 | A |
| 29 | C |
| 30 | B |
| 31 | A |
| 32 | D |
| 33 | C |
| 34 | A |
| 35 | D |
| 36 | B |
| 37 | C |
| 38 | A |
| 39 | B |
| 40 | D |
| 41 | C |
| 42 | A |
| 43 | D |
| 44 | B |
| 45 | C |
| 46 | B |
| 47 | A |
| 48 | D |
| 49 | C |
| 50 | B |



## Comentários do Dia 5


### Comentário da Questão 1

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Paralelismo exige execução simultânea; a alternância em um único núcleo não a produz.
- **B)** Correta. As duas tarefas progridem no mesmo intervalo por intercalação, embora só uma ocupe o núcleo em cada instante.
- **C)** Incorreta. Troca de contexto permite concorrência, mas não equivale a simultaneidade.
- **D)** Incorreta. Concorrência pode existir com um único núcleo; múltiplos núcleos são relevantes para paralelismo efetivo.

**Conceito:** concorrência é organização temporal com possíveis intercalações; paralelismo é execução simultânea.

**Pegadinha:** usar os dois termos como sinônimos ou exigir dois núcleos para qualquer concorrência.

**Como pensar:** pergunte primeiro se as tarefas avançam no mesmo intervalo e, depois, se executam no mesmo instante.

**Referência:** [Concorrência e paralelismo](semana_02_estudo.md#s2-d5-concorrencia-paralelismo).

### Comentário da Questão 2

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Programa é o conjunto passivo de instruções; contador de programa e pilha pertencem ao contexto de execução.
- **B)** Incorreta. Threads do mesmo processo normalmente compartilham o espaço de endereçamento.
- **C)** Incorreta. A descrição corresponde ao programa armazenado, não ao processo em execução com estado e recursos.
- **D)** Correta. O compartilhamento de código, dados, heap e recursos convive com pilha, registradores e estado próprios de cada thread.

**Conceito:** programa é passivo, processo é instância em execução e thread é fluxo escalonável dentro do processo.

**Pegadinha:** afirmar que threads compartilham tudo ou, no extremo oposto, que são tão isoladas quanto processos distintos.

**Como pensar:** separe o contêiner de recursos, que é o processo, do fluxo de instruções, que é a thread.

**Referência:** [Programa, processo e thread](semana_02_estudo.md#s2-d5-processo-thread).

### Comentário da Questão 3

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Quem aguarda a conclusão de E/S está bloqueado; prioridade não produz o evento externo esperado.
- **B)** Incorreta. Pronto significa apto a executar e aguardando apenas CPU, o que não ocorre enquanto falta a conclusão da leitura.
- **C)** Incorreta. A thread não ocupa o processador simplesmente porque a operação foi iniciada em seu nome.
- **D)** Incorreta. Esperar um evento não significa ter concluído ou sido encerrada.

**Conceito:** pronto aguarda CPU; bloqueado aguarda evento, E/S, lock ou tempo.

**Pegadinha:** classificar como pronta toda thread que não está executando.

**Como pensar:** identifique o que falta: se é apenas processador, está pronta; se é outro evento, está bloqueada.

**Referência:** [Programa, processo e thread — estados conceituais](semana_02_estudo.md#s2-d5-processo-thread).

### Comentário da Questão 4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Quantum menor tende a aumentar, e não eliminar, as trocas de contexto.
- **B)** Incorreta. Quantum grande aproxima Round Robin de FCFS; reduzi-lo reforça a alternância.
- **C)** Correta. Fatias menores podem antecipar o primeiro atendimento, mas elevam o trabalho de salvar e restaurar contextos.
- **D)** Incorreta. Expiração de quantum afeta quem executa; não conclui o evento aguardado por uma thread bloqueada.

**Conceito:** troca de contexto viabiliza a multiplexação, mas tem custo; o quantum equilibra resposta e sobrecarga.

**Pegadinha:** supor que mais alternância seja gratuita ou que o quantum controle eventos de E/S.

**Como pensar:** quantum menor significa oportunidades mais frequentes para outros prontos e, também, mais transições.

**Referência:** [Programa, processo e thread — troca de contexto](semana_02_estudo.md#s2-d5-processo-thread).

### Comentário da Questão 5

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. As threads concluem; não há conjunto permanentemente bloqueado por dependências recíprocas.
- **B)** Incorreta. Ambas executam, portanto nenhuma sofre adiamento indefinido.
- **C)** Incorreta. Não há atividade repetitiva sem progresso, mas uma intercalação que produz valor incorreto.
- **D)** Correta. As duas operações usam o mesmo valor antigo e uma gravação sobrescreve o efeito da outra.

**Conceito:** condição de corrida ocorre quando o resultado depende da ordem não controlada de acessos concorrentes conflitantes.

**Pegadinha:** tratar toda falha de concorrência como deadlock ou presumir que uma expressão de alto nível seja indivisível.

**Como pensar:** decomponha o incremento em ler, calcular e gravar; depois intercale os passos das threads.

**Referência:** [Seção crítica, condição de corrida e atomicidade](semana_02_estudo.md#s2-d5-corrida-atomicidade).

### Comentário da Questão 6

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Outras threads podem observar estados intermediários entre instruções individualmente atômicas.
- **B)** Correta. Uma sequência precisa de proteção própria, e o modelo de memória também envolve visibilidade e ordenação.
- **C)** Incorreta. Uma linha pode compilar para leitura, cálculo e escrita separados.
- **D)** Incorreta. Exclusão da seção crítica não autoriza concluir visibilidade imediata em qualquer arquitetura sem considerar as garantias do mecanismo e do modelo de memória.

**Conceito:** atomicidade, visibilidade e ordenação são propriedades relacionadas, mas distintas.

**Pegadinha:** transferir a indivisibilidade de uma instrução para toda uma sequência lógica.

**Como pensar:** determine qual é a unidade que precisa parecer indivisível para os outros fluxos, não apenas quantas linhas o código ocupa.

**Referência:** [Seção crítica, condição de corrida e atomicidade](semana_02_estudo.md#s2-d5-corrida-atomicidade).

### Comentário da Questão 7

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O mutex ordena os participantes que cooperam usando o mesmo protocolo para o estado protegido.
- **B)** Incorreta. Um acesso que ignora o mutex não é automaticamente bloqueado pelo sistema operacional.
- **C)** Incorreta. A proteção não se estende magicamente a operações alheias ao mutex.
- **D)** Incorreta. No uso convencional, mutex expressa propriedade: quem adquire deve liberar.

**Conceito:** mutex implementa exclusão mútua cooperativa e propriedade exclusiva do lock.

**Pegadinha:** imaginar que a existência do objeto mutex protege a memória mesmo quando parte do código não o utiliza.

**Como pensar:** associe cada invariante compartilhada a um lock e confira se todos os caminhos de acesso obedecem ao mesmo acordo.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

### Comentário da Questão 8

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Variável de condição acompanha um predicado protegido; sozinha não contabiliza oito permissões.
- **B)** Incorreta. Esperar ativamente durante o uso potencialmente longo de uma conexão desperdiçaria CPU.
- **C)** Correta. O contador representa exatamente as oito unidades disponíveis e bloqueia novas aquisições quando chega a zero.
- **D)** Incorreta. Mutex representa propriedade exclusiva, não oito proprietários simultâneos.

**Conceito:** semáforo contador controla N unidades equivalentes; mutex modela exclusão e propriedade.

**Pegadinha:** considerar semáforo e mutex sempre idênticos só porque ambos podem bloquear fluxos.

**Como pensar:** conte as instâncias disponíveis: uma região exclusiva sugere mutex; N unidades sugerem semáforo contador.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

### Comentário da Questão 9

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Se a consumidora conservasse o mutex ao dormir, o produtor não conseguiria adquirir o lock para inserir o item.
- **B)** Incorreta. A condição deve ser reavaliada por causa de despertares espúrios ou porque outro consumidor pode ter retirado o item.
- **C)** Incorreta. O retorno da espera ocorre com o mutex readquirido para que a verificação e a alteração do estado sejam protegidas.
- **D)** Correta. O padrão é testar em laço, liberar atomicamente o mutex durante a espera e readquiri-lo antes de prosseguir.

**Conceito:** variável de condição coordena a espera por um predicado associado a estado protegido por mutex.

**Pegadinha:** trocar `enquanto` por um teste único ou manter o lock enquanto a thread dorme.

**Como pensar:** a notificação diz “o estado pode ter mudado”; somente a nova verificação confirma que o predicado vale.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

### Comentário da Questão 10

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Espera ativa consome ciclos e é inadequada para latências longas de E/S.
- **B)** Correta. Quando a espera será curtíssima, girar pode custar menos que dormir e despertar; se ela se prolonga, o custo cresce.
- **C)** Incorreta. Dormir é justamente o oposto do comportamento de um spinlock, que testa repetidamente.
- **D)** Incorreta. Em um núcleo não preemptível, girar pode impedir que o detentor execute e libere o lock.

**Conceito:** spinlock usa espera ativa e depende de uma expectativa de retenção muito curta.

**Pegadinha:** confundir ausência de troca de contexto com ausência de custo.

**Como pensar:** compare o tempo previsto do lock com o custo de suspensão e considere se o detentor pode executar em outro núcleo.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição — spinlock](semana_02_estudo.md#s2-d5-sincronizacao).

### Comentário da Questão 11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A memória comum reduz cópias, mas os processos precisam coordenar atualizações e publicação de dados.
- **B)** Incorreta. O compartilhamento cria a possibilidade de acessos conflitantes; não os serializa automaticamente.
- **C)** Incorreta. Preservar unidades de mensagem é característica típica de fila de mensagens, não consequência inerente da memória compartilhada.
- **D)** Incorreta. A área foi criada justamente para ser acessível pelos dois processos, reduzindo nessa região o isolamento entre eles.

**Conceito:** memória compartilhada favorece throughput e transfere ao projeto a responsabilidade pela sincronização.

**Pegadinha:** interpretar menos cópias como segurança automática contra corrida.

**Como pensar:** se dois processos podem escrever nos mesmos bytes, procure imediatamente qual primitiva protege o protocolo de acesso.

**Referência:** [Comunicação entre processos — IPC](semana_02_estudo.md#s2-d5-ipc).

### Comentário da Questão 12

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Sinais carregam pouca informação, enquanto sockets não se restringem a processos aparentados.
- **B)** Incorreta. Pipe anônimo não é identificado como uma FIFO nomeada, e memória compartilhada continua exigindo sincronização.
- **C)** Correta. Filas mantêm mensagens como unidades; sockets são apropriados a cliente-servidor local ou em rede.
- **D)** Incorreta. FIFO permite comunicação sem parentesco direto, e RPC não elimina serialização, transporte nem falhas distribuídas.

**Conceito:** mecanismos de IPC diferem em localidade, estrutura dos dados, direção, persistência e custo de cópia.

**Pegadinha:** atribuir a um mecanismo a propriedade marcante de outro ou imaginar que uma abstração de alto nível elimina falhas.

**Como pensar:** relacione a necessidade dominante ao mecanismo: notificação, fluxo, mensagem, bytes compartilhados ou comunicação cliente-servidor.

**Referência:** [Comunicação entre processos — IPC](semana_02_estudo.md#s2-d5-ipc).

### Comentário da Questão 13

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Uma preempção isolada é comportamento normal de escalonamento.
- **B)** Incorreta. Disputa com conclusão normal pode envolver corrida ou contenção, mas não define deadlock.
- **C)** Incorreta. Uma E/S lenta que continua avançando é espera por evento externo, não dependência fechada entre integrantes.
- **D)** Correta. No deadlock, o conjunto não progride porque cada participante depende de ação de outro participante bloqueado.

**Conceito:** deadlock é um impasse conjunto formado por dependências que impedem o progresso.

**Pegadinha:** chamar qualquer bloqueio, lentidão ou falha de concorrência de deadlock.

**Como pensar:** procure um conjunto fechado: quem poderia liberar cada recurso também está esperando dentro do conjunto?

**Referência:** [Deadlock](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 14

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Paralelismo e prioridade não integram a lista de Coffman, e preempção contradiz a condição de não preempção.
- **B)** Correta. As quatro condições clássicas são exclusão mútua, posse e espera, não preempção e espera circular.
- **C)** Incorreta. A lista mistura mecanismos e outros problemas de progresso.
- **D)** Incorreta. Nenhum desses quatro elementos forma o conjunto necessário definido por Coffman.

**Conceito:** as quatro condições de Coffman precisam coexistir no deadlock clássico de recursos reutilizáveis.

**Pegadinha:** considerar uma condição isolada, como exclusão mútua, prova suficiente de deadlock.

**Como pensar:** memorize a cadeia lógica: recurso exclusivo, processo mantém um enquanto pede outro, recurso não é retirado e a espera fecha um ciclo.

**Referência:** [Deadlock — condições necessárias de Coffman](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 15

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Uma ordem global respeitada por todos impede que as arestas de espera fechem um ciclo de aquisição.
- **B)** Incorreta. Cada lock ainda pode continuar exclusivo.
- **C)** Incorreta. A regra não autoriza retirar compulsoriamente um lock já adquirido.
- **D)** Incorreta. O fluxo ainda pode manter `L1` enquanto espera `L2`; o que foi eliminado é a aquisição em ordem circular.

**Conceito:** prevenção rompe deliberadamente ao menos uma condição necessária; ordenação global rompe espera circular.

**Pegadinha:** escolher posse e espera apenas porque um processo mantém um lock durante a aquisição seguinte.

**Como pensar:** imagine as setas de aquisição sempre apontando de índice menor para maior; elas não conseguem retornar ao início.

**Referência:** [Deadlock — prevenção](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 16

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Solicitar tudo de uma vez não torna compartilhável um recurso intrinsecamente exclusivo.
- **B)** Incorreta. A política descrita não retira recursos já concedidos; evita a concessão parcial inicial.
- **C)** Correta. O processo não fica segurando parte dos recursos enquanto aguarda os restantes, mas pode reservar recursos antes de efetivamente usá-los.
- **D)** Incorreta. A técnica não atua diretamente sobre a ordem circular e pode, sim, prejudicar utilização e concorrência.

**Conceito:** aquisição integral antecipada é prevenção por ruptura da condição de posse e espera.

**Pegadinha:** confundir a condição rompida com espera circular ou ignorar o custo de baixa utilização.

**Como pensar:** pergunte se o processo pode manter algum recurso enquanto espera outro; pela regra, a resposta é não.

**Referência:** [Deadlock — prevenção](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 17

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Pode haver estado seguro com recursos alocados, desde que exista sequência viável de liberações e conclusões.
- **B)** Incorreta. A sequência pode ser serial e depender de recursos liberados por quem conclui antes.
- **C)** Incorreta. Segurança não exige abolir todos os recursos exclusivos.
- **D)** Correta. Basta existir alguma ordem em que todos possam terminar; inseguro significa perda dessa garantia, não impasse consumado.

**Conceito:** evitação concede pedidos somente quando o estado resultante conserva uma sequência segura.

**Pegadinha:** igualar estado inseguro a deadlock já existente.

**Como pensar:** tente construir uma ordem de conclusão usando os disponíveis e as liberações sucessivas; se alguma ordem funciona, o estado é seguro.

**Referência:** [Deadlock — evitação](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 18

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Prioridade não informa se os pedidos futuros podem ser atendidos com os recursos existentes.
- **B)** Correta. O banqueiro compara demandas máximas e necessidades remanescentes com alocações e disponibilidade para testar uma sequência segura.
- **C)** Incorreta. Essa descrição remete ao grafo de espera usado em um caso de detecção, não aos dados do banqueiro.
- **D)** Incorreta. Evitação decide antes da concessão; não depende de interromper arbitrariamente processos.

**Conceito:** o algoritmo do banqueiro evita estados inseguros com base em demanda máxima conhecida e disponibilidade.

**Pegadinha:** atribuir ao algoritmo propriedades de detecção ou recuperação posterior.

**Como pensar:** como a decisão antecipa o futuro, é necessário conhecer o máximo que cada processo ainda poderá solicitar.

**Referência:** [Deadlock — evitação](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 19

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Com uma instância por tipo, o ciclo no grafo de espera é necessário e suficiente; com múltiplas, é preciso considerar quantidades.
- **B)** Incorreta. Uma instância livre adicional pode permitir que um processo conclua e desfaça o ciclo aparente.
- **C)** Incorreta. No caso de instância única, a ausência de ciclo afasta o deadlock representado pelo grafo.
- **D)** Incorreta. Um processo pode estar bloqueado por E/S normal sem integrar qualquer impasse.

**Conceito:** a suficiência de um ciclo para detectar deadlock depende do número de instâncias de cada tipo de recurso.

**Pegadinha:** transportar automaticamente a regra do caso de instância única para múltiplas instâncias.

**Como pensar:** antes de concluir pelo ciclo, pergunte se existe outra unidade do recurso capaz de liberar algum participante.

**Referência:** [Deadlock — detecção](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 20

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Uma vítima aleatória pode destruir mais trabalho ou violar invariantes e consistência transacional.
- **B)** Incorreta. Detectar apenas identifica o impasse; alguma ação de recuperação ainda é necessária.
- **C)** Correta. Custo, prioridade, trabalho realizado e recursos mantidos orientam a vítima; rollback requer checkpoint consistente.
- **D)** Incorreta. Prioridade de CPU não retira automaticamente recursos nem desfaz dependências.

**Conceito:** recuperação pode abortar, preemptar quando possível ou restaurar estado, sempre respeitando consistência e custo.

**Pegadinha:** supor que detecção resolva o deadlock ou que qualquer encerramento seja seguro.

**Como pensar:** escolha a ação que efetivamente rompe o ciclo e, ao mesmo tempo, preserva as invariantes da aplicação.

**Referência:** [Deadlock — recuperação](semana_02_estudo.md#s2-d5-deadlock).

### Comentário da Questão 21

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Outros fluxos progridem e não foi descrito ciclo de recursos, portanto não é deadlock.
- **B)** Incorreta. A tarefa preterida não permanece ativa reagindo sem progresso, como ocorreria no livelock.
- **C)** Incorreta. Não há resultado dependente de acessos conflitantes a dados compartilhados.
- **D)** Correta. O adiamento indefinido é starvation; aging reduz o problema elevando gradualmente a prioridade de quem espera.

**Conceito:** starvation afeta um participante continuamente preterido enquanto o sistema como um todo pode progredir.

**Pegadinha:** confundir ausência de progresso individual com deadlock do conjunto.

**Como pensar:** verifique se outros concluem e se a vítima continua apta: esse padrão aponta para falta de justiça no atendimento.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

### Comentário da Questão 22

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O enunciado mostra as duas threads ativas, não uma delas indefinidamente preterida.
- **B)** Correta. Há mudanças de estado e tentativas contínuas, porém nenhuma produz progresso útil; o backoff dessincroniza novas tentativas.
- **C)** Incorreta. No deadlock, os participantes permanecem bloqueados; aqui eles agem e reagem repetidamente.
- **D)** Incorreta. Paralelismo descreve simultaneidade, não falha de progresso, e programa passivo não soluciona o protocolo.

**Conceito:** livelock é atividade contínua sem avanço útil, muitas vezes produzida por respostas simétricas.

**Pegadinha:** tomar qualquer ausência de conclusão por bloqueio de deadlock.

**Como pensar:** observe se os estados ainda mudam; se há movimento sem aproximação da conclusão, pense em livelock.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

### Comentário da Questão 23

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A prioridade efetiva fica invertida pela dependência do lock; herança permite que a detentora execute e o libere mais cedo.
- **B)** Incorreta. A baixa sofre preempções, mas o fenômeno central é a alta depender dela enquanto intermediárias interferem; quantum geral não é solução necessária.
- **C)** Incorreta. Não foram demonstradas espera circular nem todas as condições de Coffman.
- **D)** Incorreta. A alta está bloqueada pelo mutex, e não ativa alterando estados sem progresso.

**Conceito:** inversão de prioridade é a espera indireta de uma thread alta por uma baixa que mantém recurso necessário.

**Pegadinha:** acreditar que a política de prioridade resolve a espera, embora a baixa precise executar para liberar o lock.

**Como pensar:** siga a dependência real: a alta depende da baixa; logo, elevar temporariamente a baixa ajuda a alta.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

### Comentário da Questão 24

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A situação I contém espera circular, e a III envolve atividade, não simples corrida por resultado.
- **B)** Incorreta. I não apresenta atividade contínua; II não informa uma dependência de prioridades por lock.
- **C)** Correta. I é impasse circular, II é adiamento indefinido individual e III é atividade recíproca sem avanço.
- **D)** Incorreta. I descreve dependência de locks, II não tem reações ativas e III não é mero preterimento.

**Conceito:** deadlock, starvation e livelock têm causas e padrões de progresso distintos.

**Pegadinha:** usar “não terminou” como critério único e ignorar se os fluxos estão bloqueados, preteridos ou ativos.

**Como pensar:** classifique pelo movimento: ciclo bloqueado é deadlock; um apto esquecido é starvation; atividade inútil é livelock.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

### Comentário da Questão 25

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A seção crítica deve abranger o estado que precisa permanecer coerente, não toda operação executada pela thread.
- **B)** Incorreta. Bloquear por E/S não libera automaticamente um mutex já adquirido.
- **C)** Incorreta. Um mutex não muda de natureza nem admite múltiplos proprietários porque seu detentor aguarda rede.
- **D)** Correta. Reter lock durante latência longa prolonga a espera dos concorrentes e pode integrar dependências que formem deadlock.

**Conceito:** locks devem proteger o menor estado coerente possível; retenção durante E/S amplia contenção e risco de dependências.

**Pegadinha:** presumir que a thread perde a propriedade do mutex ao deixar a CPU ou entrar no estado bloqueado.

**Como pensar:** separe a atualização do estado compartilhado da operação lenta e verifique se o lock é realmente necessário durante toda a espera.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).


### Comentário da Questão 26

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Os valores não correspondem às esperas 0, 5 e 6 nem aos retornos 6, 7 e 7.
- **B)** Correta. No FCFS, P1 executa de 0 a 6, P2 de 6 a 8 e P3 de 8 a 9. A espera média é (0 + 5 + 6)/3 = 11/3, e o retorno médio é (6 + 7 + 7)/3 = 20/3.
- **C)** Incorreta. A alternativa altera as médias apesar de a ordem FCFS estar determinada pelas chegadas.
- **D)** Incorreta. Cinco não é a média das esperas; é apenas a espera individual de P2.

**Conceito:** FCFS e cálculo de espera e retorno.

**Pegadinha:** confundir o início ou a conclusão absolutos com a métrica relativa à chegada de cada processo.

**Como pensar:** desenhe primeiro a linha 0–6 P1, 6–8 P2, 8–9 P3. Depois use retorno = conclusão − chegada e, neste caso de um único burst, espera = retorno − burst.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário da Questão 27

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Com todos disponíveis no instante zero, SJF escolhe o menor próximo burst, não a ordem nominal A, B, C.
- **B)** Incorreta. Depois de C, o burst de B é menor que o de A; logo, C, A, B não é a ordem SJF.
- **C)** Incorreta. Escolher B antes de C viola o critério de menor burst entre os processos prontos.
- **D)** Correta. A execução é C de 0 a 1, B de 1 a 5 e A de 5 a 12. As esperas são 0, 1 e 5; a média é 2.

**Conceito:** SJF não preemptivo e minimização da espera média sob hipóteses ideais.

**Pegadinha:** tratar chegada simultânea como obrigação de FCFS ou calcular espera pela posição sem considerar a duração dos anteriores.

**Como pensar:** ordene os bursts disponíveis do menor para o maior e some, para cada processo, o tempo consumido pelos que o antecedem.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário da Questão 28

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. B chega quando A tem 7 unidades restantes e o preempta; C chega quando B tem 3 restantes e também preempta. As conclusões são C=4, B=7 e A=14; espera = retorno − burst produz A=6, B=2 e C=0.
- **B)** Incorreta. SRTF é justamente a versão preemptiva do SJF.
- **C)** Incorreta. No instante 2, C tem burst 2 e B ainda tem 3; portanto, C deve preemptar B.
- **D)** Incorreta. Um escalonador não escolhe processo que ainda não chegou à fila de prontos.

**Conceito:** SRTF, preempção e tempo restante.

**Pegadinha:** comparar bursts originais em vez do tempo restante ou antecipar a execução de processo que chegará no futuro.

**Como pensar:** reavalie a fila em cada chegada. Compare o restante de quem executa com o burst do recém-chegado e só então trace o próximo intervalo.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário da Questão 29

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Favorecer ainda mais as tarefas de alta prioridade agrava o adiamento da tarefa de baixa prioridade.
- **B)** Incorreta. Polling e interrupção tratam comunicação com dispositivos, não corrigem a política de prioridade da fila de prontos.
- **C)** Correta. Aging aumenta gradualmente a prioridade de quem espera e reduz o risco de starvation.
- **D)** Incorreta. Bloquear a tarefa por E/S retira-a da fila de prontos e não garante que receberá CPU quando voltar.

**Conceito:** starvation em escalonamento por prioridade e aging.

**Pegadinha:** confundir starvation com bloqueio por evento ou tentar resolver o problema concedendo mais recursos a quem já é favorecido.

**Como pensar:** observe que outros processos continuam progredindo enquanto um pronto é adiado indefinidamente; isso caracteriza starvation, e a resposta deve alterar a preferência ao longo da espera.

**Referência:** [7. Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock) e [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário da Questão 30

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Round Robin intercala os processos e pode mudar a ordem de conclusão em relação ao FCFS.
- **B)** Correta. A linha é 0–2 A, 2–4 B, 4–5 C, 5–7 A, 7–8 B e 8–9 A. Assim, C, B e A concluem em 5, 8 e 9; os primeiros atendimentos ocorrem em 0, 2 e 4.
- **C)** Incorreta. Um processo que termina antes do fim da fatia não guarda nem transfere o restante do quantum.
- **D)** Incorreta. Round Robin segue a fila circular, não escolhe automaticamente o menor burst.

**Conceito:** Round Robin, quantum, conclusão e resposta.

**Pegadinha:** emprestar quantum não utilizado ao processo seguinte ou aplicar o critério de SJF ao Round Robin.

**Como pensar:** simule cada fatia na ordem da fila, reinsira apenas quem ainda tem burst e registre separadamente primeiro atendimento e conclusão.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário da Questão 31

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Fatias pequenas aumentam a frequência de preempção e o custo de alternância; quando a fatia é muito grande, cada processo tende a executar como no FCFS.
- **B)** Incorreta. Diminuir o quantum aumenta, não elimina, trocas de contexto e não cria o critério de menor burst do SJF.
- **C)** Incorreta. Quantum grande pode atrasar o primeiro atendimento dos processos que estão atrás de um burst longo.
- **D)** Incorreta. O quantum afeta responsividade, número de trocas e comportamento da fila.

**Conceito:** compromisso entre responsividade e sobrecarga no Round Robin.

**Pegadinha:** supor que quanto menor ou maior o quantum, melhor será o sistema em todas as métricas.

**Como pensar:** compare dois limites: fatia quase nula gera alternância frequente; fatia maior que os bursts deixa cada processo terminar em sua vez.

**Referência:** [2. Programa, processo e thread](semana_02_estudo.md#s2-d5-processo-thread) e [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário da Questão 32

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. FCFS é não preemptivo no modelo clássico, mas SRTF é preemptivo.
- **B)** Incorreta. SJF clássico não preempta; Round Robin preempta ao fim do quantum, independentemente da chegada de prioridade superior.
- **C)** Incorreta. Prioridade pode ter versões preemptiva e não preemptiva, enquanto FCFS clássico não preempta.
- **D)** Correta. A alternativa classifica cada algoritmo de acordo com a definição apresentada na teoria.

**Conceito:** preempção nos algoritmos clássicos de CPU.

**Pegadinha:** inferir a preempção pelo nome do algoritmo ou tratar uma política que admite variantes como se tivesse somente uma forma.

**Como pensar:** pergunte qual evento retira a CPU do processo: FCFS/SJF aguardam bloqueio ou término; SRTF reage a menor restante; RR usa o fim do quantum; prioridade depende da variante.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário da Questão 33

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte os papéis: controlador integra a lógica física, enquanto driver é software.
- **B)** Incorreta. A abstração fornecida pelo sistema e pelo driver evita que a aplicação comum manipule detalhes elétricos e registradores específicos.
- **C)** Correta. O controlador expõe lógica e registradores; o driver traduz solicitações e coordena filas, buffers, falhas e término da operação.
- **D)** Incorreta. Escalonamento de CPU é outra função do sistema operacional e não define driver ou controlador.

**Conceito:** camadas de controle de dispositivos e papel do driver.

**Pegadinha:** trocar hardware por software ou imaginar que a aplicação precise conhecer diretamente cada dispositivo.

**Como pensar:** siga o caminho da solicitação: aplicação usa interface padronizada, driver converte a operação, controlador interage com o dispositivo físico.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).

### Comentário da Questão 34

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Polling é consulta ativa e repetida; sua conveniência depende da frequência e da duração esperada, pois esperar muito dessa forma consome CPU.
- **B)** Incorreta. Notificação iniciada pelo dispositivo descreve interrupção, não polling.
- **C)** Incorreta. Transferência de blocos com menor participação por palavra descreve DMA, que ainda requer configuração.
- **D)** Incorreta. Polling não é sinônimo obrigatório de E/S síncrona e mecanismos diferentes podem coexistir no mesmo driver.

**Conceito:** polling e seu custo operacional.

**Pegadinha:** definir polling pelos conceitos vizinhos de interrupção ou DMA, ou convertê-lo em uma classificação rígida de sincronismo.

**Como pensar:** procure quem inicia a verificação: no polling, CPU ou driver pergunta repetidamente; na interrupção, o dispositivo sinaliza.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).

### Comentário da Questão 35

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Manter uma ISR em processamento demorado eleva latência e pode prejudicar outros eventos; o trabalho extenso deve ser diferido.
- **B)** Incorreta. Reiniciar o sistema não é procedimento normal de reconhecimento de uma interrupção.
- **C)** Incorreta. A ISR pode tratar a conclusão de uma transferência feita por DMA; ela não precisa copiar pessoalmente cada byte.
- **D)** Correta. A rotina reconhece a origem, preserva o mínimo necessário, agenda o restante e retorna rapidamente.

**Conceito:** interrupção e desenho de rotina de serviço curta.

**Pegadinha:** confundir a notificação da conclusão com todo o trabalho de transferência ou processamento posterior.

**Como pensar:** separe resposta urgente ao hardware de trabalho demorado: a primeira fica na ISR; o segundo segue para contexto apropriado.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).

### Comentário da Questão 36

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Fornecer parâmetros é configuração da transferência e não transforma DMA em polling.
- **B)** Correta. DMA move o bloco entre dispositivo e memória com menor intervenção da CPU por unidade; a CPU ainda configura, protege e trata o término.
- **C)** Incorreta. Journaling registra transações do sistema de arquivos para recuperação de consistência, não executa a cópia descrita.
- **D)** Incorreta. Round Robin é uma política de escalonamento de CPU, sem relação com o mecanismo de transferência do bloco.

**Conceito:** DMA e limites da expressão transferência direta.

**Pegadinha:** interpretar menor participação da CPU como ausência total de CPU ou confundir parâmetros de DMA com consulta repetida.

**Como pensar:** identifique quem move os dados em massa. Se a controladora transfere o bloco após configuração e avisa ao final, o núcleo é DMA com possível interrupção de conclusão.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).

### Comentário da Questão 37

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A interrupção pode anunciar justamente que uma transferência DMA terminou.
- **B)** Incorreta. Um driver pode combinar estratégias e usar polling em uma fase e interrupções ou DMA em outra.
- **C)** Correta. DMA transfere o bloco, enquanto a interrupção pode notificar a conclusão; ambos podem integrar a mesma operação.
- **D)** Incorreta. Interrupção sinaliza ou transfere controle para tratamento; DMA é o mecanismo de transferência de dados em bloco.

**Conceito:** composição de polling, interrupção e DMA.

**Pegadinha:** tratar mecanismos com funções diferentes como alternativas mutuamente exclusivas.

**Como pensar:** atribua um verbo a cada conceito: polling consulta, interrupção avisa, DMA transfere. Verbos diferentes podem aparecer no mesmo fluxo.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).

### Comentário da Questão 38

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O diretório associa um nome ao objeto, o inode ou estrutura equivalente registra metadados e localização do conteúdo, e o descritor ou handle referencia uma abertura feita por um processo.
- **B)** Incorreta. O nome pertence à relação mantida pelo diretório; inode não é simplesmente o texto do nome nem desaparece por causa da abertura.
- **C)** Incorreta. Montar associa uma instância de sistema de arquivos a um ponto do namespace; não significa copiar seu conteúdo.
- **D)** Incorreta. Descritores e handles pertencem ao contexto de processos e não anulam proteção ou controle de acesso.

**Conceito:** abstrações de nome, metadados, abertura e montagem em sistemas de arquivos.

**Pegadinha:** fundir nome, inode e descritor como se fossem uma única estrutura ou interpretar montagem como cópia física.

**Como pensar:** separe três momentos: o diretório localiza pelo nome, a estrutura persistente descreve o objeto e a abertura entrega ao processo uma referência de trabalho.

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos).

### Comentário da Questão 39

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Descritores sem commit válido não demonstram que a transação foi concluída.
- **B)** Correta. No replay, uma transação confirmada pode ser reproduzida; uma transação sem commit válido é incompleta e deve ser descartada.
- **C)** Incorreta. Journal não é repositório garantido de todas as versões históricas de arquivos.
- **D)** Incorreta. Replay busca consistência das estruturas, não cria backup completo do volume.

**Conceito:** commit e replay de transações do journal.

**Pegadinha:** considerar qualquer registro parcial suficiente para confirmar a transação ou atribuir ao journal a função de versionamento.

**Como pensar:** procure a evidência de confirmação. Sem commit válido, a operação não deve ser consolidada como transação concluída durante a recuperação.

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos).

### Comentário da Questão 40

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A descrição de dados e metadados passando pelo journal corresponde a data=journal, não ao padrão data=ordered.
- **B)** Incorreta. data=journal inclui dados e metadados no journal; a alternativa o confunde com uma política mais fraca.
- **C)** Incorreta. data=writeback possui ordenação mais fraca, e nenhum modo de journaling equivale a backup.
- **D)** Correta. data=ordered registra metadados e ordena a gravação dos dados no destino principal antes do commit correspondente; data=journal registra ambos, com maior custo.

**Conceito:** diferenças entre data=ordered, data=journal e data=writeback no ext4.

**Pegadinha:** supor que a palavra ordered signifique registrar todo o conteúdo no journal ou classificar writeback como a garantia mais forte.

**Como pensar:** pergunte duas coisas: o que entra no journal e qual ordem existe entre dados no destino principal e commit de metadados.

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos).

### Comentário da Questão 41

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Journal não mantém necessariamente versões anteriores e não dispensa cópia recuperável independente.
- **B)** Incorreta. Consistência estrutural não implica preservação de conteúdo que foi excluído de maneira válida.
- **C)** Correta. Journaling reduz inconsistência após falha, mas não atende sozinho a versionamento, exclusão, ransomware, incêndio ou perda simultânea da mídia.
- **D)** Incorreta. Replicação para mídia independente não é uma consequência automática da existência de journal.

**Conceito:** journaling versus backup.

**Pegadinha:** confundir recuperação das estruturas do sistema de arquivos com recuperação do estado histórico desejado pelo usuário.

**Como pensar:** formule a pergunta de recuperação: é preciso tornar o volume consistente após queda ou restaurar uma versão anterior a partir de outra cópia? O segundo objetivo exige estratégia de backup.

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos).

### Comentário da Questão 42

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Sete corresponde a 4+2+1, ou rwx; cinco corresponde a 4+1, ou r-x; zero não concede qualquer bit.
- **B)** Incorreta. A decomposição proposta corresponderia a outros algarismos e ainda atribui permissão inexistente aos demais.
- **C)** Incorreta. A primeira tríade é do proprietário e a segunda do grupo; 5 não representa controle total.
- **D)** Incorreta. Cada algarismo deve ser decomposto dentro de sua própria tríade, e não somado aos demais.

**Conceito:** notação octal das permissões Linux em arquivo regular.

**Pegadinha:** somar algarismos entre sujeitos ou trocar a ordem proprietário, grupo e outros.

**Como pensar:** leia da esquerda para a direita por sujeito e decomponha cada dígito com r=4, w=2 e x=1.

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).

### Comentário da Questão 43

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Leitura do diretório relaciona-se à listagem de nomes e não concede execução sobre os arquivos contidos.
- **B)** Incorreta. Escrita no diretório atua sobre entradas; não reescreve automaticamente o conteúdo de todos os arquivos.
- **C)** Incorreta. Em diretório, x significa travessia ou pesquisa de componentes, não executar o diretório como programa.
- **D)** Correta. A alternativa distingue listagem, travessia e alteração de entradas, lembrando que as combinações e permissões do caminho importam.

**Conceito:** semântica de r, w e x em diretórios Linux.

**Pegadinha:** transportar sem adaptação a semântica dos bits em arquivo regular para um diretório.

**Como pensar:** em diretório, associe r a ver nomes, x a alcançar objetos pelo caminho e w a modificar a relação de entradas, sempre considerando os demais acessos necessários.

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).

### Comentário da Questão 44

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. ps e top observam processos; journalctl consulta logs.
- **B)** Correta. chmod altera bits de modo, chown muda titularidade e getfacl inspeciona ACL estendida.
- **C)** Incorreta. ip e ss apoiam diagnóstico de rede, enquanto systemctl administra ou consulta serviços.
- **D)** Incorreta. df e findmnt tratam espaço e montagem; free observa memória.

**Conceito:** comandos Linux relacionados a permissões e ACLs.

**Pegadinha:** escolher um trio de comandos reais, mas pertencentes a outra finalidade administrativa.

**Como pensar:** associe o verbo principal ao nome do comando: mode em chmod, owner em chown e ACL em getfacl.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos) e [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).

### Comentário da Questão 45

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Uma DACL reúne ACEs que concedem ou negam direitos; não se limita ao proprietário.
- **B)** Incorreta. ACEs podem ser herdadas de pastas e participar da autorização do objeto filho.
- **C)** Correta. A alternativa descreve DACL, ACE, herança e a atuação conjunta de permissões de compartilhamento e NTFS no acesso remoto.
- **D)** Incorreta. A permissão efetiva não é simplesmente a maior entre os dois conjuntos; ambos podem restringir a operação.

**Conceito:** DACLs, ACEs, herança e permissões efetivas no Windows.

**Pegadinha:** reduzir DACL à propriedade do objeto ou aplicar a regra intuitiva de que sempre prevalece a permissão mais ampla.

**Como pensar:** identifique a identidade efetiva, reúna ACEs aplicáveis e depois verifique todas as camadas de autorização atravessadas pelo acesso remoto.

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).

### Comentário da Questão 46

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Get-Process e tasklist observam processos; icacls atua sobre controle de acesso a arquivos e diretórios.
- **B)** Correta. icacls pode exibir e modificar DACLs e é o substituto atual do antigo cacls depreciado.
- **C)** Incorreta. Acompanhamento contínuo de recursos é função de ferramentas de processos, não de um utilitário de ACL.
- **D)** Incorreta. Configuração de rede é consultada por comandos próprios, como ipconfig e ferramentas PowerShell de rede.

**Conceito:** finalidade do icacls no Windows.

**Pegadinha:** inferir a função apenas porque o comando é administrativo ou confundir ACL com processos e rede.

**Como pensar:** o fragmento acl no nome ajuda a lembrar que o objeto do comando é a lista de controle de acesso.

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes) e [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos).

### Comentário da Questão 47

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. ps oferece uma fotografia do estado, e ps -eLf evidencia processos e threads; top atualiza a visão continuamente.
- **B)** Incorreta. top não altera DACL, e ps não reinicia serviços.
- **C)** Incorreta. journalctl consulta eventos, enquanto chmod altera permissões; nenhum cumpre as duas finalidades pedidas.
- **D)** Incorreta. ip route observa rotas, e ss observa sockets; esses comandos não escalonam nem enumeram processos em geral.

**Conceito:** observação pontual e contínua de processos e threads no Linux.

**Pegadinha:** reconhecer nomes válidos de comandos sem conferir o objeto que cada um observa ou modifica.

**Como pensar:** associe ps a process snapshot e top à tela dinâmica de consumo; depois verifique se a opção escolhida expõe threads.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos).

### Comentário da Questão 48

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Os pares atuam em permissões, não em estado de serviço e eventos.
- **B)** Incorreta. ip addr e ss são ferramentas de rede, e Stop-Process altera o estado de um processo.
- **C)** Incorreta. kill e taskkill encerram processos; não são instrumentos de mera consulta a serviço e log.
- **D)** Correta. systemctl status e Get-Service consultam serviços; journalctl e Get-WinEvent consultam registros de eventos nos respectivos sistemas.

**Conceito:** comandos de serviços e logs no Linux e no Windows.

**Pegadinha:** misturar comandos de observação com comandos de encerramento ou formar pares de sistemas operacionais diferentes.

**Como pensar:** divida o pedido em duas colunas, serviço e log, e só depois escolha a ferramenta correspondente em cada plataforma.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos).

### Comentário da Questão 49

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O trio atua sobre permissões e ACLs, não sobre configuração e sockets de rede.
- **B)** Incorreta. ps e kill tratam processos, e free observa memória.
- **C)** Correta. ip addr e ip route mostram endereços e rotas; ss -tulpn ajuda a relacionar sockets de escuta a protocolos e processos.
- **D)** Incorreta. systemctl e journalctl tratam serviços e logs, e findmnt mostra sistemas montados.

**Conceito:** comandos Linux de diagnóstico de configuração e sockets de rede.

**Pegadinha:** selecionar comandos administrativos conhecidos, mas que respondem a perguntas operacionais diferentes.

**Como pensar:** formule a pergunta antes do comando: onde está o endereço e a rota aponta para onde? Quais sockets estão escutando e qual processo os mantém?

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos).

### Comentário da Questão 50

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A ordem não corresponde às finalidades, taskkill altera processo e journalctl pertence ao Linux.
- **B)** Correta. Get-Process lista processos; Get-Service consulta serviços; ipconfig exibe a configuração IP; Get-NetTCPConnection examina conexões; icacls inspeciona ou modifica permissões NTFS.
- **C)** Incorreta. O conjunto reúne comandos Linux e não atende ao cenário Windows.
- **D)** Incorreta. A sequência contém ações destrutivas ou de alteração e usa o cacls depreciado, além de não corresponder às consultas pedidas.

**Conceito:** associação entre finalidade e comandos administrativos no Windows.

**Pegadinha:** confundir listar com encerrar, misturar plataformas ou preferir ferramenta depreciada quando existe substituta atual.

**Como pensar:** associe um substantivo a cada utilitário: processo, serviço, configuração IP, conexão e ACL; descarte imediatamente comandos de remoção ou encerramento quando o pedido é inspeção.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos) e [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).


---

## Questões extras de revisão fixa do Dia 5

#### Extra Dia 5.1

Considerando o escopo de Legislação CRA/CFA adotado para o cargo de Analista de Sistemas após a Retificação I, assinale a alternativa correta.

A) A RN CFA nº 640/2024 permanece como Código vigente no edital, e a RN nº 671/2025 trata do Regimento do CRA-PR.
B) As RNs nº 589/2020, nº 649/2024 e nº 670/2025 constituem o núcleo autônomo das quinze extras do Dia 5.
C) O núcleo é formado pela Lei nº 4.769/1965, pelo Decreto nº 61.934/1967, pelo Regimento/RN nº 651/2024 e pelo Código/RN nº 671/2025; as demais normas citadas no bloco ficam apenas como contexto externo.
D) Somente o Regimento pode fundamentar as extras, pois Lei, Decreto e Código possuem aplicação nacional.

#### Extra Dia 5.2

Sobre natureza, autonomia e jurisdição do CRA-PR, assinale a alternativa correta.

A) É autarquia de direito público, com autonomia técnica, administrativa e financeira, sede na capital e jurisdição em todo o Paraná nas matérias de sua competência; autonomia não significa soberania.
B) É associação privada com jurisdição nacional e independência normativa absoluta do CFA.
C) É órgão sem personalidade da Administração Direta estadual e atua apenas no município da sede.
D) A autonomia permite ao CRA-PR deixar de executar diretrizes do CFA e aprovar definitivamente o próprio Regimento.

#### Extra Dia 5.3

Assinale a alternativa que contém apenas órgãos ou estruturas enumerados no art. 3º do Regimento do CRA-PR.

A) Plenário, Tribunal de Contas, Ouvidoria e Ministério Público.
B) Diretoria Executiva, Assembleia Legislativa, Ouvidoria e Poder Judiciário.
C) Plenário, Diretoria Executiva, Secretaria Estadual e conselho municipal.
D) Plenário, Diretoria Executiva, Ouvidoria, Comissões Permanentes e Especiais e Grupos de Trabalho, além dos Órgãos de Representação.

#### Extra Dia 5.4

No Regimento do CRA-PR, o Plenário é:

A) unidade exclusivamente consultiva, sem competência de julgamento.
B) órgão colegiado de deliberação superior e primeira instância de julgamento no âmbito da jurisdição regional.
C) órgão executivo subordinado à Ouvidoria.
D) última instância nacional para recursos de todos os Conselhos Regionais.

#### Extra Dia 5.5

Sobre composição e mandato do Plenário, assinale a alternativa correta.

A) É formado por cinco Diretores, todos com mandato anual sem reeleição.
B) Possui nove membros sem suplentes, renovados integralmente a cada quatro anos.
C) É composto por nove Conselheiros Efetivos e respectivos Suplentes; renova-se a cada dois anos em um terço e dois terços alternadamente, e o mandato é de quatro anos, permitida uma reeleição.
D) Seus membros possuem mandato de dois anos, idêntico ao da Diretoria, e reeleições ilimitadas.

#### Extra Dia 5.6

Constitui competência do Plenário do CRA-PR:

A) aprovar os Planos Anuais de Fiscalização e de Trabalho, eleger membros da Diretoria e das Comissões Permanentes e julgar, em primeira instância, infrações profissionais.
B) apenas receber manifestações e encaminhá-las, sem poder deliberar.
C) exercer sozinho toda a administração cotidiana, sem participação da Diretoria.
D) instituir Comissão Especial sem ouvir a Diretoria e dispensar posterior homologação.

#### Extra Dia 5.7

Nos termos do Regimento, a Diretoria Executiva é composta por:

A) Presidente, Ouvidor, três representantes estaduais e um membro do CFA.
B) nove Conselheiros Efetivos e seus nove Suplentes.
C) Presidente, Secretário-Geral e representantes de cada município paranaense.
D) Presidente, Vice-Presidente, Diretor de Administração e Finanças, Diretor de Fiscalização e Registro e Diretor de Relações Institucionais.

#### Extra Dia 5.8

Assinale a alternativa que diferencia corretamente Diretoria Executiva e Plenário.

A) A Diretoria aprova definitivamente os Planos Anuais, enquanto o Plenário apenas os protocola.
B) A Diretoria analisa os Planos e os encaminha à apreciação do Plenário, que os aprova; a Diretoria também homologa a instituição e composição de Comissões Especiais e Grupos de Trabalho.
C) O Plenário executa sozinho todas as decisões, e a Diretoria funciona como canal de Ouvidoria.
D) Diretoria e Plenário são nomes alternativos do mesmo órgão e possuem competências indistintas.

#### Extra Dia 5.9

Quanto às competências do Presidente do CRA-PR, assinale a alternativa correta.

A) O Presidente não representa legalmente o Conselho e não pode convocar reuniões.
B) O Presidente homologa sozinho toda decisão do Plenário, sem controle colegiado.
C) O Presidente representa o CRA-PR, convoca e preside reuniões, distribui processos e institui Comissões Especiais e Grupos de Trabalho, ouvida a Diretoria; decisão urgente `ad referendum` depende de posterior apreciação.
D) A decisão `ad referendum` transfere definitivamente ao Presidente a competência do colegiado.

#### Extra Dia 5.10

Sobre reuniões e quórum no Regimento do CRA-PR, assinale a alternativa correta.

A) Plenário e Diretoria reúnem-se ordinariamente de uma a quatro vezes por mês; reunião extraordinária exige justificativa e pauta prévia, admite-se videoconferência, e o quórum de instalação e funcionamento é a maioria absoluta dos membros.
B) Reuniões ordinárias podem ocorrer no máximo uma vez por ano, e videoconferência é proibida.
C) Maioria absoluta é calculada somente sobre os membros presentes na sessão.
D) Reunião extraordinária dispensa pauta e só pode ser convocada por órgão externo.

#### Extra Dia 5.11

A respeito da Ouvidoria do CRA-PR, assinale a alternativa correta.

A) Julga infrações profissionais em primeira instância e aplica penalidades.
B) Substitui a Diretoria Executiva na administração financeira.
C) Seu titular pode ser qualquer terceiro não vinculado ao Plenário, com mandato independente.
D) O Ouvidor é eleito pelo Plenário entre Conselheiros Efetivos; a unidade é mediadora, recebe, trata, encaminha e acompanha manifestações, sem caráter executivo, deliberativo ou decisório.

#### Extra Dia 5.12

Sobre Comissões e Grupos de Trabalho, assinale a alternativa correta.

A) Toda Comissão Permanente possui cinco membros, e integrante da Diretoria deve coordenar a Comissão de Análise de Contas.
B) Salvo norma específica, Comissões Permanentes têm três membros; membro da Diretoria não integra a Comissão de Análise de Contas; Comissões Especiais e Grupos de Trabalho têm no máximo cinco membros e caráter específico ou temporário.
C) Comissões Especiais são permanentes e seus atos não precisam indicar prazo.
D) Grupos de Trabalho exercem julgamento definitivo e não se limitam ao estudo de temas.

#### Extra Dia 5.13

Segundo as disposições gerais do Regimento, assinale a alternativa correta.

A) Incluem-se o dia inicial e exclui-se o vencimento em qualquer prazo.
B) Todo caso omisso é resolvido exclusivamente pelo Presidente ou pela Ouvidoria.
C) Salvo disposição contrária, exclui-se o dia do início e inclui-se o do vencimento; o prazo inicia ou vence em dia de expediente normal, e os casos omissos são resolvidos pelo Plenário.
D) O prazo corre mesmo quando o termo inicial e o vencimento recaem em dia sem expediente, sem qualquer ajuste.

#### Extra Dia 5.14

Um profissional de Administração utiliza artifício enganoso para obter vantagem indevida, conduta do art. 6º, XVIII, do Código. Para pessoa física, a sanção-base prevista é:

A) suspensão de seis meses a um ano, acompanhada da multa aplicável e observadas as garantias processuais.
B) advertência oral sem registro e sem multa.
C) censura reservada, aplicada antes da defesa.
D) cancelamento automático e imediato, independentemente de trânsito em julgado.

#### Extra Dia 5.15

Sobre sanções, pessoa jurídica, multa e processo na RN CFA nº 671/2025, assinale a alternativa correta.

A) Suspensão e cancelamento aplicam-se da mesma forma a pessoa física e jurídica.
B) Advertência reservada é obrigatoriamente publicada no DOU, ao contrário da censura.
C) A multa substitui a sanção disciplinar, e ambas podem ser aplicadas antes do trânsito em julgado administrativo.
D) Suspensão e cancelamento não se aplicam à pessoa jurídica; a multa acompanha a sanção, e sanção somente pode ser aplicada após trânsito em julgado administrativo.

#### Extra Dia 5.16

Da frase “As reuniões podem ocorrer por videoconferência”, infere-se corretamente que:

A) toda reunião deve ocorrer remotamente.
B) a videoconferência é uma possibilidade, não uma obrigação universal.
C) nenhuma reunião pode ser presencial.
D) somente reuniões extraordinárias admitem videoconferência.

#### Extra Dia 5.17

Original: “Embora seja mediadora, a Ouvidoria não decide.” Assinale a reescrita que preserva o sentido.

A) Como decide, a Ouvidoria não é mediadora.
B) Se for mediadora, a Ouvidoria decidirá necessariamente.
C) A Ouvidoria é mediadora, mas não decide.
D) A Ouvidoria não decide; portanto, não pode mediar.

#### Extra Dia 5.18

Assinale a alternativa correta quanto à regência do pronome relativo e à crase.

A) “A Ouvidoria à qual o cidadão se dirigiu recebeu a manifestação.”
B) “A decisão que o usuário discordou foi revista.”
C) “A comissão cujos os membros foram eleitos reuniu-se.”
D) “O tema aonde a Comissão se manifestou exigia parecer.”

#### Extra Dia 5.19

Assinale a alternativa correta sobre o efeito das vírgulas.

A) Em “Os conselheiros que participaram da comissão votaram”, as vírgulas omitidas tornam a oração explicativa e abrangem necessariamente todos.
B) Orações restritivas e explicativas possuem sempre o mesmo alcance.
C) Inserir vírgulas jamais altera o conjunto referido pelo substantivo.
D) Sem vírgulas, a oração adjetiva pode selecionar um subconjunto; com vírgulas, pode apresentar explicação atribuída ao conjunto mencionado.

#### Extra Dia 5.20

Assinale a alternativa que mantém paralelismo e clareza.

A) A Ouvidoria deve receber manifestações, a análise e encaminhá-las.
B) A Ouvidoria deve receber manifestações, analisá-las e encaminhá-las.
C) A competência do Plenário é maior que a Diretoria nesse assunto.
D) O plano busca reduzir falhas, a aceleração das respostas e que dados sejam protegidos.

### Gabarito das questões extras do Dia 5

| Extra | Resposta |
|---:|:---:|
| 5.1 | C |
| 5.2 | A |
| 5.3 | D |
| 5.4 | B |
| 5.5 | C |
| 5.6 | A |
| 5.7 | D |
| 5.8 | B |
| 5.9 | C |
| 5.10 | A |
| 5.11 | D |
| 5.12 | B |
| 5.13 | C |
| 5.14 | A |
| 5.15 | D |
| 5.16 | B |
| 5.17 | C |
| 5.18 | A |
| 5.19 | D |
| 5.20 | B |

### Comentários das questões extras do Dia 5

#### Comentário Extra Dia 5.1

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A Retificação I adotou a RN nº 671/2025 como Código; a RN nº 651/2024 aprova o Regimento.
- **B)** Incorreta. Essas normas aparecem somente como contexto externo no bloco do Analista.
- **C)** Correta. A alternativa identifica as quatro bases materiais delimitadas para as extras.
- **D)** Incorreta. Lei, Decreto e Código também integram expressamente o escopo.

**Conceito:** delimitação normativa e controle de versão.

**Pegadinha:** usar norma de outro cargo ou trocar Regimento e Código.

**Como pensar:** fixe 4769, 61934, 651 e 671; as demais não fundamentam estas extras.

**Referência:** [Escopo e controle de versão](semana_02_estudo.md#s2-d5-rf-escopo).

#### Comentário Extra Dia 5.2

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A opção reúne natureza, autonomia, sede, jurisdição e o limite sistêmico.
- **B)** Incorreta. O CRA-PR não é associação privada nem possui jurisdição nacional.
- **C)** Incorreta. É autarquia com personalidade e jurisdição estadual.
- **D)** Incorreta. Autonomia não elimina diretrizes do CFA nem a aprovação federal do Regimento.

**Conceito:** natureza e jurisdição do CRA-PR.

**Pegadinha:** converter autonomia em soberania.

**Como pensar:** autonomia permite gestão própria dentro do Sistema e das competências legais.

**Referência:** [Regimento — órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos).

#### Comentário Extra Dia 5.3

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Tribunal de Contas e Ministério Público não integram a lista regimental de órgãos do CRA-PR.
- **B)** Incorreta. Assembleia Legislativa e Judiciário são externos ao Conselho.
- **C)** Incorreta. Secretaria estadual e conselho municipal não aparecem no art. 3º.
- **D)** Correta. A alternativa reproduz as cinco categorias regimentais.

**Conceito:** órgãos do CRA-PR.

**Pegadinha:** inserir instituição pública real, mas externa ao Conselho.

**Como pensar:** memorize Plenário, Diretoria, Ouvidoria, Comissões/GT e Representação.

**Referência:** [Regimento — art. 3º](semana_02_estudo.md#s2-d5-rf-regimento-orgaos).

#### Comentário Extra Dia 5.4

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O Plenário possui deliberação e julgamento.
- **B)** Correta. Essa é a função definida no art. 4º do Regimento.
- **C)** Incorreta. Ouvidoria não dirige o Plenário nem executa decisões.
- **D)** Incorreta. A última instância sistêmica recursal não pertence ao Regional.

**Conceito:** finalidade do Plenário.

**Pegadinha:** trocar primeira instância regional por última instância nacional.

**Como pensar:** Plenário decide no Regional; CFA ocupa a posição recursal prevista.

**Referência:** [Regimento — Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos).

#### Comentário Extra Dia 5.5

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde Plenário com Diretoria e altera mandato.
- **B)** Incorreta. Há suplentes e renovação parcial alternada.
- **C)** Correta. A opção reúne composição, renovação, duração e limite de reeleição.
- **D)** Incorreta. O mandato do Conselheiro é de quatro anos, com apenas uma reeleição.

**Conceito:** composição e mandato do Plenário.

**Pegadinha:** usar os dois anos da Diretoria para o mandato dos Conselheiros.

**Como pensar:** Plenário: nove, suplentes, quatro anos; renovação parcial a cada dois.

**Referência:** [Regimento — arts. 5º e 6º](semana_02_estudo.md#s2-d5-rf-regimento-orgaos).

#### Comentário Extra Dia 5.6

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aprovação de planos, eleições internas e primeira instância estão no art. 8º.
- **B)** Incorreta. Essa descrição aproxima-se da Ouvidoria, não do Plenário.
- **C)** Incorreta. A Diretoria exerce direção e gestão executiva.
- **D)** Incorreta. Instituição e homologação de Comissão/GT seguem competências distintas.

**Conceito:** competências do Plenário.

**Pegadinha:** atribuir ao órgão deliberativo toda execução cotidiana.

**Como pensar:** Plenário aprova e julga; Diretoria administra e encaminha.

**Referência:** [Regimento — competência do Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos).

#### Comentário Extra Dia 5.7

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Ouvidor e representantes não compõem a Diretoria desse modo.
- **B)** Incorreta. Essa quantidade se refere ao Plenário e seus suplentes.
- **C)** Incorreta. A composição não usa representação municipal.
- **D)** Correta. São as cinco funções previstas no art. 18.

**Conceito:** composição da Diretoria Executiva.

**Pegadinha:** misturar cargos de outros órgãos na Diretoria.

**Como pensar:** Presidente e Vice + três Diretorias temáticas.

**Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente).

#### Comentário Extra Dia 5.8

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A aprovação dos Planos pertence ao Plenário.
- **B)** Correta. A Diretoria analisa/encaminha e homologa Comissão/GT; o Plenário aprecia e aprova os Planos.
- **C)** Incorreta. A opção troca gestão executiva e mediação.
- **D)** Incorreta. São órgãos diferentes com competências próprias.

**Conceito:** Diretoria Executiva × Plenário.

**Pegadinha:** trocar `analisar e encaminhar` por `aprovar`.

**Como pensar:** acompanhe os verbos regimentais, não apenas o assunto do ato.

**Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente).

#### Comentário Extra Dia 5.9

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Representação, convocação e presidência são competências expressas.
- **B)** Incorreta. O Presidente não substitui o colegiado nem controla sozinho todas as decisões.
- **C)** Correta. A opção reúne atribuições e o caráter provisório do `ad referendum`.
- **D)** Incorreta. A providência urgente volta à apreciação competente.

**Conceito:** competências presidenciais e `ad referendum`.

**Pegadinha:** transformar decisão sujeita a confirmação em competência definitiva.

**Como pensar:** urgência antecipa a providência, não elimina o colegiado.

**Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente).

#### Comentário Extra Dia 5.10

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A opção sintetiza os arts. 30 a 33.
- **B)** Incorreta. A frequência e a possibilidade de videoconferência estão invertidas.
- **C)** Incorreta. Maioria absoluta considera o total de membros.
- **D)** Incorreta. Extraordinária exige justificativa e pauta e também pode decorrer de requerimento da maioria absoluta.

**Conceito:** reuniões e quórum.

**Pegadinha:** calcular maioria absoluta sobre os presentes.

**Como pensar:** separe total do órgão, presentes e votos efetivamente dados.

**Referência:** [Reuniões e quórum](semana_02_estudo.md#s2-d5-rf-reunioes).

#### Comentário Extra Dia 5.11

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Julgamento pertence ao Plenário, não à Ouvidoria.
- **B)** Incorreta. A unidade não possui caráter executivo ou administrativo.
- **C)** Incorreta. O Ouvidor é eleito entre Conselheiros Efetivos.
- **D)** Correta. A opção descreve escolha, finalidade e limites da Ouvidoria.

**Conceito:** Ouvidoria do CRA-PR.

**Pegadinha:** confundir encaminhar e acompanhar com decidir.

**Como pensar:** Ouvidoria é ponte de comunicação, não instância julgadora.

**Referência:** [Ouvidoria, Comissões e Grupos de Trabalho](semana_02_estudo.md#s2-d5-rf-ouvidoria-comissoes).

#### Comentário Extra Dia 5.12

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Permanentes têm, em regra, três membros, e Diretor não integra a Comissão de Análise de Contas.
- **B)** Correta. A alternativa distingue corretamente composição e duração das estruturas.
- **C)** Incorreta. Comissão Especial atende demanda específica e transitória.
- **D)** Incorreta. GT coleta dados e estuda tema; não julga definitivamente.

**Conceito:** Comissões e Grupos de Trabalho.

**Pegadinha:** aplicar o máximo de cinco das estruturas temporárias às Comissões Permanentes.

**Como pensar:** Permanente: três, salvo regra; Especial/GT: até cinco e prazo definido.

**Referência:** [Ouvidoria, Comissões e Grupos de Trabalho](semana_02_estudo.md#s2-d5-rf-ouvidoria-comissoes).

#### Comentário Extra Dia 5.13

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A regra geral faz exatamente o inverso.
- **B)** Incorreta. Casos omissos cabem ao Plenário.
- **C)** Correta. Reúne a contagem, expediente e competência para omissões.
- **D)** Incorreta. A norma considera dia de expediente normal para início e vencimento.

**Conceito:** contagem de prazo e casos omissos.

**Pegadinha:** inverter inclusão/exclusão dos termos ou atribuir omissão ao Presidente.

**Como pensar:** exclua início, inclua fim e confira expediente; omissão vai ao Plenário.

**Referência:** [Contagem de prazo e casos omissos](semana_02_estudo.md#s2-d5-rf-prazos-omissoes).

#### Comentário Extra Dia 5.14

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O inciso XVIII integra a faixa de suspensão de seis meses a um ano para pessoa física.
- **B)** Incorreta. Advertência é escrita e reservada, além de não corresponder a essa faixa.
- **C)** Incorreta. A censura é pública e não pode anteceder o processo.
- **D)** Incorreta. Cancelamento não é automático nem a sanção-base do inciso XVIII.

**Conceito:** catálogo de infrações e gradação.

**Pegadinha:** escolher sanção pela impressão subjetiva de gravidade.

**Como pensar:** localize primeiro o inciso; depois aplique a faixa dos arts. 19 a 22.

**Referência:** [Código — deveres e catálogo de infrações](semana_02_estudo.md#s2-d5-rf-etica-deveres-infracoes).

#### Comentário Extra Dia 5.15

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O art. 13, § 3º, exclui suspensão e cancelamento para PJ.
- **B)** Incorreta. Advertência é reservada; censura, suspensão e cancelamento aparecem na regra de publicação.
- **C)** Incorreta. Multa acompanha, não substitui, e o trânsito administrativo é exigido.
- **D)** Correta. A opção reúne limites subjetivos, cumulação e garantia processual.

**Conceito:** sanções, PF × PJ, multa e trânsito em julgado.

**Pegadinha:** deduzir que PJ fica fora do Código ou que multa é sanção substitutiva.

**Como pensar:** identifique sujeito, inciso, processo, sanção compatível e multa.

**Referência:** [Sanções, PF × PJ, multas e garantias](semana_02_estudo.md#s2-d5-rf-etica-sancoes).

#### Comentário Extra Dia 5.16

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. `Pode` não exprime dever universal.
- **B)** Correta. O verbo modal apresenta uma possibilidade.
- **C)** Incorreta. A frase não proíbe reuniões presenciais.
- **D)** Incorreta. Não há restrição expressa às extraordinárias.

**Conceito:** modalidade e alcance.

**Pegadinha:** trocar possibilidade por obrigação ou exclusividade.

**Como pensar:** preserve a força do verbo modal ao interpretar.

**Referência:** [Português — inferência e quantificadores](semana_02_estudo.md#s2-d5-rf-portugues).

#### Comentário Extra Dia 5.17

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Cria causa e afirma decisão, invertendo o original.
- **B)** Incorreta. Transforma concessão em condição e acrescenta necessidade.
- **C)** Correta. `Mas` preserva o contraste concessivo relevante.
- **D)** Incorreta. Conclusão e negação da mediação não existem no original.

**Conceito:** reescrita e relação concessiva/adversativa.

**Pegadinha:** manter palavras semelhantes e alterar a relação lógica.

**Como pensar:** compare negação, modalidade e valor do conector.

**Referência:** [Português — reescrita](semana_02_estudo.md#s2-d5-rf-portugues).

#### Comentário Extra Dia 5.18

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. `Dirigir-se a` exige preposição, que se funde com `a qual`.
- **B)** Incorreta. `Discordar` exige `de`: “de que”.
- **C)** Incorreta. `Cujo` não admite artigo depois.
- **D)** Incorreta. A regência pede “sobre o qual”; `aonde` indica movimento a lugar.

**Conceito:** regência do relativo e crase.

**Pegadinha:** omitir preposição exigida pelo verbo ou inserir artigo após `cujo`.

**Como pensar:** identifique a regência antes de escolher o pronome relativo.

**Referência:** [Português — regência do relativo e crase](semana_02_estudo.md#s2-d5-rf-portugues).

#### Comentário Extra Dia 5.19

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Sem vírgulas, a oração é restritiva e seleciona participantes.
- **B)** Incorreta. A pontuação pode alterar o conjunto abrangido.
- **C)** Incorreta. Vírgulas têm efeito sintático e semântico nesse contraste.
- **D)** Correta. A alternativa diferencia restrição de explicação.

**Conceito:** oração adjetiva restritiva × explicativa.

**Pegadinha:** tratar vírgula apenas como pausa respiratória.

**Como pensar:** retire a oração e verifique se ela seleciona parte do grupo ou comenta o conjunto.

**Referência:** [Português — pontuação e sentido](semana_02_estudo.md#s2-d5-rf-portugues).

#### Comentário Extra Dia 5.20

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Mistura infinitivo, substantivo e pronome sem paralelismo.
- **B)** Correta. Os três verbos no infinitivo coordenam ações equivalentes.
- **C)** Incorreta. Compara competência com órgão; seria “maior que a da Diretoria”.
- **D)** Incorreta. Mistura infinitivo, substantivo e oração desenvolvida.

**Conceito:** paralelismo e clareza comparativa.

**Pegadinha:** aceitar lista semanticamente próxima com formas sintáticas incompatíveis.

**Como pensar:** alinhe a forma de todos os itens coordenados e complete comparações.

**Referência:** [Português — paralelismo e clareza](semana_02_estudo.md#s2-d5-rf-portugues).

---

# Dia 6 — Revisão Integrada e Estudo de Caso

## Questões principais

### Questão 1

Em um enlace de 1 Gbit/s, a aplicação recebe 700 Mbit/s de dados úteis. A medida de 1 Gbit/s é largura de banda e a de 700 Mbit/s é:

A) latência.
B) jitter.
C) goodput.
D) perda.

### Questão 2

Sobre um switch Ethernet, assinale a correta.

A) Atua apenas como repetidor multiporta.
B) Encaminha sempre todos os quadros a todas as portas.
C) Elimina qualquer broadcast.
D) Aprende endereços MAC e separa domínios de colisão por porta.

### Questão 3

No encaminhamento de um pacote IPv4 por um roteador, normalmente:

A) o quadro de enlace é removido e outro é criado para o próximo enlace.
B) o segmento TCP vira obrigatoriamente datagrama UDP.
C) o endereço MAC de origem é mantido até o destino final.
D) a aplicação recebe diretamente os bits do enlace.

### Questão 4

Para `10.0.5.130/26`, a rede e o broadcast são, respectivamente:

A) `10.0.5.0` e `10.0.5.255`.
B) `10.0.5.64` e `10.0.5.127`.
C) `10.0.5.128` e `10.0.5.191`.
D) `10.0.5.130` e `10.0.5.192`.

### Questão 5

Um host IPv4 precisa alcançar endereço fora da própria sub-rede. Antes de transmitir, ele normalmente obtém por ARP o MAC:

A) do servidor remoto.
B) do DNS autoritativo.
C) do switch de acesso.
D) do gateway local.

### Questão 6

No IPv6, a descoberta de vizinhos é apoiada principalmente por:

A) broadcast ARP.
B) DNS recursivo.
C) TCP.
D) ICMPv6/Neighbor Discovery.

### Questão 7

Analise as assertivas sobre TCP e UDP.

I. TCP oferece confirmação e ordenação no transporte.
II. UDP fornece retransmissão nativa.
III. Uma aplicação sobre UDP pode implementar confiabilidade própria.

Está correto o que se afirma em:

A) I e III, apenas.
B) I e II, apenas.
C) II e III, apenas.
D) I, II e III.

### Questão 8

Um navegador usa HTTP/3 para acesso HTTPS. A associação usual é:

A) HTTP/3 sobre TCP/80.
B) HTTP/3 sem transporte.
C) HTTP/3 sobre QUIC, normalmente em UDP/443.
D) HTTP/3 sobre SMTP/25.

### Questão 9

Na inicialização IPv4 por DHCP, a sequência DORA corresponde a:

A) Discover, Offer, Request e ACK.
B) DNS, Offer, Route e ARP.
C) Deliver, Open, Resolve e Accept.
D) Discover, Order, Reply e Audit.

### Questão 10

Assinale a alternativa correta sobre DNS.

A) Atribui máscara e gateway ao cliente.
B) Resolve ou publica dados de nomes e pode usar UDP ou TCP.
C) Substitui TLS na autenticação de servidor.
D) Funciona somente por broadcast.

### Questão 11

Para enviar uma mensagem e manter cópia sincronizada no servidor, a combinação apropriada é:

A) SMTP para envio e IMAP para acesso à caixa.
B) POP3 para envio e SMTP para sincronização.
C) SNMP para envio e LDAP para leitura.
D) SFTP para envio e NTP para leitura.

### Questão 12

Qual associação está correta?

A) FTPS é SFTP com outro nome.
B) Telnet cifra o terminal por padrão.
C) SFTP transfere arquivos sobre SSH.
D) SSH é protocolo de recebimento de correio.

### Questão 13

Em uma inspeção de equipamentos, SNMP é usado principalmente para:

A) resolver nomes.
B) gerenciar e consultar objetos definidos em MIB/OID.
C) atribuir endereços IPv4.
D) cifrar tráfego web.

### Questão 14

NAT e PAT se distinguem porque PAT:

A) substitui o roteamento IP.
B) cifra todos os pacotes.
C) atua apenas em IPv6.
D) também traduz portas para multiplexar fluxos.

### Questão 15

Um log apresenta horários inconsistentes entre servidores. O serviço mais diretamente relacionado é:

A) NTP.
B) LDAP.
C) FTP.
D) ARP.

### Questão 16

Uma falha de validação explorável é uma vulnerabilidade; o agente capaz de explorá-la é uma ameaça; a combinação de probabilidade e impacto expressa:

A) disponibilidade.
B) auditoria.
C) risco.
D) não repúdio.

### Questão 17

Autenticação e autorização significam, respectivamente:

A) registrar evento e restaurar cópia.
B) provar identidade e verificar permissão para uma ação.
C) cifrar conteúdo e gerar hash.
D) detectar ataque e bloqueá-lo.

### Questão 18

Sobre sniffing, spoofing e ataque on-path, assinale a correta.

A) Sniffing necessariamente altera o conteúdo.
B) Spoofing é sinônimo de indisponibilidade.
C) On-path apenas mede latência.
D) Spoofing falsifica identidade; on-path pode interceptar e alterar tráfego.

### Questão 19

Uma equipe deseja detectar tráfego suspeito sem necessariamente interrompê-lo. O controle mais compatível é:

A) IDS.
B) IPS obrigatoriamente em linha.
C) RAID.
D) NAT.

### Questão 20

Ao publicar um portal acessível externamente, a arquitetura mais adequada é posicioná-lo:

A) na mesma VLAN dos bancos internos, sem filtros.
B) na DMZ, com regras estritas para os serviços internos necessários.
C) atrás de qualquer estação usuária.
D) fora de todo firewall.

### Questão 21

Uma VPN reduz o risco de interceptação no caminho, mas não garante que:

A) o túnel possa proteger tráfego entre extremos.
B) haja confidencialidade no canal configurado.
C) o endpoint remoto esteja sem malware ou autorizado a toda ação.
D) exista autenticação dos extremos conforme a configuração.

### Questão 22

Em criptografia, um hash é usado principalmente para:

A) confidencialidade reversível por chave.
B) produzir resumo de integridade, não recuperar o original.
C) encaminhar pacotes entre redes.
D) substituir certificado digital.

### Questão 23

Assinale a correta sobre assinatura digital.

A) É criada com a chave pública e verificada com a privada.
B) Oculta necessariamente todo o documento.
C) É criada com a chave privada e verificada com a pública.
D) É idêntica a uma senha compartilhada.

### Questão 24

O principal papel do TLS em HTTPS é:

A) proteger o canal entre cliente e servidor, conforme autenticação e configuração.
B) garantir que todo conteúdo publicado seja verdadeiro.
C) eliminar vulnerabilidades da aplicação.
D) substituir DNS e roteamento.

### Questão 25

Sobre WPA3-Personal, assinale a correta.

A) Dispensa senha forte e atualização do AP.
B) Usa apenas WEP.
C) Elimina toda necessidade de segmentação.
D) Usa SAE, mas configuração e credenciais continuam relevantes.

### Questão 26

Na resposta a incidente, a contenção tem por objetivo imediato:

A) apagar toda evidência.
B) limitar propagação e impacto antes da erradicação e recuperação.
C) restaurar sem investigar persistência.
D) publicar relatório antes de analisar.

### Questão 27

Com RPO de 30 minutos e incidente às 14h, o ponto recuperado deve ser, no máximo, de:

A) 12h.
B) 13h30.
C) 14h30.
D) qualquer horário, se houver RAID.

### Questão 28

Redundância e backup diferem porque:

A) redundância reduz interrupção; backup permite recuperar estado ou versões anteriores.
B) backup impede automaticamente indisponibilidade.
C) RAID substitui cópia externa versionada.
D) ambos têm exatamente a mesma finalidade.

### Questão 29

Concorrência é diferente de paralelismo porque concorrência:

A) exige sempre dois núcleos físicos.
B) nunca compartilha recursos.
C) pode ocorrer por intercalação sem execução simultânea real.
D) elimina condições de corrida.

### Questão 30

Uma condição de corrida ocorre quando:

A) a CPU entra em deadlock.
B) o resultado depende de intercalações não controladas sobre estado compartilhado.
C) uma thread termina antes das demais.
D) há apenas um processo no sistema.

### Questão 31

O mutex é apropriado quando se deseja:

A) permitir vários titulares simultâneos na seção crítica.
B) substituir toda estratégia de escalonamento.
C) armazenar mensagens persistentes.
D) exclusão mútua de uma seção crítica.

### Questão 32

No caso clássico de deadlock, as condições de Coffman devem:

A) coexistir.
B) ocorrer em momentos independentes.
C) ser substituídas por starvation.
D) ser ignoradas se houver semáforo.

### Questão 33

Starvation descreve situação em que:

A) nenhum participante pode avançar por espera circular.
B) um participante pode ser adiado indefinidamente, enquanto outros progridem.
C) todos os recursos são liberados automaticamente.
D) uma thread executa em paralelo.

### Questão 34

Em Round Robin, reduzir demais o quantum tende a:

A) eliminar todas as trocas de contexto.
B) tornar FCFS.
C) impedir preempção.
D) aumentar overhead de trocas de contexto.

### Questão 35

Polling e interrupção diferem porque:

A) polling consulta repetidamente; interrupção sinaliza a CPU quando necessário.
B) interrupção transfere dados sem CPU, como DMA.
C) polling cifra dispositivos.
D) ambos são sinônimos.

### Questão 36

O DMA contribui para desempenho ao:

A) eliminar a necessidade de memória.
B) permitir transferência de blocos com menor intervenção da CPU por unidade.
C) substituir drivers.
D) impedir interrupções.

### Questão 37

Journaling em sistema de arquivos serve principalmente para:

A) ser cópia externa histórica.
B) manter credenciais cifradas.
C) auxiliar recuperação de consistência após falha.
D) substituir permissões.

### Questão 38

Em Linux, a permissão `640` indica:

A) dono lê/escreve, grupo lê, outros não têm acesso.
B) todos leem e escrevem.
C) dono executa, grupo escreve, outros leem.
D) nenhuma permissão para o dono.

### Questão 39

No Windows, uma DACL é relevante para:

A) calcular CIDR.
B) armazenar rotas BGP.
C) definir ACEs de permissões e negações sobre objeto.
D) sincronizar relógio.

### Questão 40

Em um caso CRA, um portal deixa de responder, mas `ping` ao servidor funciona. A conclusão correta é:

A) a aplicação está necessariamente saudável.
B) o DNS está necessariamente correto.
C) o firewall está necessariamente aberto.
D) conectividade IP isolada não prova saúde do serviço ou da aplicação.

### Questão 41

Em uma investigação, logs com hora incorreta prejudicam principalmente:

A) correlação temporal de eventos.
B) cálculo de permissões NTFS.
C) tamanho de quadros Ethernet.
D) resolução ARP.

### Questão 42

Uma organização deve combinar segmentação, MFA, atualização e monitoramento porque:

A) um controle único elimina todo risco.
B) defesa em profundidade reduz dependência de uma única barreira.
C) IDS substitui autenticação.
D) VPN substitui correção de vulnerabilidades.

### Questão 43

Qual sequência descreve melhor um acesso web seguro após inicialização do cliente?

A) DNS, DHCP, SMTP, ARP, TLS.
B) DHCP, FTP, LDAP, NAT, HTTP.
C) DHCP, DNS, transporte, TLS e HTTP.
D) NTP, IMAP, ICMP, SSH e HTTP.

### Questão 44

Um proxy reverso normalmente representa:

A) clientes internos perante qualquer site externo.
B) somente o gateway IPv4.
C) agentes SNMP.
D) servidores publicados perante clientes.

### Questão 45

Sobre LDAP, assinale a correta.

A) É protocolo de acesso a serviços de diretório.
B) É mecanismo de tradução de portas.
C) É protocolo de transferência de arquivos.
D) É algoritmo de criptografia.

### Questão 46

Em um laudo técnico, afirmar que “porta 443 prova que o conteúdo é seguro” é incorreto porque:

A) HTTPS nunca usa 443.
B) a porta é convenção; segurança depende de protocolo, TLS, validação e endpoint.
C) TLS só existe em UDP.
D) DNS define a porta por criptografia.

### Questão 47

Assinale a situação que caracteriza mais diretamente indisponibilidade.

A) Alteração não autorizada de dado.
B) Divulgação de documento sigiloso.
C) Associação errada entre usuário e grupo.
D) DDoS que satura o enlace do órgão.

### Questão 48

Ao preservar uma imagem de disco antes de erradicar malware, a equipe prioriza:

A) autenticação.
B) compactação.
C) preservação de evidência para análise.
D) desfragmentação.

### Questão 49

Qual ação é de observação, e não de alteração de processo?

A) `taskkill`.
B) `Stop-Process`.
C) `kill`.
D) `Get-Process`.

### Questão 50

Considere a afirmação: “A restauração foi concluída; logo, o plano de continuidade foi validado.” Ela é insuficiente porque:

A) restauração nunca deve ser testada.
B) é preciso também validar integridade, dependências e funcionamento de negócio.
C) backup substitui qualquer teste.
D) RTO e RPO deixam de importar após a cópia.

## Questões extras de revisão fixa do Dia 6

#### Extra Dia 6.1

No trecho “A segmentação ajuda, mas não substitui MFA”, a ideia central é que:

A) MFA é dispensável.
B) controles são complementares.
C) segmentação impede todo ataque.
D) segurança é binária.

#### Extra Dia 6.2

De “UDP não retransmite nativamente” infere-se que:

A) UDP nunca pode transportar aplicação confiável.
B) toda perda é corrigida por TCP.
C) a aplicação pode implementar recuperação própria.
D) DNS substitui UDP.

#### Extra Dia 6.3

Em “Embora o host responda, o serviço falhou porque houve deadlock”, os conectores indicam:

A) concessão e causa.
B) causa e finalidade.
C) conclusão e oposição.
D) condição e explicação.

#### Extra Dia 6.4

Em “A analista informou à gerente que seu acesso expirou”, para eliminar ambiguidade deve-se:

A) retirar “seu”.
B) assumir o termo mais próximo.
C) usar plural.
D) explicitar “acesso da analista” ou “da gerente”.

#### Extra Dia 6.5

Da frase “o IDS pode alertar”, conclui-se que:

A) alerta é garantia universal de detecção.
B) IDS bloqueia sempre.
C) IDS substitui firewall.
D) alerta é possibilidade ou capacidade, não garantia universal de detecção.

#### Extra Dia 6.6

A reescrita que preserva “Ainda que o backup esteja íntegro, teste a restauração” é:

A) Backup íntegro proíbe teste.
B) Teste somente se houver corrupção.
C) Mesmo íntegro, o backup exige teste de restauração.
D) Testar torna o backup íntegro.

#### Extra Dia 6.7

Assinale a frase correta.

A) Haviam falhas e existe controles.
B) Havia falhas e existem controles.
C) Houveram falhas e existe controles.
D) Haviam falhas e existia controles.

#### Extra Dia 6.8

Assinale o emprego correto de regência e crase.

A) Obedeceu à política e começou à analisar registros.
B) Obedeceu a política e começou à analisar registros.
C) Referiu-se as regras e à todos.
D) Obedeceu à política e começou a analisar registros.

#### Extra Dia 6.9

Assinale a pontuação adequada.

A) Os administradores, revogaram credenciais.
B) A equipe preservou, registros essenciais.
C) Após a contenção, a equipe preservou os registros.
D) Os servidores vulneráveis, foram isolados.

#### Extra Dia 6.10

Há paralelismo adequado em:

A) Isolar hosts, a revogação de credenciais e preservar logs.
B) Isolar hosts, revogar credenciais e a preservação de logs.
C) Isolar hosts, que credenciais sejam revogadas e logs.
D) Isolar hosts, revogar credenciais e preservar logs.

#### Extra Dia 6.11

Em enlace de 1 Gbit/s, throughput de 700 Mbit/s e goodput de 620 Mbit/s, a variação do atraso é:

A) jitter.
B) largura de banda.
C) broadcast.
D) CIDR.

#### Extra Dia 6.12

Ao rotear para novo enlace Ethernet, o equipamento:

A) preserva o quadro origem intacto.
B) recria o quadro para o próximo enlace.
C) converte IP em DNS.
D) elimina o pacote IP.

#### Extra Dia 6.13

Para `192.168.10.77/27`, a rede é:

A) `192.168.10.0`.
B) `192.168.10.32`.
C) `192.168.10.64`.
D) `192.168.10.77`.

#### Extra Dia 6.14

Para destino IPv4 remoto, o host resolve por ARP o MAC:

A) do gateway local.
B) do destino remoto.
C) do DNS.
D) do NAT.

#### Extra Dia 6.15

DHCP, DNS, TLS e HTTP têm, respectivamente, funções de:

A) correio, arquivos, roteamento e tempo.
B) configuração, nomes, proteção do canal e aplicação web.
C) diretório, autenticação, backup e banco.
D) gerência, NAT, Wi-Fi e arquivo.

#### Extra Dia 6.16

Assinale a associação correta.

A) SMTP lê caixa; IMAP envia; SFTP é FTP sem cifra.
B) NTP entrega IP; SNMP resolve nomes.
C) SMTP envia; IMAP acessa caixa; SFTP usa SSH.
D) LDAP traduz portas; PAT lista diretórios.

#### Extra Dia 6.17

Uma falha explorável, código malicioso e probabilidade/impacto representam:

A) vulnerabilidade, ameaça e risco.
B) ativo, CIA e backup.
C) firewall, IDS e IPS.
D) evento, NTP e VPN.

#### Extra Dia 6.18

Assinale a correta.

A) Hash cifra reversivelmente.
B) IPS em linha pode bloquear, e HMAC usa chave secreta para integridade/autenticidade.
C) WPA3 dispensa senha forte.
D) VLAN substitui firewall.

#### Extra Dia 6.19

Com incidente às 14h, RPO 30 min e RTO 2h, é correto:

A) recuperar ponto não anterior a 13h30 e restabelecer até 2h.
B) RPO é prazo de serviço.
C) RTO é perda máxima de dados.
D) RAID substitui backup.

#### Extra Dia 6.20

Assinale a correta sobre SO.

A) DMA copia cada byte pela CPU e journaling é backup.
B) Deadlock e starvation são sinônimos.
C) Mutex permite todos na seção crítica.
D) Interrupção evita polling contínuo; DMA reduz intervenção; journaling auxilia consistência.

## Gabarito do Dia 6

### Questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | C |
| 2 | D |
| 3 | A |
| 4 | C |
| 5 | D |
| 6 | D |
| 7 | A |
| 8 | C |
| 9 | A |
| 10 | B |
| 11 | A |
| 12 | C |
| 13 | B |
| 14 | D |
| 15 | A |
| 16 | C |
| 17 | B |
| 18 | D |
| 19 | A |
| 20 | B |
| 21 | C |
| 22 | B |
| 23 | C |
| 24 | A |
| 25 | D |
| 26 | B |
| 27 | B |
| 28 | A |
| 29 | C |
| 30 | B |
| 31 | D |
| 32 | A |
| 33 | B |
| 34 | D |
| 35 | A |
| 36 | B |
| 37 | C |
| 38 | A |
| 39 | C |
| 40 | D |
| 41 | A |
| 42 | B |
| 43 | C |
| 44 | D |
| 45 | A |
| 46 | B |
| 47 | D |
| 48 | C |
| 49 | D |
| 50 | B |

### Questões extras

| Extra | Resposta |
|---:|:---:|
| 6.1 | B |
| 6.2 | C |
| 6.3 | A |
| 6.4 | D |
| 6.5 | D |
| 6.6 | C |
| 6.7 | B |
| 6.8 | D |
| 6.9 | C |
| 6.10 | D |
| 6.11 | A |
| 6.12 | B |
| 6.13 | C |
| 6.14 | A |
| 6.15 | B |
| 6.16 | C |
| 6.17 | A |
| 6.18 | B |
| 6.19 | A |
| 6.20 | D |


## Comentários do Dia 6

### Comentário da Questão 1

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Aplica a regra de métricas de rede exigida no cenário.
- **C)** Correta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** métricas de rede.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-01).

### Comentário da Questão 2

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de switch e domínios exigida no cenário.

**Conceito:** switch e domínios.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-01).

### Comentário da Questão 3

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de encapsulamento por salto exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** encapsulamento por salto.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-02).

### Comentário da Questão 4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de CIDR e broadcast exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** CIDR e broadcast.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-03).

### Comentário da Questão 5

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Aplica a regra de gateway e ARP exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** gateway e ARP.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-04).

### Comentário da Questão 6

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de IPv6 e ND exigida no cenário.

**Conceito:** IPv6 e ND.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-04).

### Comentário da Questão 7

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de TCP e UDP exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** TCP e UDP.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário da Questão 8

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de HTTP/3 e QUIC exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** HTTP/3 e QUIC.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário da Questão 9

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de DHCPv4 exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** DHCPv4.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário da Questão 10

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de DNS exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** DNS.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário da Questão 11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de correio eletrônico exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** correio eletrônico.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 12

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de SFTP e SSH exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** SFTP e SSH.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 13

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de SNMP exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** SNMP.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 14

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de NAT e PAT exigida no cenário.

**Conceito:** NAT e PAT.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 15

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de NTP exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** NTP.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 16

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de vulnerabilidade, ameaça e risco exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** vulnerabilidade, ameaça e risco.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-07).

### Comentário da Questão 17

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de AAA exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** AAA.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-07).

### Comentário da Questão 18

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de ataques de rede exigida no cenário.

**Conceito:** ataques de rede.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-07).

### Comentário da Questão 19

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de IDS exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** IDS.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 20

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de DMZ exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** DMZ.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 21

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de limites da VPN exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** limites da VPN.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 22

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de hash exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** hash.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 23

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de assinatura digital exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** assinatura digital.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 24

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de TLS exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** TLS.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 25

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de WPA3 exigida no cenário.

**Conceito:** WPA3.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 26

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de contenção exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** contenção.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

### Comentário da Questão 27

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de RPO exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** RPO.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

### Comentário da Questão 28

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de redundância e backup exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** redundância e backup.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

### Comentário da Questão 29

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de concorrência exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** concorrência.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 30

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de condição de corrida exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** condição de corrida.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 31

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de mutex exigida no cenário.

**Conceito:** mutex.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 32

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de deadlock exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** deadlock.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 33

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de starvation exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** starvation.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 34

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de Round Robin exigida no cenário.

**Conceito:** Round Robin.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 35

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de polling e interrupção exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** polling e interrupção.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 36

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de DMA exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** DMA.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 37

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de journaling exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** journaling.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 38

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de permissões Linux exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** permissões Linux.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 39

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de DACL exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** DACL.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 40

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de diagnóstico de serviço exigida no cenário.

**Conceito:** diagnóstico de serviço.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário da Questão 41

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de NTP e logs exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** NTP e logs.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 42

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de defesa em profundidade exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** defesa em profundidade.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário da Questão 43

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de fluxo web exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** fluxo web.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário da Questão 44

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de proxy reverso exigida no cenário.

**Conceito:** proxy reverso.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 45

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de LDAP exigida no cenário.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** LDAP.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário da Questão 46

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de porta e segurança exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** porta e segurança.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário da Questão 47

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de DDoS exigida no cenário.

**Conceito:** DDoS.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-07).

### Comentário da Questão 48

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Correta. Aplica a regra de evidência exigida no cenário.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** evidência.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

### Comentário da Questão 49

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Correta. Aplica a regra de comandos de observação exigida no cenário.

**Conceito:** comandos de observação.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

### Comentário da Questão 50

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **B)** Correta. Aplica a regra de validação de continuidade exigida no cenário.
- **C)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.
- **D)** Incorreta. Não preserva a regra ou a relação técnica indicada no enunciado.

**Conceito:** validação de continuidade.

**Pegadinha:** trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.

**Como pensar:** identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

## Comentários das questões extras do Dia 6

#### Comentário Extra Dia 6.1

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Correta. Mantém a regra de ideia central cobrada.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** ideia central.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-01).

#### Comentário Extra Dia 6.2

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Correta. Mantém a regra de inferência cobrada.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** inferência.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-02).

#### Comentário Extra Dia 6.3

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Mantém a regra de conectores cobrada.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** conectores.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-03).

#### Comentário Extra Dia 6.4

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Correta. Mantém a regra de ambiguidade cobrada.

**Conceito:** ambiguidade.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-04).

#### Comentário Extra Dia 6.5

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Transforma uma possibilidade em garantia universal.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Correta. Preserva o valor modal de possibilidade do IDS.

**Conceito:** modalidade.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-05).

#### Comentário Extra Dia 6.6

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Correta. Mantém a regra de reescrita cobrada.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** reescrita.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-06).

#### Comentário Extra Dia 6.7

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Correta. Mantém a regra de concordância cobrada.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** concordância.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-07).

#### Comentário Extra Dia 6.8

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não se usa crase antes de verbo no infinitivo.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Correta. Há regência de obedecer a e não há crase antes de “analisar”.

**Conceito:** crase.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-08).

#### Comentário Extra Dia 6.9

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Correta. Mantém a regra de pontuação cobrada.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** pontuação.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-09).

#### Comentário Extra Dia 6.10

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Mistura infinitivos com o substantivo “preservação”.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Correta. Coordena três verbos no infinitivo com a mesma função sintática.

**Conceito:** paralelismo.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-10).

#### Comentário Extra Dia 6.11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Mantém a regra de métricas cobrada.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** métricas.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-01).

#### Comentário Extra Dia 6.12

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Correta. Mantém a regra de encapsulamento cobrada.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** encapsulamento.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-02).

#### Comentário Extra Dia 6.13

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Correta. Mantém a regra de CIDR cobrada.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** CIDR.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-03).

#### Comentário Extra Dia 6.14

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Mantém a regra de gateway cobrada.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** gateway.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-04).

#### Comentário Extra Dia 6.15

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Correta. Mantém a regra de fluxo de protocolos cobrada.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** fluxo de protocolos.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

#### Comentário Extra Dia 6.16

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Correta. Mantém a regra de serviços de rede cobrada.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** serviços de rede.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

#### Comentário Extra Dia 6.17

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Mantém a regra de risco cobrada.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** risco.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-07).

#### Comentário Extra Dia 6.18

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Correta. Mantém a regra de controles cobrada.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** controles.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

#### Comentário Extra Dia 6.19

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Mantém a regra de RPO e RTO cobrada.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.

**Conceito:** RPO e RTO.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

#### Comentário Extra Dia 6.20

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **B)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **C)** Incorreta. Altera o sentido, a função ou o limite da regra aplicável.
- **D)** Correta. Mantém a regra de E/S e journaling cobrada.

**Conceito:** E/S e journaling.

**Pegadinha:** absolutizar, inverter a relação ou confundir conceitos próximos.

**Como pensar:** localize a regra decisiva e confira se a alternativa preserva sujeito, condição e alcance.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).
