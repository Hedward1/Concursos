# Apostila de Estudo - Semana 1

## PCPR 2026 - Agente de Polícia Judiciária

**Período planejado:** 27/07/2026 a 01/08/2026  
**Carga:** 6 horas líquidas por dia, sem contar pausas  
**Banca:** Fundação Getulio Vargas - FGV  
**Versão:** 1.0 - material em revisão obrigatória  
**Status:** não aprovado para execução até a auditoria e o aceite do usuário

## Versão do edital utilizada

- **Concurso:** Polícia Civil do Estado do Paraná.
- **Cargo:** Agente de Polícia Judiciária.
- **Banca:** Fundação Getulio Vargas - FGV.
- **Edital:** nº 01/2026, publicado em 06/07/2026.
- **Página oficial:** https://conhecimento.fgv.br/concursos/pcpr26
- **PDF oficial:** https://conhecimento.fgv.br/sites/default/files/concursos/edital-01-2026-pcpr-publicacao.docx-1.pdf
- **Arquivo local:** `Policia Civil PR/edital/edital_pcpr_2026_agente_policia_judiciaria.pdf`.
- **Data da última conferência:** 26/07/2026.
- **Situação observada:** a página oficial apresentava o edital original e a inscrição, sem retificação visível.

Antes de usar esta apostila, confira novamente a página da FGV. Se houver retificação posterior, ela deverá ser analisada antes de alterar conteúdo, datas ou regras.

## Mapa de pontuação e prioridade

| Disciplina | Questões | Participação |
|---|---:|---:|
| Língua Portuguesa | 25 | 25% |
| Raciocínio Lógico-Matemático | 5 | 5% |
| Realidade do Estado do Paraná | 5 | 5% |
| TI, Segurança Cibernética e Crimes Digitais | 25 | 25% |
| Ciências Forenses | 10 | 10% |
| Contabilidade Geral | 5 | 5% |
| Estatística | 5 | 5% |
| Legislação Estadual e Institucional | 5 | 5% |
| Direito Penal | 3 | 3% |
| Direito Processual Penal | 3 | 3% |
| Direito Constitucional | 3 | 3% |
| Direito Administrativo | 3 | 3% |
| Direitos Humanos | 3 | 3% |
| **Total** | **100** | **100%** |

Português e TI somam 50% da prova. Por isso, Português aparece diariamente e os três primeiros dias constroem a base de TI. As disciplinas menores entram cedo em blocos rotativos para não virarem primeiro contato na reta final.

## Como estudar com esta apostila

1. faça o diagnóstico do dia sem consultar a teoria;
2. estude cada seção tentando explicar o conceito com suas palavras;
3. cubra a solução dos exemplos e resolva antes de ler;
4. complete a prática guiada;
5. resolva no máximo dez questões principais e cinco extras na primeira passagem;
6. corrija todas as alternativas, não apenas o gabarito;
7. registre a causa do erro e uma regra curta;
8. programe retorno em D+2, D+7 e D+21.

O banco de 70 questões por dia será modular. Ele não deverá ser esgotado no primeiro contato.

## Matriz de rastreabilidade

| Item do edital | Seção desta apostila | Exemplos | Banco futuro | Fonte principal | Status |
|---|---|---:|---:|---|---|
| Específicos 1.1 | Dia 1 | 22 | 50 principais | edital e documentação técnica oficial | coberto na Semana 1 |
| Específicos 1.2 - sistemas | Dia 2 | 14 | 50 principais | edital e fabricantes | coberto na Semana 1 |
| Específicos 1.2 - aplicativos | Dia 3 | 16 | 50 principais | edital e documentação oficial | coberto na Semana 1 |
| Gerais 1.1 a 1.4 | Dia 4 e blocos diários | 16 | 50 principais e extras | edital e provas FGV | coberto na Semana 1 |
| Gerais 2.1 a 2.4 | Dia 5 e revisões fixas | 12 | 30 principais e extras | edital | cobertura inicial |
| Gerais 3.1 a 3.3 | Dia 5 e revisões fixas | 8 | 20 principais e extras | IBGE, IPARDES e Governo do Paraná | cobertura inicial |
| Específicos 5.2 a 5.5 | Dia 6 e revisões fixas | 16 | 30 principais e extras | legislação oficial vigente | cobertura introdutória |

---

# Dia 1 - Fundamentos de informática

## Objetivo e resultados observáveis

Ao final do dia, você deverá:

- diferenciar hardware, software, firmware e driver;
- explicar o caminho básico entre entrada, processamento, memória, armazenamento e saída;
- comparar RAM, ROM, cache, SSD e HDD;
- escolher uma estratégia básica de backup;
- distinguir BIOS e UEFI;
- diagnosticar casos simples de desempenho, inicialização e dispositivo.

## Por que esse assunto importa

O item 1.1 é a base para Windows, redes, segurança cibernética e evidências digitais. Uma questão pode apresentar um sintoma, como falha após atualização, boot inseguro ou transferência lenta, e exigir a identificação da camada correta.

## Como modelaremos a cobrança FGV

- situações concretas em vez de definições isoladas;
- alternativas com conceitos próximos;
- consequência operacional de uma escolha;
- distinção entre causa, sintoma e solução;
- comparação entre tecnologias sem tratar uma como universalmente melhor.

## Cronograma de 6h líquidas

| Etapa | Tempo | Atividade |
|---|---:|---|
| Tema principal A | 1h15 | hardware, software, CPU, memória e barramentos |
| Tema principal B | 1h15 | periféricos, armazenamento e backup |
| Tema principal C | 45min | BIOS, UEFI, drivers, firmware e contrastes |
| Questões essenciais | 45min | até 10 questões principais, com correção completa |
| Português FGV | 1h | ideia central, informação explícita e inferência |
| Revisão fixa | 40min | proposição, valor lógico e conectivos básicos |
| Caderno de erros | 20min | classificar erro e programar D+2 |

Pausas: 10 a 15 minutos depois dos blocos longos e uma pausa maior entre turnos.

## Diagnóstico sem consulta

Responda em uma frase:

1. Qual é a diferença entre RAM e SSD?
2. Um driver e um firmware ficam necessariamente no mesmo lugar?
3. Sincronizar uma pasta equivale a manter backup histórico?
4. UEFI é apenas outro nome para sistema operacional?
5. Qual componente executa instruções?

Não corrija agora. Retorne depois da teoria.

## Teoria explicada de forma didática

### 1. Hardware e software

**Hardware** é a parte física: processador, memória, placa-mãe, teclado, SSD e interfaces. **Software** é o conjunto de instruções e dados que orienta o hardware.

O software pode ser:

- **de sistema:** sistema operacional, serviços e componentes que administram recursos;
- **aplicativo:** navegador, editor de texto, planilha e sistema policial;
- **utilitário:** ferramenta de diagnóstico, compactação, backup ou proteção.

Um programa não executa sozinho. O sistema operacional carrega suas instruções na memória, a CPU as processa e dispositivos recebem ou produzem dados.

#### Exemplo resolvido 1 - Classificação

**Enunciado:** classifique teclado, Windows 11 e compactador de arquivos.  
**Dados:** teclado é físico; Windows administra recursos; compactador realiza tarefa auxiliar.  
**Raciocínio:** primeiro separe físico de lógico; depois identifique a função do software.  
**Resposta:** teclado é hardware periférico; Windows 11 é software de sistema; compactador é utilitário.  
**Justificativa:** a classificação decorre da natureza e da função.  
**Erro provável:** chamar todo software instalado pelo usuário de aplicativo sem considerar a função utilitária.

#### Exemplo resolvido 2 - Relação entre camadas

**Enunciado:** um editor solicita a impressão de um relatório. Quem produz o conteúdo e quem administra o dispositivo?  
**Dados:** há aplicativo, sistema operacional, driver e impressora.  
**Raciocínio:** o editor gera o trabalho; o sistema e o driver traduzem e encaminham; a impressora materializa.  
**Resposta:** o aplicativo produz o conteúdo; sistema operacional e driver gerenciam a comunicação; a impressora é o hardware de saída.  
**Justificativa:** nenhuma dessas camadas, isoladamente, executa todo o fluxo.  
**Erro provável:** atribuir ao driver a criação do documento.

### 2. CPU, memória, barramentos e entrada/saída

A **CPU** executa instruções. Em visão simplificada:

- a unidade de controle coordena a execução;
- a unidade lógica e aritmética realiza operações;
- registradores guardam temporariamente operandos, endereços e resultados usados diretamente pela CPU;
- a cache reduz o tempo médio de acesso a dados e instruções frequentes.

A execução percorre busca, decodificação e execução de instruções. **Clock** marca ciclos, mas frequência isolada não determina desempenho. **Núcleos** permitem trabalho concorrente quando software e carga podem ser paralelizados. **Pipeline** sobrepõe etapas de instruções diferentes, elevando a vazão; desvios e dependências podem introduzir bolhas ou esperas.

A **memória principal**, normalmente RAM, mantém dados e programas em uso. **Barramentos** e interconexões transportam dados, endereços e sinais de controle. A entrada/saída liga o sistema ao usuário e a outros dispositivos.

Não confunda **capacidade** com **velocidade**. Uma memória maior evita falta de espaço de trabalho, mas não torna todos os processos automaticamente mais rápidos.

#### Exemplo resolvido 3 - Fluxo de processamento

**Enunciado:** ao somar duas células de uma planilha, identifique entrada, processamento e saída.  
**Dados:** valores digitados, fórmula e resultado exibido.  
**Raciocínio:** valores chegam por entrada; CPU executa instruções; o resultado é gravado e exibido.  
**Resposta:** teclado/arquivo fornecem entrada, CPU processa com dados em memória e a tela apresenta a saída.  
**Justificativa:** o fluxo envolve várias partes coordenadas.  
**Erro provável:** dizer que o monitor calcula a fórmula.

#### Exemplo resolvido 4 - Gargalo de memória

**Enunciado:** um computador com pouca RAM passa a usar intensamente armazenamento para manter programas abertos. Qual é o efeito esperado?  
**Dados:** armazenamento secundário costuma ter maior latência que RAM.  
**Raciocínio:** substituir acessos à RAM por acessos ao armazenamento aumenta espera.  
**Resposta:** o sistema tende a ficar mais lento por paginação ou troca frequente.  
**Justificativa:** o problema é a diferença de desempenho entre níveis da hierarquia.  
**Erro provável:** concluir que o SSD se transforma em RAM com as mesmas características.

#### Exemplo complementar D1.1 - Pipeline

**Enunciado:** uma CPU passa a manter simultaneamente instruções em busca, decodificação e execução. O ganho esperado é sempre reduzir o tempo de uma instrução isolada?  
**Dados:** etapas de instruções diferentes são sobrepostas.  
**Raciocínio:** o mecanismo aumenta a quantidade concluída por tempo, mas uma instrução ainda percorre as etapas.  
**Resposta:** não; o ganho principal é de vazão.  
**Justificativa:** dependências e desvios também podem limitar o pipeline.  
**Erro provável:** confundir throughput com latência individual.

#### Exemplo complementar D1.2 - Núcleos e clock

**Enunciado:** um processador com mais núcleos será sempre mais rápido em qualquer programa?  
**Dados:** o benefício depende de paralelismo, arquitetura e carga.  
**Raciocínio:** programa estritamente sequencial pode não usar todos os núcleos.  
**Resposta:** não.  
**Justificativa:** contagem de núcleos é apenas um dos fatores.  
**Erro provável:** escolher especificação isolada como garantia universal.

### 3. Periféricos e dispositivos móveis

Periféricos ampliam entrada, saída, armazenamento ou comunicação:

- **entrada:** teclado, scanner, microfone;
- **saída:** monitor, impressora, alto-falante;
- **entrada e saída:** tela sensível ao toque, interface de rede, dispositivo de armazenamento gravável.

Smartphones e tablets também possuem CPU, memória, armazenamento, sensores, interfaces de rede e sistema operacional. A forma integrada não elimina essas funções.

Em entrada/saída:

- **polling:** a CPU consulta repetidamente o dispositivo;
- **interrupção:** o dispositivo sinaliza quando precisa de atenção;
- **DMA:** um controlador transfere blocos entre dispositivo e memória com menor intervenção direta da CPU.

Esses mecanismos podem coexistir. DMA não elimina controle, configuração ou interrupção de conclusão.

#### Exemplo resolvido 5 - Entrada e saída

**Enunciado:** uma tela sensível ao toque deve ser classificada somente como saída?  
**Dados:** ela exibe imagem e recebe toques.  
**Raciocínio:** a classificação considera todas as funções.  
**Resposta:** não; é dispositivo de entrada e saída.  
**Justificativa:** exibe informação e recebe comandos.  
**Erro provável:** olhar apenas para a função visual.

#### Exemplo resolvido 6 - Sensor móvel

**Enunciado:** um aplicativo registra localização usando GPS. O GPS substitui a CPU?  
**Dados:** sensor fornece dados; CPU executa o aplicativo.  
**Raciocínio:** coletar dado e processá-lo são funções diferentes.  
**Resposta:** não; o sensor é fonte de entrada, enquanto a CPU processa os dados.  
**Justificativa:** o sensor não executa toda a lógica do aplicativo.  
**Erro provável:** tratar qualquer componente eletrônico como processador principal.

#### Exemplo complementar D1.3 - Polling x interrupção

**Enunciado:** a CPU verifica milhares de vezes se um dispositivo lento terminou, permanecendo ocupada nas consultas. Qual mecanismo foi descrito?  
**Dados:** consultas repetidas iniciadas pela CPU.  
**Raciocínio:** não há sinalização espontânea do dispositivo.  
**Resposta:** polling.  
**Justificativa:** a CPU pergunta continuamente pelo estado.  
**Erro provável:** marcar interrupção, na qual o dispositivo sinaliza o evento.

#### Exemplo complementar D1.4 - DMA

**Enunciado:** um bloco grande é transferido do dispositivo para a RAM sem a CPU copiar cada unidade. Qual mecanismo é compatível?  
**Dados:** transferência em bloco com menor intervenção direta.  
**Raciocínio:** um controlador pode assumir a movimentação.  
**Resposta:** DMA.  
**Justificativa:** a CPU configura a operação e pode ser avisada ao final.  
**Erro provável:** afirmar que DMA dispensa completamente a CPU.

### 4. RAM, ROM, cache, SSD e HDD

**RAM** é memória de trabalho, normalmente volátil. Perde o conteúdo quando deixa de receber energia. **ROM** designa memória não volátil voltada à preservação de conteúdo; implementações modernas podem permitir atualização controlada.

**Cache** é pequena e rápida, próxima ou interna à CPU. Explora:

- **localidade temporal:** algo usado agora tende a ser usado novamente;
- **localidade espacial:** dados próximos ao endereço usado tendem a ser acessados.

Em gravação de cache, **write-through** atualiza também o nível inferior a cada escrita; **write-back** registra a alteração na cache e posterga a escrita do bloco modificado. A primeira tende a simplificar consistência ao custo de mais tráfego; a segunda pode reduzir tráfego, mas exige controle de blocos alterados.

**SSD** usa memória flash e não possui partes mecânicas móveis. **HDD** usa discos magnéticos e componentes mecânicos. Em geral, SSD oferece menor latência e maior resistência a impacto, enquanto HDD pode oferecer custo menor por capacidade. A decisão depende do caso.

Mídias removíveis, como unidade USB, cartão e disco externo, facilitam transporte, mas elevam riscos de perda, conexão não autorizada e código malicioso. Armazenamento em nuvem depende de serviço remoto, rede, conta e política de acesso; ele não é automaticamente público nem automaticamente um backup.

Um **bit** assume 0 ou 1. Um **byte** reúne 8 bits. Em provas, observe se o enunciado usa prefixos decimais ou binários; não misture `b` de bit com `B` de byte.

#### Exemplo resolvido 7 - Volatilidade

**Enunciado:** um relatório não salvo desaparece após queda de energia, embora o SSD esteja intacto. Onde estavam as alterações?  
**Dados:** documento aberto e ainda não persistido.  
**Raciocínio:** alterações em uso podem estar apenas na memória volátil.  
**Resposta:** provavelmente estavam na RAM e ainda não haviam sido gravadas no SSD.  
**Justificativa:** persistência exige operação de gravação.  
**Erro provável:** concluir que possuir SSD salva automaticamente todo dado em edição.

#### Exemplo resolvido 8 - Cache e localidade

**Enunciado:** um laço percorre posições consecutivas de um vetor. Qual localidade favorece a cache?  
**Dados:** acessos a endereços próximos e sequenciais.  
**Raciocínio:** blocos próximos costumam ser trazidos juntos.  
**Resposta:** localidade espacial.  
**Justificativa:** após acessar uma posição, as vizinhas têm alta chance de uso.  
**Erro provável:** marcar temporal apenas porque os acessos ocorrem em curto intervalo.

#### Exemplo complementar D1.5 - Bits e bytes

**Enunciado:** quantos bits existem em 4 bytes?  
**Dados:** 1 byte = 8 bits.  
**Raciocínio:** `4 × 8`.  
**Resposta:** 32 bits.  
**Justificativa:** a conversão usa oito bits por byte.  
**Erro provável:** inverter e dividir por oito.

#### Exemplo complementar D1.6 - Taxa em bits

**Enunciado:** ignorando overhead, uma taxa de 80 megabits por segundo corresponde a quantos megabytes por segundo?  
**Dados:** 8 bits = 1 byte.  
**Raciocínio:** `80/8`.  
**Resposta:** 10 megabytes por segundo.  
**Justificativa:** a letra minúscula `b` representa bits; maiúscula `B`, bytes.  
**Erro provável:** responder 80 por ignorar a unidade.
### 5. Backup, cópia e sincronização

**Backup** é uma cópia planejada para recuperação, com escopo, periodicidade, retenção e teste. Uma cópia isolada pode ajudar, mas não constitui estratégia completa.

- **completo:** copia todo o conjunto selecionado;
- **incremental:** copia mudanças desde o último backup de qualquer tipo;
- **diferencial:** copia mudanças desde o último completo.

Incrementais costumam reduzir janela e espaço por execução, mas a restauração pode depender de uma cadeia maior. Diferenciais crescem até o próximo completo, porém simplificam a cadeia de restauração.

**Sincronização** replica o estado atual. Exclusão ou corrupção pode ser propagada. Versionamento e retenção podem tornar um serviço mais útil para recuperação, mas isso deve ser confirmado.

A regra 3-2-1 é uma referência prática: três cópias dos dados, em dois tipos de mídia, com uma cópia fora do ambiente principal. Ela não substitui análise de risco.

#### Exemplo resolvido 9 - Incremental x diferencial

**Enunciado:** houve backup completo no domingo. Na segunda e terça ocorreram alterações. O incremental de terça copia o quê? E o diferencial?  
**Dados:** último completo domingo; incremental anterior segunda.  
**Raciocínio:** incremental olha para o último backup; diferencial olha para o último completo.  
**Resposta:** o incremental de terça copia as mudanças desde segunda; o diferencial copia as mudanças acumuladas desde domingo.  
**Justificativa:** as referências temporais são diferentes.  
**Erro provável:** inverter os conceitos porque "diferencial" parece significar somente a diferença do dia.

#### Exemplo resolvido 10 - Sincronização não basta

**Enunciado:** uma pasta sincronizada sofre exclusão acidental, propagada a todos os dispositivos. Havia backup garantido?  
**Dados:** apenas sincronização, sem retenção confirmada.  
**Raciocínio:** replicar estado não assegura ponto histórico recuperável.  
**Resposta:** não é possível afirmar; sem versionamento ou retenção, a exclusão pode atingir todas as réplicas.  
**Justificativa:** backup exige capacidade de recuperação.  
**Erro provável:** tratar qualquer cópia em nuvem como backup completo.

### 6. BIOS, UEFI, POST e boot

BIOS e UEFI são interfaces de firmware que participam da inicialização do computador.

- **POST:** verificações iniciais de hardware;
- **boot:** processo que localiza e carrega o sistema operacional;
- **BIOS legado:** modelo mais antigo;
- **UEFI:** arquitetura mais moderna, com recursos como suporte a GPT e Secure Boot.

**Secure Boot** verifica a confiança dos componentes de inicialização. Ele não substitui antivírus, atualização ou criptografia de dados.

#### Exemplo resolvido 11 - Ordem de boot

**Enunciado:** um computador tenta iniciar por mídia USB antes do disco interno. Qual configuração é relevante?  
**Dados:** há mais de um dispositivo inicializável.  
**Raciocínio:** o firmware consulta uma ordem de inicialização.  
**Resposta:** a ordem de boot configurada em BIOS/UEFI.  
**Justificativa:** ela define a prioridade dos dispositivos.  
**Erro provável:** procurar a solução apenas no editor de texto ou em aplicativo comum.

#### Exemplo resolvido 12 - Secure Boot

**Enunciado:** habilitar Secure Boot criptografa automaticamente todos os arquivos?  
**Dados:** Secure Boot valida componentes do processo de inicialização.  
**Raciocínio:** integridade do boot e confidencialidade dos arquivos são objetivos distintos.  
**Resposta:** não.  
**Justificativa:** criptografia de volume depende de recurso próprio, como BitLocker ou equivalente.  
**Erro provável:** associar qualquer recurso "secure" a todas as propriedades de segurança.

### 7. Drivers e firmware

**Driver** permite que o sistema operacional controle um dispositivo. **Firmware** é software de baixo nível associado ao próprio equipamento, armazenado em memória não volátil.

Ambos podem ser atualizados, mas com riscos distintos. Atualização interrompida de firmware pode deixar o dispositivo inoperante; driver incompatível pode impedir o funcionamento no sistema.

#### Exemplo resolvido 13 - Driver

**Enunciado:** após instalar o sistema, a placa de rede é detectada como dispositivo desconhecido. Qual camada deve ser verificada primeiro?  
**Dados:** hardware presente, mas sem controle adequado pelo sistema.  
**Raciocínio:** o sistema precisa do software de comunicação específico.  
**Resposta:** o driver da placa de rede.  
**Justificativa:** o sintoma indica falta ou incompatibilidade de driver.  
**Erro provável:** atualizar firmware sem evidência de problema no equipamento.

#### Exemplo resolvido 14 - Firmware

**Enunciado:** um fabricante corrige, por atualização do próprio SSD, um defeito interno de gerenciamento. Isso é driver?  
**Dados:** correção é gravada no dispositivo.  
**Raciocínio:** software persistente interno ao equipamento é firmware.  
**Resposta:** não; trata-se de firmware.  
**Justificativa:** a correção opera no controlador do SSD.  
**Erro provável:** chamar de driver toda atualização ligada a hardware.

### 8. Capacidade, latência, vazão e confiabilidade

- **capacidade:** quanto pode ser armazenado;
- **latência:** tempo para iniciar ou concluir uma resposta individual;
- **vazão ou throughput:** quantidade processada por unidade de tempo;
- **confiabilidade:** probabilidade de funcionamento correto ao longo do tempo;
- **disponibilidade:** proporção do tempo em que o serviço está utilizável.

Melhorar vazão não garante menor latência individual. Um sistema pode processar muitos pedidos por minuto e ainda fazer cada pedido esperar.

#### Exemplo resolvido 15 - Latência x vazão

**Enunciado:** dois scanners processam 60 páginas por minuto. Um inicia a primeira página em 2 segundos e outro em 8. A vazão é igual? A latência inicial é igual?  
**Dados:** mesma produção por minuto, tempos iniciais diferentes.  
**Raciocínio:** compare quantidade por tempo e espera individual.  
**Resposta:** a vazão informada é igual; a latência inicial é menor no primeiro.  
**Justificativa:** as métricas medem aspectos diferentes.  
**Erro provável:** concluir que mesma vazão implica mesma resposta individual.

#### Exemplo resolvido 16 - Capacidade x desempenho

**Enunciado:** trocar um HDD de 2 TB por SSD de 1 TB aumenta capacidade?  
**Dados:** 2 TB contra 1 TB; tecnologias diferentes.  
**Raciocínio:** compare capacidade separadamente do desempenho.  
**Resposta:** não; a capacidade cai, embora o desempenho possa melhorar.  
**Justificativa:** tecnologia mais rápida não significa espaço maior.  
**Erro provável:** usar "melhor" sem indicar qual critério.

## Como o conteúdo funciona na prática

Quando surgir um problema, siga quatro perguntas:

1. **Qual é o sintoma?** Lentidão, falha de boot, dispositivo ausente ou perda de dado?
2. **Em qual camada?** Hardware, firmware, driver, sistema ou aplicativo?
3. **Qual métrica foi afetada?** Capacidade, latência, vazão, disponibilidade ou integridade?
4. **Qual ação é proporcional?** Configurar, atualizar, testar, restaurar ou substituir?

Evite começar pela ação mais invasiva. Diagnóstico antecede alteração.

## Diferenças entre conceitos próximos

| Conceito A | Conceito B | Diferença decisiva |
|---|---|---|
| RAM | SSD/HDD | memória de trabalho volátil x armazenamento persistente |
| ROM | RAM | preservação sem energia x conteúdo de trabalho volátil |
| cache | armazenamento | redução de tempo de acesso x persistência e capacidade |
| backup | sincronização | recuperação histórica planejada x replicação de estado |
| incremental | diferencial | desde o último backup x desde o último completo |
| BIOS | UEFI | arquitetura legada x arquitetura moderna de firmware |
| driver | firmware | controle pelo sistema x software interno do dispositivo |
| latência | vazão | espera por operação x volume por unidade de tempo |

## Prática guiada

### Caso 1 - Delegacia com janela curta

Há 2 TB de dados. No domingo cabe um backup completo. Nos dias úteis, a janela é curta. Uma solução possível é completo semanal mais incrementais diários. A restauração de sexta exigirá o completo e os incrementais posteriores. Se a prioridade for reduzir a cadeia de restauração, diferenciais podem ser considerados, aceitando crescimento diário.

### Caso 2 - Dispositivo após reinstalação

Se a câmera funciona em outro computador, mas aparece desconhecida após reinstalação do Windows, verifique identificação, driver oficial e compatibilidade. Firmware só entra após evidência ou orientação do fabricante.

### Caso 3 - Inicialização insegura

Secure Boot desabilitado não prova infecção. Ele indica ausência daquele controle. A resposta correta combina verificação de configuração, compatibilidade e política institucional, sem prometer proteção absoluta.

## Pegadinhas do Dia 1

- hardware não executa utilmente sem software, e software precisa de hardware;
- cache não substitui RAM, SSD nem unidade lógica e aritmética;
- pipeline melhora principalmente a vazão e pode sofrer com dependências e desvios;
- mais clock ou mais núcleos, isoladamente, não garantem melhor desempenho;
- polling consulta repetidamente; interrupção sinaliza; DMA transfere blocos;
- DMA reduz intervenção direta, mas não elimina participação da CPU;
- mais capacidade não significa menor latência;
- RAM é normalmente volátil; ROM preserva conteúdo sem energia;
- sincronização pode propagar exclusão;
- incremental e diferencial usam referências temporais diferentes;
- UEFI não é sistema operacional;
- Secure Boot não criptografa arquivos;
- driver não é o mesmo que firmware;
- `b` e `B` não representam a mesma unidade;
- dispositivo de entrada e saída não precisa pertencer a uma única categoria.

## O que memorizar

- CPU executa; RAM mantém o trabalho; armazenamento persiste.
- Pipeline sobrepõe etapas; seu ganho principal é de throughput.
- Polling, interrupção e DMA organizam a comunicação de E/S de modos diferentes.
- 1 byte = 8 bits.
- Driver liga sistema e dispositivo; firmware opera dentro do equipamento.
- Backup precisa ser recuperável e testado.
- Incremental: desde o último backup. Diferencial: desde o último completo.
- UEFI é firmware moderno; Secure Boot protege a cadeia de inicialização.
- Latência mede espera; vazão mede volume por tempo.

## Erros comuns

| Erro | Correção |
|---|---|
| chamar SSD de memória RAM | ambos armazenam bits, mas têm função, persistência e desempenho distintos |
| considerar nuvem sinônimo de backup | confirme versionamento, retenção e restauração |
| trocar driver por firmware | pergunte onde o software atua e onde é armazenado |
| escolher tecnologia "melhor" sem critério | compare capacidade, latência, custo, risco e uso |
| atribuir segurança absoluta a um controle | controles reduzem riscos específicos |

## Tabela de revisão rápida

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| CPU | executa instruções | confundir com armazenamento | calcula uma fórmula |
| pipeline | sobrepõe etapas | garantir menor latência individual | várias instruções em estágios |
| polling | consulta repetida pela CPU | confundir com sinal do dispositivo | verificar estado em laço |
| DMA | transfere blocos com menor intervenção | dizer que elimina a CPU | dispositivo para RAM |
| RAM | memória de trabalho volátil | chamar de permanente | mantém documento aberto |
| cache | memória rápida por localidade | dizer que substitui RAM | reutiliza bloco frequente |
| SSD | armazenamento flash | dizer que sempre tem mais capacidade | inicialização rápida |
| backup | cópia para recuperação | confundir com sincronização | restaurar versão anterior |
| UEFI | firmware moderno de boot | chamar de SO | escolhe carregador confiável |
| driver | controle de dispositivo pelo SO | confundir com firmware | driver de rede |
| throughput | volume por tempo | confundir com latência | páginas por minuto |
| bit/byte | bit é unidade binária; byte reúne 8 bits | ignorar `b` x `B` | 80 Mb/s = 10 MB/s |

## Mini revisão do dia

Explique sem consultar:

1. o fluxo entrada-processamento-saída;
2. a diferença entre memória volátil e armazenamento persistente;
3. por que sincronização não garante recuperação;
4. como BIOS/UEFI participa do boot;
5. por que driver e firmware não são sinônimos.

## 5 perguntas de fixação

1. Por que aumentar a RAM pode reduzir paginação, mas não aumenta a capacidade do SSD?
2. Quando um backup diferencial pode facilitar a restauração em relação ao incremental?
3. Qual é a função do Secure Boot e qual proteção ele não oferece?
4. Como você distinguiria falha de driver de falha física?
5. Dê um exemplo em que a vazão aumenta sem reduzir a latência individual.

## Checklist de domínio

- [ ] Classifico hardware, software de sistema, aplicativo e utilitário.
- [ ] Explico CPU, ciclo de instrução, pipeline, registradores, RAM e cache.
- [ ] Distingo entrada, saída, polling, interrupção e DMA.
- [ ] Comparo RAM, ROM, SSD e HDD.
- [ ] Distingo completo, incremental e diferencial.
- [ ] Explico por que sincronização não basta.
- [ ] Distingo BIOS, UEFI, boot e Secure Boot.
- [ ] Distingo driver e firmware.
- [ ] Converto bits e bytes e comparo capacidade, latência e vazão.
- [ ] Resolvo os exemplos sem consultar.

## Tarefa para o caderno de erros

Crie quatro cartões:

1. `conceito confundido`;
2. `palavra decisiva do enunciado`;
3. `regra correta em até duas linhas`;
4. `novo exemplo criado por mim`.

Programe D+2 para rever backup, driver/firmware e latência/vazão.

## Questões associadas

Na futura `semana_01_questoes.md`:

- Dia 1, Questões principais 1 a 50;
- Extras do Dia 1, 10 de Português e 10 de RLM;
- primeira passagem recomendada: 10 principais e 5 extras essenciais.

## Fontes do Dia 1

- edital PCPR nº 01/2026, Conhecimentos Específicos, item 1.1;
- Microsoft, requisitos do Windows 11 e UEFI/Secure Boot: https://support.microsoft.com/pt-BR/Windows/Experience/Compatibility/windows-11-system-requirements
- documentação dos fabricantes para firmware, drivers e dispositivos;
- conceitos gerais de arquitetura e armazenamento, confrontados com documentação técnica oficial.

---

# Dia 2 - Windows 11, Android e iOS

## Objetivo e resultados observáveis

Ao final do dia, você deverá:

- administrar arquivos, contas e aplicativos em nível de prova;
- distinguir usuário padrão, administrador, autenticação e autorização;
- explicar atualização, restauração, redefinição e recuperação;
- reconhecer a finalidade de UAC, Defender, firewall, criptografia e bloqueio de tela;
- avaliar permissões de aplicativos;
- comparar Windows 11, Android e iOS sem atribuir recurso ao sistema errado.

## Por que esse assunto importa

O edital cita expressamente Windows 11, Android e iOS. A FGV pode descrever uma situação de uso e cobrar o efeito de uma configuração, a medida de segurança adequada ou a diferença entre atualizar, restaurar e redefinir.

## Como modelaremos a cobrança FGV

- casos de conta, permissão e aplicativo;
- efeito prático de uma configuração;
- atualização do sistema x atualização de aplicativo;
- recurso correto associado ao sistema errado;
- medida proporcional a perda, roubo ou falha;
- alternativa quase correta, mas absoluta ou incompleta.

## Cronograma de 6h líquidas

| Etapa | Tempo | Atividade |
|---|---:|---|
| Tema principal A | 1h15 | Windows 11: arquivos, contas, aplicativos e atualização |
| Tema principal B | 1h15 | segurança do Windows, Android e iOS |
| Tema principal C | 45min | backup, restauração, redefinição e contrastes |
| Questões essenciais | 45min | até 10 principais, com correção A-E |
| Português FGV | 1h | coesão referencial e progressão |
| Revisão fixa | 40min | formação territorial e localização do Paraná |
| Caderno de erros | 20min | recurso, sistema, efeito e causa |

## Diagnóstico sem consulta

1. Administrador e usuário autenticado são sinônimos?
2. Atualização de aplicativo substitui atualização do sistema?
3. UAC impede toda execução maliciosa?
4. Redefinir um smartphone pode apagar dados?
5. Permissão para câmera autoriza acesso a localização?

## Teoria explicada de forma didática

### 1. Arquivos, pastas, extensões e atalhos no Windows 11

O sistema de arquivos organiza dados em arquivos e diretórios. A **extensão** ajuda a indicar formato e associação de aplicativo, mas não garante que o conteúdo seja seguro ou corresponda ao nome.

Um **atalho** aponta para um recurso; apagar o atalho normalmente não apaga o arquivo original. Copiar cria outro item; mover altera sua localização. Na mesma unidade, mover pode envolver apenas atualização de referências; entre unidades, pode exigir cópia e remoção.

Exibir extensões e verificar propriedades ajuda a evitar arquivos com nomes enganosos. Um nome como `relatorio.pdf.exe` pode ser percebido incorretamente se a extensão conhecida estiver oculta.

#### Exemplo resolvido 17 - Atalho

**Enunciado:** o atalho de um sistema foi apagado da área de trabalho. O executável foi necessariamente excluído?  
**Dados:** foi removido apenas o arquivo de atalho.  
**Raciocínio:** atalho contém referência ao destino.  
**Resposta:** não; em regra, o destino permanece.  
**Justificativa:** remover a referência não equivale a remover o objeto apontado.  
**Erro provável:** confundir representação com conteúdo.

#### Exemplo resolvido 18 - Extensão oculta

**Enunciado:** um anexo aparece como `depoimento.pdf`, mas suas propriedades mostram tipo executável. Qual informação é decisiva?  
**Dados:** aparência do nome diverge do tipo real.  
**Raciocínio:** nome visível pode ocultar extensão ou ser manipulado.  
**Resposta:** o tipo e a extensão efetiva devem ser verificados antes da execução.  
**Justificativa:** a aparência não comprova o formato.  
**Erro provável:** confiar apenas no ícone ou no trecho anterior ao último ponto.

### 2. Contas, perfis e privilégios

**Autenticação** responde "quem é você?". **Autorização** responde "o que você pode fazer?". Uma conta pode ser autenticada e continuar sem permissão administrativa.

- **usuário padrão:** apropriado para uso cotidiano e menor impacto de alterações;
- **administrador:** pode realizar mudanças de maior alcance;
- **conta local:** identidade gerida no próprio computador;
- **conta Microsoft:** identidade vinculada aos serviços Microsoft e a recursos de sincronização.

O **princípio do menor privilégio** concede apenas os acessos necessários. Ele reduz o impacto de erro ou comprometimento, mas não elimina a necessidade de atualização, monitoramento e proteção.

#### Exemplo resolvido 19 - Autenticação x autorização

**Enunciado:** um servidor entra no Windows com senha correta, mas não consegue instalar um driver. Houve falha de autenticação?  
**Dados:** login aceito; ação administrativa negada.  
**Raciocínio:** identidade foi reconhecida; permissão é insuficiente.  
**Resposta:** não; o problema é de autorização ou privilégio.  
**Justificativa:** autenticação já ocorreu com sucesso.  
**Erro provável:** chamar qualquer bloqueio de "falha de login".

#### Exemplo resolvido 20 - Menor privilégio

**Enunciado:** um computador de consulta não exige instalação rotineira. Qual perfil reduz risco: padrão ou administrador?  
**Dados:** tarefas diárias não precisam de alteração administrativa.  
**Raciocínio:** conceda somente o necessário.  
**Resposta:** usuário padrão.  
**Justificativa:** limita mudanças de sistema e o impacto de execução indevida.  
**Erro provável:** dizer que administrador é sempre melhor por possuir mais recursos.

### 3. Instalação, aplicativos, drivers e Windows Update

Instalar um sistema ou aplicativo altera arquivos, configurações e, às vezes, serviços. Fontes oficiais, assinatura digital, compatibilidade e privilégio devem ser avaliados.

No Windows:

- atualizações de **qualidade** tendem a trazer correções e segurança;
- atualizações de **recurso** introduzem mudanças funcionais mais amplas;
- drivers podem chegar pelo fabricante ou por mecanismos administrados;
- reinicialização pode ser necessária para concluir substituição de componentes.

Atualizar reduz vulnerabilidades conhecidas, mas não torna o sistema invulnerável.

#### Exemplo resolvido 21 - Atualização incompleta

**Enunciado:** uma correção foi baixada, mas o sistema informa reinicialização pendente. A proteção está necessariamente concluída?  
**Dados:** instalação depende de reinício.  
**Raciocínio:** baixar e ativar são etapas distintas.  
**Resposta:** não; a atualização pode só entrar plenamente em vigor após o reinício.  
**Justificativa:** componentes em uso precisam ser substituídos no ciclo de inicialização.  
**Erro provável:** equiparar download a instalação concluída.

#### Exemplo resolvido 22 - Fonte do aplicativo

**Enunciado:** duas páginas oferecem o mesmo instalador; uma é do fornecedor e a outra é desconhecida. Qual decisão é mais segura?  
**Dados:** mesma promessa, origens diferentes.  
**Raciocínio:** origem, assinatura e integridade reduzem risco de adulteração.  
**Resposta:** obter da fonte oficial e verificar os indicadores disponíveis.  
**Justificativa:** o nome do arquivo não prova autenticidade.  
**Erro provável:** considerar arquivos iguais apenas porque possuem o mesmo nome.

### 4. Segurança do Windows 11

Controles importantes:

- **UAC:** solicita consentimento ou credenciais para elevação de privilégio;
- **Microsoft Defender Antivirus:** identifica e trata ameaças segundo mecanismos e políticas;
- **Firewall:** controla tráfego de rede segundo regras;
- **BitLocker ou criptografia de dispositivo:** protege dados armazenados, conforme edição, hardware e configuração;
- **Secure Boot:** protege a cadeia de inicialização;
- **Windows Hello:** mecanismos de autenticação associados ao dispositivo.

Cada controle cobre um risco. Firewall não substitui antivírus; criptografia não impede exclusão; UAC não garante que o usuário negará uma solicitação maliciosa.

#### Exemplo resolvido 23 - Controles complementares

**Enunciado:** um notebook usa criptografia de volume, mas não possui backup. A perda física do disco e a exclusão acidental estão igualmente tratadas?  
**Dados:** confidencialidade em repouso, ausência de cópia recuperável.  
**Raciocínio:** criptografia protege acesso indevido; backup protege recuperação.  
**Resposta:** não; a confidencialidade foi reforçada, mas a recuperação continua pendente.  
**Justificativa:** controles atendem objetivos diferentes.  
**Erro provável:** tratar criptografia como proteção universal.

#### Exemplo resolvido 24 - UAC

**Enunciado:** uma instalação solicita elevação. Aceitar a solicitação confirma que o programa é seguro?  
**Dados:** UAC pede consentimento para privilégio elevado.  
**Raciocínio:** consentimento autoriza a ação, mas não atesta benignidade.  
**Resposta:** não.  
**Justificativa:** ainda é necessário verificar origem, assinatura e necessidade.  
**Erro provável:** interpretar a janela do UAC como certificado de segurança.

### 5. Android: aplicativos, permissões, atualização e backup

No Android, aplicativos são executados com isolamento e permissões. O usuário deve avaliar se a permissão é coerente com a função. Algumas podem ser concedidas apenas durante o uso.

É importante distinguir:

- versão do Android;
- atualização de segurança;
- atualização do sistema Google Play;
- atualização individual de aplicativo.

O calendário depende de fabricante, modelo e operadora. Backup pode incluir dados e configurações, mas o escopo varia. Restaurar backup de versão posterior em versão anterior pode não ser possível.

#### Exemplo resolvido 25 - Permissão excessiva

**Enunciado:** um aplicativo de lanterna solicita contatos e microfone sem função declarada. Qual análise é adequada?  
**Dados:** permissões não parecem necessárias ao objetivo.  
**Raciocínio:** menor privilégio também vale para apps.  
**Resposta:** negar ou revisar as permissões e avaliar a legitimidade do aplicativo.  
**Justificativa:** a solicitação amplia exposição sem justificativa funcional evidente.  
**Erro provável:** aceitar porque o aplicativo está instalado em loja.

#### Exemplo resolvido 26 - Tipos de atualização

**Enunciado:** atualizar somente um mensageiro garante que o Android recebeu o patch mais recente?  
**Dados:** aplicativo e sistema têm ciclos distintos.  
**Raciocínio:** atualização do app não altera necessariamente o sistema.  
**Resposta:** não.  
**Justificativa:** deve-se verificar versão do Android, patch de segurança e sistema Google Play.  
**Erro provável:** tratar todo botão "Atualizar" como a mesma camada.

### 6. iOS: aplicativos, permissões, atualização e proteção

No iOS, permissões também são concedidas por categoria, como câmera, microfone, localização, fotos e contatos. Atualizações podem incluir sistema, correções e arquivos de segurança.

Backup pode ser realizado em serviço de nuvem ou computador, conforme configuração. Bloqueio de tela, autenticação da conta e proteção do dispositivo atuam de forma complementar. Manter software atualizado é medida central, mas não autoriza abrir links ou fornecer credenciais sem análise.

#### Exemplo resolvido 27 - Atualizar com segurança

**Enunciado:** antes de uma atualização relevante, qual preparação reduz risco de perda?  
**Dados:** dispositivo contém dados importantes.  
**Raciocínio:** atualização e recuperação devem ser planejadas.  
**Resposta:** confirmar backup recente, energia e conexão adequadas antes de atualizar pela via oficial.  
**Justificativa:** isso reduz interrupção e permite recuperação conforme o caso.  
**Erro provável:** confundir recomendação de backup com afirmação de que toda atualização apaga dados.

#### Exemplo resolvido 28 - Permissão por categoria

**Enunciado:** conceder acesso à câmera autoriza automaticamente o aplicativo a ler todos os contatos?  
**Dados:** permissões são categorias distintas.  
**Raciocínio:** uma autorização não se estende sem base a outra.  
**Resposta:** não.  
**Justificativa:** contatos exigem permissão própria.  
**Erro provável:** imaginar uma permissão única e global.

### 7. Restaurar, redefinir e recuperar

**Atualizar** instala nova versão ou correção. **Restaurar** pode recuperar arquivos, configurações ou estado anterior, conforme o recurso. **Redefinir** retorna configurações ou dispositivo a um estado inicial e pode apagar dados. **Reinstalar** grava novamente o sistema.

Antes de qualquer ação destrutiva:

1. identifique o objetivo;
2. confirme o backup;
3. verifique credenciais;
4. registre configurações;
5. use procedimento oficial.

#### Exemplo resolvido 29 - Redefinição

**Enunciado:** um smartphone será redefinido para configuração de fábrica. Qual é o pressuposto seguro?  
**Dados:** a operação pode apagar dados locais.  
**Raciocínio:** não se presume recuperação sem backup confirmado.  
**Resposta:** revisar backup, conta e credenciais antes da redefinição.  
**Justificativa:** a redefinição é potencialmente destrutiva.  
**Erro provável:** acreditar que sincronização parcial cobre todo conteúdo.

#### Exemplo resolvido 30 - Atualização x reinstalação

**Enunciado:** instalar um patch mensal equivale a reinstalar completamente o Windows?  
**Dados:** patch altera componentes específicos; reinstalação recompõe o sistema.  
**Raciocínio:** compare escopo.  
**Resposta:** não.  
**Justificativa:** são operações distintas, embora ambas alterem software do sistema.  
**Erro provável:** usar "instalar" como se todas as instalações tivessem o mesmo alcance.

## Como o conteúdo funciona na prática

Use a sequência:

1. identifique dispositivo, sistema e versão;
2. determine se o caso envolve identidade, privilégio, arquivo, aplicativo ou atualização;
3. verifique o estado antes de alterar;
4. proteja possibilidade de recuperação;
5. aplique a menor mudança suficiente;
6. valide o resultado e registre.

## Diferenças entre conceitos próximos

| Conceito A | Conceito B | Diferença decisiva |
|---|---|---|
| autenticação | autorização | comprovar identidade x definir ações permitidas |
| usuário padrão | administrador | privilégios limitados x alterações amplas |
| conta local | conta em nuvem | identidade do dispositivo x identidade vinculada a serviço |
| atualizar | reinstalar | corrigir/evoluir componentes x gravar novamente o sistema |
| restaurar | redefinir | recuperar estado/dado x voltar a estado inicial |
| antivírus | firewall | conteúdo/processo malicioso x tráfego de rede |
| criptografia | backup | confidencialidade x recuperação |
| permissão do app | privilégio da conta | acesso do aplicativo x poder do usuário |

## Prática guiada

### Caso 1 - Conta compartilhada

Não use uma única conta administrativa para todos. Separe identidades, use privilégios compatíveis e mantenha rastreabilidade. A solução não é apenas "colocar senha", pois uma senha compartilhada não identifica o autor.

### Caso 2 - Aplicativo com acesso excessivo

Liste função declarada, permissões pedidas e dados acessíveis. Negue o que não for necessário, valide a origem e remova o aplicativo se o risco não for justificável.

### Caso 3 - Dispositivo perdido

Considere bloqueio de tela, conta, possibilidade de localização/bloqueio remoto, troca de credenciais quando indicada, comunicação institucional e exposição dos dados. Criptografia reduz risco de leitura, mas não substitui resposta ao incidente.

## Pegadinhas do Dia 2

- login bem-sucedido não concede privilégio administrativo;
- UAC pede elevação, mas não garante segurança do programa;
- firewall e antivírus são complementares;
- criptografia não é backup;
- atualizar aplicativo não atualiza necessariamente o sistema;
- redefinição pode apagar dados;
- atalho não é o arquivo original;
- extensão aparente não comprova o conteúdo;
- uma permissão não autoriza automaticamente outra;
- interface e nomes podem variar por versão; a função é o núcleo da questão.

## O que memorizar

- autenticação: identidade; autorização: permissão;
- menor privilégio reduz impacto;
- atualização, restauração, redefinição e reinstalação não são sinônimos;
- segurança é combinação de controles;
- permissões devem ser compatíveis com a finalidade;
- backup deve ser confirmado antes de ação destrutiva.

## Erros comuns

| Erro | Correção |
|---|---|
| aceitar toda elevação UAC | verificar origem, necessidade e assinatura |
| usar administrador diariamente | preferir padrão quando a tarefa permitir |
| dizer que Android atualiza igual em todos os aparelhos | cronograma varia por fabricante, modelo e operadora |
| presumir que iOS/Android salvam tudo na nuvem | verificar escopo e data do backup |
| decorar caminho de menu como regra eterna | estudar função, efeito e pré-condição |

## Tabela de revisão rápida

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| autenticação | valida identidade | confundir com permissão | login aceito |
| autorização | permite ação | chamar de login | instalar driver |
| UAC | controla elevação | tratar como antivírus | pedido de consentimento |
| firewall | aplica regra de tráfego | dizer que elimina malware | bloquear conexão |
| atualização | corrige ou evolui software | confundir com reinstalação | patch mensal |
| redefinição | retorna a estado inicial | presumir preservação | fábrica no smartphone |
| permissão | acesso concedido ao app | considerar global | câmera sem contatos |
| backup | dado recuperável | presumir por existir conta | restauração após perda |

## Mini revisão do dia

1. explique autenticação e autorização;
2. dê um exemplo de controles complementares;
3. compare atualização e redefinição;
4. explique por que a permissão deve ser proporcional;
5. descreva preparação antes de restaurar ou redefinir.

## 5 perguntas de fixação

1. Por que um usuário autenticado pode não conseguir instalar um aplicativo?
2. Qual é a diferença entre proteção de boot e criptografia de dados?
3. Como verificar se um Android está atualizado em mais de uma camada?
4. Por que aceitar uma solicitação UAC não prova a segurança do programa?
5. Quais dados você confirmaria antes de redefinir um dispositivo?

## Checklist de domínio

- [ ] Distingo arquivo, pasta, atalho e extensão.
- [ ] Distingo autenticação, autorização e privilégio.
- [ ] Explico usuário padrão e administrador.
- [ ] Distingo conta local e vinculada a serviço.
- [ ] Explico atualização de qualidade e de recurso.
- [ ] Explico UAC, Defender, firewall, criptografia e Secure Boot.
- [ ] Avalio permissão de aplicativo.
- [ ] Distingo atualização de sistema e de aplicativo.
- [ ] Distingo restaurar, redefinir e reinstalar.
- [ ] Planejo recuperação antes de ação destrutiva.

## Tarefa para o caderno de erros

Para cada erro, complete:

- `sistema envolvido`;
- `recurso citado`;
- `efeito real`;
- `afirmação excessiva do distrator`;
- `teste que eu faria`.

Programe D+2 para contas/privilégios e atualização/restauração.

## Questões associadas

Na futura `semana_01_questoes.md`:

- Dia 2, Questões principais 1 a 50;
- Extras do Dia 2, 10 de Português e 10 de Realidade do Paraná;
- primeira passagem recomendada: 10 principais e 5 extras.

## Fontes do Dia 2

- Windows Update: https://support.microsoft.com/pt-br/windows/deployment/updates-lifecycle/windows-update-faq
- requisitos e segurança do Windows 11: https://support.microsoft.com/pt-BR/Windows/Experience/Compatibility/windows-11-system-requirements
- atualização Android: https://support.google.com/android/answer/7680439?hl=pt-BR
- backup Android: https://support.google.com/android/answer/2819582?hl=pt-BR
- Manual de Uso do iPhone: https://support.apple.com/pt-br/guide/iphone/welcome/ios
- atualização do iOS: https://support.apple.com/pt-br/guide/iphone/iph3e504502/ios

---

# Dia 3 - Microsoft 365, LibreOffice/BrOffice e Google Workspace

## Objetivo e resultados observáveis

Ao final do dia, você deverá:

- associar cada aplicativo à sua função principal;
- comparar formatos, salvamento, exportação e PDF;
- resolver fórmulas com operadores e referências;
- distinguir referência relativa, absoluta e mista;
- escolher papel de compartilhamento adequado;
- avaliar colaboração, histórico, proteção e risco de exposição.

## Por que esse assunto importa

A banca pode cobrar função de aplicativo, resultado de fórmula, referência copiada, formato, impressão ou colaboração. Decorar menus é frágil; compreender o efeito permite resolver enunciados mesmo quando a interface muda.

## Como modelaremos a cobrança FGV

- resultado de fórmula e cópia;
- escolha entre salvar, exportar e compartilhar;
- permissão mínima para colaboração;
- recurso equivalente em suites diferentes;
- diferença entre arquivo local, sincronizado e compartilhado;
- cenário com risco institucional.

## Cronograma de 6h líquidas

| Etapa | Tempo | Atividade |
|---|---:|---|
| Tema principal A | 1h15 | editores, apresentações, formatos e impressão |
| Tema principal B | 1h15 | planilhas, operadores, funções e referências |
| Tema principal C | 45min | colaboração, permissões, versões e proteção |
| Questões essenciais | 45min | até 10 principais, com correção completa |
| Português FGV | 1h | coerência, conectores e relações lógicas |
| Revisão fixa | 40min | mapa das leis institucionais |
| Caderno de erros | 20min | regra funcional em vez de caminho de menu |

## Diagnóstico sem consulta

1. Salvar como PDF mantém necessariamente todos os recursos editáveis?
2. Copiar `=A1*$B$1` altera quais referências?
3. Comentar e editar são a mesma permissão?
4. Sincronizar um arquivo torna qualquer pessoa editora?
5. Writer, Word e Documentos Google possuem a mesma interface?

## Teoria explicada de forma didática

### 1. Aplicativos e serviços do Microsoft 365

- **Word:** documentos de texto;
- **Excel:** planilhas e análise;
- **PowerPoint:** apresentações;
- **Outlook:** correio, calendário e organização;
- **OneDrive:** armazenamento e sincronização;
- **Teams:** comunicação e colaboração.

Aplicativos podem se integrar, mas a função principal permanece relevante. Inserir uma planilha no Word não transforma o Word em Excel.

#### Exemplo resolvido 31 - Aplicativo adequado

**Enunciado:** para calcular automaticamente médias de 500 registros, qual aplicativo é mais adequado: Word ou Excel?  
**Dados:** dados tabulares e cálculos repetitivos.  
**Raciocínio:** planilha oferece células, fórmulas e funções.  
**Resposta:** Excel.  
**Justificativa:** a tarefa exige cálculo estruturado, embora o resultado possa depois ser inserido em relatório.  
**Erro provável:** escolher Word porque a entrega final será um documento.

#### Exemplo resolvido 32 - Serviço integrado

**Enunciado:** armazenar um arquivo no OneDrive significa que todos possuem acesso?  
**Dados:** armazenamento e compartilhamento são funções relacionadas, mas distintas.  
**Raciocínio:** acesso depende das permissões configuradas.  
**Resposta:** não.  
**Justificativa:** arquivo pode permanecer privado ou ser compartilhado com papéis específicos.  
**Erro provável:** confundir nuvem com publicação pública.

### 2. LibreOffice/BrOffice

O edital cita LibreOffice/BrOffice. Para prova, associe:

- **Writer:** texto;
- **Calc:** planilha;
- **Impress:** apresentação.

Formatos abertos comuns incluem ODT, ODS e ODP. A suite pode abrir e salvar outros formatos, mas conversão pode afetar recursos. Compatibilidade deve ser testada quando o documento possui macros, fontes, fórmulas ou layout complexo.

#### Exemplo resolvido 33 - Formato aberto

**Enunciado:** qual formato é nativo de planilha no padrão OpenDocument: ODT ou ODS?  
**Dados:** ODT é texto; ODS é planilha.  
**Raciocínio:** associe a letra final à categoria.  
**Resposta:** ODS.  
**Justificativa:** é o formato OpenDocument Spreadsheet.  
**Erro provável:** escolher ODT por ser o formato OpenDocument mais lembrado.

#### Exemplo resolvido 34 - Compatibilidade

**Enunciado:** abrir um arquivo complexo de outra suite garante preservação integral?  
**Dados:** formatos e implementações podem diferir.  
**Raciocínio:** suporte à abertura não garante equivalência de todos os recursos.  
**Resposta:** não; deve-se testar layout, fórmulas, fontes e automações.  
**Justificativa:** conversão pode alterar elementos não plenamente compatíveis.  
**Erro provável:** interpretar "compatível" como "idêntico em qualquer caso".

### 3. Google Workspace

No núcleo do edital:

- **Documentos:** edição de texto;
- **Planilhas:** cálculos e dados tabulares;
- **Apresentações:** slides;
- **Drive:** armazenamento, organização e compartilhamento.

Os serviços favorecem colaboração, comentários e histórico. Um arquivo importado pode ser convertido, mantendo-se uma cópia do original conforme o fluxo adotado.

#### Exemplo resolvido 35 - Conversão

**Enunciado:** converter uma planilha importada para o formato Google precisa destruir o original?  
**Dados:** o fluxo oficial pode criar cópia no novo formato.  
**Raciocínio:** conversão e exclusão são operações distintas.  
**Resposta:** não; o original pode ser preservado e uma cópia convertida ser criada.  
**Justificativa:** a decisão de excluir não é consequência necessária da conversão.  
**Erro provável:** confundir converter com substituir obrigatoriamente.

#### Exemplo resolvido 36 - Histórico

**Enunciado:** um colaborador alterou indevidamente um trecho. Qual recurso pode ajudar a identificar e recuperar estado anterior?  
**Dados:** documento colaborativo com versões registradas.  
**Raciocínio:** histórico relaciona alterações e versões.  
**Resposta:** histórico de versões, conforme permissões e retenção do serviço.  
**Justificativa:** ele permite comparar estados anteriores.  
**Erro provável:** achar que comentário desfaz automaticamente edição.

### 4. Formatos, salvar, exportar e imprimir

**Salvar** grava o documento no formato atual. **Salvar como** cria ou grava sob outro nome, local ou formato. **Exportar** gera uma representação destinada a outro uso, como PDF.

PDF preserva apresentação para leitura e impressão, mas não garante editabilidade equivalente ao arquivo-fonte. Impressão depende de tamanho de papel, orientação, margens, escala e área selecionada.

#### Exemplo resolvido 37 - PDF

**Enunciado:** exportar uma planilha para PDF preserva necessariamente fórmulas editáveis?  
**Dados:** PDF representa o resultado visual.  
**Raciocínio:** arquivo de publicação não equivale à planilha-fonte.  
**Resposta:** não.  
**Justificativa:** o PDF tende a preservar visualização, não a lógica editável das células.  
**Erro provável:** confundir conteúdo visível com estrutura de cálculo.

#### Exemplo resolvido 38 - Impressão

**Enunciado:** uma tabela larga sai cortada. Qual conjunto deve ser avaliado antes de reduzir fonte manualmente?  
**Dados:** largura excede área imprimível.  
**Raciocínio:** orientação, escala, margens e área de impressão afetam o resultado.  
**Resposta:** revisar esses parâmetros e a seleção de impressão.  
**Justificativa:** o problema pode ser de configuração da página.  
**Erro provável:** alterar o conteúdo antes de verificar a saída.

### 5. Edição, formatação, estilos e revisão

**Conteúdo** é a informação. **Formatação direta** altera aparência local. **Estilo** aplica um conjunto reutilizável e consistente. Cabeçalho, rodapé, quebra de página e seção afetam estrutura.

Recursos de revisão, comentários e controle de alterações ajudam colaboração, mas comentário não modifica necessariamente o texto e aceitar alteração é diferente de apenas visualizá-la.

#### Exemplo resolvido 39 - Estilo x formatação direta

**Enunciado:** todos os títulos precisam mudar de fonte de modo consistente. Qual abordagem é mais sustentável?  
**Dados:** muitos elementos possuem a mesma função estrutural.  
**Raciocínio:** uma regra central reduz alterações repetidas.  
**Resposta:** alterar o estilo aplicado aos títulos.  
**Justificativa:** a mudança se propaga aos elementos vinculados.  
**Erro provável:** editar cada título manualmente.

#### Exemplo resolvido 40 - Comentário x alteração

**Enunciado:** inserir comentário "corrigir data" substitui a data no documento?  
**Dados:** comentário é anotação.  
**Raciocínio:** anotação e edição são ações distintas.  
**Resposta:** não.  
**Justificativa:** alguém ainda precisa editar ou aceitar mudança correspondente.  
**Erro provável:** tratar fluxo de revisão como alteração automática.

### 6. Fórmulas, operadores e funções

Fórmulas começam normalmente com `=`. Operadores comuns:

- aritméticos: `+`, `-`, `*`, `/`, `%`, `^`;
- comparação: `=`, `<>`, `>`, `<`, `>=`, `<=`;
- concatenação de texto: frequentemente `&`.

Parênteses alteram precedência. Funções como `SOMA`, `MÉDIA`, `MÁXIMO`, `MÍNIMO` e `SE` recebem argumentos. Separadores e nomes podem variar conforme produto, versão e localidade; a lógica permanece.

#### Exemplo resolvido 41 - Precedência

**Enunciado:** calcule `=2+3*4` e `=(2+3)*4`.  
**Dados:** multiplicação precede adição; parênteses têm prioridade.  
**Raciocínio:** primeira: `3*4=12`, depois `+2`; segunda: `2+3=5`, depois `*4`.  
**Resposta:** 14 e 20.  
**Justificativa:** os parênteses alteram a ordem.  
**Erro provável:** calcular sempre da esquerda para a direita.

#### Exemplo resolvido 42 - Função e intervalo

**Enunciado:** A1=10, A2=20 e A3=30. Qual o resultado de `=MÉDIA(A1:A3)`?  
**Dados:** soma 60, três valores.  
**Raciocínio:** média = 60/3.  
**Resposta:** 20.  
**Justificativa:** o intervalo inclui A1, A2 e A3.  
**Erro provável:** interpretar os dois pontos como divisão.

### 7. Referências relativas, absolutas e mistas

- `A1`: linha e coluna relativas;
- `$A$1`: linha e coluna fixas;
- `$A1`: coluna fixa, linha relativa;
- `A$1`: coluna relativa, linha fixa.

Ao copiar fórmula, apenas as partes relativas se ajustam.

#### Exemplo resolvido 43 - Referência absoluta

**Enunciado:** em C2 está `=B2*$F$1`. Copie para C3.  
**Dados:** B2 é relativa; `$F$1` é absoluta.  
**Raciocínio:** a linha de B avança; F1 permanece.  
**Resposta:** `=B3*$F$1`.  
**Justificativa:** cifrões fixam coluna e linha.  
**Erro provável:** alterar F1 para F2.

#### Exemplo resolvido 44 - Referência mista

**Enunciado:** copie `=$A2*B$1` uma linha abaixo e uma coluna à direita.  
**Dados:** coluna A fixa; linha 2 relativa; coluna B relativa; linha 1 fixa.  
**Raciocínio:** `$A2` vira `$A3`; `B$1` vira `C$1`.  
**Resposta:** `=$A3*C$1`.  
**Justificativa:** apenas componentes sem `$` se movem.  
**Erro provável:** tratar cada referência como inteiramente fixa ou relativa.

### 8. Compartilhamento, papéis, versões e proteção

Papéis comuns:

- **leitor/visualizador:** consulta;
- **comentarista:** consulta e comenta;
- **editor:** modifica conteúdo;
- **proprietário:** controla o arquivo e seu compartilhamento, conforme serviço.

Compartilhar com pessoa específica tende a oferecer mais controle que link amplo. Permissão deve seguir necessidade. Histórico de versões ajuda rastreabilidade, mas não substitui política de backup. Proteger células ou documento reduz alterações acidentais ou não autorizadas dentro do mecanismo, sem substituir controle de acesso ao sistema.

#### Exemplo resolvido 45 - Menor permissão

**Enunciado:** um revisor deve apontar problemas sem alterar o texto. Qual papel é suficiente?  
**Dados:** precisa comentar, não editar.  
**Raciocínio:** aplique menor privilégio.  
**Resposta:** comentarista.  
**Justificativa:** permite anotação sem conceder edição integral.  
**Erro provável:** escolher editor por ser o papel mais completo.

#### Exemplo resolvido 46 - Link público

**Enunciado:** um documento institucional foi configurado como editável por qualquer pessoa com o link. Qual risco imediato?  
**Dados:** acesso amplo e permissão de edição.  
**Raciocínio:** posse do link pode permitir alteração sem seleção individual.  
**Resposta:** modificação e divulgação indevidas por pessoas não autorizadas.  
**Justificativa:** escopo e privilégio estão excessivos.  
**Erro provável:** considerar o link secreto como autenticação robusta.

## Como o conteúdo funciona na prática

Antes de escolher ferramenta ou comando:

1. identifique o produto final: texto, cálculo, apresentação ou comunicação;
2. preserve o arquivo-fonte;
3. confirme formato e compatibilidade;
4. em planilhas, calcule primeiro sem depender das alternativas;
5. em compartilhamento, conceda o menor papel;
6. teste exportação, impressão e restauração.

## Diferenças entre conceitos próximos

| Conceito A | Conceito B | Diferença decisiva |
|---|---|---|
| salvar | exportar | manter documento de trabalho x gerar representação |
| comentário | edição | anotar x modificar conteúdo |
| estilo | formatação direta | regra reutilizável x alteração local |
| fórmula | função | expressão completa x operação nomeada |
| relativa | absoluta | ajusta na cópia x permanece fixa |
| leitor | comentarista | consulta x consulta e anotação |
| editor | proprietário | altera conteúdo x controla propriedade/compartilhamento |
| sincronização | compartilhamento | replica arquivo x concede acesso |

## Prática guiada

### Caso 1 - Tabela de percentuais

Coloque valores em B2:B10 e a taxa em F1. Use `=B2*$F$1` e copie. A linha do valor deve mudar; a taxa deve permanecer. Valide duas linhas manualmente.

### Caso 2 - Documento para revisão

Mantenha arquivo-fonte, conceda papel de comentarista, use comentários ou controle de alterações e só depois exporte a versão final para PDF.

### Caso 3 - Compatibilidade

Ao trocar de suite, abra uma cópia, compare fontes, quebras, fórmulas e impressão. Não substitua o original antes do teste.

## Pegadinhas do Dia 3

- nuvem não significa acesso público;
- comentário não é edição;
- salvar em PDF não preserva toda a editabilidade;
- compatibilidade não garante identidade perfeita;
- dois pontos em `A1:A3` indicam intervalo;
- copiar fórmula altera apenas partes relativas;
- cifrão pode fixar linha, coluna ou ambas;
- editor possui mais acesso que comentarista;
- histórico de versão não elimina necessidade de backup;
- caminho de menu pode variar, mas o efeito continua sendo cobrado.

## O que memorizar

- Word/Writer/Documentos: texto.
- Excel/Calc/Planilhas: cálculo e dados.
- PowerPoint/Impress/Apresentações: slides.
- PDF é formato de distribuição, não substituto universal do original.
- Fórmula respeita precedência.
- `$` fixa componente da referência.
- Compartilhamento segue menor privilégio.

## Erros comuns

| Erro | Correção |
|---|---|
| calcular pela aparência das alternativas | execute a fórmula passo a passo |
| esquecer precedência | use parênteses e operações por ordem |
| fixar referência errada | diga em voz alta o que deve variar |
| compartilhar como editor sem necessidade | escolha leitor ou comentarista |
| substituir original durante conversão | trabalhe em cópia e valide |

## Tabela de revisão rápida

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| ODT | documento de texto aberto | confundir com planilha | Writer |
| ODS | planilha aberta | confundir com texto | Calc |
| PDF | representação para leitura | presumir fórmulas editáveis | relatório final |
| função | operação nomeada | confundir com fórmula inteira | `SOMA(A1:A3)` |
| `$A$1` | referência absoluta | mover na cópia | taxa fixa |
| `A$1` | linha fixa | fixar também a coluna | cabeçalho |
| comentarista | anota sem editar | conceder editor | revisão |
| histórico | registra versões | chamar de backup completo | recuperar estado |

## Mini revisão do dia

1. diferencie salvar, salvar como e exportar;
2. calcule `=5+2*3`;
3. copie `=$A2*B$1` uma linha abaixo;
4. escolha papel para quem só revisa;
5. explique por que compatibilidade deve ser testada.

## 5 perguntas de fixação

1. Qual é o risco de exportar para PDF e descartar o arquivo-fonte?
2. Como os cifrões controlam a cópia de uma fórmula?
3. Por que um link compartilhado não deve ser tratado como senha?
4. Quando estilo é preferível à formatação direta?
5. Qual é a diferença entre histórico de versões e estratégia de backup?

## Checklist de domínio

- [ ] Associo aplicativos às funções principais.
- [ ] Reconheço ODT, ODS, ODP e PDF.
- [ ] Distingo salvar, salvar como e exportar.
- [ ] Resolvo precedência de operadores.
- [ ] Uso funções e intervalos básicos.
- [ ] Copio referências relativas, absolutas e mistas.
- [ ] Distingo leitor, comentarista, editor e proprietário.
- [ ] Explico histórico e colaboração.
- [ ] Avalio compatibilidade entre suites.
- [ ] Aplico menor privilégio ao compartilhamento.

## Tarefa para o caderno de erros

Registre:

- fórmula original;
- fórmula copiada;
- componente que deveria variar;
- componente que deveria ficar fixo;
- erro de cálculo ou interpretação.

Programe D+2 para referências e papéis de compartilhamento.

## Questões associadas

Na futura `semana_01_questoes.md`:

- Dia 3, Questões principais 1 a 50;
- Extras do Dia 3, 10 de Português e 10 de legislação institucional;
- primeira passagem recomendada: 10 principais e 5 extras.

## Fontes do Dia 3

- Microsoft 365: https://support.microsoft.com/pt-br/training
- LibreOffice Calc: https://help.libreoffice.org/latest/pt-BR/text/scalc/guide/main.html
- fórmulas no Calc: https://help.libreoffice.org/latest/pt-BR/text/scalc/guide/formulas.html
- Centro de Aprendizagem Google Workspace: https://support.google.com/a/users
- Planilhas Google: https://support.google.com/a/users/answer/9282959?hl=pt-BR

---

# Dia 4 - Língua Portuguesa no padrão FGV

## Objetivo e resultados observáveis

Ao final do dia, você deverá:

- localizar tema, finalidade, ideia central e tese;
- distinguir informação explícita, pressuposto, inferência e extrapolação;
- reconhecer progressão, coesão e coerência;
- identificar referentes e relações lógicas;
- classificar o modo discursivo predominante;
- avaliar reescrita quanto a sentido, correção e clareza.

## Por que esse assunto importa

Português possui 25 questões. A FGV costuma usar texto como base real da decisão. Duas alternativas podem parecer possíveis, mas apenas uma respeita todos os limites semânticos do trecho.

## Como modelaremos a cobrança FGV

- inferência limitada ao texto;
- função de um segmento;
- referente de pronome ou expressão;
- valor de conectivo no contexto;
- modo discursivo predominante;
- reescrita com pequena alteração decisiva;
- diferença entre frase correta e frase equivalente.

## Cronograma de 6h líquidas

| Etapa | Tempo | Atividade |
|---|---:|---|
| Tema principal A | 1h15 | compreensão, informação e inferência |
| Tema principal B | 1h15 | estrutura, coesão, coerência e intertextualidade |
| Tema principal C | 45min | modos discursivos e reescrita |
| Questões essenciais | 45min | até 10 principais de Português |
| Oficina de Português | 1h | justificar reescritas e eliminar distratores |
| Revisão fixa | 40min | conjuntos, porcentagem e proporcionalidade |
| Caderno de erros | 20min | evidência que confirma ou invalida a alternativa |

## Diagnóstico sem consulta

Leia: "A digitalização acelerou o atendimento, mas não eliminou a necessidade de conferir os dados."

1. O texto afirma que a conferência ficou desnecessária?
2. Qual relação é introduzida por "mas"?
3. A digitalização é apresentada como inútil?
4. Qual é a informação central?
5. Trocar "mas" por "portanto" preserva o sentido?

## Teoria explicada de forma didática

### 1. Tema, assunto, finalidade, ideia central e tese

**Tema** é o campo geral. **Assunto** é o recorte tratado. **Ideia central** resume o núcleo informativo. **Tese** é a posição defendida em texto argumentativo. **Finalidade** é o objetivo comunicativo: informar, convencer, orientar, criticar ou narrar.

Nem todo texto tem tese. Uma notícia pode informar sem defender explicitamente uma posição.

#### Exemplo resolvido 47 - Tema e ideia central

Texto: "A autenticação em dois fatores reduz o risco decorrente do vazamento de senha, embora não elimine outras formas de ataque."

**Enunciado:** indique tema e ideia central.  
**Dados:** há um controle, um benefício e um limite.  
**Raciocínio:** tema é amplo; ideia central reúne benefício e limite.  
**Resposta:** tema: segurança de autenticação; ideia central: o segundo fator reduz um risco específico, mas não elimina todos os ataques.  
**Justificativa:** a oração concessiva impede conclusão absoluta.  
**Erro provável:** resumir como "dois fatores impedem ataques".

#### Exemplo resolvido 48 - Finalidade

Texto: "Antes de redefinir o dispositivo, confirme se o backup foi concluído."

**Enunciado:** qual é a finalidade predominante?  
**Dados:** verbo no imperativo e sequência de ação.  
**Raciocínio:** o trecho orienta comportamento.  
**Resposta:** instruir ou orientar.  
**Justificativa:** não apenas informa; recomenda uma ação anterior.  
**Erro provável:** classificar como narrativo porque há ordem temporal.

### 2. Informação explícita, pressuposto, implícito e inferência

**Explícito** está dito. **Pressuposto** é informação tomada como existente pela construção. **Implícito** depende de leitura além da forma literal. **Inferência** é conclusão apoiada por pistas. **Extrapolação** vai além do autorizado.

Palavras como "ainda", "voltou", "parou" e "também" podem ativar pressupostos.

#### Exemplo resolvido 49 - Pressuposto

Frase: "A equipe voltou a testar as cópias."

**Enunciado:** o que a frase pressupõe?  
**Dados:** verbo "voltar a".  
**Raciocínio:** retomar uma ação pressupõe ocorrência anterior.  
**Resposta:** a equipe já testava ou já testou as cópias antes.  
**Justificativa:** o pressuposto decorre da construção verbal.  
**Erro provável:** inferir que os testes anteriores falharam; isso não foi dito.

#### Exemplo resolvido 50 - Inferência autorizada

Texto: "O relatório foi enviado às 18h03, três minutos após o prazo."

**Enunciado:** pode-se concluir que o envio foi intempestivo?  
**Dados:** prazo às 18h00 e envio posterior.  
**Raciocínio:** compare horários.  
**Resposta:** sim, se "prazo" indica limite final aplicável ao envio.  
**Justificativa:** a conclusão é diretamente sustentada.  
**Erro provável:** concluir também a causa do atraso, que não aparece.

### 3. Estrutura e progressão textual

Textos organizam informação em blocos. Um parágrafo pode apresentar:

- ideia principal;
- explicação;
- exemplo;
- contraste;
- consequência;
- conclusão.

**Progressão** exige que o texto avance. Repetição pode cumprir coesão, mas repetição sem função prejudica o desenvolvimento.

#### Exemplo resolvido 51 - Função do exemplo

Texto: "Controles distintos protegem riscos distintos. A criptografia, por exemplo, reduz a exposição de dados armazenados."

**Enunciado:** qual é a função da segunda frase?  
**Dados:** marcador "por exemplo".  
**Raciocínio:** a frase particulariza a afirmação geral.  
**Resposta:** exemplificar o princípio apresentado.  
**Justificativa:** criptografia é caso concreto de controle.  
**Erro provável:** dizer que a segunda frase contradiz a primeira.

#### Exemplo resolvido 52 - Conclusão

Texto: "O arquivo tinha cópia local e sincronizada, mas ambas foram corrompidas. Logo, faltava uma versão independente e recuperável."

**Enunciado:** "logo" introduz qual relação?  
**Dados:** fatos anteriores sustentam uma conclusão.  
**Raciocínio:** a última oração deriva do caso.  
**Resposta:** conclusão.  
**Justificativa:** o conector apresenta resultado argumentativo.  
**Erro provável:** classificar como causa apenas porque há relação lógica.

### 4. Coesão referencial, sequencial e lexical

**Coesão referencial** retoma ou antecipa elementos: pronomes, expressões e elipses. **Coesão sequencial** conecta partes e relações. **Coesão lexical** usa repetição controlada, sinônimos, hiperônimos e campos semânticos.

O referente deve ser identificado pelo sentido e pela estrutura, não apenas pela palavra mais próxima.

#### Exemplo resolvido 53 - Referente

Frase: "O perito entregou o laudo ao delegado, que solicitou uma cópia."

**Enunciado:** quem solicitou a cópia?  
**Dados:** pronome relativo "que" segue "delegado".  
**Raciocínio:** o antecedente sintático mais natural é "delegado".  
**Resposta:** o delegado.  
**Justificativa:** a oração relativa caracteriza esse termo.  
**Erro provável:** escolher "perito" por ser o sujeito da oração principal.

#### Exemplo resolvido 54 - Coesão lexical

Texto: "O notebook foi recolhido. O equipamento permaneceu lacrado."

**Enunciado:** que mecanismo liga as frases?  
**Dados:** "equipamento" retoma "notebook".  
**Raciocínio:** há substituição por termo mais geral.  
**Resposta:** coesão lexical por hiperônimo.  
**Justificativa:** equipamento abrange notebook e evita repetição literal.  
**Erro provável:** chamar de pronome.

### 5. Coerência, contradição, continuidade e relevância

**Coerência** é a compatibilidade global de sentidos. Um texto pode ter conectores e ainda ser incoerente. A coerência depende de:

- ausência de contradição não explicada;
- continuidade temática;
- relevância;
- compatibilidade entre partes;
- conhecimento compartilhado usado de modo razoável.

#### Exemplo resolvido 55 - Coesão sem coerência

Frase: "O sistema estava desligado; portanto, processou normalmente os pedidos naquele instante."

**Enunciado:** o conector torna a frase coerente?  
**Dados:** desligado x processamento normal simultâneo.  
**Raciocínio:** o conector não elimina contradição factual.  
**Resposta:** não.  
**Justificativa:** há coesão formal, mas incompatibilidade semântica.  
**Erro provável:** considerar qualquer frase com conector automaticamente coerente.

#### Exemplo resolvido 56 - Relevância

Texto: "A equipe analisou os logs do incidente. O prédio foi pintado em 2019. Depois, correlacionou horários e endereços IP."

**Enunciado:** qual segmento rompe a continuidade?  
**Dados:** investigação digital interrompida por pintura do prédio.  
**Raciocínio:** a informação intermediária não contribui ao tópico.  
**Resposta:** "O prédio foi pintado em 2019."  
**Justificativa:** falta relevância para a progressão.  
**Erro provável:** aceitar o segmento por ser gramaticalmente correto.

### 6. Intertextualidade

Intertextualidade é a relação de um texto com outro. Pode ocorrer por:

- citação;
- alusão;
- paráfrase;
- paródia;
- referência a gênero, fórmula ou expressão conhecida.

Reconhecer intertextualidade não autoriza atribuir ao novo texto todas as ideias do texto-fonte.

#### Exemplo resolvido 57 - Citação

Texto: "Como dispõe a norma, o acesso deve observar a finalidade autorizada."

**Enunciado:** há sinal de intertextualidade?  
**Dados:** referência explícita a uma norma.  
**Raciocínio:** o enunciado convoca outro texto.  
**Resposta:** sim, por remissão ou citação indireta.  
**Justificativa:** o sentido se apoia em texto normativo externo.  
**Erro provável:** exigir aspas para qualquer relação intertextual.

#### Exemplo resolvido 58 - Limite da alusão

Texto: "No meio do caminho havia uma senha fraca."

**Enunciado:** a alusão permite concluir que o autor reproduz todo o poema de origem?  
**Dados:** a estrutura lembra formulação conhecida.  
**Raciocínio:** alusão é relação pontual.  
**Resposta:** não.  
**Justificativa:** o novo contexto produz sentido próprio.  
**Erro provável:** transferir integralmente conteúdo e intenção do texto-fonte.

### 7. Modos discursivos

- **descrição:** apresenta características;
- **narração:** organiza acontecimentos no tempo;
- **exposição:** explica um tema;
- **argumentação:** defende posição com razões;
- **injunção:** orienta ou ordena ação.

Um texto pode misturar modos. A questão costuma pedir o predominante ou a função de um trecho.

#### Exemplo resolvido 59 - Modo predominante

Texto: "Abra as configurações, selecione atualização e verifique o status."

**Enunciado:** qual modo predomina?  
**Dados:** verbos de ação dirigidos ao leitor.  
**Raciocínio:** o texto prescreve etapas.  
**Resposta:** injunção.  
**Justificativa:** sua finalidade é orientar procedimento.  
**Erro provável:** chamar de narração por haver sequência.

#### Exemplo resolvido 60 - Texto híbrido

Texto: "A autenticação combina fatores distintos. Por isso, é mais prudente ativá-la em contas sensíveis."

**Enunciado:** o primeiro período é expositivo ou argumentativo? E o conjunto?  
**Dados:** definição seguida de recomendação fundamentada.  
**Raciocínio:** trechos podem ter funções diferentes.  
**Resposta:** o primeiro é expositivo; o conjunto assume orientação argumentativa.  
**Justificativa:** a segunda frase usa a explicação como razão.  
**Erro provável:** exigir um único modo para todas as frases.

### 8. Reescrita: sentido, correção, clareza e lógica

Uma reescrita pode:

- estar gramaticalmente correta, mas alterar o sentido;
- preservar sentido, mas mudar ênfase;
- introduzir ambiguidade;
- trocar causa por consequência;
- transformar possibilidade em certeza;
- eliminar restrição ou concessão.

Compare uma mudança por vez.

#### Exemplo resolvido 61 - Possibilidade x certeza

Original: "A atualização pode exigir reinicialização."  
Reescrita: "A atualização exige reinicialização."

**Enunciado:** o sentido foi preservado?  
**Dados:** "pode" indica possibilidade; a reescrita afirma necessidade universal.  
**Raciocínio:** houve aumento de certeza.  
**Resposta:** não.  
**Justificativa:** a modalidade foi alterada.  
**Erro provável:** ignorar verbos modais por parecerem acessórios.

#### Exemplo resolvido 62 - Concessão

Original: "Embora o arquivo estivesse criptografado, foi necessário restaurar o backup."  
Reescrita: "Como o arquivo estava criptografado, foi necessário restaurar o backup."

**Enunciado:** a relação lógica foi mantida?  
**Dados:** "embora" = concessão; "como" no início pode indicar causa.  
**Raciocínio:** a relação muda de contraste para causa.  
**Resposta:** não.  
**Justificativa:** a criptografia deixa de ser circunstância contrastante e vira causa.  
**Erro provável:** avaliar apenas as informações nominais repetidas.

## Como o conteúdo funciona na prática

### Como pensar para acertar

1. leia o comando antes das alternativas;
2. resuma o trecho em uma frase neutra;
3. sublinhe operadores: negação, restrição, possibilidade e conectores;
4. exija evidência para cada inferência;
5. compare escopo: alguns, muitos, todos, pode, deve;
6. em reescrita, identifique exatamente o que mudou.

## Diferenças entre conceitos próximos

| Conceito A | Conceito B | Diferença decisiva |
|---|---|---|
| tema | tese | campo tratado x posição defendida |
| explícito | inferido | dito x concluído por pistas |
| inferência | extrapolação | apoiada x além do texto |
| coesão | coerência | ligação formal x compatibilidade de sentido |
| referente | palavra próxima | elemento retomado x proximidade gráfica |
| exposição | argumentação | explicar x defender posição |
| narração | injunção | relatar ações x orientar ações |
| correção | equivalência | forma aceitável x mesmo sentido |

## Prática guiada

### Texto 1

"O uso de registros eletrônicos amplia a rastreabilidade. Entretanto, registros incompletos podem dificultar a análise."

- ideia central: registros ajudam, desde que tenham qualidade;
- "entretanto": oposição;
- inferência válida: completude influencia utilidade;
- extrapolação: todo registro eletrônico é confiável.

### Texto 2

"Confirme o destinatário antes de enviar o arquivo, pois a revogação do acesso não desfaz uma cópia já realizada."

- modo predominante: injuntivo;
- "pois": justificativa;
- finalidade: prevenir divulgação indevida;
- erro comum: afirmar que revogar nunca tem utilidade.

## Pegadinhas do Dia 4

- inferência não é opinião livre;
- uma palavra absoluta pode invalidar alternativa;
- coesão formal não garante coerência;
- o referente não é sempre o substantivo mais próximo;
- texto híbrido pode ter um modo predominante;
- "mas", "embora", "portanto" e "porque" não são intercambiáveis;
- frase correta pode não preservar sentido;
- retirar "pode" transforma possibilidade em certeza;
- exemplo não é necessariamente argumento principal;
- informação verdadeira no mundo pode estar ausente do texto.

## O que memorizar

- evidência textual vem antes da alternativa;
- tese exige posição defendida;
- pressuposto é ativado pela construção;
- inferência precisa de pista;
- coesão liga; coerência compatibiliza;
- modo predominante depende da função;
- reescrita exige sentido e correção.

## Erros comuns

| Erro | Correção |
|---|---|
| escolher alternativa "verdadeira" fora do texto | pergunte onde o trecho a sustenta |
| ignorar modalizadores | marque pode, deve, sempre, apenas |
| avaliar reescrita só pela gramática | compare relação lógica e alcance |
| classificar pelo primeiro verbo | observe a finalidade do conjunto |
| confundir oposição e concessão | oposição coordena; concessão admite obstáculo sem impedir o fato |

## Tabela de revisão rápida

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| tese | posição defendida | confundir com tema | "deve-se..." |
| pressuposto | dado tomado como prévio | inventar causa | "voltou a" |
| inferência | conclusão apoiada | extrapolar | envio após prazo |
| coesão | ligação textual | chamar de coerência | pronome retomador |
| coerência | compatibilidade de sentido | aceitar contradição | continuidade temática |
| injunção | orientação de ação | chamar de narração | "verifique" |
| concessão | obstáculo que não impede | trocar por causa | "embora" |
| modalização | grau de certeza/obrigação | ignorar "pode" | possibilidade |

## Mini revisão do dia

1. resuma o texto do diagnóstico;
2. explique a relação de "mas";
3. crie uma inferência e uma extrapolação;
4. diferencie coesão e coerência;
5. altere "pode" para "deve" e explique o efeito.

## 5 perguntas de fixação

1. Como provar que uma inferência é autorizada?
2. Por que uma frase coesa pode ser incoerente?
3. Como identificar o modo discursivo predominante?
4. Qual é o risco de ignorar modalizadores em reescrita?
5. Dê um exemplo de pressuposto sem acrescentar informação não autorizada.

## Checklist de domínio

- [ ] Distingo tema, ideia central, finalidade e tese.
- [ ] Distingo explícito, pressuposto e inferência.
- [ ] Reconheço extrapolação.
- [ ] Identifico a função de segmentos.
- [ ] Localizo referentes.
- [ ] Distingo coesão e coerência.
- [ ] Reconheço intertextualidade.
- [ ] Distingo os cinco modos discursivos.
- [ ] Avalio conectores no contexto.
- [ ] Comparo reescritas quanto a sentido e correção.

## Tarefa para o caderno de erros

Para cada alternativa errada, registre:

- palavra decisiva;
- evidência textual;
- tipo de erro: extrapolação, relação lógica, referente, escopo ou gramática;
- reescrita mínima que tornaria a alternativa correta.

## Questões associadas

Na futura `semana_01_questoes.md`:

- Dia 4, Questões principais 1 a 50;
- Extras do Dia 4, 10 de revisão de TI e 10 de RLM;
- primeira passagem recomendada: 10 principais e 5 extras.

## Fontes do Dia 4

- edital PCPR nº 01/2026, Conhecimentos Gerais, itens 1.1 a 1.4;
- PCPI 2025 - Oficial Investigador: https://conhecimento.fgv.br/concursos/pcpi25/2
- PCMG 2024 - Investigador: https://conhecimento.fgv.br/concursos/pcmg24/04
- PCRJ 2021 - Investigador: https://conhecimento.fgv.br/concursos/pcrj21/02
- PCAM 2021 - Investigador e áreas periciais: https://conhecimento.fgv.br/concursos/pcam21/02

---

# Dia 5 - Raciocínio Lógico-Matemático e Realidade do Paraná

## Objetivo e resultados observáveis

Ao final do dia, você deverá:

- reconhecer proposições e conectivos;
- negar proposições simples e compostas;
- aplicar equivalências introdutórias;
- resolver conjuntos, porcentagem e proporcionalidade;
- organizar a formação territorial do Paraná em etapas;
- relacionar relevo, clima, hidrografia, vegetação, população e economia;
- distinguir município, região estatística e região de planejamento;
- interpretar dado oficial sem confundir ano, unidade ou fonte.

## Por que esse assunto importa

RLM e Realidade do Paraná somam dez questões. A pontuação é menor que Português e TI, mas o conteúdo é recuperável com prática regular. O objetivo da Semana 1 é impedir primeiro contato tardio.

## Como modelaremos a cobrança FGV

- tradução entre linguagem natural e lógica;
- negação de conectivos;
- diagrama e contagem sem dupla contagem;
- porcentagem sucessiva;
- relação direta ou inversa;
- leitura de dado, mapa ou linha do tempo;
- alternativa que troca região, período ou característica.

## Cronograma de 6h líquidas

| Etapa | Tempo | Atividade |
|---|---:|---|
| Tema principal A | 1h15 | proposições, conectivos, negação e equivalências |
| Tema principal B | 1h15 | conjuntos, porcentagem e proporcionalidade |
| Tema principal C | 45min | formação e geografia do Paraná |
| Questões essenciais | 45min | 6 de RLM e 4 de Paraná |
| Português FGV | 1h | semântica contextual e ambiguidade |
| Revisão fixa | 40min | LC 259/2023 e Lei 23.213/2026, visão inicial |
| Caderno de erros | 20min | cálculo completo e fonte do dado |

## Diagnóstico sem consulta

1. Uma pergunta é uma proposição lógica?
2. Qual é a negação de "Ana estuda e Bruno trabalha"?
3. Aumentar 20% e diminuir 20% retorna ao valor inicial?
4. Quantos municípios tem o Paraná?
5. Região geográfica do IBGE e região de planejamento são necessariamente iguais?

## Teoria explicada de forma didática

### 1. Proposição, valor lógico e conectivos

**Proposição** é uma sentença declarativa que pode ser classificada como verdadeira ou falsa. Perguntas, ordens e sentenças abertas com variável não determinada não são proposições.

Conectivos básicos:

- negação: `não p`, símbolo `¬p`;
- conjunção: `p e q`, `p ∧ q`;
- disjunção inclusiva: `p ou q`, `p ∨ q`;
- condicional: `se p, então q`, `p → q`;
- bicondicional: `p se e somente se q`, `p ↔ q`.

Na disjunção inclusiva, `p ou q` é verdadeira quando pelo menos uma é verdadeira. O condicional só é falso quando o antecedente é verdadeiro e o consequente é falso.

#### Exemplo resolvido 63 - O que é proposição

**Enunciado:** classifique: I. "Curitiba é a capital do Paraná." II. "Feche a porta." III. "x é maior que 3."  
**Dados:** declaração completa, ordem e sentença aberta.  
**Raciocínio:** somente a primeira possui valor lógico determinado.  
**Resposta:** apenas I é proposição.  
**Justificativa:** II é ordem; III depende do valor de `x`.  
**Erro provável:** chamar qualquer frase gramatical de proposição.

#### Exemplo resolvido 64 - Condicional

**Enunciado:** `p` é verdadeira e `q` é falsa. Qual o valor de `p → q`?  
**Dados:** antecedente verdadeiro e consequente falso.  
**Raciocínio:** essa é a única combinação que torna o condicional falso.  
**Resposta:** falso.  
**Justificativa:** a condição ocorreu, mas a consequência afirmada não.  
**Erro provável:** tratar o condicional como conjunção em todas as linhas.

### 2. Negação e equivalências introdutórias

Leis de De Morgan:

- `¬(p ∧ q) ≡ ¬p ∨ ¬q`;
- `¬(p ∨ q) ≡ ¬p ∧ ¬q`.

Condicional:

- `p → q ≡ ¬p ∨ q`;
- contrapositiva: `p → q ≡ ¬q → ¬p`;
- negação: `¬(p → q) ≡ p ∧ ¬q`.

Não confunda **contrapositiva** com **recíproca**. De `p → q`, a recíproca `q → p` não é automaticamente equivalente.

#### Exemplo resolvido 65 - Negação da conjunção

**Enunciado:** negue "O arquivo está íntegro e o backup está disponível."  
**Dados:** estrutura `p ∧ q`.  
**Raciocínio:** negar a conjunção troca `e` por `ou` e nega cada parte.  
**Resposta:** "O arquivo não está íntegro ou o backup não está disponível."  
**Justificativa:** basta uma das partes falhar para a conjunção ser falsa.  
**Erro provável:** usar "e" na negação.

#### Exemplo resolvido 66 - Contrapositiva

**Enunciado:** dê uma equivalente a "Se o acesso foi autorizado, então houve autenticação válida."  
**Dados:** `p → q`.  
**Raciocínio:** use `¬q → ¬p`.  
**Resposta:** "Se não houve autenticação válida, então o acesso não foi autorizado."  
**Justificativa:** é a contrapositiva.  
**Erro provável:** escrever "Se houve autenticação válida, então o acesso foi autorizado", que é a recíproca.

### 3. Conjuntos e diagramas

Operações:

- união `A ∪ B`: elementos em A ou B;
- interseção `A ∩ B`: elementos comuns;
- diferença `A - B`: elementos de A que não pertencem a B;
- complemento: elementos do universo fora do conjunto.

Para dois conjuntos finitos:

`n(A ∪ B) = n(A) + n(B) - n(A ∩ B)`

A interseção é subtraída porque foi contada duas vezes.

#### Exemplo resolvido 67 - Inclusão-exclusão

**Enunciado:** 40 pessoas usam sistema A, 30 usam B e 12 usam ambos. Quantas usam pelo menos um?  
**Dados:** `n(A)=40`, `n(B)=30`, `n(A∩B)=12`.  
**Raciocínio:** `40+30-12`.  
**Resposta:** 58.  
**Justificativa:** os 12 usuários comuns não podem ser contados duas vezes.  
**Erro provável:** responder 70.

#### Exemplo resolvido 68 - Diferença

**Enunciado:** no caso anterior, quantas usam A e não usam B?  
**Dados:** 40 em A; 12 também em B.  
**Raciocínio:** retire de A a interseção.  
**Resposta:** 28.  
**Justificativa:** `40-12=28`.  
**Erro provável:** subtrair 30, como se todo B estivesse contido em A.

### 4. Números, porcentagem e proporcionalidade

Os conjuntos numéricos se encaixam: naturais, inteiros, racionais e reais. Todo inteiro é racional porque pode ser escrito sobre denominador 1. Decimal finito ou periódico é racional. Em operações, respeite sinais, frações e precedência.

Uma porcentagem é uma razão de denominador 100. Variação:

`taxa = (novo - antigo) / antigo`

Variações sucessivas multiplicam fatores. Aumento de 20% usa `1,20`; redução de 20% usa `0,80`. O produto é `0,96`, portanto não retorna ao início.

Na proporcionalidade:

- **direta:** uma grandeza cresce no mesmo fator da outra;
- **inversa:** uma cresce e a outra diminui de modo que o produto se mantém, no modelo ideal.

Em juros:

- simples: `M = C(1 + i×t)`;
- compostos: `M = C(1+i)^t`.

Capital `C`, taxa `i` e tempo `t` devem estar no mesmo período.

#### Exemplo resolvido 69 - Percentuais sucessivos

**Enunciado:** um valor de 500 aumenta 20% e depois cai 20%. Qual o valor final?  
**Dados:** fatores 1,20 e 0,80.  
**Raciocínio:** `500 × 1,20 = 600`; `600 × 0,80 = 480`.  
**Resposta:** 480.  
**Justificativa:** a segunda taxa incide sobre base diferente.  
**Erro provável:** anular `+20%` com `-20%`.

#### Exemplo resolvido 70 - Proporção inversa

**Enunciado:** quatro equipes idênticas concluem uma triagem em 6 horas. No modelo ideal, seis equipes levariam quanto?  
**Dados:** trabalho fixo; equipes e tempo inversamente proporcionais.  
**Raciocínio:** `4×6 = 6×t`; `t=4`.  
**Resposta:** 4 horas.  
**Justificativa:** mais equipes reduzem tempo no modelo sem perda de eficiência.  
**Erro provável:** aplicar regra direta e obter 9 horas.

#### Exemplo complementar D5.1 - Operação com sinais

**Enunciado:** calcule `-3 + 5/2`.  
**Dados:** `-3 = -6/2`.  
**Raciocínio:** `-6/2 + 5/2 = -1/2`.  
**Resposta:** `-1/2`, ou `-0,5`.  
**Justificativa:** denominadores iguais permitem somar numeradores.  
**Erro provável:** ignorar o sinal negativo.

#### Exemplo complementar D5.2 - Soma de frações

**Enunciado:** calcule `3/4 + 2/3`.  
**Dados:** mínimo múltiplo comum 12.  
**Raciocínio:** `9/12 + 8/12 = 17/12`.  
**Resposta:** `17/12`, ou `1 5/12`.  
**Justificativa:** frações precisam de denominador comum.  
**Erro provável:** somar numeradores e denominadores para obter `5/7`.

#### Exemplo complementar D5.3 - Juros simples

**Enunciado:** R$ 1.000,00 são aplicados a 2% ao mês por 3 meses, em juros simples. Qual o montante?  
**Dados:** `C=1000`, `i=0,02`, `t=3`.  
**Raciocínio:** `M=1000(1+0,02×3)=1000×1,06`.  
**Resposta:** R$ 1.060,00.  
**Justificativa:** a taxa incide sempre sobre o capital inicial.  
**Erro provável:** aplicar potência, própria do regime composto.

#### Exemplo complementar D5.4 - Juros compostos

**Enunciado:** use os mesmos dados no regime composto.  
**Dados:** `C=1000`, `i=0,02`, `t=3`.  
**Raciocínio:** `M=1000×1,02³=1000×1,061208`.  
**Resposta:** R$ 1.061,21, arredondado aos centavos.  
**Justificativa:** cada período incorpora juros à nova base.  
**Erro provável:** responder R$ 1.060,00, como no regime simples.
### 5. Formação territorial do Paraná

O território atual resulta de longa presença indígena, ocupação colonial, ciclos econômicos, migrações e decisões políticas. Uma periodização útil, sem apagar a diversidade, distingue:

- **Paraná Tradicional:** litoral, primeiro planalto, Campos Gerais, Guarapuava e Palmas; mineração inicial, pecuária, tropeirismo e erva-mate;
- **Norte:** expansão ligada à cafeicultura, companhias colonizadoras e ferrovias, especialmente no século XX;
- **Oeste e Sudoeste:** ocupação intensificada por frentes migratórias e expansão agropecuária no século XX.

O Paraná tornou-se província separada de São Paulo em 1853. Isso não significa que sua história começou nessa data.

#### Exemplo resolvido 71 - Formação x criação política

**Enunciado:** afirmar que a história do Paraná começou em 1853 é adequado?  
**Dados:** a criação provincial ocorreu após ocupações e sociedades anteriores.  
**Raciocínio:** criação administrativa e formação histórica são conceitos distintos.  
**Resposta:** não.  
**Justificativa:** 1853 é marco político, não início da presença humana ou da ocupação.  
**Erro provável:** transformar marco institucional em origem absoluta.

#### Exemplo resolvido 72 - Região histórico-cultural

**Enunciado:** tropeirismo e Campos Gerais se associam mais diretamente a qual esquema de ocupação?  
**Dados:** interiorização histórica pelo Paraná Tradicional.  
**Raciocínio:** relacione atividade, rota e área.  
**Resposta:** Paraná Tradicional.  
**Justificativa:** o tropeirismo contribuiu para núcleos e economia dessa área.  
**Erro provável:** associar automaticamente ao norte cafeeiro.

### 6. Geografia física: relevo, clima, hidrografia e vegetação

O relevo é frequentemente estudado como:

- planície litorânea;
- Serra do Mar;
- Primeiro, Segundo e Terceiro Planaltos.

O clima varia com latitude, altitude e massas de ar. Predominam condições subtropicais, com variações mais quentes no norte e mais frias em áreas elevadas.

A drenagem é amplamente interior, ligada à bacia do Paraná. Rios importantes incluem Paraná, Iguaçu, Paranapanema, Tibagi, Ivaí e Piquiri. No litoral, há drenagens voltadas ao Atlântico.

A vegetação integra o bioma Mata Atlântica em diferentes formações, como Floresta Ombrófila Densa, Floresta com Araucária, Floresta Estacional Semidecidual e campos.

#### Exemplo resolvido 73 - Relevo e litoral

**Enunciado:** Serra do Mar e planície litorânea são a mesma unidade?  
**Dados:** uma é alinhamento elevado; outra é faixa baixa costeira.  
**Raciocínio:** posição próxima não elimina diferença geomorfológica.  
**Resposta:** não.  
**Justificativa:** possuem altitude, forma e dinâmica distintas.  
**Erro provável:** fundir tudo o que está no leste em uma única unidade.

#### Exemplo resolvido 74 - Hidrografia

**Enunciado:** afirmar que todos os rios paranaenses correm diretamente para o Atlântico é correto?  
**Dados:** grande parte integra a bacia do Paraná.  
**Raciocínio:** drenagem interior e drenagem litorânea coexistem.  
**Resposta:** não.  
**Justificativa:** muitos rios seguem para o sistema do rio Paraná.  
**Erro provável:** deduzir direção apenas porque o estado possui litoral.

### 7. População e atividades econômicas

O Paraná tem distribuição populacional desigual e forte urbanização. Densidade é razão entre população e área, não sinônimo de população total.

A economia é diversificada:

- agropecuária e cadeias agroindustriais;
- indústria de transformação;
- comércio e serviços;
- logística e integração regional.

Evite reduzir o estado a um único produto. Ciclos históricos ajudam a explicar ocupação, mas a estrutura atual é mais complexa.

#### Exemplo resolvido 75 - Densidade

**Enunciado:** município A tem 100 mil habitantes em 100 km²; B tem 200 mil em 1.000 km². Qual é mais denso?  
**Dados:** A: `100.000/100`; B: `200.000/1.000`.  
**Raciocínio:** A=1.000 hab/km²; B=200 hab/km².  
**Resposta:** A.  
**Justificativa:** maior população total não implica maior densidade.  
**Erro provável:** escolher B pelo número absoluto.

#### Exemplo resolvido 76 - Economia diversificada

**Enunciado:** o fato de a agropecuária ser relevante permite concluir que serviços e indústria são irrelevantes?  
**Dados:** economia estadual possui múltiplos setores.  
**Raciocínio:** relevância de um setor não exclui os demais.  
**Resposta:** não.  
**Justificativa:** a economia é diversificada e regionalmente heterogênea.  
**Erro provável:** transformar destaque em exclusividade.

### 8. Organização territorial, municípios e regiões

O Paraná possui **399 municípios**, e Curitiba é a capital. Município é ente político-administrativo. Regiões podem ser criadas para finalidades distintas:

- regiões geográficas do IBGE, para análise estatística;
- regiões metropolitanas e aglomerações, por arranjo legal;
- regiões de planejamento ou desenvolvimento, para políticas públicas.

Não presuma que mapas regionais de finalidades diferentes tenham os mesmos limites.

#### Exemplo resolvido 77 - Município x região

**Enunciado:** uma região geográfica do IBGE é um novo ente federativo?  
**Dados:** trata-se de recorte analítico.  
**Raciocínio:** ente político e divisão estatística têm naturezas diferentes.  
**Resposta:** não.  
**Justificativa:** a região auxilia organização e análise, sem se tornar município ou estado.  
**Erro provável:** atribuir personalidade política a qualquer divisão territorial.

#### Exemplo resolvido 78 - Comparação de indicadores

**Enunciado:** um dado populacional de 2022 e uma estimativa de 2025 podem ser comparados como se fossem da mesma natureza?  
**Dados:** censo e estimativa possuem referência e método distintos.  
**Raciocínio:** compare ano, conceito e fonte antes do valor.  
**Resposta:** não sem ressalvas.  
**Justificativa:** séries e métodos diferentes exigem contextualização.  
**Erro provável:** copiar números atuais sem observar a data.

## Como o conteúdo funciona na prática

### Para RLM

1. traduza o texto para símbolos ou relações;
2. escreva dados e unidade;
3. resolva antes de olhar alternativas;
4. teste a resposta no enunciado;
5. identifique o erro que geraria cada distrator.

### Para Paraná

1. verifique se a questão é histórica, geográfica ou administrativa;
2. marque período e escala;
3. diferencie fato estrutural de dado conjuntural;
4. confira fonte e ano;
5. evite absolutos como "todo", "apenas" e "sempre".

## Diferenças entre conceitos próximos

| Conceito A | Conceito B | Diferença decisiva |
|---|---|---|
| proposição | sentença aberta | valor lógico definido x depende de variável |
| condicional | bicondicional | uma implicação x implicação nos dois sentidos |
| contrapositiva | recíproca | equivalente x não necessariamente equivalente |
| união | interseção | pelo menos um x elementos comuns |
| porcentagem | ponto percentual | variação relativa x diferença entre taxas |
| direta | inversa | fatores no mesmo sentido x sentidos opostos |
| população | densidade | total de pessoas x pessoas por área |
| município | região estatística | ente político x recorte analítico |

## Prática guiada

### Caso 1 - Lógica

Negue: "O sistema está atualizado ou o firewall está ativo."  
Solução: "O sistema não está atualizado e o firewall não está ativo." A negação da disjunção usa conjunção.

### Caso 2 - Porcentagem

Uma taxa passa de 20% para 25%. O aumento é de 5 pontos percentuais e de 25% em termos relativos, pois `(25-20)/20 = 0,25`.

### Caso 3 - Paraná

Ao comparar dois municípios, separe população total, área, densidade, ano e fonte. Não use somente um número para concluir desenvolvimento ou qualidade de vida.

## Pegadinhas do Dia 5

- pergunta e ordem não são proposições;
- `p → q` não equivale a `q → p`;
- negar "e" produz "ou";
- somar conjuntos sem retirar interseção duplica pessoas;
- aumento e redução de mesma taxa usam bases diferentes;
- juros simples usam base constante; compostos incorporam juros à base;
- taxa e tempo devem estar no mesmo período;
- população total não é densidade;
- 1853 é marco político, não início da história;
- região estatística não é ente federativo;
- um setor relevante não torna a economia exclusiva;
- dado sem ano pode induzir comparação inválida.

## O que memorizar

- condicional só é falso em V → F;
- `¬(p∧q)=¬p∨¬q`;
- `¬(p∨q)=¬p∧¬q`;
- união soma e retira a interseção;
- percentuais sucessivos multiplicam fatores;
- juros simples: `M=C(1+i×t)`; compostos: `M=C(1+i)^t`;
- Paraná: 399 municípios; capital Curitiba;
- formação territorial é processo, não data única;
- dado oficial deve vir com ano e fonte.

## Erros comuns

| Erro | Correção |
|---|---|
| negar mantendo o conectivo | aplique De Morgan |
| usar recíproca como equivalente | use contrapositiva |
| anular percentuais iguais | multiplique fatores |
| decorar geografia sem escala | relacione localização, unidade e processo |
| usar notícia sem fonte primária | prefira IBGE, IPARDES e órgãos estaduais |

## Tabela de revisão rápida

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| proposição | sentença V ou F | incluir pergunta | "Curitiba é capital" |
| condicional | se p, então q | inverter | V → F é falso |
| interseção | parte comum | contar duas vezes | usuários de A e B |
| percentual | razão sobre 100 | confundir com p.p. | 20% de 500 |
| juros simples | taxa sobre capital inicial | usar potência | R$ 1.000 a 2% por 3 meses |
| juros compostos | taxa sobre saldo acumulado | somar taxas sem capitalização | `1000×1,02³` |
| direta | cresce junto | usar em equipes/tempo | preço e quantidade |
| densidade | população/área | olhar só população | hab/km² |
| Paraná Tradicional | área histórico-cultural | confundir com norte cafeeiro | Campos Gerais |
| região do IBGE | recorte estatístico | chamar de ente | região intermediária |

## Mini revisão do dia

1. negue uma conjunção;
2. escreva a contrapositiva de um condicional;
3. resolva uma união com interseção;
4. explique percentuais sucessivos;
5. diferencie marco político e processo histórico.

## 5 perguntas de fixação

1. Por que a recíproca não é automaticamente equivalente ao condicional?
2. Como evitar dupla contagem em conjuntos?
3. Qual é a diferença entre porcentagem e ponto percentual?
4. Como os ciclos econômicos se relacionam à ocupação do Paraná?
5. Por que duas regionalizações do Paraná podem ter limites diferentes?

## Checklist de domínio

- [ ] Reconheço proposições e sentenças abertas.
- [ ] Uso conectivos e valores lógicos.
- [ ] Nego conjunção, disjunção e condicional.
- [ ] Distingo contrapositiva e recíproca.
- [ ] Resolvo união, interseção e diferença.
- [ ] Opero números e resolvo porcentagens e juros simples/compostos.
- [ ] Distingo proporção direta e inversa.
- [ ] Organizo a formação territorial do Paraná.
- [ ] Relaciono relevo, clima, rios e vegetação.
- [ ] Distingo população, densidade, município e região.

## Tarefa para o caderno de erros

Em RLM, registre todas as contas e a lei lógica aplicada. Em Paraná, registre:

- fato;
- período;
- escala territorial;
- fonte;
- palavra absoluta do distrator.

## Questões associadas

Na futura `semana_01_questoes.md`:

- Dia 5, Questões 1 a 30 de RLM;
- Dia 5, Questões 31 a 50 de Realidade do Paraná;
- Extras do Dia 5: 10 de Português, 5 de TI e 5 de legislação;
- primeira passagem: 6 principais de RLM, 4 de Paraná e 5 extras.

## Fontes do Dia 5

- IBGE, Paraná: https://www.ibge.gov.br/cidades-e-estados/pr.html
- IPARDES, Base de Dados do Estado: https://www.ipardes.pr.gov.br/Pagina/Base-de-Dados-do-Estado
- Patrimônio Cultural do Paraná, história paranaense: https://www.patrimoniocultural.pr.gov.br/Pagina/HISTORIA-PARANAENSE
- Instituto Água e Terra, mapas históricos: https://www.iat.pr.gov.br/Pagina/Coletanea-de-Mapas-Historicos-do-Parana
- edital PCPR nº 01/2026, Conhecimentos Gerais, itens 2.1 a 2.4 e 3.1 a 3.3.

---

# Dia 6 - Legislação institucional e integração da semana

## Objetivo e resultados observáveis

Ao final do dia, você deverá:

- localizar a função de cada norma estudada;
- explicar a relação entre normas gerais nacionais e organização estadual;
- distinguir estrutura de carreira, organização institucional e disciplina;
- reconhecer princípios, competências, deveres e vedações sem misturá-los;
- resolver casos indicando primeiro a norma e o instituto;
- evitar criação de prazo, sanção ou competência;
- integrar tecnologia, sigilo, rastreabilidade e dever funcional.

## Por que esse assunto importa

Legislação Estadual e Institucional possui cinco questões. A matéria combina literalidade e aplicação. Uma única troca de sujeito, competência ou alcance pode tornar a alternativa errada.

## Como modelaremos a cobrança FGV

- caso curto com escolha da norma aplicável;
- regra nacional x organização estadual;
- princípio x competência x dever;
- carreira x instituição;
- dever x vedação x transgressão;
- alternativa que amplia, restringe ou troca o sujeito;
- comando negativo com quatro afirmações corretas.

## Cronograma de 6h líquidas

| Etapa | Tempo | Atividade |
|---|---:|---|
| Tema principal A | 1h15 | leitura normativa, LC 259/2023 e Lei 14.735/2023 |
| Tema principal B | 1h15 | Lei 23.213/2026 e Lei 21.894/2024 |
| Tema principal C | 45min | contrastes, casos e integração |
| Questões essenciais | 45min | 6 de legislação e 4 integradas |
| Português FGV | 1h | revisão de interpretação, coesão e reescrita |
| Revisão fixa | 40min | recuperação cumulativa de TI, RLM e Paraná |
| Caderno de erros | 20min | ranking de lacunas e D+7 |

## Diagnóstico sem consulta

1. Lei Orgânica Nacional e Lei Orgânica Estadual têm a mesma função?
2. Estrutura de carreira e código disciplinar são sinônimos?
3. Toda competência da Polícia Civil pertence individualmente a qualquer servidor?
4. Uma conduta pode ser analisada em mais de uma esfera?
5. É seguro decorar sanção sem conferir o texto vigente?

## Teoria explicada de forma didática

### 1. Hierarquia, competência normativa e leitura de lei

O ponto de partida é a Constituição. A Lei Federal nº 14.735/2023 estabelece normas gerais nacionais para as Polícias Civis. O Estado organiza sua instituição e suas carreiras por normas próprias, respeitando a Constituição e as normas gerais aplicáveis.

Evite a fórmula simplista "lei federal sempre vence lei estadual". É preciso observar:

1. quem possui competência para legislar;
2. se a regra é geral ou específica;
3. qual é o objeto;
4. se houve alteração ou revogação;
5. qual texto está vigente.

Para ler lei seca:

- leia ementa e artigo inicial;
- identifique destinatário e verbo;
- marque exceções;
- separe princípio, competência, direito, dever, vedação e sanção;
- confira remissões e alterações.

#### Exemplo resolvido 79 - Objeto da norma

**Enunciado:** para saber a estrutura das carreiras do QPPC, qual norma deve ser consultada primeiro entre LC 259/2023 e Código Disciplinar?  
**Dados:** a primeira estrutura carreiras; a segunda disciplina condutas e procedimentos.  
**Raciocínio:** escolha pelo objeto.  
**Resposta:** LC Estadual nº 259/2023.  
**Justificativa:** carreira e disciplina são matérias distintas.  
**Erro provável:** escolher a norma mais recente sem observar o assunto.

#### Exemplo resolvido 80 - Norma geral e específica

**Enunciado:** uma lei estadual pode ignorar normas gerais nacionais aplicáveis?  
**Dados:** a Lei 14.735/2023 estabelece normas gerais e admite disciplina estadual específica e suplementar.  
**Raciocínio:** autonomia estadual não significa incompatibilidade livre.  
**Resposta:** não.  
**Justificativa:** a organização estadual deve respeitar o quadro constitucional e as normas gerais.  
**Erro provável:** dizer que a norma estadual sempre prevalece por tratar do próprio estado.

### 2. Lei Complementar Estadual nº 259/2023

A LC 259/2023 dispõe sobre a estruturação das carreiras da Polícia Civil do Paraná. Seu artigo inicial situa o Quadro Próprio da Polícia Civil e as funções policiais de polícia judiciária e administrativa e de apuração de infrações penais, exceto as militares.

Na leitura introdutória, concentre-se em:

- objeto da lei;
- conceitos de carreira e estrutura;
- cargos do quadro e requisitos;
- ingresso, formação e desenvolvimento;
- direitos e regras funcionais relacionados à carreira;
- alterações posteriores incorporadas ao texto consolidado.

Não use versão original isolada quando a página oficial oferece texto alterado ou compilado.

#### Exemplo resolvido 81 - Estrutura de carreira

**Enunciado:** uma questão pergunta sobre classes, progressão e ingresso. O Código Disciplinar é a fonte principal?  
**Dados:** o caso trata de desenvolvimento funcional.  
**Raciocínio:** identifique a matéria antes do artigo.  
**Resposta:** não; a LC 259/2023 é a referência inicial.  
**Justificativa:** seu objeto é a estruturação das carreiras.  
**Erro provável:** usar qualquer norma da PCPR como se tratasse de todos os temas.

#### Exemplo resolvido 82 - Exceção militar

**Enunciado:** a descrição geral das funções do QPPC inclui apuração de infrações penais militares?  
**Dados:** o texto ressalva infrações militares.  
**Raciocínio:** a exceção limita a regra.  
**Resposta:** não, conforme a ressalva legal.  
**Justificativa:** expressões como "exceto" são decisivas.  
**Erro provável:** memorizar apenas "apuração de infrações penais" e apagar a exceção.

### 3. Lei Federal nº 14.735/2023

A Lei Orgânica Nacional:

- reconhece as Polícias Civis como instituições permanentes, com funções típicas e exclusivas de Estado;
- integra as Polícias Civis ao Sistema Único de Segurança Pública;
- estabelece princípios, diretrizes e competências;
- prevê estrutura organizacional básica e quadro policial;
- trata de direitos, deveres e vedações em âmbito geral.

Entre os princípios estão proteção da dignidade humana, preservação do sigilo necessário, hierarquia e disciplina. Entre as competências institucionais estão polícia judiciária civil, apuração de infrações penais, preservação de locais, identificação, cadeia de custódia e atividades de inteligência, nos limites legais.

**Competência da instituição** não equivale automaticamente à atribuição individual de qualquer cargo. O exercício respeita a lei e as atribuições próprias.

#### Exemplo resolvido 83 - Competência institucional

**Enunciado:** a lei atribui à Polícia Civil a preservação da cadeia de custódia. Isso autoriza qualquer servidor a praticar qualquer ato sem observar seu cargo?  
**Dados:** competência institucional e atribuições individuais coexistem.  
**Raciocínio:** a instituição age por seus agentes nos limites legais.  
**Resposta:** não.  
**Justificativa:** competência do órgão não elimina distribuição de atribuições.  
**Erro provável:** transferir integralmente ao indivíduo tudo que pertence à instituição.

#### Exemplo resolvido 84 - Sigilo necessário

**Enunciado:** o princípio de preservação do sigilo significa ocultação ilimitada de toda atividade?  
**Dados:** a lei relaciona sigilo à efetividade da investigação e à intimidade, dentro da legalidade.  
**Raciocínio:** princípio tem finalidade e limites.  
**Resposta:** não.  
**Justificativa:** sigilo necessário não é autorização absoluta fora das hipóteses legais.  
**Erro provável:** transformar uma proteção funcional em poder sem limite.

### 4. Lei Estadual nº 23.213/2026

A Lei Orgânica da PCPR dispõe sobre princípios, diretrizes, estrutura, organização, funcionamento e competência da instituição no Paraná. Ela se relaciona expressamente à Constituição, à Lei Orgânica Nacional e à legislação aplicável.

O texto caracteriza a PCPR como instituição permanente, dirigida por Delegado de Polícia, com funções de polícia judiciária e administrativa e apuração de infrações penais, ressalvadas as militares.

Para a primeira leitura:

- identifique órgãos e unidades;
- marque competências institucionais;
- separe direção, execução, controle e apoio;
- observe atribuições sem inventar extensão;
- compare a lei estadual com a nacional.

#### Exemplo resolvido 85 - Lei nacional x estadual

**Enunciado:** para conhecer a organização concreta da PCPR, basta ler apenas a Lei 14.735/2023?  
**Dados:** a lei nacional estabelece normas gerais; a estadual organiza a PCPR.  
**Raciocínio:** a resposta completa exige as duas camadas.  
**Resposta:** não.  
**Justificativa:** a Lei 23.213/2026 trata da organização estadual específica.  
**Erro provável:** considerar a norma geral um organograma completo de cada estado.

#### Exemplo resolvido 86 - Funções institucionais

**Enunciado:** a PCPR apura, como regra geral, infrações penais militares?  
**Dados:** o texto legal ressalva essa categoria.  
**Raciocínio:** aplique a exceção expressa.  
**Resposta:** não.  
**Justificativa:** a competência geral de apuração não abrange as infrações militares.  
**Erro provável:** apagar a ressalva ao resumir.

### 5. Lei Estadual nº 21.894/2024

O Código Disciplinar da Polícia Civil do Paraná estabelece:

- princípios e critérios;
- destinatários;
- deveres e vedações;
- transgressões e sanções;
- aplicação da pena;
- responsabilidade;
- procedimentos, recursos e revisão;
- prescrição e instrumentos previstos no próprio código.

Na Semana 1, o objetivo é compreender a arquitetura. Prazos, espécies de sanção e enquadramentos específicos serão estudados com leitura literal e texto vigente.

**Dever** exige comportamento. **Vedação** proíbe. **Transgressão** descreve conduta disciplinarmente relevante. **Sanção** é consequência aplicada mediante o processo correspondente.

#### Exemplo resolvido 87 - Dever x vedação

**Enunciado:** "zelar pelo patrimônio" e "utilizar informação sigilosa em benefício particular" pertencem à mesma categoria lógica?  
**Dados:** uma expressão impõe conduta; outra descreve comportamento proibido.  
**Raciocínio:** observe o verbo e o efeito.  
**Resposta:** não; a primeira é dever e a segunda é vedação ou conduta proibida, conforme o texto aplicável.  
**Justificativa:** obrigação positiva e proibição não são sinônimos.  
**Erro provável:** chamar toda regra funcional de dever.

#### Exemplo resolvido 88 - Sanção sem processo

**Enunciado:** identificada suspeita de transgressão, a sanção pode ser presumida antes da apuração?  
**Dados:** o código também disciplina procedimentos e responsabilidade.  
**Raciocínio:** suspeita, apuração e decisão são etapas distintas.  
**Resposta:** não.  
**Justificativa:** a consequência depende do devido procedimento e do enquadramento comprovado.  
**Erro provável:** saltar do relato à penalidade.

### 6. Relação entre as quatro normas

| Norma | Função central nesta semana |
|---|---|
| LC 259/2023 | estruturação das carreiras do QPPC |
| Lei 14.735/2023 | normas gerais nacionais das Polícias Civis |
| Lei 23.213/2026 | organização e funcionamento da PCPR |
| Lei 21.894/2024 | disciplina, deveres, vedações e processo disciplinar |

As normas se complementam, mas não são intercambiáveis. Uma questão pode exigir duas leituras: por exemplo, princípio nacional e implementação estadual.

#### Exemplo resolvido 89 - Norma correta

**Enunciado:** onde procurar primeiro uma regra sobre processo disciplinar: Lei 23.213/2026 ou Lei 21.894/2024?  
**Dados:** o assunto é apuração disciplinar.  
**Raciocínio:** escolha a norma especializada no objeto.  
**Resposta:** Lei 21.894/2024.  
**Justificativa:** ela institui o Código Disciplinar.  
**Erro provável:** escolher a Lei Orgânica por parecer mais abrangente.

#### Exemplo resolvido 90 - Leitura combinada

**Enunciado:** uma questão pergunta por princípio nacional e unidade estadual responsável por implementá-lo. Uma única lei pode ser insuficiente?  
**Dados:** princípio e organização pertencem a camadas relacionadas.  
**Raciocínio:** consulte norma geral e norma estadual.  
**Resposta:** sim.  
**Justificativa:** a primeira pode definir o princípio; a segunda, a estrutura concreta.  
**Erro provável:** procurar toda resposta em um único diploma.

### 7. Método para resolver casos legais

Use a sequência:

1. identifique o sujeito;
2. identifique a ação;
3. determine a matéria;
4. escolha a norma;
5. localize regra e exceção;
6. compare cada elemento da alternativa;
7. não complete o texto por intuição.

Em comando "assinale a incorreta", escreva ao lado: **procuro a única errada**. Depois demonstre por que as outras estão corretas.

#### Exemplo resolvido 91 - Troca de sujeito

**Enunciado:** uma alternativa atribui a um servidor, individualmente, competência que a lei confere à instituição. Como avaliar?  
**Dados:** sujeitos normativos diferentes.  
**Raciocínio:** compare quem pratica o ato na norma e na alternativa.  
**Resposta:** a alternativa pode estar errada por troca de sujeito, salvo atribuição individual específica.  
**Justificativa:** competência institucional não se transfere automaticamente.  
**Erro provável:** observar apenas o verbo e ignorar o sujeito.

#### Exemplo resolvido 92 - Palavra absoluta

**Enunciado:** uma alternativa afirma que o sigilo é "sempre absoluto e sem exceções".  
**Dados:** a legislação usa sigilo necessário e admite hipóteses legais.  
**Raciocínio:** "sempre", "absoluto" e "sem exceções" ampliam a regra.  
**Resposta:** a afirmação é incompatível com o caráter limitado pela legalidade.  
**Justificativa:** proteção funcional não elimina todas as hipóteses legais de acesso ou divulgação.  
**Erro provável:** escolher pelo valor intuitivo do sigilo, sem ler o alcance.

### 8. Integração com tecnologia e rotina policial

Tecnologia não afasta deveres institucionais. Em um caso com arquivo, log ou sistema:

- preserve integridade e rastreabilidade;
- limite acesso;
- registre ações;
- respeite finalidade;
- use canal institucional;
- mantenha sigilo necessário;
- observe competência e atribuição.

Esta integração prepara o estudo futuro de segurança, evidência digital e cadeia de custódia.

#### Exemplo resolvido 93 - Compartilhamento indevido

**Enunciado:** um arquivo institucional sensível é enviado por link editável e amplo para facilitar o trabalho. A conveniência elimina o dever de controle?  
**Dados:** acesso excessivo e informação sensível.  
**Raciocínio:** eficiência deve coexistir com segurança, sigilo e finalidade.  
**Resposta:** não.  
**Justificativa:** o meio tecnológico não afasta deveres; deve-se restringir acesso e usar canal adequado.  
**Erro provável:** tratar rapidez como justificativa absoluta.

#### Exemplo resolvido 94 - Log e rastreabilidade

**Enunciado:** uma equipe desativa registros de acesso porque "o sistema continua funcionando". Qual dimensão foi prejudicada?  
**Dados:** operação disponível, mas ações deixam de ser registradas.  
**Raciocínio:** funcionamento e rastreabilidade são propriedades distintas.  
**Resposta:** rastreabilidade e capacidade de auditoria.  
**Justificativa:** sem logs adequados, fica mais difícil reconstruir eventos.  
**Erro provável:** medir segurança apenas pela disponibilidade.

## Como o conteúdo funciona na prática

Faça um mapa com quatro colunas:

| Pergunta | Resposta esperada |
|---|---|
| Qual é o objeto? | carreira, organização, disciplina ou norma geral |
| Quem é o sujeito? | instituição, órgão, cargo ou servidor |
| Qual é o verbo? | compete, deve, pode, é vedado |
| Há limite? | exceção, finalidade, condição ou remissão |

Antes de memorizar artigo, compreenda essa estrutura.

## Diferenças entre conceitos próximos

| Conceito A | Conceito B | Diferença decisiva |
|---|---|---|
| norma geral | norma estadual específica | diretriz nacional x organização local |
| carreira | instituição | desenvolvimento funcional x estrutura do órgão |
| competência | atribuição | poder/dever do órgão x função do cargo/agente |
| princípio | regra operacional | vetor interpretativo x comando específico |
| dever | vedação | obrigação x proibição |
| transgressão | sanção | conduta tipificada x consequência |
| suspeita | responsabilidade comprovada | notícia inicial x conclusão após procedimento |
| sigilo | ausência de controle | proteção legal x ocultação arbitrária |

## Prática guiada

### Caso 1 - Qual norma consultar?

- promoção e classe: LC 259/2023;
- estrutura da PCPR: Lei 23.213/2026;
- princípio nacional: Lei 14.735/2023;
- processo disciplinar: Lei 21.894/2024.

### Caso 2 - Informação institucional

Antes de compartilhar, responda: quem precisa, para qual finalidade, com qual papel, por quanto tempo e por qual canal. Registre a decisão quando o procedimento exigir.

### Caso 3 - Comando negativo

Marque o comando, analise sujeito, verbo, objeto e exceção de cada alternativa. O gabarito é a única incorreta; as quatro restantes precisam resistir à leitura literal.

## Pegadinhas do Dia 6

- lei mais recente não substitui automaticamente lei anterior inteira;
- lei federal não "vence sempre" sem análise de competência;
- norma geral não traz necessariamente toda a organização estadual;
- estrutura de carreira não é código disciplinar;
- competência institucional não é poder individual ilimitado;
- dever, vedação, transgressão e sanção são categorias diferentes;
- sigilo necessário não é segredo absoluto;
- suspeita não equivale a responsabilidade comprovada;
- exceções como "exceto as militares" não podem ser apagadas;
- tecnologia não suspende deveres funcionais.

## O que memorizar

- LC 259: carreiras.
- Lei 14.735: normas gerais nacionais.
- Lei 23.213: Lei Orgânica da PCPR.
- Lei 21.894: Código Disciplinar.
- Leia sujeito, verbo, objeto e exceção.
- Não crie prazo, competência ou sanção.
- Use sempre o texto oficial vigente e consolidado.

## Erros comuns

| Erro | Correção |
|---|---|
| decorar número sem objeto | associe norma a uma pergunta concreta |
| usar resumo como fonte final | confirme no texto oficial |
| ignorar alterações | consulte versão consolidada |
| transferir competência do órgão ao indivíduo | confira atribuição legal |
| concluir sanção antes do procedimento | separe suspeita, apuração e decisão |

## Tabela de revisão rápida

| Conceito | Definição curta | Pegadinha comum | Exemplo |
|---|---|---|---|
| LC 259/2023 | estrutura carreiras | chamar de código disciplinar | ingresso e desenvolvimento |
| Lei 14.735/2023 | normas gerais nacionais | tratar como organograma estadual | princípios e competências |
| Lei 23.213/2026 | organização da PCPR | confundir com carreira | órgãos e funcionamento |
| Lei 21.894/2024 | disciplina | presumir sanção automática | deveres e procedimento |
| competência | matéria do órgão | transferir ao indivíduo | preservar local |
| dever | conduta exigida | confundir com sanção | zelar |
| vedação | conduta proibida | confundir com princípio | uso indevido |
| exceção | limite da regra | apagar no resumo | exceto militares |

## Mini revisão do dia

1. associe as quatro normas a seus objetos;
2. explique norma geral e estadual;
3. diferencie competência e atribuição;
4. diferencie dever, transgressão e sanção;
5. resolva um caso de compartilhamento institucional.

## 5 perguntas de fixação

1. Por que a norma mais recente não revoga automaticamente todas as anteriores?
2. Como distinguir estrutura de carreira e organização institucional?
3. Qual é o risco de transferir competência do órgão a qualquer servidor?
4. Por que suspeita de transgressão não equivale a sanção?
5. Como tecnologia, sigilo e rastreabilidade se relacionam?

## Checklist de domínio

- [ ] Identifico o objeto das quatro normas.
- [ ] Distingo norma geral e organização estadual.
- [ ] Distingo carreira, instituição e disciplina.
- [ ] Leio sujeito, verbo, objeto e exceção.
- [ ] Distingo princípio, competência e atribuição.
- [ ] Distingo dever, vedação, transgressão e sanção.
- [ ] Não invento prazo ou consequência.
- [ ] Resolvo comando negativo conscientemente.
- [ ] Uso texto oficial consolidado.
- [ ] Integro segurança tecnológica e dever funcional.

## Tarefa para o caderno de erros

Use uma ficha por erro:

- norma;
- artigo ou seção a conferir;
- sujeito;
- verbo;
- objeto;
- exceção;
- palavra alterada pelo distrator.

Liste os cinco temas mais frágeis da semana e programe D+7.

## Questões associadas

Na futura `semana_01_questoes.md`:

- Dia 6, Questões 1 a 30 de legislação institucional;
- Dia 6, Questões 31 a 50 de integração da Semana 1;
- Extras do Dia 6: 10 de Português e 10 de revisão cumulativa;
- primeira passagem: 6 de legislação, 4 integradas e 5 extras.

## Fontes do Dia 6

- LC Estadual nº 259/2023, texto oficial: https://www.legislacao.pr.gov.br/legislacao/exibirAto.do?action=iniciarProcesso&codAto=300584
- Lei Federal nº 14.735/2023, texto oficial: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14735.htm
- Lei Estadual nº 23.213/2026, texto oficial: https://www.legislacao.pr.gov.br/legislacao/pesquisarAto.do?action=exibir&codAto=394817&codItemAto=2516525
- Lei Estadual nº 21.894/2024, texto oficial: https://www.legislacao.pr.gov.br/legislacao/pesquisarAto.do?action=exibir&codAto=323068&codItemAto=2047551
- eventual alteração posterior somente após confirmação em fonte oficial.

---

# Revisão final da Semana 1

## Recuperação ativa de 30 minutos

Sem consultar, explique:

1. RAM, SSD, cache e ROM;
2. backup incremental e diferencial;
3. driver, firmware, BIOS e UEFI;
4. autenticação, autorização e menor privilégio;
5. atualizar, restaurar, redefinir e reinstalar;
6. fórmula, função e referência absoluta;
7. leitor, comentarista, editor e proprietário;
8. inferência, extrapolação, coesão e coerência;
9. negação, contrapositiva e união de conjuntos;
10. formação, geografia e organização territorial do Paraná;
11. objeto das quatro normas do Dia 6.

## Revisão por erros

Classifique cada erro da semana:

- **C:** conceito;
- **L:** leitura do comando;
- **D:** distrator plausível;
- **M:** memória;
- **P:** procedimento ou cálculo;
- **F:** fonte ou atualização.

Priorize erros repetidos e erros de alta pontuação, especialmente Português e TI.

## Entrega final da semana

- [ ] 104 exemplos resolvidos refeitos sem consulta.
- [ ] 60 questões principais essenciais corrigidas.
- [ ] 30 questões extras essenciais corrigidas.
- [ ] revisões D+2 realizadas.
- [ ] D+7 programado.
- [ ] mapa de normas produzido.
- [ ] tabela de fórmulas e referências produzida.
- [ ] mapa básico do Paraná produzido.
- [ ] caderno de erros com causa e regra.

O número de questões acima é a meta máxima da primeira passagem desta apostila: até dez principais e cinco extras por dia. O restante do banco futuro será distribuído nas revisões.

## Conteúdo que permanece pendente

- Português, itens 1.5 a 1.26;
- RLM, itens 2.5 a 2.13;
- Realidade do Paraná, itens 3.4 a 3.7;
- TI, itens 1.3 a 1.6;
- leitura aprofundada de toda a legislação institucional e itens 5.1, 5.6 e 5.7;
- Ciências Forenses, Contabilidade, Estatística e disciplinas jurídicas.

Pendência declarada não é falha. O erro seria marcar esses itens como cobertos.

# Preparação física paralela

O TAF previsto no edital inclui barra fixa masculina ou isometria feminina, abdominal remador, shuttle run, escalada em corda e corrida de 12 minutos.

Na Semana 1:

1. localize a tabela aplicável a sexo e idade no edital;
2. faça avaliação inicial segura;
3. registre técnica, resultado e margem;
4. identifique limitações;
5. procure orientação profissional para prescrição.

Não execute teste máximo diante de dor, lesão, doença ou condição insegura. A preparação física não integra as 6h teóricas.

# Fontes utilizadas

## Concurso e banca

- PCPR 2026: https://conhecimento.fgv.br/concursos/pcpr26
- edital oficial: https://conhecimento.fgv.br/sites/default/files/concursos/edital-01-2026-pcpr-publicacao.docx-1.pdf
- PCPI 2025: https://conhecimento.fgv.br/concursos/pcpi25/2
- PCMG 2024: https://conhecimento.fgv.br/concursos/pcmg24/04
- PCRJ 2021: https://conhecimento.fgv.br/concursos/pcrj21/02
- PCAM 2021: https://conhecimento.fgv.br/concursos/pcam21/02

## Tecnologia

- Microsoft Support: https://support.microsoft.com/pt-br/
- Ajuda do Android: https://support.google.com/android/
- Manual de Uso do iPhone: https://support.apple.com/pt-br/guide/iphone/welcome/ios
- Ajuda do LibreOffice: https://help.libreoffice.org/latest/pt-BR/
- Centro de Aprendizagem Google Workspace: https://support.google.com/a/users

## Paraná

- IBGE: https://www.ibge.gov.br/cidades-e-estados/pr.html
- IPARDES: https://www.ipardes.pr.gov.br/Pagina/Base-de-Dados-do-Estado
- Patrimônio Cultural do Paraná: https://www.patrimoniocultural.pr.gov.br/Pagina/HISTORIA-PARANAENSE
- Instituto Água e Terra: https://www.iat.pr.gov.br/Pagina/Coletanea-de-Mapas-Historicos-do-Parana

## Legislação

- Sistema Estadual de Legislação do Paraná: https://www.legislacao.pr.gov.br/
- Portal da Legislação Federal: https://www.planalto.gov.br/ccivil_03/

# Próximo passo

Esta apostila deve passar por auditoria estrutural, técnica, normativa e pedagógica. Somente depois do aceite será produzida a apostila de questões da Semana 1.
