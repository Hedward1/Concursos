# Apostila de Questões - Semana 2

## CRA-PR 2026 - Analista de Sistemas

Arquivo de questões para acompanhar a `semana_02_estudo.md`.

**Status:** Material aprovado para execução. A auditoria semântica e estrutural está registrada em `relatorio_aceite.md` e pode ser reproduzida com `python tools/audit_semana02.py`. A execução pelo candidato permanece pendente.

**Critério de autoria:** as 300 questões principais e as 120 extras são autorais e foram calibradas pelo perfil documentado do Instituto Consulplan. Nenhuma questão real foi reproduzida; o índice separado registra a busca e o grau de confirmação das amostras oficiais.

**Formato:** todas as questões têm quatro alternativas, de A) a D), e exatamente uma resposta correta, em conformidade com o edital do CRA-PR 2026.

**Total planejado:** 420 questões, sendo 300 principais (50 por dia) e 120 extras de revisão fixa (20 por dia).

**Nível:** 252 itens Médios, 156 Difíceis e 12 Muito difíceis, conforme o esforço cognitivo verificado individualmente, sem preenchimento artificial de cotas. Os formatos incluem conceito aplicado, cenário prático, assertivas, alternativa correta/incorreta, comparação, cálculo CIDR, análise de incidente e interpretação de comandos.

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
- O [índice de questões oficiais](../questoes_oficiais/semana_02.md) documenta a amostra comparável em acompanhamento e a ausência, nesta versão, do conjunto verificável de caderno, gabarito definitivo e situação dos recursos.

---

# Dia 1 — Redes: topologias, LAN/WAN e equipamentos

Base usada: `semana_02/semana_02_estudo.md`, seção `# Dia 1 - Redes: topologias, LAN/WAN e equipamentos`.

## Questões principais

### S2D1Q001 — Elementos fundamentais de redes e interligação de redes

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Conceitos fundamentais de redes](semana_02_estudo.md#s2-d1-fundamentos).

Em relação aos elementos fundamentais de uma rede de computadores, assinale a alternativa correta.

A) Nó designa o equipamento final que produz dados, excluindo switches e roteadores dessa classificação.
B) Host é equipamento intermediário que encaminha tráfego sem originar nem consumir comunicação.
C) Enlace é o conjunto de regras que define formato e sequência das mensagens trocadas entre aplicações.
D) Host é sistema final, interface o liga ao enlace e roteadores podem reunir redes em uma internetwork.

### S2D1Q002 — Distinção entre rede, Internet e Web

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Conceitos fundamentais de redes — Rede, Internet e Web](semana_02_estudo.md#s2-d1-fundamentos).

O serviço de correio eletrônico do CRA-PR permanece disponível, embora o portal institucional esteja indisponível. A situação é compatível com a afirmação de que:

A) a Web inclui correio, voz e transferência de arquivos, de modo que sua indisponibilidade alcançaria esses serviços.
B) a Internet corresponde à infraestrutura física, enquanto a Web corresponde à totalidade dos protocolos de rede.
C) a Web é um serviço de aplicação utilizado sobre a Internet, que também pode transportar correio, voz e arquivos.
D) Internet e Web são denominações equivalentes quando o acesso ocorre em uma rede pública.

### S2D1Q003 — Protocolo em comparação com serviço

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Conceitos fundamentais de redes](semana_02_estudo.md#s2-d1-fundamentos).

Assinale a alternativa que diferencia corretamente protocolo de serviço.

A) Protocolo descreve a capacidade entregue ao usuário, enquanto serviço especifica o formato e a sequência das mensagens no enlace.
B) Protocolo define regras de comunicação, enquanto serviço é uma capacidade oferecida a outra camada ou aplicação.
C) Serviço existe apenas na camada de aplicação, enquanto protocolo existe apenas nas camadas física e de enlace.
D) Protocolo e serviço tornam-se conceitos equivalentes quando os dispositivos utilizam a suíte TCP/IP.

### S2D1Q004 — Emissor, receptor, mensagem, meio e protocolo na comunicação de dados

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Comunicação de dados](semana_02_estudo.md#s2-d1-comunicacao-dados).

Duas estações foram conectadas por um enlace funcional, mas não conseguem trocar informações porque utilizam parâmetros incompatíveis. Considerando os elementos da comunicação de dados, assinale a alternativa correta.

A) A existência de um meio funcional torna o protocolo opcional quando emissor e receptor usam o mesmo tipo de equipamento.
B) Emissor e receptor são necessários apenas em full-duplex; em simplex, o meio assume uma dessas funções.
C) Mensagem e meio podem ser tratados como o mesmo elemento quando o conteúdo transmitido é digital.
D) Conectividade física não assegura comunicação quando protocolos ou parâmetros são incompatíveis.

### S2D1Q005 — Direção da comunicação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Comunicação de dados — Direção da comunicação](semana_02_estudo.md#s2-d1-comunicacao-dados).

Analise as associações a seguir.

I. Sensor que apenas envia medições: simplex.
II. Rádio comunicador em que os lados falam alternadamente: half-duplex.
III. Enlace Ethernet comutado em que os lados transmitem simultaneamente: full-duplex.

Está correto o que se afirma em:

A) I, II e III.
B) II e III, apenas.
C) I, apenas.
D) I e II, apenas.

### S2D1Q006 — Largura de banda, throughput e goodput

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

Um enlace possui capacidade nominal de 100 Mbit/s. Em uma janela de 10 segundos, foram transportados 900 Mbit, dos quais 720 Mbit correspondiam ao conteúdo útil recebido pela aplicação. Desconsidere variações dentro da janela. Assinale os valores de largura de banda, throughput e goodput, respectivamente.

A) 100 Mbit/s, 90 Mbit/s e 72 Mbit/s.
B) 90 Mbit/s, 100 Mbit/s e 72 Mbit/s.
C) 100 Mbit/s, 72 Mbit/s e 90 Mbit/s.
D) 90 Mbit/s, 72 Mbit/s e 100 Mbit/s.

### S2D1Q007 — Diferença entre vazão total e vazão útil

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

Durante a transferência de um arquivo, a aplicação recebe 480 MB úteis, enquanto a rede transporta também cabeçalhos, confirmações e retransmissões. Nesse contexto, assinale a alternativa correta.

A) Goodput inclui cabeçalhos e retransmissões, ao passo que throughput considera apenas o arquivo útil entregue.
B) Throughput corresponde à capacidade nominal do enlace, enquanto goodput corresponde a toda a taxa transmitida no meio.
C) Retransmissões bem-sucedidas integram o goodput porque, ao final, seus dados também alcançam o receptor.
D) Goodput corresponde à parcela útil percebida pela aplicação e tende a ser menor ou igual ao throughput.

### S2D1Q008 — Latência

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

Um sistema remoto responde de forma estável, mas cada interação leva cerca de 180 ms para percorrer o caminho e retornar. A medida diretamente associada a esse atraso é:

A) largura de banda.
B) latência.
C) goodput.
D) perda.

### S2D1Q009 — Jitter e perda em tráfego sensível a tempo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Comunicação de dados — Medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

Em uma chamada de voz, os pacotes chegam com intervalos muito variáveis e alguns não chegam ao destino. Assinale a descrição correta.

A) A variação dos intervalos é largura de banda, e a ausência de pacotes é goodput.
B) A variação dos intervalos é perda, e a ausência de pacotes é latência.
C) Jitter é variação da latência, enquanto perda é ausência de dados esperados.
D) Jitter e perda são sinônimos, pois ambos medem a capacidade nominal do enlace.

### S2D1Q010 — Topologia física em contraste com topologia lógica

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

Quatro computadores estão ligados individualmente a um hub central. Quanto às topologias física e lógica, essa rede apresenta:

A) estrela física e comportamento lógico de meio compartilhado semelhante a barramento.
B) malha física completa e estrela lógica com enlaces seletivos.
C) barramento físico e anel lógico com passagem obrigatória de token.
D) estrela física e lógica comutada, pois a presença de um equipamento central definiria ambos os comportamentos.

### S2D1Q011 — Organização e pontos de falha da topologia em estrela

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [3. Topologia física e topologia lógica — Estrela](semana_02_estudo.md#s2-d1-topologias).

Em uma topologia física em estrela, é correto afirmar que:

A) a falha de um enlace de acesso tende a afetar um nó; a do centro pode afetar a estrela inteira.
B) os nós compartilham um cabo linear principal, e o ponto central serve apenas para terminação.
C) cada nó mantém ligação direta com os demais, usando o equipamento central somente para redundância.
D) o tráfego deve percorrer um caminho fechado em um único sentido.

### S2D1Q012 — Reconhecimento comparado das topologias

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

Sobre as topologias de rede, assinale a alternativa INCORRETA.

A) Na estrela, os enlaces de acesso convergem para um ponto central.
B) No anel, os nós formam conceitualmente um caminho fechado.
C) No barramento, cada nó possui enlace exclusivo com um equipamento central.
D) A topologia híbrida combina duas ou mais organizações topológicas.

### S2D1Q013 — Topologia em anel

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [3. Topologia física e topologia lógica — Anel](semana_02_estudo.md#s2-d1-topologias).

Determinada tecnologia conecta conceitualmente cada nó ao seguinte, formando um caminho fechado, e pode empregar passagem de token para ordenar o acesso. Trata-se de topologia em:

A) topologia em barramento.
B) topologia em anel.
C) topologia em estrela.
D) topologia em árvore.

### S2D1Q014 — Número de enlaces em malha completa

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [3. Topologia física e topologia lógica — Malha](semana_02_estudo.md#s2-d1-topologias).

Um projeto possuía malha completa entre sete roteadores, com um enlace ponto a ponto para cada par. Após a remoção de exatamente um desses enlaces, sem criação de outro, assinale a quantidade de ligações diretas que permanece.

A) 14.
B) 18.
C) 20.
D) 21.

### S2D1Q015 — Malha completa e malha parcial

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [3. Topologia física e topologia lógica — Malha](semana_02_estudo.md#s2-d1-topologias).

Sobre malha completa e malha parcial, assinale a alternativa correta.

A) Na malha parcial, cada nó possui ligação direta com os demais, mas apenas um enlace fica ativo.
B) A malha parcial trabalha com caminho único e, por isso, dispensa mecanismos de encaminhamento.
C) A malha completa utiliza menos portas que uma estrela com a mesma quantidade de nós.
D) Na malha completa, todos os pares se ligam diretamente; na parcial, apenas alguns pares possuem ligação direta.

### S2D1Q016 — Combinação de topologias no acesso e no núcleo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [3. Topologia física e topologia lógica — Híbrida](semana_02_estudo.md#s2-d1-topologias), especialmente o trecho que define a topologia híbrida pela combinação de organizações distintas.

Em cada andar de um edifício, as estações formam uma estrela em torno de um switch de acesso. No núcleo, os switches centrais possuem enlaces redundantes organizados como malha parcial. Considerando a disposição física da rede como um todo, assinale a classificação correta.

A) Estrela, pois a existência de um switch por andar impede outra classificação para a rede completa.

B) Malha parcial, pois a redundância entre os switches centrais também transforma os acessos em malha.

C) Híbrida, pois combina estrelas nos andares com uma malha parcial entre os switches centrais.

D) Anel, pois qualquer caminho redundante entre switches centrais determina um circuito fechado único.

### S2D1Q017 — Independência relativa entre topologia física e lógica

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

Analise as afirmativas sobre topologia física e lógica.

I. Uma estrela física com hub pode apresentar meio lógico compartilhado.
II. A existência de um equipamento central prova que a circulação lógica é seletiva.
III. Implementações específicas podem apresentar anel lógico sem reproduzir exatamente um anel físico.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I, II e III.
D) I e III, apenas.

### S2D1Q018 — Rede de área pessoal

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

Um relógio inteligente troca dados diretamente com o celular de seu usuário por tecnologia de curto alcance. Esse conjunto exemplifica, tipicamente, uma:

A) WAN.
B) MAN.
C) LAN metropolitana.
D) PAN.

### S2D1Q019 — WLAN como LAN independente do acesso à Internet

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

Durante uma falha do provedor, estações associam-se ao AP, obtêm acesso à impressora da mesma VLAN e não alcançam destinos externos. Assinale o diagnóstico conceitualmente correto.

A) O acesso à impressora comprova a conectividade local e também confirma o funcionamento do enlace com o provedor.
B) A falha externa altera o escopo da WLAN para PAN enquanto os clientes permanecem associados ao mesmo AP.
C) O caminho local da WLAN pode funcionar sem Internet; o diagnóstico deve prosseguir no gateway, no enlace WAN ou no provedor.
D) A comunicação local demonstra que o AP roteou entre sub-redes, ainda que clientes e impressora estejam na mesma VLAN.

### S2D1Q020 — Rede de área metropolitana

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

Um conselho interliga três unidades localizadas em diferentes bairros da mesma região metropolitana por infraestrutura de operadora. Quanto ao escopo típico, essa rede é melhor caracterizada como:

A) PAN.
B) MAN.
C) LAN limitada a uma sala.
D) barramento, pois utiliza infraestrutura compartilhada.

### S2D1Q021 — Rede de longa distância

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

A sede de um órgão em Curitiba é interligada a unidades em estados distintos por redes de longa distância. A classificação mais adequada é:

A) WAN.
B) PAN.
C) WLAN, ainda que nenhum enlace seja sem fio.
D) MAN, porque pertencer a uma única organização prevalece sobre a distribuição entre estados.

### S2D1Q022 — Meios guiados e não guiados

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5. Meios guiados e não guiados](semana_02_estudo.md#s2-d1-meios).

Analise as afirmativas sobre meios de transmissão.

I. O par trançado é meio guiado.
II. A fibra continua sendo meio guiado, embora transporte luz.
III. A comunicação por rádio é meio não guiado.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I, II e III.
D) I e III, apenas.

### S2D1Q023 — Par trançado UTP e versões blindadas

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5. Meios guiados e não guiados — Par trançado](semana_02_estudo.md#s2-d1-meios).

Sobre cabos de par trançado UTP e versões blindadas, assinale a alternativa correta.

A) O trançamento elimina toda interferência eletromagnética, mesmo fora dos limites do padrão utilizado.
B) A blindagem torna irrelevantes o aterramento e a instalação, pois atua independentemente da continuidade do sistema de proteção.
C) Variantes blindadas podem reduzir interferência, mas exigem instalação e aterramento adequados; o cobre não se torna imune.
D) UTP é adequado apenas a redes half-duplex e não permite negociação de velocidade.

### S2D1Q024 — Seleção de meio por requisitos do cenário

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [5. Meios guiados e não guiados — Fibra óptica](semana_02_estudo.md#s2-d1-meios).

Um órgão precisa interligar dois prédios com alta capacidade, e o trajeto possui forte interferência eletromagnética. A solução tecnicamente mais coerente, desde que ópticas e distâncias sejam compatíveis, é:

A) cabo coaxial escolhido apenas por possuir blindagem, sem verificar alcance, capacidade ou compatibilidade das extremidades.
B) par trançado blindado escolhido sem avaliar distância e aterramento, pois a blindagem garantiria imunidade completa.
C) enlace Wi-Fi escolhido pela taxa nominal e pela intensidade do sinal, desconsiderando interferência e planejamento de canal.
D) fibra óptica projetada para o enlace, pois não conduz o sinal como corrente elétrica.

### S2D1Q025 — Fibra monomodo e multimodo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5. Meios guiados e não guiados — Fibra óptica](semana_02_estudo.md#s2-d1-meios).

A respeito de fibras monomodo e multimodo, assinale a alternativa correta.

A) Fibra multimodo é a opção indicada para longas distâncias, sem depender dos transceptores empregados.
B) Fibra monomodo utiliza vários modos de propagação e, por definição, limita-se a enlaces internos curtos.
C) Ambas conduzem sinais elétricos e, por isso, sofrem a mesma interferência de um cabo de cobre.
D) Monomodo favorece distâncias maiores; multimodo é comum em enlaces internos, conforme o projeto.

### S2D1Q026 — Cabo coaxial

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5. Meios guiados e não guiados — Cabo coaxial](semana_02_estudo.md#s2-d1-meios).

O meio guiado formado por condutor central, isolante e blindagem, historicamente empregado em formas de Ethernet em barramento, é o cabo:

A) cabo de fibra multimodo.
B) cabo coaxial blindado.
C) cabo de par trançado UTP.
D) cabo de fibra monomodo.

### S2D1Q027 — Desempenho de comunicação sem fio

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [5. Meios guiados e não guiados — Comunicação sem fio](semana_02_estudo.md#s2-d1-meios).

Em uma sala, os clientes exibem sinal Wi-Fi forte, mas a vazão é baixa nos horários de maior uso. A explicação tecnicamente adequada é:

A) Interferência, contenção e densidade de clientes podem reduzir o throughput mesmo com sinal forte.
B) Cada cliente recebe um canal exclusivo, razão pela qual a densidade de estações não reduz a vazão.
C) A distância explica a baixa vazão, enquanto canais, obstáculos e interferência não alteram o resultado.
D) A intensidade do sinal basta para inferir goodput máximo, tornando suspeita a medição de baixa vazão.

### S2D1Q028 — Placa ou interface de rede

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [6. Placa de rede](semana_02_estudo.md#s2-d1-nic).

Assinale a alternativa que apresenta uma função compatível com a placa de rede de um host.

A) Transmitir e receber quadros, usar MAC no enlace e negociar velocidade e duplex.
B) Selecionar as rotas IP da organização a partir de uma tabela mantida pela própria interface.
C) Traduzir protocolos de aplicação antes de encapsular os dados em quadros.
D) Separar os domínios de broadcast associados ao host sem exercer roteamento.

### S2D1Q029 — Multiplicidade de interfaces e alcance do endereço MAC

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [6. Placa de rede](semana_02_estudo.md#s2-d1-nic).

Um servidor possui duas interfaces físicas e uma interface virtual. A respeito dessas interfaces e de seus endereços, assinale a alternativa correta.

A) O servidor só pode ter um endereço MAC, pois o MAC identifica de forma absoluta o gabinete.
B) Cada interface pode ter endereçamento próprio; o MAC identifica a interface no enlace, não a pessoa.
C) Interfaces virtuais não participam de redes porque não correspondem a uma placa removível.
D) As interfaces de um mesmo servidor devem pertencer à mesma sub-rede e ao mesmo enlace.

### S2D1Q030 — Repetidor

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7. Repetidores e hubs — Repetidor](semana_02_estudo.md#s2-d1-repetidor-hub).

Um equipamento regenera o sinal para ampliar o alcance de um enlace compatível, sem aprender endereços MAC nem escolher rotas IP. Esse equipamento é um:

A) roteador.
B) gateway de aplicação.
C) switch de camada 3.
D) repetidor.

### S2D1Q031 — Funcionamento do hub Ethernet clássico

**Nível:** Médio

**Uso:** Revisão

**Referência:** [7. Repetidores e hubs — Hub](semana_02_estudo.md#s2-d1-repetidor-hub).

Sobre o hub Ethernet clássico, assinale a alternativa correta.

A) É repetidor multiporta que retransmite bits e mantém um meio compartilhado em half-duplex.
B) Aprende os endereços MAC de origem e encaminha unicast conhecido pela porta associada ao destino.
C) Separa domínios de broadcast por porta e executa roteamento entre eles.
D) Mantém uma tabela IP para selecionar o próximo salto de cada quadro.

### S2D1Q032 — Efeitos da troca de hub por switch

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Diferenças entre conceitos parecidos — Hub x switch](semana_02_estudo.md#s2-d1-diferencas).

Um setor substituiu um hub por um switch de camada 2 e manteve todos os dispositivos na mesma VLAN. Analise as afirmativas.

I. O switch isola os segmentos conectados às suas portas.
II. Unicast conhecido pode ser encaminhado seletivamente.
III. O switch de camada 2 cria um domínio de broadcast por porta, mesmo na mesma VLAN.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) III, apenas.
D) I e II, apenas.

### S2D1Q033 — Aprendizagem e decisão de uma bridge

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [8. Bridges e switches — Bridge](semana_02_estudo.md#s2-d1-bridge-switch).

Uma bridge recebe um quadro por determinado segmento. O procedimento compatível com sua operação é:

A) aprender o MAC de origem no segmento de entrada e filtrar, encaminhar ou inundar conforme o destino.
B) aprender o endereço IP de destino e descartar unicast cujo destino ainda não tenha sido aprendido.
C) regenerar os bits nas portas de saída sem examinar endereços de enlace.
D) substituir o endereço IP do pacote para permitir comunicação entre redes privadas e públicas.

### S2D1Q034 — Tratamento de unicast desconhecido

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

Um switch recebe um quadro unicast cujo MAC de destino ainda não consta de sua tabela. Todos os enlaces pertencem à mesma VLAN. O switch deve:

A) converter o quadro em broadcast, alterando o endereço MAC de destino para todos os bits iguais a 1.
B) aprender o MAC de origem e inundar o quadro pelas portas pertinentes, exceto a porta de entrada.
C) tratar o destino desconhecido como remoto e encaminhar o quadro ao roteador da VLAN.
D) manter o quadro retido até que o destino se registre por um protocolo de controle da tabela MAC.

### S2D1Q035 — Filtragem de quadro na própria porta de entrada

**Nível:** Médio

**Uso:** Revisão

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

Um switch recebe por uma porta um quadro cujo MAC de destino conhecido está associado à própria porta de entrada. A ação adequada é:

A) inundar o quadro em outras VLANs para confirmar a localização do destino.
B) encaminhar o quadro de volta pela mesma porta, duplicando sua entrega no segmento.
C) filtrar o quadro, pois não há motivo para devolvê-lo ao segmento de onde veio.
D) enviá-lo ao gateway padrão com base apenas na ausência de outra porta de saída.

### S2D1Q036 — Propagação de broadcast por switch de camada 2

**Nível:** Médio

**Uso:** Revisão

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

Ao receber um quadro de broadcast em uma porta de um switch de camada 2, sem filtros adicionais, o equipamento normalmente:

A) consulta a rota IP e encaminha o quadro para outra sub-rede.
B) inunda o quadro pelas portas pertinentes da mesma VLAN, exceto a de entrada.
C) entrega o quadro somente à porta que contém o MAC de destino em sua tabela.
D) descarta o quadro porque switches não encaminham broadcasts.

### S2D1Q037 — Segmentação por portas e ausência de colisões em full-duplex

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

Sobre portas de switch e colisões em Ethernet moderna, assinale a alternativa correta.

A) A ausência de colisões reúne as VLANs em um domínio de broadcast comum ao equipamento.
B) Portas na mesma VLAN compartilham o meio half-duplex e o domínio de colisão, como em um hub.
C) A porta isola o segmento; em full-duplex não há colisões, embora a contagem didática preserve essa segmentação.
D) Full-duplex permite transmissão em apenas um sentido por vez para prevenir colisões.

### S2D1Q038 — Diferença entre switch de camada 2 e switch multicamada

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

A respeito de switches de camada 2 e de camada 3, assinale a alternativa INCORRETA.

A) Um switch de camada 2 pode aprender MACs de origem e encaminhar quadros dentro da LAN.
B) Um switch de camada 2 pode rotear entre sub-redes depois de aprender o MAC do gateway, mesmo sem função de camada 3.
C) Um switch multicamada compatível pode rotear quando essa função está habilitada e configurada.
D) Desativar o roteamento de um switch multicamada não o transforma em hub; a comutação de camada 2 pode permanecer.

### S2D1Q039 — Encaminhamento IP entre redes

**Nível:** Médio

**Uso:** Revisão

**Referência:** [9. Roteadores, gateways e access points — Roteador](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

Uma estação envia dados a um servidor localizado em outra sub-rede. O equipamento responsável por selecionar o próximo salto com base no endereço IP e na tabela de rotas é o:

A) roteador.
B) hub.
C) repetidor.
D) access point em bridge.

### S2D1Q040 — Significados contextuais de gateway

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [9. Roteadores, gateways e access points — Gateway](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

O termo gateway aparece em dois documentos: no primeiro, indica o próximo salto usado por uma estação; no segundo, indica um sistema que traduz protocolos de aplicação. A conclusão correta é:

A) o segundo documento usa o termo de forma inadequada, pois gateway designa uma interface física de saída.
B) gateway e hub são equivalentes quando o equipamento possui mais de uma porta de comunicação.
C) gateway pertence à camada de enlace e não pode designar uma interface de roteador.
D) gateway é contextual: pode indicar próximo salto ou intermediário que traduz protocolos.

### S2D1Q041 — Access point em modo bridge

**Nível:** Médio

**Uso:** Simulado

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

Um access point corporativo opera em modo bridge e conecta clientes IEEE 802.11 à LAN Ethernet. Nessa situação, o AP:

A) precisa executar NAT e DHCP para permitir a associação das estações ao rádio.
B) assume a escolha de rotas entre as sub-redes alcançadas pela rede de distribuição.
C) retransmite outro sinal Wi-Fi e dispensa conexão à rede de distribuição.
D) integra as estações sem fio à rede de distribuição e não precisa exercer roteamento, NAT ou DHCP.

### S2D1Q042 — Relação entre AP, SSID, VLAN e domínio de broadcast

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

Estações sem fio associadas a um SSID e computadores cabeados pertencem à mesma VLAN. O AP opera em bridge. Analise as afirmativas.

I. Sem isolamento ou filtros, o AP pode estender o broadcast da VLAN aos clientes sem fio.
II. O nome do SSID cria, por si só, uma nova sub-rede e um novo domínio de broadcast.
III. Mapeamento para outra VLAN ou isolamento de clientes pode alterar o alcance da comunicação.

Está correto o que se afirma em:

A) I e III, apenas.
B) II, apenas.
C) I e II, apenas.
D) I, II e III.

### S2D1Q043 — Contenção e acesso ao meio sem fio

**Nível:** Médio

**Uso:** Simulado

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

Quanto ao acesso ao meio em redes Wi-Fi, assinale a alternativa correta.

A) Estações IEEE 802.11 utilizam CSMA/CD exatamente como um hub Ethernet e detectam colisões da mesma forma.
B) Cada estação recebe um meio físico exclusivo e, por isso, não existe contenção entre clientes do mesmo rádio.
C) O rádio é compartilhado e o acesso é associado didaticamente a CSMA/CA, não ao CSMA/CD do Ethernet legado.
D) A VLAN reserva intervalos exclusivos de transmissão e afasta a contenção no canal de rádio.

### S2D1Q044 — Equipamento doméstico multifuncional

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Exemplos práticos e resolvidos — Exemplo 5, equipamento doméstico multifuncional](semana_02_estudo.md#s2-d1-exemplos).

Um equipamento doméstico possui porta WAN, quatro portas LAN e rádio Wi-Fi, além de oferecer NAT e DHCP. Assinale a associação funcional INCORRETA.

A) As quatro portas LAN podem pertencer à função de switch integrada ao aparelho.
B) O access point realiza o NAT entre WAN e LAN, enquanto o roteador apenas controla o rádio.
C) A função de roteador pode interligar a rede LAN à interface WAN.
D) NAT e DHCP podem ser serviços adicionais do produto, sem definir isoladamente a função de access point.

### S2D1Q045 — Contagem de broadcast e ressalva do full-duplex

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [10. Domínio de colisão e domínio de broadcast — Exemplo de contagem](semana_02_estudo.md#s2-d1-dominios).

Seis computadores estão ligados diretamente a um switch, todos na VLAN 10, e uma sétima porta de acesso da VLAN 10 liga o switch a uma interface de roteador. Todos os enlaces operam em full-duplex. Assinale a alternativa correta.

A) Existem sete domínios de broadcast e um único enlace isolado pelo switch.
B) O switch passa a compartilhar um domínio de colisão entre os computadores porque pertencem à mesma VLAN.
C) Existe um domínio de broadcast, sete enlaces isolados e nenhuma colisão nos enlaces full-duplex.
D) Existem seis domínios de broadcast, pois a porta ligada ao roteador não participa da VLAN.

### S2D1Q046 — VLAN e roteamento inter-VLAN

**Nível:** Médio

**Uso:** Simulado

**Referência:** [10. Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios).

Três computadores foram colocados na VLAN 10 e outros três na VLAN 20, no mesmo switch. Para que os grupos se comuniquem entre si, é correto afirmar que:

A) permanece um único domínio de broadcast, e o switch de camada 2 encaminha entre VLANs sem função adicional.
B) existem dois domínios de broadcast, e a comunicação entre eles exige roteamento.
C) existem seis domínios de broadcast, um para cada porta de acesso.
D) a criação de VLANs segmenta os enlaces, mas preserva um domínio de broadcast comum aos grupos.

### S2D1Q047 — Contagem didática de segmentos de colisão e domínio de broadcast

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [10. Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios).

Em uma única VLAN, um switch conecta diretamente dois computadores, um roteador e um hub que atende três outros computadores. Para esta questão, adote a convenção didática tradicional: cada segmento isolado por uma porta do switch é contado como domínio de colisão, enquanto todos os equipamentos permanecem no mesmo domínio de broadcast. Assinale, respectivamente, as quantidades desses domínios.

A) 1 e 4.
B) 4 e 1.
C) 6 e 4.
D) 7 e 2.

### S2D1Q048 — VLAN, bridge sem fio, roteamento e contenção

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap) e [Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios), nos trechos sobre bridge, SSID/VLAN, roteamento e contenção Wi-Fi.

Um access point em bridge mapeia o SSID `Corporativo` para a VLAN 30 e o SSID `Visitantes` para a VLAN 40. Estações cabeadas também usam a VLAN 30, os enlaces Ethernet são full-duplex e uma política no roteador bloqueia o tráfego entre as duas VLANs. Analise as afirmações.

I. Sem isolamento ou filtro adicional, broadcasts de enlace do SSID `Corporativo` podem alcançar as estações cabeadas da VLAN 30.

II. A VLAN 40 forma outro domínio de broadcast, e a comunicação com a VLAN 30 depende de roteamento e de política que a autorize.

III. A contenção no rádio da VLAN 30 não deve ser descrita como colisão Ethernet; nos enlaces cabeados full-duplex não ocorrem colisões.

Está correto o que se afirma em:

A) I, II e III.

B) I e II, apenas.

C) I e III, apenas.

D) II e III, apenas.

### S2D1Q049 — Integração de broadcast cabeado e sem fio sem equiparar os meios

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [9. Roteadores, gateways e access points — Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

Um AP em bridge conecta clientes sem fio à mesma VLAN de estações cabeadas. Assinale a alternativa tecnicamente precisa.

A) O rádio constitui um domínio de colisão Ethernet idêntico ao de um hub e utiliza CSMA/CD.
B) O AP em bridge contém o broadcast na fronteira sem fio mesmo quando não há isolamento configurado.
C) A associação ao AP mapeia cada cliente para uma VLAN e uma sub-rede próprias.
D) O AP pode estender o broadcast da VLAN, mas contenção Wi-Fi não equivale à colisão Ethernet de um hub.

### S2D1Q050 — Internetwork e recurso compartilhado

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [1. Conceitos fundamentais de redes](semana_02_estudo.md#s2-d1-fundamentos).

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

- **Dia:** Dia 1

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** relação entre lei e decreto regulamentador.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Base legal e relação entre as normas](semana_02_estudo.md#s2-d1-revisao-base-legal), especialmente a função da Lei nº 4.769/1965, do Decreto nº 61.934/1967 e os limites das resoluções.

Ao explicar a base normativa do Sistema CFA/CRAs, um analista precisa distinguir a Lei nº 4.769/1965 do Decreto nº 61.934/1967. Assinale a alternativa correta.

A) A lei disciplina o exercício profissional e estabelece o sistema, enquanto o decreto detalha sua aplicação sem substituir a norma legal.

B) A lei disciplina apenas a rotina interna dos regionais, enquanto o decreto cria o exercício profissional e ocupa o lugar da norma legal.

C) A lei e o decreto possuem a mesma função normativa, de modo que o texto regulamentar posterior prevalece sempre que houver diferença.

D) A lei e o decreto tratam de matérias independentes, de modo que uma resolução do CFA pode afastar livremente os requisitos de ambos.

#### Extra Dia 1.2

- **Dia:** Dia 1

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** âmbito e função de CFA e CRA-PR.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra), na tabela de âmbito e função central de cada entidade.

Uma demanda envolve a orientação geral do Sistema CFA/CRAs e, depois, o registro e a fiscalização de atividade realizada no Paraná. A distribuição coerente de atribuições é:

A) O CRA-PR define a orientação nacional do sistema, e o CFA executa o registro e a fiscalização ordinária dentro do estado.

B) O CFA concentra orientação, registro e fiscalização no Paraná, e o CRA-PR atua apenas como unidade consultiva sem competência própria.

C) O CRA-PR realiza as duas etapas por o fato ocorrer no estado, e o CFA intervém somente como primeira instância dos processos regionais.

D) O CFA exerce orientação e disciplina nacionais, e o CRA-PR executa diretrizes, mantém registros e fiscaliza em sua jurisdição.

#### Extra Dia 1.3
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** natureza jurídica e autonomia do CRA-PR.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

De acordo com o Regimento aprovado pela RN CFA nº 651/2024, o CRA-PR é:

A) associação privada sem autonomia financeira, subordinada administrativamente ao governo estadual.
B) órgão integrante da Administração Direta federal, sem personalidade jurídica própria.
C) autarquia com personalidade jurídica de direito público e autonomia técnica, administrativa e financeira.
D) empresa pública estadual encarregada exclusivamente de arrecadar anuidades profissionais.
#### Extra Dia 1.4
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** sede e jurisdição do CRA-PR.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

Sobre sede e jurisdição do CRA-PR, assinale a alternativa correta.

A) Sua sede fica no Distrito Federal, e sua jurisdição alcança os estados da Região Sul.
B) Sua sede pode ser fixada em qualquer município, e sua jurisdição limita-se à respectiva comarca.
C) Sua sede está na capital do Paraná, e sua jurisdição abrange todo o estado do Paraná.
D) Sua sede é definida pelo governo estadual, e sua jurisdição é nacional para fins de fiscalização.
#### Extra Dia 1.5

- **Dia:** Dia 1

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** competências centrais do CRA-PR.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra), nos itens sobre execução de diretrizes, registros, fiscalização e julgamento regional.

O CRA-PR recebe notícia de possível exercício irregular no Paraná e precisa verificar a situação registral e a conduta profissional. Assinale a atuação compatível com seu âmbito regimental.

A) Encaminhar registro, fiscalização e julgamento diretamente ao CFA, pois o conselho regional exerce apenas orientação facultativa aos interessados.

B) Executar as diretrizes do CFA, consultar e manter os registros, fiscalizar a atividade e julgar a infração nos limites de sua jurisdição.

C) Suspender a diretriz nacional no Paraná e editar regra própria para todos os regionais antes de iniciar a apuração da atividade informada.

D) Conferir apenas o registro e remeter qualquer julgamento à Ouvidoria, pois o Plenário regional não atua como primeira instância.

#### Extra Dia 1.6

- **Dia:** Dia 1

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** órgãos e estruturas do CRA-PR.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra), especialmente o rol estrutural, a posição do Plenário e a natureza mediadora da Ouvidoria.

Ao montar um mapa da estrutura regimental do CRA-PR, a equipe também registra a função do Plenário e o limite da Ouvidoria. Assinale a alternativa integralmente correta.

A) Plenário, Diretoria Executiva, Ouvidoria, comissões e órgãos de representação integram a estrutura; o Plenário delibera e a Ouvidoria medeia.

B) A Diretoria Executiva julga em primeira instância, e a Ouvidoria executa suas decisões; o Plenário atua somente como canal de mediação.

C) O Plenário apenas aconselha a Diretoria, e a Ouvidoria decide reclamações; comissões e órgãos de representação ficam fora da estrutura.

D) Comissões e órgãos de representação integram a estrutura, mas o Plenário é instância nacional e a Ouvidoria aplica penalidades regionais.

#### Extra Dia 1.7
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** posição regimental do Plenário.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

No âmbito do CRA-PR, o Plenário é caracterizado como:

A) unidade de atendimento sem competência deliberativa ou de julgamento.
B) órgão consultivo externo que apenas recomenda decisões à Diretoria Executiva.
C) instância recursal nacional responsável por uniformizar decisões de todos os CRAs.
D) órgão colegiado de deliberação superior e primeira instância de julgamento em sua jurisdição.
#### Extra Dia 1.8
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** natureza e limites da Ouvidoria.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

A respeito da Ouvidoria do CRA-PR, assinale a alternativa correta.

A) Possui caráter executivo e pode substituir a Diretoria na prática de atos administrativos.
B) Exerce função mediadora e não possui caráter administrativo, executivo, deliberativo ou decisório.
C) Atua como primeira instância de julgamento disciplinar e aplica diretamente as penalidades.
D) Formula as diretrizes nacionais do sistema e revisa as normas expedidas pelo CFA.
#### Extra Dia 1.9
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** sujeitos alcançados pelo Código de Ética.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

Quanto ao alcance do Código de Ética aprovado pela RN CFA nº 671/2025, assinale a alternativa correta.

A) Alcança profissionais de Administração e pessoas jurídicas registradas, consideradas as especificidades destas.
B) Aplica-se apenas a pessoas físicas, pois pessoas jurídicas não se submetem a deveres ou sanções éticas.
C) Alcança qualquer empresa brasileira, ainda que sua atividade não se relacione ao sistema profissional.
D) Restringe-se aos conselheiros do CFA e dos CRAs durante o exercício de mandato eletivo.
#### Extra Dia 1.10

- **Dia:** Dia 1

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** deveres éticos dos profissionais de Administração.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica), nos deveres centrais e nas condutas de risco ético.

Quatro profissionais descrevem como conduzem seus serviços. Assinale a alternativa em que todas as práticas são compatíveis com os deveres éticos estudados.

A) Preserva o sigilo e busca aperfeiçoamento, mas empresta o registro a parceiro de confiança para viabilizar serviço que ele não pode exercer.

B) Mantém independência técnica e trata o cliente com zelo, mas assina relatório de terceiro sem orientação ou supervisão efetiva.

C) Colabora com o Sistema CFA/CRAs e trata seus representantes com urbanidade, mas retarda documentos solicitados para proteger o contratante.

D) Atua com zelo e honestidade, preserva o sigilo, mantém independência técnica, busca aperfeiçoamento e colabora com o sistema profissional.

#### Extra Dia 1.11
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** dever de sigilo profissional.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

Sobre o dever de sigilo profissional, assinale a alternativa correta.

A) O profissional pode divulgar informação sigilosa para obter vantagem, desde que não haja dano financeiro imediato.
B) O dever alcança apenas informação recebida por escrito e termina automaticamente com o contrato.
C) O profissional deve guardar informação conhecida em razão do exercício profissional lícito, ressalvada situação juridicamente justificável.
D) O sigilo impede o atendimento de qualquer obrigação legal ou determinação válida da autoridade competente.
#### Extra Dia 1.12
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** responsabilidade por documento assinado.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

Um profissional assina relatório preparado por terceiro sem ter orientado nem supervisionado efetivamente o trabalho. Segundo o núcleo ético estudado, essa conduta:

A) é regular quando o terceiro possui experiência prática, ainda que não haja supervisão.
B) é obrigatória para preservar a continuidade do serviço contratado.
C) representa conduta de risco ético por atribuir chancela profissional sem orientação ou supervisão efetiva.
D) produz apenas consequência contratual, sem possível repercussão perante o sistema profissional.
#### Extra Dia 1.13

- **Dia:** Dia 1

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** espécies de sanção ética.

- **Nível:** Médio

- **Uso:** Revisão

- **Referência:** [Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica), no rol de sanções e na explicação de que a multa acompanha as sanções nas condições normativas.

Assinale a alternativa que reproduz corretamente as quatro espécies de sanção apresentadas no Código de Ética estudado.

A) Advertência escrita e pública, censura reservada, suspensão do registro e cancelamento temporário do exercício profissional.

B) Advertência verbal e reservada, censura privada, suspensão do exercício e cancelamento temporário do registro profissional.

C) Advertência escrita e reservada, censura pública, multa isolada como sanção autônoma e suspensão do exercício profissional.

D) Advertência escrita e reservada, censura pública, suspensão do exercício e cancelamento do registro profissional.

#### Extra Dia 1.14
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** aplicação de sanções à pessoa jurídica.
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

Em relação às pessoas jurídicas registradas e às sanções éticas, assinale a alternativa correta.

A) Pessoas jurídicas não são alcançadas pelo Código e não podem receber medida ética ou multa.
B) Pessoas jurídicas recebem suspensão do exercício profissional nos mesmos termos aplicáveis à pessoa física.
C) Suspensão e cancelamento profissional não se aplicam à pessoa jurídica, que permanece sujeita às sanções compatíveis e à multa prevista.
D) A única consequência possível para pessoa jurídica é o cancelamento automático de sua inscrição, sem processo.
#### Extra Dia 1.15
- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** aplicação processual e pecuniária das sanções.
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

Em processo ético, a equipe identifica uma possível infração praticada por pessoa registrada. A conclusão adequada é:

A) escolher imediatamente a sanção mais grave, pois a gravidade percebida dispensa enquadramento normativo.
B) realizar o enquadramento e observar o processo e as regras aplicáveis, inclusive a disciplina da multa que acompanha as sanções.
C) arquivar o fato sempre que não houver prejuízo financeiro comprovado, independentemente da conduta.
D) aplicar apenas multa, porque o Código não prevê sanções disciplinares acompanhadas de consequência pecuniária.
#### Extra Dia 1.16
- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** leitura de comando negativo.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Revisão fixa de Português e interpretação — Comando da questão](semana_02_estudo.md#s2-d1-revisao-comando).

Um enunciado determina: “Assinale a alternativa INCORRETA”. Para responder adequadamente, o candidato deve:

A) marcar a primeira afirmação tecnicamente verdadeira e encerrar a leitura.
B) identificar a opção que contraria o texto ou a regra, tratando-a como a exceção pedida.
C) desconsiderar a palavra destacada e procurar a síntese do conteúdo estudado.
D) selecionar a alternativa mais abrangente, ainda que extrapole o comando.
#### Extra Dia 1.17
- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** inferência autorizada e extrapolação.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Revisão fixa de Português e interpretação — Inferência x extrapolação](semana_02_estudo.md#s2-d1-revisao-inferencia).

Leia o trecho: “A fibra reduz a exposição à interferência eletromagnética no enlace óptico, mas sua implantação exige componentes compatíveis.” Assinale a inferência autorizada.

A) A escolha da fibra não elimina a necessidade de projeto e de compatibilidade entre os componentes.
B) Toda instalação de fibra oferece maior velocidade que qualquer instalação de cobre.
C) A fibra dispensa transceptores, conectores e procedimentos de instalação.
D) A ausência de interferência eletromagnética garante menor custo de implantação.
#### Extra Dia 1.18

- **Dia:** Dia 1

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** relação semântica de conectores.

- **Nível:** Médio

- **Uso:** Simulado

- **Referência:** [Conectores](semana_02_estudo.md#s2-d1-revisao-conectores), na linha que associa “mas”, “porém” e “contudo” à oposição e à quebra de expectativa.

No período “O enlace permanece ativo; contudo, o serviço não responde às requisições”, o conector destacado estabelece relação de:

A) causa e explicação.

B) oposição e ressalva.

C) conclusão e consequência.

D) condição e hipótese.

#### Extra Dia 1.19
- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** efeito lógico de palavras absolutas.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Revisão fixa de Português e interpretação — Palavras absolutas](semana_02_estudo.md#s2-d1-revisao-absolutas).

Sobre palavras como “sempre”, “nunca”, “todos” e “necessariamente” em uma alternativa, assinale a orientação correta.

A) Elas ampliam o alcance da afirmação e exigem apoio integral do texto ou da regra, embora não sejam erradas por si mesmas.
B) Elas tornam a alternativa falsa em qualquer contexto, mesmo quando reproduzem literalmente uma regra sem exceção.
C) Elas devem ser ignoradas, pois não interferem no sentido nem no alcance da proposição.
D) Elas indicam conclusão lógica e podem substituir conectores como “portanto” e “logo”.
#### Extra Dia 1.20
- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** interpretação integrada de uma ressalva técnica.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Revisão fixa de Português e interpretação — Prática breve de interpretação](semana_02_estudo.md#s2-d1-revisao-pratica-interpretacao).

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
| 5 | A |
| 6 | A |
| 7 | D |
| 8 | B |
| 9 | C |
| 10 | A |
| 11 | A |
| 12 | C |
| 13 | B |
| 14 | C |
| 15 | D |
| 16 | C |
| 17 | D |
| 18 | D |
| 19 | C |
| 20 | B |
| 21 | A |
| 22 | C |
| 23 | C |
| 24 | D |
| 25 | D |
| 26 | B |
| 27 | A |
| 28 | A |
| 29 | B |
| 30 | D |
| 31 | A |
| 32 | D |
| 33 | A |
| 34 | B |
| 35 | C |
| 36 | B |
| 37 | C |
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
| 1.3 | C |
| 1.4 | C |
| 1.5 | B |
| 1.6 | A |
| 1.7 | D |
| 1.8 | B |
| 1.9 | A |
| 1.10 | D |
| 1.11 | C |
| 1.12 | C |
| 1.13 | D |
| 1.14 | C |
| 1.15 | B |
| 1.16 | B |
| 1.17 | A |
| 1.18 | B |
| 1.19 | A |
| 1.20 | C |

## Comentários do Dia 1

### Comentário S2D1Q001

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Switches e roteadores também são nós, embora normalmente não sejam hosts finais da comunicação analisada.
- **B)** Incorreta. Host é o sistema final que origina ou consome a comunicação, não o intermediário definido apenas pelo encaminhamento.
- **C)** Incorreta. Enlace é a conexão direta entre interfaces; as regras de formato e sequência pertencem ao protocolo.
- **D)** Correta. A alternativa relaciona adequadamente host, interface, enlace e internetwork.

**Conceito:** elementos fundamentais de redes e interligação de redes.

**Pegadinha:** trocar equipamento intermediário por host ou chamar protocolo de enlace físico.

**Como pensar:** separe o participante final, seu ponto de conexão, o caminho direto e o conjunto de redes interligadas.

**Referência:** [1. Conceitos fundamentais de redes](semana_02_estudo.md#s2-d1-fundamentos).

### Comentário S2D1Q002

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D1Q003

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D1Q004

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D1Q005

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Os exemplos representam, respectivamente, simplex, half-duplex e full-duplex.
- **B)** Incorreta. II e III são verdadeiras, porém a transmissão unilateral do sensor torna I verdadeira.
- **C)** Incorreta. A afirmativa I está correta, mas II e III também estão.
- **D)** Incorreta. I e II estão corretas, mas o enlace com transmissão simultânea valida III.

**Conceito:** direção da comunicação.

**Pegadinha:** confundir duplex com número de equipamentos, em vez de observar o sentido e a simultaneidade.

**Como pensar:** marque se há um sentido, dois sentidos alternados ou dois sentidos simultâneos.

**Referência:** [2. Comunicação de dados — Direção da comunicação](semana_02_estudo.md#s2-d1-comunicacao-dados).

### Comentário S2D1Q006

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D1Q007

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D1Q008

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D1Q009

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D1Q010

**Nível:** Difícil

**Uso:** Essenciais
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Os cabos convergem para o hub, formando estrela física, mas o hub mantém o meio lógico compartilhado.
- **B)** Incorreta. Não há ligação direta entre todos os pares, requisito da malha completa.
- **C)** Incorreta. O arranjo físico não é barramento e não há informação sobre token ou anel lógico.
- **D)** Incorreta. Um equipamento central pode ser hub ou switch; sua presença não prova comutação lógica.

**Conceito:** topologia física em contraste com topologia lógica.

**Pegadinha:** deduzir o comportamento da circulação apenas pelo desenho dos cabos.

**Como pensar:** identifique primeiro a disposição física e depois pergunte o que o equipamento central faz com o sinal ou quadro.

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

### Comentário S2D1Q011

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q012

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.** O comando solicita a alternativa **INCORRETA**.

**Análise das alternativas:**

- **A)** Correta quanto ao conteúdo. Convergência dos enlaces de acesso é característica da estrela.
- **B)** Correta quanto ao conteúdo. O anel forma conceitualmente um caminho fechado.
- **C)** Incorreta quanto ao conteúdo e, por isso, é o gabarito. Enlace exclusivo com equipamento central descreve estrela, não barramento.
- **D)** Correta quanto ao conteúdo. Uma topologia híbrida combina organizações distintas.

**Observação:** o comando pede a alternativa **INCORRETA**; por isso, C é o gabarito ao atribuir ao barramento uma característica da estrela.

**Conceito:** reconhecimento comparado das topologias.

**Pegadinha:** saber a matéria e marcar uma afirmação verdadeira sem observar o comando negativo.

**Como pensar:** transforme mentalmente o enunciado em “procuro a exceção” e teste cada descrição.

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

### Comentário S2D1Q013

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q014

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D1Q015

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Se cada nó se liga diretamente a todos, a malha é completa, não parcial.
- **B)** Incorreta. Redundância cria caminhos alternativos e não dispensa decisões de encaminhamento.
- **C)** Incorreta. Malha completa exige muito mais enlaces e portas que uma estrela, para quantidades usuais de nós.
- **D)** Correta. A diferença é a presença de ligação direta em todos os pares ou apenas em parte deles.

**Conceito:** malha completa e malha parcial.

**Pegadinha:** confundir “parcial” com enlace inativo em uma malha que fisicamente continua completa.

**Como pensar:** conte quais pares possuem ligação direta, sem considerar apenas o estado momentâneo do tráfego.

**Referência:** [3. Topologia física e topologia lógica — Malha](semana_02_estudo.md#s2-d1-topologias).

### Comentário S2D1Q016

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** os switches de acesso formam estrelas locais, mas essa classificação não representa a organização diferente existente no núcleo.
- **B)** a malha parcial descreve apenas o núcleo; ela não transforma os enlaces radiais dos andares em enlaces de malha.
- **C)** a rede reúne estrelas no acesso e malha parcial no núcleo, portanto sua organização física combina mais de uma topologia.
- **D)** redundância entre equipamentos não implica, por si só, um único caminho fechado que caracterize anel.

**Conceito:** topologia híbrida como combinação de duas ou mais organizações físicas na mesma rede.

**Pegadinha:** tomar a topologia de apenas uma parte do projeto como classificação suficiente para todo o conjunto.

**Como pensar:** divida o desenho em acesso e núcleo; se cada parte segue uma organização distinta, classifique o conjunto como híbrido.

**Referência:** [3. Topologia física e topologia lógica — Híbrida](semana_02_estudo.md#s2-d1-topologias), especialmente o trecho que define a topologia híbrida pela combinação de organizações distintas.

### Comentário S2D1Q017

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. I é verdadeira, mas III também descreve uma divergência possível entre físico e lógico.
- **B)** Incorreta. II é falsa: centro físico pode ser hub ou switch; III é verdadeira.
- **C)** Incorreta. A falsidade de II impede que as três estejam corretas.
- **D)** Correta. I e III são verdadeiras, enquanto II deduz indevidamente o comportamento lógico pelo centro.

**Conceito:** independência relativa entre topologia física e lógica.

**Pegadinha:** usar a existência de um ponto central como prova de encaminhamento seletivo.

**Como pensar:** para cada afirmativa, separe a forma dos enlaces do método de circulação e acesso ao meio.

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

### Comentário S2D1Q018

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q019

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Impressão local confirma parte da LAN, mas não comprova o enlace do provedor.
- **B)** Incorreta. Uma falha externa não altera o escopo da WLAN para PAN.
- **C)** Correta. O caminho local está operacional e a investigação deve avançar para gateway, WAN ou provedor.
- **D)** Incorreta. Comunicação na mesma VLAN pode ocorrer por bridging, sem roteamento do AP.

**Conceito:** WLAN como LAN independente do acesso à Internet.

**Pegadinha:** interpretar conectividade local bem-sucedida como prova de conectividade externa.

**Como pensar:** divida o percurso em associação sem fio, LAN/VLAN, gateway e enlace WAN; valide cada trecho.

**Referência:** [4. PAN, LAN, MAN e WAN](semana_02_estudo.md#s2-d1-alcance).

### Comentário S2D1Q020

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q021

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q022

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Afirmativa I é verdadeira, mas II e III também são.
- **B)** Incorreta. Excluir I não se justifica, pois o par trançado é meio guiado.
- **C)** Correta. Par trançado e fibra confinam o sinal a um meio físico; rádio se propaga pelo espaço.
- **D)** Incorreta. I e III são verdadeiras, mas a luz percorre a fibra, tornando II verdadeira.

**Conceito:** meios guiados e não guiados.

**Pegadinha:** classificar a fibra como não guiada apenas porque ela transporta luz.

**Como pensar:** pergunte se a energia segue um caminho físico delimitado ou se se propaga no espaço.

**Referência:** [5. Meios guiados e não guiados](semana_02_estudo.md#s2-d1-meios).

### Comentário S2D1Q023

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q024

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D1Q025

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Adequação a distância depende do tipo de fibra, ópticas e padrão; multimodo não é escolha automática para longas distâncias.
- **B)** Incorreta. Monomodo não utiliza vários modos e costuma ser associada a maiores alcances.
- **C)** Incorreta. Fibra transporta luz e é imune à interferência eletromagnética no enlace óptico.
- **D)** Correta. A comparação respeita os usos típicos e preserva a ressalva do projeto.

**Conceito:** fibra monomodo e multimodo.

**Pegadinha:** converter uma tendência de uso em regra universal independente dos transceptores.

**Como pensar:** nunca analise somente o núcleo; confirme padrão, óptica, velocidade e distância.

**Referência:** [5. Meios guiados e não guiados — Fibra óptica](semana_02_estudo.md#s2-d1-meios).

### Comentário S2D1Q026

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Fibra multimodo possui núcleo e revestimentos ópticos, não condutor central metálico.
- **B)** Correta. Condutor central, isolante e blindagem são a estrutura característica do coaxial.
- **C)** Incorreta. UTP utiliza pares de condutores trançados.
- **D)** Incorreta. Monomodo também é fibra óptica e não corresponde à descrição metálica.

**Conceito:** cabo coaxial.

**Pegadinha:** associar toda blindagem a par trançado blindado e esquecer a construção coaxial.

**Como pensar:** visualize a seção transversal: um eixo condutor central envolvido por isolante e blindagem.

**Referência:** [5. Meios guiados e não guiados — Cabo coaxial](semana_02_estudo.md#s2-d1-meios).

### Comentário S2D1Q027

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O conjunto dessas variáveis explica throughput baixo mesmo com sinal forte.
- **B)** Incorreta. Clientes do mesmo rádio disputam tempo no meio compartilhado.
- **C)** Incorreta. Canal, interferência, obstáculos e contenção alteram a vazão além da distância.
- **D)** Incorreta. Intensidade de sinal é apenas uma variável e não comprova goodput máximo.

**Conceito:** desempenho de comunicação sem fio.

**Pegadinha:** tratar barras de sinal como medição completa de capacidade e qualidade do canal.

**Como pensar:** diferencie cobertura de capacidade; investigue espectro, canal, densidade e ocupação do rádio.

**Referência:** [5. Meios guiados e não guiados — Comunicação sem fio](semana_02_estudo.md#s2-d1-meios).

### Comentário S2D1Q028

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q029

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q030

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D1Q031

**Nível:** Médio

**Uso:** Revisão
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

### Comentário S2D1Q032

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D1Q033

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D1Q034

**Nível:** Difícil

**Uso:** Revisão
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Inundar não altera o MAC de destino nem transforma o quadro em broadcast.
- **B)** Correta. O switch aprende a origem e inunda o unicast desconhecido nas portas pertinentes da VLAN, menos a entrada.
- **C)** Incorreta. Desconhecido na tabela MAC não significa que o destino pertença a outra rede.
- **D)** Incorreta. O switch não depende de registro manual do destino para tentar a entrega inicial.

**Conceito:** tratamento de unicast desconhecido.

**Pegadinha:** confundir o modo de entrega por inundação com a natureza do endereço de destino.

**Como pensar:** preserve o quadro e varie somente as portas de saída; a resposta futura permitirá aprender o destino.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário S2D1Q035

**Nível:** Médio

**Uso:** Revisão
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

### Comentário S2D1Q036

**Nível:** Médio

**Uso:** Revisão
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

### Comentário S2D1Q037

**Nível:** Difícil

**Uso:** Revisão
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Colisão e broadcast são domínios distintos; ausência da primeira não reúne VLANs.
- **B)** Incorreta. Mesma VLAN implica broadcast comum, não meio half-duplex comum entre portas do switch.
- **C)** Correta. A porta segmenta o enlace, mas full-duplex elimina colisões efetivas; a contagem por porta é ressalva didática.
- **D)** Incorreta. Full-duplex permite transmissão simultânea nos dois sentidos.

**Conceito:** segmentação por portas e ausência de colisões em full-duplex.

**Pegadinha:** repetir “uma colisão por porta” como ocorrência real em enlaces full-duplex modernos.

**Como pensar:** distinga capacidade de isolamento do segmento da existência efetiva de um meio sujeito a colisão.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário S2D1Q038

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: B.** O comando solicita a alternativa **INCORRETA**.

**Análise das alternativas:**

- **A)** Correta quanto ao conteúdo. Aprender MAC e encaminhar quadros são funções de camada 2.
- **B)** Incorreta quanto ao conteúdo e, portanto, é o gabarito. Aprender o MAC do gateway não concede função de roteamento a um switch de camada 2.
- **C)** Correta quanto ao conteúdo. Equipamento multicamada pode rotear quando compatível e configurado.
- **D)** Correta quanto ao conteúdo. Desabilitar a camada 3 não apaga necessariamente a comutação de camada 2.

**Observação:** o comando pede a alternativa **INCORRETA**; por isso, B é o gabarito ao confundir aprendizagem de MAC com roteamento.

**Conceito:** diferença entre switch de camada 2 e switch multicamada.

**Pegadinha:** confundir alcance do gateway aprendido em MAC com capacidade de consultar tabela de rotas.

**Como pensar:** confirme se o equipamento possui e exerce a função de camada 3; não a deduza da mera tabela MAC.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário S2D1Q039

**Nível:** Médio

**Uso:** Revisão
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

### Comentário S2D1Q040

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D1Q041

**Nível:** Médio

**Uso:** Simulado
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

### Comentário S2D1Q042

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D1Q043

**Nível:** Médio

**Uso:** Simulado
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

### Comentário S2D1Q044

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: B.** O comando solicita a associação **INCORRETA**.

**Análise das alternativas:**

- **A)** Correta quanto ao conteúdo. As portas LAN podem compor um switch interno.
- **B)** Incorreta quanto ao conteúdo e, portanto, é o gabarito. Roteador interliga WAN e LAN; access point fornece o acesso de rádio.
- **C)** Correta quanto ao conteúdo. A função de roteamento pode encaminhar entre as interfaces LAN e WAN.
- **D)** Correta quanto ao conteúdo. NAT e DHCP são serviços adicionais e não definem um AP isolado.

**Observação:** o comando pede a associação **INCORRETA**; por isso, B é o gabarito ao trocar as funções do roteador e do access point.

**Conceito:** equipamento doméstico multifuncional.

**Pegadinha:** atribuir a função ao gabinete inteiro sem separar seus componentes lógicos.

**Como pensar:** desenhe caixas internas para switch, roteador, AP, NAT, firewall e DHCP.

**Referência:** [Exemplos práticos e resolvidos — Exemplo 5, equipamento doméstico multifuncional](semana_02_estudo.md#s2-d1-exemplos).

### Comentário S2D1Q045

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D1Q046

**Nível:** Médio

**Uso:** Simulado
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

### Comentário S2D1Q047

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D1Q048

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** as três afirmações preservam, respectivamente, o alcance do broadcast na VLAN em bridge, a separação e o roteamento entre VLANs e a diferença entre contenção Wi-Fi e colisão Ethernet.
- **B)** I e II são verdadeiras, mas III também é; Wi-Fi compartilha tempo de transmissão sem se tornar um domínio de colisão Ethernet, e full-duplex elimina colisões nos enlaces cabeados.
- **C)** I e III são verdadeiras, mas II também é; VLANs diferentes separam broadcasts e precisam de roteamento autorizado para se comunicar.
- **D)** II e III são verdadeiras, mas I também é; o AP em bridge normalmente estende a VLAN 30 ao lado sem fio quando não há isolamento ou filtro.

**Conceito:** integração entre bridge do AP, VLAN, domínio de broadcast, roteamento e comportamento dos meios sem fio e cabeado.

**Pegadinha:** tratar SSID como fronteira automática, equiparar contenção Wi-Fi a colisão Ethernet ou imaginar que VLANs se comunicam apenas por estarem no mesmo equipamento.

**Como pensar:** resolva três fronteiras separadamente: qual VLAN o AP estende, onde termina o broadcast e que mecanismo rege o acesso ao meio em cada enlace.

**Referência:** [Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap) e [Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios), nos trechos sobre bridge, SSID/VLAN, roteamento e contenção Wi-Fi.
### Comentário S2D1Q049

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D1Q050

**Nível:** Difícil

**Uso:** Simulado
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

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** a lei fornece a disciplina legal do exercício e do sistema, e o decreto a regulamenta sem ocupar sua posição hierárquica.
- **B)** a alternativa reduz indevidamente o alcance da lei e atribui ao decreto a criação da base que ele apenas regulamenta.
- **C)** lei e decreto não exercem a mesma função, e um regulamento não prevalece sobre a lei por ser posterior.
- **D)** as normas se relacionam, e resolução do CFA deve respeitar lei e decreto, não afastá-los livremente.

**Conceito:** função da lei e do decreto regulamentador na base normativa do Sistema CFA/CRAs.

**Pegadinha:** inverter criação e regulamentação ou usar posterioridade para apagar a hierarquia normativa.

**Como pensar:** identifique primeiro a norma legal que estabelece a disciplina e depois o ato que detalha sua execução dentro desses limites.

**Referência:** [Base legal e relação entre as normas](semana_02_estudo.md#s2-d1-revisao-base-legal), especialmente a função da Lei nº 4.769/1965, do Decreto nº 61.934/1967 e os limites das resoluções.

#### Comentário Extra Dia 1.2

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** a formulação nacional pertence ao CFA, enquanto registro e fiscalização no Paraná integram a atuação regional.
- **B)** o CRA-PR não é mera unidade consultiva; ele possui atribuições de execução, registro, fiscalização e julgamento em sua jurisdição.
- **C)** a localização regional não transfere ao CRA-PR a orientação nacional, e o CFA não é primeira instância dos processos regionais.
- **D)** a alternativa preserva a divisão entre orientação e disciplina nacionais e execução regional das diretrizes do sistema.

**Conceito:** repartição funcional e territorial entre CFA e CRA-PR.

**Pegadinha:** confundir o alcance nacional da orientação com a execução concreta de registro e fiscalização no estado.

**Como pensar:** associe CFA ao plano nacional e CRA-PR à atuação executiva dentro da jurisdição paranaense.

**Referência:** [CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra), na tabela de âmbito e função central de cada entidade.

#### Comentário Extra Dia 1.3
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** Incorreta. O CRA-PR não é associação privada nem se subordina administrativamente ao governo estadual nos termos descritos.
- **B)** Incorreta. Autarquia possui personalidade jurídica e integra a Administração Indireta, não a Direta.
- **C)** Correta. A natureza autárquica, a personalidade de direito público e as três autonomias constam da revisão do Regimento.
- **D)** Incorreta. O CRA-PR não é empresa pública nem possui a finalidade exclusiva indicada.

**Conceito:** natureza jurídica e autonomia do CRA-PR.

**Pegadinha:** misturar autarquia, órgão sem personalidade e empresa pública.

**Como pensar:** verifique personalidade, regime jurídico e posição na estrutura administrativa antes de olhar a atividade desempenhada.

**Referência:** [Revisão fixa de Legislação CRA/CFA — CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra).

#### Comentário Extra Dia 1.4
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Essenciais

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

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** o CRA-PR exerce funções executivas próprias na jurisdição e não remete automaticamente toda atividade regional ao CFA.
- **B)** registro, fiscalização e julgamento de infrações regionais integram suas atribuições, sempre dentro das normas e dos limites legais.
- **C)** autonomia regional não autoriza suspender diretriz do CFA nem formular regra vinculante para os demais conselhos.
- **D)** a Ouvidoria não possui caráter decisório, e o Plenário atua como primeira instância de julgamento na jurisdição.

**Conceito:** competências executivas, registrais, fiscalizatórias e disciplinares do CRA-PR.

**Pegadinha:** converter autonomia em independência normativa nacional ou retirar do regional atribuições que o Regimento lhe confere.

**Como pensar:** mantenha a resposta no plano regional e verifique se cada verbo pertence ao rol de executar, registrar, fiscalizar e julgar.

**Referência:** [CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra), nos itens sobre execução de diretrizes, registros, fiscalização e julgamento regional.

#### Comentário Extra Dia 1.6

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** a opção reúne estruturas ensinadas e preserva a diferença entre deliberação colegiada e mediação sem caráter decisório.
- **B)** as funções foram deslocadas; Plenário e Ouvidoria não exercem os papéis descritos na alternativa.
- **C)** o Plenário possui deliberação superior, a Ouvidoria não decide e as estruturas mencionadas integram o desenho regimental.
- **D)** o Plenário pertence ao CRA-PR e atua regionalmente, enquanto a Ouvidoria não aplica penalidades.

**Conceito:** componentes da estrutura regimental e distinção funcional entre Plenário e Ouvidoria.

**Pegadinha:** reconhecer nomes corretos, mas aceitar funções decisórias ou territoriais trocadas.

**Como pensar:** confira primeiro se a estrutura pertence ao CRA-PR e depois se o verbo atribuído a cada órgão combina com deliberação ou mediação.

**Referência:** [CFA x CRA-PR](semana_02_estudo.md#s2-d1-revisao-cfa-cra), especialmente o rol estrutural, a posição do Plenário e a natureza mediadora da Ouvidoria.

#### Comentário Extra Dia 1.7
**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Aprofundamento

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

**Nível:** Médio

**Uso:** Aprofundamento

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

**Nível:** Médio

**Uso:** Aprofundamento

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

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** sigilo e aperfeiçoamento são deveres, mas emprestar registro para facilitar exercício irregular permanece conduta incompatível.
- **B)** independência e zelo não legitimam chancelar documento sem orientação ou supervisão técnica efetiva.
- **C)** colaboração e urbanidade não coexistem, nesse caso, com a obstrução deliberada da fiscalização por retenção de documentos.
- **D)** todas as práticas enumeradas pertencem ao núcleo de zelo, honestidade, sigilo, independência, atualização e colaboração.

**Conceito:** deveres éticos avaliados em conjunto com condutas que não são neutralizadas por comportamentos corretos.

**Pegadinha:** aceitar uma alternativa porque começa com dois deveres verdadeiros e ignorar a infração introduzida ao final.

**Como pensar:** teste todos os verbos da alternativa; em lista conjuntiva, uma única conduta incompatível elimina o conjunto.

**Referência:** [Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica), nos deveres centrais e nas condutas de risco ético.

#### Comentário Extra Dia 1.11
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** Incorreta. Vantagem própria não constitui autorização para divulgar informação protegida.
- **B)** Incorreta. O dever não depende apenas da forma escrita nem cessa automaticamente com o contrato.
- **C)** Correta. O sigilo alcança informação conhecida no exercício profissional lícito, sem afastar hipóteses juridicamente justificadas.
- **D)** Incorreta. Sigilo não impede, em termos absolutos, o cumprimento de obrigação legal válida.

**Conceito:** dever de sigilo profissional.

**Pegadinha:** transformar o dever em regra sem qualquer ressalva ou, no extremo oposto, liberá-lo por conveniência.

**Como pensar:** identifique a origem profissional da informação e procure justa causa ou fundamento jurídico para eventual revelação.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.12
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Revisão

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

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** inverte publicidade e reserva e altera as denominações de suspensão e cancelamento previstas no rol.
- **B)** o Código não apresenta advertência verbal nem censura privada, e os qualificadores temporais não reproduzem as espécies ensinadas.
- **C)** acerta advertência e censura, mas transforma a multa associada em espécie autônoma e omite o cancelamento.
- **D)** a sequência conserva advertência escrita e reservada, censura pública, suspensão do exercício e cancelamento do registro.

**Conceito:** espécies de sanção ética e posição da multa no regime estudado.

**Pegadinha:** trocar os qualificadores “reservada” e “pública” ou inserir a multa como quinta espécie disciplinar isolada.

**Como pensar:** confira nome e qualificador de cada degrau; depois verifique se multa foi indevidamente usada para substituir uma das quatro espécies.

**Referência:** [Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica), no rol de sanções e na explicação de que a multa acompanha as sanções nas condições normativas.

#### Comentário Extra Dia 1.14
**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Revisão

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
**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** Incorreta. Percepção de gravidade não elimina enquadramento, motivação e processo.
- **B)** Correta. Enquadramento, procedimento e disciplina da multa devem ser observados em conjunto.
- **C)** Incorreta. Ausência de prejuízo financeiro não torna irrelevante qualquer violação ética.
- **D)** Incorreta. A revisão prevê sanções disciplinares acompanhadas da multa nas condições normativas.

**Conceito:** aplicação processual e pecuniária das sanções.

**Pegadinha:** escolher a penalidade por intuição ou tratar a multa como substituta automática do regime disciplinar.

**Como pensar:** percorra fato, norma, enquadramento, processo e consequência, nessa ordem.

**Referência:** [Revisão fixa de Legislação CRA/CFA — Código de Ética vigente](semana_02_estudo.md#s2-d1-revisao-etica).

#### Comentário Extra Dia 1.16
**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. O comando pede a falsa, não a primeira afirmação verdadeira encontrada.
- **B)** Correta. “INCORRETA” inverte o critério e exige localizar a opção que foge à regra.
- **C)** Incorreta. Ignorar a palavra negativa leva a responder ao comando oposto.
- **D)** Incorreta. Abrangência não compensa extrapolação nem descumprimento do enunciado.

**Observação:** este item é metalinguístico: B é o gabarito porque descreve corretamente como interpretar um comando negativo; não se está escolhendo uma afirmação materialmente falsa neste próprio item.

**Conceito:** leitura de comando negativo.

**Pegadinha:** aqui a alternativa correta explica como procurar a incorreta; o próprio item não pede que se marque uma afirmação materialmente falsa.

**Como pensar:** circule a palavra negativa e reescreva: “qual opção é a exceção”.

**Referência:** [Revisão fixa de Português e interpretação — Comando da questão](semana_02_estudo.md#s2-d1-revisao-comando).

#### Comentário Extra Dia 1.17
**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

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

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** a indisponibilidade do serviço não é apresentada como causa explicativa de o enlace permanecer ativo.
- **B)** “contudo” contrapõe o estado do enlace ao resultado inesperado do serviço e introduz uma ressalva.
- **C)** a segunda oração não conclui logicamente a primeira; ela quebra a expectativa criada por ela.
- **D)** não há hipótese nem requisito do qual dependa a afirmação principal.

**Conceito:** relação adversativa expressa pelo conector “contudo”.

**Pegadinha:** interpretar a ordem das orações como causa ou conclusão e apagar a quebra de expectativa.

**Como pensar:** substitua “contudo” por “porém”; se o sentido se mantiver, a relação é de oposição ou ressalva.

**Referência:** [Conectores](semana_02_estudo.md#s2-d1-revisao-conectores), na linha que associa “mas”, “porém” e “contudo” à oposição e à quebra de expectativa.

#### Comentário Extra Dia 1.19
**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

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

**Nível:** Médio

**Uso:** Simulado

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

### S2D2Q051 — Ordem e organização funcional do modelo OSI

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Modelo OSI e suas sete camadas](semana_02_estudo.md#s2-d2-osi).

Da camada mais próxima do usuário para a camada responsável pela transmissão de sinais, a ordem correta das sete camadas do modelo OSI é:

A) Aplicação, Sessão, Apresentação, Rede, Transporte, Física e Enlace.
B) Aplicação, Apresentação, Transporte, Sessão, Rede, Física e Enlace.
C) Física, Enlace, Rede, Transporte, Sessão, Apresentação e Aplicação.
D) Aplicação, Apresentação, Sessão, Transporte, Rede, Enlace e Física.

### S2D2Q052 — Função da camada de Apresentação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Modelo OSI — Camada 6, Apresentação](semana_02_estudo.md#s2-d2-osi).

No modelo OSI, tradução de formatos, codificação, compressão e criptografia, em sentido funcional, são responsabilidades didaticamente associadas à camada de:

A) sessão.
B) apresentação.
C) transporte.
D) rede.

### S2D2Q053 — Distinção entre as funções das camadas de Transporte e Rede

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Modelo OSI — Camadas 4 e 3](semana_02_estudo.md#s2-d2-osi).

Analise as afirmativas sobre as camadas do modelo OSI.

I. A camada de transporte oferece comunicação fim a fim entre processos e pode empregar portas.
II. A camada de rede trata do endereçamento lógico e do encaminhamento entre redes.
III. A camada de rede garante, por si própria, confirmação e retransmissão fim a fim para todo pacote IP.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I, II e III.
D) I e II, apenas.

### S2D2Q054 — Atuação da camada Física e de repetidores

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Modelo OSI — Camada 1, Física](semana_02_estudo.md#s2-d2-osi).

Um repetidor recebe sinais em uma interface e os regenera em outra, sem examinar endereços. No modelo OSI, essa atuação pertence à camada física porque ela:

A) representa bits por sinais e não interpreta endereços MAC ou IP.
B) organiza quadros e aprende endereços MAC de origem.
C) estabelece sessões e pontos de sincronização entre aplicações.
D) seleciona rotas com base no endereço IP de destino.

### S2D2Q055 — Correspondência didática entre OSI e TCP/IP

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip).

Na comparação didática entre o OSI e o modelo TCP/IP de quatro camadas, assinale a alternativa correta.

A) As camadas de transporte e rede do OSI são reunidas na camada Internet do TCP/IP.
B) Aplicação, apresentação e sessão do OSI correspondem à camada de aplicação do TCP/IP.
C) A camada de enlace do OSI corresponde à camada de transporte do TCP/IP.
D) Física e enlace permanecem obrigatoriamente separadas no modelo TCP/IP de quatro camadas.

### S2D2Q056 — Variações didáticas de quatro e cinco camadas do TCP/IP

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip).

Alguns livros apresentam a arquitetura TCP/IP em cinco camadas, separando física e enlace, enquanto outros a apresentam em quatro. Essa diferença significa que:

A) a versão de cinco camadas abandona os protocolos IP, TCP e UDP.
B) o modelo de quatro camadas não contempla meios físicos nem redes locais.
C) a suíte permanece a mesma; muda a forma pedagógica de agrupar as funções.
D) a versão de cinco camadas passa a ter correspondência perfeita com as sete camadas do OSI.

### S2D2Q057 — Encapsulamento descendente no emissor

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [3. Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento).

Em uma comunicação que usa TCP, IP e Ethernet, qual sequência representa corretamente o encapsulamento no emissor?

A) Dados → pacote IP → segmento TCP → quadro Ethernet → bits.
B) Dados → segmento TCP → pacote IP → quadro Ethernet → bits.
C) Dados → quadro Ethernet → pacote IP → segmento TCP → bits.
D) Dados → segmento TCP → quadro Ethernet → pacote IP → bits.

### S2D2Q058 — Desencapsulamento ascendente no receptor

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [3. Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento).

No receptor de uma comunicação Ethernet, IPv4 e TCP, o desencapsulamento ocorre, de forma simplificada, na seguinte ordem:

A) bits → segmento TCP → quadro Ethernet → pacote IPv4 → dados.
B) pacote IPv4 → quadro Ethernet → bits → dados → segmento TCP.
C) quadro Ethernet → bits → segmento TCP → pacote IPv4 → dados.
D) bits → quadro Ethernet → pacote IPv4 → segmento TCP → dados.

### S2D2Q059 — Campos que permanecem ou mudam a cada salto

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [3. Encapsulamento — O que muda a cada salto](semana_02_estudo.md#s2-d2-encapsulamento).

Uma estação envia um pacote IPv4 a um servidor remoto por meio de dois roteadores, sem NAT. Durante o percurso:

A) os endereços MAC são adequados a cada enlace, os endereços IP normalmente permanecem de ponta a ponta e o TTL pode ser alterado.
B) o endereço MAC do servidor permanece como destino de todos os quadros, e os roteadores substituem o IP de destino a cada salto.
C) os endereços IP mudam em todo roteador, enquanto os endereços MAC permanecem inalterados até o servidor.
D) endereços MAC e IP permanecem necessariamente idênticos, pois ambos identificam o destino final.

### S2D2Q060 — Nomenclatura específica das PDUs

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [4. PDUs](semana_02_estudo.md#s2-d2-pdus).

Assinale a associação correta entre protocolo ou camada e sua PDU didática.

A) TCP — segmento; IP — pacote ou datagrama; Ethernet — quadro; física — bits.
B) TCP — quadro; IP — segmento; Ethernet — pacote; física — dados.
C) TCP — pacote; IP — quadro; Ethernet — datagrama UDP; física — segmento.
D) TCP — bits; IP — dados; Ethernet — segmento; física — pacote.

### S2D2Q061 — Encapsulamento entre UDP e IP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [4. PDUs](semana_02_estudo.md#s2-d2-pdus), especialmente a tabela que associa o datagrama UDP ao Transporte e o datagrama IP à camada Rede/Internet.

Ao analisar uma transmissão, um técnico identifica um datagrama UDP dentro de um datagrama IPv4. Considerando a camada de cada protocolo e a ordem de encapsulamento, assinale a alternativa correta.

A) O datagrama UDP e o datagrama IP são PDUs da camada Internet e diferem apenas pelos campos de controle.

B) O datagrama UDP é uma PDU da Aplicação e encapsula o datagrama IP antes da transmissão pelo enlace.

C) O datagrama UDP é uma PDU do Transporte e fica encapsulado como carga útil no datagrama IP.

D) O datagrama IP é uma PDU do Transporte e fica encapsulado no datagrama UDP durante o envio.

### S2D2Q062 — Formato, escopo e administração do endereço MAC

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5. Endereço MAC](semana_02_estudo.md#s2-d2-mac).

Em relação aos endereços MAC usados em redes IEEE 802, assinale a alternativa correta.

A) Identificam processos de aplicação e são representados por números de porta de 16 bits.
B) Permanecem como origem e destino em todos os enlaces atravessados por um pacote, mesmo após roteamento.
C) Endereços de 48 bits, escritos em seis octetos hexadecimais, são comuns, mas podem ser localmente administrados ou mutáveis.
D) Substituem o endereço IP porque são necessariamente globais, únicos e imutáveis.

### S2D2Q063 — Aprendizagem da origem pelo switch

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5. Endereço MAC](semana_02_estudo.md#s2-d2-mac), no item que estabelece que switches aprendem o MAC de origem observado na porta de entrada.

A tabela MAC de um switch está vazia. Pela porta 5, chega um quadro com MAC de origem `AA-AA-AA-AA-AA-AA` e MAC de destino `BB-BB-BB-BB-BB-BB`. Independentemente de o destino ser localizado depois, qual registro o switch pode aprender com essa chegada?

A) O MAC de destino associado à porta 5, pois esse campo indica por onde o quadro entrou no switch.

B) O MAC de origem associado à porta de saída, definida depois da consulta ao endereço de destino.

C) Os MACs de origem e destino associados à porta 5, pois ambos aparecem no quadro recebido.

D) O MAC de origem associado à porta 5, pois essa é a localização observada para o emissor.

### S2D2Q064 — Tamanho e divisão lógica do endereço IPv4

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [6. IPv4](semana_02_estudo.md#s2-d2-ipv4).

Um endereço IPv4 possui:

A) 48 bits, divididos obrigatoriamente em 24 bits de rede e 24 de host.
B) 32 bits, e o prefixo informa quantos bits iniciais pertencem à parte de rede.
C) 64 bits, dos quais os quatro primeiros octetos identificam a rede.
D) 128 bits, representados por oito grupos hexadecimais.

### S2D2Q065 — Conversão de máscara decimal para prefixo CIDR

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

A máscara IPv4 `255.255.252.0` corresponde ao prefixo:

A) `/22`.
B) `/21`.
C) `/20`.
D) `/23`.

### S2D2Q066 — Conversão de prefixo CIDR para máscara decimal

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

Qual máscara decimal pontuada corresponde ao prefixo IPv4 `/20`?

A) `255.255.224.0`.
B) `255.255.248.0`.
C) `255.255.255.240`.
D) `255.255.240.0`.

### S2D2Q067 — Contiguidade dos bits da máscara CIDR IPv4

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

Assinale a sequência que NÃO representa uma máscara CIDR IPv4 normal, pois contém bits `1` não contíguos.

A) `255.255.255.192`.
B) `255.255.240.128`.
C) `255.248.0.0`.
D) `255.255.254.0`.

### S2D2Q068 — Cálculo de rede e broadcast pelo tamanho do bloco

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

Para o host `192.168.40.158/26`, os endereços de rede e de broadcast dirigido da sub-rede são, respectivamente:

A) `192.168.40.64` e `192.168.40.191`.
B) `192.168.40.128` e `192.168.40.190`.
C) `192.168.40.128` e `192.168.40.191`.
D) `192.168.40.152` e `192.168.40.159`.

### S2D2Q069 — Determinação da faixa de hosts em uma sub-rede `/27`

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [9. Exemplos de IPv4 e CIDR — Bloco /27](semana_02_estudo.md#s2-d2-calculos).

O endereço `10.12.7.222/27` pertence a uma sub-rede cuja faixa convencional de hosts válidos é:

A) `10.12.7.192` a `10.12.7.223`.
B) `10.12.7.193` a `10.12.7.222`.
C) `10.12.7.193` a `10.12.7.223`.
D) `10.12.7.201` a `10.12.7.230`.

### S2D2Q070 — Cálculo de rede e broadcast quando a fronteira está no terceiro octeto

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [9. Exemplos de IPv4 e CIDR — Prefixo no terceiro octeto](semana_02_estudo.md#s2-d2-calculos).

Considere o endereço `172.20.173.44/20`. Os endereços de rede e de broadcast dirigido são:

A) `172.20.160.0` e `172.20.191.255`.
B) `172.20.168.0` e `172.20.175.255`.
C) `172.20.173.0` e `172.20.173.255`.
D) `172.20.160.0` e `172.20.175.255`.

### S2D2Q071 — Quantidade convencional de hosts pelo prefixo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [8. Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

Quantos endereços IPv4 de host são convencionalmente utilizáveis em uma sub-rede `/28`?

A) 8.
B) 12.
C) 14.
D) 16.

### S2D2Q072 — Exceção do prefixo `/31` em enlace IPv4 ponto a ponto

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [9. Exemplos de IPv4 e CIDR — /31 ponto a ponto](semana_02_estudo.md#s2-d2-calculos).

O bloco `10.0.0.10/31` é empregado em um enlace IPv4 ponto a ponto compatível com a RFC 3021. Nesse contexto:

A) `10.0.0.10` e `10.0.0.11` podem representar as duas extremidades do enlace.
B) nenhum dos endereços pode ser usado, pois a fórmula `2^h - 2` resulta em zero.
C) apenas `10.0.0.10` pode ser usado, porque `10.0.0.11` é sempre broadcast.
D) o prefixo deve ser interpretado como uma rota para um único host.

### S2D2Q073 — Rota de host IPv4 com prefixo `/32`

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [9. Exemplos de IPv4 e CIDR — /32](semana_02_estudo.md#s2-d2-calculos), especificamente o Exemplo F, que define `/32` como um endereço único ou rota de host.

Uma tabela de roteamento contém a entrada `203.0.113.9/32`. No contexto de roteamento IPv4, qual conjunto de destinos essa entrada representa?

A) Somente `203.0.113.9`, pois os 32 bits foram fixados e a entrada funciona como rota de host.

B) Os endereços `203.0.113.8` e `.9`, pois o último bit permanece disponível para duas extremidades.

C) O bloco de `203.0.113.0` a `.255`, pois `/32` informa apenas o tamanho total do endereço IPv4.

D) Uma sub-rede com rede `.9` e broadcast `.10`, pois dois endereços são reservados em qualquer prefixo.

### S2D2Q074 — Limites dos blocos privados RFC 1918

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [10. Redes públicas, privadas e endereços especiais](semana_02_estudo.md#s2-d2-publicos-privados-especiais).

Qual dos endereços abaixo pertence a um bloco privado definido pela RFC 1918?

A) `172.15.200.1`.
B) `172.32.0.10`.
C) `192.169.10.20`.
D) `172.31.200.5`.

### S2D2Q075 — Endereços de loopback em IPv4 e IPv6

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [10. Redes públicas, privadas e endereços especiais — Loopback](semana_02_estudo.md#s2-d2-publicos-privados-especiais).

Sobre endereços de loopback, assinale a alternativa correta.

A) Apenas `127.0.0.1` é loopback; os demais endereços `127/8` são públicos.
B) O IPv4 reserva `127.0.0.0/8`, e o IPv6 usa `::1/128`.
C) Loopback identifica o gateway padrão que encaminha pacotes para a Internet.
D) O IPv6 utiliza `fe80::1` como seu único endereço de loopback.

### S2D2Q076 — Alcance de um endereço APIPA

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [10. Redes especiais — IPv4 link-local e APIPA](semana_02_estudo.md#s2-d2-publicos-privados-especiais), nos trechos sobre a faixa `169.254/16`, alcance local e autoconfiguração após falha de DHCP.

Um computador Windows configurado para DHCP não recebe resposta do servidor e atribui a si mesmo `169.254.20.8/16`. Como essa configuração deve ser interpretada?

A) É endereço de loopback, portanto o host o usa apenas internamente e não transmite quadros no enlace.

B) É endereço privado RFC 1918, portanto o host recebe rota padrão mesmo sem resposta do servidor DHCP.

C) É endereço link-local/APIPA, portanto pode servir no enlace, mas não cria acesso roteado e sugere falha do DHCP.

D) É endereço de documentação, portanto o host o escolhe provisoriamente para acessar redes externas.

### S2D2Q077 — Blocos especiais fora da RFC 1918

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [10. Redes especiais — IPv4 público](semana_02_estudo.md#s2-d2-publicos-privados-especiais), especialmente a ressalva de que estar fora da RFC 1918 não prova utilização unicast pública.

Um inventário classifica como “unicast público utilizável” todo endereço IPv4 que não pertence aos três blocos privados da RFC 1918. Qual ajuste técnico é necessário nessa regra?

A) Manter a regra, pois somente os blocos privados possuem restrições de alcance ou finalidade no IPv4.

B) Excluir apenas endereços terminados em `.0` ou `.255`, pois o último octeto define toda finalidade especial.

C) Consultar também os blocos especiais, pois loopback, link-local, documentação e multicast ficam fora da RFC 1918.

D) Excluir apenas endereços com prefixo maior que `/24`, pois prefixos menores são sempre públicos e roteáveis.

### S2D2Q078 — Divisão uniforme de um prefixo em sub-redes menores

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [9. Exemplos de IPv4 e CIDR — Divisão de /24 em /27](semana_02_estudo.md#s2-d2-calculos).

Ao dividir integralmente `192.168.50.0/24` em sub-redes `/27` iguais, obtêm-se:

A) 8 sub-redes, cada uma com 32 endereços e 30 hosts convencionais.
B) 4 sub-redes, cada uma com 64 endereços e 62 hosts convencionais.
C) 8 sub-redes, cada uma com 30 endereços e 28 hosts convencionais.
D) 16 sub-redes, cada uma com 16 endereços e 14 hosts convencionais.

### S2D2Q079 — Alinhamento e pertencimento a uma sub-rede `/23`

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [11. Sub-redes — Verificação de pertencimento](semana_02_estudo.md#s2-d2-subredes).

Considere A=`192.168.10.250/23`, B=`192.168.11.200/23` e C=`192.168.12.1/23`. Analise as afirmativas.

I. A e B pertencem à mesma sub-rede.
II. A rede de A e B é `192.168.10.0/23`, com broadcast `192.168.11.255`.
III. C pertence à mesma sub-rede de A e B, porque `/23` abrange dois valores consecutivos do terceiro octeto.

Está correto o que se afirma em:

A) I, apenas.
B) I e II, apenas.
C) II e III, apenas.
D) I, II e III.

### S2D2Q080 — Identificação do bloco que contém um IPv4

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [8. Rede, broadcast e hosts — Tamanho do bloco](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

Qual bloco `/26` contém o endereço `203.0.113.205`?

A) `203.0.113.128/26`.
B) `203.0.113.192/26`.
C) `203.0.113.200/26`.
D) `203.0.113.205/26`.

### S2D2Q081 — Alcançabilidade e validade do gateway dentro da sub-rede

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [12. Gateway padrão](semana_02_estudo.md#s2-d2-gateway).

Um host usa `192.168.70.78/27`. Sem mecanismos adicionais, qual endereço pode ser configurado como gateway válido e diretamente alcançável nessa sub-rede?

A) `192.168.70.64`.
B) `192.168.70.95`.
C) `192.168.70.97`.
D) `192.168.70.94`.

### S2D2Q082 — Uso do gateway como próximo salto e separação entre IP e MAC

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [12. Gateway padrão](semana_02_estudo.md#s2-d2-gateway).

Uma estação IPv4 Ethernet precisa enviar um pacote a um servidor fora de sua sub-rede e possui uma rota padrão válida. No primeiro enlace:

A) o endereço IP de destino passa a ser o do gateway, e o MAC de destino continua sendo o do servidor remoto.
B) o pacote conserva o IP do servidor como destino, enquanto o quadro usa o MAC do gateway ou próximo salto.
C) o quadro é enviado sem MAC de destino, pois o roteador toma a decisão apenas com a porta TCP.
D) a estação descobre por ARP o MAC do servidor remoto através de todos os roteadores.

### S2D2Q083 — Sequência de resolução ARP no enlace local

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [13. ARP](semana_02_estudo.md#s2-d2-arp), especialmente a decisão entre destino local e remoto e o fluxo ARP Request em broadcast seguido normalmente por ARP Reply em unicast.

O host A, `192.168.10.20/24`, enviará um pacote ao host B, `192.168.10.80/24`. O gateway é `192.168.10.1`, e A não possui a associação de B em seu cache ARP. Qual sequência descreve a resolução normal antes do primeiro quadro?

A) A transmite ARP Request em multicast perguntando por `.80`; B envia ARP Reply em broadcast a todos os hosts.

B) A transmite ARP Request em unicast ao gateway perguntando por `.80`; o gateway devolve o próprio MAC no ARP Reply.

C) A transmite ARP Request em broadcast perguntando por `.80`; B envia ARP Reply normalmente em unicast com seu MAC.

D) A transmite ARP Reply em broadcast anunciando `.80`; B confirma a associação com outro ARP Reply em unicast.

### S2D2Q084 — MAC do próximo salto para destino remoto

**Nível:** Médio

**Uso:** Revisão

**Referência:** [13. ARP — Destino remoto](semana_02_estudo.md#s2-d2-arp), no trecho que determina a resolução do MAC do gateway ou próximo salto, e não do servidor remoto.

O host `192.168.10.20/24` enviará um pacote a `198.51.100.10` usando o gateway `192.168.10.1`. Qual endereço MAC o host precisa obter por ARP para montar o primeiro quadro Ethernet?

A) O MAC do servidor remoto, pois ele permanece como destino do pacote IP durante todo o percurso.

B) O MAC do roteador da rede remota, pois esse equipamento entregará o último quadro ao servidor.

C) O MAC do switch de acesso, pois esse equipamento encaminhará o primeiro quadro dentro da LAN.

D) O MAC do gateway local, pois ele é o próximo salto alcançável no enlace do host de origem.

### S2D2Q085 — Função e transporte das mensagens ICMP

**Nível:** Médio

**Uso:** Revisão

**Referência:** [14. ICMP e ICMPv6](semana_02_estudo.md#s2-d2-icmp).

Sobre o ICMP, assinale a alternativa INCORRETA.

A) O ICMP usa uma porta TCP ou UDP própria, que precisa ser descoberta antes do envio de cada mensagem.
B) Echo Request e Echo Reply podem ser empregados pelo comando `ping`.
C) Time Exceeded e Destination Unreachable são exemplos de mensagens de controle ou erro.
D) Filtrar indiscriminadamente todo ICMP pode prejudicar diagnóstico e funções da rede.

### S2D2Q086 — Mensagens de resolução de vizinhança no IPv6

**Nível:** Médio

**Uso:** Revisão

**Referência:** [14. ICMPv6 — Neighbor Discovery, NS e NA](semana_02_estudo.md#s2-d2-icmp), nos trechos sobre resolução de endereço de enlace, multicast solicited-node e resposta Neighbor Advertisement.

Um host IPv6 conhece o endereço unicast de um vizinho no mesmo enlace, mas ainda precisa descobrir seu endereço de camada de enlace. Qual troca de mensagens atende normalmente a essa finalidade?

A) Neighbor Solicitation para multicast solicited-node e Neighbor Advertisement com a informação de enlace.

B) Router Solicitation em multicast e Router Advertisement em unicast, mesmo que o alvo não seja roteador.

C) Echo Request em multicast e Echo Reply em unicast, usando o diagnóstico como resolução de endereço.

D) ARP Request em broadcast e ARP Reply em unicast, preservando o mecanismo usado no IPv4.

### S2D2Q087 — Regras de abreviação textual de IPv6

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [15. IPv6 — Regras de abreviação](semana_02_estudo.md#s2-d2-ipv6).

Qual é a abreviação válida de `2001:0db8:0000:0000:0000:ff00:0042:8329`?

A) `2001::db8::ff00:42:8329`.
B) `2001:db8:0:0:ff00::42:8329`.
C) `2001:db8::ff00:42:8329`.
D) `2001:db8:ff00:42:8329::`.

### S2D2Q088 — Ausência de broadcast no IPv6

**Nível:** Médio

**Uso:** Revisão

**Referência:** [15. IPv6 — Tipos de endereço](semana_02_estudo.md#s2-d2-ipv6).

Em relação ao broadcast no IPv6, assinale a alternativa correta.

A) O IPv6 não possui endereço de broadcast; a entrega em grupo pode usar multicast.
B) `ff02::1` é o endereço de broadcast global de todos os dispositivos IPv6.
C) Todo prefixo IPv6 reserva o último endereço para broadcast dirigido.
D) O broadcast IPv6 existe apenas em sub-redes com prefixo `/64`.

### S2D2Q089 — Entrega unicast, multicast e anycast no IPv6

**Nível:** Médio

**Uso:** Revisão

**Referência:** [15. IPv6 — Tipos de endereço](semana_02_estudo.md#s2-d2-ipv6), especialmente as definições de entrega a uma interface, a um grupo e a uma dentre várias interfaces.

Em uma rede IPv6, X identifica uma única interface; Y identifica um grupo cujos participantes recebem uma cópia; e Z é atribuído a interfaces distintas, mas o roteamento entrega o pacote a uma delas. X, Y e Z são, respectivamente:

A) multicast, unicast e anycast.

B) anycast, multicast e unicast.

C) unicast, multicast e anycast.

D) unicast, anycast e multicast.

### S2D2Q090 — Determinação de prefixo IPv6 em fronteira de grupo

**Nível:** Médio

**Uso:** Revisão

**Referência:** [15. IPv6 — Prefixo IPv6](semana_02_estudo.md#s2-d2-ipv6).

Qual é o prefixo de rede do endereço `2001:db8:abcd:12ef:1234:5678:9abc:def0/64`?

A) `2001:db8:abcd::/64`.
B) `2001:db8:abcd:12ef::/64`.
C) `2001:db8:abcd:1200::/64`.
D) `2001:db8:abcd:12ef:1234::/64`.

### S2D2Q091 — Blocos especiais e escopos do IPv6

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [15. IPv6 — Blocos especiais importantes](semana_02_estudo.md#s2-d2-ipv6).

Sobre blocos especiais do IPv6, assinale a alternativa correta.

A) `fe80::/10` é unicast link-local, `::1/128` é loopback e `2001:db8::/32` é reservado para documentação.
B) `fc00::/7` é link-local, equivale a `fe80::/10` e nunca pode ser roteado entre sites.
C) `::/128` identifica todos os roteadores do enlace.
D) `2001:db8::/32` é a faixa obrigatória de endereços públicos de produção.

### S2D2Q092 — Multicast IPv6, escopo link-local e solicited-node no Neighbor Discovery

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [15. IPv6 — Escopo multicast](semana_02_estudo.md#s2-d2-ipv6) e [14. ICMPv6 — Neighbor Discovery](semana_02_estudo.md#s2-d2-icmp).

Analise as afirmativas sobre multicast e descoberta de vizinhos no IPv6.

I. `ff02::1` identifica todos os nós IPv6 do enlace, mas é multicast, não broadcast.
II. Na resolução inicial, uma NS é enviada ao multicast solicited-node derivado do endereço-alvo, em vez de consultar indiscriminadamente `ff02::1`.
III. Roteadores não devem encaminhar tráfego de escopo link-local para além do enlace.

Está correto o que se afirma em:

A) I, apenas.
B) I e III, apenas.
C) II e III, apenas.
D) I, II e III.

### S2D2Q093 — Escolha do prefixo a partir de requisito de hosts e maximização de sub-redes

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

Uma rede `192.168.8.0/24` deve ser dividida em sub-redes iguais, buscando a maior quantidade possível de sub-redes, com pelo menos 50 hosts convencionais em cada uma. Qual solução atende ao requisito?

A) Usar `/27`, obtendo 8 sub-redes com 62 hosts convencionais em cada uma.
B) Usar `/26`, obtendo 4 sub-redes com 62 hosts convencionais em cada uma.
C) Usar `/25`, obtendo 4 sub-redes com 126 hosts convencionais em cada uma.
D) Usar `/28`, obtendo 16 sub-redes com 50 hosts convencionais em cada uma.

### S2D2Q094 — Alinhamento e não sobreposição em VLSM

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

No bloco `10.0.0.0/24`, já foram alocados `10.0.0.0/26` e `10.0.0.128/27`. Qual prefixo adicional `/27` está corretamente alinhado e não se sobrepõe aos blocos existentes?

A) `10.0.0.32/27`.
B) `10.0.0.144/27`.
C) `10.0.0.128/27`.
D) `10.0.0.64/27`.

### S2D2Q095 — Decisão de localidade com máscaras divergentes

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [11. Sub-redes — Verificação de pertencimento](semana_02_estudo.md#s2-d2-subredes).

O host A usa `192.168.1.10/24`, e o host B usa `192.168.1.200/25`. Considerando a decisão local de cada host e desconsiderando mecanismos adicionais, assinale a alternativa correta.

A) Ambos consideram o outro local, pois os três primeiros octetos coincidem.
B) Ambos consideram o outro remoto, pois os prefixos configurados são diferentes.
C) A considera B local, mas B considera A remoto, o que pode produzir alcance assimétrico.
D) B considera A local, mas A considera B remoto, porque `/25` abrange mais endereços que `/24`.

### S2D2Q096 — Cálculo integrado de rede, broadcast e hosts em `/21`

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [8. Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

Para o endereço `10.34.173.205/21`, assinale a alternativa que apresenta rede, broadcast dirigido e quantidade convencional de hosts utilizáveis.

A) `10.34.168.0`, `10.34.175.255` e 2046 hosts.
B) `10.34.172.0`, `10.34.175.255` e 1022 hosts.
C) `10.34.168.0`, `10.34.183.255` e 4094 hosts.
D) `10.34.173.0`, `10.34.173.255` e 254 hosts.

### S2D2Q097 — Localização ordinal de sub-rede e respectivas fronteiras

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

A rede `192.168.60.0/24` foi dividida integralmente em sub-redes `/28`. Contando `192.168.60.0/28` como a primeira, quais são rede, broadcast e faixa de hosts da décima sub-rede?

A) Rede `.128`, broadcast `.143`, hosts `.129` a `.142`.
B) Rede `.144`, broadcast `.159`, hosts `.145` a `.158`.
C) Rede `.160`, broadcast `.175`, hosts `.161` a `.174`.
D) Rede `.144`, broadcast `.160`, hosts `.145` a `.159`.

### S2D2Q098 — Limites de aplicação da fórmula `2^h - 2`

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [8. Endereço de rede, broadcast e hosts válidos — Exceções](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

Analise as afirmativas sobre prefixos e exceções de endereçamento.

I. Em enlace IPv4 ponto a ponto compatível com a RFC 3021, os dois endereços de um `/31` podem representar as extremidades.
II. Um `/32` IPv4 representa um único endereço ou rota de host, sem intervalo convencional de hosts.
III. Como o IPv6 não possui broadcast, não se deve aplicar automaticamente a ele a fórmula IPv4 `2^h - 2`.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I e II, apenas.
D) I, II e III.

### S2D2Q099 — Expiração do TTL e ICMP Time Exceeded

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [14. ICMP e ICMPv6](semana_02_estudo.md#s2-d2-icmp), especialmente os trechos sobre Time Exceeded, ausência de portas de transporte e inexistência de confiabilidade automática do IP.

Um pacote IPv4 chega ao primeiro roteador com TTL igual a 1. Após reduzir o campo, o roteador obtém zero. Qual procedimento é compatível com IP e ICMP?

A) Encaminhar o pacote com TTL zero e solicitar ao destino um ICMP Destination Unreachable para a origem.

B) Restaurar o TTL ao valor inicial e encaminhar o pacote, registrando a mudança em uma mensagem ICMP Redirect.

C) Descartar o pacote e poder enviar ICMP Time Exceeded à origem, sem usar porta TCP/UDP nem retransmitir os dados.

D) Descartar o pacote e enviar ICMP Echo Reply à origem, que então refaz automaticamente a transmissão.

### S2D2Q100 — Integração entre roteamento, protocolos e comparação OSI/TCP/IP

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip), [3. Encapsulamento](semana_02_estudo.md#s2-d2-encapsulamento) e [ARP](semana_02_estudo.md#s2-d2-arp).

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
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** convivência entre legalidade e eficiência no art. 37.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão de Administração Pública — Princípios do art. 37](semana_02_estudo.md#s2-d2-revisao-principios).

Um gestor decide ignorar requisito legal porque acredita que o procedimento alternativo será mais rápido e econômico. À luz dos princípios do art. 37, assinale a alternativa correta.

A) A eficiência autoriza afastar a legalidade sempre que houver redução de custos.
B) A legalidade vincula apenas particulares, enquanto a Administração atua por liberdade geral.
C) A conduta é válida se receber publicidade depois de praticada, ainda que permaneça contrária à lei.
D) A busca de eficiência não permite descumprir o ordenamento nem atuar fora da competência atribuída.
#### Extra Dia 2.2
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** princípio da impessoalidade e vedação à promoção pessoal.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão de Administração Pública — Princípios do art. 37](semana_02_estudo.md#s2-d2-revisao-principios).

Uma autoridade utiliza campanha institucional para destacar seu nome, imagem e realizações pessoais. O princípio mais diretamente comprometido é o da:

A) impessoalidade, pois a comunicação pública não deve servir à promoção pessoal do agente.
B) eficiência, porque toda publicidade institucional reduz necessariamente a qualidade do serviço.
C) legalidade, exclusivamente porque o agente se identificou perante os cidadãos.
D) moralidade, entendida apenas como opinião subjetiva sobre o comportamento da autoridade.
#### Extra Dia 2.3
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** publicidade administrativa em harmonia com proteção de dados.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão de Administração Pública — Princípios do art. 37 e LAI x LGPD](semana_02_estudo.md#s2-d2-revisao-lai-lgpd).

Sobre publicidade administrativa e proteção de dados pessoais, assinale a alternativa correta.

A) A publicidade exige divulgação irrestrita de qualquer dado mantido pelo Poder Público.
B) Transparência é a regra, mas convive com sigilo legal, finalidade, necessidade e proteção de dados pessoais.
C) A LGPD transforma automaticamente toda informação pública em informação sigilosa.
D) A LAI deixa de produzir efeitos sempre que um documento contém qualquer dado pessoal.
#### Extra Dia 2.4
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Administração Direta, Indireta, órgão, entidade e autarquia.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão de Administração Pública — Administração Direta e Indireta](semana_02_estudo.md#s2-d2-revisao-organizacao).

Assinale a alternativa que diferencia corretamente órgão e entidade e classifica o CRA-PR.

A) Órgão e entidade possuem personalidade jurídica própria; o CRA-PR é órgão da Administração Direta.
B) Órgão é pessoa jurídica autônoma; entidade é centro de competências sem personalidade própria.
C) Órgão não possui personalidade jurídica própria; entidade possui, e o CRA-PR é autarquia da Administração Indireta.
D) O CRA-PR é associação privada, pois conselhos profissionais não integram a Administração Pública.
#### Extra Dia 2.5
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** definição de autarquia.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão de Administração Pública — Administração Direta e Indireta](semana_02_estudo.md#s2-d2-revisao-organizacao).

Na revisão estudada, autarquia é definida como:

A) modalidade de empresa pública que deve possuir capital privado majoritário.
B) órgão sem personalidade jurídica criado por ato interno para explorar atividade econômica.
C) sociedade privada formada livremente por agentes públicos e sem vínculo com a Administração Indireta.
D) pessoa jurídica de direito público criada por lei para desempenhar atividade administrativa típica.
#### Extra Dia 2.6
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** elementos clássicos do ato administrativo.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão de Administração Pública — Elementos e atributos do ato](semana_02_estudo.md#s2-d2-revisao-atos).

Servidor sem atribuição legal para decidir determinado processo pratica o ato mesmo assim. O elemento do ato administrativo diretamente afetado é:

A) o objeto, porque todo problema de autoria altera apenas o efeito jurídico produzido.
B) a forma, pois competência indica somente o modo pelo qual o ato se exterioriza.
C) a competência, que responde à pergunta sobre quem pode praticar o ato.
D) o motivo, que se confunde com a identidade funcional do agente responsável.
#### Extra Dia 2.7

- **Dia:** Dia 2

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** presunção de legitimidade, imperatividade e autoexecutoriedade.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [Elementos e atributos do ato administrativo](semana_02_estudo.md#s2-d2-revisao-atos), nos trechos sobre presunção relativa e hipóteses de autoexecutoriedade.

Ao revisar os atributos dos atos administrativos, um servidor compara a presunção de legitimidade e veracidade com a autoexecutoriedade. Assinale a alternativa correta.

A) A presunção não admite prova em contrário, e a autoexecutoriedade acompanha todo ato, mesmo sem previsão ou urgência.

B) A presunção não admite prova em contrário, e a autoexecutoriedade depende de previsão legal ou de situação urgente.

C) A presunção admite prova em contrário, e a autoexecutoriedade acompanha todo ato, mesmo sem previsão ou urgência.

D) A presunção admite prova em contrário, e a autoexecutoriedade depende de previsão legal ou de situação urgente.

#### Extra Dia 2.8
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** distinção entre anulação e revogação.
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Revisão de Administração Pública — Anulação, revogação e convalidação](semana_02_estudo.md#s2-d2-revisao-desfazimento).

A Administração identifica dois atos: o primeiro é ilegal; o segundo é válido, mas deixou de ser conveniente. A providência adequada, quanto à retirada de cada ato, é:

A) revogar ambos, porque ilegalidade e inconveniência são questões de mérito.
B) anular ambos, pois todo ato inconveniente passa a ser ilegal.
C) convalidar necessariamente o primeiro e anular o segundo.
D) anular o primeiro e, respeitados os direitos adquiridos, revogar o segundo.
#### Extra Dia 2.9
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** pressupostos da convalidação.
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Revisão de Administração Pública — Anulação, revogação e convalidação](semana_02_estudo.md#s2-d2-revisao-desfazimento).

A convalidação de ato administrativo é cabível, segundo o núcleo revisado, quando:

A) o ato é válido, mas a Administração prefere substituí-lo por solução mais conveniente.
B) há vício sanável e a correção não causa lesão ao interesse público nem prejuízo a terceiros.
C) qualquer ilegalidade é constatada, inclusive vício insanável, independentemente de consequências.
D) ocorreu má-fé do destinatário e já transcorreu o prazo de cinco anos.
#### Extra Dia 2.10

- **Dia:** Dia 2

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** decadência do direito de anular ato favorável no art. 54.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [Anulação, revogação e convalidação](semana_02_estudo.md#s2-d2-revisao-desfazimento), no parágrafo sobre prazo de cinco anos, má-fé e primeiro pagamento em efeitos patrimoniais contínuos.

Sem má-fé comprovada, a Administração revê em 2/9/2025 dois atos favoráveis: I. ato de efeito único praticado em 1/8/2020; II. benefício de efeitos patrimoniais contínuos cujo primeiro pagamento ocorreu em 1/12/2020. À luz do art. 54 da Lei nº 9.784/1999, assinale a alternativa correta.

A) Não ocorreu decadência em nenhum caso, pois vício de legalidade permite anulação a qualquer tempo, ainda que o destinatário esteja de boa-fé.

B) Ocorreu decadência nos dois casos, pois o prazo do benefício contínuo é contado da prática do ato, sem relação com o primeiro pagamento.

C) Ocorreu decadência no ato I, mas não no ato II, pois são cinco anos desde o ato ou, nos efeitos contínuos, desde o primeiro pagamento.

D) Não ocorreu decadência no ato I, mas ocorreu no ato II, pois o prazo comum é bienal e se conta do último pagamento efetuado.

#### Extra Dia 2.11

- **Dia:** Dia 2

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** articulação entre LAI e LGPD.

- **Nível:** Médio

- **Uso:** Revisão

- **Referência:** [LAI x LGPD](semana_02_estudo.md#s2-d2-revisao-lai-lgpd), especialmente a convivência entre acesso devido e proteção de dados pessoais.

Um pedido de acesso alcança documento público que também contém dados pessoais não necessários à finalidade informativa. A relação adequada entre LAI e LGPD é:

A) Aplicar somente a LAI e divulgar o documento integral, pois a presença em arquivo público afasta qualquer proteção de dado pessoal.

B) Aplicar somente a LGPD e negar todo o documento, pois a presença de qualquer dado pessoal cria sigilo automático sobre o conteúdo.

C) Escolher uma das duas leis conforme a preferência do órgão, pois transparência e proteção não podem incidir no mesmo caso.

D) Compatibilizar as duas leis, fornecer o acesso devido e proteger os dados pessoais cuja exposição não seja necessária ou autorizada.

#### Extra Dia 2.12
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** dolo e tipicidade na improbidade administrativa.
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Revisão de Administração Pública — Improbidade administrativa](semana_02_estudo.md#s2-d2-revisao-improbidade).

Um agente comete irregularidade formal, mas não há demonstração de dolo nem enquadramento nas condutas tipificadas. Com base na revisão sobre improbidade, é correto afirmar que:

A) simples ilegalidade ou voluntariedade não basta; são necessários dolo e enquadramento legal nos termos da lei.
B) toda irregularidade administrativa configura automaticamente ato de improbidade contra princípios.
C) a ausência de dano ao erário torna impossível qualquer espécie de improbidade, ainda que exista outro tipo legal doloso.
D) culpa leve e resultado inconveniente bastam, sem necessidade de conduta tipificada.
#### Extra Dia 2.13
- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** distinção entre dispensa e inexigibilidade.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Revisão de Administração Pública — Licitação e contratação direta](semana_02_estudo.md#s2-d2-revisao-licitacao).

Uma contratação possui fornecedor exclusivo comprovado e competição inviável. Considerando apenas o núcleo estudado, a situação pode caracterizar:

A) inexigibilidade, desde que observados os requisitos legais aplicáveis.
B) pregão, pois fornecedor exclusivo é critério de julgamento dessa modalidade.
C) revogação da licitação, que elimina a necessidade de processo e motivação.
D) dispensa, porque toda contratação direta pressupõe competição inviável.
#### Extra Dia 2.14

- **Dia:** Dia 2

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** contratação direta e modalidades licitatórias.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Licitação e contratação direta](semana_02_estudo.md#s2-d2-revisao-licitacao), nos trechos sobre instrução da contratação direta e modalidades da Lei nº 14.133/2021.

Uma equipe revisa duas proposições: I. contratação direta continua sujeita a processo, motivação, justificativa e controle; II. pregão e diálogo competitivo são modalidades da Lei nº 14.133/2021. Assinale a alternativa correta.

A) A proposição I está errada, e a II está errada, pois contratação direta dispensa processo e os dois institutos são critérios de julgamento.

B) A proposição I está correta, e a II está errada, pois contratação direta exige processo, mas os dois institutos são critérios de julgamento.

C) A proposição I está correta, e a II está correta, pois contratação direta exige instrução e os dois institutos integram o rol de modalidades.

D) A proposição I está errada, e a II está correta, pois contratação direta dispensa instrução, embora os dois institutos sejam modalidades.

#### Extra Dia 2.15

- **Dia:** Dia 2

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** responsabilidade civil objetiva do Estado e ação regressiva.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Responsabilidade civil do Estado](semana_02_estudo.md#s2-d2-revisao-responsabilidade), nos trechos sobre requisitos perante a vítima e regresso em caso de dolo ou culpa.

Ao analisar dano causado por agente público nessa qualidade, a equipe separa a pretensão da vítima contra o Estado da ação regressiva contra o agente. Assinale a alternativa correta.

A) A vítima deve provar conduta, dano, nexo e culpa do agente, enquanto o regresso independe de dolo ou culpa.

B) A vítima recebe indenização sem demonstrar dano ou nexo, enquanto o regresso depende de dolo ou culpa do agente.

C) A vítima deve provar conduta, dano e nexo, enquanto o regresso contra o agente independe de dolo ou culpa.

D) A vítima deve provar conduta, dano e nexo, sem provar culpa estatal, enquanto o regresso exige dolo ou culpa do agente.

#### Extra Dia 2.16

- **Dia:** Dia 2

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** quantificadores, modalidade e alcance do enunciado.

- **Nível:** Difícil

- **Uso:** Simulado

- **Referência:** [Quantificadores e alcance](semana_02_estudo.md#s2-d2-revisao-quantificadores), especialmente a diferença entre possibilidade, obrigação e recorte ponto a ponto.

Leia: “Em enlaces IPv4 ponto a ponto, um prefixo /31 pode usar os dois endereços.” Assinale a interpretação que preserva simultaneamente o contexto e a força do verbo.

A) A frase transforma o /31 em obrigação para qualquer rede IPv4 e elimina a restrição ao enlace ponto a ponto.

B) A frase apresenta, apenas no contexto ponto a ponto, a possibilidade de empregar os dois endereços do /31.

C) A frase apresenta, no contexto ponto a ponto, proibição de empregar os dois endereços, porque “pode” nega a operação.

D) A frase atribui a toda implementação IPv4 o dever de adotar /31 sempre que existirem exatamente duas interfaces.

#### Extra Dia 2.17
- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** coesão referencial e relação adversativa.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Revisão de Português — Coesão e relação lógica](semana_02_estudo.md#s2-d2-revisao-coesao).

No período “O IPv6 amplia o espaço de endereçamento; entretanto, esse fato não elimina a necessidade de planejamento”, assinale a alternativa correta.

A) “Entretanto” marca oposição ou ressalva, e “esse fato” retoma a ampliação do espaço de endereçamento.
B) “Entretanto” conclui o raciocínio, e “esse” retoma a necessidade de planejamento.
C) “Entretanto” introduz causa, e “esse” antecipa uma informação ainda não apresentada.
D) O período permite inferir que o planejamento se tornou desnecessário.
#### Extra Dia 2.18
- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pontuação de termos essenciais e expressões explicativas.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Revisão de Português — Pontuação](semana_02_estudo.md#s2-d2-revisao-pontuacao).

Assinale a alternativa com pontuação adequada.

A) Os endereços privados, podem ser reutilizados por organizações diferentes.
B) O ARP, no IPv4 sobre Ethernet, resolve endereço IP em endereço MAC.
C) O IPv6 que possui 128 bits não, utiliza endereço de broadcast.
D) O gateway padrão encaminha, destinos remotos quando não há rota mais específica.
#### Extra Dia 2.19
- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** encontro entre preposição `a` e artigo feminino `a` ou `as`.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Revisão de Português — Crase aplicada](semana_02_estudo.md#s2-d2-revisao-crase).

Assinale a alternativa em que o emprego da crase está correto.

A) O roteador começou à encaminhar os pacotes para o próximo salto.
B) A regra se aplica às sub-redes IPv4 convencionais.
C) O pacote chegou à transmitir dados depois da configuração.
D) O analista entregou o relatório à revisar pelo gestor.
#### Extra Dia 2.20
- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** equivalência em reescrita técnica.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Revisão de Português — Reescrita técnica](semana_02_estudo.md#s2-d2-revisao-reescrita).

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
| 2 | B |
| 3 | D |
| 4 | A |
| 5 | B |
| 6 | C |
| 7 | B |
| 8 | D |
| 9 | A |
| 10 | A |
| 11 | C |
| 12 | C |
| 13 | D |
| 14 | B |
| 15 | A |
| 16 | D |
| 17 | B |
| 18 | C |
| 19 | B |
| 20 | D |
| 21 | C |
| 22 | A |
| 23 | A |
| 24 | D |
| 25 | B |
| 26 | C |
| 27 | C |
| 28 | A |
| 29 | B |
| 30 | B |
| 31 | D |
| 32 | B |
| 33 | C |
| 34 | D |
| 35 | A |
| 36 | A |
| 37 | C |
| 38 | A |
| 39 | C |
| 40 | B |
| 41 | A |
| 42 | D |
| 43 | B |
| 44 | D |
| 45 | C |
| 46 | A |
| 47 | B |
| 48 | D |
| 49 | C |
| 50 | C |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 2.1 | D |
| 2.2 | A |
| 2.3 | B |
| 2.4 | C |
| 2.5 | D |
| 2.6 | C |
| 2.7 | D |
| 2.8 | D |
| 2.9 | B |
| 2.10 | C |
| 2.11 | D |
| 2.12 | A |
| 2.13 | A |
| 2.14 | C |
| 2.15 | D |
| 2.16 | B |
| 2.17 | A |
| 2.18 | B |
| 2.19 | B |
| 2.20 | A |

## Comentários do Dia 2

### Comentário S2D2Q051

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D2Q052

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Sessão organiza diálogos, manutenção e sincronização, não a forma de representar os dados.
- **B)** Correta. Apresentação cuida didaticamente da representação, codificação, compressão e proteção dos dados.
- **C)** Incorreta. Transporte atende processos finais, usando recursos como portas, segmentação e controle conforme o protocolo.
- **D)** Incorreta. Rede trata de endereçamento lógico e encaminhamento entre redes.

**Conceito:** função da camada de Apresentação.

**Pegadinha:** atribuir criptografia automaticamente ao Transporte por ela proteger uma comunicação fim a fim.

**Como pensar:** pergunte se a tarefa altera como a informação é representada ou como ela é encaminhada.

**Referência:** [1. Modelo OSI — Camada 6, Apresentação](semana_02_estudo.md#s2-d2-osi).

### Comentário S2D2Q053

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmativa II também é verdadeira ao associar endereçamento lógico e encaminhamento à Rede.
- **B)** Incorreta. A III é falsa, pois o IP não garante confirmação e retransmissão fim a fim.
- **C)** Incorreta. Incluir a III transfere indevidamente ao IP uma confiabilidade que pode ser oferecida pelo TCP.
- **D)** Correta. Transporte comunica processos e pode usar portas; Rede cuida de IP e encaminhamento.

**Conceito:** distinção entre as funções das camadas de Transporte e Rede.

**Pegadinha:** tratar comunicação fim a fim como sinônimo de entrega confiável realizada pelo IP.

**Como pensar:** avalie cada assertiva isoladamente e separe processo, rota e mecanismo de confiabilidade.

**Referência:** [1. Modelo OSI — Camadas 4 e 3](semana_02_estudo.md#s2-d2-osi).

### Comentário S2D2Q054

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A Física transmite bits como sinais sem interpretar endereços MAC ou IP.
- **B)** Incorreta. Quadros e aprendizagem de MAC pertencem ao Enlace.
- **C)** Incorreta. Diálogo e sincronização são funções conceituais da Sessão.
- **D)** Incorreta. Escolher rota pelo IP é função de Rede, não de um repetidor físico.

**Conceito:** atuação da camada Física e de repetidores.

**Pegadinha:** confundir regeneração do sinal com análise do conteúdo transportado.

**Como pensar:** se o dispositivo apenas trata sinal e bits, permaneça na camada 1.

**Referência:** [1. Modelo OSI — Camada 1, Física](semana_02_estudo.md#s2-d2-osi).

### Comentário S2D2Q055

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D2Q056

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D2Q057

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D2Q058

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O receptor precisa reconhecer o quadro antes de alcançar o segmento encapsulado no pacote.
- **B)** Incorreta. A ordem começa pelas camadas inferiores, e o segmento precede a entrega dos dados à aplicação.
- **C)** Incorreta. Bits não são processados depois do quadro; constituem sua representação no meio.
- **D)** Correta. Bits formam o quadro, do qual se extrai o pacote IPv4, depois o segmento TCP e os dados.

**Conceito:** desencapsulamento ascendente no receptor.

**Pegadinha:** repetir a ordem do emissor, quando o receptor percorre o caminho inverso.

**Como pensar:** comece pelo que chega fisicamente e remova um invólucro de cada vez.

**Referência:** [3. Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento).

### Comentário S2D2Q059

**Nível:** Difícil

**Uso:** Essenciais
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

### Comentário S2D2Q060

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. TCP usa segmento, IP pacote ou datagrama, Ethernet quadro e Física bits.
- **B)** Incorreta. A opção troca as PDUs de TCP, IP e Ethernet e chama os bits de dados genéricos.
- **C)** Incorreta. Pacote, quadro e datagrama UDP foram associados às camadas erradas.
- **D)** Incorreta. Bits são da Física, não do TCP; pacote é da camada Internet, não da Física.

**Conceito:** nomenclatura específica das PDUs.

**Pegadinha:** usar “pacote” como nome universal quando a questão exige precisão por camada.

**Como pensar:** ligue Transporte a segmento ou datagrama, Internet a pacote, Enlace a quadro e Física a bits.

**Referência:** [4. PDUs](semana_02_estudo.md#s2-d2-pdus).

### Comentário S2D2Q061

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** UDP pertence ao Transporte, enquanto IP pertence à camada Internet; o uso da palavra “datagrama” não os coloca na mesma camada.
- **B)** UDP não é protocolo da Aplicação e não encapsula IP; ele fornece a PDU que será carregada pelo datagrama IP.
- **C)** o datagrama UDP é uma unidade de Transporte que pode compor a carga útil de um datagrama IP.
- **D)** IP não pertence ao Transporte, e a alternativa inverte a ordem efetiva de encapsulamento.

**Conceito:** camada e relação de encapsulamento entre datagrama UDP e datagrama IP.

**Pegadinha:** interpretar o mesmo nome genérico de PDU como prova de que UDP e IP pertencem à mesma camada.

**Como pensar:** identifique primeiro a camada de cada protocolo; depois coloque a PDU da camada superior dentro da PDU da camada inferior.

**Referência:** [4. PDUs](semana_02_estudo.md#s2-d2-pdus), especialmente a tabela que associa o datagrama UDP ao Transporte e o datagrama IP à camada Rede/Internet.

### Comentário S2D2Q062

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D2Q063

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o endereço de destino orienta a decisão de encaminhamento, mas não demonstra que o destino seja alcançável pela porta de entrada.
- **B)** o switch associa a origem à porta pela qual o quadro chegou, não à porta que eventualmente escolherá para encaminhá-lo.
- **C)** a presença do destino no cabeçalho não revela sua localização; o switch só aprendeu diretamente a localização da origem.
- **D)** a chegada do quadro pela porta 5 comprova que o MAC de origem é alcançável por essa porta naquele momento.

**Conceito:** aprendizagem da tabela de comutação pelo MAC de origem e pela porta de entrada.

**Pegadinha:** trocar a informação aprendida sobre a origem pela decisão posterior de encaminhamento baseada no destino.

**Como pensar:** pergunte qual localização o quadro acabou de demonstrar ao equipamento: a do emissor visto na porta de chegada.

**Referência:** [5. Endereço MAC](semana_02_estudo.md#s2-d2-mac), no item que estabelece que switches aprendem o MAC de origem observado na porta de entrada.

### Comentário S2D2Q064

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D2Q065

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. `255` fornece 8 bits, outro `255` mais 8 e `252` fornece 6: `8 + 8 + 6 = 22`.
- **B)** Incorreta. `/21` usaria 248 no terceiro octeto, com cinco bits 1.
- **C)** Incorreta. `/20` corresponderia a quatro bits 1 no terceiro octeto, cujo valor seria 240.
- **D)** Incorreta. `/23` exigiria sete bits 1 no terceiro octeto, isto é, 254.

**Conceito:** conversão de máscara decimal para prefixo CIDR.

**Pegadinha:** confundir os valores próximos 248, 252 e 254 no octeto interessante.

**Como pensar:** conte os bits 1 em cada octeto, usando `252 = 11111100`.

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

### Comentário S2D2Q066

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D2Q067

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta como escolha. `255.255.255.192` tem 26 bits 1 contíguos e é máscara válida.
- **B)** Correta. Em `255.255.240.128`, o terceiro octeto termina com zeros e o quarto reintroduz um bit 1.
- **C)** Incorreta como escolha. `255.248.0.0` representa `/13` e não volta a apresentar bits 1 após zeros.
- **D)** Incorreta como escolha. `255.255.254.0` representa `/23` com contiguidade preservada.

**Observação:** o comando pede a alternativa que NÃO representa uma máscara normal; por isso, B é o gabarito embora descreva a sequência inválida.

**Conceito:** contiguidade dos bits da máscara CIDR IPv4.

**Pegadinha:** o comando pede a sequência que NÃO representa máscara normal.

**Como pensar:** depois do primeiro zero, percorra o restante e rejeite qualquer ocorrência posterior de 1.

**Referência:** [7. Máscara de rede e prefixo CIDR](semana_02_estudo.md#s2-d2-mascara).

### Comentário S2D2Q068

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. `.64` inicia o bloco anterior, que termina em `.127`.
- **B)** Incorreta. `.190` é host válido, mas o broadcast tem todos os seis bits de host em 1 e vale `.191`.
- **C)** Correta. `/26` usa máscara final 192, bloco `256 - 192 = 64`; 158 está em 128–191.
- **D)** Incorreta. `.152` e `.159` não são as fronteiras de um bloco `/26`.

**Conceito:** cálculo de rede e broadcast pelo tamanho do bloco.

**Pegadinha:** usar o último host como broadcast ou ignorar o alinhamento em múltiplos de 64.

**Como pensar:** liste 0, 64, 128 e 192; escolha o início anterior a 158 e o endereço anterior ao próximo início.

**Referência:** [8. Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

### Comentário S2D2Q069

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D2Q070

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O final 191 pertence a um bloco maior que o `/20` informado.
- **B)** Incorreta. O início 168 não é múltiplo do bloco 16 exigido por `/20`.
- **C)** Incorreta. Zerar apenas o quarto octeto equivaleria ao raciocínio de `/24`.
- **D)** Correta. `/20` tem máscara `255.255.240.0`, incremento 16 no terceiro octeto; 173 cai em 160–175.

**Conceito:** cálculo de rede e broadcast quando a fronteira está no terceiro octeto.

**Pegadinha:** aplicar o incremento apenas ao último octeto por hábito.

**Como pensar:** identifique o octeto interessante, calcule `256 - 240 = 16` e delimite o bloco que contém 173.

**Referência:** [9. Exemplos de IPv4 e CIDR — Prefixo no terceiro octeto](semana_02_estudo.md#s2-d2-calculos).

### Comentário S2D2Q071

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D2Q072

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Os dois endereços do bloco podem identificar as duas extremidades do enlace compatível.
- **B)** Incorreta. Aplicar `2^h - 2` mecanicamente apagaria justamente a exceção do `/31` ponto a ponto.
- **C)** Incorreta. No contexto RFC 3021, `.11` não é tratado como broadcast convencional do enlace.
- **D)** Incorreta. Rota de um único host é a semântica de `/32`, não de `/31`.

**Conceito:** exceção do prefixo `/31` em enlace IPv4 ponto a ponto.

**Pegadinha:** generalizar a regra de rede e broadcast das sub-redes multiacesso.

**Como pensar:** antes da fórmula, verifique o contexto; `/31` só usa ambos os endereços na situação ponto a ponto compatível.

**Referência:** [9. Exemplos de IPv4 e CIDR — /31 ponto a ponto](semana_02_estudo.md#s2-d2-calculos).

### Comentário S2D2Q073

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** o prefixo fixa todos os 32 bits do IPv4 e seleciona exatamente o endereço `203.0.113.9`.
- **B)** o prefixo que deixa um bit disponível contém dois endereços e é `/31`, não `/32`.
- **C)** o intervalo de `.0` a `.255` corresponde a um bloco `/24`; `/32` não descreve todo esse bloco.
- **D)** não se aplicam rede, broadcast e faixa convencional de hosts quando a entrada seleciona um único endereço.

**Conceito:** semântica de `/32` como rota de host no IPv4.

**Pegadinha:** aplicar mecanicamente a subtração de rede e broadcast a um prefixo sem bits de host.

**Como pensar:** calcule quantos bits restam para variar; com `32 - 32 = 0`, há somente uma combinação possível.

**Referência:** [9. Exemplos de IPv4 e CIDR — /32](semana_02_estudo.md#s2-d2-calculos), especificamente o Exemplo F, que define `/32` como um endereço único ou rota de host.

### Comentário S2D2Q074

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D2Q075

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. `127.0.0.1` é apenas o exemplo mais conhecido, não o único endereço do bloco.
- **B)** Correta. IPv4 reserva todo o bloco `127/8`, e IPv6 define `::1/128` para loopback.
- **C)** Incorreta. Loopback representa o próprio host e não funciona como gateway para a Internet.
- **D)** Incorreta. `fe80::/10` é link-local; o loopback IPv6 é `::1`.

**Conceito:** endereços de loopback em IPv4 e IPv6.

**Pegadinha:** reduzir o bloco IPv4 inteiro ao endereço usual `127.0.0.1`.

**Como pensar:** diferencie comunicação interna do próprio host de alcance limitado ao enlace.

**Referência:** [10. Redes públicas, privadas e endereços especiais — Loopback](semana_02_estudo.md#s2-d2-publicos-privados-especiais).

### Comentário S2D2Q076

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** loopback IPv4 pertence a `127.0.0.0/8`; um endereço APIPA pode ser usado em quadros no enlace local.
- **B)** `169.254.0.0/16` não integra a RFC 1918 e não fornece automaticamente rota para redes externas.
- **C)** a autoconfiguração link-local pode sustentar comunicação no mesmo enlace, mas não cria acesso à Internet e costuma sinalizar falha do DHCP esperado.
- **D)** blocos de documentação possuem outras faixas, e APIPA não torna o endereço utilizável para acesso roteado externo.

**Conceito:** natureza, alcance e significado operacional de um endereço IPv4 link-local/APIPA.

**Pegadinha:** confundir link-local com loopback, endereço privado RFC 1918 ou endereço público provisório.

**Como pensar:** reconheça `169.254/16`, limite seu alcance ao enlace e relacione sua atribuição automática à ausência de resposta DHCP.

**Referência:** [10. Redes especiais — IPv4 link-local e APIPA](semana_02_estudo.md#s2-d2-publicos-privados-especiais), nos trechos sobre a faixa `169.254/16`, alcance local e autoconfiguração após falha de DHCP.

### Comentário S2D2Q077

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** o espaço IPv4 inclui diversas faixas de finalidade especial que não pertencem aos blocos privados.
- **B)** o papel de um endereço depende do prefixo e da destinação do bloco, não apenas do valor decimal final.
- **C)** excluir somente a RFC 1918 deixa passar loopback, link-local, documentação, multicast e outras reservas.
- **D)** o tamanho do prefixo, isoladamente, não determina se um bloco é público ou possui finalidade especial.

**Conceito:** diferença entre não pertencer à RFC 1918 e ser unicast público utilizável.

**Pegadinha:** transformar um teste necessário de não privacidade em prova suficiente de alcance global.

**Como pensar:** depois de excluir os blocos privados, verifique também o registro de endereços especiais antes de concluir que o endereço é público.

**Referência:** [10. Redes especiais — IPv4 público](semana_02_estudo.md#s2-d2-publicos-privados-especiais), especialmente a ressalva de que estar fora da RFC 1918 não prova utilização unicast pública.

### Comentário S2D2Q078

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D2Q079

**Nível:** Muito difícil

**Uso:** Aprofundamento
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

### Comentário S2D2Q080

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D2Q081

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D2Q082

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D2Q083

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** o ARP Request IPv4 usa broadcast de camada 2, não multicast, e a resposta solicitada normalmente é unicast.
- **B)** o gateway não é o próximo salto para um destino da mesma sub-rede, e devolver seu próprio MAC encaminharia o primeiro quadro ao dispositivo errado.
- **C)** a máscara mostra que B está no enlace local; A pergunta em broadcast quem possui `.80`, e B informa seu MAC normalmente por unicast.
- **D)** quem desconhece a associação inicia um Request; um Reply não substitui a pergunta nem precisa ser confirmado por outro Reply.

**Conceito:** decisão de localidade e sequência Request/Reply na resolução ARP para um vizinho IPv4.

**Pegadinha:** envolver o gateway em tráfego local ou trocar Request por Reply e broadcast por multicast.

**Como pensar:** compare primeiro os prefixos; sendo o destino local, procure seu próprio MAC com Request em broadcast e receba a resposta diretamente.

**Referência:** [13. ARP](semana_02_estudo.md#s2-d2-arp), especialmente a decisão entre destino local e remoto e o fluxo ARP Request em broadcast seguido normalmente por ARP Reply em unicast.

### Comentário S2D2Q084

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o servidor continua como destino IP, mas seu MAC não é alcançável nem resolvido por ARP através de roteadores.
- **B)** o host de origem não participa do enlace remoto e não precisa conhecer o MAC do roteador que fará a entrega final.
- **C)** um switch transparente encaminha o quadro com base no MAC de destino, mas seu próprio MAC não é usado como destino desse tráfego.
- **D)** como o servidor está fora de `192.168.10.0/24`, o primeiro quadro deve ser entregue ao gateway `192.168.10.1` no enlace local.

**Conceito:** resolução ARP do próximo salto quando o destino IP pertence a outra sub-rede.

**Pegadinha:** confundir o destino fim a fim do pacote IP com o destino local do primeiro quadro Ethernet.

**Como pensar:** determine a sub-rede antes do ARP; se o destino é remoto, procure o MAC do gateway configurado na interface local.

**Referência:** [13. ARP — Destino remoto](semana_02_estudo.md#s2-d2-arp), no trecho que determina a resolução do MAC do gateway ou próximo salto, e não do servidor remoto.

### Comentário S2D2Q085

**Nível:** Médio

**Uso:** Revisão
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta como resposta ao comando INCORRETA. ICMP não utiliza portas TCP ou UDP.
- **B)** Incorreta como escolha. Echo Request e Echo Reply são mensagens usadas pelo `ping`.
- **C)** Incorreta como escolha. Time Exceeded e Destination Unreachable pertencem ao conjunto de controle e erro.
- **D)** Incorreta como escolha. Bloqueio indiscriminado pode prejudicar diagnóstico e mecanismos necessários.

**Observação:** a questão pede a afirmação **INCORRETA**; por isso, A é o gabarito, pois ICMP não usa portas TCP ou UDP.

**Conceito:** função e transporte das mensagens ICMP.

**Pegadinha:** ignorar o comando negativo ou atribuir número de porta a todo protocolo conhecido.

**Como pensar:** procure a afirmação falsa e separe ICMP, integrado à camada Internet, de TCP e UDP.

**Referência:** [14. ICMP e ICMPv6](semana_02_estudo.md#s2-d2-icmp).

### Comentário S2D2Q086

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** uma NS pode ser enviada ao multicast solicited-node do alvo, e uma NA fornece a informação de vizinhança solicitada.
- **B)** RS e RA apoiam descoberta de roteadores e parâmetros do enlace, não a resolução comum do endereço de outro host.
- **C)** Echo Request e Echo Reply servem ao diagnóstico; não substituem as mensagens específicas do Neighbor Discovery.
- **D)** IPv6 não usa ARP para essa função e não possui broadcast equivalente ao ARP Request do IPv4.

**Conceito:** resolução de endereço de enlace pelo Neighbor Discovery baseado em ICMPv6.

**Pegadinha:** transportar integralmente o ARP do IPv4 para o IPv6 ou trocar NS/NA por outras duplas do ICMPv6.

**Como pensar:** associe resolução IPv6 a Neighbor Solicitation e Neighbor Advertisement, dentro do conjunto mais amplo de Neighbor Discovery.

**Referência:** [14. ICMPv6 — Neighbor Discovery, NS e NA](semana_02_estudo.md#s2-d2-icmp), nos trechos sobre resolução de endereço de enlace, multicast solicited-node e resposta Neighbor Advertisement.

### Comentário S2D2Q087

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D2Q088

**Nível:** Médio

**Uso:** Revisão
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

### Comentário S2D2Q089

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** X descreve destino individual, portanto é unicast, e não multicast.
- **B)** X não representa várias interfaces e Z não descreve destino individual fixo.
- **C)** unicast identifica uma interface, multicast entrega ao grupo e anycast seleciona uma entre as interfaces que compartilham o endereço.
- **D)** Y requer entrega aos participantes do grupo, enquanto Z requer seleção de uma entre várias interfaces.

**Conceito:** semântica de entrega dos endereços IPv6 unicast, multicast e anycast.

**Pegadinha:** confundir “mesmo endereço em várias interfaces” com entrega de uma cópia a todas elas.

**Como pensar:** associe as expressões “uma interface”, “grupo” e “uma dentre várias” a unicast, multicast e anycast, nessa ordem.

**Referência:** [15. IPv6 — Tipos de endereço](semana_02_estudo.md#s2-d2-ipv6), especialmente as definições de entrega a uma interface, a um grupo e a uma dentre várias interfaces.

### Comentário S2D2Q090

**Nível:** Médio

**Uso:** Revisão
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Eliminar o quarto grupo preservaria apenas 48 bits, não os 64 informados.
- **B)** Correta. Quatro grupos de 16 bits totalizam 64, resultando em `2001:db8:abcd:12ef::/64`.
- **C)** Incorreta. `/64` conserva integralmente `12ef`; não se zera sua parte final como em um prefixo menor.
- **D)** Incorreta. Preservar parte do quinto grupo ultrapassaria os 64 bits de prefixo.

**Conceito:** determinação de prefixo IPv6 em fronteira de grupo.

**Pegadinha:** aplicar lógica de máscara decimal pontuada ou contar grupos em vez de bits.

**Como pensar:** some `4 × 16 = 64`, mantenha os quatro primeiros grupos e zere a parte de interface; IPv6 usa prefixo, não máscara pontuada.

**Referência:** [15. IPv6 — Prefixo IPv6](semana_02_estudo.md#s2-d2-ipv6).

### Comentário S2D2Q091

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D2Q092

**Nível:** Muito difícil

**Uso:** Simulado
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Além da I, as afirmativas II e III também descrevem corretamente o escopo e a resolução de vizinho.
- **B)** Incorreta. A II também é verdadeira: a resolução inicial não consulta indiscriminadamente todos os nós.
- **C)** Incorreta. Excluir a I chamaria implicitamente de falsa uma distinção expressa entre multicast e broadcast.
- **D)** Correta. `ff02::1` é multicast link-local; NS usa solicited-node e o roteador respeita o limite desse escopo.

**Conceito:** multicast IPv6, escopo link-local e solicited-node no Neighbor Discovery.

**Pegadinha:** chamar `ff02::1` de broadcast ou supor que toda NS seja enviada a todos os nós do enlace.

**Como pensar:** verifique separadamente tipo de endereço, grupo de destino da NS e limite de encaminhamento do escopo 2.

**Referência:** [15. IPv6 — Escopo multicast](semana_02_estudo.md#s2-d2-ipv6) e [14. ICMPv6 — Neighbor Discovery](semana_02_estudo.md#s2-d2-icmp).

### Comentário S2D2Q093

**Nível:** Difícil

**Uso:** Simulado
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. `/27` deixa 5 bits e oferece apenas `2^5 - 2 = 30` hosts.
- **B)** Correta. São necessários 6 bits de host, pois `2^6 - 2 = 62 ≥ 50`; assim, o maior prefixo é `/26`, produzindo `2^(26-24) = 4` sub-redes.
- **C)** Incorreta. `/25` oferece 126 hosts, mas gera somente 2 sub-redes, não 4, e não maximiza a quantidade.
- **D)** Incorreta. `/28` fornece `2^4 - 2 = 14` hosts, muito abaixo de 50.

**Conceito:** escolha do prefixo a partir de requisito de hosts e maximização de sub-redes.

**Pegadinha:** selecionar um bloco que comporta os hosts, mas não usa o maior prefixo possível, ou confundir total com utilizável.

**Como pensar:** encontre o menor `h` com `2^h - 2 ≥ 50`; depois faça `32 - h` e conte os bits emprestados.

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

### Comentário S2D2Q094

**Nível:** Difícil

**Uso:** Simulado
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Embora `.32` seja fronteira `/27`, o bloco 32–63 está contido no `/26` já alocado, 0–63.
- **B)** Incorreta. `.144` não é múltiplo de 32; normalizá-lo levaria ao bloco 128–159, também ocupado.
- **C)** Incorreta. `.128/27` é exatamente um dos blocos já alocados.
- **D)** Correta. `.64/27` ocupa 64–95, respeita incremento 32 e não toca 0–63 nem 128–159.

**Conceito:** alinhamento e não sobreposição em VLSM.

**Pegadinha:** verificar apenas se o número inicial parece livre, sem testar a fronteira válida e toda a faixa do bloco.

**Como pensar:** liste os inícios `/27` em 0, 32, 64, 96, 128 e compare cada intervalo com as alocações existentes.

**Referência:** [11. Sub-redes e planejamento de prefixos](semana_02_estudo.md#s2-d2-subredes).

### Comentário S2D2Q095

**Nível:** Muito difícil

**Uso:** Simulado
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

### Comentário S2D2Q096

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D2Q097

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D2Q098

**Nível:** Muito difícil

**Uso:** Simulado
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

### Comentário S2D2Q099

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** um roteador não encaminha o pacote quando o TTL chega a zero, e a mensagem associada à expiração é Time Exceeded.
- **B)** o roteador não reinicia o TTL para prolongar indefinidamente o pacote, e ICMP Redirect possui outra finalidade.
- **C)** o pacote expirado é descartado, e o roteador pode notificar a origem com ICMP Time Exceeded, sem criar conexão ou recuperar os dados perdidos.
- **D)** Echo Reply responde a Echo Request e não ordena retransmissão automática de um pacote expirado.

**Conceito:** decremento do TTL, descarte no valor zero e possível notificação ICMP Time Exceeded.

**Pegadinha:** interpretar mensagens ICMP como mecanismos de encaminhamento, correção ou retransmissão automática.

**Como pensar:** siga a ordem: decrementar TTL, descartar se zerar e apenas então considerar a mensagem de erro enviada à origem.

**Referência:** [14. ICMP e ICMPv6](semana_02_estudo.md#s2-d2-icmp), especialmente os trechos sobre Time Exceeded, ausência de portas de transporte e inexistência de confiabilidade automática do IP.

### Comentário S2D2Q100

**Nível:** Muito difícil

**Uso:** Simulado
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A III também é verdadeira ao descrever o agrupamento das camadas superiores no TCP/IP.
- **B)** Incorreta. A I também é verdadeira: o roteador recria a unidade de enlace para o próximo salto.
- **C)** Correta. As três assertivas preservam camada, escopo e comparação didática dos modelos.
- **D)** Incorreta. I e II não contêm as trocas de camada ou de protocolo sugeridas pelos distratores usuais.

**Conceito:** integração entre roteamento, protocolos e comparação OSI/TCP/IP.

**Pegadinha:** exigir correspondência rígida entre modelos ou imaginar que o mesmo quadro cruza toda a rota.

**Como pensar:** valide cada plano separadamente: quadro no enlace, IP/ICMP na Internet e funções superiores na Aplicação TCP/IP.

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip), [3. Encapsulamento](semana_02_estudo.md#s2-d2-encapsulamento) e [ARP](semana_02_estudo.md#s2-d2-arp).

#### Comentário Extra Dia 2.1
**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** Incorreta. Eficiência busca bons resultados e uso adequado de recursos, mas não autoriza afastar a lei.
- **B)** Incorreta. Para a Administração, legalidade não significa liberdade geral de fazer o que não foi proibido.
- **C)** Incorreta. Publicidade posterior não sana, por si, uma atuação contrária ao ordenamento.
- **D)** Correta. Legalidade exige atuação conforme o ordenamento e dentro da competência, mesmo quando outro caminho pareça mais rápido.

**Conceito:** convivência entre legalidade e eficiência no art. 37.

**Pegadinha:** transformar eficiência em autorização para escolher resultado acima da norma.

**Como pensar:** verifique primeiro se a atuação é juridicamente permitida; só depois compare qualidade, custo e velocidade.

**Referência:** [Revisão de Administração Pública — Princípios do art. 37](semana_02_estudo.md#s2-d2-revisao-principios).

#### Comentário Extra Dia 2.2
**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Essenciais

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

**Nível:** Médio

**Uso:** Essenciais

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

**Nível:** Médio

**Uso:** Essenciais

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
**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** Incorreta. Autarquia não é modalidade de empresa pública nem depende de capital privado.
- **B)** Incorreta. Órgão sem personalidade não é autarquia, e exploração econômica não é a função descrita no núcleo.
- **C)** Incorreta. Autarquia pertence à Administração Indireta, não surge como associação privada livre.
- **D)** Correta. A definição reúne personalidade de direito público, criação por lei e atividade administrativa típica.

**Conceito:** definição de autarquia.

**Pegadinha:** misturar características de órgão, empresa estatal e associação numa única definição.

**Como pensar:** procure o trio “direito público, criada por lei, atividade administrativa típica”.

**Referência:** [Revisão de Administração Pública — Administração Direta e Indireta](semana_02_estudo.md#s2-d2-revisao-organizacao).

#### Comentário Extra Dia 2.6
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Aprofundamento

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

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** torna absolutos os dois atributos e ignora tanto a contestabilidade quanto os limites da execução direta.
- **B)** acerta a condição da autoexecutoriedade, mas transforma a presunção relativa em impedimento absoluto de contestação.
- **C)** acerta a possibilidade de prova contrária, mas estende autoexecutoriedade a todo ato sem a condição necessária.
- **D)** a presunção é relativa e pode ser afastada, enquanto a execução direta exige autorização legal ou urgência.

**Conceito:** limites distintos da presunção de legitimidade e da autoexecutoriedade.

**Pegadinha:** acertar um dos dois atributos e aceitar a mesma alternativa sem conferir a segunda regra.

**Como pensar:** resolva como matriz de dois testes: a presunção é relativa e a execução direta não acompanha automaticamente todo ato.

**Referência:** [Elementos e atributos do ato administrativo](semana_02_estudo.md#s2-d2-revisao-atos), nos trechos sobre presunção relativa e hipóteses de autoexecutoriedade.

#### Comentário Extra Dia 2.8
**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Aprofundamento

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

**Nível:** Difícil

**Uso:** Aprofundamento

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

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** para atos favoráveis, a lei prevê decadência quinquenal quando não há má-fé comprovada.
- **B)** o ato I já ultrapassou cinco anos, mas no benefício contínuo o marco específico é o primeiro pagamento, ocorrido em dezembro.
- **C)** em setembro de 2025 já passaram cinco anos desde agosto de 2020, mas ainda não desde o primeiro pagamento de dezembro de 2020.
- **D)** inverte os resultados e usa prazo e termo inicial que não correspondem ao art. 54 estudado.

**Conceito:** decadência do direito de anular e termo inicial específico para efeitos patrimoniais contínuos.

**Pegadinha:** contar todos os casos da prática do ato, usar o último pagamento ou ignorar a ressalva de má-fé.

**Como pensar:** confirme boa-fé, identifique o tipo de efeito, escolha o marco correto e só então conte os cinco anos em cada caso.

**Referência:** [Anulação, revogação e convalidação](semana_02_estudo.md#s2-d2-revisao-desfazimento), no parágrafo sobre prazo de cinco anos, má-fé e primeiro pagamento em efeitos patrimoniais contínuos.

#### Comentário Extra Dia 2.11

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** publicidade não elimina finalidade, necessidade e proteção quando o documento contém dados pessoais.
- **B)** dado pessoal exige tratamento adequado, mas não transforma automaticamente todo o documento público em conteúdo inacessível.
- **C)** as duas leis podem incidir de forma harmônica, e a escolha não depende de preferência administrativa.
- **D)** a análise preserva a transparência cabível e limita somente a exposição pessoal sem fundamento ou necessidade.

**Conceito:** aplicação compatível da LAI e da LGPD em documento público com dados pessoais.

**Pegadinha:** resolver a convivência normativa por um absoluto, divulgação total ou sigilo total.

**Como pensar:** identifique o acesso público devido e, dentro dele, separe o dado pessoal que precisa de proteção proporcional.

**Referência:** [LAI x LGPD](semana_02_estudo.md#s2-d2-revisao-lai-lgpd), especialmente a convivência entre acesso devido e proteção de dados pessoais.

#### Comentário Extra Dia 2.12
**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Revisão

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
**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** Correta. Inviabilidade de competição caracteriza o núcleo da inexigibilidade, observados os requisitos legais.
- **B)** Incorreta. Pregão é modalidade, e exclusividade não é critério de julgamento.
- **C)** Incorreta. Retirar uma licitação não elimina processo, motivação e controle da contratação.
- **D)** Incorreta. Na dispensa, a competição é possível em tese, embora a lei autorize contratação direta.

**Conceito:** distinção entre dispensa e inexigibilidade.

**Pegadinha:** chamar toda contratação direta de dispensa.

**Como pensar:** pergunte se existe competição viável; se não existe, examine inexigibilidade, sem dispensar o processo.

**Referência:** [Revisão de Administração Pública — Licitação e contratação direta](semana_02_estudo.md#s2-d2-revisao-licitacao).

#### Comentário Extra Dia 2.14

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** contratação direta não elimina o processo, e pregão e diálogo competitivo não são critérios de julgamento.
- **B)** acerta a necessidade de instrução, mas erra ao retirar os dois institutos do rol de modalidades.
- **C)** preserva tanto os requisitos processuais da contratação direta quanto a classificação legal de pregão e diálogo competitivo.
- **D)** acerta a classificação dos institutos, mas erra ao dispensar instrução e controle da contratação direta.

**Conceito:** distinção entre contratação direta, modalidade e critério de julgamento.

**Pegadinha:** resolver corretamente uma das proposições e deixar de testar a classificação apresentada na outra.

**Como pensar:** avalie as proposições separadamente: contratação direta mantém processo; pregão e diálogo competitivo são modalidades.

**Referência:** [Licitação e contratação direta](semana_02_estudo.md#s2-d2-revisao-licitacao), nos trechos sobre instrução da contratação direta e modalidades da Lei nº 14.133/2021.

#### Comentário Extra Dia 2.15

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** a responsabilidade estatal perante a vítima é objetiva, e o regresso não dispensa dolo ou culpa do agente.
- **B)** acerta a condição subjetiva do regresso, mas responsabilidade objetiva não elimina dano nem nexo causal.
- **C)** acerta os elementos da pretensão da vítima, mas transforma indevidamente o regresso em responsabilidade objetiva do agente.
- **D)** a vítima demonstra conduta estatal, dano e nexo sem provar culpa do Estado, e o regresso exige dolo ou culpa do agente.

**Conceito:** diferença entre responsabilidade objetiva perante a vítima e responsabilidade subjetiva na ação regressiva.

**Pegadinha:** retirar dano e nexo por causa da palavra “objetiva” ou transportar essa objetividade para o regresso.

**Como pensar:** resolva em duas relações: vítima contra Estado sem prova de culpa; Estado contra agente somente com dolo ou culpa.

**Referência:** [Responsabilidade civil do Estado](semana_02_estudo.md#s2-d2-revisao-responsabilidade), nos trechos sobre requisitos perante a vítima e regresso em caso de dolo ou culpa.

#### Comentário Extra Dia 2.16

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** troca possibilidade por obrigação e estende a afirmação a qualquer rede, removendo o contexto expresso.
- **B)** conserva o recorte dos enlaces ponto a ponto e a modalidade de possibilidade indicada por “pode”.
- **C)** mantém o contexto, mas inverte a força modal; “pode” não expressa proibição.
- **D)** generaliza para toda implementação e cria um dever que não aparece no enunciado.

**Conceito:** preservação de contexto e modalidade verbal na interpretação técnica.

**Pegadinha:** corrigir um dos dois filtros e ainda trocar “pode” por “deve” ou retirar a condição ponto a ponto.

**Como pensar:** sublinhe primeiro o recorte contextual e depois classifique a força do verbo antes de comparar as paráfrases.

**Referência:** [Quantificadores e alcance](semana_02_estudo.md#s2-d2-revisao-quantificadores), especialmente a diferença entre possibilidade, obrigação e recorte ponto a ponto.

#### Comentário Extra Dia 2.17
**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. Há ressalva entre maior espaço e manutenção do planejamento, com retomada coesiva adequada.
- **B)** Incorreta. O conector não conclui; o pronome retoma a ampliação, não o planejamento.
- **C)** Incorreta. “Entretanto” não indica causa, e “esse” recupera conteúdo anterior.
- **D)** Incorreta. O trecho afirma expressamente que a necessidade não foi eliminada.

**Conceito:** coesão referencial e relação adversativa.

**Pegadinha:** ler apenas a primeira oração e ignorar a negação introduzida após o conector.

**Como pensar:** identifique o valor de “entretanto” e substitua “esse fato” por seu antecedente para testar o sentido.

**Referência:** [Revisão de Português — Coesão e relação lógica](semana_02_estudo.md#s2-d2-revisao-coesao).

#### Comentário Extra Dia 2.18
**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A vírgula separa indevidamente o sujeito “Os endereços privados” do verbo “podem”.
- **B)** Correta. As vírgulas isolam a expressão explicativa “no IPv4 sobre Ethernet”.
- **C)** Incorreta. A vírgula foi posicionada entre a negação e o verbo, sem função sintática legítima.
- **D)** Incorreta. A vírgula rompe o vínculo entre “encaminha” e seu complemento “destinos remotos”.

**Conceito:** pontuação de termos essenciais e expressões explicativas.

**Pegadinha:** inserir vírgula onde ocorre pausa oral, mesmo separando sujeito, verbo ou complemento.

**Como pensar:** preserve primeiro o esqueleto sujeito–verbo–complemento e isole apenas o trecho explicativo removível.

**Referência:** [Revisão de Português — Pontuação](semana_02_estudo.md#s2-d2-revisao-pontuacao).

#### Comentário Extra Dia 2.19
**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

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

**Nível:** Difícil

**Uso:** Simulado

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

### S2D3Q101 — Porta de transporte, demultiplexação e identificação de sockets

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Protocolo, serviço, porta e socket](semana_02_estudo.md#s2-d3-protocolo-porta), especialmente os parágrafos sobre demultiplexação e a quíntupla de uma conexão TCP.

Um servidor mantém várias aplicações de rede e recebe um segmento TCP destinado à porta 443. A respeito da entrega ao processo correto e da identificação da conexão, assinale a alternativa correta.

A) A porta de destino participa da demultiplexação, e a conexão TCP é distinguida pelos endereços e portas das duas extremidades e pelo protocolo.

B) A porta de destino identifica o host na Internet, e a conexão TCP é distinguida apenas pelo endereço IP utilizado pelo cliente.

C) A porta de origem identifica sempre o processo servidor, e a conexão TCP é distinguida apenas pelas duas portas de transporte envolvidas.

D) A porta de destino identifica o conteúdo da aplicação, e a conexão TCP é distinguida apenas pelo protocolo de transporte empregado.

### S2D3Q102 — Alcance da confiabilidade e das confirmações do TCP

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2.1 TCP: orientado à conexão e confiável](semana_02_estudo.md#s2-d3-tcp-udp).

Em uma compra realizada por meio de uma aplicação web, o cliente recebe um ACK TCP após enviar dados. Esse ACK significa que:

A) o TCP dispensou o estabelecimento de conexão antes do envio de dados.
B) a aplicação preservará obrigatoriamente as fronteiras de cada mensagem enviada.
C) o transporte confirmou o recebimento de bytes, mas não a aprovação semântica da compra pela aplicação.
D) o servidor concluiu que o usuário está autorizado a realizar a operação.

### S2D3Q103 — Características do UDP e responsabilidades da aplicação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [2.2 UDP: datagramas sem conexão](semana_02_estudo.md#s2-d3-tcp-udp), especialmente a lista de garantias não oferecidas nativamente e o parágrafo sobre mecanismos implementados pela aplicação.

Uma aplicação de telemetria envia datagramas por UDP e pretende acrescentar confirmações e reenvio seletivo em seu próprio protocolo. Considerando a divisão de responsabilidades entre transporte e aplicação, assinale a alternativa correta.

A) O UDP já ordena e retransmite os datagramas, de modo que a aplicação só pode definir o formato das mensagens trocadas.

B) O UDP impede confirmações na camada de aplicação, pois cada datagrama deve permanecer independente dos datagramas anteriores.

C) O UDP confirma a entrega sem ordenar os datagramas, e a aplicação pode implementar ordenação, mas não retransmissão.

D) O UDP não fornece conexão, confirmação nem retransmissão nativas, mas a aplicação pode implementar esses mecanismos sobre os datagramas.

### S2D3Q104 — Ausência de estado obrigatório no protocolo HTTP

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [3.1 HTTP](semana_02_estudo.md#s2-d3-http-https), no parágrafo que define stateless e cita cookies, tokens e sessões no servidor.

Uma aplicação web usa um cookie de sessão para relacionar requisições sucessivas do mesmo usuário. Essa implementação é compatível com a descrição do HTTP como stateless porque:

A) o servidor fica proibido de armazenar dados de sessão, mas o navegador pode manter qualquer estado necessário à aplicação.

B) cada conexão TCP admite uma única requisição, embora várias conexões possam compartilhar o mesmo cookie de sessão.

C) o cookie torna o protocolo de transporte stateful, sem que o servidor precise interpretar as requisições recebidas.

D) cada requisição possui semântica própria no HTTP, embora a aplicação possa correlacioná-las por cookies, tokens ou estado no servidor.

### S2D3Q105 — Garantias e limites do HTTPS

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [3.2 HTTPS](semana_02_estudo.md#s2-d3-http-https), incluindo as garantias do TLS em trânsito e a lista de garantias que não decorrem do HTTPS.

Um usuário acessa um portal por HTTPS, e o navegador valida corretamente o certificado apresentado pelo servidor. Qual conclusão é tecnicamente adequada?

A) O canal protegido comprova que as informações publicadas são verdadeiras e que a aplicação não contém vulnerabilidades exploráveis.

B) O TLS protege dados em trânsito e auxilia a autenticar o servidor, mas não substitui autorização nem correções de segurança da aplicação.

C) O certificado validado comprova que o usuário pode acessar todos os recursos e que seu dispositivo está livre de software malicioso.

D) A sessão HTTPS fornece criptografia ponta a ponta do conteúdo armazenado e impede a observação de todos os metadados de rede.

### S2D3Q106 — Métodos HTTP e classes de códigos de estado

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [3.1 HTTP](semana_02_estudo.md#s2-d3-http-https).

Sobre métodos e respostas HTTP, assinale a alternativa correta.

A) HEAD solicita os cabeçalhos de uma representação sem o corpo da resposta.
B) POST é reservado exclusivamente para obter uma representação, sem submeter dados.
C) Códigos 4xx indicam, necessariamente, falha interna do servidor.
D) Códigos 3xx significam sempre que o recurso foi removido definitivamente.

### S2D3Q107 — Tipos de registros DNS

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [4.3 Registros frequentes](semana_02_estudo.md#s2-d3-dns).

No DNS, qual registro indica os servidores de correio de um domínio?

A) A
B) AAAA
C) MX
D) CNAME

### S2D3Q108 — Consulta recursiva, iteração, cache e TTL no DNS

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [4.2 Recursão, iteração e cache](semana_02_estudo.md#s2-d3-dns).

Uma estação envia uma consulta recursiva ao seu resolvedor DNS. Nessa situação, é correto afirmar que o resolvedor:

A) só pode responder depois de consultar diretamente todos os servidores autoritativos da Internet.
B) devolve ao cliente apenas a lista de servidores raiz, sem buscar resposta.
C) pode responder com dados válidos do cache, respeitado o TTL, ou buscar a resposta final usando referências iterativas.
D) transforma automaticamente qualquer registro A em um registro MX.

### S2D3Q109 — Transportes do DNS clássico

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [4.4 Transportes do DNS clássico](semana_02_estudo.md#s2-d3-dns), nos trechos que registram 53/UDP, 53/TCP e o uso de TCP em transferências de zona.

Um firewall permite consultas DNS em 53/UDP, mas uma transferência de zona entre servidores autoritativos não é concluída. Qual explicação deve orientar a revisão da regra?

A) Transferências de zona usam datagramas em 53/UDP, e a falha indica necessariamente bloqueio de fragmentos IP pelo firewall.

B) Transferências de zona usam DNS sobre TLS em 853/TCP, ainda que nenhum transporte DNS criptografado tenha sido configurado.

C) O TCP é reservado ao DNS sobre HTTPS em 443/TCP, enquanto todo intercâmbio do DNS clássico permanece em 53/UDP.

D) O DNS clássico também usa 53/TCP, inclusive em transferências de zona, por isso permitir apenas 53/UDP é insuficiente.

### S2D3Q110 — DNS sobre TLS e DNS sobre HTTPS

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [4.4 Transportes do DNS clássico](semana_02_estudo.md#s2-d3-dns), no parágrafo final que contrasta DNS clássico, DoT em 853 e DoH sobre HTTPS.

Uma política de saída deve distinguir DNS sobre TLS (DoT) de DNS sobre HTTPS (DoH) pelas convenções usuais de transporte. Assinale a associação correta.

A) DoT utiliza TLS em 53/TCP, enquanto DoH utiliza HTTP sem TLS em 853/TCP.

B) DoT utiliza HTTPS em 443/TCP, enquanto DoH utiliza TLS diretamente em 853/TCP.

C) DoT utiliza TLS em 853/TCP, enquanto DoH utiliza HTTPS, normalmente na porta 443.

D) DoT e DoH utilizam exclusivamente 53/UDP, diferenciando-se apenas pelo formato da consulta.

### S2D3Q111 — Sequência inicial de concessão DHCP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5.1 Sequência DORA](semana_02_estudo.md#s2-d3-dhcp).

Um cliente sem configuração de rede inicia a obtenção dinâmica de parâmetros por DHCP. A sequência clássica DORA é:

A) DHCPDISCOVER, DHCPOFFER, DHCPREQUEST e DHCPACK.
B) DHCPREQUEST, DHCPACK, DHCPDISCOVER e DHCPOFFER.
C) DHCPOFFER, DHCPDISCOVER, DHCPACK e DHCPREQUEST.
D) DHCPDISCOVER, DHCPACK, DHCPOFFER e DHCPREQUEST.

### S2D3Q112 — Portas e transporte do DHCP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5. DHCP — atribuição dinâmica de configuração](semana_02_estudo.md#s2-d3-dhcp), na lista de portas clássicas imediatamente após a sequência DORA.

Na captura da obtenção inicial de configuração por DHCPv4, considere as portas clássicas atribuídas ao cliente e ao servidor. Qual fluxo está corretamente descrito?

A) O cliente envia de 67/UDP para 68/UDP, e o servidor responde de 68/UDP para 67/UDP.

B) O cliente envia de 68/UDP para 67/UDP, e o servidor responde de 67/UDP para 68/UDP.

C) O cliente envia de 68/TCP para 67/TCP, e o servidor responde de 67/TCP para 68/TCP.

D) O cliente envia de 67/TCP para 68/TCP, e o servidor responde de 68/TCP para 67/TCP.

### S2D3Q113 — Uso de DHCP relay entre segmentos roteados

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [5.1 Sequência DORA — DHCP relay](semana_02_estudo.md#s2-d3-dhcp), especialmente a explicação de que o relay encaminha mensagens entre segmentos e viabiliza o servidor central.

Um servidor DHCP central está na VLAN 10, e os clientes da VLAN 20 iniciam o DORA por broadcast. O roteamento entre as VLANs funciona, mas não se deseja estender o domínio de broadcast. Qual configuração atende ao cenário e permite selecionar o escopo correto?

A) Configurar o relay apenas na interface da VLAN 10 e manter para os clientes da VLAN 20 o mesmo escopo usado pelos servidores.

B) Encaminhar o broadcast por uma ponte entre as VLANs e escolher o escopo exclusivamente pelo endereço MAC de cada estação cliente.

C) Aplicar tradução de endereço na interface da VLAN 20 e selecionar para todos os pedidos um único escopo baseado no endereço traduzido.

D) Configurar o relay na interface de camada 3 da VLAN 20 e manter no servidor um escopo compatível com a rede desses clientes.

### S2D3Q114 — Divisão de funções entre SMTP, POP3 e IMAP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [6. Correio eletrônico: SMTP, POP3 e IMAP](semana_02_estudo.md#s2-d3-email), incluindo as subseções 6.1 a 6.4 sobre envio e acesso à caixa postal.

Em uma arquitetura convencional de correio eletrônico, é necessário distinguir o envio da mensagem do acesso posterior à caixa postal. Assinale a distribuição correta das funções.

A) POP3 realiza submissão e transferência entre servidores, enquanto SMTP e IMAP realizam acesso à caixa postal.

B) SMTP realiza submissão e transferência entre servidores, enquanto POP3 e IMAP realizam acesso à caixa postal.

C) IMAP realiza submissão e transferência entre servidores, enquanto SMTP e POP3 realizam acesso à caixa postal.

D) POP3 realiza transferência entre servidores e acesso sincronizado, enquanto IMAP realiza submissão pelo cliente.

### S2D3Q115 — Portas de submissão e transferência SMTP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [6.1 SMTP](semana_02_estudo.md#s2-d3-email), na lista de portas 25/TCP, 587/TCP e 465/TCP e seus respectivos papéis.

Uma organização separará a submissão autenticada feita pelos clientes da transferência SMTP realizada entre seus servidores de correio e outros MTAs. Qual configuração segue as convenções usuais?

A) Reservar 25/TCP à submissão autenticada dos clientes e 587/TCP exclusivamente à transferência entre MTAs.

B) Reservar 465/TCP à transferência entre MTAs e iniciar STARTTLS obrigatório depois de abrir o canal com TLS implícito.

C) Usar tipicamente 587/TCP para submissão pelos clientes e 25/TCP para transferência de mensagens entre MTAs.

D) Usar 25/UDP para transferência entre MTAs e 587/UDP para submissão autenticada pelos clientes.

### S2D3Q116 — Modelo de acesso e sincronização do IMAP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [6.3 IMAP](semana_02_estudo.md#s2-d3-email).

Um usuário precisa ler suas mensagens no telefone e no notebook, mantendo pastas e marcações sincronizadas no servidor. O protocolo mais adequado é:

A) IMAP.
B) SMTP.
C) FTP.
D) Telnet.

### S2D3Q117 — Fluxo integrado de submissão, transferência e acesso ao e-mail

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [6.4 Fluxo integrado de e-mail](semana_02_estudo.md#s2-d3-email), em conjunto com [6.3 IMAP](semana_02_estudo.md#s2-d3-email).

Uma usuária envia uma mensagem pelo serviço de sua organização. Mais tarde, acessa a caixa postal pelo telefone e pelo notebook, mantendo pastas e marcações sincronizadas. Qual combinação atende às duas etapas?

A) SMTP para submissão e acesso à caixa postal; POP3 para sincronização de pastas entre os clientes.

B) POP3 para submissão e transferência da mensagem; SMTP para acesso sincronizado à caixa postal.

C) IMAP para submissão e transferência da mensagem; POP3 para acesso sincronizado à caixa postal.

D) SMTP para submissão e transferência da mensagem; IMAP para acesso sincronizado à caixa postal.

### S2D3Q118 — Arquitetura de canais e modos do FTP

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [7.1 FTP](semana_02_estudo.md#s2-d3-transferencia-remota), nos parágrafos sobre conexão de controle, conexão de dados e porta informada pelo servidor no modo passivo.

Em um servidor FTP, o login e os comandos funcionam, mas listagens e transferências falham no modo passivo. O firewall libera somente 21/TCP. Qual diagnóstico e ajuste são coerentes com a arquitetura do protocolo?

A) Controle e dados compartilham 21/TCP; deve-se apenas ampliar o tempo limite da conexão já liberada no firewall.

B) Controle e dados usam conexões separadas; deve-se permitir ao cliente alcançar a faixa passiva anunciada pelo servidor.

C) Dados usam uma sessão UDP negociada pelo controle; deve-se liberar portas UDP altas em ambos os sentidos.

D) Dados partem sempre de 20/TCP no servidor; deve-se permitir essa origem mesmo quando foi negociado o modo passivo.

### S2D3Q119 — Funcionamento do modo passivo do FTP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7.1 FTP](semana_02_estudo.md#s2-d3-transferencia-remota), especificamente a descrição do modo passivo e da conexão de dados iniciada pelo cliente.

Depois de solicitar modo passivo em uma sessão FTP, o cliente recebe do servidor o endereço e a porta destinados à transferência. O que deve ocorrer em seguida?

A) O servidor inicia outra conexão TCP, usando 20 como origem e a porta recebida do cliente como destino.

B) O cliente inicia outra conexão TCP para o endereço e a porta informados pelo servidor, mantendo o canal de controle.

C) O servidor reutiliza a conexão de controle para os dados e separa internamente comandos e conteúdo transferido.

D) O cliente aguarda que o servidor abra a conexão de dados para sua porta de origem usada no controle.

### S2D3Q120 — Negociação e proteção dos canais no FTPS explícito

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [7.2 FTPS](semana_02_estudo.md#s2-d3-transferencia-remota), no parágrafo sobre FTPS explícito, `AUTH TLS`, `PBSZ 0`, `PROT P` e `PROT C`.

Uma política exige FTPS explícito e confidencialidade tanto no canal de controle quanto nas conexões de dados. Qual sequência atende ao requisito antes da transferência?

A) Abrir 22/TCP, enviar `AUTH TLS`, negociar o controle e selecionar `PROT C` para proteger os dados.

B) Abrir 990/TCP com TLS implícito, enviar `AUTH TLS` e selecionar `PBSZ 1` antes de `PROT P`.

C) Abrir 21/TCP, enviar `AUTH TLS`, negociar TLS e então enviar `PBSZ 0` seguido de `PROT P`.

D) Abrir 21/TCP, enviar `PROT P` antes de negociar TLS e deixar `AUTH TLS` para depois dos dados.

### S2D3Q121 — FTPS implícito, portas registradas e separação dos canais

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [7.2 FTPS](semana_02_estudo.md#s2-d3-transferencia-remota), nos parágrafos sobre FTPS implícito, registros 990/989 e negociação de portas nos modos ativo e passivo; e [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas).

Ao publicar um serviço FTPS implícito atrás de firewall, a equipe considera as portas registradas e a arquitetura herdada do FTP. Qual afirmação está correta?

A) O TLS começa na abertura do controle em 990/TCP, mas conexões de dados continuam separadas e podem usar portas negociadas.

B) FTPS implícito começa em 21/TCP com `AUTH TLS`, e toda conexão de dados deve usar obrigatoriamente 989/TCP.

C) FTPS implícito é um subsistema SSH em 22/TCP e transporta controle e dados pela mesma conexão criptografada.

D) O TLS começa na abertura do controle em 990/TCP, e todos os dados trafegam dentro dessa mesma conexão de controle.

### S2D3Q122 — SFTP como protocolo de arquivos sobre SSH

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7.3 SFTP](semana_02_estudo.md#s2-d3-transferencia-remota), especialmente a definição como SSH File Transfer Protocol e a regra “SFTP não é FTP sobre TLS”.

Uma automação precisa transferir arquivos aproveitando o serviço SSH e as chaves públicas já administradas nos servidores. Qual descrição identifica corretamente o SFTP nesse cenário?

A) É um protocolo de transferência sobre SSH, normalmente em 22/TCP, que pode reutilizar a autenticação oferecida pelo SSH.

B) É o FTP com TLS explícito, normalmente em 21/TCP, que reutiliza diretamente as chaves públicas cadastradas no SSH.

C) É o FTP com TLS implícito, normalmente em 990/TCP, que transforma certificados TLS em chaves de autenticação SSH.

D) É uma modalidade de FTPS que usa 22/TCP no controle e mantém conexões FTP separadas para transportar os dados.

### S2D3Q123 — Administração remota segura com SSH

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7.4 SSH](semana_02_estudo.md#s2-d3-transferencia-remota), incluindo os serviços oferecidos pelo SSH e os cuidados com chave do host e chaves privadas.

Um administrador precisa executar comandos em um servidor remoto por um canal com autenticação, integridade e confidencialidade. Qual solução e cuidado operacional atendem diretamente ao requisito?

A) Usar Telnet em 23/TCP e confiar na senha do usuário para cifrar toda a sessão de terminal.

B) Usar SFTP em 22/TCP e tratar o subsistema de arquivos como uma sessão interativa de comandos do sistema.

C) Usar FTPS em 990/TCP e transportar os comandos do terminal pelo canal de controle do protocolo de arquivos.

D) Usar SSH em 22/TCP, validar a chave do host e proteger as chaves privadas empregadas na autenticação.

### S2D3Q124 — Função, porta e limitação de segurança do Telnet

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7.5 Telnet](semana_02_estudo.md#s2-d3-transferencia-remota), que o define como terminal remoto em 23/TCP sem a proteção criptográfica esperada.

Durante o inventário, foi encontrado um equipamento legado que oferece Telnet sem túnel ou proteção adicional. Qual descrição combina corretamente função, transporte e limitação desse serviço?

A) Oferece terminal remoto em 23/TCP e cifra nativamente credenciais e conteúdo após a autenticação do usuário.

B) Oferece transferência de arquivos em 23/TCP e protege somente as credenciais, mantendo o conteúdo em claro.

C) Oferece terminal remoto em 23/TCP e não fornece proteção criptográfica nativa para credenciais e conteúdo.

D) Oferece terminal remoto em 23/UDP e garante integridade das mensagens, mas não confidencialidade do conteúdo.

### S2D3Q125 — Gerente, agente, MIB, OID e notificações SNMP

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp), nos trechos que definem gerente, agente, MIB, OID, GET, TRAP e INFORM.

Uma plataforma central consulta periodicamente o contador de interfaces dos roteadores e também recebe avisos espontâneos quando um enlace muda de estado. No modelo SNMP, qual descrição dos papéis e operações está correta?

A) O agente envia operações GET ao gerente, que localiza cada contador em sua própria MIB e responde com uma trap.

B) O gerente consulta no agente objetos identificados por OID, e o agente pode enviar uma trap ao gerente quando ocorre um evento.

C) O gerente expõe os objetos da MIB aos agentes, que alteram os contadores remotos por GET e confirmam cada leitura com trap.

D) O agente consulta objetos por OID no gerente, enquanto o gerente usa trap como pedido confirmado de leitura ao equipamento.

### S2D3Q126 — Portas tradicionais e níveis de proteção do SNMP

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp), nos trechos sobre 161/UDP, 162/UDP e proteção das versões; e [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas).

Uma equipe configurará consultas periódicas aos agentes e recebimento de notificações pelo gerente, com autenticação e privacidade quando suportadas. Qual desenho está tecnicamente correto?

A) Agentes recebem consultas em 162/TCP, o gerente recebe traps em 161/TCP, e SNMPv2c fornece autenticação e privacidade obrigatórias.

B) Agentes recebem consultas em 161/UDP, o gerente recebe traps em 162/UDP, e SNMPv2c fornece proteção equivalente ao SNMPv3 configurado.

C) Agentes recebem consultas em 162/UDP, o gerente recebe traps em 161/UDP, e SNMPv3 fornece privacidade sem qualquer possibilidade de autenticação.

D) Agentes recebem consultas em 161/UDP, o gerente recebe notificações em 162/UDP, e SNMPv3 pode fornecer autenticação e privacidade conforme configurado.

### S2D3Q127 — Estrutura e operações de um diretório LDAP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [9. LDAP — acesso a diretórios](semana_02_estudo.md#s2-d3-ldap), na definição de hierarquia, DN, atributos e operações bind e search.

Um cliente LDAP precisa localizar a entrada de uma servidora em um diretório corporativo e ler seus atributos. Qual descrição dos elementos e das operações está correta?

A) O DN identifica apenas a conexão com o servidor, e a operação bind devolve todas as entradas abaixo da raiz pesquisada.

B) O DN identifica um atributo isolado, e a operação search autentica o cliente antes de remover a entrada encontrada.

C) O DN identifica uma entrada na hierarquia, seus dados são atributos, e operações como bind e search integram o LDAP.

D) O DN identifica o esquema inteiro do diretório, e a operação bind altera atributos enquanto search negocia o canal TLS.

### S2D3Q128 — Proteção do LDAP e distinção entre autenticação e autorização

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [9. LDAP — acesso a diretórios](semana_02_estudo.md#s2-d3-ldap), especialmente os parágrafos sobre 389/STARTTLS, 636/LDAPS e participação do diretório em autenticação sem concentrar toda autorização.

Uma aplicação valida a identidade de usuários em um diretório LDAP, mas mantém localmente os papéis que autorizam cada operação. A conexão ao diretório também deve ser protegida. Qual afirmação está correta?

A) LDAP pode participar da autenticação sem decidir toda autorização; 389/TCP admite STARTTLS e 636/TCP é usual no LDAPS.

B) Um bind bem-sucedido concede autorização total na aplicação; 389/TCP fornece TLS implícito sem negociação adicional.

C) O diretório deve decidir todos os papéis da aplicação; 636/UDP é o único transporte protegido permitido pelo LDAP.

D) STARTTLS transforma autenticação em autorização automática; LDAPS usa 389/TCP após o cliente validar a conta existente.

### S2D3Q129 — Proxy direto

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [10.1 Proxy direto](semana_02_estudo.md#s2-d3-proxy).

Em uma rede corporativa, um componente recebe solicitações dos navegadores dos empregados e aplica política de navegação, autenticação e cache em nome desses clientes. Esse componente é um:

A) servidor DNS autoritativo.
B) NAT básico.
C) proxy reverso.
D) proxy direto.

### S2D3Q130 — Proxy reverso

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [10.2 Proxy reverso](semana_02_estudo.md#s2-d3-proxy), na definição do extremo representado e na lista de terminação TLS, balanceamento e ocultação da topologia.

Um componente recebe as conexões destinadas a um portal público, termina TLS, distribui requisições entre servidores internos e evita expor diretamente esses servidores. Como ele deve ser classificado?

A) Proxy reverso, pois recebe conexões em nome dos servidores de origem e pode aplicar funções na publicação da aplicação.

B) Proxy direto, pois recebe conexões em nome dos servidores de origem e controla a navegação realizada pelos usuários externos.

C) Proxy direto, pois a terminação de TLS define o extremo representado, independentemente da posição diante dos servidores.

D) Proxy reverso somente se cada navegador o configurar explicitamente como intermediário de suas conexões de saída.

### S2D3Q131 — Diferença entre proxy e NAT

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [10. Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy), no parágrafo que contrasta representação de um extremo pelo proxy com tradução de campos pelo NAT.

Em uma arquitetura, um proxy recebe uma conexão do cliente e intermedeia a comunicação com o destino, enquanto um equipamento NAT encaminha pacotes após reescrever campos de endereçamento. Qual distinção está correta?

A) NAT sempre cria uma nova requisição de aplicação, enquanto o proxy se limita a recalcular endereços e somas de verificação.

B) Proxy atua em nome de um extremo, enquanto NAT pode traduzir endereços e portas sem terminar a sessão de aplicação.

C) Proxy e NAT operam somente nos campos IP e de transporte, sem representar qualquer extremo ou compreender a aplicação.

D) Proxy necessariamente decifra todo conteúdo, enquanto NAT preserva sempre endereços e portas visíveis nos pacotes encaminhados.

### S2D3Q132 — NAT básico versus PAT/NAPT

**Nível:** Médio

**Uso:** Revisão

**Referência:** [11. NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat), nos dois itens que definem NAT básico e NAPT e no parágrafo sobre o contraste usado em prova.

Quando uma questão usa os termos no sentido estrito do RFC 2663 e contrapõe NAT básico a PAT/NAPT, qual é a diferença determinante?

A) NAT básico traduz endereço e porta de transporte, enquanto PAT/NAPT altera somente o endereço IP do fluxo.

B) NAT básico traduz endereços sem traduzir portas, enquanto PAT/NAPT também usa portas para multiplexar os fluxos.

C) NAT básico e PAT/NAPT traduzem sempre endereço e porta, diferenciando-se apenas pelo fabricante do equipamento.

D) NAT básico admite apenas mapeamento estático e PAT/NAPT apenas mapeamento dinâmico, sem alterar portas em nenhum caso.

### S2D3Q133 — Tabela de tradução e multiplexação do PAT/NAPT

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [11. NAT básico e PAT/NAPT — Exemplo resolvido 3: Dois usuários compartilham um IP público](semana_02_estudo.md#s2-d3-nat-pat), incluindo a tabela de mapeamentos com portas públicas diferentes.

Os hosts 10.0.0.10:52000 e 10.0.0.20:52000 iniciam conexões ao mesmo servidor e à mesma porta, compartilhando o endereço público 203.0.113.8. Como o PAT mantém os retornos separados?

A) Conserva 203.0.113.8:52000 nos dois fluxos e usa apenas o destino externo idêntico para escolher o host interno.

B) Conserva a mesma tupla pública nos dois fluxos e alterna cada resposta entre os hosts segundo sua ordem de chegada.

C) Aloca portas públicas distintas e registra em sua tabela qual combinação pública corresponde a cada origem interna.

D) Altera a porta de destino do servidor em cada fluxo e mantém uma única porta pública de origem sem mapeamento individual.

### S2D3Q134 — Limites de segurança do NAT/PAT

**Nível:** Médio

**Uso:** Revisão

**Referência:** [11. NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat).

Assinale a afirmativa correta sobre NAT/PAT.

A) NAT/PAT cifra automaticamente os dados, dispensando TLS.
B) NAT/PAT não autentica usuários, não criptografa o tráfego e não substitui um firewall.
C) PAT/NAPT impede, por definição, todo acesso indevido vindo da Internet.
D) NAT básico é um sinônimo de proxy reverso de aplicação.

### S2D3Q135 — Finalidade, porta e limite do NTP

**Nível:** Médio

**Uso:** Revisão

**Referência:** [12. NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp), nos trechos sobre 123/UDP, importância para logs e certificados, diferença para fuso e proteção das fontes.

Os relógios de três servidores apresentam desvios que dificultam correlacionar logs e verificar a validade temporal de certificados. Qual medida trata diretamente a causa sem confundir referência de tempo com exibição local?

A) Sincronizar os relógios por NTP em 123/UDP e manter fuso horário e horário de verão como configurações locais.

B) Distribuir o fuso horário por NTP em 123/TCP e deixar que cada servidor mantenha sua própria referência de relógio.

C) Sincronizar os relógios por NTP em 161/UDP e usar o estrato para definir o fuso horário exibido pelos sistemas.

D) Sincronizar por NTP em 123/UDP e considerar qualquer fonte automaticamente confiável, sem proteção ou validação operacional.

### S2D3Q136 — Alcance das associações de portas registradas pela IANA

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas) e [1. Protocolo, serviço, porta e socket — Portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).

Um inventário identifica conexões para 22/TCP, 443/TCP e 8080/TCP. Sem inspecionar os protocolos ou a configuração dos hosts, qual conclusão é válida sobre esses números de porta?

A) 22/TCP comprova SSH e 443/TCP comprova HTTPS corretamente configurado, pois aplicações não podem trocar suas portas registradas.

B) 8080/TCP não pode transportar HTTP, pois somente a porta bem conhecida 80/TCP admite esse protocolo de aplicação.

C) Um sistema compatível com o registro da IANA recusa serviços fora da porta convencional e impede outros protocolos nela.

D) As portas sugerem associações convencionais, mas a configuração pode divergir e o número isolado não prova protocolo, conteúdo ou segurança.

### S2D3Q137 — Ordem do fluxo integrado de acesso à rede

**Nível:** Médio

**Uso:** Revisão

**Referência:** [14. Fluxo integrado de acesso a um portal — etapas 1 a 4](semana_02_estudo.md#s2-d3-fluxo-integrado), começando pela entrega de IP, prefixo, gateway e DNS pelo DHCP.

Uma estação depende de configuração automática e acabou de ser conectada à rede. Qual sequência respeita a primeira dependência para que depois ela acesse um portal pelo nome?

A) Negociar TLS com o portal; depois obter a concessão DHCP, resolver o nome e escolher o gateway.

B) Resolver o nome no DNS; depois obter a concessão DHCP, descobrir o gateway e iniciar o transporte.

C) Obter a concessão DHCP; depois resolver o nome, encaminhar o tráfego e negociar a proteção do portal.

D) Criar o mapeamento PAT na borda; depois obter a concessão DHCP e configurar o servidor DNS local.

### S2D3Q138 — Diagnóstico de falha de resolução DNS

**Nível:** Médio

**Uso:** Revisão

**Referência:** [4. DNS — Exemplo resolvido 1: Nome não resolve, mas o IP responde](semana_02_estudo.md#s2-d3-dns), especialmente o raciocínio que compara os dois testes.

Uma estação alcança o endereço IP do portal, mas a tentativa pelo nome falha antes de obter qualquer endereço para a conexão. Qual frente deve ser verificada primeiro?

A) A negociação TLS, verificando certificado e algoritmos antes de confirmar qual endereço o nome deveria produzir.

B) O roteamento IP, substituindo a rota funcional usada no teste direto antes de examinar a consulta de nomes.

C) A tabela PAT, recriando o mapeamento que já permitiu alcançar o mesmo destino pelo endereço IP.

D) A resolução DNS, verificando servidor configurado, resposta recebida, cache e registros publicados para o nome.

### S2D3Q139 — Diagnóstico por etapas após a resolução DNS

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [14. Fluxo integrado de acesso a um portal — diagnóstico por sintoma](semana_02_estudo.md#s2-d3-fluxo-integrado), em conjunto com as etapas posteriores à resolução.

O resolvedor retorna o endereço correto do portal, mas os segmentos SYN enviados a 443/TCP não recebem SYN-ACK. Qual é a próxima linha de investigação tecnicamente adequada?

A) Limpar apenas o cache DNS e republicar o registro, pois uma resolução bem-sucedida impede falhas nas etapas seguintes.

B) Validar primeiro o certificado do portal, pois o servidor o envia antes de aceitar a abertura da conexão TCP.

C) Analisar primeiro a resposta HTTP da aplicação, pois seus códigos de estado antecedem a negociação da conexão TCP.

D) Verificar rota, filtragem, tradução e serviço em escuta, pois a falha ocorre depois do DNS e antes de TLS ou HTTP.

### S2D3Q140 — Sequência de HTTPS com proxy reverso

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [14. Fluxo integrado de acesso a um portal — etapas 7 a 10](semana_02_estudo.md#s2-d3-fluxo-integrado), que ordena TCP, TLS, HTTP e proxy reverso.

O nome de um portal já foi resolvido, e o cliente usará HTTPS tradicional para alcançar um proxy reverso que publica a aplicação. Qual ordenação descreve o fluxo até o servidor interno?

A) Negociar TLS; abrir TCP para 443; enviar HTTP protegido; o proxy encaminhar a requisição ao servidor interno.

B) Abrir TCP para 443; negociar TLS; enviar HTTP protegido; o proxy encaminhar a requisição ao servidor interno.

C) Enviar HTTP protegido; negociar TLS; abrir TCP para 443; o proxy encaminhar a requisição ao servidor interno.

D) Abrir TCP para 443; enviar HTTP protegido; negociar TLS; o proxy encaminhar a requisição ao servidor interno.

### S2D3Q141 — Identificação de conexões por seus extremos e protocolo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [1. Protocolo, serviço, porta e socket](semana_02_estudo.md#s2-d3-protocolo-porta), na lista dos cinco componentes usados para identificar uma conexão TCP.

Um servidor em 203.0.113.10:443 mantém duas conexões TCP vindas de 198.51.100.20, uma da porta 51000 e outra da 51001. Qual informação permite distingui-las corretamente?

A) IP e porta de origem, IP e porta de destino e protocolo, que formam combinações distintas para as conexões.

B) Apenas o endereço e a porta de destino, pois uma porta de escuta cria uma identificação exclusiva para cada cliente.

C) Apenas o endereço de origem e o nome DNS consultado, pois as portas deixam de identificar o fluxo após o handshake.

D) Apenas o número inicial de sequência escolhido pelo cliente, sem considerar endereços, portas ou protocolo de transporte.

### S2D3Q142 — Porta como indício, não como prova do protocolo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas) e [1. Protocolo, serviço, porta e socket — Portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).

Uma captura sem decodificação da aplicação mostra tráfego TCP destinado à porta 443. Qual inferência respeita o alcance dessa evidência?

A) O tráfego é HTTPS com certificado válido, e a aplicação de destino foi verificada como livre de vulnerabilidades.

B) O tráfego é necessariamente HTTP/2, e o cliente aceitou corretamente toda a cadeia apresentada pelo servidor.

C) O conteúdo está cifrado e é legítimo, pois nenhum outro protocolo ou serviço pode usar 443/TCP.

D) A porta sugere a convenção de HTTPS, mas protocolo efetivo, validação, conteúdo e segurança exigem outras evidências.

### S2D3Q143 — Transporte do HTTP/3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [3.1 HTTP e 3.2 HTTPS](semana_02_estudo.md#s2-d3-http-https), nos trechos que registram HTTP/3 sobre QUIC/UDP em 443 e preservação da proteção criptográfica.

Uma equipe migra um serviço de HTTP/2 para HTTP/3 e precisa ajustar a política de transporte sem remover a proteção criptográfica. Qual descrição está correta?

A) HTTP/3 usa QUIC sobre UDP, normalmente em 443, e integra a proteção TLS ao estabelecimento da conexão QUIC.

B) HTTP/3 inicia QUIC em UDP, mas transfere o fluxo para TCP depois do primeiro datagrama e só então negocia TLS.

C) HTTP/3 usa TCP como HTTP/2, enquanto QUIC define apenas o formato dos cabeçalhos HTTP acima desse transporte.

D) HTTP/3 usa QUIC sobre UDP sem TLS, pois os mecanismos de recuperação de perda também autenticam o servidor.

### S2D3Q144 — Registro PTR e resolução DNS reversa

**Nível:** Médio

**Uso:** Simulado

**Referência:** [4.3 Registros frequentes do DNS](semana_02_estudo.md#s2-d3-dns).

Qual registro DNS é empregado tipicamente para resolução reversa, isto é, de um endereço para um nome?

A) NS
B) SOA
C) PTR
D) TXT

### S2D3Q145 — Servidor autoritativo, resolvedor e TTL de cache

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [4.1 Componentes e 4.2 Recursão, iteração e cache do DNS](semana_02_estudo.md#s2-d3-dns), nas definições de servidor autoritativo, resolvedor recursivo, cache e TTL.

Um registro foi alterado na zona autoritativa, mas um resolvedor ainda possui a resposta anterior dentro do TTL recebido. Qual comportamento e interpretação estão corretos?

A) A alteração no autoritativo invalida imediatamente todas as cópias em cache, mesmo sem comunicação com os resolvedores.

B) O resolvedor deve descartar a resposta porque TTL determina a disponibilidade atual do servidor e a existência do domínio.

C) O autoritativo serve os dados publicados na zona, enquanto o resolvedor pode reutilizar a resposta anterior até terminar seu TTL aplicável.

D) A resposta armazenada transforma o resolvedor em autoridade da zona e permite renovar indefinidamente o TTL sem nova consulta.

### S2D3Q146 — Diagnóstico de falha na concessão DHCP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [5. DHCP — atribuição dinâmica de configuração e diagnóstico por sintoma](semana_02_estudo.md#s2-d3-dhcp), incluindo os parâmetros concedidos, DORA, relay e escopo.

Uma estação configurada para obtenção automática apresenta endereço 169.254.34.8, sem gateway e sem parâmetros válidos da rede corporativa. Qual deve ser o primeiro foco de diagnóstico?

A) Alterar apenas os registros DNS do host, pois a resolução de nomes é responsável por conceder endereço e gateway.

B) Verificar o intercâmbio DHCP, o alcance do servidor ou relay e a disponibilidade de endereços no escopo correto.

C) Configurar apenas um gateway estático e manter o endereço link-local como se fosse uma concessão válida da rede corporativa.

D) Limpar apenas a tabela ARP, pois o protocolo ARP atribui prefixo, gateway e duração da concessão automática.

### S2D3Q147 — Critérios para escolha de UDP

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [2.3 Escolha do transporte](semana_02_estudo.md#s2-d3-tcp-udp).

Qual cenário justifica de modo mais adequado a escolha de UDP, sem reduzir a decisão à frase “UDP é mais rápido”?

A) Uma aplicação precisa de um fluxo de bytes ordenado e quer que o transporte retransmita perdas nativamente.
B) Uma aplicação troca mensagens curtas e independentes, valoriza baixa latência ou multicast e pode tratar perdas conforme sua própria lógica.
C) Um serviço exige handshake SYN, SYN-ACK e ACK antes de cada datagrama.
D) Um sistema precisa que a camada de transporte preserve necessariamente as fronteiras de todas as mensagens em um fluxo TCP.

### S2D3Q148 — Garantias e limites do TCP

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [2.1 TCP: orientado à conexão e confiável](semana_02_estudo.md#s2-d3-tcp-udp), nos pontos sobre fluxo de bytes, ordenação, confirmações, fronteiras de mensagens e significado limitado do ACK.

Uma aplicação envia duas mensagens por uma conexão TCP, mas o receptor precisa reconstruir suas fronteiras e confirmar separadamente o sucesso da operação de negócio. Qual propriedade explica essa necessidade?

A) TCP entrega mensagens ordenadas preservando cada escrita, e seu ACK confirma que a operação foi aceita pela aplicação remota.

B) TCP entrega bytes ordenados sem controle de fluxo, e cada ACK delimita a mensagem de aplicação correspondente no receptor.

C) TCP entrega datagramas independentes com controle de congestionamento, e a aplicação só precisa confirmar sua gravação definitiva.

D) TCP entrega fluxo de bytes confiável e ordenado, mas não preserva fronteiras de mensagens nem confirma a semântica da aplicação.

### S2D3Q149 — Impacto operacional da sincronização NTP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [12. NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp), nos usos para logs e validade de certificados; e [14. Fluxo integrado de acesso a um portal — etapa 11](semana_02_estudo.md#s2-d3-fluxo-integrado).

Eventos relacionados aparecem com diferença de vários minutos nos logs de dois servidores, e um deles rejeita um certificado ainda válido segundo a hora correta. Qual ação é prioritária?

A) Verificar estado de sincronização, servidores NTP selecionados e fontes de tempo usadas pelas duas máquinas.

B) Alterar somente o fuso horário exibido, sem verificar a referência temporal mantida pelos relógios dos sistemas.

C) Reduzir o TTL dos registros DNS, para que os relógios sejam atualizados a cada nova resolução de nome.

D) Renovar somente o certificado rejeitado, sem corrigir o desvio também observado na correlação dos logs.

### S2D3Q150 — Fluxo do cliente ao backend publicado

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Fluxo integrado de acesso a um portal](semana_02_estudo.md#s2-d3-fluxo-integrado), com apoio de [NAT e PAT](semana_02_estudo.md#s2-d3-nat-pat) e [Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy).

Uma estação recém-conectada recebe configuração automática e acessa, por nome, um portal remoto. Na borda, vários clientes compartilham um endereço público por PAT; no destino, um proxy reverso publica a aplicação. Analise as afirmações.

I. O DHCP pode fornecer endereço, prefixo, gateway e resolvedor, mas a resolução do nome do portal pertence ao DNS.

II. Para destino remoto, o pacote mantém o IP do servidor enquanto o quadro local usa o próximo salto; na borda, o PAT pode traduzir a tupla de origem.

III. Depois do transporte e da proteção TLS, o proxy reverso pode terminar a conexão externa e iniciar outra para o backend, sem substituir DNS, roteamento ou autorização da aplicação.

Está correto o que se afirma em:

A) I e II, apenas.

B) I, II e III.

C) I e III, apenas.

D) II e III, apenas.

## Gabarito do Dia 3

### Gabarito das questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | A |
| 2 | C |
| 3 | D |
| 4 | D |
| 5 | B |
| 6 | A |
| 7 | C |
| 8 | C |
| 9 | D |
| 10 | C |
| 11 | A |
| 12 | B |
| 13 | D |
| 14 | B |
| 15 | C |
| 16 | A |
| 17 | D |
| 18 | B |
| 19 | B |
| 20 | C |
| 21 | A |
| 22 | A |
| 23 | D |
| 24 | C |
| 25 | B |
| 26 | D |
| 27 | C |
| 28 | A |
| 29 | D |
| 30 | A |
| 31 | B |
| 32 | B |
| 33 | C |
| 34 | B |
| 35 | A |
| 36 | D |
| 37 | C |
| 38 | D |
| 39 | D |
| 40 | B |
| 41 | A |
| 42 | D |
| 43 | A |
| 44 | C |
| 45 | C |
| 46 | B |
| 47 | B |
| 48 | D |
| 49 | A |
| 50 | B |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 3.1 | C |
| 3.2 | B |
| 3.3 | D |
| 3.4 | B |
| 3.5 | C |
| 3.6 | A |
| 3.7 | D |
| 3.8 | C |
| 3.9 | C |
| 3.10 | A |
| 3.11 | B |
| 3.12 | D |
| 3.13 | A |
| 3.14 | C |
| 3.15 | D |
| 3.16 | B |
| 3.17 | A |
| 3.18 | C |
| 3.19 | B |
| 3.20 | D |

## Comentários do Dia 3

### Comentário S2D3Q101

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** a porta permite ao sistema operacional encaminhar o segmento à aplicação, enquanto a conexão TCP é individualizada por IP e porta de origem, IP e porta de destino e protocolo.
- **B)** quem identifica o host na camada de rede é o endereço IP; além disso, somente o IP do cliente não distingue conexões simultâneas.
- **C)** clientes normalmente usam portas de origem dinâmicas, e apenas o par de portas não identifica de modo completo uma conexão entre hosts.
- **D)** o número da porta não certifica qual conteúdo trafega nela, e o protocolo isolado não diferencia as várias conexões TCP existentes.

**Conceito:** demultiplexação por portas e identificação de uma conexão TCP pela combinação de suas extremidades.

**Pegadinha:** atribuir à porta funções próprias do endereço IP ou tratá-la como prova do conteúdo transportado.

**Como pensar:** separe três perguntas: o IP localiza o host, a porta direciona o tráfego ao processo e a quíntupla distingue a conexão.

**Referência:** [1. Protocolo, serviço, porta e socket](semana_02_estudo.md#s2-d3-protocolo-porta), especialmente os parágrafos sobre demultiplexação e a quíntupla de uma conexão TCP.

### Comentário S2D3Q102

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D3Q103

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** ordenação e retransmissão não são serviços nativos do UDP; se necessárias, devem ser providas acima dele.
- **B)** a independência dos datagramas no transporte não limita a lógica mantida pelo protocolo de aplicação.
- **C)** o UDP também não confirma entrega nativamente, e a aplicação pode implementar tanto ordenação quanto retransmissão.
- **D)** a ausência dessas garantias no UDP não impede que o protocolo da aplicação implemente confirmação, controle de perda e reenvio.

**Conceito:** serviços ausentes no UDP e possibilidade de a aplicação construir confiabilidade acima do transporte.

**Pegadinha:** transformar “o UDP não oferece” em “uma aplicação sobre UDP não pode oferecer”.

**Como pensar:** identifique primeiro o que pertence ao cabeçalho e ao funcionamento do UDP; depois verifique o que pode ser acrescentado pela aplicação.

**Referência:** [2.2 UDP: datagramas sem conexão](semana_02_estudo.md#s2-d3-tcp-udp), especialmente a lista de garantias não oferecidas nativamente e o parágrafo sobre mecanismos implementados pela aplicação.

### Comentário S2D3Q104

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o caráter stateless do HTTP não proíbe a aplicação de manter sessão ou outros dados no servidor.
- **B)** persistência ou quantidade de requisições em uma conexão TCP não define o caráter stateless do protocolo HTTP.
- **C)** cookie é mecanismo da aplicação/HTTP e não altera a natureza do protocolo de transporte nem dispensa processamento no servidor.
- **D)** o HTTP não exige uma sessão de usuário entre requisições, mas a aplicação pode construir e correlacionar esse estado.

**Conceito:** ausência de estado obrigatório no HTTP e criação de estado pela aplicação.

**Pegadinha:** interpretar stateless como proibição absoluta de sessão ou como limitação da conexão TCP.

**Como pensar:** diferencie a semântica de cada requisição HTTP dos mecanismos adicionais usados pela aplicação para reconhecer uma sequência de interações.

**Referência:** [3.1 HTTP](semana_02_estudo.md#s2-d3-http-https), no parágrafo que define stateless e cita cookies, tokens e sessões no servidor.

### Comentário S2D3Q105

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** TLS não atesta a veracidade do conteúdo nem elimina falhas existentes no código ou na configuração da aplicação.
- **B)** a validação do certificado contribui para autenticar o servidor, e o TLS fornece confidencialidade e integridade em trânsito, dentro desse escopo.
- **C)** autorização é decidida pela aplicação, e um certificado do servidor nada prova sobre a integridade do dispositivo cliente.
- **D)** HTTPS protege a comunicação, não necessariamente o dado armazenado ou cada trecho fora do canal, e não oculta todos os metadados.

**Conceito:** propriedades de segurança oferecidas pelo HTTPS e limites do escopo de proteção do TLS.

**Pegadinha:** ampliar segurança do canal para garantias sobre conteúdo, autorização, endpoint e armazenamento.

**Como pensar:** delimite o objeto protegido: dados em trânsito no canal TLS e identidade do servidor sob validação correta; não toda a aplicação.

**Referência:** [3.2 HTTPS](semana_02_estudo.md#s2-d3-http-https), incluindo as garantias do TLS em trânsito e a lista de garantias que não decorrem do HTTPS.

### Comentário S2D3Q106

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D3Q107

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O registro A associa um nome a um endereço IPv4.
- **B)** Incorreta. O registro AAAA associa um nome a um endereço IPv6.
- **C)** Correta. MX indica os servidores responsáveis pelo correio de um domínio.
- **D)** Incorreta. CNAME define um alias para outro nome canônico.

**Conceito:** tipos de registros DNS.

**Pegadinha:** escolher registros de endereço ou alias quando o enunciado pede infraestrutura de e-mail.

**Como pensar:** relacione a finalidade pedida à sigla: endereço, alias ou mail exchanger.

**Referência:** [4.3 Registros frequentes](semana_02_estudo.md#s2-d3-dns).

### Comentário S2D3Q108

**Nível:** Difícil

**Uso:** Essenciais
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

### Comentário S2D3Q109

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** a transferência de zona é um caso clássico de uso de TCP pelo DNS; não se deve presumir que ela ocorrerá em datagramas UDP.
- **B)** DoT é uma forma específica de DNS protegido, não o transporte obrigatório de uma transferência de zona clássica.
- **C)** TCP não é exclusivo do DoH; faz parte do DNS clássico, enquanto DoH encapsula DNS em HTTPS.
- **D)** o DNS clássico possui operações em UDP e em TCP na porta 53, e uma política que autorize somente UDP interrompe operações que exigem TCP.

**Conceito:** coexistência de UDP e TCP no DNS clássico e uso de 53/TCP para transferência de zona.

**Pegadinha:** reduzir a associação frequente “DNS–53/UDP” a uma regra exclusiva.

**Como pensar:** diante de “somente UDP”, procure operações DNS que exigem TCP, sobretudo transferência de zona e situações de resposta que demandam esse transporte.

**Referência:** [4.4 Transportes do DNS clássico](semana_02_estudo.md#s2-d3-dns), nos trechos que registram 53/UDP, 53/TCP e o uso de TCP em transferências de zona.

### Comentário S2D3Q110

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** a porta padrão de DoT é 853, e DoH não é HTTP sem TLS nem usa 853 como sua convenção normal.
- **B)** a alternativa inverte as associações usuais; HTTPS caracteriza DoH, ao passo que TLS direto em 853 caracteriza DoT.
- **C)** DoT usa TLS diretamente, por padrão em 853/TCP, e DoH transporta as mensagens por HTTPS, normalmente em 443.
- **D)** 53/UDP é comum no DNS clássico, mas não descreve os transportes encapsulados indicados no enunciado.

**Conceito:** distinção entre os transportes e portas usuais de DoT e DoH.

**Pegadinha:** aplicar a porta 53 a toda forma de DNS ou trocar os encapsulamentos de DoT e DoH.

**Como pensar:** expanda as siglas: “sobre TLS” aponta para TLS direto em 853; “sobre HTTPS” herda a convenção de HTTPS em 443.

**Referência:** [4.4 Transportes do DNS clássico](semana_02_estudo.md#s2-d3-dns), no parágrafo final que contrasta DNS clássico, DoT em 853 e DoH sobre HTTPS.

### Comentário S2D3Q111

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D3Q112

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** preserva UDP, mas troca as portas atribuídas ao cliente e ao servidor.
- **B)** no fluxo clássico, o cliente DHCP usa 68/UDP e envia ao serviço do servidor em 67/UDP; a resposta faz o percurso inverso.
- **C)** as numerações estão associadas aos papéis corretos, porém o DHCPv4 clássico usa UDP, não TCP.
- **D)** além de escolher TCP, a alternativa inverte as portas de cliente e servidor.

**Conceito:** associação de 67/UDP ao servidor DHCP e de 68/UDP ao cliente DHCP.

**Pegadinha:** trocar os papéis das portas ou preservar os números e alterar indevidamente o protocolo de transporte.

**Como pensar:** fixe o par completo, não apenas os números: servidor 67/UDP e cliente 68/UDP.

**Referência:** [5. DHCP — atribuição dinâmica de configuração](semana_02_estudo.md#s2-d3-dhcp), na lista de portas clássicas imediatamente após a sequência DORA.

### Comentário S2D3Q113

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o relay deve receber o broadcast no segmento dos clientes, e o escopo precisa fornecer parâmetros válidos para a rede da VLAN 20.
- **B)** unir as VLANs em camada 2 contraria a manutenção dos domínios separados, e o MAC não substitui a identificação da sub-rede atendida.
- **C)** NAT não é o mecanismo de encaminhamento do DHCP entre segmentos e ainda ocultaria a informação necessária para escolher redes distintas.
- **D)** o relay na interface da VLAN dos clientes recebe o broadcast e o encaminha ao servidor, que deve possuir escopo correspondente àquela sub-rede.

**Conceito:** posicionamento do DHCP relay e compatibilidade entre a sub-rede cliente e o escopo no servidor central.

**Pegadinha:** propor mecanismos de camada 2 ou tradução de endereços para resolver uma limitação de broadcast entre redes roteadas.

**Como pensar:** localize onde nasce o broadcast, posicione ali o agente que o transforma em comunicação roteável e confira de qual rede devem vir os parâmetros concedidos.

**Referência:** [5.1 Sequência DORA — DHCP relay](semana_02_estudo.md#s2-d3-dhcp), especialmente a explicação de que o relay encaminha mensagens entre segmentos e viabiliza o servidor central.

### Comentário S2D3Q114

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** POP3 é protocolo de acesso, e SMTP não é empregado para leitura e organização da caixa postal.
- **B)** SMTP movimenta mensagens na submissão e entre servidores; POP3 e IMAP permitem ao destinatário acessar as mensagens armazenadas.
- **C)** IMAP é protocolo de acesso e sincronização, enquanto SMTP não exerce a função de acesso à caixa.
- **D)** POP3 não transfere mensagens entre servidores, e IMAP não é protocolo de submissão de correio.

**Conceito:** separação entre protocolos de envio/transferência e protocolos de acesso ao e-mail.

**Pegadinha:** associar qualquer protocolo ligado a e-mail indistintamente a todas as etapas do fluxo.

**Como pensar:** divida o percurso em duas fases: SMTP para mover a mensagem; POP3 ou IMAP para o destinatário consultar a caixa.

**Referência:** [6. Correio eletrônico: SMTP, POP3 e IMAP](semana_02_estudo.md#s2-d3-email), incluindo as subseções 6.1 a 6.4 sobre envio e acesso à caixa postal.

### Comentário S2D3Q115

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** troca os papéis convencionais das portas 25 e 587; esta última é a referência usual de submissão pelo cliente.
- **B)** 465/TCP é associada à submissão com TLS implícito, e por isso não se inicia ali em claro para depois aplicar STARTTLS.
- **C)** 587/TCP é a convenção típica de submissão autenticada, enquanto 25/TCP permanece associada à transferência SMTP entre servidores.
- **D)** as duas convenções SMTP apresentadas usam TCP, não UDP.

**Conceito:** distinção funcional entre 587/TCP para submissão e 25/TCP para transferência entre servidores.

**Pegadinha:** decorar os números sem relacioná-los ao papel do cliente e do MTA ou alterar o transporte para UDP.

**Como pensar:** pergunte quem inicia a etapa: usuário submetendo ao seu serviço aponta para 587; MTA entregando a outro MTA aponta para 25.

**Referência:** [6.1 SMTP](semana_02_estudo.md#s2-d3-email), na lista de portas 25/TCP, 587/TCP e 465/TCP e seus respectivos papéis.

### Comentário S2D3Q116

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D3Q117

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** SMTP não é protocolo de acesso à caixa, e o modelo típico do POP3 não fornece a sincronização solicitada.
- **B)** POP3 não realiza submissão ou transferência entre servidores, e SMTP não oferece acesso sincronizado à caixa postal.
- **C)** IMAP é usado no acesso à caixa, não no envio; POP3 tampouco é o protocolo indicado para sincronizar pastas e marcações.
- **D)** SMTP atende à movimentação da mensagem, e IMAP mantém no servidor o estado necessário para acesso coerente por múltiplos dispositivos.

**Conceito:** composição do fluxo de envio por SMTP com acesso sincronizado por IMAP.

**Pegadinha:** inverter os protocolos de envio e de acesso ou atribuir a um deles todas as etapas do correio eletrônico.

**Como pensar:** acompanhe a mensagem no tempo: primeiro ela é movimentada por SMTP; depois a caixa permanece no servidor e é sincronizada por IMAP.

**Referência:** [6.4 Fluxo integrado de e-mail](semana_02_estudo.md#s2-d3-email), em conjunto com [6.3 IMAP](semana_02_estudo.md#s2-d3-email).

### Comentário S2D3Q118

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** a sessão de controle pode estar saudável em 21/TCP enquanto a conexão separada de dados permanece bloqueada.
- **B)** no modo passivo, o servidor informa uma porta de dados e o cliente inicia uma segunda conexão TCP, que precisa ser compatível com as regras do firewall.
- **C)** FTP clássico usa TCP tanto no controle quanto na conexão de dados; o modo passivo não muda o transporte para UDP.
- **D)** a associação tradicional do lado servidor à porta 20 pertence ao modo ativo e não descreve o fluxo passivo indicado.

**Conceito:** separação entre canais FTP e efeito do modo passivo sobre iniciativa e porta da conexão de dados.

**Pegadinha:** concluir que o sucesso do controle em 21/TCP garante o tráfego de dados ou aplicar ao modo passivo a regra tradicional do modo ativo.

**Como pensar:** traduza o sintoma: comandos funcionam significa controle liberado; listagem falha significa que a segunda conexão, a de dados, não foi estabelecida.

**Referência:** [7.1 FTP](semana_02_estudo.md#s2-d3-transferencia-remota), nos parágrafos sobre conexão de controle, conexão de dados e porta informada pelo servidor no modo passivo.

### Comentário S2D3Q119

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** conexão iniciada pelo servidor, tradicionalmente a partir de 20/TCP, caracteriza o funcionamento ativo, não o passivo.
- **B)** o servidor fica à escuta na porta que anunciou e o cliente abre para ela uma segunda conexão TCP, sem eliminar o controle.
- **C)** FTP mantém separados o canal de controle e a conexão usada para cada transferência de dados.
- **D)** esperar uma abertura iniciada pelo servidor novamente descreve a lógica do modo ativo.

**Conceito:** iniciativa do cliente e porta anunciada pelo servidor no modo passivo do FTP.

**Pegadinha:** trocar os sentidos das conexões ativa e passiva ou presumir que os dados percorrem o canal de controle.

**Como pensar:** no passivo, ambos os fluxos são abertos pelo cliente: primeiro o controle; depois os dados no destino informado pelo servidor.

**Referência:** [7.1 FTP](semana_02_estudo.md#s2-d3-transferencia-remota), especificamente a descrição do modo passivo e da conexão de dados iniciada pelo cliente.

### Comentário S2D3Q120

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** 22/TCP é a convenção do SSH/SFTP, e `PROT C` deixa a conexão de dados em claro.
- **B)** abrir TLS imediatamente em 990 descreve a modalidade implícita, não a explícita, e o valor padronizado antes de `PROT` é `PBSZ 0`.
- **C)** no FTPS explícito, a sessão começa no controle FTP em 21/TCP, sobe para TLS com `AUTH TLS` e solicita privacidade dos dados com `PBSZ 0` e `PROT P`.
- **D)** os comandos de proteção dependem do canal de controle já protegido; negociar TLS depois da transferência não protege os dados anteriores.

**Conceito:** ordem de negociação do FTPS explícito e proteção independente do canal de dados.

**Pegadinha:** confundir FTPS com SFTP, trocar os modos explícito e implícito ou supor que proteger o controle protege automaticamente os dados.

**Como pensar:** procure três etapas em ordem: controle FTP em 21, subida do controle para TLS e solicitação explícita de privacidade para os dados.

**Referência:** [7.2 FTPS](semana_02_estudo.md#s2-d3-transferencia-remota), no parágrafo sobre FTPS explícito, `AUTH TLS`, `PBSZ 0`, `PROT P` e `PROT C`.

### Comentário S2D3Q121

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** na convenção implícita, TLS começa imediatamente no controle em 990/TCP, mas a arquitetura ainda prevê conexões de dados separadas e negociadas.
- **B)** começar em 21 e negociar `AUTH TLS` define a modalidade explícita, e a porta registrada 989 não é obrigatória para todo modo de dados.
- **C)** o protocolo de arquivos sobre SSH é SFTP; FTPS permanece FTP protegido por TLS e conserva a separação de canais.
- **D)** criptografar desde a abertura não funde dados e controle em uma única conexão TCP.

**Conceito:** diferença entre FTPS implícito e explícito, portas registradas e preservação dos canais separados do FTP.

**Pegadinha:** confundir FTPS com SFTP ou interpretar 989/TCP como caminho fixo de toda transferência implícita.

**Como pensar:** trate “implícito” como o momento em que TLS começa; depois aplique normalmente a arquitetura FTP de controle e dados separados.

**Referência:** [7.2 FTPS](semana_02_estudo.md#s2-d3-transferencia-remota), nos parágrafos sobre FTPS implícito, registros 990/989 e negociação de portas nos modos ativo e passivo; e [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas).

### Comentário S2D3Q122

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** SFTP opera como protocolo/subsistema sobre um transporte SSH e pode usar a infraestrutura de autenticação por chave pública já disponível.
- **B)** FTP com TLS explícito é FTPS explícito, tecnologia distinta do SFTP e normalmente iniciada em 21/TCP.
- **C)** FTP com TLS implícito também pertence ao FTPS, e certificados TLS não se convertem automaticamente em chaves SSH.
- **D)** SFTP não é modalidade de FTPS nem herda a arquitetura FTP de canais separados de controle e dados.

**Conceito:** identidade do SFTP como protocolo de arquivos sobre SSH, distinto de FTP e FTPS.

**Pegadinha:** expandir informalmente SFTP como “secure FTP” e concluir que ele é apenas FTP protegido por TLS.

**Como pensar:** localize a tecnologia base: se o protocolo funciona sobre SSH e aproveita suas chaves, trata-se de SFTP, não de uma variante FTPS.

**Referência:** [7.3 SFTP](semana_02_estudo.md#s2-d3-transferencia-remota), especialmente a definição como SSH File Transfer Protocol e a regra “SFTP não é FTP sobre TLS”.

### Comentário S2D3Q123

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** autenticar por senha não acrescenta ao Telnet a criptografia nativa que falta à sessão.
- **B)** SFTP é o protocolo de transferência de arquivos sobre SSH; não é, por si, o serviço de terminal interativo solicitado.
- **C)** FTPS protege operações FTP com TLS, mas seu canal de controle não se torna um terminal de administração do sistema.
- **D)** SSH foi projetado para administração remota protegida, e a segurança depende também de validar o host e resguardar as chaves privadas.

**Conceito:** uso do SSH para administração remota segura e controles necessários sobre as chaves.

**Pegadinha:** escolher outro protocolo protegido apenas porque ele usa TLS ou a mesma porta, sem verificar a função oferecida.

**Como pensar:** combine função e propriedades: terminal remoto mais autenticação, integridade e confidencialidade aponta para SSH; depois confira a confiança nas chaves.

**Referência:** [7.4 SSH](semana_02_estudo.md#s2-d3-transferencia-remota), incluindo os serviços oferecidos pelo SSH e os cuidados com chave do host e chaves privadas.

### Comentário S2D3Q124

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** acerta função, porta e transporte, mas atribui ao Telnet uma cifragem nativa que ele não fornece.
- **B)** Telnet não é protocolo de transferência de arquivos nem protege nativamente somente uma parte da sessão.
- **C)** Telnet oferece terminal remoto, usa convencionalmente 23/TCP e expõe credenciais e conteúdo quando não há proteção externa.
- **D)** a convenção é TCP, e o protocolo não oferece a garantia criptográfica de integridade descrita.

**Conceito:** função de terminal remoto, porta 23/TCP e ausência de proteção criptográfica nativa no Telnet.

**Pegadinha:** reconhecer corretamente o serviço e a porta, mas acrescentar uma propriedade de segurança inexistente.

**Como pensar:** recupere o trio inseparável cobrado em prova: Telnet, terminal remoto, 23/TCP em claro; para proteção moderna, compare com SSH.

**Referência:** [7.5 Telnet](semana_02_estudo.md#s2-d3-transferencia-remota), que o define como terminal remoto em 23/TCP sem a proteção criptográfica esperada.

### Comentário S2D3Q125

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** GET é normalmente iniciado pelo gerente contra o agente, e trap é notificação, não resposta do gerente a uma leitura.
- **B)** o gerente lê objetos expostos pelo agente e identificados por OIDs na estrutura da MIB; o agente pode iniciar uma trap diante de evento.
- **C)** os objetos monitorados são expostos pelo agente do equipamento, GET é leitura e trap não confirma cada consulta realizada.
- **D)** inverte gerente e agente e ainda trata trap como pedido confirmado, função incompatível com a notificação clássica.

**Conceito:** papéis de gerente e agente, identificação MIB/OID e diferença entre consulta e notificação SNMP.

**Pegadinha:** inverter o sentido das operações e confundir trap com resposta ou notificação confirmada.

**Como pensar:** acompanhe quem toma a iniciativa: o gerente pergunta por GET; o agente responde e, diante de evento, pode avisar por trap; INFORM é a alternativa confirmada.

**Referência:** [8. SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp), nos trechos que definem gerente, agente, MIB, OID, GET, TRAP e INFORM.

### Comentário S2D3Q126

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** inverte as portas, troca UDP por TCP e ainda atribui ao SNMPv2c garantias criptográficas que community strings não oferecem.
- **B)** acerta portas e transporte, mas SNMPv2c não equivale a um SNMPv3 corretamente configurado com autenticação e privacidade.
- **C)** troca os destinos das portas e nega indevidamente a capacidade de autenticação existente no SNMPv3.
- **D)** consultas e respostas usam tradicionalmente o agente em 161/UDP, notificações chegam ao gerente em 162/UDP e a proteção do SNMPv3 depende do nível e da configuração.

**Conceito:** portas, direção das mensagens e diferença de proteção entre versões do SNMP.

**Pegadinha:** apresentar uma opção parcialmente correta nas portas, mas errada ao equiparar SNMPv2c e SNMPv3.

**Como pensar:** verifique em três passos independentes: destino da consulta, destino da notificação e garantias efetivamente configuráveis em cada versão.

**Referência:** [8. SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp), nos trechos sobre 161/UDP, 162/UDP e proteção das versões; e [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas).

### Comentário S2D3Q127

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** DN identifica uma entrada do diretório, e bind está relacionado ao estabelecimento/autenticação da sessão, não à listagem da subárvore.
- **B)** DN não identifica um atributo isolado, search realiza pesquisa e não remove a entrada localizada.
- **C)** LDAP organiza entradas hierarquicamente, identifica cada uma por DN, armazena seus atributos e oferece operações como bind e search.
- **D)** bind não é operação de alteração de atributos, e search não é o mecanismo que negocia TLS.

**Conceito:** estrutura hierárquica de um diretório LDAP e finalidade geral de DN, atributos, bind e search.

**Pegadinha:** reutilizar termos reais do LDAP, mas trocar o objeto identificado e a finalidade das operações.

**Como pensar:** associe primeiro DN à entrada; depois diferencie autenticar/estabelecer contexto com bind de pesquisar entradas com search.

**Referência:** [9. LDAP — acesso a diretórios](semana_02_estudo.md#s2-d3-ldap), na definição de hierarquia, DN, atributos e operações bind e search.

### Comentário S2D3Q128

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** a aplicação pode autenticar uma identidade com apoio do LDAP e decidir permissões separadamente; o canal pode usar STARTTLS em 389/TCP ou TLS implícito em 636/TCP.
- **B)** autenticação bem-sucedida não concede todas as permissões, e a porta 389 não implica cifragem sem a negociação apropriada.
- **C)** autorização pode permanecer na aplicação, e o LDAPS usa convencionalmente TCP, não UDP; STARTTLS também oferece uma forma protegida.
- **D)** TLS protege o canal, não converte identidade em autorização, e a convenção do LDAPS com TLS implícito é 636/TCP.

**Conceito:** separação entre autenticação e autorização e formas usuais de proteger a sessão LDAP.

**Pegadinha:** combinar uma porta correta com uma conclusão indevida de autorização ou tratar TLS como política de acesso.

**Como pensar:** responda separadamente quem comprova a identidade, quem decide a permissão e como o canal LDAP recebe proteção criptográfica.

**Referência:** [9. LDAP — acesso a diretórios](semana_02_estudo.md#s2-d3-ldap), especialmente os parágrafos sobre 389/STARTTLS, 636/LDAPS e participação do diretório em autenticação sem concentrar toda autorização.

### Comentário S2D3Q129

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D3Q130

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** o componente está diante dos servidores e aceita conexões em nome deles, papel definidor do proxy reverso.
- **B)** proxy direto representa clientes em seus acessos de saída, ainda que possa aplicar políticas de navegação.
- **C)** terminar TLS é uma capacidade possível, mas a classificação direto/reverso decorre do extremo representado.
- **D)** configuração explícita no navegador é característica possível de proxy direto, não condição para classificar um proxy reverso.

**Conceito:** identificação do proxy reverso pela representação dos servidores publicados.

**Pegadinha:** definir o tipo de proxy por uma função acessória, como TLS, em vez de observar qual extremo ele representa.

**Como pensar:** localize o intermediário no fluxo: diante dos clientes e em nome deles é direto; diante dos servidores e em nome deles é reverso.

**Referência:** [10.2 Proxy reverso](semana_02_estudo.md#s2-d3-proxy), na definição do extremo representado e na lista de terminação TLS, balanceamento e ocultação da topologia.

### Comentário S2D3Q131

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** inverte os papéis; NAT altera campos de endereçamento, enquanto um proxy pode criar/intermediar comunicação em nome de um extremo.
- **B)** a distinção conceitual está no papel de representante exercido pelo proxy e na tradução feita pelo NAT no tráfego encaminhado.
- **C)** a descrição pode aproximar-se do NAT, mas elimina justamente a característica de representação que define o proxy.
- **D)** nem todo proxy consegue ler conteúdo protegido ponta a ponta, e a função do NAT é alterar campos como endereço e, no PAT, porta.

**Conceito:** diferença entre intermediação em nome de um extremo e tradução de endereçamento no encaminhamento.

**Pegadinha:** concluir que proxy e NAT são equivalentes porque ambos podem ocultar endereços internos.

**Como pensar:** pergunte se o componente representa um participante da aplicação ou se apenas encaminha o fluxo com cabeçalhos traduzidos.

**Referência:** [10. Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy), no parágrafo que contrasta representação de um extremo pelo proxy com tradução de campos pelo NAT.

### Comentário S2D3Q132

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** troca as definições; a extensão para identificadores de transporte é característica do PAT/NAPT.
- **B)** NAT básico traduz endereços IP, enquanto PAT/NAPT acrescenta a tradução de portas e permite multiplexar fluxos em um endereço externo.
- **C)** no contraste técnico pedido, os termos não são sinônimos nem dependem do fabricante.
- **D)** estático versus dinâmico não é a distinção decisiva, e PAT/NAPT efetivamente pode alterar portas.

**Conceito:** tradução somente de endereço no NAT básico versus tradução de endereço e porta no PAT/NAPT.

**Pegadinha:** aplicar o uso cotidiano de “NAT” como termo guarda-chuva quando o enunciado exige a distinção estrita.

**Como pensar:** se a banca contrapôs expressamente os termos, associe “básico” a endereço e “port” em PAT a endereço mais porta.

**Referência:** [11. NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat), nos dois itens que definem NAT básico e NAPT e no parágrafo sobre o contraste usado em prova.

### Comentário S2D3Q133

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** como destino e porta pública também seriam iguais, faltaria uma associação única para demultiplexar os retornos entre os hosts.
- **B)** ordem de chegada não identifica de modo confiável a qual conexão pertence cada segmento de resposta.
- **C)** portas externas diferentes tornam únicos os mapeamentos e permitem à tabela restaurar a origem privada correspondente em cada retorno.
- **D)** mudar a porta de destino alteraria o serviço procurado no servidor e não substitui o estado de tradução por fluxo.

**Conceito:** multiplexação de conexões por portas públicas e uso da tabela de estado do PAT/NAPT.

**Pegadinha:** imaginar que portas privadas iguais impedem o compartilhamento ou que a ordem dos pacotes basta para desfazer a tradução.

**Como pensar:** escreva as duas linhas da tabela e procure o campo que o tradutor pode tornar distinto sem mudar o servidor de destino: a porta pública de origem.

**Referência:** [11. NAT básico e PAT/NAPT — Exemplo resolvido 3: Dois usuários compartilham um IP público](semana_02_estudo.md#s2-d3-nat-pat), incluindo a tabela de mapeamentos com portas públicas diferentes.

### Comentário S2D3Q134

**Nível:** Médio

**Uso:** Revisão
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

### Comentário S2D3Q135

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** NTP sincroniza a referência temporal pela porta convencional 123/UDP; fuso e horário de verão continuam pertencendo à configuração local.
- **B)** NTP sincroniza relógios, não distribui apenas fusos, e sua associação típica é com UDP, não TCP.
- **C)** 161/UDP é a porta tradicional do agente SNMP, e estrato não define o fuso exibido.
- **D)** acerta protocolo e porta, mas fontes falsas ou mal protegidas podem introduzir desvios e precisam de controle operacional.

**Conceito:** finalidade, porta e limites do NTP em relação a fuso e confiabilidade da fonte.

**Pegadinha:** aceitar uma alternativa com 123/UDP que transforma sincronização em garantia automática de confiança.

**Como pensar:** procure a opção que reúna relógio coerente, 123/UDP e separação entre referência temporal e regras locais de exibição.

**Referência:** [12. NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp), nos trechos sobre 123/UDP, importância para logs e certificados, diferença para fuso e proteção das fontes.

### Comentário S2D3Q136

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** portas registradas orientam convenções, mas serviços podem escutar em outros números e um processo diferente pode usar uma porta conhecida.
- **B)** HTTP pode ser configurado em 8080 ou em outra porta; 80/TCP é a associação padrão, não uma imposição do protocolo.
- **C)** o registro da IANA não é um mecanismo de bloqueio do sistema operacional nem certifica o processo em escuta.
- **D)** os números ajudam a formular hipóteses, mas confirmação exige evidências do transporte, handshake, aplicação e configuração.

**Conceito:** valor indiciário, e não probatório, das associações convencionais de portas.

**Pegadinha:** transformar padronização administrativa em imposição técnica ou selo de legitimidade e segurança.

**Como pensar:** use a porta para iniciar a investigação, nunca para encerrá-la; confirme o serviço efetivo por evidências adicionais.

**Referência:** [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas) e [1. Protocolo, serviço, porta e socket — Portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).

### Comentário S2D3Q137

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** TLS pressupõe endereço de destino e conectividade de transporte, etapas posteriores à configuração local.
- **B)** a estação que depende de DHCP ainda não recebeu os parâmetros necessários para realizar normalmente a consulta externa.
- **C)** a concessão entrega os parâmetros básicos de rede dos quais dependem consulta DNS, encaminhamento, transporte e TLS.
- **D)** PAT ocorre quando tráfego já configurado alcança a borda e não precede a obtenção dos parâmetros pela estação.

**Conceito:** dependência inicial do DHCP no fluxo de uma estação sem configuração.

**Pegadinha:** começar pelo protocolo mais visível ao usuário e ignorar os pré-requisitos locais de rede.

**Como pensar:** ordene por dependência: configurar o host, resolver o destino, encaminhar, estabelecer transporte e proteger a aplicação.

**Referência:** [14. Fluxo integrado de acesso a um portal — etapas 1 a 4](semana_02_estudo.md#s2-d3-fluxo-integrado), começando pela entrega de IP, prefixo, gateway e DNS pelo DHCP.

### Comentário S2D3Q138

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** sem um endereço resultante da resolução, a sessão de transporte e a negociação TLS ainda não começaram.
- **B)** o sucesso pelo IP demonstra que existe um caminho funcional ao destino e desloca o foco para o elemento que mudou entre os testes.
- **C)** o teste direto já exigiu encaminhamento ao mesmo endereço, por isso recriar PAT não explica prioritariamente a diferença ligada ao nome.
- **D)** quando apenas o nome falha, servidor DNS, respostas, cache e dados publicados formam o primeiro bloco lógico de diagnóstico.

**Conceito:** isolamento da etapa DNS pela comparação entre acesso por endereço e acesso por nome.

**Pegadinha:** tratar qualquer falha de portal como problema de rota, TLS ou tradução sem localizar a última etapa bem-sucedida.

**Como pensar:** compare as duas tentativas e investigue o único requisito adicional da que falhou: converter o nome em endereço.

**Referência:** [4. DNS — Exemplo resolvido 1: Nome não resolve, mas o IP responde](semana_02_estudo.md#s2-d3-dns), especialmente o raciocínio que compara os dois testes.

### Comentário S2D3Q139

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o endereço correto já foi obtido, e esse sucesso não garante funcionamento de rota, filtro, NAT/PAT ou serviço de destino.
- **B)** certificado é apresentado durante TLS, que só ocorre depois de a conexão TCP estar estabelecida.
- **C)** resposta HTTP depende de transporte e, no HTTPS, de TLS; não pode anteceder o SYN-ACK ausente.
- **D)** o sintoma delimita a falha entre a resolução concluída e a abertura TCP, direcionando a análise à conectividade e ao listener.

**Conceito:** diagnóstico sequencial após DNS e antes das camadas TLS e HTTP.

**Pegadinha:** voltar a uma etapa já comprovada ou saltar para certificado e aplicação antes de estabelecer o transporte.

**Como pensar:** marque DNS como concluído e TCP como incompleto; investigue somente os componentes situados entre esses dois marcos.

**Referência:** [14. Fluxo integrado de acesso a um portal — diagnóstico por sintoma](semana_02_estudo.md#s2-d3-fluxo-integrado), em conjunto com as etapas posteriores à resolução.

### Comentário S2D3Q140

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** TLS necessita de um transporte previamente estabelecido e não pode anteceder a abertura TCP tradicional descrita.
- **B)** o cliente estabelece TCP, negocia o canal TLS, envia HTTP dentro dele e o proxy pode então encaminhar a requisição ao backend.
- **C)** HTTP protegido pressupõe tanto o transporte quanto o canal TLS, apresentados depois na alternativa.
- **D)** enviar HTTP antes da negociação TLS deixaria de seguir o fluxo HTTPS indicado no enunciado.

**Conceito:** dependência e ordem funcional entre TCP, TLS, HTTP e proxy reverso.

**Pegadinha:** reconhecer todos os componentes corretos, mas aceitar uma sequência que usa a camada superior antes de preparar a inferior.

**Como pensar:** monte a pilha de baixo para cima: transporte TCP, proteção TLS, mensagem HTTP e intermediação da aplicação.

**Referência:** [14. Fluxo integrado de acesso a um portal — etapas 7 a 10](semana_02_estudo.md#s2-d3-fluxo-integrado), que ordena TCP, TLS, HTTP e proxy reverso.

### Comentário S2D3Q141

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** a combinação de endereços, portas e TCP é diferente porque as portas de origem são 51000 e 51001.
- **B)** o destino é igual nos dois fluxos e identifica o serviço de escuta, não cada conexão aceita individualmente.
- **C)** nome DNS não integra a identificação mantida pelo TCP, enquanto as portas continuam relevantes durante a conexão.
- **D)** número de sequência participa do controle do fluxo, mas não substitui a identificação das extremidades e do protocolo.

**Conceito:** identificação de conexões TCP pela quíntupla de origem, destino e protocolo.

**Pegadinha:** confundir a porta comum de escuta com o socket individual de cada conexão estabelecida.

**Como pensar:** escreva lado a lado as cinco partes dos dois fluxos e localize o campo que muda, sem recorrer ao nome DNS.

**Referência:** [1. Protocolo, serviço, porta e socket](semana_02_estudo.md#s2-d3-protocolo-porta), na lista dos cinco componentes usados para identificar uma conexão TCP.

### Comentário S2D3Q142

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** porta de destino não demonstra que houve TLS, validação de certificado ou avaliação de vulnerabilidades da aplicação.
- **B)** 443/TCP não determina a versão HTTP nem registra a decisão tomada pelo cliente diante da cadeia de certificados.
- **C)** um processo pode usar porta convencionalmente associada a outro serviço, e o número não atesta cifra ou legitimidade.
- **D)** a associação com HTTPS é uma hipótese inicial que precisa ser confirmada pelo handshake e pelo comportamento do protocolo.

**Conceito:** limite probatório da porta de destino observada em uma captura.

**Pegadinha:** inferir propriedades do certificado, do conteúdo e da aplicação a partir de um único metadado de transporte.

**Como pensar:** formule a hipótese pela porta e procure confirmação em TLS e na aplicação antes de concluir qual protocolo ou segurança existe.

**Referência:** [13. Portas conhecidas mais cobradas](semana_02_estudo.md#s2-d3-portas) e [1. Protocolo, serviço, porta e socket — Portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).

### Comentário S2D3Q143

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** HTTP/3 é transportado por QUIC sobre UDP, usualmente em 443, e QUIC incorpora a negociação criptográfica baseada em TLS.
- **B)** a conexão HTTP/3 permanece em QUIC/UDP; não migra o fluxo para TCP após um datagrama inicial.
- **C)** usar TCP caracteriza os transportes usuais de HTTP/1.1 e HTTP/2, não a arquitetura de HTTP/3.
- **D)** recuperação de perdas e autenticação são propriedades distintas, e HTTP/3 não elimina a proteção TLS.

**Conceito:** HTTP/3 sobre QUIC/UDP e continuidade da proteção criptográfica.

**Pegadinha:** concluir que o uso de UDP elimina TLS ou que QUIC é apenas uma negociação preliminar antes do TCP.

**Como pensar:** memorize o conjunto, não termos isolados: HTTP/3, QUIC, UDP, normalmente 443 e TLS integrado.

**Referência:** [3.1 HTTP e 3.2 HTTPS](semana_02_estudo.md#s2-d3-http-https), nos trechos que registram HTTP/3 sobre QUIC/UDP em 443 e preservação da proteção criptográfica.

### Comentário S2D3Q144

**Nível:** Médio

**Uso:** Simulado
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

### Comentário S2D3Q145

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** o DNS não possui invalidação instantânea universal de caches quando o administrador altera os dados da zona.
- **B)** TTL limita o reaproveitamento da resposta em cache e não representa existência do domínio nem disponibilidade do servidor.
- **C)** autoridade decorre da responsabilidade pela zona, enquanto o resolvedor pode servir temporariamente a cópia válida mantida em cache.
- **D)** cache não confere autoridade, e a vigência não pode ser renovada indefinidamente sem obter nova resposta.

**Conceito:** distinção entre autoridade da zona, cache do resolvedor e duração determinada pelo TTL.

**Pegadinha:** interpretar TTL como validade do domínio ou imaginar propagação por invalidação imediata de todo cache.

**Como pensar:** separe origem e cópia: o autoritativo publica; o resolvedor reutiliza apenas pelo tempo remanescente autorizado no registro recebido.

**Referência:** [4.1 Componentes e 4.2 Recursão, iteração e cache do DNS](semana_02_estudo.md#s2-d3-dns), nas definições de servidor autoritativo, resolvedor recursivo, cache e TTL.

### Comentário S2D3Q146

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** DNS resolve e publica dados de nomes, mas não concede IP, prefixo e gateway ao cliente.
- **B)** endereço link-local e ausência de gateway indicam que a configuração automática esperada não foi obtida, direcionando a análise ao DHCP.
- **C)** um gateway isolado não transforma o endereço link-local em parâmetro válido da sub-rede corporativa nem corrige a concessão.
- **D)** ARP resolve endereços de enlace na rede local; não entrega a configuração fornecida pelo DHCP.

**Conceito:** reconhecimento de falha DHCP por endereço link-local e ausência dos parâmetros de rede.

**Pegadinha:** tentar corrigir uma etapa posterior ou um único parâmetro quando a concessão básica inteira falhou.

**Como pensar:** antes de DNS, rota externa ou aplicação, valide se o host recebeu por DORA um endereço da rede, prefixo, gateway e DNS.

**Referência:** [5. DHCP — atribuição dinâmica de configuração e diagnóstico por sintoma](semana_02_estudo.md#s2-d3-dhcp), incluindo os parâmetros concedidos, DORA, relay e escopo.

### Comentário S2D3Q147

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D3Q148

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** TCP não preserva as fronteiras de cada escrita e um ACK de transporte não confirma aceitação pela lógica de negócio.
- **B)** TCP possui controle de fluxo, e ACKs se referem ao fluxo de bytes, não à delimitação das mensagens da aplicação.
- **C)** datagramas independentes caracterizam UDP; TCP apresenta à aplicação um fluxo de bytes conectado.
- **D)** confiabilidade e ordenação pertencem ao fluxo de bytes, enquanto enquadramento das mensagens e confirmação semântica permanecem responsabilidades da aplicação.

**Conceito:** garantias do fluxo TCP e limites quanto a framing e sucesso da operação de aplicação.

**Pegadinha:** estender ACK e ordenação do transporte a fronteiras de mensagens ou à conclusão do negócio.

**Como pensar:** faça duas colunas: TCP cuida da entrega ordenada dos bytes; a aplicação delimita mensagens e confirma o resultado lógico.

**Referência:** [2.1 TCP: orientado à conexão e confiável](semana_02_estudo.md#s2-d3-tcp-udp), nos pontos sobre fluxo de bytes, ordenação, confirmações, fronteiras de mensagens e significado limitado do ACK.

### Comentário S2D3Q149

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** ambos os sintomas dependem de relógios coerentes e apontam diretamente para sincronização NTP e qualidade das fontes utilizadas.
- **B)** fuso altera a apresentação local, mas não corrige necessariamente o instante de referência incorreto do sistema.
- **C)** TTL DNS controla reaproveitamento de respostas em cache e não sincroniza o relógio do host.
- **D)** substituir o certificado pode mascarar um sintoma, mas deixa sem solução o desvio temporal que também corrompe os logs.

**Conceito:** impacto da sincronização de tempo sobre correlação de eventos e validações temporais.

**Pegadinha:** tratar isoladamente certificado ou exibição de horário em vez de investigar a fonte comum dos dois sintomas.

**Como pensar:** quando logs e validade temporal falham juntos, procure primeiro o relógio do sistema e sua referência NTP.

**Referência:** [12. NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp), nos usos para logs e validade de certificados; e [14. Fluxo integrado de acesso a um portal — etapa 11](semana_02_estudo.md#s2-d3-fluxo-integrado).

### Comentário S2D3Q150

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** I e II são verdadeiras, mas III também é; o proxy reverso representa os servidores publicados e pode estabelecer um fluxo separado até o backend.
- **B)** as três afirmações mantêm as fronteiras entre configuração, resolução, próximo salto, tradução, proteção do canal e publicação da aplicação.
- **C)** I e III são verdadeiras, mas II também é; o quadro aponta para o próximo salto sem trocar o IP remoto, e o PAT pode alterar a origem na borda.
- **D)** II e III são verdadeiras, mas I também é; DHCP pode informar o resolvedor, porém não executa a resolução do nome do portal.

**Conceito:** dependências e limites de DHCP, DNS, gateway, PAT, TCP/TLS/HTTP e proxy reverso no mesmo acesso.

**Pegadinha:** atribuir a um componente a função do seguinte ou supor que proxy, PAT ou porta conhecida substitui as demais etapas.

**Como pensar:** percorra configuração, resolução, encaminhamento/tradução, transporte/proteção e publicação, perguntando em cada etapa o que muda e o que permanece.

**Referência:** [Fluxo integrado de acesso a um portal](semana_02_estudo.md#s2-d3-fluxo-integrado), com apoio de [NAT e PAT](semana_02_estudo.md#s2-d3-nat-pat) e [Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy).
## Questões extras de revisão fixa do Dia 3

#### Extra Dia 3.1

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** função da Lei, do Decreto, do Regimento e do Código de Ética.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Revisão fixa do Dia 3 — Legislação: relação entre as normas](semana_02_estudo.md#s2-d3-revisao-legislacao), no quadro que separa Lei, Decreto, Regimento do CRA-PR e Código de Ética.

Considerando a função das quatro bases normativas estudadas para o Sistema CFA/CRAs, assinale a alternativa correta.

A) A Lei organiza internamente o CRA-PR; o Decreto aprova o Código de Ética; a RN nº 651 regulamenta a profissão; e a RN nº 671 cria os Conselhos.

B) A Lei aprova o Código de Ética; o Decreto cria o Sistema CFA/CRAs; a RN nº 651 disciplina o exercício; e a RN nº 671 organiza o CRA-PR.

C) A Lei disciplina o exercício e o Sistema; o Decreto regulamenta a Lei; a RN nº 651 aprova o Regimento do CRA-PR; e a RN nº 671 aprova o Código de Ética.

D) A Lei regulamenta norma anterior; o Decreto organiza o CRA-PR; a RN nº 651 cria a profissão; e a RN nº 671 define a estrutura legal dos Conselhos.

#### Extra Dia 3.2

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** campo da atividade profissional no art. 2º da Lei nº 4.769/1965.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Revisão fixa do Dia 3 — Legislação: Lei nº 4.769/1965](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente a síntese do art. 2º sobre documentos, funções e trabalhos nos campos da Administração.

À luz do art. 2º da Lei nº 4.769/1965, assinale a afirmação correta sobre o campo da atividade profissional.

A) Chefia intermediária e pesquisa integram o campo apenas em órgãos federais, pois a Lei exclui organizações privadas e administrações estaduais ou municipais.

B) Assessoria, pareceres e coordenação de projetos integram o campo quando relacionados aos campos da Administração e a seus desdobramentos ou conexões.

C) Planejamento e controle integram o campo somente quando resultam em documento contábil, pois as demais atividades dependem de outra profissão regulamentada.

D) Qualquer atividade técnica integra o campo por sua simples complexidade, ainda que não mantenha relação com a Administração nem com seus desdobramentos.

#### Extra Dia 3.3
- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** diferença entre requisito de formação e procedimento de provimento.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa do Dia 3 — Legislação: habilitação, diploma e concurso](semana_02_estudo.md#s2-d3-revisao-legislacao).

Um candidato apresenta o diploma exigido para o provimento de cargo técnico de Administração e afirma que, por isso, está dispensado do concurso previsto em lei. À luz da Lei nº 4.769/1965 e do Decreto nº 61.934/1967, a afirmação é:

A) correta, porque o diploma transforma o provimento em contratação direta.
B) correta, desde que o candidato ainda não possua registro no CRA.
C) incorreta apenas se o cargo estiver em empresa privada, pois concurso não se aplica à Administração Pública.
D) incorreta, porque a apresentação do diploma não dispensa a prestação de concurso quando este for exigido.
#### Extra Dia 3.4
- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** natureza do Sistema CFA/CRAs na Lei nº 4.769/1965.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa do Dia 3 — Legislação: natureza do Sistema](semana_02_estudo.md#s2-d3-revisao-legislacao).

Nos termos do art. 6º da Lei nº 4.769/1965, o CFA e os CRAs:

A) são associações privadas independentes, sem personalidade jurídica de direito público.
B) constituem, em conjunto, autarquia dotada de personalidade jurídica de direito público e autonomia técnica, administrativa e financeira.
C) integram a Administração Direta estadual e dependem de autorização do governador para exercer fiscalização.
D) formam empresa pública federal destinada exclusivamente à expedição de carteiras profissionais.
#### Extra Dia 3.5

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** competências do CFA.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Revisão fixa do Dia 3 — Legislação: CFA × CRA-PR](semana_02_estudo.md#s2-d3-revisao-legislacao), no contraste entre orientação federal, exame de regimentos e última instância versus execução regional.

Assinale a alternativa que reúne duas competências atribuídas ao CFA, e não aos Conselhos Regionais, pela Lei nº 4.769/1965.

A) Expedir carteiras aos inscritos da jurisdição e julgar, em primeira instância, as infrações profissionais ocorridas no respectivo estado.

B) Manter o registro regional dos profissionais e fiscalizar diretamente o exercício da profissão dentro da respectiva jurisdição territorial.

C) Examinar e aprovar os regimentos dos Regionais e julgar, em última instância, os recursos contra penalidades aplicadas por esses Conselhos.

D) Elaborar o próprio regimento regional e executar, na respectiva jurisdição, as diretrizes formuladas pelo Conselho Federal.

#### Extra Dia 3.6

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** finalidades dos Conselhos Regionais.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [Revisão fixa do Dia 3 — Legislação: competências dos CRAs](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente os verbos executar, fiscalizar, registrar, julgar e expedir.

Em relação às finalidades legais dos Conselhos Regionais de Administração, assinale a alternativa correta.

A) Executam as diretrizes do CFA, mantêm registros, fiscalizam a profissão na jurisdição, julgam infrações e expedem carteiras aos profissionais inscritos.

B) Fixam a orientação normativa nacional, alteram o Código de Ética e julgam em última instância os recursos contra penalidades de todos os Regionais.

C) Executam as diretrizes do CFA e mantêm registros, mas remetem toda fiscalização e todo julgamento de primeira instância diretamente ao Conselho Federal.

D) Fiscalizam a profissão na jurisdição e expedem carteiras, mas não podem manter registros nem aplicar as penalidades legalmente previstas aos inscritos.

#### Extra Dia 3.7

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** registro e carteira profissional.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [Revisão fixa do Dia 3 — Legislação: registro e carteira](semana_02_estudo.md#s2-d3-revisao-legislacao), na síntese do art. 14 sobre exigência do registro e funções da carteira.

Segundo o art. 14 da Lei nº 4.769/1965, assinale a alternativa correta sobre registro e carteira profissional.

A) O exercício depende de registro, mas a carteira é expedida pelo CFA, vale somente no estado emissor e não constitui documento de identidade.

B) O diploma substitui o registro, embora a carteira expedida pelo CRA sirva como identidade e produza fé em todo o território nacional.

C) A ausência de registro gera apenas pendência cadastral, e a carteira comprova a formação acadêmica sem provar o exercício da profissão.

D) O exercício depende de registro, cuja falta o torna ilegal e punível; a carteira prova o exercício, serve como identidade e tem fé nacional.

#### Extra Dia 3.8

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** registro de organizações e penalidades legais.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [Revisão fixa do Dia 3 — Legislação: arts. 15 e 16 da Lei](semana_02_estudo.md#s2-d3-revisao-legislacao), no trecho sobre registro de organizações, penalidades legais e reincidência da mesma infração em cinco anos.

Analise as afirmações sobre os arts. 15 e 16 da Lei nº 4.769/1965 e assinale a alternativa correta.

A) O registro alcança apenas pessoas físicas; na primeira infração da organização, aplicam-se multa em dobro e cancelamento automático do registro.

B) O registro alcança somente entidades públicas; advertência e censura são as únicas penalidades legais, sem consequência especial para reincidência.

C) Organizações que explorem as atividades previstas sujeitam-se a registro; a Lei prevê multa e suspensões e agrava a reincidência específica em cinco anos.

D) Organizações são dispensadas de registro se houver sócio inscrito; o cancelamento ocorre na primeira infração e independe de defesa ou enquadramento.

#### Extra Dia 3.9

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** detalhamento regulamentar da atividade profissional.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [Revisão fixa do Dia 3 — Legislação: Decreto nº 61.934/1967](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente os grupos de documentos, trabalhos, cargos, consultoria e magistério do art. 3º.

De acordo com o art. 3º do Decreto nº 61.934/1967, assinale a alternativa correta sobre a atividade profissional.

A) O magistério pertinente pode integrar a atividade, mas o dispositivo exclui consultoria, assessoramento e funções técnicas de direção ou chefia.

B) A elaboração de documentos técnicos integra a atividade, mas pesquisas, planejamento, implantação e controle pertencem a campo estranho ao Decreto.

C) Documentos e trabalhos técnicos podem integrar a atividade, assim como cargos de chefia, direção, consultoria e magistério que exijam conhecimentos de Administração.

D) Funções de assessoramento podem integrar a atividade, mas cargos de chefia e direção ficam excluídos mesmo quando exigem técnicas de Administração.

#### Extra Dia 3.10

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** elaboração e assinatura de documentos profissionais.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [Revisão fixa do Dia 3 — Legislação: documentos profissionais](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente as regras e ressalvas dos arts. 6º e 7º do Decreto nº 61.934/1967.

Considerando conjuntamente os arts. 6º e 7º do Decreto nº 61.934/1967, assinale a alternativa correta.

A) Documento do art. 3º deve ser elaborado e assinado por registrado, salvo o exercício de cargo público; cita-se o registro após a assinatura, ressalvado no art. 7º o documento oficial do ocupante do cargo.

B) Documento do art. 3º exige assinatura de registrado até no exercício de cargo público; cita-se o registro antes da assinatura, ressalvado no art. 7º todo documento produzido por empresa privada.

C) Documento do art. 3º pode ser elaborado por não registrado se receber assinatura posterior; a citação do registro é facultativa, ressalvado no art. 7º apenas o documento de autoridade federal.

D) Documento do art. 3º exige registrado apenas quando for laudo; autoridades não precisam cobrar assinatura regular, ressalvado no art. 7º todo documento apresentado por órgão público.

#### Extra Dia 3.11

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** exercício, registro e fiscalização no Decreto.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Revisão fixa do Dia 3 — Legislação: arts. 9º a 11 do Decreto](semana_02_estudo.md#s2-d3-revisao-legislacao), no trecho que articula carteira, direitos sociais, falta de registro e fiscalização pelo CRA e pelo CFA.

À luz dos arts. 9º a 11 do Decreto nº 61.934/1967, assinale a alternativa correta.

A) Exige-se apenas a carteira, sem prova dos direitos sociais; a experiência supre registro ausente, e a fiscalização cabe exclusivamente ao CFA.

B) Exigem-se carteira e prova do gozo dos direitos sociais; a falta de registro torna o exercício ilegal e punível, e CRA e CFA fiscalizam.

C) Exige-se apenas o diploma, pois a carteira é facultativa; a falta de registro gera advertência, e a fiscalização cabe exclusivamente ao CRA.

D) Exigem-se carteira e direitos sociais apenas do autônomo; o servidor atua sem registro, e a fiscalização cabe ao órgão público empregador.

#### Extra Dia 3.12

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** natureza e organização básica do CRA-PR.

- **Nível:** Médio

- **Uso:** Revisão

- **Referência:** [Revisão fixa do Dia 3 — Legislação: Regimento do CRA-PR](semana_02_estudo.md#s2-d3-revisao-legislacao), nos arts. 1º, 2º e 4º sintetizados sobre natureza, sede, jurisdição e Plenário.

Segundo o Regimento aprovado pela RN CFA nº 651/2024, assinale a descrição correta do CRA-PR e de seu Plenário.

A) É autarquia de direito público com jurisdição apenas na capital; seu Plenário atua como órgão consultivo sem competência de julgamento regional.

B) É associação privada com jurisdição em todo o Paraná; seu Plenário exerce administração cotidiana e julga apenas recursos contra decisões do CFA.

C) É autarquia de direito público com jurisdição nacional; seu Plenário constitui segunda instância federal e pode afastar as diretrizes emanadas do CFA.

D) É autarquia de direito público com sede na capital e jurisdição estadual; seu Plenário delibera em nível superior e julga a primeira instância regional.

#### Extra Dia 3.13

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** âmbito subjetivo e material do Código de Ética.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Revisão fixa do Dia 3 — Legislação: sujeitos do Código](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente o art. 4º, §§ 2º e 3º, sobre pessoas registradas e mandato eletivo.

Considere as afirmações sobre o âmbito do Código aprovado pela RN CFA nº 671/2025: I. alcança a pessoa física registrada quando exerce atividade abrangida; II. pode alcançar a pessoa jurídica registrada, observadas suas especificidades; III. considera o mandato eletivo no CFA ou nos CRAs atividade profissional para esse fim. Assinale a opção correta.

A) Estão corretas I, II e III, sem exclusão de nenhuma afirmação.

B) Estão corretas apenas I e II, ficando excluída a afirmação III.

C) Estão corretas apenas I e III, ficando excluída a afirmação II.

D) Estão corretas apenas II e III, ficando excluída a afirmação I.

#### Extra Dia 3.14

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** distinção entre dever e direito ético.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Revisão fixa do Dia 3 — Legislação: dever × direito × infração](semana_02_estudo.md#s2-d3-revisao-legislacao), no contraste entre comunicação cadastral, apontamento de falhas e condutas infracionais.

Assinale a alternativa que classifica corretamente a primeira conduta como dever e a segunda como direito na RN CFA nº 671/2025.

A) Dever: apontar falhas institucionais prejudiciais; direito: comunicar imediatamente ao CRA mudança relevante de endereço.

B) Dever: comunicar imediatamente mudança de endereço; direito: permitir que terceiro use o registro onde o profissional não atua.

C) Dever: comunicar imediatamente mudança de endereço; direito: apontar ao Sistema falhas institucionais indignas ou prejudiciais.

D) Dever: manter independência técnica; direito: assinar documento de terceiro sem orientação ou supervisão efetiva.

#### Extra Dia 3.15

- **Dia:** Dia 3

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** infrações, sanções, multa, processo e pessoa jurídica.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Revisão fixa do Dia 3 — Legislação: infrações e sanções](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente os arts. 6º, 13, 18, 22 e 23 sintetizados na revisão.

Considere as afirmações sobre a RN CFA nº 671/2025: I. assinar documento de terceiro sem orientação ou supervisão é infração; II. a sanção vem acompanhada da multa aplicável e depende de processo e trânsito administrativo; III. suspensão e cancelamento não se aplicam à pessoa jurídica; IV. a pessoa jurídica registrada fica fora de toda disciplina ética. Assinale a opção correta.

A) Estão corretas apenas I e II, ficando excluídas III e IV.

B) Estão corretas apenas I, III e IV, ficando excluída II.

C) Estão corretas apenas II e IV, ficando excluídas I e III.

D) Estão corretas apenas I, II e III, ficando excluída IV.

#### Extra Dia 3.16

- **Dia:** Dia 3

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** relação adversativa de conectores.

- **Nível:** Médio

- **Uso:** Simulado

- **Referência:** [Revisão fixa do Dia 3 — Português: conectores](semana_02_estudo.md#s2-d3-revisao-portugues), no quadro de relações de sentido que classifica “contudo” como adversativo.

Em “O CRA-PR possui autonomia administrativa; contudo, deve executar as diretrizes do CFA”, o conector destacado introduz uma relação de:

A) explicação causal.

B) oposição adversativa.

C) finalidade projetada.

D) conclusão lógica.

#### Extra Dia 3.17

- **Dia:** Dia 3

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** coesão referencial e ambiguidade pronominal.

- **Nível:** Médio

- **Uso:** Simulado

- **Referência:** [Revisão fixa do Dia 3 — Português: referência e ambiguidade](semana_02_estudo.md#s2-d3-revisao-portugues), no trecho sobre possessivo com dois antecedentes nominais compatíveis.

No período “O diretor entregou ao conselheiro seu relatório”, assinale a análise correta da referência do pronome possessivo.

A) “Seu” admite os dois antecedentes; a posse deve ser explicitada como “relatório do diretor” ou “relatório do conselheiro”, conforme a intenção.

B) “Seu” admite somente “conselheiro” por proximidade; deslocar o pronome para antes do substantivo elimina qualquer outra interpretação possível.

C) “Seu” admite somente “diretor” por exercer função de sujeito; trocar “entregou” por “encaminhou” resolve a referência sem indicar o possuidor.

D) “Seu” não admite antecedente pessoal nessa construção; retirar o possessivo torna inequívoco que o relatório pertence ao diretor.

#### Extra Dia 3.18
- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância com `haver`, `existir` e `fazer`.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Revisão fixa do Dia 3 — Português: haver, existir e concordância](semana_02_estudo.md#s2-d3-revisao-portugues).

Assinale a alternativa redigida de acordo com as regras de concordância estudadas.

A) Haviam três infrações registradas e deve existirem providências imediatas.
B) Fazem dois anos que o processo começou e houveram novas manifestações.
C) Deve haver providências, existiam inconsistências no relatório e faz dois anos que o processo começou.
D) Devem haver providências, existia três inconsistências e fazem dois anos desde a decisão.
#### Extra Dia 3.19

- **Dia:** Dia 3

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** fusão da preposição `a` com artigo feminino.

- **Nível:** Médio

- **Uso:** Simulado

- **Referência:** [Revisão fixa do Dia 3 — Português: crase](semana_02_estudo.md#s2-d3-revisao-portugues), especialmente o teste da fusão entre preposição e artigo e as vedações antes de verbo, termo masculino e certos pronomes.

Assinale a alternativa em que todos os empregos do acento grave obedecem à norma-padrão.

A) A comissão começou à examinar os autos e voltou à atuar durante a sessão.

B) A servidora dirigiu-se à unidade e entregou o ofício à gerente responsável.

C) O parecer foi remetido à um conselheiro e ficou disponível à qualquer interessado.

D) A equipe compareceu à cada setor e permaneceu face à face com os responsáveis.

#### Extra Dia 3.20

- **Dia:** Dia 3

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** pontuação de termos essenciais, oração deslocada e aposto.

- **Nível:** Médio

- **Uso:** Simulado

- **Referência:** [Revisão fixa do Dia 3 — Português: pontuação](semana_02_estudo.md#s2-d3-revisao-portugues), no contraste entre vírgula de termo deslocado ou aposto e separação indevida de termos essenciais.

Assinale a alternativa cuja pontuação está integralmente de acordo com a norma-padrão.

A) Durante a sessão, os conselheiros, analisaram o recurso administrativo.

B) A relatora apresentou, os fundamentos ao Plenário durante a reunião.

C) O parecer que havia sido revisado, recebeu a aprovação unânime do colegiado.

D) A relatora, responsável pelo parecer, apresentou sua conclusão ao Plenário.

## Gabarito das questões extras do Dia 3

| Extra | Resposta |
|---:|:---:|
| 3.1 | C |
| 3.2 | B |
| 3.3 | D |
| 3.4 | B |
| 3.5 | C |
| 3.6 | A |
| 3.7 | D |
| 3.8 | C |
| 3.9 | C |
| 3.10 | A |
| 3.11 | B |
| 3.12 | D |
| 3.13 | A |
| 3.14 | C |
| 3.15 | D |
| 3.16 | B |
| 3.17 | A |
| 3.18 | C |
| 3.19 | B |
| 3.20 | D |

## Comentários das questões extras do Dia 3

#### Comentário Extra Dia 3.1

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** a Lei não organiza internamente o CRA-PR, o Decreto não aprova o Código e as duas resoluções tiveram seus objetos trocados.
- **B)** a alternativa redistribui incorretamente os objetos das quatro bases e atribui ao Decreto a criação legal do Sistema.
- **C)** cada norma foi associada à sua função própria, da disciplina legal do exercício à aprovação do Código de Ética.
- **D)** o Decreto regulamenta a Lei, o Regimento é aprovado pela RN nº 651 e nenhuma das resoluções cria a profissão ou a estrutura legal dos Conselhos.

**Conceito:** função distinta e complementar da Lei, do Decreto, do Regimento e do Código de Ética.

**Pegadinha:** trocar os objetos das RNs nº 651 e nº 671 e confundir regulamentação com criação legal.

**Como pensar:** associe cada documento a um verbo: a Lei disciplina, o Decreto regulamenta, o Regimento organiza e o Código orienta a conduta.

**Referência:** [Revisão fixa do Dia 3 — Legislação: relação entre as normas](semana_02_estudo.md#s2-d3-revisao-legislacao), no quadro que separa Lei, Decreto, Regimento do CRA-PR e Código de Ética.

#### Comentário Extra Dia 3.2

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** o campo profissional não se restringe à esfera federal nem exclui, por esse motivo, a atuação em organizações privadas.
- **B)** o artigo inclui assessoria, documentos técnicos e trabalhos de coordenação ligados aos campos da Administração e a suas conexões.
- **C)** planejamento e controle são atividades contempladas e não dependem de se converterem em documento contábil.
- **D)** a complexidade técnica isolada não basta; a atividade precisa manter o vínculo material definido pela Lei.

**Conceito:** alcance material das atividades previstas no art. 2º da Lei nº 4.769/1965.

**Pegadinha:** restringir o campo por setor ou ampliá-lo para toda tarefa técnica sem conexão com Administração.

**Como pensar:** verifique primeiro a atividade e depois o vínculo dela com os campos da Administração, seus desdobramentos ou conexões.

**Referência:** [Revisão fixa do Dia 3 — Legislação: Lei nº 4.769/1965](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente a síntese do art. 2º sobre documentos, funções e trabalhos nos campos da Administração.

#### Comentário Extra Dia 3.3
**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Essenciais

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

**Nível:** Médio

**Uso:** Essenciais

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

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** expedição ordinária de carteiras e julgamento em primeira instância são atribuições regionais.
- **B)** manutenção de registro e fiscalização na jurisdição integram o núcleo de atuação dos CRAs.
- **C)** exame de regimentos regionais e julgamento de recursos em última instância pertencem ao CFA.
- **D)** elaboração do regimento próprio e execução territorial de diretrizes são tarefas do Conselho Regional.

**Conceito:** separação de competências entre o CFA e os Conselhos Regionais.

**Pegadinha:** apresentar atribuições verdadeiras do Sistema, mas situá-las no nível federativo errado.

**Como pensar:** associe uniformização e última instância ao CFA; associe registro, fiscalização e primeira instância ao CRA.

**Referência:** [Revisão fixa do Dia 3 — Legislação: CFA × CRA-PR](semana_02_estudo.md#s2-d3-revisao-legislacao), no contraste entre orientação federal, exame de regimentos e última instância versus execução regional.

#### Comentário Extra Dia 3.6

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** a opção reúne funções regionais previstas na Lei e detalhadas no Decreto.
- **B)** orientação nacional, alteração do Código e última instância recursal pertencem ao CFA.
- **C)** fiscalização e julgamento regional de primeira instância não são transferidos integralmente ao Conselho Federal.
- **D)** os CRAs mantêm registros e podem impor as penalidades previstas no âmbito de suas competências.

**Conceito:** núcleo funcional dos Conselhos Regionais de Administração.

**Pegadinha:** deslocar atribuições entre o nível federal e o regional ou retirar parte do rol regional.

**Como pensar:** procure a alternativa que mantenha juntos os verbos regionais executar, fiscalizar, registrar, julgar e expedir.

**Referência:** [Revisão fixa do Dia 3 — Legislação: competências dos CRAs](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente os verbos executar, fiscalizar, registrar, julgar e expedir.

#### Comentário Extra Dia 3.7

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** a carteira é expedida pelo Conselho Regional, tem fé nacional e também funciona como documento de identidade.
- **B)** diploma e registro cumprem funções diferentes, de modo que o primeiro não substitui o segundo.
- **C)** a falta de registro torna ilegal e punível o exercício, e a carteira é prova do exercício profissional.
- **D)** a opção preserva tanto o efeito jurídico do registro quanto as três funções legais da carteira.

**Conceito:** exigência de registro e eficácia jurídica da carteira profissional.

**Pegadinha:** trocar o órgão expedidor, limitar a fé territorial ou fazer o diploma substituir a inscrição.

**Como pensar:** separe habilitação acadêmica, registro profissional e documento comprobatório; cada elemento possui função própria.

**Referência:** [Revisão fixa do Dia 3 — Legislação: registro e carteira](semana_02_estudo.md#s2-d3-revisao-legislacao), na síntese do art. 14 sobre exigência do registro e funções da carteira.

#### Comentário Extra Dia 3.8

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** organizações abrangidas também se sujeitam a registro, e a primeira infração não produz automaticamente a consequência agravada descrita.
- **B)** o registro não se limita a entidades públicas, e advertência e censura pertencem ao catálogo ético, não esgotam as penalidades da Lei.
- **C)** a alternativa combina o registro da pessoa jurídica, as penalidades legais e a regra de agravamento da reincidência específica.
- **D)** a inscrição de um sócio não gera a dispensa indicada, e cancelamento não decorre automaticamente de qualquer primeira infração.

**Conceito:** registro de organizações e disciplina legal das penalidades e da reincidência.

**Pegadinha:** confundir as sanções da Lei com as do Código de Ética e antecipar a consequência da reincidência.

**Como pensar:** confira três blocos sucessivos: quem se registra, quais penalidades a Lei prevê e quando incide o agravamento.

**Referência:** [Revisão fixa do Dia 3 — Legislação: arts. 15 e 16 da Lei](semana_02_estudo.md#s2-d3-revisao-legislacao), no trecho sobre registro de organizações, penalidades legais e reincidência da mesma infração em cinco anos.

#### Comentário Extra Dia 3.9

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** o artigo não exclui consultoria, assessoramento nem cargos técnicos de direção e chefia.
- **B)** pesquisa, planejamento, implantação, coordenação e controle fazem parte do detalhamento regulamentar.
- **C)** a opção reúne os principais grupos do dispositivo e preserva o vínculo com conhecimentos de Administração.
- **D)** chefia e direção podem integrar a atividade quando exigem a aplicação de técnicas próprias do campo profissional.

**Conceito:** alcance das atividades profissionais detalhadas no art. 3º do Decreto.

**Pegadinha:** aceitar um exemplo verdadeiro e, na mesma alternativa, excluir outros grupos expressamente previstos.

**Como pensar:** rejeite opções que tratem um dos grupos do artigo como se ele excluísse documentos, gestão, consultoria ou ensino pertinente.

**Referência:** [Revisão fixa do Dia 3 — Legislação: Decreto nº 61.934/1967](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente os grupos de documentos, trabalhos, cargos, consultoria e magistério do art. 3º.

#### Comentário Extra Dia 3.10

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** a opção preserva a elaboração e assinatura por registrado, a ressalva do cargo público, a posição do número de registro e a exceção do documento oficial.
- **B)** ignora a ressalva do art. 6º, desloca o número para antes da assinatura e inventa exceção geral para empresas privadas.
- **C)** assinatura posterior não substitui a elaboração regular, o número é obrigatório e a ressalva não se limita a autoridade federal.
- **D)** a exigência não se restringe a laudos, e autoridades e empresas privadas devem cobrar a assinatura nas condições do art. 7º.

**Conceito:** elaboração, assinatura, número de registro e ressalvas aplicáveis aos documentos profissionais.

**Pegadinha:** fundir os dois artigos, ampliar suas exceções ou tratar assinatura posterior como regularização automática.

**Como pensar:** confira separadamente quem elabora e assina, onde aparece o registro, quem deve exigir a assinatura e qual documento oficial é ressalvado.

**Referência:** [Revisão fixa do Dia 3 — Legislação: documentos profissionais](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente as regras e ressalvas dos arts. 6º e 7º do Decreto nº 61.934/1967.

#### Comentário Extra Dia 3.11

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** o Decreto também exige prova do gozo dos direitos sociais, não admite experiência como registro e não reserva a fiscalização ao CFA.
- **B)** a alternativa integra corretamente os requisitos do art. 9º, o efeito do art. 10 e a competência fiscalizatória do art. 11.
- **C)** diploma não substitui carteira e registro, o exercício sem registro é ilegal e o CFA também participa da fiscalização.
- **D)** as regras não criam a dispensa geral indicada para servidor, nem entregam a fiscalização ao órgão empregador.

**Conceito:** requisitos do exercício profissional, consequência da falta de registro e órgãos fiscalizadores.

**Pegadinha:** fazer diploma ou experiência substituir registro e atribuir a fiscalização a um único órgão.

**Como pensar:** vincule cada artigo a uma etapa: art. 9º comprovação, art. 10 irregularidade do exercício e art. 11 fiscalização.

**Referência:** [Revisão fixa do Dia 3 — Legislação: arts. 9º a 11 do Decreto](semana_02_estudo.md#s2-d3-revisao-legislacao), no trecho que articula carteira, direitos sociais, falta de registro e fiscalização pelo CRA e pelo CFA.

#### Comentário Extra Dia 3.12

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** a jurisdição alcança todo o Paraná, e o Plenário possui competência deliberativa e julgadora.
- **B)** o CRA-PR é autarquia de direito público, e o Plenário não se reduz à administração cotidiana nem julga recursos do CFA.
- **C)** a jurisdição é estadual, a primeira instância é regional e a autonomia não afasta as diretrizes federais.
- **D)** a descrição reúne corretamente natureza, sede, alcance territorial e posição regimental do Plenário.

**Conceito:** natureza e organização institucional básica do CRA-PR.

**Pegadinha:** confundir autonomia com soberania, ampliar a jurisdição ou trocar a instância ocupada pelo Plenário.

**Como pensar:** fixe quatro chaves contíguas: autarquia pública, sede na capital, jurisdição paranaense e Plenário como deliberação superior e primeira instância.

**Referência:** [Revisão fixa do Dia 3 — Legislação: Regimento do CRA-PR](semana_02_estudo.md#s2-d3-revisao-legislacao), nos arts. 1º, 2º e 4º sintetizados sobre natureza, sede, jurisdição e Plenário.

#### Comentário Extra Dia 3.13

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** as três afirmações reproduzem aspectos complementares do âmbito subjetivo e material do Código.
- **B)** o mandato eletivo exercido no CFA ou nos CRAs também é considerado atividade profissional para a incidência ética.
- **C)** pessoas jurídicas registradas podem ser alcançadas, desde que se observem suas especificidades.
- **D)** a pessoa física registrada no exercício de atividade abrangida constitui sujeito típico do Código.

**Conceito:** incidência do Código sobre pessoas físicas, pessoas jurídicas e titulares de mandato no Sistema.

**Pegadinha:** excluir uma das três hipóteses expressamente contempladas ou tratar o alcance como restrito à pessoa natural.

**Como pensar:** valide separadamente registro e atividade, especificidades da pessoa jurídica e regra própria do mandato eletivo.

**Referência:** [Revisão fixa do Dia 3 — Legislação: sujeitos do Código](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente o art. 4º, §§ 2º e 3º, sobre pessoas registradas e mandato eletivo.

#### Comentário Extra Dia 3.14

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** as condutas existem no Código, mas suas categorias foram invertidas; apontar falhas é direito e comunicar endereço é dever.
- **B)** a primeira classificação está correta, porém permitir uso do registro onde não atua constitui infração, não direito.
- **C)** a comunicação cadastral imediata é dever, e o apontamento qualificado de falhas ao Sistema é direito.
- **D)** independência técnica é dever, mas assinar documento de terceiro sem orientação ou supervisão é infração.

**Conceito:** diferença funcional entre dever, direito e infração no Código de Ética.

**Pegadinha:** inverter categorias de condutas lícitas ou apresentar uma infração como prerrogativa profissional.

**Como pensar:** pergunte se o Código manda agir, protege uma faculdade ou tipifica uma proibição antes de classificar cada conduta.

**Referência:** [Revisão fixa do Dia 3 — Legislação: dever × direito × infração](semana_02_estudo.md#s2-d3-revisao-legislacao), no contraste entre comunicação cadastral, apontamento de falhas e condutas infracionais.

#### Comentário Extra Dia 3.15

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** a afirmação III também está correta, pois suspensão e cancelamento são incompatíveis com pessoa jurídica.
- **B)** II é verdadeira e IV é falsa; gravidade aparente não dispensa o processo nem o trânsito em julgado administrativo.
- **C)** I e III são verdadeiras, enquanto IV é falsa porque a pessoa jurídica registrada pode submeter-se à disciplina compatível.
- **D)** I descreve infração, II preserva multa e garantias processuais, III limita sanções incompatíveis e IV universaliza uma exclusão inexistente.

**Conceito:** articulação entre tipificação, devido processo, multa e sanções aplicáveis à pessoa jurídica.

**Pegadinha:** confundir a incompatibilidade de duas sanções com exclusão completa da pessoa jurídica do Código.

**Como pensar:** siga a sequência conduta tipificada, processo, trânsito, sanção e compatibilidade com a natureza do sujeito.

**Referência:** [Revisão fixa do Dia 3 — Legislação: infrações e sanções](semana_02_estudo.md#s2-d3-revisao-legislacao), especialmente os arts. 6º, 13, 18, 22 e 23 sintetizados na revisão.

#### Comentário Extra Dia 3.16

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** a segunda oração não apresenta a causa da autonomia administrativa.
- **B)** a segunda oração estabelece ressalva ou contraste em relação à expectativa de independência sugerida pela primeira.
- **C)** não há propósito introduzido, que poderia ser marcado por “para que” ou expressão equivalente.
- **D)** “contudo” não extrai uma conclusão; conectores conclusivos seriam “portanto” ou “logo”.

**Conceito:** valor semântico adversativo de conectores.

**Pegadinha:** interpretar a obrigação como consequência da autonomia, em vez de limite à leitura absoluta dessa autonomia.

**Como pensar:** substitua “contudo” por “porém”; se o sentido central permanecer, a relação é adversativa.

**Referência:** [Revisão fixa do Dia 3 — Português: conectores](semana_02_estudo.md#s2-d3-revisao-portugues), no quadro de relações de sentido que classifica “contudo” como adversativo.

#### Comentário Extra Dia 3.17

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** diretor e conselheiro são antecedentes masculinos possíveis, e a explicitação nominal seleciona a leitura pretendida.
- **B)** proximidade linear não cria regra de retomada obrigatória, e a posição do possessivo não identifica por si só o possuidor.
- **C)** a função de sujeito não garante exclusividade referencial, e a mera troca do verbo mantém os dois candidatos.
- **D)** o possessivo pode retomar pessoa, e sua retirada deixa a posse indefinida em vez de atribuí-la ao diretor.

**Conceito:** coesão referencial e resolução de ambiguidade pronominal.

**Pegadinha:** tratar proximidade ou função sintática como regra automática de antecedência.

**Como pensar:** teste o possessivo com cada nome compatível; se ambas as leituras funcionarem, nomeie expressamente o possuidor.

**Referência:** [Revisão fixa do Dia 3 — Português: referência e ambiguidade](semana_02_estudo.md#s2-d3-revisao-portugues), no trecho sobre possessivo com dois antecedentes nominais compatíveis.

#### Comentário Extra Dia 3.18
**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

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

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** não ocorre crase antes dos infinitivos “examinar” e “atuar”.
- **B)** “dirigir-se” e “entregar” exigem preposição, e os nomes femininos determinados admitem os artigos que formam “à unidade” e “à gerente”.
- **C)** não se usa crase diante do artigo masculino “um” nem, nesse contexto, diante do pronome indefinido “qualquer”.
- **D)** “cada” não admite o artigo feminino necessário, e a locução cristalizada é “face a face”, sem crase.

**Conceito:** fusão da preposição “a” com artigo feminino em complementos regidos.

**Pegadinha:** aplicar o acento grave diante de verbo, termo masculino, pronome indefinido ou expressão repetida.

**Como pensar:** verifique primeiro a regência e depois a presença do artigo; só a coexistência dos dois elementos produz crase.

**Referência:** [Revisão fixa do Dia 3 — Português: crase](semana_02_estudo.md#s2-d3-revisao-portugues), especialmente o teste da fusão entre preposição e artigo e as vedações antes de verbo, termo masculino e certos pronomes.

#### Comentário Extra Dia 3.20

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** a segunda vírgula separa indevidamente o sujeito “os conselheiros” do verbo “analisaram”.
- **B)** a vírgula separa o verbo “apresentou” de seu objeto direto “os fundamentos”.
- **C)** a vírgula colocada depois da oração restritiva separa o sujeito completo do predicado.
- **D)** as duas vírgulas isolam adequadamente o aposto explicativo “responsável pelo parecer”.

**Conceito:** emprego da vírgula em aposto e proibição de separar termos essenciais.

**Pegadinha:** inserir pausa gráfica entre sujeito e verbo ou entre verbo e complemento.

**Como pensar:** identifique o núcleo do sujeito e os complementos do verbo; depois isole apenas o segmento explicativo intercalado.

**Referência:** [Revisão fixa do Dia 3 — Português: pontuação](semana_02_estudo.md#s2-d3-revisao-portugues), no contraste entre vírgula de termo deslocado ou aposto e separação indevida de termos essenciais.

# Dia 4 — Segurança da Informação e Redes

## Questões principais

### S2D4Q151 — Gestão contínua do risco após a implantação de um controle

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [1. Segurança como gestão de risco](semana_02_estudo.md#s2-d4-gestao-risco), especialmente as seis etapas do processo e o tratamento do risco residual.

Depois de implantar um WAF no portal institucional, a equipe propõe encerrar a análise porque considera o ambiente definitivamente seguro. À luz da gestão de riscos, assinale a alternativa correta.

A) Encerrar a análise após o WAF, registrar o risco como eliminado e reabrir a avaliação somente se ocorrer um incidente no portal.

B) Aplicar a mesma configuração a todos os ativos, registrar conformidade uniforme e substituir a reavaliação por varreduras periódicas.

C) Revisar ativos, ameaças e vulnerabilidades, estimar probabilidade e impacto, acompanhar o controle e decidir sobre o risco residual.

D) Restringir a análise a falhas técnicas do portal, mantendo pessoas, processos, fornecedores e mudanças operacionais fora do risco.

### S2D4Q152 — Risco residual e decisão de tratamento após a aplicação de controles

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Segurança como gestão de risco](semana_02_estudo.md#s2-d4-gestao-risco).

Após implantar MFA, segmentação e monitoramento, uma organização reavalia o risco de acesso indevido. Sobre o risco residual, assinale a alternativa correta.

A) É o risco que permanece após os controles e deve ser reavaliado para aceitação ou tratamento adicional conforme o contexto.
B) Deve ser obrigatoriamente igual a zero para que o serviço possa permanecer em operação.
C) Deve ser sempre transferido a terceiro, ainda que seja compatível com os critérios de aceitação da organização.
D) Corresponde ao risco calculado antes da aplicação dos controles e deixa de existir assim que uma medida preventiva é implantada.

### S2D4Q153 — Confidencialidade como prevenção da divulgação não autorizada

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

Durante o transporte, foi perdido um disco de backup não cifrado que continha dados pessoais. Não há evidência de modificação ou destruição dos arquivos. O objetivo de segurança diretamente ameaçado é a:

A) confidencialidade.
B) integridade.
C) disponibilidade.
D) autenticidade.

### S2D4Q154 — Um único incidente pode comprometer simultaneamente os três objetivos da tríade CIA

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia) e [Malware](semana_02_estudo.md#s2-d4-malware).

Considere as afirmativas sobre um incidente de ransomware.

I. A exfiltração de uma base antes da cifração pode comprometer a confidencialidade.
II. A alteração ou cifração não autorizada de arquivos pode comprometer a integridade e a disponibilidade.
III. A existência de backup íntegro impede o vazamento e evita necessariamente a interrupção inicial.

Está correto o que se afirma em:

A) I, apenas.
B) III, apenas.
C) I, II e III.
D) I e II, apenas.

### S2D4Q155 — Autenticação comprova identidade; autorização determina ações permitidas

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

Em um sistema do conselho, o usuário apresenta sua senha e um token válido. Depois, o sistema consulta o papel funcional para decidir se ele pode alterar um cadastro. As duas etapas correspondem, respectivamente, a:

A) autorização e autenticação.
B) autenticação e autorização.
C) accounting e não repúdio.
D) auditoria e accounting.

### S2D4Q156 — MFA requer fatores pertencentes a categorias diferentes de autenticação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

Assinale a alternativa que apresenta autenticação multifator, considerando que os fatores devem pertencer a categorias diferentes.

A) Senha pessoal e PIN memorizado.
B) Duas senhas distintas cadastradas pelo mesmo usuário.
C) Impressão digital e reconhecimento facial.
D) Senha pessoal e token criptográfico sob posse do usuário.

### S2D4Q157 — Decisão de acesso por atributos de sujeito, recurso, ação e contexto

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [3.2 Autorização](semana_02_estudo.md#s2-d4-identidade-auditoria), nos trechos que distinguem RBAC, ABAC, listas de controle de acesso e accounting.

Uma política permite exportar um relatório somente quando departamento do usuário, classificação do recurso, ação solicitada, estado do dispositivo e horário atendem às condições definidas. O modelo predominante é:

A) ACL estrita, porque cada decisão depende apenas de uma entrada fixa entre uma identidade e um recurso, sem outros atributos.

B) RBAC, porque qualquer característica do usuário transforma todas as condições contextuais em um único papel funcional.

C) ABAC, porque a decisão combina atributos do sujeito, do recurso, da ação e do contexto em que a solicitação ocorre.

D) Accounting, porque o registro posterior da sessão avalia os atributos e concede a autorização antes de cada operação.

### S2D4Q158 — Função do accounting no modelo AAA

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [3.3 Auditoria e accounting](semana_02_estudo.md#s2-d4-identidade-auditoria) e [3.5 Modelo AAA](semana_02_estudo.md#s2-d4-identidade-auditoria), especialmente a diferença entre produzir registros e examiná-los.

Um concentrador registra início e término das sessões, volume consumido e operações realizadas por cada identidade. No modelo AAA, essa função deve ser classificada como:

A) Authentication, pois o registro da sessão é suficiente para comprovar novamente a identidade que iniciou o acesso.

B) Authorization, pois os dados de consumo definem por si sós os recursos que o usuário poderá acessar na sessão.

C) Accounting, pois registra sessões, consumo e ações para controle e responsabilização e fornece insumos à auditoria.

D) Auditoria, pois a produção automática de qualquer log já constitui exame completo de controles e conformidade.

### S2D4Q159 — Não repúdio apoiado por assinatura digital e por uma cadeia adequada de evidências

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

Um documento eletrônico precisa oferecer evidência que dificulte a negação falsa da autoria perante terceiro. Qual alternativa descreve a solução mais adequada?

A) Publicar apenas um hash sem vínculo com identidade, pois qualquer pessoa poderá recalculá-lo.
B) Empregar assinatura digital, com proteção da chave privada, vínculo confiável entre identidade e chave e trilha de evidências apropriada.
C) Cifrar o documento com uma chave simétrica compartilhada entre todos os envolvidos, pois qualquer detentor da chave identifica exclusivamente o autor.
D) Registrar o nome declarado pelo usuário em arquivo de texto sem controle de integridade.

### S2D4Q160 — Contexto, integridade e correlação temporal dos registros

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [3.3 Auditoria e accounting](semana_02_estudo.md#s2-d4-identidade-auditoria), especialmente os campos de contexto e os requisitos de sincronização, retenção, acesso, integridade e análise.

Uma investigação precisa correlacionar ações entre portal, proxy e diretório. Hoje os relógios divergem, alguns eventos não identificam origem nem resultado e os operadores podem editar os arquivos locais. Qual plano produz registros mais úteis e confiáveis?

A) Registrar quem fez o quê, quando, de onde, sobre qual recurso e com qual resultado, sincronizar relógios, restringir alterações e definir retenção e análise.

B) Sincronizar os relógios e centralizar os eventos, registrar apenas ações bem-sucedidas e dispensar proteção de integridade para reduzir o volume armazenado.

C) Registrar ação e resultado e proteger os arquivos, substituir a identidade pelo IP da estação e eliminar os eventos assim que terminar a coleta diária.

D) Registrar identidade e recurso, manter os relógios locais sem correlação e permitir que os operadores ajustem eventos antigos quando notarem divergências.

### S2D4Q161 — Distinção operacional entre ativo, ameaça, vulnerabilidade, evento e incidente

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

Em um cenário de segurança, o portal de serviços tem valor para a missão; um grupo criminoso pode atacá-lo; o gateway possui falha conhecida ainda não corrigida; milhares de tentativas de login são observadas; e um acesso indevido é confirmado. A classificação correta é:

A) portal: ativo; grupo criminoso: ameaça; falha não corrigida: vulnerabilidade; tentativas observadas: evento; acesso indevido confirmado: incidente.
B) portal: ameaça; grupo criminoso: vulnerabilidade; falha não corrigida: risco; tentativas observadas: incidente; acesso indevido: evento.
C) portal: controle; grupo criminoso: ativo; falha não corrigida: incidente; tentativas observadas: risco; acesso indevido: ameaça.
D) portal: vulnerabilidade; grupo criminoso: evento; falha não corrigida: ativo; tentativas observadas: controle; acesso indevido: risco.

### S2D4Q162 — Vulnerabilidade como fraqueza e risco como combinação de probabilidade e impacto

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

Um serviço exposto utiliza versão de software com falha explorável. A equipe ainda está estimando a chance de exploração e o impacto sobre dados e operação. Nesse caso:

A) a falha explorável já é, por definição, um incidente confirmado.
B) a chance de exploração isolada é o ativo, e o impacto é a ameaça.
C) vulnerabilidade e risco são sinônimos, pois ambos existem antes do ataque.
D) a falha é uma vulnerabilidade, enquanto o risco considera probabilidade e impacto adverso.

### S2D4Q163 — Evento observado em contraste com incidente de segurança confirmado

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

Um sensor gera alerta de tráfego incomum. Após correlação com registros de identidade e aplicação, confirma-se que uma conta foi usada para copiar dados sem autorização. Assinale a alternativa correta.

A) O alerta inicial já prova, necessariamente, a ocorrência e o alcance do incidente.
B) Tanto o alerta quanto a cópia confirmada são apenas vulnerabilidades.
C) A cópia não autorizada é uma ameaça potencial, mas não um incidente enquanto o atacante não for identificado.
D) O alerta é uma ocorrência observável a ser analisada; a cópia indevida confirmada caracteriza incidente.

### S2D4Q164 — Relação entre ameaça, vulnerabilidade e controle

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [4. Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco), na tabela de conceitos e no exemplo do gateway VPN.

Um grupo criminoso pode explorar uma falha conhecida no gateway VPN; a equipe avalia aplicar a correção e exigir MFA. Assinale a classificação correta dos três elementos.

A) O grupo é vulnerabilidade, a falha é controle e a correção com MFA representa a ameaça ao serviço.

B) O grupo é ameaça, a falha é vulnerabilidade e a correção com MFA representa controles que modificam o risco.

C) O grupo é incidente, a falha é ameaça e a correção com MFA representa o ativo protegido pelo gateway.

D) O grupo é risco, a falha é incidente e a correção com MFA representa o evento observado pela equipe.

### S2D4Q165 — Mecanismo de propagação de vírus e worm

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5.1 Vírus e 5.2 Worm](semana_02_estudo.md#s2-d4-malware), nos trechos que distinguem vínculo a hospedeiro e propagação automática por redes ou sistemas.

Em laboratório, a amostra X insere código em um executável e se dissemina quando o hospedeiro infectado é executado; a amostra Y procura outros sistemas e envia cópias de si sem depender de arquivo hospedeiro. A conclusão correta é:

A) X apresenta comportamento de vírus, e Y, de worm; o critério decisivo é vínculo ao hospedeiro versus propagação automática.

B) X apresenta comportamento de worm, e Y, de vírus; a dependência de um executável caracteriza autorreplicação pela rede.

C) X e Y apresentam comportamento de worm; compartilhar cópias torna irrelevante a dependência de programa hospedeiro.

D) X e Y apresentam comportamento de vírus; toda amostra maliciosa recebe essa classificação, qualquer que seja sua propagação.

### S2D4Q166 — Disfarce e execução induzida em cavalo de Troia

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [5.3 Cavalo de Troia](semana_02_estudo.md#s2-d4-malware), em contraste com os mecanismos de vírus, worm e spyware descritos na mesma seção.

Um arquivo oferecido como atualização legítima é executado pelo usuário e instala acesso remoto oculto, sem infectar outro programa nem procurar automaticamente novos sistemas. A classificação principal é:

A) worm, porque a abertura de acesso remoto demonstra que o código possui mecanismo de propagação automática.

B) vírus, porque apresentar-se como atualização implica necessariamente inserir código em um arquivo hospedeiro.

C) cavalo de Troia, porque o disfarce induz a execução e a categoria não exige autorreplicação obrigatória.

D) spyware, porque qualquer acesso remoto oculto tem como finalidade exclusiva coletar informações do usuário.

### S2D4Q167 — Alcance do ransomware e sobreposição de categorias e efeitos de malware

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Malware](semana_02_estudo.md#s2-d4-malware) e [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

Uma campanha maliciosa copia documentos, cifra compartilhamentos e interrompe o portal. Sobre a classificação e os controles envolvidos, assinale a alternativa correta.

A) Trata-se necessariamente de spyware, porque ransomware afeta somente a disponibilidade.
B) O backup elimina a necessidade de conter o atacante e investigar eventual exfiltração.
C) Ransomware pode combinar exfiltração, alteração ou cifração e interrupção, atingindo confidencialidade, integridade e disponibilidade.
D) A cifração autorizada pelo atacante preserva a integridade, pois o conteúdo original ainda pode existir em backup.

### S2D4Q168 — Spyware, rootkit, bot e botnet como categorias distintas de malware

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Malware](semana_02_estudo.md#s2-d4-malware).

Assinale a associação correta entre categorias de malware.

A) Rootkit: conjunto distribuído de máquinas usado exclusivamente em DDoS; botnet: ferramenta que apenas oculta privilégios locais.
B) Spyware: coleta informações; rootkit: busca ocultar presença ou manter privilégio; botnet: conjunto de bots sob controle.
C) Bot: arquivo hospedeiro que só se propaga após execução manual; vírus: dispositivo comprometido controlado remotamente.
D) Spyware: cifra arquivos para extorsão; rootkit: mensagem fraudulenta enviada por SMS; botnet: falha de configuração.

### S2D4Q169 — Classificação de phishing por alvo e canal

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [6. Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing), na lista que distingue alvo específico, pessoa de alta relevância, SMS ou mensagem e voz.

Considere quatro campanhas: I. mensagem SMS leva servidores a uma página falsa; II. ligação de voz solicita um código de acesso; III. e-mail personalizado mira um analista específico; IV. e-mail elaborado mira a presidência do órgão. A associação correta é:

A) I–vishing; II–smishing; III–spear phishing; IV–whaling.

B) I–smishing; II–vishing; III–spear phishing; IV–whaling.

C) I–smishing; II–vishing; III–whaling; IV–spear phishing.

D) I–whaling; II–spear phishing; III–smishing; IV–vishing.

### S2D4Q170 — Manipulação por autoridade, urgência e pretexto, com verificação por canal independente

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing).

Um servidor recebe mensagem urgente, aparentemente enviada pela presidência, pedindo alteração imediata dos dados bancários de um fornecedor. A ação mais adequada é:

A) verificar a solicitação por canal independente e seguir o procedimento de autorização, mesmo que a mensagem use autoridade e urgência.
B) atender imediatamente, pois mensagens de alta autoridade dispensam confirmação.
C) responder à própria mensagem pedindo confirmação, pois isso garante que o remetente aparente controla a conta.
D) considerar a mensagem legítima se não houver anexo executável, já que engenharia social depende de malware.

### S2D4Q171 — Alcance e limites do MFA diante de phishing

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing).

Quanto ao uso de MFA contra phishing, assinale a alternativa correta.

A) MFA impede todo phishing, porque elimina a possibilidade de o usuário acessar página falsa.
B) MFA protege a conta mesmo quando o atacante captura uma sessão autenticada ou controla a recuperação da conta.
C) Dois segredos do tipo senha constituem MFA e neutralizam qualquer reutilização de credenciais.
D) MFA reduz o impacto do roubo de senha, mas certos ataques podem capturar sessão, induzir aprovação ou explorar a recuperação da conta.

### S2D4Q172 — Spoofing de IP e limite do caminho de retorno

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [7.1 Spoofing](semana_02_estudo.md#s2-d4-ataques-rede), especialmente a definição de falsificação de origem e a ressalva sobre o retorno em IP spoofing.

Um sensor registra datagramas com endereço IP de origem pertencente a terceiros. O serviço envia as respostas a esses endereços, e não há evidência de sessão bidirecional com o emissor. Assinale a análise correta.

A) O caso caracteriza sniffing, pois a simples captura passiva permite escolher a origem e receber todas as respostas do serviço.

B) O caso é compatível com spoofing, pois a origem pode ter sido falsificada; essa falsificação, isoladamente, não garante ao emissor o retorno das respostas.

C) O caso comprova ataque on-path, pois todo endereço de origem falsificado coloca o emissor no caminho e lhe entrega o tráfego de retorno.

D) O caso comprova DDoS, pois a falsificação de origem demonstra múltiplos sistemas comprometidos e controle bidirecional das conexões.

### S2D4Q173 — Captura passiva e interceptação ativa no caminho

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [7.2 Sniffing e 7.3 Man-in-the-middle ou ataque on-path](semana_02_estudo.md#s2-d4-ataques-rede), incluindo a ressalva sobre criptografia com validação correta.

Em teste autorizado, a equipe usa espelhamento de porta para copiar quadros sem alterar o fluxo. Em outro caso, um invasor redireciona o tráfego pelo próprio equipamento e apresenta certificado falso, rejeitado pelo cliente. A interpretação correta é:

A) O primeiro caso é sniffing; o segundo é ataque on-path, e a validação correta do certificado pode impedir que o cliente aceite o endpoint substituído.

B) O primeiro caso é on-path; o segundo é sniffing, e a rejeição do certificado demonstra que nenhum posicionamento intermediário ocorreu.

C) Os dois casos são sniffing, pois ataque on-path só existe depois que o invasor consegue alterar com sucesso o conteúdo da aplicação.

D) Os dois casos são on-path, pois qualquer observação de quadros exige encaminhamento ativo e torna irrelevante a validação do certificado.

### S2D4Q174 — Força bruta, dicionário, password spraying e credential stuffing

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).

Uma campanha testa a mesma pequena lista de senhas comuns em milhares de contas, evitando muitas tentativas consecutivas em uma única conta. Essa técnica e a distinção para credential stuffing estão corretamente descritas em:

A) força bruta; credential stuffing cria senhas aleatórias sem usar vazamentos.
B) ataque de dicionário; credential stuffing falsifica o endereço IP de origem.
C) password spraying; credential stuffing reutiliza pares de credenciais obtidos em vazamentos.
D) phishing; credential stuffing explora exclusivamente falhas de memória.

### S2D4Q175 — Mitigação antes do ponto de saturação em DDoS

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [7.5 DoS e DDoS](semana_02_estudo.md#s2-d4-ataques-rede), nos trechos sobre saturação de banda, mitigação a montante e limite do firewall local depois do gargalo.

Uma botnet satura o enlace do órgão antes de o tráfego alcançar o firewall local. O portal continua saudável em testes internos, e o firewall apresenta baixa utilização. Qual resposta atua no ponto tecnicamente adequado?

A) Ampliar apenas as regras do firewall local e manter o mesmo enlace, pois o descarte posterior recupera a capacidade já consumida a montante.

B) Trocar o firewall por um IDS fora de banda e manter o mesmo enlace, pois a detecção local interrompe o volume antes de sua chegada.

C) Escalar apenas os servidores do portal e manter o mesmo enlace, pois capacidade de aplicação compensa a saturação ocorrida no acesso.

D) Coordenar filtragem ou limpeza a montante com o provedor e avaliar serviço anti-DDoS, CDN ou capacidade anterior ao gargalo.

### S2D4Q176 — Classificação de controles por natureza e por função

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles), [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips) e [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).

Um órgão adotou treinamento periódico contra phishing, um IDS para alertar sobre tráfego suspeito e cópias de segurança testadas para restaurar dados. Quanto à natureza e à função predominante desses controles, assinale a alternativa correta.

A) O treinamento é controle físico e corretivo; o IDS é administrativo e preventivo; o backup é técnico e dissuasório.
B) Os três controles são exclusivamente técnicos e preventivos, pois todos atuam antes do encerramento do incidente.
C) O treinamento é administrativo e predominantemente preventivo; o IDS é técnico e detectivo; o backup exerce função de recuperação.
D) O IDS é controle físico de recuperação, enquanto o treinamento e o backup são exclusivamente compensatórios.

### S2D4Q177 — Independência e complementaridade das camadas de defesa em profundidade

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles).

Uma arquitetura possui filtro de e-mail, MFA, segmentação, EDR e backup, mas todas essas camadas são administradas por uma única credencial compartilhada e sem proteção adicional. À luz da defesa em profundidade, é correto afirmar que:

A) a credencial comum constitui uma falha compartilhada capaz de enfraquecer várias camadas, apesar da diversidade aparente de controles.
B) a presença de cinco controles elimina o risco residual, ainda que todos dependam da mesma credencial.
C) defesa em profundidade exige que todas as camadas sejam do mesmo fabricante e tenham a mesma dependência administrativa.
D) o backup torna irrelevantes a segmentação e a proteção de identidade, pois permite desfazer qualquer incidente.

### S2D4Q178 — Filtragem stateful e limites do firewall

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [9. Firewall](semana_02_estudo.md#s2-d4-firewall).

Sobre firewalls, assinale a afirmativa correta.

A) Um firewall sem estado acompanha toda a sessão e decide com base no histórico completo da conexão.
B) Um firewall stateful acompanha o estado das conexões, mas ainda depende de política adequada e não corrige vulnerabilidades da aplicação.
C) Um firewall de borda observa necessariamente todo ataque interno, mesmo quando o tráfego não cruza o ponto em que ele está instalado.
D) Permitir uma porta conhecida garante que o conteúdo transportado por ela seja legítimo e que a aplicação esteja sem vulnerabilidades.

### S2D4Q179 — Ciclo de vida das regras de firewall

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [9. Firewall](semana_02_estudo.md#s2-d4-firewall), especialmente os trechos sobre mínimo necessário, documentação, revisão, registros e limites de visibilidade sobre tráfego cifrado.

Uma equipe revisa as regras do firewall de um serviço institucional. Considere as práticas a seguir.

A) I, apenas.

B) I e II, apenas.

C) II e III, apenas.

D) I, II e III.

### S2D4Q180 — IDS fora do caminho de encaminhamento

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips), nos trechos que contrastam detecção fora de banda com prevenção em linha.

A organização quer analisar uma cópia do tráfego, gerar alertas e evitar que o sensor participe do caminho obrigatório de encaminhamento. Qual combinação de controle e posicionamento atende diretamente ao requisito?

A) IDS fora de banda, recebendo cópias por porta espelhada ou TAP e emitindo alertas.

B) IDS em linha, encaminhando todo o tráfego e descartando cada correspondência detectada.

C) IPS fora de banda, recebendo cópias e bloqueando os pacotes no mesmo caminho de dados.

D) IPS em linha, inspecionando o tráfego e aplicando bloqueio preventivo às correspondências.

### S2D4Q181 — Falso positivo de IPS e disponibilidade

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips), especialmente a matriz de falsos positivos e falsos negativos e o impacto de bloqueios preventivos em linha.

Depois de uma atualização de assinatura, um IPS em linha classifica requisições legítimas como ataque e passa a bloqueá-las. Como se classificam a decisão do controle e seu possível efeito?

A) Verdadeiro positivo, pois a regra detectou tráfego malicioso e preservou a disponibilidade do serviço.

B) Verdadeiro negativo, pois o tráfego legítimo foi liberado e a regra permaneceu sem atuação preventiva.

C) Falso negativo, pois a regra deixou de detectar um ataque que continuou chegando normalmente à aplicação.

D) Falso positivo, pois tráfego legítimo foi bloqueado e a disponibilidade do serviço pode ser prejudicada.

### S2D4Q182 — Separação de portal, aplicação e banco por DMZ

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [11. DMZ](semana_02_estudo.md#s2-d4-dmz), especialmente o posicionamento do componente exposto e a filtragem mínima para segmentos internos mais restritos.

Um portal público encaminha solicitações a uma aplicação, que acessa um banco de dados sensível. Qual desenho reduz melhor a exposição e o movimento lateral entre essas camadas?

A) Colocar o portal na DMZ, separar aplicação e banco e liberar somente os fluxos exigidos entre as camadas.

B) Colocar portal, aplicação e banco na DMZ e permitir livre comunicação entre os três componentes.

C) Colocar portal e banco na DMZ, manter a aplicação interna e permitir acesso direto do portal aos dados.

D) Colocar o portal na DMZ, reunir aplicação e banco com usuários e liberar da DMZ qualquer fluxo interno.

### S2D4Q183 — VPN de acesso remoto e endpoint comprometido

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [12. VPN](semana_02_estudo.md#s2-d4-vpn), nos trechos sobre proteção do canal, confiança no endpoint, autenticação e política de acesso.

Um empregado estabelece uma VPN de acesso remoto a partir de um notebook já comprometido por malware. Qual avaliação delimita corretamente a proteção oferecida pelo túnel?

A) O túnel cifra o percurso e neutraliza o malware no notebook, dispensando EDR e verificação de postura.

B) O túnel autentica a conta e torna o notebook confiável, dispensando segmentação e limitação de privilégios.

C) O túnel protege o percurso, mas não saneia o notebook; postura, MFA, segmentação e menor privilégio continuam necessários.

D) O túnel impede credencial roubada e exploração do gateway, mesmo sem MFA, correções e monitoramento.

### S2D4Q184 — Modelos de VPN e política de acesso

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [12. VPN](semana_02_estudo.md#s2-d4-vpn), especialmente a distinção entre site-to-site e acesso remoto e os controles que permanecem necessários ao redor do túnel.

Uma organização precisa interligar continuamente as redes de duas unidades e também conectar analistas individuais que trabalham fora delas. Assinale a alternativa correta sobre os modelos de VPN e seus limites.

A) Site-to-site atende as redes e acesso remoto atende os analistas, mas ambos concedem automaticamente todas as rotas internas.

B) Acesso remoto atende as redes e site-to-site atende os analistas, desde que cada túnel tenha uma política de autorização.

C) Site-to-site atende as redes e acesso remoto atende os analistas, mas IPsec protege apenas Web e TLS atua apenas na camada IP.

D) Site-to-site atende as redes e acesso remoto atende os analistas, sem substituir autenticação, correção e política de acesso.

### S2D4Q185 — VLAN e controle do tráfego inter-VLAN

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [13. Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao), nos trechos que separam domínios de camada 2 e controle dos fluxos roteados por ACL ou firewall.

Usuários e servidores foram colocados em VLANs diferentes, mas o equipamento de camada 3 permite qualquer tráfego entre elas. Qual diagnóstico e medida são tecnicamente adequados?

A) A VLAN já bloqueia o movimento roteado, por isso a política permissiva não produz comunicação entre os segmentos.

B) A VLAN separa a camada 2, mas o caminho roteado permanece; ACL ou firewall deve limitar os fluxos necessários.

C) O roteamento inter-VLAN reúne novamente os broadcasts, por isso somente a remoção total do roteamento cria segmentação.

D) O identificador da VLAN aplica automaticamente a política de camada 3, por isso basta revisar os enlaces trunk.

### S2D4Q186 — Menor privilégio para conta de serviço

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [13. Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao) e [3. Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria), especialmente sujeito, ação, objeto, contexto e revisão de privilégios.

Uma aplicação precisa consultar duas visões e executar dois procedimentos no banco, sempre a partir de seus servidores. Qual configuração melhor aplica menor privilégio à conta de serviço?

A) Conta exclusiva, somente as operações e os objetos exigidos, origem restrita aos servidores e revisão periódica.

B) Conta de proprietário compartilhada, origem restrita aos servidores e auditoria anual das operações executadas.

C) Papel comum a usuários autenticados, acesso ao esquema inteiro e rotação periódica da senha compartilhada.

D) Conta administrativa por servidor, todas as operações liberadas e confiança baseada apenas na VLAN de origem.

### S2D4Q187 — Divisão de funções entre criptografia simétrica e assimétrica

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia), nos trechos sobre eficiência, quantidade de chaves, assinatura e estabelecimento de segredos.

Um sistema precisa proteger grande volume de dados e também verificar assinaturas de pacotes de atualização. Qual divisão de mecanismos é tecnicamente adequada?

A) Usar o par assimétrico para cifrar todo o volume e uma chave simétrica compartilhada para produzir assinatura pública.

B) Usar a chave simétrica para cifrar o volume e a mesma chave compartilhada para provar autoria perante qualquer terceiro.

C) Usar cifra simétrica no volume e mecanismo assimétrico para assinatura, verificação ou estabelecimento de chaves.

D) Usar a chave privada para cifrar o volume e a chave pública para recuperar os dados e ocultar a identidade do emissor.

### S2D4Q188 — Criptografia híbrida em uma sessão TLS

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia) e [17. TLS](semana_02_estudo.md#s2-d4-tls), especialmente a separação entre autenticação/estabelecimento e proteção simétrica do tráfego.

Em uma construção criptográfica híbrida como a usada conceitualmente no TLS, quais funções cabem aos mecanismos de estabelecimento e às chaves da sessão?

A) O mecanismo assimétrico cifra cada registro da aplicação, e a chave simétrica valida sozinha o certificado do servidor.

B) Mecanismo assimétrico ou PSK participa da autenticação e dos segredos, e chaves simétricas protegem os registros.

C) A função hash estabelece confidencialidade dos registros, e a chave assimétrica serve apenas para compactar o handshake.

D) O certificado cifra todo o fluxo com a chave pública, e a chave simétrica é usada somente antes da negociação.

### S2D4Q189 — Hash publicado junto de arquivo comprometido

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas), no trecho sobre referência confiável, autenticação do resumo e substituição conjunta de arquivo e hash.

Um invasor substitui um instalador e também o hash exibido na mesma página de download. Qual procedimento permite avaliar a integridade sem confiar novamente no recurso já comprometido?

A) Comparar o arquivo com o hash da página, pois resistência a colisões autentica a origem mesmo se ambos forem trocados.

B) Publicar um segundo algoritmo de hash na mesma página, pois dois resumos impedem substituição simultânea pelo invasor.

C) Baixar duas cópias do mesmo servidor e comparar seus hashes, pois igualdade entre elas comprova a versão do fornecedor.

D) Verificar manifesto assinado ou resumo obtido de fonte independente autenticada antes de aceitar o instalador.

### S2D4Q190 — HMAC entre sistemas com segredo compartilhado

**Nível:** Médio

**Uso:** Revisão

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas), especialmente a definição de HMAC, o uso de segredo compartilhado e o limite de não repúdio.

Dois sistemas compartilham um segredo e precisam detectar alterações e autenticar mensagens entre si, sem requisito de não repúdio perante terceiros. Qual mecanismo atende diretamente ao caso?

A) Calcular SHA-256 sem chave e enviar o resumo no mesmo canal usado para transportar a mensagem.

B) Cifrar a mensagem com AES-CTR sem etiqueta de autenticação e comparar apenas o texto recuperado.

C) Aplicar uma função de senha com salt público à mensagem e tratar o resultado como assinatura digital.

D) Calcular HMAC-SHA-256 com o segredo compartilhado e verificar o código junto da mensagem.

### S2D4Q191 — Armazenamento seguro de senhas com função de derivação, salt e custo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas).

Qual prática é mais adequada para armazenar senhas de usuários?

A) Aplicar função de derivação de chave própria para senhas, com salt único e custo configurável, mantendo parâmetros e migração documentados.
B) Cifrar reversivelmente todas as senhas com uma chave fixa compartilhada pela aplicação, mesmo quando só é necessário verificar o conhecimento.
C) Usar hash genérico rápido, sem salt, para reduzir o tempo disponível ao atacante.
D) Armazenar a senha em texto claro e proteger apenas o nome da coluna no banco.

### S2D4Q192 — Chaves e propriedades da assinatura digital

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [16. Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado), nos trechos sobre geração com chave privada, verificação com chave pública e ausência de confidencialidade automática.

Um órgão assina digitalmente um documento e o distribui em formato legível para verificação pública. No modelo simplificado de assinatura assimétrica, assinale a alternativa correta.

A) O signatário usa a chave pública e o verificador usa a privada; a operação comprova origem sem ocultar o conteúdo.

B) O signatário usa a chave privada e o verificador usa a pública; a operação também cifra o conteúdo para o verificador.

C) O signatário usa a chave privada e o verificador usa a pública; a operação apoia origem e integridade, não sigilo.

D) O signatário publica um hash sem chave e o verificador o recalcula; a igualdade identifica necessariamente o autor.

### S2D4Q193 — Validação do certificado de um servidor TLS

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [16. Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado), especialmente cadeia de confiança, assinaturas, validade, nome, uso da chave e revogação contextual.

Um cliente acessa `api.cra-pr.exemplo` e recebe um certificado X.509 do servidor. Qual procedimento reúne as verificações pertinentes antes de confiar na identidade apresentada?

A) Validar cadeia, assinaturas e datas, mas ignorar nome esperado, uso da chave e revogação se a cifra negociada for forte.

B) Validar nome, uso da chave e revogação, mas aceitar o certificado apresentado como sua própria âncora sem verificar a cadeia.

C) Validar cadeia e assinaturas até âncora confiável, datas, nome esperado, uso da chave e revogação conforme o contexto.

D) Validar porta 443, reputação comercial da emissora e tamanho da chave, sem conferir cadeia, nome ou período de validade.

### S2D4Q194 — Etapas conceituais do TLS 1.3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [17. TLS](semana_02_estudo.md#s2-d4-tls), nos trechos sobre negociação, derivação de segredos, autenticação do servidor, Finished e proteção autenticada com chaves de sessão.

Em uma conexão TLS 1.3 com autenticação do servidor por certificado, qual sequência representa adequadamente o handshake e a proteção posterior dos dados?

A) Validar a porta do serviço, usar a chave pública do certificado em todos os registros e dispensar chaves de sessão.

B) Negociar parâmetros, derivar segredos, validar o servidor e usar chaves simétricas autenticadas nos registros da aplicação.

C) Extrair o segredo apenas do certificado, ignorar o nome do servidor e usar Finished como substituto da cadeia de confiança.

D) Corrigir os endpoints durante o handshake, proteger os dados armazenados e dispensar controles de segurança na aplicação.

### S2D4Q195 — WPA3-Personal, SAE e modo de transição

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [18. Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi), especialmente SAE, limites diante de senha fraca e ataque online e comportamento do modo de transição.

Considere as afirmações sobre WPA2-Personal e WPA3-Personal.

A) I, II e III.

B) I e II, apenas.

C) I e III, apenas.

D) II e III, apenas.

### S2D4Q196 — Identidade individual em Wi-Fi institucional

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [18. Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi), nos trechos sobre modo Enterprise, 802.1X, identidade individual, validação do servidor e limites de segredos coletivos.

Uma rede Wi-Fi institucional precisa autenticar usuários individualmente, revogar um acesso sem trocar o segredo de todos e registrar cada autenticação. Qual desenho atende melhor a esses requisitos?

A) WPA3-Personal com segredo coletivo, rotação trimestral e associação dos registros ao endereço MAC de cada cliente.

B) WPA2-Personal com segredo por setor, portal individual e revogação feita pela troca da senha de todo o setor.

C) WPA3-Personal em transição, segredo coletivo e presunção de que todo cliente negociou SAE ao associar.

D) WPA2/WPA3-Enterprise com 802.1X, identidades individuais, validação do servidor e registros de autenticação.

### S2D4Q197 — Ordem e objetivos da resposta a incidentes

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [19. Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes), especialmente análise, contenção, preservação de evidências, erradicação e recuperação validada.

Após alertas de ransomware em várias estações, a equipe precisa avançar do indício até o retorno controlado do serviço. Qual sequência preserva os objetivos distintos da resposta a incidentes?

A) Validar e delimitar, restaurar imediatamente, apagar os registros, conter somente se o comprometimento reaparecer.

B) Validar e delimitar, conter preservando evidências, erradicar causas e recuperar para estado conhecido e monitorado.

C) Tratar todo alerta como confirmado, desligar indiscriminadamente, restaurar e encerrar quando o serviço responder.

D) Analisar o indício, erradicar antes de conter, recuperar e coletar evidências somente depois das alterações.

### S2D4Q198 — Cadeias de restauração, RPO e RTO

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), nos trechos sobre restauração incremental e diferencial e sobre os significados temporais de RPO e RTO.

Considere as afirmações sobre backup e objetivos de recuperação.

A) Apenas as afirmações I e II.

B) Apenas as afirmações I e III.

C) Apenas as afirmações II e III.

D) As afirmações I, II e III.

### S2D4Q199 — Backups resistentes a ransomware

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), especialmente isolamento, credenciais separadas, imutabilidade ou versões e validação periódica de restauração.

Considere as medidas para reduzir a chance de um ransomware comprometer simultaneamente produção e recuperação.

A) I, II e III.

B) I e II, apenas.

C) I e III, apenas.

D) II e III, apenas.

### S2D4Q200 — Alta disponibilidade e recuperação histórica

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), nos trechos que distinguem redundância ou alta disponibilidade de backup versionado para recuperação de estado anterior.

Um portal deve continuar operando após a falha de um servidor e recuperar uma versão anterior depois de exclusão ou cifração maliciosa. Qual arquitetura atende aos dois objetivos?

A) Dois nós ativos com replicação síncrona do estado atual, sem cópia histórica separada ou protegida.

B) Espelhamento RAID no servidor e replicação síncrona do estado atual, sem retenção de versões em backup.

C) Backups completos e incrementais frequentes, sem servidor alternativo capaz de assumir a carga durante uma falha.

D) Serviço redundante com failover e backups versionados, protegidos e testados para restaurar estados anteriores.

## Gabarito do Dia 4

### Questões principais 1–25


| Questão | Resposta |
|---:|:---:|
| 1 | C |
| 2 | A |
| 3 | A |
| 4 | D |
| 5 | B |
| 6 | D |
| 7 | C |
| 8 | C |
| 9 | B |
| 10 | A |
| 11 | A |
| 12 | D |
| 13 | D |
| 14 | B |
| 15 | A |
| 16 | C |
| 17 | C |
| 18 | B |
| 19 | B |
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
| 28 | B |
| 29 | B |
| 30 | A |
| 31 | D |
| 32 | A |
| 33 | C |
| 34 | D |
| 35 | B |
| 36 | A |
| 37 | C |
| 38 | B |
| 39 | D |
| 40 | D |
| 41 | A |
| 42 | C |
| 43 | C |
| 44 | B |
| 45 | A |
| 46 | D |
| 47 | B |
| 48 | D |
| 49 | A |
| 50 | D |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 4.1 | B |
| 4.2 | D |
| 4.3 | A |
| 4.4 | C |
| 4.5 | C |
| 4.6 | D |
| 4.7 | A |
| 4.8 | C |
| 4.9 | B |
| 4.10 | A |
| 4.11 | C |
| 4.12 | C |
| 4.13 | B |
| 4.14 | D |
| 4.15 | A |
| 4.16 | C |
| 4.17 | B |
| 4.18 | D |
| 4.19 | A |
| 4.20 | D |


## Comentários do Dia 4


### Comentário S2D4Q151

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** um controle reduz risco dentro de determinado contexto, mas não converte segurança em estado definitivo nem dispensa monitoramento.
- **B)** ativos com funções, exposições e impactos diferentes exigem análise contextual; conformidade e varredura não substituem todo o processo.
- **C)** a gestão permanece cíclica, combinando identificação, análise, tratamento, verificação da eficácia e decisão consciente sobre o risco que restou.
- **D)** pessoas, processos, fornecedores e mudanças operacionais também podem alterar probabilidade e impacto, não apenas falhas técnicas.

**Conceito:** segurança da informação como processo contínuo de gestão e monitoramento de riscos.

**Pegadinha:** tratar a aquisição de um controle relevante como prova de risco zero ou como encerramento permanente da avaliação.

**Como pensar:** procure a alternativa que percorre contexto, análise, tratamento, monitoramento e decisão sobre risco residual sem prometer segurança absoluta.

**Referência:** [1. Segurança como gestão de risco](semana_02_estudo.md#s2-d4-gestao-risco), especialmente as seis etapas do processo e o tratamento do risco residual.

### Comentário S2D4Q152

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O risco remanescente precisa ser reavaliado para decidir entre aceitação, tratamento adicional, transferência ou outra resposta cabível.
- **B)** Incorreta. Controles modificam o risco, mas a gestão não deve prometer risco zero como condição universal de operação.
- **C)** Incorreta. Transferência é uma opção de tratamento, não destino obrigatório; um risco compatível com os critérios organizacionais pode ser aceito.
- **D)** Incorreta. O risco anterior aos controles é o risco inerente ou inicial no modelo considerado; residual é o que permanece depois do tratamento.

**Conceito:** risco residual e decisão de tratamento após a aplicação de controles.

**Pegadinha:** confundir risco residual com risco inicial ou afirmar que seu valor deve ser sempre zero, positivo e mensurável, ou transferido.

**Como pensar:** localize primeiro o momento da avaliação: se os controles já foram aplicados, o que resta é residual e ainda exige decisão contextual.

**Referência:** [Segurança como gestão de risco](semana_02_estudo.md#s2-d4-gestao-risco).

### Comentário S2D4Q153

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D4Q154

**Nível:** Difícil

**Uso:** Essenciais
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A afirmativa I é verdadeira, mas a II também é: cifração não autorizada altera o estado dos arquivos e pode impedir seu uso.
- **B)** Incorreta. A III é falsa. Backup apoia recuperação, porém não impede exfiltração nem garante que não haverá interrupção inicial.
- **C)** Incorreta. Inclui a afirmativa III, que exagera o alcance do backup.
- **D)** Correta. Exfiltração afeta confidencialidade; alteração ou cifração indevida pode afetar integridade e disponibilidade.

**Conceito:** um único incidente pode comprometer simultaneamente os três objetivos da tríade CIA.

**Pegadinha:** limitar ransomware à disponibilidade ou tratar backup como controle capaz de impedir vazamento e interrupção.

**Como pensar:** decomponha o cenário por efeito: saída de dados, mudança indevida e indisponibilidade devem ser classificados separadamente.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia) e [Malware](semana_02_estudo.md#s2-d4-malware).

### Comentário S2D4Q155

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D4Q156

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D4Q157

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** uma ACL pode participar do controle, mas a decisão do enunciado não se limita a uma associação fixa entre identidade e objeto.
- **B)** RBAC concentra a autorização em papéis ou funções; a presença de departamento não apaga as condições de recurso, ação, dispositivo e horário.
- **C)** ABAC avalia atributos do sujeito, do objeto, da ação e do ambiente, exatamente as dimensões usadas pela política descrita.
- **D)** accounting registra sessões, consumo e ações; ele não substitui o mecanismo que decide se a operação deve ser autorizada.

**Conceito:** autorização baseada em atributos em contraste com papel, lista de acesso e registro de atividade.

**Pegadinha:** reconhecer um atributo ligado ao cargo e concluir RBAC, ignorando que recurso, ação e contexto também integram a decisão.

**Como pensar:** identifique quais elementos alimentam a política; múltiplos atributos do sujeito, objeto, ação e ambiente apontam para ABAC.

**Referência:** [3.2 Autorização](semana_02_estudo.md#s2-d4-identidade-auditoria), nos trechos que distinguem RBAC, ABAC, listas de controle de acesso e accounting.

### Comentário S2D4Q158

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** authentication confirma a identidade por evidências apropriadas; a existência de um registro de sessão não refaz essa comprovação.
- **B)** authorization aplica permissões e políticas; o consumo já registrado não define, sozinho, o que a identidade pode acessar.
- **C)** accounting documenta consumo, sessões e ações para controle e responsabilização, gerando material que pode ser examinado pela auditoria.
- **D)** auditoria é atividade mais ampla de análise de registros, controles e conformidade; produzir logs não completa automaticamente esse exame.

**Conceito:** accounting como terceiro componente do AAA e como fonte de evidências para auditoria.

**Pegadinha:** traduzir o terceiro A como se accounting fosse sinônimo perfeito de autenticação, autorização ou de todo o processo de auditoria.

**Como pensar:** associe os três verbos do AAA: autenticar identifica, autorizar permite e accounting registra; a auditoria analisa esse material.

**Referência:** [3.3 Auditoria e accounting](semana_02_estudo.md#s2-d4-identidade-auditoria) e [3.5 Modelo AAA](semana_02_estudo.md#s2-d4-identidade-auditoria), especialmente a diferença entre produzir registros e examiná-los.

### Comentário S2D4Q159

**Nível:** Difícil

**Uso:** Essenciais
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

### Comentário S2D4Q160

**Nível:** Difícil

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** o plano reúne contexto suficiente, tempo correlacionável, controle de alteração, retenção e capacidade de análise, cobrindo as lacunas do cenário.
- **B)** sincronização e centralização favorecem correlação, porém falhas e negações também importam, e os registros precisam de proteção contra alteração.
- **C)** ação, resultado e integridade são úteis, mas IP não substitui identidade confiável e descarte imediato inviabiliza retenção e investigação posterior.
- **D)** identidade e recurso ajudam, mas relógios divergentes impedem ordenar fontes, e edição livre pelos examinados compromete a confiabilidade.

**Conceito:** requisitos complementares para logs sustentarem accounting, auditoria e investigação.

**Pegadinha:** aceitar uma solução parcialmente correta que sincroniza, contextualiza ou protege os registros, mas deixa outra dimensão essencial sem tratamento.

**Como pensar:** aplique três filtros sucessivos: o evento explica a ação, pode ser correlacionado no tempo e permanece íntegro e disponível para análise.

**Referência:** [3.3 Auditoria e accounting](semana_02_estudo.md#s2-d4-identidade-auditoria), especialmente os campos de contexto e os requisitos de sincronização, retenção, acesso, integridade e análise.

### Comentário S2D4Q161

**Nível:** Muito difícil

**Uso:** Aprofundamento
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

### Comentário S2D4Q162

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A presença de uma falha explorável não demonstra que houve exploração ou comprometimento.
- **B)** Incorreta. O serviço é o ativo; a chance e o impacto são componentes usados na avaliação do risco.
- **C)** Incorreta. Vulnerabilidade é a fraqueza; risco é a possibilidade avaliada de dano, e os conceitos não são sinônimos.
- **D)** Correta. A versão falha constitui vulnerabilidade, e o risco depende da combinação contextual de probabilidade e impacto adverso.

**Conceito:** vulnerabilidade como fraqueza e risco como combinação de probabilidade e impacto.

**Pegadinha:** transformar automaticamente toda vulnerabilidade em incidente ou usar vulnerabilidade e risco como termos intercambiáveis.

**Como pensar:** primeiro identifique a fraqueza; depois avalie a possibilidade e a consequência de ela ser explorada.

**Referência:** [Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco).

### Comentário S2D4Q163

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D4Q164

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** o agente capaz de causar dano é a ameaça, enquanto a fraqueza explorável é a vulnerabilidade; correção e MFA não são ameaça.
- **B)** o criminoso representa a fonte potencial de dano, a falha oferece a condição explorável e os controles reduzem probabilidade, impacto ou ambos.
- **C)** incidente exige ocorrência concreta que comprometa ou ameace a segurança, e a medida aplicada não se transforma no ativo protegido.
- **D)** risco combina probabilidade e impacto, incidente é ocorrência concreta e evento não corresponde ao conjunto de medidas de proteção.

**Conceito:** classificação operacional de ameaça, vulnerabilidade e controle dentro de um cenário de risco.

**Pegadinha:** trocar os papéis dos elementos porque todos aparecem na mesma cadeia causal de um possível incidente.

**Como pensar:** pergunte quem pode causar dano, qual fraqueza pode ser explorada e qual medida procura alterar a probabilidade ou o impacto.

**Referência:** [4. Ativo, ameaça, vulnerabilidade, risco, evento e incidente](semana_02_estudo.md#s2-d4-conceitos-risco), na tabela de conceitos e no exemplo do gateway VPN.

### Comentário S2D4Q165

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** X depende do executável hospedeiro, característica do vírus, enquanto Y se autopropaga entre sistemas, comportamento típico de worm.
- **B)** a alternativa inverte os mecanismos; dependência de hospedeiro não define worm, e propagação automática não define vírus.
- **C)** a disseminação de X continua vinculada ao arquivo e à sua execução; esse detalhe impede classificar as duas amostras do mesmo modo.
- **D)** malware é a categoria ampla, e vírus é uma categoria específica; o modo de propagação permanece discriminador.

**Conceito:** distinção entre vírus e worm pelo mecanismo de vinculação e propagação.

**Pegadinha:** classificar pelo dano ou pelo simples fato de a amostra gerar cópias, ignorando como essas cópias alcançam outros sistemas.

**Como pensar:** procure primeiro o hospedeiro; se a propagação depende dele, pense em vírus, e se ocorre automaticamente entre sistemas, pense em worm.

**Referência:** [5.1 Vírus e 5.2 Worm](semana_02_estudo.md#s2-d4-malware), nos trechos que distinguem vínculo a hospedeiro e propagação automática por redes ou sistemas.

### Comentário S2D4Q166

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** acesso remoto é uma possível carga maliciosa, mas worm exige a característica de propagação automática ausente no cenário.
- **B)** o rótulo de atualização é o disfarce; nada informa que o código se vinculou a outro arquivo ou programa hospedeiro.
- **C)** apresentação enganosa e execução induzida são os traços centrais do cavalo de Troia, sem necessidade de autorreplicação.
- **D)** spyware se caracteriza pela coleta de informações; acesso remoto oculto pode ter outras finalidades e não prova coleta exclusiva.

**Conceito:** cavalo de Troia definido pelo disfarce e pela indução da vítima à execução.

**Pegadinha:** classificar a amostra apenas pela carga instalada, sem observar o mecanismo usado para chegar e executar no sistema.

**Como pensar:** separe entrega, propagação e carga; neste caso, disfarce e execução voluntária induzida decidem a categoria principal.

**Referência:** [5.3 Cavalo de Troia](semana_02_estudo.md#s2-d4-malware), em contraste com os mecanismos de vírus, worm e spyware descritos na mesma seção.

### Comentário S2D4Q167

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Spyware foca coleta de informações, e ransomware moderno não se limita à disponibilidade.
- **B)** Incorreta. Backup pode apoiar a recuperação, mas não contém o invasor, não remove persistência e não desfaz a exfiltração.
- **C)** Correta. Campanhas de ransomware podem combinar roubo, alteração, cifração e interrupção, comprometendo toda a tríade CIA.
- **D)** Incorreta. A existência de outra cópia não torna autorizada a alteração dos arquivos em produção nem preserva sua integridade naquele ambiente.

**Conceito:** alcance do ransomware e sobreposição de categorias e efeitos de malware.

**Pegadinha:** reduzir ransomware à cifração local ou acreditar que backup resolve confidencialidade e erradicação.

**Como pensar:** avalie separadamente o que saiu do ambiente, o que foi alterado e o que ficou indisponível.

**Referência:** [Malware](semana_02_estudo.md#s2-d4-malware) e [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

### Comentário S2D4Q168

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D4Q169

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** troca os canais das campanhas I e II; SMS caracteriza smishing e voz caracteriza vishing.
- **B)** I e II são classificados pelo canal, enquanto III e IV são distinguidos pela especificidade e pela relevância hierárquica do alvo.
- **C)** acerta os canais de I e II, mas troca os alvos de III e IV; analista específico indica spear phishing, e presidência indica whaling.
- **D)** atribui categorias de alvo às campanhas definidas pelo canal e categorias de canal às campanhas definidas pelo perfil da vítima.

**Conceito:** variações de phishing classificadas pelas dimensões canal e alvo.

**Pegadinha:** resolver apenas metade da associação ou misturar categorias que descrevem o meio de contato com categorias que descrevem a vítima.

**Como pensar:** primeiro marque SMS e voz; depois separe alvo específico de pessoa de alta relevância e confira as quatro posições.

**Referência:** [6. Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing), na lista que distingue alvo específico, pessoa de alta relevância, SMS ou mensagem e voz.

### Comentário S2D4Q170

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D4Q171

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D4Q172

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** sniffing captura e analisa tráfego; ele não concede, por definição, a capacidade de falsificar o campo de origem ou controlar o retorno.
- **B)** a divergência é compatível com IP spoofing, e os pacotes de resposta seguem o endereço declarado, salvo outra condição que dê ao emissor acesso ao caminho.
- **C)** falsificação não prova posicionamento intermediário; um atacante on-path pode observar o retorno, mas essa condição não decorre apenas do IP forjado.
- **D)** DDoS requer ataque distribuído à disponibilidade; origem falsificada, sozinha, não prova botnet nem controle bidirecional.

**Conceito:** spoofing como falsificação de origem e limite operacional do caminho de resposta no IP spoofing.

**Pegadinha:** inferir que falsificar a origem automaticamente coloca o emissor no caminho ou lhe assegura receber as respostas.

**Como pensar:** separe dois testes: há identidade aparente falsificada e existe condição independente para observar o caminho de retorno?.

**Referência:** [7.1 Spoofing](semana_02_estudo.md#s2-d4-ataques-rede), especialmente a definição de falsificação de origem e a ressalva sobre o retorno em IP spoofing.

### Comentário S2D4Q173

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** copiar tráfego caracteriza sniffing, enquanto redirecioná-lo pelo equipamento do invasor cria posição on-path; rejeitar o certificado bloqueia a confiança no endpoint falso.
- **B)** as classificações foram invertidas, e a rejeição mostra que a validação atuou, não que o adversário deixou de estar no caminho.
- **C)** o posicionamento on-path existe pela capacidade de intermediar a comunicação, ainda que uma tentativa concreta de alteração seja detectada e rejeitada.
- **D)** espelhamento permite observação sem encaminhamento pelo analisador, e autenticação correta do canal continua relevante contra substituição.

**Conceito:** diferença entre captura de tráfego, posicionamento on-path e efeito da validação criptográfica.

**Pegadinha:** definir o ataque somente pelo resultado final e confundir tentativa bloqueada com ausência de posição ou de capacidade de interceptação.

**Como pensar:** identifique primeiro quem apenas recebe uma cópia e quem participa do caminho; depois avalie se a credencial apresentada foi validada.

**Referência:** [7.2 Sniffing e 7.3 Man-in-the-middle ou ataque on-path](semana_02_estudo.md#s2-d4-ataques-rede), incluindo a ressalva sobre criptografia com validação correta.

### Comentário S2D4Q174

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D4Q175

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o firewall recebe o tráfego somente depois do enlace saturado; descartar nesse ponto não devolve a capacidade consumida antes dele.
- **B)** IDS fora de banda pode detectar e alertar, mas não bloqueia o fluxo a montante nem cria banda no enlace já esgotado.
- **C)** servidores adicionais tratam capacidade da aplicação, enquanto o sintoma e os indicadores localizam o gargalo no enlace de acesso.
- **D)** filtragem, limpeza ou capacidade antes do gargalo impede que todo o volume atravesse o enlace; provedor, anti-DDoS e CDN podem participar dessa arquitetura.

**Conceito:** seleção do ponto de mitigação de DDoS conforme a localização da saturação.

**Pegadinha:** escolher um controle válido em outro cenário, mas instalado depois do recurso que já foi esgotado.

**Como pensar:** localize primeiro o gargalo e só depois escolha o controle; a mitigação eficaz precisa atuar antes ou no próprio ponto de saturação.

**Referência:** [7.5 DoS e DDoS](semana_02_estudo.md#s2-d4-ataques-rede), nos trechos sobre saturação de banda, mitigação a montante e limite do firewall local depois do gargalo.

### Comentário S2D4Q176

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D4Q177

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D4Q178

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A filtragem sem estado avalia pacotes individualmente; acompanhar o estado da conexão é característica do firewall stateful.
- **B)** Correta. Stateful descreve o acompanhamento da conexão, sem transformar o controle em garantia contra toda vulnerabilidade ou política ruim.
- **C)** Incorreta. Uma ameaça interna pode não atravessar o ponto observado pelo firewall de borda.
- **D)** Incorreta. Porta permitida pode transportar conteúdo malicioso, e o firewall não corrige falhas da aplicação.

**Conceito:** filtragem stateful e limites do firewall.

**Pegadinha:** converter uma capacidade verdadeira — acompanhar estado — em promessa de segurança completa para a aplicação.

**Como pensar:** separe a decisão sobre o fluxo da segurança do conteúdo e do software que recebe esse fluxo.

**Referência:** [9. Firewall](semana_02_estudo.md#s2-d4-firewall).

### Comentário S2D4Q179

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** a afirmação I é correta, mas o acompanhamento previsto na afirmação II também integra o ciclo de vida seguro da regra.
- **B)** mínimo necessário, justificativa, responsável, revisão e registros reduzem permissões excessivas e regras esquecidas.
- **C)** a afirmação II é correta, porém cifra não elimina risco, não torna a regra permanente e não dispensa controle de saída.
- **D)** a afirmação III contraria a necessidade de revisar regras e de controlar comunicações iniciadas para fora.

**Conceito:** elaboração e manutenção de política de firewall ao longo do ciclo de vida das regras.

**Pegadinha:** tratar tráfego cifrado como automaticamente legítimo ou confundir uma liberação inicial com autorização permanente.

**Como pensar:** verifique necessidade, escopo, responsável, evidência de uso e prazo de revisão; nenhuma porta ou cifra substitui essas decisões.

**Referência:** [9. Firewall](semana_02_estudo.md#s2-d4-firewall), especialmente os trechos sobre mínimo necessário, documentação, revisão, registros e limites de visibilidade sobre tráfego cifrado.

### Comentário S2D4Q180

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** o IDS pode receber cópia por SPAN ou TAP, analisar fora do caminho de produção e gerar alertas sem encaminhar os pacotes.
- **B)** encaminhamento obrigatório com descarte corresponde à atuação preventiva em linha, não ao IDS fora de banda solicitado.
- **C)** um sensor que recebe apenas cópia não ocupa o mesmo caminho dos pacotes e não os descarta diretamente nesse caminho.
- **D)** o IPS em linha pode bloquear tráfego, mas participa justamente do caminho que o enunciado manda evitar.

**Conceito:** função e posicionamento de IDS fora de banda em contraste com IPS em linha.

**Pegadinha:** separar incorretamente o nome do controle de sua posição e de sua capacidade de intervir no fluxo.

**Como pensar:** procure a combinação completa “cópia do tráfego + alerta + fora do caminho”; ela descreve IDS fora de banda.

**Referência:** [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips), nos trechos que contrastam detecção fora de banda com prevenção em linha.

### Comentário S2D4Q181

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o tráfego era legítimo, portanto a classificação como ataque não constitui verdadeiro positivo.
- **B)** um verdadeiro negativo exigiria tráfego legítimo corretamente liberado, mas o IPS o bloqueou.
- **C)** falso negativo ocorre quando um ataque real não é detectado ou impedido, situação oposta à descrita.
- **D)** o controle marcou como malicioso um evento legítimo e, por estar em linha, pode tornar o serviço indisponível para usuários válidos.

**Conceito:** falso positivo, falso negativo e impacto operacional de um IPS em linha.

**Pegadinha:** classificar o resultado pela ação de bloquear, sem comparar a decisão do sensor com a natureza real do tráfego.

**Como pensar:** monte duas colunas — realidade e decisão — e depois avalie o efeito do bloqueio sobre a disponibilidade.

**Referência:** [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips), especialmente a matriz de falsos positivos e falsos negativos e o impacto de bloqueios preventivos em linha.

### Comentário S2D4Q182

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** somente o componente necessário fica exposto na DMZ, e novas barreiras limitam portal, aplicação e banco aos fluxos indispensáveis.
- **B)** reunir banco e serviço exposto amplia o alcance de um comprometimento e elimina barreiras entre as camadas.
- **C)** publicar o banco e permitir acesso direto do portal contorna a camada de aplicação e expõe o ativo mais sensível.
- **D)** acesso irrestrito da DMZ à rede interna transforma o componente exposto em caminho amplo para movimento lateral.

**Conceito:** DMZ como segmento intermediário e filtragem entre camadas de uma aplicação publicada.

**Pegadinha:** considerar a DMZ uma rede confiável ou colocar nela todos os componentes apenas porque pertencem ao mesmo serviço.

**Como pensar:** aproxime da Internet apenas o componente indispensável e crie uma decisão de acesso mínima em cada travessia seguinte.

**Referência:** [11. DMZ](semana_02_estudo.md#s2-d4-dmz), especialmente o posicionamento do componente exposto e a filtragem mínima para segmentos internos mais restritos.

### Comentário S2D4Q183

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** a VPN protege dados no percurso, mas não remove processos maliciosos nem substitui controles no dispositivo.
- **B)** autenticar uma identidade não comprova a integridade do equipamento nem autoriza acesso irrestrito aos segmentos internos.
- **C)** o canal pode estar protegido enquanto o endpoint permanece hostil, por isso postura, MFA, segmentação e menor privilégio continuam necessários.
- **D)** credenciais ainda podem ser roubadas e gateways vulneráveis continuam exploráveis sem correções e monitoramento.

**Conceito:** alcance da VPN de acesso remoto e separação entre segurança do canal, endpoint, identidade e autorização.

**Pegadinha:** transferir a confiança criptográfica do túnel para o dispositivo ou para todas as ações do usuário.

**Como pensar:** avalie separadamente percurso, endpoint, identidade e privilégio; a VPN resolve principalmente o primeiro componente.

**Referência:** [12. VPN](semana_02_estudo.md#s2-d4-vpn), nos trechos sobre proteção do canal, confiança no endpoint, autenticação e política de acesso.

### Comentário S2D4Q184

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** a associação dos modelos está correta, mas um túnel autenticado não concede automaticamente acesso a todas as redes e ações.
- **B)** os modelos foram invertidos; site-to-site liga redes, enquanto acesso remoto atende usuários ou dispositivos.
- **C)** a associação dos modelos está correta, porém a alternativa troca o escopo usual de IPsec e de soluções baseadas em TLS.
- **D)** cada necessidade recebe o modelo apropriado, e o túnel continua dependente de autenticação, correções e autorização mínima.

**Conceito:** VPN site-to-site, VPN de acesso remoto e limites de autorização do túnel.

**Pegadinha:** acertar os extremos do túnel, mas atribuir acesso irrestrito ou inverter as tecnologias de proteção.

**Como pensar:** primeiro identifique “rede com rede” ou “dispositivo com organização”; depois verifique identidade, integridade e escopo autorizado.

**Referência:** [12. VPN](semana_02_estudo.md#s2-d4-vpn), especialmente a distinção entre site-to-site e acesso remoto e os controles que permanecem necessários ao redor do túnel.

### Comentário S2D4Q185

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** VLAN separa o domínio de camada 2, mas não bloqueia o tráfego que a função de roteamento autoriza entre sub-redes.
- **B)** a separação de broadcast permanece, porém o movimento lateral roteado precisa de política explícita em ACL ou firewall.
- **C)** roteamento não funde os domínios de broadcast, e a segmentação pode permitir somente os fluxos necessários sem remover toda comunicação.
- **D)** o identificador de VLAN não expressa sozinho a política de camada 3, e trunk trata transporte de VLANs, não autorização inter-VLAN.

**Conceito:** diferença entre separação de camada 2 por VLAN e filtragem do tráfego roteado.

**Pegadinha:** transformar isolamento de broadcast em bloqueio automático de toda comunicação entre os segmentos.

**Como pensar:** siga o pacote depois da VLAN; se existe roteamento, procure o controle que decide quais fluxos podem atravessá-lo.

**Referência:** [13. Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao), nos trechos que separam domínios de camada 2 e controle dos fluxos roteados por ACL ou firewall.

### Comentário S2D4Q186

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** a configuração limita identidade, ações, objetos e origem ao necessário e ainda prevê revisão ao longo do tempo.
- **B)** restringir a origem não compensa o privilégio de proprietário nem a falta de responsabilização causada por conta compartilhada.
- **C)** autenticação e rotação de senha não justificam conceder o esquema inteiro nem compartilhar a mesma autorização com usuários.
- **D)** identidade por servidor melhora rastreabilidade, mas privilégio administrativo amplo e confiança exclusiva na VLAN violam o mínimo necessário.

**Conceito:** menor privilégio aplicado à conta de serviço e ao fluxo entre aplicação e banco.

**Pegadinha:** aceitar um controle verdadeiro — origem, rotação ou conta separada — como compensação para permissões excessivas.

**Como pensar:** confira quatro limites em conjunto: quem acessa, qual ação executa, sobre qual objeto e a partir de qual contexto.

**Referência:** [13. Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao) e [3. Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria), especialmente sujeito, ação, objeto, contexto e revisão de privilégios.

### Comentário S2D4Q187

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** mecanismos assimétricos são mais custosos para grande volume, e segredo compartilhado não produz assinatura verificável publicamente.
- **B)** cifra simétrica é adequada ao volume, mas uma chave conhecida por várias partes não identifica exclusivamente qual delas produziu o resultado.
- **C)** cifras simétricas são eficientes para dados volumosos, enquanto pares assimétricos atendem assinatura, verificação e estabelecimento de chaves.
- **D)** operação com chave privada não é regra genérica de confidencialidade, e verificação pública não oculta a identidade do emissor.

**Conceito:** chaves, eficiência e aplicações dos mecanismos simétricos e assimétricos.

**Pegadinha:** associar mecanicamente chave privada a confidencialidade ou segredo compartilhado a assinatura pública.

**Como pensar:** separe desempenho do volume de dados das funções de identidade e estabelecimento; cada família resolve uma parte diferente.

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia), nos trechos sobre eficiência, quantidade de chaves, assinatura e estabelecimento de segredos.

### Comentário S2D4Q188

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** TLS não aplica a chave assimétrica a cada registro, e uma chave simétrica não valida por si o vínculo de identidade do certificado.
- **B)** mecanismos assimétricos ou PSK ajudam a autenticar e estabelecer segredos, dos quais derivam chaves simétricas eficientes para os registros.
- **C)** hash isolado não fornece confidencialidade, e mecanismo assimétrico não é técnica de compactação do handshake.
- **D)** certificado não cifra diretamente todo o fluxo, e as chaves simétricas são usadas depois da negociação para proteger a sessão.

**Conceito:** divisão de funções na criptografia híbrida e no TLS.

**Pegadinha:** imaginar que a chave do certificado cifra cada byte ou que hash isolado substitui a cifra da sessão.

**Como pensar:** separe a fase de obter confiança e segredos da fase de proteger eficientemente o volume de dados.

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia) e [17. TLS](semana_02_estudo.md#s2-d4-tls), especialmente a separação entre autenticação/estabelecimento e proteção simétrica do tráfego.

### Comentário S2D4Q189

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** a comparação só prova igualdade com a referência apresentada; se ambos foram trocados, o valor adulterado também coincidirá.
- **B)** quem controla a página pode recalcular e substituir resumos de vários algoritmos junto com o arquivo.
- **C)** duas cópias fornecidas pela mesma origem comprometida podem ser idênticas e igualmente maliciosas.
- **D)** assinatura ou canal independente autenticado protege a referência contra a mesma capacidade que alterou o arquivo.

**Conceito:** hash para integridade e necessidade de uma referência autêntica e independente.

**Pegadinha:** confundir resistência criptográfica do algoritmo com confiança na origem que publicou o resumo.

**Como pensar:** antes de comparar valores, pergunte se o atacante capaz de trocar o arquivo também consegue trocar a referência.

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas), no trecho sobre referência confiável, autenticação do resumo e substituição conjunta de arquivo e hash.

### Comentário S2D4Q190

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** qualquer parte pode recalcular um hash sem chave após alterar a mensagem, portanto ele não autentica a origem por si só.
- **B)** modo de cifra sem autenticação pode preservar confidencialidade, mas não fornece a verificação de integridade solicitada.
- **C)** salt público e função de senha não criam assinatura nem autenticam a mensagem perante quem conhece um segredo comum.
- **D)** HMAC combina a mensagem com o segredo compartilhado para oferecer integridade e autenticação entre quem conhece a chave.

**Conceito:** HMAC como código de autenticação de mensagem baseado em segredo compartilhado.

**Pegadinha:** atribuir autenticação a hash simples, cifra sem etiqueta ou função de armazenamento de senhas.

**Como pensar:** quando há segredo comum e se deseja autenticar a mensagem, procure MAC ou HMAC; não repúdio exige outra estrutura.

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas), especialmente a definição de HMAC, o uso de segredo compartilhado e o limite de não repúdio.

### Comentário S2D4Q191

**Nível:** Difícil

**Uso:** Simulado
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

### Comentário S2D4Q192

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** a alternativa inverte as chaves; no modelo apresentado, a chave privada assina e a pública verifica.
- **B)** as chaves estão corretamente associadas, mas assinatura não cifra automaticamente o documento nem restringe sua leitura ao verificador.
- **C)** a assinatura vincula a chave privada aos dados, e a chave pública permite verificar origem e integridade sem esconder o conteúdo.
- **D)** qualquer pessoa pode calcular hash sem segredo; a igualdade apoia integridade perante uma referência confiável, não identifica o autor.

**Conceito:** geração, verificação e propriedades da assinatura digital assimétrica.

**Pegadinha:** inverter as chaves ou acrescentar confidencialidade a uma operação destinada a origem e integridade.

**Como pensar:** separe assinatura de cifração: a primeira usa a chave privada do signatário e pode ser verificada publicamente.

**Referência:** [16. Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado), nos trechos sobre geração com chave privada, verificação com chave pública e ausência de confidencialidade automática.

### Comentário S2D4Q193

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** cifra forte não compensa certificado emitido para outro nome, uso incompatível ou credencial que deixou de ser aceitável.
- **B)** conferir campos da folha não basta se o cliente transforma arbitrariamente o próprio certificado recebido em âncora confiável.
- **C)** a validação combina caminho confiável, assinaturas, período, identidade esperada, finalidade da chave e estado de revogação aplicável.
- **D)** porta e reputação comercial não substituem as verificações criptográficas e semânticas do certificado.

**Conceito:** validação completa de certificado X.509 apresentado por servidor.

**Pegadinha:** validar apenas parte dos campos ou substituir confiança criptográfica por porta, marca da emissora ou força da cifra.

**Como pensar:** pergunte quem assinou, para qual nome, durante qual período, para qual uso e se a credencial continua aceitável.

**Referência:** [16. Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado), especialmente cadeia de confiança, assinaturas, validade, nome, uso da chave e revogação contextual.

### Comentário S2D4Q194

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** porta não autentica servidor, e TLS não cifra todos os registros diretamente com a chave pública do certificado.
- **B)** o handshake negocia e deriva material secreto, autentica o servidor e produz chaves simétricas para proteger os registros da aplicação.
- **C)** certificado não entrega sozinho o segredo da sessão, Finished não substitui cadeia e nome, e essas verificações não podem ser ignoradas.
- **D)** TLS protege o canal; não corrige endpoints, não protege automaticamente armazenamento e não elimina falhas da aplicação.

**Conceito:** fluxo conceitual e limites de proteção do TLS 1.3.

**Pegadinha:** reduzir o protocolo ao certificado ou ampliar a proteção do canal para endpoints, armazenamento e código da aplicação.

**Como pensar:** percorra as fases em ordem: negociar, derivar, autenticar, confirmar e então transportar com chaves simétricas autenticadas.

**Referência:** [17. TLS](semana_02_estudo.md#s2-d4-tls), nos trechos sobre negociação, derivação de segredos, autenticação do servidor, Finished e proteção autenticada com chaves de sessão.

### Comentário S2D4Q195

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** as três afirmações delimitam a melhoria de SAE, os riscos que permanecem e a possível negociação WPA2 no modo de transição.
- **B)** I e II são verdadeiras, mas III também é; compatibilidade com cliente legado pode manter associações WPA2-Personal.
- **C)** I e III são verdadeiras, mas II também é; SAE não produz invulnerabilidade a todos os ataques ou falhas.
- **D)** II e III são verdadeiras, mas I também é; resistência à verificação offline por captura é uma diferença importante de SAE.

**Conceito:** diferença entre WPA2-Personal e WPA3-Personal, alcance de SAE e limites do modo de transição.

**Pegadinha:** transformar uma melhoria específica contra captura passiva em proteção absoluta ou presumir que todo cliente negociou WPA3.

**Como pensar:** separe três perguntas: qual troca é usada, qual ataque ela dificulta e qual modo foi realmente negociado pelo cliente.

**Referência:** [18. Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi), especialmente SAE, limites diante de senha fraca e ataque online e comportamento do modo de transição.

### Comentário S2D4Q196

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** segredo coletivo não autentica cada pessoa, e MAC pode ser alterado ou compartilhado, sem substituir identidade individual.
- **B)** segredo por setor reduz o grupo afetado, mas ainda não permite revogar um único usuário sem alterar a credencial coletiva.
- **C)** modo de transição pode admitir associação WPA2, e segredo coletivo continua sem responsabilização individual suficiente.
- **D)** Enterprise com 802.1X permite identidades individuais, revogação e registros, desde que o servidor de autenticação seja validado corretamente.

**Conceito:** segurança Wi-Fi institucional com 802.1X e identidades individuais.

**Pegadinha:** confundir identificação de dispositivo ou segredo de grupo com autenticação individual revogável.

**Como pensar:** procure uma identidade por usuário, validação do servidor e capacidade de revogar uma conta sem redistribuir segredo coletivo.

**Referência:** [18. Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi), nos trechos sobre modo Enterprise, 802.1X, identidade individual, validação do servidor e limites de segredos coletivos.

### Comentário S2D4Q197

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** restaurar antes de conter e erradicar favorece reinfecção, e apagar registros destrói material de investigação.
- **B)** a sequência confirma e delimita, limita expansão, remove causa e persistência e retorna em condição validada e monitorada.
- **C)** alerta exige análise, desligamento indiscriminado pode ampliar impacto ou perder evidência, e resposta não termina com mera disponibilidade.
- **D)** erradicar antes de conter permite expansão, e evidências relevantes devem ser preservadas antes de alterações destrutivas.

**Conceito:** objetivos e ordenação das fases de resposta a incidentes.

**Pegadinha:** antecipar restauração ou erradicação e tratar disponibilidade aparente como validação suficiente do retorno.

**Como pensar:** siga as perguntas em ordem: o que ocorreu, como limitar, como remover a causa e como voltar com confiança.

**Referência:** [19. Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes), especialmente análise, contenção, preservação de evidências, erradicação e recuperação validada.

### Comentário S2D4Q198

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** I e II descrevem corretamente as cadeias, mas III também aplica corretamente RPO e RTO ao horário dado.
- **B)** I e III são corretas, mas II também é; o diferencial mais recente já acumula mudanças desde o completo.
- **C)** II e III são corretas, mas I também é; a restauração incremental depende da sequência posterior ao completo.
- **D)** as três afirmações distinguem adequadamente as duas cadeias e os dois objetivos de recuperação.

**Conceito:** restauração incremental e diferencial, ponto de recuperação por RPO e prazo de retorno por RTO.

**Pegadinha:** trocar a quantidade de conjuntos da cadeia ou tratar RPO como duração e RTO como frequência de cópia.

**Como pensar:** resolva quatro filtros separadamente: cadeia incremental, cadeia diferencial, ponto aceitável dos dados e prazo aceitável do serviço.

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), nos trechos sobre restauração incremental e diferencial e sobre os significados temporais de RPO e RTO.

### Comentário S2D4Q199

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** as três medidas reduzem falha comum administrativa, preservam estados anteriores e comprovam que a cópia pode voltar a operar.
- **B)** I e II são corretas, mas sem III a existência da cópia não demonstra restauração íntegra, completa e funcional.
- **C)** I e III são corretas, mas II também é necessária para preservar histórico contra exclusão ou cifra propagada.
- **D)** II e III são corretas, mas I reduz a chance de credenciais e alcance de produção destruírem todas as cópias.

**Conceito:** proteção de backups contra ransomware e validação da capacidade de restauração.

**Pegadinha:** contar cópias ou versões sem avaliar isolamento administrativo e teste real de recuperação.

**Como pensar:** imagine o atacante com privilégios de produção e verifique quais cópias ainda resistem, qual histórico permanece e se ele pode ser restaurado.

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), especialmente isolamento, credenciais separadas, imutabilidade ou versões e validação periódica de restauração.

### Comentário S2D4Q200

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** dois nós aumentam disponibilidade, mas a replicação do estado atual pode copiar o dano para ambos sem oferecer versão anterior.
- **B)** RAID e replicação podem tolerar falhas físicas, mas também podem propagar exclusão ou cifra e não preservam histórico por si.
- **C)** backups podem recuperar dados, porém não fornecem componente em execução para assumir imediatamente a carga do servidor falho.
- **D)** redundância e failover sustentam continuidade diante da falha, enquanto backups versionados recuperam um estado anterior íntegro.

**Conceito:** complementaridade entre alta disponibilidade, redundância e backup versionado.

**Pegadinha:** usar uma solução de continuidade presente como se ela também preservasse histórico recuperável.

**Como pensar:** associe falha de componente a failover e dano lógico ou exclusão a uma cópia anterior protegida e testada.

**Referência:** [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), nos trechos que distinguem redundância ou alta disponibilidade de backup versionado para recuperação de estado anterior.

## Questões extras de revisão fixa do Dia 4

#### Extra Dia 4.1

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** aplicação conjunta de legalidade e eficiência.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [RF4-ADM-01 — Princípios do art. 37: LIMPE](semana_02_estudo.md#rf4-adm-01), especialmente a compatibilização entre produtividade e atuação conforme a lei.

Um gestor identifica uma etapa legalmente obrigatória que torna o procedimento lento. Considerando legalidade e eficiência, assinale a conduta compatível com o art. 37 da Constituição.

A) Suprimir imediatamente a etapa, desde que demonstre economia e registre por escrito as razões gerenciais que justificaram a decisão.

B) Buscar ganhos nas etapas permitidas e propor a alteração da regra pelos meios próprios, sem descumprir a obrigação enquanto ela vigorar.

C) Suprimir a etapa e publicar o ato posteriormente, pois transparência e redução de custo convalidam a inobservância do requisito legal.

D) Tratar a obrigação como facultativa, pois o agente público possui a mesma liberdade geral do particular para escolher como deve atuar.

#### Extra Dia 4.2

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** publicidade institucional e impessoalidade.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [RF4-ADM-02 — Publicidade institucional](semana_02_estudo.md#rf4-adm-02), no trecho sobre finalidades permitidas e vedação de promoção pessoal de autoridade ou servidor.

Uma campanha oficial sobre nova obra destaca o nome, a fotografia e um slogan eleitoral da autoridade responsável. À luz do art. 37, § 1º, assinale a alternativa correta.

A) A campanha é válida se as informações sobre a obra forem verdadeiras, pois a veracidade afasta eventual promoção pessoal da autoridade.

B) A campanha é inválida porque a Constituição proíbe até a identificação do órgão público responsável pela informação de interesse coletivo.

C) A campanha é válida se também apresentar conteúdo educativo, pois essa finalidade permite associar a realização pública à imagem do gestor.

D) A campanha deve servir à educação, à informação ou à orientação social, sem nomes, símbolos ou imagens que promovam agentes públicos.

#### Extra Dia 4.3

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** órgão, entidade, autarquia e desconcentração.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [RF4-ADM-03 — Órgão, entidade e autarquia](semana_02_estudo.md#rf4-adm-03), especialmente a distinção entre desconcentração interna e criação legal de entidade autárquica.

Um ministério cria internamente um novo departamento, enquanto lei específica cria uma autarquia para executar atividade administrativa. Assinale a classificação correta.

A) O departamento é órgão sem personalidade, surgido por desconcentração; a autarquia é entidade pública da Administração Indireta.

B) O departamento é entidade com personalidade, surgida por descentralização; a autarquia é órgão interno da Administração Direta.

C) O departamento e a autarquia são órgãos sem personalidade, pois ambos permanecem subordinados à pessoa política que os instituiu.

D) O departamento e a autarquia são entidades privadas, pois a execução especializada retira de ambos a natureza de direito público.

#### Extra Dia 4.4
- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** motivo e motivação do ato administrativo.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [RF4-ADM-04 — Elementos do ato administrativo](semana_02_estudo.md#rf4-adm-04).

Uma autoridade aplica sanção afirmando que houve inspeção em certa data, mas a inspeção jamais ocorreu. O vício central e a distinção correta são:

A) objeto; motivação é o fato que ocorreu no mundo e motivo é apenas sua redação.
B) finalidade; todo erro sobre fatos corresponde necessariamente a desvio de finalidade.
C) motivo; motivo é o suporte fático e jurídico do ato, enquanto motivação é a exposição desses fundamentos.
D) competência; fato inexistente transforma automaticamente a atribuição legal da autoridade.
#### Extra Dia 4.5

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** presunção e autoexecutoriedade.

- **Nível:** Difícil

- **Uso:** Essenciais

- **Referência:** [RF4-ADM-05 — Atributos do ato administrativo](semana_02_estudo.md#rf4-adm-05), nos trechos sobre presunção relativa e condições da autoexecutoriedade.

Considere as afirmações sobre atributos do ato administrativo: I. a presunção de legitimidade e veracidade admite prova em contrário; II. a autoexecutoriedade depende de previsão legal ou de urgência admitida pelo ordenamento; III. a autoexecutoriedade acompanha todo ato e impede controle posterior. Assinale a opção correta.

A) Está correta apenas I, ficando excluídas as afirmações II e III.

B) Estão corretas apenas II e III, ficando excluída a afirmação I.

C) Estão corretas apenas I e II, ficando excluída a afirmação III.

D) Estão corretas apenas I e III, ficando excluída a afirmação II.

#### Extra Dia 4.6

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** anulação, revogação, convalidação e decadência.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [RF4-ADM-06 — Anulação, revogação, convalidação e art. 54](semana_02_estudo.md#rf4-adm-06), especialmente os arts. 53, 54 e 55 da Lei nº 9.784/1999 sintetizados na seção.

Considere as afirmações à luz da Lei nº 9.784/1999: I. ato ilegal deve ser anulado; II. ato válido pode ser revogado por mérito; III. defeito sanável pode ser convalidado sem lesão ao interesse público ou prejuízo a terceiro; IV. o direito de anular ato favorável decai em cinco anos, salvo má-fé. Assinale a opção correta.

A) Estão corretas somente I e II, com exclusão das afirmações III e IV.

B) Estão corretas somente I, III e IV, com exclusão da afirmação II.

C) Estão corretas somente II, III e IV, com exclusão da afirmação I.

D) Estão corretas I, II, III e IV, sem exclusão de nenhuma afirmação.

#### Extra Dia 4.7

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** compatibilização entre transparência e proteção de dados.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [RF4-ADM-07 — LAI e LGPD](semana_02_estudo.md#rf4-adm-07), no trecho sobre análise contextual, acesso parcial e afastamento dos absolutos de divulgação total e sigilo total.

Um pedido de acesso alcança documento com gastos públicos e dados pessoais sem relação necessária com a fiscalização da despesa. Considerando LAI e LGPD, assinale a alternativa correta.

A) O órgão deve avaliar finalidade, necessidade, interesse público e restrições legais, permitindo o acesso à parte pública e protegendo dados pessoais quando cabível.

B) O órgão deve negar integralmente o pedido, pois a presença de qualquer dado pessoal transforma todo o documento em informação sigilosa pelo prazo máximo.

C) O órgão deve divulgar integralmente o documento, pois a existência de gasto público elimina a incidência dos princípios de finalidade e necessidade sobre os dados pessoais.

D) O órgão deve eliminar previamente todos os dados pessoais, pois a LGPD impede seu tratamento pelo Poder Público até para cumprir competência ou atribuição legal.

#### Extra Dia 4.8
- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** dolo e tipicidade na improbidade administrativa.
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [RF4-ADM-08 — Improbidade administrativa](semana_02_estudo.md#rf4-adm-08).

Um agente pratica irregularidade administrativa, mas não há demonstração de dolo nem enquadramento em conduta tipificada na Lei de Improbidade. Assinale a alternativa correta.

A) Toda ilegalidade constitui automaticamente improbidade contra princípios.
B) A voluntariedade do ato substitui o dolo e a tipicidade exigidos pela lei.
C) Mera ilegalidade não basta: o enquadramento por improbidade exige conduta dolosa tipificada e os demais requisitos legais.
D) A ausência de dano ao erário exclui qualquer modalidade de improbidade, mesmo quando exista outro tipo doloso.
#### Extra Dia 4.9

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** modalidades, dispensa e inexigibilidade.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [RF4-ADM-09 — Modalidades, dispensa e inexigibilidade](semana_02_estudo.md#rf4-adm-09), especialmente os arts. 28, 33, 72, 74 e 75 da Lei nº 14.133/2021 sintetizados na seção.

Considere as afirmações sobre a Lei nº 14.133/2021: I. pregão, concorrência, concurso, leilão e diálogo competitivo são modalidades; II. menor preço e técnica e preço são critérios de julgamento, não modalidades; III. dispensa decorre de hipótese legal e inexigibilidade de competição inviável, sem afastar instrução e motivação. Assinale a opção correta.

A) Estão corretas apenas I e II, ficando excluída a afirmação III.

B) Estão corretas I, II e III, sem exclusão de nenhuma afirmação.

C) Estão corretas apenas I e III, ficando excluída a afirmação II.

D) Estão corretas apenas II e III, ficando excluída a afirmação I.

#### Extra Dia 4.10

- **Dia:** Dia 4

- **Bloco:** Bloco 4

- **Matéria:** Administração Pública

- **Assunto:** responsabilidade objetiva e direito de regresso.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [RF4-ADM-10 — Responsabilidade civil do Estado](semana_02_estudo.md#rf4-adm-10), no contraste entre responsabilidade objetiva perante a vítima e elemento subjetivo exigido no direito de regresso.

Durante o serviço, um agente causa dano a terceiro com veículo público. Provados a conduta estatal, o dano e o nexo causal, assinale a alternativa correta sobre a reparação e eventual regresso.

A) A vítima não precisa provar culpa para responsabilizar o Estado; no regresso, porém, deve ser demonstrado dolo ou culpa do agente.

B) O Estado indeniza mesmo sem dano ou nexo causal; depois do pagamento, o regresso decorre automaticamente do vínculo funcional do agente.

C) A vítima deve demandar primeiro o agente e provar sua culpa; o Estado responde apenas de forma subsidiária se ele não tiver patrimônio.

D) O Estado só indeniza se a vítima provar dolo do agente; depois do pagamento, o regresso dispensa prova de dolo ou culpa do responsável.

#### Extra Dia 4.11
- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** negação da conjunção.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RF4-RLM-01 — Negação de conjunção e disjunção](semana_02_estudo.md#rf4-rlm-01).

Considere as proposições P: “o firewall bloqueou a origem” e Q: “o IPS conteve o ataque”. A negação de “P e Q” é:

A) “P ou Q”.
B) “não P e não Q”.
C) “não P ou não Q”.
D) “P se, e somente se, Q”.
#### Extra Dia 4.12
- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** negação da condicional e do quantificador universal.
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [RF4-RLM-02 — Condicional e quantificadores](semana_02_estudo.md#rf4-rlm-02).

Assinale a alternativa que apresenta corretamente a negação de uma condicional e de um quantificador universal.

A) A negação de “P implica Q” é “não P implica não Q”, e a de “todo servidor tem backup” é “nenhum servidor tem backup”.
B) A negação de “P implica Q” é “não P e Q”, e a de “todo” preserva o quantificador universal.
C) A negação de “P implica Q” é “P e não Q”, e a de “todo servidor tem backup” é “existe pelo menos um servidor que não tem backup”.
D) A negação de “P implica Q” é “P ou Q”, e a de “todo” é “algum”, sem negar o predicado.
#### Extra Dia 4.13
- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** princípio da inclusão-exclusão.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RF4-RLM-03 — Princípio da inclusão-exclusão](semana_02_estudo.md#rf4-rlm-03).

Em uma auditoria, 42 ativos possuem o controle A, 35 possuem o controle B e 17 possuem ambos. Quantos possuem pelo menos um dos dois controles?

A) 77.
B) 60.
C) 94.
D) 24.
#### Extra Dia 4.14
- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** porcentagem reversa.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RF4-RLM-04 — Porcentagem reversa](semana_02_estudo.md#rf4-rlm-04).

Após desconto de 20%, uma licença passou a custar R$ 240,00. Qual era o preço anterior ao desconto?

A) R$ 192,00.
B) R$ 260,00.
C) R$ 288,00.
D) R$ 300,00.
#### Extra Dia 4.15
- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** proporção inversa e produtividade.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [RF4-RLM-05 — Proporção e produtividade](semana_02_estudo.md#rf4-rlm-05).

Se 6 analistas, com a mesma produtividade, concluem uma revisão em 12 horas, em quanto tempo 9 analistas concluiriam o mesmo trabalho, mantidas as demais condições?

A) 8 horas.
B) 18 horas.
C) 6 horas.
D) 27 horas.
#### Extra Dia 4.16
- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** relações de sentido dos conectores.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [RF4-PT-01 — Conectores](semana_02_estudo.md#rf4-pt-01).

Leia: “Embora o controle reduzisse o risco, ocorreu um incidente; portanto, o plano de resposta foi acionado.” Os conectores destacados exprimem, respectivamente:

A) causa e oposição.
B) condição e finalidade.
C) concessão e conclusão.
D) conclusão e concessão.
#### Extra Dia 4.17
- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** referência anafórica e inferência autorizada.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [RF4-PT-02 — Inferência e referência](semana_02_estudo.md#rf4-pt-02).

Leia: “A equipe isolou apenas o servidor comprometido. Essa medida conteve o tráfego, mas não comprovou a erradicação da ameaça.” Assinale a alternativa correta.

A) “Essa medida” anuncia uma providência ainda não mencionada, em referência catafórica.
B) “Essa medida” retoma o isolamento do servidor, e o texto não autoriza concluir que a ameaça foi erradicada.
C) O trecho permite inferir que todos os servidores foram isolados e restaurados.
D) A contenção do tráfego comprova necessariamente a eliminação da causa do incidente.
#### Extra Dia 4.18

- **Dia:** Dia 4

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** concordância de `haver` e `existir`.

- **Nível:** Médio

- **Uso:** Simulado

- **Referência:** [RF4-PT-03 — Haver existencial e existir](semana_02_estudo.md#rf4-pt-03), especialmente a impessoalidade de “haver” existencial e a concordância pessoal de “existir”.

Assinale a alternativa integralmente redigida de acordo com a norma-padrão de concordância.

A) Devem haver falhas no inventário, e existia registros ainda sem revisão.

B) Houveram falhas no inventário, e deve existir registros ainda sem revisão.

C) Havia falhas no inventário, e deve existirem registros ainda sem revisão.

D) Pode haver falhas no inventário, e existem registros ainda sem revisão.

#### Extra Dia 4.19
- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pontuação e crase.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [RF4-PT-04 — Pontuação e crase](semana_02_estudo.md#rf4-pt-04).

Assinale a alternativa com pontuação e emprego da crase adequados.

A) Após a contenção do incidente, a equipe dirigiu-se à sala de crise.
B) Os relatórios produzidos pela equipe, foram entregues à revisar.
C) O analista encaminhou, a evidência a autoridade responsável.
D) A equipe começou à restaurar o serviço, e o gestor à acompanhou.
#### Extra Dia 4.20

- **Dia:** Dia 4
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita com preservação de causa e consequência.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [RF4-PT-05 — Reescrita e clareza](semana_02_estudo.md#rf4-pt-05).

Original: “Como havia risco imediato, a equipe isolou o servidor.” Assinale a reescrita que preserva o sentido e a correção.

A) Embora não houvesse risco, a equipe isolou necessariamente todos os servidores.
B) A equipe isolou o servidor; contudo, havia risco imediato como consequência.
C) Se a equipe isolou o servidor, então não poderia haver risco imediato.
D) Havia risco imediato; por isso, a equipe isolou o servidor.

### Gabarito das questões extras do Dia 4

| Extra | Resposta |
|---:|:---:|
| 4.1 | B |
| 4.2 | D |
| 4.3 | A |
| 4.4 | C |
| 4.5 | C |
| 4.6 | D |
| 4.7 | A |
| 4.8 | C |
| 4.9 | B |
| 4.10 | A |
| 4.11 | C |
| 4.12 | C |
| 4.13 | B |
| 4.14 | D |
| 4.15 | A |
| 4.16 | C |
| 4.17 | B |
| 4.18 | D |
| 4.19 | A |
| 4.20 | D |

### Comentários das questões extras do Dia 4

#### Comentário Extra Dia 4.1

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** vantagem econômica e motivação não autorizam o agente a afastar requisito legal vigente.
- **B)** eficiência orienta a otimização possível, mas a mudança da obrigação precisa ocorrer pela via juridicamente competente.
- **C)** publicidade posterior não sana automaticamente a violação da legalidade.
- **D)** o agente público atua segundo competências e autorizações jurídicas, e não pela liberdade geral reservada ao particular.

**Conceito:** aplicação conjunta dos princípios da legalidade e da eficiência.

**Pegadinha:** transformar eficiência, economia ou publicidade em autorização para descumprir a lei.

**Como pensar:** verifique primeiro os limites jurídicos; dentro deles, escolha a solução de melhor qualidade e produtividade.

**Referência:** [RF4-ADM-01 — Princípios do art. 37: LIMPE](semana_02_estudo.md#rf4-adm-01), especialmente a compatibilização entre produtividade e atuação conforme a lei.

#### Comentário Extra Dia 4.2

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** uma mensagem verdadeira ainda pode violar a impessoalidade ao promover pessoalmente a autoridade.
- **B)** identificação institucional necessária à orientação do cidadão não se confunde com promoção do agente.
- **C)** finalidade educativa não autoriza nome, fotografia ou slogan que personalize a realização administrativa.
- **D)** a opção preserva as finalidades constitucionais e a proibição de elementos caracterizadores de promoção pessoal.

**Conceito:** finalidade e limites impessoais da publicidade institucional.

**Pegadinha:** supor que veracidade ou conteúdo educativo neutralizam automaticamente a personalização da campanha.

**Como pensar:** separe informação sobre a atuação do órgão de propaganda centrada na imagem de quem ocupa o cargo.

**Referência:** [RF4-ADM-02 — Publicidade institucional](semana_02_estudo.md#rf4-adm-02), no trecho sobre finalidades permitidas e vedação de promoção pessoal de autoridade ou servidor.

#### Comentário Extra Dia 4.3

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** departamento interno é centro de competências sem personalidade, enquanto a autarquia é pessoa jurídica pública da Administração Indireta.
- **B)** a alternativa inverte personalidade, técnica organizacional e posição administrativa das duas estruturas.
- **C)** a autarquia possui personalidade jurídica própria, embora permaneça vinculada à finalidade legal e sujeita a controle.
- **D)** especialização administrativa não transforma departamento nem autarquia em entidade de direito privado.

**Conceito:** diferença entre órgão, entidade autárquica, desconcentração e descentralização.

**Pegadinha:** equiparar criação de unidade interna à criação de nova pessoa jurídica.

**Como pensar:** pergunte se surgiu uma nova personalidade jurídica; sem ela há órgão e desconcentração, com autarquia há entidade e descentralização.

**Referência:** [RF4-ADM-03 — Órgão, entidade e autarquia](semana_02_estudo.md#rf4-adm-03), especialmente a distinção entre desconcentração interna e criação legal de entidade autárquica.

#### Comentário Extra Dia 4.4
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Essenciais

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

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** a afirmação II também é correta, pois autoexecutoriedade não é atributo incondicionado.
- **B)** I é verdadeira e III é falsa; execução direta não elimina controle administrativo ou judicial posterior.
- **C)** I reconhece o caráter relativo da presunção, II expressa as hipóteses de execução direta e III formula um absoluto falso.
- **D)** II é verdadeira e III é falsa; nem todo ato pode ser executado coercitivamente sem ordem judicial.

**Conceito:** limites da presunção de legitimidade e da autoexecutoriedade.

**Pegadinha:** converter atributos relativos ou condicionados em poderes absolutos e imunes a controle.

**Como pensar:** avalie separadamente a possibilidade de prova contrária e a existência de fundamento para execução direta.

**Referência:** [RF4-ADM-05 — Atributos do ato administrativo](semana_02_estudo.md#rf4-adm-05), nos trechos sobre presunção relativa e condições da autoexecutoriedade.

#### Comentário Extra Dia 4.6

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** III e IV também são verdadeiras, pois a Lei prevê convalidação condicionada e decadência com ressalva de má-fé.
- **B)** II é verdadeira; a Administração pode revogar ato válido por conveniência ou oportunidade, respeitados os limites jurídicos.
- **C)** I é verdadeira; ilegalidade conduz à anulação, e não à revogação por mérito.
- **D)** as quatro afirmações preservam, respectivamente, legalidade, mérito, condições de saneamento e limite temporal do poder de anular.

**Conceito:** distinção e condições de anulação, revogação, convalidação e decadência administrativa.

**Pegadinha:** trocar ilegalidade por mérito, universalizar a convalidação ou ignorar o limite temporal do ato favorável.

**Como pensar:** classifique primeiro o problema como ilegalidade, mérito ou vício sanável; depois verifique prejuízo, boa-fé e prazo.

**Referência:** [RF4-ADM-06 — Anulação, revogação, convalidação e art. 54](semana_02_estudo.md#rf4-adm-06), especialmente os arts. 53, 54 e 55 da Lei nº 9.784/1999 sintetizados na seção.

#### Comentário Extra Dia 4.7

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** transparência e proteção de dados devem ser compatibilizadas, inclusive mediante acesso à parcela pública e resguardo do conteúdo protegido.
- **B)** dado pessoal não torna automaticamente sigiloso todo o documento nem determina, por si só, prazo máximo de restrição.
- **C)** interesse no gasto público não elimina finalidade, necessidade e demais limites incidentes sobre dados pessoais.
- **D)** a LGPD permite tratamento pelo Poder Público para finalidade pública e execução de competência ou atribuição legal.

**Conceito:** convivência entre transparência pública e proteção juridicamente adequada de dados pessoais.

**Pegadinha:** substituir a análise contextual por sigilo total, divulgação total ou proibição total de tratamento.

**Como pensar:** identifique a finalidade do acesso, separe a informação pública do dado protegido e aplique a restrição apenas na medida necessária.

**Referência:** [RF4-ADM-07 — LAI e LGPD](semana_02_estudo.md#rf4-adm-07), no trecho sobre análise contextual, acesso parcial e afastamento dos absolutos de divulgação total e sigilo total.

#### Comentário Extra Dia 4.8
**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Aprofundamento

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

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** a afirmação III também é verdadeira; contratação direta não elimina processo e motivação.
- **B)** as três afirmações separam modalidades, critérios e fundamentos distintos de contratação direta.
- **C)** a afirmação II é verdadeira, pois menor preço e técnica e preço pertencem ao rol de critérios de julgamento.
- **D)** a afirmação I é verdadeira e reproduz as cinco modalidades previstas na nova Lei de Licitações.

**Conceito:** distinção entre modalidade, critério de julgamento, dispensa e inexigibilidade.

**Pegadinha:** chamar critérios de modalidades ou tratar contratação direta como ausência de instrução processual.

**Como pensar:** monte três caixas antes de responder: formas do procedimento, critérios para julgar propostas e fundamentos da contratação direta.

**Referência:** [RF4-ADM-09 — Modalidades, dispensa e inexigibilidade](semana_02_estudo.md#rf4-adm-09), especialmente os arts. 28, 33, 72, 74 e 75 da Lei nº 14.133/2021 sintetizados na seção.

#### Comentário Extra Dia 4.10

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** perante a vítima, a culpa é dispensada; perante o agente, a pretensão regressiva requer dolo ou culpa.
- **B)** dano e nexo causal continuam necessários, e o vínculo funcional sozinho não basta para a ação regressiva.
- **C)** o regime constitucional não torna a responsabilidade estatal meramente subsidiária nas condições descritas.
- **D)** a vítima não precisa provar dolo ou culpa para a responsabilidade objetiva, mas o regresso depende de um desses elementos.

**Conceito:** requisitos distintos da responsabilidade objetiva estatal e do direito de regresso.

**Pegadinha:** transportar a objetividade da relação Estado-vítima para a relação regressiva contra o agente.

**Como pensar:** separe as duas relações jurídicas e pergunte, em cada uma, quais fatos precisam ser demonstrados.

**Referência:** [RF4-ADM-10 — Responsabilidade civil do Estado](semana_02_estudo.md#rf4-adm-10), no contraste entre responsabilidade objetiva perante a vítima e elemento subjetivo exigido no direito de regresso.

#### Comentário Extra Dia 4.11
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** Incorreta. Mantém as proposições positivas e não nega a conjunção.
- **B)** Incorreta. Exige que ambas sejam falsas, condição mais forte que a negação da conjunção.
- **C)** Correta. Pela lei de De Morgan, nega-se cada parcela e troca-se `e` por `ou`.
- **D)** Incorreta. Bicondicional expressa equivalência, não a negação pedida.

**Conceito:** negação da conjunção.

**Pegadinha:** negar cada parcela sem trocar o conectivo.

**Como pensar:** `não (P e Q)` transforma-se em `não P ou não Q`.

**Referência:** [RF4-RLM-01 — Negação de conjunção e disjunção](semana_02_estudo.md#rf4-rlm-01).

#### Comentário Extra Dia 4.12
**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Revisão

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

**Nível:** Médio

**Uso:** Revisão

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

**Nível:** Médio

**Uso:** Revisão

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

**Nível:** Médio

**Uso:** Revisão

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

**Nível:** Médio

**Uso:** Simulado

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

**Nível:** Difícil

**Uso:** Simulado

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

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** a locução com “haver” existencial deve ficar no singular, e “existia” deveria concordar com “registros”.
- **B)** “houveram” deve permanecer no singular, e a locução com “existir” deve concordar no plural com “registros”.
- **C)** “havia falhas” está correto, mas o auxiliar de “existir” deve ir ao plural em “devem existir registros”.
- **D)** “pode haver” permanece no singular e “existem” concorda com o sujeito plural “registros”.

**Conceito:** impessoalidade de “haver” existencial e concordância do verbo “existir”.

**Pegadinha:** flexionar “haver” como se tivesse sujeito ou manter “existir” no singular diante de sujeito plural.

**Como pensar:** se puder trocar por “existir”, mantenha “haver” e seu auxiliar no singular; com “existir”, localize o sujeito.

**Referência:** [RF4-PT-03 — Haver existencial e existir](semana_02_estudo.md#rf4-pt-03), especialmente a impessoalidade de “haver” existencial e a concordância pessoal de “existir”.

#### Comentário Extra Dia 4.19
**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

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
**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Altera causa para concessão, nega o risco e amplia um servidor para todos.
- **B)** Incorreta. `Contudo` cria oposição e inverte a relação causal original.
- **C)** Incorreta. Cria uma condicional e uma negação de risco inexistentes no original.
- **D)** Correta. `Por isso` apresenta a consequência da causa expressa na primeira oração.

**Conceito:** reescrita com preservação de causa e consequência.

**Pegadinha:** manter vocabulário semelhante, mas trocar conector, alcance ou polaridade.

**Como pensar:** compare agente, ação, causa, consequência e grau de certeza.

**Referência:** [RF4-PT-05 — Reescrita e clareza](semana_02_estudo.md#rf4-pt-05).



---

# Dia 5 — Sistemas Operacionais Avançados

## Questões principais


### S2D5Q201 — Concorrência é organização temporal com possíveis intercalações; paralelismo é execução simultânea

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Concorrência e paralelismo](semana_02_estudo.md#s2-d5-concorrencia-paralelismo).

Em um computador com um único núcleo, o sistema operacional alterna a execução das tarefas A e B ao longo de certo intervalo, de modo que ambas avançam, embora apenas uma execute a cada instante. Nesse caso, ocorre

A) paralelismo sem concorrência, pois as tarefas não compartilham o mesmo instante de CPU.
B) concorrência sem paralelismo, pois há progresso intercalado, mas não execução simultânea.
C) paralelismo e concorrência, pois toda alternância de contexto equivale à simultaneidade.
D) ausência de concorrência, pois ela exige pelo menos dois núcleos físicos.

### S2D5Q202 — Programa é passivo, processo é instância em execução e thread é fluxo escalonável dentro do processo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Programa, processo e thread](semana_02_estudo.md#s2-d5-processo-thread).

Sobre programa, processo e thread, assinale a afirmativa correta.

A) Programa é uma instância ativa que já possui, necessariamente, contador de programa e pilha de execução.
B) Threads distintas de um mesmo processo possuem espaços de endereçamento totalmente isolados entre si.
C) Processo é apenas o arquivo executável armazenado, sem estado ou recursos associados à execução.
D) Threads do mesmo processo normalmente compartilham código, dados e recursos abertos, mas mantêm pilhas e registradores próprios.

### S2D5Q203 — Pronto aguarda CPU; bloqueado aguarda evento, E/S, lock ou tempo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Programa, processo e thread — estados conceituais](semana_02_estudo.md#s2-d5-processo-thread).

Uma thread solicitou a leitura de um bloco em disco e aguarda a conclusão da operação. Enquanto o evento não ocorre, ela se encontra conceitualmente no estado

A) bloqueado, e elevar sua prioridade não substitui a conclusão da E/S aguardada.
B) pronto, pois toda thread que não está usando a CPU disputa imediatamente o processador.
C) executando, pois a operação de disco foi iniciada em seu nome.
D) terminado, pois deixou de executar instruções no processador.

### S2D5Q204 — Troca de contexto viabiliza a multiplexação, mas tem custo; o quantum equilibra resposta e sobrecarga

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Programa, processo e thread — troca de contexto](semana_02_estudo.md#s2-d5-processo-thread).

Em um sistema que usa Round Robin, a equipe reduz bastante o quantum, mantendo inalteradas as demais condições. Um efeito plausível dessa decisão é

A) eliminar as trocas de contexto, já que cada tarefa permanecerá menos tempo na CPU.
B) transformar o algoritmo em FCFS, pois os processos passarão a executar até o fim.
C) melhorar a responsividade em alguns cenários, ao custo de mais trocas de contexto e maior sobrecarga.
D) fazer com que threads bloqueadas por E/S se tornem prontas a cada expiração do quantum.

### S2D5Q205 — Condição de corrida e atualização perdida

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Seção crítica, condição de corrida e atomicidade](semana_02_estudo.md#s2-d5-corrida-atomicidade), no exemplo que decompõe atualização em leitura, cálculo e escrita e identifica a atualização perdida.

Duas threads executam sem sincronização `contador = contador + 1`, partindo de 40. Ambas leem 40, calculam 41 e gravam 41. Como deve ser classificado esse resultado?

A) Deadlock, pois cada thread mantém um recurso exclusivo e espera indefinidamente que a outra libere o recurso necessário.

B) Starvation, pois o escalonador favorece continuamente uma thread e impede que a outra conclua sua operação sobre o contador.

C) Condição de corrida com atualização perdida, pois ambas calculam sobre o mesmo valor antigo e uma gravação encobre o outro incremento.

D) Livelock, pois as threads reagem e repetem o incremento indefinidamente, permanecendo ativas sem concluir a operação lógica.

### S2D5Q206 — Atomicidade, visibilidade e ordenação são propriedades relacionadas, mas distintas

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Seção crítica, condição de corrida e atomicidade](semana_02_estudo.md#s2-d5-corrida-atomicidade).

Quanto à atomicidade em programas concorrentes, assinale a afirmativa correta.

A) Se cada instrução de máquina for atômica, qualquer sequência formada por elas também será atômica.
B) A atomicidade de uma operação isolada não torna atômica uma sequência; visibilidade e ordenação também podem afetar a correção.
C) Uma atribuição escrita em uma única linha de linguagem de alto nível é necessariamente indivisível para todas as threads.
D) Atomicidade e exclusão mútua garantem, por si sós, que toda gravação seja imediatamente visível em qualquer arquitetura.

### S2D5Q207 — Mutex implementa exclusão mútua cooperativa e propriedade exclusiva do lock

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

Um mutex protege o saldo de uma conta compartilhada. Para que o protocolo de exclusão seja efetivo, é correto afirmar que

A) basta uma das threads usar o mutex, pois o sistema operacional bloqueará automaticamente acessos não cooperantes.
B) todos os participantes que acessam o saldo devem respeitar o mesmo protocolo de aquisição e liberação do mutex.
C) o mutex torna atômicas todas as operações do processo, inclusive as que não usam esse mecanismo.
D) a thread que adquiriu o mutex pode delegar livremente sua liberação a qualquer fluxo, pois mutex não expressa propriedade.

### S2D5Q208 — Semáforo contador para unidades equivalentes

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Mutex, semáforos, monitores e variáveis de condição — semáforo binário e contador](semana_02_estudo.md#s2-d5-sincronizacao), no trecho que relaciona o contador a N unidades do recurso.

Um pool possui oito conexões equivalentes, e cada cliente deve ocupar exatamente uma delas enquanto realiza sua operação. Qual primitiva representa diretamente a disponibilidade do pool?

A) Um semáforo binário iniciado em um, decrementado na aquisição e incrementado quando qualquer uma das oito conexões é devolvida.

B) Um mutex único que admite oito proprietários simultâneos e transfere sua propriedade a cada cliente que entra no pool.

C) Um semáforo contador iniciado em oito, decrementado na aquisição e incrementado quando a conexão ocupada é devolvida.

D) Uma variável de condição sem contador associado, cuja notificação representa permanentemente cada conexão ainda disponível no pool.

### S2D5Q209 — Variável de condição coordena a espera por um predicado associado a estado protegido por mutex

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

Uma consumidora retira itens de uma fila protegida por mutex e aguarda quando a fila está vazia. No padrão correto com variável de condição, a consumidora deve

A) manter o mutex enquanto dorme, impedindo que o produtor altere a fila até o despertar.
B) testar a fila uma única vez com `if`, pois notificações eliminam despertares espúrios e disputas após o despertar.
C) liberar o mutex, aguardar e continuar sem readquiri-lo, para evitar qualquer contenção.
D) verificar o predicado em laço; a espera libera atomicamente o mutex e o readquire antes de retornar.

### S2D5Q210 — Spinlock usa espera ativa e depende de uma expectativa de retenção muito curta

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Mutex, semáforos, monitores e variáveis de condição — spinlock](semana_02_estudo.md#s2-d5-sincronizacao).

Sobre spinlocks, assinale a alternativa correta.

A) Podem ser úteis em trechos muito curtos, especialmente em multiprocessadores, mas desperdiçam CPU quando a espera se prolonga.
B) São indicados para esperas longas por E/S, pois a espera ativa economiza ciclos de CPU.
C) Colocam obrigatoriamente a thread para dormir até que o recurso seja liberado.
D) São sempre a melhor escolha em um único núcleo não preemptível, mesmo se o detentor do lock ainda precisar executar.

### S2D5Q211 — Memória compartilhada favorece throughput e transfere ao projeto a responsabilidade pela sincronização

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Comunicação entre processos — IPC](semana_02_estudo.md#s2-d5-ipc).

Dois processos locais precisam trocar grande volume de dados com baixa sobrecarga de cópia. A equipe escolhe memória compartilhada. Essa escolha

A) pode favorecer o desempenho, mas exige um protocolo adicional de sincronização e visibilidade para acessos concorrentes.
B) elimina condições de corrida, pois o sistema serializa automaticamente toda leitura e gravação na área comum.
C) preserva unidades de mensagem e ordenação por prioridade de forma inerente, como uma fila de mensagens.
D) impede que os processos alterem a mesma região, preservando o isolamento integral entre eles.

### S2D5Q212 — Mecanismos de IPC diferem em localidade, estrutura dos dados, direção, persistência e custo de cópia

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Comunicação entre processos — IPC](semana_02_estudo.md#s2-d5-ipc).

Considere mecanismos de comunicação entre processos. Assinale a associação correta.

A) Sinal — transporte de grandes blocos estruturados; socket — restrito a processos com relação de parentesco.
B) Pipe anônimo — necessariamente acessível por nome global; memória compartilhada — dispensa sincronização.
C) Fila de mensagens — preserva unidades de mensagem; socket — pode atender comunicação local ou em rede.
D) FIFO — exige que os processos sejam pai e filho; RPC — elimina falhas de transporte e serialização.

### S2D5Q213 — Deadlock como impasse conjunto

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Deadlock](semana_02_estudo.md#s2-d5-deadlock), no parágrafo inicial que define o conjunto bloqueado por dependências internas de recursos ou eventos.

Quatro processos deixaram de progredir. Qual cenário caracteriza propriamente um deadlock do conjunto?

A) Um processo pronto é continuamente ultrapassado por outros, embora todos os demais continuem concluindo suas execuções normalmente.

B) Os processos alteram repetidamente suas ações em resposta uns aos outros, permanecendo ativos sem produzir avanço útil.

C) Todos aguardam uma operação de disco lenta, mas o dispositivo continua processando pedidos e sinalizará cada conclusão.

D) Cada processo aguarda um recurso mantido por outro integrante bloqueado, formando dependências fechadas que nenhum deles pode desfazer.

### S2D5Q214 — Condições necessárias de Coffman

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Deadlock — as quatro condições necessárias de Coffman](semana_02_estudo.md#s2-d5-deadlock), na lista numerada das condições e em sua aplicação conjunta.

No modelo clássico de recursos reutilizáveis, qual conjunto contém exatamente as quatro condições necessárias de Coffman que, coexistindo, possibilitam deadlock?

A) Exclusão mútua, posse e espera, preempção compulsória e espera circular.

B) Exclusão mútua, posse e espera, não preempção e espera circular.

C) Exclusão mútua, posse e espera, não preempção e espera acíclica.

D) Exclusão mútua, liberação antecipada, não preempção e espera circular.

### S2D5Q215 — Prevenção rompe deliberadamente ao menos uma condição necessária; ordenação global rompe espera circular

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Deadlock — prevenção](semana_02_estudo.md#s2-d5-deadlock).

Uma aplicação impõe a regra de que todos os fluxos devem adquirir os locks `L1`, `L2` e `L3` sempre nessa ordem crescente, inclusive nos caminhos de erro. Essa é uma técnica de prevenção que atua diretamente contra a condição de

A) espera circular.
B) exclusão mútua.
C) não preempção.
D) posse e espera.

### S2D5Q216 — Aquisição integral antecipada é prevenção por ruptura da condição de posse e espera

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Deadlock — prevenção](semana_02_estudo.md#s2-d5-deadlock).

Um sistema exige que cada processo solicite, antes de iniciar, todos os recursos de que precisará; se o conjunto completo não estiver disponível, nenhum deles é concedido. A estratégia previne o deadlock principalmente por romper

A) a exclusão mútua, pois todos os recursos passam a ser compartilháveis.
B) a não preempção, pois o sistema retira recursos já concedidos a qualquer momento.
C) a posse e espera, embora possa reduzir a utilização dos recursos.
D) a espera circular, sem produzir qualquer impacto sobre a eficiência.

### S2D5Q217 — Estado seguro na evitação de deadlock

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Deadlock — evitação](semana_02_estudo.md#s2-d5-deadlock), na definição de sequência segura e na ressalva de que estado inseguro não significa deadlock já ocorrido.

Um algoritmo de evitação avalia o estado que resultaria da concessão de um pedido. Qual critério distingue corretamente estado seguro de estado inseguro?

A) O estado é seguro somente sem recursos alocados; o estado inseguro significa que um ciclo já bloqueia todos os participantes.

B) O estado é seguro somente se todas as demandas puderem ser atendidas simultaneamente; o estado inseguro comprova deadlock atual.

C) O estado é seguro quando algum processo pode concluir imediatamente; o estado inseguro significa indisponibilidade permanente de todo recurso.

D) O estado é seguro se existe uma sequência de conclusão para todos; o estado inseguro perde essa garantia, sem provar deadlock atual.

### S2D5Q218 — O algoritmo do banqueiro evita estados inseguros com base em demanda máxima conhecida e disponibilidade

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Deadlock — evitação](semana_02_estudo.md#s2-d5-deadlock).

O algoritmo do banqueiro é um exemplo clássico de evitação de deadlock. Para decidir se uma concessão preserva um estado seguro, ele pressupõe, entre outros dados,

A) apenas a prioridade atual de cada processo, sem informações sobre recursos.
B) as demandas máximas declaradas, as alocações correntes e os recursos disponíveis.
C) somente um grafo de espera com exatamente uma instância de cada recurso.
D) a interrupção compulsória de qualquer processo sempre que houver uma nova solicitação.

### S2D5Q219 — Ciclos e número de instâncias na detecção de deadlock

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Deadlock — detecção](semana_02_estudo.md#s2-d5-deadlock), no contraste entre grafo com instância única e análise de disponíveis, alocados e pedidos quando há múltiplas instâncias.

Ao analisar ciclos em um grafo de espera, como o número de instâncias de cada tipo de recurso afeta a conclusão sobre deadlock?

A) Com uma instância por tipo, o ciclo é necessário e suficiente; com várias, as quantidades importam e o ciclo isolado não basta.

B) Com uma instância por tipo, o ciclo é apenas necessário; com várias, qualquer ciclo basta, sem considerar as quantidades disponíveis.

C) Com uma ou várias instâncias por tipo, todo ciclo é necessário e suficiente, independentemente das quantidades de recursos ainda disponíveis.

D) Com uma instância por tipo, a ausência de ciclo confirma deadlock; com várias, qualquer processo bloqueado basta, mesmo havendo recursos disponíveis.

### S2D5Q220 — Recuperação pode abortar, preemptar quando possível ou restaurar estado, sempre respeitando consistência e custo

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Deadlock — recuperação](semana_02_estudo.md#s2-d5-deadlock).

Após detectar um deadlock em operações transacionais, o sistema precisa recuperar o progresso preservando a consistência. Uma ação tecnicamente adequada é

A) encerrar aleatoriamente todos os participantes, sem avaliar dados ou trabalho já realizado.
B) ignorar o ciclo, pois a detecção já rompe automaticamente uma das condições de Coffman.
C) escolher vítima por critérios de custo e, quando suportado, abortar ou restaurar um checkpoint consistente.
D) aumentar a prioridade de todos os processos, o que libera compulsoriamente os recursos mantidos.

### S2D5Q221 — Starvation afeta um participante continuamente preterido enquanto o sistema como um todo pode progredir

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

Em um escalonador de prioridade estrita, tarefas de baixa prioridade permanecem prontas, mas são continuamente ultrapassadas por novas tarefas de alta prioridade. O problema e uma mitigação compatível são, respectivamente,

A) deadlock e imposição de ordem global de locks.
B) livelock e redução do número de núcleos.
C) condição de corrida e uso de memória compartilhada.
D) starvation e aging gradual da prioridade de quem espera.

### S2D5Q222 — Livelock é atividade contínua sem avanço útil, muitas vezes produzida por respostas simétricas

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

Duas threads detectam conflito, liberam seus recursos, tentam novamente ao mesmo tempo e repetem indefinidamente esse comportamento. Elas continuam ativas, mas não concluem trabalho útil. Trata-se de

A) livelock, que pode ser mitigado por backoff aleatório para romper a simetria.
B) starvation, necessariamente causada por uma fila de prioridade estrita.
C) deadlock, pois ambas permanecem bloqueadas sem mudar de estado.
D) paralelismo, que se resolve substituindo threads por programas passivos.

### S2D5Q223 — Inversão de prioridade é a espera indireta de uma thread alta por uma baixa que mantém recurso necessário

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

Uma thread de alta prioridade aguarda um mutex mantido por uma thread de baixa prioridade. Threads de prioridade intermediária preemptam repetidamente a detentora, retardando a liberação do mutex. O cenário descreve

A) starvation da thread de baixa prioridade, resolvida necessariamente por aumentar o quantum de todas as threads.
B) inversão de prioridade, mitigável por herança temporária da prioridade pela detentora do mutex.
C) deadlock clássico, pois as quatro condições de Coffman estão demonstradas no enunciado.
D) livelock, pois a thread de alta prioridade permanece executando e alterando o mutex.

### S2D5Q224 — Deadlock, starvation e livelock têm causas e padrões de progresso distintos

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

Analise as situações.

I. T1 mantém A e espera B, enquanto T2 mantém B e espera A.
II. Um fluxo pronto nunca é escolhido, embora outros concluam normalmente.
III. Dois fluxos reagem um ao outro continuamente, mas não avançam.

As situações I, II e III correspondem, respectivamente, a

A) starvation, deadlock e condição de corrida.
B) livelock, inversão de prioridade e deadlock.
C) condição de corrida, livelock e starvation.
D) deadlock, starvation e livelock.

### S2D5Q225 — Locks devem proteger o menor estado coerente possível; retenção durante E/S amplia contenção e risco de dependências

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

Uma thread adquire um mutex, inicia uma operação de rede potencialmente longa e mantém o lock até receber a resposta. À luz das boas práticas de sincronização, essa decisão

A) é obrigatória, pois toda E/S deve ocorrer dentro de uma seção crítica, mesmo que não acesse o estado protegido.
B) elimina contenção, já que a thread bloqueada deixa de ser proprietária do mutex automaticamente.
C) transforma o mutex em semáforo contador e permite que outros participantes entrem na seção protegida.
D) pode ampliar a contenção e participar de ciclos de dependência; convém proteger apenas o menor estado coerente necessário.



### S2D5Q226 — FCFS e cálculo de espera e retorno

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

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

### S2D5Q227 — SJF não preemptivo e minimização da espera média sob hipóteses ideais

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

Três processos A, B e C chegam no instante zero com bursts de CPU iguais a 7, 4 e 1, respectivamente. Aplicando SJF não preemptivo, sem custo de troca, é correto afirmar que:

A) a ordem será A, B, C, pois SJF preserva a ordem de chegada quando todos chegam juntos.
B) a ordem será C, A, B, e a espera média será 8/3 unidades.
C) a ordem será C, B, A, e a espera média será 2 unidades.
D) a ordem será B, C, A, e a espera média será 3 unidades.

### S2D5Q228 — SRTF, preempção e tempo restante

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

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

### S2D5Q229 — Starvation em escalonamento por prioridade e aging

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [7. Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock), no parágrafo que define starvation e aging; e [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

Em um escalonador por prioridade, chegadas contínuas de tarefas mais prioritárias mantêm uma tarefa pronta de baixa prioridade sem CPU por tempo indefinido. Qual ajuste combate diretamente o fenômeno?

A) Elevar a prioridade inicial de cada nova tarefa de alta prioridade, para que ela conclua antes de ampliar a fila.

B) Aplicar aging, aumentando gradualmente a prioridade da tarefa pronta conforme cresce seu tempo de espera na fila.

C) Reduzir gradualmente a prioridade da tarefa que já esperou, reservando a CPU aos fluxos que chegaram mais recentemente.

D) Manter prioridades estáticas e usar FCFS apenas para desempatar tarefas que já possuem exatamente o mesmo nível.

### S2D5Q230 — Round Robin, quantum, conclusão e resposta

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

Três processos chegam no instante zero, na ordem A, B e C, com bursts 5, 3 e 1. Em Round Robin com quantum 2 e custo de troca desprezado, assinale a alternativa correta.

A) A, B e C terminam nos instantes 5, 8 e 9, pois o quantum não altera a ordem de conclusão do FCFS.
B) C, B e A terminam nos instantes 5, 8 e 9; os tempos de resposta de A, B e C são 0, 2 e 4.
C) B, C e A terminam nos instantes 6, 7 e 9; o quantum não utilizado por C é transferido a A.
D) C, A e B terminam nos instantes 1, 6 e 9, pois o menor burst sempre recebe a CPU primeiro.

### S2D5Q231 — Compromisso entre responsividade e sobrecarga no Round Robin

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [2. Programa, processo e thread](semana_02_estudo.md#s2-d5-processo-thread) e [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

Sobre o tamanho do quantum no Round Robin, assinale a afirmativa correta.

A) Quantum muito pequeno tende a elevar preempções e trocas de contexto; quantum muito grande aproxima o comportamento de FCFS.
B) Quantum muito pequeno elimina o custo de troca de contexto e transforma o algoritmo em SJF.
C) Quantum muito grande melhora necessariamente o primeiro atendimento de todas as tarefas interativas.
D) O tamanho do quantum não afeta tempo de resposta nem sobrecarga, apenas a prioridade estática.

### S2D5Q232 — Preempção nos algoritmos clássicos de CPU

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [8. Escalonamento de CPU — algoritmos clássicos](semana_02_estudo.md#s2-d5-escalonamento), na caracterização de FCFS, SJF, SRTF, prioridade e Round Robin.

Considerando as definições clássicas de FCFS, SJF, SRTF, escalonamento por prioridade e Round Robin, qual classificação quanto à preempção está correta?

A) FCFS e SJF são não preemptivos; SRTF também não preempta; prioridade sempre preempta; Round Robin troca somente em bloqueio.

B) FCFS preempta em cada chegada; SJF não preempta; SRTF preempta; prioridade é sempre não preemptiva; Round Robin usa quantum.

C) FCFS não preempta; SJF preempta por menor burst; SRTF não preempta; prioridade admite variantes; Round Robin não usa preempção.

D) FCFS e SJF são não preemptivos; SRTF preempta; prioridade admite ambas as variantes; Round Robin preempta ao fim do quantum.

### S2D5Q233 — Camadas de controle de dispositivos e papel do driver

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).

Em uma operação de entrada/saída, qual descrição distingue corretamente controlador e driver?

A) O driver é o circuito físico do dispositivo, e o controlador é um programa executado no espaço da aplicação.
B) O aplicativo precisa conhecer os registradores elétricos de cada dispositivo, pois o driver apenas define permissões de arquivo.
C) O controlador contém lógica e registradores do dispositivo; o driver traduz operações do sistema operacional, administra filas, buffers, erros e conclusão.
D) Driver e controlador são nomes equivalentes para o mecanismo que escalona processos na CPU.

### S2D5Q234 — Polling e seu custo operacional

**Nível:** Médio

**Uso:** Revisão

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — polling](semana_02_estudo.md#s2-d5-dispositivos-e-s), na definição da consulta repetida e no contraste entre espera curta e longa.

Um driver pode consultar um registrador de estado em laço até o dispositivo terminar. Em que situação e com qual custo esse polling é adequadamente caracterizado?

A) É consulta repetida, aceitável em espera curtíssima ou evento muito frequente, mas consome ciclos se a espera se prolongar.

B) É notificação iniciada pelo dispositivo, adequada a esperas longas porque a CPU permanece dormindo sem realizar consultas periódicas.

C) É transferência autônoma de blocos pelo controlador, adequada quando se quer dispensar a CPU de mover cada unidade de dados.

D) É espera necessariamente síncrona, incompatível com qualquer driver que também utilize interrupções em outras fases da operação.

### S2D5Q235 — Interrupção e desenho de rotina de serviço curta

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — interrupções](semana_02_estudo.md#s2-d5-dispositivos-e-s), no trecho sobre reconhecimento, estado mínimo, processamento diferido e retorno rápido da ISR.

Um dispositivo sinaliza por interrupção que uma operação terminou e há processamento demorado a realizar sobre o resultado. Qual desenho da ISR é o mais adequado em regra?

A) Manter a ISR até concluir todo o processamento, inclusive operações que possam dormir, e reconhecer o dispositivo somente ao final.

B) Retornar sem reconhecer a origem, deixando que novas interrupções repitam o sinal até uma thread comum consultar o dispositivo.

C) Copiar na ISR todo o bloco byte a byte, ainda que uma transferência DMA já tenha colocado os dados na memória.

D) Reconhecer o dispositivo, preservar o mínimo necessário, agendar o trabalho demorado em contexto apropriado e retornar rapidamente.

### S2D5Q236 — DMA e limites da expressão transferência direta

**Nível:** Médio

**Uso:** Revisão

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s), na sequência de configuração pela CPU, transferência do bloco e sinalização de conclusão.

A CPU configura origem, destino, tamanho e direção; depois, a controladora transfere um bloco entre dispositivo e memória e sinaliza o término. Qual mecanismo predomina?

A) E/S programada, porque fornecer os parâmetros significa que a CPU também moveu cada palavra do bloco entre os extremos.

B) DMA, porque a controladora move o bloco após a configuração da CPU, que ainda participa da preparação e da conclusão.

C) Polling, porque toda configuração inicial implica que a CPU consultou repetidamente o estado durante a transferência inteira.

D) E/S dirigida por interrupção sem DMA, porque o aviso final comprova que a CPU realizou cada unidade transferida.

### S2D5Q237 — Composição de polling, interrupção e DMA

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — comparação operacional](semana_02_estudo.md#s2-d5-dispositivos-e-s), especialmente a afirmação de que os três mecanismos não são mutuamente exclusivos.

Um driver prepara uma transferência em bloco, acompanha uma fase inicial e recebe aviso de conclusão. Qual relação entre polling, interrupção e DMA é tecnicamente válida?

A) Se o bloco usa DMA, a conclusão não pode gerar interrupção e precisa ser descoberta exclusivamente por polling.

B) A interrupção move o bloco para a memória, enquanto DMA serve somente para avisar à CPU que a operação terminou.

C) O driver pode configurar DMA, usar polling em alguma fase e receber interrupção ao final; os mecanismos podem coexistir.

D) Ao escolher polling em uma fase, o driver fica impedido de empregar DMA ou interrupção na mesma operação.

### S2D5Q238 — Abstrações de nome, metadados e abertura em sistemas de arquivos

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos), na lista que distingue diretório, inode ou equivalente, descritor/handle e montagem.

Ao resolver um caminho e abrir um arquivo, o sistema percorre estruturas persistentes e cria uma referência utilizável pelo processo. Qual associação entre as abstrações está correta?

A) Diretório relaciona nome a objeto; inode guarda metadados e referência ao conteúdo; descritor representa a abertura no processo.

B) Diretório guarda descritores por processo; inode relaciona nomes a objetos; descritor mantém os metadados persistentes do arquivo.

C) Diretório armazena apenas blocos de conteúdo; inode representa a abertura do processo; descritor relaciona o nome ao objeto.

D) Diretório copia o sistema montado; inode contém somente o texto do nome; descritor é referência global de todos os processos.

### S2D5Q239 — Commit e replay de transações do journal

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos).

Após uma queda de energia, o journal de um sistema de arquivos contém uma transação sem registro de commit válido. No replay, a conduta compatível com a teoria de journaling é:

A) considerar a transação confirmada apenas porque seus descritores foram gravados.
B) tratá-la como incompleta e descartá-la, enquanto transações confirmadas podem ser reproduzidas.
C) restaurar automaticamente uma cópia histórica de todos os arquivos alterados.
D) converter a transação em backup completo antes de montar o sistema de arquivos.

### S2D5Q240 — Modos de journaling do ext4

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos), especialmente as diferenças entre `data=ordered`, `data=journal` e `data=writeback`.

Considere as afirmações sobre os modos de journaling do ext4.

A) I e II, apenas.

B) I e III, apenas.

C) II e III, apenas.

D) I, II e III.

### S2D5Q241 — Journaling e recuperação de versão excluída

**Nível:** Médio

**Uso:** Simulado

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos), nos trechos que diferenciam recuperação de consistência e recuperação histórica por backup.

Um arquivo foi excluído legitimamente e a ausência só foi percebida dias depois. O volume permaneceu consistente e utiliza journaling. Qual conclusão é tecnicamente adequada?

A) O journal conserva todas as versões do arquivo e permite escolher qualquer estado anterior sem outra cópia.

B) A consistência do volume comprova que o conteúdo excluído continua recuperável no próprio sistema de arquivos.

C) O journal ajuda a recuperar consistência após falhas, mas recuperar versão anterior exige estratégia de backup.

D) A presença do journal implica replicação automática dos arquivos em uma mídia independente e histórica.

### S2D5Q242 — Conversão do modo Linux `750`

**Nível:** Médio

**Uso:** Simulado

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente a decomposição octal `r=4`, `w=2`, `x=1` e a ordem proprietário, grupo e outros.

Em um arquivo regular Linux, qual representação simbólica corresponde ao modo octal `750`, na ordem proprietário, grupo e outros?

A) proprietário `rwx`, grupo `r--`, outros `---`.

B) proprietário `rw-`, grupo `r-x`, outros `--x`.

C) proprietário `rwx`, grupo `rw-`, outros `---`.

D) proprietário `rwx`, grupo `r-x`, outros `---`.

### S2D5Q243 — Semântica de permissões em diretórios Linux

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), nos trechos sobre listagem por `r`, travessia por `x` e alteração de entradas com `w` e `x`.

Considere as afirmações sobre bits de permissão aplicados a um diretório Linux.

A) I e II, apenas.

B) I e III, apenas.

C) I, II e III.

D) II e III, apenas.

### S2D5Q244 — Comandos Linux para modo, proprietário e ACL

**Nível:** Médio

**Uso:** Simulado

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos) e [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente `chmod`, `chown`, `getfacl` e `setfacl`.

Um administrador precisa, nessa ordem, alterar os bits de modo de um arquivo existente, trocar seu proprietário e inspecionar sua ACL estendida. Qual sequência é adequada?

A) `umask`, `chgrp` e `setfacl`.

B) `chmod`, `chown` e `getfacl`.

C) `setfacl`, `chgrp` e `getfacl`.

D) `chattr`, `chown` e `setfacl`.

### S2D5Q245 — Permissões Linux e Windows em três camadas

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente a semântica de `rwx` em arquivo e diretório, DACL/ACE e combinação entre compartilhamento e NTFS.

Considere permissões em Linux e Windows.

I. Em um arquivo Linux com modo `750`, o grupo pode ler e executar, mas não gravar.

II. Em um diretório Linux com modo `640`, o grupo pode ler a lista de nomes, mas a ausência de `x` impede atravessar o caminho e acessar normalmente as entradas.

III. No acesso remoto do Windows, permissões de compartilhamento e NTFS podem atuar em conjunto; a DACL reúne ACEs aplicáveis e a permissão efetiva não é simplesmente a mais ampla.

Está correto o que se afirma em:

A) I, apenas.

B) II e III, apenas.

C) I, II e III.

D) I e III, apenas.

### S2D5Q246 — Finalidade do `icacls`

**Nível:** Médio

**Uso:** Simulado

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes) e [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), nos trechos sobre DACL e finalidade do `icacls`.

Um administrador Windows precisa exibir e modificar ACEs, herança e permissões de arquivos e diretórios. Qual utilitário atende diretamente a essa tarefa?

A) `attrib`, usado para exibir ou alterar atributos como oculto e somente leitura.

B) `takeown`, usado para assumir a propriedade de arquivo cujo acesso foi negado.

C) `icacls`, usado para exibir ou modificar ACEs, herança e permissões de acesso.

D) `cipher`, usado para administrar cifração EFS em arquivos e diretórios.

### S2D5Q247 — Observação pontual e contínua de processos Linux

**Nível:** Médio

**Uso:** Simulado

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), especialmente `ps -eLf` para observação pontual e `top` para atualização contínua.

Uma equipe precisa primeiro obter uma fotografia de processos e threads Linux e depois acompanhar continuamente o consumo por thread. Qual par de comandos é o mais pertinente?

A) `ps -eLf` para a fotografia e `top -H` para a visão dinâmica.

B) `pgrep -a` para a fotografia e `nice` para a visão dinâmica.

C) `pstree -p` para a fotografia e `renice` para a visão dinâmica.

D) `jobs -l` para a fotografia e `kill` para a visão dinâmica.

### S2D5Q248 — Consulta de serviços e logs em Linux e Windows

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), nos trechos sobre `systemctl`, `journalctl`, `Get-Service` e `Get-WinEvent`.

O analista precisa, nessa ordem, consultar o estado de um serviço Linux, seus eventos, o estado de um serviço Windows e eventos relacionados. Qual sequência usa ferramentas de observação adequadas?

A) `journalctl`; `systemctl status`; `Get-WinEvent`; `Get-Service`.

B) `systemctl status`; `journalctl`; `Get-Service`; `Get-WinEvent`.

C) `ps -ef`; `dmesg --follow`; `Get-Process`; `Get-Content C:\Logs\app.log`.

D) `systemctl restart`; `journalctl --vacuum`; `Restart-Service`; `Clear-EventLog`.

### S2D5Q249 — Endereços, rotas e sockets no Linux

**Nível:** Médio

**Uso:** Simulado

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), especialmente `ip addr`, `ip route` e `ss -tulpn`.

Em um diagnóstico Linux, é preciso verificar endereços das interfaces, tabela de rotas e sockets de escuta associados a processos. Qual conjunto atende diretamente às três consultas?

A) `ip -br link`, `ip neigh` e `ping`.

B) `dig`, `traceroute` e `tcpdump -n`.

C) `ethtool eth0`, `arp -n` e `nmap -sV localhost`.

D) `ip addr`, `ip route` e `ss -tulpn`.

### S2D5Q250 — Sequência de comandos administrativos no Windows

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos) e [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente `Get-Process`, `Get-Service`, `ipconfig`, `Get-NetTCPConnection` e `icacls`.

Em uma estação Windows, o analista deve, nessa ordem, listar processos, consultar serviços, exibir a configuração IP, examinar conexões TCP e verificar permissões NTFS. Qual sequência corresponde às finalidades?

A) `Get-Process`; `Get-Service`; `ipconfig`; `Get-NetTCPConnection`; `icacls`.

B) `Get-Service`; `Get-Process`; `ipconfig`; `Get-NetTCPConnection`; `icacls`.

C) `Get-Process`; `Get-Service`; `Get-NetAdapter`; `Test-NetConnection`; `takeown`.

D) `tasklist`; `sc.exe query`; `ipconfig`; `netstat -ano`; `attrib`.

## Gabarito do Dia 5

### Questões principais 1–25


| Questão | Resposta |
|---:|:---:|
| 1 | B |
| 2 | D |
| 3 | A |
| 4 | C |
| 5 | C |
| 6 | B |
| 7 | B |
| 8 | C |
| 9 | D |
| 10 | A |
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
| 22 | A |
| 23 | B |
| 24 | D |
| 25 | D |



### Questões principais 26–50


| Questão | Gabarito |
|---:|:---:|
| 26 | B |
| 27 | C |
| 28 | A |
| 29 | B |
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
| 42 | D |
| 43 | C |
| 44 | B |
| 45 | C |
| 46 | C |
| 47 | A |
| 48 | B |
| 49 | D |
| 50 | A |

### Gabarito das questões extras

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
| 5.12 | D |
| 5.13 | C |
| 5.14 | A |
| 5.15 | A |
| 5.16 | B |
| 5.17 | C |
| 5.18 | B |
| 5.19 | D |
| 5.20 | B |


## Comentários do Dia 5


### Comentário S2D5Q201

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D5Q202

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D5Q203

**Nível:** Médio

**Uso:** Essenciais
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

### Comentário S2D5Q204

**Nível:** Difícil

**Uso:** Essenciais
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

### Comentário S2D5Q205

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** as threads não formam espera circular nem permanecem bloqueadas; ambas chegam a executar a gravação.
- **B)** nenhuma thread é adiada indefinidamente pelo escalonador, pois as duas executam e concluem seus passos.
- **C)** as duas operações usam a mesma leitura inicial, e a segunda gravação substitui um resultado igual sem incorporar os dois incrementos.
- **D)** não há repetição ativa sem progresso; ocorre uma única intercalação que produz valor final incorreto.

**Conceito:** dependência do resultado em uma ordem concorrente não controlada e perda de atualização em read-modify-write.

**Pegadinha:** chamar toda falha de concorrência de deadlock, starvation ou livelock sem verificar bloqueio, adiamento ou repetição.

**Como pensar:** decomponha a expressão em três ações e intercale T1 e T2; se ambas calculam a partir de 40, só um incremento aparece no resultado.

**Referência:** [Seção crítica, condição de corrida e atomicidade](semana_02_estudo.md#s2-d5-corrida-atomicidade), no exemplo que decompõe atualização em leitura, cálculo e escrita e identifica a atualização perdida.

### Comentário S2D5Q206

**Nível:** Difícil

**Uso:** Essenciais
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

### Comentário S2D5Q207

**Nível:** Médio

**Uso:** Essenciais
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Um acesso que ignora o mutex não é automaticamente bloqueado pelo sistema operacional.
- **B)** Correta. O mutex ordena os participantes que cooperam usando o mesmo protocolo para o estado protegido.
- **C)** Incorreta. A proteção não se estende magicamente a operações alheias ao mutex.
- **D)** Incorreta. No uso convencional, mutex expressa propriedade: quem adquire deve liberar.

**Conceito:** mutex implementa exclusão mútua cooperativa e propriedade exclusiva do lock.

**Pegadinha:** imaginar que a existência do objeto mutex protege a memória mesmo quando parte do código não o utiliza.

**Como pensar:** associe cada invariante compartilhada a um lock e confira se todos os caminhos de acesso obedecem ao mesmo acordo.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

### Comentário S2D5Q208

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** um contador restrito a zero e um representa apenas uma permissão, não as oito unidades disponíveis.
- **B)** mutex expressa propriedade exclusiva e, no modelo convencional, não possui oito proprietários simultâneos.
- **C)** o valor do semáforo acompanha o número de conexões livres, bloqueando nova aquisição quando as oito estiverem ocupadas.
- **D)** variável de condição coordena espera por um predicado, mas não mantém sozinha o estado permanente de oito permissões.

**Conceito:** uso de semáforo contador para controlar N instâncias equivalentes de um recurso.

**Pegadinha:** escolher uma primitiva que também bloqueia threads, mas não modela a cardinalidade nem a propriedade exigida.

**Como pensar:** conte as permissões simultâneas: uma unidade exclusiva sugere mutex; oito unidades intercambiáveis sugerem contador inicializado em oito.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição — semáforo binário e contador](semana_02_estudo.md#s2-d5-sincronizacao), no trecho que relaciona o contador a N unidades do recurso.

### Comentário S2D5Q209

**Nível:** Difícil

**Uso:** Essenciais
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

### Comentário S2D5Q210

**Nível:** Difícil

**Uso:** Essenciais
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Quando a espera será curtíssima, girar pode custar menos que dormir e despertar; se ela se prolonga, o custo cresce.
- **B)** Incorreta. Espera ativa consome ciclos e é inadequada para latências longas de E/S.
- **C)** Incorreta. Dormir é justamente o oposto do comportamento de um spinlock, que testa repetidamente.
- **D)** Incorreta. Em um núcleo não preemptível, girar pode impedir que o detentor execute e libere o lock.

**Conceito:** spinlock usa espera ativa e depende de uma expectativa de retenção muito curta.

**Pegadinha:** confundir ausência de troca de contexto com ausência de custo.

**Como pensar:** compare o tempo previsto do lock com o custo de suspensão e considere se o detentor pode executar em outro núcleo.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição — spinlock](semana_02_estudo.md#s2-d5-sincronizacao).

### Comentário S2D5Q211

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D5Q212

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D5Q213

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** adiamento indefinido de um participante enquanto outros progridem caracteriza starvation.
- **B)** atividade contínua sem progresso útil caracteriza livelock, não o bloqueio conjunto do deadlock.
- **C)** uma E/S demorada que segue avançando constitui espera normal por evento externo.
- **D)** o conjunto está fechado em dependências recíprocas, e quem poderia liberar cada recurso também não consegue avançar.

**Conceito:** deadlock como estado de impasse de um conjunto, e não como qualquer espera ou falta de progresso.

**Pegadinha:** confundir deadlock com starvation, livelock ou bloqueio temporário por operação externa ainda ativa.

**Como pensar:** pergunte se existe alguém fora do conjunto capaz de produzir o evento esperado; se toda liberação depende de outro bloqueado interno, há impasse.

**Referência:** [Deadlock](semana_02_estudo.md#s2-d5-deadlock), no parágrafo inicial que define o conjunto bloqueado por dependências internas de recursos ou eventos.

### Comentário S2D5Q214

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** a condição canônica é não preempção; retirada compulsória possível rompe uma das bases do impasse clássico.
- **B)** recursos exclusivos, manutenção de um recurso enquanto outro é solicitado, ausência de retirada compulsória e ciclo de espera compõem a lista.
- **C)** espera acíclica é justamente o oposto da espera circular necessária ao conjunto de Coffman.
- **D)** liberação antecipada evita que o processo conserve um recurso enquanto espera outro e, portanto, não substitui posse e espera.

**Conceito:** identificação exata das quatro condições necessárias de Coffman.

**Pegadinha:** trocar apenas um termo da lista por sua negação ou por uma política que rompe a condição correspondente.

**Como pensar:** reconstrua a cena: recurso exclusivo, alguém o possui e pede outro, ninguém o retira e as dependências fecham um ciclo.

**Referência:** [Deadlock — as quatro condições necessárias de Coffman](semana_02_estudo.md#s2-d5-deadlock), na lista numerada das condições e em sua aplicação conjunta.

### Comentário S2D5Q215

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D5Q216

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D5Q217

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** estados seguros podem possuir recursos alocados, e insegurança não equivale necessariamente à existência de ciclo bloqueado.
- **B)** os processos podem concluir em sequência, reutilizando recursos liberados, sem que todas as demandas sejam atendidas ao mesmo tempo.
- **C)** um primeiro processo concluível não basta se suas liberações não permitirem completar os demais, e insegurança não significa indisponibilidade permanente.
- **D)** basta existir ao menos uma ordem viável para todos terminarem; perder essa ordem garantida aumenta o risco, mas não comprova impasse consumado.

**Conceito:** sequência segura e diferença entre estado inseguro e deadlock já existente.

**Pegadinha:** exigir conclusão simultânea ou tratar a perda de garantia preventiva como diagnóstico de impasse atual.

**Como pensar:** simule liberações sucessivas: escolha quem pode terminar, devolva seus recursos e repita até todos concluírem; uma ordem completa torna o estado seguro.

**Referência:** [Deadlock — evitação](semana_02_estudo.md#s2-d5-deadlock), na definição de sequência segura e na ressalva de que estado inseguro não significa deadlock já ocorrido.

### Comentário S2D5Q218

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D5Q219

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** no caso de instância única o ciclo fecha a dependência sem saída; com múltiplas, outra unidade disponível pode permitir conclusão e desfazer o ciclo.
- **B)** inverte a suficiência; ela vale no modelo de instância única e deixa de valer para o ciclo isolado no modelo múltiplo.
- **C)** disponibilidade e quantidade de instâncias são decisivas quando um mesmo tipo de recurso possui mais de uma unidade.
- **D)** ausência de ciclo afasta o impasse representado no caso simples, e um bloqueio isolado pode ser espera normal.

**Conceito:** condição de suficiência do ciclo conforme a cardinalidade dos recursos.

**Pegadinha:** transportar a regra correta do grafo de instância única sem verificar se existem unidades adicionais do recurso.

**Como pensar:** antes de concluir pelo ciclo, pergunte se outra instância livre pode permitir que um participante termine e libere as demais.

**Referência:** [Deadlock — detecção](semana_02_estudo.md#s2-d5-deadlock), no contraste entre grafo com instância única e análise de disponíveis, alocados e pedidos quando há múltiplas instâncias.

### Comentário S2D5Q220

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D5Q221

**Nível:** Médio

**Uso:** Aprofundamento
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

### Comentário S2D5Q222

**Nível:** Médio

**Uso:** Aprofundamento
**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Há mudanças de estado e tentativas contínuas, porém nenhuma produz progresso útil; o backoff dessincroniza novas tentativas.
- **B)** Incorreta. O enunciado mostra as duas threads ativas, não uma delas indefinidamente preterida.
- **C)** Incorreta. No deadlock, os participantes permanecem bloqueados; aqui eles agem e reagem repetidamente.
- **D)** Incorreta. Paralelismo descreve simultaneidade, não falha de progresso, e programa passivo não soluciona o protocolo.

**Conceito:** livelock é atividade contínua sem avanço útil, muitas vezes produzida por respostas simétricas.

**Pegadinha:** tomar qualquer ausência de conclusão por bloqueio de deadlock.

**Como pensar:** observe se os estados ainda mudam; se há movimento sem aproximação da conclusão, pense em livelock.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

### Comentário S2D5Q223

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A baixa sofre preempções, mas o fenômeno central é a alta depender dela enquanto intermediárias interferem; quantum geral não é solução necessária.
- **B)** Correta. A prioridade efetiva fica invertida pela dependência do lock; herança permite que a detentora execute e o libere mais cedo.
- **C)** Incorreta. Não foram demonstradas espera circular nem todas as condições de Coffman.
- **D)** Incorreta. A alta está bloqueada pelo mutex, e não ativa alterando estados sem progresso.

**Conceito:** inversão de prioridade é a espera indireta de uma thread alta por uma baixa que mantém recurso necessário.

**Pegadinha:** acreditar que a política de prioridade resolve a espera, embora a baixa precise executar para liberar o lock.

**Como pensar:** siga a dependência real: a alta depende da baixa; logo, elevar temporariamente a baixa ajuda a alta.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

### Comentário S2D5Q224

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A situação I contém espera circular, e a III envolve atividade, não simples corrida por resultado.
- **B)** Incorreta. I não apresenta atividade contínua; II não informa uma dependência de prioridades por lock.
- **C)** Incorreta. I descreve dependência de locks, II não tem reações ativas e III não é mero preterimento.
- **D)** Correta. I é impasse circular, II é adiamento indefinido individual e III é atividade recíproca sem avanço.

**Conceito:** deadlock, starvation e livelock têm causas e padrões de progresso distintos.

**Pegadinha:** usar “não terminou” como critério único e ignorar se os fluxos estão bloqueados, preteridos ou ativos.

**Como pensar:** classifique pelo movimento: ciclo bloqueado é deadlock; um apto esquecido é starvation; atividade inútil é livelock.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

### Comentário S2D5Q225

**Nível:** Difícil

**Uso:** Aprofundamento
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


### Comentário S2D5Q226

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D5Q227

**Nível:** Difícil

**Uso:** Aprofundamento
**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Com todos disponíveis no instante zero, SJF escolhe o menor próximo burst, não a ordem nominal A, B, C.
- **B)** Incorreta. Depois de C, o burst de B é menor que o de A; logo, C, A, B não é a ordem SJF.
- **C)** Correta. A execução é C de 0 a 1, B de 1 a 5 e A de 5 a 12. As esperas são 0, 1 e 5; a média é 2.
- **D)** Incorreta. Escolher B antes de C viola o critério de menor burst entre os processos prontos.

**Conceito:** SJF não preemptivo e minimização da espera média sob hipóteses ideais.

**Pegadinha:** tratar chegada simultânea como obrigação de FCFS ou calcular espera pela posição sem considerar a duração dos anteriores.

**Como pensar:** ordene os bursts disponíveis do menor para o maior e some, para cada processo, o tempo consumido pelos que o antecedem.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário S2D5Q228

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D5Q229

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** favorecer ainda mais as novas tarefas prioritárias mantém ou agrava o adiamento da tarefa já prejudicada.
- **B)** aging faz o tempo de espera influenciar a prioridade e cria uma oportunidade crescente de escalonamento para a tarefa adiada.
- **C)** reduzir a prioridade de quem espera reforça a preferência que originou o starvation.
- **D)** desempate somente dentro do mesmo nível não ajuda uma tarefa que permanece abaixo das chegadas sucessivas.

**Conceito:** starvation por prioridade e sua mitigação direta mediante aging.

**Pegadinha:** propor ajustes que melhoram a vazão das tarefas já favorecidas sem alterar a chance de quem espera indefinidamente.

**Como pensar:** identifique quem continua pronto enquanto outros progridem e procure uma política que aumente sua preferência à medida que o tempo passa.

**Referência:** [7. Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock), no parágrafo que define starvation e aging; e [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

### Comentário S2D5Q230

**Nível:** Difícil

**Uso:** Aprofundamento
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

### Comentário S2D5Q231

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D5Q232

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** SRTF é a versão preemptiva do SJF, prioridade não possui apenas uma variante e Round Robin preempta pelo quantum.
- **B)** FCFS clássico não preempta por nova chegada, e escalonamento por prioridade pode ser preemptivo ou não.
- **C)** SJF clássico não preempta, SRTF preempta quando surge menor tempo restante e Round Robin utiliza preempção periódica.
- **D)** a alternativa preserva as duas políticas clássicas não preemptivas, a versão preemptiva por menor restante, as variantes de prioridade e a fatia do RR.

**Conceito:** classificação completa dos principais algoritmos quanto à retirada da CPU.

**Pegadinha:** acertar parte da lista e errar justamente um algoritmo de nome semelhante, como SJF versus SRTF.

**Como pensar:** associe cada retirada a seu gatilho: menor restante no SRTF, fim do quantum no RR e chegada prioritária somente na variante preemptiva de prioridade.

**Referência:** [8. Escalonamento de CPU — algoritmos clássicos](semana_02_estudo.md#s2-d5-escalonamento), na caracterização de FCFS, SJF, SRTF, prioridade e Round Robin.

### Comentário S2D5Q233

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D5Q234

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** polling mantém CPU ou driver verificando o estado e pode ser eficiente apenas quando o custo esperado da espera ativa é pequeno.
- **B)** sinal iniciado pelo dispositivo e suspensão da CPU descrevem a lógica de interrupção, não de polling.
- **C)** movimentação de bloco com menor intervenção por unidade descreve DMA, embora um driver possa combinar os mecanismos.
- **D)** polling não determina sozinho sincronia da E/S e pode coexistir com interrupção no mesmo driver ou em fases diferentes.

**Conceito:** iniciativa da consulta no polling e custo da espera ativa conforme sua duração.

**Pegadinha:** definir polling pelas propriedades de interrupção ou DMA ou transformá-lo em escolha exclusiva de arquitetura.

**Como pensar:** pergunte quem verifica o término e quantos ciclos são gastos: no polling, a CPU pergunta repetidamente; quanto maior a demora, maior o desperdício.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — polling](semana_02_estudo.md#s2-d5-dispositivos-e-s), na definição da consulta repetida e no contraste entre espera curta e longa.

### Comentário S2D5Q235

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** trabalho extenso ou bloqueante dentro da ISR aumenta latência e pode impedir o atendimento tempestivo de outros eventos.
- **B)** não reconhecer a fonte pode causar nova sinalização contínua e não constitui protocolo adequado de tratamento.
- **C)** se DMA transferiu o bloco, a ISR trata a conclusão; não precisa repetir a cópia de cada byte.
- **D)** a parte urgente e mínima fica na ISR, enquanto o processamento pesado é diferido para ambiente onde possa executar com segurança.

**Conceito:** divisão entre resposta imediata ao hardware e trabalho posterior no tratamento de interrupções.

**Pegadinha:** confundir “tratar a interrupção” com realizar toda a operação e todo o processamento dentro da ISR.

**Como pensar:** separe o que precisa cessar/registrar o evento agora do que pode ser agendado; a ISR deve liberar rapidamente o caminho de interrupções.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — interrupções](semana_02_estudo.md#s2-d5-dispositivos-e-s), no trecho sobre reconhecimento, estado mínimo, processamento diferido e retorno rápido da ISR.

### Comentário S2D5Q236

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** configurar descritores não significa que a CPU execute a movimentação de cada unidade de dados.
- **B)** a característica decisiva é a transferência em bloco feita pelo mecanismo/controladora, com menor participação da CPU por palavra.
- **C)** polling exige consultas repetidas ao estado; uma configuração inicial não demonstra que isso ocorreu durante toda a cópia.
- **D)** uma interrupção pode apenas anunciar que o DMA terminou e não prova transferência palavra a palavra pela CPU.

**Conceito:** divisão de responsabilidades entre configuração/conclusão pela CPU e transferência em bloco por DMA.

**Pegadinha:** interpretar “direta” como ausência total de CPU ou tomar a interrupção de término como mecanismo que moveu os dados.

**Como pensar:** identifique quem percorre o bloco: se a controladora faz a cópia depois de receber parâmetros, trata-se de DMA mesmo com CPU no início e no fim.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s), na sequência de configuração pela CPU, transferência do bloco e sinalização de conclusão.

### Comentário S2D5Q237

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** uma interrupção é forma comum de anunciar justamente a conclusão de uma transferência DMA.
- **B)** DMA move os dados; interrupção transfere o controle à rotina de tratamento para sinalizar ou processar o evento.
- **C)** os mecanismos possuem funções diferentes e podem compor fases da mesma operação conforme o desenho do driver.
- **D)** consultar estado em certo momento não proíbe utilizar transferência DMA e notificação por interrupção em outros momentos.

**Conceito:** composição funcional, em vez de exclusão, entre polling, interrupção e DMA.

**Pegadinha:** tratar tecnologias vizinhas como modos globais incompatíveis ou trocar os verbos “consultar”, “avisar” e “transferir”.

**Como pensar:** atribua uma função a cada mecanismo: polling consulta, interrupção avisa, DMA transfere; funções distintas podem integrar um único fluxo.

**Referência:** [9. Dispositivos, drivers, interrupções, polling e DMA — comparação operacional](semana_02_estudo.md#s2-d5-dispositivos-e-s), especialmente a afirmação de que os três mecanismos não são mutuamente exclusivos.

### Comentário S2D5Q238

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** o namespace associa o nome ao objeto, a estrutura persistente descreve o arquivo e a abertura fornece ao processo uma referência operacional.
- **B)** diretório não armazena a tabela privada de descritores, e inode não é a relação textual de nomes mantida pelo diretório.
- **C)** diretório organiza nomes, inode persiste metadados/referências e descritor é a referência da abertura, não o vínculo do nome.
- **D)** montagem associa namespaces sem copiar todo o conteúdo, inode não se reduz ao nome e descritores pertencem a contextos de processo.

**Conceito:** separação entre nome no diretório, metadados/referência persistente no inode e estado aberto no descritor.

**Pegadinha:** fundir três abstrações que aparecem na mesma operação de abertura ou trocar a persistente pela referência de processo.

**Como pensar:** percorra três etapas: localizar pelo nome, obter o objeto persistente e criar uma referência aberta para aquele processo.

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos), na lista que distingue diretório, inode ou equivalente, descritor/handle e montagem.

### Comentário S2D5Q239

**Nível:** Difícil

**Uso:** Revisão
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

### Comentário S2D5Q240

**Nível:** Difícil

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** I e II são verdadeiras, mas III também descreve corretamente a ordenação mais fraca de `data=writeback`.
- **B)** I e III são verdadeiras, mas II também é; `data=ordered` ordena os dados associados antes do commit dos metadados.
- **C)** II e III são verdadeiras, mas I também é; `data=journal` registra dados e metadados no journal.
- **D)** as três afirmações distinguem o conteúdo registrado e a ordem de escrita de cada modo.

**Conceito:** diferenças entre `data=ordered`, `data=journal` e `data=writeback` no ext4.

**Pegadinha:** interpretar “ordered” como registro de todos os dados no journal ou atribuir a `writeback` a ordenação mais forte.

**Como pensar:** avalie separadamente o que entra no journal e quando os dados chegam ao destino principal em relação ao commit.

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos), especialmente as diferenças entre `data=ordered`, `data=journal` e `data=writeback`.

### Comentário S2D5Q241

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** journal registra operações para consistência e não funciona necessariamente como repositório de todas as versões anteriores.
- **B)** estrutura consistente pode refletir corretamente uma exclusão válida, sem preservar o conteúdo que o usuário deseja recuperar.
- **C)** journaling auxilia o retorno estrutural após falha, enquanto versão histórica depende de cópia retida por uma estratégia de backup.
- **D)** journaling no volume não cria, por si só, outra mídia nem histórico independente dos arquivos.

**Conceito:** diferença entre journaling e backup.

**Pegadinha:** confundir consistência do sistema de arquivos com preservação do estado histórico desejado.

**Como pensar:** pergunte se o objetivo é corrigir estruturas após uma queda ou recuperar dados de outro momento; o segundo exige backup.

**Referência:** [10. Sistemas de arquivos e journaling](semana_02_estudo.md#s2-d5-sistemas-arquivos), nos trechos que diferenciam recuperação de consistência e recuperação histórica por backup.

### Comentário S2D5Q242

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** `r--` para o grupo vale 4 e omite a execução representada pelo valor 1 de `5`.
- **B)** `rw-` vale 6 e `--x` vale 1, portanto a sequência descrita não corresponde a `750`.
- **C)** `rw-` para o grupo vale 6, enquanto o segundo algarismo do modo é 5.
- **D)** `7=4+2+1` produz `rwx`, `5=4+1` produz `r-x` e `0` não concede bits.

**Conceito:** notação octal e simbólica das permissões de arquivo no Linux.

**Pegadinha:** trocar um bit dentro da tríade ou perder a ordem proprietário, grupo e outros.

**Como pensar:** decomponha cada algarismo separadamente com 4, 2 e 1 e só então escreva sua tríade simbólica.

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente a decomposição octal `r=4`, `w=2`, `x=1` e a ordem proprietário, grupo e outros.

### Comentário S2D5Q243

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** I e II são verdadeiras, mas III também descreve a combinação normalmente necessária para alterar entradas.
- **B)** I e III são verdadeiras, mas II também é; execução em diretório representa travessia ou pesquisa.
- **C)** as três afirmações distinguem listagem, travessia e modificação de entradas no diretório.
- **D)** II e III são verdadeiras, mas I também é; leitura se relaciona à listagem dos nomes.

**Conceito:** semântica de `r`, `w` e `x` em diretórios Linux.

**Pegadinha:** transportar sem adaptação a semântica dos mesmos bits em arquivos regulares.

**Como pensar:** associe `r` a ver nomes, `x` a percorrer o caminho e `w+x` a modificar a relação de entradas.

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), nos trechos sobre listagem por `r`, travessia por `x` e alteração de entradas com `w` e `x`.

### Comentário S2D5Q244

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** `umask` influencia permissões iniciais, `chgrp` troca o grupo e `setfacl` modifica, em vez de apenas inspecionar, a ACL.
- **B)** `chmod` altera bits de modo, `chown` troca o proprietário e `getfacl` exibe a ACL estendida.
- **C)** `setfacl` altera ACL em vez dos bits básicos solicitados, e `chgrp` troca grupo, não proprietário.
- **D)** `chattr` trata atributos especiais, e `setfacl` modifica a ACL em vez de cumprir a inspeção pedida.

**Conceito:** comandos Linux relacionados a permissões, titularidade e ACLs.

**Pegadinha:** escolher ferramentas da mesma área administrativa, mas trocar o objeto ou o sentido de consulta e alteração.

**Como pensar:** associe literalmente mode a `chmod`, owner a `chown` e consulta de ACL a `getfacl`.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos) e [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente `chmod`, `chown`, `getfacl` e `setfacl`.

### Comentário S2D5Q245

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** I é verdadeira, mas II e III também são; os bits mudam de efeito operacional em diretórios, e o acesso remoto do Windows atravessa mais de uma camada de autorização.
- **B)** II e III são verdadeiras, mas I também é; o algarismo `5` representa `r-x`, sem permissão de gravação para o grupo.
- **C)** as três afirmações aplicam corretamente a tríade em dois tipos de objeto Linux e a composição de autorização no Windows.
- **D)** I e III são verdadeiras, mas II também é; `r` permite listar nomes, enquanto a falta de `x` impede a travessia normal do diretório.

**Conceito:** diferenças da tríade `rwx` por tipo de objeto e composição de DACL, compartilhamento e NTFS.

**Pegadinha:** transportar a semântica de arquivo para diretório ou tratar a permissão mais ampla do Windows como resultado automático.

**Como pensar:** identifique primeiro o objeto Linux e a tríade da classe aplicável; depois, no Windows, confira todas as camadas de autorização atravessadas.

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente a semântica de `rwx` em arquivo e diretório, DACL/ACE e combinação entre compartilhamento e NTFS.
### Comentário S2D5Q246

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** `attrib` trata atributos de arquivo e não administra as ACEs que compõem a lista de controle de acesso.
- **B)** `takeown` altera a propriedade para recuperar controle, mas não é a ferramenta geral de edição da DACL.
- **C)** `icacls` exibe e modifica permissões, ACEs e propriedades de herança em arquivos e diretórios.
- **D)** `cipher` administra EFS e não substitui o utilitário de permissões e herança.

**Conceito:** finalidade do comando `icacls` no Windows.

**Pegadinha:** confundir ferramentas próximas de administração de arquivos que atuam em atributos, propriedade, cifra e controle de acesso.

**Como pensar:** identifique qual estrutura deve mudar; para ACL e ACE, procure o utilitário cujo nome contém `acls`.

**Referência:** [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes) e [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), nos trechos sobre DACL e finalidade do `icacls`.

### Comentário S2D5Q247

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** `ps -eLf` produz uma fotografia que inclui threads, e `top -H` atualiza a observação por thread continuamente.
- **B)** `pgrep` localiza processos por critérios, enquanto `nice` inicia processo com prioridade ajustada e não cria visão dinâmica.
- **C)** `pstree` mostra hierarquia, mas `renice` altera prioridade de processo existente em vez de monitorar consumo.
- **D)** `jobs` limita-se aos trabalhos do shell atual, e `kill` envia sinais em vez de acompanhar recursos.

**Conceito:** ferramentas Linux para fotografia e acompanhamento contínuo de processos e threads.

**Pegadinha:** escolher comandos relacionados a processos que alteram prioridade ou estado em vez de observar continuamente.

**Como pensar:** associe `ps` a process snapshot e `top` à tela atualizada; depois confirme a opção de exibir threads.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), especialmente `ps -eLf` para observação pontual e `top` para atualização contínua.

### Comentário S2D5Q248

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** todas são ferramentas de consulta, mas a sequência troca serviço e eventos em ambas as plataformas.
- **B)** `systemctl status` e `Get-Service` consultam serviços; `journalctl` e `Get-WinEvent` consultam eventos nas plataformas correspondentes.
- **C)** os comandos mostram processos, mensagens do kernel ou conteúdo genérico, sem cumprir a associação pedida para serviços e eventos.
- **D)** os quatro comandos alteram estado, retenção ou conteúdo, contrariando a necessidade de mera observação.

**Conceito:** comandos de consulta de serviços e logs em Linux e Windows.

**Pegadinha:** inverter a ordem de ferramentas corretas ou aceitar comandos de alteração quando o pedido é somente observar.

**Como pensar:** monte duas colunas, serviço e log, e preencha cada uma primeiro para Linux e depois para Windows.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), nos trechos sobre `systemctl`, `journalctl`, `Get-Service` e `Get-WinEvent`.

### Comentário S2D5Q249

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** os comandos tratam estado de enlace, vizinhança e alcançabilidade, mas não entregam as três consultas solicitadas.
- **B)** o conjunto consulta DNS, caminho e captura de pacotes, não a configuração local completa e os sockets por processo.
- **C)** o conjunto aborda interface física, cache ARP e varredura, sem substituir as três visões locais pedidas.
- **D)** `ip addr` mostra endereços, `ip route` mostra rotas e `ss -tulpn` relaciona sockets de escuta a protocolos e processos.

**Conceito:** comandos Linux para configuração IP, rotas e sockets de rede.

**Pegadinha:** escolher ferramentas legítimas de rede que respondem a perguntas operacionais diferentes.

**Como pensar:** transforme cada substantivo em uma consulta: endereço com `ip addr`, rota com `ip route` e socket com `ss`.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), especialmente `ip addr`, `ip route` e `ss -tulpn`.

### Comentário S2D5Q250

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** a sequência associa cada consulta ao utilitário correspondente e termina com a ferramenta de permissões NTFS.
- **B)** os utilitários são pertinentes, mas os dois primeiros estão invertidos em relação a processos e serviços.
- **C)** `Get-NetAdapter` não exibe sozinho toda a configuração pedida, `Test-NetConnection` testa conectividade e `takeown` altera propriedade.
- **D)** os quatro primeiros podem apoiar as respectivas consultas, mas `attrib` trata atributos e não verifica a DACL NTFS.

**Conceito:** associação entre finalidades administrativas e comandos Windows.

**Pegadinha:** trocar a ordem de comandos corretos ou confundir adaptação, teste, propriedade e atributos com as consultas solicitadas.

**Como pensar:** associe, na ordem, processo, serviço, IP, conexão e ACL; depois descarte qualquer ferramenta que altere objeto diferente.

**Referência:** [12. Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos) e [11. Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente `Get-Process`, `Get-Service`, `ipconfig`, `Get-NetTCPConnection` e `icacls`.

## Questões extras de revisão fixa do Dia 5

#### Extra Dia 5.1

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** delimitação normativa e controle de versão.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Escopo e controle de versão](semana_02_estudo.md#s2-d5-rf-escopo), especialmente o núcleo de quatro fontes e a substituição da RN nº 640/2024 pela RN nº 671/2025.

Ao revisar as fontes que podem fundamentar as questões extras de Legislação CRA/CFA, a equipe deve aplicar o recorte do cargo após a Retificação I. Assinale o conjunto correto.

A) Lei nº 4.769/1965, Decreto nº 61.934/1967, Regimento/RN nº 651/2024 e Código/RN nº 640/2024, mantido pela Retificação I.

B) Lei nº 4.769/1965, RNs nº 589/2020, nº 649/2024 e nº 670/2025 e Lei nº 12.514/2011, todas como núcleo material das extras.

C) Lei nº 4.769/1965, Decreto nº 61.934/1967, Regimento/RN nº 651/2024 e Código/RN nº 671/2025, conforme a Retificação I.

D) Lei nº 4.769/1965, Decreto nº 61.934/1967, Regimento/RN nº 671/2025 e Código/RN nº 651/2024, com as funções normativas invertidas.

#### Extra Dia 5.2

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** natureza e jurisdição do CRA-PR.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), nos arts. 1º e 2º resumidos na seção.

Um relatório institucional precisa registrar, sem transformar autonomia em soberania, a natureza jurídica, a sede e a jurisdição do CRA-PR. Assinale a redação correta.

A) É autarquia de direito público, com autonomia técnica, administrativa e financeira, sede na capital e jurisdição no Paraná nas matérias de sua competência.

B) É autarquia de direito privado, com autonomia apenas administrativa, sede na capital e jurisdição nacional para editar diretrizes destinadas a todos os CRAs.

C) É órgão da Administração Direta estadual, com autonomia técnica e financeira, sede na capital e jurisdição restrita aos serviços prestados pelo governo paranaense.

D) É autarquia de direito público, com autonomia técnica, administrativa e financeira, sede na capital e independência para afastar diretrizes nacionais do CFA.

#### Extra Dia 5.3

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** órgãos do CRA-PR.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), no resumo do art. 3º.

Para montar o organograma regimental, a equipe deve usar apenas as categorias enumeradas no art. 3º do Regimento do CRA-PR. Assinale a lista integralmente compatível.

A) Plenário; Diretoria Executiva; Presidência; Ouvidoria; Comissões Permanentes, Especiais e Grupos de Trabalho.

B) Plenário; Diretoria Executiva; Ouvidoria; Conselheiros efetivos e suplentes; Órgãos de Representação.

C) Plenário; Diretoria Executiva; Ouvidoria; setores administrativos; Comissões Permanentes e Especiais.

D) Plenário; Diretoria Executiva; Ouvidoria; Comissões Permanentes, Especiais e Grupos de Trabalho; Órgãos de Representação.

#### Extra Dia 5.4

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** finalidade do Plenário.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), especialmente o art. 4º e a diferença entre primeira e última instância.

Ao classificar o Plenário no desenho institucional do CRA-PR, qual descrição preserva simultaneamente sua posição e sua função de julgamento?

A) Órgão consultivo da Diretoria, sem competência deliberativa e sem atuação no julgamento de processos regionais.

B) Órgão colegiado de deliberação superior e primeira instância de julgamento no âmbito da jurisdição regional.

C) Órgão executivo responsável pela administração cotidiana e pela execução isolada de todas as decisões do Conselho.

D) Órgão recursal nacional encarregado da revisão final dos processos julgados por todos os Conselhos Regionais.

#### Extra Dia 5.5

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** composição e mandato do Plenário.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), nos resumos dos arts. 5º e 6º.

Assinale a alternativa que combina corretamente composição, forma de renovação e duração do mandato dos Conselheiros do CRA-PR.

A) Nove Conselheiros Efetivos e respectivos Suplentes; renovação bienal alternada em um terço e dois terços; mandato de dois anos, permitida uma reeleição.

B) Nove Conselheiros Efetivos, sem respectivos Suplentes; renovação bienal alternada em um terço e dois terços; mandato de quatro anos, permitida uma reeleição.

C) Nove Conselheiros Efetivos e respectivos Suplentes; renovação bienal alternada em um terço e dois terços; mandato de quatro anos, permitida uma reeleição.

D) Nove Conselheiros Efetivos e respectivos Suplentes; renovação integral ao fim de quatro anos; mandato de quatro anos, permitidas reeleições ilimitadas.

#### Extra Dia 5.6

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** competências do Plenário.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), no rol resumido do art. 8º.

Os conjuntos abaixo reúnem atos regimentais atribuídos predominantemente a uma estrutura do CRA-PR. Qual conjunto pertence ao Plenário?

A) Aprovar os Planos Anuais, eleger a Diretoria e as Comissões Permanentes e julgar infrações profissionais em primeira instância.

B) Analisar os Planos Anuais, encaminhá-los à apreciação superior e homologar Comissões Especiais e Grupos de Trabalho.

C) Representar legalmente o Conselho, convocar as reuniões colegiadas e instituir Comissões Especiais, ouvida a Diretoria.

D) Receber, tratar e encaminhar manifestações dos usuários, acompanhar as respostas e avaliar a satisfação com os serviços.

#### Extra Dia 5.7

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** composição da Diretoria Executiva.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente), especialmente o art. 18 resumido na seção.

Qual alternativa reproduz os cinco cargos que compõem a Diretoria Executiva do CRA-PR segundo o art. 18 do Regimento?

A) Presidente, Vice-Presidente, Ouvidor, Diretor de Administração e Finanças e Diretor de Fiscalização e Registro.

B) Presidente, Vice-Presidente, Secretário-Geral, Diretor de Tecnologia e Diretor de Relações Institucionais.

C) Presidente, Vice-Presidente, Diretor de Administração e Finanças, Diretor de Ética e Diretor Eleitoral.

D) Presidente, Vice-Presidente, Diretor de Administração e Finanças, Diretor de Fiscalização e Registro e Diretor de Relações Institucionais.

#### Extra Dia 5.8

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** Diretoria Executiva × Plenário.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente), nos arts. 23 e 25 e na tabela Plenário × Diretoria × Presidente.

Na tramitação dos Planos Anuais e na criação de Comissões Especiais ou Grupos de Trabalho, qual sequência respeita a distribuição regimental de competências?

A) A Diretoria aprova os Planos, o Plenário apenas os protocola e o Presidente homologa sozinho as estruturas temporárias.

B) A Diretoria analisa e encaminha os Planos, o Plenário os aprova e a Diretoria homologa a instituição e a composição das estruturas temporárias.

C) O Presidente analisa e encaminha os Planos, a Diretoria os aprova e o Plenário homologa a composição das estruturas temporárias.

D) O Plenário analisa e encaminha os Planos, a Diretoria os aprova e a Ouvidoria homologa a instituição das estruturas temporárias.

#### Extra Dia 5.9

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** competências presidenciais e `ad referendum`.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente), especialmente o art. 25 e a explicação do inciso XVIII.

Ao descrever os poderes do Presidente, o parecer deve preservar a participação da Diretoria e o controle colegiado de providência urgente. Assinale a alternativa correta.

A) O Presidente representa e convoca, institui Comissão Especial após ouvir a Diretoria, mas seu ato urgente `ad referendum` dispensa apreciação posterior.

B) O Presidente representa e convoca, institui Comissão Especial apenas após votação do Plenário e submete o ato `ad referendum` à decisão final da Ouvidoria.

C) O Presidente representa e convoca, institui Comissão Especial após ouvir a Diretoria e submete o ato urgente `ad referendum` ao colegiado competente.

D) O Presidente representa e convoca, institui Comissão Especial sem ouvir a Diretoria e submete o ato `ad referendum` exclusivamente ao CFA.

#### Extra Dia 5.10

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** reuniões e quórum.

- **Nível:** Difícil

- **Uso:** Aprofundamento

- **Referência:** [Reuniões e quórum](semana_02_estudo.md#s2-d5-rf-reunioes), nos resumos dos arts. 30 a 33.

Uma minuta reúne quatro regras sobre reuniões do Plenário e da Diretoria. Qual versão está integralmente de acordo com o Regimento?

A) Reuniões ordinárias ocorrem de uma a quatro vezes por mês; a extraordinária exige justificativa e pauta; admite-se videoconferência; o quórum é maioria absoluta do total.

B) Reuniões ordinárias ocorrem de uma a quatro vezes por ano; a extraordinária dispensa pauta; admite-se videoconferência; o quórum é maioria simples dos presentes.

C) Reuniões ordinárias ocorrem de uma a quatro vezes por mês; a extraordinária exige justificativa e pauta; admite-se videoconferência; o quórum é maioria dos presentes.

D) Reuniões ordinárias ocorrem de uma a quatro vezes por mês; a extraordinária exige justificativa e pauta; exige-se presença física; o quórum é dois terços do total.

#### Extra Dia 5.11

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** Ouvidoria do CRA-PR.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Ouvidoria, Comissões e Grupos de Trabalho](semana_02_estudo.md#s2-d5-rf-ouvidoria-comissoes), especialmente os arts. 43 a 46 resumidos na seção.

Um usuário pede à Ouvidoria que anule uma decisão do Plenário. Ao responder, o CRA-PR também precisa explicar como o titular da unidade é escolhido. Assinale a orientação correta.

A) O Ouvidor é escolhido pela Diretoria entre profissionais registrados e pode anular a decisão quando identificar falha no atendimento ao usuário.

B) O Ouvidor é nomeado pelo Presidente entre terceiros e pode substituir a Diretoria na execução das providências decorrentes da manifestação.

C) O Ouvidor é eleito pelo Plenário entre Conselheiros Efetivos e pode rever o mérito da decisão, pois a mediação inclui poder deliberativo.

D) O Ouvidor é eleito pelo Plenário entre Conselheiros Efetivos e pode tratar, encaminhar e acompanhar o pedido, mas não anular a decisão.

#### Extra Dia 5.12

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** Comissões e Grupos de Trabalho.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Ouvidoria, Comissões e Grupos de Trabalho](semana_02_estudo.md#s2-d5-rf-ouvidoria-comissoes), nos arts. 49 a 54 resumidos na seção.

Ao verificar a composição de estruturas auxiliares, o controle interno compara regra geral das Comissões Permanentes, impedimento na Análise de Contas e limite das estruturas temporárias. Assinale a síntese correta.

A) Permanentes têm cinco membros; Diretor deve integrar a Análise de Contas; Especiais e GTs têm até três membros e duração permanente.

B) Permanentes têm três membros em qualquer hipótese; Diretor não integra comissão alguma; Especiais e GTs têm até cinco membros e caráter permanente.

C) Permanentes têm três membros, salvo regra específica; Diretor pode coordenar a Análise de Contas; Especiais e GTs não possuem limite nem prazo.

D) Permanentes têm três membros, salvo regra específica; Diretor não integra a Análise de Contas; Especiais e GTs têm até cinco membros e caráter temporário.

#### Extra Dia 5.13

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** contagem de prazo e casos omissos.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Contagem de prazo e casos omissos](semana_02_estudo.md#s2-d5-rf-prazos-omissoes), nos resumos dos arts. 58 e 60.

Uma unidade precisa calcular prazo regimental e encaminhar uma omissão não disciplinada. Qual procedimento reúne corretamente as três regras gerais?

A) Inclui o dia inicial, exclui o vencimento, mantém os termos em dia sem expediente e envia a omissão ao Presidente.

B) Exclui o dia inicial, inclui o vencimento, mantém os termos em dia sem expediente e envia a omissão ao CFA.

C) Exclui o dia inicial, inclui o vencimento, exige expediente normal no início e no fim e envia a omissão ao Plenário.

D) Inclui o dia inicial e o vencimento, exige expediente normal apenas no fim e envia a omissão à Ouvidoria.

#### Extra Dia 5.14

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** catálogo de infrações e gradação.

- **Nível:** Difícil

- **Uso:** Revisão

- **Referência:** [Código: deveres e catálogo de infrações](semana_02_estudo.md#s2-d5-rf-etica-deveres-infracoes) e [Sanções, PF × PJ, multas e garantias processuais](semana_02_estudo.md#s2-d5-rf-etica-sancoes).

Uma pessoa física registrada usa artifício enganoso para obter vantagem indevida, enquadrando-se no art. 6º, XVIII. Qual consequência-base preserva sanção, multa e momento de aplicação?

A) Suspensão de seis meses a um ano, com a multa aplicável em conjunto e imposição somente após o trânsito em julgado administrativo.

B) Censura pública, com a multa substituindo a sanção e imposição antes da conclusão do processo administrativo.

C) Suspensão de um a cinco anos, com multa facultativa e imposição logo após a decisão inicial do Conselho Regional.

D) Cancelamento do registro, com multa conjunta e execução imediata antes da apreciação dos recursos administrativos.

#### Extra Dia 5.15

- **Dia:** Dia 5

- **Bloco:** Bloco 4

- **Matéria:** Legislação CRA/CFA

- **Assunto:** sanções, PF × PJ, multa e trânsito em julgado.

- **Nível:** Muito difícil

- **Uso:** Revisão

- **Referência:** [Sanções, PF × PJ, multas e garantias processuais](semana_02_estudo.md#s2-d5-rf-etica-sancoes), especialmente os arts. 13, § 3º, 18 e 23.

Em processo ético contra pessoa jurídica registrada, a decisão cogita suspensão, multa e execução antes do fim dos recursos. Assinale a alternativa que resolve corretamente os três pontos.

A) Suspensão e cancelamento não se aplicam à pessoa jurídica; a multa acompanha a sanção; a execução exige trânsito administrativo.

B) Suspensão e cancelamento não se aplicam à pessoa jurídica; a multa substitui a sanção; a execução exige trânsito administrativo.

C) Suspensão e cancelamento não se aplicam à pessoa jurídica; a multa acompanha a sanção; a execução pode preceder o trânsito administrativo.

D) Suspensão e cancelamento aplicam-se à pessoa jurídica; a multa substitui a sanção; a execução pode preceder o trânsito administrativo.

#### Extra Dia 5.16
- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** modalidade e alcance.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português — inferência e quantificadores](semana_02_estudo.md#s2-d5-rf-portugues).

Da frase “As reuniões podem ocorrer por videoconferência”, infere-se corretamente que:

A) toda reunião deve ocorrer remotamente.
B) a videoconferência é uma possibilidade, não uma obrigação universal.
C) nenhuma reunião pode ser presencial.
D) somente reuniões extraordinárias admitem videoconferência.
#### Extra Dia 5.17
- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita e relação concessiva/adversativa.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português — reescrita](semana_02_estudo.md#s2-d5-rf-portugues).

Original: “Embora seja mediadora, a Ouvidoria não decide.” Assinale a reescrita que preserva o sentido.

A) Como decide, a Ouvidoria não é mediadora.
B) Se for mediadora, a Ouvidoria decidirá necessariamente.
C) A Ouvidoria é mediadora, mas não decide.
D) A Ouvidoria não decide; portanto, não pode mediar.
#### Extra Dia 5.18
- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** regência do relativo e crase.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português — regência do relativo e crase](semana_02_estudo.md#s2-d5-rf-portugues).

Assinale a alternativa correta quanto à regência do pronome relativo e à crase.

A) “A decisão que o usuário discordou foi revista.”
B) “A Ouvidoria à qual o cidadão se dirigiu recebeu a manifestação.”
C) “A comissão cujos os membros foram eleitos reuniu-se.”
D) “O tema aonde a Comissão se manifestou exigia parecer.”
#### Extra Dia 5.19
- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** oração adjetiva restritiva × explicativa.
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português — pontuação e sentido](semana_02_estudo.md#s2-d5-rf-portugues).

Assinale a alternativa correta sobre o efeito das vírgulas.

A) Em “Os conselheiros que participaram da comissão votaram”, as vírgulas omitidas tornam a oração explicativa e abrangem necessariamente todos.
B) Orações restritivas e explicativas possuem sempre o mesmo alcance.
C) Inserir vírgulas jamais altera o conjunto referido pelo substantivo.
D) Sem vírgulas, a oração adjetiva pode selecionar um subconjunto; com vírgulas, pode apresentar explicação atribuída ao conjunto mencionado.
#### Extra Dia 5.20

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** paralelismo e clareza comparativa.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português — paralelismo e clareza](semana_02_estudo.md#s2-d5-rf-portugues).

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
| 5.12 | D |
| 5.13 | C |
| 5.14 | A |
| 5.15 | A |
| 5.16 | B |
| 5.17 | C |
| 5.18 | B |
| 5.19 | D |
| 5.20 | B |

### Comentários das questões extras do Dia 5

#### Comentário Extra Dia 5.1

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** a Retificação I não manteve a RN nº 640/2024 como Código vigente; ela passou a indicar a RN nº 671/2025.
- **B)** essas resoluções e a Lei nº 12.514/2011 ficam como contexto externo e não formam o núcleo material das extras.
- **C)** reúne Lei, Decreto, Regimento/RN nº 651/2024 e Código/RN nº 671/2025 no recorte efetivamente adotado.
- **D)** inverte Regimento e Código; a RN nº 651/2024 é o Regimento e a RN nº 671/2025 aprova o Código.

**Conceito:** delimitação normativa e controle de versão após a retificação do edital.

**Pegadinha:** manter a resolução substituída ou trocar os números do Regimento e do Código.

**Como pensar:** identifique primeiro a função de cada fonte e só depois confira o número vigente de cada resolução.

**Referência:** [Escopo e controle de versão](semana_02_estudo.md#s2-d5-rf-escopo), especialmente o núcleo de quatro fontes e a substituição da RN nº 640/2024 pela RN nº 671/2025.

#### Comentário Extra Dia 5.2

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** preserva natureza autárquica pública, três autonomias, sede na capital e jurisdição estadual limitada às competências do Conselho.
- **B)** o CRA-PR não é autarquia de direito privado nem possui competência normativa nacional sobre os demais regionais.
- **C)** o Conselho tem personalidade autárquica própria e não integra a Administração Direta do Estado do Paraná.
- **D)** autonomia não significa soberania nem autoriza afastar as diretrizes nacionais do CFA.

**Conceito:** natureza jurídica, autonomia, sede e alcance territorial do CRA-PR.

**Pegadinha:** converter autonomia em independência sistêmica ou confundir autarquia com órgão da Administração Direta.

**Como pensar:** valide separadamente natureza, autonomias, sede e limite material da jurisdição.

**Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), nos arts. 1º e 2º resumidos na seção.

#### Comentário Extra Dia 5.3

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** a Presidência não aparece como categoria autônoma no rol do art. 3º, embora o Presidente possua competências próprias.
- **B)** Conselheiros efetivos e suplentes compõem o Plenário, mas não são apresentados como órgão separado nesse rol.
- **C)** “setores administrativos” não substitui a categoria regimental dos Órgãos de Representação nem completa o rol.
- **D)** reproduz as cinco categorias enumeradas na seção teórica correspondente ao art. 3º.

**Conceito:** órgãos e estruturas regimentais do CRA-PR.

**Pegadinha:** transformar cargo, integrante ou setor interno em órgão autônomo do rol.

**Como pensar:** compare categorias institucionais, sem confundir quem exerce função com o órgão ao qual pertence.

**Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), no resumo do art. 3º.

#### Comentário Extra Dia 5.4

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** o Plenário delibera e julga matérias regionais, não se limita a aconselhar a Diretoria.
- **B)** reúne a posição colegiada superior e a atuação como primeira instância na jurisdição do CRA-PR.
- **C)** direção administrativa e execução cotidiana pertencem predominantemente à Diretoria, dentro de suas competências.
- **D)** o Plenário é regional e de primeira instância; a função recursal nacional atribuída por lei pertence ao CFA.

**Conceito:** natureza colegiada, deliberação superior e julgamento regional pelo Plenário.

**Pegadinha:** trocar deliberação por execução ou primeira instância regional por última instância nacional.

**Como pensar:** separe posição institucional, âmbito territorial e grau de julgamento antes de escolher.

**Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), especialmente o art. 4º e a diferença entre primeira e última instância.

#### Comentário Extra Dia 5.5

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** acerta composição e renovação, mas reduz indevidamente o mandato de Conselheiro para dois anos.
- **B)** o Plenário inclui respectivos Suplentes; eles não podem ser retirados da composição.
- **C)** preserva os nove pares, a renovação bienal alternada e o mandato quadrienal com uma reeleição.
- **D)** a renovação não é integral e a possibilidade de reeleição não é ilimitada.

**Conceito:** composição do Plenário, renovação alternada e mandato dos Conselheiros.

**Pegadinha:** transportar o mandato bienal da Diretoria para os Conselheiros ou eliminar os Suplentes.

**Como pensar:** confira em três colunas: composição, ciclo de renovação e mandato com limite de reeleição.

**Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), nos resumos dos arts. 5º e 6º.

#### Comentário Extra Dia 5.6

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** aprovação dos Planos, eleição dos membros e julgamento regional em primeira instância integram as competências do Plenário.
- **B)** análise e encaminhamento dos Planos, assim como a homologação indicada, pertencem à Diretoria Executiva.
- **C)** representação, convocação e instituição dessas estruturas são atribuições do Presidente, nos limites regimentais.
- **D)** o conjunto descreve a atuação mediadora e de acompanhamento da Ouvidoria.

**Conceito:** distribuição de competências entre Plenário, Diretoria, Presidente e Ouvidoria.

**Pegadinha:** reconhecer atos verdadeiros do CRA-PR, mas atribuí-los ao órgão errado.

**Como pensar:** associe cada verbo ao responsável predominante antes de avaliar o conjunto completo.

**Referência:** [Regimento/RN CFA nº 651/2024: órgãos e Plenário](semana_02_estudo.md#s2-d5-rf-regimento-orgaos), no rol resumido do art. 8º.

#### Comentário Extra Dia 5.7

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** o Ouvidor não ocupa uma das cinco Diretorias enumeradas no art. 18.
- **B)** Secretário-Geral e Diretor de Tecnologia não substituem os cargos regimentais de Administração e Finanças e de Fiscalização e Registro.
- **C)** Diretor de Ética e Diretor Eleitoral não integram a composição listada para a Diretoria Executiva.
- **D)** apresenta Presidência, Vice-Presidência e as três Diretorias setoriais previstas no Regimento.

**Conceito:** composição regimental da Diretoria Executiva.

**Pegadinha:** inserir funções ou áreas existentes no ambiente institucional como se fossem cargos da Diretoria.

**Como pensar:** confirme a dupla Presidente/Vice e depois as três Diretorias: Administração e Finanças, Fiscalização e Registro e Relações Institucionais.

**Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente), especialmente o art. 18 resumido na seção.

#### Comentário Extra Dia 5.8

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** a aprovação dos Planos cabe ao Plenário, e a homologação regimental não é ato isolado do Presidente.
- **B)** preserva análise e encaminhamento pela Diretoria, aprovação pelo Plenário e homologação das estruturas pela Diretoria.
- **C)** desloca as etapas dos Planos e entrega ao Plenário a homologação atribuída à Diretoria.
- **D)** inverte Plenário e Diretoria e atribui poder homologatório à Ouvidoria, que não decide.

**Conceito:** encadeamento de competências nos Planos Anuais e nas estruturas temporárias.

**Pegadinha:** reconhecer os verbos corretos, mas trocá-los entre Diretoria, Plenário, Presidente e Ouvidoria.

**Como pensar:** resolva em duas trilhas: Diretoria analisa/encaminha e Plenário aprova; Presidente institui e Diretoria homologa.

**Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente), nos arts. 23 e 25 e na tabela Plenário × Diretoria × Presidente.

#### Comentário Extra Dia 5.9

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** `ad referendum` exige apreciação posterior e não transforma a providência urgente em decisão definitiva do Presidente.
- **B)** a instituição é feita pelo Presidente, ouvida a Diretoria, e a Ouvidoria não exerce decisão final sobre o ato.
- **C)** conserva representação e convocação, oitiva da Diretoria e retorno da providência urgente ao colegiado competente.
- **D)** elimina indevidamente a oitiva e cria submissão exclusiva ao CFA, não prevista como regra geral do instituto.

**Conceito:** competências do Presidente, oitiva da Diretoria e natureza provisória do `ad referendum`.

**Pegadinha:** confundir decisão urgente com transferência definitiva da competência colegiada.

**Como pensar:** confirme quem age de imediato, quem deve ser ouvido e quem reaprecia a medida depois.

**Referência:** [Diretoria Executiva e Presidente](semana_02_estudo.md#s2-d5-rf-diretoria-presidente), especialmente o art. 25 e a explicação do inciso XVIII.

#### Comentário Extra Dia 5.10

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** combina periodicidade mensal, pauta e justificativa, possibilidade de videoconferência e maioria absoluta do total de membros.
- **B)** troca mês por ano, dispensa pauta e calcula quórum por maioria simples dos presentes.
- **C)** acerta as três primeiras regras, mas maioria absoluta toma como base o total de membros, não somente os presentes.
- **D)** o Regimento admite videoconferência e não fixa dois terços como quórum geral de instalação e funcionamento.

**Conceito:** periodicidade, reunião extraordinária, videoconferência e maioria absoluta.

**Pegadinha:** preservar quase toda a regra e alterar apenas a base de cálculo do quórum.

**Como pensar:** audite as quatro proposições separadamente; uma única troca invalida a alternativa inteira.

**Referência:** [Reuniões e quórum](semana_02_estudo.md#s2-d5-rf-reunioes), nos resumos dos arts. 30 a 33.

#### Comentário Extra Dia 5.11

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** a escolha não cabe à Diretoria nem recai genericamente sobre profissionais registrados, e a unidade não anula decisões.
- **B)** o titular não é terceiro livremente nomeado e a Ouvidoria não substitui a Diretoria na execução administrativa.
- **C)** acerta eleição e elegibilidade, mas mediação não confere poder deliberativo nem revisão de mérito.
- **D)** o Plenário elege o Ouvidor entre Conselheiros Efetivos, e a unidade recebe, trata, encaminha e acompanha sem decidir.

**Conceito:** escolha do Ouvidor e ausência de caráter executivo, deliberativo ou decisório.

**Pegadinha:** acertar a forma de eleição e, na mesma alternativa, ampliar indevidamente os poderes da unidade.

**Como pensar:** resolva dois filtros independentes: quem pode ser eleito e quais verbos a Ouvidoria pode praticar.

**Referência:** [Ouvidoria, Comissões e Grupos de Trabalho](semana_02_estudo.md#s2-d5-rf-ouvidoria-comissoes), especialmente os arts. 43 a 46 resumidos na seção.

#### Comentário Extra Dia 5.12

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** inverte os quantitativos, exige participação vedada na Análise de Contas e transforma estruturas temporárias em permanentes.
- **B)** elimina a ressalva normativa, amplia o impedimento para toda comissão e atribui permanência a estruturas específicas ou temporárias.
- **C)** membro da Diretoria não pode integrar a Comissão de Análise de Contas, e o ato temporário deve indicar limite e prazo.
- **D)** preserva a regra de três membros, o impedimento específico e o máximo de cinco nas estruturas temporárias.

**Conceito:** composição e limites das Comissões e dos Grupos de Trabalho.

**Pegadinha:** generalizar um impedimento específico ou trocar o número de membros e a natureza temporal.

**Como pensar:** confira separadamente regra geral, exceção da Análise de Contas e teto das estruturas temporárias.

**Referência:** [Ouvidoria, Comissões e Grupos de Trabalho](semana_02_estudo.md#s2-d5-rf-ouvidoria-comissoes), nos arts. 49 a 54 resumidos na seção.

#### Comentário Extra Dia 5.13

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** inverte inclusão e exclusão, ignora o expediente normal e atribui a omissão ao Presidente.
- **B)** acerta os termos incluído e excluído, mas erra o expediente e transfere ao CFA a competência do Plenário.
- **C)** exclui o início, inclui o vencimento, exige expediente normal nos termos e leva a omissão ao Plenário.
- **D)** inclui indevidamente o dia inicial, trata o expediente de modo incompleto e atribui decisão à Ouvidoria.

**Conceito:** contagem de prazo, expediente normal e competência para casos omissos.

**Pegadinha:** acertar uma parte da contagem e errar a condição de expediente ou o órgão competente.

**Como pensar:** aplique em ordem: termo excluído, termo incluído, calendário útil e autoridade para a omissão.

**Referência:** [Contagem de prazo e casos omissos](semana_02_estudo.md#s2-d5-rf-prazos-omissoes), nos resumos dos arts. 58 e 60.

#### Comentário Extra Dia 5.14

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** o inciso XVIII leva à suspensão de seis meses a um ano, acompanhada de multa e aplicada após o trânsito administrativo.
- **B)** censura não é a sanção-base do inciso XVIII, a multa não substitui a sanção e o processo deve terminar.
- **C)** a faixa de um a cinco anos pertence a outro grupo de infrações, e a multa não é facultativa nem a decisão inicial basta.
- **D)** cancelamento não é a consequência-base dessa conduta e não pode ser executado antes do trânsito administrativo.

**Conceito:** tipificação do art. 6º, XVIII, faixa de suspensão, multa conjunta e garantia processual.

**Pegadinha:** localizar a natureza da sanção, mas trocar sua faixa ou antecipar a aplicação.

**Como pensar:** faça a sequência inciso → sanção/faixa → multa conjunta → trânsito em julgado administrativo.

**Referência:** [Código: deveres e catálogo de infrações](semana_02_estudo.md#s2-d5-rf-etica-deveres-infracoes) e [Sanções, PF × PJ, multas e garantias processuais](semana_02_estudo.md#s2-d5-rf-etica-sancoes).

#### Comentário Extra Dia 5.15

**Alternativa correta: A.**

**Nível:** Muito difícil

**Uso:** Revisão

**Análise das alternativas:**

- **A)** preserva simultaneamente a incompatibilidade das duas sanções, a multa conjunta e a garantia processual.
- **B)** acerta sujeito e momento processual, mas afirma incorretamente que a multa substitui a sanção.
- **C)** acerta sujeito e relação da multa, mas antecipa a aplicação para antes do trânsito em julgado administrativo.
- **D)** as duas sanções não se aplicam à pessoa jurídica, a multa é conjunta e a aplicação exige trânsito administrativo.

**Conceito:** regime sancionador da pessoa jurídica, relação entre multa e sanção e trânsito administrativo.

**Pegadinha:** construir alternativas próximas que falham em apenas um dos três filtros jurídicos.

**Como pensar:** avalie independentemente sujeito, efeito pecuniário e momento processual; aceite apenas a opção que passa nos três.

**Referência:** [Sanções, PF × PJ, multas e garantias processuais](semana_02_estudo.md#s2-d5-rf-etica-sancoes), especialmente os arts. 13, § 3º, 18 e 23.

#### Comentário Extra Dia 5.16
**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

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

**Nível:** Médio

**Uso:** Simulado

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
**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. `Discordar` exige `de`: “de que”.
- **B)** Correta. `Dirigir-se a` exige preposição, que se funde com `a qual`.
- **C)** Incorreta. `Cujo` não admite artigo depois.
- **D)** Incorreta. A regência pede “sobre o qual”; `aonde` indica movimento a lugar.

**Conceito:** regência do relativo e crase.

**Pegadinha:** omitir preposição exigida pelo verbo ou inserir artigo após `cujo`.

**Como pensar:** identifique a regência antes de escolher o pronome relativo.

**Referência:** [Português — regência do relativo e crase](semana_02_estudo.md#s2-d5-rf-portugues).

#### Comentário Extra Dia 5.19
**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

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

**Nível:** Médio

**Uso:** Simulado

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

### S2D6Q251 — Métricas de rede

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Comunicação de dados e medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados), com recuperação em [D6-RF-MX-01](semana_02_estudo.md#s2-d6-rf-mx-01)

Em um enlace de 1 Gbit/s, a aplicação recebe 700 Mbit/s de dados úteis. A medida de 1 Gbit/s é largura de banda e a de 700 Mbit/s é:

A) latência.
B) jitter.
C) perda.
D) goodput.

### S2D6Q252 — Switch Ethernet e domínios

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch), nos comportamentos de aprendizagem e encaminhamento; e [Domínios de colisão e broadcast](semana_02_estudo.md#s2-d1-dominios).

Quatro hosts estão ligados a um switch de camada 2 na mesma VLAN. Sobre aprendizagem, encaminhamento e domínios Ethernet, assinale a alternativa correta.

A) O switch aprende MAC de origem, encaminha unicast conhecido seletivamente e isola colisões por porta, sem eliminar broadcasts da VLAN.

B) O switch aprende MAC apenas pelo destino dos quadros e impede que broadcasts alcancem outras portas da mesma VLAN.

C) O switch aprende MAC de origem e encaminha unicast conhecido seletivamente, mas todas as portas permanecem no mesmo domínio de colisão.

D) O switch repete bits por todas as portas, não aprende endereços e mantém um único domínio de colisão compartilhado.

### S2D6Q253 — Encapsulamento por salto

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento), com recuperação em [D6-RF-MX-02](semana_02_estudo.md#s2-d6-rf-mx-02)

No encaminhamento de um pacote IPv4 por um roteador, normalmente:

A) o quadro de enlace é removido e outro é criado para o próximo enlace.
B) o segmento TCP vira obrigatoriamente datagrama UDP.
C) o endereço MAC de origem é mantido até o destino final.
D) a aplicação recebe diretamente os bits do enlace.

### S2D6Q254 — CIDR e broadcast

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts) e [Cálculos resolvidos de CIDR](semana_02_estudo.md#s2-d2-calculos)

Para `10.0.5.130/26`, a rede e o broadcast são, respectivamente:

A) `10.0.5.0` e `10.0.5.255`.
B) `10.0.5.64` e `10.0.5.127`.
C) `10.0.5.128` e `10.0.5.191`.
D) `10.0.5.130` e `10.0.5.192`.

### S2D6Q255 — Gateway e ARP

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Gateway padrão](semana_02_estudo.md#s2-d2-gateway) e [ARP](semana_02_estudo.md#s2-d2-arp)

Um host IPv4 precisa alcançar endereço fora da própria sub-rede. Antes de transmitir, ele normalmente obtém por ARP o MAC:

A) do servidor remoto.
B) do DNS autoritativo.
C) do switch de acesso.
D) do gateway local.

### S2D6Q256 — IPv6 e Neighbor Discovery

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [ICMP e ICMPv6 — Neighbor Discovery, NS e NA](semana_02_estudo.md#s2-d2-icmp) e [IPv6](semana_02_estudo.md#s2-d2-ipv6), incluindo a ausência de broadcast no IPv6.

Um host IPv6 precisa descobrir o endereço de enlace de um vizinho e verificar sua alcançabilidade no segmento local. Qual mecanismo atende a essas funções?

A) ARP por broadcast, com mensagens Request e Reply idênticas às utilizadas na resolução de vizinhos IPv4.

B) Neighbor Discovery sobre ICMPv6, com mensagens como Neighbor Solicitation e Neighbor Advertisement e uso apropriado de multicast.

C) DHCPv6 por concessão, com mensagens do servidor destinadas a testar continuamente a alcançabilidade entre os vizinhos.

D) DNS por consulta recursiva, com registros AAAA usados para obter diretamente o endereço de enlace do vizinho.

### S2D6Q257 — TCP e UDP

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [TCP e UDP](semana_02_estudo.md#s2-d3-tcp-udp), com síntese em [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05)

Analise as assertivas sobre TCP e UDP.

I. TCP oferece confirmação e ordenação no transporte.
II. UDP fornece retransmissão nativa.
III. Uma aplicação sobre UDP pode implementar confiabilidade própria.

Está correto o que se afirma em:

A) I e III, apenas.
B) I e II, apenas.
C) II e III, apenas.
D) I, II e III.

### S2D6Q258 — HTTP/3 e QUIC

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [HTTP e HTTPS](semana_02_estudo.md#s2-d3-http-https), nos trechos que distinguem HTTP/1.1 e HTTP/2 em TCP de HTTP/3 sobre QUIC/UDP; e [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05).

Ao liberar um portal para navegadores que negociam HTTP/3, a equipe precisa reconhecer o transporte e a porta usual desse acesso HTTPS. Qual associação está correta?

A) HTTP/3 usa TCP em 443, e QUIC participa apenas da compactação dos cabeçalhos acima do transporte.

B) HTTP/3 usa QUIC sobre UDP em 80, sem a proteção criptográfica exigida no acesso HTTPS descrito.

C) HTTP/3 usa QUIC sobre UDP, normalmente em 443, com os recursos de transporte e proteção integrados ao QUIC.

D) HTTP/3 usa UDP diretamente sem QUIC, enquanto a confiabilidade permanece delegada a uma conexão TCP paralela.

### S2D6Q259 — Sequência DORA no DHCPv4

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [DHCP — sequência DORA](semana_02_estudo.md#s2-d3-dhcp), na lista ordenada das mensagens; e [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05).

Na obtenção inicial de configuração por DHCPv4, qual alternativa apresenta as quatro mensagens da sequência DORA em sua ordem lógica?

A) DHCPDISCOVER, DHCPOFFER, DHCPREQUEST e DHCPACK.

B) DHCPOFFER, DHCPDISCOVER, DHCPACK e DHCPREQUEST.

C) DHCPDISCOVER, DHCPREQUEST, DHCPOFFER e DHCPACK.

D) DHCPREQUEST, DHCPOFFER, DHCPDISCOVER e DHCPACK.

### S2D6Q260 — Função e transportes do DNS

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [DNS](semana_02_estudo.md#s2-d3-dns), nas subseções de componentes, registros, cache/TTL e transportes; e [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05).

A respeito da função, da hierarquia e dos transportes do DNS, assinale a alternativa tecnicamente correta.

A) DNS publica somente endereços IPv4 e usa exclusivamente 53/UDP, inclusive para toda transferência de zona.

B) DNS resolve e publica diferentes dados por registros; no modo clássico, utiliza 53/UDP e também 53/TCP.

C) Todo resolvedor é autoritativo para os dados consultados e deve ignorar cache, TTL e referências recebidas na hierarquia.

D) DNSSEC cifra consultas e respostas para confidencialidade e torna desnecessário o suporte a TCP no DNS clássico.

### S2D6Q261 — Envio e acesso sincronizado ao correio eletrônico

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Correio eletrônico — SMTP, POP3 e IMAP](semana_02_estudo.md#s2-d3-email), nas subseções de funções e fluxo integrado; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

Uma usuária precisa submeter uma mensagem ao serviço de correio e depois manter pastas, marcações e leitura sincronizadas entre dois dispositivos. Qual combinação é adequada?

A) SMTP para sincronização da caixa; POP3 para transferência entre servidores e preservação das pastas compartilhadas.

B) IMAP para submissão e transferência da mensagem; SMTP para acesso sincronizado à caixa mantida no servidor.

C) POP3 para submissão da mensagem; IMAP para transferência entre servidores e manutenção da fila de entrega.

D) SMTP para submissão e transferência da mensagem; IMAP para acesso sincronizado à caixa mantida no servidor.

### S2D6Q262 — SFTP e SSH

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [FTP, FTPS, SFTP, SSH e Telnet](semana_02_estudo.md#s2-d3-transferencia-remota), especialmente as subseções SFTP e SSH e a distinção para FTPS; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

Uma rotina de arquivos deve aproveitar a autenticação por chave e o serviço SSH já disponíveis no servidor. Qual relação entre os protocolos está correta?

A) SFTP é FTP protegido por TLS explícito e inicia sua negociação no canal de controle em 21/TCP.

B) FTPS é o subsistema de arquivos do SSH e reutiliza diretamente a sessão criptografada normalmente aberta em 22/TCP.

C) SFTP é um protocolo de transferência sobre SSH e pode reutilizar sua autenticação, normalmente pela porta 22/TCP.

D) Telnet é a modalidade interativa do SSH e fornece a mesma proteção criptográfica de canal normalmente em 23/TCP.

### S2D6Q263 — MIB e OID no SNMP

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp), nas definições de gerente, agente, MIB, OID e operações; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

Um gerente SNMP precisa consultar no agente o contador de octetos de uma interface. Qual relação entre MIB e OID permite localizar o objeto gerenciado?

A) MIB é o endereço do gerente, e OID é a community string usada como credencial de qualquer versão do SNMP.

B) MIB organiza os objetos gerenciados, e OID identifica um objeto específico nessa estrutura para operações do protocolo.

C) MIB identifica somente um objeto, e OID representa toda a hierarquia e substitui as operações GET e SET.

D) MIB e OID são chaves de autenticação, usadas pelo SNMPv3 para substituir usuários, algoritmos e políticas de acesso.

### S2D6Q264 — NAT básico e PAT/NAPT

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat), nas definições e no exemplo da tabela com portas públicas diferentes; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

Em uma comparação estrita entre NAT básico e PAT/NAPT, qual característica permite a vários fluxos internos compartilhar um único endereço público?

A) PAT preserva as portas e altera somente o endereço IP, enquanto NAT básico traduz também cada identificador de transporte.

B) PAT cria apenas associação individual entre endereços, sem manter qualquer distinção de portas entre fluxos simultâneos.

C) PAT traduz somente a porta de destino, nunca o endereço, e dispensa tabela para desfazer a tradução dos retornos.

D) PAT traduz endereço e também portas de transporte, mantendo mapeamentos que distinguem os fluxos no endereço compartilhado.

### S2D6Q265 — NTP e coerência temporal

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp), nos trechos sobre 123/UDP, correlação de logs e diferença entre referência e fuso; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

Logs de servidores registram o mesmo evento com vários minutos de diferença, embora a exibição de fuso esteja configurada. Qual afirmação aponta o serviço e o escopo corretos?

A) NTP sincroniza a referência dos relógios, normalmente em 123/UDP, enquanto fuso e horário de verão são configurações locais.

B) NTP distribui somente o fuso em 123/TCP e não altera a referência temporal mantida pelo relógio do sistema.

C) NTP usa o TTL do DNS para reajustar os relógios sempre que uma resposta de nome expira no cache.

D) NTP ordena os registros depois de coletados, mas não sincroniza os relógios que geraram os eventos originais.

### S2D6Q266 — Vulnerabilidade, ameaça e risco

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Conceitos de risco](semana_02_estudo.md#s2-d4-conceitos-risco), com recuperação em [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07)

Uma falha de validação explorável é uma vulnerabilidade; o agente capaz de explorá-la é uma ameaça; a combinação de probabilidade e impacto expressa:

A) um requisito de disponibilidade.
B) um registro de auditoria.
C) uma medida de risco.
D) uma garantia de não repúdio.

### S2D6Q267 — Autenticação e autorização

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria), nas subseções 3.1 e 3.2; e [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07).

Em um sistema, a pessoa apresenta credenciais válidas, mas a tentativa de aprovar pagamento é negada por sua função. Qual associação descreve as duas decisões?

A) Autenticação verifica a permissão para pagar, e autorização comprova a identidade apresentada pelas credenciais.

B) Autenticação estabelece confiança na identidade, e autorização verifica se essa identidade pode executar o pagamento.

C) Autenticação registra a ação para auditoria, e autorização garante que o usuário não possa negar o evento.

D) Autenticação atribui o papel funcional, e autorização valida a senha usada para entrar no sistema.

### S2D6Q268 — Sniffing, spoofing e ataque on-path

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede), nas subseções de spoofing, sniffing e ataque on-path; e [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07).

Ao classificar técnicas de ataque à comunicação de rede, qual alternativa distingue corretamente spoofing e ataque on-path sem atribuir ao sniffing uma alteração obrigatória?

A) Sniffing pode observar passivamente, mas spoofing exige interceptar e modificar todos os pacotes entre os dois extremos.

B) Spoofing falsifica identidade ou origem; on-path se posiciona no caminho para interceptar e pode também alterar o tráfego.

C) Sniffing altera ativamente o conteúdo, enquanto on-path se limita a falsificar o endereço de origem sem interceptar comunicação.

D) Spoofing falsifica identidade ou origem, mas um atacante on-path somente observa e nunca consegue modificar o tráfego.

### S2D6Q269 — IDS para detecção sem bloqueio obrigatório

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips), nas subseções que contrastam monitoramento/alerta com prevenção em linha; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

Uma equipe quer analisar cópias do tráfego, gerar alertas sobre padrões suspeitos e evitar que o controle precise bloquear os fluxos observados. Qual arquitetura atende ao requisito?

A) IDS, que pode monitorar fora do caminho direto e alertar sem possuir a obrigação de interromper cada fluxo.

B) IPS passivo, que recebe somente cópia do tráfego e por definição não possui capacidade de prevenção em linha.

C) IDS em linha, que necessariamente descarta todo pacote classificado como suspeito antes de emitir qualquer alerta.

D) IDS ou IPS indistintamente, pois ambos operam sempre fora de linha e garantem o mesmo bloqueio dos ataques.

### S2D6Q270 — Publicação de portal em DMZ

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [DMZ](semana_02_estudo.md#s2-d4-dmz), nos princípios de exposição intermediária, fluxo mínimo e presunção de possível comprometimento; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

Um portal acessível pela internet precisa consultar um serviço interno específico, sem expor diretamente a rede de dados sensíveis. Qual desenho segue o princípio da DMZ?

A) Colocar portal e serviço interno na mesma VLAN e liberar todos os fluxos para evitar falhas de integração.

B) Colocar o portal fora do perímetro de filtragem e permitir que ele alcance diretamente qualquer endereço da rede interna.

C) Colocar o portal na DMZ e considerar confiável qualquer conexão originada nesse segmento para todos os serviços internos.

D) Colocar o portal na DMZ e autorizar para a rede interna somente os fluxos indispensáveis, explicitamente filtrados e monitorados.

### S2D6Q271 — Limites da VPN

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [VPN](semana_02_estudo.md#s2-d4-vpn), com contraste em [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08)

Uma VPN foi corretamente configurada com cifra e autenticação dos extremos, e seu túnel está operacional. Ainda assim, qual propriedade permanece fora do escopo direto da VPN?

A) Proteger, no túnel, o tráfego em trânsito entre os extremos configurados.

B) Autenticar os extremos para o estabelecimento do túnel, conforme o mecanismo adotado.

C) Assegurar que o dispositivo remoto esteja sem malware e autorizar cada ação dentro das aplicações acessadas.

D) Aplicar proteção criptográfica de integridade aos dados transportados no túnel, conforme a suíte negociada.

### S2D6Q272 — Hash como resumo de integridade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Hash, MAC e armazenamento de senhas — hash](semana_02_estudo.md#s2-d4-hash-hmac-senhas), incluindo o uso de referência confiável e os limites de confidencialidade/autenticação; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

Uma equipe recebe um arquivo e um valor de referência por canal confiável, calcula novamente a função hash e compara os resultados. Qual propriedade e limite descrevem o procedimento?

A) O hash cifra o arquivo de forma reversível, e uma chave de decifragem permite recuperar integralmente a entrada original.

B) O hash produz um resumo para verificar alteração contra referência confiável, sem permitir recuperar normalmente o original pelo resumo.

C) O hash fornece sozinho confidencialidade e autenticação de origem, mesmo quando atacante pode substituir arquivo e resumo juntos.

D) O hash garante ausência absoluta de colisões e permite reconstruir qualquer entrada que tenha produzido o valor publicado.

### S2D6Q273 — Assinatura digital

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Assinatura digital e certificado](semana_02_estudo.md#s2-d4-assinatura-certificado), com contraste em [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08)

Assinale a correta sobre assinatura digital.

A) É criada com a chave pública e verificada com a privada.
B) Oculta necessariamente todo o documento.
C) É criada com a chave privada e verificada com a pública.
D) É idêntica a uma senha compartilhada.

### S2D6Q274 — Papel e limites do TLS

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [TLS](semana_02_estudo.md#s2-d4-tls), nas propriedades pretendidas e na lista de elementos fora do canal; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

Um cliente HTTPS valida corretamente o certificado do servidor e conclui o handshake TLS. Qual conclusão permanece dentro do escopo técnico desse canal?

A) TLS pode autenticar o servidor e proteger confidencialidade e integridade em trânsito, conforme validação, algoritmos e configuração.

B) TLS comprova que todo conteúdo publicado é verdadeiro e autoriza o usuário a executar qualquer operação na aplicação.

C) TLS protege somente dados armazenados após a sessão e não oferece confidencialidade ou integridade durante o transporte.

D) TLS garante que os dois endpoints estejam livres de malware e oculta todos os metadados observáveis na rede.

### S2D6Q275 — WPA3-Personal e SAE

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi), nas subseções WPA3, modo de transição e boas práticas; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

Uma organização migra a rede sem fio de WPA2-Personal para WPA3-Personal. Qual afirmação sobre o mecanismo e os cuidados restantes está correta?

A) SAE elimina a necessidade de senha forte, atualização de firmware e proteção da administração do ponto de acesso.

B) SAE permite reutilizar passivamente a captura da associação para tentativas offline exatamente como no WPA2-Personal baseado em PSK.

C) O modo de transição garante que todos os clientes negociem WPA3 e recebam as mesmas propriedades do perfil mais novo.

D) WPA3-Personal usa SAE, mas credenciais, firmware, configuração, modo negociado e segmentação continuam relevantes à segurança.

### S2D6Q276 — Objetivo imediato da contenção

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Resposta a incidentes — resposta e contenção](semana_02_estudo.md#s2-d4-resposta-incidentes), no contraste com erradicação e recuperação; e [D6-RF-MX-09](semana_02_estudo.md#s2-d6-rf-mx-09).

Após confirmar um incidente em propagação, a equipe inicia a contenção antes de erradicar persistência e recuperar os serviços. Qual ação expressa o objetivo imediato dessa fase?

A) Apagar artefatos e logs dos hosts afetados para impedir que evidências sejam usadas durante a investigação posterior.

B) Isolar ou restringir ativos e fluxos para limitar propagação e impacto, preservando condições para as etapas seguintes.

C) Remover toda persistência, corrigir o vetor explorado e rotacionar credenciais, concluindo definitivamente a causa do incidente.

D) Restaurar todos os serviços ao estado validado, confirmar o funcionamento e encerrar o monitoramento de recorrência.

### S2D6Q277 — RPO

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup) e [D6-RF-MX-09 — Resposta, continuidade e objetivos de recuperação](semana_02_estudo.md#s2-d6-rf-mx-09)

Com RPO de 30 minutos e incidente às 14h, qual é o horário mais antigo ainda aceitável para o ponto de recuperação?

A) 13h, subtraindo uma hora do instante do incidente.

B) 14h30, somando o RPO ao instante do incidente.

C) 14h, pois o RPO exige sempre perda igual a zero.

D) 13h30, subtraindo a janela máxima de perda tolerada.

### S2D6Q278 — Redundância e backup

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Backup e disponibilidade — backup × redundância × alta disponibilidade](semana_02_estudo.md#s2-d4-backup), incluindo o limite de RAID e replicação; e [D6-RF-MX-09](semana_02_estudo.md#s2-d6-rf-mx-09).

Um serviço usa dois componentes em failover e também mantém cópias isoladas e versionadas dos dados. Qual distinção entre os dois controles está correta?

A) Redundância oferece alternativa para reduzir interrupção; backup permite restaurar dados ou versões anteriores após perda ou corrupção.

B) Backup assume automaticamente a carga em tempo real durante falha; redundância preserva versões históricas para restauração posterior.

C) RAID fornece cópia externa versionada contra exclusão; backup serve somente para trocar imediatamente um componente defeituoso.

D) Redundância e backup têm a mesma finalidade, o mesmo ponto de recuperação e o mesmo tempo de retorno.

### S2D6Q279 — Concorrência sem paralelismo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho que distingue intercalação concorrente de execução simultânea paralela.

Em um processador de núcleo único, o sistema alterna rapidamente as tarefas A e B. Ambas avançam durante o intervalo observado, mas apenas uma executa em cada instante. Como se classifica o cenário?

A) Paralelismo sem concorrência, porque as tarefas compartilham o intervalo de processamento.

B) Ausência de concorrência, porque a execução simultânea exige pelo menos dois núcleos.

C) Concorrência sem paralelismo, porque há intercalação sem execução simultânea real.

D) Concorrência com paralelismo, porque cada troca de contexto cria simultaneidade entre as tarefas.

### S2D6Q280 — Atualização perdida por condição de corrida

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente condição de corrida e atualização perdida em operação composta.

Duas threads executam sem sincronização `saldo = saldo + 10`. Ambas leem o saldo inicial de 100 e depois gravam 110, embora o resultado esperado fosse 120. O comportamento caracteriza:

A) deadlock, porque as duas threads acessaram o mesmo recurso e nenhuma atualização foi válida.

B) condição de corrida, porque a sequência de leitura, cálculo e escrita permitiu atualização perdida.

C) starvation, porque uma das threads ficou definitivamente impedida de executar no processador.

D) livelock, porque as duas threads desfizeram repetidamente a operação executada pela outra.

### S2D6Q281 — Mutex e propriedade da seção crítica

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho sobre exclusão mútua e propriedade do mutex.

Uma seção crítica deve admitir apenas uma thread por vez, e a thread que adquirir o controle deve liberá-lo ao sair. Qual mecanismo modela diretamente esse requisito?

A) Semáforo contador iniciado em oito, permitindo oito titulares simultâneos da seção.

B) Variável de condição usada sem mutex, tratando a notificação como propriedade exclusiva.

C) Barreira de sincronização, liberando todas as threads quando o mesmo ponto for alcançado.

D) Mutex compartilhado pelos participantes, com aquisição e liberação ao redor da seção crítica.

### S2D6Q282 — Condições necessárias de Coffman

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente as quatro condições necessárias de Coffman.

No modelo clássico de deadlock com recursos reutilizáveis, qual conjunto apresenta as quatro condições necessárias de Coffman?

A) Exclusão mútua, posse e espera, não preempção e espera circular.

B) Exclusão mútua, posse e espera, preempção obrigatória e espera circular.

C) Exclusão mútua, aquisição sem retenção, não preempção e espera circular.

D) Exclusão mútua, posse e espera, não preempção e ordem acíclica.

### S2D6Q283 — Starvation em prioridade estrita

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), nos trechos sobre starvation, aging e diferenças para outros problemas de progresso.

Em um escalonador de prioridade estrita, uma tarefa de baixa prioridade permanece pronta, mas novas tarefas de alta prioridade sempre a ultrapassam. As demais concluem normalmente. O fenômeno e uma mitigação são:

A) deadlock e ordenação global de locks, pois nenhum participante consegue avançar.

B) livelock e backoff, pois a tarefa executa repetidamente sem produzir resultado útil.

C) starvation e aging, pois a tarefa pode ser adiada indefinidamente enquanto outras avançam.

D) inversão de prioridade e herança, pois uma tarefa alta aguarda lock mantido pela baixa.

### S2D6Q284 — Round Robin

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento), com recuperação em [D6-RF-MX-10](semana_02_estudo.md#s2-d6-rf-mx-10)

Em Round Robin, reduzir demais o quantum tende a:

A) eliminar todas as trocas de contexto.
B) tornar FCFS.
C) impedir preempção.
D) aumentar overhead de trocas de contexto.

### S2D6Q285 — Polling e interrupção

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente a diferença entre consulta repetida por polling e sinalização por interrupção.

Polling e interrupção são formas de coordenar a CPU com um dispositivo de entrada e saída. Assinale a alternativa que distingue corretamente os mecanismos.

A) No polling, a CPU consulta o estado; na interrupção, o dispositivo sinaliza quando requer tratamento.

B) No polling, o dispositivo sinaliza a CPU; na interrupção, a CPU consulta periodicamente o estado.

C) Nos dois mecanismos, a CPU consulta em intervalos fixos; muda apenas a prioridade atribuída ao driver.

D) Na interrupção, o dispositivo transfere todo o bloco; no polling, ele apenas informa a conclusão.

### S2D6Q286 — Transferência em bloco por DMA

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho sobre DMA, configuração pela CPU e menor intervenção por unidade transferida.

A CPU informa endereço, direção e tamanho à controladora. Ela transfere um bloco entre dispositivo e memória e sinaliza a conclusão, sem a CPU copiar cada unidade. O mecanismo predominante é:

A) E/S programada, em que a CPU executa instruções para copiar cada palavra entre registrador e memória.

B) DMA, em que a controladora move o bloco com menor intervenção da CPU por unidade transferida.

C) E/S por interrupção, em que cada evento chama uma rotina para a CPU copiar individualmente a próxima palavra.

D) Polling, em que a CPU consulta o estado e transfere diretamente cada unidade quando o dispositivo fica pronto.

### S2D6Q287 — Commit e replay no journaling

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente commit, replay e limite do journaling perante histórico e falha física.

Após uma queda de energia, o sistema de arquivos examina o journal antes de montar o volume. Qual conduta representa a recuperação típica de consistência?

A) Reproduzir todas as transações, inclusive as que não possuem commit, para preservar o estado mais recente.

B) Reverter toda exclusão registrada e restaurar automaticamente cada versão anterior do conteúdo afetado.

C) Reproduzir transações confirmadas e ignorar as incompletas, recuperando a consistência das estruturas.

D) Reconstruir setores fisicamente ilegíveis a partir do journal, mesmo sem outra cópia dos dados do volume.

### S2D6Q288 — Permissões Linux

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), com recuperação em [D6-RF-MX-10](semana_02_estudo.md#s2-d6-rf-mx-10)

Em Linux, a permissão `640` indica:

A) dono lê/escreve, grupo lê, outros não têm acesso.
B) todos leem e escrevem.
C) dono executa, grupo escreve, outros leem.
D) nenhuma permissão para o dono.

### S2D6Q289 — ACEs em uma DACL do Windows

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho sobre DACL, ACEs de permissão ou negação e herança.

No modelo de controle de acesso do Windows, qual alternativa descreve corretamente uma DACL associada a um objeto?

A) Contém somente ACEs de auditoria; permissões e negações ficam exclusivamente na SACL.

B) Contém apenas ACEs de permissão; uma negação explícita não pode integrar essa lista.

C) Contém ACEs de permissão ou negação, inclusive entradas herdadas conforme a configuração.

D) Contém somente o SID do proprietário; as ACEs ficam armazenadas apenas no compartilhamento.

### S2D6Q290 — Alcance diagnóstico de um `ping` bem-sucedido

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05), no trecho sobre diagnóstico em camadas e limites do `ping` perante transporte e aplicação.

Um portal HTTPS não responde, mas `ping` enviado diretamente ao endereço IP do servidor recebe respostas. Qual conclusão orienta corretamente o próximo diagnóstico?

A) A aplicação está saudável, portanto a falha deve estar exclusivamente no cache do navegador cliente.

B) A resolução DNS está correta, portanto não é necessário consultar o nome usado para acessar o portal.

C) A porta TCP 443 está acessível, portanto o firewall e o processo HTTPS já foram integralmente validados.

D) Há alguma conectividade IP e ICMP, mas ainda é preciso testar porta, TLS, processo e aplicação.

### S2D6Q291 — Sincronização temporal e correlação de logs

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06), especialmente NTP, consistência de horários e correlação temporal entre registros.

Durante uma investigação, os relógios de três servidores apresentam diferenças de vários minutos. Qual atividade fica mais diretamente prejudicada por essa inconsistência?

A) Comparar o hash de um arquivo com um resumo confiável para detectar alteração de conteúdo.

B) Ordenar e correlacionar eventos dos servidores para reconstruir a linha do tempo do incidente.

C) Identificar a conta registrada explicitamente no campo de usuário de cada evento coletado.

D) Interpretar o código de severidade e o texto gravado pela fonte em cada registro local.

### S2D6Q292 — Independência das camadas de defesa

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08), no trecho sobre controles complementares e defesa em profundidade.

Uma organização combina atualização, MFA, segmentação, monitoramento e backup. Qual princípio justifica manter controles diferentes e complementares?

A) Um único controle bem configurado elimina o risco residual, e as demais camadas servem apenas para auditoria.

B) A defesa em profundidade reduz a dependência de uma única barreira quando um controle falha ou é contornado.

C) As camadas devem compartilhar fabricante e credencial administrativa para que uma decisão se propague a todas.

D) O backup substitui prevenção e detecção, pois qualquer comprometimento pode ser desfeito sem impacto adicional.

### S2D6Q293 — Dependências de um acesso HTTPS por HTTP/2

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05), especialmente DHCP, DNS, estabelecimento do transporte, TLS e HTTP.

Uma estação IPv4 recém-inicializada, sem configuração estática, acessará por nome um portal HTTPS usando HTTP/2 sobre TCP. Qual ordem representa as dependências principais até a requisição?

A) DHCP, conexão TCP, requisição HTTP, resolução DNS e handshake TLS.

B) Resolução DNS, DHCP, handshake TLS, conexão TCP e requisição HTTP.

C) DHCP, resolução DNS, conexão TCP, handshake TLS e requisição HTTP.

D) DHCP, resolução DNS, handshake TLS, requisição HTTP e conexão TCP.

### S2D6Q294 — Papel de um proxy reverso

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06), no trecho que diferencia proxy direto e proxy reverso.

Um intermediário recebe requisições de clientes externos destinadas a um portal, seleciona um servidor interno e devolve a resposta sem expor diretamente o backend. Esse papel corresponde a:

A) proxy direto, que representa clientes internos perante os servidores externos escolhidos por eles.

B) proxy transparente de saída, que intercepta tráfego de clientes sem configuração explícita no navegador.

C) proxy de cache de saída, que armazena respostas externas para reutilização por usuários internos.

D) proxy reverso, que representa os servidores publicados perante os clientes e encaminha ao backend.

### S2D6Q295 — Acesso a serviço de diretório por LDAP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06), especialmente a finalidade de LDAP em serviços de diretório.

Uma aplicação precisa consultar entradas hierárquicas de usuários, grupos e atributos mantidas em um serviço de diretório. Qual protocolo é diretamente associado a essa operação?

A) LDAP, usado para consultar e modificar entradas organizadas em serviço de diretório.

B) Kerberos, usado principalmente para emitir tíquetes de autenticação entre participantes.

C) RADIUS, usado principalmente em autenticação, autorização e accounting de acesso à rede.

D) DNS, usado para publicar e resolver nomes e outros registros distribuídos de recursos.

### S2D6Q296 — Porta convencional e prova de segurança

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05), no trecho que trata porta como associação convencional, e não prova de protocolo ou segurança.

Um laudo afirma que um serviço é seguro apenas porque aceita conexões na porta TCP 443. Qual avaliação técnica está correta?

A) A porta 443 força HTTPS e valida certificado automaticamente, independentemente do software que atende a conexão.

B) TLS só oferece proteção quando usa a porta 443, e qualquer porta alternativa impede autenticação e cifração.

C) A porta é uma convenção; é preciso verificar protocolo, TLS, certificado, configuração e segurança do endpoint.

D) A regra de firewall para a porta 443 encapsula em TLS qualquer conteúdo em claro enviado pela aplicação.

### S2D6Q297 — DDoS

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia), [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede) e [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07)

Assinale a situação que caracteriza mais diretamente indisponibilidade.

A) Alteração não autorizada de dado.
B) Divulgação de documento sigiloso.
C) Associação errada entre usuário e grupo.
D) DDoS que satura o enlace do órgão.

### S2D6Q298 — Preservação de imagem forense

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09), especialmente preservação de evidências antes de ações de erradicação.

Antes de erradicar malware, a equipe cria imagem bit a bit do disco, calcula hashes e registra a cadeia de custódia. Qual objetivo predomina nessa atividade?

A) Contenção, porque a criação da imagem bloqueia automaticamente toda comunicação do host comprometido.

B) Erradicação, porque a cópia bit a bit remove malware e persistência do equipamento original.

C) Preservação de evidência, porque hashes e custódia apoiam integridade e análise posterior reproduzível.

D) Recuperação, porque a imagem forense devolve automaticamente o host a um estado conhecido e limpo.

### S2D6Q299 — Comandos de observação

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), com recuperação em [D6-RF-MX-10](semana_02_estudo.md#s2-d6-rf-mx-10)

Qual ação é de observação, e não de alteração de processo?

A) `Get-Process`.
B) `Stop-Process`.
C) `kill`.
D) `taskkill`.

### S2D6Q300 — RPO, RTO, dependências e continuidade efetiva

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Recuperação por dependências e validação ponta a ponta](semana_02_estudo.md#s2-d6-recuperacao-dependencias) e [Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), nos trechos sobre RPO, RTO, dependências e validação do negócio.

Um incidente ocorre às 14h. O banco é restaurado ao ponto consistente das 13h35 e a infraestrutura volta às 16h30, mas a fila de pagamentos permanece incompatível e o serviço de autenticação necessário está indisponível. O plano define RPO de 30 minutos e RTO de 4 horas. Analise as afirmações.

I. O ponto das 13h35 atende ao RPO, mas esse resultado isolado não comprova a recuperação do serviço.

II. O horário das 16h30 está dentro da janela de RTO; contudo, enquanto fila e autenticação impedirem a transação de ponta a ponta, o serviço ainda não foi efetivamente restabelecido.

III. O teste de continuidade deve validar integridade, dependências, responsabilidades, comunicação e retorno controlado; a existência do backup não substitui essas verificações.

Está correto o que se afirma em:

A) I e II, apenas.

B) I, II e III.

C) I e III, apenas.

D) II e III, apenas.

## Questões extras de revisão fixa do Dia 6
#### Extra Dia 6.1
- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** ideia central.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-01).

No trecho “A segmentação ajuda, mas não substitui MFA”, a ideia central é que:

A) MFA é dispensável.
B) controles são complementares.
C) segmentação impede todo ataque.
D) segurança é binária.
#### Extra Dia 6.2

- **Dia:** Dia 6

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** inferência.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [D6-RF-PT-02 — Inferência](semana_02_estudo.md#s2-d6-rf-pt-02), aplicada à ausência de garantias nativas do UDP.

A documentação afirma: “UDP não oferece retransmissão nativa”. Qual inferência respeita o alcance dessa afirmação?

A) A aplicação fica impedida de criar confirmações, temporizadores ou retransmissões para os próprios dados.

B) Qualquer perda será corrigida automaticamente pela camada de transporte antes de alcançar a aplicação.

C) A aplicação pode criar confirmações, temporizadores ou retransmissões quando o serviço precisar deles.

D) A ausência de retransmissão nativa garante que cada datagrama será entregue uma única vez ao destino.

#### Extra Dia 6.3
- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** conectores.
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-03).

Em “Embora o host responda, o serviço falhou porque houve deadlock”, os conectores indicam:

A) concessão e causa.
B) causa e finalidade.
C) conclusão e oposição.
D) condição e explicação.
#### Extra Dia 6.4

- **Dia:** Dia 6

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** ambiguidade.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [D6-RF-PT-04 — Ambiguidade](semana_02_estudo.md#s2-d6-rf-pt-04), na orientação de explicitar o referente.

Em “A analista informou à gerente que seu acesso expirou”, o possessivo admite duas referentes. Qual intervenção elimina efetivamente a ambiguidade?

A) Retirar “seu” e escrever apenas “o acesso expirou”, sem identificar a pessoa a quem o acesso pertence.

B) Deslocar “seu” para depois de “expirou”, mantendo analista e gerente como antecedentes possíveis.

C) Flexionar o possessivo no plural e conservar as duas pessoas no período, sem indicar a titular do acesso.

D) Substituir “seu acesso” por “o acesso da analista” ou “o acesso da gerente”, conforme o sentido pretendido.

#### Extra Dia 6.5

- **Dia:** Dia 6

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** modalidade.

- **Nível:** Médio

- **Uso:** Essenciais

- **Referência:** [D6-RF-PT-05 — Modalidade](semana_02_estudo.md#s2-d6-rf-pt-05), na distinção entre possibilidade, obrigação e garantia.

No relatório consta que “o IDS pode alertar sobre o evento”. Qual leitura conserva a força modal do verbo empregado?

A) O verbo assegura que o IDS detectará e alertará sobre todos os eventos, sem exceção operacional.

B) O verbo expressa possibilidade ou capacidade de alertar, sem prometer detecção universal dos eventos.

C) O verbo afirma que o IDS sempre bloqueará o evento antes de qualquer alerta aos responsáveis.

D) O verbo impõe ao IDS a obrigação de emitir alerta e torna impossível a ausência de detecção.

#### Extra Dia 6.6

- **Dia:** Dia 6

- **Bloco:** Bloco 5

- **Matéria:** Língua Portuguesa

- **Assunto:** reescrita.

- **Nível:** Médio

- **Uso:** Aprofundamento

- **Referência:** [D6-RF-PT-06 — Reescrita](semana_02_estudo.md#s2-d6-rf-pt-06), na preservação da concessão e da orientação principal.

Qual alternativa preserva o sentido de “Ainda que o backup esteja íntegro, teste a restauração”?

A) Como o backup está íntegro, o teste de restauração deve ser dispensado pela equipe responsável.

B) O teste de restauração deve ocorrer somente quando houver indício anterior de corrupção no backup.

C) Mesmo que o backup esteja íntegro, a equipe deve realizar o teste de restauração previsto.

D) A realização do teste torna o backup íntegro e substitui a verificação posterior da restauração.

#### Extra Dia 6.7
- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-07).

Assinale a frase correta.

A) Haviam falhas e existe controles.
B) Havia falhas e existem controles.
C) Houveram falhas e existe controles.
D) Haviam falhas e existia controles.
#### Extra Dia 6.8
- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** crase.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-08).

Assinale o emprego correto de regência e crase.

A) Obedeceu à política e começou à analisar registros.
B) Obedeceu a política e começou à analisar registros.
C) Referiu-se as regras e à todos.
D) Obedeceu à política e começou a analisar registros.
#### Extra Dia 6.9
- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pontuação.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-09).

Assinale a pontuação adequada.

A) Após a contenção, a equipe preservou os registros.
B) A equipe preservou, registros essenciais.
C) Os administradores, revogaram credenciais.
D) Os servidores vulneráveis, foram isolados.
#### Extra Dia 6.10
- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** paralelismo.
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-10).

Há paralelismo adequado em:

A) Isolar hosts, a revogação de credenciais e preservar logs.
B) Isolar hosts, revogar credenciais e a preservação de logs.
C) Isolar hosts, que credenciais sejam revogadas e logs.
D) Isolar hosts, revogar credenciais e preservar logs.
#### Extra Dia 6.11

- **Dia:** Dia 6

- **Bloco:** Bloco 4

- **Matéria:** Redes de Computadores

- **Assunto:** métricas.

- **Nível:** Médio

- **Uso:** Revisão

- **Referência:** [D6-RF-MX-01 — Recuperação ativa de redes e métricas](semana_02_estudo.md#s2-d6-rf-mx-01), na distinção entre latência, jitter, throughput, goodput e largura de banda.

Em quatro medições consecutivas, a latência de um fluxo foi de 20 ms, 35 ms, 18 ms e 42 ms. Qual métrica descreve a oscilação observada entre esses atrasos?

A) Jitter, porque mede a variação do atraso entre as medições do fluxo.

B) Throughput, porque mede a quantidade total de bits transmitida por unidade de tempo.

C) Goodput, porque mede a parcela de dados úteis entregue à aplicação no intervalo.

D) Largura de banda, porque mede a capacidade nominal disponível no enlace utilizado.

#### Extra Dia 6.12

- **Dia:** Dia 6

- **Bloco:** Bloco 4

- **Matéria:** Redes de Computadores

- **Assunto:** encapsulamento.

- **Nível:** Médio

- **Uso:** Revisão

- **Referência:** [D6-RF-MX-02 — Camadas, encapsulamento e evidência](semana_02_estudo.md#s2-d6-rf-mx-02), na renovação do quadro a cada enlace roteado.

Um roteador recebe um quadro Ethernet e deve encaminhar o pacote IP por outro enlace Ethernet. Qual operação descreve corretamente essa passagem?

A) Reutiliza o quadro recebido e mantém os endereços MAC de origem e destino durante todo o caminho IP.

B) Remove o quadro recebido, examina o pacote IP e cria um novo quadro adequado ao próximo enlace.

C) Remove também o pacote IP e encaminha somente a carga da aplicação dentro do mesmo quadro recebido.

D) Mantém o quadro de enlace intacto e troca os endereços IP do pacote a cada salto percorrido.

#### Extra Dia 6.13
- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Redes de Computadores
- **Assunto:** CIDR.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-03).

Para `192.168.10.77/27`, a rede é:

A) `192.168.10.0`.
B) `192.168.10.32`.
C) `192.168.10.64`.
D) `192.168.10.77`.
#### Extra Dia 6.14
- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Redes de Computadores
- **Assunto:** gateway.
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-04).

Para destino IPv4 remoto, o host resolve por ARP o MAC:

A) do gateway local.
B) do destino remoto.
C) do DNS.
D) do NAT.
#### Extra Dia 6.15

- **Dia:** Dia 6

- **Bloco:** Bloco 4

- **Matéria:** Redes de Computadores

- **Assunto:** fluxo de protocolos.

- **Nível:** Médio

- **Uso:** Revisão

- **Referência:** [D6-RF-MX-05 — Protocolos: transporte, Web, nomes e configuração](semana_02_estudo.md#s2-d6-rf-mx-05), na regra de integração entre os quatro protocolos.

Em uma sequência simplificada de acesso Web, qual alternativa associa corretamente DHCP, DNS, TLS e HTTP às respectivas funções?

A) DHCP resolve nomes; DNS configura o cliente; TLS expressa a aplicação Web; HTTP protege criptograficamente o canal.

B) DHCP configura o cliente; DNS resolve nomes; TLS protege o canal; HTTP expressa a aplicação Web.

C) DHCP protege o canal; DNS expressa a aplicação Web; TLS configura o cliente; HTTP resolve nomes.

D) DHCP expressa a aplicação Web; DNS protege o canal; TLS resolve nomes; HTTP configura o cliente.

#### Extra Dia 6.16
- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Redes de Computadores
- **Assunto:** serviços de rede.
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

Assinale a associação correta.

A) SMTP lê caixa; IMAP envia; SFTP é FTP sem cifra.
B) NTP entrega IP; SNMP resolve nomes.
C) SMTP envia; IMAP acessa caixa; SFTP usa SSH.
D) LDAP traduz portas; PAT lista diretórios.
#### Extra Dia 6.17

- **Dia:** Dia 6

- **Bloco:** Bloco 4

- **Matéria:** Segurança da Informação

- **Assunto:** risco.

- **Nível:** Médio

- **Uso:** Simulado

- **Referência:** [D6-RF-MX-07 — Segurança: objetivo, identidade, risco e ataque](semana_02_estudo.md#s2-d6-rf-mx-07), nas definições de vulnerabilidade, ameaça e risco.

Uma biblioteca contém falha explorável; um código malicioso pode explorá-la; a organização avalia a probabilidade e o impacto dessa exploração. Os três elementos são, respectivamente:

A) vulnerabilidade, risco e ameaça.

B) ameaça, risco e vulnerabilidade.

C) risco, vulnerabilidade e ameaça.

D) vulnerabilidade, ameaça e risco.

#### Extra Dia 6.18

- **Dia:** Dia 6

- **Bloco:** Bloco 4

- **Matéria:** Segurança da Informação

- **Assunto:** controles.

- **Nível:** Difícil

- **Uso:** Simulado

- **Referência:** [D6-RF-MX-08 — Controles, criptografia e Wi-Fi](semana_02_estudo.md#s2-d6-rf-mx-08), nas distinções firewall × IDS × IPS e HMAC × assinatura digital.

Uma arquitetura usa IPS em linha e HMAC nas mensagens entre dois serviços. Assinale a alternativa que descreve corretamente os dois controles.

A) O IPS em linha pode bloquear tráfego; o HMAC usa par de chaves pública e privada como uma assinatura digital.

B) O IPS em linha pode bloquear tráfego; o HMAC usa segredo compartilhado para verificar integridade e autenticidade.

C) O IPS em linha apenas alerta, sem atuar no fluxo; o HMAC usa segredo compartilhado para verificar integridade e autenticidade.

D) O IPS em linha substitui qualquer firewall; o HMAC cifra reversivelmente a mensagem com o segredo compartilhado.

#### Extra Dia 6.19

- **Dia:** Dia 6

- **Bloco:** Bloco 4

- **Matéria:** Continuidade de Serviços

- **Assunto:** RPO e RTO.

- **Nível:** Difícil

- **Uso:** Simulado

- **Referência:** [D6-RF-MX-09 — Resposta, continuidade e objetivos de recuperação](semana_02_estudo.md#s2-d6-rf-mx-09), nas definições e no exemplo de RPO e RTO.

Um incidente começa às 14h. O serviço possui RPO de 30 minutos e RTO de 2 horas. Qual resultado atende simultaneamente aos dois objetivos?

A) Recuperar dados de um ponto não anterior a 13h30 e restabelecer o serviço até as 16h.

B) Recuperar dados de um ponto às 13h e restabelecer o serviço até as 14h30.

C) Recuperar dados de um ponto não anterior a 13h30 e restabelecer o serviço até as 17h.

D) Recuperar dados de um ponto não anterior a 12h e restabelecer o serviço até as 14h30.

#### Extra Dia 6.20

- **Dia:** Dia 6

- **Bloco:** Bloco 4

- **Matéria:** Sistemas Operacionais

- **Assunto:** E/S e journaling.

- **Nível:** Difícil

- **Uso:** Simulado

- **Referência:** [D6-RF-MX-10 — Sistemas operacionais: progresso, E/S e persistência](semana_02_estudo.md#s2-d6-rf-mx-10), nas linhas polling/interrupção/DMA e sistema de arquivos/journaling.

Ao documentar entrada/saída e recuperação do sistema de arquivos, a equipe compara interrupção, DMA e journaling. Qual síntese está correta?

A) A interrupção exige polling contínuo; o DMA transfere cada byte pela CPU; o journaling funciona como cópia histórica dos arquivos.

B) A interrupção sinaliza eventos; o DMA reduz intervenção da CPU; o journaling garante ausência de perda e substitui o backup.

C) A interrupção sinaliza eventos; o DMA elimina toda atuação da CPU; o journaling auxilia a recuperar consistência após falha.

D) A interrupção evita polling contínuo; o DMA reduz intervenção da CPU; o journaling auxilia a recuperar consistência após falha.

## Gabarito do Dia 6

### Questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | D |
| 2 | A |
| 3 | A |
| 4 | C |
| 5 | D |
| 6 | B |
| 7 | A |
| 8 | C |
| 9 | A |
| 10 | B |
| 11 | D |
| 12 | C |
| 13 | B |
| 14 | D |
| 15 | A |
| 16 | C |
| 17 | B |
| 18 | B |
| 19 | A |
| 20 | D |
| 21 | C |
| 22 | B |
| 23 | C |
| 24 | A |
| 25 | D |
| 26 | B |
| 27 | D |
| 28 | A |
| 29 | C |
| 30 | B |
| 31 | D |
| 32 | A |
| 33 | C |
| 34 | D |
| 35 | A |
| 36 | B |
| 37 | C |
| 38 | A |
| 39 | C |
| 40 | D |
| 41 | B |
| 42 | B |
| 43 | C |
| 44 | D |
| 45 | A |
| 46 | C |
| 47 | D |
| 48 | C |
| 49 | A |
| 50 | B |

### Questões extras

| Extra | Resposta |
|---:|:---:|
| 6.1 | B |
| 6.2 | C |
| 6.3 | A |
| 6.4 | D |
| 6.5 | B |
| 6.6 | C |
| 6.7 | B |
| 6.8 | D |
| 6.9 | A |
| 6.10 | D |
| 6.11 | A |
| 6.12 | B |
| 6.13 | C |
| 6.14 | A |
| 6.15 | B |
| 6.16 | C |
| 6.17 | D |
| 6.18 | B |
| 6.19 | A |
| 6.20 | D |


## Comentários do Dia 6

### Comentário S2D6Q251

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** latência é o tempo de atraso entre envio e recebimento, normalmente medido em unidades de tempo; não é a taxa de dados úteis entregue à aplicação.
- **B)** jitter é a variação da latência entre entregas sucessivas, e não uma vazão expressa em Mbit/s.
- **C)** perda representa dados que não chegaram ao destino, por quantidade ou proporção; não denomina a taxa útil recebida.
- **D)** goodput mede a taxa efetivamente útil percebida pela aplicação, depois de descontadas sobrecargas como cabeçalhos e retransmissões. Por isso, os 700 Mbit/s de dados úteis são goodput, enquanto 1 Gbit/s é a capacidade nominal do enlace.

**Conceito:** largura de banda, throughput, goodput, latência, jitter e perda.

**Pegadinha:** tratar toda medida de desempenho como “velocidade” e ignorar tanto a unidade quanto o ponto em que ela é observada.

**Como pensar:** classifique primeiro a grandeza: capacidade nominal é largura de banda; taxa transportada é throughput; parcela útil recebida pela aplicação é goodput; tempo é latência; variação do tempo é jitter.

**Referência:** [Comunicação de dados e medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados), com recuperação em [D6-RF-MX-01](semana_02_estudo.md#s2-d6-rf-mx-01).
### Comentário S2D6Q252

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** o switch associa MAC de origem à porta, seleciona saídas para unicast conhecido e separa segmentos, enquanto a VLAN permanece domínio de broadcast.
- **B)** a aprendizagem usa o MAC de origem, e broadcast continua sendo inundado nas portas pertinentes da mesma VLAN.
- **C)** acerta aprendizagem e unicast conhecido, mas cada porta segmenta o enlace em relação às demais, não conserva um domínio de colisão único.
- **D)** repetição de bits sem tabela MAC e meio de colisão compartilhado descrevem um hub Ethernet legado.

**Conceito:** aprendizagem da tabela MAC e diferença entre segmentação de colisão e propagação de broadcast.

**Pegadinha:** transferir automaticamente ao domínio de broadcast a separação que o switch produz entre segmentos de colisão.

**Como pensar:** compare três equipamentos: hub repete bits, switch decide por MAC e roteador separa redes; depois trate colisão e broadcast separadamente.

**Referência:** [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch), nos comportamentos de aprendizagem e encaminhamento; e [Domínios de colisão e broadcast](semana_02_estudo.md#s2-d1-dominios).

### Comentário S2D6Q253

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** ao receber o quadro, o roteador remove o encapsulamento do enlace de entrada, examina o pacote IP e o encapsula em um novo quadro adequado ao próximo enlace.
- **B)** rotear um pacote não converte automaticamente o protocolo de transporte. Um segmento TCP permanece associado ao TCP salvo atuação específica de outro mecanismo, que o enunciado não descreve.
- **C)** endereços MAC identificam os extremos do enlace atual; eles mudam quando o pacote é reenquadrado para outro salto e não são preservados fim a fim.
- **D)** a aplicação recebe dados depois do processamento e do desencapsulamento pelas camadas da pilha; não recebe diretamente sinais ou bits brutos do enlace.

**Conceito:** encapsulamento por camada e recriação do quadro a cada enlace roteado.

**Pegadinha:** confundir o pacote IP, que atravessa a rota com ajustes próprios, com o quadro de enlace, cuja validade é local.

**Como pensar:** separe as unidades: quadro/MAC no enlace, pacote/IP entre redes e segmento ou datagrama no transporte. Ao mudar de enlace, o quadro precisa mudar.

**Referência:** [Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento), com recuperação em [D6-RF-MX-02](semana_02_estudo.md#s2-d6-rf-mx-02).
### Comentário S2D6Q254

**Nível:** Difícil

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** rede `.0` e broadcast `.255` correspondem ao bloco /24 inteiro, não ao /26 indicado.
- **B)** `.64` a `.127` é o bloco /26 anterior. O último octeto 130 já pertence ao bloco iniciado em 128.
- **C)** /26 corresponde à máscara 255.255.255.192, cujo tamanho de bloco é `256 − 192 = 64`. Os blocos começam em 0, 64, 128 e 192; 130 cai em 128–191, logo rede é `.128` e broadcast é `.191`.
- **D)** `.130` é um host do bloco, não seu endereço de rede; `.192` é o início do bloco seguinte, não o broadcast do bloco atual.

**Conceito:** cálculo de rede e broadcast em sub-rede IPv4 CIDR.

**Pegadinha:** usar o próximo múltiplo como broadcast, sem subtrair um, ou tomar o próprio IP como endereço de rede.

**Como pensar:** converta /26 em 255.255.255.192, calcule bloco 64, localize o intervalo que contém 130 e use início como rede e próximo início menos um como broadcast.

**Referência:** [Rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts) e [Cálculos resolvidos de CIDR](semana_02_estudo.md#s2-d2-calculos).
### Comentário S2D6Q255

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** o servidor está fora da sub-rede; seu MAC não é descoberto através dos roteadores. O endereço IP continua sendo do destino remoto, mas o primeiro quadro é dirigido ao próximo salto local.
- **B)** DNS autoritativo publica dados da zona e não fornece o endereço MAC necessário ao enlace local.
- **C)** o switch encaminha o quadro de forma transparente; o host não usa o MAC do switch de acesso como próximo salto IP.
- **D)** após concluir que o destino é remoto, o host consulta ou usa o cache ARP para associar o IPv4 do gateway ao MAC da interface local do roteador e envia o quadro a esse endereço.

**Conceito:** decisão de entrega remota e resolução ARP do próximo salto.

**Pegadinha:** procurar o MAC do destino final, em vez do MAC do gateway que é alcançável no enlace local.

**Como pensar:** compare destino e prefixo local. Se forem redes diferentes, mantenha o IP remoto no pacote, mas obtenha por ARP o MAC do gateway para o primeiro quadro.

**Referência:** [Gateway padrão](semana_02_estudo.md#s2-d2-gateway) e [ARP](semana_02_estudo.md#s2-d2-arp).
### Comentário S2D6Q256

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** IPv6 não usa o ARP do IPv4 nem possui broadcast; a resolução de vizinhança integra o ND.
- **B)** ND pertence ao ICMPv6 e usa NS/NA, além de multicast específico, para resolução e manutenção da vizinhança.
- **C)** DHCPv6 pode fornecer configuração, mas não substitui as funções de descoberta e alcançabilidade de vizinhos.
- **D)** registro AAAA fornece endereço IPv6 associado a nome, não o endereço de enlace de um vizinho local.

**Conceito:** Neighbor Discovery como mecanismo ICMPv6 para descoberta de enlace e alcançabilidade.

**Pegadinha:** transportar ARP e broadcast do IPv4 ao IPv6 ou confundir endereço IP obtido por DNS com endereço de enlace.

**Como pensar:** ao ler “vizinho IPv6”, associe imediatamente ND, ICMPv6, NS/NA e multicast solicited-node.

**Referência:** [ICMP e ICMPv6 — Neighbor Discovery, NS e NA](semana_02_estudo.md#s2-d2-icmp) e [IPv6](semana_02_estudo.md#s2-d2-ipv6), incluindo a ausência de broadcast no IPv6.

### Comentário S2D6Q257

**Nível:** Difícil

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** I é verdadeira porque o TCP oferece confirmação, retransmissão e entrega ordenada do fluxo; III também é verdadeira porque uma aplicação sobre UDP pode acrescentar confirmações, controle de perda e ordenação próprios.
- **B)** inclui II, que é falsa: UDP não fornece retransmissão nativa.
- **C)** mantém a falsa II e exclui I, embora confirmação e ordenação sejam propriedades do TCP.
- **D)** considera verdadeira a assertiva II; a ausência de garantias nativas é precisamente uma característica do UDP.

**Conceito:** garantias de transporte do TCP, ausência de garantias nativas do UDP e responsabilidades da aplicação.

**Pegadinha:** transformar “UDP não retransmite nativamente” em “nenhuma aplicação sobre UDP pode ser confiável”.

**Como pensar:** julgue cada assertiva isoladamente e separe o que o protocolo oferece do que a aplicação pode construir sobre ele: I verdadeira, II falsa, III verdadeira.

**Referência:** [TCP e UDP](semana_02_estudo.md#s2-d3-tcp-udp), com síntese em [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05).
### Comentário S2D6Q258

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** HTTP/3 muda o transporte para QUIC sobre UDP; TCP é a associação usual de HTTP/1.1 e HTTP/2.
- **B)** acerta QUIC/UDP, mas o acesso HTTPS usa normalmente 443 e mantém proteção criptográfica.
- **C)** QUIC opera sobre UDP e provê à conexão HTTP/3 os mecanismos necessários, normalmente na porta 443.
- **D)** QUIC não é dispensado nem existe uma conexão TCP paralela obrigatória para fornecer a confiabilidade do HTTP/3.

**Conceito:** associação entre HTTP/3, QUIC, UDP e porta usual 443.

**Pegadinha:** aplicar a regra histórica “HTTP usa TCP” ou imaginar que UDP elimine confiabilidade e proteção da pilha superior.

**Como pensar:** recupere o conjunto completo: HTTP/3 → QUIC → UDP → normalmente 443.

**Referência:** [HTTP e HTTPS](semana_02_estudo.md#s2-d3-http-https), nos trechos que distinguem HTTP/1.1 e HTTP/2 em TCP de HTTP/3 sobre QUIC/UDP; e [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário S2D6Q259

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** o cliente primeiro descobre servidores, recebe oferta, solicita formalmente a escolhida e recebe a confirmação da concessão.
- **B)** servidor não oferece antes de o cliente anunciar a descoberta, e a confirmação não antecede a solicitação.
- **C)** o cliente precisa receber uma oferta antes de enviar o pedido referente à concessão escolhida.
- **D)** uma solicitação não inicia a sequência clássica antes da descoberta e da oferta correspondente.

**Conceito:** expansão e ordem cronológica de DORA no DHCPv4.

**Pegadinha:** reconhecer as quatro mensagens verdadeiras, mas aceitar uma permutação incompatível com o diálogo cliente-servidor.

**Como pensar:** conte a conversa: cliente procura, servidor oferece, cliente pede e servidor confirma.

**Referência:** [DHCP — sequência DORA](semana_02_estudo.md#s2-d3-dhcp), na lista ordenada das mensagens; e [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário S2D6Q260

**Nível:** Médio

**Uso:** Essenciais

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** DNS publica vários tipos de dados e usa TCP, por exemplo, em transferências de zona e outras condições que o exijam.
- **B)** o sistema distribuído trabalha com registros diversos, e seu transporte clássico contempla tanto UDP quanto TCP na porta 53.
- **C)** resolvedor recursivo não se torna autoridade da zona e pode reutilizar cache enquanto o TTL permanecer válido.
- **D)** DNSSEC busca autenticidade e integridade dos dados, não confidencialidade, e não elimina TCP do DNS clássico.

**Conceito:** finalidade do DNS e coexistência de UDP e TCP no transporte clássico.

**Pegadinha:** reduzir DNS a nome→IPv4 e 53/UDP ou atribuir confidencialidade ao DNSSEC.

**Como pensar:** lembre três dimensões independentes: tipos de registro, papel de autoridade/recursão/cache e transporte UDP mais TCP.

**Referência:** [DNS](semana_02_estudo.md#s2-d3-dns), nas subseções de componentes, registros, cache/TTL e transportes; e [D6-RF-MX-05](semana_02_estudo.md#s2-d6-rf-mx-05).

### Comentário S2D6Q261

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** SMTP não oferece sincronização de caixa, e POP3 não é o mecanismo de transferência entre MTAs nem preserva pastas compartilhadas.
- **B)** inverte os papéis; IMAP acessa a caixa, enquanto SMTP não sincroniza pastas do usuário.
- **C)** POP3 não é protocolo de submissão, e IMAP não transfere mensagens entre servidores de correio.
- **D)** SMTP movimenta a mensagem na submissão e entrega, e IMAP mantém no servidor o estado necessário ao acesso por vários clientes.

**Conceito:** separação entre envio por SMTP e acesso sincronizado por IMAP.

**Pegadinha:** atribuir a qualquer protocolo de e-mail todas as etapas ou trocar movimentação da mensagem por acesso à caixa.

**Como pensar:** divida a necessidade em verbos: enviar/submeter aponta para SMTP; acessar e sincronizar no servidor aponta para IMAP.

**Referência:** [Correio eletrônico — SMTP, POP3 e IMAP](semana_02_estudo.md#s2-d3-email), nas subseções de funções e fluxo integrado; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário S2D6Q262

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** FTP acrescido de TLS explícito é FTPS; SFTP pertence à família SSH e não inicia como FTP em 21/TCP.
- **B)** FTPS preserva o protocolo FTP e usa TLS, não é o subsistema de arquivos do SSH.
- **C)** SFTP opera sobre transporte SSH, normalmente em 22/TCP, e pode aproveitar as chaves e políticas de autenticação desse serviço.
- **D)** Telnet é protocolo distinto e não fornece a proteção criptográfica nativa oferecida pelo SSH.

**Conceito:** SFTP como protocolo de transferência sobre SSH, distinto de FTPS e Telnet.

**Pegadinha:** interpretar a letra “S” como simples versão TLS do FTP ou fundir protocolos que oferecem acesso remoto.

**Como pensar:** mantenha as famílias: SFTP/SSH usam 22; FTPS é FTP+TLS; Telnet é terminal sem a proteção esperada.

**Referência:** [FTP, FTPS, SFTP, SSH e Telnet](semana_02_estudo.md#s2-d3-transferencia-remota), especialmente as subseções SFTP e SSH e a distinção para FTPS; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário S2D6Q263

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** MIB não é endereço de rede, e OID identifica objeto; community string é outro elemento usado em versões como v1/v2c.
- **B)** a MIB descreve a organização lógica dos objetos, e o OID fornece o identificador do contador consultado.
- **C)** inverte estrutura e identificador, além de confundir OID com as operações realizadas sobre o objeto.
- **D)** MIB/OID descrevem o que é gerenciado e não substituem mecanismos de autenticação, privacidade e autorização do SNMPv3.

**Conceito:** finalidade complementar da MIB e do OID na gerência SNMP.

**Pegadinha:** trocar hierarquia por identificador ou transformar metadados de gerenciamento em credenciais de segurança.

**Como pensar:** leia MIB como catálogo/estrutura e OID como o endereço lógico de uma entrada específica nesse catálogo.

**Referência:** [SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp), nas definições de gerente, agente, MIB, OID e operações; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário S2D6Q264

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** inverte a distinção; NAT básico traduz endereço, e PAT acrescenta os identificadores de transporte.
- **B)** sem portas ou outro identificador único, fluxos iguais no mesmo endereço público não poderiam ser demultiplexados adequadamente.
- **C)** PAT normalmente inclui tradução de endereço e depende de estado/mapeamento para encaminhar cada retorno ao host correto.
- **D)** portas públicas diferentes permitem multiplexar as conexões e relacionar cada resposta à origem interna correspondente.

**Conceito:** tradução adicional de portas e multiplexação de fluxos pelo PAT/NAPT.

**Pegadinha:** usar NAT como termo amplo e esquecer a diferença específica pedida ou imaginar tradução sem tabela de retorno.

**Como pensar:** procure o campo extra que torna únicas conexões sob o mesmo IP público: a porta de transporte traduzida.

**Referência:** [NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat), nas definições e no exemplo da tabela com portas públicas diferentes; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário S2D6Q265

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** NTP alinha a referência temporal usada pelos sistemas, enquanto a apresentação local depende de fuso e regras de horário.
- **B)** o protocolo sincroniza relógios e usa convencionalmente UDP, não apenas distribuição de fuso por TCP.
- **C)** TTL controla o reaproveitamento de dados DNS em cache e não serve como fonte de tempo para NTP.
- **D)** NTP atua nos relógios dos hosts; não é ferramenta posterior de reordenação dos arquivos de log.

**Conceito:** finalidade e porta do NTP e distinção entre sincronização temporal e fuso local.

**Pegadinha:** tentar corrigir apenas a forma de exibição ou relacionar TTL de registros à referência do relógio.

**Como pensar:** diferencie instante e apresentação: NTP sincroniza o instante; fuso determina como esse instante aparece ao usuário.

**Referência:** [NTP — sincronização de tempo](semana_02_estudo.md#s2-d3-ntp), nos trechos sobre 123/UDP, correlação de logs e diferença entre referência e fuso; e [D6-RF-MX-06](semana_02_estudo.md#s2-d6-rf-mx-06).

### Comentário S2D6Q266

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** disponibilidade é a propriedade de acesso oportuno ao serviço ou dado, não a combinação entre chance de exploração e consequência.
- **B)** auditoria examina registros, controles e conformidade; não denomina a exposição resultante de ameaça, vulnerabilidade e impacto.
- **C)** no modelo operacional estudado, risco expressa a possibilidade de uma ameaça explorar uma vulnerabilidade e causar impacto; probabilidade e impacto sustentam sua análise e priorização.
- **D)** não repúdio é a capacidade de produzir evidência contra a negação falsa de uma ação, e não uma medida de risco.

**Conceito:** distinção entre vulnerabilidade, ameaça, impacto e risco.

**Pegadinha:** trocar um conceito de gestão de risco por uma propriedade de segurança ou por um mecanismo de controle.

**Como pensar:** identifique os papéis: vulnerabilidade é fraqueza; ameaça é causa potencial; impacto é consequência; a combinação analisada para decidir tratamento é risco.

**Referência:** [Conceitos de risco](semana_02_estudo.md#s2-d4-conceitos-risco), com recuperação em [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07).
### Comentário S2D6Q267

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** troca as perguntas; identidade pertence à autenticação, e permissão pertence à autorização.
- **B)** credenciais válidas permitem autenticar, mas a política de função pode negar a ação durante a autorização.
- **C)** registro e exame de ações pertencem a accounting/auditoria; não repúdio é propriedade distinta.
- **D)** validação de credencial é autenticação, enquanto a atribuição/uso de papéis participa da decisão de autorização.

**Conceito:** diferença lógica entre provar quem é o sujeito e decidir o que ele pode fazer.

**Pegadinha:** presumir que login bem-sucedido concede automaticamente toda ação ou inverter os componentes AAA.

**Como pensar:** faça duas perguntas em ordem: “quem é?” para autenticação; “pode fazer isso?” para autorização.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria), nas subseções 3.1 e 3.2; e [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07).

### Comentário S2D6Q268

**Nível:** Difícil

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** a primeira parte admite corretamente captura passiva, mas spoofing é definido pela falsificação e não exige controlar todos os pacotes do caminho.
- **B)** mantém os verbos definidores separados — falsificar no spoofing e interpor-se, interceptar e possivelmente alterar no on-path.
- **C)** sniffing não requer alteração, e on-path descreve posição/intermediação no fluxo, não apenas falsificação de origem fora dele.
- **D)** acerta spoofing, porém um atacante on-path pode observar e potencialmente modificar a comunicação interceptada.

**Conceito:** distinção entre falsificação de identidade, captura de tráfego e interposição ativa no caminho.

**Pegadinha:** tratar técnicas que podem ser combinadas como sinônimos ou tornar alteração requisito de toda observação.

**Como pensar:** associe um verbo a cada técnica: sniffing captura, spoofing falsifica e on-path interpõe-se no fluxo.

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede), nas subseções de spoofing, sniffing e ataque on-path; e [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07).

### Comentário S2D6Q269

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** IDS pode receber tráfego espelhado, detectar e alertar sem ocupar posição capaz ou obrigada a bloquear.
- **B)** a descrição funcional é de IDS; IPS caracteriza-se pela capacidade preventiva em linha ou posição equivalente.
- **C)** bloqueio necessário de pacotes é comportamento de prevenção, não requisito definidor de um IDS.
- **D)** IDS e IPS possuem posições e capacidades diferentes e nenhum deles garante detectar ou bloquear todo ataque.

**Conceito:** diferença operacional entre detecção/alerta por IDS e prevenção em linha por IPS.

**Pegadinha:** selecionar o controle mais interventivo sem observar que o requisito exclui bloqueio obrigatório.

**Como pensar:** destaque os verbos: “detectar e alertar” aponta para IDS; “interromper em linha” apontaria para IPS.

**Referência:** [IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips), nas subseções que contrastam monitoramento/alerta com prevenção em linha; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário S2D6Q270

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** unir exposição pública e ativos internos amplia movimento lateral e elimina uma barreira de segmentação importante.
- **B)** retirar o portal do perímetro e liberar qualquer destino elimina controles justamente onde a exposição é maior.
- **C)** DMZ é zona de exposição controlada e não fonte automaticamente confiável para acesso irrestrito à rede interna.
- **D)** a DMZ recebe o serviço exposto, enquanto regras mínimas e explícitas limitam o que um eventual comprometimento alcançaria internamente.

**Conceito:** DMZ como segmento intermediário com comunicação interna estritamente necessária.

**Pegadinha:** interpretar DMZ como rede sem filtros ou como justificativa para confiar no serviço exposto.

**Como pensar:** presuma o portal comprometível e pergunte qual opção reduz o caminho até os dados ao mínimo funcional documentado.

**Referência:** [DMZ](semana_02_estudo.md#s2-d4-dmz), nos princípios de exposição intermediária, fluxo mínimo e presunção de possível comprometimento; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário S2D6Q271

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** na questão, a VPN está corretamente configurada e operacional; proteger o tráfego em trânsito dentro do escopo do túnel é justamente uma de suas funções.
- **B)** a autenticação usada para estabelecer o túnel pode integrar a solução VPN e foi dada como configurada no cenário; isso não equivale a autorizar todas as operações nas aplicações.
- **C)** a VPN protege o canal, mas não remove malware do endpoint nem substitui os controles de autorização de cada sistema. Um dispositivo comprometido pode usar um túnel criptograficamente válido.
- **D)** proteção de integridade dos dados em trânsito é uma propriedade esperada da suíte criptográfica do túnel corretamente configurado, dentro do escopo descrito.

**Conceito:** diferença entre proteção do túnel VPN, postura do endpoint e autorização na aplicação.

**Pegadinha:** estender a segurança do canal ao dispositivo e aos privilégios de negócio exercidos depois que o tráfego chega.

**Como pensar:** delimite o escopo: VPN protege dados em trânsito e autentica conforme o mecanismo; antimalware, correções do endpoint e autorização de ações permanecem controles separados.

**Referência:** [VPN](semana_02_estudo.md#s2-d4-vpn), com contraste em [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2D6Q272

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** reversibilidade por chave caracteriza criptografia, enquanto hash é projetado como transformação unidirecional.
- **B)** comparar o resumo calculado com referência protegida ajuda a detectar alteração, mas não oferece caminho normal de recuperação da entrada.
- **C)** hash sem segredo não cifra nem autentica origem; se ambos os valores puderem ser trocados, a comparação perde a confiança.
- **D)** funções têm saídas finitas e colisões existem matematicamente; a segurança busca torná-las impraticáveis, não impossíveis.

**Conceito:** uso de hash para integridade e distinção para cifra reversível e autenticação.

**Pegadinha:** usar informalmente “codificar” como se o resumo pudesse ser decifrado ou lhe atribuir garantias que exigem HMAC/assinatura.

**Como pensar:** procure três elementos: resumo de tamanho fixo, comparação com referência confiável e ausência de operação inversa por chave.

**Referência:** [Hash, MAC e armazenamento de senhas — hash](semana_02_estudo.md#s2-d4-hash-hmac-senhas), incluindo o uso de referência confiável e os limites de confidencialidade/autenticação; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário S2D6Q273

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** inverte os papéis do par de chaves: a chave privada do signatário cria a assinatura, enquanto a chave pública correspondente permite verificá-la.
- **B)** assinatura digital não tem como objetivo ocultar o documento; confidencialidade exige criptografia apropriada e é propriedade distinta.
- **C)** no modelo de assinatura assimétrica, o titular usa a chave privada para assinar, e terceiros usam a chave pública correspondente para verificar integridade e autenticidade conforme o esquema.
- **D)** senha compartilhada é um segredo simétrico; não oferece a mesma verificabilidade pública e separação entre chave privada e pública.

**Conceito:** criação e verificação de assinatura digital por criptografia assimétrica.

**Pegadinha:** aplicar à assinatura a direção usada para confidencialidade ou confundir assinatura com cifragem de todo o conteúdo.

**Como pensar:** pergunte quem precisa poder produzir e quem precisa poder verificar: somente o titular controla a privada; verificadores usam a pública.

**Referência:** [Assinatura digital e certificado](semana_02_estudo.md#s2-d4-assinatura-certificado), com contraste em [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2D6Q274

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** autenticação do servidor, confidencialidade e integridade dos dados em trânsito são propriedades pretendidas quando o TLS é validado e configurado adequadamente.
- **B)** segurança do canal não atesta veracidade do conteúdo nem substitui a autorização de cada ação pela aplicação.
- **C)** TLS protege justamente dados durante o transporte; proteção de armazenamento exige mecanismos próprios.
- **D)** endpoint comprometido está fora do escopo direto, e alguns metadados continuam observáveis apesar da cifra.

**Conceito:** propriedades do TLS e limite entre proteção do canal, endpoint e aplicação.

**Pegadinha:** ampliar a autenticação do servidor e a cifra em trânsito para garantias absolutas sobre conteúdo, permissão ou endpoint.

**Como pensar:** delimite fisicamente o canal: TLS protege o que transita entre os extremos configurados, não tudo o que existe antes, depois ou dentro da aplicação.

**Referência:** [TLS](semana_02_estudo.md#s2-d4-tls), nas propriedades pretendidas e na lista de elementos fora do canal; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário S2D6Q275

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** SAE melhora a troca autenticada, mas não corrige senha fraca, firmware vulnerável ou administração exposta.
- **B)** SAE foi desenhado para evitar que a captura passiva forneça o mesmo verificador reutilizável em ataques offline do modelo PSK.
- **C)** clientes legados podem negociar WPA2 no modo de transição, de modo que a proteção depende do modo realmente utilizado.
- **D)** SAE é a marca técnica do WPA3-Personal, mas a segurança continua sendo resultado da configuração e de controles complementares.

**Conceito:** uso de SAE no WPA3-Personal e permanência de requisitos operacionais de segurança.

**Pegadinha:** interpretar a adoção de padrão mais novo como eliminação automática de senha forte, atualização e segmentação.

**Como pensar:** aceite a alternativa que combine a melhoria específica, SAE, com limites realistas; rejeite promessas de invulnerabilidade.

**Referência:** [Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi), nas subseções WPA3, modo de transição e boas práticas; e [D6-RF-MX-08](semana_02_estudo.md#s2-d6-rf-mx-08).

### Comentário S2D6Q276

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** apagar registros compromete investigação e cadeia de custódia; conter não significa destruir evidência.
- **B)** restrição temporária reduz o dano em curso e ganha tempo para remover a causa e restaurar de modo controlado.
- **C)** remover persistência e corrigir o ponto de entrada são objetivos de erradicação, posteriores ou parcialmente sobrepostos à contenção.
- **D)** restabelecer ativos validados e acompanhar recorrência pertencem à recuperação, não ao objetivo imediato de limitar expansão.

**Conceito:** contenção como limitação da propagação e do impacto antes da erradicação e recuperação.

**Pegadinha:** confundir fases que podem se sobrepor operacionalmente, mas possuem finalidades diferentes.

**Como pensar:** associe cada verbo à fase: conter limita, erradicar remove a causa e recuperar restaura/valida a operação.

**Referência:** [Resposta a incidentes — resposta e contenção](semana_02_estudo.md#s2-d4-resposta-incidentes), no contraste com erradicação e recuperação; e [D6-RF-MX-09](semana_02_estudo.md#s2-d6-rf-mx-09).

### Comentário S2D6Q277

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** um ponto das 13h implicaria perda potencial de uma hora, excedendo o RPO de 30 minutos.
- **B)** somar a janela produz um horário posterior ao incidente, que não representa o limite de perda de dados anterior à interrupção.
- **C)** um ponto das 14h seria melhor que o limite e também recuperável, mas não é o **mais antigo** ainda aceitável; RPO de 30 minutos não exige perda zero.
- **D)** `14h − 30 minutos = 13h30`; esse é o limite temporal mais antigo que ainda mantém a perda dentro do objetivo definido.

**Conceito:** cálculo e interpretação operacional do RPO.

**Pegadinha:** somar em vez de subtrair a janela ou confundir “ponto aceitável” com “ponto mais antigo aceitável”.

**Como pensar:** trate o RPO como a distância máxima para trás a partir do incidente: instante do incidente menos RPO.

**Referência:** [Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup) e [D6-RF-MX-09 — Resposta, continuidade e objetivos de recuperação](semana_02_estudo.md#s2-d6-rf-mx-09).
### Comentário S2D6Q278

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** redundância prioriza continuidade diante da falha de componente, enquanto backup conserva estado recuperável e histórico.
- **B)** inverte as finalidades; backup normalmente exige restauração, e redundância fornece componente ou caminho alternativo.
- **C)** RAID pode tolerar falha física específica, mas replica corrupção/exclusão e não equivale a cópia isolada versionada.
- **D)** os controles são complementares e podem possuir objetivos, tempos e pontos de recuperação diferentes.

**Conceito:** continuidade por redundância versus recuperação histórica por backup.

**Pegadinha:** tratar replicação ou RAID como backup e confundir serviço ainda disponível com dado recuperável de versão anterior.

**Como pensar:** pergunte se o controle mantém a operação agora ou permite voltar no tempo; a primeira função é redundância, a segunda é backup.

**Referência:** [Backup e disponibilidade — backup × redundância × alta disponibilidade](semana_02_estudo.md#s2-d4-backup), incluindo o limite de RAID e replicação; e [D6-RF-MX-09](semana_02_estudo.md#s2-d6-rf-mx-09).

### Comentário S2D6Q279

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** compartilhar um intervalo não significa executar no mesmo instante, portanto não há paralelismo.
- **B)** concorrência pode existir com uma única CPU por meio de intercalação e progresso de várias tarefas.
- **C)** as tarefas concorrem pelo processador e avançam de forma intercalada, sem simultaneidade física.
- **D)** troca de contexto alterna a tarefa em execução e não cria dois fluxos executando ao mesmo tempo.

**Conceito:** diferença entre concorrência e paralelismo.

**Pegadinha:** interpretar progresso no mesmo intervalo como execução simultânea no mesmo instante.

**Como pensar:** pergunte se as tarefas podem avançar alternadamente e, em seguida, se executam exatamente ao mesmo tempo.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho que distingue intercalação concorrente de execução simultânea paralela.

### Comentário S2D6Q280

**Nível:** Médio

**Uso:** Aprofundamento

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** ambas as threads executaram e concluíram; não existe espera circular que impeça o progresso.
- **B)** o resultado dependeu da intercalação de uma operação não atômica e uma gravação sobrescreveu o efeito da outra.
- **C)** nenhuma thread foi adiada indefinidamente; o defeito ocorreu mesmo com as duas executando.
- **D)** não houve reação repetida sem avanço, mas uma única intercalação que perdeu atualização.

**Conceito:** condição de corrida e atualização perdida.

**Pegadinha:** confundir erro de valor compartilhado com problemas de ausência de progresso.

**Como pensar:** decomponha a atribuição em leitura, soma e escrita e observe se uma thread pode usar um valor desatualizado.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente condição de corrida e atualização perdida em operação composta.

### Comentário S2D6Q281

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** um contador em oito controla múltiplas unidades e não impõe um único titular na seção crítica.
- **B)** variável de condição coordena espera por predicado e depende de estado protegido, não substituindo o mutex.
- **C)** barreira alinha fases de várias threads, mas não concede propriedade exclusiva sobre uma seção.
- **D)** o mutex expressa exclusão e propriedade, desde que todos os participantes respeitem aquisição e liberação.

**Conceito:** finalidade do mutex na proteção de seção crítica.

**Pegadinha:** escolher outro mecanismo de sincronização apenas porque também coordena threads.

**Como pensar:** procure o mecanismo cuja regra central é um titular por vez e liberação pelo fluxo que o adquiriu.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho sobre exclusão mútua e propriedade do mutex.

### Comentário S2D6Q282

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** deadlock clássico requer coexistência de exclusão mútua, posse e espera, não preempção e espera circular.
- **B)** preempção obrigatória rompe uma das condições; a condição necessária é a impossibilidade de retirar o recurso compulsoriamente.
- **C)** aquisição sem conservar recursos enquanto espera rompe justamente a condição de posse e espera.
- **D)** ordem acíclica elimina a espera circular em vez de constituí-la.

**Conceito:** condições necessárias de Coffman para deadlock.

**Pegadinha:** substituir uma condição por uma técnica que a rompe e, portanto, previne o impasse.

**Como pensar:** procure quatro restrições que possam coexistir e sustentar um ciclo, não medidas de prevenção.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente as quatro condições necessárias de Coffman.

### Comentário S2D6Q283

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** o sistema continua concluindo tarefas e não existe ciclo de espera entre participantes.
- **B)** no livelock, os participantes permanecem ativos reagindo sem avanço útil, o que não ocorre no cenário.
- **C)** starvation permite progresso global enquanto uma tarefa é preterida; aging eleva gradualmente sua prioridade.
- **D)** inversão exige uma tarefa prioritária aguardando recurso mantido por outra de prioridade menor.

**Conceito:** starvation por prioridade e mitigação por aging.

**Pegadinha:** confundir o adiamento de um participante com impasse, atividade sem progresso ou inversão por lock.

**Como pensar:** observe quem progride: se o sistema avança, mas um participante pode esperar para sempre, procure starvation.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), nos trechos sobre starvation, aging e diferenças para outros problemas de progresso.

### Comentário S2D6Q284

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** quantum pequeno faz a fatia expirar mais vezes e tende a aumentar, não eliminar, as trocas de contexto.
- **B)** é o quantum muito grande que aproxima Round Robin de FCFS, porque cada processo tende a executar por longos intervalos antes da preempção.
- **C)** Round Robin é preemptivo; reduzir o quantum torna a preempção por fim de fatia mais frequente.
- **D)** fatias curtas elevam o número de preempções e o custo administrativo de salvar e restaurar contextos.

**Conceito:** efeito do tamanho do quantum no Round Robin.

**Pegadinha:** inverter os efeitos de quantum pequeno e quantum grande.

**Como pensar:** imagine uma mesma carga dividida em fatias: quanto menores as fatias, mais fronteiras e trocas; quanto maiores, mais o comportamento se aproxima de FCFS.

**Referência:** [Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento), com recuperação em [D6-RF-MX-10](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2D6Q285

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** polling parte de consultas iniciadas pela CPU, enquanto interrupção permite ao dispositivo notificar a ocorrência do evento.
- **B)** a alternativa inverte as iniciativas que caracterizam cada mecanismo.
- **C)** interrupção não exige consulta periódica para descobrir cada evento; a sinalização é sua diferença central.
- **D)** interrupção notifica e não define quem transfere todo o bloco; transferência em bloco remete a DMA.

**Conceito:** diferença operacional entre polling e interrupção.

**Pegadinha:** inverter quem inicia a verificação ou atribuir à interrupção a função de transferir dados.

**Como pensar:** pergunte se a CPU precisa perguntar repetidamente ou se o dispositivo pode chamar sua atenção quando necessário.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente a diferença entre consulta repetida por polling e sinalização por interrupção.

### Comentário S2D6Q286

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** o cenário afasta a cópia de cada palavra pela CPU, característica da E/S programada.
- **B)** a CPU prepara a operação, mas a controladora realiza a transferência do bloco e depois sinaliza a conclusão.
- **C)** interrupção pode comunicar conclusão, porém a alternativa descreve a CPU copiando cada unidade, o que não ocorreu.
- **D)** polling envolve consulta repetida e, como descrito, mantém a CPU responsável por cada transferência.

**Conceito:** funcionamento e limite da expressão transferência direta por DMA.

**Pegadinha:** concluir que configuração inicial ou interrupção final elimina a participação do DMA.

**Como pensar:** identifique quem move o bloco; se a controladora transfere e a CPU apenas configura e trata o fim, procure DMA.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho sobre DMA, configuração pela CPU e menor intervenção por unidade transferida.

### Comentário S2D6Q287

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** ausência de commit indica transação incompleta, que não deve ser consolidada como concluída no replay.
- **B)** journal não é repositório obrigatório de todas as versões nem desfaz automaticamente exclusões válidas.
- **C)** transações confirmadas podem ser repetidas, enquanto as incompletas são descartadas para recuperar coerência estrutural.
- **D)** journaling não substitui redundância ou backup quando a mídia deixa de fornecer os blocos físicos.

**Conceito:** recuperação de consistência por commit e replay do journal.

**Pegadinha:** transformar journal em versionamento, backup ou mecanismo de reconstrução física da mídia.

**Como pensar:** procure a evidência de commit; ela separa a transação confirmada da operação incompleta durante a recuperação.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), especialmente commit, replay e limite do journaling perante histórico e falha física.

### Comentário S2D6Q288

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** `6 = 4 + 2 = rw-` para o dono; `4 = r--` para o grupo; `0 = ---` para outros.
- **B)** leitura e escrita para todos seria `666`, não `640`.
- **C)** a opção mistura bits entre as tríades; `640` não concede execução ao dono, escrita ao grupo nem leitura a outros.
- **D)** o primeiro dígito é 6, portanto o dono possui leitura e escrita.

**Conceito:** interpretação de modo octal Unix por proprietário, grupo e outros.

**Pegadinha:** somar bits entre classes diferentes ou esquecer a ordem proprietário/grupo/outros.

**Como pensar:** leia cada dígito separadamente usando `r=4`, `w=2`, `x=1`: `6→rw-`, `4→r--`, `0→---`.

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), com recuperação em [D6-RF-MX-10](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2D6Q289

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** SACL está ligada à auditoria; a DACL é que reúne ACEs usadas para permitir ou negar acesso.
- **B)** ACE de negação pode integrar a DACL e participar da decisão efetiva.
- **C)** a DACL contém ACEs de permissão ou negação, que podem ser explícitas ou herdadas conforme a configuração.
- **D)** propriedade e DACL são componentes distintos, e ACEs não ficam restritas à configuração de compartilhamento.

**Conceito:** composição de uma DACL no Windows.

**Pegadinha:** trocar DACL por SACL, limitar a lista a permissões ou confundi-la com propriedade e compartilhamento.

**Como pensar:** associe DACL à decisão de acesso e ACE às entradas que concedem ou negam direitos ao objeto.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10), no trecho sobre DACL, ACEs de permissão ou negação e herança.

### Comentário S2D6Q290

**Nível:** Médio

**Uso:** Revisão

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** resposta ICMP não consulta o processo do portal e não comprova a saúde da aplicação.
- **B)** o teste foi feito por endereço IP e pode funcionar mesmo quando a resolução do nome está incorreta.
- **C)** ICMP não testa a porta TCP 443, o handshake TLS nem a disponibilidade do processo servidor.
- **D)** o resultado demonstra alcance IP para ICMP, mas deixa abertas hipóteses nas camadas de transporte, TLS e aplicação.

**Conceito:** alcance e limite diagnóstico do `ping`.

**Pegadinha:** ampliar uma evidência de conectividade de rede para conclusões sobre DNS, porta e aplicação.

**Como pensar:** registre exatamente o que foi testado e avance por camadas sem transformar um sucesso parcial em prova do serviço completo.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05), no trecho sobre diagnóstico em camadas e limites do `ping` perante transporte e aplicação.

### Comentário S2D6Q291

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** a comparação criptográfica do conteúdo não depende diretamente de os hosts concordarem sobre o horário.
- **B)** relógios divergentes podem inverter a ordem aparente dos fatos e dificultar a reconstrução conjunta da sequência do incidente.
- **C)** um identificador de conta já gravado permanece legível, embora o momento atribuído à ação possa estar incorreto.
- **D)** severidade e mensagem podem ser interpretadas, mas sua posição correta na linha do tempo fica comprometida.

**Conceito:** importância da sincronização temporal para correlação de logs.

**Pegadinha:** confundir campos ainda legíveis no evento com a capacidade de ordenar eventos de fontes diferentes.

**Como pensar:** imagine três relógios discordando e pergunte qual análise depende de saber o que ocorreu antes e depois.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06), especialmente NTP, consistência de horários e correlação temporal entre registros.

### Comentário S2D6Q292

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** nenhum controle elimina todo risco, e as demais camadas exercem funções preventivas, detectivas e de recuperação.
- **B)** controles complementares limitam o impacto da falha ou evasão de uma barreira isolada.
- **C)** credencial e dependência comuns podem criar um único ponto capaz de enfraquecer várias camadas ao mesmo tempo.
- **D)** backup apoia recuperação, mas não evita exfiltração, indisponibilidade inicial ou persistência do atacante.

**Conceito:** defesa em profundidade e redução de dependências comuns.

**Pegadinha:** contar produtos como garantia absoluta ou tratar recuperação como substituta de prevenção e detecção.

**Como pensar:** pergunte o que ainda limita o ataque se uma das barreiras for vencida; essa é a função das camadas complementares.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08), no trecho sobre controles complementares e defesa em profundidade.

### Comentário S2D6Q293

**Nível:** Difícil

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** a estação precisa resolver o nome antes de abrir a conexão, e a requisição HTTPS ocorre depois do handshake TLS.
- **B)** sem configuração estática, DHCP precede a resolução, e TLS sobre HTTP/2 depende da conexão TCP já estabelecida.
- **C)** a estação obtém configuração, resolve o nome, estabelece TCP, negocia TLS e só então envia a requisição HTTP protegida.
- **D)** handshake TLS e requisição HTTP não antecedem a conexão TCP que os transporta no cenário especificado.

**Conceito:** encadeamento funcional de DHCP, DNS, TCP, TLS e HTTP/2.

**Pegadinha:** reconhecer todos os protocolos, mas ignorar a dependência temporal existente entre eles.

**Como pensar:** pergunte em ordem: como obter configuração, como localizar o servidor, como criar o canal e quando enviar a requisição.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05), especialmente DHCP, DNS, estabelecimento do transporte, TLS e HTTP.

### Comentário S2D6Q294

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** proxy direto atua em nome dos clientes que acessam destinos, e não em nome do serviço publicado.
- **B)** transparência de saída muda a forma de configuração do cliente, mas continua mediando o lado dos usuários.
- **C)** cache de saída atende clientes internos que consomem conteúdo externo, direção oposta à do cenário.
- **D)** o proxy reverso recebe em nome do serviço e escolhe o backend que atenderá a solicitação externa.

**Conceito:** diferença entre proxy direto e proxy reverso.

**Pegadinha:** classificar todo intermediário HTTP como proxy de clientes sem observar quem ele representa.

**Como pensar:** identifique o lado ocultado e representado: clientes indicam proxy direto; servidores publicados indicam proxy reverso.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06), no trecho que diferencia proxy direto e proxy reverso.

### Comentário S2D6Q295

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** LDAP fornece operações para consultar e modificar entradas e atributos de um diretório.
- **B)** Kerberos trata autenticação baseada em tíquetes e não é o protocolo geral de consulta das entradas descritas.
- **C)** RADIUS apoia AAA de acesso à rede, embora possa integrar-se a uma fonte de identidades separada.
- **D)** DNS resolve nomes e publica registros, mas não substitui a estrutura hierárquica de usuários e grupos de LDAP.

**Conceito:** finalidade do protocolo LDAP.

**Pegadinha:** escolher outro protocolo ligado a identidade ou nomes sem conferir a operação de diretório solicitada.

**Como pensar:** procure o protocolo cujo objeto são entradas e atributos organizados em uma árvore de diretório.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06), especialmente a finalidade de LDAP em serviços de diretório.

### Comentário S2D6Q296

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** qualquer processo pode escutar a porta, e o número não executa handshake nem valida certificado.
- **B)** TLS pode operar em outras portas quando configurado, sem perder suas propriedades apenas por causa da numeração.
- **C)** porta sugere um serviço esperado, mas a segurança depende do protocolo real, da validação, da configuração e dos endpoints.
- **D)** firewall permite ou bloqueia fluxos; ele não transforma automaticamente protocolo em claro em sessão TLS.

**Conceito:** diferença entre associação de porta, protocolo efetivo e garantias de segurança.

**Pegadinha:** tratar convenção operacional como mecanismo criptográfico ou evidência conclusiva do conteúdo.

**Como pensar:** use a porta como indício inicial e confirme handshake, certificado, parâmetros e estado dos endpoints antes de concluir.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05), no trecho que trata porta como associação convencional, e não prova de protocolo ou segurança.

### Comentário S2D6Q297

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** alteração não autorizada afeta diretamente a integridade do dado.
- **B)** divulgação de informação sigilosa compromete a confidencialidade.
- **C)** associação indevida entre usuário e grupo representa falha de identidade ou autorização e pode produzir outros impactos, mas não descreve diretamente indisponibilidade.
- **D)** saturar o enlace por DDoS impede ou degrada o acesso oportuno ao serviço, atingindo diretamente a disponibilidade.

**Conceito:** classificação do efeito de um DDoS na tríade CIA.

**Pegadinha:** classificar pelo mecanismo genérico “ataque” em vez do efeito imediato sobre o ativo.

**Como pensar:** pergunte o que aconteceu com o dado ou serviço: foi exposto, alterado ou ficou inacessível? Saturação aponta para disponibilidade.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia), [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede) e [D6-RF-MX-07](semana_02_estudo.md#s2-d6-rf-mx-07).
### Comentário S2D6Q298

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** conter exige limitar comunicação ou propagação; a aquisição da imagem não isola o host por si só.
- **B)** copiar o conteúdo preserva inclusive vestígios maliciosos e não remove a persistência do original.
- **C)** imagem, hashes e cadeia de custódia permitem demonstrar integridade e repetir a análise sem alterar a fonte.
- **D)** imagem forense preserva o estado investigado, que pode estar comprometido, e não equivale a recuperação limpa.

**Conceito:** preservação de evidência digital antes da erradicação.

**Pegadinha:** confundir aquisição forense com ações que isolam, removem o agente ou restauram o serviço.

**Como pensar:** observe que a equipe está congelando e documentando o estado para análise, não tentando torná-lo operacional.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09), especialmente preservação de evidências antes de ações de erradicação.

### Comentário S2D6Q299

**Nível:** Médio

**Uso:** Simulado

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** `Get-Process` consulta e lista informações de processos no PowerShell sem encerrá-los por si só.
- **B)** `Stop-Process` encerra processos pelo PowerShell; não é comando meramente consultivo.
- **C)** `kill` envia sinal a um processo em sistemas Unix-like; conforme o sinal, solicita término ou outra alteração de estado.
- **D)** `taskkill` solicita ou força o encerramento de processo no Windows e, portanto, altera o estado do sistema.

**Conceito:** separação entre observação e ação na administração de processos.

**Pegadinha:** presumir que todo comando cujo nome menciona processo apenas lista ou, ao contrário, que a listagem já encerra o alvo.

**Como pensar:** classifique pelo verbo: `Get` observa; `Stop`, `kill` e `taskkill` solicitam mudança de estado.

**Referência:** [Windows e Linux — comandos pertinentes](semana_02_estudo.md#s2-d5-comandos), com recuperação em [D6-RF-MX-10](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2D6Q300

**Nível:** Muito difícil

**Uso:** Simulado

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** I e II são verdadeiras, mas III também é; continuidade exige testar componentes organizacionais e técnicos além do ponto e do horário de restauração.
- **B)** as três afirmações calculam os objetivos temporais e preservam a diferença entre infraestrutura disponível e serviço de negócio funcional.
- **C)** I e III são verdadeiras, mas II também é; 16h30 fica duas horas e meia após o incidente, embora as dependências ainda impeçam declarar recuperação.
- **D)** II e III são verdadeiras, mas I também é; recuperar 13h35 em incidente às 14h implica perda potencial de 25 minutos, dentro do RPO de 30.

**Conceito:** avaliação conjunta de RPO, RTO, dependências e critérios de continuidade efetiva.

**Pegadinha:** declarar sucesso pelo relógio ou pelo backup sem validar a transação completa e as dependências do serviço.

**Como pensar:** calcule perda e indisponibilidade, depois teste dados, integrações, pessoas e operação; objetivo temporal atendido não encerra sozinho a recuperação.

**Referência:** [Recuperação por dependências e validação ponta a ponta](semana_02_estudo.md#s2-d6-recuperacao-dependencias) e [Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), nos trechos sobre RPO, RTO, dependências e validação do negócio.
#### Comentário Extra Dia 6.1
**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** Incorreta. O trecho afirma que a segmentação não substitui MFA; portanto, não autoriza dispensar esse segundo controle.
- **B)** Correta. A conjunção “mas” delimita o alcance da segmentação e mostra que ela e MFA cumprem funções complementares.
- **C)** Incorreta. “Ajuda” expressa contribuição limitada, não capacidade de impedir todo e qualquer ataque.
- **D)** Incorreta. A frase combina controles em camadas e não descreve segurança como um estado binário de tudo ou nada.

**Conceito:** ideia central.

**Pegadinha:** transformar “ajuda” em garantia total ou interpretar “não substitui” como inutilidade de um dos controles.

**Como pensar:** preserve as duas partes da adversativa: a segmentação é útil, mas continua insuficiente sem controles complementares.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-01).

#### Comentário Extra Dia 6.2

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** uma ausência nativa no transporte não proíbe a aplicação de implementar mecanismo próprio.
- **B)** o UDP não corrige automaticamente toda perda antes da entrega à aplicação.
- **C)** confirmações, temporizadores e novas tentativas podem ser implementados na camada de aplicação conforme a necessidade.
- **D)** o UDP não garante entrega nem unicidade de cada datagrama recebido.

**Conceito:** inferência válida e limite da expressão “não oferece nativamente”.

**Pegadinha:** transformar ausência de recurso nativo em proibição de implementá-lo ou em garantia oposta.

**Como pensar:** separe o que o protocolo fornece por si do que a aplicação pode acrescentar acima dele.

**Referência:** [D6-RF-PT-02 — Inferência](semana_02_estudo.md#s2-d6-rf-pt-02), aplicada à ausência de garantias nativas do UDP.

#### Comentário Extra Dia 6.3
**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** Correta. “Embora” introduz concessão, e “porque” apresenta a causa atribuída à falha do serviço.
- **B)** Incorreta. “Embora” não é causal, e “porque” não introduz finalidade nesse período.
- **C)** Incorreta. Não há conclusão no primeiro conector nem oposição no segundo.
- **D)** Incorreta. “Embora” não estabelece condição, e “porque” indica causa, não mera explicação desvinculada do fato.

**Conceito:** conectores.

**Pegadinha:** classificar conectores apenas pela posição, ignorando a relação semântica construída entre as orações.

**Como pensar:** pergunte qual obstáculo foi admitido sem impedir a conclusão e qual fato explica diretamente a falha.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-03).

#### Comentário Extra Dia 6.4

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** a retirada do possessivo não informa se o acesso pertence à analista ou à gerente.
- **B)** mudar a posição do possessivo não elimina automaticamente os dois antecedentes compatíveis.
- **C)** a flexão não identifica a titular e ainda cria incompatibilidade com o acesso singular do exemplo.
- **D)** o complemento nominal explícito seleciona uma das duas referentes conforme a intenção comunicativa.

**Conceito:** ambiguidade pronominal e explicitação do referente.

**Pegadinha:** alterar forma ou posição do pronome sem resolver a dupla possibilidade de referência.

**Como pensar:** pergunte “acesso de quem?” e escolha a redação que responde isso dentro do próprio período.

**Referência:** [D6-RF-PT-04 — Ambiguidade](semana_02_estudo.md#s2-d6-rf-pt-04), na orientação de explicitar o referente.

#### Comentário Extra Dia 6.5

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Essenciais

**Análise das alternativas:**

- **A)** “pode” não converte detecção e alerta em garantia universal.
- **B)** preserva a possibilidade ou capacidade e rejeita uma promessa absoluta de detecção.
- **C)** o verbo não cria bloqueio, e IDS não se torna IPS pela modalidade empregada.
- **D)** possibilidade ou capacidade não equivale a obrigação nem exclui falhas de detecção.

**Conceito:** modalidade verbal e alcance de afirmações técnicas.

**Pegadinha:** substituir “pode” por “deve”, “sempre” ou “garante”.

**Como pensar:** classifique a força do verbo antes de avaliar qualquer conclusão técnica adicionada.

**Referência:** [D6-RF-PT-05 — Modalidade](semana_02_estudo.md#s2-d6-rf-pt-05), na distinção entre possibilidade, obrigação e garantia.

#### Comentário Extra Dia 6.6

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** transforma a integridade aparente em causa para dispensar exatamente a ação recomendada.
- **B)** cria uma condição restritiva que não aparece no enunciado original.
- **C)** “mesmo que” mantém a concessão e a necessidade de testar a restauração.
- **D)** inverte a relação lógica e atribui ao teste o poder de produzir a integridade do backup.

**Conceito:** equivalência semântica em reescrita concessiva.

**Pegadinha:** trocar concessão por causa, condição exclusiva ou relação de resultado.

**Como pensar:** preserve simultaneamente a ressalva sobre integridade e a orientação de executar o teste.

**Referência:** [D6-RF-PT-06 — Reescrita](semana_02_estudo.md#s2-d6-rf-pt-06), na preservação da concessão e da orientação principal.

#### Comentário Extra Dia 6.7
**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** Incorreta. `Haver` com sentido de existir fica no singular (`havia`), e `existir` deve concordar com `controles` (`existem`).
- **B)** Correta. `Havia` permanece impessoal no singular, enquanto `existem` concorda com o sujeito plural `controles`.
- **C)** Incorreta. O verbo impessoal não vai ao plural, e `existe` também não concorda com `controles`.
- **D)** Incorreta. `Haviam` viola a impessoalidade de `haver`, e `existia` está no singular diante de `controles`.

**Conceito:** concordância.

**Pegadinha:** aplicar ao verbo `haver` impessoal a mesma concordância exigida pelo verbo pessoal `existir`.

**Como pensar:** substitua `haver` por `existir`: o primeiro permanece singular; o segundo concorda com o termo que passa a sujeito.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-07).

#### Comentário Extra Dia 6.8
**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** Incorreta. `Obedeceu à política` está correto, mas não há crase antes do infinitivo em `começou a analisar`.
- **B)** Incorreta. A regência de `obedecer` pede preposição `a`, que se funde com o artigo de `a política`; além disso, permanece a crase indevida antes do infinitivo.
- **C)** Incorreta. O correto é `referiu-se às regras`, e `todos` não admite artigo feminino que justifique `à`.
- **D)** Correta. Há crase em `à política` pela regência e pelo artigo, e apenas preposição simples antes de `analisar`.

**Conceito:** crase.

**Pegadinha:** marcar crase mecanicamente depois de qualquer verbo regente ou antes de infinitivo e pronome.

**Como pensar:** confirme separadamente a preposição exigida e a presença de artigo feminino; só depois faça a fusão.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-08).

#### Comentário Extra Dia 6.9
**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** Correta. A vírgula delimita adequadamente o adjunto adverbial deslocado `Após a contenção`.
- **B)** Incorreta. A vírgula rompe a ligação entre o verbo `preservou` e seu objeto direto `registros essenciais`.
- **C)** Incorreta. A vírgula separa indevidamente o sujeito `Os administradores` do verbo `revogaram`.
- **D)** Incorreta. A vírgula separa o sujeito `Os servidores vulneráveis` da locução verbal `foram isolados`.

**Conceito:** pontuação.

**Pegadinha:** inserir vírgula pela pausa da fala e romper sujeito, verbo ou complemento.

**Como pensar:** encontre primeiro o esqueleto sujeito–verbo–complemento e isole apenas o termo realmente deslocado.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-09).

#### Comentário Extra Dia 6.10
**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Aprofundamento

**Análise das alternativas:**

- **A)** Incorreta. Coordena os infinitivos `Isolar` e `preservar` com a nominalização `a revogação`, quebrando o paralelismo.
- **B)** Incorreta. Os dois primeiros membros são verbos no infinitivo, mas o terceiro é o substantivo `preservação`.
- **C)** Incorreta. A enumeração mistura infinitivo, oração desenvolvida e substantivo isolado.
- **D)** Correta. `Isolar`, `revogar` e `preservar` são três infinitivos coordenados com a mesma função sintática.

**Conceito:** paralelismo.

**Pegadinha:** aceitar uma enumeração semanticamente coerente, mas construída com formas sintáticas incompatíveis.

**Como pensar:** compare a forma gramatical de cada item coordenado e mantenha o mesmo padrão do início ao fim.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-pt-10).

#### Comentário Extra Dia 6.11

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** jitter é a variação da latência, exatamente o comportamento mostrado pelas medições.
- **B)** throughput mede vazão efetivamente transmitida, não oscilação temporal do atraso.
- **C)** goodput mede carga útil entregue, excluindo sobrecargas conforme o recorte da medição.
- **D)** largura de banda representa capacidade nominal ou disponível, não variação da latência.

**Conceito:** distinção entre métricas de capacidade, vazão útil e atraso.

**Pegadinha:** escolher uma métrica de desempenho verdadeira, mas que mede outra grandeza.

**Como pensar:** identifique primeiro a grandeza que varia; atraso que oscila aponta para jitter.

**Referência:** [D6-RF-MX-01 — Recuperação ativa de redes e métricas](semana_02_estudo.md#s2-d6-rf-mx-01), na distinção entre latência, jitter, throughput, goodput e largura de banda.

#### Comentário Extra Dia 6.12

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** endereços MAC pertencem ao enlace e não permanecem como identidade fim a fim por todos os roteadores.
- **B)** o roteador desencapsula o quadro local, consulta o pacote IP e o encapsula em novo quadro para o próximo enlace.
- **C)** o pacote IP é preservado para o encaminhamento; o roteador não envia apenas a carga de aplicação.
- **D)** o quadro muda no salto, enquanto os endereços IP fim a fim não são simplesmente trocados a cada roteador.

**Conceito:** relação entre pacote IP e quadro de enlace durante o roteamento.

**Pegadinha:** tratar endereço MAC como fim a fim ou retirar a camada IP no equipamento intermediário.

**Como pensar:** acompanhe separadamente o pacote que cruza redes e o quadro que vale apenas no enlace atual.

**Referência:** [D6-RF-MX-02 — Camadas, encapsulamento e evidência](semana_02_estudo.md#s2-d6-rf-mx-02), na renovação do quadro a cada enlace roteado.

#### Comentário Extra Dia 6.13
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** Incorreta. Em `/27`, o bloco que começa em `.0` termina em `.31`; ele não contém o endereço `.77`.
- **B)** Incorreta. O bloco iniciado em `.32` termina em `.63`, ainda antes do endereço informado.
- **C)** Correta. A máscara `/27` cria blocos de 32 endereços; `.77` pertence ao intervalo `.64`–`.95`, cuja rede é `.64`.
- **D)** Incorreta. `.77` é um endereço de host dentro do bloco, não o endereço que identifica a rede.

**Conceito:** CIDR.

**Pegadinha:** usar o IP fornecido como rede ou escolher o múltiplo de 32 anterior errado.

**Como pensar:** calcule o tamanho do bloco (`256 − 224 = 32`) e escolha o maior múltiplo de 32 que não ultrapasse 77.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-03).

#### Comentário Extra Dia 6.14
**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** Correta. Para um destino fora da sub-rede, o próximo salto local é o gateway; o host precisa do MAC da interface local desse roteador.
- **B)** Incorreta. ARP opera no enlace local e não atravessa roteadores para descobrir diretamente o MAC do host remoto.
- **C)** Incorreta. O servidor DNS pode resolver um nome em IP, mas não é necessariamente o próximo salto do pacote nem o alvo da resolução ARP.
- **D)** Incorreta. NAT é uma função de tradução; mesmo quando ocorre no roteador, o host resolve o MAC da interface do gateway, não um “MAC do NAT”.

**Conceito:** gateway.

**Pegadinha:** procurar no enlace local o MAC do destino final que está em outra rede.

**Como pensar:** primeiro compare os prefixos; se o destino for remoto, a resolução de enlace aponta para o próximo salto configurado.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-04).

#### Comentário Extra Dia 6.15

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Revisão

**Análise das alternativas:**

- **A)** troca configuração e resolução e atribui aplicação e proteção aos protocolos opostos.
- **B)** DHCP fornece configuração, DNS resolve/publica nomes, TLS protege o canal e HTTP realiza a interação Web.
- **C)** cada uma das quatro funções foi associada a um protocolo de papel diferente.
- **D)** DHCP não é protocolo de aplicação Web, DNS não protege o canal, TLS não resolve nomes e HTTP não configura o cliente.

**Conceito:** papel funcional de protocolos em um fluxo de acesso Web.

**Pegadinha:** permutar funções verdadeiras entre protocolos conhecidos.

**Como pensar:** leia a cadeia como configuração → nomes → proteção do canal → requisição/resposta Web.

**Referência:** [D6-RF-MX-05 — Protocolos: transporte, Web, nomes e configuração](semana_02_estudo.md#s2-d6-rf-mx-05), na regra de integração entre os quatro protocolos.

#### Comentário Extra Dia 6.16
**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. SMTP é usado no envio e na transferência de mensagens; IMAP acessa a caixa, e SFTP oferece transferência sobre SSH com proteção.
- **B)** Incorreta. NTP sincroniza relógios, enquanto SNMP realiza gerência e monitoramento; nenhum deles cumpre as funções descritas.
- **C)** Correta. SMTP envia, IMAP mantém acesso e sincronização da caixa, e SFTP opera como subsistema do SSH.
- **D)** Incorreta. LDAP consulta diretórios, e PAT traduz endereços e portas; eles não traduzem portas e listam diretórios na ordem afirmada.

**Conceito:** serviços de rede.

**Pegadinha:** associar protocolos reais a funções vizinhas, mas trocadas entre envio, acesso, diretório e tradução.

**Como pensar:** atribua uma palavra funcional a cada protocolo: SMTP–envio, IMAP–caixa, SFTP–arquivo sobre SSH.

**Referência:** [Revisão fixa do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

#### Comentário Extra Dia 6.17

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** acerta a vulnerabilidade, mas troca ameaça e risco nas duas posições finais.
- **B)** a falha não é ameaça, e o agente potencial não corresponde à avaliação de risco.
- **C)** risco é o resultado da análise, não a fraqueza inicial do componente.
- **D)** falha explorável é vulnerabilidade, causa potencial é ameaça e probabilidade combinada ao impacto forma o risco.

**Conceito:** distinção entre fraqueza, causa potencial e avaliação de risco.

**Pegadinha:** permutar conceitos próximos preservando os mesmos três termos nas opções.

**Como pensar:** associe fraqueza ao sistema, possibilidade de exploração à ameaça e probabilidade/impacto ao risco.

**Referência:** [D6-RF-MX-07 — Segurança: objetivo, identidade, risco e ataque](semana_02_estudo.md#s2-d6-rf-mx-07), nas definições de vulnerabilidade, ameaça e risco.

#### Comentário Extra Dia 6.18

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** acerta a capacidade do IPS, mas atribui ao HMAC a estrutura assimétrica de uma assinatura digital.
- **B)** o IPS em linha pode tentar bloquear, e o HMAC usa segredo compartilhado para integridade e autenticidade.
- **C)** acerta o HMAC, mas reduz o IPS em linha ao papel passivo de alerta típico de um IDS.
- **D)** IPS não substitui todo firewall, e HMAC autentica um resumo; não cifra reversivelmente a mensagem.

**Conceito:** função de prevenção em linha e autenticação simétrica de mensagens.

**Pegadinha:** acertar um dos dois controles e trocar o outro por conceito criptográfico próximo.

**Como pensar:** resolva em dois filtros: ação possível no tráfego e tipo de chave usado para autenticar a mensagem.

**Referência:** [D6-RF-MX-08 — Controles, criptografia e Wi-Fi](semana_02_estudo.md#s2-d6-rf-mx-08), nas distinções firewall × IDS × IPS e HMAC × assinatura digital.

#### Comentário Extra Dia 6.19

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** o RPO admite no máximo trinta minutos de perda, e o RTO fixa duas horas para restabelecimento após as 14h.
- **B)** o ponto das 13h excede a perda tolerada, embora o horário de restabelecimento esteja dentro do RTO.
- **C)** o ponto de dados atende ao RPO, mas as 17h ultrapassam o RTO em uma hora.
- **D)** o restabelecimento é rápido, porém o ponto das 12h viola largamente o RPO.

**Conceito:** cálculo conjunto do ponto de recuperação e do tempo de restabelecimento.

**Pegadinha:** cumprir apenas um objetivo e induzir a aceitação do resultado completo.

**Como pensar:** calcule primeiro 14h − 30 min para o dado e depois 14h + 2 h para o serviço.

**Referência:** [D6-RF-MX-09 — Resposta, continuidade e objetivos de recuperação](semana_02_estudo.md#s2-d6-rf-mx-09), nas definições e no exemplo de RPO e RTO.

#### Comentário Extra Dia 6.20

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** interrupção é alternativa ao polling contínuo, DMA reduz trabalho por unidade e journal não é backup histórico.
- **B)** acerta interrupção e DMA, mas journaling não garante ausência de perda nem substitui backup.
- **C)** DMA reduz a intervenção por unidade transferida, mas não elimina toda participação ou configuração pela CPU.
- **D)** descreve adequadamente sinalização por interrupção, transferência por DMA e recuperação de consistência pelo journal.

**Conceito:** diferenças entre mecanismos de E/S e de consistência do sistema de arquivos.

**Pegadinha:** aceitar absolutos como “elimina toda atuação” ou transformar journal em garantia e cópia histórica.

**Como pensar:** associe cada mecanismo ao seu efeito limitado, sem convertê-lo em substituto completo de CPU ou backup.

**Referência:** [D6-RF-MX-10 — Sistemas operacionais: progresso, E/S e persistência](semana_02_estudo.md#s2-d6-rf-mx-10), nas linhas polling/interrupção/DMA e sistema de arquivos/journaling.

## Temas de discursiva da Semana 2

Os temas abaixo são complementares: não alteram as 420 questões objetivas, seus gabaritos ou comentários. Use até 30 linhas por resposta e aplique os critérios de autocorreção após escrever.

### Tema discursivo 1 — Resposta a incidente no portal do CRA-PR

**Enunciado:** Um portal de serviços do CRA-PR apresenta acesso indevido a contas e indisponibilidade parcial. Discorra sobre uma resposta que concilie preservação de evidências, contenção, erradicação, recuperação, comunicação e prevenção de recorrência.

**Roteiro:** apresente a gravidade do serviço; diferencie detecção, contenção e erradicação; relacione logs, MFA, segmentação, backup, RPO/RTO e lições aprendidas; encerre com medidas de governança e capacitação.

### Tema discursivo 2 — Continuidade e segurança de serviços digitais

**Enunciado:** Analise como uma autarquia profissional pode combinar disponibilidade de serviços digitais, proteção de dados e continuidade operacional, sem confundir redundância com backup ou segurança de canal com segurança do endpoint.

**Roteiro:** formule uma tese; desenvolva defesa em profundidade, controle de acesso, VPN/TLS, segmentação e resposta a incidentes; diferencie redundância, backup, RPO e RTO; conclua com teste de restauração e validação de negócio.

### Critérios de autocorreção da discursiva

- **Aderência:** respondi ao problema, sem fugir para uma lista de tecnologias?
- **Tese e progressão:** apresentei posição clara e desenvolvi causas, controles e efeitos em ordem lógica?
- **Precisão técnica:** diferenciei conceitos próximos, como IDS/IPS, backup/redundância e RPO/RTO?
- **Aplicação pública:** relacionei o caso à continuidade, dados e dever institucional da autarquia?
- **Coesão e norma:** usei conectores, referência clara, regência, concordância e pontuação corretas?
- **Conclusão:** retomei a tese com medida verificável, como teste, política, treinamento ou revisão periódica?
