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
