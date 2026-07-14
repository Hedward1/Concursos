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
- questão sem nível válido imediatamente abaixo do título ou bloco fora da matriz aplicável; as matrizes diárias 20/20/10 e 8/8/4 são obrigatórias, e exceções pedagógicas previamente declaradas e justificadas restringem-se a conjuntos complementares e super simulados;
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
| Qualidade das questões | 15 | Enunciados claros, níveis calibrados, distribuição 20/20/10 e 8/8/4, distratores plausíveis, variedade e apenas uma resposta correta. |
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

Ao concluir os seis dias, prepare um arquivo próprio chamado `semana_XX/semana_XX_super_simulado.md`, com **60 questões inéditas**: dez questões integradoras por dia, cobrindo também as revisões fixas quando pertinentes. Salvo justificativa registrada no plano da semana, distribua 24 questões médias, 24 difíceis e 12 muito difíceis. O simulado deve ser resolvido sem consulta, em tempo contínuo, e conter gabarito, nível, comentário individual de A–D, conceito, pegadinha, raciocínio e referência à teoria. Ele é material suplementar e não altera o total oficial de 420 itens da semana.

## Estrutura mínima da apostila de questões

Por dia:

- 50 questões principais e 20 extras;
- quatro alternativas, exclusivamente A–D;
- nível imediatamente abaixo do título de cada questão;
- gabarito de 70 itens e 70 comentários;
- comentário com alternativa correta, análise de A–D, conceito, pegadinha, modo de raciocínio e seção real da apostila;
- distribuição equilibrada de respostas e proibição de enunciados literalmente duplicados.

As extras devem utilizar a `Revisão fixa do Dia X`. Questões de revisão mista devem apontar para um mapa de revisão ou para seções específicas já estudadas.

### Níveis obrigatórios e distribuição

Use exclusivamente `Médio`, `Difícil` e `Muito difícil`, no formato:

```markdown
### Questão N
**Nível: Difícil**
```

O mesmo vale para questões extras, blocos de questões de revisão, simulados e questionários complementares. A classificação também deve aparecer no comentário.

Distribuição obrigatória por dia:

| Bloco | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Principais | 20 | 20 | 10 | 50 |
| Extras | 8 | 8 | 4 | 20 |
| Total diário | 28 | 28 | 14 | 70 |

Na semana completa, isso corresponde a 168 médias, 168 difíceis e 84 muito difíceis. A matriz padrão dos conjuntos adicionais é 40%/40%/20%, com arredondamento inteiro que preserve o total e matriz declarada antes da produção: em 20 itens, 8/8/4; em 30, 12/12/6; em 60, 24/24/12. Uma exceção pedagógica só é válida quando registrada e justificada previamente no plano do conjunto.

- **Médio:** exige compreensão, comparação ou aplicação direta em cenário, comando, código, norma ou cálculo. Os distratores representam erros comuns, mas um candidato bem preparado consegue eliminá-los sem cadeia longa de inferências.
- **Difícil:** exige interpretação cuidadosa, comparação de conceitos próximos, mais de uma etapa ou identificação de erro sutil. Não pode ser resolvida apenas pelo reconhecimento de palavra-chave.
- **Muito difícil:** integra conceitos ou exige diagnóstico ou cadeia de raciocínio com múltiplas etapas; quando o conteúdo comportar aplicação, apresenta cenário e consequências suficientes e alternativas próximas. A dificuldade decorre do raciocínio exigido, nunca de ambiguidade, informação omitida ou simples aumento do texto.

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

## Auditoria antes de concluir uma semana

Confirme:

- 300 principais, 120 extras, 420 gabaritos e 420 comentários;
- 168 questões médias, 168 difíceis e 84 muito difíceis, com nível idêntico no item e no comentário;
- 60 questões, 60 gabaritos e 60 comentários no super simulado, com matriz padrão de 24 médias, 24 difíceis e 12 muito difíceis, salvo exceção previamente justificada;
- seis revisões fixas, seis blocos de fixação e seis mapas de cobrança;
- zero alternativa E, opção A–D duplicada, numeração ausente, duplicidade literal ou referência inexistente;
- todas as referências presentes no arquivo de estudo;
- todas as 420 questões aprovadas na auditoria semântica individual;
- gabaritos equilibrados, sem três letras iguais seguidas e sem motivos repetidos não justificados, com item, tabela e comentário sincronizados;
- nenhum viés indevido de comprimento, tom ou especificidade na alternativa correta;
- comandos negativos acompanhados de observação pedagógica;
- exemplos importantes com raciocínio e resposta verificados;
- matriz de rastreabilidade sem questão órfã ou tópico cobrado sem teoria;
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
| Médio/Difícil/Muito difícil — banco (420) | 168/168/84 |
| Gabaritos | 420 |
| Comentários completos | 420 |
| Referências válidas | 420 |
| Super simulado | 60 |
| Médio/Difícil/Muito difícil — super | matriz aplicada (padrão: 24/24/12) |
| Alternativas E | 0 |
| Questões órfãs de teoria | 0 |
| Gabaritos divergentes | 0 |
| Alertas de motivos repetidos no gabarito | 0 ou todos revisados e justificados |
| Alertas de comprimento/alinhamento | 0 ou todos revisados |
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

- **Semana 1:** a estrutura de 300 principais, 120 extras e 420 comentários está completa. Os Dias 3–6 foram revisados quanto a níveis, distratores, comentários, gabaritos e calibração cognitiva; somam 112 médias, 112 difíceis e 56 muito difíceis. Os Dias 1–2 foram preservados e ainda não possuem classificação de nível. A precisão das referências teóricas também permanece pendente, sobretudo no Dia 3. Portanto, a Semana 1 possui **conformidade parcial** e não está integralmente aceita pelo novo padrão.
- **Semana 2:** a estrutura de 300 principais, 120 extras, 420 gabaritos, 420 comentários e 420 referências está presente, mas os itens ainda não possuem os três níveis deste padrão e os comentários usam formato legado. O Dia 4 mistura hierarquias de título nos comentários, e uma checagem amostral já encontrou divergência na Questão 1 do Dia 1 entre o cabeçalho do comentário (`B`) e o gabarito/análise (`D`). A migração ocorrerá em três lotes de dois dias, cada um auditado e publicado separadamente. Referências existentes não dispensam a auditoria semântica, a recalibração dos níveis e o preenchimento da rubrica.
