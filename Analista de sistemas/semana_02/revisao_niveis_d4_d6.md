# Recalibração semântica de níveis — Semana 2, Dias 4 a 6

Data da revisão: **19/07/2026**.

## Contrato de integração

- Escopo fechado: `S2D4Q151` a `S2D6Q300`.
- Valores permitidos em nível: `Médio`, `Difícil` e `Muito difícil`.
- Valores permitidos nos campos de alerta: `Sim` e `Não`.
- `Reescrita = Sim` significa que enunciado ou alternativas precisam mudar por ambiguidade, distrator absurdo/alheio ou pista visual substantiva. Mudança isolada de nível não conta como reescrita.
- O nível recomendado considera o esforço real do item atual, sem preservar cotas por posição: `Médio` exige aplicação direta; `Difícil`, ao menos duas regras ou decisões; `Muito difícil`, três ou mais filtros independentes ou integração equivalente com alternativas próximas.
- A coluna `Observação` registra ação não capturada pelos três alertas e usa `—` quando não há ação adicional.
- Foram avaliados os enunciados e as alternativas atuais. Os comentários do Dia 6, corrigidos em lote paralelo, não influenciaram os alertas; `S2D6Q277` foi lida já com o enunciado corrigido.

## Dia 4 — S2D4Q151 a S2D4Q200

| ID | Nível atual | Nível recomendado | Justificativa cognitiva | Ambiguidade | Distrator absurdo/alheio | Pista de comprimento | Reescrita | Observação |
|---|---|---|---|:---:|:---:|:---:|:---:|---|
| S2D4Q151 | Médio | Médio | Reconhece diretamente segurança como ciclo contínuo de gestão de riscos. | Não | Não | Sim | Sim | A correta é a única alternativa que enumera todo o ciclo e se destaca pela extensão. |
| S2D4Q152 | Médio | Médio | Aplica diretamente a definição de risco residual e sua reavaliação. | Não | Não | Não | Não | — |
| S2D4Q153 | Médio | Médio | Identifica confidencialidade a partir da possível divulgação de dados. | Não | Não | Não | Não | — |
| S2D4Q154 | Médio | Difícil | Julga três afirmações e relaciona exfiltração, cifra e backup aos objetivos da tríade CIA. | Não | Não | Não | Não | — |
| S2D4Q155 | Médio | Médio | Distingue diretamente autenticação de autorização no fluxo descrito. | Não | Não | Não | Não | — |
| S2D4Q156 | Médio | Médio | Aplica uma única regra: MFA combina categorias distintas de fatores. | Não | Não | Não | Não | — |
| S2D4Q157 | Médio | Médio | Reconhece ABAC pelos atributos explicitamente enumerados. | Não | Sim | Sim | Sim | A correta é a sigla isolada `ABAC`; biometria e accounting não são modelos concorrentes de autorização. |
| S2D4Q158 | Médio | Médio | Recupera diretamente o significado e a função de accounting em AAA. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que qualifica a relação entre accounting e auditoria. |
| S2D4Q159 | Médio | Difícil | Combina assinatura, proteção da chave privada, vínculo de identidade e cadeia de evidências. | Não | Não | Não | Não | — |
| S2D4Q160 | Médio | Difícil | Seleciona simultaneamente contexto do evento, proteção de integridade e sincronização temporal dos registros. | Não | Não | Sim | Sim | A correta reúne todos os requisitos e supera claramente os distratores em extensão. |
| S2D4Q161 | Médio | Muito difícil | Classifica cinco elementos independentes como ativo, ameaça, vulnerabilidade, evento e incidente. | Não | Não | Não | Não | — |
| S2D4Q162 | Médio | Médio | Separa diretamente fraqueza explorável de risco calculado por probabilidade e impacto. | Não | Não | Não | Não | — |
| S2D4Q163 | Médio | Difícil | Distingue o evento inicial do incidente confirmado após correlação de evidências. | Não | Não | Não | Não | — |
| S2D4Q164 | Médio | Médio | Confere associações diretas entre ameaça, vulnerabilidade e controle. | Não | Não | Sim | Sim | A correta é a única alternativa extensa que preserva as três associações. |
| S2D4Q165 | Médio | Médio | Contrasta diretamente vírus dependente de hospedeiro e worm autorreplicante. | Não | Não | Sim | Sim | A correta é sensivelmente mais longa e concentra toda a distinção pedida. |
| S2D4Q166 | Médio | Médio | Reconhece cavalo de Troia pelo disfarce e pela indução à execução. | Não | Sim | Não | Sim | DDoS não é categoria concorrente de programa malicioso no cenário e torna um distrator alheio. |
| S2D4Q167 | Médio | Difícil | Relaciona ransomware a exfiltração, cifra, interrupção e aos três objetivos da tríade CIA. | Não | Não | Não | Não | — |
| S2D4Q168 | Médio | Médio | Confere definições diretas de spyware, rootkit e botnet. | Não | Não | Não | Não | — |
| S2D4Q169 | Médio | Difícil | Associa quatro modalidades de phishing ao alvo ou ao canal correspondente. | Não | Não | Sim | Sim | A correta é a única enumeração completa e é muito mais longa que os distratores. |
| S2D4Q170 | Médio | Difícil | Identifica autoridade e urgência e escolhe verificação independente com autorização formal. | Não | Não | Não | Não | — |
| S2D4Q171 | Difícil | Difícil | Distingue roubo de senha de captura de sessão, fadiga de aprovação e abuso de recuperação. | Não | Não | Não | Não | — |
| S2D4Q172 | Difícil | Difícil | Define spoofing e aplica a ressalva de que IP falsificado não assegura o retorno das respostas. | Não | Não | Sim | Sim | A correta tem quase o dobro da extensão média dos distratores e é a única qualificada. |
| S2D4Q173 | Difícil | Difícil | Contrasta captura passiva com posicionamento ativo capaz de observar e alterar a comunicação. | Não | Não | Sim | Sim | A correta é muito mais extensa e reúne sozinha as duas distinções. |
| S2D4Q174 | Difícil | Difícil | Identifica password spraying e depois o diferencia de credential stuffing. | Não | Não | Não | Não | — |
| S2D4Q175 | Difícil | Difícil | Infere saturação a montante e seleciona mitigação antes do firewall local. | Não | Não | Sim | Sim | A correta é a única resposta extensa com um conjunto de medidas tecnicamente viáveis. |
| S2D4Q176 | Difícil | Difícil | Classifica três controles simultaneamente por natureza e função predominante. | Não | Não | Não | Não | — |
| S2D4Q177 | Difícil | Difícil | Detecta dependência administrativa comum e infere seu efeito sobre várias camadas de defesa. | Não | Não | Não | Não | — |
| S2D4Q178 | Difícil | Difícil | Combina estado de conexão, qualidade da política e limites do firewall perante a aplicação. | Não | Não | Não | Não | — |
| S2D4Q179 | Difícil | Difícil | Integra menor exposição, documentação, revisão, registro e visibilidade sobre tráfego cifrado. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que acumula todas as práticas recomendadas. |
| S2D4Q180 | Difícil | Médio | Reconhece diretamente o IDS fora de banda a partir de cópia de tráfego e ausência de bloqueio. | Não | Sim | Sim | Sim | A correta é uma expressão curta; firewall como backup e VPN sem detecção são distratores alheios ao requisito. |
| S2D4Q181 | Difícil | Difícil | Relaciona erro de classificação, atuação preventiva em linha e impacto na disponibilidade. | Não | Não | Sim | Sim | A correta é quase duas vezes maior e a única que desenvolve toda a cadeia causal. |
| S2D4Q182 | Difícil | Difícil | Posiciona três camadas em segmentos distintos e limita os fluxos entre elas. | Não | Não | Sim | Sim | A correta se destaca como a única arquitetura detalhada e qualificada. |
| S2D4Q183 | Difícil | Difícil | Separa proteção do canal de confiança no endpoint e combina controles compensatórios. | Não | Não | Sim | Sim | A correta é muito mais extensa e reúne todas as ressalvas. |
| S2D4Q184 | Difícil | Difícil | Associa dois modelos de VPN aos respectivos usos e ainda verifica requisitos de segurança. | Não | Não | Sim | Sim | A correta é a única alternativa longa que cobre os dois modelos e seus limites. |
| S2D4Q185 | Difícil | Difícil | Distingue isolamento de camada 2 do controle necessário sobre tráfego roteado. | Não | Não | Sim | Sim | A correta é substancialmente mais longa e a única que integra VLAN e filtragem interna. |
| S2D4Q186 | Difícil | Difícil | Aplica menor privilégio a operações, objetos, origem, contexto e revisão periódica. | Não | Não | Sim | Sim | A correta concentra cinco restrições e supera visivelmente os distratores. |
| S2D4Q187 | Difícil | Difícil | Contrasta chaves, eficiência e aplicações de mecanismos simétricos e assimétricos. | Não | Não | Sim | Sim | A correta é a única descrição completa e muito mais extensa. |
| S2D4Q188 | Difícil | Difícil | Divide autenticação e estabelecimento de segredos dos mecanismos que protegem o tráfego volumoso. | Não | Não | Sim | Sim | A correta tem aproximadamente o dobro da extensão dos distratores. |
| S2D4Q189 | Difícil | Difícil | Percebe que arquivo e hash foram adulterados e exige uma referência autenticada independente. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que explicita o modelo de ataque. |
| S2D4Q190 | Difícil | Médio | Seleciona diretamente HMAC diante de segredo compartilhado e ausência de não repúdio. | Não | Não | Sim | Sim | A correta é sensivelmente mais curta que todos os distratores e se destaca visualmente. |
| S2D4Q191 | Muito difícil | Difícil | Combina função própria para senhas, salt individual, custo ajustável e gestão de parâmetros. | Não | Não | Não | Não | — |
| S2D4Q192 | Muito difícil | Difícil | Relaciona chave privada, chave pública, origem, integridade e ausência de confidencialidade automática. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que reúne propriedades e limite. |
| S2D4Q193 | Muito difícil | Difícil | Verifica cadeia, assinaturas, validade, nome, uso de chave e revogação, mas enfrenta distratores pouco próximos. | Não | Não | Sim | Sim | A correta é a única lista completa e se destaca claramente pela extensão. |
| S2D4Q194 | Muito difícil | Difícil | Ordena negociação, derivação de segredos, validação de identidade e proteção simétrica da sessão. | Não | Não | Sim | Sim | A correta tem quase o dobro da extensão média das demais. |
| S2D4Q195 | Muito difícil | Difícil | Distingue SAE das capturas offline e preserva limites contra senha fraca, ataque online e falhas. | Não | Não | Sim | Sim | A correta tem aproximadamente o dobro da extensão dos distratores e concentra todas as ressalvas. |
| S2D4Q196 | Muito difícil | Difícil | Integra 802.1X, identidade individual, validação do servidor, segmentação e monitoramento. | Não | Não | Sim | Sim | A correta é substancialmente mais longa e a única arquitetura completa. |
| S2D4Q197 | Muito difícil | Difícil | Ordena análise, contenção, erradicação e recuperação preservando evidências. | Não | Não | Sim | Sim | A correta é a alternativa mais longa e a única sequência integralmente qualificada. |
| S2D4Q198 | Muito difícil | Muito difícil | Julga incremental, diferencial, RPO e RTO em duas afirmações com quatro filtros independentes. | Não | Não | Sim | Sim | `I e II estão corretas` é muito mais curta que as três opções explicativas e denuncia a combinação. |
| S2D4Q199 | Muito difícil | Difícil | Combina isolamento, credenciais separadas, imutabilidade, versões e teste de restauração. | Não | Não | Sim | Sim | A correta é muito mais extensa e a única que enumera uma estratégia completa. |
| S2D4Q200 | Muito difícil | Difícil | Escolhe alta disponibilidade para falha presente e backup versionado para recuperação do passado. | Não | Não | Sim | Sim | A correta é a única resposta extensa que atende simultaneamente aos dois objetivos. |

## Dia 5 — S2D5Q201 a S2D5Q250

| ID | Nível atual | Nível recomendado | Justificativa cognitiva | Ambiguidade | Distrator absurdo/alheio | Pista de comprimento | Reescrita | Observação |
|---|---|---|---|:---:|:---:|:---:|:---:|---|
| S2D5Q201 | Médio | Médio | Distingue diretamente concorrência intercalada de paralelismo simultâneo. | Não | Não | Não | Não | — |
| S2D5Q202 | Médio | Médio | Recupera as definições usuais de programa, processo e thread. | Não | Não | Não | Não | — |
| S2D5Q203 | Médio | Médio | Reconhece o estado bloqueado pela espera explícita de E/S. | Não | Não | Não | Não | — |
| S2D5Q204 | Médio | Difícil | Relaciona redução do quantum a responsividade e aumento de trocas e sobrecarga. | Não | Não | Não | Não | — |
| S2D5Q205 | Médio | Médio | Reconhece atualização perdida no entrelaçamento já descrito passo a passo. | Não | Não | Sim | Sim | A correta é a única alternativa longa que nomeia o fenômeno e sua causa operacional. |
| S2D5Q206 | Médio | Difícil | Separa atomicidade de visibilidade e ordenação em uma sequência concorrente. | Não | Não | Não | Não | — |
| S2D5Q207 | Médio | Médio | Aplica diretamente a cooperação de todos os participantes no mesmo mutex. | Não | Não | Não | Não | — |
| S2D5Q208 | Médio | Médio | Seleciona diretamente semáforo contador para oito unidades equivalentes. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que explicita inicialização, aquisição e devolução. |
| S2D5Q209 | Médio | Difícil | Exige testar o predicado em laço e compreender liberação e reaquisição atômica do mutex. | Não | Não | Não | Não | — |
| S2D5Q210 | Médio | Difícil | Pondera retenção curta, multiprocessamento e desperdício de CPU na espera ativa. | Não | Não | Não | Não | — |
| S2D5Q211 | Médio | Difícil | Relaciona menor cópia da memória compartilhada à necessidade de sincronização e visibilidade. | Não | Não | Não | Não | — |
| S2D5Q212 | Médio | Difícil | Compara preservação de mensagens e alcance local ou em rede entre mecanismos de IPC. | Não | Não | Não | Não | — |
| S2D5Q213 | Médio | Médio | Reconhece diretamente a definição de impasse conjunto. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que descreve a dependência completa. |
| S2D5Q214 | Médio | Médio | Recupera diretamente a lista canônica das quatro condições de Coffman. | Não | Sim | Não | Sim | Os distratores são listas de termos de sistemas operacionais sem formar condições concorrentes próximas. |
| S2D5Q215 | Médio | Médio | Mapeia diretamente ordem global de locks à ruptura da espera circular. | Não | Não | Não | Não | — |
| S2D5Q216 | Médio | Médio | Mapeia diretamente aquisição integral antecipada à ruptura de posse e espera. | Não | Não | Não | Não | — |
| S2D5Q217 | Médio | Difícil | Exige reconhecer uma sequência segura e distinguir estado inseguro de deadlock já ocorrido. | Não | Não | Sim | Sim | A correta é muito mais extensa e a única que inclui a ressalva decisiva. |
| S2D5Q218 | Médio | Difícil | Combina demanda máxima, alocação corrente e disponibilidade na decisão do banqueiro. | Não | Não | Não | Não | — |
| S2D5Q219 | Médio | Difícil | Distingue a suficiência do ciclo para uma e para múltiplas instâncias de recursos. | Não | Não | Sim | Sim | A correta é substancialmente mais longa e a única que trata os dois casos. |
| S2D5Q220 | Médio | Difícil | Seleciona vítima por custo e combina aborto ou checkpoint com preservação da consistência. | Não | Não | Não | Não | — |
| S2D5Q221 | Difícil | Médio | Reconhece diretamente starvation e sua mitigação clássica por aging. | Não | Não | Não | Não | — |
| S2D5Q222 | Difícil | Médio | Reconhece diretamente livelock e o uso de backoff para romper simetria. | Não | Não | Não | Não | — |
| S2D5Q223 | Difícil | Difícil | Identifica inversão de prioridade no encadeamento de três classes e seleciona herança. | Não | Não | Não | Não | — |
| S2D5Q224 | Difícil | Difícil | Classifica três cenários independentes como deadlock, starvation e livelock. | Não | Não | Não | Não | — |
| S2D5Q225 | Difícil | Difícil | Infere contenção e possível dependência a partir de lock mantido durante E/S. | Não | Não | Não | Não | — |
| S2D5Q226 | Difícil | Difícil | Simula FCFS e calcula espera e retorno médios de três processos. | Não | Não | Não | Não | — |
| S2D5Q227 | Difícil | Difícil | Ordena três bursts por SJF e calcula a espera média. | Não | Não | Não | Não | — |
| S2D5Q228 | Difícil | Difícil | Simula preempções no SRTF e calcula o tempo de espera de cada processo. | Não | Não | Não | Não | — |
| S2D5Q229 | Difícil | Médio | Reconhece diretamente starvation por prioridade e aging como mitigação. | Não | Sim | Não | Sim | Polling e bloqueio por E/S são alheios à correção do escalonador descrito. |
| S2D5Q230 | Difícil | Difícil | Simula várias fatias do Round Robin e calcula conclusão e resposta. | Não | Não | Não | Não | — |
| S2D5Q231 | Difícil | Difícil | Contrasta os efeitos de quantum pequeno e grande sobre resposta, preempção e FCFS. | Não | Não | Não | Não | — |
| S2D5Q232 | Difícil | Difícil | Classifica FCFS, SJF, SRTF, prioridade e Round Robin quanto à preempção. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que cobre todos os algoritmos. |
| S2D5Q233 | Difícil | Difícil | Separa hardware controlador de software driver e confere múltiplas responsabilidades. | Não | Não | Não | Não | — |
| S2D5Q234 | Difícil | Médio | Reconhece polling e aplica diretamente a ressalva sobre espera curta ou prolongada. | Não | Não | Sim | Sim | A correta tem quase o dobro da extensão média dos distratores. |
| S2D5Q235 | Difícil | Difícil | Relaciona reconhecimento mínimo, adiamento do trabalho demorado e retorno rápido da ISR. | Não | Não | Sim | Sim | A correta é claramente mais longa e reúne todas as boas práticas. |
| S2D5Q236 | Difícil | Médio | Reconhece diretamente DMA pela transferência em bloco após configuração da controladora. | Não | Sim | Sim | Sim | Journaling e Round Robin são alheios à transferência; a correta é também muito mais longa. |
| S2D5Q237 | Difícil | Difícil | Combina configuração por DMA e interrupção de conclusão sem tratá-las como excludentes. | Não | Não | Sim | Sim | A correta é substancialmente mais longa e a única que compõe os mecanismos. |
| S2D5Q238 | Difícil | Difícil | Associa nome, metadados e referência aberta a diretório, inode e descritor. | Não | Não | Sim | Sim | A correta é muito mais extensa e a única que define as três abstrações. |
| S2D5Q239 | Difícil | Difícil | Diferencia transação sem commit, que é descartada, de transação confirmada, que pode ser repetida. | Não | Não | Não | Não | — |
| S2D5Q240 | Difícil | Difícil | Compara ordered, journal e writeback e aplica a ordem entre dados e commit de metadados. | Não | Não | Sim | Sim | A correta tem cerca do dobro da extensão e concentra toda a semântica exigida. |
| S2D5Q241 | Muito difícil | Médio | Aplica diretamente a distinção entre consistência estrutural por journal e histórico por backup. | Não | Não | Sim | Sim | A correta é muito mais longa e a única que explicita os limites do journaling. |
| S2D5Q242 | Muito difícil | Médio | Converte diretamente cada algarismo de `750` em permissões. | Não | Não | Sim | Sim | A correta é a única descrição completa e supera claramente as demais em extensão. |
| S2D5Q243 | Muito difícil | Difícil | Distingue leitura, travessia e escrita em diretórios e combina permissões para criar ou remover. | Não | Não | Sim | Sim | A correta tem aproximadamente o dobro da extensão dos distratores. |
| S2D5Q244 | Muito difícil | Médio | Associa diretamente `chmod`, `chown` e `getfacl` às três finalidades dadas. | Não | Sim | Não | Sim | Os três distratores são listas de comandos de processos, rede ou armazenamento sem função próxima. |
| S2D5Q245 | Muito difícil | Difícil | Integra DACL, ACE, herança e combinação entre permissões de compartilhamento e NTFS. | Não | Não | Sim | Sim | A correta é substancialmente mais longa e reúne sozinha todos os elementos. |
| S2D5Q246 | Muito difícil | Médio | Recupera diretamente a finalidade de `icacls`. | Não | Sim | Sim | Sim | Processos, CPU e rede são funções alheias; a correta é também muito mais longa. |
| S2D5Q247 | Muito difícil | Médio | Associa diretamente `ps -eLf` à fotografia e `top` ao acompanhamento contínuo. | Não | Sim | Não | Sim | Os distratores misturam ACL, serviços e rede com observação de processos. |
| S2D5Q248 | Muito difícil | Difícil | Mapeia serviço e log em Linux e Windows a quatro comandos pertinentes. | Não | Sim | Sim | Sim | Os distratores combinam alteração, rede e encerramento; a correta é também a opção mais extensa. |
| S2D5Q249 | Muito difícil | Médio | Associa diretamente `ip` à configuração e `ss` aos sockets. | Não | Sim | Não | Sim | Permissões, processos e armazenamento formam trios alheios ao diagnóstico solicitado. |
| S2D5Q250 | Muito difícil | Difícil | Mapeia cinco finalidades administrativas aos comandos Windows correspondentes. | Não | Sim | Não | Sim | Os distratores incluem ordem trocada, comandos destrutivos e conjuntos Linux manifestamente inadequados. |

## Dia 6 — S2D6Q251 a S2D6Q300

| ID | Nível atual | Nível recomendado | Justificativa cognitiva | Ambiguidade | Distrator absurdo/alheio | Pista de comprimento | Reescrita | Observação |
|---|---|---|---|:---:|:---:|:---:|:---:|---|
| S2D6Q251 | Médio | Médio | Distingue diretamente capacidade nominal de taxa útil entregue à aplicação. | Não | Não | Não | Não | — |
| S2D6Q252 | Médio | Médio | Recupera diretamente aprendizagem MAC e separação de colisão por porta. | Não | Não | Sim | Sim | A correta é a alternativa mais longa e a única que combina as duas propriedades. |
| S2D6Q253 | Médio | Médio | Aplica diretamente a troca do quadro a cada enlace roteado. | Não | Não | Não | Não | — |
| S2D6Q254 | Médio | Difícil | Calcula o bloco `/26` e deriva rede e broadcast. | Não | Não | Não | Não | — |
| S2D6Q255 | Médio | Médio | Identifica diretamente o MAC do gateway para destino fora da sub-rede. | Não | Não | Não | Não | — |
| S2D6Q256 | Médio | Médio | Reconhece Neighbor Discovery como mecanismo ICMPv6. | Não | Sim | Sim | Sim | DNS e TCP são alheios à descoberta de vizinhos; a correta é também muito mais longa. |
| S2D6Q257 | Médio | Difícil | Julga três afirmações sobre ordenação, retransmissão e confiabilidade da aplicação. | Não | Não | Não | Não | — |
| S2D6Q258 | Médio | Médio | Associa diretamente HTTP/3 a QUIC sobre UDP. | Não | Sim | Sim | Sim | SMTP é alheio ao transporte Web; a correta tem o dobro da extensão dos distratores. |
| S2D6Q259 | Médio | Médio | Recupera diretamente a expansão da sequência DORA. | Não | Sim | Não | Sim | Os distratores são listas de palavras ou protocolos sem relação funcional com a negociação DHCP. |
| S2D6Q260 | Médio | Médio | Reconhece diretamente a função e os transportes usuais do DNS. | Não | Sim | Sim | Sim | DHCP e TLS recebem funções trocadas; a correta é também claramente mais longa. |
| S2D6Q261 | Médio | Médio | Associa diretamente SMTP ao envio e IMAP à caixa sincronizada. | Não | Sim | Não | Sim | SNMP, LDAP, SFTP e NTP formam pares alheios ao fluxo de correio. |
| S2D6Q262 | Médio | Médio | Reconhece diretamente SFTP como transferência sobre SSH. | Não | Sim | Não | Sim | Protocolo de recebimento de correio é uma função alheia ao contraste entre acesso remoto e transferência segura. |
| S2D6Q263 | Médio | Médio | Recupera diretamente a finalidade de MIB e OID no SNMP. | Não | Sim | Sim | Sim | DNS, DHCP e TLS são alheios ao gerenciamento consultado; a correta é muito mais extensa. |
| S2D6Q264 | Médio | Médio | Distingue diretamente PAT pela tradução adicional de portas. | Não | Sim | Sim | Sim | Cifra e exclusividade de IPv6 são propriedades alheias; a correta é quase duas vezes maior. |
| S2D6Q265 | Médio | Médio | Reconhece NTP pelo sintoma explícito de horários inconsistentes. | Não | Sim | Não | Sim | LDAP, FTP e ARP não são alternativas funcionais próximas para sincronização temporal. |
| S2D6Q266 | Médio | Médio | Recupera diretamente risco como combinação de probabilidade e impacto. | Não | Não | Não | Não | — |
| S2D6Q267 | Médio | Médio | Distingue diretamente prova de identidade de verificação de permissão. | Não | Sim | Sim | Sim | Restore, cifra, hash e IDS são ações alheias à dupla autenticação/autorização; a correta é a mais longa. |
| S2D6Q268 | Médio | Difícil | Distingue falsificação de identidade de interceptação capaz de alterar tráfego. | Não | Não | Sim | Sim | A correta tem quase o dobro da extensão e é a única definição dupla. |
| S2D6Q269 | Médio | Médio | Seleciona diretamente IDS para detecção sem bloqueio necessário. | Não | Sim | Não | Sim | RAID e NAT são controles alheios ao requisito de detectar tráfego suspeito. |
| S2D6Q270 | Médio | Médio | Aplica diretamente DMZ e filtragem estrita ao portal externo. | Não | Não | Sim | Sim | A correta é a única alternativa detalhada e quase duplica a extensão média. |
| S2D6Q271 | Difícil | Médio | Aplica uma única ressalva: VPN não torna o endpoint confiável nem concede toda autorização. | Não | Não | Não | Não | — |
| S2D6Q272 | Difícil | Médio | Reconhece diretamente hash como resumo de integridade não reversível. | Não | Sim | Sim | Sim | Roteamento é alheio à primitiva criptográfica; a correta é também muito mais longa. |
| S2D6Q273 | Difícil | Médio | Recupera diretamente as chaves usadas para assinar e verificar. | Não | Não | Não | Não | — |
| S2D6Q274 | Difícil | Médio | Reconhece diretamente TLS como proteção autenticada do canal. | Não | Sim | Sim | Sim | Substituir DNS e roteamento é função alheia; a correta tem o dobro da extensão média. |
| S2D6Q275 | Difícil | Médio | Recupera diretamente SAE e a permanência de requisitos de configuração e credencial. | Não | Não | Sim | Sim | A correta é muito mais longa que os distratores. |
| S2D6Q276 | Difícil | Médio | Reconhece diretamente contenção como limitação de propagação e impacto. | Não | Não | Sim | Sim | A correta tem aproximadamente o dobro da extensão média. |
| S2D6Q277 | Difícil | Médio | Subtrai diretamente trinta minutos do horário do incidente para aplicar o RPO. | Não | Não | Não | Não | — |
| S2D6Q278 | Difícil | Médio | Distingue diretamente continuidade por redundância de recuperação histórica por backup. | Não | Não | Sim | Sim | A correta tem cerca do dobro da extensão das demais. |
| S2D6Q279 | Difícil | Médio | Reconhece diretamente intercalação concorrente sem simultaneidade. | Não | Não | Sim | Sim | A correta é aproximadamente duas vezes maior que os distratores. |
| S2D6Q280 | Difícil | Médio | Reconhece diretamente condição de corrida pela dependência da intercalação. | Não | Não | Sim | Sim | A correta tem mais que o dobro da extensão média e contém toda a definição. |
| S2D6Q281 | Difícil | Médio | Recupera diretamente exclusão mútua como finalidade do mutex. | Não | Sim | Não | Sim | Escalonamento e mensagens persistentes não são alternativas próximas para a função do mutex. |
| S2D6Q282 | Difícil | Médio | Recupera diretamente que as condições de Coffman precisam coexistir. | Não | Sim | Sim | Sim | A correta é uma palavra curta, enquanto os distratores trazem relações vagas ou alheias. |
| S2D6Q283 | Difícil | Médio | Reconhece diretamente adiamento indefinido com progresso dos demais. | Não | Não | Sim | Sim | A correta é claramente mais longa e a única definição completa. |
| S2D6Q284 | Difícil | Médio | Aplica diretamente o efeito de quantum excessivamente pequeno. | Não | Não | Não | Não | — |
| S2D6Q285 | Difícil | Médio | Contrasta diretamente consulta repetida e sinalização por interrupção. | Não | Sim | Sim | Sim | Cifra de dispositivos é alheia à comparação; a correta é mais que o dobro da extensão média. |
| S2D6Q286 | Difícil | Médio | Reconhece diretamente menor intervenção da CPU na transferência em bloco. | Não | Não | Sim | Sim | A correta é três vezes maior que a extensão média dos distratores. |
| S2D6Q287 | Difícil | Médio | Recupera diretamente journaling como apoio à consistência após falha. | Não | Sim | Sim | Sim | Credenciais e permissões são funções alheias; a correta é também muito mais longa. |
| S2D6Q288 | Difícil | Médio | Converte diretamente os três algarismos de `640` em permissões. | Não | Não | Não | Não | — |
| S2D6Q289 | Difícil | Médio | Reconhece diretamente DACL como conjunto de ACEs de permissão e negação. | Não | Sim | Sim | Sim | CIDR, BGP e NTP são temas alheios; a correta é quase três vezes maior. |
| S2D6Q290 | Difícil | Médio | Aplica uma única ressalva: `ping` não comprova a saúde da aplicação. | Não | Não | Sim | Sim | A correta é claramente mais longa e a única que evita conclusões absolutas. |
| S2D6Q291 | Muito difícil | Médio | Reconhece diretamente o prejuízo de relógios errados à correlação temporal. | Não | Sim | Não | Sim | NTFS, quadros Ethernet e ARP são alheios ao efeito de horário incorreto nos logs. |
| S2D6Q292 | Muito difícil | Médio | Recupera diretamente defesa em profundidade como redução de dependência de uma barreira. | Não | Não | Sim | Sim | A correta é claramente mais longa e a única que formula o princípio. |
| S2D6Q293 | Muito difícil | Difícil | Ordena DHCP, DNS, transporte, TLS e HTTP segundo dependências funcionais. | Não | Sim | Não | Sim | Os distratores são sequências de protocolos sem encadeamento funcional coerente. |
| S2D6Q294 | Muito difícil | Médio | Reconhece diretamente proxy reverso como representante dos servidores publicados. | Não | Sim | Não | Sim | Agentes SNMP são alheios à distinção entre representação de clientes e de servidores. |
| S2D6Q295 | Muito difícil | Médio | Recupera diretamente LDAP como protocolo de acesso a diretórios. | Não | Sim | Não | Sim | NAT, transferência de arquivos e algoritmo criptográfico são funções alheias. |
| S2D6Q296 | Muito difícil | Médio | Aplica diretamente a ressalva de que porta convencional não prova protocolo, validação ou endpoint seguro. | Não | Sim | Sim | Sim | As afirmações sobre HTTPS, TLS e DNS são absurdas; a correta tem mais que o triplo da extensão média. |
| S2D6Q297 | Muito difícil | Médio | Identifica diretamente DDoS como ataque à disponibilidade. | Não | Não | Não | Não | — |
| S2D6Q298 | Muito difícil | Médio | Reconhece diretamente preservação de evidência antes da erradicação. | Não | Sim | Sim | Sim | Desfragmentação é alheia ao objetivo forense; a correta é quase três vezes maior. |
| S2D6Q299 | Muito difícil | Médio | Distingue diretamente o comando de consulta dos três comandos de encerramento. | Não | Não | Não | Não | — |
| S2D6Q300 | Muito difícil | Difícil | Exige validar integridade, dependências e funcionamento de negócio além da restauração técnica. | Não | Não | Sim | Sim | A correta tem mais que o dobro da extensão média e reúne todos os critérios adicionais. |

## Resultado consolidado

| Recorte | Médio atual | Difícil atual | Muito difícil atual | Médio recomendado | Difícil recomendado | Muito difícil recomendado | Mudanças de nível | Reescritas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dia 4 | 20 | 20 | 10 | 14 | 34 | 2 | 19 | 32 |
| Dia 5 | 20 | 20 | 10 | 21 | 29 | 0 | 25 | 24 |
| Dia 6 | 20 | 20 | 10 | 45 | 5 | 0 | 33 | 37 |
| **Total** | **60** | **60** | **30** | **80** | **68** | **2** | **77** | **93** |

### Contagem dos alertas semânticos

| Alerta | Itens |
|---|---:|
| Ambiguidade | 0 |
| Distrator absurdo ou alheio | 36 |
| Pista substantiva de comprimento | 76 |
| Reescrita por ao menos um dos alertas | 93 |
| Apenas ajuste de nível ou preservação | 57 |

### IDs que exigem reescrita

`S2D4Q151, S2D4Q157, S2D4Q158, S2D4Q160, S2D4Q164, S2D4Q165, S2D4Q166, S2D4Q169, S2D4Q172, S2D4Q173, S2D4Q175, S2D4Q179, S2D4Q180, S2D4Q181, S2D4Q182, S2D4Q183, S2D4Q184, S2D4Q185, S2D4Q186, S2D4Q187, S2D4Q188, S2D4Q189, S2D4Q190, S2D4Q192, S2D4Q193, S2D4Q194, S2D4Q195, S2D4Q196, S2D4Q197, S2D4Q198, S2D4Q199, S2D4Q200, S2D5Q205, S2D5Q208, S2D5Q213, S2D5Q214, S2D5Q217, S2D5Q219, S2D5Q229, S2D5Q232, S2D5Q234, S2D5Q235, S2D5Q236, S2D5Q237, S2D5Q238, S2D5Q240, S2D5Q241, S2D5Q242, S2D5Q243, S2D5Q244, S2D5Q245, S2D5Q246, S2D5Q247, S2D5Q248, S2D5Q249, S2D5Q250, S2D6Q252, S2D6Q256, S2D6Q258, S2D6Q259, S2D6Q260, S2D6Q261, S2D6Q262, S2D6Q263, S2D6Q264, S2D6Q265, S2D6Q267, S2D6Q268, S2D6Q269, S2D6Q270, S2D6Q272, S2D6Q274, S2D6Q275, S2D6Q276, S2D6Q278, S2D6Q279, S2D6Q280, S2D6Q281, S2D6Q282, S2D6Q283, S2D6Q285, S2D6Q286, S2D6Q287, S2D6Q289, S2D6Q290, S2D6Q291, S2D6Q292, S2D6Q293, S2D6Q294, S2D6Q295, S2D6Q296, S2D6Q298, S2D6Q300`

## Veredito do recorte

A matriz mecânica `20/20/10` por dia volta a superestimar os itens finais. A distribuição semântica recomendada é `80/68/2`; apenas `S2D4Q161` e `S2D4Q198` sustentam três ou mais filtros independentes no texto atual.

As 77 mudanças de nível podem ser aplicadas como alteração de metadado. Os 93 itens marcados com `Reescrita = Sim` devem ter plausibilidade e equilíbrio visual corrigidos antes de eventual balanceamento de gabarito; permutar letras não elimina as pistas identificadas.
