# Apostila de Questões - Semana 1 v1.2

## CRA-PR 2026 - Analista de Sistemas

Arquivo de questões para acompanhar a `Apostila_Estudo_Semana_1_CRA_PR_Analista_Sistemas_v1_2.md`.

**Critério de autoria:** esta versão não reproduz questões reais de provas anteriores. Todas as 300 questões são autorais e estão marcadas como `Questão autoral no estilo Instituto Consulplan`. As provas públicas da banca foram usadas somente como referência de estilo de cobrança.

**Formato:** todas as questões têm quatro alternativas, de A) a D), conforme o edital do CRA-PR 2026.

**Total:** 300 questões, sendo exatamente 50 por dia.

**Nível pretendido:** médio a difícil, com assertivas completas, verdadeiro/falso, estudos de caso, comandos SQL, cenários de órgão público e distratores plausíveis.

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

## Questões

### Questão 1 — Questão autoral no estilo Instituto Consulplan

Em uma rotina de diagnóstico, um analista precisa converter o valor binário 101101 para decimal. O resultado correto é:

A) 53
B) 64
C) 45
D) 37

### Questão 2 — Questão autoral no estilo Instituto Consulplan

Um dump de memória apresenta o byte 1111 0000. Em hexadecimal, esse valor deve ser representado por:

A) FF
B) F0
C) 0F
D) E0

### Questão 3 — Questão autoral no estilo Instituto Consulplan

Considere as assertivas sobre unidades de informação.

I. Um byte é composto por 8 bits.
II. Com 8 bits, podem ser representadas 256 combinações distintas.
III. O maior valor sem sinal representável com 8 bits é 256.

Está correto apenas o que se afirma em:

A) I e II
B) I e III
C) II e III
D) I, II e III

### Questão 4 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre a hierarquia de memória.

A) Registradores ficam no nível mais rápido e próximo da CPU.
B) O SSD é normalmente mais rápido que registradores e cache.
C) A RAM é volátil e usada como memória principal durante a execução de programas.
D) A memória cache costuma ser usada para manter dados frequentemente acessados próximos da CPU.

### Questão 5 — Questão autoral no estilo Instituto Consulplan

Durante a execução de um programa, a CPU precisa realizar uma soma e uma comparação lógica. O componente diretamente associado a essas operações é:

A) Barramento de endereços
B) Memória secundária
C) ULA/ALU
D) Unidade de controle

### Questão 6 — Questão autoral no estilo Instituto Consulplan

Um técnico afirma que a RAM é suficiente como política de armazenamento permanente porque possui alta velocidade. Essa afirmação é:

A) incorreta apenas se o sistema operacional for Linux.
B) incorreta, pois a RAM é volátil e não substitui SSD/HD para persistência.
C) correta, pois toda memória rápida é permanente por definição.
D) correta apenas em processadores de 64 bits.

### Questão 7 — Questão autoral no estilo Instituto Consulplan

Em uma placa de rede, a chegada de um pacote pode sinalizar à CPU que há evento a tratar. Esse mecanismo é melhor descrito como:

A) interrupção
B) compilação
C) paginação
D) normalização

### Questão 8 — Questão autoral no estilo Instituto Consulplan

Analise as assertivas sobre interrupções.

I. Interrupções podem ser usadas para tratar eventos de entrada e saída.
II. Toda interrupção representa falha irrecuperável de hardware.
III. Interrupções de temporizador ajudam sistemas multitarefa a alternar a execução.

Está correto apenas o que se afirma em:

A) I e II
B) II e III
C) I, II e III
D) I e III

### Questão 9 — Questão autoral no estilo Instituto Consulplan

Um programa trabalha com endereços virtuais, e o hardware/SO traduz esses endereços para posições reais na RAM. Essa descrição se refere a:

A) codificação ASCII de caracteres.
B) barramento de controle substituindo a RAM.
C) memória virtual com tradução para endereços físicos.
D) armazenamento permanente por firmware.

### Questão 10 — Questão autoral no estilo Instituto Consulplan

No modo de endereçamento imediato, o operando:

A) fica exclusivamente em registrador indicado indiretamente.
B) aparece na própria instrução.
C) é obrigatoriamente buscado em uma tabela de páginas.
D) é sempre recuperado de um arquivo no SSD.

### Questão 11 — Questão autoral no estilo Instituto Consulplan

Um projeto em C possui três arquivos-fonte compilados separadamente, mas um módulo chama função definida em outro. A etapa responsável por resolver referências entre módulos e bibliotecas é:

A) ligação, realizada pelo linker.
B) interpretação linha a linha.
C) paginação por demanda.
D) cache write-back.

### Questão 12 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre compiladores e interpretadores.

A) O interpretador sempre gera executável nativo independente antes de qualquer execução.
B) O compilador só existe em sistemas operacionais Linux.
C) O interpretador é um componente físico obrigatório da CPU.
D) O compilador traduz o código antes da execução; o interpretador executa/traduz de modo incremental durante a execução.

### Questão 13 — Questão autoral no estilo Instituto Consulplan

Um analista observa que determinado algoritmo acessa repetidamente posições próximas de um vetor. Esse comportamento tende a favorecer:

A) substituição da ULA pela memória cache.
B) conversão automática de binário para Unicode.
C) localidade espacial e melhor aproveitamento de cache.
D) eliminação da necessidade de memória RAM.

### Questão 14 — Questão autoral no estilo Instituto Consulplan

Considere as afirmações sobre representação de caracteres.

I. Caracteres são representados internamente por códigos numéricos.
II. ASCII é suficiente para representar, de forma ampla, todos os caracteres de todos os idiomas modernos.
III. Unicode tem objetivo mais abrangente que o ASCII.

Está correto apenas o que se afirma em:

A) I, II e III
B) I e III
C) I e II
D) II e III

### Questão 15 — Questão autoral no estilo Instituto Consulplan

Um processador de 64 bits é assim chamado, em termos gerais, por características relacionadas:

A) à largura de palavra, registradores e endereçamento, conforme a arquitetura.
B) à quantidade fixa de 64 núcleos físicos.
C) à velocidade mínima de internet de 64 Mbps.
D) ao tamanho obrigatório de 64 GB de RAM.

### Questão 16 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre barramentos em arquitetura de computadores.

A) O barramento de endereços indica a posição a ser acessada.
B) O barramento de controle carrega sinais de coordenação, como leitura e escrita.
C) O barramento de endereços é o responsável por executar operações aritméticas.
D) O barramento de dados transporta conteúdo entre componentes.

### Questão 17 — Questão autoral no estilo Instituto Consulplan

Em uma arquitetura com pipeline, a vantagem esperada é:

A) eliminar dependências de dados entre instruções.
B) substituir a memória cache por registradores.
C) aumentar a vazão ao sobrepor etapas de instruções.
D) garantir que cada instrução individual sempre tenha latência menor.

### Questão 18 — Questão autoral no estilo Instituto Consulplan

Uma falha de cache, ou cache miss, ocorre quando:

A) o programa é compilado sem bibliotecas externas.
B) o dado procurado não está na cache e precisa ser buscado em nível inferior da hierarquia.
C) a CPU encontra o dado na cache L1.
D) o sistema operacional desliga a RAM por segurança.

### Questão 19 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre ponto flutuante.

A) Números reais podem ser representados de forma aproximada, com possibilidade de erro de arredondamento.
B) Todo número decimal com casas fracionárias é representado exatamente.
C) Ponto flutuante é usado apenas para armazenar caracteres Unicode.
D) Erros de arredondamento são impossíveis em computação digital.

### Questão 20 — Questão autoral no estilo Instituto Consulplan

Em complemento de dois, uma característica importante é:

A) eliminar a necessidade de bit de sinal ou codificação equivalente.
B) representar apenas números positivos.
C) ser uma técnica exclusiva de codificação de textos.
D) facilitar operações aritméticas com inteiros negativos no hardware.

### Questão 21 — Questão autoral no estilo Instituto Consulplan

Um arquivo executável já ligado precisa ser colocado na memória para iniciar sua execução. Essa etapa é realizada pelo:

A) montador, que traduz assembly para máquina.
B) pré-processador, que executa o programa final.
C) carregador, ou loader.
D) linker, que já resolveu referências antes.

### Questão 22 — Questão autoral no estilo Instituto Consulplan

Uma palavra de máquina de 32 bits possui quantos bytes?

A) 32 bytes.
B) 4 bytes.
C) 2 bytes.
D) 8 bytes.

### Questão 23 — Questão autoral no estilo Instituto Consulplan

Em um relatório técnico, throughput e latência foram usados como métricas de desempenho. A interpretação correta é:

A) throughput mede trabalho por unidade de tempo; latência mede tempo de resposta/espera.
B) throughput e latência são sinônimos perfeitos.
C) latência mede apenas capacidade de disco em GB.
D) throughput mede exclusivamente temperatura da CPU.

### Questão 24 — Questão autoral no estilo Instituto Consulplan

Considere uma instrução hipotética MOV R1, #5, na qual #5 representa o valor literal a ser carregado. Esse exemplo ilustra:

A) endereçamento indireto por memória.
B) paginação por demanda.
C) DMA de dispositivo.
D) endereçamento imediato.

### Questão 25 — Questão autoral no estilo Instituto Consulplan

Um dispositivo de E/S transfere dados para a memória com menor intervenção da CPU. Esse mecanismo é conhecido como:

A) linkedição dinâmica.
B) codificação ASCII.
C) DMA, acesso direto à memória.
D) ULA vetorial.

### Questão 26 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre firmware.

A) É uma política de escalonamento de processos.
B) É software de baixo nível associado ao controle de hardware ou dispositivo.
C) É sempre um aplicativo de usuário instalado no navegador.
D) É sinônimo de memória RAM volátil.

### Questão 27 — Questão autoral no estilo Instituto Consulplan

Um analista compara memórias e afirma: “quanto mais próximo da CPU, em geral, menor a capacidade e maior a velocidade”. A afirmação está:

A) correta para a hierarquia típica de registradores/cache/RAM/armazenamento.
B) incorreta, pois SSD é sempre menor e mais rápido que cache.
C) incorreta, pois registradores são os maiores armazenamentos do computador.
D) correta apenas quando não existe cache.

### Questão 28 — Questão autoral no estilo Instituto Consulplan

V/F: Sobre representação de dados, marque a sequência correta.

I. Um bit pode assumir, em computação digital clássica, os valores 0 ou 1.
II. Um byte é composto por 4 bits.
III. Um caractere pode ser representado por um código numérico.

A sequência correta é:

A) V, V, F.
B) F, V, V.
C) F, F, V.
D) V, F, V.

### Questão 29 — Questão autoral no estilo Instituto Consulplan

Um sistema de 64 bits pode endereçar espaços maiores que um sistema de 32 bits, em tese, porque:

A) o sistema elimina a necessidade de memória virtual.
B) o barramento de controle deixa de existir.
C) a largura de endereçamento permite representar mais endereços distintos.
D) o clock do processador é obrigatoriamente 64 vezes maior.

### Questão 30 — Questão autoral no estilo Instituto Consulplan

Assinale a incorreta sobre execução de instruções em uma CPU.

A) A CPU executa instruções sem qualquer uso de registradores.
B) A etapa de busca obtém uma instrução da memória.
C) A etapa de decodificação interpreta qual operação deve ser realizada.
D) A execução pode envolver a ULA, registradores e acesso à memória.

### Questão 31 — Questão autoral no estilo Instituto Consulplan

Um administrador observa que um programa acessa repetidamente o mesmo valor em curto intervalo. Esse comportamento exemplifica:

A) localidade temporal.
B) localidade espacial apenas.
C) interrupção mascarável.
D) endereçamento por registrador obrigatório.

### Questão 32 — Questão autoral no estilo Instituto Consulplan

Em computação, a expressão “programa armazenado” associada à arquitetura de von Neumann indica que:

A) programas nunca usam memória principal.
B) dados ficam apenas em dispositivos de entrada.
C) a CPU deixa de buscar instruções.
D) instruções e dados podem residir na memória para serem processados pela CPU.

### Questão 33 — Questão autoral no estilo Instituto Consulplan

Uma rotina em assembly é traduzida para código de máquina por um:

A) loader, que carrega o executável em memória.
B) escalonador, que escolhe processo para CPU.
C) montador, ou assembler.
D) linker, que apenas resolve referências entre objetos.

### Questão 34 — Questão autoral no estilo Instituto Consulplan

Em um cenário de suporte, um usuário pergunta por que aumentar a RAM pode melhorar desempenho quando há muitas aplicações abertas. A explicação mais adequada é:

A) mais RAM elimina a necessidade de sistema operacional.
B) mais RAM pode reduzir paginação/swap e permitir manter mais dados de processos em memória principal.
C) mais RAM aumenta automaticamente a frequência da CPU.
D) mais RAM transforma SSD em cache L1.

### Questão 35 — Questão autoral no estilo Instituto Consulplan

Uma CPU usa registradores para armazenar temporariamente operandos e resultados intermediários. Essa afirmação está:

A) correta, pois registradores são pequenos e muito rápidos.
B) incorreta, pois registradores ficam apenas no SSD.
C) incorreta, pois registradores só armazenam arquivos permanentes.
D) correta apenas em computadores sem memória cache.

### Questão 36 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa que apresenta somente memórias voláteis ou tipicamente temporárias no processamento.

A) SSD, HD e fita magnética.
B) DVD, SSD e ROM de firmware.
C) HD, RAM e fita magnética.
D) Registradores, cache e RAM.

### Questão 37 — Questão autoral no estilo Instituto Consulplan

Uma interrupção mascarável é, em termos gerais, aquela que:

A) representa apenas erro lógico de programação.
B) é sinônimo de cache miss.
C) pode ser temporariamente desabilitada ou adiada pelo processador/SO em certas condições.
D) nunca pode ser ignorada em nenhuma circunstância.

### Questão 38 — Questão autoral no estilo Instituto Consulplan

Ao avaliar desempenho, um analista conclui que a largura de banda da memória indica:

A) quantidade de instruções da linguagem SQL.
B) quantidade de dados que pode ser transferida por unidade de tempo.
C) tempo mínimo de resposta de um único acesso, exclusivamente.
D) número máximo de usuários cadastrados no sistema.

### Questão 39 — Questão autoral no estilo Instituto Consulplan

Em um número hexadecimal, as letras A, B, C, D, E e F correspondem, respectivamente, aos valores decimais:

A) 10, 11, 12, 13, 14 e 15.
B) 11, 12, 13, 14, 15 e 16.
C) 1, 2, 3, 4, 5 e 6.
D) 16, 17, 18, 19, 20 e 21.

### Questão 40 — Questão autoral no estilo Instituto Consulplan

Um periférico solicita atenção da CPU após concluir operação de leitura. A vantagem do uso de interrupção nesse caso é:

A) impedir qualquer multitarefa no sistema.
B) transformar o periférico em memória principal.
C) dispensar todos os drivers de dispositivo.
D) evitar que a CPU consulte continuamente o dispositivo para saber se terminou.

### Questão 41 — Questão autoral no estilo Instituto Consulplan

Em uma arquitetura com cache write-back, a escrita modificada pode:

A) ser descartada porque cache nunca armazena dados alterados.
B) eliminar a necessidade de coerência de cache.
C) ser mantida temporariamente na cache e atualizada na memória principal posteriormente.
D) ser sempre escrita simultaneamente na RAM a cada alteração.

### Questão 42 — Questão autoral no estilo Instituto Consulplan

Considere um sistema com barramento de dados de 64 bits. Isso significa que, em uma transferência, o barramento pode transportar:

A) 64 GB de armazenamento permanente.
B) 64 bits de dados por operação/ciclo de transferência, conforme a arquitetura.
C) 64 endereços físicos obrigatoriamente.
D) 64 programas simultâneos, sempre.

### Questão 43 — Questão autoral no estilo Instituto Consulplan

Quando se diz que um byte pode assumir 256 combinações, o intervalo sem sinal mais comum é:

A) 0 a 255.
B) 1 a 256.
C) 0 a 256.
D) -128 a 255.

### Questão 44 — Questão autoral no estilo Instituto Consulplan

Em uma linguagem compilada tradicional, se uma biblioteca externa não é encontrada durante a geração do executável, o erro tende a ocorrer na etapa de:

A) digitação do código-fonte pela CPU.
B) execução de ULA para soma inteira.
C) conversão de ASCII para Unicode.
D) ligação.

### Questão 45 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre ROM e RAM.

A) RAM é apenas leitura, e ROM é leitura e escrita livre em toda execução.
B) ROM substitui registradores durante cálculos da ULA.
C) ROM é tipicamente não volátil; RAM é volátil e usada na execução de programas.
D) ROM e RAM são sempre voláteis e equivalentes.

### Questão 46 — Questão autoral no estilo Instituto Consulplan

Uma rotina que executa muitas operações aritméticas, mas acessa pouco disco, tende a ser limitada principalmente por:

A) regência verbal.
B) processamento de CPU.
C) latência de impressora.
D) normalização de banco.

### Questão 47 — Questão autoral no estilo Instituto Consulplan

Um sistema embarcado usa firmware para inicializar dispositivo e carregar configurações básicas. A afirmação mais adequada é:

A) firmware atua em nível baixo e pode inicializar/controlar hardware antes do sistema completo.
B) firmware só existe depois que o usuário abre o editor de texto.
C) firmware é sempre armazenado apenas em RAM volátil.
D) firmware é um tipo de consulta agregada.

### Questão 48 — Questão autoral no estilo Instituto Consulplan

Em arquitetura de computadores, a principal função dos registradores de propósito geral é:

A) guardar permanentemente todos os arquivos do usuário.
B) substituir o sistema de arquivos.
C) controlar diretamente o registro profissional no CRA.
D) armazenar temporariamente operandos, endereços ou resultados usados pela CPU.

### Questão 49 — Questão autoral no estilo Instituto Consulplan

Uma operação de polling contínuo para verificar se um dispositivo terminou uma tarefa tende a ser menos eficiente que interrupções porque:

A) polling é sinônimo de memória cache L2.
B) interrupções impedem qualquer retorno ao processo anterior.
C) a CPU gasta tempo verificando repetidamente o dispositivo, mesmo sem novo evento.
D) o dispositivo deixa de existir quando não há interrupção.

### Questão 50 — Questão autoral no estilo Instituto Consulplan

Em uma conversão rápida, o hexadecimal B7 equivale em decimal a:

A) 117.
B) 183.
C) 177.
D) 187.

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

---

# Dia 2 — Sistemas Operacionais

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões

### Questão 1 — Questão autoral no estilo Instituto Consulplan

Em um órgão público, um sistema de protocolo fica lento quando vários usuários acessam relatórios ao mesmo tempo. O sistema operacional atua nesse cenário principalmente para:

A) transformar todo processo em arquivo permanente.
B) gerenciar processos, memória, arquivos e dispositivos compartilhados.
C) substituir o banco de dados relacional em todas as consultas.
D) eliminar a necessidade de autenticação de usuários.

### Questão 2 — Questão autoral no estilo Instituto Consulplan

Considere as assertivas.

I. Programa é um conjunto de instruções armazenado.
II. Processo é um programa em execução, com contexto e recursos associados.
III. Thread é sempre um processo totalmente independente, sem compartilhar recursos.

Está correto apenas o que se afirma em:

A) I e II.
B) I e III.
C) II e III.
D) I, II e III.

### Questão 3 — Questão autoral no estilo Instituto Consulplan

Um processo que aguarda leitura de disco ser concluída normalmente está no estado:

A) executando na CPU.
B) pronto, obrigatoriamente.
C) zumbi desde o início da leitura.
D) bloqueado/esperando.

### Questão 4 — Questão autoral no estilo Instituto Consulplan

No escalonamento preemptivo, o sistema operacional:

A) desativa interrupções de temporizador permanentemente.
B) executa apenas um programa por inicialização do computador.
C) pode interromper um processo em execução para dar CPU a outro.
D) precisa esperar o processo terminar voluntariamente em todos os casos.

### Questão 5 — Questão autoral no estilo Instituto Consulplan

Em um servidor com pouca RAM, o uso intenso de swap começa a degradar o desempenho. Esse fenômeno se relaciona diretamente a:

A) conversão de arquivos NTFS para ext4 sem reinicialização.
B) paginação excessiva e possível thrashing.
C) aumento automático do clock da CPU.
D) eliminação de falhas de página.

### Questão 6 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre paginação e segmentação.

A) Paginação usa blocos de tamanho fixo; segmentação usa divisões lógicas de tamanho variável.
B) Paginação usa apenas blocos variáveis; segmentação usa apenas frames fixos.
C) Paginação impede memória virtual.
D) Segmentação é uma política de backup de arquivos.

### Questão 7 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre memória virtual.

A) Pode apoiar execução de programas maiores que a RAM disponível, com uso de armazenamento secundário.
B) Ajuda na proteção entre processos.
C) É exatamente a mesma coisa que a memória RAM física instalada.
D) Permite que cada processo tenha uma visão própria de espaço de endereçamento.

### Questão 8 — Questão autoral no estilo Instituto Consulplan

Um arquivo `C:\Dados\relatorio.pdf` no Windows e `/home/ana/relatorio.pdf` no Linux são exemplos de:

A) permissões de execução.
B) nomes de processos em execução.
C) caminhos absolutos.
D) caminhos relativos.

### Questão 9 — Questão autoral no estilo Instituto Consulplan

Um sistema de arquivos com journaling reduz risco de inconsistência após queda de energia porque:

A) elimina permissões de acesso.
B) mantém registros auxiliares de operações para recuperação da estrutura do sistema de arquivos.
C) substitui cópias de segurança de todos os documentos do órgão.
D) impede qualquer falha física no disco.

### Questão 10 — Questão autoral no estilo Instituto Consulplan

No Linux, a sequência `chmod 640 arquivo.txt` define, em termos gerais:

A) permissões diferentes para usuário, grupo e outros.
B) a troca de proprietário do arquivo para o usuário 640.
C) a criação de um novo processo com PID 640.
D) a compactação do arquivo usando nível 640.

### Questão 11 — Questão autoral no estilo Instituto Consulplan

Em um serviço Windows, a execução em segundo plano significa que:

A) o processo nunca consome CPU ou memória.
B) o serviço é sempre malware.
C) o serviço não pode ser registrado em logs.
D) o serviço pode executar tarefas sem interação direta contínua do usuário.

### Questão 12 — Questão autoral no estilo Instituto Consulplan

Um driver de impressora instalado incorretamente pode impedir impressão porque o driver:

A) substitui o spool de impressão e todos os serviços.
B) é sempre dispensável em qualquer hardware moderno.
C) é o software que permite ao SO comunicar-se adequadamente com o dispositivo.
D) é a memória física que armazena todos os arquivos impressos.

### Questão 13 — Questão autoral no estilo Instituto Consulplan

Duas threads incrementam a mesma variável global sem sincronização. Em execuções diferentes, o resultado final varia. O problema descrito é:

A) falha de página irrecuperável.
B) condição de corrida.
C) deadlock por espera circular obrigatória.
D) fragmentação externa de memória.

### Questão 14 — Questão autoral no estilo Instituto Consulplan

Um mutex é usado quando se deseja:

A) garantir exclusão mútua no acesso a uma região crítica.
B) aumentar o tamanho da RAM física.
C) ordenar arquivos em ordem alfabética.
D) substituir o escalonador do sistema operacional.

### Questão 15 — Questão autoral no estilo Instituto Consulplan

Considere o cenário: Processo A segura o recurso X e aguarda Y; Processo B segura Y e aguarda X. Se nenhum recurso for liberado, há exemplo de:

A) cache hit.
B) spooling de impressão.
C) starvation sem posse de recurso.
D) deadlock por espera circular.

### Questão 16 — Questão autoral no estilo Instituto Consulplan

As condições clássicas associadas ao deadlock incluem:

A) seleção, projeção, junção e divisão.
B) volatilidade, persistência, Unicode e ASCII.
C) exclusão mútua, posse e espera, não preempção e espera circular.
D) legalidade, impessoalidade, moralidade e publicidade.

### Questão 17 — Questão autoral no estilo Instituto Consulplan

Um processo finalizou, mas seu processo pai ainda não coletou o status de término em sistema Unix-like. Esse processo é chamado de:

A) thread daemon obrigatória.
B) zumbi.
C) órfão sempre em execução ativa.
D) bloqueado por E/S.

### Questão 18 — Questão autoral no estilo Instituto Consulplan

V/F: Sobre chamadas de sistema.

I. Chamadas de sistema permitem que programas solicitem serviços controlados do kernel.
II. Operações de arquivo e E/S podem envolver chamadas de sistema.
III. Chamadas de sistema substituem a CPU durante a execução.

A sequência correta é:

A) V, V, F.
B) V, F, V.
C) F, V, V.
D) F, F, V.

### Questão 19 — Questão autoral no estilo Instituto Consulplan

Um administrador usa `ps` e `top` em Linux para investigar lentidão. Essas ferramentas ajudam principalmente a:

A) alterar permissões de arquivos.
B) formatar partições obrigatoriamente.
C) compilar kernel automaticamente.
D) observar processos e consumo de recursos.

### Questão 20 — Questão autoral no estilo Instituto Consulplan

Em uma política Round Robin, um quantum muito pequeno tende a:

A) impedir preempção.
B) transformar processos I/O-bound em arquivos.
C) aumentar a frequência de trocas de contexto.
D) eliminar todo overhead de escalonamento.

### Questão 21 — Questão autoral no estilo Instituto Consulplan

Um processo CPU-bound é aquele que:

A) é sempre um processo zumbi.
B) usa intensamente processamento, com menor tempo relativo aguardando E/S.
C) passa a maior parte do tempo esperando disco e rede.
D) não pode ser escalonado.

### Questão 22 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre permissões e usuários em sistemas operacionais.

A) Permissões ajudam a controlar leitura, escrita e execução de arquivos.
B) Ambientes multiusuário exigem controle de identidade e autorização.
C) Usuário administrador/root deve ser usado com cautela.
D) Permissão de arquivo elimina a necessidade de autenticação de usuários.

### Questão 23 — Questão autoral no estilo Instituto Consulplan

Uma atualização do sistema operacional em servidor crítico deve ser:

A) sempre aplicada sem teste e sem janela de manutenção.
B) sempre proibida em órgãos públicos.
C) considerada substituta de logs e backup.
D) planejada, testada quando possível e acompanhada de política de backup/rollback.

### Questão 24 — Questão autoral no estilo Instituto Consulplan

Um sistema operacional registra eventos de autenticação, falhas de serviço e erros de dispositivo. Esses registros são importantes porque:

A) substituem a necessidade de controle de acesso.
B) são sempre apagados antes de qualquer análise.
C) ajudam auditoria, diagnóstico e investigação de incidentes.
D) impedem automaticamente todo ataque.

### Questão 25 — Questão autoral no estilo Instituto Consulplan

Em um sistema multitarefa, a troca de contexto consiste em:

A) executar apenas processos finalizados.
B) salvar o estado de uma tarefa e restaurar o estado de outra.
C) renomear arquivos temporários.
D) converter memória virtual em ROM.

### Questão 26 — Questão autoral no estilo Instituto Consulplan

A diferença entre caminho relativo e absoluto é que:

A) o absoluto identifica o caminho a partir da raiz/unidade; o relativo depende do diretório atual.
B) o relativo sempre começa com C:\ e o absoluto nunca começa com /.
C) o absoluto só existe em redes TCP/IP.
D) o relativo contém permissões de execução obrigatoriamente.

### Questão 27 — Questão autoral no estilo Instituto Consulplan

Em sistemas Unix-like, `chown` é usado para:

A) alterar apenas bits de permissão numérica como 755.
B) listar processos ativos.
C) encerrar processo por sinal.
D) alterar proprietário e/ou grupo de arquivo.

### Questão 28 — Questão autoral no estilo Instituto Consulplan

Um processo sofre starvation quando:

A) termina e aguarda coleta pelo processo pai.
B) acessa dado presente na cache.
C) permanece indefinidamente sem receber recurso/CPU por política desfavorável.
D) entra em espera circular segurando recurso de outro processo obrigatoriamente.

### Questão 29 — Questão autoral no estilo Instituto Consulplan

Em virtualização, uma máquina virtual:

A) só pode executar um editor de texto.
B) executa um ambiente isolado sobre camada de virtualização e recursos físicos compartilhados.
C) elimina completamente a necessidade de hardware físico.
D) é sinônimo de memória virtual.

### Questão 30 — Questão autoral no estilo Instituto Consulplan

Um sistema com alta taxa de falhas de página provavelmente está:

A) buscando páginas ausentes na memória física, possivelmente com acesso a disco.
B) executando todas as instruções diretamente da cache L1 sem falta.
C) sem memória virtual por definição.
D) apenas trocando proprietário de arquivos.

### Questão 31 — Questão autoral no estilo Instituto Consulplan

Um servidor usa fila de impressão para organizar documentos enviados por vários setores. Essa técnica se relaciona a:

A) deadlock necessariamente.
B) segmentação de memória.
C) linkedição de bibliotecas.
D) spooling.

### Questão 32 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre NTFS e ext4.

A) São formatos de registradores da CPU.
B) São protocolos de e-mail.
C) São sistemas de arquivos, comuns respectivamente em Windows e Linux.
D) São algoritmos de escalonamento de CPU.

### Questão 33 — Questão autoral no estilo Instituto Consulplan

O comando `kill` em Linux:

A) lista exclusivamente diretórios ocultos.
B) envia sinais a processos, frequentemente para solicitar encerramento.
C) remove fisicamente o processador do computador.
D) altera permissões de arquivo para 755.

### Questão 34 — Questão autoral no estilo Instituto Consulplan

Um serviço travado mantém um lock e impede outros processos de avançar. A primeira análise técnica deve verificar:

A) se há recurso compartilhado retido e dependências de espera entre processos.
B) se a crase foi usada corretamente no nome do serviço.
C) se a chave primária do banco é sempre nula.
D) se o monitor possui resolução 4K.

### Questão 35 — Questão autoral no estilo Instituto Consulplan

Uma política de backup consistente para estações e servidores deve considerar:

A) apenas a existência de journaling no sistema de arquivos.
B) somente copiar atalhos da área de trabalho.
C) desativar logs para economizar espaço sempre.
D) periodicidade, retenção, teste de restauração e proteção contra perda/ataque.

### Questão 36 — Questão autoral no estilo Instituto Consulplan

Em um ambiente com múltiplos usuários, o isolamento entre processos contribui para:

A) dispensar permissões de arquivos.
B) eliminar autenticação no login.
C) impedir que um processo acesse indevidamente memória de outro.
D) proibir qualquer comunicação legítima entre processos.

### Questão 37 — Questão autoral no estilo Instituto Consulplan

Um administrador observa que um processo consome 95% de CPU por longo tempo, mas quase não acessa disco. Uma classificação inicial plausível é:

A) arquivo relativo.
B) CPU-bound.
C) I/O-bound.
D) processo zumbi.

### Questão 38 — Questão autoral no estilo Instituto Consulplan

V/F: Sobre deadlock.

I. Espera circular é uma das condições clássicas.
II. Todo processo bloqueado está necessariamente em deadlock.
III. Prevenção pode atacar uma das condições necessárias.

A sequência correta é:

A) V, F, V.
B) V, V, F.
C) F, V, V.
D) F, F, V.

### Questão 39 — Questão autoral no estilo Instituto Consulplan

Em sistemas operacionais, a diferença entre autenticação e autorização é:

A) autenticação define permissões e autorização verifica identidade, sempre nessa ordem invertida.
B) ambas significam exatamente a mesma coisa.
C) autorização é usada apenas para memória cache.
D) autenticação verifica identidade; autorização define permissões de acesso.

### Questão 40 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre sistemas multitarefa.

A) Multitarefa impede uso de interrupções.
B) Multitarefa só existe quando não há sistema operacional.
C) A alternância rápida entre processos pode dar aparência de execução simultânea em uma CPU.
D) Multitarefa exige obrigatoriamente um núcleo físico para cada processo existente.

### Questão 41 — Questão autoral no estilo Instituto Consulplan

Um arquivo possui permissão de leitura para o grupo, mas não para “outros”. Isso significa que:

A) o arquivo se torna processo em execução.
B) usuários pertencentes ao grupo podem ler, enquanto usuários fora do grupo e não proprietários podem não ter essa permissão.
C) qualquer usuário externo sempre pode ler o arquivo.
D) o proprietário perde automaticamente todas as permissões.

### Questão 42 — Questão autoral no estilo Instituto Consulplan

O kernel oferece chamadas de sistema para operações de arquivo porque:

A) aplicações não devem manipular hardware e estruturas críticas diretamente sem controle.
B) aplicações precisam sempre escrever setores físicos manualmente.
C) o sistema de arquivos não possui permissões.
D) o kernel é apenas uma interface gráfica.

### Questão 43 — Questão autoral no estilo Instituto Consulplan

Um processo órfão em Unix-like é aquele cujo:

A) estado já terminou e só aguarda coleta de status pelo pai.
B) arquivo executável foi apagado antes de iniciar.
C) mutex foi liberado corretamente.
D) processo pai terminou antes dele, e ele passa a ser adotado por outro processo do sistema.

### Questão 44 — Questão autoral no estilo Instituto Consulplan

Assinale a incorreta sobre swap.

A) Uso excessivo pode degradar o desempenho.
B) Tem a mesma latência e velocidade da memória cache L1.
C) Pode apoiar a memória virtual quando a RAM está pressionada.
D) É normalmente mais lento que acesso à RAM.

### Questão 45 — Questão autoral no estilo Instituto Consulplan

Um administrador quer saber quais serviços subiram com falha após reinicialização em Linux com systemd. O comando mais relacionado é:

A) chown -R /, pois muda todos os donos e resolve falhas.
B) systemctl status ou journalctl, conforme o caso.
C) chmod 777, pois sempre corrige serviços.
D) SELECT * FROM services, pois serviços são tabelas SQL.

### Questão 46 — Questão autoral no estilo Instituto Consulplan

Em Windows, permissões NTFS são relevantes porque:

A) controlam acesso a arquivos e pastas por usuários/grupos.
B) substituem integralmente autenticação de domínio.
C) servem apenas para colorir ícones.
D) só existem em mídias FAT32.

### Questão 47 — Questão autoral no estilo Instituto Consulplan

Uma aplicação faz muitas leituras de rede e fica frequentemente bloqueada aguardando resposta externa. Ela tende a ser:

A) CPU-bound puro.
B) processo zumbi.
C) interrupção não mascarável.
D) I/O-bound.

### Questão 48 — Questão autoral no estilo Instituto Consulplan

Assinale a correta sobre monitores, semáforos e mutexes.

A) São modos de endereçamento da CPU.
B) São tipos de backup incremental.
C) São mecanismos/conceitos usados para sincronização de concorrência.
D) São sistemas de arquivos do Windows.

### Questão 49 — Questão autoral no estilo Instituto Consulplan

Um servidor sofreu queda brusca de energia. Após reiniciar, o sistema de arquivos usa seu journal para reduzir inconsistências. Mesmo assim, o administrador deve:

A) desativar logs para impedir análise.
B) validar dados e usar backups se houver perda ou corrupção de arquivos.
C) descartar todos os backups por serem redundantes.
D) remover todas as permissões para acelerar o disco.

### Questão 50 — Questão autoral no estilo Instituto Consulplan

Em uma região crítica, a ausência de sincronização adequada pode gerar:

A) inconsistência de dados por acesso concorrente.
B) aumento automático de espaço em disco.
C) criação automática de usuários.
D) desativação de todo o escalonamento.

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

---

# Dia 3 — Banco de Dados Base e SQL

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões

### Questão 1 — Questão autoral no estilo Instituto Consulplan

Em um sistema do CRA, a tabela `profissional(id_profissional, nome, uf, situacao)` deve retornar apenas profissionais ativos do Paraná. A consulta correta é:

A) SELECT nome FROM profissional WHERE uf = 'PR' AND situacao = 'ATIVO';
B) SELECT nome FROM profissional GROUP BY uf = 'PR' AND situacao = 'ATIVO';
C) SELECT nome FROM profissional ORDER BY uf = 'PR' AND situacao = 'ATIVO';
D) SELECT nome FROM profissional HAVING uf = 'PR' AND situacao = 'ATIVO';

### Questão 2 — Questão autoral no estilo Instituto Consulplan

A tabela `anuidade(id_anuidade, id_profissional, ano, valor)` deve retornar o total de anuidades por ano. Assinale a consulta adequada.

A) SELECT ano, COUNT(*) AS total FROM anuidade WHERE ano;
B) SELECT ano, total FROM anuidade ORDER BY COUNT(*);
C) UPDATE anuidade SET total = COUNT(*) GROUP BY ano;
D) SELECT ano, COUNT(*) AS total FROM anuidade GROUP BY ano;

### Questão 3 — Questão autoral no estilo Instituto Consulplan

Para listar apenas setores com mais de 20 profissionais cadastrados, considerando `profissional(id, setor)`, a consulta correta é:

A) SELECT setor FROM profissional HAVING setor > 20;
B) SELECT setor, COUNT(*) FROM profissional ORDER BY COUNT(*) > 20;
C) SELECT setor, COUNT(*) FROM profissional GROUP BY setor HAVING COUNT(*) > 20;
D) SELECT setor, COUNT(*) FROM profissional WHERE COUNT(*) > 20 GROUP BY setor;

### Questão 4 — Questão autoral no estilo Instituto Consulplan

No modelo relacional, `id_profissional` em `anuidade` referenciando `profissional(id_profissional)` é exemplo de:

A) comando DDL.
B) chave estrangeira.
C) chave candidata obrigatoriamente única em anuidade.
D) atributo multivalorado em 1FN.

### Questão 5 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre chave primária.

A) Identifica unicamente cada linha e não deve aceitar valor nulo.
B) Serve apenas para ordenar alfabeticamente a tabela.
C) Pode repetir livremente valores em uma mesma tabela.
D) É sempre formada por exatamente uma coluna textual.

### Questão 6 — Questão autoral no estilo Instituto Consulplan

Um relacionamento N:N entre `usuario` e `perfil` deve ser implementado, no modelo relacional, por:

A) uma coluna `perfis` contendo lista separada por vírgula em `usuario`.
B) a exclusão da entidade `perfil` para evitar duplicidade.
C) uma chave estrangeira obrigatoriamente única em `usuario`.
D) uma tabela associativa, como `usuario_perfil(id_usuario, id_perfil)`.

### Questão 7 — Questão autoral no estilo Instituto Consulplan

Uma tabela `matricula(id_aluno, id_disciplina, nome_aluno, nome_disciplina)` tem chave composta `(id_aluno, id_disciplina)`. O problema de normalização mais evidente é:

A) violação de ACID, pois há campos textuais.
B) ausência de SQL, pois tabela normalizada não possui nomes.
C) violação da 2FN, pois nomes dependem apenas de parte da chave composta.
D) violação da 1FN, pois toda chave composta é proibida.

### Questão 8 — Questão autoral no estilo Instituto Consulplan

A tabela `servidor(id_servidor, id_departamento, nome_departamento)` pode violar a 3FN porque:

A) a 3FN exige que toda tabela tenha exatamente duas colunas.
B) `nome_departamento` depende de `id_departamento`, que não é a chave primária da tabela servidor.
C) toda tabela com campo textual viola 3FN.
D) a presença de chave estrangeira é proibida na 3FN.

### Questão 9 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa que diferencia corretamente `DELETE` e `DROP`.

A) `DELETE` remove linhas; `DROP` remove objeto de banco, como uma tabela.
B) `DELETE` remove a tabela inteira do catálogo; `DROP` remove apenas linhas filtradas.
C) Ambos são sinônimos e sempre preservam a estrutura da tabela.
D) `DROP` é usado para filtrar registros com `WHERE`.

### Questão 10 — Questão autoral no estilo Instituto Consulplan

Em `UPDATE profissional SET situacao = 'INATIVO';`, sem cláusula WHERE, o efeito provável é:

A) alterar apenas a primeira linha por padrão SQL.
B) não alterar nenhuma linha, pois WHERE é obrigatório em todo UPDATE.
C) remover a tabela `profissional`.
D) alterar a situação de todas as linhas da tabela.

### Questão 11 — Questão autoral no estilo Instituto Consulplan

Para localizar registros sem e-mail cadastrado em `profissional(email)`, usa-se:

A) WHERE email == NULL
B) WHERE NULL(email)
C) WHERE email IS NULL
D) WHERE email = NULL

### Questão 12 — Questão autoral no estilo Instituto Consulplan

Considere as tabelas `profissional(id, nome)` e `anuidade(id, id_profissional, ano)`. Para listar profissionais e suas anuidades, a junção correta é:

A) SELECT p.nome, a.ano FROM profissional p WHERE a.id_profissional = p.id;
B) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id_profissional = p.id;
C) SELECT p.nome, a.ano FROM profissional p JOIN anuidade a ON a.id = p.nome;
D) SELECT p.nome, a.ano FROM profissional p, anuidade a;

### Questão 13 — Questão autoral no estilo Instituto Consulplan

Um relatório deve mostrar todos os profissionais, mesmo os que ainda não possuem anuidade lançada. A junção mais adequada, partindo de `profissional`, é:

A) LEFT JOIN anuidade.
B) INNER JOIN anuidade.
C) CROSS JOIN anuidade.
D) JOIN sem ON obrigatório.

### Questão 14 — Questão autoral no estilo Instituto Consulplan

Em SQL, `COUNT(*)` e `COUNT(email)` podem produzir resultados diferentes porque:

A) `COUNT(*)` conta apenas linhas com e-mail preenchido.
B) `COUNT(email)` sempre conta todas as linhas da tabela.
C) Ambas as formas são inválidas em SQL.
D) `COUNT(email)` ignora valores NULL na coluna, enquanto `COUNT(*)` conta linhas.

### Questão 15 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre `PRIMARY KEY`, `UNIQUE` e `NOT NULL`.

A) `NOT NULL` cria automaticamente relacionamento entre tabelas.
B) `PRIMARY KEY` permite valores repetidos se houver índice.
C) `PRIMARY KEY` combina unicidade e não nulidade; `UNIQUE` impede repetição; `NOT NULL` impede ausência de valor.
D) `UNIQUE` e `NOT NULL` são sinônimos perfeitos.

### Questão 16 — Questão autoral no estilo Instituto Consulplan

Um analista deseja impedir que `valor_anuidade` seja negativo. A restrição mais adequada é:

A) DROP valor_anuidade.
B) CHECK (valor_anuidade >= 0).
C) FOREIGN KEY (valor_anuidade).
D) ORDER BY valor_anuidade.

### Questão 17 — Questão autoral no estilo Instituto Consulplan

V/F: Sobre SQL.

I. `CREATE TABLE` é comando DDL.
II. `GRANT` é comando relacionado a controle de privilégios.
III. `COMMIT` desfaz uma transação confirmada.

A sequência correta é:

A) V, V, F.
B) V, F, V.
C) F, V, F.
D) V, V, V.

### Questão 18 — Questão autoral no estilo Instituto Consulplan

Em uma transação de pagamento, o sistema deve registrar pagamento e baixar débito. Se a baixa falhar, o registro do pagamento também deve ser desfeito. Essa exigência representa:

A) projeção.
B) cardinalidade.
C) ordenamento.
D) atomicidade.

### Questão 19 — Questão autoral no estilo Instituto Consulplan

Um índice criado sobre `numero_processo` tende a:

A) eliminar a necessidade de backup.
B) substituir a chave estrangeira em relacionamentos.
C) melhorar consultas filtradas por `numero_processo`, com custo adicional em inserções/atualizações.
D) garantir por si só que não haverá valores repetidos.

### Questão 20 — Questão autoral no estilo Instituto Consulplan

Uma view `vw_profissionais_ativos` pode ser usada para:

A) executar sempre antes de qualquer trigger.
B) oferecer uma visão lógica filtrada dos dados.
C) armazenar obrigatoriamente cópia física independente em todo SGBD.
D) substituir todas as permissões do banco automaticamente.

### Questão 21 — Questão autoral no estilo Instituto Consulplan

Uma trigger definida para executar após `INSERT` em `anuidade` é:

A) rotina disparada automaticamente por evento de inserção.
B) consulta manual que o usuário deve sempre chamar por SELECT.
C) restrição que só impede NULL.
D) índice criado para melhorar busca textual.

### Questão 22 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre stored procedures.

A) São sempre idênticas a views simples.
B) São obrigatoriamente chaves primárias compostas.
C) São comandos DDL usados exclusivamente para apagar tabelas.
D) Podem encapsular lógica e comandos SQL armazenados no SGBD.

### Questão 23 — Questão autoral no estilo Instituto Consulplan

Em álgebra relacional, seleção e projeção correspondem, respectivamente, a:

A) criar índices e apagar tabelas.
B) confirmar e desfazer transações.
C) filtrar linhas e escolher colunas.
D) escolher colunas e filtrar linhas.

### Questão 24 — Questão autoral no estilo Instituto Consulplan

Em modelagem conceitual, uma entidade é:

A) um backup incremental.
B) um objeto ou conceito relevante do domínio, como Profissional ou Processo.
C) uma coluna obrigatoriamente numérica.
D) uma consulta SQL com WHERE.

### Questão 25 — Questão autoral no estilo Instituto Consulplan

Um atributo multivalorado no MER, como vários telefones de uma pessoa, costuma ser tratado no modelo relacional por:

A) tabela separada ou estrutura relacional que permita múltiplos valores atômicos.
B) uma única coluna com todos os telefones separados por vírgula.
C) excluir os telefones excedentes.
D) usar `ORDER BY telefone` como substituto da modelagem.

### Questão 26 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre independência física de dados.

A) Qualquer alteração física exige reescrever todas as consultas sempre.
B) Significa que dados não precisam de SGBD.
C) Significa apagar as regras de integridade.
D) Mudanças em armazenamento ou índices podem ocorrer sem alterar necessariamente a visão lógica da aplicação.

### Questão 27 — Questão autoral no estilo Instituto Consulplan

Um dicionário de dados é importante porque:

A) é uma tabela obrigatória de senhas em texto claro.
B) é usado apenas para ordenar alfabeticamente relatórios.
C) armazena metadados sobre tabelas, colunas, restrições e objetos do banco.
D) substitui todos os dados de negócio.

### Questão 28 — Questão autoral no estilo Instituto Consulplan

Em uma consulta `SELECT setor, salario FROM servidor GROUP BY setor;`, considerando regras SQL usuais, há problema porque:

A) SELECT não permite listar mais de uma coluna.
B) `salario` não está agregado nem aparece no GROUP BY.
C) `setor` jamais pode aparecer em GROUP BY.
D) GROUP BY só pode ser usado com DELETE.

### Questão 29 — Questão autoral no estilo Instituto Consulplan

Um usuário executa `DELETE FROM profissional WHERE situacao = 'INATIVO';`. O comando:

A) remove linhas que atendem à condição, preservando a estrutura da tabela.
B) remove a tabela `profissional` do banco.
C) altera a situação para INATIVO.
D) cria cópia de segurança antes de apagar.

### Questão 30 — Questão autoral no estilo Instituto Consulplan

Para inserir novo profissional com nome e UF, a estrutura correta é:

A) SELECT INTO profissional (nome, uf) VALUES ('Ana Lima', 'PR');
B) UPDATE INTO profissional VALUES ('Ana Lima', 'PR');
C) DROP INTO profissional VALUES ('Ana Lima', 'PR');
D) INSERT INTO profissional (nome, uf) VALUES ('Ana Lima', 'PR');

### Questão 31 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre transações concorrentes.

A) Toda concorrência elimina a necessidade de COMMIT.
B) Concorrência impede qualquer uso de índices.
C) Níveis de isolamento controlam interferências como leituras sujas e não repetíveis.
D) Isolamento significa que o banco só aceita um usuário por dia.

### Questão 32 — Questão autoral no estilo Instituto Consulplan

Um cadastro guarda `cpf` com restrição UNIQUE, mas a chave primária é `id_pessoa`. Isso significa que:

A) UNIQUE permite duplicidade quando há índice.
B) `cpf` não deve repetir, mas a identificação primária da linha é `id_pessoa`.
C) `cpf` obrigatoriamente é a chave primária.
D) `id_pessoa` pode repetir livremente por existir CPF UNIQUE.

### Questão 33 — Questão autoral no estilo Instituto Consulplan

Em `profissional(id, nome, id_cidade)` e `cidade(id, nome)`, uma consulta para listar profissional e cidade deve relacionar:

A) profissional.id_cidade = cidade.id.
B) profissional.id = cidade.nome.
C) profissional.nome = cidade.id.
D) profissional.id_cidade = profissional.id.

### Questão 34 — Questão autoral no estilo Instituto Consulplan

Assinale a incorreta sobre normalização.

A) A 2FN evita dependência parcial em chave composta.
B) A 3FN evita dependência transitiva.
C) Normalizar significa sempre eliminar todas as tabelas auxiliares para reduzir joins.
D) A 1FN busca atributos atômicos.

### Questão 35 — Questão autoral no estilo Instituto Consulplan

Uma consulta precisa mostrar os três maiores valores de anuidade. Em SQL padrão/variações de SGBD, a ideia correta envolve:

A) usar WHERE valor DESC.
B) usar DROP para remover valores menores.
C) ordenar por valor decrescente e limitar o resultado conforme o SGBD.
D) usar GROUP BY valor para garantir os maiores valores.

### Questão 36 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre `TRUNCATE` em comparação com `DELETE`.

A) `TRUNCATE` é comando de consulta equivalente a SELECT.
B) `TRUNCATE` remove dados da tabela de forma estruturalmente mais ampla/rápida em muitos SGBDs, sem filtro linha a linha como DELETE com WHERE.
C) `TRUNCATE` sempre remove apenas uma linha escolhida por WHERE.
D) `DELETE` remove obrigatoriamente a estrutura da tabela.

### Questão 37 — Questão autoral no estilo Instituto Consulplan

Um relatório exibe profissionais mesmo quando a cidade não foi cadastrada. A consulta usa `LEFT JOIN cidade`. Quando não há cidade correspondente, as colunas de `cidade` tendem a aparecer como:

A) NULL.
B) zero obrigatoriamente.
C) texto “ERRO” automaticamente.
D) a chave primária da tabela esquerda.

### Questão 38 — Questão autoral no estilo Instituto Consulplan

Em modelagem, se uma pessoa jurídica pode ter vários responsáveis técnicos ao longo do tempo, e um profissional pode responder por várias pessoas jurídicas, a modelagem mais flexível é:

A) guardar todos os responsáveis em uma coluna texto da pessoa jurídica.
B) permitir apenas um responsável por profissional em todo o sistema.
C) usar apenas o nome do profissional sem chave.
D) criar relacionamento associativo com atributos como data_inicio e data_fim.

### Questão 39 — Questão autoral no estilo Instituto Consulplan

Assinale a correta sobre backup lógico de banco de dados.

A) Dispensa teste de restauração.
B) Substitui controle de permissões.
C) Pode exportar estrutura e dados em formato recuperável, conforme ferramenta do SGBD.
D) É sempre idêntico a copiar os arquivos físicos abertos sem consistência.

### Questão 40 — Questão autoral no estilo Instituto Consulplan

Uma tabela `documento(id_documento, tags)` armazena várias tags separadas por ponto e vírgula na coluna `tags`. O principal problema é:

A) impossibilidade de qualquer consulta SELECT.
B) violação da atomicidade esperada na 1FN.
C) excesso de chaves estrangeiras.
D) uso obrigatório de HAVING.

### Questão 41 — Questão autoral no estilo Instituto Consulplan

Em um sistema, `numero_registro` deve ser obrigatório e não repetido, mas a PK técnica é `id`. Uma combinação adequada de restrições é:

A) NOT NULL e UNIQUE em `numero_registro`.
B) apenas CHECK (numero_registro IS NULL).
C) apenas FOREIGN KEY em `numero_registro` sem tabela referenciada.
D) ORDER BY numero_registro na criação da tabela.

### Questão 42 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa que melhor descreve SGBD.

A) Planilha isolada sem controle de integridade ou concorrência.
B) Apenas o arquivo físico com extensão `.db`.
C) Somente a linguagem SQL, sem mecanismos de controle.
D) Software que gerencia armazenamento, consulta, integridade, segurança e transações de dados.

### Questão 43 — Questão autoral no estilo Instituto Consulplan

Um usuário recebeu permissão apenas de leitura em uma tabela. O comando relacionado a conceder essa permissão é:

A) DROP SELECT ON tabela TO usuario;
B) UPDATE SELECT ON tabela TO usuario;
C) GRANT SELECT ON tabela TO usuario;
D) REVOKE SELECT ON tabela FROM usuario;

### Questão 44 — Questão autoral no estilo Instituto Consulplan

Em uma tabela de auditoria, uma trigger registra automaticamente alterações após UPDATE em `profissional`. A principal vantagem é:

A) substituir todos os backups.
B) automatizar o registro de eventos relevantes sem depender de ação manual do usuário.
C) impedir qualquer UPDATE em todas as situações.
D) eliminar necessidade de transações.

### Questão 45 — Questão autoral no estilo Instituto Consulplan

Assinale a correta sobre cardinalidade mínima e máxima no MER.

A) Indicam, em termos de participação, quantas ocorrências podem ou devem se relacionar.
B) Definem apenas a cor do losango no diagrama.
C) São comandos SQL executados no SELECT.
D) Substituem chaves primárias no modelo relacional.

### Questão 46 — Questão autoral no estilo Instituto Consulplan

Se um atributo `cpf` determina `nome` e `nome` determina `id_setor`, em uma mesma tabela cujo identificador é `cpf`, há risco de:

A) ausência de qualquer dependência funcional.
B) violação obrigatória de 1FN por haver CPF.
C) comando DCL inválido.
D) dependência transitiva, se `id_setor` depende indiretamente da chave por meio de `nome`.

### Questão 47 — Questão autoral no estilo Instituto Consulplan

Um comando `SELECT DISTINCT uf FROM profissional;` retorna:

A) apaga UFs duplicadas da tabela.
B) cria índice único sobre `uf`.
C) as UFs distintas existentes no resultado.
D) todas as linhas originais, inclusive UFs repetidas.

### Questão 48 — Questão autoral no estilo Instituto Consulplan

Uma aplicação precisa garantir que duas operações de débito e crédito ocorram juntas. A propriedade de durabilidade em ACID garante que:

A) ROLLBACK confirme os dados definitivamente.
B) após COMMIT, os efeitos confirmados persistam mesmo diante de falhas previstas pelo SGBD.
C) a transação nunca precise de log.
D) a transação sempre ignore isolamento.

### Questão 49 — Questão autoral no estilo Instituto Consulplan

Assinale a incorreta sobre joins.

A) INNER JOIN retorna apenas linhas com correspondência segundo a condição.
B) LEFT JOIN preserva as linhas da tabela à esquerda.
C) Condição de junção mal definida pode produzir resultados incorretos ou produto cartesiano.
D) JOIN sempre dispensa qualquer relação lógica entre as tabelas.

### Questão 50 — Questão autoral no estilo Instituto Consulplan

Uma consulta `SELECT situacao, COUNT(*) FROM profissional GROUP BY situacao ORDER BY COUNT(*) DESC;` tem como efeito:

A) alterar a situação de todos os profissionais.
B) remover situações repetidas da tabela física.
C) filtrar apenas grupos com total maior que zero por HAVING.
D) contar profissionais por situação e ordenar os grupos do maior para o menor total.

## Gabarito do Dia 3

1. A
2. D
3. C
4. B
5. A
6. D
7. C
8. B
9. A
10. D
11. C
12. B
13. A
14. D
15. C
16. B
17. A
18. D
19. C
20. B
21. A
22. D
23. C
24. B
25. A
26. D
27. C
28. B
29. A
30. D
31. C
32. B
33. A
34. C
35. C
36. B
37. A
38. D
39. C
40. B
41. A
42. D
43. C
44. B
45. A
46. D
47. C
48. B
49. D
50. D

## Comentários do Dia 3

### Comentário da Questão 1

- **Alternativa correta:** A.
- **A) está correta:** A cláusula WHERE filtra simultaneamente UF e situação.
- **B) está errada:** GROUP BY agrupa linhas; não é usado para filtrar condições booleanas dessa forma.
- **C) está errada:** ORDER BY ordena o resultado; não filtra registros.
- **D) está errada:** HAVING é usado para filtrar grupos agregados; aqui o filtro é de linhas.
- **Conceito cobrado:** SELECT com WHERE.
- **Pegadinha usada:** Trocar WHERE por GROUP BY, ORDER BY ou HAVING..
- **Como pensar para acertar:** Filtro de linha antes de agregação pede WHERE.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 2

- **Alternativa correta:** D.
- **A) está errada:** WHERE ano não agrupa nem calcula corretamente por ano.
- **B) está errada:** Não há coluna total definida e falta agrupamento.
- **C) está errada:** UPDATE altera dados; não é consulta de totalização.
- **D) está correta:** COUNT com GROUP BY ano calcula o total por ano.
- **Conceito cobrado:** GROUP BY e COUNT.
- **Pegadinha usada:** Usar função agregada sem agrupamento adequado..
- **Como pensar para acertar:** Quando a pergunta pede “por ano”, pense em GROUP BY ano.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 3

- **Alternativa correta:** C.
- **A) está errada:** A condição não usa agregação e setor não é quantidade.
- **B) está errada:** ORDER BY ordena; não filtra grupos.
- **C) está correta:** HAVING filtra grupos após o agrupamento por setor.
- **D) está errada:** WHERE não filtra agregações como COUNT(*) depois do agrupamento.
- **Conceito cobrado:** GROUP BY e HAVING.
- **Pegadinha usada:** Confundir WHERE e HAVING..
- **Como pensar para acertar:** WHERE filtra linhas; HAVING filtra grupos.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 4

- **Alternativa correta:** B.
- **A) está errada:** A coluna é elemento estrutural; a questão pergunta o papel relacional.
- **B) está correta:** A coluna na tabela anuidade aponta para a chave de profissional.
- **C) está errada:** Várias anuidades podem pertencer ao mesmo profissional; não precisa ser única.
- **D) está errada:** É uma coluna atômica de referência, não uma lista multivalorada.
- **Conceito cobrado:** Chave estrangeira.
- **Pegadinha usada:** Achar que toda FK é única..
- **Como pensar para acertar:** Pergunte: a coluna aponta para registro de outra tabela? Então é FK.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 5

- **Alternativa correta:** A.
- **A) está correta:** Chave primária garante identificação única e integridade de entidade.
- **B) está errada:** Ordenação é feita por ORDER BY ou índices, não pela definição conceitual de PK.
- **C) está errada:** Repetição violaria unicidade da chave primária.
- **D) está errada:** Pode ser simples ou composta e não precisa ser textual.
- **Conceito cobrado:** Chave primária.
- **Pegadinha usada:** Reduzir chave primária a ordenação ou texto..
- **Como pensar para acertar:** PK responde “como identifico uma linha de modo único?”.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 6

- **Alternativa correta:** D.
- **A) está errada:** Lista no campo viola atomicidade e dificulta integridade.
- **B) está errada:** Excluir entidade perde informação do domínio.
- **C) está errada:** FK única representaria no máximo 1:1/1:N limitado, não N:N.
- **D) está correta:** Relacionamentos N:N viram tabela intermediária com FKs.
- **Conceito cobrado:** Mapeamento N:N.
- **Pegadinha usada:** Usar lista em coluna para múltiplos valores..
- **Como pensar para acertar:** N:N quase sempre exige tabela associativa.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 7

- **Alternativa correta:** C.
- **A) está errada:** ACID é propriedade de transações, não forma normal.
- **B) está errada:** Tabelas podem ter atributos textuais; o problema é dependência parcial.
- **C) está correta:** nome_aluno depende de id_aluno; nome_disciplina depende de id_disciplina.
- **D) está errada:** Chave composta não viola 1FN por si só.
- **Conceito cobrado:** Segunda Forma Normal.
- **Pegadinha usada:** Não reconhecer dependência parcial..
- **Como pensar para acertar:** Quando a chave é composta, veja se atributo depende da chave inteira.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 8

- **Alternativa correta:** B.
- **A) está errada:** Não existe essa exigência.
- **B) está correta:** Há dependência transitiva de atributo não chave.
- **C) está errada:** Campos textuais são permitidos.
- **D) está errada:** Chaves estrangeiras são compatíveis com normalização.
- **Conceito cobrado:** Terceira Forma Normal.
- **Pegadinha usada:** Confundir dependência transitiva com presença de texto..
- **Como pensar para acertar:** Procure atributo não chave determinando outro atributo não chave.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 9

- **Alternativa correta:** A.
- **A) está correta:** DELETE é DML; DROP é DDL.
- **B) está errada:** A alternativa inverte os comandos.
- **C) está errada:** DROP não preserva a tabela.
- **D) está errada:** DROP não é comando de filtro de registros.
- **Conceito cobrado:** DELETE x DROP.
- **Pegadinha usada:** Confundir remoção de dados com remoção de estrutura..
- **Como pensar para acertar:** Pergunte: quero apagar linhas ou eliminar o objeto tabela?
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 10

- **Alternativa correta:** D.
- **A) está errada:** SQL não limita automaticamente à primeira linha.
- **B) está errada:** WHERE é recomendável, mas não obrigatório em SQL.
- **C) está errada:** Remover tabela é função de DROP TABLE.
- **D) está correta:** Sem WHERE, UPDATE atinge todos os registros da tabela alvo.
- **Conceito cobrado:** UPDATE sem WHERE.
- **Pegadinha usada:** Subestimar efeito de comando sem filtro..
- **Como pensar para acertar:** Sempre procure WHERE em comandos de alteração.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 11

- **Alternativa correta:** C.
- **A) está errada:** Além de não ser SQL padrão nesse contexto, mantém erro conceitual de comparar NULL.
- **B) está errada:** Essa não é forma padrão de testar ausência de valor.
- **C) está correta:** NULL deve ser testado com IS NULL.
- **D) está errada:** NULL não deve ser comparado com `=` como valor comum.
- **Conceito cobrado:** NULL e IS NULL.
- **Pegadinha usada:** Comparar NULL como se fosse valor comum..
- **Como pensar para acertar:** NULL significa ausência/desconhecido; use IS NULL.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 12

- **Alternativa correta:** B.
- **A) está errada:** A tabela `a` não foi declarada no FROM/JOIN.
- **B) está correta:** A junção relaciona FK da anuidade à PK do profissional.
- **C) está errada:** Relaciona id de anuidade com nome, campos incompatíveis.
- **D) está errada:** Sem condição de junção, gera produto cartesiano.
- **Conceito cobrado:** JOIN e condição de junção.
- **Pegadinha usada:** Produto cartesiano por falta de ON..
- **Como pensar para acertar:** Identifique PK e FK e escreva a condição de associação.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 13

- **Alternativa correta:** A.
- **A) está correta:** LEFT JOIN preserva todas as linhas da tabela à esquerda.
- **B) está errada:** INNER JOIN traria apenas profissionais com correspondência em anuidade.
- **C) está errada:** CROSS JOIN gera combinações sem correspondência lógica.
- **D) está errada:** Junção sem condição tende a erro ou produto cartesiano.
- **Conceito cobrado:** LEFT JOIN.
- **Pegadinha usada:** Usar INNER JOIN quando precisa preservar ausência de correspondência..
- **Como pensar para acertar:** Se quer todos da tabela esquerda, pense em LEFT JOIN.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 14

- **Alternativa correta:** D.
- **A) está errada:** COUNT(*) conta linhas do grupo, independentemente de coluna específica.
- **B) está errada:** COUNT(coluna) não conta NULLs daquela coluna.
- **C) está errada:** Ambas são formas comuns e válidas.
- **D) está correta:** Funções agregadas tratam NULL de forma específica.
- **Conceito cobrado:** Funções agregadas e NULL.
- **Pegadinha usada:** Ignorar o tratamento de NULL em agregações..
- **Como pensar para acertar:** Veja se a contagem é de linhas ou de valores não nulos da coluna.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 15

- **Alternativa correta:** C.
- **A) está errada:** Relacionamento é função de chave estrangeira.
- **B) está errada:** Repetição violaria a chave primária.
- **C) está correta:** Cada restrição tem papel próprio.
- **D) está errada:** Um valor pode ser obrigatório sem ser único, ou único conforme regra sem ser PK.
- **Conceito cobrado:** Restrições de integridade.
- **Pegadinha usada:** Confundir unicidade, obrigatoriedade e relacionamento..
- **Como pensar para acertar:** Separe: único, obrigatório, identificador e referência.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 16

- **Alternativa correta:** B.
- **A) está errada:** DROP removeria objeto/coluna conforme sintaxe, não validaria regra.
- **B) está correta:** CHECK valida regra de domínio para a coluna.
- **C) está errada:** FK referencia outra tabela; não valida faixa numérica por si só.
- **D) está errada:** ORDER BY apenas ordena resultado.
- **Conceito cobrado:** CHECK constraint.
- **Pegadinha usada:** Usar FK ou ordenação para validação de domínio..
- **Como pensar para acertar:** Regra sobre valor permitido sugere CHECK.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 17

- **Alternativa correta:** A.
- **A) está correta:** I e II estão corretas; COMMIT confirma, não desfaz.
- **B) está errada:** GRANT realmente controla privilégios e COMMIT não desfaz.
- **C) está errada:** CREATE TABLE é DDL.
- **D) está errada:** III está errada: quem desfaz é ROLLBACK antes da confirmação.
- **Conceito cobrado:** DDL, DCL e TCL.
- **Pegadinha usada:** Trocar COMMIT e ROLLBACK..
- **Como pensar para acertar:** Classifique comandos pelo efeito: estrutura, privilégio, transação.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 18

- **Alternativa correta:** D.
- **A) está errada:** Projeção escolhe colunas na álgebra relacional.
- **B) está errada:** Cardinalidade descreve relacionamentos entre entidades.
- **C) está errada:** Ordenamento não trata consistência transacional.
- **D) está correta:** Atomicidade exige tudo ou nada na transação.
- **Conceito cobrado:** ACID: atomicidade.
- **Pegadinha usada:** Confundir propriedades transacionais com modelagem..
- **Como pensar para acertar:** Quando operações dependem entre si, pense em tudo-ou-nada.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 19

- **Alternativa correta:** C.
- **A) está errada:** Índice não protege contra perda de dados.
- **B) está errada:** Índice e FK têm funções diferentes.
- **C) está correta:** Índices aceleram leitura, mas exigem manutenção.
- **D) está errada:** Índice comum não garante unicidade; para isso há índice/constraint UNIQUE.
- **Conceito cobrado:** Índices.
- **Pegadinha usada:** Tratar índice como solução universal..
- **Como pensar para acertar:** Índice melhora alguns acessos, mas não substitui integridade nem backup.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 20

- **Alternativa correta:** B.
- **A) está errada:** View e trigger têm funções diferentes.
- **B) está correta:** View encapsula consulta e apresenta recorte lógico.
- **C) está errada:** Nem toda view é materializada.
- **D) está errada:** Views podem ajudar segurança, mas não substituem gestão de privilégios.
- **Conceito cobrado:** Views.
- **Pegadinha usada:** Achar que toda view materializa dados..
- **Como pensar para acertar:** Pense em view como consulta/visão lógica, salvo caso materializado.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 21

- **Alternativa correta:** A.
- **A) está correta:** Trigger responde a evento definido no banco.
- **B) está errada:** Trigger é automática conforme evento.
- **C) está errada:** Isso é NOT NULL; trigger pode ter lógica mais ampla.
- **D) está errada:** Índice não é rotina de evento.
- **Conceito cobrado:** Triggers.
- **Pegadinha usada:** Confundir trigger com procedure chamada manualmente..
- **Como pensar para acertar:** A palavra-chave é “disparada por evento”.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 22

- **Alternativa correta:** D.
- **A) está errada:** Views representam consultas; procedures executam lógica.
- **B) está errada:** Procedure não é chave.
- **C) está errada:** Procedures podem conter lógica variada; não são DROP.
- **D) está correta:** Procedures permitem reaproveitar rotinas no banco.
- **Conceito cobrado:** Stored procedures.
- **Pegadinha usada:** Confundir procedure e view..
- **Como pensar para acertar:** Procedure faz; view mostra/representa consulta.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 23

- **Alternativa correta:** C.
- **A) está errada:** São operações de administração/DDL, não seleção/projeção.
- **B) está errada:** Isso se relaciona a COMMIT/ROLLBACK.
- **C) está correta:** Seleção restringe tuplas; projeção restringe atributos.
- **D) está errada:** A alternativa inverte os conceitos.
- **Conceito cobrado:** Álgebra relacional.
- **Pegadinha usada:** Inverter seleção e projeção..
- **Como pensar para acertar:** Seleção lembra condição sobre linhas; projeção lembra colunas projetadas.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 24

- **Alternativa correta:** B.
- **A) está errada:** Backup não é elemento de MER.
- **B) está correta:** Entidade representa algo sobre o qual se deseja guardar dados.
- **C) está errada:** Coluna é atributo no modelo relacional.
- **D) está errada:** Consulta não é entidade conceitual.
- **Conceito cobrado:** Modelo Entidade-Relacionamento.
- **Pegadinha usada:** Confundir entidade com atributo ou consulta..
- **Como pensar para acertar:** Entidade costuma virar tabela no modelo lógico.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 25

- **Alternativa correta:** A.
- **A) está correta:** Isso preserva 1FN e integridade.
- **B) está errada:** Isso viola atomicidade e dificulta consultas.
- **C) está errada:** Perde informação necessária.
- **D) está errada:** Ordenação não resolve multivaloração.
- **Conceito cobrado:** Atributos multivalorados e 1FN.
- **Pegadinha usada:** Guardar listas em uma coluna..
- **Como pensar para acertar:** Múltiplos valores pedem múltiplas linhas/entidade associada.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 26

- **Alternativa correta:** D.
- **A) está errada:** A independência busca reduzir esse impacto.
- **B) está errada:** A independência é propriedade da arquitetura do SGBD.
- **C) está errada:** Integridade continua necessária.
- **D) está correta:** Essa é a ideia de independência física.
- **Conceito cobrado:** Independência física de dados.
- **Pegadinha usada:** Confundir ajuste físico com mudança lógica obrigatória..
- **Como pensar para acertar:** Índice é bom exemplo: muda desempenho/armazenamento sem mudar consulta.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 27

- **Alternativa correta:** C.
- **A) está errada:** Senhas em texto claro seriam falha grave; não define dicionário.
- **B) está errada:** Dicionário de dados descreve estrutura, não apenas ordenação.
- **C) está correta:** Dicionário contém dados sobre os dados.
- **D) está errada:** Metadados não substituem registros de negócio.
- **Conceito cobrado:** Dicionário de dados e metadados.
- **Pegadinha usada:** Não distinguir dados e metadados..
- **Como pensar para acertar:** Dicionário responde “como o banco está estruturado?”.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 28

- **Alternativa correta:** B.
- **A) está errada:** SELECT pode listar múltiplas expressões.
- **B) está correta:** Coluna solta junto de agrupamento causa ambiguidade.
- **C) está errada:** Pelo contrário, setor é a coluna agrupada.
- **D) está errada:** GROUP BY é cláusula de consulta SELECT.
- **Conceito cobrado:** GROUP BY e colunas não agregadas.
- **Pegadinha usada:** Selecionar coluna fora do agrupamento..
- **Como pensar para acertar:** Toda coluna no SELECT deve ser agregada ou fazer parte do agrupamento.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 29

- **Alternativa correta:** A.
- **A) está correta:** DELETE remove registros filtrados.
- **B) está errada:** Isso seria DROP TABLE.
- **C) está errada:** Isso seria UPDATE, não DELETE.
- **D) está errada:** SQL não garante backup automático nesse comando.
- **Conceito cobrado:** DELETE com WHERE.
- **Pegadinha usada:** Confundir DELETE com DROP ou UPDATE..
- **Como pensar para acertar:** Observe o verbo SQL: DELETE remove linhas; UPDATE altera valores.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 30

- **Alternativa correta:** D.
- **A) está errada:** SELECT não é a forma padrão de inserção simples com VALUES.
- **B) está errada:** UPDATE altera linhas existentes; não usa essa estrutura.
- **C) está errada:** DROP remove objetos; não insere dados.
- **D) está correta:** INSERT INTO ... VALUES adiciona registro.
- **Conceito cobrado:** INSERT.
- **Pegadinha usada:** Trocar comandos DML..
- **Como pensar para acertar:** Inserir nova linha pede INSERT INTO.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 31

- **Alternativa correta:** C.
- **A) está errada:** COMMIT continua necessário para confirmar transações.
- **B) está errada:** Índices e concorrência podem coexistir.
- **C) está correta:** Isolamento trata efeitos de concorrência entre transações.
- **D) está errada:** Isolamento não proíbe concorrência; controla seus efeitos.
- **Conceito cobrado:** Isolamento transacional.
- **Pegadinha usada:** Confundir isolamento com ausência total de concorrência..
- **Como pensar para acertar:** Isolamento é controle de efeitos, não proibição absoluta de simultaneidade.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 32

- **Alternativa correta:** B.
- **A) está errada:** UNIQUE existe justamente para impedir duplicidade conforme regra.
- **B) está correta:** UNIQUE garante unicidade sem necessariamente ser a PK.
- **C) está errada:** UNIQUE não torna automaticamente o campo PK.
- **D) está errada:** A PK não pode repetir.
- **Conceito cobrado:** UNIQUE x PRIMARY KEY.
- **Pegadinha usada:** Tratar UNIQUE como PK automaticamente..
- **Como pensar para acertar:** Unicidade pode existir em campos que não são a chave primária.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 33

- **Alternativa correta:** A.
- **A) está correta:** A FK id_cidade aponta para a PK de cidade.
- **B) está errada:** Relaciona identificador a texto de forma incorreta.
- **C) está errada:** Relaciona nome textual a identificador.
- **D) está errada:** Relaciona colunas da mesma tabela sem alcançar cidade.
- **Conceito cobrado:** Condição de JOIN por PK/FK.
- **Pegadinha usada:** Juntar colunas com nomes parecidos sem respeitar relacionamento..
- **Como pensar para acertar:** Identifique FK na tabela filha e PK na tabela referenciada.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 34

- **Alternativa correta:** C.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: esse é o ponto clássico da 2FN.
- **B) está correta como afirmação:** Correta: esse é o foco da 3FN.
- **C) é a incorreta:** Incorreta: normalização frequentemente cria separações/tabelas para reduzir redundância.
- **D) está correta como afirmação:** Correta: atomicidade é foco da 1FN.
- **Conceito cobrado:** Normalização.
- **Pegadinha usada:** Achar que normalizar é juntar tudo para evitar joins..
- **Como pensar para acertar:** Normalização reduz redundância; desempenho pode exigir avaliação posterior.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 35

- **Alternativa correta:** C.
- **A) está errada:** WHERE filtra condições, não ordena.
- **B) está errada:** DROP remove objetos e não deve ser usado para relatório.
- **C) está correta:** ORDER BY valor DESC combinado a LIMIT/FETCH/TOP conforme o SGBD resolve a necessidade.
- **D) está errada:** GROUP BY agrupa; não seleciona top N por si só.
- **Conceito cobrado:** ORDER BY e limitação de resultados.
- **Pegadinha usada:** Confundir ordenação com filtro/agrupamento..
- **Como pensar para acertar:** Para maiores/menores, pense em ORDER BY; para quantidade, em LIMIT/FETCH/TOP.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 36

- **Alternativa correta:** B.
- **A) está errada:** TRUNCATE não consulta dados.
- **B) está correta:** TRUNCATE costuma remover todas as linhas e tem comportamento próprio por SGBD.
- **C) está errada:** TRUNCATE não é usado com filtro linha a linha como DELETE.
- **D) está errada:** DELETE remove linhas; estrutura permanece.
- **Conceito cobrado:** DELETE x TRUNCATE.
- **Pegadinha usada:** Tratar todos os comandos de remoção como iguais..
- **Como pensar para acertar:** Diferencie apagar linhas filtradas, esvaziar tabela e remover objeto.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 37

- **Alternativa correta:** A.
- **A) está correta:** LEFT JOIN preserva a linha da esquerda e preenche ausência da direita com NULL.
- **B) está errada:** Ausência em junção externa é representada por NULL, não zero por regra geral.
- **C) está errada:** SGBD não preenche automaticamente com esse texto.
- **D) está errada:** Colunas da direita ausentes não viram PK da esquerda.
- **Conceito cobrado:** LEFT JOIN e NULL.
- **Pegadinha usada:** Não entender como ausência de correspondência é representada..
- **Como pensar para acertar:** LEFT preserva a esquerda; o que falta da direita vira NULL.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 38

- **Alternativa correta:** D.
- **A) está errada:** Lista textual prejudica integridade e consultas.
- **B) está errada:** Contraria o requisito de múltiplas relações.
- **C) está errada:** Nome não garante identificação nem integridade.
- **D) está correta:** A associação N:N com histórico precisa de tabela própria e atributos do vínculo.
- **Conceito cobrado:** Modelagem de relacionamento com atributos.
- **Pegadinha usada:** Guardar histórico em texto livre..
- **Como pensar para acertar:** Quando o relacionamento tem dados próprios, ele merece tabela própria.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 39

- **Alternativa correta:** C.
- **A) está errada:** Backup sem teste pode falhar quando necessário.
- **B) está errada:** Backup e segurança de acesso são controles distintos.
- **C) está correta:** Backups lógicos usam dumps/exportações para restauração.
- **D) está errada:** Cópia física sem consistência pode ser inválida.
- **Conceito cobrado:** Backup e recuperação em SGBD.
- **Pegadinha usada:** Achar que qualquer cópia de arquivo aberto é backup válido..
- **Como pensar para acertar:** Backup precisa ser consistente e restaurável.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 40

- **Alternativa correta:** B.
- **A) está errada:** SELECT ainda é possível, mas consultas e integridade ficam ruins.
- **B) está correta:** Múltiplos valores em uma única coluna violam 1FN.
- **C) está errada:** O problema é ausência de estrutura relacional, não excesso de FK.
- **D) está errada:** HAVING não corrige multivaloração.
- **Conceito cobrado:** 1FN e atributos multivalorados.
- **Pegadinha usada:** Aceitar lista em campo como modelagem normalizada..
- **Como pensar para acertar:** Se há vários valores no mesmo campo, suspeite de 1FN.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 41

- **Alternativa correta:** A.
- **A) está correta:** Obrigatoriedade vem de NOT NULL; não repetição vem de UNIQUE.
- **B) está errada:** Essa condição permitiria/forçaria nulidade, o oposto da exigência.
- **C) está errada:** FK exige referência; não resolve unicidade/obrigatoriedade sozinha.
- **D) está errada:** ORDER BY não cria restrição de integridade.
- **Conceito cobrado:** NOT NULL e UNIQUE.
- **Pegadinha usada:** Misturar restrição de domínio, unicidade e ordenação..
- **Como pensar para acertar:** Traduza requisito: obrigatório = NOT NULL; não repetido = UNIQUE.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 42

- **Alternativa correta:** D.
- **A) está errada:** Planilha não é SGBD completo.
- **B) está errada:** O arquivo pode armazenar dados, mas SGBD é o software gerenciador.
- **C) está errada:** SQL é linguagem; SGBD inclui vários serviços.
- **D) está correta:** Essa é a função do sistema gerenciador de banco de dados.
- **Conceito cobrado:** SGBD.
- **Pegadinha usada:** Confundir banco, arquivo, linguagem e gerenciador..
- **Como pensar para acertar:** Procure a camada que oferece serviços de gerenciamento dos dados.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 43

- **Alternativa correta:** C.
- **A) está errada:** DROP remove objetos e não concede privilégio.
- **B) está errada:** UPDATE altera dados e não concede privilégio.
- **C) está correta:** GRANT concede privilégio; SELECT é privilégio de leitura.
- **D) está errada:** REVOKE remove permissão, não concede.
- **Conceito cobrado:** DCL: GRANT e REVOKE.
- **Pegadinha usada:** Trocar concessão e revogação..
- **Como pensar para acertar:** Permissão concedida = GRANT; permissão retirada = REVOKE.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 44

- **Alternativa correta:** B.
- **A) está errada:** Auditoria não substitui backup.
- **B) está correta:** Trigger pode executar lógica de auditoria ao ocorrer evento.
- **C) está errada:** Trigger pode validar/bloquear dependendo da lógica, mas auditoria não significa proibição automática.
- **D) está errada:** Transações continuam importantes.
- **Conceito cobrado:** Triggers de auditoria.
- **Pegadinha usada:** Achar que trigger sempre bloqueia operação..
- **Como pensar para acertar:** Veja o evento: após UPDATE, registre automaticamente.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 45

- **Alternativa correta:** A.
- **A) está correta:** Cardinalidade modela obrigatoriedade e quantidade de vínculos.
- **B) está errada:** Cor visual não é cardinalidade.
- **C) está errada:** Cardinalidade é conceito de modelagem.
- **D) está errada:** Cardinalidade orienta mapeamento, mas não substitui chaves.
- **Conceito cobrado:** Cardinalidade no MER.
- **Pegadinha usada:** Reduzir cardinalidade a detalhe visual..
- **Como pensar para acertar:** Pergunte: uma ocorrência se relaciona com quantas da outra?
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 46

- **Alternativa correta:** D.
- **A) está errada:** O enunciado descreve dependências.
- **B) está errada:** CPF como atributo atômico não viola 1FN por si só.
- **C) está errada:** A questão é de normalização, não de privilégios.
- **D) está correta:** A 3FN busca evitar dependências transitivas.
- **Conceito cobrado:** Dependência funcional e 3FN.
- **Pegadinha usada:** Não seguir a cadeia de dependência..
- **Como pensar para acertar:** Monte a relação: chave -> atributo não chave -> outro atributo.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 47

- **Alternativa correta:** C.
- **A) está errada:** SELECT não altera fisicamente os dados.
- **B) está errada:** DISTINCT não cria restrição nem índice.
- **C) está correta:** DISTINCT elimina duplicidades no resultado projetado.
- **D) está errada:** DISTINCT remove repetições na projeção.
- **Conceito cobrado:** DISTINCT.
- **Pegadinha usada:** Confundir resultado da consulta com alteração permanente..
- **Como pensar para acertar:** SELECT consulta; não muda dados sem comando de modificação.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 48

- **Alternativa correta:** B.
- **A) está errada:** ROLLBACK desfaz, não confirma.
- **B) está correta:** Durabilidade trata permanência após confirmação.
- **C) está errada:** Logs são mecanismos comuns para durabilidade.
- **D) está errada:** Isolamento é outra propriedade ACID.
- **Conceito cobrado:** ACID: durabilidade.
- **Pegadinha usada:** Trocar durabilidade por atomicidade ou rollback..
- **Como pensar para acertar:** Depois do COMMIT, o banco deve preservar o que foi confirmado.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 49

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: sem correspondência, a linha fica fora.
- **B) está correta como afirmação:** Correta: a esquerda é mantida mesmo sem correspondência.
- **C) está correta como afirmação:** Correta: ON inadequado distorce o resultado.
- **D) é a incorreta:** Incorreta: a junção útil depende de relação lógica e condição adequada.
- **Conceito cobrado:** JOINs.
- **Pegadinha usada:** Achar que basta juntar tabelas sem condição lógica..
- **Como pensar para acertar:** JOIN bom nasce do relacionamento do modelo.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

### Comentário da Questão 50

- **Alternativa correta:** D.
- **A) está errada:** SELECT não altera dados.
- **B) está errada:** Agrupamento não apaga registros.
- **C) está errada:** Não há HAVING na consulta; apenas ordenação.
- **D) está correta:** GROUP BY agrega por situação; ORDER BY COUNT(*) DESC ordena por total decrescente.
- **Conceito cobrado:** GROUP BY e ORDER BY com agregação.
- **Pegadinha usada:** Confundir consulta agregada com alteração física..
- **Como pensar para acertar:** Leia cláusula por cláusula: SELECT, GROUP BY, ORDER BY.
- **Referência à apostila de estudo:** Dia 3 — Banco de Dados Base e SQL.

---

# Dia 4 — Legislação CRA-PR/CFA

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

**Confirmação prévia das normas do Dia 4:** foram utilizadas fontes oficiais para orientar as questões de Lei 4.769/1965, Decreto 61.934/1967, Lei 12.514/2011, RN CFA 649/2024, RN CFA 670/2025, RN CFA 546/2018, RN CFA 626/2023, RN CFA 589/2020, RN CFA 651/2024, RN CFA 671/2025, RN CFA 680/2025 e Regimento Interno do CRA-PR. As questões evitam cobrar artigo, prazo ou penalidade específica quando isso exigiria reprodução literal ou confirmação pontual além da ementa/fonte oficial consultada.

## Questões

### Questão 1 — Questão autoral no estilo Instituto Consulplan

Uma empresa no Paraná divulga serviços típicos de Administração sem regularidade perante o CRA competente. Em tese, a situação se relaciona principalmente com:

A) competência exclusiva do Poder Judiciário para criar registro profissional administrativo.
B) dispensa automática de registro por possuir CNPJ ativo.
C) matéria apenas tributária municipal, sem relação com conselho profissional.
D) registro e fiscalização pelo CRA-PR, conforme legislação profissional e regulamentos do Sistema CFA/CRAs.

### Questão 2 — Questão autoral no estilo Instituto Consulplan

Um profissional usa o número de registro de outro para assinar documento técnico. À luz do estudo do Código de Ética, a conduta:

A) é irrelevante porque registro é apenas dado cadastral sem efeito profissional.
B) é sempre resolvida apenas por correção ortográfica do documento.
C) é incompatível com a ética profissional e pode envolver uso indevido de nome ou registro.
D) é regular se o documento for entregue em meio eletrônico.

### Questão 3 — Questão autoral no estilo Instituto Consulplan

O CRA-PR identifica pessoa física exercendo atividade privativa da área de Administração sem registro. A atuação mais compatível com sua finalidade institucional é:

A) ignorar a situação por não envolver anuidade paga.
B) fiscalizar a regularidade do exercício profissional em sua jurisdição.
C) editar lei federal para punir criminalmente o interessado.
D) substituir automaticamente a atuação de todos os demais órgãos públicos.

### Questão 4 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre a relação entre CFA e CRA.

A) O CFA exerce função normativa/orientadora em âmbito federal do sistema, enquanto o CRA atua regionalmente.
B) O CRA-PR pode alterar sozinho normas nacionais para todos os CRAs.
C) O CFA é subordinado administrativamente ao CRA-PR.
D) Cada município paranaense possui um CFA próprio.

### Questão 5 — Questão autoral no estilo Instituto Consulplan

A RN CFA nº 651/2024 aparece no estudo porque:

A) é o Código de Ética vigente indicado no edital.
B) aprova o Regulamento das Eleições do Sistema CFA/CRAs.
C) institui o Programa Especial de Recuperação de Créditos.
D) aprova o Regimento Interno do CRA-PR.

### Questão 6 — Questão autoral no estilo Instituto Consulplan

Segundo o edital vigente usado no material, o Código de Ética e Disciplina deve ser estudado com base na:

A) Lei nº 14.133/2021.
B) RN CFA nº 649/2024 apenas.
C) RN CFA nº 671/2025.
D) RN CFA nº 651/2024.

### Questão 7 — Questão autoral no estilo Instituto Consulplan

Um administrador toma conhecimento de informação sensível de cliente em razão de atividade profissional lícita. A conduta esperada, segundo a lógica do Código de Ética, é:

A) omitir a informação de fiscalização legítima em qualquer hipótese.
B) guardar sigilo, salvo justa causa ou hipótese legal/profissional cabível.
C) divulgar a informação sempre que isso gere vantagem comercial.
D) publicar a informação em relatório aberto sem avaliar necessidade.

### Questão 8 — Questão autoral no estilo Instituto Consulplan

Uma pessoa jurídica registrada no CRA dificulta deliberadamente uma fiscalização regular. O caso se relaciona mais diretamente com:

A) deveres perante a fiscalização e possível infração ética/administrativa.
B) direito irrestrito de impedir qualquer atuação do conselho.
C) mero erro de concordância sem relevância institucional.
D) competência exclusiva do setor de informática do órgão.

### Questão 9 — Questão autoral no estilo Instituto Consulplan

A Lei Federal nº 4.769/1965 é base de estudo porque:

A) define comandos SQL para bancos relacionais.
B) aprova o Regimento Interno do CRA-PR de 2024.
C) regulamenta exclusivamente a Lei de Licitações.
D) dispõe sobre o exercício da profissão de Administrador e fundamenta o Sistema CFA/CRAs.

### Questão 10 — Questão autoral no estilo Instituto Consulplan

O Decreto Federal nº 61.934/1967 deve ser lido em conjunto com a Lei nº 4.769/1965 porque:

A) cria nova Constituição para os CRAs.
B) trata de Unicode e representação de dados.
C) regulamenta a lei profissional.
D) revoga integralmente a lei que regulamenta.

### Questão 11 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre o CRA-PR conforme estudado.

A) É órgão municipal subordinado à prefeitura de Curitiba.
B) É autarquia de direito público, com jurisdição no Estado do Paraná.
C) É sindicato privado de adesão facultativa sem função fiscalizatória.
D) Tem jurisdição nacional sobre todos os administradores do país.

### Questão 12 — Questão autoral no estilo Instituto Consulplan

Um caso envolve orientação normativa geral para todos os Conselhos Regionais de Administração. A competência aponta, em regra, para:

A) CFA.
B) CRA-PR isoladamente.
C) qualquer pessoa jurídica registrada.
D) setor de protocolo de uma prefeitura.

### Questão 13 — Questão autoral no estilo Instituto Consulplan

A RN CFA nº 649/2024 e a RN CFA nº 670/2025 devem ser estudadas em conjunto porque:

A) ambas aprovam o Código de Ética de 2025.
B) ambas tratam exclusivamente de eleição do sistema.
C) ambas revogam a Lei 4.769/1965.
D) a primeira aprova o Regulamento de Registro e a segunda o altera.

### Questão 14 — Questão autoral no estilo Instituto Consulplan

A RN CFA nº 589/2020 está ligada ao estudo de:

A) regimento interno específico do CRA-PR.
B) eleições do Sistema CFA/CRAs.
C) fiscalização do Sistema CFA/CRAs.
D) código de ética aprovado em 2025.

### Questão 15 — Questão autoral no estilo Instituto Consulplan

A RN CFA nº 626/2023, conforme ementa oficial, relaciona-se ao:

A) Regimento Interno do CRA-PR.
B) Programa Especial de Recuperação de Créditos (PERC).
C) Regulamento de Registro do Sistema CFA/CRAs.
D) Código de Ética e Disciplina.

### Questão 16 — Questão autoral no estilo Instituto Consulplan

A RN CFA nº 546/2018 foi confirmada como norma que trata de:

A) concessão de isenção de débitos pelos CRAs.
B) regulamento eleitoral do Sistema CFA/CRAs.
C) Código de Ética de 2025.
D) normalização de banco de dados.

### Questão 17 — Questão autoral no estilo Instituto Consulplan

A Lei nº 12.514/2011 pode aparecer na prova porque:

A) define as atribuições da ULA em processadores.
B) é o Código de Ética dos Profissionais de Administração.
C) aprova o Regimento Interno do CRA-PR.
D) trata de contribuições devidas aos conselhos profissionais.

### Questão 18 — Questão autoral no estilo Instituto Consulplan

Em um processo ético, uma sanção deve ser analisada:

A) sem qualquer norma, apenas por opinião do fiscal.
B) exclusivamente pelo setor de TI, independentemente do fato.
C) conforme a norma aplicável, a gravidade da conduta e as especificidades de pessoa física ou jurídica.
D) sempre como cancelamento automático do registro, sem gradação.

### Questão 19 — Questão autoral no estilo Instituto Consulplan

Um profissional assina relatório técnico sem ter orientado, supervisionado ou participado do trabalho. A pegadinha provável em prova é tratar isso como:

A) tema de fiscalização e ética profissional.
B) conduta regular por mera autorização verbal informal, o que é inadequado.
C) situação que pode envolver infração ética.
D) uso de registro com responsabilidade profissional.

### Questão 20 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre sigilo profissional.

A) O sigilo protege informações conhecidas em razão da atividade profissional.
B) O sigilo deve ser interpretado com atenção a hipóteses legais e justa causa.
C) O dever de sigilo pode conviver com obrigações legais de fiscalização.
D) O sigilo autoriza divulgar informações sensíveis sempre que houver interesse comercial.

### Questão 21 — Questão autoral no estilo Instituto Consulplan

Um candidato confunde RN 651/2024 com RN 671/2025. A associação correta é:

A) RN 651/2024: Código de Ética; RN 671/2025: Regimento do CRA-PR.
B) Ambas tratam apenas de licitação pública.
C) Ambas tratam apenas de banco de dados relacional.
D) RN 651/2024: Regimento do CRA-PR; RN 671/2025: Código de Ética.

### Questão 22 — Questão autoral no estilo Instituto Consulplan

Em caso de pessoa jurídica atuando em áreas de Administração, o registro no CRA é relevante porque:

A) CNPJ substitui qualquer registro profissional.
B) somente pessoa física pode ser fiscalizada em qualquer hipótese.
C) a fiscalização profissional também pode alcançar pessoas jurídicas conforme a legislação e regulamentos aplicáveis.
D) pessoa jurídica nunca é mencionada no Código de Ética atual.

### Questão 23 — Questão autoral no estilo Instituto Consulplan

A expressão “jurisdição do CRA-PR” no contexto do Regimento deve ser entendida como:

A) abrangência mundial de qualquer empresa paranaense.
B) âmbito territorial de atuação do Conselho Regional no Paraná.
C) competência para julgar crimes federais.
D) espaço de memória virtual do sistema.

### Questão 24 — Questão autoral no estilo Instituto Consulplan

Um cidadão reclama que o CRA-PR não poderia fiscalizar porque “somente sindicatos representam profissões”. A resposta correta é:

A) conselho profissional e sindicato têm naturezas diferentes; o CRA fiscaliza exercício profissional por base legal.
B) o cidadão está correto, pois CRA é sindicato privado.
C) o CRA só pode fiscalizar se houver filiação sindical.
D) o CFA é uma empresa municipal de representação coletiva.

### Questão 25 — Questão autoral no estilo Instituto Consulplan

A RN CFA nº 680/2025, confirmada em fonte oficial, trata de:

A) Regulamento de Registro do Sistema CFA/CRAs.
B) Código de Ética e Disciplina.
C) Regimento Interno do CRA-PR.
D) Regulamento das Eleições do Sistema CFA/CRAs.

### Questão 26 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta sobre o estudo de normas adicionais do edital.

A) Questão autoral pode ser tratada como real se tiver estilo parecido.
B) Norma citada no edital pode ser ignorada por ter leitura difícil.
C) Quando a fonte oficial confirma apenas ementa/objeto, é prudente não criar cobrança de artigo, prazo ou sanção específica sem texto consolidado.
D) É seguro inventar prazo provável se a norma parecer semelhante a outra.

### Questão 27 — Questão autoral no estilo Instituto Consulplan

Um fiscal do CRA solicita documentos para verificar regularidade de atuação. A empresa responde com agressões pessoais e se recusa sem fundamento. O caso pode envolver:

A) competência do SGBD para impor penalidade.
B) violação de deveres de urbanidade e cooperação com fiscalização, conforme normas aplicáveis.
C) exercício regular e irrestrito de impedir qualquer fiscalização.
D) matéria exclusivamente de acentuação gráfica.

### Questão 28 — Questão autoral no estilo Instituto Consulplan

Se uma norma do CFA “altera o Regulamento de Registro”, a forma correta de estudá-la é:

A) ler a norma alteradora junto com o regulamento alterado.
B) ler apenas o número da norma e ignorar seu objeto.
C) substituir todas as normas do edital por ela.
D) usar apenas resumo informal sem fonte.

### Questão 29 — Questão autoral no estilo Instituto Consulplan

O Plenário do CRA-PR, conforme a lógica regimental estudada, é melhor compreendido como:

A) aplicativo de protocolo eletrônico.
B) modalidade de licitação para bens comuns.
C) setor privado sem vínculo com a autarquia.
D) órgão colegiado de deliberação superior.

### Questão 30 — Questão autoral no estilo Instituto Consulplan

A Diretoria Executiva, em comparação com o Plenário, tende a estar mais ligada:

A) à substituição do Código de Ética por ato informal.
B) ao julgamento de comandos SQL.
C) à execução administrativa e condução das atividades institucionais.
D) à edição de leis federais autônomas.

### Questão 31 — Questão autoral no estilo Instituto Consulplan

Um profissional alega que, por ser servidor público, não precisa observar preceitos éticos da profissão ao atuar na área de Administração. A afirmação é:

A) irrelevante porque ética profissional só vale para estudantes.
B) problemática, pois o exercício profissional pode atrair deveres éticos independentemente do vínculo.
C) correta em qualquer hipótese, pois servidor público nunca responde perante conselho.
D) correta apenas se o ato ocorrer em horário comercial.

### Questão 32 — Questão autoral no estilo Instituto Consulplan

Em questão sobre competência do CFA para orientar e disciplinar o exercício profissional, a base normativa geral citada pelas RNs costuma remeter a:

A) Lei nº 4.769/1965 e Decreto nº 61.934/1967.
B) Código de Trânsito Brasileiro apenas.
C) Manual de SQL ANSI.
D) Regimento de uma prefeitura municipal, exclusivamente.

### Questão 33 — Questão autoral no estilo Instituto Consulplan

Assinale a incorreta sobre o Código de Ética estudado.

A) Pode alcançar pessoas jurídicas, observadas especificidades.
B) Inclui temas como sigilo, zelo e independência técnica.
C) Autoriza abdicar da independência técnica sempre que houver pressão do contratante.
D) Trata de deveres e responsabilidades no exercício das atividades de Administração.

### Questão 34 — Questão autoral no estilo Instituto Consulplan

Uma entidade deseja saber por que deve manter cadastro atualizado junto ao CRA. A justificativa mais ligada ao estudo é:

A) cadastro é irrelevante após o primeiro registro.
B) cadastro serve apenas para estética do documento.
C) regularidade cadastral permite comunicação, fiscalização e controle profissional adequados.
D) cadastro atualizado substitui qualquer dever ético.

### Questão 35 — Questão autoral no estilo Instituto Consulplan

Em caso de conflito entre interesse comercial do profissional e dever de proteção do cliente/sociedade, o Código de Ética tende a privilegiar:

A) uso de registro por terceiros para ampliar mercado.
B) conduta responsável, honesta, técnica e compatível com a função social da profissão.
C) vantagem econômica imediata em qualquer hipótese.
D) sigilo apenas quando for conveniente ao profissional.

### Questão 36 — Questão autoral no estilo Instituto Consulplan

Um enunciado diz que a RN CFA nº 649/2024 “aprova o regulamento de registro do sistema CFA/CRAs”. Essa afirmação está:

A) correta, conforme ementa oficial.
B) errada, pois a RN 649 trata de eleição.
C) errada, pois a RN 649 é o Código de Ética.
D) errada, pois a RN 649 aprova o Regimento do CRA-PR.

### Questão 37 — Questão autoral no estilo Instituto Consulplan

Um enunciado afirma que a RN CFA nº 670/2025 revoga a Lei nº 4.769/1965. A afirmação é:

A) correta, pois toda resolução posterior revoga lei anterior.
B) correta apenas se o CRA-PR concordar em sessão interna.
C) ponto de SQL, sem relação com legislação.
D) incorreta, pois a RN 670 altera regulamento de registro aprovado por RN, não revoga lei federal.

### Questão 38 — Questão autoral no estilo Instituto Consulplan

Na leitura dirigida das normas do edital, qual associação está correta?

A) RN 589/2020: SQL; RN 626/2023: SO; RN 680/2025: RLM.
B) RN 589/2020: Regimento CRA-PR; RN 626/2023: Regimento CRA-PR; RN 680/2025: Regimento CRA-PR.
C) RN 589/2020: fiscalização; RN 626/2023: PERC; RN 680/2025: eleições.
D) RN 589/2020: eleições; RN 626/2023: Código de Ética; RN 680/2025: registro.

### Questão 39 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa que melhor representa uma questão realista sobre competência do CRA-PR.

A) Julgar definitivamente ação judicial sobre dano moral.
B) Fiscalizar, em sua jurisdição, o exercício de atividades abrangidas pela legislação profissional.
C) Criar crime federal novo para toda profissão regulamentada.
D) Revogar unilateralmente a RN do CFA em todo o Brasil.

### Questão 40 — Questão autoral no estilo Instituto Consulplan

Um profissional registrado presta serviço em área de Administração e recusa aperfeiçoamento mínimo mesmo diante de mudanças normativas relevantes. O tema se relaciona ao dever de:

A) aperfeiçoamento profissional e atuação responsável.
B) usar registro de terceiro quando não souber o tema.
C) omitir-se sempre que houver novidade normativa.
D) transferir toda responsabilidade ao cliente.

### Questão 41 — Questão autoral no estilo Instituto Consulplan

A defesa dos interesses de quem recebe os serviços profissionais deve ser compreendida:

A) como autorização para fraudar fiscalização se beneficiar o cliente.
B) como dispensa de sigilo e independência técnica.
C) como substituição do Código de Ética por contrato privado.
D) dentro dos limites da lei, da técnica e da ética profissional.

### Questão 42 — Questão autoral no estilo Instituto Consulplan

Em uma questão sobre penalidades, se o enunciado não traz artigo específico e o material não confirmou prazo ou gradação detalhada, a postura correta é:

A) ignorar a existência de sanções éticas.
B) assumir que toda infração tem a mesma consequência.
C) responder apenas com base em conceitos gerais confirmados e evitar inventar detalhe.
D) escolher a maior penalidade sempre.

### Questão 43 — Questão autoral no estilo Instituto Consulplan

Uma pessoa jurídica registrada afirma que o Código de Ética só alcança pessoas físicas. Segundo a RN 671/2025 estudada, a afirmação é:

A) irrelevante, pois Código de Ética não consta do edital.
B) incorreta, pois o Código também contempla pessoas jurídicas, observadas especificidades.
C) correta, pois pessoa jurídica nunca exerce atividade em Administração.
D) correta apenas se a empresa tiver contrato privado.

### Questão 44 — Questão autoral no estilo Instituto Consulplan

Assinale a incorreta sobre fontes oficiais usadas no estudo.

A) O edital vigente deve orientar a seleção das normas a estudar.
B) Textos oficiais do CFA e do Planalto são fontes adequadas para legislação.
C) Provas anteriores ajudam a entender estilo, sem transformar questão autoral em real.
D) Uma questão criada no material pode ser chamada de real se parecer com a Consulplan.

### Questão 45 — Questão autoral no estilo Instituto Consulplan

A finalidade social dos conselhos profissionais se relaciona principalmente com:

A) garantir mercado sem qualquer controle ético.
B) substituir todos os órgãos de controle do Estado.
C) impedir qualquer atuação de profissionais registrados.
D) fiscalizar o exercício profissional para proteger a sociedade e a qualidade dos serviços.

### Questão 46 — Questão autoral no estilo Instituto Consulplan

Se uma empresa explora atividade de Administração e mantém profissional habilitado apenas formalmente, sem atuação real, a banca pode explorar:

A) tema exclusivo de pontuação e crase.
B) inexistência de qualquer competência do CRA.
C) responsabilidade técnica fictícia e uso indevido de registro/nome.
D) regularidade automática pela simples existência de nome no papel.

### Questão 47 — Questão autoral no estilo Instituto Consulplan

Um fiscal regional aplica entendimento nacional uniformizado pelo CFA. Essa situação é compatível com:

A) competência municipal para registro profissional.
B) a relação entre orientação normativa federal do CFA e execução regional pelos CRAs.
C) subordinação do CFA a cada fiscal regional.
D) ausência de qualquer norma nacional no sistema.

### Questão 48 — Questão autoral no estilo Instituto Consulplan

Em prova, uma alternativa diz: “O CRA-PR tem sede na capital do Paraná e jurisdição em todo o Estado”. Com base no Regimento estudado, a frase está:

A) correta.
B) errada, porque a jurisdição é nacional.
C) errada, porque o CRA-PR é órgão municipal.
D) errada, porque conselho profissional não possui jurisdição administrativa.

### Questão 49 — Questão autoral no estilo Instituto Consulplan

A conduta de facilitar o exercício profissional a terceiro não habilitado deve ser vista como:

A) dever ético de solidariedade irrestrita.
B) ato sem qualquer relevância para o CRA.
C) apenas problema de formatação de relatório.
D) potencial infração ética/profissional, conforme o Código e normas aplicáveis.

### Questão 50 — Questão autoral no estilo Instituto Consulplan

Assinale a correta sobre a leitura da Lei 4.769/1965 e do Decreto 61.934/1967.

A) A lei é irrelevante porque há resoluções normativas.
B) Ambos tratam exclusivamente de informática básica.
C) A lei estabelece base legal e o decreto detalha sua regulamentação.
D) O decreto elimina a necessidade de ler a lei.

## Gabarito do Dia 4

1. D
2. C
3. B
4. A
5. D
6. C
7. B
8. A
9. D
10. C
11. B
12. A
13. D
14. C
15. B
16. A
17. D
18. C
19. B
20. D
21. D
22. C
23. B
24. A
25. D
26. C
27. B
28. A
29. D
30. C
31. B
32. A
33. C
34. C
35. B
36. A
37. D
38. C
39. B
40. A
41. D
42. C
43. B
44. D
45. D
46. C
47. B
48. A
49. D
50. C

## Comentários do Dia 4

### Comentário da Questão 1

- **Alternativa correta:** D.
- **A) está errada:** O Judiciário não é o órgão de registro/fiscalização profissional.
- **B) está errada:** CNPJ não substitui regularidade profissional perante conselho quando exigida.
- **C) está errada:** Pode haver tributos, mas o caso descreve fiscalização profissional.
- **D) está correta:** Pessoas jurídicas que atuam em áreas abrangidas podem estar sujeitas a registro/fiscalização.
- **Conceito cobrado:** Registro e fiscalização de pessoa jurídica.
- **Pegadinha usada:** Confundir CNPJ com registro profissional..
- **Como pensar para acertar:** Pergunte se a atividade exercida está no campo fiscalizado pelo Sistema CFA/CRA.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 2

- **Alternativa correta:** C.
- **A) está errada:** Registro identifica habilitação e responsabilidade profissional.
- **B) está errada:** O problema é ético/profissional, não textual.
- **C) está correta:** O Código busca coibir uso indevido de registro e responsabilização técnica fictícia.
- **D) está errada:** O meio de entrega não legitima uso indevido de registro.
- **Conceito cobrado:** Código de Ética: uso indevido de registro.
- **Pegadinha usada:** Tratar registro profissional como formalidade sem consequência..
- **Como pensar para acertar:** Assinatura e registro indicam responsabilidade técnica.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 3

- **Alternativa correta:** B.
- **A) está errada:** Fiscalização não se limita a quem já paga anuidade.
- **B) está correta:** CRAs atuam regionalmente em registro e fiscalização.
- **C) está errada:** CRA não edita lei federal.
- **D) está errada:** Conselho tem competência específica, não universal.
- **Conceito cobrado:** Competência fiscalizatória do CRA.
- **Pegadinha usada:** Confundir competência administrativa com legislativa..
- **Como pensar para acertar:** Conselho regional fiscaliza o exercício profissional no território.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 4

- **Alternativa correta:** A.
- **A) está correta:** Essa é a lógica de sistema federal-regional de conselhos.
- **B) está errada:** Normas nacionais cabem ao CFA, não a um regional isolado.
- **C) está errada:** O CFA ocupa plano federal do sistema; não é subordinado ao regional.
- **D) está errada:** O CFA é federal; os regionais são CRAs.
- **Conceito cobrado:** Competência CFA x CRA.
- **Pegadinha usada:** Trocar plano federal por regional..
- **Como pensar para acertar:** Localize se a ação é normativa nacional ou execução/fiscalização local.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 5

- **Alternativa correta:** D.
- **A) está errada:** O Código de Ética indicado é a RN CFA nº 671/2025.
- **B) está errada:** Esse objeto se relaciona à RN CFA nº 680/2025.
- **C) está errada:** Esse tema se relaciona à RN CFA nº 626/2023.
- **D) está correta:** A norma é fonte de aprovação/organização do Regimento do CRA-PR.
- **Conceito cobrado:** RN CFA 651/2024 e Regimento.
- **Pegadinha usada:** Trocar o número e objeto das resoluções..
- **Como pensar para acertar:** Associe 651 ao Regimento do CRA-PR.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 6

- **Alternativa correta:** C.
- **A) está errada:** Essa lei trata de licitações e contratos administrativos.
- **B) está errada:** A RN 649/2024 trata do regulamento de registro.
- **C) está correta:** O edital conforme Retificação I indica a RN 671/2025, e fonte oficial aponta revogação da RN 640/2024.
- **D) está errada:** A RN 651/2024 aprova o Regimento do CRA-PR, não o Código de Ética.
- **Conceito cobrado:** RN CFA 671/2025.
- **Pegadinha usada:** Usar norma revogada ou norma de objeto diferente..
- **Como pensar para acertar:** Siga o edital vigente e confirme a ementa da norma.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 7

- **Alternativa correta:** B.
- **A) está errada:** Sigilo não é escudo absoluto contra dever legal/fiscalizatório.
- **B) está correta:** Sigilo profissional é dever, mas não deve ser lido de forma absoluta contra a lei.
- **C) está errada:** Vantagem comercial não justifica violar sigilo.
- **D) está errada:** Tratamento de informação deve respeitar sigilo e finalidade.
- **Conceito cobrado:** Sigilo profissional.
- **Pegadinha usada:** Tratar sigilo como inexistente ou absoluto..
- **Como pensar para acertar:** Busque equilíbrio: sigilo é regra ética, mas há hipóteses legais e justa causa.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 8

- **Alternativa correta:** A.
- **A) está correta:** Obstar fiscalização é conduta relevante no sistema de controle profissional.
- **B) está errada:** Fiscalização regular é finalidade institucional do CRA.
- **C) está errada:** O caso é de conduta perante fiscalização.
- **D) está errada:** Não é problema técnico de TI.
- **Conceito cobrado:** Fiscalização do CRA e ética.
- **Pegadinha usada:** Transformar infração em direito do fiscalizado..
- **Como pensar para acertar:** Se há fiscalização regular, dificultar o ato é ponto sensível.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 9

- **Alternativa correta:** D.
- **A) está errada:** SQL é tema de TI, não dessa lei.
- **B) está errada:** O Regimento do CRA-PR é aprovado por RN específica do CFA.
- **C) está errada:** A lei trata da profissão de Administrador.
- **D) está correta:** É a lei estruturante da profissão e do sistema de conselhos.
- **Conceito cobrado:** Lei 4.769/1965.
- **Pegadinha usada:** Misturar lei profissional com outras áreas..
- **Como pensar para acertar:** Identifique a lei base da profissão e dos conselhos.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 10

- **Alternativa correta:** C.
- **A) está errada:** Decreto não substitui Constituição.
- **B) está errada:** Não tem relação com arquitetura de computadores.
- **C) está correta:** Decreto regulamentar detalha a execução da lei.
- **D) está errada:** Decreto regulamentar não revoga a lei regulamentada.
- **Conceito cobrado:** Decreto regulamentar.
- **Pegadinha usada:** Achar que decreto contraria ou substitui lei..
- **Como pensar para acertar:** Decreto regulamenta dentro dos limites da lei.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 11

- **Alternativa correta:** B.
- **A) está errada:** Não é órgão municipal.
- **B) está correta:** O Regimento caracteriza o CRA-PR como autarquia regional.
- **C) está errada:** Conselho profissional não se confunde com sindicato.
- **D) está errada:** A jurisdição do CRA-PR é estadual.
- **Conceito cobrado:** Natureza e jurisdição do CRA-PR.
- **Pegadinha usada:** Confundir conselho, sindicato e órgão municipal..
- **Como pensar para acertar:** Guarde: autarquia, direito público, jurisdição estadual.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 12

- **Alternativa correta:** A.
- **A) está correta:** O CFA exerce papel uniformizador/normativo do sistema.
- **B) está errada:** Um regional não normatiza sozinho todo o sistema.
- **C) está errada:** Registrados cumprem normas; não editam diretrizes nacionais.
- **D) está errada:** Não é órgão do Sistema CFA/CRAs.
- **Conceito cobrado:** Papel normativo do CFA.
- **Pegadinha usada:** Atribuir competência nacional ao regional..
- **Como pensar para acertar:** Nacional/uniformizador sugere CFA.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 13

- **Alternativa correta:** D.
- **A) está errada:** Código de Ética é RN 671/2025.
- **B) está errada:** Regulamento eleitoral é RN 680/2025.
- **C) está errada:** Resolução normativa não revoga a lei profissional.
- **D) está correta:** Norma alteradora precisa ser lida com a norma alterada.
- **Conceito cobrado:** Regulamento de Registro: RN 649 e RN 670.
- **Pegadinha usada:** Ler norma alteradora isoladamente..
- **Como pensar para acertar:** Quando a ementa diz “altera”, volte à norma principal.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 14

- **Alternativa correta:** C.
- **A) está errada:** Esse objeto é da RN 651/2024.
- **B) está errada:** Esse objeto é da RN 680/2025.
- **C) está correta:** A norma aprova o Regulamento de Fiscalização.
- **D) está errada:** Esse objeto é da RN 671/2025.
- **Conceito cobrado:** RN CFA 589/2020.
- **Pegadinha usada:** Confundir fiscalização, ética, regimento e eleição..
- **Como pensar para acertar:** Associe 589 a fiscalização.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 15

- **Alternativa correta:** B.
- **A) está errada:** Regimento do CRA-PR é RN 651/2024.
- **B) está correta:** A ementa da RN 626/2023 indica o PERC.
- **C) está errada:** Registro é RN 649/2024, alterada pela RN 670/2025.
- **D) está errada:** Código de Ética é RN 671/2025.
- **Conceito cobrado:** RN CFA 626/2023.
- **Pegadinha usada:** Trocar recuperação de créditos por registro ou ética..
- **Como pensar para acertar:** PERC = recuperação de créditos.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 16

- **Alternativa correta:** A.
- **A) está correta:** Esse é o objeto indicado na fonte oficial.
- **B) está errada:** Regulamento eleitoral é RN 680/2025.
- **C) está errada:** Código de Ética é RN 671/2025.
- **D) está errada:** Não é tema de legislação CFA/CRA.
- **Conceito cobrado:** RN CFA 546/2018.
- **Pegadinha usada:** Confundir isenção de débitos com PERC ou eleição..
- **Como pensar para acertar:** Associe 546 a isenção de débitos.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 17

- **Alternativa correta:** D.
- **A) está errada:** Isso é arquitetura de computadores.
- **B) está errada:** Código de Ética é RN CFA nº 671/2025.
- **C) está errada:** O Regimento é aprovado por RN CFA específica.
- **D) está correta:** A lei é relevante para anuidades, taxas e cobrança no contexto de conselhos.
- **Conceito cobrado:** Lei 12.514/2011.
- **Pegadinha usada:** Ignorar normas financeiras dos conselhos..
- **Como pensar para acertar:** Conselho profissional envolve contribuições e anuidades; por isso a lei importa.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 18

- **Alternativa correta:** C.
- **A) está errada:** Processo sancionador exige base normativa.
- **B) está errada:** Sanção ética é matéria institucional/jurídica, não apenas técnica.
- **C) está correta:** Sanções dependem do caso e do sujeito alcançado.
- **D) está errada:** Não se deve presumir pena máxima automática.
- **Conceito cobrado:** Sanções éticas.
- **Pegadinha usada:** Presumir pena específica sem base confirmada..
- **Como pensar para acertar:** Sem artigo/prazo específico confirmado, fique nos critérios gerais da norma.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 19

- **Alternativa correta:** B.
- **A) está errada:** O caso realmente envolve fiscalização/ética.
- **B) está correta:** Assinatura técnica pressupõe responsabilidade efetiva.
- **C) está errada:** Essa afirmação está alinhada ao Código de Ética.
- **D) está errada:** A assinatura vincula responsabilidade, por isso exige participação real.
- **Conceito cobrado:** Responsabilidade por assinatura técnica.
- **Pegadinha usada:** Aceitar assinatura de fachada..
- **Como pensar para acertar:** Pergunte se houve atuação técnica real por quem assina.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 20

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: esse é o núcleo do dever.
- **B) está correta como afirmação:** Correta: não é regra para acobertar ilegalidades.
- **C) está correta como afirmação:** Correta: sigilo não elimina deveres legais.
- **D) é a incorreta:** Incorreta: vantagem comercial não justifica violação de sigilo.
- **Conceito cobrado:** Sigilo profissional.
- **Pegadinha usada:** Transformar dever de sigilo em autorização de divulgação..
- **Como pensar para acertar:** Sigilo protege o cliente/sociedade, não interesses comerciais indevidos.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 21

- **Alternativa correta:** D.
- **A) está errada:** A alternativa inverte os objetos.
- **B) está errada:** Nenhuma das duas tem esse objeto central.
- **C) está errada:** São normas do Sistema CFA/CRAs, não de TI.
- **D) está correta:** Essa associação foi confirmada pelas fontes oficiais.
- **Conceito cobrado:** Associação de Resoluções Normativas.
- **Pegadinha usada:** Trocar números próximos de RNs..
- **Como pensar para acertar:** Faça cartão de memorização número -> ementa.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 22

- **Alternativa correta:** C.
- **A) está errada:** CNPJ é registro empresarial/fiscal, não registro em conselho profissional.
- **B) está errada:** Pessoas jurídicas podem estar sujeitas à fiscalização conforme atividade.
- **C) está correta:** O Sistema CFA/CRAs não se limita sempre à pessoa física.
- **D) está errada:** A RN 671/2025 inclui pessoas jurídicas no título e no alcance.
- **Conceito cobrado:** Pessoa jurídica no Sistema CFA/CRA.
- **Pegadinha usada:** CNPJ como falso substituto de registro profissional..
- **Como pensar para acertar:** Verifique atividade exercida e norma de registro/fiscalização.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 23

- **Alternativa correta:** B.
- **A) está errada:** O CRA-PR tem jurisdição regional, não mundial.
- **B) está correta:** Jurisdição aqui se refere à atuação regional do CRA-PR.
- **C) está errada:** Conselho profissional não é vara criminal.
- **D) está errada:** É termo de TI fora de contexto.
- **Conceito cobrado:** Jurisdição do CRA-PR.
- **Pegadinha usada:** Importar sentido de outras áreas sem contexto..
- **Como pensar para acertar:** No regimento de conselho, jurisdição é território de atuação.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 24

- **Alternativa correta:** A.
- **A) está correta:** Sindicatos representam interesses; conselhos fiscalizam exercício profissional.
- **B) está errada:** CRA não se confunde com sindicato.
- **C) está errada:** Fiscalização profissional não depende de filiação sindical.
- **D) está errada:** O CFA é conselho federal do sistema profissional.
- **Conceito cobrado:** Conselho profissional x sindicato.
- **Pegadinha usada:** Confundir representação sindical com fiscalização profissional..
- **Como pensar para acertar:** Conselho profissional protege a sociedade por fiscalização do exercício.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 25

- **Alternativa correta:** D.
- **A) está errada:** Registro é RN 649/2024, alterada pela RN 670/2025.
- **B) está errada:** É RN 671/2025.
- **C) está errada:** É RN 651/2024.
- **D) está correta:** A ementa oficial aponta o regulamento eleitoral.
- **Conceito cobrado:** RN CFA 680/2025.
- **Pegadinha usada:** Confundir eleição com registro ou ética..
- **Como pensar para acertar:** Associe 680 a eleições.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 26

- **Alternativa correta:** C.
- **A) está errada:** Questão real exige fonte confirmada.
- **B) está errada:** Se está no edital, deve entrar no estudo.
- **C) está correta:** Isso evita inventar detalhe normativo.
- **D) está errada:** Não se inventa prazo ou sanção.
- **Conceito cobrado:** Rigor de fontes normativas.
- **Pegadinha usada:** Inventar informação por plausibilidade..
- **Como pensar para acertar:** Fonte oficial primeiro; detalhe específico só com texto confirmado.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 27

- **Alternativa correta:** B.
- **A) está errada:** SGBD não aplica sanção ética.
- **B) está correta:** A conduta hostil e obstrutiva é relevante em ética/fiscalização.
- **C) está errada:** Não há direito irrestrito de impedir fiscalização regular.
- **D) está errada:** A situação é institucional e ética.
- **Conceito cobrado:** Urbanidade e fiscalização.
- **Pegadinha usada:** Tratar obstrução como defesa legítima automática..
- **Como pensar para acertar:** Fiscalização regular exige resposta institucional adequada.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 28

- **Alternativa correta:** A.
- **A) está correta:** Alterações só fazem sentido conectadas ao texto base.
- **B) está errada:** Número sem ementa não orienta cobrança.
- **C) está errada:** Norma alteradora não substitui todo o edital.
- **D) está errada:** Fonte oficial é essencial.
- **Conceito cobrado:** Norma alteradora.
- **Pegadinha usada:** Ler alteração sem texto base..
- **Como pensar para acertar:** Quando uma norma altera outra, estude o par.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 29

- **Alternativa correta:** D.
- **A) está errada:** Não é ferramenta de TI.
- **B) está errada:** Pregão é modalidade; Plenário é órgão interno.
- **C) está errada:** Plenário integra a estrutura institucional.
- **D) está correta:** O Plenário exerce deliberação no âmbito do Conselho.
- **Conceito cobrado:** Órgãos do Regimento do CRA-PR.
- **Pegadinha usada:** Confundir órgão interno com ferramenta ou modalidade..
- **Como pensar para acertar:** Deliberação superior dentro do Conselho aponta para Plenário.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 30

- **Alternativa correta:** C.
- **A) está errada:** Normas éticas não são substituídas informalmente.
- **B) está errada:** Não é tema de banco de dados.
- **C) está correta:** A diretoria atua na gestão/execução conforme o Regimento.
- **D) está errada:** Diretoria de conselho não edita lei federal.
- **Conceito cobrado:** Diretoria Executiva do CRA-PR.
- **Pegadinha usada:** Misturar órgão executivo com competência legislativa..
- **Como pensar para acertar:** Plenário delibera; Diretoria executa/gestiona.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 31

- **Alternativa correta:** B.
- **A) está errada:** O Código se volta a profissionais e pessoas jurídicas.
- **B) está correta:** O Código alcança atuação profissional, inclusive em diferentes vínculos, conforme norma.
- **C) está errada:** A generalização é indevida.
- **D) está errada:** Horário não elimina dever profissional.
- **Conceito cobrado:** Alcance do Código de Ética.
- **Pegadinha usada:** Achar que vínculo funcional elimina dever profissional..
- **Como pensar para acertar:** O foco é a atividade exercida e o registro, não apenas o tipo de vínculo.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 32

- **Alternativa correta:** A.
- **A) está correta:** As RNs do CFA mencionam a lei e o decreto como fundamentos.
- **B) está errada:** Não é a base da profissão de Administração.
- **C) está errada:** Não é fonte jurídica do Sistema CFA/CRAs.
- **D) está errada:** A base é do Sistema CFA/CRAs e lei federal.
- **Conceito cobrado:** Fundamentos legais do Sistema CFA/CRAs.
- **Pegadinha usada:** Não reconhecer lei/decreto base citados nas normas..
- **Como pensar para acertar:** Quando uma RN fundamenta competência, volte à lei profissional e ao decreto.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 33

- **Alternativa correta:** C.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: a RN 671/2025 inclui pessoas jurídicas.
- **B) está correta como afirmação:** Correta: são deveres destacados.
- **C) é a incorreta:** Incorreta: independência técnica é valor protegido, não renunciável por pressão indevida.
- **D) está correta como afirmação:** Correta: esse é seu objeto.
- **Conceito cobrado:** Código de Ética: deveres.
- **Pegadinha usada:** Transformar pressão externa em justificativa ética..
- **Como pensar para acertar:** Ética profissional protege independência e responsabilidade técnica.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 34

- **Alternativa correta:** C.
- **A) está errada:** Mudanças podem precisar ser comunicadas conforme normas.
- **B) está errada:** Cadastro tem função institucional.
- **C) está correta:** Cadastro atualizado sustenta a atuação do Conselho.
- **D) está errada:** Regularidade cadastral não elimina deveres éticos.
- **Conceito cobrado:** Registro e atualização cadastral.
- **Pegadinha usada:** Tratar cadastro como formalidade inútil..
- **Como pensar para acertar:** Conselho fiscaliza e comunica com base em dados cadastrais confiáveis.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 35

- **Alternativa correta:** B.
- **A) está errada:** Uso indevido de registro é conduta sensível/vedada.
- **B) está correta:** Ética profissional limita atuação voltada apenas a vantagem pessoal.
- **C) está errada:** Interesse econômico não autoriza violar deveres éticos.
- **D) está errada:** Sigilo é dever, não conveniência unilateral.
- **Conceito cobrado:** Finalidade ética da profissão.
- **Pegadinha usada:** Reduzir ética a interesse comercial..
- **Como pensar para acertar:** Quando houver conflito, procure dever profissional e interesse social.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 36

- **Alternativa correta:** A.
- **A) está correta:** A ementa oficial confirma o regulamento de registro.
- **B) está errada:** Eleição é RN 680/2025.
- **C) está errada:** Código de Ética é RN 671/2025.
- **D) está errada:** Regimento do CRA-PR é RN 651/2024.
- **Conceito cobrado:** RN CFA 649/2024.
- **Pegadinha usada:** Trocar ementas das resoluções..
- **Como pensar para acertar:** Memorize: 649 = registro.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 37

- **Alternativa correta:** D.
- **A) está errada:** Hierarquia normativa não funciona assim.
- **B) está errada:** Conselho regional não revoga lei federal.
- **C) está errada:** É questão de hierarquia normativa.
- **D) está correta:** Resolução normativa não revoga a lei profissional federal.
- **Conceito cobrado:** Hierarquia normativa e RN 670/2025.
- **Pegadinha usada:** Achar que norma inferior posterior revoga lei federal..
- **Como pensar para acertar:** Observe hierarquia: RN não revoga lei federal.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 38

- **Alternativa correta:** C.
- **A) está errada:** Essas normas são de legislação CFA/CRA.
- **B) está errada:** Regimento do CRA-PR é RN 651/2024.
- **C) está correta:** As três associações correspondem às ementas confirmadas.
- **D) está errada:** Todas as associações estão trocadas.
- **Conceito cobrado:** Leitura dirigida das RNs.
- **Pegadinha usada:** Misturar objetos normativos..
- **Como pensar para acertar:** Use mapa número -> tema: fiscalização, PERC, eleições.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 39

- **Alternativa correta:** B.
- **A) está errada:** Conselho não substitui Poder Judiciário em ação judicial.
- **B) está correta:** Essa é atuação típica do regional.
- **C) está errada:** Isso é competência legislativa penal, não do CRA.
- **D) está errada:** Regional não revoga norma nacional do CFA.
- **Conceito cobrado:** Competência do CRA-PR.
- **Pegadinha usada:** Extrapolar poder do conselho..
- **Como pensar para acertar:** Conselhos têm competências administrativas específicas.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 40

- **Alternativa correta:** A.
- **A) está correta:** O Código destaca zelo, responsabilidade e aperfeiçoamento.
- **B) está errada:** Uso de registro de terceiro é inadequado.
- **C) está errada:** Omissão não substitui dever profissional.
- **D) está errada:** Responsabilidade profissional não é simplesmente transferida.
- **Conceito cobrado:** Dever de aperfeiçoamento e zelo.
- **Pegadinha usada:** Tratar atualização profissional como opcional irrelevante..
- **Como pensar para acertar:** Mudança normativa exige estudo e responsabilidade técnica.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 41

- **Alternativa correta:** D.
- **A) está errada:** Interesse do cliente não justifica fraude.
- **B) está errada:** Defesa do cliente convive com sigilo e independência.
- **C) está errada:** Contrato não elimina norma ética.
- **D) está correta:** O dever de defesa não autoriza condutas ilícitas ou antiéticas.
- **Conceito cobrado:** Deveres profissionais e limites éticos.
- **Pegadinha usada:** Usar interesse do cliente como justificativa absoluta..
- **Como pensar para acertar:** Dever profissional tem limites jurídicos e éticos.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 42

- **Alternativa correta:** C.
- **A) está errada:** Sanções existem, mas detalhes exigem base.
- **B) está errada:** Gradação é parte do tema ético.
- **C) está correta:** Sem fonte específica, não se deve criar prazo/sanção exata.
- **D) está errada:** Pena depende de norma e caso.
- **Conceito cobrado:** Sanções e cautela normativa.
- **Pegadinha usada:** Inventar artigo, prazo ou penalidade..
- **Como pensar para acertar:** Conceito geral sim; detalhe específico só com fonte confirmada.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 43

- **Alternativa correta:** B.
- **A) está errada:** O Código consta no edital vigente.
- **B) está correta:** O título e dispositivos iniciais incluem pessoas jurídicas.
- **C) está errada:** Pessoas jurídicas podem exercer atividades nas áreas de Administração.
- **D) está errada:** Contrato privado não afasta automaticamente a norma ética.
- **Conceito cobrado:** Pessoa jurídica no Código de Ética.
- **Pegadinha usada:** Excluir pessoa jurídica do alcance do Código..
- **Como pensar para acertar:** Leia o título e o alcance subjetivo da norma.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 44

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: o edital é o mapa da prova.
- **B) está correta como afirmação:** Correta: são fontes primárias/ oficiais.
- **C) está correta como afirmação:** Correta: estilo não é fonte de autoria real.
- **D) é a incorreta:** Incorreta: questão real exige fonte confirmada.
- **Conceito cobrado:** Fontes e honestidade metodológica.
- **Pegadinha usada:** Confundir estilo de banca com questão real..
- **Como pensar para acertar:** Nunca marque como real sem prova de origem.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 45

- **Alternativa correta:** D.
- **A) está errada:** Ética e fiscalização são centrais.
- **B) está errada:** Conselhos têm função específica, não universal.
- **C) está errada:** A fiscalização busca regularidade, não impedir atuação lícita.
- **D) está correta:** Conselhos não existem apenas para interesse corporativo; há função pública de fiscalização.
- **Conceito cobrado:** Função dos conselhos profissionais.
- **Pegadinha usada:** Reduzir conselho a corporação privada..
- **Como pensar para acertar:** Conselho profissional tem função pública de fiscalização.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 46

- **Alternativa correta:** C.
- **A) está errada:** O caso é ético/fiscalizatório.
- **B) está errada:** O CRA tem competência de fiscalização profissional.
- **C) está correta:** Responsável técnico deve exercer atuação efetiva conforme normas aplicáveis.
- **D) está errada:** Formalidade sem atuação real pode ser problemática.
- **Conceito cobrado:** Responsabilidade técnica e fiscalização.
- **Pegadinha usada:** Confundir presença formal com atuação efetiva..
- **Como pensar para acertar:** Pergunte se há atuação técnica real e regularidade material.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 47

- **Alternativa correta:** B.
- **A) está errada:** O sistema profissional não é municipal nesse sentido.
- **B) está correta:** O sistema combina uniformização nacional e atuação regional.
- **C) está errada:** Inverte a estrutura.
- **D) está errada:** Há função uniformizadora do CFA.
- **Conceito cobrado:** Sistema CFA/CRAs.
- **Pegadinha usada:** Inverter a direção da uniformização normativa..
- **Como pensar para acertar:** Nacional orienta; regional executa/fiscaliza.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 48

- **Alternativa correta:** A.
- **A) está correta:** A apostila destacou sede na capital e jurisdição estadual.
- **B) está errada:** Nacional é extrapolação indevida para um regional.
- **C) está errada:** O CRA-PR não é órgão municipal.
- **D) está errada:** O Regimento trata de jurisdição regional.
- **Conceito cobrado:** Regimento do CRA-PR.
- **Pegadinha usada:** Trocar jurisdição estadual por nacional ou municipal..
- **Como pensar para acertar:** Memorize sede e jurisdição como dados básicos do Regimento.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 49

- **Alternativa correta:** D.
- **A) está errada:** Solidariedade não autoriza irregularidade profissional.
- **B) está errada:** Exercício profissional irregular é relevante para o conselho.
- **C) está errada:** É conduta profissional, não forma textual.
- **D) está correta:** Facilitar atuação irregular contraria a fiscalização profissional.
- **Conceito cobrado:** Facilitação de exercício irregular.
- **Pegadinha usada:** Transformar ajuda indevida em dever ético..
- **Como pensar para acertar:** Ética protege a sociedade contra atuação não habilitada.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

### Comentário da Questão 50

- **Alternativa correta:** C.
- **A) está errada:** RNs se fundamentam na lei e no decreto.
- **B) está errada:** O tema é profissão de Administração e sistema de conselhos.
- **C) está correta:** Lei e decreto devem ser estudados em conjunto.
- **D) está errada:** Regulamento não substitui a lei.
- **Conceito cobrado:** Lei e decreto da profissão.
- **Pegadinha usada:** Desconsiderar a base legal por existirem RNs..
- **Como pensar para acertar:** Comece pela lei, depois leia o decreto e normas do CFA.
- **Referência à apostila de estudo:** Dia 4 — Legislação CRA-PR/CFA.

---

# Dia 5 — Língua Portuguesa e Discursiva

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões

### Questão 1 — Questão autoral no estilo Instituto Consulplan

Leia o trecho: “A digitalização de serviços públicos amplia o acesso do cidadão, mas exige mecanismos de segurança para que a eficiência não comprometa direitos.” A ideia central é:

A) a eficiência administrativa é incompatível com direitos do cidadão.
B) a segurança impede qualquer melhoria em serviços públicos.
C) a digitalização pode ampliar o acesso, desde que acompanhada de segurança e respeito a direitos.
D) a digitalização deve ser abandonada porque sempre viola direitos.

### Questão 2 — Questão autoral no estilo Instituto Consulplan

No trecho “... mas exige mecanismos de segurança”, o conector “mas” estabelece relação de:

A) causa.
B) oposição/ressalva.
C) conclusão.
D) finalidade.

### Questão 3 — Questão autoral no estilo Instituto Consulplan

Leia: “Nem toda inovação tecnológica representa melhoria administrativa.” A inferência correta é:

A) algumas inovações tecnológicas podem não melhorar a Administração.
B) nenhuma inovação tecnológica melhora a Administração.
C) toda inovação tecnológica piora a Administração.
D) inovação tecnológica e Administração são temas sem relação.

### Questão 4 — Questão autoral no estilo Instituto Consulplan

Leia: “A transparência fortalece a confiança social, desde que respeite a proteção de dados pessoais.” Assinale a alternativa que extrapola o texto.

A) A transparência pode fortalecer a confiança social.
B) A proteção de dados pessoais deve ser considerada.
C) Transparência e proteção de dados precisam ser conciliadas.
D) Todo dado pessoal deve ser divulgado para garantir confiança.

### Questão 5 — Questão autoral no estilo Instituto Consulplan

A reescrita que preserva o sentido de “A revisão diária reduz o esquecimento e melhora a retenção do conteúdo” é:

A) A retenção melhora porque o esquecimento aumenta.
B) A revisão diária prejudica a retenção, embora reduza o conteúdo.
C) O esquecimento é reduzido e a retenção do conteúdo é melhorada pela revisão diária.
D) A revisão diária elimina definitivamente qualquer esquecimento.

### Questão 6 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta quanto à concordância verbal.

A) Existe pendências no cadastro.
B) Faltam documentos no processo administrativo.
C) Falta documentos no processo administrativo.
D) Haviam muitos candidatos na sala, no sentido de existir.

### Questão 7 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa em que a crase está corretamente empregada.

A) O relatório foi encaminhado à diretoria técnica.
B) O candidato começou à revisar o edital.
C) A servidora entregou o documento à ele.
D) O servidor foi à pé ao protocolo.

### Questão 8 — Questão autoral no estilo Instituto Consulplan

A vírgula foi empregada incorretamente em:

A) Após a publicação do edital, os candidatos organizaram o cronograma.
B) O CRA-PR, autarquia profissional, publicou orientações.
C) Embora o conteúdo seja extenso, a revisão diária ajuda.
D) Os candidatos, leram o edital com atenção.

### Questão 9 — Questão autoral no estilo Instituto Consulplan

Leia: “O sistema é eficiente; contudo, depende de dados atualizados.” O conector “contudo” poderia ser substituído, sem prejuízo do sentido, por:

A) porque.
B) a fim de que.
C) entretanto.
D) portanto.

### Questão 10 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta quanto à regência verbal no padrão formal.

A) A decisão implicou em mudanças, obrigatoriamente.
B) O candidato obedeceu ao edital.
C) O candidato obedeceu o edital.
D) O servidor assistiu o treinamento, no sentido de ver, como única forma formal.

### Questão 11 — Questão autoral no estilo Instituto Consulplan

Leia: “Os dados foram revisados, e esse procedimento reduziu inconsistências.” A expressão “esse procedimento” retoma:

A) a revisão dos dados.
B) as inconsistências.
C) apenas a palavra “dados”.
D) uma informação externa ao texto.

### Questão 12 — Questão autoral no estilo Instituto Consulplan

No período “Se o planejamento for consistente, a execução será mais segura”, a oração introduzida por “se” expressa:

A) conclusão.
B) concessão.
C) oposição.
D) condição.

### Questão 13 — Questão autoral no estilo Instituto Consulplan

Assinale a frase em que “há” e “a” foram empregados corretamente.

A) Há prova ocorrerá daqui a dois meses.
B) A três meses estudo; há dois meses farei a prova.
C) Estudo há três meses; a prova ocorrerá daqui a dois meses.
D) Estudo a três meses; a prova ocorrerá daqui há dois meses.

### Questão 14 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa em que há ambiguidade de referência.

A) A equipe revisou o documento antes do envio.
B) O analista informou ao coordenador que seu relatório estava incompleto.
C) O analista informou que o relatório da equipe estava incompleto.
D) O coordenador recebeu o relatório final ontem.

### Questão 15 — Questão autoral no estilo Instituto Consulplan

Leia: “A medida é necessária, pois reduz riscos operacionais.” No contexto, “pois” introduz ideia de:

A) explicação/causa.
B) oposição.
C) alternância.
D) condição.

### Questão 16 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta quanto à colocação pronominal no padrão formal.

A) Não deve-se ignorar o edital.
B) Me informaram o resultado ontem, em início formal de frase.
C) Jamais deve-se desconsiderar a legislação.
D) Não se deve ignorar o edital.

### Questão 17 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa com pontuação adequada.

A) Curitiba, capital do Paraná sediará, o evento.
B) Curitiba capital, do Paraná sediará o evento.
C) Curitiba, capital do Paraná, sediará o evento.
D) Curitiba capital do Paraná, sediará o evento.

### Questão 18 — Questão autoral no estilo Instituto Consulplan

Leia: “Apenas os candidatos que revisaram legislação específica acertaram a questão.” A palavra “apenas” indica:

A) concessão.
B) restrição.
C) causa.
D) conclusão.

### Questão 19 — Questão autoral no estilo Instituto Consulplan

A frase correta quanto à concordância nominal é:

A) Seguem anexos os documentos solicitados.
B) Segue anexo os documentos solicitados.
C) As informações seguem anexo.
D) Os relatórios seguem anexa.

### Questão 20 — Questão autoral no estilo Instituto Consulplan

Leia: “A política foi implementada para reduzir filas.” A expressão “para reduzir filas” indica:

A) consequência não planejada.
B) oposição.
C) concessão.
D) finalidade.

### Questão 21 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa em que a palavra “onde” foi empregada adequadamente.

A) O argumento onde o candidato se baseou é frágil.
B) A situação onde houve dúvida foi resolvida.
C) O prédio onde funciona o setor de atendimento passa por reforma.
D) A norma onde o tema foi tratado é recente.

### Questão 22 — Questão autoral no estilo Instituto Consulplan

Em uma dissertação, uma tese eficiente deve:

A) ser substituída por uma lista de exemplos sem relação.
B) apresentar posição clara sobre o tema.
C) apenas copiar o tema sem posicionamento.
D) surgir somente depois da conclusão.

### Questão 23 — Questão autoral no estilo Instituto Consulplan

Leia a introdução: “A tecnologia é importante. Hoje tudo é tecnologia. A tecnologia está em todos os lugares.” O principal problema é:

A) generalidade e ausência de tese clara.
B) excesso de argumento técnico específico.
C) uso obrigatório de linguagem jurídica avançada.
D) presença de conclusão completa no início.

### Questão 24 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa que apresenta melhor desenvolvimento argumentativo.

A) Digitalização é boa porque sim.
B) Todo mundo sabe que tecnologia resolve tudo.
C) O tema é muito debatido atualmente.
D) A digitalização reduz deslocamentos e filas, mas exige sistemas acessíveis e seguros para não excluir cidadãos vulneráveis.

### Questão 25 — Questão autoral no estilo Instituto Consulplan

Assinale a frase que evita linguagem informal inadequada à discursiva.

A) Dados são um negócio meio complicado.
B) A parada da transparência ajuda geral.
C) A Administração Pública deve adotar critérios transparentes na gestão de dados.
D) A gestão de dados é tipo uma coisa muito top.

### Questão 26 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa em que a crase é indevida.

A) A informação foi encaminhada à autoridade competente.
B) O servidor começou à analisar o processo.
C) O servidor referiu-se à auditoria interna.
D) A equipe compareceu à reunião.

### Questão 27 — Questão autoral no estilo Instituto Consulplan

Leia: “Os candidatos que estudaram o edital resolveram melhor as questões.” Sem vírgulas, a oração “que estudaram o edital” tem valor:

A) restritivo.
B) explicativo.
C) conclusivo.
D) adversativo.

### Questão 28 — Questão autoral no estilo Instituto Consulplan

Leia: “Os candidatos, que estudaram o edital, resolveram melhor as questões.” Com vírgulas, a oração destacada tem valor:

A) restritivo indispensável.
B) condicional.
C) comparativo.
D) explicativo.

### Questão 29 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa que preserva paralelismo sintático.

A) O plano exige estudar, revisão e questões resolvidas.
B) O plano exige teoria e resolver e erros.
C) O plano exige ler a teoria, resolver questões e revisar erros.
D) O plano exige leitura, resolver questões e que revise erros.

### Questão 30 — Questão autoral no estilo Instituto Consulplan

Em “A equipe revisou o relatório; o coordenador, a planilha”, a vírgula em “o coordenador, a planilha” indica:

A) oração subordinada adverbial.
B) elipse do verbo “revisou”.
C) separação indevida de sujeito e verbo.
D) aposto explicativo.

### Questão 31 — Questão autoral no estilo Instituto Consulplan

Assinale a frase correta no padrão formal.

A) Faz dois anos que o sistema foi implantado.
B) Fazem dois anos que o sistema foi implantado.
C) Fizeram dois anos que o sistema foi implantado.
D) Fazem-se dois anos que o sistema foi implantado.

### Questão 32 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa em que “porquê” está corretamente empregado.

A) Estudo porquê quero aprovação.
B) Porquê você faltou?
C) Não sei porque ele faltou, no sentido de motivo.
D) O candidato explicou o porquê de sua ausência.

### Questão 33 — Questão autoral no estilo Instituto Consulplan

No trecho “A medida é eficiente, portanto deve ser mantida”, o termo “portanto” introduz:

A) concessão.
B) condição.
C) conclusão.
D) oposição.

### Questão 34 — Questão autoral no estilo Instituto Consulplan

Leia: “O relatório foi entregue pelo analista.” A expressão “pelo analista” exerce função de:

A) adjunto adnominal de relatório.
B) agente da passiva.
C) sujeito paciente.
D) objeto direto.

### Questão 35 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa que apresenta relação de causa.

A) O sistema foi revisado porque apresentava falhas recorrentes.
B) O sistema foi revisado, porém continuou instável.
C) O sistema foi revisado para reduzir riscos.
D) Embora revisado, o sistema continuou instável.

### Questão 36 — Questão autoral no estilo Instituto Consulplan

Em “A norma publicada em 2025 alterou o procedimento”, o termo “publicada em 2025” funciona como:

A) verbo principal com sujeito oculto.
B) conector conclusivo.
C) objeto direto de “alterou”.
D) caracterização/restrição da norma.

### Questão 37 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa em que a pontuação preserva melhor a clareza.

A) No início da semana o candidato revisou, arquitetura, sistemas operacionais e banco de dados.
B) No início da semana, o candidato, revisou, arquitetura.
C) No início da semana, o candidato revisou arquitetura, sistemas operacionais e banco de dados.
D) No início, da semana o candidato, revisou arquitetura sistemas operacionais e banco de dados.

### Questão 38 — Questão autoral no estilo Instituto Consulplan

Leia: “A solução não é simples, tampouco impossível.” A palavra “tampouco” indica:

A) finalidade.
B) adição negativa, equivalente a “também não”.
C) conclusão afirmativa.
D) causa principal.

### Questão 39 — Questão autoral no estilo Instituto Consulplan

A alternativa que melhor conclui uma dissertação sobre ética no uso de dados públicos é:

A) Assim, o uso ético de dados exige transparência, segurança e responsabilidade institucional para gerar confiança social.
B) Portanto, dados são importantes e existem computadores.
C) Enfim, cada pessoa que faça o que quiser com dados.
D) Conclui-se que nada pode ser feito.

### Questão 40 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta quanto à acentuação.

A) publico, tecnico e logico nunca recebem acento.
B) público é acentuada por ser monossílabo tônico.
C) técnico não recebe acento por terminar em vogal.
D) público, técnico e lógico são acentuadas por serem proparoxítonas.

### Questão 41 — Questão autoral no estilo Instituto Consulplan

Leia: “O órgão publicou o edital e divulgou o cronograma.” A conjunção “e” estabelece:

A) condição para a primeira ação.
B) conclusão obrigatória.
C) adição de ações.
D) oposição entre ações.

### Questão 42 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa com regência nominal adequada.

A) O relatório era compatível a norma, obrigatoriamente sem artigo.
B) O candidato estava apto ao exercício da função.
C) O candidato estava apto o exercício da função.
D) A decisão foi favorável o candidato.

### Questão 43 — Questão autoral no estilo Instituto Consulplan

No comando de prova “assinale a alternativa incorreta”, a estratégia adequada é:

A) destacar a palavra “incorreta” e procurar a afirmação errada.
B) marcar a primeira alternativa que pareça familiar.
C) ignorar palavras negativas para ganhar tempo.
D) resolver como se a banca pedisse a correta.

### Questão 44 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa em que a reescrita altera o sentido original: “O candidato só revisou legislação depois de errar o simulado.”

A) Somente após errar o simulado, o candidato revisou legislação.
B) A revisão de legislação ocorreu apenas depois do erro no simulado.
C) Foi depois de errar o simulado que o candidato revisou legislação.
D) O candidato revisou legislação antes de errar o simulado.

### Questão 45 — Questão autoral no estilo Instituto Consulplan

Leia: “A equipe, apesar das restrições orçamentárias, concluiu o projeto.” A expressão entre vírgulas indica:

A) finalidade do projeto.
B) explicação do sujeito equipe.
C) concessão/contraste com a conclusão do projeto.
D) causa direta da conclusão.

### Questão 46 — Questão autoral no estilo Instituto Consulplan

Assinale a frase sem problema de concordância.

A) A maioria dos candidatos estavam preparado.
B) Mais de um candidato acertou a questão.
C) Mais de um candidato acertaram a questão.
D) Os candidato acertaram a questão.

### Questão 47 — Questão autoral no estilo Instituto Consulplan

Em uma dissertação, coesão textual é melhor definida como:

A) ligação formal e semântica entre partes do texto por retomadas e conectores.
B) quantidade de linhas escritas, independentemente de sentido.
C) uso de palavras difíceis sem relação lógica.
D) ausência total de pronomes e conectores.

### Questão 48 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa correta quanto à ortografia.

A) excessão
B) essessão
C) exseção
D) exceção

### Questão 49 — Questão autoral no estilo Instituto Consulplan

Leia: “A capacitação dos servidores é essencial, uma vez que novas tecnologias exigem atualização constante.” A expressão “uma vez que” indica:

A) alternância.
B) proporção.
C) causa/explicação.
D) oposição.

### Questão 50 — Questão autoral no estilo Instituto Consulplan

A alternativa que mantém linguagem objetiva é:

A) Houveram problemas muito tipo complicados.
B) O sistema apresentou falhas de integração e exigiu revisão dos cadastros.
C) O sistema deu umas coisas estranhas e ficou meio ruim.
D) A coisa do cadastro não estava legal.

## Gabarito do Dia 5

1. C
2. B
3. A
4. D
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
16. D
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
30. B
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

## Comentários do Dia 5

### Comentário da Questão 1

- **Alternativa correta:** C.
- **A) está errada:** O texto defende compatibilização, não incompatibilidade.
- **B) está errada:** O trecho apresenta segurança como condição, não impedimento absoluto.
- **C) está correta:** A alternativa preserva benefício e ressalva do texto.
- **D) está errada:** O texto não condena a digitalização; apenas condiciona seu uso responsável.
- **Conceito cobrado:** Interpretação: ideia central.
- **Pegadinha usada:** Transformar ressalva em negação total..
- **Como pensar para acertar:** Procure a tese completa: benefício + condição/limite.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 2

- **Alternativa correta:** B.
- **A) está errada:** Causa seria indicada por porque, uma vez que, pois em certos contextos.
- **B) está correta:** O conector contrapõe o benefício da digitalização à exigência de segurança.
- **C) está errada:** Conclusão seria indicada por portanto, logo, assim.
- **D) está errada:** Finalidade seria indicada por para, a fim de.
- **Conceito cobrado:** Conectores adversativos.
- **Pegadinha usada:** Ignorar o valor argumentativo do conector..
- **Como pensar para acertar:** Sempre pergunte que relação o conector cria entre as ideias.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 3

- **Alternativa correta:** A.
- **A) está correta:** “Nem toda” nega a universalidade, sem negar todos os casos.
- **B) está errada:** A alternativa transforma negação parcial em negação total.
- **C) está errada:** O texto não afirma piora universal.
- **D) está errada:** O texto estabelece relação, ainda que com ressalva.
- **Conceito cobrado:** Inferência e quantificadores.
- **Pegadinha usada:** Confundir “nem toda” com “nenhuma”..
- **Como pensar para acertar:** Negação de “todo” é “algum não”, não “nenhum”.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 4

- **Alternativa correta:** D.
- **A) está errada:** É compatível com o trecho.
- **B) está errada:** É compatível com a condição apresentada.
- **C) está errada:** É inferência autorizada pelo trecho.
- **D) está correta:** Essa é extrapolação: o texto condiciona transparência ao respeito à proteção de dados.
- **Conceito cobrado:** Extrapolação textual.
- **Pegadinha usada:** Absolutizar uma ideia limitada pelo texto..
- **Como pensar para acertar:** Veja se a alternativa ultrapassa o que o texto permite afirmar.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 5

- **Alternativa correta:** C.
- **A) está errada:** Inverte a relação lógica.
- **B) está errada:** Altera completamente o sentido.
- **C) está correta:** A voz passiva preserva o sentido essencial.
- **D) está errada:** “Reduz” não significa “elimina definitivamente”.
- **Conceito cobrado:** Reescrita sem alteração de sentido.
- **Pegadinha usada:** Trocar redução por eliminação absoluta..
- **Como pensar para acertar:** Compare núcleo verbal e intensidade das palavras.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 6

- **Alternativa correta:** B.
- **A) está errada:** Com o verbo existir, o sujeito “pendências” exige plural: existem.
- **B) está correta:** O sujeito é “documentos”, no plural; o verbo concorda.
- **C) está errada:** O verbo deveria concordar com “documentos”.
- **D) está errada:** Haver com sentido de existir é impessoal e fica no singular.
- **Conceito cobrado:** Concordância verbal.
- **Pegadinha usada:** Confundir haver impessoal com existir..
- **Como pensar para acertar:** Ache o sujeito; cuidado com haver/existir/faltar.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 7

- **Alternativa correta:** A.
- **A) está correta:** Encaminhar algo a alguém + “a diretoria” gera crase.
- **B) está errada:** Não há crase antes de verbo.
- **C) está errada:** Não há crase antes de pronome pessoal masculino.
- **D) está errada:** Não há crase em “a pé”, expressão com palavra masculina.
- **Conceito cobrado:** Crase.
- **Pegadinha usada:** Aplicar crase antes de verbo/pronome masculino..
- **Como pensar para acertar:** Teste a regência e se o termo feminino aceita artigo.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 8

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Adjunto adverbial deslocado pode ser separado por vírgula.
- **B) está correta como afirmação:** Aposto explicativo fica isolado por vírgulas.
- **C) está correta como afirmação:** Oração subordinada deslocada pede vírgula.
- **D) é a incorreta:** Não se separa sujeito do verbo por vírgula.
- **Conceito cobrado:** Pontuação: vírgula.
- **Pegadinha usada:** Usar vírgula por pausa intuitiva entre sujeito e verbo..
- **Como pensar para acertar:** Não separe sujeito e predicado.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 9

- **Alternativa correta:** C.
- **A) está errada:** Porque indica causa/explicação.
- **B) está errada:** A fim de que indica finalidade.
- **C) está correta:** Entretanto também indica oposição/ressalva.
- **D) está errada:** Portanto indica conclusão, não oposição.
- **Conceito cobrado:** Coesão: conectores.
- **Pegadinha usada:** Trocar oposição por conclusão..
- **Como pensar para acertar:** Identifique a relação de contraste entre as orações.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 10

- **Alternativa correta:** B.
- **A) está errada:** Implicar no sentido de acarretar é tradicionalmente transitivo direto: implicou mudanças.
- **B) está correta:** O verbo obedecer exige preposição “a”.
- **C) está errada:** Falta a preposição exigida no padrão formal.
- **D) está errada:** No padrão cobrado, assistir no sentido de ver pode reger “a”.
- **Conceito cobrado:** Regência verbal.
- **Pegadinha usada:** Aplicar regência coloquial em prova formal..
- **Como pensar para acertar:** Verbos comuns em concurso têm regências cobradas de modo padrão.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 11

- **Alternativa correta:** A.
- **A) está correta:** O demonstrativo retoma a ação descrita anteriormente.
- **B) está errada:** As inconsistências aparecem como resultado reduzido, não como procedimento.
- **C) está errada:** O referente é a ação de revisar dados, não só o substantivo.
- **D) está errada:** O referente está no próprio trecho.
- **Conceito cobrado:** Coesão referencial.
- **Pegadinha usada:** Retomar substantivo isolado quando o pronome retoma ideia..
- **Como pensar para acertar:** Pergunte: que ação ou termo anterior faz sentido como “procedimento”?
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 12

- **Alternativa correta:** D.
- **A) está errada:** Conclusão seria marcada por portanto, logo.
- **B) está errada:** Concessão seria marcada por embora, ainda que.
- **C) está errada:** Oposição seria marcada por mas, porém, contudo.
- **D) está correta:** A execução mais segura depende da condição apresentada.
- **Conceito cobrado:** Relação condicional.
- **Pegadinha usada:** Confundir condição com conclusão..
- **Como pensar para acertar:** Se indica hipótese/condição.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 13

- **Alternativa correta:** C.
- **A) está errada:** Antes de “prova” nesse contexto, o correto seria “a prova”.
- **B) está errada:** Tempo decorrido pede “há”; futuro pede “a”.
- **C) está correta:** Há indica tempo decorrido; a indica tempo futuro.
- **D) está errada:** Os usos estão invertidos.
- **Conceito cobrado:** Uso de há e a.
- **Pegadinha usada:** Trocar passado por futuro..
- **Como pensar para acertar:** Há = tempo decorrido; a = tempo futuro/distância.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 14

- **Alternativa correta:** B.
- **A) está errada:** A estrutura é clara.
- **B) está correta:** “Seu relatório” pode ser do analista ou do coordenador.
- **C) está errada:** O referente está claro.
- **D) está errada:** Não há pronome ambíguo.
- **Conceito cobrado:** Ambiguidade e pronomes.
- **Pegadinha usada:** Ignorar referente de possessivo..
- **Como pensar para acertar:** Pronome possessivo pode gerar dupla leitura.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 15

- **Alternativa correta:** A.
- **A) está correta:** A oração explica por que a medida é necessária.
- **B) está errada:** Oposição exigiria mas, porém, contudo.
- **C) está errada:** Alternância seria ou...ou.
- **D) está errada:** Condição seria marcada por se, caso.
- **Conceito cobrado:** Conectores explicativos.
- **Pegadinha usada:** Ler pois como adversativo sem contexto..
- **Como pensar para acertar:** Pergunte: a segunda oração explica a primeira?
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 16

- **Alternativa correta:** D.
- **A) está errada:** A negativa favorece “não se deve”.
- **B) está errada:** Em início de período formal, evita-se iniciar com pronome oblíquo átono.
- **C) está errada:** “Jamais” também atrai próclise: jamais se deve.
- **D) está correta:** Palavra negativa atrai próclise.
- **Conceito cobrado:** Colocação pronominal.
- **Pegadinha usada:** Ignorar palavras atrativas..
- **Como pensar para acertar:** Negativas como não e jamais atraem o pronome para antes do verbo.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 17

- **Alternativa correta:** C.
- **A) está errada:** A pontuação quebra a relação entre sujeito, verbo e complemento.
- **B) está errada:** A pontuação fragmenta o termo explicativo.
- **C) está correta:** O aposto explicativo fica isolado por vírgulas.
- **D) está errada:** Falta isolar adequadamente o aposto e há vírgula indevida antes do verbo.
- **Conceito cobrado:** Aposto e vírgula.
- **Pegadinha usada:** Não isolar aposto explicativo..
- **Como pensar para acertar:** Aposto explicativo pode ser retirado sem destruir a estrutura.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 18

- **Alternativa correta:** B.
- **A) está errada:** Não há ideia de obstáculo superado.
- **B) está correta:** A palavra limita o grupo aos candidatos que revisaram legislação específica.
- **C) está errada:** Não explica motivo diretamente; restringe alcance.
- **D) está errada:** Não há conclusão marcada.
- **Conceito cobrado:** Semântica: palavra restritiva.
- **Pegadinha usada:** Ignorar palavra que limita o alcance da frase..
- **Como pensar para acertar:** Palavras como apenas, somente e só restringem o universo.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 19

- **Alternativa correta:** A.
- **A) está correta:** “Anexos” concorda com “documentos”.
- **B) está errada:** O verbo e o adjetivo não concordam com “documentos”.
- **C) está errada:** O adjetivo deveria concordar: anexas.
- **D) está errada:** O adjetivo deveria concordar com relatórios: anexos.
- **Conceito cobrado:** Concordância nominal.
- **Pegadinha usada:** Tratar anexo como invariável nesse contexto..
- **Como pensar para acertar:** Anexo, incluso e obrigado costumam concordar com o termo a que se referem.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 20

- **Alternativa correta:** D.
- **A) está errada:** A estrutura indica propósito, não resultado acidental.
- **B) está errada:** Não há contraste.
- **C) está errada:** Não há embora/ainda que.
- **D) está correta:** Mostra o objetivo da implementação da política.
- **Conceito cobrado:** Relação de finalidade.
- **Pegadinha usada:** Confundir finalidade com causa..
- **Como pensar para acertar:** Pergunte: para quê?
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 21

- **Alternativa correta:** C.
- **A) está errada:** Argumento não é lugar físico.
- **B) está errada:** Situação não é lugar físico; use “em que”.
- **C) está correta:** Onde retoma lugar físico.
- **D) está errada:** Para norma, prefira “em que” ou “na qual”.
- **Conceito cobrado:** Uso de onde.
- **Pegadinha usada:** Usar onde para qualquer referente..
- **Como pensar para acertar:** Reserve onde para lugar.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 22

- **Alternativa correta:** B.
- **A) está errada:** Exemplos precisam servir a uma posição.
- **B) está correta:** A tese orienta os argumentos do texto.
- **C) está errada:** Cópia do tema não mostra defesa ou recorte.
- **D) está errada:** A tese deve aparecer cedo, em geral na introdução.
- **Conceito cobrado:** Discursiva: tese.
- **Pegadinha usada:** Introdução vaga sem posição..
- **Como pensar para acertar:** Pergunte: que ponto de vista o texto defenderá?
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 23

- **Alternativa correta:** A.
- **A) está correta:** O trecho repete ideia ampla sem posicionamento argumentativo.
- **B) está errada:** Não há argumento específico; há generalidade.
- **C) está errada:** O problema não é falta de juridiquês, mas falta de tese.
- **D) está errada:** Não há conclusão estruturada.
- **Conceito cobrado:** Discursiva: introdução.
- **Pegadinha usada:** Confundir repetição genérica com contextualização..
- **Como pensar para acertar:** Contextualize, mas apresente tese.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 24

- **Alternativa correta:** D.
- **A) está errada:** É afirmação vaga e sem desenvolvimento.
- **B) está errada:** Generaliza e não argumenta.
- **C) está errada:** Frase genérica sem argumento.
- **D) está correta:** A frase traz argumento, efeito e ressalva concreta.
- **Conceito cobrado:** Discursiva: desenvolvimento.
- **Pegadinha usada:** Confundir opinião solta com argumento..
- **Como pensar para acertar:** Bom argumento explica mecanismo, consequência ou exemplo.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 25

- **Alternativa correta:** C.
- **A) está errada:** Expressão coloquial e vaga.
- **B) está errada:** Gíria e informalidade prejudicam o texto.
- **C) está correta:** A frase é formal, clara e objetiva.
- **D) está errada:** Linguagem informal inadequada.
- **Conceito cobrado:** Registro formal.
- **Pegadinha usada:** Usar oralidade em texto dissertativo..
- **Como pensar para acertar:** Em prova, prefira clareza formal a gírias.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 26

- **Alternativa correta:** B.
- **A) está errada:** Encaminhar a + a autoridade justifica crase.
- **B) está correta:** Antes de verbo não ocorre crase.
- **C) está errada:** Referir-se a + a auditoria justifica crase.
- **D) está errada:** Comparecer a + a reunião justifica crase.
- **Conceito cobrado:** Crase indevida.
- **Pegadinha usada:** Crase antes de verbo..
- **Como pensar para acertar:** Antes de infinitivo não há artigo feminino.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 27

- **Alternativa correta:** A.
- **A) está correta:** Sem vírgulas, restringe quais candidatos resolveram melhor.
- **B) está errada:** Explicativa viria isolada por vírgulas.
- **C) está errada:** Não há conclusão.
- **D) está errada:** Não há oposição.
- **Conceito cobrado:** Orações adjetivas restritivas.
- **Pegadinha usada:** Ignorar efeito da ausência de vírgula..
- **Como pensar para acertar:** Com vírgula explica; sem vírgula restringe.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 28

- **Alternativa correta:** D.
- **A) está errada:** Restritiva não é isolada por vírgulas.
- **B) está errada:** Não há se/caso.
- **C) está errada:** Não há comparação.
- **D) está correta:** As vírgulas indicam informação acessória/explicativa.
- **Conceito cobrado:** Orações adjetivas explicativas.
- **Pegadinha usada:** Não perceber o papel das vírgulas..
- **Como pensar para acertar:** Vírgulas mudam o alcance da oração adjetiva.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 29

- **Alternativa correta:** C.
- **A) está errada:** Estruturas não paralelas.
- **B) está errada:** Construção truncada e sem paralelismo.
- **C) está correta:** Os três complementos estão no infinitivo.
- **D) está errada:** Mistura substantivo, infinitivo e oração.
- **Conceito cobrado:** Paralelismo sintático.
- **Pegadinha usada:** Misturar estruturas sem necessidade..
- **Como pensar para acertar:** Itens coordenados devem ter forma semelhante.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 30

- **Alternativa correta:** B.
- **A) está errada:** Não há oração subordinada.
- **B) está correta:** A vírgula marca a omissão de termo já expresso antes.
- **C) está errada:** Aqui o verbo está omitido, não separado.
- **D) está errada:** “a planilha” é complemento elíptico, não aposto.
- **Conceito cobrado:** Pontuação e elipse.
- **Pegadinha usada:** Não reconhecer verbo omitido..
- **Como pensar para acertar:** Veja se um termo anterior foi omitido para evitar repetição.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 31

- **Alternativa correta:** A.
- **A) está correta:** Fazer indicando tempo decorrido é impessoal e fica no singular.
- **B) está errada:** O verbo fazer temporal fica no singular.
- **C) está errada:** Também viola a impessoalidade temporal.
- **D) está errada:** Construção inadequada para o sentido de tempo decorrido.
- **Conceito cobrado:** Verbo fazer impessoal.
- **Pegadinha usada:** Concordar fazer temporal com expressão plural..
- **Como pensar para acertar:** Tempo decorrido: faz/há no singular.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 32

- **Alternativa correta:** D.
- **A) está errada:** Em causa explicativa, usa-se porque, sem acento.
- **B) está errada:** Em pergunta direta, usa-se por que separado.
- **C) está errada:** Quando equivale a “por qual motivo”, usa-se por que.
- **D) está correta:** Com artigo “o”, porquê é substantivo e recebe acento.
- **Conceito cobrado:** Uso dos porquês.
- **Pegadinha usada:** Não distinguir substantivo, pergunta e explicação..
- **Como pensar para acertar:** Veja se há artigo, pergunta ou causa.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 33

- **Alternativa correta:** C.
- **A) está errada:** Concessão seria embora/ainda que.
- **B) está errada:** Condição seria se/caso.
- **C) está correta:** A manutenção decorre da eficiência afirmada antes.
- **D) está errada:** Oposição seria mas/porém/contudo.
- **Conceito cobrado:** Conector conclusivo.
- **Pegadinha usada:** Trocar conclusão por causa ou oposição..
- **Como pensar para acertar:** Portanto fecha raciocínio.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 34

- **Alternativa correta:** B.
- **A) está errada:** A expressão indica agente da ação, não característica do relatório.
- **B) está correta:** Na voz passiva, indica quem praticou a ação.
- **C) está errada:** O sujeito paciente é “O relatório”.
- **D) está errada:** Na voz passiva, o objeto direto da ativa vira sujeito.
- **Conceito cobrado:** Voz passiva e agente da passiva.
- **Pegadinha usada:** Confundir agente da passiva com sujeito..
- **Como pensar para acertar:** Pergunte quem praticou a ação na passiva.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 35

- **Alternativa correta:** A.
- **A) está correta:** Porque introduz a causa da revisão.
- **B) está errada:** Porém introduz oposição.
- **C) está errada:** Para indica finalidade.
- **D) está errada:** Embora indica concessão.
- **Conceito cobrado:** Relações semânticas.
- **Pegadinha usada:** Confundir causa e finalidade..
- **Como pensar para acertar:** Causa explica por que ocorreu; finalidade indica para quê.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 36

- **Alternativa correta:** D.
- **A) está errada:** O verbo principal é “alterou”.
- **B) está errada:** Não há conector conclusivo.
- **C) está errada:** O objeto direto é “o procedimento”.
- **D) está correta:** O particípio caracteriza qual norma está sendo mencionada.
- **Conceito cobrado:** Termos da oração e valor adjetivo.
- **Pegadinha usada:** Perder a estrutura sujeito-verbo-objeto..
- **Como pensar para acertar:** Localize o verbo principal antes de classificar termos.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 37

- **Alternativa correta:** C.
- **A) está errada:** A vírgula após “revisou” separa verbo do complemento.
- **B) está errada:** Separa sujeito/verbo e cria fragmentos.
- **C) está correta:** A vírgula isola adjunto deslocado e a enumeração está clara.
- **D) está errada:** Vírgulas fragmentam termos e falta pontuação na enumeração.
- **Conceito cobrado:** Pontuação e enumeração.
- **Pegadinha usada:** Inserir vírgulas entre verbo e complemento..
- **Como pensar para acertar:** Use vírgula para deslocamentos e enumeração, não para quebrar núcleo sintático.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 38

- **Alternativa correta:** B.
- **A) está errada:** Não indica objetivo.
- **B) está correta:** Tampouco reforça negação em segunda ideia.
- **C) está errada:** Não conclui; acrescenta negação.
- **D) está errada:** Não explica motivo.
- **Conceito cobrado:** Semântica de conectores.
- **Pegadinha usada:** Não reconhecer conectores negativos..
- **Como pensar para acertar:** Tampouco = também não.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 39

- **Alternativa correta:** A.
- **A) está correta:** Retoma o tema e fecha com síntese coerente.
- **B) está errada:** É genérica e pouco relacionada à tese.
- **C) está errada:** Contraria responsabilidade institucional.
- **D) está errada:** Conclusão derrotista e sem proposta de fechamento coerente.
- **Conceito cobrado:** Discursiva: conclusão.
- **Pegadinha usada:** Conclusão genérica ou contraditória..
- **Como pensar para acertar:** Retome tese e argumentos sem abrir assunto novo.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 40

- **Alternativa correta:** D.
- **A) está errada:** Sem acento, mudam ou perdem a grafia normativa no sentido indicado.
- **B) está errada:** Não é monossílabo.
- **C) está errada:** Proparoxítonas são acentuadas independentemente desse final.
- **D) está correta:** Todas têm tonicidade antepenúltima e recebem acento.
- **Conceito cobrado:** Acentuação gráfica.
- **Pegadinha usada:** Aplicar regra de oxítona/paroxítona a proparoxítona..
- **Como pensar para acertar:** Identifique a sílaba tônica.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 41

- **Alternativa correta:** C.
- **A) está errada:** Não há hipótese.
- **B) está errada:** Não há portanto/logo.
- **C) está correta:** Publicar e divulgar são ações somadas.
- **D) está errada:** Não há contraste.
- **Conceito cobrado:** Conectivo aditivo.
- **Pegadinha usada:** Superinterpretar conector simples..
- **Como pensar para acertar:** Nem todo conector esconde contraste; “e” geralmente soma.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 42

- **Alternativa correta:** B.
- **A) está errada:** O padrão esperado é compatível com a norma.
- **B) está correta:** Apto rege preposição “a”; “ao exercício” está correto.
- **C) está errada:** Falta preposição.
- **D) está errada:** Favorável rege preposição “a”: favorável ao candidato.
- **Conceito cobrado:** Regência nominal.
- **Pegadinha usada:** Achar que só verbos regem preposição..
- **Como pensar para acertar:** Nomes como apto, favorável e compatível também pedem complemento regido.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 43

- **Alternativa correta:** A.
- **A) está correta:** O comando muda o alvo da questão.
- **B) está errada:** Familiaridade não garante correção.
- **C) está errada:** Ignorar o comando leva a erro.
- **D) está errada:** Isso inverte o objetivo da questão.
- **Conceito cobrado:** Leitura de enunciado.
- **Pegadinha usada:** Errar por comando negativo..
- **Como pensar para acertar:** Antes das alternativas, marque o comando da questão.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 44

- **Alternativa correta:** D.
- **A) está errada:** Preserva a ordem temporal e a restrição.
- **B) está errada:** Preserva sentido.
- **C) está errada:** Preserva ênfase e ordem temporal.
- **D) está correta:** Altera a ordem temporal expressa por “depois”.
- **Conceito cobrado:** Reescrita e sentido temporal.
- **Pegadinha usada:** Trocar depois por antes..
- **Como pensar para acertar:** Observe advérbios e marcadores temporais.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 45

- **Alternativa correta:** C.
- **A) está errada:** Não indica objetivo.
- **B) está errada:** Não define quem é a equipe; introduz obstáculo.
- **C) está correta:** As restrições eram obstáculo, mas não impediram a conclusão.
- **D) está errada:** As restrições não causaram a conclusão.
- **Conceito cobrado:** Concessão.
- **Pegadinha usada:** Confundir obstáculo superado com causa..
- **Como pensar para acertar:** Apesar de = embora, ainda que.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 46

- **Alternativa correta:** B.
- **A) está errada:** Há mistura inadequada de concordâncias.
- **B) está correta:** Com “mais de um”, o verbo costuma ficar no singular, salvo ideia de reciprocidade.
- **C) está errada:** No caso simples, a concordância esperada é singular.
- **D) está errada:** Falta plural em candidato.
- **Conceito cobrado:** Concordância verbal e nominal.
- **Pegadinha usada:** Não observar núcleo e estrutura fixa..
- **Como pensar para acertar:** Procure expressões especiais e concordância interna.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 47

- **Alternativa correta:** A.
- **A) está correta:** Coesão permite que as ideias se encadeiem.
- **B) está errada:** Tamanho não garante coesão.
- **C) está errada:** Vocabulário difícil não substitui conexão entre ideias.
- **D) está errada:** Pronomes e conectores são recursos de coesão.
- **Conceito cobrado:** Coesão textual.
- **Pegadinha usada:** Confundir coesão com tamanho ou rebuscamento..
- **Como pensar para acertar:** Pergunte se uma ideia leva claramente à próxima.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 48

- **Alternativa correta:** D.
- **A) está errada:** Grafia incorreta.
- **B) está errada:** Grafia incorreta.
- **C) está errada:** Grafia incorreta.
- **D) está correta:** Essa é a grafia correta.
- **Conceito cobrado:** Ortografia.
- **Pegadinha usada:** Grafia de palavra frequente em enunciados..
- **Como pensar para acertar:** Memorize palavras de alta frequência em provas.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 49

- **Alternativa correta:** C.
- **A) está errada:** Não há escolha entre alternativas.
- **B) está errada:** Não indica aumento ou diminuição proporcional.
- **C) está correta:** Explica por que a capacitação é essencial.
- **D) está errada:** Não há contraste.
- **Conceito cobrado:** Locuções conjuntivas.
- **Pegadinha usada:** Não reconhecer locução causal..
- **Como pensar para acertar:** Substitua mentalmente por “porque” e veja se mantém sentido.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

### Comentário da Questão 50

- **Alternativa correta:** B.
- **A) está errada:** Além de informal, há erro com “houveram”.
- **B) está correta:** A frase é específica e clara.
- **C) está errada:** Informal e imprecisa.
- **D) está errada:** Vaga e informal.
- **Conceito cobrado:** Clareza e objetividade.
- **Pegadinha usada:** Usar linguagem vaga/informal..
- **Como pensar para acertar:** Prefira substantivos precisos e verbos claros.
- **Referência à apostila de estudo:** Dia 5 — Língua Portuguesa e Discursiva.

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

---

# Dia 6 — Administração Pública, RLM e Revisão

**Base usada:** edital vigente, apostila de estudo v1.2 e fontes oficiais/estilo indicadas no início deste arquivo.

## Questões

### Questão 1 — Questão autoral no estilo Instituto Consulplan

Em processo seletivo para contratação de solução de tecnologia, servidor sugere restringir o edital a uma marca específica sem justificativa técnica. À luz dos princípios da Administração Pública, a conduta mais adequada é:

A) classificar a despesa como sigilosa para afastar controle externo
B) aceitar a indicação, pois a Administração pode escolher livremente a marca que considerar mais conhecida
C) exigir justificativa técnica objetiva e compatível com o interesse público, evitando direcionamento indevido
D) dispensar a licitação automaticamente, porque tecnologia sempre envolve fornecedor exclusivo

### Questão 2 — Questão autoral no estilo Instituto Consulplan

Sobre os princípios expressos do caput do art. 37 da Constituição Federal, assinale a alternativa correta.

A) Legalidade, impessoalidade, moralidade, publicidade e eficiência orientam a atuação administrativa direta e indireta.
B) Legalidade, pessoalidade, moralidade, sigilo e economicidade são os princípios expressos do art. 37.
C) Os princípios do art. 37 vinculam apenas órgãos federais, não alcançando autarquias estaduais ou municipais.
D) A eficiência permite ignorar a legalidade quando o resultado administrativo for mais rápido.

### Questão 3 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre Administração Direta e Indireta.

A) Órgãos públicos da Administração Direta não possuem personalidade jurídica própria.
B) Empresas públicas e sociedades de economia mista integram a Administração Indireta.
C) Ministérios, secretarias e autarquias são órgãos despersonalizados da Administração Direta.
D) Autarquias integram a Administração Indireta e possuem personalidade jurídica própria.

### Questão 4 — Questão autoral no estilo Instituto Consulplan

Um conselho profissional, criado por lei para fiscalizar determinada profissão, exerce poder de polícia administrativa e arrecada contribuições vinculadas à atividade fiscalizatória. Em regra, sua natureza aproxima-se de:

A) empresa pública exploradora de atividade econômica
B) organização social criada por contrato de gestão, sem lei instituidora
C) autarquia corporativa ou entidade de fiscalização profissional, com regime público em aspectos essenciais
D) fundação privada sem qualquer prerrogativa pública

### Questão 5 — Questão autoral no estilo Instituto Consulplan

Analise as assertivas sobre atos administrativos:

I. Competência, finalidade, forma, motivo e objeto são elementos clássicos do ato administrativo.
II. A presunção de legitimidade permite que o ato produza efeitos até eventual invalidação.
III. A autoexecutoriedade está presente em todos os atos administrativos, sem exceção.

Está correto apenas o que se afirma em:

A) I, II e III
B) I e II
C) I e III
D) II e III

### Questão 6 — Questão autoral no estilo Instituto Consulplan

No tema ato administrativo, assinale a alternativa incorreta.

A) Finalidade é o resultado de interesse público que a Administração busca alcançar.
B) Motivo corresponde aos pressupostos de fato e de direito que justificam a prática do ato.
C) Objeto é o efeito jurídico imediato produzido pelo ato administrativo.
D) Competência pode ser livremente transferida de modo definitivo por acordo informal entre servidores.

### Questão 7 — Questão autoral no estilo Instituto Consulplan

Uma autoridade remove servidor para outra unidade exclusivamente para puni-lo por crítica feita em reunião interna, embora o ato aparente atender ao interesse do serviço. O vício mais evidente está ligado ao elemento:

A) objeto material inexistente
B) competência territorial tributária
C) publicidade externa obrigatória
D) finalidade

### Questão 8 — Questão autoral no estilo Instituto Consulplan

Em licitação para contratação de serviço comum de suporte técnico, a Administração pretende adotar modalidade adequada à disputa de bens e serviços comuns, com lances e julgamento objetivo. Em regra, a modalidade mais associada a essa lógica é:

A) leilão
B) diálogo competitivo
C) pregão
D) concurso

### Questão 9 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre contratação direta.

A) Dispensa e inexigibilidade são expressões equivalentes e podem ser usadas indistintamente pela Administração.
B) Dispensa ocorre em hipóteses legais nas quais a competição é possível em tese, mas a lei autoriza não licitar.
C) Inexigibilidade ocorre quando a competição é inviável, como em fornecedor exclusivo devidamente comprovado.
D) Contratação direta exige processo com justificativas e não elimina dever de motivação.

### Questão 10 — Questão autoral no estilo Instituto Consulplan

Em contratação de objeto complexo de tecnologia, a Administração ainda não consegue definir sozinha a solução técnica mais adequada e precisa dialogar com licitantes previamente selecionados para desenvolver alternativas. A modalidade que melhor se ajusta a esse desenho é:

A) diálogo competitivo
B) leilão
C) concurso
D) credenciamento

### Questão 11 — Questão autoral no estilo Instituto Consulplan

Analise as assertivas sobre licitação:

I. O edital vincula tanto a Administração quanto os licitantes.
II. O julgamento deve observar critérios previamente definidos no instrumento convocatório.
III. A Administração pode alterar critérios de julgamento após a abertura das propostas para favorecer a proposta que considere mais conveniente.

Está correto apenas o que se afirma em:

A) I e III
B) II e III
C) I, II e III
D) I e II

### Questão 12 — Questão autoral no estilo Instituto Consulplan

Sobre critérios de julgamento em licitações, assinale a alternativa incorreta.

A) Técnica e preço pode ser adequado quando qualidade técnica e preço precisam ser ponderados.
B) A Administração pode escolher qualquer critério depois de conhecer as propostas, desde que economize recursos.
C) Menor preço é critério possível quando o objeto admite comparação objetiva de preço.
D) Maior desconto pode ser usado quando a disputa se dá sobre desconto aplicado a parâmetro definido.

### Questão 13 — Questão autoral no estilo Instituto Consulplan

Um agente público causa dano a particular, no exercício de função administrativa, durante operação regular de fiscalização. Em regra, para responsabilização civil objetiva do Estado por ato comissivo, exige-se:

A) contrato firmado entre vítima e Administração
B) conduta estatal, dano e nexo causal
C) dolo específico do agente e condenação penal prévia
D) prova de culpa administrativa em todos os casos

### Questão 14 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre responsabilidade civil do Estado.

A) Culpa exclusiva da vítima pode excluir o dever de indenizar.
B) Caso fortuito ou força maior podem afastar responsabilidade quando rompem o nexo causal.
C) Culpa concorrente da vítima pode atenuar o valor da indenização.
D) Na responsabilidade objetiva, o dano é presumido e não precisa ser demonstrado.

### Questão 15 — Questão autoral no estilo Instituto Consulplan

Em caso de omissão estatal, como ausência de manutenção mínima de estrutura pública conhecida como perigosa, a análise costuma exigir com mais força:

A) aplicação automática da responsabilidade objetiva em qualquer falta de serviço público
B) inexistência de responsabilidade porque omissão nunca indeniza
C) necessidade de contrato administrativo com a vítima
D) verificação do dever específico de agir, possibilidade de atuação e nexo com o dano

### Questão 16 — Questão autoral no estilo Instituto Consulplan

Sobre improbidade administrativa, assinale a alternativa correta.

A) Improbidade só pode ocorrer quando há enriquecimento ilícito do agente.
B) Ato de improbidade é sempre matéria penal e só pode ser julgado após condenação criminal.
C) Nem toda ilegalidade administrativa configura improbidade; é necessário enquadramento legal e elemento subjetivo quando exigido.
D) Qualquer erro formal em processo administrativo, mesmo sem relevância, é improbidade automática.

### Questão 17 — Questão autoral no estilo Instituto Consulplan

Analise as assertivas sobre improbidade:

I. Atos de improbidade podem envolver enriquecimento ilícito, dano ao erário ou violação de princípios, conforme enquadramento legal.
II. O simples desacordo técnico razoável entre servidores, sem má-fé ou prejuízo relevante, caracteriza improbidade automaticamente.
III. A responsabilização por improbidade deve observar devido processo e defesa.

Está correto apenas o que se afirma em:

A) I, II e III
B) I e III
C) I e II
D) II e III

### Questão 18 — Questão autoral no estilo Instituto Consulplan

Em uma autarquia, a autoridade competente decide anular ato ilegal que concedeu vantagem indevida a servidor. A anulação administrativa decorre principalmente do princípio da:

A) autotutela
B) continuidade do serviço público
C) especialidade
D) hierarquia das fontes privadas

### Questão 19 — Questão autoral no estilo Instituto Consulplan

Assinale a alternativa incorreta sobre controle da Administração Pública.

A) Controle externo pode ser exercido pelo Legislativo com auxílio do tribunal de contas, conforme o caso.
B) Controle judicial pode verificar legalidade de atos administrativos.
C) Controle judicial substitui livremente o administrador para escolher a solução mais conveniente em qualquer caso.
D) Controle interno é exercido dentro da própria estrutura administrativa.

### Questão 20 — Questão autoral no estilo Instituto Consulplan

Em pedido de acesso a documentos de procedimento administrativo, o órgão público deve partir da premissa de que:

A) informações públicas só podem ser entregues a advogados constituídos
B) o servidor pode negar acesso sem motivar para evitar trabalho adicional
C) a publicidade é regra e o sigilo é exceção justificada nas hipóteses legais
D) todo documento administrativo é sigiloso até autorização judicial

### Questão 21 — Questão autoral no estilo Instituto Consulplan

Um banco de dados de órgão público contém CPF, telefone e endereço de cidadãos atendidos. Ao tratar esses dados, a Administração deve:

A) apagar todos os dados imediatamente, impedindo a prestação do serviço
B) observar finalidade, necessidade, segurança e base legal para o tratamento
C) publicar integralmente a base porque todo dado estatal é público
D) compartilhar os dados livremente com qualquer fornecedor interessado

### Questão 22 — Questão autoral no estilo Instituto Consulplan

A respeito do poder de polícia administrativa, assinale a alternativa correta.

A) permite condicionar e restringir direitos individuais em benefício do interesse público, nos limites legais
B) autoriza qualquer restrição sem previsão legal quando a autoridade considerar conveniente
C) é exercido exclusivamente pelo Poder Judiciário após processo penal
D) elimina a necessidade de contraditório em todos os processos sancionadores

### Questão 23 — Questão autoral no estilo Instituto Consulplan

Em processo administrativo sancionador, antes de aplicar penalidade, a Administração deve assegurar, como regra:

A) decisão secreta sem ciência do interessado
B) aplicação da sanção antes da apuração para evitar demora
C) renúncia automática ao recurso administrativo
D) contraditório e ampla defesa

### Questão 24 — Questão autoral no estilo Instituto Consulplan

A motivação dos atos administrativos é especialmente relevante porque:

A) substitui a publicidade e torna o ato sigiloso
B) transforma todo ato vinculado em discricionário
C) permite controlar as razões de fato e de direito que sustentam a decisão
D) dispensa a existência de competência legal para o ato

### Questão 25 — Questão autoral no estilo Instituto Consulplan

Se a proposição P representa “o sistema está disponível” e Q representa “o usuário autenticou”, a negação de P -> Q é:

A) não P e não Q
B) P e não Q
C) não P e Q
D) não P ou Q

### Questão 26 — Questão autoral no estilo Instituto Consulplan

Considere a proposição: “Todo processo eletrônico possui número de protocolo”. Sua negação lógica é:

A) Existe processo eletrônico que não possui número de protocolo.
B) Nenhum processo eletrônico possui número de protocolo.
C) Todo processo sem número de protocolo é eletrônico.
D) Existe número de protocolo que não possui processo eletrônico.

### Questão 27 — Questão autoral no estilo Instituto Consulplan

Em um setor, 18 servidores conhecem SQL, 12 conhecem Linux e 7 conhecem ambos. O número de servidores que conhece SQL ou Linux é:

A) 30
B) 37
C) 16
D) 23

### Questão 28 — Questão autoral no estilo Instituto Consulplan

Um contrato de manutenção custa R$ 48.000,00 por 12 meses. Mantidas as mesmas condições proporcionais, o custo para 5 meses será:

A) R$ 24.000,00
B) R$ 9.600,00
C) R$ 20.000,00
D) R$ 19.200,00

### Questão 29 — Questão autoral no estilo Instituto Consulplan

Um equipamento teve reajuste de 12% sobre o preço de R$ 7.500,00. O novo preço é:

A) R$ 6.600,00
B) R$ 8.400,00
C) R$ 8.250,00
D) R$ 9.000,00

### Questão 30 — Questão autoral no estilo Instituto Consulplan

Após desconto de 15%, um software passou a custar R$ 3.400,00. O preço original era:

A) R$ 4.000,00
B) R$ 3.910,00
C) R$ 3.850,00
D) R$ 4.250,00

### Questão 31 — Questão autoral no estilo Instituto Consulplan

Uma equipe resolve 36 chamados em 4 horas com 3 técnicos trabalhando no mesmo ritmo. Com 6 técnicos, em 5 horas, a quantidade esperada de chamados é:

A) 72
B) 60
C) 120
D) 90

### Questão 32 — Questão autoral no estilo Instituto Consulplan

A sequência 7, 11, 15, 19, ... é uma progressão aritmética. O 20º termo é:

A) 87
B) 76
C) 83
D) 80

### Questão 33 — Questão autoral no estilo Instituto Consulplan

Em uma progressão geométrica de primeiro termo 3 e razão 2, a soma dos 6 primeiros termos é:

A) 63
B) 189
C) 96
D) 192

### Questão 34 — Questão autoral no estilo Instituto Consulplan

Em uma urna há 5 crachás azuis e 3 vermelhos. Retirando-se dois crachás sem reposição, a probabilidade de ambos serem azuis é:

A) 5/14
B) 25/64
C) 10/28
D) 3/8

### Questão 35 — Questão autoral no estilo Instituto Consulplan

Em uma comissão de 4 pessoas, há 2 analistas de sistemas entre 10 servidores. Sorteando-se 1 pessoa ao acaso, a probabilidade de não ser analista de sistemas é:

A) 1/5
B) 2/5
C) 3/5
D) 4/5

### Questão 36 — Questão autoral no estilo Instituto Consulplan

A negação da proposição “O relatório foi entregue e o protocolo foi gerado” é:

A) O relatório foi entregue ou o protocolo foi gerado.
B) Se o relatório foi entregue, então o protocolo foi gerado.
C) O relatório não foi entregue ou o protocolo não foi gerado.
D) O relatório não foi entregue e o protocolo não foi gerado.

### Questão 37 — Questão autoral no estilo Instituto Consulplan

Considere verdadeira a afirmação: “Se há backup íntegro, então a restauração é possível”. Se a restauração não é possível, pode-se concluir logicamente que:

A) a afirmação condicional é necessariamente falsa
B) não há backup íntegro
C) há backup íntegro
D) a restauração é possível mesmo sem backup

### Questão 38 — Questão autoral no estilo Instituto Consulplan

Em uma tabela-verdade com três proposições simples independentes P, Q e R, o número de linhas é:

A) 8
B) 6
C) 9
D) 12

### Questão 39 — Questão autoral no estilo Instituto Consulplan

Em uma pesquisa interna, 40 servidores usam o sistema A, 25 usam o sistema B, 10 usam ambos e 8 não usam nenhum dos dois. O total de servidores pesquisados é:

A) 75
B) 55
C) 73
D) 63

### Questão 40 — Questão autoral no estilo Instituto Consulplan

Sobre a Lei de Licitações, princípios e procedimento, assinale a alternativa incorreta.

A) O julgamento deve seguir critério previsto, preservando isonomia entre licitantes.
B) A Administração pode fracionar despesa para enquadrar artificialmente a contratação em hipótese de dispensa.
C) A fase preparatória deve buscar adequada definição do objeto e justificativa da contratação.
D) A publicidade permite controle social, ressalvadas hipóteses legais de sigilo.

### Questão 41 — Questão autoral no estilo Instituto Consulplan

Uma contratação pública exige objeto padronizado, disputa clara e julgamento pelo menor preço. A providência mais alinhada ao princípio do julgamento objetivo é:

A) ocultar os critérios para evitar recursos
B) definir previamente critérios mensuráveis e aplicá-los a todos os licitantes
C) permitir que a comissão escolha a proposta que pareça mais simpática ao interesse público
D) alterar o critério caso a proposta preferida não vença

### Questão 42 — Questão autoral no estilo Instituto Consulplan

Um particular sofre dano porque servidor, dirigindo veículo oficial em serviço, colide por desatenção. O Estado indeniza a vítima e comprova culpa do servidor. Em tese, em relação ao agente, cabe:

A) ação regressiva, observados dolo ou culpa do agente
B) cobrança regressiva automática sem apurar conduta do agente
C) impossibilidade absoluta de regresso porque a responsabilidade estatal é objetiva
D) transferência da indenização diretamente à seguradora privada sem processo

### Questão 43 — Questão autoral no estilo Instituto Consulplan

Em controle de legalidade, a revogação de ato administrativo válido, porém inconveniente ou inoportuno, difere da anulação porque:

A) revogação sempre decorre de ordem judicial; anulação sempre depende de licitação
B) revogação corrige vício de competência; anulação corrige falta de orçamento
C) revogação e anulação são sinônimos no controle administrativo
D) revogação atua sobre mérito administrativo; anulação atua sobre ilegalidade

### Questão 44 — Questão autoral no estilo Instituto Consulplan

Sobre atos administrativos vinculados e discricionários, assinale a alternativa incorreta.

A) Mesmo no ato discricionário, competência, finalidade e forma permanecem vinculadas à lei.
B) Ato discricionário permite decisão contrária à lei quando a autoridade invoca eficiência.
C) No ato vinculado, a lei define os requisitos de modo mais fechado, reduzindo margem de escolha.
D) No ato discricionário, a Administração decide dentro de margem legal de conveniência e oportunidade.

### Questão 45 — Questão autoral no estilo Instituto Consulplan

Em uma repartição, 60% dos processos foram concluídos no prazo. Dos 240 processos recebidos, o número de processos concluídos fora do prazo foi:

A) 120
B) 96
C) 144
D) 80

### Questão 46 — Questão autoral no estilo Instituto Consulplan

Três servidores analisam 90 processos em 6 dias. Mantido o ritmo, cinco servidores analisam 150 processos em:

A) 6 dias
B) 5 dias
C) 9 dias
D) 10 dias

### Questão 47 — Questão autoral no estilo Instituto Consulplan

A soma dos múltiplos de 5 entre 5 e 100, inclusive, é:

A) 1000
B) 950
C) 525
D) 1050

### Questão 48 — Questão autoral no estilo Instituto Consulplan

Se 2^x = 64, então 2^(x+2) vale:

A) 66
B) 4096
C) 256
D) 128

### Questão 49 — Questão autoral no estilo Instituto Consulplan

Em uma equipe, a razão entre analistas e técnicos é 3:5. Se há 24 analistas, o total de servidores da equipe é:

A) 72
B) 64
C) 40
D) 48

### Questão 50 — Questão autoral no estilo Instituto Consulplan

Considere as proposições: P é falsa e Q é verdadeira. O valor lógico de P ou (não Q) é:

A) falso
B) verdadeiro
C) indeterminado
D) verdadeiro apenas se P implicar Q

## Gabarito do Dia 6

1. C
2. A
3. C
4. C
5. B
6. D
7. D
8. C
9. A
10. A
11. D
12. B
13. B
14. D
15. D
16. C
17. B
18. A
19. C
20. C
21. B
22. A
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
40. B
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

## Comentários do Dia 6

### Comentário da Questão 1

- **Alternativa correta:** C.
- **A) está errada:** Sigilo é excepcional e não elimina controle; publicidade e motivação são regras no procedimento administrativo.
- **B) está errada:** A escolha pública deve ser motivada e vinculada ao interesse público; preferência sem justificativa pode violar impessoalidade, isonomia e competitividade.
- **C) está correta:** A decisão administrativa deve observar legalidade, impessoalidade, moralidade, publicidade, eficiência e princípios licitatórios, com motivação técnica quando houver especificação restritiva.
- **D) está errada:** Exclusividade precisa ser demonstrada quando cabível; não se presume só por se tratar de tecnologia.
- **Conceito cobrado:** Princípios do art. 37 e licitação.
- **Pegadinha usada:** Tratar conveniência administrativa como liberdade absoluta de escolha..
- **Como pensar para acertar:** Em restrição de edital, procure motivação técnica, isonomia e competitividade.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 2

- **Alternativa correta:** A.
- **A) está correta:** Esses são os princípios expressos do caput do art. 37, aplicáveis à Administração Pública direta e indireta.
- **B) está errada:** Pessoalidade e sigilo não substituem impessoalidade e publicidade no rol expresso do caput.
- **C) está errada:** O caput menciona Administração direta e indireta de qualquer dos Poderes da União, Estados, Distrito Federal e Municípios.
- **D) está errada:** Eficiência não autoriza afastar a legalidade; os princípios atuam de forma conjunta.
- **Conceito cobrado:** Princípios constitucionais da Administração Pública.
- **Pegadinha usada:** Achar que eficiência supera legalidade..
- **Como pensar para acertar:** Memorize LIMPE e lembre que nenhum princípio expresso anula os demais.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 3

- **Alternativa correta:** C.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Essa afirmação está correta: órgãos são centros de competência sem personalidade distinta da pessoa federativa.
- **B) está correta como afirmação:** Essa afirmação está correta: ambas são entidades administrativas da Administração Indireta.
- **C) é a incorreta:** Essa é a incorreta: autarquias não são órgãos; são entidades da Administração Indireta com personalidade própria.
- **D) está correta como afirmação:** Essa afirmação está correta: autarquias são pessoas jurídicas de direito público integrantes da Administração Indireta.
- **Conceito cobrado:** Administração Direta e Indireta.
- **Pegadinha usada:** Misturar órgão com entidade..
- **Como pensar para acertar:** Separe órgão sem personalidade de entidade com personalidade própria.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 4

- **Alternativa correta:** C.
- **A) está errada:** Conselho profissional não é criado para exploração empresarial de mercado.
- **B) está errada:** Organizações sociais são entidades privadas qualificadas; a fiscalização profissional decorre de lei e poder público.
- **C) está correta:** Conselhos profissionais costumam ser tratados como entidades de fiscalização profissional com natureza autárquica em pontos centrais, especialmente no exercício de poder de polícia.
- **D) está errada:** A fiscalização profissional envolve competências públicas e não se resume a atividade privada.
- **Conceito cobrado:** Autarquias e conselhos profissionais.
- **Pegadinha usada:** Confundir conselho profissional com entidade privada comum..
- **Como pensar para acertar:** Observe criação legal, fiscalização profissional e poder de polícia.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 5

- **Alternativa correta:** B.
- **A) está errada:** A assertiva III impede o conjunto completo, pois transforma atributo eventual em universal.
- **B) está correta:** I está correta quanto aos elementos; II está correta porque os atos presumem-se legítimos até prova ou decisão em contrário.
- **C) está errada:** III é falsa: autoexecutoriedade não existe em todos os atos; depende de previsão legal ou urgência.
- **D) está errada:** I também está correta; além disso, III generaliza indevidamente.
- **Conceito cobrado:** Ato administrativo: elementos e atributos.
- **Pegadinha usada:** Usar “todos” para generalizar atributo que não é universal..
- **Como pensar para acertar:** Liste os elementos e trate atributos com cuidado: presunção é ampla; autoexecutoriedade não é absoluta.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 6

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: finalidade vincula o ato ao interesse público e ao objetivo previsto em lei.
- **B) está correta como afirmação:** Correta: motivo envolve situação fática e fundamento jurídico.
- **C) está correta como afirmação:** Correta: objeto é o conteúdo ou efeito imediato do ato.
- **D) é a incorreta:** Incorreta: competência decorre de norma, é em regra irrenunciável e sua delegação/avocação seguem limites legais.
- **Conceito cobrado:** Elementos do ato administrativo.
- **Pegadinha usada:** Tratar competência como propriedade pessoal do agente..
- **Como pensar para acertar:** Competência vem da lei; não nasce de acordo informal.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 7

- **Alternativa correta:** D.
- **A) está errada:** O objeto do ato pode existir formalmente; o problema central é a intenção desviada.
- **B) está errada:** A questão não envolve tributação nem competência territorial fiscal.
- **C) está errada:** A publicidade pode ser relevante, mas não explica a punição disfarçada como interesse do serviço.
- **D) está correta:** Há desvio de finalidade quando o ato é praticado com objetivo diverso do interesse público previsto, ainda que use forma aparentemente válida.
- **Conceito cobrado:** Desvio de finalidade.
- **Pegadinha usada:** Confundir motivo aparente com finalidade real..
- **Como pensar para acertar:** Procure a pergunta: o ato foi usado para alcançar finalidade pública ou objetivo pessoal/punitivo disfarçado?
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 8

- **Alternativa correta:** C.
- **A) está errada:** Leilão é ligado à alienação de bens, não à contratação comum de suporte técnico.
- **B) está errada:** Diálogo competitivo é voltado a contratações complexas em que a Administração dialoga para estruturar solução.
- **C) está correta:** Pregão é associado à contratação de bens e serviços comuns, com disputa por lances e critério objetivo, conforme a lógica cobrada em concursos.
- **D) está errada:** Concurso é modalidade voltada à escolha de trabalho técnico, científico ou artístico, com prêmio ou remuneração.
- **Conceito cobrado:** Modalidades de licitação.
- **Pegadinha usada:** Trocar modalidade pelo nome conhecido sem olhar objeto da contratação..
- **Como pensar para acertar:** Identifique primeiro o objeto: bem/serviço comum aponta para pregão.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 9

- **Alternativa correta:** A.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) é a incorreta:** Incorreta: dispensa e inexigibilidade têm fundamentos diferentes e não são sinônimos.
- **B) está correta como afirmação:** Correta: na dispensa, a licitação seria possível, mas a lei permite contratar diretamente em situações previstas.
- **C) está correta como afirmação:** Correta: a inviabilidade de competição é núcleo da inexigibilidade.
- **D) está correta como afirmação:** Correta: contratar diretamente não significa contratar sem procedimento ou sem controle.
- **Conceito cobrado:** Dispensa e inexigibilidade.
- **Pegadinha usada:** Achar que contratação direta é uma categoria única sem distinções..
- **Como pensar para acertar:** Pergunte se a competição é possível: se sim, pode haver dispensa; se inviável, inexigibilidade.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 10

- **Alternativa correta:** A.
- **A) está correta:** O diálogo competitivo é voltado a contratações complexas em que a Administração dialoga com licitantes para desenvolver solução antes das propostas finais.
- **B) está errada:** Leilão não serve para estruturar solução técnica complexa; está ligado à alienação de bens.
- **C) está errada:** Concurso escolhe trabalho técnico, científico ou artístico, não estrutura contratação complexa por diálogo.
- **D) está errada:** Credenciamento é procedimento auxiliar para contratar todos que preencham condições, não a modalidade descrita.
- **Conceito cobrado:** Modalidades de licitação.
- **Pegadinha usada:** Confundir modalidade com procedimento auxiliar..
- **Como pensar para acertar:** Quando houver solução complexa e diálogo para definir alternativas, pense em diálogo competitivo.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 11

- **Alternativa correta:** D.
- **A) está errada:** III viola vinculação, julgamento objetivo e isonomia.
- **B) está errada:** I também está correta, e III é incompatível com o procedimento licitatório.
- **C) está errada:** O conjunto não procede porque a assertiva III admite favorecimento e mudança indevida de critérios.
- **D) está correta:** Vinculação ao edital e julgamento objetivo exigem respeito aos critérios previamente estabelecidos.
- **Conceito cobrado:** Princípios licitatórios.
- **Pegadinha usada:** Confundir discricionariedade com liberdade para mudar regra no meio do certame..
- **Como pensar para acertar:** Critério de julgamento precisa estar antes e ser aplicado sem casuísmo.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 12

- **Alternativa correta:** B.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: esse critério combina avaliação técnica e econômica conforme o objeto.
- **B) é a incorreta:** Incorreta: o critério deve ser definido previamente; economia não justifica surpresa ou quebra de isonomia.
- **C) está correta como afirmação:** Correta: menor preço é critério tradicional e objetivo.
- **D) está correta como afirmação:** Correta: o maior desconto é critério previsto para situações em que há base de comparação.
- **Conceito cobrado:** Critérios de julgamento.
- **Pegadinha usada:** Colocar economicidade acima da vinculação ao edital..
- **Como pensar para acertar:** Critérios são fixados antes da disputa; depois aplica-se o que foi anunciado.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 13

- **Alternativa correta:** B.
- **A) está errada:** Responsabilidade extracontratual não depende de contrato com a vítima.
- **B) está correta:** Na responsabilidade objetiva por ato comissivo, a vítima deve demonstrar conduta, dano e nexo, sem necessidade de provar culpa do agente.
- **C) está errada:** Dolo e condenação penal não são requisitos gerais da responsabilidade civil objetiva do Estado.
- **D) está errada:** A responsabilidade objetiva dispensa prova de culpa, embora culpa possa importar para regresso.
- **Conceito cobrado:** Responsabilidade civil do Estado.
- **Pegadinha usada:** Achar que responsabilidade objetiva elimina nexo causal..
- **Como pensar para acertar:** Mesmo sem culpa, procure sempre dano e nexo entre ação estatal e prejuízo.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 14

- **Alternativa correta:** D.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: se o dano decorre exclusivamente da vítima, rompe-se o nexo causal.
- **B) está correta como afirmação:** Correta: eventos externos podem excluir responsabilidade se eliminarem o nexo com a atuação estatal.
- **C) está correta como afirmação:** Correta: concorrência causal pode reduzir a indenização conforme a participação da vítima.
- **D) é a incorreta:** Incorreta: responsabilidade objetiva dispensa culpa, mas não dispensa prova de dano e nexo causal.
- **Conceito cobrado:** Excludentes e atenuantes da responsabilidade civil.
- **Pegadinha usada:** Confundir dispensa de culpa com dispensa de prova do dano..
- **Como pensar para acertar:** Objetiva não significa automática; exige dano e nexo.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 15

- **Alternativa correta:** D.
- **A) está errada:** A omissão não gera responsabilidade automática em qualquer hipótese; exige análise do dever e do nexo.
- **B) está errada:** Omissão pode gerar responsabilidade quando presentes requisitos jurídicos.
- **C) está errada:** A responsabilidade por omissão não depende de contrato com a vítima.
- **D) está correta:** Em omissões, a cobrança costuma avaliar se havia dever concreto de agir, possibilidade de evitar o dano e relação causal com a omissão.
- **Conceito cobrado:** Responsabilidade por omissão.
- **Pegadinha usada:** Usar regra de ato comissivo como fórmula automática para toda omissão..
- **Como pensar para acertar:** Em omissão, pergunte: havia dever concreto e possibilidade real de agir?
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 16

- **Alternativa correta:** C.
- **A) está errada:** Há outras categorias além de enriquecimento ilícito, como dano ao erário e violação de princípios, conforme enquadramento legal.
- **B) está errada:** Improbidade tem regime próprio de responsabilização civil-administrativa, ainda que possa coexistir com esfera penal.
- **C) está correta:** A improbidade é ilícito qualificado; concurso costuma cobrar que ilegalidade simples não basta automaticamente.
- **D) está errada:** Erro formal pode gerar correção ou nulidade, mas não necessariamente improbidade.
- **Conceito cobrado:** Improbidade administrativa.
- **Pegadinha usada:** Transformar toda irregularidade em improbidade..
- **Como pensar para acertar:** Procure gravidade, enquadramento e elemento subjetivo; não pule direto para improbidade.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 17

- **Alternativa correta:** B.
- **A) está errada:** O conjunto é falso por causa da assertiva II.
- **B) está correta:** I resume categorias relevantes; III preserva garantias processuais. II generaliza indevidamente e transforma divergência técnica em improbidade automática.
- **C) está errada:** II está errada porque improbidade não decorre automaticamente de divergência técnica razoável.
- **D) está errada:** I também está correta, e II é a pegadinha.
- **Conceito cobrado:** Improbidade administrativa.
- **Pegadinha usada:** Confundir erro, divergência ou ilegalidade simples com improbidade qualificada..
- **Como pensar para acertar:** Separe irregularidade administrativa de ato ímprobo.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 18

- **Alternativa correta:** A.
- **A) está correta:** A autotutela permite à Administração anular seus próprios atos ilegais e revogar atos inconvenientes ou inoportunos, observados limites e garantias.
- **B) está errada:** Continuidade trata da permanência do serviço, não da correção de ato ilegal.
- **C) está errada:** Especialidade limita entidades aos fins para os quais foram criadas, mas não é o fundamento principal da anulação de ato ilegal.
- **D) está errada:** A expressão não é princípio administrativo aplicável ao caso.
- **Conceito cobrado:** Autotutela administrativa.
- **Pegadinha usada:** Trocar autotutela por controle externo ou por continuidade..
- **Como pensar para acertar:** Quando a Administração corrige o próprio ato, pense em autotutela.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 19

- **Alternativa correta:** C.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: é uma forma clássica de controle externo.
- **B) está correta como afirmação:** Correta: o Judiciário controla legalidade, respeitando limites quanto ao mérito administrativo.
- **C) é a incorreta:** Incorreta: o Judiciário não substitui o mérito administrativo legítimo de modo amplo; atua especialmente sobre legalidade e abuso.
- **D) está correta como afirmação:** Correta: controle interno ocorre no âmbito da própria Administração.
- **Conceito cobrado:** Controle administrativo, legislativo e judicial.
- **Pegadinha usada:** Confundir controle de legalidade com substituição integral do mérito administrativo..
- **Como pensar para acertar:** Controle judicial não é administração paralela; foque legalidade, desvio e abuso.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 20

- **Alternativa correta:** C.
- **A) está errada:** O acesso à informação não depende genericamente de representação por advogado.
- **B) está errada:** Negativa de acesso exige fundamento; conveniência interna não basta.
- **C) está correta:** A lógica da transparência administrativa é publicidade como regra, com sigilo apenas quando houver fundamento legal.
- **D) está errada:** Isso inverte a regra de publicidade e transparência.
- **Conceito cobrado:** Publicidade e acesso à informação.
- **Pegadinha usada:** Tratar sigilo como regra por comodidade administrativa..
- **Como pensar para acertar:** Em prova, transparência começa pela publicidade; exceções precisam de base legal.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 21

- **Alternativa correta:** B.
- **A) está errada:** Proteção de dados não significa impossibilitar serviço público; significa tratar com base e limites.
- **B) está correta:** Tratamento de dados pessoais pelo poder público exige finalidade pública, adequação, necessidade, segurança e base legal.
- **C) está errada:** Dados pessoais não se tornam publicáveis indiscriminadamente por estarem em órgão público.
- **D) está errada:** Compartilhamento exige fundamento, finalidade e controles; não é livre.
- **Conceito cobrado:** LGPD aplicada ao setor público.
- **Pegadinha usada:** Confundir publicidade administrativa com exposição de dados pessoais..
- **Como pensar para acertar:** Separe transparência pública de proteção de dados pessoais.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 22

- **Alternativa correta:** A.
- **A) está correta:** Poder de polícia é atividade estatal de limitar ou disciplinar direitos, atividades e bens em razão do interesse público, dentro da lei.
- **B) está errada:** Poder de polícia também se submete à legalidade e proporcionalidade.
- **C) está errada:** Poder de polícia administrativa é exercido pela Administração, sem se confundir com polícia judiciária.
- **D) está errada:** Processos sancionadores devem observar garantias, ainda que haja medidas cautelares em situações específicas.
- **Conceito cobrado:** Poder de polícia.
- **Pegadinha usada:** Associar polícia administrativa apenas a segurança pública ou processo penal..
- **Como pensar para acertar:** Busque a ideia de limitar atividades privadas em nome do interesse público, com base legal.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 23

- **Alternativa correta:** D.
- **A) está errada:** Sigilo absoluto e ausência de ciência violam garantias processuais.
- **B) está errada:** A sanção exige apuração regular, salvo medidas cautelares proporcionais e fundamentadas que não substituem o julgamento.
- **C) está errada:** O interessado não perde automaticamente meios de impugnação por ser investigado.
- **D) está correta:** Sanções administrativas devem observar garantias processuais, inclusive oportunidade de defesa.
- **Conceito cobrado:** Processo administrativo sancionador.
- **Pegadinha usada:** Confundir eficiência com punição sem processo..
- **Como pensar para acertar:** Em sanção, procure contraditório, ampla defesa e motivação.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 24

- **Alternativa correta:** C.
- **A) está errada:** Motivação não substitui publicidade; ambos podem ser necessários.
- **B) está errada:** Motivação não altera a natureza vinculada ou discricionária do ato.
- **C) está correta:** Motivação explicita fundamentos, permite controle e protege contra arbitrariedade.
- **D) está errada:** Motivar não corrige incompetência; competência continua necessária.
- **Conceito cobrado:** Motivação administrativa.
- **Pegadinha usada:** Achar que fundamentar convalida qualquer vício..
- **Como pensar para acertar:** Motivação mostra o porquê; não apaga falta de competência, finalidade ou objeto lícito.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 25

- **Alternativa correta:** B.
- **A) está errada:** A condicional só é falsa quando P é verdadeiro e Q é falso.
- **B) está correta:** A negação da condicional é antecedente verdadeiro e consequente falso: P ∧ ¬Q.
- **C) está errada:** Isso nega o antecedente e mantém o consequente; não é a negação da condicional.
- **D) está errada:** ¬P ∨ Q é equivalente à própria condicional, não à sua negação.
- **Conceito cobrado:** Lógica proposicional: negação da condicional.
- **Pegadinha usada:** Negar cada parte sem respeitar a tabela-verdade..
- **Como pensar para acertar:** Condicional só falha em V -> F; transforme isso em P e não Q.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 26

- **Alternativa correta:** A.
- **A) está correta:** A negação de “todo A é B” é “existe A que não é B”.
- **B) está errada:** Isso é o contrário universal, mais forte que a negação lógica.
- **C) está errada:** Essa proposição altera a relação entre os conjuntos e não nega a original.
- **D) está errada:** Troca sujeito e predicado, criando outra afirmação.
- **Conceito cobrado:** Negação de quantificadores.
- **Pegadinha usada:** Confundir negação com contrária universal..
- **Como pensar para acertar:** Negue “todo” com “existe pelo menos um que não”.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 27

- **Alternativa correta:** D.
- **A) está errada:** Soma 18 + 12 sem retirar a interseção contada duas vezes.
- **B) está errada:** Soma também a interseção, aumentando indevidamente o total.
- **C) está errada:** Subtrai a interseção duas vezes ou usa operação inadequada.
- **D) está correta:** Pela inclusão-exclusão: 18 + 12 - 7 = 23.
- **Conceito cobrado:** Conjuntos: inclusão-exclusão.
- **Pegadinha usada:** Contar duas vezes quem pertence aos dois grupos..
- **Como pensar para acertar:** Para “ou”, some os conjuntos e subtraia a interseção uma vez.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 28

- **Alternativa correta:** C.
- **A) está errada:** Esse seria o custo de 6 meses, não de 5.
- **B) está errada:** Esse corresponde a 2,4 meses na proporção dada, não a 5 meses.
- **C) está correta:** 48.000 / 12 = 4.000 por mês; em 5 meses, 4.000 x 5 = 20.000.
- **D) está errada:** Esse valor decorre de aplicar 40% em vez da proporção correta de 5/12.
- **Conceito cobrado:** Regra de três simples.
- **Pegadinha usada:** Usar porcentagem aproximada sem calcular a razão correta..
- **Como pensar para acertar:** Encontre primeiro o valor unitário ou monte a proporção 12 para 48.000, 5 para x.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 29

- **Alternativa correta:** B.
- **A) está errada:** Esse valor subtrai 12%, mas o enunciado fala em reajuste positivo.
- **B) está correta:** 12% de 7.500 é 900; 7.500 + 900 = 8.400.
- **C) está errada:** Esse valor corresponde a reajuste de 10%, não de 12%.
- **D) está errada:** Esse valor adiciona 20%, não 12%.
- **Conceito cobrado:** Porcentagem.
- **Pegadinha usada:** Confundir aumento com desconto ou usar 10% por aproximação..
- **Como pensar para acertar:** Calcule 12% = 0,12 e some ao preço inicial.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 30

- **Alternativa correta:** A.
- **A) está correta:** Se 3.400 representa 85% do preço original, então original = 3.400 / 0,85 = 4.000.
- **B) está errada:** Esse valor soma 15% sobre 3.400, mas desconto percentual não se desfaz somando o mesmo percentual sobre o valor final.
- **C) está errada:** Não corresponde à divisão por 0,85; mistura desconto com diferença absoluta.
- **D) está errada:** Esse valor supõe que 3.400 seja 80% do original, não 85%.
- **Conceito cobrado:** Porcentagem reversa.
- **Pegadinha usada:** Somar 15% ao valor descontado para voltar ao preço original..
- **Como pensar para acertar:** Quando o valor final é após desconto, divida por 1 - taxa.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 31

- **Alternativa correta:** D.
- **A) está errada:** Esse valor dobra os técnicos, mas mantém 4 horas, ignorando a quinta hora.
- **B) está errada:** Esse valor não preserva a proporção composta entre técnicos e tempo.
- **C) está errada:** Esse valor superestima a produção ao aplicar fator incorreto.
- **D) está correta:** A produtividade é 36 / (4 x 3) = 3 chamados por técnico-hora; 6 x 5 x 3 = 90.
- **Conceito cobrado:** Regra de três composta.
- **Pegadinha usada:** Variar duas grandezas e considerar apenas uma..
- **Como pensar para acertar:** Calcule produtividade por técnico-hora ou monte proporção com técnicos e tempo.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 32

- **Alternativa correta:** C.
- **A) está errada:** Esse valor soma 20 razões ao primeiro termo, mas até o 20º termo há 19 intervalos.
- **B) está errada:** Esse valor considera razão ou número de intervalos menor que o correto.
- **C) está correta:** Em PA, an = a1 + (n-1)r. Assim, a20 = 7 + 19 x 4 = 83.
- **D) está errada:** Esse valor usa 20 x 4 sem considerar corretamente o primeiro termo.
- **Conceito cobrado:** Progressão aritmética.
- **Pegadinha usada:** Usar n razões em vez de n-1..
- **Como pensar para acertar:** Do primeiro ao vigésimo termo há 19 saltos.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 33

- **Alternativa correta:** B.
- **A) está errada:** 63 é a soma dos seis primeiros termos da PG 1,2,4,8,16,32, sem multiplicar pelo primeiro termo 3.
- **B) está correta:** S6 = 3(2^6 - 1)/(2 - 1) = 3 x 63 = 189.
- **C) está errada:** 96 é o sexto termo multiplicado por fator inadequado, não a soma total.
- **D) está errada:** 192 corresponde a 3 x 64, sem subtrair 1 na fórmula da soma.
- **Conceito cobrado:** Progressão geométrica.
- **Pegadinha usada:** Confundir termo geral com soma da PG..
- **Como pensar para acertar:** Para soma da PG finita, use a1(q^n - 1)/(q - 1) quando q diferente de 1.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 34

- **Alternativa correta:** A.
- **A) está correta:** A probabilidade é 5/8 x 4/7 = 20/56 = 5/14.
- **B) está errada:** Esse cálculo trataria as retiradas como independentes com reposição.
- **C) está errada:** Embora equivalente a 5/14 se simplificado, a forma 10/28 indicaria contagem de combinações mal feita; a alternativa esperada simplificada é 5/14.
- **D) está errada:** 3/8 é a proporção inicial de vermelhos, não a probabilidade de dois azuis.
- **Conceito cobrado:** Probabilidade sem reposição.
- **Pegadinha usada:** Usar reposição quando o enunciado diz sem reposição..
- **Como pensar para acertar:** Atualize o denominador e o numerador após a primeira retirada.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 35

- **Alternativa correta:** D.
- **A) está errada:** 1/5 é a probabilidade de ser analista de sistemas, não de não ser.
- **B) está errada:** 2/5 corresponderia a 4 em 10, mas o enunciado tem 8 não analistas.
- **C) está errada:** Não corresponde ao complemento de 2/10.
- **D) está correta:** Há 8 servidores que não são analistas de sistemas entre 10; 8/10 = 4/5.
- **Conceito cobrado:** Probabilidade complementar.
- **Pegadinha usada:** Responder a probabilidade do evento, não do complemento solicitado..
- **Como pensar para acertar:** Calcule o complemento: P(não A) = 1 - P(A).
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 36

- **Alternativa correta:** C.
- **A) está errada:** Essa proposição é uma disjunção sem negação dos termos.
- **B) está errada:** Isso transforma conjunção em condicional, não é negação lógica.
- **C) está correta:** Pela lei de De Morgan, negar P e Q resulta em não P ou não Q.
- **D) está errada:** Isso nega os dois simultaneamente, mas a negação de conjunção exige pelo menos um falso.
- **Conceito cobrado:** Leis de De Morgan.
- **Pegadinha usada:** Trocar “e” por “e” ao negar, em vez de trocar para “ou”..
- **Como pensar para acertar:** Negue os termos e troque o conectivo: não(P e Q) = não P ou não Q.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 37

- **Alternativa correta:** B.
- **A) está errada:** Se o consequente é falso, a condicional só seria falsa se P fosse verdadeiro; a conclusão lógica é não P.
- **B) está correta:** Pelo modus tollens, de P -> Q e não Q conclui-se não P.
- **C) está errada:** Isso contradiz a consequência lógica da condicional com consequente falso.
- **D) está errada:** O enunciado informa que a restauração não é possível.
- **Conceito cobrado:** Argumentação lógica: modus tollens.
- **Pegadinha usada:** Confundir modus tollens com afirmação do consequente..
- **Como pensar para acertar:** Com P -> Q e ¬Q, conclua ¬P.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 38

- **Alternativa correta:** A.
- **A) está correta:** Com n proposições simples, a tabela-verdade tem 2^n linhas; para 3, 2^3 = 8.
- **B) está errada:** 6 resulta de 3 x 2, mas a combinação é exponencial, não multiplicação simples por 2.
- **C) está errada:** 9 seria 3^2, operação sem relação com a quantidade de valores lógicos binários.
- **D) está errada:** 12 não corresponde a 2^3.
- **Conceito cobrado:** Tabela-verdade.
- **Pegadinha usada:** Multiplicar n por 2 em vez de calcular 2^n..
- **Como pensar para acertar:** Cada proposição dobra o número de combinações.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 39

- **Alternativa correta:** D.
- **A) está errada:** Soma A + B + nenhum sem retirar a interseção duplicada.
- **B) está errada:** 55 é apenas o total que usa ao menos um sistema; falta somar quem não usa nenhum.
- **C) está errada:** Subtrai ou soma a interseção de modo incorreto.
- **D) está correta:** Usam ao menos um: 40 + 25 - 10 = 55. Somando os 8 que não usam nenhum, total = 63.
- **Conceito cobrado:** Conjuntos com complemento.
- **Pegadinha usada:** Esquecer o grupo fora dos conjuntos..
- **Como pensar para acertar:** Calcule a união e depois some quem está fora dela.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 40

- **Alternativa correta:** B.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: julgamento objetivo e vinculação protegem a igualdade.
- **B) é a incorreta:** Incorreta: fracionamento indevido para burlar licitação viola a finalidade do regime de contratação.
- **C) está correta como afirmação:** Correta: planejamento e definição adequada do objeto são centrais para contratação pública.
- **D) está correta como afirmação:** Correta: publicidade é regra com exceções justificadas.
- **Conceito cobrado:** Licitação: planejamento e vedação ao fracionamento indevido.
- **Pegadinha usada:** Confundir gestão por parcelas com fracionamento para burlar licitação..
- **Como pensar para acertar:** Parcelamento técnico pode existir; fracionamento artificial para dispensar licitação é o problema.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 41

- **Alternativa correta:** B.
- **A) está errada:** Critérios precisam ser conhecidos para possibilitar controle e competição.
- **B) está correta:** Julgamento objetivo exige critérios claros e aplicação uniforme.
- **C) está errada:** Simpatia ou preferência subjetiva viola objetividade e impessoalidade.
- **D) está errada:** Mudança posterior quebra vinculação e isonomia.
- **Conceito cobrado:** Julgamento objetivo.
- **Pegadinha usada:** Confundir interesse público com escolha subjetiva sem critério..
- **Como pensar para acertar:** Critério objetivo é anunciado antes e aplicado depois.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 42

- **Alternativa correta:** A.
- **A) está correta:** Após indenizar, o Estado pode buscar ressarcimento do agente causador quando demonstrados dolo ou culpa.
- **B) está errada:** Regresso contra agente exige demonstração de dolo ou culpa.
- **C) está errada:** A objetividade perante a vítima não impede regresso contra agente culpado ou doloso.
- **D) está errada:** A questão cobra relação Estado-agente; eventual seguro não elimina requisitos de regresso.
- **Conceito cobrado:** Responsabilidade civil e ação regressiva.
- **Pegadinha usada:** Confundir responsabilidade objetiva do Estado com responsabilidade automática do agente..
- **Como pensar para acertar:** Perante a vítima, o Estado responde objetivamente; contra o agente, apura dolo ou culpa.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 43

- **Alternativa correta:** D.
- **A) está errada:** A afirmação mistura temas sem relação e inverte a lógica da autotutela.
- **B) está errada:** Vício de competência é tema de legalidade, não de revogação por mérito.
- **C) está errada:** Não são sinônimos; possuem fundamentos diferentes.
- **D) está correta:** Revogação desfaz ato válido por conveniência/oportunidade; anulação retira ato ilegal.
- **Conceito cobrado:** Anulação e revogação.
- **Pegadinha usada:** Tratar todo desfazimento de ato como anulação..
- **Como pensar para acertar:** Pergunte se o problema é ilegalidade ou conveniência.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 44

- **Alternativa correta:** B.
- **Observação:** a questão pede a alternativa incorreta; portanto, o gabarito é a afirmação errada.
- **A) está correta como afirmação:** Correta: discricionariedade não torna todos os elementos livres.
- **B) é a incorreta:** Incorreta: discricionariedade existe dentro da legalidade; eficiência não autoriza decisão ilegal.
- **C) está correta como afirmação:** Correta: ato vinculado deixa pouca ou nenhuma liberdade quanto à prática quando presentes requisitos.
- **D) está correta como afirmação:** Correta: discricionariedade é liberdade dentro da lei.
- **Conceito cobrado:** Atos vinculados e discricionários.
- **Pegadinha usada:** Achar que discricionariedade é liberdade sem limite..
- **Como pensar para acertar:** Discricionariedade é escolha legítima dentro da moldura legal.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 45

- **Alternativa correta:** B.
- **A) está errada:** 120 seria 50% do total.
- **B) está correta:** Se 60% foram no prazo, 40% ficaram fora do prazo; 40% de 240 = 96.
- **C) está errada:** 144 é o número concluído no prazo, não fora do prazo.
- **D) está errada:** 80 corresponde a um terço de 240, não a 40%.
- **Conceito cobrado:** Porcentagem e complemento.
- **Pegadinha usada:** Responder o percentual informado em vez do complemento pedido..
- **Como pensar para acertar:** Quando a questão pede fora do prazo, use 100% - 60%.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 46

- **Alternativa correta:** A.
- **A) está correta:** Produtividade: 90/(3 x 6)=5 processos por servidor-dia. Cinco servidores fazem 25 por dia; 150/25 = 6 dias.
- **B) está errada:** Esse valor supõe produtividade maior do que a informada.
- **C) está errada:** Ignora o aumento de servidores em relação ao primeiro cenário.
- **D) está errada:** Usa proporção direta apenas com processos, sem considerar servidores.
- **Conceito cobrado:** Regra de três composta.
- **Pegadinha usada:** Não ajustar simultaneamente produção e quantidade de servidores..
- **Como pensar para acertar:** Calcule produtividade por servidor-dia para evitar inversão.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 47

- **Alternativa correta:** D.
- **A) está errada:** Erro comum ao considerar média 50 em vez de 52,5 ou excluir um termo.
- **B) está errada:** Provável exclusão indevida do 100 ou do 5.
- **C) está errada:** Metade da soma correta, como se houvesse 10 termos em vez de 20.
- **D) está correta:** É PA de 5 a 100 com razão 5. Há 20 termos; soma = (5 + 100) x 20 / 2 = 1050.
- **Conceito cobrado:** Progressão aritmética: soma.
- **Pegadinha usada:** Contar termos incorretamente nos extremos inclusivos..
- **Como pensar para acertar:** Conte os termos e use média dos extremos vezes quantidade.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 48

- **Alternativa correta:** C.
- **A) está errada:** Expoente não se soma ao resultado da potência dessa forma.
- **B) está errada:** Esse é 64^2, mas 2^(x+2) = 2^x x 2^2 = 64 x 4.
- **C) está correta:** Como 2^x = 64 = 2^6, x = 6. Logo 2^(x+2)=2^8=256.
- **D) está errada:** Esse valor seria 2^(x+1), não 2^(x+2).
- **Conceito cobrado:** Potenciação.
- **Pegadinha usada:** Tratar soma de expoente como soma no resultado..
- **Como pensar para acertar:** Use propriedades: 2^(x+2)=2^x x 2^2.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 49

- **Alternativa correta:** B.
- **A) está errada:** Superestima o total por atribuir valor errado a cada parte da razão.
- **B) está correta:** 3 partes correspondem a 24, então 1 parte vale 8. Técnicos: 5 x 8 = 40. Total = 24 + 40 = 64.
- **C) está errada:** 40 é o número de técnicos, não o total.
- **D) está errada:** Esse valor usaria razão 3:3 ou cálculo incompleto.
- **Conceito cobrado:** Razão e proporção.
- **Pegadinha usada:** Confundir uma parte do grupo com o total..
- **Como pensar para acertar:** Transforme a razão em partes e encontre o valor de uma parte.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

### Comentário da Questão 50

- **Alternativa correta:** A.
- **A) está correta:** P é falso; não Q é falso porque Q é verdadeiro. Falso ou falso resulta falso.
- **B) está errada:** Não há parcela verdadeira na disjunção.
- **C) está errada:** Com valores de P e Q dados, a expressão tem valor determinado.
- **D) está errada:** A expressão não depende de condicional; é uma disjunção simples.
- **Conceito cobrado:** Operadores lógicos.
- **Pegadinha usada:** Esquecer de negar Q antes de aplicar o “ou”..
- **Como pensar para acertar:** Calcule de dentro para fora: primeiro não Q, depois a disjunção.
- **Referência à apostila de estudo:** Dia 6 — Administração Pública, RLM e Revisão.

---
