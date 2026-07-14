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
8. **Aprovar:** somente considerar a semana concluída quando não houver falha eliminatória e a nota da rubrica for igual ou superior a 90 pontos.

### Critérios eliminatórios

A ocorrência de qualquer item abaixo reprova o material, independentemente da nota:

- conteúdo incompatível com o edital oficial vigente ou norma apresentada como certa sem fonte confirmada;
- tema cobrado nas questões sem sustentação suficiente na apostila de estudo ou em revisão anterior identificada;
- gabarito tecnicamente incorreto, ambíguo ou incompatível com o comentário;
- questão sem quatro alternativas A–D, com alternativa E ou sem uma única melhor resposta;
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
| Qualidade das questões | 15 | Enunciados claros, distratores plausíveis, dificuldade média ou alta, variedade e apenas uma resposta correta. |
| Qualidade dos comentários | 15 | Correta justificada; A–D analisadas; conceito, pegadinha, estratégia de resolução e referência precisa. |
| Organização e uso pedagógico | 5 | Cronograma, títulos, tabelas, checklist, revisão ativa e navegação consistentes. |
| **Total** | **100** | **Aprovação mínima: 90 pontos e nenhuma falha eliminatória.** |

Faixas de resultado:

- **90 a 100:** aprovado;
- **80 a 89:** revisão obrigatória antes do uso;
- **abaixo de 80:** refazer os blocos deficientes;
- **qualquer falha eliminatória:** reprovado até a correção, mesmo com nota igual ou superior a 90.

## Estrutura mínima da apostila de estudo

Cada semana possui seis dias. Cada dia deve conter:

1. objetivo, resultados esperados, relevância para a prova e cronograma de 6h líquidas;
2. teoria com regras, exemplos, diferenças entre conceitos próximos e pegadinhas;
3. prática guiada, checklist de domínio, caderno de erros e fontes;
4. `## Revisão fixa do Dia X`, identificando disciplina, assunto, origem do conteúdo e teoria que sustenta as 20 extras;
5. `## 5 perguntas de fixação`, com recuperação ativa do tema principal;
6. `## Assuntos que serão cobrados na Apostila de Questões`, ligando a teoria às questões principais e extras.
7. `## Mapa de conexões do Dia`, em Mermaid e acompanhado de leitura ativa: deve mostrar fluxo, dependências, decisões e de três a cinco pegadinhas. Os nós devem apontar para seções reais da teoria quando o formato do mapa permitir.

O cronograma não pode apenas nomear os blocos recorrentes. Logo após a tabela de 6h, inclua `## Conteúdo dos blocos de revisão e consolidação`, com subseções para os Blocos 4, 5 e 6. Cada uma deve trazer o resumo teórico, regras, exemplo e pegadinha necessários para estudar o item daquele dia sem procurar outro capítulo.

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

## Super simulado semanal

Ao concluir os seis dias, prepare um arquivo próprio chamado `semana_XX/semana_XX_super_simulado.md`, com **60 questões inéditas** e de dificuldade alta: dez questões integradoras por dia, cobrindo também as revisões fixas quando pertinentes. O simulado deve ser resolvido sem consulta, em tempo contínuo, e conter gabarito, comentário individual de A–D, conceito, pegadinha, raciocínio e referência à teoria. Ele é material suplementar e não altera o total oficial de 420 itens da semana.

## Estrutura mínima da apostila de questões

Por dia:

- 50 questões principais e 20 extras;
- quatro alternativas, exclusivamente A–D;
- gabarito de 70 itens e 70 comentários;
- comentário com alternativa correta, análise de A–D, conceito, pegadinha, modo de raciocínio e seção real da apostila;
- distribuição equilibrada de respostas e proibição de enunciados literalmente duplicados.

As extras devem utilizar a `Revisão fixa do Dia X`. Questões de revisão mista devem apontar para um mapa de revisão ou para seções específicas já estudadas.

### Padrão de elaboração das questões

As questões devem combinar formatos como estudo de caso, assertivas completas, verdadeiro ou falso, alternativa correta/incorreta, comandos reais, interpretação e cálculo. Os distratores precisam representar erros plausíveis de conceito, procedimento ou leitura. São proibidas alternativas artificiais, absurdas, de assunto alheio ou que revelem a resposta pelo tamanho e pela redação.

O gabarito deve variar de modo natural entre A, B, C e D. A distribuição não precisa ser matematicamente idêntica, mas não pode formar padrão previsível. Questões de comando negativo, como “assinale a incorreta”, devem ter o comando destacado e comentário compatível com a lógica negativa.

### Padrão obrigatório dos comentários

Cada comentário deve funcionar como uma pequena aula e conter:

1. **Gabarito:** letra e resposta correta.
2. **Por que está correta:** regra aplicada ao enunciado, sem mera repetição da alternativa.
3. **Análise de A, B, C e D:** explicação individual de por que cada opção está correta ou errada.
4. **Conceito cobrado:** nome preciso do conteúdo avaliado.
5. **Pegadinha:** erro de leitura ou conceito explorado pelos distratores.
6. **Como pensar para acertar:** sequência curta e reutilizável de raciocínio.
7. **Referência à apostila de estudo:** seção ou âncora real que ensina o conteúdo.

Nos comandos “assinale a incorreta”, a alternativa do gabarito deve ser descrita explicitamente como incorreta e as outras três como corretas. Em questões com cálculo, SQL, código, CIDR ou lógica, o comentário deve mostrar as etapas necessárias para reproduzir o resultado. Em legislação, deve distinguir texto confirmado, interpretação e hipótese prática.

### Auditoria semântica de cada questão

Além da contagem automática, todas as questões devem ser lidas com este checklist:

- o enunciado é suficiente, claro e não entrega a resposta;
- existe somente uma melhor alternativa;
- o gabarito foi resolvido independentemente do comentário;
- os quatro distratores são pertinentes e plausíveis;
- o comentário responde exatamente ao comando da questão;
- A, B, C e D foram analisadas sem contradição;
- o conceito aparece na teoria indicada;
- a dificuldade declarada corresponde ao esforço exigido;
- não há repetição literal ou variação superficial de outra questão;
- a linguagem está adequada ao nível e ao estilo do Instituto Consulplan.

## Auditoria antes de concluir uma semana

Confirme:

- 300 principais, 120 extras, 420 gabaritos e 420 comentários;
- seis revisões fixas, seis blocos de fixação e seis mapas de cobrança;
- zero alternativa E, numeração ausente, duplicidade literal ou referência inexistente;
- todas as referências presentes no arquivo de estudo;
- todas as 420 questões aprovadas na auditoria semântica individual;
- exemplos importantes com raciocínio e resposta verificados;
- matriz de rastreabilidade sem questão órfã ou tópico cobrado sem teoria;
- rubrica preenchida com pelo menos 90/100 e zero critério eliminatório;
- README e Plano Mestre atualizados somente depois da validação.

### Relatório de aceite da semana

Ao finalizar, registre no fim da apostila de estudo ou em relatório de revisão:

| Item | Resultado |
|---|---|
| Nota da rubrica | X/100 |
| Critérios eliminatórios encontrados | 0 ou lista de correções |
| Questões principais | 300 |
| Questões extras | 120 |
| Comentários completos | 420 |
| Referências válidas | 420 |
| Alternativas E | 0 |
| Questões órfãs de teoria | 0 |
| Gabaritos divergentes | 0 |
| Status final | Aprovado/Revisão obrigatória/Reprovado |

O relatório não substitui a revisão. Ele registra as evidências usadas para declarar a semana pronta.

## Aplicação às semanas existentes

- **Semana 1:** a estrutura de 300 principais, 120 extras e 420 comentários está completa, mas ainda exige reavaliação pelo novo modelo. Os comentários principais usam referência genérica ao dia e os comentários das extras não possuem referência à seção teórica. Até a correção e a auditoria semântica, a semana permanece **pendente de aceite no novo padrão**.
- **Semana 2:** a estrutura de 300 principais, 120 extras e 420 comentários está completa. A checagem inicial encontrou referências para a teoria em todos os comentários e nenhum destino de link ausente. A aprovação definitiva ainda depende da auditoria semântica individual e do preenchimento da rubrica.
