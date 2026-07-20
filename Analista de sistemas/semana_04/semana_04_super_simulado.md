# Super Simulado — Semana 4

**Status:** **Material aprovado para execução**; execução do candidato pendente.

**Finalidade:** 60 questões autorais e inéditas sobre requisitos, UML, componentes, engenharia de software, testes, qualidade, manutenção, integração e recursos informacionais. A forma foi calibrada pelo perfil documentado do Instituto Consulplan; nenhum item reproduz questão oficial ou questão do banco semanal.

**Aplicação sugerida:** 2h30 sem consulta, em bloco contínuo. Marque resposta e confiança de 0 a 3. Faça a correção integral A–D em sessão posterior e retorne às referências indicadas.

**Matriz revisada:** 40 Médias, 16 Difíceis e 4 Muito difíceis. Os rótulos refletem a cadeia de raciocínio efetivamente exigida após auditoria semântica independente.

## Cobertura por dia-base

| Dia-base | Conteúdo predominante | Questões |
|---:|---|---|
| 1 | Requisitos, análise OO e casos de uso | S4S001–S4S010 |
| 2 | UML estrutural e comportamental | S4S011–S4S020 |
| 3 | Componentes, deployment e ferramentas | S4S021–S4S030 |
| 4 | Ciclos de vida e projetos | S4S031–S4S040 |
| 5 | Testes, qualidade e manutenção | S4S041–S4S050 |
| 6 | Integração, ITIL/COBIT e recursos informacionais | S4S051–S4S060 |

## Questões — Dia-base 1

### S4S001 — Função e qualidade

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

“O portal emitirá certidão” e “95% das emissões terminarão em até 2 s” são, respectivamente:

A) requisito funcional e requisito não funcional mensurável.

B) duas regras de negócio com a mesma finalidade.

C) duas soluções de interface sem requisito associado.

D) requisito não funcional e requisito funcional.


### S4S002 — Critério verificável

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Qualidade e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

Qual redação permite aceite objetivo?

A) Em dias úteis, o portal deverá responder rapidamente às consultas recebidas.

B) A solução usará tecnologia moderna para oferecer desempenho satisfatório aos usuários.

C) Sob 200 usuários simultâneos, 95% das consultas responderão em até 2 s.

D) As consultas serão eficientes sempre que a rede e o servidor colaborarem.


### S4S003 — Necessidade antes da solução

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Necessidade, requisito, regra e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

O setor relata demora e pede “comprar chatbot”. A primeira ação de análise é:

A) registrar chatbot como requisito obrigatório sem validar o problema.

B) investigar a necessidade e as causas antes de fixar a solução tecnológica.

C) excluir o setor da validação porque já indicou uma tecnologia.

D) tratar a demora apenas como requisito de interface gráfica.


### S4S004 — Técnica de elicitação

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Elicitação](semana_04_estudo.md#s4-d1-elicitacao).

Usuários executam atalhos tácitos que não conseguem explicar em entrevista. Qual técnica complementa melhor?

A) questionário fechado aplicado sem observar o ambiente.

B) leitura exclusiva do código atual como prova da necessidade.

C) priorização por custo antes de descobrir o procedimento.

D) observação contextual do trabalho seguida de confirmação com os usuários.


### S4S005 — Priorização com dependência

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Análise e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

Requisito A tem alto valor; B tem valor médio, mas é pré-requisito técnico de A. Qual decisão é madura?

A) priorizar A isoladamente porque valor elimina dependências.

B) considerar a dependência e planejar B antes ou junto de A.

C) descartar B porque não possui o maior valor individual.

D) somar votos sem registrar risco, custo ou precedência.


### S4S006 — Verificação e validação

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

Um requisito é claro e testável, mas descreve regra que o setor competente rejeita. Conclui-se que:

A) falhou apenas na ortografia e deve manter a regra descrita.

B) foi validado porque qualquer requisito testável é correto.

C) não precisa de rastreabilidade, pois a redação está completa.

D) passou pela verificação textual, mas falhou na validação da necessidade.


### S4S007 — Impacto pela rastreabilidade

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Gestão e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

Uma regra muda. Qual percurso oferece análise de impacto mais confiável?

A) requisito sem versão e lista de arquivos baseada em memória.

B) somente casos de teste, presumindo que cobrem todo o escopo.

C) apenas o cronograma, sem identificar entregas afetadas.

D) origem, requisito, modelos, componentes, código e testes vinculados.


### S4S008 — Responsabilidade orientada a objetos

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Análise orientada a objetos](semana_04_estudo.md#s4-d1-oo).

Um “objeto Deus” valida, persiste, notifica e emite relatórios. Qual refatoração conceitual é adequada?

A) distribuir responsabilidades coesas e explicitar colaborações por contratos.

B) duplicar o objeto em cada tela mantendo todas as responsabilidades.

C) transformar cada atributo em ator de caso de uso.

D) remover todas as colaborações para obter independência absoluta.


### S4S009 — Caso de uso e fronteira

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Casos de uso](semana_04_estudo.md#s4-d1-casos-uso).

Cidadão solicita certidão; atendente auxilia; serviço externo valida pagamento. Qual modelagem preserva os papéis?

A) atores ficam fora da fronteira e casos representam objetivos oferecidos pelo sistema.

B) atendente e serviço tornam-se classes internas sem relação com atores.

C) a tela de certidão substitui o objetivo e vira o único ator.

D) todo passo interno vira caso autônomo sem valor para qualquer ator.


### S4S010 — Include, extend e competência

**Dia-base:** 1

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Relações entre casos de uso](semana_04_estudo.md#s4-d1-relacoes-casos) e [Fonte, competência e hierarquia](semana_04_estudo.md#s4-d1-b4).

“Decidir requerimento” sempre executa “Registrar autoria”. Durante “Consultar andamento”, no ponto “oferecer cópia”, “Solicitar cópia integral” é inserido se o interessado autorizado optar. Além disso, a regra deve respeitar a fonte competente. Qual leitura é correta?

A) registrar autoria como extend; solicitar cópia integral como include; fonte da regra rastreada.

B) registrar autoria como include; solicitar cópia integral como extend; fonte da regra rastreada.

C) registrar autoria como include; solicitar cópia integral como extend; competência presumida pela autonomia regional.

D) registrar autoria como include; solicitar cópia integral como generalização; fonte da regra rastreada.


## Questões — Dia-base 2

### S4S011 — Classe e objeto

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Classes e objetos](semana_04_estudo.md#s4-d2-classes-objetos).

No modelo, Profissional define atributos comuns; p123 possui CPF e situação próprios. Eles são:

A) dois objetos sem relação de instanciação.

B) classe e objeto, respectivamente.

C) objeto e classe, respectivamente.

D) dois componentes implantáveis.


### S4S012 — Leitura da multiplicidade

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Associações e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

Unidade 1 — 0..* Profissional significa que:

A) cada Profissional deve pertencer simultaneamente a muitas Unidades.

B) a associação exige ao menos um Profissional por Unidade.

C) a quantidade atual é sempre ilimitada e desconhecida.

D) uma Unidade pode ligar-se a zero ou muitos Profissionais.


### S4S013 — Composição

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Relações estruturais](semana_04_estudo.md#s4-d2-relacoes-estruturais).

Pedido contém Itens que não existem fora dele e são eliminados com o todo. A relação mais expressiva é:

A) composição entre Pedido e Item.

B) dependência transitória entre Item e Pedido.

C) generalização de Pedido por Item.

D) agregação compartilhada sem vínculo de vida.


### S4S014 — Escolha da perspectiva

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [UML, classes e objetos](semana_04_estudo.md#s4-d2-uml).

A equipe quer representar ordem de mensagens durante autenticação. O diagrama principal deve ser:

A) de classes, pois atributos determinam toda ordem de execução.

B) de deployment, pois nós substituem mensagens.

C) de sequência, pois destaca linhas de vida e ordem temporal.

D) de estados, pois qualquer chamada é um estado persistente.


### S4S015 — Fragmento alt

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Fragmentos combinados](semana_04_estudo.md#s4-d2-fragmentos).

Após validar pagamento, o fluxo segue “aprovado” ou “recusado”, de forma exclusiva. Use:

A) fragmento loop sem condição de saída.

B) fragmento opt com dois caminhos simultâneos.

C) fragmento alt com guardas mutuamente exclusivas.

D) composição entre as linhas de vida.


### S4S016 — Ordem na comunicação

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Comunicação](semana_04_estudo.md#s4-d2-comunicacao).

Em diagrama de comunicação, 1:solicitar, 1.1:validar e 1.2:registrar indicam que:

A) validar e registrar detalham mensagens subordinadas à solicitação.

B) as três mensagens são classes em generalização.

C) registrar ocorre antes de solicitar por ter mais dígitos.

D) a ordem é irrelevante porque vínculos bastam.


### S4S017 — Decisão e concorrência

**Dia-base:** 2

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Atividades](semana_04_estudo.md#s4-d2-atividades).

Após triagem, escolhe-se deferir ou indeferir, e os ramos alternativos reconvergem. Em seguida, notificar e arquivar ocorrem em paralelo, e ambas devem terminar antes do encerramento. A notação exige:

A) decision/join para a escolha e fork/merge para a concorrência.

B) decision/merge para a escolha e fork, sem join, para a concorrência.

C) decision sem merge para a escolha e fork/join para a concorrência.

D) decision/merge para a escolha e fork/join para a concorrência.


### S4S018 — Evento, guarda e efeito

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados](semana_04_estudo.md#s4-d2-estados).

Transição cancelar [semPagamento] / liberarVaga contém, respectivamente:

A) guarda, efeito e evento.

B) evento, guarda e efeito.

C) estado, classe e objeto.

D) mensagem, multiplicidade e composição.


### S4S019 — Consistência entre vistas

**Dia-base:** 2

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Consistência entre vistas](semana_04_estudo.md#s4-d6-integracao).

Sequência envia aprovar() a objeto que o diagrama de classes não permite alcançar; atividade prevê ramo ausente no caso de uso. O que fazer?

A) alinhar somente a sequência às classes e manter a divergência entre atividade e caso de uso.

B) alinhar os comportamentos, mas dispensar registro da decisão porque os diagramas são da mesma versão.

C) revisar as inconsistências e justificar ou alinhar relações e comportamentos.

D) adicionar a relação estrutural e remover o ramo automaticamente, sem consultar a regra que originou as vistas.


### S4S020 — UML e controle administrativo

**Dia-base:** 2

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Atividades](semana_04_estudo.md#s4-d2-atividades) e [Administração Pública](semana_04_estudo.md#s4-d2-b4).

Um fluxo administrativo possui decisão por competência; dois trabalhos ocorrem em paralelo e ambos devem terminar antes de um ato final sujeito a controle. Qual desenho e leitura são adequados?

A) atividade com guardas, fork sem join antes do ato final e registro da competência e do ato.

B) atividade com guardas e fork/join, registrando o ato, mas presumindo competência em razão da eficiência.

C) atividade com guardas e merge para sincronizar os trabalhos, preservando competência e evidência do ato.

D) atividade com guardas, fork/join e evidência do ato; eficiência não afasta competência.


## Questões — Dia-base 3

### S4S021 — Componente e nó

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Componentes](semana_04_estudo.md#s4-d3-componentes).

Qual distinção é correta?

A) Componente é servidor; nó é interface fornecida.

B) Componente é arquivo; nó é caso de uso.

C) Componente é módulo lógico; nó é recurso de execução.

D) Componente e nó são sinônimos em qualquer perspectiva.


### S4S022 — Fornecedor e consumidor

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Interfaces e portas](semana_04_estudo.md#s4-d3-interfaces).

Cadastro implementa Consulta; Relatórios a utiliza. Logo:

A) Cadastro fornece a interface e Relatórios a requer.

B) Relatórios fornece porque inicia a chamada.

C) Cadastro requer porque recebe a mensagem.

D) ambos manifestam a interface como arquivo.


### S4S023 — Direção da dependência

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dependência e realização](semana_04_estudo.md#s4-d3-dependencias).

A usa serviço de B. A dependência tracejada parte de:

A) B em direção a A, pois B recebe a chamada.

B) ambos, pois toda dependência é bidirecional.

C) um nó em direção a um artefato qualquer.

D) A, cliente dependente, em direção a B, fornecedor.


### S4S024 — Dispositivo, ambiente e artefato

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Deployment](semana_04_estudo.md#s4-d3-deployment).

Servidor físico contém JVM que executa api.jar. A classificação é:

A) componente, interface e nó.

B) dispositivo, ambiente e artefato.

C) artefato, dependência e porta.

D) ator, caso de uso e classe.


### S4S025 — Manifestação e deployment

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos](semana_04_estudo.md#s4-d3-artefatos).

cadastro.jar concretiza Cadastro e roda na JVM. As relações são:

A) deployment com Cadastro e generalização da JVM.

B) realização do servidor e include com a JVM.

C) caminho com Cadastro e composição da JVM.

D) manifestação com Cadastro e deployment na JVM.


### S4S026 — Portas para dois canais

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Interfaces e portas](semana_04_estudo.md#s4-d3-interfaces).

Atendimento recebe API e lote por contratos distintos, mantendo lógica comum. Modele:

A) dois componentes idênticos sem qualquer contrato.

B) duas portas com interfaces próprias no mesmo componente.

C) uma porta TCP usada como componente de negócio.

D) dois nós que realizam automaticamente as interfaces.


### S4S027 — Rastreabilidade por ferramenta

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio](semana_04_estudo.md#s4-d3-ferramentas).

Requisito, commit, build e teste estão desconectados. Priorize:

A) IDs e vínculos versionados entre requisito, commit, build e resultados de teste.

B) IDs ligando requisito e commit, enquanto build e teste ficam identificados apenas por nomes sem versão.

C) modelo reverso ligado ao build, presumindo que a estrutura recuperada representa a necessidade.

D) repositório com versões dos artefatos, mas sem relações entre requisito, build e resultado de teste.


### S4S028 — Engenharia reversa

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio](semana_04_estudo.md#s4-d3-ferramentas).

Uma ferramenta extrai classes do legado. O uso responsável é:

A) arquitetura-alvo aprovada porque o código extraído compila sem erros.

B) baseline estrutural conferida apenas contra o código atual, sem validar decisões com a equipe.

C) baseline estrutural validada com código, equipe e decisões registradas.

D) modelo estrutural revisado pela equipe e usado como substituto dos testes dinâmicos.


### S4S029 — Contrato, artefato e escala

**Dia-base:** 3

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Artefatos](semana_04_estudo.md#s4-d3-artefatos).

Portal requer Consulta; Cadastro a fornece; cadastro.jar roda em dois nós. Uma mudança de contrato exige:

A) rastrear clientes, versionar o build, testar e conferir ambos os deployments.

B) versionar contrato e build, testar apenas Cadastro e replicar o pacote nos dois nós.

C) atualizar Portal e Cadastro, reutilizar o número do build e validar somente um dos nós.

D) rastrear clientes e versionar o build, mas testar o contrato somente após implantar nos dois nós.


### S4S030 — Justificativa técnica sem salto

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português técnico](semana_04_estudo.md#s4-d3-b5-portugues).

Qual frase preserva concessão, referente e limite da evidência?

A) Como o build passou, os dois nós e suas configurações necessariamente estão corretos.

B) Embora o build tenha passado, esse resultado não garante a configuração dos dois nós.

C) O build passou; contudo, isso comprova que toda configuração de implantação está correta.

D) Embora eles tenham passado, isso funciona; portanto, os dois ambientes dispensam validação adicional.


## Questões — Dia-base 4

### S4S031 — Ênfase da cascata

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Sobre os modelos de ciclo de vida, assinale a alternativa **INCORRETA**.

A) A espiral organiza ciclos orientados à identificação e redução de riscos.

B) O desenvolvimento por reuso avalia e integra ativos já existentes.

C) A prototipação pode antecipar aprendizagem sobre requisitos incertos.

D) A cascata proíbe qualquer retorno ou controle de mudança após uma fase.


### S4S032 — Espiral orientada a risco

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Integração inédita domina a incerteza. A espiral recomenda:

A) adiar toda prova até o fim da construção.

B) analisar risco, experimentar, avaliar e planejar a próxima volta.

C) entregar camadas técnicas sem testar a integração.

D) fixar solução de reuso sem avaliar compatibilidade.


### S4S033 — Protótipo descartável

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Protótipo com dados fixos validou navegação, mas não possui segurança. Deve-se:

A) promover o código porque a tela agradou aos usuários.

B) chamá-lo de incremento pronto para produção.

C) preservar o aprendizado e reimplementar a solução produtiva.

D) impedir feedback para evitar mudança de escopo.


### S4S034 — Iteração e incremento

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Assinale a distinção correta.

A) Iteração refina; incremento acrescenta capacidade utilizável.

B) Toda iteração entrega obrigatoriamente função nova.

C) Incremento é repetição sem alteração do produto.

D) Ambos são fases físicas de deployment.


### S4S035 — Reuso com custo total

**Dia-base:** 4

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

Componente gratuito exige adaptação, infraestrutura e suporte. A decisão deve:

A) comparar adequação, integração, dependência, testes e custo total.

B) comparar licença e adaptação, tratando infraestrutura e suporte como irrelevantes para a decisão.

C) avaliar função e custo inicial, adiando testes de integração e dependência para depois da adoção.

D) contratar suporte do fornecedor e considerar transferidos os riscos de integração e resultado.


### S4S036 — Marco da elaboração

**Dia-base:** 4

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Fases do desenvolvimento](semana_04_estudo.md#s4-d4-fases).

Há requisitos extensos, mas arquitetura e integração crítica seguem incertas. Conclui-se que:

A) iniciar construção porque os requisitos extensos bastam como baseline, tratando os riscos arquiteturais nas primeiras versões.

B) iniciar transição para validar a integração crítica com usuários no ambiente operacional.

C) a elaboração ainda precisa tratar arquitetura e riscos centrais.

D) retornar à concepção até eliminar toda incerteza de requisito, adiando a definição da arquitetura.


### S4S037 — Acompanhar e controlar

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Gerenciamento de projetos](semana_04_estudo.md#s4-d4-projetos).

Painel mostra atraso; ninguém decide ação. Houve:

A) controle completo porque o indicador ficou vermelho.

B) somente planejamento, pois dado real não é acompanhamento.

C) acompanhamento, mas não controle completo do desvio.

D) encerramento, porque a data planejada foi ultrapassada.


### S4S038 — WBS e cronograma

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Escopo, WBS, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

Qual distinção é correta?

A) WBS lista apenas datas; cronograma define todo o escopo.

B) ambos são organogramas dos responsáveis.

C) WBS elimina a necessidade de controlar mudanças.

D) WBS decompõe entregas; cronograma ordena atividades no tempo.


### S4S039 — Mudança integrada

**Dia-base:** 4

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

Novo módulo amplia usuários, carga e fornecedor, mas pedem manter todas as referências. Antes de decidir, deve-se:

A) atualizar escopo e cronograma e deixar custo, risco e aquisição para controle posterior.

B) avaliar WBS, prazo, custo, qualidade, comunicação, risco e aquisição.

C) avaliar custo e risco e aprovar antes de analisar impactos em qualidade, comunicação e aquisição.

D) avaliar todos os impactos e rejeitar a mudança apenas porque existe uma baseline aprovada.


### S4S040 — Risco esperado e decisão

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [RLM aplicado a projetos](semana_04_estudo.md#s4-d4-b4-rlm).

Risco A: 20% de R$ 50 mil; B: 40% de R$ 20 mil. Pelo valor esperado simples:

A) A vale R$ 2,5 mil e B R$ 80 mil; B ocorrerá.

B) B é maior só porque tem probabilidade maior.

C) ambos valem R$ 70 mil pela soma dos impactos.

D) A vale R$ 10 mil; B, R$ 8 mil; não há certeza.


## Questões — Dia-base 5

### S4S041 — Erro, defeito e falha

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

Um analista entende mal a regra, codifica condição errada e o sistema rejeita pedido válido. Temos:

A) erro humano, defeito no código e falha observada.

B) falha humana, teste no código e erro do usuário.

C) defeito humano, falha latente e requisito executável.

D) somente falha, pois erro e defeito são sinônimos.


### S4S042 — Teste estático e dinâmico

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

Ao comparar uma revisão documental com um teste que executa o sistema, qual par está correto?

A) ambas são dinâmicas porque envolvem pessoas.

B) ambas são estáticas porque seguem um roteiro.

C) revisão é dinâmica; teste executado é estático.

D) revisão é estática; execução do sistema é dinâmica.


### S4S043 — Níveis de teste

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

Verificar colaboração entre Cadastro e Cobrança, depois validar fluxo completo com usuário, corresponde a:

A) teste unitário e análise estática.

B) teste de sistema e teste de componente isolado.

C) teste de integração e teste de aceitação.

D) regressão e manutenção adaptativa.


### S4S044 — Caixa-preta e caixa-branca

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

Partições de equivalência e cobertura de ramos são, respectivamente:

A) duas técnicas de caixa-branca.

B) caixa-preta e caixa-branca.

C) duas técnicas de caixa-preta.

D) níveis de integração e aceitação.


### S4S045 — Reteste e regressão

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

Após corrigir cálculo de taxa, a equipe executa o caso que falhou e também fluxos vizinhos. Isso é:

A) somente aceitação, porque todo teste após mudança é aceitação.

B) reteste da correção e regressão sobre áreas potencialmente afetadas.

C) apenas teste estático, pois a regra já foi revisada.

D) manutenção preventiva sem qualquer verificação dinâmica.


### S4S046 — Verificação e validação

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Qualidade](semana_04_estudo.md#s4-d5-qualidade).

“Construímos conforme a especificação?” e “construímos o produto necessário?” referem-se a:

A) verificação e validação, respectivamente.

B) validação e verificação, respectivamente.

C) controle e aquisição, respectivamente.

D) teste unitário e manutenção, respectivamente.


### S4S047 — Produto e processo

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Qualidade](semana_04_estudo.md#s4-d5-qualidade).

Qual afirmação é correta?

A) garantia é apenas inspeção final do executável.

B) controle elimina necessidade de critérios mensuráveis.

C) qualidade equivale à ausência de reclamação registrada.

D) garantia atua no processo; controle examina resultados e produto.


### S4S048 — Categoria de manutenção

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Manutenção](semana_04_estudo.md#s4-d5-manutencao).

Alterar o sistema para nova versão obrigatória do SGBD, sem mudar a função de negócio, é manutenção:

A) corretiva.

B) perfectiva.

C) adaptativa.

D) preventiva.


### S4S049 — Mudança segura e fases

**Dia-base:** 5

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

Defeito surge após alteração de regra. Qual fluxo é mais completo?

A) rastrear requisito/impacto, corrigir modelos, testar e implantar sob controle.

B) rastrear o requisito, corrigir o código, executar somente o caso que falhou e implantar.

C) corrigir requisito e teste, manter modelos e código até a próxima versão e liberar sob exceção.

D) corrigir modelos e código, executar regressão e implantar sem registrar origem e análise de impacto.


### S4S050 — Teste, qualidade e fonte normativa

**Dia-base:** 5

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao) e [Testes de software](semana_04_estudo.md#s4-d5-testes).

Uma regra legal muda; o órgão pretende alterar só o código e manter requisito e testes. Qual decisão é correta?

A) confirmar a fonte e atualizar código e testes, mantendo o requisito por já existir baseline aprovada.

B) confirmar a fonte, atualizar requisito e código e executar apenas o reteste da regra alterada.

C) confirmar a fonte competente, atualizar a cadeia e executar reteste e regressão.

D) confirmar a fonte e atualizar toda a cadeia, publicando antes de executar reteste e regressão.


## Questões — Dia-base 6

### S4S051 — Cadeia mínima

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao).

Qual cadeia oferece rastreabilidade de ponta a ponta?

A) necessidade → servidor → custo → implantação, sem requisitos, modelos ou testes.

B) modelo → e-mail → implantação → mudança, sem versão ou origem rastreável.

C) necessidade → requisito → modelo → componente → código → teste → mudança.

D) código → usuário → aceite automático, sem requisito, modelo ou evidência de teste.


### S4S052 — Consistência entre vistas

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao).

Caso exige pagamento opcional; sequência o trata obrigatório; teste cobre apenas obrigatório. A ação correta é:

A) aceitar divergência porque cada vista possui verdade independente.

B) decidir a regra e alinhar caso, interação e teste versionados.

C) apagar o teste e manter as duas regras incompatíveis.

D) trocar o nó de execução para corrigir a semântica.


### S4S053 — Valor em ITIL

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

No recorte estudado, gestão de serviço orienta-se a:

A) produzir documentos sem relação com resultados.

B) substituir governança por ferramenta de chamados.

C) eliminar toda participação do usuário na avaliação.

D) cocriar valor por serviços que apoiam resultados desejados.


### S4S054 — COBIT e governança

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Qual afirmação é adequada?

A) governança avalia, direciona e monitora; gestão planeja e executa atividades.

B) governança executa todo chamado e gestão define apenas estratégia.

C) COBIT é um ERP obrigatório para qualquer órgão.

D) governança e gestão são sinônimos sem separação de responsabilidades.


### S4S055 — ITIL e COBIT

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

Sobre ITIL e COBIT, assinale a alternativa **INCORRETA**.

A) ITIL oferece orientação para gestão de serviços e cocriação de valor.

B) COBIT estrutura governança e gestão de informação e tecnologia.

C) ITIL e COBIT podem complementar-se em escopos distintos.

D) ITIL e COBIT são ferramentas concorrentes de chamados com escopo equivalente.


### S4S056 — Finalidade do GED

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

O problema é controlar versões, metadados, acesso e recuperação de documentos digitais. Priorize:

A) CRM.

B) ERP.

C) GED.

D) BPM.


### S4S057 — Workflow e BPM

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Qual distinção é correta?

A) workflow automatiza tarefas; BPM gerencia processos ponta a ponta.

B) workflow define governança de TI; BPM armazena apenas PDFs.

C) workflow e BPM são sempre sinônimos de ERP.

D) BPM elimina pessoas; workflow dispensa regras.


### S4S058 — ERP e CRM

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Integrar finanças, compras e estoque; depois gerir histórico de atendimento externo corresponde a:

A) CRM e GED, respectivamente.

B) ERP e CRM, respectivamente.

C) BPM e ERP, respectivamente.

D) GED e workflow, respectivamente.


### S4S059 — Escolha integrada de recursos

**Dia-base:** 6

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

Processo de fiscalização possui documentos versionados, tarefas entre áreas e visão ponta a ponta. A combinação coerente é:

A) GED para documentos, workflow para tarefas e ERP para modelar o processo ponta a ponta.

B) GED para documentos, workflow para tarefas e BPM para o processo.

C) GED para documentos, BPM para tarefas locais e workflow para gestão ponta a ponta.

D) ERP para documentos, workflow para tarefas e BPM para o processo ponta a ponta.


### S4S060 — Integração, governança e conclusão

**Dia-base:** 6

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao) e [Português](semana_04_estudo.md#s4-d6-portugues).

Mudança de regra afeta caso, componente, serviço e processo. Qual conclusão técnica é mais defensável?

A) Atualizar requisito, caso e componente e, após um teste funcional aprovado, declarar valor sem verificar processo e controles.

B) Alinhar as vistas e o processo, mas manter os testes anteriores porque a alteração não mudou a interface.

C) A cadeia deve ser atualizada, testada e governada antes de declarar valor e conformidade.

D) Aplicar controles de ITIL/COBIT e registrar a mudança, sem atualizar código e testes rastreados.


## Gabarito

| S4S001 | S4S002 | S4S003 | S4S004 | S4S005 | S4S006 | S4S007 | S4S008 | S4S009 | S4S010 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | B | D | B | D | D | A | A | B |

| S4S011 | S4S012 | S4S013 | S4S014 | S4S015 | S4S016 | S4S017 | S4S018 | S4S019 | S4S020 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | C | A | D | B | C | D |

| S4S021 | S4S022 | S4S023 | S4S024 | S4S025 | S4S026 | S4S027 | S4S028 | S4S029 | S4S030 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | B | D | B | A | C | A | B |

| S4S031 | S4S032 | S4S033 | S4S034 | S4S035 | S4S036 | S4S037 | S4S038 | S4S039 | S4S040 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | C | A | A | C | C | D | B | D |

| S4S041 | S4S042 | S4S043 | S4S044 | S4S045 | S4S046 | S4S047 | S4S048 | S4S049 | S4S050 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | D | C | B | B | A | D | C | A | C |

| S4S051 | S4S052 | S4S053 | S4S054 | S4S055 | S4S056 | S4S057 | S4S058 | S4S059 | S4S060 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | B | D | A | D | C | A | B | B | C |

## Comentários

### Comentário S4S001

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O primeiro define serviço; o segundo, desempenho verificável.
- **B)** Incorreta. A segunda mede qualidade técnica, não regra do domínio.
- **C)** Incorreta. Ambas expressam resultados exigidos do sistema.
- **D)** Incorreta. A classificação ficaria invertida.

**Conceito:** Tipos de requisitos.

**Pegadinha:** Trocar função do sistema por atributo de qualidade.

**Como pensar:** Classifique quem precisa, o que o sistema faz e sob qual qualidade.

**Referência à apostila de estudo:** [Tipos e níveis de requisitos](semana_04_estudo.md#s4-d1-tipos-requisitos).


### Comentário S4S002

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Qualidade e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. “Rapidamente” não possui medida; “em dias úteis” apenas delimita o calendário.
- **B)** Incorreta. Tecnologia e bom são vagos e não definem aceite.
- **C)** Correta. Carga, operação, proporção de respostas e limiar tornam o requisito testável.
- **D)** Incorreta. Eficiente e colaborar não estabelecem condição reproduzível.

**Conceito:** Qualidade do requisito.

**Pegadinha:** Aceitar adjetivo sem medida como critério verificável.

**Como pensar:** Procure condição, medida, limiar e forma de aceite.

**Referência à apostila de estudo:** [Qualidade e verificabilidade](semana_04_estudo.md#s4-d1-qualidade-requisitos).


### Comentário S4S003

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Necessidade, requisito, regra e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Converte proposta em necessidade sem análise.
- **B)** Correta. A solução sugerida pode não tratar o problema real.
- **C)** Incorreta. A fonte continua necessária para compreender o contexto.
- **D)** Incorreta. A causa e o resultado desejado ainda são desconhecidos.

**Conceito:** Requisitos e solução.

**Pegadinha:** Confundir necessidade com implementação antecipada.

**Como pensar:** Separe problema, regra, restrição e solução proposta.

**Referência à apostila de estudo:** [Necessidade, requisito, regra e solução](semana_04_estudo.md#s4-d1-conceitos-requisitos).


### Comentário S4S004

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Elicitação](semana_04_estudo.md#s4-d1-elicitacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Respostas pré-definidas podem ocultar os atalhos.
- **B)** Incorreta. Código mostra implementação, não toda a intenção.
- **C)** Incorreta. Ainda falta compreender o trabalho.
- **D)** Correta. A prática real torna o conhecimento tácito observável.

**Conceito:** Elicitação de requisitos.

**Pegadinha:** Escolher técnica sem considerar fonte e incerteza.

**Como pensar:** Identifique informação faltante e selecione técnica capaz de obtê-la.

**Referência à apostila de estudo:** [Elicitação](semana_04_estudo.md#s4-d1-elicitacao).


### Comentário S4S005

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Análise e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A entrega pode tornar-se inviável sem B.
- **B)** Correta. Valor e ordem técnica precisam ser analisados em conjunto.
- **C)** Incorreta. Seu valor habilitador foi ignorado.
- **D)** Incorreta. Popularidade sozinha não resolve o encadeamento.

**Conceito:** Análise e priorização.

**Pegadinha:** Priorizar apenas por pressão, ignorando valor, risco e dependência.

**Como pensar:** Compare valor, risco, dependência, custo e urgência legítima.

**Referência à apostila de estudo:** [Análise e priorização](semana_04_estudo.md#s4-d1-analise-priorizacao).


### Comentário S4S006

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O problema é aderência, não forma.
- **B)** Incorreta. Testabilidade não substitui aceite autorizado.
- **C)** Incorreta. Origem e decisão ainda precisam ser registradas.
- **D)** Correta. Qualidade formal não garante correção para o interessado.

**Conceito:** Verificação e validação de requisitos.

**Pegadinha:** Confundir texto bem formado com necessidade correta.

**Como pensar:** Primeiro verifique qualidade interna; depois valide com a fonte autorizada.

**Referência à apostila de estudo:** [Especificação e validação](semana_04_estudo.md#s4-d1-especificacao-validacao).


### Comentário S4S007

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Gestão e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Faltam histórico e vínculos verificáveis.
- **B)** Incorreta. Não se confirma origem, modelo ou implementação.
- **C)** Incorreta. Datas não mostram a cadeia técnica.
- **D)** Correta. A cadeia cobre intenção, projeto, implementação e verificação.

**Conceito:** Rastreabilidade de requisitos.

**Pegadinha:** Registrar vínculo sem versão, direção ou uso na análise de impacto.

**Como pensar:** Percorra origem, requisito, modelo, implementação, teste e mudança.

**Referência à apostila de estudo:** [Gestão e rastreabilidade](semana_04_estudo.md#s4-d1-gestao-rastreabilidade).


### Comentário S4S008

**Dia-base:** 1

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Análise orientada a objetos](semana_04_estudo.md#s4-d1-oo).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Reduz acoplamento sem apagar as integrações necessárias.
- **B)** Incorreta. Replica o acoplamento e a inconsistência.
- **C)** Incorreta. Atores representam papéis externos, não dados internos.
- **D)** Incorreta. O sistema precisa cooperar para cumprir objetivos.

**Conceito:** Responsabilidade orientada a objetos.

**Pegadinha:** Criar classe por substantivo sem responsabilidade coerente.

**Como pensar:** Distribua responsabilidades e colaborações antes de escolher estrutura.

**Referência à apostila de estudo:** [Análise orientada a objetos](semana_04_estudo.md#s4-d1-oo).


### Comentário S4S009

**Dia-base:** 1

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Casos de uso](semana_04_estudo.md#s4-d1-casos-uso).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Atores interagem; o sistema contém seus comportamentos observáveis.
- **B)** Incorreta. Papéis externos foram apagados indevidamente.
- **C)** Incorreta. Tela é solução, não papel externo.
- **D)** Incorreta. Fragmenta o objetivo e perde a perspectiva externa.

**Conceito:** Atores, fronteira e objetivo.

**Pegadinha:** Tratar tela ou módulo interno como objetivo do ator.

**Como pensar:** Aplique três filtros: papel externo, fronteira e objetivo observável.

**Referência à apostila de estudo:** [Casos de uso](semana_04_estudo.md#s4-d1-casos-uso).


### Comentário S4S010

**Dia-base:** 1

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Relações entre casos de uso](semana_04_estudo.md#s4-d1-relacoes-casos) e [Fonte, competência e hierarquia](semana_04_estudo.md#s4-d1-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Inverte as relações: o reuso obrigatório é include, e a inserção opcional no ponto indicado é extend.
- **B)** Correta. Reuso obrigatório, inserção condicional em ponto de extensão e origem normativa são tratados separadamente.
- **C)** Incorreta. Acerta as relações UML, mas autonomia regional não cria nem presume competência normativa.
- **D)** Incorreta. Acerta o include e a fonte, porém opção condicionada em ponto de extensão não é generalização.

**Conceito:** Include, extend e generalização.

**Pegadinha:** Usar include e extend apenas para ordenar passos.

**Como pensar:** Verifique reuso obrigatório, autonomia do caso base, ponto/condição de extensão e fonte competente.

**Referência à apostila de estudo:** [Relações entre casos de uso](semana_04_estudo.md#s4-d1-relacoes-casos) e [Fonte, competência e hierarquia](semana_04_estudo.md#s4-d1-b4).


### Comentário S4S011

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Classes e objetos](semana_04_estudo.md#s4-d2-classes-objetos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Profissional funciona como definição compartilhada.
- **B)** Correta. A classe define; p123 é ocorrência identificável com estado.
- **C)** Incorreta. A ordem ficaria invertida.
- **D)** Incorreta. Não são módulos de deployment.

**Conceito:** Classe, objeto e instância.

**Pegadinha:** Confundir molde com ocorrência identificável.

**Como pensar:** Separe definição compartilhada de estado de uma instância.

**Referência à apostila de estudo:** [Classes e objetos](semana_04_estudo.md#s4-d2-classes-objetos).


### Comentário S4S012

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Associações e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A leitura do extremo foi invertida.
- **B)** Incorreta. Zero está permitido.
- **C)** Incorreta. Multiplicidade define limite estrutural, não contagem atual.
- **D)** Correta. A multiplicidade no extremo Profissional conta ocorrências por Unidade.

**Conceito:** Associação e multiplicidade.

**Pegadinha:** Ler multiplicidade do lado errado ou como quantidade atual.

**Como pensar:** Leia quantas instâncias daquele extremo podem ligar-se a uma do oposto.

**Referência à apostila de estudo:** [Associações e multiplicidade](semana_04_estudo.md#s4-d2-associacoes).


### Comentário S4S013

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Relações estruturais](semana_04_estudo.md#s4-d2-relacoes-estruturais).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Há propriedade forte e dependência de ciclo de vida.
- **B)** Incorreta. Uso passageiro não expressa propriedade forte.
- **C)** Incorreta. Item não é especialização de Pedido.
- **D)** Incorreta. É mais fraca que a regra descrita.

**Conceito:** Generalização, dependência, agregação e composição.

**Pegadinha:** Usar composição sem dependência forte de ciclo de vida.

**Como pensar:** Compare especialização, uso transitório, todo fraco e todo forte.

**Referência à apostila de estudo:** [Relações estruturais](semana_04_estudo.md#s4-d2-relacoes-estruturais).


### Comentário S4S014

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [UML, classes e objetos](semana_04_estudo.md#s4-d2-uml).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Estrutura estática não mostra a sequência.
- **B)** Incorreta. Topologia não descreve o fluxo temporal.
- **C)** Correta. A pergunta exige interação ordenada.
- **D)** Incorreta. Mensagem e estado não são equivalentes.

**Conceito:** Perspectivas da UML.

**Pegadinha:** Tratar diagrama como sistema executável ou usar visão inadequada.

**Como pensar:** Comece pela pergunta e escolha a perspectiva que a responde.

**Referência à apostila de estudo:** [UML, classes e objetos](semana_04_estudo.md#s4-d2-uml).


### Comentário S4S015

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Fragmentos combinados](semana_04_estudo.md#s4-d2-fragmentos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Loop representa repetição.
- **B)** Incorreta. Opt possui comportamento opcional único.
- **C)** Correta. Alt representa alternativas condicionais.
- **D)** Incorreta. Relação estrutural não controla mensagens.

**Conceito:** Fragmentos alt, opt e loop.

**Pegadinha:** Trocar alternativa exclusiva por repetição ou opcionalidade.

**Como pensar:** Leia operador, guardas e quantidade de operandos.

**Referência à apostila de estudo:** [Fragmentos combinados](semana_04_estudo.md#s4-d2-fragmentos).


### Comentário S4S016

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Comunicação](semana_04_estudo.md#s4-d2-comunicacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A numeração reconstrói a ordem e o aninhamento.
- **B)** Incorreta. Números não definem herança.
- **C)** Incorreta. A leitura hierárquica foi invertida.
- **D)** Incorreta. A numeração é justamente o recurso temporal.

**Conceito:** Diagrama de comunicação.

**Pegadinha:** Ignorar numeração ao reconstruir a ordem.

**Como pensar:** Use vínculos e números hierárquicos das mensagens.

**Referência à apostila de estudo:** [Comunicação](semana_04_estudo.md#s4-d2-comunicacao).


### Comentário S4S017

**Dia-base:** 2

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Atividades](semana_04_estudo.md#s4-d2-atividades).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Join não seleciona alternativa, e merge não sincroniza trabalhos concorrentes.
- **B)** Incorreta. A escolha reconverge corretamente, mas falta o join exigido antes do encerramento.
- **C)** Incorreta. O fork/join atende ao paralelismo, porém os ramos alternativos declarados precisam reconvergir.
- **D)** Correta. Decision/merge tratam escolha e reconvergência; fork/join tratam paralelismo e sincronização.

**Conceito:** Fluxo de atividades.

**Pegadinha:** Confundir decisão/merge com fork/join.

**Como pensar:** Separe escolha, reconvergência de alternativas, abertura do paralelismo e sincronização final.

**Referência à apostila de estudo:** [Atividades](semana_04_estudo.md#s4-d2-atividades).


### Comentário S4S018

**Dia-base:** 2

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Máquinas de estados](semana_04_estudo.md#s4-d2-estados).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A ordem está invertida.
- **B)** Correta. A notação separa gatilho, condição e ação.
- **C)** Incorreta. São categorias diferentes.
- **D)** Incorreta. Não pertencem à transição descrita.

**Conceito:** Estados e transições.

**Pegadinha:** Confundir evento, guarda e efeito.

**Como pensar:** Leia gatilho, condição e ação na ordem semântica.

**Referência à apostila de estudo:** [Máquinas de estados](semana_04_estudo.md#s4-d2-estados).


### Comentário S4S019

**Dia-base:** 2

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Consistência entre vistas](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Corrige apenas uma das duas inconsistências descritas e deixa o comportamento divergente.
- **B)** Incorreta. Alinhar sem registrar a decisão perde a rastreabilidade entre versões e regras.
- **C)** Correta. A divergência pode indicar abstração legítima ou inconsistência; por isso, deve ser justificada ou alinhada de modo rastreável.
- **D)** Incorreta. Alterar as duas vistas automaticamente pode apagar uma regra válida antes de determinar a intenção correta.

**Conceito:** Consistência semântica entre vistas.

**Pegadinha:** Tratar toda divergência como independência entre diagramas ou, no extremo oposto, exigir identidade entre níveis de abstração.

**Como pensar:** Cruze estrutura, interação, fluxo e objetivo; cada divergência exige decisão rastreável.

**Referência à apostila de estudo:** [Consistência entre vistas](semana_04_estudo.md#s4-d6-integracao).


### Comentário S4S020

**Dia-base:** 2

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Atividades](semana_04_estudo.md#s4-d2-atividades) e [Administração Pública](semana_04_estudo.md#s4-d2-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O fork abre os dois trabalhos, mas sem join o ato final pode ocorrer antes de ambos terminarem.
- **B)** Incorreta. A notação atende ao fluxo, mas eficiência não supre a competência exigida para o ato.
- **C)** Incorreta. Merge reconverge alternativas; não sincroniza trabalhos abertos concorrentemente.
- **D)** Correta. A notação e o princípio administrativo tratam fluxo e limite.

**Conceito:** Fluxo de atividades e controle administrativo.

**Pegadinha:** Confundir merge com join ou transformar eficiência em fonte de competência.

**Como pensar:** Aplique quatro filtros: escolha, concorrência, evidência e competência.

**Referência à apostila de estudo:** [Atividades](semana_04_estudo.md#s4-d2-atividades) e [Administração Pública](semana_04_estudo.md#s4-d2-b4).


### Comentário S4S021

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Componentes](semana_04_estudo.md#s4-d3-componentes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Mistura módulo, hardware e contrato.
- **B)** Incorreta. Artefato e objetivo foram confundidos.
- **C)** Correta. As visões respondem responsabilidade e localização.
- **D)** Incorreta. Possuem semânticas próprias.

**Conceito:** Componente modular.

**Pegadinha:** Confundir componente, classe, arquivo e servidor.

**Como pensar:** Separe capacidade lógica, contrato, artefato e nó.

**Referência à apostila de estudo:** [Componentes](semana_04_estudo.md#s4-d3-componentes).


### Comentário S4S022

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Interfaces e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cumprir e consumir determinam os papéis.
- **B)** Incorreta. Chamar não significa implementar.
- **C)** Incorreta. Receber e executar caracteriza fornecimento.
- **D)** Incorreta. Interface não é artefato.

**Conceito:** Interfaces fornecidas e requeridas.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com rede.

**Como pensar:** Pergunte quem cumpre, quem requer e por qual fronteira.

**Referência à apostila de estudo:** [Interfaces e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4S023

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Dependência e realização](semana_04_estudo.md#s4-d3-dependencias).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Receber não o torna cliente nessa relação.
- **B)** Incorreta. Reciprocidade precisa ser modelada à parte.
- **C)** Incorreta. O caso descreve dependência lógica.
- **D)** Correta. Mudança no fornecedor pode afetar o cliente.

**Conceito:** Dependência, realização e substituição.

**Pegadinha:** Inverter seta ou tratar uso como implementação.

**Como pensar:** Separe cliente dependente, contrato e realizador.

**Referência à apostila de estudo:** [Dependência e realização](semana_04_estudo.md#s4-d3-dependencias).


### Comentário S4S024

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Deployment](semana_04_estudo.md#s4-d3-deployment).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. As três categorias estão trocadas.
- **B)** Correta. Hardware, plataforma e peça implantável ficam separados.
- **C)** Incorreta. Nenhum papel corresponde.
- **D)** Incorreta. A visão comportamental é inadequada.

**Conceito:** Nós e ambientes de execução.

**Pegadinha:** Misturar topologia física e módulos lógicos.

**Como pensar:** Classifique dispositivo, ambiente, caminho e peça implantável.

**Referência à apostila de estudo:** [Deployment](semana_04_estudo.md#s4-d3-deployment).


### Comentário S4S025

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Artefatos](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Componente não é destino físico.
- **B)** Incorreta. Relações pertencem a outros domínios.
- **C)** Incorreta. Conectividade não substitui as relações.
- **D)** Correta. Uma explica o que concretiza; outra, onde executa.

**Conceito:** Artefato, manifestação e implantação.

**Pegadinha:** Trocar o que o arquivo concretiza por onde ele é instalado.

**Como pensar:** Pergunte se a relação responde o quê ou onde.

**Referência à apostila de estudo:** [Artefatos](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4S026

**Dia-base:** 3

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Interfaces e portas](semana_04_estudo.md#s4-d3-interfaces).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Duplica e oculta a diferença.
- **B)** Correta. Distingue fronteiras sem duplicar responsabilidade.
- **C)** Incorreta. Porta UML e rede foram confundidas.
- **D)** Incorreta. Nó não implementa contrato por existir.

**Conceito:** Interfaces fornecidas e requeridas.

**Pegadinha:** Inverter fornecedor e consumidor ou confundir porta UML com rede.

**Como pensar:** Pergunte quem cumpre, quem requer e por qual fronteira.

**Referência à apostila de estudo:** [Interfaces e portas](semana_04_estudo.md#s4-d3-interfaces).


### Comentário S4S027

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A cadeia cria evidência de ponta a ponta.
- **B)** Incorreta. O primeiro vínculo existe, mas nomes sem versão não identificam de modo reprodutível build e teste.
- **C)** Incorreta. Engenharia reversa recupera estrutura; não prova que o código representa a necessidade original.
- **D)** Incorreta. Versionar artefatos sem relacioná-los não permite percorrer requisito, implementação, build e evidência.

**Conceito:** Ferramentas e rastreabilidade.

**Pegadinha:** Atribuir à automação garantia de intenção ou qualidade.

**Como pensar:** Escolha pela lacuna e exija evidência versionada.

**Referência à apostila de estudo:** [Ferramentas de apoio](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4S028

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Ferramentas de apoio](semana_04_estudo.md#s4-d3-ferramentas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Compilar não transforma a estrutura legada, que pode conter erosão, em arquitetura-alvo aprovada.
- **B)** Incorreta. A conferência com o código valida a extração, mas não recupera intenção nem decisões sem validação humana.
- **C)** Correta. A extração recupera estrutura, não intenção completa.
- **D)** Incorreta. Revisão estrutural não substitui evidência dinâmica sobre o comportamento executado.

**Conceito:** Ferramentas e rastreabilidade.

**Pegadinha:** Atribuir à automação garantia de intenção ou qualidade.

**Como pensar:** Escolha pela lacuna e exija evidência versionada.

**Referência à apostila de estudo:** [Ferramentas de apoio](semana_04_estudo.md#s4-d3-ferramentas).


### Comentário S4S029

**Dia-base:** 3

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Artefatos](semana_04_estudo.md#s4-d3-artefatos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Integra impacto lógico, artefato, verificação e escala física.
- **B)** Incorreta. Versiona e replica o fornecedor, mas não verifica os clientes afetados pela mudança do contrato.
- **C)** Incorreta. Atualiza os participantes, porém reutilizar a versão e testar um só nó perde reprodutibilidade e cobertura física.
- **D)** Incorreta. Rastreia e versiona, mas deixa a incompatibilidade chegar aos dois destinos antes de testá-la.

**Conceito:** Artefato, manifestação e implantação.

**Pegadinha:** Trocar o que o arquivo concretiza por onde ele é instalado.

**Como pensar:** Percorra contrato, consumidores, implementação, build, teste e destinos.

**Referência à apostila de estudo:** [Artefatos](semana_04_estudo.md#s4-d3-artefatos).


### Comentário S4S030

**Dia-base:** 3

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Português técnico](semana_04_estudo.md#s4-d3-b5-portugues).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Transforma evidência parcial em certeza causal.
- **B)** Correta. Concessão e referente são claros, sem garantia indevida.
- **C)** Incorreta. Conector contrasta, mas a conclusão continua excessiva.
- **D)** Incorreta. Referentes são vagos e o salto permanece.

**Conceito:** Precisão da justificativa técnica.

**Pegadinha:** Preservar palavras e alterar referente, paralelismo ou força.

**Como pensar:** Cheque conector, referente, modalidade e alcance da conclusão.

**Referência à apostila de estudo:** [Português técnico](semana_04_estudo.md#s4-d3-b5-portugues).


### Comentário S4S031

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Gabarito:** D (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. A orientação por riscos distingue a espiral.
- **B)** Correta. Reuso exige avaliar adequação e integração dos ativos.
- **C)** Correta. Protótipos ajudam a investigar requisitos incertos.
- **D)** Incorreta (gabarito). Sequencialidade não torna realimentação ou mudança absolutamente impossíveis.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** Cascata, espiral, reuso, prototipação, RAD e incremento.

**Pegadinha:** Escolher pelo rótulo sem analisar contexto.

**Como pensar:** Cheque estabilidade, risco, feedback, reuso e valor fatiável.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4S032

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Preserva a maior incerteza.
- **B)** Correta. O risco orienta cada ciclo.
- **C)** Incorreta. Incrementar não substitui redução de risco.
- **D)** Incorreta. Ativo existente não elimina risco.

**Conceito:** Cascata, espiral, reuso, prototipação, RAD e incremento.

**Pegadinha:** Escolher pelo rótulo sem analisar contexto.

**Como pensar:** Cheque estabilidade, risco, feedback, reuso e valor fatiável.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4S033

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Usabilidade não valida qualidade interna.
- **B)** Incorreta. Faltam requisitos essenciais.
- **C)** Correta. A intenção exploratória não legitima atalhos.
- **D)** Incorreta. Aprendizagem é finalidade do protótipo.

**Conceito:** Cascata, espiral, reuso, prototipação, RAD e incremento.

**Pegadinha:** Escolher pelo rótulo sem analisar contexto.

**Como pensar:** Cheque estabilidade, risco, feedback, reuso e valor fatiável.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4S034

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Podem ocorrer juntos ou separadamente.
- **B)** Incorreta. Pode apenas reduzir defeito ou incerteza.
- **C)** Incorreta. Precisa agregar capacidade.
- **D)** Incorreta. São estratégias de desenvolvimento.

**Conceito:** Cascata, espiral, reuso, prototipação, RAD e incremento.

**Pegadinha:** Escolher pelo rótulo sem analisar contexto.

**Como pensar:** Cheque estabilidade, risco, feedback, reuso e valor fatiável.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4S035

**Dia-base:** 4

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Preço inicial não representa todo o esforço.
- **B)** Incorreta. Infraestrutura e suporte integram o custo total e não podem ser retirados da comparação.
- **C)** Incorreta. Compatibilidade nominal e preço inicial não substituem teste de integração nem avaliação de dependência.
- **D)** Incorreta. Suporte contratado não transfere ao fornecedor a responsabilidade do órgão por integração e aceite.

**Conceito:** Cascata, espiral, reuso, prototipação, RAD e incremento.

**Pegadinha:** Escolher pelo rótulo sem analisar contexto.

**Como pensar:** Cheque estabilidade, risco, feedback, reuso e valor fatiável.

**Referência à apostila de estudo:** [Modelos de ciclo de vida](semana_04_estudo.md#s4-d4-modelos).


### Comentário S4S036

**Dia-base:** 4

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Fases do desenvolvimento](semana_04_estudo.md#s4-d4-fases).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Baseline extensa não justifica avançar deixando arquitetura e riscos centrais sem tratamento.
- **B)** Incorreta. Transição pressupõe produto suficientemente integrado e pronto para preparação operacional.
- **C)** Correta. Volume documental não substitui redução de risco.
- **D)** Incorreta. A elaboração trata arquitetura e risco sem exigir retorno até eliminar toda incerteza de requisito.

**Conceito:** Concepção, elaboração, construção e transição.

**Pegadinha:** Tratar ênfase de fase como proibição absoluta.

**Como pensar:** Associe visão, arquitetura/risco, produto e uso operacional.

**Referência à apostila de estudo:** [Fases do desenvolvimento](semana_04_estudo.md#s4-d4-fases).


### Comentário S4S037

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Gerenciamento de projetos](semana_04_estudo.md#s4-d4-projetos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Cor não executa resposta.
- **B)** Incorreta. Comparar realizado é acompanhar.
- **C)** Correta. Medição sem decisão não corrige a situação.
- **D)** Incorreta. Atraso não encerra automaticamente o projeto.

**Conceito:** Projeto, planejamento, acompanhamento e controle.

**Pegadinha:** Confundir medir com controlar ou projeto com operação.

**Como pensar:** Localize objetivo temporário, referência, medição e decisão.

**Referência à apostila de estudo:** [Gerenciamento de projetos](semana_04_estudo.md#s4-d4-projetos).


### Comentário S4S038

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Escopo, WBS, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. As funções foram invertidas.
- **B)** Incorreta. Papéis não substituem entregas nem sequência.
- **C)** Incorreta. Baseline ainda precisa de governança.
- **D)** Correta. Escopo e tempo se conectam, mas não são iguais.

**Conceito:** Escopo e restrições do projeto.

**Pegadinha:** Usar WBS como cronograma ou isolar efeitos da mudança.

**Como pensar:** Parta da entrega e propague impactos nas restrições.

**Referência à apostila de estudo:** [Escopo, WBS, tempo e custos](semana_04_estudo.md#s4-d4-escopo-tempo-custos).


### Comentário S4S039

**Dia-base:** 4

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Escopo e prazo não cobrem os impactos explícitos em custo, risco e aquisição.
- **B)** Correta. A mudança possui impactos cruzados explícitos.
- **C)** Incorreta. Aprova antes de concluir a análise integrada de qualidade, comunicação e aquisição.
- **D)** Incorreta. Baseline sujeita a controle não significa imutabilidade nem rejeição automática.

**Conceito:** Integração do gerenciamento.

**Pegadinha:** Transferir todo risco ao fornecedor ou decidir uma área isoladamente.

**Como pensar:** Liste impactos, estime consequências e só então atualize referências autorizadas.

**Referência à apostila de estudo:** [Riscos, aquisições e integração](semana_04_estudo.md#s4-d4-riscos-aquisicoes-integracao).


### Comentário S4S040

**Dia-base:** 4

**Nível:** Médio

**Uso:** Simulado

**Referência:** [RLM aplicado a projetos](semana_04_estudo.md#s4-d4-b4-rlm).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Cálculos e interpretação estão errados.
- **B)** Incorreta. O impacto também compõe a medida.
- **C)** Incorreta. Probabilidades foram ignoradas.
- **D)** Correta. Os produtos estão corretos e o limite é preservado.

**Conceito:** Probabilidade, impacto e lógica.

**Pegadinha:** Usar a base errada ou tratar valor esperado como certeza.

**Como pensar:** Calcule cada exposição e não converta valor esperado em evento certo.

**Referência à apostila de estudo:** [RLM aplicado a projetos](semana_04_estudo.md#s4-d4-b4-rlm).


### Comentário S4S041

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A cadeia distingue causa, produto e manifestação.
- **B)** Incorreta. As categorias foram trocadas.
- **C)** Incorreta. Pessoa não é classificada como defeito de software.
- **D)** Incorreta. Os três conceitos possuem papéis próprios.

**Conceito:** Fundamentos, níveis e técnicas de teste.

**Pegadinha:** Confundir erro, defeito, falha, nível e técnica.

**Como pensar:** Identifique objeto, objetivo, execução e oráculo do teste.

**Referência à apostila de estudo:** [Testes de software](semana_04_estudo.md#s4-d5-testes).


### Comentário S4S042

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Dinâmico refere-se à execução do software.
- **B)** Incorreta. Roteiro não elimina execução.
- **C)** Incorreta. A classificação foi invertida.
- **D)** Correta. Uma analisa sem executar; a outra observa execução.

**Conceito:** Fundamentos, níveis e técnicas de teste.

**Pegadinha:** Confundir erro, defeito, falha, nível e técnica.

**Como pensar:** Identifique objeto, objetivo, execução e oráculo do teste.

**Referência à apostila de estudo:** [Testes de software](semana_04_estudo.md#s4-d5-testes).


### Comentário S4S043

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O escopo excede uma unidade e há execução.
- **B)** Incorreta. A ordem e o objetivo não correspondem.
- **C)** Correta. Primeiro examina interfaces; depois, necessidade de negócio.
- **D)** Incorreta. São categorias de outra dimensão.

**Conceito:** Fundamentos, níveis e técnicas de teste.

**Pegadinha:** Confundir erro, defeito, falha, nível e técnica.

**Como pensar:** Identifique objeto, objetivo, execução e oráculo do teste.

**Referência à apostila de estudo:** [Testes de software](semana_04_estudo.md#s4-d5-testes).


### Comentário S4S044

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Partição não exige código.
- **B)** Correta. Uma deriva da entrada; outra, da estrutura interna.
- **C)** Incorreta. Cobertura de ramos usa estrutura.
- **D)** Incorreta. São técnicas, não níveis.

**Conceito:** Fundamentos, níveis e técnicas de teste.

**Pegadinha:** Confundir erro, defeito, falha, nível e técnica.

**Como pensar:** Identifique objeto, objetivo, execução e oráculo do teste.

**Referência à apostila de estudo:** [Testes de software](semana_04_estudo.md#s4-d5-testes).


### Comentário S4S045

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Testes de software](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Objetivo e nível não decorrem da data.
- **B)** Correta. Confirma a mudança e procura efeitos colaterais.
- **C)** Incorreta. Os casos são executados.
- **D)** Incorreta. A descrição inclui execução de testes.

**Conceito:** Fundamentos, níveis e técnicas de teste.

**Pegadinha:** Confundir erro, defeito, falha, nível e técnica.

**Como pensar:** Identifique objeto, objetivo, execução e oráculo do teste.

**Referência à apostila de estudo:** [Testes de software](semana_04_estudo.md#s4-d5-testes).


### Comentário S4S046

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Qualidade](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Conformidade e adequação são perguntas distintas.
- **B)** Incorreta. A ordem está invertida.
- **C)** Incorreta. Não são as categorias pedidas.
- **D)** Incorreta. Nível e mudança não respondem.

**Conceito:** Qualidade de produto e processo.

**Pegadinha:** Reduzir qualidade à ausência de defeito conhecido.

**Como pensar:** Separe atributo, critério, garantia do processo e controle do produto.

**Referência à apostila de estudo:** [Qualidade](semana_04_estudo.md#s4-d5-qualidade).


### Comentário S4S047

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Qualidade](semana_04_estudo.md#s4-d5-qualidade).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Reduz indevidamente a atuação preventiva.
- **B)** Incorreta. Sem critério não há avaliação objetiva.
- **C)** Incorreta. Silêncio não prova adequação.
- **D)** Correta. Prevenção e detecção possuem ênfases complementares.

**Conceito:** Qualidade de produto e processo.

**Pegadinha:** Reduzir qualidade à ausência de defeito conhecido.

**Como pensar:** Separe atributo, critério, garantia do processo e controle do produto.

**Referência à apostila de estudo:** [Qualidade](semana_04_estudo.md#s4-d5-qualidade).


### Comentário S4S048

**Dia-base:** 5

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Manutenção](semana_04_estudo.md#s4-d5-manutencao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Não há defeito sendo reparado.
- **B)** Incorreta. O objetivo principal não é melhoria solicitada.
- **C)** Correta. A mudança responde ao ambiente tecnológico.
- **D)** Incorreta. Não é reestruturação para reduzir falha futura.

**Conceito:** Categorias e fluxo de manutenção.

**Pegadinha:** Classificar pela tecnologia usada, não pelo motivo da mudança.

**Como pensar:** Pergunte se corrige, adapta, melhora ou previne degradação.

**Referência à apostila de estudo:** [Manutenção](semana_04_estudo.md#s4-d5-manutencao).


### Comentário S4S049

**Dia-base:** 5

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A cadeia preserva consistência e evidência.
- **B)** Incorreta. Há origem e correção, mas faltam alinhamento dos modelos, regressão e implantação controlada.
- **C)** Incorreta. Requisito e teste atualizados não tornam coerentes modelos e código deixados para outra versão.
- **D)** Incorreta. Corrige, testa e implanta, porém sem origem e impacto registrados perde a cadeia de decisão.

**Conceito:** Processos, modelos e fases.

**Pegadinha:** Confundir modelo de ciclo com categoria de manutenção.

**Como pensar:** Percorra origem, impacto, produtos, verificação e transição.

**Referência à apostila de estudo:** [Processos e fases](semana_04_estudo.md#s4-d5-processos).


### Comentário S4S050

**Dia-base:** 5

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao) e [Testes de software](semana_04_estudo.md#s4-d5-testes).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A fonte é confirmada, mas manter o requisito rompe a cadeia que deve explicar código e testes.
- **B)** Incorreta. Atualiza a origem e a implementação, porém reteste isolado não procura efeitos colaterais.
- **C)** Correta. Legalidade, rastreabilidade e qualidade são integradas.
- **D)** Incorreta. Atualiza a cadeia, mas publicar antes de reteste e regressão elimina a evidência prévia exigida.

**Conceito:** Fonte e competência institucional.

**Pegadinha:** Confundir autonomia regional com poder de afastar lei.

**Como pensar:** Valide fonte, versão, impacto, correção e evidência de teste.

**Referência à apostila de estudo:** [Legislação CRA/CFA](semana_04_estudo.md#s4-d5-legislacao) e [Testes de software](semana_04_estudo.md#s4-d5-testes).


### Comentário S4S051

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Faltam decisões lógicas e evidência.
- **B)** Incorreta. Não há controle suficiente.
- **C)** Correta. Liga origem, realização, verificação e evolução.
- **D)** Incorreta. Implementação não substitui validação.

**Conceito:** Integração de requisitos, UML, testes e mudança.

**Pegadinha:** Atualizar uma vista e deixar as demais incoerentes.

**Como pensar:** Percorra a cadeia e verifique consistência entre vistas.

**Referência à apostila de estudo:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao).


### Comentário S4S052

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Descrevem o mesmo sistema.
- **B)** Correta. A inconsistência precisa de resolução rastreável.
- **C)** Incorreta. Remove evidência sem decidir.
- **D)** Incorreta. Topologia não resolve regra.

**Conceito:** Integração de requisitos, UML, testes e mudança.

**Pegadinha:** Atualizar uma vista e deixar as demais incoerentes.

**Como pensar:** Percorra a cadeia e verifique consistência entre vistas.

**Referência à apostila de estudo:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao).


### Comentário S4S053

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Artefato não é fim isolado.
- **B)** Incorreta. Ferramenta não cobre direção e controle.
- **C)** Incorreta. Valor depende do contexto das partes.
- **D)** Correta. Serviço e valor ligam capacidade a resultado.

**Conceito:** Gestão de serviços e governança de TI.

**Pegadinha:** Tratar ITIL e COBIT como sinônimos ou produtos técnicos.

**Como pensar:** Separe valor de serviço, governança, direção, gestão e controle.

**Referência à apostila de estudo:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).


### Comentário S4S054

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Os domínios são relacionados, não idênticos.
- **B)** Incorreta. As ênfases foram invertidas.
- **C)** Incorreta. É estrutura de governança e gestão, não produto ERP.
- **D)** Incorreta. A distinção é essencial.

**Conceito:** Gestão de serviços e governança de TI.

**Pegadinha:** Tratar ITIL e COBIT como sinônimos ou produtos técnicos.

**Como pensar:** Separe valor de serviço, governança, direção, gestão e controle.

**Referência à apostila de estudo:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).


### Comentário S4S055

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).

**Gabarito:** D (a afirmação incorreta).

**Análise das alternativas:**

- **A)** Correta. Gestão de serviços e valor integram o recorte de ITIL.
- **B)** Correta. Governança e gestão de informação e tecnologia integram o recorte de COBIT.
- **C)** Correta. Os escopos podem coexistir e apoiar objetivos relacionados.
- **D)** Incorreta (gabarito). Nenhum deles se reduz a ferramenta de chamados, e seus escopos não são equivalentes.

**Observação:** a questão pede a alternativa incorreta; por isso, D é o gabarito.

**Conceito:** Gestão de serviços e governança de TI.

**Pegadinha:** Tratar ITIL e COBIT como sinônimos ou produtos técnicos.

**Como pensar:** Separe valor de serviço, governança, direção, gestão e controle.

**Referência à apostila de estudo:** [ITIL e COBIT](semana_04_estudo.md#s4-d6-itil-cobit).


### Comentário S4S056

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Foca relacionamento com públicos/clientes.
- **B)** Incorreta. Integra recursos e funções internas amplas.
- **C)** Correta. A necessidade central é gestão documental.
- **D)** Incorreta. Gerencia processos ponta a ponta, não só documentos.

**Conceito:** Recursos informacionais.

**Pegadinha:** Escolher sigla por moda sem identificar o problema.

**Como pensar:** Classifique documento, fluxo, processo, integração interna e relacionamento.

**Referência à apostila de estudo:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).


### Comentário S4S057

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Automação local e gestão do processo possuem alcances distintos.
- **B)** Incorreta. As finalidades não correspondem.
- **C)** Incorreta. Integração empresarial é outra necessidade.
- **D)** Incorreta. Ambos podem envolver pessoas e regras.

**Conceito:** Recursos informacionais.

**Pegadinha:** Escolher sigla por moda sem identificar o problema.

**Como pensar:** Classifique documento, fluxo, processo, integração interna e relacionamento.

**Referência à apostila de estudo:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).


### Comentário S4S058

**Dia-base:** 6

**Nível:** Médio

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. CRM não integra toda retaguarda e GED é documental.
- **B)** Correta. Um integra funções internas; outro, relacionamento.
- **C)** Incorreta. BPM não é sistema de relacionamento por definição.
- **D)** Incorreta. Documentos e tarefas não cobrem as duas necessidades.

**Conceito:** Recursos informacionais.

**Pegadinha:** Escolher sigla por moda sem identificar o problema.

**Como pensar:** Classifique documento, fluxo, processo, integração interna e relacionamento.

**Referência à apostila de estudo:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).


### Comentário S4S059

**Dia-base:** 6

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. GED e workflow atendem às duas primeiras camadas, mas ERP não substitui BPM na gestão ponta a ponta.
- **B)** Correta. Cada recurso responde a uma camada do problema.
- **C)** Incorreta. BPM e workflow foram invertidos entre tarefa local executável e processo ponta a ponta.
- **D)** Incorreta. Workflow e BPM estão adequados, mas ERP não é a escolha específica para controle documental versionado.

**Conceito:** Recursos informacionais.

**Pegadinha:** Escolher sigla por moda sem identificar o problema.

**Como pensar:** Separe objeto documental, fluxo executável e processo gerenciado.

**Referência à apostila de estudo:** [GED, workflow, BPM, ERP e CRM](semana_04_estudo.md#s4-d6-recursos).


### Comentário S4S060

**Dia-base:** 6

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao) e [Português](semana_04_estudo.md#s4-d6-portugues).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Um teste funcional não sustenta valor nem conformidade sem verificar processo, controles e demais efeitos.
- **B)** Incorreta. Interface preservada não prova que testes antigos cobrem a regra e os efeitos modificados.
- **C)** Correta. Integra rastreabilidade, serviço, processo e evidência.
- **D)** Incorreta. Governança e registro não substituem atualização técnica nem testes ligados à mudança.

**Conceito:** Precisão lógica e argumentativa.

**Pegadinha:** Criar causalidade ou garantia além da evidência.

**Como pensar:** Cheque origem, vistas, teste, serviço, processo, controle e força da conclusão.

**Referência à apostila de estudo:** [Integração e rastreabilidade](semana_04_estudo.md#s4-d6-integracao) e [Português](semana_04_estudo.md#s4-d6-portugues).


---
