# Banco de Questões — Semana 4

**Período:** 03/08/2026 a 08/08/2026.
**Cargo:** Analista de Sistemas.
**Banca de referência:** Instituto Consulplan.
**Status:** **Material aprovado para execução**; execução do candidato pendente.

Este banco reúne **420 questões autorais**, todas com quatro alternativas (`A–D`) e comentário integral: **300 principais**, cinquenta por dia, e **120 extras**, vinte por dia. Questões oficiais não são copiadas para cá; o índice de aplicação no caderno original está em [questões oficiais da Semana 4](../questoes_oficiais/semana_04.md).

## Como usar sem antecipar conteúdo

1. estude Blocos 1–3 e conclua o produto prático do dia;
2. em D0, resolva as seis primeiras Essenciais; avance até a décima apenas com tempo para corrigir A–D;
3. use Aprofundamento depois da teoria; abra Revisão no ciclo D+7 e Simulado no ciclo reservado;
4. use as cinco extras Essenciais de cada dia na reabertura D+7 da matéria fixa;
5. registre resposta, tempo e confiança antes do gabarito;
6. explique por que a correta atende ao comando e por que cada distrator falha antes de ler o comentário.

## Identificação e filas

| Conjunto | IDs | Uso planejado |
|---|---|---|
| Principais do Dia 1 | S4D1Q001–S4D1Q050 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 2 | S4D2Q051–S4D2Q100 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 3 | S4D3Q101–S4D3Q150 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 4 | S4D4Q151–S4D4Q200 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 5 | S4D5Q201–S4D5Q250 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Principais do Dia 6 | S4D6Q251–S4D6Q300 | 10 Essenciais, 20 Aprofundamento, 10 Revisão e 10 Simulado |
| Extras de cada dia | Extra Dia N.1–N.20 | 5 Essenciais, 5 Aprofundamento, 5 Revisão e 5 Simulado |

`Nível` descreve esforço cognitivo real, não cota. `Uso` controla o momento de abertura e não equivale a dificuldade.

## Critério de construção no estilo da banca

Os itens alternam conceito direto, assertivas, associação, cenário de órgão público, seleção de artefato UML, análise de consequência e identificação do detalhe discriminador. O objetivo não é reproduzir frases de provas: é treinar leitura integral do comando, alternativas plausíveis do mesmo domínio, distinção entre artefatos próximos e integração moderada entre requisito, modelo, processo, teste e controle.

Comandos negativos (`INCORRETA`, `EXCETO`, `NÃO`) ficam visualmente claros e o comentário registra a inversão. Detalhes dependentes de edição ou ferramenta são delimitados; o banco não transforma uma particularidade de produto em regra universal. Cada referência aponta para teoria anterior e suficiente da própria semana ou para revisão fixa já estudada.

## Distribuição das extras

| Dia | Revisão fixa que sustenta as vinte extras |
|---:|---|
| 1 | Legislação CRA/CFA e Português |
| 2 | Administração Pública e Português |
| 3 | Legislação CRA/CFA e Português |
| 4 | Administração Pública e RLM |
| 5 | Legislação CRA/CFA e Português |
| 6 | Português; o Bloco 6 apenas recupera erros e não cria lista objetiva nova |

## Regra para o caderno de erros

Para erro ou acerto inseguro, registre ID, tema, causa, regra decisiva, alternativa escolhida, motivo da plausibilidade, contraexemplo e datas D+2/D+7/D+21. Na reabertura, cubra as alternativas e reconstrua a regra: não memorize a letra.

# Dia 1 — Requisitos, análise orientada a objetos e casos de uso

## Questões principais

### S4D1Q001 — Necessidade e requisito

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Necessidade, requisito, regra, restrição e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

A direção quer reduzir o prazo médio dos protocolos, mas ainda não definiu capacidades do sistema. Essa declaração é, predominantemente:

A) um requisito funcional completo, pois contém um indicador.
B) um objetivo ou necessidade de negócio a decompor em requisitos verificáveis.
C) uma restrição tecnológica, pois limita a arquitetura disponível.
D) um caso de uso, pois identifica interação entre ator e sistema.

### S4D1Q002 — Comportamento funcional

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

No portal do CRA, qual enunciado descreve requisito funcional em vez de atributo de qualidade?

A) O serviço deve permanecer disponível em 99,5% da janela mensal acordada.
B) A interface deve atender aos critérios de acessibilidade estabelecidos no projeto.
C) O sistema deve permitir ao interessado consultar o andamento pelo número do protocolo.
D) A consulta deve responder em até dois segundos no cenário de carga definido.

### S4D1Q003 — Qualidade mensurável

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

Assinale o requisito de desempenho que possui condição de verificação suficiente.

A) Durante a operação normal, as telas devem responder de modo satisfatório aos usuários.
B) Sob a carga usual, o sistema deve ser rápido nas consultas consideradas mais importantes.
C) No ambiente de homologação, o sistema deve apresentar o melhor desempenho possível.
D) No ambiente definido, com 200 consultas de protocolo simultâneas, 95% devem responder em até dois segundos.

### S4D1Q004 — Regra de negócio e derivação

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Necessidade, requisito, regra, restrição e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

A regra “somente servidor designado pode assinar o despacho” foi confirmada. Qual tratamento é mais adequado?

A) Converter a frase diretamente em uma tela de login e encerrar a análise.
B) Registrar a regra e derivar autorização, dados de designação e critérios.
C) Tratar a frase apenas como requisito de desempenho do módulo de assinatura.
D) Delegar ao banco de dados a escolha autônoma de quem pode assinar.

### S4D1Q005 — Requisito composto e rastreável

**Nível:** Muito difícil

**Uso:** Essenciais

**Referência:** [Exemplos resolvidos — qualidade e aceitação](semana_04_estudo.md#s4-d1-exemplos-qualidade).

O rascunho único determina receber pedido, validar anexos, calcular taxa e notificar. A equipe precisa priorizar, testar e controlar mudanças separadamente. Qual revisão é mais consistente?

A) Decompor os quatro comportamentos, manter suas dependências e ligar cada um a critérios e à origem comum.
B) Eliminar as dependências para que cada requisito possa mudar sem análise de impacto.
C) Substituir os verbos por um requisito genérico de usabilidade do protocolo.
D) Manter uma frase indivisível e criar um único teste de sucesso para todo o fluxo.

### S4D1Q006 — Restrição de solução

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

A organização determina que o novo módulo use o provedor institucional de identidade já homologado. O enunciado expressa:

A) uma restrição que limita alternativas de solução e cria requisito de interface.
B) um caso de uso completo, com ator, fluxo e pós-condição.
C) um objetivo de negócio sem consequência para a solução.
D) um requisito de usabilidade sobre a facilidade de autenticação.

### S4D1Q007 — Critério de aceitação

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

Para o requisito “apenas analistas designados podem decidir”, qual critério cobre adequadamente os dois lados da regra?

A) Todo usuário autenticado consegue abrir a tela de decisão.
B) O analista designado visualiza seu nome no cabeçalho.
C) A equipe confirma verbalmente que o controle parece seguro.
D) Designado: decisão registrada; não designado: bloqueio sem decisão.

### S4D1Q008 — Qualidade de requisito — comando negativo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

Sobre características de um bom requisito, assinale a alternativa **INCORRETA**.

A) Ser consistente exige não contradizer requisitos válidos do conjunto.
B) Ser necessário liga o requisito a objetivo, obrigação ou valor justificável.
C) Ser verificável permite obter evidência objetiva de atendimento.
D) Ser rastreável significa permanecer imutável depois de aprovado.

### S4D1Q009 — Mapa de interessados

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

Ao identificar interessados para um serviço de protocolo, a equipe deve:

A) mapear componentes internos como se cada módulo fosse, por si só, uma parte interessada.
B) mapear usuários, decisores, equipes de apoio, responsáveis por integrações e pessoas afetadas.
C) mapear somente quem opera a interface, excluindo equipes de apoio e pessoas afetadas.
D) mapear apenas a autoridade de maior nível, sem considerar conhecimento ou impacto distribuído.

### S4D1Q010 — Diagnóstico de requisitos integrado

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

Considere: I. “A consulta deve ser intuitiva”; II. a fonte não foi registrada; III. o requisito contradiz regra vigente; IV. não existe método definido capaz de produzir evidência objetiva. Qual diagnóstico associa corretamente os quatro defeitos?

A) I viola apenas prioridade; II viola desempenho; III viola singularidade; IV viola origem.
B) I é funcional completo; II é irrelevante; III pode ser ignorado; IV prova viabilidade.
C) I falta critério mensurável; II perde rastreabilidade; III viola consistência; IV viola verificabilidade.
D) I é caso de uso; II é restrição; III é protótipo; IV é requisito derivado.

### S4D1Q011 — Observação na elicitação

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

Para descobrir atalhos e exceções do trabalho que não aparecem no manual, a técnica mais diretamente útil é:

A) ler apenas o manual e assumir que toda prática coincide com ele.
B) construir a solução antes de consultar quem executa o processo.
C) observar o trabalho real e depois confirmar a legitimidade das variações.
D) usar somente questionário fechado com alternativas já definidas.

### S4D1Q012 — Entrevista preparada

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

Em entrevista com especialista, qual sequência aumenta a qualidade da evidência?

A) Definir objetivo, estudar contexto, explorar exemplos e exceções, resumir e confirmar o entendimento.
B) Limitar-se a perguntas binárias e tratar silêncio como aprovação formal.
C) Começar pela solução escolhida, buscar concordância e omitir objeções do registro.
D) Fazer perguntas sem objetivo, encerrar sem síntese e completar lacunas por intuição.

### S4D1Q013 — Oficina — comando negativo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — elicitação](semana_04_estudo.md#s4-d1-exemplos-elicitacao).

Sobre uma oficina para resolver conflito entre atendimento e fiscalização, assinale a alternativa **INCORRETA**.

A) A votação por maioria dispensa registrar obrigação, risco e autoridade decisória.
B) A facilitação deve tornar explícitos objetivos, divergências e critérios.
C) As decisões e questões abertas precisam de responsável e registro.
D) Alternativas como preenchimento progressivo podem ser avaliadas por impacto.

### S4D1Q014 — Triangulação de fontes

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — elicitação](semana_04_estudo.md#s4-d1-exemplos-elicitacao).

Manual e prática observada divergem sobre exceções do protocolo. A conduta adequada é:

A) automatizar toda exceção observada, pois prática repetida cria regra válida.
B) eliminar o fluxo oficial e manter somente a versão mais fácil de implementar.
C) registrar a divergência, entrevistar envolvidos e levar a exceção ao dono do processo para decisão.
D) adotar o manual sem examinar a operação, pois documento sempre prevalece como requisito.

### S4D1Q015 — Elicitação e análise em conflito

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

Fiscalização exige cinco anexos no protocolo; atendimento quer um campo mínimo; a norma exige dois na entrada e três antes da decisão. Qual solução analítica é mais defensável?

A) Fazer todos os anexos opcionais e deixar cada servidor escolher no momento.
B) Exigir cinco na entrada porque a área mais rigorosa reduz qualquer risco.
C) Aceitar apenas um campo em todas as etapas porque melhora o tempo de fila.
D) Exigir dois na entrada e três antes da decisão, com completude progressiva e fonte rastreada.

### S4D1Q016 — Detecção de duplicidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Análise, modelagem e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

Dois requisitos usam “solicitante” e “interessado” para o mesmo papel, mas possuem critérios diferentes. Antes de uni-los, a equipe deve:

A) confirmar equivalência, comparar critérios e preservar diferenças.
B) fundir os textos pelo nome mais curto e apagar a origem anterior.
C) manter duplicação deliberada para aumentar o número de requisitos.
D) escolher o requisito com identificador numérico mais recente.

### S4D1Q017 — Controle de escopo

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — análise e priorização](semana_04_estudo.md#s4-d1-exemplos-analise).

Num projeto de consulta de protocolo, surge pedido para substituir todo o financeiro. A primeira decisão correta é:

A) ignorar o pedido sem registro porque ele parece grande.
B) comparar com o objetivo e a fronteira, registrar e separar o excedente.
C) interromper a consulta até que o financeiro seja integralmente refeito.
D) incluir toda a substituição porque o pedido veio de interessado.

### S4D1Q018 — Priorização multicritério

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Análise, modelagem e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

Uma adequação obrigatória vence em 30 dias; um relatório depende dela; uma troca visual possui alto apelo. Qual priorização é justificável?

A) usar somente a ordem de chegada e não registrar justificativa.
B) considerar obrigação, prazo, risco e dependência antes do apelo visual.
C) priorizar o tema visual porque recebeu mais mensagens dos usuários.
D) priorizar o relatório antes da base de que depende.

### S4D1Q019 — Especificação com atributos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

Além do texto do requisito, qual conjunto apoia gestão e validação?

A) Cor da tela, linguagem escolhida e nome do programador, obrigatoriamente.
B) Apenas número sequencial e data de criação.
C) Somente assinatura do patrocinador, sem critérios técnicos.
D) Identificador, fonte, justificativa, prioridade, estado, critérios e relações.

### S4D1Q020 — Cadeia de requisitos completa

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

Um requisito de notificação veio da obrigação de ciência, aparece no caso “Decidir requerimento”, é implementado por serviço e verificado por teste. A obrigação muda. Qual análise é completa?

A) Modificar apenas o serviço e manter documentação para preservar a baseline.
B) Apagar a ligação com a obrigação para impedir que futuras mudanças se propaguem.
C) Percorrer obrigação → requisito → caso → serviço → teste; decidir e versionar o impacto.
D) Alterar somente o teste, pois ele é o último elo e corrige os anteriores.

### S4D1Q021 — Validação de necessidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

A validação de requisitos procura principalmente confirmar se:

A) o artefato segue o padrão documental e não contém contradições internas.
B) cada requisito possui identificador único e redação conforme o modelo adotado.
C) o conjunto expressa as necessidades corretas dentro do escopo.
D) a implementação reproduz fielmente as decisões técnicas de projeto.

### S4D1Q022 — Verificação e validação — comando negativo

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

Assinale a alternativa **INCORRETA** sobre verificação e validação de requisitos.

A) A consistência com o modelo prova, sozinha, que o usuário necessita da solução descrita.
B) A verificação pode examinar clareza, consistência e conformidade do artefato.
C) A validação pode usar protótipos, cenários e revisão com interessados.
D) Um requisito pode ser bem escrito e ainda representar a necessidade errada.

### S4D1Q023 — Limite do protótipo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — validação, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-exemplos-validacao).

Usuários aprovaram a aparência do protótipo, mas carga, autorização e falhas não foram exercitadas. Conclui-se que:

A) requisitos de segurança deixam de existir após aceite de usabilidade.
B) o protótipo prova viabilidade de produção sob qualquer carga.
C) a evidência valida aspectos de interação, não as qualidades e exceções ausentes.
D) todo o sistema está validado porque as telas receberam aprovação.

### S4D1Q024 — Baseline controlada

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

Após aprovar uma baseline, surge mudança justificada. O procedimento adequado é:

A) criar requisito paralelo sem ligação com a versão anterior.
B) editar silenciosamente o texto para evitar burocracia.
C) rejeitar automaticamente toda mudança posterior.
D) registrar, analisar impacto, decidir, versionar e comunicar.

### S4D1Q025 — Impacto multifiltro

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — validação, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-exemplos-validacao).

Uma nova regra encurta prazo e muda quem pode recorrer. Há requisito, caso de uso, estado, mensagens, serviço e testes relacionados. Qual plano reduz melhor a omissão?

A) Alterar o número do prazo em uma tela e considerar a mudança concluída.
B) Confirmar fonte, seguir vínculos, avaliar estados e permissões e atualizar os artefatos aprovados.
C) Atualizar somente o requisito porque modelos e testes são consequências automáticas.
D) Apagar o histórico anterior para impedir interpretações divergentes.

### S4D1Q026 — Rastreabilidade bidirecional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

Ao partir de um requisito selecionado, qual pergunta é respondida pela rastreabilidade para trás?

A) Qual objetivo, fonte ou regra justifica este requisito?
B) Quais requisitos posteriores dependem deste requisito?
C) Quais artefatos deverão ser revistos se este requisito mudar?
D) Quais testes e componentes realizam este requisito?

### S4D1Q027 — Requisito derivado

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

A obrigação de responsabilizar alterações leva à necessidade de guardar autor, instante e versão. Esses requisitos são:

A) casos de uso autônomos obrigatórios em qualquer sistema.
B) derivados da obrigação e precisam manter ligação com ela.
C) independentes de qualquer fonte porque foram propostos pela TI.
D) apenas detalhes de interface sem valor para o domínio.

### S4D1Q028 — Consistência entre requisitos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

R1 diz que todo protocolo exige autenticação; R2 permite consulta pública anônima do andamento. Antes de declarar conflito, a equipe deve:

A) apagar R2 porque anonimato sempre invalida segurança.
B) apagar R1 porque consulta pública torna toda autenticação inútil.
C) manter ambos sem esclarecer objeto, pois contradição ajuda testes.
D) delimitar operações e dados, pois as frases podem tratar escopos distintos.

### S4D1Q029 — Viabilidade — comando negativo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

Na análise de viabilidade de requisito, assinale a alternativa **INCORRETA**.

A) Prototipação pode reduzir incerteza técnica sem validar todo o produto.
B) Uma alternativa pode preservar o objetivo quando a solução inicial é inviável.
C) Custo, prazo, tecnologia e competências podem afetar a viabilidade.
D) Se o requisito tem alto valor, limitações técnicas e legais podem ser ignoradas.

### S4D1Q030 — Conflito, prioridade e rastreabilidade

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — análise e priorização](semana_04_estudo.md#s4-d1-exemplos-analise).

Dois requisitos disputam capacidade: A atende obrigação iminente e habilita C; B melhora conveniência, mas não possui dependências. Há risco técnico alto em A. À luz da priorização multicritério e da rastreabilidade, qual decisão é mais justificável?

A) Dividir igualmente o tempo sem avaliar se qualquer entrega fica utilizável.
B) Priorizar B porque é tecnicamente mais simples e ocultar a obrigação.
C) Priorizar A, mitigar o risco, registrar a dependência de C e justificar o adiamento de B.
D) Priorizar C antes de A para entregar valor visual, embora C dependa de A.

### S4D1Q031 — Análise OO e projeto

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

Na análise orientada a objetos, o foco predominante é:

A) escolher índices e formato físico de todas as tabelas.
B) compreender conceitos, responsabilidades e colaborações do domínio.
C) fixar framework, servidor e biblioteca de interface.
D) converter cada tela existente em classe obrigatória.

### S4D1Q032 — Classe e objeto

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

Assinale a distinção correta entre classe e objeto.

A) Classe descreve características comuns; objeto é ocorrência com identidade e estado.
B) Classe existe apenas em banco; objeto existe apenas na interface.
C) Classe e objeto são sinônimos quando possuem os mesmos atributos.
D) Classe é valor corrente; objeto é o conjunto de regras de todos os tipos.

### S4D1Q033 — Responsabilidade e coesão

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — análise orientada a objetos](semana_04_estudo.md#s4-d1-exemplos-oo).

Uma classe central autentica, calcula prazo, gera documento e envia e-mail. O primeiro diagnóstico é:

A) encapsulamento completo porque há uma única classe pública.
B) alta coesão porque todas as operações usam computador.
C) baixa coesão por reunir responsabilidades com razões distintas para mudar.
D) generalização adequada porque a classe possui muitos métodos.

### S4D1Q034 — Abstração e encapsulamento — comando negativo

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

Sobre abstração e encapsulamento, assinale a alternativa **INCORRETA**.

A) Abstrair é selecionar propriedades relevantes ao propósito do modelo.
B) Encapsular permite ocultar representação atrás de responsabilidades.
C) Encapsular significa concentrar toda regra do sistema em uma única classe privada.
D) O nível de detalhe adequado depende da pergunta respondida pelo modelo.

### S4D1Q035 — Modelo de domínio integrado

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — análise orientada a objetos](semana_04_estudo.md#s4-d1-exemplos-oo).

No texto “Profissional envia Requerimento; Protocolo registra data; Servidor profere Despacho”, qual modelagem inicial é mais sólida?

A) Criar somente Sistema com todos os atributos e métodos para evitar associações.
B) Converter cada palavra iniciada por maiúscula em classe definitiva.
C) Criar classes Enviar, Registrar e Proferir porque todo verbo representa entidade.
D) Tratar conceitos como candidatos, explorar vínculos pelos verbos e validar o vocabulário.

### S4D1Q036 — Associação e generalização

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

“Fiscal é um Servidor e analisa Processo” sugere, respectivamente:

A) generalização entre Fiscal e Servidor e associação entre Fiscal e Processo.
B) dependência de Servidor para Fiscal e herança de Processo.
C) duas composições, pois as frases possuem verbos.
D) duas generalizações, pois Fiscal participa das duas relações.

### S4D1Q037 — Candidato a classe

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

Qual elemento é o candidato mais forte a classe de domínio no cenário de protocolo?

A) Prazo, quando representado apenas como duração sem identidade própria.
B) TelaDeCadastro, quando existe apenas como detalhe da solução nesse recorte.
C) Requerimento, por ter identidade, estado e regras próprias.
D) NúmeroDoProtocolo, quando funciona apenas como valor identificador do requerimento.

### S4D1Q038 — Acoplamento

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

Para reduzir acoplamento entre protocolo e notificação, sem perder a obrigação de comunicar, a modelagem deve:

A) remover qualquer interação e também a obrigação de notificar.
B) expor todos os atributos internos do notificante para acesso direto.
C) copiar toda a lógica de notificação para dentro de Protocolo.
D) definir contrato estável e ocultar detalhes internos do notificante.

### S4D1Q039 — Ator — comando negativo

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

Sobre atores em casos de uso, assinale a alternativa **INCORRETA**.

A) O mesmo papel pode ser desempenhado por várias pessoas.
B) Todo ator precisa ser uma pessoa física identificada nominalmente.
C) Uma pessoa pode exercer papéis de ator distintos.
D) Outro sistema pode atuar como ator de apoio.

### S4D1Q040 — Fronteira e sistema externo

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — casos de uso](semana_04_estudo.md#s4-d1-exemplos-casos).

O Portal é o sistema modelado e usa provedor externo de identidade; seu banco faz parte do Portal. Qual representação é coerente?

A) Provedor e banco são atores porque ambos são tecnologias.
B) Portal é ator de si próprio e todos os casos ficam fora da fronteira.
C) Provedor é ator externo; casos ficam dentro; banco interno não é ator.
D) Banco é ator primário e o interessado é classe interna.

### S4D1Q041 — Objetivo de caso de uso

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

Qual nome representa melhor um caso de uso orientado a objetivo?

A) Banco de protocolos.
B) Passo 3: clicar em avançar.
C) Consultar andamento do protocolo.
D) Botão azul de consulta.

### S4D1Q042 — Precondição

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

No caso “Consultar dados restritos”, a frase “o interessado já está autenticado” é:

A) generalização obrigatória de todo caso de uso.
B) pós-condição de sucesso, pois aparece antes da resposta.
C) ator secundário, pois autenticação interage com o sistema.
D) precondição, se o caso apenas assume esse estado ao começar.

### S4D1Q043 — Pós-condição

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

Qual frase é uma pós-condição verificável de sucesso de “Protocolar requerimento”?

A) O requerimento fica registrado com número, instante e autor.
B) O usuário deseja que tudo funcione corretamente.
C) O sistema é moderno e amigável.
D) O interessado deve estar autenticado antes de iniciar.

### S4D1Q044 — Fluxo alternativo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplos resolvidos — fluxos e condições](semana_04_estudo.md#s4-d1-exemplos-fluxos).

Durante “Protocolar requerimento”, anexo inválido leva à solicitação de correção. A melhor descrição é:

A) fluxo alternativo ligado ao passo de validação.
B) generalização do interessado.
C) pós-condição de sucesso do protocolo.
D) novo ator chamado AnexoInválido.

### S4D1Q045 — Caso de uso completo

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

Para revisar “Protocolar requerimento”, a equipe possui ator, gatilho e fluxo feliz, mas não registra autorização, anexos inválidos nem estado em falha. Qual complemento é mais útil?

A) Tratar a autorização apenas como observação e manter uma pós-condição única, sem estado de falha.
B) Adicionar o anexo inválido como ator secundário e descrever somente o retorno à tela inicial.
C) Criar fluxos para autorização e anexo inválido, mas deixar sem resultado observável os caminhos de falha.
D) Adicionar condições, alternativas e estados finais rastreados aos requisitos.

### S4D1Q046 — Inclusão

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

Dois casos sempre executam “Validar identidade”, que possui comportamento comum significativo. A relação adequada é:

A) «extend», de “Validar identidade” para ambos, pois ocorre sempre.
B) generalização, porque validar acontece antes dos outros casos.
C) nenhuma relação, pois casos de uso não podem reutilizar comportamento.
D) «include», dos casos base para “Validar identidade”.

### S4D1Q047 — Extensão — comando negativo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

Sobre a relação «extend», assinale a alternativa **INCORRETA**.

A) A seta parte do caso extensor e aponta para o caso base.
B) Um ponto de extensão pode indicar onde o acréscimo se encaixa.
C) O caso base fica incompleto e sempre depende do extensor para produzir valor.
D) A extensão pode ter condição; sem condição associada, ela é incondicional nos pontos especificados.

### S4D1Q048 — Generalização de atores

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

Ator “Servidor” consulta processo; “Fiscal” é um tipo de Servidor e também registra vistoria. A modelagem possível é:

A) compor Fiscal dentro de Servidor e destruir ambos juntos.
B) generalizar Fiscal a partir de Servidor e adicionar ao específico a relação própria.
C) usar include de Fiscal para Servidor, pois um papel executa o outro.
D) usar extend de Servidor para Fiscal, pois fiscalização é opcional.

### S4D1Q049 — Ordem não implica include — comando negativo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

Assinale a alternativa **INCORRETA** sobre relações entre casos de uso.

A) Include representa comportamento comum executado como parte do base.
B) Extend representa acréscimo condicionado a um base autônomo.
C) Generalização representa especialização, não sequência temporal.
D) Se A ocorre antes de B, então B obrigatoriamente inclui A.

### S4D1Q050 — Relações integradas de casos

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Exemplos resolvidos — include, extend e generalização](semana_04_estudo.md#s4-d1-exemplos-relacoes).

“Protocolar recurso” sempre executa “Validar identidade”; durante “Emitir certidão”, no ponto “selecionar entrega”, “Solicitar envio postal” é inserido se o usuário escolher essa modalidade; “Fiscal” é um Servidor especializado. A combinação correta de relações é:

A) include para validar; extend para envio postal; generalização de Fiscal para Servidor.
B) generalização para validar; include para envio; extend entre atores.
C) include para os três vínculos, pois todos aparecem no mesmo modelo.
D) extend para validar; include para envio; composição entre os atores.

## Questões extras dos blocos fixos do Dia 1

#### Extra Dia 1.1

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** competência regional
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

Uma notícia de possível exercício irregular refere-se a fato ocorrido no Paraná. A atuação ordinária no âmbito regional cabe, conforme suas atribuições:

A) ao CFA exclusivamente, porque nenhum Regional fiscaliza sua jurisdição.
B) ao sindicato, que substitui o conselho na atividade fiscalizatória.
C) ao CRA-PR, observada sua jurisdição e a legislação do sistema.
D) à secretaria estadual, pois o CRA-PR integra a Administração Direta.

#### Extra Dia 1.2

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** hierarquia normativa
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

Uma resolução recente parece contrariar requisito expresso da lei. Qual raciocínio deve orientar a análise?

A) Conferir redação, vigência, objeto, competência e hierarquia.
B) Considerar lei e resolução atos equivalentes em qualquer matéria.
C) Ignorar a lei porque sua redação é anterior à criação do sistema atual.
D) Aplicar a resolução apenas por ser numericamente mais recente.

#### Extra Dia 1.3

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** lei e decreto
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

A relação geral segura entre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967 é:

A) a lei fornece a base legal, e o decreto a regulamenta dentro dos limites legais.
B) o decreto fornece a base legal, e a lei apenas executa os detalhes administrativos.
C) o decreto regulamenta a lei e pode afastá-la sempre que for posterior.
D) lei e decreto ocupam o mesmo nível, resolvendo-se divergência apenas pela data.

#### Extra Dia 1.4

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Regimento e Código de Ética
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

Uma dúvida trata da organização interna do CRA-PR; outra, de conduta ética profissional. A consulta inicial coerente é:

A) Código de Ética para estrutura interna e Regimento para conduta profissional.
B) Regimento do CRA-PR para organização e Código de Ética para conduta.
C) somente o Regimento para as duas questões, porque ele foi aprovado pelo CFA.
D) somente o Código de Ética para as duas questões, porque é o ato mais recente.

#### Extra Dia 1.5

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** competências integradas
- **Nível:** Muito difícil
- **Uso:** Essenciais
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

Um fato ocorre no Paraná, exige apuração local e levanta questão que demanda orientação uniforme do sistema. Qual encaminhamento respeita território, função e hierarquia?

A) CRA-PR apura localmente e também fixa, por ato próprio, orientação nacional que prevalece sobre a lei.
B) CRA-PR atua no fato; CFA orienta nacionalmente; ambos usam fontes vigentes.
C) CFA assume a apuração regional, enquanto o CRA-PR fixa a orientação uniforme para todo o sistema.
D) CRA-PR atua no fato e o CFA orienta nacionalmente, mas a resolução mais recente afasta a lei anterior.

#### Extra Dia 1.6

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** autonomia regional
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

A autonomia administrativa do CRA-PR deve ser entendida como:

A) atuação própria nos limites da lei, do regimento e do sistema.
B) competência para substituir o CFA em toda orientação nacional.
C) poder para afastar lei federal dentro do Paraná.
D) subordinação à Administração Direta estadual.

#### Extra Dia 1.7

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** vigência e objeto
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

Duas resoluções possuem anos diferentes e tratam de objetos distintos. Para escolher a aplicável, deve-se primeiro:

A) aplicar a resolução de número mais alto, presumindo que ela substituiu as anteriores.
B) identificar objeto e competência e conferir a vigência.
C) identificar o objeto, mas dispensar a vigência porque ambas constam do repositório oficial.
D) verificar a competência, mas presumir revogado todo ato anterior ao edital.

#### Extra Dia 1.8

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** CFA e CRA-PR
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

Assinale a alternativa **INCORRETA** sobre o mapa CFA/CRA-PR.

A) A orientação nacional e a execução regional podem aparecer no mesmo caso.
B) A existência do CFA torna desnecessária qualquer atuação regional do CRA-PR.
C) A fonte deve ser escolhida também pelo objeto da dúvida.
D) O território do fato é relevante para localizar atuação regional.

#### Extra Dia 1.9

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** fonte normativa e requisito
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

Uma exigência legal será implementada no novo portal. Qual afirmação preserva a relação entre norma e software?

A) O analista pode criar prazo ausente e registrá-lo como artigo.
B) O portal pode alterar a obrigação para simplificar a interface.
C) A norma define a obrigação; o portal a implementa com rastreabilidade.
D) A regra deixa de ser jurídica quando vira requisito de software.

#### Extra Dia 1.10

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** análise normativa multifiltro
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

Um servidor usa resolução recente para afastar lei; atribui ao CFA fato puramente regional; e consulta Código de Ética para estrutura do CRA-PR. Quais três correções são necessárias?

A) Respeitar a hierarquia; verificar atuação do CRA-PR na jurisdição; consultar o Regimento para organização interna.
B) Respeitar a hierarquia; manter a apuração exclusivamente no CFA; consultar o Regimento para organização interna.
C) Respeitar a hierarquia; verificar a atuação do CRA-PR; consultar o Código de Ética para organização interna.
D) Aplicar apenas a cronologia; verificar a atuação do CRA-PR; consultar o Regimento para organização interna.

#### Extra Dia 1.11

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** modalidade verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

Em “a rastreabilidade pode reduzir omissões”, a forma verbal indica:

A) certeza de que nenhuma omissão ocorrerá.
B) proibição de usar outro mecanismo de controle.
C) obrigação jurídica expressa em qualquer contexto.
D) possibilidade ou capacidade, sem garantir eliminação universal.

#### Extra Dia 1.12

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** conectores
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

Em “os critérios eram vagos; portanto, o requisito não podia ser verificado”, “portanto” introduz:

A) finalidade da escolha de critérios.
B) concessão que contraria a primeira oração.
C) consequência do fato apresentado antes.
D) condição necessária ainda não realizada.

#### Extra Dia 1.13

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** referência pronominal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

No período “A equipe revisou a especificação e encaminhou-a ao gestor”, o pronome “a” retoma:

A) a especificação.
B) a equipe.
C) o gestor.
D) a revisão, termo que não está expresso.

#### Extra Dia 1.14

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita e voz verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

A passagem de “Os analistas validaram os requisitos” para a voz passiva, preservando papéis, é:

A) Validaram-se os analistas pelos requisitos.
B) Os requisitos validaram os analistas.
C) Os analistas foram validados pelos requisitos.
D) Os requisitos foram validados pelos analistas.

#### Extra Dia 1.15

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita integrada
- **Nível:** Muito difícil
- **Uso:** Revisão
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d1-exemplos-portugues).

Original: “Embora o protótipo possa esclarecer a interação, ele não valida automaticamente a segurança.” Qual reescrita preserva concessão, modalidade e referente?

A) Porque o protótipo pode esclarecer a interação, ele valida automaticamente a segurança.
B) Embora o protótipo esclareça a interação, a segurança pode ser considerada automaticamente validada.
C) Ainda que esclareça a interação, o protótipo não valida automaticamente a segurança.
D) Se o protótipo esclarecer a interação, ele não poderá validar a segurança.

#### Extra Dia 1.16

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concessão
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

A relação expressa por “Embora o requisito esteja claro, ainda falta confirmar sua fonte” é de:

A) causa: a clareza produz necessariamente a falta de fonte.
B) concessão: a clareza não elimina a pendência de origem.
C) finalidade: a fonte existe para tornar o requisito claro.
D) condição: a fonte só falta se o requisito estiver claro.

#### Extra Dia 1.17

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** quantificadores
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

A frase “Alguns requisitos não possuem critério” permite concluir que:

A) todos os requisitos possuem critério.
B) exatamente um requisito não possui critério.
C) há requisito sem critério, sem quantidade definida.
D) nenhum requisito possui critério.

#### Extra Dia 1.18

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita e modalidade
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

Assinale a reescrita **INCORRETA** para “A oficina pode reduzir conflitos”.

A) A oficina pode favorecer a redução de conflitos.
B) A oficina elimina necessariamente todos os conflitos.
C) A oficina é capaz de contribuir para reduzir conflitos.
D) É possível que a oficina reduza conflitos.

#### Extra Dia 1.19

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** coesão referencial
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

Em “O analista informou ao gestor que seu requisito estava incompleto”, o possessivo pode gerar ambiguidade. A revisão mais clara, se o requisito é do gestor, é:

A) O analista informou ao gestor que o requisito deste estava incompleto.
B) O analista informou ao gestor que seu requisito estava incompleto.
C) O analista informou ao gestor que o requisito do próprio analista estava incompleto.
D) O gestor informou ao analista que o requisito do gestor estava incompleto.

#### Extra Dia 1.20

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita e coesão
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d1-exemplos-portugues).

Original: “Se a fonte for confirmada, o requisito poderá ser aprovado; contudo, isso não dispensa o teste.” Qual paráfrase preserva condição, possibilidade, oposição e referência?

A) Como a fonte foi confirmada, o requisito deve ser aprovado, embora o teste seja dispensável.
B) Se a fonte for confirmada, o requisito será aprovado; portanto, o teste deixa de ser necessário.
C) Mesmo que a fonte não seja confirmada, o requisito poderá ser aprovado, desde que o teste seja dispensado.
D) Confirmada a fonte, será possível aprovar; ainda assim, o teste continua necessário.

## Gabarito do Dia 1

### Gabarito das questões principais

| Questão | Resposta |
|---:|:---:|
| 1 | B |
| 2 | C |
| 3 | D |
| 4 | B |
| 5 | A |
| 6 | A |
| 7 | D |
| 8 | D |
| 9 | B |
| 10 | C |
| 11 | C |
| 12 | A |
| 13 | A |
| 14 | C |
| 15 | D |
| 16 | A |
| 17 | B |
| 18 | B |
| 19 | D |
| 20 | C |
| 21 | C |
| 22 | A |
| 23 | C |
| 24 | D |
| 25 | B |
| 26 | A |
| 27 | B |
| 28 | D |
| 29 | D |
| 30 | C |
| 31 | B |
| 32 | A |
| 33 | C |
| 34 | C |
| 35 | D |
| 36 | A |
| 37 | C |
| 38 | D |
| 39 | B |
| 40 | C |
| 41 | C |
| 42 | D |
| 43 | A |
| 44 | A |
| 45 | D |
| 46 | D |
| 47 | C |
| 48 | B |
| 49 | D |
| 50 | A |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 1.1 | C |
| 1.2 | A |
| 1.3 | A |
| 1.4 | B |
| 1.5 | B |
| 1.6 | A |
| 1.7 | B |
| 1.8 | B |
| 1.9 | C |
| 1.10 | A |
| 1.11 | D |
| 1.12 | C |
| 1.13 | A |
| 1.14 | D |
| 1.15 | C |
| 1.16 | B |
| 1.17 | C |
| 1.18 | B |
| 1.19 | A |
| 1.20 | D |

## Comentários do Dia 1

### Comentário S4D1Q001

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Necessidade, requisito, regra, restrição e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O indicador não descreve comportamento observável do sistema.
- **B)** Correta. Expressa resultado institucional sem antecipar comportamento ou tecnologia.
- **C)** Incorreta. Nenhuma tecnologia ou limite de solução foi informado.
- **D)** Incorreta. Não há ator, fronteira nem objetivo operacional descrito.

**Conceito:** objetivo de negócio versus requisito.

**Pegadinha:** chamar toda demanda dirigida à TI de requisito funcional.

**Como pensar:** pergunte se a frase explica por que mudar ou o que o sistema deve fazer.

**Referência:** [Necessidade, requisito, regra, restrição e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

### Comentário S4D1Q002

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Percentual de disponibilidade é requisito de qualidade.
- **B)** Incorreta. Acessibilidade caracteriza qualidade da interação.
- **C)** Correta. Define capacidade observável oferecida a um papel externo.
- **D)** Incorreta. Tempo de resposta mensurável é atributo de desempenho.

**Conceito:** requisito funcional.

**Pegadinha:** confundir qualquer frase com verbo obrigatório com função.

**Como pensar:** identifique se a frase diz o que ocorre ou quão bem deve ocorrer.

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

### Comentário S4D1Q003

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. “Satisfatório” carece de métrica e limiar de avaliação.
- **B)** Incorreta. “Carga usual”, “rápido” e “mais importantes” não possuem valores definidos.
- **C)** Incorreta. “Melhor possível” não estabelece métrica nem limite verificável.
- **D)** Correta. Delimita ambiente, carga, operação, estatística e limiar observável.

**Conceito:** verificabilidade de requisito de qualidade.

**Pegadinha:** substituir adjetivo vago por outro adjetivo.

**Como pensar:** procure operação, cenário, métrica e limiar.

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

### Comentário S4D1Q004

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Necessidade, requisito, regra, restrição e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Login é uma solução parcial e não prova designação vigente.
- **B)** Correta. Mantém a política separada dos mecanismos que a implementam e testam.
- **C)** Incorreta. A regra trata autorização, não tempo de resposta.
- **D)** Incorreta. O mecanismo técnico não define sozinho a política institucional.

**Conceito:** regra de negócio e requisitos derivados.

**Pegadinha:** reduzir autorização a autenticação.

**Como pensar:** separe política, informação necessária, comportamento e teste.

**Referência:** [Necessidade, requisito, regra, restrição e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

### Comentário S4D1Q005

**Nível:** Muito difícil

**Uso:** Essenciais

**Referência:** [Exemplos resolvidos — qualidade e aceitação](semana_04_estudo.md#s4-d1-exemplos-qualidade).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Preserva singularidade sem perder ordem, fonte e visão do objetivo integrado.
- **B)** Incorreta. Decomposição não apaga relações funcionais entre comportamentos.
- **C)** Incorreta. A troca perde comportamentos funcionais necessários.
- **D)** Incorreta. Uma falha não indicaria qual obrigação deixou de ser atendida.

**Conceito:** singularidade, dependência e rastreabilidade.

**Pegadinha:** confundir decomposição com isolamento.

**Como pensar:** separe o que muda e testa isoladamente, mas preserve ligações.

**Referência:** [Exemplos resolvidos — qualidade e aceitação](semana_04_estudo.md#s4-d1-exemplos-qualidade).

### Comentário S4D1Q006

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Há tecnologia/serviço obrigatório e interação externa a especificar.
- **B)** Incorreta. A frase não descreve objetivo interativo nem fluxo.
- **C)** Incorreta. A determinação condiciona concretamente a arquitetura.
- **D)** Incorreta. Não há medida de facilidade ou experiência do usuário.

**Conceito:** restrição e interface externa.

**Pegadinha:** classificar toda integração como função isolada.

**Como pensar:** procure o limite imposto e depois as capacidades derivadas.

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

### Comentário S4D1Q007

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Acesso à tela não comprova permissão para decidir.
- **B)** Incorreta. A exibição não verifica bloqueio nem registro da decisão.
- **C)** Incorreta. Opinião sem cenário e resultado não constitui critério objetivo.
- **D)** Correta. Exercita a autorização positiva com persistência e a negativa sem produzir decisão indevida.

**Conceito:** critério de aceitação de autorização.

**Pegadinha:** testar apenas o caminho permitido.

**Como pensar:** derive cenários autorizado e proibido e confira o estado final.

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

### Comentário S4D1Q008

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Correta. A afirmação descreve corretamente consistência.
- **B)** Correta. A afirmação descreve corretamente necessidade.
- **C)** Correta. A afirmação descreve corretamente verificabilidade.
- **D)** Incorreta. Rastreabilidade registra origem e relações; mudanças controladas continuam possíveis.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** qualidade e rastreabilidade de requisitos.

**Pegadinha:** confundir ligação controlada com congelamento.

**Como pensar:** teste cada característica por sua finalidade.

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

### Comentário S4D1Q009

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Componente é elemento técnico, não parte interessada por si; seus responsáveis podem sê-lo.
- **B)** Correta. Partes interessadas são pessoas, grupos ou organizações com influência, conhecimento ou impacto, não apenas quem acessa a tela.
- **C)** Incorreta. Exclui decisores, apoio, integrações e afetados.
- **D)** Incorreta. Hierarquia não substitui conhecimento e impacto distribuídos.

**Conceito:** identificação de interessados.

**Pegadinha:** equiparar interessado a usuário de tela.

**Como pensar:** mapeie quem decide, conhece, opera, mantém, integra e sofre impacto.

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

### Comentário S4D1Q010

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. As categorias não correspondem aos sintomas descritos.
- **B)** Incorreta. A análise aceita defeitos centrais e inverte verificabilidade.
- **C)** Correta. Cada sintoma é ligado à característica de qualidade diretamente afetada.
- **D)** Incorreta. Os quatro rótulos pertencem a conceitos diferentes.

**Conceito:** diagnóstico multifiltro de qualidade.

**Pegadinha:** resolver por palavra isolada sem seguir a ordem.

**Como pensar:** associe cada evidência à propriedade que ela impede.

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

### Comentário S4D1Q011

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Documento declarado pode divergir do trabalho efetivo.
- **B)** Incorreta. A antecipação elimina evidência necessária.
- **C)** Correta. A observação revela prática; a confirmação separa desvio de regra válida.
- **D)** Incorreta. O formato pode ocultar exceções não antecipadas.

**Conceito:** observação e validação.

**Pegadinha:** automatizar o procedimento observado sem autorização.

**Como pensar:** descubra a prática e valide sua legitimidade com o responsável.

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

### Comentário S4D1Q012

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A preparação e a confirmação reduzem omissões e interpretação unilateral.
- **B)** Incorreta. Questões fechadas não bastam, e silêncio não confirma significado.
- **C)** Incorreta. A condução cria viés de confirmação e perde conflito.
- **D)** Incorreta. Falta preparação, validação e rastreabilidade.

**Conceito:** entrevista de requisitos.

**Pegadinha:** confundir conversa realizada com requisito validado.

**Como pensar:** prepare, explore evidência, parafraseie e confirme.

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

### Comentário S4D1Q013

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — elicitação](semana_04_estudo.md#s4-d1-exemplos-elicitacao).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Incorreta. Votação majoritária não dispensa obrigação, risco nem autoridade competente.
- **B)** Correta. Isso permite negociar com base em razões observáveis.
- **C)** Correta. O registro sustenta acompanhamento e rastreabilidade.
- **D)** Correta. Explorar opção intermediária é parte legítima da análise.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** oficina e negociação.

**Pegadinha:** tratar consenso numérico como validade automática.

**Como pensar:** procure critérios, competência e registro além da preferência.

**Referência:** [Exemplos resolvidos — elicitação](semana_04_estudo.md#s4-d1-exemplos-elicitacao).

### Comentário S4D1Q014

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — elicitação](semana_04_estudo.md#s4-d1-exemplos-elicitacao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Frequência não prova autorização institucional.
- **B)** Incorreta. Facilidade técnica não resolve legitimidade do processo.
- **C)** Correta. Combina fontes sem declarar automaticamente correta a prática ou o documento.
- **D)** Incorreta. O documento pode estar desatualizado ou incompleto.

**Conceito:** triangulação e decisão institucional.

**Pegadinha:** escolher uma fonte por aparência de autoridade.

**Como pensar:** separe evidência observada de regra autorizada.

**Referência:** [Exemplos resolvidos — elicitação](semana_04_estudo.md#s4-d1-exemplos-elicitacao).

### Comentário S4D1Q015

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Remove consistência e transfere regra ao operador.
- **B)** Incorreta. Ignora a regra fornecida e o objetivo do atendimento.
- **C)** Incorreta. Viola requisitos documentais antes da decisão.
- **D)** Correta. Integra obrigação, fluxo, exceções e objetivos sem escolher um extremo arbitrário.

**Conceito:** negociação multifonte e requisito progressivo.

**Pegadinha:** resolver conflito por preferência de uma área.

**Como pensar:** localize a regra superior, os momentos do fluxo e os critérios de cada parte.

**Referência:** [Elicitação: descobrir, não apenas perguntar](semana_04_estudo.md#s4-d1-elicitacao).

### Comentário S4D1Q016

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Análise, modelagem e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Termos semelhantes podem esconder escopos, fontes ou condições distintas.
- **B)** Incorreta. A união perde rastreabilidade e pode apagar regra.
- **C)** Incorreta. Duplicidade eleva inconsistência e custo de mudança.
- **D)** Incorreta. Numeração não demonstra validade ou abrangência.

**Conceito:** análise de duplicidade semântica.

**Pegadinha:** considerar sinônimos aparentes como identidade comprovada.

**Como pensar:** compare definição, fonte, condição e critério antes de consolidar.

**Referência:** [Análise, modelagem e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

### Comentário S4D1Q017

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — análise e priorização](semana_04_estudo.md#s4-d1-exemplos-analise).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A decisão ficaria sem rastreabilidade e sem avaliação.
- **B)** Correta. A comparação controla a expansão; o registro preserva a necessidade que excede o escopo.
- **C)** Incorreta. Não foi demonstrada dependência total entre as iniciativas.
- **D)** Incorreta. Legitimidade da fonte não torna o pedido aderente ao escopo.

**Conceito:** análise de escopo.

**Pegadinha:** confundir registrar demanda com incluí-la.

**Como pensar:** teste ligação com objetivo, fronteira e dependências.

**Referência:** [Exemplos resolvidos — análise e priorização](semana_04_estudo.md#s4-d1-exemplos-analise).

### Comentário S4D1Q018

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Análise, modelagem e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O método ignora risco, valor e obrigação.
- **B)** Correta. A ordem resulta de critérios explícitos e da relação entre entregas.
- **C)** Incorreta. Volume de pedidos não supera obrigação sem análise.
- **D)** Incorreta. A dependência técnica torna a ordem inconsistente.

**Conceito:** priorização por valor, risco e dependência.

**Pegadinha:** reduzir prioridade a votação ou cronologia.

**Como pensar:** liste obrigação, prazo, valor, risco, custo e dependências.

**Referência:** [Análise, modelagem e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

### Comentário S4D1Q019

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Detalhes podem existir, mas não substituem atributos essenciais.
- **B)** Incorreta. Dois campos não sustentam origem, aceite ou relação.
- **C)** Incorreta. Aprovação não torna o requisito testável ou conectado.
- **D)** Correta. Esses atributos permitem entender origem, decisão, aceite e impacto.

**Conceito:** atributos de requisito.

**Pegadinha:** tratar o texto como registro gerencial completo.

**Como pensar:** procure origem, razão, prioridade, estado, aceite e ligações.

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

### Comentário S4D1Q020

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A baseline controlada precisa permanecer coerente após decisão.
- **B)** Incorreta. Remover origem destrói justificativa e análise de impacto.
- **C)** Correta. Usa rastreabilidade bidirecional e controle de mudança em toda a cadeia.
- **D)** Incorreta. Teste não redefine requisito, modelo ou implementação.

**Conceito:** rastreabilidade e mudança integrada.

**Pegadinha:** atualizar apenas o artefato mais visível.

**Como pensar:** percorra a cadeia nos dois sentidos e sincronize versões.

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

### Comentário S4D1Q021

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Conformidade formal e consistência interna são evidências de verificação, não bastam para validar a necessidade.
- **B)** Incorreta. Identificação e padrão textual apoiam a verificação, mas não confirmam que o conteúdo é o necessário.
- **C)** Correta. Validação confronta o conteúdo com objetivos, fontes e uso pretendido.
- **D)** Incorreta. Fidelidade da implementação ao projeto não confirma, por si, que os requisitos representam a necessidade correta.

**Conceito:** validação de requisitos.

**Pegadinha:** confundir qualidade do formato com necessidade correta.

**Como pensar:** pergunte se estamos especificando a coisa certa.

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

### Comentário S4D1Q022

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Incorreta. Consistência interna não prova necessidade externa; isso exige validação com interessados e objetivos.
- **B)** Correta. Isso corresponde à qualidade interna da especificação.
- **C)** Correta. Essas técnicas exploram adequação ao uso e à necessidade.
- **D)** Correta. Forma correta não garante conteúdo correto.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** verificação versus validação.

**Pegadinha:** tratar consistência interna como aceite do negócio.

**Como pensar:** separe construir o artefato corretamente de representar a coisa certa.

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

### Comentário S4D1Q023

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — validação, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-exemplos-validacao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Uma qualidade não substitui outra.
- **B)** Incorreta. Não houve cenário de desempenho ou ambiente produtivo.
- **C)** Correta. O alcance do aceite deve acompanhar o que foi realmente demonstrado.
- **D)** Incorreta. A conclusão extrapola a evidência visual.

**Conceito:** alcance da validação por protótipo.

**Pegadinha:** generalizar evidência parcial.

**Como pensar:** liste o que foi demonstrado e o que ainda exige outra técnica.

**Referência:** [Exemplos resolvidos — validação, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-exemplos-validacao).

### Comentário S4D1Q024

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A duplicação rompe histórico e coerência.
- **B)** Incorreta. A alteração perde decisão, impacto e versão.
- **C)** Incorreta. Baseline não torna requisito imutável.
- **D)** Correta. Baseline serve de referência para mudança controlada, não para bloqueio eterno.

**Conceito:** baseline e controle de mudança.

**Pegadinha:** confundir referência acordada com congelamento.

**Como pensar:** controle entrada, impacto, decisão, incorporação e comunicação.

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

### Comentário S4D1Q025

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — validação, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-exemplos-validacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Ignora autorização, comportamento, testes e outros consumidores.
- **B)** Correta. Combina origem, impacto estrutural/comportamental, decisão e sincronização.
- **C)** Incorreta. Artefatos não se atualizam semanticamente por si.
- **D)** Incorreta. Histórico controlado é necessário para auditoria e comparação.

**Conceito:** análise de impacto multifiltro.

**Pegadinha:** reduzir regra transversal a campo visível.

**Como pensar:** confira fonte, sujeito, prazo, estados, interfaces, implementação e testes.

**Referência:** [Exemplos resolvidos — validação, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-exemplos-validacao).

### Comentário S4D1Q026

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O sentido retrocede do artefato à sua origem e razão.
- **B)** Incorreta. A pergunta segue do requisito para dependentes posteriores.
- **C)** Incorreta. A pergunta percorre impactos adiante na cadeia.
- **D)** Incorreta. A pergunta segue para artefatos que realizam ou verificam o requisito.

**Conceito:** rastreabilidade para trás.

**Pegadinha:** confundir direção com posição na tabela.

**Como pensar:** parta do requisito e pergunte de onde ele veio.

**Referência:** [Gestão, baseline, mudança e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

### Comentário S4D1Q027

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A forma de modelagem depende do escopo e não é universal.
- **B)** Correta. A capacidade de auditoria decorre de requisito ou objetivo anterior.
- **C)** Incorreta. A derivação possui justificativa explícita.
- **D)** Incorreta. Autor, instante e versão sustentam responsabilização.

**Conceito:** requisitos derivados.

**Pegadinha:** descartar requisito por não ter sido dito literalmente.

**Como pensar:** procure a necessidade superior que torna a consequência indispensável.

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

### Comentário S4D1Q028

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Segurança depende do recurso e do dado exposto.
- **B)** Incorreta. Outras operações podem continuar protegidas.
- **C)** Incorreta. Ambiguidade deliberada não é critério de teste.
- **D)** Correta. Autenticação para protocolar pode coexistir com consulta pública limitada.

**Conceito:** consistência e escopo.

**Pegadinha:** identificar conflito por palavra sem comparar operação.

**Como pensar:** explicite sujeito, ação, objeto, condição e dado.

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

### Comentário S4D1Q029

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Correta. A técnica produz evidência limitada ao experimento.
- **B)** Correta. Reexaminar a forma sem perder a necessidade é adequado.
- **C)** Correta. Esses fatores condicionam implementação realista.
- **D)** Incorreta. Valor não afasta restrições; o trade-off precisa de decisão e alternativa.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** viabilidade de requisitos.

**Pegadinha:** tratar valor como autorização para violar restrições.

**Como pensar:** teste objetivo, limites e opções antes de aceitar a solução.

**Referência:** [Qualidade, critérios de aceitação e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

### Comentário S4D1Q030

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — análise e priorização](semana_04_estudo.md#s4-d1-exemplos-analise).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Distribuição simétrica não resolve prioridade nem risco.
- **B)** Incorreta. Simplicidade não supera obrigação e transparência.
- **C)** Correta. Prioriza obrigação e dependência, mitiga o risco e justifica o adiamento de modo rastreável.
- **D)** Incorreta. A ordem viola a dependência declarada.

**Conceito:** priorização integrada.

**Pegadinha:** considerar apenas valor ou apenas risco.

**Como pensar:** combine obrigação, dependência, risco, custo e resultado utilizável.

**Referência:** [Exemplos resolvidos — análise e priorização](semana_04_estudo.md#s4-d1-exemplos-analise).

### Comentário S4D1Q031

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. É decisão técnica posterior e não define análise OO.
- **B)** Correta. A análise descreve o problema antes de detalhar tecnologia.
- **C)** Incorreta. São escolhas de projeto/implementação.
- **D)** Incorreta. Tela não determina automaticamente conceito do domínio.

**Conceito:** análise OO versus projeto.

**Pegadinha:** antecipar solução tecnológica.

**Como pensar:** pergunte se a decisão descreve o domínio ou a realização.

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

### Comentário S4D1Q032

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Separa o tipo modelado de uma instância concreta.
- **B)** Incorreta. Ambos são conceitos de modelagem independentes dessas camadas.
- **C)** Incorreta. Compartilhar estrutura não elimina identidade da ocorrência.
- **D)** Incorreta. Os papéis de descrição e ocorrência foram invertidos.

**Conceito:** classe versus objeto.

**Pegadinha:** confundir descrição com instância.

**Como pensar:** pergunte se o elemento define um tipo ou representa uma ocorrência.

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

### Comentário S4D1Q033

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — análise orientada a objetos](semana_04_estudo.md#s4-d1-exemplos-oo).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Centralização de responsabilidades não garante encapsulamento adequado.
- **B)** Incorreta. Compartilhar plataforma não cria responsabilidade coesa.
- **C)** Correta. As funções pertencem a conceitos e serviços diferentes.
- **D)** Incorreta. Quantidade de métodos não caracteriza herança.

**Conceito:** coesão e distribuição de responsabilidades.

**Pegadinha:** medir coesão pela quantidade de código.

**Como pensar:** agrupe comportamentos pela informação e pelo motivo de mudança.

**Referência:** [Exemplos resolvidos — análise orientada a objetos](semana_04_estudo.md#s4-d1-exemplos-oo).

### Comentário S4D1Q034

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Correta. A afirmação descreve a redução intencional de detalhes.
- **B)** Correta. A interface protege detalhes que podem mudar.
- **C)** Incorreta. Encapsulamento protege decisões internas; não justifica baixa coesão centralizada.
- **D)** Correta. Modelos são parciais e orientados a finalidade.

**Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.

**Conceito:** abstração e encapsulamento.

**Pegadinha:** reduzir encapsulamento a modificador de visibilidade.

**Como pensar:** avalie relevância, responsabilidade e fronteira de mudança.

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

### Comentário S4D1Q035

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — análise orientada a objetos](semana_04_estudo.md#s4-d1-exemplos-oo).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A solução apaga conceitos e concentra responsabilidades.
- **B)** Incorreta. Capitalização não prova identidade, estado ou relevância.
- **C)** Incorreta. Verbos sugerem comportamento, não classes automaticamente.
- **D)** Correta. Combina descoberta, crítica e confirmação sem automatizar a extração gramatical.

**Conceito:** identificação multifiltro de classes.

**Pegadinha:** aplicar regra mecânica substantivo-classe.

**Como pensar:** proponha candidatos, atribua responsabilidades e valide semântica.

**Referência:** [Exemplos resolvidos — análise orientada a objetos](semana_04_estudo.md#s4-d1-exemplos-oo).

### Comentário S4D1Q036

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A primeira é relação é-um; a segunda é vínculo significativo.
- **B)** Incorreta. Direções e naturezas não correspondem ao domínio.
- **C)** Incorreta. Não há todo-parte nem ciclo de vida dependente.
- **D)** Incorreta. Analisar Processo não torna Fiscal subtipo de Processo.

**Conceito:** generalização e associação.

**Pegadinha:** usar a mesma relação para todo vínculo.

**Como pensar:** teste 'é um' para especialização e vínculo para associação.

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

### Comentário S4D1Q037

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Nesse recorte, a duração funciona como valor, não como objeto com identidade e ciclo próprios.
- **B)** Incorreta. O elemento pertence à solução de interface e não é, por isso, conceito do domínio.
- **C)** Correta. O conceito é reconhecido pelo negócio e participa de comportamentos.
- **D)** Incorreta. No cenário dado, o número é atributo identificador do requerimento, não o conceito mais forte para classe.

**Conceito:** classe candidata.

**Pegadinha:** escolher substantivo sem relevância.

**Como pensar:** procure identidade, estado, comportamento e vocabulário do domínio.

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

### Comentário S4D1Q038

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Baixo acoplamento não autoriza perder requisito.
- **B)** Incorreta. A exposição rompe encapsulamento e amplia dependência.
- **C)** Incorreta. A duplicação aumenta motivos de mudança e dependência.
- **D)** Correta. O cliente conhece o contrato necessário, não a implementação completa.

**Conceito:** baixo acoplamento com responsabilidade.

**Pegadinha:** confundir desacoplamento com ausência de colaboração.

**Como pensar:** preserve o contrato necessário e esconda decisões internas.

**Referência:** [Análise e projeto orientado a objetos](semana_04_estudo.md#s4-d1-oo).

### Comentário S4D1Q039

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Correta. Ator abstrai indivíduos concretos.
- **B)** Incorreta. Ator é papel externo e pode ser desempenhado por pessoa ou sistema.
- **C)** Correta. Papéis dependem do objetivo e da relação com a fronteira.
- **D)** Correta. Sistema externo pode trocar informação com o sistema modelado.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** ator como papel externo.

**Pegadinha:** equiparar ator a pessoa nomeada.

**Como pensar:** defina papel, objetivo e posição fora da fronteira.

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

### Comentário S4D1Q040

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — casos de uso](semana_04_estudo.md#s4-d1-exemplos-casos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Tecnologia interna não é ator apenas por trocar dados.
- **B)** Incorreta. O sistema modelado contém os comportamentos do caso.
- **C)** Correta. A classificação segue o escopo declarado e a interação externa.
- **D)** Incorreta. Os papéis e posições foram invertidos.

**Conceito:** fronteira e atores técnicos.

**Pegadinha:** classificar qualquer componente como ator.

**Como pensar:** declare o sistema sob estudo e posicione apenas papéis externos.

**Referência:** [Exemplos resolvidos — casos de uso](semana_04_estudo.md#s4-d1-exemplos-casos).

### Comentário S4D1Q041

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Nomeia armazenamento, não comportamento com valor.
- **B)** Incorreta. Nomeia etapa interna e dependente da interface.
- **C)** Correta. Usa verbo e objeto para expressar resultado de valor ao ator.
- **D)** Incorreta. Nomeia detalhe de interface, não objetivo.

**Conceito:** nome e objetivo de caso de uso.

**Pegadinha:** modelar controles da tela como objetivos.

**Como pensar:** pergunte qual resultado o ator obtém.

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

### Comentário S4D1Q042

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não há relação de especialização.
- **B)** Incorreta. Pós-condição descreve estado após o caso.
- **C)** Incorreta. A frase é estado, não papel externo.
- **D)** Correta. Descreve estado necessário antes do fluxo, sem executá-lo.

**Conceito:** precondição de caso de uso.

**Pegadinha:** transformar todo estado prévio em passo.

**Como pensar:** pergunte se o caso assume ou produz a condição.

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

### Comentário S4D1Q043

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Expressa estado garantido e observável após conclusão bem-sucedida.
- **B)** Incorreta. Desejo genérico não descreve estado do sistema.
- **C)** Incorreta. Atributos vagos não são pós-condição.
- **D)** Incorreta. Isso é precondição no recorte apresentado.

**Conceito:** pós-condição de sucesso.

**Pegadinha:** confundir condição de entrada com resultado.

**Como pensar:** descreva o estado que permanece depois do sucesso.

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

### Comentário S4D1Q044

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Exemplos resolvidos — fluxos e condições](semana_04_estudo.md#s4-d1-exemplos-fluxos).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O desvio continua a servir o mesmo objetivo e nasce de condição do fluxo.
- **B)** Incorreta. Não há especialização de papel.
- **C)** Incorreta. A correção impede o sucesso normal naquele caminho.
- **D)** Incorreta. Condição ou dado não é papel externo.

**Conceito:** fluxo alternativo.

**Pegadinha:** criar caso ou ator para cada erro.

**Como pensar:** ligue o desvio ao passo, à condição e ao estado resultante.

**Referência:** [Exemplos resolvidos — fluxos e condições](semana_04_estudo.md#s4-d1-exemplos-fluxos).

### Comentário S4D1Q045

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A observação não torna a autorização verificável, e permanece ausente o resultado da falha.
- **B)** Incorreta. Anexo inválido é condição/dado, não papel externo, e o retorno de tela não cobre todos os estados.
- **C)** Incorreta. Os desvios foram nomeados, mas ainda não possuem pós-condições ou garantias observáveis.
- **D)** Correta. Cobre entrada, exceções, estados e rastreabilidade sem confundir com projeto de tela.

**Conceito:** descrição completa de caso de uso.

**Pegadinha:** considerar fluxo feliz suficiente.

**Como pensar:** confira objetivo, entrada, normal, alternativas, saída, regras e ligações.

**Referência:** [Casos de uso: ator, objetivo, fronteira e fluxo](semana_04_estudo.md#s4-d1-casos-uso).

### Comentário S4D1Q046

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Extensão acrescenta comportamento condicionado, não obrigatório.
- **B)** Incorreta. Ordem temporal não caracteriza especialização.
- **C)** Incorreta. Inclusão existe justamente para comportamento comum significativo.
- **D)** Correta. O comportamento reutilizado é obrigatório e incorporado aos casos base.

**Conceito:** relação include.

**Pegadinha:** escolher pela ordem de execução.

**Como pensar:** teste obrigatoriedade e reutilização; depois confira a direção.

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

### Comentário S4D1Q047

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Correta. Essa é a direção da dependência de extensão.
- **B)** Correta. O ponto delimita o local em que o comportamento adicional pode ser inserido.
- **C)** Incorreta. Na extensão, o caso base é significativo sem o comportamento adicional.
- **D)** Correta. A UML admite condição opcional; sua ausência não invalida a extensão, apenas a torna incondicional.

**Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.

**Conceito:** relação extend, pontos de extensão e condição opcional.

**Pegadinha:** tratar extensão como passo obrigatório ou exigir condição em todo «extend».

**Como pensar:** confirme autonomia do base, pontos de extensão, eventual condição e direção.

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

### Comentário S4D1Q048

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Composição não descreve hierarquia de atores.
- **B)** Correta. O ator especializado herda relações do geral e acrescenta comportamento.
- **C)** Incorreta. Include relaciona comportamentos de casos, não tipos de ator.
- **D)** Incorreta. Extensão não representa especialização de papéis.

**Conceito:** generalização de atores.

**Pegadinha:** trocar herança por relações entre casos.

**Como pensar:** aplique o teste 'é um' e confira relações herdadas.

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

### Comentário S4D1Q049

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Correta. A afirmação respeita obrigatoriedade e incorporação.
- **B)** Correta. A afirmação descreve a semântica da extensão.
- **C)** Correta. A afirmação distingue corretamente as relações.
- **D)** Incorreta. Precedência, por si só, não prova reutilização obrigatória incorporada.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** relações de casos de uso.

**Pegadinha:** inferir semântica apenas pela ordem.

**Como pensar:** teste obrigatoriedade, autonomia, reutilização e especialização.

**Referência:** [Inclusão, extensão e generalização](semana_04_estudo.md#s4-d1-relacoes-casos).

### Comentário S4D1Q050

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Exemplos resolvidos — include, extend e generalização](semana_04_estudo.md#s4-d1-exemplos-relacoes).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Cada relação satisfaz incorporação obrigatória, inserção no ponto de extensão e especialização.
- **B)** Incorreta. Aplica relações a naturezas incompatíveis.
- **C)** Incorreta. Compartilhar diagrama não torna todas as relações inclusão.
- **D)** Incorreta. Inverte obrigatoriedade/autonomia e usa relação estrutural imprópria.

**Conceito:** integração de include, extend e generalização.

**Pegadinha:** escolher uma única relação para situações distintas.

**Como pensar:** aplique três filtros: obrigatório comum, adicional condicional e 'é um'.

**Referência:** [Exemplos resolvidos — include, extend e generalização](semana_04_estudo.md#s4-d1-exemplos-relacoes).

### Comentário Extra Dia 1.1

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** competência regional
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A orientação nacional não elimina a atuação regional.
- **B)** Incorreta. Sindicato não substitui conselho profissional nessa competência.
- **C)** Correta. O Regional exerce as competências territoriais que lhe são atribuídas.
- **D)** Incorreta. O enquadramento proposto não corresponde ao sistema profissional.

**Conceito:** competência regional do CRA-PR.

**Pegadinha:** confundir alcance nacional do CFA com execução exclusiva.

**Como pensar:** identifique território e natureza da providência.

**Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

### Comentário Extra Dia 1.2

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** hierarquia normativa
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A data não autoriza afastar norma superior fora dos limites da competência.
- **B)** Incorreta. Os atos não possuem a mesma natureza hierárquica.
- **C)** Incorreta. Vigência deve ser verificada, não presumida pela idade.
- **D)** Incorreta. Cronologia isolada não resolve hierarquia ou competência.

**Conceito:** hierarquia, competência e vigência.

**Pegadinha:** usar apenas a data como critério.

**Como pensar:** confira fonte, objeto, nível e competência.

**Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

### Comentário Extra Dia 1.3

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** lei e decreto
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Regulamentar detalha execução sem substituir a lei.
- **B)** Incorreta. Inverte a função da base legal e a do regulamento.
- **C)** Incorreta. O decreto regulamenta, mas sua posterioridade não lhe permite afastar a lei.
- **D)** Incorreta. Lei e decreto possuem naturezas e posições distintas; a data isolada não resolve conflito.

**Conceito:** lei e decreto regulamentador.

**Pegadinha:** tratar regulamentação como revogação.

**Como pensar:** parta da base legal e leia o regulamento dentro dela.

**Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

### Comentário Extra Dia 1.4

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Regimento e Código de Ética
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Os objetos materiais das duas fontes foram trocados.
- **B)** Correta. Cada fonte é selecionada pelo objeto material da dúvida.
- **C)** Incorreta. A aprovação pelo CFA não transforma o Regimento em fonte geral sobre conduta ética.
- **D)** Incorreta. A maior atualidade não substitui a análise do objeto regulado.

**Conceito:** seleção de fonte normativa.

**Pegadinha:** escolher fonte por data ou suporte.

**Como pensar:** classifique primeiro o objeto da dúvida.

**Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

### Comentário Extra Dia 1.5

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** competências integradas
- **Nível:** Muito difícil
- **Uso:** Essenciais
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A atuação local está bem situada, mas o Regional não assume alcance nacional nem supera a lei.
- **B)** Correta. Distribui execução e orientação sem ignorar norma ou jurisdição.
- **C)** Incorreta. Inverte os planos territorial e sistêmico atribuídos no cenário.
- **D)** Incorreta. Acerta a distribuição funcional, mas erra ao fazer cronologia superar hierarquia.

**Conceito:** competência regional/nacional e fonte.

**Pegadinha:** resolver caso multifonte com um único rótulo.

**Como pensar:** separe território, natureza da ação, órgão e norma.

**Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

### Comentário Extra Dia 1.6

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** autonomia regional
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Autonomia não rompe a ordem jurídica nem a coordenação sistêmica.
- **B)** Incorreta. O alcance regional não se converte em competência nacional geral.
- **C)** Incorreta. Autonomia administrativa não supera a lei.
- **D)** Incorreta. O enquadramento não decorre da autonomia do Regional.

**Conceito:** autonomia do CRA-PR.

**Pegadinha:** confundir autonomia com soberania.

**Como pensar:** associe autonomia a atuação própria com limites jurídicos.

**Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

### Comentário Extra Dia 1.7

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** vigência e objeto
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Numeração não demonstra pertinência material nem revogação.
- **B)** Correta. Norma mais nova de matéria diversa não substitui a fonte pertinente.
- **C)** Incorreta. Repositório oficial não dispensa conferir vigência e eventuais relações entre atos.
- **D)** Incorreta. Competência é necessária, mas anterioridade ao edital não implica revogação.

**Conceito:** objeto, competência e vigência.

**Pegadinha:** usar número ou ano como atalho.

**Como pensar:** comece pela pergunta jurídica, depois localize a fonte.

**Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

### Comentário Extra Dia 1.8

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** CFA e CRA-PR
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Correta. As competências podem cooperar sem se confundir.
- **B)** Incorreta. O sistema distribui atribuições; a esfera nacional não elimina a regional.
- **C)** Correta. O objeto impede aplicar ato materialmente alheio.
- **D)** Correta. A jurisdição é um filtro pertinente.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** competências do sistema CFA/CRAs.

**Pegadinha:** transformar coordenação em exclusividade operacional.

**Como pensar:** separe alcance nacional, jurisdição e objeto.

**Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

### Comentário Extra Dia 1.9

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** fonte normativa e requisito
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Prazos e artigos exigem confirmação oficial.
- **B)** Incorreta. Conveniência técnica não autoriza mudar a norma.
- **C)** Correta. Tecnologia realiza a obrigação, mas não cria sua literalidade.
- **D)** Incorreta. A origem normativa permanece relevante.

**Conceito:** rastreabilidade de fonte normativa.

**Pegadinha:** deixar a solução redefinir a regra.

**Como pensar:** confirme a fonte e preserve a ligação no requisito.

**Referência:** [Revisão fixa: Legislação CRA/CFA](semana_04_estudo.md#s4-d1-b4).

### Comentário Extra Dia 1.10

- **Dia:** Dia 1
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** análise normativa multifiltro
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Corrige nível normativo, competência territorial e objeto da fonte.
- **B)** Incorreta. Corrige hierarquia e fonte, mas mantém inadequada a atribuição do fato puramente regional.
- **C)** Incorreta. Corrige hierarquia e competência, mas conserva a fonte de objeto incompatível com organização interna.
- **D)** Incorreta. Corrige competência e fonte, mas ainda usa cronologia isolada para afastar a lei.

**Conceito:** hierarquia, competência e objeto.

**Pegadinha:** corrigir apenas um dos três erros.

**Como pensar:** monte tabela fato → órgão → fonte → limite.

**Referência:** [Exemplos resolvidos — Legislação CRA/CFA](semana_04_estudo.md#s4-d1-exemplos-legislacao).

### Comentário Extra Dia 1.11

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** modalidade verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A frase não contém garantia universal.
- **B)** Incorreta. Não há exclusividade ou proibição.
- **C)** Incorreta. Pode não equivale automaticamente a deve.
- **D)** Correta. O modal preserva conclusão não absoluta.

**Conceito:** modalidade.

**Pegadinha:** converter possibilidade em certeza.

**Como pensar:** marque o verbo modal e preserve seu grau.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.12

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** conectores
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. A segunda oração não expressa objetivo.
- **B)** Incorreta. Não há contraste concessivo.
- **C)** Correta. A vagueza explica a impossibilidade de verificação.
- **D)** Incorreta. A estrutura não usa hipótese.

**Conceito:** relação de consequência.

**Pegadinha:** trocar conectores apenas por proximidade.

**Como pensar:** identifique qual oração causa e qual resulta.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.13

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** referência pronominal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O pronome feminino singular funciona como objeto direto de encaminhou.
- **B)** Incorreta. A equipe é sujeito das duas ações, não objeto encaminhado.
- **C)** Incorreta. O gestor aparece como destinatário introduzido por “ao”.
- **D)** Incorreta. Não há esse antecedente nominal no período.

**Conceito:** coesão referencial.

**Pegadinha:** escolher o termo mais próximo sem testar função.

**Como pensar:** combine gênero, número, sentido e sintaxe.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.14

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita e voz verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A frase muda o elemento validado.
- **B)** Incorreta. A forma continua ativa e inverte a relação.
- **C)** Incorreta. Agente e paciente foram invertidos.
- **D)** Correta. O objeto torna-se sujeito paciente e o agente é mantido.

**Conceito:** voz ativa e passiva.

**Pegadinha:** preservar palavras e inverter papéis.

**Como pensar:** localize agente, ação e paciente antes da transformação.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.15

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita integrada
- **Nível:** Muito difícil
- **Uso:** Revisão
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d1-exemplos-portugues).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Troca concessão por causa e passa a afirmar justamente a validação automática negada no original.
- **B)** Incorreta. Mantém forma concessiva, mas inverte a conclusão sobre a segurança.
- **C)** Correta. Mantém contraste concessivo, possibilidade e papel instrumental do protótipo.
- **D)** Incorreta. Troca concessão por condição e possibilidade por impossibilidade categórica.

**Conceito:** reescrita com modalidade e coesão.

**Pegadinha:** preservar vocabulário e alterar lógica.

**Como pensar:** confira conector, modal, referente e papéis.

**Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d1-exemplos-portugues).

### Comentário Extra Dia 1.16

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concessão
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Não existe causalidade entre as proposições.
- **B)** Correta. A segunda ideia prevalece apesar do fato inicial.
- **C)** Incorreta. A oração não expressa objetivo.
- **D)** Incorreta. A leitura condicional não é indicada.

**Conceito:** oração concessiva.

**Pegadinha:** interpretar contraste como causa.

**Como pensar:** substitua mentalmente por 'ainda que' e teste.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.17

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** quantificadores
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Contradiz a existência afirmada.
- **B)** Incorreta. “Alguns” não fixa cardinalidade igual a um.
- **C)** Correta. Há pelo menos um caso, mas a frase não determina a quantidade nem exclui a possibilidade de todos.
- **D)** Incorreta. A conclusão amplia “alguns” para o conjunto inteiro.

**Conceito:** quantificação existencial e escopo.

**Pegadinha:** transformar existência em cardinalidade exata ou em universalidade.

**Como pensar:** marque quantificador e alcance da negação sem acrescentar uma exclusão que o enunciado não declarou.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.18

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita e modalidade
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Correta. Conserva modalidade e sentido geral.
- **B)** Incorreta. A redação converte possibilidade em certeza universal.
- **C)** Correta. Preserva capacidade sem garantia absoluta.
- **D)** Correta. Mantém o valor de possibilidade.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** preservação da modalidade.

**Pegadinha:** usar termo absoluto como suposta paráfrase.

**Como pensar:** compare o grau de certeza entre original e reescrita.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.19

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** coesão referencial
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. “Deste” retoma explicitamente o gestor no contexto proposto.
- **B)** Incorreta. Mantém exatamente a ambiguidade.
- **C)** Incorreta. A frase é clara, mas atribui o requisito ao analista, não ao gestor.
- **D)** Incorreta. Explicita o proprietário correto, porém troca quem informa e quem recebe a informação.

**Conceito:** ambiguidade pronominal.

**Pegadinha:** manter possessivo com dois antecedentes possíveis.

**Como pensar:** nomeie o referente ou use demonstrativo inequivocamente.

**Referência:** [Português: modalidade, referência e sentido](semana_04_estudo.md#s4-d1-portugues).

### Comentário Extra Dia 1.20

- **Dia:** Dia 1
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita e coesão
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d1-exemplos-portugues).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Troca a condição por fato, a possibilidade por obrigação e torna o teste dispensável.
- **B)** Incorreta. Preserva a condição, mas converte possibilidade em certeza e oposição em conclusão que dispensa o teste.
- **C)** Incorreta. Mantém possibilidade, mas inverte a condição e faz da dispensa do teste requisito para aprovação.
- **D)** Correta. Mantém os quatro vínculos sem transformar possibilidade em garantia irrestrita.

**Conceito:** reescrita multifiltro.

**Pegadinha:** preservar tema e perder relações lógicas.

**Como pensar:** verifique uma a uma condição, modal, conector e referente.

**Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d1-exemplos-portugues).

---

# Dia 2 — UML: classes, objetos, sequência, comunicação, atividades e estados

## Questões principais

### S4D2Q051 — UML e processo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

Assinale a afirmação correta sobre UML.

A) É um processo com fases obrigatórias e invariáveis.
B) É uma linguagem de programação executável em qualquer ambiente.
C) É uma ferramenta específica para desenhar telas.
D) É uma linguagem de modelagem aplicável em processos distintos.

### S4D2Q052 — Perspectiva do diagrama

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

A equipe precisa evidenciar a ordem de mensagens entre interface, controlador e serviço. Qual diagrama responde mais diretamente?

A) Diagrama de sequência.
B) Diagrama de objetos.
C) Máquina de estados.
D) Diagrama de classes.

### S4D2Q053 — Classe e objeto

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

No modelo, “Protocolo” define atributos; “p17:Protocolo” possui situação EmAnalise. Eles representam, respectivamente:

A) dois casos de uso.
B) objeto e classe.
C) classe e instância.
D) dois atores.

### S4D2Q054 — Atributo e operação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

Em uma classe, “-situacao: Situacao” e “+protocolar(p: Pedido): Protocolo” indicam:

A) operação protegida e atributo de pacote.
B) duas multiplicidades de associação.
C) dois objetos concretos com valores atuais.
D) atributo privado e operação pública com retorno.

### S4D2Q055 — Escolha integrada de perspectivas

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

O revisor precisa responder: I. quais tipos se relacionam; II. quais valores existem no cenário; III. em que ordem ocorrem chamadas; IV. como o protocolo reage a eventos. A sequência adequada é:

A) casos de uso; componentes; classes; objetos.
B) classes; objetos; sequência; máquina de estados.
C) estados; sequência; classes; atividades.
D) objetos; classes; atividades; comunicação.

### S4D2Q056 — Visibilidade

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

Na notação usual de classe UML, o símbolo “-” antes de um atributo indica visibilidade:

A) privada.
B) de pacote.
C) pública.
D) protegida.

### S4D2Q057 — Multiplicidade opcional

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

A multiplicidade “0..1” em uma extremidade indica:

A) exatamente uma ocorrência obrigatória.
B) uma ou muitas ocorrências.
C) ausência permitida ou uma única ocorrência.
D) zero ou muitas ocorrências sem limite.

### S4D2Q058 — Leitura pelas extremidades

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Exemplos resolvidos — associação e multiplicidade](semana_04_estudo.md#s4-d2-exemplos-multiplicidade).

Em “Unidade 1 — 0..* Servidor”, qual leitura é correta?

A) Cada Servidor pode ligar-se a muitas Unidades, e cada Unidade a apenas um Servidor.
B) Servidor liga-se a uma Unidade; Unidade pode ter zero ou muitos Servidores.
C) Unidade e Servidor possuem necessariamente relação muitos para muitos.
D) Cada Unidade liga-se a um único Servidor, que pode não estar associado a Unidade alguma.

### S4D2Q059 — Associação estrutural

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

Uma associação UML representa predominantemente:

A) a autorização de segurança concedida ao usuário.
B) a ordem temporal obrigatória das mensagens.
C) a destruição conjunta de quaisquer objetos conectados.
D) um vínculo estrutural significativo entre classificadores.

### S4D2Q060 — Estrutura e instâncias integradas

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

O diagrama de classes define Profissional 1 — 0..* Requerimento. Uma fotografia mostra p1 ligado a r1 e r2; r3 sem Profissional. No recorte, qual avaliação é correta?

A) Todos os vínculos violam a regra porque um Profissional não pode ter dois Requerimentos.
B) p1–r1/r2 respeita a regra, mas r3 viola o “1” exigido na extremidade Profissional.
C) r3 é válido porque 0..* está escrito próximo de Requerimento.
D) O diagrama de objetos pode ignorar multiplicidades do modelo.

### S4D2Q061 — Generalização

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

Em uma generalização entre Fiscal e Servidor, o triângulo vazio aponta para:

A) o objeto criado primeiro em tempo de execução.
B) a classe que possui mais atributos privados.
C) Fiscal, porque toda seta aponta para o filho.
D) Servidor, o classificador mais geral.

### S4D2Q062 — Dependência

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

Uma operação recebe Formatador apenas como parâmetro temporário, sem guardar vínculo. A relação mínima adequada pode ser:

A) uma dependência de uso temporário.
B) associação obrigatória 1..1, independentemente do modelo.
C) composição, porque existe chamada de operação.
D) generalização, porque ambos participam da mesma operação.

### S4D2Q063 — Agregação compartilhada — comando negativo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

Sobre agregação compartilhada, assinale a alternativa **INCORRETA**.

A) O losango vazio fica na extremidade do todo, não na extremidade da parte.
B) A relação expressa uma forma fraca de todo-parte, sem impor destruição conjunta.
C) O losango vazio obriga destruição da parte quando o todo é destruído.
D) A semântica não deve ser inferida apenas porque objetos se contêm no código.

### S4D2Q064 — Composição

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

Processo é o todo; cada Peça pertence a um único Processo, não pode ser compartilhada e não permanece após a extinção do Processo. Qual modelagem preserva a força da relação e o lado do losango?

A) Associação simples, sem losango, porque a multiplicidade 1:N já expressa o ciclo de vida.
B) Agregação compartilhada, com losango vazio em Peça, pois a parte conhece o todo.
C) Composição, com losango preenchido em Processo, apoiada por exclusividade e ciclo de vida.
D) Dependência Peça→Processo, pois o uso do todo substitui qualquer vínculo estrutural.

### S4D2Q065 — Relações estruturais multifiltro

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — relações estruturais](semana_04_estudo.md#s4-d2-exemplos-relacoes).

Considere: Fiscal é Servidor; Relatório usa Formatador temporariamente; Processo possui Peça exclusiva e existencialmente dependente. As relações são:

A) dependência; associação 1..1; generalização.
B) generalização; dependência; composição.
C) associação; composição; dependência.
D) composição; generalização; agregação compartilhada.

### S4D2Q066 — Navegabilidade

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

Navegabilidade em uma associação indica:

A) capacidade modelada de navegar de uma extremidade à outra.
B) número mínimo e máximo de objetos relacionados.
C) permissão de segurança concedida ao usuário.
D) ordem cronológica de criação dos objetos.

### S4D2Q067 — Elemento abstrato

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

Em notação UML, o nome de uma classe em itálico pode indicar que ela é:

A) uma multiplicidade indefinida.
B) classe abstrata, sem instanciação direta.
C) uma mensagem assíncrona.
D) obrigatoriamente um objeto destruído.

### S4D2Q068 — Operação e método

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

A distinção conceitual adequada é:

A) operação e método nunca possuem relação entre si.
B) operação é valor de atributo; método é multiplicidade.
C) operação declara serviço; método realiza o comportamento.
D) operação existe somente em objeto; método somente em ator.

### S4D2Q069 — Papéis e multiplicidades

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

Nomes de papel em extremidades de associação servem para:

A) explicitar como cada classificador participa do vínculo.
B) substituir todas as multiplicidades por texto livre.
C) definir a ordem das mensagens de sequência.
D) indicar automaticamente visibilidade pública.

### S4D2Q070 — Modelo estrutural integrado

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — relações estruturais](semana_04_estudo.md#s4-d2-exemplos-relacoes).

Um Processo compõe 1..* Peças; cada Peça pertence a um Processo; um Fiscal, subtipo de Servidor, usa Formatador só durante exportação. Qual modelo preserva todos os fatos?

A) Generalização Processo→Peça; composição Servidor→Fiscal; associação Fiscal–Formatador 1..1.
B) Processo 1 ◆— 1..* Peça (composição); Fiscal→Servidor (generalização); Fiscal→Formatador (dependência).
C) Composição com losango em Peça; generalização Servidor→Fiscal; dependência Formatador→Fiscal.
D) Agregação Processo–Peça 0..*; associação Fiscal–Servidor; composição Fiscal–Formatador.

### S4D2Q071 — Finalidade da sequência

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

No diagrama de sequência, o tempo progride predominantemente:

A) pela espessura da linha de vida.
B) da direita para a esquerda obrigatoriamente.
C) do centro para as extremidades.
D) verticalmente, de cima para baixo.

### S4D2Q072 — Linha de vida

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

Uma linha de vida representa:

A) uma classe sem qualquer instância ou papel na interação.
B) a participação/existência de um elemento ao longo da interação.
C) a multiplicidade de uma associação estrutural.
D) um fluxo administrativo independente de mensagens.

### S4D2Q073 — Síncrona e assíncrona — comando negativo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

Sobre mensagens síncronas e assíncronas, assinale a alternativa **INCORRETA**.

A) A escolha depende da interação modelada, não apenas do nome da operação.
B) Uma mensagem de retorno pode ser omitida quando o contexto é claro.
C) Na chamada síncrona, o emissor normalmente aguarda a conclusão.
D) Toda mensagem assíncrona devolve imediatamente o valor necessário ao próximo passo.

### S4D2Q074 — Criação e destruição

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

Se um objeto nasce durante a interação e outro deixa de existir, a notação deve:

A) representar a criação por mensagem, mas manter as duas linhas completas desde o topo.
B) desenhar ambas as linhas do topo ao fim e usar ativações para marcar nascimento e morte.
C) iniciar as duas linhas no ponto de criação e encerrá-las juntas no fim da interação.
D) iniciar a linha do objeto criado na criação e encerrar a do objeto destruído na destruição.

### S4D2Q075 — Ordem e dependência de retorno

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — sequência](semana_04_estudo.md#s4-d2-exemplos-sequencia).

Controlador chama calcularPrazo(), usa o valor para registrarLimite() e depois notifica. Qual sequência preserva dependências?

A) registrarLimite → notificar → calcularPrazo → retorno.
B) calcularPrazo → retorno do prazo → registrarLimite → notificar.
C) notificar → calcularPrazo e registrarLimite em ordem irrelevante.
D) calcularPrazo e destruir o controlador antes do retorno.

### S4D2Q076 — Fragmento alt

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

Para representar dois caminhos alternativos selecionados por guardas, usa-se:

A) fragmento alt.
B) fragmento loop.
C) uma composição entre linhas de vida.
D) fragmento par.

### S4D2Q077 — Fragmento opt

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

Um único trecho executa somente se o usuário solicitar recibo. O operador adequado é:

A) alt sem segundo operando obrigatório em qualquer situação.
B) loop, porque a solicitação ocorre uma vez.
C) opt, com guarda da solicitação.
D) par, porque o recibo é independente da tela.

### S4D2Q078 — Fragmento loop

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

Para validar cada anexo enquanto houver item pendente, o fragmento mais apropriado é:

A) alt, pois cada anexo é um participante.
B) loop, com condição ou limites de repetição.
C) break, pois validar exige abandonar a interação sempre.
D) opt, pois todos os anexos são ignorados por padrão.

### S4D2Q079 — Fragmento par

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

No fragmento par, é correto afirmar que:

A) os operandos podem avançar em paralelo, preservadas as ordens internas relevantes.
B) todos os eventos tornam-se simultâneos no mesmo instante físico.
C) a numeração das mensagens deixa de ter significado em qualquer perspectiva.
D) somente um operando executa conforme guarda.

### S4D2Q080 — Interação com fragmentos integrados

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

O sistema repete validação por anexo; em cada item escolhe válido/inválido; após todos, dispara auditoria e notificação em paralelo. A combinação é:

A) loop contendo alt, seguido de par.
B) alt contendo loop, seguido de par.
C) loop contendo par, seguido de alt.
D) par contendo alt, seguido de loop.

### S4D2Q081 — Diagrama de comunicação

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Comunicação: vínculos e mensagens numeradas](semana_04_estudo.md#s4-d2-comunicacao).

O diagrama de comunicação enfatiza:

A) estados internos e transições por evento.
B) classes, atributos e herança sem mensagens.
C) participantes ligados e mensagens com ordem numérica.
D) fluxo de trabalho com fork e join.

### S4D2Q082 — Conversão sequência–comunicação

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — comunicação](semana_04_estudo.md#s4-d2-exemplos-comunicacao).

Em sequência, `solicitar()` ativa o controlador; durante essa execução ele chama `validar()` e, após o retorno, `salvar()`. Ao converter para comunicação e preservar ordem e aninhamento, qual numeração é coerente?

A) `1: solicitar()`; `1.1: salvar()`; `1.2: validar()`.
B) `1: solicitar()`; `1: validar()`; `1: salvar()`.
C) `1: solicitar()`; `1.1: validar()`; `1.2: salvar()`.
D) `1: solicitar()`; `2: validar()`; `1.1: salvar()`.

### S4D2Q083 — Final de atividade e de fluxo

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

Auditoria e notificação seguem em paralelo. Se o canal estiver indisponível, apenas a notificação deve terminar; a auditoria continua. Ao fim global, todo o comportamento deve encerrar. Qual solução preserva os dois alcances?

A) Final de atividade no ramo indisponível e final de fluxo no encerramento global.
B) Final de fluxo no ramo indisponível e final de atividade no encerramento global.
C) Join no ramo indisponível e merge no encerramento global.
D) Final de atividade nos dois pontos, pois ambos representam término local.

### S4D2Q084 — Decisão e merge

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

Após validar documentos, exatamente um caminho executa: analisar mérito se completos ou solicitar complemento se incompletos. Concluído o caminho escolhido, deve-se registrar andamento sem esperar pelo outro. Usa-se:

A) decisão para separar e merge para reunir os caminhos alternativos.
B) fork para separar e join para sincronizar os caminhos concorrentes.
C) decisão para separar e join para aguardar a conclusão dos dois caminhos.
D) fork para separar e merge para prosseguir após o primeiro caminho concluído.

### S4D2Q085 — Atividade multifiltro

**Nível:** Muito difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — atividades](semana_04_estudo.md#s4-d2-exemplos-atividades).

Após protocolo, cadastro e documentos são verificados em paralelo; ambos devem terminar; então, conforme resultado, deferir ou solicitar correção; depois registrar andamento. A sequência de nós é:

A) fork → ações → merge → decisão → dois joins.
B) join inicial → loop → final de fluxo antes da decisão.
C) decisão → ações paralelas → merge → join → registro.
D) fork → ações paralelas → join → decisão → ramos → merge → registro.

### S4D2Q086 — Nó inicial

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

O nó inicial de uma atividade:

A) representa automaticamente o ator primário.
B) marca o ponto inicial do fluxo da atividade.
C) encerra somente o ramo que o alcança.
D) sincroniza todos os ramos concorrentes.

### S4D2Q087 — Fluxo de objeto

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

Um fluxo de objeto, diferentemente do mero fluxo de controle, evidencia:

A) herança entre as ações.
B) multiplicidade de classes associadas.
C) visibilidade privada de uma operação.
D) dados ou objetos que passam entre ações.

### S4D2Q088 — Raias

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

Receber, analisar e notificar pertencem, respectivamente, à Unidade, à Comissão e ao Sistema; a ordem deve permanecer receber→analisar→notificar, sem paralelismo implícito. Qual modelagem evidencia responsabilidade sem alterar o fluxo?

A) Guardas com o nome das unidades, escolhendo apenas um responsável para toda a atividade.
B) Generalização entre Unidade, Comissão e Sistema, herdando a sequência das ações.
C) Raias para os responsáveis, mantendo fluxos de controle que preservem a ordem informada.
D) Fork ao entrar em cada raia, para executar as três ações simultaneamente.

### S4D2Q089 — Guardas de decisão

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

Em uma decisão, guardas adequadas devem:

A) coincidir com nomes de raias, pois a responsabilidade define a condição.
B) ser simultaneamente verdadeiras para liberar todos os caminhos de saída.
C) usar multiplicidades para limitar quantas vezes cada caminho é percorrido.
D) cobrir os casos previstos sem sobreposição indesejada entre condições.

### S4D2Q090 — Merge versus join integrado

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — atividades](semana_04_estudo.md#s4-d2-exemplos-atividades).

Um modelo usa merge para reunir duas verificações realmente paralelas e join para reunir caminhos “aprovado”/“rejeitado”, dos quais só um ocorre. Qual correção é necessária?

A) Manter ambos porque merge e join são semanticamente idênticos.
B) Trocar o primeiro por join e o segundo por merge.
C) Trocar os dois por fork, pois todas as linhas devem ser divididas.
D) Trocar os dois por final de atividade e continuar depois.

### S4D2Q091 — Estado, evento e transição

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

Uma transição de máquina de estados descreve:

A) uma passagem entre estados que pode ter gatilho, guarda e efeito.
B) uma mensagem numerada trocada entre participantes de uma colaboração.
C) uma partição de responsabilidades atribuídas às ações de uma atividade.
D) um vínculo estrutural entre classificadores, qualificado por multiplicidade.

### S4D2Q092 — Evento, guarda e efeito

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

No rótulo “decidir [documentosValidos] / registrarDecisao”, os elementos são:

A) evento decidir; guarda documentosValidos; efeito registrarDecisao.
B) efeito decidir; multiplicidade documentosValidos; ator registrarDecisao.
C) guarda decidir; efeito documentosValidos; estado registrarDecisao.
D) estado decidir; evento documentosValidos; classe registrarDecisao.

### S4D2Q093 — Ações entry, do e exit

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

Em um estado, “entry”, “do” e “exit” correspondem, respectivamente, a comportamentos:

A) ao sair, ao entrar e durante a permanência.
B) ao entrar, durante a permanência e ao sair.
C) de classe, de objeto e de componente.
D) de decisão, merge e join.

### S4D2Q094 — Transição interna — comando negativo

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

O estado `EmAnalise` possui `entry/carregar`, `do/monitorar` e `exit/liberar`. O evento `atualizar` deve alterar dados sem executar saída/entrada; `reiniciar` deve executar saída e nova entrada. Assinale a alternativa **INCORRETA**.

A) Uma transição interna em `atualizar` pode executar seu efeito sem acionar `exit/liberar` e `entry/carregar`.
B) Uma auto-transição externa em `reiniciar` sai e reentra em `EmAnalise`, permitindo executar `exit` e `entry`.
C) Trocar a auto-transição de `reiniciar` por uma interna mudaria o comportamento exigido pelas ações do estado.
D) Como o estado aparente é o mesmo, a transição interna pode substituir a auto-transição sem alterar as ações executadas.

### S4D2Q095 — Estados e guardas integrados

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Exemplos resolvidos — máquinas de estados](semana_04_estudo.md#s4-d2-exemplos-estados).

Em `EmAnalise`, o evento `decidir` deve levar a `Deferido` se os documentos forem válidos e houver aprovação; levar a `Indeferido` se forem válidos e não houver aprovação; e solicitar correção, sem executar `exit`/`entry`, se forem inválidos. Qual modelo preserva todos os requisitos?

A) Usar um fork após `decidir`, entrar nos dois estados-alvo e cancelar depois o ramo incompatível.
B) Usar duas transições sem guarda aos estados-alvo e uma auto-transição externa para documentos inválidos.
C) Usar duas transições guardadas aos estados-alvo e uma transição interna para inválidos, com o efeito de correção.
D) Usar apenas auto-transições externas em `EmAnalise` e registrar deferimento ou indeferimento como efeitos.

### S4D2Q096 — Pseudestado inicial

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

O pseudestado inicial indica:

A) a entrada padrão da região da máquina de estados.
B) um objeto de classe abstrata.
C) o término de apenas um fluxo de atividade.
D) uma mensagem de criação assíncrona.

### S4D2Q097 — Estado final

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

Alcançar um estado final em uma região indica:

A) retorno automático ao pseudestado inicial.
B) destruição obrigatória de todas as instâncias do sistema.
C) sincronização de fluxos concorrentes de atividade.
D) conclusão do comportamento daquela região conforme o modelo.

### S4D2Q098 — Estado composto

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

Um estado composto é útil para:

A) substituir qualquer atividade paralela por multiplicidade.
B) representar herança entre classes.
C) mostrar mensagens numeradas entre objetos.
D) agrupar subestados e detalhar o comportamento interno.

### S4D2Q099 — Histórico — comando negativo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

Sobre pseudestado de histórico, assinale a alternativa **INCORRETA**.

A) Pode ser usado em estado composto para retomar configuração anterior.
B) Seu significado depende do tipo de histórico modelado.
C) Ele é obrigatoriamente um log de auditoria persistido no banco.
D) Não substitui, por si, requisitos de rastreabilidade institucional.

### S4D2Q100 — Caso UML integrado

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Prática guiada — quatro perspectivas](semana_04_estudo.md#s4-d2-pratica).

No caso do requerimento: tipos e multiplicidades; chamadas de validação; verificações paralelas; e ciclo Rascunho→Protocolado→EmAnalise. Qual combinação preserva cada perspectiva?

A) Classes para tipos; comunicação sem numeração para chamadas; atividades com merge para paralelismo; estados sem eventos.
B) Classes para tipos; sequência para chamadas; atividades com fork/join; estados com eventos e guardas.
C) Objetos para tipos; sequência para chamadas; atividades com fork sem join; estados com guardas sem eventos.
D) Classes para tipos; sequência para chamadas; atividades com decisão/merge; objetos para o ciclo reativo.

## Questões extras dos blocos fixos do Dia 2

#### Extra Dia 2.1

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** princípios do art. 37
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

No exercício da função administrativa, a busca de eficiência:

A) permite descumprir regra sempre que houver economia.
B) substitui impessoalidade quando o gestor conhece o interessado.
C) deve ocorrer dentro da legalidade e dos demais princípios aplicáveis.
D) dispensa motivação de toda decisão automatizada.

#### Extra Dia 2.2

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** publicidade e impessoalidade
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

Uma campanha divulga serviço público necessário, mas centraliza nome, imagem e slogan pessoal da autoridade, sem relação educativa com o conteúdo. Qual diagnóstico preserva o dever de informar e a vedação à promoção pessoal?

A) A publicidade proíbe divulgar o serviço, pois comunicação institucional é incompatível com a função administrativa.
B) A eficiência autoriza personalização sempre que o alcance crescer, ainda que a mensagem promova a autoridade.
C) A finalidade pública afasta a impessoalidade, desde que nome e imagem acompanhem informação verdadeira.
D) A divulgação do serviço pode atender à publicidade, mas o destaque pessoal viola a impessoalidade.

#### Extra Dia 2.3

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** anulação e revogação
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

Um ato apresenta vício insanável de legalidade. A retirada correspondente é, em regra, tratada como:

A) publicidade.
B) revogação.
C) desconcentração.
D) anulação.

#### Extra Dia 2.4

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** anulação e revogação
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

Um ato válido deixou de ser conveniente, e a matéria admite retirada por mérito. O instituto adequado é:

A) revogação por mérito.
B) anulação por vício inexistente.
C) convalidação do mérito.
D) descentralização da decisão.

#### Extra Dia 2.5

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** atos administrativos
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

Considere: I. ato com vício insanável; II. ato válido, mas inconveniente; III. vício sanável em hipótese juridicamente admitida. Os tratamentos correspondentes são:

A) convalidação; revogação; anulação.
B) anulação; convalidação; revogação.
C) revogação; anulação; convalidação.
D) anulação; revogação; convalidação.

#### Extra Dia 2.6

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** organização administrativa
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

Uma pessoa administrativa distribui competências entre unidades internas, sem criar nova pessoa jurídica. Ocorre:

A) composição administrativa.
B) desconcentração interna.
C) descentralização por criação de entidade.
D) revogação da personalidade anterior.

#### Extra Dia 2.7

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** organização administrativa
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

Quando a execução é transferida a outra pessoa jurídica nos termos aplicáveis, há:

A) desconcentração.
B) convalidação.
C) descentralização.
D) impessoalidade.

#### Extra Dia 2.8

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** órgãos e entidades
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

Sobre órgãos e distribuição interna, assinale a alternativa **INCORRETA**.

A) A ausência de nova pessoa distingue o caso de descentralização.
B) A estrutura interna não deve ser confundida com transferência a entidade.
C) A desconcentração pode distribuir competências entre órgãos internos.
D) Todo órgão criado por desconcentração possui personalidade jurídica própria.

#### Extra Dia 2.9

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** elementos do ato
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

Competência, finalidade, forma, motivo e objeto são recuperados no bloco como:

A) tipos de descentralização territorial.
B) princípios exclusivos da modelagem UML.
C) elementos ou requisitos do ato administrativo.
D) fases obrigatórias de qualquer projeto de software.

#### Extra Dia 2.10

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** diagnóstico integrado
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

Uma unidade interna foi criada sem nova pessoa; depois, ato válido tornou-se inconveniente; campanha atribuiu resultado institucional ao dirigente. Os diagnósticos são:

A) desconcentração; revogação, se cabível; violação à impessoalidade.
B) descentralização; anulação por ilegalidade; observância da publicidade.
C) desconcentração; convalidação do mérito; violação à eficiência.
D) descentralização; revogação, se cabível; violação à legalidade.

#### Extra Dia 2.11

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

Assinale a frase com concordância adequada.

A) A ordem das mensagens evidenciam as sequências.
B) A ordem das mensagens evidencia a sequência.
C) As ordem das mensagens evidencia a sequência.
D) A ordem das mensagens evidenciam a sequência.

#### Extra Dia 2.12

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

Com sujeito composto anteposto, a redação adequada é:

A) Decisão e merge possuem funções distintas.
B) Decisão e merge possuir funções distintas.
C) Decisão e merge possui funções distintas.
D) Decisão e merge possuí funções distintas.

#### Extra Dia 2.13

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pontuação
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

Assinale a pontuação adequada no período simples.

A) A análise cuidadosa das guardas, reduz ambiguidades.
B) A análise cuidadosa das guardas reduz ambiguidades.
C) A análise, cuidadosa das guardas reduz ambiguidades.
D) A análise cuidadosa, das guardas, reduz ambiguidades.

#### Extra Dia 2.14

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** orações relativas
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

Um relatório informa que existem 30 processos e que apenas 12 possuem recurso. Para afirmar que somente esses 12 aguardam análise, qual redação preserva o alcance?

A) Os processos que possuem recurso aguardam análise.
B) Os processos, que possuem recurso, aguardam análise.
C) Aguardam análise os processos, os quais possuem recurso.
D) Os processos aguardam análise, porque possuem recurso.

#### Extra Dia 2.15

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita
- **Nível:** Muito difícil
- **Uso:** Revisão
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

Original: “Após a validação, decisão e merge mantêm funções distintas, que o diagrama evidencia.” Qual reescrita preserva concordância, referência e sentido?

A) Após a validação, o diagrama evidencia que decisão e merge mantém funções distintas.
B) O diagrama evidencia, após a validação, que decisão e merge mantêm função distinta.
C) O diagrama evidencia que decisão e merge, após a validação, mantêm funções distintas.
D) Decisão e merge, após a validação, mantêm funções distintas, onde o diagrama evidencia.

#### Extra Dia 2.16

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pronomes relativos
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

Assinale o emprego adequado de “cujo”.

A) O processo cujo o prazo venceu foi revisado.
B) O processo cujo venceu o prazo foi revisado.
C) O processo cujo prazo venceu foi revisado.
D) O processo que cujo prazo venceu foi revisado.

#### Extra Dia 2.17

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pronomes relativos
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

Qual frase emprega “onde” com valor locativo adequado?

A) A decisão onde o gestor aprovou foi publicada.
B) O prazo onde termina amanhã foi alterado.
C) O requisito onde define o prazo foi revisado.
D) A unidade onde o atendimento ocorre foi reformada.

#### Extra Dia 2.18

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pontuação
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

Assinale a alternativa **INCORRETA** quanto à pontuação.

A) A leitura das multiplicidades, revela a regra.
B) A equipe corrigiu o modelo após a revisão.
C) Após a revisão, a equipe corrigiu o modelo.
D) A equipe, após a revisão, corrigiu o modelo.

#### Extra Dia 2.19

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância e oração relativa
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

Somente parte dos diagramas representa interações; esses são os que preservam a ordem. Qual redação mantém concordância e alcance restritivo?

A) Os diagramas, que representam interações, preservam a ordem das mensagens.
B) Os diagramas que representam interações preservam a ordem das mensagens.
C) Os diagramas que representa interações preservam a ordem das mensagens.
D) Os diagramas que representam interações preserva a ordem das mensagens.

#### Extra Dia 2.20

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** revisão integrada
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

Rascunho: “A sequência das mensagens, mostram os serviços onde depende o protocolo, que foram validado.” Qual revisão corrige concordância, vírgula, relativo e referente?

A) As sequência da mensagem mostra, os serviço que depende o protocolo validado.
B) A sequência das mensagens mostra os serviços dos quais o protocolo depende e que foram validados.
C) A sequência, das mensagens mostram os serviços cujo o protocolo depende e foi validados.
D) A sequência das mensagens mostram os serviços onde o protocolo dependem, que foi validado.

## Gabarito do Dia 2

### Gabarito das questões principais

| Questão | Resposta |
|---:|:---:|
| 51 | D |
| 52 | A |
| 53 | C |
| 54 | D |
| 55 | B |
| 56 | A |
| 57 | C |
| 58 | B |
| 59 | D |
| 60 | B |
| 61 | D |
| 62 | A |
| 63 | C |
| 64 | C |
| 65 | B |
| 66 | A |
| 67 | B |
| 68 | C |
| 69 | A |
| 70 | B |
| 71 | D |
| 72 | B |
| 73 | D |
| 74 | D |
| 75 | B |
| 76 | A |
| 77 | C |
| 78 | B |
| 79 | A |
| 80 | A |
| 81 | C |
| 82 | C |
| 83 | D |
| 84 | A |
| 85 | D |
| 86 | B |
| 87 | D |
| 88 | C |
| 89 | D |
| 90 | B |
| 91 | A |
| 92 | A |
| 93 | B |
| 94 | D |
| 95 | C |
| 96 | A |
| 97 | B |
| 98 | D |
| 99 | C |
| 100 | B |

### Gabarito das questões extras

| Extra | Resposta |
|---:|:---:|
| 2.1 | C |
| 2.2 | D |
| 2.3 | D |
| 2.4 | A |
| 2.5 | D |
| 2.6 | B |
| 2.7 | C |
| 2.8 | D |
| 2.9 | C |
| 2.10 | A |
| 2.11 | B |
| 2.12 | A |
| 2.13 | B |
| 2.14 | A |
| 2.15 | C |
| 2.16 | C |
| 2.17 | D |
| 2.18 | A |
| 2.19 | B |
| 2.20 | B |

## Comentários do Dia 2

### Comentário S4D2Q051

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. UML não define por si um processo de desenvolvimento.
- **B)** Incorreta. Modelagem não equivale a linguagem de programação universal.
- **C)** Incorreta. UML é independente de uma única ferramenta e possui escopo mais amplo.
- **D)** Correta. A notação não impõe sozinha ciclo de vida ou ferramenta.

**Conceito:** natureza da UML.

**Pegadinha:** confundir linguagem, processo e ferramenta.

**Como pensar:** separe notação, método de trabalho e produto de software.

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

### Comentário S4D2Q052

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O eixo temporal vertical destaca a precedência das mensagens.
- **B)** Incorreta. Ele mostra uma fotografia de instâncias e valores.
- **C)** Incorreta. Ela enfatiza reação de um objeto a eventos conforme estado.
- **D)** Incorreta. Ele enfatiza tipos e relações estruturais.

**Conceito:** seleção de diagrama.

**Pegadinha:** escolher pela presença de objetos.

**Como pensar:** identifique qual pergunta o modelo precisa responder.

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

### Comentário S4D2Q053

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Os elementos não expressam objetivos de interação.
- **B)** Incorreta. A ordem entre descrição e ocorrência foi invertida.
- **C)** Correta. O primeiro descreve o tipo; o segundo, ocorrência com valor.
- **D)** Incorreta. Nenhum dos dois é papel externo por essa descrição.

**Conceito:** classe versus objeto UML.

**Pegadinha:** confundir tipo com ocorrência nomeada.

**Como pensar:** procure nome de tipo e valor concreto.

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

### Comentário S4D2Q054

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Símbolos e naturezas foram invertidos.
- **B)** Incorreta. A notação está dentro dos compartimentos da classe.
- **C)** Incorreta. Não há especificação de instância nem slots.
- **D)** Correta. A notação combina visibilidade, nome, tipo, assinatura e retorno.

**Conceito:** notação de atributo e operação.

**Pegadinha:** ler sinais como aritmética.

**Como pensar:** separe visibilidade, nome, parâmetros e tipo.

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

### Comentário S4D2Q055

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. As perspectivas não respondem às quatro perguntas.
- **B)** Correta. Cada diagrama enfatiza exatamente estrutura, fotografia, tempo e ciclo reativo.
- **C)** Incorreta. A ordem associa perguntas a diagramas incompatíveis.
- **D)** Incorreta. Troca estrutura/fotografia e não focaliza ciclo reativo.

**Conceito:** seleção multifiltro de diagramas.

**Pegadinha:** usar um diagrama para toda pergunta.

**Como pensar:** classifique cada dúvida como estrutura, instância, interação ou estado.

**Referência:** [UML: linguagem, modelo e perspectiva](semana_04_estudo.md#s4-d2-uml).

### Comentário S4D2Q056

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O sinal menos representa acesso privado no classificador.
- **B)** Incorreta. A visibilidade de pacote é representada por “~”.
- **C)** Incorreta. A visibilidade pública é representada por “+”.
- **D)** Incorreta. A visibilidade protegida é representada por “#”.

**Conceito:** visibilidade UML.

**Pegadinha:** interpretar o sinal como operação matemática.

**Como pensar:** recupere + público, - privado, # protegido e ~ pacote.

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

### Comentário S4D2Q057

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Isso seria multiplicidade 1.
- **B)** Incorreta. Isso seria 1..*.
- **C)** Correta. O mínimo é zero e o máximo é um.
- **D)** Incorreta. Isso seria 0..* ou *.

**Conceito:** multiplicidade 0..1.

**Pegadinha:** ler apenas o limite máximo.

**Como pensar:** leia mínimo e máximo separadamente.

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

### Comentário S4D2Q058

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Exemplos resolvidos — associação e multiplicidade](semana_04_estudo.md#s4-d2-exemplos-multiplicidade).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Inverte o lado 0..* e ignora o mínimo.
- **B)** Correta. A marca junto a cada extremidade é lida fixando uma instância da oposta.
- **C)** Incorreta. Somente um lado admite muitos no recorte.
- **D)** Incorreta. Inverte a multiplicidade da extremidade Servidor.

**Conceito:** leitura de multiplicidade.

**Pegadinha:** ler a marca pelo elemento visualmente mais próximo.

**Como pensar:** fixe um objeto de um lado e leia quantos do outro.

**Referência:** [Exemplos resolvidos — associação e multiplicidade](semana_04_estudo.md#s4-d2-exemplos-multiplicidade).

### Comentário S4D2Q059

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Navegabilidade ou vínculo não equivale a permissão.
- **B)** Incorreta. Ordem de interação é foco de sequência/comunicação.
- **C)** Incorreta. Somente composição forte possui semântica específica de ciclo.
- **D)** Correta. A relação registra conexões possíveis e propriedades de extremidade.

**Conceito:** associação UML.

**Pegadinha:** atribuir à linha qualquer semântica.

**Como pensar:** procure vínculo estrutural e examine as propriedades das extremidades.

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

### Comentário S4D2Q060

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O lado Requerimento admite muitos por Profissional.
- **B)** Correta. A fotografia é confrontada com a multiplicidade para cada Requerimento.
- **C)** Incorreta. Para um Requerimento, deve-se ler a extremidade Profissional igual a 1.
- **D)** Incorreta. Instâncias válidas devem respeitar as restrições aplicáveis.

**Conceito:** consistência entre classe, objeto e multiplicidade.

**Pegadinha:** validar apenas um lado da associação.

**Como pensar:** fixe cada ocorrência e verifique as duas extremidades.

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

### Comentário S4D2Q061

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A relação não expressa ordem de criação.
- **B)** Incorreta. Quantidade de atributos não decide hierarquia.
- **C)** Incorreta. A direção foi invertida.
- **D)** Correta. A seta de generalização vai do específico ao geral.

**Conceito:** direção da generalização.

**Pegadinha:** decidir pelo desenho sem teste 'é um'.

**Como pensar:** identifique específico, geral e direção do triângulo.

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

### Comentário S4D2Q062

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O cliente usa o fornecedor sem estrutura duradoura informada.
- **B)** Incorreta. Não foi informado vínculo persistente.
- **C)** Incorreta. Uso temporário não prova todo-parte nem ciclo de vida.
- **D)** Incorreta. Participação não estabelece relação é-um.

**Conceito:** dependência versus associação.

**Pegadinha:** transformar toda chamada em associação.

**Como pensar:** verifique se o vínculo é estrutural ou apenas uso.

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

### Comentário S4D2Q063

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

**Gabarito: C (a afirmação incorreta).**

**Análise das alternativas:**

- **A)** Correta. A notação posiciona o losango no agregador.
- **B)** Correta. Essa é a intenção usual da agregação compartilhada.
- **C)** Incorreta. Essa dependência forte não decorre da agregação compartilhada.
- **D)** Correta. O domínio precisa justificar o vínculo.

**Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.

**Conceito:** agregação compartilhada.

**Pegadinha:** atribuir semântica de composição ao losango vazio.

**Como pensar:** confira tipo do losango, lado do todo e ciclo de vida.

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

### Comentário S4D2Q064

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Multiplicidade limita quantidade, mas não expressa sozinha exclusividade de composição nem dependência de ciclo de vida.
- **B)** Incorreta. A agregação compartilhada é fraca e, além disso, o losango foi colocado na parte.
- **C)** Correta. O losango preenchido fica no Processo, e exclusividade e ciclo de vida sustentam a composição.
- **D)** Incorreta. Dependência representa uso, não a relação estrutural forte informada entre todo e parte.

**Conceito:** composição.

**Pegadinha:** usar composição para qualquer colaboração.

**Como pensar:** teste todo-parte, exclusividade e dependência existencial.

**Referência:** [Generalização, dependência, agregação e composição](semana_04_estudo.md#s4-d2-relacoes-estruturais).

### Comentário S4D2Q065

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — relações estruturais](semana_04_estudo.md#s4-d2-exemplos-relacoes).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Ignora especialização e ciclo de vida.
- **B)** Correta. Os três fatos expressam, respectivamente, é-um, uso e todo-parte forte.
- **C)** Incorreta. As semânticas foram deslocadas entre os casos.
- **D)** Incorreta. Nenhum dos três rótulos atende completamente aos fatos.

**Conceito:** diagnóstico integrado de relações UML.

**Pegadinha:** escolher uma relação pela mera existência de ligação.

**Como pensar:** aplique 'é um', uso, vínculo estrutural e ciclo de vida.

**Referência:** [Exemplos resolvidos — relações estruturais](semana_04_estudo.md#s4-d2-exemplos-relacoes).

### Comentário S4D2Q066

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Trata acesso estrutural no modelo, não quantidade ou privilégio.
- **B)** Incorreta. Isso é multiplicidade.
- **C)** Incorreta. Controle de acesso não é inferido da seta.
- **D)** Incorreta. A associação não determina sequência temporal.

**Conceito:** navegabilidade.

**Pegadinha:** confundir seta com autorização ou cardinalidade.

**Como pensar:** separe direção de navegação, quantidade e segurança.

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

### Comentário S4D2Q067

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Multiplicidade usa intervalos nas extremidades.
- **B)** Correta. Itálico é notação usual para elemento abstrato.
- **C)** Incorreta. Mensagem não é indicada pelo estilo do nome da classe.
- **D)** Incorreta. Destruição pertence a interações/linhas de vida.

**Conceito:** classe abstrata.

**Pegadinha:** ler estilo tipográfico como estado de execução.

**Como pensar:** associe itálico à abstração no classificador.

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

### Comentário S4D2Q068

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Método pode implementar uma operação.
- **B)** Incorreta. Os conceitos pertencem a categorias diferentes.
- **C)** Correta. Separa contrato comportamental e realização.
- **D)** Incorreta. A distinção não depende desses diagramas.

**Conceito:** operação versus método.

**Pegadinha:** usar os termos como sinônimos absolutos.

**Como pensar:** separe serviço declarado de realização.

**Referência:** [Classes, objetos, atributos, operações e visibilidade](semana_04_estudo.md#s4-d2-classes-objetos).

### Comentário S4D2Q069

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. O papel dá significado contextual à extremidade.
- **B)** Incorreta. Papel e multiplicidade têm funções distintas.
- **C)** Incorreta. Ordem temporal não é função do papel da associação.
- **D)** Incorreta. Papel não determina visibilidade por si.

**Conceito:** papéis de associação.

**Pegadinha:** confundir propriedades de extremidade.

**Como pensar:** leia nome, multiplicidade e navegabilidade separadamente.

**Referência:** [Associação, papéis, navegabilidade e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

### Comentário S4D2Q070

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — relações estruturais](semana_04_estudo.md#s4-d2-exemplos-relacoes).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Processo não é especialização de Peça, Fiscal não compõe Servidor e uso temporário não exige associação 1..1.
- **B)** Correta. A composição preserva todo e cardinalidade; a generalização aponta ao geral; a dependência representa uso transitório.
- **C)** Incorreta. Inverte o todo da composição, a direção da generalização e o cliente da dependência.
- **D)** Incorreta. Enfraquece o ciclo de vida, perde a relação é-um e transforma uso temporário em composição.

**Conceito:** modelagem estrutural multifiltro.

**Pegadinha:** resolver relações sem conferir multiplicidade e ciclo.

**Como pensar:** para cada vínculo, teste tipo, direção, cardinalidade e existência.

**Referência:** [Exemplos resolvidos — relações estruturais](semana_04_estudo.md#s4-d2-exemplos-relacoes).

### Comentário S4D2Q071

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Espessura não define precedência.
- **B)** Incorreta. O eixo horizontal organiza participantes.
- **C)** Incorreta. Não há essa convenção temporal.
- **D)** Correta. A posição vertical das ocorrências expressa ordem temporal.

**Conceito:** eixo temporal da sequência.

**Pegadinha:** ler o eixo horizontal como tempo.

**Como pensar:** siga as mensagens verticalmente.

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

### Comentário S4D2Q072

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A linha representa participante específico no recorte.
- **B)** Correta. Ela organiza ocorrências e execuções do participante.
- **C)** Incorreta. Cardinalidade pertence ao modelo estrutural.
- **D)** Incorreta. Esse foco é típico de atividades.

**Conceito:** linha de vida.

**Pegadinha:** confundir participante com classe inteira.

**Como pensar:** identifique quem participa e quando existe.

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

### Comentário S4D2Q073

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

**Gabarito: D (a afirmação incorreta).**

**Análise das alternativas:**

- **A)** Correta. O comportamento e a dependência importam.
- **B)** Correta. A omissão visual não elimina necessariamente o retorno semântico.
- **C)** Correta. A espera é característica típica dessa semântica.
- **D)** Incorreta. Envio assíncrono não garante retorno imediato para dependência subsequente.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** mensagens síncronas e assíncronas.

**Pegadinha:** inferir resposta imediata de qualquer envio.

**Como pensar:** procure dependência de conclusão e valor.

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

### Comentário S4D2Q074

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. A mensagem de criação não corrige uma linha desenhada antes da existência, nem representa a destruição do outro objeto.
- **B)** Incorreta. Especificação de execução não substitui o início e o término da linha de vida.
- **C)** Incorreta. Criação e destruição pertencem a objetos distintos e não devem ser aplicadas às duas linhas em conjunto.
- **D)** Correta. Cada linha começa ou termina no evento que delimita a existência do respectivo objeto.

**Conceito:** criação e destruição em sequência.

**Pegadinha:** representar existência apenas por texto.

**Como pensar:** alinhe começo e fim da linha aos eventos.

**Referência:** [Sequência: linhas de vida, mensagens e ocorrências](semana_04_estudo.md#s4-d2-sequencia).

### Comentário S4D2Q075

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Exemplos resolvidos — sequência](semana_04_estudo.md#s4-d2-exemplos-sequencia).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Usa o prazo antes de obtê-lo.
- **B)** Correta. O registro depende do valor; a notificação vem após persistência no cenário.
- **C)** Incorreta. A notificação antecipada e a perda de dependência contradizem o caso.
- **D)** Incorreta. A destruição impediria as ações subsequentes modeladas.

**Conceito:** ordenação causal de mensagens.

**Pegadinha:** ordenar pelo nome e não pela dependência.

**Como pensar:** marque que valor cada mensagem produz e consome.

**Referência:** [Exemplos resolvidos — sequência](semana_04_estudo.md#s4-d2-exemplos-sequencia).

### Comentário S4D2Q076

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Cada operando corresponde a alternativa condicional.
- **B)** Incorreta. Loop representa repetição.
- **C)** Incorreta. Composição é relação estrutural entre classificadores.
- **D)** Incorreta. Par representa potencial de execução paralela.

**Conceito:** fragmento alt.

**Pegadinha:** escolher par porque há dois blocos.

**Como pensar:** pergunte se executa um caminho ou vários em paralelo.

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

### Comentário S4D2Q077

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Opt expressa diretamente a condição única.
- **B)** Incorreta. Ocorrer uma vez não caracteriza repetição.
- **C)** Correta. Opt modela trecho condicional sem alternativa obrigatória.
- **D)** Incorreta. Independência não implica concorrência no caso.

**Conceito:** fragmento opt.

**Pegadinha:** usar alt para toda condição isolada.

**Como pensar:** se há apenas bloco opcional, escolha opt.

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

### Comentário S4D2Q078

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Alt escolhe alternativas, não iteração.
- **B)** Correta. A mesma sequência se repete para a coleção/condição.
- **C)** Incorreta. Break interrompe a interação envolvente sob condição.
- **D)** Incorreta. A obrigatoriedade descrita é repetitiva, não meramente opcional.

**Conceito:** fragmento loop.

**Pegadinha:** tratar repetição como alternativas independentes.

**Como pensar:** procure comportamento reiterado e condição de parada.

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

### Comentário S4D2Q079

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Par relaxa a ordem total entre os operandos.
- **B)** Incorreta. Par permite intercalação/concorrência, não exige simultaneidade absoluta.
- **C)** Incorreta. As ordens internas continuam importantes.
- **D)** Incorreta. Essa é semântica de alternativa.

**Conceito:** fragmento par.

**Pegadinha:** equiparar concorrência a simultaneidade total.

**Como pensar:** distinga ordem dentro do operando e entre operandos.

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

### Comentário S4D2Q080

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A estrutura representa repetição, escolha por item e concorrência final.
- **B)** Incorreta. Colocar `alt` fora de `loop` escolhe um ramo antes da repetição, em vez de decidir validade a cada anexo.
- **C)** Incorreta. O `par` dentro do `loop` cria concorrência durante cada validação e deixa a alternativa para depois do conjunto.
- **D)** Incorreta. Inicia a concorrência antes da escolha e transfere a repetição para o fim, alterando as três dependências.

**Conceito:** composição de fragmentos combinados.

**Pegadinha:** escolher operador pela quantidade de blocos.

**Como pensar:** identifique primeiro repetição, depois escolha, depois concorrência.

**Referência:** [Fragmentos combinados, guardas e repetição](semana_04_estudo.md#s4-d2-fragmentos).

### Comentário S4D2Q081

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Comunicação: vínculos e mensagens numeradas](semana_04_estudo.md#s4-d2-comunicacao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Esse é o foco da máquina de estados.
- **B)** Incorreta. Esse é o foco estrutural de classes.
- **C)** Correta. A topologia de colaboração fica mais visível.
- **D)** Incorreta. Esse é o foco de atividades.

**Conceito:** diagrama de comunicação.

**Pegadinha:** afirmar que ele não possui ordem.

**Como pensar:** procure vínculos e números das mensagens.

**Referência:** [Comunicação: vínculos e mensagens numeradas](semana_04_estudo.md#s4-d2-comunicacao).

### Comentário S4D2Q082

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — comunicação](semana_04_estudo.md#s4-d2-exemplos-comunicacao).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Numera `salvar()` antes de `validar()` e inverte a dependência informada.
- **B)** Incorreta. Repetir `1` apaga a ordem e o aninhamento das chamadas internas.
- **C)** Correta. `1.1` e `1.2` preservam, dentro de `solicitar()`, a precedência entre validação e persistência.
- **D)** Incorreta. A numeração mistura uma chamada externa `2` com uma chamada interna posterior `1.1`, perdendo a estrutura original.

**Conceito:** equivalência entre perspectivas de interação.

**Pegadinha:** preservar objetos e perder ordem.

**Como pensar:** converta posição vertical em numeração consistente.

**Referência:** [Exemplos resolvidos — comunicação](semana_04_estudo.md#s4-d2-exemplos-comunicacao).

### Comentário S4D2Q083

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O final de atividade no ramo local encerraria também a auditoria, e o final de fluxo não produziria o término global pedido.
- **B)** Correta. O final de fluxo encerra só a notificação, enquanto o final de atividade encerra o comportamento completo.
- **C)** Incorreta. Join e merge tratam reunião de fluxos; não substituem os dois alcances de término exigidos.
- **D)** Incorreta. Final de atividade possui alcance global, portanto não representa o encerramento isolado da notificação.

**Conceito:** nós finais de atividade.

**Pegadinha:** tratar todo símbolo final como global.

**Como pensar:** pergunte qual escopo é encerrado.

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

### Comentário S4D2Q084

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Os caminhos não coexistem, portanto não precisam de barreira.
- **B)** Incorreta. Fork/join modelaria dois fluxos concorrentes e exigiria ambos, contra a exclusividade do caso.
- **C)** Incorreta. A decisão separa corretamente, mas o join esperaria por dois caminhos dos quais apenas um pode ocorrer.
- **D)** Incorreta. Fork executaria os dois caminhos; merge não corrige esse paralelismo indevido.

**Conceito:** decisão e merge.

**Pegadinha:** usar join para alternativas.

**Como pensar:** pergunte se os ramos coexistem ou são excludentes.

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

### Comentário S4D2Q085

**Nível:** Muito difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — atividades](semana_04_estudo.md#s4-d2-exemplos-atividades).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Merge não garante conclusão dos dois fluxos.
- **B)** Incorreta. Join sem entradas concorrentes e final precoce inviabilizam o caso.
- **C)** Incorreta. Decisão não abre concorrência, e a ordem de reunião está invertida.
- **D)** Correta. Representa concorrência com barreira e alternativa reunida sem bloqueio.

**Conceito:** atividade com paralelismo e alternativas.

**Pegadinha:** trocar merge e join por ambos reunirem linhas.

**Como pensar:** classifique ramos como concorrentes ou excludentes em cada ponto.

**Referência:** [Exemplos resolvidos — atividades](semana_04_estudo.md#s4-d2-exemplos-atividades).

### Comentário S4D2Q086

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Ator pertence à perspectiva de casos de uso.
- **B)** Correta. Ele inicia tokens/fluxo conforme a semântica da atividade.
- **C)** Incorreta. Isso descreve final de fluxo.
- **D)** Incorreta. Essa é função do join.

**Conceito:** nó inicial de atividade.

**Pegadinha:** confundir símbolo preenchido com composição.

**Como pensar:** leia o símbolo dentro do tipo de diagrama.

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

### Comentário S4D2Q087

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Generalização não é função do fluxo.
- **B)** Incorreta. Isso pertence ao diagrama estrutural.
- **C)** Incorreta. Visibilidade não é transportada pelo fluxo.
- **D)** Correta. Ele mostra a circulação de informação necessária ao comportamento.

**Conceito:** fluxo de objeto.

**Pegadinha:** tratar toda seta de atividade como idêntica.

**Como pensar:** pergunte se a aresta transporta controle ou objeto.

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

### Comentário S4D2Q088

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Guarda seleciona fluxo por condição; não atribui, por si, as três responsabilidades.
- **B)** Incorreta. Generalização modela relação é-um, não distribuição de trabalho no comportamento.
- **C)** Correta. As raias mostram os responsáveis, e os fluxos mantêm a dependência sequencial descrita.
- **D)** Incorreta. Posicionar ações em raias distintas não exige nem autoriza criar paralelismo ausente no caso.

**Conceito:** partições/raias de atividade.

**Pegadinha:** inferir concorrência da disposição.

**Como pensar:** separe quem executa de quando executa.

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

### Comentário S4D2Q089

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Raias não contêm a condição decisória.
- **B)** Incorreta. Isso pode tornar a escolha ambígua.
- **C)** Incorreta. Multiplicidade não decide fluxo.
- **D)** Correta. A escolha precisa ser determinável para os cenários previstos.

**Conceito:** guardas em atividade.

**Pegadinha:** escrever condições sem cobertura do domínio.

**Como pensar:** teste exclusividade e completude no cenário.

**Referência:** [Atividades: fluxo, decisão e concorrência](semana_04_estudo.md#s4-d2-atividades).

### Comentário S4D2Q090

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Exemplos resolvidos — atividades](semana_04_estudo.md#s4-d2-exemplos-atividades).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A diferença de sincronização é decisiva.
- **B)** Correta. Concorrentes exigem sincronização; alternativos exigem simples reunião.
- **C)** Incorreta. Fork não reúne fluxo.
- **D)** Incorreta. Final de atividade impede a continuação.

**Conceito:** merge e join em dois contextos.

**Pegadinha:** decidir pelo losango/barra sem analisar coexistência.

**Como pensar:** pergunte quantos ramos podem estar ativos e o que deve ser aguardado.

**Referência:** [Exemplos resolvidos — atividades](semana_04_estudo.md#s4-d2-exemplos-atividades).

### Comentário S4D2Q091

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Ela conecta estados e pode possuir gatilho, guarda e efeito.
- **B)** Incorreta. Isso pertence à interação de comunicação.
- **C)** Incorreta. Isso pertence ao diagrama de atividades.
- **D)** Incorreta. Isso pertence ao diagrama de classes.

**Conceito:** transição de estados.

**Pegadinha:** confundir qualquer seta UML.

**Como pensar:** leia a seta dentro da pergunta sobre ciclo de vida.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q092

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A ordem segue evento [guarda] / efeito.
- **B)** Incorreta. Mistura conceitos de outros diagramas.
- **C)** Incorreta. As categorias foram deslocadas.
- **D)** Incorreta. O rótulo não nomeia esses elementos.

**Conceito:** rótulo de transição.

**Pegadinha:** ler a condição como gatilho.

**Como pensar:** separe ocorrência, condição booleana e ação executada.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q093

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A ordem foi trocada.
- **B)** Correta. Cada palavra indica momento relativo ao estado.
- **C)** Incorreta. Não são categorias estruturais.
- **D)** Incorreta. Não são nós de atividade.

**Conceito:** comportamentos internos de estado.

**Pegadinha:** memorizar palavras sem relacionar ao momento.

**Como pensar:** associe entrada, duração e saída.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q094

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Gabarito: D (a afirmação incorreta).**

**Análise das alternativas:**

- **A)** Correta. A transição interna trata o evento e seu efeito sem abandonar e reentrar no estado.
- **B)** Correta. A auto-transição externa permite executar `exit/liberar` e depois `entry/carregar`.
- **C)** Correta. A substituição eliminaria exatamente a saída e a nova entrada requeridas por `reiniciar`.
- **D)** Incorreta. O mesmo nome de estado antes e depois não torna equivalentes os conjuntos de ações executadas.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** transição interna versus auto-transição.

**Pegadinha:** comparar somente estado de origem e destino.

**Como pensar:** verifique se há saída, entrada e efeitos associados.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q095

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Exemplos resolvidos — máquinas de estados](semana_04_estudo.md#s4-d2-exemplos-estados).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Fork ativaria resultados mutuamente exclusivos e exigiria cancelamento não previsto no requisito.
- **B)** Incorreta. As saídas sem guarda são concorrentes na escolha, e a auto-transição externa executaria saída e reentrada no caso inválido.
- **C)** Correta. Guardas exclusivas selecionam os estados-alvo, enquanto a transição interna executa a correção sem `exit`/`entry`.
- **D)** Incorreta. Auto-transições externas não alcançam os estados-alvo e ainda contrariam a exigência de não reentrar no caso inválido.

**Conceito:** máquina de estados multifiltro.

**Pegadinha:** perder exclusividade das guardas ou confundir transição interna com auto-transição externa.

**Como pensar:** enumere evento, condições exclusivas, estados-alvo e necessidade ou não de `exit`/`entry`.

**Referência:** [Exemplos resolvidos — máquinas de estados](semana_04_estudo.md#s4-d2-exemplos-estados).

### Comentário S4D2Q096

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A transição de saída conduz ao estado inicial efetivo.
- **B)** Incorreta. Pseudestado não é instância de domínio.
- **C)** Incorreta. Isso pertence ao final de fluxo.
- **D)** Incorreta. A notação não representa mensagem.

**Conceito:** pseudestado inicial.

**Pegadinha:** confundir círculos preenchidos entre diagramas.

**Como pensar:** identifique o tipo de diagrama e o papel de entrada.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q097

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Não há reinício implícito.
- **B)** Incorreta. Conclusão da região não implica destruição universal.
- **C)** Incorreta. Essa é função de join em atividades.
- **D)** Correta. O estado final encerra o ciclo modelado no escopo correspondente.

**Conceito:** estado final.

**Pegadinha:** atribuir efeitos globais ao final local.

**Como pensar:** delimite a região e o comportamento concluído.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q098

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. O recurso não tem essa finalidade.
- **B)** Incorreta. Hierarquia de estados não é generalização estrutural.
- **C)** Incorreta. Isso é comunicação.
- **D)** Correta. A composição cria hierarquia comportamental.

**Conceito:** estado composto.

**Pegadinha:** confundir composição de estados com composição de classes.

**Como pensar:** observe se a hierarquia é comportamental ou estrutural.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q099

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

**Gabarito: C (a afirmação incorreta).**

**Análise das alternativas:**

- **A)** Correta. Essa é sua finalidade comportamental.
- **B)** Correta. Histórico raso e profundo possuem alcance diferente.
- **C)** Incorreta. Histórico de estado retoma configuração anterior; não implica registro persistente de auditoria.
- **D)** Correta. Retomada comportamental e auditoria são conceitos distintos.

**Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.

**Conceito:** pseudestado de histórico.

**Pegadinha:** associar a palavra histórico a log de dados.

**Como pensar:** pergunte se o modelo retoma estado ou registra evidência.

**Referência:** [Máquinas de estados: evento, guarda e efeito](semana_04_estudo.md#s4-d2-estados).

### Comentário S4D2Q100

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Prática guiada — quatro perspectivas](semana_04_estudo.md#s4-d2-pratica).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Comunicação sem numeração perde a ordem, merge não sincroniza verificações paralelas e estados sem eventos omitem os gatilhos.
- **B)** Correta. Cada aspecto recebe o diagrama e os elementos semanticamente adequados.
- **C)** Incorreta. Objetos mostram ocorrências, fork sem join não cria a barreira exigida e guardas sem eventos deixam incompleta a reação.
- **D)** Incorreta. Decisão/merge trata alternativas, não sincronização, e objetos não modelam o ciclo reativo.

**Conceito:** integração de diagramas UML.

**Pegadinha:** tentar expressar tudo em uma única perspectiva.

**Como pensar:** classifique cada informação antes de escolher a notação.

**Referência:** [Prática guiada — quatro perspectivas](semana_04_estudo.md#s4-d2-pratica).

### Comentário Extra Dia 2.1

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** princípios do art. 37
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Economia isolada não elimina a legalidade.
- **B)** Incorreta. Os princípios não são permutáveis dessa forma.
- **C)** Correta. Eficiência orienta resultado, mas não autoriza afastar o ordenamento.
- **D)** Incorreta. Automação não cria dispensa geral de motivação.

**Conceito:** legalidade e eficiência.

**Pegadinha:** opor princípios como se um anulasse o outro.

**Como pensar:** teste a solução eficiente dentro dos limites jurídicos.

**Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

### Comentário Extra Dia 2.2

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** publicidade e impessoalidade
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Publicidade exige transparência e não torna ilícita toda comunicação institucional de serviço.
- **B)** Incorreta. Eficiência não afasta impessoalidade nem legitima promoção da autoridade.
- **C)** Incorreta. Informação verdadeira e finalidade pública não autorizam personalizar a mensagem institucional.
- **D)** Correta. Distingue a divulgação legítima do serviço do destaque pessoal incompatível com a impessoalidade.

**Conceito:** publicidade e impessoalidade.

**Pegadinha:** concluir que publicidade proíbe comunicação.

**Como pensar:** distinga transparência institucional de promoção da pessoa.

**Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

### Comentário Extra Dia 2.3

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** anulação e revogação
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. É princípio, não modalidade de retirada.
- **B)** Incorreta. Revogação incide sobre conveniência/oportunidade de ato válido, quando cabível.
- **C)** Incorreta. É técnica de distribuição interna de competências.
- **D)** Correta. A causa é invalidade jurídica, não escolha de mérito.

**Conceito:** anulação por ilegalidade.

**Pegadinha:** usar revogação como gênero para toda retirada.

**Como pensar:** identifique primeiro se há vício ou mérito.

**Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

### Comentário Extra Dia 2.4

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** anulação e revogação
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A retirada decorre de conveniência e oportunidade, não de ilegalidade.
- **B)** Incorreta. O caso afirma validade do ato.
- **C)** Incorreta. Convalidação trata vício sanável, não inconveniência.
- **D)** Incorreta. Distribuição administrativa não resolve a retirada.

**Conceito:** revogação por mérito.

**Pegadinha:** chamar ato inconveniente de ilegal.

**Como pensar:** classifique validade e depois a razão da retirada.

**Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

### Comentário Extra Dia 2.5

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** atos administrativos
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Tenta sanar vício insanável e trata o vício sanável como causa de anulação.
- **B)** Incorreta. Acerta o primeiro caso, mas troca mérito por saneamento e vício sanável por revogação.
- **C)** Incorreta. Inverte anulação e revogação nos dois primeiros casos, embora acerte o terceiro.
- **D)** Correta. Cada instituto responde a invalidade, mérito e saneamento possível.

**Conceito:** anulação, revogação e convalidação.

**Pegadinha:** classificar apenas pelo efeito de retirar ou manter.

**Como pensar:** diagnostique vício, mérito e possibilidade de saneamento.

**Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

### Comentário Extra Dia 2.6

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** organização administrativa
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. O termo não descreve a técnica indicada.
- **B)** Correta. A distribuição permanece dentro da mesma pessoa, entre órgãos.
- **C)** Incorreta. Não houve nova pessoa jurídica.
- **D)** Incorreta. Não há retirada de ato nem personalidade.

**Conceito:** desconcentração.

**Pegadinha:** associar toda distribuição a descentralização.

**Como pensar:** pergunte se a competência saiu da mesma pessoa.

**Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

### Comentário Extra Dia 2.7

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** organização administrativa
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Desconcentração distribui competências internamente.
- **B)** Incorreta. Convalidação sana vício admissível.
- **C)** Correta. A atividade ultrapassa a estrutura interna da mesma pessoa.
- **D)** Incorreta. É princípio e não técnica organizacional.

**Conceito:** descentralização.

**Pegadinha:** olhar apenas a palavra transferência.

**Como pensar:** verifique se há outra pessoa ou somente outro órgão.

**Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

### Comentário Extra Dia 2.8

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** órgãos e entidades
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

**Gabarito: D (a afirmação incorreta).**

**Análise das alternativas:**

- **A)** Correta. Personalidade é filtro central.
- **B)** Correta. Os fenômenos possuem alcances diferentes.
- **C)** Correta. A afirmação descreve a técnica corretamente.
- **D)** Incorreta. Órgão integra uma pessoa e não recebe personalidade apenas pela desconcentração.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** órgão e desconcentração.

**Pegadinha:** equiparar unidade interna a entidade.

**Como pensar:** pergunte quem possui personalidade jurídica.

**Referência:** [Exemplos resolvidos — Administração Pública](semana_04_estudo.md#s4-d2-exemplos-adm).

### Comentário Extra Dia 2.9

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** elementos do ato
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não classificam transferência de atividade.
- **B)** Incorreta. Os termos pertencem ao Direito Administrativo neste contexto.
- **C)** Correta. O conjunto organiza a análise da validade do ato.
- **D)** Incorreta. Não constituem ciclo de desenvolvimento.

**Conceito:** elementos do ato administrativo.

**Pegadinha:** transportar categorias de uma disciplina para outra.

**Como pensar:** localize agente competente, finalidade, forma, motivo e conteúdo.

**Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

### Comentário Extra Dia 2.10

- **Dia:** Dia 2
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** diagnóstico integrado
- **Nível:** Muito difícil
- **Uso:** Aprofundamento
- **Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Aplica personalidade, mérito e vedação à promoção pessoal em sequência.
- **B)** Incorreta. Não houve outra pessoa jurídica, nem ilegalidade; divulgar não torna regular a promoção pessoal.
- **C)** Incorreta. A organização está correta, mas mérito não se convalida e o desvio indicado é de impessoalidade.
- **D)** Incorreta. Erra a distribuição entre pessoas e troca o problema de promoção pessoal por legalidade genérica.

**Conceito:** organização, ato e princípios.

**Pegadinha:** resolver caso integrado com rótulo único.

**Como pensar:** para cada fato, teste personalidade, validade/mérito e finalidade.

**Referência:** [Revisão fixa: Administração Pública](semana_04_estudo.md#s4-d2-b4).

### Comentário Extra Dia 2.11

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Mudar o objeto não corrige o sujeito singular.
- **B)** Correta. O núcleo singular “ordem” exige verbo no singular.
- **C)** Incorreta. Artigo e substantivo também estão em desacordo.
- **D)** Incorreta. O verbo concordou indevidamente com termo preposicionado plural.

**Conceito:** concordância com núcleo do sujeito.

**Pegadinha:** concordar com o termo plural mais próximo.

**Como pensar:** pergunte quem pratica a ação e ache o núcleo.

**Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

### Comentário Extra Dia 2.12

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância verbal
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. Os dois núcleos coordenados exigem plural.
- **B)** Incorreta. O infinitivo não forma o predicado finito esperado.
- **C)** Incorreta. O verbo singular não concorda com os dois núcleos.
- **D)** Incorreta. Há erro de flexão e acentuação.

**Conceito:** concordância com sujeito composto.

**Pegadinha:** concordar apenas com o núcleo mais próximo.

**Como pensar:** conte os núcleos do sujeito anteposto.

**Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

### Comentário Extra Dia 2.13

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pontuação
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. A vírgula separa indevidamente sujeito e predicado.
- **B)** Correta. Não se separa sujeito do verbo sem elemento intercalado.
- **C)** Incorreta. A vírgula isola trecho sem função explicativa completa.
- **D)** Incorreta. O complemento nominal foi separado indevidamente.

**Conceito:** vírgula e estrutura sintática.

**Pegadinha:** pontuar pela extensão do sujeito.

**Como pensar:** localize sujeito completo e verbo antes de inserir vírgula.

**Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

### Comentário Extra Dia 2.14

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** orações relativas
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

**Alternativa correta: A.**

**Análise das alternativas:**

- **A)** Correta. A relativa sem vírgulas seleciona o subconjunto dos 12 processos que possuem recurso.
- **B)** Incorreta. As vírgulas tornam a oração explicativa e atribuem recurso ao conjunto contextual dos processos.
- **C)** Incorreta. A relativa explicativa depois da vírgula também não seleciona somente os 12.
- **D)** Incorreta. A oração causal explica a espera, mas não restringe o sujeito ao subconjunto informado.

**Conceito:** oração relativa restritiva.

**Pegadinha:** ignorar o efeito das vírgulas.

**Como pensar:** pergunte se a oração seleciona ou apenas explica.

**Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

### Comentário Extra Dia 2.15

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** reescrita
- **Nível:** Muito difícil
- **Uso:** Revisão
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. O sujeito composto “decisão e merge” exige “mantêm”.
- **B)** Incorreta. A concordância está adequada, mas o singular “função distinta” altera a informação original.
- **C)** Correta. Mantém sujeito composto plural, referência ao conteúdo e adjunto deslocado.
- **D)** Incorreta. “Onde” exige antecedente locativo e não retoma adequadamente “funções distintas”.

**Conceito:** reescrita com concordância e coesão.

**Pegadinha:** preservar palavras e perder relações sintáticas.

**Como pensar:** confira núcleos, referente do relativo e posição do adjunto.

**Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

### Comentário Extra Dia 2.16

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pronomes relativos
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

**Alternativa correta: C.**

**Análise das alternativas:**

- **A)** Incorreta. Não se usa artigo imediatamente após “cujo”.
- **B)** Incorreta. Falta o substantivo possuído ligado ao relativo.
- **C)** Correta. “Cujo” expressa posse entre processo e prazo, concordando com o possuído.
- **D)** Incorreta. Há duplicação indevida de relativos.

**Conceito:** pronome relativo cujo.

**Pegadinha:** inserir artigo após cujo.

**Como pensar:** identifique possuidor, coisa possuída e concordância.

**Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

### Comentário Extra Dia 2.17

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pronomes relativos
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

**Alternativa correta: D.**

**Análise das alternativas:**

- **A)** Incorreta. Decisão não funciona como antecedente locativo.
- **B)** Incorreta. Prazo exige relativo não locativo.
- **C)** Incorreta. Requisito não é lugar; cabe construção como “que define”.
- **D)** Correta. O antecedente é lugar em que a ação ocorre.

**Conceito:** pronome relativo onde.

**Pegadinha:** usar onde como relativo universal.

**Como pensar:** teste se o antecedente admite 'em que' com sentido de lugar.

**Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

### Comentário Extra Dia 2.18

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** pontuação
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

**Gabarito: A (a afirmação incorreta).**

**Análise das alternativas:**

- **A)** Incorreta. A vírgula separa sujeito e verbo sem termo intercalado.
- **B)** Correta. O adjunto ao final pode aparecer sem vírgula nesse período.
- **C)** Correta. A vírgula destaca adjunto adverbial deslocado.
- **D)** Correta. As vírgulas isolam o adjunto intercalado.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** pontuação de adjunto e sujeito.

**Pegadinha:** usar vírgula como marca de respiração.

**Como pensar:** localize o esqueleto sujeito-verbo-complemento.

**Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

### Comentário Extra Dia 2.19

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** concordância e oração relativa
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. As vírgulas transformam a relativa em explicativa e atribuem a característica ao conjunto, contra o recorte informado.
- **B)** Correta. Sujeito e verbo estão no plural, e a relativa restringe o conjunto.
- **C)** Incorreta. “Que” retoma “diagramas”, por isso o verbo deve ir ao plural: “representam”.
- **D)** Incorreta. O sujeito plural “os diagramas” exige “preservam”.

**Conceito:** concordância em oração relativa.

**Pegadinha:** ajustar apenas o verbo principal.

**Como pensar:** confira cada oração e seu respectivo sujeito.

**Referência:** [Português: concordância e pontuação](semana_04_estudo.md#s4-d2-portugues).

### Comentário Extra Dia 2.20

- **Dia:** Dia 2
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** revisão integrada
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

**Alternativa correta: B.**

**Análise das alternativas:**

- **A)** Incorreta. Cria desacordos nominais e vírgula indevida.
- **B)** Correta. Concorda com sequência, remove vírgula indevida, rege depender de e liga o plural aos serviços.
- **C)** Incorreta. Separa complemento, erra concordância e usa cujo inadequadamente.
- **D)** Incorreta. Mantém erros de concordância, regência e referente.

**Conceito:** revisão de período técnico.

**Pegadinha:** corrigir uma falha e manter as demais.

**Como pensar:** revise núcleo, regência, relativo, pontuação e referente em ordem.

**Referência:** [Exemplos resolvidos — Português](semana_04_estudo.md#s4-d2-exemplos-portugues).

# Dia 3 - Componentes, implementação e ferramentas de apoio

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. A matriz inicial é 20/20/10 nas principais e 8/8/4 nas extras. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais - S4D3Q101 a S4D3Q150

### S4D3Q101 — Componente e servidor

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Em uma revisão arquitetural, a equipe precisa representar o módulo lógico de Cadastro, independentemente do servidor em que será executado. Qual elemento é adequado?

A) Um componente Cadastro.

B) Um nó Cadastro.

C) Um caminho de comunicação.

D) Um artefato de configuração.


### S4D3Q102 — Granularidade do componente

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

A pergunta do modelo é quais módulos entregáveis oferecem serviços ao Portal. As classes Serviço, Repositório e Validador pertencem ao mesmo módulo Processos. Qual representação atende à pergunta?

A) Um componente para cada classe, todos com contratos próprios.

B) Um componente Processos, com as classes internas e o contrato do módulo.

C) Um artefato Processos, sem representar o contrato oferecido.

D) Um componente Portal, contendo as três classes e seus métodos.


### S4D3Q103 — Responsabilidade modular

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

No cenário do CRA-PR, o módulo Notificações deve poder mudar de provedor sem alterar a regra de Registro. Qual decisão favorece esse objetivo?

A) Unir toda a lógica em Registro para reduzir elementos.

B) Representar o provedor como porta UML de Registro.

C) Separar Notificações e fazê-lo cumprir um contrato consumido por Registro.

D) Substituir o contrato por um caminho físico entre servidores.


### S4D3Q104 — Contrato externo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Um diagrama deve mostrar o que Cobrança oferece sem revelar suas classes internas. O que deve ser enfatizado?

A) A porta do nó que hospeda Cobrança.

B) A classe pública que inicia Cobrança.

C) O artefato que manifesta Cobrança.

D) A interface fornecida por Cobrança.


### S4D3Q105 — Coesão e substituição

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Dois módulos misturam envio de mensagem, cálculo de taxa e persistência. Qual ação é coerente?

A) Separar por tecnologia e manter contratos implícitos.

B) Separar responsabilidades e explicitar dependências por interfaces.

C) Separar por servidor e duplicar as regras compartilhadas.

D) Manter os módulos e ocultar dependências no diagrama.


### S4D3Q106 — Visão adequada

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Qual pergunta é respondida principalmente por um diagrama de componentes?

A) Em qual endereço físico cada pacote está instalado?

B) Qual sequência temporal ocorre entre objetos?

C) Qual estado interno segue um evento?

D) Quais módulos oferecem ou requerem contratos?


### S4D3Q107 — Módulo e classes internas

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Um analista concluiu que toda classe pública constitui necessariamente um componente separado. Assinale a avaliação correta.

A) Não; a classe pode integrar a realização interna de um componente.

B) Sim; a visibilidade pública define a fronteira de cada componente.

C) Sim; uma classe pública realiza obrigatoriamente uma interface.

D) Não; toda classe pública deve ser representada como artefato.


### S4D3Q108 — Responsabilidade observável

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Relatórios aparece no modelo, mas não possui responsabilidade nem contrato identificáveis. Qual correção é mais útil?

A) Definir primeiro as dependências entre Relatórios e os demais módulos.

B) Modelar Relatórios como nó e depois alocar seus artefatos.

C) Definir a capacidade de Relatórios e seus serviços externos.

D) Detalhar as classes internas antes de identificar seu contrato.


### S4D3Q109 — Substituição por contrato

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Cobrança requer Repositório; RepositórioSQL e RepositórioMemória cumprem o contrato. O que permite substituição em testes?

A) Dependência direta de Cobrança para cada classe concreta.

B) Dependência de Cobrança para contratos distintos de cada repositório.

C) Dependência de Cobrança para o contrato, realizado pelas alternativas.

D) Realização de Repositório pela própria Cobrança, sem alternativas externas.


### S4D3Q110 — Impacto da mudança

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Portal e Aplicativo requerem Autenticação; Auditoria usa outro contrato. Se uma operação de Autenticação for removida, quais são candidatos imediatos ao impacto?

A) Portal e Aplicativo.

B) Somente Auditoria, por proximidade visual.

C) Todos os nós físicos.

D) Apenas a interface.


### S4D3Q111 — Encapsulamento do componente

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Sobre o conteúdo interno de um componente, assinale a alternativa correta.

A) Deve expor sua realização interna para permitir a substituição.

B) Pode conter classificadores, mas não apresentar interfaces externas.

C) É determinado pelo nó em que seus artefatos serão implantados.

D) Pode encapsular a realização e expor somente os contratos externos.


### S4D3Q112 — Limite do diagrama de componentes

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Portal requer Consulta e Cadastro a fornece. Qual conclusão NÃO pode ser garantida apenas pelo desenho?

A) Portal aparece como consumidor do contrato Consulta.

B) A integração cumprirá disponibilidade e desempenho em produção.

C) Cadastro aparece como fornecedor do contrato Consulta.

D) A relação arquitetural deverá ser verificada por testes.


### S4D3Q113 — Fornecedor da interface

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Cadastro implementa consultar e Relatórios a invoca. Quem fornece ConsultaCadastral?

A) Cadastro.

B) Relatórios.

C) Ambos, pois um implementa e o outro invoca.

D) A própria interface, pois ela define as operações.


### S4D3Q114 — Interface requerida

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Portal não conclui solicitação sem ValidarRegistro. Como representar a necessidade?

A) Como interface fornecida por Portal.

B) Como dispositivo contido em Portal.

C) Como interface requerida por Portal.

D) Como manifestação de Portal.


### S4D3Q115 — Sentido da porta UML

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Uma porta na fronteira de Atendimento representa:

A) um ponto de rede que identifica a porta TCP usada pelo componente.

B) um ponto de interação que agrupa contratos da fronteira.

C) um artefato que materializa as interfaces do componente.

D) um nó interno que executa os serviços do componente.


### S4D3Q116 — Conector de montagem

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Uma interface requerida de Portal liga-se à fornecida compatível de Cadastro. Isso indica:

A) manifestação do Portal no código.

B) implantação no mesmo nó.

C) herança obrigatória.

D) montagem entre consumidor e fornecedor.


### S4D3Q117 — Realização de interface

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Qual relação descreve que RepositórioSQL cumpre as operações de Repositório?

A) Caminho de comunicação.

B) Deployment.

C) Dependência genérica.

D) Realização de interface.


### S4D3Q118 — Direção da dependência

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

A utiliza serviço exposto por B. A seta tracejada de dependência parte de:

A) B e aponta para A.

B) A e aponta para B.

C) ambos simultaneamente.

D) um nó físico.


### S4D3Q119 — Dependência e caminho físico

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Qual distinção está correta?

A) Dependência liga cliente e fornecedor; caminho liga artefato e nó.

B) Dependência e caminho representam conexões lógicas equivalentes.

C) Dependência mostra uso lógico; caminho mostra comunicação entre nós.

D) Dependência mostra implantação; caminho mostra realização de contrato.


### S4D3Q120 — Comando negativo sobre interfaces

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Sobre interfaces e portas, assinale a alternativa INCORRETA.

A) Porta UML designa necessariamente um endpoint TCP ou UDP.

B) Interface fornecida especifica serviço oferecido pelo componente.

C) Interface requerida especifica serviço do qual o componente depende.

D) Porta organiza interfaces expostas em um ponto da fronteira.


### S4D3Q121 — Dois fornecedores substituíveis

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Portal requer Pagamento; ProvedorA e ProvedorB realizam o contrato, mas só um é selecionado por ambiente. Qual desenho preserva substituição?

A) Portal depende diretamente de ProvedorA e troca a classe por configuração.

B) Portal requer Pagamento, mas cada provedor expõe contrato próprio.

C) Portal requer Pagamento; ambos o realizam; a configuração escolhe um.

D) Portal depende de ambos os provedores e ativa somente um por ambiente.


### S4D3Q122 — Mudança interna sem quebra externa

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Cadastro refatora classes, preservando interface e comportamento contratado. Qual efeito é coerente?

A) O contrato preservado evita mudança obrigatória nos consumidores.

B) O componente deve ser movido para outro nó antes da refatoração.

C) As interfaces requeridas passam a ser fornecidas após a refatoração.

D) A realização da interface precisa ser removida durante a refatoração.


### S4D3Q123 — Compatibilidade declarada e teste

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Interfaces têm o mesmo nome, mas discordam no formato e significado de campo. Qual avaliação é correta?

A) A montagem garante compatibilidade quando as interfaces têm o mesmo nome.

B) A assinatura igual basta, mesmo que a semântica dos campos seja distinta.

C) A co-localização no mesmo nó resolve divergências de formato e significado.

D) A compatibilidade semântica ainda precisa ser especificada e testada.


### S4D3Q124 — Visão lógica não prova execução

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

O modelo mostra componentes, mas é preciso decidir isolamento de ambientes e caminhos. Qual ação é apropriada?

A) Detalhar portas e interfaces no diagrama de componentes existente.

B) Adicionar uma visão de deployment ligada aos artefatos dos componentes.

C) Substituir cada componente por uma classe associada ao servidor.

D) Distribuir os componentes por endereços anotados na visão lógica.


### S4D3Q125 — Portas para canais distintos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

Atendimento recebe API e lote por contratos diferentes, com mesma lógica interna. Qual solução é expressiva?

A) Usar duas portas, cada qual associada ao contrato do respectivo canal.

B) Usar dois componentes idênticos, ambos com os dois contratos.

C) Usar um caminho físico distinto para representar cada contrato.

D) Usar um único contrato e indicar os canais apenas nos artefatos.


### S4D3Q126 — Impacto multiconsumidor

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

Uma interface ganha parâmetro obrigatório. Três consumidores a requerem; dois usam a operação e um usa outra. Qual análise é precisa?

A) Revisar somente os dois consumidores que usam a operação alterada.

B) Revisar os três consumidores e alterar todos antes de qualquer teste.

C) Revisar os três; priorizar os dois usos e confirmar o terceiro.

D) Revisar apenas o fornecedor, pois o contrato preserva os consumidores.


### S4D3Q127 — Uso e realização

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

ServiçoRelatorio requer Consulta; Cadastro realiza Consulta. Qual leitura está correta?

A) ServiçoRelatorio realiza por iniciar chamada.

B) ServiçoRelatorio é cliente; Cadastro é implementador.

C) Cadastro requer por receber chamada.

D) Ambos manifestam a interface.


### S4D3Q128 — Estrutura interna e contrato

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

Um componente contém partes internas e oferece interface externa. Qual afirmação é adequada?

A) A estrutura interna deve ser exposta para o componente continuar substituível.

B) A interface externa deve enumerar todas as partes usadas na realização.

C) As partes internas precisam ser representadas como nós de execução.

D) A estrutura interna pode ser modelada sem romper o encapsulamento.


### S4D3Q129 — Transição da visão lógica para física

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Para ligar Cadastro ao deployment, qual sequência é coerente?

A) Cadastro é implantado diretamente no nó, sem artefato intermediário.

B) Um artefato realiza Cadastro e o nó manifesta esse artefato.

C) O ambiente manifesta Cadastro e o artefato realiza o ambiente.

D) Um artefato manifesta Cadastro e é implantado em ambiente de execução.


### S4D3Q130 — Nó de execução

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Em deployment, nó representa:

A) um contrato lógico oferecido por um componente.

B) um recurso computacional que hospeda ou executa artefatos.

C) uma sequência de mensagens entre objetos em execução.

D) uma unidade modular responsável por regra de negócio.


### S4D3Q131 — Dispositivo e ambiente

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Servidor físico contém JVM que executa api.jar. Qual classificação é coerente?

A) Servidor é componente; JVM é interface; jar é nó.

B) Servidor é artefato; JVM é dependência; jar é porta.

C) Servidor é dispositivo; JVM é ambiente; api.jar é artefato.

D) Servidor é interface; JVM é componente; jar é caminho.


### S4D3Q132 — Caminho de comunicação

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

A associação entre nó Aplicação e nó Dados que permite interação representa:

A) um caminho de comunicação.

B) realização de interface.

C) manifestação do servidor.

D) generalização de dispositivos.


### S4D3Q133 — Cliente sem acesso direto ao banco

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

A arquitetura exige Cliente→Aplicação e Aplicação→Dados, vedando Cliente→Dados. Qual diagrama traduz isso?

A) Um componente com três interfaces, sem nós.

B) Um caminho direto rotulado como proibido, mas usado.

C) Três artefatos por realizações.

D) Três nós ligados apenas por Cliente–Aplicação e Aplicação–Dados.


### S4D3Q134 — Ambientes aninhados

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Um dispositivo hospeda duas VMs, cada qual com artefatos próprios. Qual modelagem preserva níveis?

A) Um dispositivo para cada VM, ambos contidos em um componente.

B) Um dispositivo contendo duas VMs modeladas como artefatos.

C) Um ambiente contendo dois dispositivos ligados por caminhos.

D) Um dispositivo contendo dois ambientes, cada qual com seus artefatos.


### S4D3Q135 — Restrição em três camadas

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Portal acessa Cadastro; Cadastro acessa Dados; o banco fica isolado. Qual combinação é correta?

A) Manifestar os componentes em artefatos, implantá-los nos nós e limitar os caminhos.

B) Implantar os componentes diretamente e usar interfaces como caminhos entre nós.

C) Manifestar os nós em artefatos e ligar cada componente ao banco por dependência.

D) Implantar todas as peças no mesmo nó e registrar isolamento apenas no contrato.


### S4D3Q136 — Limite do deployment

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

O diagrama mostra caminho Aplicação–Dados. O que ainda exige verificação externa?

A) Os nós e os papéis de cada um na topologia representada.

B) A existência da comunicação prevista entre Aplicação e Dados.

C) Os protocolos e atributos operacionais exigidos para essa comunicação.

D) Os artefatos implantados em cada nó e as relações de manifestação.


### S4D3Q137 — Escala com instâncias

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

O mesmo artefato da API é implantado em dois nós. Qual leitura é adequada?

A) Cada deployment cria uma nova interface lógica para a API.

B) Cada deployment exige um componente lógico diferente.

C) Há duas implantações do artefato e pode haver um só componente lógico.

D) Há um artefato por nó e a manifestação deixa de existir.


### S4D3Q138 — Posicionamento do artefato

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

cadastro-api.jar deve executar na JVM de Aplicação-1. Qual relação responde ao posicionamento?

A) Dependência do nó para interface.

B) Realização do dispositivo.

C) Generalização da JVM.

D) Deployment do artefato no ambiente.


### S4D3Q139 — Comando negativo sobre nós

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

Sobre deployment, assinale a alternativa INCORRETA.

A) Todo nó representa necessariamente um componente do domínio.

B) Um dispositivo pode conter um ou mais ambientes de execução.

C) Um artefato pode ser implantado em dispositivo ou ambiente.

D) Um caminho de comunicação pode conectar nós da topologia.


### S4D3Q140 — Manifestação e implantação combinadas

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

relatorios.jar concretiza Relatórios e é instalado na JVM do servidor B. Qual conjunto é correto?

A) Manifestação entre componente e jar; deployment entre componente e JVM.

B) Manifestação entre jar e componente; deployment entre jar e JVM.

C) Realização entre jar e componente; manifestação entre jar e JVM.

D) Deployment entre jar e componente; realização entre jar e JVM.


### S4D3Q141 — Pacote comum e configurações distintas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

O mesmo pacote vai a homologação e produção com configurações próprias. Qual modelo é preciso?

A) Criar um componente para homologação e outro para produção, com o mesmo pacote.

B) Implantar o pacote nos dois ambientes, cada qual com sua configuração.

C) Manifestar cada ambiente em sua configuração e implantar o nó.

D) Usar uma configuração externa sem registrar a diferença entre ambientes.


### S4D3Q142 — Tipos de artefato

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

Qual conjunto contém apenas exemplos coerentes de artefatos?

A) Componente, interface, executável e caso de uso.

B) Servidor, roteador, script e caminho de comunicação.

C) Biblioteca, componente, configuração e ambiente de execução.

D) Executável, biblioteca, script e arquivo de configuração.


### S4D3Q143 — Três camadas sem mistura

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

Considere Cadastro, cadastro.jar e JVM. Assinale a cadeia correta.

A) cadastro.jar manifesta Cadastro e é implantado na JVM.

B) Cadastro manifesta cadastro.jar e a JVM é implantada no arquivo.

C) A JVM manifesta Cadastro e cadastro.jar é implantado no componente.

D) cadastro.jar realiza Cadastro e a JVM manifesta o arquivo.


### S4D3Q144 — Ferramenta para rastreabilidade

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Requisitos, commits e testes estão desconectados. Qual prioridade trata a causa?

A) Modelador que gere diagramas e mantenha a ligação apenas por nomes.

B) IDE que associe commits ao autor, sem vínculo com requisito ou teste.

C) Repositório integrado a versão e testes, com IDs e vínculos rastreáveis.

D) Gerador que produza código e registre o build, sem relacionar o requisito.


### S4D3Q145 — Limite da engenharia reversa

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Uma ferramenta extrai diagrama do legado. Qual uso é responsável?

A) Tratá-lo como registro fiel dos requisitos que originaram o sistema.

B) Usá-lo como baseline estrutural e validar as decisões ausentes.

C) Tratá-lo como prova da arquitetura planejada, inclusive das decisões erodidas.

D) Usá-lo para substituir testes, pois a estrutura extraída comprova comportamento.


### S4D3Q146 — Limite da engenharia direta

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Modelador gera esqueletos de classes. Qual afirmação é correta?

A) Garante os requisitos não funcionais descritos no modelo de origem.

B) Automatiza a estrutura, mas comportamento e qualidade ainda exigem verificação.

C) Dispensa versionar o código gerado quando o modelo já possui histórico.

D) Mantém modelo e código sincronizados depois de qualquer alteração manual.


### S4D3Q147 — Round-trip sem falsa garantia

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Modelo e código são sincronizados, mas alterados sem precedência. Qual risco permanece?

A) O modelo sempre prevalece, mesmo quando o código contém a correção validada.

B) O código sempre prevalece, ainda que o modelo contenha decisão não implementada.

C) Conflitos desaparecem se modelo e código estiverem no mesmo repositório.

D) Persistem conflitos; fonte de verdade, fluxo e revisão precisam ser definidos.


### S4D3Q148 — Cadeia de ferramentas e evidência

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

O órgão quer saber se cada requisito chegou ao pacote implantado e passou no teste. Qual cadeia é adequada?

A) Requisito → diagrama sem versão → arquivo local → implantação manual.

B) Requisito → tarefa sem commit → build local → teste sem versão → deployment.

C) Requisito → commit → build versionado → teste → deployment registrado.

D) Requisito → código gerado → build versionado → nó, presumindo aceite.


### S4D3Q149 — Cenário integrado de arquitetura e ferramentas

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

Cadastro fornece Consulta; Portal a requer; cadastro.jar roda em dois nós. Uma mudança deve chegar controladamente. Qual plano é completo?

A) Alterar o jar, copiar aos dois nós e atualizar o modelo depois da implantação.

B) Versionar contrato e código, rastrear consumidores, testar o build e registrar ambos os deployments.

C) Versionar só o modelo, gerar dois builds locais e validar apenas o primeiro nó.

D) Criar um novo servidor, manter o contrato e presumir compatibilidade dos consumidores.


### S4D3Q150 — Auditoria de ferramenta e implantação

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

A ferramenta afirma round-trip, o build não é identificável e um dos dois nós executa pacote antigo. Qual resposta reúne três controles?

A) Sincronizar modelo e código, manter builds locais e comparar os nós manualmente.

B) Fixar a versão do modelo, recompilar sem ID e atualizar apenas o nó antigo.

C) Versionar somente o código, gerar build mutável e registrar o ambiente, não o nó.

D) Fixar modelo/código, gerar build imutável identificado e verificar cada nó.


## Questões extras - Dia 3

#### Extra Dia 3.1 — Lei e decreto

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Qual relação entre a Lei nº 4.769/1965 e o Decreto nº 61.934/1967 foi revisada?

A) A lei define a base; o decreto disciplina sua execução nos limites legais.

B) O decreto detalha a execução e pode afastar a lei quando for posterior.

C) A lei organiza apenas o CRA-PR; o decreto estrutura o sistema nacional.

D) As duas fontes têm o mesmo nível e prevalece a mais específica.


#### Extra Dia 3.2 — Âmbito do CFA e CRA

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Assinale a divisão coerente de atuação.

A) O CRA-PR aplica orientação nacional e substitui o CFA quando o fato é paranaense.

B) O CFA orienta nacionalmente e também executa sozinho todas as atribuições regionais.

C) O CFA atua nacionalmente; o CRA-PR exerce atribuições em sua jurisdição.

D) CFA e CRA-PR têm âmbitos distintos e não integram o mesmo sistema.


#### Extra Dia 3.3 — Função do Regimento

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

O Regimento Interno serve principalmente para:

A) organizar os órgãos internos e ampliar suas competências além da lei.

B) organizar órgãos, competências e funcionamento conforme as fontes superiores.

C) definir orientação nacional e substituir as competências reservadas ao CFA.

D) disciplinar a profissão e afastar o decreto nos assuntos internos.


#### Extra Dia 3.4 — Autonomia integrada

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

A autonomia do CRA-PR significa:

A) gerir o âmbito regional sem observar orientações do sistema nacional.

B) editar decisões regionais com força superior às fontes federais.

C) exercer todas as competências nacionais quando o fato ocorrer no Paraná.

D) gerir seu âmbito, preservando integração e competências do sistema.


#### Extra Dia 3.5 — Método de leitura normativa

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Qual sequência reduz erros?

A) Identificar primeiro o território e presumir a competência do órgão local.

B) Identificar a fonte e aplicar sempre a norma mais recente ao caso.

C) Identificar a finalidade e afastar a competência quando houver eficiência.

D) Identificar fonte, âmbito, sujeito, conduta e competência.


#### Extra Dia 3.6 — Detalhamento por resolução

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Uma resolução detalha procedimento, mas alternativa diz que revogou lei. Avalie.

A) Prevalece sobre a lei se for mais recente e tratar de procedimento específico.

B) Pode detalhar a execução em sua competência, sem revogar a lei.

C) Suspende a lei apenas na jurisdição regional em que o procedimento se aplica.

D) Vincula a Administração mesmo se contrariar a base legal que regulamenta.


#### Extra Dia 3.7 — Comando negativo institucional

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Assinale a alternativa INCORRETA.

A) O decreto disciplina a execução da lei sem poder contrariá-la.

B) O CFA exerce atribuições nacionais de orientação e supervisão do sistema.

C) A autonomia do CRA-PR permite afastar orientação federal incompatível com sua gestão.

D) O CRA-PR exerce registro, orientação e fiscalização em sua jurisdição.


#### Extra Dia 3.8 — Competência e território

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Fato no Paraná possui orientação nacional. Qual análise é adequada?

A) Aplicar a orientação nacional e conferir a competência regional para executar ou fiscalizar.

B) Aplicar apenas a orientação regional, pois o território desloca a competência normativa.

C) Transferir a orientação nacional ao CRA-PR, que passa a defini-la para o caso.

D) Aplicar a orientação nacional sem conferir qual órgão tem competência executória.


#### Extra Dia 3.9 — Hierarquia e jurisdição

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Qual distinção está correta?

A) Jurisdição define força normativa; hierarquia define o território de aplicação.

B) Jurisdição delimita território; hierarquia ordena a força das fontes.

C) Jurisdição e hierarquia indicam, ambas, o órgão que praticará o ato.

D) Jurisdição e hierarquia são filtros equivalentes para o mesmo problema.


#### Extra Dia 3.10 — Caso integrado de fonte

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

Decisão regional contraria lei alegando autonomia e eficiência. Qual resposta é correta?

A) Manter a decisão, pois eficiência permite flexibilizar competência no caso concreto.

B) Revogar a lei no âmbito regional, pois autonomia transfere força normativa.

C) Tratar a lei como orientação nacional, sem efeito sobre a decisão executória.

D) Reconhecer que autonomia e eficiência não afastam legalidade nem competência.


#### Extra Dia 3.11 — Referente inequívoco

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“Cadastro notificou Cobrança quando ele falhou.” Se Cobrança falhou, qual revisão elimina ambiguidade?

A) Quando ele falhou, Cadastro notificou Cobrança.

B) Quando Cobrança falhou, Cadastro enviou a notificação.

C) Quando Cadastro falhou, enviou a notificação a Cobrança.

D) Quando Cobrança falhou, enviou a notificação a Cadastro.


#### Extra Dia 3.12 — Paralelismo verbal

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Qual enumeração mantém paralelismo?

A) Modelar, a geração e que testes sejam.

B) Componentes modelados, gerar e rastreabilidade.

C) A modelagem, gerar e testes que rastreiam.

D) Modelar componentes, gerar código e rastrear testes.


#### Extra Dia 3.13 — Restritiva e explicativa

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Em “Os módulos que falharam serão reimplantados”, a oração:

A) restringe o conjunto aos módulos que falharam.

B) explica que todos os módulos falharam.

C) atribui à falha a causa da reimplantação.

D) informa que a reimplantação causou as falhas.


#### Extra Dia 3.14 — Conector conclusivo

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Qual conector introduz conclusão?

A) Embora.

B) Porque.

C) Portanto.

D) Contudo.


#### Extra Dia 3.15 — Escopo da negação

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“Nem todos os artefatos foram implantados” significa:

A) nenhum foi implantado.

B) alguns foram implantados e alguns não.

C) existe ao menos um não implantado.

D) exatamente um não foi implantado.


#### Extra Dia 3.16 — Possibilidade e garantia

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

Um teste mostrou que a configuração pode funcionar no cenário. Qual reescrita preserva a força?

A) O resultado indica possibilidade no cenário avaliado, sem garantia para os demais.

B) O resultado recomenda uso nos demais ambientes, embora ainda precisem ser testados.

C) O resultado comprova funcionamento nos ambientes equivalentes ao cenário testado.

D) O resultado garante funcionamento sempre que o cenário se repete.


#### Extra Dia 3.17 — Ambiguidade técnica

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“O artefato foi enviado ao nó com sua configuração.” Se a configuração é do artefato, qual revisão é precisa?

A) O artefato e sua configuração foram enviados pelo nó de destino.

B) O nó recebeu o artefato acompanhado de sua própria configuração.

C) A configuração do nó foi enviada juntamente com o artefato.

D) O artefato, com a configuração correspondente, foi enviado ao nó.


#### Extra Dia 3.18 — Reescrita paralela

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

A instrução exige três ações da equipe: versionar o modelo, revisar o código e registrar o teste. Qual redação preserva agente, obrigação e paralelismo?

A) A equipe deve versionar o modelo, revisar o código e talvez registrar o teste.

B) A equipe deve versionar o modelo, revisar o código e registrar o teste.

C) À equipe cabem o versionamento do modelo, revisar o código e o registro do teste.

D) O modelo deve versionar a equipe, revisar o código e registrar o teste.


#### Extra Dia 3.19 — Três filtros de reescrita

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

“Embora o build tenha passado, isso não garante todos os ambientes.” Qual versão preserva concessão, referente e força?

A) Embora o build tenha passado, o resultado não assegura a correção de todos os ambientes.

B) Como o build passou, o resultado assegura a correção em todos os ambientes.

C) Embora o build tenha passado, todos os ambientes dispensam nova validação.

D) Apesar de isso ter passado, eles não garantem a correção do ambiente.


#### Extra Dia 3.20 — Justificativa técnica precisa

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues) e [artefatos e deployment](semana_04_estudo.md#s4-d3-artefatos).

Qual justificativa distingue manifestação e deployment?

A) O arquivo concretiza o nó e, por isso, o componente passa a funcionar.

B) O nó manifesta o arquivo, enquanto o componente é implantado no ambiente.

C) O arquivo manifesta o componente e é implantado no nó de execução.

D) O deployment realiza a interface e dispensa o teste do componente.


## Gabarito - Dia 3

### Principais

| S4D3Q101 | S4D3Q102 | S4D3Q103 | S4D3Q104 | S4D3Q105 | S4D3Q106 | S4D3Q107 | S4D3Q108 | S4D3Q109 | S4D3Q110 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | B | C | D | B | D | A | C | C | A |

| S4D3Q111 | S4D3Q112 | S4D3Q113 | S4D3Q114 | S4D3Q115 | S4D3Q116 | S4D3Q117 | S4D3Q118 | S4D3Q119 | S4D3Q120 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | A | C | B | D | D | B | C | A |

| S4D3Q121 | S4D3Q122 | S4D3Q123 | S4D3Q124 | S4D3Q125 | S4D3Q126 | S4D3Q127 | S4D3Q128 | S4D3Q129 | S4D3Q130 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | B | A | C | B | D | D | B |

| S4D3Q131 | S4D3Q132 | S4D3Q133 | S4D3Q134 | S4D3Q135 | S4D3Q136 | S4D3Q137 | S4D3Q138 | S4D3Q139 | S4D3Q140 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | D | A | C | C | D | A | B |

| S4D3Q141 | S4D3Q142 | S4D3Q143 | S4D3Q144 | S4D3Q145 | S4D3Q146 | S4D3Q147 | S4D3Q148 | S4D3Q149 | S4D3Q150 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | B | B | D | C | B | D |

### Extras

| 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | B | D | D | B | C | A | B | D |

| 3.11 | 3.12 | 3.13 | 3.14 | 3.15 | 3.16 | 3.17 | 3.18 | 3.19 | 3.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | C | A | D | B | A | C |

## Comentários - Dia 3

### Comentário S4D3Q101

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O componente representa a unidade modular e não fixa o recurso de execução.
- **B)** Incorreta. Nó responde à arquitetura de execução, não à responsabilidade modular.
- **C)** Incorreta. Caminho representa comunicação entre nós, não um módulo.
- **D)** Incorreta. Artefato é peça física de informação, não a capacidade lógica.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q102

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A pergunta pede o módulo entregável, não um componente por classe interna.
- **B)** Correta. A granularidade modular concentra as classes internas sob um componente.
- **C)** Incorreta. Artefato não substitui a unidade modular nem seu contrato.
- **D)** Incorreta. As classes pertencem a Processos, não ao componente Portal.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q103

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A fusão aumenta acoplamento e dificulta a troca do provedor.
- **B)** Incorreta. Porta é ponto de interação, não fornecedor externo.
- **C)** Correta. A separação com contrato explícito limita o acoplamento à abstração.
- **D)** Incorreta. Topologia física não define a abstração lógica necessária.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q104

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Porta de nó pertence à visão de execução, não ao contrato oferecido.
- **B)** Incorreta. Classe iniciadora não define, por si, o serviço externo do componente.
- **C)** Incorreta. O artefato concretiza informação; não descreve o serviço oferecido.
- **D)** Correta. A interface explicita o serviço externo preservando encapsulamento.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q105

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Separação por tecnologia não cria responsabilidades coesas nem contratos explícitos.
- **B)** Correta. A solução melhora coesão sem ocultar integrações legítimas.
- **C)** Incorreta. Separação física com duplicação não resolve a mistura de responsabilidades.
- **D)** Incorreta. Ocultar dependências no desenho não reduz seu impacto real.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q106

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Essa é pergunta de deployment.
- **B)** Incorreta. Interação temporal é própria de sequência.
- **C)** Incorreta. Essa pergunta é tratada por estados.
- **D)** Correta. A visão organiza módulos e seus contratos.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q107

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Não há correspondência obrigatória um-para-um.
- **B)** Incorreta. Visibilidade pública não fixa a fronteira modular.
- **C)** Incorreta. Ser pública não torna a classe realizadora obrigatória de interface.
- **D)** Incorreta. Classe é classificador, não artefato implantável por definição.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q108

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Dependências só ganham sentido depois de existir responsabilidade e contrato reconhecíveis.
- **B)** Incorreta. Misturar a visão lógica com nó e artefato não define a capacidade modular.
- **C)** Correta. Responsabilidade e contrato tornam o elemento verificável.
- **D)** Incorreta. Detalhar realização interna antes do contrato não corrige a lacuna externa.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q109

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Isso acopla a regra às implementações.
- **B)** Incorreta. Contratos distintos não permitem trocar realizações sob a mesma abstração.
- **C)** Correta. O consumidor permanece estável enquanto a realização varia.
- **D)** Incorreta. Cobrança é consumidora do contrato, não sua realização substituta.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q110

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A análise segue os consumidores da interface afetada.
- **B)** Incorreta. Posição não estabelece dependência.
- **C)** Incorreta. Mudança lógica não afeta automaticamente todo recurso.
- **D)** Incorreta. Clientes que usam a operação podem quebrar.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q111

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Expor a realização reduz encapsulamento e não é requisito para substituição.
- **B)** Incorreta. Componente pode conter classificadores e também expor contratos.
- **C)** Incorreta. O nó posiciona execução, mas não determina a responsabilidade lógica.
- **D)** Correta. Encapsulamento controla exposição, não elimina estrutura interna.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q112

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Gabarito:** B (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. A requerida expressa Portal como consumidor dessa necessidade.
- **B)** Incorreta (gabarito). O diagrama declara contrato, mas não prova atributos operacionais.
- **C)** Correta. A fornecida expressa Cadastro como fornecedor do serviço.
- **D)** Correta. A montagem declara uma relação que deverá ser verificada.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** Limites da modelagem.

**Pegadinha:** Transformar relação declarada em prova de qualidade.

**Como pensar:** Identifique a pergunta da visão e separe responsabilidade lógica, contrato, arquivo e execução.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q113

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É quem cumpre o contrato.
- **B)** Incorreta. Relatórios requer o serviço, embora inicie a chamada.
- **C)** Incorreta. Invocar o contrato não torna Relatórios fornecedor junto com Cadastro.
- **D)** Incorreta. A interface define operações, mas quem as cumpre e fornece é Cadastro.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q114

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Isso afirmaria que Portal oferece o serviço.
- **B)** Incorreta. Necessidade não é recurso físico.
- **C)** Correta. A requerida explicita serviço necessário ao consumidor.
- **D)** Incorreta. Manifestação não expressa consumo.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q115

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Porta UML não identifica necessariamente porta TCP.
- **B)** Correta. A porta organiza comunicação na fronteira.
- **C)** Incorreta. Artefato pode manifestar elemento lógico, mas não é porta.
- **D)** Incorreta. Nó é recurso de execução, não ponto da fronteira do componente.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q116

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Manifestação envolve artefato.
- **B)** Incorreta. Ligação lógica não determina co-localização.
- **C)** Incorreta. Montagem não é generalização.
- **D)** Correta. A conexão casa necessidade e oferta compatíveis.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q117

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Une nós.
- **B)** Incorreta. Posiciona artefato em nó.
- **C)** Incorreta. Não expressa implementação do contrato.
- **D)** Correta. Associa implementador ao contrato.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q118

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Fornecedor não é cliente nessa relação.
- **B)** Correta. Parte do cliente dependente para o fornecedor.
- **C)** Incorreta. Dependência não é sempre bidirecional.
- **D)** Incorreta. Não é a relação lógica descrita.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q119

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Caminho conecta nós, não artefato e nó; esta última é implantação.
- **B)** Incorreta. As relações pertencem a perguntas e visões distintas.
- **C)** Correta. As relações respondem a visões distintas.
- **D)** Incorreta. Implantação e realização são relações diferentes das duas comparadas.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Separe cliente dependente, fornecedor do serviço e classificador que realiza a interface.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q120

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Porta UML é ponto de interação de um elemento, não endpoint de transporte TCP ou UDP.
- **B)** Correta. A interface fornecida formaliza um serviço que o componente oferece a seus consumidores.
- **C)** Correta. A interface requerida formaliza um serviço de que o componente depende para operar.
- **D)** Correta. A porta pode agrupar interfaces e explicitar um ponto de interação na fronteira do elemento.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Pergunte quem cumpre o contrato, quem precisa dele e por qual ponto ele é exposto.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q121

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A dependência concreta acopla Portal a uma implementação.
- **B)** Incorreta. Contratos diferentes não sustentam a mesma substituição transparente.
- **C)** Correta. Separa contrato, realizações e decisão de ambiente.
- **D)** Incorreta. Ativar apenas um não elimina o acoplamento direto a ambos.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Aplique direção do consumidor e realização pelas alternativas.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q122

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Encapsulamento protege clientes quando o contrato permanece.
- **B)** Incorreta. Refatoração lógica não exige migração física.
- **C)** Incorreta. Refatorar não inverte papéis de interfaces.
- **D)** Incorreta. A realização pode continuar vinculada ao contrato preservado.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Verifique primeiro se o contrato observável mudou.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q123

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Montagem não prova compatibilidade pelo nome.
- **B)** Incorreta. Assinatura aparente não resolve divergência semântica.
- **C)** Incorreta. Co-localização não corrige formato nem significado.
- **D)** Correta. Contrato envolve significado, não só aparência.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Cheque assinatura, significado e teste.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q124

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Detalhar a visão lógica não mostra ambientes nem caminhos físicos.
- **B)** Correta. A visão acrescenta onde e como executar.
- **C)** Incorreta. Classe associada a servidor mistura responsabilidade lógica e execução.
- **D)** Incorreta. Anotar endereços na visão lógica não substitui uma topologia de deployment.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Separe o que a visão atual responde e complemente-a.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q125

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Distingue interações sem duplicar responsabilidade.
- **B)** Incorreta. Duplica a responsabilidade e não separa adequadamente os canais.
- **C)** Incorreta. Caminho físico conecta nós, não representa contrato do canal.
- **D)** Incorreta. Um único contrato ocultaria a diferença entre os canais exigida no cenário.

**Conceito:** Contrato de componente.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com porta de rede.

**Como pensar:** Distinga responsabilidade, ponto e contrato.

**Referência à apostila de estudo:** [Interfaces fornecidas, requeridas e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4D3Q126

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O terceiro continua candidato porque depende da mesma interface e precisa ser confirmado.
- **B)** Incorreta. Revisar todos não significa alterar quem usa operação compatível.
- **C)** Correta. Dependência aponta candidatos; uso refina impacto.
- **D)** Incorreta. Alterar apenas o fornecedor não trata consumidores afetados pela assinatura.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Use dependência, operação usada e versionamento.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q127

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Consumo não é implementação.
- **B)** Correta. Requerer e realizar são papéis distintos.
- **C)** Incorreta. Receber e executar caracteriza fornecimento.
- **D)** Incorreta. Interface não é artefato.

**Conceito:** Dependência e realização.

**Pegadinha:** Inverter a direção da dependência ou tratar uso como realização.

**Como pensar:** Identifique consumidor, contrato e implementador.

**Referência à apostila de estudo:** [Dependência, realização e substituição](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4D3Q128

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Modelar estrutura interna não obriga expô-la aos consumidores.
- **B)** Incorreta. O contrato expõe apenas o necessário, não toda a realização.
- **C)** Incorreta. Parte lógica interna não se torna nó de execução.
- **D)** Correta. Detalhamento interno não obriga exposição total.

**Conceito:** Componente e responsabilidade modular.

**Pegadinha:** Confundir módulo lógico com classe, arquivo ou servidor.

**Como pensar:** Separe detalhamento interno de exposição ao cliente.

**Referência à apostila de estudo:** [Componentes como unidades modulares](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4D3Q129

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O componente lógico não é implantado diretamente; um artefato faz a ponte.
- **B)** Incorreta. Artefato manifesta componente, e nó não manifesta artefato.
- **C)** Incorreta. Ambiente não manifesta componente, e artefato não realiza ambiente.
- **D)** Correta. Manifestação liga lógico a físico; deployment posiciona.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Componente lógico → artefato → nó.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q130

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Contrato lógico é interface, não nó.
- **B)** Correta. Essa é sua função.
- **C)** Incorreta. Sequência de mensagens pertence à visão de interação.
- **D)** Incorreta. Unidade modular com regra é componente, não nó.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Localize dispositivo, ambiente, artefato e caminho; só então avalie a topologia.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q131

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Troca as semânticas.
- **B)** Incorreta. Nenhuma classificação corresponde.
- **C)** Correta. Cada elemento ocupa a camada adequada.
- **D)** Incorreta. Não representa o cenário.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Classifique hardware, plataforma e peça.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q132

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Declara conectividade relevante entre nós.
- **B)** Incorreta. Liga implementador a contrato.
- **C)** Incorreta. Envolve artefato e elemento lógico.
- **D)** Incorreta. Não há especialização.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Localize dispositivo, ambiente, artefato e caminho; só então avalie a topologia.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q133

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não mostra conectividade.
- **B)** Incorreta. Contradiz a restrição.
- **C)** Incorreta. Realização não é caminho.
- **D)** Correta. Registra a mediação exigida.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Materialize apenas caminhos autorizados.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q134

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. As VMs são ambientes no dispositivo, não dispositivos contidos em componente.
- **B)** Incorreta. VM é ambiente de execução, não artefato.
- **C)** Incorreta. A contenção está invertida e caminho não substitui os ambientes.
- **D)** Correta. Separa hardware comum e contextos de execução.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Aplique recurso físico, virtualização e posicionamento.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q135

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra lógico, físico e conectividade.
- **B)** Incorreta. Componentes não são implantados diretamente e interfaces não são caminhos físicos.
- **C)** Incorreta. Nós não são manifestados por artefatos, e dependência não representa isolamento físico.
- **D)** Incorreta. Co-localização contradiz o isolamento e contrato não configura a topologia.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Verifique manifestação, destino e conectividade.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q136

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Os nós representados e seus papéis podem ser lidos no próprio diagrama.
- **B)** Incorreta. O caminho já declara a comunicação prevista.
- **C)** Correta. Caminho não prova todos os atributos.
- **D)** Incorreta. Artefatos e manifestação são outra pergunta, não os atributos do caminho declarado.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Separe conectividade de atributos verificáveis.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q137

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Uma implantação adicional não cria interface lógica.
- **B)** Incorreta. Um mesmo componente pode ser concretizado pelo artefato implantado em vários nós.
- **C)** Correta. Multiplicidade física pode cumprir a mesma responsabilidade.
- **D)** Incorreta. Pode ser o mesmo artefato nos dois nós, e a manifestação permanece válida.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Separe identidade lógica, pacote e multiplicidade.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q138

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não posiciona arquivo.
- **B)** Incorreta. Dispositivo não é interface.
- **C)** Incorreta. Não há especialização.
- **D)** Correta. Registra onde a peça é instalada/executada.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Pergunte se a relação explica o que o arquivo concretiza ou onde ele é instalado.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q139

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Nó é recurso; componente é módulo lógico.
- **B)** Correta. Dispositivo pode conter ambientes de execução.
- **C)** Correta. Artefato pode ser implantado em dispositivo ou ambiente.
- **D)** Correta. Caminho de comunicação conecta nós da topologia.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Diagrama de deployment.

**Pegadinha:** Misturar módulo lógico, arquivo implantável e recurso de execução.

**Como pensar:** Localize dispositivo, ambiente, artefato e caminho; só então avalie a topologia.

**Referência à apostila de estudo:** [Nós e ambientes de execução](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4D3Q140

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A direção da manifestação e o elemento implantado estão trocados.
- **B)** Correta. Uma explica concretização; outra posicionamento.
- **C)** Incorreta. Artefato não realiza componente, e manifestação não posiciona o jar na JVM.
- **D)** Incorreta. Deployment não liga jar a componente e JVM não realiza artefato.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Filtre lógico, peça física e destino.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q141

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Variação de ambiente não cria responsabilidades lógicas distintas.
- **B)** Correta. Separa o comum do variável.
- **C)** Incorreta. Ambiente não é manifestado por configuração, e nó não é o item implantado.
- **D)** Incorreta. O modelo precisa registrar a configuração variável de cada ambiente.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Distinga componente, pacote e configuração.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q142

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mistura elementos lógicos com um artefato.
- **B)** Incorreta. Mistura nós e relação com um artefato.
- **C)** Incorreta. Mistura artefatos com componente e ambiente de execução.
- **D)** Correta. São peças físicas de informação.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Procure peças de informação concretas.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q143

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Conserva lógico, físico e destino.
- **B)** Incorreta. Componente não manifesta artefato, e JVM não é implantada no arquivo.
- **C)** Incorreta. JVM não manifesta componente, e artefato não é implantado em componente.
- **D)** Incorreta. Artefato manifesta componente, não o realiza; JVM não manifesta arquivo.

**Conceito:** Artefato, manifestação e deployment.

**Pegadinha:** Usar manifestação e deployment como relações equivalentes.

**Como pensar:** Classifique os elementos antes das relações.

**Referência à apostila de estudo:** [Artefatos, manifestação e implantação](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4D3Q144

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Ligação apenas por nomes não cria cadeia rastreável entre evidências.
- **B)** Incorreta. Autoria do commit não o vincula ao requisito e ao teste.
- **C)** Correta. Cria a cadeia de evidências ausente.
- **D)** Incorreta. Build sem vínculo com requisito não resolve a causa da desconexão.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Use lacuna, vínculo e evidência.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q145

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Código não revela integralmente os requisitos que o originaram.
- **B)** Correta. Extrai estrutura, não toda a intenção.
- **C)** Incorreta. A estrutura atual pode divergir da arquitetura planejada.
- **D)** Incorreta. Estrutura extraída não comprova comportamento nem substitui testes.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Avalie observação, inferência e validação.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q146

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Esqueleto estrutural não prova requisitos não funcionais.
- **B)** Correta. Automação não substitui verificação.
- **C)** Incorreta. Código gerado também precisa de histórico próprio e rastreável.
- **D)** Incorreta. Alteração manual pode romper a sincronização.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Separe estrutura, comportamento e evidência.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q147

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Precedência fixa do modelo pode descartar correção válida do código.
- **B)** Incorreta. Precedência fixa do código pode ignorar decisão ainda não implementada.
- **C)** Incorreta. Compartilhar repositório não resolve conflito sem governança.
- **D)** Correta. Sincronização não resolve governança.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Combine sincronização, autoridade e revisão.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q148

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Faltam histórico de mudança, build versionado, teste e destino registrado.
- **B)** Incorreta. Tarefa sem commit, build local e teste sem versão quebram a cadeia.
- **C)** Correta. Cobre intenção, mudança, produto, verificação e destino.
- **D)** Incorreta. Código gerado e build não substituem teste nem registro de aceite/deployment.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Exija origem, mudança, build, teste e implantação.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q149

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Falta versionar antes da cópia, testar compatibilidade e registrar os destinos.
- **B)** Correta. Integra contrato, impacto, artefato, teste e topologia.
- **C)** Incorreta. Builds locais e validação de um único nó não controlam a mudança completa.
- **D)** Incorreta. Novo servidor não corrige contrato nem comprova compatibilidade.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Percorra contrato, consumidores, implementação, artefato, teste e destinos.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4D3Q150

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Builds locais continuam sem identidade reprodutível e a comparação manual não prova cada deployment.
- **B)** Incorreta. Recompilar sem ID não cria artefato imutável nem verifica ambos os nós.
- **C)** Incorreta. Build mutável e registro apenas do ambiente não controlam a deriva por nó.
- **D)** Correta. Trata coerência, reprodutibilidade e deriva operacional.

**Conceito:** Ferramentas de apoio ao desenvolvimento.

**Pegadinha:** Atribuir à automação garantia de intenção, qualidade ou atualização.

**Como pensar:** Aplique controle de fonte, identidade do artefato e evidência por destino.

**Referência à apostila de estudo:** [Ferramentas de apoio e rastreabilidade](semana_04_estudo.md#s4-d3-ferramentas).


#### Comentário Extra Dia 3.1

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A lei dá a base e o decreto disciplina sua execução nos limites legais.
- **B)** Incorreta. Posterioridade do decreto não lhe permite afastar a lei.
- **C)** Incorreta. A lei federal não organiza apenas o conselho regional.
- **D)** Incorreta. Lei e decreto não têm o mesmo nível hierárquico.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.2

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O fato regional não transfere ao CRA-PR toda competência nacional.
- **B)** Incorreta. Atuação nacional não concentra no CFA toda execução regional.
- **C)** Correta. Combina integração e âmbito.
- **D)** Incorreta. Âmbitos distintos coexistem dentro do sistema integrado.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.3

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Regimento não amplia competência interna além da lei.
- **B)** Correta. Estrutura atuação interna sem superar lei.
- **C)** Incorreta. Regimento regional não substitui competências nacionais do CFA.
- **D)** Incorreta. Fonte interna não disciplina a profissão nem afasta decreto superior.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.4

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Autonomia regional continua integrada ao sistema nacional.
- **B)** Incorreta. Gestão regional não altera a hierarquia das fontes.
- **C)** Incorreta. Local do fato não transfere todas as competências nacionais.
- **D)** Correta. Autonomia e integração coexistem.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.5

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Território isolado não permite presumir competência.
- **B)** Incorreta. Fonte mais recente não prevalece automaticamente sobre superior.
- **C)** Incorreta. Finalidade e eficiência não afastam competência.
- **D)** Correta. Os filtros evitam transferências indevidas.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.6

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Cronologia e especialidade não tornam resolução superior à lei.
- **B)** Correta. Regulamentação é limitada pela hierarquia.
- **C)** Incorreta. Resolução não suspende lei no território regional.
- **D)** Incorreta. Procedimento administrativo continua vinculado à base legal.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.7

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Gabarito:** C (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. O Decreto nº 61.934/1967 disciplina a execução da Lei nº 4.769/1965.
- **B)** Correta. A atuação nacional do CFA integra a divisão institucional revisada.
- **C)** Incorreta (gabarito). Autonomia de gestão não permite afastar orientação federal válida.
- **D)** Correta. O CRA-PR exerce atribuições dentro de sua jurisdição e competência.

**Observação:** a questão pede a alternativa incorreta; por isso, C é o gabarito.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.8

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A orientação nacional e a competência executória regional são filtros distintos.
- **B)** Incorreta. Território não desloca competência normativa nacional.
- **C)** Incorreta. Execução regional não transfere ao CRA-PR a definição da orientação nacional.
- **D)** Incorreta. Aplicar orientação sem conferir competência executória omite filtro indispensável.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.9

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte os papéis dos dois filtros.
- **B)** Correta. São dimensões diferentes.
- **C)** Incorreta. Nenhum dos filtros, isoladamente, identifica sempre o agente competente.
- **D)** Incorreta. Território e força da fonte são problemas distintos.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.10

- **Dia:** Dia 3
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, âmbito e competência no Sistema CFA/CRAs
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Eficiência não flexibiliza competência contra a lei.
- **B)** Incorreta. Autonomia não permite revogar lei em âmbito regional.
- **C)** Incorreta. Lei federal aplicável não se reduz a orientação sem efeito.
- **D)** Correta. Os filtros convergem.

**Conceito:** Fonte, âmbito e competência no Sistema CFA/CRAs.

**Pegadinha:** Confundir hierarquia, autonomia e jurisdição.

**Como pensar:** Classifique fonte, âmbito, sujeito, conduta e competência.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d3-b4-legislacao).


#### Comentário Extra Dia 3.11

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O pronome continua com referente ambíguo.
- **B)** Correta. O nome fixa o referente.
- **C)** Incorreta. Torna Cadastro, e não Cobrança, o elemento que falhou.
- **D)** Incorreta. Torna Cobrança agente da notificação e muda o sentido.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.12

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mistura estruturas.
- **B)** Incorreta. Não é paralela.
- **C)** Incorreta. Mistura categorias.
- **D)** Correta. Três verbos no infinitivo.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.13

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Delimita o referente.
- **B)** Incorreta. A leitura de todos os módulos dependeria de oração explicativa.
- **C)** Incorreta. A oração delimita o conjunto; não estabelece, por si, relação causal.
- **D)** Incorreta. A oração não torna a reimplantação causa das falhas.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.14

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Marca concessão.
- **B)** Incorreta. Marca causa.
- **C)** Correta. Marca consequência/conclusão.
- **D)** Incorreta. Marca contraste.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.15

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. É mais forte.
- **B)** Incorreta. A frase admite que nenhum tenha sido implantado; não garante os dois grupos.
- **C)** Correta. Nega o universal por contraexemplo.
- **D)** Incorreta. A quantidade de não implantados não é determinada.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.16

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Mantém escopo e modalidade.
- **B)** Incorreta. Introduz recomendação de uso que o resultado não sustenta.
- **C)** Incorreta. Amplia a evidência para ambientes apenas considerados equivalentes.
- **D)** Incorreta. Transforma possibilidade observada em garantia repetível.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.17

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Torna o nó agente do envio e altera o sentido.
- **B)** Incorreta. “Sua” passa a ligar a configuração ao nó.
- **C)** Incorreta. Atribui a configuração ao nó, não ao artefato.
- **D)** Correta. A posse fica explícita.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.18

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. “Talvez” enfraquece apenas a terceira obrigação.
- **B)** Correta. Três deveres paralelos.
- **C)** Incorreta. Mistura construções nominais e verbais sem paralelismo.
- **D)** Incorreta. Atribui ao modelo a ação reservada à equipe.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.19

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Muito difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. `Embora` mantém a concessão; `o resultado` explicita o referente; `não assegura` preserva a força.
- **B)** Incorreta. Troca concessão por causa e cria garantia geral.
- **C)** Incorreta. Mantém a concessão, mas conclui dispensa indevida de validação.
- **D)** Incorreta. Referentes vagos e escopo singular impedem preservar o sentido.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues).


#### Comentário Extra Dia 3.20

- **Dia:** Dia 3
- **Bloco:** Bloco 5
- **Matéria:** Língua Portuguesa
- **Assunto:** Precisão, paralelismo e escopo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues) e [artefatos e deployment](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Artefato não concretiza nó, e funcionamento não decorre apenas da relação.
- **B)** Incorreta. Nó não manifesta arquivo, e componente não é implantado diretamente.
- **C)** Correta. Nomeia elementos e relações corretamente.
- **D)** Incorreta. Deployment não realiza interface nem elimina testes.

**Conceito:** Precisão, paralelismo e escopo.

**Pegadinha:** Alterar referente, relação ou força da afirmação.

**Como pensar:** Cheque referente, paralelismo, conector e escopo.

**Referência à apostila de estudo:** [Português aplicado](semana_04_estudo.md#s4-d3-b5-portugues) e [artefatos e deployment](semana_04_estudo.md#s4-d3-artefatos).


---
# Dia 4 - Engenharia de software, ciclos de vida e gerenciamento de projetos

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. A matriz inicial é 20/20/10 nas principais e 8/8/4 nas extras. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais - S4D4Q151 a S4D4Q200

### S4D4Q151 — Finalidade da engenharia

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Qual descrição melhor caracteriza engenharia de software?

A) Disciplina que aplica processo, método e controle ao desenvolvimento e à evolução.

B) Disciplina que concentra o desenvolvimento na produção e aprovação de modelos.

C) Automação que transforma requisitos informais em software validado.

D) Processo que congela requisitos para impedir mudanças durante o desenvolvimento.


### S4D4Q152 — Processo e produto

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

No fluxo “validar requisito”, qual é um produto observável?

A) Ata que comprova apenas a presença dos participantes.

B) Registro versionado da decisão e de seu resultado.

C) Relatório que informa somente a duração da reunião.

D) Histórico da ferramenta usada para projetar o requisito.


### S4D4Q153 — Método e ferramenta

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Assinale a distinção correta.

A) Método registra a execução; ferramenta define como executar.

B) Método organiza atividades; ferramenta decide quais são necessárias.

C) Método orienta a execução; ferramenta automatiza ou registra parte dela.

D) Método e ferramenta são produtos observáveis gerados pelo processo.


### S4D4Q154 — Adaptação proporcional

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Correção textual e integração de pagamentos usam controles idênticos e pesados. Qual decisão é coerente?

A) Usar o mesmo fluxo, mas dispensar versão na correção textual.

B) Reduzir controles da integração porque o prazo torna o risco aceitável.

C) Aplicar controles idênticos, pois proporcionalidade compromete auditoria.

D) Preservar controles mínimos e ampliá-los conforme risco e evidência exigida.


### S4D4Q155 — Evidência de validação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Houve reunião de requisitos, sem decisão nem versão. O que falta?

A) Um registro dos participantes, ainda que não informe a decisão.

B) Uma saída rastreável que registre critério e resultado da validação.

C) Uma nova reunião, desta vez sem interessados externos.

D) Uma ferramenta diferente, capaz de substituir a decisão humana.


### S4D4Q156 — Processo em cenário público

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

Em sistema público sujeito a auditoria, qual prática combina adaptação e controle?

A) Registrar todas as atividades, ainda que decisões e versões não se relacionem.

B) Reduzir evidências nas mudanças críticas para acelerar a aprovação formal.

C) Aplicar o mesmo volume documental a toda mudança, sem classificar o risco.

D) Definir evidências pelo risco e rastrear decisões até teste e aceite.


### S4D4Q157 — Ênfase da cascata

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

A cascata enfatiza:

A) fases predominantemente sequenciais, com produtos e marcos definidos.

B) ciclos que priorizam os maiores riscos antes de planejar a volta seguinte.

C) entregas funcionais sucessivas que ampliam a capacidade do produto.

D) composição do sistema a partir de ativos previamente avaliados.


### S4D4Q158 — Núcleo da espiral

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual elemento distingue a espiral?

A) Sequência sem análise de incerteza.

B) Geração automática como marco.

C) Ciclos guiados pela identificação e redução de riscos.

D) Entrega integral antes de consultar usuários.


### S4D4Q159 — Reuso avaliado

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Antes de reutilizar componente pronto, deve-se avaliar:

A) adequação funcional, ignorando custos de adaptação já estimados.

B) preço de aquisição e prazo, transferindo o risco ao fornecedor.

C) adequação, adaptação, integração, teste, dependência e custo total.

D) compatibilidade técnica, sem considerar suporte e dependência futura.


### S4D4Q160 — Protótipo descartável

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Protótipo usa dados fixos e não tem segurança; valida navegação. O tratamento adequado é:

A) Registrar o aprendizado e reimplementar conforme arquitetura e controles produtivos.

B) Evoluir o mesmo código, ainda que seus atalhos não tenham sido avaliados.

C) Entregá-lo como incremento, limitando o aceite ao fluxo de navegação.

D) Mantê-lo como solução paralela para obter novo feedback em produção.


### S4D4Q161 — Protótipo evolutivo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Se o protótipo evoluirá até o produto, qual condição é essencial?

A) Manter os atalhos, desde que o protótipo já tenha validado a interface.

B) Adiar testes não funcionais até a primeira versão usada em produção.

C) Tratar o código como descartável, mesmo após decidir que será mantido.

D) Sustentar arquitetura, qualidade e critérios de evolução desde o início.


### S4D4Q162 — Condições para RAD

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual contexto favorece RAD?

A) Sistema acoplado, tecnologia inédita e validações esporádicas dos usuários.

B) Escopo modular, tecnologia conhecida e usuários disponíveis para decisões rápidas.

C) Escopo amplo, arquitetura incerta e equipe sem poder de decisão.

D) Sistema crítico integrado, prazo curto e indisponibilidade de especialistas.


### S4D4Q163 — Desenvolvimento evolutivo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

O desenvolvimento evolutivo caracteriza-se por:

A) amadurecer a solução em versões sucessivas orientadas por uso e feedback.

B) fechar a solução antes da primeira versão e preservar o escopo inicial.

C) compor a solução apenas com ativos existentes e evitar desenvolvimento novo.

D) prototipar a interface, descartar o resultado e manter requisitos estáveis.


### S4D4Q164 — Incremento funcional

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual exemplo constitui incremento?

A) Reorganizar a implementação da consulta sem ampliar a função do portal.

B) Corrigir o desempenho interno da consulta mantendo a mesma capacidade.

C) Adicionar emissão de certificado ao portal que já oferece consulta.

D) Reexecutar os testes da consulta depois de atualizar a infraestrutura.


### S4D4Q165 — Iteração e incremento

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Assinale a distinção correta.

A) Iteração acrescenta capacidade; incremento apenas revisa trabalho existente.

B) Iteração refina trabalho; incremento acrescenta capacidade; ambos podem coexistir.

C) Iteração e incremento são sinônimos quando há mais de uma entrega.

D) Iteração ocorre na análise; incremento, exclusivamente na construção.


### S4D4Q166 — Cenário estável e marcos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Escopo regulatório estável, tecnologia conhecida e aprovações formais. Qual escolha é defensável?

A) Espiral com protótipos para reduzir a incerteza de tecnologia já conhecida.

B) Prototipação descartável promovida a produto após a aprovação do fluxo.

C) RAD sem participação de usuários, pois o escopo já está estável.

D) Cascata adaptada, com marcos, validações e controle de mudanças.


### S4D4Q167 — Cenário de alto risco

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Biometria inédita, integração instável e requisitos incertos dominam. Qual abordagem é alinhada?

A) Cascata com prova técnica adiada até o encerramento da construção.

B) Reuso do primeiro componente disponível, sem avaliar integração.

C) Incrementos funcionais, deixando o risco técnico para a entrega final.

D) Espiral com experimentos voltados à redução dos riscos dominantes.


### S4D4Q168 — Incerteza de interação

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Usuários não descrevem o fluxo, mas avaliam telas simuladas. Qual estratégia ajuda?

A) Cascata com aprovação da descrição incompleta antes de mostrar as telas.

B) Prototipação para aprender com as telas e registrar as decisões obtidas.

C) RAD sem participação dos usuários até a implantação da primeira versão.

D) Build automatizado para substituir a elicitação do fluxo desconhecido.


### S4D4Q169 — Custo total do reuso

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Componente gratuito exige adaptação, infraestrutura e suporte. A decisão considera:

A) preço de licença, pois custo zero torna a integração economicamente neutra.

B) tempo de procura, sem considerar a adaptação posterior do componente.

C) custo total e risco de integração, incluindo adaptação e suporte.

D) quantidade de funções, ainda que infraestrutura e suporte sejam incompatíveis.


### S4D4Q170 — Comando negativo sobre ciclos

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Assinale a alternativa INCORRETA.

A) RAD dispensa arquitetura e aceite quando a velocidade é prioritária.

B) Espiral organiza os ciclos segundo os riscos que devem ser reduzidos.

C) Desenvolvimento incremental amplia a capacidade em partes utilizáveis.

D) Prototipação antecipa uma representação para apoiar a aprendizagem.


### S4D4Q171 — RAD sem atalho

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Módulo independente tem prazo curto e usuários disponíveis. Qual plano usa RAD adequadamente?

A) Prototipar rapidamente e deixar integração e aceite para a entrega final.

B) Componentizar sem limitar o escopo, aproveitando a disponibilidade dos usuários.

C) Prototipar e componentizar, com testes de integração e aceite frequentes.

D) Aplicar o mesmo plano ao sistema crítico, pois o prazo curto justifica RAD.


### S4D4Q172 — Reuso com incompatibilidade

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Biblioteca cobre 80%, mas protocolo, auditoria e suporte divergem. Qual decisão é madura?

A) Comparar adaptação, integração, testes, dependência e construção alternativa.

B) Adotar a biblioteca, pois cobertura de 80% compensa requisitos não atendidos.

C) Descartá-la, pois qualquer incompatibilidade impede reuso economicamente viável.

D) Adotá-la e transferir ao fornecedor a aceitação das lacunas restantes.


### S4D4Q173 — Mudança tardia em cascata

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Requisito muda durante construção em projeto sequencial. Qual resposta é adequada?

A) Recusar a mudança, pois o marco sequencial torna a baseline imutável.

B) Alterar o código e manter especificação e testes como referência original.

C) Reiniciar o projeto na concepção, independentemente do impacto apurado.

D) Analisar o impacto, decidir a mudança e atualizar produtos e baselines.


### S4D4Q174 — Volta da espiral

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

A equipe repete tarefas sem identificar nem tratar riscos. Qual avaliação é correta?

A) A repetição basta, pois a forma cíclica define o modelo espiral.

B) Falta orientar cada volta pela identificação e redução de riscos.

C) A repetição transforma o processo em cascata com retornos controlados.

D) A ausência de registro indica que os riscos já foram reduzidos.


### S4D4Q175 — Fatia incremental

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Como entregar valor cedo sem produzir camada técnica inutilizável isoladamente?

A) Entregar uma capacidade utilizável que atravesse as camadas necessárias.

B) Concluir a camada de dados inteira antes de iniciar qualquer função.

C) Entregar componentes técnicos isolados e integrá-los apenas ao final.

D) Dividir o trabalho pelo tamanho dos arquivos, sem critério de uso.


### S4D4Q176 — Iteração sem incremento

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Qual situação é iteração sem novo incremento?

A) Adicionar emissão de documento à versão que já permitia consulta.

B) Implantar uma nova função de consulta após o aceite dos usuários.

C) Revisar arquitetura e testes do mesmo incremento antes de entregá-lo.

D) Liberar uma segunda capacidade em versão posterior do produto.


### S4D4Q177 — Combinação contextual

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Projeto usa protótipo, espiral e incrementos. Isso é incoerente?

A) Sim; cada projeto precisa adotar um único modelo durante todo o ciclo.

B) Não; estratégias podem cumprir objetivos distintos sob controle comum.

C) Sim; prototipação e incremento sempre produzem artefatos incompatíveis.

D) Não; combinar estratégias torna desnecessário definir critérios de passagem.


### S4D4Q178 — Protótipo e segurança

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Protótipo evolutivo usará dados reais. Como evitar fragilidade?

A) Adiar segurança até a transição, mantendo apenas controles de usabilidade.

B) Definir segurança, arquitetura sustentável e gates de qualidade desde o início.

C) Tratar o código como descartável até a data de entrada em produção.

D) Usar a aprovação da interface como evidência de confidencialidade.


### S4D4Q179 — Incrementos e arquitetura

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Incrementos acumulam duplicação e dependências frágeis. Qual ação preserva evolução?

A) Proibir refatoração para preservar a velocidade de cada incremento isolado.

B) Adiar a integração até o fim, quando todas as capacidades estiverem prontas.

C) Tratar os incrementos como produtos separados, cada qual com sua arquitetura.

D) Refinar arquitetura, executar regressão e controlar dívida a cada ciclo.


### S4D4Q180 — Escolha por quatro critérios

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Escopo muda; valor é fatiável; integração tem alto risco; usuários estão disponíveis. Qual plano é defensável?

A) Usar cascata com teste final, pois a integração recomenda estabilizar o escopo.

B) Combinar incrementos e feedback com experimentos sobre o risco e controle arquitetural.

C) Usar RAD para acelerar, deixando a arquitetura emergir após os primeiros módulos.

D) Priorizar reuso para reduzir construção, mesmo sem ativos avaliados para a integração.


### S4D4Q181 — Finalidade da concepção

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Qual pergunta predomina na concepção?

A) A capacidade planejada foi integrada e verificada?

B) A solução está apta ao uso no ambiente-alvo?

C) A visão e o escopo inicial justificam o projeto?

D) A arquitetura reduziu os riscos centrais?


### S4D4Q182 — Finalidade da elaboração

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

A elaboração enfatiza:

A) arquitetura-base, riscos centrais e requisitos significativos.

B) visão inicial, caso de negócio e limites preliminares.

C) incrementos integrados, testes e documentação da solução.

D) migração, treinamento e aceite no ambiente operacional.


### S4D4Q183 — Finalidade da construção

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Na construção predomina:

A) delimitar visão, escopo inicial e viabilidade do esforço.

B) implementar, integrar e verificar a capacidade planejada.

C) preparar migração, treinamento e aceite no ambiente-alvo.

D) estabilizar arquitetura-base e reduzir os riscos centrais.


### S4D4Q184 — Finalidade da transição

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Qual conjunto associa-se à transição?

A) visão, atores, riscos iniciais e caso de negócio.

B) arquitetura-base, requisitos significativos e prova de risco.

C) código, incrementos integrados e testes da capacidade.

D) implantação, migração, treinamento e aceite operacional.


### S4D4Q185 — Atividades sobrepostas

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Código de protótipo aparece na elaboração para reduzir risco. Isso contradiz as fases?

A) Não; o código pode servir à redução do risco arquitetural dominante.

B) Sim; qualquer produção de código pertence exclusivamente à construção.

C) Não; as quatro fases têm a mesma finalidade e podem se substituir.

D) Sim; na elaboração só se admitem requisitos e diagramas conceituais.


### S4D4Q186 — Marco de elaboração

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Há muitos requisitos, mas arquitetura e integração crítica estão incertas. A elaboração acabou?

A) Sim; o volume de requisitos demonstra maturidade suficiente para o marco.

B) Sim; arquitetura e integração devem ser verificadas apenas na construção.

C) Não; ainda faltam evidências sobre arquitetura e riscos centrais.

D) Não; requisitos significativos não fazem parte dos produtos da elaboração.


### S4D4Q187 — Transição completa

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Pacote foi copiado; migração, treinamento e monitoramento faltam. Avalie.

A) A transição terminou, pois o pacote já está no ambiente de destino.

B) A transição deve ser reiniciada, descartando o deployment já executado.

C) O deployment ocorreu, mas a prontidão operacional ainda não foi demonstrada.

D) A construção não terminou, pois migração e treinamento pertencem a ela.


### S4D4Q188 — Fases sem rigidez

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Assinale a alternativa INCORRETA.

A) Elaboração prioriza riscos arquiteturais antes da construção predominante.

B) Construção implementa e integra a capacidade definida para a iteração.

C) Transição busca uso efetivo da solução no ambiente-alvo.

D) Requisitos só podem ser discutidos durante a fase de concepção.


### S4D4Q189 — Cadeia de evidências

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Há visão aceita, prova arquitetural, incrementos testados e plano de migração não executado. Qual leitura?

A) Há evidências das três primeiras fases; a transição ainda requer execução e validação.

B) Há apenas concepção; as demais evidências são planos sem resultado observável.

C) Há transição concluída; o plano de migração basta como evidência operacional.

D) Há elaboração e transição, mas os incrementos testados não provam construção.


### S4D4Q190 — Comando negativo sobre fases

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

Assinale a alternativa INCORRETA.

A) Transição termina com a cópia do artefato para o ambiente-alvo.

B) Concepção delimita visão, escopo inicial e justificativa do projeto.

C) Elaboração trata arquitetura-base e riscos centrais do projeto.

D) Construção implementa, integra e verifica a capacidade planejada.


### S4D4Q191 — Fases do projeto e operação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

O CRA autoriza um portal após aprovar a justificativa; a equipe detalha as baselines, produz entregas enquanto mede desvios e decide correções, obtém o aceite e transfere o resultado. Depois começa o suporte mensal. Qual leitura é correta?

A) Autorização é planejamento; baselines são iniciação; produção é controle; aceite é execução; suporte é encerramento.

B) Autorização é iniciação; baselines são planejamento; execução convive com acompanhamento e controle; aceite e transferência encerram; suporte é operação.

C) Autorização é execução; baselines são controle; produção é encerramento; aceite inicia a operação; suporte mantém o projeto permanente.

D) Autorização é concepção do RUP; baselines são elaboração; produção dispensa controle; aceite é transição; suporte integra o mesmo projeto.


### S4D4Q192 — Planejar, acompanhar e controlar

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

Há cronograma-base; relatório mostra atraso; gerente analisa e aprova replanejamento. Qual sequência?

A) Planejamento definiu a baseline; acompanhamento aprovou o replanejamento.

B) Planejamento definiu e mediu; controle apenas registrou o atraso observado.

C) Acompanhamento definiu a baseline; controle mediu e planejou a resposta.

D) Planejamento definiu; acompanhamento mediu; controle decidiu e atualizou.


### S4D4Q193 — WBS e cronograma

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

WBS lista entregas hierárquicas; cronograma, atividades e datas. Conclui-se que:

A) WBS decompõe o escopo; cronograma organiza o trabalho no tempo.

B) WBS ordena atividades; cronograma decompõe as entregas do escopo.

C) WBS distribui pessoas; cronograma define os pacotes de trabalho.

D) WBS e cronograma representam a mesma estrutura, com níveis distintos.


### S4D4Q194 — Mudança de escopo integrada

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

Solicita-se novo módulo sem alterar prazo, equipe, orçamento ou qualidade. Qual conduta?

A) Aceitar e acrescentar o módulo à WBS, preservando as demais baselines.

B) Rejeitar, pois uma baseline aprovada torna qualquer mudança inadmissível.

C) Avaliar efeitos em escopo, prazo, custo, qualidade, recursos e riscos.

D) Alterar apenas escopo e orçamento, pois prazo e qualidade foram fixados.


### S4D4Q195 — Tempo, custo e dependência

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

Fornecedor atrasa atividade crítica dez dias e gera ociosidade. Qual análise é completa?

A) Recalcular prazo e custo, executar a resposta ao risco e controlar a mudança.

B) Atualizar o cronograma e manter o orçamento, pois a ociosidade não gera custo.

C) Cobrar o fornecedor e manter as baselines até a atividade voltar ao plano.

D) Remover a dependência crítica do cronograma para preservar o marco original.


### S4D4Q196 — Qualidade e comunicação

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas e comunicação](semana_04_estudo.md#s4-d4-qualidade-pessoas-comunicacao).

Requisito diz “rápido”; direção recebe relatório técnico sem decisão clara. Qual plano resolve ambos?

A) Quantificar “rápido” e manter o mesmo relatório técnico para todos os públicos.

B) Definir medida e teste; adaptar a comunicação à decisão, preservando os fatos.

C) Manter “rápido” e resumir o relatório, retirando resultados desfavoráveis.

D) Usar ausência de reclamações como medida e enviar o painel sem contexto.


### S4D4Q197 — Pessoas, comunicação e risco

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Especialista ficará indisponível antes de integração crítica. Qual resposta integrada?

A) Esperar a indisponibilidade e então redistribuir as tarefas da integração.

B) Adicionar pessoas no último dia e manter papéis e comunicação inalterados.

C) Registrar o risco sem resposta, para não antecipar mudança de responsabilidade.

D) Tratar o risco, transferir conhecimento, ajustar papéis e comunicar marcos.


### S4D4Q198 — Aquisição não transfere tudo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Serviço externo será contratado, sem interface e aceite definidos. Qual afirmação é correta?

A) Contratar por preço e prazo, deixando integração e aceite sob risco do fornecedor.

B) Definir o aceite depois da entrega, quando a interface real estiver disponível.

C) Definir escopo, aceite, riscos, responsáveis e integração antes da contratação.

D) Tratar a integração após o encerramento, quando o serviço já estiver transferido.


### S4D4Q199 — Mudança com cinco impactos

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Mudança amplia usuários, exige fornecedor, eleva carga e altera data. Qual decisão integra?

A) Atualizar WBS, prazo e custo, mantendo capacidade e comunicação já aprovadas.

B) Reavaliar escopo, prazo, custo, qualidade, comunicação, riscos e aquisição.

C) Aprovar a mudança e registrar apenas os impactos que alterarem a data final.

D) Rejeitar a mudança, pois fornecedor e aumento de carga impedem análise integrada.


### S4D4Q200 — Cenário integrado de controle

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Painel mostra atraso; risco virou problema; aquisição depende de integração fora da WBS; teste não tem limite. Qual ação é completa?

A) Tratar o atraso, manter a WBS e aceitar o teste qualitativo até nova medição.

B) Cobrar o fornecedor, incluir a integração na WBS e manter o limite de teste aberto.

C) Tratar problema e risco residual, corrigir WBS e aceite, replanejar e comunicar.

D) Replanejar o prazo, encerrar o risco ocorrido e comunicar somente após o aceite.


## Questões extras - Dia 4

#### Extra Dia 4.1 — Legalidade e eficiência

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Eficiência administrativa:

A) deve ser buscada dentro da legalidade e da competência administrativa.

B) permite flexibilizar procedimento sempre que houver ganho mensurável.

C) supre ausência de competência quando o resultado atende ao interesse público.

D) converte ato lento em inválido, ainda que praticado conforme a lei.


#### Extra Dia 4.2 — Impessoalidade

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Publicidade com promoção pessoal conflita principalmente com:

A) descentralização administrativa e controle de resultados.

B) autotutela administrativa e revisão dos próprios atos.

C) impessoalidade administrativa e finalidade pública.

D) especialidade administrativa e definição de competência.


#### Extra Dia 4.3 — Publicidade e proteção

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Qual afirmação é coerente?

A) A publicidade exige publicar dados pessoais ligados a qualquer ato administrativo.

B) A publicidade favorece transparência, respeitados sigilo legal e proteção de dados.

C) A proteção de dados afasta a publicidade sempre que houver identificação pessoal.

D) A publicidade permite promoção pessoal quando a informação institucional é verdadeira.


#### Extra Dia 4.4 — Desconcentração

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Criar coordenação na mesma pessoa jurídica é:

A) descentralização pela criação de nova entidade.

B) descentralização pela delegação a um particular.

C) desconcentração com criação de nova pessoa jurídica.

D) desconcentração dentro da mesma pessoa jurídica.


#### Extra Dia 4.5 — Autarquia

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Autarquia integra:

A) Administração Direta, como órgão sem personalidade jurídica própria.

B) Administração Indireta, como pessoa jurídica de direito privado.

C) Administração Direta, como entidade com autonomia apenas financeira.

D) Administração Indireta, como pessoa jurídica de direito público.


#### Extra Dia 4.6 — Anulação e revogação

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Ato ilegal; ato válido inconveniente são retirados, respectivamente, por:

A) revogação; anulação.

B) anulação; revogação.

C) desconcentração; descentralização.

D) delegação; avocação.


#### Extra Dia 4.7 — Controle e decisão

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Indicador revela desvio, mas ninguém age. Avalie.

A) Houve controle completo, pois o painel tornou o desvio visível.

B) Houve decisão de controle, mas faltou medir o resultado obtido.

C) Houve acompanhamento, mas faltou decisão para completar o controle.

D) Não houve acompanhamento, pois nenhum ato corretivo foi executado.


#### Extra Dia 4.8 — Cenário organizacional

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Distribuir atribuições entre unidades internas sem nova pessoa caracteriza:

A) desconcentração administrativa.

B) descentralização por outorga.

C) descentralização por delegação.

D) centralização administrativa.


#### Extra Dia 4.9 — Comando negativo administrativo

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Assinale a alternativa INCORRETA.

A) A eficiência administrativa deve permanecer dentro da legalidade.

B) A publicidade exige divulgar dado pessoal sempre que o ato for público.

C) A impessoalidade impede usar a atuação institucional para promoção pessoal.

D) A autarquia integra a Administração Indireta e possui personalidade própria.


#### Extra Dia 4.10 — Caso integrado administrativo

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

Ato ilegal é eficiente e popular. Qual providência conceitual?

A) Revogar o ato por inconveniência, pois a eficiência não foi suficiente.

B) Convalidar o ato, pois resultado popular permite superar vícios de competência.

C) Manter o ato, pois eficiência e popularidade compensam a ilegalidade.

D) Tratar a ilegalidade pela anulação, verificando competência e limites aplicáveis.


#### Extra Dia 4.11 — Implicação

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

“Se marco atrasar, custo aumentará” é falsa somente quando:

A) marco não atrasa e custo aumenta.

B) marco atrasa e custo não aumenta.

C) ambos ocorrem.

D) nenhum ocorre.


#### Extra Dia 4.12 — Contrapositiva

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Contrapositiva de “se teste passou, build foi gerado”:

A) se build foi gerado, teste passou.

B) se teste não passou, build não gerou.

C) teste passou e build não gerou.

D) se build não foi gerado, teste não passou.


#### Extra Dia 4.13 — Negação de conjunção

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Negar “escopo aprovado e risco tratado” resulta em:

A) escopo não aprovado ou risco não tratado.

B) escopo não aprovado e risco não tratado.

C) escopo aprovado ou risco tratado.

D) se escopo aprovado, então risco tratado.


#### Extra Dia 4.14 — Negação universal

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Negar “todo incremento foi testado” é:

A) nenhum foi testado.

B) exatamente um foi testado.

C) existe ao menos um não testado.

D) todos foram testados duas vezes.


#### Extra Dia 4.15 — Aumento percentual

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Custo passou de 80 para 100 mil. O aumento foi:

A) 20%.

B) 80%.

C) 25%.

D) 125%.


#### Extra Dia 4.16 — Exposição simples

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Probabilidade 20% e impacto R$ 50.000 produzem:

A) R$ 10.000.

B) R$ 2.500.

C) R$ 50.020.

D) R$ 250.000.


#### Extra Dia 4.17 — Base percentual reversa

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Após aumento de 25%, custo é 100 mil. Base era:

A) R$ 75 mil.

B) R$ 125 mil.

C) R$ 25 mil.

D) R$ 80 mil.


#### Extra Dia 4.18 — Comparação de riscos

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

A: 10%×100 mil; B: 40%×20 mil. Pelo valor esperado:

A) A vale 1 mil e B vale 80 mil; B é maior.

B) A vale 10 mil e B vale 8 mil; A é maior.

C) B deve ser priorizado porque sua probabilidade isolada é maior.

D) A e B têm a mesma exposição após ponderar probabilidade e impacto.


#### Extra Dia 4.19 — Implicação e percentual

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Se risco ocorrer, custo cresce 25%. O risco ocorreu e base era 80 mil. Conclui-se:

A) novo custo de 100 mil.

B) custo de 20 mil.

C) nada pode ser concluído.

D) custo de 60 mil.


#### Extra Dia 4.20 — Cálculo e limite

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

Riscos: 20%×50 mil e 10%×30 mil. Avalie.

A) Exposições de R$ 70 mil; a soma dos impactos define a prioridade.

B) Exposições de R$ 10 mil e R$ 30 mil; a maior probabilidade define a prioridade.

C) Exposições de R$ 10 mil e R$ 3 mil; o cálculo não substitui análise qualitativa.

D) Exposições de R$ 50 mil e R$ 30 mil; esses valores ocorrerão com certeza.


## Gabarito - Dia 4

### Principais

| S4D4Q151 | S4D4Q152 | S4D4Q153 | S4D4Q154 | S4D4Q155 | S4D4Q156 | S4D4Q157 | S4D4Q158 | S4D4Q159 | S4D4Q160 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | B | C | D | B | D | A | C | C | A |

| S4D4Q161 | S4D4Q162 | S4D4Q163 | S4D4Q164 | S4D4Q165 | S4D4Q166 | S4D4Q167 | S4D4Q168 | S4D4Q169 | S4D4Q170 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | A | C | B | D | D | B | C | A |

| S4D4Q171 | S4D4Q172 | S4D4Q173 | S4D4Q174 | S4D4Q175 | S4D4Q176 | S4D4Q177 | S4D4Q178 | S4D4Q179 | S4D4Q180 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | B | A | C | B | B | D | B |

| S4D4Q181 | S4D4Q182 | S4D4Q183 | S4D4Q184 | S4D4Q185 | S4D4Q186 | S4D4Q187 | S4D4Q188 | S4D4Q189 | S4D4Q190 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | B | D | A | C | C | D | A | A |

| S4D4Q191 | S4D4Q192 | S4D4Q193 | S4D4Q194 | S4D4Q195 | S4D4Q196 | S4D4Q197 | S4D4Q198 | S4D4Q199 | S4D4Q200 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | A | B | D | C | B | C |

### Extras

| 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 4.6 | 4.7 | 4.8 | 4.9 | 4.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | B | D | D | B | C | A | B | D |

| 4.11 | 4.12 | 4.13 | 4.14 | 4.15 | 4.16 | 4.17 | 4.18 | 4.19 | 4.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | C | A | D | B | A | C |

## Comentários - Dia 4

### Comentário S4D4Q151

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra produção, qualidade, mudança e evidência.
- **B)** Incorreta. Engenharia não se concentra apenas na produção e aprovação de modelos.
- **C)** Incorreta. Automação não transforma requisito informal em produto validado sem trabalho humano.
- **D)** Incorreta. Engenharia administra mudanças; não se define por impedi-las.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q152

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Presença dos participantes não registra a decisão de validação.
- **B)** Correta. Documenta o resultado da validação.
- **C)** Incorreta. Duração da reunião não é o resultado da validação.
- **D)** Incorreta. Histórico da ferramenta não substitui a decisão sobre o requisito.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q153

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte orientação do método e registro da ferramenta.
- **B)** Incorreta. Ferramenta não decide sozinha as atividades necessárias.
- **C)** Correta. Os papéis são complementares.
- **D)** Incorreta. Método e ferramenta apoiam a execução; não são produtos do processo por definição.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q154

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Mudança simples ainda precisa de versionamento mínimo.
- **B)** Incorreta. Prazo urgente não torna aceitável reduzir controle de integração crítica.
- **C)** Incorreta. Proporcionalidade por risco é compatível com auditoria quando produz evidência adequada.
- **D)** Correta. Adapta disciplina sem removê-la.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q155

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Lista de participantes não informa qual decisão foi tomada.
- **B)** Correta. Sem ela não se sabe o que foi aceito.
- **C)** Incorreta. Nova reunião sem interessados não cria a evidência ausente.
- **D)** Incorreta. Ferramenta diferente não substitui decisão humana rastreável.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q156

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Volume sem vínculo entre decisão e versão não garante rastreabilidade.
- **B)** Incorreta. Mudanças críticas exigem mais evidência proporcional, não menos.
- **C)** Incorreta. Controle idêntico sem classificar risco ignora a adaptação proporcional.
- **D)** Correta. Oferece proporcionalidade e auditabilidade.

**Conceito:** Engenharia de software e processo.

**Pegadinha:** Confundir disciplina proporcional com burocracia ou ausência de processo.

**Como pensar:** Separe atividade, método, ferramenta, produto e evidência; depois avalie o risco.

**Referência à apostila de estudo:** [Fundamentos de engenharia de software](semana_04_estudo.md#s4-d4-engenharia).


### Comentário S4D4Q157

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Progressão organizada é seu traço central.
- **B)** Incorreta. Ciclos guiados por riscos caracterizam a espiral.
- **C)** Incorreta. Entregas funcionais sucessivas caracterizam desenvolvimento incremental.
- **D)** Incorreta. Composição com ativos avaliados caracteriza desenvolvimento baseado em reuso.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q158

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Contraria a espiral.
- **B)** Incorreta. Ferramenta não define modelo.
- **C)** Correta. Risco orienta objetivo e próximo passo.
- **D)** Incorreta. Há avaliação por ciclo.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q159

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Adequação funcional isolada não elimina custos de adaptação.
- **B)** Incorreta. Preço e prazo não transferem ao fornecedor todo o risco.
- **C)** Correta. Reuso é decisão técnica e econômica.
- **D)** Incorreta. Compatibilidade técnica isolada ignora suporte e dependência futura.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q160

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Preserva conhecimento sem promover atalhos.
- **B)** Incorreta. Evoluir atalhos não avaliados transforma dívida exploratória em risco de produto.
- **C)** Incorreta. Aceite de navegação não torna o protótipo incremento produtivo.
- **D)** Incorreta. Colocar solução frágil em produção não é condição para obter novo feedback.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q161

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Validação da interface não torna aceitável conservar todos os atalhos.
- **B)** Incorreta. Código destinado à produção precisa considerar qualidade não funcional desde cedo.
- **C)** Incorreta. Depois da decisão de mantê-lo, tratá-lo como descartável orienta controles inadequados.
- **D)** Correta. O código mantido precisa ser sustentável.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q162

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Acoplamento, tecnologia inédita e feedback esporádico não sustentam RAD.
- **B)** Correta. Condições sustentam rapidez com feedback.
- **C)** Incorreta. Escopo amplo e decisões indisponíveis impedem ciclos rápidos controlados.
- **D)** Incorreta. Criticidade integrada e especialistas indisponíveis elevam risco para adoção direta de RAD.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q163

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Entendimento e solução evoluem.
- **B)** Incorreta. Fechar solução antes da primeira versão contraria a evolução por feedback.
- **C)** Incorreta. Uso exclusivo de ativos existentes caracteriza reuso, não evolução.
- **D)** Incorreta. Protótipo descartável com requisitos estáveis não descreve amadurecimento do produto.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q164

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Reorganização interna sem nova função não agrega capacidade utilizável.
- **B)** Incorreta. Melhoria interna de desempenho, no cenário, não adiciona função ao produto.
- **C)** Correta. Amplia capacidade utilizável.
- **D)** Incorreta. Reexecutar testes é verificação, não nova capacidade.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q165

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A alternativa inverte refinamento iterativo e acréscimo incremental.
- **B)** Correta. São conceitos independentes.
- **C)** Incorreta. Repetição de entrega não torna os dois conceitos sinônimos.
- **D)** Incorreta. Iteração não se limita à análise nem incremento exclusivamente à construção.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q166

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Tecnologia conhecida reduz a justificativa para experimento orientado a risco como eixo.
- **B)** Incorreta. Protótipo descartável não deve ser promovido a produto apenas pelo fluxo aprovado.
- **C)** Incorreta. RAD exige participação e decisões rápidas dos usuários.
- **D)** Correta. As condições favorecem sequência planejada.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q167

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Adiar prova técnica conserva o risco dominante.
- **B)** Incorreta. Disponibilidade do primeiro componente não prova adequação.
- **C)** Incorreta. Entrega incremental não reduz, sozinha, o risco técnico adiado.
- **D)** Correta. Risco define objetivos.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q168

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Aprovar descrição incompleta antes das telas preserva a incerteza.
- **B)** Correta. Torna feedback concreto.
- **C)** Incorreta. Excluir usuários até a implantação adia a aprendizagem necessária.
- **D)** Incorreta. Build automatizado não elicita fluxo desconhecido.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q169

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Licença gratuita não neutraliza adaptação, infraestrutura e suporte.
- **B)** Incorreta. Tempo de procura isolado não representa o custo total futuro.
- **C)** Correta. Custos indiretos podem dominar.
- **D)** Incorreta. Quantidade de funções não resolve incompatibilidade de infraestrutura e suporte.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q170

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Velocidade não permite dispensar arquitetura e aceite.
- **B)** Correta. A espiral organiza ciclos em torno da identificação e redução de riscos.
- **C)** Correta. Desenvolvimento incremental amplia a capacidade em partes utilizáveis.
- **D)** Correta. Prototipação pode tornar requisitos incertos concretos para aprendizagem.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque estabilidade, risco dominante, aprendizagem e possibilidade de incremento.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q171

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Deixar integração e aceite para o final remove feedback e evidência frequentes.
- **B)** Incorreta. Escopo ilimitado elimina o recorte que favorece RAD.
- **C)** Correta. Rapidez não remove qualidade.
- **D)** Incorreta. Prazo curto não autoriza generalizar o plano a sistema crítico sem análise.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque modularidade, feedback e controles.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q172

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cobertura parcial não resolve críticos.
- **B)** Incorreta. Cobertura de 80% não compensa automaticamente requisitos críticos ausentes.
- **C)** Incorreta. Incompatibilidade pode ser tratável por adaptação economicamente viável.
- **D)** Incorreta. O órgão conserva a responsabilidade de aceitar o resultado.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Combine adequação, restrições e custo/risco.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q173

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Baseline sequencial pode ser alterada pela governança competente.
- **B)** Incorreta. Alterar só o código cria divergência com especificação e testes.
- **C)** Incorreta. Retorno à concepção depende do impacto, não é automático.
- **D)** Correta. Preserva coerência entre fases.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Verifique produtos, restrições e decisão.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q174

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Forma cíclica sem orientação por risco não basta.
- **B)** Correta. O ciclo deve ser dirigido por risco.
- **C)** Incorreta. Repetição sem risco não transforma necessariamente o processo em cascata.
- **D)** Incorreta. Ausência de registro não demonstra redução de riscos.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Diferencie forma circular de finalidade.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q175

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Entrega resultado utilizável.
- **B)** Incorreta. Camada técnica completa, isoladamente, não entrega a função utilizável.
- **C)** Incorreta. Componentes técnicos isolados adiam o valor até a integração final.
- **D)** Incorreta. Tamanho de arquivo não corresponde a capacidade de uso.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque valor, integração mínima e aceite.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q176

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Emissão de documento adiciona nova capacidade.
- **B)** Incorreta. Nova função de consulta entregue é incremento.
- **C)** Correta. Há refinamento sem nova capacidade entregue.
- **D)** Incorreta. Segunda capacidade liberada também é incremento.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Separe refinamento de capacidade entregue.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q177

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não há obrigação de exclusividade de um modelo por todo o ciclo.
- **B)** Correta. Ênfases podem compor abordagem contextual.
- **C)** Incorreta. Protótipo e incremento podem produzir artefatos com papéis compatíveis.
- **D)** Incorreta. Combinação aumenta, não elimina, a necessidade de critérios de passagem.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Verifique finalidade, compatibilidade e governança.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q178

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Dados reais tornam segurança relevante antes da transição.
- **B)** Correta. Código permanente precisa de controles.
- **C)** Incorreta. Código destinado a evoluir não deve ser tratado como descartável até a produção.
- **D)** Incorreta. Usabilidade e confidencialidade são dimensões distintas.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Integre permanência, exposição e qualidade.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q179

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Proibir refatoração preserva dívida e degrada capacidade futura.
- **B)** Incorreta. Adiar integração posterga incompatibilidades entre incrementos.
- **C)** Incorreta. O produto acumulado exige coerência arquitetural comum.
- **D)** Correta. Combina valor e integridade.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Cheque valor, arquitetura e regressão.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q180

**Nível:** Muito difícil

**Uso:** Aprofundamento

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Teste final e estabilização forçada não respondem à mudança nem ao risco alto.
- **B)** Correta. Atende aos quatro condicionantes.
- **C)** Incorreta. RAD sem controle arquitetural atende prazo, mas ignora risco e evolução.
- **D)** Incorreta. Reuso sem ativos avaliados não responde à integração de alto risco.

**Conceito:** Modelos e estratégias de ciclo de vida.

**Pegadinha:** Escolher pelo rótulo sem comparar estabilidade, risco, feedback e entrega.

**Como pensar:** Aplique mudança, valor, risco e feedback.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4D4Q181

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Capacidade integrada e verificada é pergunta de construção.
- **B)** Incorreta. Aptidão no ambiente-alvo é pergunta de transição.
- **C)** Correta. Delimita propósito e viabilidade.
- **D)** Incorreta. Redução de riscos arquiteturais é pergunta de elaboração.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q182

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Reduz incerteza arquitetural.
- **B)** Incorreta. Visão e caso de negócio predominam na concepção.
- **C)** Incorreta. Incrementos integrados e testes predominam na construção.
- **D)** Incorreta. Migração, treinamento e aceite predominam na transição.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q183

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Visão, escopo e viabilidade predominam na concepção.
- **B)** Correta. O produto é desenvolvido e testado.
- **C)** Incorreta. Migração, treinamento e aceite predominam na transição.
- **D)** Incorreta. Arquitetura-base e riscos predominam na elaboração.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q184

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Visão, atores e caso de negócio são evidências de concepção.
- **B)** Incorreta. Arquitetura-base e prova de risco são evidências de elaboração.
- **C)** Incorreta. Código e testes são evidências de construção, não de uso operacional.
- **D)** Correta. Busca aptidão ao uso.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q185

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Atividade não é proibida fora da fase dominante.
- **B)** Incorreta. Restringir todo código à construção transforma ênfase em proibição.
- **C)** Incorreta. As fases possuem finalidades predominantes distintas.
- **D)** Incorreta. Elaboração também pode usar código exploratório para reduzir risco.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Distinga atividade de finalidade predominante.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q186

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Volume documental não substitui evidência sobre arquitetura e risco.
- **B)** Incorreta. Arquitetura e integração crítica devem ser tratadas na elaboração.
- **C)** Correta. O marco reflete a finalidade.
- **D)** Incorreta. Requisitos significativos participam dos produtos da elaboração.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Cheque arquitetura, riscos e plano.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q187

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Pacote no destino não demonstra migração, treinamento e monitoramento.
- **B)** Incorreta. Não é preciso descartar o deployment para completar a transição.
- **C)** Correta. Instalação é apenas parte.
- **D)** Incorreta. Migração e treinamento pertencem à transição, não provam falta de construção.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Separe instalação, prontidão e aceite.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q188

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Gabarito:** D (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. Elaboração enfatiza arquitetura-base e riscos centrais.
- **B)** Correta. Construção implementa, integra e verifica a capacidade planejada.
- **C)** Correta. Transição busca colocar a solução em uso no ambiente-alvo.
- **D)** Incorreta (gabarito). Requisitos podem ser refinados em fases posteriores; concepção indica uma ênfase, não uma exclusividade.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Identifique absoluto que transforma ênfase em proibição.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q189

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Plano sozinho não conclui a última.
- **B)** Incorreta. Prova arquitetural e incrementos testados são resultados observáveis das fases seguintes.
- **C)** Incorreta. Plano de migração sem execução não conclui a transição.
- **D)** Incorreta. Incrementos testados são evidência de construção, e a transição ainda não ocorreu.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Mapeie evidência e diferencie plano de resultado.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q190

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).

**Gabarito:** A (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Incorreta (gabarito). Cópia do artefato não basta para demonstrar prontidão operacional.
- **B)** Correta. Concepção delimita visão, escopo inicial e viabilidade.
- **C)** Correta. Elaboração enfrenta riscos arquiteturais relevantes.
- **D)** Correta. Construção produz e verifica incrementos da solução.

**Observação:** a questão pede a alternativa incorreta; por isso, A é o gabarito.

**Conceito:** Finalidade das fases.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta de outras atividades.

**Como pensar:** Pergunte o que domina: visão, arquitetura/risco, produto integrado ou uso operacional.

**Referência à apostila de estudo:** [Concepção, elaboração, construção e transição](semana_04_estudo.md#s4-d4-fases).


### Comentário S4D4Q191

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Troca iniciação por planejamento, inverte a função das baselines e desloca execução, encerramento e operação.
- **B)** Correta. A autorização inicia; as baselines planejam; entrega e medição coexistem; aceite e transferência encerram; suporte recorrente é operação.
- **C)** Incorreta. A autorização não é execução, e a continuidade do suporte não transforma o esforço temporário em projeto permanente.
- **D)** Incorreta. Mistura fases do processo de desenvolvimento com fases de gerenciamento e elimina indevidamente o controle durante a execução.

**Conceito:** Fases de projeto e distinção entre projeto, processo de desenvolvimento e operação.

**Pegadinha:** Confundir fases de projeto com fases do RUP e tratar execução e controle como compartimentos incompatíveis.

**Como pensar:** Associe cada evidência à sua finalidade: autorizar, planejar, produzir, medir/decidir, aceitar/transferir e operar.

**Referência à apostila de estudo:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).


### Comentário S4D4Q192

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Acompanhamento mede; não aprova, por si, o replanejamento.
- **B)** Incorreta. Medição pertence ao acompanhamento, não ao planejamento.
- **C)** Incorreta. Planejamento define baseline e acompanhamento mede antes do controle.
- **D)** Correta. As funções aparecem com evidência.

**Conceito:** Gerenciamento de projetos.

**Pegadinha:** Confundir medição com controle ou projeto com operação.

**Como pensar:** Localize baseline, dado real e decisão.

**Referência à apostila de estudo:** [Projeto, planejamento, acompanhamento e controle](semana_04_estudo.md#s4-d4-projetos).


### Comentário S4D4Q193

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Respondem a perguntas diferentes.
- **B)** Incorreta. A alternativa inverte decomposição de escopo e ordenação temporal.
- **C)** Incorreta. Distribuição de pessoas não é WBS, e cronograma não define pacotes.
- **D)** Incorreta. Os artefatos respondem a perguntas diferentes, não a níveis da mesma estrutura.

**Conceito:** Escopo, decomposição e restrições.

**Pegadinha:** Usar WBS como cronograma ou tratar mudança isoladamente.

**Como pensar:** Separe o que entregar de quando executar.

**Referência à apostila de estudo:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).


### Comentário S4D4Q194

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Preservar demais baselines ignora impactos cruzados da mudança.
- **B)** Incorreta. Baseline aprovada admite mudança por governança informada.
- **C)** Correta. Mudança atravessa áreas.
- **D)** Incorreta. Alterar apenas escopo e orçamento cria divergência com prazo e qualidade.

**Conceito:** Escopo, decomposição e restrições.

**Pegadinha:** Usar WBS como cronograma ou tratar mudança isoladamente.

**Como pensar:** Aplique trabalho, restrições e riscos.

**Referência à apostila de estudo:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).


### Comentário S4D4Q195

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Conecta tempo, custo, risco e decisão.
- **B)** Incorreta. Ociosidade pode gerar custo e deve entrar na análise integrada.
- **C)** Incorreta. Cobrança sem atualizar baselines posterga o controle do impacto.
- **D)** Incorreta. Remover a dependência do cronograma não remove a dependência real.

**Conceito:** Escopo, decomposição e restrições.

**Pegadinha:** Usar WBS como cronograma ou tratar mudança isoladamente.

**Como pensar:** Causa → dependência → prazo → custo → resposta.

**Referência à apostila de estudo:** [Escopo, WBS/EAP, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).


### Comentário S4D4Q196

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas e comunicação](semana_04_estudo.md#s4-d4-qualidade-pessoas-comunicacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Quantificar ajuda a qualidade, mas a mesma comunicação não atende todos os públicos.
- **B)** Correta. Cria evidência e comunicação útil.
- **C)** Incorreta. “Rápido” continua vago e retirar resultado desfavorável distorce os fatos.
- **D)** Incorreta. Ausência de reclamação não mede desempenho, e painel sem contexto não orienta decisão.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Combine medida, teste, interessado e decisão.

**Referência à apostila de estudo:** [Qualidade, pessoas e comunicação](semana_04_estudo.md#s4-d4-qualidade-pessoas-comunicacao).


### Comentário S4D4Q197

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Esperar a indisponibilidade perde a oportunidade de prevenir impacto.
- **B)** Incorreta. Pessoas sem preparo não garantem competência, e papéis permanecem frágeis.
- **C)** Incorreta. Registro sem resposta não trata a exposição identificada.
- **D)** Correta. Trata probabilidade, capacidade e interessados.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Integre risco, competência, responsável e comunicação.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


### Comentário S4D4Q198

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O órgão mantém responsabilidade por integração e aceite.
- **B)** Incorreta. Definir aceite depois da entrega posterga um critério contratual essencial.
- **C)** Correta. Fornecedor não absorve tudo.
- **D)** Incorreta. Integração deve ser planejada e acompanhada durante o projeto.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Cheque compra, aceite, integração e responsabilidade.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


### Comentário S4D4Q199

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Mantém sem revisão capacidade e comunicação afetadas pela ampliação de usuários.
- **B)** Correta. Todos os efeitos entram.
- **C)** Incorreta. Registrar apenas impactos de data ignora os demais efeitos integrados.
- **D)** Incorreta. Fornecedor e carga exigem análise; não impedem toda mudança automaticamente.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Percorra efeitos e exija baselines coerentes.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


### Comentário S4D4Q200

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Mantém a lacuna de WBS e aceita critério de teste sem limite.
- **B)** Incorreta. Inclui integração na WBS, mas não define limite de aceite nem trata o problema completo.
- **C)** Correta. Corrige os pontos integrados.
- **D)** Incorreta. Risco ocorrido vira problema; não deve ser simplesmente encerrado sem risco residual.

**Conceito:** Integração das áreas de projeto.

**Pegadinha:** Transferir risco, usar comunicação genérica ou aceitar qualidade vaga.

**Como pensar:** Meça, trate, atualize escopo, defina qualidade e controle.

**Referência à apostila de estudo:** [Qualidade, pessoas, comunicação, riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


#### Comentário Extra Dia 4.1

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Princípios convivem.
- **B)** Incorreta. Ganho mensurável não autoriza flexibilizar procedimento aplicável por si só.
- **C)** Incorreta. Resultado útil não supre ausência de competência.
- **D)** Incorreta. Lentidão não transforma automaticamente ato legal em inválido.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.2

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Descentralização e controle não tratam promoção pessoal.
- **B)** Incorreta. Autotutela e revisão de atos não são o princípio violado no caso.
- **C)** Correta. Comunicação institucional não serve à promoção.
- **D)** Incorreta. Especialidade e competência não são o eixo da promoção pessoal.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.3

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Publicidade de ato não torna todo dado pessoal publicável.
- **B)** Correta. Não é absoluta.
- **C)** Incorreta. Proteção de dados e publicidade precisam ser compatibilizadas no caso concreto.
- **D)** Incorreta. Verdade da informação não autoriza promoção pessoal.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.4

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A criação de nova entidade caracteriza descentralização, o que não ocorreu.
- **B)** Incorreta. Não houve delegação a particular.
- **C)** Incorreta. Desconcentração não cria nova pessoa jurídica.
- **D)** Correta. Distribui competências internamente.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.5

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Autarquia não integra a Administração Direta e possui personalidade própria.
- **B)** Incorreta. Autarquia é pessoa jurídica de direito público, não privado.
- **C)** Incorreta. Não integra a Administração Direta nem possui apenas autonomia financeira.
- **D)** Correta. É a classificação revisada.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.6

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Ordem invertida.
- **B)** Correta. Legalidade e mérito distinguem.
- **C)** Incorreta. São organizacionais.
- **D)** Incorreta. Não correspondem.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.7

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Visibilidade do desvio não completa o controle sem decisão.
- **B)** Incorreta. O cenário contém medição; o que falta é decisão de controle.
- **C)** Correta. Informação precisa gerar ação.
- **D)** Incorreta. O desvio foi medido, portanto houve acompanhamento.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.8

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Mantém a mesma pessoa.
- **B)** Incorreta. Não houve outorga a nova entidade.
- **C)** Incorreta. Não houve delegação da execução a outra pessoa.
- **D)** Incorreta. Distribuir atribuições internas não concentra competências.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.9

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Gabarito:** B (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. A eficiência administrativa deve permanecer dentro da legalidade.
- **B)** Incorreta (gabarito). Interesse público do ato não elimina limites à divulgação de dados pessoais.
- **C)** Correta. Impessoalidade veda o uso da atuação institucional para promoção pessoal.
- **D)** Correta. Autarquia integra a Administração Indireta e possui personalidade de direito público.

**Observação:** a questão pede a alternativa incorreta; por isso, B é o gabarito.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.10

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Administração Pública
- **Assunto:** Princípios, organização e controle administrativo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ilegalidade conduz à análise de anulação, não de revogação por mérito.
- **B)** Incorreta. Resultado popular não torna todo vício de competência convalidável.
- **C)** Incorreta. Eficiência e popularidade não prevalecem sobre a legalidade.
- **D)** Correta. Legalidade precede mérito.

**Conceito:** Princípios, organização e controle administrativo.

**Pegadinha:** Transformar princípio em autorização absoluta ou confundir organização e retirada do ato.

**Como pensar:** Identifique legalidade, finalidade, pessoa jurídica e motivo da retirada.

**Referência à apostila de estudo:** [Administração Pública](semana_04_estudo.md#s4-d4-b4-administracao).


#### Comentário Extra Dia 4.11

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Antecedente falso.
- **B)** Correta. É verdadeiro→falso.
- **C)** Incorreta. V→V é verdadeiro.
- **D)** Incorreta. F→F é verdadeiro.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.12

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Recíproca.
- **B)** Incorreta. Inversa.
- **C)** Incorreta. Negação.
- **D)** Correta. Nega e inverte.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.13

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. De Morgan.
- **B)** Incorreta. Exigir ambas as negações é mais forte que negar a conjunção.
- **C)** Incorreta. A disjunção das afirmações positivas não nega a conjunção.
- **D)** Incorreta. A implicação muda o conectivo e não é a negação pedida.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.14

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Mais forte.
- **B)** Incorreta. Não decorre.
- **C)** Correta. Contraexemplo nega universal.
- **D)** Incorreta. Contradiz.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.15

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Usa base final.
- **B)** Incorreta. Confunde base.
- **C)** Correta. 20/80 = 25%.
- **D)** Incorreta. É razão final/base.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.16

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. 0,20×50.000.
- **B)** Incorreta. Multiplicação errada.
- **C)** Incorreta. Soma grandezas.
- **D)** Incorreta. Divisão indevida.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.17

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Subtrai percentual do final.
- **B)** Incorreta. Direção inversa.
- **C)** Incorreta. Confunde percentual e base.
- **D)** Correta. 100/1,25=80.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.18

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Os produtos corretos são 10% de 100 mil = 10 mil e 40% de 20 mil = 8 mil.
- **B)** Correta. As exposições são 10 mil para A e 8 mil para B; portanto, A é maior.
- **C)** Incorreta. A comparação exige probabilidade e impacto, não apenas a probabilidade isolada.
- **D)** Incorreta. As exposições calculadas são diferentes: 10 mil e 8 mil.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.19

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. 80×1,25.
- **B)** Incorreta. É só acréscimo.
- **C)** Incorreta. Antecedente confirmado.
- **D)** Incorreta. Sinal oposto.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


#### Comentário Extra Dia 4.20

- **Dia:** Dia 4
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico-Matemático
- **Assunto:** Lógica, percentuais e exposição de risco
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Soma impactos sem multiplicar pelas probabilidades.
- **B)** Incorreta. O segundo produto correto é R$ 3 mil, e probabilidade isolada não define prioridade.
- **C)** Correta. Produtos e limite corretos.
- **D)** Incorreta. Usa impactos como exposições e transforma incerteza em certeza.

**Conceito:** Lógica, percentuais e exposição de risco.

**Pegadinha:** Usar base errada ou inverter implicação.

**Como pensar:** Formalize a relação, escolha a base e calcule em etapas.

**Referência à apostila de estudo:** [Raciocínio Lógico-Matemático](semana_04_estudo.md#s4-d4-b4-rlm).


---

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
