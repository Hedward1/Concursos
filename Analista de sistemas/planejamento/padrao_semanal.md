# Padrão de Qualidade das Semanas de Estudo

Este documento é o contrato de estrutura para toda semana criada ou revisada no repositório. Ele preserva a autonomia temática de cada semana, mas impede que teoria, questões e revisões tenham níveis diferentes de acabamento.

## Modelo oficial de avaliação e aceite

Toda apostila deve passar pelo mesmo ciclo de qualidade:

1. **Planejar:** selecionar os tópicos no Plano Mestre e conferir sua correspondência literal com o edital vigente.
2. **Mapear:** registrar o que será ensinado, exemplificado, memorizado e cobrado em cada dia.
3. **Produzir a teoria:** explicar o conteúdo do básico à aplicação, sem pressupor conhecimento que ainda não foi apresentado.
4. **Resolver exemplos:** demonstrar o raciocínio completo, o resultado e o erro mais provável em cada tópico importante.
5. **Produzir as questões:** cobrar apenas conteúdos ensinados ou explicitamente classificados como revisão de semana anterior.
6. **Comentar as respostas:** explicar a correta, cada alternativa errada, o conceito, a pegadinha e o caminho mental para chegar à resposta.
7. **Auditar:** validar estrutura, conteúdo, fontes, gabarito, referências e alinhamento entre os dois arquivos.
8. **Aprovar:** somente considerar o material aprovado para execução quando não houver falha eliminatória e a nota da rubrica for igual ou superior a 90 pontos. O status `Concluído` depende também da execução pelo candidato.

### Critérios eliminatórios

A ocorrência de qualquer item abaixo reprova o material, independentemente da nota:

- conteúdo incompatível com o edital oficial vigente ou norma apresentada como certa sem fonte confirmada;
- tema cobrado nas questões sem sustentação suficiente na apostila de estudo ou em revisão anterior identificada;
- gabarito tecnicamente incorreto, ambíguo ou incompatível com o comentário;
- questão sem quatro alternativas A–D, com alternativa E ou sem uma única melhor resposta;
- questão sem nível válido imediatamente abaixo do título ou com dificuldade artificialmente inflada para fechar uma matriz; as matrizes diárias 20/20/10 e 8/8/4 orientam a produção, mas uma auditoria semântica posterior pode recalibrar níveis quando registrar item, motivo e distribuição final;
- distrator absurdo, alheio ao tema, meramente cômico ou eliminável sem conhecimento do conteúdo;
- dificuldade artificial criada por ambiguidade, informação ausente, texto desnecessariamente longo ou pista visual na alternativa correta;
- comentário que não analise individualmente A, B, C e D;
- exemplo resolvido sem raciocínio, solução ou explicação do resultado;
- quantidade, numeração, gabarito ou comentário incompleto;
- referência inexistente, genérica, quebrada ou apontando para tema diferente;
- reprodução de questão real sem identificação e fonte confirmada;
- criação de artigo, prazo, sanção, competência ou exceção legal sem confirmação oficial;
- alteração indevida de questão, comentário ou gabarito já aprovado.

### Rubrica de 100 pontos

| Dimensão | Pontos | Evidência exigida |
|---|---:|---|
| Fidelidade ao edital e às fontes | 15 | Tópicos rastreados ao edital; normas e dados verificáveis; pendências declaradas. |
| Cobertura e profundidade da teoria | 20 | Conceitos, funcionamento, diferenças, aplicação, memorização e pegadinhas suficientes para resolver as questões. |
| Exemplos e prática guiada | 15 | No mínimo dois exemplos resolvidos por tópico importante, com raciocínio, solução e erro comum. |
| Alinhamento entre estudo e questões | 15 | Toda questão aponta para seção real da teoria; nenhuma cobrança órfã; distribuição coerente com o dia. |
| Qualidade das questões | 15 | Enunciados claros, níveis calibrados a partir da matriz inicial 20/20/10 e 8/8/4 ou exceção semântica documentada, distratores plausíveis, variedade e apenas uma resposta correta. |
| Qualidade dos comentários | 15 | Correta justificada; A–D analisadas; conceito, pegadinha, estratégia de resolução e referência precisa. |
| Organização e uso pedagógico | 5 | Cronograma, títulos, tabelas, checklist, revisão ativa e navegação consistentes. |
| **Total** | **100** | **Aprovação mínima: 90 pontos e nenhuma falha eliminatória.** |

Faixas de resultado:

- **90 a 100:** aprovado;
- **80 a 89:** revisão obrigatória antes do uso;
- **abaixo de 80:** refazer os blocos deficientes;
- **qualquer falha eliminatória:** reprovado até a correção, mesmo com nota igual ou superior a 90.

## Estrutura mínima da apostila de estudo

Cada semana possui seis dias. Cada dia deve funcionar quando lido de cima para baixo e seguir esta ordem física, não apenas uma ordem indicada no cronograma:

1. objetivo, resultados esperados e orientação de uso;
2. cronograma dividido em sessões executáveis;
3. Bloco 1 — teoria principal;
4. Bloco 2 — aprofundamento;
5. Bloco 3 — exemplos e prática guiada;
6. Bloco 4 — matéria fixa ou revisão programada;
7. Bloco 5 — Português ou prática discursiva;
8. Bloco 6 — recuperação ativa e caderno de erros, sem conteúdo novo;
9. mini revisão e perguntas de fixação;
10. checklist de domínio;
11. roteiro das questões, com usos e carga distribuída;
12. correção, registro dos erros e fechamento.

O mapa de conexões do dia deve aparecer depois do ensino dos conceitos que representa e antes do fechamento. Em Mermaid ou formato equivalente, deve mostrar fluxo, dependências, decisões e de três a cinco pegadinhas; seus nós devem apontar para seções reais quando o formato permitir.

É proibido posicionar os Blocos 4, 5 e 6 antes dos Blocos 1, 2 e 3. Também é proibido criar, depois da revisão ou do checklist, capítulos como `Reforço de alinhamento`, `Assuntos cobrados` ou outra seção-remendo para ensinar o que as questões exigem. Todo conteúdo resolutivo deve integrar o bloco principal correspondente antes da primeira indicação de resolução.

### Jornada executável e carga de estudo

Cada dia deve ter primeira passagem executável em **duas ou, quando o volume exigir, no máximo três sessões reais de 2h30 a 3h líquidas**, sempre com ponto de parada explícito. A teoria necessária deve permanecer antes da cobrança; se leitura, prática e correção não couberem nesse limite, reduza a quantidade de questões da primeira passagem e leve o saldo do banco para D+2. Não acrescente sessões ao dia nem comprima todo o banco no primeiro contato.

Cada cronograma deve distinguir:

| Etapa | Conteúdo mínimo | Limite de execução |
|---|---|---|
| Sessão A | abertura e início dos Blocos 1–3, na ordem física | 2h30 a 3h líquidas |
| Sessão B | continuação na ordem física; conclusão dos Blocos 1–3 e avanço compatível | 2h30 a 3h líquidas |
| Sessão C, quando necessária | conclusão ou saldo dos Blocos 4–6, mini revisão, amostra fixa de até 10 Essenciais e correção integral | 2h30 a 3h líquidas; última sessão do dia |
| Revisão D+2 | demais Essenciais, corrigidas antes do aprofundamento; depois, retorno às âncoras e Aprofundamento | ciclo futuro próprio de 2h30 a 3h |
| Revisão D+7 | recuperação espaçada e caderno de erros | ciclo futuro próprio de 2h30 a 3h |
| Simulado do ciclo seguinte | itens reservados, sem consulta, e correção posterior | ciclo futuro próprio de 2h30 a 3h |

O cronograma deve contabilizar separadamente leitura, resolução, correção A–D, produção discursiva e caderno de erros. A existência de 50 principais e 20 extras não significa que os 70 itens devam ser resolvidos e corrigidos na primeira passagem.

### Contrato pedagógico dos Blocos 4, 5 e 6

Os Blocos 1, 2 e 3 concentram o tema principal. Os três blocos finais têm funções fixas e não podem ser deslocados para números maiores apenas porque o tema técnico foi dividido em mais etapas:

| Bloco | Função obrigatória | Evidência mínima antes das questões |
|---|---|---|
| 4 | Matéria fixa ou revisão programada | disciplina, origem do conteúdo, conceito, regra, exemplo, aplicação, pegadinha e seção de referência |
| 5 | Português ou prática discursiva | regra linguística ou estrutura textual, modelo comentado e orientação de autocorreção |
| 6 | Revisão ativa e caderno de erros | conteúdo de origem já estudado, pergunta de recuperação, correção do erro e entrega prática |

Regras obrigatórias:

- ensinar antes de cobrar, considerando a ordem real dos dias; citar um tema ou prometer aprofundamento futuro não constitui cobertura;
- não usar como base de uma questão norma, comando, fórmula ou conceito ainda marcado como pendente;
- quando o Bloco 4 recuperar conteúdo anterior, indicar semana, dia e seção de origem;
- não solicitar texto no Bloco 5 antes de apresentar estrutura, modelo ou exemplo suficiente;
- não introduzir conteúdo novo no Bloco 6: ele deve recuperar o dia atual ou dias anteriores e terminar com lista de erros, regras recuperadas, respostas sem consulta ou plano de revisão;
- criar IDs únicos por semana, dia e bloco, como `s2-d3-b4`, evitando links ambíguos para títulos repetidos;
- declarar a faixa de questões principais ou extras associada a cada bloco; se um bloco tiver apenas entrega prática e nenhum item objetivo, registrar isso expressamente.
- manter o Bloco 6 fisicamente depois de todo conteúdo dos Blocos 1–5; ele não pode legitimar questão anterior nem apresentar regra, norma, fórmula ou conceito novo.

Quando a semana abranger Português/discursiva ou quando houver previsão de treino discursivo, inclua tema, proposta, roteiro de estrutura e critérios de autocorreção.

O mapa é diário, não semanal: ele deve servir diretamente à sessão de estudo e ao respectivo caderno de erros.

### Padrão da teoria e dos exemplos resolvidos

Cada tópico importante precisa seguir esta sequência:

1. definição em linguagem clara;
2. funcionamento passo a passo;
3. aplicação prática ou cenário de órgão público;
4. diferença para conceitos semelhantes;
5. como o Instituto Consulplan pode cobrar;
6. no mínimo dois exemplos resolvidos;
7. pegadinhas e erros comuns;
8. síntese do que memorizar;
9. verificação no checklist de domínio.

Cada exemplo resolvido deve conter **situação ou enunciado**, **dados relevantes**, **raciocínio passo a passo**, **resposta final**, **por que a solução funciona** e **erro provável do candidato**. Em SQL, cálculo, lógica, redes ou código, o resultado deve ser conferido. Em legislação, a solução deve apontar a base oficial sem inventar literalidade.

### Rastreabilidade da cobertura

Antes de criar as questões, monte uma matriz por dia com:

| Tópico do edital | Seção da teoria | Exemplos resolvidos | Questões principais | Questões extras | Status |
|---|---|---:|---:|---:|---|
| Tema previsto | Âncora ou título real | Quantidade | Faixa de números | Faixa de números | Coberto/Pendente |

Uma questão só pode entrar na apostila quando houver uma seção correspondente na teoria da própria semana ou uma referência explícita à revisão de semana anterior. As referências devem usar títulos ou âncoras reais e permanecer válidas após qualquer reorganização.

Antes da produção, a leitura da seção indicada deve ser suficiente para resolver o item sem informação externa. Não considere coberta a questão cuja referência apenas mencione o assunto, aponte para um dia futuro ou leve a uma lista de tópicos sem regra, exemplo ou aplicação.

## Super simulado semanal

Ao concluir os seis dias, prepare um arquivo próprio chamado `semana_XX/semana_XX_super_simulado.md`, com **60 questões inéditas**: dez questões integradoras por dia, cobrindo também as revisões fixas quando pertinentes. Use 24 médias, 24 difíceis e 12 muito difíceis como matriz inicial; a auditoria individual pode recalibrar a distribuição, desde que registre cada alteração e não infle o nível. O simulado deve ser resolvido sem consulta, em tempo contínuo, e conter gabarito, nível, comentário individual de A–D, conceito, pegadinha, raciocínio e referência à teoria. Ele é material suplementar e não altera o total oficial de 420 itens da semana.

## Estrutura mínima da apostila de questões

Por dia:

- 50 questões principais e 20 extras;
- quatro alternativas, exclusivamente A–D;
- nível imediatamente abaixo do título de cada questão;
- gabarito de 70 itens e 70 comentários;
- comentário com alternativa correta, análise de A–D, conceito, pegadinha, modo de raciocínio e seção real da apostila;
- distribuição equilibrada de respostas e proibição de enunciados literalmente duplicados.
- categoria operacional junto a cada item: `Essenciais`, `Aprofundamento`, `Revisão` ou `Simulado`;
- referência Markdown precisa junto a cada item, inclusive nas 50 principais, apontando para âncora anterior e suficiente.

Toda questão principal deve informar, no mínimo, sem depender do comentário:

```markdown
**Nível:** Difícil
**Uso:** Aprofundamento
**Referência:** [Dia 3 — JOIN e NULL](semana_XX_estudo.md#sX-d3-joins-null)
```

Toda questão extra vinculada aos Blocos 4, 5 ou 6 deve conservar os metadados completos:

```markdown
**Dia:** 3
**Bloco:** 4 — Legislação CRA/CFA
**Matéria:** Legislação CRA/CFA
**Assunto:** competências do CRA
**Nível:** Difícil
**Uso:** Aprofundamento
**Referência:** [Dia 3 — Bloco 4](semana_XX_estudo.md#sX-d3-b4)
```

O comentário repete o nível, o uso e a mesma referência. A auditoria deve ler individualmente todas as principais e extras; quando uma questão já estiver correta e coberta, basta preservar seu conteúdo e tornar a rastreabilidade precisa.

As extras devem utilizar a `Revisão fixa do Dia X`. Questões de revisão mista devem apontar para um mapa de revisão ou para seções específicas já estudadas.

Antes da primeira questão, inclua um roteiro operacional que distribua o banco completo:

- `Essenciais`: amostra fixa de até 10 na primeira passagem, com correção integral; as demais abrem D+2;
- `Aprofundamento`: somente depois da correção integral das Essenciais que abrem D+2; pode continuar em ciclo próprio antes de D+7;
- `Revisão`: D+7, como recuperação espaçada, não continuação automática da primeira passagem;
- `Simulado`: conjunto reservado para o ciclo seguinte, resolvido sem consulta.

A classificação indica quando usar o item, não sua dificuldade. Uma questão média pode ser reservada para revisão, e uma questão difícil pode ser essencial se avaliar um conceito central.

### Níveis obrigatórios e distribuição

Use exclusivamente `Médio`, `Difícil` e `Muito difícil`, no formato:

```markdown
### Questão N
**Nível: Difícil**
```

O mesmo vale para questões extras, blocos de questões de revisão, simulados e questionários complementares. A classificação também deve aparecer no comentário.

Matriz de planejamento por dia:

| Bloco | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Principais | 20 | 20 | 10 | 50 |
| Extras | 8 | 8 | 4 | 20 |
| Total diário | 28 | 28 | 14 | 70 |

Na semana completa, a matriz planejada corresponde a 168 médias, 168 difíceis e 84 muito difíceis. Para material novo, use como alvo 40%/40%/20%, com arredondamento inteiro que preserve o total e matriz declarada antes da produção: em 20 itens, 8/8/4; em 30, 12/12/6; em 60, 24/24/12.

A matriz não autoriza chamar recuperação literal de “difícil” nem questão direta de “muito difícil”. Se uma auditoria posterior demonstrar nível superestimado ou subestimado, escolha uma destas ações:

1. aprofundar legitimamente o enunciado e o raciocínio, sem aumentar texto ou ambiguidade de forma artificial; ou
2. recalibrar o rótulo no item e no comentário e registrar a distribuição final no relatório.

Quando a recalibração posterior alterar a matriz, a exceção é válida somente se listar as questões afetadas, explicar o motivo e preservar a honestidade pedagógica. Contagem nunca prevalece sobre clareza, resposta única e dificuldade real.

- **Médio:** exige compreensão, comparação ou aplicação direta em cenário, comando, código, norma ou cálculo. Os distratores representam erros comuns, mas um candidato bem preparado consegue eliminá-los sem cadeia longa de inferências.
- **Difícil:** exige interpretação cuidadosa, comparação de conceitos próximos, mais de uma etapa ou identificação de erro sutil. Não pode ser resolvida apenas pelo reconhecimento de palavra-chave.
- **Muito difícil:** integra conceitos ou exige diagnóstico ou cadeia de raciocínio com múltiplas etapas; quando o conteúdo comportar aplicação, apresenta cenário e consequências suficientes e alternativas próximas. A dificuldade decorre do raciocínio exigido, nunca de ambiguidade, informação omitida ou simples aumento do texto.

Antes de aceitar a distribuição final, aplique um **teste de dificuldade substantiva**:

- uma questão `Difícil` deve exigir ao menos duas regras já ensinadas ou duas decisões sucessivas, com distratores que falhem em etapas diferentes;
- uma questão `Muito difícil` deve exigir três ou mais filtros independentes — por exemplo, fonte, vigência, hierarquia, competência, sujeito, conduta, processo e consequência — ou cadeia técnica equivalente;
- associar vários números a seus objetos, reproduzir uma tabela ou alongar o caso sem acrescentar decisão continua sendo tarefa de reconhecimento e não justifica nível elevado;
- se um dia terminar sem nenhuma questão `Muito difícil`, o relatório deve demonstrar por que o conteúdo não permite integração legítima. Quando três ou mais regras ensinadas puderem formar um caso de resposta única, reescreva um conjunto limitado de itens em vez de aceitar dificuldade nula ou apenas trocar rótulos.

### Padrão de elaboração das questões

As questões devem combinar formatos como estudo de caso, assertivas completas, verdadeiro ou falso, alternativa correta/incorreta, comandos reais, interpretação e cálculo. Cada um dos três distratores deve representar erro plausível e identificável de conceito, procedimento ou leitura: inversão de conceitos próximos, sintaxe verossímil, generalização indevida, causa e consequência trocadas, resposta parcialmente correta ou verdade que não atende ao comando.

As quatro alternativas devem permanecer no mesmo domínio, com paralelismo gramatical, especificidade e extensão comparáveis. São proibidas opções artificiais, absurdas, de assunto alheio, engraçadas, repetidas ou que revelem a resposta pelo tamanho, tom ou redação. Para a auditoria, conte os caracteres úteis depois de remover o rótulo A–D e a marcação Markdown. Gere um alerta se a correta tiver mais de 1,30 vez o comprimento do maior distrator ou menos de 0,70 vez o comprimento do menor. O alerta exige revisão e justificativa, mas não reprova automaticamente o item; nunca alongue distratores apenas para equilibrar caracteres.

O gabarito deve variar de modo natural entre A, B, C e D e ficar equilibrado dentro de cada faixa de dificuldade, com diferença máxima de uma ocorrência quando a quantidade permitir. Não aceite três ou mais respostas iguais consecutivas. Sinalize para revisão qualquer motivo de duas a quatro letras que se repita três vezes seguidas; uma alternância curta e ocasional, isoladamente, não constitui falha. Depois de qualquer permutação, mova junto o texto da alternativa e sua explicação, atualize a tabela de respostas e confira `questão = gabarito = comentário`.

Questões de comando negativo, como “assinale a incorreta”, devem ter o comando destacado e comentário compatível com a lógica negativa. Inclua uma observação explícita no comentário para lembrar que o gabarito corresponde à afirmação errada.

### Padrão obrigatório dos comentários

Cada comentário deve funcionar como uma pequena aula. Em comandos positivos, siga este núcleo canônico:

```markdown
- **Alternativa correta:** C.
- **Nível:** Difícil.
- **A) está errada:** explicação ligada exatamente ao texto de A.
- **B) está errada:** explicação ligada exatamente ao texto de B.
- **C) está correta:** regra aplicada ao enunciado, sem repetir a alternativa.
- **D) está errada:** explicação ligada exatamente ao texto de D.
- **Conceito cobrado:** nome preciso do conteúdo.
- **Pegadinha usada:** erro comum explorado.
- **Como pensar para acertar:** sequência curta e reutilizável.
- **Referência à apostila de estudo:** seção ou âncora real.
```

A análise da alternativa correta já deve explicar por que ela resolve o item; não crie um campo redundante que apenas repita sua redação. As explicações de A–D precisam acompanhar as alternativas quando elas forem reordenadas.

Em comandos negativos, como “assinale a INCORRETA”, use a polaridade do enunciado e explicite que o gabarito identifica a afirmação errada:

```markdown
- **Gabarito:** C (a afirmação incorreta).
- **Nível:** Difícil.
- **A) está correta:** explicação ligada exatamente ao texto de A.
- **B) está correta:** explicação ligada exatamente ao texto de B.
- **C) está incorreta:** erro que torna C o gabarito.
- **D) está correta:** explicação ligada exatamente ao texto de D.
- **Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.
- **Conceito cobrado:** nome preciso do conteúdo.
- **Pegadinha usada:** erro comum explorado.
- **Como pensar para acertar:** sequência curta e reutilizável.
- **Referência à apostila de estudo:** seção ou âncora real.
```

Em questões com cálculo, SQL, código, CIDR ou lógica, o comentário deve mostrar as etapas necessárias para reproduzir o resultado. Em legislação, deve distinguir texto confirmado, interpretação e hipótese prática.

### Auditoria semântica de cada questão

Além da contagem automática, todas as questões devem ser lidas com este checklist:

- o enunciado é suficiente, claro e não entrega a resposta;
- existe somente uma melhor alternativa;
- o gabarito foi resolvido independentemente do comentário;
- as quatro alternativas são distintas e os três distratores são pertinentes e plausíveis;
- o comentário responde exatamente ao comando da questão;
- A, B, C e D foram analisadas sem contradição;
- cada explicação ainda descreve a alternativa da mesma letra depois de qualquer reordenação;
- o conceito aparece na teoria indicada;
- o nível aparece logo abaixo do título, repete-se no comentário e corresponde ao esforço exigido;
- a correta não se destaca indevidamente por extensão, especificidade, tom ou construção gramatical;
- não há repetição literal, duplicata aproximada ou variação superficial de outra questão;
- não há três letras iguais consecutivas nem motivo de duas a quatro letras repetido três vezes sem revisão e justificativa;
- a linguagem está adequada ao nível e ao estilo do Instituto Consulplan.

### Auditoria pedagógica de cobertura de principais e extras

Antes de editar, classifique individualmente todas as questões principais e extras do lote. A auditoria começa em modo somente leitura, antes de reorganizar a teoria, para que o diagnóstico não seja apagado pela correção:

- `Coberta`: teoria anterior e suficiente, referência válida e bloco adequado;
- `Parcialmente coberta`: há base anterior, mas falta regra, exemplo, aplicação ou detalhe indispensável;
- `Não coberta`: a resposta depende de conteúdo ausente;
- `Cobrada antes do momento correto`: a teoria aparece somente em dia ou etapa posterior;
- `Inadequada para o bloco`: o item não cumpre a função pedagógica do bloco;
- `Ambígua`: mais de uma leitura ou resposta permanece defensável.
- `Nível superestimado`: o rótulo exige cadeia de raciocínio maior do que o item realmente apresenta;
- `Nível subestimado`: o item exige integração ou inferências acima do rótulo atribuído.

Para cada item que não esteja `Coberto`, escolha uma ação rastreável: complementar teoria suficiente antes da cobrança; mover para depois do ensino; reformular; substituir; ou remover quando estiver fora do planejamento. Uma frase isolada adicionada apenas para legitimar o gabarito não corrige falta de cobertura.

Registre a auditoria nesta tabela:

| Semana | Dia | Faixa | Matéria | Questões verificadas | Problemas encontrados | Correções |
|---|---:|---|---|---:|---:|---:|
| Semana X | Dia X | Principais 1–50 e Extras 1–20 | disciplina | 70 | quantidade | quantidade |

## Auditoria antes de concluir uma semana

Confirme:

- 300 principais, 120 extras, 420 gabaritos e 420 comentários;
- distribuição de níveis planejada ou exceção pós-auditoria justificada, sempre com nível idêntico no item e no comentário;
- 60 questões, 60 gabaritos e 60 comentários no super simulado, com matriz padrão de 24 médias, 24 difíceis e 12 muito difíceis, salvo exceção previamente justificada;
- seis revisões fixas, seis blocos de fixação e seis mapas de cobrança;
- Blocos 4, 5 e 6 identificados em todos os dias, sem conteúdo novo no Bloco 6 e com entrega prática registrada;
- zero alternativa E, opção A–D duplicada, numeração ausente, duplicidade literal ou referência inexistente;
- todas as referências presentes no arquivo de estudo;
- nenhuma referência aponta para conteúdo futuro, superficial ou apenas pendente;
- todas as principais contêm Nível, Uso e Referência; todas as extras dos Blocos 4–6 contêm Dia, Bloco, Matéria, Assunto, Nível, Uso e Referência; migração pendente só é aceita quando estiver explicitamente fora do lote;
- todas as 420 questões aprovadas na auditoria semântica individual;
- gabaritos equilibrados, sem três letras iguais seguidas e sem motivos repetidos não justificados, com item, tabela e comentário sincronizados;
- nenhum viés indevido de comprimento, tom ou especificidade na alternativa correta;
- comandos negativos acompanhados de observação pedagógica;
- exemplos importantes com raciocínio e resposta verificados;
- matriz de rastreabilidade sem questão órfã ou tópico cobrado sem teoria;
- ordem física validada: Blocos 1–3, Blocos 4–6, revisão, checklist, questões, correção e fechamento;
- nenhuma seção-remendo posterior à revisão, ao checklist ou às questões;
- carga de cada sessão executável em aproximadamente 3 horas líquidas e banco completo distribuído por uso;
- rubrica preenchida com pelo menos 90/100 e zero critério eliminatório;
- diff sem conflito, placeholder ou artefato de edição e blocos fora do escopo preservados;
- README e Plano Mestre atualizados somente depois da validação.

### Relatório de aceite da semana

Ao finalizar, registre no fim da apostila de estudo ou em relatório de revisão:

| Item | Resultado |
|---|---|
| Nota da rubrica | X/100 |
| Critérios eliminatórios encontrados | 0 ou lista de correções |
| Questões principais | 300 |
| Questões extras | 120 |
| Médio/Difícil/Muito difícil — banco (420) | distribuição final e eventual justificativa de recalibração |
| Gabaritos | 420 |
| Comentários completos | 420 |
| Referências válidas | 420 |
| Super simulado | 60 |
| Médio/Difícil/Muito difícil — super | distribuição final auditada; matriz inicial: 24/24/12 |
| Alternativas E | 0 |
| Questões órfãs de teoria | 0 |
| Gabaritos divergentes | 0 |
| Alertas de motivos repetidos no gabarito | 0 ou todos revisados e justificados |
| Alertas de comprimento/alinhamento | 0 ou todos revisados |
| Questões principais e extras cobertas/parciais/não cobertas/antecipadas/inadequadas/ambíguas | X/X/X/X/X/X |
| Questões com nível superestimado/subestimado após a correção | 0/0 |
| Conteúdo novo introduzido no Bloco 6 | 0 |
| Referências a conteúdo futuro ou superficial | 0 |
| Sessões acima da carga planejada | 0 ou lista justificada |
| Itens revisados/novos/substituídos/removidos | X/X/X/X |
| Blocos preservados fora do escopo | lista |
| Status final | Aprovado/Revisão obrigatória/Reprovado |

O relatório não substitui a revisão. Ele registra as evidências usadas para declarar a semana pronta.

## Execução incremental, preservação e publicação

Semanas extensas não devem ser criadas ou revisadas simultaneamente em trilhas diferentes. Trabalhe em uma única semana e em um único eixo por vez, usando os seguintes pontos de controle:

1. **Delimitar:** registrar arquivos, dias e blocos autorizados; congelar explicitamente tudo o que estiver fora do escopo.
2. **Criar baseline:** conferir branch, status e diff; quando houver material aprovado, guardar hash ou comparar o bloco antes e depois.
3. **Produzir por lote:** limitar cada lote a no máximo dois dias, cerca de 140 questões, ou a um componente isolado como teoria, parecer ou super simulado.
4. **Auditar o lote:** validar contagens, níveis, opções, gabaritos, comentários, fontes, duplicatas, comprimento e preservação antes de iniciar o próximo.
5. **Publicar checkpoint:** criar commit atômico apenas com os arquivos do lote, enviar ao GitHub e integrar à `main` quando autorizado.
6. **Sincronizar:** confirmar `main` local e remota no mesmo commit e diretório limpo; o commit publicado deve permitir reversão objetiva.
7. **Prosseguir:** somente começar o lote seguinte depois que o anterior estiver validado e publicado.

### Plano transitório de migração — julho de 2026

Neste ciclo de migração, a ordem é: padrões semanais; Semana 2 de Analista em lotes D1–D2, D3–D4 e D5–D6; depois Direito, também em lotes de até dois dias. Não editar os bancos de Analista e Direito ao mesmo tempo. Este roteiro deixa de reger o trabalho quando os materiais legados indicados abaixo forem migrados.

## Aplicação às semanas existentes

- **Semana 1:** a estrutura de 300 principais, 120 extras e 420 comentários está completa. As 80 extras dos Blocos 4–6 nos Dias 3–6 permanecem aceitas no recorte da auditoria anterior. As 100 principais dos Dias 3–4 receberam auditoria semântica individual, teoria anterior suficiente, uso operacional e referência precisa; seus níveis foram recalibrados com exceção documentada no relatório do lote. Os Dias 1–2 permaneceram intactos e ainda não possuem classificação de nível; as 100 principais dos Dias 5–6 continuam fora deste aceite. Por isso, a semana conserva **conformidade parcial** fora dos recortes já auditados.
- **Semana 2:** a estrutura de 300 principais, 120 extras, 420 gabaritos, 420 comentários e 420 referências foi migrada e auditada integralmente. As 300 principais e as 120 extras receberam leitura semântica individual, níveis recalibrados, usos e referências; 144 principais e 65 extras foram reformuladas, quatro principais receberam aprofundamento multifiltro e o super simulado foi auditado com dez itens por dia. A distribuição final e as evidências estão em `../semana_02/relatorio_aceite.md`. O lote está **aprovado para execução**, com execução do candidato pendente.
- **Semana 3:** a estrutura de 300 principais, 120 extras, 420 comentários e super simulado de 60 itens foi produzida e auditada integralmente. Os 420 itens foram relidos em três lotes independentes; dois gabaritos incorretos foram corrigidos antes do aceite, níveis e distratores foram recalibrados e a dependência de produto recebeu delimitação. A distribuição final e as evidências estão em `../semana_03/relatorio_aceite.md`. O lote está **aprovado para execução**, com execução do candidato pendente.
- **Semana 4:** a estrutura de 300 principais, 120 extras, 420 comentários e super simulado de 60 itens foi produzida e auditada integralmente. Os 420 itens foram relidos em lotes independentes, o super recebeu segunda auditoria cega, as dificuldades foram recalibradas sem cotas e nenhuma resposta semântica precisou ser trocada. As posições A–D só foram permutadas depois do congelamento semântico, com alternativa, análise e tabela movidas juntas. A cobertura dos itens 13–17, a jornada, a discursiva e as questões oficiais separadas estão registradas em `../semana_04/relatorio_aceite.md`. O lote está **aprovado para execução**, com execução do candidato pendente.
