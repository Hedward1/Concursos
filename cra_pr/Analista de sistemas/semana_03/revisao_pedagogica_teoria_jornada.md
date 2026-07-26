# Revisão pedagógica — teoria, jornada e progressão discursiva da Semana 3

**Data da auditoria:** 19/07/2026
**Escopo principal:** `semana_03_estudo.md`, `semana_03_jornada.md` e `semana_03_dissertacoes.md`.
**Consulta cruzada:** edital local, jornada da Semana 2, índice de questões oficiais e bancos parciais apenas quando necessários para testar teoria antes da cobrança e os localizadores de filas.
**Regra de preservação:** esta auditoria não alterou os três arquivos avaliados.

## Resultado executivo

O núcleo pedagógico é amplo e, em geral, bem ordenado: os 26 pontos formais dos itens 6, 7 e 8 do edital estão localizados; os seis dias possuem Blocos 1–6 completos e na ordem; a jornada fecha 360 minutos por dia; as datas D+2, D+7 e D+21 estão corretas; e a progressão discursiva reproduz as regras materiais e a rubrica do edital.

O conjunto, porém, ainda não deve receber aceite final. Há quatro famílias de ajuste:

1. localizadores temáticos das filas de dez questões não sincronizados com os IDs atuais;
2. dois congestionamentos de revisão sem desempate operacional suficiente;
3. uma cobrança oficial de trigger MySQL colocada antes de uma síntese teórica específica do produto;
4. um link local para o banco consolidado ainda inexistente.

## Contagens verificadas

| Verificação | Resultado |
|---|---:|
| linhas da apostila | 4.575 |
| linhas da jornada | 290 |
| linhas do caderno discursivo | 187 |
| âncoras explícitas na apostila | 204 |
| âncoras explícitas no caderno discursivo | 6 |
| âncoras duplicadas | 0 |
| dias com Blocos 1–6, uma vez cada e em ordem | 6 de 6 |
| exemplos resolvidos completos na apostila | 91 |
| distribuição dos exemplos por dia | 18, 24, 12, 12, 12 e 13 |
| entradas do edital auditadas | 26: itens 6.1–6.15, 7.1–7.10 e item 8 |
| entradas do edital localizadas em teoria | 26 de 26 |
| links locais Markdown nos três arquivos | 38 |
| links locais resolvidos | 37 |
| links locais quebrados | 1 |
| URLs externas distintas encontradas | 46, incluindo URL fictícia usada em exemplo |
| dias com 360 minutos preservados | 6 de 6 |
| datas D+2 corretas | 6 de 6 |
| janelas D+7 e D+21 corretas | 6 de 6 |
| dias da progressão discursiva | 6 |
| questões oficiais posicionadas | 3: duas válidas e uma anulada |

## Cobertura dos itens 6, 7 e 8 do edital

### Item 6 — Banco de dados

Cobertura localizada e anterior às filas principais:

| Edital | Local predominante |
|---|---|
| 6.1–6.5: conceitos, AD, independência, dicionário e níveis | Dia 1 |
| 6.6–6.12: relacional, álgebra, modelagem, normalização, MER e mapeamento | Dia 2 |
| 6.13: SQL ANSI — definição, consulta e manipulação | Dias 3 e 4 |
| 6.14: Transact-SQL | Dia 4 |
| 6.15: suporte à inteligência de negócio | Dia 6 |

Não foi encontrada lacuna literal neste item. A separação de SQL entre consulta no Dia 3 e definição/manipulação no Dia 4 é pedagogicamente defensável e está declarada.

### Item 7 — SGBD

| Edital | Local predominante |
|---|---|
| 7.1–7.5: segurança, transação, concorrência, recuperação e integridade | Dia 5 |
| 7.6–7.8: procedures, views e triggers | Dia 4 |
| 7.9: índices e otimização | Dia 6 |
| 7.10: transações distribuídas | Dia 5 |

A teoria distingue garantia, mecanismo e consequência e evita transformar segurança, integridade, isolamento e recuperação em sinônimos.

### Item 8 — produtos

SQL Server, MySQL e PostgreSQL são comparados no Dia 6, com versão explícita, dialeto, organização, índices, plano e concorrência. A delimitação por produto é adequada. Em verificação pontual de fontes oficiais, PostgreSQL 18.4, SQL Server 2025/17.x e a linha MySQL 9.7 estavam documentados na data da auditoria.

## Ordem pedagógica e teoria antes da cobrança

### O que passou

- Os Blocos 1, 2 e 3 precedem produto, revisões, discursiva, Bloco 6 e questões em todos os dias.
- Cada dia possui exatamente um Bloco 1, 2, 3, 4, 5 e 6, nessa ordem.
- O Bloco 6 está declarado como recuperação, sem conteúdo novo.
- As filas D0 começam depois dos 170 minutos de teoria e aplicação.
- A questão oficial 35, de outer join, é aberta somente depois do Dia 3.
- A questão oficial 32, anulada por ambiguidade em BI, é estudada somente depois do Dia 6, sem taxa de acerto nem letra a memorizar.

### Ajuste necessário — questão oficial 36

A questão oficial 36 é dependente de comportamento de trigger no MySQL 8. O Dia 4 ensina trigger de modo geral e apresenta implementação T-SQL; a documentação MySQL 8.4 aparece nas fontes, mas não há, antes da calibração, um quadro teórico curto que ensine as particularidades usadas pelo item — evento, impossibilidade de `CALL` para disparar trigger e restrições sobre tabela temporária.

**Risco:** a resolução pode virar consulta posterior ou memorização do gabarito, contrariando a regra de teoria antes da cobrança.

**Correção recomendada:** inserir antes da calibração uma caixa de comparação MySQL 8.4 com apenas as regras necessárias e fonte oficial, ou deslocar esse item para depois da comparação de produtos do Dia 6.

### Ajuste necessário — filas temáticas e IDs

As seções `Fila ordenada de dez Essenciais` descrevem tema por ID, mas os títulos dos bancos parciais atuais mostram que esses localizadores não foram regenerados depois da ordenação definitiva das questões. O problema aparece nos seis dias. Exemplos objetivos:

- `S3D1Q002` está descrita como “funções do SGBD”, mas o item atual é “Informação em contexto”;
- `S3D2Q052` está descrita como “chaves candidatas”, mas o item atual é “Tupla e grau da relação”;
- `S3D3Q104` está descrita como `INNER JOIN`, mas o item atual trata limites de `BETWEEN`;
- `S3D4Q152` está descrita como PK/UNIQUE, mas o item atual trata operações de DML;
- `S3D5Q202` está descrita genericamente como ACID, mas o item atual focaliza savepoint e confirmação;
- `S3D6Q251` está descrita como B-tree/hash, mas o item atual trata índice como caminho com custo.

**Contagem:** 6 de 6 mapas de fila possuem ao menos uma divergência comprovada.
**Risco:** retorno à âncora errada, D+2 com expectativa temática falsa e aparente cobrança de conteúdo ainda não localizado.
**Correção recomendada:** gerar a tabela `ID → título real → âncora real → momento` diretamente do banco congelado.

## Jornada e carga de 360 minutos

### Resultado

Todos os dias preservam 360 minutos líquidos:

- Sessão A: 170;
- Sessão B: 170;
- consolidação: 20.

Nos Dias 1–5, o Bloco 5 discursivo usa 40 minutos. No Dia 6, usa 45; a jornada reduz Bloco 6 e fechamento sem aumentar a carga. Os Dias 3 e 4 não repetem localmente a linha de consolidação em sua subseção da apostila, mas a rotina global e a jornada governante mantêm os 20 minutos. Trata-se de assimetria editorial, não de estouro real.

## D+2, D+7, D+21 e colisões com a Semana 2

### Datas

| Origem | D+2 | D+7 | D+21 | Resultado |
|---:|---:|---:|---:|---|
| 27/07 | 29/07 | 03/08 | 17/08 | correto |
| 28/07 | 30/07 | 04/08 | 18/08 | correto |
| 29/07 | 31/07 | 05/08 | 19/08 | correto |
| 30/07 | 01/08 | 06/08 | 20/08 | correto |
| 31/07 | 02/08 | 07/08 | 21/08 | correto |
| 01/08 | 03/08 | 08/08 | 22/08 | correto |

### Colisão 1 — abertura de 27/07

A Semana 2 admite transportar o D+2 do Dia 5 de 26/07 para 27/07 como D+3. No mesmo 27/07 já vencem:

- eventual D+2 do Dia 6 da Semana 2;
- D+7 do Dia 1 da Semana 2;
- revisão fixa de Legislação e Google Documentos.

A jornada da Semana 3 prioriza o saldo do Dia 6, mas não diz onde entra o saldo transportado do Dia 5. Quatro demandas podem disputar 35 minutos.

### Colisão 2 — primeiro Bloco 4 de 03/08

Se o domingo não for usado, em 03/08 coincidem:

- D+3 do Dia 5 da Semana 3;
- D+2 do Dia 6 da Semana 3;
- D+7 do Dia 1 da Semana 3;
- matéria fixa da Semana 4.

A regra geral manda concluir saldos antes do D+7, mas não define prioridade entre os dois saldos nem o destino nominal do remanescente.

**Correção recomendada para as duas colisões:** declarar uma fila única ordenada, por exemplo `saldo mais antigo → saldo D+2/D+3 seguinte → D+7 → núcleo fixo reservado`, com teto por minutos e data explícita da próxima reabertura. O núcleo fixo de dez minutos não deve desaparecer.

## Divisão das Extras

A versão recompilada passou nesta verificação. Apostila, jornada e metadados dos bancos atuais declaram:

| Dia | Distribuição validada |
|---:|---|
| 1 | 8 Legislação + 8 Google Documentos + 4 Português, intercaladas por faixa de uso |
| 2 | 7 Administração + 7 Google Planilhas + 6 Português, intercaladas por faixa de uso |
| 3 | 10 Legislação + 5 RLM + 5 Português |
| 4 | 12 Administração + 8 Português |
| 5 | 10 Legislação + 5 internet + 5 Português |
| 6 | 5 RLM + 10 ferramentas/internet + 5 Português/discursiva |

Nos Dias 1 e 2, a intercalação é intencional e o campo `Matéria` é a fonte operacional. **Contagem:** 6 de 6 dias sincronizados.

## Progressão discursiva e regras do edital

### Resultado

O caderno discursivo passou nos pontos auditados:

- dissertação de conhecimento geral;
- caráter eliminatório e classificatório;
- 20 pontos e mínimo de 12;
- 20 a 30 linhas;
- menos de 20 linhas recebe zero;
- excedente à 30ª linha é desconsiderado;
- manuscrito legível, caneta transparente azul ou preta;
- ausência de consulta;
- somente Folha de Texto Definitivo avaliada;
- objetiva e discursiva dentro das quatro horas do cargo;
- classificação até a 30ª posição das listas aplicáveis;
- critérios e pesos 4 + 4 + 3 + 2 + 3 + 4 = 20;
- descontos microestruturais coerentes;
- progressão tese → desenvolvimento 1 → desenvolvimento 2/contraponto → introdução/conclusão → plano → texto integral;
- Dia 6 com planejamento 7 min, redação 30 min e revisão 8 min = 45 min.

Não foi encontrada regra de proposta de intervenção no formato Enem, e o material corretamente não a impõe.

## Links e âncoras

### O que passou

- 204 âncoras da apostila e 6 do caderno discursivo, sem duplicação;
- todas as âncoras usadas pela jornada para teoria e dissertação existem;
- o PDF local do edital existe e a página 28 confirma os itens 6–8;
- o índice de questões oficiais existe e registra caderno, página, gabarito pós-recursos e anulação;
- as fontes externas são predominantemente primárias: Planalto, CFA, Google, PostgreSQL, MySQL, Microsoft e Oracle.

### Link pendente

`semana_03_jornada.md` aponta para `semana_03_questoes.md`, arquivo que ainda não existia no momento da auditoria.

**Contagem:** 1 link local quebrado em 38.
**Correção recomendada:** recompilar o banco consolidado ou retirar temporariamente o link até a geração.

## Parecer

| Eixo | Parecer |
|---|---|
| cobertura literal dos itens 6–8 | aprovado |
| teoria e exemplos | aprovado com ressalva da calibração MySQL |
| Blocos 1–6 | aprovado |
| 360 min/dia | aprovado |
| D+2/D+7/D+21 | datas aprovadas; precedência precisa de ajuste |
| colisões com Semana 2 | ajuste necessário |
| discursiva | aprovado |
| links/âncoras | aprovado com um link pendente |
| sincronização das Extras | aprovado |
| sincronização temática das filas de dez IDs | não aprovado |

**Status final:** **aprovado pedagogicamente com bloqueios de integração**. O conteúdo teórico pode ser preservado; o aceite operacional depende de sincronizar os localizadores das filas, resolver as duas colisões, ensinar a particularidade MySQL antes da questão oficial 36 e gerar `semana_03_questoes.md`.

## Fechamento dos bloqueios de integração

**Data da revalidação:** 19/07/2026. Esta seção registra o estado posterior às correções e substitui, para fins de aceite, o status histórico acima.

| Bloqueio original | Revalidação posterior | Situação |
|---|---|---|
| mapas `ID → título → âncora` das filas | as 60 linhas dos seis mapas foram comparadas com as 300 questões do banco consolidado; títulos e referências coincidem, com **0 divergências** | fechado |
| colisão de 27/07 | a jornada reserva os dez minutos intocáveis da matéria fixa, ordena `D+3 S2D5 → D+2 S2D6 → D+7 S2D1` nos 25 minutos restantes e reabre eventual saldo em 28/07 | fechado |
| colisão de 03/08 | a jornada ordena `D+3 S3D5 → D+2 S3D6 → D+7 S3D1 → matéria fixa da Semana 4`, preserva os dez minutos fixos e reabre eventual saldo em 04/08 | fechado |
| teoria MySQL antes da questão oficial 36 | a caixa [trigger no MySQL 8.4](semana_03_estudo.md#s3-d4-trigger-mysql8), situada no Dia 4 antes da fila e da calibração oficial, ensina os eventos declarados, o disparo automático — e não por `CALL` — e a restrição a tabela `TEMPORARY` e view | fechado |
| link para o banco consolidado | `semana_03_questoes.md` existe no diretório da semana e o link da jornada resolve; nova varredura encontrou **38 de 38 links locais válidos** nos três arquivos auditados | fechado |

**Status revalidado:** **aprovado pedagogicamente, sem bloqueios de integração pendentes**. Permanecem preservados os seis dias de 360 minutos, a sequência Blocos 1–6 e as janelas D+2, D+7 e D+21.
