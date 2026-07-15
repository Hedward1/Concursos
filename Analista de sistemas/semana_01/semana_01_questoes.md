# Apostila de Questões - Semana 1 v1.3

## CRA-PR 2026 - Analista de Sistemas

Arquivo de questões para acompanhar a `semana_01_estudo.md`.

**Critério de autoria:** esta versão não reproduz questões reais de provas anteriores. As 300 questões principais e as 120 questões extras são autorais. Todas seguem o estilo de cobrança do Instituto Consulplan. As provas públicas da banca foram usadas somente como referência de estilo, sem reprodução de questões reais.

**Formato:** todas as questões têm quatro alternativas, de A) a D), conforme o edital do CRA-PR 2026.

**Total:** 420 questões, sendo 300 questões principais (50 por dia) e 120 questões extras de revisão fixa (20 por dia).

**Níveis a partir do Dia 3:** `Médio`, `Difícil` e `Muito difícil`. Cada bloco de 50 questões principais adota 20/20/10; cada bloco de 20 extras adota 8/8/4. A dificuldade deve decorrer do conhecimento exigido e de distratores plausíveis, nunca de ambiguidade ou informação ausente. Essa regra também se aplica a todo questionário complementar criado a partir do Dia 3. Os questionários dos Dias 1 e 2 foram preservados nesta revisão.

---

## Fontes oficiais e referências de estilo

- Edital CRA-PR 2026, cargo Analista de Sistemas, conforme Retificação I: https://cdnsite.institutoconsulplan.org.br/concursos/1330/b2c07c473c9749fea22728da3c964c06.pdf
- Lei Federal nº 4.769/1965: https://www.planalto.gov.br/ccivil_03/leis/l4769.htm
- Decreto Federal nº 61.934/1967: https://www.planalto.gov.br/ccivil_03/decreto/Antigos/D61934.htm
- Lei nº 12.514/2011: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12514.htm
- RN CFA nº 649/2024: https://documentos.cfa.org.br/?a=show&c=documento&id=951
- RN CFA nº 670/2025: https://documentos.cfa.org.br/?a=show&c=documento&id=1033
- RN CFA nº 546/2018: https://documentos.cfa.org.br/?a=show&c=documento&id=700
- RN CFA nº 626/2023: https://documentos.cfa.org.br/?a=show&c=documento&id=803
- RN CFA nº 589/2020: https://documentos.cfa.org.br/arquivos/resolucao_normativa_589_2020_745.pdf
- RN CFA nº 651/2024: https://documentos.cfa.org.br/?a=show&c=documento&id=955
- RN CFA nº 671/2025: https://documentos.cfa.org.br/?a=show&c=documento&id=1038
- RN CFA nº 680/2025: https://documentos.cfa.org.br/?a=show&c=documento&id=1058
- Provas Instituto Consulplan usadas apenas como referência de estilo: TJRO 2025 Analista de Sistemas; TJMA 2024 Analista de Sistemas; Câmara Municipal de Belo Horizonte 2024 Analista de TI.

---

# Dia 1 — Arquitetura e Organização de Computadores

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões principais

### Questão 1

Em uma rotina de diagnóstico, um analista precisa converter o valor binário 101101 para decimal. O resultado correto é:

A) 53
B) 64
C) 45
D) 37

### Questão 2

Um dump de memória apresenta o byte 1111 0000. Em hexadecimal, esse valor deve ser representado por:

A) FF
B) F0
C) 0F
D) E0

### Questão 3

Considere as assertivas sobre unidades de informação.

I. Um byte é composto por 8 bits.
II. Com 8 bits, podem ser representadas 256 combinações distintas.
III. O maior valor sem sinal representável com 8 bits é 256.

Está correto apenas o que se afirma em:

A) I e II
B) I e III
C) II e III
D) I, II e III

### Questão 4

Assinale a alternativa incorreta sobre a hierarquia de memória.

A) Registradores ficam no nível mais rápido e próximo da CPU.
B) O SSD é normalmente mais rápido que registradores e cache.
C) A RAM é volátil e usada como memória principal durante a execução de programas.
D) A memória cache costuma ser usada para manter dados frequentemente acessados próximos da CPU.

### Questão 5

Durante a execução de um programa, a CPU precisa realizar uma soma e uma comparação lógica. O componente diretamente associado a essas operações é:

A) Barramento de endereços
B) Memória secundária
C) ULA/ALU
D) Unidade de controle

### Questão 6

Um técnico afirma que a RAM é suficiente como política de armazenamento permanente porque possui alta velocidade. Essa afirmação é:

A) incorreta apenas se o sistema operacional for Linux.
B) incorreta, pois a RAM é volátil e não substitui SSD/HD para persistência.
C) correta, pois toda memória rápida é permanente por definição.
D) correta apenas em processadores de 64 bits.

### Questão 7

Em uma placa de rede, a chegada de um pacote pode sinalizar à CPU que há evento a tratar. Esse mecanismo é melhor descrito como:

A) interrupção
B) compilação
C) paginação
D) normalização

### Questão 8

Analise as assertivas sobre interrupções.

I. Interrupções podem ser usadas para tratar eventos de entrada e saída.
II. Toda interrupção representa falha irrecuperável de hardware.
III. Interrupções de temporizador ajudam sistemas multitarefa a alternar a execução.

Está correto apenas o que se afirma em:

A) I e II
B) II e III
C) I, II e III
D) I e III

### Questão 9

Um programa trabalha com endereços virtuais, e o hardware/SO traduz esses endereços para posições reais na RAM. Essa descrição se refere a:

A) codificação ASCII de caracteres.
B) barramento de controle substituindo a RAM.
C) memória virtual com tradução para endereços físicos.
D) armazenamento permanente por firmware.

### Questão 10

No modo de endereçamento imediato, o operando:

A) fica exclusivamente em registrador indicado indiretamente.
B) aparece na própria instrução.
C) é obrigatoriamente buscado em uma tabela de páginas.
D) é sempre recuperado de um arquivo no SSD.

### Questão 11

Um projeto em C possui três arquivos-fonte compilados separadamente, mas um módulo chama função definida em outro. A etapa responsável por resolver referências entre módulos e bibliotecas é:

A) ligação, realizada pelo linker.
B) interpretação linha a linha.
C) paginação por demanda.
D) cache write-back.

### Questão 12

Assinale a alternativa correta sobre compiladores e interpretadores.

A) O interpretador sempre gera executável nativo independente antes de qualquer execução.
B) O compilador só existe em sistemas operacionais Linux.
C) O interpretador é um componente físico obrigatório da CPU.
D) O compilador traduz o código antes da execução; o interpretador executa/traduz de modo incremental durante a execução.

### Questão 13

Um analista observa que determinado algoritmo acessa repetidamente posições próximas de um vetor. Esse comportamento tende a favorecer:

A) substituição da ULA pela memória cache.
B) conversão automática de binário para Unicode.
C) localidade espacial e melhor aproveitamento de cache.
D) eliminação da necessidade de memória RAM.

### Questão 14

Considere as afirmações sobre representação de caracteres.

I. Caracteres são representados internamente por códigos numéricos.
II. ASCII é suficiente para representar, de forma ampla, todos os caracteres de todos os idiomas modernos.
III. Unicode tem objetivo mais abrangente que o ASCII.

Está correto apenas o que se afirma em:

A) I, II e III
B) I e III
C) I e II
D) II e III

### Questão 15

Um processador de 64 bits é assim chamado, em termos gerais, por características relacionadas:

A) à largura de palavra, registradores e endereçamento, conforme a arquitetura.
B) à quantidade fixa de 64 núcleos físicos.
C) à velocidade mínima de internet de 64 Mbps.
D) ao tamanho obrigatório de 64 GB de RAM.

### Questão 16

Assinale a alternativa incorreta sobre barramentos em arquitetura de computadores.

A) O barramento de endereços indica a posição a ser acessada.
B) O barramento de controle carrega sinais de coordenação, como leitura e escrita.
C) O barramento de endereços é o responsável por executar operações aritméticas.
D) O barramento de dados transporta conteúdo entre componentes.

### Questão 17

Em uma arquitetura com pipeline, a vantagem esperada é:

A) eliminar dependências de dados entre instruções.
B) substituir a memória cache por registradores.
C) aumentar a vazão ao sobrepor etapas de instruções.
D) garantir que cada instrução individual sempre tenha latência menor.

### Questão 18

Uma falha de cache, ou cache miss, ocorre quando:

A) o programa é compilado sem bibliotecas externas.
B) o dado procurado não está na cache e precisa ser buscado em nível inferior da hierarquia.
C) a CPU encontra o dado na cache L1.
D) o sistema operacional desliga a RAM por segurança.

### Questão 19

Assinale a alternativa correta sobre ponto flutuante.

A) Números reais podem ser representados de forma aproximada, com possibilidade de erro de arredondamento.
B) Todo número decimal com casas fracionárias é representado exatamente.
C) Ponto flutuante é usado apenas para armazenar caracteres Unicode.
D) Erros de arredondamento são impossíveis em computação digital.

### Questão 20

Em complemento de dois, uma característica importante é:

A) eliminar a necessidade de bit de sinal ou codificação equivalente.
B) representar apenas números positivos.
C) ser uma técnica exclusiva de codificação de textos.
D) facilitar operações aritméticas com inteiros negativos no hardware.

### Questão 21

Um arquivo executável já ligado precisa ser colocado na memória para iniciar sua execução. Essa etapa é realizada pelo:

A) montador, que traduz assembly para máquina.
B) pré-processador, que executa o programa final.
C) carregador, ou loader.
D) linker, que já resolveu referências antes.

### Questão 22

Uma palavra de máquina de 32 bits possui quantos bytes?

A) 32 bytes.
B) 4 bytes.
C) 2 bytes.
D) 8 bytes.

### Questão 23

Em um relatório técnico, throughput e latência foram usados como métricas de desempenho. A interpretação correta é:

A) throughput mede trabalho por unidade de tempo; latência mede tempo de resposta/espera.
B) throughput e latência são sinônimos perfeitos.
C) latência mede apenas capacidade de disco em GB.
D) throughput mede exclusivamente temperatura da CPU.

### Questão 24

Considere uma instrução hipotética MOV R1, #5, na qual #5 representa o valor literal a ser carregado. Esse exemplo ilustra:

A) endereçamento indireto por memória.
B) paginação por demanda.
C) DMA de dispositivo.
D) endereçamento imediato.

### Questão 25

Um dispositivo de E/S transfere dados para a memória com menor intervenção da CPU. Esse mecanismo é conhecido como:

A) linkedição dinâmica.
B) codificação ASCII.
C) DMA, acesso direto à memória.
D) ULA vetorial.

### Questão 26

Assinale a alternativa correta sobre firmware.

A) É uma política de escalonamento de processos.
B) É software de baixo nível associado ao controle de hardware ou dispositivo.
C) É sempre um aplicativo de usuário instalado no navegador.
D) É sinônimo de memória RAM volátil.

### Questão 27

Um analista compara memórias e afirma: “quanto mais próximo da CPU, em geral, menor a capacidade e maior a velocidade”. A afirmação está:

A) correta para a hierarquia típica de registradores/cache/RAM/armazenamento.
B) incorreta, pois SSD é sempre menor e mais rápido que cache.
C) incorreta, pois registradores são os maiores armazenamentos do computador.
D) correta apenas quando não existe cache.

### Questão 28

V/F: Sobre representação de dados, marque a sequência correta.

I. Um bit pode assumir, em computação digital clássica, os valores 0 ou 1.
II. Um byte é composto por 4 bits.
III. Um caractere pode ser representado por um código numérico.

A sequência correta é:

A) V, V, F.
B) F, V, V.
C) F, F, V.
D) V, F, V.

### Questão 29

Um sistema de 64 bits pode endereçar espaços maiores que um sistema de 32 bits, em tese, porque:

A) o sistema elimina a necessidade de memória virtual.
B) o barramento de controle deixa de existir.
C) a largura de endereçamento permite representar mais endereços distintos.
D) o clock do processador é obrigatoriamente 64 vezes maior.

### Questão 30

Assinale a incorreta sobre execução de instruções em uma CPU.

A) A CPU executa instruções sem qualquer uso de registradores.
B) A etapa de busca obtém uma instrução da memória.
C) A etapa de decodificação interpreta qual operação deve ser realizada.
D) A execução pode envolver a ULA, registradores e acesso à memória.

### Questão 31

Um administrador observa que um programa acessa repetidamente o mesmo valor em curto intervalo. Esse comportamento exemplifica:

A) localidade temporal.
B) localidade espacial apenas.
C) interrupção mascarável.
D) endereçamento por registrador obrigatório.

### Questão 32

Em computação, a expressão “programa armazenado” associada à arquitetura de von Neumann indica que:

A) programas nunca usam memória principal.
B) dados ficam apenas em dispositivos de entrada.
C) a CPU deixa de buscar instruções.
D) instruções e dados podem residir na memória para serem processados pela CPU.

### Questão 33

Uma rotina em assembly é traduzida para código de máquina por um:

A) loader, que carrega o executável em memória.
B) escalonador, que escolhe processo para CPU.
C) montador, ou assembler.
D) linker, que apenas resolve referências entre objetos.

### Questão 34

Em um cenário de suporte, um usuário pergunta por que aumentar a RAM pode melhorar desempenho quando há muitas aplicações abertas. A explicação mais adequada é:

A) mais RAM elimina a necessidade de sistema operacional.
B) mais RAM pode reduzir paginação/swap e permitir manter mais dados de processos em memória principal.
C) mais RAM aumenta automaticamente a frequência da CPU.
D) mais RAM transforma SSD em cache L1.

### Questão 35

Uma CPU usa registradores para armazenar temporariamente operandos e resultados intermediários. Essa afirmação está:

A) correta, pois registradores são pequenos e muito rápidos.
B) incorreta, pois registradores ficam apenas no SSD.
C) incorreta, pois registradores só armazenam arquivos permanentes.
D) correta apenas em computadores sem memória cache.

### Questão 36

Assinale a alternativa que apresenta somente memórias voláteis ou tipicamente temporárias no processamento.

A) SSD, HD e fita magnética.
B) DVD, SSD e ROM de firmware.
C) HD, RAM e fita magnética.
D) Registradores, cache e RAM.

### Questão 37

Uma interrupção mascarável é, em termos gerais, aquela que:

A) representa apenas erro lógico de programação.
B) é sinônimo de cache miss.
C) pode ser temporariamente desabilitada ou adiada pelo processador/SO em certas condições.
D) nunca pode ser ignorada em nenhuma circunstância.

### Questão 38

Ao avaliar desempenho, um analista conclui que a largura de banda da memória indica:

A) quantidade de instruções da linguagem SQL.
B) quantidade de dados que pode ser transferida por unidade de tempo.
C) tempo mínimo de resposta de um único acesso, exclusivamente.
D) número máximo de usuários cadastrados no sistema.

### Questão 39

Em um número hexadecimal, as letras A, B, C, D, E e F correspondem, respectivamente, aos valores decimais:

A) 10, 11, 12, 13, 14 e 15.
B) 11, 12, 13, 14, 15 e 16.
C) 1, 2, 3, 4, 5 e 6.
D) 16, 17, 18, 19, 20 e 21.

### Questão 40

Um periférico solicita atenção da CPU após concluir operação de leitura. A vantagem do uso de interrupção nesse caso é:

A) impedir qualquer multitarefa no sistema.
B) transformar o periférico em memória principal.
C) dispensar todos os drivers de dispositivo.
D) evitar que a CPU consulte continuamente o dispositivo para saber se terminou.

### Questão 41

Em uma arquitetura com cache write-back, a escrita modificada pode:

A) ser descartada porque cache nunca armazena dados alterados.
B) eliminar a necessidade de coerência de cache.
C) ser mantida temporariamente na cache e atualizada na memória principal posteriormente.
D) ser sempre escrita simultaneamente na RAM a cada alteração.

### Questão 42

Considere um sistema com barramento de dados de 64 bits. Isso significa que, em uma transferência, o barramento pode transportar:

A) 64 GB de armazenamento permanente.
B) 64 bits de dados por operação/ciclo de transferência, conforme a arquitetura.
C) 64 endereços físicos obrigatoriamente.
D) 64 programas simultâneos, sempre.

### Questão 43

Quando se diz que um byte pode assumir 256 combinações, o intervalo sem sinal mais comum é:

A) 0 a 255.
B) 1 a 256.
C) 0 a 256.
D) -128 a 255.

### Questão 44

Em uma linguagem compilada tradicional, se uma biblioteca externa não é encontrada durante a geração do executável, o erro tende a ocorrer na etapa de:

A) digitação do código-fonte pela CPU.
B) execução de ULA para soma inteira.
C) conversão de ASCII para Unicode.
D) ligação.

### Questão 45

Assinale a alternativa correta sobre ROM e RAM.

A) RAM é apenas leitura, e ROM é leitura e escrita livre em toda execução.
B) ROM substitui registradores durante cálculos da ULA.
C) ROM é tipicamente não volátil; RAM é volátil e usada na execução de programas.
D) ROM e RAM são sempre voláteis e equivalentes.

### Questão 46

Uma rotina que executa muitas operações aritméticas, mas acessa pouco disco, tende a ser limitada principalmente por:

A) regência verbal.
B) processamento de CPU.
C) latência de impressora.
D) normalização de banco.

### Questão 47

Um sistema embarcado usa firmware para inicializar dispositivo e carregar configurações básicas. A afirmação mais adequada é:

A) firmware atua em nível baixo e pode inicializar/controlar hardware antes do sistema completo.
B) firmware só existe depois que o usuário abre o editor de texto.
C) firmware é sempre armazenado apenas em RAM volátil.
D) firmware é um tipo de consulta agregada.

### Questão 48

Em arquitetura de computadores, a principal função dos registradores de propósito geral é:

A) guardar permanentemente todos os arquivos do usuário.
B) substituir o sistema de arquivos.
C) controlar diretamente o registro profissional no CRA.
D) armazenar temporariamente operandos, endereços ou resultados usados pela CPU.

### Questão 49

Uma operação de polling contínuo para verificar se um dispositivo terminou uma tarefa tende a ser menos eficiente que interrupções porque:

A) polling é sinônimo de memória cache L2.
B) interrupções impedem qualquer retorno ao processo anterior.
C) a CPU gasta tempo verificando repetidamente o dispositivo, mesmo sem novo evento.
D) o dispositivo deixa de existir quando não há interrupção.

### Questão 50

Em uma conversão rápida, o hexadecimal B7 equivale em decimal a:

A) 117.
B) 183.
C) 177.
D) 187.

## Questões extras de revisão fixa do Dia 1

#### Extra Dia 1.1

**Área:** Legislação CRA/CFA.

Um candidato confundiu a atuação do CFA com a do CRA-PR. Considerando a estrutura do Sistema CFA/CRAs, assinale a alternativa correta.

A) O CRA-PR pode deixar de observar as normas gerais do CFA quando editar regra interna própria.
B) Pessoa jurídica que explora atividade típica de Administração nunca se sujeita a registro no Sistema CFA/CRAs.
C) O CFA atua em plano nacional e normativo; o CRA-PR exerce registro e fiscalização no âmbito regional do Paraná.
D) A fiscalização do CRA depende sempre de provocação prévia de outro órgão público.

#### Extra Dia 1.2

**Área:** Legislação CRA/CFA.

Sobre a Lei Federal nº 4.769/1965, assinale a alternativa correta.

A) O CFA executa ordinariamente o registro profissional de todos os administradores no Paraná.
B) O Regimento Interno substitui a lei federal que disciplina a profissão.
C) Emprestar o registro a terceiro é irregular apenas quando houver prejuízo financeiro comprovado.
D) A lei é uma base legal do exercício da profissão de Administrador e da organização do Sistema CFA/CRAs.

#### Extra Dia 1.3

**Área:** Legislação CRA/CFA.

Na leitura da legislação específica, um aluno separou lei e decreto. Assinale a alternativa correta.

A) O Decreto nº 61.934/1967 regulamenta a Lei nº 4.769/1965.
B) A norma indicada no edital pode ser trocada por resolução mais recente sem retificação oficial.
C) Sigilo profissional é faculdade do registrado e pode ser afastado por conveniência comercial.
D) Anuidade, taxa e cobrança administrativa são temas alheios aos conselhos profissionais.

#### Extra Dia 1.4

**Área:** Legislação CRA/CFA.

O edital cobra Regimento Interno do CRA-PR. Sobre sua função, assinale a alternativa correta.

A) Pessoa jurídica que explora atividade típica de Administração nunca se sujeita a registro no Sistema CFA/CRAs.
B) O Regimento Interno organiza órgãos, competências e funcionamento do CRA-PR.
C) A fiscalização do CRA depende sempre de provocação prévia de outro órgão público.
D) A RN CFA nº 651/2024 deve ser estudada como Código de Ética.

#### Extra Dia 1.5

**Área:** Legislação CRA/CFA.

Sobre a natureza institucional do CRA-PR, conforme a apostila de estudo, assinale a alternativa correta.

A) O Regimento Interno substitui a lei federal que disciplina a profissão.
B) Emprestar o registro a terceiro é irregular apenas quando houver prejuízo financeiro comprovado.
C) O CRA-PR é tratado como autarquia com personalidade jurídica de direito público e autonomia administrativa.
D) O CRA-PR pode deixar de observar as normas gerais do CFA quando editar regra interna própria.

#### Extra Dia 1.6

**Área:** Legislação CRA/CFA.

A RN CFA nº 651/2024 foi citada no estudo da Semana 1. Assinale a alternativa correta.

A) Sigilo profissional é faculdade do registrado e pode ser afastado por conveniência comercial.
B) Anuidade, taxa e cobrança administrativa são temas alheios aos conselhos profissionais.
C) O CFA executa ordinariamente o registro profissional de todos os administradores no Paraná.
D) Ela foi usada como norma oficial que aprova o Regimento Interno do CRA-PR.

#### Extra Dia 1.7

**Área:** Legislação CRA/CFA.

Sobre o Código de Ética indicado no edital vigente, assinale a alternativa correta.

A) A apostila usa a RN CFA nº 671/2025 porque ela aparece no edital retificado e foi tratada como Código de Ética vigente.
B) A fiscalização do CRA depende sempre de provocação prévia de outro órgão público.
C) A RN CFA nº 651/2024 deve ser estudada como Código de Ética.
D) A norma indicada no edital pode ser trocada por resolução mais recente sem retificação oficial.

#### Extra Dia 1.8

**Área:** Legislação CRA/CFA.

Uma empresa presta serviços típicos de Administração no Paraná. Em relação ao Sistema CFA/CRAs, assinale a alternativa correta.

A) Emprestar o registro a terceiro é irregular apenas quando houver prejuízo financeiro comprovado.
B) A pessoa jurídica pode se sujeitar a registro e fiscalização quando atua em atividade abrangida pelo campo profissional.
C) O CRA-PR pode deixar de observar as normas gerais do CFA quando editar regra interna própria.
D) Pessoa jurídica que explora atividade típica de Administração nunca se sujeita a registro no Sistema CFA/CRAs.

#### Extra Dia 1.9

**Área:** Legislação CRA/CFA.

Um profissional registrado utiliza informações confidenciais de cliente para obter vantagem em outra contratação. Assinale a alternativa correta.

A) Anuidade, taxa e cobrança administrativa são temas alheios aos conselhos profissionais.
B) O CFA executa ordinariamente o registro profissional de todos os administradores no Paraná.
C) A conduta viola o dever de sigilo profissional, salvo hipótese legal ou justa causa que autorize a revelação.
D) O Regimento Interno substitui a lei federal que disciplina a profissão.

#### Extra Dia 1.10

**Área:** Legislação CRA/CFA.

Um administrador permite que terceiro use seu nome e registro para assinar trabalho que ele não acompanhou. Assinale a alternativa correta.

A) A RN CFA nº 651/2024 deve ser estudada como Código de Ética.
B) A norma indicada no edital pode ser trocada por resolução mais recente sem retificação oficial.
C) Sigilo profissional é faculdade do registrado e pode ser afastado por conveniência comercial.
D) Emprestar nome ou registro profissional pode caracterizar infração ética e uso indevido da habilitação.

#### Extra Dia 1.11

**Área:** Legislação CRA/CFA.

Em uma ação fiscalizatória, a empresa se recusa a apresentar documentos básicos sobre atividade profissional regulada. Assinale a alternativa correta.

A) Dificultar fiscalização regular pode ensejar apuração no âmbito competente do conselho.
B) O CRA-PR pode deixar de observar as normas gerais do CFA quando editar regra interna própria.
C) Pessoa jurídica que explora atividade típica de Administração nunca se sujeita a registro no Sistema CFA/CRAs.
D) A fiscalização do CRA depende sempre de provocação prévia de outro órgão público.

#### Extra Dia 1.12

**Área:** Legislação CRA/CFA.

Sobre a Lei nº 12.514/2011 na leitura dirigida, assinale a alternativa correta.

A) O CFA executa ordinariamente o registro profissional de todos os administradores no Paraná.
B) Ela é relevante por tratar de contribuições devidas aos conselhos profissionais.
C) O Regimento Interno substitui a lei federal que disciplina a profissão.
D) Emprestar o registro a terceiro é irregular apenas quando houver prejuízo financeiro comprovado.

#### Extra Dia 1.13

**Área:** Legislação CRA/CFA.

A RN CFA nº 649/2024 aparece na leitura dirigida da Semana 1. Assinale a alternativa correta.

A) A norma indicada no edital pode ser trocada por resolução mais recente sem retificação oficial.
B) Sigilo profissional é faculdade do registrado e pode ser afastado por conveniência comercial.
C) Ela deve ser estudada como regulamento de registro do Sistema CFA/CRAs.
D) Anuidade, taxa e cobrança administrativa são temas alheios aos conselhos profissionais.

#### Extra Dia 1.14

**Área:** Legislação CRA/CFA.

Sobre a RN CFA nº 670/2025, conforme a leitura dirigida da apostila, assinale a alternativa correta.

A) Pessoa jurídica que explora atividade típica de Administração nunca se sujeita a registro no Sistema CFA/CRAs.
B) A fiscalização do CRA depende sempre de provocação prévia de outro órgão público.
C) A RN CFA nº 651/2024 deve ser estudada como Código de Ética.
D) Ela deve ser lida em conjunto com a RN CFA nº 649/2024, pois altera o regulamento de registro.

#### Extra Dia 1.15

**Área:** Legislação CRA/CFA.

Quanto às normas RN CFA nº 546/2018, 626/2023 e 589/2020 no material da Semana 1, assinale a alternativa correta.

A) Quando o resumo completo estiver pendente, o estudo deve priorizar leitura oficial e evitar decorar prazo ou sanção sem confirmação.
B) O Regimento Interno substitui a lei federal que disciplina a profissão.
C) Emprestar o registro a terceiro é irregular apenas quando houver prejuízo financeiro comprovado.
D) O CRA-PR pode deixar de observar as normas gerais do CFA quando editar regra interna própria.

#### Extra Dia 1.16

**Área:** Língua Portuguesa/interpretação.

Leia o trecho: "O relatório foi enviado à Diretoria após a consolidação dos dados; por isso, a decisão foi adiada." A expressão "por isso" indica:

A) oposição entre envio do relatório e decisão adiada.
B) conclusão ou consequência em relação ao fato anterior.
C) explicação da causa sem relação com consequência.
D) adição de informação independente.

#### Extra Dia 1.17

**Área:** Língua Portuguesa/interpretação.

No trecho "A comissão revisou o edital e encaminhou suas conclusões", o pronome "suas" retoma:

A) as conclusões do edital.
B) as conclusões do candidato.
C) as conclusões da comissão.
D) as conclusões da banca e do órgão simultaneamente.

#### Extra Dia 1.18

**Área:** Língua Portuguesa/interpretação.

Assinale a reescrita que preserva o sentido de: "Somente os documentos conferidos serão encaminhados."

A) Todos os documentos, conferidos ou não, serão encaminhados.
B) Nenhum documento conferido será encaminhado.
C) Os documentos serão conferidos depois do encaminhamento.
D) Apenas os documentos conferidos serão encaminhados.

#### Extra Dia 1.19

**Área:** Língua Portuguesa/interpretação.

Assinale a alternativa em que a crase está corretamente empregada.

A) O processo foi encaminhado à unidade responsável.
B) O servidor começou à revisar os autos.
C) A equipe respondeu à todos os interessados.
D) O relatório foi enviado à setor técnico.

#### Extra Dia 1.20

**Área:** Língua Portuguesa/interpretação.

Leia: "Embora o sistema estivesse disponível, muitos usuários não concluíram o cadastro." A oração iniciada por "Embora" expressa:

A) causa direta.
B) concessão.
C) conclusão.
D) condição necessária.


## Gabarito do Dia 1

1. C
2. B
3. A
4. B
5. C
6. B
7. A
8. D
9. C
10. B
11. A
12. D
13. C
14. B
15. A
16. C
17. C
18. B
19. A
20. D
21. C
22. B
23. A
24. D
25. C
26. B
27. A
28. D
29. C
30. A
31. A
32. D
33. C
34. B
35. A
36. D
37. C
38. B
39. A
40. D
41. C
42. B
43. A
44. D
45. C
46. B
47. A
48. D
49. C
50. B

### Gabarito das questões extras de revisão fixa do Dia 1

Extra Dia 1.1: C
Extra Dia 1.2: D
Extra Dia 1.3: A
Extra Dia 1.4: B
Extra Dia 1.5: C
Extra Dia 1.6: D
Extra Dia 1.7: A
Extra Dia 1.8: B
Extra Dia 1.9: C
Extra Dia 1.10: D
Extra Dia 1.11: A
Extra Dia 1.12: B
Extra Dia 1.13: C
Extra Dia 1.14: D
Extra Dia 1.15: A
Extra Dia 1.16: B
Extra Dia 1.17: C
Extra Dia 1.18: D
Extra Dia 1.19: A
Extra Dia 1.20: B


## Comentários do Dia 1

### Comentário da Questão 1

- **Alternativa correta:** C.
- **A) está errada:** 53 inclui peso que não está marcado no binário apresentado.
- **B) está errada:** 64 seria 2^6, mas 101101 possui composição posicional, não apenas quantidade de bits.
- **C) está correta:** 101101₂ = 32 + 8 + 4 + 1 = 45.
- **D) está errada:** 37 resulta de ignorar o bit de peso 8; a soma posicional fica incompleta.
- **Conceito cobrado:** Conversão de binário para decimal.
- **Pegadinha usada:** Confundir potência de dois com valor posicional..
- **Como pensar para acertar:** Escreva os pesos 32, 16, 8, 4, 2 e 1 e some apenas os que têm bit 1.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 2

- **Alternativa correta:** B.
- **A) está errada:** FF corresponderia a 1111 1111, não a 1111 0000.
- **B) está correta:** Cada quarteto vira um dígito hexadecimal: 1111 = F e 0000 = 0.
- **C) está errada:** 0F inverte a ordem dos quartetos; a ordem deve ser preservada.
- **D) está errada:** E corresponde a 1110, não a 1111.
- **Conceito cobrado:** Conversão binário-hexadecimal.
- **Pegadinha usada:** Inverter quartetos ou trocar F por E..
- **Como pensar para acertar:** Separe o byte em grupos de quatro bits da esquerda para a direita.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 3

- **Alternativa correta:** A.
- **A) está correta:** I e II estão corretas; com 8 bits há 2^8 combinações.
- **B) está errada:** III está errada: o maior valor sem sinal é 255 porque a contagem começa em 0.
- **C) está errada:** I é verdadeira e III é falsa; a alternativa exclui uma correta e inclui uma incorreta.
- **D) está errada:** Inclui III, que confunde quantidade de combinações com maior valor.
- **Conceito cobrado:** Bits, bytes e representação sem sinal.
- **Pegadinha usada:** Confundir 256 combinações com maior valor 256..
- **Como pensar para acertar:** Separe “quantidade de valores” de “maior valor possível”.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 4

- **Alternativa correta:** B.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Essa afirmação está correta: registradores estão no topo da hierarquia.
- **B) é a incorreta:** Essa é a incorreta: SSD é persistente, mas fica muito abaixo de registradores e cache em velocidade.
- **C) está correta como afirmação:** Essa afirmação está correta: RAM perde dados sem energia e apoia execução.
- **D) está correta como afirmação:** Essa afirmação está correta: cache reduz o tempo médio de acesso.
- **Conceito cobrado:** Hierarquia de memória.
- **Pegadinha usada:** Trocar persistência por velocidade..
- **Como pensar para acertar:** Ordene mentalmente: registradores, cache, RAM, SSD/HD.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 5

- **Alternativa correta:** C.
- **A) está errada:** O barramento de endereços indica posições de acesso, não executa operações.
- **B) está errada:** SSD/HD armazenam dados de forma persistente, mas não executam operações da CPU.
- **C) está correta:** A unidade lógica e aritmética executa operações aritméticas e lógicas.
- **D) está errada:** A unidade de controle coordena a execução, mas não é o bloco responsável pelo cálculo em si.
- **Conceito cobrado:** Componentes da CPU.
- **Pegadinha usada:** Confundir coordenação da instrução com execução aritmética..
- **Como pensar para acertar:** Associe cálculo e lógica à ULA; coordenação à unidade de controle.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 6

- **Alternativa correta:** B.
- **A) está errada:** A volatilidade da RAM independe do sistema operacional.
- **B) está correta:** RAM apoia execução, mas perde dados sem energia; persistência exige armazenamento não volátil.
- **C) está errada:** Velocidade não implica persistência; cache e RAM são rápidas e voláteis.
- **D) está errada:** A largura da arquitetura não transforma RAM em armazenamento permanente.
- **Conceito cobrado:** RAM e armazenamento secundário.
- **Pegadinha usada:** Associar velocidade a persistência..
- **Como pensar para acertar:** Pergunte: o dado permanece após desligar? Se não, não é armazenamento permanente.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 7

- **Alternativa correta:** A.
- **A) está correta:** A interrupção avisa a CPU de evento que demanda tratamento.
- **B) está errada:** Compilação traduz código-fonte; não sinaliza eventos de dispositivo.
- **C) está errada:** Paginação gerencia memória virtual; não é aviso de dispositivo.
- **D) está errada:** Normalização é técnica de banco de dados, sem relação com sinalização da CPU.
- **Conceito cobrado:** Interrupções de hardware.
- **Pegadinha usada:** Tratar interrupção como erro ou como etapa de tradução..
- **Como pensar para acertar:** Interrupção é aviso/evento; nem sempre é falha.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 8

- **Alternativa correta:** D.
- **A) está errada:** II é falsa porque interrupção não é necessariamente falha.
- **B) está errada:** II é falsa e I também deveria estar incluída.
- **C) está errada:** Inclui II, que usa generalização indevida.
- **D) está correta:** I e III estão corretas; interrupções atendem eventos e temporizador apoia escalonamento.
- **Conceito cobrado:** Interrupções e multitarefa.
- **Pegadinha usada:** A palavra “toda” torna a assertiva II falsa..
- **Como pensar para acertar:** Classifique interrupção como mecanismo de controle de eventos, não como sinônimo de erro.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 9

- **Alternativa correta:** C.
- **A) está errada:** ASCII codifica caracteres, não endereços de memória.
- **B) está errada:** Barramento de controle coordena sinais; não substitui a memória.
- **C) está correta:** O processo enxerga endereço virtual, que é convertido para endereço físico.
- **D) está errada:** Firmware controla dispositivo; não descreve tradução de endereços de processo.
- **Conceito cobrado:** Endereço virtual e endereço físico.
- **Pegadinha usada:** Confundir endereço virtual com arquivo em disco..
- **Como pensar para acertar:** Procure a relação processo -> endereço virtual -> tradução -> RAM física.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 10

- **Alternativa correta:** B.
- **A) está errada:** Isso descreve outra forma de endereçamento, não o imediato.
- **B) está correta:** O valor é fornecido diretamente na instrução, como em uma movimentação de constante.
- **C) está errada:** Tabela de páginas pertence à tradução de memória virtual, não ao modo imediato em si.
- **D) está errada:** O modo imediato não exige armazenamento secundário.
- **Conceito cobrado:** Modos de endereçamento.
- **Pegadinha usada:** Misturar endereçamento de instrução com memória virtual..
- **Como pensar para acertar:** A palavra “imediato” sugere que o valor está diretamente na instrução.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 11

- **Alternativa correta:** A.
- **A) está correta:** O linker combina objetos e resolve referências externas.
- **B) está errada:** Interpretação executa/traduz durante a execução; não resolve módulos compilados.
- **C) está errada:** Paginação trata memória virtual, não montagem de executável.
- **D) está errada:** Write-back é política de cache, não etapa de construção de programa.
- **Conceito cobrado:** Compilador, linker e loader.
- **Pegadinha usada:** Confundir compilador com linker..
- **Como pensar para acertar:** Pense no fluxo: compilar arquivos, ligar objetos, carregar em memória, executar.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 12

- **Alternativa correta:** D.
- **A) está errada:** Essa descrição se aproxima mais de compilação tradicional.
- **B) está errada:** Compiladores existem em diferentes sistemas operacionais.
- **C) está errada:** Interpretador é software/ambiente de execução, não componente físico da CPU.
- **D) está correta:** Essa é a distinção clássica cobrada em concursos.
- **Conceito cobrado:** Tradução de programas.
- **Pegadinha usada:** Transformar diferença conceitual em diferença de sistema operacional..
- **Como pensar para acertar:** Compare quando a tradução acontece: antes ou durante a execução.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 13

- **Alternativa correta:** C.
- **A) está errada:** Cache armazena dados; ULA executa operações.
- **B) está errada:** Localidade de referência não trata codificação de caracteres.
- **C) está correta:** Acesso a posições próximas aumenta chance de linhas de cache úteis.
- **D) está errada:** Cache melhora desempenho, mas não elimina RAM.
- **Conceito cobrado:** Cache e localidade de referência.
- **Pegadinha usada:** Achar que cache muda a função da CPU..
- **Como pensar para acertar:** Associe repetição/proximidade de acessos a localidade temporal/espacial.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 14

- **Alternativa correta:** B.
- **A) está errada:** Inclui II, que superestima o ASCII.
- **B) está correta:** I e III estão corretas; Unicode é mais amplo que ASCII.
- **C) está errada:** II é falsa porque ASCII é limitado.
- **D) está errada:** II é falsa e I também deveria estar incluída.
- **Conceito cobrado:** Codificação de caracteres.
- **Pegadinha usada:** Confundir ASCII com Unicode..
- **Como pensar para acertar:** Lembre que texto também é dado codificado numericamente.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 15

- **Alternativa correta:** A.
- **A) está correta:** A expressão envolve capacidades naturais de processamento/endereçamento da arquitetura.
- **B) está errada:** 64 bits não significa possuir 64 núcleos.
- **C) está errada:** Bits da arquitetura não são taxa de rede.
- **D) está errada:** Arquitetura de 64 bits não impõe esse tamanho de RAM.
- **Conceito cobrado:** Arquitetura de 32/64 bits.
- **Pegadinha usada:** Associar bits da arquitetura a núcleos, internet ou memória instalada..
- **Como pensar para acertar:** Veja o contexto: largura interna/endereçamento, não quantidade de componentes.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 16

- **Alternativa correta:** C.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: ele transporta informação de localização.
- **B) está correta como afirmação:** Correta: controle coordena operações.
- **C) é a incorreta:** Incorreta: operações aritméticas são executadas pela ULA, não pelo barramento de endereços.
- **D) está correta como afirmação:** Correta: dados trafegam pelo barramento de dados.
- **Conceito cobrado:** Barramentos.
- **Pegadinha usada:** Atribuir função de processamento ao meio de comunicação..
- **Como pensar para acertar:** Separe transportar dados, indicar endereço e controlar operação.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 17

- **Alternativa correta:** C.
- **A) está errada:** Dependências podem causar hazards; o pipeline não as elimina por definição.
- **B) está errada:** Pipeline é técnica de execução, não substituição de memória.
- **C) está correta:** Pipelining permite que diferentes instruções ocupem etapas distintas simultaneamente.
- **D) está errada:** Pipeline melhora vazão, mas uma instrução isolada não necessariamente fica com menor latência.
- **Conceito cobrado:** Pipeline de CPU.
- **Pegadinha usada:** Confundir vazão com latência individual..
- **Como pensar para acertar:** Pense em linha de produção: mais itens por tempo, não necessariamente item isolado mais rápido.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 18

- **Alternativa correta:** B.
- **A) está errada:** Não se relaciona ao conteúdo da cache.
- **B) está correta:** Essa é a definição de cache miss.
- **C) está errada:** Isso seria cache hit, não miss.
- **D) está errada:** Não é conceito de cache.
- **Conceito cobrado:** Cache hit e cache miss.
- **Pegadinha usada:** Trocar hit por miss..
- **Como pensar para acertar:** Pergunte: encontrou na cache? Se sim, hit; se não, miss.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 19

- **Alternativa correta:** A.
- **A) está correta:** Representação de ponto flutuante é finita e pode aproximar valores.
- **B) está errada:** Muitos valores decimais não têm representação binária finita exata.
- **C) está errada:** Caracteres e números reais usam representações diferentes.
- **D) está errada:** A limitação de precisão torna arredondamento possível.
- **Conceito cobrado:** Representação de ponto flutuante.
- **Pegadinha usada:** Usar “todo” e “impossível” em tema de precisão..
- **Como pensar para acertar:** Lembre que a representação é finita; nem todo real cabe exatamente.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 20

- **Alternativa correta:** D.
- **A) está errada:** O sinal continua representado pelo padrão de bits.
- **B) está errada:** Complemento de dois representa positivos e negativos.
- **C) está errada:** É técnica de representação numérica, não textual.
- **D) está correta:** Complemento de dois é a forma usual para inteiros com sinal.
- **Conceito cobrado:** Inteiros com sinal.
- **Pegadinha usada:** Tratar complemento de dois como texto ou como eliminação do sinal..
- **Como pensar para acertar:** Associe complemento de dois a inteiros negativos e aritmética binária.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 21

- **Alternativa correta:** C.
- **A) está errada:** O assembler traduz linguagem de montagem.
- **B) está errada:** Pré-processamento não é execução/carregamento.
- **C) está correta:** O loader carrega e prepara o programa em memória.
- **D) está errada:** O linker atua antes, combinando objetos e bibliotecas.
- **Conceito cobrado:** Loader.
- **Pegadinha usada:** Confundir linker e loader..
- **Como pensar para acertar:** No fluxo clássico, ligar vem antes de carregar; carregar vem antes de executar.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 22

- **Alternativa correta:** B.
- **A) está errada:** Confunde a quantidade de bits com bytes.
- **B) está correta:** 32 bits divididos por 8 bits por byte resultam em 4 bytes.
- **C) está errada:** 2 bytes correspondem a 16 bits.
- **D) está errada:** 8 bytes correspondem a 64 bits.
- **Conceito cobrado:** Bits e bytes.
- **Pegadinha usada:** Não converter bit para byte..
- **Como pensar para acertar:** Divida a quantidade de bits por 8.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 23

- **Alternativa correta:** A.
- **A) está correta:** Vazão e tempo de resposta são métricas diferentes.
- **B) está errada:** Maior vazão não significa necessariamente menor latência.
- **C) está errada:** Latência é tempo, não capacidade.
- **D) está errada:** Throughput mede produção/vazão, não temperatura.
- **Conceito cobrado:** Métricas de desempenho.
- **Pegadinha usada:** Confundir vazão com tempo de resposta..
- **Como pensar para acertar:** Pergunte: é quantidade produzida ou tempo para responder?
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 24

- **Alternativa correta:** D.
- **A) está errada:** No indireto, a instrução aponta para local que contém o endereço do operando.
- **B) está errada:** Paginação é técnica de memória virtual, não modo da instrução.
- **C) está errada:** DMA trata transferência de E/S, não operando imediato.
- **D) está correta:** O operando literal está codificado na própria instrução.
- **Conceito cobrado:** Modos de endereçamento.
- **Pegadinha usada:** Não reconhecer o valor literal na instrução..
- **Como pensar para acertar:** Valor escrito diretamente na instrução indica imediato.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 25

- **Alternativa correta:** C.
- **A) está errada:** Ligação dinâmica trata bibliotecas, não transferência de dispositivo.
- **B) está errada:** ASCII codifica caracteres, não transfere blocos de E/S.
- **C) está correta:** DMA permite transferência entre dispositivo e memória sem CPU mover cada byte.
- **D) está errada:** ULA executa operações; não é mecanismo de E/S.
- **Conceito cobrado:** Entrada/saída e DMA.
- **Pegadinha usada:** Confundir mecanismo de E/S com processamento ou tradução de código..
- **Como pensar para acertar:** Procure “dispositivo para memória com pouca CPU”: isso sugere DMA.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 26

- **Alternativa correta:** B.
- **A) está errada:** Escalonamento é função de sistema operacional.
- **B) está correta:** Firmware fica embarcado/associado a dispositivos e fornece controle básico.
- **C) está errada:** Aplicativos de usuário não são firmware por definição.
- **D) está errada:** Firmware é software; RAM é memória principal volátil.
- **Conceito cobrado:** Firmware.
- **Pegadinha usada:** Tratar firmware como hardware puro ou aplicativo comum..
- **Como pensar para acertar:** Firmware fica entre hardware e software, mas continua sendo software.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 27

- **Alternativa correta:** A.
- **A) está correta:** Memórias próximas da CPU tendem a ser mais rápidas e menores.
- **B) está errada:** SSD costuma ser maior e mais lento que cache.
- **C) está errada:** Registradores são pequenos e muito rápidos.
- **D) está errada:** A afirmação justamente envolve cache na hierarquia.
- **Conceito cobrado:** Hierarquia de memória.
- **Pegadinha usada:** Inverter capacidade e velocidade..
- **Como pensar para acertar:** Pense em custo por bit: quanto mais rápido e próximo, menor tende a ser.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 28

- **Alternativa correta:** D.
- **A) está errada:** II está errada e III está correta.
- **B) está errada:** I está errada nessa alternativa, mas bit digital clássico é 0 ou 1.
- **C) está errada:** I deveria ser verdadeira.
- **D) está correta:** I é verdadeira; II é falsa porque byte tem 8 bits; III é verdadeira.
- **Conceito cobrado:** Representação de dados.
- **Pegadinha usada:** Trocar byte por quarteto de bits..
- **Como pensar para acertar:** Teste cada frase de forma independente.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 29

- **Alternativa correta:** C.
- **A) está errada:** Sistemas de 64 bits também podem usar memória virtual.
- **B) está errada:** Barramentos continuam existindo conforme a arquitetura.
- **C) está correta:** Mais bits de endereço significam mais combinações possíveis.
- **D) está errada:** Bits de arquitetura não determinam multiplicação de clock.
- **Conceito cobrado:** Endereçamento em arquiteturas.
- **Pegadinha usada:** Confundir largura de endereço com clock..
- **Como pensar para acertar:** Mais bits significam mais combinações de endereços.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 30

- **Alternativa correta:** A.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) é a incorreta:** Incorreta: registradores são fundamentais para operação interna da CPU.
- **B) está correta como afirmação:** Correta: a CPU busca instruções para executar.
- **C) está correta como afirmação:** Correta: decodificação entende a instrução.
- **D) está correta como afirmação:** Correta: depende da instrução.
- **Conceito cobrado:** Ciclo de instrução.
- **Pegadinha usada:** Ignorar registradores no ciclo de execução..
- **Como pensar para acertar:** Busque, decodifique e execute mentalmente; registradores aparecem no caminho.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 31

- **Alternativa correta:** A.
- **A) está correta:** Reuso de um mesmo dado em intervalo curto caracteriza localidade temporal.
- **B) está errada:** Localidade espacial envolve endereços próximos, não necessariamente o mesmo dado.
- **C) está errada:** Interrupção é evento de controle, não padrão de acesso a dado.
- **D) está errada:** O padrão de acesso não implica obrigatoriamente esse modo de endereçamento.
- **Conceito cobrado:** Localidade temporal.
- **Pegadinha usada:** Confundir temporal com espacial..
- **Como pensar para acertar:** Temporal tem relação com tempo/reuso; espacial com vizinhança de endereços.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 32

- **Alternativa correta:** D.
- **A) está errada:** Contraria o conceito de programa armazenado.
- **B) está errada:** Dados podem estar na memória e no armazenamento.
- **C) está errada:** A CPU continua buscando instruções para executar.
- **D) está correta:** A ideia central é armazenar o programa na memória.
- **Conceito cobrado:** Arquitetura de von Neumann.
- **Pegadinha usada:** Negar a presença de instruções na memória..
- **Como pensar para acertar:** A palavra-chave é memória armazenando instruções.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 33

- **Alternativa correta:** C.
- **A) está errada:** Loader prepara a execução, não traduz assembly.
- **B) está errada:** Escalonador é do sistema operacional.
- **C) está correta:** Assembler traduz linguagem de montagem para código de máquina.
- **D) está errada:** O linker não traduz assembly diretamente.
- **Conceito cobrado:** Assembler.
- **Pegadinha usada:** Confundir montador, linker e loader..
- **Como pensar para acertar:** Associe assembly a assembler/montador.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 34

- **Alternativa correta:** B.
- **A) está errada:** SO continua necessário para gerenciar recursos.
- **B) está correta:** Com mais memória física, o sistema tende a depender menos de armazenamento secundário para páginas.
- **C) está errada:** RAM não altera diretamente o clock do processador.
- **D) está errada:** São componentes diferentes da hierarquia.
- **Conceito cobrado:** RAM e desempenho.
- **Pegadinha usada:** Atribuir à RAM efeitos de CPU ou SO..
- **Como pensar para acertar:** Relacione muitas aplicações a pressão de memória e paginação.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 35

- **Alternativa correta:** A.
- **A) está correta:** Registradores armazenam temporariamente operandos, endereços e resultados usados diretamente pela CPU.
- **B) está errada:** Registradores pertencem à CPU, não ao SSD.
- **C) está errada:** Eles são temporários, não arquivos permanentes.
- **D) está errada:** Registradores existem mesmo com cache.
- **Conceito cobrado:** Registradores.
- **Pegadinha usada:** Confundir registradores de CPU com registros de arquivo/cadastro..
- **Como pensar para acertar:** Veja o contexto: CPU e operandos indicam registradores internos.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 36

- **Alternativa correta:** D.
- **A) está errada:** São meios de armazenamento persistente.
- **B) está errada:** Inclui meios não voláteis.
- **C) está errada:** Mistura RAM volátil com meios persistentes.
- **D) está correta:** Esses níveis são usados temporariamente durante o processamento.
- **Conceito cobrado:** Volatilidade e hierarquia.
- **Pegadinha usada:** Misturar RAM com armazenamento permanente..
- **Como pensar para acertar:** Separe memória de trabalho de armazenamento persistente.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 37

- **Alternativa correta:** C.
- **A) está errada:** Interrupções podem vir de hardware e eventos externos.
- **B) está errada:** Cache miss é evento de memória, não tipo de interrupção mascarável.
- **C) está correta:** Interrupções mascaráveis podem ser controladas conforme prioridade e contexto.
- **D) está errada:** Isso se aproxima de interrupção não mascarável.
- **Conceito cobrado:** Tipos de interrupção.
- **Pegadinha usada:** Confundir mascarável com não mascarável..
- **Como pensar para acertar:** Máscara sugere possibilidade de bloquear/adiar.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 38

- **Alternativa correta:** B.
- **A) está errada:** Não se relaciona a memória.
- **B) está correta:** Largura de banda mede taxa de transferência.
- **C) está errada:** Isso é mais próximo de latência.
- **D) está errada:** Não é métrica de memória.
- **Conceito cobrado:** Largura de banda de memória.
- **Pegadinha usada:** Confundir largura de banda com latência..
- **Como pensar para acertar:** Taxa de transferência é “quanto por tempo”; latência é “quanto demora”.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 39

- **Alternativa correta:** A.
- **A) está correta:** Hexadecimal usa 16 símbolos; A começa no valor 10.
- **B) está errada:** Desloca todos os valores em uma unidade.
- **C) está errada:** Confunde letras com ordem alfabética simples.
- **D) está errada:** Esses valores excedem um único dígito hexadecimal.
- **Conceito cobrado:** Base hexadecimal.
- **Pegadinha usada:** Achar que F vale 16..
- **Como pensar para acertar:** Lembre: os dígitos vão de 0 a 15.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 40

- **Alternativa correta:** D.
- **A) está errada:** Interrupções ajudam multitarefa, não impedem.
- **B) está errada:** Periférico continua sendo dispositivo de E/S.
- **C) está errada:** Drivers continuam necessários para controle adequado.
- **D) está correta:** Interrupções reduzem espera ativa/polling constante.
- **Conceito cobrado:** Interrupções e E/S.
- **Pegadinha usada:** Não perceber a diferença entre polling e interrupção..
- **Como pensar para acertar:** Evento concluído avisa a CPU em vez de a CPU ficar perguntando.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 41

- **Alternativa correta:** C.
- **A) está errada:** Cache pode armazenar linhas modificadas.
- **B) está errada:** Coerência continua sendo preocupação em sistemas com múltiplas caches.
- **C) está correta:** Write-back adia a escrita na memória até momento adequado.
- **D) está errada:** Isso descreve write-through, não write-back.
- **Conceito cobrado:** Políticas de escrita de cache.
- **Pegadinha usada:** Confundir write-back com write-through..
- **Como pensar para acertar:** Back sugere retorno posterior para a memória principal.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 42

- **Alternativa correta:** B.
- **A) está errada:** Largura de barramento não é capacidade de armazenamento.
- **B) está correta:** A largura do barramento de dados indica quantidade de bits transportados em paralelo.
- **C) está errada:** Endereço é função do barramento de endereços, não de dados.
- **D) está errada:** Número de programas não decorre diretamente da largura do barramento.
- **Conceito cobrado:** Barramento de dados.
- **Pegadinha usada:** Trocar largura do barramento por capacidade ou quantidade de programas..
- **Como pensar para acertar:** Pergunte: é barramento de dados, endereços ou controle?
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 43

- **Alternativa correta:** A.
- **A) está correta:** Há 256 valores porque o zero é contado.
- **B) está errada:** Esse intervalo tem 256 valores, mas não é o intervalo binário sem sinal usual.
- **C) está errada:** Esse intervalo teria 257 valores.
- **D) está errada:** Mistura representação com sinal e sem sinal incorretamente.
- **Conceito cobrado:** Intervalo sem sinal.
- **Pegadinha usada:** Esquecer o zero..
- **Como pensar para acertar:** Quantidade de combinações é 256; maior valor é 255.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 44

- **Alternativa correta:** D.
- **A) está errada:** CPU não digita nem valida biblioteca no código-fonte.
- **B) está errada:** ULA executa operações, não resolve biblioteca externa.
- **C) está errada:** Codificação de caracteres não resolve dependências de biblioteca.
- **D) está correta:** A resolução de símbolos externos e bibliotecas ocorre no linking.
- **Conceito cobrado:** Ligação de programas.
- **Pegadinha usada:** Atribuir erro de dependência ao compilador sempre, sem distinguir etapas..
- **Como pensar para acertar:** Se o problema é símbolo/biblioteca externa, pense em linker.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 45

- **Alternativa correta:** C.
- **A) está errada:** A sigla ROM remete a memória de leitura; RAM permite acesso de leitura/escrita.
- **B) está errada:** ROM não substitui registradores no processamento.
- **C) está correta:** A distinção central envolve persistência e função.
- **D) está errada:** ROM normalmente preserva conteúdo; RAM é volátil.
- **Conceito cobrado:** ROM e RAM.
- **Pegadinha usada:** Inverter siglas e propriedades..
- **Como pensar para acertar:** Associe ROM a firmware/não volatilidade e RAM a execução/volatilidade.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 46

- **Alternativa correta:** B.
- **A) está errada:** Não é tema técnico do cenário.
- **B) está correta:** Cálculo intensivo com pouca E/S tende a ser CPU-bound.
- **C) está errada:** O cenário não envolve impressão.
- **D) está errada:** Não há indicação de modelagem de dados.
- **Conceito cobrado:** CPU-bound.
- **Pegadinha usada:** Confundir gargalo de CPU com gargalo de E/S..
- **Como pensar para acertar:** Observe o recurso mais demandado no cenário.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 47

- **Alternativa correta:** A.
- **A) está correta:** Essa é função típica de firmware em dispositivos.
- **B) está errada:** Firmware é anterior e mais baixo nível que aplicativos de usuário.
- **C) está errada:** Firmware costuma ficar em memória não volátil.
- **D) está errada:** Consulta agregada é banco de dados, não firmware.
- **Conceito cobrado:** Firmware em sistemas embarcados.
- **Pegadinha usada:** Tratar firmware como aplicativo comum..
- **Como pensar para acertar:** Veja inicialização e controle básico de hardware: isso aponta para firmware.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 48

- **Alternativa correta:** D.
- **A) está errada:** Persistência de arquivos é função de armazenamento secundário.
- **B) está errada:** Sistema de arquivos é abstração do SO sobre armazenamento.
- **C) está errada:** Registro profissional é legislação, não arquitetura.
- **D) está correta:** Registradores apoiam a execução imediata de instruções.
- **Conceito cobrado:** Registradores de propósito geral.
- **Pegadinha usada:** Confundir “registro” técnico com cadastro profissional..
- **Como pensar para acertar:** Contexto CPU indica registradores internos, não registros administrativos.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 49

- **Alternativa correta:** C.
- **A) está errada:** Polling é técnica de consulta de estado, não cache.
- **B) está errada:** Após tratar a interrupção, o sistema pode retornar ao fluxo anterior.
- **C) está correta:** Polling pode desperdiçar ciclos de CPU em consultas repetidas.
- **D) está errada:** O dispositivo continua existindo; a diferença é o método de aviso.
- **Conceito cobrado:** Polling e interrupções.
- **Pegadinha usada:** Não perceber o custo de espera ativa..
- **Como pensar para acertar:** Compare “ficar perguntando” com “ser avisado quando acontecer”.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentário da Questão 50

- **Alternativa correta:** B.
- **A) está errada:** 117 ignora o peso posicional de base 16.
- **B) está correta:** B vale 11; B7 = 11 x 16 + 7 = 176 + 7 = 183.
- **C) está errada:** 177 resultaria de usar B como 10 e somar 17 indevidamente.
- **D) está errada:** 187 soma 11 x 16 com 11, como se 7 valesse 11.
- **Conceito cobrado:** Conversão hexadecimal-decimal.
- **Pegadinha usada:** Errar o valor da letra ou o peso 16..
- **Como pensar para acertar:** Transforme a letra em decimal e aplique valor posicional: dezena hexadecimal vale vezes 16.
- **Referência à apostila de estudo:** Dia 1 — Arquitetura e Organização de Computadores.

### Comentários das questões extras de revisão fixa do Dia 1

#### Comentário Extra Dia 1.1

- **Alternativa correta:** C.
- **A) está errada:** O CRA-PR tem autonomia administrativa, mas atua dentro do Sistema CFA/CRAs e não afasta a normatização geral do CFA.
- **B) está errada:** A pessoa jurídica pode estar sujeita a registro e fiscalização quando atua em campo abrangido pela Administração.
- **C) está correta:** A distinção central é nacional/normativo para o CFA e regional/executivo para o CRA.
- **D) está errada:** A fiscalização profissional é função típica do conselho regional e pode ocorrer no âmbito de sua competência.
- **Conceito cobrado:** Competência do CFA e do CRA-PR.
- **Pegadinha usada:** Trocar competência nacional por competência regional.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.2

- **Alternativa correta:** D.
- **A) está errada:** O registro e a fiscalização regional são atribuições dos CRAs; o CFA atua em plano nacional e normativo.
- **B) está errada:** Regimento organiza funcionamento interno; não substitui a lei federal nem o decreto regulamentador.
- **C) está errada:** O uso indevido de nome ou registro profissional já compromete a ética e a regularidade, independentemente de dano financeiro imediato.
- **D) está correta:** A Lei nº 4.769/1965 estrutura a profissão e sustenta a atuação dos conselhos.
- **Conceito cobrado:** Lei nº 4.769/1965.
- **Pegadinha usada:** Tratar a lei como norma meramente interna do CRA-PR.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.3

- **Alternativa correta:** A.
- **A) está correta:** O decreto detalha a execução da lei, por isso deve ser lido junto da Lei nº 4.769/1965.
- **B) está errada:** Para concurso, a base é o edital vigente; norma nova só substitui conteúdo se houver fonte oficial e pertinência ao edital.
- **C) está errada:** Sigilo é dever profissional, salvo hipótese legal, autorização legítima ou justa causa reconhecida.
- **D) está errada:** A Lei nº 12.514/2011 trata de contribuições devidas aos conselhos profissionais.
- **Conceito cobrado:** Decreto nº 61.934/1967.
- **Pegadinha usada:** Confundir norma regulamentadora com lei criadora.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.4

- **Alternativa correta:** B.
- **A) está errada:** A pessoa jurídica pode estar sujeita a registro e fiscalização quando atua em campo abrangido pela Administração.
- **B) está correta:** O Regimento é a referência interna para entender como o conselho regional se estrutura e decide.
- **C) está errada:** A fiscalização profissional é função típica do conselho regional e pode ocorrer no âmbito de sua competência.
- **D) está errada:** Na apostila, a RN CFA nº 651/2024 aparece como norma que aprova o Regimento Interno do CRA-PR; o Código de Ética é a RN CFA nº 671/2025.
- **Conceito cobrado:** Regimento Interno do CRA-PR.
- **Pegadinha usada:** Confundir regimento com código de ética.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.5

- **Alternativa correta:** C.
- **A) está errada:** Regimento organiza funcionamento interno; não substitui a lei federal nem o decreto regulamentador.
- **B) está errada:** O uso indevido de nome ou registro profissional já compromete a ética e a regularidade, independentemente de dano financeiro imediato.
- **C) está correta:** A apostila destaca o CRA-PR como autarquia de direito público no contexto do Sistema CFA/CRAs.
- **D) está errada:** O CRA-PR tem autonomia administrativa, mas atua dentro do Sistema CFA/CRAs e não afasta a normatização geral do CFA.
- **Conceito cobrado:** Natureza jurídica do CRA-PR.
- **Pegadinha usada:** Tratar conselho profissional como órgão sem personalidade própria.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.6

- **Alternativa correta:** D.
- **A) está errada:** Sigilo é dever profissional, salvo hipótese legal, autorização legítima ou justa causa reconhecida.
- **B) está errada:** A Lei nº 12.514/2011 trata de contribuições devidas aos conselhos profissionais.
- **C) está errada:** O registro e a fiscalização regional são atribuições dos CRAs; o CFA atua em plano nacional e normativo.
- **D) está correta:** A referência à RN 651/2024 serve para vincular o Regimento Interno à fonte oficial do CFA.
- **Conceito cobrado:** RN CFA nº 651/2024.
- **Pegadinha usada:** Atribuir à RN 651/2024 conteúdo de ética profissional.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.7

- **Alternativa correta:** A.
- **A) está correta:** A RN 671/2025 é a referência ética adotada no material aprovado para a Semana 1.
- **B) está errada:** A fiscalização profissional é função típica do conselho regional e pode ocorrer no âmbito de sua competência.
- **C) está errada:** Na apostila, a RN CFA nº 651/2024 aparece como norma que aprova o Regimento Interno do CRA-PR; o Código de Ética é a RN CFA nº 671/2025.
- **D) está errada:** Para concurso, a base é o edital vigente; norma nova só substitui conteúdo se houver fonte oficial e pertinência ao edital.
- **Conceito cobrado:** RN CFA nº 671/2025.
- **Pegadinha usada:** Usar automaticamente a RN 640/2024 apesar da retificação indicada.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.8

- **Alternativa correta:** B.
- **A) está errada:** O uso indevido de nome ou registro profissional já compromete a ética e a regularidade, independentemente de dano financeiro imediato.
- **B) está correta:** O foco da fiscalização não se limita à pessoa física quando a pessoa jurídica exerce atividade profissional regulada.
- **C) está errada:** O CRA-PR tem autonomia administrativa, mas atua dentro do Sistema CFA/CRAs e não afasta a normatização geral do CFA.
- **D) está errada:** A pessoa jurídica pode estar sujeita a registro e fiscalização quando atua em campo abrangido pela Administração.
- **Conceito cobrado:** Registro de pessoa jurídica.
- **Pegadinha usada:** Achar que apenas profissionais individuais podem ser fiscalizados.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.9

- **Alternativa correta:** C.
- **A) está errada:** A Lei nº 12.514/2011 trata de contribuições devidas aos conselhos profissionais.
- **B) está errada:** O registro e a fiscalização regional são atribuições dos CRAs; o CFA atua em plano nacional e normativo.
- **C) está correta:** O sigilo protege informações obtidas no exercício profissional e não pode ser afastado por conveniência pessoal.
- **D) está errada:** Regimento organiza funcionamento interno; não substitui a lei federal nem o decreto regulamentador.
- **Conceito cobrado:** Sigilo profissional.
- **Pegadinha usada:** Tratar sigilo como escolha comercial do profissional.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.10

- **Alternativa correta:** D.
- **A) está errada:** Na apostila, a RN CFA nº 651/2024 aparece como norma que aprova o Regimento Interno do CRA-PR; o Código de Ética é a RN CFA nº 671/2025.
- **B) está errada:** Para concurso, a base é o edital vigente; norma nova só substitui conteúdo se houver fonte oficial e pertinência ao edital.
- **C) está errada:** Sigilo é dever profissional, salvo hipótese legal, autorização legítima ou justa causa reconhecida.
- **D) está correta:** A regularidade profissional exige responsabilidade real pelo trabalho, não mera cessão formal do registro.
- **Conceito cobrado:** Uso indevido de nome ou registro.
- **Pegadinha usada:** Exigir dano financeiro para reconhecer irregularidade ética.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.11

- **Alternativa correta:** A.
- **A) está correta:** A fiscalização depende de colaboração mínima do fiscalizado quando há competência do CRA.
- **B) está errada:** O CRA-PR tem autonomia administrativa, mas atua dentro do Sistema CFA/CRAs e não afasta a normatização geral do CFA.
- **C) está errada:** A pessoa jurídica pode estar sujeita a registro e fiscalização quando atua em campo abrangido pela Administração.
- **D) está errada:** A fiscalização profissional é função típica do conselho regional e pode ocorrer no âmbito de sua competência.
- **Conceito cobrado:** Fiscalização profissional.
- **Pegadinha usada:** Supor que a fiscalização só ocorre após decisão judicial.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.12

- **Alternativa correta:** B.
- **A) está errada:** O registro e a fiscalização regional são atribuições dos CRAs; o CFA atua em plano nacional e normativo.
- **B) está correta:** A norma foi incluída porque anuidade, taxas e cobrança podem aparecer em contexto de conselhos.
- **C) está errada:** Regimento organiza funcionamento interno; não substitui a lei federal nem o decreto regulamentador.
- **D) está errada:** O uso indevido de nome ou registro profissional já compromete a ética e a regularidade, independentemente de dano financeiro imediato.
- **Conceito cobrado:** Lei nº 12.514/2011.
- **Pegadinha usada:** Ignorar normas financeiras dos conselhos por parecerem administrativas.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.13

- **Alternativa correta:** C.
- **A) está errada:** Para concurso, a base é o edital vigente; norma nova só substitui conteúdo se houver fonte oficial e pertinência ao edital.
- **B) está errada:** Sigilo é dever profissional, salvo hipótese legal, autorização legítima ou justa causa reconhecida.
- **C) está correta:** Registro é atividade central do CRA e a RN 649/2024 foi apontada como regulamento de registro.
- **D) está errada:** A Lei nº 12.514/2011 trata de contribuições devidas aos conselhos profissionais.
- **Conceito cobrado:** RN CFA nº 649/2024.
- **Pegadinha usada:** Confundir registro com sanção ética.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.14

- **Alternativa correta:** D.
- **A) está errada:** A pessoa jurídica pode estar sujeita a registro e fiscalização quando atua em campo abrangido pela Administração.
- **B) está errada:** A fiscalização profissional é função típica do conselho regional e pode ocorrer no âmbito de sua competência.
- **C) está errada:** Na apostila, a RN CFA nº 651/2024 aparece como norma que aprova o Regimento Interno do CRA-PR; o Código de Ética é a RN CFA nº 671/2025.
- **D) está correta:** Norma alteradora não deve ser estudada isoladamente; deve ser conectada ao texto alterado.
- **Conceito cobrado:** RN CFA nº 670/2025.
- **Pegadinha usada:** Ler norma alteradora como se fosse conteúdo autônomo sem relação com registro.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.15

- **Alternativa correta:** A.
- **A) está correta:** A apostila sinaliza ponto pendente de confirmação para não transformar hipótese em certeza de prova.
- **B) está errada:** Regimento organiza funcionamento interno; não substitui a lei federal nem o decreto regulamentador.
- **C) está errada:** O uso indevido de nome ou registro profissional já compromete a ética e a regularidade, independentemente de dano financeiro imediato.
- **D) está errada:** O CRA-PR tem autonomia administrativa, mas atua dentro do Sistema CFA/CRAs e não afasta a normatização geral do CFA.
- **Conceito cobrado:** Normas pendentes de confirmação.
- **Pegadinha usada:** Criar regra específica sem fonte oficial consolidada.
- **Como pensar para acertar:** Identifique o sujeito da situação: CFA, CRA-PR, profissional, pessoa jurídica ou terceiro; depois elimine afirmações absolutas que contrariem o edital.

#### Comentário Extra Dia 1.16

- **Alternativa correta:** B.
- **A) está errada:** Oposição seria indicada por conectores como 'mas' ou 'contudo'.
- **B) está correta:** O conector 'por isso' estabelece consequência.
- **C) está errada:** O conector retoma o fato anterior para apresentar efeito.
- **D) está errada:** Não há mera soma de ideias; há relação conclusiva.
- **Conceito cobrado:** Coesão por conectores.
- **Pegadinha usada:** Confundir conclusão com oposição.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 1.17

- **Alternativa correta:** C.
- **A) está errada:** Edital não é agente que conclui; o referente lógico é comissão.
- **B) está errada:** Candidato não aparece no trecho.
- **C) está correta:** O pronome possessivo deve ser interpretado pelo referente compatível no texto.
- **D) está errada:** Não há dois referentes expressos nessa frase.
- **Conceito cobrado:** Referência pronominal.
- **Pegadinha usada:** Escolher referente próximo sem observar sentido.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 1.18

- **Alternativa correta:** D.
- **A) está errada:** Altera o sentido restritivo de 'somente'.
- **B) está errada:** Inverte completamente o sentido.
- **C) está errada:** Muda a ordem lógica dos fatos.
- **D) está correta:** 'Somente' equivale a 'apenas' no contexto.
- **Conceito cobrado:** Reescrita e manutenção de sentido.
- **Pegadinha usada:** Perder palavra restritiva.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 1.19

- **Alternativa correta:** A.
- **A) está correta:** Há preposição 'a' + artigo feminino em 'à unidade'.
- **B) está errada:** Não há crase antes de verbo.
- **C) está errada:** Não há artigo feminino antes de 'todos'.
- **D) está errada:** Não há artigo feminino antes de palavra masculina.
- **Conceito cobrado:** Crase.
- **Pegadinha usada:** Aplicar crase antes de verbo, masculino ou pronome indefinido.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 1.20

- **Alternativa correta:** B.
- **A) está errada:** Causa indicaria motivo; 'embora' introduz fato contrário à expectativa.
- **B) está correta:** 'Embora' introduz concessão.
- **C) está errada:** Conclusão seria marcada por 'logo', 'portanto' ou equivalente.
- **D) está errada:** Condição seria introduzida por 'se', 'caso' ou equivalente.
- **Conceito cobrado:** Valor semântico de conjunção.
- **Pegadinha usada:** Confundir concessão com causa.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

---

# Dia 2 — Sistemas Operacionais

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões principais

### Questão 1

Em um órgão público, um sistema de protocolo fica lento quando vários usuários acessam relatórios ao mesmo tempo. O sistema operacional atua nesse cenário principalmente para:

A) transformar todo processo em arquivo permanente.
B) gerenciar processos, memória, arquivos e dispositivos compartilhados.
C) substituir o banco de dados relacional em todas as consultas.
D) eliminar a necessidade de autenticação de usuários.

### Questão 2

Considere as assertivas.

I. Programa é um conjunto de instruções armazenado.
II. Processo é um programa em execução, com contexto e recursos associados.
III. Thread é sempre um processo totalmente independente, sem compartilhar recursos.

Está correto apenas o que se afirma em:

A) I e II.
B) I e III.
C) II e III.
D) I, II e III.

### Questão 3

Um processo que aguarda leitura de disco ser concluída normalmente está no estado:

A) executando na CPU.
B) pronto, obrigatoriamente.
C) zumbi desde o início da leitura.
D) bloqueado/esperando.

### Questão 4

No escalonamento preemptivo, o sistema operacional:

A) desativa interrupções de temporizador permanentemente.
B) executa apenas um programa por inicialização do computador.
C) pode interromper um processo em execução para dar CPU a outro.
D) precisa esperar o processo terminar voluntariamente em todos os casos.

### Questão 5

Em um servidor com pouca RAM, o uso intenso de swap começa a degradar o desempenho. Esse fenômeno se relaciona diretamente a:

A) conversão de arquivos NTFS para ext4 sem reinicialização.
B) paginação excessiva e possível thrashing.
C) aumento automático do clock da CPU.
D) eliminação de falhas de página.

### Questão 6

Assinale a alternativa correta sobre paginação e segmentação.

A) Paginação usa blocos de tamanho fixo; segmentação usa divisões lógicas de tamanho variável.
B) Paginação usa apenas blocos variáveis; segmentação usa apenas frames fixos.
C) Paginação impede memória virtual.
D) Segmentação é uma política de backup de arquivos.

### Questão 7

Assinale a alternativa incorreta sobre memória virtual.

A) Pode apoiar execução de programas maiores que a RAM disponível, com uso de armazenamento secundário.
B) Ajuda na proteção entre processos.
C) É exatamente a mesma coisa que a memória RAM física instalada.
D) Permite que cada processo tenha uma visão própria de espaço de endereçamento.

### Questão 8

Um arquivo `C:\Dados\relatorio.pdf` no Windows e `/home/ana/relatorio.pdf` no Linux são exemplos de:

A) permissões de execução.
B) nomes de processos em execução.
C) caminhos absolutos.
D) caminhos relativos.

### Questão 9

Um sistema de arquivos com journaling reduz risco de inconsistência após queda de energia porque:

A) elimina permissões de acesso.
B) mantém registros auxiliares de operações para recuperação da estrutura do sistema de arquivos.
C) substitui cópias de segurança de todos os documentos do órgão.
D) impede qualquer falha física no disco.

### Questão 10

No Linux, a sequência `chmod 640 arquivo.txt` define, em termos gerais:

A) permissões diferentes para usuário, grupo e outros.
B) a troca de proprietário do arquivo para o usuário 640.
C) a criação de um novo processo com PID 640.
D) a compactação do arquivo usando nível 640.

### Questão 11

Em um serviço Windows, a execução em segundo plano significa que:

A) o processo nunca consome CPU ou memória.
B) o serviço é sempre malware.
C) o serviço não pode ser registrado em logs.
D) o serviço pode executar tarefas sem interação direta contínua do usuário.

### Questão 12

Um driver de impressora instalado incorretamente pode impedir impressão porque o driver:

A) substitui o spool de impressão e todos os serviços.
B) é sempre dispensável em qualquer hardware moderno.
C) é o software que permite ao SO comunicar-se adequadamente com o dispositivo.
D) é a memória física que armazena todos os arquivos impressos.

### Questão 13

Duas threads incrementam a mesma variável global sem sincronização. Em execuções diferentes, o resultado final varia. O problema descrito é:

A) falha de página irrecuperável.
B) condição de corrida.
C) deadlock por espera circular obrigatória.
D) fragmentação externa de memória.

### Questão 14

Um mutex é usado quando se deseja:

A) garantir exclusão mútua no acesso a uma região crítica.
B) aumentar o tamanho da RAM física.
C) ordenar arquivos em ordem alfabética.
D) substituir o escalonador do sistema operacional.

### Questão 15

Considere o cenário: Processo A segura o recurso X e aguarda Y; Processo B segura Y e aguarda X. Se nenhum recurso for liberado, há exemplo de:

A) cache hit.
B) spooling de impressão.
C) starvation sem posse de recurso.
D) deadlock por espera circular.

### Questão 16

As condições clássicas associadas ao deadlock incluem:

A) seleção, projeção, junção e divisão.
B) volatilidade, persistência, Unicode e ASCII.
C) exclusão mútua, posse e espera, não preempção e espera circular.
D) legalidade, impessoalidade, moralidade e publicidade.

### Questão 17

Um processo finalizou, mas seu processo pai ainda não coletou o status de término em sistema Unix-like. Esse processo é chamado de:

A) thread daemon obrigatória.
B) zumbi.
C) órfão sempre em execução ativa.
D) bloqueado por E/S.

### Questão 18

V/F: Sobre chamadas de sistema.

I. Chamadas de sistema permitem que programas solicitem serviços controlados do kernel.
II. Operações de arquivo e E/S podem envolver chamadas de sistema.
III. Chamadas de sistema substituem a CPU durante a execução.

A sequência correta é:

A) V, V, F.
B) V, F, V.
C) F, V, V.
D) F, F, V.

### Questão 19

Um administrador usa `ps` e `top` em Linux para investigar lentidão. Essas ferramentas ajudam principalmente a:

A) alterar permissões de arquivos.
B) formatar partições obrigatoriamente.
C) compilar kernel automaticamente.
D) observar processos e consumo de recursos.

### Questão 20

Em uma política Round Robin, um quantum muito pequeno tende a:

A) impedir preempção.
B) transformar processos I/O-bound em arquivos.
C) aumentar a frequência de trocas de contexto.
D) eliminar todo overhead de escalonamento.

### Questão 21

Um processo CPU-bound é aquele que:

A) é sempre um processo zumbi.
B) usa intensamente processamento, com menor tempo relativo aguardando E/S.
C) passa a maior parte do tempo esperando disco e rede.
D) não pode ser escalonado.

### Questão 22

Assinale a alternativa incorreta sobre permissões e usuários em sistemas operacionais.

A) Permissões ajudam a controlar leitura, escrita e execução de arquivos.
B) Ambientes multiusuário exigem controle de identidade e autorização.
C) Usuário administrador/root deve ser usado com cautela.
D) Permissão de arquivo elimina a necessidade de autenticação de usuários.

### Questão 23

Uma atualização do sistema operacional em servidor crítico deve ser:

A) sempre aplicada sem teste e sem janela de manutenção.
B) sempre proibida em órgãos públicos.
C) considerada substituta de logs e backup.
D) planejada, testada quando possível e acompanhada de política de backup/rollback.

### Questão 24

Um sistema operacional registra eventos de autenticação, falhas de serviço e erros de dispositivo. Esses registros são importantes porque:

A) substituem a necessidade de controle de acesso.
B) são sempre apagados antes de qualquer análise.
C) ajudam auditoria, diagnóstico e investigação de incidentes.
D) impedem automaticamente todo ataque.

### Questão 25

Em um sistema multitarefa, a troca de contexto consiste em:

A) executar apenas processos finalizados.
B) salvar o estado de uma tarefa e restaurar o estado de outra.
C) renomear arquivos temporários.
D) converter memória virtual em ROM.

### Questão 26

A diferença entre caminho relativo e absoluto é que:

A) o absoluto identifica o caminho a partir da raiz/unidade; o relativo depende do diretório atual.
B) o relativo sempre começa com C:\ e o absoluto nunca começa com /.
C) o absoluto só existe em redes TCP/IP.
D) o relativo contém permissões de execução obrigatoriamente.

### Questão 27

Em sistemas Unix-like, `chown` é usado para:

A) alterar apenas bits de permissão numérica como 755.
B) listar processos ativos.
C) encerrar processo por sinal.
D) alterar proprietário e/ou grupo de arquivo.

### Questão 28

Um processo sofre starvation quando:

A) termina e aguarda coleta pelo processo pai.
B) acessa dado presente na cache.
C) permanece indefinidamente sem receber recurso/CPU por política desfavorável.
D) entra em espera circular segurando recurso de outro processo obrigatoriamente.

### Questão 29

Em virtualização, uma máquina virtual:

A) só pode executar um editor de texto.
B) executa um ambiente isolado sobre camada de virtualização e recursos físicos compartilhados.
C) elimina completamente a necessidade de hardware físico.
D) é sinônimo de memória virtual.

### Questão 30

Um sistema com alta taxa de falhas de página provavelmente está:

A) buscando páginas ausentes na memória física, possivelmente com acesso a disco.
B) executando todas as instruções diretamente da cache L1 sem falta.
C) sem memória virtual por definição.
D) apenas trocando proprietário de arquivos.

### Questão 31

Um servidor usa fila de impressão para organizar documentos enviados por vários setores. Essa técnica se relaciona a:

A) deadlock necessariamente.
B) segmentação de memória.
C) linkedição de bibliotecas.
D) spooling.

### Questão 32

Assinale a alternativa correta sobre NTFS e ext4.

A) São formatos de registradores da CPU.
B) São protocolos de e-mail.
C) São sistemas de arquivos, comuns respectivamente em Windows e Linux.
D) São algoritmos de escalonamento de CPU.

### Questão 33

O comando `kill` em Linux:

A) lista exclusivamente diretórios ocultos.
B) envia sinais a processos, frequentemente para solicitar encerramento.
C) remove fisicamente o processador do computador.
D) altera permissões de arquivo para 755.

### Questão 34

Um serviço travado mantém um lock e impede outros processos de avançar. A primeira análise técnica deve verificar:

A) se há recurso compartilhado retido e dependências de espera entre processos.
B) se a crase foi usada corretamente no nome do serviço.
C) se a chave primária do banco é sempre nula.
D) se o monitor possui resolução 4K.

### Questão 35

Uma política de backup consistente para estações e servidores deve considerar:

A) apenas a existência de journaling no sistema de arquivos.
B) somente copiar atalhos da área de trabalho.
C) desativar logs para economizar espaço sempre.
D) periodicidade, retenção, teste de restauração e proteção contra perda/ataque.

### Questão 36

Em um ambiente com múltiplos usuários, o isolamento entre processos contribui para:

A) dispensar permissões de arquivos.
B) eliminar autenticação no login.
C) impedir que um processo acesse indevidamente memória de outro.
D) proibir qualquer comunicação legítima entre processos.

### Questão 37

Um administrador observa que um processo consome 95% de CPU por longo tempo, mas quase não acessa disco. Uma classificação inicial plausível é:

A) arquivo relativo.
B) CPU-bound.
C) I/O-bound.
D) processo zumbi.

### Questão 38

V/F: Sobre deadlock.

I. Espera circular é uma das condições clássicas.
II. Todo processo bloqueado está necessariamente em deadlock.
III. Prevenção pode atacar uma das condições necessárias.

A sequência correta é:

A) V, F, V.
B) V, V, F.
C) F, V, V.
D) F, F, V.

### Questão 39

Em sistemas operacionais, a diferença entre autenticação e autorização é:

A) autenticação define permissões e autorização verifica identidade, sempre nessa ordem invertida.
B) ambas significam exatamente a mesma coisa.
C) autorização é usada apenas para memória cache.
D) autenticação verifica identidade; autorização define permissões de acesso.

### Questão 40

Assinale a alternativa correta sobre sistemas multitarefa.

A) Multitarefa impede uso de interrupções.
B) Multitarefa só existe quando não há sistema operacional.
C) A alternância rápida entre processos pode dar aparência de execução simultânea em uma CPU.
D) Multitarefa exige obrigatoriamente um núcleo físico para cada processo existente.

### Questão 41

Um arquivo possui permissão de leitura para o grupo, mas não para “outros”. Isso significa que:

A) o arquivo se torna processo em execução.
B) usuários pertencentes ao grupo podem ler, enquanto usuários fora do grupo e não proprietários podem não ter essa permissão.
C) qualquer usuário externo sempre pode ler o arquivo.
D) o proprietário perde automaticamente todas as permissões.

### Questão 42

O kernel oferece chamadas de sistema para operações de arquivo porque:

A) aplicações não devem manipular hardware e estruturas críticas diretamente sem controle.
B) aplicações precisam sempre escrever setores físicos manualmente.
C) o sistema de arquivos não possui permissões.
D) o kernel é apenas uma interface gráfica.

### Questão 43

Um processo órfão em Unix-like é aquele cujo:

A) estado já terminou e só aguarda coleta de status pelo pai.
B) arquivo executável foi apagado antes de iniciar.
C) mutex foi liberado corretamente.
D) processo pai terminou antes dele, e ele passa a ser adotado por outro processo do sistema.

### Questão 44

Assinale a incorreta sobre swap.

A) Uso excessivo pode degradar o desempenho.
B) Tem a mesma latência e velocidade da memória cache L1.
C) Pode apoiar a memória virtual quando a RAM está pressionada.
D) É normalmente mais lento que acesso à RAM.

### Questão 45

Um administrador quer saber quais serviços subiram com falha após reinicialização em Linux com systemd. O comando mais relacionado é:

A) chown -R /, pois muda todos os donos e resolve falhas.
B) systemctl status ou journalctl, conforme o caso.
C) chmod 777, pois sempre corrige serviços.
D) SELECT * FROM services, pois serviços são tabelas SQL.

### Questão 46

Em Windows, permissões NTFS são relevantes porque:

A) controlam acesso a arquivos e pastas por usuários/grupos.
B) substituem integralmente autenticação de domínio.
C) servem apenas para colorir ícones.
D) só existem em mídias FAT32.

### Questão 47

Uma aplicação faz muitas leituras de rede e fica frequentemente bloqueada aguardando resposta externa. Ela tende a ser:

A) CPU-bound puro.
B) processo zumbi.
C) interrupção não mascarável.
D) I/O-bound.

### Questão 48

Assinale a correta sobre monitores, semáforos e mutexes.

A) São modos de endereçamento da CPU.
B) São tipos de backup incremental.
C) São mecanismos/conceitos usados para sincronização de concorrência.
D) São sistemas de arquivos do Windows.

### Questão 49

Um servidor sofreu queda brusca de energia. Após reiniciar, o sistema de arquivos usa seu journal para reduzir inconsistências. Mesmo assim, o administrador deve:

A) desativar logs para impedir análise.
B) validar dados e usar backups se houver perda ou corrupção de arquivos.
C) descartar todos os backups por serem redundantes.
D) remover todas as permissões para acelerar o disco.

### Questão 50

Em uma região crítica, a ausência de sincronização adequada pode gerar:

A) inconsistência de dados por acesso concorrente.
B) aumento automático de espaço em disco.
C) criação automática de usuários.
D) desativação de todo o escalonamento.

## Questões extras de revisão fixa do Dia 2

#### Extra Dia 2.1

**Área:** Administração Pública.

Sobre os princípios do art. 37 da Constituição, assinale a alternativa correta.

A) Publicidade impede qualquer sigilo em documentos públicos.
B) Legalidade, impessoalidade, moralidade, publicidade e eficiência formam o núcleo expresso conhecido como LIMPE.
C) Responsabilidade civil do Estado dispensa dano e nexo causal.
D) Ato administrativo não precisa de finalidade pública se for conveniente ao gestor.

#### Extra Dia 2.2

**Área:** Administração Pública.

Um órgão público decide contratar servidor por afinidade pessoal, sem critério objetivo. Qual princípio é diretamente afetado?

A) Impessoalidade, pois a atuação administrativa deve buscar finalidade pública e critérios objetivos.
B) Autarquia integra a Administração Direta porque executa serviço público.
C) Improbidade é sinônimo de qualquer erro formal cometido pelo agente.
D) Pregão é modalidade voltada à alienação de bens públicos.

#### Extra Dia 2.3

**Área:** Administração Pública.

Sobre Administração Direta e Indireta, assinale a alternativa correta.

A) Competência do ato administrativo pode ser escolhida livremente pela autoridade.
B) Eficiência autoriza descumprir legalidade para alcançar resultado rápido.
C) LGPD elimina a aplicação da LAI em todos os pedidos de acesso.
D) Administração Direta é composta pelos entes federativos e seus órgãos; Administração Indireta reúne entidades com personalidade própria.

#### Extra Dia 2.4

**Área:** Administração Pública.

No contexto dos conselhos profissionais, assinale a alternativa correta.

A) Na inexigibilidade, a competição é possível, mas a lei prefere dispensá-la.
B) Ato administrativo não precisa de finalidade pública se for conveniente ao gestor.
C) Conselhos profissionais são frequentemente tratados como autarquias corporativas ou entidades de fiscalização profissional.
D) Publicidade impede qualquer sigilo em documentos públicos.

#### Extra Dia 2.5

**Área:** Administração Pública.

Sobre autarquias, assinale a alternativa correta.

A) Responsabilidade civil do Estado dispensa dano e nexo causal.
B) Autarquia possui personalidade jurídica própria e integra a Administração Indireta.
C) Pregão é modalidade voltada à alienação de bens públicos.
D) Autarquia integra a Administração Direta porque executa serviço público.

#### Extra Dia 2.6

**Área:** Administração Pública.

Uma autoridade pratica ato sem competência legal. Qual elemento do ato administrativo está comprometido?

A) Competência.
B) Improbidade é sinônimo de qualquer erro formal cometido pelo agente.
C) LGPD elimina a aplicação da LAI em todos os pedidos de acesso.
D) Competência do ato administrativo pode ser escolhida livremente pela autoridade.

#### Extra Dia 2.7

**Área:** Administração Pública.

Sobre finalidade do ato administrativo, assinale a alternativa correta.

A) Eficiência autoriza descumprir legalidade para alcançar resultado rápido.
B) Publicidade impede qualquer sigilo em documentos públicos.
C) Na inexigibilidade, a competição é possível, mas a lei prefere dispensá-la.
D) O ato deve perseguir finalidade pública; desvio para interesse pessoal pode invalidá-lo.

#### Extra Dia 2.8

**Área:** Administração Pública.

A Administração anulou ato ilegal após constatar vício. Assinale a alternativa correta.

A) Ato administrativo não precisa de finalidade pública se for conveniente ao gestor.
B) Autarquia integra a Administração Direta porque executa serviço público.
C) A anulação relaciona-se ao controle de legalidade do ato administrativo.
D) Responsabilidade civil do Estado dispensa dano e nexo causal.

#### Extra Dia 2.9

**Área:** Administração Pública.

Sobre LAI e transparência, assinale a alternativa correta.

A) Pregão é modalidade voltada à alienação de bens públicos.
B) A publicidade é regra, mas informações protegidas por sigilo legal ou dados pessoais exigem tratamento adequado.
C) Competência do ato administrativo pode ser escolhida livremente pela autoridade.
D) Improbidade é sinônimo de qualquer erro formal cometido pelo agente.

#### Extra Dia 2.10

**Área:** Administração Pública.

Sobre LGPD na Administração Pública, assinale a alternativa correta.

A) O tratamento de dados pessoais deve observar finalidade, necessidade, segurança e base legal adequada.
B) LGPD elimina a aplicação da LAI em todos os pedidos de acesso.
C) Na inexigibilidade, a competição é possível, mas a lei prefere dispensá-la.
D) Eficiência autoriza descumprir legalidade para alcançar resultado rápido.

#### Extra Dia 2.11

**Área:** Administração Pública.

Sobre improbidade administrativa, assinale a alternativa correta.

A) Publicidade impede qualquer sigilo em documentos públicos.
B) Responsabilidade civil do Estado dispensa dano e nexo causal.
C) Ato administrativo não precisa de finalidade pública se for conveniente ao gestor.
D) Improbidade não é qualquer ilegalidade; exige enquadramento na lei e requisitos próprios, inclusive elemento subjetivo quando exigido.

#### Extra Dia 2.12

**Área:** Administração Pública.

Servidor usa o cargo para obter vantagem patrimonial indevida. Em tese, a situação se aproxima de qual categoria clássica?

A) Autarquia integra a Administração Direta porque executa serviço público.
B) Improbidade é sinônimo de qualquer erro formal cometido pelo agente.
C) Enriquecimento ilícito.
D) Pregão é modalidade voltada à alienação de bens públicos.

#### Extra Dia 2.13

**Área:** Administração Pública.

Em licitação, o edital definiu critério e exigências. Durante o julgamento, a Administração quer ignorá-los. Assinale a alternativa correta.

A) Competência do ato administrativo pode ser escolhida livremente pela autoridade.
B) A vinculação ao edital impede julgamento contrário às regras previamente estabelecidas.
C) Eficiência autoriza descumprir legalidade para alcançar resultado rápido.
D) LGPD elimina a aplicação da LAI em todos os pedidos de acesso.

#### Extra Dia 2.14

**Área:** Administração Pública.

Sobre dispensa e inexigibilidade de licitação, assinale a alternativa correta.

A) Na dispensa, a competição é possível em tese, mas a lei autoriza não licitar; na inexigibilidade, a competição é inviável.
B) Na inexigibilidade, a competição é possível, mas a lei prefere dispensá-la.
C) Ato administrativo não precisa de finalidade pública se for conveniente ao gestor.
D) Publicidade impede qualquer sigilo em documentos públicos.

#### Extra Dia 2.15

**Área:** Administração Pública.

Para aquisição de bem ou serviço comum, a modalidade ordinariamente associada pela Lei nº 14.133/2021 é:

A) Responsabilidade civil do Estado dispensa dano e nexo causal.
B) Pregão é modalidade voltada à alienação de bens públicos.
C) Autarquia integra a Administração Direta porque executa serviço público.
D) Pregão.

#### Extra Dia 2.16

**Área:** Língua Portuguesa/interpretação.

Assinale a frase em que a concordância verbal está adequada.

A) Haviam muitos processos pendentes no setor.
B) Existia muitos processos pendentes no setor.
C) Havia muitos processos pendentes no setor.
D) Foi analisado as planilhas do setor.

#### Extra Dia 2.17

**Área:** Língua Portuguesa/interpretação.

No período "O servidor informou ao candidato que seu recurso fora analisado", há possível ambiguidade porque:

A) o verbo 'informou' está sem complemento.
B) o pronome 'seu' pode se referir ao servidor ou ao candidato.
C) a forma 'fora' indica futuro do presente.
D) a palavra 'recurso' impede qualquer dupla interpretação.

#### Extra Dia 2.18

**Área:** Língua Portuguesa/interpretação.

Assinale a frase em que "onde" foi empregado adequadamente.

A) O setor onde os documentos são arquivados será reorganizado.
B) A situação onde ocorreu o erro será analisada.
C) A norma onde consta o prazo foi revogada.
D) O procedimento onde o candidato recorreu foi digital.

#### Extra Dia 2.19

**Área:** Língua Portuguesa/interpretação.

Assinale a alternativa em que a pontuação preserva melhor a clareza.

A) Após a conferência dos dados a equipe, publicou o resultado.
B) Após, a conferência dos dados a equipe publicou o resultado.
C) Após a conferência, dos dados a equipe publicou, o resultado.
D) Após a conferência dos dados, a equipe publicou o resultado.

#### Extra Dia 2.20

**Área:** Língua Portuguesa/interpretação.

Leia: "O parecer não elimina a necessidade de nova análise." Infere-se corretamente que:

A) a nova análise foi dispensada pelo parecer.
B) o parecer proibiu qualquer análise futura.
C) ainda será necessária nova análise.
D) a análise anterior foi anulada automaticamente.


## Gabarito do Dia 2

1. B
2. A
3. D
4. C
5. B
6. A
7. C
8. C
9. B
10. A
11. D
12. C
13. B
14. A
15. D
16. C
17. B
18. A
19. D
20. C
21. B
22. D
23. D
24. C
25. B
26. A
27. D
28. C
29. B
30. A
31. D
32. C
33. B
34. A
35. D
36. C
37. B
38. A
39. D
40. C
41. B
42. A
43. D
44. B
45. B
46. A
47. D
48. C
49. B
50. A

### Gabarito das questões extras de revisão fixa do Dia 2

Extra Dia 2.1: B
Extra Dia 2.2: A
Extra Dia 2.3: D
Extra Dia 2.4: C
Extra Dia 2.5: B
Extra Dia 2.6: A
Extra Dia 2.7: D
Extra Dia 2.8: C
Extra Dia 2.9: B
Extra Dia 2.10: A
Extra Dia 2.11: D
Extra Dia 2.12: C
Extra Dia 2.13: B
Extra Dia 2.14: A
Extra Dia 2.15: D
Extra Dia 2.16: C
Extra Dia 2.17: B
Extra Dia 2.18: A
Extra Dia 2.19: D
Extra Dia 2.20: C


## Comentários do Dia 2

### Comentário da Questão 1

- **Alternativa correta:** B.
- **A) está errada:** Processo em execução não é convertido em arquivo por definição.
- **B) está correta:** O SO coordena recursos para aplicações concorrentes.
- **C) está errada:** O SO não substitui o SGBD; cada camada tem função própria.
- **D) está errada:** SO pode apoiar autenticação, mas não elimina a necessidade de controle.
- **Conceito cobrado:** Funções do sistema operacional.
- **Pegadinha usada:** Confundir SO com SGBD ou aplicativo..
- **Como pensar para acertar:** Identifique a camada que gerencia recursos básicos do computador.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 2

- **Alternativa correta:** A.
- **A) está correta:** Programa e processo estão corretamente diferenciados; thread costuma compartilhar recursos do processo.
- **B) está errada:** III está errada porque thread não é sempre processo independente.
- **C) está errada:** I é verdadeira e III é falsa.
- **D) está errada:** Inclui III, que generaliza incorretamente thread.
- **Conceito cobrado:** Programa, processo e thread.
- **Pegadinha usada:** Tratar thread como processo isolado em todos os recursos..
- **Como pensar para acertar:** Separe código armazenado, execução com contexto e linha de execução.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 3

- **Alternativa correta:** D.
- **A) está errada:** Se aguarda E/S, em regra não está usando a CPU.
- **B) está errada:** Pronto significa apto a executar; aqui falta evento de E/S.
- **C) está errada:** Zumbi é processo terminado aguardando coleta de status.
- **D) está correta:** Ele não pode prosseguir até a conclusão da E/S.
- **Conceito cobrado:** Estados de processo.
- **Pegadinha usada:** Confundir bloqueado com pronto ou zumbi..
- **Como pensar para acertar:** Pergunte se o processo está apto a executar agora. Se depende de evento, está bloqueado.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 4

- **Alternativa correta:** C.
- **A) está errada:** Temporizador é mecanismo importante para preempção.
- **B) está errada:** Multitarefa permite alternância entre vários processos.
- **C) está correta:** Preempção permite retirada da CPU conforme política.
- **D) está errada:** Isso descreve comportamento não preemptivo/cooperativo.
- **Conceito cobrado:** Escalonamento preemptivo.
- **Pegadinha usada:** Confundir preemptivo com cooperativo..
- **Como pensar para acertar:** Procure a ideia de retirada forçada/controlada da CPU.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 5

- **Alternativa correta:** B.
- **A) está errada:** Não há relação com conversão de sistema de arquivos.
- **B) está correta:** Muitas trocas entre RAM e disco reduzem trabalho útil.
- **C) está errada:** Swap não aumenta clock.
- **D) está errada:** Uso de swap decorre justamente de pressão de memória/falhas de página.
- **Conceito cobrado:** Memória virtual e swap.
- **Pegadinha usada:** Achar que swap sempre melhora desempenho..
- **Como pensar para acertar:** Swap ajuda a sobreviver à falta de RAM, mas disco é muito mais lento.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 6

- **Alternativa correta:** A.
- **A) está correta:** Essa é a distinção clássica cobrada.
- **B) está errada:** Inverte a distinção.
- **C) está errada:** Paginação é técnica comum de implementação de memória virtual.
- **D) está errada:** Segmentação é técnica de organização de memória.
- **Conceito cobrado:** Paginação e segmentação.
- **Pegadinha usada:** Inverter fixo e variável..
- **Como pensar para acertar:** Associe página/frame a tamanho fixo e segmento a unidade lógica.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 7

- **Alternativa correta:** C.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: disco/swap pode apoiar a memória virtual.
- **B) está correta como afirmação:** Correta: espaços virtuais isolados dificultam acesso indevido.
- **C) é a incorreta:** Incorreta: memória virtual é abstração; RAM é memória física.
- **D) está correta como afirmação:** Correta: a abstração isola processos.
- **Conceito cobrado:** Memória virtual.
- **Pegadinha usada:** Igualar abstração virtual à RAM física..
- **Como pensar para acertar:** Virtual é o que o processo enxerga; físico é onde efetivamente está na RAM.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 8

- **Alternativa correta:** C.
- **A) está errada:** São localizações, não permissões.
- **B) está errada:** São caminhos de arquivo, não processos.
- **C) está correta:** Ambos partem da unidade/raiz e indicam localização completa.
- **D) está errada:** Caminho relativo depende do diretório atual; os exemplos não dependem.
- **Conceito cobrado:** Caminhos de arquivos.
- **Pegadinha usada:** Confundir localização de arquivo com permissão ou processo..
- **Como pensar para acertar:** Caminho absoluto não depende do diretório atual.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 9

- **Alternativa correta:** B.
- **A) está errada:** Permissões continuam existindo.
- **B) está correta:** Journaling ajuda a restaurar consistência estrutural.
- **C) está errada:** Journaling não recupera necessariamente arquivos apagados ou versões antigas.
- **D) está errada:** Journaling não evita defeito de hardware.
- **Conceito cobrado:** Journaling.
- **Pegadinha usada:** Achar que journaling é backup completo..
- **Como pensar para acertar:** Journaling cuida de consistência; backup cuida de recuperação de dados.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 10

- **Alternativa correta:** A.
- **A) está correta:** chmod altera permissões; 640 representa leitura/escrita para dono, leitura para grupo e nenhuma para outros.
- **B) está errada:** Troca de proprietário é com chown, não chmod.
- **C) está errada:** chmod não cria processo.
- **D) está errada:** Não é comando de compactação.
- **Conceito cobrado:** Permissões Linux e chmod.
- **Pegadinha usada:** Confundir chmod e chown..
- **Como pensar para acertar:** Veja o verbo: mode/permissão, não owner/proprietário.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 11

- **Alternativa correta:** D.
- **A) está errada:** Serviços podem consumir recursos.
- **B) está errada:** Serviços podem ser legítimos ou maliciosos; não se presume sempre.
- **C) está errada:** Eventos de serviços podem aparecer em logs.
- **D) está correta:** Serviços rodam em background para funções do sistema/aplicações.
- **Conceito cobrado:** Serviços em segundo plano.
- **Pegadinha usada:** Generalizar serviço como malware ou como inofensivo sem análise..
- **Como pensar para acertar:** Serviço é modo de execução; a legitimidade depende do caso.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 12

- **Alternativa correta:** C.
- **A) está errada:** Driver e spool têm funções diferentes.
- **B) está errada:** Dispositivos ainda dependem de drivers ou módulos equivalentes.
- **C) está correta:** Driver traduz comandos do SO/aplicação para o hardware específico.
- **D) está errada:** Driver não é armazenamento físico.
- **Conceito cobrado:** Drivers de dispositivo.
- **Pegadinha usada:** Confundir driver com hardware ou fila de impressão..
- **Como pensar para acertar:** Driver é camada de controle do dispositivo.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 13

- **Alternativa correta:** B.
- **A) está errada:** Não há indicação de página ausente ou erro de memória virtual.
- **B) está correta:** O resultado depende da ordem de execução concorrente.
- **C) está errada:** Não há descrição de espera circular; há disputa sem sincronização.
- **D) está errada:** O problema é concorrência, não alocação de memória.
- **Conceito cobrado:** Condição de corrida.
- **Pegadinha usada:** Confundir inconsistência concorrente com deadlock..
- **Como pensar para acertar:** Se o resultado depende do timing de threads, pense em corrida.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 14

- **Alternativa correta:** A.
- **A) está correta:** Mutex permite que apenas um fluxo acesse recurso protegido por vez.
- **B) está errada:** Mutex não altera hardware.
- **C) está errada:** Ordenação de arquivos não é função de mutex.
- **D) está errada:** Mutex sincroniza acesso; não escolhe processos para CPU.
- **Conceito cobrado:** Mutex e região crítica.
- **Pegadinha usada:** Atribuir ao mutex funções de desempenho ou escalonamento..
- **Como pensar para acertar:** Associe mutex a “um por vez” em recurso compartilhado.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 15

- **Alternativa correta:** D.
- **A) está errada:** Cache hit ocorre quando dado é encontrado na cache.
- **B) está errada:** Spooling é enfileiramento de trabalhos de E/S.
- **C) está errada:** Starvation é espera indefinida por política; aqui há ciclo de recursos.
- **D) está correta:** Há dependência circular entre processos e recursos.
- **Conceito cobrado:** Deadlock.
- **Pegadinha usada:** Confundir espera circular com lentidão genérica..
- **Como pensar para acertar:** Procure ciclo: A espera B, B espera A.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 16

- **Alternativa correta:** C.
- **A) está errada:** São operações da álgebra relacional.
- **B) está errada:** São conceitos de representação/memória, não condições de deadlock.
- **C) está correta:** Essas são as quatro condições clássicas.
- **D) está errada:** São princípios administrativos, não condições de deadlock.
- **Conceito cobrado:** Condições de deadlock.
- **Pegadinha usada:** Confundir listas de disciplinas diferentes..
- **Como pensar para acertar:** Memorize as quatro condições como um bloco técnico de SO.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 17

- **Alternativa correta:** B.
- **A) está errada:** Daemon é processo/serviço de background, não esse estado específico.
- **B) está correta:** Processo zumbi terminou, mas permanece na tabela até coleta do status.
- **C) está errada:** Órfão é processo cujo pai terminou; não é a mesma definição.
- **D) está errada:** Bloqueado aguarda evento; o processo zumbi já terminou.
- **Conceito cobrado:** Processo zumbi.
- **Pegadinha usada:** Confundir zumbi, órfão e bloqueado..
- **Como pensar para acertar:** Observe: terminou, mas ainda consta para o pai coletar status.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 18

- **Alternativa correta:** A.
- **A) está correta:** I e II estão corretas; III é falsa porque chamadas não substituem hardware de execução.
- **B) está errada:** II é verdadeira e III é falsa.
- **C) está errada:** I é verdadeira e III é falsa.
- **D) está errada:** I e II não deveriam ser falsas.
- **Conceito cobrado:** Chamadas de sistema.
- **Pegadinha usada:** Atribuir às chamadas de sistema papel físico da CPU..
- **Como pensar para acertar:** Chamadas são interface de solicitação ao kernel.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 19

- **Alternativa correta:** D.
- **A) está errada:** chmod/chown são usados para permissões/proprietário.
- **B) está errada:** ps/top não formatam disco.
- **C) está errada:** Essas ferramentas não compilam kernel.
- **D) está correta:** ps lista processos e top acompanha uso em tempo real.
- **Conceito cobrado:** Comandos Linux de processos.
- **Pegadinha usada:** Confundir comandos de monitoramento com comandos de permissão..
- **Como pensar para acertar:** Associe ps/top a processos e desempenho.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 20

- **Alternativa correta:** C.
- **A) está errada:** Round Robin é preemptivo por fatias de tempo.
- **B) está errada:** Não há tal transformação.
- **C) está correta:** Fatias muito pequenas geram muitas alternâncias.
- **D) está errada:** Mais trocas tendem a aumentar overhead.
- **Conceito cobrado:** Round Robin e quantum.
- **Pegadinha usada:** Achar que quantum menor é sempre melhor..
- **Como pensar para acertar:** Pense no custo de alternar tarefas.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 21

- **Alternativa correta:** B.
- **A) está errada:** Zumbi já terminou; CPU-bound está ligado ao perfil de uso.
- **B) está correta:** CPU-bound demanda CPU como recurso principal.
- **C) está errada:** Isso descreve I/O-bound.
- **D) está errada:** Todo processo executável depende de escalonamento.
- **Conceito cobrado:** Processos CPU-bound e I/O-bound.
- **Pegadinha usada:** Confundir gargalo de processamento com E/S..
- **Como pensar para acertar:** Identifique qual recurso limita a execução.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 22

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: permissões limitam operações sobre objetos.
- **B) está correta como afirmação:** Correta: autenticação/autorização são essenciais.
- **C) está correta como afirmação:** Correta: privilégios elevados aumentam risco.
- **D) é a incorreta:** Incorreta: permissão e autenticação são controles complementares.
- **Conceito cobrado:** Usuários, permissões e privilégios.
- **Pegadinha usada:** Confundir autorização com autenticação..
- **Como pensar para acertar:** Primeiro identifica o usuário; depois verifica o que ele pode fazer.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 23

- **Alternativa correta:** D.
- **A) está errada:** Ambientes críticos exigem planejamento.
- **B) está errada:** Atualizações de segurança são necessárias; o ponto é planejar.
- **C) está errada:** Atualização, log e backup são práticas complementares.
- **D) está correta:** Atualizações corrigem falhas, mas podem impactar operação.
- **Conceito cobrado:** Administração e manutenção de SO.
- **Pegadinha usada:** Tratar atualização como sempre segura ou sempre proibida..
- **Como pensar para acertar:** Em produção, equilíbrio entre segurança e continuidade.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 24

- **Alternativa correta:** C.
- **A) está errada:** Controle de acesso e logs têm funções distintas.
- **B) está errada:** Boas práticas preservam logs relevantes.
- **C) está correta:** Logs permitem rastrear eventos e causas prováveis.
- **D) está errada:** Logs ajudam detectar/analisar; não impedem tudo sozinhos.
- **Conceito cobrado:** Logs do sistema.
- **Pegadinha usada:** Achar que log é prevenção completa..
- **Como pensar para acertar:** Log é evidência/registro; prevenção exige controles adicionais.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 25

- **Alternativa correta:** B.
- **A) está errada:** Processos finalizados não são alternados para execução útil.
- **B) está correta:** Context switch permite alternância controlada entre execuções.
- **C) está errada:** Não se trata de sistema de arquivos.
- **D) está errada:** Não há conversão desse tipo.
- **Conceito cobrado:** Troca de contexto.
- **Pegadinha usada:** Confundir contexto de execução com contexto textual..
- **Como pensar para acertar:** O SO precisa lembrar onde parou uma tarefa para retomar depois.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 26

- **Alternativa correta:** A.
- **A) está correta:** Essa é a distinção prática em sistemas de arquivos.
- **B) está errada:** Inverte exemplos comuns de Windows/Linux.
- **C) está errada:** Caminhos absolutos existem em sistemas de arquivos locais.
- **D) está errada:** Permissão é outro atributo.
- **Conceito cobrado:** Caminhos absoluto e relativo.
- **Pegadinha usada:** Confundir sintaxe com permissão..
- **Como pensar para acertar:** Pergunte: preciso saber o diretório atual para resolver?
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 27

- **Alternativa correta:** D.
- **A) está errada:** Isso é função típica de chmod.
- **B) está errada:** ps/top listam processos.
- **C) está errada:** kill envia sinais a processos.
- **D) está correta:** chown vem de change owner.
- **Conceito cobrado:** Comandos Linux.
- **Pegadinha usada:** Trocar chown e chmod..
- **Como pensar para acertar:** Owner indica proprietário; mode indica permissões.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 28

- **Alternativa correta:** C.
- **A) está errada:** Isso é processo zumbi.
- **B) está errada:** Isso é cache hit.
- **C) está correta:** Starvation é inanição por falta de atendimento.
- **D) está errada:** Isso descreve deadlock, não starvation em geral.
- **Conceito cobrado:** Starvation.
- **Pegadinha usada:** Confundir starvation com deadlock e zumbi..
- **Como pensar para acertar:** Starvation é falta de progresso por não ser escolhido/atendido.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 29

- **Alternativa correta:** B.
- **A) está errada:** Máquinas virtuais podem executar sistemas completos.
- **B) está correta:** Virtualização abstrai hardware para ambientes isolados.
- **C) está errada:** Hardware físico continua existindo.
- **D) está errada:** São conceitos diferentes: VM de sistema e memória virtual.
- **Conceito cobrado:** Virtualização.
- **Pegadinha usada:** Confundir máquina virtual com memória virtual..
- **Como pensar para acertar:** Ambas usam “virtual”, mas em níveis diferentes.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 30

- **Alternativa correta:** A.
- **A) está correta:** Page fault ocorre quando a página necessária não está carregada.
- **B) está errada:** Isso seria cenário de muitos hits, não page faults.
- **C) está errada:** Falha de página é fenômeno de memória virtual/paginação.
- **D) está errada:** Não se relaciona a chown/permissões.
- **Conceito cobrado:** Falha de página.
- **Pegadinha usada:** Achar que toda falha de página é erro fatal..
- **Como pensar para acertar:** Falha de página pode ser tratável, mas em excesso degrada desempenho.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 31

- **Alternativa correta:** D.
- **A) está errada:** Fila de impressão não implica deadlock por si só.
- **B) está errada:** Segmentação é memória, não fila de impressão.
- **C) está errada:** Linkedição é construção de programa.
- **D) está correta:** Spooling enfileira trabalhos para dispositivo mais lento/compartilhado.
- **Conceito cobrado:** Spooling.
- **Pegadinha usada:** Confundir fila de E/S com bloqueio..
- **Como pensar para acertar:** Dispositivo compartilhado e fila de trabalhos sugerem spooling.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 32

- **Alternativa correta:** C.
- **A) está errada:** Sistemas de arquivos organizam armazenamento, não registradores.
- **B) está errada:** Protocolos de e-mail são SMTP, IMAP, POP3 etc.
- **C) está correta:** NTFS é comum no Windows; ext4 é comum em Linux.
- **D) está errada:** Escalonamento usa políticas como Round Robin, prioridade etc.
- **Conceito cobrado:** Sistemas de arquivos.
- **Pegadinha usada:** Confundir siglas de sistemas de arquivos com protocolos..
- **Como pensar para acertar:** Associe NTFS/ext4 à organização de arquivos no armazenamento.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 33

- **Alternativa correta:** B.
- **A) está errada:** Listagem de arquivos é função de ls.
- **B) está correta:** kill trabalha com sinais como TERM e KILL.
- **C) está errada:** É comando de software, não remoção de hardware.
- **D) está errada:** Isso é chmod.
- **Conceito cobrado:** Sinais e processos Linux.
- **Pegadinha usada:** Interpretar o nome do comando literalmente demais..
- **Como pensar para acertar:** Em Unix/Linux, sinais são mecanismo de controle de processos.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 34

- **Alternativa correta:** A.
- **A) está correta:** Locks e esperas podem indicar deadlock ou contenção.
- **B) está errada:** Questão de Português não diagnostica lock.
- **C) está errada:** Pode haver banco envolvido, mas o cenário é de lock/processos.
- **D) está errada:** Resolução do monitor não explica lock de processo.
- **Conceito cobrado:** Locks e diagnóstico de concorrência.
- **Pegadinha usada:** Olhar para elementos irrelevantes ao cenário..
- **Como pensar para acertar:** Quando aparecer lock, procure região crítica, recurso e espera.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 35

- **Alternativa correta:** D.
- **A) está errada:** Journaling não substitui backup.
- **B) está errada:** Backup deve cobrir dados relevantes e configuração conforme política.
- **C) está errada:** Logs podem ser importantes para auditoria e diagnóstico.
- **D) está correta:** Backup útil precisa ser recuperável e protegido.
- **Conceito cobrado:** Backup em sistemas operacionais.
- **Pegadinha usada:** Confundir consistência do FS com recuperação de dados..
- **Como pensar para acertar:** Backup bom é aquele que pode ser restaurado quando necessário.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 36

- **Alternativa correta:** C.
- **A) está errada:** Isolamento de processos e permissões de arquivos são controles distintos.
- **B) está errada:** Autenticação continua necessária.
- **C) está correta:** Espaços de endereçamento isolados protegem processos.
- **D) está errada:** Comunicação pode existir via mecanismos controlados de IPC.
- **Conceito cobrado:** Proteção e isolamento de processos.
- **Pegadinha usada:** Tratar isolamento como ausência total de comunicação..
- **Como pensar para acertar:** Isolamento protege; comunicação legítima ocorre por canais controlados.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 37

- **Alternativa correta:** B.
- **A) está errada:** Arquivo relativo não classifica perfil de processo.
- **B) está correta:** O gargalo principal parece ser processamento.
- **C) está errada:** I/O-bound esperaria muito por disco/rede, o que não foi descrito.
- **D) está errada:** Zumbi não consome CPU de forma útil.
- **Conceito cobrado:** CPU-bound.
- **Pegadinha usada:** Confundir consumo de CPU com espera de E/S..
- **Como pensar para acertar:** Olhe o recurso que fica no limite.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 38

- **Alternativa correta:** A.
- **A) está correta:** I e III estão corretas; II é falsa porque bloqueio pode ser espera normal de E/S.
- **B) está errada:** II é falsa e III é verdadeira.
- **C) está errada:** I deveria ser verdadeira.
- **D) está errada:** I deveria ser verdadeira.
- **Conceito cobrado:** Deadlock.
- **Pegadinha usada:** Bloqueado não é sinônimo de deadlock..
- **Como pensar para acertar:** Deadlock exige padrão de dependência; bloqueio isolado pode ser normal.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 39

- **Alternativa correta:** D.
- **A) está errada:** A alternativa inverte os conceitos.
- **B) está errada:** São controles relacionados, mas distintos.
- **C) está errada:** Autorização trata acesso a recursos em geral.
- **D) está correta:** Primeiro identifica; depois decide o que pode fazer.
- **Conceito cobrado:** Autenticação e autorização.
- **Pegadinha usada:** Confundir identidade com permissão..
- **Como pensar para acertar:** Pergunte: quem é o usuário? Depois: o que ele pode fazer?
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 40

- **Alternativa correta:** C.
- **A) está errada:** Interrupções ajudam multitarefa.
- **B) está errada:** O SO é o gerenciador típico da multitarefa.
- **C) está correta:** Escalonamento e interrupções permitem compartilhamento da CPU.
- **D) está errada:** Um núcleo pode alternar entre vários processos.
- **Conceito cobrado:** Multitarefa.
- **Pegadinha usada:** Achar que simultaneidade percebida exige núcleo por processo..
- **Como pensar para acertar:** Diferencie paralelismo real e concorrência por alternância.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 41

- **Alternativa correta:** B.
- **A) está errada:** Permissão não transforma arquivo em processo.
- **B) está correta:** A tríade usuário-grupo-outros controla permissões distintas.
- **C) está errada:** Sem permissão para outros, leitura não é garantida.
- **D) está errada:** Permissões do proprietário são avaliadas separadamente.
- **Conceito cobrado:** Permissões Linux.
- **Pegadinha usada:** Ignorar a tríade usuário/grupo/outros..
- **Como pensar para acertar:** Leia cada classe de permissão separadamente.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 42

- **Alternativa correta:** A.
- **A) está correta:** O kernel centraliza controle, segurança e abstração.
- **B) está errada:** A ideia é justamente evitar acesso físico manual direto.
- **C) está errada:** Sistemas de arquivos podem ter permissões; chamadas as respeitam.
- **D) está errada:** Kernel é núcleo do SO, não apenas GUI.
- **Conceito cobrado:** Kernel e chamadas de sistema.
- **Pegadinha usada:** Não perceber a função de proteção/abstração do SO..
- **Como pensar para acertar:** SO protege recursos e fornece serviços padronizados.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 43

- **Alternativa correta:** D.
- **A) está errada:** Isso define processo zumbi.
- **B) está errada:** Isso não define órfão.
- **C) está errada:** Liberação de mutex não define processo órfão.
- **D) está correta:** Órfão perde o pai original, mas pode continuar executando.
- **Conceito cobrado:** Processo órfão.
- **Pegadinha usada:** Confundir órfão com zumbi..
- **Como pensar para acertar:** Órfão perdeu o pai; zumbi já terminou e aguarda coleta.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 44

- **Alternativa correta:** B.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: muita troca gera lentidão.
- **B) é a incorreta:** Incorreta: swap em disco/SSD é muito mais lento que cache L1.
- **C) está correta como afirmação:** Correta: swap é usado como apoio.
- **D) está correta como afirmação:** Correta: armazenamento secundário é mais lento que RAM.
- **Conceito cobrado:** Swap e desempenho.
- **Pegadinha usada:** Tratar swap como memória rápida..
- **Como pensar para acertar:** Swap ajuda capacidade, mas cobra preço de desempenho.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 45

- **Alternativa correta:** B.
- **A) está errada:** Além de perigoso, chown não é diagnóstico de serviço.
- **B) está correta:** systemctl verifica serviços e journalctl consulta logs do systemd.
- **C) está errada:** chmod altera permissões e não diagnostica serviço por si só.
- **D) está errada:** Serviços do SO não são consultados por SQL comum.
- **Conceito cobrado:** Administração Linux com systemd.
- **Pegadinha usada:** Usar comando destrutivo ou fora do contexto..
- **Como pensar para acertar:** Para serviço, procure systemctl; para logs, journalctl.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 46

- **Alternativa correta:** A.
- **A) está correta:** NTFS permite controle de permissões no sistema de arquivos.
- **B) está errada:** Permissões dependem de identidade autenticada; não substituem autenticação.
- **C) está errada:** Permissões afetam acesso, não aparência.
- **D) está errada:** FAT32 não tem o mesmo modelo robusto de permissões NTFS.
- **Conceito cobrado:** Permissões NTFS.
- **Pegadinha usada:** Confundir autenticação e autorização..
- **Como pensar para acertar:** Permissão responde “pode acessar?” depois de saber quem é o usuário.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 47

- **Alternativa correta:** D.
- **A) está errada:** CPU-bound exigiria processamento intenso, não espera de rede.
- **B) está errada:** O processo ainda está ativo aguardando E/S.
- **C) está errada:** Não é tipo de interrupção; é perfil de processo.
- **D) está correta:** O desempenho depende de entrada/saída, como rede.
- **Conceito cobrado:** I/O-bound.
- **Pegadinha usada:** Confundir espera de rede com processamento intensivo..
- **Como pensar para acertar:** Se o processo espera dispositivo/rede/disco, pense em E/S.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 48

- **Alternativa correta:** C.
- **A) está errada:** Modos de endereçamento são outro tema.
- **B) está errada:** Backup incremental é política de cópia, não sincronização.
- **C) está correta:** Todos aparecem no estudo de controle de acesso concorrente.
- **D) está errada:** Sistemas de arquivos incluem NTFS, FAT32, ext4 etc.
- **Conceito cobrado:** Sincronização.
- **Pegadinha usada:** Confundir termos de concorrência com armazenamento..
- **Como pensar para acertar:** Quando o tema é acesso compartilhado, pense em sincronização.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 49

- **Alternativa correta:** B.
- **A) está errada:** Logs ajudam diagnóstico pós-incidente.
- **B) está correta:** Journal não garante recuperação de conteúdo perdido; backup continua essencial.
- **C) está errada:** Backups continuam necessários.
- **D) está errada:** Permissões não devem ser removidas como solução genérica.
- **Conceito cobrado:** Journaling e backup.
- **Pegadinha usada:** Confundir recuperação de consistência com recuperação completa de dados..
- **Como pensar para acertar:** Depois de falha, diferencie estrutura íntegra de dados recuperáveis.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentário da Questão 50

- **Alternativa correta:** A.
- **A) está correta:** Região crítica protege recurso compartilhado contra interleavings indevidos.
- **B) está errada:** Sincronização não aumenta armazenamento.
- **C) está errada:** Não há relação com cadastro de usuários.
- **D) está errada:** O escalonador continua existindo.
- **Conceito cobrado:** Região crítica.
- **Pegadinha usada:** Subestimar acesso concorrente..
- **Como pensar para acertar:** Se dois fluxos mexem no mesmo dado, pergunte como o acesso é protegido.
- **Referência à apostila de estudo:** Dia 2 — Sistemas Operacionais.

### Comentários das questões extras de revisão fixa do Dia 2

#### Comentário Extra Dia 2.1

- **Alternativa correta:** B.
- **A) está errada:** Publicidade é regra, mas admite restrições legais, como sigilo necessário e proteção de dados.
- **B) está correta:** A sigla LIMPE resume os princípios expressos mais cobrados.
- **C) está errada:** Mesmo na responsabilidade objetiva, são necessários dano e nexo causal.
- **D) está errada:** Finalidade pública é elemento essencial; interesse pessoal vicia o ato.
- **Conceito cobrado:** Princípios expressos da Administração Pública.
- **Pegadinha usada:** Trocar princípio expresso por princípio implícito ou absoluto.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.2

- **Alternativa correta:** A.
- **A) está correta:** Favorecimento pessoal é incompatível com impessoalidade.
- **B) está errada:** Autarquia tem personalidade jurídica própria e integra a Administração Indireta.
- **C) está errada:** Improbidade exige enquadramento legal e requisitos próprios; erro formal não basta automaticamente.
- **D) está errada:** Leilão é associado à alienação; pregão é usado para bens e serviços comuns.
- **Conceito cobrado:** Impessoalidade.
- **Pegadinha usada:** Confundir impessoalidade com ausência de identificação do agente.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.3

- **Alternativa correta:** D.
- **A) está errada:** Competência decorre da lei e não é simples escolha pessoal.
- **B) está errada:** Eficiência deve atuar junto da legalidade; resultado não justifica violar a lei.
- **C) está errada:** LAI e LGPD devem ser compatibilizadas; proteção de dados não anula automaticamente transparência pública.
- **D) está correta:** A distinção principal é órgão sem personalidade própria versus entidade com personalidade jurídica.
- **Conceito cobrado:** Organização administrativa.
- **Pegadinha usada:** Chamar autarquia de órgão da Administração Direta.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.4

- **Alternativa correta:** C.
- **A) está errada:** Inexigibilidade ocorre quando a competição é inviável; competição possível com autorização legal remete à dispensa.
- **B) está errada:** Finalidade pública é elemento essencial; interesse pessoal vicia o ato.
- **C) está correta:** A apostila associa o CRA-PR à natureza autárquica e à fiscalização profissional.
- **D) está errada:** Publicidade é regra, mas admite restrições legais, como sigilo necessário e proteção de dados.
- **Conceito cobrado:** Conselhos profissionais e autarquias.
- **Pegadinha usada:** Tratar conselho profissional como associação privada comum.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.5

- **Alternativa correta:** B.
- **A) está errada:** Mesmo na responsabilidade objetiva, são necessários dano e nexo causal.
- **B) está correta:** Esse é o ponto de prova mais direto sobre autarquias.
- **C) está errada:** Leilão é associado à alienação; pregão é usado para bens e serviços comuns.
- **D) está errada:** Autarquia tem personalidade jurídica própria e integra a Administração Indireta.
- **Conceito cobrado:** Autarquia.
- **Pegadinha usada:** Achar que toda entidade pública é órgão sem personalidade.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.6

- **Alternativa correta:** A.
- **A) está correta:** Competência é o poder legalmente atribuído ao agente ou órgão para praticar o ato.
- **B) está errada:** Improbidade exige enquadramento legal e requisitos próprios; erro formal não basta automaticamente.
- **C) está errada:** LAI e LGPD devem ser compatibilizadas; proteção de dados não anula automaticamente transparência pública.
- **D) está errada:** Competência decorre da lei e não é simples escolha pessoal.
- **Conceito cobrado:** Elementos do ato administrativo.
- **Pegadinha usada:** Confundir competência com motivo do ato.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.7

- **Alternativa correta:** D.
- **A) está errada:** Eficiência deve atuar junto da legalidade; resultado não justifica violar a lei.
- **B) está errada:** Publicidade é regra, mas admite restrições legais, como sigilo necessário e proteção de dados.
- **C) está errada:** Inexigibilidade ocorre quando a competição é inviável; competição possível com autorização legal remete à dispensa.
- **D) está correta:** Finalidade pública é elemento obrigatório do ato administrativo.
- **Conceito cobrado:** Finalidade pública.
- **Pegadinha usada:** Considerar conveniência pessoal como finalidade administrativa legítima.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.8

- **Alternativa correta:** C.
- **A) está errada:** Finalidade pública é elemento essencial; interesse pessoal vicia o ato.
- **B) está errada:** Autarquia tem personalidade jurídica própria e integra a Administração Indireta.
- **C) está correta:** Ato ilegal deve ser tratado pelo prisma da legalidade, não apenas da conveniência.
- **D) está errada:** Mesmo na responsabilidade objetiva, são necessários dano e nexo causal.
- **Conceito cobrado:** Controle do ato administrativo.
- **Pegadinha usada:** Confundir anulação por ilegalidade com revogação por mérito.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.9

- **Alternativa correta:** B.
- **A) está errada:** Leilão é associado à alienação; pregão é usado para bens e serviços comuns.
- **B) está correta:** Transparência pública convive com exceções justificadas.
- **C) está errada:** Competência decorre da lei e não é simples escolha pessoal.
- **D) está errada:** Improbidade exige enquadramento legal e requisitos próprios; erro formal não basta automaticamente.
- **Conceito cobrado:** LAI e publicidade.
- **Pegadinha usada:** Tratar publicidade como exposição irrestrita de todo dado.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.10

- **Alternativa correta:** A.
- **A) está correta:** A LGPD exige controle sobre por que e como dados pessoais são tratados.
- **B) está errada:** LAI e LGPD devem ser compatibilizadas; proteção de dados não anula automaticamente transparência pública.
- **C) está errada:** Inexigibilidade ocorre quando a competição é inviável; competição possível com autorização legal remete à dispensa.
- **D) está errada:** Eficiência deve atuar junto da legalidade; resultado não justifica violar a lei.
- **Conceito cobrado:** LGPD.
- **Pegadinha usada:** Achar que órgão público pode tratar qualquer dado sem finalidade.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.11

- **Alternativa correta:** D.
- **A) está errada:** Publicidade é regra, mas admite restrições legais, como sigilo necessário e proteção de dados.
- **B) está errada:** Mesmo na responsabilidade objetiva, são necessários dano e nexo causal.
- **C) está errada:** Finalidade pública é elemento essencial; interesse pessoal vicia o ato.
- **D) está correta:** A apostila reforça que erro administrativo não vira improbidade automaticamente.
- **Conceito cobrado:** Improbidade administrativa.
- **Pegadinha usada:** Equiparar ilegalidade simples a improbidade.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.12

- **Alternativa correta:** C.
- **A) está errada:** Autarquia tem personalidade jurídica própria e integra a Administração Indireta.
- **B) está errada:** Improbidade exige enquadramento legal e requisitos próprios; erro formal não basta automaticamente.
- **C) está correta:** Obter vantagem patrimonial indevida é o exemplo clássico de enriquecimento ilícito.
- **D) está errada:** Leilão é associado à alienação; pregão é usado para bens e serviços comuns.
- **Conceito cobrado:** Atos de improbidade.
- **Pegadinha usada:** Confundir vantagem pessoal com mera falha formal.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.13

- **Alternativa correta:** B.
- **A) está errada:** Competência decorre da lei e não é simples escolha pessoal.
- **B) está correta:** Edital vincula Administração e licitantes.
- **C) está errada:** Eficiência deve atuar junto da legalidade; resultado não justifica violar a lei.
- **D) está errada:** LAI e LGPD devem ser compatibilizadas; proteção de dados não anula automaticamente transparência pública.
- **Conceito cobrado:** Vinculação ao edital.
- **Pegadinha usada:** Achar que o edital é só orientação sem força vinculante.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.14

- **Alternativa correta:** A.
- **A) está correta:** Essa diferença é uma das mais cobradas em noções de licitação.
- **B) está errada:** Inexigibilidade ocorre quando a competição é inviável; competição possível com autorização legal remete à dispensa.
- **C) está errada:** Finalidade pública é elemento essencial; interesse pessoal vicia o ato.
- **D) está errada:** Publicidade é regra, mas admite restrições legais, como sigilo necessário e proteção de dados.
- **Conceito cobrado:** Contratação direta.
- **Pegadinha usada:** Inverter dispensa e inexigibilidade.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.15

- **Alternativa correta:** D.
- **A) está errada:** Mesmo na responsabilidade objetiva, são necessários dano e nexo causal.
- **B) está errada:** Leilão é associado à alienação; pregão é usado para bens e serviços comuns.
- **C) está errada:** Autarquia tem personalidade jurídica própria e integra a Administração Indireta.
- **D) está correta:** Pregão é a modalidade típica para bens e serviços comuns.
- **Conceito cobrado:** Modalidades de licitação.
- **Pegadinha usada:** Trocar pregão por leilão ou concurso.
- **Como pensar para acertar:** Localize o instituto pedido no comando e diferencie conceitos próximos antes de escolher a alternativa.

#### Comentário Extra Dia 2.16

- **Alternativa correta:** C.
- **A) está errada:** Com sentido de existir, 'haver' é impessoal e fica no singular.
- **B) está errada:** Com 'existir', o verbo concorda: existiam muitos processos.
- **C) está correta:** Verbo haver com sentido de existir permanece no singular.
- **D) está errada:** O particípio deve concordar: foram analisadas as planilhas.
- **Conceito cobrado:** Concordância verbal.
- **Pegadinha usada:** Flexionar indevidamente verbo impessoal.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.17

- **Alternativa correta:** B.
- **A) está errada:** O verbo possui complemento indireto e oração completiva.
- **B) está correta:** Pronome possessivo pode gerar ambiguidade referencial.
- **C) está errada:** Fora é mais-que-perfeito, não futuro.
- **D) está errada:** A ambiguidade permanece no pronome possessivo.
- **Conceito cobrado:** Ambiguidade.
- **Pegadinha usada:** Ignorar dupla referência possível.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.18

- **Alternativa correta:** A.
- **A) está correta:** 'Onde' retoma lugar físico.
- **B) está errada:** 'Onde' deve indicar lugar físico; 'situação em que' seria melhor.
- **C) está errada:** Para norma, use 'em que' ou 'na qual'.
- **D) está errada:** Não se trata propriamente de lugar físico.
- **Conceito cobrado:** Emprego de onde.
- **Pegadinha usada:** Usar 'onde' para qualquer referência abstrata.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.19

- **Alternativa correta:** D.
- **A) está errada:** A vírgula separa indevidamente sujeito e verbo.
- **B) está errada:** A vírgula fragmenta a locução introdutória.
- **C) está errada:** As vírgulas quebram relações sintáticas essenciais.
- **D) está correta:** Adjunto adverbial antecipado pode ser separado por vírgula.
- **Conceito cobrado:** Pontuação.
- **Pegadinha usada:** Separar sujeito e verbo por vírgula.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.20

- **Alternativa correta:** C.
- **A) está errada:** O texto diz o contrário: não elimina a necessidade.
- **B) está errada:** Não há ideia de proibição.
- **C) está correta:** A inferência deve respeitar a negação presente no texto.
- **D) está errada:** O trecho não afirma anulação.
- **Conceito cobrado:** Interpretação literal e inferência.
- **Pegadinha usada:** Ignorar o alcance do 'não'.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

---

# Dia 3 — Banco de Dados Base e SQL

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões principais

### Questão 1
**Nível: Médio**

Em um sistema do CRA, a tabela `profissional(id_profissional, nome, uf, situacao)` deve retornar apenas profissionais ativos do Paraná. A consulta correta é:

A) SELECT nome FROM profissional WHERE uf = 'PR' ORDER BY (situacao = 'ATIVO') DESC;
B) SELECT nome FROM profissional WHERE uf = 'PR' OR situacao = 'ATIVO';
C) SELECT nome FROM profissional WHERE uf = 'PR' AND situacao = 'ATIVO';
D) SELECT nome FROM profissional WHERE uf <> 'PR' AND situacao = 'ATIVO';

### Questão 2
**Nível: Médio**

A tabela `anuidade(id_anuidade, id_profissional, ano, valor)` deve retornar o total de anuidades por ano. Assinale a consulta adequada.

A) SELECT ano, COUNT(*) AS total FROM anuidade GROUP BY ano;
B) SELECT ano, COUNT(*) AS total FROM anuidade GROUP BY id_profissional;
C) SELECT ano, SUM(valor) AS total FROM anuidade GROUP BY ano;
D) SELECT COUNT(*) AS total FROM anuidade;

### Questão 3
**Nível: Médio**

Para listar apenas setores com mais de 20 profissionais cadastrados, considerando `profissional(id, setor)`, a consulta correta é:

A) SELECT setor, COUNT(*) FROM profissional WHERE setor IS NOT NULL GROUP BY setor;
B) SELECT setor, COUNT(*) FROM profissional GROUP BY setor ORDER BY COUNT(*) DESC FETCH FIRST 20 ROWS ONLY;
C) SELECT setor, COUNT(*) FROM profissional GROUP BY setor HAVING COUNT(*) >= 20;
D) SELECT setor, COUNT(*) FROM profissional GROUP BY setor HAVING COUNT(*) > 20;

### Questão 4
**Nível: Médio**

No modelo relacional, `id_profissional` em `anuidade` referenciando `profissional(id_profissional)` é exemplo de:

A) chave estrangeira.
B) chave primária de `anuidade`, porque identifica o profissional associado.
C) chave candidata que deve ser única em `anuidade`.
D) índice de pesquisa sem função de integridade referencial.

### Questão 5
**Nível: Médio**

Assinale a alternativa correta sobre chave primária.

A) Identifica unicamente cada linha e não aceita valor nulo.
B) Impede repetição, mas pode aceitar NULL porque equivale a uma restrição UNIQUE comum.
C) Deve ser simples; chaves compostas não podem exercer o papel de chave primária.
D) É escolhida entre as chaves candidatas, mas só passa a exigir unicidade quando referenciada por uma FK.

### Questão 6
**Nível: Médio**

Um relacionamento N:N entre `usuario` e `perfil` deve ser implementado, no modelo relacional, por:

A) uma coluna `perfis` em `usuario`, contendo os identificadores em uma lista delimitada.
B) uma FK `id_usuario` em `perfil`, permitindo que cada perfil aponte para apenas um usuário.
C) uma tabela associativa, como `usuario_perfil(id_usuario, id_perfil)`.
D) uma FK `id_perfil` em `usuario`, limitando cada usuário a um único perfil.

### Questão 7
**Nível: Médio**

Uma tabela `matricula(id_aluno, id_disciplina, nome_aluno, nome_disciplina)` tem chave composta `(id_aluno, id_disciplina)`. O problema de normalização mais evidente é:

A) violação de 1FN, porque uma chave composta impede que os atributos sejam atômicos.
B) violação de 2FN, pois cada nome depende de apenas uma parte da chave composta.
C) violação de 3FN exclusivamente, porque os nomes dependem transitivamente um do outro.
D) nenhuma violação, pois a combinação `(id_aluno, id_disciplina)` é única.

### Questão 8
**Nível: Médio**

A tabela `servidor(id_servidor, id_departamento, nome_departamento)` pode violar a 3FN porque:

A) há dependência parcial de `nome_departamento` em uma parte da chave composta de `servidor`.
B) o nome do departamento se repete em várias linhas, o que por si só viola a 1FN.
C) `id_servidor` determina `id_departamento`, que por sua vez determina `nome_departamento`.
D) qualquer FK para `departamento` é incompatível com a 3FN.

### Questão 9
**Nível: Médio**

Assinale a alternativa que diferencia corretamente `DELETE` e `DROP`.

A) `DELETE` remove linhas; `DROP` remove um objeto do banco, como a tabela.
B) `DELETE` sem WHERE remove linhas e a definição da tabela; `DROP` preserva a definição.
C) `DELETE` e `DROP` removem somente dados, diferenciando-se apenas pela possibilidade de ROLLBACK.
D) `DROP` esvazia a tabela e preserva sua estrutura para reutilização, enquanto `DELETE` exige filtro.

### Questão 10
**Nível: Médio**

Em `UPDATE profissional SET situacao = 'INATIVO';`, sem cláusula WHERE, o efeito provável é:

A) alterar a situação de todas as linhas da tabela.
B) alterar apenas a linha de menor chave primária, por ser a primeira do plano de execução.
C) ser rejeitado pelo SQL padrão, pois todo UPDATE exige predicado de seleção.
D) alterar somente as linhas que já estavam ativas, por inferência do valor atribuído.

### Questão 11
**Nível: Médio**

Para localizar registros sem e-mail cadastrado em `profissional(email)`, usa-se:

A) WHERE email = ''
B) WHERE email <> NULL
C) WHERE COALESCE(email, '') = ''
D) WHERE email IS NULL

### Questão 12
**Nível: Médio**

Considere `profissional(id, nome)` e `anuidade(id, id_profissional, ano)`. Para listar somente pares profissional–anuidade com correspondência pela chave, a consulta correta é:

A) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id = p.id;
B) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id_profissional = p.id;
C) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id_profissional = a.id;
D) SELECT p.nome, a.ano FROM profissional p CROSS JOIN anuidade a;

### Questão 13
**Nível: Médio**

Um relatório deve mostrar todos os profissionais, mesmo os que ainda não possuem anuidade lançada. A junção mais adequada, partindo de `profissional`, é:

A) CROSS JOIN anuidade, combinando cada profissional com todas as anuidades.
B) INNER JOIN anuidade ON anuidade.id_profissional = profissional.id.
C) RIGHT JOIN anuidade ON anuidade.id_profissional = profissional.id, preservando o lado de `anuidade`.
D) LEFT JOIN anuidade ON anuidade.id_profissional = profissional.id.

### Questão 14
**Nível: Médio**

Em SQL, `COUNT(*)` e `COUNT(email)` podem produzir resultados diferentes porque:

A) `COUNT(*)` ignora linhas nas quais qualquer coluna contenha NULL.
B) `COUNT(email)` ignora NULL nessa coluna, enquanto `COUNT(*)` conta as linhas.
C) as duas expressões sempre devolvem o mesmo total, independentemente dos dados.
D) `COUNT(email)` conta os NULLs, atribuindo zero a cada valor ausente.

### Questão 15
**Nível: Médio**

Assinale a alternativa correta sobre `PRIMARY KEY`, `UNIQUE` e `NOT NULL`.

A) `UNIQUE` e `NOT NULL` formam uma chave candidata e substituem automaticamente qualquer `PRIMARY KEY` já declarada.
B) `PRIMARY KEY` garante unicidade, mas permite NULL quando não existe uma restrição `NOT NULL` separada.
C) `PRIMARY KEY` impõe unicidade e não nulidade; `UNIQUE` veda duplicatas não nulas; `NOT NULL` veda nulos.
D) `NOT NULL` impede valores repetidos, enquanto `UNIQUE` exige preenchimento e define a chave primária da tabela.

### Questão 16
**Nível: Médio**

Um analista deseja impedir que `valor_anuidade` seja negativo. A restrição mais adequada é:

A) NOT NULL em `valor_anuidade`.
B) CHECK (valor_anuidade >= 0).
C) UNIQUE em `valor_anuidade`.
D) DEFAULT 0 para `valor_anuidade`.

### Questão 17
**Nível: Médio**

V/F: Sobre SQL.

I. `CREATE TABLE` é comando DDL.
II. `GRANT` é comando relacionado a controle de privilégios.
III. `COMMIT` desfaz uma transação confirmada.

A sequência correta é:

A) V, F, V.
B) V, V, F.
C) F, V, F.
D) V, V, V.

### Questão 18
**Nível: Médio**

Em uma transação de pagamento, o sistema deve registrar pagamento e baixar débito. Se a baixa falhar, o registro do pagamento também deve ser desfeito. Essa exigência representa:

A) consistência, porque toda regra válida implica desfazer todas as etapas.
B) isolamento, porque as duas operações não podem coexistir na mesma transação.
C) durabilidade, porque a falha ocorre antes de qualquer confirmação.
D) atomicidade, porque as etapas devem produzir um único resultado de tudo ou nada.

### Questão 19
**Nível: Médio**

Um índice criado sobre `numero_processo` tende a:

A) garantir unicidade de `numero_processo`, mesmo que o índice não tenha sido declarado UNIQUE.
B) acelerar qualquer consulta da tabela, sem custo mensurável para operações de escrita.
C) melhorar consultas compatíveis com a chave do índice, ao custo de espaço e manutenção nas escritas.
D) eliminar toda varredura da tabela, inclusive em filtros que não utilizem a coluna indexada.

### Questão 20
**Nível: Médio**

Uma view `vw_profissionais_ativos` pode ser usada para:

A) armazenar obrigatoriamente uma cópia física autônoma dos dados retornados.
B) conceder acesso aos dados subjacentes independentemente das permissões configuradas.
C) aceitar INSERT, UPDATE e DELETE em qualquer definição, sem restrições do SGBD.
D) oferecer uma visão lógica baseada em consulta, que pode filtrar e projetar dados.

### Questão 21
**Nível: Difícil**

Uma trigger `AFTER INSERT` em `anuidade` registra auditoria na mesma transação do comando que a disparou. Não há transação autônoma específica. Se a transação principal sofrer `ROLLBACK`, é correto afirmar que:

A) a trigger somente será executada depois do COMMIT, razão pela qual sua auditoria sempre persistirá.
B) a trigger é executada pelo evento e seu registro de auditoria normalmente também será desfeito pelo ROLLBACK.
C) a aplicação precisa executar `CALL trigger_auditoria` antes do ROLLBACK.
D) o registro produzido pela trigger não participa das propriedades ACID da transação principal.

### Questão 22
**Nível: Difícil**

Uma rotina `registrar_pagamento` deve receber parâmetros, validar dados, inserir o pagamento e atualizar o débito quando chamada pela aplicação. A solução mais compatível é:

A) uma stored procedure, que encapsula comandos e lógica sob chamada explícita.
B) uma trigger, pois triggers são chamadas explicitamente pela aplicação.
C) uma restrição CHECK, capaz de executar vários comandos DML.
D) uma view, pois toda view aceita parâmetros e executa alterações encadeadas.

### Questão 23
**Nível: Difícil**

Considere `π_nome(σ_uf = 'PR' ∧ situacao = 'ATIVO'(Profissional))`. Essa expressão de álgebra relacional representa:

A) todas as colunas dos profissionais, agrupadas por UF e situação.
B) apenas os nomes de todos os profissionais, ordenados por UF.
C) a quantidade de profissionais ativos em cada UF.
D) os nomes dos profissionais cujas tuplas satisfazem simultaneamente UF e situação.

### Questão 24
**Nível: Difícil**

Um processo pode possuir nenhuma ou várias fiscalizações. Cada fiscalização tem número próprio, data, resultado e responsável. No MER, a representação mais adequada é:

A) guardar todas as fiscalizações em um único atributo multivalorado de `Processo`.
B) transformar `Fiscalizacao` em domínio do atributo `resultado`.
C) modelar `Fiscalizacao` como entidade relacionada a `Processo` em 1:N.
D) representar cada fiscalização como atributo derivado, sem identidade nem dados próprios.

### Questão 25
**Nível: Difícil**

Uma pessoa pode ter vários telefones, e cada telefone possui tipo e indicação de principal. O mapeamento relacional que melhor preserva a 1FN é:

A) repetir todos os dados de `Pessoa` em uma nova linha para cada telefone.
B) adicionar `telefone1`, `telefone2` e `telefone3` à tabela `Pessoa`.
C) armazenar telefone, tipo e indicador em uma string delimitada.
D) criar uma tabela `PessoaTelefone`, com FK para `Pessoa` e uma chave adequada.

### Questão 26
**Nível: Difícil**

O DBA altera organização em disco, particionamento e índices, mas mantém tabelas, colunas e consultas usadas pela aplicação. Isso exemplifica:

A) independência lógica, porque o modelo conceitual foi substituído.
B) integridade referencial, porque as FKs permaneceram válidas.
C) independência física, pois a implementação mudou sem alterar o esquema lógico.
D) durabilidade, porque toda mudança física exige COMMIT.

### Questão 27
**Nível: Difícil**

Antes de executar um `ALTER TABLE`, o analista consulta o catálogo do SGBD para descobrir tipos, valores padrão, restrições e índices existentes. Ele está consultando:

A) metadados mantidos no dicionário de dados.
B) exclusivamente o log de transações.
C) dados operacionais produzidos pelos usuários.
D) uma cópia física obrigatória das tabelas de negócio.

### Questão 28
**Nível: Difícil**

Considere `lancamento(id_lancamento PK, setor, valor)`, com vários lançamentos por setor: `SELECT setor, id_lancamento, SUM(valor) FROM lancamento GROUP BY setor;`. Em regras SQL usuais, o problema é que:

A) a presença da PK no SELECT dispensa sua agregação ou inclusão no GROUP BY.
B) `id_lancamento` não está agregado, não integra o GROUP BY e não é determinado por `setor`.
C) SUM só pode ser usada quando também existe uma cláusula HAVING.
D) a função agregada deveria aparecer antes das demais expressões no SELECT.

### Questão 29
**Nível: Difícil**

Dentro de uma transação ainda não confirmada, executa-se `DELETE FROM profissional WHERE situacao = 'INATIVO';`. É correto afirmar que:

A) o comando exclui o objeto `profissional` e suas restrições, mas preserva os dados para eventual `ROLLBACK`.
B) a remoção das linhas-pai sempre exclui as linhas filhas, ainda que a FK esteja configurada com `RESTRICT`.
C) o DELETE remove as linhas permitidas e pode ser desfeito por ROLLBACK antes do COMMIT.
D) por ser uma operação DML, a exclusão torna-se irreversível ao fim do comando, mesmo sem `COMMIT` explícito.

### Questão 30
**Nível: Difícil**

Considere `profissional(id INTEGER GENERATED ALWAYS AS IDENTITY, nome VARCHAR(100) NOT NULL, uf CHAR(2) NOT NULL DEFAULT 'PR')`. Para inserir Ana e Bruno usando o valor padrão de `uf`, emprega-se:

A) `INSERT INTO profissional (nome, uf) VALUES ('Ana', NULL), ('Bruno', NULL);`
B) `INSERT INTO profissional VALUES ('Ana'), ('Bruno');`
C) `UPDATE profissional SET nome IN ('Ana', 'Bruno');`
D) `INSERT INTO profissional (nome) VALUES ('Ana'), ('Bruno');`

### Questão 31
**Nível: Difícil**

Sobre níveis de isolamento, considerada a classificação ANSI clássica e ressalvadas implementações mais fortes dos SGBDs, assinale a correta.

A) REPEATABLE READ impede leituras sujas e não repetíveis; o tratamento de fantasmas deve ser conferido no padrão e no SGBD.
B) READ COMMITTED garante que duas leituras da mesma linha, na mesma transação, sempre retornem o mesmo valor.
C) READ UNCOMMITTED impede leitura de valores ainda não confirmados.
D) SERIALIZABLE elimina a necessidade de COMMIT e de mecanismos de controle de concorrência.

### Questão 32
**Nível: Difícil**

Uma tabela possui `id_pessoa` como PK e `cpf` com restrição UNIQUE, mas sem NOT NULL. A interpretação mais precisa é:

A) a restrição `UNIQUE` transforma `cpf` em nova chave primária e substitui automaticamente `id_pessoa`.
B) `id_pessoa` segue como PK; CPF não nulo duplicado é rejeitado, e NULL varia conforme o SGBD.
C) `UNIQUE` também impõe `NOT NULL` em todos os SGBDs, tornando obrigatório o preenchimento de `cpf`.
D) a unicidade de `cpf` permite repetir `id_pessoa` quando cada ocorrência estiver associada a um CPF distinto.

### Questão 33
**Nível: Difícil**

Para listar todos os profissionais e, quando existente, o nome de sua cidade, considerando `profissional(id, nome, id_cidade)` e `cidade(id, nome)`, usa-se:

A) `SELECT p.nome, c.nome FROM profissional p LEFT JOIN cidade c ON c.id = p.id_cidade WHERE c.id IS NOT NULL;`
B) `SELECT p.nome, c.nome FROM profissional p INNER JOIN cidade c ON c.id = p.id_cidade;`
C) `SELECT p.nome, c.nome FROM profissional p LEFT JOIN cidade c ON c.id = p.id;`
D) `SELECT p.nome, c.nome FROM profissional p LEFT JOIN cidade c ON c.id = p.id_cidade;`

### Questão 34
**Nível: Difícil**

Assinale a afirmativa incorreta sobre normalização e decomposição.

A) Com chave candidata simples, não existe dependência parcial dessa chave a ser removida pela 2FN.
B) Uma cadeia chave → atributo não chave → outro atributo não chave pode indicar violação de 3FN.
C) Qualquer decomposição que distribua colunas em duas tabelas preserva dados e dependências automaticamente.
D) Normalização reduz redundâncias e anomalias, mas pode aumentar a necessidade de junções.

### Questão 35
**Nível: Difícil**

Usando sintaxe SQL com FETCH, deseja-se retornar no máximo três linhas de anuidade com maior `valor`, usando o menor `id_anuidade` como desempate. A consulta correta é:

A) `SELECT * FROM anuidade ORDER BY valor DESC, id_anuidade ASC FETCH FIRST 3 ROWS ONLY;`
B) `SELECT * FROM anuidade ORDER BY valor ASC, id_anuidade ASC FETCH FIRST 3 ROWS ONLY;`
C) `SELECT * FROM anuidade ORDER BY valor DESC, id_anuidade ASC OFFSET 3 ROWS;`
D) `SELECT * FROM anuidade FETCH FIRST 3 ROWS ONLY;`

### Questão 36
**Nível: Difícil**

Sobre DELETE, TRUNCATE e DROP, assinale a alternativa correta.

A) DELETE sem WHERE e TRUNCATE têm comportamento transacional, de log e identidade idêntico em qualquer SGBD.
B) TRUNCATE esvazia a tabela sem predicado e preserva o objeto; transação, FKs e identidade variam por SGBD.
C) TRUNCATE aceita WHERE para selecionar individualmente as linhas removidas.
D) DROP TABLE esvazia a tabela, mas preserva estrutura e restrições.

### Questão 37
**Nível: Difícil**

Deseja-se listar todos os setores, inclusive os que não possuem profissional ativo, com a respectiva contagem. A consulta correta é:

A) `SELECT s.id, COUNT(p.id) FROM setor s LEFT JOIN profissional p ON p.id_setor = s.id WHERE p.ativo = 1 GROUP BY s.id;`
B) `SELECT s.id, COUNT(p.id) FROM setor s LEFT JOIN profissional p ON p.id_setor = s.id AND p.ativo = 1 GROUP BY s.id;`
C) `SELECT s.id, COUNT(*) FROM setor s LEFT JOIN profissional p ON p.id_setor = s.id AND p.ativo = 1 GROUP BY s.id;`
D) `SELECT s.id, COUNT(p.id) FROM setor s INNER JOIN profissional p ON p.id_setor = s.id AND p.ativo = 1 GROUP BY s.id;`

### Questão 38
**Nível: Difícil**

Um profissional pode responder por várias pessoas jurídicas, e cada pessoa jurídica pode possuir vários responsáveis ao longo do tempo. O vínculo guarda início, fim e situação. A melhor solução é:

A) colocar uma única FK `id_pessoa_juridica` em `Profissional`.
B) colocar uma única FK `id_responsavel_atual` em `PessoaJuridica`.
C) criar tabela associativa com FKs, período, situação e restrições de integridade.
D) guardar nomes e períodos em uma coluna textual de histórico.

### Questão 39
**Nível: Difícil**

É necessário produzir backup lógico consistente enquanto o banco permanece disponível para escritas concorrentes. A conduta mais segura é:

A) usar ferramenta do SGBD com snapshot ou exportação consistente e validar o resultado mediante teste de restauração.
B) exportar cada tabela por consultas independentes, sem snapshot ou coordenação transacional.
C) copiar diretamente os arquivos físicos abertos pelo SGBD.
D) criar índices adicionais, pois eles substituem mecanismos de backup e recuperação.

### Questão 40
**Nível: Difícil**

A coluna `documento.tags` contém valores como `fiscalização;anuidade;recurso`. Para consultar e restringir cada tag com integridade relacional, a melhor remodelagem é:

A) conservar a string e validar cada tag apenas com LIKE.
B) duplicar toda a linha de `Documento` para cada tag.
C) criar colunas fixas `tag1`, `tag2`, `tag3` e `tag4`.
D) criar `DocumentoTag`, com uma tag por linha e FK para `Documento`.

### Questão 41
**Nível: Muito difícil**

A tabela já possui `id` como PK. `numero_registro` deve ser obrigatório e único, enquanto `situacao` só pode assumir `A` ou `I`. A definição mais adequada é:

A) `numero_registro VARCHAR(20) REFERENCES profissional(numero_registro), situacao CHAR(1)`
B) `numero_registro VARCHAR(20) PRIMARY KEY, situacao CHAR(1)`
C) `numero_registro VARCHAR(20) CHECK (numero_registro IS NOT NULL), situacao CHAR(1)`
D) `numero_registro VARCHAR(20) NOT NULL UNIQUE, situacao CHAR(1) NOT NULL CHECK (situacao IN ('A','I'))`

### Questão 42
**Nível: Muito difícil**

Uma plataforma mantém visões externas sobre um esquema lógico comum. O DBA reorganiza índices e partições sem alterar essas visões; em paralelo, o sistema precisa isolar transações concorrentes e recuperar commits após falha. A conclusão tecnicamente correta é:

A) toda reorganização física exige reescrever as visões externas, enquanto o rollback, sozinho, assegura a persistência dos commits.
B) o SGBD fornece independência física por meio dos mapeamentos entre níveis e coordena concorrência, log e recuperação para preservar as transações.
C) cada visão externa deve possuir esquema lógico próprio, e cópias periódicas do banco substituem o controle de isolamento entre transações.
D) a linguagem SQL, independentemente do SGBD, implementa os mapeamentos entre níveis e restaura automaticamente os commits após falha.

### Questão 43
**Nível: Muito difícil**

O usuário `relatorio` deve consultar apenas `id` e `nome` dos profissionais ativos, sem acessar CPF, linhas inativas ou operações de escrita. Considerando o menor privilégio e uma solução independente do filtro da aplicação, a configuração mais adequada é:

A) criar uma view que projete `id` e `nome` e filtre `situacao = 'A'`, concedendo `SELECT` apenas sobre essa view e nenhum privilégio sobre a tabela-base.
B) conceder `SELECT` sobre a tabela-base e exigir que cada relatório aplique corretamente o filtro de situação e omita o CPF.
C) conceder `SELECT (id, nome)` sobre a tabela-base, pois a restrição de colunas também impede, por si só, a leitura de linhas inativas.
D) criar a view filtrada, mas manter também `SELECT` sobre a tabela-base para que o usuário possa validar os dados exibidos.

### Questão 44
**Nível: Muito difícil**

Várias aplicações atualizam `profissional`, e toda alteração deve gerar auditoria centralizada com valores anteriores e novos. A alternativa mais adequada é:

A) associar uma trigger ao UPDATE, registrando valores anteriores e novos e observando transação, recursão e volume.
B) depender de cada aplicação para inserir voluntariamente a auditoria após atualizar a linha.
C) criar uma view simples, pois toda view intercepta automaticamente alterações nas tabelas-base.
D) criar um índice, pois índices mantêm histórico completo das versões anteriores de cada linha.

### Questão 45
**Nível: Muito difícil**

Um profissional pode não possuir anuidade ou possuir várias, cada anuidade pertence exatamente a um profissional e não pode existir mais de uma anuidade do mesmo profissional no mesmo exercício. Qual implementação traduz simultaneamente cardinalidade, participação e unicidade temporal?

A) manter `profissional_id` anulável em `Anuidade` e criar índice simples por `exercicio`, permitindo anuidades sem profissional.
B) armazenar em `Profissional` uma FK obrigatória para uma única anuidade, repetindo a linha do profissional a cada novo exercício.
C) usar `Anuidade.profissional_id` como FK `NOT NULL` e impor `UNIQUE (profissional_id, exercicio)`, sem exigir que todo profissional possua linha em `Anuidade`.
D) criar uma tabela associativa entre `Profissional` e `Anuidade`, com FKs anuláveis, para representar um relacionamento muitos-para-muitos.

### Questão 46
**Nível: Muito difícil**

Considere `Servidor(id_servidor, nome, id_departamento, nome_departamento)`, com `id_servidor → id_departamento` e `id_departamento → nome_departamento`. A decomposição adequada para eliminar a dependência transitiva é:

A) manter `Servidor(id_servidor, nome)` e descartar os atributos de departamento, pois dependências transitivas devem ser eliminadas com perda de informação.
B) conservar a tabela original e declarar `nome_departamento` como `UNIQUE`, impedindo que dois servidores pertençam ao mesmo departamento.
C) separar `Servidor` e `Departamento`, ligados por `id_departamento` como FK.
D) criar `Departamento(id_servidor, nome_departamento)` e retirar `id_departamento`, usando o servidor como identificador da unidade administrativa.

### Questão 47
**Nível: Muito difícil**

A tabela contém `(uf, situacao)` = `(PR,A)`, `(PR,A)`, `(PR,I)`, `(NULL,A)` e `(NULL,A)`. O resultado de `SELECT DISTINCT uf, situacao FROM profissional` possui:

A) duas linhas, porque DISTINCT considera apenas `uf` e ignora `situacao`.
B) cinco linhas, porque DISTINCT não atua quando a projeção possui mais de uma coluna.
C) quatro combinações, pois cada NULL é sempre distinto de outro NULL na eliminação de duplicatas.
D) três combinações: `(PR,A)`, `(PR,I)` e uma ocorrência de `(NULL,A)`.

### Questão 48
**Nível: Muito difícil**

A transação T1 atualiza um cadastro e recebe confirmação de `COMMIT`. Em seguida, T2 altera o mesmo cadastro, mas o servidor falha antes do commit de T2. Após a recuperação, qual estado respeita ACID e o papel do log de recuperação?

A) reaplicar T1 e T2, pois toda alteração registrada em memória antes da falha deve tornar-se durável.
B) preservar os efeitos confirmados de T1 e desfazer os efeitos incompletos de T2, combinando durabilidade e atomicidade.
C) desfazer T1 e preservar T2, pois a transação mais recente substitui a anterior mesmo sem confirmação.
D) desfazer ambas, pois o isolamento impede que qualquer transação sobreviva a uma falha do servidor.

### Questão 49
**Nível: Muito difícil**

Assinale a afirmativa incorreta sobre junções externas.

A) Um predicado no WHERE que rejeite NULL da tabela direita pode eliminar linhas preservadas por LEFT JOIN.
B) Mover qualquer predicado entre ON e WHERE nunca altera o resultado de uma junção externa.
C) Após LEFT JOIN, COUNT(chave_da_direita) conta correspondências, enquanto COUNT(*) também conta a linha estendida por NULL.
D) Um filtro da tabela direita colocado no ON pode restringir correspondências sem eliminar a linha da esquerda.

### Questão 50
**Nível: Muito difícil**

Considere `SELECT situacao, COUNT(*) AS total FROM profissional WHERE uf = 'PR' GROUP BY situacao HAVING COUNT(*) >= 10 ORDER BY total DESC;`. A consulta:

A) filtra o Paraná, agrupa por situação, exige dez linhas por grupo e ordena pelo total.
B) mantém profissionais individuais cujo identificador seja maior ou igual a dez e os ordena pela situação cadastral.
C) ordena as linhas antes dos filtros, elimina situações repetidas da tabela física e então calcula o total de cada grupo.
D) agrupa inicialmente todas as UFs e somente depois do `HAVING` seleciona os registros do Paraná pelo `WHERE`.

## Questões extras de revisão fixa do Dia 3

#### Extra Dia 3.1

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Sanções ético-disciplinares
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Em caso de infração ética, a aplicação de sanção pelo sistema profissional deve observar qual diretriz geral?

A) Toda infração ética deve ser julgada originariamente pelo CFA, ainda que o fato pertença à jurisdição regional.
B) Havendo prova documental, o CRA pode aplicar a sanção definitiva sem ouvir o acusado, deixando a defesa apenas para eventual recurso.
C) A competência sancionadora deve ser exercida em apuração regular, com contraditório e defesa.
D) A denúncia transfere ao denunciante a escolha da penalidade, cabendo ao Conselho apenas executá-la.

#### Extra Dia 3.2

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Código de Ética e pessoa jurídica
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Sobre pessoas jurídicas no Código de Ética estudado, assinale a alternativa correta.

A) A RN CFA nº 671/2025 também alcança pessoas jurídicas, observadas as especificidades indicadas para elas.
B) A RN CFA nº 651/2024 é o Código de Ética, e a RN CFA nº 671/2025 trata exclusivamente do Regimento do CRA-PR.
C) A RN CFA nº 671/2025 disciplina somente pessoas físicas, pois pessoas jurídicas ficam fora de qualquer parâmetro ético.
D) Alcançar pessoas jurídicas significa aplicar automaticamente a elas todas as sanções previstas para profissionais, sem distinção.

#### Extra Dia 3.3

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Sanções e pessoa jurídica
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Uma questão afirma que suspensão e cancelamento previstos para profissionais se aplicam indistintamente à pessoa jurídica. Conforme a apostila, assinale a alternativa correta.

A) A suspensão aplica-se à pessoa jurídica, mas o cancelamento fica reservado ao profissional.
B) A aplicação indistinta é problemática, pois o material ressalta que suspensão e cancelamento não se aplicam à pessoa jurídica na RN CFA nº 671/2025.
C) O cancelamento aplica-se à pessoa jurídica, mas a suspensão só pode alcançar o responsável técnico.
D) As duas sanções aplicam-se à pessoa jurídica sempre que houver dano econômico, ainda que a norma estabeleça tratamento diverso.

#### Extra Dia 3.4

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Jurisdição regional
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Sobre jurisdição do CRA-PR, assinale a alternativa correta.

A) O registro originário no Paraná confere ao CRA-PR jurisdição fiscalizatória sobre o profissional em todo o território nacional.
B) O CFA executa ordinariamente registro, fiscalização e julgamento inicial de todos os fatos ocorridos no Paraná.
C) A atuação do CRA-PR vincula-se ao Paraná, sem afastar a coordenação normativa e as competências nacionais do Sistema CFA/CRAs.
D) Qualquer CRA pode sancionar fato ocorrido no Paraná, porque a validade nacional do registro elimina limites territoriais.

#### Extra Dia 3.5

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Importância do Regimento
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Uma alternativa afirma que o Regimento Interno é irrelevante porque não trata de SQL, redes ou sistemas. Assinale a correta.

A) O Regimento interessa somente aos empregados da área jurídica, não ao cargo de Analista de Sistemas previsto no mesmo edital.
B) O Regimento tem função apenas cerimonial e não produz regras internas sobre funcionamento ou competências.
C) Por ser norma interna, o Regimento pode afastar a lei federal e as normas gerais do CFA em matéria regional.
D) O Regimento é conteúdo expresso e organiza competências, órgãos e funcionamento do CRA-PR.

#### Extra Dia 3.6

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Exercício sem registro
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Um fiscal do CRA atua em caso de exercício profissional sem registro. Assinale a alternativa que melhor representa a lógica da fiscalização.

A) A fiscalização só pode começar após denúncia formal de outro órgão público.
B) A fiscalização verifica a regularidade do exercício no campo da Administração, inclusive registro e atividade.
C) A fiscalização limita-se a verificar pagamento de anuidade, sem examinar habilitação ou atividade exercida.
D) Toda inspeção local deve ser executada diretamente pelo CFA, cabendo ao CRA apenas arquivar o resultado.

#### Extra Dia 3.7

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Publicidade profissional
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Sobre publicidade profissional no campo ético, assinale a alternativa correta.

A) A divulgação deve evitar informação enganosa, uso indevido de título e promessa incompatível com a ética.
B) É permitida promessa de resultado certo quando o profissional possui experiência comprovada.
C) O uso de título profissional sem habilitação deixa de ser irregular se o anúncio informar que se trata de nome comercial.
D) A disciplina ética alcança a execução contratual, mas não a forma de captação ou apresentação pública do serviço.

#### Extra Dia 3.8

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Registro e exercício profissional
**Nível:** Médio
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Uma sociedade empresária contrata pessoa sem registro para executar atividade típica fiscalizada pelo CRA. Assinale a alternativa correta.

A) O contrato transfere integralmente à empresa a responsabilidade pelo exercício, tornando irrelevante o registro do executor.
B) O diploma do contratado basta para o exercício regular, ainda que falte o registro profissional exigível.
C) Somente o profissional pode ser examinado pelo Sistema; a organização que explora a atividade fica sempre fora da fiscalização.
D) O caso pode envolver exercício profissional irregular e responsabilidade da organização, exigindo análise pelo CRA competente.

#### Extra Dia 3.9

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Regularidade registral
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Sobre atualização cadastral e regularidade perante conselho profissional, assinale a alternativa mais precisa.

A) A atualização do endereço, por si só, regulariza exercício antes praticado sem o registro exigível.
B) Atualização cadastral e registro regular facilitam a fiscalização, sem afastar os deveres profissionais.
C) Uma inscrição ativa em qualquer Regional torna desnecessário comunicar mudança relevante de jurisdição ou de dados.
D) A certidão cadastral transfere ao Conselho a responsabilidade técnica pelos atos do registrado.

#### Extra Dia 3.10

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Finalidade institucional da fiscalização profissional
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Sobre a finalidade institucional da fiscalização exercida pelo Sistema CFA/CRAs, assinale a alternativa correta.

A) Sua finalidade principal é assegurar reserva econômica aos registrados, independentemente da qualidade dos serviços prestados à sociedade.
B) A fiscalização busca proteger a sociedade e verificar a regularidade do exercício profissional no campo da Administração.
C) Sua atuação limita-se à cobrança de anuidades, sem alcançar habilitação, registro ou atividade efetivamente exercida.
D) A fiscalização regional substitui o Poder Judiciário na solução definitiva de todo conflito contratual envolvendo profissionais.

#### Extra Dia 3.11

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Registro e fiscalização de pessoa jurídica
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Uma pessoa jurídica oferece habitualmente serviços inseridos no campo da Administração no Paraná. À luz da lógica de registro e fiscalização estudada, assinale a alternativa correta.

A) A natureza da atividade pode sujeitar a pessoa jurídica ao registro e à fiscalização do CRA-PR, conforme a legislação aplicável.
B) A existência de CNPJ afasta, por si só, qualquer exigência relacionada ao conselho profissional.
C) Apenas pessoas físicas podem ser fiscalizadas, ainda que a empresa explore atividade profissional sujeita ao Sistema CFA/CRAs.
D) A empresa somente pode ser examinada pelo CFA, porque os Conselhos Regionais não atuam sobre pessoas jurídicas.

#### Extra Dia 3.12

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Fiscalização e ética
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Sobre o vínculo entre ética e fiscalização, assinale a alternativa correta.

A) A fiscalização verifica o exercício; a ética disciplina a conduta, podendo ambas incidir no mesmo fato.
B) A fiscalização examina apenas pessoas jurídicas, enquanto a ética alcança somente pessoas físicas.
C) A apuração ética substitui toda verificação de habilitação, registro e enquadramento da atividade.
D) Fiscalização e ética são sinônimos: comprovar registro regular encerra qualquer análise de conduta.

#### Extra Dia 3.13

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Independência técnica diante de pressão do cliente
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Um cliente pressiona o profissional a assinar conclusão que não encontra suporte nos dados analisados. À luz da independência técnica estudada, a conduta adequada é:

A) Assinar a conclusão solicitada, desde que o cliente assuma verbalmente a responsabilidade pelo conteúdo.
B) Validar o documento porque a vontade do contratante prevalece sobre o juízo técnico de quem o subscreve.
C) Retirar os dados contrários à conclusão para evitar divergência, mantendo apenas os elementos favoráveis ao cliente.
D) Recusar a validação sem suporte e manter somente conclusão que possa ser tecnicamente fundamentada.

#### Extra Dia 3.14

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Processo ético-disciplinar
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Sobre defesa e recurso em processo disciplinar, assinale a alternativa correta em termos gerais.

A) A competência pode ser escolhida pelo denunciante, desde que o acusado receba cópia da decisão final.
B) A defesa apresentada somente depois do encerramento definitivo sempre convalida a ausência de contraditório na instrução.
C) A atuação sancionadora deve observar órgão competente, ciência dos fatos, oportunidade de defesa e decisão fundamentada.
D) A existência de recurso permite que a primeira instância aplique qualquer sanção antes de instaurar procedimento.

#### Extra Dia 3.15

**Dia:** 3
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Competência e jurisdição
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4)

Uma questão mistura CFA, CRA-PR e Conselho Regional de outro Estado em um caso com registro, fiscalização e recurso. Qual estratégia é mais segura?

A) Atribuir ao CFA registro e fiscalização ordinários sempre que o profissional atue fora do estado de sua inscrição original.
B) Permitir que um CRA de outro Estado determine diretamente a sanção no Paraná, sem observar a distribuição institucional.
C) Atribuir todo julgamento ao CRA do primeiro registro, mesmo quando o fato e a atividade ocorram em outra jurisdição.
D) Separar competência nacional, execução regional e jurisdição territorial antes de classificar o ato.

#### Extra Dia 3.16

**Dia:** 3
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Língua Portuguesa
**Assunto:** Uso dos porquês
**Nível:** Difícil
**Referência:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5)

Assinale a alternativa em que todas as formas destacadas estão empregadas corretamente.

A) O relatório não explicou **porque** o acesso falhou nem o **por que** da demora.
B) A equipe perguntou **por quê** o serviço parou e registrou o **porque** no chamado.
C) Perguntou-se **por que** falhou, explicou-se **porque** faltou espaço e registrou-se o **porquê**.
D) Ninguém informou **porquê** a fila cresceu; ela cresceu **por que** faltou capacidade.

#### Extra Dia 3.17

**Dia:** 3
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Língua Portuguesa
**Assunto:** Regência verbal
**Nível:** Muito difícil
**Referência:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5)

Assinale a frase em que as duas regências verbais estão adequadas à norma-padrão.

A) O candidato aspirava o cargo e obedeceu o edital durante a preparação.
B) O candidato recorreu da decisão e assistiu ao julgamento do recurso.
C) O candidato preferiu recorrer do que aceitar a decisão e informou o resultado os colegas.
D) O candidato assistiu o julgamento e chegou no órgão antes da sessão.

#### Extra Dia 3.18

**Dia:** 3
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Língua Portuguesa
**Assunto:** Coesão sequencial, equivalência de conectores e preservação de inferência
**Nível:** Muito difícil
**Referência:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5)

Leia: “O índice reduziu o custo das leituras; contudo, elevou a manutenção das escritas. Portanto, sua adoção deve considerar o padrão de uso.” Qual reescrita preserva tanto a oposição entre os dois efeitos quanto a conclusão derivada desse contraste?

A) O índice reduziu o custo das leituras; por isso, elevou a manutenção das escritas; contudo, deve-se considerar o padrão de uso.
B) Embora o índice reduzisse o custo das leituras, elevou a manutenção das escritas, porque sua adoção considera o padrão de uso.
C) O índice reduziu o custo das leituras; entretanto, elevou a manutenção das escritas. Logo, sua adoção deve considerar o padrão de uso.
D) O índice reduziu o custo das leituras e elevou a manutenção das escritas, se sua adoção considerar o padrão de uso.

#### Extra Dia 3.19

**Dia:** 3
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Língua Portuguesa
**Assunto:** Formulação de tese, relação causal condicionada e projeto argumentativo
**Nível:** Muito difícil
**Referência:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5)

Uma discursiva pede posicionamento sobre transformação digital no serviço público, com análise de ganhos, riscos e efeitos sobre usuários vulneráveis. Qual tese delimita uma relação causal defensável e oferece critérios para organizar o desenvolvimento?

A) A digitalização deve avançar sempre que reduzir custos, deixando segurança e acessibilidade para ajustes posteriores à implantação.
B) A manutenção de atendimento presencial basta para garantir inclusão, de modo que métricas de desempenho e segurança se tornam secundárias.
C) A tecnologia é neutra, e os resultados da transformação digital dependem exclusivamente do treinamento oferecido aos servidores.
D) A transformação digital amplia eficiência e acesso quando integra segurança, interoperabilidade, acessibilidade e canais alternativos, com avaliação por indicadores.

#### Extra Dia 3.20

**Dia:** 3
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Língua Portuguesa
**Assunto:** Concordância nominal e verbal
**Nível:** Muito difícil
**Referência:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5)

Assinale a alternativa em que todas as concordâncias estão adequadas à norma-padrão.

A) Seguem anexas as planilhas e inclusos os pareceres; os servidores disseram estar quites.
B) Segue anexas as planilhas e inclusos os pareceres; os servidores disseram estar quites.
C) Seguem anexo as planilhas e incluso os pareceres; os servidores disseram estar quites.
D) Segue anexa as planilhas e incluso os pareceres; os servidores disseram estar quite.

## Entrega prática do Bloco 6 — Dia 3

**Referência:** [Dia 3 — Bloco 6 — Recuperação ativa e caderno de erros](semana_01_estudo.md#s1-d3-b6)

Sem consultar, produza seis registros: dois sobre Banco de Dados, dois sobre Legislação e dois sobre Língua Portuguesa. Em cada registro, informe `confusão | regra recuperada | contraexemplo | seção de origem | próxima ação`. Termine indicando os dois pontos que voltarão no início do Dia 4. Se a regra não puder ser recuperada, marque `não retido`; não acrescente teoria nova.

## Gabarito do Dia 3

1. C
2. A
3. D
4. A
5. A
6. C
7. B
8. C
9. A
10. A
11. D
12. B
13. D
14. B
15. C
16. B
17. B
18. D
19. C
20. D
21. B
22. A
23. D
24. C
25. D
26. C
27. A
28. B
29. C
30. D
31. A
32. B
33. D
34. C
35. A
36. B
37. B
38. C
39. A
40. D
41. D
42. B
43. A
44. A
45. C
46. C
47. D
48. B
49. B
50. A

### Gabarito das questões extras de revisão fixa do Dia 3

Extra Dia 3.1: C
Extra Dia 3.2: A
Extra Dia 3.3: B
Extra Dia 3.4: C
Extra Dia 3.5: D
Extra Dia 3.6: B
Extra Dia 3.7: A
Extra Dia 3.8: D
Extra Dia 3.9: B
Extra Dia 3.10: B
Extra Dia 3.11: A
Extra Dia 3.12: A
Extra Dia 3.13: D
Extra Dia 3.14: C
Extra Dia 3.15: D
Extra Dia 3.16: C
Extra Dia 3.17: B
Extra Dia 3.18: C
Extra Dia 3.19: D
Extra Dia 3.20: A


## Comentários do Dia 3

### Comentário da Questão 1

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** A consulta filtra a UF, mas apenas ordena pela expressão de situação; ela não exclui os inativos.
- **B) está errada:** O OR inclui também profissionais ativos de outros estados e profissionais inativos do Paraná.
- **C) está correta:** Os dois predicados ligados por AND mantêm somente profissionais que satisfazem simultaneamente UF e situação.
- **D) está errada:** O operador de diferença seleciona ativos que não pertencem ao Paraná.
- **Conceito cobrado:** SELECT com WHERE.
- **Pegadinha usada:** Trocar a conjunção lógica ou confundir ordenação com filtragem.
- **Como pensar para acertar:** Traduza “ativos do Paraná” em duas condições simultâneas unidas por AND.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 2

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** GROUP BY forma um grupo por ano e COUNT conta as linhas de cada grupo.
- **B) está errada:** O agrupamento está no profissional, não no ano solicitado, e a projeção de ano não acompanha esse agrupamento.
- **C) está errada:** SUM calcula o valor monetário acumulado por ano, e não a quantidade de anuidades.
- **D) está errada:** A agregação produz apenas o total geral, sem separar os registros por ano.
- **Conceito cobrado:** GROUP BY e COUNT.
- **Pegadinha usada:** Confundir contagem, soma e total geral.
- **Como pensar para acertar:** Identifique primeiro a medida pedida — quantidade — e depois a dimensão — ano.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 3

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** A consulta elimina setores nulos, mas não restringe os grupos pela quantidade de profissionais.
- **B) está errada:** Ela retorna os vinte maiores grupos, que não são necessariamente os grupos com mais de vinte integrantes.
- **C) está errada:** O operador >= inclui setores com exatamente vinte profissionais, contrariando “mais de 20”.
- **D) está correta:** HAVING aplica a condição estrita depois da contagem de cada setor.
- **Conceito cobrado:** GROUP BY e HAVING.
- **Pegadinha usada:** Confundir limite de linhas, ordenação e o operador estrito da condição agregada.
- **Como pensar para acertar:** Agrupe por setor e aplique no HAVING exatamente COUNT(*) > 20.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 4

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A coluna na tabela filha referencia a chave da tabela `profissional`.
- **B) está errada:** A PK identifica cada anuidade; a coluna descrita identifica o profissional referenciado.
- **C) está errada:** Em 1:N, várias anuidades podem apontar para o mesmo profissional, portanto a coluna não precisa ser única.
- **D) está errada:** Embora possa existir índice de apoio, o papel informado pelo enunciado é o de restrição referencial.
- **Conceito cobrado:** Chave estrangeira.
- **Pegadinha usada:** Confundir a identificação da linha filha com a referência à linha pai.
- **Como pensar para acertar:** Quando uma coluna aponta para chave de outra tabela, classifique-a como FK.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 5

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A PK materializa a integridade de entidade: identificação única e não nula.
- **B) está errada:** PRIMARY KEY não é apenas UNIQUE; ela também impede NULL.
- **C) está errada:** Uma PK pode conter mais de uma coluna quando a identificação do domínio é composta.
- **D) está errada:** A unicidade decorre da própria restrição de PK, independentemente de existir uma FK apontando para ela.
- **Conceito cobrado:** Chave primária.
- **Pegadinha usada:** Tratar PRIMARY KEY como simples UNIQUE ou proibir chave composta.
- **Como pensar para acertar:** Separe quatro ideias: candidata, escolhida como PK, única e não nula.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 6

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** A lista reúne valores não atômicos e não oferece integridade referencial individual para cada perfil.
- **B) está errada:** Uma única FK em `perfil` modelaria outro vínculo e impediria o compartilhamento N:N pretendido.
- **C) está correta:** A associativa representa cada par usuário–perfil e pode impor FKs e unicidade sobre o par.
- **D) está errada:** Uma única FK em `usuario` permitiria no máximo um perfil por usuário.
- **Conceito cobrado:** Mapeamento N:N.
- **Pegadinha usada:** Reduzir N:N a uma FK simples ou a uma lista em coluna.
- **Como pensar para acertar:** Se ambos os lados admitem muitos, transforme cada vínculo em uma linha associativa.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 7

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Chave composta é compatível com 1FN; atomicidade diz respeito aos valores dos atributos.
- **B) está correta:** `nome_aluno` depende só de `id_aluno` e `nome_disciplina` só de `id_disciplina`.
- **C) está errada:** O defeito mostrado é dependência parcial direta, anterior à análise de dependência transitiva.
- **D) está errada:** A unicidade da chave não impede dependências parciais de atributos não chave.
- **Conceito cobrado:** Segunda Forma Normal.
- **Pegadinha usada:** Achar que uma chave composta basta para garantir 2FN.
- **Como pensar para acertar:** Para cada atributo não chave, teste se ele depende da chave composta inteira.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 8

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** O enunciado apresenta uma chave simples, portanto não há parte de chave composta a examinar.
- **B) está errada:** Repetição pode indicar redundância, mas 1FN trata da atomicidade de cada valor.
- **C) está correta:** A cadeia entre chave e atributos não chave caracteriza dependência transitiva.
- **D) está errada:** Separar `Departamento` e referenciá-lo por FK é justamente uma solução normalizada.
- **Conceito cobrado:** Terceira Forma Normal.
- **Pegadinha usada:** Confundir repetição visual, dependência parcial e dependência transitiva.
- **Como pensar para acertar:** Expresse as dependências: id_servidor → id_departamento → nome_departamento.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 9

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A alternativa separa corretamente manipulação de linhas e remoção de objeto.
- **B) está errada:** DELETE não elimina a definição; DROP é que remove o objeto do catálogo.
- **C) está errada:** DROP não se limita aos dados e a comparação transacional depende do SGBD, não define os comandos.
- **D) está errada:** A descrição de esvaziar preservando estrutura se aproxima de TRUNCATE; DELETE também pode ser usado sem WHERE.
- **Conceito cobrado:** DELETE x DROP.
- **Pegadinha usada:** Misturar DELETE, TRUNCATE e DROP.
- **Como pensar para acertar:** Pergunte se o alvo são linhas ou o próprio objeto do esquema.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 10

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** Sem predicado, todas as linhas da tabela participam da atualização.
- **B) está errada:** A ordem física ou a PK não limitam um UPDATE sem WHERE.
- **C) está errada:** WHERE é opcional; sua ausência amplia o conjunto-alvo em vez de tornar o comando inválido.
- **D) está errada:** O novo valor não cria um filtro implícito sobre o estado anterior.
- **Conceito cobrado:** UPDATE sem WHERE.
- **Pegadinha usada:** Inventar filtro implícito ou supor que o SGBD protege automaticamente contra UPDATE global.
- **Como pensar para acertar:** Determine o conjunto de linhas depois do WHERE; sem WHERE, o conjunto é a tabela inteira.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 11

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** String vazia é um valor e não equivale necessariamente à ausência representada por NULL.
- **B) está errada:** Comparações comuns com NULL resultam em desconhecido; não localizam os nulos.
- **C) está errada:** A expressão também seleciona e-mails cadastrados como string vazia, ampliando o resultado pedido.
- **D) está correta:** IS NULL é o predicado próprio para testar ausência de valor.
- **Conceito cobrado:** NULL e IS NULL.
- **Pegadinha usada:** Confundir NULL, string vazia e comparação comum.
- **Como pensar para acertar:** Para ausência estrita, use IS NULL sem converter o valor.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 12

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Ela compara as PKs independentes das duas tabelas, não a FK da anuidade com o profissional.
- **B) está correta:** A condição liga a FK `a.id_profissional` à PK `p.id` e retorna os pares correspondentes.
- **C) está errada:** A condição compara duas colunas da própria tabela `anuidade` e não relaciona `profissional`.
- **D) está errada:** CROSS JOIN produz todas as combinações, não apenas pares relacionados.
- **Conceito cobrado:** JOIN e condição de junção.
- **Pegadinha usada:** Usar colunas de mesmo nome ou PKs independentes no lugar do par PK–FK.
- **Como pensar para acertar:** Localize a FK na tabela filha e iguale-a à PK da tabela pai.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 13

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Produto cartesiano cria pares sem relação e não representa ausência de anuidade.
- **B) está errada:** INNER JOIN elimina profissionais sem correspondência.
- **C) está errada:** Partindo de `profissional`, preservar o lado direito não garante todos os profissionais.
- **D) está correta:** LEFT JOIN preserva cada profissional e preenche com NULL quando não há anuidade correspondente.
- **Conceito cobrado:** LEFT JOIN.
- **Pegadinha usada:** Escolher uma junção externa pelo nome sem observar qual lado precisa ser preservado.
- **Como pensar para acertar:** Coloque o conjunto obrigatório à esquerda e use LEFT JOIN com a condição PK–FK.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 14

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** COUNT(*) conta linhas sem examinar a nulidade de uma coluna específica.
- **B) está correta:** A distinção entre contagem de linhas e de valores não nulos está correta.
- **C) está errada:** Os resultados diferem quando há linhas cujo e-mail é NULL.
- **D) está errada:** COUNT(coluna) conta valores não nulos; ele não converte cada NULL em zero contado.
- **Conceito cobrado:** Funções agregadas e NULL.
- **Pegadinha usada:** Tratar COUNT(*) e COUNT(coluna) como sinônimos diante de NULL.
- **Como pensar para acertar:** Pergunte se a unidade contada é a linha ou um valor presente na coluna.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 15

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** As duas restrições podem formar uma chave alternativa, mas não substituem automaticamente a PK escolhida.
- **B) está errada:** A integridade de entidade torna a PK não nula sem declaração adicional.
- **C) está correta:** A alternativa separa identificação, unicidade e obrigatoriedade, com a ressalva de portabilidade para NULL em UNIQUE.
- **D) está errada:** Os efeitos foram invertidos: NOT NULL trata ausência e UNIQUE trata duplicidade.
- **Conceito cobrado:** Restrições de integridade.
- **Pegadinha usada:** Confundir chave primária, chave alternativa e obrigatoriedade.
- **Como pensar para acertar:** Associe cada restrição ao seu efeito e não suponha que UNIQUE implica NOT NULL.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 16

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** NOT NULL impede ausência, mas ainda aceita números negativos.
- **B) está correta:** CHECK expressa diretamente o domínio permitido para o valor.
- **C) está errada:** UNIQUE evita repetição, não limita o sinal do número.
- **D) está errada:** DEFAULT fornece valor quando ele é omitido, mas não rejeita um negativo informado.
- **Conceito cobrado:** CHECK constraint.
- **Pegadinha usada:** Confundir valor padrão, obrigatoriedade, unicidade e regra de domínio.
- **Como pensar para acertar:** Quando o requisito é uma condição booleana sobre o valor, traduza-o em CHECK.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 17

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** A sequência erra ao negar a função de GRANT e ao afirmar que COMMIT desfaz.
- **B) está correta:** CREATE TABLE é DDL, GRANT é DCL e COMMIT confirma, portanto a sequência é V, V, F.
- **C) está errada:** CREATE TABLE realmente define estrutura, logo a primeira proposição não é falsa.
- **D) está errada:** A terceira proposição é falsa porque ROLLBACK, antes da confirmação, é o comando de desfazer.
- **Conceito cobrado:** DDL, DCL e TCL.
- **Pegadinha usada:** Trocar DDL/DCL e inverter COMMIT com ROLLBACK.
- **Como pensar para acertar:** Classifique cada comando pelo efeito concreto antes de montar a sequência.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 18

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Consistência trata a passagem entre estados válidos; o requisito explícito de indivisibilidade é atomicidade.
- **B) está errada:** Isolamento controla interferência entre transações concorrentes, não a indivisibilidade interna descrita.
- **C) está errada:** Durabilidade protege efeitos já confirmados, enquanto o caso exige desfazer uma execução parcial.
- **D) está correta:** A unidade lógica deve confirmar ambas as operações ou não conservar nenhuma.
- **Conceito cobrado:** ACID: atomicidade.
- **Pegadinha usada:** Confundir as quatro propriedades ACID diante de uma falha parcial.
- **Como pensar para acertar:** Associe “todas as etapas ou nenhuma” diretamente à atomicidade.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 19

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Índice comum não impõe unicidade; isso requer índice ou restrição UNIQUE.
- **B) está errada:** O ganho depende do plano e do predicado, e inserções/atualizações precisam manter o índice.
- **C) está correta:** A alternativa apresenta o benefício de leitura e o custo de manutenção sem prometer ganho universal.
- **D) está errada:** O otimizador pode escolher varredura e o índice não ajuda automaticamente filtros em outras colunas.
- **Conceito cobrado:** Índices.
- **Pegadinha usada:** Tratar índice como garantia de unicidade ou aceleração universal e gratuita.
- **Como pensar para acertar:** Relacione a coluna e o padrão de acesso, depois considere custo de espaço e escrita.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 20

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** View comum é lógica; materialização é uma modalidade específica, não obrigatória.
- **B) está errada:** Views podem apoiar segurança, mas continuam sujeitas à política de privilégios.
- **C) está errada:** A atualizabilidade depende da definição da view e das regras do SGBD.
- **D) está correta:** Ela encapsula uma consulta e apresenta seu resultado como relação lógica.
- **Conceito cobrado:** Views.
- **Pegadinha usada:** Generalizar materialização, atualizabilidade ou permissões de views.
- **Como pensar para acertar:** Pense primeiro em consulta armazenada lógica; trate os demais comportamentos como condicionais.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 21

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Uma trigger AFTER reage ao comando, não espera necessariamente o COMMIT, e não ganha persistência independente.
- **B) está correta:** Sem transação autônoma específica, o efeito automático da trigger integra a mesma unidade transacional do INSERT.
- **C) está errada:** Triggers são disparadas pelo evento configurado, não por chamada explícita da aplicação.
- **D) está errada:** Os efeitos da trigger participam da transação e podem ser desfeitos com ela.
- **Conceito cobrado:** Triggers.
- **Pegadinha usada:** Confundir execução automática com persistência autônoma.
- **Como pensar para acertar:** Descubra primeiro em qual transação o efeito foi produzido; depois aplique COMMIT ou ROLLBACK à unidade inteira.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 22

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Procedure é adequada para receber parâmetros e coordenar validação, inserção e atualização.
- **B) está errada:** Trigger é ligada a evento no banco; o requisito descreve chamada explícita com parâmetros.
- **C) está errada:** CHECK valida uma expressão sobre dados e não encapsula uma sequência geral de comandos.
- **D) está errada:** View representa consulta e não é, por definição, uma rotina parametrizada de DML encadeado.
- **Conceito cobrado:** Stored procedures.
- **Pegadinha usada:** Confundir rotina chamada, consulta lógica, evento automático e restrição declarativa.
- **Como pensar para acertar:** Separe quem chama o objeto e se ele apenas mostra dados ou executa uma sequência de ações.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 23

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** A expressão não contém agrupamento nem preserva todas as colunas.
- **B) está errada:** A seleção interna filtra as tuplas e não há operação de ordenação.
- **C) está errada:** Não existe função de contagem nem agrupamento na expressão.
- **D) está correta:** Sigma seleciona as linhas pela condição e pi projeta somente o atributo `nome`.
- **Conceito cobrado:** Álgebra relacional.
- **Pegadinha usada:** Inverter seleção e projeção ou acrescentar ordenação/agregação inexistentes.
- **Como pensar para acertar:** Leia de dentro para fora: primeiro σ filtra tuplas; depois π escolhe atributos.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 24

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Uma lista em atributo perde atomicidade e dificulta representar os dados próprios de cada ocorrência.
- **B) está errada:** Domínio restringe valores de atributo; não representa ocorrências com número, data e responsável.
- **C) está correta:** Cada fiscalização possui identidade e atributos, e várias podem apontar para um processo.
- **D) está errada:** Os dados são persistentes e próprios, portanto não constituem mero atributo derivado.
- **Conceito cobrado:** Modelo Entidade-Relacionamento.
- **Pegadinha usada:** Reduzir uma entidade dependente com atributos próprios a um campo ou domínio.
- **Como pensar para acertar:** Se o conceito tem várias ocorrências e atributos próprios, modele-o como entidade e defina a cardinalidade.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 25

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** A repetição duplica os dados da pessoa e cria anomalias de atualização.
- **B) está errada:** Colunas numeradas criam grupo repetido, limite artificial e muitos nulos.
- **C) está errada:** A string reúne vários valores sem integridade individual nem consulta relacional adequada.
- **D) está correta:** Cada telefone passa a ocupar linha própria, com atributos atômicos e vínculo referencial à pessoa.
- **Conceito cobrado:** Atributos multivalorados e 1FN.
- **Pegadinha usada:** Escolher colunas repetidas, lista delimitada ou duplicação da entidade principal.
- **Como pensar para acertar:** Transforme cada ocorrência multivalorada em uma linha relacionada por FK.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 26

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** A estrutura lógica usada pela aplicação foi mantida; não houve substituição do modelo conceitual.
- **B) está errada:** Integridade referencial pode continuar válida, mas não nomeia a separação entre níveis descrita.
- **C) está correta:** Alterações de armazenamento e índices sem mudança das consultas exemplificam independência física.
- **D) está errada:** Durabilidade trata persistência após confirmação, não desacoplamento físico–lógico.
- **Conceito cobrado:** Independência física de dados.
- **Pegadinha usada:** Confundir nível físico, integridade e propriedade transacional.
- **Como pensar para acertar:** Pergunte qual nível mudou e qual nível permaneceu estável.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 27

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Tipos, defaults, constraints e índices são dados sobre objetos do banco.
- **B) está errada:** O log registra operações para recuperação; não é o catálogo estrutural completo.
- **C) está errada:** Os valores de negócio não descrevem a estrutura de colunas, padrões e restrições.
- **D) está errada:** O catálogo não precisa duplicar fisicamente o conteúdo das tabelas de negócio.
- **Conceito cobrado:** Dicionário de dados e metadados.
- **Pegadinha usada:** Confundir metadados, dados de negócio, log e cópia física.
- **Como pensar para acertar:** Se a informação descreve objetos e regras do banco, ela pertence ao dicionário de dados.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 28

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Ser PK da relação não faz `id_lancamento` ser determinado pelo setor agrupado; há vários IDs por setor.
- **B) está correta:** A projeção mistura granularidade de setor com um ID individual sem regra que escolha um ID do grupo.
- **C) está errada:** Agregações podem ser usadas sem HAVING; HAVING apenas filtra grupos quando necessário.
- **D) está errada:** A ordem visual das expressões projetadas não corrige a incompatibilidade de granularidade.
- **Conceito cobrado:** GROUP BY e colunas não agregadas.
- **Pegadinha usada:** Supor que qualquer PK pode ser projetada em um agrupamento ou exigir HAVING para toda agregação.
- **Como pensar para acertar:** Cada expressão não agregada deve ser compatível com a granularidade do grupo; aqui setor não determina um único lançamento.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 29

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Excluir o objeto seria efeito de DROP TABLE, não de DELETE filtrado.
- **B) está errada:** FKs podem restringir a exclusão ou definir ações diferentes; cascata não é automática em todos os casos.
- **C) está correta:** DELETE atua nas linhas filtradas, preserva o objeto e integra a transação ainda não confirmada.
- **D) está errada:** Antes da confirmação, ROLLBACK pode desfazer o DML dentro do modelo transacional descrito.
- **Conceito cobrado:** DELETE com WHERE.
- **Pegadinha usada:** Confundir linhas, objeto, cascata referencial e confirmação transacional.
- **Como pensar para acertar:** Separe três perguntas: o que DELETE atinge, o que as FKs permitem e se já houve COMMIT.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 30

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** NULL explícito não aciona o DEFAULT e viola o NOT NULL de `uf`.
- **B) está errada:** Sem lista de colunas, os valores não correspondem corretamente ao esquema que também contém `id` e `uf`.
- **C) está errada:** UPDATE não insere linhas e a expressão SET apresentada não é atribuição válida.
- **D) está correta:** Ao omitir `id` gerado e `uf`, cada linha recebe a identidade e o padrão definidos pelo esquema.
- **Conceito cobrado:** INSERT.
- **Pegadinha usada:** Confundir omissão de coluna com NULL explícito e ignorar coluna de identidade.
- **Como pensar para acertar:** Liste apenas as colunas fornecidas; deixe identidade e DEFAULT serem preenchidos pelo SGBD.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 31

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A alternativa associa corretamente o nível às anomalias evitadas e preserva a ressalva de implementação.
- **B) está errada:** READ COMMITTED impede ler dado não confirmado, mas outra transação pode confirmar mudança entre as leituras.
- **C) está errada:** READ UNCOMMITTED é justamente o nível associado à possibilidade de leitura suja.
- **D) está errada:** Serializable é um nível forte, mas ainda depende de transações, confirmação e controle de concorrência.
- **Conceito cobrado:** Isolamento transacional.
- **Pegadinha usada:** Transformar um nível em garantia maior do que ele oferece ou dispensar o mecanismo transacional.
- **Como pensar para acertar:** Compare cada nível com as anomalias que ele impede, sem extrapolar a garantia.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 32

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Uma chave alternativa UNIQUE não substitui automaticamente a PK declarada.
- **B) está correta:** A alternativa preserva os papéis distintos e evita absolutizar o tratamento de NULL entre implementações.
- **C) está errada:** Obrigatoriedade é efeito de NOT NULL, não consequência universal de UNIQUE.
- **D) está errada:** A PK permanece única independentemente dos valores de outra coluna.
- **Conceito cobrado:** UNIQUE x PRIMARY KEY.
- **Pegadinha usada:** Confundir chave alternativa com chave primária e UNIQUE com NOT NULL.
- **Como pensar para acertar:** Leia cada restrição separadamente e preserve a ressalva de portabilidade para NULL.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 33

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** O predicado no WHERE rejeita o NULL do lado direito e elimina justamente os profissionais sem cidade.
- **B) está errada:** INNER JOIN elimina os profissionais que não têm cidade correspondente.
- **C) está errada:** A condição usa a PK do profissional em lugar da FK da cidade.
- **D) está correta:** LEFT JOIN preserva todos os profissionais e relaciona a FK `id_cidade` à PK de `cidade`.
- **Conceito cobrado:** Condição de JOIN por PK/FK.
- **Pegadinha usada:** Acertar o tipo de JOIN, mas errar a chave ou neutralizar o efeito externo no WHERE.
- **Como pensar para acertar:** Preserve a tabela obrigatória à esquerda, ligue FK à PK e não rejeite depois os NULLs da direita.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 34

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** Dependência parcial pressupõe chave composta; a afirmação está correta.
- **B) está errada:** A cadeia descreve dependência transitiva entre atributos não chave e está correta.
- **C) está correta:** Decompor sem examinar junção sem perda e dependências pode eliminar associações ou permitir estados indevidos.
- **D) está errada:** Organização e desempenho não são sinônimos; a normalização pode exigir mais joins.
- **Conceito cobrado:** Normalização.
- **Pegadinha usada:** Tratar normalização como simples divisão física de colunas, sem analisar dependências.
- **Como pensar para acertar:** Valide cada forma normal pelas dependências e não aceite uma decomposição só porque criou mais tabelas.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 35

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A consulta ordena pelos maiores valores, resolve empates pelo menor ID e limita a três linhas.
- **B) está errada:** A ordenação crescente escolhe os menores valores.
- **C) está errada:** OFFSET 3 descarta as três primeiras linhas em vez de retorná-las.
- **D) está errada:** Sem ORDER BY, não há garantia de que as três linhas sejam as de maior valor.
- **Conceito cobrado:** ORDER BY e limitação de resultados.
- **Pegadinha usada:** Limitar antes de definir uma ordem determinística ou inverter ASC/DESC.
- **Como pensar para acertar:** Primeiro estabeleça a ordenação completa; depois aplique o limite de linhas.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 36

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Há diferenças importantes e dependentes do SGBD; a equivalência universal é falsa.
- **B) está correta:** A descrição mantém o núcleo comum e explicita os pontos de portabilidade.
- **C) está errada:** TRUNCATE não é remoção linha a linha com predicado.
- **D) está errada:** DROP remove o objeto, não apenas seu conteúdo.
- **Conceito cobrado:** DELETE x TRUNCATE.
- **Pegadinha usada:** Absolutizar detalhes dependentes do SGBD ou trocar remoção de dados por remoção de objeto.
- **Como pensar para acertar:** Memorize o núcleo de cada comando e trate transação, log, identidade e FKs como detalhes de implementação.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 37

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** O WHERE rejeita o NULL da linha estendida e elimina setores sem profissional ativo.
- **B) está correta:** O filtro no ON limita correspondências ativas, LEFT preserva setores vazios e COUNT da chave direita produz zero sem par.
- **C) está errada:** COUNT(*) conta também a linha preservada sem correspondência, produzindo um em vez de zero.
- **D) está errada:** INNER JOIN só conserva setores com ao menos uma correspondência ativa.
- **Conceito cobrado:** LEFT JOIN e NULL.
- **Pegadinha usada:** Neutralizar o LEFT JOIN no WHERE ou contar a linha estendida com COUNT(*).
- **Como pensar para acertar:** Filtre o lado opcional no ON e conte uma coluna não nula apenas quando houver correspondência.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 38

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Uma FK única limita o profissional a uma pessoa jurídica e não representa o histórico N:N.
- **B) está errada:** A coluna guarda apenas o responsável atual e não permite vários vínculos nem períodos completos.
- **C) está correta:** A associativa representa cada vínculo e seus atributos próprios ao longo do tempo.
- **D) está errada:** Texto livre perde atomicidade, referências e validação temporal.
- **Conceito cobrado:** Modelagem de relacionamento com atributos.
- **Pegadinha usada:** Modelar apenas o estado atual ou esconder histórico N:N em texto.
- **Como pensar para acertar:** Quando o relacionamento possui atributos e multiplicidade nos dois lados, transforme-o em tabela associativa.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 39

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Consistência da captura e teste de restauração tratam tanto geração quanto recuperabilidade do backup.
- **B) está errada:** Exportações independentes podem observar instantes diferentes e quebrar relações entre tabelas.
- **C) está errada:** Arquivos copiados durante escrita podem não representar estado recuperável e coerente.
- **D) está errada:** Índices são estruturas de acesso e não cópias recuperáveis dos dados.
- **Conceito cobrado:** Backup e recuperação em SGBD.
- **Pegadinha usada:** Confundir cópia de arquivos ou exportações isoladas com backup consistente e testado.
- **Como pensar para acertar:** Verifique o ponto consistente da captura e nunca considere o backup confiável sem restauração de teste.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 40

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** LIKE não cria atomicidade nem integridade individual e pode produzir correspondências imprecisas.
- **B) está errada:** Duplicar o documento introduz redundância e anomalias de atualização.
- **C) está errada:** Colunas numeradas criam limite artificial, grupos repetidos e muitos nulos.
- **D) está correta:** A tabela separa as ocorrências e permite chave, FK e restrição por tag.
- **Conceito cobrado:** 1FN e atributos multivalorados.
- **Pegadinha usada:** Preservar lista delimitada ou trocar uma lista por colunas repetidas.
- **Como pensar para acertar:** Uma ocorrência por linha permite atomicidade, chaves e consultas relacionais exatas.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 41

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** Uma FK exige chave referenciada adequada e não substitui UNIQUE, NOT NULL e CHECK requeridos.
- **B) está errada:** Criar outra PRIMARY KEY conflita com a PK técnica já existente e não restringe a situação.
- **C) está errada:** O CHECK de não nulidade não impede duplicação e a situação continua sem domínio definido.
- **D) está correta:** Mantém `id` como PK e expressa separadamente obrigatoriedade, unicidade e domínio de situação.
- **Conceito cobrado:** NOT NULL e UNIQUE.
- **Pegadinha usada:** Tentar substituir a PK técnica ou usar uma única restrição para três requisitos diferentes.
- **Como pensar para acertar:** Traduza cada regra do domínio em sua constraint própria, sem alterar a chave já escolhida.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 42

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** Independência física evita a reescrita das visões por mera reorganização interna, e rollback não assegura sozinho a persistência de commits.
- **B) está correta:** Os mapeamentos do SGBD desacoplam o nível físico dos demais, enquanto concorrência, log e recuperação preservam as propriedades transacionais.
- **C) está errada:** As visões compartilham o esquema lógico, e backup periódico não substitui isolamento nem recuperação transacional.
- **D) está errada:** SQL expressa operações, mas os mecanismos de mapeamento, escalonamento e recuperação são implementados pelo SGBD.
- **Conceito cobrado:** Arquitetura de três esquemas, independência física e serviços transacionais do SGBD.
- **Pegadinha usada:** Atribuir à linguagem ou ao backup funções operacionais do SGBD e confundir mudança física com mudança lógica.
- **Como pensar para acertar:** Separe os níveis de abstração e identifique qual componente preserva tanto os mapeamentos quanto as garantias de transação.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 43

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** A view aplica projeção e seleção no banco, e a ausência de privilégio na tabela-base impede contornar essas restrições.
- **B) está errada:** O acesso à tabela-base expõe CPF e linhas inativas se o filtro da aplicação falhar ou for omitido.
- **C) está errada:** Restringir colunas não restringe linhas; profissionais inativos continuariam acessíveis.
- **D) está errada:** O privilégio mantido na tabela-base oferece um caminho de leitura que ignora a proteção da view.
- **Conceito cobrado:** Menor privilégio, views de segurança, projeção e seleção.
- **Pegadinha usada:** Confundir restrição de coluna com restrição de linha ou confiar em filtro aplicado apenas pelo cliente.
- **Como pensar para acertar:** Liste dados, linhas e operações permitidos e elimine qualquer privilégio que permita ultrapassar um desses limites.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 44

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** A trigger centraliza a reação automática, mas exige avaliação dos efeitos transacionais e operacionais.
- **B) está errada:** A solução fica dispersa e uma aplicação pode omitir ou implementar a auditoria de forma diferente.
- **C) está errada:** View comum representa consulta e não funciona automaticamente como interceptador de UPDATE.
- **D) está errada:** Índice acelera acesso; não é histórico de auditoria das versões modificadas.
- **Conceito cobrado:** Triggers de auditoria.
- **Pegadinha usada:** Confundir automação por evento com view, índice ou código voluntário de cada cliente.
- **Como pensar para acertar:** Escolha o objeto acionado pelo próprio evento e avalie seu vínculo com a transação principal.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 45

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** A FK anulável permite anuidade sem profissional, e o índice por exercício não impede duplicidade por profissional e ano.
- **B) está errada:** A FK no lado de `Profissional` limita o vínculo e induz repetição da entidade a cada exercício.
- **C) está correta:** A FK `NOT NULL` garante um profissional por anuidade, a ausência de linha preserva a participação opcional e a restrição composta evita duplicidade anual.
- **D) está errada:** O domínio descreve um-para-muitos, não muitos-para-muitos, e não admite anuidades sem profissional.
- **Conceito cobrado:** Mapeamento 1:N, participação obrigatória e chave candidata composta.
- **Pegadinha usada:** Modelar apenas a cardinalidade máxima e esquecer participação mínima ou unicidade dependente do exercício.
- **Como pensar para acertar:** Traduza separadamente as três regras: lado da FK, nulabilidade da FK e combinação de atributos que deve ser única.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 46

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** A decomposição não deve perder a informação de departamento do servidor.
- **B) está errada:** UNIQUE não elimina a dependência transitiva e ainda impediria vários servidores no mesmo departamento.
- **C) está correta:** A decomposição representa cada fato em sua relação e preserva o vínculo por FK.
- **D) está errada:** A tabela de departamento deve ser identificada pelo departamento, não pelo servidor.
- **Conceito cobrado:** Dependência funcional e 3FN.
- **Pegadinha usada:** Declarar UNIQUE para mascarar dependência ou decompor com a chave errada.
- **Como pensar para acertar:** Coloque cada atributo junto de seu determinante e mantenha a associação por chave estrangeira.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 47

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** DISTINCT considera o conjunto completo de colunas projetadas, não somente a primeira.
- **B) está errada:** A eliminação de duplicatas também se aplica a projeções com várias colunas.
- **C) está errada:** Para eliminação de duplicatas, as duas ocorrências do mesmo par com NULL não geram linhas separadas.
- **D) está correta:** Os pares repetidos são reduzidos a uma ocorrência, inclusive o par com NULL no resultado DISTINCT.
- **Conceito cobrado:** DISTINCT.
- **Pegadinha usada:** Aplicar DISTINCT a uma coluna isolada ou tratar cada NULL como linha distinta no resultado.
- **Como pensar para acertar:** Forme os pares projetados e elimine repetições do par completo.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 48

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** Registrar uma alteração não confirmada não autoriza torná-la permanente; T2 deve ser desfeita.
- **B) está correta:** A recuperação conserva T1 pela durabilidade e elimina os efeitos parciais de T2 pela atomicidade.
- **C) está errada:** A ordem temporal não substitui o estado de confirmação; uma transação sem commit não prevalece sobre outra confirmada.
- **D) está errada:** Isolamento controla interferência concorrente, mas não exige apagar uma transação cujo commit já foi reconhecido.
- **Conceito cobrado:** Recuperação com log, atomicidade e durabilidade.
- **Pegadinha usada:** Confundir alteração mais recente com alteração confirmada ou tratar toda falha como motivo para desfazer todos os commits.
- **Como pensar para acertar:** Classifique cada transação no instante da falha: committed deve sobreviver; uncommitted deve ser desfeita.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 49

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** A afirmação está correta: o filtro posterior pode neutralizar a preservação da linha esquerda.
- **B) está correta:** A posição do predicado pode alterar quais linhas são correspondidas ou eliminadas; por isso a afirmação é incorreta.
- **C) está errada:** A diferença entre contagem da chave direita e de linhas é correta quando não há correspondência.
- **D) está errada:** A afirmação está correta: falhar no ON produz ausência de par, mas a linha esquerda permanece.
- **Conceito cobrado:** JOINs.
- **Pegadinha usada:** Tratar ON e WHERE como intercambiáveis em LEFT JOIN.
- **Como pensar para acertar:** Simule uma linha sem correspondência e acompanhe o NULL pelo ON, WHERE e COUNT.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 50

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** A alternativa segue corretamente a ordem lógica FROM/WHERE/GROUP BY/HAVING/SELECT/ORDER BY.
- **B) está errada:** A condição de dez está no HAVING sobre COUNT, não sobre identificador individual.
- **C) está errada:** ORDER BY atua no resultado agregado e nenhum comando modifica a tabela física.
- **D) está errada:** WHERE é aplicado antes do agrupamento, então as demais UFs nem entram nos grupos.
- **Conceito cobrado:** GROUP BY e ORDER BY com agregação.
- **Pegadinha usada:** Ler o SELECT na ordem escrita e aplicar HAVING a linhas individuais.
- **Como pensar para acertar:** Reordene mentalmente as cláusulas pela execução lógica e acompanhe o conjunto em cada etapa.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentários das questões extras de revisão fixa do Dia 3

#### Comentário Extra Dia 3.1

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** A distribuição entre instâncias não desaparece só porque a matéria é ética.
- **B) está errada:** Prova pré-constituída não elimina contraditório nem autoriza converter o recurso na primeira oportunidade de defesa.
- **C) está correta:** Poder disciplinar exige órgão competente e procedimento que permita participação do acusado.
- **D) está errada:** Denunciante provoca a apuração, mas não substitui o órgão julgador nem define a sanção.
- **Conceito cobrado:** Sanções ético-disciplinares.
- **Pegadinha usada:** Confundir poder disciplinar com punição imediata ou escolha privada da pena.
- **Como pensar para acertar:** Verifique competência, procedimento, contraditório e defesa antes de examinar a penalidade.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.2

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A alternativa preserva tanto o alcance quanto a necessidade de observar as especificidades do sujeito.
- **B) está errada:** As funções das duas resoluções foram invertidas.
- **C) está errada:** O material inclui pessoas jurídicas no campo da norma ética, com tratamento próprio.
- **D) está errada:** Incidência da norma não autoriza transposição mecânica de toda sanção de pessoa física.
- **Conceito cobrado:** Código de Ética e pessoa jurídica.
- **Pegadinha usada:** Confundir o número e o objeto das resoluções ou igualar integralmente PF e PJ.
- **Como pensar para acertar:** Identifique primeiro a norma e seu alcance; depois verifique se a consequência é específica do sujeito.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.3

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** A alternativa mantém uma transposição que a ressalva estudada não autoriza.
- **B) está correta:** Ela reproduz o ponto específico destacado na apostila para diferenciar sujeitos e sanções.
- **C) está errada:** A distinção proposta também atribui à pessoa jurídica sanção que o material ressalva.
- **D) está errada:** Dano econômico não cria, por si só, sanção ou destinatário não previstos.
- **Conceito cobrado:** Sanções e pessoa jurídica.
- **Pegadinha usada:** Confundir submissão da PJ à norma ética com identidade absoluta de sanções.
- **Como pensar para acertar:** Separe alcance subjetivo da norma e rol de consequências aplicáveis a cada sujeito.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Validade nacional do registro não transforma o Regional de origem em fiscal de todo o País.
- **B) está errada:** Coordenação federal não absorve a execução ordinária atribuída ao Regional competente.
- **C) está correta:** A alternativa combina jurisdição regional e integração ao sistema nacional.
- **D) está errada:** Os limites territoriais continuam relevantes para a competência regional.
- **Conceito cobrado:** Jurisdição regional.
- **Pegadinha usada:** Confundir validade nacional, jurisdição regional e coordenação federal.
- **Como pensar para acertar:** Localize o fato, identifique o Regional competente e só depois examine o papel nacional do CFA.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.5

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** O edital define o conteúdo do cargo; a área técnica do candidato não exclui a legislação comum cobrada.
- **B) está errada:** O Regimento disciplina a estrutura e o funcionamento interno, não sendo peça meramente simbólica.
- **C) está errada:** Norma interna opera dentro da hierarquia e não revoga a lei ou a normatização superior aplicável.
- **D) está correta:** Conteúdo expresso do edital e organização institucional tornam seu estudo pertinente ao concurso.
- **Conceito cobrado:** Importância do Regimento.
- **Pegadinha usada:** Desprezar conteúdo comum do edital ou superestimar a autonomia de norma interna.
- **Como pensar para acertar:** Parta do edital e da função institucional da norma, não apenas da especialidade técnica do cargo.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.6

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** O conselho regional pode atuar no âmbito de sua competência sem depender sempre de provocação externa.
- **B) está correta:** A alternativa relaciona corretamente fiscalização ao exercício regular da profissão.
- **C) está errada:** Cobrança não esgota o poder fiscalizatório sobre atividade, habilitação e registro.
- **D) está errada:** A execução regional não é substituída pela coordenação normativa federal.
- **Conceito cobrado:** Exercício sem registro.
- **Pegadinha usada:** Reduzir fiscalização a cobrança ou deslocar toda execução para o CFA.
- **Como pensar para acertar:** Pergunte qual atividade é exercida, se exige habilitação/registro e qual Regional possui jurisdição.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.7

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A alternativa reúne os cuidados centrais de veracidade, título e expectativa criada no público.
- **B) está errada:** Experiência não torna eticamente segura uma garantia absoluta de resultado futuro.
- **C) está errada:** Rótulo comercial não legitima título profissional reservado ou potencialmente enganoso.
- **D) está errada:** A comunicação profissional também integra a conduta submetida a parâmetros éticos.
- **Conceito cobrado:** Publicidade profissional.
- **Pegadinha usada:** Usar experiência, aviso comercial ou liberdade publicitária para afastar deveres éticos.
- **Como pensar para acertar:** Teste veracidade, habilitação do título e promessa de resultado em cada alternativa.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.8

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Contrato privado não elimina requisitos profissionais nem impede fiscalização.
- **B) está errada:** Formação acadêmica e registro profissional são requisitos distintos quando a lei exige ambos.
- **C) está errada:** A pessoa jurídica pode sujeitar-se a registro e fiscalização conforme a atividade explorada.
- **D) está correta:** A alternativa preserva a apuração individualizada do executor, da atividade e da organização.
- **Conceito cobrado:** Registro e exercício profissional.
- **Pegadinha usada:** Achar que contrato, diploma ou personalidade jurídica afastam automaticamente o controle profissional.
- **Como pensar para acertar:** Separe formação, registro do executor, atividade explorada e deveres da organização.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.9

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Correção posterior de dado não apaga automaticamente irregularidade material anterior.
- **B) está correta:** A alternativa reconhece a função probatória e fiscalizatória sem transformar cadastro em salvo-conduto.
- **C) está errada:** Validade do registro não elimina deveres de atualização e regras de jurisdição aplicáveis.
- **D) está errada:** Certidão comprova situação; não desloca autoria nem responsabilidade técnica.
- **Conceito cobrado:** Regularidade registral.
- **Pegadinha usada:** Transformar regularidade documental em cura automática ou transferência de responsabilidade.
- **Como pensar para acertar:** Diferencie prova cadastral, habilitação para exercer e responsabilidade pelos atos praticados.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.10

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A proteção corporativa dos registrados não substitui a finalidade pública da fiscalização profissional.
- **B) está correta:** O controle de habilitação, registro e atividade protege os destinatários dos serviços e a regularidade do exercício.
- **C) está errada:** A fiscalização não se reduz à dimensão financeira; ela examina o exercício profissional no campo fiscalizado.
- **D) está errada:** O Conselho exerce competência administrativa própria, mas não substitui a função jurisdicional em todo conflito contratual.
- **Conceito cobrado:** Finalidade institucional da fiscalização profissional.
- **Pegadinha usada:** Reduzir a fiscalização à cobrança ou convertê-la em defesa econômica da categoria.
- **Como pensar para acertar:** Relacione fiscalização a interesse público, regularidade do exercício e proteção da sociedade.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.11

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A sujeição ao Sistema depende da atividade profissional explorada e da competência regional aplicável, não apenas da forma empresarial.
- **B) está errada:** CNPJ identifica a pessoa jurídica, mas não substitui eventual regularidade profissional exigida para a atividade.
- **C) está errada:** Pessoas jurídicas também podem estar sujeitas a registro e fiscalização quando atuam no campo profissional abrangido.
- **D) está errada:** O CRA exerce registro e fiscalização em sua jurisdição; o CFA desempenha funções nacionais de coordenação e normatização.
- **Conceito cobrado:** Registro e fiscalização de pessoa jurídica.
- **Pegadinha usada:** Tratar o CNPJ como dispensa automática ou excluir pessoas jurídicas da fiscalização regional.
- **Como pensar para acertar:** Identifique a atividade oferecida, a jurisdição e a regularidade exigível antes de concluir.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.12

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Um fato pode envolver simultaneamente exercício irregular e violação de dever profissional.
- **B) está errada:** O alcance dos controles não se divide de modo absoluto por pessoa física e jurídica.
- **C) está errada:** Conduta e regularidade são dimensões distintas e complementares.
- **D) está errada:** Regularidade registral não impede que a conduta profissional seja eticamente questionada.
- **Conceito cobrado:** Fiscalização e ética.
- **Pegadinha usada:** Fundir os controles ou torná-los mutuamente exclusivos.
- **Como pensar para acertar:** Pergunte separadamente: o sujeito podia exercer a atividade e, ao exercê-la, agiu de modo ético?
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.13

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** A responsabilidade técnica de quem assina não é transferida por autorização verbal do cliente.
- **B) está errada:** A expectativa do contratante não substitui a independência e o fundamento técnico exigidos do profissional.
- **C) está errada:** Omitir dados relevantes produz informação enganosa e compromete a honestidade da análise.
- **D) está correta:** Recusar conclusão sem suporte preserva a independência e limita a validação ao que pode ser tecnicamente sustentado.
- **Conceito cobrado:** Independência técnica diante de pressão do cliente.
- **Pegadinha usada:** Tratar a vontade do contratante como substituta do juízo e da responsabilidade profissionais.
- **Como pensar para acertar:** Pergunte se quem assina consegue demonstrar tecnicamente a conclusão com os dados do caso.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.14

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Competência decorre das normas do sistema, não da preferência da parte.
- **B) está errada:** Defesa tardia não substitui automaticamente participação útil na formação da decisão.
- **C) está correta:** A alternativa reúne garantias mínimas de processo sancionador regular.
- **D) está errada:** Recurso não autoriza eliminar instrução e contraditório na instância inicial.
- **Conceito cobrado:** Processo ético-disciplinar.
- **Pegadinha usada:** Usar o recurso como justificativa para suprimir competência, instrução ou defesa inicial.
- **Como pensar para acertar:** Examine a sequência: competência, ciência, instrução contraditória, decisão e recurso.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.15

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Atuação interestadual não transfere automaticamente toda execução local ao órgão federal.
- **B) está errada:** Cooperação entre órgãos não elimina regras de jurisdição e de competência decisória.
- **C) está errada:** Registro de origem não cria competência territorial perpétua sobre qualquer fato futuro.
- **D) está correta:** A estratégia identifica natureza, território e instância antes de escolher a sigla.
- **Conceito cobrado:** Competência e jurisdição.
- **Pegadinha usada:** Responder pela sigla mais ampla ou pelo registro original sem classificar ato, lugar e instância.
- **Como pensar para acertar:** Monte uma tabela com ato, órgão executor, território e eventual instância revisora.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d3-b4).

#### Comentário Extra Dia 3.16

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Pergunta indireta pede `por que`, e o substantivo acompanhado de artigo pede `porquê`.
- **B) está errada:** No meio da pergunta usa-se `por que`; como substantivo, a forma é `porquê`.
- **C) está correta:** As três ocorrências correspondem, respectivamente, a pergunta indireta, causa e substantivo.
- **D) está errada:** A pergunta indireta exige `por que`, e a explicação causal exige `porque`.
- **Conceito cobrado:** Uso dos porquês.
- **Pegadinha usada:** Aplicar a mesma forma a pergunta indireta, explicação e substantivo.
- **Como pensar para acertar:** Substitua mentalmente por “por qual razão”, “pois” ou “o motivo” em cada ocorrência.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5).

#### Comentário Extra Dia 3.17

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** No sentido de desejar, `aspirar` pede `a`, e `obedecer` também rege `a`.
- **B) está correta:** `Recorrer da decisão` e `assistir ao julgamento`, no sentido de presenciar, seguem as regências cobradas.
- **C) está errada:** A norma-padrão prefere a estrutura `preferiu X a Y`, e `informar` exige construção adequada dos complementos.
- **D) está errada:** No sentido de presenciar, é `assistiu ao`; na norma tradicional, `chegou ao órgão`.
- **Conceito cobrado:** Regência verbal.
- **Pegadinha usada:** Avaliar apenas o primeiro verbo e deixar passar erro no segundo.
- **Como pensar para acertar:** Identifique o sentido de cada verbo e teste separadamente a preposição exigida.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5).

#### Comentário Extra Dia 3.18

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** `Por isso` transforma o aumento de custo em consequência da redução, e `contudo` troca a conclusão por oposição.
- **B) está errada:** A construção concessiva não recompõe a sequência original, e `porque` introduz causa, não conclusão.
- **C) está correta:** `Entretanto` preserva a oposição de `contudo`, e `logo` mantém a conclusão introduzida por `portanto`.
- **D) está errada:** A coordenação com `e` enfraquece o contraste, enquanto `se` cria condição inexistente no texto.
- **Conceito cobrado:** Coesão sequencial, equivalência de conectores e preservação de inferência.
- **Pegadinha usada:** Substituir conectores por palavras gramaticais possíveis, mas semanticamente incompatíveis com a relação entre as orações.
- **Como pensar para acertar:** Nomeie a relação em cada fronteira do texto e só então procure dois conectores que preservem ambas.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5).

#### Comentário Extra Dia 3.19

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** Subordinar segurança e acessibilidade a ajuste posterior cria uma tese unilateral que não enfrenta os riscos exigidos pelo comando.
- **B) está errada:** Um canal presencial, isoladamente, não mede desempenho nem garante segurança ou inclusão no serviço digital.
- **C) está errada:** Atribuir os resultados exclusivamente ao treinamento ignora desenho do serviço, infraestrutura, governança e condições de acesso.
- **D) está correta:** A tese apresenta ganho possível, condições verificáveis e resposta ao risco de exclusão, oferecendo eixos claros para argumentação.
- **Conceito cobrado:** Formulação de tese, relação causal condicionada e projeto argumentativo.
- **Pegadinha usada:** Escolher uma frase categórica ou temática que menciona o assunto, mas não articula ganhos, riscos e critérios de avaliação.
- **Como pensar para acertar:** Verifique se a tese responde ao recorte, admite condições e antecipa argumentos que possam ser desenvolvidos e comprovados.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5).

#### Comentário Extra Dia 3.20

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** Verbo e adjetivos concordam corretamente com `planilhas`, `pareceres` e `servidores`.
- **B) está errada:** Os adjetivos estão ajustados, mas `segue` não concorda com o sujeito plural `as planilhas`.
- **C) está errada:** O verbo concorda, porém `anexo` e `incluso` não concordam com os substantivos plurais.
- **D) está errada:** O verbo deve concordar com `planilhas`, `incluso` com `pareceres` e `quite` com `servidores`.
- **Conceito cobrado:** Concordância nominal e verbal.
- **Pegadinha usada:** Corrigir apenas o verbo e ignorar a flexão dos adjetivos predicativos ou anexos.
- **Como pensar para acertar:** Localize o referente de cada forma variável e confira gênero e número um a um.
- **Referência à apostila de estudo:** [Dia 3 — Bloco 5 — Língua Portuguesa](semana_01_estudo.md#s1-d3-b5).

---

# Dia 4 — Legislação CRA-PR/CFA

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

**Confirmação prévia das normas do Dia 4:** foram utilizadas fontes oficiais para orientar as questões de Lei 4.769/1965, Decreto 61.934/1967, Lei 12.514/2011, RN CFA 649/2024, RN CFA 670/2025, RN CFA 546/2018, RN CFA 626/2023, RN CFA 589/2020, RN CFA 651/2024, RN CFA 671/2025, RN CFA 680/2025 e Regimento Interno do CRA-PR. As questões evitam cobrar artigo, prazo ou penalidade específica quando isso exigiria reprodução literal ou confirmação pontual além da ementa/fonte oficial consultada.

## Questões principais

### Questão 1
**Nível: Médio**

Uma sociedade empresária sediada no Paraná passa a oferecer, de modo habitual, serviços técnicos enquadrados no campo da Administração, mas sustenta que o CNPJ ativo torna desnecessária qualquer providência perante o conselho profissional. À luz da legislação estudada, a conclusão correta é:

A) somente os sócios pessoas físicas podem estar sujeitos ao Sistema CFA/CRAs, nunca a pessoa jurídica.
B) a natureza das atividades pode sujeitar a empresa ao registro e à fiscalização do CRA-PR, no âmbito de sua jurisdição.
C) cabe ao CFA realizar diretamente todo registro e toda fiscalização local, pois os CRAs exercem apenas função consultiva.
D) o CNPJ e a indicação informal de um profissional registrado tornam desnecessária a análise da atividade básica da empresa.

### Questão 2
**Nível: Médio**

Um profissional permite que terceiro utilize seu número de registro para assinar documento técnico que ele não elaborou nem supervisionou. Segundo o Código de Ética estudado, essa conduta:

A) pode configurar uso indevido do nome ou do registro e é incompatível com a responsabilidade profissional.
B) gera apenas necessidade de atualização cadastral, sem repercussão ética.
C) torna-se regular se houver consentimento escrito entre os envolvidos.
D) é admitida quando o documento eletrônico também contém a assinatura do verdadeiro autor.

### Questão 3
**Nível: Médio**

O CRA-PR identifica pessoa física exercendo atividade sujeita ao registro profissional, em município paranaense, sem a regularidade exigida. A providência institucional mais compatível com suas atribuições é:

A) fiscalizar a regularidade do exercício profissional dentro de sua jurisdição.
B) aguardar provocação formal do CFA, pois o CRA não pode iniciar fiscalização regional.
C) remeter obrigatoriamente o caso ao CFA, que detém competência exclusiva para toda atuação local.
D) limitar-se à cobrança de anuidades, porque a verificação do exercício profissional não integra suas funções.

### Questão 4
**Nível: Médio**

Assinale a alternativa que distingue corretamente as funções do CFA e dos CRAs no sistema profissional.

A) O CFA executa ordinariamente a fiscalização em cada município, e os CRAs apenas emitem pareceres consultivos.
B) Cada CRA pode afastar norma nacional do CFA sempre que entender mais adequada uma disciplina local.
C) O CFA exerce função normativa e orientadora em âmbito nacional, enquanto o CRA atua no registro e na fiscalização em sua região.
D) CFA e CRA possuem a mesma competência territorial, variando apenas a denominação do órgão.

### Questão 5
**Nível: Médio**

No conjunto normativo indicado para o CRA-PR, a RN CFA nº 651/2024 tem por objeto:

A) aprovar o Regimento Interno do CRA-PR.
B) aprovar o Regulamento das Eleições do Sistema CFA/CRAs.
C) instituir o Programa Especial de Recuperação de Créditos dos Conselhos Regionais.
D) aprovar o Regulamento de Registro de pessoas físicas e jurídicas do Sistema CFA/CRAs.

### Questão 6
**Nível: Médio**

De acordo com a consolidação normativa utilizada no edital, o Código de Ética e Disciplina dos Profissionais de Administração está aprovado pela:

A) RN CFA nº 640/2024, que permaneceu vigente sem revogação posterior.
B) RN CFA nº 649/2024, dedicada ao registro profissional.
C) RN CFA nº 651/2024, que aprovou o Regimento Interno do CRA-PR.
D) RN CFA nº 671/2025.

### Questão 7
**Nível: Médio**

Um profissional conhece informação confidencial de cliente em razão de trabalho regularmente executado. Segundo o Código de Ética, ele deve:

A) manter silêncio absoluto até mesmo diante de dever legal específico ou requisição legítima.
B) preservar o sigilo, ressalvadas a justa causa e as hipóteses legais ou profissionais cabíveis.
C) tratar o sigilo como facultativo quando não conseguir identificar prejuízo econômico imediato.
D) compartilhar a informação com parceiros comerciais sempre que eles também estiverem sujeitos a dever genérico de confidencialidade.

### Questão 8
**Nível: Médio**

Durante fiscalização regular, uma pessoa jurídica registrada oculta documentos pertinentes e cria obstáculos deliberados ao trabalho do CRA. À luz do material, essa conduta:

A) é apenas irregularidade procedimental sem relevância quando o registro da empresa está ativo.
B) decorre do direito de defesa, que autoriza recusa geral e imotivada a qualquer solicitação fiscalizatória.
C) não pode ser examinada pelo Código de Ética, pois suas disposições alcançam exclusivamente pessoas físicas.
D) pode caracterizar obstrução à fiscalização e gerar repercussão ética ou administrativa.

### Questão 9
**Nível: Médio**

A Lei Federal nº 4.769/1965 ocupa posição central no estudo porque:

A) disciplina exclusivamente anuidades, taxas e execução de créditos dos conselhos.
B) aprova diretamente o atual Regimento Interno do CRA-PR.
C) dispõe sobre o exercício da profissão de Administrador e fornece base legal ao Sistema CFA/CRAs.
D) institui apenas regras éticas, sem tratar da organização profissional.

### Questão 10
**Nível: Médio**

Quanto à relação entre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967, assinale a alternativa correta.

A) O decreto pode afastar comandos da lei quando trouxer solução administrativa posterior.
B) O decreto regulamenta a lei profissional, devendo permanecer dentro dos limites legais.
C) O decreto constitui regimento autônomo do CRA-PR e não se relaciona ao exercício profissional.
D) O decreto cuida apenas das eleições do Sistema CFA/CRAs.

### Questão 11
**Nível: Médio**

Conforme o Regimento Interno estudado, o CRA-PR é:

A) autarquia federal de atuação nacional, subordinada hierarquicamente ao CFA em todos os seus atos administrativos.
B) autarquia dotada de personalidade jurídica de direito público, autonomia técnica, administrativa e financeira e jurisdição no Estado do Paraná.
C) empresa pública estadual encarregada de executar políticas de emprego para administradores.
D) associação privada de filiação facultativa, sem poder de fiscalização profissional.

### Questão 12
**Nível: Médio**

A edição de orientação normativa geral destinada a todos os Conselhos Regionais de Administração situa-se, em regra, na esfera do:

A) coletivo de pessoas físicas e jurídicas registradas, por votação direta.
B) Plenário do CRA-PR, por ser órgão deliberativo superior em toda a federação.
C) conjunto dos CRAs, independentemente de deliberação ou norma nacional do CFA.
D) CFA, por sua função normativa e orientadora nacional.

### Questão 13
**Nível: Médio**

Por que a RN CFA nº 649/2024 e a RN CFA nº 670/2025 devem ser lidas em conjunto?

A) A primeira aprova o Regulamento de Registro e a segunda o altera.
B) A primeira aprova o regulamento eleitoral e a segunda altera o processo de votação.
C) Ambas substituem integralmente a Lei nº 4.769/1965 no tema do exercício profissional.
D) A primeira aprova o Código de Ética e a segunda disciplina suas sanções.

### Questão 14
**Nível: Médio**

No mapa de normas do edital, a RN CFA nº 589/2020 está associada ao tema:

A) Regimento Interno do CRA-PR.
B) eleições no Sistema CFA/CRAs.
C) fiscalização no Sistema CFA/CRAs.
D) Código de Ética aprovado em 2025.

### Questão 15
**Nível: Médio**

Conforme a ementa oficial consolidada no material, a RN CFA nº 626/2023 relaciona-se ao:

A) funcionamento interno do CRA-PR.
B) Regulamento de Registro do Sistema CFA/CRAs.
C) Programa Especial de Recuperação de Créditos — PERC.
D) Código de Ética e Disciplina.

### Questão 16
**Nível: Médio**

A RN CFA nº 546/2018 foi incluída no edital por tratar da:

A) aprovação do Código de Ética e Disciplina.
B) recuperação especial de créditos por meio do PERC.
C) alteração do Regulamento de Registro do Sistema CFA/CRAs.
D) isenção de débitos concedida pelos Conselhos Regionais de Administração.

### Questão 17
**Nível: Médio**

A Lei nº 12.514/2011 integra o estudo do sistema de conselhos profissionais principalmente porque disciplina:

A) contribuições devidas aos conselhos profissionais e aspectos de sua cobrança.
B) campos privativos de atuação previstos para o Administrador.
C) a estrutura interna específica do CRA-PR.
D) deveres éticos e hipóteses de sigilo dos Profissionais de Administração.

### Questão 18
**Nível: Médio**

Ao analisar a consequência de uma infração ética, o candidato deve considerar:

A) que todas as sanções são aplicáveis de forma idêntica a pessoas físicas e jurídicas.
B) que a penalidade máxima decorre automaticamente da simples comprovação material da conduta.
C) a norma aplicável, a gravidade do caso e as especificidades previstas para pessoa física ou jurídica.
D) que apenas decisão judicial criminal pode impor qualquer sanção no âmbito profissional.

### Questão 19
**Nível: Médio**

Um profissional assina relatório técnico elaborado por terceiro, embora não tenha orientado, supervisionado nem participado do trabalho. À luz do Código de Ética, a melhor conclusão é:

A) a assinatura é regular se o autor material do relatório tiver dado autorização escrita.
B) o ato torna-se regular quando a pessoa jurídica contratante possui registro ativo no CRA.
C) a irregularidade somente existe se for demonstrado prejuízo econômico ao cliente.
D) a conduta pode configurar infração ética: a assinatura técnica exige participação efetiva.

### Questão 20
**Nível: Médio**

Assinale a alternativa incorreta a respeito do sigilo profissional.

A) O dever alcança informações conhecidas em razão da atividade profissional.
B) A expectativa de vantagem comercial, por si só, autoriza a divulgação de informação confidencial.
C) O sigilo pode conviver com obrigações legais e com atuação fiscalizatória legítima.
D) A justa causa e as hipóteses legais precisam ser consideradas na análise do dever de sigilo.

### Questão 21
**Nível: Difícil**

Assinale a associação correta entre norma e objeto no conjunto estudado.

A) RN CFA nº 651/2024 — Código de Ética; RN CFA nº 671/2025 — Regimento Interno do CRA-PR.
B) RN CFA nº 649/2024 — eleições; RN CFA nº 680/2025 — registro profissional.
C) RN CFA nº 626/2023 — fiscalização; RN CFA nº 589/2020 — recuperação de créditos.
D) RN CFA nº 651/2024 — Regimento Interno do CRA-PR; RN CFA nº 671/2025 — Código de Ética e Disciplina.

### Questão 22
**Nível: Difícil**

Uma empresa presta de forma habitual serviços enquadrados no campo da Administração. Quanto à regularidade perante o Sistema CFA/CRAs, é correto afirmar que:

A) a pessoa jurídica somente se sujeita a registro se todos os seus sócios forem Administradores.
B) a indicação de responsável técnico registrado sempre substitui o eventual registro da pessoa jurídica.
C) a existência de CNPJ e contrato social impede a incidência de regras profissionais sobre a empresa.
D) a atividade pode sujeitar a pessoa jurídica a registro e fiscalização, além de exigir responsabilidade técnica.

### Questão 23
**Nível: Difícil**

Segundo o Regimento Interno aprovado pela RN CFA nº 651/2024, o CRA-PR possui sede na capital e jurisdição:

A) restrita ao município de Curitiba, com delegação eventual aos demais municípios.
B) em todo o Estado do Paraná.
C) sobre os três estados da Região Sul.
D) nacional, embora a fiscalização ordinária se concentre no Paraná.

### Questão 24
**Nível: Difícil**

Um candidato confunde conselho profissional com sindicato. A correção conceitual adequada é:

A) o conselho exerce função pública de registro e fiscalização profissional; o sindicato representa interesses da categoria, possuindo natureza e finalidade distintas.
B) o conselho representa interesses trabalhistas coletivos, enquanto o sindicato aplica sanções éticas e mantém o registro profissional.
C) ambos são autarquias e diferem apenas pela abrangência territorial.
D) o sindicato é unidade descentralizada do conselho e executa obrigatoriamente suas resoluções.

### Questão 25
**Nível: Difícil**

A norma do edital associada ao Regulamento das Eleições do Sistema CFA/CRAs é a:

A) RN CFA nº 546/2018.
B) RN CFA nº 589/2020.
C) RN CFA nº 680/2025.
D) RN CFA nº 651/2024.

### Questão 26
**Nível: Difícil**

Ao estudar uma resolução cuja íntegra não foi consolidada na apostila, mas cuja ementa oficial foi confirmada, a postura tecnicamente mais segura é:

A) completar prazos e requisitos por analogia com outro conselho profissional.
B) presumir que toda resolução do CFA contém o mesmo procedimento e as mesmas sanções.
C) substituir a norma pela lei federal mais próxima, ainda que tratem de objetos diferentes.
D) restringir a conclusão ao objeto confirmado e consultar a fonte oficial antes de afirmar prazos ou penalidades.

### Questão 27
**Nível: Difícil**

Durante uma diligência, o fiscalizado dirige ofensas pessoais à equipe e recusa, sem justificativa, acesso a documentos pertinentes. No plano ético-profissional, o caso pode envolver:

A) imunidade decorrente do direito de defesa, que abrange ofensas e obstrução deliberada.
B) apenas inadimplemento contratual privado, porque a fiscalização não integra a atividade dos CRAs.
C) violação de urbanidade e possível obstrução à fiscalização, sem prejuízo do devido processo para apuração.
D) nulidade automática da diligência, independentemente da regularidade da solicitação feita.

### Questão 28
**Nível: Difícil**

Uma resolução posterior altera dispositivos do Regulamento de Registro aprovado por resolução anterior. Para identificar a disciplina vigente, deve-se:

A) ignorar a alteração enquanto a resolução original não for formalmente republicada pela União.
B) consultar apenas a resolução alteradora, pois ela necessariamente reproduz todo o regulamento.
C) ler o texto anterior em conjunto com as alterações posteriores, observando o alcance expresso de cada modificação.
D) considerar revogado todo o regulamento anterior, mesmo quando a norma posterior altera apenas dispositivos determinados.

### Questão 29
**Nível: Difícil**

Na estrutura do CRA-PR descrita no Regimento Interno, o órgão deliberativo superior é:

A) o Plenário.
B) a Ouvidoria, por receber manifestações externas e revisar todas as decisões do conselho.
C) a representação institucional, que substitui os órgãos colegiados nas matérias normativas.
D) a Diretoria Executiva, responsável também pela deliberação plenária em caráter permanente.

### Questão 30
**Nível: Difícil**

No desenho regimental do CRA-PR, a Diretoria Executiva está mais diretamente ligada:

A) à execução e à administração das deliberações e atividades do Conselho.
B) ao controle externo de manifestações atribuído à Ouvidoria.
C) à função deliberativa superior reservada ao Plenário.
D) à edição de normas nacionais vinculantes para todos os CRAs.

### Questão 31
**Nível: Difícil**

Servidor público regularmente inscrito no CRA exerce, em seu cargo, atividade própria do campo profissional. Quanto ao Código de Ética:

A) ele se aplica apenas ao exercício liberal e nunca alcança atividade funcional.
B) o estatuto funcional elimina automaticamente toda responsabilidade perante o sistema profissional.
C) os deveres éticos profissionais continuam pertinentes quando a atuação se insere no campo da profissão.
D) a incidência depende exclusivamente de remuneração privada adicional.

### Questão 32
**Nível: Difícil**

Para compreender conjuntamente a base legal e a regulamentação do exercício profissional, o par normativo central é:

A) RN CFA nº 589/2020 e RN CFA nº 671/2025.
B) Lei nº 12.514/2011 e RN CFA nº 626/2023.
C) RN CFA nº 651/2024 e RN CFA nº 680/2025.
D) Lei nº 4.769/1965 e Decreto nº 61.934/1967.

### Questão 33
**Nível: Difícil**

Assinale a alternativa incorreta à luz dos deveres éticos estudados.

A) O Código de Ética alcança pessoas físicas e jurídicas, observadas as especificidades aplicáveis.
B) O dever de sigilo admite análise de justa causa e de hipóteses legais.
C) A independência técnica pode ser abandonada sempre que o cliente registrar a ordem por escrito.
D) A atualização cadastral e o aperfeiçoamento profissional integram deveres relevantes.

### Questão 34
**Nível: Difícil**

A obrigação de manter endereço e dados cadastrais atualizados perante o Conselho contribui para:

A) substituir a renovação de registro por simples comunicação informal.
B) viabilizar comunicações, fiscalização e controle regular do vínculo profissional.
C) transferir ao CFA toda comunicação destinada ao profissional inscrito no CRA.
D) sanar automaticamente qualquer infração anterior praticada pelo inscrito.

### Questão 35
**Nível: Difícil**

Um cliente exige que o profissional omita dado tecnicamente relevante para melhorar a aparência de um parecer. A resposta compatível com o Código de Ética é:

A) atender, pois a defesa do cliente prevalece sobre qualquer limite técnico.
B) preservar honestidade, responsabilidade e independência técnica, recusando a omissão indevida.
C) atender se houver cláusula contratual de confidencialidade sobre o parecer.
D) transferir a assinatura a outro profissional, mantendo a mesma omissão.

### Questão 36
**Nível: Difícil**

A RN CFA nº 649/2024 é corretamente identificada, no material, como a norma que:

A) aprova o Regulamento das Eleições do Sistema CFA/CRAs.
B) institui o Programa Especial de Recuperação de Créditos dos CRAs.
C) aprova o Regimento Interno específico do CRA-PR.
D) aprova o Regulamento de Registro de pessoas físicas e jurídicas no Sistema CFA/CRAs.

### Questão 37
**Nível: Difícil**

A respeito da RN CFA nº 670/2025 e da hierarquia normativa, assinale a alternativa correta.

A) A resolução promove alterações no regulamento aprovado por outra resolução, sem poder revogar lei federal.
B) A resolução substitui o Decreto nº 61.934/1967 em toda matéria profissional.
C) A resolução altera automaticamente qualquer lei federal que mencione registro profissional.
D) A resolução pode revogar a Lei nº 4.769/1965 porque é mais recente.

### Questão 38
**Nível: Difícil**

Assinale a sequência que associa corretamente as três resoluções aos respectivos temas: RN CFA nº 589/2020; RN CFA nº 626/2023; RN CFA nº 680/2025.

A) registro; ética; regimento interno.
B) fiscalização; PERC; eleições.
C) eleições; fiscalização; registro.
D) PERC; isenção de débitos; ética.

### Questão 39
**Nível: Difícil**

Uma denúncia relata exercício irregular da profissão em cidade do interior do Paraná. Em regra, a apuração fiscalizatória regional insere-se na competência do:

A) CRA-PR, por exercer registro e fiscalização em sua jurisdição.
B) CFA, porque somente o órgão nacional pode verificar exercício irregular.
C) Plenário do CFA, como instância inicial obrigatória de toda fiscalização municipal.
D) Poder Executivo estadual, pois o CRA não possui função fiscalizatória própria.

### Questão 40
**Nível: Difícil**

O dever de aperfeiçoamento profissional deve ser compreendido como:

A) obrigação exclusiva do empregador, sem participação do inscrito.
B) compromisso do profissional com atualização e qualidade responsável de sua atuação.
C) faculdade sem relação com zelo, competência ou responsabilidade técnica.
D) dever que pode ser integralmente delegado ao responsável administrativo da pessoa jurídica.

### Questão 41
**Nível: Muito difícil**

Um cliente pede ao profissional que omita de parecer uma limitação metodológica relevante, alegando que a informação prejudicaria a negociação. A omissão tornaria a conclusão mais favorável, mas tecnicamente incompleta. À luz dos deveres profissionais, a conduta adequada é:

A) omitir a limitação, porque a defesa do interesse econômico confiado prevalece enquanto não houver ordem judicial em contrário.
B) registrar a limitação apenas em arquivo interno e entregar ao destinatário o parecer incompleto solicitado pelo cliente.
C) recusar a distorção, explicitar a limitação relevante e defender apenas interesses legítimos, preservando independência técnica e limites éticos e legais.
D) encerrar automaticamente o contrato sem esclarecer o problema, pois qualquer divergência técnica impede a continuidade da relação profissional.

### Questão 42
**Nível: Muito difícil**

O enunciado descreve uma infração, mas não informa artigo, circunstâncias agravantes nem elementos suficientes para individualizar a sanção. A resposta mais rigorosa é:

A) reconhecer a possível infração, mas não inventar penalidade específica sem consultar a norma e os elementos do caso.
B) aplicar automaticamente a sanção mais grave para evitar impunidade.
C) importar a penalidade prevista em norma de outro conselho profissional.
D) concluir que nenhuma responsabilização é possível enquanto não houver condenação judicial.

### Questão 43
**Nível: Muito difícil**

Quanto à aplicação do Código de Ética às pessoas jurídicas registradas, assinale a alternativa correta.

A) Todas as sanções previstas para pessoa física incidem de modo idêntico sobre a pessoa jurídica.
B) A incidência do Código sobre pessoa jurídica depende de adesão voluntária no ato de registro.
C) A pessoa jurídica somente se submete ao Código quando todos os sócios possuem registro profissional.
D) O Código alcança a pessoa jurídica, mas suspensão e cancelamento não se aplicam a ela.

### Questão 44
**Nível: Muito difícil**

Durante a preparação, o candidato encontra duas versões de uma resolução em materiais não oficiais e uma questão sem indicação de prova, embora redigida no estilo da banca. Qual procedimento compromete a rastreabilidade e deve ser rejeitado?

A) confrontar número, ementa, vigência e eventuais alterações no repositório oficial antes de consolidar o conteúdo.
B) usar o edital para delimitar o objeto e consultar o texto oficial completo quando a ementa não resolver a dúvida.
C) classificar como autoral uma questão apenas inspirada no estilo da banca e indicar separadamente a fonte normativa utilizada.
D) atribuir origem oficial pela semelhança de estilo e escolher como vigente a versão mais recente do material, sem validar metadados oficiais.

### Questão 45
**Nível: Muito difícil**

Ao planejar a fiscalização, a gestão compara dois casos: uma atividade potencialmente lesiva exercida sem habilitação e uma falha cadastral formal de baixo risco. Propõe-se priorizar apenas ações com maior arrecadação. Qual diretriz compatibiliza finalidade institucional, risco social e limites de atuação?

A) concentrar toda a fiscalização nos inscritos, pois a proteção econômica da categoria é a finalidade exclusiva do sistema.
B) priorizar o risco social, atuar dentro da competência e observar o devido processo, usando orientação, registro e fiscalização sem tratar arrecadação como fim.
C) assumir competência sobre qualquer atividade econômica relacionada ao caso, ainda que atribuída por lei a outro órgão público.
D) selecionar primeiro as infrações de maior retorno financeiro, pois a arrecadação substitui a análise de risco e de interesse público.

### Questão 46
**Nível: Muito difícil**

Uma empresa indica formalmente responsável técnico, mas ele apenas empresta o nome e não orienta nem supervisiona os serviços. A análise correta é:

A) a situação pode caracterizar responsabilidade fictícia, empréstimo de nome ou registro e ausência de atuação técnica real.
B) a irregularidade é exclusivamente contratual e não se relaciona ao uso do registro profissional.
C) a indicação documental basta para demonstrar responsabilidade efetiva, independentemente da atuação concreta.
D) o registro ativo da empresa elimina qualquer dever individual do responsável indicado.

### Questão 47
**Nível: Muito difícil**

Uma instrução operacional do CRA-PR passa a adotar critério incompatível com norma nacional válida do CFA sobre a mesma matéria. Ao identificar o conflito, qual solução respeita a distribuição de competências do Sistema CFA/CRAs?

A) manter o critério regional, porque a jurisdição estadual autoriza afastar unilateralmente toda orientação normativa nacional.
B) rever o ato regional e alinhar a execução fiscalizatória à norma nacional, tratando eventual discordância pelos canais institucionais competentes.
C) considerar a norma nacional automaticamente revogada pela instrução regional posterior, ainda que editada por órgão diverso.
D) transferir à Diretoria Executiva do CRA-PR o poder de alterar a regra nacional para todos os Conselhos Regionais.

### Questão 48
**Nível: Muito difícil**

O CRA-PR mantém sua sede em Curitiba, instala atendimento descentralizado em Londrina e realiza fiscalização em Cascavel. Qual consequência institucional decorre corretamente da distinção entre sede, unidade de atendimento e jurisdição?

A) a unidade de Londrina passa a exercer jurisdição própria e independente sobre os municípios próximos.
B) a atuação em Cascavel depende da criação prévia de um Conselho municipal com personalidade jurídica autônoma.
C) a sede permanece na capital e a jurisdição alcança todo o Paraná; unidades descentralizadas não se tornam novos Conselhos autônomos.
D) a instalação de atendimento fora da capital converte a jurisdição estadual do CRA-PR em competência nacional compartilhada.

### Questão 49
**Nível: Muito difícil**

Um inscrito orienta pessoa sem habilitação a exercer atividade profissional sujeita ao sistema, ainda que não obtenha lucro e não se prove dano concreto. À luz do Código de Ética:

A) a ausência de lucro exclui necessariamente a relevância ética da colaboração.
B) a conduta somente pode ser examinada depois de condenação penal da pessoa auxiliada.
C) auxiliar pessoa não habilitada a exercer a profissão pode configurar infração, mesmo sem lucro ou dano.
D) o registro regular do inscrito autoriza que ele transfira informalmente sua habilitação.

### Questão 50
**Nível: Muito difícil**

A Lei nº 4.769/1965 estabelece determinado requisito profissional; o Decreto nº 61.934/1967 disciplina sua execução, e uma resolução administrativa recebe interpretação que dispensaria o requisito legal. Qual método resolve adequadamente esse conflito aparente?

A) aplicar a resolução por ser mais específica e recente, ainda que a interpretação afaste diretamente o requisito previsto em lei.
B) interpretar decreto e resolução dentro dos limites da lei, rejeitando leitura regulamentar que crie contradição ou dispense requisito legal.
C) aplicar sempre o decreto posterior, porque a cronologia basta para que regulamento modifique a lei regulamentada.
D) escolher livremente a norma mais favorável ao interessado, pois atos do sistema profissional possuem a mesma hierarquia da lei.

## Questões extras de revisão fixa do Dia 4

#### Extra Dia 4.1

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Modalidade concurso na Lei nº 14.133/2021
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Na Lei nº 14.133/2021, a modalidade destinada à escolha de trabalho técnico, científico ou artístico, com julgamento por melhor técnica ou conteúdo artístico e concessão de prêmio ou remuneração ao vencedor, é:

A) o pregão, empregado também para a alienação de bens imóveis.
B) o leilão, utilizado para selecionar projetos técnicos mediante prêmio.
C) o concurso.
D) a concorrência, necessariamente adotada sempre que houver trabalho artístico.

#### Extra Dia 4.2

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Elementos da responsabilidade civil objetiva do Estado
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Para examinar a responsabilidade civil objetiva do Estado por atuação de agente público, o roteiro básico deve verificar:

A) conduta estatal, dano e nexo causal, além de eventual causa excludente ou atenuante.
B) apenas o dano, pois a conduta e o nexo são presumidos de modo absoluto.
C) dolo do agente, culpa da vítima e condenação penal prévia.
D) culpa administrativa comprovada e inexistência de qualquer excludente.

#### Extra Dia 4.3

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Publicidade administrativa e proteção de dados pessoais
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Um relatório administrativo contém decisões de interesse coletivo e, nos anexos, dados pessoais sem relação necessária com a divulgação. Qual conduta é compatível com a publicidade administrativa estudada?

A) Negar acesso ao relatório inteiro, pois qualquer dado pessoal transforma todo o processo em sigiloso.
B) Divulgar integralmente o documento, porque a publicidade elimina toda proteção conferida a dados pessoais.
C) Substituir os dados por mensagem de promoção da autoridade responsável, desde que o relatório permaneça disponível.
D) Dar acesso às partes de interesse público e resguardar os dados pessoais sem divulgação autorizada, fundamentando a restrição.

#### Extra Dia 4.4

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Culpa concorrente da vítima
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Se a conduta da vítima concorre para a produção do dano, essa circunstância:

A) é irrelevante no regime objetivo e jamais altera a reparação.
B) sempre rompe integralmente o nexo causal e exclui a responsabilidade estatal.
C) pode reduzir a indenização, conforme a contribuição causal demonstrada.
D) transfere automaticamente toda responsabilidade ao agente público.

#### Extra Dia 4.5

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Excludentes do nexo causal
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Caso fortuito ou força maior, na responsabilidade civil do Estado:

A) pode excluir a responsabilidade quando efetivamente romper o nexo causal.
B) gera responsabilidade automática sempre que o fato ocorrer em bem público.
C) atua apenas para reduzir o valor, sem possibilidade de romper o nexo causal.
D) jamais interfere no dever de indenizar, porque a responsabilidade é objetiva.

#### Extra Dia 4.6

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Motivação objetiva do ato administrativo
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Ao indeferir um pedido administrativo, a autoridade apresenta apenas a frase “por conveniência do setor”, sem indicar fatos nem fundamento jurídico. À luz da motivação objetiva, a decisão:

A) está suficientemente motivada, pois qualquer menção à conveniência encerra o dever de justificar.
B) deve expor os pressupostos de fato e de direito que sustentam a conclusão administrativa.
C) pode permanecer sem justificativa sempre que o resultado seja desfavorável ao interessado.
D) só precisa indicar fundamento depois de eventual recurso, quando a motivação passa a ser obrigatória.

#### Extra Dia 4.7

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Princípio da moralidade administrativa
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

O princípio da moralidade administrativa exige atuação:

A) apenas formalmente conforme a lei, ainda que desleal ou desonesta.
B) conforme a convicção moral pessoal do agente, independentemente de padrões institucionais.
C) orientada exclusivamente pela eficiência, ainda que outros princípios sejam sacrificados.
D) ética, leal e proba, para além da simples aparência de legalidade.

#### Extra Dia 4.8

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Motivo e motivação do ato administrativo
**Nível:** Médio
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Em relação aos elementos do ato administrativo, a motivação corresponde:

A) ao acontecimento material que produz o efeito do ato, confundindo-se com seu resultado.
B) à exposição dos pressupostos de fato e de direito que sustentam a decisão.
C) à competência legal atribuída ao agente que pratica o ato.
D) a uma formalidade dispensável em todo ato discricionário.

#### Extra Dia 4.9

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Impessoalidade, moralidade e desvio de finalidade
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Uma autoridade direciona fiscalização para prejudicar desafeto pessoal, embora tente apresentar justificativa formal. A conduta viola mais diretamente:

A) apenas a publicidade, porque o vício desaparece se a motivação for divulgada.
B) somente a eficiência, pois o resultado fiscalizatório pode ser financeiramente útil.
C) a legalidade, mas não a impessoalidade, já que a autoridade possui competência para fiscalizar.
D) a impessoalidade e a moralidade, além de poder revelar desvio da finalidade pública.

#### Extra Dia 4.10

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Distinção entre motivo e motivação
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4)

Em um ato administrativo, a situação concreta prevista pela norma é registrada no processo e a autoridade explica por que esses fatos justificam a decisão. A distinção correta é:

A) motivo e motivação são sinônimos e correspondem apenas à forma externa do documento.
B) motivo é a divulgação pública do ato, enquanto motivação é a competência legal da autoridade.
C) motivo reúne os pressupostos de fato e de direito; motivação é a exposição desses pressupostos na decisão.
D) motivo é sempre discricionário, e motivação somente existe quando o interessado concorda com o resultado.

#### Extra Dia 4.11

**Dia:** 4
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Prática discursiva
**Assunto:** Estrutura do parágrafo argumentativo
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5)

Qual alternativa apresenta um parágrafo argumentativo completo, com ideia central, justificativa e consequência relacionada ao tema da ética no serviço público?

A) Ética no serviço público. Fiscalização. Confiança. Responsabilidade.
B) A ética é importante, conforme diversas normas existentes, e esse fato dispensa explicar seus efeitos práticos.
C) Embora o tema seja relevante, qualquer exemplo concreto reduziria a objetividade e deve ser evitado.
D) A ética orienta decisões imparciais porque impede que interesses privados prevaleçam; assim, fortalece a confiança social na atuação administrativa.

#### Extra Dia 4.12

**Dia:** 4
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Prática discursiva
**Assunto:** Emprego do acento indicativo de crase
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5)

Assinale a alternativa em que o acento indicativo de crase está empregado incorretamente.

A) O fiscal referiu-se àquela irregularidade.
B) A equipe começou à revisar os autos pela manhã.
C) O processo foi encaminhado à chefia competente.
D) A reunião terá início às 14 horas.

#### Extra Dia 4.13

**Dia:** 4
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Prática discursiva
**Assunto:** Conectivos concessivos
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5)

Qual reescrita preserva a relação concessiva de “Ainda que o prazo seja curto, a equipe concluirá a análise”?

A) Porque o prazo é curto, a equipe concluirá a análise.
B) Mesmo que o prazo seja curto, a equipe concluirá a análise.
C) Para que o prazo seja curto, a equipe concluirá a análise.
D) Logo que o prazo seja curto, a equipe concluirá a análise.

#### Extra Dia 4.14

**Dia:** 4
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Prática discursiva
**Assunto:** Formulação de tese argumentativa
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5)

Para iniciar um texto sobre ética e eficiência no serviço público, assinale a tese mais adequada.

A) A eficiência pública produz resultados legítimos quando permanece vinculada à legalidade, à impessoalidade e à responsabilidade ética dos agentes.
B) Ética e eficiência são assuntos importantes, e o texto apresentará algumas informações sobre ambos.
C) A Administração Pública possui muitos problemas, todos causados exclusivamente pela falta de tecnologia.
D) Ser eficiente é agir rapidamente, ainda que controles jurídicos e deveres éticos sejam afastados.

#### Extra Dia 4.15

**Dia:** 4
**Bloco:** 5 — Português ou prática discursiva
**Matéria:** Prática discursiva
**Assunto:** Conclusão argumentativa e retomada da tese
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5)

Qual conclusão encerra adequadamente um parágrafo que defendeu transparência com proteção de dados, sem introduzir argumento novo?

A) Portanto, a Administração deve divulgar informações de interesse público e, ao mesmo tempo, resguardar dados pessoais sem base para exposição, equilibrando os deveres já examinados.
B) Em conclusão, seria necessário discutir também toda a história constitucional do país, assunto que não foi tratado no desenvolvimento.
C) Assim, transparência significa publicar integralmente qualquer documento, pois restrições nunca podem ser justificadas.
D) Logo, proteção de dados e publicidade são incompatíveis, razão pela qual uma delas deve sempre ser eliminada.

#### Extra Dia 4.16

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Raciocínio Lógico-Matemático
**Assunto:** Proporcionalidade direta
**Nível:** Difícil
**Referência:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4)

Uma equipe analisa 72 processos em 6 dias, mantendo ritmo constante. No mesmo ritmo, quantos processos analisará em 10 dias?

A) 126.
B) 108.
C) 120.
D) 144.

#### Extra Dia 4.17

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Raciocínio Lógico-Matemático
**Assunto:** Inclusão-exclusão com três conjuntos e cálculo do complemento
**Nível:** Muito difícil
**Referência:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4)

Em um grupo de 100 candidatos, 58 estudam Legislação, 50 estudam Português e 42 estudam Informática. Estudam Legislação e Português 28; Legislação e Informática 24; Português e Informática 20; e as três disciplinas, 12. As interseções aos pares incluem quem estuda as três. Quantos não estudam nenhuma delas?

A) 2.
B) 8.
C) 10.
D) 22.

#### Extra Dia 4.18

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Raciocínio Lógico-Matemático
**Assunto:** Negação de quantificadores e da conjunção
**Nível:** Muito difícil
**Referência:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4)

A negação lógica de “Todo fiscal conferiu o relatório e algum analista validou o parecer” é:

A) Nenhum fiscal conferiu o relatório e algum analista não validou o parecer.
B) Algum fiscal não conferiu o relatório ou nenhum analista validou o parecer.
C) Todo fiscal não conferiu o relatório ou algum analista não validou o parecer.
D) Algum fiscal conferiu o relatório e todo analista deixou de validar o parecer.

#### Extra Dia 4.19

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Raciocínio Lógico-Matemático
**Assunto:** Soma de progressão aritmética e aplicação sucessiva de percentual
**Nível:** Muito difícil
**Referência:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4)

Um plano prevê analisar 12 processos na primeira semana e aumentar a meta em 4 processos a cada semana, durante 10 semanas. Ao final, constatou-se que 20% do total planejado correspondiam a registros duplicados e foram excluídos. Quantos processos válidos permaneceram no plano?

A) 240.
B) 300.
C) 220.
D) 264.

#### Extra Dia 4.20

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Raciocínio Lógico-Matemático
**Assunto:** Probabilidade hipergeométrica e contagem de combinações sem reposição
**Nível:** Muito difícil
**Referência:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4)

De 10 acessos, 3 estão bloqueados e 7 liberados. Três acessos distintos são escolhidos ao acaso, sem reposição. Qual é a probabilidade de a amostra conter exatamente dois acessos liberados e um bloqueado?

A) 7/15.
B) 7/24.
C) 3/8.
D) 21/40.

## Entrega prática do Bloco 6 — Dia 4

**Referência:** [Dia 4 — Bloco 6 — Recuperação CFA × CRA e caderno de erros](semana_01_estudo.md#s1-d4-b6)

Sem consultar, classifique cinco casos em `sujeito | conduta | território | órgão | fonte | motivo da classificação`. Depois confira o Bloco 4 do Dia 3 e destaque cada correção. Use somente Lei, Decreto, Regimento aprovado pela RN nº 651/2024 ou Código de Ética aprovado pela RN nº 671/2025; não preencha lacunas com norma pendente.

## Gabarito do Dia 4

1. B
2. A
3. A
4. C
5. A
6. D
7. B
8. D
9. C
10. B
11. B
12. D
13. A
14. C
15. C
16. D
17. A
18. C
19. D
20. B
21. D
22. D
23. B
24. A
25. C
26. D
27. C
28. C
29. A
30. A
31. C
32. D
33. C
34. B
35. B
36. D
37. A
38. B
39. A
40. B
41. C
42. A
43. D
44. D
45. B
46. A
47. B
48. C
49. C
50. B

### Gabarito das questões extras de revisão fixa do Dia 4

Extra Dia 4.1: C
Extra Dia 4.2: A
Extra Dia 4.3: D
Extra Dia 4.4: C
Extra Dia 4.5: A
Extra Dia 4.6: B
Extra Dia 4.7: D
Extra Dia 4.8: B
Extra Dia 4.9: D
Extra Dia 4.10: C
Extra Dia 4.11: D
Extra Dia 4.12: B
Extra Dia 4.13: B
Extra Dia 4.14: A
Extra Dia 4.15: A
Extra Dia 4.16: C
Extra Dia 4.17: C
Extra Dia 4.18: B
Extra Dia 4.19: A
Extra Dia 4.20: D


## Comentários do Dia 4

### Comentário da Questão 1

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** A sujeição da pessoa jurídica não depende de todos os sócios serem profissionais; considera-se a atividade exercida.
- **B) está correta:** A atividade básica situada no campo profissional pode sujeitar a empresa ao registro e à fiscalização do CRA-PR.
- **C) está errada:** O CFA orienta e normatiza nacionalmente; a atuação ordinária de registro e fiscalização regional cabe ao CRA.
- **D) está errada:** CNPJ e indicação informal de profissional não substituem a verificação das exigências de registro e responsabilidade técnica.
- **Conceito cobrado:** Registro e fiscalização de pessoa jurídica.
- **Pegadinha usada:** Tratar CNPJ ou indicação informal de responsável como substitutos da regularidade profissional.
- **Como pensar para acertar:** Identifique a atividade efetivamente oferecida e, depois, o conselho regional competente.
- **Referência à apostila de estudo:** Dia 4 — “Registro, fiscalização e exercício irregular”.

### Comentário da Questão 2

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** Permitir uso do próprio registro sem elaboração ou supervisão pode configurar empréstimo de nome ou registro.
- **B) está errada:** Não se trata de simples dado cadastral: o número de registro vincula identidade e responsabilidade profissional.
- **C) está errada:** O consentimento não transforma empréstimo de registro em atuação técnica efetiva.
- **D) está errada:** A dupla assinatura ou o suporte eletrônico não supre a ausência de participação e responsabilidade do inscrito.
- **Conceito cobrado:** Uso indevido do nome ou registro profissional.
- **Pegadinha usada:** Confundir autorização formal ou assinatura eletrônica com atuação técnica real.
- **Como pensar para acertar:** Pergunte quem elaborou, orientou ou supervisionou o trabalho cuja responsabilidade está sendo assumida.
- **Referência à apostila de estudo:** Dia 4 — “Código de Ética: sigilo, zelo, independência e uso do registro”.

### Comentário da Questão 3

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A fiscalização regional da regularidade do exercício profissional integra a finalidade do CRA-PR.
- **B) está errada:** O CRA pode agir no âmbito de sua competência fiscalizatória sem depender de provocação prévia do CFA.
- **C) está errada:** A função nacional do CFA não elimina a competência executiva e fiscalizatória do conselho regional.
- **D) está errada:** O CRA não se limita à cobrança: registro e fiscalização são funções centrais do sistema.
- **Conceito cobrado:** Competência fiscalizatória regional.
- **Pegadinha usada:** Reduzir o CRA a arrecadador ou deslocar toda atuação local para o CFA.
- **Como pensar para acertar:** Associe CFA a orientação nacional e CRA a registro e fiscalização em sua jurisdição.
- **Referência à apostila de estudo:** Dia 4 — “Competência do CFA x competência do CRA”.

### Comentário da Questão 4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** A fiscalização local é função típica dos CRAs; o CFA não a executa ordinariamente em cada município.
- **B) está errada:** Norma regional não pode afastar unilateralmente disciplina nacional válida do sistema.
- **C) está correta:** A alternativa apresenta corretamente a distribuição geral: orientação normativa nacional pelo CFA e execução regional pelo CRA.
- **D) está errada:** As competências se articulam, mas as abrangências territoriais não são idênticas.
- **Conceito cobrado:** Distribuição de competências no Sistema CFA/CRAs.
- **Pegadinha usada:** Inverter o papel nacional do CFA e o papel regional dos CRAs.
- **Como pensar para acertar:** Use a dupla ‘normatização nacional / execução regional’ como eixo de comparação.
- **Referência à apostila de estudo:** Dia 4 — “Competência do CFA x competência do CRA”.

### Comentário da Questão 5

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A RN CFA nº 651/2024 aprova o Regimento Interno do CRA-PR.
- **B) está errada:** O regulamento eleitoral indicado é o aprovado pela RN CFA nº 680/2025.
- **C) está errada:** O PERC está associado à RN CFA nº 626/2023.
- **D) está errada:** O Regulamento de Registro está associado à RN CFA nº 649/2024.
- **Conceito cobrado:** Objeto da RN CFA nº 651/2024.
- **Pegadinha usada:** Trocar os objetos de resoluções próximas no mapa do edital.
- **Como pensar para acertar:** Monte pares fixos entre número, ano e objeto de cada resolução.
- **Referência à apostila de estudo:** Dia 4 — “3. Regimento Interno do CRA-PR e RN CFA nº 651/2024”.

### Comentário da Questão 6

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** A RN CFA nº 640/2024 foi sucedida e revogada na consolidação indicada no material.
- **B) está errada:** A RN CFA nº 649/2024 trata do Regulamento de Registro, não do Código de Ética.
- **C) está errada:** A RN CFA nº 651/2024 aprova o Regimento Interno do CRA-PR.
- **D) está correta:** A RN CFA nº 671/2025 aprova o Código de Ética e Disciplina vigente considerado no edital.
- **Conceito cobrado:** Norma vigente do Código de Ética.
- **Pegadinha usada:** Escolher norma anterior ou resolução de objeto diferente apenas pela proximidade numérica.
- **Como pensar para acertar:** Diferencie a norma vigente de eventual resolução anterior mencionada no histórico.
- **Referência à apostila de estudo:** Dia 4 — “4. Código de Ética — RN CFA nº 671/2025”.

### Comentário da Questão 7

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** O sigilo não é absoluto diante de justa causa ou obrigação legal legitimamente configurada.
- **B) está correta:** A regra é preservar a informação, com exame das exceções justificadas previstas no ordenamento.
- **C) está errada:** A inexistência aparente de dano econômico não torna a confidencialidade facultativa.
- **D) está errada:** Dever genérico de confidencialidade de terceiros não autoriza compartilhamento sem necessidade e fundamento.
- **Conceito cobrado:** Dever de sigilo e suas exceções.
- **Pegadinha usada:** Oscilar entre sigilo absoluto e divulgação livre por conveniência.
- **Como pensar para acertar:** Comece pela preservação do sigilo e só depois verifique justa causa ou hipótese legal concreta.
- **Referência à apostila de estudo:** Dia 4 — “Código de Ética: sigilo, zelo, independência e uso do registro”.

### Comentário da Questão 8

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Registro ativo não neutraliza deveres de colaboração nem sana comportamento obstrutivo.
- **B) está errada:** O direito de defesa não equivale a autorização para recusa geral e imotivada a diligência regular.
- **C) está errada:** O Código alcança pessoas físicas e jurídicas, observadas as especificidades aplicáveis.
- **D) está correta:** Ocultar documentos pertinentes e criar obstáculos deliberados pode caracterizar obstrução à fiscalização.
- **Conceito cobrado:** Obstrução à fiscalização por pessoa jurídica.
- **Pegadinha usada:** Usar direito de defesa ou registro ativo como imunidade contra fiscalização regular.
- **Como pensar para acertar:** Separe contestação fundamentada de comportamento destinado a impedir a atividade fiscalizatória.
- **Referência à apostila de estudo:** Dia 4 — “Pessoa física, pessoa jurídica e responsabilidade técnica”.

### Comentário da Questão 9

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Contribuições e cobrança dos conselhos são tema central da Lei nº 12.514/2011, não objeto exclusivo da Lei nº 4.769/1965.
- **B) está errada:** O Regimento Interno atual do CRA-PR foi aprovado pela RN CFA nº 651/2024.
- **C) está correta:** A Lei nº 4.769/1965 é a base legal do exercício profissional de Administração e da organização CFA/CRAs.
- **D) está errada:** A lei profissional não se limita à ética; ela estrutura o exercício da profissão e o sistema.
- **Conceito cobrado:** Função da Lei nº 4.769/1965.
- **Pegadinha usada:** Confundir lei profissional com normas financeiras, regimentais ou exclusivamente éticas.
- **Como pensar para acertar:** Associe a lei de 1965 à base da profissão; depois situe as normas especiais ao redor dela.
- **Referência à apostila de estudo:** Dia 4 — “1. Lei Federal nº 4.769/1965”.

### Comentário da Questão 10

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Decreto regulamentar não pode afastar a lei que lhe dá fundamento.
- **B) está correta:** A relação correta é de lei como base e decreto como regulamentação dentro dos limites legais.
- **C) está errada:** O Decreto nº 61.934/1967 regulamenta a lei profissional, não constitui regimento local autônomo.
- **D) está errada:** O decreto não tem como objeto exclusivo o processo eleitoral do sistema.
- **Conceito cobrado:** Relação entre lei e decreto regulamentar.
- **Pegadinha usada:** Supor que norma posterior e infralegal prevalece automaticamente sobre a lei.
- **Como pensar para acertar:** Em conflito, preserve a hierarquia: o decreto detalha a execução, mas não pode contrariar a lei.
- **Referência à apostila de estudo:** Dia 4 — “2. Decreto Federal nº 61.934/1967”.

### Comentário da Questão 11

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** O CRA-PR não possui atuação nacional nem perde sua autonomia administrativa pela articulação com o CFA.
- **B) está correta:** O Regimento o caracteriza como autarquia de direito público, autônoma e com jurisdição no Paraná.
- **C) está errada:** Não se trata de empresa pública estadual destinada a políticas de emprego.
- **D) está errada:** Conselho profissional não é associação privada facultativa; exerce funções públicas de registro e fiscalização.
- **Conceito cobrado:** Natureza jurídica e jurisdição do CRA-PR.
- **Pegadinha usada:** Confundir autarquia profissional com órgão subordinado, empresa estatal ou associação privada.
- **Como pensar para acertar:** Memorize o conjunto: direito público, autonomia própria e jurisdição estadual.
- **Referência à apostila de estudo:** Dia 4 — “3. Regimento Interno do CRA-PR e RN CFA nº 651/2024”.

### Comentário da Questão 12

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Os registrados não editam por votação direta a orientação normativa geral dos conselhos.
- **B) está errada:** O Plenário do CRA-PR é superior dentro do Conselho Regional, não em toda a federação.
- **C) está errada:** Os CRAs aplicam a disciplina do sistema, mas não substituem isoladamente a competência normativa nacional.
- **D) está correta:** A orientação normativa geral do sistema situa-se na esfera nacional do CFA.
- **Conceito cobrado:** Função normativa nacional do CFA.
- **Pegadinha usada:** Confundir superioridade interna do Plenário regional com competência nacional.
- **Como pensar para acertar:** Observe a abrangência do comando: se destinado a todos os CRAs, a referência é o CFA.
- **Referência à apostila de estudo:** Dia 4 — “Competência do CFA x competência do CRA”.

### Comentário da Questão 13

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A RN CFA nº 649/2024 aprovou o Regulamento de Registro e a RN CFA nº 670/2025 o alterou.
- **B) está errada:** O regulamento eleitoral indicado no edital está na RN CFA nº 680/2025.
- **C) está errada:** Resoluções administrativas não substituem nem revogam integralmente a lei federal profissional.
- **D) está errada:** O Código de Ética vigente está na RN CFA nº 671/2025.
- **Conceito cobrado:** Regulamento de Registro e norma alteradora.
- **Pegadinha usada:** Ler a resolução alteradora isoladamente ou trocar seu objeto com ética e eleições.
- **Como pensar para acertar:** Estude a norma-base e a norma alteradora como um conjunto, preservando a hierarquia.
- **Referência à apostila de estudo:** Dia 4 — “Normas do edital: função de cada uma”.

### Comentário da Questão 14

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** O Regimento Interno do CRA-PR está associado à RN CFA nº 651/2024.
- **B) está errada:** As eleições do sistema são objeto da RN CFA nº 680/2025.
- **C) está correta:** A RN CFA nº 589/2020 está vinculada à fiscalização no Sistema CFA/CRAs.
- **D) está errada:** O Código de Ética vigente está associado à RN CFA nº 671/2025.
- **Conceito cobrado:** Objeto da RN CFA nº 589/2020.
- **Pegadinha usada:** Permutar objetos entre resoluções listadas no mesmo edital.
- **Como pensar para acertar:** Fixe a associação ‘589/2020 — fiscalização’ sem inventar detalhes não consolidados.
- **Referência à apostila de estudo:** Dia 4 — “Normas do edital: função de cada uma”.

### Comentário da Questão 15

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** O funcionamento interno do CRA-PR é disciplinado por seu Regimento, aprovado pela RN CFA nº 651/2024.
- **B) está errada:** O Regulamento de Registro foi aprovado pela RN CFA nº 649/2024.
- **C) está correta:** A ementa da RN CFA nº 626/2023 a relaciona ao Programa Especial de Recuperação de Créditos — PERC.
- **D) está errada:** O Código de Ética vigente foi aprovado pela RN CFA nº 671/2025.
- **Conceito cobrado:** Objeto da RN CFA nº 626/2023.
- **Pegadinha usada:** Confundir recuperação de créditos com registro, ética ou regimento.
- **Como pensar para acertar:** Associe a sigla PERC a recuperação de créditos e ao número 626/2023.
- **Referência à apostila de estudo:** Dia 4 — “Normas do edital: função de cada uma”.

### Comentário da Questão 16

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** O Código de Ética vigente foi aprovado pela RN CFA nº 671/2025.
- **B) está errada:** O PERC está associado à RN CFA nº 626/2023.
- **C) está errada:** A alteração do Regulamento de Registro é objeto da RN CFA nº 670/2025.
- **D) está correta:** A RN CFA nº 546/2018 trata da concessão de isenção de débitos pelos CRAs.
- **Conceito cobrado:** Objeto da RN CFA nº 546/2018.
- **Pegadinha usada:** Aproximar indevidamente ‘isenção de débitos’ e ‘recuperação de créditos’.
- **Como pensar para acertar:** Diferencie benefício de isenção, ligado à RN 546, do programa de recuperação, ligado à RN 626.
- **Referência à apostila de estudo:** Dia 4 — “Normas do edital: função de cada uma”.

### Comentário da Questão 17

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A Lei nº 12.514/2011 disciplina contribuições devidas a conselhos profissionais e aspectos de cobrança.
- **B) está errada:** Os campos da profissão decorrem da legislação profissional iniciada pela Lei nº 4.769/1965.
- **C) está errada:** A estrutura interna do CRA-PR está em seu Regimento, aprovado pela RN CFA nº 651/2024.
- **D) está errada:** Deveres éticos e sigilo são disciplinados pelo Código de Ética, não constituem o objeto principal da Lei nº 12.514/2011.
- **Conceito cobrado:** Contribuições aos conselhos profissionais.
- **Pegadinha usada:** Trocar o objeto financeiro da Lei nº 12.514/2011 por ética, profissão ou regimento.
- **Como pensar para acertar:** Associe ‘12.514’ a anuidades, contribuições, taxas e cobrança dos conselhos.
- **Referência à apostila de estudo:** Dia 4 — “Lei nº 12.514/2011 — contribuições e cobrança”.

### Comentário da Questão 18

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Há especificidades de destinatário e de sanção; não se pode aplicar tudo de modo idêntico a PF e PJ.
- **B) está errada:** A comprovação da conduta não dispensa o enquadramento normativo nem a análise da gravidade e das circunstâncias.
- **C) está correta:** A resposta exige norma aplicável, gravidade e distinções entre pessoa física e jurídica.
- **D) está errada:** A responsabilização ética-profissional não depende exclusivamente de condenação criminal judicial.
- **Conceito cobrado:** Individualização de sanções éticas.
- **Pegadinha usada:** Aplicar automaticamente a sanção máxima ou igualar pessoa física e jurídica.
- **Como pensar para acertar:** Primeiro enquadre a conduta; depois verifique destinatário, circunstâncias e sanções admitidas.
- **Referência à apostila de estudo:** Dia 4 — “Sanções: como estudar sem inventar prazo ou penalidade”.

### Comentário da Questão 19

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Autorização do autor material não cria participação técnica do profissional que assina.
- **B) está errada:** O registro da empresa não substitui a responsabilidade efetiva de quem subscreve o documento técnico.
- **C) está errada:** Prejuízo econômico concreto não é condição necessária para reconhecer o desvalor ético da assinatura fictícia.
- **D) está correta:** Assinar sem orientar, supervisionar ou participar pode configurar infração, pois atribui responsabilidade sem atuação real.
- **Conceito cobrado:** Assinatura técnica sem participação efetiva.
- **Pegadinha usada:** Confundir autorização formal ou registro da empresa com supervisão real.
- **Como pensar para acertar:** Compare a responsabilidade declarada pela assinatura com a atuação efetivamente realizada.
- **Referência à apostila de estudo:** Dia 4 — “Código de Ética: sigilo, zelo, independência e uso do registro”.

### Comentário da Questão 20

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** A afirmação descreve corretamente a origem funcional do dever de sigilo.
- **B) está correta:** Interesse comercial não é justa causa automática e não autoriza divulgar informação confidencial.
- **C) está errada:** Preservar sigilo não impede o cumprimento de obrigação legal ou colaboração com fiscalização legítima.
- **D) está errada:** O material admite análise de justa causa e das hipóteses legais pertinentes.
- **Conceito cobrado:** Limites do sigilo profissional.
- **Pegadinha usada:** Transformar conveniência econômica em exceção legítima ao sigilo.
- **Como pensar para acertar:** Nos itens ‘incorreta’, marque a opção que converte interesse privado em autorização geral de divulgação.
- **Referência à apostila de estudo:** Dia 4 — “Código de Ética: sigilo, zelo, independência e uso do registro”.

### Comentário da Questão 21

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Os objetos foram invertidos: RN 651 é Regimento e RN 671 é Código de Ética.
- **B) está errada:** A RN 649 trata de registro; a RN 680, de eleições.
- **C) está errada:** A RN 589 trata de fiscalização; a RN 626, do PERC.
- **D) está correta:** As duas associações correspondem ao mapa normativo confirmado no material.
- **Conceito cobrado:** Associação entre resoluções e objetos.
- **Pegadinha usada:** Inverter pares verdadeiros ou reunir dois números corretos com objetos trocados.
- **Como pensar para acertar:** Cheque separadamente cada metade da alternativa; ambas precisam estar corretas.
- **Referência à apostila de estudo:** Dia 4 — “Normas do edital: função de cada uma”.

### Comentário da Questão 22

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** A sujeição da pessoa jurídica decorre da atividade, não da profissão de todos os sócios.
- **B) está errada:** A responsabilidade técnica não substitui automaticamente eventual dever de registro da própria empresa.
- **C) está errada:** CNPJ e contrato social não criam imunidade perante a regulação profissional.
- **D) está correta:** A atividade básica pode atrair registro e fiscalização, com observância também da responsabilidade técnica.
- **Conceito cobrado:** Registro de pessoa jurídica e responsabilidade técnica.
- **Pegadinha usada:** Tratar registro da empresa e indicação de responsável como obrigações mutuamente excludentes.
- **Como pensar para acertar:** Analise em camadas: atividade da pessoa jurídica, registro aplicável e atuação efetiva do responsável.
- **Referência à apostila de estudo:** Dia 4 — “Pessoa física, pessoa jurídica e responsabilidade técnica”.

### Comentário da Questão 23

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A sede fica na capital, mas a jurisdição não se limita ao município.
- **B) está correta:** O Regimento atribui ao CRA-PR jurisdição em todo o Estado do Paraná.
- **C) está errada:** A jurisdição não abrange automaticamente Santa Catarina e Rio Grande do Sul.
- **D) está errada:** O CRA-PR não possui jurisdição nacional.
- **Conceito cobrado:** Sede e jurisdição territorial do CRA-PR.
- **Pegadinha usada:** Confundir o local da sede administrativa com o limite territorial da competência.
- **Como pensar para acertar:** Leia as duas informações separadamente: sede na capital; jurisdição em todo o estado.
- **Referência à apostila de estudo:** Dia 4 — “3. Regimento Interno do CRA-PR e RN CFA nº 651/2024”.

### Comentário da Questão 24

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Conselho e sindicato têm natureza e finalidade distintas: fiscalização pública de um lado, representação da categoria de outro.
- **B) está errada:** A alternativa inverte as funções típicas das duas entidades.
- **C) está errada:** Sindicato não é autarquia, e a diferença não é apenas territorial.
- **D) está errada:** Não há relação de unidade administrativa ou subordinação necessária entre sindicato e conselho.
- **Conceito cobrado:** Distinção entre conselho profissional e sindicato.
- **Pegadinha usada:** Atribuir ao conselho defesa corporativa ou ao sindicato poder de polícia profissional.
- **Como pensar para acertar:** Pergunte se a função descrita protege a sociedade pela fiscalização ou representa interesses trabalhistas da categoria.
- **Referência à apostila de estudo:** Dia 4 — “Natureza e finalidade do Sistema CFA/CRAs”.

### Comentário da Questão 25

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** A RN 546/2018 trata de isenção de débitos.
- **B) está errada:** A RN 589/2020 está associada à fiscalização.
- **C) está correta:** A RN 680/2025 aprova o Regulamento das Eleições do Sistema CFA/CRAs.
- **D) está errada:** A RN 651/2024 aprova o Regimento Interno do CRA-PR.
- **Conceito cobrado:** Objeto da RN CFA nº 680/2025.
- **Pegadinha usada:** Confundir eleições com regimento ou fiscalização por proximidade no edital.
- **Como pensar para acertar:** Fixe o par ‘680/2025 — eleições’ e descarte as resoluções com objeto já conhecido.
- **Referência à apostila de estudo:** Dia 4 — “Normas do edital: função de cada uma”.

### Comentário da Questão 26

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Analogia não autoriza inventar prazo ou requisito para uma resolução específica.
- **B) está errada:** Resoluções do mesmo órgão podem ter objetos e procedimentos muito diferentes.
- **C) está errada:** Lei próxima em tema não substitui resolução expressamente indicada com objeto próprio.
- **D) está correta:** A conclusão deve ficar no alcance da fonte confirmada até consulta ao texto oficial integral.
- **Conceito cobrado:** Rigor metodológico no uso de fontes normativas.
- **Pegadinha usada:** Preencher lacunas da fonte com memória, analogia ou padrão de outro conselho.
- **Como pensar para acertar:** Diferencie o que a ementa confirma do que exigiria leitura do artigo correspondente.
- **Referência à apostila de estudo:** Dia 4 — “Sanções: como estudar sem inventar prazo ou penalidade”.

### Comentário da Questão 27

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Direito de defesa não legitima ofensa pessoal nem obstrução deliberada de diligência regular.
- **B) está errada:** A fiscalização profissional é função institucional do CRA, e o caso não se reduz a contrato privado.
- **C) está correta:** As condutas podem afetar urbanidade e fiscalização, mas sua apuração deve respeitar o devido processo.
- **D) está errada:** A simples resistência não anula automaticamente a diligência; é necessário examinar a regularidade concreta.
- **Conceito cobrado:** Urbanidade, fiscalização e devido processo.
- **Pegadinha usada:** Usar garantias de defesa como salvo-conduto para qualquer comportamento.
- **Como pensar para acertar:** Separe contestação legítima de ofensa e de ato material destinado a impedir a fiscalização.
- **Referência à apostila de estudo:** Dia 4 — “Infrações recorrentes no Código de Ética”.

### Comentário da Questão 28

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** A validade da alteração não depende, como regra geral do enunciado, de republicação integral pela União.
- **B) está errada:** A resolução alteradora pode não reproduzir os dispositivos que permaneceram vigentes.
- **C) está correta:** A disciplina vigente resulta da norma-base combinada com as modificações expressamente produzidas pela norma posterior.
- **D) está errada:** Alteração pontual não equivale a revogação total do regulamento anterior.
- **Conceito cobrado:** Leitura de norma-base e norma alteradora.
- **Pegadinha usada:** Adotar automaticamente revogação total ou ler apenas um dos diplomas.
- **Como pensar para acertar:** Identifique quais dispositivos foram alterados e preserve os demais até prova de revogação.
- **Referência à apostila de estudo:** Dia 4 — “RN CFA nº 649/2024 e RN CFA nº 670/2025”.

### Comentário da Questão 29

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** O Plenário é o órgão deliberativo superior na estrutura regimental.
- **B) está errada:** A Ouvidoria recebe e trata manifestações, sem assumir a posição do Plenário.
- **C) está errada:** Representação institucional não equivale a órgão deliberativo superior.
- **D) está errada:** A Diretoria Executiva cumpre funções de execução e administração, não substitui o órgão deliberativo superior.
- **Conceito cobrado:** Estrutura interna do CRA-PR.
- **Pegadinha usada:** Confundir órgão executivo, canal de ouvidoria ou representação com instância deliberativa superior.
- **Como pensar para acertar:** Associe ‘deliberativo superior’ ao Plenário e ‘execução/administração’ à Diretoria.
- **Referência à apostila de estudo:** Dia 4 — “Estrutura interna do CRA-PR”.

### Comentário da Questão 30

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A Diretoria Executiva se relaciona à execução e à administração das atividades e deliberações.
- **B) está errada:** A Ouvidoria possui finalidade própria de interlocução e tratamento de manifestações.
- **C) está errada:** A deliberação superior compete ao Plenário.
- **D) está errada:** Normas nacionais para todo o sistema situam-se na esfera do CFA, não da Diretoria regional.
- **Conceito cobrado:** Função da Diretoria Executiva.
- **Pegadinha usada:** Inverter as funções do Plenário, da Diretoria e da Ouvidoria.
- **Como pensar para acertar:** Observe o verbo nuclear: deliberar remete ao Plenário; executar e administrar, à Diretoria.
- **Referência à apostila de estudo:** Dia 4 — “Estrutura interna do CRA-PR”.

### Comentário da Questão 31

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** O Código não se restringe ao profissional liberal quando a pessoa atua no campo da profissão.
- **B) está errada:** Regime funcional e responsabilidade profissional podem coexistir; um não elimina automaticamente o outro.
- **C) está correta:** O vínculo público não afasta deveres éticos inerentes à atuação profissional sujeita ao sistema.
- **D) está errada:** A incidência ética não depende de remuneração privada paralela.
- **Conceito cobrado:** Incidência ética no exercício funcional.
- **Pegadinha usada:** Confundir vínculo estatutário com imunidade perante deveres da profissão.
- **Como pensar para acertar:** Olhe para a natureza da atividade exercida, não apenas para a forma do vínculo de trabalho.
- **Referência à apostila de estudo:** Dia 4 — “Abrangência do Código de Ética”.

### Comentário da Questão 32

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** RN 589 e RN 671 tratam de fiscalização e ética.
- **B) está errada:** Lei 12.514 e RN 626 tratam de contribuições e recuperação de créditos, não formam o par profissão/regulamentação.
- **C) está errada:** RN 651 e RN 680 tratam, respectivamente, de regimento e eleições.
- **D) está correta:** A Lei 4.769/1965 fornece a base e o Decreto 61.934/1967 a regulamenta.
- **Conceito cobrado:** Base legal e regulamentar da profissão.
- **Pegadinha usada:** Formar pares apenas porque as duas normas constam do edital.
- **Como pensar para acertar:** Procure a relação hierárquica direta: lei profissional seguida de seu decreto regulamentador.
- **Referência à apostila de estudo:** Dia 4 — “Lei nº 4.769/1965 e Decreto nº 61.934/1967”.

### Comentário da Questão 33

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** A abrangência inclui PF e PJ, com adaptações e especificidades.
- **B) está errada:** O sigilo deve ser conjugado com justa causa e hipóteses legais.
- **C) está correta:** Ordem escrita do cliente não elimina independência técnica nem torna lícita uma conduta inadequada.
- **D) está errada:** Atualização cadastral e aperfeiçoamento integram os deveres destacados no material.
- **Conceito cobrado:** Deveres éticos e independência técnica.
- **Pegadinha usada:** Supor que ordem contratual escrita afasta responsabilidade pessoal do profissional.
- **Como pensar para acertar:** Nos itens ‘incorreta’, desconfie de permissões absolutas criadas pela vontade do cliente.
- **Referência à apostila de estudo:** Dia 4 — “Código de Ética: sigilo, zelo, independência e uso do registro”.

### Comentário da Questão 34

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Atualização cadastral não substitui procedimentos de registro eventualmente exigidos.
- **B) está correta:** Dados atualizados permitem notificação, controle e fiscalização regulares.
- **C) está errada:** A obrigação se cumpre perante o conselho competente; não transfere toda comunicação ao CFA.
- **D) está errada:** A correção cadastral não apaga nem sana automaticamente infrações anteriores.
- **Conceito cobrado:** Dever de atualização cadastral.
- **Pegadinha usada:** Transformar um dever instrumental em mecanismo de renovação, transferência de competência ou anistia.
- **Como pensar para acertar:** Pense na finalidade prática do cadastro: localizar, comunicar e controlar o vínculo profissional.
- **Referência à apostila de estudo:** Dia 4 — “Deveres profissionais no Código de Ética”.

### Comentário da Questão 35

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A defesa do cliente existe dentro de limites jurídicos, técnicos e éticos.
- **B) está correta:** Honestidade e independência técnica impedem omissão destinada a distorcer a conclusão profissional.
- **C) está errada:** Cláusula de confidencialidade não autoriza falsidade ou supressão tecnicamente indevida.
- **D) está errada:** Trocar o signatário não corrige a omissão e pode ampliar a irregularidade.
- **Conceito cobrado:** Independência técnica diante de pressão do cliente.
- **Pegadinha usada:** Tratar interesse contratual como superior à verdade técnica e à ética.
- **Como pensar para acertar:** Pergunte se a ordem preserva a integridade do parecer; se distorce o conteúdo, deve ser recusada.
- **Referência à apostila de estudo:** Dia 4 — “Código de Ética: sigilo, zelo, independência e uso do registro”.

### Comentário da Questão 36

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** O regulamento eleitoral está na RN 680/2025.
- **B) está errada:** O PERC está associado à RN 626/2023.
- **C) está errada:** O Regimento Interno do CRA-PR está na RN 651/2024.
- **D) está correta:** A RN 649/2024 aprova o Regulamento de Registro de PF e PJ no sistema.
- **Conceito cobrado:** Objeto da RN CFA nº 649/2024.
- **Pegadinha usada:** Trocar a norma de registro por resoluções de crédito, regimento ou eleição.
- **Como pensar para acertar:** No mapa normativo, leia ‘649’ como norma-base de registro e ‘670’ como sua alteração.
- **Referência à apostila de estudo:** Dia 4 — “RN CFA nº 649/2024 e RN CFA nº 670/2025”.

### Comentário da Questão 37

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A RN 670/2025 atua no plano infralegal, alterando regulamento aprovado por resolução anterior.
- **B) está errada:** Alteração do regulamento de registro não substitui integralmente o decreto regulamentar.
- **C) está errada:** Resolução tampouco altera automaticamente qualquer lei que trate da matéria.
- **D) está errada:** Resolução não possui força para revogar lei federal, ainda que posterior.
- **Conceito cobrado:** Hierarquia normativa e alcance da RN nº 670/2025.
- **Pegadinha usada:** Aplicar o critério cronológico sem considerar a hierarquia entre lei, decreto e resolução.
- **Como pensar para acertar:** Antes de comparar datas, identifique a espécie normativa e o objeto exato da alteração.
- **Referência à apostila de estudo:** Dia 4 — “Hierarquia e leitura conjunta das normas”.

### Comentário da Questão 38

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Registro, ética e regimento correspondem a outras resoluções do edital.
- **B) está correta:** A ordem correta é RN 589 — fiscalização; RN 626 — PERC; RN 680 — eleições.
- **C) está errada:** A sequência desloca eleições e registro para números incorretos.
- **D) está errada:** PERC está na RN 626, isenção na RN 546 e ética na RN 671.
- **Conceito cobrado:** Mapa de resoluções do edital.
- **Pegadinha usada:** Apresentar três temas verdadeiros, mas fora da ordem dos números dados.
- **Como pensar para acertar:** Resolva cada par de modo independente e só então valide a sequência completa.
- **Referência à apostila de estudo:** Dia 4 — “Normas do edital: função de cada uma”.

### Comentário da Questão 39

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** O fato ocorrido no Paraná insere-se, em regra, na jurisdição fiscalizatória do CRA-PR.
- **B) está errada:** A função nacional do CFA não elimina a atuação fiscalizatória regional.
- **C) está errada:** O Plenário do CFA não é instância inicial obrigatória de toda ocorrência municipal.
- **D) está errada:** O CRA exerce função pública de fiscalização profissional própria.
- **Conceito cobrado:** Competência territorial de fiscalização.
- **Pegadinha usada:** Confundir orientação nacional com execução direta de toda fiscalização local.
- **Como pensar para acertar:** Localize o fato e associe-o ao CRA da respectiva jurisdição.
- **Referência à apostila de estudo:** Dia 4 — “Competência do CFA x competência do CRA”.

### Comentário da Questão 40

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** O empregador pode apoiar a capacitação, mas isso não elimina o dever do profissional.
- **B) está correta:** Aperfeiçoamento é dever ligado à competência, ao zelo e à qualidade responsável.
- **C) está errada:** O Código trata atualização como relevante para a atuação responsável, não como faculdade desconectada.
- **D) está errada:** O profissional não transfere integralmente a terceiro seu dever pessoal de qualificação.
- **Conceito cobrado:** Aperfeiçoamento e atualização profissional.
- **Pegadinha usada:** Externalizar o dever ao empregador ou tratá-lo como opção sem efeito ético.
- **Como pensar para acertar:** Relacione atualização contínua com a qualidade e a responsabilidade dos serviços prestados.
- **Referência à apostila de estudo:** Dia 4 — “Deveres profissionais no Código de Ética”.

### Comentário da Questão 41

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** Interesse econômico e ausência de ordem judicial não autorizam apresentar conclusão tecnicamente incompleta.
- **B) está errada:** Guardar a ressalva internamente não corrige a informação material omitida do parecer entregue ao destinatário.
- **C) está correta:** O profissional deve recusar a distorção, explicitar a limitação e conciliar lealdade legítima com independência, técnica, ética e legalidade.
- **D) está errada:** A divergência exige posicionamento técnico e registro adequado, mas não determina, por si só, encerramento automático e sem esclarecimento.
- **Conceito cobrado:** Lealdade ao cliente, independência técnica e integridade do parecer.
- **Pegadinha usada:** Tratar defesa do interesse confiado como autorização para omitir dado material ou como dever automático de romper o contrato.
- **Como pensar para acertar:** Verifique se a conduta preserva simultaneamente completude técnica, limites normativos e defesa apenas de interesses legítimos.
- **Referência à apostila de estudo:** Dia 4 — “Deveres profissionais no Código de Ética”.

### Comentário da Questão 42

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** É possível reconhecer o enquadramento em tese sem inventar penalidade que depende de norma e circunstâncias não fornecidas.
- **B) está errada:** A sanção máxima não decorre automaticamente do reconhecimento genérico de infração.
- **C) está errada:** Norma de outro conselho não fornece automaticamente a pena aplicável ao Sistema CFA/CRAs.
- **D) está errada:** A apuração ético-profissional possui autonomia e não exige sempre condenação judicial.
- **Conceito cobrado:** Rigor na determinação de sanções.
- **Pegadinha usada:** Forçar uma pena específica quando o enunciado não traz elementos suficientes.
- **Como pensar para acertar:** Responda apenas até onde vão a fonte e os fatos; não complete a lacuna com analogia.
- **Referência à apostila de estudo:** Dia 4 — “Sanções: como estudar sem inventar prazo ou penalidade”.

### Comentário da Questão 43

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** O material registra especificidades de sanção, portanto a aplicação não é idêntica a PF e PJ.
- **B) está errada:** A submissão decorre da regulação profissional, não de adesão ética facultativa.
- **C) está errada:** A composição societária não condiciona, nesses termos, a incidência ética sobre a pessoa jurídica registrada.
- **D) está correta:** O Código alcança pessoas jurídicas; suspensão e cancelamento não se aplicam a elas segundo a consolidação estudada.
- **Conceito cobrado:** Aplicação do Código de Ética à pessoa jurídica.
- **Pegadinha usada:** Generalizar sanções de pessoa física ou criar condições societárias inexistentes.
- **Como pensar para acertar:** Separe duas perguntas: o Código alcança a PJ? Sim. Todas as sanções de PF se aplicam? Não.
- **Referência à apostila de estudo:** Dia 4 — “Pessoa física, pessoa jurídica e responsabilidade técnica”.

### Comentário da Questão 44

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **Observação:** a questão pede o procedimento que compromete a rastreabilidade; portanto, o gabarito é a prática inadequada.
- **A) está errada:** Conferir metadados e alterações no repositório oficial é justamente o controle necessário para identificar a versão vigente.
- **B) está errada:** O edital delimita o objeto, e o texto oficial completo resolve dúvidas que a ementa, sozinha, não esclarece.
- **C) está errada:** Informar a natureza autoral e separar a fonte normativa evita atribuição falsa de proveniência.
- **D) está correta:** Estilo semelhante não prova origem oficial, e a data de material preparatório não substitui validação de vigência e autenticidade.
- **Conceito cobrado:** Proveniência, vigência normativa e rotulagem de questões autorais.
- **Pegadinha usada:** Confundir aparência de autenticidade ou data recente de apostila com evidência documental verificável.
- **Como pensar para acertar:** Separe duas verificações: autenticidade da questão e vigência da norma; ambas exigem fonte identificável.
- **Referência à apostila de estudo:** Dia 4 — “Método de estudo e controle de fontes”.

### Comentário da Questão 45

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** A fiscalização não se limita a proteger mercado ou renda dos inscritos e não pode ignorar risco social relevante.
- **B) está correta:** A priorização por risco, dentro da competência e com devido processo, vincula orientação, registro e fiscalização à proteção da sociedade.
- **C) está errada:** A finalidade pública não amplia a competência legal do Conselho para substituir indiscriminadamente outros órgãos.
- **D) está errada:** Receita sustenta a atividade institucional, mas não substitui critérios de risco, competência e interesse público.
- **Conceito cobrado:** Finalidade pública, planejamento por risco e limites da competência fiscalizatória.
- **Pegadinha usada:** Usar arrecadação ou proteção corporativa como critério autônomo de prioridade e confundir finalidade com expansão de competência.
- **Como pensar para acertar:** Relacione a medida ao risco para a sociedade, confirme a competência e só então verifique procedimento e instrumentos cabíveis.
- **Referência à apostila de estudo:** Dia 4 — “Natureza e finalidade do Sistema CFA/CRAs”.

### Comentário da Questão 46

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** Empréstimo de nome ou registro e responsabilidade técnica meramente formal podem configurar irregularidade.
- **B) está errada:** A indicação fictícia alcança responsabilidade e ética profissional, não apenas o contrato.
- **C) está errada:** Documento formal não comprova sozinho supervisão ou orientação efetivas.
- **D) está errada:** Registro da pessoa jurídica não elimina deveres individuais de quem assume responsabilidade técnica.
- **Conceito cobrado:** Responsabilidade técnica efetiva.
- **Pegadinha usada:** Confundir nomeação documental com participação profissional real.
- **Como pensar para acertar:** Compare o que o responsável declarou assumir com os atos que efetivamente praticou.
- **Referência à apostila de estudo:** Dia 4 — “Pessoa física, pessoa jurídica e responsabilidade técnica”.

### Comentário da Questão 47

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** Jurisdição estadual delimita a atuação regional, mas não confere poder para afastar regra nacional válida do sistema.
- **B) está correta:** O ato regional deve ser revisto para compatibilizar a execução local, sem impedir que a discordância seja levada ao canal institucional próprio.
- **C) está errada:** A posterioridade não produz revogação quando o órgão regional carece de competência para substituir a norma nacional.
- **D) está errada:** A Diretoria de um CRA não recebe competência para alterar regra nacional aplicável aos demais Conselhos.
- **Conceito cobrado:** Distribuição funcional de competências, norma nacional e execução fiscalizatória regional.
- **Pegadinha usada:** Confundir autonomia administrativa, cronologia e hierarquia funcional com competência normativa nacional.
- **Como pensar para acertar:** Identifique quem editou cada ato, seu alcance territorial e qual órgão possui competência para resolver o conflito.
- **Referência à apostila de estudo:** Dia 4 — “Competência do CFA x competência do CRA”.

### Comentário da Questão 48

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** Unidade descentralizada não adquire jurisdição ou personalidade autônoma apenas por funcionar fora da sede.
- **B) está errada:** A fiscalização estadual não depende da criação de Conselho municipal em cada localidade atendida.
- **C) está correta:** Curitiba continua sendo a sede, a jurisdição permanece estadual e o atendimento descentralizado integra o mesmo CRA-PR.
- **D) está errada:** Descentralizar atendimento dentro do Estado não amplia a competência do Conselho para o território nacional.
- **Conceito cobrado:** Sede, jurisdição territorial e descentralização administrativa.
- **Pegadinha usada:** Confundir unidade de atendimento com novo ente autônomo ou extensão territorial de competência.
- **Como pensar para acertar:** Analise separadamente endereço da sede, alcance jurídico da atuação e natureza organizacional da unidade local.
- **Referência à apostila de estudo:** Dia 4 — “3. Regimento Interno do CRA-PR e RN CFA nº 651/2024”.

### Comentário da Questão 49

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** Lucro não é requisito necessário para caracterizar auxílio ao exercício não habilitado.
- **B) está errada:** A responsabilização ética não depende obrigatoriamente de condenação penal prévia do terceiro.
- **C) está correta:** Auxiliar pessoa não habilitada a exercer atividade profissional pode configurar infração por si só.
- **D) está errada:** Registro pessoal não pode ser transferido informalmente a quem não possui habilitação.
- **Conceito cobrado:** Auxílio ao exercício profissional por não habilitado.
- **Pegadinha usada:** Acrescentar lucro, dano ou condenação penal como requisitos indispensáveis.
- **Como pensar para acertar:** Observe o núcleo da conduta: facilitar exercício reservado por quem não tem habilitação.
- **Referência à apostila de estudo:** Dia 4 — “Infrações recorrentes no Código de Ética”.

### Comentário da Questão 50

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** Especialidade e data da resolução não lhe permitem afastar requisito estabelecido por lei.
- **B) está correta:** Decreto e resolução são interpretados dentro da base legal, sem criar contradição nem dispensar requisito reservado à lei.
- **C) está errada:** Um decreto regulamentar posterior não modifica a lei apenas por critério cronológico.
- **D) está errada:** A solução do conflito normativo não depende da livre escolha da regra mais favorável, mas de hierarquia e competência.
- **Conceito cobrado:** Hierarquia normativa, poder regulamentar e limites das resoluções administrativas.
- **Pegadinha usada:** Aplicar isoladamente cronologia, especialidade ou favorabilidade e ignorar a relação de subordinação à lei.
- **Como pensar para acertar:** Ordene os atos por hierarquia e competência antes de usar critérios de interpretação entre normas do mesmo nível.
- **Referência à apostila de estudo:** Dia 4 — “Lei nº 4.769/1965 e Decreto nº 61.934/1967”.

### Comentários das questões extras de revisão fixa do Dia 4

#### Comentário Extra Dia 4.1

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Pregão destina-se a bens e serviços comuns, não à seleção descrita.
- **B) está errada:** Leilão é modalidade ligada à alienação de bens, não ao prêmio por trabalho técnico ou artístico.
- **C) está correta:** Concurso é a modalidade definida para escolha de trabalho técnico, científico ou artístico mediante prêmio ou remuneração.
- **D) está errada:** Concorrência não substitui obrigatoriamente o concurso nessa hipótese específica.
- **Conceito cobrado:** Modalidade concurso na Lei nº 14.133/2021.
- **Pegadinha usada:** Confundir concurso público de pessoal com concurso enquanto modalidade licitatória.
- **Como pensar para acertar:** Associe ‘trabalho técnico/científico/artístico + prêmio’ diretamente a concurso.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.2

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** Conduta, dano e nexo formam o núcleo da análise, sem excluir causas de ruptura ou redução do nexo.
- **B) está errada:** Dano isolado não basta; é necessário ligá-lo a uma conduta estatal.
- **C) está errada:** Dolo do agente e condenação penal não são requisitos gerais da responsabilidade objetiva estatal.
- **D) está errada:** O regime objetivo não exige, como regra, prova de culpa administrativa nesses termos.
- **Conceito cobrado:** Elementos da responsabilidade civil objetiva do Estado.
- **Pegadinha usada:** Confundir responsabilidade objetiva com responsabilidade automática.
- **Como pensar para acertar:** Sempre percorra conduta, dano, nexo e possíveis excludentes ou atenuantes.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.3

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** A presença de dado pessoal não torna automaticamente sigiloso todo o conteúdo que possa ser separado.
- **B) está errada:** Publicidade não é autorização para expor irrestritamente dados pessoais sem fundamento.
- **C) está errada:** Publicidade institucional não deve ser usada como instrumento de promoção pessoal da autoridade.
- **D) está correta:** A solução preserva o acesso ao conteúdo público e restringe somente os dados cuja divulgação não esteja autorizada.
- **Conceito cobrado:** Publicidade administrativa e proteção de dados pessoais.
- **Pegadinha usada:** Tratar transparência e proteção de dados como escolhas absolutas e incompatíveis.
- **Como pensar para acertar:** Separe a informação de interesse público dos dados pessoais e fundamente qualquer restrição.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Mesmo no regime objetivo, a causalidade da vítima pode influir no valor devido.
- **B) está errada:** A concorrência não rompe sempre e integralmente o nexo; isso depende de sua intensidade.
- **C) está correta:** A participação causal da vítima pode justificar redução proporcional da reparação.
- **D) está errada:** A responsabilidade não é automaticamente transferida ao agente público.
- **Conceito cobrado:** Culpa concorrente da vítima.
- **Pegadinha usada:** Confundir contribuição parcial com causa exclusiva.
- **Como pensar para acertar:** Avalie se a vítima apenas concorreu ou foi a causa exclusiva do resultado.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.5

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A ruptura efetiva do nexo por caso fortuito ou força maior pode afastar o dever de indenizar.
- **B) está errada:** Ocorrência em bem público não basta para responsabilização automática.
- **C) está errada:** A força maior não atua somente como redutor; pode excluir a responsabilidade se romper o nexo.
- **D) está errada:** A objetividade do regime não elimina a necessidade de nexo causal.
- **Conceito cobrado:** Excludentes do nexo causal.
- **Pegadinha usada:** Entender responsabilidade objetiva como obrigação de indenizar qualquer evento.
- **Como pensar para acertar:** Verifique se o evento externo rompeu a ligação causal entre atuação estatal e dano.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.6

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Fórmula genérica de conveniência não demonstra quais fatos e normas sustentam o indeferimento.
- **B) está correta:** Motivar é tornar explícitos os pressupostos fáticos e jurídicos usados para chegar à decisão.
- **C) está errada:** Resultado desfavorável não elimina o dever de apresentar justificativa quando ela é exigível.
- **D) está errada:** A motivação deve acompanhar a decisão e permitir compreensão e controle, não surgir apenas depois de recurso.
- **Conceito cobrado:** Motivação objetiva do ato administrativo.
- **Pegadinha usada:** Confundir a simples presença de uma frase justificativa com exposição verificável dos fundamentos.
- **Como pensar para acertar:** Pergunte quais fatos ocorreram, qual regra se aplica e como ambos conduzem ao resultado.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.7

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Legalidade formal não basta quando a conduta é desleal ou ímproba.
- **B) está errada:** Moralidade administrativa não é a preferência moral privada de cada agente.
- **C) está errada:** Eficiência convive com os demais princípios e não legitima seu sacrifício.
- **D) está correta:** A exigência envolve ética institucional, lealdade e probidade.
- **Conceito cobrado:** Princípio da moralidade administrativa.
- **Pegadinha usada:** Reduzir moralidade à lei formal ou à moral pessoal do agente.
- **Como pensar para acertar:** Pense em padrões objetivos de honestidade, lealdade e boa administração.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.8

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Resultado material não se confunde com motivação.
- **B) está correta:** Motivação é a exteriorização das razões de fato e de direito da decisão.
- **C) está errada:** Competência identifica quem pode praticar o ato, não por que ele foi praticado.
- **D) está errada:** Atos discricionários não são, por isso, sempre dispensados de motivação.
- **Conceito cobrado:** Motivo e motivação do ato administrativo.
- **Pegadinha usada:** Trocar a razão do ato, sua exposição, sua competência e seu resultado.
- **Como pensar para acertar:** Use a distinção: motivo é o pressuposto; motivação é sua exposição no ato.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.9

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Publicidade do motivo não corrige o uso pessoal da competência.
- **B) está errada:** Eficiência não é o único princípio atingido, mesmo que haja resultado útil.
- **C) está errada:** A perseguição pessoal atinge diretamente a impessoalidade e pode configurar desvio de finalidade.
- **D) está correta:** Finalidade pública não pode ser usada como fachada para vingança pessoal; há ofensa à impessoalidade e à moralidade.
- **Conceito cobrado:** Impessoalidade, moralidade e desvio de finalidade.
- **Pegadinha usada:** Confundir competência formal para fiscalizar com legitimidade do propósito concreto.
- **Como pensar para acertar:** Pergunte se a finalidade real é pública ou pessoal, ainda que o ato pareça formalmente regular.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.10

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Os conceitos não se confundem nem se limitam à aparência documental do ato.
- **B) está errada:** Publicidade e competência são categorias distintas de motivo e motivação.
- **C) está correta:** O motivo corresponde aos pressupostos que autorizam o ato; a motivação registra e explica esses pressupostos.
- **D) está errada:** A distinção não depende da concordância do interessado, nem todo motivo é livremente escolhido.
- **Conceito cobrado:** Distinção entre motivo e motivação.
- **Pegadinha usada:** Trocar o fundamento do ato por sua exposição formal ou por outro elemento administrativo.
- **Como pensar para acertar:** Identifique primeiro os fatos e a regra; depois localize onde a autoridade os explica na decisão.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Administração Pública](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.11

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** A sequência de palavras não forma um parágrafo nem estabelece relação entre tese, razão e consequência.
- **B) está errada:** A afirmação genérica não desenvolve a ideia nem demonstra por que a ética produz determinado efeito.
- **C) está errada:** Exemplo pertinente pode concretizar o argumento; evitá-lo por regra empobrece o desenvolvimento.
- **D) está correta:** O trecho apresenta ideia central, explica sua razão e extrai consequência coerente para a confiança social.
- **Conceito cobrado:** Estrutura do parágrafo argumentativo.
- **Pegadinha usada:** Confundir enumeração de palavras ou generalidade com desenvolvimento de argumento.
- **Como pensar para acertar:** Procure tese do parágrafo, justificativa introduzida por relação lógica e consequência vinculada.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5).

#### Comentário Extra Dia 4.12

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** Em ‘àquela’, há fusão da preposição exigida com o demonstrativo.
- **B) está correta:** Antes de verbo no infinitivo não ocorre crase: o correto é ‘começou a revisar’.
- **C) está errada:** ‘Encaminhado à chefia’ admite preposição e artigo feminino.
- **D) está errada:** Na indicação de horário determinado, ‘às 14 horas’ está correto.
- **Conceito cobrado:** Emprego do acento indicativo de crase.
- **Pegadinha usada:** Marcar crase mecanicamente antes de palavra feminina e esquecer que ‘revisar’ é verbo.
- **Como pensar para acertar:** Teste a presença simultânea de preposição ‘a’ e artigo ou demonstrativo compatível.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5).

#### Comentário Extra Dia 4.13

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** ‘Porque’ introduz causa, não concessão.
- **B) está correta:** ‘Mesmo que’ preserva o valor concessivo de ‘ainda que’.
- **C) está errada:** ‘Para que’ introduz finalidade.
- **D) está errada:** ‘Logo que’ expressa valor temporal.
- **Conceito cobrado:** Conectivos concessivos.
- **Pegadinha usada:** Escolher locução gramaticalmente possível, mas com relação semântica diferente.
- **Como pensar para acertar:** Substitua o conector e verifique se permanece a ideia de obstáculo que não impede o resultado.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5).

#### Comentário Extra Dia 4.14

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A tese assume posição clara e delimita a relação entre resultado administrativo e limites jurídicos e éticos.
- **B) está errada:** O anúncio do tema não apresenta posição defensável nem critério para o desenvolvimento.
- **C) está errada:** A generalização causal absoluta não é demonstrada e reduz indevidamente o problema à tecnologia.
- **D) está errada:** Eficiência não legitima o afastamento de legalidade e deveres éticos.
- **Conceito cobrado:** Formulação de tese argumentativa.
- **Pegadinha usada:** Escolher frase temática ou afirmação absoluta no lugar de uma tese delimitada.
- **Como pensar para acertar:** Verifique se a frase contém posição, recorte e relações que possam orientar os argumentos seguintes.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5).

#### Comentário Extra Dia 4.15

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A conclusão retoma a compatibilização já defendida e indica consequência coerente, sem abrir frente nova.
- **B) está errada:** A alternativa introduz tema histórico não desenvolvido anteriormente.
- **C) está errada:** A conclusão contradiz a premissa de que publicidade admite restrições justificadas.
- **D) está errada:** O trecho cria oposição absoluta e abandona a solução de equilíbrio construída no desenvolvimento.
- **Conceito cobrado:** Conclusão argumentativa e retomada da tese.
- **Pegadinha usada:** Acrescentar assunto novo ou contradizer o argumento no fechamento.
- **Como pensar para acertar:** Retome a tese, sintetize o raciocínio e encerre sem inaugurar novo eixo temático.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5).

#### Comentário Extra Dia 4.16

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** 126 não preserva a proporcionalidade estabelecida.
- **B) está errada:** 108 corresponderia a 9 dias no mesmo ritmo.
- **C) está correta:** Mantido o ritmo, 72 ÷ 6 = 12 processos por dia; em 10 dias, 12 × 10 = 120.
- **D) está errada:** 144 corresponderia a 12 dias no ritmo calculado.
- **Conceito cobrado:** Proporcionalidade direta.
- **Pegadinha usada:** Multiplicar ou dividir pelos números do enunciado sem encontrar a taxa unitária.
- **Como pensar para acertar:** Calcule primeiro a produção diária e depois multiplique pelo novo número de dias.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.17

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** O valor 2 decorre de descontar indevidamente a interseção tripla mais de uma vez.
- **B) está errada:** O valor 8 resulta de ajuste incompleto das interseções no cálculo da união.
- **C) está correta:** A união é `58 + 50 + 42 − 28 − 24 − 20 + 12 = 90`; portanto, `100 − 90 = 10` não estudam nenhuma.
- **D) está errada:** O valor 22 confunde a interseção tripla com parcela adicional a ser retirada do complemento.
- **Conceito cobrado:** Inclusão-exclusão com três conjuntos e cálculo do complemento.
- **Pegadinha usada:** Subtrair as interseções aos pares sem devolver a interseção tripla, contada e retirada múltiplas vezes.
- **Como pensar para acertar:** Calcule a união com todos os sete termos da fórmula e só depois subtraia o resultado do total.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.18

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** A negação de ‘todo’ é ‘algum não’, e a negação da conjunção exige ‘ou’.
- **B) está correta:** Por De Morgan, nega-se cada parcela: algum fiscal não conferiu ou nenhum analista validou.
- **C) está errada:** ‘Todo fiscal não conferiu’ é mais forte que a negação correta de ‘todo fiscal conferiu’.
- **D) está errada:** A alternativa mantém afirmações positivas que não correspondem à negação das duas parcelas.
- **Conceito cobrado:** Negação de quantificadores e da conjunção.
- **Pegadinha usada:** Negar apenas os verbos sem trocar ‘e’ por ‘ou’ e sem inverter adequadamente os quantificadores.
- **Como pensar para acertar:** Aplique em duas etapas: De Morgan na conjunção e, depois, negue cada quantificador.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.19

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** O décimo termo é 48, a soma planejada é `10 × (12 + 48) ÷ 2 = 300` e 80% desse total corresponde a 240.
- **B) está errada:** 300 é o total da progressão antes da exclusão dos 20% de duplicidades.
- **C) está errada:** 220 não corresponde nem à soma da PA nem à aplicação de 80% sobre essa soma.
- **D) está errada:** 264 resulta de aplicar percentual ou base incompatível com o total planejado.
- **Conceito cobrado:** Soma de progressão aritmética e aplicação sucessiva de percentual.
- **Pegadinha usada:** Parar na soma da PA ou aplicar a exclusão percentual a um termo, e não ao total acumulado.
- **Como pensar para acertar:** Determine o último termo, calcule a soma dos dez termos e somente então retenha 80% do total.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4).

#### Comentário Extra Dia 4.20

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** `7/15` não resolve a composição exigida em três escolhas.
- **B) está errada:** `7/24` não contabiliza todas as escolhas possíveis para o único acesso bloqueado.
- **C) está errada:** `3/8` corresponde a uma razão parcial e não à seleção sem reposição de uma composição específica.
- **D) está correta:** Há `C(7,2) × C(3,1) = 63` amostras favoráveis entre `C(10,3) = 120`; logo, a probabilidade é `63/120 = 21/40`.
- **Conceito cobrado:** Probabilidade hipergeométrica e contagem de combinações sem reposição.
- **Pegadinha usada:** Fixar uma ordem para as categorias ou esquecer diferentes escolhas do item bloqueado.
- **Como pensar para acertar:** Conte escolhas favoráveis por categoria e divida pelo total de subconjuntos de três acessos.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 4 — Raciocínio Lógico-Matemático](semana_01_estudo.md#s1-d4-b4).


---

# Dia 5 — Língua Portuguesa e Discursiva

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões principais

### Questão 1
**Nível: Médio**

Leia o trecho: “A digitalização de serviços públicos amplia o acesso do cidadão, mas exige mecanismos de segurança para que a eficiência não comprometa direitos.” A ideia central é:

A) A digitalização pode ampliar o acesso, desde que acompanhada de segurança e respeito a direitos.
B) A segurança da informação constitui objetivo independente do acesso e da eficiência dos serviços.
C) A ampliação do acesso só é legítima quando todos os canais presenciais são eliminados.
D) A preservação de direitos necessariamente reduz a eficiência dos serviços digitalizados.

### Questão 2
**Nível: Médio**

No trecho “... mas exige mecanismos de segurança”, o conector “mas” estabelece relação de:

A) causa, pois justifica por que a digitalização amplia o acesso.
B) oposição com valor de ressalva, sem anular o benefício mencionado antes.
C) conclusão, pois apresenta uma consequência inevitável da ampliação do acesso.
D) condição, pois substitui a estrutura “desde que” sem alteração sintática.

### Questão 3
**Nível: Médio**

Leia: “Nem toda inovação tecnológica representa melhoria administrativa.” A inferência autorizada pelo enunciado é:

A) A maior parte das inovações tecnológicas não produz melhoria administrativa.
B) Existe ao menos uma inovação tecnológica que pode não representar melhoria administrativa.
C) Nenhuma inovação tecnológica representa melhoria administrativa.
D) Somente inovações desenvolvidas pela própria Administração produzem melhoria.

### Questão 4
**Nível: Médio**

Leia: “A transparência fortalece a confiança social, desde que respeite a proteção de dados pessoais.” Assinale a alternativa que extrapola o texto.

A) A transparência pode contribuir para fortalecer a confiança social.
B) A proteção de dados pessoais funciona como limite a ser observado.
C) A confiança social exige divulgação irrestrita de todo dado pessoal do órgão.
D) Transparência e proteção de dados podem ser compatibilizadas.

### Questão 5
**Nível: Médio**

A reescrita que preserva o sentido de “A revisão diária reduz o esquecimento e melhora a retenção do conteúdo” é:

A) Como melhora a retenção, a revisão diária aumenta o esquecimento do conteúdo.
B) O esquecimento é reduzido e a retenção do conteúdo é melhorada pela revisão diária.
C) A revisão diária reduz o conteúdo esquecido, embora prejudique sua retenção.
D) A revisão diária impede qualquer esquecimento e assegura retenção integral do conteúdo.

### Questão 6
**Nível: Médio**

Assinale a alternativa correta quanto à concordância verbal no padrão formal.

A) Existe, no cadastro, pendências que impedem a emissão da certidão.
B) Falta, nos autos, os comprovantes exigidos pelo edital.
C) Faltam documentos no processo administrativo encaminhado à comissão.
D) Devem haver documentos suficientes para a análise do pedido.

### Questão 7
**Nível: Médio**

Assinale a alternativa em que o emprego do acento indicativo de crase está correto.

A) A servidora entregou a manifestação à Vossa Senhoria.
B) O candidato começou à revisar o edital após o simulado.
C) O relatório foi encaminhado à diretoria técnica para análise.
D) O servidor retornou à pé ao setor de protocolo.

### Questão 8
**Nível: Médio**

Assinale a alternativa em que a vírgula foi empregada incorretamente.

A) Após a publicação do edital, os candidatos reorganizaram o cronograma.
B) O CRA-PR, autarquia de fiscalização profissional, divulgou novas orientações.
C) Embora o conteúdo seja extenso, a revisão diária favorece a retenção.
D) Os candidatos que revisaram o edital, identificaram a alteração do prazo.

### Questão 9
**Nível: Médio**

Leia: “O sistema é eficiente; contudo, depende de dados atualizados.” Sem alterar a relação entre as orações, “contudo” pode ser substituído por:

A) entretanto.
B) por conseguinte.
C) porquanto.
D) contanto que.

### Questão 10
**Nível: Médio**

Assinale a alternativa correta quanto à regência verbal no padrão formal.

A) O candidato visava o cargo de analista, no sentido de aspirar a ele.
B) O candidato obedeceu ao edital e às orientações da banca.
C) A equipe preferiu revisar o texto do que manter a versão anterior.
D) Os servidores assistiram o treinamento, no sentido de presenciá-lo.

### Questão 11
**Nível: Médio**

Leia: “Os dados cadastrais foram conferidos por dois servidores, e esse procedimento reduziu inconsistências.” A expressão “esse procedimento” retoma:

A) uma etapa do trabalho não mencionada no período.
B) a redução das inconsistências identificadas no cadastro.
C) apenas o substantivo “servidores”.
D) a conferência dos dados cadastrais por dois servidores.

### Questão 12
**Nível: Médio**

No período “Se o planejamento for consistente, a execução será mais segura”, a oração introduzida por “se” expressa:

A) conclusão decorrente de uma premissa já comprovada.
B) concessão diante de um obstáculo insuficiente.
C) oposição entre planejamento e execução.
D) condição para que a execução seja mais segura.

### Questão 13
**Nível: Médio**

Assinale a alternativa em que “há” e “a” foram empregados corretamente.

A) Estudo o conteúdo há três meses, e a prova ocorrerá daqui a vinte dias.
B) A três meses estudo o conteúdo, e a prova será realizada há vinte dias.
C) Há três meses ocorrerá a prova, e o edital saiu a duas semanas.
D) Estudo o conteúdo a três meses, e a prova ocorrerá daqui há vinte dias.

### Questão 14
**Nível: Médio**

Assinale a alternativa em que há ambiguidade de referência pronominal.

A) A equipe revisou seu próprio relatório antes de enviá-lo à diretoria.
B) O analista informou que o relatório elaborado pela equipe estava incompleto.
C) O analista informou ao coordenador que seu relatório estava incompleto.
D) O coordenador recebeu ontem o relatório final elaborado pelo analista.

### Questão 15
**Nível: Médio**

Leia: “A medida deve ser mantida, pois reduz riscos operacionais sem restringir o atendimento.” No contexto, “pois” introduz:

A) explicação que fundamenta a necessidade de manter a medida.
B) ressalva que limita a eficácia da medida.
C) alternativa à manutenção da medida.
D) condição necessária para a redução dos riscos.

### Questão 16
**Nível: Médio**

Assinale a alternativa correta quanto à colocação pronominal no padrão formal.

A) Não se deve desconsiderar a retificação publicada pela banca.
B) Me comunicaram o resultado no início da reunião.
C) A comissão tinha comunicado-me a alteração antes da reunião.
D) Não deve-se desconsiderar a retificação publicada pela banca.

### Questão 17
**Nível: Médio**

Assinale a alternativa com pontuação adequada.

A) Curitiba, capital do Paraná sediará o encontro regional em agosto.
B) Curitiba, capital do Paraná, sediará o encontro regional em agosto.
C) Curitiba capital do Paraná, sediará o encontro regional em agosto.
D) Curitiba capital, do Paraná, sediará o encontro regional em agosto.

### Questão 18
**Nível: Médio**

Leia: “Apenas os candidatos que revisaram a legislação específica identificaram a exceção normativa.” Considerando o alcance de “apenas”, o período afirma que:

A) os candidatos identificaram somente uma exceção, embora pudessem identificar outras.
B) todos os candidatos revisaram a legislação, mas somente alguns identificaram a exceção.
C) a revisão da legislação foi a única atividade realizada por todos os candidatos.
D) o grupo que identificou a exceção ficou restrito aos candidatos que revisaram a legislação específica.

### Questão 19
**Nível: Médio**

Assinale a frase correta quanto à concordância nominal e verbal.

A) Segue anexa ao processo os relatórios solicitados pela comissão.
B) Segue anexos ao processo os documentos solicitados pela comissão.
C) Seguem anexo ao processo as declarações solicitadas pela comissão.
D) Seguem anexos ao processo os documentos solicitados pela comissão.

### Questão 20
**Nível: Médio**

Leia: “A política de atendimento foi reformulada para reduzir filas sem excluir usuários com dificuldade de acesso digital.” A oração “para reduzir filas” expressa:

A) consequência imprevista da reformulação.
B) contraste entre a política e o atendimento.
C) finalidade atribuída à reformulação da política.
D) concessão diante de uma dificuldade.

### Questão 21
**Nível: Difícil**

Assinale a alternativa em que a palavra “onde” foi empregada de acordo com a norma-padrão.

A) O prédio onde funciona o setor de atendimento passa por reforma.
B) A hipótese onde o prazo seria prorrogado foi rejeitada.
C) O fundamento onde a decisão se apoiou consta do parecer.
D) O processo onde a inconsistência foi registrada retornou à unidade.

### Questão 22
**Nível: Difícil**

Para o tema “digitalização de serviços públicos e proteção de direitos”, qual enunciado funciona melhor como tese de uma dissertação?

A) A digitalização dos serviços públicos avançou nas últimas décadas e integra o cotidiano administrativo.
B) A expansão dos serviços digitais deve combinar ganho de eficiência, canais inclusivos e proteção efetiva dos dados pessoais.
C) De que modo a Administração poderá digitalizar serviços sem produzir novos riscos aos cidadãos?
D) Serão examinados exemplos de plataformas públicas antes de se apresentar, ao final, uma opinião sobre o tema.

### Questão 23
**Nível: Difícil**

Leia a introdução: “A tecnologia é importante. Hoje tudo é tecnologia. A tecnologia está em todos os lugares.” O principal problema argumentativo do trecho é:

A) a antecipação de uma proposta de intervenção que deveria aparecer apenas na conclusão.
B) a delimitação excessiva do tema, que impede a inclusão de exemplos no desenvolvimento.
C) a presença de argumento circular, embora haja tese explícita sobre serviços públicos digitais.
D) a generalidade das afirmações e a ausência de uma tese que delimite o ponto de vista.

### Questão 24
**Nível: Difícil**

Em um desenvolvimento sobre digitalização inclusiva, assinale o trecho que apresenta argumento mais consistente.

A) A digitalização merece atenção porque constitui tema atual e frequentemente debatido pela sociedade.
B) Os serviços digitais são eficientes quando funcionam bem, razão pela qual devem ser ampliados.
C) A digitalização reduz deslocamentos e espera, ampliando o acesso; sem acessibilidade e canais alternativos, porém, pode excluir usuários vulneráveis.
D) A existência de plataformas eletrônicas demonstra, por si só, que todos os cidadãos passaram a ter acesso equivalente.

### Questão 25
**Nível: Difícil**

Assinale a frase mais adequada a uma dissertação por combinar registro formal, precisão e objetividade.

A) É absolutamente evidente para qualquer pessoa sensata que os dados públicos exigem bastante cuidado.
B) A meu ver, parece que talvez a transparência possa ajudar um pouco a Administração.
C) A gestão de dados envolve certas coisas importantes, que serão resolvidas conforme for possível.
D) A Administração deve definir finalidade, controle de acesso e prazo de retenção para os dados que trata.

### Questão 26
**Nível: Difícil**

Assinale a alternativa em que o acento indicativo de crase foi empregado indevidamente.

A) O servidor começou à analisar o processo após receber a defesa.
B) A informação foi encaminhada à autoridade responsável pela decisão.
C) A comissão fez referência àquela auditoria realizada em maio.
D) A equipe compareceu às reuniões previstas no cronograma.

### Questão 27
**Nível: Difícil**

Leia: “Os candidatos que estudaram o edital resolveram melhor as questões.” Sem vírgulas, a oração “que estudaram o edital” permite concluir que:

A) todos os candidatos que não estudaram o edital necessariamente resolveram pior as questões.
B) todos os candidatos estudaram o edital, e a oração apenas acrescenta informação acessória.
C) o estudo do edital é apresentado como causa comprovada e exclusiva do melhor desempenho.
D) a afirmação sobre melhor desempenho se restringe ao subconjunto dos candidatos que estudaram o edital.

### Questão 28
**Nível: Difícil**

Leia: “Os candidatos, que estudaram o edital, resolveram melhor as questões.” Considerando apenas a estrutura sintática e a pontuação, a oração entre vírgulas tem valor:

A) restritivo, pois seleciona apenas parte dos candidatos mencionados.
B) condicional, pois subordina o desempenho ao estudo do edital.
C) comparativo, pois confronta dois grupos de candidatos.
D) explicativo, pois acrescenta informação acessória sobre todos os candidatos.

### Questão 29
**Nível: Difícil**

Assinale a alternativa que preserva o paralelismo sintático dos termos coordenados.

A) O plano exige a análise de riscos, controlar acessos e a revisão de incidentes.
B) O plano exige ler a teoria, resolver questões e revisar os erros registrados.
C) O plano exige que o candidato leia a teoria, resolver questões e revisão dos erros.
D) O plano exige leitura da teoria, resolver questões e que os erros sejam revistos.

### Questão 30
**Nível: Difícil**

Em “A equipe revisou o relatório; o coordenador, a planilha; e a diretora, o parecer”, as vírgulas após “coordenador” e “diretora”:

A) isolam vocativos dirigidos aos responsáveis por cada documento.
B) separam indevidamente os sujeitos dos verbos expressos nas duas orações.
C) assinalam a elipse do verbo “revisou”, recuperável na primeira oração.
D) introduzem apostos que especificam “relatório” e “planilha”.

### Questão 31
**Nível: Difícil**

Assinale a frase correta no padrão formal.

A) Houveram dois anos de testes antes que o sistema fosse implantado.
B) Fazem dois anos que o sistema foi implantado e seis meses que passou pela última revisão.
C) Devem fazer dois anos que o sistema foi implantado e seis meses que passou pela última revisão.
D) Faz dois anos que o sistema foi implantado e seis meses que passou pela última revisão.

### Questão 32
**Nível: Difícil**

Assinale a alternativa em que “porquê” está corretamente empregado.

A) O relatório não foi enviado porquê faltava a assinatura da chefia.
B) Ninguém explicou o porquê da alteração realizada no cronograma.
C) A comissão perguntou porque motivo o candidato não apresentou o documento.
D) Porquê o prazo foi alterado sem comunicação aos interessados?

### Questão 33
**Nível: Difícil**

Leia: “A revisão cruzada detectou inconsistências que a conferência automática não identificara; portanto, o procedimento deve ser mantido.” O termo “portanto” introduz:

A) conclusão sustentada pelo resultado mencionado na oração anterior.
B) condição necessária para que as inconsistências sejam detectadas.
C) concessão que relativiza a utilidade da revisão cruzada.
D) oposição entre a conferência automática e a manutenção do procedimento.

### Questão 34
**Nível: Difícil**

No período “As inconsistências foram identificadas pela equipe de auditoria durante a revisão”, a expressão “pela equipe de auditoria” exerce a função de:

A) agente da passiva, pois indica quem praticou a ação verbal.
B) adjunto adnominal que restringe o sentido de “inconsistências”.
C) sujeito paciente, pois recebe a ação de identificar.
D) objeto indireto exigido pelo verbo “identificar”.

### Questão 35
**Nível: Difícil**

Assinale a alternativa em que a segunda oração expressa causa da ação indicada na primeira.

A) A equipe reabriu a análise para verificar a autenticidade dos documentos.
B) A equipe reabriu a análise, embora o prazo interno já estivesse encerrado.
C) A equipe reabriu a análise porque surgiram documentos capazes de alterar a decisão.
D) A equipe reabriria a análise, desde que a autoridade prorrogasse o prazo.

### Questão 36
**Nível: Difícil**

Em “A norma publicada em 2025 alterou o procedimento de registro”, o segmento “publicada em 2025” funciona como:

A) oração reduzida adverbial que indica quando ocorreu a alteração do procedimento.
B) predicado principal cujo sujeito está oculto no período.
C) oração reduzida de particípio com valor adjetivo, que restringe a referência de “norma”.
D) complemento nominal exigido pelo substantivo “norma”.

### Questão 37
**Nível: Difícil**

Assinale a alternativa em que a pontuação está inteiramente adequada.

A) No início da semana, o candidato, conforme o cronograma, revisou arquitetura, sistemas operacionais e banco de dados.
B) No início da semana o candidato, conforme o cronograma, revisou arquitetura sistemas operacionais e banco de dados.
C) No início da semana, o candidato, revisou arquitetura, sistemas operacionais e banco de dados.
D) No início, da semana, o candidato conforme o cronograma revisou, arquitetura, sistemas operacionais e banco de dados.

### Questão 38
**Nível: Difícil**

Leia: “A solução não elimina todos os riscos, tampouco dispensa o monitoramento contínuo.” Nesse contexto, “tampouco”:

A) introduz a finalidade de manter o monitoramento.
B) conclui que os riscos persistem por falta de monitoramento.
C) acrescenta uma segunda negação, com sentido equivalente a “também não”.
D) explica a causa de a solução não eliminar todos os riscos.

### Questão 39
**Nível: Difícil**

Assinale a alternativa que melhor conclui uma dissertação cuja tese defende transparência compatível com a proteção de dados pessoais.

A) Portanto, a transformação digital também exige discutir a aquisição de equipamentos, tema que não foi examinado neste texto.
B) Assim, finalidade definida, acesso controlado e prestação de contas permitem conciliar transparência e proteção de dados, fortalecendo a confiança social.
C) Conclui-se que a publicidade deve prevalecer em qualquer hipótese, ainda que exponha dados pessoais sem necessidade.
D) Em síntese, transparência e proteção de dados são assuntos complexos, e cada órgão decidirá livremente como agir.

### Questão 40
**Nível: Difícil**

Assinale a alternativa correta quanto à acentuação gráfica.

A) “Órgão”, “relatório” e “possível” recebem acento pela mesma regra.
B) “Público”, “técnico” e “lógico” são acentuados por serem proparoxítonos.
C) “Lógico” pode perder o acento sem alteração de pronúncia ou de classe gramatical.
D) “Técnico” é acentuado por ser paroxítona terminada em “o”.

### Questão 41
**Nível: Muito difícil**

Leia: “A comissão confrontou as propostas e registrou as divergências; contudo, não homologou o resultado.” Qual reescrita preserva a adição entre as duas primeiras ações e a oposição introduzida no segmento final, sem criar relação causal inexistente?

A) Como confrontou as propostas, a comissão registrou as divergências; portanto, não homologou o resultado.
B) A comissão ou confrontou as propostas ou registrou as divergências; por isso, não homologou o resultado.
C) Embora confrontasse as propostas, a comissão registrou as divergências e, por essa razão, não homologou o resultado.
D) A comissão confrontou as propostas e registrou as divergências; entretanto, não homologou o resultado.

### Questão 42
**Nível: Muito difícil**

Assinale a alternativa em que todas as relações de regência nominal estão adequadas ao padrão formal.

A) O parecer era compatível à norma e contrário o entendimento anterior.
B) O sistema permaneceu acessível aos usuários e passível à auditoria externa.
C) A comissão mostrou-se favorável com o recurso e avessa de nova instrução.
D) O candidato estava apto ao exercício da função e consciente das responsabilidades do cargo.

### Questão 43
**Nível: Muito difícil**

Em uma questão que pede a alternativa INCORRETA, lê-se: “A Administração pode anular atos ilegais e revogar atos válidos inconvenientes, produzindo, em ambos os casos, efeitos necessariamente retroativos.” A primeira parte distingue corretamente os institutos, mas o trecho final generaliza os efeitos. Qual procedimento conduz ao julgamento correto?

A) considerar a opção correta, porque basta uma de suas orações coordenadas reproduzir regra verdadeira.
B) testar a proposição inteira, perceber que o qualificador “em ambos os casos” torna falsa a generalização e marcá-la após reler o comando.
C) desconsiderar o trecho sobre efeitos, porque informações posteriores à primeira vírgula não integram o núcleo da alternativa.
D) inverter mentalmente cada afirmação verdadeira e escolher outra opção, sem verificar o alcance de expressões como “necessariamente”.

### Questão 44
**Nível: Muito difícil**

Considere que, no período “O candidato só revisou legislação depois de errar o simulado”, o advérbio “só” incide sobre a circunstância temporal. Assinale a reescrita que altera o sentido original.

A) Somente depois de errar o simulado, o candidato revisou legislação.
B) A revisão de legislação pelo candidato ocorreu apenas após o erro no simulado.
C) Antes de errar o simulado, o candidato já havia revisado legislação.
D) Foi apenas depois do erro no simulado que o candidato revisou legislação.

### Questão 45
**Nível: Muito difícil**

Leia: “Embora dispusesse de orçamento reduzido, a equipe concluiu as etapas essenciais; por isso, a direção manteve o cronograma.” Qual reescrita preserva simultaneamente a concessão do primeiro segmento e a consequência expressa no segundo período?

A) Ainda que tivesse orçamento reduzido, a equipe concluiu as etapas essenciais; consequentemente, a direção manteve o cronograma.
B) Como tinha orçamento reduzido, a equipe concluiu as etapas essenciais; apesar disso, a direção manteve o cronograma.
C) Se tivesse orçamento reduzido, a equipe concluiria as etapas essenciais; entretanto, a direção manteve o cronograma.
D) A equipe concluiu as etapas essenciais porque tinha orçamento reduzido; ainda assim, a direção manteve o cronograma.

### Questão 46
**Nível: Muito difícil**

Assinale a frase inteiramente correta quanto à concordância no padrão formal.

A) Mais de um setor enviaram o parecer solicitado pela diretoria.
B) Devem haver, nos autos, razões suficientes para rever a decisão.
C) Um ou outro candidatos apresentaram dúvida sobre a retificação.
D) Mais de um candidato apresentou recurso fundamentado contra o resultado.

### Questão 47
**Nível: Muito difícil**

Leia: “O órgão deve informar a finalidade do tratamento e limitar o acesso aos dados. O cumprimento conjunto **dessas exigências** reduz usos incompatíveis; **a última delas**, porém, não dispensa o registro das operações.” As duas expressões destacadas retomam, respectivamente:

A) apenas o dever de informar; e o conjunto indeterminado de operações futuras.
B) uma obrigação que será anunciada depois; e a redução dos usos incompatíveis.
C) as duas obrigações do primeiro período; e, especificamente, a limitação de acesso aos dados.
D) apenas a finalidade do tratamento; e, especificamente, o dever de informar os titulares.

### Questão 48
**Nível: Muito difícil**

Complete corretamente o período: “A ___ do edital corrigiu o erro material; depois, a autoridade decidiu ___ os demais termos e recomendou ___ no tratamento dos dados pessoais.”

A) ratificação — retificar — discrição.
B) retificação — ratificar — discrição.
C) ratificação — ratificar — descrição.
D) retificação — retificar — descrição.

### Questão 49
**Nível: Muito difícil**

Leia: “A capacitação deve ser contínua, uma vez que a atualização dos sistemas modifica procedimentos e riscos; ainda assim, treinamento isolado não substitui controles técnicos.” Qual par de conectores pode substituir as expressões destacadas sem alterar, respectivamente, a causa e a oposição concessiva?

A) à medida que — portanto.
B) a menos que — por conseguinte.
C) porque — mesmo assim.
D) embora — por essa razão.

### Questão 50
**Nível: Muito difícil**

Em relatório administrativo, a redação deve separar fato observado de providência recomendada e fornecer elementos verificáveis. Qual trecho atende conjuntamente a esses critérios, sem apresentar inferência como fato comprovado?

A) O teste de 12 de maio registrou três falhas de integração, detalhadas nos itens 4, 7 e 9; recomenda-se corrigi-las até 20 de maio e repetir o teste.
B) As falhas decorreram certamente de negligência da equipe, razão pela qual serão adotadas, oportunamente, todas as providências cabíveis.
C) Foram observadas inconsistências relevantes em diversos pontos, o que demonstra a necessidade evidente de aperfeiçoar o sistema.
D) O cadastro será regularizado no momento adequado, conforme a causa provável das falhas venha a ser confirmada pelos responsáveis.

## Questões extras de revisão fixa do Dia 5

#### Extra Dia 5.1

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Articulação entre lei, decreto, resoluções e regimento
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Sobre a articulação entre as normas centrais da legislação profissional, assinale a alternativa correta.

A) O Regimento Interno pode ampliar, por decisão regional, o campo profissional definido na lei federal.
B) As resoluções do CFA prevalecem sobre a lei e o decreto sempre que forem posteriores.
C) A lei disciplina a profissão, o decreto a regulamenta e os atos do Sistema CFA/CRAs complementam matérias de sua competência.
D) O decreto regulamentador cuida apenas da organização interna do CRA-PR, sem relação com a execução da lei.

#### Extra Dia 5.2

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Uso de título e regularidade do exercício profissional
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Uma pessoa sem habilitação regular anuncia-se publicamente como profissional registrado no CRA-PR. Assinale a alternativa correta.

A) A fiscalização somente pode atuar se um cliente comprovar prejuízo patrimonial decorrente do anúncio.
B) O anúncio é matéria exclusivamente publicitária enquanto não houver contrato assinado com cliente.
C) O registro obtido posteriormente torna regular, de forma retroativa, todo uso anterior do título.
D) A situação deve ser verificada quanto à regularidade do exercício e ao possível uso indevido da condição profissional.

#### Extra Dia 5.3

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Campo e competência territorial de fiscalização
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Quanto à atuação fiscalizatória no Sistema CFA/CRAs, assinale a alternativa correta.

A) Cabe exclusivamente ao CFA realizar inspeções e apurar exercício irregular em todo o território nacional.
B) O CRA fiscaliza, em sua jurisdição, atividades relacionadas ao campo profissional da Administração.
C) Toda atividade empresarial desenvolvida no Paraná se sujeita ao CRA-PR, ainda que alheia ao campo da Administração.
D) A competência do CRA é definida apenas pelo domicílio de quem apresenta a denúncia.

#### Extra Dia 5.4

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Conteúdo e método de estudo do Código de Ética
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

No estudo da RN CFA nº 671/2025 indicado pelo material, deve-se priorizar:

A) deveres, direitos, infrações e lógica de fixação e gradação das sanções.
B) apenas valores de anuidades e regras de cobrança administrativa.
C) a estrutura dos órgãos internos do CRA-PR, por se tratar do seu Regimento Interno.
D) somente a memorização da numeração dos artigos, sem relacioná-los a casos concretos.

#### Extra Dia 5.5

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Finalidade dos conselhos profissionais
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

A finalidade institucional da fiscalização exercida pelos conselhos profissionais é:

A) defender exclusivamente interesses econômicos dos profissionais registrados.
B) substituir o Poder Judiciário na solução definitiva de todo conflito contratual da categoria.
C) definir, de forma autônoma, os currículos obrigatórios de todos os cursos superiores da área.
D) proteger a sociedade e promover a regularidade do exercício profissional.

#### Extra Dia 5.6

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Efetividade da responsabilidade técnica
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Uma empresa indica responsável técnico que apenas empresta o nome e assina documentos, sem acompanhar as atividades. À luz do material, assinale a alternativa correta.

A) A indicação é suficiente quando o profissional autoriza, por escrito, o uso permanente de seu registro.
B) A responsabilidade técnica pressupõe atuação efetiva e regular, não simples assinatura formal sem participação.
C) A pessoa jurídica pode assumir a responsabilidade técnica em nome próprio, sem profissional identificado.
D) A responsabilidade do indicado termina com a assinatura inicial, ainda que a atividade continue sob seu nome.

#### Extra Dia 5.7

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Seleção da norma vigente indicada no edital
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Por que o material adota a RN CFA nº 671/2025, e não a RN CFA nº 640/2024, como base principal do Código de Ética?

A) Porque a resolução mais recente disponível na internet sempre substitui o conteúdo do edital, mesmo sem ato oficial.
B) Porque a RN CFA nº 651/2024 converteu-se automaticamente no novo Código de Ética.
C) Porque a apostila segue o edital retificado e a informação de revogação indicada em fonte oficial.
D) Porque as duas resoluções devem ser aplicadas cumulativamente aos mesmos fatos, sem análise de vigência.

#### Extra Dia 5.8

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Método de resolução de casos de legislação específica
**Nível:** Médio
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Diante de um caso prático de legislação do Sistema CFA/CRAs, qual sequência de análise é mais segura?

A) Identificar a conduta, o sujeito envolvido, o órgão competente e a norma aplicável.
B) Escolher primeiro a sanção mais severa e depois procurar uma norma que a justifique.
C) Tratar CFA e CRA como autoridades de competência idêntica em qualquer situação.
D) Desconsiderar expressões como “em regra” e “salvo”, porque não alteram o alcance normativo.

#### Extra Dia 5.9

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Legalidade, processo e proporcionalidade das sanções
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Um enunciado sustenta que qualquer descumprimento administrativo produz automaticamente a cassação do registro. Assinale a alternativa correta.

A) A afirmação está correta, pois a cassação é consequência necessária de toda infração.
B) A sanção pode ser aplicada sem defesa prévia quando a irregularidade estiver documentada.
C) A proporcionalidade autoriza o conselho a criar penalidade não prevista sempre que a considerar mais justa.
D) A afirmação está errada: a sanção exige base normativa, processo regular e adequação ao caso.

#### Extra Dia 5.10

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Objeto do Regimento Interno do CRA-PR
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Em uma questão sobre a RN CFA nº 651/2024, qual conteúdo deve ser associado diretamente ao Regimento Interno do CRA-PR?

A) Apenas os valores anuais de contribuições e as regras de cobrança judicial.
B) A definição originária do campo privativo da profissão em todo o território nacional.
C) Os deveres éticos e as sanções disciplinares previstos no Código de Ética vigente.
D) A estrutura dos órgãos, a distribuição de competências e o funcionamento institucional do conselho regional.

#### Extra Dia 5.11

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Publicidade e uso indevido de condição profissional
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Um terceiro sem registro anuncia serviços e se apresenta como profissional regularmente habilitado perante o CRA-PR. Assinale a alternativa correta.

A) O CRA-PR só pode verificar o anúncio depois de decisão definitiva de órgão de defesa do consumidor.
B) A conduta pode configurar uso indevido de condição profissional e justifica verificação fiscalizatória.
C) O fato somente interessa à fiscalização se o anúncio já tiver gerado contrato remunerado.
D) A obtenção posterior do registro convalida automaticamente a divulgação feita quando inexistia habilitação.

#### Extra Dia 5.12

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Relação entre lei e decreto regulamentador
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Sobre a relação entre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967, assinale a alternativa correta.

A) O decreto pode ampliar livremente as atividades profissionais além dos limites definidos pela lei.
B) O decreto regulamenta a lei e detalha sua execução, sem ocupar posição hierárquica superior.
C) A edição do decreto revogou a lei, que deixou de integrar a base normativa da profissão.
D) O decreto tem natureza de regimento interno e vincula somente os órgãos do CRA-PR.

#### Extra Dia 5.13

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Distinção entre formação, registro e regularidade financeira
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Um profissional registrado deixa de pagar contribuição devida ao conselho. Qual afirmação distingue corretamente os efeitos possíveis dessa situação?

A) A inadimplência pode gerar consequências perante o conselho, mas não apaga a formação acadêmica.
B) A falta de pagamento permite aplicar qualquer restrição sem processo ou fundamento normativo.
C) A inadimplência cancela o diploma e elimina a formação acadêmica obtida pelo profissional.
D) A contribuição deixa de ser exigível sempre que o profissional mantém vínculo acadêmico com a área.

#### Extra Dia 5.14

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Uso de fontes oficiais no estudo normativo
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Para responder a uma questão que cobre prazo, rito ou sanção específica, a conduta de estudo mais segura é:

A) atribuir a mesma autoridade a comentários de cursos e ao texto publicado pelo órgão competente.
B) adotar o prazo mencionado em um resumo, ainda que diverja da publicação oficial.
C) conferir o texto oficial da norma pertinente e sua vigência, usando o resumo como apoio.
D) aplicar automaticamente a resolução numericamente mais recente, mesmo que o edital indique outra base.

#### Extra Dia 5.15

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Identificação da fonte normativa pela matéria
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Uma questão solicita a norma mais diretamente relacionada à sede, aos órgãos internos e ao funcionamento institucional do CRA-PR. A resposta é:

A) o Regimento Interno do CRA-PR aprovado pela RN CFA nº 651/2024.
B) a Lei nº 4.769/1965, apenas por disciplinar o campo profissional.
C) o Decreto nº 61.934/1967, exclusivamente por regulamentar a lei profissional.
D) o Código de Ética dos Profissionais de Administração.

#### Extra Dia 5.16

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Hierarquia e função das fontes da legislação profissional
**Nível:** Difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Sobre a relação entre lei, decreto regulamentar, resoluções do CFA e Regimento Interno do CRA-PR, assinale a alternativa correta.

A) O Regimento pode ampliar livremente o campo profissional definido em lei, desde que a alteração produza efeitos apenas no Paraná.
B) Resoluções posteriores prevalecem automaticamente sobre a lei sempre que disciplinarem assunto mais específico.
C) A lei estabelece a base; o decreto regulamenta sua execução; resoluções e Regimento atuam dentro de suas competências e dos limites superiores.
D) O decreto substitui a lei regulamentada, que deixa de integrar a análise após sua publicação.

#### Extra Dia 5.17

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Competência nacional do CFA e atuação regional do CRA-PR
**Nível:** Muito difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Uma empresa presta serviços no campo da Administração no Paraná e surge dúvida sobre qual entidade deve verificar sua regularidade local. Assinale a alternativa correta.

A) O CFA realiza ordinariamente toda fiscalização local, porque os Conselhos Regionais possuem função apenas consultiva.
B) O CRA-PR atua no registro e na fiscalização em sua jurisdição, enquanto o CFA exerce coordenação e normatização nacionais.
C) Qualquer CRA pode fiscalizar diretamente o fato no Paraná, sem consideração de jurisdição territorial.
D) A existência de CNPJ transfere a análise ao registro empresarial e afasta toda competência do Sistema CFA/CRAs.

#### Extra Dia 5.18

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Responsabilidade técnica e uso indevido do registro
**Nível:** Muito difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Uma pessoa registrada é indicada como responsável técnica por empresa, mas apenas permite o uso de seu nome e assina documentos que não elaborou nem supervisionou. À luz do conteúdo estudado:

A) a responsabilidade técnica exige participação efetiva, e o empréstimo de nome ou registro pode gerar apuração ética e fiscalizatória.
B) a assinatura formal basta para regularizar a atividade, mesmo sem qualquer atuação técnica real.
C) o consentimento da empresa transforma automaticamente em regular o uso do registro profissional.
D) o CRA só pode examinar o caso se houver condenação judicial prévia por dano material.

#### Extra Dia 5.19

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Sigilo profissional e suas exceções
**Nível:** Muito difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Profissional recebe proposta para revelar informação confidencial conhecida durante serviço prestado a um cliente. Não há dever legal de divulgação nem justa causa demonstrada. A conduta compatível com o Código de Ética é:

A) revelar a informação se a proposta for financeiramente vantajosa, pois o interesse econômico configura exceção ética.
B) divulgar parte do conteúdo em rede social, desde que não identifique nominalmente o cliente.
C) repassar os dados a terceiro e atribuir a ele a decisão sobre eventual publicação.
D) preservar o sigilo, pois vantagem comercial não substitui justa causa nem hipótese legal aplicável.

#### Extra Dia 5.20

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Distinção entre Regimento Interno e Código de Ética
**Nível:** Muito difícil
**Referência:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4)

Em um caso, discute-se a competência do Plenário e da Diretoria do CRA-PR; em outro, examina-se possível violação de sigilo profissional. Qual associação normativa está correta?

A) Ambos os temas pertencem exclusivamente ao Regulamento de Registro aprovado pela RN CFA nº 649/2024.
B) A estrutura interna é matéria do Código de Ética, enquanto o sigilo pertence ao Regimento Interno.
C) Órgãos e competências internas remetem ao Regimento aprovado pela RN CFA nº 651/2024; sigilo profissional remete ao Código de Ética da RN CFA nº 671/2025.
D) O Regimento e o Código de Ética possuem objeto idêntico e podem ser usados indistintamente.

## Entrega prática do Bloco 6 — Dia 5

**Referência:** [Dia 5 — Bloco 6 — Recuperação de Português e caderno de erros](semana_01_estudo.md#s1-d5-b6)

Escolha três frases erradas do seu caderno e registre `forma original | forma corrigida | regra recuperada | seção de origem`. Em seguida, escreva sem consulta uma frase concessiva e outra conclusiva. Se a justificativa depender de regra ainda não estudada, marque o ponto para semana posterior; não crie regra nova neste bloco.

## Gabarito do Dia 5

1. A
2. B
3. B
4. C
5. B
6. C
7. C
8. D
9. A
10. B
11. D
12. D
13. A
14. C
15. A
16. A
17. B
18. D
19. D
20. C
21. A
22. B
23. D
24. C
25. D
26. A
27. D
28. D
29. B
30. C
31. D
32. B
33. A
34. A
35. C
36. C
37. A
38. C
39. B
40. B
41. D
42. D
43. B
44. C
45. A
46. D
47. C
48. B
49. C
50. A

### Gabarito das questões extras de revisão fixa do Dia 5

Extra Dia 5.1: C
Extra Dia 5.2: D
Extra Dia 5.3: B
Extra Dia 5.4: A
Extra Dia 5.5: D
Extra Dia 5.6: B
Extra Dia 5.7: C
Extra Dia 5.8: A
Extra Dia 5.9: D
Extra Dia 5.10: D
Extra Dia 5.11: B
Extra Dia 5.12: B
Extra Dia 5.13: A
Extra Dia 5.14: C
Extra Dia 5.15: A
Extra Dia 5.16: C
Extra Dia 5.17: B
Extra Dia 5.18: A
Extra Dia 5.19: D
Extra Dia 5.20: C


## Comentários do Dia 5

### Comentário da Questão 1

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** Resume o benefício da digitalização e a ressalva relativa à segurança e aos direitos.
- **B) está errada:** A segurança aparece integrada ao ganho de acesso e eficiência, não como objetivo independente.
- **C) está errada:** O texto não condiciona a legitimidade da digitalização à eliminação dos canais presenciais.
- **D) está errada:** O trecho não afirma que preservar direitos reduz necessariamente a eficiência.
- **Conceito cobrado:** Interpretação e identificação da ideia central.
- **Pegadinha usada:** Omitir uma parte da tese ou transformar ressalva em incompatibilidade.
- **Como pensar para acertar:** Reúna a afirmação principal e o limite introduzido por “mas”.
- **Referência à apostila de estudo:** Dia 5 — interpretação, ideia central e inferência.

### Comentário da Questão 2

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** A exigência de segurança não é apresentada como causa da ampliação do acesso.
- **B) está correta:** “Mas” contrapõe uma ressalva ao benefício anterior sem negá-lo.
- **C) está errada:** O segmento não conclui o raciocínio; limita o alcance da primeira afirmação.
- **D) está errada:** O valor semântico é adversativo, e não condicional.
- **Conceito cobrado:** Relação semântica de conectores.
- **Pegadinha usada:** Confundir ressalva com causa, conclusão ou condição.
- **Como pensar para acertar:** Substitua o conector por “porém” e verifique a preservação do contraste.
- **Referência à apostila de estudo:** Dia 5 — semântica, coesão e conectores.

### Comentário da Questão 3

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** O período não informa se a maioria das inovações falha.
- **B) está correta:** Negar que toda inovação melhore a Administração admite ao menos um caso que não melhora.
- **C) está errada:** “Nem toda” não equivale a “nenhuma”.
- **D) está errada:** A origem da inovação não é mencionada.
- **Conceito cobrado:** Inferência e alcance de quantificadores.
- **Pegadinha usada:** Converter negação parcial em negação total ou em afirmação de maioria.
- **Como pensar para acertar:** Traduza “nem todo A é B” por “existe A que não é B”.
- **Referência à apostila de estudo:** Dia 5 — inferência, extrapolação e quantificadores.

### Comentário da Questão 4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Reproduz a relação entre transparência e confiança admitida no texto.
- **B) está errada:** Corresponde ao limite expresso pela locução “desde que”.
- **C) está correta:** A divulgação irrestrita de todo dado pessoal contradiz o limite de proteção e extrapola o texto.
- **D) está errada:** Sintetiza a compatibilização permitida pelo enunciado.
- **Conceito cobrado:** Identificação de extrapolação textual.
- **Pegadinha usada:** Absolutizar uma afirmação condicionada.
- **Como pensar para acertar:** Desconfie de termos absolutos quando o texto estabelece limite explícito.
- **Referência à apostila de estudo:** Dia 5 — inferência e extrapolação.

### Comentário da Questão 5

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Introduz aumento do esquecimento, sentido oposto ao original.
- **B) está correta:** A passagem para a voz passiva preserva as duas ações e seus sentidos.
- **C) está errada:** Afirma prejuízo à retenção, enquanto o período original afirma melhora.
- **D) está errada:** “Impede qualquer” e “integral” tornam absolutos efeitos que o original apenas apresenta como redução e melhora.
- **Conceito cobrado:** Reescrita com preservação de sentido.
- **Pegadinha usada:** Alterar polaridade ou intensidade lexical.
- **Como pensar para acertar:** Compare sujeito lógico, ações, direção dos efeitos e grau das afirmações.
- **Referência à apostila de estudo:** Dia 5 — reescrita e equivalência semântica.

### Comentário da Questão 6

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Com “existir”, o sujeito plural “pendências” exige “existem”.
- **B) está errada:** O sujeito plural “os comprovantes” exige “faltam”.
- **C) está correta:** “Faltam” concorda com o sujeito plural “documentos”.
- **D) está errada:** Na locução com “haver” existencial, o auxiliar permanece no singular: “deve haver”.
- **Conceito cobrado:** Concordância verbal com existir, faltar e haver.
- **Pegadinha usada:** Tratar “haver” existencial como verbo pessoal ou ignorar sujeito posposto.
- **Como pensar para acertar:** Identifique o verbo e teste se há sujeito ou construção impessoal.
- **Referência à apostila de estudo:** Dia 5 — sintaxe e concordância verbal.

### Comentário da Questão 7

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Em regra, não se usa artigo antes do pronome de tratamento “Vossa Senhoria”.
- **B) está errada:** Não ocorre crase antes de verbo no infinitivo.
- **C) está correta:** A regência de “encaminhar a” encontra o artigo feminino de “a diretoria”.
- **D) está errada:** A expressão “a pé” contém palavra masculina e não recebe crase.
- **Conceito cobrado:** Crase: fusão da preposição com artigo feminino.
- **Pegadinha usada:** Inserir crase antes de verbo, pronome de tratamento ou palavra masculina.
- **Como pensar para acertar:** Verifique simultaneamente a exigência de preposição e a admissão de artigo.
- **Referência à apostila de estudo:** Dia 5 — crase, casos obrigatórios e proibidos.

### Comentário da Questão 8

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa em que a vírgula foi empregada incorretamente; portanto, o gabarito corresponde à frase com pontuação inadequada.
- **A) está errada:** A vírgula isola corretamente o adjunto adverbial deslocado.
- **B) está errada:** As vírgulas isolam o aposto explicativo.
- **C) está errada:** A oração subordinada adverbial anteposta está corretamente separada.
- **D) está correta:** A vírgula separa o sujeito completo “Os candidatos que revisaram o edital” do verbo “identificaram”.
- **Conceito cobrado:** Emprego da vírgula.
- **Pegadinha usada:** Inserir vírgula entre sujeito e predicado por percepção de pausa.
- **Como pensar para acertar:** Localize primeiro o núcleo do sujeito e o verbo principal.
- **Referência à apostila de estudo:** Dia 5 — pontuação e usos da vírgula.

### Comentário da Questão 9

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** “Entretanto” preserva o valor adversativo de “contudo”.
- **B) está errada:** “Por conseguinte” tem valor conclusivo.
- **C) está errada:** “Porquanto” introduz causa ou explicação.
- **D) está errada:** “Contanto que” introduz condição.
- **Conceito cobrado:** Substituição de conectores com preservação de sentido.
- **Pegadinha usada:** Escolher conector formal de relação lógica diferente.
- **Como pensar para acertar:** Classifique a relação entre as orações antes de comparar os conectores.
- **Referência à apostila de estudo:** Dia 5 — conectores e progressão lógica.

### Comentário da Questão 10

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** No sentido de aspirar, “visar” rege preposição “a”: “visava ao cargo”.
- **B) está correta:** “Obedecer” rege preposição “a”, presente em “ao edital” e “às orientações”.
- **C) está errada:** Na comparação normativa, prefere-se uma coisa a outra, não “do que” outra.
- **D) está errada:** No sentido de presenciar, “assistir” rege preposição “a”: “assistiram ao treinamento”.
- **Conceito cobrado:** Regência verbal.
- **Pegadinha usada:** Empregar regência coloquial em construção formal.
- **Como pensar para acertar:** Determine o sentido do verbo e, só então, a preposição exigida.
- **Referência à apostila de estudo:** Dia 5 — regência verbal.

### Comentário da Questão 11

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** O referente está expresso no próprio período.
- **B) está errada:** A redução das inconsistências é o efeito atribuído ao procedimento.
- **C) está errada:** O referente não é o substantivo isolado, mas a ação descrita.
- **D) está correta:** O demonstrativo encapsula a ação anterior de conferir os dados por dois servidores.
- **Conceito cobrado:** Coesão referencial.
- **Pegadinha usada:** Associar o demonstrativo ao substantivo mais próximo, e não à ideia retomada.
- **Como pensar para acertar:** Substitua “esse procedimento” pela alternativa e verifique a coerência.
- **Referência à apostila de estudo:** Dia 5 — coesão, referência e retomada.

### Comentário da Questão 12

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** “Se” não apresenta conclusão de premissa comprovada.
- **B) está errada:** Não há obstáculo admitido com valor concessivo.
- **C) está errada:** Planejamento e execução não são contrapostos.
- **D) está correta:** A segurança da execução depende da hipótese de o planejamento ser consistente.
- **Conceito cobrado:** Oração subordinada adverbial condicional.
- **Pegadinha usada:** Confundir condição com conclusão ou concessão.
- **Como pensar para acertar:** Pergunte de qual hipótese depende o resultado da oração principal.
- **Referência à apostila de estudo:** Dia 5 — conectores e relações condicionais.

### Comentário da Questão 13

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** “Há” indica tempo decorrido, e “a” integra a expressão de tempo futuro.
- **B) está errada:** Tempo decorrido pede “há três meses”; futuro pede “daqui a vinte dias”.
- **C) está errada:** “Há” não marca tempo futuro, e tempo decorrido exige “há duas semanas”.
- **D) está errada:** Os dois empregos estão invertidos.
- **Conceito cobrado:** Distinção entre “há” e “a” em expressões temporais.
- **Pegadinha usada:** Trocar a marca de passado pela de futuro.
- **Como pensar para acertar:** Use “há” para tempo decorrido e “a” para tempo futuro ou distância.
- **Referência à apostila de estudo:** Dia 5 — ortografia e emprego contextual de “há” e “a”.

### Comentário da Questão 14

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** “Seu próprio relatório” e o pronome objeto remetem claramente à equipe e ao relatório.
- **B) está errada:** A autoria foi explicitada pela expressão “elaborado pela equipe”.
- **C) está correta:** “Seu relatório” pode ser entendido como relatório do analista ou do coordenador.
- **D) está errada:** Analista e coordenador têm funções sintáticas e referências claramente delimitadas.
- **Conceito cobrado:** Ambiguidade pronominal.
- **Pegadinha usada:** Ignorar a possibilidade de dois antecedentes para o possessivo.
- **Como pensar para acertar:** Liste os referentes compatíveis com o pronome e verifique se há mais de um.
- **Referência à apostila de estudo:** Dia 5 — coesão referencial e clareza.

### Comentário da Questão 15

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A redução de riscos fundamenta a orientação de manter a medida.
- **B) está errada:** A segunda oração reforça, e não restringe, a primeira.
- **C) está errada:** Não se apresentam opções alternadas.
- **D) está errada:** A redução dos riscos é dada como razão, não como condição hipotética.
- **Conceito cobrado:** Valor explicativo e causal de “pois”.
- **Pegadinha usada:** Classificar o conector isoladamente, sem observar o contexto.
- **Como pensar para acertar:** Verifique se a segunda oração responde por que a primeira é defendida.
- **Referência à apostila de estudo:** Dia 5 — conectores de causa e explicação.

### Comentário da Questão 16

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A próclise é motivada pelo advérbio negativo “não”.
- **B) está errada:** No padrão formal cobrado, evita-se iniciar a oração com pronome oblíquo átono.
- **C) está errada:** O pronome não pode ser posposto ao particípio; caberia “tinha-me comunicado” ou “me tinha comunicado”.
- **D) está errada:** A palavra negativa atrai o pronome: “não se deve”.
- **Conceito cobrado:** Colocação pronominal.
- **Pegadinha usada:** Ignorar palavras atrativas ou reproduzir ordem coloquial.
- **Como pensar para acertar:** Procure termos negativos antes do verbo e posicione o pronome antes dele.
- **Referência à apostila de estudo:** Dia 5 — sintaxe e colocação pronominal.

### Comentário da Questão 17

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Falta a segunda vírgula para encerrar o aposto “capital do Paraná”.
- **B) está correta:** O aposto explicativo está isolado por duas vírgulas.
- **C) está errada:** A vírgula separa indevidamente o sujeito do verbo e não abre o aposto.
- **D) está errada:** A pontuação fragmenta o aposto e separa o sujeito do predicado.
- **Conceito cobrado:** Pontuação de aposto explicativo.
- **Pegadinha usada:** Usar apenas uma vírgula em termo intercalado.
- **Como pensar para acertar:** Retire o segmento explicativo e confira se a estrutura principal permanece íntegra.
- **Referência à apostila de estudo:** Dia 5 — pontuação e termos intercalados.

### Comentário da Questão 18

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** “Apenas” não incide sobre a quantidade de exceções identificadas.
- **B) está errada:** Não se afirma que todos os candidatos revisaram a legislação.
- **C) está errada:** O período não enumera todas as atividades realizadas pelos candidatos.
- **D) está correta:** O advérbio restringe aos candidatos que revisaram a legislação o grupo que identificou a exceção.
- **Conceito cobrado:** Alcance semântico de advérbio restritivo.
- **Pegadinha usada:** Deslocar mentalmente o escopo de “apenas”.
- **Como pensar para acertar:** Identifique o constituinte imediatamente abrangido pelo advérbio.
- **Referência à apostila de estudo:** Dia 5 — semântica contextual e restrição.

### Comentário da Questão 19

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Verbo e predicativo deveriam concordar com “os relatórios”: “seguem anexos”.
- **B) está errada:** O verbo deveria ir ao plural para concordar com “os documentos”.
- **C) está errada:** O predicativo deveria ser “anexas”, em concordância com “as declarações”.
- **D) está correta:** “Seguem” e “anexos” concordam com “os documentos”.
- **Conceito cobrado:** Concordância verbal e nominal.
- **Pegadinha usada:** Tratar “anexo” como invariável ou concordar com termo preposicionado.
- **Como pensar para acertar:** Localize o sujeito e o substantivo caracterizado pelo adjetivo.
- **Referência à apostila de estudo:** Dia 5 — concordância verbal e nominal.

### Comentário da Questão 20

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** A redução de filas é apresentada como objetivo deliberado.
- **B) está errada:** Não há oposição entre as ideias.
- **C) está correta:** A estrutura “para + infinitivo” indica o propósito da reformulação.
- **D) está errada:** O trecho não admite obstáculo com valor concessivo.
- **Conceito cobrado:** Oração subordinada adverbial final reduzida de infinitivo.
- **Pegadinha usada:** Confundir finalidade planejada com consequência.
- **Como pensar para acertar:** Pergunte “a política foi reformulada para quê?”.
- **Referência à apostila de estudo:** Dia 5 — conectores e relação de finalidade.

### Comentário da Questão 21

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** “Prédio” é lugar físico retomado adequadamente por “onde”.
- **B) está errada:** “Hipótese” é referente abstrato e não admite o uso normativo de “onde”.
- **C) está errada:** “Fundamento” não designa lugar físico; caberia “em que” ou “no qual”.
- **D) está errada:** “Processo” não é empregado como lugar físico; recomenda-se “em que” ou “no qual”.
- **Conceito cobrado:** Emprego normativo do pronome relativo “onde”.
- **Pegadinha usada:** Estender “onde” a qualquer antecedente abstrato.
- **Como pensar para acertar:** Verifique se o antecedente nomeia efetivamente um lugar.
- **Referência à apostila de estudo:** Dia 5 — coesão, pronomes relativos e reescrita.

### Comentário da Questão 22

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A frase apenas contextualiza o tema, sem defender posição.
- **B) está correta:** Delimita a posição e antecipa os eixos argumentativos de eficiência, inclusão e proteção.
- **C) está errada:** A pergunta problematiza o tema, mas não apresenta a resposta que será defendida.
- **D) está errada:** O metatexto adia o posicionamento e não formula tese.
- **Conceito cobrado:** Construção de tese dissertativa.
- **Pegadinha usada:** Confundir contextualização, pergunta ou roteiro com posicionamento.
- **Como pensar para acertar:** Procure uma frase discutível que possa orientar os parágrafos de desenvolvimento.
- **Referência à apostila de estudo:** Dia 5 — discursiva: introdução e tese.

### Comentário da Questão 23

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** O trecho não propõe intervenção nem apresenta conclusão.
- **B) está errada:** O problema é falta, e não excesso, de delimitação.
- **C) está errada:** Há repetição, mas não existe tese explícita sobre serviços públicos digitais.
- **D) está correta:** O trecho repete uma ideia ampla sem recorte nem posição argumentativa.
- **Conceito cobrado:** Diagnóstico de introdução dissertativa.
- **Pegadinha usada:** Tratar repetição temática como contextualização suficiente.
- **Como pensar para acertar:** Pergunte qual posição concreta o restante do texto deveria demonstrar.
- **Referência à apostila de estudo:** Dia 5 — discursiva: introdução, recorte e tese.

### Comentário da Questão 24

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Atualidade do tema, isoladamente, não explica mecanismo nem consequência.
- **B) está errada:** A formulação é circular: associa eficiência apenas ao fato de funcionar bem.
- **C) está correta:** Apresenta benefício, mecanismo concreto e contraponto relacionado à inclusão.
- **D) está errada:** A existência de plataforma não comprova acesso equivalente para todos.
- **Conceito cobrado:** Qualidade do desenvolvimento argumentativo.
- **Pegadinha usada:** Confundir afirmação formal ou atual com argumento desenvolvido.
- **Como pensar para acertar:** Prefira o trecho que liga tese, causa, consequência e ressalva pertinente.
- **Referência à apostila de estudo:** Dia 5 — discursiva: desenvolvimento e progressão argumentativa.

### Comentário da Questão 25

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** O apelo a “qualquer pessoa sensata” é avaliativo e substitui demonstração por pressão retórica.
- **B) está errada:** Marcas de opinião e hesitação tornam a afirmação subjetiva e imprecisa.
- **C) está errada:** “Certas coisas” e “conforme for possível” são expressões vagas.
- **D) está correta:** Indica sujeito, dever e três medidas verificáveis em registro formal.
- **Conceito cobrado:** Registro formal, precisão e objetividade.
- **Pegadinha usada:** Confundir aparência formal com redação informativa.
- **Como pensar para acertar:** Escolha a frase com agente, ação e critérios concretos.
- **Referência à apostila de estudo:** Dia 5 — discursiva: linguagem formal, clareza e objetividade.

### Comentário da Questão 26

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Não se emprega crase antes do infinitivo “analisar”.
- **B) está errada:** “Encaminhar a” e o artigo de “autoridade” produzem crase.
- **C) está errada:** Em “àquela”, fundem-se a preposição regida e o “a” inicial do demonstrativo.
- **D) está errada:** “Comparecer a” encontra o artigo plural de “as reuniões”.
- **Conceito cobrado:** Crase em contextos de regência.
- **Pegadinha usada:** Aplicar mecanicamente o acento antes de qualquer termo feminino ou infinitivo.
- **Como pensar para acertar:** Faça o teste da preposição e do artigo em cada alternativa.
- **Referência à apostila de estudo:** Dia 5 — crase e regência.

### Comentário da Questão 27

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** O período nada afirma sobre o desempenho necessário de todos os que não estudaram.
- **B) está errada:** A leitura de totalidade seria favorecida pela oração explicativa entre vírgulas.
- **C) está errada:** A estrutura não demonstra causalidade exclusiva.
- **D) está correta:** A oração sem vírgulas delimita quais candidatos recebem a afirmação de melhor desempenho.
- **Conceito cobrado:** Oração subordinada adjetiva restritiva.
- **Pegadinha usada:** Extrair causalidade ou universalidade de uma simples delimitação.
- **Como pensar para acertar:** Observe se a oração seleciona o referente ou apenas acrescenta informação.
- **Referência à apostila de estudo:** Dia 5 — sintaxe, orações adjetivas e pontuação.

### Comentário da Questão 28

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** A oração restritiva não seria isolada por vírgulas.
- **B) está errada:** Não há conector nem hipótese condicional.
- **C) está errada:** A estrutura não estabelece comparação entre grupos.
- **D) está correta:** As vírgulas atribuem valor explicativo à informação sobre o conjunto mencionado.
- **Conceito cobrado:** Oração subordinada adjetiva explicativa.
- **Pegadinha usada:** Ignorar que a pontuação altera o alcance da oração adjetiva.
- **Como pensar para acertar:** Compare o efeito semântico de retirar ou inserir as vírgulas.
- **Referência à apostila de estudo:** Dia 5 — sintaxe e pontuação de orações adjetivas.

### Comentário da Questão 29

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Coordena substantivo, infinitivo e novo sintagma nominal sem uniformidade.
- **B) está correta:** Os três itens coordenados são verbos no infinitivo com seus complementos.
- **C) está errada:** Mistura oração desenvolvida, infinitivo e substantivo.
- **D) está errada:** Combina substantivo, infinitivo e oração desenvolvida.
- **Conceito cobrado:** Paralelismo sintático.
- **Pegadinha usada:** Manter coerência temática, mas quebrar a forma gramatical da enumeração.
- **Como pensar para acertar:** Isole os itens coordenados e compare sua estrutura.
- **Referência à apostila de estudo:** Dia 5 — reescrita e paralelismo.

### Comentário da Questão 30

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** “O coordenador” e “a diretora” exercem função de sujeito, não de vocativo.
- **B) está errada:** Não há verbo expresso depois dos sujeitos; a vírgula sinaliza justamente sua elipse.
- **C) está correta:** O verbo “revisou” foi omitido nas duas últimas orações e recuperado da primeira.
- **D) está errada:** “A planilha” e “o parecer” são complementos do verbo elíptico, não apostos.
- **Conceito cobrado:** Vírgula vicária e elipse verbal.
- **Pegadinha usada:** Confundir omissão marcada por vírgula com separação indevida.
- **Como pensar para acertar:** Reponha o verbo da primeira oração nas estruturas seguintes.
- **Referência à apostila de estudo:** Dia 5 — pontuação e elipse.

### Comentário da Questão 31

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** “Haver” com sentido de existir é impessoal: “houve dois anos de testes”.
- **B) está errada:** A expressão plural de tempo não leva o verbo impessoal ao plural.
- **C) está errada:** O auxiliar de locução com “fazer” temporal também deve ficar no singular: “deve fazer”.
- **D) está correta:** “Fazer” com sentido de tempo decorrido é impessoal e permanece no singular.
- **Conceito cobrado:** Verbos impessoais em expressões temporais e existenciais.
- **Pegadinha usada:** Fazer o verbo concordar com a expressão plural posposta.
- **Como pensar para acertar:** Verifique se “fazer” indica tempo e se “haver” equivale a existir.
- **Referência à apostila de estudo:** Dia 5 — concordância e verbos impessoais.

### Comentário da Questão 32

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Na oração causal, usa-se “porque”.
- **B) está correta:** Com artigo, “porquê” é substantivo e significa “motivo”.
- **C) está errada:** A locução interrogativa exige “por que motivo”, com as duas palavras separadas.
- **D) está errada:** Em pergunta direta, usa-se “por que”.
- **Conceito cobrado:** Emprego de porque, por que e porquê.
- **Pegadinha usada:** Escolher a forma pela entonação, sem analisar função e posição.
- **Como pensar para acertar:** Teste “por qual motivo” e observe a presença de artigo.
- **Referência à apostila de estudo:** Dia 5 — ortografia e emprego dos porquês.

### Comentário da Questão 33

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A detecção adicional de inconsistências serve de premissa para manter o procedimento.
- **B) está errada:** A manutenção é defendida como conclusão, não como condição.
- **C) está errada:** Não se admite obstáculo nem se relativiza a utilidade da revisão.
- **D) está errada:** Embora haja contraste entre tipos de conferência no primeiro segmento, “portanto” liga a premissa à conclusão.
- **Conceito cobrado:** Conector conclusivo e progressão argumentativa.
- **Pegadinha usada:** Classificar o conector pela oposição interna do período, e não pela ligação que ele realiza.
- **Como pensar para acertar:** Identifique exatamente quais segmentos o conector relaciona.
- **Referência à apostila de estudo:** Dia 5 — conectores e conclusão.

### Comentário da Questão 34

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Na voz passiva, “pela equipe de auditoria” nomeia quem identificou.
- **B) está errada:** A expressão não caracteriza o substantivo “inconsistências”.
- **C) está errada:** O sujeito paciente é “As inconsistências”.
- **D) está errada:** Na forma ativa, “a equipe de auditoria” seria sujeito, não objeto indireto.
- **Conceito cobrado:** Voz passiva e agente da passiva.
- **Pegadinha usada:** Confundir o agente introduzido por preposição com objeto indireto.
- **Como pensar para acertar:** Converta o período para a voz ativa e identifique quem pratica a ação.
- **Referência à apostila de estudo:** Dia 5 — sintaxe e vozes verbais.

### Comentário da Questão 35

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** “Para verificar” expressa finalidade.
- **B) está errada:** “Embora” introduz concessão.
- **C) está correta:** O surgimento dos documentos explica por que a análise foi reaberta.
- **D) está errada:** “Desde que” introduz condição.
- **Conceito cobrado:** Relações adverbiais de causa, concessão, finalidade e condição.
- **Pegadinha usada:** Confundir a razão de uma ação com seu objetivo.
- **Como pensar para acertar:** Pergunte se a oração responde “por quê?”, “para quê?” ou “em que condição?”.
- **Referência à apostila de estudo:** Dia 5 — semântica dos conectores.

### Comentário da Questão 36

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** “Em 2025” situa a publicação da norma, não diretamente a alteração do procedimento.
- **B) está errada:** O verbo principal é “alterou”, cujo sujeito expresso é “A norma publicada em 2025”.
- **C) está correta:** A estrutura reduzida de particípio equivale a “que foi publicada em 2025” e restringe o referente.
- **D) está errada:** O segmento caracteriza “norma” e não completa nominalmente seu sentido.
- **Conceito cobrado:** Oração reduzida de particípio com valor adjetivo.
- **Pegadinha usada:** Associar todo marcador temporal ao verbo principal.
- **Como pensar para acertar:** Desenvolva a oração reduzida e observe qual termo ela modifica.
- **Referência à apostila de estudo:** Dia 5 — sintaxe do período e orações reduzidas.

### Comentário da Questão 37

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Os termos intercalados estão delimitados e a enumeração foi pontuada adequadamente.
- **B) está errada:** Faltam vírgulas entre os três itens enumerados.
- **C) está errada:** A vírgula separa indevidamente o sujeito “o candidato” do verbo “revisou”.
- **D) está errada:** Há vírgulas que fragmentam o adjunto e separam o verbo de seu complemento.
- **Conceito cobrado:** Pontuação de termos deslocados, intercalados e enumerados.
- **Pegadinha usada:** Pontuar por pausas de leitura sem respeitar a estrutura sintática.
- **Como pensar para acertar:** Marque primeiro a estrutura principal e depois isole apenas os termos acessórios.
- **Referência à apostila de estudo:** Dia 5 — pontuação e clareza.

### Comentário da Questão 38

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** O monitoramento não é apresentado como finalidade da primeira negação.
- **B) está errada:** A locução não introduz conclusão.
- **C) está correta:** “Tampouco” adiciona “não dispensa” a “não elimina”.
- **D) está errada:** O segundo predicado não explica a causa do primeiro.
- **Conceito cobrado:** Conector de adição negativa.
- **Pegadinha usada:** Inferir causa ou conclusão de uma simples coordenação negativa.
- **Como pensar para acertar:** Substitua “tampouco” por “também não”.
- **Referência à apostila de estudo:** Dia 5 — semântica e conectores.

### Comentário da Questão 39

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Abre assunto novo que o próprio trecho reconhece não ter desenvolvido.
- **B) está correta:** Retoma a tese e sintetiza medidas compatíveis com transparência e proteção de dados.
- **C) está errada:** Contradiz a tese ao defender publicidade irrestrita.
- **D) está errada:** Produz fechamento vago e sugere liberdade incompatível com critérios normativos.
- **Conceito cobrado:** Conclusão dissertativa.
- **Pegadinha usada:** Encerrar com tema novo, contradição ou generalidade.
- **Como pensar para acertar:** Verifique se a conclusão retoma a tese sem criar premissa inédita.
- **Referência à apostila de estudo:** Dia 5 — discursiva: conclusão e retomada da tese.

### Comentário da Questão 40

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** As palavras são acentuadas por regras distintas de paroxítonas terminadas em ditongo e em “l”.
- **B) está correta:** As três palavras têm a antepenúltima sílaba tônica e toda proparoxítona é acentuada.
- **C) está errada:** A forma normativa adjetiva “lógico” exige acento e tem tonicidade antepenúltima.
- **D) está errada:** “Técnico” é proparoxítono, não paroxítono terminado em “o”.
- **Conceito cobrado:** Regras de acentuação gráfica.
- **Pegadinha usada:** Agrupar palavras acentuadas como se obedecessem à mesma regra.
- **Como pensar para acertar:** Separe as sílabas e localize a sílaba tônica antes de aplicar a regra.
- **Referência à apostila de estudo:** Dia 5 — ortografia e acentuação.

### Comentário da Questão 41

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** `Como` cria causa e `portanto` cria conclusão, relações que o texto não estabelece entre as três ações.
- **B) está errada:** A correlação `ou... ou` transforma ações cumulativas em alternativas, e `por isso` acrescenta causalidade.
- **C) está errada:** `Embora` introduz concessão e `por essa razão` apresenta a não homologação como consequência necessária.
- **D) está correta:** `E` mantém a soma das duas ações, enquanto `entretanto` preserva a oposição de `contudo`.
- **Conceito cobrado:** Coordenação aditiva, oposição e equivalência semântica na reescrita.
- **Pegadinha usada:** Produzir frase gramaticalmente correta, mas trocar adição e contraste por causa, conclusão, alternância ou concessão.
- **Como pensar para acertar:** Marque a relação lógica em cada ponto de articulação e compare as duas relações na reescrita.
- **Referência à apostila de estudo:** Dia 5 — semântica e relações entre orações.

### Comentário da Questão 42

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** O padrão é “compatível com a norma” e “contrário ao entendimento”.
- **B) está errada:** “Acessível aos usuários” está correto, mas “passível” rege “de”: “passível de auditoria”.
- **C) está errada:** O padrão é “favorável ao recurso” e “avessa a nova instrução”.
- **D) está correta:** “Apto a” e “consciente de” regem adequadamente “ao exercício” e “das responsabilidades”.
- **Conceito cobrado:** Regência nominal de múltiplos nomes.
- **Pegadinha usada:** Inserir uma relação correta ao lado de outra incorreta na mesma alternativa.
- **Como pensar para acertar:** Valide separadamente cada nome e seu complemento.
- **Referência à apostila de estudo:** Dia 5 — regência nominal.

### Comentário da Questão 43

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** Em uma afirmação composta por `e`, uma parcela verdadeira não salva a proposição quando a outra parcela é falsa.
- **B) está correta:** A distinção entre anulação e revogação não valida a generalização de efeitos retroativos; o qualificador torna a opção incorreta.
- **C) está errada:** O trecho final integra a proposição e altera seu valor, ainda que apareça depois de uma formulação inicialmente correta.
- **D) está errada:** Inverter frases sem examinar conectivos e qualificadores aumenta o risco de responder à polaridade errada do comando.
- **Conceito cobrado:** Escopo de qualificadores, conjunção lógica e leitura de comando negativo.
- **Pegadinha usada:** Interromper a análise no fragmento verdadeiro e ignorar que `em ambos os casos` estende uma conclusão falsa aos dois institutos.
- **Como pensar para acertar:** Decomponha a opção, teste cada parcela e o alcance dos qualificadores, recomponha seu valor e só então releia o comando.
- **Referência à apostila de estudo:** Dia 5 — estratégia de prova, leitura do comando e eliminação.

### Comentário da Questão 44

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** Mantém a revisão em momento posterior ao erro e preserva a restrição temporal.
- **B) está errada:** “Apenas após” conserva o mesmo limite temporal.
- **C) está correta:** Afirma revisão anterior ao erro e inverte a ordem temporal original.
- **D) está errada:** A construção clivada enfatiza, sem alterar, o momento da revisão.
- **Conceito cobrado:** Escopo adverbial e reescrita semântica.
- **Pegadinha usada:** Ignorar a instrução sobre o alcance de “só” ou observar apenas palavras repetidas.
- **Como pensar para acertar:** Compare a ordem dos eventos e o elemento sobre o qual recai a restrição.
- **Referência à apostila de estudo:** Dia 5 — reescrita, escopo e marcadores temporais.

### Comentário da Questão 45

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** `Ainda que` conserva a concessão de `embora`, e `consequentemente` mantém o valor conclusivo de `por isso`.
- **B) está errada:** `Como` converte o orçamento reduzido em causa da conclusão, e `apesar disso` troca consequência por concessão.
- **C) está errada:** `Se` cria condição hipotética, enquanto `entretanto` apresenta oposição em lugar da consequência.
- **D) está errada:** `Porque` transforma o obstáculo em causa, e `ainda assim` não preserva a inferência que liga conclusão e manutenção do cronograma.
- **Conceito cobrado:** Concessão, consequência e preservação de relações lógicas em reescrita.
- **Pegadinha usada:** Manter o assunto e a correção gramatical, mas permutar as relações entre os segmentos.
- **Como pensar para acertar:** Analise os dois conectores separadamente e exija que a alternativa preserve ambos, não apenas o primeiro.
- **Referência à apostila de estudo:** Dia 5 — conectores concessivos.

### Comentário da Questão 46

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** Com “mais de um”, o verbo fica normalmente no singular: “enviou”.
- **B) está errada:** Na locução existencial, o auxiliar permanece no singular: “deve haver”.
- **C) está errada:** O padrão é “um ou outro candidato apresentou”, com núcleo e verbo no singular.
- **D) está correta:** A expressão “mais de um candidato” exige singular na ausência de reciprocidade ou repetição.
- **Conceito cobrado:** Casos especiais de concordância verbal.
- **Pegadinha usada:** Aplicar concordância puramente numérica a expressões de estrutura singular.
- **Como pensar para acertar:** Reconheça a expressão fixa e verifique se existe exceção contextual.
- **Referência à apostila de estudo:** Dia 5 — concordância e verbos impessoais.

### Comentário da Questão 47

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** `Dessas exigências` está no plural e encapsula duas obrigações, não somente o dever de informar.
- **B) está errada:** A primeira expressão é anafórica, e `a última delas` não retoma o efeito de reduzir usos incompatíveis.
- **C) está correta:** A primeira expressão resume as duas obrigações; `a última delas` seleciona a segunda, limitar o acesso.
- **D) está errada:** `Finalidade` é objeto de uma obrigação, não o conjunto retomado, e a última medida não é informar titulares.
- **Conceito cobrado:** Encapsulamento anafórico, antecedente composto e seleção referencial.
- **Pegadinha usada:** Ignorar número, ordem dos antecedentes e o alcance do demonstrativo `última`.
- **Como pensar para acertar:** Expanda cada expressão pelo possível antecedente e confirme concordância, posição e continuidade de sentido.
- **Referência à apostila de estudo:** Dia 5 — coesão referencial e progressão textual.

### Comentário da Questão 48

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** “Ratificação” confirma; não nomeia a correção do erro, e “retificar” não expressa a confirmação dos demais termos.
- **B) está correta:** “Retificação” corrige, “ratificar” confirma e “discrição” indica reserva ou prudência.
- **C) está errada:** “Ratificação” não corresponde à correção, e “descrição” não significa prudência no trato de dados.
- **D) está errada:** “Retificar” significa corrigir, e “descrição” significa ato de descrever, inadequado à ideia de reserva.
- **Conceito cobrado:** Parônimos e seleção lexical contextual.
- **Pegadinha usada:** Confundir palavras próximas na forma, mas diferentes no sentido.
- **Como pensar para acertar:** Substitua cada lacuna por uma definição curta antes de avaliar o conjunto.
- **Referência à apostila de estudo:** Dia 5 — semântica contextual e precisão vocabular.

### Comentário da Questão 49

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** `À medida que` introduz proporção e `portanto` conclusão, alterando as duas relações originais.
- **B) está errada:** `A menos que` cria condição excepcional e `por conseguinte` introduz consequência.
- **C) está correta:** `Porque` preserva a justificativa causal, e `mesmo assim` mantém a oposição concessiva de `ainda assim`.
- **D) está errada:** `Embora` é concessivo, não causal, e `por essa razão` converte a oposição em conclusão.
- **Conceito cobrado:** Equivalência contextual de conectores causais e concessivos.
- **Pegadinha usada:** Acertar a substituição de um conector e aceitar que o segundo altere a progressão argumentativa.
- **Como pensar para acertar:** Determine o valor de cada expressão destacada e valide o par completo na ordem em que aparece.
- **Referência à apostila de estudo:** Dia 5 — conectores de causa, condição, proporção e concessão.

### Comentário da Questão 50

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** Identifica data, quantidade e localização dos achados e distingue o registro factual da correção e do reteste recomendados.
- **B) está errada:** Afirma causa com certeza sem apresentar evidência e usa expressões vagas para ação e prazo.
- **C) está errada:** `Diversos pontos`, `relevantes` e `necessidade evidente` não permitem conferir achados nem separar dado de avaliação.
- **D) está errada:** Momento, causa e responsáveis permanecem indeterminados, e a providência não possui critério verificável.
- **Conceito cobrado:** Redação administrativa, verificabilidade e distinção entre constatação e recomendação.
- **Pegadinha usada:** Confundir tom categórico ou formal com objetividade e apresentar inferência causal como fato comprovado.
- **Como pensar para acertar:** Procure evidência identificável, delimitação do achado e marca explícita de que a providência é recomendada.
- **Referência à apostila de estudo:** Dia 5 — discursiva e redação objetiva.

## Temas de discursiva do Dia 5

Os temas abaixo não contam nas 50 questões objetivas. Use-os para treinar estrutura, tese, progressão argumentativa, coesão e conclusão objetiva.

### Tema discursivo 1 — Governo digital e proteção de dados

**Enunciado:** Em até 30 linhas, discorra sobre os desafios de conciliar transformação digital em órgãos públicos, eficiência administrativa e proteção de dados pessoais dos cidadãos.

**Modelo de estrutura:**
- Introdução: apresente a tensão entre eficiência digital e proteção de direitos.
- Desenvolvimento 1: explique ganhos de digitalização, interoperabilidade e redução de burocracia.
- Desenvolvimento 2: trate de finalidade, necessidade, segurança da informação, controle de acesso e transparência.
- Conclusão: proponha governança de dados, capacitação e controles técnicos como solução equilibrada.

### Tema discursivo 2 — Segurança da informação em autarquias profissionais

**Enunciado:** Em até 30 linhas, analise a importância de políticas de segurança da informação em entidade pública de fiscalização profissional que mantém dados de registrados, processos e documentos administrativos.

**Modelo de estrutura:**
- Introdução: situe a segurança da informação como requisito de continuidade, confiança e legalidade.
- Desenvolvimento 1: aborde confidencialidade, integridade, disponibilidade, backup e controle de acesso.
- Desenvolvimento 2: relacione riscos de vazamento, indisponibilidade e alteração indevida a danos ao serviço público.
- Conclusão: defenda política formal, gestão de incidentes, capacitação e revisão periódica.

### Critérios de autocorreção da discursiva

- **Abordagem do tema:** respondeu exatamente ao que foi perguntado, sem fuga temática.
- **Tese:** apresentou posição clara já no início.
- **Desenvolvimento:** usou argumentos técnicos e exemplos de órgão público.
- **Coesão:** conectou ideias com progressão lógica, sem saltos.
- **Estrutura textual:** respeitou introdução, desenvolvimento e conclusão.
- **Gramática e pontuação:** evitou períodos longos demais, concordância incorreta e vírgula separando sujeito de verbo.
- **Conclusão:** retomou a tese e indicou solução compatível com o problema.
- **Erros que derrubam nota:** fuga do tema, ausência de tese, texto em tópicos, excesso de generalidade, contradição e erros gramaticais recorrentes.

### Comentários das questões extras de revisão fixa do Dia 5

#### Comentário Extra Dia 5.1

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** O Regimento organiza o conselho regional e não pode ampliar o campo profissional fixado em lei.
- **B) está errada:** Resoluções complementam a disciplina dentro da competência normativa, mas não prevalecem sobre lei e decreto.
- **C) está correta:** A alternativa respeita a função e a hierarquia de cada espécie normativa.
- **D) está errada:** O decreto regulamenta a execução da lei profissional e não se limita à organização interna do CRA-PR.
- **Conceito cobrado:** Articulação entre lei, decreto, resoluções e regimento.
- **Pegadinha usada:** Confundir posterioridade ou detalhamento com superioridade hierárquica.
- **Como pensar para acertar:** Identifique o fundamento legal e a função complementar de cada ato.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.2

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** A atuação fiscalizatória não depende de dano patrimonial comprovado pelo cliente.
- **B) está errada:** O possível uso indevido pode existir antes da celebração de contrato.
- **C) está errada:** Registro posterior não torna automaticamente regular uma conduta praticada antes da habilitação.
- **D) está correta:** A apresentação pública como registrado exige verificação de habilitação e de uso regular da condição profissional.
- **Conceito cobrado:** Uso de título e regularidade do exercício profissional.
- **Pegadinha usada:** Condicionar a irregularidade a contrato, prejuízo ou regularização posterior.
- **Como pensar para acertar:** Compare a condição apresentada no anúncio com a habilitação existente naquele momento.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.3

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** A fiscalização regional ordinária cabe aos CRAs em suas jurisdições; o CFA atua no plano nacional e normativo.
- **B) está correta:** Reúne os critérios material e territorial da atuação do CRA.
- **C) está errada:** A mera condição empresarial não basta; a atividade deve guardar relação com o campo fiscalizado.
- **D) está errada:** A competência não decorre apenas do domicílio do denunciante.
- **Conceito cobrado:** Campo e competência territorial de fiscalização.
- **Pegadinha usada:** Universalizar a competência do CFA ou do conselho regional.
- **Como pensar para acertar:** Verifique simultaneamente a matéria da atividade e a jurisdição competente.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.4

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A estrutura confirmada do Código reúne deveres, direitos, infrações e critérios de fixação e gradação das sanções; o rito processual possui regulamentação própria.
- **B) está errada:** Anuidades e cobrança não constituem o núcleo do Código de Ética.
- **C) está errada:** A RN CFA nº 651/2024, e não a nº 671/2025, é associada ao Regimento Interno no material.
- **D) está errada:** Memorização isolada não permite resolver situações éticas concretas.
- **Conceito cobrado:** Conteúdo e método de estudo do Código de Ética.
- **Pegadinha usada:** Trocar as resoluções ou reduzir o estudo à numeração de artigos.
- **Como pensar para acertar:** Associe cada norma a seu objeto e aplique a regra à conduta descrita.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.5

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Conselho profissional não se limita à defesa econômica corporativa.
- **B) está errada:** A fiscalização administrativa não substitui a função jurisdicional em todo conflito.
- **C) está errada:** Definição autônoma de currículos universitários não é a finalidade indicada.
- **D) está correta:** A proteção social e a regularidade do exercício justificam a função fiscalizatória.
- **Conceito cobrado:** Finalidade dos conselhos profissionais.
- **Pegadinha usada:** Equiparar conselho a associação privada, tribunal ou instituição de ensino.
- **Como pensar para acertar:** Relacione a fiscalização ao interesse público protegido.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.6

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Autorização para usar o registro não substitui a atuação técnica efetiva.
- **B) está correta:** Responsabilidade técnica exige participação real e regular na atividade assumida.
- **C) está errada:** A pessoa jurídica não elimina a necessidade de profissional habilitado quando a responsabilidade técnica é exigível.
- **D) está errada:** A responsabilidade acompanha a atividade exercida sob a indicação, e não apenas a assinatura inicial.
- **Conceito cobrado:** Efetividade da responsabilidade técnica.
- **Pegadinha usada:** Tratar indicação profissional como cessão formal de nome ou registro.
- **Como pensar para acertar:** Procure evidência de acompanhamento, decisão técnica e atuação concreta.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.7

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Novidade cronológica, sem pertinência ao edital e ato oficial, não basta para trocar a base.
- **B) está errada:** A RN CFA nº 651/2024 é relacionada ao Regimento Interno, não ao novo Código de Ética.
- **C) está correta:** O material fundamenta a escolha no edital retificado e na fonte oficial de vigência.
- **D) está errada:** Normas sucessivas não se aplicam cumulativamente de modo automático aos mesmos fatos.
- **Conceito cobrado:** Seleção da norma vigente indicada no edital.
- **Pegadinha usada:** Aplicar automaticamente a norma numericamente mais recente ou acumular textos sucessivos.
- **Como pensar para acertar:** Confira edital, retificação, objeto da resolução e informação oficial de vigência.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.8

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** A decomposição do caso evita confundir conduta, sujeito, competência e fundamento.
- **B) está errada:** A sanção é consequência da análise normativa, não seu ponto de partida.
- **C) está errada:** CFA e CRA possuem papéis distintos no sistema.
- **D) está errada:** Ressalvas e quantificadores alteram o alcance da norma e da alternativa.
- **Conceito cobrado:** Método de resolução de casos de legislação específica.
- **Pegadinha usada:** Decidir por severidade, palavra-chave ou autoridade genérica.
- **Como pensar para acertar:** Monte a sequência fato, sujeito, competência, regra e consequência.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.9

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Nem toda infração conduz à penalidade máxima.
- **B) está errada:** Prova documental não elimina, por si só, as garantias do processo e da defesa.
- **C) está errada:** Proporcionalidade orienta a escolha dentro da lei; não autoriza criar sanção.
- **D) está correta:** Penalidade requer previsão, procedimento e adequação à infração apurada.
- **Conceito cobrado:** Legalidade, processo e proporcionalidade das sanções.
- **Pegadinha usada:** Transformar rigor em automatismo ou em poder sancionador sem limite.
- **Como pensar para acertar:** Verifique previsão normativa, competência, procedimento e gradação.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.10

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** O Regimento não se limita a contribuições nem à cobrança.
- **B) está errada:** A definição originária do campo profissional pertence à base legal da profissão.
- **C) está errada:** Deveres éticos e sanções remetem ao Código de Ética vigente.
- **D) está correta:** Estrutura, órgãos, competências e funcionamento são matérias típicas do Regimento Interno.
- **Conceito cobrado:** Objeto do Regimento Interno do CRA-PR.
- **Pegadinha usada:** Misturar organização institucional, campo profissional e disciplina ética.
- **Como pensar para acertar:** Associe “quem faz o quê dentro do CRA-PR” ao Regimento.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.11

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A verificação fiscalizatória não depende de decisão definitiva de órgão de defesa do consumidor.
- **B) está correta:** A apresentação como registrado sem possuir essa condição justifica apuração pelo órgão competente.
- **C) está errada:** O anúncio pode ser relevante antes mesmo de gerar contrato remunerado.
- **D) está errada:** Registro posterior não convalida automaticamente a apresentação anterior como habilitado.
- **Conceito cobrado:** Publicidade e uso indevido de condição profissional.
- **Pegadinha usada:** Exigir contrato, dano ou decisão de terceiro como condição para fiscalizar.
- **Como pensar para acertar:** Compare o conteúdo objetivo do anúncio com a situação registral existente.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.12

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Regulamentar não autoriza o decreto a ultrapassar os limites da lei.
- **B) está correta:** O decreto detalha a execução da lei sem revogá-la nem superá-la hierarquicamente.
- **C) está errada:** A edição do regulamento não elimina a lei regulamentada.
- **D) está errada:** O Decreto nº 61.934/1967 não é regimento interno do CRA-PR.
- **Conceito cobrado:** Relação entre lei e decreto regulamentador.
- **Pegadinha usada:** Confundir detalhamento regulamentar com inovação ilimitada ou revogação.
- **Como pensar para acertar:** Preserve a lei como fundamento e situe o decreto como ato de execução.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.13

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Separa corretamente formação acadêmica de situação financeira perante o conselho.
- **B) está errada:** Consequências dependem de fundamento normativo e das garantias aplicáveis.
- **C) está errada:** Conselho profissional não cancela diploma nem apaga formação acadêmica por inadimplência.
- **D) está errada:** Vínculo acadêmico, por si só, não extingue contribuição regularmente devida.
- **Conceito cobrado:** Distinção entre formação, registro e regularidade financeira.
- **Pegadinha usada:** Tratar diploma, registro e anuidade como uma única condição.
- **Como pensar para acertar:** Identifique qual relação jurídica cada consequência pode atingir.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.14

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Comentário didático e ato oficial não possuem a mesma autoridade normativa.
- **B) está errada:** Resumo auxilia o estudo, mas não prevalece sobre publicação oficial divergente.
- **C) está correta:** Texto oficial e vigência são indispensáveis para detalhes literais como prazo, rito e penalidade.
- **D) está errada:** Número ou data mais recente não substitui automaticamente a base indicada no edital.
- **Conceito cobrado:** Uso de fontes oficiais no estudo normativo.
- **Pegadinha usada:** Tomar material secundário ou novidade cronológica como fonte suficiente.
- **Como pensar para acertar:** Confirme texto, vigência e pertinência ao edital antes de memorizar detalhe.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.15

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A matéria institucional indicada é objeto do Regimento aprovado pela RN CFA nº 651/2024.
- **B) está errada:** A lei profissional não é a fonte mais direta para a estrutura interna específica do CRA-PR.
- **C) está errada:** O decreto regulamenta a lei da profissão, mas não substitui o Regimento regional.
- **D) está errada:** O Código de Ética disciplina condutas, deveres, vedações e sanções éticas.
- **Conceito cobrado:** Identificação da fonte normativa pela matéria.
- **Pegadinha usada:** Escolher a norma mais ampla quando o comando pede organização interna.
- **Como pensar para acertar:** Associe sede, órgãos e funcionamento ao ato regimental.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.16

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Norma interna regional não pode ampliar por conta própria matéria delimitada em lei federal.
- **B) está errada:** Posterioridade e especialidade não tornam resolução hierarquicamente superior à lei.
- **C) está correta:** Cada ato exerce função própria dentro de uma relação de competência e subordinação normativa.
- **D) está errada:** O decreto regulamenta a lei e não a revoga nem substitui.
- **Conceito cobrado:** Hierarquia e função das fontes da legislação profissional.
- **Pegadinha usada:** Confundir detalhamento normativo com poder para contrariar ou substituir a lei.
- **Como pensar para acertar:** Ordene as fontes e identifique o objeto legítimo de cada uma antes de aplicar seus detalhes.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.17

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** O CFA coordena e normatiza nacionalmente, mas a execução fiscalizatória cotidiana cabe ao Regional competente.
- **B) está correta:** A alternativa preserva a divisão entre atuação nacional do CFA e atuação regional do CRA-PR.
- **C) está errada:** A validade do sistema não elimina a distribuição territorial de competências entre os CRAs.
- **D) está errada:** CNPJ não afasta a análise da atividade profissional explorada nem eventual registro exigível.
- **Conceito cobrado:** Competência nacional do CFA e atuação regional do CRA-PR.
- **Pegadinha usada:** Trocar coordenação nacional por fiscalização local ou ignorar a jurisdição.
- **Como pensar para acertar:** Localize o fato e separe quem edita normas gerais de quem registra e fiscaliza na região.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.18

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** Responsabilidade técnica pressupõe atuação real; emprestar nome ou assinar trabalho alheio pode violar dever profissional.
- **B) está errada:** Documento formal não substitui orientação, supervisão e participação técnica efetivas.
- **C) está errada:** A concordância privada não transforma conduta incompatível com a disciplina profissional em regular.
- **D) está errada:** A fiscalização administrativa não depende de condenação judicial prévia para verificar regularidade e conduta.
- **Conceito cobrado:** Responsabilidade técnica e uso indevido do registro.
- **Pegadinha usada:** Confundir assinatura ou autorização formal com efetivo exercício da responsabilidade técnica.
- **Como pensar para acertar:** Verifique quem realmente orientou, supervisionou e assumiu tecnicamente o trabalho.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.19

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** Vantagem econômica não constitui, por si, justa causa para quebrar o sigilo profissional.
- **B) está errada:** A retirada do nome não autoriza divulgação de conteúdo confidencial quando a informação continua protegida.
- **C) está errada:** Transferir os dados a terceiro já representa revelação e não desloca a responsabilidade ética.
- **D) está correta:** Sem hipótese legal ou justa causa, prevalece o dever de preservar a informação conhecida no exercício profissional.
- **Conceito cobrado:** Sigilo profissional e suas exceções.
- **Pegadinha usada:** Criar exceção comercial ou indireta para contornar o dever de confidencialidade.
- **Como pensar para acertar:** Procure fundamento jurídico concreto para a revelação; ausente ele, mantenha o sigilo.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

#### Comentário Extra Dia 5.20

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** O Regulamento de Registro não concentra estrutura institucional e disciplina ética.
- **B) está errada:** A alternativa troca os objetos: órgãos internos pertencem ao Regimento; sigilo, ao Código de Ética.
- **C) está correta:** A RN nº 651/2024 aprova o Regimento do CRA-PR, e a RN nº 671/2025 disciplina condutas éticas como o sigilo.
- **D) está errada:** Regimento e Código possuem funções diferentes e não são intercambiáveis.
- **Conceito cobrado:** Distinção entre Regimento Interno e Código de Ética.
- **Pegadinha usada:** Associar norma verdadeira ao objeto errado ou fundir disciplinas distintas.
- **Como pensar para acertar:** Classifique primeiro se o caso trata de estrutura do Conselho ou de conduta profissional.
- **Referência à apostila de estudo:** [Dia 5 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d5-b4).

---

# Dia 6 — Administração Pública, RLM e Revisão

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões principais

### Questão 1
**Nível: Médio**

Em licitação para solução de tecnologia, a unidade requisitante indica determinada marca como única aceitável, mas não apresenta estudo que demonstre incompatibilidade das demais opções. À luz dos princípios administrativos, a providência adequada é:

A) manter a marca e classificar a justificativa como sigilosa, para evitar questionamentos de concorrentes.
B) aceitar a escolha por se tratar de decisão discricionária da área técnica, ainda que não haja motivação objetiva.
C) converter automaticamente o caso em inexigibilidade, porque produtos tecnológicos são presumidamente exclusivos.
D) exigir justificativa técnica objetiva e pertinente ao interesse público, afastando direcionamento indevido.

### Questão 2
**Nível: Médio**

Assinale a alternativa que reúne apenas os princípios expressos no caput do art. 37 da Constituição Federal.

A) Legalidade, supremacia do interesse público, publicidade, continuidade e eficiência.
B) Legalidade, pessoalidade, moralidade, transparência e economicidade.
C) Legalidade, impessoalidade, moralidade, publicidade e eficiência.
D) Impessoalidade, autotutela, motivação, publicidade e eficiência.

### Questão 3
**Nível: Médio**

Assinale a alternativa incorreta sobre Administração Direta e Indireta.

A) Autarquias são órgãos despersonalizados da Administração Direta, embora possuam autonomia financeira.
B) Autarquias, empresas públicas e sociedades de economia mista integram a Administração Indireta.
C) Secretarias e ministérios são órgãos sem personalidade jurídica própria.
D) Entidades da Administração Indireta possuem personalidade jurídica própria.

### Questão 4
**Nível: Médio**

O CRA-PR exerce registro e fiscalização profissional, possui personalidade jurídica de direito público e autonomia técnica, administrativa e financeira. Essa descrição o aproxima, em regra, de:

A) empresa pública prestadora de serviço econômico em regime privado.
B) órgão da Administração Direta estadual sem personalidade própria.
C) autarquia corporativa ou entidade de fiscalização profissional.
D) associação civil privada mantida apenas por contribuições voluntárias.

### Questão 5
**Nível: Médio**

Analise as assertivas sobre atos administrativos.

I. Competência, finalidade, forma, motivo e objeto são elementos clássicos.
II. A presunção de legitimidade permite que o ato produza efeitos até eventual invalidação.
III. A autoexecutoriedade está presente em todo ato administrativo, sem exceção.

Está correto apenas o que se afirma em:

A) I, II e III.
B) II e III.
C) I e III.
D) I e II.

### Questão 6
**Nível: Médio**

Assinale a alternativa incorreta acerca dos elementos do ato administrativo.

A) Finalidade relaciona-se ao interesse público que deve orientar o ato.
B) Motivo corresponde aos pressupostos de fato e de direito da decisão.
C) Objeto é o efeito jurídico imediato produzido pelo ato.
D) Competência transfere-se definitivamente por acordo informal, sem autorização legal.

### Questão 7
**Nível: Médio**

Uma autoridade remove servidor para local distante com o propósito real de puni-lo por crítica legítima, embora declare genericamente “necessidade do serviço”. O vício mais evidente recai sobre:

A) a forma, porque toda remoção exige decisão judicial.
B) a finalidade, pois a competência foi usada para perseguição pessoal.
C) o motivo, apenas porque fatos administrativos não admitem avaliação.
D) o objeto, porque remoção nunca pode alterar a lotação.

### Questão 8
**Nível: Médio**

Para contratar serviço comum de suporte técnico, com especificações usuais de mercado e disputa por lances, a modalidade em regra mais compatível é:

A) leilão.
B) pregão.
C) diálogo competitivo.
D) concurso.

### Questão 9
**Nível: Médio**

Assinale a alternativa incorreta sobre contratação direta.

A) Na inexigibilidade, a competição é inviável e essa circunstância deve ser demonstrada.
B) Na dispensa, a competição pode ser viável, mas a lei autoriza a contratação direta em hipótese específica.
C) Dispensa e inexigibilidade são equivalentes, pois em ambas a Administração escolhe livremente não licitar.
D) A contratação direta continua exigindo processo, justificativa, motivação e controle.

### Questão 10
**Nível: Médio**

A Administração precisa contratar solução inovadora e complexa, mas ainda não consegue definir os meios técnicos aptos a atender sua necessidade. Pretende dialogar com licitantes previamente selecionados antes da apresentação das propostas finais. A modalidade descrita é:

A) concorrência com critério de maior lance.
B) diálogo competitivo.
C) concurso.
D) leilão.

### Questão 11
**Nível: Médio**

Analise as assertivas sobre o julgamento em licitações.

I. O edital vincula a Administração e os licitantes.
II. Os critérios de julgamento devem ser previamente definidos.
III. Após conhecer as propostas, a comissão pode mudar o critério para escolher a solução que considere melhor.

Está correto apenas o que se afirma em:

A) I e III.
B) II e III.
C) I e II.
D) I, II e III.

### Questão 12
**Nível: Médio**

Assinale a alternativa incorreta a respeito dos critérios de julgamento.

A) O critério pode ser escolhido depois da abertura das propostas, desde que a decisão seja motivada.
B) Técnica e preço pode ponderar qualidade técnica e valor econômico quando cabível.
C) Menor preço é possível quando o objeto admite comparação objetiva e atende aos requisitos definidos.
D) Maior desconto pode incidir sobre parâmetro previamente estabelecido no edital.

### Questão 13
**Nível: Médio**

Durante serviço, veículo oficial conduzido por agente público colide com automóvel particular. Para a responsabilidade objetiva do Estado por esse ato comissivo, a vítima deve demonstrar, em regra:

A) contrato anterior com a Administração e inadimplemento.
B) conduta estatal, dano e nexo causal.
C) dolo específico do agente e condenação penal.
D) culpa do serviço, ainda que não exista dano comprovado.

### Questão 14
**Nível: Médio**

Assinale a alternativa incorreta sobre a responsabilidade civil objetiva do Estado.

A) O dano é presumido e dispensa demonstração pela vítima.
B) Caso fortuito ou força maior podem excluir a responsabilidade quando rompem o nexo.
C) Culpa concorrente da vítima pode reduzir a indenização.
D) Culpa exclusiva da vítima pode romper o nexo causal.

### Questão 15
**Nível: Médio**

Uma estrutura pública apresenta risco conhecido, mas o órgão deixa de realizar manutenção que lhe competia. Na análise da omissão estatal, deve-se verificar especialmente:

A) se qualquer dano ocorreu em propriedade pública, o que basta para indenização automática.
B) se existe contrato administrativo entre o órgão e a vítima.
C) se houve condenação disciplinar prévia do servidor responsável.
D) o dever específico de agir, a possibilidade de atuação, a falha e o nexo com o dano.

### Questão 16
**Nível: Médio**

A respeito da improbidade administrativa, assinale a alternativa correta.

A) Toda irregularidade administrativa configura improbidade, ainda que puramente formal.
B) Nem toda ilegalidade é improbidade; exige-se enquadramento legal e o elemento subjetivo previsto.
C) Improbidade é matéria exclusivamente penal e pressupõe condenação criminal.
D) Somente enriquecimento ilícito pode constituir improbidade.

### Questão 17
**Nível: Médio**

Analise as assertivas.

I. Atos de improbidade podem envolver enriquecimento ilícito, lesão ao erário ou violação de princípios, conforme a lei.
II. Divergência técnica razoável caracteriza automaticamente improbidade.
III. A responsabilização deve observar devido processo e defesa.

Está correto apenas o que se afirma em:

A) I e III.
B) I, II e III.
C) I e II.
D) II e III.

### Questão 18
**Nível: Médio**

A Administração identifica ilegalidade em ato que ela própria praticou e decide invalidá-lo, respeitados os direitos processuais pertinentes. Essa atuação decorre principalmente do poder de:

A) autotutela.
B) polícia judiciária.
C) hierarquia legislativa.
D) tutela jurisdicional.

### Questão 19
**Nível: Médio**

Assinale a alternativa incorreta sobre o controle da Administração Pública.

A) O Legislativo exerce controle externo com auxílio dos tribunais de contas, nos termos constitucionais.
B) O Judiciário pode controlar a legalidade de atos administrativos.
C) A própria Administração exerce controle interno sobre seus atos e agentes.
D) O Judiciário pode substituir livremente o administrador na escolha de mérito entre opções legais igualmente válidas.

### Questão 20
**Nível: Médio**

Diante de pedido de acesso a documentos administrativos, a premissa correta é:

A) todo processo é sigiloso até autorização judicial.
B) o acesso depende sempre da demonstração de interesse jurídico individual.
C) a publicidade é regra e o sigilo, exceção que precisa de fundamento legal.
D) a Administração pode negar o pedido sem motivação quando o atendimento exigir trabalho adicional.

### Questão 21
**Nível: Difícil**

Um cidadão pede cópia de planilha usada em política pública. O arquivo contém resultados estatísticos de interesse coletivo, mas também CPF, telefone e endereço dos atendidos. A solução mais compatível com LAI e LGPD é:

A) negar integralmente o acesso, porque a presença de qualquer dado pessoal torna todo o documento sigiloso.
B) fornecer as informações públicas cabíveis com anonimização ou ocultação dos dados pessoais desnecessários, motivando eventuais restrições.
C) publicar a planilha integral, pois dados mantidos pelo Estado são necessariamente públicos.
D) exigir consentimento individual de todos os titulares antes de divulgar até mesmo os dados estatísticos agregados.

### Questão 22
**Nível: Difícil**

No exercício regular do poder de polícia, uma autarquia constata infração e aplica restrição prevista em lei após procedimento próprio. A conclusão correta é:

A) a existência de competência legal elimina contraditório e ampla defesa em qualquer sanção aplicada no exercício do poder de polícia.
B) a natureza preventiva do poder de polícia dispensa motivação e proporcionalidade quando a restrição estiver prevista em ato interno.
C) toda restrição administrativa depende de condenação penal anterior, ainda que a lei atribua competência sancionadora à autarquia.
D) a Administração pode restringir direitos no interesse público, com base legal e respeito às garantias.

### Questão 23
**Nível: Difícil**

Em processo administrativo sancionador, a comissão conclui a instrução sem ouvir o interessado e propõe aplicação imediata de multa. Qual sequência corrige o vício?

A) aplicar a multa, publicar o resultado e abrir defesa apenas se houver recurso.
B) colher defesa informal depois da decisão, sem reabrir a instrução.
C) dar ciência da imputação, assegurar defesa e produção pertinente de provas e, depois, proferir decisão motivada.
D) submeter a proposta diretamente ao Judiciário, que substituirá o processo administrativo.

### Questão 24
**Nível: Difícil**

Uma autoridade possui competência para decidir, mas indefere pedido usando apenas a frase “por interesse público”, sem indicar fatos nem fundamento jurídico. Nesse caso, a motivação é relevante porque:

A) expõe as razões de fato e de direito, permitindo controlar a legalidade e a coerência da decisão.
B) converte automaticamente uma decisão vinculada em discricionária.
C) substitui a competência e permite que qualquer servidor assine o ato.
D) torna desnecessária a existência de motivo verdadeiro, desde que o texto seja formal.

### Questão 25
**Nível: Difícil**

Considere a proposição: “Se o edital é regular, então os critérios são públicos e objetivos”. Sua negação lógica é:

A) O edital não é regular e os critérios não são públicos nem objetivos.
B) O edital é regular e algum critério não é público ou não é objetivo.
C) Se os critérios não são públicos ou não são objetivos, então o edital não é regular.
D) O edital não é regular ou os critérios são públicos e objetivos.

### Questão 26
**Nível: Difícil**

A negação de “Todo ato válido foi motivado ou algum recurso foi provido” é:

A) Nenhum ato válido foi motivado ou algum recurso não foi provido.
B) Algum ato válido não foi motivado e nenhum recurso foi provido.
C) Algum ato válido foi motivado e todo recurso foi improvido.
D) Nenhum ato válido foi motivado ou nenhum recurso foi provido.

### Questão 27
**Nível: Difícil**

Em um grupo, 92 pessoas usam o sistema A, 71 usam o sistema B e 38 usam ambos. Quantas usam exatamente um dos dois sistemas?

A) 87.
B) 49.
C) 54.
D) 125.

### Questão 28
**Nível: Difícil**

Seis servidores, com produtividade uniforme, analisam 360 processos em 5 dias. Em nova etapa, dez servidores trabalharão 8 dias, mas com produtividade individual equivalente a 75% da anterior. Quantos processos serão analisados?

A) 900.
B) 600.
C) 720.
D) 576.

### Questão 29
**Nível: Difícil**

Um equipamento de R$ 7.500,00 sofre aumento de 12% e, sobre o preço reajustado, recebe desconto de 10%. O preço final é:

A) R$ 7.650,00.
B) R$ 7.500,00.
C) R$ 7.560,00.
D) R$ 8.250,00.

### Questão 30
**Nível: Difícil**

Um serviço teve primeiro acréscimo de 25% sobre o preço original e, depois, desconto de 15% sobre o valor reajustado, passando a custar R$ 4.250,00. O preço original era:

A) R$ 4.000,00.
B) R$ 3.612,50.
C) R$ 4.250,00.
D) R$ 5.000,00.

### Questão 31
**Nível: Difícil**

Quatro técnicos resolvem 160 chamados em 5 horas. Em outro turno, cinco técnicos trabalham 6 horas, mas cada um produz apenas 80% do ritmo anterior. A produção esperada é:

A) 240 chamados.
B) 160 chamados.
C) 200 chamados.
D) 192 chamados.

### Questão 32
**Nível: Difícil**

Uma progressão aritmética tem primeiro termo 7 e razão 4. A soma dos 20 primeiros termos é:

A) 83.
B) 830.
C) 940.
D) 900.

### Questão 33
**Nível: Difícil**

Em uma progressão geométrica, o primeiro termo é 3 e a razão é 2. A soma dos oito primeiros termos é:

A) 384.
B) 765.
C) 768.
D) 1.533.

### Questão 34
**Nível: Difícil**

Uma urna contém 5 crachás azuis e 3 vermelhos. Três crachás são retirados simultaneamente. A probabilidade de saírem exatamente dois azuis e um vermelho é:

A) 3/8.
B) 5/14.
C) 15/28.
D) 9/28.

### Questão 35
**Nível: Difícil**

Entre 10 servidores, 2 são analistas. Três servidores distintos são sorteados, sem reposição. A probabilidade de o grupo conter pelo menos um analista é:

A) 8/15.
B) 2/5.
C) 7/15.
D) 1/5.

### Questão 36
**Nível: Difícil**

A negação de “O relatório foi entregue e o protocolo foi gerado ou a assinatura foi validada”, considerando a estrutura “R e (P ou A)”, é:

A) O relatório não foi entregue ou (o protocolo não foi gerado e a assinatura não foi validada).
B) O relatório não foi entregue ou o protocolo não foi gerado ou a assinatura não foi validada.
C) (O relatório não foi entregue e o protocolo não foi gerado) ou a assinatura não foi validada.
D) O relatório foi entregue e o protocolo não foi gerado e a assinatura não foi validada.

### Questão 37
**Nível: Difícil**

São verdadeiras as proposições: “Se existe backup íntegro, então a verificação termina sem erro” e “Se a verificação termina sem erro, então a restauração é possível”. Sabendo que a restauração não é possível, conclui-se validamente que:

A) a primeira condicional é falsa.
B) existe backup íntegro, mas não foi usado.
C) não existe backup íntegro.
D) a verificação terminou sem erro.

### Questão 38
**Nível: Difícil**

Para proposições simples P, Q e R, em quantas das oito valorações possíveis a expressão `(P → Q) e (Q → R)` é verdadeira?

A) 6.
B) 3.
C) 5.
D) 4.

### Questão 39
**Nível: Difícil**

Em 200 servidores, 110 usam A, 90 usam B e 70 usam C. Usam A e B, 45; A e C, 30; B e C, 25; e os três sistemas, 15. Quantos usam pelo menos um dos sistemas?

A) 170.
B) 200.
C) 155.
D) 185.

### Questão 40
**Nível: Difícil**

Uma unidade planeja duas contratações previsíveis e de mesma natureza, mas propõe separá-las artificialmente para que cada valor se enquadre em hipótese de dispensa. Assinale a alternativa incorreta.

A) O planejamento deve considerar a necessidade global e a natureza dos objetos.
B) O fracionamento é legítimo sempre que cada processo isolado permanecer abaixo do limite legal.
C) A contratação direta não elimina motivação, justificativa e controle.
D) O procedimento deve preservar isonomia, planejamento e finalidade pública.

### Questão 41
**Nível: Muito difícil**

Edital para serviço comum fixa requisitos técnicos mínimos e menor preço como critério. Após a abertura, a proposta de menor preço descumpre requisito essencial, e a comissão cogita dispensá-lo apenas para preservar essa proposta. A solução juridicamente mais adequada é:

A) ignorar o requisito essencial, pois o menor preço sempre prevalece sobre especificações técnicas previamente divulgadas.
B) aplicar o edital; se o requisito for ilegal, corrigir o procedimento impessoalmente, não dispensá-lo só para um licitante.
C) alterar retroativamente o edital para dispensar o requisito apenas nessa proposta, mantendo os atos praticados e afastando nova publicidade.
D) classificar a proposta por economicidade mesmo sem atendimento ao objeto, substituindo o julgamento objetivo por conveniência da comissão.

### Questão 42
**Nível: Muito difícil**

Veículo oficial em serviço causa dano a particular. A prova demonstra nexo causal, culpa concorrente da vítima e culpa do agente público. A alternativa correta é:

A) a responsabilidade pode ser objetiva; a culpa concorrente atenua a indenização, e o regresso exige dolo ou culpa.
B) A culpa concorrente elimina necessariamente toda responsabilidade do Estado, embora preserve ação regressiva automática contra o agente.
C) A responsabilidade objetiva torna dispensáveis a prova do dano e do nexo causal e impede considerar qualquer causa concorrente.
D) O Estado somente indeniza depois da condenação pessoal do agente, mas pode exercer regresso sem demonstrar dolo ou culpa.

### Questão 43
**Nível: Muito difícil**

A Administração descobre que licença foi concedida por autoridade absolutamente incompetente. Além disso, a licença tornou-se inconveniente à política pública atual. Para desfazer o ato, deve:

A) revogá-lo exclusivamente por conveniência, pois o mérito absorve qualquer ilegalidade.
B) anulá-lo pelo vício, observadas as garantias; revogação não encobre ilegalidade.
C) convalidá-lo obrigatoriamente e, em seguida, revogá-lo, independentemente da natureza do vício.
D) aguardar decisão judicial, porque a Administração não pode invalidar ato próprio favorável.

### Questão 44
**Nível: Muito difícil**

A lei permite multa entre R$ 2.000,00 e R$ 20.000,00 conforme gravidade e circunstâncias. A autoridade aplica o máximo para retaliar crítica do administrado e usa motivação genérica. A conclusão correta é:

A) a discricionariedade não autoriza desvio de finalidade e exige motivação conforme os critérios legais.
B) a existência de faixa legal torna a escolha do valor imune ao controle de finalidade, motivação e proporcionalidade.
C) o valor máximo é sempre válido quando está dentro da faixa, ainda que a motivação não relacione gravidade e circunstâncias.
D) em ato discricionário, o controle pode alcançar apenas a competência da autoridade, nunca finalidade, motivo ou proporcionalidade.

### Questão 45
**Nível: Muito difícil**

Um setor recebeu 240 processos no primeiro mês e concluiu 60%, restando 96 pendentes. No mês seguinte, recebeu 25% mais processos e concluiu inicialmente 72%; depois, concluiu 25% dos que ainda estavam pendentes. Quantos permaneceram pendentes e qual foi a redução percentual em relação ao fim do primeiro mês?

A) 84 processos e 12,5%.
B) 72 processos e 25%.
C) 63 processos e 25%.
D) 63 processos e 34,375%.

### Questão 46
**Nível: Muito difícil**

Três servidores analisam 90 processos em 6 dias. Cinco servidores trabalharão 8 dias no mesmo ritmo bruto, mas 20% de sua capacidade será consumida por retrabalho. Quantos processos líquidos serão concluídos?

A) 180.
B) 200.
C) 150.
D) 160.

### Questão 47
**Nível: Muito difícil**

Considere os múltiplos positivos de 5 até 200, inclusive, que não são múltiplos de 10. Excluindo também, desse conjunto, os números divisíveis por 3, qual é a soma dos termos restantes?

A) 2.000.
B) 1.260.
C) 1.265.
D) 735.

### Questão 48
**Nível: Muito difícil**

Se `2^(x - 1) = 16`, qual é o valor de `4^(x + 1) / 8^(x - 2)`?

A) 2.
B) 4.
C) 16.
D) 8.

### Questão 49
**Nível: Muito difícil**

Em uma equipe, a razão entre analistas e técnicos é 3:5. Após a contratação de 6 analistas, sem mudança no número de técnicos, a razão passa a 9:10. Quantos servidores havia inicialmente?

A) 32.
B) 40.
C) 48.
D) 24.

### Questão 50
**Nível: Muito difícil**

Considere P falsa, Q verdadeira e R falsa. O valor lógico de `[(P ou Q) → R] se e somente se [Q e (não R)]` é:

A) indeterminado, porque P é falsa.
B) verdadeiro.
C) falso.
D) verdadeiro apenas se Q implicar R.

## Questões extras de revisão fixa do Dia 6

#### Extra Dia 6.1

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Abrangência do Código de Ética
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

A respeito do Código de Ética indicado no edital, assinale a alternativa correta.

A) Ele disciplina exclusivamente pessoas físicas, deixando toda conduta de pessoa jurídica para o Regulamento de Registro.
B) Seu objeto principal é organizar os órgãos internos do CRA-PR e distribuir competências administrativas entre eles.
C) Ele alcança pessoas físicas e jurídicas e, por isso, aplica suspensão e cancelamento de forma idêntica a ambas.
D) Ele disciplina deveres e condutas de pessoas físicas e jurídicas, com as especificidades cabíveis.

#### Extra Dia 6.2

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Fiscalização de pessoa jurídica e responsabilidade técnica
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Uma empresa oferece no Paraná serviços situados no campo da Administração e indica responsável técnico que apenas assina documentos, sem participar do trabalho. A fiscalização deve:

A) considerar suficiente a existência do CNPJ e encerrar a análise.
B) examinar o objeto da atividade, a regularidade aplicável e a participação técnica efetiva.
C) presumir que a indicação formal substitui eventual registro da pessoa jurídica.
D) verificar apenas se o responsável está adimplente, sem examinar a atividade da empresa.

#### Extra Dia 6.3

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Relação entre lei e decreto regulamentar
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Sobre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967, assinale a alternativa correta.

A) O decreto substituiu a lei e passou a ocupar posição hierárquica superior no Sistema CFA/CRAs.
B) A lei estabelece a base da profissão e do Sistema, enquanto o decreto regulamenta sua execução sem poder contrariá-la.
C) A lei trata apenas da organização interna do CRA-PR, e o decreto define exclusivamente deveres éticos.
D) O decreto pode ampliar livremente o campo profissional sempre que um Conselho Regional considerar a medida conveniente.

#### Extra Dia 6.4

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Persistência do sigilo profissional
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Profissional encerra contrato e, meses depois, recebe proposta comercial para revelar informação confidencial conhecida durante o serviço. A conduta adequada é:

A) preservar o sigilo, ressalvada justa causa ou hipótese legal devidamente aplicável.
B) revelar apenas se a proposta for financeiramente vantajosa ao antigo cliente.
C) revelar a informação, pois o término do contrato extingue automaticamente o sigilo.
D) consultar apenas o contrato, porque o Código de Ética deixa de incidir após o encerramento.

#### Extra Dia 6.5

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Fiscalização e exercício regular da defesa
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Durante fiscalização regular, o fiscalizado discorda da interpretação do CRA. A postura compatível com o material é:

A) ocultar os documentos até que o CFA decida previamente o mérito.
B) impedir toda diligência, pois o direito de defesa suspende automaticamente a fiscalização.
C) fornecer as informações pertinentes dentro da competência fiscalizatória e exercer defesa pelos meios regulares.
D) emprestar o registro de terceiro para demonstrar regularidade provisória.

#### Extra Dia 6.6

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Hierarquia normativa e limites do poder regulamentar no Sistema CFA/CRAs
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Um ato interno de Conselho Regional pretende ampliar o conjunto de atividades profissionais para além da Lei nº 4.769/1965, invocando como fundamento geral o Decreto nº 61.934/1967. A conclusão adequada é:

A) a autonomia administrativa do CRA permite inovar livremente no campo profissional definido em lei.
B) o decreto regulamentar pode criar obrigações primárias sem apoio legal, desde que o ato regional repita seu texto.
C) o decreto deve permanecer nos limites da lei regulamentada, e ato interno do CRA não pode ampliar por conta própria a base legal da profissão.
D) o critério da especialidade faz o ato interno prevalecer automaticamente sobre a lei e o decreto.

#### Extra Dia 6.7

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Roteiro de resolução em legislação profissional
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Em caso prático de legislação profissional, o roteiro mais seguro é:

A) identificar o sujeito, a competência territorial e a norma que disciplina o objeto.
B) escolher primeiro a sanção mais grave e depois procurar uma norma compatível.
C) atribuir toda atuação ao CFA sempre que houver conflito.
D) tratar registro, ética, fiscalização e regimento como um único objeto normativo.

#### Extra Dia 6.8

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Jurisdição dos Conselhos Regionais
**Nível:** Médio
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Um fato ocorre fora do Paraná, mas a alternativa atribui automaticamente sua fiscalização ao CRA-PR. Antes de aceitar a afirmação, deve-se:

A) considerar que todo CRA possui jurisdição nacional concorrente.
B) aplicar apenas o Código de Ética, pois território nunca interfere na competência.
C) presumir competência do CRA-PR sempre que a atividade envolver Administração.
D) verificar a jurisdição e a competência do conselho regional correspondente.

#### Extra Dia 6.9

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Integração entre registro, ética e competência
**Nível:** Difícil
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

Empresa no Paraná exerce atividade sujeita ao sistema sem regularidade, enquanto profissional registrado lhe empresta o número sem atuação efetiva. A associação correta é:

A) o registro da empresa pertence exclusivamente ao Regimento Interno, enquanto o empréstimo do número é disciplinado pelo regulamento eleitoral.
B) o registro ativo do profissional regulariza automaticamente a empresa e torna irrelevante examinar sua participação técnica ou eventual infração ética.
C) ambas as situações são resolvidas somente pela Lei nº 12.514/2011, pois eventual irregularidade se converte em questão de anuidade e cobrança.
D) a regularidade deve ser verificada na lei, no decreto e na fonte oficial aplicável; o empréstimo pode violar o Código de Ética; a fiscalização regional cabe ao CRA-PR.

#### Extra Dia 6.10

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Controle de fontes normativas
**Nível:** Difícil
**Referência:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4)

A apostila confirmou apenas a ementa oficial de determinada resolução adicional, sem consolidar seus artigos e prazos. Em uma questão autoral, a conduta metodológica correta é:

A) afirmar o objeto confirmado e conferir a fonte oficial antes de detalhar.
B) presumir a sanção máxima aplicável a qualquer descumprimento e registrar o dado como se estivesse consolidado na fonte oficial.
C) ignorar integralmente a resolução, inclusive para mencionar o objeto que já foi confirmado por sua ementa oficial.
D) reproduzir o prazo de resolução semelhante de outro conselho e apresentá-lo como regra específica da norma ainda não consultada.

#### Extra Dia 6.11

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Localidade espacial e cache
**Nível:** Difícil
**Referência:** [Dia 1 — Cache, localidade e políticas de escrita](semana_01_estudo.md#cache-localidade-e-políticas-de-escrita)

Um programa percorre sequencialmente os elementos contíguos de um vetor. Qual princípio explica por que esse padrão tende a favorecer o aproveitamento da cache?

A) Localidade temporal, porque cada elemento precisa ser gravado permanentemente antes do próximo acesso.
B) Localidade espacial, porque o acesso a um endereço torna provável o uso próximo de endereços vizinhos.
C) Memória virtual, porque toda leitura sequencial elimina automaticamente faltas de página e de cache.
D) Write-back, porque essa política transforma elementos contíguos em registradores internos da CPU.

#### Extra Dia 6.12

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Pipeline, vazão e latência
**Nível:** Difícil
**Referência:** [Dia 1 — Pipeline de CPU](semana_01_estudo.md#pipeline-de-cpu)

Sobre o pipeline de CPU estudado, assinale a alternativa correta.

A) Ele executa toda instrução em uma única etapa e impede a sobreposição entre instruções diferentes.
B) Ele reduz obrigatoriamente a latência individual de toda instrução, mesmo quando existem dependências e desvios.
C) Ele sobrepõe etapas de instruções diferentes e tende a elevar a vazão, embora conflitos e dependências possam gerar paradas.
D) Ele substitui cache e registradores, pois mantém todas as instruções simultaneamente na memória secundária.

#### Extra Dia 6.13

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Round Robin e quantum
**Nível:** Difícil
**Referência:** [Dia 2 — CPU-bound, I/O-bound, quantum e starvation](semana_01_estudo.md#cpu-bound-io-bound-quantum-e-starvation)

No escalonamento Round Robin, qual afirmação descreve corretamente o papel do quantum?

A) Cada processo recebe uma fatia de CPU; quantum muito curto tende a aumentar as trocas de contexto, enquanto um muito longo pode piorar a resposta interativa.
B) O quantum é uma prioridade fixa que impede a preempção do processo até seu encerramento.
C) Cada processo executa até terminar seu surto completo, e a fila só é consultada quando ele se bloqueia definitivamente.
D) O quantum determina a quantidade de memória virtual do processo e não interfere na alternância de CPU.

#### Extra Dia 6.14

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Page fault e paginação
**Nível:** Difícil
**Referência:** [Dia 2 — Memória virtual, page fault, swap e thrashing](semana_01_estudo.md#memória-virtual-page-fault-swap-e-thrashing)

Durante a execução, um processo acessa uma página válida de seu espaço virtual que não está carregada na memória física naquele instante. A ocorrência descrita é:

A) necessariamente um erro fatal de segmentação, pois paginação não admite carregamento posterior.
B) um page fault, que pode fazer parte do funcionamento normal da memória virtual ao exigir o carregamento da página.
C) um deadlock, porque o processo sempre passa a esperar circularmente por outro processo.
D) um caso de journaling, mecanismo responsável por traduzir endereços virtuais em físicos.

#### Extra Dia 6.15

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** WHERE, GROUP BY e HAVING
**Nível:** Difícil
**Referência:** [Dia 3 — GROUP BY, HAVING e agregações](semana_01_estudo.md#s1-d3-group-by-having)

Qual consulta retorna, entre empregados ativos, apenas departamentos com mais de cinco empregados?

A) `SELECT depto, COUNT(*) FROM empregado WHERE ativo = 1 AND COUNT(*) > 5 GROUP BY depto;`
B) `SELECT depto, COUNT(*) FROM empregado HAVING ativo = 1 AND COUNT(*) > 5 GROUP BY depto;`
C) `SELECT depto FROM empregado WHERE COUNT(*) > 5 GROUP BY depto AND ativo = 1;`
D) `SELECT depto, COUNT(*) FROM empregado WHERE ativo = 1 GROUP BY depto HAVING COUNT(*) > 5;`

#### Extra Dia 6.16

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Comportamento de COUNT diante de NULL
**Nível:** Difícil
**Referência:** [Dia 3 — GROUP BY, HAVING e agregações](semana_01_estudo.md#s1-d3-group-by-having)

Uma tabela possui quatro linhas na coluna `valor`: 1000, NULL, 2000 e NULL. O resultado de `COUNT(valor)` e `COUNT(*)`, respectivamente, é:

A) 4 e 4.
B) 2 e 2.
C) 2 e 4.
D) 4 e 2.

#### Extra Dia 6.17

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Integração entre Regimento e Código de Ética
**Nível:** Muito difícil
**Referência:** [Dia 4 — Regimento Interno do CRA-PR](semana_01_estudo.md#s1-d4-regimento) e [Código de Ética](semana_01_estudo.md#s1-d4-codigo-etica)

No CRA-PR, o Plenário delibera sobre matéria institucional, a Diretoria executa a decisão e, em caso separado, profissional divulga dado sigiloso sem justa causa. A classificação normativa correta é:

A) todas as situações pertencem exclusivamente ao Regulamento de Registro.
B) a deliberação do Plenário é matéria do Código de Ética, e o sigilo é tema do regulamento eleitoral.
C) estrutura interna: Regimento da RN CFA nº 651/2024; sigilo profissional: Código de Ética da RN CFA nº 671/2025.
D) a Diretoria exerce função normativa nacional do CFA, e a divulgação é sempre regular após o término do contrato.

#### Extra Dia 6.18

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Crase, concordância e pontuação
**Nível:** Muito difícil
**Referência:** [Dia 5 — Concordância, regência, crase e pontuação](semana_01_estudo.md#s1-d5-concordancia-regencia-crase-pontuacao)

Assinale a frase plenamente adequada à norma-padrão e à linguagem administrativa.

A) Embora o prazo fosse curto, a equipe começou a revisar os autos e os encaminhou à chefia.
B) Embora o prazo fosse curto a equipe começou a revisar os autos, e encaminhou-os à chefia.
C) Encaminhou-se os autos à chefia, embora a equipe começasse a revisá-los.
D) A equipe começou à revisar os autos e encaminhou-os a chefia.

#### Extra Dia 6.19

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Inexigibilidade e formalização da contratação direta
**Nível:** Muito difícil
**Referência:** [Dia 4 — Contratação pública](semana_01_estudo.md#s1-d4-contratacao-publica)

A Administração comprova que somente um fornecedor pode atender legitimamente ao objeto e documenta a inviabilidade de competição. A conclusão correta é:

A) a contratação direta afasta os princípios da impessoalidade e da economicidade.
B) trata-se de dispensa, porque exclusividade significa competição possível não realizada.
C) a exclusividade autoriza escolha verbal do fornecedor e elimina instrução processual.
D) pode haver inexigibilidade, mas continuam necessários processo, motivação, justificativa e controle.

#### Extra Dia 6.20

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Percentuais condicionais, recuperação da base e reclassificação entre categorias
**Nível:** Muito difícil
**Referência:** [Dia 4 — Microtrilha de RLM](semana_01_estudo.md#s1-d4-rlm-extras)

De todos os processos analisados, 40% foram rejeitados. Dos restantes, 25% retornaram para complementação, e 135 foram aceitos definitivamente. Depois, um terço dos rejeitados foi reclassificado para complementação. Quantos processos foram analisados e qual passou a ser a diferença entre os totais em complementação e rejeitados?

A) 225 processos e 15 processos.
B) 300 processos e 5 processos.
C) 300 processos e 40 processos.
D) 360 processos e 15 processos.

## Entrega prática do Bloco 6 — Dia 6

**Referência:** [Dia 6 — Bloco 6 — Protocolo de retenção dos Dias 1–5](semana_01_estudo.md#s1-d6-b6)

Depois de resolver as Extras 6.11–6.20 sem consulta, complete a tabela abaixo. Se houver menos de seis acertos com confiança real, selecione os três erros de maior impacto para abrir a Semana 2.

| Extra | Resposta inicial | Confiança (`alta`, `média` ou `baixa`) | Resultado | Regra recuperada | Nova tentativa |
|---|---|---|---|---|---|
| 6.11–6.20 | preencher uma linha por Extra |  |  |  |  |

## Gabarito do Dia 6

1. D
2. C
3. A
4. C
5. D
6. D
7. B
8. B
9. C
10. B
11. C
12. A
13. B
14. A
15. D
16. B
17. A
18. A
19. D
20. C
21. B
22. D
23. C
24. A
25. B
26. B
27. A
28. C
29. C
30. A
31. D
32. D
33. B
34. C
35. A
36. A
37. C
38. D
39. D
40. B
41. B
42. A
43. B
44. A
45. D
46. D
47. C
48. D
49. A
50. C

### Gabarito das questões extras de revisão fixa do Dia 6

Extra Dia 6.1: D
Extra Dia 6.2: B
Extra Dia 6.3: B
Extra Dia 6.4: A
Extra Dia 6.5: C
Extra Dia 6.6: C
Extra Dia 6.7: A
Extra Dia 6.8: D
Extra Dia 6.9: D
Extra Dia 6.10: A
Extra Dia 6.11: B
Extra Dia 6.12: C
Extra Dia 6.13: A
Extra Dia 6.14: B
Extra Dia 6.15: D
Extra Dia 6.16: C
Extra Dia 6.17: C
Extra Dia 6.18: A
Extra Dia 6.19: D
Extra Dia 6.20: B


## Comentários do Dia 6

### Comentário da Questão 1

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Sigilo não serve para ocultar ausência de justificativa nem para afastar controle.
- **B) está errada:** Discricionariedade técnica continua sujeita a motivação, impessoalidade e competitividade.
- **C) está errada:** Tecnologia não gera presunção de fornecedor exclusivo nem inexigibilidade automática.
- **D) está correta:** A indicação de marca exige fundamento objetivo ligado à necessidade pública, sem favorecimento.
- **Conceito cobrado:** Impessoalidade, motivação e competitividade.
- **Pegadinha usada:** Tratar preferência técnica não demonstrada como liberdade discricionária.
- **Como pensar para acertar:** Procure uma justificativa verificável que ligue a restrição ao objeto e ao interesse público.
- **Referência à apostila de estudo:** Dia 6 — “1. Princípios da Administração Pública” e “6. Licitação pública”.

### Comentário da Questão 2

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Supremacia e continuidade são princípios estudados, mas não compõem o conjunto expresso do caput.
- **B) está errada:** Pessoalidade não integra o rol expresso; transparência e economicidade, embora relevantes, não substituem impessoalidade, publicidade e eficiência na enumeração do caput.
- **C) está correta:** A alternativa reproduz os cinco princípios expressos, memorizados por LIMPE.
- **D) está errada:** Autotutela e motivação não substituem legalidade e moralidade na sigla LIMPE.
- **Conceito cobrado:** Princípios expressos do art. 37.
- **Pegadinha usada:** Misturar princípios implícitos ou conceitos correlatos com o rol expresso.
- **Como pensar para acertar:** Recupere a sigla LIMPE: legalidade, impessoalidade, moralidade, publicidade e eficiência.
- **Referência à apostila de estudo:** Dia 6 — “1. Princípios da Administração Pública”.

### Comentário da Questão 3

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta:** Autarquia é entidade com personalidade jurídica própria, não órgão despersonalizado da Direta.
- **B) está errada:** As três espécies mencionadas pertencem à Administração Indireta.
- **C) está errada:** Órgãos da Administração Direta não possuem personalidade própria.
- **D) está errada:** Personalidade própria é característica das entidades descentralizadas.
- **Conceito cobrado:** Administração Direta e Indireta.
- **Pegadinha usada:** Confundir órgão com entidade e autonomia com personalidade.
- **Como pensar para acertar:** Pergunte se o sujeito possui personalidade jurídica: órgão não; entidade da Indireta, sim.
- **Referência à apostila de estudo:** Dia 6 — “2. Organização administrativa e autarquias”.

### Comentário da Questão 4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Empresa pública possui personalidade de direito privado e não corresponde à descrição.
- **B) está errada:** Órgão da Direta não tem personalidade jurídica própria.
- **C) está correta:** Conselho profissional é tratado, em regra, como autarquia corporativa de fiscalização.
- **D) está errada:** A função pública e o regime descrito afastam a natureza de associação voluntária.
- **Conceito cobrado:** Natureza dos conselhos profissionais.
- **Pegadinha usada:** Confundir autarquia corporativa com empresa estatal, órgão ou associação privada.
- **Como pensar para acertar:** Associe personalidade pública, autonomia e poder de fiscalização a entidade autárquica.
- **Referência à apostila de estudo:** Dia 6 — “2. Organização administrativa e autarquias”.

### Comentário da Questão 5

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** A assertiva III torna a alternativa incorreta, pois a autoexecutoriedade não é universal.
- **B) está errada:** A assertiva I também é correta e não pode ser excluída.
- **C) está errada:** A assertiva III continua incorreta nesta combinação.
- **D) está correta:** I e II estão corretas; III generaliza indevidamente um atributo.
- **Conceito cobrado:** Elementos e atributos dos atos administrativos.
- **Pegadinha usada:** Transformar atributo presente quando cabível em atributo de todos os atos.
- **Como pensar para acertar:** Avalie cada assertiva: os elementos são clássicos e a presunção é geral, mas a autoexecutoriedade depende do caso.
- **Referência à apostila de estudo:** Dia 6 — “3. Atos administrativos”.

### Comentário da Questão 6

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** Finalidade deve permanecer vinculada ao interesse público.
- **B) está errada:** Motivo reúne os pressupostos fáticos e jurídicos.
- **C) está errada:** Objeto corresponde ao efeito jurídico do ato.
- **D) está correta:** Competência decorre da norma e não pode ser transferida definitivamente por pacto informal.
- **Conceito cobrado:** Elementos do ato administrativo.
- **Pegadinha usada:** Tratar competência legal como disponibilidade pessoal do agente.
- **Como pensar para acertar:** Associe cada elemento à pergunta correspondente e desconfie de transferência sem base normativa.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 7

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** O enunciado não indica exigência judicial de forma.
- **B) está correta:** Usar competência para punir crítica desvia o ato de sua finalidade pública.
- **C) está errada:** Fatos e fundamentos podem ser controlados, mas o núcleo do caso é a perseguição.
- **D) está errada:** Remoção pode existir juridicamente; o problema está no propósito concreto.
- **Conceito cobrado:** Desvio de finalidade.
- **Pegadinha usada:** Aceitar a finalidade declarada sem confrontá-la com o objetivo real.
- **Como pensar para acertar:** Pergunte para que o ato foi efetivamente praticado, e não apenas qual justificativa foi escrita.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 8

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Leilão destina-se à alienação de bens.
- **B) está correta:** Pregão é associado a bens e serviços comuns com disputa objetiva.
- **C) está errada:** Diálogo competitivo atende contratações complexas que exigem construção de soluções.
- **D) está errada:** Concurso seleciona trabalho técnico, científico ou artístico.
- **Conceito cobrado:** Modalidade pregão.
- **Pegadinha usada:** Escolher modalidade pelo valor ou pelo caráter tecnológico, sem identificar o objeto comum.
- **Como pensar para acertar:** Comece pelo objeto: sendo serviço comum, examine o cabimento do pregão.
- **Referência à apostila de estudo:** Dia 6 — “6. Licitação pública”.

### Comentário da Questão 9

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** A inviabilidade precisa ser demonstrada, não presumida.
- **B) está errada:** A afirmação descreve corretamente a lógica da dispensa.
- **C) está correta:** Dispensa pressupõe hipótese legal com competição possível; inexigibilidade, inviabilidade de competição.
- **D) está errada:** Contratação direta não significa contratação sem processo.
- **Conceito cobrado:** Dispensa e inexigibilidade.
- **Pegadinha usada:** Usar ‘sem licitação’ para tratar institutos distintos como sinônimos.
- **Como pensar para acertar:** Pergunte se a competição é viável: se sim, pode haver dispensa legal; se não, inexigibilidade.
- **Referência à apostila de estudo:** Dia 6 — “Licitação: modalidade, critério, contratação direta e procedimento”.

### Comentário da Questão 10

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Maior lance é critério ligado especialmente ao leilão, não modalidade adequada ao caso.
- **B) está correta:** A descrição corresponde ao diálogo competitivo.
- **C) está errada:** Concurso seleciona trabalho técnico ou artístico por prêmio.
- **D) está errada:** Leilão aliena bens e não promove diálogo para desenvolver solução.
- **Conceito cobrado:** Diálogo competitivo.
- **Pegadinha usada:** Confundir complexidade do objeto com concorrência ou concurso sem observar a fase de diálogo.
- **Como pensar para acertar:** Procure os sinais ‘solução ainda não definida’ e ‘diálogo com selecionados’.
- **Referência à apostila de estudo:** Dia 6 — “Licitação: modalidade, critério, contratação direta e procedimento”.

### Comentário da Questão 11

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** A assertiva III viola vinculação ao edital e julgamento objetivo.
- **B) está errada:** A assertiva III também torna essa combinação incorreta.
- **C) está correta:** I e II expressam vinculação e prévia definição dos critérios.
- **D) está errada:** Nem todas estão corretas, pois o critério não pode mudar após conhecer propostas.
- **Conceito cobrado:** Vinculação ao edital e julgamento objetivo.
- **Pegadinha usada:** Apresentar mudança posterior como exercício legítimo de conveniência.
- **Como pensar para acertar:** Critérios devem existir antes da competição e valer igualmente para todos.
- **Referência à apostila de estudo:** Dia 6 — “6. Licitação pública”.

### Comentário da Questão 12

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta:** Escolher critério após conhecer propostas viola julgamento objetivo e vinculação.
- **B) está errada:** Técnica e preço é critério legal quando a ponderação é cabível.
- **C) está errada:** Menor preço pode ser usado com requisitos objetivos de qualidade.
- **D) está errada:** Maior desconto incide sobre parâmetro previamente definido.
- **Conceito cobrado:** Critérios de julgamento.
- **Pegadinha usada:** Confundir motivação posterior com autorização para mudar as regras da disputa.
- **Como pensar para acertar:** O critério deve ser definido no edital, antes de a Administração conhecer as propostas.
- **Referência à apostila de estudo:** Dia 6 — “6. Licitação pública”.

### Comentário da Questão 13

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Responsabilidade extracontratual não exige contrato com a vítima.
- **B) está correta:** Conduta, dano e nexo causal são requisitos centrais do regime objetivo.
- **C) está errada:** Dolo e condenação penal não são pressupostos da pretensão da vítima contra o Estado.
- **D) está errada:** Sem dano não há dever de indenizar; culpa do serviço não é exigida em todo ato comissivo.
- **Conceito cobrado:** Responsabilidade objetiva por ato comissivo.
- **Pegadinha usada:** Confundir ausência de prova de culpa com ausência de dano ou nexo.
- **Como pensar para acertar:** A vítima não precisa provar culpa, mas deve ligar a atuação estatal ao dano.
- **Referência à apostila de estudo:** Dia 6 — “7. Responsabilidade civil do Estado”.

### Comentário da Questão 14

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta:** Responsabilidade objetiva não presume a existência do dano.
- **B) está errada:** Eventos externos podem excluir responsabilidade se forem causalmente decisivos.
- **C) está errada:** Culpa concorrente pode reduzir, sem necessariamente eliminar, a indenização.
- **D) está errada:** Culpa exclusiva pode romper totalmente o nexo.
- **Conceito cobrado:** Nexo causal e excludentes.
- **Pegadinha usada:** Interpretar ‘objetiva’ como ‘automática’.
- **Como pensar para acertar:** Separe culpa do agente, dispensada perante a vítima, de dano e nexo, que continuam necessários.
- **Referência à apostila de estudo:** Dia 6 — “7. Responsabilidade civil do Estado”.

### Comentário da Questão 15

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** Dano em estrutura pública não basta, isoladamente, para responsabilização automática.
- **B) está errada:** Contrato com a vítima não é requisito geral.
- **C) está errada:** Condenação disciplinar prévia não condiciona a análise civil.
- **D) está correta:** Omissão exige investigar dever e possibilidade de agir, falha e relação causal.
- **Conceito cobrado:** Responsabilidade por omissão estatal.
- **Pegadinha usada:** Aplicar automaticamente a mesma fórmula de ato comissivo a qualquer omissão.
- **Como pensar para acertar:** Identifique o dever concreto de proteção ou manutenção e sua conexão com o dano.
- **Referência à apostila de estudo:** Dia 6 — “Improbidade e responsabilidade civil do Estado”.

### Comentário da Questão 16

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Irregularidade formal pode existir sem os requisitos da improbidade.
- **B) está correta:** A caracterização depende do tipo legal e do elemento subjetivo exigido.
- **C) está errada:** A ação de improbidade não se confunde com persecução exclusivamente penal.
- **D) está errada:** Há categorias além do enriquecimento ilícito, como lesão ao erário e violação de princípios.
- **Conceito cobrado:** Ilegalidade versus improbidade.
- **Pegadinha usada:** Converter todo erro administrativo em ato de improbidade.
- **Como pensar para acertar:** Exija enquadramento legal e elemento subjetivo antes de concluir pela improbidade.
- **Referência à apostila de estudo:** Dia 6 — “5. Improbidade administrativa”.

### Comentário da Questão 17

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** I reconhece categorias legais e III preserva devido processo; II cria automatismo indevido.
- **B) está errada:** A assertiva II é falsa, impedindo a correção de todas.
- **C) está errada:** A combinação inclui a falsa assertiva II.
- **D) está errada:** A assertiva I é correta e não pode ser excluída.
- **Conceito cobrado:** Categorias e garantias na improbidade.
- **Pegadinha usada:** Tratar divergência técnica razoável como dolo ou má-fé automática.
- **Como pensar para acertar:** Analise o enquadramento e o elemento subjetivo, sem dispensar processo e defesa.
- **Referência à apostila de estudo:** Dia 6 — “5. Improbidade administrativa”.

### Comentário da Questão 18

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** Autotutela permite à Administração controlar e invalidar seus próprios atos ilegais.
- **B) está errada:** Polícia judiciária não descreve o controle interno do ato administrativo.
- **C) está errada:** Hierarquia legislativa não é poder administrativo de desfazimento.
- **D) está errada:** Tutela jurisdicional é exercida pelo Judiciário, não pela própria Administração.
- **Conceito cobrado:** Autotutela e anulação.
- **Pegadinha usada:** Confundir controle administrativo próprio com controle judicial.
- **Como pensar para acertar:** Se a Administração revê o próprio ato por ilegalidade, associe a autotutela.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 19

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** A alternativa descreve o controle externo constitucional.
- **B) está errada:** O Judiciário controla a legalidade do ato.
- **C) está errada:** Controle interno ocorre dentro da própria organização administrativa.
- **D) está correta:** O controle judicial não autoriza substituição irrestrita do mérito administrativo legítimo.
- **Conceito cobrado:** Limites do controle judicial.
- **Pegadinha usada:** Transformar controle de legalidade em administração direta pelo juiz.
- **Como pensar para acertar:** Diferencie ilegalidade controlável de escolha legítima entre opções permitidas pela lei.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 20

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Sigilo não é presumido para todos os processos.
- **B) está errada:** A LAI não condiciona todo acesso à demonstração de interesse pessoal.
- **C) está correta:** A regra é transparência; restrição precisa de fundamento legal.
- **D) está errada:** Carga de trabalho não autoriza negativa imotivada de acesso.
- **Conceito cobrado:** Publicidade e acesso à informação.
- **Pegadinha usada:** Tratar sigilo ou interesse jurídico como regra geral.
- **Como pensar para acertar:** Parta do acesso e verifique depois se há exceção legal justificável.
- **Referência à apostila de estudo:** Dia 6 — “4. LAI e LGPD”.

### Comentário da Questão 21

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A presença de dado pessoal não torna necessariamente sigiloso todo o conteúdo público.
- **B) está correta:** É possível compatibilizar transparência e proteção mediante seleção, anonimização ou ocultação motivada.
- **C) está errada:** Custódia estatal não converte CPF, telefone e endereço em dados de divulgação irrestrita.
- **D) está errada:** Dados agregados podem ser divulgados sem exigir consentimento individual em toda hipótese, observada a base jurídica.
- **Conceito cobrado:** Compatibilização entre LAI e LGPD.
- **Pegadinha usada:** Escolher entre transparência total e sigilo total, como se não houvesse tratamento proporcional.
- **Como pensar para acertar:** Separe o conteúdo público dos identificadores pessoais e divulgue apenas o necessário e juridicamente cabível.
- **Referência à apostila de estudo:** Dia 6 — “4. LAI e LGPD”.

### Comentário da Questão 22

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Em sanções, a competência não afasta automaticamente contraditório e defesa.
- **B) está errada:** Caráter preventivo não elimina motivação nem proporcionalidade.
- **C) está errada:** Restrição administrativa não depende sempre de processo penal.
- **D) está correta:** Poder de polícia admite limitações legais e proporcionais, com garantias compatíveis com o caso.
- **Conceito cobrado:** Poder de polícia e limites jurídicos.
- **Pegadinha usada:** Confundir poder administrativo com autorização irrestrita.
- **Como pensar para acertar:** Verifique competência, fundamento legal, finalidade, proporcionalidade e procedimento.
- **Referência à apostila de estudo:** Dia 6 — “Art. 37, Administração Indireta e conselhos profissionais”.

### Comentário da Questão 23

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Defesa posterior à sanção não corrige, como regra, a falta de participação antes da decisão.
- **B) está errada:** Defesa informal posterior, sem reabertura da instrução, não assegura contraditório efetivo antes da decisão sancionadora.
- **C) está correta:** Ciência, defesa, prova pertinente e decisão motivada compõem a sequência regular.
- **D) está errada:** O Judiciário não substitui obrigatoriamente toda instrução administrativa.
- **Conceito cobrado:** Contraditório e ampla defesa no processo sancionador.
- **Pegadinha usada:** Tratar recurso posterior como substituto suficiente da defesa prévia.
- **Como pensar para acertar:** A sanção deve resultar de instrução participativa e terminar em decisão fundamentada.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 24

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** A motivação permite examinar fatos, fundamentos, coerência e finalidade.
- **B) está errada:** Expor razões não altera a natureza vinculada ou discricionária prevista em lei.
- **C) está errada:** Motivação não cria competência para quem não a possui.
- **D) está errada:** Texto formal não substitui motivo verdadeiro nem sana sua inexistência.
- **Conceito cobrado:** Motivo e motivação.
- **Pegadinha usada:** Confundir exteriorização das razões com elemento capaz de curar qualquer vício.
- **Como pensar para acertar:** Motivo é a base fática e jurídica; motivação é sua exposição controlável.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 25

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A negação da condicional mantém o antecedente verdadeiro, não o nega.
- **B) está correta:** Negar `E → (P e O)` resulta em `E e não(P e O)`, isto é, `E e (não P ou não O)`.
- **C) está errada:** A contrapositiva é equivalente à original, não sua negação.
- **D) está errada:** A disjunção proposta equivale à própria condicional em outra forma.
- **Conceito cobrado:** Negação de condicional com consequente composto.
- **Pegadinha usada:** Negar todas as parcelas sem aplicar a forma `P e não Q`.
- **Como pensar para acertar:** Primeiro negue a condicional; depois aplique De Morgan ao consequente.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 26

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** A alternativa mantém uma disjunção e troca quantificadores de modo inadequado.
- **B) está correta:** Negar a disjunção exige negar ambas as parcelas e ligá-las por conjunção.
- **C) está errada:** Ela afirma existência positiva de motivação e não nega corretamente a segunda parcela.
- **D) está errada:** Negar “todo” não produz “nenhum”, e o conectivo final deveria ser uma conjunção.
- **Conceito cobrado:** Negação de quantificadores e disjunção.
- **Pegadinha usada:** Aplicar De Morgan sem inverter corretamente ‘todo’ e ‘algum’.
- **Como pensar para acertar:** Negue cada lado: ‘todo’ vira ‘algum não’; ‘algum’ vira ‘nenhum’; ‘ou’ vira ‘e’.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 27

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Exatamente um é `(92 - 38) + (71 - 38) = 54 + 33 = 87`.
- **B) está errada:** 49 não corresponde à retirada da interseção de ambos os conjuntos.
- **C) está errada:** 54 é apenas a parcela que usa A e não B.
- **D) está errada:** 125 é o total da união `92 + 71 - 38`, não o número em exatamente um.
- **Conceito cobrado:** Conjuntos: exatamente um.
- **Pegadinha usada:** Confundir união, diferença de um conjunto e exatamente um.
- **Como pensar para acertar:** Retire a interseção de cada conjunto e some as duas partes exclusivas.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 28

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** 900 ignora a queda de produtividade individual.
- **B) está errada:** 600 não combina corretamente servidores, dias e produtividade.
- **C) está correta:** A taxa original é 12 processos por servidor-dia; a nova é 9, gerando `10 × 8 × 9 = 720`.
- **D) está errada:** 576 aplica a redução a base ou período inadequado.
- **Conceito cobrado:** Regra de três composta com produtividade.
- **Pegadinha usada:** Aumentar pessoas e tempo sem ajustar a produtividade relativa.
- **Como pensar para acertar:** Calcule a taxa por servidor-dia, aplique 75% e só então multiplique pelos novos recursos.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 29

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Esse valor resulta de compensação linear inadequada entre 12% e 10%.
- **B) está errada:** Aumento e desconto de percentuais diferentes não retornam ao preço inicial.
- **C) está correta:** O preço passa a 8.400 e depois a `8.400 × 0,90 = 7.560`.
- **D) está errada:** 8.250 corresponde a operação percentual diversa.
- **Conceito cobrado:** Percentuais sucessivos.
- **Pegadinha usada:** Somar e subtrair percentuais como se incidissem sobre a mesma base.
- **Como pensar para acertar:** Aplique os fatores na ordem: `7.500 × 1,12 × 0,90`.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 30

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** O fator acumulado é `1,25 × 0,85 = 1,0625`; `4.250 ÷ 1,0625 = 4.000`.
- **B) está errada:** O cálculo usa apenas uma das transformações e não recupera a base.
- **C) está errada:** R$ 4.250,00 é o valor final, não o original.
- **D) está errada:** R$ 5.000,00 seria o valor antes do desconto, mas já depois do aumento.
- **Conceito cobrado:** Porcentagem reversa com fatores sucessivos.
- **Pegadinha usada:** Voltar ao preço original somando ou subtraindo as taxas do valor final.
- **Como pensar para acertar:** Monte o fator acumulado e divida o preço final por ele.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 31

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** 240 seria a produção com ritmo integral, sem redução a 80%.
- **B) está errada:** 160 ignora a ampliação de horas e técnicos.
- **C) está errada:** 200 aplica ajuste parcial e não usa a taxa por técnico-hora.
- **D) está correta:** A taxa é 8 chamados por técnico-hora; `8 × 0,8 × 5 × 6 = 192`.
- **Conceito cobrado:** Produtividade composta com fator de eficiência.
- **Pegadinha usada:** Aplicar o percentual ao total antigo em vez de à taxa individual.
- **Como pensar para acertar:** Encontre a produtividade unitária, ajuste-a e multiplique pelo novo total de técnico-horas.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 32

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** 83 é o vigésimo termo, não a soma.
- **B) está errada:** 830 resulta de usar extremos ou número de termos incorretamente.
- **C) está errada:** 940 excede a soma correta.
- **D) está correta:** `a20 = 7 + 19×4 = 83`; logo `S20 = (7+83)×20/2 = 900`.
- **Conceito cobrado:** Termo e soma de progressão aritmética.
- **Pegadinha usada:** Calcular corretamente o último termo e marcá-lo como soma.
- **Como pensar para acertar:** Calcule `a20` e depois aplique a média dos extremos vezes o número de termos.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 33

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** 384 é o oitavo termo da PG, não sua soma.
- **B) está correta:** A soma é `3(2^8 - 1)/(2 - 1) = 3×255 = 765`.
- **C) está errada:** 768 confunde a soma com `3×2^8`.
- **D) está errada:** 1.533 corresponde a outra quantidade de termos.
- **Conceito cobrado:** Soma finita de progressão geométrica.
- **Pegadinha usada:** Trocar termo geral pela soma acumulada.
- **Como pensar para acertar:** Use a fórmula da soma e confirme que há oito termos, de 3 a 384.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 34

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** 3/8 não considera a retirada conjunta de três crachás.
- **B) está errada:** 5/14 equivale a 10/28 e subconta as combinações.
- **C) está correta:** Há `C(5,2)×C(3,1)=30` casos favoráveis em `C(8,3)=56`; a razão é `15/28`.
- **D) está errada:** 9/28 não corresponde à contagem combinatória.
- **Conceito cobrado:** Probabilidade hipergeométrica.
- **Pegadinha usada:** Multiplicar probabilidades sem considerar as diferentes ordens ou combinações.
- **Como pensar para acertar:** Conte combinações favoráveis e divida pelo total de grupos de três.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 35

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Use o complemento: `1 - C(8,3)/C(10,3) = 1 - 56/120 = 8/15`.
- **B) está errada:** 2/5 não representa três retiradas sem reposição.
- **C) está errada:** 7/15 não é o complemento correto do evento sem analistas.
- **D) está errada:** 1/5 é a proporção de analistas em uma retirada única.
- **Conceito cobrado:** Probabilidade pelo evento complementar.
- **Pegadinha usada:** Usar a proporção da primeira retirada para um grupo de três.
- **Como pensar para acertar:** É mais simples calcular ‘nenhum analista’ e subtrair o resultado de 1.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 36

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** `não[R e (P ou A)] = não R ou (não P e não A)`.
- **B) está errada:** A alternativa nega a disjunção interna de forma incompleta, mantendo ‘ou’.
- **C) está errada:** A negação externa de uma conjunção pede disjunção, não conjunção.
- **D) está errada:** A alternativa mantém o relatório entregue, contrariando uma das possibilidades da negação.
- **Conceito cobrado:** Lei de De Morgan em expressão aninhada.
- **Pegadinha usada:** Trocar apenas um conectivo ou ignorar os parênteses.
- **Como pensar para acertar:** Negue de fora para dentro: primeiro a conjunção; depois a disjunção interna.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 37

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** As condicionais podem permanecer verdadeiras; o dado permite aplicar contraposição.
- **B) está errada:** A existência de backup contradiria a cadeia de implicações e o fato informado.
- **C) está correta:** De ‘não restauração’ obtém-se ‘não verificação sem erro’ e, depois, ‘não backup íntegro’.
- **D) está errada:** A impossibilidade de restauração impede concluir verificação sem erro.
- **Conceito cobrado:** Encadeamento de condicionais e modus tollens.
- **Pegadinha usada:** Afirmar o antecedente ou declarar a regra falsa diante da negação do consequente.
- **Como pensar para acertar:** Percorra as contrapositivas da segunda condicional para a primeira.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 38

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Seis ignora que `P=1,Q=0` e `Q=1,R=0` invalidam casos.
- **B) está errada:** Três omite uma valoração em que antecedente falso torna a condicional verdadeira.
- **C) está errada:** Cinco inclui linha em que uma das implicações é falsa.
- **D) está correta:** As valorações 000, 001, 011 e 111 satisfazem ambas as condicionais: quatro linhas.
- **Conceito cobrado:** Contagem de valorações em condicionais encadeadas.
- **Pegadinha usada:** Considerar condicional verdadeira apenas quando antecedente e consequente são verdadeiros.
- **Como pensar para acertar:** Elimine as linhas em que alguma condicional tem antecedente verdadeiro e consequente falso.
- **Referência à apostila de estudo:** Dia 6 — “8. Raciocínio lógico: proposições e conectivos”.

### Comentário da Questão 39

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** 170 é o resultado antes de devolver a interseção tripla subtraída em excesso.
- **B) está errada:** 200 é o universo, não necessariamente a união.
- **C) está errada:** 155 decorre de tratamento incorreto das interseções.
- **D) está correta:** Inclusão-exclusão: `110+90+70-45-30-25+15 = 185`.
- **Conceito cobrado:** Inclusão-exclusão com três conjuntos.
- **Pegadinha usada:** Subtrair as interseções duplas sem somar de volta a interseção tripla.
- **Como pensar para acertar:** Aplique a fórmula completa e observe que quem está nos três foi retirado três vezes.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 40

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está errada:** Planejamento deve considerar a demanda global e evitar manipulação do enquadramento.
- **B) está correta:** Separar artificialmente objetos previsíveis para alcançar dispensa não se torna legítimo pelo valor isolado.
- **C) está errada:** Contratação direta continua documentada e controlável.
- **D) está errada:** Isonomia e finalidade pública também regem o planejamento da contratação.
- **Conceito cobrado:** Fracionamento indevido e contratação direta.
- **Pegadinha usada:** Olhar apenas o valor de cada processo e ignorar a unidade planejável da necessidade.
- **Como pensar para acertar:** Pergunte se a separação decorre de razão técnica real ou serve apenas para contornar a licitação.
- **Referência à apostila de estudo:** Dia 6 — “Licitação: modalidade, critério, contratação direta e procedimento”.

### Comentário da Questão 41

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** Menor preço só é comparável entre propostas que atendem às condições válidas do objeto.
- **B) está correta:** Os critérios publicados devem valer para todos; eventual ilegalidade do edital exige correção impessoal do procedimento.
- **C) está errada:** Alteração retroativa dirigida a uma proposta viola publicidade, vinculação e isonomia.
- **D) está errada:** Economicidade não autoriza contratar objeto em desacordo com requisito essencial válido.
- **Conceito cobrado:** Julgamento objetivo, vinculação e correção do edital.
- **Pegadinha usada:** Usar menor preço para dispensar requisito técnico apenas do licitante preferido.
- **Como pensar para acertar:** Primeiro verifique conformidade; depois compare preços. Se a regra for ilegal, corrija-a para todos.
- **Referência à apostila de estudo:** Dia 6 — “Licitação: modalidade, critério, contratação direta e procedimento”.

### Comentário da Questão 42

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** A alternativa articula corretamente três planos: regime perante a vítima, causalidade concorrente e regresso subjetivo.
- **B) está errada:** Culpa concorrente pode atenuar, enquanto culpa exclusiva pode excluir.
- **C) está errada:** Responsabilidade objetiva não dispensa dano e nexo nem torna excludentes irrelevantes.
- **D) está errada:** A vítima não precisa aguardar condenação do agente; o regresso, porém, exige dolo ou culpa.
- **Conceito cobrado:** Responsabilidade objetiva, culpa concorrente e ação regressiva.
- **Pegadinha usada:** Misturar os requisitos da relação Estado-vítima com os da relação Estado-agente.
- **Como pensar para acertar:** Resolva em duas relações: vítima contra Estado; depois Estado contra agente culpado ou doloso.
- **Referência à apostila de estudo:** Dia 6 — “Improbidade e responsabilidade civil do Estado”.

### Comentário da Questão 43

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** Revogação atua sobre ato válido e não encobre incompetência absoluta.
- **B) está correta:** A ilegalidade conduz à anulação; a inconveniência não muda a natureza do vício.
- **C) está errada:** Convalidação não é obrigatória nem cabível para todo vício, especialmente nos termos absolutos do caso.
- **D) está errada:** A autotutela permite à Administração examinar e invalidar seus próprios atos ilegais.
- **Conceito cobrado:** Anulação, revogação e vício de competência.
- **Pegadinha usada:** Escolher revogação porque o ato também se tornou inconveniente.
- **Como pensar para acertar:** A legalidade vem antes do mérito: ato inválido é objeto de anulação, não de revogação corretiva.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 44

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** A margem discricionária permanece dentro da lei e deve servir à finalidade pública com motivação coerente.
- **B) está errada:** Faixa legal não torna imunes ao controle a finalidade, os motivos e a proporcionalidade.
- **C) está errada:** Validade numérica não sana retaliação nem motivação deficiente.
- **D) está errada:** Competência não é o único elemento controlável em ato discricionário.
- **Conceito cobrado:** Controle da discricionariedade e desvio de finalidade.
- **Pegadinha usada:** Confundir margem de escolha com imunidade jurídica.
- **Como pensar para acertar:** Examine não só se o valor cabe na faixa, mas por que e para que o máximo foi escolhido.
- **Referência à apostila de estudo:** Dia 6 — “Atos administrativos: elementos, atributos e desfazimento”.

### Comentário da Questão 45

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** 84 era a quantidade pendente antes da etapa adicional; além disso, 12,5% mede apenas a queda de 96 para 84.
- **B) está errada:** 72 não resulta da retirada de 25% sobre os 84 atrasados do segundo mês.
- **C) está errada:** O total 63 está correto, mas a redução deve ser calculada sobre os 96 pendentes do primeiro mês, não confundida com a taxa da etapa adicional.
- **D) está correta:** O segundo mês teve 300 processos, 84 pendentes e 63 após a etapa adicional; a queda de 33 sobre 96 equivale a 34,375%.
- **Conceito cobrado:** Percentuais sucessivos, complemento percentual e comparação entre bases.
- **Pegadinha usada:** Aplicar todos os percentuais ao total inicial ou confundir taxa de regularização com redução relativa entre os meses.
- **Como pensar para acertar:** Calcule cada mês em sua própria base, atualize as pendências e somente depois compare a diferença com o valor do primeiro mês.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 46

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** 180 desconta 10%, e não 20%, da capacidade bruta.
- **B) está errada:** 200 ignora que 20% da capacidade será consumida.
- **C) está errada:** 150 aplica o percentual à produção inicial, não ao novo cenário.
- **D) está correta:** A taxa bruta é 5 processos por servidor-dia; a capacidade bruta nova é 200 e a líquida, 160.
- **Conceito cobrado:** Regra de três composta com perda por retrabalho.
- **Pegadinha usada:** Calcular corretamente a produção bruta e esquecer o fator líquido.
- **Como pensar para acertar:** Encontre a taxa unitária, projete a capacidade bruta e aplique 80%.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 47

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** 2.000 é a soma dos números terminados em 5 antes da segunda exclusão.
- **B) está errada:** 1.260 resulta de contagem ou soma incorreta dos termos que também são divisíveis por 3.
- **C) está correta:** Os termos terminados em 5 somam 2.000; os divisíveis por 3 são `15, 45, ..., 195` e somam 735; resta 1.265.
- **D) está errada:** 735 é justamente a soma do subconjunto que deve ser excluído, não a dos termos restantes.
- **Conceito cobrado:** Progressões aritméticas, divisibilidade e diferença de subconjuntos.
- **Pegadinha usada:** Parar após excluir múltiplos de 10 ou marcar a soma do subconjunto eliminado.
- **Como pensar para acertar:** Forme a PA dos números terminados em 5, identifique nela a sub-PA divisível por 3 e subtraia as duas somas.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 48

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** O valor 2 decorre de subtrair diretamente os expoentes sem considerar que as bases representam potências diferentes de 2.
- **B) está errada:** O valor 4 resulta de simplificação incompleta do quociente após a substituição de `x`.
- **C) está errada:** O valor 16 ignora parte do expoente presente no denominador.
- **D) está correta:** De `2^(x-1)=2^4`, obtém-se `x=5`; então `4^6/8^3 = 2^12/2^9 = 2^3 = 8`.
- **Conceito cobrado:** Equação exponencial, mudança de base e quociente de potências.
- **Pegadinha usada:** Igualar expoentes de bases distintas ou substituir `x` sem converter numerador e denominador para a mesma base.
- **Como pensar para acertar:** Determine `x`, escreva 4 e 8 como potências de 2 e só então subtraia os expoentes do quociente.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 49

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** Se A=3k e T=5k, `(3k+6)/(5k)=9/10`, logo `k=4` e o total inicial é 32.
- **B) está errada:** Esse total não satisfaz simultaneamente as razões antes e depois da contratação.
- **C) está errada:** 48 corresponderia a k=6, que não gera a nova razão.
- **D) está errada:** 24 corresponderia a k=3, também incompatível com 9:10.
- **Conceito cobrado:** Razões com alteração de uma das parcelas.
- **Pegadinha usada:** Aplicar a nova razão ao total antigo sem montar a equação.
- **Como pensar para acertar:** Represente as quantidades por 3k e 5k, acrescente 6 apenas aos analistas e resolva.
- **Referência à apostila de estudo:** Dia 6 — “RLM: lógica, conjuntos e cálculo”.

### Comentário da Questão 50

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** Os valores de P, Q e R determinam completamente a expressão.
- **B) está errada:** Os dois lados da bicondicional têm valores diferentes, portanto ela não é verdadeira.
- **C) está correta:** `P ou Q` é verdadeiro e implica R falso, tornando o lado esquerdo falso; `Q e não R` é verdadeiro; a bicondicional é falsa.
- **D) está errada:** A condição adicional proposta não faz parte da avaliação solicitada.
- **Conceito cobrado:** Avaliação de expressão lógica composta.
- **Pegadinha usada:** Avaliar a condicional como verdadeira apenas porque seu antecedente contém uma parcela falsa.
- **Como pensar para acertar:** Calcule cada subexpressão, depois a condicional e, por último, compare os lados da bicondicional.
- **Referência à apostila de estudo:** Dia 6 — “8. Raciocínio lógico: proposições e conectivos”.

### Comentários das questões extras de revisão fixa do Dia 6

#### Comentário Extra Dia 6.1

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** O Código de Ética também alcança pessoas jurídicas registradas no CRA competente, observadas as especificidades aplicáveis.
- **B) está errada:** Estrutura interna pertence ao Regimento, não ao objeto principal do Código.
- **C) está errada:** O material registra que suspensão e cancelamento não se aplicam à PJ.
- **D) está correta:** O Código orienta deveres e infrações de PF e PJ, com especificidades.
- **Conceito cobrado:** Abrangência do Código de Ética.
- **Pegadinha usada:** Ou excluir a pessoa jurídica, ou aplicar-lhe todas as sanções de modo idêntico.
- **Como pensar para acertar:** Separe incidência do Código de aplicação específica de cada sanção.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.2

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** CNPJ não substitui regularidade profissional.
- **B) está correta:** A fiscalização deve unir objeto da empresa, regularidade e atuação técnica real.
- **C) está errada:** Indicação formal não basta quando o responsável não participa.
- **D) está errada:** Adimplência isolada não comprova atuação técnica nem registro da empresa.
- **Conceito cobrado:** Fiscalização de pessoa jurídica e responsabilidade técnica.
- **Pegadinha usada:** Confundir documento formal com participação efetiva.
- **Como pensar para acertar:** Examine a atividade exercida e quem realmente orienta ou supervisiona o serviço.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.3

- **Alternativa correta:** B.
- **Nível:** Médio.
- **A) está errada:** Decreto regulamentar não revoga nem supera hierarquicamente a lei que executa.
- **B) está correta:** A lei fornece a base normativa, e o decreto detalha sua execução dentro dos limites legais.
- **C) está errada:** A lei e o decreto tratam da profissão e do Sistema, não se limitam a Regimento e Código de Ética.
- **D) está errada:** Regulamento e ato regional não podem ampliar livremente matéria definida em lei.
- **Conceito cobrado:** Relação entre lei e decreto regulamentar.
- **Pegadinha usada:** Confundir regulamentação com revogação, superioridade ou inovação sem base legal.
- **Como pensar para acertar:** Identifique qual fonte cria a base e qual apenas organiza sua execução.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.4

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** O sigilo subsiste, ressalvado fundamento legal ou justa causa aplicável.
- **B) está errada:** Vantagem econômica não constitui justa causa por si só.
- **C) está errada:** O fim do contrato não libera automaticamente a informação.
- **D) está errada:** Dever ético não é afastado apenas pelo encerramento do instrumento contratual.
- **Conceito cobrado:** Persistência do sigilo profissional.
- **Pegadinha usada:** Reduzir o sigilo à vigência formal do contrato.
- **Como pensar para acertar:** Pergunte se existe exceção jurídica concreta; sem ela, preserve a confidencialidade.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.5

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Discordância não autoriza ocultação até decisão nacional.
- **B) está errada:** Direito de defesa não suspende toda fiscalização automaticamente.
- **C) está correta:** Colaboração com diligência regular convive com defesa pelos canais próprios.
- **D) está errada:** Registro de terceiro não demonstra regularidade e pode gerar outra infração.
- **Conceito cobrado:** Fiscalização e exercício regular da defesa.
- **Pegadinha usada:** Tratar defesa como autorização para obstrução.
- **Como pensar para acertar:** Cumpra as solicitações pertinentes e conteste formalmente o que considerar indevido.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.6

- **Alternativa correta:** C.
- **Nível:** Médio.
- **A) está errada:** Autonomia administrativa não atribui ao CRA poder para redefinir matéria reservada à lei.
- **B) está errada:** Decreto regulamentar detalha a execução da lei; não recebe competência legislativa primária por ser repetido em ato regional.
- **C) está correta:** Lei, decreto regulamentar e ato interno formam níveis distintos; os dois últimos devem respeitar a base legal da profissão.
- **D) está errada:** Especialidade não autoriza norma hierarquicamente inferior a contrariar ou ampliar a lei que lhe dá fundamento.
- **Conceito cobrado:** Hierarquia normativa e limites do poder regulamentar no Sistema CFA/CRAs.
- **Pegadinha usada:** Confundir autonomia do conselho com competência para inovar além da lei.
- **Como pensar para acertar:** Identifique qual norma cria a base profissional e verifique se os atos inferiores apenas a executam ou tentam ampliá-la.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.7

- **Alternativa correta:** A.
- **Nível:** Médio.
- **A) está correta:** Sujeito, território e objeto normativo evitam as trocas mais comuns.
- **B) está errada:** Sanção é etapa posterior ao enquadramento e não deve ser presumida.
- **C) está errada:** CFA e CRA possuem funções articuladas, mas não idênticas.
- **D) está errada:** Registro, ética, fiscalização e regimento têm objetos diferentes.
- **Conceito cobrado:** Roteiro de resolução em legislação profissional.
- **Pegadinha usada:** Começar pela penalidade ou pelo número da norma sem identificar o caso.
- **Como pensar para acertar:** Mapeie quem praticou o quê, onde e sob qual disciplina.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.8

- **Alternativa correta:** D.
- **Nível:** Médio.
- **A) está errada:** CRAs possuem jurisdições regionais, não competência nacional concorrente automática.
- **B) está errada:** Ética não elimina a análise territorial da fiscalização.
- **C) está errada:** Atividade de Administração não atribui por si só todo caso ao CRA-PR.
- **D) está correta:** O local do fato e o conselho competente precisam ser verificados.
- **Conceito cobrado:** Jurisdição dos Conselhos Regionais.
- **Pegadinha usada:** Associar o nome CRA-PR a fatos ocorridos em qualquer território.
- **Como pensar para acertar:** Localize o fato antes de atribuir competência regional.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.9

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** Regimento organiza a estrutura interna, enquanto regulamento eleitoral não disciplina o uso do registro no caso apresentado.
- **B) está errada:** Registro do profissional não sana a empresa nem legitima empréstimo de número.
- **C) está errada:** Lei 12.514 trata de contribuições, não resolve isoladamente ambos os fatos.
- **D) está correta:** A alternativa exige fonte oficial confirmada para a regularidade, separa a conduta ética e atribui a fiscalização ao CRA-PR em sua jurisdição.
- **Conceito cobrado:** Integração entre registro, ética e competência.
- **Pegadinha usada:** Usar uma única norma para fatos de objetos diferentes.
- **Como pensar para acertar:** Divida o caso em regularidade da PJ, comportamento do profissional e órgão fiscalizador.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.10

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** Detalhes de artigo, prazo ou pena exigem consulta ao texto oficial.
- **B) está errada:** Sanção máxima não pode ser presumida sem base normativa e circunstâncias.
- **C) está errada:** O objeto confirmado pela ementa pode ser utilizado com a devida limitação.
- **D) está errada:** Analogia com outro conselho não confirma prazo específico.
- **Conceito cobrado:** Controle de fontes normativas.
- **Pegadinha usada:** Preencher lacuna documental com memória ou analogia.
- **Como pensar para acertar:** Afirme somente o que a fonte consultada comprova.
- **Referência à apostila de estudo:** [Dia 6 — Bloco 4 — Legislação CRA/CFA](semana_01_estudo.md#s1-d6-b4).

#### Comentário Extra Dia 6.11

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** O caso não depende de reutilizar imediatamente o mesmo elemento, que caracterizaria localidade temporal.
- **B) está correta:** Elementos contíguos ocupam endereços próximos, favorecendo o aproveitamento dos dados vizinhos trazidos para a cache.
- **C) está errada:** Memória virtual não elimina automaticamente faltas nem explica especificamente o benefício dos endereços contíguos.
- **D) está errada:** Write-back é política de escrita e não converte dados do vetor em registradores.
- **Conceito cobrado:** Localidade espacial no uso da cache.
- **Pegadinha usada:** Trocar localidade espacial por temporal ou por uma política de escrita.
- **Como pensar para acertar:** Pergunte se o padrão repete o mesmo endereço ou percorre endereços vizinhos.
- **Referência à apostila de estudo:** [Dia 1 — Cache, localidade e políticas de escrita](semana_01_estudo.md#cache-localidade-e-políticas-de-escrita).

#### Comentário Extra Dia 6.12

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** Pipeline existe justamente para permitir sobreposição de etapas entre instruções diferentes.
- **B) está errada:** A técnica melhora vazão, mas não garante menor latência individual em toda situação.
- **C) está correta:** Busca, decodificação e execução podem ocorrer para instruções distintas ao mesmo tempo, com possíveis paradas por conflitos.
- **D) está errada:** Pipeline não substitui a hierarquia de memória nem mantém instruções na memória secundária para executá-las.
- **Conceito cobrado:** Pipeline, vazão e latência.
- **Pegadinha usada:** Transformar ganho de throughput em redução obrigatória da latência individual.
- **Como pensar para acertar:** Separe quantidade de instruções concluídas por tempo da duração de uma instrução específica.
- **Referência à apostila de estudo:** [Dia 1 — Pipeline de CPU](semana_01_estudo.md#pipeline-de-cpu).

#### Comentário Extra Dia 6.13

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **A) está correta:** O quantum limita o tempo contínuo de CPU e influencia tanto o custo de alternância quanto o tempo de resposta.
- **B) está errada:** Round Robin é preemptivo; o quantum não representa prioridade fixa até o encerramento.
- **C) está errada:** Ao esgotar a fatia, processo ainda não concluído retorna à fila para permitir a alternância.
- **D) está errada:** Quantum é parâmetro de escalonamento da CPU, não medida de memória virtual.
- **Conceito cobrado:** Round Robin e efeito do quantum.
- **Pegadinha usada:** Confundir fatia de tempo com prioridade, execução até o fim ou tamanho de memória.
- **Como pensar para acertar:** Relacione quantum a preempção, fila circular, trocas de contexto e responsividade.
- **Referência à apostila de estudo:** [Dia 2 — CPU-bound, I/O-bound, quantum e starvation](semana_01_estudo.md#cpu-bound-io-bound-quantum-e-starvation).

#### Comentário Extra Dia 6.14

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **A) está errada:** Página ausente da RAM pode ser carregada; isso não equivale necessariamente a violação fatal de memória.
- **B) está correta:** O acesso provoca page fault e permite ao sistema operacional buscar a página, conforme o mecanismo de memória virtual.
- **C) está errada:** Deadlock exige espera circular por recursos e não decorre automaticamente de página não residente.
- **D) está errada:** Journaling protege a consistência do sistema de arquivos e não realiza a tradução descrita.
- **Conceito cobrado:** Page fault no funcionamento da memória virtual.
- **Pegadinha usada:** Tratar todo page fault como erro fatal ou confundi-lo com deadlock e journaling.
- **Como pensar para acertar:** Verifique se a página é válida e apenas não está residente; nesse caso, o SO pode carregá-la.
- **Referência à apostila de estudo:** [Dia 2 — Memória virtual, page fault, swap e thrashing](semana_01_estudo.md#memória-virtual-page-fault-swap-e-thrashing).

#### Comentário Extra Dia 6.15

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **A) está errada:** COUNT(*) sobre o grupo deve ser testado em HAVING, não em WHERE.
- **B) está errada:** A ordem sintática está errada e HAVING não antecede GROUP BY nesses termos.
- **C) está errada:** Agregação não pode ser usada assim em WHERE, e a cláusula GROUP BY está mal formada.
- **D) está correta:** WHERE filtra linhas ativas antes do agrupamento; HAVING filtra os grupos pelo COUNT.
- **Conceito cobrado:** WHERE, GROUP BY e HAVING.
- **Pegadinha usada:** Usar WHERE para condição agregada ou inverter a ordem das cláusulas.
- **Como pensar para acertar:** Filtre linhas com WHERE, agrupe e filtre resultados agregados com HAVING.
- **Referência à apostila de estudo:** [Dia 3 — GROUP BY, HAVING e agregações](semana_01_estudo.md#s1-d3-group-by-having).

#### Comentário Extra Dia 6.16

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** COUNT(coluna) ignora NULL e não retorna 4.
- **B) está errada:** COUNT(*) inclui todas as linhas e não retorna 2.
- **C) está correta:** Há dois valores não nulos e quatro linhas: 2 e 4.
- **D) está errada:** A ordem dos resultados foi invertida.
- **Conceito cobrado:** Comportamento de COUNT diante de NULL.
- **Pegadinha usada:** Tratar COUNT(coluna) e COUNT(*) como equivalentes.
- **Como pensar para acertar:** Conte valores não nulos para a coluna e todas as linhas para o asterisco.
- **Referência à apostila de estudo:** [Dia 3 — GROUP BY, HAVING e agregações](semana_01_estudo.md#s1-d3-group-by-having).

#### Comentário Extra Dia 6.17

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **A) está errada:** Regulamento de Registro não disciplina a divisão interna de funções nem substitui o Código.
- **B) está errada:** A alternativa inverte Regimento, Ética e regulamento eleitoral.
- **C) está correta:** RN 651/Regimento organiza Plenário e Diretoria; RN 671/Código rege o sigilo profissional.
- **D) está errada:** A Diretoria regional não assume função normativa nacional, e sigilo não desaparece automaticamente.
- **Conceito cobrado:** Integração entre Regimento e Código de Ética.
- **Pegadinha usada:** Aplicar uma resolução verdadeira ao objeto errado.
- **Como pensar para acertar:** Classifique primeiro estrutura institucional e conduta profissional; só depois associe as normas.
- **Referência à apostila de estudo:** [Dia 4 — Regimento Interno do CRA-PR](semana_01_estudo.md#s1-d4-regimento) e [Código de Ética](semana_01_estudo.md#s1-d4-codigo-etica).

#### Comentário Extra Dia 6.18

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **A) está correta:** A frase usa vírgula após a concessiva, não emprega crase antes de verbo e usa corretamente ‘à chefia’.
- **B) está errada:** A oração concessiva anteposta pede vírgula, e a vírgula antes de ‘e’ separa indevidamente ações com o mesmo sujeito.
- **C) está errada:** Com partícula apassivadora, o verbo deve concordar: ‘encaminharam-se os autos’.
- **D) está errada:** Não há crase antes de infinitivo, e ‘chefia’ exige artigo no contexto.
- **Conceito cobrado:** Crase, concordância e pontuação.
- **Pegadinha usada:** Corrigir um fenômeno e deixar outro erro discreto na mesma alternativa.
- **Como pensar para acertar:** Verifique separadamente a oração anteposta, a concordância e cada ocorrência de ‘a’.
- **Referência à apostila de estudo:** [Dia 5 — Concordância, regência, crase e pontuação](semana_01_estudo.md#s1-d5-concordancia-regencia-crase-pontuacao).

#### Comentário Extra Dia 6.19

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **A) está errada:** Impessoalidade e economicidade continuam aplicáveis.
- **B) está errada:** Inviabilidade de competição aponta para inexigibilidade, não dispensa.
- **C) está errada:** Contratação direta não autoriza escolha oral ou ausência de processo.
- **D) está correta:** Exclusividade comprovada pode tornar a competição inviável, mas não elimina a instrução da contratação direta.
- **Conceito cobrado:** Inexigibilidade e formalização da contratação direta.
- **Pegadinha usada:** Confundir ausência de licitação com ausência de procedimento e princípios.
- **Como pensar para acertar:** Responda duas perguntas: a competição é viável? Quais deveres processuais permanecem?
- **Referência à apostila de estudo:** [Dia 4 — Contratação pública](semana_01_estudo.md#s1-d4-contratacao-publica).

#### Comentário Extra Dia 6.20

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **A) está errada:** 225 surge ao dividir 135 apenas por 60% e ainda não produz a diferença informada após a reclassificação.
- **B) está correta:** Aceitos são 45% do total, logo houve 300 processos; rejeitados passam de 120 para 80 e a complementação de 45 para 85, diferença de 5.
- **C) está errada:** O total 300 está correto, mas 40 é a quantidade reclassificada, não a diferença final entre 85 e 80.
- **D) está errada:** 360 não satisfaz os 135 aceitos, pois 45% de 360 corresponde a 162.
- **Conceito cobrado:** Percentuais condicionais, recuperação da base e reclassificação entre categorias.
- **Pegadinha usada:** Somar percentuais de bases diferentes ou confundir quantidade transferida com diferença final.
- **Como pensar para acertar:** Recupere o total pelos aceitos, encontre cada categoria inicial e atualize origem e destino pela mesma transferência.
- **Referência à apostila de estudo:** [Dia 4 — Microtrilha de RLM](semana_01_estudo.md#s1-d4-rlm-extras).
