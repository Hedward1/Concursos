# CRA-PR 2026 - Direito

Material de preparação para os cargos de **Advogado** e **Analista Jurídico** do concurso CRA-PR 2026.

Os dois cargos compartilham a mesma matriz de 50 questões, o mesmo conteúdo programático e a mesma prova discursiva de parecer jurídico. Por isso, este projeto utiliza uma única trilha de estudo. As diferenças de requisito, vaga, jornada e turno estão registradas abaixo.

## Situação do projeto

- planejamento geral: criado;
- método de preparação jurídica: criado;
- padrão de qualidade das semanas: criado;
- matriz de fontes e vigência: criada;
- edital consolidado conforme Retificação I: preservado localmente;
- Semana 1: material produzido e aprovado para execução; falta a auditoria operacional do candidato;
- Semanas 2 a 9: ainda não produzidas.

Uma semana só poderá ser chamada de concluída depois da auditoria prevista em `planejamento/padrao_semanal_juridico.md`.

## Cargos atendidos

| Item | Advogado | Analista Jurídico |
|---|---|---|
| Requisito específico | Ensino Superior em Direito e registro regular na OAB/PR | Ensino Superior em Direito |
| Vagas indicadas no edital consolidado | 25 de cadastro de reserva | 1 imediata + 25 de cadastro de reserva |
| Jornada | 30 horas semanais | 40 horas semanais |
| Turno da prova | Tarde | Manhã |
| Duração da prova | 4h30 | 4h30 |
| Discursiva | Parecer jurídico | Parecer jurídico |

O edital permite inscrição em até dois cargos quando as provas ocorrem em turnos distintos. Assim, quem cumprir os requisitos de ambos poderá aproveitar integralmente o mesmo material, mas deverá confirmar as inscrições e todas as condições diretamente na página oficial do concurso.

## Matriz da prova objetiva

Todas as questões valem 2 pontos.

| Disciplina | Questões | Pontos | Participação na objetiva | Prioridade |
|---|---:|---:|---:|---|
| Direito Constitucional | 8 | 16 | 16% | Muito alta |
| Direito Administrativo | 8 | 16 | 16% | Muito alta |
| Direito Processual Civil | 8 | 16 | 16% | Muito alta |
| Legislação do CRA-PR e do CFA | 8 | 16 | 16% | Muito alta |
| Língua Portuguesa | 5 | 10 | 10% | Alta |
| Direito do Trabalho | 4 | 8 | 8% | Média |
| Direito Tributário | 4 | 8 | 8% | Média |
| Direito Civil | 3 | 6 | 6% | Média, com conteúdo extenso |
| Direito Financeiro e Orçamentário | 2 | 4 | 4% | Menor peso, mas obrigatória |
| **Total** | **50** | **100** | **100%** | |

Constitucional, Administrativo, Processo Civil e Legislação CRA/CFA concentram **32 questões e 64 pontos**. Esse núcleo recebe revisões em todas as semanas.

## Parecer jurídico

A prova discursiva vale 20 pontos e deve ter de 30 a 60 linhas:

- 15 pontos para abordagem do tema e desenvolvimento do conteúdo jurídico;
- 5 pontos para aspectos linguísticos;
- nota mínima de 12 pontos para aprovação;
- tema relacionado aos conhecimentos específicos do cargo;
- realização sem consulta.

O parecer é treinado desde a primeira semana. O estudo não ficará restrito à memorização de um modelo: haverá identificação do problema, seleção da norma aplicável, construção da fundamentação, enfrentamento de argumentos contrários, conclusão e revisão linguística.

Só serão corrigidos os pareceres de candidatos com pelo menos 60 pontos na objetiva e classificados até a 30ª posição por lista e por cargo. Depois da preferência etária prevista em lei, a nota do parecer é o primeiro critério de desempate.

## Prazo para títulos

A avaliação de títulos vale até 5 pontos. A nota final máxima é 125: objetiva 100 + parecer 20 + títulos 5. O edital consolidado fixa **23h59 de 03/08/2026** como término do upload e informa que não haverá novo prazo. Quem tiver titulação deve conferir imediatamente os documentos e históricos exigidos nos itens 7.3 a 7.24.

## Método de preparação

O método-base é o mesmo usado no projeto de Analista de Sistemas:

`edital -> planejamento -> teoria -> exemplos e casos -> questões -> correção comentada -> caderno de erros -> simulado -> revisão direcionada`

Na área jurídica, cada etapa incorpora quatro cuidados adicionais:

1. separar texto legal, jurisprudência, doutrina e hipótese prática;
2. controlar vigência, alteração e revogação das normas;
3. identificar tribunal, precedente e data de corte quando houver jurisprudência;
4. praticar parecer jurídico em progressão semanal.

O roteiro operacional de 6h líquidas, as revisões espaçadas e o treino do parecer estão em `planejamento/metodo_preparacao_direito.md`.

## Estrutura

- `README.md`: visão geral e estado do projeto;
- `edital/edital_cra_pr_2026_advogado_analista_juridico_retificacao_1.pdf`: edital oficial consolidado utilizado como base;
- `planejamento/plano_mestre_cra_pr_2026_direito.md`: cronograma de 9 semanas e controle de cobertura;
- `planejamento/metodo_preparacao_direito.md`: método diário e semanal de estudo;
- `planejamento/padrao_semanal_juridico.md`: contrato de qualidade para teoria, questões, pareceres e simulados;
- `fontes/matriz_edital_fontes.md`: fontes primárias, vigência, data de conferência e pendências;
- `semana_XX/semana_XX_estudo.md`: apostila teórica da semana, quando produzida;
- `semana_XX/semana_XX_questoes.md`: índice do banco de questões comentadas;
- `semana_XX/questoes/`: fragmentos modulares do banco, quando o volume exigir;
- `semana_XX/semana_XX_pareceres.md`: casos, espelhos e treinos de parecer;
- `semana_XX/semana_XX_super_simulado.md`: simulado integrador semanal.
- `semana_XX/relatorio_aceite.md`: auditoria do material e pendências de execução.

A primeira semana está em [`semana_01/`](semana_01/README.md).

## Alerta sobre a Retificação I

O PDF antigo que estava na pasta de Analista de Sistemas não é o arquivo consolidado atual: ele ainda cita a RN CFA nº 640/2024. A versão oficial disponível em 13/07/2026 está identificada como **conforme Retificação I** e substitui essa referência pela **RN CFA nº 671/2025**, que revogou expressamente a RN nº 640/2024.

Para impedir mistura entre normas:

- o projeto de Direito usa a versão consolidada baixada da página oficial;
- a RN nº 671/2025 é a base vigente e editalícia;
- a RN nº 640/2024 só poderá aparecer como histórico normativo claramente identificado;
- toda apostila deverá registrar a data de conferência de suas fontes.

## Outros alertas de vigência

- O edital nomeia a Resolução CNJ nº 115/2010 no tópico de precatórios, mas a base oficial do CNJ a identifica como revogada pela Resolução nº 303/2019. O material deverá preservar a referência editalícia como histórico e ensinar o regime atual sem apresentar a nº 115 como vigente.
- A Convenção nº 87 da OIT consta expressamente em Direito do Trabalho, embora não tenha sido ratificada pelo Brasil. Seu conteúdo será estudado sem alegar incorporação ao direito interno por ratificação.

O tratamento operacional desses conflitos está em `fontes/matriz_edital_fontes.md`.

## Fontes centrais

- [Edital consolidado conforme Retificação I](https://cdnsite.institutoconsulplan.org.br/concursos/1330/b2c07c473c9749fea22728da3c964c06.pdf)
- [Página do concurso indicada pelo CRA-PR](https://www.institutoconsulplan.org.br/Concurso/crapr2026)
- [Notícia e cronograma no site do CRA-PR](https://cra-pr.org.br/cra-pr-divulga-edital-de-concurso-publico/)
- [RN CFA nº 671/2025](https://documentos.cfa.org.br/?a=show&c=documento&id=1038)
- [Página oficial do Regimento Interno do CRA-PR](https://cra-pr.org.br/transparencia_legislacao/transparencia-regimento-interno/)

## Regra de atualização

O candidato deve acompanhar os atos da banca até a prova. Antes de produzir cada semana, a versão do edital, a legislação e as fontes jurisprudenciais serão revalidadas. Mudança posterior não será incorporada de memória: será registrada na matriz de fontes, com link oficial e data de conferência.
