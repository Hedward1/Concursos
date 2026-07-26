# Revisão semântica — Super Simulado da Semana 3

## Escopo

Arquivo auditado e corrigido diretamente: `semana_03_super_simulado.md`.

Foram lidos e confrontados:

- 60 questões, dez por dia da Semana 3;
- 240 alternativas;
- 60 comentários individualizados;
- 240 análises de alternativas;
- tabela integral de gabarito;
- 45 referências internas distintas para a teoria consolidada.

Critérios: unicidade e correção do gabarito, suficiência da teoria, precisão da referência, dependência de produto/dialeto, dificuldade real, competitividade de distratores, coerência do comentário e pistas formais de comprimento ou sequência.

## Resultado semântico

| Controle | Resultado |
|---|---:|
| Gabaritos incorretos | **0** |
| Itens com duas alternativas defensáveis | **0** |
| Comentários contraditórios | **0** |
| Referências quebradas | **0** |
| Referências semanticamente inadequadas | **0** |
| Níveis inflados corrigidos | **9** |
| Conjuntos de distratores reescritos | **8** |
| Delimitação de produto/dialeto acrescentada | **1** |
| Pista de comprimento corrigida | **1** |

O banco preserva os 60 IDs, as 60 letras corretas e a ordem das questões.

## 1. Gabaritos e comentários

Nenhum gabarito foi alterado. As respostas permanecem únicas e tecnicamente adequadas, inclusive nos itens de maior integração:

- `S3S020`: dependências parcial e transitiva são tratadas sem perder o vínculo entre protocolo e item;
- `S3S029`: `LEFT JOIN`, filtro em `ON`, `COUNT(p.id)` e `HAVING` preservam ausência e filtram o grupo correto;
- `S3S030`: grão por profissional e chave única de desempate produzem paginação estável;
- `S3S046`: redo da confirmada e undo da não confirmada permanecem corretamente separados;
- `S3S059`: a sequência de baseline, cardinalidade, estatística, sargabilidade e regressão continua sendo a chave;
- `S3S060`: integração, grão, modelo dimensional e razão entre somas permanecem a solução correta.

As 240 análises foram verificadas. Cada comentário contém uma análise A–D, aponta a mesma letra da tabela e explica o erro específico das alternativas incorretas.

## 2. Recalibração dos níveis

O desenho original reservava exatamente dois itens “Muito difícil” por dia, mas nove deles exigiam apenas aplicação direta de quadro ou exemplo. Foram reclassificados para **Difícil**, no enunciado e no comentário:

| ID | Motivo da reclassificação |
|---|---|
| `S3S009` | classificação direta de quatro elementos explicitamente estudados |
| `S3S010` | associação direta entre AD, DBA, mudança física e visão externa |
| `S3S019` | mapeamento padrão de N:M com atributo no relacionamento |
| `S3S039` | roteiro de saneamento e aplicação de constraints com uma única solução completa |
| `S3S040` | transação explícita com commit final e rollback no erro |
| `S3S049` | integração de três controles, mas com solução conceitual direta |
| `S3S050` | correspondência direta entre constraint, menor privilégio e transação |
| `S3S059` | protocolo de diagnóstico já apresentado na teoria |
| `S3S060` | pipeline de BI correto por eliminação de grão e média inadequados |

Foram mantidos como **Muito difícil**:

- `S3S020`, pela combinação de chave composta, dependência parcial, transitiva e preservação de vínculos;
- `S3S029`, pela composição simultânea de junção externa, posição do filtro, contagem de nulos e `HAVING`;
- `S3S030`, pela integração entre granularidade, agregação, ordenação total e paginação.

Distribuição após esta primeira passagem: **24 Médios, 33 Difíceis e 3 Muito difíceis**.

Naquele estágio, o cabeçalho do simulado foi sincronizado: **24/24/12** permaneceu identificado como desenho inicial, enquanto **24/33/3** registrou o resultado desta primeira passagem. A integração definitiva está documentada ao fim deste relatório.

## 3. Distratores reescritos

Foram reescritos oito conjuntos nos quais duas ou mais alternativas eram caricatas ou estavam longe demais do erro conceitual cobrado:

| ID | Melhoria aplicada |
|---|---|
| `S3S010` | todos os planos agora acertam parte de papéis/níveis e falham em uma fronteira específica |
| `S3S037` | os erros agora comparam conferência posterior, amostra, estimativa e `SELECT` com predicado idêntico |
| `S3S039` | as alternativas erradas passaram a omitir, cada uma, órfãos, nulos, regra de negócio ou rollback |
| `S3S040` | a alternativa fraca sobre recursão foi trocada por transação que confirma mesmo após falha de auditoria |
| `S3S049` | cada alternativa incorreta agora preserva parte de atomicidade, concorrência ou recuperação e falha nas demais |
| `S3S055` | os erros agora tratam estatística individual, irrelevância da estimativa ou troca prematura do join |
| `S3S059` | a migração caricata foi substituída por atualização isolada de estatística sem testar sargabilidade/regressão |
| `S3S060` | os erros agora envolvem grão implícito, perda de denominadores ou granularidade por interação |

As 32 análises correspondentes foram sincronizadas. Nenhuma letra correta mudou.

## 4. Produto, dialeto e precisão formal

### `S3S052`

O conceito do intervalo semiaberto estava correto, mas a questão misturava funções e literais sem explicitar dialeto. O enunciado agora declara **SQL conceitual** e exige adaptar limites e tipos ao produto; o comentário repete a ressalva. Isso impede que validade sintática em um único SGBD vire atalho para a resposta.

### `S3S051`

A alternativa correta C tinha 30 caracteres, enquanto os distratores tinham de 43 a 59. Ela foi ampliada para explicitar que `uf` e `ativo` são as duas colunas iniciais contíguas do índice. A análise também foi atualizada. O ajuste remove a pista de alternativa excepcionalmente curta sem adicionar informação que entregue a chave.

## 5. Referências

As 45 âncoras distintas usadas pelo simulado existem em `semana_03_estudo.md`; nenhuma troca foi necessária. Também não foi encontrado item cujo alvo fosse apenas existente, mas semanticamente errado.

Pontos sensíveis confirmados:

- `S3S010` combina corretamente `#s3-d1-ad-dba` com `#s3-d1-arquitetura-bd`;
- `S3S029` combina junções com `#s3-d3-agrupamento-having`;
- `S3S039` aponta ao exemplo de migração e às restrições DDL;
- `S3S049` reúne transações, concorrência e recuperação;
- `S3S059` reúne otimização e índices;
- `S3S060` reúne BI e exemplos dimensionais.

## 6. Revalidação mecânica posterior

| Controle | Resultado |
|---|---:|
| Questões encontradas | 60/60 |
| Comentários encontrados | 60/60 |
| Quatro alternativas A–D por questão | 60/60 |
| Quatro análises A–D por comentário | 60/60 |
| Nível do item igual ao comentário | 60/60 |
| Tabela de gabarito igual ao comentário | 60/60 |
| Distribuição das letras | A=15, B=15, C=15, D=15 |
| Sequências de três letras iguais | 0 |
| Motivos de 2–4 letras repetidos três vezes seguidas | 0 |
| Referências internas ausentes | 0 |
| Alternativa correta abaixo de 0,65× ou acima de 1,35× da média dos distratores | 0 |

## Parecer final

**Aprovado.** O Super Simulado cobre os seis dias, possui gabaritos corretos, comentários consistentes, referências válidas e distribuição perfeita de letras. Depois das correções, os níveis refletem melhor a carga cognitiva e os distratores exigem domínio do conteúdo em vez de simples descarte por absurdo.

## Auditoria independente posterior e integração final

Este relatório registra a primeira passagem semântica. A [auditoria independente posterior](revisao_semantica_super_simulado_independente.md) resolveu novamente os 60 itens sem consultar o gabarito e substitui, como estado atual, a distribuição 24/33/3 acima. Ela delimitou `S3S036` ao SQL Server, reclassificou outros 19 itens de Difícil para Médio e fortaleceu os distratores de `S3S017`, `S3S045`, `S3S056`, `S3S057` e `S3S058`.

A distribuição definitiva é **43 Médios, 14 Difíceis e 3 Muito difíceis**. Na integração final, seis respostas do super tiveram somente a posição A–D permutada: `S3S012` A→C, `S3S020` D→B, `S3S035` A→C, `S3S036` C→A, `S3S059` B→A e `S3S060` C→D. Alternativa, análise correspondente e tabela foram movidas em conjunto, sem mudar a solução semântica. O resultado final é A=15, B=15, C=15 e D=15; por nível: Médio 10/11/11/11, Difícil 4/3/3/4 e Muito difícil 1/1/1/0. A verificação mecânica posterior permaneceu limpa.
