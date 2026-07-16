# Apostila de Questões - Semana 1 v1.3

## CRA-PR 2026 - Analista de Sistemas

Arquivo de questões para acompanhar a `semana_01_estudo.md`.

**Critério de autoria:** esta versão não reproduz questões reais de provas anteriores. As 300 questões principais e as 120 questões do banco complementar são autorais. Todas seguem o estilo de cobrança do Instituto Consulplan. As provas públicas da banca foram usadas somente como referência de estilo, sem reprodução de questões reais.

**Formato:** todas as questões têm quatro alternativas, de A) a D), conforme o edital do CRA-PR 2026.

**Total:** 420 questões, sendo 300 questões principais (50 por dia) e 120 questões do banco complementar (20 por dia).

**Níveis auditados:** `Médio`, `Difícil` e `Muito difícil`. A matriz 20/20/10 para 50 principais e 8/8/4 para 20 complementares orienta a produção, mas a auditoria semântica deve corrigir rótulos superestimados ou subestimados e documentar a exceção. As distribuições finais são: Dia 1, 50/16/4; Dia 2, 50/15/5; Dia 3, 25/18/7; Dia 4, 30/15/5. Os Dias 5 e 6 permanecem no formato anterior até o lote próprio. As justificativas constam dos relatórios de auditoria dos Dias 1–2 e 3–4. A dificuldade deve decorrer do conhecimento exigido e de distratores plausíveis, nunca de ambiguidade ou informação ausente.

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

**Base usada:** edital vigente, apostila de estudo v1.3 e fontes oficiais/estilo indicadas no início deste arquivo.

**Calendário de uso:** a primeira passagem termina após a resolução e a correção de `Q1`, `Q2`, `Q3`, `Q5`, `Q6`, `Q7`, `Q11`, `Q13`, `E1` e `E16`. As outras dez Essenciais — `Q9`, `Q12`, `Q16`, `Q17`, `Q25`, `E2`, `E3`, `E8`, `E13` e `E19` — abrem D+2 e devem ser corrigidas antes do Aprofundamento. O saldo de Aprofundamento continua antes de D+7; Revisão fica em D+7; Simulado pertence ao ciclo seguinte.

## Questões principais

### Questão 1
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Sistemas de numeração](semana_01_estudo.md#s1-d1-numeracao)

Em uma rotina de diagnóstico, um analista precisa converter o valor binário 101101 para decimal. O resultado correto é:

A) 53
B) 64
C) 45
D) 37

### Questão 2
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Sistemas de numeração](semana_01_estudo.md#s1-d1-numeracao)

Um dump de memória apresenta o byte 1111 0000. Em hexadecimal, esse valor deve ser representado por:

A) FF
B) F0
C) 0F
D) E0

### Questão 3
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

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
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

Assinale a alternativa incorreta sobre a hierarquia de memória.

A) Registradores ficam no nível mais rápido e próximo da CPU.
B) A cache, por possuir menor capacidade, é normalmente mais lenta que a RAM durante um acesso.
C) A RAM é volátil e usada como memória principal durante a execução de programas.
D) A memória cache costuma ser usada para manter dados frequentemente acessados próximos da CPU.

### Questão 5
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

Durante a execução de um programa, a CPU precisa realizar uma soma e uma comparação lógica. O componente diretamente associado a essas operações é:

A) unidade de controle, que coordena as etapas da instrução.
B) cache, que aproxima dados frequentemente usados da CPU.
C) ULA/ALU, que executa operações aritméticas e lógicas.
D) registradores, que mantêm temporariamente operandos e resultados.

### Questão 6
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

Um técnico afirma que a RAM, por ser rápida, basta para armazenar permanentemente os dados de uma aplicação. Essa afirmação é:

A) correta, porque o encerramento ordenado transforma automaticamente a RAM em memória não volátil.
B) incorreta, pois a RAM é volátil e a persistência exige SSD, HD ou outro meio não volátil.
C) correta, porque o circuito de refresh da RAM preserva os dados mesmo depois da falta de energia.
D) incorreta apenas quando a cache utiliza write-back e ainda possui linhas marcadas como dirty.

### Questão 7
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Interrupções e E/S](semana_01_estudo.md#s1-d1-interrupcoes-io)

Em uma placa de rede, a chegada de um pacote faz o controlador sinalizar à CPU que existe um evento a tratar, sem consulta contínua do processador. Esse mecanismo é:

A) interrupção gerada pelo dispositivo.
B) polling executado continuamente pela CPU.
C) transferência por DMA sem sinal de conclusão.
D) espera ocupada no registrador de estado.

### Questão 8
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

Um controlador pode acompanhar a conclusão de uma operação de E/S por polling ou por interrupção. Considere as afirmações:

I. O polling em laço apertado pode consumir ciclos mesmo quando ainda não existe evento novo.
II. A interrupção, por si só, transfere todo o bloco do dispositivo para a RAM, dispensando DMA.
III. A interrupção reduz a espera ativa, embora ainda exista custo para salvar contexto e executar o tratador.

Está correto apenas o que se afirma em:

A) I.
B) I e III.
C) II e III.
D) I, II e III.

### Questão 9
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Enderecamento](semana_01_estudo.md#s1-d1-enderecamento)

Um programa utiliza endereços que são traduzidos pelo hardware e pelo sistema operacional para posições reais na RAM. Essa descrição corresponde a:

A) memória virtual com tradução de endereços virtuais para físicos.
B) acesso direto do programa apenas a endereços físicos globais.
C) endereçamento imediato, no qual o operando está na instrução.
D) endereçamento direto, sem tradução e sem isolamento entre processos.

### Questão 10
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Enderecamento](semana_01_estudo.md#s1-d1-enderecamento)

No modo de endereçamento imediato, o operando:

A) está na memória apontada por um endereço guardado em outro local.
B) aparece como valor literal na própria instrução.
C) está na posição de memória indicada diretamente pela instrução.
D) resulta da soma entre um registrador-base e um deslocamento calculado.

### Questão 11
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

Um projeto em C possui três arquivos-fonte compilados separadamente, mas um módulo chama função definida em outro. A etapa responsável por resolver referências entre módulos e bibliotecas é:

A) ligação, realizada pelo linker.
B) compilação isolada de cada arquivo-fonte.
C) carregamento do executável pronto na memória.
D) montagem de instruções assembly em código objeto.

### Questão 12
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

Assinale a alternativa correta sobre compiladores e interpretadores.

A) O interpretador sempre produz um executável nativo autônomo antes de iniciar qualquer comando.
B) O compilador apenas carrega na memória um executável que já foi ligado por outro programa.
C) O interpretador combina arquivos objeto e resolve referências externas antes da execução.
D) O compilador traduz previamente o programa; o interpretador traduz ou executa unidades durante a execução.

### Questão 13
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade)

Um analista observa que determinado algoritmo acessa repetidamente posições próximas de um vetor. Esse comportamento tende a favorecer:

A) localidade temporal, porque apenas o mesmo elemento é reutilizado.
B) ausência de localidade, porque cada posição possui endereço distinto.
C) localidade espacial e melhor aproveitamento das linhas de cache.
D) write-back, porque a proximidade dos endereços determina a política de escrita.

### Questão 14
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

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
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

Uma arquitetura possui registradores gerais de 64 bits, barramento de endereços de 36 bits e barramento de dados de 32 bits. Admita memória endereçada por byte. Considere:

I. A denominação “64 bits” não significa que existam 64 núcleos.
II. Com 36 linhas de endereço, podem ser distinguidos, em tese, `2^36` endereços de byte.
III. O barramento de dados de 32 bits pode transportar 32 bits em paralelo por transferência, sem redefinir sozinho a largura dos registradores.

Está correto o que se afirma em:

A) I, apenas.
B) II e III, apenas.
C) I e II, apenas.
D) I, II e III.

### Questão 16
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

Assinale a alternativa incorreta sobre barramentos em arquitetura de computadores.

A) O barramento de endereços indica a posição a ser acessada.
B) O barramento de controle carrega sinais de coordenação, como leitura e escrita.
C) O barramento de controle executa as operações aritméticas da instrução.
D) O barramento de dados transporta conteúdo entre componentes.

### Questão 17
**Nível: Difícil**
**Uso:** Essenciais
**Referência:** [Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho)

Em um pipeline, uma instrução depende do resultado da anterior e, logo depois, ocorre um desvio previsto incorretamente. A interpretação correta é:

A) instruções independentes podem se sobrepor; a dependência insere espera e a previsão errada pode descartar trabalho.
B) a sobreposição elimina a dependência de dados, mas o desvio ainda pode reduzir a capacidade da memória principal.
C) o desvio incorreto aumenta necessariamente a latência da RAM, enquanto a dependência altera apenas a largura dos registradores.
D) o pipeline garante menor latência para cada instrução, mesmo quando surgem dependências e desvios incorretos.

### Questão 18
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade)

Uma falha de cache, ou cache miss, ocorre quando:

A) a linha está na cache, mas foi marcada como dirty depois de uma escrita.
B) o dado é encontrado na cache e pode ser entregue como cache hit.
C) o dado procurado não está na cache e deve ser buscado em nível inferior.
D) a escrita atualiza cache e RAM ao mesmo tempo pela política write-through.

### Questão 19
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

Assinale a alternativa correta sobre ponto flutuante.

A) Uma representação finita pode aproximar certos valores reais e produzir arredondamento.
B) Todo decimal finito possui representação binária finita e exata no mesmo número de bits.
C) O arredondamento ocorre apenas quando há divisão por zero durante uma operação.
D) Aumentar a quantidade de bits torna exata a representação de qualquer número real.

### Questão 20
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

Em complemento de dois com 8 bits, interprete `11111100` como inteiro com sinal e some `00000101`. O resultado correto é:

A) o primeiro operando vale -124 e a soma produz -119, sem overflow.
B) o primeiro operando vale 252 e a soma produz 1, com overflow de sinal.
C) o primeiro operando vale -4 e a soma produz 1, com overflow de sinal.
D) o primeiro operando vale -4 e a soma produz 1, sem overflow de sinal.

### Questão 21
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

Um arquivo executável já ligado precisa ser colocado na memória para iniciar sua execução. Essa etapa é realizada pelo:

A) montador, que traduz instruções assembly para código objeto.
B) compilador, que traduz o código-fonte e também inicia o processo.
C) carregador, que mapeia o executável e prepara sua execução.
D) linker, que combina os módulos e coloca o processo em execução.

### Questão 22
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

Uma palavra de máquina de 32 bits possui quantos bytes?

A) 32 bytes.
B) 4 bytes.
C) 2 bytes.
D) 8 bytes.

### Questão 23
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho)

Dois servidores foram medidos sob a mesma carga. O servidor X concluiu 120 requisições por segundo, com latência mediana de 40 ms; o servidor Y concluiu 100 por segundo, com latência mediana de 25 ms. Conclui-se corretamente que:

A) X possui maior throughput e também menor latência que Y.
B) X possui maior throughput, enquanto Y possui menor latência.
C) Y possui maior throughput, enquanto X possui menor latência.
D) Y possui menor throughput e também maior latência que X.

### Questão 24
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Enderecamento](semana_01_estudo.md#s1-d1-enderecamento)

Considere uma instrução hipotética MOV R1, #5, na qual #5 representa o valor literal a ser carregado. Esse exemplo ilustra:

A) endereçamento indireto, pois `#5` contém outro endereço a consultar.
B) endereçamento direto, pois `#5` identifica uma posição fixa da memória.
C) endereçamento indexado, pois `#5` deve ser somado a um registrador-base.
D) endereçamento imediato, pois o valor literal está codificado na instrução.

### Questão 25
**Nível: Difícil**
**Uso:** Essenciais
**Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

Para receber um bloco de um dispositivo, a CPU configura endereço, tamanho e direção da operação; o controlador move o bloco para a RAM e sinaliza a conclusão. Considere:

I. A CPU não precisa copiar cada byte do bloco por instrução.
II. O DMA elimina toda participação da CPU antes e depois da transferência.
III. Uma interrupção de conclusão é compatível com o uso de DMA.

Está correto apenas o que se afirma em:

A) I e II.
B) II e III.
C) I e III.
D) I, II e III.

### Questão 26
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Firmware](semana_01_estudo.md#s1-d1-firmware)

Assinale a alternativa correta sobre firmware.

A) É o driver carregado pelo sistema operacional para oferecer uma interface uniforme ao dispositivo.
B) É software de baixo nível, normalmente persistente, usado para inicializar ou controlar hardware.
C) É a memória ROM em si, independentemente de existir código nela armazenado.
D) É qualquer aplicativo que acesse diretamente um periférico por meio do sistema operacional.

### Questão 27
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

Um analista compara memórias e afirma: “quanto mais próximo da CPU, em geral, menor a capacidade e maior a velocidade”. A afirmação está:

A) correta para a hierarquia típica de registradores/cache/RAM/armazenamento.
B) incorreta, porque maior capacidade implica necessariamente menor latência em qualquer tecnologia.
C) incorreta, porque a RAM fica fisicamente mais próxima da CPU que os registradores e a cache.
D) correta apenas para memórias não voláteis, pois volatilidade define sozinha a hierarquia.

### Questão 28
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

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
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

Um sistema de 64 bits pode endereçar espaços maiores que um sistema de 32 bits, em tese, porque:

A) a largura do barramento de dados determina, sozinha, todos os endereços disponíveis.
B) a quantidade instalada de RAM deve coincidir com todo o espaço teórico representável.
C) a largura de endereçamento permite representar mais endereços distintos.
D) a largura arquitetural elimina a tradução entre endereços virtuais e físicos.

### Questão 30
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Programa armazenado e ciclo de instrução](semana_01_estudo.md#s1-d1-von-neumann-ciclo)

Assinale a incorreta sobre execução de instruções em uma CPU.

A) A CPU conclui instruções sem usar registradores para instrução, operandos ou resultados.
B) A etapa de busca obtém uma instrução da memória.
C) A etapa de decodificação interpreta qual operação deve ser realizada.
D) A execução pode envolver a ULA, registradores e acesso à memória.

### Questão 31
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade)

Um administrador observa que um programa acessa repetidamente o mesmo valor em curto intervalo. Esse comportamento exemplifica:

A) política write-through, pois todo reuso exige escrita imediata na RAM.
B) localidade espacial, pois envolve apenas endereços vizinhos ao valor.
C) ausência de localidade, pois o mesmo dado não pode permanecer na cache.
D) localidade temporal, pois o mesmo dado tende a ser reutilizado em intervalo curto.

### Questão 32
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Programa armazenado e ciclo de instrução](semana_01_estudo.md#s1-d1-von-neumann-ciclo)

Em computação, a expressão “programa armazenado” associada à arquitetura de von Neumann indica que:

A) programas permanecem apenas no armazenamento secundário e não ocupam a memória principal.
B) instruções ficam na CPU, enquanto apenas os dados podem ser armazenados na memória principal.
C) dados e instruções exigem memórias totalmente separadas para que a CPU consiga executar o programa.
D) instruções e dados podem residir na memória e ser buscados pela CPU durante o processamento.

### Questão 33
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

Uma rotina em assembly é traduzida para código de máquina por um:

A) loader, que mapeia na memória um executável já formado.
B) compilador, que recebe necessariamente código-fonte de alto nível.
C) montador, ou assembler, que converte as instruções assembly.
D) linker, que combina objetos e resolve referências entre módulos.

### Questão 34
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

Uma CPU possui registradores de 64 bits, barramento de endereços de 36 bits e barramento de dados de 32 bits. Apenas o barramento de dados passa a 64 bits. Admita endereçamento por byte e a mesma taxa máxima de transferências no barramento; não há informação de que controlador e memória sustentem o novo pico. A conclusão adequada é:

A) o espaço permanece `2^36` bytes; o pico bruto dobra sob a premissa dada, mas vazão efetiva e latência não podem ser garantidas.
B) o espaço permanece `2^36` bytes; o pico bruto não muda, pois somente o barramento de endereços determina os bits transferidos.
C) o espaço permanece `2^36` bytes; o pico bruto dobra e, por isso, a vazão efetiva do sistema necessariamente dobra apesar dos gargalos não medidos.
D) o espaço passa a `2^64` bytes; o pico bruto e a vazão efetiva dobram, enquanto a latência de cada acesso cai pela metade.

### Questão 35
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

Uma CPU usa registradores para armazenar temporariamente operandos e resultados intermediários. Essa afirmação está:

A) correta, pois registradores são pequenos, rápidos e mantêm operandos e resultados próximos da ULA durante a execução.
B) incorreta, pois a RAM sempre possui menor latência e substitui os registradores durante a execução.
C) incorreta, pois a cache guarda todos os operandos diretamente usados pela ULA, sem apoio de registradores.
D) correta apenas quando os registradores são não voláteis e preservam o resultado após o desligamento.

### Questão 36
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

Assinale a alternativa que apresenta somente memórias voláteis ou tipicamente temporárias no processamento.

A) SSD, HD e fita magnética.
B) DVD, SSD e ROM de firmware.
C) HD, RAM e fita magnética.
D) Registradores, cache e RAM.

### Questão 37
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Interrupções e E/S](semana_01_estudo.md#s1-d1-interrupcoes-io)

Durante uma região crítica, a CPU mascara interrupções comuns de um dispositivo. Nesse intervalo, chega uma dessas interrupções e também um evento não mascarável. Assinale a conclusão correta.

A) ambos os eventos devem ser descartados, pois qualquer máscara apaga as interrupções pendentes.
B) o evento comum deve ser atendido imediatamente, enquanto o não mascarável aguarda a retirada da máscara.
C) os dois eventos são equivalentes e sua ordem depende apenas da velocidade do barramento de dados.
D) o evento comum pode ficar pendente até a reabilitação; a máscara ordinária não bloqueia o não mascarável.

### Questão 38
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Arquiteturas, barramentos e capacidade](semana_01_estudo.md#s1-d1-arquitetura-32-64)

Ao avaliar desempenho, um analista conclui que a largura de banda da memória indica:

A) tempo necessário para concluir um único acesso à memória.
B) quantidade de dados que pode ser transferida por unidade de tempo.
C) capacidade total de armazenamento disponível nos módulos de RAM.
D) quantidade de endereços representáveis pelo barramento de endereços.

### Questão 39
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Sistemas de numeração](semana_01_estudo.md#s1-d1-numeracao)

Em um número hexadecimal, as letras A, B, C, D, E e F correspondem, respectivamente, aos valores decimais:

A) 10, 11, 12, 13, 14 e 15.
B) 11, 12, 13, 14, 15 e 16.
C) 1, 2, 3, 4, 5 e 6.
D) 16, 17, 18, 19, 20 e 21.

### Questão 40
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

Um periférico solicita atenção da CPU após concluir operação de leitura. A vantagem do uso de interrupção nesse caso é:

A) manter a CPU em espera ocupada, mas com prioridade maior que a do periférico.
B) fazer o dispositivo mover o bloco para a RAM sem controlador nem configuração.
C) eliminar o custo de tratamento e a necessidade de salvar qualquer contexto da CPU.
D) permitir que a CPU execute outro trabalho e seja avisada quando a operação terminar.

### Questão 41
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Políticas de escrita da cache](semana_01_estudo.md#s1-d1-cache-escrita)

Uma linha marcada como dirty permanece em uma cache write-back enquanto outro agente precisa ler a mesma região na memória principal. Assinale a alternativa correta.

A) sem coerência ou limpeza, outro agente pode ler valor antigo; write-through atualiza a RAM a cada escrita e aumenta o tráfego.
B) a marca dirty informa que a RAM já possui o valor novo; por isso, nenhum protocolo de coerência é necessário.
C) o write-back impede qualquer leitura concorrente e transforma a linha modificada em armazenamento permanente.
D) write-back e write-through mantêm a RAM igualmente atualizada a cada escrita, diferindo apenas no tamanho da cache.

### Questão 42
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

Considere um sistema com barramento de dados de 64 bits. Isso significa que, em uma transferência, o barramento pode transportar:

A) 64 endereços distintos, independentemente da largura do barramento de endereços.
B) 64 bits de dados em paralelo por operação de transferência, conforme a arquitetura.
C) 64 bytes por transferência, pois cada linha do barramento representa um byte completo.
D) 64 bits por segundo, sem relação com a frequência ou o protocolo do barramento.

### Questão 43
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

Quando se diz que um byte pode assumir 256 combinações, o intervalo sem sinal mais comum é:

A) 0 a 255.
B) 1 a 256.
C) 0 a 256.
D) -128 a 255.

### Questão 44
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

Três módulos foram compilados e produziram arquivos objeto. Ao gerar o executável, surgiu uma referência externa não resolvida; corrigida a biblioteca, o sistema iniciou o programa. A sequência correta é:

A) o loader deveria resolver o símbolo antes da compilação, e o linker apenas copiaria o executável para a RAM.
B) o assembler deveria combinar bibliotecas de alto nível, e o compilador carregaria o programa para execução.
C) o linker resolve referências entre objetos e bibliotecas; depois, o loader mapeia o executável na memória.
D) o compilador resolve necessariamente todo símbolo externo, e o loader substitui bibliotecas ausentes durante a execução.

### Questão 45
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

Assinale a alternativa correta sobre ROM e RAM.

A) ROM e RAM são normalmente não voláteis, mas diferem apenas na política de escrita.
B) A RAM armazena apenas rotinas de inicialização, enquanto a ROM recebe os dados de trabalho dos processos.
C) ROM é tipicamente não volátil; RAM é volátil e usada na execução de programas.
D) A volatilidade de ROM e RAM depende exclusivamente da frequência de clock usada pelo processador.

### Questão 46
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho)

Duas versões executam a mesma carga com clock e comportamento de cache equivalentes. A versão otimizada reduz bolhas do pipeline ao reordenar instruções independentes, conclui 40% mais tarefas por segundo e mantém a latência praticamente igual. Em uma cadeia de instruções dependentes, o ganho desaparece. O diagnóstico correto é:

A) A cache explica o ganho; a cadeia dependente não melhora porque miss rate igual sempre aumenta a latência de memória.
B) A latência de cada tarefa caiu 40%; o valor praticamente igual deve ser ignorado por medir apenas o percentil observado.
C) O pipeline só eleva vazão quando o clock sobe; com frequência constante, a medição de tarefas por segundo é incompatível.
D) A sobreposição elevou a vazão com instruções independentes; a cadeia limitou o paralelismo, sem evidência de ganho em cache, clock ou latência.

### Questão 47
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Firmware](semana_01_estudo.md#s1-d1-firmware)

Um sistema embarcado usa firmware para inicializar dispositivo e carregar configurações básicas. A afirmação mais adequada é:

A) o firmware atua em baixo nível e pode preparar ou controlar o hardware antes do sistema completo.
B) o firmware substitui todo driver e toda interface oferecida posteriormente pelo sistema operacional.
C) o firmware é necessariamente volátil e precisa ser reinstalado depois de cada desligamento.
D) o firmware é o próprio componente físico, e não software armazenado em memória persistente.

### Questão 48
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

Em arquitetura de computadores, a principal função dos registradores de propósito geral é:

A) indicar exclusivamente o endereço da próxima instrução, como faz o contador de programa.
B) manter exclusivamente a instrução corrente, como faz o registrador de instrução.
C) armazenar apenas flags de zero, sinal, carry e overflow produzidas pela ULA.
D) manter temporariamente operandos, endereços e resultados de uso geral pela CPU.

### Questão 49
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

Um controlador transfere blocos grandes para a RAM, enquanto pequenos estados ficam prontos em até 2 µs — menos que o custo de uma interrupção. A CPU deve trabalhar durante os blocos e reagir ao término ou erro. Qual política combina volume, espera e notificação?

A) aplicar polling a cada byte dos blocos e desativar interrupções, deixando o DMA apenas para consultar o estado do controlador.
B) usar polling limitado nos estados muito curtos, DMA nos blocos e interrupção para comunicar conclusão ou erro da transferência.
C) gerar uma interrupção por byte, reservar DMA para mensagens pequenas e consultar continuamente o estado durante todo o bloco.
D) iniciar DMA sem endereço ou tamanho e dispensar notificação, pois o controlador substitui configuração, CPU e tratamento de erro.

### Questão 50
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

Em complemento de dois com 8 bits, o hexadecimal `F4` é somado a `0F`. O resultado correto, interpretado como inteiro com sinal, é:

A) `03`, equivalente a 3, mas com overflow de sinal.
B) `E5`, equivalente a -27, sem overflow de sinal.
C) `03`, equivalente a 3, sem overflow de sinal.
D) `103`, equivalente a 259, em um registrador de 8 bits.

## Banco complementar do Dia 1

#### Extra Dia 1.1
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [CFA e CRA](semana_01_estudo.md#s1-d1-cfa-cra)

**Área:** Legislação CRA/CFA.

Um candidato confundiu a atuação do CFA com a do CRA-PR. Considerando a estrutura do Sistema CFA/CRAs, assinale a alternativa correta.

A) O CFA realiza ordinariamente os registros no Paraná, e o CRA-PR limita-se a editar normas nacionais.
B) O CFA orienta e normatiza nacionalmente, e o CRA-PR executa registro e fiscalização em sua jurisdição.
C) A autonomia administrativa do CRA-PR permite afastar normas gerais expedidas pelo CFA para o sistema.
D) CFA e CRA-PR possuem competência territorial idêntica, diferenciando-se apenas pelo local de suas sedes.

#### Extra Dia 1.2
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Lei 4.769/1965](semana_01_estudo.md#s1-d1-lei-decreto)

**Área:** Legislação CRA/CFA.

Sobre a Lei Federal nº 4.769/1965, assinale a alternativa correta.

A) A lei trata apenas de cobrança de anuidades e não disciplina o exercício profissional.
B) A lei pode ser substituída por regimento regional sempre que houver regra administrativa mais recente.
C) A lei atribui ao CFA a execução ordinária de todo registro e fiscalização regional.
D) A lei integra a base do exercício da profissão e da organização do Sistema CFA/CRAs.

#### Extra Dia 1.3
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Lei e decreto regulamentador](semana_01_estudo.md#s1-d1-lei-decreto)

**Área:** Legislação CRA/CFA.

Na leitura da legislação específica, um aluno separou lei e decreto. Assinale a alternativa correta.

A) O decreto possui hierarquia superior à lei e pode contrariá-la para completar sua regulamentação.
B) O Decreto nº 61.934/1967 regulamenta a Lei nº 4.769/1965, detalhando sua execução sem poder contrariá-la.
C) A lei apenas executa o decreto, que constitui a fonte primária da organização profissional.
D) Lei e decreto possuem o mesmo objeto, mas não mantêm relação de regulamentação entre si.

#### Extra Dia 1.4
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Regimento e natureza do CRA-PR](semana_01_estudo.md#s1-d1-regimento-natureza)

**Área:** Legislação CRA/CFA.

O edital cobra Regimento Interno do CRA-PR. Sobre sua função, assinale a alternativa correta.

A) O Regimento cria a profissão e prevalece sobre a Lei nº 4.769/1965 no Paraná.
B) O Regimento disciplina exclusivamente condutas éticas e substitui o Código de Ética.
C) O Regimento organiza os órgãos, as competências internas e o funcionamento do CRA-PR.
D) O Regimento é regulamento nacional de registro aplicado indistintamente a todos os CRAs.

#### Extra Dia 1.5
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Regimento e natureza do CRA-PR](semana_01_estudo.md#s1-d1-regimento-natureza)

**Área:** Legislação CRA/CFA.

O CRA-PR possui personalidade jurídica de direito público e autonomia administrativa, mas integra o Sistema CFA/CRAs. A conclusão correta é:

A) a personalidade pública transforma o CRA-PR em órgão subordinado hierarquicamente ao Governo do Paraná.
B) a autonomia permite organizar sua administração, sem romper a integração ao sistema nem afastar normas nacionais do CFA.
C) a integração ao sistema elimina a personalidade jurídica e toda competência administrativa regional.
D) a autonomia permite ao CRA-PR substituir leis federais e normas nacionais por decisão exclusivamente interna.

#### Extra Dia 1.6
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Regimento e natureza do CRA-PR](semana_01_estudo.md#s1-d1-regimento-natureza)

**Área:** Legislação CRA/CFA.

A RN CFA nº 651/2024 foi citada no estudo da Semana 1. Assinale a alternativa correta.

A) A RN CFA nº 651/2024 aprova o Regimento Interno do CRA-PR.
B) A RN CFA nº 651/2024 aprova o Código de Ética vigente do sistema.
C) A RN CFA nº 651/2024 institui o regulamento nacional de registro profissional.
D) A RN CFA nº 651/2024 disciplina exclusivamente contribuições e anuidades.

#### Extra Dia 1.7
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Ética profissional](semana_01_estudo.md#s1-d1-etica)

**Área:** Legislação CRA/CFA.

Um profissional empregado em órgão público recebe ordem para assinar, sem revisão, parecer preparado por terceiro e contrário à sua convicção técnica. À luz da independência e da responsabilidade profissional, assinale a alternativa correta.

A) o vínculo público transfere integralmente a responsabilidade técnica ao superior que expediu a ordem.
B) a assinatura é regular se o documento não gerar prejuízo financeiro imediato ao órgão.
C) o profissional deve assinar e registrar sua discordância apenas depois de eventual processo disciplinar.
D) o profissional deve recusar autoria sem exame e preservar sua independência técnica, fundamentando a atuação.

#### Extra Dia 1.8
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Registro de pessoa jurídica](semana_01_estudo.md#s1-d1-registro-pj)

**Área:** Legislação CRA/CFA.

Uma empresa presta serviços típicos de Administração no Paraná. Em relação ao Sistema CFA/CRAs, assinale a alternativa correta.

A) a existência de CNPJ dispensa a análise da atividade básica e de eventual responsabilidade técnica.
B) a atividade básica no campo profissional pode sujeitar a pessoa jurídica a registro, fiscalização e responsabilidade técnica aplicável.
C) apenas os sócios pessoas físicas podem ser fiscalizados, ainda que a empresa ofereça atividade profissional regulada.
D) a pessoa jurídica deve pedir registro diretamente ao CFA, sem atuação ordinária do conselho regional.

#### Extra Dia 1.9
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Ética profissional](semana_01_estudo.md#s1-d1-etica)

**Área:** Legislação CRA/CFA.

Um profissional registrado utiliza informações confidenciais de cliente para obter vantagem em outra contratação. Assinale a alternativa correta.

A) o uso comercial viola o sigilo; eventual revelação exige fundamento legítimo e deve limitar-se ao necessário.
B) o registro profissional autoriza compartilhar os dados com parceiros desde que o cliente não prove dano.
C) o sigilo impede inclusive resposta delimitada a determinação legal válida de autoridade competente.
D) a informação deixa de ser sigilosa quando puder aumentar a competitividade do profissional registrado.

#### Extra Dia 1.10
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Ética profissional](semana_01_estudo.md#s1-d1-etica)

**Área:** Legislação CRA/CFA.

Um administrador permite que terceiro use seu nome e registro para assinar trabalho que ele não acompanhou. Assinale a alternativa correta.

A) a assinatura é regular se o terceiro possuir experiência, ainda que o registrado não examine o trabalho.
B) a ausência de dano financeiro elimina a responsabilidade ligada à autoria e à habilitação profissional.
C) ceder nome ou registro sem participação real pode configurar infração; assinatura implica responsabilidade técnica.
D) o empréstimo é permitido quando o documento informa internamente quem realizou o trabalho, mesmo sem revisão.

#### Extra Dia 1.11
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Fiscalização e processo](semana_01_estudo.md#s1-d1-fiscalizacao-processo)

**Área:** Legislação CRA/CFA.

Em uma ação fiscalizatória, a empresa se recusa a apresentar documentos básicos sobre atividade profissional regulada. Assinale a alternativa correta.

A) a recusa encerra a fiscalização, pois o conselho regional somente pode atuar depois de ordem judicial específica.
B) diante de requisição regular, a obstrução pode ser apurada pelo CRA, com contraditório e defesa.
C) a empresa deve ser sancionada imediatamente pelo CFA, sem instrução regional nem oportunidade de manifestação.
D) a apresentação de documentos é sempre facultativa, mesmo quando pertinentes à atividade fiscalizada e regularmente solicitados.

#### Extra Dia 1.12
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Contribuições aos conselhos](semana_01_estudo.md#s1-d1-contribuicoes)

**Área:** Legislação CRA/CFA.

Sobre a Lei nº 12.514/2011 na leitura dirigida, assinale a alternativa correta.

A) a lei aprova o Regimento Interno do CRA-PR e define a composição de seus órgãos.
B) a lei institui o Código de Ética e disciplina exclusivamente infrações profissionais.
C) a lei substitui o regulamento de registro e define todas as modalidades de inscrição.
D) a lei é relevante para contribuições devidas aos conselhos profissionais e sua cobrança.

#### Extra Dia 1.13
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Regulamento de registro](semana_01_estudo.md#s1-d1-registro-rn649-670)

**Área:** Legislação CRA/CFA.

A RN CFA nº 649/2024 aparece na leitura dirigida da Semana 1. Assinale a alternativa correta.

A) a RN CFA nº 649/2024 aprova o Regimento Interno específico do CRA-PR.
B) a RN CFA nº 649/2024 institui o Código de Ética atualmente adotado no material.
C) a RN CFA nº 649/2024 aprova o regulamento de registro no Sistema CFA/CRAs.
D) a RN CFA nº 649/2024 trata exclusivamente de contribuições e cobrança de anuidades.

#### Extra Dia 1.14
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [RN 649/2024 e RN 670/2025](semana_01_estudo.md#s1-d1-registro-rn649-670)

**Área:** Legislação CRA/CFA.

Ao consolidar o regulamento de registro, o estudante encontrou a RN CFA nº 649/2024 e a RN CFA nº 670/2025. A leitura correta é:

A) a RN 649 é a norma-base de registro, alterada pontualmente pela RN 670; ambas devem ser lidas juntas.
B) a RN 670 revoga integralmente a RN 649 e passa a disciplinar, sozinha, todas as modalidades de registro.
C) a RN 649 trata de ética, enquanto a RN 670 converte seu objeto em Regimento Interno do CRA-PR.
D) a RN 670 possui objeto financeiro autônomo e não interfere no texto do regulamento de registro.

#### Extra Dia 1.15
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Normas dirigidas e controle de fonte](semana_01_estudo.md#s1-d1-normas-dirigidas)

**Área:** Legislação CRA/CFA.

Para resolver um caso que envolve registro de pessoa jurídica, conduta ética e competência interna do CRA-PR, o estudante separou as fontes: RN 649/2024 alterada pela RN 670/2025; RN 671/2025; e RN 651/2024. Assinale a estratégia correta.

A) usar apenas a RN 670, porque toda norma alteradora substitui integralmente a norma-base e também resolve ética e competência interna.
B) usar a RN 640 como fonte ética atual e ignorar a RN 671, pois a revogação oficial produziria efeitos apenas em casos futuros, não no edital vigente.
C) aplicar 649/670 ao registro, 671 à conduta ética e 651 ao funcionamento interno, verificando em cada ponto objeto, vigência e hierarquia.
D) aplicar a RN 651 ao registro e a RN 649 ao Código de Ética, porque uma norma regional teria prevalência e a numeração indicaria hierarquia.

#### Extra Dia 1.16
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Conectores](semana_01_estudo.md#s1-d1-portugues-conectores)

**Área:** Língua Portuguesa/interpretação.

Leia o trecho: "O relatório foi enviado à Diretoria após a consolidação dos dados; por isso, a decisão foi adiada." A expressão "por isso" indica:

A) condição necessária para que o envio do relatório ocorra.
B) oposição entre a consolidação e o envio dos dados.
C) adição de informação sem relação lógica com a anterior.
D) conclusão ou consequência produzida a partir do fato anterior.

#### Extra Dia 1.17
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Referência pronominal](semana_01_estudo.md#s1-d1-portugues-referencia)

**Área:** Língua Portuguesa/interpretação.

No trecho "A comissão revisou o edital e encaminhou suas conclusões", qual é a avaliação linguística mais precisa?

A) O possessivo é ambíguo: pode indicar conclusões da comissão ou do edital, e o contexto não resolve o possuidor.
B) O possessivo retoma univocamente a comissão, pois o feminino plural de “suas” concorda com o possuidor.
C) O possessivo retoma univocamente o edital, porque a proximidade sempre determina o referente pronominal.
D) O possessivo exige um candidato oculto como possuidor, embora nenhum candidato apareça no período.

#### Extra Dia 1.18
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Reescrita e restrição](semana_01_estudo.md#s1-d1-portugues-reescrita)

**Área:** Língua Portuguesa/interpretação.

Assinale a reescrita que preserva o sentido de: "Somente os documentos conferidos serão encaminhados."

A) Todos os documentos, conferidos ou não, serão encaminhados.
B) Nenhum documento conferido será encaminhado.
C) Apenas os documentos conferidos serão encaminhados.
D) Os documentos serão conferidos somente depois do encaminhamento.

#### Extra Dia 1.19
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Crase](semana_01_estudo.md#s1-d1-portugues-crase)

**Área:** Língua Portuguesa/interpretação.

Assinale a alternativa em que a crase está corretamente empregada.

A) O servidor começou à revisar os autos recebidos.
B) A equipe respondeu à todos os interessados no processo.
C) O relatório foi encaminhado à setor técnico competente.
D) O processo foi encaminhado à unidade responsável pela análise.

#### Extra Dia 1.20
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Conectores](semana_01_estudo.md#s1-d1-portugues-conectores)

**Área:** Língua Portuguesa/interpretação.

Leia: "Embora o sistema estivesse disponível, muitos usuários não concluíram o cadastro." A oração iniciada por "Embora" expressa:

A) causa direta.
B) conclusão.
C) concessão.
D) condição necessária.


## Gabarito do Dia 1

1. C
2. B
3. A
4. B
5. C
6. B
7. A
8. B
9. A
10. B
11. A
12. D
13. C
14. B
15. D
16. C
17. A
18. C
19. A
20. D
21. C
22. B
23. B
24. D
25. C
26. B
27. A
28. D
29. C
30. A
31. D
32. D
33. C
34. A
35. A
36. D
37. D
38. B
39. A
40. D
41. A
42. B
43. A
44. C
45. C
46. D
47. A
48. D
49. B
50. C

### Gabarito do banco complementar do Dia 1

Extra Dia 1.1: B
Extra Dia 1.2: D
Extra Dia 1.3: B
Extra Dia 1.4: C
Extra Dia 1.5: B
Extra Dia 1.6: A
Extra Dia 1.7: D
Extra Dia 1.8: B
Extra Dia 1.9: A
Extra Dia 1.10: C
Extra Dia 1.11: B
Extra Dia 1.12: D
Extra Dia 1.13: C
Extra Dia 1.14: A
Extra Dia 1.15: C
Extra Dia 1.16: D
Extra Dia 1.17: A
Extra Dia 1.18: C
Extra Dia 1.19: D
Extra Dia 1.20: C


## Comentários do Dia 1

### Comentário da Questão 1

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Sistemas de numeração](semana_01_estudo.md#s1-d1-numeracao)

- **Alternativa correta:** C.
- **A) está errada:** 53 inclui peso que não está marcado no binário apresentado.
- **B) está errada:** 64 seria 2^6, mas 101101 possui composição posicional, não apenas quantidade de bits.
- **C) está correta:** 101101₂ = 32 + 8 + 4 + 1 = 45.
- **D) está errada:** 37 resulta de ignorar o bit de peso 8; a soma posicional fica incompleta.
- **Conceito cobrado:** Conversão de binário para decimal.
- **Pegadinha usada:** Confundir potência de dois com valor posicional.
- **Como pensar para acertar:** Escreva os pesos 32, 16, 8, 4, 2 e 1 e some apenas os que têm bit 1.

### Comentário da Questão 2

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Sistemas de numeração](semana_01_estudo.md#s1-d1-numeracao)

- **Alternativa correta:** B.
- **A) está errada:** FF corresponderia a 1111 1111, não a 1111 0000.
- **B) está correta:** Cada quarteto vira um dígito hexadecimal: 1111 = F e 0000 = 0.
- **C) está errada:** 0F inverte a ordem dos quartetos; a ordem deve ser preservada.
- **D) está errada:** E corresponde a 1110, não a 1111.
- **Conceito cobrado:** Conversão binário-hexadecimal.
- **Pegadinha usada:** Inverter quartetos ou trocar F por E.
- **Como pensar para acertar:** Separe o byte em grupos de quatro bits da esquerda para a direita.

### Comentário da Questão 3

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** A.
- **A) está correta:** I e II estão corretas; com 8 bits há 2^8 combinações.
- **B) está errada:** III está errada: o maior valor sem sinal é 255 porque a contagem começa em 0.
- **C) está errada:** I é verdadeira e III é falsa; a alternativa exclui uma correta e inclui uma incorreta.
- **D) está errada:** Inclui III, que confunde quantidade de combinações com maior valor.
- **Conceito cobrado:** Bits, bytes e representação sem sinal.
- **Pegadinha usada:** Confundir 256 combinações com maior valor 256.
- **Como pensar para acertar:** Separe “quantidade de valores” de “maior valor possível”.

### Comentário da Questão 4

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

- **Alternativa correta:** B.
- **Observação:** A questão pede a alternativa incorreta.
- **A) está correta como afirmação:** Registradores ocupam o topo da hierarquia de velocidade.
- **B) é a incorreta:** Menor capacidade não torna a cache mais lenta; ela normalmente possui latência menor que a RAM.
- **C) está correta como afirmação:** RAM é memória principal volátil de trabalho.
- **D) está correta como afirmação:** Cache aproxima dados de acesso frequente da CPU.
- **Conceito cobrado:** Hierarquia de memória.
- **Pegadinha usada:** Inferir velocidade apenas pela capacidade.
- **Como pensar para acertar:** Compare latência, capacidade e proximidade da CPU separadamente.
### Comentário da Questão 5

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

- **Alternativa correta:** C.
- **A) está errada:** A unidade de controle coordena, mas não realiza o cálculo lógico-aritmético.
- **B) está errada:** A cache fornece dados rapidamente, mas não executa a operação.
- **C) está correta:** A ULA realiza soma, comparação e outras operações lógicas.
- **D) está errada:** Registradores guardam operandos e resultados, sem substituir a ULA.
- **Conceito cobrado:** Componentes da CPU.
- **Pegadinha usada:** Confundir coordenação, armazenamento e execução.
- **Como pensar para acertar:** Localize onde cada componente atua no ciclo da instrução.
### Comentário da Questão 6

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

- **Alternativa correta:** B.
- **A) está errada:** Encerramento ordenado não muda a natureza volátil da RAM.
- **B) está correta:** Persistência exige meio não volátil; velocidade e persistência são propriedades distintas.
- **C) está errada:** Refresh mantém células enquanto há alimentação, não depois da falta de energia.
- **D) está errada:** A política de escrita da cache não torna a RAM armazenamento permanente.
- **Conceito cobrado:** RAM e persistência.
- **Pegadinha usada:** Inferir não volatilidade a partir de velocidade ou refresh.
- **Como pensar para acertar:** Pergunte onde o dado permanece depois de desligar a alimentação.
### Comentário da Questão 7

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Interrupções e E/S](semana_01_estudo.md#s1-d1-interrupcoes-io)

- **Alternativa correta:** A.
- **A) está correta:** O dispositivo sinaliza o evento à CPU por interrupção.
- **B) está errada:** No polling, a CPU consulta repetidamente o estado do dispositivo.
- **C) está errada:** DMA transfere dados, mas não é sinônimo do aviso descrito.
- **D) está errada:** Espera ocupada também exige consultas repetidas pela CPU.
- **Conceito cobrado:** Interrupção de dispositivo.
- **Pegadinha usada:** Confundir aviso de evento com transferência ou consulta contínua.
- **Como pensar para acertar:** Se o dispositivo avisa a CPU, identifique interrupção.
### Comentário da Questão 8

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

- **Alternativa correta:** B.
- **A) está errada:** A afirmação III também é verdadeira.
- **B) está correta:** Polling pode desperdiçar ciclos; interrupção reduz espera ativa, mas possui overhead.
- **C) está errada:** A afirmação II atribui à interrupção uma transferência que pertence ao DMA.
- **D) está errada:** Inclui a afirmação II, que dispensa indevidamente o DMA.
- **Conceito cobrado:** Polling, interrupção e custo de tratamento.
- **Pegadinha usada:** Tratar sinalização e transferência de dados como o mesmo mecanismo.
- **Como pensar para acertar:** Separe quem consulta, quem avisa e quem transfere o bloco.
### Comentário da Questão 9

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Enderecamento](semana_01_estudo.md#s1-d1-enderecamento)

- **Alternativa correta:** A.
- **A) está correta:** O processo usa endereço virtual traduzido para endereço físico.
- **B) está errada:** Processos normalmente não acessam apenas um espaço físico global sem isolamento.
- **C) está errada:** Endereçamento imediato trata do operando codificado na instrução.
- **D) está errada:** A descrição nega justamente a tradução e o isolamento apresentados.
- **Conceito cobrado:** Endereço virtual e físico.
- **Pegadinha usada:** Misturar modo de operando com tradução de memória.
- **Como pensar para acertar:** Siga o caminho programa → endereço virtual → tradução → RAM.
### Comentário da Questão 10

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Enderecamento](semana_01_estudo.md#s1-d1-enderecamento)

- **Alternativa correta:** B.
- **A) está errada:** Descreve endereçamento indireto.
- **B) está correta:** No imediato, o literal aparece na própria instrução.
- **C) está errada:** Descreve acesso direto a uma posição de memória.
- **D) está errada:** Descreve forma indexada por base e deslocamento.
- **Conceito cobrado:** Modo imediato.
- **Pegadinha usada:** Confundir valor literal com endereço ou deslocamento.
- **Como pensar para acertar:** Identifique se a instrução contém o valor ou apenas como encontrá-lo.
### Comentário da Questão 11

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

- **Alternativa correta:** A.
- **A) está correta:** O linker combina objetos e resolve referências externas.
- **B) está errada:** Compilar isoladamente não resolve a chamada entre módulos.
- **C) está errada:** O loader atua depois que o executável já foi formado.
- **D) está errada:** O assembler traduz assembly; não liga módulos de alto nível.
- **Conceito cobrado:** Linker.
- **Pegadinha usada:** Trocar as etapas de compilação, ligação, montagem e carga.
- **Como pensar para acertar:** Referência entre arquivos objeto aponta para a ligação.
### Comentário da Questão 12

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

- **Alternativa correta:** D.
- **A) está errada:** Produzir sempre executável nativo autônomo caracteriza outra estratégia.
- **B) está errada:** Carregar executável é função do loader, não definição de compilador.
- **C) está errada:** Combinar objetos e símbolos externos é função do linker.
- **D) está correta:** Expressa o contraste clássico entre tradução prévia e execução incremental.
- **Conceito cobrado:** Compilador e interpretador.
- **Pegadinha usada:** Atribuir ao interpretador funções do linker ou loader.
- **Como pensar para acertar:** Compare o momento em que tradução e execução acontecem.
### Comentário da Questão 13

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade)

- **Alternativa correta:** C.
- **A) está errada:** O cenário fala em endereços próximos, não necessariamente no mesmo elemento.
- **B) está errada:** Vizinhança de endereços caracteriza uma forma de localidade.
- **C) está correta:** Linhas de cache podem trazer dados vizinhos úteis ao percurso.
- **D) está errada:** Política de escrita e padrão de acesso são decisões diferentes.
- **Conceito cobrado:** Localidade espacial.
- **Pegadinha usada:** Confundir proximidade espacial, reuso temporal e política de escrita.
- **Como pensar para acertar:** Endereços vizinhos sugerem localidade espacial.
### Comentário da Questão 14

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** B.
- **A) está errada:** Inclui II, que superestima o ASCII.
- **B) está correta:** I e III estão corretas; Unicode é mais amplo que ASCII.
- **C) está errada:** II é falsa porque ASCII é limitado.
- **D) está errada:** II é falsa e I também deveria estar incluída.
- **Conceito cobrado:** Codificação de caracteres.
- **Pegadinha usada:** Confundir ASCII com Unicode.
- **Como pensar para acertar:** Lembre que texto também é dado codificado numericamente.

### Comentário da Questão 15

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

- **Alternativa correta:** D.
- **A) está errada:** As afirmações II e III também estão corretas.
- **B) está errada:** Exclui a afirmação I, que separa largura arquitetural de quantidade de núcleos.
- **C) está errada:** Exclui a afirmação III, pois largura do barramento de dados é independente.
- **D) está correta:** Registradores, endereçamento e transporte têm larguras relacionadas, mas não idênticas por obrigação.
- **Conceito cobrado:** Larguras de registrador, endereço e dados.
- **Pegadinha usada:** Tratar o rótulo “64 bits” como medida única de toda a máquina.
- **Como pensar para acertar:** Avalie separadamente processamento, quantidade de endereços e bits transferidos.
### Comentário da Questão 16

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

- **Alternativa correta:** C.
- **Observação:** A questão pede a alternativa incorreta.
- **A) está correta como afirmação:** O barramento de endereços identifica a posição de acesso.
- **B) está correta como afirmação:** O barramento de controle leva sinais como leitura e escrita.
- **C) é a incorreta:** Sinais coordenam a operação; a ULA executa o cálculo aritmético.
- **D) está correta como afirmação:** O barramento de dados transporta o conteúdo.
- **Conceito cobrado:** Barramentos e ULA.
- **Pegadinha usada:** Confundir coordenação do acesso com execução do cálculo.
- **Como pensar para acertar:** Separe endereço, dados, controle e processamento.
### Comentário da Questão 17

- **Nível: Difícil**
- **Uso:** Essenciais
- **Referência:** [Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho)

- **Alternativa correta:** A.
- **A) está correta:** Pipeline sobrepõe etapas, mas dependências e desvios podem produzir stalls e descartes.
- **B) está errada:** Dependência não é eliminada e não altera capacidade da RAM.
- **C) está errada:** Desvio e dependência afetam o fluxo do pipeline, não essas larguras.
- **D) está errada:** O ganho principal é de vazão e não há garantia de menor latência individual.
- **Conceito cobrado:** Pipeline, dependência e desvio.
- **Pegadinha usada:** Transformar melhora potencial de throughput em garantia de latência.
- **Como pensar para acertar:** Identifique o paralelismo e depois os eventos que interrompem o fluxo.
### Comentário da Questão 18

- **Nível: Médio**
- **Uso:** Aprofundamento
- **Referência:** [Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade)

- **Alternativa correta:** C.
- **A) está errada:** Dirty indica modificação pendente, não ausência do dado.
- **B) está errada:** Encontrar o dado é cache hit.
- **C) está correta:** Cache miss exige buscar o dado em nível inferior.
- **D) está errada:** Write-through é uma política de escrita, não uma falha de leitura.
- **Conceito cobrado:** Cache hit e cache miss.
- **Pegadinha usada:** Misturar presença do dado, estado dirty e política de escrita.
- **Como pensar para acertar:** Primeiro pergunte se o dado procurado está na cache.
### Comentário da Questão 19

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** A.
- **A) está correta:** Uma quantidade finita de bits pode aproximar valores sem representação binária finita.
- **B) está errada:** Nem todo decimal finito é exato em base binária com largura finita.
- **C) está errada:** Arredondamento não se limita à divisão por zero.
- **D) está errada:** Mais bits reduzem erro, mas não tornam exato todo número real.
- **Conceito cobrado:** Ponto flutuante e aproximação.
- **Pegadinha usada:** Converter maior precisão em exatidão universal.
- **Como pensar para acertar:** Diferencie faixa, precisão e representação exata.
### Comentário da Questão 20

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** D.
- **A) está errada:** `11111100` não vale -124 em complemento de dois.
- **B) está errada:** A leitura 252 ignora que o valor deve ser interpretado com sinal.
- **C) está errada:** A soma -4 + 5 = 1 cabe no intervalo de 8 bits, sem overflow.
- **D) está correta:** O padrão representa -4 e a soma gera `00000001`, equivalente a 1.
- **Conceito cobrado:** Complemento de dois e overflow.
- **Pegadinha usada:** Alternar indevidamente entre leitura com e sem sinal.
- **Como pensar para acertar:** Interprete a largura e o sinal antes de somar e testar o intervalo.
### Comentário da Questão 21

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

- **Alternativa correta:** C.
- **A) está errada:** O assembler traduz assembly e não carrega o executável pronto.
- **B) está errada:** Compilar não é iniciar o processo na memória.
- **C) está correta:** O loader mapeia o executável e prepara o início da execução.
- **D) está errada:** O linker forma o executável, mas não inicia o processo.
- **Conceito cobrado:** Loader.
- **Pegadinha usada:** Confundir formação do executável com sua carga.
- **Como pensar para acertar:** Ligar vem antes de carregar; carregar vem antes de executar.
### Comentário da Questão 22

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** B.
- **A) está errada:** Confunde a quantidade de bits com bytes.
- **B) está correta:** 32 bits divididos por 8 bits por byte resultam em 4 bytes.
- **C) está errada:** 2 bytes correspondem a 16 bits.
- **D) está errada:** 8 bytes correspondem a 64 bits.
- **Conceito cobrado:** Bits e bytes.
- **Pegadinha usada:** Não converter bit para byte.
- **Como pensar para acertar:** Divida a quantidade de bits por 8.

### Comentário da Questão 23

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho)

- **Alternativa correta:** B.
- **A) está errada:** X tem maior throughput, porém maior latência.
- **B) está correta:** 120 > 100 requisições/s, enquanto 25 < 40 ms.
- **C) está errada:** Inverte as duas comparações.
- **D) está errada:** Y tem menor throughput, mas também menor latência.
- **Conceito cobrado:** Throughput e latência.
- **Pegadinha usada:** Supor que o melhor valor de uma métrica garante o melhor da outra.
- **Como pensar para acertar:** Compare requisições por tempo e tempo por requisição separadamente.
### Comentário da Questão 24

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Enderecamento](semana_01_estudo.md#s1-d1-enderecamento)

- **Alternativa correta:** D.
- **A) está errada:** `#5` é o valor e não um endereço que aponta para outro.
- **B) está errada:** O símbolo não indica uma posição fixa de memória.
- **C) está errada:** Não há registrador-base nem cálculo de índice.
- **D) está correta:** O literal está codificado diretamente na instrução.
- **Conceito cobrado:** Endereçamento imediato aplicado.
- **Pegadinha usada:** Tratar a notação de literal como endereço.
- **Como pensar para acertar:** Determine se o campo contém o valor ou a localização do valor.
### Comentário da Questão 25

- **Nível: Difícil**
- **Uso:** Essenciais
- **Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

- **Alternativa correta:** C.
- **A) está errada:** A afirmação II é falsa, pois a CPU ainda configura e trata a operação.
- **B) está errada:** A afirmação II é falsa e a I também deveria ser incluída.
- **C) está correta:** DMA move o bloco sem cópia byte a byte pela CPU e pode avisar por interrupção.
- **D) está errada:** Inclui a eliminação absoluta da CPU, que não ocorre.
- **Conceito cobrado:** DMA e interrupção de conclusão.
- **Pegadinha usada:** Interpretar menor intervenção como ausência total da CPU.
- **Como pensar para acertar:** Separe configuração, transferência do bloco e aviso de conclusão.
### Comentário da Questão 26

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Firmware](semana_01_estudo.md#s1-d1-firmware)

- **Alternativa correta:** B.
- **A) está errada:** Driver e firmware são softwares distintos e atuam em camadas diferentes.
- **B) está correta:** Firmware fornece inicialização ou controle básico próximo ao hardware.
- **C) está errada:** ROM é um meio de armazenamento; firmware é o código nela armazenado.
- **D) está errada:** Nem todo aplicativo que usa um dispositivo é firmware.
- **Conceito cobrado:** Firmware.
- **Pegadinha usada:** Confundir código, meio de armazenamento, driver e aplicativo.
- **Como pensar para acertar:** Procure software persistente associado ao controle básico do hardware.
### Comentário da Questão 27

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

- **Alternativa correta:** A.
- **A) está correta:** A hierarquia típica troca capacidade e custo por menor latência perto da CPU.
- **B) está errada:** Maior capacidade não implica necessariamente menor latência.
- **C) está errada:** Registradores e cache ficam mais próximos da execução que a RAM.
- **D) está errada:** Volatilidade não é o único critério da hierarquia.
- **Conceito cobrado:** Relações na hierarquia de memória.
- **Pegadinha usada:** Converter tendência de projeto em regra baseada em uma única propriedade.
- **Como pensar para acertar:** Considere conjuntamente proximidade, latência, custo e capacidade.
### Comentário da Questão 28

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** D.
- **A) está errada:** II está errada e III está correta.
- **B) está errada:** I está errada nessa alternativa, mas bit digital clássico é 0 ou 1.
- **C) está errada:** I deveria ser verdadeira.
- **D) está correta:** I é verdadeira; II é falsa porque byte tem 8 bits; III é verdadeira.
- **Conceito cobrado:** Representação de dados.
- **Pegadinha usada:** Trocar byte por quarteto de bits.
- **Como pensar para acertar:** Teste cada frase de forma independente.

### Comentário da Questão 29

- **Nível: Médio**
- **Uso:** Aprofundamento
- **Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

- **Alternativa correta:** C.
- **A) está errada:** Barramento de dados e largura de endereçamento são grandezas distintas.
- **B) está errada:** Espaço teórico não precisa estar integralmente preenchido por RAM física.
- **C) está correta:** Mais bits de endereço permitem mais combinações distintas.
- **D) está errada:** Arquitetura de 64 bits ainda pode usar endereços virtuais e tradução.
- **Conceito cobrado:** Capacidade de endereçamento.
- **Pegadinha usada:** Confundir espaço representável, memória instalada e largura de dados.
- **Como pensar para acertar:** Conte as combinações possíveis no campo de endereço.
### Comentário da Questão 30

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Programa armazenado e ciclo de instrução](semana_01_estudo.md#s1-d1-von-neumann-ciclo)

- **Alternativa correta:** A.
- **Observação:** A questão pede a alternativa incorreta.
- **A) é a incorreta:** Registradores mantêm instruções, operandos, endereços ou resultados ao longo do ciclo.
- **B) está correta como afirmação:** A busca obtém a instrução.
- **C) está correta como afirmação:** A decodificação identifica a operação.
- **D) está correta como afirmação:** A execução pode combinar ULA, registradores e memória.
- **Conceito cobrado:** Ciclo de instrução.
- **Pegadinha usada:** Omitir os armazenamentos internos necessários ao processamento.
- **Como pensar para acertar:** Percorra busca, decodificação, operandos, execução e resultado.
### Comentário da Questão 31

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade)

- **Alternativa correta:** D.
- **A) está errada:** Política de escrita não decorre do simples reuso de leitura.
- **B) está errada:** Localidade espacial envolve endereços vizinhos.
- **C) está errada:** Reuso do mesmo dado favorece, em vez de impedir, permanência na cache.
- **D) está correta:** Reutilizar o mesmo valor em curto intervalo caracteriza localidade temporal.
- **Conceito cobrado:** Localidade temporal.
- **Pegadinha usada:** Misturar tempo, vizinhança e escrita.
- **Como pensar para acertar:** Mesmo dado em pouco tempo significa localidade temporal.
### Comentário da Questão 32

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Programa armazenado e ciclo de instrução](semana_01_estudo.md#s1-d1-von-neumann-ciclo)

- **Alternativa correta:** D.
- **A) está errada:** O programa precisa ser levado à memória para execução.
- **B) está errada:** Instruções também podem residir na memória.
- **C) está errada:** A separação física obrigatória não define o modelo de von Neumann.
- **D) está correta:** Dados e instruções podem ser armazenados e buscados pela CPU.
- **Conceito cobrado:** Programa armazenado.
- **Pegadinha usada:** Transformar distinção lógica em separação física obrigatória.
- **Como pensar para acertar:** Lembre que a CPU busca tanto instruções quanto operandos na memória.
### Comentário da Questão 33

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

- **Alternativa correta:** C.
- **A) está errada:** Loader recebe executável já formado.
- **B) está errada:** Compilador tradicional traduz linguagem de nível mais alto.
- **C) está correta:** Assembler traduz instruções assembly para código de máquina ou objeto.
- **D) está errada:** Linker combina objetos; não traduz a linguagem assembly.
- **Conceito cobrado:** Assembler.
- **Pegadinha usada:** Trocar tradução, ligação e carregamento.
- **Como pensar para acertar:** Relacione diretamente assembly a assembler.
### Comentário da Questão 34

- **Nível: Muito difícil**
- **Uso:** Aprofundamento
- **Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

- **Alternativa correta:** A.
- **A) está correta:** Separa `2^36` bytes endereçáveis, pico bruto dobrado sob a premissa e métricas efetivas ainda não demonstradas.
- **B) está errada:** A premissa mantém a taxa de transferências e dobra os bits de cada transferência, portanto o pico bruto muda.
- **C) está errada:** O pico bruto do barramento não prova que controlador, memória e carga entreguem o dobro de vazão efetiva.
- **D) está errada:** A largura de dados não altera as 36 linhas de endereço, e nem vazão efetiva nem latência seguem automaticamente o pico bruto.
- **Conceito cobrado:** Espaço endereçável, largura por transferência, pico bruto, vazão efetiva e latência.
- **Pegadinha usada:** Transformar capacidade teórica do barramento em desempenho observado obrigatório.
- **Como pensar para acertar:** Decida, separadamente, endereço, largura, taxa teórica, gargalos do sistema e tempo de resposta.
### Comentário da Questão 35

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

- **Alternativa correta:** A.
- **A) está correta:** Registradores são pequenos, rápidos e diretamente usados pela CPU.
- **B) está errada:** RAM possui maior latência e não elimina registradores.
- **C) está errada:** Cache e registradores possuem papéis complementares.
- **D) está errada:** Registradores de trabalho são temporários e não precisam ser não voláteis.
- **Conceito cobrado:** Registradores.
- **Pegadinha usada:** Substituir registradores por outro nível da hierarquia.
- **Como pensar para acertar:** Identifique onde a ULA obtém operandos imediatos e grava resultados.
### Comentário da Questão 36

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

- **Alternativa correta:** D.
- **A) está errada:** São meios de armazenamento persistente.
- **B) está errada:** Inclui meios não voláteis.
- **C) está errada:** Mistura RAM volátil com meios persistentes.
- **D) está correta:** Esses níveis são usados temporariamente durante o processamento.
- **Conceito cobrado:** Volatilidade e hierarquia.
- **Pegadinha usada:** Misturar RAM com armazenamento permanente.
- **Como pensar para acertar:** Separe memória de trabalho de armazenamento persistente.

### Comentário da Questão 37

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Interrupções e E/S](semana_01_estudo.md#s1-d1-interrupcoes-io)

- **Alternativa correta:** D.
- **A) está errada:** Mascarar normalmente adia eventos elegíveis; não implica descartá-los todos.
- **B) está errada:** Inverte o tratamento esperado de evento mascarável e não mascarável.
- **C) está errada:** A distinção decorre de prioridade e mascaramento, não da largura do barramento.
- **D) está correta:** O evento comum pode permanecer pendente, e a máscara ordinária não bloqueia o não mascarável.
- **Conceito cobrado:** Interrupções mascaráveis e não mascaráveis.
- **Pegadinha usada:** Confundir adiar com apagar e inverter as prioridades.
- **Como pensar para acertar:** Determine primeiro se o evento aceita a máscara aplicada.
### Comentário da Questão 38

- **Nível: Médio**
- **Uso:** Aprofundamento
- **Referência:** [Arquiteturas, barramentos e capacidade](semana_01_estudo.md#s1-d1-arquitetura-32-64)

- **Alternativa correta:** B.
- **A) está errada:** Tempo de um único acesso descreve latência.
- **B) está correta:** Largura de banda mede volume transferido por unidade de tempo.
- **C) está errada:** Capacidade total é quantidade armazenável, não taxa de transferência.
- **D) está errada:** Quantidade de endereços depende do barramento de endereços.
- **Conceito cobrado:** Largura de banda.
- **Pegadinha usada:** Confundir taxa, latência, capacidade e endereçamento.
- **Como pensar para acertar:** Procure a grandeza “dados por unidade de tempo”.
### Comentário da Questão 39

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Sistemas de numeração](semana_01_estudo.md#s1-d1-numeracao)

- **Alternativa correta:** A.
- **A) está correta:** Hexadecimal usa 16 símbolos; A começa no valor 10.
- **B) está errada:** Desloca todos os valores em uma unidade.
- **C) está errada:** Confunde letras com ordem alfabética simples.
- **D) está errada:** Esses valores excedem um único dígito hexadecimal.
- **Conceito cobrado:** Base hexadecimal.
- **Pegadinha usada:** Achar que F vale 16.
- **Como pensar para acertar:** Lembre: os dígitos vão de 0 a 15.

### Comentário da Questão 40

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

- **Alternativa correta:** D.
- **A) está errada:** Espera ocupada é justamente o comportamento que a interrupção pode evitar.
- **B) está errada:** Transferência de dados ainda requer mecanismo e configuração adequados.
- **C) está errada:** Tratar uma interrupção possui custo e pode exigir salvar contexto.
- **D) está correta:** A CPU trabalha e recebe o aviso quando a E/S termina.
- **Conceito cobrado:** Interrupção versus polling.
- **Pegadinha usada:** Tratar redução de espera como eliminação de todo custo.
- **Como pensar para acertar:** Compare “ficar consultando” com “ser avisado”.
### Comentário da Questão 41

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Políticas de escrita da cache](semana_01_estudo.md#s1-d1-cache-escrita)

- **Alternativa correta:** A.
- **A) está correta:** Dirty em write-back pode deixar a RAM desatualizada; write-through aumenta tráfego ao atualizar cada escrita.
- **B) está errada:** Dirty indica precisamente que a cópia da memória pode estar antiga.
- **C) está errada:** A política não cria armazenamento permanente nem bloqueio universal.
- **D) está errada:** As políticas diferem no momento em que a RAM é atualizada.
- **Conceito cobrado:** Write-back, write-through e coerência.
- **Pegadinha usada:** Confundir estado dirty com memória principal já sincronizada.
- **Como pensar para acertar:** Localize primeiro onde está o valor mais recente.
### Comentário da Questão 42

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Arquiteturas de 32 e 64 bits](semana_01_estudo.md#s1-d1-arquitetura-32-64)

- **Alternativa correta:** B.
- **A) está errada:** Quantidade de endereços depende do barramento de endereços.
- **B) está correta:** A largura indica quantos bits de dados trafegam em paralelo por transferência.
- **C) está errada:** 64 bits correspondem a 8 bytes, não a 64 bytes.
- **D) está errada:** Largura não determina sozinha a taxa por segundo.
- **Conceito cobrado:** Barramento de dados.
- **Pegadinha usada:** Trocar bits por bytes ou largura por frequência.
- **Como pensar para acertar:** Separe bits por transferência de transferências por segundo.
### Comentário da Questão 43

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** A.
- **A) está correta:** Há 256 valores porque o zero é contado.
- **B) está errada:** Esse intervalo tem 256 valores, mas não é o intervalo binário sem sinal usual.
- **C) está errada:** Esse intervalo teria 257 valores.
- **D) está errada:** Mistura representação com sinal e sem sinal incorretamente.
- **Conceito cobrado:** Intervalo sem sinal.
- **Pegadinha usada:** Esquecer o zero.
- **Como pensar para acertar:** Quantidade de combinações é 256; maior valor é 255.

### Comentário da Questão 44

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Tradução de programas](semana_01_estudo.md#s1-d1-traducao-programas)

- **Alternativa correta:** C.
- **A) está errada:** Loader não resolve símbolos antes da compilação e linker não carrega processos.
- **B) está errada:** Assembler não combina bibliotecas de alto nível e compilador não é loader.
- **C) está correta:** Linker resolve referências; loader mapeia o executável formado.
- **D) está errada:** Símbolos externos podem depender da ligação, e loader não inventa biblioteca ausente.
- **Conceito cobrado:** Compilação, ligação e carregamento.
- **Pegadinha usada:** Inverter a ordem e a responsabilidade das ferramentas.
- **Como pensar para acertar:** Identifique o artefato existente em cada etapa: fonte, objeto e executável.
### Comentário da Questão 45

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Hierarquia de memória](semana_01_estudo.md#s1-d1-hierarquia-memoria)

- **Alternativa correta:** C.
- **A) está errada:** A RAM é normalmente volátil.
- **B) está errada:** Inverte os usos típicos de RAM e ROM.
- **C) está correta:** ROM tende a preservar conteúdo; RAM atende aos dados e programas em execução.
- **D) está errada:** Clock não determina sozinho a volatilidade da memória.
- **Conceito cobrado:** ROM e RAM.
- **Pegadinha usada:** Inverter volatilidade, função e causa técnica.
- **Como pensar para acertar:** Pergunte qual memória é área de trabalho e qual tende a preservar inicialização.
### Comentário da Questão 46

- **Nível: Muito difícil**
- **Uso:** Aprofundamento
- **Referência:** [Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho)

- **Alternativa correta:** D.
- **A) está errada:** O comportamento de cache é equivalente e não explica por que somente instruções independentes ganham vazão.
- **B) está errada:** A medição separa throughput maior de latência individual praticamente estável.
- **C) está errada:** Melhor uso das etapas pode elevar instruções concluídas por ciclo sem alterar a frequência.
- **D) está correta:** Integra vazão, independência de instruções, limite da cadeia dependente e ausência de mudança nas demais métricas.
- **Conceito cobrado:** Pipeline, paralelismo entre instruções, throughput, latência e gargalo de dependência.
- **Pegadinha usada:** Atribuir o ganho a cache/clock ou transformá-lo em melhora universal de qualquer carga.
- **Como pensar para acertar:** Cruze três filtros: métrica que mudou, tipo de instrução que ganhou e grandezas mantidas constantes.
### Comentário da Questão 47

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Firmware](semana_01_estudo.md#s1-d1-firmware)

- **Alternativa correta:** A.
- **A) está correta:** Firmware pode executar inicialização e controle básico antes do sistema completo.
- **B) está errada:** Drivers e interfaces do sistema continuam tendo funções próprias.
- **C) está errada:** Firmware costuma persistir entre desligamentos.
- **D) está errada:** Firmware é software, não o componente físico em si.
- **Conceito cobrado:** Firmware em sistema embarcado.
- **Pegadinha usada:** Confundir firmware com driver, hardware ou código volátil.
- **Como pensar para acertar:** Observe a inicialização persistente e próxima do dispositivo.
### Comentário da Questão 48

- **Nível: Médio**
- **Uso:** Simulado
- **Referência:** [Componentes da CPU](semana_01_estudo.md#s1-d1-cpu-componentes)

- **Alternativa correta:** D.
- **A) está errada:** Essa é função específica do contador de programa.
- **B) está errada:** Essa é função específica do registrador de instrução.
- **C) está errada:** Flags ficam em registrador de estado, não descrevem o uso geral.
- **D) está correta:** Registradores gerais mantêm operandos, endereços e resultados temporários.
- **Conceito cobrado:** Tipos de registradores.
- **Pegadinha usada:** Trocar registradores gerais por registradores especializados.
- **Como pensar para acertar:** Diferencie armazenamento de uso geral de PC, IR e flags.
### Comentário da Questão 49

- **Nível: Muito difícil**
- **Uso:** Aprofundamento
- **Referência:** [Polling, interrupção e DMA](semana_01_estudo.md#s1-d1-polling-dma)

- **Alternativa correta:** B.
- **A) está errada:** Polling por byte monopoliza a CPU e inverte a função do DMA na movimentação do bloco.
- **B) está correta:** A espera curta e limitada admite polling; o volume favorece DMA; conclusão e erro pedem notificação por interrupção.
- **C) está errada:** Interromper por byte aumenta overhead, enquanto DMA não é mero mecanismo para mensagens pequenas.
- **D) está errada:** DMA exige configuração e a CPU ainda precisa tratar conclusão ou falha comunicada pelo controlador.
- **Conceito cobrado:** Seleção combinada entre polling, interrupção e DMA.
- **Pegadinha usada:** Escolher um único mecanismo sem considerar duração, volume e evento que precisa ser comunicado.
- **Como pensar para acertar:** Aplique três filtros: espera curta, transferência em bloco e notificação assíncrona.
### Comentário da Questão 50

- **Nível: Difícil**
- **Uso:** Simulado
- **Referência:** [Representação de dados](semana_01_estudo.md#s1-d1-representacao-dados)

- **Alternativa correta:** C.
- **A) está errada:** O valor numérico 3 está correto, mas não existe overflow nessa soma.
- **B) está errada:** A soma de `F4` (-12) com `0F` (15) não produz `E5`.
- **C) está correta:** -12 + 15 = 3, representado por `03`, dentro da faixa de 8 bits.
- **D) está errada:** Um registrador de 8 bits mantém apenas oito bits; além disso, a leitura ignora o sinal.
- **Conceito cobrado:** Hexadecimal, complemento de dois e overflow.
- **Pegadinha usada:** Misturar resultado aritmético, largura e interpretação com sinal.
- **Como pensar para acertar:** Converta com sinal, some e só então verifique faixa e representação.
### Comentários do banco complementar do Dia 1

#### Comentário Extra Dia 1.1

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [CFA e CRA](semana_01_estudo.md#s1-d1-cfa-cra)

- **Alternativa correta:** B.
- **A) está errada:** Inverte as funções nacional e regional.
- **B) está correta:** O CFA orienta e normatiza nacionalmente; o CRA-PR executa registro e fiscalização regional.
- **C) está errada:** Autonomia administrativa não autoriza afastar normas gerais do sistema.
- **D) está errada:** As competências territoriais e funcionais não são idênticas.
- **Conceito cobrado:** CFA e CRA-PR.
- **Pegadinha usada:** Confundir autonomia com ruptura do sistema.
- **Como pensar para acertar:** Identifique primeiro o alcance nacional ou regional da atuação.
#### Comentário Extra Dia 1.2

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Lei 4.769/1965](semana_01_estudo.md#s1-d1-lei-decreto)

- **Alternativa correta:** D.
- **A) está errada:** A lei também disciplina a profissão e a estrutura institucional.
- **B) está errada:** Regimento não substitui lei federal.
- **C) está errada:** A execução regional ordinária cabe ao conselho regional.
- **D) está correta:** A Lei nº 4.769/1965 integra a base do exercício profissional e do sistema.
- **Conceito cobrado:** Lei nº 4.769/1965.
- **Pegadinha usada:** Reduzir o objeto da lei ou inverter CFA e CRA.
- **Como pensar para acertar:** Separe fonte legal, organização interna e execução regional.
#### Comentário Extra Dia 1.3

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Lei e decreto regulamentador](semana_01_estudo.md#s1-d1-lei-decreto)

- **Alternativa correta:** B.
- **A) está errada:** Decreto não pode contrariar lei sob pretexto de regulamentá-la.
- **B) está correta:** O Decreto nº 61.934/1967 regulamenta a Lei nº 4.769/1965 e deve respeitar sua hierarquia ao detalhar a execução.
- **C) está errada:** A relação é inversa: o decreto executa a lei.
- **D) está errada:** As fontes mantêm relação expressa de regulamentação.
- **Conceito cobrado:** Lei e decreto regulamentador.
- **Pegadinha usada:** Inverter hierarquia e função normativa.
- **Como pensar para acertar:** Identifique qual norma fornece a base e qual detalha sua execução.
#### Comentário Extra Dia 1.4

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Regimento e natureza do CRA-PR](semana_01_estudo.md#s1-d1-regimento-natureza)

- **Alternativa correta:** C.
- **A) está errada:** Regimento não cria profissão nem prevalece sobre lei.
- **B) está errada:** Código de Ética e Regimento possuem objetos diferentes.
- **C) está correta:** O Regimento disciplina órgãos, competências e funcionamento interno do CRA-PR.
- **D) está errada:** Regulamento nacional de registro é outra norma.
- **Conceito cobrado:** Função do Regimento Interno.
- **Pegadinha usada:** Trocar organização interna por ética ou registro.
- **Como pensar para acertar:** Relacione regimento à estrutura e ao funcionamento do órgão.
#### Comentário Extra Dia 1.5

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Regimento e natureza do CRA-PR](semana_01_estudo.md#s1-d1-regimento-natureza)

- **Alternativa correta:** B.
- **A) está errada:** O CRA-PR não se converte em órgão estadual subordinado.
- **B) está correta:** Autonomia administrativa convive com integração e observância das normas nacionais.
- **C) está errada:** Integrar o sistema não elimina personalidade nem competência regional.
- **D) está errada:** Autonomia não permite substituir lei federal ou norma nacional válida.
- **Conceito cobrado:** Natureza, autonomia e integração do CRA-PR.
- **Pegadinha usada:** Transformar autonomia em soberania normativa.
- **Como pensar para acertar:** Avalie separadamente personalidade, autonomia e vínculo sistêmico.
#### Comentário Extra Dia 1.6

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Regimento e natureza do CRA-PR](semana_01_estudo.md#s1-d1-regimento-natureza)

- **Alternativa correta:** A.
- **A) está correta:** A RN CFA nº 651/2024 aprova o Regimento Interno do CRA-PR.
- **B) está errada:** O Código de Ética adotado é objeto de outra resolução.
- **C) está errada:** O regulamento de registro é aprovado pela RN nº 649/2024.
- **D) está errada:** A RN nº 651/2024 não possui objeto exclusivamente financeiro.
- **Conceito cobrado:** Objeto da RN CFA nº 651/2024.
- **Pegadinha usada:** Trocar Regimento, Ética e Registro.
- **Como pensar para acertar:** Associe cada resolução ao seu objeto oficial.
#### Comentário Extra Dia 1.7

- **Nível: Difícil**
- **Uso:** Simulado
- **Referência:** [Ética profissional](semana_01_estudo.md#s1-d1-etica)

- **Alternativa correta:** D.
- **A) está errada:** O vínculo público não elimina a responsabilidade profissional.
- **B) está errada:** Ausência de dano imediato não legitima autoria sem exame.
- **C) está errada:** O dever técnico deve orientar a conduta antes da assinatura.
- **D) está correta:** Independência técnica e responsabilidade impedem assinatura automática de trabalho alheio e contrário à convicção.
- **Conceito cobrado:** Independência e autoria profissional.
- **Pegadinha usada:** Usar hierarquia funcional para afastar responsabilidade técnica.
- **Como pensar para acertar:** Verifique autoria, exame efetivo e convicção técnica antes do vínculo empregatício.
#### Comentário Extra Dia 1.8

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Registro de pessoa jurídica](semana_01_estudo.md#s1-d1-registro-pj)

- **Alternativa correta:** B.
- **A) está errada:** CNPJ não resolve sozinho a sujeição profissional.
- **B) está correta:** Atividade básica no campo regulado pode exigir registro, fiscalização e responsabilidade técnica.
- **C) está errada:** Pessoa jurídica também pode ser objeto de registro e fiscalização.
- **D) está errada:** A atuação ordinária na jurisdição cabe ao CRA.
- **Conceito cobrado:** Registro de pessoa jurídica.
- **Pegadinha usada:** Tratar formalidade empresarial como substituta da regularidade profissional.
- **Como pensar para acertar:** Comece pela atividade efetivamente oferecida e depois identifique a jurisdição.
#### Comentário Extra Dia 1.9

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Ética profissional](semana_01_estudo.md#s1-d1-etica)

- **Alternativa correta:** A.
- **A) está correta:** Vantagem comercial não afasta sigilo; revelação exige fundamento legítimo e limite de necessidade.
- **B) está errada:** Ausência de dano provado não autoriza compartilhar informação confidencial.
- **C) está errada:** O sigilo não transforma toda determinação legal válida em impossível.
- **D) está errada:** Interesse competitivo não retira a confidencialidade.
- **Conceito cobrado:** Sigilo profissional e revelação legítima.
- **Pegadinha usada:** Confundir exceção fundada com conveniência comercial.
- **Como pensar para acertar:** Teste finalidade, fundamento e extensão da eventual revelação.
#### Comentário Extra Dia 1.10

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Ética profissional](semana_01_estudo.md#s1-d1-etica)

- **Alternativa correta:** C.
- **A) está errada:** Experiência do terceiro não substitui exame e autoria responsáveis.
- **B) está errada:** A infração não depende de dano financeiro consumado.
- **C) está correta:** Nome, assinatura e registro pressupõem participação e responsabilidade reais.
- **D) está errada:** Informação interna não corrige a cessão formal sem revisão.
- **Conceito cobrado:** Empréstimo de nome ou registro.
- **Pegadinha usada:** Tratar assinatura como formalidade sem autoria.
- **Como pensar para acertar:** Pergunte quem examinou, assumiu e pode responder tecnicamente pelo trabalho.
#### Comentário Extra Dia 1.11

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [Fiscalização e processo](semana_01_estudo.md#s1-d1-fiscalizacao-processo)

- **Alternativa correta:** B.
- **A) está errada:** Fiscalização regular não depende sempre de ordem judicial específica.
- **B) está correta:** Obstrução pode ser apurada regionalmente, com contraditório e defesa.
- **C) está errada:** Não se elimina instrução e competência regional por remessa imediata ao CFA.
- **D) está errada:** Documento pertinente e regularmente solicitado não é sempre facultativo.
- **Conceito cobrado:** Fiscalização, competência e devido processo.
- **Pegadinha usada:** Opor fiscalização e garantias processuais como se fossem incompatíveis.
- **Como pensar para acertar:** Verifique validade da solicitação, órgão competente e etapa processual.
#### Comentário Extra Dia 1.12

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Contribuições aos conselhos](semana_01_estudo.md#s1-d1-contribuicoes)

- **Alternativa correta:** D.
- **A) está errada:** Regimento do CRA-PR é objeto de resolução específica.
- **B) está errada:** Código de Ética não é o objeto da Lei nº 12.514/2011.
- **C) está errada:** A lei não substitui o regulamento técnico de registro.
- **D) está correta:** A norma é relevante para contribuições devidas aos conselhos profissionais.
- **Conceito cobrado:** Lei nº 12.514/2011.
- **Pegadinha usada:** Trocar objeto financeiro por Regimento, Ética ou Registro.
- **Como pensar para acertar:** Associe a lei às contribuições e sua cobrança.
#### Comentário Extra Dia 1.13

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Regulamento de registro](semana_01_estudo.md#s1-d1-registro-rn649-670)

- **Alternativa correta:** C.
- **A) está errada:** O Regimento do CRA-PR é aprovado pela RN nº 651/2024.
- **B) está errada:** O Código de Ética adotado é a RN nº 671/2025.
- **C) está correta:** A RN nº 649/2024 aprova o regulamento de registro.
- **D) está errada:** Contribuições não constituem seu objeto exclusivo.
- **Conceito cobrado:** Objeto da RN CFA nº 649/2024.
- **Pegadinha usada:** Trocar os objetos das resoluções.
- **Como pensar para acertar:** Use a matriz norma → objeto antes de analisar detalhes.
#### Comentário Extra Dia 1.14

- **Nível: Difícil**
- **Uso:** Aprofundamento
- **Referência:** [RN 649/2024 e RN 670/2025](semana_01_estudo.md#s1-d1-registro-rn649-670)

- **Alternativa correta:** A.
- **A) está correta:** A RN nº 649 fornece o regulamento-base e a RN nº 670 altera dispositivo dele.
- **B) está errada:** A alteração não revoga integralmente todo o regulamento.
- **C) está errada:** Nenhuma das duas converte o objeto em Ética ou Regimento do CRA-PR.
- **D) está errada:** A RN nº 670 interfere diretamente no regulamento de registro.
- **Conceito cobrado:** Norma-base e norma alteradora.
- **Pegadinha usada:** Ler a norma alteradora como substituição integral ou objeto autônomo.
- **Como pensar para acertar:** Identifique primeiro o texto-base e depois o dispositivo alterado.
#### Comentário Extra Dia 1.15

- **Nível: Muito difícil**
- **Uso:** Simulado
- **Referência:** [Normas dirigidas e controle de fonte](semana_01_estudo.md#s1-d1-normas-dirigidas)

- **Alternativa correta:** C.
- **A) está errada:** Norma alteradora não resolve automaticamente todos os objetos nem substitui integralmente a base.
- **B) está errada:** A RN nº 671/2025 é a fonte ética vigente indicada, e a revogação da RN nº 640/2024 não pode ser ignorada.
- **C) está correta:** A seleção separa registro, ética e funcionamento interno e ainda exige controle de vigência e hierarquia.
- **D) está errada:** Inverte os objetos e usa numeração como falsa medida de hierarquia.
- **Conceito cobrado:** Proveniência, objeto, vigência e hierarquia normativa.
- **Pegadinha usada:** Escolher fonte pelo número ou pela novidade sem conferir o objeto.
- **Como pensar para acertar:** Para cada problema, selecione a fonte pelo objeto e confirme sua relação temporal.
#### Comentário Extra Dia 1.16

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Conectores](semana_01_estudo.md#s1-d1-portugues-conectores)

- **Alternativa correta:** D.
- **A) está errada:** A expressão não introduz condição.
- **B) está errada:** Oposição exigiria conector adversativo.
- **C) está errada:** Existe relação lógica explícita com o período anterior.
- **D) está correta:** “Por isso” introduz conclusão ou consequência.
- **Conceito cobrado:** Conector conclusivo.
- **Pegadinha usada:** Trocar consequência por condição, oposição ou adição.
- **Como pensar para acertar:** Substitua mentalmente por “portanto” e teste o sentido.
#### Comentário Extra Dia 1.17

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Referência pronominal](semana_01_estudo.md#s1-d1-portugues-referencia)

- **Alternativa correta:** A.
- **A) está correta:** “Suas” concorda com “conclusões”, a coisa possuída, e não identifica sozinho se o possuidor é a comissão ou o edital.
- **B) está errada:** A flexão do possessivo não concorda com o possuidor e, portanto, não elimina a segunda leitura.
- **C) está errada:** Proximidade não torna o edital referente obrigatório nem resolve toda ambiguidade.
- **D) está errada:** Não há candidato expresso nem necessidade gramatical de pressupor um referente oculto.
- **Conceito cobrado:** Ambiguidade de pronome possessivo.
- **Pegadinha usada:** Usar concordância ou proximidade como regra automática para identificar o possuidor.
- **Como pensar para acertar:** Separe a coisa possuída do possuidor e teste se o contexto exclui uma das leituras.
#### Comentário Extra Dia 1.18

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Reescrita e restrição](semana_01_estudo.md#s1-d1-portugues-reescrita)

- **Alternativa correta:** C.
- **A) está errada:** Remove a restrição imposta por “somente”.
- **B) está errada:** Nega o encaminhamento autorizado pelo original.
- **C) está correta:** “Apenas” conserva o valor restritivo de “somente”.
- **D) está errada:** Desloca a restrição e altera a ordem dos fatos.
- **Conceito cobrado:** Reescrita e operador restritivo.
- **Pegadinha usada:** Preservar palavras, mas mudar o alcance da restrição.
- **Como pensar para acertar:** Identifique exatamente qual conjunto “somente” limita.
#### Comentário Extra Dia 1.19

- **Nível: Médio**
- **Uso:** Essenciais
- **Referência:** [Crase](semana_01_estudo.md#s1-d1-portugues-crase)

- **Alternativa correta:** D.
- **A) está errada:** Não ocorre crase antes de verbo.
- **B) está errada:** “Todos” não admite artigo feminino nessa construção.
- **C) está errada:** “Setor” é substantivo masculino.
- **D) está correta:** Há preposição `a` exigida por “encaminhar” e artigo feminino de “unidade”.
- **Conceito cobrado:** Crase.
- **Pegadinha usada:** Aplicar acento antes de verbo, pronome ou palavra masculina.
- **Como pensar para acertar:** Verifique separadamente a preposição regente e a possibilidade de artigo feminino.
#### Comentário Extra Dia 1.20

- **Nível: Médio**
- **Uso:** Revisão
- **Referência:** [Conectores](semana_01_estudo.md#s1-d1-portugues-conectores)

- **Alternativa correta:** C.
- **A) está errada:** “Embora” não introduz causa direta.
- **B) está errada:** Conclusão seria marcada por “portanto” ou equivalente.
- **C) está correta:** O conector apresenta fato contrário à expectativa sem impedir a oração principal.
- **D) está errada:** Condição seria introduzida por “se” ou “caso”.
- **Conceito cobrado:** Concessão.
- **Pegadinha usada:** Confundir concessão com causa, conclusão ou condição.
- **Como pensar para acertar:** Procure a quebra de expectativa expressa por “embora”.
---

# Dia 2 — Sistemas Operacionais

**Base usada:** edital vigente, apostila de estudo v1.3 e fontes oficiais/estilo indicadas no início deste arquivo.

**Calendário de uso:** a primeira passagem termina após a resolução e a correção de `Q1`, `Q2`, `Q3`, `Q6`, `Q9`, `Q13`, `Q15`, `Q18`, `E3` e `E20`. As outras dez Essenciais — `Q4`, `Q5`, `Q7`, `Q12`, `Q14`, `Q16`, `Q22`, `E1`, `E5` e `E16` — abrem D+2 e devem ser corrigidas antes do Aprofundamento. O saldo de Aprofundamento continua antes de D+7; Revisão fica em D+7; Simulado pertence ao ciclo seguinte.

## Questões principais

### Questão 1
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Conceito, kernel e chamadas de sistema](semana_01_estudo.md#s1-d2-so-kernel)

Em um órgão público, um sistema de protocolo fica lento quando vários usuários acessam relatórios ao mesmo tempo. O sistema operacional atua nesse cenário principalmente para:

A) transformar todo processo em arquivo permanente.
B) substituir o banco de dados relacional em todas as consultas.
C) gerenciar processos, memória, arquivos e dispositivos compartilhados.
D) eliminar a necessidade de autenticação de usuários.

### Questão 2
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

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
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

Um processo que aguarda leitura de disco ser concluída normalmente está no estado:

A) executando na CPU.
B) pronto, obrigatoriamente.
C) zumbi desde o início da leitura.
D) bloqueado/esperando.

### Questão 4
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

No escalonamento preemptivo, o sistema operacional:

A) desativa interrupções de temporizador permanentemente.
B) pode interromper um processo em execução para dar CPU a outro.
C) executa apenas um programa por inicialização do computador.
D) precisa esperar o processo terminar voluntariamente em todos os casos.

### Questão 5
**Nível: Difícil**
**Uso:** Essenciais
**Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

Um servidor apresenta 95% da RAM ocupada, faltas de página em sequência, disco saturado e pouco trabalho útil concluído. Depois de confirmar que os conjuntos de trabalho não cabem na memória física, o diagnóstico e a intervenção coerentes são:

A) contenção de CPU; aumentar o quantum para impedir que páginas sejam retiradas da cache.
B) deadlock de E/S; reiniciar o serviço para romper necessariamente a espera circular entre páginas.
C) thrashing; reduzir a pressão de memória ou ampliar a RAM, em vez de tratar swap como substituta equivalente.
D) journaling excessivo; desativar o registro do sistema de arquivos para eliminar as faltas de página.

### Questão 6
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

Assinale a alternativa correta sobre paginação e segmentação.

A) Paginação usa blocos de tamanho fixo; segmentação usa divisões lógicas de tamanho variável.
B) Paginação usa apenas blocos variáveis; segmentação usa apenas frames fixos.
C) Paginação impede memória virtual.
D) Segmentação é uma política de backup de arquivos.

### Questão 7
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

Assinale a alternativa incorreta sobre memória virtual.

A) É exatamente a mesma coisa que a memória RAM física instalada.
B) Ajuda na proteção entre processos.
C) Pode apoiar execução de programas maiores que a RAM disponível, com uso de armazenamento secundário.
D) Permite que cada processo tenha uma visão própria de espaço de endereçamento.

### Questão 8
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

Um arquivo `C:\Dados\relatorio.pdf` no Windows e `/home/ana/relatorio.pdf` no Linux são exemplos de:

A) permissões de execução.
B) nomes de processos em execução.
C) caminhos absolutos.
D) caminhos relativos.

### Questão 9
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

Um sistema de arquivos com journaling reduz risco de inconsistência após queda de energia porque:

A) elimina permissões de acesso.
B) mantém registros auxiliares de operações para recuperação da estrutura do sistema de arquivos.
C) cria cópias históricas integrais dos documentos e dispensa política separada de retenção e restauração.
D) impede qualquer falha física no disco.

### Questão 10
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

No Linux, a sequência `chmod 640 arquivo.txt` define, em termos gerais:

A) permissões diferentes para usuário, grupo e outros.
B) a troca de proprietário do arquivo para o usuário 640.
C) a criação de um novo processo com PID 640.
D) a compactação do arquivo usando nível 640.

### Questão 11
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

Em um serviço Windows, a execução em segundo plano significa que:

A) o processo nunca consome CPU ou memória.
B) o serviço é sempre malware.
C) o serviço não pode ser monitorado nem registrado nos logs do sistema enquanto permanecer em segundo plano.
D) o serviço pode executar tarefas sem interação direta contínua do usuário.

### Questão 12
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Dispositivos, drivers e spooling](semana_01_estudo.md#s1-d2-dispositivos-spooling)

Um driver de impressora instalado incorretamente pode impedir impressão porque o driver:

A) substitui o spool de impressão e todos os serviços.
B) é sempre dispensável em qualquer hardware moderno.
C) é a memória física reservada para armazenar documentos e controlar permanentemente a fila de impressão.
D) é o software que permite ao SO comunicar-se adequadamente com o dispositivo.

### Questão 13
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

Duas threads incrementam a mesma variável global sem sincronização. Em execuções diferentes, o resultado final varia. O problema descrito é:

A) falha de página, porque a variação indicaria página ausente da memória física.
B) condição de corrida, pois o resultado depende da ordem de interleaving das operações concorrentes.
C) deadlock, pois as threads necessariamente seguram recursos e entram em espera circular.
D) fragmentação externa, porque os endereços da variável foram distribuídos em blocos não contíguos.

### Questão 14
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

Um mutex é usado quando se deseja:

A) garantir exclusão mútua no acesso a uma região crítica.
B) aumentar o tamanho da RAM física.
C) ordenar arquivos em ordem alfabética.
D) substituir o escalonador do sistema operacional.

### Questão 15
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

Considere o cenário: Processo A segura o recurso X e aguarda Y; Processo B segura Y e aguarda X. Se nenhum recurso for liberado, há exemplo de:

A) cache hit.
B) spooling de impressão.
C) starvation sem posse de recurso.
D) deadlock por espera circular.

### Questão 16
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

As condições clássicas associadas ao deadlock incluem:

A) seleção, projeção, junção e divisão.
B) volatilidade, persistência, Unicode e ASCII.
C) exclusão mútua, posse e espera, não preempção e espera circular.
D) legalidade, impessoalidade, moralidade e publicidade, que formam parte dos princípios administrativos expressos.

### Questão 17
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

Em um sistema Unix-like, o filho F1 terminou, mas seu pai ainda não coletou o status. O filho F2 continua executando depois que seu pai terminou e foi adotado por um processo do sistema. Nesse instante, F1 e F2 são, respectivamente:

A) órfão e zumbi, porque ambos perderam o processo que iniciou sua execução.
B) bloqueado e pronto, porque a coleta do status determina a fila da CPU.
C) zumbi e bloqueado, porque adoção impede o segundo filho de executar.
D) zumbi e órfão, pois o primeiro aguarda coleta e o segundo perdeu o pai original.

### Questão 18
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Conceito, kernel e chamadas de sistema](semana_01_estudo.md#s1-d2-so-kernel)

V/F: Sobre chamadas de sistema.

I. Chamadas de sistema permitem que programas solicitem serviços controlados do kernel.
II. Operações de arquivo e E/S podem envolver chamadas de sistema.
III. Chamadas de sistema substituem a CPU durante a execução.

A sequência correta é:

A) F, V, V.
B) V, F, V.
C) V, V, F.
D) F, F, V.

### Questão 19
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

Um administrador usa `ps` e `top` em Linux para investigar lentidão. Essas ferramentas ajudam principalmente a:

A) alterar permissões de arquivos.
B) formatar e verificar partições antes de exibir qualquer informação sobre processos ativos.
C) observar processos e consumo de recursos.
D) compilar kernel automaticamente.

### Questão 20
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

Em um servidor interativo com Round Robin, o quantum foi reduzido de 40 ms para 2 ms. O tempo de resposta inicial melhorou, mas cresceram as trocas de contexto e caiu a parcela de CPU dedicada ao trabalho útil. A interpretação correta é:

A) o quantum curto favoreceu a responsividade, mas elevou o overhead de preempção e restauração de contexto.
B) o quantum curto converteu a política em não preemptiva, e a queda decorre de processos executados até o fim.
C) o quantum passou a representar prioridade fixa, impedindo que processos I/O-bound retornassem à fila.
D) a redução eliminou o custo de alternância; a queda de trabalho útil precisa decorrer apenas de falha de disco.

### Questão 21
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

Um processo CPU-bound é aquele que:

A) é sempre um processo zumbi.
B) passa a maior parte do tempo bloqueado aguardando disco, rede ou outro dispositivo de entrada e saída.
C) usa intensamente processamento, com menor tempo relativo aguardando E/S.
D) não pode ser escalonado.

### Questão 22
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

Assinale a alternativa incorreta sobre permissões e usuários em sistemas operacionais.

A) Permissões ajudam a controlar leitura, escrita e execução de arquivos.
B) Ambientes multiusuário exigem controle de identidade e autorização.
C) Usuário administrador/root deve ser usado com cautela.
D) Permissão de arquivo elimina a necessidade de autenticação de usuários.

### Questão 23
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

Um servidor crítico precisa receber correção de segurança, mas a equipe ainda não confirmou a compatibilidade da aplicação e nunca testou a restauração do backup disponível. A conduta tecnicamente adequada é:

A) aplicar imediatamente em produção, pois correção de segurança torna desnecessários teste e retorno.
B) adiar indefinidamente a correção, pois qualquer risco operacional torna a atualização tecnicamente proibida.
C) testar em ambiente compatível, verificar restauração e rollback, definir janela e registrar o resultado da mudança.
D) copiar apenas os logs atuais e atualizar, pois registros de eventos substituem imagem e backup recuperável.

### Questão 24
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

Um sistema operacional registra eventos de autenticação, falhas de serviço e erros de dispositivo. Esses registros são importantes porque:

A) substituem autenticação, autorização e todos os demais mecanismos preventivos de controle de acesso.
B) são sempre apagados antes de qualquer análise.
C) ajudam auditoria, diagnóstico e investigação de incidentes.
D) impedem automaticamente todo ataque.

### Questão 25
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

Um temporizador interrompe P1 enquanto ele executa; o escalonador escolhe P2, que havia sido interrompido anteriormente. Para que ambos retomem corretamente, o sistema operacional deve:

A) descartar o contador de programa de P1 e reiniciar P2 desde sua primeira instrução.
B) copiar integralmente o espaço virtual de P1 para P2, manter os registradores atuais e dispensar qualquer ponto de retomada.
C) marcar P1 como terminado e P2 como zumbi antes de devolver a CPU ao usuário.
D) salvar registradores e ponto de retomada de P1, restaurar o contexto de P2 e assumir o custo dessa alternância.

### Questão 26
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

A diferença entre caminho relativo e absoluto é que:

A) o absoluto identifica o caminho a partir da raiz/unidade; o relativo depende do diretório atual.
B) o relativo sempre começa pela unidade `C:\`, enquanto o absoluto nunca começa pela raiz `/` nem depende do diretório atual.
C) o absoluto só existe em redes TCP/IP.
D) o relativo contém permissões de execução obrigatoriamente.

### Questão 27
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

Em sistemas Unix-like, `chown` é usado para:

A) alterar apenas bits de permissão numérica como 755.
B) listar processos ativos.
C) encerrar processo por sinal.
D) alterar proprietário e/ou grupo de arquivo.

### Questão 28
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

Um processo de baixa prioridade permanece pronto, mas novas tarefas prioritárias sempre o ultrapassam. Não existe ciclo de recursos retidos, e elevar gradualmente sua prioridade faria com que voltasse a executar. O quadro e a técnica descritos são:

A) starvation e aging, pois há espera indefinida por política, sem necessidade de espera circular.
B) deadlock e journaling, pois toda espera prolongada decorre necessariamente de ciclo entre processos e operações do sistema de arquivos.
C) processo zumbi e reaping, pois o processo já terminou e precisa ter seu status coletado.
D) thrashing e swap, pois a fila de prontos é consequência necessária de faltas de página.

### Questão 29
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Virtualização e isolamento](semana_01_estudo.md#s1-d2-virtualizacao)

Uma equipe compara duas opções no mesmo hospedeiro: executar um sistema convidado completo em máquina virtual ou executar a aplicação em contêiner. Ela precisa identificar o que é compartilhado, o limite de isolamento e o custo aceito. Assinale a análise correta.

A) ambas compartilham obrigatoriamente o kernel do hospedeiro; a VM apenas acrescenta diretórios e não altera custo.
B) o contêiner possui kernel convidado integralmente independente; por isso sempre isola mais falhas, exige mais recursos físicos e elimina a necessidade de atualizar o hospedeiro.
C) a VM elimina dependência do hardware e de backup; o contêiner elimina a necessidade de controle de acesso.
D) a VM pode executar kernel convidado sobre recursos mediados; o contêiner compartilha o kernel hospedeiro, tendendo a menor sobrecarga, mas com outro limite de isolamento.

### Questão 30
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

Um processo realiza dois acessos: primeiro, a uma página válida de seu espaço virtual que não está na RAM; depois, a um endereço que não pertence ao espaço autorizado. O tratamento esperado é, respectivamente:

A) encerrar o processo nos dois acessos, porque todo page fault representa violação fatal.
B) carregar os dois endereços do swap, pois validade e proteção não participam da decisão.
C) tratar a ausência carregando a página válida e sinalizar falha no acesso inválido ou não autorizado.
D) ignorar o primeiro acesso e executar o segundo diretamente, pois a paginação remove a proteção.

### Questão 31
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Dispositivos, drivers e spooling](semana_01_estudo.md#s1-d2-dispositivos-spooling)

Um servidor usa fila de impressão para organizar documentos enviados por vários setores. Essa técnica se relaciona a:

A) deadlock, pois toda fila de dispositivo forma necessariamente ciclo entre processos e recursos.
B) segmentação de memória, pois cada documento ocupa segmento lógico variável antes da impressão.
C) linkedição, pois cada trabalho combina módulos de código antes de alcançar o dispositivo.
D) spooling, que mantém trabalhos em fila intermediária para atendimento pelo dispositivo compartilhado.

### Questão 32
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Windows e Linux](semana_01_estudo.md#s1-d2-windows-linux)

Assinale a alternativa correta sobre NTFS e ext4.

A) São formatos de registradores da CPU.
B) São protocolos de e-mail.
C) São sistemas de arquivos, comuns respectivamente em Windows e Linux.
D) São algoritmos de escalonamento usados para dividir a CPU entre processos de Windows e Linux.

### Questão 33
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

O comando `kill` em Linux:

A) lista exclusivamente diretórios ocultos.
B) envia sinais a processos, frequentemente para solicitar encerramento.
C) remove fisicamente o processador associado ao PID e encerra todos os demais processos dependentes desse hardware.
D) altera permissões de arquivo para 755.

### Questão 34
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

R1, R2 e R3 são exclusivos. P1 mantém R1 e espera R2; P2 mantém R2 e espera R3; P3 mantém R3 e espera R1. Os processos conservam o recurso enquanto esperam, e o sistema não o retira compulsoriamente. Avaliam-se três ações: I — impor ordem global `R1 → R2 → R3` para aquisições futuras; II — aumentar o quantum; III — abortar P2 e liberar R2. Assinale a análise correta.

A) O grafo não possui ciclo por envolver três processos; I serve apenas para melhorar justiça, e III não altera as dependências.
B) O caso é starvation de P3; aging rompe as retenções, enquanto I preserva a espera circular já existente.
C) O grafo contém ciclo sob as demais condições; I previne nova espera circular, e III pode recuperar o caso ao liberar uma aresta do ciclo.
D) Há deadlock, mas I o previne eliminando exclusão mútua; II libera os locks pela preempção da CPU, e III mantém R2 retido.

### Questão 35
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

Um servidor mantém cópia diária em volume permanentemente conectado. Um ransomware cifra os dados de produção e essa cópia; o journal preserva a consistência do sistema de arquivos, mas não recupera o conteúdo anterior. A correção da política deve priorizar:

A) aumentar apenas o journal, porque consistência estrutural cria versões históricas dos arquivos cifrados.
B) manter cópia isolada, definir retenção e testar restauração, além de conservar periodicidade compatível.
C) reduzir a frequência das cópias para impedir que dados corrompidos sejam detectados durante a execução.
D) substituir backup por logs de auditoria, pois o registro do incidente permite reconstruir qualquer arquivo.

### Questão 36
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

Dois processos de usuários distintos precisam trocar mensagens, mas um deles tenta ler diretamente a memória privada do outro. Qual desenho preserva isolamento sem impedir a comunicação legítima?

A) negar o acesso direto e usar mecanismo de IPC controlado pelo sistema operacional, com permissões apropriadas.
B) liberar todo o espaço de endereçamento de ambos, pois autenticação inicial torna qualquer leitura segura.
C) desativar a memória virtual, compartilhar registradores e confiar somente nas permissões de arquivos para separar os usuários.
D) proibir toda comunicação entre processos, porque isolamento e IPC são propriedades incompatíveis.

### Questão 37
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

Um administrador observa que um processo consome 95% de CPU por longo tempo, mas quase não acessa disco. Uma classificação inicial plausível é:

A) arquivo relativo.
B) CPU-bound.
C) I/O-bound.
D) processo zumbi.

### Questão 38
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

Um sistema exige que todo processo adquira recursos na ordem global `R1 → R2 → R3`. Considere os efeitos dessa política.

I. A ordem impede que um processo mantenha R3 enquanto espera R1, rompendo a possibilidade de espera circular.
II. Exclusão mútua pode continuar existindo nos recursos que não admitem compartilhamento.
III. A política garante que nenhum processo sofrerá starvation, independentemente do escalonamento.

Assinale a alternativa correta.

A) Apenas I; a ordem também elimina obrigatoriamente a exclusão mútua.
B) Apenas I e II; ela previne o ciclo, mas não garante justiça de atendimento.
C) Apenas II e III; a ordem preserva o ciclo e elimina espera indefinida.
D) I, II e III; qualquer prevenção de deadlock também impede starvation.

### Questão 39
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

Em sistemas operacionais, a diferença entre autenticação e autorização é:

A) autenticação define permissões e autorização verifica identidade, sempre nessa ordem invertida.
B) ambas significam exatamente a mesma coisa.
C) autorização é usada apenas para memória cache.
D) autenticação verifica identidade; autorização define permissões de acesso.

### Questão 40
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

Assinale a alternativa correta sobre sistemas multitarefa.

A) Multitarefa impede uso de interrupções.
B) Multitarefa só existe quando não há sistema operacional.
C) A alternância rápida entre processos pode dar aparência de execução simultânea em uma CPU.
D) Multitarefa exige um núcleo físico dedicado e executando em paralelo para cada processo existente no sistema.

### Questão 41
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

Um arquivo possui permissão de leitura para o grupo, mas não para “outros”. Isso significa que:

A) o arquivo se torna processo em execução.
B) membros do grupo podem ler; usuários tratados como “outros” dependem das permissões dessa classe.
C) qualquer usuário externo sempre pode ler o arquivo.
D) o proprietário perde automaticamente todas as permissões sempre que alguma autorização é concedida ao grupo.

### Questão 42
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Conceito, kernel e chamadas de sistema](semana_01_estudo.md#s1-d2-so-kernel)

O kernel oferece chamadas de sistema para operações de arquivo porque:

A) aplicações não devem manipular hardware e estruturas críticas diretamente sem controle.
B) aplicações precisam escrever manualmente cada setor físico e decidir sozinhas proteção, concorrência e acesso ao dispositivo.
C) o sistema de arquivos não possui permissões.
D) o kernel é apenas uma interface gráfica.

### Questão 43
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

Em Unix-like, o pai de um processo termina enquanto o filho ainda executa. Mais tarde, o filho adotado também termina, mas o processo adotante ainda não coletou seu status. A sequência correta de classificações é:

A) zumbi enquanto executa e órfão depois que termina, pois a coleta ocorre antes da adoção.
B) órfão após perder o pai original e, depois de terminar, zumbi até que o adotante colete o status.
C) bloqueado após perder o pai e pronto depois de terminar, porque adoção altera apenas a fila da CPU.
D) órfão nas duas etapas, pois um processo adotado não pode gerar informação de término.

### Questão 44
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

Assinale a incorreta sobre swap.

A) Uso excessivo pode degradar o desempenho.
B) Tem a mesma latência e velocidade da memória cache L1.
C) Pode apoiar a memória virtual quando a RAM está pressionada.
D) É normalmente mais lento que acesso à RAM.

### Questão 45
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

Após reinicializar um servidor Linux com `systemd`, o administrador precisa primeiro listar todas as unidades em falha e, depois, inspecionar uma unidade específica. A sequência mais precisa é:

A) `systemctl status` sem identificar unidade; depois `chmod 777` no executável do serviço.
B) `journalctl --vacuum-time=1s`; depois `chown -R` no diretório raiz para recriar permissões.
C) `systemctl --failed`; depois `systemctl status nome.service` e correlação dos logs pelo horário.
D) `ps` para alterar diretamente o estado das unidades do systemd; depois `kill -9` em todos os processos, sem selecionar o serviço investigado.

### Questão 46
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

Em Windows, permissões NTFS são relevantes porque:

A) controlam acesso a arquivos e pastas por usuários/grupos.
B) substituem integralmente autenticação de domínio.
C) servem apenas para colorir ícones.
D) só existem em mídias FAT32.

### Questão 47
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

Uma aplicação faz muitas leituras de rede e fica frequentemente bloqueada aguardando resposta externa. Ela tende a ser:

A) CPU-bound, pois a CPU seria o recurso dominante mesmo durante as esperas de rede descritas.
B) processo zumbi, porque já teria terminado e aguardaria apenas a coleta de seu status.
C) interrupção não mascarável, porque toda espera de rede classifica o processo como evento de hardware.
D) I/O-bound, pois seu progresso depende das respostas externas e de períodos frequentes de espera por E/S.

### Questão 48
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

Assinale a correta sobre monitores, semáforos e mutexes.

A) São modos de endereçamento da CPU.
B) São tipos de backup incremental.
C) São mecanismos/conceitos usados para sincronização de concorrência.
D) São sistemas de arquivos usados pelo Windows para serializar acessos concorrentes a pastas e volumes compartilhados.

### Questão 49
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

Um servidor sofreu queda brusca de energia. Após reiniciar, o sistema de arquivos usa seu journal para reduzir inconsistências. Mesmo assim, o administrador deve:

A) desativar logs para impedir análise.
B) validar dados e usar backups se houver perda ou corrupção de arquivos.
C) descartar todos os backups por serem redundantes.
D) remover permissões, desativar auditoria e considerar a estrutura consistente como prova suficiente de que nenhum dado foi perdido.

### Questão 50
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

Em uma região crítica, a ausência de sincronização adequada pode gerar:

A) inconsistência de dados por acesso concorrente.
B) aumento automático do espaço em disco e preservação do resultado, mesmo quando duas escritas se intercalam.
C) criação automática de usuários.
D) desativação de todo o escalonamento.

## Banco complementar do Dia 2

#### Extra Dia 2.1
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

**Área:** Administração Pública.

Uma chefia afirma que a busca por eficiência permite omitir resultado administrativo cuja divulgação é obrigatória e para o qual não existe sigilo legal. À luz dos princípios expressos do art. 37, assinale a alternativa correta.

A) A eficiência prevalece isoladamente e autoriza afastar a regra jurídica quando houver ganho de tempo.
B) A publicidade é absoluta e exige divulgação integral até mesmo de dados protegidos por restrição legal.
C) Legalidade e publicidade continuam aplicáveis; eficiência não legitima ocultação sem fundamento jurídico.
D) A impessoalidade exige que nenhum ato identifique o órgão responsável por sua prática ou divulgação.

#### Extra Dia 2.2
**Nível: Médio**
**Uso:** Revisão
**Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

**Área:** Administração Pública.

Uma autoridade escolhe beneficiário de decisão administrativa apenas por amizade, embora existam critérios objetivos aplicáveis. O princípio diretamente violado é:

A) impessoalidade, porque a decisão deve perseguir finalidade pública sem favorecimento pessoal.
B) publicidade, porque toda escolha administrativa precisa ser transmitida em sessão pública ao vivo.
C) eficiência, porque esse princípio exige selecionar sempre a alternativa de menor custo financeiro.
D) moralidade, exclusivamente, pois favorecimento pessoal nunca repercute sobre a impessoalidade.

#### Extra Dia 2.3
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

**Área:** Administração Pública.

Assinale a alternativa que diferencia corretamente órgão e entidade na organização administrativa.

A) Órgão e entidade possuem sempre personalidade jurídica própria, diferenciando-se apenas pelo nome legal.
B) Entidade integra necessariamente a mesma pessoa política e resulta apenas de desconcentração interna.
C) Órgão pertence exclusivamente à Administração Indireta, enquanto toda entidade existe apenas dentro da Administração Direta e sem personalidade própria.
D) Órgão integra a estrutura de uma pessoa; entidade possui personalidade própria e pode compor a Administração Indireta.

#### Extra Dia 2.4
**Nível: Médio**
**Uso:** Simulado
**Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

**Área:** Administração Pública.

Considerando especificamente a natureza e a atuação institucional do CRA-PR, assinale a alternativa correta.

A) É associação privada comum, sem personalidade de direito público, poder de fiscalização profissional ou vínculo com a Administração Indireta.
B) Integra a Administração Indireta como entidade autárquica de fiscalização profissional, nos limites de sua competência.
C) É órgão interno do CFA, sem personalidade própria e sem autonomia administrativa ou financeira.
D) Integra a Administração Direta estadual porque sua jurisdição territorial coincide com o Estado do Paraná.

#### Extra Dia 2.5
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

**Área:** Administração Pública.

Uma lei cria entidade com personalidade jurídica própria para executar atividade administrativa típica, sujeita a controle finalístico. Essa entidade:

A) é órgão desconcentrado, pois a personalidade própria não interfere na posição administrativa.
B) é autarquia da Administração Indireta, distinta dos órgãos sem personalidade jurídica própria.
C) integra a Administração Direta, porque toda atividade pública pertence à pessoa política originária.
D) transforma-se em empresa privada, pois descentralização e personalidade afastam o regime público.

#### Extra Dia 2.6
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Ato administrativo, competência, anulação e revogação](semana_01_estudo.md#s1-d2-atos-controle)

**Área:** Administração Pública.

Uma autoridade sem atribuição legal aplica penalidade. O ato observa a forma prevista e descreve fatos verdadeiros, mas a competência não foi delegada nem admitia escolha livre. Qual conclusão é adequada?

A) O ato é válido, porque forma e motivo corretos suprem a falta de atribuição da autoridade.
B) O vício recai sobre a finalidade, pois competência corresponde ao resultado material produzido.
C) A discricionariedade permite conservar o ato sempre que a autoridade alegar interesse público.
D) O elemento competência está viciado, e a ilegalidade exige controle próprio; conveniência não sana a falta.

#### Extra Dia 2.7
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Ato administrativo, competência, anulação e revogação](semana_01_estudo.md#s1-d2-atos-controle)

**Área:** Administração Pública.

Uma autoridade usa poder de fiscalização formalmente existente para perseguir desafeto, e não para proteger o interesse público previsto na norma. O caso indica:

A) desvio de finalidade, capaz de viciar o ato apesar da aparência formal de competência.
B) mera opção de mérito insuscetível de controle, pois a finalidade pode ser escolhida pelo agente.
C) vício apenas de forma, corrigido com nova publicação do mesmo ato e dos mesmos motivos pessoais.
D) exercício regular de eficiência, porque alcançar rapidamente um resultado afasta a finalidade legal.

#### Extra Dia 2.8
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Ato administrativo, competência, anulação e revogação](semana_01_estudo.md#s1-d2-atos-controle)

**Área:** Administração Pública.

A Administração identifica dois atos: X nasceu ilegal por falta de competência; Y é válido, mas deixou de ser conveniente. Respeitados os demais requisitos, as providências correspondentes são:

A) revogar X e anular Y, porque mérito administrativo precede sempre a análise de legalidade.
B) anular X por ilegalidade e revogar Y por conveniência e oportunidade.
C) revogar ambos, pois a Administração nunca pode anular os próprios atos ilegais.
D) anular ambos, porque todo ato inconveniente se torna automaticamente ilegal.

#### Extra Dia 2.9
**Nível: Médio**
**Uso:** Revisão
**Referência:** [LAI e LGPD](semana_01_estudo.md#s1-d2-lai-lgpd)

**Área:** Administração Pública.

Um pedido de acesso alcança documento público que contém trecho divulgável e dado pessoal protegido sem relevância para a finalidade do requerimento. A resposta compatível com a LAI é:

A) negar integralmente o documento, porque a presença de qualquer dado pessoal torna todo conteúdo secreto.
B) divulgar integralmente, porque publicidade elimina a proteção jurídica de dados mantidos pelo poder público.
C) ignorar o pedido até que o titular do dado autorize formalmente qualquer informação institucional.
D) analisar acesso parcial, restrição ou ocultação do dado protegido e fundamentar a decisão sobre o restante.

#### Extra Dia 2.10
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [LAI e LGPD](semana_01_estudo.md#s1-d2-lai-lgpd)

**Área:** Administração Pública.

Um cidadão pede, com base na LAI, dados estatísticos de atendimento e a planilha bruta que também contém CPF, endereço e diagnóstico individual. O órgão precisa conciliar transparência e proteção de dados. Assinale a solução que aplica corretamente os filtros necessários.

A) identificar a finalidade pública, entregar a parcela estatística e avaliar anonimização ou restrição dos dados pessoais, com fundamento expresso.
B) recusar tudo apenas porque existe CPF na planilha, sem separar conteúdo público de informação pessoal.
C) publicar a planilha bruta integralmente, pois o pedido baseado na LAI torna finalidade, necessidade, anonimização e segurança requisitos facultativos para o poder público.
D) exigir consentimento de todos os titulares como única base possível, mesmo para produzir estatística pública anônima.

#### Extra Dia 2.11
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Improbidade administrativa](semana_01_estudo.md#s1-d2-improbidade)

**Área:** Administração Pública.

Um servidor interpreta norma complexa de modo razoável, sem dolo ou benefício, e o ato é posteriormente anulado. Em outro caso, agente direciona deliberadamente ato para obter vantagem tipificada em lei. À luz da disciplina vigente, assinale a alternativa correta.

A) Os dois casos configuram automaticamente improbidade, porque a anulação administrativa prova o elemento subjetivo.
B) Ilegalidade isolada não basta; o segundo caso ainda exige comprovação de conduta dolosa, tipo legal e nexo pertinente.
C) Apenas o primeiro caso configura improbidade, pois erro interpretativo é mais grave que vantagem deliberada.
D) Nenhum caso pode configurar improbidade, porque agentes públicos respondem somente na esfera disciplinar.

#### Extra Dia 2.12
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Improbidade administrativa](semana_01_estudo.md#s1-d2-improbidade)

**Área:** Administração Pública.

Um agente usa dolosamente o cargo para incorporar vantagem patrimonial indevida ao próprio patrimônio. Em tese, a categoria clássica mais diretamente relacionada é:

A) mera irregularidade formal, independentemente do benefício obtido ou do elemento subjetivo.
B) lesão culposa presumida, porque toda vantagem dispensa tipificação e prova de conduta.
C) enriquecimento ilícito, desde que o caso seja enquadrado nos requisitos legais aplicáveis.
D) violação administrativa atípica, pois vantagem patrimonial nunca integra a Lei de Improbidade.

#### Extra Dia 2.13
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Licitações, pregão, dispensa e inexigibilidade](semana_01_estudo.md#s1-d2-licitacoes)

**Área:** Administração Pública.

Um edital válido estabelece critério objetivo de julgamento. Depois de abertas as propostas, a comissão pretende adotar critério novo para favorecer solução que considera tecnicamente melhor, sem alterar formalmente o procedimento. A conclusão correta é:

A) o critério novo pode ser aplicado sem motivação, porque julgamento técnico afasta as regras do edital.
B) a comissão pode escolher qualquer critério após conhecer as propostas, desde que mencione eficiência.
C) a vinculação alcança apenas licitantes; a Administração não precisa observar as regras que publicou.
D) o julgamento deve respeitar edital e legalidade; mudança válida exige procedimento próprio, publicidade e motivação.

#### Extra Dia 2.14
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Licitações, pregão, dispensa e inexigibilidade](semana_01_estudo.md#s1-d2-licitacoes)

**Área:** Administração Pública.

O órgão avalia dois objetos. O primeiro é serviço comum com padrões objetivos e vários fornecedores. O segundo depende de fornecedor exclusivo, condição devidamente comprovada. Mesmo na contratação direta, haverá instrução e motivação. Assinale o enquadramento correto.

A) o primeiro conduz ordinariamente ao pregão; o segundo pode admitir inexigibilidade pela competição inviável, com processo motivado.
B) ambos exigem inexigibilidade, porque definir padrão objetivo torna a competição tecnicamente impossível.
C) o primeiro admite dispensa por preferência administrativa sem hipótese legal; o segundo dispensa instrução, justificativa e motivação porque a exclusividade foi alegada.
D) ambos devem ser contratados por leilão, pois pluralidade ou exclusividade não alteram a modalidade aplicável.

#### Extra Dia 2.15
**Nível: Médio**
**Uso:** Simulado
**Referência:** [Licitações, pregão, dispensa e inexigibilidade](semana_01_estudo.md#s1-d2-licitacoes)

**Área:** Administração Pública.

Um órgão pretende contratar serviço comum, com padrões de desempenho e qualidade objetivamente definidos, e não há inviabilidade de competição demonstrada. A modalidade ordinariamente adequada é:

A) concurso, porque todo serviço prestado à Administração constitui trabalho técnico ou artístico premiado.
B) pregão, pois o objeto comum admite disputa segundo critérios objetivos previstos na Lei nº 14.133/2021.
C) leilão, porque serviços comuns devem ser alienados ao licitante que oferecer o maior lance.
D) inexigibilidade, porque a descrição objetiva do objeto torna impossível comparar fornecedores concorrentes.

#### Extra Dia 2.16
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Concordância e verbo haver impessoal](semana_01_estudo.md#s1-d2-portugues-concordancia)

**Área:** Língua Portuguesa/interpretação.

Assinale a frase em que a concordância verbal está adequada.

A) Havia muitos processos pendentes no setor.
B) Existia muitos processos pendentes no setor.
C) Haviam muitos processos pendentes no setor.
D) Foi analisado as planilhas do setor.

#### Extra Dia 2.17
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Referência pronominal e uso de onde](semana_01_estudo.md#s1-d2-portugues-ambiguidade-onde)

**Área:** Língua Portuguesa/interpretação.

No período "O servidor informou ao candidato que seu recurso fora analisado", há possível ambiguidade porque:

A) o verbo 'informou' está sem complemento.
B) o pronome 'seu' pode se referir ao servidor ou ao candidato.
C) a forma 'fora' indica futuro do presente.
D) a palavra 'recurso' elimina qualquer dupla interpretação, ainda que o possessivo permaneça ligado a dois antecedentes possíveis.

#### Extra Dia 2.18
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Referência pronominal e uso de onde](semana_01_estudo.md#s1-d2-portugues-ambiguidade-onde)

**Área:** Língua Portuguesa/interpretação.

Assinale a frase em que "onde" foi empregado adequadamente.

A) O setor onde os documentos são arquivados será reorganizado.
B) A situação onde ocorreu o erro será analisada.
C) A norma onde consta o prazo foi revogada.
D) O procedimento onde o candidato recorreu foi digital.

#### Extra Dia 2.19
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Pontuação e restrição de sentido](semana_01_estudo.md#s1-d2-portugues-pontuacao)

**Área:** Língua Portuguesa/interpretação.

Assinale a alternativa em que a pontuação preserva melhor a clareza.

A) Após a conferência dos dados a equipe, publicou o resultado.
B) Após, a conferência dos dados a equipe publicou o resultado.
C) Após a conferência, dos dados a equipe publicou, o resultado.
D) Após a conferência dos dados, a equipe publicou o resultado.

#### Extra Dia 2.20
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Comando negativo e inferência literal](semana_01_estudo.md#s1-d2-portugues-comando)

**Área:** Língua Portuguesa/interpretação.

Leia: "O parecer não elimina a necessidade de nova análise." Infere-se corretamente que:

A) a nova análise foi dispensada pelo parecer.
B) o parecer proibiu qualquer análise futura.
C) ainda será necessária nova análise.
D) a análise anterior foi anulada automaticamente.


## Gabarito do Dia 2

1. C
2. A
3. D
4. B
5. C
6. A
7. A
8. C
9. B
10. A
11. D
12. D
13. B
14. A
15. D
16. C
17. D
18. C
19. C
20. A
21. C
22. D
23. C
24. C
25. D
26. A
27. D
28. A
29. D
30. C
31. D
32. C
33. B
34. C
35. B
36. A
37. B
38. B
39. D
40. C
41. B
42. A
43. B
44. B
45. C
46. A
47. D
48. C
49. B
50. A

### Gabarito do banco complementar do Dia 2

Extra Dia 2.1: C
Extra Dia 2.2: A
Extra Dia 2.3: D
Extra Dia 2.4: B
Extra Dia 2.5: B
Extra Dia 2.6: D
Extra Dia 2.7: A
Extra Dia 2.8: B
Extra Dia 2.9: D
Extra Dia 2.10: A
Extra Dia 2.11: B
Extra Dia 2.12: C
Extra Dia 2.13: D
Extra Dia 2.14: A
Extra Dia 2.15: B
Extra Dia 2.16: A
Extra Dia 2.17: B
Extra Dia 2.18: A
Extra Dia 2.19: D
Extra Dia 2.20: C


## Comentários do Dia 2

### Comentário da Questão 1
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Conceito, kernel e chamadas de sistema](semana_01_estudo.md#s1-d2-so-kernel)

- **Alternativa correta:** C.
- **A) está errada:** Processo em execução não é convertido em arquivo por definição.
- **B) está errada:** O SO não substitui o SGBD; cada camada tem função própria.
- **C) está correta:** O SO coordena recursos para aplicações concorrentes.
- **D) está errada:** SO pode apoiar autenticação, mas não elimina a necessidade de controle.
- **Conceito cobrado:** Funções do sistema operacional.
- **Pegadinha usada:** Confundir SO com SGBD ou aplicativo.
- **Como pensar para acertar:** Identifique a camada que gerencia recursos básicos do computador.

### Comentário da Questão 2
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

- **Alternativa correta:** A.
- **A) está correta:** Programa e processo estão corretamente diferenciados; thread costuma compartilhar recursos do processo.
- **B) está errada:** III está errada porque thread não é sempre processo independente.
- **C) está errada:** I é verdadeira e III é falsa.
- **D) está errada:** Inclui III, que generaliza incorretamente thread.
- **Conceito cobrado:** Programa, processo e thread.
- **Pegadinha usada:** Tratar thread como processo isolado em todos os recursos.
- **Como pensar para acertar:** Separe código armazenado, execução com contexto e linha de execução.

### Comentário da Questão 3
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

- **Alternativa correta:** D.
- **A) está errada:** Se aguarda E/S, em regra não está usando a CPU.
- **B) está errada:** Pronto significa apto a executar; aqui falta evento de E/S.
- **C) está errada:** Zumbi é processo terminado aguardando coleta de status.
- **D) está correta:** Ele não pode prosseguir até a conclusão da E/S.
- **Conceito cobrado:** Estados de processo.
- **Pegadinha usada:** Confundir bloqueado com pronto ou zumbi.
- **Como pensar para acertar:** Pergunte se o processo está apto a executar agora. Se depende de evento, está bloqueado.

### Comentário da Questão 4
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

- **Alternativa correta:** B.
- **A) está errada:** Temporizador é mecanismo importante para preempção.
- **B) está correta:** Preempção permite retirada da CPU conforme política.
- **C) está errada:** Multitarefa permite alternância entre vários processos.
- **D) está errada:** Isso descreve comportamento não preemptivo/cooperativo.
- **Conceito cobrado:** Escalonamento preemptivo.
- **Pegadinha usada:** Confundir preemptivo com cooperativo.
- **Como pensar para acertar:** Procure a ideia de retirada forçada/controlada da CPU.

### Comentário da Questão 5
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

- **Alternativa correta:** C.
- **A) está errada:** Saturação de disco e faltas de página apontam para memória; quantum não mantém páginas na cache.
- **B) está errada:** O caso não apresenta ciclo de recursos, e reinício não é diagnóstico de deadlock.
- **C) está correta:** Pressão de RAM, paginação intensa e pouco trabalho útil caracterizam thrashing; reduzir a demanda ou ampliar RAM ataca a causa.
- **D) está errada:** Journal e faltas de página pertencem a mecanismos distintos; desativar registro não resolve pressão de memória.
- **Conceito cobrado:** Thrashing, swap e diagnóstico de pressão de memória.
- **Pegadinha usada:** Confundir o recurso saturado com a causa e propor ação que não reduz o conjunto de trabalho.
- **Como pensar para acertar:** Confirme pressão de RAM, faltas, atividade de disco e trabalho útil antes de escolher a intervenção.

### Comentário da Questão 6
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

- **Alternativa correta:** A.
- **A) está correta:** Essa é a distinção clássica cobrada.
- **B) está errada:** Inverte a distinção.
- **C) está errada:** Paginação é técnica comum de implementação de memória virtual.
- **D) está errada:** Segmentação é técnica de organização de memória.
- **Conceito cobrado:** Paginação e segmentação.
- **Pegadinha usada:** Inverter fixo e variável.
- **Como pensar para acertar:** Associe página/frame a tamanho fixo e segmento a unidade lógica.

### Comentário da Questão 7
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

- **Alternativa correta:** A.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) é a incorreta:** Incorreta: memória virtual é abstração; RAM é memória física.
- **B) está correta como afirmação:** Correta: espaços virtuais isolados dificultam acesso indevido.
- **C) está correta como afirmação:** Correta: disco/swap pode apoiar a memória virtual.
- **D) está correta como afirmação:** Correta: a abstração isola processos.
- **Conceito cobrado:** Memória virtual.
- **Pegadinha usada:** Igualar abstração virtual à RAM física.
- **Como pensar para acertar:** Virtual é o que o processo enxerga; físico é onde efetivamente está na RAM.

### Comentário da Questão 8
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

- **Alternativa correta:** C.
- **A) está errada:** São localizações, não permissões.
- **B) está errada:** São caminhos de arquivo, não processos.
- **C) está correta:** Ambos partem da unidade/raiz e indicam localização completa.
- **D) está errada:** Caminho relativo depende do diretório atual; os exemplos não dependem.
- **Conceito cobrado:** Caminhos de arquivos.
- **Pegadinha usada:** Confundir localização de arquivo com permissão ou processo.
- **Como pensar para acertar:** Caminho absoluto não depende do diretório atual.

### Comentário da Questão 9
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

- **Alternativa correta:** B.
- **A) está errada:** Permissões continuam existindo.
- **B) está correta:** Journaling ajuda a restaurar consistência estrutural.
- **C) está errada:** Journaling não recupera necessariamente arquivos apagados ou versões antigas.
- **D) está errada:** Journaling não evita defeito de hardware.
- **Conceito cobrado:** Journaling.
- **Pegadinha usada:** Achar que journaling é backup completo.
- **Como pensar para acertar:** Journaling cuida de consistência; backup cuida de recuperação de dados.

### Comentário da Questão 10
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

- **Alternativa correta:** A.
- **A) está correta:** chmod altera permissões; 640 representa leitura/escrita para dono, leitura para grupo e nenhuma para outros.
- **B) está errada:** Troca de proprietário é com chown, não chmod.
- **C) está errada:** chmod não cria processo.
- **D) está errada:** Não é comando de compactação.
- **Conceito cobrado:** Permissões Linux e chmod.
- **Pegadinha usada:** Confundir chmod e chown.
- **Como pensar para acertar:** Veja o verbo: mode/permissão, não owner/proprietário.

### Comentário da Questão 11
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

- **Alternativa correta:** D.
- **A) está errada:** Serviços podem consumir recursos.
- **B) está errada:** Serviços podem ser legítimos ou maliciosos; não se presume sempre.
- **C) está errada:** Eventos de serviços podem aparecer em logs.
- **D) está correta:** Serviços rodam em background para funções do sistema/aplicações.
- **Conceito cobrado:** Serviços em segundo plano.
- **Pegadinha usada:** Generalizar serviço como malware ou como inofensivo sem análise.
- **Como pensar para acertar:** Serviço é modo de execução; a legitimidade depende do caso.

### Comentário da Questão 12
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Dispositivos, drivers e spooling](semana_01_estudo.md#s1-d2-dispositivos-spooling)

- **Alternativa correta:** D.
- **A) está errada:** Driver e spool têm funções diferentes.
- **B) está errada:** Dispositivos ainda dependem de drivers ou módulos equivalentes.
- **C) está errada:** Driver não é armazenamento físico nem fila permanente de impressão.
- **D) está correta:** Driver traduz comandos do SO/aplicação para o hardware específico.
- **Conceito cobrado:** Drivers de dispositivo.
- **Pegadinha usada:** Confundir driver com hardware ou fila de impressão.
- **Como pensar para acertar:** Driver é camada de controle do dispositivo.

### Comentário da Questão 13
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** B.
- **A) está errada:** Não há indicação de página ausente ou erro de memória virtual.
- **B) está correta:** O resultado depende da ordem de execução concorrente.
- **C) está errada:** Não há descrição de espera circular; há disputa sem sincronização.
- **D) está errada:** O problema é concorrência, não alocação de memória.
- **Conceito cobrado:** Condição de corrida.
- **Pegadinha usada:** Confundir inconsistência concorrente com deadlock.
- **Como pensar para acertar:** Se o resultado depende do timing de threads, pense em corrida.

### Comentário da Questão 14
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** A.
- **A) está correta:** Mutex permite que apenas um fluxo acesse recurso protegido por vez.
- **B) está errada:** Mutex não altera hardware.
- **C) está errada:** Ordenação de arquivos não é função de mutex.
- **D) está errada:** Mutex sincroniza acesso; não escolhe processos para CPU.
- **Conceito cobrado:** Mutex e região crítica.
- **Pegadinha usada:** Atribuir ao mutex funções de desempenho ou escalonamento.
- **Como pensar para acertar:** Associe mutex a “um por vez” em recurso compartilhado.

### Comentário da Questão 15
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** D.
- **A) está errada:** Cache hit ocorre quando dado é encontrado na cache.
- **B) está errada:** Spooling é enfileiramento de trabalhos de E/S.
- **C) está errada:** Starvation é espera indefinida por política; aqui há ciclo de recursos.
- **D) está correta:** Há dependência circular entre processos e recursos.
- **Conceito cobrado:** Deadlock.
- **Pegadinha usada:** Confundir espera circular com lentidão genérica.
- **Como pensar para acertar:** Procure ciclo: A espera B, B espera A.

### Comentário da Questão 16
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** C.
- **A) está errada:** São operações da álgebra relacional.
- **B) está errada:** São conceitos de representação/memória, não condições de deadlock.
- **C) está correta:** Essas são as quatro condições clássicas.
- **D) está errada:** São princípios administrativos, não condições de deadlock.
- **Conceito cobrado:** Condições de deadlock.
- **Pegadinha usada:** Confundir listas de disciplinas diferentes.
- **Como pensar para acertar:** Memorize as quatro condições como um bloco técnico de SO.

### Comentário da Questão 17
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

- **Alternativa correta:** D.
- **A) está errada:** Inverte as classificações: F1 terminou sem coleta, enquanto F2 perdeu o pai original.
- **B) está errada:** Coleta de status e adoção não correspondem aos estados bloqueado e pronto.
- **C) está errada:** F1 é zumbi, mas F2 pode continuar executando após ser adotado; não fica bloqueado por definição.
- **D) está correta:** F1 aguarda reaping como zumbi; F2 é órfão adotado por outro processo do sistema.
- **Conceito cobrado:** Diferença entre processo zumbi e órfão.
- **Pegadinha usada:** Tratar perda do pai e ausência de coleta do status como o mesmo evento.
- **Como pensar para acertar:** Pergunte separadamente se o processo já terminou e se o pai original ainda existe.

### Comentário da Questão 18
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Conceito, kernel e chamadas de sistema](semana_01_estudo.md#s1-d2-so-kernel)

- **Alternativa correta:** C.
- **A) está errada:** I é verdadeira, e III é falsa.
- **B) está errada:** II é verdadeira e III é falsa.
- **C) está correta:** I e II estão corretas; III é falsa porque chamadas não substituem hardware de execução.
- **D) está errada:** I e II não deveriam ser falsas.
- **Conceito cobrado:** Chamadas de sistema.
- **Pegadinha usada:** Atribuir às chamadas de sistema papel físico da CPU.
- **Como pensar para acertar:** Chamadas são interface de solicitação ao kernel.

### Comentário da Questão 19
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

- **Alternativa correta:** C.
- **A) está errada:** chmod/chown são usados para permissões/proprietário.
- **B) está errada:** ps/top não formatam disco.
- **C) está correta:** ps lista processos e top acompanha uso em tempo real.
- **D) está errada:** Essas ferramentas não compilam kernel.
- **Conceito cobrado:** Comandos Linux de processos.
- **Pegadinha usada:** Confundir comandos de monitoramento com comandos de permissão.
- **Como pensar para acertar:** Associe ps/top a processos e desempenho.

### Comentário da Questão 20
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

- **Alternativa correta:** A.
- **A) está correta:** Fatias menores podem melhorar resposta inicial, mas aumentam preempções e custo de troca de contexto.
- **B) está errada:** Round Robin continua preemptivo; quantum curto não faz cada processo executar até terminar.
- **C) está errada:** Quantum é fatia de tempo, não prioridade fixa, e processos de E/S podem retornar à fila.
- **D) está errada:** A própria elevação das trocas explica perda de CPU útil; não é necessário presumir falha de disco.
- **Conceito cobrado:** Trade-off entre quantum, responsividade e overhead.
- **Pegadinha usada:** Avaliar apenas a resposta interativa e ignorar o custo de alternância.
- **Como pensar para acertar:** Compare simultaneamente latência percebida, número de trocas e trabalho útil concluído.

### Comentário da Questão 21
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

- **Alternativa correta:** C.
- **A) está errada:** Zumbi já terminou; CPU-bound está ligado ao perfil de uso.
- **B) está errada:** Isso descreve I/O-bound.
- **C) está correta:** CPU-bound demanda CPU como recurso principal.
- **D) está errada:** Todo processo executável depende de escalonamento.
- **Conceito cobrado:** Processos CPU-bound e I/O-bound.
- **Pegadinha usada:** Confundir gargalo de processamento com E/S.
- **Como pensar para acertar:** Identifique qual recurso limita a execução.

### Comentário da Questão 22
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: permissões limitam operações sobre objetos.
- **B) está correta como afirmação:** Correta: autenticação/autorização são essenciais.
- **C) está correta como afirmação:** Correta: privilégios elevados aumentam risco.
- **D) é a incorreta:** Incorreta: permissão e autenticação são controles complementares.
- **Conceito cobrado:** Usuários, permissões e privilégios.
- **Pegadinha usada:** Confundir autorização com autenticação.
- **Como pensar para acertar:** Primeiro identifica o usuário; depois verifica o que ele pode fazer.

### Comentário da Questão 23
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

- **Alternativa correta:** C.
- **A) está errada:** Urgência de segurança não elimina teste, janela e capacidade de retorno em servidor crítico.
- **B) está errada:** Adiamento indefinido mantém a exposição; risco deve ser tratado, não convertido em proibição absoluta.
- **C) está correta:** A sequência combina compatibilidade, restaurabilidade, rollback, janela e evidência da mudança.
- **D) está errada:** Logs registram eventos, mas não restauram sistema ou dados como imagem e backup recuperável.
- **Conceito cobrado:** Manutenção segura, backup e rollback.
- **Pegadinha usada:** Escolher entre aplicação impulsiva e paralisação, sem montar controles de continuidade.
- **Como pensar para acertar:** Verifique segurança, compatibilidade, recuperação, janela e registro como decisões complementares.

### Comentário da Questão 24
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

- **Alternativa correta:** C.
- **A) está errada:** Controle de acesso e logs têm funções distintas.
- **B) está errada:** Boas práticas preservam logs relevantes.
- **C) está correta:** Logs permitem rastrear eventos e causas prováveis.
- **D) está errada:** Logs ajudam detectar/analisar; não impedem tudo sozinhos.
- **Conceito cobrado:** Logs do sistema.
- **Pegadinha usada:** Achar que log é prevenção completa.
- **Como pensar para acertar:** Log é evidência/registro; prevenção exige controles adicionais.

### Comentário da Questão 25
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

- **Alternativa correta:** D.
- **A) está errada:** Sem o contador de programa, P1 não retomaria corretamente; P2 não deve reiniciar do começo.
- **B) está errada:** Troca de contexto não copia integralmente espaços virtuais nem conserva os registradores de P1 para P2.
- **C) está errada:** Preempção não termina P1, e zumbi é processo já encerrado aguardando coleta.
- **D) está correta:** O SO salva o contexto de P1, restaura o de P2 e paga overhead para alternar execuções.
- **Conceito cobrado:** Sequência e custo da troca de contexto.
- **Pegadinha usada:** Confundir alternância de CPU com cópia de memória ou mudança para estado terminado.
- **Como pensar para acertar:** Identifique o estado mínimo necessário para cada processo continuar do ponto em que parou.

### Comentário da Questão 26
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

- **Alternativa correta:** A.
- **A) está correta:** Essa é a distinção prática em sistemas de arquivos.
- **B) está errada:** Inverte exemplos comuns de Windows/Linux.
- **C) está errada:** Caminhos absolutos existem em sistemas de arquivos locais.
- **D) está errada:** Permissão é outro atributo.
- **Conceito cobrado:** Caminhos absoluto e relativo.
- **Pegadinha usada:** Confundir sintaxe com permissão.
- **Como pensar para acertar:** Pergunte: preciso saber o diretório atual para resolver?

### Comentário da Questão 27
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

- **Alternativa correta:** D.
- **A) está errada:** Isso é função típica de chmod.
- **B) está errada:** ps/top listam processos.
- **C) está errada:** kill envia sinais a processos.
- **D) está correta:** chown vem de change owner.
- **Conceito cobrado:** Comandos Linux.
- **Pegadinha usada:** Trocar chown e chmod.
- **Como pensar para acertar:** Owner indica proprietário; mode indica permissões.

### Comentário da Questão 28
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

- **Alternativa correta:** A.
- **A) está correta:** A espera decorre de política de prioridade, e aging combate a inanição elevando quem aguarda.
- **B) está errada:** Sem ciclo de recursos, não há base para deadlock; journaling não altera prioridades.
- **C) está errada:** O processo permanece pronto e não terminou, portanto não é zumbi nem precisa de reaping.
- **D) está errada:** Não há sinais de pressão de memória, faltas de página ou troca excessiva.
- **Conceito cobrado:** Starvation, ausência de ciclo e aging.
- **Pegadinha usada:** Chamar qualquer espera longa de deadlock ou relacioná-la à memória.
- **Como pensar para acertar:** Procure a causa da falta de progresso e verifique se existe ciclo de recursos retidos.

### Comentário da Questão 29
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Virtualização e isolamento](semana_01_estudo.md#s1-d2-virtualizacao)

- **Alternativa correta:** D.
- **A) está errada:** Contêineres compartilham o kernel; uma VM pode possuir kernel convidado e outro custo operacional.
- **B) está errada:** A alternativa inverte o compartilhamento de kernel e transforma um trade-off em superioridade universal.
- **C) está errada:** Ambas dependem de recursos físicos e continuam exigindo backup, atualização e controle de acesso.
- **D) está correta:** Distingue o que é compartilhado, o limite de isolamento e a tendência de menor sobrecarga do contêiner, sem torná-la absoluta.
- **Conceito cobrado:** VM, contêiner, compartilhamento de kernel e isolamento.
- **Pegadinha usada:** Escolher pela palavra “virtual” sem verificar camada compartilhada e custo aceito.
- **Como pensar para acertar:** Aplique três filtros: kernel, falha que se deseja isolar e recurso operacional consumido.

### Comentário da Questão 30
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

- **Alternativa correta:** C.
- **A) está errada:** Uma página válida apenas não residente pode ser carregada e não exige encerramento.
- **B) está errada:** O SO verifica validade e proteção; endereço inválido não se torna carregável por estar no swap.
- **C) está correta:** Ausência de página válida é tratável; acesso inválido ou não autorizado produz falha de proteção.
- **D) está errada:** Paginação preserva controle de endereços e não autoriza executar acesso inválido diretamente.
- **Conceito cobrado:** Page fault tratável e violação de endereço/proteção.
- **Pegadinha usada:** Tratar todo page fault como fatal ou todo endereço como carregável.
- **Como pensar para acertar:** Decida primeiro se o endereço é válido e autorizado; só depois verifique residência na RAM.

### Comentário da Questão 31
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Dispositivos, drivers e spooling](semana_01_estudo.md#s1-d2-dispositivos-spooling)

- **Alternativa correta:** D.
- **A) está errada:** Fila de impressão não implica deadlock por si só.
- **B) está errada:** Segmentação é memória, não fila de impressão.
- **C) está errada:** Linkedição é construção de programa.
- **D) está correta:** Spooling enfileira trabalhos para dispositivo mais lento/compartilhado.
- **Conceito cobrado:** Spooling.
- **Pegadinha usada:** Confundir fila de E/S com bloqueio.
- **Como pensar para acertar:** Dispositivo compartilhado e fila de trabalhos sugerem spooling.

### Comentário da Questão 32
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Windows e Linux](semana_01_estudo.md#s1-d2-windows-linux)

- **Alternativa correta:** C.
- **A) está errada:** Sistemas de arquivos organizam armazenamento, não registradores.
- **B) está errada:** Protocolos de e-mail são SMTP, IMAP, POP3 etc.
- **C) está correta:** NTFS é comum no Windows; ext4 é comum em Linux.
- **D) está errada:** Escalonamento usa políticas como Round Robin, prioridade etc.
- **Conceito cobrado:** Sistemas de arquivos.
- **Pegadinha usada:** Confundir siglas de sistemas de arquivos com protocolos.
- **Como pensar para acertar:** Associe NTFS/ext4 à organização de arquivos no armazenamento.

### Comentário da Questão 33
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

- **Alternativa correta:** B.
- **A) está errada:** Listagem de arquivos é função de ls.
- **B) está correta:** kill trabalha com sinais como TERM e KILL.
- **C) está errada:** É comando de software, não remoção de hardware.
- **D) está errada:** Isso é chmod.
- **Conceito cobrado:** Sinais e processos Linux.
- **Pegadinha usada:** Interpretar o nome do comando literalmente demais.
- **Como pensar para acertar:** Em Unix/Linux, sinais são mecanismo de controle de processos.

### Comentário da Questão 34
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** C.
- **A) está errada:** Três processos podem formar ciclo; a ordem global atua sobre espera circular, e abortar P2 libera R2.
- **B) está errada:** O cenário satisfaz o ciclo de deadlock, não mera starvation; aging não desfaz recursos já retidos.
- **C) está correta:** O grafo fecha o ciclo, a ordem global previne nova circularidade e a liberação de R2 pode iniciar a recuperação.
- **D) está errada:** A ordem não elimina exclusão mútua; preempção da CPU não libera locks, e o aborto indicado libera R2.
- **Conceito cobrado:** Grafo de espera, condições de deadlock, prevenção e recuperação.
- **Pegadinha usada:** Acertar o diagnóstico, mas atribuir à ação efeito sobre a condição ou aresta errada.
- **Como pensar para acertar:** Desenhe as dependências, confira as quatro condições e teste qual ação rompe condição futura ou aresta atual.

### Comentário da Questão 35
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

- **Alternativa correta:** B.
- **A) está errada:** Journal recupera consistência, mas não cria versão histórica imune à cifra.
- **B) está correta:** Isolamento, retenção e teste de restauração cobrem falha simultânea e recuperabilidade.
- **C) está errada:** Menor frequência amplia possível perda de dados e não impede propagação da corrupção.
- **D) está errada:** Logs ajudam investigação; não contêm necessariamente o conteúdo necessário para restaurar arquivos.
- **Conceito cobrado:** Backup isolado, retenção, restauração e journaling.
- **Pegadinha usada:** Confundir existência de cópia ou journal com capacidade comprovada de recuperação.
- **Como pensar para acertar:** Pergunte se a cópia sobrevive ao mesmo incidente e se sua restauração foi testada.

### Comentário da Questão 36
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

- **Alternativa correta:** A.
- **A) está correta:** Mantém espaços privados e oferece comunicação deliberada por canal controlado e autorizado.
- **B) está errada:** Autenticação não autoriza leitura arbitrária de memória nem substitui isolamento.
- **C) está errada:** Desativar memória virtual reduz proteção, e registradores não são canal geral de IPC.
- **D) está errada:** Isolamento impede acesso indevido, não a comunicação mediada pelo sistema operacional.
- **Conceito cobrado:** Isolamento de endereçamento e IPC controlada.
- **Pegadinha usada:** Tratar proteção e comunicação como escolhas mutuamente excludentes.
- **Como pensar para acertar:** Separe acesso direto indevido de troca explícita por mecanismo autorizado.

### Comentário da Questão 37
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

- **Alternativa correta:** B.
- **A) está errada:** Arquivo relativo não classifica perfil de processo.
- **B) está correta:** O gargalo principal parece ser processamento.
- **C) está errada:** I/O-bound esperaria muito por disco/rede, o que não foi descrito.
- **D) está errada:** Zumbi não consome CPU de forma útil.
- **Conceito cobrado:** CPU-bound.
- **Pegadinha usada:** Confundir consumo de CPU com espera de E/S.
- **Como pensar para acertar:** Olhe o recurso que fica no limite.

### Comentário da Questão 38
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** B.
- **A) está errada:** I é verdadeira, mas II também: recursos ainda podem exigir exclusão mútua.
- **B) está correta:** A ordem rompe a espera circular e preserva possível exclusão mútua, sem garantir justiça.
- **C) está errada:** I é verdadeira e III é falsa; ordem não assegura atendimento de todas as prioridades.
- **D) está errada:** Prevenir o ciclo de deadlock não elimina automaticamente starvation.
- **Conceito cobrado:** Condições de deadlock, prevenção por ordenação e efeito sobre starvation.
- **Pegadinha usada:** Supor que atacar uma condição necessária resolve também exclusão mútua e justiça.
- **Como pensar para acertar:** Avalie separadamente ciclo, compartilhamento do recurso e política de atendimento.

### Comentário da Questão 39
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

- **Alternativa correta:** D.
- **A) está errada:** A alternativa inverte os conceitos.
- **B) está errada:** São controles relacionados, mas distintos.
- **C) está errada:** Autorização trata acesso a recursos em geral.
- **D) está correta:** Primeiro identifica; depois decide o que pode fazer.
- **Conceito cobrado:** Autenticação e autorização.
- **Pegadinha usada:** Confundir identidade com permissão.
- **Como pensar para acertar:** Pergunte: quem é o usuário? Depois: o que ele pode fazer?

### Comentário da Questão 40
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

- **Alternativa correta:** C.
- **A) está errada:** Interrupções ajudam multitarefa.
- **B) está errada:** O SO é o gerenciador típico da multitarefa.
- **C) está correta:** Escalonamento e interrupções permitem compartilhamento da CPU.
- **D) está errada:** Um núcleo pode alternar entre vários processos.
- **Conceito cobrado:** Multitarefa.
- **Pegadinha usada:** Achar que simultaneidade percebida exige núcleo por processo.
- **Como pensar para acertar:** Diferencie paralelismo real e concorrência por alternância.

### Comentário da Questão 41
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

- **Alternativa correta:** B.
- **A) está errada:** Permissão não transforma arquivo em processo.
- **B) está correta:** A tríade usuário-grupo-outros controla permissões distintas.
- **C) está errada:** Sem permissão para outros, leitura não é garantida.
- **D) está errada:** Permissões do proprietário são avaliadas separadamente.
- **Conceito cobrado:** Permissões Linux.
- **Pegadinha usada:** Ignorar a tríade usuário/grupo/outros.
- **Como pensar para acertar:** Leia cada classe de permissão separadamente.

### Comentário da Questão 42
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Conceito, kernel e chamadas de sistema](semana_01_estudo.md#s1-d2-so-kernel)

- **Alternativa correta:** A.
- **A) está correta:** O kernel centraliza controle, segurança e abstração.
- **B) está errada:** A ideia é justamente evitar acesso físico manual direto.
- **C) está errada:** Sistemas de arquivos podem ter permissões; chamadas as respeitam.
- **D) está errada:** Kernel é núcleo do SO, não apenas GUI.
- **Conceito cobrado:** Kernel e chamadas de sistema.
- **Pegadinha usada:** Não perceber a função de proteção/abstração do SO.
- **Como pensar para acertar:** SO protege recursos e fornece serviços padronizados.

### Comentário da Questão 43
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Processos, threads e estados](semana_01_estudo.md#s1-d2-processos-estados)

- **Alternativa correta:** B.
- **A) está errada:** Enquanto executa após perder o pai, o filho é órfão, não zumbi.
- **B) está correta:** A classificação muda de órfão adotado para zumbi quando termina e aguarda coleta.
- **C) está errada:** Perda do pai não determina bloqueio, e processo terminado não retorna à fila de prontos.
- **D) está errada:** Adoção não elimina o registro do término nem a necessidade de reaping.
- **Conceito cobrado:** Transição entre órfão, adoção e zumbi.
- **Pegadinha usada:** Fixar um único rótulo apesar da mudança de estado e do evento de término.
- **Como pensar para acertar:** Monte a linha do tempo: pai termina, adoção ocorre, filho termina, status é coletado.

### Comentário da Questão 44
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Memória virtual, paginação e segmentação](semana_01_estudo.md#s1-d2-memoria-virtual)

- **Alternativa correta:** B.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: muita troca gera lentidão.
- **B) é a incorreta:** Incorreta: swap em disco/SSD é muito mais lento que cache L1.
- **C) está correta como afirmação:** Correta: swap é usado como apoio.
- **D) está correta como afirmação:** Correta: armazenamento secundário é mais lento que RAM.
- **Conceito cobrado:** Swap e desempenho.
- **Pegadinha usada:** Tratar swap como memória rápida.
- **Como pensar para acertar:** Swap ajuda capacidade, mas cobra preço de desempenho.

### Comentário da Questão 45
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Serviços, comandos e logs](semana_01_estudo.md#s1-d2-servicos-logs)

- **Alternativa correta:** C.
- **A) está errada:** `status` sem unidade não substitui a listagem precisa, e `chmod 777` é alteração insegura sem diagnóstico.
- **B) está errada:** Limpar logs destrói evidência; mudar donos recursivamente não identifica unidades em falha.
- **C) está correta:** `--failed` lista as unidades; `status` e os logs contextualizam a unidade escolhida.
- **D) está errada:** `ps` observa processos, mas não altera unidades; encerrar todos indiscriminadamente amplia o incidente.
- **Conceito cobrado:** Sequência de diagnóstico de unidades em falha no systemd.
- **Pegadinha usada:** Escolher comando relacionado, porém com escopo errado ou efeito destrutivo.
- **Como pensar para acertar:** Primeiro liste o conjunto exato, depois aprofunde uma unidade e correlacione o horário.

### Comentário da Questão 46
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Autenticação, autorização e permissões](semana_01_estudo.md#s1-d2-seguranca-permissoes)

- **Alternativa correta:** A.
- **A) está correta:** NTFS permite controle de permissões no sistema de arquivos.
- **B) está errada:** Permissões dependem de identidade autenticada; não substituem autenticação.
- **C) está errada:** Permissões afetam acesso, não aparência.
- **D) está errada:** FAT32 não tem o mesmo modelo robusto de permissões NTFS.
- **Conceito cobrado:** Permissões NTFS.
- **Pegadinha usada:** Confundir autenticação e autorização.
- **Como pensar para acertar:** Permissão responde “pode acessar?” depois de saber quem é o usuário.

### Comentário da Questão 47
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

- **Alternativa correta:** D.
- **A) está errada:** CPU-bound exigiria processamento intenso, não espera de rede.
- **B) está errada:** O processo ainda está ativo aguardando E/S.
- **C) está errada:** Não é tipo de interrupção; é perfil de processo.
- **D) está correta:** O desempenho depende de entrada/saída, como rede.
- **Conceito cobrado:** I/O-bound.
- **Pegadinha usada:** Confundir espera de rede com processamento intensivo.
- **Como pensar para acertar:** Se o processo espera dispositivo/rede/disco, pense em E/S.

### Comentário da Questão 48
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** C.
- **A) está errada:** Modos de endereçamento são outro tema.
- **B) está errada:** Backup incremental é política de cópia, não sincronização.
- **C) está correta:** Todos aparecem no estudo de controle de acesso concorrente.
- **D) está errada:** Sistemas de arquivos incluem NTFS, FAT32, ext4 etc.
- **Conceito cobrado:** Sincronização.
- **Pegadinha usada:** Confundir termos de concorrência com armazenamento.
- **Como pensar para acertar:** Quando o tema é acesso compartilhado, pense em sincronização.

### Comentário da Questão 49
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Sistemas de arquivos, journaling e backup](semana_01_estudo.md#s1-d2-arquivos-backup)

- **Alternativa correta:** B.
- **A) está errada:** Logs ajudam diagnóstico pós-incidente.
- **B) está correta:** Journal não garante recuperação de conteúdo perdido; backup continua essencial.
- **C) está errada:** Backups continuam necessários.
- **D) está errada:** Permissões não devem ser removidas como solução genérica.
- **Conceito cobrado:** Journaling e backup.
- **Pegadinha usada:** Confundir recuperação de consistência com recuperação completa de dados.
- **Como pensar para acertar:** Depois de falha, diferencie estrutura íntegra de dados recuperáveis.

### Comentário da Questão 50
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Concorrência, região crítica e deadlock](semana_01_estudo.md#s1-d2-concorrencia)

- **Alternativa correta:** A.
- **A) está correta:** Região crítica protege recurso compartilhado contra interleavings indevidos.
- **B) está errada:** Sincronização não aumenta armazenamento.
- **C) está errada:** Não há relação com cadastro de usuários.
- **D) está errada:** O escalonador continua existindo.
- **Conceito cobrado:** Região crítica.
- **Pegadinha usada:** Subestimar acesso concorrente.
- **Como pensar para acertar:** Se dois fluxos mexem no mesmo dado, pergunte como o acesso é protegido.

### Comentários do banco complementar do Dia 2

#### Comentário Extra Dia 2.1
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

- **Alternativa correta:** C.
- **A) está errada:** Eficiência opera dentro da legalidade e não cria autorização autônoma para ocultar resultado.
- **B) está errada:** Publicidade admite restrições constitucionais e legais; não é divulgação irrestrita.
- **C) está correta:** A busca por eficiência não afasta legalidade nem publicidade quando inexiste sigilo aplicável.
- **D) está errada:** Impessoalidade combate promoção e favorecimento, mas não apaga a identificação institucional do ato.
- **Conceito cobrado:** Convivência entre legalidade, publicidade e eficiência.
- **Pegadinha usada:** Transformar um princípio em autorização para afastar os demais.
- **Como pensar para acertar:** Verifique a regra jurídica, a existência de sigilo e o limite da eficiência no mesmo caso.

#### Comentário Extra Dia 2.2
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

- **Alternativa correta:** A.
- **A) está correta:** Favorecimento pessoal é incompatível com impessoalidade.
- **B) está errada:** Publicidade não exige transmissão ao vivo de toda escolha e não resolve o favorecimento descrito.
- **C) está errada:** Eficiência não se reduz ao menor preço e não legitima preferência pessoal.
- **D) está errada:** A conduta pode também afrontar moralidade, mas não deixa de atingir diretamente a impessoalidade.
- **Conceito cobrado:** Impessoalidade.
- **Pegadinha usada:** Escolher um princípio relacionado como se ele excluísse o princípio diretamente acionado.
- **Como pensar para acertar:** Procure favorecimento, promoção ou perseguição pessoal diante de critério objetivo.

#### Comentário Extra Dia 2.3
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

- **Alternativa correta:** D.
- **A) está errada:** Órgão não possui necessariamente personalidade; ele integra a estrutura de uma pessoa.
- **B) está errada:** Personalidade própria e descentralização caracterizam entidade, não mera desconcentração interna.
- **C) está errada:** Órgãos também existem na Administração Direta, e entidades podem integrar a Indireta.
- **D) está correta:** A distinção decisiva é estrutura sem personalidade própria versus pessoa administrativa própria.
- **Conceito cobrado:** Organização administrativa.
- **Pegadinha usada:** Chamar autarquia de órgão da Administração Direta.
- **Como pensar para acertar:** Pergunte se existe pessoa jurídica própria ou apenas centro de competências dentro de outra pessoa.

#### Comentário Extra Dia 2.4
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

- **Alternativa correta:** B.
- **A) está errada:** O CRA-PR não é associação privada comum; exerce fiscalização profissional como pessoa de direito público.
- **B) está correta:** A natureza autárquica o situa na Administração Indireta e não elimina os limites de competência.
- **C) está errada:** O CRA-PR possui personalidade e autonomia próprias; não é simples órgão interno do CFA.
- **D) está errada:** Jurisdição estadual não o transforma em órgão da Administração Direta do Estado.
- **Conceito cobrado:** Conselhos profissionais e autarquias.
- **Pegadinha usada:** Inferir a posição administrativa apenas pela área territorial de atuação.
- **Como pensar para acertar:** Separe personalidade, natureza autárquica, autonomia e jurisdição.

#### Comentário Extra Dia 2.5
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [LIMPE, organização administrativa e autarquia](semana_01_estudo.md#s1-d2-limpe-organizacao)

- **Alternativa correta:** B.
- **A) está errada:** Personalidade própria impede classificar a entidade como mero órgão desconcentrado.
- **B) está correta:** Autarquia possui personalidade própria e resulta de descentralização administrativa.
- **C) está errada:** A atividade continua pública, mas a nova pessoa integra a Administração Indireta.
- **D) está errada:** Personalidade não converte automaticamente entidade pública em empresa privada.
- **Conceito cobrado:** Autarquia.
- **Pegadinha usada:** Achar que toda entidade pública é órgão sem personalidade.
- **Como pensar para acertar:** Relacione criação legal, personalidade própria e posição na Administração Indireta.

#### Comentário Extra Dia 2.6
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Ato administrativo, competência, anulação e revogação](semana_01_estudo.md#s1-d2-atos-controle)

- **Alternativa correta:** D.
- **A) está errada:** Forma e motivo não transferem competência a quem não recebeu atribuição legal.
- **B) está errada:** Competência responde quem pode agir; finalidade responde para qual interesse o ato se dirige.
- **C) está errada:** Discricionariedade permanece limitada pela competência e não sana ilegalidade por conveniência.
- **D) está correta:** A falta compromete competência, e o controle deve tratar a ilegalidade, não um juízo de mérito.
- **Conceito cobrado:** Elementos do ato administrativo.
- **Pegadinha usada:** Usar acertos em outros elementos para legitimar agente incompetente.
- **Como pensar para acertar:** Identifique quem praticou o ato, qual norma atribui poder e se a escolha era juridicamente possível.

#### Comentário Extra Dia 2.7
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Ato administrativo, competência, anulação e revogação](semana_01_estudo.md#s1-d2-atos-controle)

- **Alternativa correta:** A.
- **A) está correta:** O poder foi usado para fim pessoal diverso daquele definido pela norma.
- **B) está errada:** Finalidade não é escolha livre de mérito; interesse pessoal permanece controlável.
- **C) está errada:** Nova publicação não altera o propósito persecutório que viciou o ato.
- **D) está errada:** Eficiência não legitima perseguição nem substitui a finalidade pública.
- **Conceito cobrado:** Finalidade pública.
- **Pegadinha usada:** Considerar conveniência pessoal como finalidade administrativa legítima.
- **Como pensar para acertar:** Compare o fim previsto na norma com o resultado pessoal efetivamente buscado.

#### Comentário Extra Dia 2.8
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Ato administrativo, competência, anulação e revogação](semana_01_estudo.md#s1-d2-atos-controle)

- **Alternativa correta:** B.
- **A) está errada:** Inverte legalidade e mérito: ato ilegal é anulado, não revogado.
- **B) está correta:** X exige anulação; Y admite revogação por mérito, observados os limites aplicáveis.
- **C) está errada:** A Administração controla a legalidade dos próprios atos e pode anulá-los.
- **D) está errada:** Inconveniência de ato válido não o transforma automaticamente em ilegal.
- **Conceito cobrado:** Controle do ato administrativo.
- **Pegadinha usada:** Confundir anulação por ilegalidade com revogação por mérito.
- **Como pensar para acertar:** Aplique dois filtros em ordem: validade jurídica e, se válido, conveniência/oportunidade.

#### Comentário Extra Dia 2.9
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [LAI e LGPD](semana_01_estudo.md#s1-d2-lai-lgpd)

- **Alternativa correta:** D.
- **A) está errada:** A restrição deve alcançar o dado protegido, não necessariamente todo o documento.
- **B) está errada:** Publicidade não elimina sigilo legal nem proteção de dados pessoais.
- **C) está errada:** O órgão deve decidir e fundamentar; silêncio não é técnica regular de compatibilização.
- **D) está correta:** Acesso parcial e ocultação justificada conciliam transparência com proteção da parcela restrita.
- **Conceito cobrado:** LAI e publicidade.
- **Pegadinha usada:** Tratar publicidade como exposição irrestrita de todo dado.
- **Como pensar para acertar:** Separe conteúdo divulgável e protegido antes de decidir extensão e fundamento do acesso.

#### Comentário Extra Dia 2.10
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [LAI e LGPD](semana_01_estudo.md#s1-d2-lai-lgpd)

- **Alternativa correta:** A.
- **A) está correta:** A solução identifica finalidade, separa parcelas, aplica necessidade e escolhe restrição ou anonimização fundamentada.
- **B) está errada:** A presença de dado pessoal não torna automaticamente secreta a estatística pública separável.
- **C) está errada:** LAI e LGPD coexistem; transparência não suspende necessidade e segurança.
- **D) está errada:** Consentimento não é a única base jurídica e não impede produção legítima de estatística anônima.
- **Conceito cobrado:** Compatibilização entre LAI, LGPD, finalidade, necessidade e segurança.
- **Pegadinha usada:** Resolver o conflito aparente com negação total ou divulgação total, sem separar dados.
- **Como pensar para acertar:** Identifique informação, dado pessoal, finalidade, parcela necessária e fundamento da decisão.

#### Comentário Extra Dia 2.11
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Improbidade administrativa](semana_01_estudo.md#s1-d2-improbidade)

- **Alternativa correta:** B.
- **A) está errada:** Anulação demonstra ilegalidade, não prova automaticamente dolo ou tipificação.
- **B) está correta:** Improbidade exige conduta dolosa tipificada e os demais vínculos do caso; erro razoável isolado não basta.
- **C) está errada:** Vantagem deliberada é mais grave em tese; a alternativa inverte a análise e ignora o tipo legal.
- **D) está errada:** As esferas podem coexistir quando os requisitos próprios de cada uma estiverem presentes.
- **Conceito cobrado:** Improbidade administrativa.
- **Pegadinha usada:** Equiparar ilegalidade simples a improbidade.
- **Como pensar para acertar:** Teste conduta, dolo, tipo e nexo; não comece apenas pelo resultado ou pela anulação.

#### Comentário Extra Dia 2.12
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Improbidade administrativa](semana_01_estudo.md#s1-d2-improbidade)

- **Alternativa correta:** C.
- **A) está errada:** Vantagem incorporada dolosamente não é mera falha de forma.
- **B) está errada:** Tipificação e prova continuam necessárias; a vantagem não autoriza presunções irrestritas.
- **C) está correta:** Vantagem patrimonial indevida obtida pelo uso doloso do cargo remete, em tese, a enriquecimento ilícito.
- **D) está errada:** A Lei de Improbidade contempla hipóteses de vantagem patrimonial nos limites do tipo legal.
- **Conceito cobrado:** Atos de improbidade.
- **Pegadinha usada:** Confundir vantagem pessoal com mera falha formal.
- **Como pensar para acertar:** Identifique a natureza da vantagem, o vínculo com o cargo, o dolo e o enquadramento legal.

#### Comentário Extra Dia 2.13
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Licitações, pregão, dispensa e inexigibilidade](semana_01_estudo.md#s1-d2-licitacoes)

- **Alternativa correta:** D.
- **A) está errada:** Avaliação técnica deve respeitar critério válido e não dispensa motivação.
- **B) está errada:** Eficiência não autoriza critério criado depois da abertura das propostas.
- **C) está errada:** A vinculação alcança Administração e participantes.
- **D) está correta:** Critérios publicados orientam o julgamento; mudança legítima exige procedimento, publicidade e motivação.
- **Conceito cobrado:** Vinculação ao edital.
- **Pegadinha usada:** Achar que o edital é só orientação sem força vinculante.
- **Como pensar para acertar:** Compare o critério aplicado com o instrumento válido e verifique quando a mudança foi proposta.

#### Comentário Extra Dia 2.14
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Licitações, pregão, dispensa e inexigibilidade](semana_01_estudo.md#s1-d2-licitacoes)

- **Alternativa correta:** A.
- **A) está correta:** Objeto comum e competição viável apontam para pregão; exclusividade comprovada pode inviabilizar competição, sem eliminar instrução.
- **B) está errada:** Padrões objetivos favorecem comparação e não tornam ambos os objetos inexigíveis.
- **C) está errada:** Dispensa depende de hipótese legal, e exclusividade não afasta processo e motivação.
- **D) está errada:** Leilão não é solução para os dois objetos e ignora viabilidade de competição.
- **Conceito cobrado:** Objeto comum, inviabilidade de competição e formalização da contratação direta.
- **Pegadinha usada:** Escolher modalidade pelo nome do objeto sem examinar competição e dever processual.
- **Como pensar para acertar:** Aplique três filtros: natureza do objeto, viabilidade da disputa e instrução/motivação remanescente.

#### Comentário Extra Dia 2.15
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Licitações, pregão, dispensa e inexigibilidade](semana_01_estudo.md#s1-d2-licitacoes)

- **Alternativa correta:** B.
- **A) está errada:** Concurso seleciona trabalho técnico, científico ou artístico mediante prêmio, não serviço comum ordinário.
- **B) está correta:** Padrões objetivos e competição viável caracterizam o campo típico do pregão.
- **C) está errada:** Leilão se relaciona à alienação, não à contratação descrita.
- **D) está errada:** Inexigibilidade pressupõe competição inviável, afastada pelo próprio cenário.
- **Conceito cobrado:** Modalidades de licitação.
- **Pegadinha usada:** Trocar pregão por leilão ou concurso.
- **Como pensar para acertar:** Classifique o objeto e verifique se a competição é viável antes de escolher modalidade ou contratação direta.

#### Comentário Extra Dia 2.16
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Concordância e verbo haver impessoal](semana_01_estudo.md#s1-d2-portugues-concordancia)

- **Alternativa correta:** A.
- **A) está correta:** Com sentido de existir, 'haver' é impessoal e fica no singular.
- **B) está errada:** Com 'existir', o verbo concorda: existiam muitos processos.
- **C) está errada:** Com sentido de existir, o verbo `haver` não deve ser flexionado no plural.
- **D) está errada:** O particípio deve concordar: foram analisadas as planilhas.
- **Conceito cobrado:** Concordância verbal.
- **Pegadinha usada:** Flexionar indevidamente verbo impessoal.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.17
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Referência pronominal e uso de onde](semana_01_estudo.md#s1-d2-portugues-ambiguidade-onde)

- **Alternativa correta:** B.
- **A) está errada:** O verbo possui complemento indireto e oração completiva.
- **B) está correta:** Pronome possessivo pode gerar ambiguidade referencial.
- **C) está errada:** Fora é mais-que-perfeito, não futuro.
- **D) está errada:** A ambiguidade permanece no pronome possessivo.
- **Conceito cobrado:** Ambiguidade.
- **Pegadinha usada:** Ignorar dupla referência possível.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.18
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Referência pronominal e uso de onde](semana_01_estudo.md#s1-d2-portugues-ambiguidade-onde)

- **Alternativa correta:** A.
- **A) está correta:** 'Onde' retoma lugar físico.
- **B) está errada:** 'Onde' deve indicar lugar físico; 'situação em que' seria melhor.
- **C) está errada:** Para norma, use 'em que' ou 'na qual'.
- **D) está errada:** Não se trata propriamente de lugar físico.
- **Conceito cobrado:** Emprego de onde.
- **Pegadinha usada:** Usar 'onde' para qualquer referência abstrata.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.19
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Pontuação e restrição de sentido](semana_01_estudo.md#s1-d2-portugues-pontuacao)

- **Alternativa correta:** D.
- **A) está errada:** A vírgula separa indevidamente sujeito e verbo.
- **B) está errada:** A vírgula fragmenta a locução introdutória.
- **C) está errada:** As vírgulas quebram relações sintáticas essenciais.
- **D) está correta:** Adjunto adverbial antecipado pode ser separado por vírgula.
- **Conceito cobrado:** Pontuação.
- **Pegadinha usada:** Separar sujeito e verbo por vírgula.
- **Como pensar para acertar:** Volte ao texto ou à regra gramatical aplicada; não escolha a alternativa apenas por soar mais formal.

#### Comentário Extra Dia 2.20
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Comando negativo e inferência literal](semana_01_estudo.md#s1-d2-portugues-comando)

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
**Uso:** Essenciais
**Referência:** [Consultas, ordem lógica, ordenação e limitação](semana_01_estudo.md#s1-d3-sql-consultas)

Em um sistema do CRA, a tabela `profissional(id_profissional, nome, uf, situacao)` deve retornar apenas profissionais ativos do Paraná. A consulta correta é:

A) SELECT nome FROM profissional WHERE uf = 'PR' ORDER BY (situacao = 'ATIVO') DESC;
B) SELECT nome FROM profissional WHERE uf = 'PR' OR situacao = 'ATIVO';
C) SELECT nome FROM profissional WHERE uf = 'PR' AND situacao = 'ATIVO';
D) SELECT nome FROM profissional WHERE uf <> 'PR' AND situacao = 'ATIVO';

### Questão 2
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes)

A tabela `anuidade(id_anuidade, id_profissional, ano, valor)` deve retornar a **quantidade de lançamentos de anuidade por ano**. Assinale a consulta adequada.

A) SELECT ano, COUNT(*) AS total FROM anuidade GROUP BY ano;
B) SELECT ano, COUNT(*) AS total FROM anuidade GROUP BY id_profissional;
C) SELECT ano, SUM(valor) AS total FROM anuidade GROUP BY ano;
D) SELECT COUNT(*) AS total FROM anuidade;

### Questão 3
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes)

Para listar apenas setores com mais de 20 profissionais cadastrados, considerando `profissional(id, setor)`, a consulta correta é:

A) SELECT setor, COUNT(*) FROM profissional WHERE setor IS NOT NULL GROUP BY setor;
B) SELECT setor, COUNT(*) FROM profissional GROUP BY setor ORDER BY COUNT(*) DESC FETCH FIRST 20 ROWS ONLY;
C) SELECT setor, COUNT(*) FROM profissional GROUP BY setor HAVING COUNT(*) >= 20;
D) SELECT setor, COUNT(*) FROM profissional GROUP BY setor HAVING COUNT(*) > 20;

### Questão 4
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade)

No modelo relacional, `id_profissional` em `anuidade` referenciando `profissional(id_profissional)` é exemplo de:

A) chave estrangeira.
B) chave primária de `anuidade`, porque identifica o profissional associado.
C) chave candidata que deve ser única em `anuidade`.
D) índice de pesquisa sem função de integridade referencial.

### Questão 5
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade)

Assinale a alternativa correta sobre chave primária.

A) Identifica unicamente cada linha e não aceita valor nulo.
B) Impede repetição, mas pode aceitar NULL porque equivale a uma restrição UNIQUE comum.
C) Deve ser simples; chaves compostas não podem exercer o papel de chave primária.
D) É escolhida entre as chaves candidatas, mas só passa a exigir unicidade quando referenciada por uma FK.

### Questão 6
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Modelo Entidade-Relacionamento e mapeamento](semana_01_estudo.md#s1-d3-mer-mapeamento)

Um relacionamento N:N entre `usuario` e `perfil` deve ser implementado, no modelo relacional, por:

A) uma coluna `perfis` em `usuario`, contendo os identificadores em uma lista delimitada.
B) uma FK `id_usuario` em `perfil`, permitindo que cada perfil aponte para apenas um usuário.
C) uma tabela associativa, como `usuario_perfil(id_usuario, id_perfil)`.
D) uma FK `id_perfil` em `usuario`, limitando cada usuário a um único perfil.

### Questão 7
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Normalização básica](semana_01_estudo.md#s1-d3-normalizacao-base)

Uma tabela `matricula(id_aluno, id_disciplina, nome_aluno, nome_disciplina)` tem chave composta `(id_aluno, id_disciplina)`. O problema de normalização mais evidente é:

A) violação de 1FN, porque uma chave composta impede que os atributos sejam atômicos.
B) violação de 2FN, pois cada nome depende de apenas uma parte da chave composta.
C) violação de 3FN exclusivamente, porque os nomes dependem transitivamente um do outro.
D) nenhuma violação, pois a combinação `(id_aluno, id_disciplina)` é única.

### Questão 8
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Normalização básica](semana_01_estudo.md#s1-d3-normalizacao-base)

A tabela `servidor(id_servidor, id_departamento, nome_departamento)` pode violar a 3FN porque:

A) há dependência parcial de `nome_departamento` em uma parte da chave composta de `servidor`.
B) o nome do departamento se repete em várias linhas, o que por si só viola a 1FN.
C) `id_servidor` determina `id_departamento`, que por sua vez determina `nome_departamento`.
D) qualquer FK para `departamento` é incompatível com a 3FN.

### Questão 9
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao)

Assinale a alternativa que diferencia corretamente `DELETE` e `DROP`.

A) `DELETE` remove linhas; `DROP` remove um objeto do banco, como a tabela.
B) `DELETE` sem WHERE remove linhas e a definição da tabela; `DROP` preserva a definição.
C) `DELETE` e `DROP` removem somente dados, diferenciando-se apenas pela possibilidade de ROLLBACK.
D) `DROP` esvazia a tabela e preserva sua estrutura para reutilização, enquanto `DELETE` exige filtro.

### Questão 10
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao)

Em `UPDATE profissional SET situacao = 'INATIVO';`, sem cláusula WHERE, o efeito provável é:

A) alterar a situação de todas as linhas da tabela.
B) alterar apenas a linha de menor chave primária, por ser a primeira do plano de execução.
C) ser rejeitado pelo SQL padrão, pois todo UPDATE exige predicado de seleção.
D) alterar somente as linhas que já estavam ativas, por inferência do valor atribuído.

### Questão 11
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [NULL, lógica de três valores e DISTINCT](semana_01_estudo.md#s1-d3-null-distinct)

Para localizar exclusivamente os registros em que `profissional.email` contém o valor SQL `NULL`, usa-se:

A) WHERE email = ''
B) WHERE email <> NULL
C) WHERE COALESCE(email, '') = ''
D) WHERE email IS NULL

### Questão 12
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins)

Considere `profissional(id, nome)` e `anuidade(id, id_profissional, ano)`. Para listar somente pares profissional–anuidade com correspondência pela chave, a consulta correta é:

A) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id = p.id;
B) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id_profissional = p.id;
C) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id_profissional = a.id;
D) SELECT p.nome, a.ano FROM profissional p CROSS JOIN anuidade a;

### Questão 13
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins)

Um relatório deve mostrar todos os profissionais, mesmo os que ainda não possuem anuidade lançada. A junção mais adequada, partindo de `profissional`, é:

A) CROSS JOIN anuidade, combinando cada profissional com todas as anuidades.
B) INNER JOIN anuidade ON anuidade.id_profissional = profissional.id.
C) RIGHT JOIN anuidade ON anuidade.id_profissional = profissional.id, preservando o lado de `anuidade`.
D) LEFT JOIN anuidade ON anuidade.id_profissional = profissional.id.

### Questão 14
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes)

Em SQL, `COUNT(*)` e `COUNT(email)` podem produzir resultados diferentes porque:

A) `COUNT(*)` ignora linhas nas quais qualquer coluna contenha NULL.
B) `COUNT(email)` ignora NULL nessa coluna, enquanto `COUNT(*)` conta as linhas.
C) as duas expressões sempre devolvem o mesmo total, independentemente dos dados.
D) `COUNT(email)` conta os NULLs, atribuindo zero a cada valor ausente.

### Questão 15
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade)

Assinale a alternativa correta sobre `PRIMARY KEY`, `UNIQUE` e `NOT NULL`.

A) `UNIQUE` e `NOT NULL` formam uma chave candidata e substituem automaticamente qualquer `PRIMARY KEY` já declarada.
B) `PRIMARY KEY` garante unicidade, mas permite NULL quando não existe uma restrição `NOT NULL` separada.
C) `PRIMARY KEY` impõe unicidade e não nulidade; `UNIQUE` veda duplicatas não nulas; `NOT NULL` veda nulos.
D) `NOT NULL` impede valores repetidos, enquanto `UNIQUE` exige preenchimento e define a chave primária da tabela.

### Questão 16
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade)

Um analista deseja impedir que `valor_anuidade` seja negativo. A restrição mais adequada é:

A) NOT NULL em `valor_anuidade`.
B) CHECK (valor_anuidade >= 0).
C) UNIQUE em `valor_anuidade`.
D) DEFAULT 0 para `valor_anuidade`.

### Questão 17
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [SQL ANSI básico](semana_01_estudo.md#s1-d3-sql-base)

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
**Uso:** Aprofundamento
**Referência:** [Transações e ACID](semana_01_estudo.md#s1-d3-transacoes-acid)

Em uma transação de pagamento, o sistema deve registrar pagamento e baixar débito. Se a baixa falhar, o registro do pagamento também deve ser desfeito. Essa exigência representa:

A) consistência, porque toda regra válida implica desfazer todas as etapas.
B) isolamento, porque as duas operações não podem coexistir na mesma transação.
C) durabilidade, porque a falha ocorre antes de qualquer confirmação.
D) atomicidade, porque as etapas devem produzir um único resultado de tudo ou nada.

### Questão 19
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Índices e custo de manutenção](semana_01_estudo.md#s1-d3-indices)

Um índice criado sobre `numero_processo` tende a:

A) garantir unicidade de `numero_processo`, mesmo que o índice não tenha sido declarado UNIQUE.
B) acelerar qualquer consulta da tabela, sem custo mensurável para operações de escrita.
C) melhorar consultas compatíveis com a chave do índice, ao custo de espaço e manutenção nas escritas.
D) eliminar toda varredura da tabela, inclusive em filtros que não utilizem a coluna indexada.

### Questão 20
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Views, procedures e triggers](semana_01_estudo.md#s1-d3-objetos-programaveis)

Uma view `vw_profissionais_ativos` pode ser usada para:

A) armazenar obrigatoriamente uma cópia física autônoma dos dados retornados.
B) conceder acesso aos dados subjacentes independentemente das permissões configuradas.
C) aceitar INSERT, UPDATE e DELETE em qualquer definição, sem restrições do SGBD.
D) oferecer uma visão lógica baseada em consulta, que pode filtrar e projetar dados.

### Questão 21
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Trigger, transação, rollback e auditoria](semana_01_estudo.md#s1-d3-trigger-transacional)

Uma trigger `AFTER INSERT` em `anuidade` registra auditoria na mesma transação do comando que a disparou. Não há transação autônoma específica. Se a transação principal sofrer `ROLLBACK`, é correto afirmar que:

A) a trigger somente será executada depois do COMMIT, razão pela qual sua auditoria sempre persistirá.
B) a trigger é executada pelo evento e seu registro de auditoria normalmente também será desfeito pelo ROLLBACK.
C) a aplicação precisa executar `CALL trigger_auditoria` antes do ROLLBACK.
D) o registro produzido pela trigger não participa das propriedades ACID da transação principal.

### Questão 22
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Views, procedures e triggers](semana_01_estudo.md#s1-d3-objetos-programaveis)

Uma rotina `registrar_pagamento` deve receber parâmetros, validar dados, inserir o pagamento e atualizar o débito quando chamada pela aplicação. A solução mais compatível é:

A) uma stored procedure, que encapsula comandos e lógica sob chamada explícita.
B) uma trigger, pois triggers são chamadas explicitamente pela aplicação.
C) uma restrição CHECK, capaz de executar vários comandos DML.
D) uma view, pois toda view aceita parâmetros e executa alterações encadeadas.

### Questão 23
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Álgebra relacional](semana_01_estudo.md#s1-d3-algebra-relacional)

Considere `π_nome(σ_uf = 'PR' ∧ situacao = 'ATIVO'(Profissional))`. Essa expressão de álgebra relacional representa:

A) todas as colunas dos profissionais, agrupadas por UF e situação.
B) apenas os nomes de todos os profissionais, ordenados por UF.
C) a quantidade de profissionais ativos em cada UF.
D) os nomes dos profissionais cujas tuplas satisfazem simultaneamente UF e situação.

### Questão 24
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Modelo Entidade-Relacionamento e mapeamento](semana_01_estudo.md#s1-d3-mer-mapeamento)

Um processo pode possuir nenhuma ou várias fiscalizações. Cada fiscalização tem número próprio, data, resultado e responsável. No MER, a representação mais adequada é:

A) guardar todas as fiscalizações em um único atributo multivalorado de `Processo`.
B) transformar `Fiscalizacao` em domínio do atributo `resultado`.
C) modelar `Fiscalizacao` como entidade relacionada a `Processo` em 1:N.
D) representar cada fiscalização como atributo derivado, sem identidade nem dados próprios.

### Questão 25
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Modelo Entidade-Relacionamento e mapeamento](semana_01_estudo.md#s1-d3-mer-mapeamento)

Uma pessoa pode ter vários telefones, e cada telefone possui tipo e indicação de principal. O mapeamento relacional que melhor preserva a 1FN é:

A) repetir todos os dados de `Pessoa` em uma nova linha para cada telefone.
B) adicionar `telefone1`, `telefone2` e `telefone3` à tabela `Pessoa`.
C) armazenar telefone, tipo e indicador em uma string delimitada.
D) criar uma tabela `PessoaTelefone`, com FK para `Pessoa` e uma chave adequada.

### Questão 26
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Conceitos e arquitetura de SGBD](semana_01_estudo.md#s1-d3-conceitos-sgbd)

O DBA altera organização em disco, particionamento e índices, mas mantém tabelas, colunas e consultas usadas pela aplicação. Isso exemplifica:

A) independência lógica, porque o modelo conceitual foi substituído.
B) integridade referencial, porque as FKs permaneceram válidas.
C) independência física, pois a implementação mudou sem alterar o esquema lógico.
D) durabilidade, porque toda mudança física exige COMMIT.

### Questão 27
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Metadados, catálogo e independência física](semana_01_estudo.md#s1-d3-metadados-catalogo)

Antes de executar um `ALTER TABLE`, o analista consulta o catálogo do SGBD para descobrir tipos, valores padrão, restrições e índices existentes. Ele está consultando:

A) metadados mantidos no dicionário de dados.
B) exclusivamente o log de transações.
C) dados operacionais produzidos pelos usuários.
D) uma cópia física obrigatória das tabelas de negócio.

### Questão 28
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes)

Considere `lancamento(id_lancamento PK, setor, valor)`, com vários lançamentos por setor: `SELECT setor, id_lancamento, SUM(valor) FROM lancamento GROUP BY setor;`. Em regras SQL usuais, o problema é que:

A) a presença da PK no SELECT dispensa sua agregação ou inclusão no GROUP BY.
B) `id_lancamento` não está agregado, não integra o GROUP BY e não é determinado por `setor`.
C) SUM só pode ser usada quando também existe uma cláusula HAVING.
D) a função agregada deveria aparecer antes das demais expressões no SELECT.

### Questão 29
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao)

Dentro de uma transação ainda não confirmada, executa-se `DELETE FROM profissional WHERE situacao = 'INATIVO';`. É correto afirmar que:

A) o comando exclui o objeto `profissional` e suas restrições, mas preserva os dados para eventual `ROLLBACK`.
B) a remoção das linhas-pai sempre exclui as linhas filhas, ainda que a FK esteja configurada com `RESTRICT`.
C) o DELETE remove as linhas permitidas e pode ser desfeito por ROLLBACK antes do COMMIT.
D) por ser uma operação DML, a exclusão torna-se irreversível ao fim do comando, mesmo sem `COMMIT` explícito.

### Questão 30
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao)

Considere `profissional(id INTEGER GENERATED ALWAYS AS IDENTITY, nome VARCHAR(100) NOT NULL, uf CHAR(2) NOT NULL DEFAULT 'PR')`. Para inserir Ana e Bruno usando o valor padrão de `uf`, emprega-se:

A) `INSERT INTO profissional (nome, uf) VALUES ('Ana', NULL), ('Bruno', NULL);`
B) `INSERT INTO profissional VALUES ('Ana'), ('Bruno');`
C) `UPDATE profissional SET nome IN ('Ana', 'Bruno');`
D) `INSERT INTO profissional (nome) VALUES ('Ana'), ('Bruno');`

### Questão 31
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Isolamento e anomalias](semana_01_estudo.md#s1-d3-isolamento)

Sobre níveis de isolamento, considerada a classificação ANSI clássica e ressalvadas implementações mais fortes dos SGBDs, assinale a correta.

A) REPEATABLE READ impede leituras sujas e não repetíveis; na matriz ANSI clássica, fantasmas ainda podem ocorrer, embora alguns SGBDs ofereçam garantia mais forte.
B) READ COMMITTED garante que duas leituras da mesma linha, na mesma transação, sempre retornem o mesmo valor.
C) READ UNCOMMITTED impede leitura de valores ainda não confirmados.
D) SERIALIZABLE elimina a necessidade de COMMIT e de mecanismos de controle de concorrência.

### Questão 32
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade)

Uma tabela possui `id_pessoa` como PK e `cpf` com restrição UNIQUE, mas sem NOT NULL. A interpretação mais precisa é:

A) a restrição `UNIQUE` transforma `cpf` em nova chave primária e substitui automaticamente `id_pessoa`.
B) `id_pessoa` segue como PK; CPF não nulo duplicado é rejeitado, e NULL varia conforme o SGBD.
C) `UNIQUE` também impõe `NOT NULL` em todos os SGBDs, tornando obrigatório o preenchimento de `cpf`.
D) a unicidade de `cpf` permite repetir `id_pessoa` quando cada ocorrência estiver associada a um CPF distinto.

### Questão 33
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins)

Para listar todos os profissionais e, quando existente, o nome de sua cidade, considerando `profissional(id, nome, id_cidade)` e `cidade(id, nome)`, usa-se:

A) `SELECT p.nome, c.nome FROM profissional p LEFT JOIN cidade c ON c.id = p.id_cidade WHERE c.id IS NOT NULL;`
B) `SELECT p.nome, c.nome FROM profissional p INNER JOIN cidade c ON c.id = p.id_cidade;`
C) `SELECT p.nome, c.nome FROM profissional p LEFT JOIN cidade c ON c.id = p.id;`
D) `SELECT p.nome, c.nome FROM profissional p LEFT JOIN cidade c ON c.id = p.id_cidade;`

### Questão 34
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Dependências e decomposição](semana_01_estudo.md#s1-d3-normalizacao-decomposicao)

Assinale a afirmativa incorreta sobre normalização e decomposição.

A) Com chave candidata simples, não existe dependência parcial dessa chave a ser removida pela 2FN.
B) Uma cadeia chave → atributo não chave → outro atributo não chave pode indicar violação de 3FN.
C) Qualquer decomposição que distribua colunas em duas tabelas preserva dados e dependências automaticamente.
D) Normalização reduz redundâncias e anomalias, mas pode aumentar a necessidade de junções.

### Questão 35
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Consultas, ordem lógica, ordenação e limitação](semana_01_estudo.md#s1-d3-sql-consultas)

Usando sintaxe SQL com FETCH, deseja-se retornar no máximo três linhas de anuidade com maior `valor`, usando o menor `id_anuidade` como desempate. A consulta correta é:

A) `SELECT * FROM anuidade ORDER BY valor DESC, id_anuidade ASC FETCH FIRST 3 ROWS ONLY;`
B) `SELECT * FROM anuidade ORDER BY valor ASC, id_anuidade ASC FETCH FIRST 3 ROWS ONLY;`
C) `SELECT * FROM anuidade ORDER BY valor DESC, id_anuidade ASC OFFSET 3 ROWS;`
D) `SELECT * FROM anuidade FETCH FIRST 3 ROWS ONLY;`

### Questão 36
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao)

Sobre DELETE, TRUNCATE e DROP, assinale a alternativa correta.

A) DELETE sem WHERE e TRUNCATE têm comportamento transacional, de log e identidade idêntico em qualquer SGBD.
B) TRUNCATE esvazia a tabela sem predicado e preserva o objeto; transação, FKs e identidade variam por SGBD.
C) TRUNCATE aceita WHERE para selecionar individualmente as linhas removidas.
D) DROP TABLE esvazia a tabela, mas preserva estrutura e restrições.

### Questão 37
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins)

Deseja-se listar todos os setores, inclusive os que não possuem profissional ativo, com a respectiva contagem. A consulta correta é:

A) `SELECT s.id, COUNT(p.id) FROM setor s LEFT JOIN profissional p ON p.id_setor = s.id WHERE p.ativo = 1 GROUP BY s.id;`
B) `SELECT s.id, COUNT(p.id) FROM setor s LEFT JOIN profissional p ON p.id_setor = s.id AND p.ativo = 1 GROUP BY s.id;`
C) `SELECT s.id, COUNT(*) FROM setor s LEFT JOIN profissional p ON p.id_setor = s.id AND p.ativo = 1 GROUP BY s.id;`
D) `SELECT s.id, COUNT(p.id) FROM setor s INNER JOIN profissional p ON p.id_setor = s.id AND p.ativo = 1 GROUP BY s.id;`

### Questão 38
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Participação, cardinalidade e vínculos temporais](semana_01_estudo.md#s1-d3-participacao-temporalidade)

Um profissional pode responder por várias pessoas jurídicas, e cada pessoa jurídica pode possuir vários responsáveis ao longo do tempo. O vínculo guarda início, fim e situação. A melhor solução é:

A) colocar uma única FK `id_pessoa_juridica` em `Profissional`.
B) colocar uma única FK `id_responsavel_atual` em `PessoaJuridica`.
C) criar tabela associativa com FKs, período, situação e restrições de integridade.
D) guardar nomes e períodos em uma coluna textual de histórico.

### Questão 39
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Backup lógico consistente e restauração](semana_01_estudo.md#s1-d3-backup-consistente)

É necessário produzir backup lógico consistente enquanto o banco permanece disponível para escritas concorrentes. A conduta mais segura é:

A) usar ferramenta do SGBD com snapshot ou exportação consistente e validar o resultado mediante teste de restauração.
B) exportar cada tabela por consultas independentes, sem snapshot ou coordenação transacional.
C) copiar diretamente os arquivos físicos abertos pelo SGBD.
D) criar índices adicionais, pois eles substituem mecanismos de backup e recuperação.

### Questão 40
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Normalização básica](semana_01_estudo.md#s1-d3-normalizacao-base)

A coluna `documento.tags` contém valores como `fiscalização;anuidade;recurso`. Para consultar e restringir cada tag com integridade relacional, a melhor remodelagem é:

A) conservar a string e validar cada tag apenas com LIKE.
B) duplicar toda a linha de `Documento` para cada tag.
C) criar colunas fixas `tag1`, `tag2`, `tag3` e `tag4`.
D) criar `DocumentoTag`, com uma tag por linha e FK para `Documento`.

### Questão 41
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade)

A tabela já possui `id` como PK. `numero_registro` deve ser obrigatório e único, enquanto `situacao` só pode assumir `A` ou `I`. A definição mais adequada é:

A) `numero_registro VARCHAR(20) REFERENCES profissional(numero_registro), situacao CHAR(1)`
B) `numero_registro VARCHAR(20) PRIMARY KEY, situacao CHAR(1)`
C) `numero_registro VARCHAR(20) CHECK (numero_registro IS NOT NULL), situacao CHAR(1)`
D) `numero_registro VARCHAR(20) NOT NULL UNIQUE, situacao CHAR(1) NOT NULL CHECK (situacao IN ('A','I'))`

### Questão 42
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Conceitos de SGBD e independência física](semana_01_estudo.md#s1-d3-conceitos-sgbd), [isolamento e anomalias](semana_01_estudo.md#s1-d3-isolamento) e [log, redo, undo e recuperação](semana_01_estudo.md#s1-d3-log-recuperacao)

Uma plataforma mantém visões externas sobre um esquema lógico comum. O DBA reorganiza índices e partições sem alterar essas visões; em paralelo, o sistema precisa isolar transações concorrentes e recuperar commits após falha. A conclusão tecnicamente correta é:

A) toda reorganização física exige reescrever as visões externas, enquanto o rollback, sozinho, assegura a persistência dos commits.
B) o SGBD fornece independência física por meio dos mapeamentos entre níveis e coordena concorrência, log e recuperação para preservar as transações.
C) cada visão externa deve possuir esquema lógico próprio, e cópias periódicas do banco substituem o controle de isolamento entre transações.
D) a linguagem SQL, independentemente do SGBD, implementa os mapeamentos entre níveis e restaura automaticamente os commits após falha.

### Questão 43
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Segurança e menor privilégio com views](semana_01_estudo.md#s1-d3-menor-privilegio)

O usuário `relatorio` deve consultar apenas `id` e `nome` dos profissionais ativos, sem acessar CPF, linhas inativas ou operações de escrita. Considerando o menor privilégio e uma solução independente do filtro da aplicação, a configuração mais adequada é:

A) criar uma view que projete `id` e `nome` e filtre `situacao = 'A'`, concedendo `SELECT` apenas sobre essa view e nenhum privilégio sobre a tabela-base.
B) conceder `SELECT` sobre a tabela-base e exigir que cada relatório aplique corretamente o filtro de situação e omita o CPF.
C) conceder `SELECT (id, nome)` sobre a tabela-base, pois a restrição de colunas também impede, por si só, a leitura de linhas inativas.
D) criar a view filtrada, mas manter também `SELECT` sobre a tabela-base para que o usuário possa validar os dados exibidos.

### Questão 44
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Trigger, transação, rollback e auditoria](semana_01_estudo.md#s1-d3-trigger-transacional)

Várias aplicações atualizam `profissional`, e toda alteração deve gerar auditoria centralizada com valores anteriores e novos. A alternativa mais adequada é:

A) associar uma trigger ao UPDATE, registrando valores anteriores e novos e observando transação, recursão e volume.
B) depender de cada aplicação para inserir voluntariamente a auditoria após atualizar a linha.
C) criar uma view simples, pois toda view intercepta automaticamente alterações nas tabelas-base.
D) criar um índice, pois índices mantêm histórico completo das versões anteriores de cada linha.

### Questão 45
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Participação, cardinalidade e vínculos temporais](semana_01_estudo.md#s1-d3-participacao-temporalidade)

Um profissional pode não possuir anuidade ou possuir várias, cada anuidade pertence exatamente a um profissional e não pode existir mais de uma anuidade do mesmo profissional no mesmo exercício. Qual implementação traduz simultaneamente cardinalidade, participação e unicidade temporal?

A) manter `profissional_id` anulável em `Anuidade` e criar índice simples por `exercicio`, permitindo anuidades sem profissional.
B) armazenar em `Profissional` uma FK obrigatória para uma única anuidade, repetindo a linha do profissional a cada novo exercício.
C) usar `Anuidade.profissional_id` como FK `NOT NULL` e impor `UNIQUE (profissional_id, exercicio)`, sem exigir que todo profissional possua linha em `Anuidade`.
D) criar uma tabela associativa entre `Profissional` e `Anuidade`, com FKs anuláveis, para representar um relacionamento muitos-para-muitos.

### Questão 46
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Dependências e decomposição](semana_01_estudo.md#s1-d3-normalizacao-decomposicao)

Considere `Servidor(id_servidor, nome, id_departamento, nome_departamento)`, com `id_servidor → id_departamento` e `id_departamento → nome_departamento`. A decomposição adequada para eliminar a dependência transitiva é:

A) manter `Servidor(id_servidor, nome)` e descartar os atributos de departamento, pois dependências transitivas devem ser eliminadas com perda de informação.
B) conservar a tabela original e declarar `nome_departamento` como `UNIQUE`, impedindo que dois servidores pertençam ao mesmo departamento.
C) separar `Servidor` e `Departamento`, ligados por `id_departamento` como FK.
D) criar `Departamento(id_servidor, nome_departamento)` e retirar `id_departamento`, usando o servidor como identificador da unidade administrativa.

### Questão 47
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [NULL, lógica de três valores e DISTINCT](semana_01_estudo.md#s1-d3-null-distinct)

A tabela contém `(uf, situacao)` = `(PR,A)`, `(PR,A)`, `(PR,I)`, `(NULL,A)` e `(NULL,A)`. O resultado de `SELECT DISTINCT uf, situacao FROM profissional` possui:

A) duas linhas, porque DISTINCT considera apenas `uf` e ignora `situacao`.
B) cinco linhas, porque DISTINCT não atua quando a projeção possui mais de uma coluna.
C) quatro combinações, pois cada NULL é sempre distinto de outro NULL na eliminação de duplicatas.
D) três combinações: `(PR,A)`, `(PR,I)` e uma ocorrência de `(NULL,A)`.

### Questão 48
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Log, redo, undo e recuperação](semana_01_estudo.md#s1-d3-log-recuperacao)

A transação T1 atualiza um cadastro e recebe confirmação de `COMMIT`. Em seguida, T2 altera o mesmo cadastro, mas o servidor falha antes do commit de T2. Após a recuperação, qual estado respeita ACID e o papel do log de recuperação?

A) reaplicar T1 e T2, pois toda alteração registrada em memória antes da falha deve tornar-se durável.
B) preservar os efeitos confirmados de T1 e desfazer os efeitos incompletos de T2, combinando durabilidade e atomicidade.
C) desfazer T1 e preservar T2, pois a transação mais recente substitui a anterior mesmo sem confirmação.
D) desfazer ambas, pois o isolamento impede que qualquer transação sobreviva a uma falha do servidor.

### Questão 49
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins)

Assinale a afirmativa incorreta sobre junções externas.

A) Um predicado no WHERE que rejeite NULL da tabela direita pode eliminar linhas preservadas por LEFT JOIN.
B) Mover qualquer predicado entre ON e WHERE nunca altera o resultado de uma junção externa.
C) Após LEFT JOIN, COUNT(chave_da_direita) conta correspondências, enquanto COUNT(*) também conta a linha estendida por NULL.
D) Um filtro da tabela direita colocado no ON pode restringir correspondências sem eliminar a linha da esquerda.

### Questão 50
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes)

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
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Simulado
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
**Uso:** Simulado
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
**Uso:** Simulado
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
**Uso:** Simulado
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
**Uso:** Simulado
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
- **Uso:** Essenciais
- **A) está errada:** A consulta filtra a UF, mas apenas ordena pela expressão de situação; ela não exclui os inativos.
- **B) está errada:** O OR inclui também profissionais ativos de outros estados e profissionais inativos do Paraná.
- **C) está correta:** Os dois predicados ligados por AND mantêm somente profissionais que satisfazem simultaneamente UF e situação.
- **D) está errada:** O operador de diferença seleciona ativos que não pertencem ao Paraná.
- **Conceito cobrado:** SELECT com WHERE.
- **Pegadinha usada:** Trocar a conjunção lógica ou confundir ordenação com filtragem.
- **Como pensar para acertar:** Traduza “ativos do Paraná” em duas condições simultâneas unidas por AND.
- **Referência à apostila de estudo:** [Consultas, ordem lógica, ordenação e limitação](semana_01_estudo.md#s1-d3-sql-consultas).

### Comentário da Questão 2

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está correta:** GROUP BY forma um grupo por ano e COUNT conta as linhas de cada grupo.
- **B) está errada:** O agrupamento está no profissional, não no ano solicitado, e a projeção de ano não acompanha esse agrupamento.
- **C) está errada:** `SUM(valor)` calcula o valor monetário acumulado por ano, e não a quantidade de lançamentos solicitada.
- **D) está errada:** A agregação produz apenas o total geral, sem separar os registros por ano.
- **Conceito cobrado:** GROUP BY e COUNT.
- **Pegadinha usada:** Confundir contagem, soma e total geral.
- **Como pensar para acertar:** Identifique primeiro a medida pedida — quantidade — e depois a dimensão — ano.
- **Referência à apostila de estudo:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes).

### Comentário da Questão 3

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** A consulta elimina setores nulos, mas não restringe os grupos pela quantidade de profissionais.
- **B) está errada:** Ela retorna os vinte maiores grupos, que não são necessariamente os grupos com mais de vinte integrantes.
- **C) está errada:** O operador >= inclui setores com exatamente vinte profissionais, contrariando “mais de 20”.
- **D) está correta:** HAVING aplica a condição estrita depois da contagem de cada setor.
- **Conceito cobrado:** GROUP BY e HAVING.
- **Pegadinha usada:** Confundir limite de linhas, ordenação e o operador estrito da condição agregada.
- **Como pensar para acertar:** Agrupe por setor e aplique no HAVING exatamente COUNT(*) > 20.
- **Referência à apostila de estudo:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes).

### Comentário da Questão 4

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está correta:** A coluna na tabela filha referencia a chave da tabela `profissional`.
- **B) está errada:** A PK identifica cada anuidade; a coluna descrita identifica o profissional referenciado.
- **C) está errada:** Em 1:N, várias anuidades podem apontar para o mesmo profissional, portanto a coluna não precisa ser única.
- **D) está errada:** Embora possa existir índice de apoio, o papel informado pelo enunciado é o de restrição referencial.
- **Conceito cobrado:** Chave estrangeira.
- **Pegadinha usada:** Confundir a identificação da linha filha com a referência à linha pai.
- **Como pensar para acertar:** Quando uma coluna aponta para chave de outra tabela, classifique-a como FK.
- **Referência à apostila de estudo:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade).

### Comentário da Questão 5

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está correta:** A PK materializa a integridade de entidade: identificação única e não nula.
- **B) está errada:** PRIMARY KEY não é apenas UNIQUE; ela também impede NULL.
- **C) está errada:** Uma PK pode conter mais de uma coluna quando a identificação do domínio é composta.
- **D) está errada:** A unicidade decorre da própria restrição de PK, independentemente de existir uma FK apontando para ela.
- **Conceito cobrado:** Chave primária.
- **Pegadinha usada:** Tratar PRIMARY KEY como simples UNIQUE ou proibir chave composta.
- **Como pensar para acertar:** Separe quatro ideias: candidata, escolhida como PK, única e não nula.
- **Referência à apostila de estudo:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade).

### Comentário da Questão 6

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** A lista reúne valores não atômicos e não oferece integridade referencial individual para cada perfil.
- **B) está errada:** Uma única FK em `perfil` modelaria outro vínculo e impediria o compartilhamento N:N pretendido.
- **C) está correta:** A associativa representa cada par usuário–perfil e pode impor FKs e unicidade sobre o par.
- **D) está errada:** Uma única FK em `usuario` permitiria no máximo um perfil por usuário.
- **Conceito cobrado:** Mapeamento N:N.
- **Pegadinha usada:** Reduzir N:N a uma FK simples ou a uma lista em coluna.
- **Como pensar para acertar:** Se ambos os lados admitem muitos, transforme cada vínculo em uma linha associativa.
- **Referência à apostila de estudo:** [Modelo Entidade-Relacionamento e mapeamento](semana_01_estudo.md#s1-d3-mer-mapeamento).

### Comentário da Questão 7

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** Chave composta é compatível com 1FN; atomicidade diz respeito aos valores dos atributos.
- **B) está correta:** `nome_aluno` depende só de `id_aluno` e `nome_disciplina` só de `id_disciplina`.
- **C) está errada:** O defeito mostrado é dependência parcial direta, anterior à análise de dependência transitiva.
- **D) está errada:** A unicidade da chave não impede dependências parciais de atributos não chave.
- **Conceito cobrado:** Segunda Forma Normal.
- **Pegadinha usada:** Achar que uma chave composta basta para garantir 2FN.
- **Como pensar para acertar:** Para cada atributo não chave, teste se ele depende da chave composta inteira.
- **Referência à apostila de estudo:** [Normalização básica](semana_01_estudo.md#s1-d3-normalizacao-base).

### Comentário da Questão 8

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** O enunciado apresenta uma chave simples, portanto não há parte de chave composta a examinar.
- **B) está errada:** Repetição pode indicar redundância, mas 1FN trata da atomicidade de cada valor.
- **C) está correta:** A cadeia entre chave e atributos não chave caracteriza dependência transitiva.
- **D) está errada:** Separar `Departamento` e referenciá-lo por FK é justamente uma solução normalizada.
- **Conceito cobrado:** Terceira Forma Normal.
- **Pegadinha usada:** Confundir repetição visual, dependência parcial e dependência transitiva.
- **Como pensar para acertar:** Expresse as dependências: id_servidor → id_departamento → nome_departamento.
- **Referência à apostila de estudo:** [Normalização básica](semana_01_estudo.md#s1-d3-normalizacao-base).

### Comentário da Questão 9

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está correta:** A alternativa separa corretamente manipulação de linhas e remoção de objeto.
- **B) está errada:** DELETE não elimina a definição; DROP é que remove o objeto do catálogo.
- **C) está errada:** DROP não se limita aos dados e a comparação transacional depende do SGBD, não define os comandos.
- **D) está errada:** A descrição de esvaziar preservando estrutura se aproxima de TRUNCATE; DELETE também pode ser usado sem WHERE.
- **Conceito cobrado:** DELETE x DROP.
- **Pegadinha usada:** Misturar DELETE, TRUNCATE e DROP.
- **Como pensar para acertar:** Pergunte se o alvo são linhas ou o próprio objeto do esquema.
- **Referência à apostila de estudo:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao).

### Comentário da Questão 10

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está correta:** Sem predicado, todas as linhas da tabela participam da atualização.
- **B) está errada:** A ordem física ou a PK não limitam um UPDATE sem WHERE.
- **C) está errada:** WHERE é opcional; sua ausência amplia o conjunto-alvo em vez de tornar o comando inválido.
- **D) está errada:** O novo valor não cria um filtro implícito sobre o estado anterior.
- **Conceito cobrado:** UPDATE sem WHERE.
- **Pegadinha usada:** Inventar filtro implícito ou supor que o SGBD protege automaticamente contra UPDATE global.
- **Como pensar para acertar:** Determine o conjunto de linhas depois do WHERE; sem WHERE, o conjunto é a tabela inteira.
- **Referência à apostila de estudo:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao).

### Comentário da Questão 11

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** String vazia é um valor e não equivale necessariamente à ausência representada por NULL.
- **B) está errada:** Comparações comuns com NULL resultam em desconhecido; não localizam os nulos.
- **C) está errada:** `COALESCE(email, '') = ''` também seleciona string vazia, enquanto o enunciado exige exclusivamente o valor SQL `NULL`.
- **D) está correta:** `IS NULL` testa exatamente o valor SQL `NULL` exigido.
- **Conceito cobrado:** NULL e IS NULL.
- **Pegadinha usada:** Confundir NULL, string vazia e comparação comum.
- **Como pensar para acertar:** Para ausência estrita, use IS NULL sem converter o valor.
- **Referência à apostila de estudo:** [NULL, lógica de três valores e DISTINCT](semana_01_estudo.md#s1-d3-null-distinct).

### Comentário da Questão 12

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** Ela compara as PKs independentes das duas tabelas, não a FK da anuidade com o profissional.
- **B) está correta:** A condição liga a FK `a.id_profissional` à PK `p.id` e retorna os pares correspondentes.
- **C) está errada:** A condição compara duas colunas da própria tabela `anuidade` e não relaciona `profissional`.
- **D) está errada:** CROSS JOIN produz todas as combinações, não apenas pares relacionados.
- **Conceito cobrado:** JOIN e condição de junção.
- **Pegadinha usada:** Usar colunas de mesmo nome ou PKs independentes no lugar do par PK–FK.
- **Como pensar para acertar:** Localize a FK na tabela filha e iguale-a à PK da tabela pai.
- **Referência à apostila de estudo:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins).

### Comentário da Questão 13

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** Produto cartesiano cria pares sem relação e não representa ausência de anuidade.
- **B) está errada:** INNER JOIN elimina profissionais sem correspondência.
- **C) está errada:** Partindo de `profissional`, preservar o lado direito não garante todos os profissionais.
- **D) está correta:** LEFT JOIN preserva cada profissional e preenche com NULL quando não há anuidade correspondente.
- **Conceito cobrado:** LEFT JOIN.
- **Pegadinha usada:** Escolher uma junção externa pelo nome sem observar qual lado precisa ser preservado.
- **Como pensar para acertar:** Coloque o conjunto obrigatório à esquerda e use LEFT JOIN com a condição PK–FK.
- **Referência à apostila de estudo:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins).

### Comentário da Questão 14

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** COUNT(*) conta linhas sem examinar a nulidade de uma coluna específica.
- **B) está correta:** A distinção entre contagem de linhas e de valores não nulos está correta.
- **C) está errada:** Os resultados diferem quando há linhas cujo e-mail é NULL.
- **D) está errada:** COUNT(coluna) conta valores não nulos; ele não converte cada NULL em zero contado.
- **Conceito cobrado:** Funções agregadas e NULL.
- **Pegadinha usada:** Tratar COUNT(*) e COUNT(coluna) como sinônimos diante de NULL.
- **Como pensar para acertar:** Pergunte se a unidade contada é a linha ou um valor presente na coluna.
- **Referência à apostila de estudo:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes).

### Comentário da Questão 15

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais
- **A) está errada:** As duas restrições podem formar uma chave alternativa, mas não substituem automaticamente a PK escolhida.
- **B) está errada:** A integridade de entidade torna a PK não nula sem declaração adicional.
- **C) está correta:** A alternativa separa identificação, unicidade e obrigatoriedade, com a ressalva de portabilidade para NULL em UNIQUE.
- **D) está errada:** Os efeitos foram invertidos: NOT NULL trata ausência e UNIQUE trata duplicidade.
- **Conceito cobrado:** Restrições de integridade.
- **Pegadinha usada:** Confundir chave primária, chave alternativa e obrigatoriedade.
- **Como pensar para acertar:** Associe cada restrição ao seu efeito e não suponha que UNIQUE implica NOT NULL.
- **Referência à apostila de estudo:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade).

### Comentário da Questão 16

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** NOT NULL impede ausência, mas ainda aceita números negativos.
- **B) está correta:** CHECK expressa diretamente o domínio permitido para o valor.
- **C) está errada:** UNIQUE evita repetição, não limita o sinal do número.
- **D) está errada:** DEFAULT fornece valor quando ele é omitido, mas não rejeita um negativo informado.
- **Conceito cobrado:** CHECK constraint.
- **Pegadinha usada:** Confundir valor padrão, obrigatoriedade, unicidade e regra de domínio.
- **Como pensar para acertar:** Quando o requisito é uma condição booleana sobre o valor, traduza-o em CHECK.
- **Referência à apostila de estudo:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade).

### Comentário da Questão 17

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** A sequência erra ao negar a função de GRANT e ao afirmar que COMMIT desfaz.
- **B) está correta:** CREATE TABLE é DDL, GRANT é DCL e COMMIT confirma, portanto a sequência é V, V, F.
- **C) está errada:** CREATE TABLE realmente define estrutura, logo a primeira proposição não é falsa.
- **D) está errada:** A terceira proposição é falsa porque ROLLBACK, antes da confirmação, é o comando de desfazer.
- **Conceito cobrado:** DDL, DCL e TCL.
- **Pegadinha usada:** Trocar DDL/DCL e inverter COMMIT com ROLLBACK.
- **Como pensar para acertar:** Classifique cada comando pelo efeito concreto antes de montar a sequência.
- **Referência à apostila de estudo:** [SQL ANSI básico](semana_01_estudo.md#s1-d3-sql-base).

### Comentário da Questão 18

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** Consistência trata a passagem entre estados válidos; o requisito explícito de indivisibilidade é atomicidade.
- **B) está errada:** Isolamento controla interferência entre transações concorrentes, não a indivisibilidade interna descrita.
- **C) está errada:** Durabilidade protege efeitos já confirmados, enquanto o caso exige desfazer uma execução parcial.
- **D) está correta:** A unidade lógica deve confirmar ambas as operações ou não conservar nenhuma.
- **Conceito cobrado:** ACID: atomicidade.
- **Pegadinha usada:** Confundir as quatro propriedades ACID diante de uma falha parcial.
- **Como pensar para acertar:** Associe “todas as etapas ou nenhuma” diretamente à atomicidade.
- **Referência à apostila de estudo:** [Transações e ACID](semana_01_estudo.md#s1-d3-transacoes-acid).

### Comentário da Questão 19

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** Índice comum não impõe unicidade; isso requer índice ou restrição UNIQUE.
- **B) está errada:** O ganho depende do plano e do predicado, e inserções/atualizações precisam manter o índice.
- **C) está correta:** A alternativa apresenta o benefício de leitura e o custo de manutenção sem prometer ganho universal.
- **D) está errada:** O otimizador pode escolher varredura e o índice não ajuda automaticamente filtros em outras colunas.
- **Conceito cobrado:** Índices.
- **Pegadinha usada:** Tratar índice como garantia de unicidade ou aceleração universal e gratuita.
- **Como pensar para acertar:** Relacione a coluna e o padrão de acesso, depois considere custo de espaço e escrita.
- **Referência à apostila de estudo:** [Índices e custo de manutenção](semana_01_estudo.md#s1-d3-indices).

### Comentário da Questão 20

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** View comum é lógica; materialização é uma modalidade específica, não obrigatória.
- **B) está errada:** Views podem apoiar segurança, mas continuam sujeitas à política de privilégios.
- **C) está errada:** A atualizabilidade depende da definição da view e das regras do SGBD.
- **D) está correta:** Ela encapsula uma consulta e apresenta seu resultado como relação lógica.
- **Conceito cobrado:** Views.
- **Pegadinha usada:** Generalizar materialização, atualizabilidade ou permissões de views.
- **Como pensar para acertar:** Pense primeiro em consulta armazenada lógica; trate os demais comportamentos como condicionais.
- **Referência à apostila de estudo:** [Views, procedures e triggers](semana_01_estudo.md#s1-d3-objetos-programaveis).

### Comentário da Questão 21

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Aprofundamento
- **A) está errada:** Uma trigger AFTER reage ao comando, não espera necessariamente o COMMIT, e não ganha persistência independente.
- **B) está correta:** Sem transação autônoma específica, o efeito automático da trigger integra a mesma unidade transacional do INSERT.
- **C) está errada:** Triggers são disparadas pelo evento configurado, não por chamada explícita da aplicação.
- **D) está errada:** Os efeitos da trigger participam da transação e podem ser desfeitos com ela.
- **Conceito cobrado:** Triggers.
- **Pegadinha usada:** Confundir execução automática com persistência autônoma.
- **Como pensar para acertar:** Descubra primeiro em qual transação o efeito foi produzido; depois aplique COMMIT ou ROLLBACK à unidade inteira.
- **Referência à apostila de estudo:** [Trigger, transação, rollback e auditoria](semana_01_estudo.md#s1-d3-trigger-transacional).

### Comentário da Questão 22

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Aprofundamento
- **A) está correta:** Procedure é adequada para receber parâmetros e coordenar validação, inserção e atualização.
- **B) está errada:** Trigger é ligada a evento no banco; o requisito descreve chamada explícita com parâmetros.
- **C) está errada:** CHECK valida uma expressão sobre dados e não encapsula uma sequência geral de comandos.
- **D) está errada:** View representa consulta e não é, por definição, uma rotina parametrizada de DML encadeado.
- **Conceito cobrado:** Stored procedures.
- **Pegadinha usada:** Confundir rotina chamada, consulta lógica, evento automático e restrição declarativa.
- **Como pensar para acertar:** Separe quem chama o objeto e se ele apenas mostra dados ou executa uma sequência de ações.
- **Referência à apostila de estudo:** [Views, procedures e triggers](semana_01_estudo.md#s1-d3-objetos-programaveis).

### Comentário da Questão 23

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Aprofundamento
- **A) está errada:** A expressão não contém agrupamento nem preserva todas as colunas.
- **B) está errada:** A seleção interna filtra as tuplas e não há operação de ordenação.
- **C) está errada:** Não existe função de contagem nem agrupamento na expressão.
- **D) está correta:** Sigma seleciona as linhas pela condição e pi projeta somente o atributo `nome`.
- **Conceito cobrado:** Álgebra relacional.
- **Pegadinha usada:** Inverter seleção e projeção ou acrescentar ordenação/agregação inexistentes.
- **Como pensar para acertar:** Leia de dentro para fora: primeiro σ filtra tuplas; depois π escolhe atributos.
- **Referência à apostila de estudo:** [Álgebra relacional](semana_01_estudo.md#s1-d3-algebra-relacional).

### Comentário da Questão 24

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** Uma lista em atributo perde atomicidade e dificulta representar os dados próprios de cada ocorrência.
- **B) está errada:** Domínio restringe valores de atributo; não representa ocorrências com número, data e responsável.
- **C) está correta:** Cada fiscalização possui identidade e atributos, e várias podem apontar para um processo.
- **D) está errada:** Os dados são persistentes e próprios, portanto não constituem mero atributo derivado.
- **Conceito cobrado:** Modelo Entidade-Relacionamento.
- **Pegadinha usada:** Reduzir uma entidade dependente com atributos próprios a um campo ou domínio.
- **Como pensar para acertar:** Se o conceito tem várias ocorrências e atributos próprios, modele-o como entidade e defina a cardinalidade.
- **Referência à apostila de estudo:** [Modelo Entidade-Relacionamento e mapeamento](semana_01_estudo.md#s1-d3-mer-mapeamento).

### Comentário da Questão 25

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** A repetição duplica os dados da pessoa e cria anomalias de atualização.
- **B) está errada:** Colunas numeradas criam grupo repetido, limite artificial e muitos nulos.
- **C) está errada:** A string reúne vários valores sem integridade individual nem consulta relacional adequada.
- **D) está correta:** Cada telefone passa a ocupar linha própria, com atributos atômicos e vínculo referencial à pessoa.
- **Conceito cobrado:** Atributos multivalorados e 1FN.
- **Pegadinha usada:** Escolher colunas repetidas, lista delimitada ou duplicação da entidade principal.
- **Como pensar para acertar:** Transforme cada ocorrência multivalorada em uma linha relacionada por FK.
- **Referência à apostila de estudo:** [Modelo Entidade-Relacionamento e mapeamento](semana_01_estudo.md#s1-d3-mer-mapeamento).

### Comentário da Questão 26

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está errada:** A estrutura lógica usada pela aplicação foi mantida; não houve substituição do modelo conceitual.
- **B) está errada:** Integridade referencial pode continuar válida, mas não nomeia a separação entre níveis descrita.
- **C) está correta:** Alterações de armazenamento e índices sem mudança das consultas exemplificam independência física.
- **D) está errada:** Durabilidade trata persistência após confirmação, não desacoplamento físico–lógico.
- **Conceito cobrado:** Independência física de dados.
- **Pegadinha usada:** Confundir nível físico, integridade e propriedade transacional.
- **Como pensar para acertar:** Pergunte qual nível mudou e qual nível permaneceu estável.
- **Referência à apostila de estudo:** [Conceitos e arquitetura de SGBD](semana_01_estudo.md#s1-d3-conceitos-sgbd).

### Comentário da Questão 27

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento
- **A) está correta:** Tipos, defaults, constraints e índices são dados sobre objetos do banco.
- **B) está errada:** O log registra operações para recuperação; não é o catálogo estrutural completo.
- **C) está errada:** Os valores de negócio não descrevem a estrutura de colunas, padrões e restrições.
- **D) está errada:** O catálogo não precisa duplicar fisicamente o conteúdo das tabelas de negócio.
- **Conceito cobrado:** Dicionário de dados e metadados.
- **Pegadinha usada:** Confundir metadados, dados de negócio, log e cópia física.
- **Como pensar para acertar:** Se a informação descreve objetos e regras do banco, ela pertence ao dicionário de dados.
- **Referência à apostila de estudo:** [Metadados, catálogo e independência física](semana_01_estudo.md#s1-d3-metadados-catalogo).

### Comentário da Questão 28

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Aprofundamento
- **A) está errada:** Ser PK da relação não faz `id_lancamento` ser determinado pelo setor agrupado; há vários IDs por setor.
- **B) está correta:** A projeção mistura granularidade de setor com um ID individual sem regra que escolha um ID do grupo.
- **C) está errada:** Agregações podem ser usadas sem HAVING; HAVING apenas filtra grupos quando necessário.
- **D) está errada:** A ordem visual das expressões projetadas não corrige a incompatibilidade de granularidade.
- **Conceito cobrado:** GROUP BY e colunas não agregadas.
- **Pegadinha usada:** Supor que qualquer PK pode ser projetada em um agrupamento ou exigir HAVING para toda agregação.
- **Como pensar para acertar:** Cada expressão não agregada deve ser compatível com a granularidade do grupo; aqui setor não determina um único lançamento.
- **Referência à apostila de estudo:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes).

### Comentário da Questão 29

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Aprofundamento
- **A) está errada:** Excluir o objeto seria efeito de DROP TABLE, não de DELETE filtrado.
- **B) está errada:** FKs podem restringir a exclusão ou definir ações diferentes; cascata não é automática em todos os casos.
- **C) está correta:** DELETE atua nas linhas filtradas, preserva o objeto e integra a transação ainda não confirmada.
- **D) está errada:** Antes da confirmação, ROLLBACK pode desfazer o DML dentro do modelo transacional descrito.
- **Conceito cobrado:** DELETE com WHERE.
- **Pegadinha usada:** Confundir linhas, objeto, cascata referencial e confirmação transacional.
- **Como pensar para acertar:** Separe três perguntas: o que DELETE atinge, o que as FKs permitem e se já houve COMMIT.
- **Referência à apostila de estudo:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao).

### Comentário da Questão 30

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Aprofundamento
- **A) está errada:** NULL explícito não aciona o DEFAULT e viola o NOT NULL de `uf`.
- **B) está errada:** Sem lista de colunas, os valores não correspondem corretamente ao esquema que também contém `id` e `uf`.
- **C) está errada:** UPDATE não insere linhas e a expressão SET apresentada não é atribuição válida.
- **D) está correta:** Ao omitir `id` gerado e `uf`, cada linha recebe a identidade e o padrão definidos pelo esquema.
- **Conceito cobrado:** INSERT.
- **Pegadinha usada:** Confundir omissão de coluna com NULL explícito e ignorar coluna de identidade.
- **Como pensar para acertar:** Liste apenas as colunas fornecidas; deixe identidade e DEFAULT serem preenchidos pelo SGBD.
- **Referência à apostila de estudo:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao).

### Comentário da Questão 31

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está correta:** A matriz ANSI associa `REPEATABLE READ` à prevenção de leituras sujas e não repetíveis, mas ainda admite fantasmas; implementações específicas podem oferecer garantia mais forte.
- **B) está errada:** READ COMMITTED impede ler dado não confirmado, mas outra transação pode confirmar mudança entre as leituras.
- **C) está errada:** READ UNCOMMITTED é justamente o nível associado à possibilidade de leitura suja.
- **D) está errada:** Serializable é um nível forte, mas ainda depende de transações, confirmação e controle de concorrência.
- **Conceito cobrado:** Isolamento transacional.
- **Pegadinha usada:** Transformar um nível em garantia maior do que ele oferece ou dispensar o mecanismo transacional.
- **Como pensar para acertar:** Compare cada nível com as anomalias que ele impede, sem extrapolar a garantia.
- **Referência à apostila de estudo:** [Isolamento e anomalias](semana_01_estudo.md#s1-d3-isolamento).

### Comentário da Questão 32

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está errada:** Uma chave alternativa UNIQUE não substitui automaticamente a PK declarada.
- **B) está correta:** A alternativa preserva os papéis distintos e evita absolutizar o tratamento de NULL entre implementações.
- **C) está errada:** Obrigatoriedade é efeito de NOT NULL, não consequência universal de UNIQUE.
- **D) está errada:** A PK permanece única independentemente dos valores de outra coluna.
- **Conceito cobrado:** UNIQUE x PRIMARY KEY.
- **Pegadinha usada:** Confundir chave alternativa com chave primária e UNIQUE com NOT NULL.
- **Como pensar para acertar:** Leia cada restrição separadamente e preserve a ressalva de portabilidade para NULL.
- **Referência à apostila de estudo:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade).

### Comentário da Questão 33

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está errada:** O predicado no WHERE rejeita o NULL do lado direito e elimina justamente os profissionais sem cidade.
- **B) está errada:** INNER JOIN elimina os profissionais que não têm cidade correspondente.
- **C) está errada:** A condição usa a PK do profissional em lugar da FK da cidade.
- **D) está correta:** LEFT JOIN preserva todos os profissionais e relaciona a FK `id_cidade` à PK de `cidade`.
- **Conceito cobrado:** Condição de JOIN por PK/FK.
- **Pegadinha usada:** Acertar o tipo de JOIN, mas errar a chave ou neutralizar o efeito externo no WHERE.
- **Como pensar para acertar:** Preserve a tabela obrigatória à esquerda, ligue FK à PK e não rejeite depois os NULLs da direita.
- **Referência à apostila de estudo:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins).

### Comentário da Questão 34

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Revisão
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não é a resposta:** A afirmação é correta, pois dependência parcial pressupõe chave composta.
- **B) não é a resposta:** A afirmação é correta; a cadeia pode descrever dependência transitiva entre atributos não chave.
- **C) é a resposta:** A afirmação é incorreta; decompor sem examinar junção sem perda e dependências pode eliminar associações ou permitir estados indevidos.
- **D) não é a resposta:** A afirmação é correta; normalização e desempenho não são sinônimos, e a decomposição pode exigir mais joins.
- **Conceito cobrado:** Normalização.
- **Pegadinha usada:** Tratar normalização como simples divisão física de colunas, sem analisar dependências.
- **Como pensar para acertar:** Valide cada forma normal pelas dependências e não aceite uma decomposição só porque criou mais tabelas.
- **Referência à apostila de estudo:** [Dependências e decomposição](semana_01_estudo.md#s1-d3-normalizacao-decomposicao).

### Comentário da Questão 35

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está correta:** A consulta ordena pelos maiores valores, resolve empates pelo menor ID e limita a três linhas.
- **B) está errada:** A ordenação crescente escolhe os menores valores.
- **C) está errada:** OFFSET 3 descarta as três primeiras linhas em vez de retorná-las.
- **D) está errada:** Sem ORDER BY, não há garantia de que as três linhas sejam as de maior valor.
- **Conceito cobrado:** ORDER BY e limitação de resultados.
- **Pegadinha usada:** Limitar antes de definir uma ordem determinística ou inverter ASC/DESC.
- **Como pensar para acertar:** Primeiro estabeleça a ordenação completa; depois aplique o limite de linhas.
- **Referência à apostila de estudo:** [Consultas, ordem lógica, ordenação e limitação](semana_01_estudo.md#s1-d3-sql-consultas).

### Comentário da Questão 36

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está errada:** Há diferenças importantes e dependentes do SGBD; a equivalência universal é falsa.
- **B) está correta:** A descrição mantém o núcleo comum e explicita os pontos de portabilidade.
- **C) está errada:** TRUNCATE não é remoção linha a linha com predicado.
- **D) está errada:** DROP remove o objeto, não apenas seu conteúdo.
- **Conceito cobrado:** DELETE x TRUNCATE.
- **Pegadinha usada:** Absolutizar detalhes dependentes do SGBD ou trocar remoção de dados por remoção de objeto.
- **Como pensar para acertar:** Memorize o núcleo de cada comando e trate transação, log, identidade e FKs como detalhes de implementação.
- **Referência à apostila de estudo:** [INSERT, UPDATE, DELETE, TRUNCATE e DROP](semana_01_estudo.md#s1-d3-comandos-alteracao).

### Comentário da Questão 37

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está errada:** O WHERE rejeita o NULL da linha estendida e elimina setores sem profissional ativo.
- **B) está correta:** O filtro no ON limita correspondências ativas, LEFT preserva setores vazios e COUNT da chave direita produz zero sem par.
- **C) está errada:** COUNT(*) conta também a linha preservada sem correspondência, produzindo um em vez de zero.
- **D) está errada:** INNER JOIN só conserva setores com ao menos uma correspondência ativa.
- **Conceito cobrado:** LEFT JOIN e NULL.
- **Pegadinha usada:** Neutralizar o LEFT JOIN no WHERE ou contar a linha estendida com COUNT(*).
- **Como pensar para acertar:** Filtre o lado opcional no ON e conte uma coluna não nula apenas quando houver correspondência.
- **Referência à apostila de estudo:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins).

### Comentário da Questão 38

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está errada:** Uma FK única limita o profissional a uma pessoa jurídica e não representa o histórico N:N.
- **B) está errada:** A coluna guarda apenas o responsável atual e não permite vários vínculos nem períodos completos.
- **C) está correta:** A associativa representa cada vínculo e seus atributos próprios ao longo do tempo.
- **D) está errada:** Texto livre perde atomicidade, referências e validação temporal.
- **Conceito cobrado:** Modelagem de relacionamento com atributos.
- **Pegadinha usada:** Modelar apenas o estado atual ou esconder histórico N:N em texto.
- **Como pensar para acertar:** Quando o relacionamento possui atributos e multiplicidade nos dois lados, transforme-o em tabela associativa.
- **Referência à apostila de estudo:** [Participação, cardinalidade e vínculos temporais](semana_01_estudo.md#s1-d3-participacao-temporalidade).

### Comentário da Questão 39

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Revisão
- **A) está correta:** Consistência da captura e teste de restauração tratam tanto geração quanto recuperabilidade do backup.
- **B) está errada:** Exportações independentes podem observar instantes diferentes e quebrar relações entre tabelas.
- **C) está errada:** Arquivos copiados durante escrita podem não representar estado recuperável e coerente.
- **D) está errada:** Índices são estruturas de acesso e não cópias recuperáveis dos dados.
- **Conceito cobrado:** Backup e recuperação em SGBD.
- **Pegadinha usada:** Confundir cópia de arquivos ou exportações isoladas com backup consistente e testado.
- **Como pensar para acertar:** Verifique o ponto consistente da captura e nunca considere o backup confiável sem restauração de teste.
- **Referência à apostila de estudo:** [Backup lógico consistente e restauração](semana_01_estudo.md#s1-d3-backup-consistente).

### Comentário da Questão 40

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Revisão
- **A) está errada:** LIKE não cria atomicidade nem integridade individual e pode produzir correspondências imprecisas.
- **B) está errada:** Duplicar o documento introduz redundância e anomalias de atualização.
- **C) está errada:** Colunas numeradas criam limite artificial, grupos repetidos e muitos nulos.
- **D) está correta:** A tabela separa as ocorrências e permite chave, FK e restrição por tag.
- **Conceito cobrado:** 1FN e atributos multivalorados.
- **Pegadinha usada:** Preservar lista delimitada ou trocar uma lista por colunas repetidas.
- **Como pensar para acertar:** Uma ocorrência por linha permite atomicidade, chaves e consultas relacionais exatas.
- **Referência à apostila de estudo:** [Normalização básica](semana_01_estudo.md#s1-d3-normalizacao-base).

### Comentário da Questão 41

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Simulado
- **A) está errada:** Uma FK exige chave referenciada adequada e não substitui UNIQUE, NOT NULL e CHECK requeridos.
- **B) está errada:** Criar outra PRIMARY KEY conflita com a PK técnica já existente e não restringe a situação.
- **C) está errada:** O CHECK de não nulidade não impede duplicação e a situação continua sem domínio definido.
- **D) está correta:** Mantém `id` como PK e expressa separadamente obrigatoriedade, unicidade e domínio de situação.
- **Conceito cobrado:** NOT NULL e UNIQUE.
- **Pegadinha usada:** Tentar substituir a PK técnica ou usar uma única restrição para três requisitos diferentes.
- **Como pensar para acertar:** Traduza cada regra do domínio em sua constraint própria, sem alterar a chave já escolhida.
- **Referência à apostila de estudo:** [Restrições, valores padrão e integridade referencial](semana_01_estudo.md#s1-d3-restricoes-integridade).

### Comentário da Questão 42

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Uso:** Simulado
- **A) está errada:** Independência física evita a reescrita das visões por mera reorganização interna, e rollback não assegura sozinho a persistência de commits.
- **B) está correta:** Os mapeamentos do SGBD desacoplam o nível físico dos demais, enquanto concorrência, log e recuperação preservam as propriedades transacionais.
- **C) está errada:** As visões compartilham o esquema lógico, e backup periódico não substitui isolamento nem recuperação transacional.
- **D) está errada:** SQL expressa operações, mas os mecanismos de mapeamento, escalonamento e recuperação são implementados pelo SGBD.
- **Conceito cobrado:** Arquitetura de três esquemas, independência física e serviços transacionais do SGBD.
- **Pegadinha usada:** Atribuir à linguagem ou ao backup funções operacionais do SGBD e confundir mudança física com mudança lógica.
- **Como pensar para acertar:** Separe os níveis de abstração e identifique qual componente preserva tanto os mapeamentos quanto as garantias de transação.
- **Referência à apostila de estudo:** [Conceitos de SGBD e independência física](semana_01_estudo.md#s1-d3-conceitos-sgbd), [isolamento e anomalias](semana_01_estudo.md#s1-d3-isolamento) e [log, redo, undo e recuperação](semana_01_estudo.md#s1-d3-log-recuperacao).

### Comentário da Questão 43

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **Uso:** Simulado
- **A) está correta:** A view aplica projeção e seleção no banco, e a ausência de privilégio na tabela-base impede contornar essas restrições.
- **B) está errada:** O acesso à tabela-base expõe CPF e linhas inativas se o filtro da aplicação falhar ou for omitido.
- **C) está errada:** Restringir colunas não restringe linhas; profissionais inativos continuariam acessíveis.
- **D) está errada:** O privilégio mantido na tabela-base oferece um caminho de leitura que ignora a proteção da view.
- **Conceito cobrado:** Menor privilégio, views de segurança, projeção e seleção.
- **Pegadinha usada:** Confundir restrição de coluna com restrição de linha ou confiar em filtro aplicado apenas pelo cliente.
- **Como pensar para acertar:** Liste dados, linhas e operações permitidos e elimine qualquer privilégio que permita ultrapassar um desses limites.
- **Referência à apostila de estudo:** [Segurança e menor privilégio com views](semana_01_estudo.md#s1-d3-menor-privilegio).

### Comentário da Questão 44

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **Uso:** Simulado
- **A) está correta:** A trigger centraliza a reação automática, mas exige avaliação dos efeitos transacionais e operacionais.
- **B) está errada:** A solução fica dispersa e uma aplicação pode omitir ou implementar a auditoria de forma diferente.
- **C) está errada:** View comum representa consulta e não funciona automaticamente como interceptador de UPDATE.
- **D) está errada:** Índice acelera acesso; não é histórico de auditoria das versões modificadas.
- **Conceito cobrado:** Triggers de auditoria.
- **Pegadinha usada:** Confundir automação por evento com view, índice ou código voluntário de cada cliente.
- **Como pensar para acertar:** Escolha o objeto acionado pelo próprio evento e avalie seu vínculo com a transação principal.
- **Referência à apostila de estudo:** [Trigger, transação, rollback e auditoria](semana_01_estudo.md#s1-d3-trigger-transacional).

### Comentário da Questão 45

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **Uso:** Simulado
- **A) está errada:** A FK anulável permite anuidade sem profissional, e o índice por exercício não impede duplicidade por profissional e ano.
- **B) está errada:** A FK no lado de `Profissional` limita o vínculo e induz repetição da entidade a cada exercício.
- **C) está correta:** A FK `NOT NULL` garante um profissional por anuidade, a ausência de linha preserva a participação opcional e a restrição composta evita duplicidade anual.
- **D) está errada:** O domínio descreve um-para-muitos, não muitos-para-muitos, e não admite anuidades sem profissional.
- **Conceito cobrado:** Mapeamento 1:N, participação obrigatória e chave candidata composta.
- **Pegadinha usada:** Modelar apenas a cardinalidade máxima e esquecer participação mínima ou unicidade dependente do exercício.
- **Como pensar para acertar:** Traduza separadamente as três regras: lado da FK, nulabilidade da FK e combinação de atributos que deve ser única.
- **Referência à apostila de estudo:** [Participação, cardinalidade e vínculos temporais](semana_01_estudo.md#s1-d3-participacao-temporalidade).

### Comentário da Questão 46

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Simulado
- **A) está errada:** A decomposição não deve perder a informação de departamento do servidor.
- **B) está errada:** UNIQUE não elimina a dependência transitiva e ainda impediria vários servidores no mesmo departamento.
- **C) está correta:** A decomposição representa cada fato em sua relação e preserva o vínculo por FK.
- **D) está errada:** A tabela de departamento deve ser identificada pelo departamento, não pelo servidor.
- **Conceito cobrado:** Dependência funcional e 3FN.
- **Pegadinha usada:** Declarar UNIQUE para mascarar dependência ou decompor com a chave errada.
- **Como pensar para acertar:** Coloque cada atributo junto de seu determinante e mantenha a associação por chave estrangeira.
- **Referência à apostila de estudo:** [Dependências e decomposição](semana_01_estudo.md#s1-d3-normalizacao-decomposicao).

### Comentário da Questão 47

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **Uso:** Simulado
- **A) está errada:** DISTINCT considera o conjunto completo de colunas projetadas, não somente a primeira.
- **B) está errada:** A eliminação de duplicatas também se aplica a projeções com várias colunas.
- **C) está errada:** Para eliminação de duplicatas, as duas ocorrências do mesmo par com NULL não geram linhas separadas.
- **D) está correta:** Os pares repetidos são reduzidos a uma ocorrência, inclusive o par com NULL no resultado DISTINCT.
- **Conceito cobrado:** DISTINCT.
- **Pegadinha usada:** Aplicar DISTINCT a uma coluna isolada ou tratar cada NULL como linha distinta no resultado.
- **Como pensar para acertar:** Forme os pares projetados e elimine repetições do par completo.
- **Referência à apostila de estudo:** [NULL, lógica de três valores e DISTINCT](semana_01_estudo.md#s1-d3-null-distinct).

### Comentário da Questão 48

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Uso:** Simulado
- **A) está errada:** Registrar uma alteração não confirmada não autoriza torná-la permanente; T2 deve ser desfeita.
- **B) está correta:** A recuperação conserva T1 pela durabilidade e elimina os efeitos parciais de T2 pela atomicidade.
- **C) está errada:** A ordem temporal não substitui o estado de confirmação; uma transação sem commit não prevalece sobre outra confirmada.
- **D) está errada:** Isolamento controla interferência concorrente, mas não exige apagar uma transação cujo commit já foi reconhecido.
- **Conceito cobrado:** Recuperação com log, atomicidade e durabilidade.
- **Pegadinha usada:** Confundir alteração mais recente com alteração confirmada ou tratar toda falha como motivo para desfazer todos os commits.
- **Como pensar para acertar:** Classifique cada transação no instante da falha: committed deve sobreviver; uncommitted deve ser desfeita.
- **Referência à apostila de estudo:** [Log, redo, undo e recuperação](semana_01_estudo.md#s1-d3-log-recuperacao).

### Comentário da Questão 49

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Uso:** Simulado
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não é a resposta:** A afirmação é correta; o filtro posterior pode neutralizar a preservação da linha esquerda.
- **B) é a resposta:** A afirmação é incorreta; a posição do predicado pode alterar quais linhas são correspondidas ou eliminadas.
- **C) não é a resposta:** A afirmação é correta; `COUNT(chave_da_direita)` e `COUNT(*)` diferem quando não há correspondência.
- **D) não é a resposta:** A afirmação é correta; falhar no `ON` produz ausência de par, mas a linha esquerda permanece.
- **Conceito cobrado:** JOINs.
- **Pegadinha usada:** Tratar ON e WHERE como intercambiáveis em LEFT JOIN.
- **Como pensar para acertar:** Simule uma linha sem correspondência e acompanhe o NULL pelo ON, WHERE e COUNT.
- **Referência à apostila de estudo:** [Junções, ON e WHERE](semana_01_estudo.md#s1-d3-joins).

### Comentário da Questão 50

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Simulado
- **A) está correta:** A alternativa segue corretamente a ordem lógica FROM/WHERE/GROUP BY/HAVING/SELECT/ORDER BY.
- **B) está errada:** A condição de dez está no HAVING sobre COUNT, não sobre identificador individual.
- **C) está errada:** ORDER BY atua no resultado agregado e nenhum comando modifica a tabela física.
- **D) está errada:** WHERE é aplicado antes do agrupamento, então as demais UFs nem entram nos grupos.
- **Conceito cobrado:** GROUP BY e ORDER BY com agregação.
- **Pegadinha usada:** Ler o SELECT na ordem escrita e aplicar HAVING a linhas individuais.
- **Como pensar para acertar:** Reordene mentalmente as cláusulas pela execução lógica e acompanhe o conjunto em cada etapa.
- **Referência à apostila de estudo:** [Agregações, GROUP BY, HAVING e contagens](semana_01_estudo.md#s1-d3-agregacoes).

### Comentários das questões extras de revisão fixa do Dia 3

#### Comentário Extra Dia 3.1

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Revisão.

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

- **Uso:** Revisão.

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

- **Uso:** Revisão.

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

- **Uso:** Revisão.

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

- **Uso:** Revisão.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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
**Uso:** Essenciais
**Referência:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt)

Uma sociedade empresária sediada no Paraná passa a oferecer, de modo habitual, serviços técnicos enquadrados no campo da Administração, mas sustenta que o CNPJ ativo torna desnecessária qualquer providência perante o conselho profissional. À luz da legislação estudada, a conclusão correta é:

A) somente os sócios pessoas físicas podem estar sujeitos ao Sistema CFA/CRAs, nunca a pessoa jurídica.
B) a natureza das atividades pode sujeitar a empresa ao registro e à fiscalização do CRA-PR, no âmbito de sua jurisdição.
C) cabe ao CFA realizar diretamente todo registro e toda fiscalização local, pois os CRAs exercem apenas função consultiva.
D) o CNPJ e a indicação informal de um profissional registrado tornam desnecessária a análise da atividade básica da empresa.

### Questão 2
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes)

Um profissional permite que terceiro utilize seu número de registro para assinar documento técnico que ele não elaborou nem supervisionou. Segundo o Código de Ética estudado, essa conduta:

A) pode configurar uso indevido do nome ou do registro e é incompatível com a responsabilidade profissional.
B) gera apenas necessidade de atualização cadastral, sem repercussão ética.
C) torna-se regular se houver consentimento escrito entre os envolvidos.
D) é admitida quando o documento eletrônico também contém a assinatura do verdadeiro autor.

### Questão 3
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

O CRA-PR identifica pessoa física exercendo atividade sujeita ao registro profissional, em município paranaense, sem a regularidade exigida. A providência institucional mais compatível com suas atribuições é:

A) fiscalizar a regularidade do exercício profissional dentro de sua jurisdição.
B) aguardar provocação formal do CFA, pois o CRA não pode iniciar fiscalização regional.
C) remeter obrigatoriamente o caso ao CFA, que detém competência exclusiva para toda atuação local.
D) limitar-se à cobrança de anuidades, porque a verificação do exercício profissional não integra suas funções.

### Questão 4
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

Assinale a alternativa que distingue corretamente as funções do CFA e dos CRAs no sistema profissional.

A) O CFA executa ordinariamente a fiscalização em cada município, e os CRAs apenas emitem pareceres consultivos.
B) Cada CRA pode afastar norma nacional do CFA sempre que entender mais adequada uma disciplina local.
C) O CFA exerce função normativa e orientadora em âmbito nacional, enquanto o CRA atua no registro e na fiscalização em sua região.
D) CFA e CRA possuem a mesma competência territorial, variando apenas a denominação do órgão.

### Questão 5
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento)

No conjunto normativo indicado para o CRA-PR, a RN CFA nº 651/2024 tem por objeto:

A) aprovar o Regimento Interno do CRA-PR.
B) aprovar o Regulamento das Eleições do Sistema CFA/CRAs.
C) instituir o Programa Especial de Recuperação de Créditos dos Conselhos Regionais.
D) aprovar o Regulamento de Registro de pessoas físicas e jurídicas do Sistema CFA/CRAs.

### Questão 6
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Código de Ética e RN 671/2025](semana_01_estudo.md#s1-d4-codigo-etica)

De acordo com a consolidação normativa utilizada no edital, o Código de Ética e Disciplina dos Profissionais de Administração está aprovado pela:

A) RN CFA nº 640/2024, que permaneceu vigente sem revogação posterior.
B) RN CFA nº 649/2024, dedicada ao registro profissional.
C) RN CFA nº 651/2024, que aprovou o Regimento Interno do CRA-PR.
D) RN CFA nº 671/2025.

### Questão 7
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres)

Um profissional conhece informação confidencial de cliente em razão de trabalho regularmente executado. Segundo o Código de Ética, ele deve:

A) manter silêncio absoluto até mesmo diante de dever legal específico ou requisição legítima.
B) preservar o sigilo, ressalvadas a justa causa e as hipóteses legais ou profissionais cabíveis.
C) tratar o sigilo como facultativo quando não conseguir identificar prejuízo econômico imediato.
D) compartilhar a informação com parceiros comerciais sempre que eles também estiverem sujeitos a dever genérico de confidencialidade.

### Questão 8
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes)

Durante fiscalização regular, uma pessoa jurídica registrada oculta documentos pertinentes e cria obstáculos deliberados ao trabalho do CRA. À luz do material, essa conduta:

A) é apenas irregularidade procedimental sem relevância quando o registro da empresa está ativo.
B) decorre do direito de defesa, que autoriza recusa geral e imotivada a qualquer solicitação fiscalizatória.
C) não pode ser examinada pelo Código de Ética, pois suas disposições alcançam exclusivamente pessoas físicas.
D) pode caracterizar obstrução à fiscalização e gerar repercussão ética ou administrativa.

### Questão 9
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Lei 4.769/1965](semana_01_estudo.md#s1-d4-lei-4769)

A Lei Federal nº 4.769/1965 ocupa posição central no estudo porque:

A) disciplina exclusivamente anuidades, taxas e execução de créditos dos conselhos.
B) aprova diretamente o atual Regimento Interno do CRA-PR.
C) dispõe sobre o exercício da profissão de Administrador e fornece base legal ao Sistema CFA/CRAs.
D) institui apenas regras éticas, sem tratar da organização profissional.

### Questão 10
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Decreto 61.934/1967](semana_01_estudo.md#s1-d4-decreto-61934)

Quanto à relação entre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967, assinale a alternativa correta.

A) O decreto pode afastar comandos da lei quando trouxer solução administrativa posterior.
B) O decreto regulamenta a lei profissional, devendo permanecer dentro dos limites legais.
C) O decreto constitui regimento autônomo do CRA-PR e não se relaciona ao exercício profissional.
D) O decreto cuida apenas das eleições do Sistema CFA/CRAs.

### Questão 11
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento)

Conforme o Regimento Interno estudado, o CRA-PR é:

A) autarquia federal de atuação nacional, subordinada hierarquicamente ao CFA em todos os seus atos administrativos.
B) autarquia dotada de personalidade jurídica de direito público, autonomia técnica, administrativa e financeira e jurisdição no Estado do Paraná.
C) empresa pública estadual encarregada de executar políticas de emprego para administradores.
D) associação privada de filiação facultativa, sem poder de fiscalização profissional.

### Questão 12
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

A edição de orientação normativa geral destinada a todos os Conselhos Regionais de Administração situa-se, em regra, na esfera do:

A) coletivo de pessoas físicas e jurídicas registradas, por votação direta.
B) Plenário do CRA-PR, por ser órgão deliberativo superior em toda a federação.
C) conjunto dos CRAs, independentemente de deliberação ou norma nacional do CFA.
D) CFA, por sua função normativa e orientadora nacional.

### Questão 13
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670)

Por que a RN CFA nº 649/2024 e a RN CFA nº 670/2025 devem ser lidas em conjunto?

A) A primeira aprova o Regulamento de Registro e a segunda o altera.
B) A primeira aprova o regulamento eleitoral e a segunda altera o processo de votação.
C) Ambas substituem integralmente a Lei nº 4.769/1965 no tema do exercício profissional.
D) A primeira aprova o Código de Ética e a segunda disciplina suas sanções.

### Questão 14
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589)

No mapa de normas do edital, a RN CFA nº 589/2020 está associada ao tema:

A) Regimento Interno do CRA-PR.
B) eleições no Sistema CFA/CRAs.
C) fiscalização no Sistema CFA/CRAs.
D) Código de Ética aprovado em 2025.

### Questão 15
**Nível: Médio**
**Uso:** Essenciais
**Referência:** [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626)

Conforme a ementa oficial consolidada no material, a RN CFA nº 626/2023 relaciona-se ao:

A) funcionamento interno do CRA-PR.
B) Regulamento de Registro do Sistema CFA/CRAs.
C) Programa Especial de Recuperação de Créditos — PERC.
D) Código de Ética e Disciplina.

### Questão 16
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [RN 546/2018 — isenção de débitos](semana_01_estudo.md#s1-d4-rn-546)

A RN CFA nº 546/2018 foi incluída no edital por tratar da:

A) aprovação do Código de Ética e Disciplina.
B) recuperação especial de créditos por meio do PERC.
C) alteração do Regulamento de Registro do Sistema CFA/CRAs.
D) isenção de débitos concedida pelos Conselhos Regionais de Administração.

### Questão 17
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Lei 12.514/2011 — contribuições e cobrança](semana_01_estudo.md#s1-d4-lei-12514)

A Lei nº 12.514/2011 integra o estudo do sistema de conselhos profissionais principalmente porque disciplina:

A) contribuições devidas aos conselhos profissionais e aspectos de sua cobrança.
B) campos privativos de atuação previstos para o Administrador.
C) a estrutura interna específica do CRA-PR.
D) deveres éticos e hipóteses de sigilo dos Profissionais de Administração.

### Questão 18
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento); [Diretoria Executiva](semana_01_estudo.md#s1-d4-diretoria); [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

Em processo administrativo fiscal por fato ocorrido no Paraná, a unidade de fiscalização conclui a instrução. A Diretoria Executiva pretende realizar o julgamento de primeira instância por administrar as atividades do Conselho, enquanto o autuado sustenta que somente o CFA poderia julgá-lo. Qual encaminhamento compatibiliza o Regulamento de Fiscalização e o Regimento do CRA-PR?

A) Manter o processo no CRA-PR, submeter a primeira instância ao Plenário e reservar à Diretoria execução e gestão, sem deslocar ao CFA a competência regional.
B) Manter o processo no CRA-PR, mas atribuir o julgamento de primeira instância à Diretoria por ela administrar as atividades, cabendo ao Plenário apenas executar a decisão.
C) Remeter o julgamento inicial ao CFA e permitir que o CRA-PR apenas instrua o processo, porque a função uniformizadora federal absorve a competência regional originária.
D) Submeter o julgamento à unidade de fiscalização e reservar ao Plenário eventual revisão, porque o órgão que instrui o processo também exerce a primeira instância decisória.

### Questão 19
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes)

Um profissional assina relatório técnico elaborado por terceiro, embora não tenha orientado, supervisionado nem participado do trabalho. À luz do Código de Ética, a melhor conclusão é:

A) a assinatura é regular se o autor material do relatório tiver dado autorização escrita.
B) o ato torna-se regular quando a pessoa jurídica contratante possui registro ativo no CRA.
C) a irregularidade somente existe se for demonstrado prejuízo econômico ao cliente.
D) a conduta pode configurar infração ética: a assinatura técnica exige participação efetiva.

### Questão 20
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres)

Assinale a alternativa incorreta a respeito do sigilo profissional.

A) O dever alcança informações conhecidas em razão da atividade profissional.
B) A expectativa de vantagem comercial, por si só, autoriza a divulgação de informação confidencial.
C) O sigilo pode conviver com obrigações legais e com atuação fiscalizatória legítima.
D) A justa causa e as hipóteses legais precisam ser consideradas na análise do dever de sigilo.

### Questão 21
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Mapa consolidado das resoluções](semana_01_estudo.md#s1-d4-mapa-rns); [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [Código de Ética e RN 671/2025](semana_01_estudo.md#s1-d4-codigo-etica); [RN 680/2025 — eleições](semana_01_estudo.md#s1-d4-rn-680); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia)

Uma nota de consolidação normativa afirma que: a RN CFA nº 670/2025 substituiu integralmente a RN nº 649/2024; a RN nº 671/2025 apenas complementou a RN nº 640/2024; a RN nº 680/2025 apenas alterou a RN nº 633/2023; e o PERC da RN nº 626/2023 permanece aberto em 2026. Qual revisão corrige integralmente a nota?

A) Toda resolução posterior substitui a anterior sobre tema próximo e, por ser mais recente, pode afastar a lei e o decreto regulamentar.
B) A RN nº 670 preserva a RN nº 649, mas a RN nº 671 convive com a RN nº 640, a RN nº 680 apenas altera a RN nº 633 e o PERC permanece aberto enquanto não houver revogação expressa.
C) A RN nº 671 revoga a RN nº 640 e a RN nº 680 revoga a RN nº 633, mas a RN nº 670 elimina todo o Regulamento de Registro e a ementa da RN nº 626 basta para presumir condições atuais do PERC.
D) A RN nº 649 permanece como base, com o art. 11 alterado pela RN nº 670; as RNs nº 671 e 680 revogam suas antecessoras; e o PERC de 2023 deve ser lido com a RN nº 627, preservados lei e decreto.

### Questão 22
**Nível: Muito difícil**
**Uso:** Aprofundamento
**Referência:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670)

Uma consultoria sediada no Paraná, com CNPJ ativo, oferece habitualmente serviços no campo da Administração. Sustenta que somente o CFA poderia examinar seu registro e fiscalizá-la, pois o Regulamento de Registro é uma norma nacional aprovada por esse órgão. Assinale a análise completa.

A) A atividade pode exigir registro e o CRA-PR pode fiscalizar, mas o pedido registral deve ser decidido originariamente pelo CFA porque ele aprovou o regulamento nacional.
B) O CFA uniformiza a disciplina e o CRA-PR fiscaliza no território, mas o CNPJ ativo dispensa o registro da pessoa jurídica mesmo quando os serviços prestados estão no campo profissional.
C) A atividade pode exigir registro e o CRA-PR pode processá-lo, mas a fiscalização cotidiana cabe ao CFA porque a resolução aplicada tem alcance nacional.
D) A atividade deve ser examinada, o CFA uniformiza a disciplina nacional e o CRA-PR processa o registro e fiscaliza a pessoa jurídica em sua jurisdição.

### Questão 23
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento)

Segundo o Regimento Interno aprovado pela RN CFA nº 651/2024, o CRA-PR possui sede na capital e jurisdição:

A) restrita ao município de Curitiba, com delegação eventual aos demais municípios.
B) em todo o Estado do Paraná.
C) sobre os três estados da Região Sul.
D) nacional, embora a fiscalização ordinária se concentre no Paraná.

### Questão 24
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Conselho profissional × sindicato](semana_01_estudo.md#s1-d4-conselho-sindicato)

Um candidato confunde conselho profissional com sindicato. A correção conceitual adequada é:

A) conselho e sindicato são autarquias voltadas à fiscalização profissional e diferem apenas pela abrangência territorial de sua atuação.
B) o conselho representa interesses trabalhistas coletivos, enquanto o sindicato aplica sanções éticas e mantém o registro profissional.
C) o conselho exerce função pública de registro e fiscalização profissional; o sindicato representa interesses da categoria, possuindo natureza e finalidade distintas.
D) o sindicato integra a estrutura descentralizada do conselho e executa suas resoluções profissionais na representação obrigatória da categoria.

### Questão 25
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [RN 680/2025 — eleições](semana_01_estudo.md#s1-d4-rn-680)

A norma do edital associada ao Regulamento das Eleições do Sistema CFA/CRAs é a:

A) RN CFA nº 546/2018.
B) RN CFA nº 589/2020.
C) RN CFA nº 680/2025.
D) RN CFA nº 651/2024.

### Questão 26
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [Lei 12.514/2011 — contribuições e cobrança](semana_01_estudo.md#s1-d4-lei-12514); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia)

Em 2026, um resumo não oficial anuncia adesão atual ao PERC e reproduz descontos e datas históricos. O autor consultou apenas a ementa da RN CFA nº 626/2023, embora o repositório oficial indique alteração pela RN nº 627/2023. Qual procedimento produz conclusão juridicamente rastreável?

A) Adotar o resumo mais recente e apenas confrontar sua ementa, pois a data do material secundário resolve eventual divergência entre versões.
B) Tratar a RN nº 627 como norma capaz de tornar o programa permanente e de modificar livremente a Lei nº 12.514/2011.
C) Usar a ementa para confirmar objeto, prazos, descontos e abertura atual, porque a consulta à norma alteradora seria apenas complementar.
D) Conferir a fonte oficial, ler as RNs nº 626 e 627 em conjunto e não transportar a adesão de 2023 nem suas condições para 2026 sem nova base oficial.

### Questão 27
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes)

Em fiscalização regular no Paraná, o inscrito ofende a equipe, oculta documentos pertinentes e alega que o direito de defesa autoriza recusa geral. Sustenta também que apenas o CFA poderia apurar os fatos. O processo administrativo acaba de ser instaurado. Assinale a conclusão correta.

A) A defesa não legitima obstrução; o CRA-PR atua em sua jurisdição, e qualquer sanção depende do processo e de decisão administrativa definitiva.
B) O CRA-PR pode aplicar imediatamente a sanção máxima, pois a comprovação material dispensa contraditório e individualização.
C) O direito de defesa torna lícitas a recusa e as ofensas, e a atuação regional depende de autorização individual do CFA.
D) O registro ativo reduz os fatos a irregularidade procedimental sem relevância ética e impede atuação fiscalizatória regional.

### Questão 28
**Nível: Difícil**
**Uso:** Aprofundamento
**Referência:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia)

Ao consolidar o Regulamento de Registro, uma equipe usa apenas o texto original da RN CFA nº 649/2024. Outra afirma que a RN nº 670/2025 revogou integralmente o regulamento e pode afastar requisitos legais por ser posterior. Qual método está correto?

A) Ignorar a RN nº 670 até que todo o texto da RN nº 649 seja republicado em um único documento.
B) Aplicar somente a RN nº 670, pois a alteração de um artigo substitui o regulamento inteiro e prevalece sobre lei e decreto.
C) Aplicar ao art. 11 a redação da RN nº 670, preservar a RN nº 649 no restante e interpretar ambas nos limites da lei e do decreto.
D) Permitir que cada CRA escolha entre a redação original e a alterada conforme a conveniência de sua jurisdição.

### Questão 29
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento)

Na estrutura do CRA-PR descrita no Regimento Interno, o órgão deliberativo superior é:

A) o Plenário.
B) a Ouvidoria, por receber manifestações externas e revisar todas as decisões do conselho.
C) a representação institucional, que substitui os órgãos colegiados nas matérias normativas.
D) a Diretoria Executiva, responsável também pela deliberação plenária em caráter permanente.

### Questão 30
**Nível: Médio**
**Uso:** Aprofundamento
**Referência:** [Diretoria Executiva](semana_01_estudo.md#s1-d4-diretoria)

No desenho regimental do CRA-PR, a Diretoria Executiva está mais diretamente ligada:

A) à execução e à administração das deliberações e atividades do Conselho.
B) ao controle externo de manifestações atribuído à Ouvidoria.
C) à função deliberativa superior reservada ao Plenário.
D) à edição de normas nacionais vinculantes para todos os CRAs.

### Questão 31
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes)

Servidor público inscrito no CRA exerce atividade própria do campo profissional. Por ordem escrita da chefia, assina relatório integralmente preparado por terceiro, sem ter orientado ou supervisionado o trabalho, e afirma que o vínculo funcional exclui o Código de Ética. Qual análise é correta?

A) O regime funcional afasta o Código, porque responsabilidade profissional somente existe no exercício liberal.
B) A ordem escrita transfere à chefia toda responsabilidade e torna regular a assinatura sem participação técnica.
C) O Código aplica-se; a ordem não sana assinatura sem supervisão, e eventual sanção exige processo e decisão definitiva.
D) Somente o empregador público pode examinar a conduta, e o CRA deve aguardar condenação criminal antes de iniciar qualquer apuração.

### Questão 32
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Lei e decreto regulamentar](semana_01_estudo.md#s1-d4-decreto-61934)

Para compreender conjuntamente a base legal e a regulamentação do exercício profissional, o par normativo central é:

A) RN CFA nº 589/2020 e RN CFA nº 671/2025.
B) Lei nº 12.514/2011 e RN CFA nº 626/2023.
C) RN CFA nº 651/2024 e RN CFA nº 680/2025.
D) Lei nº 4.769/1965 e Decreto nº 61.934/1967.

### Questão 33
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres)

Assinale a alternativa incorreta à luz dos deveres éticos estudados.

A) O Código de Ética alcança pessoas físicas e jurídicas, observadas as especificidades aplicáveis.
B) O dever de sigilo admite análise de justa causa e de hipóteses legais.
C) A independência técnica pode ser abandonada sempre que o cliente registrar a ordem por escrito.
D) A atualização cadastral e o aperfeiçoamento profissional integram deveres relevantes.

### Questão 34
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres)

A obrigação de manter endereço e dados cadastrais atualizados perante o Conselho contribui para:

A) substituir a renovação de registro por simples comunicação informal.
B) viabilizar comunicações, fiscalização e controle regular do vínculo profissional.
C) transferir ao CFA toda comunicação destinada ao profissional inscrito no CRA.
D) sanar automaticamente qualquer infração anterior praticada pelo inscrito.

### Questão 35
**Nível: Muito difícil**
**Uso:** Revisão
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt)

Um cliente pede parecer favorável a uma operação e exige que seja retirada uma limitação metodológica relevante. Os cálculos foram produzidos por equipe que o profissional não orientou nem supervisionou, mas o cliente afirma que a defesa de seu interesse legítimo autoriza a omissão e a assinatura. Qual resposta concilia corretamente os deveres envolvidos?

A) Explicitar a limitação, preservar conclusão independente e defender o interesse legítimo, mas assinar os cálculos da equipe mesmo sem tê-los orientado ou supervisionado.
B) Defender o interesse legítimo sem distorcer o parecer, explicitar a limitação, manter independência técnica e não assinar trabalho sem participação, orientação ou supervisão.
C) Não assinar os cálculos sem orientação, preservar conclusão independente e defender o interesse legítimo, mas omitir da versão entregue a limitação registrada internamente.
D) Explicitar a limitação e não assinar o trabalho alheio, mas aceitar a conclusão exigida pelo cliente sempre que ela favorecer um interesse legítimo.

### Questão 36
**Nível: Médio**
**Uso:** Revisão
**Referência:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670)

A RN CFA nº 649/2024 é corretamente identificada, no material, como a norma que:

A) aprova o Regulamento das Eleições do Sistema CFA/CRAs.
B) institui o Programa Especial de Recuperação de Créditos dos CRAs.
C) aprova o Regimento Interno específico do CRA-PR.
D) aprova o Regulamento de Registro de pessoas físicas e jurídicas no Sistema CFA/CRAs.

### Questão 37
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

Uma instrução regional determina que, no Paraná, seja mantida a redação original do art. 11 da RN CFA nº 649/2024 e afirma que a RN nº 670/2025, por ser posterior, teria revogado todo o regulamento e poderia dispensar requisito estabelecido em lei. Qual revisão resolve os três erros?

A) Aplicar a RN nº 670 ao art. 11, preservar o restante da RN nº 649, respeitar lei e decreto e alinhar a execução regional à norma nacional.
B) Reconhecer a alteração parcial, mas preservar a redação original no Paraná porque a autonomia regional permite afastar norma nacional sobre registro.
C) Respeitar a hierarquia legal, porém ignorar a RN nº 670 até que a RN nº 649 seja integralmente republicada pelo CFA.
D) Aplicar a instrução regional por ser específica e a RN nº 670 por ser recente, escolhendo em cada caso a solução mais favorável, ainda que contradiga a lei.

### Questão 38
**Nível: Difícil**
**Uso:** Revisão
**Referência:** [Mapa consolidado das resoluções](semana_01_estudo.md#s1-d4-mapa-rns); [RN 546/2018 — isenção de débitos](semana_01_estudo.md#s1-d4-rn-546); [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [RN 680/2025 — eleições](semana_01_estudo.md#s1-d4-rn-680)

Ao revisar uma tabela normativa, o candidato precisa conferir não apenas o objeto, mas também a relação de alteração ou revogação e o alcance temporal ensinado. Qual linha de consolidação está integralmente correta?

A) RN nº 589 — PERC e revogação das RNs nº 446 e 449; RN nº 626 — fiscalização alterada pela RN nº 627; RN nº 680 — registro e revogação da RN nº 633; RN nº 546 — ética e revogação da RN nº 510.
B) RN nº 589: fiscalização, revoga RNs nº 446 e 449; RN nº 626: PERC alterado pela RN nº 627, com adesão em 2023; RN nº 680: eleições, revoga RN nº 633; RN nº 546: isenção ligada à Lei nº 12.514, revoga RN nº 510.
C) RN nº 589 — eleições; RN nº 626 — PERC permanentemente aberto; RN nº 680 — alteração do Regulamento de Registro; RN nº 546 — fiscalização, sem relação com lei federal.
D) RN nº 589 — fiscalização sem revogações; RN nº 626 — isenção de débitos; RN nº 680 — eleições que apenas complementam a RN nº 633; RN nº 546 — PERC alterado pela RN nº 627.

### Questão 39
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

Uma denúncia relata exercício irregular da profissão em cidade do interior do Paraná. Em regra, a apuração fiscalizatória regional insere-se na competência do:

A) CRA-PR, por exercer registro e fiscalização em sua jurisdição.
B) CFA, porque somente o órgão nacional pode verificar exercício irregular.
C) Plenário do CFA, como instância inicial obrigatória de toda fiscalização municipal.
D) Poder Executivo estadual, pois o CRA não possui função fiscalizatória própria.

### Questão 40
**Nível: Médio**
**Uso:** Revisão
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres)

O dever de aperfeiçoamento profissional deve ser compreendido como:

A) obrigação exclusiva do empregador, sem participação do inscrito.
B) compromisso do profissional com atualização e qualidade responsável de sua atuação.
C) faculdade sem relação com zelo, competência ou responsabilidade técnica.
D) dever que pode ser integralmente delegado ao responsável administrativo da pessoa jurídica.

### Questão 41
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes)

Um profissional detém informação confidencial obtida licitamente. Durante apuração regular, recebe requisição pertinente do CRA e, ao mesmo tempo, ordem do cliente para omitir limitação técnica do parecer e recusar qualquer cooperação sob alegação de sigilo absoluto. Qual solução equilibra corretamente os deveres?

A) Obedecer integralmente ao cliente, porque defender seus interesses transforma o sigilo em impedimento absoluto à fiscalização e autoriza a omissão técnica.
B) Divulgar publicamente todo o conteúdo confidencial, pois a existência de fiscalização elimina qualquer dever de sigilo.
C) Resguardar o sigilo legítimo, atender adequadamente à requisição válida e preservar a independência técnica, expondo a limitação relevante.
D) Destruir os registros e encerrar o contrato sem explicação, pois qualquer tensão entre sigilo e fiscalização afasta os deveres profissionais.

### Questão 42
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

Há prova documental de que uma pessoa jurídica registrada obstruiu fiscalização do CRA-PR. O processo acaba de ser instaurado, não houve contraditório nem individualização das circunstâncias, e propõe-se aplicar desde logo suspensão e multa. Qual análise é integralmente correta?

A) O CRA-PR pode apurar e o Código alcança a pessoa jurídica, mas a sanção exige decisão definitiva e individualização; suspensão e cancelamento não se aplicam a esse sujeito.
B) O CRA-PR pode apurar e suspensão e cancelamento não se aplicam à pessoa jurídica, mas a prova documental permite advertência e multa antes da decisão definitiva.
C) O CRA-PR pode apurar e a sanção exige decisão definitiva e individualização, mas a suspensão pode atingir a pessoa jurídica quando a conduta obstrui fiscalização.
D) O Código alcança a pessoa jurídica e a sanção exige decisão definitiva e individualização, mas a competência originária pelo fato ocorrido no Paraná pertence ao CFA.

### Questão 43
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes)

Duas pessoas físicas respondem, em processos distintos, por condutas enquadradas na mesma infração ética. Uma apresenta circunstâncias potencialmente atenuantes; a outra, circunstâncias potencialmente agravantes. Antes das decisões definitivas, propõe-se aplicar a ambas a mesma sanção máxima apenas porque o enquadramento é igual. Qual método está correto?

A) Aplicar sanção idêntica depois de comprovado o mesmo enquadramento, pois a individualização altera apenas o valor da multa associada.
B) Considerar as diferenças pessoais desde o início, mas executar provisoriamente a sanção antes da decisão definitiva e ajustá-la após eventual recurso.
C) Aguardar as decisões definitivas, mas graduar a sanção apenas pelo dano econômico, sem considerar culpa, gravidade ou demais circunstâncias.
D) Individualizar, em cada processo, a sanção segundo culpa, gravidade e circunstâncias atenuantes ou agravantes, aplicando-a somente após o trânsito em julgado administrativo.

### Questão 44
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia); [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626)

O candidato encontra: uma página oficial da RN nº 649 com documento relacionado à RN nº 670; uma apostila não oficial dizendo que todo o regulamento foi substituído; e uma questão sem prova identificada que anuncia PERC aberto em 2026. Qual procedimento compromete a rastreabilidade e deve ser rejeitado?

A) Confirmar no repositório número, ementa e documentos relacionados e ler a norma-base com a alteradora dentro de seu alcance expresso.
B) Classificar a questão como autoral, separar sua fonte normativa e verificar se a informação temporal sobre o PERC possui base oficial atual.
C) Limitar a conclusão ao objeto confirmado quando a fonte não sustenta prazo ou requisito e respeitar a hierarquia entre lei, decreto e resolução.
D) Presumir origem oficial pelo estilo, adotar a versão mais recente da apostila e transportar condições históricas para 2026 sem validar metadados.

### Questão 45
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589)

Em processo administrativo fiscal decorrente de fato punível ocorrido no Paraná, o fiscalizado sustenta, simultaneamente, que apenas o CFA poderia aplicar sanção e que eventual penalidade profissional afastaria qualquer outra consequência prevista em lei. À luz do Regulamento de Fiscalização estudado, assinale a conclusão correta.

A) O CFA possui competência originária exclusiva para sancionar toda infração ocorrida nas jurisdições regionais, e sua decisão substitui qualquer consequência legal.
B) A competência originária para aplicar sanção é do CRA onde ocorreu o fato punível, e a sanção profissional não afasta a possibilidade de outras penas previstas em lei.
C) O CRA limita-se ao cadastro dos inscritos; toda sanção por exercício profissional irregular depende de decisão judicial prévia.
D) O fiscalizado pode escolher qualquer CRA para julgar o caso, e a primeira sanção aplicada extingue as demais consequências possíveis.

### Questão 46
**Nível: Muito difícil**
**Uso:** Simulado
**Referência:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes)

Uma pessoa jurídica com registro ativo mantém responsável técnico apenas no papel. Empregado não habilitado usa o número desse profissional para assinar documentos, sem orientação ou supervisão. Não houve dano concreto demonstrado, e a empresa invoca esse fato e o cadastro regular contra a fiscalização do CRA-PR. Qual análise é completa?

A) O registro ativo não comprova supervisão e o CRA-PR pode separar os sujeitos, mas a ausência de dano concreto exclui relevância profissional do uso do número e da facilitação.
B) A ausência de dano não impede a apuração regional, mas ela deve restringir-se ao empregado, pois a execução material afasta o exame das condutas do profissional e da empresa.
C) O registro ativo não comprova supervisão; o CRA-PR pode apurar uso do número e facilitação, separando as condutas da empresa, do profissional e do empregado antes de sancionar.
D) O registro ativo e a ausência de dano não encerram a análise, e os sujeitos devem ser separados, mas a origem nacional das normas transfere ao CFA a fiscalização cotidiana no Paraná.

### Questão 47
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia)

O CRA-PR possui autonomia administrativa e jurisdição estadual. Uma instrução regional posterior, porém, adota critério incompatível com norma nacional válida do CFA e determina que as fiscalizações locais ignorem a regra federal até nova deliberação regional. Qual resposta preserva simultaneamente autonomia, jurisdição e unidade normativa?

A) Manter a instrução porque sua posterioridade e especialidade territorial bastam para revogar a norma nacional dentro do Paraná.
B) Rever o ato, executar regionalmente a norma nacional válida e levar eventual divergência aos canais institucionais, sem confundir autonomia com soberania.
C) Paralisar toda fiscalização no Paraná até que o CFA execute pessoalmente cada diligência, pois conflito normativo elimina a competência regional.
D) Autorizar o Plenário ou a Diretoria do CRA-PR a alterar a regra nacional para todos os CRAs, já que o Regional possui personalidade jurídica própria.

### Questão 48
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra)

Uma unidade de atendimento do CRA-PR em Londrina declara possuir jurisdição autônoma sobre o norte do Estado, recusa encaminhar fiscalização em Cascavel por considerá-la fora de sua área e adota critério contrário a norma nacional do CFA. Qual solução reúne corretamente estrutura e competência?

A) Manter sede em Curitiba e jurisdição estadual, tratar a unidade como atendimento descentralizado e aplicar a norma nacional na execução regional.
B) Restringir a atuação do CRA-PR a Curitiba e transferir a fiscalização de Cascavel diretamente ao CFA, porque a sede define a jurisdição.
C) Reconhecer a unidade como novo Conselho regional, limitado ao norte do Paraná e autorizado a criar disciplina própria.
D) Admitir que cada unidade escolha a norma aplicável em sua área, pois a descentralização administrativa divide automaticamente a jurisdição estadual.

### Questão 49
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes)

Um inscrito empresta seu número de registro a pessoa não habilitada, permite que ela assine trabalhos e, depois, deixa de atender notificação válida e recusa documentos pertinentes. Não houve lucro nem dano concreto demonstrado. Qual conclusão é correta?

A) Ausência de lucro e dano elimina a relevância de todas as condutas, restando apenas questão contratual privada.
B) Somente a pessoa não habilitada pode ser examinada, porque o registro regular transfere informalmente a habilitação do inscrito.
C) Facilitação, uso do registro e obstrução devem ser apurados separadamente, mesmo sem lucro ou dano, com processo antes da sanção.
D) O conjunto dos fatos impõe cancelamento automático do registro, sem necessidade de enquadramento, defesa ou decisão administrativa definitiva.

### Questão 50
**Nível: Difícil**
**Uso:** Simulado
**Referência:** [Lei 12.514/2011 — contribuições e cobrança](semana_01_estudo.md#s1-d4-lei-12514); [RN 546/2018 — isenção de débitos](semana_01_estudo.md#s1-d4-rn-546); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia)

Em 2026, instrução regional invoca a Lei nº 12.514/2011 para combinar os critérios de isenção da RN nº 546/2018 com os descontos do PERC e reabrir a adesão prevista na RN nº 626/2023, sem consultar a RN nº 627/2023. Qual análise preserva objeto, cadeia normativa, hierarquia e temporalidade?

A) Distinguir isenção e PERC, ler as RNs nº 626 e 627 e reconhecer a adesão de 2023, mas admitir reabertura regional em 2026 porque a lei autoriza recuperação de créditos.
B) Distinguir a isenção da RN nº 546 do PERC, ler as RNs nº 626 e 627 em conjunto e rejeitar a combinação e a reabertura regional sem nova base oficial aplicável a 2026.
C) Distinguir isenção e PERC e rejeitar a reabertura regional em 2026, mas dispensar a RN nº 627 porque a expiração do período de adesão torna irrelevante a norma alteradora.
D) Ler as RNs nº 626 e 627 e rejeitar a reabertura regional em 2026, mas tratar a RN nº 546 como parte do PERC e aplicar seus critérios de isenção à recuperação de créditos.

## Questões extras de revisão fixa do Dia 4

#### Extra Dia 4.1

**Dia:** 4
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Administração Pública
**Assunto:** Modalidade concurso na Lei nº 14.133/2021
**Nível:** Médio
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Essenciais
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Aprofundamento
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Revisão
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
**Uso:** Simulado
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
**Uso:** Simulado
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
**Uso:** Simulado
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
**Uso:** Simulado
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
**Uso:** Simulado
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
18. A
19. D
20. B
21. D
22. D
23. B
24. C
25. C
26. D
27. A
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
46. C
47. B
48. A
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
- **Uso:** Essenciais.
- **A) está errada:** A sujeição da pessoa jurídica não depende de todos os sócios serem profissionais; considera-se a atividade exercida.
- **B) está correta:** A atividade básica situada no campo profissional pode sujeitar a empresa ao registro e à fiscalização do CRA-PR.
- **C) está errada:** O CFA orienta e normatiza nacionalmente; a atuação ordinária de registro e fiscalização regional cabe ao CRA.
- **D) está errada:** CNPJ e indicação informal de profissional não substituem a verificação das exigências de registro e responsabilidade técnica.
- **Conceito cobrado:** Registro e fiscalização de pessoa jurídica.
- **Pegadinha usada:** Tratar CNPJ ou indicação informal de responsável como substitutos da regularidade profissional.
- **Como pensar para acertar:** Identifique a atividade efetivamente oferecida e, depois, o conselho regional competente.
- **Referência à apostila de estudo:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt).

### Comentário da Questão 2

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está correta:** Permitir uso do próprio registro sem elaboração ou supervisão pode configurar empréstimo de nome ou registro.
- **B) está errada:** Não se trata de simples dado cadastral: o número de registro vincula identidade e responsabilidade profissional.
- **C) está errada:** O consentimento não transforma empréstimo de registro em atuação técnica efetiva.
- **D) está errada:** A dupla assinatura ou o suporte eletrônico não supre a ausência de participação e responsabilidade do inscrito.
- **Conceito cobrado:** Uso indevido do nome ou registro profissional.
- **Pegadinha usada:** Confundir autorização formal ou assinatura eletrônica com atuação técnica real.
- **Como pensar para acertar:** Pergunte quem elaborou, orientou ou supervisionou o trabalho cuja responsabilidade está sendo assumida.
- **Referência à apostila de estudo:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes).

### Comentário da Questão 3

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está correta:** A fiscalização regional da regularidade do exercício profissional integra a finalidade do CRA-PR.
- **B) está errada:** O CRA pode agir no âmbito de sua competência fiscalizatória sem depender de provocação prévia do CFA.
- **C) está errada:** A função nacional do CFA não elimina a competência executiva e fiscalizatória do conselho regional.
- **D) está errada:** O CRA não se limita à cobrança: registro e fiscalização são funções centrais do sistema.
- **Conceito cobrado:** Competência fiscalizatória regional.
- **Pegadinha usada:** Reduzir o CRA a arrecadador ou deslocar toda atuação local para o CFA.
- **Como pensar para acertar:** Associe CFA a orientação nacional e CRA a registro e fiscalização em sua jurisdição.
- **Referência à apostila de estudo:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** A fiscalização local é função típica dos CRAs; o CFA não a executa ordinariamente em cada município.
- **B) está errada:** Norma regional não pode afastar unilateralmente disciplina nacional válida do sistema.
- **C) está correta:** A alternativa apresenta corretamente a distribuição geral: orientação normativa nacional pelo CFA e execução regional pelo CRA.
- **D) está errada:** As competências se articulam, mas as abrangências territoriais não são idênticas.
- **Conceito cobrado:** Distribuição de competências no Sistema CFA/CRAs.
- **Pegadinha usada:** Inverter o papel nacional do CFA e o papel regional dos CRAs.
- **Como pensar para acertar:** Use a dupla ‘normatização nacional / execução regional’ como eixo de comparação.
- **Referência à apostila de estudo:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 5

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está correta:** A RN CFA nº 651/2024 aprova o Regimento Interno do CRA-PR.
- **B) está errada:** O regulamento eleitoral indicado é o aprovado pela RN CFA nº 680/2025.
- **C) está errada:** O PERC está associado à RN CFA nº 626/2023.
- **D) está errada:** O Regulamento de Registro está associado à RN CFA nº 649/2024.
- **Conceito cobrado:** Objeto da RN CFA nº 651/2024.
- **Pegadinha usada:** Trocar os objetos de resoluções próximas no mapa do edital.
- **Como pensar para acertar:** Monte pares fixos entre número, ano e objeto de cada resolução.
- **Referência à apostila de estudo:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento).

### Comentário da Questão 6

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** A RN CFA nº 640/2024 foi sucedida e revogada na consolidação indicada no material.
- **B) está errada:** A RN CFA nº 649/2024 trata do Regulamento de Registro, não do Código de Ética.
- **C) está errada:** A RN CFA nº 651/2024 aprova o Regimento Interno do CRA-PR.
- **D) está correta:** A RN CFA nº 671/2025 aprova o Código de Ética e Disciplina vigente considerado no edital.
- **Conceito cobrado:** Norma vigente do Código de Ética.
- **Pegadinha usada:** Escolher norma anterior ou resolução de objeto diferente apenas pela proximidade numérica.
- **Como pensar para acertar:** Diferencie a norma vigente de eventual resolução anterior mencionada no histórico.
- **Referência à apostila de estudo:** [Código de Ética e RN 671/2025](semana_01_estudo.md#s1-d4-codigo-etica).

### Comentário da Questão 7

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** O sigilo não é absoluto diante de justa causa ou obrigação legal legitimamente configurada.
- **B) está correta:** A regra é preservar a informação, com exame das exceções justificadas previstas no ordenamento.
- **C) está errada:** A inexistência aparente de dano econômico não torna a confidencialidade facultativa.
- **D) está errada:** Dever genérico de confidencialidade de terceiros não autoriza compartilhamento sem necessidade e fundamento.
- **Conceito cobrado:** Dever de sigilo e suas exceções.
- **Pegadinha usada:** Oscilar entre sigilo absoluto e divulgação livre por conveniência.
- **Como pensar para acertar:** Comece pela preservação do sigilo e só depois verifique justa causa ou hipótese legal concreta.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres).

### Comentário da Questão 8

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** Registro ativo não neutraliza deveres de colaboração nem sana comportamento obstrutivo.
- **B) está errada:** O direito de defesa não equivale a autorização para recusa geral e imotivada a diligência regular.
- **C) está errada:** O Código alcança pessoas físicas e jurídicas, observadas as especificidades aplicáveis.
- **D) está correta:** Ocultar documentos pertinentes e criar obstáculos deliberados pode caracterizar obstrução à fiscalização.
- **Conceito cobrado:** Obstrução à fiscalização por pessoa jurídica.
- **Pegadinha usada:** Usar direito de defesa ou registro ativo como imunidade contra fiscalização regular.
- **Como pensar para acertar:** Separe contestação fundamentada de comportamento destinado a impedir a atividade fiscalizatória.
- **Referência à apostila de estudo:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes).

### Comentário da Questão 9

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** Contribuições e cobrança dos conselhos são tema central da Lei nº 12.514/2011, não objeto exclusivo da Lei nº 4.769/1965.
- **B) está errada:** O Regimento Interno atual do CRA-PR foi aprovado pela RN CFA nº 651/2024.
- **C) está correta:** A Lei nº 4.769/1965 é a base legal do exercício profissional de Administração e da organização CFA/CRAs.
- **D) está errada:** A lei profissional não se limita à ética; ela estrutura o exercício da profissão e o sistema.
- **Conceito cobrado:** Função da Lei nº 4.769/1965.
- **Pegadinha usada:** Confundir lei profissional com normas financeiras, regimentais ou exclusivamente éticas.
- **Como pensar para acertar:** Associe a lei de 1965 à base da profissão; depois situe as normas especiais ao redor dela.
- **Referência à apostila de estudo:** [Lei 4.769/1965](semana_01_estudo.md#s1-d4-lei-4769).

### Comentário da Questão 10

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** Decreto regulamentar não pode afastar a lei que lhe dá fundamento.
- **B) está correta:** A relação correta é de lei como base e decreto como regulamentação dentro dos limites legais.
- **C) está errada:** O Decreto nº 61.934/1967 regulamenta a lei profissional, não constitui regimento local autônomo.
- **D) está errada:** O decreto não tem como objeto exclusivo o processo eleitoral do sistema.
- **Conceito cobrado:** Relação entre lei e decreto regulamentar.
- **Pegadinha usada:** Supor que norma posterior e infralegal prevalece automaticamente sobre a lei.
- **Como pensar para acertar:** Em conflito, preserve a hierarquia: o decreto detalha a execução, mas não pode contrariar a lei.
- **Referência à apostila de estudo:** [Decreto 61.934/1967](semana_01_estudo.md#s1-d4-decreto-61934).

### Comentário da Questão 11

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** O CRA-PR não possui atuação nacional nem perde sua autonomia administrativa pela articulação com o CFA.
- **B) está correta:** O Regimento o caracteriza como autarquia de direito público, autônoma e com jurisdição no Paraná.
- **C) está errada:** Não se trata de empresa pública estadual destinada a políticas de emprego.
- **D) está errada:** Conselho profissional não é associação privada facultativa; exerce funções públicas de registro e fiscalização.
- **Conceito cobrado:** Natureza jurídica e jurisdição do CRA-PR.
- **Pegadinha usada:** Confundir autarquia profissional com órgão subordinado, empresa estatal ou associação privada.
- **Como pensar para acertar:** Memorize o conjunto: direito público, autonomia própria e jurisdição estadual.
- **Referência à apostila de estudo:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento).

### Comentário da Questão 12

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** Os registrados não editam por votação direta a orientação normativa geral dos conselhos.
- **B) está errada:** O Plenário do CRA-PR é superior dentro do Conselho Regional, não em toda a federação.
- **C) está errada:** Os CRAs aplicam a disciplina do sistema, mas não substituem isoladamente a competência normativa nacional.
- **D) está correta:** A orientação normativa geral do sistema situa-se na esfera nacional do CFA.
- **Conceito cobrado:** Função normativa nacional do CFA.
- **Pegadinha usada:** Confundir superioridade interna do Plenário regional com competência nacional.
- **Como pensar para acertar:** Observe a abrangência do comando: se destinado a todos os CRAs, a referência é o CFA.
- **Referência à apostila de estudo:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 13

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está correta:** A RN CFA nº 649/2024 aprovou o Regulamento de Registro e a RN CFA nº 670/2025 o alterou.
- **B) está errada:** O regulamento eleitoral indicado no edital está na RN CFA nº 680/2025.
- **C) está errada:** Resoluções administrativas não substituem nem revogam integralmente a lei federal profissional.
- **D) está errada:** O Código de Ética vigente está na RN CFA nº 671/2025.
- **Conceito cobrado:** Regulamento de Registro e norma alteradora.
- **Pegadinha usada:** Ler a resolução alteradora isoladamente ou trocar seu objeto com ética e eleições.
- **Como pensar para acertar:** Estude a norma-base e a norma alteradora como um conjunto, preservando a hierarquia.
- **Referência à apostila de estudo:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670).

### Comentário da Questão 14

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** O Regimento Interno do CRA-PR está associado à RN CFA nº 651/2024.
- **B) está errada:** As eleições do sistema são objeto da RN CFA nº 680/2025.
- **C) está correta:** A RN CFA nº 589/2020 está vinculada à fiscalização no Sistema CFA/CRAs.
- **D) está errada:** O Código de Ética vigente está associado à RN CFA nº 671/2025.
- **Conceito cobrado:** Objeto da RN CFA nº 589/2020.
- **Pegadinha usada:** Permutar objetos entre resoluções listadas no mesmo edital.
- **Como pensar para acertar:** Fixe a associação ‘589/2020 — fiscalização’ sem inventar detalhes não consolidados.
- **Referência à apostila de estudo:** [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589).

### Comentário da Questão 15

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **A) está errada:** O funcionamento interno do CRA-PR é disciplinado por seu Regimento, aprovado pela RN CFA nº 651/2024.
- **B) está errada:** O Regulamento de Registro foi aprovado pela RN CFA nº 649/2024.
- **C) está correta:** A ementa da RN CFA nº 626/2023 a relaciona ao Programa Especial de Recuperação de Créditos — PERC.
- **D) está errada:** O Código de Ética vigente foi aprovado pela RN CFA nº 671/2025.
- **Conceito cobrado:** Objeto da RN CFA nº 626/2023.
- **Pegadinha usada:** Confundir recuperação de créditos com registro, ética ou regimento.
- **Como pensar para acertar:** Associe a sigla PERC a recuperação de créditos e ao número 626/2023.
- **Referência à apostila de estudo:** [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626).

### Comentário da Questão 16

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está errada:** O Código de Ética vigente foi aprovado pela RN CFA nº 671/2025.
- **B) está errada:** O PERC está associado à RN CFA nº 626/2023.
- **C) está errada:** A alteração do Regulamento de Registro é objeto da RN CFA nº 670/2025.
- **D) está correta:** A RN CFA nº 546/2018 trata da concessão de isenção de débitos pelos CRAs.
- **Conceito cobrado:** Objeto da RN CFA nº 546/2018.
- **Pegadinha usada:** Aproximar indevidamente ‘isenção de débitos’ e ‘recuperação de créditos’.
- **Como pensar para acertar:** Diferencie benefício de isenção, ligado à RN 546, do programa de recuperação, ligado à RN 626.
- **Referência à apostila de estudo:** [RN 546/2018 — isenção de débitos](semana_01_estudo.md#s1-d4-rn-546).

### Comentário da Questão 17

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está correta:** A Lei nº 12.514/2011 disciplina contribuições devidas a conselhos profissionais e aspectos de cobrança.
- **B) está errada:** Os campos da profissão decorrem da legislação profissional iniciada pela Lei nº 4.769/1965.
- **C) está errada:** A estrutura interna do CRA-PR está em seu Regimento, aprovado pela RN CFA nº 651/2024.
- **D) está errada:** Deveres éticos e sigilo são disciplinados pelo Código de Ética, não constituem o objeto principal da Lei nº 12.514/2011.
- **Conceito cobrado:** Contribuições aos conselhos profissionais.
- **Pegadinha usada:** Trocar o objeto financeiro da Lei nº 12.514/2011 por ética, profissão ou regimento.
- **Como pensar para acertar:** Associe ‘12.514’ a anuidades, contribuições, taxas e cobrança dos conselhos.
- **Referência à apostila de estudo:** [Lei 12.514/2011 — contribuições e cobrança](semana_01_estudo.md#s1-d4-lei-12514).

### Comentário da Questão 18

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **A) está correta:** O fato permanece na competência regional originária, o Plenário exerce a primeira instância de julgamento e a Diretoria conserva suas funções executivas e administrativas.
- **B) está errada:** Administrar as atividades do Conselho não transfere à Diretoria a primeira instância reservada ao Plenário nem reduz este a executor de decisão alheia.
- **C) está errada:** A função nacional e uniformizadora do CFA não absorve o julgamento originário do fato ocorrido na jurisdição do CRA-PR.
- **D) está errada:** A unidade de fiscalização instrui o processo, mas não substitui o Plenário como primeira instância decisória.
- **Conceito cobrado:** Distribuição de funções entre fiscalização, Plenário, Diretoria Executiva, CRA-PR e CFA.
- **Pegadinha usada:** Confundir gestão administrativa ou instrução processual com competência para julgar em primeira instância.
- **Como pensar para acertar:** Separe `quem instrui → quem julga em primeira instância → quem executa e administra → qual órgão possui competência territorial`.
- **Referência à apostila de estudo:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento); [Diretoria Executiva](semana_01_estudo.md#s1-d4-diretoria); [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 19

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está errada:** Autorização do autor material não cria participação técnica do profissional que assina.
- **B) está errada:** O registro da empresa não substitui a responsabilidade efetiva de quem subscreve o documento técnico.
- **C) está errada:** Prejuízo econômico concreto não é condição necessária para reconhecer o desvalor ético da assinatura fictícia.
- **D) está correta:** Assinar sem orientar, supervisionar ou participar pode configurar infração, pois atribui responsabilidade sem atuação real.
- **Conceito cobrado:** Assinatura técnica sem participação efetiva.
- **Pegadinha usada:** Confundir autorização formal ou registro da empresa com supervisão real.
- **Como pensar para acertar:** Compare a responsabilidade declarada pela assinatura com a atuação efetivamente realizada.
- **Referência à apostila de estudo:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes).

### Comentário da Questão 20

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não é a resposta:** A afirmação descreve corretamente a origem funcional do dever de sigilo.
- **B) é a resposta:** A afirmação está incorreta, pois interesse comercial não é justa causa automática e não autoriza divulgar informação confidencial.
- **C) não é a resposta:** A afirmação está correta: preservar sigilo não impede o cumprimento de obrigação legal ou colaboração com fiscalização legítima.
- **D) não é a resposta:** A afirmação está correta: o material admite análise de justa causa e das hipóteses legais pertinentes.
- **Conceito cobrado:** Limites do sigilo profissional.
- **Pegadinha usada:** Transformar conveniência econômica em exceção legítima ao sigilo.
- **Como pensar para acertar:** Nos itens ‘incorreta’, marque a opção que converte interesse privado em autorização geral de divulgação.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres).

### Comentário da Questão 21

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **Uso:** Aprofundamento.
- **A) está errada:** Posterioridade não produz substituição automática nem permite a resolução afastar lei ou decreto; é preciso identificar o alcance expresso de cada ato.
- **B) está errada:** A RN nº 671 revoga a RN nº 640, a RN nº 680 revoga a RN nº 633 e a existência do ato de 2023 não mantém adesão indefinidamente aberta.
- **C) está errada:** Apesar de acertar duas revogações, transforma alteração específica do art. 11 em revogação total e usa ementa histórica para inventar condições atuais.
- **D) está correta:** A alternativa reconstrói corretamente norma-base, alteração parcial, duas revogações expressas, relação entre RN nº 626 e RN nº 627 e limite temporal do PERC, sem romper a hierarquia.
- **Conceito cobrado:** Consolidação simultânea de normas-base, alterações, revogações, temporalidade e hierarquia.
- **Pegadinha usada:** Considerar que toda norma posterior revoga integralmente a anterior ou que vigência formal equivale a programa permanentemente aberto.
- **Como pensar para acertar:** Para cada número, registre `objeto → relação com outra norma → efeito temporal`; só depois confira a hierarquia comum a todas.
- **Referência à apostila de estudo:** [Mapa consolidado das resoluções](semana_01_estudo.md#s1-d4-mapa-rns); [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [Código de Ética e RN 671/2025](semana_01_estudo.md#s1-d4-codigo-etica); [RN 680/2025 — eleições](semana_01_estudo.md#s1-d4-rn-680); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia).

### Comentário da Questão 22

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **Uso:** Aprofundamento.
- **A) está errada:** Acerta a possível incidência do registro e a fiscalização territorial, mas a aprovação da norma nacional não desloca ao CFA a decisão originária do pedido registral.
- **B) está errada:** Acerta a uniformização nacional e a execução regional, mas o CNPJ ativo não dispensa registro quando a atividade efetivamente exercida o exige.
- **C) está errada:** Acerta a análise da atividade e o processamento regional do registro, mas atribui indevidamente ao CFA a fiscalização cotidiana no Paraná.
- **D) está correta:** A alternativa percorre atividade, incidência registral, função uniformizadora do CFA e execução do registro e da fiscalização pelo CRA-PR.
- **Conceito cobrado:** Relação entre atividade da pessoa jurídica, regulamento nacional, registro e fiscalização territorial.
- **Pegadinha usada:** Acertar três camadas e deslocar apenas a decisão registral, a incidência sobre a pessoa jurídica ou a fiscalização para o órgão errado.
- **Como pensar para acertar:** Resolva em quatro filtros: `atividade → necessidade de registro → quem uniformiza → quem registra e fiscaliza no território`.
- **Referência à apostila de estudo:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670).

### Comentário da Questão 23

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está errada:** A sede fica na capital, mas a jurisdição não se limita ao município.
- **B) está correta:** O Regimento atribui ao CRA-PR jurisdição em todo o Estado do Paraná.
- **C) está errada:** A jurisdição não abrange automaticamente Santa Catarina e Rio Grande do Sul.
- **D) está errada:** O CRA-PR não possui jurisdição nacional.
- **Conceito cobrado:** Sede e jurisdição territorial do CRA-PR.
- **Pegadinha usada:** Confundir o local da sede administrativa com o limite territorial da competência.
- **Como pensar para acertar:** Leia as duas informações separadamente: sede na capital; jurisdição em todo o estado.
- **Referência à apostila de estudo:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento).

### Comentário da Questão 24

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está errada:** Sindicato não é autarquia nem exerce fiscalização profissional; a diferença entre as entidades não é apenas territorial.
- **B) está errada:** A alternativa inverte as funções típicas das duas entidades.
- **C) está correta:** Conselho e sindicato têm natureza e finalidade distintas: fiscalização pública de um lado, representação da categoria de outro.
- **D) está errada:** Não há relação de unidade administrativa ou subordinação entre as entidades, e o sindicato não executa resoluções do conselho.
- **Conceito cobrado:** Distinção entre conselho profissional e sindicato.
- **Pegadinha usada:** Atribuir ao conselho defesa corporativa ou ao sindicato poder de polícia profissional.
- **Como pensar para acertar:** Pergunte se a função descrita protege a sociedade pela fiscalização ou representa interesses trabalhistas da categoria.
- **Referência à apostila de estudo:** [Conselho profissional × sindicato](semana_01_estudo.md#s1-d4-conselho-sindicato).

### Comentário da Questão 25

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está errada:** A RN 546/2018 trata de isenção de débitos.
- **B) está errada:** A RN 589/2020 está associada à fiscalização.
- **C) está correta:** A RN 680/2025 aprova o Regulamento das Eleições do Sistema CFA/CRAs.
- **D) está errada:** A RN 651/2024 aprova o Regimento Interno do CRA-PR.
- **Conceito cobrado:** Objeto da RN CFA nº 680/2025.
- **Pegadinha usada:** Confundir eleições com regimento ou fiscalização por proximidade no edital.
- **Como pensar para acertar:** Fixe o par ‘680/2025 — eleições’ e descarte as resoluções com objeto já conhecido.
- **Referência à apostila de estudo:** [RN 680/2025 — eleições](semana_01_estudo.md#s1-d4-rn-680).

### Comentário da Questão 26

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **A) está errada:** Data recente de material secundário não substitui a validação do ato e de seus documentos relacionados no repositório oficial.
- **B) está errada:** A RN nº 627 altera ato administrativo específico; não torna o PERC permanente nem modifica livremente a lei que fornece a base geral.
- **C) está errada:** A ementa confirma o objeto, mas não sustenta sozinha prazo, desconto ou abertura atual do programa.
- **D) está correta:** A solução lê norma-base e alteradora, respeita o recorte temporal confirmado e evita transportar condições históricas para 2026.
- **Conceito cobrado:** Proveniência, cadeia de alteração e temporalidade de programa de recuperação de créditos.
- **Pegadinha usada:** Confundir texto ainda consultável com benefício permanentemente aberto ou transformar ementa em regulamento completo.
- **Como pensar para acertar:** Confirme `fonte → norma relacionada → período alcançado`; se faltar base atual, não conclua prazo ou condição vigente.
- **Referência à apostila de estudo:** [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [Lei 12.514/2011 — contribuições e cobrança](semana_01_estudo.md#s1-d4-lei-12514); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia).

### Comentário da Questão 27

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **A) está correta:** A resposta distingue defesa legítima de obstrução, identifica o órgão territorial e preserva o estágio processual antes de qualquer consequência.
- **B) está errada:** Competência regional não autoriza sanção imediata; contraditório, decisão definitiva e individualização continuam necessários.
- **C) está errada:** Direito de defesa não abrange ofensa ou obstrução, e o CRA-PR não depende de autorização individual do CFA para fiscalizar sua jurisdição.
- **D) está errada:** Registro ativo não neutraliza deveres éticos nem converte o CRA em órgão meramente cadastral.
- **Conceito cobrado:** Articulação entre fiscalização regional, infrações éticas e devido processo administrativo.
- **Pegadinha usada:** Escolher entre dois extremos: imunidade total em nome da defesa ou punição imediata em nome da fiscalização.
- **Como pensar para acertar:** Verifique em ordem `regularidade da diligência → natureza da resistência → órgão territorial → estágio do processo`.
- **Referência à apostila de estudo:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes).

### Comentário da Questão 28

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **A) está errada:** A alteração expressa não depende de republicação integral da norma-base para ser considerada na consolidação.
- **B) está errada:** A RN nº 670 altera especificamente o art. 11; não substitui todo o regulamento nem supera lei e decreto.
- **C) está correta:** A solução combina corretamente alcance da alteração, preservação da norma-base e posição hierárquica dos atos administrativos.
- **D) está errada:** O CRA executa regionalmente a disciplina vigente, mas não escolhe livremente entre redações nacionais conflitantes.
- **Conceito cobrado:** Consolidação de alteração parcial com controle de hierarquia e competência.
- **Pegadinha usada:** Trocar alteração pontual por revogação integral ou autonomia executiva por liberdade normativa.
- **Como pensar para acertar:** Localize o dispositivo alterado, substitua somente sua redação e teste o resultado contra a lei e o decreto.
- **Referência à apostila de estudo:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia).

### Comentário da Questão 29

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está correta:** O Plenário é o órgão deliberativo superior na estrutura regimental.
- **B) está errada:** A Ouvidoria recebe e trata manifestações, sem assumir a posição do Plenário.
- **C) está errada:** Representação institucional não equivale a órgão deliberativo superior.
- **D) está errada:** A Diretoria Executiva cumpre funções de execução e administração, não substitui o órgão deliberativo superior.
- **Conceito cobrado:** Estrutura interna do CRA-PR.
- **Pegadinha usada:** Confundir órgão executivo, canal de ouvidoria ou representação com instância deliberativa superior.
- **Como pensar para acertar:** Associe ‘deliberativo superior’ ao Plenário e ‘execução/administração’ à Diretoria.
- **Referência à apostila de estudo:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento).

### Comentário da Questão 30

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **A) está correta:** A Diretoria Executiva se relaciona à execução e à administração das atividades e deliberações.
- **B) está errada:** A Ouvidoria possui finalidade própria de interlocução e tratamento de manifestações.
- **C) está errada:** A deliberação superior compete ao Plenário.
- **D) está errada:** Normas nacionais para todo o sistema situam-se na esfera do CFA, não da Diretoria regional.
- **Conceito cobrado:** Função da Diretoria Executiva.
- **Pegadinha usada:** Inverter as funções do Plenário, da Diretoria e da Ouvidoria.
- **Como pensar para acertar:** Observe o verbo nuclear: deliberar remete ao Plenário; executar e administrar, à Diretoria.
- **Referência à apostila de estudo:** [Diretoria Executiva](semana_01_estudo.md#s1-d4-diretoria).

### Comentário da Questão 31

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **A) está errada:** O Código alcança o servidor quando ele exerce atividade pertencente ao campo profissional; o tipo de vínculo não cria imunidade.
- **B) está errada:** Ordem escrita não transfere integralmente responsabilidade nem torna legítima assinatura sem orientação ou supervisão.
- **C) está correta:** A alternativa integra incidência do Código, possível infração pela assinatura sem supervisão e necessidade de processo para definir consequência.
- **D) está errada:** A atuação do CRA não depende de condenação criminal nem é excluída pela competência disciplinar do empregador.
- **Conceito cobrado:** Responsabilidade ética do servidor e assinatura de trabalho sem supervisão.
- **Pegadinha usada:** Tratar ordem hierárquica ou regime funcional como causa automática de exclusão da responsabilidade profissional.
- **Como pensar para acertar:** Separe o vínculo de trabalho da natureza técnica do ato e pergunte se houve participação, orientação ou supervisão real.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes).

### Comentário da Questão 32

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Revisão.
- **A) está errada:** RN 589 e RN 671 tratam de fiscalização e ética.
- **B) está errada:** Lei 12.514 e RN 626 tratam de contribuições e recuperação de créditos, não formam o par profissão/regulamentação.
- **C) está errada:** RN 651 e RN 680 tratam, respectivamente, de regimento e eleições.
- **D) está correta:** A Lei 4.769/1965 fornece a base e o Decreto 61.934/1967 a regulamenta.
- **Conceito cobrado:** Base legal e regulamentar da profissão.
- **Pegadinha usada:** Formar pares apenas porque as duas normas constam do edital.
- **Como pensar para acertar:** Procure a relação hierárquica direta: lei profissional seguida de seu decreto regulamentador.
- **Referência à apostila de estudo:** [Lei e decreto regulamentar](semana_01_estudo.md#s1-d4-decreto-61934).

### Comentário da Questão 33

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não é a resposta:** A afirmação está correta: a abrangência inclui PF e PJ, com adaptações e especificidades.
- **B) não é a resposta:** A afirmação está correta: o sigilo deve ser conjugado com justa causa e hipóteses legais.
- **C) é a resposta:** A afirmação está incorreta, pois ordem escrita do cliente não elimina independência técnica nem torna lícita uma conduta inadequada.
- **D) não é a resposta:** A afirmação está correta: atualização cadastral e aperfeiçoamento integram os deveres destacados no material.
- **Conceito cobrado:** Deveres éticos e independência técnica.
- **Pegadinha usada:** Supor que ordem contratual escrita afasta responsabilidade pessoal do profissional.
- **Como pensar para acertar:** Nos itens ‘incorreta’, desconfie de permissões absolutas criadas pela vontade do cliente.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres).

### Comentário da Questão 34

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **A) está errada:** Atualização cadastral não substitui procedimentos de registro eventualmente exigidos.
- **B) está correta:** Dados atualizados permitem notificação, controle e fiscalização regulares.
- **C) está errada:** A obrigação se cumpre perante o conselho competente; não transfere toda comunicação ao CFA.
- **D) está errada:** A correção cadastral não apaga nem sana automaticamente infrações anteriores.
- **Conceito cobrado:** Dever de atualização cadastral.
- **Pegadinha usada:** Transformar um dever instrumental em mecanismo de renovação, transferência de competência ou anistia.
- **Como pensar para acertar:** Pense na finalidade prática do cadastro: localizar, comunicar e controlar o vínculo profissional.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres).

### Comentário da Questão 35

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Uso:** Revisão.
- **A) está errada:** Preserva interesse, integridade e independência, mas admite assinatura sem participação, orientação ou supervisão do trabalho técnico.
- **B) está correta:** A alternativa compatibiliza interesse legítimo do cliente, integridade do parecer, independência técnica e responsabilidade pela autoria ou supervisão.
- **C) está errada:** Preserva autoria e independência, mas registrar internamente a limitação não corrige sua omissão na versão entregue ao destinatário.
- **D) está errada:** Preserva a limitação e a autoria responsável, mas subordina a conclusão técnica ao resultado desejado pelo cliente.
- **Conceito cobrado:** Conciliação entre interesse legítimo, integridade, independência técnica e responsabilidade pela assinatura.
- **Pegadinha usada:** Oferecer três deveres corretamente atendidos e violar apenas o quarto, exigindo a conferência integral da alternativa.
- **Como pensar para acertar:** Teste cada opção em quatro filtros: `interesse legítimo sem distorção → limitação explícita → independência → participação ou supervisão real`.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt).

### Comentário da Questão 36

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Revisão.
- **A) está errada:** O regulamento eleitoral está na RN 680/2025.
- **B) está errada:** O PERC está associado à RN 626/2023.
- **C) está errada:** O Regimento Interno do CRA-PR está na RN 651/2024.
- **D) está correta:** A RN 649/2024 aprova o Regulamento de Registro de PF e PJ no sistema.
- **Conceito cobrado:** Objeto da RN CFA nº 649/2024.
- **Pegadinha usada:** Trocar a norma de registro por resoluções de crédito, regimento ou eleição.
- **Como pensar para acertar:** No mapa normativo, leia ‘649’ como norma-base de registro e ‘670’ como sua alteração.
- **Referência à apostila de estudo:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670).

### Comentário da Questão 37

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **A) está correta:** A alternativa corrige simultaneamente o alcance parcial da RN nº 670, a preservação da norma-base, a hierarquia e o dever de alinhamento da execução regional.
- **B) está errada:** Autonomia regional não autoriza manter redação nacional superada por alteração válida do CFA.
- **C) está errada:** A republicação integral não é condição para considerar a nova redação expressamente dada ao art. 11.
- **D) está errada:** Especificidade territorial e posterioridade não legitimam ato regional ou resolução que contradiga norma superior.
- **Conceito cobrado:** Alteração parcial, hierarquia e distribuição normativa entre CFA e CRA.
- **Pegadinha usada:** Resolver apenas um dos três conflitos e deixar outro erro intacto, sobretudo confundindo autonomia com soberania.
- **Como pensar para acertar:** Teste cada ato em três eixos: `o que foi alterado → qual norma é superior → quem pode uniformizar nacionalmente`.
- **Referência à apostila de estudo:** [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 38

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **A) está errada:** A alternativa troca os objetos de RN nº 589 e RN nº 626 e ainda atribui registro e ética às normas erradas.
- **B) está correta:** Os quatro objetos, as revogações, a alteração da RN nº 626 e o limite temporal do PERC coincidem com o mapa consolidado.
- **C) está errada:** Além de deslocar objetos, apresenta como permanente programa cuja adesão ensinada foi temporal em 2023.
- **D) está errada:** Omite revogações expressas e cruza PERC, isenção e alteração normativa entre números diferentes.
- **Conceito cobrado:** Reconstrução de objetos, alterações, revogações e temporalidade no mapa de resoluções.
- **Pegadinha usada:** Oferecer números e temas verdadeiros, mas montar uma cadeia em que apenas uma relação oculta está trocada.
- **Como pensar para acertar:** Não valide apenas o objeto; confira para cada linha `objeto + norma relacionada + efeito temporal`.
- **Referência à apostila de estudo:** [Mapa consolidado das resoluções](semana_01_estudo.md#s1-d4-mapa-rns); [RN 546/2018 — isenção de débitos](semana_01_estudo.md#s1-d4-rn-546); [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [RN 680/2025 — eleições](semana_01_estudo.md#s1-d4-rn-680).

### Comentário da Questão 39

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **A) está correta:** O fato ocorrido no Paraná insere-se, em regra, na jurisdição fiscalizatória do CRA-PR.
- **B) está errada:** A função nacional do CFA não elimina a atuação fiscalizatória regional.
- **C) está errada:** O Plenário do CFA não é instância inicial obrigatória de toda ocorrência municipal.
- **D) está errada:** O CRA exerce função pública de fiscalização profissional própria.
- **Conceito cobrado:** Competência territorial de fiscalização.
- **Pegadinha usada:** Confundir orientação nacional com execução direta de toda fiscalização local.
- **Como pensar para acertar:** Localize o fato e associe-o ao CRA da respectiva jurisdição.
- **Referência à apostila de estudo:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 40

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **A) está errada:** O empregador pode apoiar a capacitação, mas isso não elimina o dever do profissional.
- **B) está correta:** Aperfeiçoamento é dever ligado à competência, ao zelo e à qualidade responsável.
- **C) está errada:** O Código trata atualização como relevante para a atuação responsável, não como faculdade desconectada.
- **D) está errada:** O profissional não transfere integralmente a terceiro seu dever pessoal de qualificação.
- **Conceito cobrado:** Aperfeiçoamento e atualização profissional.
- **Pegadinha usada:** Externalizar o dever ao empregador ou tratá-lo como opção sem efeito ético.
- **Como pensar para acertar:** Relacione atualização contínua com a qualidade e a responsabilidade dos serviços prestados.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres).

### Comentário da Questão 41

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **A) está errada:** Defender interesses legítimos não transforma sigilo em salvo-conduto para omitir limitação ou impedir fiscalização regular.
- **B) está errada:** Fiscalização não elimina o sigilo nem autoriza divulgação pública indiscriminada de toda informação do cliente.
- **C) está correta:** A solução preserva confidencialidade legítima, cooperação juridicamente cabível e independência técnica, sem absolutizar qualquer dever.
- **D) está errada:** Destruição de registros e encerramento sem esclarecimento não resolvem o conflito e ainda impedem tratamento responsável das obrigações.
- **Conceito cobrado:** Compatibilização entre sigilo, fiscalização e independência técnica.
- **Pegadinha usada:** Escolher um dever verdadeiro e tratá-lo como absoluto, sacrificando todos os demais.
- **Como pensar para acertar:** Pergunte separadamente `o que deve permanecer confidencial`, `o que a requisição válida alcança` e `o que a integridade técnica exige`.
- **Referência à apostila de estudo:** [Abrangência e deveres éticos](semana_01_estudo.md#s1-d4-etica-abrangencia-deveres); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes).

### Comentário da Questão 42

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **A) está correta:** A alternativa identifica competência regional, incidência do Código, etapa processual, individualização e sanções incompatíveis com a pessoa jurídica.
- **B) está errada:** Acerta sujeito, competência e limite sancionatório, mas a robustez da prova não permite advertência ou multa antes da decisão administrativa definitiva.
- **C) está errada:** Acerta competência, processo e individualização, mas suspensão e cancelamento não se aplicam à pessoa jurídica.
- **D) está errada:** Acerta incidência, processo e individualização, mas a competência originária pelo fato ocorrido no Paraná é regional.
- **Conceito cobrado:** Matriz completa de sanção: órgão, sujeito, processo, gradação e limite material.
- **Pegadinha usada:** Acertar quase toda a matriz e errar somente a fase de aplicação, a sanção compatível ou o órgão territorial.
- **Como pensar para acertar:** Percorra cinco perguntas: `quem apura`, `quem responde`, `qual fase`, `qual sanção é admitida` e `quais circunstâncias foram provadas`.
- **Referência à apostila de estudo:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 43

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **A) está errada:** O mesmo enquadramento não elimina a individualização, que alcança a sanção e considera elementos além do valor da multa.
- **B) está errada:** Circunstâncias pessoais devem ser examinadas, mas não autorizam executar sanção provisória antes da decisão administrativa definitiva.
- **C) está errada:** Aguardar o processo é necessário, porém a gradação não se limita ao dano econômico e deve considerar culpa, gravidade e demais circunstâncias.
- **D) está correta:** A sanção deve ser individualizada na decisão de cada processo, mas só pode ser aplicada depois do trânsito em julgado administrativo.
- **Conceito cobrado:** Gradação individual de sanções para condutas com o mesmo enquadramento ético.
- **Pegadinha usada:** Confundir identidade do tipo infracional com identidade obrigatória da sanção ou acertar a individualização e antecipar sua execução.
- **Como pensar para acertar:** Separe `enquadramento → culpa e gravidade → atenuantes e agravantes → sanção individualizada na decisão → aplicação após o trânsito administrativo`.
- **Referência à apostila de estudo:** [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes).

### Comentário da Questão 44

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Observação:** a questão pede o procedimento que compromete a rastreabilidade; portanto, o gabarito é a prática inadequada.
- **A) está errada:** O procedimento é adequado: ele reconstrói a norma vigente a partir de fonte oficial e do alcance da alteração.
- **B) está errada:** Rotular a questão como autoral e exigir base atual para informação temporal preserva proveniência e evita falsa atualização.
- **C) está errada:** Limitar a conclusão ao que a fonte sustenta e respeitar a hierarquia são controles corretos de suficiência.
- **D) está correta:** A alternativa reúne três falhas: falsa origem, escolha de versão sem validação e transporte temporal de condições históricas.
- **Conceito cobrado:** Rastreabilidade conjunta de questão, versão normativa e efeito temporal.
- **Pegadinha usada:** Aceitar aparência de oficialidade, material recente ou texto disponível como substitutos de metadados e cadeia de alterações.
- **Como pensar para acertar:** Faça três auditorias independentes: `de onde veio a questão`, `qual texto normativo está vigente` e `para que período a regra vale`.
- **Referência à apostila de estudo:** [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia); [RNs 649/2024 e 670/2025](semana_01_estudo.md#s1-d4-rn-649-670); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626).

### Comentário da Questão 45

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **A) está errada:** A função nacional do CFA não elimina a competência originária atribuída ao Conselho Regional onde ocorreu o fato punível.
- **B) está correta:** A RN CFA nº 589/2020 atribui a competência originária ao CRA do local do fato e esclarece que as sanções da legislação profissional não afastam outras penas previstas em lei.
- **C) está errada:** Fiscalização e aplicação de sanções administrativas profissionais integram a atuação do CRA e não dependem de condenação judicial prévia.
- **D) está errada:** A competência não fica à livre escolha do fiscalizado, e a sanção profissional não extingue automaticamente outras consequências legais.
- **Conceito cobrado:** Competência sancionadora regional e autonomia das consequências legais.
- **Pegadinha usada:** Transformar a função nacional do CFA em competência originária exclusiva ou tratar a sanção profissional como excludente de todas as demais.
- **Como pensar para acertar:** Localize primeiro onde ocorreu o fato; depois separe a sanção profissional de outras consequências previstas em lei.
- **Referência à apostila de estudo:** [RN 589/2020 — fiscalização](semana_01_estudo.md#s1-d4-rn-589).

### Comentário da Questão 46

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **A) está errada:** Acerta registro, supervisão, competência e separação dos sujeitos, mas uso do número e facilitação não dependem de dano concreto para serem apurados.
- **B) está errada:** Acerta competência e irrelevância da ausência de dano, mas a execução material não afasta o exame das condutas do profissional e da pessoa jurídica.
- **C) está correta:** A alternativa separa registro da organização, supervisão do responsável, habilitação do executor, sujeitos envolvidos, competência regional e fase sancionatória.
- **D) está errada:** Acerta registro, dano e separação dos sujeitos, mas a origem nacional da norma não transfere ao CFA a fiscalização cotidiana no Paraná.
- **Conceito cobrado:** Responsabilidade técnica fictícia integrada a uso de registro, facilitação e fiscalização regional.
- **Pegadinha usada:** Acertar quase todas as camadas e excluir apenas a relevância da conduta, um dos sujeitos ou a competência regional.
- **Como pensar para acertar:** Faça uma matriz `PJ registrada | RT atuou? | executor é habilitado? | quem fiscaliza? | qual fase processual?`.
- **Referência à apostila de estudo:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes).

### Comentário da Questão 47

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **A) está errada:** Ato regional posterior e territorialmente específico não revoga norma nacional quando falta competência para substituí-la.
- **B) está correta:** A solução conserva a execução fiscalizatória regional, a unidade normativa nacional e o canal legítimo para divergência institucional.
- **C) está errada:** Conflito não elimina a competência do CRA-PR nem transfere ao CFA a execução pessoal de cada diligência local.
- **D) está errada:** Personalidade e autonomia do CRA não conferem a seus órgãos poder normativo nacional sobre todos os Regionais.
- **Conceito cobrado:** Autonomia regional, jurisdição executiva e uniformização nacional.
- **Pegadinha usada:** Tratar o conflito como escolha entre soberania regional e centralização completa no CFA, ignorando a distribuição complementar de funções.
- **Como pensar para acertar:** Separe `quem normatiza nacionalmente`, `quem executa no território` e `como a divergência deve ser encaminhada`.
- **Referência à apostila de estudo:** [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra); [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia).

### Comentário da Questão 48

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **A) está correta:** A alternativa resolve os quatro elementos: sede, jurisdição estadual, natureza da unidade descentralizada e submissão da execução à norma nacional.
- **B) está errada:** A sede não limita a jurisdição a Curitiba, e o CFA não substitui o CRA-PR na fiscalização ordinária de Cascavel.
- **C) está errada:** Unidade de atendimento não se converte em Conselho autônomo nem ganha competência para formular disciplina própria.
- **D) está errada:** Descentralização administrativa não fragmenta automaticamente a jurisdição nem autoriza escolha local da norma aplicável.
- **Conceito cobrado:** Estrutura regimental integrada à distribuição CFA × CRA.
- **Pegadinha usada:** Transformar localização física em personalidade, jurisdição ou poder normativo independente.
- **Como pensar para acertar:** Diferencie `onde fica a sede`, `qual território o CRA alcança`, `o que é a unidade` e `quem uniformiza a regra nacional`.
- **Referência à apostila de estudo:** [Regimento do CRA-PR e RN 651/2024](semana_01_estudo.md#s1-d4-regimento); [Competência CFA × CRA](semana_01_estudo.md#s1-d4-cfa-cra).

### Comentário da Questão 49

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **A) está errada:** Lucro ou dano não são requisitos necessários para examinar facilitação, uso indevido e obstrução descritos no caso.
- **B) está errada:** Habilitação não é transferível, e a conduta do inscrito precisa ser analisada separadamente da atuação do terceiro.
- **C) está correta:** A alternativa identifica infrações potencialmente autônomas e, ao mesmo tempo, impede punição automática sem processo.
- **D) está errada:** A gravidade aparente do conjunto não dispensa enquadramento, defesa, decisão definitiva e individualização.
- **Conceito cobrado:** Concurso fático de facilitação, uso do registro e descumprimento da fiscalização.
- **Pegadinha usada:** Exigir resultado econômico para reconhecer infração ou, no extremo oposto, saltar diretamente para cancelamento automático.
- **Como pensar para acertar:** Isole cada verbo do caso — `emprestar`, `permitir`, `não atender`, `recusar` — e depois aplique a regra processual comum.
- **Referência à apostila de estudo:** [Registro, fiscalização e responsabilidade técnica](semana_01_estudo.md#s1-d4-registro-fiscalizacao-rt); [Infrações éticas](semana_01_estudo.md#s1-d4-etica-infracoes); [Sanções, gradação e pessoa jurídica](semana_01_estudo.md#s1-d4-sancoes).

### Comentário da Questão 50

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **A) está errada:** Acerta objeto, cadeia e recorte temporal, mas a autorização legal geral não permite que instrução regional reabra em 2026 programa nacional encerrado.
- **B) está correta:** A solução separa isenção e recuperação, consulta norma-base e alteradora e impede transportar ou combinar condições históricas sem nova base oficial.
- **C) está errada:** Acerta objeto, hierarquia e temporalidade, mas a norma alteradora continua indispensável para reconstruir corretamente a disciplina histórica do PERC.
- **D) está errada:** Acerta a cadeia do PERC e rejeita a reabertura, mas mistura a isenção da RN nº 546 com o objeto e as condições da recuperação de créditos.
- **Conceito cobrado:** Distinção entre isenção e PERC com controle de fonte, alteração normativa, competência e temporalidade.
- **Pegadinha usada:** Acertar quase toda a cadeia e errar apenas a competência para reabrir, a necessidade da norma alteradora ou o objeto da RN nº 546.
- **Como pensar para acertar:** Verifique `objeto de cada RN → norma relacionada → período alcançado → autoridade competente → existência de base oficial atual`.
- **Referência à apostila de estudo:** [Lei 12.514/2011 — contribuições e cobrança](semana_01_estudo.md#s1-d4-lei-12514); [RN 546/2018 — isenção de débitos](semana_01_estudo.md#s1-d4-rn-546); [RN 626/2023 — PERC](semana_01_estudo.md#s1-d4-rn-626); [Proveniência, vigência e hierarquia](semana_01_estudo.md#s1-d4-fontes-hierarquia).

### Comentários das questões extras de revisão fixa do Dia 4

#### Comentário Extra Dia 4.1

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Essenciais.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Aprofundamento.

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

- **Uso:** Revisão.

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

- **Uso:** Revisão.

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não é a resposta:** A afirmação está correta: em ‘àquela’, há fusão da preposição exigida com o demonstrativo.
- **B) é a resposta:** A afirmação está incorreta, pois antes de verbo no infinitivo não ocorre crase: o correto é ‘começou a revisar’.
- **C) não é a resposta:** A afirmação está correta: ‘encaminhado à chefia’ admite preposição e artigo feminino.
- **D) não é a resposta:** A afirmação está correta: na indicação de horário determinado, ‘às 14 horas’ está correto.
- **Conceito cobrado:** Emprego do acento indicativo de crase.
- **Pegadinha usada:** Marcar crase mecanicamente antes de palavra feminina e esquecer que ‘revisar’ é verbo.
- **Como pensar para acertar:** Teste a presença simultânea de preposição ‘a’ e artigo ou demonstrativo compatível.
- **Referência à apostila de estudo:** [Dia 4 — Bloco 5 — Prática discursiva](semana_01_estudo.md#s1-d4-b5).

#### Comentário Extra Dia 4.13

- **Uso:** Revisão.

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

- **Uso:** Revisão.

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

- **Uso:** Revisão.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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

- **Uso:** Simulado.

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

**Base usada:** edital vigente, apostila de estudo v1.3 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões principais

### Questão 1

**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao)

Leia o trecho: “A digitalização de serviços públicos amplia o acesso do cidadão, mas exige mecanismos de segurança para que a eficiência não comprometa direitos.” A ideia central é:

A) A digitalização pode ampliar o acesso, desde que acompanhada de segurança e respeito a direitos.
B) A segurança da informação constitui objetivo independente do acesso e da eficiência dos serviços.
C) A ampliação do acesso só é legítima quando todos os canais presenciais são eliminados.
D) A preservação de direitos necessariamente reduz a eficiência dos serviços digitalizados.

### Questão 2

**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

No trecho “... mas exige mecanismos de segurança”, o conector “mas” estabelece relação de:

A) causa, pois justifica por que a digitalização amplia o acesso.
B) oposição com valor de ressalva, sem anular o benefício mencionado antes.
C) conclusão, pois apresenta uma consequência inevitável da ampliação do acesso.
D) condição, pois substitui a estrutura “desde que” sem alteração sintática.

### Questão 3

**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao)

Leia: “Nem toda inovação tecnológica representa melhoria administrativa.” A inferência logicamente autorizada pelo enunciado é:

A) A maior parte das inovações tecnológicas não produz melhoria administrativa.
B) Existe ao menos uma inovação tecnológica que não representa melhoria administrativa.
C) Nenhuma inovação tecnológica representa melhoria administrativa.
D) Somente inovações desenvolvidas pela própria Administração produzem melhoria.

### Questão 4

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao)

Leia: “A transparência fortalece a confiança social, desde que respeite a proteção de dados pessoais.” Assinale a alternativa que extrapola o texto.

A) A transparência pode contribuir para fortalecer a confiança social.
B) A proteção de dados pessoais funciona como limite a ser observado.
C) A confiança social exige divulgação irrestrita de todo dado pessoal do órgão.
D) Transparência e proteção de dados podem ser compatibilizadas.

### Questão 5

**Nível:** Difícil
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita)

A reescrita que preserva o sentido de “A revisão diária reduz o esquecimento e melhora a retenção do conteúdo” é:

A) Como melhora a retenção, a revisão diária aumenta o esquecimento do conteúdo.
B) O esquecimento é reduzido e a retenção do conteúdo é melhorada pela revisão diária.
C) A revisão diária reduz o conteúdo esquecido, embora prejudique sua retenção.
D) A revisão diária impede qualquer esquecimento e assegura retenção integral do conteúdo.

### Questão 6

**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia)

Assinale a alternativa correta quanto à concordância verbal no padrão formal.

A) Existe, no cadastro, pendências que impedem a emissão da certidão.
B) Falta, nos autos, os comprovantes exigidos pelo edital.
C) Faltam documentos no processo administrativo encaminhado à comissão.
D) Devem haver documentos suficientes para a análise do pedido.

### Questão 7

**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase)

Assinale a alternativa em que o emprego do acento indicativo de crase está correto.

A) A servidora entregou a manifestação à Vossa Senhoria.
B) O candidato começou à revisar o edital após o simulado.
C) O relatório foi encaminhado à diretoria técnica para análise.
D) O servidor retornou à pé ao setor de protocolo.

### Questão 8

**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao)

Assinale a alternativa em que a vírgula foi empregada incorretamente.

A) Após a publicação do edital, os candidatos reorganizaram o cronograma.
B) O CRA-PR, autarquia de fiscalização profissional, divulgou novas orientações.
C) Embora o conteúdo seja extenso, a revisão diária favorece a retenção.
D) Os candidatos que revisaram o edital, identificaram a alteração do prazo.

### Questão 9

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “O sistema é eficiente; contudo, depende de dados atualizados.” Sem alterar a relação entre as orações, “contudo” pode ser substituído por:

A) entretanto.
B) por conseguinte.
C) porquanto.
D) contanto que.

### Questão 10

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase)

Assinale a alternativa correta quanto à regência verbal no padrão formal.

A) O candidato visava o cargo de analista, no sentido de aspirar a ele.
B) O candidato obedeceu ao edital e às orientações da banca.
C) A equipe preferiu revisar o texto do que manter a versão anterior.
D) Os servidores assistiram o treinamento, no sentido de presenciá-lo.

### Questão 11

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “Os dados cadastrais foram conferidos por dois servidores, e esse procedimento reduziu inconsistências.” A expressão “esse procedimento” retoma:

A) uma etapa do trabalho não mencionada no período.
B) a redução das inconsistências identificadas no cadastro.
C) apenas o substantivo “servidores”.
D) a conferência dos dados cadastrais por dois servidores.

### Questão 12

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

No período “Se o planejamento for consistente, a execução será mais segura”, a oração introduzida por “se” expressa:

A) conclusão decorrente de uma premissa já comprovada.
B) concessão diante de um obstáculo insuficiente.
C) oposição entre planejamento e execução.
D) condição para que a execução seja mais segura.

### Questão 13

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos)

Assinale a alternativa em que “há” e “a” foram empregados corretamente.

A) Estudo o conteúdo há três meses, e a prova ocorrerá daqui a vinte dias.
B) A três meses estudo o conteúdo, e a prova será realizada há vinte dias.
C) Há três meses ocorrerá a prova, e o edital saiu a duas semanas.
D) Estudo o conteúdo a três meses, e a prova ocorrerá daqui há vinte dias.

### Questão 14

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Colocação pronominal, ambiguidade e uso de onde](semana_01_estudo.md#s1-d5-colocacao-onde)

Assinale a alternativa em que há ambiguidade de referência pronominal.

A) A equipe revisou seu próprio relatório antes de enviá-lo à diretoria.
B) O analista informou que o relatório elaborado pela equipe estava incompleto.
C) O analista informou ao coordenador que seu relatório estava incompleto.
D) O coordenador recebeu ontem o relatório final elaborado pelo analista.

### Questão 15

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “A medida deve ser mantida, pois reduz riscos operacionais sem restringir o atendimento.” Nesse contexto, “pois” introduz:

A) explicação que justifica a manutenção da medida.
B) ressalva que limita a eficácia atribuída à medida.
C) alternativa que dispensa a manutenção da medida.
D) condição prévia para que os riscos sejam reduzidos.

### Questão 16

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Colocação pronominal, ambiguidade e uso de onde](semana_01_estudo.md#s1-d5-colocacao-onde)

Assinale a alternativa correta quanto à colocação pronominal no padrão formal.

A) Não se deve desconsiderar a retificação publicada pela banca.
B) Me comunicaram o resultado no início da reunião.
C) A comissão tinha comunicado-me a alteração antes da reunião.
D) Não deve-se desconsiderar a retificação publicada pela banca.

### Questão 17

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao)

Assinale a alternativa com pontuação adequada.

A) Curitiba, capital do Paraná sediará o encontro regional em agosto.
B) Curitiba, capital do Paraná, sediará o encontro regional em agosto.
C) Curitiba capital do Paraná, sediará o encontro regional em agosto.
D) Curitiba capital, do Paraná, sediará o encontro regional em agosto.

### Questão 18

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “Apenas os candidatos que revisaram a legislação específica identificaram a exceção normativa.” Considerando o alcance de “apenas”, o período afirma que:

A) os candidatos identificaram somente uma exceção, embora pudessem identificar outras.
B) todos os candidatos revisaram a legislação, mas somente alguns identificaram a exceção.
C) a revisão da legislação foi a única atividade realizada por todos os candidatos.
D) somente candidatos que revisaram a legislação específica integram o grupo que identificou a exceção.

### Questão 19

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia)

Assinale a frase correta quanto à concordância nominal e verbal.

A) Segue anexa ao processo os relatórios solicitados pela comissão.
B) Segue anexos ao processo os documentos solicitados pela comissão.
C) Seguem anexo ao processo as declarações solicitadas pela comissão.
D) Seguem anexos ao processo os documentos solicitados pela comissão.

### Questão 20

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “A política de atendimento foi reformulada para reduzir filas sem excluir usuários com dificuldade de acesso digital.” A oração “para reduzir filas” expressa:

A) consequência imprevista da reformulação.
B) contraste entre a política e o atendimento.
C) finalidade atribuída à reformulação da política.
D) concessão diante de uma dificuldade.

### Questão 21

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Colocação pronominal, ambiguidade e uso de onde](semana_01_estudo.md#s1-d5-colocacao-onde)

Assinale a alternativa em que a palavra “onde” foi empregada de acordo com a norma-padrão.

A) O prédio onde funciona o setor de atendimento passa por reforma.
B) A hipótese onde o prazo seria prorrogado foi rejeitada.
C) O fundamento onde a decisão se apoiou consta do parecer.
D) A conclusão onde a comissão chegou foi registrada no parecer.

### Questão 22

**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Estrutura da discursiva](semana_01_estudo.md#s1-d5-discursiva-estrutura)

Para o tema “digitalização de serviços públicos e proteção de direitos”, qual enunciado funciona melhor como tese de uma dissertação?

A) A digitalização dos serviços públicos avançou nas últimas décadas e integra o cotidiano administrativo.
B) A expansão dos serviços digitais deve combinar ganho de eficiência, canais inclusivos e proteção efetiva dos dados pessoais.
C) De que modo a Administração poderá digitalizar serviços sem produzir novos riscos aos cidadãos?
D) Serão examinados exemplos de plataformas públicas antes de se apresentar, ao final, uma opinião sobre o tema.

### Questão 23

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Estrutura da discursiva](semana_01_estudo.md#s1-d5-discursiva-estrutura)

Leia a introdução: “A tecnologia é importante. Hoje tudo é tecnologia. A tecnologia está em todos os lugares.” O principal problema argumentativo do trecho é:

A) a antecipação de uma proposta de intervenção que deveria aparecer apenas na conclusão.
B) a delimitação excessiva do tema, que impede a inclusão de exemplos no desenvolvimento.
C) a presença de argumento circular, embora haja tese explícita sobre serviços públicos digitais.
D) a generalidade das afirmações e a ausência de uma tese que delimite o ponto de vista.

### Questão 24

**Nível:** Difícil
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Modelo discursivo comentado](semana_01_estudo.md#s1-d5-discursiva-modelo)

Em um desenvolvimento sobre digitalização inclusiva, assinale o trecho que apresenta argumento mais consistente.

A) A digitalização merece atenção por ser tema atual, mas essa atualidade basta para demonstrar sua inclusão.
B) Os serviços digitais funcionam bem quando são eficientes, razão suficiente para sua expansão irrestrita.
C) A digitalização reduz deslocamentos e espera; sem acessibilidade e canais alternativos, porém, pode excluir usuários vulneráveis.
D) A existência de plataformas eletrônicas demonstra acesso equivalente, independentemente das condições dos usuários.

### Questão 25

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Autocorreção da discursiva](semana_01_estudo.md#s1-d5-discursiva-rubrica)

Assinale a frase mais adequada a uma dissertação por combinar registro formal, precisão e objetividade.

A) É absolutamente evidente para qualquer pessoa sensata que os dados públicos exigem bastante cuidado.
B) A meu ver, parece que talvez a transparência possa ajudar um pouco a Administração.
C) A gestão de dados envolve certas coisas importantes, que serão resolvidas conforme for possível.
D) A Administração deve definir finalidade, controle de acesso e prazo de retenção para os dados que trata.

### Questão 26

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase)

Assinale a alternativa em que o acento indicativo de crase foi empregado indevidamente.

A) O servidor começou à analisar o processo após receber a defesa.
B) A informação foi encaminhada à autoridade responsável pela decisão.
C) A comissão fez referência àquela auditoria realizada em maio.
D) A equipe compareceu às reuniões previstas no cronograma.

### Questão 27

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes)

Leia: “Os candidatos que estudaram o edital resolveram melhor as questões.” Sem vírgulas, a oração “que estudaram o edital” permite concluir que:

A) todos os candidatos que não estudaram o edital necessariamente resolveram pior as questões.
B) todos os candidatos estudaram o edital, e a oração apenas acrescenta informação acessória.
C) o estudo do edital é apresentado como causa comprovada e exclusiva do melhor desempenho.
D) a afirmação sobre melhor desempenho se restringe ao subconjunto dos candidatos que estudaram o edital.

### Questão 28

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes)

Leia: “Os candidatos, que estudaram o edital, resolveram melhor as questões.” Considerando apenas a estrutura sintática e a pontuação, a oração entre vírgulas tem valor:

A) restritivo, pois seleciona apenas parte dos candidatos mencionados.
B) condicional, pois subordina o desempenho ao estudo do edital.
C) comparativo, pois confronta dois grupos de candidatos.
D) explicativo, pois acrescenta informação acessória sobre todos os candidatos.

### Questão 29

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita)

Assinale a alternativa que preserva o paralelismo sintático dos termos coordenados.

A) O plano exige a análise de riscos, controlar acessos e a revisão de incidentes.
B) O plano exige ler a teoria, resolver questões e revisar os erros registrados.
C) O plano exige que o candidato leia a teoria, resolver questões e revisão dos erros.
D) O plano exige leitura da teoria, resolver questões e que os erros sejam revistos.

### Questão 30

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao)

Em “A equipe revisou o relatório; o coordenador, a planilha; e a diretora, o parecer”, as vírgulas após “coordenador” e “diretora”:

A) isolam vocativos dirigidos aos responsáveis por cada documento.
B) separam indevidamente os sujeitos dos verbos expressos nas duas orações.
C) assinalam a elipse do verbo “revisou”, recuperável na primeira oração.
D) introduzem apostos que especificam “relatório” e “planilha”.

### Questão 31

**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia)

Assinale a frase correta no padrão formal.

A) Houveram dois anos de testes antes que o sistema fosse implantado.
B) Fazem dois anos que o sistema foi implantado e seis meses que passou pela última revisão.
C) Devem fazer dois anos que o sistema foi implantado e seis meses que passou pela última revisão.
D) Faz dois anos que o sistema foi implantado e seis meses que passou pela última revisão.

### Questão 32

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos)

Assinale a alternativa em que “porquê” está corretamente empregado.

A) O relatório não foi enviado porquê faltava a assinatura da chefia.
B) Ninguém explicou o porquê da alteração realizada no cronograma.
C) A comissão perguntou porque motivo o candidato não apresentou o documento.
D) Porquê o prazo foi alterado sem comunicação aos interessados?

### Questão 33

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “A revisão cruzada detectou inconsistências que a conferência automática não identificara; portanto, o procedimento deve ser mantido.” O termo “portanto” introduz:

A) conclusão sustentada pelo resultado mencionado na oração anterior.
B) condição necessária para que as inconsistências sejam detectadas.
C) concessão que relativiza a utilidade da revisão cruzada.
D) oposição entre a conferência automática e a manutenção do procedimento.

### Questão 34

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes)

No período “As inconsistências foram identificadas pela equipe de auditoria durante a revisão”, a expressão “pela equipe de auditoria” exerce a função de:

A) agente da passiva, pois indica quem praticou a ação verbal.
B) adjunto adnominal que restringe o sentido de “inconsistências”.
C) sujeito paciente, pois recebe a ação de identificar.
D) objeto indireto exigido pelo verbo “identificar”.

### Questão 35

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Assinale a alternativa em que a segunda oração expressa causa da ação indicada na primeira.

A) A equipe reabriu a análise para verificar a autenticidade dos documentos.
B) A equipe reabriu a análise, embora o prazo interno já estivesse encerrado.
C) A equipe reabriu a análise porque surgiram documentos capazes de alterar a decisão.
D) A equipe reabriria a análise, desde que a autoridade prorrogasse o prazo.

### Questão 36

**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes)

Em “A norma publicada em 2025 alterou o procedimento de registro”, o segmento “publicada em 2025” funciona como:

A) oração reduzida adverbial que indica quando ocorreu a alteração do procedimento.
B) predicado principal cujo sujeito está oculto no período.
C) oração reduzida de particípio, com valor adjetivo, que delimita “norma”.
D) complemento nominal exigido pelo substantivo “norma”.

### Questão 37

**Nível:** Difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao)

Assinale a alternativa em que a pontuação está inteiramente adequada.

A) No início da semana, o candidato, conforme o cronograma, revisou arquitetura, sistemas operacionais e banco de dados.
B) No início da semana o candidato, conforme o cronograma, revisou arquitetura sistemas operacionais e banco de dados.
C) No início da semana, o candidato, revisou arquitetura, sistemas operacionais e banco de dados.
D) No início, da semana, o candidato conforme o cronograma revisou, arquitetura, sistemas operacionais e banco de dados.

### Questão 38

**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “A solução não elimina todos os riscos, tampouco dispensa o monitoramento contínuo.” Nesse contexto, “tampouco”:

A) introduz a finalidade de manter o monitoramento.
B) conclui que os riscos persistem por falta de monitoramento.
C) acrescenta uma segunda negação, com sentido equivalente a “também não”.
D) explica a causa de a solução não eliminar todos os riscos.

### Questão 39

**Nível:** Difícil
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 5 — Estrutura da discursiva](semana_01_estudo.md#s1-d5-discursiva-estrutura)

Assinale a alternativa que melhor conclui uma dissertação cuja tese defende transparência compatível com a proteção de dados pessoais.

A) Portanto, deve-se discutir também a aquisição de equipamentos, assunto que não integrou a argumentação desenvolvida.
B) Assim, finalidade definida, acesso controlado e prestação de contas conciliam transparência e proteção de dados.
C) Conclui-se que a publicidade deve prevalecer sempre, mesmo quando expuser dados pessoais sem necessidade.
D) Em síntese, os dois valores são complexos, cabendo a cada órgão decidir livremente qual deles observar.

### Questão 40

**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos)

Assinale a alternativa correta quanto à acentuação gráfica.

A) “Órgão”, “relatório” e “possível” recebem acento pela mesma regra.
B) “Público”, “técnico” e “lógico” são acentuados por serem proparoxítonos.
C) “Lógico” pode perder o acento sem alteração de pronúncia ou de classe gramatical.
D) “Técnico” é acentuado por ser paroxítona terminada em “o”.

### Questão 41

**Nível:** Muito difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita)

Leia: “A comissão confrontou as propostas e registrou as divergências; contudo, não homologou o resultado.” Qual reescrita preserva a adição entre as duas primeiras ações e a oposição introduzida no segmento final, sem criar relação causal inexistente?

A) Como confrontou as propostas, a comissão registrou as divergências; portanto, não homologou o resultado.
B) A comissão ou confrontou as propostas ou registrou as divergências; por isso, não homologou o resultado.
C) Embora confrontasse as propostas, a comissão registrou as divergências e, por essa razão, não homologou o resultado.
D) A comissão confrontou as propostas e registrou as divergências; entretanto, não homologou o resultado.

### Questão 42

**Nível:** Difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase)

Assinale a alternativa em que todas as relações de regência nominal estão adequadas ao padrão formal.

A) O parecer era compatível à norma e contrário o entendimento anterior.
B) O sistema permaneceu acessível aos usuários e passível à auditoria externa.
C) A comissão mostrou-se favorável com o recurso e avessa de nova instrução.
D) O candidato estava apto ao exercício e consciente das responsabilidades.

### Questão 43

**Nível:** Muito difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao)

Um texto informa que 3 de 20 processos atrasaram e que a auditoria não identificou uma causa comum. Em uma questão que pede a alternativa INCORRETA, lê-se: “Alguns processos atrasaram; logo, todos os atrasos decorreram de negligência e exigem a mesma providência.” Qual procedimento conduz ao julgamento correto?

A) considerar a opção correta, porque a primeira oração coincide com um dado expresso no texto-base.
B) testar a proposição inteira, identificar a generalização quantitativa e a causa não demonstrada e, após reler o comando, marcá-la.
C) desconsiderar o trecho após o ponto e vírgula, pois somente a primeira oração participa do valor da alternativa.
D) aceitar a conclusão, porque o conector “logo” transforma qualquer hipótese causal em fato comprovado pelo texto.

### Questão 44

**Nível:** Difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita)

Considere que, no período “O candidato só revisou legislação depois de errar o simulado”, o advérbio “só” incide sobre a circunstância temporal. Assinale a reescrita que altera o sentido original.

A) Somente depois de errar o simulado, o candidato revisou legislação.
B) A revisão de legislação pelo candidato ocorreu apenas após o erro no simulado.
C) Antes de errar o simulado, o candidato já havia revisado legislação.
D) Foi apenas depois do erro no simulado que o candidato revisou legislação.

### Questão 45

**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “Embora dispusesse de orçamento reduzido, a equipe concluiu as etapas essenciais; por isso, a direção manteve o cronograma.” Qual reescrita preserva simultaneamente a concessão do primeiro segmento e a consequência expressa no segundo período?

A) Ainda que tivesse orçamento reduzido, a equipe concluiu as etapas essenciais; consequentemente, a direção manteve o cronograma.
B) Como tinha orçamento reduzido, a equipe concluiu as etapas essenciais; apesar disso, a direção manteve o cronograma.
C) Se tivesse orçamento reduzido, a equipe concluiria as etapas essenciais; entretanto, a direção manteve o cronograma.
D) A equipe concluiu as etapas essenciais porque tinha orçamento reduzido; ainda assim, a direção manteve o cronograma.

### Questão 46

**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia)

Assinale a frase inteiramente correta quanto à concordância no padrão formal.

A) Mais de um setor enviaram o parecer solicitado pela diretoria.
B) Devem haver, nos autos, razões suficientes para rever a decisão.
C) Um ou outro candidatos apresentaram dúvida sobre a retificação.
D) Mais de um candidato apresentou recurso fundamentado contra o resultado.

### Questão 47

**Nível:** Difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “O órgão deve informar a finalidade do tratamento e limitar o acesso aos dados. O cumprimento conjunto **dessas exigências** reduz usos incompatíveis; **a última delas**, porém, não dispensa o registro das operações.” As duas expressões destacadas retomam, respectivamente:

A) apenas o dever de informar; e o conjunto indeterminado de operações futuras.
B) uma obrigação que será anunciada depois; e a redução dos usos incompatíveis.
C) as duas obrigações do primeiro período; e, especificamente, a limitação de acesso aos dados.
D) apenas a finalidade do tratamento; e, especificamente, o dever de informar os titulares.

### Questão 48

**Nível:** Muito difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos)

Complete corretamente o período: “A ___ do edital corrigiu o erro material; depois, a autoridade decidiu ___ os demais termos e recomendou ___ no tratamento dos dados pessoais.”

A) ratificação — retificar — discrição.
B) retificação — ratificar — discrição.
C) ratificação — ratificar — descrição.
D) retificação — retificar — descrição.

### Questão 49

**Nível:** Difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao)

Leia: “A capacitação deve ser contínua, uma vez que a atualização dos sistemas modifica procedimentos e riscos; ainda assim, treinamento isolado não substitui controles técnicos.” Qual par de conectores pode substituir as expressões destacadas sem alterar, respectivamente, a causa e a oposição concessiva?

A) à medida que — portanto.
B) a menos que — por conseguinte.
C) porque — mesmo assim.
D) embora — por essa razão.

### Questão 50

**Nível:** Muito difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Autocorreção da discursiva](semana_01_estudo.md#s1-d5-discursiva-rubrica)

Em relatório administrativo, a redação deve separar fato observado de providência recomendada e fornecer elementos verificáveis. Qual trecho atende conjuntamente a esses critérios, sem apresentar inferência como fato comprovado?

A) Em 12 de maio, o teste registrou falhas nos itens 4, 7 e 9; recomenda-se corrigi-las até 20 de maio e testar novamente.
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
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia)

Sobre a articulação entre as normas centrais da legislação profissional, assinale a alternativa correta.

A) O Regimento Interno pode ampliar, por decisão regional, o campo profissional definido na lei federal.
B) As resoluções do CFA prevalecem sobre a lei e o decreto sempre que forem posteriores.
C) A lei disciplina a profissão; o decreto a regulamenta; atos do Sistema complementam matérias de sua competência.
D) O decreto regulamentador cuida apenas da organização interna do CRA-PR, sem relação com a execução da lei.

#### Extra Dia 5.2

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Uso de título e regularidade do exercício profissional
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao)

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
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao)

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
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade)

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
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao)

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
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade)

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
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia)

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
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 5 — Processo, sanção e controle de fonte](semana_01_estudo.md#s1-d5-processo-sancao)

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
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Processo, sanção e controle de fonte](semana_01_estudo.md#s1-d5-processo-sancao)

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
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia)

Em uma questão sobre a RN CFA nº 651/2024, qual conteúdo deve ser associado diretamente ao Regimento Interno do CRA-PR?

A) Apenas os valores anuais de contribuições e as regras de cobrança judicial.
B) A definição originária do campo privativo da profissão em todo o território nacional.
C) Os deveres éticos e as sanções disciplinares previstos no Código de Ética vigente.
D) A estrutura dos órgãos, as competências internas e o funcionamento do Regional.

#### Extra Dia 5.11

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Pessoa jurídica, responsabilidade ética e compatibilidade de sanções
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade)

Uma pessoa jurídica registrada e seu responsável técnico são apurados por condutas relacionadas ao mesmo serviço. À luz das especificidades ensinadas, assinale a alternativa correta.

A) A pessoa jurídica fica fora do Código de Ética, e somente o responsável técnico pode ser apurado.
B) Ambos podem ser apurados, mas sanções próprias do exercício não se aplicam indistintamente à pessoa jurídica.
C) A sanção escolhida para o responsável técnico deve ser automaticamente reproduzida para a pessoa jurídica.
D) O registro empresarial absorve toda responsabilidade individual e impede a análise da atuação do profissional.

#### Extra Dia 5.12

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Relação entre lei e decreto regulamentador
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia)

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
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao)

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
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia)

Para responder a uma questão que cobre prazo, rito ou sanção específica, a conduta de estudo mais segura é:

A) atribuir a mesma autoridade a comentários de cursos e ao texto publicado pelo órgão competente.
B) adotar o prazo mencionado em um resumo, ainda que diverja da publicação oficial.
C) conferir o texto oficial da norma pertinente e sua vigência, usando o resumo como apoio.
D) aplicar automaticamente a resolução numericamente mais recente, mesmo que o edital indique outra base.

#### Extra Dia 5.15

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Plenário, Diretoria Executiva e distribuição interna de funções
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia)

O Plenário delibera sobre matéria institucional dentro de sua competência, e a Diretoria Executiva conduz a execução administrativa correspondente. A associação correta é:

A) deliberação superior pelo Plenário e execução administrativa pela Diretoria, nos limites do Regimento.
B) deliberação e execução exclusivas da Diretoria, pois o Plenário possui função apenas consultiva.
C) execução pelo Plenário e revisão ética automática pela Diretoria, independentemente da matéria.
D) distribuição livre pelo presidente, porque o Regimento não diferencia órgãos deliberativos e executivos.

#### Extra Dia 5.16

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Indício, contraditório e decisão fundamentada
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Processo, sanção e controle de fonte](semana_01_estudo.md#s1-d5-processo-sancao)

Durante fiscalização, são documentados indícios de irregularidade. Antes da aplicação de consequência sancionadora, a sequência compatível com o material é:

A) tratar o indício como condenação e executar imediatamente a sanção sugerida pelo denunciante.
B) dispensar ciência e defesa quando houver documento produzido por agente de fiscalização.
C) submeter o caso à autoridade competente, com apuração regular, contraditório, defesa e decisão fundamentada.
D) escolher primeiro a sanção mais severa e localizar depois uma norma que possa justificá-la.

#### Extra Dia 5.17

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Jurisdição regional e coordenação nacional em caso concreto
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao)

Uma empresa registrada em outro estado passa a executar, no Paraná, atividade ligada ao campo fiscalizado. Para analisar o fato local, a alternativa correta é:

A) somente o CFA pode verificar a atividade, porque o registro originário torna os Regionais incompetentes.
B) o CRA-PR pode examinar o fato em sua jurisdição, enquanto o CFA mantém coordenação e normatização nacionais.
C) qualquer CRA pode aplicar diretamente medida no Paraná, sem considerar território nem processo.
D) o registro em outro estado regulariza automaticamente toda atividade futura, qualquer que seja o local de execução.

#### Extra Dia 5.18

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Independência técnica diante de pressão hierárquica
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade)

Um superior pressiona o responsável técnico a alterar conclusão de relatório sem novo dado ou fundamento verificável. A conduta compatível com o conteúdo estudado é:

A) preservar a independência técnica, registrar os fundamentos e recusar a validação de informação sem suporte.
B) alterar o relatório, porque a hierarquia administrativa elimina a responsabilidade de quem assina.
C) retirar apenas a identificação do documento e manter a conclusão sem base, evitando responsabilidade ética.
D) atender à ordem e invocar sigilo para impedir qualquer exame posterior pela fiscalização.

#### Extra Dia 5.19

**Dia:** 5
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Sigilo profissional e suas exceções
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade)

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
**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia)

Em um caso, discute-se a competência do Plenário e da Diretoria do CRA-PR; em outro, examina-se possível violação de sigilo profissional. Qual associação normativa está correta?

A) Ambos os temas pertencem exclusivamente ao Regulamento de Registro aprovado pela RN CFA nº 649/2024.
B) A estrutura interna é matéria do Código de Ética, enquanto o sigilo pertence ao Regimento Interno.
C) Estrutura e competências remetem à RN nº 651/2024; sigilo, à RN nº 671/2025.
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
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está correta:** Resume o benefício da digitalização e a ressalva relativa à segurança e aos direitos.
- **B) está errada:** A segurança aparece integrada ao ganho de acesso e eficiência, não como objetivo independente.
- **C) está errada:** O texto não condiciona a legitimidade da digitalização à eliminação dos canais presenciais.
- **D) está errada:** O trecho não afirma que preservar direitos reduz necessariamente a eficiência.
- **Conceito cobrado:** Interpretação e identificação da ideia central.
- **Pegadinha usada:** Omitir uma parte da tese ou transformar ressalva em incompatibilidade.
- **Como pensar para acertar:** Reúna a afirmação principal e o limite introduzido por “mas”.
- **Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao).

### Comentário da Questão 2

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está errada:** A exigência de segurança não é apresentada como causa da ampliação do acesso.
- **B) está correta:** “Mas” contrapõe uma ressalva ao benefício anterior sem negá-lo.
- **C) está errada:** O segmento não conclui o raciocínio; limita o alcance da primeira afirmação.
- **D) está errada:** O valor semântico é adversativo, e não condicional.
- **Conceito cobrado:** Relação semântica de conectores.
- **Pegadinha usada:** Confundir ressalva com causa, conclusão ou condição.
- **Como pensar para acertar:** Substitua o conector por “porém” e verifique a preservação do contraste.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 3

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está errada:** O período não informa se a maioria das inovações falha.
- **B) está correta:** Negar que toda inovação represente melhoria implica ao menos um caso que não a representa.
- **C) está errada:** “Nem toda” não equivale a “nenhuma”.
- **D) está errada:** A origem da inovação não é mencionada.
- **Conceito cobrado:** Inferência e alcance de quantificadores.
- **Pegadinha usada:** Converter negação parcial em negação total ou em afirmação de maioria.
- **Como pensar para acertar:** Traduza “nem todo A é B” por “existe A que não é B”.
- **Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao).

### Comentário da Questão 4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** Reproduz a relação entre transparência e confiança admitida no texto.
- **B) está errada:** Corresponde ao limite expresso pela locução “desde que”.
- **C) está correta:** A divulgação irrestrita de todo dado pessoal contradiz o limite de proteção e extrapola o texto.
- **D) está errada:** Sintetiza a compatibilização permitida pelo enunciado.
- **Conceito cobrado:** Identificação de extrapolação textual.
- **Pegadinha usada:** Absolutizar uma afirmação condicionada.
- **Como pensar para acertar:** Desconfie de termos absolutos quando o texto estabelece limite explícito.
- **Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao).

### Comentário da Questão 5

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está errada:** Introduz aumento do esquecimento, sentido oposto ao original.
- **B) está correta:** A passagem para a voz passiva preserva as duas ações e seus sentidos.
- **C) está errada:** Afirma prejuízo à retenção, enquanto o período original afirma melhora.
- **D) está errada:** “Impede qualquer” e “integral” tornam absolutos efeitos que o original apenas apresenta como redução e melhora.
- **Conceito cobrado:** Reescrita com preservação de sentido.
- **Pegadinha usada:** Alterar polaridade ou intensidade lexical.
- **Como pensar para acertar:** Compare sujeito lógico, ações, direção dos efeitos e grau das afirmações.
- **Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita).

### Comentário da Questão 6

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está errada:** Com “existir”, o sujeito plural “pendências” exige “existem”.
- **B) está errada:** O sujeito plural “os comprovantes” exige “faltam”.
- **C) está correta:** “Faltam” concorda com o sujeito plural “documentos”.
- **D) está errada:** Na locução com “haver” existencial, o auxiliar permanece no singular: “deve haver”.
- **Conceito cobrado:** Concordância verbal com existir, faltar e haver.
- **Pegadinha usada:** Tratar “haver” existencial como verbo pessoal ou ignorar sujeito posposto.
- **Como pensar para acertar:** Identifique o verbo e teste se há sujeito ou construção impessoal.
- **Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia).

### Comentário da Questão 7

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está errada:** Em regra, não se usa artigo antes do pronome de tratamento “Vossa Senhoria”.
- **B) está errada:** Não ocorre crase antes de verbo no infinitivo.
- **C) está correta:** A regência de “encaminhar a” encontra o artigo feminino de “a diretoria”.
- **D) está errada:** A expressão “a pé” contém palavra masculina e não recebe crase.
- **Conceito cobrado:** Crase: fusão da preposição com artigo feminino.
- **Pegadinha usada:** Inserir crase antes de verbo, pronome de tratamento ou palavra masculina.
- **Como pensar para acertar:** Verifique simultaneamente a exigência de preposição e a admissão de artigo.
- **Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase).

### Comentário da Questão 8

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Observação:** a questão pede a alternativa em que a vírgula foi empregada incorretamente; portanto, o gabarito corresponde à frase com pontuação inadequada.
- **A) está errada:** A vírgula isola corretamente o adjunto adverbial deslocado.
- **B) está errada:** As vírgulas isolam o aposto explicativo.
- **C) está errada:** A oração subordinada adverbial anteposta está corretamente separada.
- **D) está correta:** A vírgula separa o sujeito completo “Os candidatos que revisaram o edital” do verbo “identificaram”.
- **Conceito cobrado:** Emprego da vírgula.
- **Pegadinha usada:** Inserir vírgula entre sujeito e predicado por percepção de pausa.
- **Como pensar para acertar:** Localize primeiro o núcleo do sujeito e o verbo principal.
- **Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao).

### Comentário da Questão 9

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** “Entretanto” preserva o valor adversativo de “contudo”.
- **B) está errada:** “Por conseguinte” tem valor conclusivo.
- **C) está errada:** “Porquanto” introduz causa ou explicação.
- **D) está errada:** “Contanto que” introduz condição.
- **Conceito cobrado:** Substituição de conectores com preservação de sentido.
- **Pegadinha usada:** Escolher conector formal de relação lógica diferente.
- **Como pensar para acertar:** Classifique a relação entre as orações antes de comparar os conectores.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 10

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** No sentido de aspirar, “visar” rege preposição “a”: “visava ao cargo”.
- **B) está correta:** “Obedecer” rege preposição “a”, presente em “ao edital” e “às orientações”.
- **C) está errada:** Na comparação normativa, prefere-se uma coisa a outra, não “do que” outra.
- **D) está errada:** No sentido de presenciar, “assistir” rege preposição “a”: “assistiram ao treinamento”.
- **Conceito cobrado:** Regência verbal.
- **Pegadinha usada:** Empregar regência coloquial em construção formal.
- **Como pensar para acertar:** Determine o sentido do verbo e, só então, a preposição exigida.
- **Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase).

### Comentário da Questão 11

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** O referente está expresso no próprio período.
- **B) está errada:** A redução das inconsistências é o efeito atribuído ao procedimento.
- **C) está errada:** O referente não é o substantivo isolado, mas a ação descrita.
- **D) está correta:** O demonstrativo encapsula a ação anterior de conferir os dados por dois servidores.
- **Conceito cobrado:** Coesão referencial.
- **Pegadinha usada:** Associar o demonstrativo ao substantivo mais próximo, e não à ideia retomada.
- **Como pensar para acertar:** Substitua “esse procedimento” pela alternativa e verifique a coerência.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 12

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** “Se” não apresenta conclusão de premissa comprovada.
- **B) está errada:** Não há obstáculo admitido com valor concessivo.
- **C) está errada:** Planejamento e execução não são contrapostos.
- **D) está correta:** A segurança da execução depende da hipótese de o planejamento ser consistente.
- **Conceito cobrado:** Oração subordinada adverbial condicional.
- **Pegadinha usada:** Confundir condição com conclusão ou concessão.
- **Como pensar para acertar:** Pergunte de qual hipótese depende o resultado da oração principal.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 13

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** “Há” indica tempo decorrido, e “a” integra a expressão de tempo futuro.
- **B) está errada:** Tempo decorrido pede “há três meses”; futuro pede “daqui a vinte dias”.
- **C) está errada:** “Há” não marca tempo futuro, e tempo decorrido exige “há duas semanas”.
- **D) está errada:** Os dois empregos estão invertidos.
- **Conceito cobrado:** Distinção entre “há” e “a” em expressões temporais.
- **Pegadinha usada:** Trocar a marca de passado pela de futuro.
- **Como pensar para acertar:** Use “há” para tempo decorrido e “a” para tempo futuro ou distância.
- **Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos).

### Comentário da Questão 14

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** “Seu próprio relatório” e o pronome objeto remetem claramente à equipe e ao relatório.
- **B) está errada:** A autoria foi explicitada pela expressão “elaborado pela equipe”.
- **C) está correta:** “Seu relatório” pode ser entendido como relatório do analista ou do coordenador.
- **D) está errada:** Analista e coordenador têm funções sintáticas e referências claramente delimitadas.
- **Conceito cobrado:** Ambiguidade pronominal.
- **Pegadinha usada:** Ignorar a possibilidade de dois antecedentes para o possessivo.
- **Como pensar para acertar:** Liste os referentes compatíveis com o pronome e verifique se há mais de um.
- **Referência:** [Dia 5 — Colocação pronominal, ambiguidade e uso de onde](semana_01_estudo.md#s1-d5-colocacao-onde).

### Comentário da Questão 15

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** A redução de riscos fundamenta a orientação de manter a medida.
- **B) está errada:** A segunda oração reforça, e não restringe, a primeira.
- **C) está errada:** Não se apresentam opções alternadas.
- **D) está errada:** A redução dos riscos é dada como razão, não como condição hipotética.
- **Conceito cobrado:** Valor explicativo e causal de “pois”.
- **Pegadinha usada:** Classificar o conector isoladamente, sem observar o contexto.
- **Como pensar para acertar:** Verifique se a segunda oração responde por que a primeira é defendida.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 16

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** A próclise é motivada pelo advérbio negativo “não”.
- **B) está errada:** No padrão formal cobrado, evita-se iniciar a oração com pronome oblíquo átono.
- **C) está errada:** O pronome não pode ser posposto ao particípio; caberia “tinha-me comunicado” ou “me tinha comunicado”.
- **D) está errada:** A palavra negativa atrai o pronome: “não se deve”.
- **Conceito cobrado:** Colocação pronominal.
- **Pegadinha usada:** Ignorar palavras atrativas ou reproduzir ordem coloquial.
- **Como pensar para acertar:** Procure termos negativos antes do verbo e posicione o pronome antes dele.
- **Referência:** [Dia 5 — Colocação pronominal, ambiguidade e uso de onde](semana_01_estudo.md#s1-d5-colocacao-onde).

### Comentário da Questão 17

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** Falta a segunda vírgula para encerrar o aposto “capital do Paraná”.
- **B) está correta:** O aposto explicativo está isolado por duas vírgulas.
- **C) está errada:** A vírgula separa indevidamente o sujeito do verbo e não abre o aposto.
- **D) está errada:** A pontuação fragmenta o aposto e separa o sujeito do predicado.
- **Conceito cobrado:** Pontuação de aposto explicativo.
- **Pegadinha usada:** Usar apenas uma vírgula em termo intercalado.
- **Como pensar para acertar:** Retire o segmento explicativo e confira se a estrutura principal permanece íntegra.
- **Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao).

### Comentário da Questão 18

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** “Apenas” não incide sobre a quantidade de exceções identificadas.
- **B) está errada:** Não se afirma que todos os candidatos revisaram a legislação.
- **C) está errada:** O período não enumera todas as atividades realizadas pelos candidatos.
- **D) está correta:** O advérbio restringe aos candidatos que revisaram a legislação o grupo que identificou a exceção.
- **Conceito cobrado:** Alcance semântico de advérbio restritivo.
- **Pegadinha usada:** Deslocar mentalmente o escopo de “apenas”.
- **Como pensar para acertar:** Identifique o constituinte imediatamente abrangido pelo advérbio.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 19

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** Verbo e predicativo deveriam concordar com “os relatórios”: “seguem anexos”.
- **B) está errada:** O verbo deveria ir ao plural para concordar com “os documentos”.
- **C) está errada:** O predicativo deveria ser “anexas”, em concordância com “as declarações”.
- **D) está correta:** “Seguem” e “anexos” concordam com “os documentos”.
- **Conceito cobrado:** Concordância verbal e nominal.
- **Pegadinha usada:** Tratar “anexo” como invariável ou concordar com termo preposicionado.
- **Como pensar para acertar:** Localize o sujeito e o substantivo caracterizado pelo adjetivo.
- **Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia).

### Comentário da Questão 20

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** A redução de filas é apresentada como objetivo deliberado.
- **B) está errada:** Não há oposição entre as ideias.
- **C) está correta:** A estrutura “para + infinitivo” indica o propósito da reformulação.
- **D) está errada:** O trecho não admite obstáculo com valor concessivo.
- **Conceito cobrado:** Oração subordinada adverbial final reduzida de infinitivo.
- **Pegadinha usada:** Confundir finalidade planejada com consequência.
- **Como pensar para acertar:** Pergunte “a política foi reformulada para quê?”.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 21

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** “Prédio” é lugar físico retomado adequadamente por “onde”.
- **B) está errada:** “Hipótese” é referente abstrato e não admite o uso normativo de “onde”.
- **C) está errada:** “Fundamento” não designa lugar físico; caberia “em que” ou “no qual”.
- **D) está errada:** “Conclusão” é antecedente abstrato sem valor locativo; o padrão é “a que a comissão chegou”.
- **Conceito cobrado:** Emprego normativo do pronome relativo “onde”.
- **Pegadinha usada:** Estender “onde” a qualquer antecedente abstrato.
- **Como pensar para acertar:** Verifique se o antecedente nomeia efetivamente um lugar.
- **Referência:** [Dia 5 — Colocação pronominal, ambiguidade e uso de onde](semana_01_estudo.md#s1-d5-colocacao-onde).

### Comentário da Questão 22

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está errada:** A frase apenas contextualiza o tema, sem defender posição.
- **B) está correta:** Delimita a posição e antecipa os eixos argumentativos de eficiência, inclusão e proteção.
- **C) está errada:** A pergunta problematiza o tema, mas não apresenta a resposta que será defendida.
- **D) está errada:** O metatexto adia o posicionamento e não formula tese.
- **Conceito cobrado:** Construção de tese dissertativa.
- **Pegadinha usada:** Confundir contextualização, pergunta ou roteiro com posicionamento.
- **Como pensar para acertar:** Procure uma frase discutível que possa orientar os parágrafos de desenvolvimento.
- **Referência:** [Dia 5 — Estrutura da discursiva](semana_01_estudo.md#s1-d5-discursiva-estrutura).

### Comentário da Questão 23

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** O trecho não propõe intervenção nem apresenta conclusão.
- **B) está errada:** O problema é falta, e não excesso, de delimitação.
- **C) está errada:** Há repetição, mas não existe tese explícita sobre serviços públicos digitais.
- **D) está correta:** O trecho repete uma ideia ampla sem recorte nem posição argumentativa.
- **Conceito cobrado:** Diagnóstico de introdução dissertativa.
- **Pegadinha usada:** Tratar repetição temática como contextualização suficiente.
- **Como pensar para acertar:** Pergunte qual posição concreta o restante do texto deveria demonstrar.
- **Referência:** [Dia 5 — Estrutura da discursiva](semana_01_estudo.md#s1-d5-discursiva-estrutura).

### Comentário da Questão 24

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** Atualidade do tema, isoladamente, não explica mecanismo nem consequência.
- **B) está errada:** A formulação é circular: associa eficiência apenas ao fato de funcionar bem.
- **C) está correta:** Apresenta benefício, mecanismo concreto e contraponto relacionado à inclusão.
- **D) está errada:** A existência de plataforma não comprova acesso equivalente para todos.
- **Conceito cobrado:** Qualidade do desenvolvimento argumentativo.
- **Pegadinha usada:** Confundir afirmação formal ou atual com argumento desenvolvido.
- **Como pensar para acertar:** Prefira o trecho que liga tese, causa, consequência e ressalva pertinente.
- **Referência:** [Dia 5 — Modelo discursivo comentado](semana_01_estudo.md#s1-d5-discursiva-modelo).

### Comentário da Questão 25

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** O apelo a “qualquer pessoa sensata” é avaliativo e substitui demonstração por pressão retórica.
- **B) está errada:** Marcas de opinião e hesitação tornam a afirmação subjetiva e imprecisa.
- **C) está errada:** “Certas coisas” e “conforme for possível” são expressões vagas.
- **D) está correta:** Indica sujeito, dever e três medidas verificáveis em registro formal.
- **Conceito cobrado:** Registro formal, precisão e objetividade.
- **Pegadinha usada:** Confundir aparência formal com redação informativa.
- **Como pensar para acertar:** Escolha a frase com agente, ação e critérios concretos.
- **Referência:** [Dia 5 — Autocorreção da discursiva](semana_01_estudo.md#s1-d5-discursiva-rubrica).

### Comentário da Questão 26

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** Não se emprega crase antes do infinitivo “analisar”.
- **B) está errada:** “Encaminhar a” e o artigo de “autoridade” produzem crase.
- **C) está errada:** Em “àquela”, fundem-se a preposição regida e o “a” inicial do demonstrativo.
- **D) está errada:** “Comparecer a” encontra o artigo plural de “as reuniões”.
- **Conceito cobrado:** Crase em contextos de regência.
- **Pegadinha usada:** Aplicar mecanicamente o acento antes de qualquer termo feminino ou infinitivo.
- **Como pensar para acertar:** Faça o teste da preposição e do artigo em cada alternativa.
- **Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase).

### Comentário da Questão 27

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** O período nada afirma sobre o desempenho necessário de todos os que não estudaram.
- **B) está errada:** A leitura de totalidade seria favorecida pela oração explicativa entre vírgulas.
- **C) está errada:** A estrutura não demonstra causalidade exclusiva.
- **D) está correta:** A oração sem vírgulas delimita quais candidatos recebem a afirmação de melhor desempenho.
- **Conceito cobrado:** Oração subordinada adjetiva restritiva.
- **Pegadinha usada:** Extrair causalidade ou universalidade de uma simples delimitação.
- **Como pensar para acertar:** Observe se a oração seleciona o referente ou apenas acrescenta informação.
- **Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes).

### Comentário da Questão 28

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** A oração restritiva não seria isolada por vírgulas.
- **B) está errada:** Não há conector nem hipótese condicional.
- **C) está errada:** A estrutura não estabelece comparação entre grupos.
- **D) está correta:** As vírgulas atribuem valor explicativo à informação sobre o conjunto mencionado.
- **Conceito cobrado:** Oração subordinada adjetiva explicativa.
- **Pegadinha usada:** Ignorar que a pontuação altera o alcance da oração adjetiva.
- **Como pensar para acertar:** Compare o efeito semântico de retirar ou inserir as vírgulas.
- **Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes).

### Comentário da Questão 29

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** Coordena substantivo, infinitivo e novo sintagma nominal sem uniformidade.
- **B) está correta:** Os três itens coordenados são verbos no infinitivo com seus complementos.
- **C) está errada:** Mistura oração desenvolvida, infinitivo e substantivo.
- **D) está errada:** Combina substantivo, infinitivo e oração desenvolvida.
- **Conceito cobrado:** Paralelismo sintático.
- **Pegadinha usada:** Manter coerência temática, mas quebrar a forma gramatical da enumeração.
- **Como pensar para acertar:** Isole os itens coordenados e compare sua estrutura.
- **Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita).

### Comentário da Questão 30

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** “O coordenador” e “a diretora” exercem função de sujeito, não de vocativo.
- **B) está errada:** Não há verbo expresso depois dos sujeitos; a vírgula sinaliza justamente sua elipse.
- **C) está correta:** O verbo “revisou” foi omitido nas duas últimas orações e recuperado da primeira.
- **D) está errada:** “A planilha” e “o parecer” são complementos do verbo elíptico, não apostos.
- **Conceito cobrado:** Vírgula vicária e elipse verbal.
- **Pegadinha usada:** Confundir omissão marcada por vírgula com separação indevida.
- **Como pensar para acertar:** Reponha o verbo da primeira oração nas estruturas seguintes.
- **Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao).

### Comentário da Questão 31

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** “Haver” com sentido de existir é impessoal: “houve dois anos de testes”.
- **B) está errada:** A expressão plural de tempo não leva o verbo impessoal ao plural.
- **C) está errada:** O auxiliar de locução com “fazer” temporal também deve ficar no singular: “deve fazer”.
- **D) está correta:** “Fazer” com sentido de tempo decorrido é impessoal e permanece no singular.
- **Conceito cobrado:** Verbos impessoais em expressões temporais e existenciais.
- **Pegadinha usada:** Fazer o verbo concordar com a expressão plural posposta.
- **Como pensar para acertar:** Verifique se “fazer” indica tempo e se “haver” equivale a existir.
- **Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia).

### Comentário da Questão 32

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** Na oração causal, usa-se “porque”.
- **B) está correta:** Com artigo, “porquê” é substantivo e significa “motivo”.
- **C) está errada:** A locução interrogativa exige “por que motivo”, com as duas palavras separadas.
- **D) está errada:** Em pergunta direta, usa-se “por que”.
- **Conceito cobrado:** Emprego de porque, por que e porquê.
- **Pegadinha usada:** Escolher a forma pela entonação, sem analisar função e posição.
- **Como pensar para acertar:** Teste “por qual motivo” e observe a presença de artigo.
- **Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos).

### Comentário da Questão 33

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** A detecção adicional de inconsistências serve de premissa para manter o procedimento.
- **B) está errada:** A manutenção é defendida como conclusão, não como condição.
- **C) está errada:** Não se admite obstáculo nem se relativiza a utilidade da revisão.
- **D) está errada:** Embora haja contraste entre tipos de conferência no primeiro segmento, “portanto” liga a premissa à conclusão.
- **Conceito cobrado:** Conector conclusivo e progressão argumentativa.
- **Pegadinha usada:** Classificar o conector pela oposição interna do período, e não pela ligação que ele realiza.
- **Como pensar para acertar:** Identifique exatamente quais segmentos o conector relaciona.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 34

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está correta:** Na voz passiva, “pela equipe de auditoria” nomeia quem identificou.
- **B) está errada:** A expressão não caracteriza o substantivo “inconsistências”.
- **C) está errada:** O sujeito paciente é “As inconsistências”.
- **D) está errada:** Na forma ativa, “a equipe de auditoria” seria sujeito, não objeto indireto.
- **Conceito cobrado:** Voz passiva e agente da passiva.
- **Pegadinha usada:** Confundir o agente introduzido por preposição com objeto indireto.
- **Como pensar para acertar:** Converta o período para a voz ativa e identifique quem pratica a ação.
- **Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes).

### Comentário da Questão 35

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** “Para verificar” expressa finalidade.
- **B) está errada:** “Embora” introduz concessão.
- **C) está correta:** O surgimento dos documentos explica por que a análise foi reaberta.
- **D) está errada:** “Desde que” introduz condição.
- **Conceito cobrado:** Relações adverbiais de causa, concessão, finalidade e condição.
- **Pegadinha usada:** Confundir a razão de uma ação com seu objetivo.
- **Como pensar para acertar:** Pergunte se a oração responde “por quê?”, “para quê?” ou “em que condição?”.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 36

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** “Em 2025” situa a publicação da norma, não diretamente a alteração do procedimento.
- **B) está errada:** O verbo principal é “alterou”, cujo sujeito expresso é “A norma publicada em 2025”.
- **C) está correta:** A estrutura reduzida de particípio equivale a “que foi publicada em 2025” e restringe o referente.
- **D) está errada:** O segmento caracteriza “norma” e não completa nominalmente seu sentido.
- **Conceito cobrado:** Oração reduzida de particípio com valor adjetivo.
- **Pegadinha usada:** Associar todo marcador temporal ao verbo principal.
- **Como pensar para acertar:** Desenvolva a oração reduzida e observe qual termo ela modifica.
- **Referência:** [Dia 5 — Sintaxe e relações entre orações](semana_01_estudo.md#s1-d5-sintaxe-oracoes).

### Comentário da Questão 37

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está correta:** Os termos intercalados estão delimitados e a enumeração foi pontuada adequadamente.
- **B) está errada:** Faltam vírgulas entre os três itens enumerados.
- **C) está errada:** A vírgula separa indevidamente o sujeito “o candidato” do verbo “revisou”.
- **D) está errada:** Há vírgulas que fragmentam o adjunto e separam o verbo de seu complemento.
- **Conceito cobrado:** Pontuação de termos deslocados, intercalados e enumerados.
- **Pegadinha usada:** Pontuar por pausas de leitura sem respeitar a estrutura sintática.
- **Como pensar para acertar:** Marque primeiro a estrutura principal e depois isole apenas os termos acessórios.
- **Referência:** [Dia 5 — Pontuação](semana_01_estudo.md#s1-d5-pontuacao).

### Comentário da Questão 38

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** O monitoramento não é apresentado como finalidade da primeira negação.
- **B) está errada:** A locução não introduz conclusão.
- **C) está correta:** “Tampouco” adiciona “não dispensa” a “não elimina”.
- **D) está errada:** O segundo predicado não explica a causa do primeiro.
- **Conceito cobrado:** Conector de adição negativa.
- **Pegadinha usada:** Inferir causa ou conclusão de uma simples coordenação negativa.
- **Como pensar para acertar:** Substitua “tampouco” por “também não”.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 39

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **A) está errada:** Abre assunto novo que o próprio trecho reconhece não ter desenvolvido.
- **B) está correta:** Retoma a tese e sintetiza medidas compatíveis com transparência e proteção de dados.
- **C) está errada:** Contradiz a tese ao defender publicidade irrestrita.
- **D) está errada:** Produz fechamento vago e sugere liberdade incompatível com critérios normativos.
- **Conceito cobrado:** Conclusão dissertativa.
- **Pegadinha usada:** Encerrar com tema novo, contradição ou generalidade.
- **Como pensar para acertar:** Verifique se a conclusão retoma a tese sem criar premissa inédita.
- **Referência:** [Dia 5 — Estrutura da discursiva](semana_01_estudo.md#s1-d5-discursiva-estrutura).

### Comentário da Questão 40

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** As palavras são acentuadas por regras distintas de paroxítonas terminadas em ditongo e em “l”.
- **B) está correta:** As três palavras têm a antepenúltima sílaba tônica e toda proparoxítona é acentuada.
- **C) está errada:** A forma normativa adjetiva “lógico” exige acento e tem tonicidade antepenúltima.
- **D) está errada:** “Técnico” é proparoxítono, não paroxítono terminado em “o”.
- **Conceito cobrado:** Regras de acentuação gráfica.
- **Pegadinha usada:** Agrupar palavras acentuadas como se obedecessem à mesma regra.
- **Como pensar para acertar:** Separe as sílabas e localize a sílaba tônica antes de aplicar a regra.
- **Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos).

### Comentário da Questão 41

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** `Como` cria causa e `portanto` cria conclusão, relações que o texto não estabelece entre as três ações.
- **B) está errada:** A correlação `ou... ou` transforma ações cumulativas em alternativas, e `por isso` acrescenta causalidade.
- **C) está errada:** `Embora` introduz concessão e `por essa razão` apresenta a não homologação como consequência necessária.
- **D) está correta:** `E` mantém a soma das duas ações, enquanto `entretanto` preserva a oposição de `contudo`.
- **Conceito cobrado:** Coordenação aditiva, oposição e equivalência semântica na reescrita.
- **Pegadinha usada:** Produzir frase gramaticalmente correta, mas trocar adição e contraste por causa, conclusão, alternância ou concessão.
- **Como pensar para acertar:** Marque a relação lógica em cada ponto de articulação e compare as duas relações na reescrita.
- **Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita).

### Comentário da Questão 42

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** O padrão é “compatível com a norma” e “contrário ao entendimento”.
- **B) está errada:** “Acessível aos usuários” está correto, mas “passível” rege “de”: “passível de auditoria”.
- **C) está errada:** O padrão é “favorável ao recurso” e “avessa a nova instrução”.
- **D) está correta:** “Apto a” e “consciente de” regem adequadamente “ao exercício” e “das responsabilidades”.
- **Conceito cobrado:** Regência nominal de múltiplos nomes.
- **Pegadinha usada:** Inserir uma relação correta ao lado de outra incorreta na mesma alternativa.
- **Como pensar para acertar:** Valide separadamente cada nome e seu complemento.
- **Referência:** [Dia 5 — Regência e crase](semana_01_estudo.md#s1-d5-regencia-crase).

### Comentário da Questão 43

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** A parcela inicial verdadeira não torna verdadeira uma proposição cujo restante extrapola quantidade e causa.
- **B) está correta:** O procedimento testa o todo, rejeita a passagem de “3 de 20” para “todos” e não aceita negligência sem causa demonstrada.
- **C) está errada:** O trecho posterior integra a alternativa e precisa ser avaliado antes da aplicação do comando negativo.
- **D) está errada:** Um conector conclusivo organiza a frase, mas não cria evidência para transformar hipótese em fato.
- **Conceito cobrado:** Quantificador, inferência causal, composição da alternativa e leitura de comando negativo.
- **Pegadinha usada:** Parar no fragmento verdadeiro e aceitar simultaneamente generalização e causa não comprovada.
- **Como pensar para acertar:** Compare número, causa e consequência com o texto-base; avalie a proposição completa e, por fim, aplique “INCORRETA”.
- **Referência:** [Dia 5 — Interpretação, inferência e pressupostos](semana_01_estudo.md#s1-d5-interpretacao).

### Comentário da Questão 44

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** Mantém a revisão em momento posterior ao erro e preserva a restrição temporal.
- **B) está errada:** “Apenas após” conserva o mesmo limite temporal.
- **C) está correta:** Afirma revisão anterior ao erro e inverte a ordem temporal original.
- **D) está errada:** A construção clivada enfatiza, sem alterar, o momento da revisão.
- **Conceito cobrado:** Escopo adverbial e reescrita semântica.
- **Pegadinha usada:** Ignorar a instrução sobre o alcance de “só” ou observar apenas palavras repetidas.
- **Como pensar para acertar:** Compare a ordem dos eventos e o elemento sobre o qual recai a restrição.
- **Referência:** [Dia 5 — Reescrita e preservação de sentido](semana_01_estudo.md#s1-d5-reescrita).

### Comentário da Questão 45

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está correta:** `Ainda que` conserva a concessão de `embora`, e `consequentemente` mantém o valor conclusivo de `por isso`.
- **B) está errada:** `Como` converte o orçamento reduzido em causa da conclusão, e `apesar disso` troca consequência por concessão.
- **C) está errada:** `Se` cria condição hipotética, enquanto `entretanto` apresenta oposição em lugar da consequência.
- **D) está errada:** `Porque` transforma o obstáculo em causa, e `ainda assim` não preserva a inferência que liga conclusão e manutenção do cronograma.
- **Conceito cobrado:** Concessão, consequência e preservação de relações lógicas em reescrita.
- **Pegadinha usada:** Manter o assunto e a correção gramatical, mas permutar as relações entre os segmentos.
- **Como pensar para acertar:** Analise os dois conectores separadamente e exija que a alternativa preserve ambos, não apenas o primeiro.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 46

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** Com “mais de um”, o verbo fica normalmente no singular: “enviou”.
- **B) está errada:** Na locução existencial, o auxiliar permanece no singular: “deve haver”.
- **C) está errada:** O padrão é “um ou outro candidato apresentou”, com núcleo e verbo no singular.
- **D) está correta:** A expressão “mais de um candidato” exige singular na ausência de reciprocidade ou repetição.
- **Conceito cobrado:** Casos especiais de concordância verbal.
- **Pegadinha usada:** Aplicar concordância puramente numérica a expressões de estrutura singular.
- **Como pensar para acertar:** Reconheça a expressão fixa e verifique se existe exceção contextual.
- **Referência:** [Dia 5 — Concordância verbal e nominal](semana_01_estudo.md#s1-d5-concordancia).

### Comentário da Questão 47

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** `Dessas exigências` está no plural e encapsula duas obrigações, não somente o dever de informar.
- **B) está errada:** A primeira expressão é anafórica, e `a última delas` não retoma o efeito de reduzir usos incompatíveis.
- **C) está correta:** A primeira expressão resume as duas obrigações; `a última delas` seleciona a segunda, limitar o acesso.
- **D) está errada:** `Finalidade` é objeto de uma obrigação, não o conjunto retomado, e a última medida não é informar titulares.
- **Conceito cobrado:** Encapsulamento anafórico, antecedente composto e seleção referencial.
- **Pegadinha usada:** Ignorar número, ordem dos antecedentes e o alcance do demonstrativo `última`.
- **Como pensar para acertar:** Expanda cada expressão pelo possível antecedente e confirme concordância, posição e continuidade de sentido.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 48

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** “Ratificação” confirma; não nomeia a correção do erro, e “retificar” não expressa a confirmação dos demais termos.
- **B) está correta:** “Retificação” corrige, “ratificar” confirma e “discrição” indica reserva ou prudência.
- **C) está errada:** “Ratificação” não corresponde à correção, e “descrição” não significa prudência no trato de dados.
- **D) está errada:** “Retificar” significa corrigir, e “descrição” significa ato de descrever, inadequado à ideia de reserva.
- **Conceito cobrado:** Parônimos e seleção lexical contextual.
- **Pegadinha usada:** Confundir palavras próximas na forma, mas diferentes no sentido.
- **Como pensar para acertar:** Substitua cada lacuna por uma definição curta antes de avaliar o conjunto.
- **Referência:** [Dia 5 — Ortografia, acentuação e parônimos](semana_01_estudo.md#s1-d5-acentuacao-paronimos).

### Comentário da Questão 49

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** `À medida que` introduz proporção e `portanto` conclusão, alterando as duas relações originais.
- **B) está errada:** `A menos que` cria condição excepcional e `por conseguinte` introduz consequência.
- **C) está correta:** `Porque` preserva a justificativa causal, e `mesmo assim` mantém a oposição concessiva de `ainda assim`.
- **D) está errada:** `Embora` é concessivo, não causal, e `por essa razão` converte a oposição em conclusão.
- **Conceito cobrado:** Equivalência contextual de conectores causais e concessivos.
- **Pegadinha usada:** Acertar a substituição de um conector e aceitar que o segundo altere a progressão argumentativa.
- **Como pensar para acertar:** Determine o valor de cada expressão destacada e valide o par completo na ordem em que aparece.
- **Referência:** [Dia 5 — Semântica, coesão e conectores](semana_01_estudo.md#s1-d5-semantica-coesao).

### Comentário da Questão 50

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está correta:** Identifica data, quantidade e localização dos achados e distingue o registro factual da correção e do reteste recomendados.
- **B) está errada:** Afirma causa com certeza sem apresentar evidência e usa expressões vagas para ação e prazo.
- **C) está errada:** `Diversos pontos`, `relevantes` e `necessidade evidente` não permitem conferir achados nem separar dado de avaliação.
- **D) está errada:** Momento, causa e responsáveis permanecem indeterminados, e a providência não possui critério verificável.
- **Conceito cobrado:** Redação administrativa, verificabilidade e distinção entre constatação e recomendação.
- **Pegadinha usada:** Confundir tom categórico ou formal com objetividade e apresentar inferência causal como fato comprovado.
- **Como pensar para acertar:** Procure evidência identificável, delimitação do achado e marca explícita de que a providência é recomendada.
- **Referência:** [Dia 5 — Autocorreção da discursiva](semana_01_estudo.md#s1-d5-discursiva-rubrica).

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
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está errada:** O Regimento organiza o conselho regional e não pode ampliar o campo profissional fixado em lei.
- **B) está errada:** Resoluções complementam a disciplina dentro da competência normativa, mas não prevalecem sobre lei e decreto.
- **C) está correta:** A alternativa respeita a função e a hierarquia de cada espécie normativa.
- **D) está errada:** O decreto regulamenta a execução da lei profissional e não se limita à organização interna do CRA-PR.
- **Conceito cobrado:** Articulação entre lei, decreto, resoluções e regimento.
- **Pegadinha usada:** Confundir posterioridade ou detalhamento com superioridade hierárquica.
- **Como pensar para acertar:** Identifique o fundamento legal e a função complementar de cada ato.
- **Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia).

#### Comentário Extra Dia 5.2

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **A) está errada:** A atuação fiscalizatória não depende de dano patrimonial comprovado pelo cliente.
- **B) está errada:** O possível uso indevido pode existir antes da celebração de contrato.
- **C) está errada:** Registro posterior não torna automaticamente regular uma conduta praticada antes da habilitação.
- **D) está correta:** A apresentação pública como registrado exige verificação de habilitação e de uso regular da condição profissional.
- **Conceito cobrado:** Uso de título e regularidade do exercício profissional.
- **Pegadinha usada:** Condicionar a irregularidade a contrato, prejuízo ou regularização posterior.
- **Como pensar para acertar:** Compare a condição apresentada no anúncio com a habilitação existente naquele momento.
- **Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao).

#### Comentário Extra Dia 5.3

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** A fiscalização regional ordinária cabe aos CRAs em suas jurisdições; o CFA atua no plano nacional e normativo.
- **B) está correta:** Reúne os critérios material e territorial da atuação do CRA.
- **C) está errada:** A mera condição empresarial não basta; a atividade deve guardar relação com o campo fiscalizado.
- **D) está errada:** A competência não decorre apenas do domicílio do denunciante.
- **Conceito cobrado:** Campo e competência territorial de fiscalização.
- **Pegadinha usada:** Universalizar a competência do CFA ou do conselho regional.
- **Como pensar para acertar:** Verifique simultaneamente a matéria da atividade e a jurisdição competente.
- **Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao).

#### Comentário Extra Dia 5.4

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **A) está correta:** A estrutura confirmada do Código reúne deveres, direitos, infrações e critérios de fixação e gradação das sanções; o rito processual possui regulamentação própria.
- **B) está errada:** Anuidades e cobrança não constituem o núcleo do Código de Ética.
- **C) está errada:** A RN CFA nº 651/2024, e não a nº 671/2025, é associada ao Regimento Interno no material.
- **D) está errada:** Memorização isolada não permite resolver situações éticas concretas.
- **Conceito cobrado:** Conteúdo e método de estudo do Código de Ética.
- **Pegadinha usada:** Trocar as resoluções ou reduzir o estudo à numeração de artigos.
- **Como pensar para acertar:** Associe cada norma a seu objeto e aplique a regra à conduta descrita.
- **Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade).

#### Comentário Extra Dia 5.5

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** Conselho profissional não se limita à defesa econômica corporativa.
- **B) está errada:** A fiscalização administrativa não substitui a função jurisdicional em todo conflito.
- **C) está errada:** Definição autônoma de currículos universitários não é a finalidade indicada.
- **D) está correta:** A proteção social e a regularidade do exercício justificam a função fiscalizatória.
- **Conceito cobrado:** Finalidade dos conselhos profissionais.
- **Pegadinha usada:** Equiparar conselho a associação privada, tribunal ou instituição de ensino.
- **Como pensar para acertar:** Relacione a fiscalização ao interesse público protegido.
- **Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao).

#### Comentário Extra Dia 5.6

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** Autorização para usar o registro não substitui a atuação técnica efetiva.
- **B) está correta:** Responsabilidade técnica exige participação real e regular na atividade assumida.
- **C) está errada:** A pessoa jurídica não elimina a necessidade de profissional habilitado quando a responsabilidade técnica é exigível.
- **D) está errada:** A responsabilidade acompanha a atividade exercida sob a indicação, e não apenas a assinatura inicial.
- **Conceito cobrado:** Efetividade da responsabilidade técnica.
- **Pegadinha usada:** Tratar indicação profissional como cessão formal de nome ou registro.
- **Como pensar para acertar:** Procure evidência de acompanhamento, decisão técnica e atuação concreta.
- **Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade).

#### Comentário Extra Dia 5.7

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está errada:** Novidade cronológica, sem pertinência ao edital e ato oficial, não basta para trocar a base.
- **B) está errada:** A RN CFA nº 651/2024 é relacionada ao Regimento Interno, não ao novo Código de Ética.
- **C) está correta:** O material fundamenta a escolha no edital retificado e na fonte oficial de vigência.
- **D) está errada:** Normas sucessivas não se aplicam cumulativamente de modo automático aos mesmos fatos.
- **Conceito cobrado:** Seleção da norma vigente indicada no edital.
- **Pegadinha usada:** Aplicar automaticamente a norma numericamente mais recente ou acumular textos sucessivos.
- **Como pensar para acertar:** Confira edital, retificação, objeto da resolução e informação oficial de vigência.
- **Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia).

#### Comentário Extra Dia 5.8

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **A) está correta:** A decomposição do caso evita confundir conduta, sujeito, competência e fundamento.
- **B) está errada:** A sanção é consequência da análise normativa, não seu ponto de partida.
- **C) está errada:** CFA e CRA possuem papéis distintos no sistema.
- **D) está errada:** Ressalvas e quantificadores alteram o alcance da norma e da alternativa.
- **Conceito cobrado:** Método de resolução de casos de legislação específica.
- **Pegadinha usada:** Decidir por severidade, palavra-chave ou autoridade genérica.
- **Como pensar para acertar:** Monte a sequência fato, sujeito, competência, regra e consequência.
- **Referência:** [Dia 5 — Processo, sanção e controle de fonte](semana_01_estudo.md#s1-d5-processo-sancao).

#### Comentário Extra Dia 5.9

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** Nem toda infração conduz à penalidade máxima.
- **B) está errada:** Prova documental não elimina, por si só, as garantias do processo e da defesa.
- **C) está errada:** Proporcionalidade orienta a escolha dentro da lei; não autoriza criar sanção.
- **D) está correta:** Penalidade requer previsão, procedimento e adequação à infração apurada.
- **Conceito cobrado:** Legalidade, processo e proporcionalidade das sanções.
- **Pegadinha usada:** Transformar rigor em automatismo ou em poder sancionador sem limite.
- **Como pensar para acertar:** Verifique previsão normativa, competência, procedimento e gradação.
- **Referência:** [Dia 5 — Processo, sanção e controle de fonte](semana_01_estudo.md#s1-d5-processo-sancao).

#### Comentário Extra Dia 5.10

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** O Regimento não se limita a contribuições nem à cobrança.
- **B) está errada:** A definição originária do campo profissional pertence à base legal da profissão.
- **C) está errada:** Deveres éticos e sanções remetem ao Código de Ética vigente.
- **D) está correta:** Estrutura, órgãos, competências e funcionamento são matérias típicas do Regimento Interno.
- **Conceito cobrado:** Objeto do Regimento Interno do CRA-PR.
- **Pegadinha usada:** Misturar organização institucional, campo profissional e disciplina ética.
- **Como pensar para acertar:** Associe “quem faz o quê dentro do CRA-PR” ao Regimento.
- **Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia).

#### Comentário Extra Dia 5.11

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** O Código de Ética alcança pessoas físicas e jurídicas, observadas as especificidades de cada sujeito.
- **B) está correta:** Ambos podem ser apurados, sem transportar à pessoa jurídica sanções próprias do exercício profissional.
- **C) está errada:** Sujeitos distintos exigem enquadramento compatível; não há reprodução automática de sanção.
- **D) está errada:** O registro da empresa não absorve a responsabilidade individual pela atuação técnica praticada.
- **Conceito cobrado:** Responsabilidade ética de pessoa física e jurídica e compatibilidade de sanções.
- **Pegadinha usada:** Excluir a pessoa jurídica do Código ou aplicar indistintamente a ambos a mesma consequência.
- **Como pensar para acertar:** Separe sujeitos, condutas e sanções compatíveis antes de concluir.
- **Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade).

#### Comentário Extra Dia 5.12

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** Regulamentar não autoriza o decreto a ultrapassar os limites da lei.
- **B) está correta:** O decreto detalha a execução da lei sem revogá-la nem superá-la hierarquicamente.
- **C) está errada:** A edição do regulamento não elimina a lei regulamentada.
- **D) está errada:** O Decreto nº 61.934/1967 não é regimento interno do CRA-PR.
- **Conceito cobrado:** Relação entre lei e decreto regulamentador.
- **Pegadinha usada:** Confundir detalhamento regulamentar com inovação ilimitada ou revogação.
- **Como pensar para acertar:** Preserve a lei como fundamento e situe o decreto como ato de execução.
- **Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia).

#### Comentário Extra Dia 5.13

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está correta:** Separa corretamente formação acadêmica de situação financeira perante o conselho.
- **B) está errada:** Consequências dependem de fundamento normativo e das garantias aplicáveis.
- **C) está errada:** Conselho profissional não cancela diploma nem apaga formação acadêmica por inadimplência.
- **D) está errada:** Vínculo acadêmico, por si só, não extingue contribuição regularmente devida.
- **Conceito cobrado:** Distinção entre formação, registro e regularidade financeira.
- **Pegadinha usada:** Tratar diploma, registro e anuidade como uma única condição.
- **Como pensar para acertar:** Identifique qual relação jurídica cada consequência pode atingir.
- **Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao).

#### Comentário Extra Dia 5.14

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** Comentário didático e ato oficial não possuem a mesma autoridade normativa.
- **B) está errada:** Resumo auxilia o estudo, mas não prevalece sobre publicação oficial divergente.
- **C) está correta:** Texto oficial e vigência são indispensáveis para detalhes literais como prazo, rito e penalidade.
- **D) está errada:** Número ou data mais recente não substitui automaticamente a base indicada no edital.
- **Conceito cobrado:** Uso de fontes oficiais no estudo normativo.
- **Pegadinha usada:** Tomar material secundário ou novidade cronológica como fonte suficiente.
- **Como pensar para acertar:** Confirme texto, vigência e pertinência ao edital antes de memorizar detalhe.
- **Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia).

#### Comentário Extra Dia 5.15

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está correta:** O Regimento atribui ao Plenário a deliberação superior e à Diretoria a execução administrativa em suas competências.
- **B) está errada:** O Plenário não é meramente consultivo, nem a Diretoria concentra toda deliberação institucional.
- **C) está errada:** O Plenário não se converte em órgão executivo, e revisão ética não é função automática da Diretoria.
- **D) está errada:** A distribuição de funções decorre do Regimento, não de escolha livre do presidente.
- **Conceito cobrado:** Distinção funcional entre Plenário e Diretoria Executiva.
- **Pegadinha usada:** Inverter deliberação e execução ou apagar a distribuição regimental de competências.
- **Como pensar para acertar:** Identifique se a ação é deliberar ou executar e associe o órgão regimental.
- **Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia).

#### Comentário Extra Dia 5.16

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** Indício inicia ou instrui a apuração; não equivale a condenação nem executa a escolha do denunciante.
- **B) está errada:** A existência de documento não elimina ciência dos fatos, contraditório e defesa.
- **C) está correta:** Autoridade competente, apuração regular, contraditório, defesa e decisão fundamentada formam a sequência segura.
- **D) está errada:** Sanção precisa de base normativa e não pode ser escolhida antes do enquadramento e do processo.
- **Conceito cobrado:** Distinção entre indício, apuração e decisão sancionadora.
- **Pegadinha usada:** Transformar documento em condenação ou selecionar pena antes da norma e do processo.
- **Como pensar para acertar:** Percorra `indício → autoridade → apuração → defesa → decisão fundamentada`.
- **Referência:** [Dia 5 — Processo, sanção e controle de fonte](semana_01_estudo.md#s1-d5-processo-sancao).

#### Comentário Extra Dia 5.17

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** O registro de origem não transfere ao CFA toda verificação cotidiana nem elimina a atuação regional sobre o fato local.
- **B) está correta:** O território da execução orienta a atuação do CRA-PR, preservadas coordenação e normatização nacionais do CFA.
- **C) está errada:** A jurisdição e o processo não podem ser ignorados por outro Regional.
- **D) está errada:** Registro anterior não regulariza automaticamente toda atividade futura em qualquer território.
- **Conceito cobrado:** Jurisdição do fato e distinção entre atuação regional e coordenação nacional.
- **Pegadinha usada:** Confundir registro originário com imunidade territorial ou competência fiscalizatória exclusiva do CFA.
- **Como pensar para acertar:** Localize o fato, identifique o Regional da jurisdição e separe sua atuação da função nacional do CFA.
- **Referência:** [Dia 5 — Registro, jurisdição e fiscalização](semana_01_estudo.md#s1-d5-registro-fiscalizacao).

#### Comentário Extra Dia 5.18

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está correta:** Independência técnica exige fundamento verificável e impede validar conclusão sem suporte por pressão hierárquica.
- **B) está errada:** A ordem superior não elimina a responsabilidade de quem altera e assina o relatório.
- **C) está errada:** Retirar a identificação não cria fundamento nem torna ética uma conclusão sem base.
- **D) está errada:** Sigilo não serve para encobrir irregularidade nem afastar fiscalização competente.
- **Conceito cobrado:** Independência técnica, fundamentação e responsabilidade profissional.
- **Pegadinha usada:** Tratar hierarquia ou sigilo como autorização para alterar informação técnica sem base.
- **Como pensar para acertar:** Exija evidência, preserve a autoria responsável e recuse validação incompatível com o fundamento técnico.
- **Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade).

#### Comentário Extra Dia 5.19

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** Vantagem econômica não constitui, por si, justa causa para quebrar o sigilo profissional.
- **B) está errada:** A retirada do nome não autoriza divulgação de conteúdo confidencial quando a informação continua protegida.
- **C) está errada:** Transferir os dados a terceiro já representa revelação e não desloca a responsabilidade ética.
- **D) está correta:** Sem hipótese legal ou justa causa, prevalece o dever de preservar a informação conhecida no exercício profissional.
- **Conceito cobrado:** Sigilo profissional e suas exceções.
- **Pegadinha usada:** Criar exceção comercial ou indireta para contornar o dever de confidencialidade.
- **Como pensar para acertar:** Procure fundamento jurídico concreto para a revelação; ausente ele, mantenha o sigilo.
- **Referência:** [Dia 5 — Ética e responsabilidade técnica](semana_01_estudo.md#s1-d5-etica-responsabilidade).

#### Comentário Extra Dia 5.20

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **A) está errada:** O Regulamento de Registro não concentra estrutura institucional e disciplina ética.
- **B) está errada:** A alternativa troca os objetos: órgãos internos pertencem ao Regimento; sigilo, ao Código de Ética.
- **C) está correta:** A RN nº 651/2024 aprova o Regimento do CRA-PR, e a RN nº 671/2025 disciplina condutas éticas como o sigilo.
- **D) está errada:** Regimento e Código possuem funções diferentes e não são intercambiáveis.
- **Conceito cobrado:** Distinção entre Regimento Interno e Código de Ética.
- **Pegadinha usada:** Associar norma verdadeira ao objeto errado ou fundir disciplinas distintas.
- **Como pensar para acertar:** Classifique primeiro se o caso trata de estrutura do Conselho ou de conduta profissional.
- **Referência:** [Dia 5 — Fontes e hierarquia normativa](semana_01_estudo.md#s1-d5-fontes-hierarquia).

---

# Dia 6 — Administração Pública, RLM e Revisão

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões principais

### Questão 1
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

Em licitação para solução de tecnologia, a unidade requisitante indica determinada marca como única aceitável, mas não apresenta estudo que demonstre incompatibilidade das demais opções. À luz dos princípios administrativos, a providência adequada é:

A) manter a marca e classificar a justificativa como sigilosa, para evitar questionamentos de concorrentes.
B) aceitar a escolha por se tratar de decisão discricionária da área técnica, ainda que não haja motivação objetiva.
C) converter automaticamente o caso em inexigibilidade, porque produtos tecnológicos são presumidamente exclusivos.
D) exigir justificativa técnica objetiva e pertinente ao interesse público, afastando direcionamento indevido.

### Questão 2
**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Princípios da Administração Pública](semana_01_estudo.md#s1-d6-principios)

Assinale a alternativa que reúne apenas os princípios expressos no caput do art. 37 da Constituição Federal.

A) Legalidade, supremacia do interesse público, publicidade, continuidade e eficiência.
B) Legalidade, pessoalidade, moralidade, transparência e economicidade.
C) Legalidade, impessoalidade, moralidade, publicidade e eficiência.
D) Impessoalidade, autotutela, motivação, publicidade e eficiência.

### Questão 3
**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Organização administrativa](semana_01_estudo.md#s1-d6-organizacao)

Assinale a alternativa incorreta sobre Administração Direta e Indireta.

A) Autarquias são órgãos despersonalizados da Administração Direta, embora possuam autonomia financeira.
B) Autarquias, empresas públicas e sociedades de economia mista integram a Administração Indireta.
C) Secretarias e ministérios são órgãos sem personalidade jurídica própria.
D) Entidades da Administração Indireta possuem personalidade jurídica própria.

### Questão 4
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Organização administrativa](semana_01_estudo.md#s1-d6-organizacao)

O CRA-PR exerce registro e fiscalização profissional, possui personalidade jurídica de direito público e autonomia técnica, administrativa e financeira. Essa descrição o aproxima, em regra, de:

A) empresa pública prestadora de serviço econômico em regime privado.
B) órgão da Administração Direta estadual sem personalidade própria.
C) autarquia corporativa ou entidade de fiscalização profissional.
D) associação civil privada mantida apenas por contribuições voluntárias.

### Questão 5
**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos)

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
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos)

Assinale a alternativa incorreta acerca dos elementos do ato administrativo.

A) Finalidade relaciona-se ao interesse público que deve orientar o ato.
B) Motivo corresponde aos pressupostos de fato e de direito da decisão.
C) Objeto é o efeito jurídico imediato produzido pelo ato.
D) Competência transfere-se definitivamente por acordo informal, sem autorização legal.

### Questão 7
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos)

Uma autoridade remove servidor para local distante com o propósito real de puni-lo por crítica legítima, embora declare genericamente “necessidade do serviço”. O vício mais evidente recai sobre:

A) a forma, porque toda remoção exige decisão judicial.
B) a finalidade, pois a competência foi usada para perseguição pessoal.
C) o motivo, apenas porque fatos administrativos não admitem avaliação.
D) o objeto, porque remoção nunca pode alterar a lotação.

### Questão 8
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

Para contratar serviço comum de suporte técnico, com especificações usuais de mercado e disputa por lances, a modalidade em regra mais compatível é:

A) leilão.
B) pregão.
C) diálogo competitivo.
D) concurso.

### Questão 9
**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

Assinale a alternativa incorreta sobre contratação direta.

A) Na inexigibilidade, a competição é inviável e essa circunstância deve ser demonstrada.
B) Na dispensa, a competição pode ser viável, mas a lei autoriza a contratação direta em hipótese específica.
C) Dispensa e inexigibilidade são equivalentes, pois em ambas a Administração escolhe livremente não licitar.
D) A contratação direta continua exigindo processo, justificativa, motivação e controle.

### Questão 10
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

A Administração precisa contratar solução inovadora e complexa, mas ainda não consegue definir os meios técnicos aptos a atender sua necessidade. Pretende dialogar com licitantes previamente selecionados antes da apresentação das propostas finais. A modalidade descrita é:

A) concorrência com critério de maior lance.
B) diálogo competitivo.
C) concurso.
D) leilão.

### Questão 11
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

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
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

Assinale a alternativa incorreta a respeito dos critérios de julgamento.

A) O critério pode ser escolhido depois da abertura das propostas, desde que a decisão seja motivada.
B) Técnica e preço pode ponderar qualidade técnica e valor econômico quando cabível.
C) Menor preço é possível quando o objeto admite comparação objetiva e atende aos requisitos definidos.
D) Maior desconto pode incidir sobre parâmetro previamente estabelecido no edital.

### Questão 13
**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade)

Durante serviço, veículo oficial conduzido por agente público colide com automóvel particular. Para a responsabilidade objetiva do Estado por esse ato comissivo, a vítima deve demonstrar, em regra:

A) contrato anterior com a Administração e inadimplemento.
B) conduta estatal, dano e nexo causal.
C) dolo específico do agente e condenação penal.
D) culpa do serviço, ainda que não exista dano comprovado.

### Questão 14
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade)

Assinale a alternativa incorreta sobre a responsabilidade civil objetiva do Estado.

A) O dano é presumido e dispensa demonstração pela vítima.
B) Caso fortuito ou força maior podem excluir a responsabilidade quando rompem o nexo.
C) Culpa concorrente da vítima pode reduzir a indenização.
D) Culpa exclusiva da vítima pode romper o nexo causal.

### Questão 15
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade)

Uma estrutura pública apresenta risco conhecido, mas o órgão deixa de realizar manutenção que lhe competia. Na análise da omissão estatal, deve-se verificar especialmente:

A) se qualquer dano ocorreu em propriedade pública, o que basta para indenização automática.
B) se existe contrato administrativo entre o órgão e a vítima.
C) se houve condenação disciplinar prévia do servidor responsável.
D) o dever específico de agir, a possibilidade de atuação, a falha e o nexo com o dano.

### Questão 16
**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Improbidade administrativa](semana_01_estudo.md#s1-d6-improbidade)

A respeito da improbidade administrativa, assinale a alternativa correta.

A) Toda ilegalidade administrativa configura improbidade, ainda que faltem dolo e tipificação legal.
B) Nem toda ilegalidade é improbidade; exige-se conduta dolosa tipificada na lei.
C) Improbidade é matéria exclusivamente penal e pressupõe condenação criminal prévia do agente.
D) Somente enriquecimento ilícito pode constituir improbidade, ainda que haja outras categorias legais.

### Questão 17
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Improbidade administrativa](semana_01_estudo.md#s1-d6-improbidade)

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
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos)

A Administração identifica ilegalidade em ato que ela própria praticou e decide invalidá-lo, respeitados os direitos processuais pertinentes. Essa atuação decorre principalmente do poder de:

A) autotutela administrativa.
B) polícia judiciária.
C) hierarquia legislativa.
D) tutela jurisdicional.

### Questão 19
**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Poderes administrativos e agentes públicos](semana_01_estudo.md#s1-d6-poderes-agentes)

Uma candidata é contratada por uma autarquia, sob regime da CLT, para exercer atribuições permanentes sem ocupar cargo estatutário. À luz das noções de agentes públicos, ela é:

A) particular em colaboração, porque o vínculo trabalhista exclui a condição de agente público.
B) servidora estatutária ocupante de cargo efetivo, porque toda autarquia adota regime estatutário.
C) agente política ocupante de função de confiança, independentemente da forma de investidura.
D) empregada pública ocupante de emprego público e integrante da categoria ampla de agentes públicos.

### Questão 20
**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Transparência, LAI e LGPD](semana_01_estudo.md#s1-d6-transparencia)

Diante de pedido de acesso a documentos administrativos, a premissa correta é:

A) todo processo é sigiloso até autorização judicial.
B) o acesso depende sempre da demonstração de interesse jurídico individual.
C) a publicidade é regra e o sigilo, exceção que precisa de fundamento legal.
D) a Administração pode negar o pedido sem motivação quando o atendimento exigir trabalho adicional.

### Questão 21
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Transparência, LAI e LGPD](semana_01_estudo.md#s1-d6-transparencia)

Um cidadão pede cópia de planilha usada em política pública. O arquivo contém resultados estatísticos de interesse coletivo, mas também CPF, telefone e endereço dos atendidos. A solução mais compatível com LAI e LGPD é:

A) negar integralmente o acesso, porque a presença de qualquer dado pessoal torna todo o documento sigiloso.
B) fornecer as informações públicas cabíveis com anonimização ou ocultação dos dados pessoais desnecessários, motivando eventuais restrições.
C) publicar a planilha integral, pois dados mantidos pelo Estado são necessariamente públicos.
D) exigir consentimento individual de todos os titulares antes de divulgar até mesmo os dados estatísticos agregados.

### Questão 22
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Poderes administrativos e agentes públicos](semana_01_estudo.md#s1-d6-poderes-agentes)

No exercício regular do poder de polícia, uma autarquia constata infração e aplica restrição prevista em lei após procedimento próprio. A conclusão correta é:

A) a existência de competência legal elimina contraditório e ampla defesa em qualquer sanção aplicada no exercício do poder de polícia.
B) a natureza preventiva do poder de polícia dispensa motivação e proporcionalidade quando a restrição estiver prevista em ato interno.
C) toda restrição administrativa depende de condenação penal anterior, ainda que a lei atribua competência sancionadora à autarquia.
D) a Administração pode restringir direitos no interesse público, com base legal e respeito às garantias.

### Questão 23
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Poderes administrativos e agentes públicos](semana_01_estudo.md#s1-d6-poderes-agentes)

Em processo administrativo sancionador, a comissão conclui a instrução sem ouvir o interessado e propõe aplicação imediata de multa. Qual sequência corrige o vício?

A) aplicar a multa, publicar o resultado e abrir defesa apenas se houver recurso.
B) colher defesa informal depois da decisão, sem reabrir a instrução.
C) dar ciência da imputação, assegurar defesa e produção pertinente de provas e, depois, proferir decisão motivada.
D) submeter a proposta diretamente ao Judiciário, que substituirá o processo administrativo.

### Questão 24
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos)

Uma autoridade possui competência para decidir, mas indefere pedido usando apenas a frase “por interesse público”, sem indicar fatos nem fundamento jurídico. Nesse caso, a motivação é relevante porque:

A) expõe as razões de fato e de direito, permitindo controlar a legalidade e a coerência da decisão.
B) converte automaticamente uma decisão vinculada em discricionária.
C) substitui a competência e permite que qualquer servidor assine o ato.
D) torna desnecessária a existência de motivo verdadeiro, desde que o texto seja formal.

### Questão 25
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica)

Considere a proposição: “Se o edital é regular, então os critérios são públicos e objetivos”. Sua negação lógica é:

A) O edital não é regular e os critérios não são públicos nem objetivos.
B) O edital é regular e algum critério não é público ou não é objetivo.
C) Se os critérios não são públicos ou não são objetivos, então o edital não é regular.
D) O edital não é regular ou os critérios são públicos e objetivos.

### Questão 26
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica)

A negação de “Todo ato válido foi motivado ou algum recurso foi provido” é:

A) Nenhum ato válido foi motivado ou algum recurso não foi provido.
B) Algum ato válido não foi motivado e nenhum recurso foi provido.
C) Algum ato válido foi motivado e todo recurso foi improvido.
D) Nenhum ato válido foi motivado ou nenhum recurso foi provido.

### Questão 27
**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Em um grupo, 92 pessoas usam o sistema A, 71 usam o sistema B e 38 usam ambos. Quantas usam exatamente um dos dois sistemas?

A) 87.
B) 49.
C) 54.
D) 125.

### Questão 28
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Seis servidores, com produtividade uniforme, analisam 360 processos em 5 dias. Em nova etapa, dez servidores trabalharão 8 dias, mas com produtividade individual equivalente a 75% da anterior. Quantos processos serão analisados?

A) 900.
B) 600.
C) 720.
D) 576.

### Questão 29
**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Um equipamento de R$ 7.500,00 sofre aumento de 12% e, sobre o preço reajustado, recebe desconto de 10%. O preço final é:

A) R$ 7.650,00.
B) R$ 7.500,00.
C) R$ 7.560,00.
D) R$ 8.250,00.

### Questão 30
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Um serviço teve primeiro acréscimo de 25% sobre o preço original e, depois, desconto de 15% sobre o valor reajustado, passando a custar R$ 4.250,00. O preço original era:

A) R$ 4.000,00.
B) R$ 3.612,50.
C) R$ 4.250,00.
D) R$ 5.000,00.

### Questão 31
**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Quatro técnicos resolvem 160 chamados em 5 horas. Em outro turno, cinco técnicos trabalham 6 horas, mas cada um produz apenas 80% do ritmo anterior. A produção esperada é:

A) 240 chamados.
B) 160 chamados.
C) 200 chamados.
D) 192 chamados.

### Questão 32
**Nível:** Médio
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Uma progressão aritmética tem primeiro termo 7 e razão 4. A soma dos 20 primeiros termos é:

A) 83.
B) 830.
C) 940.
D) 900.

### Questão 33
**Nível:** Médio
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Em uma progressão geométrica, o primeiro termo é 3 e a razão é 2. A soma dos oito primeiros termos é:

A) 384.
B) 765.
C) 768.
D) 1.533.

### Questão 34
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** Primeira passagem
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Uma urna contém 5 crachás azuis e 3 vermelhos. Três crachás são retirados simultaneamente. A probabilidade de saírem exatamente dois azuis e um vermelho é:

A) 3/8.
B) 5/14.
C) 15/28.
D) 9/28.

### Questão 35
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Entre 10 servidores, 2 são analistas. Três servidores distintos são sorteados, sem reposição. A probabilidade de o grupo conter pelo menos um analista é:

A) 8/15.
B) 2/5.
C) 7/15.
D) 1/5.

### Questão 36
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica)

A negação de “O relatório foi entregue e o protocolo foi gerado ou a assinatura foi validada”, considerando a estrutura “R e (P ou A)”, é:

A) O relatório não foi entregue ou (o protocolo não foi gerado e a assinatura não foi validada).
B) O relatório não foi entregue ou o protocolo não foi gerado ou a assinatura não foi validada.
C) (O relatório não foi entregue e o protocolo não foi gerado) ou a assinatura não foi validada.
D) O relatório foi entregue e o protocolo não foi gerado e a assinatura não foi validada.

### Questão 37
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica)

São verdadeiras as proposições: “Se existe backup íntegro, então a verificação termina sem erro” e “Se a verificação termina sem erro, então a restauração é possível”. Sabendo que a restauração não é possível, conclui-se validamente que:

A) a primeira condicional é falsa.
B) existe backup íntegro, mas não foi usado.
C) não existe backup íntegro.
D) a verificação terminou sem erro.

### Questão 38
**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica)

Para proposições simples P, Q e R, em quantas das oito valorações possíveis a expressão `(P → Q) e (Q → R)` é verdadeira?

A) 6.
B) 3.
C) 5.
D) 4.

### Questão 39
**Nível:** Difícil
**Uso:** Essenciais
**Momento:** D+2
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Em 200 servidores, 110 usam A, 90 usam B e 70 usam C. Usam A e B, 45; A e C, 30; B e C, 25; e os três sistemas, 15. Quantos usam pelo menos um dos sistemas?

A) 170.
B) 200.
C) 155.
D) 185.

### Questão 40
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

Uma unidade planeja duas contratações previsíveis e de mesma natureza, mas propõe separá-las artificialmente para que cada valor se enquadre em hipótese de dispensa. Assinale a alternativa incorreta.

A) O planejamento deve considerar a necessidade global e a natureza dos objetos.
B) O fracionamento é legítimo sempre que cada processo isolado permanecer abaixo do limite legal.
C) A contratação direta não elimina motivação, justificativa e controle.
D) O procedimento deve preservar isonomia, planejamento e finalidade pública.

### Questão 41
**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes)

Edital para serviço comum fixa requisitos técnicos mínimos e menor preço como critério. Após a abertura, a proposta de menor preço descumpre requisito essencial, e a comissão cogita dispensá-lo apenas para preservar essa proposta. A solução juridicamente mais adequada é:

A) ignorar o requisito essencial, pois o menor preço sempre prevalece sobre especificações técnicas previamente divulgadas.
B) aplicar o edital; se o requisito for ilegal, corrigir o procedimento impessoalmente, não dispensá-lo só para um licitante.
C) alterar retroativamente o edital para dispensar o requisito apenas nessa proposta, mantendo os atos praticados e afastando nova publicidade.
D) classificar a proposta por economicidade mesmo sem atendimento ao objeto, substituindo o julgamento objetivo por conveniência da comissão.

### Questão 42
**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade)

Veículo oficial em serviço causa dano a particular. A prova demonstra nexo causal, culpa concorrente da vítima e culpa do agente público. A alternativa correta é:

A) a responsabilidade pode ser objetiva; a culpa concorrente atenua a indenização, e o regresso exige dolo ou culpa.
B) A culpa concorrente elimina necessariamente toda responsabilidade do Estado, embora preserve ação regressiva automática contra o agente.
C) A responsabilidade objetiva torna dispensáveis a prova do dano e do nexo causal e impede considerar qualquer causa concorrente.
D) O Estado somente indeniza depois da condenação pessoal do agente, mas pode exercer regresso sem demonstrar dolo ou culpa.

### Questão 43
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos)

A Administração descobre que licença foi concedida por autoridade absolutamente incompetente. Além disso, a licença tornou-se inconveniente à política pública atual. Para desfazer o ato, deve:

A) revogá-lo exclusivamente por conveniência, pois o mérito absorve qualquer ilegalidade.
B) anulá-lo pelo vício, observadas as garantias; revogação não encobre ilegalidade.
C) convalidá-lo obrigatoriamente e, em seguida, revogá-lo, independentemente da natureza do vício.
D) aguardar decisão judicial, porque a Administração não pode invalidar ato próprio favorável.

### Questão 44
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos)

A lei permite multa entre R$ 2.000,00 e R$ 20.000,00 conforme gravidade e circunstâncias. A autoridade aplica o máximo para retaliar crítica do administrado e usa motivação genérica. A conclusão correta é:

A) a discricionariedade não autoriza desvio de finalidade e exige motivação conforme os critérios legais.
B) a existência de faixa legal torna a escolha do valor imune ao controle de finalidade, motivação e proporcionalidade.
C) o valor máximo é sempre válido quando está dentro da faixa, ainda que a motivação não relacione gravidade e circunstâncias.
D) em ato discricionário, o controle pode alcançar apenas a competência da autoridade, nunca finalidade, motivo ou proporcionalidade.

### Questão 45
**Nível:** Muito difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Para comparar duas coortes independentes, sem transferência de pendências entre elas, um setor recebeu 240 processos na coorte do primeiro mês e concluiu 60%, restando 96. Na coorte do segundo mês, recebeu 25% mais processos do que na primeira, concluiu inicialmente 72% e, depois, concluiu 25% dos que ainda estavam pendentes dessa segunda coorte. Quantos permaneceram pendentes na segunda coorte e qual foi a redução percentual desse saldo em relação aos 96 da primeira?

A) 84 processos e 12,5%.
B) 72 processos e 25%.
C) 63 processos e 25%.
D) 63 processos e 34,375%.

### Questão 46
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Três servidores analisam 90 processos em 6 dias. Cinco servidores trabalharão 8 dias no mesmo ritmo bruto, mas 20% de sua capacidade será consumida por retrabalho. Quantos processos líquidos serão concluídos?

A) 180.
B) 200.
C) 150.
D) 160.

### Questão 47
**Nível:** Muito difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Considere os múltiplos positivos de 5 até 200, inclusive, que não são múltiplos de 10. Excluindo também, desse conjunto, os números divisíveis por 3, qual é a soma dos termos restantes?

A) 2.000.
B) 1.260.
C) 1.265.
D) 735.

### Questão 48
**Nível:** Muito difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Uma quantidade passou, nesta ordem, por três operações: aumento de 20%, subtração de 18 unidades e multiplicação do resultado por 2. O valor final foi 132. Aplicando o princípio da regressão ou reversão, qual era a quantidade inicial?

A) 44.
B) 55.
C) 84.
D) 70.

### Questão 49
**Nível:** Difícil
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos)

Em uma equipe, a razão entre analistas e técnicos é 3:5. Após a contratação de 6 analistas, sem mudança no número de técnicos, a razão passa a 9:10. Quantos servidores havia inicialmente?

A) 32.
B) 40.
C) 48.
D) 24.

### Questão 50
**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica)

Considere P falsa, Q verdadeira e R falsa. O valor lógico de `[(P ou Q) → R] se e somente se [Q e (não R)]` é:

A) indeterminado, pois o valor de P impede decidir a bicondicional.
B) verdadeiro, pois os dois lados da bicondicional são verdadeiros.
C) falso, pois o lado esquerdo é falso e o lado direito é verdadeiro.
D) verdadeiro, pois a falsidade de R torna falsa apenas a segunda parcela.

## Questões complementares do Dia 6

#### Extra Dia 6.1

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Abrangência do Código de Ética
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

Durante fiscalização regular, o fiscalizado discorda da interpretação do CRA. A postura compatível com o material é:

A) reter os documentos até manifestação prévia do CFA, sem atender à diligência regional.
B) recusar a diligência, porque a defesa suspende automaticamente o poder fiscalizatório.
C) atender às solicitações pertinentes do CRA e impugnar formalmente o que considerar indevido.
D) usar registro de terceiro como prova provisória de regularidade enquanto discute a interpretação.

#### Extra Dia 6.6

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Hierarquia normativa e limites do poder regulamentar no Sistema CFA/CRAs
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

Um ato interno de Conselho Regional pretende ampliar o conjunto de atividades profissionais para além da Lei nº 4.769/1965, invocando como fundamento geral o Decreto nº 61.934/1967. A conclusão adequada é:

A) prevalece o ato regional, por autonomia administrativa, mesmo sem base na lei.
B) o decreto pode criar obrigação primária, e o ato regional apenas a reproduz.
C) decreto e ato regional devem respeitar a lei e não podem ampliar, sem base legal, o campo profissional.
D) o ato regional posterior prevalece pela especialidade, ainda que contrarie a lei.

#### Extra Dia 6.7

**Dia:** 6
**Bloco:** 4 — Matéria fixa ou revisão programada
**Matéria:** Legislação CRA/CFA
**Assunto:** Roteiro de resolução em legislação profissional
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Nível:** Médio
**Uso:** Simulado
**Momento:** Ciclo seguinte
**Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4)

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
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 1 — Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade)

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
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 1 — Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho)

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
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
**Referência:** [Dia 2 — Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento)

No escalonamento Round Robin, qual afirmação descreve corretamente o papel do quantum?

A) É uma fatia de CPU; quantum curto aumenta trocas, e quantum longo pode piorar a resposta.
B) É prioridade fixa; impede preempção e mantém o processo até seu encerramento.
C) É o surto completo; a fila só é retomada quando o processo se bloqueia ou termina.
D) É uma cota de memória virtual; define páginas sem afetar a alternância da CPU.

#### Extra Dia 6.14

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** Page fault e paginação
**Nível:** Médio
**Uso:** Aprofundamento
**Momento:** Antes de D+7
**Referência:** [Dia 2 — Memória virtual, paginação e thrashing](semana_01_estudo.md#s1-d2-memoria-virtual)

Durante a execução, um processo acessa uma página válida de seu espaço virtual que não está carregada na memória física naquele instante. A ocorrência descrita é:

A) necessariamente um erro fatal de segmentação, pois paginação não admite carregamento posterior.
B) um page fault, evento normal quando o sistema precisa carregar uma página virtual válida.
C) um deadlock, porque o processo sempre passa a esperar circularmente por outro processo.
D) um caso de journaling, mecanismo responsável por traduzir endereços virtuais em físicos.

#### Extra Dia 6.15

**Dia:** 6
**Bloco:** 6 — Revisão ativa e caderno de erros
**Matéria:** Revisão ativa integrada
**Assunto:** WHERE, GROUP BY e HAVING
**Nível:** Difícil
**Uso:** Aprofundamento
**Momento:** Antes de D+7
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
**Nível:** Médio
**Uso:** Revisão
**Momento:** D+7
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
**Nível:** Difícil
**Uso:** Revisão
**Momento:** D+7
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
**Uso:** Simulado
**Momento:** Ciclo seguinte
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
**Nível:** Difícil
**Uso:** Simulado
**Momento:** Ciclo seguinte
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
**Uso:** Simulado
**Momento:** Ciclo seguinte
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

### Gabarito das questões complementares do Dia 6

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
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **A) está errada:** Sigilo não serve para ocultar ausência de justificativa nem para afastar controle.
- **B) está errada:** Discricionariedade técnica continua sujeita a motivação, impessoalidade e competitividade.
- **C) está errada:** Tecnologia não gera presunção de fornecedor exclusivo nem inexigibilidade automática.
- **D) está correta:** A indicação de marca exige fundamento objetivo ligado à necessidade pública, sem favorecimento.
- **Conceito cobrado:** Impessoalidade, motivação e competitividade.
- **Pegadinha usada:** Tratar preferência técnica não demonstrada como liberdade discricionária.
- **Como pensar para acertar:** Procure uma justificativa verificável que ligue a restrição ao objeto e ao interesse público.

### Comentário da Questão 2

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Princípios da Administração Pública](semana_01_estudo.md#s1-d6-principios).
- **A) está errada:** Supremacia e continuidade são princípios estudados, mas não compõem o conjunto expresso do caput.
- **B) está errada:** Pessoalidade não integra o rol expresso; transparência e economicidade, embora relevantes, não substituem impessoalidade, publicidade e eficiência na enumeração do caput.
- **C) está correta:** A alternativa reproduz os cinco princípios expressos, memorizados por LIMPE.
- **D) está errada:** Autotutela e motivação não substituem legalidade e moralidade na sigla LIMPE.
- **Conceito cobrado:** Princípios expressos do art. 37.
- **Pegadinha usada:** Misturar princípios implícitos ou conceitos correlatos com o rol expresso.
- **Como pensar para acertar:** Recupere a sigla LIMPE: legalidade, impessoalidade, moralidade, publicidade e eficiência.

### Comentário da Questão 3

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Organização administrativa](semana_01_estudo.md#s1-d6-organizacao).
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) deve ser marcada:** A afirmação é falsa. Autarquia é entidade com personalidade jurídica própria, não órgão despersonalizado da Direta.
- **B) não deve ser marcada:** A afirmação é verdadeira. As três espécies mencionadas pertencem à Administração Indireta.
- **C) não deve ser marcada:** A afirmação é verdadeira. Órgãos da Administração Direta não possuem personalidade própria.
- **D) não deve ser marcada:** A afirmação é verdadeira. Personalidade própria é característica das entidades descentralizadas.
- **Conceito cobrado:** Administração Direta e Indireta.
- **Pegadinha usada:** Confundir órgão com entidade e autonomia com personalidade.
- **Como pensar para acertar:** Pergunte se o sujeito possui personalidade jurídica: órgão não; entidade da Indireta, sim.

### Comentário da Questão 4

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Organização administrativa](semana_01_estudo.md#s1-d6-organizacao).
- **A) está errada:** Empresa pública possui personalidade de direito privado e não corresponde à descrição.
- **B) está errada:** Órgão da Direta não tem personalidade jurídica própria.
- **C) está correta:** Conselho profissional é tratado, em regra, como autarquia corporativa de fiscalização.
- **D) está errada:** A função pública e o regime descrito afastam a natureza de associação voluntária.
- **Conceito cobrado:** Natureza dos conselhos profissionais.
- **Pegadinha usada:** Confundir autarquia corporativa com empresa estatal, órgão ou associação privada.
- **Como pensar para acertar:** Associe personalidade pública, autonomia e poder de fiscalização a entidade autárquica.

### Comentário da Questão 5

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos).
- **A) está errada:** A assertiva III torna a alternativa incorreta, pois a autoexecutoriedade não é universal.
- **B) está errada:** A assertiva I também é correta e não pode ser excluída.
- **C) está errada:** A assertiva III continua incorreta nesta combinação.
- **D) está correta:** I e II estão corretas; III generaliza indevidamente um atributo.
- **Conceito cobrado:** Elementos e atributos dos atos administrativos.
- **Pegadinha usada:** Transformar atributo presente quando cabível em atributo de todos os atos.
- **Como pensar para acertar:** Avalie cada assertiva: os elementos são clássicos e a presunção é geral, mas a autoexecutoriedade depende do caso.

### Comentário da Questão 6

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos).
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não deve ser marcada:** A afirmação é verdadeira. Finalidade deve permanecer vinculada ao interesse público.
- **B) não deve ser marcada:** A afirmação é verdadeira. Motivo reúne os pressupostos fáticos e jurídicos.
- **C) não deve ser marcada:** A afirmação é verdadeira. Objeto corresponde ao efeito jurídico do ato.
- **D) deve ser marcada:** A afirmação é falsa. Competência decorre da norma e não pode ser transferida definitivamente por pacto informal.
- **Conceito cobrado:** Elementos do ato administrativo.
- **Pegadinha usada:** Tratar competência legal como disponibilidade pessoal do agente.
- **Como pensar para acertar:** Associe cada elemento à pergunta correspondente e desconfie de transferência sem base normativa.

### Comentário da Questão 7

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos).
- **A) está errada:** O enunciado não indica exigência judicial de forma.
- **B) está correta:** Usar competência para punir crítica desvia o ato de sua finalidade pública.
- **C) está errada:** Fatos e fundamentos podem ser controlados, mas o núcleo do caso é a perseguição.
- **D) está errada:** Remoção pode existir juridicamente; o problema está no propósito concreto.
- **Conceito cobrado:** Desvio de finalidade.
- **Pegadinha usada:** Aceitar a finalidade declarada sem confrontá-la com o objetivo real.
- **Como pensar para acertar:** Pergunte para que o ato foi efetivamente praticado, e não apenas qual justificativa foi escrita.

### Comentário da Questão 8

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **A) está errada:** Leilão destina-se à alienação de bens.
- **B) está correta:** Pregão é associado a bens e serviços comuns com disputa objetiva.
- **C) está errada:** Diálogo competitivo atende contratações complexas que exigem construção de soluções.
- **D) está errada:** Concurso seleciona trabalho técnico, científico ou artístico.
- **Conceito cobrado:** Modalidade pregão.
- **Pegadinha usada:** Escolher modalidade pelo valor ou pelo caráter tecnológico, sem identificar o objeto comum.
- **Como pensar para acertar:** Comece pelo objeto: sendo serviço comum, examine o cabimento do pregão.

### Comentário da Questão 9

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não deve ser marcada:** A afirmação é verdadeira. A inviabilidade precisa ser demonstrada, não presumida.
- **B) não deve ser marcada:** A afirmação é verdadeira. A afirmação descreve corretamente a lógica da dispensa.
- **C) deve ser marcada:** A afirmação é falsa. Dispensa pressupõe hipótese legal com competição possível; inexigibilidade, inviabilidade de competição.
- **D) não deve ser marcada:** A afirmação é verdadeira. Contratação direta não significa contratação sem processo.
- **Conceito cobrado:** Dispensa e inexigibilidade.
- **Pegadinha usada:** Usar ‘sem licitação’ para tratar institutos distintos como sinônimos.
- **Como pensar para acertar:** Pergunte se a competição é viável: se sim, pode haver dispensa legal; se não, inexigibilidade.

### Comentário da Questão 10

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **A) está errada:** Maior lance é critério ligado especialmente ao leilão, não modalidade adequada ao caso.
- **B) está correta:** A descrição corresponde ao diálogo competitivo.
- **C) está errada:** Concurso seleciona trabalho técnico ou artístico por prêmio.
- **D) está errada:** Leilão aliena bens e não promove diálogo para desenvolver solução.
- **Conceito cobrado:** Diálogo competitivo.
- **Pegadinha usada:** Confundir complexidade do objeto com concorrência ou concurso sem observar a fase de diálogo.
- **Como pensar para acertar:** Procure os sinais ‘solução ainda não definida’ e ‘diálogo com selecionados’.

### Comentário da Questão 11

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **A) está errada:** A assertiva III viola vinculação ao edital e julgamento objetivo.
- **B) está errada:** A assertiva III também torna essa combinação incorreta.
- **C) está correta:** I e II expressam vinculação e prévia definição dos critérios.
- **D) está errada:** Nem todas estão corretas, pois o critério não pode mudar após conhecer propostas.
- **Conceito cobrado:** Vinculação ao edital e julgamento objetivo.
- **Pegadinha usada:** Apresentar mudança posterior como exercício legítimo de conveniência.
- **Como pensar para acertar:** Critérios devem existir antes da competição e valer igualmente para todos.

### Comentário da Questão 12

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) deve ser marcada:** A afirmação é falsa. Escolher critério após conhecer propostas viola julgamento objetivo e vinculação.
- **B) não deve ser marcada:** A afirmação é verdadeira. Técnica e preço é critério legal quando a ponderação é cabível.
- **C) não deve ser marcada:** A afirmação é verdadeira. Menor preço pode ser usado com requisitos objetivos de qualidade.
- **D) não deve ser marcada:** A afirmação é verdadeira. Maior desconto incide sobre parâmetro previamente definido.
- **Conceito cobrado:** Critérios de julgamento.
- **Pegadinha usada:** Confundir motivação posterior com autorização para mudar as regras da disputa.
- **Como pensar para acertar:** O critério deve ser definido no edital, antes de a Administração conhecer as propostas.

### Comentário da Questão 13

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade).
- **A) está errada:** Responsabilidade extracontratual não exige contrato com a vítima.
- **B) está correta:** Conduta, dano e nexo causal são requisitos centrais do regime objetivo.
- **C) está errada:** Dolo e condenação penal não são pressupostos da pretensão da vítima contra o Estado.
- **D) está errada:** Sem dano não há dever de indenizar; culpa do serviço não é exigida em todo ato comissivo.
- **Conceito cobrado:** Responsabilidade objetiva por ato comissivo.
- **Pegadinha usada:** Confundir ausência de prova de culpa com ausência de dano ou nexo.
- **Como pensar para acertar:** A vítima não precisa provar culpa, mas deve ligar a atuação estatal ao dano.

### Comentário da Questão 14

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade).
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) deve ser marcada:** A afirmação é falsa. Responsabilidade objetiva não presume a existência do dano.
- **B) não deve ser marcada:** A afirmação é verdadeira. Eventos externos podem excluir responsabilidade se forem causalmente decisivos.
- **C) não deve ser marcada:** A afirmação é verdadeira. Culpa concorrente pode reduzir, sem necessariamente eliminar, a indenização.
- **D) não deve ser marcada:** A afirmação é verdadeira. Culpa exclusiva pode romper totalmente o nexo.
- **Conceito cobrado:** Nexo causal e excludentes.
- **Pegadinha usada:** Interpretar ‘objetiva’ como ‘automática’.
- **Como pensar para acertar:** Separe culpa do agente, dispensada perante a vítima, de dano e nexo, que continuam necessários.

### Comentário da Questão 15

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade).
- **A) está errada:** Dano em estrutura pública não basta, isoladamente, para responsabilização automática.
- **B) está errada:** Contrato com a vítima não é requisito geral.
- **C) está errada:** Condenação disciplinar prévia não condiciona a análise civil.
- **D) está correta:** Omissão exige investigar dever e possibilidade de agir, falha e relação causal.
- **Conceito cobrado:** Responsabilidade por omissão estatal.
- **Pegadinha usada:** Aplicar automaticamente a mesma fórmula de ato comissivo a qualquer omissão.
- **Como pensar para acertar:** Identifique o dever concreto de proteção ou manutenção e sua conexão com o dano.

### Comentário da Questão 16

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Improbidade administrativa](semana_01_estudo.md#s1-d6-improbidade).
- **A) está errada:** Irregularidade formal pode existir sem os requisitos da improbidade.
- **B) está correta:** A caracterização atual exige conduta dolosa enquadrada em tipo previsto na lei.
- **C) está errada:** A ação de improbidade não se confunde com persecução exclusivamente penal.
- **D) está errada:** Há categorias além do enriquecimento ilícito, como lesão ao erário e violação de princípios.
- **Conceito cobrado:** Ilegalidade versus improbidade.
- **Pegadinha usada:** Converter todo erro administrativo em ato de improbidade.
- **Como pensar para acertar:** Exija enquadramento legal e elemento subjetivo antes de concluir pela improbidade.

### Comentário da Questão 17

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Improbidade administrativa](semana_01_estudo.md#s1-d6-improbidade).
- **A) está correta:** I reconhece categorias legais e III preserva devido processo; II cria automatismo indevido.
- **B) está errada:** A assertiva II é falsa, impedindo a correção de todas.
- **C) está errada:** A combinação inclui a falsa assertiva II.
- **D) está errada:** A assertiva I é correta e não pode ser excluída.
- **Conceito cobrado:** Categorias e garantias na improbidade.
- **Pegadinha usada:** Tratar divergência técnica razoável como dolo ou má-fé automática.
- **Como pensar para acertar:** Analise o enquadramento e o elemento subjetivo, sem dispensar processo e defesa.

### Comentário da Questão 18

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos).
- **A) está correta:** Autotutela permite à Administração controlar e invalidar seus próprios atos ilegais.
- **B) está errada:** Polícia judiciária não descreve o controle interno do ato administrativo.
- **C) está errada:** Hierarquia legislativa não é poder administrativo de desfazimento.
- **D) está errada:** Tutela jurisdicional é exercida pelo Judiciário, não pela própria Administração.
- **Conceito cobrado:** Autotutela e anulação.
- **Pegadinha usada:** Confundir controle administrativo próprio com controle judicial.
- **Como pensar para acertar:** Se a Administração revê o próprio ato por ilegalidade, associe a autotutela.

### Comentário da Questão 19

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Poderes administrativos e agentes públicos](semana_01_estudo.md#s1-d6-poderes-agentes).
- **A) está errada:** Empregado público mantém vínculo com a Administração e integra a categoria ampla de agente público.
- **B) está errada:** O enunciado informa vínculo celetista e emprego público, não cargo estatutário.
- **C) está errada:** A contratação descrita não transforma a empregada em agente política nem em ocupante de função de confiança.
- **D) está correta:** Quem é contratado sob a CLT para emprego público é empregado público e também agente público em sentido amplo.
- **Conceito cobrado:** Agentes públicos: cargo, emprego e função.
- **Pegadinha usada:** Tratar agente público como sinônimo exclusivo de servidor estatutário.
- **Como pensar para acertar:** Identifique primeiro a natureza do vínculo e depois a posição dentro da categoria ampla de agentes públicos.

### Comentário da Questão 20

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Transparência, LAI e LGPD](semana_01_estudo.md#s1-d6-transparencia).
- **A) está errada:** Sigilo não é presumido para todos os processos.
- **B) está errada:** A LAI não condiciona todo acesso à demonstração de interesse pessoal.
- **C) está correta:** A regra é transparência; restrição precisa de fundamento legal.
- **D) está errada:** Carga de trabalho não autoriza negativa imotivada de acesso.
- **Conceito cobrado:** Publicidade e acesso à informação.
- **Pegadinha usada:** Tratar sigilo ou interesse jurídico como regra geral.
- **Como pensar para acertar:** Parta do acesso e verifique depois se há exceção legal justificável.

### Comentário da Questão 21

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Transparência, LAI e LGPD](semana_01_estudo.md#s1-d6-transparencia).
- **A) está errada:** A presença de dado pessoal não torna necessariamente sigiloso todo o conteúdo público.
- **B) está correta:** É possível compatibilizar transparência e proteção mediante seleção, anonimização ou ocultação motivada.
- **C) está errada:** Custódia estatal não converte CPF, telefone e endereço em dados de divulgação irrestrita.
- **D) está errada:** Dados agregados podem ser divulgados sem exigir consentimento individual em toda hipótese, observada a base jurídica.
- **Conceito cobrado:** Compatibilização entre LAI e LGPD.
- **Pegadinha usada:** Escolher entre transparência total e sigilo total, como se não houvesse tratamento proporcional.
- **Como pensar para acertar:** Separe o conteúdo público dos identificadores pessoais e divulgue apenas o necessário e juridicamente cabível.

### Comentário da Questão 22

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Poderes administrativos e agentes públicos](semana_01_estudo.md#s1-d6-poderes-agentes).
- **A) está errada:** Em sanções, a competência não afasta automaticamente contraditório e defesa.
- **B) está errada:** Caráter preventivo não elimina motivação nem proporcionalidade.
- **C) está errada:** Restrição administrativa não depende sempre de processo penal.
- **D) está correta:** Poder de polícia admite limitações legais e proporcionais, com garantias compatíveis com o caso.
- **Conceito cobrado:** Poder de polícia e limites jurídicos.
- **Pegadinha usada:** Confundir poder administrativo com autorização irrestrita.
- **Como pensar para acertar:** Verifique competência, fundamento legal, finalidade, proporcionalidade e procedimento.

### Comentário da Questão 23

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Poderes administrativos e agentes públicos](semana_01_estudo.md#s1-d6-poderes-agentes).
- **A) está errada:** Defesa posterior à sanção não corrige, como regra, a falta de participação antes da decisão.
- **B) está errada:** Defesa informal posterior, sem reabertura da instrução, não assegura contraditório efetivo antes da decisão sancionadora.
- **C) está correta:** Ciência, defesa, prova pertinente e decisão motivada compõem a sequência regular.
- **D) está errada:** O Judiciário não substitui obrigatoriamente toda instrução administrativa.
- **Conceito cobrado:** Contraditório e ampla defesa no processo sancionador.
- **Pegadinha usada:** Tratar recurso posterior como substituto suficiente da defesa prévia.
- **Como pensar para acertar:** A sanção deve resultar de instrução participativa e terminar em decisão fundamentada.

### Comentário da Questão 24

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos).
- **A) está correta:** A motivação permite examinar fatos, fundamentos, coerência e finalidade.
- **B) está errada:** Expor razões não altera a natureza vinculada ou discricionária prevista em lei.
- **C) está errada:** Motivação não cria competência para quem não a possui.
- **D) está errada:** Texto formal não substitui motivo verdadeiro nem sana sua inexistência.
- **Conceito cobrado:** Motivo e motivação.
- **Pegadinha usada:** Confundir exteriorização das razões com elemento capaz de curar qualquer vício.
- **Como pensar para acertar:** Motivo é a base fática e jurídica; motivação é sua exposição controlável.

### Comentário da Questão 25

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica).
- **A) está errada:** A negação da condicional mantém o antecedente verdadeiro, não o nega.
- **B) está correta:** Negar `E → (P e O)` resulta em `E e não(P e O)`, isto é, `E e (não P ou não O)`.
- **C) está errada:** A contrapositiva é equivalente à original, não sua negação.
- **D) está errada:** A disjunção proposta equivale à própria condicional em outra forma.
- **Conceito cobrado:** Negação de condicional com consequente composto.
- **Pegadinha usada:** Negar todas as parcelas sem aplicar a forma `P e não Q`.
- **Como pensar para acertar:** Primeiro negue a condicional; depois aplique De Morgan ao consequente.

### Comentário da Questão 26

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica).
- **A) está errada:** A alternativa mantém uma disjunção e troca quantificadores de modo inadequado.
- **B) está correta:** Negar a disjunção exige negar ambas as parcelas e ligá-las por conjunção.
- **C) está errada:** Ela afirma existência positiva de motivação e não nega corretamente a segunda parcela.
- **D) está errada:** Negar “todo” não produz “nenhum”, e o conectivo final deveria ser uma conjunção.
- **Conceito cobrado:** Negação de quantificadores e disjunção.
- **Pegadinha usada:** Aplicar De Morgan sem inverter corretamente ‘todo’ e ‘algum’.
- **Como pensar para acertar:** Negue cada lado: ‘todo’ vira ‘algum não’; ‘algum’ vira ‘nenhum’; ‘ou’ vira ‘e’.

### Comentário da Questão 27

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está correta:** Exatamente um é `(92 - 38) + (71 - 38) = 54 + 33 = 87`.
- **B) está errada:** 49 não corresponde à retirada da interseção de ambos os conjuntos.
- **C) está errada:** 54 é apenas a parcela que usa A e não B.
- **D) está errada:** 125 é o total da união `92 + 71 - 38`, não o número em exatamente um.
- **Conceito cobrado:** Conjuntos: exatamente um.
- **Pegadinha usada:** Confundir união, diferença de um conjunto e exatamente um.
- **Como pensar para acertar:** Retire a interseção de cada conjunto e some as duas partes exclusivas.

### Comentário da Questão 28

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 900 ignora a queda de produtividade individual.
- **B) está errada:** 600 não combina corretamente servidores, dias e produtividade.
- **C) está correta:** A taxa original é 12 processos por servidor-dia; a nova é 9, gerando `10 × 8 × 9 = 720`.
- **D) está errada:** 576 aplica a redução a base ou período inadequado.
- **Conceito cobrado:** Regra de três composta com produtividade.
- **Pegadinha usada:** Aumentar pessoas e tempo sem ajustar a produtividade relativa.
- **Como pensar para acertar:** Calcule a taxa por servidor-dia, aplique 75% e só então multiplique pelos novos recursos.

### Comentário da Questão 29

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** Esse valor resulta de compensação linear inadequada entre 12% e 10%.
- **B) está errada:** Aumento e desconto de percentuais diferentes não retornam ao preço inicial.
- **C) está correta:** O preço passa a 8.400 e depois a `8.400 × 0,90 = 7.560`.
- **D) está errada:** 8.250 corresponde a operação percentual diversa.
- **Conceito cobrado:** Percentuais sucessivos.
- **Pegadinha usada:** Somar e subtrair percentuais como se incidissem sobre a mesma base.
- **Como pensar para acertar:** Aplique os fatores na ordem: `7.500 × 1,12 × 0,90`.

### Comentário da Questão 30

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está correta:** O fator acumulado é `1,25 × 0,85 = 1,0625`; `4.250 ÷ 1,0625 = 4.000`.
- **B) está errada:** O cálculo usa apenas uma das transformações e não recupera a base.
- **C) está errada:** R$ 4.250,00 é o valor final, não o original.
- **D) está errada:** R$ 5.000,00 seria o valor antes do desconto, mas já depois do aumento.
- **Conceito cobrado:** Porcentagem reversa com fatores sucessivos.
- **Pegadinha usada:** Voltar ao preço original somando ou subtraindo as taxas do valor final.
- **Como pensar para acertar:** Monte o fator acumulado e divida o preço final por ele.

### Comentário da Questão 31

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 240 seria a produção com ritmo integral, sem redução a 80%.
- **B) está errada:** 160 ignora a ampliação de horas e técnicos.
- **C) está errada:** 200 aplica ajuste parcial e não usa a taxa por técnico-hora.
- **D) está correta:** A taxa é 8 chamados por técnico-hora; `8 × 0,8 × 5 × 6 = 192`.
- **Conceito cobrado:** Produtividade composta com fator de eficiência.
- **Pegadinha usada:** Aplicar o percentual ao total antigo em vez de à taxa individual.
- **Como pensar para acertar:** Encontre a produtividade unitária, ajuste-a e multiplique pelo novo total de técnico-horas.

### Comentário da Questão 32

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 83 é o vigésimo termo, não a soma.
- **B) está errada:** 830 resulta de usar extremos ou número de termos incorretamente.
- **C) está errada:** 940 excede a soma correta.
- **D) está correta:** `a20 = 7 + 19×4 = 83`; logo `S20 = (7+83)×20/2 = 900`.
- **Conceito cobrado:** Termo e soma de progressão aritmética.
- **Pegadinha usada:** Calcular corretamente o último termo e marcá-lo como soma.
- **Como pensar para acertar:** Calcule `a20` e depois aplique a média dos extremos vezes o número de termos.

### Comentário da Questão 33

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 384 é o oitavo termo da PG, não sua soma.
- **B) está correta:** A soma é `3(2^8 - 1)/(2 - 1) = 3×255 = 765`.
- **C) está errada:** 768 confunde a soma com `3×2^8`.
- **D) está errada:** 1.533 corresponde a outra quantidade de termos.
- **Conceito cobrado:** Soma finita de progressão geométrica.
- **Pegadinha usada:** Trocar termo geral pela soma acumulada.
- **Como pensar para acertar:** Use a fórmula da soma e confirme que há oito termos, de 3 a 384.

### Comentário da Questão 34

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** Primeira passagem.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 3/8 não considera a retirada conjunta de três crachás.
- **B) está errada:** 5/14 equivale a 10/28 e subconta as combinações.
- **C) está correta:** Há `C(5,2)×C(3,1)=30` casos favoráveis em `C(8,3)=56`; a razão é `15/28`.
- **D) está errada:** 9/28 não corresponde à contagem combinatória.
- **Conceito cobrado:** Probabilidade hipergeométrica.
- **Pegadinha usada:** Multiplicar probabilidades sem considerar as diferentes ordens ou combinações.
- **Como pensar para acertar:** Conte combinações favoráveis e divida pelo total de grupos de três.

### Comentário da Questão 35

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está correta:** Use o complemento: `1 - C(8,3)/C(10,3) = 1 - 56/120 = 8/15`.
- **B) está errada:** 2/5 não representa três retiradas sem reposição.
- **C) está errada:** 7/15 não é o complemento correto do evento sem analistas.
- **D) está errada:** 1/5 é a proporção de analistas em uma retirada única.
- **Conceito cobrado:** Probabilidade pelo evento complementar.
- **Pegadinha usada:** Usar a proporção da primeira retirada para um grupo de três.
- **Como pensar para acertar:** É mais simples calcular ‘nenhum analista’ e subtrair o resultado de 1.

### Comentário da Questão 36

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica).
- **A) está correta:** `não[R e (P ou A)] = não R ou (não P e não A)`.
- **B) está errada:** A alternativa nega a disjunção interna de forma incompleta, mantendo ‘ou’.
- **C) está errada:** A negação externa de uma conjunção pede disjunção, não conjunção.
- **D) está errada:** A alternativa mantém o relatório entregue, contrariando uma das possibilidades da negação.
- **Conceito cobrado:** Lei de De Morgan em expressão aninhada.
- **Pegadinha usada:** Trocar apenas um conectivo ou ignorar os parênteses.
- **Como pensar para acertar:** Negue de fora para dentro: primeiro a conjunção; depois a disjunção interna.

### Comentário da Questão 37

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica).
- **A) está errada:** As condicionais podem permanecer verdadeiras; o dado permite aplicar contraposição.
- **B) está errada:** A existência de backup contradiria a cadeia de implicações e o fato informado.
- **C) está correta:** De ‘não restauração’ obtém-se ‘não verificação sem erro’ e, depois, ‘não backup íntegro’.
- **D) está errada:** A impossibilidade de restauração impede concluir verificação sem erro.
- **Conceito cobrado:** Encadeamento de condicionais e modus tollens.
- **Pegadinha usada:** Afirmar o antecedente ou declarar a regra falsa diante da negação do consequente.
- **Como pensar para acertar:** Percorra as contrapositivas da segunda condicional para a primeira.

### Comentário da Questão 38

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica).
- **A) está errada:** Seis ignora que `P=1,Q=0` e `Q=1,R=0` invalidam casos.
- **B) está errada:** Três omite uma valoração em que antecedente falso torna a condicional verdadeira.
- **C) está errada:** Cinco inclui linha em que uma das implicações é falsa.
- **D) está correta:** As valorações 000, 001, 011 e 111 satisfazem ambas as condicionais: quatro linhas.
- **Conceito cobrado:** Contagem de valorações em condicionais encadeadas.
- **Pegadinha usada:** Considerar condicional verdadeira apenas quando antecedente e consequente são verdadeiros.
- **Como pensar para acertar:** Elimine as linhas em que alguma condicional tem antecedente verdadeiro e consequente falso.

### Comentário da Questão 39

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Essenciais.
- **Momento:** D+2.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 170 é o resultado antes de devolver a interseção tripla subtraída em excesso.
- **B) está errada:** 200 é o universo, não necessariamente a união.
- **C) está errada:** 155 decorre de tratamento incorreto das interseções.
- **D) está correta:** Inclusão-exclusão: `110+90+70-45-30-25+15 = 185`.
- **Conceito cobrado:** Inclusão-exclusão com três conjuntos.
- **Pegadinha usada:** Subtrair as interseções duplas sem somar de volta a interseção tripla.
- **Como pensar para acertar:** Aplique a fórmula completa e observe que quem está nos três foi retirado três vezes.

### Comentário da Questão 40

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) não deve ser marcada:** A afirmação é verdadeira. Planejamento deve considerar a demanda global e evitar manipulação do enquadramento.
- **B) deve ser marcada:** A afirmação é falsa. Separar artificialmente objetos previsíveis para alcançar dispensa não se torna legítimo pelo valor isolado.
- **C) não deve ser marcada:** A afirmação é verdadeira. Contratação direta continua documentada e controlável.
- **D) não deve ser marcada:** A afirmação é verdadeira. Isonomia e finalidade pública também regem o planejamento da contratação.
- **Conceito cobrado:** Fracionamento indevido e contratação direta.
- **Pegadinha usada:** Olhar apenas o valor de cada processo e ignorar a unidade planejável da necessidade.
- **Como pensar para acertar:** Pergunte se a separação decorre de razão técnica real ou serve apenas para contornar a licitação.

### Comentário da Questão 41

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Licitações e contratação direta](semana_01_estudo.md#s1-d6-licitacoes).
- **A) está errada:** Menor preço só é comparável entre propostas que atendem às condições válidas do objeto.
- **B) está correta:** Os critérios publicados devem valer para todos; eventual ilegalidade do edital exige correção impessoal do procedimento.
- **C) está errada:** Alteração retroativa dirigida a uma proposta viola publicidade, vinculação e isonomia.
- **D) está errada:** Economicidade não autoriza contratar objeto em desacordo com requisito essencial válido.
- **Conceito cobrado:** Julgamento objetivo, vinculação e correção do edital.
- **Pegadinha usada:** Usar menor preço para dispensar requisito técnico apenas do licitante preferido.
- **Como pensar para acertar:** Primeiro verifique conformidade; depois compare preços. Se a regra for ilegal, corrija-a para todos.

### Comentário da Questão 42

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Responsabilidade civil do Estado](semana_01_estudo.md#s1-d6-responsabilidade).
- **A) está correta:** A alternativa articula corretamente três planos: regime perante a vítima, causalidade concorrente e regresso subjetivo.
- **B) está errada:** Culpa concorrente pode atenuar, enquanto culpa exclusiva pode excluir.
- **C) está errada:** Responsabilidade objetiva não dispensa dano e nexo nem torna excludentes irrelevantes.
- **D) está errada:** A vítima não precisa aguardar condenação do agente; o regresso, porém, exige dolo ou culpa.
- **Conceito cobrado:** Responsabilidade objetiva, culpa concorrente e ação regressiva.
- **Pegadinha usada:** Misturar os requisitos da relação Estado-vítima com os da relação Estado-agente.
- **Como pensar para acertar:** Resolva em duas relações: vítima contra Estado; depois Estado contra agente culpado ou doloso.

### Comentário da Questão 43

- **Alternativa correta:** B.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos).
- **A) está errada:** Revogação atua sobre ato válido e não encobre incompetência absoluta.
- **B) está correta:** A ilegalidade conduz à anulação; a inconveniência não muda a natureza do vício.
- **C) está errada:** Convalidação não é obrigatória nem cabível para todo vício, especialmente nos termos absolutos do caso.
- **D) está errada:** A autotutela permite à Administração examinar e invalidar seus próprios atos ilegais.
- **Conceito cobrado:** Anulação, revogação e vício de competência.
- **Pegadinha usada:** Escolher revogação porque o ato também se tornou inconveniente.
- **Como pensar para acertar:** A legalidade vem antes do mérito: ato inválido é objeto de anulação, não de revogação corretiva.

### Comentário da Questão 44

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Atos administrativos](semana_01_estudo.md#s1-d6-atos).
- **A) está correta:** A margem discricionária permanece dentro da lei e deve servir à finalidade pública com motivação coerente.
- **B) está errada:** Faixa legal não torna imunes ao controle a finalidade, os motivos e a proporcionalidade.
- **C) está errada:** Validade numérica não sana retaliação nem motivação deficiente.
- **D) está errada:** Competência não é o único elemento controlável em ato discricionário.
- **Conceito cobrado:** Controle da discricionariedade e desvio de finalidade.
- **Pegadinha usada:** Confundir margem de escolha com imunidade jurídica.
- **Como pensar para acertar:** Examine não só se o valor cabe na faixa, mas por que e para que o máximo foi escolhido.

### Comentário da Questão 45

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 84 é a pendência antes da etapa adicional; 12,5% compara 84 com 96 sem aplicar os 25% finais.
- **B) está errada:** 72 não resulta da redução de 25% sobre os 84 pendentes da segunda coorte.
- **C) está errada:** O saldo 63 está correto, mas a redução deve ser calculada sobre os 96 da primeira coorte.
- **D) está correta:** A segunda coorte tem 300 processos, deixa 84 pendentes e depois 63; a queda de 33 sobre 96 equivale a 34,375%.
- **Conceito cobrado:** Percentuais sucessivos, complemento percentual e comparação entre bases.
- **Pegadinha usada:** Misturar as coortes ou confundir a taxa da última etapa com a variação entre os saldos.
- **Como pensar para acertar:** Calcule separadamente cada coorte e só depois compare os dois saldos indicados.

### Comentário da Questão 46

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 180 desconta 10%, e não 20%, da capacidade bruta.
- **B) está errada:** 200 ignora que 20% da capacidade será consumida.
- **C) está errada:** 150 aplica o percentual à produção inicial, não ao novo cenário.
- **D) está correta:** A taxa bruta é 5 processos por servidor-dia; a capacidade bruta nova é 200 e a líquida, 160.
- **Conceito cobrado:** Regra de três composta com perda por retrabalho.
- **Pegadinha usada:** Calcular corretamente a produção bruta e esquecer o fator líquido.
- **Como pensar para acertar:** Encontre a taxa unitária, projete a capacidade bruta e aplique 80%.

### Comentário da Questão 47

- **Alternativa correta:** C.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** 2.000 é a soma dos números terminados em 5 antes da segunda exclusão.
- **B) está errada:** 1.260 resulta de contagem ou soma incorreta dos termos que também são divisíveis por 3.
- **C) está correta:** Os termos terminados em 5 somam 2.000; os divisíveis por 3 são `15, 45, ..., 195` e somam 735; resta 1.265.
- **D) está errada:** 735 é justamente a soma do subconjunto que deve ser excluído, não a dos termos restantes.
- **Conceito cobrado:** Progressões aritméticas, divisibilidade e diferença de subconjuntos.
- **Pegadinha usada:** Parar após excluir múltiplos de 10 ou marcar a soma do subconjunto eliminado.
- **Como pensar para acertar:** Forme a PA dos números terminados em 5, identifique nela a sub-PA divisível por 3 e subtraia as duas somas.

### Comentário da Questão 48

- **Alternativa correta:** D.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está errada:** O valor 44 resulta de desfazer parcialmente as operações ou de usar bases incorretas.
- **B) está errada:** Dividir 132 por 2 e por 1,20 sem devolver as 18 unidades produz 55.
- **C) está errada:** Somar 18 após dividir por 2 produz 84, mas ainda falta desfazer o aumento de 20%.
- **D) está correta:** Reverta a ordem: `132 ÷ 2 = 66`; `66 + 18 = 84`; `84 ÷ 1,20 = 70`.
- **Conceito cobrado:** Princípio da regressão ou reversão com operações sucessivas.
- **Pegadinha usada:** Desfazer as operações na ordem direta ou esquecer de inverter uma delas.
- **Como pensar para acertar:** Comece do resultado final e aplique as operações inversas na ordem contrária.

### Comentário da Questão 49

- **Alternativa correta:** A.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Conjuntos, proporcionalidade, sequências e probabilidade](semana_01_estudo.md#s1-d6-rlm-conjuntos-calculos).
- **A) está correta:** Se A=3k e T=5k, `(3k+6)/(5k)=9/10`, logo `k=4` e o total inicial é 32.
- **B) está errada:** Esse total não satisfaz simultaneamente as razões antes e depois da contratação.
- **C) está errada:** 48 corresponderia a k=6, que não gera a nova razão.
- **D) está errada:** 24 corresponderia a k=3, também incompatível com 9:10.
- **Conceito cobrado:** Razões com alteração de uma das parcelas.
- **Pegadinha usada:** Aplicar a nova razão ao total antigo sem montar a equação.
- **Como pensar para acertar:** Represente as quantidades por 3k e 5k, acrescente 6 apenas aos analistas e resolva.

### Comentário da Questão 50

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Lógica proposicional e argumentativa](semana_01_estudo.md#s1-d6-rlm-logica).
- **A) está errada:** Os valores de P, Q e R determinam completamente a expressão.
- **B) está errada:** Os dois lados da bicondicional têm valores diferentes, portanto ela não é verdadeira.
- **C) está correta:** `P ou Q` é verdadeiro e implica R falso, tornando o lado esquerdo falso; `Q e não R` é verdadeiro; a bicondicional é falsa.
- **D) está errada:** A falsidade de `R` torna `não R` verdadeiro no lado direito e não produz o resultado descrito.
- **Conceito cobrado:** Avaliação de expressão lógica composta.
- **Pegadinha usada:** Avaliar a condicional como verdadeira apenas porque seu antecedente contém uma parcela falsa.
- **Como pensar para acertar:** Calcule cada subexpressão, depois a condicional e, por último, compare os lados da bicondicional.

### Comentários das questões complementares do Dia 6

#### Comentário Extra Dia 6.1

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está errada:** O Código de Ética também alcança pessoas jurídicas registradas no CRA competente, observadas as especificidades aplicáveis.
- **B) está errada:** Estrutura interna pertence ao Regimento, não ao objeto principal do Código.
- **C) está errada:** O material registra que suspensão e cancelamento não se aplicam à PJ.
- **D) está correta:** O Código orienta deveres e infrações de PF e PJ, com especificidades.
- **Conceito cobrado:** Abrangência do Código de Ética.
- **Pegadinha usada:** Ou excluir a pessoa jurídica, ou aplicar-lhe todas as sanções de modo idêntico.
- **Como pensar para acertar:** Separe incidência do Código de aplicação específica de cada sanção.

#### Comentário Extra Dia 6.2

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está errada:** CNPJ não substitui regularidade profissional.
- **B) está correta:** A fiscalização deve unir objeto da empresa, regularidade e atuação técnica real.
- **C) está errada:** Indicação formal não basta quando o responsável não participa.
- **D) está errada:** Adimplência isolada não comprova atuação técnica nem registro da empresa.
- **Conceito cobrado:** Fiscalização de pessoa jurídica e responsabilidade técnica.
- **Pegadinha usada:** Confundir documento formal com participação efetiva.
- **Como pensar para acertar:** Examine a atividade exercida e quem realmente orienta ou supervisiona o serviço.

#### Comentário Extra Dia 6.3

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está errada:** Decreto regulamentar não revoga nem supera hierarquicamente a lei que executa.
- **B) está correta:** A lei fornece a base normativa, e o decreto detalha sua execução dentro dos limites legais.
- **C) está errada:** A lei e o decreto tratam da profissão e do Sistema, não se limitam a Regimento e Código de Ética.
- **D) está errada:** Regulamento e ato regional não podem ampliar livremente matéria definida em lei.
- **Conceito cobrado:** Relação entre lei e decreto regulamentar.
- **Pegadinha usada:** Confundir regulamentação com revogação, superioridade ou inovação sem base legal.
- **Como pensar para acertar:** Identifique qual fonte cria a base e qual apenas organiza sua execução.

#### Comentário Extra Dia 6.4

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está correta:** O sigilo subsiste, ressalvado fundamento legal ou justa causa aplicável.
- **B) está errada:** Vantagem econômica não constitui justa causa por si só.
- **C) está errada:** O fim do contrato não libera automaticamente a informação.
- **D) está errada:** Dever ético não é afastado apenas pelo encerramento do instrumento contratual.
- **Conceito cobrado:** Persistência do sigilo profissional.
- **Pegadinha usada:** Reduzir o sigilo à vigência formal do contrato.
- **Como pensar para acertar:** Pergunte se existe exceção jurídica concreta; sem ela, preserve a confidencialidade.

#### Comentário Extra Dia 6.5

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está errada:** Discordância não autoriza ocultação até decisão nacional.
- **B) está errada:** Direito de defesa não suspende toda fiscalização automaticamente.
- **C) está correta:** Colaboração com diligência regular convive com defesa pelos canais próprios.
- **D) está errada:** Registro de terceiro não demonstra regularidade e pode gerar outra infração.
- **Conceito cobrado:** Fiscalização e exercício regular da defesa.
- **Pegadinha usada:** Tratar defesa como autorização para obstrução.
- **Como pensar para acertar:** Cumpra as solicitações pertinentes e conteste formalmente o que considerar indevido.

#### Comentário Extra Dia 6.6

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está errada:** Autonomia administrativa não atribui ao CRA poder para redefinir matéria reservada à lei.
- **B) está errada:** Decreto regulamentar detalha a execução da lei; não recebe competência legislativa primária por ser repetido em ato regional.
- **C) está correta:** Lei, decreto regulamentar e ato interno formam níveis distintos; os dois últimos devem respeitar a base legal da profissão.
- **D) está errada:** Especialidade não autoriza norma hierarquicamente inferior a contrariar ou ampliar a lei que lhe dá fundamento.
- **Conceito cobrado:** Hierarquia normativa e limites do poder regulamentar no Sistema CFA/CRAs.
- **Pegadinha usada:** Confundir autonomia do conselho com competência para inovar além da lei.
- **Como pensar para acertar:** Identifique qual norma cria a base profissional e verifique se os atos inferiores apenas a executam ou tentam ampliá-la.

#### Comentário Extra Dia 6.7

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está correta:** Sujeito, território e objeto normativo evitam as trocas mais comuns.
- **B) está errada:** Sanção é etapa posterior ao enquadramento e não deve ser presumida.
- **C) está errada:** CFA e CRA possuem funções articuladas, mas não idênticas.
- **D) está errada:** Registro, ética, fiscalização e regimento têm objetos diferentes.
- **Conceito cobrado:** Roteiro de resolução em legislação profissional.
- **Pegadinha usada:** Começar pela penalidade ou pelo número da norma sem identificar o caso.
- **Como pensar para acertar:** Mapeie quem praticou o quê, onde e sob qual disciplina.

#### Comentário Extra Dia 6.8

- **Alternativa correta:** D.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está errada:** CRAs possuem jurisdições regionais, não competência nacional concorrente automática.
- **B) está errada:** Ética não elimina a análise territorial da fiscalização.
- **C) está errada:** Atividade de Administração não atribui por si só todo caso ao CRA-PR.
- **D) está correta:** O local do fato e o conselho competente precisam ser verificados.
- **Conceito cobrado:** Jurisdição dos Conselhos Regionais.
- **Pegadinha usada:** Associar o nome CRA-PR a fatos ocorridos em qualquer território.
- **Como pensar para acertar:** Localize o fato antes de atribuir competência regional.

#### Comentário Extra Dia 6.9

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está errada:** Regimento organiza a estrutura interna, enquanto regulamento eleitoral não disciplina o uso do registro no caso apresentado.
- **B) está errada:** Registro do profissional não sana a empresa nem legitima empréstimo de número.
- **C) está errada:** Lei 12.514 trata de contribuições, não resolve isoladamente ambos os fatos.
- **D) está correta:** A alternativa exige fonte oficial confirmada para a regularidade, separa a conduta ética e atribui a fiscalização ao CRA-PR em sua jurisdição.
- **Conceito cobrado:** Integração entre registro, ética e competência.
- **Pegadinha usada:** Usar uma única norma para fatos de objetos diferentes.
- **Como pensar para acertar:** Divida o caso em regularidade da PJ, comportamento do profissional e órgão fiscalizador.

#### Comentário Extra Dia 6.10

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 6 — Legislação CRA/CFA consolidada](semana_01_estudo.md#s1-d6-b4).
- **A) está correta:** Detalhes de artigo, prazo ou pena exigem consulta ao texto oficial.
- **B) está errada:** Sanção máxima não pode ser presumida sem base normativa e circunstâncias.
- **C) está errada:** O objeto confirmado pela ementa pode ser utilizado com a devida limitação.
- **D) está errada:** Analogia com outro conselho não confirma prazo específico.
- **Conceito cobrado:** Controle de fontes normativas.
- **Pegadinha usada:** Preencher lacuna documental com memória ou analogia.
- **Como pensar para acertar:** Afirme somente o que a fonte consultada comprova.

#### Comentário Extra Dia 6.11

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 1 — Cache e localidade](semana_01_estudo.md#s1-d1-cache-localidade).
- **A) está errada:** O caso não depende de reutilizar imediatamente o mesmo elemento, que caracterizaria localidade temporal.
- **B) está correta:** Elementos contíguos ocupam endereços próximos, favorecendo o aproveitamento dos dados vizinhos trazidos para a cache.
- **C) está errada:** Memória virtual não elimina automaticamente faltas nem explica especificamente o benefício dos endereços contíguos.
- **D) está errada:** Write-back é política de escrita e não converte dados do vetor em registradores.
- **Conceito cobrado:** Localidade espacial no uso da cache.
- **Pegadinha usada:** Trocar localidade espacial por temporal ou por uma política de escrita.
- **Como pensar para acertar:** Pergunte se o padrão repete o mesmo endereço ou percorre endereços vizinhos.

#### Comentário Extra Dia 6.12

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 1 — Pipeline e desempenho](semana_01_estudo.md#s1-d1-pipeline-desempenho).
- **A) está errada:** Pipeline existe justamente para permitir sobreposição de etapas entre instruções diferentes.
- **B) está errada:** A técnica melhora vazão, mas não garante menor latência individual em toda situação.
- **C) está correta:** Busca, decodificação e execução podem ocorrer para instruções distintas ao mesmo tempo, com possíveis paradas por conflitos.
- **D) está errada:** Pipeline não substitui a hierarquia de memória nem mantém instruções na memória secundária para executá-las.
- **Conceito cobrado:** Pipeline, vazão e latência.
- **Pegadinha usada:** Transformar ganho de throughput em redução obrigatória da latência individual.
- **Como pensar para acertar:** Separe quantidade de instruções concluídas por tempo da duração de uma instrução específica.

#### Comentário Extra Dia 6.13

- **Alternativa correta:** A.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 2 — Escalonamento, quantum e starvation](semana_01_estudo.md#s1-d2-escalonamento).
- **A) está correta:** O quantum limita o tempo contínuo de CPU e influencia tanto o custo de alternância quanto o tempo de resposta.
- **B) está errada:** Round Robin é preemptivo; o quantum não representa prioridade fixa até o encerramento.
- **C) está errada:** Ao esgotar a fatia, processo ainda não concluído retorna à fila para permitir a alternância.
- **D) está errada:** Quantum é parâmetro de escalonamento da CPU, não medida de memória virtual.
- **Conceito cobrado:** Round Robin e efeito do quantum.
- **Pegadinha usada:** Confundir fatia de tempo com prioridade, execução até o fim ou tamanho de memória.
- **Como pensar para acertar:** Relacione quantum a preempção, fila circular, trocas de contexto e responsividade.

#### Comentário Extra Dia 6.14

- **Alternativa correta:** B.
- **Nível:** Médio.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 2 — Memória virtual, paginação e thrashing](semana_01_estudo.md#s1-d2-memoria-virtual).
- **A) está errada:** Página ausente da RAM pode ser carregada; isso não equivale necessariamente a violação fatal de memória.
- **B) está correta:** Uma página virtual válida não residente provoca page fault e pode ser carregada pelo sistema operacional.
- **C) está errada:** Deadlock exige espera circular por recursos e não decorre automaticamente de página não residente.
- **D) está errada:** Journaling protege a consistência do sistema de arquivos e não realiza a tradução descrita.
- **Conceito cobrado:** Page fault no funcionamento da memória virtual.
- **Pegadinha usada:** Tratar todo page fault como erro fatal ou confundi-lo com deadlock e journaling.
- **Como pensar para acertar:** Verifique se a página é válida e apenas não está residente; nesse caso, o SO pode carregá-la.

#### Comentário Extra Dia 6.15

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Aprofundamento.
- **Momento:** Antes de D+7.
- **Referência:** [Dia 3 — GROUP BY, HAVING e agregações](semana_01_estudo.md#s1-d3-group-by-having).
- **A) está errada:** COUNT(*) sobre o grupo deve ser testado em HAVING, não em WHERE.
- **B) está errada:** A ordem sintática está errada e HAVING não antecede GROUP BY nesses termos.
- **C) está errada:** Agregação não pode ser usada assim em WHERE, e a cláusula GROUP BY está mal formada.
- **D) está correta:** WHERE filtra linhas ativas antes do agrupamento; HAVING filtra os grupos pelo COUNT.
- **Conceito cobrado:** WHERE, GROUP BY e HAVING.
- **Pegadinha usada:** Usar WHERE para condição agregada ou inverter a ordem das cláusulas.
- **Como pensar para acertar:** Filtre linhas com WHERE, agrupe e filtre resultados agregados com HAVING.

#### Comentário Extra Dia 6.16

- **Alternativa correta:** C.
- **Nível:** Médio.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 3 — GROUP BY, HAVING e agregações](semana_01_estudo.md#s1-d3-group-by-having).
- **A) está errada:** COUNT(coluna) ignora NULL e não retorna 4.
- **B) está errada:** COUNT(*) inclui todas as linhas e não retorna 2.
- **C) está correta:** Há dois valores não nulos e quatro linhas: 2 e 4.
- **D) está errada:** A ordem dos resultados foi invertida.
- **Conceito cobrado:** Comportamento de COUNT diante de NULL.
- **Pegadinha usada:** Tratar COUNT(coluna) e COUNT(*) como equivalentes.
- **Como pensar para acertar:** Conte valores não nulos para a coluna e todas as linhas para o asterisco.

#### Comentário Extra Dia 6.17

- **Alternativa correta:** C.
- **Nível:** Difícil.
- **Uso:** Revisão.
- **Momento:** D+7.
- **Referência:** [Dia 4 — Regimento Interno do CRA-PR](semana_01_estudo.md#s1-d4-regimento) e [Código de Ética](semana_01_estudo.md#s1-d4-codigo-etica).
- **A) está errada:** Regulamento de Registro não disciplina a divisão interna de funções nem substitui o Código.
- **B) está errada:** A alternativa inverte Regimento, Ética e regulamento eleitoral.
- **C) está correta:** RN 651/Regimento organiza Plenário e Diretoria; RN 671/Código rege o sigilo profissional.
- **D) está errada:** A Diretoria regional não assume função normativa nacional, e sigilo não desaparece automaticamente.
- **Conceito cobrado:** Integração entre Regimento e Código de Ética.
- **Pegadinha usada:** Aplicar uma resolução verdadeira ao objeto errado.
- **Como pensar para acertar:** Classifique primeiro estrutura institucional e conduta profissional; só depois associe as normas.

#### Comentário Extra Dia 6.18

- **Alternativa correta:** A.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 5 — Concordância, regência, crase e pontuação](semana_01_estudo.md#s1-d5-concordancia-regencia-crase-pontuacao).
- **A) está correta:** A frase usa vírgula após a concessiva, não emprega crase antes de verbo e usa corretamente ‘à chefia’.
- **B) está errada:** A oração concessiva anteposta pede vírgula, e a vírgula antes de ‘e’ separa indevidamente ações com o mesmo sujeito.
- **C) está errada:** Com partícula apassivadora, o verbo deve concordar: ‘encaminharam-se os autos’.
- **D) está errada:** Não há crase antes de infinitivo, e ‘chefia’ exige artigo no contexto.
- **Conceito cobrado:** Crase, concordância e pontuação.
- **Pegadinha usada:** Corrigir um fenômeno e deixar outro erro discreto na mesma alternativa.
- **Como pensar para acertar:** Verifique separadamente a oração anteposta, a concordância e cada ocorrência de ‘a’.

#### Comentário Extra Dia 6.19

- **Alternativa correta:** D.
- **Nível:** Difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 4 — Contratação pública](semana_01_estudo.md#s1-d4-contratacao-publica).
- **A) está errada:** Impessoalidade e economicidade continuam aplicáveis.
- **B) está errada:** Inviabilidade de competição aponta para inexigibilidade, não dispensa.
- **C) está errada:** Contratação direta não autoriza escolha oral ou ausência de processo.
- **D) está correta:** Exclusividade comprovada pode tornar a competição inviável, mas não elimina a instrução da contratação direta.
- **Conceito cobrado:** Inexigibilidade e formalização da contratação direta.
- **Pegadinha usada:** Confundir ausência de licitação com ausência de procedimento e princípios.
- **Como pensar para acertar:** Responda duas perguntas: a competição é viável? Quais deveres processuais permanecem?

#### Comentário Extra Dia 6.20

- **Alternativa correta:** B.
- **Nível:** Muito difícil.
- **Uso:** Simulado.
- **Momento:** Ciclo seguinte.
- **Referência:** [Dia 4 — Microtrilha de RLM](semana_01_estudo.md#s1-d4-rlm-extras).
- **A) está errada:** 225 surge ao dividir 135 apenas por 60% e ainda não produz a diferença informada após a reclassificação.
- **B) está correta:** Aceitos são 45% do total, logo houve 300 processos; rejeitados passam de 120 para 80 e a complementação de 45 para 85, diferença de 5.
- **C) está errada:** O total 300 está correto, mas 40 é a quantidade reclassificada, não a diferença final entre 85 e 80.
- **D) está errada:** 360 não satisfaz os 135 aceitos, pois 45% de 360 corresponde a 162.
- **Conceito cobrado:** Percentuais condicionais, recuperação da base e reclassificação entre categorias.
- **Pegadinha usada:** Somar percentuais de bases diferentes ou confundir quantidade transferida com diferença final.
- **Como pensar para acertar:** Recupere o total pelos aceitos, encontre cada categoria inicial e atualize origem e destino pela mesma transferência.
