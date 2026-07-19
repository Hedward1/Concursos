# Auditoria substantiva de níveis e cobertura — super simulado da Semana 2

Esta auditoria considera os 60 itens já integrados e as nove substituições aplicadas ao super simulado. Sete substituições corrigiram a cobertura do Dia 1; S2S010 e S2S017 deixaram de ser mera recuperação literal. Uma segunda leitura independente também aproximou os distratores de S2S024, S2S041, S2S042, S2S057, S2S059 e S2S060 sem mudar seus gabaritos.

O nível não decorre de cota nem da quantidade de termos mencionados na alternativa. **Médio** indica uma decisão aplicada; **Difícil**, comparação sutil ou decisões encadeadas; **Muito difícil**, três ou mais filtros realmente independentes, com distratores que falhem em etapas distintas. Associar três protocolos a três funções, reproduzir uma sequência já dada pelo enunciado ou derivar vários valores do mesmo cálculo continua sendo reconhecimento ou uma única cadeia, não três filtros.

| ID | Nível antes da auditoria | Nível final sem cotas | Justificativa cognitiva | Dia de cobertura |
|---|---|---|---|---:|
| S2S001 | Médio | Difícil | Exige decidir que o destino é remoto e, depois, separar o IP fim a fim do quadro recriado em cada enlace. | Dia 2 |
| S2S002 | Médio | Difícil | Exige localizar o bloco do `/27` e derivar corretamente rede, broadcast e faixa de hosts. | Dia 2 |
| S2S003 | Médio | Médio | As três assertivas se resolvem por uma única comparação direta entre as funções de hub, switch e roteador. | Dia 1 |
| S2S004 | Médio | Difícil | Exige selecionar ND para o próximo salto IPv6 e preservar no pacote o endereço remoto. | Dia 2 |
| S2S005 | Médio | Difícil | Exige distinguir simultaneamente dado útil de vazão e variação de atraso de latência média. | Dia 1 |
| S2S006 | Médio | Médio | Cobra uma única distinção conceitual: OSI como modelo e correspondência apenas aproximada com TCP/IP. | Dia 2 |
| S2S007 | Médio | Médio | Basta testar a rota local e escolher a padrão quando o destino não pertence ao prefixo conectado. | Dia 2 |
| S2S008 | Médio | Difícil | Exige separar estrela física de meio lógico e contrastar hub compartilhado com switch full-duplex. | Dia 1 |
| S2S009 | Médio | Médio | A resolução depende de reconhecer uma única exceção operacional: o uso ponto a ponto de `/31`. | Dia 2 |
| S2S010 | Médio | Médio | Na substituta, é preciso associar os cabeçalhos observados às PDUs de enlace, rede e transporte. | Dia 2 |
| S2S011 | Médio | Médio | Uma única decisão diagnóstica isola DNS depois de endereço, gateway e acesso por IP já comprovados. | Dia 3 |
| S2S012 | Médio | Difícil | Exige reconhecer QUIC sobre UDP como HTTP/3 e manter a validação TLS no fluxo. | Dia 3 |
| S2S013 | Médio | Médio | Associa diretamente SMTP, IMAP e POP3 às funções já enunciadas; reproduzir esse mapa funcional não cria uma cadeia de diagnóstico. | Dia 3 |
| S2S014 | Médio | Difícil | Exige identificar SFTP como subsistema SSH e, separadamente, FTPS como FTP protegido por TLS. | Dia 3 |
| S2S015 | Médio | Médio | Cobra uma única fronteira conceitual: porta sugere serviço, mas não comprova conteúdo, identidade ou proteção. | Dia 3 |
| S2S016 | Médio | Médio | Cobra os papéis diretos de manager, agent, MIB e OID em um único fluxo de consulta e notificação. | Dia 3 |
| S2S017 | Médio | Difícil | É preciso perceber a colisão das portas de origem, escolher portas públicas distintas e manter a associação stateful para devolver as respostas. | Dia 3 |
| S2S018 | Médio | Médio | Basta limitar a conclusão do certificado à identidade da chave e à proteção do canal, rejeitando extrapolações. | Dia 4 |
| S2S019 | Médio | Difícil | Exige distinguir a falsificação inicial do IP/MAC da captura posterior do tráfego. | Dia 4 |
| S2S020 | Médio | Difícil | Integra controles de defesa em profundidade, mas a decisão central é rejeitar um controle universal e cobrir superfícies distintas; os controles listados não são filtros independentes. | Dia 4 |
| S2S021 | Médio | Difícil | Exige escolher HMAC para segredo compartilhado e assinatura assimétrica para verificação por terceiros. | Dia 4 |
| S2S022 | Médio | Difícil | Na substituta, é preciso classificar a estrela física e depois distinguir o comportamento lógico de hub e switch. | Dia 1 |
| S2S023 | Médio | Difícil | Exige posicionar o IDS fora do caminho para observar e o IPS em linha para bloquear. | Dia 4 |
| S2S024 | Médio | Difícil | Contrasta a proteção de SAE com os limites do modo de transição, da senha e de controles complementares em uma comparação técnica encadeada. | Dia 4 |
| S2S025 | Difícil | Difícil | Aplica uma única cadeia de resposta: conter e preservar antes de erradicar, restaurar e validar; a enumeração de ações não multiplica o número de filtros. | Dia 4 |
| S2S026 | Difícil | Difícil | Exige calcular separadamente perda para RPO e indisponibilidade para RTO antes de comparar os objetivos. | Dia 4 |
| S2S027 | Difícil | Difícil | Exige separar continuidade diante de falha física de recuperação lógica por versão isolada e íntegra. | Dia 4 |
| S2S028 | Difícil | Difícil | Exige combinar cifração para o destinatário e assinatura do remetente para verificação pública. | Dia 4 |
| S2S029 | Difícil | Muito difícil | Na substituta, alcance, 10 Gbit/s e imunidade eletromagnética funcionam como três filtros independentes. | Dia 1 |
| S2S030 | Difícil | Difícil | Exige aprender a origem e tratar o destino desconhecido; o aprendizado posterior de B é consequência da mesma regra aplicada à resposta, não um terceiro filtro independente. | Dia 1 |
| S2S031 | Difícil | Difícil | Exige reconhecer a atualização perdida e identificar a necessidade de sincronizar leitura, cálculo e gravação. | Dia 5 |
| S2S032 | Difícil | Difícil | Exige associar a ordem global à espera circular e compreender que as outras condições de Coffman podem permanecer. | Dia 5 |
| S2S033 | Difícil | Médio | Identificado o adiamento indefinido, uma única decisão aplica aging como resposta direta à starvation. | Dia 5 |
| S2S034 | Difícil | Médio | Identificado o livelock simétrico, uma única decisão escolhe aleatoriedade ou assimetria para quebrar o ciclo. | Dia 5 |
| S2S035 | Difícil | Difícil | Monta uma linha FCFS e deriva três métricas do mesmo início e término; os valores compartilham o mesmo raciocínio intermediário. | Dia 5 |
| S2S036 | Difícil | Difícil | Exige acompanhar o esgotamento do semáforo e o desbloqueio posterior provocado por `post`. | Dia 5 |
| S2S037 | Difícil | Difícil | Exige escolher DMA para o bloco e manter interrupção de conclusão, driver e tratamento de erros. | Dia 5 |
| S2S038 | Difícil | Difícil | Exige calcular o efeito da permissão herdada e expressar a exceção individual por ACE explícita. | Dia 5 |
| S2S039 | Difícil | Muito difícil | Requer selecionar a classe de grupo, decodificar dois modos octais e diferenciar `x` em arquivo e diretório. | Dia 5 |
| S2S040 | Difícil | Difícil | Exige localizar a última camada comprovada e testar TCP e firewall antes de TLS ou aplicação. | Dia 6 |
| S2S041 | Difícil | Difícil | Separa vetores e ordena contenção, evidência, erradicação e recuperação, mas permanece uma decisão coordenada de resposta ao incidente. | Dia 6 |
| S2S042 | Difícil | Médio | O enunciado fornece a cadeia permitida; basta rejeitar a opção que acrescenta uma aresta desnecessária, ainda que limitada a HTTPS ou a outra porta conhecida. | Dia 6 |
| S2S043 | Difícil | Difícil | Exige separar cache e endpoint de validação TLS, formando duas etapas sucessivas de diagnóstico. | Dia 6 |
| S2S044 | Difícil | Difícil | Distingue autenticação do túnel de autorização e menor privilégio nos destinos, com auditoria como consequência operacional. | Dia 6 |
| S2S045 | Difícil | Médio | Aplica diretamente o procedimento de preservar o bruto, normalizar offsets conhecidos e corrigir a fonte temporal para eventos futuros. | Dia 6 |
| S2S046 | Difícil | Difícil | Distingue restauração dentro do RPO de retorno funcional dentro do RTO e exige validar as dependências do serviço. | Dia 6 |
| S2S047 | Difícil | Difícil | Percorre uma única cadeia de atribuição — tupla e horário, entrada PAT e registros internos — sem alternativas que exijam três diagnósticos independentes. | Dia 6 |
| S2S048 | Difícil | Difícil | Na substituta, é preciso classificar a rede local da sede e a interligação ampla entre estados. | Dia 1 |
| S2S049 | Muito difícil | Médio | O próprio enunciado descreve encaminhamento, comutação e associação Wi‑Fi; a resposta apenas nomeia as três funções do gabinete. | Dia 1 |
| S2S050 | Muito difícil | Muito difícil | Na substituta, é preciso contar VLANs, compreender o bridging do AP e exigir roteamento entre os domínios. | Dia 1 |
| S2S051 | Muito difícil | Médio | Associa diretamente três sintomas a LDAP, SNMP e NTP; é um mapa funcional, não uma investigação com três filtros. | Dia 3 |
| S2S052 | Muito difícil | Difícil | Exige distinguir observação de mutação e selecionar a sequência de consultas que preserva a evidência. | Dia 5 |
| S2S053 | Muito difícil | Muito difícil | Exige aplicar maior prefixo, escolher o próximo salto, resolver seu MAC e preservar o IP final. | Dia 2 |
| S2S054 | Muito difícil | Difícil | Exige separar confiabilidade implementada pela aplicação das garantias que continuam ausentes no UDP. | Dia 3 |
| S2S055 | Muito difícil | Difícil | Na substituta, exige calcular pares não ordenados e validar o trade-off entre redundância e complexidade. | Dia 1 |
| S2S056 | Muito difícil | Difícil | Classifica ações concretas dentro de um único ciclo de resposta; repetir a mesma distinção em vários verbos não cria filtros independentes. | Dia 6 |
| S2S057 | Muito difícil | Difícil | Distingue autenticação de autorização por papel e objeto e completa a solução com menor privilégio e registro. | Dia 6 |
| S2S058 | Muito difícil | Difícil | Exige separar a renovação dos MACs por enlace da permanência dos IPs fim a fim. | Dia 2 |
| S2S059 | Muito difícil | Difícil | Compara controles nas fronteiras do proxy, mas a escolha decorre de uma única configuração coerente de confiança e proteção ponta a ponta. | Dia 3 |
| S2S060 | Muito difícil | Difícil | Localiza a falha antes do transporte e ordena rede antes de TLS; resolução, rota e ND integram a mesma cadeia de diagnóstico. | Dia 2 |

## Totais e condição de aplicação

| Distribuição | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Antes da auditoria | 24 | 24 | 12 | 60 |
| Final integrada, sem cotas | 16 | 40 | 4 | 60 |

- Cobertura: exatamente 10 itens para cada Dia 1–6.
- Reformulações: nove itens com letras originais preservadas; sete corrigiram a cobertura do Dia 1 e duas eliminaram recuperação meramente literal.
- Distratores aproximados após a leitura independente: S2S024, S2S041, S2S042, S2S057, S2S059 e S2S060, sempre com análise A–D sincronizada e gabarito preservado.
- Muito difíceis finais: S2S029 cruza alcance, capacidade e interferência; S2S039 exige avaliar classe, dois tipos de objeto e comando negativo; S2S050 testa separadamente domínio, bridging e roteamento; S2S053 encadeia maior prefixo, próximo salto, ARP e preservação do IP final.
- A distribuição final registra a dificuldade observada. Ela não tenta reconstruir artificialmente a matriz de planejamento por simples troca de rótulos.
