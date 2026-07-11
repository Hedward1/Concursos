# Super Simulado — Semana 1

**Finalidade:** 60 questões inéditas, de alta dificuldade, para integrar Arquitetura, Sistemas Operacionais, Banco de Dados, Legislação CRA/CFA, Português, Administração Pública e RLM.

**Aplicação sugerida:** 4h30 sem consulta. Marque as questões de maior incerteza e preencha o caderno de erros apenas após a correção comentada.

## Bloco 1 — Arquitetura e organização de computadores

### Questão 1

Um processador usa cache com alta localidade temporal em um laço que atualiza repetidamente o mesmo contador. A conclusão correta é:

A) o contador tende a permanecer acessível em cache após acessos recentes.  
B) a localidade temporal elimina a necessidade de RAM.  
C) a localidade espacial exige acesso a endereços aleatórios.  
D) cache é memória secundária persistente.

### Questão 2

Considere `11111111₂ + 1₂` em registrador de 8 bits sem extensão. O resultado armazenado e a condição relevante são:

A) `100000000₂`, sem perda.  
B) `11111111₂`, com underflow.  
C) `00000001₂`, com carry ignorado.
D) `00000000₂`, com overflow no limite do registrador.  

### Questão 3

Em uma operação de E/S orientada por interrupção, a sequência conceitualmente adequada é:

A) CPU consulta sem parar o dispositivo e nunca suspende fluxo.  
B) dispositivo sinaliza evento; CPU executa rotina apropriada e retoma o fluxo.  
C) DMA executa toda instrução da aplicação.  
D) o periférico altera diretamente o código-fonte.

### Questão 4

Um barramento de dados de 32 bits significa, principalmente, que:

A) endereça exatamente 32 bytes de memória.  
B) o processador possui 32 registradores.  
C) transfere grupos de até 32 bits por operação de barramento, conforme o projeto.  
D) toda instrução possui 32 bits.

### Questão 5

Sobre compilador, ligador e carregador, assinale a correta.

A) o carregador transforma linguagem de alto nível em objeto.  
B) o ligador resolve referências entre módulos; o carregador prepara o programa para execução.  
C) o interpretador sempre produz executável independente.  
D) o compilador substitui o sistema operacional na alocação de memória.

### Questão 6

Uma política write-back em cache, em contraste com write-through, tende a:

A) adiar a propagação até a linha modificada precisar ser substituída ou sincronizada.  
B) atualizar a memória principal a cada escrita de cache.  
C) impedir qualquer incoerência entre níveis.  
D) dispensar bits de modificação.

### Questão 7

No complemento de dois de 8 bits, `11111111₂` representa:

A) 255.  
B) −127.  
C) 1.
D) −1.  

### Questão 8

Uma CPU executa instruções enquanto um controlador DMA transfere bloco de disco para RAM. A afirmação correta é:

A) DMA elimina toda participação da CPU, inclusive configuração e conclusão.  
B) DMA é igual a polling.  
C) DMA reduz cópias por byte pela CPU, mas exige coordenação e normalmente sinaliza conclusão.  
D) DMA transfere dados apenas entre caches.

### Questão 9

Em hierarquia de memória, a razão principal para cache ser menor e mais rápida que RAM é:

A) armazenar todos os arquivos do sistema.  
B) substituir registradores.  
C) explorar localidade com tecnologia de menor latência e maior custo por bit.  
D) impedir paginação.

### Questão 10

Analise as assertivas.

I. Um byte possui oito bits.  
II. Hexadecimal facilita representar agrupamentos de quatro bits.  
III. Todo número binário de oito bits representa valor positivo.

Está correto o que se afirma em:

A) I e III, apenas.  
B) I e II, apenas.  
C) II e III, apenas.  
D) I, II e III.

## Bloco 2 — Sistemas operacionais

### Questão 11

Uma thread aguarda a conclusão de leitura em disco. Sem considerar particularidades do SO, seu estado mais adequado é:

A) bloqueada, pois aguarda evento de E/S.  
B) pronta, pois aguarda somente CPU.  
C) terminada.  
D) executando em kernel continuamente.

### Questão 12

Em paginação por demanda, um page fault significa necessariamente que:

A) o endereço virtual é sempre inválido.  
B) houve deadlock.  
C) a TLB foi permanentemente corrompida.
D) a página referenciada não está residente e o SO deve tratar a situação.  

### Questão 13

Um processo A mantém recurso X e espera Y; B mantém Y e espera X. A situação descreve:

A) espera circular, uma condição de Coffman.  
B) starvation.  
C) condição de corrida.  
D) interrupção mascarável.

### Questão 14

Qual alternativa distingue corretamente mutex de semáforo contador?

A) mutex é usado somente em processos distintos; semáforo somente em threads.  
B) semáforo elimina todo deadlock.  
C) ambos garantem justiça de escalonamento.
D) mutex controla exclusão por um titular; semáforo contador pode representar múltiplas unidades disponíveis.  

### Questão 15

No Round Robin, um quantum excessivamente grande aproxima o comportamento de:

A) SJF preemptivo.  
B) FCFS para tarefas que não bloqueiam antes do fim do quantum.  
C) escalonamento por prioridade estrita.  
D) deadlock evitável.

### Questão 16

Sobre sistema de arquivos com journaling, assinale a correta.

A) journaling é cópia independente para recuperar versão antiga.  
B) journaling substitui ACL e permissões.  
C) journaling registra operações para ajudar a recuperar consistência após falha.  
D) journaling impede qualquer corrupção de dados da aplicação.

### Questão 17

Em Linux, `chmod 640 relatorio` concede:

A) execução ao dono e leitura a todos.  
B) leitura e escrita ao dono, leitura ao grupo e nada a outros.  
C) leitura e escrita a todos.  
D) somente leitura ao dono.

### Questão 18

Uma thread de baixa prioridade mantém mutex necessário a thread de alta prioridade, enquanto threads médias ocupam CPU. O risco predominante é:

A) inversão de prioridade.  
B) fragmentação externa.  
C) page fault.  
D) livelock obrigatório.

### Questão 19

Polling e interrupção são adequados, respectivamente, quando:

A) dispositivo sinaliza; CPU nunca é notificada.  
B) ambos transferem bloco por DMA.  
C) ambos suspendem permanentemente a CPU.
D) CPU consulta estado repetidamente; dispositivo sinaliza evento assíncrono.  

### Questão 20

Em Windows, a permissão efetiva de acesso remoto a arquivo pode depender de:

A) somente da maior permissão NTFS.  
B) apenas do nome do arquivo.  
C) compartilhamento e NTFS, além da identidade e herança aplicáveis.  
D) somente da extensão do arquivo.

## Bloco 3 — Banco de dados e SQL

### Questão 21

Em uma relação `MATRICULA(aluno, disciplina, professor)`, a dependência `disciplina → professor` pode indicar anomalia quando a chave é `(aluno, disciplina)` porque:

A) toda dependência parcial é chave candidata.  
B) a relação está necessariamente em BCNF.  
C) professor depende de parte da chave composta, sugerindo decomposição.  
D) professor deve ser atributo multivalorado.

### Questão 22

Para listar departamentos sem empregados, a estratégia relacional mais direta é:

A) `INNER JOIN` e `WHERE empregado.id IS NOT NULL`.  
B) `LEFT JOIN` de departamento para empregado e filtro de identificador nulo do empregado.  
C) `CROSS JOIN` sem filtro.  
D) `GROUP BY` sem junção.

### Questão 23

Em SQL, condição sobre resultado agregado deve aparecer tipicamente em:

A) `HAVING`, após o agrupamento.  
B) `WHERE`, sempre.  
C) `ORDER BY`, exclusivamente.  
D) `FROM`, antes das tabelas.

### Questão 24

Uma transação transfere valor entre contas e falha após debitar a origem, antes de creditar destino. A propriedade que exige estado “tudo ou nada” é:

A) isolamento.  
B) durabilidade.  
C) independência física.
D) atomicidade.  

### Questão 25

Uma chave estrangeira preserva principalmente:

A) integridade referencial entre relação filha e relação referenciada.  
B) ordenação física dos registros.  
C) confidencialidade de colunas.  
D) exclusão automática de duplicatas em qualquer atributo.

### Questão 26

Considere `SELECT COUNT(*) FROM T WHERE x <> 5;` com `x` nulo em uma linha. Essa linha:

A) é contada, porque nulo é diferente de 5.  
B) gera erro obrigatório.  
C) é convertida em zero.
D) não satisfaz o predicado, pois a comparação resulta em desconhecido.  

### Questão 27

Uma decomposição é preferível quando reduz redundância sem perder a possibilidade de reconstruir a relação original por junção. Esse requisito é:

A) dependência multivalorada.  
B) junção sem perda.  
C) negação de integridade.  
D) materialização obrigatória.

### Questão 28

Sob isolamento `READ COMMITTED`, uma transação não deve ler:

A) dado confirmado por outra transação.  
B) sua própria escrita.  
C) dado ainda não confirmado por outra transação.  
D) nenhuma linha duas vezes.

### Questão 29

Índice pode piorar desempenho de escrita porque:

A) elimina páginas de dados.  
B) precisa ser mantido em inserções, alterações e exclusões.  
C) impede predicados seletivos.  
D) substitui estatísticas do otimizador.

### Questão 30

Em modelagem ER, uma entidade fraca é caracterizada, em geral, por:

A) depender de entidade proprietária para identificação completa.  
B) não possuir atributos.  
C) ter somente relacionamentos N:N.  
D) não poder ser mapeada ao modelo relacional.

## Bloco 4 — Legislação CRA/CFA

### Questão 31

Na hierarquia estudada, a associação correta é:

A) Lei organiza apenas o CRA-PR; Código cria autarquias.  
B) Decreto revoga automaticamente a Lei.  
C) Regimento substitui registro profissional.
D) Lei estrutura profissão e sistema; Decreto regulamenta; Regimento organiza o CRA; Código disciplina conduta.  

### Questão 32

O exercício profissional sem o registro exigido pela Lei nº 4.769/1965 é:

A) plenamente regular se houver diploma.  
B) permitido somente em pessoa jurídica.  
C) ilegal e sujeito às consequências previstas, pois diploma não substitui registro.  
D) questão exclusiva do CFA, sem CRA competente.

### Questão 33

Compete ao CRA, em sua jurisdição, principalmente:

A) editar Constituição Federal.  
B) exercer somente função consultiva.  
C) executar diretrizes, manter registro e fiscalizar exercício profissional.  
D) julgar recurso nacional como única instância.

### Questão 34

Em matéria ético-disciplinar, é incompatível com o Código:

A) comunicar alteração relevante ao Conselho.  
B) assinar documento de terceiro sem orientação ou supervisão.  
C) preservar independência técnica.  
D) colaborar com fiscalização regular.

### Questão 35

Sobre o CFA, assinale a correta.

A) examina, modifica e aprova regimentos regionais, nos termos legais.  
B) atua apenas no Paraná.  
C) expede exclusivamente toda carteira regional.  
D) não integra o Sistema CFA/CRAs.

### Questão 36

Uma empresa que explora atividade abrangida profissionalmente deve observar:

A) que só pessoa física se registra.  
B) liberdade para usar título profissional sem responsável.  
C) dispensa automática por ser privada.
D) registro e fiscalização nos termos da Lei e normas aplicáveis.  

### Questão 37

O princípio da legalidade para autarquia profissional exige que:

A) atuação tenha fundamento e limites no ordenamento.  
B) agente faça tudo que a lei não proíbe.  
C) eficiência afaste formalidade legal.  
D) publicidade permita promoção pessoal.

### Questão 38

No Regimento do CRA-PR, o Plenário é corretamente descrito como:

A) órgão privado de apoio informal.  
B) substituto do CFA nacional.  
C) órgão sem competência decisória.
D) órgão colegiado de deliberação superior e primeira instância regional, conforme o Regimento.  

### Questão 39

Sanção ética pressupõe, em regra:

A) impressão subjetiva sem processo.  
B) processo regular, tipificação e garantia de defesa, observadas as regras aplicáveis.  
C) decisão automática de terceiro.  
D) ausência de trânsito administrativo.

### Questão 40

O uso de registro profissional de terceiro é grave porque:

A) amplia a concorrência legítima.  
B) substitui a carteira de identidade.  
C) compromete habilitação, responsabilidade e fiscalização profissional.  
D) é permitido para pessoa jurídica.

## Bloco 5 — Português e discursiva

### Questão 41

Leia: “Embora a autarquia tenha digitalizado o atendimento, persistem riscos que exigem controles.” A reescrita equivalente é:

A) Como digitalizou, a autarquia eliminou os riscos.  
B) Ainda que tenha digitalizado o atendimento, a autarquia continua sujeita a riscos que exigem controles.  
C) A autarquia digitalizou, portanto os riscos persistem por causa da digitalização.  
D) Se digitalizasse, os riscos deixariam de existir.

### Questão 42

No período “Os relatórios que continham dados pessoais foram restringidos”, a oração destacada:

A) restringe o conjunto aos relatórios que continham dados pessoais.  
B) isola explicação sobre todos os relatórios.  
C) expressa causa da restrição.  
D) equivale a uma oração coordenada conclusiva.

### Questão 43

Assinale a alternativa correta quanto à concordância.

A) Haviam indícios de falha e existe controles suficientes.  
B) Houveram indícios e deve existirem providências.  
C) Fazem dois anos que houveram ocorrências.
D) Havia indícios de falha e existem controles suficientes.  

### Questão 44

Assinale a frase correta quanto a regência e crase.

A) A equipe obedeceu a norma e começou à revisar os registros.  
B) O Conselho referiu-se à todos os responsáveis.  
C) A equipe obedeceu à norma e começou a revisar os registros.  
D) A decisão foi favorável a à defesa.

### Questão 45

Em texto técnico, a substituição de “pode reduzir o risco” por “elimina o risco” é inadequada porque:

A) preserva o mesmo grau de certeza.  
B) apenas reduz o tamanho do período.  
C) troca possibilidade por garantia absoluta.  
D) melhora a coesão por omitir o sujeito.

### Questão 46

Assinale a pontuação correta.

A) Os conselheiros, aprovaram o relatório final.  
B) Após a análise dos autos, o Plenário deliberou sobre o recurso.  
C) O CRA-PR decidiu, encaminhar o processo.  
D) A fiscalização que identificou a falha, comunicou o fato.

### Questão 47

Em “O CRA comunicou ao profissional que seu registro precisava de atualização”, a ambiguidade de “seu” é eliminada por:

A) “O CRA comunicou ao profissional que o registro do profissional precisava de atualização.”  
B) retirar o possessivo, sem indicar titular.  
C) trocar “profissional” por “ele”.  
D) usar “registro precisava-se”.

### Questão 48

Uma conclusão discursiva tecnicamente adequada deve:

A) introduzir tema novo sem relação com a tese.  
B) repetir literalmente todos os argumentos.  
C) evitar qualquer verbo de ação.
D) retomar a tese e propor encaminhamento coerente com o desenvolvimento.  

### Questão 49

Há paralelismo em:

A) A política prevê proteger dados, revisar acessos e registrar incidentes.  
B) A política prevê proteger dados, a revisão de acessos e que se registre incidentes.  
C) A política prevê a proteção de dados, revisar acessos e incidentes registrados.  
D) Proteger dados, a revisão e que incidentes sejam registro.

### Questão 50

Em uma redação sobre proteção de dados, o argumento mais consistente é:

A) transparência exige divulgação irrestrita de qualquer dado pessoal.  
B) proteção de dados impede toda publicidade administrativa.  
C) somente tecnologia, sem governança, resolve o problema.
D) finalidade, necessidade e segurança devem compatibilizar transparência e proteção de dados.  

## Bloco 6 — Administração Pública, RLM e revisão

### Questão 51

Uma autoridade revoga ato válido por mudança de conveniência administrativa. A medida é:

A) anulação por ilegalidade.  
B) revogação por mérito, respeitados limites jurídicos.  
C) convalidação obrigatória.  
D) controle judicial de oportunidade.

### Questão 52

Em regra, a convalidação é possível quando o vício:

A) envolve finalidade desviada, sempre.  
B) decorre de crime, sem processo.  
C) é sanável e não causa lesão ao interesse público nem prejuízo a terceiros.  
D) elimina necessidade de motivação.

### Questão 53

O art. 37, §1º, da Constituição veda que publicidade institucional:

A) informe serviços ao cidadão.  
B) caracterize promoção pessoal de autoridade ou servidor.  
C) tenha caráter educativo ou de orientação social.  
D) identifique o órgão responsável.

### Questão 54

Sobre LAI e LGPD, é correto afirmar que:

A) transparência e proteção de dados devem ser compatibilizadas conforme finalidade e restrições legais.  
B) qualquer dado pessoal torna sigiloso todo documento.  
C) LGPD impede tratamento pelo Poder Público em qualquer hipótese.  
D) LAI elimina necessidade de segurança.

### Questão 55

Negue logicamente a frase “Todos os processos foram analisados e nenhum recurso foi provido”.

A) Nenhum processo foi analisado ou todo recurso foi provido.  
B) Algum processo foi analisado e nenhum recurso foi provido.  
C) Todos os processos foram analisados ou algum recurso foi provido.
D) Algum processo não foi analisado ou algum recurso foi provido.  

### Questão 56

Se `P → Q` é verdadeira e `Q` é falsa, então:

A) P é necessariamente verdadeira.  
B) nada pode ser concluído sobre P.  
C) P é necessariamente falsa.  
D) Q é verdadeira por contraposição.

### Questão 57

Uma sequência começa em 3 e cada termo é o dobro do anterior mais 1. O quarto termo é:

A) 15.  
B) 23.  
C) 31.  
D) 47.

### Questão 58

Em licitação, contratação direta não significa ausência de fundamento legal; significa:

A) escolha livre do gestor.  
B) hipótese legal de dispensa ou inexigibilidade, observados requisitos aplicáveis.  
C) proibição de motivação.  
D) substituição de toda pesquisa de preços.

### Questão 59

Para responsabilidade civil objetiva do Estado, em regra, exige-se:

A) dano, conduta administrativa e nexo causal, sem exigência de provar culpa subjetiva do agente.  
B) condenação criminal prévia do agente.  
C) risco integral em toda situação.  
D) inexistência de serviço público.

### Questão 60

No caderno de erros, a estratégia mais eficaz após errar questão por confundir anulação e revogação é:

A) memorizar apenas a letra do gabarito.  
B) excluir a questão para evitar repetição.  
C) estudar assunto sem revisar o erro.
D) registrar a distinção ilegalidade × mérito e resolver caso novo que a exija.  

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

- **A)** Correta. Aplica corretamente a regra de localidade e cache.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** localidade e cache.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 2

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de aritmética binária.

**Conceito:** aritmética binária.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 3

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de interrupções.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** interrupções.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 4

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de barramentos.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** barramentos.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 5

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de ferramentas de tradução.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** ferramentas de tradução.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 6

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de políticas de escrita.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** políticas de escrita.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 7

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de complemento de dois.

**Conceito:** complemento de dois.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 8

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de DMA.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** DMA.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 9

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de hierarquia de memória.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** hierarquia de memória.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 10

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de representação numérica.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** representação numérica.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 1 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 11

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de estados de thread.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** estados de thread.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 12

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de paginação.

**Conceito:** paginação.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 13

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de deadlock.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** deadlock.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 14

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de sincronização.

**Conceito:** sincronização.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 15

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de Round Robin.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** Round Robin.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 16

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de journaling.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** journaling.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 17

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de permissões Linux.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** permissões Linux.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 18

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de inversão de prioridade.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** inversão de prioridade.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 19

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de polling e interrupção.

**Conceito:** polling e interrupção.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 20

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de permissões Windows.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** permissões Windows.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 2 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 21

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de normalização.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** normalização.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 22

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de junções SQL.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** junções SQL.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 23

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de agregação SQL.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** agregação SQL.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 24

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de ACID.

**Conceito:** ACID.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 25

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de integridade referencial.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** integridade referencial.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 26

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de NULL em SQL.

**Conceito:** NULL em SQL.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 27

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de junção sem perda.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** junção sem perda.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 28

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de isolamento.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** isolamento.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 29

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de índices.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** índices.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 30

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de entidade fraca.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** entidade fraca.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 3 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 31

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de hierarquia normativa.

**Conceito:** hierarquia normativa.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 32

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de registro profissional.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** registro profissional.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 33

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de competência do CRA.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** competência do CRA.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 34

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de ética profissional.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** ética profissional.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 35

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de competência do CFA.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** competência do CFA.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 36

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de registro de pessoa jurídica.

**Conceito:** registro de pessoa jurídica.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 37

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de legalidade.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** legalidade.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 38

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de Plenário.

**Conceito:** Plenário.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 39

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de processo disciplinar.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** processo disciplinar.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 40

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de uso indevido de registro.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** uso indevido de registro.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 4 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 41

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de concessão.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** concessão.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 42

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de oração restritiva.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** oração restritiva.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 43

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de concordância.

**Conceito:** concordância.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 44

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de regência e crase.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** regência e crase.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 45

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de modalidade.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** modalidade.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 46

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de pontuação.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** pontuação.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 47

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de referência pronominal.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** referência pronominal.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 48

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de conclusão discursiva.

**Conceito:** conclusão discursiva.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 49

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de paralelismo.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** paralelismo.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 50

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de proteção de dados.

**Conceito:** proteção de dados.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 5 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 51

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de revogação.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** revogação.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 52

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de convalidação.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** convalidação.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 53

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de impessoalidade.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** impessoalidade.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 54

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de LAI e LGPD.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** LAI e LGPD.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 55

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de negação lógica.

**Conceito:** negação lógica.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 56

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de modus tollens.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** modus tollens.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 57

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Correta. Aplica corretamente a regra de sequência.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** sequência.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 58

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Correta. Aplica corretamente a regra de contratação direta.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** contratação direta.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 59

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica corretamente a regra de responsabilidade estatal.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.

**Conceito:** responsabilidade estatal.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.

### Comentário da Questão 60

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **B)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **C)** Incorreta. Contraria a relação, o limite ou a finalidade exigida no enunciado.
- **D)** Correta. Aplica corretamente a regra de caderno de erros.

**Conceito:** caderno de erros.

**Pegadinha:** trocar um conceito próximo pela regra efetivamente cobrada.

**Como pensar:** isole a condição decisiva do caso e descarte alternativas que ampliam, invertem ou deslocam sua função.

**Referência:** Semana 1, Dia 6 — teoria, prática guiada e mapa de conexões do dia correspondente.
