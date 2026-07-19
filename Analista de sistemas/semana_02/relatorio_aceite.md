# Relatório de Aceite - Semana 2 - Analista de Sistemas

Data da auditoria: **19/07/2026**.

## Veredito

| Aceite | Resultado |
|---|---|
| Produção | **Aprovado - 90/100, sem falha eliminatória detectada** |
| Status autorizado | **Material aprovado para execução** |
| Operacional | **Pendente da execução pelo candidato** |

O aceite registra produção, estrutura e consistência do lote. Não comprova horas estudadas, revisões, questões resolvidas nem desempenho do candidato.

## Inventário

| Componente | Resultado |
|---|---:|
| Dias de estudo | 6 |
| Questões principais | 300 |
| Questões extras | 120 |
| Banco semanal | 420 |
| Comentários A-D | 420 |
| Super simulado | 60 |
| Comentários A-D do super | 60 |
| Alternativas E | 0 |

## Distribuição

| Conjunto | Médio | Difícil | Muito difícil | Total |
|---|---:|---:|---:|---:|
| Banco semanal | 168 | 168 | 84 | 420 |
| Super simulado | 24 | 24 | 12 | 60 |

No banco, cada dia possui 15 Essenciais, 25 de Aprofundamento, 15 de Revisão e 15 de Simulado.

## Validações

- identificadores principais contínuos de S2D1Q001 a S2D6Q300;
- 120 extras preservadas e classificadas;
- quatro alternativas por item e quatro análises por comentário;
- nível e uso sincronizados entre item e comentário;
- referências do banco e do super simulado apontando para âncoras existentes;
- ausência de três gabaritos iguais consecutivos;
- comentários genéricos legados do super simulado removidos;
- 60 itens do super simulado individualizados e ligados à teoria;
- `git diff --check` sem erro;
- auditoria reproduzível por `python tools/audit_semana02.py`.

## Perfil da banca e questões oficiais

O lote segue `../planejamento/perfil_banca_consulplan.md`. A matriz 20/20/10 e 8/8/4 é pedagógica e não é apresentada como estatística oficial da banca.

A busca por questões reais está registrada em `../questoes_oficiais/semana_02.md`. Nenhum item foi chamado de oficial sem caderno e gabarito definitivo verificáveis.

## Rubrica

| Critério | Máximo | Nota | Evidência |
|---|---:|---:|---|
| Fidelidade ao edital e cobertura | 15 | 14 | redes, segurança e SO vinculados ao programa; nova conferência oficial ainda será necessária se houver retificação |
| Teoria, exemplos e aplicação | 15 | 14 | seis dias extensos, exemplos, prática e mapas |
| Qualidade e calibração das questões | 20 | 17 | banco completo e consistente; faltam dados empíricos de aplicação |
| Comentários, gabaritos e referências | 15 | 14 | estrutura A-D integral e referências válidas |
| Jornada e revisão | 10 | 9 | carga e revisões presentes; execução real ainda pendente |
| Aderência documentada à Consulplan | 10 | 8 | contrato aplicado; amostra oficial específica de TI ainda não confirmada |
| Português, discursiva e caderno de erros | 5 | 5 | revisão e recuperação integradas |
| Organização, integridade e automação | 10 | 9 | arquivos navegáveis e auditoria reproduzível |
| **Total** | **100** | **90** | **Material aprovado para execução** |

## Limites e pendências operacionais

- resolver as filas D0 e registrar confiança;
- executar D+2, D+7 e D+21;
- preencher o caderno de erros;
- resolver o super simulado sem consulta;
- registrar tempo e desempenho por assunto;
- incorporar questões oficiais quando houver fonte verificável.

Até essas etapas serem cumpridas, o material não recebe o status `Concluído`.
