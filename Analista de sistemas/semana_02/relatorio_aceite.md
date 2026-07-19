# Relatório de Aceite - Semana 2 - Analista de Sistemas

**Data da auditoria reparadora:** 19/07/2026.

## Veredito

| Aceite | Resultado |
|---|---|
| Produção | **Aprovada - 95/100, sem falha eliminatória** |
| Status autorizado | **Material aprovado para execução** |
| Execução pelo candidato | **Pendente** |

Este relatório substitui o aceite anterior de 90/100, que foi suspenso depois que a auditoria ampliada encontrou níveis inflados, referências semanticamente imprecisas e comentários genéricos no super simulado. A nova nota usa exclusivamente a rubrica canônica de `../planejamento/padrao_semanal.md`.

`Material aprovado para execução` significa que teoria, jornada, questões, discursiva e simulado foram produzidos e auditados. Não comprova horas estudadas, revisões cumpridas, textos escritos nem desempenho; portanto, a semana não está `Concluída`.

## Inventário final

| Componente | Quantidade |
|---|---:|
| Dias de estudo | 6 |
| Questões principais | 300 |
| Questões extras | 120 |
| Banco semanal | 420 |
| Gabaritos e comentários A-D do banco | 420 |
| Super simulado | 60 |
| Gabaritos e comentários A-D do super | 60 |
| Alternativas E | 0 |

### Dificuldade auditada

| Conjunto | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Principais | 173 | 116 | 11 | 300 |
| Extras | 79 | 40 | 1 | 120 |
| **Banco semanal** | **252** | **156** | **12** | **420** |
| Super simulado | 16 | 40 | 4 | 60 |

As matrizes 20/20/10, 8/8/4 e 24/24/12 foram referências iniciais de produção, não cotas de aceite. A classificação final decorre da leitura individual: Médio exige aplicação direta; Difícil, ao menos duas decisões; Muito difícil, três ou mais filtros independentes. Enumeração ou associação direta de vários conceitos não foi aceita como dificuldade máxima.

### Uso pedagógico do banco

| Uso | Quantidade |
|---|---:|
| Essenciais | 90 |
| Aprofundamento | 150 |
| Revisão | 90 |
| Simulado | 90 |

A primeira passagem abre seis principais Essenciais por dia, com teto de dez somente quando houver correção integral. As extras `Dia X.1–X.5` entram pela primeira vez no D+7, depois de eventual saldo D0/D+2. O restante segue a fila prevista em `semana_02_jornada.md`.

## Evidência da auditoria semântica

- 300 principais classificadas individualmente em `revisao_niveis_d1_d3.md` e `revisao_niveis_d4_d6.md`;
- 120 extras auditadas quanto a cobertura, resposta única, nível, distratores e comprimento em `revisao_extras_d1_d2.md`, `revisao_extras_d3_d4.md` e `revisao_extras_d5_d6.md`;
- 144 principais e 65 extras reformuladas; quatro principais receberam aprofundamento multifiltro final, sendo três já pertencentes ao conjunto das 144;
- super simulado relido integralmente, com exatamente dez itens por dia, nove substituições de cobertura e seis refinamentos adicionais de distratores;
- 24 itens do banco foram resolvidos novamente após a integração, em amostra estratificada de quatro por dia; os quatro multifiltro e todos os comandos negativos também foram conferidos;
- o nível do super foi recalibrado novamente após leitura humana, reduzindo a inflação de `Muito difícil` e preservando apenas S2S029, S2S039, S2S050 e S2S053 nessa faixa;
- gabaritos equilibrados dentro de cada nível: no banco, 63/63/63/63 entre as médias, 39/39/39/39 entre as difíceis e 3/3/3/3 entre as muito difíceis; no super, 4/4/4/4, 10/10/10/10 e 1/1/1/1;
- zero sequência de três letras iguais, motivo curto repetido três vezes, duplicata literal, alerta de comprimento sem tratamento, comando negativo sem observação ou divergência entre item, tabela e comentário;
- todas as referências apontam para âncoras existentes e anteriores à cobrança; Q150 e Q300 receberam reforço teórico e referência específica após a conferência pós-integração.

O verificador final foi executado com:

```text
python tools/audit_semana02.py
OK: 420 questões + 60 do super simulado; metadados, alternativas, comentários, gabaritos e âncoras validados.
Principais: Médio=173, Difícil=116, Muito difícil=11
Extras: Médio=79, Difícil=40, Muito difícil=1
Banco: Médio=252, Difícil=156, Muito difícil=12
Super: Médio=16, Difícil=40, Muito difícil=4
```

## Jornada e discursiva

- cada dia fecha 360 minutos líquidos: Sessão A de 170, Sessão B de 170 e consolidação de 20;
- a ordem física foi corrigida para teoria, exemplos e prática guiada antes dos Blocos 4–6, seguida por revisão, checklist e fechamento;
- D+2, D+7 e D+21 possuem datas, precedência e pontos de parada; o saldo não aumenta a carga diária;
- a progressão discursiva vai de recorte e tese ao texto integral manuscrito de 45 minutos;
- foram conferidos gênero, 20 pontos, mínimo de 12, 20–30 linhas, tempo oficial compartilhado de 4 horas, folha definitiva e rubrica macro/micro do edital.

## Perfil da banca e questões oficiais

O lote foi calibrado pelo contrato de `../planejamento/perfil_banca_consulplan.md`: comandos precisos, alternativas do mesmo domínio, cenários funcionais, cálculos executáveis e negação visível. A calibração permanece **provisória** quanto à amostra empírica comparável, porque não foi confirmado o conjunto completo de caderno específico, gabarito definitivo e situação dos recursos.

A busca está documentada em `../questoes_oficiais/semana_02.md`. Nenhuma questão foi chamada de oficial nem copiada para o banco autoral. O concurso da Prefeitura de Vitória/ES permanece em acompanhamento para eventual uso futuro no PDF original, depois da confirmação completa.

## Rubrica canônica

| Dimensão | Máximo | Nota | Evidência |
|---|---:|---:|---|
| Fidelidade ao edital e às fontes | 15 | 14 | conteúdo rastreado e regras discursivas conferidas; amostra oficial comparável ainda provisória |
| Cobertura e profundidade da teoria | 20 | 19 | teoria suficiente e referências autocontidas; execução depende das rotas e pontos de parada |
| Exemplos e prática guiada | 15 | 13 | exemplos, casos e produtos presentes nos seis dias; nem toda subseção extensa possui dois exemplos autônomos |
| Alinhamento entre estudo e questões | 15 | 15 | 420 itens cobertos, referências sincronizadas e zero questão órfã |
| Qualidade das questões | 15 | 14 | resposta única, nível substantivo, distratores revisados e equilíbrio A-D; calibração empírica oficial segue provisória |
| Qualidade dos comentários | 15 | 15 | 480 comentários com A-D, conceito, pegadinha, raciocínio e referência |
| Organização e uso pedagógico | 5 | 5 | ordem física, jornada de 6h, filas e revisões espaçadas validadas |
| **Total** | **100** | **95** | **Material aprovado para execução** |

## Pendências operacionais

- executar as filas D0 e registrar confiança de 0 a 3;
- cumprir D+2, D+7 e D+21 sem somar sessões;
- preencher o caderno de erros e reescrever o trecho discursivo mais fraco;
- resolver o super sem consulta e corrigi-lo em sessão separada;
- registrar tempo e desempenho por assunto;
- repetir o checkpoint de questões oficiais antes da Semana 3.

Essas pendências não reprovam a produção; elas impedem apenas o status `Concluído`.
