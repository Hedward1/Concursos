# Super Simulado — Semana 2

**Finalidade:** 60 questões inéditas e integradoras de Redes, Segurança e Sistemas Operacionais Avançados, em nível alto de dificuldade.

**Aplicação sugerida:** 4h30 sem consulta. Registre incertezas antes de conferir o gabarito e relacione cada erro ao mapa de conexões do dia correspondente.

## Bloco 1 — Redes, equipamentos e endereçamento

### S2S001 — Encapsulamento roteado

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-02).

Em uma LAN, o host A envia tráfego a servidor remoto. O switch de acesso conhece o MAC do gateway, mas não o do servidor remoto. A sequência correta é:

A) A envia quadro ao MAC do gateway; cada roteador remove e recria o quadro do próximo enlace.
B) A resolve por ARP o MAC do servidor remoto e o quadro atravessa todos os roteadores intacto.
C) A envia pacote IP diretamente ao switch, sem quadro de enlace.
D) A usa DNS para descobrir o MAC do gateway.

### S2S002 — CIDR

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-03).

Para `172.16.34.190/27`, a alternativa correta é:

A) rede `172.16.34.192`, broadcast `172.16.34.223`, hosts de 193 a 222.
B) rede `172.16.34.160`, broadcast `172.16.34.192`, hosts de 161 a 191.
C) rede `172.16.34.0`, broadcast `172.16.34.255`, 254 hosts.
D) rede `172.16.34.160`, broadcast `172.16.34.191`, hosts de 161 a 190.

### S2S003 — Equipamentos

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

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

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-04).

Em IPv6, a alternativa correta sobre descoberta de vizinhos é:

A) usa broadcast ARP idêntico ao IPv4.
B) depende obrigatoriamente de DHCPv4.
C) usa ICMPv6/Neighbor Discovery e não emprega broadcast IPv6.
D) substitui roteamento por DNS.

### S2S005 — Métricas

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-01).

Um enlace de 1 Gbit/s apresenta throughput de 820 Mbit/s, goodput de 760 Mbit/s e atraso variável. A interpretação correta é:

A) goodput inclui mais overhead que throughput.
B) a variação de atraso é jitter, e goodput mede dados úteis entregues.
C) 1 Gbit/s é a latência máxima.
D) jitter é sinônimo de perda de pacote.

### S2S006 — OSI e TCP/IP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip).

O modelo OSI e TCP/IP devem ser comparados de modo que:

A) OSI seja referência conceitual e TCP/IP uma arquitetura/suíte, com correspondência aproximada.
B) cada camada OSI tenha exatamente uma camada TCP/IP correspondente.
C) ambos sejam protocolos de roteamento.
D) TCP/IP não possua camada de aplicação.

### S2S007 — Rota padrão

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

Uma rota `0.0.0.0/0` em tabela IPv4 representa:

A) rede local com dois hosts.
B) endereço de loopback.
C) broadcast limitado.
D) rota padrão aplicável quando não há rota mais específica.

### S2S008 — Topologia física e lógica

**Nível:** Médio

**Uso:** Simulado

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).

Em uma topologia física em estrela com hub central, é correto afirmar que:

A) cada estação constitui domínio de colisão independente.
B) o hub aprende MAC e filtra tráfego.
C) a topologia lógica pode compartilhar meio e colisões, apesar da estrela física.
D) o hub roteia entre VLANs.

### S2S009 — Prefixos especiais

**Nível:** Médio

**Uso:** Simulado

**Referência:** [15. IPv6 — Blocos especiais importantes](semana_02_estudo.md#s2-d2-ipv6).

Uma estação com máscara `/31` deve ser interpretada como:

A) LAN comum de zero hosts.
B) rota padrão.
C) caso especial, normalmente aplicável a enlace ponto a ponto, sem subtrair dois mecanicamente.
D) máscara inválida em qualquer cenário.

### S2S010 — PDU de enlace

**Nível:** Médio

**Uso:** Simulado

**Referência:** [9. Exemplos de IPv4 e CIDR — /31 ponto a ponto](semana_02_estudo.md#s2-d2-calculos).

Ao encapsular dados de aplicação em TCP/IP, a PDU na camada de enlace é normalmente denominada:

A) segmento, sempre.
B) quadro.
C) pacote, sempre.
D) socket.

## Bloco 2 — Protocolos, serviços e segurança

### S2S011 — Fluxo de serviços

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

Um cliente recebe endereço, máscara, gateway e DNS; resolve um nome; acessa portal HTTPS. A sequência funcional mais adequada é:

A) DHCP, DNS, transporte, TLS e HTTP.
B) DNS, DHCP, SMTP, TLS.
C) ARP, LDAP, FTP e HTTP.
D) NTP, ICMP, SFTP e TLS.

### S2S012 — HTTP/3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

Sobre HTTP/3, assinale a correta.

A) elimina TLS.
B) é SMTP sobre TCP/25.
C) torna DNS desnecessário.
D) usa normalmente QUIC sobre UDP/443.

### S2S013 — Correio

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

Em uma política de correio, SMTP, IMAP e POP3 se relacionam, respectivamente, a:

A) envio, acesso/sincronização e recuperação de mensagens.
B) criptografia, roteamento e NAT.
C) configuração IP, nomes e tempo.
D) autenticação, autorização e auditoria.

### S2S014 — Transferência segura

**Nível:** Médio

**Uso:** Simulado

**Referência:** [7.4 SSH](semana_02_estudo.md#s2-d3-transferencia-remota).

SFTP e FTPS diferem porque:

A) ambos são necessariamente o mesmo protocolo.
B) FTPS é terminal remoto e SFTP é correio.
C) nenhum oferece proteção de canal.
D) SFTP transfere arquivos sobre SSH; FTPS é FTP protegido por TLS.

### S2S015 — Portas

**Nível:** Médio

**Uso:** Simulado

**Referência:** [5. DHCP — atribuição dinâmica de configuração](semana_02_estudo.md#s2-d3-dhcp).

Uma porta TCP/UDP conhecida:

A) prova conteúdo seguro independentemente do endpoint.
B) é convenção de serviço, não prova isolada do protocolo efetivo ou da segurança.
C) identifica unicamente um usuário.
D) substitui certificado digital.

### S2S016 — SNMP

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

Em SNMP, manager, agent, MIB e OID correspondem a:

A) cliente, servidor web, banco e usuário.
B) camadas OSI.
C) elementos de gerenciamento e identificação de objetos monitorados.
D) etapas de DHCP.

### S2S017 — PAT

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

PAT permite que vários fluxos internos compartilhem endereço público principalmente por:

A) substituição de DNS por ARP.
B) tradução adicional de portas.
C) criação de certificados.
D) eliminação de roteamento.

### S2S018 — TLS

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

Um certificado TLS válido demonstra, em condições normais, que:

A) a identidade associada à chave foi validada conforme a cadeia e o canal pode ser autenticado/protegido.
B) o endpoint está livre de malware.
C) o conteúdo da aplicação é verdadeiro.
D) o usuário recebeu autorização para qualquer recurso.

### S2S019 — Spoofing

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).

Qual associação entre ataque e efeito está correta?

A) sniffing: necessariamente altera dados.
B) DDoS: garante confidencialidade.
C) phishing: atualiza sistemas.
D) spoofing: falsifica identidade ou origem.

### S2S020 — Defesa em profundidade

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

Em defesa em profundidade, a afirmação correta é:

A) MFA torna atualização de sistemas dispensável.
B) VPN elimina necessidade de controle de acesso do endpoint.
C) segmentação, autenticação, atualização e monitoramento reduzem dependência de barreira única.
D) firewall substitui backup.

## Bloco 3 — Criptografia, controles e continuidade

### S2S021 — Hash, HMAC e assinatura

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

Assinale a alternativa correta sobre hash, HMAC e assinatura digital.

A) hash cifra reversivelmente; HMAC dispensa segredo.
B) assinatura serve apenas para ocultar conteúdo.
C) HMAC usa chave secreta; assinatura é produzida com chave privada e verificada com a pública.
D) hash substitui certificado.

### S2S022 — DMZ

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

Uma DMZ é empregada para:

A) colocar servidor público em mesma rede de bancos internos.
B) isolar serviços expostos e controlar fluxos para redes internas.
C) eliminar necessidade de firewall.
D) dispensar atualização de servidores.

### S2S023 — IDS e IPS

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

IDS e IPS diferem porque:

A) IDS detecta/alerta, enquanto IPS pode atuar em linha para bloquear.
B) IDS sempre bloqueia e IPS só registra.
C) ambos são backups.
D) ambos substituem VPN.

### S2S024 — WPA3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

WPA3-Personal melhora autenticação de acesso sem fio ao usar:

A) WEP.
B) broadcast para autenticar.
C) apenas endereço MAC.
D) SAE, sem dispensar senha forte e configuração segura.

### S2S025 — Resposta a ransomware

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

Em incidente de ransomware, restaurar imediatamente antes de conter persistência é inadequado porque:

A) a ameaça pode permanecer ativa e comprometer a recuperação.
B) backup nunca deve ser usado.
C) RPO elimina necessidade de investigação.
D) logs não são evidência.

### S2S026 — RPO e RTO

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

RPO de 15 minutos e RTO de 4 horas significam, respectivamente:

A) prazo de restabelecimento e frequência obrigatória de backup.
B) disponibilidade e confidencialidade.
C) tamanho do backup e tempo de retenção.
D) perda máxima tolerável de dados e prazo desejado de restabelecimento.

### S2S027 — RAID e backup

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

RAID não substitui backup versionado porque:

A) RAID sempre fica offline.
B) replicação pode propagar exclusão, corrupção ou cifração maliciosa.
C) backup não possui cópias.
D) RAID não melhora disponibilidade.

### S2S028 — Assinatura digital

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

Uma assinatura digital fornece principalmente:

A) compressão de dados.
B) anonimato obrigatório.
C) integridade e vínculo verificável com o signatário, conforme o contexto criptográfico.
D) roteamento seguro.

### S2S029 — Gestão de risco

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-07).

Segurança da informação como gestão de risco exige:

A) comprar um produto e encerrar revisões.
B) identificar contexto, ativos, ameaças, vulnerabilidades, impacto, tratamento e monitoramento.
C) eliminar todas as ameaças existentes.
D) focar somente em software.

### S2S030 — MFA

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing).

Autenticação multifator combina fatores de naturezas distintas para:

A) provar identidade com evidências independentes, não apenas repetir senha.
B) substituir autorização.
C) eliminar logs.
D) tornar phishing impossível.

## Bloco 4 — Sistemas operacionais avançados

### S2S031 — Condição de corrida

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

Uma condição de corrida depende de:

A) existência obrigatória de rede.
B) uso de memória somente leitura.
C) término de todas as threads.
D) ordem de intercalação sobre estado compartilhado sem sincronização adequada.

### S2S032 — Coffman

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Deadlock — condições necessárias de Coffman](semana_02_estudo.md#s2-d5-deadlock).

O conjunto clássico de condições de Coffman inclui:

A) broadcast, NAT, DNS e DHCP.
B) autenticação, autorização, auditoria e não repúdio.
C) exclusão mútua, posse e espera, não preempção e espera circular.
D) paginação, segmentação, cache e DMA.

### S2S033 — Starvation

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

Starvation ocorre quando:

A) participantes esperam circularmente sem progresso conjunto.
B) todas as threads terminam.
C) uma tarefa pode ser adiada indefinidamente enquanto outras avançam.
D) o sistema de arquivos perde consistência.

### S2S034 — Livelock

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).

Livelock difere de deadlock porque no livelock:

A) recursos são sempre liberados.
B) participantes podem mudar de estado repetidamente, mas sem progresso útil.
C) não há execução alguma.
D) a CPU está desligada.

### S2S035 — Métricas de escalonamento

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-01).

Em escalonamento, tempo de resposta mede:

A) intervalo até a primeira resposta perceptível ao usuário.
B) somente o tempo total de CPU.
C) espaço ocupado no disco.
D) perda de dados tolerável.

### S2S036 — Semáforo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).

Um semáforo contador é adequado para:

A) substituir todas as permissões de arquivo.
B) garantir ausência de deadlock em qualquer desenho.
C) armazenar dados de aplicação.
D) representar quantidade de unidades equivalentes disponíveis.

### S2S037 — DMA

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

DMA é preferível a cópia controlada por CPU, principalmente, quando:

A) há transferência de blocos e se deseja reduzir intervenção por unidade.
B) é necessário calcular CIDR.
C) o dispositivo não possui driver.
D) se quer substituir interrupções em todo caso.

### S2S038 — DACL

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

Uma DACL do Windows contém:

A) somente endereços IP.
B) registros DNS.
C) páginas de memória.
D) ACEs de permissão ou negação, possivelmente herdadas.

### S2S039 — Permissões Linux

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

Em Linux, ao avaliar `rwx` para dono, grupo e outros, é incorreto:

A) verificar identidade e grupo efetivos.
B) somar permissões entre tríades como se fossem um único direito universal.
C) separar leitura, escrita e execução.
D) considerar ACL quando aplicável.

### S2S040 — Diagnóstico em camadas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

Uma aplicação responde a ping, mas não atende na porta esperada. A análise deve:

A) concluir saúde total do serviço.
B) ignorar logs.
C) separar conectividade IP de transporte, processo, firewall e aplicação.
D) restaurar backup sem diagnóstico.

## Bloco 5 — Estudo de caso integrado

### S2S041 — Resposta a incidente

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).

Um portal recebe DDoS, apresenta credenciais reutilizadas e banco acessível indevidamente. A ordem mais defensável é:

A) publicar senhas para acelerar análise.
B) conter impacto, preservar evidências, bloquear vetores, erradicar persistência e recuperar.
C) restaurar sem revogar acessos.
D) ignorar logs por serem volumosos.

### S2S042 — Segmentação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).

Para limitar movimento lateral após comprometimento de estação, é mais diretamente útil:

A) segmentação de rede e controles de acesso.
B) aumentar tamanho de cache.
C) trocar IPv4 por IPv6 sem política.
D) remover todos os logs.

### S2S043 — DNS e TLS

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

Uma consulta DNS funciona, mas HTTPS falha por certificado expirado. Isso demonstra que:

A) DNS garante certificado válido.
B) HTTPS dispensa transporte.
C) certificado substitui resolução de nomes.
D) DNS e validação TLS resolvem camadas/problemas distintos.

### S2S044 — VPN e autorização

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).

Em acesso remoto, VPN estabelecida não autoriza usuário a qualquer recurso porque:

A) VPN elimina identidade.
B) VPN só funciona em LAN.
C) túnel protegido e autorização são controles distintos.
D) autorização é responsabilidade do DNS.

### S2S045 — NTP e logs

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

Logs de firewall, aplicação e sistema só permitem correlação confiável se:

A) todos usarem POP3.
B) forem descartados após incidente.
C) relógios possuírem referência de tempo coerente, como NTP bem configurado.
D) houver apenas um host.

### S2S046 — Validação de recuperação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).

Uma restauração atende RPO, mas falha em validar integrações do negócio. A conclusão é:

A) continuidade está integralmente validada.
B) recuperar dados não basta; é preciso testar dependências e serviço.
C) RTO não importa.
D) backup é redundância.

### S2S047 — NAT e PAT

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

No fluxo de requisição, NAT/PAT pode:

A) traduzir endereço e, com PAT, porta, sem substituir a aplicação HTTP.
B) resolver nome DNS.
C) gerar assinatura digital.
D) escalonar threads.

### S2S048 — Integridade

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

O princípio CIA mais diretamente afetado por alteração não autorizada de cadastro é:

A) disponibilidade.
B) confidencialidade somente.
C) não repúdio exclusivamente.
D) integridade.

### S2S049 — Senhas

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas).

Uma senha armazenada corretamente deve, em regra, ser:

A) guardada por função de derivação/hash apropriada com sal, não reversível como cifra comum.
B) cifrada com chave pública do usuário e exibida em log.
C) compartilhada entre contas administrativas.
D) substituída por endereço MAC.

### S2S050 — Controles complementares

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [8. Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles), [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips) e [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).

Em autenticação de serviço web, certificado válido e MFA não eliminam:

A) necessidade de DNS.
B) todo uso de logs.
C) necessidade de rede.
D) necessidade de autorização e de correção de vulnerabilidades da aplicação.

## Bloco 6 — Revisão de alta dificuldade

### S2S051 — LDAP, SNMP e NTP

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

Assinale a combinação correta: protocolo para diretório, para gerência e para sincronização de tempo.

A) SMTP, DNS e DHCP.
B) LDAP, SNMP e NTP.
C) SFTP, ARP e ICMP.
D) HTTP, PAT e TLS.

### S2S052 — Comandos de observação

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).

O uso de `Get-Process`, ao contrário de `Stop-Process`, caracteriza:

A) exclusão de arquivo.
B) alteração de DACL.
C) observação de processos, não alteração de estado.
D) restauração de backup.

### S2S053 — Rotas específicas

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

Em roteamento, a rota mais específica normalmente:

A) é ignorada se existir gateway.
B) prevalece sobre rota padrão para destino correspondente.
C) só existe em IPv6.
D) substitui ARP local.

### S2S054 — UDP

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).

Se a aplicação usa UDP, é correto afirmar que:

A) não há garantias nativas de ordenação/retransmissão, mas a aplicação pode criar mecanismos próprios.
B) não pode obter confiabilidade adicional.
C) todo datagrama chega duplicado.
D) TCP passa a ser obrigatório.

### S2S055 — Criptografia

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia) e [17. TLS](semana_02_estudo.md#s2-d4-tls).

Qual técnica oferece confidencialidade reversível por chave?

A) hash.
B) checksum sem chave.
C) assinatura isolada.
D) criptografia.

### S2S056 — Erradicação

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

Em um incidente, erradicação significa:

A) somente detectar alerta.
B) apagar todas as evidências.
C) eliminar causa/persistência maliciosa após contenção, antes da recuperação controlada.
D) aplicar RPO.

### S2S057 — Autorização

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).

Uma ACL permissiva demais em servidor de arquivos é principalmente problema de:

A) latência.
B) CIDR.
C) autorização.
D) NTP.

### S2S058 — MAC no enlace

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [6. Placa de rede](semana_02_estudo.md#s2-d1-nic).

Na análise de tráfego, endereço MAC é relevante principalmente:

A) para resolver nomes globalmente.
B) no enlace local, não como identificador fim a fim roteável.
C) para cifrar HTTP.
D) para autenticar pessoa usuária.

### S2S059 — Proxy reverso

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).

Um proxy reverso diante de vários servidores de aplicação pode contribuir para:

A) publicação controlada e distribuição de requisições, conforme configuração.
B) substituir banco de dados.
C) eliminar TLS.
D) criar endereços IP por DHCP.

### S2S060 — Caderno de erros

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).

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

### Comentário S2S001

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. A envia quadro ao MAC do gateway; cada roteador remove e recria o quadro do próximo enlace. A proposição aplica o ponto decisivo de encapsulamento roteado..
- **B)** Incorreta. A opção sustenta que A resolve por ARP o MAC do servidor remoto e o quadro atravessa todos os roteadores intacto; no caso, a regra decisiva é: A envia quadro ao MAC do gateway; cada roteador remove e recria o quadro do próximo enlace.
- **C)** Incorreta. A opção sustenta que A envia pacote IP diretamente ao switch, sem quadro de enlace; no caso, a regra decisiva é: A envia quadro ao MAC do gateway; cada roteador remove e recria o quadro do próximo enlace.
- **D)** Incorreta. A opção sustenta que A usa DNS para descobrir o MAC do gateway; no caso, a regra decisiva é: A envia quadro ao MAC do gateway; cada roteador remove e recria o quadro do próximo enlace.

**Conceito:** encapsulamento roteado.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-02).
### Comentário S2S002

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que rede `172.16.34.192`, broadcast `172.16.34.223`, hosts de 193 a 222; no caso, a regra decisiva é: rede `172.16.34.160`, broadcast `172.16.34.191`, hosts de 161 a 190.
- **B)** Incorreta. A opção sustenta que rede `172.16.34.160`, broadcast `172.16.34.192`, hosts de 161 a 191; no caso, a regra decisiva é: rede `172.16.34.160`, broadcast `172.16.34.191`, hosts de 161 a 190.
- **C)** Incorreta. A opção sustenta que rede `172.16.34.0`, broadcast `172.16.34.255`, 254 hosts; no caso, a regra decisiva é: rede `172.16.34.160`, broadcast `172.16.34.191`, hosts de 161 a 190.
- **D)** Correta. rede `172.16.34.160`, broadcast `172.16.34.191`, hosts de 161 a 190. A proposição aplica o ponto decisivo de CIDR..

**Conceito:** CIDR.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-03).
### Comentário S2S003

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que I e II, apenas; no caso, a regra decisiva é: I, II e III.
- **B)** Correta. I, II e III. A proposição aplica o ponto decisivo de equipamentos..
- **C)** Incorreta. A opção sustenta que I e III, apenas; no caso, a regra decisiva é: I, II e III.
- **D)** Incorreta. A opção sustenta que II e III, apenas; no caso, a regra decisiva é: I, II e III.

**Conceito:** equipamentos.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).
### Comentário S2S004

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que usa broadcast ARP idêntico ao IPv4; no caso, a regra decisiva é: usa ICMPv6/Neighbor Discovery e não emprega broadcast IPv6.
- **B)** Incorreta. A opção sustenta que depende obrigatoriamente de DHCPv4; no caso, a regra decisiva é: usa ICMPv6/Neighbor Discovery e não emprega broadcast IPv6.
- **C)** Correta. usa ICMPv6/Neighbor Discovery e não emprega broadcast IPv6. A proposição aplica o ponto decisivo de IPv6 e ND..
- **D)** Incorreta. A opção sustenta que substitui roteamento por DNS; no caso, a regra decisiva é: usa ICMPv6/Neighbor Discovery e não emprega broadcast IPv6.

**Conceito:** IPv6 e ND.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-04).
### Comentário S2S005

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que goodput inclui mais overhead que throughput; no caso, a regra decisiva é: a variação de atraso é jitter, e goodput mede dados úteis entregues.
- **B)** Correta. a variação de atraso é jitter, e goodput mede dados úteis entregues. A proposição aplica o ponto decisivo de métricas..
- **C)** Incorreta. A opção sustenta que 1 Gbit/s é a latência máxima; no caso, a regra decisiva é: a variação de atraso é jitter, e goodput mede dados úteis entregues.
- **D)** Incorreta. A opção sustenta que jitter é sinônimo de perda de pacote; no caso, a regra decisiva é: a variação de atraso é jitter, e goodput mede dados úteis entregues.

**Conceito:** métricas.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-01).
### Comentário S2S006

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. OSI seja referência conceitual e TCP/IP uma arquitetura/suíte, com correspondência aproximada. A proposição aplica o ponto decisivo de OSI e TCP/IP..
- **B)** Incorreta. A opção sustenta que cada camada OSI tenha exatamente uma camada TCP/IP correspondente; no caso, a regra decisiva é: OSI seja referência conceitual e TCP/IP uma arquitetura/suíte, com correspondência aproximada.
- **C)** Incorreta. A opção sustenta que ambos sejam protocolos de roteamento; no caso, a regra decisiva é: OSI seja referência conceitual e TCP/IP uma arquitetura/suíte, com correspondência aproximada.
- **D)** Incorreta. A opção sustenta que TCP/IP não possua camada de aplicação; no caso, a regra decisiva é: OSI seja referência conceitual e TCP/IP uma arquitetura/suíte, com correspondência aproximada.

**Conceito:** OSI e TCP/IP.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [2. Modelo TCP/IP](semana_02_estudo.md#s2-d2-tcpip).
### Comentário S2S007

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que rede local com dois hosts; no caso, a regra decisiva é: rota padrão aplicável quando não há rota mais específica.
- **B)** Incorreta. A opção sustenta que endereço de loopback; no caso, a regra decisiva é: rota padrão aplicável quando não há rota mais específica.
- **C)** Incorreta. A opção sustenta que broadcast limitado; no caso, a regra decisiva é: rota padrão aplicável quando não há rota mais específica.
- **D)** Correta. rota padrão aplicável quando não há rota mais específica. A proposição aplica o ponto decisivo de rota padrão..

**Conceito:** rota padrão.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).
### Comentário S2S008

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que cada estação constitui domínio de colisão independente; no caso, a regra decisiva é: a topologia lógica pode compartilhar meio e colisões, apesar da estrela física.
- **B)** Incorreta. A opção sustenta que o hub aprende MAC e filtra tráfego; no caso, a regra decisiva é: a topologia lógica pode compartilhar meio e colisões, apesar da estrela física.
- **C)** Correta. a topologia lógica pode compartilhar meio e colisões, apesar da estrela física. A proposição aplica o ponto decisivo de topologia física e lógica..
- **D)** Incorreta. A opção sustenta que o hub roteia entre VLANs; no caso, a regra decisiva é: a topologia lógica pode compartilhar meio e colisões, apesar da estrela física.

**Conceito:** topologia física e lógica.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [3. Topologia física e topologia lógica](semana_02_estudo.md#s2-d1-topologias).
### Comentário S2S009

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que LAN comum de zero hosts; no caso, a regra decisiva é: caso especial, normalmente aplicável a enlace ponto a ponto, sem subtrair dois mecanicamente.
- **B)** Incorreta. A opção sustenta que rota padrão; no caso, a regra decisiva é: caso especial, normalmente aplicável a enlace ponto a ponto, sem subtrair dois mecanicamente.
- **C)** Correta. caso especial, normalmente aplicável a enlace ponto a ponto, sem subtrair dois mecanicamente. A proposição aplica o ponto decisivo de prefixos especiais..
- **D)** Incorreta. A opção sustenta que máscara inválida em qualquer cenário; no caso, a regra decisiva é: caso especial, normalmente aplicável a enlace ponto a ponto, sem subtrair dois mecanicamente.

**Conceito:** prefixos especiais.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [15. IPv6 — Blocos especiais importantes](semana_02_estudo.md#s2-d2-ipv6).
### Comentário S2S010

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que segmento, sempre; no caso, a regra decisiva é: quadro.
- **B)** Correta. quadro. A proposição aplica o ponto decisivo de PDU de enlace..
- **C)** Incorreta. A opção sustenta que pacote, sempre; no caso, a regra decisiva é: quadro.
- **D)** Incorreta. A opção sustenta que socket; no caso, a regra decisiva é: quadro.

**Conceito:** PDU de enlace.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [9. Exemplos de IPv4 e CIDR — /31 ponto a ponto](semana_02_estudo.md#s2-d2-calculos).
### Comentário S2S011

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. DHCP, DNS, transporte, TLS e HTTP. A proposição aplica o ponto decisivo de fluxo de serviços..
- **B)** Incorreta. A opção sustenta que DNS, DHCP, SMTP, TLS; no caso, a regra decisiva é: DHCP, DNS, transporte, TLS e HTTP.
- **C)** Incorreta. A opção sustenta que ARP, LDAP, FTP e HTTP; no caso, a regra decisiva é: DHCP, DNS, transporte, TLS e HTTP.
- **D)** Incorreta. A opção sustenta que NTP, ICMP, SFTP e TLS; no caso, a regra decisiva é: DHCP, DNS, transporte, TLS e HTTP.

**Conceito:** fluxo de serviços.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).
### Comentário S2S012

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que elimina TLS; no caso, a regra decisiva é: usa normalmente QUIC sobre UDP/443.
- **B)** Incorreta. A opção sustenta que é SMTP sobre TCP/25; no caso, a regra decisiva é: usa normalmente QUIC sobre UDP/443.
- **C)** Incorreta. A opção sustenta que torna DNS desnecessário; no caso, a regra decisiva é: usa normalmente QUIC sobre UDP/443.
- **D)** Correta. usa normalmente QUIC sobre UDP/443. A proposição aplica o ponto decisivo de HTTP/3..

**Conceito:** HTTP/3.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).
### Comentário S2S013

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. envio, acesso/sincronização e recuperação de mensagens. A proposição aplica o ponto decisivo de correio..
- **B)** Incorreta. A opção sustenta que criptografia, roteamento e NAT; no caso, a regra decisiva é: envio, acesso/sincronização e recuperação de mensagens.
- **C)** Incorreta. A opção sustenta que configuração IP, nomes e tempo; no caso, a regra decisiva é: envio, acesso/sincronização e recuperação de mensagens.
- **D)** Incorreta. A opção sustenta que autenticação, autorização e auditoria; no caso, a regra decisiva é: envio, acesso/sincronização e recuperação de mensagens.

**Conceito:** correio.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).
### Comentário S2S014

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que ambos são necessariamente o mesmo protocolo; no caso, a regra decisiva é: SFTP transfere arquivos sobre SSH; FTPS é FTP protegido por TLS.
- **B)** Incorreta. A opção sustenta que FTPS é terminal remoto e SFTP é correio; no caso, a regra decisiva é: SFTP transfere arquivos sobre SSH; FTPS é FTP protegido por TLS.
- **C)** Incorreta. A opção sustenta que nenhum oferece proteção de canal; no caso, a regra decisiva é: SFTP transfere arquivos sobre SSH; FTPS é FTP protegido por TLS.
- **D)** Correta. SFTP transfere arquivos sobre SSH; FTPS é FTP protegido por TLS. A proposição aplica o ponto decisivo de transferência segura..

**Conceito:** transferência segura.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [7.4 SSH](semana_02_estudo.md#s2-d3-transferencia-remota).
### Comentário S2S015

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que prova conteúdo seguro independentemente do endpoint; no caso, a regra decisiva é: é convenção de serviço, não prova isolada do protocolo efetivo ou da segurança.
- **B)** Correta. é convenção de serviço, não prova isolada do protocolo efetivo ou da segurança. A proposição aplica o ponto decisivo de portas..
- **C)** Incorreta. A opção sustenta que identifica unicamente um usuário; no caso, a regra decisiva é: é convenção de serviço, não prova isolada do protocolo efetivo ou da segurança.
- **D)** Incorreta. A opção sustenta que substitui certificado digital; no caso, a regra decisiva é: é convenção de serviço, não prova isolada do protocolo efetivo ou da segurança.

**Conceito:** portas.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [5. DHCP — atribuição dinâmica de configuração](semana_02_estudo.md#s2-d3-dhcp).
### Comentário S2S016

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que cliente, servidor web, banco e usuário; no caso, a regra decisiva é: elementos de gerenciamento e identificação de objetos monitorados.
- **B)** Incorreta. A opção sustenta que camadas OSI; no caso, a regra decisiva é: elementos de gerenciamento e identificação de objetos monitorados.
- **C)** Correta. elementos de gerenciamento e identificação de objetos monitorados. A proposição aplica o ponto decisivo de SNMP..
- **D)** Incorreta. A opção sustenta que etapas de DHCP; no caso, a regra decisiva é: elementos de gerenciamento e identificação de objetos monitorados.

**Conceito:** SNMP.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).
### Comentário S2S017

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que substituição de DNS por ARP; no caso, a regra decisiva é: tradução adicional de portas.
- **B)** Correta. tradução adicional de portas. A proposição aplica o ponto decisivo de PAT..
- **C)** Incorreta. A opção sustenta que criação de certificados; no caso, a regra decisiva é: tradução adicional de portas.
- **D)** Incorreta. A opção sustenta que eliminação de roteamento; no caso, a regra decisiva é: tradução adicional de portas.

**Conceito:** PAT.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).
### Comentário S2S018

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. a identidade associada à chave foi validada conforme a cadeia e o canal pode ser autenticado/protegido. A proposição aplica o ponto decisivo de TLS..
- **B)** Incorreta. A opção sustenta que o endpoint está livre de malware; no caso, a regra decisiva é: a identidade associada à chave foi validada conforme a cadeia e o canal pode ser autenticado/protegido.
- **C)** Incorreta. A opção sustenta que o conteúdo da aplicação é verdadeiro; no caso, a regra decisiva é: a identidade associada à chave foi validada conforme a cadeia e o canal pode ser autenticado/protegido.
- **D)** Incorreta. A opção sustenta que o usuário recebeu autorização para qualquer recurso; no caso, a regra decisiva é: a identidade associada à chave foi validada conforme a cadeia e o canal pode ser autenticado/protegido.

**Conceito:** TLS.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S019

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que sniffing: necessariamente altera dados; no caso, a regra decisiva é: spoofing: falsifica identidade ou origem.
- **B)** Incorreta. A opção sustenta que DDoS: garante confidencialidade; no caso, a regra decisiva é: spoofing: falsifica identidade ou origem.
- **C)** Incorreta. A opção sustenta que phishing: atualiza sistemas; no caso, a regra decisiva é: spoofing: falsifica identidade ou origem.
- **D)** Correta. spoofing: falsifica identidade ou origem. A proposição aplica o ponto decisivo de spoofing..

**Conceito:** spoofing.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Ataques de rede](semana_02_estudo.md#s2-d4-ataques-rede).
### Comentário S2S020

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que MFA torna atualização de sistemas dispensável; no caso, a regra decisiva é: segmentação, autenticação, atualização e monitoramento reduzem dependência de barreira única.
- **B)** Incorreta. A opção sustenta que VPN elimina necessidade de controle de acesso do endpoint; no caso, a regra decisiva é: segmentação, autenticação, atualização e monitoramento reduzem dependência de barreira única.
- **C)** Correta. segmentação, autenticação, atualização e monitoramento reduzem dependência de barreira única. A proposição aplica o ponto decisivo de defesa em profundidade..
- **D)** Incorreta. A opção sustenta que firewall substitui backup; no caso, a regra decisiva é: segmentação, autenticação, atualização e monitoramento reduzem dependência de barreira única.

**Conceito:** defesa em profundidade.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S021

**Alternativa correta: C.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que hash cifra reversivelmente; HMAC dispensa segredo; no caso, a regra decisiva é: HMAC usa chave secreta; assinatura é produzida com chave privada e verificada com a pública.
- **B)** Incorreta. A opção sustenta que assinatura serve apenas para ocultar conteúdo; no caso, a regra decisiva é: HMAC usa chave secreta; assinatura é produzida com chave privada e verificada com a pública.
- **C)** Correta. HMAC usa chave secreta; assinatura é produzida com chave privada e verificada com a pública. A proposição aplica o ponto decisivo de hash, HMAC e assinatura..
- **D)** Incorreta. A opção sustenta que hash substitui certificado; no caso, a regra decisiva é: HMAC usa chave secreta; assinatura é produzida com chave privada e verificada com a pública.

**Conceito:** hash, HMAC e assinatura.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S022

**Alternativa correta: B.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que colocar servidor público em mesma rede de bancos internos; no caso, a regra decisiva é: isolar serviços expostos e controlar fluxos para redes internas.
- **B)** Correta. isolar serviços expostos e controlar fluxos para redes internas. A proposição aplica o ponto decisivo de DMZ..
- **C)** Incorreta. A opção sustenta que eliminar necessidade de firewall; no caso, a regra decisiva é: isolar serviços expostos e controlar fluxos para redes internas.
- **D)** Incorreta. A opção sustenta que dispensar atualização de servidores; no caso, a regra decisiva é: isolar serviços expostos e controlar fluxos para redes internas.

**Conceito:** DMZ.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S023

**Alternativa correta: A.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. IDS detecta/alerta, enquanto IPS pode atuar em linha para bloquear. A proposição aplica o ponto decisivo de IDS e IPS..
- **B)** Incorreta. A opção sustenta que IDS sempre bloqueia e IPS só registra; no caso, a regra decisiva é: IDS detecta/alerta, enquanto IPS pode atuar em linha para bloquear.
- **C)** Incorreta. A opção sustenta que ambos são backups; no caso, a regra decisiva é: IDS detecta/alerta, enquanto IPS pode atuar em linha para bloquear.
- **D)** Incorreta. A opção sustenta que ambos substituem VPN; no caso, a regra decisiva é: IDS detecta/alerta, enquanto IPS pode atuar em linha para bloquear.

**Conceito:** IDS e IPS.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S024

**Alternativa correta: D.**

**Nível:** Médio

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que WEP; no caso, a regra decisiva é: SAE, sem dispensar senha forte e configuração segura.
- **B)** Incorreta. A opção sustenta que broadcast para autenticar; no caso, a regra decisiva é: SAE, sem dispensar senha forte e configuração segura.
- **C)** Incorreta. A opção sustenta que apenas endereço MAC; no caso, a regra decisiva é: SAE, sem dispensar senha forte e configuração segura.
- **D)** Correta. SAE, sem dispensar senha forte e configuração segura. A proposição aplica o ponto decisivo de WPA3..

**Conceito:** WPA3.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S025

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. a ameaça pode permanecer ativa e comprometer a recuperação. A proposição aplica o ponto decisivo de resposta a ransomware..
- **B)** Incorreta. A opção sustenta que backup nunca deve ser usado; no caso, a regra decisiva é: a ameaça pode permanecer ativa e comprometer a recuperação.
- **C)** Incorreta. A opção sustenta que RPO elimina necessidade de investigação; no caso, a regra decisiva é: a ameaça pode permanecer ativa e comprometer a recuperação.
- **D)** Incorreta. A opção sustenta que logs não são evidência; no caso, a regra decisiva é: a ameaça pode permanecer ativa e comprometer a recuperação.

**Conceito:** resposta a ransomware.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).
### Comentário S2S026

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que prazo de restabelecimento e frequência obrigatória de backup; no caso, a regra decisiva é: perda máxima tolerável de dados e prazo desejado de restabelecimento.
- **B)** Incorreta. A opção sustenta que disponibilidade e confidencialidade; no caso, a regra decisiva é: perda máxima tolerável de dados e prazo desejado de restabelecimento.
- **C)** Incorreta. A opção sustenta que tamanho do backup e tempo de retenção; no caso, a regra decisiva é: perda máxima tolerável de dados e prazo desejado de restabelecimento.
- **D)** Correta. perda máxima tolerável de dados e prazo desejado de restabelecimento. A proposição aplica o ponto decisivo de RPO e RTO..

**Conceito:** RPO e RTO.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).
### Comentário S2S027

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que RAID sempre fica offline; no caso, a regra decisiva é: replicação pode propagar exclusão, corrupção ou cifração maliciosa.
- **B)** Correta. replicação pode propagar exclusão, corrupção ou cifração maliciosa. A proposição aplica o ponto decisivo de RAID e backup..
- **C)** Incorreta. A opção sustenta que backup não possui cópias; no caso, a regra decisiva é: replicação pode propagar exclusão, corrupção ou cifração maliciosa.
- **D)** Incorreta. A opção sustenta que RAID não melhora disponibilidade; no caso, a regra decisiva é: replicação pode propagar exclusão, corrupção ou cifração maliciosa.

**Conceito:** RAID e backup.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).
### Comentário S2S028

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que compressão de dados; no caso, a regra decisiva é: integridade e vínculo verificável com o signatário, conforme o contexto criptográfico.
- **B)** Incorreta. A opção sustenta que anonimato obrigatório; no caso, a regra decisiva é: integridade e vínculo verificável com o signatário, conforme o contexto criptográfico.
- **C)** Correta. integridade e vínculo verificável com o signatário, conforme o contexto criptográfico. A proposição aplica o ponto decisivo de assinatura digital..
- **D)** Incorreta. A opção sustenta que roteamento seguro; no caso, a regra decisiva é: integridade e vínculo verificável com o signatário, conforme o contexto criptográfico.

**Conceito:** assinatura digital.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S029

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que comprar um produto e encerrar revisões; no caso, a regra decisiva é: identificar contexto, ativos, ameaças, vulnerabilidades, impacto, tratamento e monitoramento.
- **B)** Correta. identificar contexto, ativos, ameaças, vulnerabilidades, impacto, tratamento e monitoramento. A proposição aplica o ponto decisivo de gestão de risco..
- **C)** Incorreta. A opção sustenta que eliminar todas as ameaças existentes; no caso, a regra decisiva é: identificar contexto, ativos, ameaças, vulnerabilidades, impacto, tratamento e monitoramento.
- **D)** Incorreta. A opção sustenta que focar somente em software; no caso, a regra decisiva é: identificar contexto, ativos, ameaças, vulnerabilidades, impacto, tratamento e monitoramento.

**Conceito:** gestão de risco.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-07).
### Comentário S2S030

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. provar identidade com evidências independentes, não apenas repetir senha. A proposição aplica o ponto decisivo de MFA..
- **B)** Incorreta. A opção sustenta que substituir autorização; no caso, a regra decisiva é: provar identidade com evidências independentes, não apenas repetir senha.
- **C)** Incorreta. A opção sustenta que eliminar logs; no caso, a regra decisiva é: provar identidade com evidências independentes, não apenas repetir senha.
- **D)** Incorreta. A opção sustenta que tornar phishing impossível; no caso, a regra decisiva é: provar identidade com evidências independentes, não apenas repetir senha.

**Conceito:** MFA.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Phishing e engenharia social](semana_02_estudo.md#s2-d4-phishing).
### Comentário S2S031

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que existência obrigatória de rede; no caso, a regra decisiva é: ordem de intercalação sobre estado compartilhado sem sincronização adequada.
- **B)** Incorreta. A opção sustenta que uso de memória somente leitura; no caso, a regra decisiva é: ordem de intercalação sobre estado compartilhado sem sincronização adequada.
- **C)** Incorreta. A opção sustenta que término de todas as threads; no caso, a regra decisiva é: ordem de intercalação sobre estado compartilhado sem sincronização adequada.
- **D)** Correta. ordem de intercalação sobre estado compartilhado sem sincronização adequada. A proposição aplica o ponto decisivo de condição de corrida..

**Conceito:** condição de corrida.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2S032

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que broadcast, NAT, DNS e DHCP; no caso, a regra decisiva é: exclusão mútua, posse e espera, não preempção e espera circular.
- **B)** Incorreta. A opção sustenta que autenticação, autorização, auditoria e não repúdio; no caso, a regra decisiva é: exclusão mútua, posse e espera, não preempção e espera circular.
- **C)** Correta. exclusão mútua, posse e espera, não preempção e espera circular. A proposição aplica o ponto decisivo de Coffman..
- **D)** Incorreta. A opção sustenta que paginação, segmentação, cache e DMA; no caso, a regra decisiva é: exclusão mútua, posse e espera, não preempção e espera circular.

**Conceito:** Coffman.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Deadlock — condições necessárias de Coffman](semana_02_estudo.md#s2-d5-deadlock).
### Comentário S2S033

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que participantes esperam circularmente sem progresso conjunto; no caso, a regra decisiva é: uma tarefa pode ser adiada indefinidamente enquanto outras avançam.
- **B)** Incorreta. A opção sustenta que todas as threads terminam; no caso, a regra decisiva é: uma tarefa pode ser adiada indefinidamente enquanto outras avançam.
- **C)** Correta. uma tarefa pode ser adiada indefinidamente enquanto outras avançam. A proposição aplica o ponto decisivo de starvation..
- **D)** Incorreta. A opção sustenta que o sistema de arquivos perde consistência; no caso, a regra decisiva é: uma tarefa pode ser adiada indefinidamente enquanto outras avançam.

**Conceito:** starvation.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2S034

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que recursos são sempre liberados; no caso, a regra decisiva é: participantes podem mudar de estado repetidamente, mas sem progresso útil.
- **B)** Correta. participantes podem mudar de estado repetidamente, mas sem progresso útil. A proposição aplica o ponto decisivo de livelock..
- **C)** Incorreta. A opção sustenta que não há execução alguma; no caso, a regra decisiva é: participantes podem mudar de estado repetidamente, mas sem progresso útil.
- **D)** Incorreta. A opção sustenta que a CPU está desligada; no caso, a regra decisiva é: participantes podem mudar de estado repetidamente, mas sem progresso útil.

**Conceito:** livelock.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Starvation, livelock e inversão de prioridade](semana_02_estudo.md#s2-d5-starvation-livelock).
### Comentário S2S035

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. intervalo até a primeira resposta perceptível ao usuário. A proposição aplica o ponto decisivo de métricas de escalonamento..
- **B)** Incorreta. A opção sustenta que somente o tempo total de CPU; no caso, a regra decisiva é: intervalo até a primeira resposta perceptível ao usuário.
- **C)** Incorreta. A opção sustenta que espaço ocupado no disco; no caso, a regra decisiva é: intervalo até a primeira resposta perceptível ao usuário.
- **D)** Incorreta. A opção sustenta que perda de dados tolerável; no caso, a regra decisiva é: intervalo até a primeira resposta perceptível ao usuário.

**Conceito:** métricas de escalonamento.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-01).
### Comentário S2S036

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que substituir todas as permissões de arquivo; no caso, a regra decisiva é: representar quantidade de unidades equivalentes disponíveis.
- **B)** Incorreta. A opção sustenta que garantir ausência de deadlock em qualquer desenho; no caso, a regra decisiva é: representar quantidade de unidades equivalentes disponíveis.
- **C)** Incorreta. A opção sustenta que armazenar dados de aplicação; no caso, a regra decisiva é: representar quantidade de unidades equivalentes disponíveis.
- **D)** Correta. representar quantidade de unidades equivalentes disponíveis. A proposição aplica o ponto decisivo de semáforo..

**Conceito:** semáforo.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mutex, semáforos, monitores e variáveis de condição](semana_02_estudo.md#s2-d5-sincronizacao).
### Comentário S2S037

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. há transferência de blocos e se deseja reduzir intervenção por unidade. A proposição aplica o ponto decisivo de DMA..
- **B)** Incorreta. A opção sustenta que é necessário calcular CIDR; no caso, a regra decisiva é: há transferência de blocos e se deseja reduzir intervenção por unidade.
- **C)** Incorreta. A opção sustenta que o dispositivo não possui driver; no caso, a regra decisiva é: há transferência de blocos e se deseja reduzir intervenção por unidade.
- **D)** Incorreta. A opção sustenta que se quer substituir interrupções em todo caso; no caso, a regra decisiva é: há transferência de blocos e se deseja reduzir intervenção por unidade.

**Conceito:** DMA.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2S038

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que somente endereços IP; no caso, a regra decisiva é: ACEs de permissão ou negação, possivelmente herdadas.
- **B)** Incorreta. A opção sustenta que registros DNS; no caso, a regra decisiva é: ACEs de permissão ou negação, possivelmente herdadas.
- **C)** Incorreta. A opção sustenta que páginas de memória; no caso, a regra decisiva é: ACEs de permissão ou negação, possivelmente herdadas.
- **D)** Correta. ACEs de permissão ou negação, possivelmente herdadas. A proposição aplica o ponto decisivo de DACL..

**Conceito:** DACL.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2S039

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que verificar identidade e grupo efetivos; no caso, a regra decisiva é: somar permissões entre tríades como se fossem um único direito universal.
- **B)** Correta. somar permissões entre tríades como se fossem um único direito universal. A proposição aplica o ponto decisivo de permissões Linux..
- **C)** Incorreta. A opção sustenta que separar leitura, escrita e execução; no caso, a regra decisiva é: somar permissões entre tríades como se fossem um único direito universal.
- **D)** Incorreta. A opção sustenta que considerar ACL quando aplicável; no caso, a regra decisiva é: somar permissões entre tríades como se fossem um único direito universal.

**Conceito:** permissões Linux.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2S040

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que concluir saúde total do serviço; no caso, a regra decisiva é: separar conectividade IP de transporte, processo, firewall e aplicação.
- **B)** Incorreta. A opção sustenta que ignorar logs; no caso, a regra decisiva é: separar conectividade IP de transporte, processo, firewall e aplicação.
- **C)** Correta. separar conectividade IP de transporte, processo, firewall e aplicação. A proposição aplica o ponto decisivo de diagnóstico em camadas..
- **D)** Incorreta. A opção sustenta que restaurar backup sem diagnóstico; no caso, a regra decisiva é: separar conectividade IP de transporte, processo, firewall e aplicação.

**Conceito:** diagnóstico em camadas.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).
### Comentário S2S041

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que publicar senhas para acelerar análise; no caso, a regra decisiva é: conter impacto, preservar evidências, bloquear vetores, erradicar persistência e recuperar.
- **B)** Correta. conter impacto, preservar evidências, bloquear vetores, erradicar persistência e recuperar. A proposição aplica o ponto decisivo de resposta a incidente..
- **C)** Incorreta. A opção sustenta que restaurar sem revogar acessos; no caso, a regra decisiva é: conter impacto, preservar evidências, bloquear vetores, erradicar persistência e recuperar.
- **D)** Incorreta. A opção sustenta que ignorar logs por serem volumosos; no caso, a regra decisiva é: conter impacto, preservar evidências, bloquear vetores, erradicar persistência e recuperar.

**Conceito:** resposta a incidente.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [8. Escalonamento de CPU](semana_02_estudo.md#s2-d5-escalonamento).
### Comentário S2S042

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. segmentação de rede e controles de acesso. A proposição aplica o ponto decisivo de segmentação..
- **B)** Incorreta. A opção sustenta que aumentar tamanho de cache; no caso, a regra decisiva é: segmentação de rede e controles de acesso.
- **C)** Incorreta. A opção sustenta que trocar IPv4 por IPv6 sem política; no caso, a regra decisiva é: segmentação de rede e controles de acesso.
- **D)** Incorreta. A opção sustenta que remover todos os logs; no caso, a regra decisiva é: segmentação de rede e controles de acesso.

**Conceito:** segmentação.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [8. Bridges e switches — Switch](semana_02_estudo.md#s2-d1-bridge-switch).
### Comentário S2S043

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que DNS garante certificado válido; no caso, a regra decisiva é: DNS e validação TLS resolvem camadas/problemas distintos.
- **B)** Incorreta. A opção sustenta que HTTPS dispensa transporte; no caso, a regra decisiva é: DNS e validação TLS resolvem camadas/problemas distintos.
- **C)** Incorreta. A opção sustenta que certificado substitui resolução de nomes; no caso, a regra decisiva é: DNS e validação TLS resolvem camadas/problemas distintos.
- **D)** Correta. DNS e validação TLS resolvem camadas/problemas distintos. A proposição aplica o ponto decisivo de DNS e TLS..

**Conceito:** DNS e TLS.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S044

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que VPN elimina identidade; no caso, a regra decisiva é: túnel protegido e autorização são controles distintos.
- **B)** Incorreta. A opção sustenta que VPN só funciona em LAN; no caso, a regra decisiva é: túnel protegido e autorização são controles distintos.
- **C)** Correta. túnel protegido e autorização são controles distintos. A proposição aplica o ponto decisivo de VPN e autorização..
- **D)** Incorreta. A opção sustenta que autorização é responsabilidade do DNS; no caso, a regra decisiva é: túnel protegido e autorização são controles distintos.

**Conceito:** VPN e autorização.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-08).
### Comentário S2S045

**Alternativa correta: C.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que todos usarem POP3; no caso, a regra decisiva é: relógios possuírem referência de tempo coerente, como NTP bem configurado.
- **B)** Incorreta. A opção sustenta que forem descartados após incidente; no caso, a regra decisiva é: relógios possuírem referência de tempo coerente, como NTP bem configurado.
- **C)** Correta. relógios possuírem referência de tempo coerente, como NTP bem configurado. A proposição aplica o ponto decisivo de NTP e logs..
- **D)** Incorreta. A opção sustenta que houver apenas um host; no caso, a regra decisiva é: relógios possuírem referência de tempo coerente, como NTP bem configurado.

**Conceito:** NTP e logs.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).
### Comentário S2S046

**Alternativa correta: B.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que continuidade está integralmente validada; no caso, a regra decisiva é: recuperar dados não basta; é preciso testar dependências e serviço.
- **B)** Correta. recuperar dados não basta; é preciso testar dependências e serviço. A proposição aplica o ponto decisivo de validação de recuperação..
- **C)** Incorreta. A opção sustenta que RTO não importa; no caso, a regra decisiva é: recuperar dados não basta; é preciso testar dependências e serviço.
- **D)** Incorreta. A opção sustenta que backup é redundância; no caso, a regra decisiva é: recuperar dados não basta; é preciso testar dependências e serviço.

**Conceito:** validação de recuperação.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-09).
### Comentário S2S047

**Alternativa correta: A.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. traduzir endereço e, com PAT, porta, sem substituir a aplicação HTTP. A proposição aplica o ponto decisivo de NAT e PAT..
- **B)** Incorreta. A opção sustenta que resolver nome DNS; no caso, a regra decisiva é: traduzir endereço e, com PAT, porta, sem substituir a aplicação HTTP.
- **C)** Incorreta. A opção sustenta que gerar assinatura digital; no caso, a regra decisiva é: traduzir endereço e, com PAT, porta, sem substituir a aplicação HTTP.
- **D)** Incorreta. A opção sustenta que escalonar threads; no caso, a regra decisiva é: traduzir endereço e, com PAT, porta, sem substituir a aplicação HTTP.

**Conceito:** NAT e PAT.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).
### Comentário S2S048

**Alternativa correta: D.**

**Nível:** Difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que disponibilidade; no caso, a regra decisiva é: integridade.
- **B)** Incorreta. A opção sustenta que confidencialidade somente; no caso, a regra decisiva é: integridade.
- **C)** Incorreta. A opção sustenta que não repúdio exclusivamente; no caso, a regra decisiva é: integridade.
- **D)** Correta. integridade. A proposição aplica o ponto decisivo de integridade..

**Conceito:** integridade.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).
### Comentário S2S049

**Alternativa correta: A.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. guardada por função de derivação/hash apropriada com sal, não reversível como cifra comum. A proposição aplica o ponto decisivo de senhas..
- **B)** Incorreta. A opção sustenta que cifrada com chave pública do usuário e exibida em log; no caso, a regra decisiva é: guardada por função de derivação/hash apropriada com sal, não reversível como cifra comum.
- **C)** Incorreta. A opção sustenta que compartilhada entre contas administrativas; no caso, a regra decisiva é: guardada por função de derivação/hash apropriada com sal, não reversível como cifra comum.
- **D)** Incorreta. A opção sustenta que substituída por endereço MAC; no caso, a regra decisiva é: guardada por função de derivação/hash apropriada com sal, não reversível como cifra comum.

**Conceito:** senhas.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [15. Hash, MAC e armazenamento de senhas](semana_02_estudo.md#s2-d4-hash-hmac-senhas).
### Comentário S2S050

**Alternativa correta: D.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que necessidade de DNS; no caso, a regra decisiva é: necessidade de autorização e de correção de vulnerabilidades da aplicação.
- **B)** Incorreta. A opção sustenta que todo uso de logs; no caso, a regra decisiva é: necessidade de autorização e de correção de vulnerabilidades da aplicação.
- **C)** Incorreta. A opção sustenta que necessidade de rede; no caso, a regra decisiva é: necessidade de autorização e de correção de vulnerabilidades da aplicação.
- **D)** Correta. necessidade de autorização e de correção de vulnerabilidades da aplicação. A proposição aplica o ponto decisivo de controles complementares..

**Conceito:** controles complementares.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [8. Controles e defesa em profundidade](semana_02_estudo.md#s2-d4-controles), [10. IDS × IPS](semana_02_estudo.md#s2-d4-ids-ips) e [20. Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup).
### Comentário S2S051

**Alternativa correta: B.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que SMTP, DNS e DHCP; no caso, a regra decisiva é: LDAP, SNMP e NTP.
- **B)** Correta. LDAP, SNMP e NTP. A proposição aplica o ponto decisivo de LDAP, SNMP e NTP..
- **C)** Incorreta. A opção sustenta que SFTP, ARP e ICMP; no caso, a regra decisiva é: LDAP, SNMP e NTP.
- **D)** Incorreta. A opção sustenta que HTTP, PAT e TLS; no caso, a regra decisiva é: LDAP, SNMP e NTP.

**Conceito:** LDAP, SNMP e NTP.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).
### Comentário S2S052

**Alternativa correta: C.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que exclusão de arquivo; no caso, a regra decisiva é: observação de processos, não alteração de estado.
- **B)** Incorreta. A opção sustenta que alteração de DACL; no caso, a regra decisiva é: observação de processos, não alteração de estado.
- **C)** Correta. observação de processos, não alteração de estado. A proposição aplica o ponto decisivo de comandos de observação..
- **D)** Incorreta. A opção sustenta que restauração de backup; no caso, a regra decisiva é: observação de processos, não alteração de estado.

**Conceito:** comandos de observação.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-10).
### Comentário S2S053

**Alternativa correta: B.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que é ignorada se existir gateway; no caso, a regra decisiva é: prevalece sobre rota padrão para destino correspondente.
- **B)** Correta. prevalece sobre rota padrão para destino correspondente. A proposição aplica o ponto decisivo de rotas específicas..
- **C)** Incorreta. A opção sustenta que só existe em IPv6; no caso, a regra decisiva é: prevalece sobre rota padrão para destino correspondente.
- **D)** Incorreta. A opção sustenta que substitui ARP local; no caso, a regra decisiva é: prevalece sobre rota padrão para destino correspondente.

**Conceito:** rotas específicas.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).
### Comentário S2S054

**Alternativa correta: A.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. não há garantias nativas de ordenação/retransmissão, mas a aplicação pode criar mecanismos próprios. A proposição aplica o ponto decisivo de UDP..
- **B)** Incorreta. A opção sustenta que não pode obter confiabilidade adicional; no caso, a regra decisiva é: não há garantias nativas de ordenação/retransmissão, mas a aplicação pode criar mecanismos próprios.
- **C)** Incorreta. A opção sustenta que todo datagrama chega duplicado; no caso, a regra decisiva é: não há garantias nativas de ordenação/retransmissão, mas a aplicação pode criar mecanismos próprios.
- **D)** Incorreta. A opção sustenta que TCP passa a ser obrigatório; no caso, a regra decisiva é: não há garantias nativas de ordenação/retransmissão, mas a aplicação pode criar mecanismos próprios.

**Conceito:** UDP.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-05).
### Comentário S2S055

**Alternativa correta: D.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que hash; no caso, a regra decisiva é: criptografia.
- **B)** Incorreta. A opção sustenta que checksum sem chave; no caso, a regra decisiva é: criptografia.
- **C)** Incorreta. A opção sustenta que assinatura isolada; no caso, a regra decisiva é: criptografia.
- **D)** Correta. criptografia. A proposição aplica o ponto decisivo de criptografia..

**Conceito:** criptografia.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [14. Criptografia simétrica e assimétrica](semana_02_estudo.md#s2-d4-criptografia) e [17. TLS](semana_02_estudo.md#s2-d4-tls).
### Comentário S2S056

**Alternativa correta: C.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que somente detectar alerta; no caso, a regra decisiva é: eliminar causa/persistência maliciosa após contenção, antes da recuperação controlada.
- **B)** Incorreta. A opção sustenta que apagar todas as evidências; no caso, a regra decisiva é: eliminar causa/persistência maliciosa após contenção, antes da recuperação controlada.
- **C)** Correta. eliminar causa/persistência maliciosa após contenção, antes da recuperação controlada. A proposição aplica o ponto decisivo de erradicação..
- **D)** Incorreta. A opção sustenta que aplicar RPO; no caso, a regra decisiva é: eliminar causa/persistência maliciosa após contenção, antes da recuperação controlada.

**Conceito:** erradicação.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).
### Comentário S2S057

**Alternativa correta: C.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que latência; no caso, a regra decisiva é: autorização.
- **B)** Incorreta. A opção sustenta que CIDR; no caso, a regra decisiva é: autorização.
- **C)** Correta. autorização. A proposição aplica o ponto decisivo de autorização..
- **D)** Incorreta. A opção sustenta que NTP; no caso, a regra decisiva é: autorização.

**Conceito:** autorização.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Autenticação, autorização, auditoria e não repúdio](semana_02_estudo.md#s2-d4-identidade-auditoria).
### Comentário S2S058

**Alternativa correta: B.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que para resolver nomes globalmente; no caso, a regra decisiva é: no enlace local, não como identificador fim a fim roteável.
- **B)** Correta. no enlace local, não como identificador fim a fim roteável. A proposição aplica o ponto decisivo de MAC no enlace..
- **C)** Incorreta. A opção sustenta que para cifrar HTTP; no caso, a regra decisiva é: no enlace local, não como identificador fim a fim roteável.
- **D)** Incorreta. A opção sustenta que para autenticar pessoa usuária; no caso, a regra decisiva é: no enlace local, não como identificador fim a fim roteável.

**Conceito:** MAC no enlace.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [6. Placa de rede](semana_02_estudo.md#s2-d1-nic).
### Comentário S2S059

**Alternativa correta: A.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Correta. publicação controlada e distribuição de requisições, conforme configuração. A proposição aplica o ponto decisivo de proxy reverso..
- **B)** Incorreta. A opção sustenta que substituir banco de dados; no caso, a regra decisiva é: publicação controlada e distribuição de requisições, conforme configuração.
- **C)** Incorreta. A opção sustenta que eliminar TLS; no caso, a regra decisiva é: publicação controlada e distribuição de requisições, conforme configuração.
- **D)** Incorreta. A opção sustenta que criar endereços IP por DHCP; no caso, a regra decisiva é: publicação controlada e distribuição de requisições, conforme configuração.

**Conceito:** proxy reverso.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Mapa de revisão do Dia 6](semana_02_estudo.md#s2-d6-rf-mx-06).
### Comentário S2S060

**Alternativa correta: D.**

**Nível:** Muito difícil

**Uso:** Simulado

**Análise das alternativas:**

- **A)** Incorreta. A opção sustenta que registrar somente a letra certa; no caso, a regra decisiva é: classificar a falha, escrever regra, contraexemplo e seção de recuperação.
- **B)** Incorreta. A opção sustenta que apagar questões erradas; no caso, a regra decisiva é: classificar a falha, escrever regra, contraexemplo e seção de recuperação.
- **C)** Incorreta. A opção sustenta que repetir respostas sem diagnóstico; no caso, a regra decisiva é: classificar a falha, escrever regra, contraexemplo e seção de recuperação.
- **D)** Correta. classificar a falha, escrever regra, contraexemplo e seção de recuperação. A proposição aplica o ponto decisivo de caderno de erros..

**Conceito:** caderno de erros.

**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.

**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.

**Referência:** [Tríade CIA](semana_02_estudo.md#s2-d4-cia).
