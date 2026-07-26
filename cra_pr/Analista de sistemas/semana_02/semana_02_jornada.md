# Jornada Executável - Semana 2 - Analista de Sistemas

## Arquivos de execução

- [Apostila teórica](semana_02_estudo.md);
- [banco de questões](semana_02_questoes.md);
- [progressão discursiva e rubrica oficial](semana_02_dissertacoes.md);
- [super simulado](semana_02_super_simulado.md).

## Regra de precedência

Este arquivo é o cronograma operacional vigente da Semana 2. Ele substitui as tabelas de tempo legadas dentro de `semana_02_estudo.md` quando houver divergência. A teoria da apostila permanece a fonte de conteúdo.

Cada dia possui **6 horas líquidas**:

- Sessão A: 2h50 de aquisição e aplicação;
- Sessão B: 2h50 de revisão, discursiva, questões e correção;
- consolidação administrativa: 20 minutos para caderno de erros e agendamento.

Pausas não entram na carga líquida. A ordem física de execução é sempre: Blocos 1–3, produto prático, Bloco 4, Bloco 5, Bloco 6, questões, correção e fechamento.

## Estrutura fixa

### Sessão A - 2h50

| Etapa | Tempo | Execução |
|---|---:|---|
| Bloco 1 | 55 min | teoria-base e contrastes |
| Bloco 2 | 55 min | aprofundamento, funcionamento e exemplo resolvido |
| Bloco 3 | 60 min | aplicação, caso e produto prático |

### Sessão B - 2h50

| Etapa | Tempo | Execução |
|---|---:|---|
| Bloco 4 | 35 min | revisão D+2/D+7 ou núcleo comum já ensinado |
| Bloco 5 | 40 min | Português e progressão discursiva |
| Bloco 6 | 25 min | recuperação ativa, sem conteúdo novo |
| Essenciais | 30 min | seis itens da fila D0; teto de dez |
| Correção | 25 min | análise A-D e caderno de erros |
| Fechamento | 15 min | mini revisão, confiança e checklist |

### Consolidação - 20 min

Registrar erro ou acerto inseguro, regra correta, contraste, aplicação nova, referência, data D+2, D+7 e D+21. Nenhuma questão adicional entra nesse período.

### Regra operacional do D+2

O Bloco 4 do D+2 começa pelo saldo não resolvido da fila D0, limitado a quatro itens e sempre com correção A-D. Quando o mesmo bloco também trouxer Legislação, Administração Pública ou RLM, preserve até dez minutos para a recuperação curta dessa matéria. Pare quando a correção integral não couber; eventual remanescente tem prioridade na próxima reabertura e não autoriza aumentar a carga do dia.

### Regra de leitura e ponto de parada

A apostila é fonte de estudo e consulta, não ordem para reler linearmente todas as suas páginas em D0. Na Sessão A, siga as âncoras e os assuntos listados no dia, execute ao menos o exemplo ou caso previsto e encerre aos 170 minutos com o produto prático. Subseção que não couber deve ser marcada para aprofundamento antes das questões correspondentes; ela não pode ser cobrada antecipadamente nem justificar aumento da jornada.

## Dia 1 - Redes, topologias e equipamentos

**Teoria-base:** [fundamentos e comunicação](semana_02_estudo.md#s2-d1-fundamentos), [topologias](semana_02_estudo.md#s2-d1-topologias), [meios](semana_02_estudo.md#s2-d1-meios) e [equipamentos](semana_02_estudo.md#s2-d1-repetidor-hub). **Discursiva:** [Dia 1 - recorte e tese](semana_02_dissertacoes.md#s2-disc-d1).

### Sessão A

- Bloco 1: comunicação, métricas, alcance e meios;
- Bloco 2: topologias e equipamentos por camada/função;
- Bloco 3: colisão, broadcast e diagnóstico de uma LAN.

**Ponto de parada:** desenhar uma LAN com hosts, switch, AP e roteador; marcar enlaces, VLAN, domínios de broadcast e próximo salto. Explicar em áudio por que switch não é sinônimo de roteador.

### Sessão B

- Bloco 4: Legislação CFA/CRA já ensinada;
- Bloco 5: leitura de comandos e tese do Dia 1 do caderno discursivo;
- Bloco 6: recuperação de hub/switch, colisão/broadcast e largura de banda/throughput/goodput;
- fila D0: S2D1Q001 a S2D1Q006; avançar em ordem até S2D1Q010 somente com correção integral.

## Dia 2 - OSI, TCP/IP, IPv4, IPv6 e CIDR

**Teoria-base:** [modelo OSI](semana_02_estudo.md#s2-d2-osi), [encapsulamento](semana_02_estudo.md#s2-d2-encapsulamento), [IPv4 e CIDR](semana_02_estudo.md#s2-d2-ipv4) e [IPv6](semana_02_estudo.md#s2-d2-ipv6). **Discursiva:** [Dia 2 - desenvolvimento 1](semana_02_dissertacoes.md#s2-disc-d2).

### Sessão A

- Bloco 1: camadas, PDUs e encapsulamento;
- Bloco 2: IPv4, máscara, rede, broadcast, hosts e sub-redes;
- Bloco 3: IPv6, ARP/ND, ICMP e caso de endereçamento.

**Ponto de parada:** resolver manualmente os casos IPv4 `/27` e `/23`, identificando rede, broadcast e faixa de hosts. No caso IPv6, expandir/comprimir o endereço, identificar prefixo e escopo e registrar que não existe broadcast. Determinar o próximo salto somente em um cenário que informe destino, prefixo local e rota/gateway; o prefixo isolado não basta.

### Sessão B

- Bloco 4: Administração Pública já ensinada;
- Bloco 5: coesão e parágrafo argumentativo do Dia 2;
- Bloco 6: recuperação de camadas, PDU, CIDR e exceções `/31` e `/32`;
- fila D0: S2D2Q051 a S2D2Q056; teto S2D2Q060.

## Dia 3 - Protocolos e serviços

**Teoria-base:** [protocolo, serviço, porta e socket](semana_02_estudo.md#s2-d3-protocolo-porta), [TCP e UDP](semana_02_estudo.md#s2-d3-tcp-udp), [HTTP/HTTPS](semana_02_estudo.md#s2-d3-http-https) e [fluxo integrado](semana_02_estudo.md#s2-d3-fluxo-integrado). **Discursiva:** [Dia 3 - desenvolvimento 2 e contraponto](semana_02_dissertacoes.md#s2-disc-d3).

### Sessão A

- Bloco 1: protocolo, serviço, porta, socket e TCP/UDP;
- Bloco 2: HTTP, DNS, DHCP, correio e acesso/transferência remota;
- Bloco 3: SNMP, LDAP, proxy, NAT/PAT, NTP e diagnóstico integrado.

**Ponto de parada:** construir tabela com serviço, finalidade, transporte usual, porta usual e ressalva; explicar por que porta conhecida não prova identidade nem criptografia.

### Sessão B

- Bloco 4: Legislação CFA/CRA e saldo D+2 do Dia 1;
- Bloco 5: contraponto técnico do Dia 3;
- Bloco 6: recuperação por fluxo DNS → transporte → TLS → HTTP;
- fila D0: S2D3Q101 a S2D3Q106; teto S2D3Q110.

## Dia 4 - Segurança da informação e redes

**Teoria-base:** [gestão de risco](semana_02_estudo.md#s2-d4-gestao-risco), [tríade CIA](semana_02_estudo.md#s2-d4-cia), [controles](semana_02_estudo.md#s2-d4-controles) e [resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes). **Discursiva:** [Dia 4 - introdução e conclusão](semana_02_dissertacoes.md#s2-disc-d4).

### Sessão A

- Bloco 1: CIA, ameaça, vulnerabilidade, risco e ataque;
- Bloco 2: controles, firewall, DMZ, IDS/IPS, VPN, Wi-Fi, autenticação e criptografia;
- Bloco 3: resposta a incidentes, backup e caso de comprometimento.

Nesta semana, backup aparece apenas como controle de recuperação e continuidade necessário ao caso de segurança. O fechamento autônomo do item 11 do edital permanece no ciclo técnico previsto para a Semana 5.

**Ponto de parada:** entregar fluxo operacional `preparar → detectar/analisar → conter → erradicar → recuperar → retroalimentar controles`, com evidência preservada, responsável e critério de retorno. Registrar que, no NIST SP 800-61 Rev. 3, essas atividades se integram ao CSF 2.0 e podem se sobrepor; a seta organiza o raciocínio, não cria fases estanques.

### Sessão B

- Bloco 4: Administração Pública/RLM e saldo D+2 do Dia 2;
- Bloco 5: introdução e conclusão do Dia 4;
- Bloco 6: recuperação de ataque, ativo, efeito, evidência e controle;
- fila D0: S2D4Q151 a S2D4Q156; teto S2D4Q160.

## Dia 5 - Sistemas operacionais avançados

**Teoria-base:** [processo e thread](semana_02_estudo.md#s2-d5-processo-thread), [sincronização](semana_02_estudo.md#s2-d5-sincronizacao), [deadlock](semana_02_estudo.md#s2-d5-deadlock), [E/S](semana_02_estudo.md#s2-d5-dispositivos-e-s) e [sistemas de arquivos](semana_02_estudo.md#s2-d5-sistemas-arquivos). **Discursiva:** [Dia 5 - plano integral](semana_02_dissertacoes.md#s2-disc-d5).

### Sessão A

- Bloco 1: processo, thread, estados e escalonamento;
- Bloco 2: concorrência, região crítica, sincronização, starvation e deadlock;
- Bloco 3: E/S, sistemas de arquivos, permissões e caso Windows/Linux; memória permanece apenas como recuperação da Semana 1 quando surgir no caderno de erros.

**Ponto de parada:** resolver um escalonamento curto, reconhecer as quatro condições de Coffman e propor prevenção sem confundir deadlock com starvation.

### Sessão B

- Bloco 4: Legislação CFA/CRA e saldo D+2 do Dia 3;
- Bloco 5: planejamento integral da dissertação do Dia 5;
- Bloco 6: recuperação de processo/thread, mecanismo/garantia, E/S, sistema de arquivos e permissões;
- fila D0: S2D5Q201 a S2D5Q206; teto S2D5Q210.

## Dia 6 - Integração e diagnóstico

**Teoria-base:** [apostila integrada do Dia 6](semana_02_estudo.md), [revisão mista](semana_02_estudo.md#s2-d6-revisao-fixa) e [mapa localizador dos Dias 1 a 5](semana_02_estudo.md#s2-d6-rf-mapa). **Discursiva:** [Dia 6 - texto completo](semana_02_dissertacoes.md#s2-disc-d6).

### Sessão A

- Bloco 1: caminho completo da requisição e diagnóstico em camadas;
- Bloco 2: segurança, logs, continuidade e dependências;
- Bloco 3: estudo de caso integrado de rede, serviço e SO.

**Ponto de parada:** preencher matriz sintoma → camada → evidência → hipótese → teste → ação, sem escolher solução antes de confirmar a causa.

### Sessão B ajustada

| Etapa | Tempo |
|---|---:|
| Bloco 4 - revisão mista e saldo D+2 do Dia 4 | 35 min |
| Bloco 5 - dissertação completa manuscrita | 45 min |
| Bloco 6 - recuperação integrada | 20 min |
| Essenciais S2D6Q251–S2D6Q256 | 30 min |
| Correção A-D | 25 min |
| Fechamento semanal | 15 min |

O saldo S2D6Q257–S2D6Q260 abre o D+2. A dissertação deve ser corrigida pela rubrica e ter ao menos um trecho reescrito.

## D+2 que vence depois dos seis dias

- **Dia 5:** em 26/07/2026, resolver em até 35 minutos o saldo que ainda restar em S2D5Q207–S2D5Q210, com correção A-D. Se o domingo estiver reservado ao descanso, executar esse bloco antes do conteúdo novo de 27/07 e registrar honestamente o deslocamento para D+3.
- **Dia 6:** em 27/07/2026, resolver no primeiro bloco de revisão da Semana 3 o saldo que ainda restar em S2D6Q257–S2D6Q260, sem somar uma sessão extra à jornada.

## Reabertura D+7

Entre 27/07 e 01/08/2026, reabrir em até 35 minutos a fila Essencial do dia correspondente, sempre com correção A-D. Primeiro, concluir eventual saldo principal D0/D+2. Em seguida, abrir pela primeira vez as cinco extras Essenciais indicadas abaixo, em ordem. O que não couber permanece prioritário na próxima reabertura e não autoriza aumentar a carga.

| Dia de origem | Extras Essenciais de primeiro contato no D+7 |
|---:|---|
| 1 | Extra Dia 1.1–1.5 |
| 2 | Extra Dia 2.1–2.5 |
| 3 | Extra Dia 3.1–3.5 |
| 4 | Extra Dia 4.1–4.5 |
| 5 | Extra Dia 5.1–5.5 |
| 6 | Extra Dia 6.1–6.5 |

Depois dessas Essenciais, erros e acertos inseguros de confiança 0–1 têm precedência; somente se todos estiverem resolvidos e seguros, repetir sem consulta os itens de menor confiança. Questões de Aprofundamento, Revisão e Simulado não substituem essa recuperação. O super simulado só entra depois da execução dos seis dias e da correção das filas D0.

## Reabertura D+21

Entre 10 e 15/08/2026, no bloco de revisão correspondente a cada dia, recuperar oralmente o mapa central, refazer de três a cinco itens errados ou de menor confiança e conferir a regra apenas depois da resposta. Reabrir a teoria inteira ou criar uma sessão adicional não faz parte desse ciclo; lacuna persistente volta ao caderno de erros da Semana 5.

## Uso do restante do banco

- `Aprofundamento`: abrir somente depois da correção integral das Essenciais do D+2 e continuar em ciclo próprio;
- `Revisão`: usar depois da reabertura das Essenciais no D+7, conforme o tempo disponível;
- `Simulado`: reservar para o ciclo seguinte e resolver sem consulta;
- super simulado semanal: executar em tempo contínuo apenas depois dos seis dias e das filas D0 corrigidas.
