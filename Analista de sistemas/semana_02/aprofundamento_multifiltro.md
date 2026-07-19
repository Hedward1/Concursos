# Aprofundamento multifiltro — Semana 2

Este lote pós-auditoria aprofunda quatro itens, um em cada dia que terminaria sem questão principal `Muito difícil`. As letras, os usos e os objetivos pedagógicos são preservados; a dificuldade passa a decorrer de três ou mais filtros independentes ensinados na apostila.

## S2D1Q048 — VLAN, bridge sem fio, roteamento e contenção

**ID:** S2D1Q048

**Estado do item:** Aprofundamento pós-auditoria.

**Enunciado substitutivo:** Um access point em bridge mapeia o SSID `Corporativo` para a VLAN 30 e o SSID `Visitantes` para a VLAN 40. Estações cabeadas também usam a VLAN 30, os enlaces Ethernet são full-duplex e uma política no roteador bloqueia o tráfego entre as duas VLANs. Analise as afirmações.

I. Sem isolamento ou filtro adicional, broadcasts de enlace do SSID `Corporativo` podem alcançar as estações cabeadas da VLAN 30.

II. A VLAN 40 forma outro domínio de broadcast, e a comunicação com a VLAN 30 depende de roteamento e de política que a autorize.

III. A contenção no rádio da VLAN 30 não deve ser descrita como colisão Ethernet; nos enlaces cabeados full-duplex não ocorrem colisões.

Está correto o que se afirma em:

**Alternativas substitutivas:**

A) I, II e III.

B) I e II, apenas.

C) I e III, apenas.

D) II e III, apenas.

**Gabarito original:** A.

**Gabarito verificado:** A.

**Nível anterior auditado:** Difícil.

**Nível final:** Muito difícil.

**Uso:** Simulado.

**Referência precisa:** [Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap) e [Domínio de colisão e domínio de broadcast](semana_02_estudo.md#s2-d1-dominios), nos trechos sobre bridge, SSID/VLAN, roteamento e contenção Wi-Fi.

**Comentário substitutivo completo:**

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A)** está correta: as três afirmações preservam, respectivamente, o alcance do broadcast na VLAN em bridge, a separação e o roteamento entre VLANs e a diferença entre contenção Wi-Fi e colisão Ethernet.
- **B)** está errada: I e II são verdadeiras, mas III também é; Wi-Fi compartilha tempo de transmissão sem se tornar um domínio de colisão Ethernet, e full-duplex elimina colisões nos enlaces cabeados.
- **C)** está errada: I e III são verdadeiras, mas II também é; VLANs diferentes separam broadcasts e precisam de roteamento autorizado para se comunicar.
- **D)** está errada: II e III são verdadeiras, mas I também é; o AP em bridge normalmente estende a VLAN 30 ao lado sem fio quando não há isolamento ou filtro.
- **Conceito cobrado:** integração entre bridge do AP, VLAN, domínio de broadcast, roteamento e comportamento dos meios sem fio e cabeado.
- **Pegadinha usada:** tratar SSID como fronteira automática, equiparar contenção Wi-Fi a colisão Ethernet ou imaginar que VLANs se comunicam apenas por estarem no mesmo equipamento.
- **Como pensar para acertar:** resolva três fronteiras separadamente: qual VLAN o AP estende, onde termina o broadcast e que mecanismo rege o acesso ao meio em cada enlace.
- **Referência à apostila de estudo:** [Access point](semana_02_estudo.md#s2-d1-roteador-gateway-ap) e [Domínios](semana_02_estudo.md#s2-d1-dominios).

## S2D3Q150 — Fluxo do cliente ao backend publicado

**ID:** S2D3Q150

**Estado do item:** Aprofundamento pós-auditoria.

**Enunciado substitutivo:** Uma estação recém-conectada recebe configuração automática e acessa, por nome, um portal remoto. Na borda, vários clientes compartilham um endereço público por PAT; no destino, um proxy reverso publica a aplicação. Analise as afirmações.

I. O DHCP pode fornecer endereço, prefixo, gateway e resolvedor, mas a resolução do nome do portal pertence ao DNS.

II. Para destino remoto, o pacote mantém o IP do servidor enquanto o quadro local usa o próximo salto; na borda, o PAT pode traduzir a tupla de origem.

III. Depois do transporte e da proteção TLS, o proxy reverso pode terminar a conexão externa e iniciar outra para o backend, sem substituir DNS, roteamento ou autorização da aplicação.

Está correto o que se afirma em:

**Alternativas substitutivas:**

A) I e II, apenas.

B) I, II e III.

C) I e III, apenas.

D) II e III, apenas.

**Gabarito original:** B.

**Gabarito verificado:** B.

**Nível anterior auditado:** Difícil.

**Nível final:** Muito difícil.

**Uso:** Simulado.

**Referência precisa:** [Fluxo integrado de acesso a um portal](semana_02_estudo.md#s2-d3-fluxo-integrado), com apoio de [NAT e PAT](semana_02_estudo.md#s2-d3-nat-pat) e [Proxy direto e proxy reverso](semana_02_estudo.md#s2-d3-proxy).

**Comentário substitutivo completo:**

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A)** está errada: I e II são verdadeiras, mas III também é; o proxy reverso representa os servidores publicados e pode estabelecer um fluxo separado até o backend.
- **B)** está correta: as três afirmações mantêm as fronteiras entre configuração, resolução, próximo salto, tradução, proteção do canal e publicação da aplicação.
- **C)** está errada: I e III são verdadeiras, mas II também é; o quadro aponta para o próximo salto sem trocar o IP remoto, e o PAT pode alterar a origem na borda.
- **D)** está errada: II e III são verdadeiras, mas I também é; DHCP pode informar o resolvedor, porém não executa a resolução do nome do portal.
- **Conceito cobrado:** dependências e limites de DHCP, DNS, gateway, PAT, TCP/TLS/HTTP e proxy reverso no mesmo acesso.
- **Pegadinha usada:** atribuir a um componente a função do seguinte ou supor que proxy, PAT ou porta conhecida substitui as demais etapas.
- **Como pensar para acertar:** percorra configuração, resolução, encaminhamento/tradução, transporte/proteção e publicação, perguntando em cada etapa o que muda e o que permanece.
- **Referência à apostila de estudo:** [Fluxo integrado](semana_02_estudo.md#s2-d3-fluxo-integrado), [NAT/PAT](semana_02_estudo.md#s2-d3-nat-pat) e [Proxy](semana_02_estudo.md#s2-d3-proxy).

## S2D5Q245 — Permissões Linux e Windows em três camadas

**ID:** S2D5Q245

**Estado do item:** Aprofundamento pós-auditoria.

**Enunciado substitutivo:** Considere permissões em Linux e Windows.

I. Em um arquivo Linux com modo `750`, o grupo pode ler e executar, mas não gravar.

II. Em um diretório Linux com modo `640`, o grupo pode ler a lista de nomes, mas a ausência de `x` impede atravessar o caminho e acessar normalmente as entradas.

III. No acesso remoto do Windows, permissões de compartilhamento e NTFS podem atuar em conjunto; a DACL reúne ACEs aplicáveis e a permissão efetiva não é simplesmente a mais ampla.

Está correto o que se afirma em:

**Alternativas substitutivas:**

A) I, apenas.

B) II e III, apenas.

C) I, II e III.

D) I e III, apenas.

**Gabarito original:** C.

**Gabarito verificado:** C.

**Nível anterior auditado:** Difícil.

**Nível final:** Muito difícil.

**Uso:** Simulado.

**Referência precisa:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes), especialmente a semântica de `rwx` em arquivo e diretório, DACL/ACE e combinação entre compartilhamento e NTFS.

**Comentário substitutivo completo:**

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A)** está errada: I é verdadeira, mas II e III também são; os bits mudam de efeito operacional em diretórios, e o acesso remoto do Windows atravessa mais de uma camada de autorização.
- **B)** está errada: II e III são verdadeiras, mas I também é; o algarismo `5` representa `r-x`, sem permissão de gravação para o grupo.
- **C)** está correta: as três afirmações aplicam corretamente a tríade em dois tipos de objeto Linux e a composição de autorização no Windows.
- **D)** está errada: I e III são verdadeiras, mas II também é; `r` permite listar nomes, enquanto a falta de `x` impede a travessia normal do diretório.
- **Conceito cobrado:** diferenças da tríade `rwx` por tipo de objeto e composição de DACL, compartilhamento e NTFS.
- **Pegadinha usada:** transportar a semântica de arquivo para diretório ou tratar a permissão mais ampla do Windows como resultado automático.
- **Como pensar para acertar:** identifique primeiro o objeto Linux e a tríade da classe aplicável; depois, no Windows, confira todas as camadas de autorização atravessadas.
- **Referência à apostila de estudo:** [Permissões em Linux e Windows](semana_02_estudo.md#s2-d5-permissoes).

## S2D6Q300 — RPO, RTO, dependências e continuidade efetiva

**ID:** S2D6Q300

**Estado do item:** Aprofundamento pós-auditoria.

**Enunciado substitutivo:** Um incidente ocorre às 14h. O banco é restaurado ao ponto consistente das 13h35 e a infraestrutura volta às 16h30, mas a fila de pagamentos permanece incompatível e o serviço de autenticação necessário está indisponível. O plano define RPO de 30 minutos e RTO de 4 horas. Analise as afirmações.

I. O ponto das 13h35 atende ao RPO, mas esse resultado isolado não comprova a recuperação do serviço.

II. O horário das 16h30 está dentro da janela de RTO; contudo, enquanto fila e autenticação impedirem a transação de ponta a ponta, o serviço ainda não foi efetivamente restabelecido.

III. O teste de continuidade deve validar integridade, dependências, responsabilidades, comunicação e retorno controlado; a existência do backup não substitui essas verificações.

Está correto o que se afirma em:

**Alternativas substitutivas:**

A) I e II, apenas.

B) I, II e III.

C) I e III, apenas.

D) II e III, apenas.

**Gabarito original:** B.

**Gabarito verificado:** B.

**Nível anterior auditado:** Difícil.

**Nível final:** Muito difícil.

**Uso:** Simulado.

**Referência precisa:** [Recuperação por dependências e validação ponta a ponta](semana_02_estudo.md#s2-d6-recuperacao-dependencias) e [Backup e disponibilidade](semana_02_estudo.md#s2-d4-backup), nos trechos sobre RPO, RTO, dependências e validação do negócio.

**Comentário substitutivo completo:**

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A)** está errada: I e II são verdadeiras, mas III também é; continuidade exige testar componentes organizacionais e técnicos além do ponto e do horário de restauração.
- **B)** está correta: as três afirmações calculam os objetivos temporais e preservam a diferença entre infraestrutura disponível e serviço de negócio funcional.
- **C)** está errada: I e III são verdadeiras, mas II também é; 16h30 fica duas horas e meia após o incidente, embora as dependências ainda impeçam declarar recuperação.
- **D)** está errada: II e III são verdadeiras, mas I também é; recuperar 13h35 em incidente às 14h implica perda potencial de 25 minutos, dentro do RPO de 30.
- **Conceito cobrado:** avaliação conjunta de RPO, RTO, dependências e critérios de continuidade efetiva.
- **Pegadinha usada:** declarar sucesso pelo relógio ou pelo backup sem validar a transação completa e as dependências do serviço.
- **Como pensar para acertar:** calcule perda e indisponibilidade, depois teste dados, integrações, pessoas e operação; objetivo temporal atendido não encerra sozinho a recuperação.
- **Referência à apostila de estudo:** [Continuidade](semana_02_estudo.md#s2-d6-rf-mx-09) e [Backup](semana_02_estudo.md#s2-d4-backup).

## Resultado da exceção pós-auditoria

| Dia | Item | Nível anterior | Nível final | Filtros independentes |
|---|---|---|---|---|
| 1 | S2D1Q048 | Difícil | Muito difícil | bridge/VLAN; broadcast/roteamento; contenção Wi-Fi/full-duplex |
| 3 | S2D3Q150 | Difícil | Muito difícil | configuração/resolução; próximo salto/PAT; transporte/TLS/proxy |
| 5 | S2D5Q245 | Difícil | Muito difícil | arquivo Linux; diretório Linux; autorização remota Windows |
| 6 | S2D6Q300 | Difícil | Muito difícil | RPO; RTO/serviço efetivo; dependências/continuidade |
