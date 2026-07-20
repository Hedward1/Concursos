# Dia 5 — Testes, qualidade, manutenção e processos de desenvolvimento

As 70 questões são autorais, calibradas pelo perfil documentado do Instituto Consulplan e ambientadas, quando pertinente, em situações públicas. Nenhum item reproduz questão real. Na primeira passagem, resolva seis dos dez itens classificados como Essenciais e avance até dez somente se houver correção A–D integral.

## Questões principais — S4D5Q201 a S4D5Q250

### S4D5Q201 — Erro, defeito e falha

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Um analista interpreta incorretamente a regra de prazo, registra-a errada na especificação e, ao executar o sistema, observa data final indevida. A sequência conceitual correta é:

A) erro humano → defeito → falha.

B) falha → defeito → erro humano.

C) defeito → falha → erro humano.

D) erro humano → falha → defeito.

### S4D5Q202 — Revisão sem execução

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

A equipe lê requisitos, identifica uma ambiguidade e a corrige antes de existir código executável. Essa atividade é:

A) teste dinâmico de sistema, porque o requisito representa o sistema.

B) teste de aceitação, porque houve participação da área usuária.

C) regressão, porque o texto anterior foi substituído.

D) teste estático, pois examina produto de trabalho sem executar software.

### S4D5Q203 — Nível de componente

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Uma função de cálculo é exercitada isoladamente com dependências substituídas por dublês. O foco está na lógica local. Trata-se de teste de:

A) componente.

B) integração.

C) sistema.

D) aceitação.

### S4D5Q204 — Contrato entre serviços

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Dois serviços funcionam isoladamente, mas divergem no formato do campo `dataPagamento`. Qual nível ataca diretamente esse risco?

A) Componente.

B) Aceitação.

C) Integração.

D) Manutenção.

### S4D5Q205 — Sistema e aceitação

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

O portal completo passa pelos fluxos ponta a ponta. Depois, representantes verificam se ele sustenta o procedimento real e o critério contratual. Assinale a leitura correta.

A) Ambos são testes de componente porque cada tela é um componente.

B) O primeiro foco é teste de sistema; o segundo, teste de aceitação.

C) Ambos são aceitação porque o sistema está completo.

D) O primeiro é regressão e o segundo é confirmação.

### S4D5Q206 — Correção e entorno

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Após corrigir a falha de cálculo, a equipe repete o caso que falhou e testa módulos consumidores. Esses dois objetivos são, respectivamente:

A) regressão e confirmação.

B) aceitação e sistema.

C) verificação e inspeção.

D) confirmação e regressão.

### S4D5Q207 — Função e atributo

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Verificar se o sistema calcula a taxa correta e medir seu tempo sob carga correspondem, respectivamente, a testes:

A) de componente e de aceitação.

B) estático e dinâmico.

C) funcional e não funcional.

D) de confirmação e regressão.

### S4D5Q208 — Fronteira de desconto

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

A regra concede desconto para idade igual ou superior a 65. Qual conjunto é mais aderente à análise de valor-limite?

A) 64, 65 e 66.

B) 1, 30 e 100.

C) 65, 70 e 80.

D) 0, 64 e 100.

### S4D5Q209 — Cobertura de instruções

**Nível:** Difícil

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Uma suíte executou 100% das instruções de um módulo. É correto concluir que:

A) todas as combinações de entrada foram testadas.

B) todas as decisões tiveram resultados verdadeiro e falso.

C) o módulo está validado pelos usuários.

D) ela não prova cobertura de decisões nem ausência de defeitos.

### S4D5Q210 — Fonte do esperado

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Antes de executar um caso de cálculo, a equipe usa regra aprovada e cálculo independente para definir o resultado correto. Essa fonte de decisão é o:

A) oráculo de teste.

B) resultado observado.

C) caso de teste.

D) critério de saída.

### S4D5Q211 — Combinações de regras

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Benefício depende de três condições binárias e cada combinação determina uma ação. Qual técnica organiza melhor condições e ações?

A) Cobertura de instruções.

B) Ataque de erros.

C) Teste de instalação.

D) Tabela de decisão.

### S4D5Q212 — Ciclo de um pedido

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Um pedido pode estar em rascunho, enviado, em análise, deferido ou indeferido; certos eventos são proibidos em alguns estados. A técnica mais direta é:

A) teste de transição de estados.

B) partição por navegador.

C) cobertura de instruções.

D) teste de volume.

### S4D5Q213 — Priorização por risco

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Há pouco tempo: um módulo crítico mudou muito e falha historicamente; outro, informativo, não mudou. A priorização tecnicamente justificável é:

A) priorizar o módulo menor, usando tempo de execução como medida suficiente de risco.

B) dividir o tempo igualmente, pois ambos integram a mesma entrega e merecem igual cobertura.

C) aprofundar primeiro o módulo crítico por probabilidade e impacto, registrando a cobertura residual e sua decisão.

D) testar apenas as linhas alteradas do módulo crítico, sem examinar consumidores que permaneceram estáveis.

### S4D5Q214 — Critério de saída

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Qual opção constitui critério de saída observável para uma campanha?

A) Encerrar quando especialistas não propuserem novos cenários após uma rodada de exploração.

B) Cumprir a data final, ainda que riscos prioritários permaneçam sem evidência suficiente.

C) Defeitos críticos tratados, cobertura acordada atingida e risco residual formalmente aceito.

D) Executar todos os casos, mesmo com resultados sem análise e defeitos críticos ainda abertos.

### S4D5Q215 — Independência sob restrições

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Em projeto crítico, autores revisam primeiro, equipe distinta testa depois, especialistas do negócio validam e todos compartilham evidências. Qual avaliação preserva três filtros: diversidade de perspectiva, colaboração e limites da independência?

A) A combinação amplia a detecção sem garantir imparcialidade absoluta; papéis e conflitos devem ser explícitos.

B) Somente equipe externa pode testar; qualquer contato com autores invalida a independência.

C) Autores não podem testar nada, pois conhecer o código torna todo resultado inútil.

D) Participação do negócio transforma todos os testes em aceitação e garante qualidade.

### S4D5Q216 — Caso reproduzível

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Um registro diz apenas “testar login; deve funcionar”. Para torná-lo caso de teste auditável, é essencial acrescentar:

A) precondições, entradas/passos, resultado esperado e critério de comparação.

B) nome do testador, duração estimada e ferramenta usada na execução.

C) captura da tela final e classificação da severidade antes de executar.

D) código-fonte do módulo e histórico completo de todas as alterações.

### S4D5Q217 — Fluxos de caso de uso

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Um caso de uso possui fluxo principal e alternativa para documento inválido. O conjunto mínimo coerente de testes inclui:

A) apenas o fluxo principal, porque alternativas não fazem parte do objetivo.

B) somente cobertura de classes, sem entradas de negócio.

C) um cenário principal e outro da alternativa, ambos com resultados esperados.

D) um teste de desempenho, pois documento inválido reduz velocidade.

### S4D5Q218 — Exploração com rastreabilidade

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Durante sessão exploratória, o testador formula hipóteses, aprende e adapta próximos passos. Em contexto auditável, a melhor prática é:

A) evitar qualquer registro para preservar espontaneidade.

B) registrar missão, percurso, dados, evidências e riscos.

C) executar somente roteiro fixo, pois adaptação não é teste.

D) substituir todos os testes especificados por exploração.

### S4D5Q219 — Ambiguidade precoce

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

A frase “o sistema deve responder rapidamente” é encontrada em revisão. Qual encaminhamento é mais adequado?

A) aceitar e deixar o testador decidir depois o que é rápido.

B) traduzir automaticamente como média inferior a um segundo.

C) negociar condição, carga, medida e limite verificáveis no requisito.

D) classificar como falha do software já observada.

### S4D5Q220 — Plano de teste por camadas

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

Uma mudança altera regra local, contrato entre serviços e fluxo completo usado pelo cidadão. Qual plano é mais coerente?

A) fazer apenas aceitação, porque ela contém implicitamente todos os defeitos técnicos.

B) fazer apenas componente, pois todo defeito começa no código.

C) cobrir componente, integração e sistema, além de aceitação se houver risco de prontidão.

D) escolher nível pela disponibilidade do ambiente, sem olhar riscos.

### S4D5Q221 — Qualidade além da função

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Um sistema calcula corretamente, mas expõe dados a perfil indevido. A conclusão adequada é:

A) o produto tem qualidade plena porque a regra foi calculada.

B) a função correta não compensa a falha de segurança do produto.

C) o problema é somente de processo, nunca do produto.

D) segurança só pode ser avaliada depois da manutenção.

### S4D5Q222 — Desempenho verificável

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Qual formulação substitui melhor “a consulta deve ser rápida”?

A) A consulta deve ficar perceptivelmente mais rápida que a versão anterior.

B) Sob carga definida, 95% das consultas devem responder em até dois segundos.

C) O tempo médio deve ser considerado satisfatório pelos usuários envolvidos.

D) Nenhuma consulta poderá ultrapassar o tempo ideal em qualquer cenário de uso.

### S4D5Q223 — Produto, processo e evidência

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Uma equipe adota revisão obrigatória, mede defeitos escapados e testa cada incremento. Ainda assim, uma entrega específica falha no aceite. Qual alternativa preserva produto, processo e evidência?

A) A revisão obrigatória demonstra qualidade do processo; a falha isolada deve ser tratada apenas no produto.

B) Os testes do incremento bastam como evidência da entrega; o aceite negativo indica apenas divergência operacional.

C) A falha de aceite invalida o processo adotado, que deve ser substituído antes de corrigir a entrega.

D) O processo reduz riscos, mas a entrega requer evidência própria; a falha deve corrigir o produto e realimentar o processo.

### S4D5Q224 — Garantia e controle

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Auditar se revisões previstas ocorreram e executar testes no incremento são, respectivamente, atividades mais próximas de:

A) controle e garantia, nessa ordem.

B) validação do produto e manutenção corretiva.

C) garantia da qualidade e controle da qualidade.

D) aceitação operacional e teste de integração.

### S4D5Q225 — Especificação certa, necessidade errada

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

O produto segue integralmente a especificação, mas servidores não conseguem concluir o procedimento real. O diagnóstico é:

A) a validação passou porque o código está conforme.

B) o produto foi verificado, mas não validado para a necessidade.

C) não existe problema de qualidade sem defeito de código.

D) todo requisito não funcional deve ser removido.

### S4D5Q226 — Indicador sem contexto

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Duas equipes registram 20 defeitos cada. Para comparar esse indicador de forma mais defensável, é necessário considerar:

A) os nomes dos testadores, a ferramenta usada e a ordem dos registros.

B) uma meta de zero defeito, sem distinguir gravidade, contexto ou oportunidade.

C) apenas o prazo de entrega, a quantidade de commits e o número de reuniões.

D) tamanho e complexidade do produto, exposição, severidade e fase ou oportunidade de detecção.

### S4D5Q227 — Custos de qualidade

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Treinamento preventivo, inspeção de entrega e correção após uso representam, nessa ordem:

A) falha interna, prevenção e avaliação.

B) avaliação, falha interna e prevenção.

C) prevenção, avaliação e falha externa.

D) manutenção adaptativa, integração e qualidade de processo.

### S4D5Q228 — Teste e qualidade

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Assinale a afirmação correta sobre teste e qualidade.

A) Teste revela defeitos e informa decisões, mas não constrói sozinho a qualidade.

B) Uma suíte aprovada demonstra que o produto está livre de defeitos relevantes.

C) A equipe de testes responde sozinha pela qualidade entregue ao usuário.

D) Práticas preventivas tornam desnecessária a execução de testes no produto.

### S4D5Q229 — Segurança mensurável

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Um requisito diz apenas “o portal deve ser seguro”. Qual refinamento é mais útil?

A) Adotar uma ferramenta de varredura, registrar sua versão e executá-la antes da entrega.

B) Exigir ausência de incidentes por um ano, sem delimitar recursos, ameaças ou perfis.

C) Submeter o portal a aceite final de segurança, deixando os critérios para a equipe executora.

D) Definir recursos, papéis, acessos permitidos/negados, registros e critérios de teste no contexto.

### S4D5Q230 — Confiabilidade e interação

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

O portal recupera-se após falha em cinco minutos, mas 40% dos usuários abandonam o formulário por mensagens incompreensíveis. A leitura correta é:

A) a recuperação prova qualidade global e invalida o abandono.

B) há evidência de recuperação, mas também falha na capacidade de interação.

C) abandono é sempre defeito corretivo de banco de dados.

D) somente validação técnica de componente pode analisar ambos.

### S4D5Q231 — Três atributos, três evidências

**Nível:** Muito difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Nova versão deve responder sob carga, impedir acesso indevido e permitir alteração localizada. Qual plano preserva três atributos, critérios e evidências?

A) Executar apenas fluxo funcional feliz e inferir os três atributos.

B) Medir carga/percentil, testar autorização por papéis e analisar impacto da mudança.

C) Medir linhas de código e concluir desempenho, segurança e flexibilidade.

D) Fazer aceite informal e registrar que usuários gostaram.

### S4D5Q232 — Decisão de liberação

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

Testes funcionais passaram; desempenho excede o limite e há risco conhecido aceito apenas verbalmente. Qual ação é mais consistente?

A) Liberar porque as funções passaram e registrar o desempenho como risco operacional posterior.

B) Redefinir o limite usando o resultado observado e atualizar a especificação antes do relatório.

C) Cancelar a liberação, pois todo risco residual impede decisão de aceite ou mitigação.

D) Registrar o desvio e submeter correção, mitigação ou aceite formal à autoridade antes da liberação.

### S4D5Q233 — Falha pós-entrega

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Após entrega, detecta-se cálculo incorreto e altera-se o módulo para restaurar a regra. A manutenção é:

A) corretiva.

B) adaptativa.

C) perfectiva.

D) preventiva.

### S4D5Q234 — Mudança externa

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Serviço governamental altera contrato obrigatório; o sistema interno funcionava, mas precisa adaptar-se. Trata-se predominantemente de manutenção:

A) corretiva.

B) preventiva.

C) adaptativa.

D) perfectiva.

### S4D5Q235 — Melhoria e prevenção

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Um módulo lento é otimizado para atender demanda e outro, sem falha conhecida, é refatorado para reduzir fragilidade antes de mudança prevista. As classificações dominantes são:

A) corretiva e adaptativa.

B) preventiva e corretiva.

C) perfectiva e preventiva.

D) adaptativa e perfectiva.

### S4D5Q236 — Análise de impacto

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Antes de mudar regra compartilhada, qual conjunto constitui análise de impacto adequada?

A) Alterar a primeira ocorrência encontrada e aguardar reclamações.

B) Rastrear dependências técnicas e de negócio, testes e operação afetados.

C) Contar linhas modificadas e usar o tamanho do `diff` como alcance funcional.

D) Repetir o caso solicitado e presumir que consumidores permanecem inalterados.

### S4D5Q237 — Baseline controlada

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Sobre baseline e controle de configuração, assinale a correta.

A) Baseline é referência congelada que nenhuma mudança autorizada pode substituir.

B) Baseline é referência aprovada, alterável por decisão, versionamento e rastreabilidade controlados.

C) Controle de configuração equivale ao uso de Git, mesmo sem identificação ou auditoria.

D) Toda alteração exige o mesmo rito, sem considerar impacto ou criticidade.

### S4D5Q238 — Mudança emergencial

**Nível:** Muito difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Falha crítica exige correção urgente. Qual abordagem preserva urgência, risco, configuração e recuperação?

A) Aplicar rito emergencial: registrar, autorizar, versionar, testar conforme o risco, preparar reversão, monitorar e revisar.

B) Corrigir diretamente em produção, registrar depois e dispensar versão separada para reduzir a indisponibilidade.

C) Aguardar todo o rito comum, sem decisão excepcional, embora a avaliação indique dano crescente.

D) Liberar após confirmação local, sem regressão, reversão ou monitoramento, porque a mudança é pequena.

### S4D5Q239 — Liberação e regressão

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Uma correção passou no caso original. Antes da liberação, o passo adicional mais justificado é:

A) liberar sem nova evidência, pois confirmação basta.

B) executar regressão proporcional e preparar reversão e monitoramento.

C) reclassificar a correção como perfectiva para reduzir controles.

D) criar nova baseline sem associar requisitos e testes.

### S4D5Q240 — Motivo dominante em mudança mista

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

Uma lei externa muda cálculo; ao adaptar, a equipe também melhora legibilidade e corrige defeito antigo. Como classificar a solicitação principal?

A) Adaptativa, registrando separadamente os outros motivos.

B) Somente corretiva, porque qualquer defeito antigo domina todo pacote.

C) Somente perfectiva, porque o código ficou melhor.

D) Impossível classificar uma mudança com mais de um efeito.

### S4D5Q241 — Sequencial sob risco e data

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Projeto tem regra estável, auditoria formal e data fixa, mas integração inédita concentra risco técnico. Qual decisão evita tanto dogma sequencial quanto improviso?

A) Manter marcos e baselines, antecipar prova da integração e iterar conforme o risco.

B) Aplicar cascata rígida e testar integração apenas ao final, pois a regra é estável.

C) Eliminar documentação e marcos porque qualquer iteração é ágil.

D) Construir tudo como protótipo descartável e convertê-lo automaticamente em produção.

### S4D5Q242 — Entrega por incrementos

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Disponibilizar primeiro consulta, depois protocolo e por fim relatórios, cada parte integrada e utilizável, caracteriza desenvolvimento:

A) puramente prototípico.

B) somente sequencial.

C) corretivo.

D) incremental.

### S4D5Q243 — Iteração

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Em cada ciclo, a equipe revisa requisitos, arquitetura, implementação e testes à luz do feedback. Isso representa:

A) ausência de planejamento.

B) cascata obrigatoriamente sem retorno.

C) manutenção apenas pós-entrega.

D) desenvolvimento iterativo/evolucionário.

### S4D5Q244 — Protótipo e produção

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Uma interface navegável com dados fictícios valida fluxo; direção quer publicá-la porque “já funciona”. Qual resposta considera objetivo, arquitetura e qualidade?

A) Publicar imediatamente, pois validação com usuário substitui todos os testes.

B) Usar aprendizados, mas só tratar o artefato como produto após engenharia e testes.

C) Descartar também todo aprendizado, porque protótipos não geram requisito.

D) Tratá-la como incremento produtivo apenas mudando o nome do artefato.

### S4D5Q245 — Espiral guiada por risco

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Qual descrição melhor caracteriza o modelo espiral?

A) Sequência linear em que riscos só são registrados depois da entrega.

B) Prototipação sem planejamento ou compromisso de produto.

C) Entregas diárias obrigatórias com escopo sempre variável.

D) Ciclos analisam riscos, desenvolvem e planejam a passagem seguinte.

### S4D5Q246 — RAD e reúso sob filtros

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Um órgão tem prazo curto, módulos delimitáveis e usuários disponíveis, mas pretende reutilizar componente sem avaliar licença, suporte e compatibilidade. Qual decisão é coerente?

A) Reúso elimina análise e teste porque o componente já existe.

B) RAD admite `timeboxing`; reúso exige licença, integração, suporte e testes.

C) RAD exige construir tudo do zero para evitar dependência.

D) Prazo curto torna irrelevantes arquitetura e participação do usuário.

### S4D5Q247 — Concepção

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Na fase de concepção, a ênfase recai em:

A) completar toda funcionalidade e otimização.

B) migrar usuários e obter aceite operacional.

C) detalhar todas as classes antes de avaliar valor.

D) visão, escopo, viabilidade e riscos iniciais.

### S4D5Q248 — Elaboração

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Qual resultado indica que a elaboração cumpriu sua finalidade?

A) Todo manual de usuário foi entregue e treinamento concluído.

B) Nenhum requisito poderá mudar depois.

C) Riscos arquiteturais e requisitos críticos foram tratados; o plano foi refinado.

D) Somente telas foram prototipadas, sem atacar integração crítica.

### S4D5Q249 — Construção e transição

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

O produto precisa completar capacidades, estabilizar incrementos, migrar dados, treinar usuários e obter aceite. A alocação de ênfase correta é:

A) elaboração completa tudo; concepção realiza migração.

B) transição apenas copia arquivos; treinamento pertence à concepção.

C) construção completa o produto; transição o implanta e busca aceite.

D) teste só ocorre na transição, após todo código.

### S4D5Q250 — Processo adaptado

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Equipe escolhe processo para sistema público com risco técnico moderado, feedback frequente e obrigação de rastreabilidade. Qual orientação é mais defensável?

A) Combinar ciclos verificáveis, rastreabilidade proporcional e gestão de riscos.

B) Escolher um rótulo conhecido e aplicar todas as práticas sem adaptação.

C) Eliminar controle de mudanças para responder rapidamente.

D) Adiar testes até o marco final para preservar independência.

## Questões extras — Dia 5

#### Extra Dia 5.1 — Fonte da profissão

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Hierarquia de fontes

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Ao identificar a base legal que disciplina a profissão, o primeiro filtro deve recair sobre:

A) qualquer resolução posterior, apenas por ser mais nova.

B) o regimento interno regional, em qualquer matéria.

C) uma notícia institucional sem vínculo normativo.

D) a lei de regência.

#### Extra Dia 5.2 — Regulamentação

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Lei, decreto e regimento

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

O ato destinado a regulamentar a lei não deve ser confundido com:

A) a própria regulamentação executiva da lei.

B) regimento interno do conselho regional.

C) norma situada abaixo da lei.

D) ato que deve respeitar a lei.

#### Extra Dia 5.3 — Âmbito nacional e regional

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Competência CFA/CRA

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Em caso que combina orientação nacional e fiscalização no Paraná, qual leitura é adequada?

A) CFA atua nacionalmente; CRA-PR, em sua jurisdição, sem romper a unidade do sistema.

B) CRA-PR pode afastar norma nacional sempre que agir dentro de sua autonomia administrativa.

C) CFA deve executar diligências regionais sempre que a orientação nacional estiver envolvida.

D) O órgão regional apenas recebe ordens e não exerce atribuição própria na jurisdição.

#### Extra Dia 5.4 — Caso ético

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Enquadramento ético

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Antes de concluir sobre consequência ética, a análise deve identificar:

A) sujeito, conduta, contexto e regra aplicável.

B) apenas a repercussão pública do caso.

C) somente o cargo do denunciante.

D) a sanção mais severa disponível.

#### Extra Dia 5.5 — Publicidade e sigilo

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Publicidade e proteção

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Um pedido de informação alcança documento com trecho público e dado protegido. A solução mais coerente é:

A) publicar integralmente porque todo ato institucional é público.

B) negar todo o documento porque existe um dado protegido.

C) deixar cada servidor decidir sem critério ou registro.

D) fornecer a parte acessível e proteger o trecho restrito, com fundamento.

#### Extra Dia 5.6 — Objeto e fonte

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Roteiro de leitura institucional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Qual roteiro reduz erro ao escolher a fonte aplicável?

A) objeto → fonte → sujeito → território → competência → limite.

B) data → popularidade → tamanho do ato → opinião.

C) sanção → notícia → órgão → objeto.

D) território → qualquer ato local → dispensa da lei.

#### Extra Dia 5.7 — Autonomia regional

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Autonomia e unidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

A autonomia do conselho regional significa que ele:

A) pode afastar lei nacional por decisão administrativa.

B) atua em sua jurisdição dentro das normas superiores.

C) não precisa prestar contas nem motivar atos.

D) possui competência nacional exclusiva.

#### Extra Dia 5.8 — Ato posterior

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Hierarquia e temporalidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Uma resolução posterior diverge da lei. A mera posterioridade permite afastar a lei?

A) Sim, porque todo ato mais novo revoga o anterior.

B) Sim, se o ato tiver número maior.

C) Não; prevalecem hierarquia, competência e compatibilidade.

D) Depende apenas da preferência do aplicador.

#### Extra Dia 5.9 — Decisão institucional

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Aplicação institucional

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Servidor encontra conflito aparente entre orientação geral, ato regional e dado protegido. Qual conduta é mais defensável?

A) Identificar hierarquia, competência e proteção; fundamentar e encaminhar a dúvida.

B) Aplicar automaticamente o ato regional por estar mais próximo do caso.

C) Divulgar tudo para evitar alegação de omissão.

D) Paralisar indefinidamente sem identificar o ponto de conflito.

#### Extra Dia 5.10 — Competência no Paraná

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Jurisdição regional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

Em registro e fiscalização referentes à jurisdição paranaense, o órgão regional deve ser considerado:

A) mero destinatário sem atribuição própria.

B) substituto integral do órgão nacional em toda matéria.

C) competente dentro das atribuições e limites aplicáveis.

D) livre de qualquer norma geral.

#### Extra Dia 5.11 — Reescrita com três filtros

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Referência e paralelismo

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Assinale a reescrita que preserva sentido, paralelismo e referente em “A equipe revisou o requisito e a planilha, depois encaminhou-a à direção”.

A) A equipe revisou o requisito e a planilha, por isso encaminhou-lhe à direção.

B) Depois de revisar o requisito e a planilha, a equipe encaminhou a planilha à direção.

C) Depois da revisão do requisito, da planilha e encaminhar à direção, a equipe concluiu.

D) A planilha, depois de revisar a equipe e o requisito, foi encaminhada.

#### Extra Dia 5.12 — Conector concessivo

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Conector concessivo e relação lógica

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Qual período expressa concessão de modo correto?

A) O teste passou, portanto o risco aumentou, sem relação apresentada.

B) Porque o teste passou, contudo a equipe executou o teste.

C) Embora o teste tenha passado, o risco residual precisa ser avaliado.

D) O teste passou, logo embora o risco seja avaliado.

#### Extra Dia 5.13 — Sujeito e verbo

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Concordância

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Assinale a frase correta.

A) Falta evidências para encerrar os testes.

B) Faltam evidências para encerrar os testes.

C) As evidências, permite encerrar os testes.

D) Devem haver evidências suficientes.

#### Extra Dia 5.14 — Escopo da negação

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Negação e quantificador

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

A frase “Nem todos os casos foram aprovados” significa que:

A) nenhum caso foi aprovado.

B) todos os casos foram aprovados.

C) exatamente um caso foi reprovado.

D) há caso reprovado, mas pode haver aprovados.

#### Extra Dia 5.15 — Precisão e pontuação

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Reescrita integral

**Nível:** Muito difícil

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Qual opção preserva concordância, pontuação, relação causal e modalização adequada?

A) Os requisitos, estava ambíguo, portanto revisou-se eles e eliminou todo retrabalho.

B) Embora estavam ambíguos os requisitos porque a equipe revisou, nunca haverá retrabalho.

C) Como os requisitos estavam ambíguos, a equipe os revisou; a medida pode reduzir retrabalho.

D) A equipe revisou os requisitos, os quais portanto elimina os retrabalhos.

#### Extra Dia 5.16 — Paralelismo verbal

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Paralelismo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Qual enumeração mantém paralelismo?

A) levantamento de requisitos, modelar processos e que se meçam resultados.

B) que se levantem requisitos, modelar e a medição.

C) levantar requisitos, a modelagem e resultados medidos.

D) levantar requisitos, modelar processos, testar e medir resultados.

#### Extra Dia 5.17 — Referente inequívoco

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Referência pronominal

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Em “O gerente informou o analista de que seu relatório estava incompleto”, a melhor reescrita, se o relatório é do analista, é:

A) O gerente informou o analista, cujo seu relatório estava incompleto.

B) O gerente informou-lhe de que seu relatório estava incompleto.

C) O gerente informou que o analista estava incompleto em seu relatório.

D) O gerente informou ao analista que o relatório deste estava incompleto.

#### Extra Dia 5.18 — Relações lógicas combinadas

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Coesão lógica

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Qual período mantém causa, contraste e conclusão sem contradição?

A) Os testes reduziram incertezas, porque restou risco; portanto, a redução não ocorreu.

B) Embora restou risco, logo a autoridade adiou, entretanto porque testou.

C) Os testes reduziram incertezas; porém, restou risco e, por isso, a liberação foi adiada.

D) A autoridade adiou a liberação, contudo por isso não havia risco.

#### Extra Dia 5.19 — Reescrita técnica completa

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Modalização e causalidade

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

A frase “A ferramenta sempre garante qualidade, e isso prova que nunca há falhas” deve ser reescrita sem perder o tema, mas corrigindo absolutos e relação causal. Assinale a melhor opção.

A) A ferramenta costuma garantir qualidade e, quando configurada, praticamente elimina falhas.

B) A simples adoção da ferramenta assegura a execução correta do processo e, por isso, reduz falhas.

C) Ferramentas apoiam a qualidade, logo resultados favoráveis confirmam a ausência de falhas.

D) A ferramenta pode apoiar controles, mas resultados dependem do uso e de evidências; não provam ausência de falhas.

#### Extra Dia 5.20 — Período integrado

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Reescrita integrada

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

Escolha a versão que preserva agente, cronologia, paralelismo e conclusão proporcional.

A) A equipe identificou o defeito, avaliou o impacto, corrigiu o módulo e executou a regressão; assim, reuniu evidência para decidir a liberação.

B) Depois de identificar o defeito, o impacto foi avaliado e o módulo corrigiu a equipe; assim, a regressão garantiu a liberação.

C) A equipe identificou e corrigiu o defeito; como avaliou o impacto depois da liberação, a regressão tornou-se desnecessária.

D) Identificado o defeito, a equipe avaliou o impacto e corrigiu o módulo; logo, a qualidade total ficou comprovada sem regressão.

## Gabarito — Dia 5

### Principais

| S4D5Q201 | S4D5Q202 | S4D5Q203 | S4D5Q204 | S4D5Q205 | S4D5Q206 | S4D5Q207 | S4D5Q208 | S4D5Q209 | S4D5Q210 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | D | A | C | B | D | C | A | D | A |

| S4D5Q211 | S4D5Q212 | S4D5Q213 | S4D5Q214 | S4D5Q215 | S4D5Q216 | S4D5Q217 | S4D5Q218 | S4D5Q219 | S4D5Q220 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| D | A | C | C | A | A | C | B | C | C |

| S4D5Q221 | S4D5Q222 | S4D5Q223 | S4D5Q224 | S4D5Q225 | S4D5Q226 | S4D5Q227 | S4D5Q228 | S4D5Q229 | S4D5Q230 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| B | B | D | C | B | D | C | A | D | B |

| S4D5Q231 | S4D5Q232 | S4D5Q233 | S4D5Q234 | S4D5Q235 | S4D5Q236 | S4D5Q237 | S4D5Q238 | S4D5Q239 | S4D5Q240 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| B | D | A | C | C | B | B | A | B | A |

| S4D5Q241 | S4D5Q242 | S4D5Q243 | S4D5Q244 | S4D5Q245 | S4D5Q246 | S4D5Q247 | S4D5Q248 | S4D5Q249 | S4D5Q250 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | D | D | B | D | B | D | C | C | A |

### Extras

| 5.1 | 5.2 | 5.3 | 5.4 | 5.5 | 5.6 | 5.7 | 5.8 | 5.9 | 5.10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| D | B | A | A | D | A | B | C | A | C |

| 5.11 | 5.12 | 5.13 | 5.14 | 5.15 | 5.16 | 5.17 | 5.18 | 5.19 | 5.20 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| B | C | B | D | C | D | D | C | D | A |

## Comentários — Dia 5

### Comentário S4D5Q201

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A decisão humana introduz um problema no artefato, depois manifestado na execução.
- **B)** Incorreta. A falha é observada na execução, não a origem cronológica do caso.
- **C)** Incorreta. O erro humano ocorreu antes do defeito inserido.
- **D)** Incorreta. O defeito já existe no artefato antes da manifestação.

**Conceito:** Erro, defeito e falha.

**Pegadinha:** Tratar os três termos como sinônimos.

**Como pensar:** Siga origem humana, artefato afetado e comportamento observado.


### Comentário S4D5Q202

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Teste dinâmico exige executar o item de teste.
- **B)** Incorreta. Participação do usuário não define sozinha o nível.
- **C)** Incorreta. Regressão procura efeitos adversos de mudança, normalmente com base de testes.
- **D)** Correta. A revisão encontra defeito no documento sem execução.

**Conceito:** Teste estático.

**Pegadinha:** Negar caráter de teste à revisão.

**Como pensar:** Pergunte se houve execução e qual artefato foi examinado.

### Comentário S4D5Q203

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O objeto é uma unidade isolável e sua lógica local.
- **B)** Incorreta. As interfaces reais entre unidades não são o objeto principal.
- **C)** Incorreta. O sistema completo não está sendo exercitado.
- **D)** Incorreta. Não se avalia prontidão para o uso do negócio.

**Conceito:** Nível de componente.

**Pegadinha:** Definir nível pelo uso de dublê ou pelo executor.

**Como pensar:** Identifique o objeto e o risco dominante.

### Comentário S4D5Q204

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Cada serviço isolado já funciona; o risco está entre eles.
- **B)** Incorreta. Aceitação pode perceber o efeito, mas não é o foco direto do contrato.
- **C)** Correta. O defeito está no contrato e na interação entre serviços.
- **D)** Incorreta. Manutenção é atividade de mudança pós-entrega, não nível de teste.

**Conceito:** Teste de integração.

**Pegadinha:** Chamar qualquer teste de API de sistema.

**Como pensar:** Localize a fronteira onde o defeito nasce.

### Comentário S4D5Q205

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Tela não redefine o objeto global exercitado.
- **B)** Correta. Sistema avalia o conjunto diante de requisitos; aceitação avalia prontidão e necessidade.
- **C)** Incorreta. Completude do produto não transforma toda execução em aceitação.
- **D)** Incorreta. Esses termos descrevem objetivos de teste de mudança, não os níveis narrados.

**Conceito:** Sistema e aceitação.

**Pegadinha:** Usar ambiente ou completude como único critério.

**Como pensar:** Separe avaliação técnica do sistema e prontidão para o uso.

### Comentário S4D5Q206

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A ordem dos objetivos foi invertida.
- **B)** Incorreta. Níveis não substituem os objetivos de mudança.
- **C)** Incorreta. Ambas as ações descritas são execuções dinâmicas.
- **D)** Correta. O primeiro verifica a correção; o segundo busca efeitos laterais.

**Conceito:** Confirmação e regressão.

**Pegadinha:** Chamar todo reteste de regressão.

**Como pensar:** Pergunte: caso original ou áreas potencialmente afetadas?

### Comentário S4D5Q207

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A descrição fornece tipos, não níveis.
- **B)** Incorreta. Ambos podem ser dinâmicos; o contraste é de objetivo.
- **C)** Correta. Cálculo avalia função; tempo sob carga avalia atributo de desempenho.
- **D)** Incorreta. Nenhuma correção prévia foi informada.

**Conceito:** Tipos funcional e não funcional.

**Pegadinha:** Trocar tipo por nível.

**Como pensar:** Nomeie primeiro o que está sendo avaliado.

### Comentário S4D5Q208

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. São a fronteira e seus vizinhos imediatos.
- **B)** Incorreta. Espalha valores sem concentrar a mudança de comportamento.
- **C)** Incorreta. Examina só a classe com desconto.
- **D)** Incorreta. Inclui extremos, mas omite o primeiro valor elegível.

**Conceito:** Análise de valor-limite.

**Pegadinha:** Testar apenas o valor descrito na regra.

**Como pensar:** Procure o ponto de mudança e os dois lados.

### Comentário S4D5Q209

**Nível:** Difícil

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Instruções podem ser cobertas por poucas combinações.
- **B)** Incorreta. Cobertura de instruções não implica cobertura completa de decisões.
- **C)** Incorreta. Cobertura interna não demonstra adequação ao uso.
- **D)** Correta. Cobertura é evidência limitada, não prova de correção total.

**Conceito:** Cobertura estrutural.

**Pegadinha:** Transformar porcentagem em garantia absoluta.

**Como pensar:** Pergunte o que a métrica mede e o que deixa de medir.


### Comentário S4D5Q210

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Ele permite comparar observado e esperado.
- **B)** Incorreta. É a saída obtida, que será confrontada com o esperado.
- **C)** Incorreta. Organiza a execução, mas não é necessariamente a fonte do resultado correto.
- **D)** Incorreta. Critério de saída decide encerramento do processo de teste.

**Conceito:** Oráculo de teste e resultado esperado.

**Pegadinha:** Confundir mecanismo de execução com fonte de verdade.

**Como pensar:** Localize quem determina o esperado antes da execução.

### Comentário S4D5Q211

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A estrutura interna não organiza a regra de negócio.
- **B)** Incorreta. Experiência pode ajudar, mas não explicita sistematicamente combinações.
- **C)** Incorreta. Instalação é tipo/contexto, não técnica combinatória.
- **D)** Correta. Ela representa combinações de condições e consequências.

**Conceito:** Tabela de decisão.

**Pegadinha:** Escolher técnica estrutural para regra combinatória.

**Como pensar:** Conte condições, combinações e ações.

### Comentário S4D5Q212

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Estados, eventos e transições permitidas/proibidas formam a base.
- **B)** Incorreta. Navegador não é o eixo do comportamento descrito.
- **C)** Incorreta. Pode complementar, mas não deriva o ciclo de negócio.
- **D)** Incorreta. Volume não examina permissões de transição.

**Conceito:** Transição de estados.

**Pegadinha:** Olhar somente o fluxo feliz.

**Como pensar:** Modele estado atual, evento, guarda e próximo estado.

### Comentário S4D5Q213

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Velocidade isolada não atende à exposição.
- **B)** Incorreta. Igualdade de tempo ignora exposição e criticidade distintas.
- **C)** Correta. Risco orienta profundidade e ordem com base em exposição.
- **D)** Incorreta. Alterações podem afetar consumidores estáveis fora das linhas editadas.

**Conceito:** Teste baseado em risco.

**Pegadinha:** Usar urgência sem impacto ou impacto sem probabilidade.

**Como pensar:** Compare exposição e registre risco residual.


### Comentário S4D5Q214

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. É subjetivo e não reproduzível.
- **B)** Incorreta. Data pode restringir, mas não substitui avaliação do risco.
- **C)** Correta. Condições verificáveis e decisão explícita permitem encerrar.
- **D)** Incorreta. Execução sem avaliação não demonstra atendimento.

**Conceito:** Critério de saída.

**Pegadinha:** Confundir limite de agenda com evidência de qualidade.

**Como pensar:** Procure condição mensurável e responsável pela aceitação do risco.

### Comentário S4D5Q215

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Há perspectivas diferentes, colaboração e reconhecimento do limite.
- **B)** Incorreta. Independência admite graus e não exige isolamento total.
- **C)** Incorreta. Teste do autor é útil, embora tenha vieses próprios.
- **D)** Incorreta. Participação não redefine todo nível nem oferece garantia absoluta.

**Conceito:** Independência de teste.

**Pegadinha:** Converter independência em isolamento ou garantia.

**Como pensar:** Avalie graus, perspectivas, comunicação e risco de viés.

### Comentário S4D5Q216

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Esses elementos permitem execução, decisão e reprodução.
- **B)** Incorreta. Autoria e duração não definem o esperado.
- **C)** Incorreta. Captura e severidade não definem condições, passos nem resultado esperado.
- **D)** Incorreta. Código integral não substitui condições e resultados.

**Conceito:** Caso de teste completo.

**Pegadinha:** Confundir anotação de execução com especificação do teste.

**Como pensar:** Pergunte se outra pessoa consegue repetir e decidir.


### Comentário S4D5Q217

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Alternativas pertencem ao comportamento especificado.
- **B)** Incorreta. Estrutura não substitui os cenários do caso de uso.
- **C)** Correta. Os fluxos declarados precisam de evidência correspondente.
- **D)** Incorreta. O risco descrito é funcional, não de desempenho.

**Conceito:** Testes derivados de caso de uso.

**Pegadinha:** Ignorar fluxos alternativos.

**Como pensar:** Transforme cada caminho relevante em condição e resultado.


### Comentário S4D5Q218

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Ausência de evidência impede reprodução e aprendizado institucional.
- **B)** Correta. Exploração pode ser disciplinada e rastreável.
- **C)** Incorreta. Adaptação é característica da exploração.
- **D)** Incorreta. Técnicas são complementares e dependem do risco.

**Conceito:** Teste exploratório.

**Pegadinha:** Opor exploração e disciplina.

**Como pensar:** Preserve liberdade de investigação e evidência mínima.


### Comentário S4D5Q219

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Isso cria oráculo subjetivo e tardio.
- **B)** Incorreta. O limite não foi acordado e média pode ocultar cauda.
- **C)** Correta. A ambiguidade deve virar critério testável antes da implementação.
- **D)** Incorreta. Ainda não houve execução nem comportamento observado.

**Conceito:** Revisão de requisito.

**Pegadinha:** Inventar métrica para fechar a revisão.

**Como pensar:** Converta adjetivo em condição, medida e limiar acordados.


### Comentário S4D5Q220

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Testes

**Referência:** [Testes: fundamento, níveis, tipos e técnicas](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Aceitação não substitui diagnóstico e cobertura nos níveis anteriores.
- **B)** Incorreta. Contratos e fluxo completo têm riscos próprios.
- **C)** Correta. Cada nível cobre um objeto, e aceitação responde à necessidade de uso.
- **D)** Incorreta. Ambiente restringe execução, mas não define o objetivo.

**Conceito:** Estratégia multinível.

**Pegadinha:** Procurar um único nível que substitua os demais.

**Como pensar:** Mapeie risco local, interface, ponta a ponta e prontidão.


### Comentário S4D5Q221

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Ignora requisito de segurança.
- **B)** Correta. Atendimento funcional não encerra avaliação de qualidade.
- **C)** Incorreta. Exposição indevida é propriedade observável do produto.
- **D)** Incorreta. Pode e deve ser especificada e testada no ciclo.

**Conceito:** Qualidade multidimensional.

**Pegadinha:** Reduzir qualidade a correção funcional.

**Como pensar:** Liste necessidades além da função e suas evidências.


### Comentário S4D5Q222

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não define base, medida nem limiar.
- **B)** Correta. Declara carga, população, medida e limite.
- **C)** Incorreta. Média e “bom” permanecem vagos.
- **D)** Incorreta. Absoluto sem contexto é impraticável e não mensurável como escrito.

**Conceito:** Requisito de desempenho.

**Pegadinha:** Usar adjetivo ou absoluto no lugar de critério.

**Como pensar:** Exija carga, população, métrica, limite e ambiente.


### Comentário S4D5Q223

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Restringe o aprendizado ao produto e impede que a falha realimente o processo.
- **B)** Incorreta. O teste não invalida evidência contrária produzida no aceite.
- **C)** Incorreta. Falha deve gerar análise e melhoria, não conclusão totalizante.
- **D)** Correta. Separa capacidade do processo, resultado do produto e melhoria.

**Conceito:** Qualidade de produto e processo.

**Pegadinha:** Inferir produto perfeito de processo disciplinado.

**Como pensar:** Procure evidência do item e aprendizado do processo.


### Comentário S4D5Q224

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Inverte processo e produto.
- **B)** Incorreta. Não há mudança pós-entrega nem adequação ao uso descrita.
- **C)** Correta. A primeira examina confiança no processo; a segunda avalia o produto.
- **D)** Incorreta. Esses são níveis/contextos de teste, não o contraste solicitado.

**Conceito:** Garantia e controle da qualidade.

**Pegadinha:** Usar “qualidade” como bloco único.

**Como pensar:** Pergunte se a evidência incide sobre processo ou produto.


### Comentário S4D5Q225

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Conformidade com especificação caracteriza verificação.
- **B)** Correta. Conformidade documental e utilidade são perguntas distintas.
- **C)** Incorreta. Requisito ou solução inadequados também comprometem qualidade.
- **D)** Incorreta. A dificuldade de interação deve ser especificada e avaliada.

**Conceito:** Verificação e validação.

**Pegadinha:** Considerar documento aprovado como verdade suficiente.

**Como pensar:** Compare construir conforme descrição e resolver a necessidade.


### Comentário S4D5Q226

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Contagem é útil quando contextualizada.
- **B)** Incorreta. A meta absoluta não fornece denominador nem torna as equipes comparáveis.
- **C)** Incorreta. Prazo, commits e reuniões não substituem exposição, severidade e fase de detecção.
- **D)** Correta. O denominador e o contexto mudam a interpretação.

**Conceito:** Métricas contextualizadas.

**Pegadinha:** Comparar totais sem denominador.

**Como pensar:** Pergunte objetivo, fonte, fórmula, contexto, limiar e ação.


### Comentário S4D5Q227

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Treinamento não é falha; correção após uso não é avaliação.
- **B)** Incorreta. A sequência troca todas as categorias.
- **C)** Correta. Cada custo corresponde à finalidade e ao momento.
- **D)** Incorreta. Mistura categorias de outros eixos.

**Conceito:** Custo da qualidade.

**Pegadinha:** Classificar pelo nome da atividade sem olhar finalidade/momento.

**Como pensar:** Localize prevenção, detecção e onde a falha apareceu.

### Comentário S4D5Q228

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Teste é parte da estratégia, não sinônimo do resultado inteiro.
- **B)** Incorreta. Testes cobrem condições finitas e não provam ausência total.
- **C)** Incorreta. Ela é construída e avaliada por vários papéis.
- **D)** Incorreta. Prevenção e detecção são complementares.

**Conceito:** Papel do teste.

**Pegadinha:** Transformar teste em garantia absoluta.

**Como pensar:** Pergunte que risco e evidência o teste cobre.


### Comentário S4D5Q229

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ferramenta não define ameaça, acesso nem evidência.
- **B)** Incorreta. Ausência de incidente observado não delimita ativos, ameaças, perfis nem controles.
- **C)** Incorreta. Segurança tardia aumenta risco e não cria oráculo.
- **D)** Correta. Transforma desejo em regras e evidências observáveis.

**Conceito:** Requisito de segurança.

**Pegadinha:** Confundir produto comprado com propriedade verificada.

**Como pensar:** Defina ativo, ator, ação, condição, evidência e limite.


### Comentário S4D5Q230

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Evidência de confiabilidade não resolve interação.
- **B)** Correta. Um atributo não compensa automaticamente o outro.
- **C)** Incorreta. A causa não foi demonstrada e o atributo é outro.
- **D)** Incorreta. Recuperação e uso exigem níveis e métodos adequados ao risco.

**Conceito:** Atributos de qualidade.

**Pegadinha:** Usar um indicador positivo como nota global.

**Como pensar:** Associe cada evidência ao atributo que realmente mede.


### Comentário S4D5Q231

**Nível:** Muito difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Fluxo feliz não mede carga, acesso negado nem manutenibilidade.
- **B)** Correta. Carga/percentil evidencia desempenho; papéis testam segurança; impacto examina manutenibilidade.
- **C)** Incorreta. Uma métrica estrutural isolada não prova esses atributos.
- **D)** Incorreta. Percepção geral não substitui critérios específicos.

**Conceito:** Qualidade por atributos.

**Pegadinha:** Buscar uma evidência única para propriedades distintas.

**Como pensar:** Decomponha atributo, condição, medida e instrumento.


### Comentário S4D5Q232

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — Qualidade

**Referência:** [Qualidade de produto, processo e evidência](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Um atributo obrigatório falhou.
- **B)** Incorreta. Mudar critério depois da execução destrói a evidência.
- **C)** Incorreta. Risco residual pode ser tratado por decisão competente.
- **D)** Correta. Critério falhou e o risco exige decisão rastreável.

**Conceito:** Qualidade e risco residual.

**Pegadinha:** Deixar a função apagar outros critérios.

**Como pensar:** Confronte cada saída com limite e autoridade de risco.


### Comentário S4D5Q233

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O motivo dominante é corrigir defeito manifestado.
- **B)** Incorreta. Não houve mudança do ambiente.
- **C)** Incorreta. Não se busca nova função ou melhoria voluntária.
- **D)** Incorreta. A ação ocorre para corrigir problema existente.

**Conceito:** Manutenção corretiva.

**Pegadinha:** Classificar pela complexidade da alteração.

**Como pensar:** Olhe o motivo que originou a mudança.

### Comentário S4D5Q234

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O sistema não tinha defeito diante do contrato anterior.
- **B)** Incorreta. O objetivo não é apenas reduzir risco futuro interno.
- **C)** Correta. A mudança responde a ambiente externo alterado.
- **D)** Incorreta. Pode haver melhoria, mas a causa dominante é adaptação.

**Conceito:** Manutenção adaptativa.

**Pegadinha:** Chamar a futura incompatibilidade de defeito original.

**Como pensar:** Identifique se mudou o produto ou o ambiente exigido.

### Comentário S4D5Q235

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não há defeito funcional nem mudança externa no segundo caso.
- **B)** Incorreta. A ordem e os motivos foram invertidos.
- **C)** Correta. A primeira melhora atributo; a segunda reduz risco futuro.
- **D)** Incorreta. O cenário não aponta ambiente alterado.

**Conceito:** Perfectiva e preventiva.

**Pegadinha:** Classificar toda melhoria interna como perfectiva.

**Como pensar:** Pergunte se o objetivo é ganho atual ou prevenção de problema futuro.

### Comentário S4D5Q236

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não identifica dependências nem risco.
- **B)** Correta. A mudança pode propagar-se por artefatos técnicos e operacionais.
- **C)** Incorreta. Tamanho do diff não representa alcance funcional.
- **D)** Incorreta. Confirmação isolada não protege consumidores.

**Conceito:** Análise de impacto.

**Pegadinha:** Limitar impacto ao arquivo editado.

**Como pensar:** Percorra elos para frente e para trás.


### Comentário S4D5Q237

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Imutabilidade absoluta impediria mudança autorizada.
- **B)** Correta. Controle permite evolução sem perder integridade.
- **C)** Incorreta. Ferramenta não substitui identificação, status, auditoria e decisão.
- **D)** Incorreta. Rigor deve ser proporcional e definido.

**Conceito:** Baseline e configuração.

**Pegadinha:** Confundir controle com congelamento ou ferramenta.

**Como pensar:** Pergunte o que é identificado, aprovado, versionado e auditável.


### Comentário S4D5Q238

**Nível:** Muito difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Acelera sem apagar controles essenciais.
- **B)** Incorreta. Perde rastreabilidade e eleva risco.
- **C)** Incorreta. Processo deve prever proporcionalidade e emergência.
- **D)** Incorreta. Tamanho não prova baixo impacto.

**Conceito:** Mudança emergencial.

**Pegadinha:** Escolher entre burocracia integral e ausência total de controle.

**Como pensar:** Mantenha registro, decisão, versão, teste, reversão e pós-revisão.


### Comentário S4D5Q239

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Confirmação não cobre efeitos laterais.
- **B)** Correta. Correção local precisa de proteção e prontidão operacional.
- **C)** Incorreta. Categoria não altera risco real.
- **D)** Incorreta. Baseline sem rastreabilidade não fecha a mudança.

**Conceito:** Liberação segura.

**Pegadinha:** Parar no reteste bem-sucedido.

**Como pensar:** Feche impacto técnico e prontidão operacional.


### Comentário S4D5Q240

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 3 — Manutenção

**Referência:** [Manutenção e gestão da mudança](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A origem dominante é a obrigação externa, sem esconder efeitos adicionais.
- **B)** Incorreta. O defeito não originou a solicitação principal.
- **C)** Incorreta. Melhoria interna não é a causa central.
- **D)** Incorreta. Pode-se classificar motivo dominante e decompor trabalhos.

**Conceito:** Classificação por motivo.

**Pegadinha:** Usar o último efeito como causa da demanda.

**Como pensar:** Separe origem principal de atividades agregadas.


### Comentário S4D5Q241

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Combina previsibilidade, evidência formal e redução precoce do risco.
- **B)** Incorreta. Risco técnico desconhecido pede evidência precoce.
- **C)** Incorreta. Iteração não suspende governança.
- **D)** Incorreta. Protótipo não prova arquitetura produtiva.

**Conceito:** Adaptação de processo.

**Pegadinha:** Escolher rótulo pelo único fator favorável.

**Como pensar:** Pondere estabilidade, risco técnico, conformidade, feedback e data.


### Comentário S4D5Q242

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Incrementos são operacionais, não apenas artefatos de aprendizado.
- **B)** Incorreta. Há entregas parciais de valor.
- **C)** Incorreta. Corretiva é categoria de manutenção.
- **D)** Correta. O produto cresce por capacidades entregáveis.

**Conceito:** Incremental.

**Pegadinha:** Confundir incremento com protótipo.

**Como pensar:** Pergunte se a parte entregue integra o produto utilizável.

### Comentário S4D5Q243

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Iteração pode ter objetivos, riscos e critérios.
- **B)** Incorreta. O cenário descreve revisitação deliberada.
- **C)** Incorreta. Os ciclos pertencem ao desenvolvimento.
- **D)** Correta. A solução é refinada em ciclos de aprendizado.

**Conceito:** Desenvolvimento iterativo e evolucionário.

**Pegadinha:** Equiparar mudança a improviso.

**Como pensar:** Procure planejamento por ciclo e aprendizado.

### Comentário S4D5Q244

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Validação parcial não cobre atributos e integração.
- **B)** Correta. O protótipo preserva aprendizados, mas produto exige engenharia e testes.
- **C)** Incorreta. O valor principal pode ser justamente o aprendizado.
- **D)** Incorreta. Rótulo não altera dívida nem evidência.

**Conceito:** Prototipação.

**Pegadinha:** Confundir aparência funcional com produto pronto.

**Como pensar:** Declare hipótese, evidência obtida e lacunas para produção.


### Comentário S4D5Q245

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Análise de risco é central e precoce.
- **B)** Incorreta. Protótipo pode ser estratégia, não definição inteira.
- **C)** Incorreta. Cadência específica não define espiral.
- **D)** Correta. O risco orienta o aprofundamento iterativo.

**Conceito:** Modelo espiral.

**Pegadinha:** Reduzi-lo ao desenho geométrico ou a protótipo.

**Como pensar:** Procure decisão explícita guiada por risco em cada ciclo.


### Comentário S4D5Q246

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Existência não prova adequação ao contexto.
- **B)** Correta. Velocidade e reúso só são adequados com riscos do ativo tratados.
- **C)** Incorreta. RAD não proíbe reúso.
- **D)** Incorreta. São justamente fatores críticos de viabilidade.

**Conceito:** RAD e desenvolvimento orientado a reúso.

**Pegadinha:** Tratar componente pronto como risco zero.

**Como pensar:** Avalie prazo, modularidade, participação e riscos transferidos.


### Comentário S4D5Q247

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Isso domina a construção.
- **B)** Incorreta. Isso domina a transição.
- **C)** Incorreta. Detalhamento exaustivo é prematuro.
- **D)** Correta. A fase decide viabilidade e fronteira do esforço.

**Conceito:** Fase de concepção.

**Pegadinha:** Confundir início com documentação completa.

**Como pensar:** Pergunte se vale a pena, para quem e dentro de qual escopo.


### Comentário S4D5Q248

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. São resultados típicos de transição.
- **B)** Incorreta. Iteração continua e mudança controlada é possível.
- **C)** Correta. A fase estabiliza base arquitetural e reduz incerteza.
- **D)** Incorreta. Aprendizado visual não resolve risco arquitetural informado.

**Conceito:** Fase de elaboração.

**Pegadinha:** Tomá-la como redação de documentos.

**Como pensar:** Procure arquitetura executável, risco reduzido e plano realista.


### Comentário S4D5Q249

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Inverte finalidades.
- **B)** Incorreta. Reduz transição e desloca atividade.
- **C)** Correta. As fases têm ênfases distintas e ainda iteram.
- **D)** Incorreta. Teste atravessa as fases.

**Conceito:** Construção e transição.

**Pegadinha:** Tratar fase como disciplina exclusiva.

**Como pensar:** Associe capacidade integrada à construção e prontidão do uso à transição.


### Comentário S4D5Q250

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Processos

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra feedback, evidência e governança.
- **B)** Incorreta. Contexto e risco devem orientar o processo.
- **C)** Incorreta. Resposta a mudança não equivale a perda de rastreabilidade.
- **D)** Incorreta. Teste precoce e multinível reduz risco.

**Conceito:** Seleção e adaptação de processo.

**Pegadinha:** Procurar modelo universal.

**Como pensar:** Relacione cada prática a risco, entrega, conformidade e evidência.


#### Comentário Extra Dia 5.1

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Hierarquia de fontes

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ato inferior não afasta lei por novidade.
- **B)** Incorreta. Regimento organiza competências internas dentro de limites.
- **C)** Incorreta. Notícia não substitui fonte jurídica.
- **D)** Correta. Lei é a fonte primária para a disciplina legal indicada.

**Conceito:** Hierarquia de fontes.

**Pegadinha:** Escolher o ato mais recente sem observar hierarquia.

**Como pensar:** Identifique objeto e espécie normativa.


#### Comentário Extra Dia 5.2

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Lei, decreto e regimento

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. É justamente a função descrita.
- **B)** Correta. Decreto regulamentador e regimento têm objetos distintos.
- **C)** Incorreta. Regulamento é subordinado à lei.
- **D)** Incorreta. Essa limitação é correta.

**Conceito:** Lei, decreto e regimento.

**Pegadinha:** Tratar todos os atos como equivalentes.

**Como pensar:** Associe cada fonte ao objeto que organiza.

#### Comentário Extra Dia 5.3

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Competência CFA/CRA

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Preserva função nacional, execução regional e limites.
- **B)** Incorreta. Autonomia não elimina hierarquia e unidade sistêmica.
- **C)** Incorreta. Direção nacional não absorve toda atuação local.
- **D)** Incorreta. O sistema prevê atuação regional dentro de jurisdição.

**Conceito:** Competência CFA/CRA.

**Pegadinha:** Confundir autonomia com soberania ou centralização total.

**Como pensar:** Filtre território, verbo de competência e limite.


#### Comentário Extra Dia 5.4

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Enquadramento ético

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Esses filtros precedem a consequência.
- **B)** Incorreta. Repercussão não substitui enquadramento.
- **C)** Incorreta. O foco recai no sujeito e na conduta relevantes.
- **D)** Incorreta. Consequência não deve preceder a classificação da conduta.

**Conceito:** Enquadramento ético.

**Pegadinha:** Pular diretamente para sanção.

**Como pensar:** Classifique quem fez o quê, em qual contexto e sob qual regra.

#### Comentário Extra Dia 5.5

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Publicidade e proteção

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Publicidade não elimina proteção específica.
- **B)** Incorreta. Restrição parcial não implica sigilo total automaticamente.
- **C)** Incorreta. Decisão deve seguir competência e regra aplicável.
- **D)** Correta. Concilia transparência e limite de divulgação.

**Conceito:** Publicidade e proteção.

**Pegadinha:** Escolher transparência total ou sigilo total.

**Como pensar:** Separe partes, base, finalidade e competência.


#### Comentário Extra Dia 5.6

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Roteiro de leitura institucional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A sequência filtra pertinência e alcance.
- **B)** Incorreta. Esses critérios não definem competência normativa.
- **C)** Incorreta. Começar pela consequência favorece enquadramento prematuro.
- **D)** Incorreta. Território não autoriza contrariar fonte superior.

**Conceito:** Roteiro de leitura institucional.

**Pegadinha:** Começar pela consequência desejada.

**Como pensar:** Encontre primeiro o objeto jurídico do caso.


#### Comentário Extra Dia 5.7

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Autonomia e unidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Órgão regional não revoga lei.
- **B)** Correta. Autonomia opera dentro do sistema e da hierarquia.
- **C)** Incorreta. Autonomia não elimina controles.
- **D)** Incorreta. A jurisdição regional delimita atuação.

**Conceito:** Autonomia e unidade.

**Pegadinha:** Converter autonomia em soberania.

**Como pensar:** Pergunte qual competência, em qual território e sob qual limite.


#### Comentário Extra Dia 5.8

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Hierarquia e temporalidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A revogação depende de competência e hierarquia.
- **B)** Incorreta. Numeração não define validade material.
- **C)** Correta. Novidade cronológica não supera fonte superior.
- **D)** Incorreta. Aplicação não é escolha livre.

**Conceito:** Hierarquia e temporalidade.

**Pegadinha:** Aplicar “lei posterior” a espécies distintas sem filtro.

**Como pensar:** Antes da data, verifique nível e competência.


#### Comentário Extra Dia 5.9

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Aplicação institucional

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra todos os filtros e preserva rastreabilidade.
- **B)** Incorreta. Proximidade não resolve hierarquia nem proteção.
- **C)** Incorreta. Transparência não apaga restrição legítima.
- **D)** Incorreta. Deve-se formular a dúvida e buscar decisão competente.

**Conceito:** Aplicação institucional.

**Pegadinha:** Resolver conflito por proximidade ou medo.

**Como pensar:** Isole cada fonte, alcance e dado antes de decidir.


#### Comentário Extra Dia 5.10

**Dia:** Dia 5

**Bloco:** Bloco 4 — Legislação CRA/CFA

**Matéria:** Legislação CRA/CFA

**Assunto:** Jurisdição regional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Ignora a função regional.
- **B)** Incorreta. Atuação local não transfere toda competência nacional.
- **C)** Correta. A atuação regional decorre da jurisdição, sem romper o sistema.
- **D)** Incorreta. A unidade do sistema e a hierarquia permanecem.

**Conceito:** Jurisdição regional.

**Pegadinha:** Oscilar entre inexistência e competência ilimitada.

**Como pensar:** Associe território, atribuição e limite.

#### Comentário Extra Dia 5.11

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Referência e paralelismo

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O pronome e a regência não identificam o objeto.
- **B)** Correta. Explicita o referente e preserva a sequência.
- **C)** Incorreta. A enumeração perde paralelismo e altera a ação.
- **D)** Incorreta. Inverte agentes e sentido.

**Conceito:** Referência e paralelismo.

**Pegadinha:** Aceitar pronome formalmente possível, mas semanticamente ambíguo.

**Como pensar:** Confira agente, objeto, forma paralela e ordem.

#### Comentário Extra Dia 5.12

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Conector concessivo e relação lógica

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O conector conclusivo não decorre logicamente do fato.
- **B)** Incorreta. Combina conectores incompatíveis e repete a causa.
- **C)** Correta. A oração concessiva admite o fato e preserva a ressalva.
- **D)** Incorreta. A estrutura concessiva está truncada.

**Conceito:** Conector concessivo e relação lógica.

**Pegadinha:** Escolher conector pela sonoridade.

**Como pensar:** Nomeie a relação antes de selecionar a palavra.

#### Comentário Extra Dia 5.13

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Concordância

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O verbo não concorda com o sujeito plural.
- **B)** Correta. O sujeito plural posposto exige verbo no plural.
- **C)** Incorreta. Há vírgula indevida e discordância.
- **D)** Incorreta. `Haver` no sentido de existir é impessoal.

**Conceito:** Concordância.

**Pegadinha:** Tomar o termo anterior ao verbo como sujeito automático.

**Como pensar:** Localize o núcleo do sujeito e verifique impessoalidade.

#### Comentário Extra Dia 5.14

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Negação e quantificador

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Isso seria negação de existência mais forte.
- **B)** Incorreta. Contraria a negação.
- **C)** Incorreta. A quantidade exata não é informada.
- **D)** Correta. A negação recai sobre o quantificador universal.

**Conceito:** Negação e quantificador.

**Pegadinha:** Converter `nem todos` em `nenhum`.

**Como pensar:** Formalize: não é verdade que todos passaram.


#### Comentário Extra Dia 5.15

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Reescrita integral

**Nível:** Muito difícil

**Uso:** Revisão

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Há discordância, colocação inadequada e absoluto indevido.
- **B)** Incorreta. A concessão é mal formada e a conclusão absoluta não decorre.
- **C)** Correta. A causa é explícita, o referente é claro e a conclusão não é absoluta.
- **D)** Incorreta. Há discordância e uso inadequado de conector.

**Conceito:** Reescrita integral.

**Pegadinha:** Premiar frase longa ou vocabularmente rebuscada.

**Como pensar:** Teste sintaxe, referente, relação lógica e força da afirmação.

#### Comentário Extra Dia 5.16

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Paralelismo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mistura substantivo, infinitivo e oração.
- **B)** Incorreta. A série não conserva estrutura.
- **C)** Incorreta. Mistura formas e relações.
- **D)** Correta. Todos os núcleos estão no infinitivo.

**Conceito:** Paralelismo.

**Pegadinha:** Ver apenas o sentido geral da lista.

**Como pensar:** Marque a forma gramatical de cada item.

#### Comentário Extra Dia 5.17

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Referência pronominal

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Há construção redundante e inadequada.
- **B)** Incorreta. O possessivo continua ambíguo e a regência é problemática.
- **C)** Incorreta. Altera o predicado e o sentido.
- **D)** Correta. `deste` explicita o referente pretendido no contexto.

**Conceito:** Referência pronominal.

**Pegadinha:** Manter possessivo com dois possíveis possuidores.

**Como pensar:** Repita ou marque explicitamente o núcleo.

#### Comentário Extra Dia 5.18

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Coesão lógica

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Causa e conclusão contradizem as premissas.
- **B)** Incorreta. Estrutura concessiva e conectores estão mal articulados.
- **C)** Correta. Cada conector corresponde à relação narrada.
- **D)** Incorreta. Contraste e consequência não se sustentam.

**Conceito:** Coesão lógica.

**Pegadinha:** Aceitar sequência de conectores sem relação real.

**Como pensar:** Substitua cada conector por sua função e teste a inferência.

#### Comentário Extra Dia 5.19

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Modalização e causalidade

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Apenas suaviza absolutos sem corrigir a garantia.
- **B)** Incorreta. Presume que a adoção da ferramenta assegura a execução do processo.
- **C)** Incorreta. Mantém a inferência indevida de ausência de falhas.
- **D)** Correta. Mantém a ferramenta como apoio condicionado e rejeita inferir ausência de falhas.

**Conceito:** Modalização e causalidade.

**Pegadinha:** Trocar `sempre` por advérbio menos forte e manter o erro.

**Como pensar:** Explicite condição, alcance e limite da evidência.


#### Comentário Extra Dia 5.20

**Dia:** Dia 5

**Bloco:** Bloco 5 — Português

**Matéria:** Português

**Assunto:** Reescrita integrada

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português: precisão lógica](semana_04_estudo.md#s4-d5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A sequência é paralela e a conclusão limita-se à evidência.
- **B)** Incorreta. Agente, paralelismo e conclusão estão corrompidos.
- **C)** Incorreta. Conectores não representam a cronologia nem a lógica.
- **D)** Incorreta. A enumeração não é paralela e a conclusão é absoluta.

**Conceito:** Reescrita integrada.

**Pegadinha:** Preferir a alternativa mais enfática.

**Como pensar:** Confira quem age, em que ordem, com que forma e qual conclusão.



---

# Dia 6 — Integração de Engenharia/UML, ITIL, COBIT e recursos informacionais

As 70 questões são autorais, calibradas pelo perfil documentado do Instituto Consulplan e ambientadas, quando pertinente, em situações públicas. Nenhum item reproduz questão real. Na primeira passagem, resolva seis dos dez itens classificados como Essenciais e avance até dez somente se houver correção A–D integral. As 20 Extras pertencem exclusivamente ao Português dos Blocos 4–5; o caderno de erros não cria banco próprio.

## Questões principais — S4D6Q251 a S4D6Q300

### S4D6Q251 — Diagrama pela pergunta

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A equipe precisa mostrar quem interage com o sistema e qual objetivo cada participante busca, sem detalhar mensagens internas. A vista mais adequada é:

A) diagrama de casos de uso.

B) diagrama de sequência entre participantes.

C) diagrama de implantação dos nós.

D) máquina de estados do participante.

### S4D6Q252 — Ordem de mensagens

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Para explicar em que ordem Portal, Serviço de Cadastro e Repositório trocam mensagens durante uma solicitação, use prioritariamente:

A) diagrama de classes.

B) diagrama de componentes.

C) diagrama de sequência.

D) casos de uso.

### S4D6Q253 — Ciclo do pedido

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Um pedido passa por rascunho, enviado, em análise e decidido; eventos são permitidos conforme o estado atual. O diagrama mais direto é:

A) diagrama de atividades do processo.

B) diagrama de objetos em dado instante.

C) máquina de estados do pedido.

D) diagrama de implantação dos artefatos.

### S4D6Q254 — Fluxo e paralelismo

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Uma análise divide-se em conferência documental e consulta cadastral paralelas, reunindo resultados antes da decisão. Qual diagrama destaca esse comportamento?

A) atividade.

B) classes.

C) componentes.

D) casos de uso.

### S4D6Q255 — Unidade substituível e interface

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A arquitetura precisa mostrar módulos substituíveis, interfaces fornecidas e dependências. Qual vista é mais adequada?

A) diagrama de objetos.

B) diagrama de componentes.

C) diagrama de atividade.

D) diagrama de casos de uso.

### S4D6Q256 — Do requisito ao teste

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A ligação `necessidade → requisito → caso de uso → caso de teste` serve principalmente para:

A) bloquear novas mudanças depois da aprovação formal e da baseline.

B) ligar origem, realização e evidência para avaliar cobertura e impacto.

C) dispensar revisão dos elos depois de registrados.

D) substituir a execução dos testes por vínculos documentais.

### S4D6Q257 — Mensagem e responsabilidade

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Um diagrama de sequência envia `calcularPrazo()` a um participante cuja classe não possui responsabilidade compatível. A ação correta é:

A) manter as vistas separadas, pois cada uma pode atribuir responsabilidades próprias.

B) duplicar `calcularPrazo()` nas classes participantes para eliminar a divergência.

C) confrontar interação e estrutura, corrigindo a mensagem ou a responsabilidade atribuída.

D) remover o elo entre os modelos e registrar ambos como alternativas válidas.

### S4D6Q258 — Impacto do prazo

**Nível:** Difícil

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A regra de prazo muda de dias corridos para úteis e utiliza calendário corporativo. Qual análise de impacto é mais completa?

A) Rastrear regra, calendário, consumidores e telas; revisar dados, mensagens, testes de fronteira/regressão, documentação e liberação.

B) Revisar regra, telas e calendário, mas testar apenas um dia útil comum e o módulo alterado.

C) Atualizar cálculo, dados e testes de fronteira, sem verificar consumidores nem o contrato do calendário.

D) Criar novo caso de uso e nova classe de prazo, mantendo artefatos e testes anteriores como baseline vigente.

### S4D6Q259 — Teste derivado de guarda

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A transição `pendente → em análise` exige todos os documentos válidos. Qual teste deriva diretamente dessa guarda?

A) Variar carga e tempo do servidor sem alterar os documentos.

B) Testar ausência, invalidade e completude; só a completude deve habilitar a transição.

C) Comparar a aparência do botão usando sempre os mesmos documentos válidos.

D) Executar apenas o conjunto completo e verificar a transição permitida.

### S4D6Q260 — Nós de execução

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A equipe precisa mostrar em quais nós executam portal, serviço e banco e como se comunicam. Use:

A) diagrama de implantação.

B) diagrama de classes.

C) diagrama de sequência.

D) diagrama de estados.

### S4D6Q261 — Objetivo e estrutura

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

O caso de uso “Protocolar pedido” possui o conceito Pedido com documentos. Qual relação entre vistas é correta?

A) Cada caso de uso deve corresponder a uma única classe controladora, em relação biunívoca entre as duas vistas.

B) Toda classe participante da realização deve também aparecer como ator no caso de uso.

C) Classes com operações completas tornam dispensável registrar fluxos alternativos no caso de uso.

D) O caso de uso descreve objetivo externo; classes modelam conceitos e responsabilidades que participam de sua realização.

### S4D6Q262 — Multiplicidade com base

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A regra diz que um pedido deve possuir ao menos um documento e cada documento pertence a um único pedido. Qual modelagem é coerente?

A) `0..1` Documento por Pedido e `1..*` Pedidos por Documento.

B) `1..*` Documentos por Pedido e `0..*` Pedidos por Documento.

C) `1..*` Documentos por Pedido e `1` Pedido por Documento.

D) `1` Documento por Pedido e nenhuma associação no sentido inverso.

### S4D6Q263 — Reúso em casos de uso

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Dois casos de uso sempre executam a mesma validação obrigatória; um comportamento opcional ocorre só sob condição. A relação conceitual mais adequada é:

A) usar `extend` na validação obrigatória e também na variação condicionada.

B) usar `include` na validação obrigatória comum e `extend` no comportamento opcional condicionado.

C) usar `include` em ambos, deixando a condição dentro do caso incluído.

D) representar a validação e a variação como atores secundários dos dois casos.

### S4D6Q264 — Comunicação e sequência

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Sobre diagramas de comunicação e sequência, assinale a correta.

A) Ambos modelam estrutura; comunicação substitui mensagens por associações permanentes.

B) Sequência registra estados do participante, enquanto comunicação registra somente classes.

C) Ambos têm a mesma ênfase temporal e diferem apenas pela orientação gráfica empregada.

D) Ambos modelam interação; sequência destaca tempo, e comunicação destaca ligações com mensagens numeradas.

### S4D6Q265 — Paralelismo e decisão integrados

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Um fluxo abre duas verificações paralelas, reúne ambas, aplica regra de decisão e encerra por três resultados. Qual alternativa preserva sintaxe e semântica do diagrama de atividade?

A) Usar divisão paralela, junção correspondente, nó de decisão com guardas e finais coerentes com os resultados.

B) Usar decisão para abrir os ramos e merge para sincronizá-los antes das guardas finais.

C) Usar fork para abrir os ramos e final de fluxo em cada um, supondo que os finais os sincronizem.

D) Serializar as verificações, usar decisão após a primeira e omitir a sincronização da segunda.

### S4D6Q266 — Guarda de estado

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Em uma máquina de estados, a transição é rotulada `aprovar [documentosValidos] / notificar`. A interpretação correta é:

A) `aprovar` é gatilho; `[documentosValidos]`, guarda; `notificar`, efeito.

B) `aprovar` é efeito; `[documentosValidos]`, estado-alvo; `notificar`, gatilho.

C) `aprovar` nomeia o estado de origem; guarda e efeito são mensagens.

D) Os três trechos são eventos síncronos executados na ordem escrita.

### S4D6Q267 — Interface requerida e fornecida

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

O componente Portal requer serviço de autenticação e o componente Identidade o fornece. A modelagem deve:

A) marcar no Portal a fornecida e em Identidade a requerida, invertendo produtor e consumidor modelados.

B) marcar no Portal a interface requerida e em Identidade a fornecida, ligando-as pelo contrato.

C) ocultar interfaces e manter somente uma dependência genérica entre os componentes.

D) representar Portal e Identidade como atores conectados ao mesmo caso de uso.

### S4D6Q268 — Implantação e atributos

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

O requisito exige disponibilidade e isolamento de dados. Qual uso do diagrama de implantação é adequado?

A) Representar redundância de nós e aceitar o desenho como prova suficiente dos atributos.

B) Exibir zonas e caminhos, mas omitir vínculo com requisitos e testes para manter as vistas independentes.

C) Usar multiplicidades no diagrama de classes para indicar redundância e isolamento físicos.

D) Modelar nós, zonas/redundância e comunicações, ligando decisões a requisitos e testes dos atributos.

### S4D6Q269 — Rastreabilidade em duas direções

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Qual associação está correta?

A) Para frente confirma a origem do requisito; para trás localiza sua implementação e seus testes.

B) Para frente localiza somente a documentação; para trás congela a origem e impede mudanças.

C) Para frente localiza realização e testes; para trás confirma origem e justificativa.

D) Para frente apoia cobertura; para trás serve apenas à auditoria histórica, não à análise de impacto.

### S4D6Q270 — Pedido documental integrado

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Um pedido exige documento válido, passa por análise e é implantado em dois nós. Qual cadeia inicial é mais coerente?

A) Partir da implantação, inferir atores pelos nós e escrever testes sem oráculo explícito.

B) Partir de requisito/caso de uso, alinhar atividade/estados e interações, chegar a componentes/implantação e testes rastreados.

C) Partir da classe `Pedido`, derivar dela todos os estados e considerar o aceite coberto pela estrutura em qualquer cenário.

D) Executar testes exploratórios, transformar resultados em requisitos e depois desenhar as vistas correspondentes.

### S4D6Q271 — Serviço e resultado

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

No recorte de gestão de serviços, um serviço deve ser entendido como meio de:

A) fornecer equipamentos ao consumidor, transferindo a ele propriedade e operação.

B) eliminar os riscos do consumidor, ainda que o serviço crie novos custos.

C) facilitar resultados desejados sem o consumidor gerir sozinho custos e riscos específicos.

D) produzir saídas internas previstas, ainda que não apoiem resultado percebido.

### S4D6Q272 — Saída e resultado

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

A central entrega relatório mensal; gestores passam a decidir mais cedo com dados confiáveis. São, respectivamente:

A) resultado e saída.

B) incidente e problema.

C) governança e gestão.

D) saída e resultado.

### S4D6Q273 — Interrupção e restauração

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Portal indisponível afeta milhares de usuários; a causa ainda é desconhecida. Qual ação inicial preserva classificação, prioridade e evidência?

A) Registrar o incidente e adiar a restauração até concluir a causa raiz.

B) Tratar como requisição urgente porque os usuários pedem a volta do acesso.

C) Classificar/priorizar o incidente por impacto/urgência, restaurar com contorno seguro e guardar evidências.

D) Aplicar correção emergencial sem registro, restaurar e encerrar antes de avaliar recorrência.

### S4D6Q274 — Causa recorrente

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

O serviço é restaurado por reinício, mas cai semanalmente. A investigação da causa e o controle do contorno pertencem prioritariamente à gestão de:

A) requisição de serviço, pois o reinício é procedimento conhecido.

B) incidente, pois a restauração temporária também elimina a causa.

C) problema, que investiga causa e controla contorno ou erro conhecido.

D) mudança, pois a recorrência exige alterar produção antes da investigação.

### S4D6Q275 — Pedido predefinido

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Servidor solicita acesso padrão previsto em catálogo e sujeito a aprovação conhecida. Isso se aproxima de:

A) incidente relacionado ao acesso.

B) problema de autorização recorrente.

C) decisão de governança de acesso.

D) requisição de serviço padronizada.

### S4D6Q276 — Mudança avaliada

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Uma solução de problema exige alterar configuração compartilhada. A prática de mudança deve:

A) impedir alterações na configuração compartilhada para conservar a estabilidade.

B) aplicar o mesmo rito máximo a qualquer alteração, sem considerar risco, urgência ou contexto operacional.

C) avaliar risco, autorizar no nível adequado, programar/testar a alteração e verificar resultado e reversão.

D) executar primeiro e registrar depois apenas se a correção causar outro incidente.

### S4D6Q277 — Ponto de contato

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Qual descrição é adequada ao service desk?

A) Resolvedor exclusivo de toda causa, do registro inicial à correção definitiva em qualquer equipe.

B) Instância de governança que define estratégia e investimento de serviço.

C) Ponto de contato para demandas e comunicação com usuários, integrado às práticas de serviço.

D) Software de chamados que opera independentemente de pessoas e processos.

### S4D6Q278 — Melhoria contínua

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Qual sequência sustenta melhoria contínua?

A) Adquirir ferramenta, registrar a baseline depois e declarar benefício pelo volume.

B) Alterar simultaneamente todo o processo para acelerar, sem isolar medidas.

C) Definir meta de saída interna e medir produção sem resultado do serviço.

D) Comparar estados atual/desejado, priorizar, mudar, medir resultado e aprender.

### S4D6Q279 — Incidente, problema e mudança

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Falha grave é contornada; análise encontra causa em biblioteca; correção exige nova versão. Qual encadeamento é mais coerente?

A) Incidente investiga a biblioteca, problema restaura e mudança registra a indisponibilidade.

B) Incidente restaura, problema investiga/gerencia causa e mudança controla a nova versão.

C) Incidente restaura e encerra; a nova versão segue como requisição, sem registrar problema.

D) Problema e mudança usam um único registro; incidente só é aberto se a nova versão falhar.

### S4D6Q280 — Priorização operacional

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Dois incidentes: um afeta um relatório adiado; outro impede atendimento nacional. A prioridade deve considerar:

A) impacto, urgência, acordos e contexto, usando a chegada apenas como um dos critérios.

B) horário de registro, salvo preferência técnica por item posterior com solução mais simples.

C) esforço de resolução, priorizando sempre a ocorrência mais fácil.

D) posição hierárquica do solicitante, independentemente do efeito no serviço.

### S4D6Q281 — Governança e gestão

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Conselho avalia opções, define direção e monitora resultados; equipes planejam e executam ações alinhadas. No COBIT, isso corresponde a:

A) gestão em ambos, pois governança não monitora.

B) governança no primeiro conjunto e gestão no segundo.

C) governança em ambos, pois gestão não decide planos.

D) governança no primeiro conjunto; monitoramento e execução pertencem somente à gestão.

### S4D6Q282 — Escopo empresarial de I&T

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

O COBIT trata informação e tecnologia:

A) somente na infraestrutura e no suporte internos mantidos pelo departamento de TI.

B) em toda a organização, onde I&T contribui para os objetivos institucionais.

C) apenas durante auditorias externas ou verificações regulatórias.

D) exclusivamente no ciclo de software executado pelas equipes técnicas.

### S4D6Q283 — Decisão e execução

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Há três opções de investimento, riscos distintos e indicadores de benefício. Qual distribuição de responsabilidades é coerente?

A) Governança escolhe a opção, detalha e executa o plano; gestão apenas reúne os indicadores.

B) Gestão define apetite de risco e prioridade; governança executa o investimento e reporta.

C) Auditoria escolhe a prioridade; governança autoriza e gestão limita-se a evidenciar conformidade.

D) Governança avalia opções, direciona e monitora; gestão detalha o plano, executa e reporta evidências.

### S4D6Q284 — Complementaridade

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Qual comparação entre ITIL e COBIT é adequada?

A) São softwares concorrentes para a mesma operação e apenas um deve ser instalado e utilizado pela organização.

B) ITIL orienta produtos/serviços; COBIT abrange governança e gestão de I&T; ambos podem ser integrados.

C) ITIL assume a governança institucional e COBIT executa integralmente as práticas de serviço.

D) Ambos conferem certificação organizacional automática depois da adoção.

### S4D6Q285 — Adaptação do referencial

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Uma organização pretende implementar todas as práticas e controles com igual rigor, sem avaliar porte, risco ou objetivo. A resposta mais consistente é:

A) Aplicar todas as práticas e controles com o mesmo rigor para preservar a integridade.

B) Adaptar o sistema ao contexto, priorizando objetivos, papéis, informação e evidências relevantes.

C) Selecionar somente as práticas mais fáceis, pois adaptação dispensa objetivos e riscos.

D) Transferir adaptação e prioridades ao fornecedor, que conhece a configuração técnica.

### S4D6Q286 — Documento com ciclo de vida

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Capturar, classificar, indexar, versionar, controlar acesso, reter e recuperar documentos caracteriza principalmente:

A) GED, pelo ciclo de versão, acesso e retenção documental.

B) CRM, pelo histórico de interações associado aos documentos.

C) ERP, pela integração da transação que originou cada documento.

D) BPM, pela gestão ponta a ponta do processo que usa os documentos.

### S4D6Q287 — Roteamento de tarefas

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Uma solicitação deve passar por triagem, análise e decisão conforme papéis e regras. O recurso mais diretamente associado ao encaminhamento é:

A) GED, pelo versionamento dos documentos que acompanham a solicitação.

B) workflow, pelo roteamento de tarefas e estados segundo papéis e regras.

C) CRM, pelo histórico dos contatos mantidos ao longo do atendimento.

D) ERP, pela integração das transações geradas depois da decisão.

### S4D6Q288 — Melhoria ponta a ponta

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Órgão deseja descobrir o processo real, modelar AS-IS, analisar espera, desenhar TO-BE, definir dono, executar, medir e melhorar. Isso caracteriza:

A) workflow como disciplina completa de descoberta, desenho e melhoria.

B) BPMN como método de gestão que define dono, indicador e execução.

C) GED como gestão do ciclo do processo, além do ciclo documental.

D) BPM como disciplina de gestão de processos ponta a ponta.

### S4D6Q289 — Integração transacional

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Compras, patrimônio, orçamento e pessoas usam módulos coordenados e dados consistentes para registrar transações. A finalidade aproxima-se de:

A) CRM.

B) GED.

C) workflow isolado.

D) ERP.

### S4D6Q290 — Histórico de relacionamento

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

O órgão quer reunir contatos, manifestações, canais e respostas para manter continuidade do relacionamento com cidadão/registrado. O núcleo é:

A) ERP.

B) CRM.

C) GED.

D) BPMN.

### S4D6Q291 — Cinco recursos, um atendimento

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Cidadão envia documento, demanda segue por tarefas, deferimento gera cobrança, contatos ficam históricos e o órgão mede o processo inteiro. Qual mapeamento preserva os cinco objetos?

A) GED–documento; workflow–tarefas; ERP–interações; CRM–cobrança; BPM–resultado ponta a ponta.

B) GED–documento; workflow–melhoria; BPM–tarefas; ERP–cobrança; CRM–interações.

C) GED–documento; workflow–tarefas; ERP–cobrança; CRM–interações; BPM–resultado ponta a ponta.

D) GED–tarefas; workflow–documento; ERP–cobrança; CRM–interações; BPM–resultado ponta a ponta.

### S4D6Q292 — Regra, vista e evidência

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

A regra exige dois aprovadores para valor alto. Qual cadeia é coerente?

A) Formalizar requisito/limite; modelar decisão e interação; alocar responsabilidades; testar valores abaixo/acima e segregação.

B) Modelar dois aprovadores apenas na classe, usar uma interação para todo valor e testar somente acima do limite.

C) Registrar a regra na implantação, manter um aprovador no fluxo e testar apenas a infraestrutura dos nós.

D) Executar testes exploratórios, escolher o limite observado e atualizar o requisito sem confirmar sua fonte.

### S4D6Q293 — Vistas contraditórias

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Caso de uso permite cancelamento após envio; máquina de estados proíbe; teste espera permissão. Qual tratamento é correto?

A) Confirmar fonte e decisão com responsáveis, alinhar caso de uso, estados e teste e versionar a baseline.

B) Adotar o teste por ser mais recente e ajustar somente o caso de uso ao resultado obtido.

C) Manter as três versões como perspectivas válidas e versioná-las sem decidir qual regra prevalece.

D) Remover o elo entre estado e teste e registrar a divergência fora da baseline do requisito.

### S4D6Q294 — Mudança transversal

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Nova regra altera ator autorizado, estado permitido e serviço externo, com prazo curto. Qual resposta integra pelo menos três filtros independentes?

A) Atualizar requisito, ator/caso e estado; manter a interface externa e testar só a tela, sem regressão.

B) Atualizar requisito, estado e contrato externo; preservar a autorização anterior e testar apenas o fluxo principal.

C) Atualizar autorização, interface, segurança e dados; deixar fonte e vistas para depois e dispensar monitoramento.

D) Atualizar fonte/requisito/autorização; revisar vistas, interface, segurança e dados; confirmar/regredir, versionar, implantar e monitorar.

### S4D6Q295 — Serviço sob governança

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Governança prioriza disponibilidade; gestão implementa monitoramento; ocorre interrupção recorrente e uma correção é proposta. Qual encadeamento é adequado?

A) Governança reinicia o serviço e aprova a correção; incidente controla orçamento; problema executa a nova versão.

B) Incidente espera a causa; problema define a prioridade institucional; mudança implanta sem nova autorização.

C) ITIL define a prioridade institucional; COBIT executa as práticas; gestão deixa de reportar após o monitoramento.

D) Governança direciona/monitora; gestão opera e mede; incidente restaura, problema investiga e mudança controla a correção.

### S4D6Q296 — Valor com saída insuficiente

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Uma equipe entrega 500 relatórios no prazo, mas ninguém os usa e decisões não melhoram. Qual avaliação considera saída, resultado, valor e melhoria?

A) O volume evidencia saída; é preciso confrontar necessidade, uso e resultado, revisar a medida e melhorar o serviço.

B) Volume e prazo evidenciam saída, resultado e valor; a medida deve permanecer mesmo sem uso.

C) A falta de uso invalida qualquer medição; o serviço deve parar até que o valor seja declarado.

D) A falta de uso é incidente de disponibilidade; produzir mais relatórios restaura o serviço e encerra o caso.

### S4D6Q297 — Documento, fluxo e processo

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Um órgão digitaliza documentos, automatiza aprovações redundantes e percebe aumento do prazo total. Qual diagnóstico preserva três conceitos?

A) GED controla documentos e workflow encaminha tarefas, mas BPM deve analisar/redesenhar o processo antes de automatizar desperdício.

B) GED controla documentos e deve remover aprovações sem BPM, pois o versionamento revela o desperdício.

C) Workflow acelera tarefas; se o prazo total piorar, bastam novas regras sem rever o processo ponta a ponta.

D) BPM consiste em trocar a ferramenta de workflow e manter as aprovações com monitoramento melhor.

### S4D6Q298 — ERP e CRM conectados

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Atendimento no CRM gera parcelamento registrado no ERP. Qual controle de integração é mais importante?

A) Replicar todos os campos com sincronização periódica, sem dono nem mapeamento semântico.

B) Permitir novas tentativas e confiar no log da transação, sem idempotência nem reconciliação.

C) Usar o mesmo identificador e nomes de tela como prova de integração, sem contrato de autorização.

D) Definir identidade, semântica, autorização, idempotência, tratamento de falhas e reconciliação entre interação e transação.

### S4D6Q299 — ITIL e COBIT sem sobreposição indevida

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Organização quer melhorar suporte e assegurar alinhamento institucional. Qual uso evita rivalidade e sobreposição indevida?

A) Mapear ambos, mas duplicar aprovações e indicadores para manter cadeias independentes de controle e responsabilidade institucional.

B) Usar ITIL para práticas e prioridades institucionais, deixando COBIT apenas para auditoria periódica.

C) Usar COBIT para objetivos e execução das práticas, deixando ITIL restrito ao service desk.

D) Usar COBIT em objetivos e responsabilidades; ITIL em práticas de serviço; mapear papéis, métricas e interfaces.

### S4D6Q300 — Ciclo completo do serviço público

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

Um novo serviço nasce de manifestação do cidadão, exige documentos, integra cobrança, entra em produção e depois apresenta falha recorrente. Qual alternativa mantém requisitos, UML, recursos, testes, serviço e governança em um ciclo verificável?

A) Rastrear requisito/vistas e integrar recursos, mas usar o incidente de produção como aceite e deixar a gestão definir prioridades institucionais.

B) Modelar requisito/vistas/testes e integrar recursos; governança direciona, mas falha recorrente vira requisição e correção sem mudança.

C) Rastrear necessidade a requisitos/vistas/testes; integrar recursos sob BPM; governança direcionar/monitorar, gestão operar; incidente restaurar, problema investigar e mudança corrigir.

D) Rastrear necessidade e testes e integrar a suíte; governança opera incidentes, gestão redefine risco e o contorno encerra a falha recorrente.

## Questões extras — Dia 6

#### Extra Dia 6.1 — Concessão

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Relação concessiva

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Assinale o período em que o conector expressa concessão.

A) Como o canal é útil, ele precisa de avaliação contínua.

B) O canal é útil; portanto, precisa de avaliação contínua.

C) O canal é útil, mas recebe mensagens diariamente.

D) Embora o canal seja útil, ele precisa de avaliação contínua.

#### Extra Dia 6.2 — Causa e consequência

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Relação causal entre orações

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Qual frase apresenta relação causal coerente?

A) Como as respostas eram tardias, o órgão reviu o fluxo de atendimento.

B) Embora as respostas fossem tardias, o órgão reviu o fluxo de atendimento.

C) As respostas eram tardias; contudo, o órgão reviu o fluxo de atendimento.

D) O órgão reviu o fluxo; portanto, as respostas passaram a ser tardias.

#### Extra Dia 6.3 — Haver e concordância

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Concordância integrada

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Assinale a opção correta quanto a concordância, impessoalidade de `haver` e pontuação.

A) Houveram manifestações que exigem resposta, e faltam equipes para analisá-las.

B) Há manifestações que exige resposta, e falta equipes para analisá-las.

C) Há manifestações que exigem resposta, e faltam equipes para analisá-las.

D) Devem haver manifestações que exigem resposta, e faltam equipe para analisá-las.

#### Extra Dia 6.4 — Quantificador negado

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Negação de universal

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

A frase “Nem todas as sugestões foram acolhidas” permite concluir que:

A) nenhuma das sugestões apresentadas foi acolhida pelo órgão.

B) ao menos uma sugestão não foi acolhida.

C) exatamente uma sugestão foi recusada.

D) todas foram acolhidas parcialmente.

#### Extra Dia 6.5 — Oração relativa e sentido

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Restrição e explicação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Compare: I. “Os canais que recebem alto volume serão ampliados.” II. “Os canais, que recebem alto volume, serão ampliados.” A leitura adequada é:

A) Em ambas, somente os canais de alto volume serão ampliados.

B) I restringe a ampliação aos canais de alto volume; II explica que o conjunto referido recebe alto volume.

C) I explica algo sobre todos os canais do conjunto referido; II seleciona apenas os que recebem alto volume.

D) A vírgula altera apenas o ritmo; o alcance permanece restritivo nas duas frases.

#### Extra Dia 6.6 — Referente explícito

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Referência pronominal

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Em “A ouvidoria enviou a análise à diretoria depois de revisá-la”, se a análise foi revisada, a forma mais clara é:

A) A ouvidoria enviou a análise à diretoria depois de revisá-la cuidadosamente.

B) Depois da diretoria revisar a ouvidoria, enviou a análise.

C) Depois de revisar a análise, a ouvidoria a enviou à diretoria.

D) A análise enviou-se à diretoria que a revisou.

#### Extra Dia 6.7 — Paralelismo e função

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Paralelismo sintático e semântico

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Qual enumeração preserva forma e função semântica?

A) escutar os cidadãos, análise das causas, responder às demandas e avaliação dos resultados.

B) escuta dos cidadãos, analisar as causas, resposta às demandas e avaliar os resultados.

C) que se ouçam os cidadãos, analisar as causas, que se responda às demandas e avaliar resultados.

D) ouvir os cidadãos, analisar as causas, responder às demandas e avaliar os resultados.

#### Extra Dia 6.8 — Modalização

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Modalização proporcional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Qual reescrita evita garantia absoluta sem esvaziar a ideia?

A) A escuta qualificada melhora necessariamente qualquer serviço, mesmo sem resposta.

B) A escuta talvez se relacione a melhorias, sem que seja possível indicar como.

C) A escuta qualificada pode melhorar serviços quando gera análise, resposta e acompanhamento.

D) A escuta não melhora serviço algum porque não garante resultado em todos os casos.

#### Extra Dia 6.9 — Reescrita sob quatro filtros

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Reescrita integrada

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Escolha a reescrita com concordância, referência, relação lógica e força de afirmação adequadas.

A) Como as manifestações revelaram falhas recorrentes, a equipe as analisou e propôs medidas que podem reduzir o problema.

B) Embora as manifestações tenham revelado falhas recorrentes, a equipe as analisou e propôs medidas que podem reduzir o problema.

C) Como as manifestações revelaram falhas recorrentes, a equipe lhes analisou e propôs medidas que podem reduzir o problema.

D) Como as manifestações revelou falhas recorrentes, a equipe as analisou e propôs medidas que eliminam o problema.

#### Extra Dia 6.10 — Vírgula com intercalação

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Pontuação de termo intercalado

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Assinale a pontuação correta.

A) Após examinar as manifestações a equipe responsável, apresentou o relatório.

B) A equipe responsável apresentou o relatório, após, examinar as manifestações.

C) Após o exame das manifestações a equipe responsável apresentou, o relatório.

D) A equipe responsável, após examinar as manifestações, apresentou o relatório.

#### Extra Dia 6.11 — Correlação e cronologia

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Correlação verbal e sequência

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Assinale a versão que preserva cronologia, correlação verbal, agente e conclusão proporcional.

A) Depois que o órgão analisou as manifestações, revisou o fluxo e passou a acompanhar os resultados; assim, pôde verificar se as mudanças produziam efeito.

B) Depois que o órgão analisara as manifestações, revisaria o fluxo e passou a acompanhar os resultados; assim, sempre comprovou a melhoria.

C) Depois que o órgão analisou as manifestações, o fluxo foi revisto e os resultados provaram que toda mudança produz melhoria.

D) Depois de analisar as manifestações, a diretoria revisou o fluxo e o órgão mediu os resultados antes de implementar as mudanças.

#### Extra Dia 6.12 — Gerúndio ambíguo

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Gerúndio e ambiguidade

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Em “O setor respondeu ao cidadão enviando o relatório incompleto”, se o relatório já estava incompleto antes do envio, a reescrita mais clara é:

A) O setor respondeu ao cidadão enquanto deixava o relatório incompleto durante o envio.

B) O setor respondeu ao cidadão e lhe enviou o relatório, que já estava incompleto.

C) O setor respondeu ao cidadão e, ao enviar o relatório, tornou-o incompleto.

D) O relatório incompleto respondeu ao cidadão depois de ser enviado pelo setor.

#### Extra Dia 6.13 — Redundância

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Concisão com preservação

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Qual frase elimina redundância sem perder a condição necessária?

A) O órgão respondeu às manifestações dentro do prazo definido.

B) O órgão apresentou uma resposta respondida às manifestações dentro do prazo definido.

C) O órgão respondeu às manifestações.

D) O órgão respondeu às manifestações dentro do prazo antecipado previamente.

#### Extra Dia 6.14 — Paralelismo de critérios

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Paralelismo argumentativo

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Em uma tese, quais termos formam série paralela e semanticamente comparável?

A) tornar as decisões transparentes, clareza das respostas e avaliar os resultados.

B) transparência das decisões, responder com clareza e avaliação dos resultados.

C) decisões transparentes, respostas claras e avaliar os resultados.

D) transparência das decisões, clareza das respostas e avaliação dos resultados.

#### Extra Dia 6.15 — Sentido preservado

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Preservação semântica

**Nível:** Muito difícil

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

A frase “A escuta não substitui a decisão administrativa, mas pode qualificá-la quando há análise e resposta” deve ser reescrita preservando negação, contraste, possibilidade, referente e condição. Assinale a correta.

A) Embora não tome o lugar da decisão administrativa, a escuta sempre a torna correta quando há análise e resposta.

B) A escuta pode tornar a decisão mais bem fundamentada quando há análise e resposta e, por isso, substituí-la.

C) Embora não tome o lugar da decisão administrativa, a escuta pode torná-la mais bem fundamentada se houver análise e resposta.

D) Embora não tome o lugar da decisão administrativa, a escuta pode torná-la mais bem fundamentada mesmo sem análise ou resposta.

#### Extra Dia 6.16 — Coesão entre períodos

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Progressão textual

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Qual sequência possui progressão coerente?

A) As manifestações revelaram demora no atendimento. Esse diagnóstico orientou a revisão do fluxo. Depois, o novo prazo foi medido para verificar o efeito da mudança.

B) As manifestações revelaram demora. Antes de concluir o diagnóstico e revisar o fluxo, o novo prazo foi medido. Só depois, o resultado motivou a mudança.

C) As manifestações revelaram demora. O fluxo foi revisto. Esse diagnóstico só surgiu depois da medição do efeito.

D) As manifestações revelaram demora. O novo prazo foi medido. Portanto, o fluxo foi revisto antes de qualquer mudança.

#### Extra Dia 6.17 — Regência e crase

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Regência e crase

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Assinale a frase correta quanto à regência e ao emprego da crase.

A) A equipe apresentou à análise a diretoria e respondeu as manifestações.

B) A equipe apresentou a análise à diretoria e respondeu às manifestações.

C) A equipe apresentou a análise à uma diretoria e respondeu à todas as manifestações.

D) A equipe apresentou à análise à diretoria e respondeu as manifestações.

#### Extra Dia 6.18 — Tese e desenvolvimento

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Desenvolvimento da tese

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Uma introdução afirma que escuta melhora serviços quando há resposta e avaliação. Qual desenvolvimento preserva a arquitetura argumentativa?

A) Explicar como novas tecnologias ampliam canais, sem relacioná-las a resposta ou avaliação.

B) Defender que manifestações raramente ajudam e, por isso, resposta e avaliação são dispensáveis.

C) Explicar como respostas fecham o ciclo com o cidadão e indicadores avaliam se a mudança resolveu o problema.

D) Reafirmar que escuta melhora serviços com resposta e avaliação, sem desenvolver o mecanismo causal nem apresentar evidência que o sustente.

#### Extra Dia 6.19 — Conclusão sob filtros

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Conclusão dissertativa

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Qual conclusão retoma tese e eixos, preserva linguagem geral, não cria argumento novo e evita garantia absoluta?

A) Assim, resposta e avaliação melhoram os canais, e uma ferramenta de IA garantirá eliminar definitivamente as falhas.

B) Assim, canais de escuta contribuem quando há resposta, mas a avaliação torna-se dispensável após a satisfação do cidadão.

C) Assim, canais de escuta apenas registram demandas, pois a decisão administrativa deve ignorar percepções do cidadão.

D) Assim, a escuta melhora serviços quando manifestações recebem resposta e mudanças são avaliadas, aproximando decisão pública e necessidade real.

#### Extra Dia 6.20 — Revisão integral

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Revisão do texto integral

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

Ao revisar uma dissertação de 20 a 30 linhas, qual protocolo cobre conteúdo, coesão, sintaxe, sentido e formato sem substituir o texto por outro tema?

A) Conferir tema, tese, função dos parágrafos, progressão e linhas; depois trocar palavras comuns por raras sem revisar sintaxe e sentido.

B) Conferir tema/tese, função dos parágrafos, progressão, conectores, referentes, gramática, sentido, conclusão e linhas; reescrever o pior trecho.

C) Conferir gramática, referentes, pontuação e linhas e reescrever o pior período, sem revisar tese, argumentos ou conclusão.

D) Conferir tema, tese, coesão, sintaxe e conclusão e então acrescentar argumento novo na última linha, sem reescrever o trecho fraco.

## Gabarito — Dia 6

### Principais

| S4D6Q251 | S4D6Q252 | S4D6Q253 | S4D6Q254 | S4D6Q255 | S4D6Q256 | S4D6Q257 | S4D6Q258 | S4D6Q259 | S4D6Q260 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | C | C | A | B | B | C | A | B | A |

| S4D6Q261 | S4D6Q262 | S4D6Q263 | S4D6Q264 | S4D6Q265 | S4D6Q266 | S4D6Q267 | S4D6Q268 | S4D6Q269 | S4D6Q270 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| D | C | B | D | A | A | B | D | C | B |

| S4D6Q271 | S4D6Q272 | S4D6Q273 | S4D6Q274 | S4D6Q275 | S4D6Q276 | S4D6Q277 | S4D6Q278 | S4D6Q279 | S4D6Q280 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| C | D | C | C | D | C | C | D | B | A |

| S4D6Q281 | S4D6Q282 | S4D6Q283 | S4D6Q284 | S4D6Q285 | S4D6Q286 | S4D6Q287 | S4D6Q288 | S4D6Q289 | S4D6Q290 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| B | B | D | B | B | A | B | D | D | B |

| S4D6Q291 | S4D6Q292 | S4D6Q293 | S4D6Q294 | S4D6Q295 | S4D6Q296 | S4D6Q297 | S4D6Q298 | S4D6Q299 | S4D6Q300 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| C | A | A | D | D | A | A | D | D | C |

### Extras

| 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | 6.6 | 6.7 | 6.8 | 6.9 | 6.10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| D | A | C | B | B | C | D | C | A | D |

| 6.11 | 6.12 | 6.13 | 6.14 | 6.15 | 6.16 | 6.17 | 6.18 | 6.19 | 6.20 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | B | A | D | C | A | B | C | D | B |

## Comentários — Dia 6

### Comentário S4D6Q251

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A pergunta é sobre atores, objetivos e fronteira.
- **B)** Incorreta. Sequência enfatiza ordem temporal de mensagens.
- **C)** Incorreta. Implantação mostra nós e artefatos.
- **D)** Incorreta. Estados mostram ciclo de vida de um objeto.

**Conceito:** Escolha de diagrama.

**Pegadinha:** Escolher a vista mais detalhada em vez da pertinente.

**Como pensar:** Traduza a pergunta do caso para a pergunta de cada diagrama.

### Comentário S4D6Q252

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Classes mostram estrutura, não a cronologia da interação.
- **B)** Incorreta. Componentes mostram unidades e interfaces, sem detalhar necessariamente a ordem.
- **C)** Correta. Ele evidencia participantes e ordenação temporal.
- **D)** Incorreta. Casos de uso mostram objetivos externos.

**Conceito:** Diagrama de sequência.

**Pegadinha:** Usar estrutura para responder comportamento temporal.

**Como pensar:** Procure a palavra ordem e os participantes.

### Comentário S4D6Q253

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Atividade mostra fluxo, mas não é a vista principal do ciclo persistente.
- **B)** Incorreta. Objetos são instâncias em uma fotografia estrutural.
- **C)** Correta. O foco é ciclo de vida, evento, guarda e transição.
- **D)** Incorreta. Nós não descrevem transições de negócio.

**Conceito:** Máquina de estados.

**Pegadinha:** Confundir fluxo de trabalho com ciclo de vida do objeto.

**Como pensar:** Pergunte se o interesse é onde está o objeto e como reage a eventos.


### Comentário S4D6Q254

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Fork/join, decisões e fluxo são próprios dessa vista.
- **B)** Incorreta. Classe não mostra paralelismo do processo.
- **C)** Incorreta. Componente mostra organização física/lógica, não o fluxo narrado.
- **D)** Incorreta. Objetivos não detalham a coordenação interna.

**Conceito:** Diagrama de atividades.

**Pegadinha:** Escolher sequência apenas porque há ordem.

**Como pensar:** Procure fluxo, ramificação, paralelismo e junção.

### Comentário S4D6Q255

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Objetos mostram instâncias em um momento.
- **B)** Correta. Componentes e interfaces respondem à estrutura modular.
- **C)** Incorreta. Atividades mostram fluxo de ações.
- **D)** Incorreta. Casos de uso não descrevem unidades de implementação.

**Conceito:** Componentes e interfaces.

**Pegadinha:** Chamar classe de componente por ambos serem caixas.

**Como pensar:** Identifique unidade substituível, interface e dependência.

### Comentário S4D6Q256

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Rastreabilidade controla impacto, não congela necessidade.
- **B)** Correta. Os elos permitem navegar justificativa e evidência.
- **C)** Incorreta. Relações precisam ser analisadas e mantidas.
- **D)** Incorreta. Matriz não é evidência de execução.

**Conceito:** Rastreabilidade.

**Pegadinha:** Tratar a matriz como garantia automática.

**Como pensar:** Pergunte de onde veio, onde foi realizado e como foi testado.


### Comentário S4D6Q257

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Vistas são parciais, não contraditórias por licença.
- **B)** Incorreta. Duplicação não resolve alocação de responsabilidade.
- **C)** Correta. As vistas devem contar uma história compatível.
- **D)** Incorreta. Eliminar evidência não corrige o modelo.

**Conceito:** Consistência entre vistas.

**Pegadinha:** Aceitar cada diagrama isoladamente correto.

**Como pensar:** Confronte mensagem, receptor, operação e requisito.


### Comentário S4D6Q258

**Nível:** Difícil

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A mudança atravessa regra, arquitetura, teste e operação.
- **B)** Incorreta. Ainda omite fronteiras do calendário, regressão nos consumidores e a liberação integrada.
- **C)** Incorreta. Cobre parte do cálculo, mas ignora consumidores e o contrato da dependência corporativa.
- **D)** Incorreta. Cria artefatos paralelos sem resolver a inconsistência com a baseline ainda vigente.

**Conceito:** Impacto rastreável.

**Pegadinha:** Limitar a mudança ao artefato onde foi percebida.

**Como pensar:** Percorra origem, dependências, testes e operação.


### Comentário S4D6Q259

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não avalia a regra da guarda.
- **B)** Correta. Os dados exercitam lados falso e verdadeiro da condição.
- **C)** Incorreta. Aparência não prova a condição de estado.
- **D)** Incorreta. Não cobre as condições impeditivas.

**Conceito:** Teste de guarda.

**Pegadinha:** Testar somente a transição permitida.

**Como pensar:** Negue e satisfaça cada condição relevante.


### Comentário S4D6Q260

**Nível:** Médio

**Uso:** Essenciais

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Ele relaciona nós, artefatos e caminhos de comunicação.
- **B)** Incorreta. Classes não localizam execução.
- **C)** Incorreta. Mensagens não substituem topologia de implantação.
- **D)** Incorreta. Estados não representam infraestrutura.

**Conceito:** Diagrama de implantação.

**Pegadinha:** Confundir comunicação lógica com localização de execução.

**Como pensar:** Procure onde o artefato roda e por qual ligação.

### Comentário S4D6Q261

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não há correspondência biunívoca obrigatória.
- **B)** Incorreta. Ator é papel externo, não classe interna.
- **C)** Incorreta. Estrutura não descreve sozinha os cenários.
- **D)** Correta. As vistas têm funções distintas e conectáveis.

**Conceito:** Caso de uso e classes.

**Pegadinha:** Forçar mapeamento um para um.

**Como pensar:** Separe objetivo externo de estrutura interna.


### Comentário S4D6Q262

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Contraria ambos os limites.
- **B)** Incorreta. Preserva o mínimo por pedido, mas permite documento órfão ou compartilhado por vários pedidos.
- **C)** Correta. Representa mínimo um e pertencimento único.
- **D)** Incorreta. Limita indevidamente a um documento e não representa o pertencimento nos dois sentidos da associação.

**Conceito:** Multiplicidade.

**Pegadinha:** Escolher cardinalidade por conveniência técnica.

**Como pensar:** Leia cada extremidade como pergunta em linguagem natural.


### Comentário S4D6Q263

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Extensão não representa trecho sempre obrigatório.
- **B)** Correta. Preserva obrigatoriedade e variabilidade.
- **C)** Incorreta. Inclusão contradiz a condição opcional.
- **D)** Incorreta. Ator representa papel externo.

**Conceito:** Include e extend.

**Pegadinha:** Decidir pelo desenho mais curto.

**Como pensar:** Pergunte se o comportamento sempre ocorre ou acrescenta variação condicionada.


### Comentário S4D6Q264

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ele modela mensagens entre participantes conectados.
- **B)** Incorreta. Ambos mostram participantes e mensagens; sequência não se reduz a estados, nem comunicação a classes estáticas.
- **C)** Incorreta. A ênfase altera legibilidade conforme a pergunta.
- **D)** Correta. A diferença é de ênfase, não de universo modelado.

**Conceito:** Diagramas de interação.

**Pegadinha:** Tratá-los como conteúdos sem relação ou equivalentes perfeitos.

**Como pensar:** Compare mesma interação sob duas ênfases.


### Comentário S4D6Q265

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cada elemento atende a uma função distinta.
- **B)** Incorreta. Decisão escolhe alternativas; não sincroniza fluxos paralelos.
- **C)** Incorreta. Finais de fluxo encerram ramos, mas não substituem a junção que sincroniza os caminhos paralelos.
- **D)** Incorreta. Serializar altera o paralelismo e a decisão antecipada deixa uma verificação fora da regra integrada.

**Conceito:** Atividade com múltiplos controles.

**Pegadinha:** Trocar decisão por fork ou merge por join.

**Como pensar:** Pergunte se os caminhos são alternativos ou simultâneos e onde sincronizam.

### Comentário S4D6Q266

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A notação separa gatilho, condição e ação.
- **B)** Incorreta. Inverte gatilho e efeito e trata a expressão booleana como estado-alvo.
- **C)** Incorreta. O primeiro termo é gatilho; guarda e efeito não formam duas mensagens sem receptor.
- **D)** Incorreta. A notação descreve gatilho, condição e efeito, não três chamadas síncronas.

**Conceito:** Evento, guarda e efeito.

**Pegadinha:** Ler qualquer rótulo como nome de estado.

**Como pensar:** Separe gatilho, condição booleana e ação.


### Comentário S4D6Q267

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Inverte os papéis.
- **B)** Correta. Mostra contrato e direção da necessidade.
- **C)** Incorreta. Componentes colaboram por interfaces.
- **D)** Incorreta. Atores são papéis externos ao sistema.

**Conceito:** Interfaces de componentes.

**Pegadinha:** Inverter requerido e fornecido.

**Como pensar:** Pergunte quem precisa do contrato e quem o realiza.


### Comentário S4D6Q268

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Diagrama não é teste nem garantia.
- **B)** Incorreta. A omissão impede análise do risco.
- **C)** Incorreta. Classe não localiza instâncias de execução.
- **D)** Correta. A vista apoia raciocínio, mas a evidência vem também de testes e operação.

**Conceito:** Implantação e qualidade.

**Pegadinha:** Tomar desenho de arquitetura como evidência suficiente.

**Como pensar:** Ligue topologia a requisito, mecanismo e teste.


### Comentário S4D6Q269

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Inverte as duas direções da rastreabilidade.
- **B)** Incorreta. Restringe a direção para frente e atribui à direção para trás um congelamento inexistente.
- **C)** Correta. As direções respondem a cobertura e pertinência.
- **D)** Incorreta. Impacto percorre dependências em ambas as direções.

**Conceito:** Rastreabilidade bidirecional.

**Pegadinha:** Decorar seta sem formular pergunta.

**Como pensar:** Pergunte “onde foi realizado?” e “por que existe?”.

### Comentário S4D6Q270

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A ordem e os elos não preservam justificativa.
- **B)** Correta. A cadeia vai da necessidade às vistas e evidências pertinentes.
- **C)** Incorreta. Uma classe monolítica não substitui as vistas.
- **D)** Incorreta. O oráculo deve nascer de necessidade aprovada.

**Conceito:** Cadeia integrada.

**Pegadinha:** Começar pelo artefato favorito.

**Como pensar:** Parta da necessidade e acrescente vistas somente pela pergunta.


### Comentário S4D6Q271

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Serviço não se reduz a ativo físico.
- **B)** Incorreta. Gestão trata riscos; não promete eliminação.
- **C)** Correta. O foco é habilitar resultado e valor no contexto.
- **D)** Incorreta. Saída sem resultado não define valor.

**Conceito:** Serviço e valor.

**Pegadinha:** Reduzir serviço a produto ou atividade interna.

**Como pensar:** Pergunte qual resultado o interessado consegue alcançar.


### Comentário S4D6Q272

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A ordem foi invertida.
- **B)** Incorreta. Não há interrupção nem causa.
- **C)** Incorreta. O contraste solicitado é de efeito da atividade.
- **D)** Correta. Relatório é produto da atividade; decisão melhor é efeito no interessado.

**Conceito:** Output e outcome.

**Pegadinha:** Usar “entrega” como sinônimo automático de valor.

**Como pensar:** Separe o produzido do efeito obtido.

### Comentário S4D6Q273

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Prolonga impacto e confunde incidente com problema.
- **B)** Incorreta. Pedido decorrente da interrupção não muda a natureza.
- **C)** Correta. Incidente busca restauração sem exigir causa definitiva.
- **D)** Incorreta. Urgência não elimina controle mínimo e aprendizado.

**Conceito:** Gestão de incidente.

**Pegadinha:** Exigir diagnóstico causal antes de restaurar.

**Como pensar:** Primeiro reduza impacto; preserve dados para aprender.


### Comentário S4D6Q274

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não é demanda predefinida do usuário.
- **B)** Incorreta. O reinício restaura temporariamente o serviço, mas não demonstra eliminação da causa recorrente.
- **C)** Correta. Ela reduz recorrência ao investigar causas e gerir contornos/erros conhecidos.
- **D)** Incorreta. Uma mudança pode implementar a solução, mas investigar a causa deve anteceder a alteração proposta.

**Conceito:** Gestão de problema.

**Pegadinha:** Confundir restauração com eliminação da causa.

**Como pensar:** Separe impacto atual de recorrência e causa.

### Comentário S4D6Q275

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não há interrupção não planejada.
- **B)** Incorreta. Não se investiga causa.
- **C)** Incorreta. A execução do pedido não é decisão de direção.
- **D)** Correta. É demanda normal e predefinida.

**Conceito:** Requisição de serviço.

**Pegadinha:** Chamar toda demanda de incidente.

**Como pensar:** Pergunte se é falha ou pedido normal.


### Comentário S4D6Q276

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Estabilidade depende de mudanças bem avaliadas, não congelamento.
- **B)** Incorreta. Controle deve ser proporcional ao risco.
- **C)** Correta. Mudança busca resultado controlado e proporcional.
- **D)** Incorreta. Correção técnica não elimina impacto ou reversão.

**Conceito:** Habilitação de mudança.

**Pegadinha:** Confundir controle com burocracia uniforme.

**Como pensar:** Relacione risco, autoridade, agenda, teste e reversão.


### Comentário S4D6Q277

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Problemas podem exigir várias equipes.
- **B)** Incorreta. Ponto de contato não substitui governança.
- **C)** Correta. A função facilita acesso e comunicação, sem absorver tudo.
- **D)** Incorreta. Prática/capacidade não é apenas software.

**Conceito:** Service desk.

**Pegadinha:** Reduzi-lo a ferramenta ou a resolvedor universal.

**Como pensar:** Identifique contato, comunicação, registro e encaminhamento.


### Comentário S4D6Q278

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Aquisição não prova benefício.
- **B)** Incorreta. Sem baseline e isolamento, resultado fica opaco.
- **C)** Incorreta. Saída isolada pode não representar valor.
- **D)** Correta. A melhoria liga direção, evidência e ajuste.

**Conceito:** Melhoria contínua.

**Pegadinha:** Começar pela solução favorita.

**Como pensar:** Defina onde está, onde quer chegar e como saberá.


### Comentário S4D6Q279

**Nível:** Difícil

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Inverte as finalidades.
- **B)** Correta. Cada prática conserva objetivo e conexão.
- **C)** Incorreta. Os conceitos não correspondem ao caso.
- **D)** Incorreta. O ciclo possui objetos e evidências diferentes.

**Conceito:** Práticas conectadas.

**Pegadinha:** Forçar um rótulo único para todo o ciclo.

**Como pensar:** Classifique cada objetivo no tempo.

### Comentário S4D6Q280

**Nível:** Médio

**Uso:** Aprofundamento

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Prioridade responde ao efeito no serviço.
- **B)** Incorreta. FIFO pode ignorar dano maior.
- **C)** Incorreta. Resolver o mais fácil não minimiza impacto.
- **D)** Incorreta. Governança pode definir critérios, mas pessoa isolada não substitui impacto.

**Conceito:** Priorização de incidentes.

**Pegadinha:** Confundir fila com prioridade.

**Como pensar:** Compare alcance, urgência e compromisso.


### Comentário S4D6Q281

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Monitoramento é responsabilidade central da governança.
- **B)** Correta. Preserva avaliação/direção/monitoramento e execução alinhada.
- **C)** Incorreta. Gestão toma decisões dentro da direção definida.
- **D)** Incorreta. O monitoramento integra a governança; a gestão planeja, executa e reporta sob a direção definida.

**Conceito:** Governança e gestão.

**Pegadinha:** Reduzir governança a aprovação ou gestão a operação cega.

**Como pensar:** Pergunte quem direciona e quem materializa.

### Comentário S4D6Q282

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O escopo é mais amplo.
- **B)** Correta. I&T empresarial apoia objetivos e envolve múltiplas partes.
- **C)** Incorreta. Governança é contínua, não evento isolado.
- **D)** Incorreta. Serviços, dados, riscos e decisões também entram.

**Conceito:** Escopo do COBIT.

**Pegadinha:** Confiná-lo à área técnica.

**Como pensar:** Observe a contribuição da I&T aos objetivos empresariais.


### Comentário S4D6Q283

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Atribui à governança o detalhamento e a execução que cabem à gestão.
- **B)** Incorreta. Inverte direção e execução.
- **C)** Incorreta. Auditoria oferece asseguração, não assume todos os papéis.
- **D)** Correta. Separa escolha institucional, implementação e retorno.

**Conceito:** Papéis no sistema de governança.

**Pegadinha:** Personificar o framework ou inverter papéis.

**Como pensar:** Siga avaliar/direcionar/monitorar versus planejar/construir/executar.


### Comentário S4D6Q284

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Nenhum é software.
- **B)** Correta. Os focos são distintos e complementares.
- **C)** Incorreta. Os referenciais não se excluem desse modo.
- **D)** Incorreta. A adoção não gera garantia automática.

**Conceito:** ITIL e COBIT.

**Pegadinha:** Procurar vencedor entre referenciais.

**Como pensar:** Compare foco, nível de decisão e integração.


### Comentário S4D6Q285

**Nível:** Difícil

**Uso:** Revisão

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Volume de práticas não prova efetividade.
- **B)** Correta. Referenciais orientam solução adequada à necessidade.
- **C)** Incorreta. Adaptação não significa ausência de estrutura.
- **D)** Incorreta. Ferramenta não define governança institucional.

**Conceito:** Adoção contextual.

**Pegadinha:** Confundir completude documental com adequação.

**Como pensar:** Comece por objetivos, risco, contexto e lacunas.


### Comentário S4D6Q286

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O objeto é o ciclo documental digital.
- **B)** Incorreta. CRM centra relacionamento e interações.
- **C)** Incorreta. ERP integra transações administrativas.
- **D)** Incorreta. BPM governa processo ponta a ponta, não substitui o repositório documental.

**Conceito:** Gestão eletrônica de documentos.

**Pegadinha:** Reduzi-lo a pasta ou confundi-lo com todo o processo.

**Como pensar:** Identifique documento, versão, metadado, acesso e retenção.

### Comentário S4D6Q287

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. GED guarda documentos, mas não define por si o fluxo completo.
- **B)** Correta. Ele roteia tarefas e estados segundo regras e papéis.
- **C)** Incorreta. CRM mantém relacionamento, não é o motor de tarefas por definição.
- **D)** Incorreta. ERP pode incorporar fluxo, mas sua finalidade nuclear é integração transacional.

**Conceito:** Roteamento de tarefas por workflow.

**Pegadinha:** Confundir sistema que contém workflow com a finalidade do conceito.

**Como pensar:** Procure fila, tarefa, estado, regra e papel.


### Comentário S4D6Q288

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Roteamento não inclui necessariamente análise e governança do processo.
- **B)** Incorreta. Notação representa, mas não executa toda disciplina.
- **C)** Incorreta. Documento não é o centro do problema.
- **D)** Correta. O ciclo vai de descoberta a melhoria contínua ponta a ponta.

**Conceito:** Gestão de processos de negócio.

**Pegadinha:** Reduzir BPM a desenho, notação ou software.

**Como pensar:** Procure ciclo, dono, resultado e melhoria.


### Comentário S4D6Q289

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. CRM foca relacionamento e interações.
- **B)** Incorreta. GED foca documentos.
- **C)** Incorreta. Fluxo pode apoiar, mas não define integração empresarial dos módulos.
- **D)** Correta. ERP integra processos e dados transacionais de áreas.

**Conceito:** Planejamento de recursos empresariais.

**Pegadinha:** Chamá-lo de banco único ou de qualquer sistema grande.

**Como pensar:** Procure módulos transacionais integrados.

### Comentário S4D6Q290

**Nível:** Médio

**Uso:** Revisão

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Transação administrativa não é o foco.
- **B)** Correta. O objeto é relacionamento e histórico de interações.
- **C)** Incorreta. Documentos podem estar ligados, mas não substituem histórico relacional.
- **D)** Incorreta. Notação não mantém relacionamento.

**Conceito:** Gestão do relacionamento com públicos.

**Pegadinha:** Reduzi-lo a vendas ou agenda.

**Como pensar:** Pergunte quem interagiu, por qual canal e com qual histórico.

### Comentário S4D6Q291

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Troca os objetos de ERP e CRM: cobrança é transação; contatos compõem relacionamento.
- **B)** Incorreta. Inverte workflow e BPM: um encaminha tarefas; o outro governa o resultado ponta a ponta.
- **C)** Correta. Cada recurso responde a objeto e finalidade próprios.
- **D)** Incorreta. Inverte GED e workflow: documento versionado não é o mesmo objeto que tarefa encaminhada.

**Conceito:** Integração de recursos.

**Pegadinha:** Escolher a maior plataforma como sinônimo de todas as capacidades.

**Como pensar:** Associe documento, tarefa, processo, transação e relacionamento.

### Comentário S4D6Q292

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A regra aparece em comportamento, estrutura e evidência.
- **B)** Incorreta. A classe não prova a decisão, e testar apenas acima do limite deixa fronteira e segregação sem evidência suficiente.
- **C)** Incorreta. Topologia não expressa sozinha a regra.
- **D)** Incorreta. O esperado deve anteceder a execução.

**Conceito:** Cadeia requisito–UML–teste.

**Pegadinha:** Tomar um artefato como substituto de todos.

**Como pensar:** Faça a regra atravessar vistas e casos de teste.


### Comentário S4D6Q293

**Nível:** Médio

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Contradição exige autoridade, consistência e rastreabilidade.
- **B)** Incorreta. Cronologia não define regra válida.
- **C)** Incorreta. Vistas podem ser parciais, não contraditórias na mesma regra.
- **D)** Incorreta. Isso oculta o defeito sem resolvê-lo.

**Conceito:** Resolução de inconsistência.

**Pegadinha:** Resolver pela artefato mais recente ou mais detalhado.

**Como pensar:** Volte à fonte e registre a decisão.


### Comentário S4D6Q294

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mantém o contrato externo sem revisão e omite regressão e evidência operacional.
- **B)** Incorreta. Preserva autorização incompatível e testa somente o caminho principal, sem os demais impactos.
- **C)** Incorreta. Segurança e dados não compensam a ausência de fonte, vistas consistentes e monitoramento posterior.
- **D)** Correta. Cobre origem, modelos, risco, teste e operação.

**Conceito:** Impacto transversal.

**Pegadinha:** Usar urgência para apagar dependências.

**Como pensar:** Siga requisito, vistas, segurança, teste, versão e operação.


### Comentário S4D6Q295

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Inverte responsabilidades e personifica o framework.
- **B)** Incorreta. Confunde objetivos e paralisa resposta.
- **C)** Incorreta. Serviço continua submetido à governança.
- **D)** Correta. Papéis e práticas permanecem distintos e conectados.

**Conceito:** Governança e serviço integrados.

**Pegadinha:** Misturar nível institucional e prática operacional.

**Como pensar:** Ordene direção, restauração, causa, mudança e monitoramento.


### Comentário S4D6Q296

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Valor depende do efeito no contexto, não só da produção.
- **B)** Incorreta. Confunde output com outcome.
- **C)** Incorreta. Resultados podem exigir medidas combinadas, não ausência de evidência.
- **D)** Incorreta. Não há interrupção de serviço descrita.

**Conceito:** Saída, resultado e valor.

**Pegadinha:** Premiar produtividade sem benefício.

**Como pensar:** Pergunte o que foi produzido e o que mudou para o interessado.


### Comentário S4D6Q297

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Separa objetos e corrige a causa ponta a ponta.
- **B)** Incorreta. Ciclo documental não decide desenho do processo.
- **C)** Incorreta. Automação pode acelerar desperdício.
- **D)** Incorreta. Disciplina não se reduz a produto.

**Conceito:** GED, workflow e BPM.

**Pegadinha:** Confundir digitalização/automação com melhoria.

**Como pensar:** Mapeie AS-IS, causa, TO-BE, dono e indicador.


### Comentário S4D6Q298

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 3 — Recursos informacionais

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Duplicação indiscriminada amplia inconsistência.
- **B)** Incorreta. Log não substitui idempotência nem reconciliação; uma repetição pode duplicar a transação.
- **C)** Incorreta. Aparência não prova contrato nem reconciliação.
- **D)** Correta. A integração precisa de consistência técnica, tratamento de falhas e responsabilidade definida.

**Conceito:** Integração CRM–ERP.

**Pegadinha:** Confundir proximidade visual com consistência.

**Como pensar:** Confira identidade, contrato, acesso, repetição, erro e reconciliação.


### Comentário S4D6Q299

**Nível:** Difícil

**Uso:** Simulado

**Bloco:** Bloco 2 — ITIL e COBIT

**Referência:** [Fundamentos de ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Duplicação não gera valor e ignora adaptação.
- **B)** Incorreta. Prática operacional não substitui direção.
- **C)** Incorreta. Governança não executa todas as práticas.
- **D)** Correta. Os referenciais se complementam sob desenho explícito.

**Conceito:** Uso complementar de referenciais.

**Pegadinha:** Somar documentos sem integrar responsabilidades.

**Como pensar:** Mapeie objetivo, decisão, prática, papel e medida.


### Comentário S4D6Q300

**Nível:** Muito difícil

**Uso:** Simulado

**Bloco:** Bloco 1 — Integração de Engenharia e UML

**Referência:** [Integração de requisitos, UML, testes e mudança](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Incidente em produção não substitui aceite, e gestão não define sozinha prioridades reservadas à governança.
- **B)** Incorreta. A cadeia de construção é plausível, mas a classificação da falha e a correção sem controle de mudança quebram a operação.
- **C)** Correta. A cadeia cobre origem, construção, operação, decisão e aprendizado.
- **D)** Incorreta. Classificação e controle estão incorretos.

**Conceito:** Integração da Semana 4.

**Pegadinha:** Escolher solução única para cadeia multidimensional.

**Como pensar:** Percorra necessidade, artefatos, recursos, evidência, operação e retorno.


#### Comentário Extra Dia 6.1

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Relação concessiva

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. `Como` introduz causa no período, não uma concessão.
- **B)** Incorreta. `Portanto` apresenta conclusão derivada da utilidade.
- **C)** Incorreta. `Mas` coordena uma relação adversativa, sem oração concessiva subordinada.
- **D)** Correta. `Embora` admite o primeiro fato e apresenta ressalva.

**Conceito:** Relação concessiva.

**Pegadinha:** Escolher conector pelo tom formal.

**Como pensar:** Substitua por “apesar de” e verifique o sentido.

#### Comentário Extra Dia 6.2

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Relação causal entre orações

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A demora é causa apresentada para a revisão.
- **B)** Incorreta. `Embora` introduz concessão, não apresenta a demora como causa da revisão.
- **C)** Incorreta. `Contudo` marca oposição entre fatos, não a relação causal solicitada.
- **D)** Incorreta. A conclusão está sintaticamente formada, mas inverte a direção de causa e consequência.

**Conceito:** Relação causal entre orações.

**Pegadinha:** Confundir causa, contraste e conclusão.

**Como pensar:** Nomeie premissa e efeito antes do conector.

#### Comentário Extra Dia 6.3

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Concordância integrada

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. `Haver` existencial fica no singular e `faltar` deve ir ao plural.
- **B)** Incorreta. `Há` está correto, mas `exige` e `falta` deveriam concordar com os sujeitos plurais.
- **C)** Correta. `Há` é impessoal; `faltam` concorda com `equipes`; o referente é claro.
- **D)** Incorreta. A locução existencial deveria ser `deve haver`, e `faltam` não concorda com `equipe` no singular.

**Conceito:** Concordância integrada.

**Pegadinha:** Aplicar plural ao verbo mais próximo.

**Como pensar:** Localize impessoalidade, sujeito de cada verbo e referente.

#### Comentário Extra Dia 6.4

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Negação de universal

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A afirmação é mais forte que o enunciado.
- **B)** Correta. É a negação do universal.
- **C)** Incorreta. Não há quantidade exata.
- **D)** Incorreta. O enunciado não informa parcialidade.

**Conceito:** Negação de universal.

**Pegadinha:** Transformar `nem todas` em `nenhuma`.

**Como pensar:** Formalize `não é verdade que todas`.

#### Comentário Extra Dia 6.5

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Restrição e explicação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Somente I seleciona o subconjunto de alto volume; II caracteriza o conjunto referido.
- **B)** Correta. A pontuação altera o alcance da oração relativa.
- **C)** Incorreta. Inverte as leituras restritiva de I e explicativa de II.
- **D)** Incorreta. As vírgulas mudam o alcance semântico, não apenas o ritmo de leitura.

**Conceito:** Restrição e explicação.

**Pegadinha:** Tratar vírgula como pausa sem efeito semântico.

**Como pensar:** Pergunte se a oração seleciona parte ou comenta o conjunto.


#### Comentário Extra Dia 6.6

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Referência pronominal

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O pronome em `revisá-la` ainda pode retomar `análise` ou `diretoria`.
- **B)** Incorreta. Altera o agente e o sentido.
- **C)** Correta. A ordem e o objeto ficam inequívocos.
- **D)** Incorreta. Muda quem realizou a revisão.

**Conceito:** Referência pronominal.

**Pegadinha:** Acreditar que gênero sozinho resolve todo antecedente.

**Como pensar:** Explicite agente e objeto quando houver concorrência.

#### Comentário Extra Dia 6.7

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Paralelismo sintático e semântico

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Alterna infinitivos com sintagmas nominais na mesma série de ações.
- **B)** Incorreta. Também mistura substantivos e infinitivos, embora mantenha o tema dos quatro itens.
- **C)** Incorreta. Alterna orações desenvolvidas e infinitivos sem uma forma coordenada comum.
- **D)** Correta. Quatro verbos no infinitivo descrevem ações coordenadas.

**Conceito:** Paralelismo sintático e semântico.

**Pegadinha:** Ver apenas terminações semelhantes.

**Como pensar:** Confira forma gramatical e papel de cada item.

#### Comentário Extra Dia 6.8

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Modalização proporcional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Mantém absoluto.
- **B)** Incorreta. A modalização elimina precisão.
- **C)** Correta. Modula a afirmação e explicita condições.
- **D)** Incorreta. Confunde ausência de garantia com ausência de contribuição.

**Conceito:** Modalização proporcional.

**Pegadinha:** Trocar certeza por vagueza total.

**Como pensar:** Use possibilidade com mecanismo e condição.


#### Comentário Extra Dia 6.9

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Reescrita integrada

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Há causa, referente claro, concordância e modalização.
- **B)** Incorreta. A frase é gramatical e modalizada, mas troca a relação causal original por concessão.
- **C)** Incorreta. `Analisar` pede objeto direto; `lhes` não retoma corretamente `as manifestações` nessa função.
- **D)** Incorreta. `Revelou` não concorda com `manifestações`, e `eliminam` transforma possibilidade em resultado garantido.

**Conceito:** Reescrita integrada.

**Pegadinha:** Premiar alternativa mais enfática.

**Como pensar:** Cheque sintaxe, referente, conector e grau de certeza.


#### Comentário Extra Dia 6.10

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Pontuação de termo intercalado

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Falta vírgula após a oração adverbial antecipada, e a vírgula usada separa sujeito e verbo.
- **B)** Incorreta. As vírgulas isolam indevidamente a preposição e rompem a locução infinitiva `após examinar`.
- **C)** Incorreta. Falta vírgula após o adjunto adverbial antecipado, e a vírgula usada separa `apresentou` de seu objeto.
- **D)** Correta. As vírgulas delimitam termo intercalado.

**Conceito:** Pontuação de termo intercalado.

**Pegadinha:** Pontuar pela pausa oral apenas.

**Como pensar:** Retire a intercalação e confira a oração-base.

#### Comentário Extra Dia 6.11

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Correlação verbal e sequência

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Tempos, agente, sequência e limite da conclusão são coerentes.
- **B)** Incorreta. Mistura mais-que-perfeito, futuro do pretérito e pretérito sem sequência coerente e ainda absolutiza a conclusão.
- **C)** Incorreta. A construção é gramatical, mas transforma resultados em prova universal de que toda mudança melhora.
- **D)** Incorreta. Mantém agentes identificáveis, porém mede resultados antes de implementar as mudanças cujo efeito seria avaliado.

**Conceito:** Correlação verbal e sequência.

**Pegadinha:** Aceitar uma sequência plausível com tempos incompatíveis.

**Como pensar:** Marque agente, linha do tempo, forma verbal e alcance da conclusão.


#### Comentário Extra Dia 6.12

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Gerúndio e ambiguidade

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Faz a incompletude ocorrer durante o envio, em vez de marcar o estado anterior do relatório.
- **B)** Correta. Explicita o estado prévio e separa as ações.
- **C)** Incorreta. Afirma que o envio tornou o relatório incompleto, alterando a relação temporal dada.
- **D)** Incorreta. Troca agente e paciente.

**Conceito:** Gerúndio e ambiguidade.

**Pegadinha:** Deixar o gerúndio sugerir causa ou simultaneidade indevida.

**Como pensar:** Explicite tempo, agente e estado do objeto.


#### Comentário Extra Dia 6.13

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Concisão com preservação

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Retira repetição e conserva ação, objeto e limite temporal.
- **B)** Incorreta. Repete núcleos sem acrescentar sentido.
- **C)** Incorreta. Elimina também a condição de prazo.
- **D)** Incorreta. Mantém redundância temporal em “antecipado previamente”.

**Conceito:** Concisão com preservação.

**Pegadinha:** Cortar informação essencial em nome da concisão.

**Como pensar:** Remova duplicação, não condição relevante.

#### Comentário Extra Dia 6.14

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Paralelismo argumentativo

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Alterna infinitivo, sintagma nominal e novo infinitivo.
- **B)** Incorreta. Alterna sintagma nominal, infinitivo e outro sintagma nominal.
- **C)** Incorreta. Combina dois sintagmas de núcleo nominal com um infinitivo.
- **D)** Correta. Três sintagmas nominais representam critérios.

**Conceito:** Paralelismo argumentativo.

**Pegadinha:** Olhar só a terminação das palavras.

**Como pensar:** Compare forma e categoria de cada critério.

#### Comentário Extra Dia 6.15

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Preservação semântica

**Nível:** Muito difícil

**Uso:** Revisão

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Preserva negação e condição, mas troca possibilidade por garantia de correção absoluta.
- **B)** Incorreta. Mantém possibilidade e condição, porém afirma que a escuta pode substituir a decisão.
- **C)** Correta. Mantém todos os cinco componentes de sentido.
- **D)** Incorreta. Mantém negação, contraste e referente, mas elimina a condição de análise e resposta.

**Conceito:** Preservação semântica.

**Pegadinha:** Conservar tema, mas inverter operador lógico.

**Como pensar:** Liste negação, contraste, modal, referente e condição.


#### Comentário Extra Dia 6.16

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Progressão textual

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cada período retoma e avança a cadeia causal.
- **B)** Incorreta. Mede um prazo novo antes do diagnóstico e só depois revê o fluxo, invertendo a cadeia de intervenção e efeito.
- **C)** Incorreta. Faz o diagnóstico que justificaria a revisão surgir apenas depois da medição do resultado dessa revisão.
- **D)** Incorreta. Conclui que a medição provocou uma revisão situada antes da própria mudança medida.

**Conceito:** Progressão textual.

**Pegadinha:** Confundir repetição temática com encadeamento.

**Como pensar:** Pergunte o que cada frase retoma e acrescenta.


#### Comentário Extra Dia 6.17

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Regência e crase

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A relação entre complementos foi invertida e falta crase no segundo.
- **B)** Correta. Os verbos regem complementos com `a`, combinados com artigos femininos.
- **C)** Incorreta. Não cabe crase antes de artigo indefinido nem, em regra, antes de `todas` assim usado.
- **D)** Incorreta. Há crase indevida no objeto direto e ausência no complemento regido.

**Conceito:** Regência e crase.

**Pegadinha:** Aplicar crase diante de qualquer palavra feminina.

**Como pensar:** Teste a preposição exigida e o artigo admitido.

#### Comentário Extra Dia 6.18

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Desenvolvimento da tese

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Abandona a tese.
- **B)** Incorreta. Contradiz a posição sem justificativa.
- **C)** Correta. Retoma os dois critérios e os desenvolve causalmente.
- **D)** Incorreta. Repetição não produz desenvolvimento.

**Conceito:** Desenvolvimento da tese.

**Pegadinha:** Escolher texto sobre o tema, mas sem sustentar os eixos.

**Como pensar:** Associe cada parágrafo a um critério da tese.


#### Comentário Extra Dia 6.19

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Conclusão dissertativa

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Introduz solução nova e usa absolutos.
- **B)** Incorreta. Retoma resposta, mas abandona o eixo de avaliação que condicionava a melhoria.
- **C)** Incorreta. Contradiz a tese ao separar escuta e necessidade real da decisão pública.
- **D)** Correta. Retoma os critérios, sintetiza e modula o efeito.

**Conceito:** Conclusão dissertativa.

**Pegadinha:** Usar impacto retórico para inserir proposta inédita.

**Como pensar:** Retome tese e critérios com consequência proporcional.


#### Comentário Extra Dia 6.20

**Dia:** Dia 6

**Bloco:** Bloco 5 — Português e dissertação integral

**Matéria:** Português

**Assunto:** Revisão do texto integral

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português dos Blocos 4–5](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Revê parte da estrutura global, mas abandona sintaxe e sentido e troca precisão por preciosismo vocabular.
- **B)** Correta. O protocolo percorre critérios globais e locais com produto verificável.
- **C)** Incorreta. Cobre aspectos locais, mas deixa tese, argumentos e conclusão fora da revisão.
- **D)** Incorreta. Conclusão não deve abrir eixo não desenvolvido.

**Conceito:** Revisão do texto integral.

**Pegadinha:** Reduzir revisão a caça de erros gráficos.

**Como pensar:** Revise do macrotema ao período e finalize com reescrita concreta.
