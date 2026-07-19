# Relatório de Aceite — Semana 3 — Analista de Sistemas

**Data da auditoria:** 19/07/2026.

## Veredito

| Aceite | Resultado |
|---|---|
| Produção | **Aprovada — 98/100, sem falha eliminatória** |
| Status autorizado | **Material aprovado para execução** |
| Execução pelo candidato | **Pendente** |

`Material aprovado para execução` significa que teoria, jornada, banco autoral, progressão discursiva e super simulado foram produzidos, confrontados com o edital e auditados. Não comprova horas estudadas, revisões cumpridas, texto manuscrito nem desempenho; portanto, a semana não está `Concluída`.

## Inventário final

| Componente | Quantidade |
|---|---:|
| Dias de estudo | 6 |
| Carga diária | 360 minutos líquidos |
| Exemplos resolvidos completos na teoria | 91 |
| Questões principais | 300 |
| Questões extras | 120 |
| Banco semanal autoral | 420 |
| Gabaritos e comentários A–D do banco | 420 |
| Super simulado | 60 |
| Gabaritos e comentários A–D do super | 60 |
| Alternativas E | 0 |

### Dificuldade auditada

| Conjunto | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Principais | 180 | 107 | 13 | 300 |
| Extras | 82 | 36 | 2 | 120 |
| **Banco semanal** | **262** | **143** | **15** | **420** |
| Super simulado | 43 | 14 | 3 | 60 |

As matrizes diárias `20/20/10`, `8/8/4` e a matriz inicial `24/24/12` do super orientaram a redação; não foram tratadas como cotas. A leitura individual rebaixou itens solucionáveis por associação direta e preservou `Muito difícil` apenas quando havia ao menos três filtros ou decisões reais.

### Uso pedagógico do banco

| Uso | Quantidade |
|---|---:|
| Essenciais | 90 |
| Aprofundamento | 150 |
| Revisão | 90 |
| Simulado | 90 |

A fila diária abre seis principais Essenciais e permite avançar até dez somente quando houver correção A–D integral. O saldo segue D+2; as Extras Essenciais abrem em D+7; Revisão, Simulado e D+21 permanecem nos ciclos próprios, sem criar uma terceira sessão diária.

## Evidência das auditorias semânticas

Os 420 itens receberam leitura em três lotes independentes de 140 questões e 140 comentários:

- [Dias 1–2](revisao_semantica_dias_01_02.md): um gabarito incorreto foi corrigido (`S3D2Q071 = A`), 58 níveis foram recalibrados, 57 conjuntos de alternativas foram reescritos e 160 rótulos genéricos de referência foram substituídos; a revalidação terminou sem alerta de extensão, âncora ausente ou divergência;
- [Dias 3–4](revisao_semantica_dias_03_04.md): três inconsistências bloqueadoras, três lacunas teóricas, 19 níveis inflados, 11 conjuntos de distratores, 17 referências e duas delimitações de produto foram sanados; `S3D4Q162` passou a registrar a resposta semanticamente correta;
- [Dias 5–6](revisao_semantica_dias_05_06.md): não havia gabarito ambíguo ou incorreto; foram encerradas ressalvas de literal temporal, `INCLUDE`, versões dos produtos e fallback clustered do InnoDB, além de oito níveis e 13 conjuntos de distratores;
- [super simulado — primeira passagem](revisao_semantica_super_simulado.md): 60 itens, 240 alternativas e 240 análises foram relidos; nove níveis e oito conjuntos de distratores foram corrigidos, sem mudança de resposta semântica;
- [super simulado — auditoria independente](revisao_semantica_super_simulado_independente.md): a resolução cega coincidiu em 60/60; depois foram encerrados um problema de delimitação de produto, 19 níveis inflados e cinco conjuntos de distratores fracos. A distribuição efetiva ficou em 43/14/3.

Depois das correções semânticas, três posições de alternativas do banco e seis do super foram permutadas com as respectivas análises e tabelas. As respostas semânticas permaneceram inalteradas. O banco ficou exatamente A=105, B=105, C=105 e D=105; no super, A=B=C=D=15. Dentro de cada nível, a diferença final é de no máximo uma letra. Não há trinca de letra igual nem motivo curto de duas a quatro letras repetido três vezes.

O [relatório pedagógico](revisao_pedagogica_teoria_jornada.md) confirmou cobertura dos 26 recortes dos itens 6, 7 e 8 do edital, 91 exemplos completos, seis mapas de dez Essenciais sincronizados, Blocos 1–6 na ordem, teoria MySQL anterior à questão oficial correspondente e 38/38 links locais válidos nos arquivos auditados.

## Jornada, revisões e discursiva

- cada dia fecha 360 minutos: Sessão A de 170, Sessão B de 170 e consolidação de 20;
- D0, D+2, D+7 e D+21 possuem datas e pontos de parada;
- as colisões de 27/07 e 03/08 reservam dez minutos para a matéria fixa, usam 25 minutos no saldo mais antigo e transportam o restante sem ampliar a carga;
- o Bloco 6 recupera conteúdo anterior e não introduz regra nova;
- a discursiva progride de recorte/tese ao texto integral manuscrito de 20 a 30 linhas, com rubrica de 20 pontos e mínimo de 12.

## Perfil da banca e questões oficiais

O lote segue o contrato de `../planejamento/perfil_banca_consulplan.md`: comandos variados, alternativas do mesmo domínio, cenários práticos, integração moderada, negação visível e delimitação do fornecedor quando o comportamento depende de SQL Server, MySQL ou PostgreSQL.

O índice `../questoes_oficiais/semana_03.md` separa o banco autoral de uma amostra verificável do TJMA 2024, Tipo 4 — Azul:

- questão 35, p. 13: outer join, mantida com gabarito D;
- questão 36, p. 14: trigger no MySQL, gabarito definitivo B após recurso;
- questão 32, p. 12: BI/ETL, anulada e usada somente como caso de controle de ambiguidade.

Os enunciados oficiais não foram copiados para as 420 questões autorais. A resolução ocorre no PDF original e usa o gabarito pós-recursos e as decisões oficiais.

## Resultado da verificação mecânica

O verificador `tools/audit_semana03.py` confere contagens, IDs, quatro alternativas, quatro análises, metadados, usos, âncoras, tabelas, sequência de respostas, equilíbrio por nível, comandos negativos, títulos das filas, links, carga e regras discursivas. A execução final deve produzir `OK` sem exceção não documentada.

Na execução final, o verificador retornou:

```text
OK: estrutura integral da Semana 3 validada.
Banco: 300 principais + 120 extras; níveis principais=180/107/13; extras=82/36/2.
Super simulado: 60 itens; níveis=43/14/3.
Equilíbrio por nível no super: M=10/11/11/11; D=4/3/3/4; MD=1/1/1/0.
Alertas formais brutos de comprimento: banco=92; super=0.
```

Os 92 sinais brutos do banco não permaneceram como pista não analisada: a auditoria semântica reescreveu os conjuntos em que a forma entregava a chave, e os casos restantes possuem justificativa individual de precisão técnica no próprio comentário. Não se alongaram distratores apenas para igualar caracteres.

| Item canônico | Resultado |
|---|---|
| Nota da rubrica | 98/100 |
| Critérios eliminatórios encontrados após correção | 0 |
| Questões principais / extras | 300 / 120 |
| Médio / Difícil / Muito difícil — banco | 262 / 143 / 15 |
| Gabaritos / comentários / referências válidas | 420 / 420 / 420 |
| Super simulado e distribuição | 60 — 43 / 14 / 3 |
| Alternativas E | 0 |
| Questões órfãs de teoria | 0 |
| Gabaritos divergentes | 0 |
| Motivos repetidos ou trincas | 0 |
| Alertas formais de comprimento/alinhamento | 92 no banco, todos revisados e justificados; 0 no super |
| Principais e extras cobertas / parciais / não cobertas / antecipadas / inadequadas / ambíguas | 420 / 0 / 0 / 0 / 0 / 0 |
| Nível superestimado / subestimado após correção | 0 / 0 |
| Conteúdo novo no Bloco 6 | 0 |
| Referências futuras ou superficiais | 0 |
| Sessões acima da carga | 0 |
| Itens revisados / novos / substituídos / removidos | 420 / 420 / 0 / 0 |
| Status final | **Material aprovado para execução** |

## Rubrica canônica

| Dimensão | Máximo | Nota | Evidência |
|---|---:|---:|---|
| Fidelidade ao edital e às fontes | 15 | 15 | itens 6–8 rastreados; edital, documentação dos fornecedores e amostra oficial conferidos |
| Cobertura e profundidade da teoria | 20 | 20 | conceitos, contrastes, prática, pegadinhas e 26 recortes do edital cobertos antes das questões |
| Exemplos e prática guiada | 15 | 14 | 91 exemplos completos e produtos diários; alguns detalhes menores são tratados dentro de casos integrados |
| Alinhamento entre estudo e questões | 15 | 15 | 420 itens cobertos, títulos de filas sincronizados e zero questão órfã |
| Qualidade das questões | 15 | 14 | resposta única, níveis recalibrados, distratores revistos e equilíbrio A–D; a amostra oficial específica é útil, porém pequena |
| Qualidade dos comentários | 15 | 15 | 480 comentários com A–D, conceito, pegadinha, estratégia e referência |
| Organização e uso pedagógico | 5 | 5 | jornada de 6h, pontos de parada, filas espaçadas, discursiva e navegação validados |
| **Total** | **100** | **98** | **Material aprovado para execução** |

## Pendências operacionais

- executar as filas D0 e registrar confiança de 0 a 3;
- cumprir D+2, D+7 e D+21 dentro dos blocos previstos;
- preencher o caderno de erros e reescrever o trecho discursivo mais fraco;
- resolver os dois itens oficiais válidos e analisar o item anulado sem contabilizá-lo como acerto;
- executar o super sem consulta e corrigi-lo em sessão posterior;
- registrar tempo e desempenho por assunto.

Essas pendências não reprovam a produção; elas impedem apenas o status `Concluído`.
