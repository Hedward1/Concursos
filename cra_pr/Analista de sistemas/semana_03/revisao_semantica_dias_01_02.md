# Revisão semântica — Dias 1 e 2 da Semana 3

**Data da revisão:** 19/07/2026

**Arquivo auditado:** `partes/questoes_dias_01_02.md`
**Escopo preservado:** 100 questões principais, 40 extras e seus 140 comentários. O banco auditado não foi editado.

## Método

Cada item foi resolvido independentemente do comentário e, em seguida, confrontado com o gabarito, as análises A–D e a teoria indicada. A leitura verificou: suficiência do enunciado, resposta única, correção do gabarito, cobertura teórica anterior, precisão da âncora, dificuldade substantiva e qualidade dos distratores.

Para o alerta objetivo de extensão, foi aplicado o padrão do projeto: correta maior que `1,30 ×` o maior distrator ou menor que `0,70 ×` o menor distrator, após retirada da marcação Markdown. O alerta pede revisão editorial; isoladamente, não declara o conteúdo falso.

## Resultado executivo

| Critério | Resultado |
|---|---:|
| Questões e comentários lidos | 140/140 |
| Gabaritos semanticamente corretos | 139 |
| Resposta incorreta | 1 |
| Questões ambíguas após leitura integral | 0 |
| Teoria insuficiente ou cobrada antes da hora | 0 |
| Fragmentos de referência ausentes ou semanticamente errados | 0 |
| Níveis superestimados | 58 |
| Alertas objetivos de extensão/alinhamento das alternativas | 57 |
| Status do lote | **Revisão obrigatória** |

O erro eliminatório é `S3D2Q071`. A teoria é suficiente para todos os itens e, nesse caso, contradiz precisamente o gabarito registrado.

## Achado crítico — resposta incorreta

| ID | Diagnóstico | Evidência | Correção recomendada |
|---|---|---|---|
| `S3D2Q071` | Gabarito e comentário incorretos | O enunciado pede o mapeamento de vários telefones por profissional, cada um com tipo e confirmação. A alternativa **A** propõe relação própria com a chave do profissional e os dados de cada telefone, que é a solução ensinada. A alternativa **C**, marcada como correta, propõe texto separado por ponto e vírgula, justamente o antipadrão que oculta ocorrências e viola a representação relacional. | Trocar o gabarito de **C** para **A**, marcar A como correta, C como incorreta e ajustar tabela/comentário. Recalibrar o nível de Difícil para Médio. |

Não foi encontrada segunda resposta defensável nos outros 139 itens.

## Níveis superestimados

O padrão semanal exige duas decisões reais para `Difícil` e três ou mais filtros independentes para `Muito difícil`. Associação direta, reprodução de definição, identificação de conector ou combinação de rótulos não sobe de nível apenas por conter várias entradas.

### Dia 1 — principais

Recomenda-se `Difícil → Médio` em:

`S3D1Q010`, `S3D1Q019`, `S3D1Q020`, `S3D1Q021`, `S3D1Q022`, `S3D1Q023`, `S3D1Q029`, `S3D1Q032`, `S3D1Q033`, `S3D1Q035`, `S3D1Q036`, `S3D1Q037`, `S3D1Q038`, `S3D1Q039`, `S3D1Q040`, `S3D1Q041`, `S3D1Q042`, `S3D1Q046` e `S3D1Q047`.

Recomenda-se `Muito difícil → Difícil` em:

`S3D1Q045`, `S3D1Q049` e `S3D1Q050`.

Os itens `S3D1Q043`, `S3D1Q044` e `S3D1Q048` sustentam o nível Muito difícil porque integram governança, nível arquitetural, proveniência, contrato externo e mudança física em uma cadeia multifiltro.

### Dia 1 — extras

Recomenda-se `Difícil → Médio` em:

`Extra Dia 1.13`, `Extra Dia 1.14`, `Extra Dia 1.15` e `Extra Dia 1.18`.

### Dia 2 — principais

Recomenda-se `Difícil → Médio` em:

`S3D2Q069`, `S3D2Q070`, `S3D2Q071`, `S3D2Q072`, `S3D2Q073`, `S3D2Q074`, `S3D2Q076`, `S3D2Q077`, `S3D2Q083`, `S3D2Q084`, `S3D2Q085`, `S3D2Q086`, `S3D2Q091`, `S3D2Q092`, `S3D2Q096`, `S3D2Q098` e `S3D2Q099`.

Recomenda-se `Muito difícil → Difícil` em:

`S3D2Q087`, `S3D2Q089`, `S3D2Q090`, `S3D2Q093` e `S3D2Q097`.

Recomenda-se `Muito difícil → Médio` em:

`S3D2Q088`, `S3D2Q094` e `S3D2Q095`.

### Dia 2 — extras

Recomenda-se `Difícil → Médio` em:

`Extra Dia 2.13`, `Extra Dia 2.14`, `Extra Dia 2.15`, `Extra Dia 2.16`, `Extra Dia 2.17`, `Extra Dia 2.18` e `Extra Dia 2.20`.

### Contagem das recalibrações

| Faixa | Quantidade |
|---|---:|
| Dia 1 — principais | 22 |
| Dia 1 — extras | 4 |
| Dia 2 — principais | 25 |
| Dia 2 — extras | 7 |
| **Total** | **58** |

## Distratores fracos e pistas de extensão

Foram encontrados 57 alertas objetivos de comprimento. O padrão dominante é a alternativa correta ser a única formulação completa e qualificada, enquanto os distratores são absolutos, curtos ou de domínio claramente estranho. Isso permite acertar por forma antes de dominar o conteúdo.

### Dia 1 — principais, 14 alertas

`S3D1Q006`, `S3D1Q009`, `S3D1Q020`, `S3D1Q022`, `S3D1Q025`, `S3D1Q026`, `S3D1Q027`, `S3D1Q032`, `S3D1Q033`, `S3D1Q034`, `S3D1Q041`, `S3D1Q044`, `S3D1Q046` e `S3D1Q048`.

### Dia 1 — extras, 9 alertas

`Extra Dia 1.5`, `Extra Dia 1.6`, `Extra Dia 1.8`, `Extra Dia 1.10`, `Extra Dia 1.11`, `Extra Dia 1.12`, `Extra Dia 1.13`, `Extra Dia 1.15` e `Extra Dia 1.17`.

### Dia 2 — principais, 26 alertas

`S3D2Q055`, `S3D2Q056`, `S3D2Q058`, `S3D2Q060`, `S3D2Q063`, `S3D2Q065`, `S3D2Q067`, `S3D2Q068`, `S3D2Q069`, `S3D2Q077`, `S3D2Q078`, `S3D2Q079`, `S3D2Q080`, `S3D2Q081`, `S3D2Q082`, `S3D2Q083`, `S3D2Q086`, `S3D2Q087`, `S3D2Q088`, `S3D2Q089`, `S3D2Q090`, `S3D2Q093`, `S3D2Q096`, `S3D2Q097`, `S3D2Q098` e `S3D2Q099`.

### Dia 2 — extras, 8 alertas

`Extra Dia 2.4`, `Extra Dia 2.5`, `Extra Dia 2.7`, `Extra Dia 2.12`, `Extra Dia 2.13`, `Extra Dia 2.16`, `Extra Dia 2.17` e `Extra Dia 2.18`.

### Casos qualitativamente mais evidentes

| Padrão | IDs representativos | Problema |
|---|---|---|
| Correta é a única alternativa qualificada | `S3D1Q009`, `S3D1Q044`, `S3D1Q048`, `S3D2Q058`, `S3D2Q090`, `S3D2Q098` | A resposta concentra ressalvas e relações causais; as demais são negações simples ou erros grosseiros. |
| Distratores de domínio estranho | `Extra Dia 1.6`, `Extra Dia 1.9`, `Extra Dia 1.10`, `S3D2Q069`, `S3D2Q084`, `Extra Dia 2.17` | Opções mencionam ortografia, planilha, armazenamento, caracteres ou ordenação sem permanecer no mesmo domínio da decisão. |
| Absolutos fáceis de eliminar | `S3D1Q021`, `S3D1Q031`, `Extra Dia 1.11`, `Extra Dia 1.17`, `S3D2Q087`, `S3D2Q094` | “Toda”, “somente”, “sempre”, “automaticamente” ou equivalentes tornam a alternativa falsa sem exigir o conteúdo central. |

Recomendação: reescrever os distratores como erros plausíveis da mesma família conceitual e encurtar a correta quando a explicação adicional puder ficar no comentário. Não alongar opções apenas para equilibrar caracteres.

## Cobertura teórica e referências

Os 140 itens possuem fragmento existente e a teoria anterior oferece a regra necessária. Não foi localizado conteúdo cobrado apenas depois do item, nem referência que leve a assunto diferente.

No Dia 2, os 70 links usam o rótulo genérico “Material-base do tópico”, embora apontem para fragmentos específicos como `#s3-d2-chaves`, `#s3-d2-mapeamento` e `#s3-d2-google-planilhas`. Isso não constitui erro semântico de referência, mas é uma melhoria editorial recomendada: exibir o nome real da seção facilita a navegação e a correção do aluno.

## Ordem de correção recomendada

1. Corrigir `S3D2Q071` antes de qualquer publicação ou execução.
2. Recalibrar os 58 níveis no item, comentário e matriz de distribuição.
3. Revisar os 57 alertas de extensão, começando pelos casos qualitativos da tabela.
4. Tornar os rótulos de referência do Dia 2 descritivos, sem alterar os fragmentos já válidos.
5. Rodar novamente o auditor de contagem, equilíbrio por nível, gabarito e comprimento.

## Parecer

O lote tem boa cobertura e comentários coerentes em 139 itens, mas não deve ser declarado pronto enquanto `S3D2Q071` mantiver resposta errada. A dificuldade também está sistematicamente inflada em questões de reconhecimento direto, e a extensão da correta oferece pista em 57 itens. Após essas correções, a base teórica e a rastreabilidade já existentes permitem aprovação sem expansão de conteúdo.

## Fechamento dos achados

Revalidação concluída em 19/07/2026 sobre o arquivo-fonte dos Dias 1 e 2. As seções anteriores preservam o diagnóstico inicial; esta seção registra o estado depois das correções.

| Achado inicial | Tratamento aplicado | Resultado final |
|---|---|---:|
| Gabarito incorreto de `S3D2Q071` | Resposta corrigida para **A** no comentário e na tabela; análises de A e C sincronizadas | **1/1 corrigido** |
| Níveis inflados | Recalibração aplicada no item e no comentário de cada ID apontado | **58/58 corrigidos** |
| Alertas objetivos de extensão | Alternativas reescritas de forma substantiva, preservando o conceito e o gabarito; justificativas antigas removidas | **57/57 tratados; 0 alertas** |
| Rótulos genéricos de referência | Substituição pelo nome descritivo da seção, sem alterar o fragmento válido | **160/160 ocorrências tratadas; 0 restantes** |

### Métricas da revalidação

- questões e comentários: **140/140** pares presentes, com IDs únicos, quatro alternativas A–D e quatro análises A–D;
- gabaritos: **140/140** entradas de tabela coincidem com o campo “Alternativa correta”;
- metadados: nível, uso e referência coincidem entre item e comentário em **140/140** pares;
- referências: **47** fragmentos locais distintos utilizados e **0** âncoras ausentes;
- extensão: **0** alternativas corretas fora do intervalo objetivo de `0,70 ×` a `1,30 ×` dos distratores; **0** justificativas antigas de comprimento remanescentes;
- sequência: **0** trincas de letras iguais e **0** motivos curtos de largura 2 a 4 repetidos três vezes;
- distribuição por dia: Dia 1 `A=17, B=17, C=18, D=18`; Dia 2 `A=18, B=18, C=17, D=17`;
- distribuição por nível: Médio `A=28, B=28, C=29, D=29`; Difícil `A=6, B=6, C=5, D=6`; Muito difícil `A=1, B=1, C=1, D=0`.

**Status final dos Dias 1 e 2: aprovado para integração ao consolidado da Semana 3.**

### Nota de integração global

O balanceamento posterior dos 420 itens permutou a posição de uma alternativa de nível Médio neste lote, sem alterar o conteúdo semanticamente correto. Questão, comentário e tabela foram movidos em conjunto. A distribuição final de letras dos Dias 1–2 ficou: Médio A=28, B=29, C=28, D=29; Difícil A=6, B=6, C=5, D=6; Muito difícil A=1, B=1, C=1, D=0. A diferença permanece em no máximo uma letra dentro de cada nível.
