# Relatório de Migração - Semana 2 - Analista de Sistemas

**Data de conclusão:** 19/07/2026.

## Situação

A migração estrutural e a auditoria semântica foram concluídas. O veredito vigente está em `relatorio_aceite.md`: **Material aprovado para execução**, com execução do candidato pendente.

Este documento preserva a diferença entre três etapas que não podem ser confundidas:

1. baseline legado;
2. migração mecânica;
3. auditoria semântica e reparação final.

## Baseline e migração mecânica

A primeira migração acrescentou IDs, níveis, usos e referências às 300 principais e normalizou as 120 extras. A distribuição `168 Médias / 168 Difíceis / 84 Muito difíceis` era apenas a aplicação mecânica das matrizes iniciais 20/20/10 e 8/8/4. Ela nunca constituiu classificação semântica final.

Também foi adotado o uso operacional de 90 Essenciais, 150 Aprofundamento, 90 Revisão e 90 Simulado. Uso indica quando resolver; não define dificuldade.

## Diagnóstico posterior

A auditoria ampliada demonstrou que a migração mecânica ainda possuía:

- dificuldade superestimada por preenchimento de matriz;
- alternativas corretas destacadas pelo comprimento em parte do banco;
- distratores alheios ou pouco discriminadores;
- duplicatas entre extras;
- referências corretas como âncora, mas imprecisas em conteúdo em casos pontuais;
- comentários genéricos e referências semanticamente erradas no super;
- cobertura desequilibrada do super entre os seis dias;
- prática guiada posicionada depois dos Blocos 4–6;
- fila das 30 extras Essenciais sem identificação explícita no D+7.

Por isso, o aceite intermediário foi suspenso e não é usado como evidência final.

## Reparação concluída

- as 300 principais e as 120 extras foram classificadas item a item;
- 144 principais e 65 extras foram reformuladas; quatro principais receberam aprofundamento multifiltro final;
- duplicatas, pistas de comprimento e distratores fracos foram eliminados;
- 110 permutações no banco foram sincronizadas entre alternativa, comentário e tabelas para obter equilíbrio A-D por nível, sem mudar a resposta substantiva;
- o super recebeu nove substituições de cobertura, seis refinamentos adicionais e nova leitura integral;
- a dificuldade do super foi recalibrada sem cotas, preservando somente quatro itens Muito difíceis;
- o super passou a conter exatamente dez itens de cada dia;
- jornada, ordem física, D+2/D+7/D+21 e progressão discursiva foram normalizadas;
- o auditor passou a verificar comprimento, duplicatas, motivos de gabarito, equilíbrio por nível, comandos negativos, cobertura 10 × 6, ordem física, filas e âncoras semânticas críticas.

## Distribuição final

| Conjunto | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Principais | 173 | 116 | 11 | 300 |
| Extras | 79 | 40 | 1 | 120 |
| Banco | 252 | 156 | 12 | 420 |
| Super | 16 | 40 | 4 | 60 |

Essa distribuição substitui integralmente a fotografia mecânica 168/168/84. Nenhum rótulo foi mantido apenas para fechar quota.

## Questões oficiais

A ausência de item oficial integrado não é apresentada como “bloqueio sanado”. A busca de 19/07/2026 não confirmou simultaneamente caderno específico, gabarito definitivo e situação dos recursos para uma amostra aderente. A ausência e o concurso comparável em acompanhamento estão registrados em `../questoes_oficiais/semana_02.md`.

## Evidência final

```text
python tools/audit_semana02.py
OK: 420 questões + 60 do super simulado; metadados, alternativas, comentários, gabaritos e âncoras validados.
Principais: Médio=173, Difícil=116, Muito difícil=11
Extras: Médio=79, Difícil=40, Muito difícil=1
Banco: Médio=252, Difícil=156, Muito difícil=12
Super: Médio=16, Difícil=40, Muito difícil=4
```

O diagnóstico intermediário está encerrado. Para nota, rubrica, limites e pendências operacionais, prevalece `relatorio_aceite.md`.
