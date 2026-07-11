# Super Simulado — Semana 2

**Finalidade:** 60 questões inéditas e integradoras de Redes, Segurança e Sistemas Operacionais Avançados, em nível alto de dificuldade.

**Aplicação sugerida:** 4h30 sem consulta. Registre incertezas antes de conferir o gabarito e relacione cada erro ao mapa de conexões do dia correspondente.

## Bloco 1 — Redes, equipamentos e endereçamento

### Questão 1

Em uma LAN, o host A envia tráfego a servidor remoto. O switch de acesso conhece o MAC do gateway, mas não o do servidor remoto. A sequência correta é:

A) A envia quadro ao MAC do gateway; cada roteador remove e recria o quadro do próximo enlace.  
B) A resolve por ARP o MAC do servidor remoto e o quadro atravessa todos os roteadores intacto.  
C) A envia pacote IP diretamente ao switch, sem quadro de enlace.  
D) A usa DNS para descobrir o MAC do gateway.

### Questão 2

Para `172.16.34.190/27`, a alternativa correta é:

A) rede `172.16.34.192`, broadcast `172.16.34.223`, hosts de 193 a 222.  
B) rede `172.16.34.160`, broadcast `172.16.34.192`, hosts de 161 a 191.  
C) rede `172.16.34.0`, broadcast `172.16.34.255`, 254 hosts.
D) rede `172.16.34.160`, broadcast `172.16.34.191`, hosts de 161 a 190.  

### Questão 3

Considere as assertivas sobre equipamentos.

I. Hub repete sinais e não aprende MAC.  
II. Switch reduz colisões por porta, mas não elimina broadcast por si só.  
III. Roteador delimita domínios de broadcast ao encaminhar entre redes.

Está correto o que se afirma em:

A) I e II, apenas.  
B) I, II e III.
C) I e III, apenas.  
D) II e III, apenas.  

### Questão 4

Em IPv6, a alternativa correta sobre descoberta de vizinhos é:

A) usa broadcast ARP idêntico ao IPv4.  
B) depende obrigatoriamente de DHCPv4.  
C) usa ICMPv6/Neighbor Discovery e não emprega broadcast IPv6.  
D) substitui roteamento por DNS.

### Questão 5

Um enlace de 1 Gbit/s apresenta throughput de 820 Mbit/s, goodput de 760 Mbit/s e atraso variável. A interpretação correta é:

A) goodput inclui mais overhead que throughput.  
B) a variação de atraso é jitter, e goodput mede dados úteis entregues.  
C) 1 Gbit/s é a latência máxima.  
D) jitter é sinônimo de perda de pacote.

### Questão 6

O modelo OSI e TCP/IP devem ser comparados de modo que:

A) OSI seja referência conceitual e TCP/IP uma arquitetura/suíte, com correspondência aproximada.  
B) cada camada OSI tenha exatamente uma camada TCP/IP correspondente.  
C) ambos sejam protocolos de roteamento.  
D) TCP/IP não possua camada de aplicação.

### Questão 7

Uma rota `0.0.0.0/0` em tabela IPv4 representa:

A) rede local com dois hosts.  
B) endereço de loopback.  
C) broadcast limitado.
D) rota padrão aplicável quando não há rota mais específica.  

### Questão 8

Em uma topologia física em estrela com hub central, é correto afirmar que:

A) cada estação constitui domínio de colisão independente.  
B) o hub aprende MAC e filtra tráfego.  
C) a topologia lógica pode compartilhar meio e colisões, apesar da estrela física.  
D) o hub roteia entre VLANs.

### Questão 9

Uma estação com máscara `/31` deve ser interpretada como:

A) LAN comum de zero hosts.  
B) rota padrão.  
C) caso especial, normalmente aplicável a enlace ponto a ponto, sem subtrair dois mecanicamente.  
D) máscara inválida em qualquer cenário.

### Questão 10

Ao encapsular dados de aplicação em TCP/IP, a PDU na camada de enlace é normalmente denominada:

A) segmento, sempre.  
B) quadro.  
C) pacote, sempre.  
D) socket.

## Bloco 2 — Protocolos, serviços e segurança

### Questão 11

Um cliente recebe endereço, máscara, gateway e DNS; resolve um nome; acessa portal HTTPS. A sequência funcional mais adequada é:

A) DHCP, DNS, transporte, TLS e HTTP.  
B) DNS, DHCP, SMTP, TLS.  
C) ARP, LDAP, FTP e HTTP.  
D) NTP, ICMP, SFTP e TLS.

### Questão 12

Sobre HTTP/3, assinale a correta.

A) elimina TLS.  
B) é SMTP sobre TCP/25.  
C) torna DNS desnecessário.
D) usa normalmente QUIC sobre UDP/443.  

### Questão 13

Em uma política de correio, SMTP, IMAP e POP3 se relacionam, respectivamente, a:

A) envio, acesso/sincronização e recuperação de mensagens.  
B) criptografia, roteamento e NAT.  
C) configuração IP, nomes e tempo.  
D) autenticação, autorização e auditoria.

### Questão 14

SFTP e FTPS diferem porque:

A) ambos são necessariamente o mesmo protocolo.  
B) FTPS é terminal remoto e SFTP é correio.  
C) nenhum oferece proteção de canal.
D) SFTP transfere arquivos sobre SSH; FTPS é FTP protegido por TLS.  

### Questão 15

Uma porta TCP/UDP conhecida:

A) prova conteúdo seguro independentemente do endpoint.  
B) é convenção de serviço, não prova isolada do protocolo efetivo ou da segurança.  
C) identifica unicamente um usuário.  
D) substitui certificado digital.

### Questão 16

Em SNMP, manager, agent, MIB e OID correspondem a:

A) cliente, servidor web, banco e usuário.  
B) camadas OSI.  
C) elementos de gerenciamento e identificação de objetos monitorados.  
D) etapas de DHCP.

### Questão 17

PAT permite que vários fluxos internos compartilhem endereço público principalmente por:

A) substituição de DNS por ARP.  
B) tradução adicional de portas.  
C) criação de certificados.  
D) eliminação de roteamento.

### Questão 18

Um certificado TLS válido demonstra, em condições normais, que:

A) a identidade associada à chave foi validada conforme a cadeia e o canal pode ser autenticado/protegido.  
B) o endpoint está livre de malware.  
C) o conteúdo da aplicação é verdadeiro.  
D) o usuário recebeu autorização para qualquer recurso.

### Questão 19

Qual associação entre ataque e efeito está correta?

A) sniffing: necessariamente altera dados.  
B) DDoS: garante confidencialidade.  
C) phishing: atualiza sistemas.
D) spoofing: falsifica identidade ou origem.  

### Questão 20

Em defesa em profundidade, a afirmação correta é:

A) MFA torna atualização de sistemas dispensável.  
B) VPN elimina necessidade de controle de acesso do endpoint.  
C) segmentação, autenticação, atualização e monitoramento reduzem dependência de barreira única.  
D) firewall substitui backup.

## Bloco 3 — Criptografia, controles e continuidade

### Questão 21

Assinale a alternativa correta sobre hash, HMAC e assinatura digital.

A) hash cifra reversivelmente; HMAC dispensa segredo.  
B) assinatura serve apenas para ocultar conteúdo.  
C) HMAC usa chave secreta; assinatura é produzida com chave privada e verificada com a pública.  
D) hash substitui certificado.

### Questão 22

Uma DMZ é empregada para:

A) colocar servidor público em mesma rede de bancos internos.  
B) isolar serviços expostos e controlar fluxos para redes internas.  
C) eliminar necessidade de firewall.  
D) dispensar atualização de servidores.

### Questão 23

IDS e IPS diferem porque:

A) IDS detecta/alerta, enquanto IPS pode atuar em linha para bloquear.  
B) IDS sempre bloqueia e IPS só registra.  
C) ambos são backups.  
D) ambos substituem VPN.

### Questão 24

WPA3-Personal melhora autenticação de acesso sem fio ao usar:

A) WEP.  
B) broadcast para autenticar.  
C) apenas endereço MAC.
D) SAE, sem dispensar senha forte e configuração segura.  

### Questão 25

Em incidente de ransomware, restaurar imediatamente antes de conter persistência é inadequado porque:

A) a ameaça pode permanecer ativa e comprometer a recuperação.  
B) backup nunca deve ser usado.  
C) RPO elimina necessidade de investigação.  
D) logs não são evidência.

### Questão 26

RPO de 15 minutos e RTO de 4 horas significam, respectivamente:

A) prazo de restabelecimento e frequência obrigatória de backup.  
B) disponibilidade e confidencialidade.  
C) tamanho do backup e tempo de retenção.
D) perda máxima tolerável de dados e prazo desejado de restabelecimento.  

### Questão 27

RAID não substitui backup versionado porque:

A) RAID sempre fica offline.  
B) replicação pode propagar exclusão, corrupção ou cifração maliciosa.  
C) backup não possui cópias.  
D) RAID não melhora disponibilidade.

### Questão 28

Uma assinatura digital fornece principalmente:

A) compressão de dados.  
B) anonimato obrigatório.  
C) integridade e vínculo verificável com o signatário, conforme o contexto criptográfico.  
D) roteamento seguro.

### Questão 29

Segurança da informação como gestão de risco exige:

A) comprar um produto e encerrar revisões.  
B) identificar contexto, ativos, ameaças, vulnerabilidades, impacto, tratamento e monitoramento.  
C) eliminar todas as ameaças existentes.  
D) focar somente em software.

### Questão 30

Autenticação multifator combina fatores de naturezas distintas para:

A) provar identidade com evidências independentes, não apenas repetir senha.  
B) substituir autorização.  
C) eliminar logs.  
D) tornar phishing impossível.

## Bloco 4 — Sistemas operacionais avançados

### Questão 31

Uma condição de corrida depende de:

A) existência obrigatória de rede.  
B) uso de memória somente leitura.  
C) término de todas as threads.
D) ordem de intercalação sobre estado compartilhado sem sincronização adequada.  

### Questão 32

O conjunto clássico de condições de Coffman inclui:

A) broadcast, NAT, DNS e DHCP.  
B) autenticação, autorização, auditoria e não repúdio.  
C) exclusão mútua, posse e espera, não preempção e espera circular.  
D) paginação, segmentação, cache e DMA.

### Questão 33

Starvation ocorre quando:

A) participantes esperam circularmente sem progresso conjunto.  
B) todas as threads terminam.  
C) uma tarefa pode ser adiada indefinidamente enquanto outras avançam.  
D) o sistema de arquivos perde consistência.

### Questão 34

Livelock difere de deadlock porque no livelock:

A) recursos são sempre liberados.  
B) participantes podem mudar de estado repetidamente, mas sem progresso útil.  
C) não há execução alguma.  
D) a CPU está desligada.

### Questão 35

Em escalonamento, tempo de resposta mede:

A) intervalo até a primeira resposta perceptível ao usuário.  
B) somente o tempo total de CPU.  
C) espaço ocupado no disco.  
D) perda de dados tolerável.

### Questão 36

Um semáforo contador é adequado para:

A) substituir todas as permissões de arquivo.  
B) garantir ausência de deadlock em qualquer desenho.  
C) armazenar dados de aplicação.
D) representar quantidade de unidades equivalentes disponíveis.  

### Questão 37

DMA é preferível a cópia controlada por CPU, principalmente, quando:

A) há transferência de blocos e se deseja reduzir intervenção por unidade.  
B) é necessário calcular CIDR.  
C) o dispositivo não possui driver.  
D) se quer substituir interrupções em todo caso.

### Questão 38

Uma DACL do Windows contém:

A) somente endereços IP.  
B) registros DNS.  
C) páginas de memória.
D) ACEs de permissão ou negação, possivelmente herdadas.  

### Questão 39

Em Linux, ao avaliar `rwx` para dono, grupo e outros, é incorreto:

A) verificar identidade e grupo efetivos.  
B) somar permissões entre tríades como se fossem um único direito universal.  
C) separar leitura, escrita e execução.  
D) considerar ACL quando aplicável.

### Questão 40

Uma aplicação responde a ping, mas não atende na porta esperada. A análise deve:

A) concluir saúde total do serviço.  
B) ignorar logs.  
C) separar conectividade IP de transporte, processo, firewall e aplicação.  
D) restaurar backup sem diagnóstico.

## Bloco 5 — Estudo de caso integrado

### Questão 41

Um portal recebe DDoS, apresenta credenciais reutilizadas e banco acessível indevidamente. A ordem mais defensável é:

A) publicar senhas para acelerar análise.  
B) conter impacto, preservar evidências, bloquear vetores, erradicar persistência e recuperar.  
C) restaurar sem revogar acessos.  
D) ignorar logs por serem volumosos.

### Questão 42

Para limitar movimento lateral após comprometimento de estação, é mais diretamente útil:

A) segmentação de rede e controles de acesso.  
B) aumentar tamanho de cache.  
C) trocar IPv4 por IPv6 sem política.  
D) remover todos os logs.

### Questão 43

Uma consulta DNS funciona, mas HTTPS falha por certificado expirado. Isso demonstra que:

A) DNS garante certificado válido.  
B) HTTPS dispensa transporte.  
C) certificado substitui resolução de nomes.
D) DNS e validação TLS resolvem camadas/problemas distintos.  

### Questão 44

Em acesso remoto, VPN estabelecida não autoriza usuário a qualquer recurso porque:

A) VPN elimina identidade.  
B) VPN só funciona em LAN.  
C) túnel protegido e autorização são controles distintos.  
D) autorização é responsabilidade do DNS.

### Questão 45

Logs de firewall, aplicação e sistema só permitem correlação confiável se:

A) todos usarem POP3.  
B) forem descartados após incidente.  
C) relógios possuírem referência de tempo coerente, como NTP bem configurado.  
D) houver apenas um host.

### Questão 46

Uma restauração atende RPO, mas falha em validar integrações do negócio. A conclusão é:

A) continuidade está integralmente validada.  
B) recuperar dados não basta; é preciso testar dependências e serviço.  
C) RTO não importa.  
D) backup é redundância.

### Questão 47

No fluxo de requisição, NAT/PAT pode:

A) traduzir endereço e, com PAT, porta, sem substituir a aplicação HTTP.  
B) resolver nome DNS.  
C) gerar assinatura digital.  
D) escalonar threads.

### Questão 48

O princípio CIA mais diretamente afetado por alteração não autorizada de cadastro é:

A) disponibilidade.  
B) confidencialidade somente.  
C) não repúdio exclusivamente.
D) integridade.  

### Questão 49

Uma senha armazenada corretamente deve, em regra, ser:

A) guardada por função de derivação/hash apropriada com sal, não reversível como cifra comum.  
B) cifrada com chave pública do usuário e exibida em log.  
C) compartilhada entre contas administrativas.  
D) substituída por endereço MAC.

### Questão 50

Em autenticação de serviço web, certificado válido e MFA não eliminam:

A) necessidade de DNS.  
B) todo uso de logs.  
C) necessidade de rede.
D) necessidade de autorização e de correção de vulnerabilidades da aplicação.  

## Bloco 6 — Revisão de alta dificuldade

### Questão 51

Assinale a combinação correta: protocolo para diretório, para gerência e para sincronização de tempo.

A) SMTP, DNS e DHCP.  
B) LDAP, SNMP e NTP.  
C) SFTP, ARP e ICMP.  
D) HTTP, PAT e TLS.

### Questão 52

O uso de `Get-Process`, ao contrário de `Stop-Process`, caracteriza:

A) exclusão de arquivo.  
B) alteração de DACL.  
C) observação de processos, não alteração de estado.  
D) restauração de backup.

### Questão 53

Em roteamento, a rota mais específica normalmente:

A) é ignorada se existir gateway.  
B) prevalece sobre rota padrão para destino correspondente.  
C) só existe em IPv6.  
D) substitui ARP local.

### Questão 54

Se a aplicação usa UDP, é correto afirmar que:

A) não há garantias nativas de ordenação/retransmissão, mas a aplicação pode criar mecanismos próprios.  
B) não pode obter confiabilidade adicional.  
C) todo datagrama chega duplicado.  
D) TCP passa a ser obrigatório.

### Questão 55

Qual técnica oferece confidencialidade reversível por chave?

A) hash.  
B) checksum sem chave.  
C) assinatura isolada.
D) criptografia.  

### Questão 56

Em um incidente, erradicação significa:

A) somente detectar alerta.  
B) apagar todas as evidências.  
C) eliminar causa/persistência maliciosa após contenção, antes da recuperação controlada.  
D) aplicar RPO.

### Questão 57

Uma ACL permissiva demais em servidor de arquivos é principalmente problema de:

A) latência.  
B) CIDR.  
C) autorização.  
D) NTP.

### Questão 58

Na análise de tráfego, endereço MAC é relevante principalmente:

A) para resolver nomes globalmente.  
B) no enlace local, não como identificador fim a fim roteável.  
C) para cifrar HTTP.  
D) para autenticar pessoa usuária.

### Questão 59

Um proxy reverso diante de vários servidores de aplicação pode contribuir para:

A) publicação controlada e distribuição de requisições, conforme configuração.  
B) substituir banco de dados.  
C) eliminar TLS.  
D) criar endereços IP por DHCP.

### Questão 60

O melhor uso do caderno de erros após o simulado é:

A) registrar somente a letra certa.  
B) apagar questões erradas.  
C) repetir respostas sem diagnóstico.
D) classificar a falha, escrever regra, contraexemplo e seção de recuperação.  

## Gabarito

| Questão | Resposta |
|---:|:---:|
| 1 | A |
| 2 | D |
| 3 | B |
| 4 | C |
| 5 | B |
| 6 | A |
| 7 | D |
| 8 | C |
| 9 | C |
| 10 | B |
| 11 | A |
| 12 | D |
| 13 | A |
| 14 | D |
| 15 | B |
| 16 | C |
| 17 | B |
| 18 | A |
| 19 | D |
| 20 | C |
| 21 | C |
| 22 | B |
| 23 | A |
| 24 | D |
| 25 | A |
| 26 | D |
| 27 | B |
| 28 | C |
| 29 | B |
| 30 | A |
| 31 | D |
| 32 | C |
| 33 | C |
| 34 | B |
| 35 | A |
| 36 | D |
| 37 | A |
| 38 | D |
| 39 | B |
| 40 | C |
| 41 | B |
| 42 | A |
| 43 | D |
| 44 | C |
| 45 | C |
| 46 | B |
| 47 | A |
| 48 | D |
| 49 | A |
| 50 | D |
| 51 | B |
| 52 | C |
| 53 | B |
| 54 | A |
| 55 | D |
| 56 | C |
| 57 | C |
| 58 | B |
| 59 | A |
| 60 | D |

## Comentários

### Comentário da Questão 1

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de encapsulamento roteado no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** encapsulamento roteado.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 2

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de CIDR no cenário proposto.

**Conceito:** CIDR.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 3

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de equipamentos no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** equipamentos.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de IPv6 e ND no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** IPv6 e ND.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 5

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de métricas no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** métricas.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 6

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de OSI e TCP/IP no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** OSI e TCP/IP.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 7

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de rota padrão no cenário proposto.

**Conceito:** rota padrão.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 8

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de topologia física e lógica no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** topologia física e lógica.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 9

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de prefixos especiais no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** prefixos especiais.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 10

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de PDU de enlace no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** PDU de enlace.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de fluxo de serviços no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** fluxo de serviços.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 12

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de HTTP/3 no cenário proposto.

**Conceito:** HTTP/3.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 13

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de correio no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** correio.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 14

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de transferência segura no cenário proposto.

**Conceito:** transferência segura.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 15

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de portas no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** portas.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 16

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de SNMP no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** SNMP.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 17

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de PAT no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** PAT.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 18

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de TLS no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** TLS.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 19

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de spoofing no cenário proposto.

**Conceito:** spoofing.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 20

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de defesa em profundidade no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** defesa em profundidade.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 21

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de hash, HMAC e assinatura no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** hash, HMAC e assinatura.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 22

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de DMZ no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** DMZ.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 23

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de IDS e IPS no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** IDS e IPS.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 24

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de WPA3 no cenário proposto.

**Conceito:** WPA3.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 25

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de resposta a ransomware no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** resposta a ransomware.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 26

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de RPO e RTO no cenário proposto.

**Conceito:** RPO e RTO.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 27

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de RAID e backup no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** RAID e backup.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 28

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de assinatura digital no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** assinatura digital.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 29

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de gestão de risco no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** gestão de risco.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 30

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de MFA no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** MFA.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 31

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de condição de corrida no cenário proposto.

**Conceito:** condição de corrida.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 32

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de Coffman no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** Coffman.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 33

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de starvation no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** starvation.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 34

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de livelock no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** livelock.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 35

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de métricas de escalonamento no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** métricas de escalonamento.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 36

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de semáforo no cenário proposto.

**Conceito:** semáforo.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 37

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de DMA no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** DMA.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 38

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de DACL no cenário proposto.

**Conceito:** DACL.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 39

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de permissões Linux no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** permissões Linux.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 40

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de diagnóstico em camadas no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** diagnóstico em camadas.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 41

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de resposta a incidente no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** resposta a incidente.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 42

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de segmentação no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** segmentação.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 43

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de DNS e TLS no cenário proposto.

**Conceito:** DNS e TLS.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 44

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de VPN e autorização no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** VPN e autorização.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 45

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de NTP e logs no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** NTP e logs.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 46

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de validação de recuperação no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** validação de recuperação.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 47

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de NAT e PAT no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** NAT e PAT.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 48

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de integridade no cenário proposto.

**Conceito:** integridade.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 49

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de senhas no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** senhas.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 50

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de controles complementares no cenário proposto.

**Conceito:** controles complementares.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 51

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de LDAP, SNMP e NTP no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** LDAP, SNMP e NTP.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 52

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de comandos de observação no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** comandos de observação.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 53

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de rotas específicas no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** rotas específicas.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 54

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de UDP no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** UDP.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 55

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de criptografia no cenário proposto.

**Conceito:** criptografia.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 56

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de erradicação no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** erradicação.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 57

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Correta. Aplica a regra de autorização no cenário proposto.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** autorização.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 58

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Correta. Aplica a regra de MAC no enlace no cenário proposto.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** MAC no enlace.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 59

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica a regra de proxy reverso no cenário proposto.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.

**Conceito:** proxy reverso.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.

### Comentário da Questão 60

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **B)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **C)** Incorreta. Confunde função, camada, garantia ou limite técnico do caso.
- **D)** Correta. Aplica a regra de caderno de erros no cenário proposto.

**Conceito:** caderno de erros.

**Pegadinha:** aceitar uma afirmação parcialmente verdadeira que desloca o conceito para outra camada ou finalidade.

**Como pensar:** identifique o objetivo técnico, a condição do cenário e o controle ou protocolo que realmente o atende.

**Referência:** Semana 2 — teoria, mapa de conexões e caderno de erros do dia correspondente.
