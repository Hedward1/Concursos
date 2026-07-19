# Super Simulado — Semana 2

**Finalidade:** 60 questões inéditas e integradoras de Redes, Segurança e Sistemas Operacionais Avançados, com dificuldade calibrada pelo esforço real de resolução.

**Aplicação sugerida:** 2h30 sem consulta para responder; faça a correção integral em sessão posterior de até 2h30. Este tempo pertence ao material suplementar e não reproduz a aplicação oficial, cuja objetiva e discursiva compartilham o período previsto no edital. Registre incertezas antes de conferir o gabarito e relacione cada erro ao mapa de conexões do dia correspondente.

## Cobertura programática auditada

O super simulado contém exatamente dez itens de cada dia. A dificuldade foi atribuída pelo esforço cognitivo real, sem cotas artificiais.

| Dia | Conteúdo predominante | Questões |
|---:|---|---|
| 1 | Comunicação de dados, topologias, meios e equipamentos | S2S003, S2S005, S2S008, S2S022, S2S029, S2S030, S2S048, S2S049, S2S050, S2S055 |
| 2 | Modelos, endereçamento, encapsulamento e roteamento | S2S001, S2S002, S2S004, S2S006, S2S007, S2S009, S2S010, S2S053, S2S058, S2S060 |
| 3 | Protocolos e serviços de rede | S2S011, S2S012, S2S013, S2S014, S2S015, S2S016, S2S017, S2S051, S2S054, S2S059 |
| 4 | Segurança de redes, criptografia e continuidade | S2S018, S2S019, S2S020, S2S021, S2S023, S2S024, S2S025, S2S026, S2S027, S2S028 |
| 5 | Sistemas operacionais avançados | S2S031, S2S032, S2S033, S2S034, S2S035, S2S036, S2S037, S2S038, S2S039, S2S052 |
| 6 | Diagnóstico, incidentes e integração operacional | S2S040, S2S041, S2S042, S2S043, S2S044, S2S045, S2S046, S2S047, S2S056, S2S057 |

## Bloco 1 — Redes, equipamentos e endereçamento

### S2S001 — Encapsulamento roteado

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento), com apoio de [Gateway padrão](semana_02_estudo.md#s2-d2-gateway) e [ARP](semana_02_estudo.md#s2-d2-arp).

Em uma LAN, o host A envia tráfego a servidor remoto. O switch de acesso conhece o MAC do gateway, mas não o do servidor remoto. A sequência correta é:

A) A envia pacote IP diretamente ao switch, sem quadro de enlace.
B) A resolve por ARP o MAC do servidor remoto e o quadro atravessa todos os roteadores intacto.
C) A envia quadro ao MAC do gateway; cada roteador remove e recria o quadro do próximo enlace.
D) A usa DNS para descobrir o MAC do gateway.

### S2S002 — CIDR

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts) e [Exemplos resolvidos de IPv4 e CIDR](semana_02_estudo.md#s2-d2-calculos).

Para `172.16.34.190/27`, a alternativa correta é:

A) rede `172.16.34.192`, broadcast `172.16.34.223`, hosts de 193 a 222.
B) rede `172.16.34.160`, broadcast `172.16.34.192`, hosts de 161 a 191.
C) rede `172.16.34.0`, broadcast `172.16.34.255`, 254 hosts.
D) rede `172.16.34.160`, broadcast `172.16.34.191`, hosts de 161 a 190.

### S2S003 — Equipamentos

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios), com os detalhes de [Repetidores e hubs](semana_02_estudo.md#s2-d1-repetidor-hub), [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch) e [Roteadores](semana_02_estudo.md#s2-d1-roteador-gateway-ap).

Considere as assertivas sobre equipamentos.

I. Hub repete sinais e não aprende MAC.
II. Switch reduz colisões por porta, mas não elimina broadcast por si só.
III. Roteador delimita domínios de broadcast ao encaminhar entre redes.

Está correto o que se afirma em:

A) I e II, apenas.
B) I, II e III.
C) I e III, apenas.
D) II e III, apenas.

### S2S004 — IPv6 e ND

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [ICMPv6 e Neighbor Discovery](semana_02_estudo.md#s2-d2-icmp) e [IPv6](semana_02_estudo.md#s2-d2-ipv6).

Um host IPv6 precisa enviar um pacote a uma rede remota e ainda não conhece o endereço de enlace do roteador local. A ação correta é:

A) emitir ARP em broadcast para obter o endereço de enlace do servidor remoto.
B) usar Neighbor Discovery por ICMPv6 para resolver o próximo salto e manter o IPv6 remoto no pacote.
C) consultar DNS para obter o endereço de enlace associado ao gateway configurado.
D) solicitar uma concessão DHCPv4 antes de construir o quadro destinado ao roteador.

### S2S005 — Métricas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Comunicação de dados — medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).

Um enlace de 1 Gbit/s apresenta throughput de 820 Mbit/s, goodput de 760 Mbit/s, latência média de 20 ms e variação de 8 ms. A interpretação correta é:

A) os 760 Mbit/s representam dados úteis, e os 8 ms representam jitter do enlace.
B) os 820 Mbit/s representam capacidade nominal, e os 20 ms representam goodput.
C) a diferença entre 1 Gbit/s e 820 Mbit/s mede somente a perda física de pacotes.
D) a diferença entre throughput e goodput corresponde necessariamente à latência média.

### S2S006 — OSI e TCP/IP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelo TCP/IP e correspondência com o OSI](semana_02_estudo.md#s2-d2-tcpip).

Ao relacionar o modelo OSI à arquitetura TCP/IP, deve-se considerar que:

A) o OSI descreve a implementação da Internet, enquanto TCP/IP serve apenas como modelo abstrato.
B) a camada Internet do TCP/IP reúne aplicação, apresentação e sessão do modelo OSI.
C) as sete camadas do OSI correspondem de forma biunívoca às quatro camadas do TCP/IP.
D) o OSI organiza funções conceituais, e TCP/IP agrupa algumas delas em uma correspondência aproximada.

### S2S007 — Rota padrão

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Limites do cálculo CIDR — prefixo /0](semana_02_estudo.md#s2-d6-rf-mx-03) e [Gateway padrão](semana_02_estudo.md#s2-d2-gateway).

Uma tabela possui `10.20.30.0/24` via interface local e `0.0.0.0/0` via `10.20.30.1`. Para o destino `198.51.100.8`, a entrada usada é:

A) a rota local `/24`, porque toda rota conectada prevalece para qualquer destino.
B) uma rota de loopback, porque o destino não pertence ao prefixo diretamente ligado.
C) a rota `/0`, porque nenhuma entrada mais específica da tabela corresponde ao destino.
D) uma rota de broadcast, porque o próximo salto está dentro da rede diretamente ligada.

### S2S008 — Topologia física e lógica

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias) e [Funcionamento do hub](semana_02_estudo.md#s2-d1-repetidor-hub).

Duas salas usam o mesmo cabeamento físico em estrela. Na primeira, o equipamento central é um hub; na segunda, um switch full-duplex. A conclusão correta é:

A) ambas apresentam o mesmo comportamento lógico, pois o desenho físico determina o acesso ao meio.
B) ambas têm estrela física, mas apenas a sala com hub mantém o meio lógico compartilhado e sujeito a colisões.
C) a sala com hub possui enlaces seletivos, enquanto a sala com switch repete todos os sinais.
D) a sala com switch forma uma malha física, enquanto a sala com hub forma um barramento físico.

### S2S009 — Prefixos especiais

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplo E — /31 ponto a ponto](semana_02_estudo.md#s2-d2-calculos), dentro das regras de [rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).

Uma ferramenta de inventário rejeita as interfaces `192.0.2.10/31` e `192.0.2.11/31` de um enlace ponto a ponto porque as classifica como rede e broadcast. O enlace, porém, está operacional. O diagnóstico correto é:

A) a ferramenta aplicou a regra de LAN convencional; nesse uso de `/31`, os dois endereços podem representar as extremidades.
B) a interface `.11` continua reservada a broadcast; o enlace funciona apenas porque algum roteador executa proxy ARP.
C) o prefixo `/31` equivale à rota padrão e, por isso, aceita qualquer par de endereços IPv4 no mesmo enlace.
D) a comunicação comprova erro de máscara; enlaces ponto a ponto IPv4 precisam usar, obrigatoriamente, prefixo `/30`.

### S2S010 — Unidades na captura Ethernet

**Nível:** Médio

**Uso:** Simulado

**Referência:** [PDUs](semana_02_estudo.md#s2-d2-pdus), aplicada à identificação dos três cabeçalhos observados na captura.

Uma ferramenta captura uma requisição HTTPS em uma LAN Ethernet e separa os cabeçalhos Ethernet, IPv4 e TCP. Qual alternativa nomeia corretamente as unidades de dados correspondentes a essas três camadas?

A) Ethernet como quadro, IPv4 como pacote e TCP como segmento.

B) Ethernet como segmento, IPv4 como quadro e TCP como pacote.

C) Ethernet como pacote, IPv4 como socket e TCP como quadro.

D) Ethernet como quadro, IPv4 como segmento e TCP como bits.

## Bloco 2 — Protocolos, serviços e segurança

### S2S011 — Fluxo de serviços

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Fluxo integrado de acesso a um portal](semana_02_estudo.md#s2-d3-fluxo-integrado).

Um cliente recebeu configuração por DHCP, alcança o gateway e abre o portal pelo endereço IP, mas falha somente quando usa o nome `portal.exemplo`. O próximo teste mais informativo é:

A) verificar a fila SMTP, pois o correio publica o endereço usado pelo navegador.
B) renovar a concessão DHCP, embora endereço, rota e gateway já estejam funcionais.
C) testar NTP, pois a sincronização de tempo resolve nomes antes de iniciar o HTTPS.
D) consultar o resolvedor e os registros DNS, antes de investigar transporte ou TLS do portal.

### S2S012 — HTTP/3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [HTTP e HTTPS](semana_02_estudo.md#s2-d3-http-https), com o contraste de transporte em [TCP × UDP](semana_02_estudo.md#s2-d3-tcp-udp).

Uma captura mostra tráfego UDP/443 com pacotes QUIC durante a abertura de um portal, seguido de falha na validação do certificado. A leitura correta é:

A) o tráfego só pode ser DNS, porque HTTPS sempre depende exclusivamente de TCP.
B) o uso de UDP elimina a autenticação do servidor e torna o certificado irrelevante.
C) a captura prova que o nome foi resolvido por QUIC, sem participação do serviço DNS.
D) o fluxo é compatível com HTTP/3, que usa QUIC/UDP e ainda incorpora proteção e validação TLS.

### S2S013 — Correio

**Nível:** Médio

**Uso:** Simulado

**Referência:** [SMTP, POP3 e IMAP](semana_02_estudo.md#s2-d3-email).

Uma organização precisa transferir mensagens entre servidores, manter pastas sincronizadas em vários dispositivos e oferecer acesso simples por download. A associação correta é:

A) IMAP para transferência entre servidores, POP3 para sincronização e SMTP para download.
B) POP3 para transferência entre servidores, SMTP para sincronização e IMAP para download.
C) SMTP para transferência, IMAP para sincronização e POP3 para acesso simples às mensagens.
D) SMTP para sincronização, IMAP para transferência e POP3 para resolução dos destinatários.

### S2S014 — Transferência segura

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [FTP, FTPS, SFTP, SSH e Telnet](semana_02_estudo.md#s2-d3-transferencia-remota).

Ao liberar transferência segura em um firewall, o administrador precisa distinguir SFTP de FTPS explícito. A afirmação correta é:

A) SFTP inicia em 21/TCP e negocia canais de dados FTP, enquanto FTPS usa apenas 22/TCP.
B) SFTP e FTPS usam a mesma sessão SSH, mudando apenas o certificado apresentado ao cliente.
C) SFTP opera como subsistema SSH; FTPS mantém controle e dados do FTP protegidos por TLS.
D) SFTP protege apenas o controle, enquanto FTPS transfere arquivos sem proteger o canal de dados.

### S2S015 — Portas

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Protocolo, serviço, porta e socket — portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).

Um sensor identifica conexões destinadas à porta 443. A conclusão tecnicamente adequada é:

A) todo fluxo contém HTTPS válido, ainda que a aplicação use outro protocolo nessa porta.
B) a porta sugere o serviço esperado, mas conteúdo, identidade e proteção exigem outras evidências.
C) cada conexão pertence a um único usuário, pois a porta de destino funciona como credencial.
D) o número da porta valida o servidor, dispensando certificado e inspeção do protocolo negociado.

### S2S016 — SNMP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp).

Um sistema consulta periodicamente o uso de CPU de um roteador e recebe uma notificação quando uma interface cai. Nesse fluxo:

A) o manager consulta o agent por OIDs definidos na MIB, e o agent pode emitir notificações de evento.
B) o agent organiza toda a árvore de objetos, enquanto a MIB identifica apenas uma instância numérica.
C) a MIB envia consultas ao manager, e o OID funciona como agente instalado no equipamento.
D) o OID substitui o transporte SNMP, e a MIB atua como protocolo de configuração dinâmica do roteador.

### S2S017 — PAT com portas de origem iguais

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat), especialmente a tabela de associações entre endereços e portas.

Dois hosts internos, ambos usando a porta de origem `50000`, acessam simultaneamente o mesmo serviço TCP, no mesmo endereço IP e porta de destino, pela única IPv4 pública do gateway. Qual ação do PAT permite devolver cada resposta ao host correto?

A) Atribuir portas públicas distintas e manter cada associação com a tupla interna correspondente.

B) Traduzir somente o endereço de origem e usar o endereço do servidor para distinguir as respostas.

C) Conservar a mesma porta pública para os dois fluxos e dispensar estado no gateway.

D) Atribuir portas públicas distintas, mas descartar o vínculo com endereço e porta internos após enviar a requisição.

### S2S018 — TLS

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado) e [TLS](semana_02_estudo.md#s2-d4-tls).

Um navegador valida nome, validade, uso e cadeia do certificado apresentado por um portal. Esse resultado permite concluir que:

A) o servidor está livre de código malicioso e a aplicação executa sem vulnerabilidades conhecidas.
B) todo conteúdo entregue pelo portal é verdadeiro e foi previamente auditado pela autoridade certificadora.
C) a chave apresentada foi vinculada ao nome validado, apoiando a autenticação e a proteção do canal.
D) qualquer usuário autenticado no canal recebeu autorização para consultar todos os recursos internos.

### S2S019 — Spoofing

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).

Em uma LAN, quadros passam a anunciar o IP do gateway associado ao MAC do atacante; em seguida, parte do tráfego é desviada e capturada. A falsificação que viabilizou o desvio caracteriza:

A) sniffing, pois a captura passiva cria por si só a associação falsa entre IP e MAC.
B) spoofing, pois houve falsificação da identidade ou da origem aparente antes da captura do tráfego.
C) phishing, pois alterar a origem de quadros exige que a vítima informe credenciais em uma página falsa.
D) DDoS, pois todo anúncio de origem forjada tem como objetivo necessário saturar o serviço.

### S2S020 — Defesa em profundidade

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles), com os limites específicos de [Firewall](semana_02_estudo.md#s2-d4-firewall), [VPN](semana_02_estudo.md#s2-d4-vpn) e [Backup](semana_02_estudo.md#s2-d4-backup).

Uma conta com MFA é comprometida por sequestro de sessão, e o invasor tenta alcançar servidores e cifrar dados. A resposta de arquitetura mais coerente é:

A) confiar somente no MFA, pois um segundo fator cobre sessões roubadas e vulnerabilidades do endpoint.
B) ampliar apenas o firewall de borda, mantendo rede interna plana e cópias de dados acessíveis on-line.
C) substituir atualização e monitoramento por VPN, já que o túnel autenticado controla qualquer ação interna.
D) combinar revogação de sessão, segmentação interna, correções, monitoramento e backup isolado testado.

## Bloco 3 — Criptografia, controles e continuidade

### S2S021 — Hash, HMAC e assinatura

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas) e [Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado).

Ao proteger uma mensagem entre duas partes que compartilham segredo e, em outro fluxo, produzir prova verificável por terceiros, devem ser usados, respectivamente:

A) HMAC com segredo compartilhado e assinatura com chave privada verificável pela chave pública.
B) hash simples sem chave e cifração simétrica apresentada como assinatura do remetente.
C) certificado sem assinatura e HMAC calculado somente com a chave pública do destinatário.
D) checksum público e hash reversível que permita recuperar a identidade do signatário.

### S2S022 — Estrela física com hub e switch

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias), em conjunto com [Repetidores e hubs](semana_02_estudo.md#s2-d1-repetidor-hub) e [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch).

Duas salas possuem cabeamento físico em estrela. Na sala X, o equipamento central é um hub Ethernet em half-duplex; na sala Y, é um switch com enlaces full-duplex. Qual conclusão relaciona corretamente a disposição física e o comportamento lógico?

A) X e Y eliminam o meio compartilhado, pois a estrela física impede colisões em qualquer equipamento central.

B) X forma malha lógica por repetir sinais, enquanto Y forma barramento físico ao aprender endereços MAC.

C) X e Y têm estrela física; X mantém meio lógico compartilhado, enquanto Y segmenta os enlaces por porta.

D) X separa colisões por porta, enquanto Y repete cada sinal recebido para todas as demais interfaces.

### S2S023 — IDS e IPS

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [IDS e IPS](semana_02_estudo.md#s2-d4-ids-ips).

Uma equipe quer observar tráfego por uma porta espelhada sem interferir no fluxo e, em outro ponto, bloquear padrões maliciosos antes que cheguem ao servidor. A combinação adequada é:

A) IPS fora do caminho para apenas alertar e IDS em linha para descartar os pacotes detectados.
B) dois IPS fora do caminho, pois uma cópia do tráfego basta para impedir a entrega ao servidor.
C) dois IDS em linha, pois todo sistema de detecção bloqueia automaticamente a sessão suspeita.
D) IDS no ponto de observação e IPS em linha, com política para interromper o tráfego identificado.

### S2S024 — WPA3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi).

Durante a migração para WPA3-Personal, o ponto de acesso mantém modo de transição e uma senha fraca. A avaliação correta é:

A) SAE protege também as associações WPA2 mantidas pelo modo de transição; por isso, a captura do handshake legado deixa de depender da força da senha.
B) anunciar WPA3 no modo de transição faz clientes legados negociarem SAE automaticamente, impedindo que permaneçam em WPA2-Personal.
C) SAE melhora a troca autenticada, mas senha fraca, downgrade, firmware e configuração ainda exigem controle.
D) ativar proteção de quadros de gerenciamento torna secundária a força da senha, pois esse controle substitui a resistência da autenticação a tentativas de adivinhação.

### S2S025 — Resposta a ransomware

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes).

Arquivos foram cifrados, uma credencial administrativa foi reutilizada e o agente malicioso ainda mantém comunicação externa. Há backup isolado de duas horas atrás. A sequência mais defensável é:

A) restaurar o backup, manter a credencial ativa para investigação e bloquear a comunicação ao final.
B) isolar os ativos, preservar evidências, revogar acessos, bloquear o vetor, erradicar e então restaurar validando o serviço.
C) apagar os registros locais, reinstalar apenas o antivírus e restaurar os dados sobre o ambiente ainda ativo.
D) manter os ativos conectados até concluir a coleta, restaurar em paralelo e revogar acessos somente após o retorno.

### S2S026 — RPO e RTO

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Backup e disponibilidade — RPO e RTO](semana_02_estudo.md#s2-d4-backup).

Um incidente ocorre às 10h18. O ponto consistente mais recente é 10h05 e o serviço volta às 14h. Com RPO de 15 minutos e RTO de 4 horas, conclui-se que:

A) ambos foram atendidos: a perda potencial é de treze minutos e a indisponibilidade, de três horas e quarenta e dois minutos.
B) somente o RTO foi violado, pois o prazo deve ser contado desde o ponto recuperado das 10h05.
C) somente o RPO foi violado, pois treze minutos de perda excedem o objetivo estabelecido.
D) nenhum pode ser avaliado, pois RPO e RTO dependem exclusivamente da frequência nominal dos backups.

### S2S027 — RAID e backup

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).

Um volume em RAID 1 continua disponível após a falha de um disco, mas todos os arquivos são cifrados por uma conta comprometida. Há snapshots isolados e versionados. A interpretação correta é:

A) o RAID tratou a falha física; a recuperação lógica depende de uma versão íntegra, isolada e previamente testada.
B) o RAID deveria desfazer a cifração, pois espelhamento mantém automaticamente uma cópia histórica dos arquivos.
C) os snapshots substituem a redundância de disco, pois qualquer versão recuperável mantém o serviço continuamente disponível.
D) a troca do disco restaura os arquivos anteriores, desde que o novo componente possua capacidade igual ou maior.

### S2S028 — Assinatura digital

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia) e [Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado).

Um relatório deve permanecer confidencial para o destinatário e permitir que terceiros verifiquem autoria e integridade. O desenho adequado é:

A) assinar com a chave pública do destinatário e publicar a chave privada usada para a verificação.
B) calcular hash sem assinatura e cifrar o relatório com a chave privada do remetente.
C) cifrar para o destinatário e assinar o conteúdo com a chave privada do remetente, validando ambas as operações.
D) aplicar apenas HMAC com segredo compartilhado, permitindo verificação pública por qualquer terceiro.

### S2S029 — Meio para enlace entre prédios

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Meios de transmissão](semana_02_estudo.md#s2-d1-meios), especialmente os critérios de alcance, capacidade e interferência usados na comparação entre cobre, fibra e comunicação sem fio.

Um conselho precisa interligar dois prédios separados por 2 km, atravessando uma área com forte interferência eletromagnética, e sustentar 10 Gbit/s no backbone. Há dutos disponíveis entre os prédios. Qual solução atende de modo mais consistente às três restrições?

A) Fibra óptica com transceptores compatíveis, pois combina alcance, capacidade e imunidade eletromagnética no enlace.

B) Fibra óptica com transceptores de 1 Gbit/s homologados para 2 km, priorizando alcance e imunidade no enlace.

C) Rádio ponto a ponto de 10 Gbit/s dimensionado para 2 km, sem estudo de espectro na área de forte interferência.

D) Par trançado 10GBASE-T em trechos de 100 m, com gabinetes ativos sucessivos dentro dos dutos sujeitos à interferência.

### S2S030 — Aprendizado e inundação no switch

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch), nos trechos sobre aprendizado pelo MAC de origem, inundação de unicast desconhecido e aprendizado da resposta.

Em uma VLAN, um switch recebe pela porta 1 um quadro do host A para o host B. A tabela ainda não contém nenhum dos dois MACs. B recebe o quadro por outra porta e responde. Qual sequência descreve corretamente o comportamento do switch?

A) Aprende B na porta 1, descarta o primeiro quadro e transmite a resposta por todas as portas da VLAN.

B) Aprende A na porta 1, envia o primeiro quadro apenas ao roteador e mantém B desconhecido após a resposta.

C) Não aprende endereço algum, converte o primeiro quadro em broadcast e encaminha a resposta ao roteador.

D) Aprende A na porta 1, inunda o primeiro quadro na VLAN e aprende B na porta pela qual chega a resposta.

## Bloco 4 — Sistemas operacionais avançados

### S2S031 — Condição de corrida

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Seção crítica, condição de corrida e atomicidade](semana_02_estudo.md#s2-d5-corrida-atomicidade).

Um saldo vale 100. Duas threads leem esse valor antes de qualquer gravação; uma calcula 70 e a outra, 50, e ambas gravam depois. A conclusão correta é:

A) o saldo final será sempre 20, porque as duas subtrações são atomicamente combinadas pelo processador.
B) pode ocorrer atualização perdida, deixando 70 ou 50; a seção leitura-cálculo-gravação precisa de sincronização.
C) existe deadlock, pois toda leitura concorrente cria espera circular entre as threads participantes.
D) existe somente starvation, pois uma das duas gravações necessariamente deixa de executar indefinidamente.

### S2S032 — Coffman

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Deadlock — condições necessárias de Coffman](semana_02_estudo.md#s2-d5-deadlock).

Um sistema exige que todos os locks sejam adquiridos segundo uma ordem global crescente. Se a regra for obedecida, ela previne deadlock principalmente porque:

A) impede ciclos de dependência, rompendo a condição de espera circular mesmo que outras condições persistam.
B) introduz preempção obrigatória, retirando de uma thread cada recurso antes de nova aquisição.
C) elimina a exclusão mútua, permitindo que qualquer thread use simultaneamente todos os recursos.
D) impede posse e espera, pois toda thread passa a adquirir exatamente um recurso por execução.

### S2S033 — Starvation

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

Em uma fila de prioridade, requisições urgentes chegam continuamente e uma tarefa de baixa prioridade nunca recebe CPU. Qual ajuste enfrenta diretamente o problema descrito?

A) aumentar o quantum de todas as tarefas sem alterar a prioridade acumulada durante a espera.
B) ordenar a aquisição de locks, embora a tarefa não esteja bloqueada esperando recursos circulares.
C) reiniciar a tarefa sempre que uma requisição urgente chegar, preservando sua prioridade original.
D) aplicar aging, elevando gradualmente a prioridade da tarefa que permanece aguardando.

### S2S034 — Livelock

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

Dois workers detectam conflito, liberam o recurso e tentam novamente após o mesmo intervalo; ambos repetem a reação indefinidamente. A medida mais adequada é:

A) impedir qualquer liberação de recurso, convertendo cada nova tentativa em espera bloqueada permanente.
B) introduzir espera aleatória ou assimetria de prioridade para quebrar o ciclo ativo sem progresso.
C) aumentar igualmente a frequência das tentativas, mantendo a resposta simétrica dos dois workers.
D) substituir o recurso por memória somente leitura, sem verificar se as operações precisam modificá-lo.

### S2S035 — Métricas de escalonamento

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

No FCFS não preemptivo, P1 chega em `t=0` com burst 5 e P2 chega em `t=1` com burst 2. Para P2, resposta, espera e retorno são, respectivamente:

A) 1, 4 e 6 unidades, pois a resposta é contada desde o início da execução de P1.
B) 4, 4 e 6 unidades, pois P2 inicia em `t=5` e termina em `t=7`.
C) 4, 6 e 7 unidades, pois espera e retorno são medidos a partir de `t=0`.
D) 5, 5 e 2 unidades, pois o burst de P2 determina diretamente seu retorno.

### S2S036 — Semáforo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

Um pool possui três conexões e um semáforo contador inicia em 3. Três threads executam `wait`; uma quarta tenta adquirir, e depois uma das três executa `post`. O comportamento esperado é:

A) a quarta thread entra imediatamente antes do `post`, pois o contador pode assumir valor negativo sem bloqueio.
B) o `post` encerra a quarta thread, pois a operação serve para revogar uma aquisição pendente.
C) as três primeiras bloqueiam entre si, pois semáforo contador permite somente uma thread no pool.
D) a quarta thread bloqueia e pode prosseguir após o `post`, quando uma unidade volta a ficar disponível.

### S2S037 — DMA

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).

Uma interface recebe blocos grandes e a CPU está sobrecarregada com interrupções por pequenas unidades transferidas. O desenho mais adequado é:

A) usar polling contínuo da CPU durante todo o bloco, eliminando o controlador e o driver do dispositivo.
B) gerar uma interrupção por byte, preservando a mesma sobrecarga e retirando o uso de buffers.
C) configurar DMA para mover o bloco e usar interrupção de conclusão, mantendo driver e tratamento de erros.
D) transferir o bloco por DNS, pois a resolução de nomes reduz a participação da CPU na entrada e saída.

### S2S038 — DACL

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).

Uma pasta herda `Modificar` para o grupo Financeiro, mas Ana, integrante do grupo, deve apenas ler essa subpasta. Uma forma coerente de expressar a exceção na DACL é:

A) manter a leitura necessária e aplicar ACE explícita que negue a Ana os direitos de alteração, verificando o efeito da herança.
B) criar um registro DNS para Ana, pois nomes individuais prevalecem sobre permissões herdadas do grupo.
C) alterar a rota da estação de Ana, pois a DACL avalia o próximo salto antes de verificar as ACEs.
D) conceder `Controle total` diretamente a Ana, pois uma permissão explícita individual sempre restringe os direitos herdados do grupo.

### S2S039 — Permissões Linux

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).

Um arquivo regular `relatorio.sh`, com modo `764`, e o diretório `dados`, com modo `750`, pertencem ao usuário `root` e ao grupo `ti`. Ana não é proprietária, pertence ao grupo `ti` e não há ACL estendida. Ao combinar a classe aplicável com o significado de `r`, `w` e `x`, assinale a alternativa **INCORRETA**:

A) no arquivo, Ana pode ler e gravar, mas não executá-lo, porque para o grupo a tríade é `rw-`.
B) no diretório, Ana pode listar nomes e atravessar o caminho, mas não criar ou remover entradas, pois ao grupo falta `w`.
C) o proprietário possui `rwx` nos dois objetos, porque a primeira tríade vale `7` em ambos os modos.
D) Ana pode executar o arquivo ao combinar o `x` da tríade do proprietário com o `rw-` de seu grupo.

### S2S040 — Diagnóstico em camadas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [IPv6, próximo salto e protocolos de controle](semana_02_estudo.md#s2-d6-rf-mx-04) e [Protocolos: transporte, Web, nomes e configuração](semana_02_estudo.md#s2-d6-rf-mx-05).

O nome resolve, o host responde a ICMP e o processo aparece escutando localmente em 443, mas a conexão remota expira após uma alteração de firewall. O próximo diagnóstico deve:

A) renovar o endereço por DHCP, embora resolução, rota e alcance IP já tenham sido comprovados.
B) testar o caminho TCP e as regras entre origem e servidor antes de atribuir a falha ao TLS ou à aplicação.
C) substituir o certificado, pois timeout anterior ao handshake demonstra expiração da credencial TLS.
D) restaurar os dados da aplicação, pois uma porta inacessível comprova corrupção do armazenamento.

## Bloco 5 — Estudo de caso integrado

### S2S041 — Resposta a incidente

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 4 — Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes).

Um portal sofre saturação externa, uso de credenciais reutilizadas e consultas indevidas ao banco. A ação coordenada mais defensável é:

A) mitigar o tráfego e revogar as credenciais reutilizadas, restaurando o banco imediatamente sem preservar evidências nem verificar persistência.
B) isolar o banco e preservar seus registros, mantendo o portal exposto e as credenciais ativas até concluir a recuperação para não alterar o cenário.
C) mitigar o tráfego, revogar acessos, preservar e correlacionar evidências, conter o banco e recuperar após erradicar as causas.
D) mitigar a saturação, preservar evidências e recuperar o banco, adiando a revogação das credenciais e dispensando a análise da autorização que permitiu as consultas.

### S2S042 — Segmentação

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dia 4 — Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao).

Uma estação comprometida deve acessar apenas o proxy; o proxy acessa a aplicação, e somente a aplicação consulta o banco. A política que melhor limita movimento lateral é:

A) separar as zonas e autorizar estação→proxy, proxy→aplicação e também estação→aplicação, desde que os dois acessos usem HTTPS.
B) separar estação e banco, mas manter proxy e aplicação na mesma zona com permissão ampla dessa zona para consultar o banco.
C) separar as quatro zonas e autorizar estação→proxy, proxy→aplicação, proxy→banco e aplicação→banco, restringindo todos esses fluxos às portas usadas.
D) separar as zonas e autorizar apenas estação→proxy, proxy→aplicação e aplicação→banco nos fluxos necessários.

### S2S043 — DNS e TLS

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 3 — DNS](semana_02_estudo.md#s2-d3-dns), [Dia 4 — Assinatura e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado) e [Dia 4 — TLS](semana_02_estudo.md#s2-d4-tls).

Após uma troca de servidor, alguns clientes resolvem o nome para o endereço novo, alcançam a porta 443 e rejeitam o certificado expirado; outros ainda usam endereço antigo em cache. A conclusão correta é:

A) renovar o certificado corrige automaticamente o cache DNS e força todos os clientes a usar o endereço novo.
B) limpar o cache torna irrelevantes nome, cadeia e validade do certificado apresentado pelo novo servidor.
C) o sucesso da conexão TCP prova que DNS e certificado estão corretos, restando apenas falha de HTTP.
D) cache e resolução determinam o endpoint; depois, TLS valida nome, cadeia e validade de sua credencial.

### S2S044 — VPN e autorização

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 4 — VPN](semana_02_estudo.md#s2-d4-vpn) e [Dia 4 — Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

Um fornecedor autentica usuário e dispositivo na VPN, mas precisa acessar somente uma aplicação de suporte, sem visibilidade das demais sub-redes. O desenho adequado é:

A) aplicar autorização por identidade e destino, limitar rotas/fluxos ao serviço necessário e registrar as ações.
B) liberar toda a rede interna, pois a autenticação do túnel já concede menor privilégio aos recursos alcançados.
C) remover a autenticação da aplicação, pois a VPN transfere automaticamente os papéis do usuário a cada sistema.
D) usar apenas DNS dividido, pois ocultar nomes impede tecnicamente o acesso por endereço aos outros segmentos.

### S2S045 — NTP e logs

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dia 3 — NTP](semana_02_estudo.md#s2-d3-ntp) e [Dia 4 — Auditoria e accounting](semana_02_estudo.md#s2-d4-identidade-auditoria).

Firewall, proxy e servidor registraram o mesmo incidente com desvios conhecidos de `+90 s`, `-30 s` e `0 s`. Para reconstruir a linha do tempo, a equipe deve:

A) ordenar apenas pelo texto das mensagens, pois diferenças de relógio não alteram a sequência aparente dos eventos.
B) preservar os registros, normalizar os horários pelos desvios e corrigir a sincronização para eventos futuros.
C) apagar as fontes divergentes e manter somente o servidor cujo relógio já estava correto durante o incidente.
D) substituir os horários por ordem de coleta, porque NTP impede qualquer correlação retrospectiva de registros.

### S2S046 — Validação de recuperação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 4 — Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup) e [Dia 6 — Resposta, continuidade e objetivos de recuperação](semana_02_estudo.md#s2-d6-rf-mx-09).

O banco foi restaurado dentro do RPO, mas a fila mantém mensagens incompatíveis e a aplicação não conclui transações antes do limite de RTO. A decisão correta é:

A) declarar sucesso, pois o atendimento ao RPO substitui os testes de integração e o objetivo de tempo.
B) descartar a fila sem análise, pois qualquer dependência externa fica fora do escopo de recuperação do serviço.
C) validar dados, esquema, fila e transações de ponta a ponta, acompanhando também o prazo de restabelecimento.
D) converter o backup em RAID, pois redundância de disco garante compatibilidade lógica entre as integrações.

### S2S047 — NAT e PAT

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 3 — NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat).

Um firewall registra `203.0.113.5:41000` acessando um portal às 14h03. Centenas de estações compartilham esse IP por PAT. Para atribuir o fluxo, é necessário:

A) consultar apenas o DNS público, pois o nome identifica a estação interna que originou a conexão.
B) usar somente o certificado do portal, pois a chave do servidor contém o endereço privado do cliente.
C) comparar apenas o IP público, pois a porta traduzida não participa da identificação mantida pelo PAT.
D) correlacionar horário e tupla pública com a tabela de traduções e, depois, com registros do host e da aplicação.

### S2S048 — LAN na sede e WAN entre estados

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Classificação por alcance e finalidade](semana_02_estudo.md#s2-d1-alcance), na comparação entre PAN, LAN, MAN e WAN sem depender apenas da tecnologia empregada.

Um conselho administra diretamente a rede Ethernet e Wi-Fi dentro de sua sede. As sedes regionais, instaladas em estados distintos, são interligadas por circuitos contratados de uma operadora. Qual classificação considera corretamente o escopo das duas estruturas?

A) As duas estruturas são WAN, pois qualquer rede com acesso sem fio ultrapassa necessariamente o edifício.

B) A rede da sede é uma LAN, e a interligação geograficamente ampla entre as sedes compõe uma WAN.

C) As duas estruturas são MAN, pois o uso de Ethernet ou Wi-Fi determina sozinho o alcance geográfico.

D) A rede da sede é uma PAN, e os circuitos entre estados formam outra LAN sob gestão da operadora.

### S2S049 — Funções de um roteador sem fio

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Roteadores, gateways e access points](semana_02_estudo.md#s2-d1-roteador-gateway-ap), com apoio de [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch), no exemplo de equipamento multifuncional.

Um equipamento doméstico possui porta WAN, quatro portas LAN Ethernet e rádio Wi-Fi. Ele encaminha tráfego entre WAN e LAN, comuta quadros entre as portas LAN e associa clientes sem fio à mesma rede local. Ao separar as funções lógicas do gabinete, qual descrição está correta?

A) A WAN e a LAN são ligadas pelo roteador, as portas LAN pelo switch e os clientes Wi-Fi pelo access point.

B) A porta WAN executa acesso Wi-Fi, as portas LAN fazem NAT e o rádio escolhe rotas entre redes distintas.

C) As portas LAN executam roteamento, o rádio funciona como hub Ethernet e a porta WAN aprende MACs da WLAN.

D) O rádio executa roteamento IP, as portas LAN atuam como repetidor e a porta WAN funciona como bridge sem fio.

### S2S050 — VLAN, access point e roteamento

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios), articulado com [Access points](semana_02_estudo.md#s2-d1-roteador-gateway-ap) e [VLANs no switch](semana_02_estudo.md#s2-d1-bridge-switch).

Um switch mantém portas nas VLANs 10 e 20. Um access point em modo bridge associa o SSID corporativo à VLAN 10, e um roteador realiza o encaminhamento autorizado entre as duas VLANs. Qual conclusão combina corretamente alcance de broadcast, papel do AP e comunicação entre as VLANs?

A) Existem dois domínios de broadcast; o AP estende a VLAN 10, mas o switch de camada 2 encaminha sozinho entre as VLANs.

B) Existem dois domínios de broadcast; o AP cria um domínio separado do Wi-Fi, e o roteador liga a WLAN às duas VLANs.

C) Existem dois domínios de broadcast; o AP estende a VLAN 10 ao Wi-Fi e a comunicação entre VLANs exige roteamento.

D) Existe um domínio de broadcast; o AP estende a VLAN 10 ao Wi-Fi, e a comunicação com a VLAN 20 exige roteamento.

## Bloco 6 — Revisão de alta dificuldade

### S2S051 — LDAP, SNMP e NTP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dia 3 — SNMP](semana_02_estudo.md#s2-d3-snmp), [Dia 3 — LDAP](semana_02_estudo.md#s2-d3-ldap) e [Dia 3 — NTP](semana_02_estudo.md#s2-d3-ntp).

O monitoramento SNMP continua funcional, autenticações baseadas em diretório falham e os horários dos logs divergem. O diagnóstico deve separar:

A) MIB para autenticação, LDAP para métricas e DHCP para corrigir os relógios dos servidores.
B) SNMP para diretório, NTP para objetos gerenciados e LDAP para conceder endereços aos clientes.
C) LDAP para o diretório, SNMP para gerência e NTP para tempo, testando cada dependência de forma independente.
D) NTP para autenticação, SNMP para resolução de nomes e LDAP para sincronização temporal dos logs.

### S2S052 — Comandos de observação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 5 — Windows e Linux: comandos pertinentes](semana_02_estudo.md#s2-d5-comandos).

Um serviço Windows falha intermitentemente. Antes de autorizar reinício, a equipe precisa observar processo, estado do serviço e eventos, preservando evidências. A sequência adequada é:

A) consultar `Get-Process`, `Get-Service` e `Get-WinEvent`; só depois executar ação de parada ou reinício aprovada.
B) iniciar por `Stop-Process`, apagar os eventos e então usar `Get-Process` para reconstruir o estado anterior.
C) alterar a DACL do executável, encerrar todos os processos e dispensar a consulta ao estado do serviço.
D) restaurar o sistema, remover os logs e usar `Get-Service` apenas para confirmar que a intervenção terminou.

### S2S053 — Rotas específicas

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Dia 2 — Gateway padrão](semana_02_estudo.md#s2-d2-gateway) e [Dia 2 — ARP](semana_02_estudo.md#s2-d2-arp).

Um host `10.0.1.10/24` possui rota `10.20.0.0/16` via `10.0.1.1`, rota `10.20.30.0/24` via `10.0.1.2` e padrão via `10.0.1.254`. Para `10.20.30.40`, ele deve:

A) usar o gateway padrão e resolver por ARP o MAC de `10.20.30.40`, pois o destino está fora da LAN.
B) escolher a rota `/24`, resolver o MAC de `10.0.1.2` e manter `10.20.30.40` como IP de destino.
C) enviar diretamente ao servidor, procurando seu MAC por ARP através de todos os roteadores intermediários.
D) usar a rota `/16` e substituir no pacote o IP de destino pelo endereço `10.0.1.1`.

### S2S054 — UDP

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 3 — TCP × UDP](semana_02_estudo.md#s2-d3-tcp-udp).

Uma aplicação sobre UDP numera mensagens, confirma recebimento, retransmite após timeout e descarta duplicatas. Nesse desenho:

A) o UDP passa a garantir ordenação e retransmissão nativas para qualquer aplicação que use a mesma porta.
B) as confirmações transformam automaticamente o fluxo em TCP e exigem o handshake de três vias.
C) a confiabilidade foi implementada acima do UDP; perdas e reordenação continuam sem tratamento nativo no transporte.
D) a numeração impede perda no caminho, tornando temporizadores e retransmissões logicamente desnecessários.

### S2S055 — Enlaces de uma malha completa

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Topologias](semana_02_estudo.md#s2-d1-topologias), no cálculo `n × (n − 1) / 2` para malha completa e na comparação entre redundância, custo e complexidade.

Seis roteadores devem formar uma malha física completa, com um enlace ponto a ponto exclusivo para cada par. Qual alternativa informa o número de enlaces e uma consequência coerente dessa topologia?

A) São 6 enlaces; cada roteador liga-se somente ao seguinte, mas a falha de qualquer enlace preserva todos os caminhos.

B) São 15 enlaces; há somente um caminho possível entre cada par, e qualquer falha de enlace desconecta seus extremos.

C) São 30 enlaces; cada direção exige cabo próprio, mas desaparece a necessidade de controlar rotas alternativas.

D) São 15 enlaces; há caminhos alternativos, mas crescem a quantidade de portas e a complexidade operacional.

### S2S056 — Erradicação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 4 — Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes).

Após comprometer uma aplicação, o invasor cria tarefa agendada, mantém token ativo e explora uma biblioteca vulnerável. A classificação correta das ações é:

A) isolar e restaurar erradicam; preservar logs recupera; corrigir a biblioteca apenas detecta o incidente.
B) isolar e revogar o token contêm; remover a tarefa e corrigir/reconstruir erradicam; restaurar e validar recuperam.
C) remover a tarefa contém; manter o token preserva evidência; restaurar antes da correção elimina a vulnerabilidade.
D) revogar o token recupera; corrigir a biblioteca detecta; validar o serviço substitui contenção e erradicação.

### S2S057 — Autorização

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 4 — Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria) e [Dia 4 — Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao).

Um usuário autentica-se por MFA e VPN, pertence ao setor Financeiro e consegue consultar objetos de outro setor porque a API confia apenas em uma ACL de rede ampla. A correção adequada é:

A) substituir a ACL ampla por uma ACL de rede por setor e continuar autorizando na API apenas pela sub-rede de origem, tomada como prova do objeto permitido.
B) validar na API somente o papel Financeiro e liberar todos os objetos alcançáveis por esse papel, sem conferir o setor associado a cada objeto.
C) manter a ACL ampla e exigir nova autenticação MFA em cada consulta, tratando a confirmação da identidade como autorização suficiente sobre o objeto.
D) aplicar autorização por papel e por objeto na aplicação, restringir fluxos e registrar decisões de acesso.

### S2S058 — MAC no enlace

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 2 — Endereço MAC](semana_02_estudo.md#s2-d2-mac).

Um cliente envia pacote a servidor remoto através de dois roteadores, sem NAT. Ao comparar capturas nos três enlaces, espera-se que:

A) os MACs de cliente e servidor permaneçam em todos os quadros, enquanto os endereços IP mudem a cada roteador.
B) cada enlace use MACs do próximo salto, enquanto os IPs de cliente e servidor permaneçam fim a fim no pacote.
C) o MAC do servidor seja resolvido pelo cliente e transportado intacto, embora o IP do gateway mude por enlace.
D) cada roteador substitua IP e porta de destino, mas preserve o quadro Ethernet originalmente emitido pelo cliente.

### S2S059 — Proxy reverso

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Dia 3 — Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy).

Um proxy reverso termina TLS, distribui requisições e encaminha o endereço de origem aos backends. A configuração mais segura é:

A) validar o certificado externo e proteger o trecho interno, mas repassar sem sobrescrever qualquer cabeçalho de origem recebido do cliente.
B) aceitar o endereço de origem somente quando inserido pelo proxy e monitorar a saúde, mas publicar os backends diretamente como contingência fora dos mesmos controles.
C) validar o certificado externo, proteger o trecho interno, aceitar cabeçalhos de origem apenas do proxy e monitorar a saúde dos backends.
D) terminar TLS no proxy, usar verificações de saúde e cifrar o trecho interno aceitando qualquer certificado apresentado pelos backends.

### S2S060 — Diagnóstico dual-stack e TLS

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [IPv6](semana_02_estudo.md#s2-d2-ipv6), [DNS](semana_02_estudo.md#s2-d3-dns) e [TLS](semana_02_estudo.md#s2-d4-tls).

Um portal publica A e AAAA. O acesso por IPv4 funciona; por IPv6, o cliente resolve o AAAA, mas não alcança o próximo salto e nunca inicia TLS. A conclusão correta é:

A) testar rota e Neighbor Discovery no caminho IPv6 antes do handshake; depois validar no TLS nome, cadeia e validade do certificado.
B) validar primeiro nome, cadeia e validade do certificado pelo endereço IPv6, pois a resolução do AAAA já comprova que o próximo salto está acessível.
C) testar apenas TCP/443 no endereço AAAA e, diante do timeout, remover o registro AAAA sem isolar rota e Neighbor Discovery no enlace local.
D) forçar o uso do registro A e atribuir a falha ao conteúdo do AAAA, pois o sucesso em IPv4 comprova também a validade do caminho e do TLS em IPv6.

## Gabarito

| Questão | Resposta |
|---:|:---:|
| 1 | C |
| 2 | D |
| 3 | B |
| 4 | B |
| 5 | A |
| 6 | D |
| 7 | C |
| 8 | B |
| 9 | A |
| 10 | A |
| 11 | D |
| 12 | D |
| 13 | C |
| 14 | C |
| 15 | B |
| 16 | A |
| 17 | A |
| 18 | C |
| 19 | B |
| 20 | D |
| 21 | A |
| 22 | C |
| 23 | D |
| 24 | C |
| 25 | B |
| 26 | A |
| 27 | A |
| 28 | C |
| 29 | A |
| 30 | D |
| 31 | B |
| 32 | A |
| 33 | D |
| 34 | B |
| 35 | B |
| 36 | D |
| 37 | C |
| 38 | A |
| 39 | D |
| 40 | B |
| 41 | C |
| 42 | D |
| 43 | D |
| 44 | A |
| 45 | B |
| 46 | C |
| 47 | D |
| 48 | B |
| 49 | A |
| 50 | C |
| 51 | C |
| 52 | A |
| 53 | B |
| 54 | C |
| 55 | D |
| 56 | B |
| 57 | D |
| 58 | B |
| 59 | C |
| 60 | A |

## Comentários

### Comentário S2S001

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Em uma LAN Ethernet, o pacote IP precisa ser encapsulado em um quadro para circular no enlace. O switch recebe e encaminha quadros, não um pacote IP “solto”.
- **B)** Incorreta. ARP atua no enlace local e não procura o MAC de um servidor situado atrás de roteadores. Para esse destino remoto, A resolve o MAC do próximo salto; além disso, o quadro não atravessa intacto todos os enlaces.
- **C)** Correta. Como o servidor está em outra rede, A mantém o IP do servidor como destino do pacote, mas endereça o quadro Ethernet ao MAC do gateway. Em cada salto, o roteador retira o invólucro de enlace recebido, processa o pacote IP e cria outro quadro adequado ao enlace de saída.
- **D)** Incorreta. DNS resolve nomes e publica dados de domínio; não descobre o endereço MAC do gateway. No IPv4 sobre Ethernet, essa associação local é obtida por ARP.

**Conceito:** Encapsulamento por enlace e entrega ao próximo salto em uma comunicação roteada.

**Pegadinha:** Confundir o destino IP fim a fim com o destino MAC do quadro atual. O servidor continua no cabeçalho IP, enquanto o gateway ocupa o campo MAC de destino no primeiro enlace.

**Como pensar:** Primeiro compare a rede do host com a rede do destino. Sendo remoto, identifique o gateway como próximo salto; depois separe o que permanece no pacote IP do que precisa ser recriado em cada enlace.

**Referência:** [Encapsulamento e desencapsulamento](semana_02_estudo.md#s2-d2-encapsulamento), com apoio de [Gateway padrão](semana_02_estudo.md#s2-d2-gateway) e [ARP](semana_02_estudo.md#s2-d2-arp).
### Comentário S2S002

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A faixa 192–223 é o bloco seguinte. O endereço 172.16.34.190 não pertence a ele.
- **B)** Incorreta. A rede .160 está correta, mas o broadcast é .191, não .192. O endereço .192 já inicia a próxima sub-rede, e .191 não pode ser tratado como host.
- **C)** Incorreta. Rede .0, broadcast .255 e 254 hosts correspondem ao recorte de um /24, não ao prefixo /27 fornecido.
- **D)** Correta. Um /27 usa máscara 255.255.255.224 e blocos de 32 endereços. O valor 190 cai no bloco 160–191: rede .160, broadcast .191 e hosts .161 a .190.

**Conceito:** Determinação de rede, broadcast e intervalo utilizável a partir do prefixo IPv4.

**Pegadinha:** Usar o primeiro endereço do bloco seguinte como broadcast. O broadcast é “próximo múltiplo menos um”, razão pela qual termina em .191.

**Como pensar:** Calcule 256 − 224 = 32 e liste os múltiplos relevantes: 128, 160 e 192. Como 160 ≤ 190 < 192, a rede começa em 160 e o broadcast é 192 − 1.

**Referência:** [Endereço de rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts) e [Exemplos resolvidos de IPv4 e CIDR](semana_02_estudo.md#s2-d2-calculos).
### Comentário S2S003

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. As assertivas I e II são verdadeiras, mas a III também é: o roteador impede, por padrão, que o broadcast local de camada 2 seja encaminhado entre suas interfaces.
- **B)** Correta. O hub apenas repete sinais e não mantém tabela MAC; o switch isola segmentos por porta, sem romper o domínio de broadcast enquanto a mesma VLAN for mantida; e o roteador separa redes e seus domínios de broadcast.
- **C)** Incorreta. A combinação omite a assertiva II. Em comparação com o hub, o switch segmenta o ambiente de colisão por porta; em enlaces full-duplex modernos, a formulação mais precisa é que não há colisões Ethernet nesses enlaces.
- **D)** Incorreta. A combinação exclui a assertiva I, embora o hub seja justamente um repetidor multiporta de camada física, sem aprendizado de MAC.

**Conceito:** Funções de hub, switch e roteador e seus efeitos sobre colisões e broadcasts.

**Pegadinha:** Interpretar “reduz colisões por porta” como se o switch eliminasse também os broadcasts. Sem VLAN ou roteamento, o broadcast continua dentro da mesma LAN.

**Como pensar:** Julgue cada assertiva pela unidade que o equipamento processa: sinal no hub, quadro/MAC no switch e pacote IP/rede no roteador. Depois forme a combinação apenas com as três assertivas já validadas.

**Referência:** [Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios), com os detalhes de [Repetidores e hubs](semana_02_estudo.md#s2-d1-repetidor-hub), [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch) e [Roteadores](semana_02_estudo.md#s2-d1-roteador-gateway-ap).
### Comentário S2S004

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. IPv6 não usa ARP nem broadcast, e o host local não procura o endereço de enlace do servidor situado atrás de roteadores.
- **B)** Correta. O host usa NS/NA do Neighbor Discovery para resolver o roteador no enlace, enquanto o pacote conserva o endereço IPv6 do servidor remoto.
- **C)** Incorreta. DNS publica e resolve dados de nomes; ele não fornece o endereço de enlace do gateway para a entrega local.
- **D)** Incorreta. DHCPv4 configura IPv4 e não é pré-requisito para a descoberta do próximo salto em uma comunicação IPv6.

**Conceito:** Neighbor Discovery do próximo salto e separação entre destino IPv6 fim a fim e endereço de enlace.

**Pegadinha:** Procurar o endereço de enlace do servidor remoto ou transportar o modelo de broadcast do ARP para o IPv6.

**Como pensar:** Determine primeiro que o destino é remoto; depois separe o IPv6 do destino, que permanece no pacote, do endereço de enlace do gateway, obtido por ND.

**Referência:** [ICMPv6 e Neighbor Discovery](semana_02_estudo.md#s2-d2-icmp) e [IPv6](semana_02_estudo.md#s2-d2-ipv6).
### Comentário S2S005

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. Goodput representa a taxa de dados úteis percebidos pela aplicação, e jitter representa a variação do atraso, aqui expressa pelos 8 ms.
- **B)** Incorreta. 820 Mbit/s é throughput observado, não capacidade nominal; 20 ms é latência média, não goodput.
- **C)** Incorreta. A diferença para a capacidade nominal pode refletir protocolos, contenção e outras limitações; ela não mede somente perda física.
- **D)** Incorreta. A diferença entre throughput e goodput decorre de overhead e retransmissões, não corresponde necessariamente à latência.

**Conceito:** Diferença entre largura de banda, throughput, goodput, latência, jitter e perda.

**Pegadinha:** Tratar toda grandeza de desempenho como “velocidade”. A unidade e a pergunta operacional distinguem capacidade, taxa útil, tempo, variação e ausência de entrega.

**Como pensar:** Use as unidades e o ponto de observação: bit/s separa capacidade, vazão e dado útil; milissegundos separam atraso médio e sua variação.

**Referência:** [Comunicação de dados — medidas de desempenho](semana_02_estudo.md#s2-d1-comunicacao-dados).
### Comentário S2S006

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A relação está invertida: OSI é o modelo conceitual de referência, enquanto TCP/IP descreve uma arquitetura e suíte efetivamente usadas.
- **B)** Incorreta. Aplicação, apresentação e sessão se relacionam à aplicação TCP/IP, não à camada Internet, que trata do encaminhamento IP.
- **C)** Incorreta. Não há relação biunívoca entre sete e quatro camadas; sessão e apresentação, por exemplo, costumam integrar a aplicação TCP/IP.
- **D)** Correta. As funções do OSI ajudam a raciocinar por camadas, mas TCP/IP reúne algumas delas, por isso a correspondência é aproximada.

**Conceito:** Modelos em camadas e correspondência funcional não exata entre OSI e TCP/IP.

**Pegadinha:** Transformar uma tabela didática de equivalência em identidade perfeita. O agrupamento de funções varia sem mudar a pilha real de protocolos.

**Como pensar:** Compare funções, não apenas nomes: identifique os agrupamentos do TCP/IP e rejeite qualquer equivalência perfeita entre as duas pilhas didáticas.

**Referência:** [Modelo TCP/IP e correspondência com o OSI](semana_02_estudo.md#s2-d2-tcpip).
### Comentário S2S007

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A rota conectada `/24` só corresponde a destinos entre `10.20.30.0` e `10.20.30.255`, não ao endereço consultado.
- **B)** Incorreta. Loopback pertence ao bloco `127.0.0.0/8`; a ausência de rota conectada não transforma o destino em retorno local.
- **C)** Correta. Como não existe correspondência mais específica, `0.0.0.0/0` seleciona o próximo salto `10.20.30.1`.
- **D)** Incorreta. A entrada `/0` expressa rota residual; ela não transforma destino remoto nem gateway em broadcast.

**Conceito:** Rota padrão e seleção por maior comprimento de prefixo.

**Pegadinha:** Aplicar a fórmula de quantidade de hosts a /0 como se a entrada fosse uma LAN convencional. No contexto da tabela de roteamento, /0 é o caminho residual.

**Como pensar:** Teste o destino contra cada prefixo e escolha o mais longo que corresponda. Se nenhum prefixo específico casar, use `/0`.

**Referência:** [Limites do cálculo CIDR — prefixo /0](semana_02_estudo.md#s2-d6-rf-mx-03) e [Gateway padrão](semana_02_estudo.md#s2-d2-gateway).
### Comentário S2S008

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. O mesmo desenho de cabos não impõe o mesmo acesso lógico ao meio; o equipamento central altera o comportamento da rede.
- **B)** Correta. O cabeamento é estrela nos dois casos, mas o hub mantém meio half-duplex compartilhado; o switch full-duplex separa os enlaces.
- **C)** Incorreta. As funções foram invertidas: o hub repete sinais, enquanto o switch aprende MAC e encaminha quadros seletivamente.
- **D)** Incorreta. Trocar hub por switch não converte estrela física em malha nem em barramento; muda a operação lógica, não a disposição dos cabos.

**Conceito:** Independência entre a disposição física da rede e a forma lógica de acesso ao meio.

**Pegadinha:** Inferir o comportamento lógico apenas pelo desenho em estrela. Trocar o dispositivo central de hub por switch muda a operação, mesmo mantendo os mesmos cabos.

**Como pensar:** Avalie separadamente a forma dos cabos e a unidade processada pelo equipamento central. Estrela física pode sustentar comportamentos lógicos diferentes.

**Referência:** [Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias) e [Funcionamento do hub](semana_02_estudo.md#s2-d1-repetidor-hub).
### Comentário S2S009

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. A ferramenta transplantou para o caso especial a reserva convencional de rede e broadcast; em enlace compatível, as duas pontas usam os dois endereços.
- **B)** Incorreta. No uso ponto a ponto do `/31`, `.11` pode identificar a segunda extremidade; o funcionamento não depende da hipótese acrescentada de proxy ARP.
- **C)** Incorreta. A rota padrão usa `/0`; `/31` identifica somente um bloco contíguo de dois endereços.
- **D)** Incorreta. `/30` é uma possibilidade, não uma obrigação; `/31` é válido no contexto ponto a ponto apropriado.

**Conceito:** Diagnóstico de ferramenta que aplica indevidamente a regra convencional de rede e broadcast a um enlace IPv4 `/31`.

**Pegadinha:** Concluir que o enlace funcional depende de proxy ARP ou de máscara errada sem antes conferir a exceção própria do `/31`.

**Como pensar:** Confronte a regra usada pela ferramenta com o tipo de enlace; em ponto a ponto compatível, não se descarta automaticamente um endereço como rede e o outro como broadcast.

**Referência:** [Exemplo E — /31 ponto a ponto](semana_02_estudo.md#s2-d2-calculos), dentro das regras de [rede, broadcast e hosts válidos](semana_02_estudo.md#s2-d2-rede-broadcast-hosts).
### Comentário S2S010

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Ethernet transporta um quadro, IPv4 forma o pacote ou datagrama de rede e TCP organiza o segmento de transporte.
- **B)** segmento pertence ao transporte, quadro ao enlace e pacote à rede; a opção desloca as três unidades.
- **C)** socket é uma extremidade de comunicação mantida pelo sistema operacional, não uma PDU do IPv4.
- **D)** segmento pertence ao TCP e bits representam a transmissão física, não as unidades atribuídas a IPv4 e TCP.

**Conceito:** associação entre cabeçalhos observados e PDUs de enlace, rede e transporte.

**Pegadinha:** tratar pacote como nome universal ou deslocar a PDU correta para a camada vizinha.

**Como pensar:** identifique cada cabeçalho da captura e percorra a sequência transporte, rede e enlace antes de comparar as associações.

**Referência:** [PDUs](semana_02_estudo.md#s2-d2-pdus), aplicada à identificação dos três cabeçalhos observados na captura.

### Comentário S2S011

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. SMTP movimenta correio e não publica o endereço de rede consumido pelo navegador.
- **B)** Incorreta. A concessão já forneceu configuração funcional; renová-la não isola uma falha que ocorre apenas ao usar o nome.
- **C)** Incorreta. NTP sincroniza relógios, mas não resolve o FQDN do portal nem substitui o serviço de nomes.
- **D)** Correta. Como o acesso por IP e o gateway funcionam, testar o resolvedor e os registros DNS isola a etapa que ainda diferencia os dois acessos.

**Conceito:** Diagnóstico por etapas entre configuração IP, resolução DNS e acesso HTTPS.

**Pegadinha:** Recomeçar pela configuração do cliente mesmo quando os testes já isolaram a falha na etapa dependente de nome.

**Como pensar:** Compare o que muda entre os dois testes. Se endereço, rota e acesso por IP funcionam e só o FQDN falha, investigue DNS antes das camadas seguintes.

**Referência:** [Fluxo integrado de acesso a um portal](semana_02_estudo.md#s2-d3-fluxo-integrado).
### Comentário S2S012

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. UDP/443 com QUIC é compatível com HTTP/3; HTTPS não está limitado a TCP nas versões atuais.
- **B)** Incorreta. QUIC integra as propriedades criptográficas aplicáveis, e a identidade do servidor continua sujeita à validação de credenciais.
- **C)** Incorreta. QUIC não substitui DNS; a resolução do nome ocorre como dependência separada antes do acesso ao endpoint.
- **D)** Correta. A captura é compatível com HTTP/3 sobre QUIC/UDP, e a falha de certificado pertence à validação TLS incorporada ao fluxo.

**Conceito:** Pilha de transporte do HTTP/3: HTTP sobre QUIC/UDP com proteção criptográfica integrada.

**Pegadinha:** Interpretar o uso de UDP como ausência de TLS ou como prova de que o tráfego não pode ser HTTPS.

**Como pensar:** Leia a pilha na ordem HTTP/3 → QUIC → UDP e mantenha separadas a resolução DNS e a validação criptográfica do servidor.

**Referência:** [HTTP e HTTPS](semana_02_estudo.md#s2-d3-http-https), com o contraste de transporte em [TCP × UDP](semana_02_estudo.md#s2-d3-tcp-udp).
### Comentário S2S013

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. IMAP acessa e sincroniza caixas; não é o protocolo de transferência entre servidores, e SMTP não é o mecanismo de download.
- **B)** Incorreta. POP3 acessa mensagens e SMTP as transfere; a sequência inverte os papéis centrais dos três protocolos.
- **C)** Correta. SMTP transfere mensagens, IMAP mantém estado e pastas sincronizados, e POP3 oferece acesso simples orientado à recuperação.
- **D)** Incorreta. SMTP não sincroniza caixas, IMAP não transfere correio entre servidores e POP3 não resolve destinatários.

**Conceito:** Separação entre envio/transferência de correio e acesso à caixa postal.

**Pegadinha:** Tratar todos os protocolos de e-mail como equivalentes. SMTP movimenta mensagens; IMAP e POP3 dão acesso à caixa, com modelos diferentes de sincronização.

**Como pensar:** Resolva cada requisito separadamente: transferência leva a SMTP, sincronização a IMAP e acesso simples/download a POP3.

**Referência:** [SMTP, POP3 e IMAP](semana_02_estudo.md#s2-d3-email).
### Comentário S2S014

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. As portas e arquiteturas foram trocadas: SFTP costuma usar SSH em 22/TCP, enquanto FTPS explícito inicia pelo controle FTP em 21/TCP.
- **B)** Incorreta. FTPS não usa a sessão SSH do SFTP; ele preserva FTP e acrescenta proteção TLS.
- **C)** Correta. SFTP é um protocolo de arquivos sobre SSH; FTPS mantém os canais do FTP e protege controle e dados conforme a negociação TLS.
- **D)** Incorreta. SFTP protege sua sessão SSH, e FTPS precisa proteger também o canal de dados; a opção inverte esses alcances.

**Conceito:** Diferença de arquitetura entre SFTP sobre SSH e FTP protegido por TLS.

**Pegadinha:** Expandir SFTP como “Secure FTP” e concluir que ele é FTP com TLS. Essa descrição pertence ao FTPS.

**Como pensar:** Identifique a pilha e o comportamento no firewall: SFTP usa SSH; FTPS mantém controle e dados do FTP sob TLS.

**Referência:** [FTP, FTPS, SFTP, SSH e Telnet](semana_02_estudo.md#s2-d3-transferencia-remota).
### Comentário S2S015

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A porta 443 é uma convenção e pode transportar serviço inesperado, conteúdo malicioso ou uma aplicação vulnerável.
- **B)** Correta. O número sugere HTTPS, mas o protocolo negociado, o certificado e a inspeção do fluxo fornecem evidência adicional.
- **C)** Incorreta. A porta identifica um ponto de entrega no host, não uma pessoa; várias conexões e usuários podem compartilhá-la.
- **D)** Incorreta. A numeração da porta não vincula nome a chave pública e não substitui a validação de certificado.

**Conceito:** Porta de transporte como identificador convencional de serviço, não como prova de identidade ou segurança.

**Pegadinha:** Converter uma heurística útil de prova — “HTTPS costuma usar 443” — em uma garantia lógica — “tudo em 443 é HTTPS seguro”.

**Como pensar:** Trate a porta como indício operacional. Confirme protocolo, identidade e proteção por evidências próprias antes de concluir que o fluxo é seguro.

**Referência:** [Protocolo, serviço, porta e socket — portas conhecidas não são uma garantia](semana_02_estudo.md#s2-d3-protocolo-porta).
### Comentário S2S016

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. O manager consulta o agent usando OIDs definidos na MIB, e notificações permitem ao agent informar eventos.
- **B)** Incorreta. O agent expõe e atualiza valores, enquanto MIB descreve a árvore e OID identifica instâncias nela.
- **C)** Incorreta. MIB organiza a estrutura de objetos, mas não é a entidade que inicia consultas; OID identifica um objeto, não executa o agent.
- **D)** Incorreta. OID e MIB não substituem o transporte nem o protocolo; SNMP também não entrega configuração dinâmica de rede.

**Conceito:** Arquitetura lógica de gerência SNMP e identificação hierárquica de objetos monitorados.

**Pegadinha:** Tratar MIB como um banco de dados comum e OID como seu usuário. A MIB descreve a estrutura dos objetos; OID é o identificador de um objeto específico.

**Como pensar:** Distribua os papéis: manager pergunta e recebe eventos, agent representa o dispositivo, MIB organiza e OID identifica.

**Referência:** [SNMP — gerenciamento e monitoramento](semana_02_estudo.md#s2-d3-snmp).
### Comentário S2S017

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** portas públicas diferentes distinguem os fluxos, enquanto a tabela preserva o vínculo com cada endereço e porta internos.
- **B)** como os dois fluxos usam o mesmo serviço no mesmo servidor, o endereço de destino não separa a qual host interno pertence cada resposta.
- **C)** fluxos indistinguíveis na interface pública não poderiam ser desmultiplexados, e o PAT depende de estado de tradução.
- **D)** portas externas diferentes só ajudam enquanto a tabela mantém o vínculo com o endereço e a porta internos de cada fluxo.

**Conceito:** desmultiplexação de fluxos por PAT e tabela de tradução com portas públicas distintas.

**Pegadinha:** reconhecer que o endereço público é compartilhado, mas ignorar o estado e a diferenciação pelas portas.

**Como pensar:** compare as tuplas dos dois fluxos e procure o campo que o gateway pode tornar diferente na interface pública.

**Referência:** [NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat), especialmente a tabela de associações entre endereços e portas.

### Comentário S2S018

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A validação do certificado não examina o endpoint em busca de malware nem prova ausência de vulnerabilidades na aplicação.
- **B)** Incorreta. A autoridade certificadora não audita a veracidade de todo conteúdo publicado pelo titular do certificado.
- **C)** Correta. Nome, cadeia, validade e uso apoiam o vínculo entre a identidade validada e a chave empregada para autenticar e proteger o canal.
- **D)** Incorreta. Autenticar o servidor e proteger o canal não autoriza automaticamente usuários em todos os recursos internos.

**Conceito:** Escopo da confiança fornecida pelo certificado e das garantias do canal TLS.

**Pegadinha:** Expandir “conexão autenticada” para “máquina limpa, conteúdo honesto e usuário autorizado”. Essas propriedades exigem controles independentes.

**Como pensar:** Delimite a prova: certificado e handshake tratam identidade da chave e canal. Estado do endpoint, conteúdo e autorização exigem controles próprios.

**Referência:** [Certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado) e [TLS](semana_02_estudo.md#s2-d4-tls).
### Comentário S2S019

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Sniffing descreve a captura do tráfego; não cria, por definição, a associação falsa entre o IP do gateway e o MAC do atacante.
- **B)** Correta. O anúncio atribui ao atacante uma identidade de rede que não lhe pertence; essa falsificação de origem é spoofing, ainda que depois possibilite captura.
- **C)** Incorreta. Phishing depende de engano dirigido à vítima, normalmente por mensagem ou página fraudulenta; o cenário descreve adulteração de origem na LAN.
- **D)** Incorreta. DDoS busca degradar a disponibilidade por volume ou exaustão; a falsificação apresentada pode servir ao desvio sem saturação.

**Conceito:** Distinção entre a falsificação de origem que desvia o tráfego e a captura que pode ocorrer depois do desvio.

**Pegadinha:** Nomear todo o encadeamento pela captura posterior e ignorar que a pergunta isola a falsificação responsável pela associação IP–MAC indevida.

**Como pensar:** Separe as etapas: primeiro alguém falsifica a origem para redirecionar; depois pode capturar. O verbo cobrado no primeiro passo é “falsificar”.

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).
### Comentário S2S020

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. MFA reduz certos ataques de credencial, mas sessão sequestrada, vulnerabilidade do endpoint e autorização permanecem riscos distintos.
- **B)** Incorreta. Firewall de borda não limita sozinho o movimento lateral nem recupera dados cifrados; rede plana e cópias on-line ampliam o impacto.
- **C)** Incorreta. VPN protege o túnel, mas não substitui correções, monitoramento ou controle de sessão dentro do ambiente.
- **D)** Correta. Revogação, segmentação, correções, detecção e backup isolado atuam em fases e superfícies diferentes do ataque.

**Conceito:** Defesa em profundidade aplicada a identidade, movimento lateral, vulnerabilidades, detecção e recuperação.

**Pegadinha:** Supor que um controle forte torna os demais dispensáveis. Defesa em profundidade existe justamente porque cada camada tem escopo e modos de falha próprios.

**Como pensar:** Liste os riscos do cenário e associe um controle a cada um. Rejeite qualquer opção que trate MFA, VPN ou firewall como barreira universal.

**Referência:** [Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles), com os limites específicos de [Firewall](semana_02_estudo.md#s2-d4-firewall), [VPN](semana_02_estudo.md#s2-d4-vpn) e [Backup](semana_02_estudo.md#s2-d4-backup).
### Comentário S2S021

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. HMAC usa segredo compartilhado para autenticar a mensagem; a assinatura é produzida com a chave privada e pode ser verificada com a pública.
- **B)** Incorreta. Hash sem chave não autentica uma parte por segredo, e cifração simétrica não produz prova publicamente verificável do signatário.
- **C)** Incorreta. Certificado precisa de assinatura e validação; HMAC não é calculado apenas com uma chave pública.
- **D)** Incorreta. Checksum não autentica origem, e hash é unidirecional, não um mecanismo reversível de recuperação de identidade.

**Conceito:** Autenticação simétrica por HMAC e prova assimétrica por assinatura digital.

**Pegadinha:** tratar resumo, autenticação com segredo, prova assimétrica e vínculo de identidade como se fossem variações do mesmo mecanismo.

**Como pensar:** Pergunte quem consegue produzir e quem consegue verificar: HMAC compartilha segredo; assinatura separa chave privada de produção e pública de verificação.

**Referência:** [Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas) e [Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado).
### Comentário S2S022

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** a estrela descreve a disposição dos enlaces, mas não determina sozinha se o meio lógico é compartilhado.
- **B)** repetição pelo hub não cria malha, e aprendizado de MAC pelo switch não muda o cabeamento físico para barramento.
- **C)** ambas são estrelas físicas; o hub repete sinais no meio compartilhado, e o switch isola os enlaces por porta.
- **D)** as funções foram invertidas; quem repete sinais é o hub, enquanto o switch faz encaminhamento seletivo.

**Conceito:** distinção entre topologia física, comportamento lógico, hub e switch.

**Pegadinha:** inferir o funcionamento lógico apenas pelo desenho físico em estrela.

**Como pensar:** decida primeiro a topologia do cabeamento e, depois, verifique se o equipamento central repete sinais ou examina endereços MAC.

**Referência:** [Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias), em conjunto com [Repetidores e hubs](semana_02_estudo.md#s2-d1-repetidor-hub) e [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário S2S023

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. O papel está invertido: IDS fora do caminho observa e alerta; IPS em linha pode bloquear segundo a política.
- **B)** Incorreta. Um IPS que recebe somente cópia não controla a entrega original e, portanto, não bloqueia o servidor por essa posição.
- **C)** Incorreta. Um IDS não ganha capacidade automática de bloqueio apenas por ser colocado em linha; a solução e a configuração precisam suportar prevenção.
- **D)** Correta. A porta espelhada atende ao IDS sem interferência, e a posição em linha permite ao IPS descartar ou interromper tráfego.

**Conceito:** posição no caminho e capacidade de resposta de sistemas de detecção e prevenção de intrusão.

**Pegadinha:** concluir pelo termo “intrusão” que os dois produtos sempre bloqueiam ou que um deles torna desnecessários outros controles.

**Como pensar:** Combine posição e ação: cópia do tráfego favorece detecção; passagem obrigatória pelo equipamento permite prevenção ativa.

**Referência:** [IDS e IPS](semana_02_estudo.md#s2-d4-ids-ips).
### Comentário S2S024

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. SAE protege a associação WPA3; clientes que permanecem em WPA2-Personal no modo de transição ainda usam o mecanismo legado e sua segurança continua ligada à força da senha.
- **B)** Incorreta. O anúncio simultâneo não converte clientes legados em clientes SAE; eles podem continuar negociando WPA2, o que mantém a superfície própria do modo de transição.
- **C)** Correta. SAE fortalece a troca autenticada, sem eliminar riscos de senha fraca, downgrade, falha de implementação ou firmware desatualizado.
- **D)** Incorreta. Proteção de quadros de gerenciamento atende outra superfície e não substitui uma senha resistente nem a autenticação SAE corretamente configurada.

**Conceito:** SAE no WPA3-Personal, modo de transição e controles operacionais complementares.

**Pegadinha:** interpretar a adoção de SAE como eliminação da senha ou como garantia contra engenharia social, falha de implementação e modo de transição inseguro.

**Como pensar:** Avalie separadamente o mecanismo SAE, a qualidade da senha e a possibilidade de transição/downgrade; melhoria criptográfica não elimina configuração segura.

**Referência:** [Segurança Wi-Fi: WPA2 e WPA3](semana_02_estudo.md#s2-d4-wifi).
### Comentário S2S025

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Restaurar antes de bloquear comunicação e revogar a credencial mantém o vetor ativo e pode comprometer novamente os dados recuperados.
- **B)** Correta. A sequência limita o dano, preserva evidências, elimina acessos e persistência e só então recupera a partir de fonte validada.
- **C)** Incorreta. Apagar registros destrói evidência, e atualizar apenas o antivírus não remove necessariamente persistência, credenciais ou vetor explorado.
- **D)** Incorreta. Manter o ambiente conectado prolonga o risco; recuperação paralela em base ainda comprometida pode reiniciar a cifração.

**Conceito:** Sequência coordenada de contenção, preservação, erradicação e recuperação diante de ransomware.

**Pegadinha:** Priorizar a restauração visível antes de interromper comunicação, acessos e persistência que podem contaminar o ponto recuperado.

**Como pensar:** Ordene pelo risco de recorrência: limite o dano e preserve evidência, remova vetor e persistência, depois restaure e valide.

**Referência:** [Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes).
### Comentário S2S026

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. Treze minutos de perda atendem ao RPO, e três horas e quarenta e dois minutos de indisponibilidade atendem ao RTO.
- **B)** Incorreta. RTO é contado desde a interrupção às 10h18 até o restabelecimento às 14h, não desde o timestamp do backup.
- **C)** Incorreta. A perda entre 10h05 e 10h18 é de treze minutos, portanto fica dentro do RPO de quinze minutos.
- **D)** Incorreta. Os objetivos podem ser avaliados pelo ponto recuperado e pelo tempo de retorno; frequência nominal não os substitui.

**Conceito:** Cálculo de RPO pela perda temporal e de RTO pela duração da indisponibilidade.

**Pegadinha:** Contar o RTO a partir do ponto do backup ou interpretar RPO como frequência obrigatória, em vez de resultado recuperável.

**Como pensar:** Subtraia 10h05 de 10h18 para o RPO e 10h18 de 14h para o RTO; compare cada intervalo com seu objetivo.

**Referência:** [Backup e disponibilidade — RPO e RTO](semana_02_estudo.md#s2-d4-backup).
### Comentário S2S027

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. O espelhamento manteve operação após a falha física, mas a cifração lógica atingiu o estado corrente; uma versão isolada permite retornar no tempo.
- **B)** Incorreta. RAID 1 replica o estado atual e pode replicar a cifração; ele não mantém automaticamente histórico recuperável.
- **C)** Incorreta. Snapshot recuperável não oferece, por si só, continuidade imediata diante de falha física; backup e redundância têm papéis diferentes.
- **D)** Incorreta. Trocar o disco reconstrói o espelho com o estado cifrado; capacidade física não restaura a versão anterior.

**Conceito:** Complementaridade entre redundância contra falha física e versão isolada contra dano lógico.

**Pegadinha:** Confundir uma segunda cópia sincronizada do estado atual com histórico independente para recuperação.

**Como pensar:** Pergunte qual falha cada mecanismo cobre: RAID mantém disponibilidade física; versão isolada permite desfazer alteração lógica.

**Referência:** [Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).
### Comentário S2S028

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Assina-se com a chave privada do remetente; publicar uma chave privada elimina sua proteção e não fornece confidencialidade adequada.
- **B)** Incorreta. Hash sem assinatura não vincula o remetente, e cifrar com a chave privada não é o desenho correto para confidencialidade ao destinatário.
- **C)** Correta. A cifração restringe a leitura ao destinatário, enquanto a assinatura do remetente fornece integridade e autoria verificável.
- **D)** Incorreta. HMAC depende de segredo compartilhado e não permite que terceiros independentes verifiquem publicamente a autoria.

**Conceito:** Composição de cifração para confidencialidade e assinatura para integridade e autoria verificável.

**Pegadinha:** Usar uma única operação para duas propriedades diferentes ou inverter as chaves usadas para assinar e cifrar.

**Como pensar:** Separe os objetivos: quem pode ler determina a cifração; quem produziu e se houve alteração determina a assinatura.

**Referência:** [Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia) e [Assinatura digital e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado).
### Comentário S2S029

**Alternativa correta: A.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** com ópticas adequadas, a fibra atende ao alcance e à capacidade e não conduz interferência eletromagnética.
- **B)** os transceptores atendem a distância e imunidade, mas limitam o enlace a 1 Gbit/s, abaixo da capacidade exigida.
- **C)** alcance e taxa nominais não dispensam o estudo de espectro justamente onde a interferência é uma restrição explícita.
- **D)** a solução multiplica pontos ativos e permanece baseada em cobre dentro da área eletromagneticamente hostil.

**Conceito:** escolha do meio a partir de alcance, capacidade e interferência eletromagnética.

**Pegadinha:** eleger um meio por uma única qualidade e ignorar as outras restrições simultâneas.

**Como pensar:** transforme alcance, vazão e interferência em três filtros e elimine qualquer alternativa que falhe em pelo menos um deles.

**Referência:** [Meios de transmissão](semana_02_estudo.md#s2-d1-meios), especialmente os critérios de alcance, capacidade e interferência usados na comparação entre cobre, fibra e comunicação sem fio.

### Comentário S2S030

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** o switch aprende o MAC de origem A na porta 1 e não possui motivo para descartar o unicast desconhecido.
- **B)** o primeiro quadro é inundado na VLAN, e a resposta permite aprender o MAC de B em sua porta de entrada.
- **C)** o switch aprende origens e não altera o endereço unicast de destino para transformá-lo em broadcast.
- **D)** há aprendizado de A, inundação do destino ainda desconhecido e posterior aprendizado de B pela resposta.

**Conceito:** sequência de aprendizado, inundação e encaminhamento de um switch de camada 2.

**Pegadinha:** supor que o switch aprende pelo destino ou que inundação muda a natureza unicast do quadro.

**Como pensar:** aplique três filtros na ordem: aprender a origem, consultar o destino e aprender a origem do quadro de resposta.

**Referência:** [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch), nos trechos sobre aprendizado pelo MAC de origem, inundação de unicast desconhecido e aprendizado da resposta.

### Comentário S2S031

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. As subtrações não formam uma operação atômica; ambas partem de 100 e uma gravação pode sobrescrever a outra.
- **B)** Correta. O ciclo leitura-cálculo-gravação sofre atualização perdida, podendo terminar em 70 ou 50 em vez de 20.
- **C)** Incorreta. Não há ciclo de espera por recursos; o defeito é uma corrida entre acessos conflitantes ao mesmo estado.
- **D)** Incorreta. As duas threads podem executar; o problema não é adiamento indefinido, mas o resultado dependente da intercalação.

**Conceito:** Atualização perdida em seção crítica composta por leitura, cálculo e gravação.

**Pegadinha:** Somar mentalmente as duas retiradas sem simular que ambas leram o mesmo valor antes das gravações.

**Como pensar:** Escreva a sequência `ler 100, ler 100, gravar 70, gravar 50` e depois inverta as gravações; a variação revela a corrida.

**Referência:** [Seção crítica, condição de corrida e atomicidade](semana_02_estudo.md#s2-d5-corrida-atomicidade).
### Comentário S2S032

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. Se todos adquirem em uma direção global, não se forma ciclo de dependência, rompendo a espera circular.
- **B)** Incorreta. A regra não retira recursos já adquiridos; não preempção pode permanecer.
- **C)** Incorreta. Ordenação não torna locks simultaneamente compartilháveis; exclusão mútua pode continuar existindo.
- **D)** Incorreta. Uma thread ainda pode manter um lock enquanto pede outro de ordem maior, portanto posse e espera não é necessariamente eliminada.

**Conceito:** Prevenção de deadlock por ordenação global e ruptura da espera circular.

**Pegadinha:** Atribuir à ordenação a ruptura de todas as condições de Coffman, em vez de identificar a condição específica afetada.

**Como pensar:** Tente desenhar um ciclo respeitando a ordem crescente. Como cada aresta só avança na ordem, o ciclo não fecha.

**Referência:** [Deadlock — condições necessárias de Coffman](semana_02_estudo.md#s2-d5-deadlock).
### Comentário S2S033

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Aumentar o quantum sem alterar prioridade não garante que a tarefa preterida seja escolhida enquanto urgentes continuam chegando.
- **B)** Incorreta. Ordenação de locks previne certos deadlocks, mas o caso é de justiça do escalonador, não de espera circular.
- **C)** Incorreta. Reiniciar a tarefa preserva ou piora o adiamento, pois ela continua com baixa prioridade a cada chegada urgente.
- **D)** Correta. Aging aumenta a prioridade com o tempo de espera e reduz a possibilidade de adiamento indefinido.

**Conceito:** Starvation em prioridade e mitigação por aging.

**Pegadinha:** Aplicar técnica de deadlock ou ajustar quantum sem tratar a causa: uma prioridade que nunca melhora.

**Como pensar:** Como o sistema progride e apenas a tarefa baixa espera, identifique starvation e escolha o mecanismo que melhora justiça ao longo do tempo.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).
### Comentário S2S034

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Impedir toda liberação pode converter o caso em bloqueio e não corrige de forma segura o protocolo de concorrência.
- **B)** Correta. Backoff aleatório ou prioridade assimétrica impede que os dois workers repitam a mesma reação no mesmo instante.
- **C)** Incorreta. Aumentar igualmente a frequência mantém a simetria e pode apenas consumir mais CPU sem progresso.
- **D)** Incorreta. Tornar o recurso somente leitura muda o requisito funcional e não resolve o protocolo se as operações precisam escrever.

**Conceito:** Livelock por reação simétrica e quebra do ciclo com backoff ou assimetria.

**Pegadinha:** Aumentar tentativas ou bloquear permanentemente, em vez de quebrar a simetria que mantém a atividade improdutiva.

**Como pensar:** Confirme atividade sem progresso e procure uma política que faça os participantes tomarem decisões diferentes na próxima tentativa.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).
### Comentário S2S035

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. P2 chega em `t=1`, não em `t=0`; portanto seu tempo de resposta não é uma unidade.
- **B)** Correta. P1 ocupa `0–5`; P2 espera quatro unidades, inicia em 5 e termina em 7, produzindo resposta 4, espera 4 e retorno 6.
- **C)** Incorreta. Espera e retorno são medidos a partir da chegada de P2, e não da origem absoluta do cronograma.
- **D)** Incorreta. Burst é serviço de CPU; ele não substitui os intervalos entre chegada, início e conclusão.

**Conceito:** Cálculo de resposta, espera e retorno em FCFS não preemptivo.

**Pegadinha:** Medir a partir de `t=0` ou confundir burst de P2 com tempo de retorno.

**Como pensar:** Desenhe `P1: 0–5` e `P2: 5–7`; subtraia a chegada `t=1` do início e da conclusão.

**Referência:** [Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).
### Comentário S2S036

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Após três aquisições, não há unidade livre; a quarta tentativa deve bloquear em vez de prosseguir livremente.
- **B)** Incorreta. `post` incrementa a disponibilidade ou acorda um interessado; não encerra a thread que aguardava.
- **C)** Incorreta. Semáforo contador admite até N usuários, não apenas um; exclusão binária seria outro caso.
- **D)** Correta. O contador modela as três conexões; `post` devolve uma unidade e permite que uma thread aguardando prossiga.

**Conceito:** Evolução de um semáforo contador em aquisição, bloqueio e liberação de um pool.

**Pegadinha:** Tratar o contador como ilimitado ou confundir `post` com cancelamento da thread em espera.

**Como pensar:** Simule 3→2→1→0; a quarta espera. Depois do `post`, uma unidade volta a estar disponível para a fila.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).
### Comentário S2S037

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Polling mantém a CPU consultando o dispositivo e não elimina controlador, driver ou custo de acompanhamento do bloco.
- **B)** Incorreta. Uma interrupção por byte preserva a frequência elevada de eventos e não aproveita a transferência em bloco.
- **C)** Correta. DMA assume o movimento repetitivo do bloco, enquanto driver e CPU configuram a operação e tratam sua conclusão e seus erros.
- **D)** Incorreta. DNS não transfere dados entre dispositivo e memória e não reduz a participação da CPU na entrada e saída local.

**Conceito:** Combinação de DMA para transferência em bloco e interrupção para sinalizar conclusão.

**Pegadinha:** Tratar DMA, interrupção e driver como alternativas excludentes, quando eles podem dividir etapas da mesma operação.

**Como pensar:** Separe configuração, movimentação e conclusão: CPU/driver configuram, DMA move e uma interrupção pode notificar o término.

**Referência:** [Dispositivos, drivers, interrupções, polling e DMA](semana_02_estudo.md#s2-d5-dispositivos-e-s).
### Comentário S2S038

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. Uma ACE explícita de negação para Ana pode limitar os direitos herdados via grupo; a equipe deve conferir o conjunto efetivo e preservar a leitura necessária.
- **B)** Incorreta. DNS não participa da avaliação de direitos sobre o objeto e não prevalece sobre ACEs herdadas ou explícitas.
- **C)** Incorreta. Roteamento decide caminho de rede; a DACL avalia sujeitos e direitos no descritor de segurança do objeto.
- **D)** Incorreta. `Controle total` amplia os direitos de Ana; o caráter explícito da ACE não a transforma automaticamente em restrição.

**Conceito:** Permissão efetiva no Windows pela interação entre associação a grupo, herança e ACE explícita.

**Pegadinha:** Tentar corrigir permissão de objeto com DNS ou rota, ou supor que toda ACE individual explícita seja restritiva independentemente dos direitos concedidos.

**Como pensar:** Liste as ACEs herdadas via grupos e a exceção necessária para Ana; depois verifique a permissão efetiva resultante.

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).
### Comentário S2S039

**Alternativa correta: D.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. Como integrante de `ti`, Ana recebe no arquivo a segunda tríade de `764`: `rw-`.
- **B)** Correta. No diretório `750`, a tríade de grupo `r-x` permite listar nomes e atravessar o caminho, mas a ausência de `w` impede criar ou remover entradas.
- **C)** Correta. Em `764` e `750`, a tríade do proprietário é `7`, isto é, `rwx`.
- **D)** Incorreta. As tríades não são somadas: Ana usa a classe de grupo e, no arquivo, não recebe o `x` reservado ao proprietário.

**Observação:** A questão pede a alternativa **INCORRETA**; por isso, D é o gabarito.

**Conceito:** Seleção da classe de permissão e diferença semântica de `r`, `w` e `x` em arquivo e diretório no Linux.

**Pegadinha:** Somar direitos de proprietário, grupo e outros ou interpretar `rwx` do mesmo modo para arquivos e diretórios.

**Como pensar:** Identifique primeiro a classe de Ana, decodifique a tríade do grupo em cada modo e só então aplique o significado dos bits ao tipo de objeto.

**Referência:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).
### Comentário S2S040

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. DHCP não é a hipótese mais informativa quando nome, rota e alcance IP já foram demonstrados.
- **B)** Correta. ICMP e socket local já funcionam; o timeout remoto após mudança de firewall direciona o teste ao caminho TCP e às regras intermediárias antes do TLS.
- **C)** Incorreta. Se o TCP não se estabelece, o handshake TLS ainda não chegou à etapa de validar o certificado.
- **D)** Incorreta. Inacessibilidade da porta não comprova dano aos dados e não justifica restauração antes do diagnóstico.

**Conceito:** Isolamento de falha entre conectividade IP, caminho TCP/firewall, socket e handshake TLS.

**Pegadinha:** Trocar certificado ou dados antes de comprovar que o transporte alcança o socket remoto.

**Como pensar:** Marque o último degrau confirmado: IP e escuta local. O próximo é testar TCP pela origem e revisar a mudança de firewall.

**Referência:** [IPv6, próximo salto e protocolos de controle](semana_02_estudo.md#s2-d6-rf-mx-04) e [Protocolos: transporte, Web, nomes e configuração](semana_02_estudo.md#s2-d6-rf-mx-05).
### Comentário S2S041

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A mitigação e a revogação tratam dois vetores, mas restaurar sem preservar evidências e sem procurar persistência deixa a causa incompleta e pode contaminar novamente o serviço.
- **B)** Incorreta. Preservar registros e isolar o banco são ações úteis, porém manter o portal exposto e as credenciais ativas prolonga os vetores enquanto a equipe recupera o ambiente.
- **C)** Correta. A resposta trata disponibilidade, identidade e banco com controles próprios, preserva evidências e condiciona a recuperação à erradicação.
- **D)** Incorreta. Adiar a revogação conserva acesso indevido, e ignorar a falha de autorização permite repetir as consultas mesmo depois de recuperar o banco.

**Conceito:** ciclo de resposta a incidentes: detecção/análise, contenção, preservação, erradicação e recuperação validada.

**Pegadinha:** escolher uma opção que reúne ações defensáveis, mas deixa um dos vetores ativo ou recupera antes de erradicar a causa.

**Como pensar:** Separe os três vetores e exija contenção específica, evidência preservada, erradicação e retorno validado.

**Referência:** [Dia 4 — Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes).
### Comentário S2S042

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A aresta estação→aplicação contorna o proxy e cria um caminho adicional justamente para o ativo já comprometido.
- **B)** Incorreta. Manter proxy e aplicação juntos e conceder à zona acesso amplo ao banco não limita os fluxos aos processos e portas estritamente necessários.
- **C)** Incorreta. Restringir portas não torna necessário o fluxo proxy→banco; essa aresta contorna a aplicação e amplia o movimento lateral possível.
- **D)** Correta. Zonas separadas e regras específicas implementam a cadeia mínima e impedem saltos não necessários.

**Conceito:** segmentação de rede combinada com política de acesso entre segmentos.

**Pegadinha:** aceitar uma aresta adicional por usar HTTPS ou por restringi-la a uma porta conhecida, embora o destino não seja necessário à missão.

**Como pensar:** Desenhe o fluxo autorizado como um grafo e rejeite qualquer aresta extra, sobretudo estação→banco.

**Referência:** [Dia 4 — Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao).
### Comentário S2S043

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Renovação de certificado não altera TTL nem invalida automaticamente caches que ainda apontam para o endpoint antigo.
- **B)** Incorreta. Limpar cache pode mudar o endereço alcançado, mas o cliente ainda precisa validar nome, cadeia e validade do certificado recebido.
- **C)** Incorreta. Conexão TCP comprova transporte até um endpoint, não a correção do cache nem a validade da credencial TLS.
- **D)** Correta. DNS escolhe o endereço conforme cache e registros; TLS avalia depois a identidade e a validade do endpoint efetivamente alcançado.

**Conceito:** separação entre resolução de nomes, transporte e validação do canal TLS.

**Pegadinha:** transformar o sucesso de uma dependência — DNS — em prova de saúde ou validade de todas as etapas seguintes.

**Como pensar:** Siga as etapas e mantenha seus estados separados: cache/resolução, transporte e validação TLS do servidor alcançado.

**Referência:** [Dia 3 — DNS](semana_02_estudo.md#s2-d3-dns), [Dia 4 — Assinatura e certificado digital](semana_02_estudo.md#s2-d4-assinatura-certificado) e [Dia 4 — TLS](semana_02_estudo.md#s2-d4-tls).
### Comentário S2S044

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. A VPN autentica e protege o caminho, enquanto rotas, ACLs e autorização por identidade limitam o fornecedor ao serviço necessário e permitem auditoria.
- **B)** Incorreta. Autenticação do túnel não concede menor privilégio; liberar toda a rede transforma identidade válida em acesso excessivo.
- **C)** Incorreta. A aplicação ainda deve autenticar e autorizar conforme seu contexto; a VPN não transfere automaticamente papéis.
- **D)** Incorreta. DNS dividido reduz descoberta por nome, mas não bloqueia acesso direto por endereço nem substitui filtragem.

**Conceito:** autenticação/proteção do túnel não implicam autorização irrestrita aos recursos internos.

**Pegadinha:** interpretar “VPN conectada” como ingresso automático em uma rede interna plana e totalmente liberada.

**Como pensar:** Responda três perguntas: quem entrou, por qual canal e a quais destinos pode chegar. Só a última exige a política de autorização e fluxo.

**Referência:** [Dia 4 — VPN](semana_02_estudo.md#s2-d4-vpn) e [Dia 4 — Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).
### Comentário S2S045

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Texto semelhante não corrige timestamps desalinhados e pode inverter causa e efeito na linha do tempo.
- **B)** Correta. Os registros brutos devem ser preservados; os desvios conhecidos permitem normalizar a análise, e a sincronização deve ser corrigida para novas evidências.
- **C)** Incorreta. Fontes divergentes ainda contêm eventos úteis; descartá-las reduz a cobertura da investigação.
- **D)** Incorreta. NTP apoia a coerência futura, mas desvios conhecidos ainda podem ser aplicados retrospectivamente sem substituir os registros originais.

**Conceito:** Normalização temporal de evidências preservadas e correção da sincronização para eventos futuros.

**Pegadinha:** Corrigir os relógios e sobrescrever evidências, ou descartar fontes apenas porque seus timestamps divergem.

**Como pensar:** Preserve o bruto, aplique os offsets numa cópia analítica e documente a correção; depois repare a fonte temporal.

**Referência:** [Dia 3 — NTP](semana_02_estudo.md#s2-d3-ntp) e [Dia 4 — Auditoria e accounting](semana_02_estudo.md#s2-d4-identidade-auditoria).
### Comentário S2S046

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. RPO cobre a perda de dados, não a compatibilidade das integrações nem o prazo de retorno do processo de negócio.
- **B)** Incorreta. Descartar fila sem análise pode perder transações e mascarar incompatibilidade entre componentes restaurados.
- **C)** Correta. Recuperação válida exige dados, esquema, fila e transações coerentes, além de atendimento ao RTO e retorno monitorado.
- **D)** Incorreta. RAID trata disponibilidade de componentes e não corrige incompatibilidade lógica de mensagens e esquema.

**Conceito:** validação funcional de recuperação, distinguindo RPO, RTO, backup e continuidade do serviço.

**Pegadinha:** considerar a restauração dos dados como prova suficiente de que todo o serviço e suas dependências estão operacionais.

**Como pensar:** Verifique três resultados independentes: ponto dos dados, prazo de retorno e execução ponta a ponta das dependências.

**Referência:** [Dia 4 — Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup) e [Dia 6 — Resposta, continuidade e objetivos de recuperação](semana_02_estudo.md#s2-d6-rf-mx-09).
### Comentário S2S047

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. DNS resolve nomes, mas não contém o vínculo temporal entre uma porta pública traduzida e a estação privada.
- **B)** Incorreta. O certificado identifica o servidor no canal; ele não revela o cliente interno oculto pelo PAT.
- **C)** Incorreta. Vários fluxos compartilham o IP público, e a porta traduzida é parte decisiva da associação.
- **D)** Correta. A tupla e o horário localizam a entrada de PAT; logs sincronizados do host e da aplicação completam a atribuição.

**Conceito:** Atribuição de fluxo PAT por tupla, horário, tabela de tradução e correlação de registros.

**Pegadinha:** Usar apenas o IP público e ignorar porta e tempo quando muitos clientes compartilham o mesmo endereço.

**Como pensar:** Reconstrua de fora para dentro: tupla pública+tempo → entrada PAT → IP/porta privada → logs do host/aplicação.

**Referência:** [Dia 3 — NAT básico e PAT/NAPT](semana_02_estudo.md#s2-d3-nat-pat).
### Comentário S2S048

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** uma WLAN pode permanecer restrita ao ambiente local, sem converter toda a estrutura em WAN.
- **B)** a rede interna da sede possui escopo local, enquanto a interligação entre estados caracteriza alcance amplo de WAN.
- **C)** MAN se associa ao escopo metropolitano; Ethernet e Wi-Fi não definem, isoladamente, a categoria geográfica.
- **D)** PAN cobre o entorno pessoal, e contratar a operadora não transforma enlaces entre estados em uma única LAN.

**Conceito:** classificação de redes por alcance, finalidade e contexto de interligação.

**Pegadinha:** classificar a rede apenas pela tecnologia de acesso ou pela entidade que opera o circuito.

**Como pensar:** classifique primeiro a rede dentro do edifício e, depois, a estrutura que conecta unidades em regiões distantes.

**Referência:** [Classificação por alcance e finalidade](semana_02_estudo.md#s2-d1-alcance), na comparação entre PAN, LAN, MAN e WAN sem depender apenas da tecnologia empregada.

### Comentário S2S049

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** o único gabinete reúne roteador entre redes, switch na LAN e access point para os clientes sem fio.
- **B)** a porta WAN não associa clientes Wi-Fi, NAT não é função das portas do switch e o rádio não substitui o roteamento.
- **C)** portas LAN do produto operam como switch, o rádio atua como access point e a WAN não aprende a WLAN como função principal.
- **D)** o rádio presta acesso sem fio, as portas LAN comutam quadros e o encaminhamento entre redes cabe ao roteador.

**Conceito:** separação entre as funções de roteador, switch e access point em produto multifuncional.

**Pegadinha:** atribuir ao gabinete inteiro uma única função e trocar os papéis de seus componentes internos.

**Como pensar:** siga três fluxos: WAN↔LAN exige roteamento, LAN↔LAN exige comutação e cliente Wi-Fi↔LAN exige access point.

**Referência:** [Roteadores, gateways e access points](semana_02_estudo.md#s2-d1-roteador-gateway-ap), com apoio de [Bridges e switches](semana_02_estudo.md#s2-d1-bridge-switch), no exemplo de equipamento multifuncional.

### Comentário S2S050

**Alternativa correta: C.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** a contagem e o papel do AP estão corretos, mas um switch de camada 2 não roteia entre as VLANs.
- **B)** o AP em bridge integra o SSID à VLAN 10; ele não cria outro domínio quando esse mapeamento já foi definido.
- **C)** VLAN 10 e VLAN 20 são dois domínios, o AP integra o SSID à VLAN 10 e a comunicação entre elas depende de camada 3.
- **D)** o papel do AP e a necessidade de roteamento estão corretos, mas duas VLANs formam dois domínios de broadcast.

**Conceito:** relação entre VLAN, domínio de broadcast, bridging do access point e roteamento entre redes.

**Pegadinha:** confundir isolamento de enlace full-duplex, SSID e separação de domínio de broadcast.

**Como pensar:** conte as VLANs, determine a VLAN transportada pelo AP e, por fim, identifique o mecanismo exigido para atravessar a fronteira entre elas.

**Referência:** [Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios), articulado com [Access points](semana_02_estudo.md#s2-d1-roteador-gateway-ap) e [VLANs no switch](semana_02_estudo.md#s2-d1-bridge-switch).

### Comentário S2S051

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. MIB organiza objetos SNMP e não autentica usuários; DHCP entrega configuração de rede, não corrige por si só relógios distribuídos.
- **B)** Incorreta. As funções foram deslocadas: SNMP não é diretório, NTP não gerencia MIB e LDAP não concede endereços IP.
- **C)** Correta. Cada sintoma é isolado em sua dependência: LDAP para autenticação/diretório, SNMP para gerência e NTP para coerência temporal.
- **D)** Incorreta. NTP sincroniza tempo, SNMP gerencia equipamentos e LDAP trata diretório; a alternativa troca os três papéis.

**Conceito:** Diagnóstico independente de diretório LDAP, gerência SNMP e sincronização NTP.

**Pegadinha:** Inferir que SNMP funcional valida LDAP ou NTP só porque os três serviços participam da mesma infraestrutura.

**Como pensar:** Mapeie cada sintoma ao serviço responsável e não use o sucesso de uma dependência como prova das outras duas.

**Referência:** [Dia 3 — SNMP](semana_02_estudo.md#s2-d3-snmp), [Dia 3 — LDAP](semana_02_estudo.md#s2-d3-ldap) e [Dia 3 — NTP](semana_02_estudo.md#s2-d3-ntp).
### Comentário S2S052

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. Os três cmdlets coletam estado e evidência; a equipe separa observação inicial de uma alteração posterior autorizada.
- **B)** Incorreta. Encerrar primeiro muda o estado e apagar eventos destrói justamente a evidência necessária ao diagnóstico.
- **C)** Incorreta. DACL não substitui diagnóstico de processo/serviço, e encerrar todos os processos é uma intervenção desproporcional.
- **D)** Incorreta. Restauração e remoção de logs alteram amplamente o ambiente antes de a falha ter sido delimitada.

**Conceito:** Sequência de diagnóstico Windows com coleta não destrutiva antes de ações sobre processo ou serviço.

**Pegadinha:** Executar a ação de recuperação antes de coletar processo, serviço e eventos que sustentam a hipótese.

**Como pensar:** Classifique cada verbo: `Get-*` observa; `Stop-*` ou reinício altera. Preserve evidência antes da mutação aprovada.

**Referência:** [Dia 5 — Windows e Linux: comandos pertinentes](semana_02_estudo.md#s2-d5-comandos).
### Comentário S2S053

**Alternativa correta: B.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A rota `/24` é mais específica que a padrão, e ARP deve resolver o próximo salto local, não o servidor remoto.
- **B)** Correta. O maior prefixo correspondente é `/24`; o quadro usa o MAC de `10.0.1.2` e o pacote mantém o destino final.
- **C)** Incorreta. O servidor remoto não está no enlace, portanto seu MAC não é descoberto através dos roteadores.
- **D)** Incorreta. Embora `/16` corresponda, `/24` também corresponde e vence; o IP de destino não é trocado pelo gateway.

**Conceito:** Maior prefixo, escolha do próximo salto e resolução ARP no enlace local.

**Pegadinha:** Escolher a primeira rota que corresponde ou resolver o MAC do destino remoto em vez do gateway vencedor.

**Como pensar:** Teste `/16`, `/24` e `/0`; escolha `/24`, leia o gateway e só então aplique ARP ao próximo salto local.

**Referência:** [Dia 2 — Gateway padrão](semana_02_estudo.md#s2-d2-gateway) e [Dia 2 — ARP](semana_02_estudo.md#s2-d2-arp).
### Comentário S2S054

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Os mecanismos pertencem à aplicação específica e não alteram as garantias nativas do UDP para outros fluxos.
- **B)** Incorreta. Implementar ACK e retransmissão não transforma automaticamente a pilha em TCP nem cria seu handshake.
- **C)** Correta. A aplicação construiu estado e recuperação sobre um transporte que continua oferecendo datagramas sem ordenação ou retransmissão nativas.
- **D)** Incorreta. Números de sequência detectam lacunas e duplicatas, mas não impedem que perdas ocorram no caminho.

**Conceito:** Confiabilidade implementada na aplicação sobre UDP sem mudar as garantias nativas do transporte.

**Pegadinha:** Confundir comportamento do protocolo de aplicação com propriedade universal do UDP ou com transformação em TCP.

**Como pensar:** Separe as camadas: identifique o que o cabeçalho UDP não faz e o que numeração, ACK e temporizador acrescentam acima dele.

**Referência:** [Dia 3 — TCP × UDP](semana_02_estudo.md#s2-d3-tcp-udp).
### Comentário S2S055

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** seis enlaces não conectam diretamente todos os quinze pares, e a descrição se aproxima de um anel, não de malha completa.
- **B)** a contagem está correta, mas a malha completa oferece caminhos indiretos quando um enlace direto falha.
- **C)** trinta conta cada par duas vezes; um enlace ponto a ponto atende à comunicação nos dois sentidos.
- **D)** `6 × 5 / 2 = 15`, e a redundância obtida exige mais interfaces, enlaces e controle operacional.

**Conceito:** cálculo de enlaces e trade-off de redundância em uma malha física completa.

**Pegadinha:** esquecer a divisão por dois ou confundir malha completa com anel de seis enlaces.

**Como pensar:** conte os pares não ordenados com `n(n−1)/2` e, depois, confira se a consequência combina redundância com maior custo.

**Referência:** [Topologias](semana_02_estudo.md#s2-d1-topologias), no cálculo `n × (n − 1) / 2` para malha completa e na comparação entre redundância, custo e complexidade.

### Comentário S2S056

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Restaurar não erradica, preservar logs não recupera o serviço e corrigir a biblioteca vai além de simples detecção.
- **B)** Correta. Isolamento e revogação limitam atividade; remover persistência e vulnerabilidade elimina causas; restauração e validação devolvem a capacidade.
- **C)** Incorreta. Remover tarefa atua sobre persistência, manter token conserva acesso indevido e restauração anterior à correção não elimina a falha.
- **D)** Incorreta. As três classificações estão trocadas e nenhuma etapa substitui as demais.

**Conceito:** Classificação de ações concretas em contenção, erradicação e recuperação.

**Pegadinha:** Classificar pelo momento cronológico sem observar o objetivo técnico de cada ação.

**Como pensar:** Pergunte o verbo: limitar atividade contém; remover causa/persistência erradica; devolver e testar o serviço recupera.

**Referência:** [Dia 4 — Resposta a incidentes](semana_02_estudo.md#s2-d4-resposta-incidentes).
### Comentário S2S057

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Sub-rede de origem é contexto de rede, não prova de que o usuário pode consultar aquele objeto; a API continuaria sem decisão por identidade e recurso.
- **B)** Incorreta. O papel restringe uma categoria de usuários, mas não basta quando o próprio objeto pertence a outro setor e exige verificação específica.
- **C)** Incorreta. Repetir MFA reforça a autenticação, porém não decide se a identidade confirmada possui autorização sobre o objeto solicitado.
- **D)** Correta. A solução combina papel, verificação do objeto, limitação de fluxo e registro da decisão, aplicando menor privilégio em camadas.

**Conceito:** Autorização por papel e objeto complementada por segmentação e auditoria.

**Pegadinha:** Confundir autenticação forte e alcance de rede com permissão de negócio sobre cada objeto.

**Como pensar:** Valide em sequência identidade, papel, objeto, caminho de rede e registro; o cenário falha nas decisões posteriores à autenticação.

**Referência:** [Dia 4 — Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria) e [Dia 4 — Segmentação e controle de acesso](semana_02_estudo.md#s2-d4-segmentacao).
### Comentário S2S058

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Endereços MAC pertencem ao enlace e mudam por salto; os IPs fim a fim não são substituídos por roteadores comuns sem NAT.
- **B)** Correta. Cada roteador desencapsula e cria novo quadro para o enlace seguinte, enquanto origem e destino IP permanecem no pacote.
- **C)** Incorreta. O cliente resolve o endereço de enlace do próximo salto, não o MAC do servidor remoto através dos roteadores.
- **D)** Incorreta. Roteamento normal não troca porta e IP de destino nem preserva o quadro Ethernet inicial fim a fim.

**Conceito:** Renovação dos endereços MAC por enlace e preservação lógica dos endereços IP sem NAT.

**Pegadinha:** Misturar os campos que pertencem ao quadro local com os que identificam a comunicação no pacote roteado.

**Como pensar:** Para cada captura, escreva `MAC origem/destino = enlace atual`; depois mantenha `IP origem/destino = cliente/servidor`.

**Referência:** [Dia 2 — Endereço MAC](semana_02_estudo.md#s2-d2-mac).
### Comentário S2S059

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. Se o proxy repassa o cabeçalho recebido sem removê-lo ou sobrescrevê-lo, o cliente pode forjar a origem que os backends tratam como confiável.
- **B)** Incorreta. Publicar diretamente os backends cria um caminho que contorna terminação TLS, política de cabeçalhos e demais controles centralizados no proxy.
- **C)** Correta. O desenho valida a borda, protege o trecho até os backends, evita falsificação de cabeçalhos confiáveis e detecta destinos indisponíveis.
- **D)** Incorreta. Cifrar sem validar a identidade do backend permite conexão com endpoint indevido; health check não substitui a autenticação do trecho TLS interno.

**Conceito:** Operação segura de proxy reverso com TLS, cabeçalhos confiáveis, backends protegidos e health checks.

**Pegadinha:** Confiar em cabeçalho de origem não validado ou supor que terminação TLS elimina a proteção e o monitoramento internos.

**Como pensar:** Verifique quatro fronteiras: cliente→proxy, proxy→backend, origem encaminhada e seleção de backend saudável.

**Referência:** [Dia 3 — Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy).
### Comentário S2S060

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. A falha ocorre antes do TLS: primeiro devem ser verificados rota e ND no IPv6; somente após o transporte cabe validar nome, cadeia e validade.
- **B)** Incorreta. Resolver o AAAA comprova DNS, mas não alcançabilidade do próximo salto; sem caminho e transporte, a validação TLS nem sequer pode começar.
- **C)** Incorreta. O timeout remoto não localiza a causa já situada antes do próximo salto; remover o AAAA mascara o defeito sem distinguir rota de Neighbor Discovery.
- **D)** Incorreta. O sucesso pelo registro A valida somente o caminho IPv4 e o TLS observado nele; não prova a correção do endereço, da rota ou do enlace IPv6.

**Conceito:** Diagnóstico dual-stack por resolução AAAA, rota/Neighbor Discovery, transporte e validação TLS.

**Pegadinha:** Culpar o certificado por falha que acontece antes do handshake ou misturar parâmetros de DHCPv4 com a pilha IPv6.

**Como pensar:** Marque o último passo comprovado: DNS retorna AAAA. Teste então rota e ND, depois transporte e só ao final TLS.

**Referência:** [IPv6](semana_02_estudo.md#s2-d2-ipv6), [DNS](semana_02_estudo.md#s2-d3-dns) e [TLS](semana_02_estudo.md#s2-d4-tls).
