# Dia 5 — Transações, concorrência, integridade, segurança e recuperação

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais — S3D5Q201 a S3D5Q250

### S3D5Q201 — Unidade lógica de trabalho

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transferência exige débito em A e crédito em B. Qual delimitação atende ao conceito de transação?

A) Cada `UPDATE` deve ser confirmado isoladamente, porque atua em linha distinta.

B) A consulta do saldo e todos os relatórios posteriores devem entrar obrigatoriamente na mesma transação.

C) Débito e crédito devem integrar uma única unidade lógica, confirmada somente se o conjunto for válido.

D) O limite deve ser escolhido pela quantidade de comandos, não pelo requisito de negócio.

### S3D5Q202 — Savepoint e confirmação

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transação cria um `SAVEPOINT`, executa mais dois comandos e faz rollback até esse ponto. Ainda não houve `COMMIT`. Assinale a interpretação correta.

A) Tudo o que antecede o savepoint já é durável.

B) O rollback até o ponto confirma automaticamente o trecho preservado.

C) O savepoint cria uma segunda transação independente.

D) O trecho preservado continua pertencendo à transação ativa e depende de commit.

### S3D5Q203 — Último comando concluído

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

O último `UPDATE` de uma transação terminou e retornou “1 linha afetada”, mas a confirmação ainda não se tornou definitiva. No modelo didático, a transação pode estar:

A) parcialmente confirmada, sem que a mensagem do comando prove durabilidade.

B) confirmada, porque qualquer mensagem de sucesso equivale a commit.

C) abortada, pois o último comando já foi executado.

D) encerrada, ainda que o contexto transacional permaneça aberto.

### S3D5Q204 — Atomicidade e consistência

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Um débito foi executado, o crédito correspondente falhou e nenhuma parte deve permanecer. Qual associação é tecnicamente adequada?

A) Isolamento exige o rollback; durabilidade preserva o total.

B) Atomicidade impede o efeito parcial; consistência descreve a preservação do estado válido.

C) Consistência desfaz comandos; isolamento define o saldo inicial.

D) Durabilidade impede o efeito parcial; atomicidade decide quem pode acessar.

### S3D5Q205 — Início da durabilidade

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Em relação à durabilidade, qual evidência é necessária para tratar o resultado como permanente?

A) A decisão de commit concluída segundo o protocolo do SGBD.

B) A execução bem-sucedida de pelo menos um comando.

C) A criação de um savepoint antes da última escrita.

D) A existência de duas sessões lendo o mesmo valor.

### S3D5Q206 — Autocommit em operação composta

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma aplicação deixa o autocommit ativo e executa separadamente o débito e o crédito de uma transferência. O segundo comando falha. Qual risco foi criado?

A) Um `ROLLBACK` emitido depois da falha desfaz também o débito já confirmado pelo autocommit.

B) Nenhum; o autocommit agrupa comandos consecutivos por regra.

C) O autocommit cria um savepoint comum aos dois comandos, permitindo desfazer o conjunto.

D) O débito pode já estar confirmado, rompendo a atomicidade da operação composta.

### S3D5Q207 — Mapeamento das propriedades ACID

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Assinale a associação correta.

A) Atomicidade — ocultar dados de usuários sem privilégio.

B) Isolamento — controlar interferências concorrentes dentro da garantia escolhida.

C) Consistência — garantir que todas as sessões vejam sempre o mesmo instante.

D) Durabilidade — manter cópia histórica independente de toda transação.

### S3D5Q208 — Rollback após commit

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transação alcançou o estado confirmado. O usuário percebe depois que aplicou uma regra errada. O que se conclui?

A) Um savepoint anterior desfaz o commit já encerrado.

B) Basta emitir `ROLLBACK` na mesma conexão para apagar a confirmação.

C) A correção exige nova operação compensatória ou procedimento próprio; rollback simples não desfaz commit concluído.

D) O SGBD deve ignorar a confirmação porque a regra de negócio estava errada.

### S3D5Q209 — Consistência e regra de negócio

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma transferência atualiza as duas contas, mas a lógica soma R$ 100 em B e subtrai R$ 90 de A. Não existe restrição que represente o total. Qual diagnóstico é correto?

A) A atomicidade detectará sozinha a diferença de R$ 10.

B) O isolamento corrigirá a fórmula antes do commit.

C) A transação pode ser atômica e ainda produzir estado inconsistente, pois a regra foi implementada incorretamente.

D) A durabilidade impedirá o commit por ausência de backup.

### S3D5Q210 — Conexão perdida antes da confirmação

**Nível:** Muito difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

Uma aplicação recebeu sucesso no último comando, perdeu a conexão antes de obter evidência de commit e não sabe a decisão final. Qual conduta é mais segura?

A) Não tratar a mensagem do comando como prova; verificar o estado de negócio ou a decisão antes de repetir a operação.

B) Repetir imediatamente o débito, pois a transação necessariamente abortou.

C) Considerar o resultado confirmado, porque a conexão caiu depois do `UPDATE`.

D) Usar um novo savepoint na conexão encerrada para consultar a decisão.

### S3D5Q211 — Leitura suja

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 altera um valor; T2 lê esse valor; depois T1 aborta. O que T2 realizou?

A) Leitura fantasma.

B) Atualização perdida.

C) Leitura não repetível de valor confirmado.

D) Leitura suja, pois consumiu dado que nunca se confirmou.

### S3D5Q212 — Leitura não repetível

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 lê a linha do profissional 17. T2 altera essa mesma linha e confirma. T1 a relê e encontra outro valor. A anomalia é:

A) leitura suja.

B) leitura não repetível.

C) fantasma, obrigatoriamente.

D) deadlock.

### S3D5Q213 — Fantasma

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 conta pedidos pendentes e obtém 4. T2 insere outro pedido pendente e confirma. T1 repete o mesmo predicado e obtém 5. Trata-se de:

A) fantasma.

B) leitura suja.

C) atualização perdida.

D) starvation.

### S3D5Q214 — Atualização perdida

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

O estoque é 10. T1 lê 10 e calcula 8; T2 lê 10 e calcula 7. T1 grava 8 e T2 grava 7. Qual conclusão é correta?

A) O resultado 7 equivale às duas vendas em qualquer ordem serial.

B) Houve leitura suja porque T2 leu 10.

C) A escrita de T2 eliminou o efeito de T1; o resultado serial esperado seria 5.

D) O fenômeno é fantasma, pois o estoque mudou.

### S3D5Q215 — Significado de serializável

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Duas transações têm operações intercaladas, mas o efeito final equivale integralmente à ordem serial T2 seguida de T1. Essa execução:

A) não pode ser serializável, porque houve intercalação.

B) pode ser serializável, pois equivalência de efeito não exige execução física uma por vez.

C) é necessariamente Read Uncommitted.

D) prova ausência de qualquer rollback possível.

### S3D5Q216 — Read Committed no modelo clássico

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Na tabela conceitual do padrão SQL usada no estudo, o nível Read Committed:

A) admite leitura suja, mas impede fantasma.

B) impede toda anomalia de leitura.

C) impede leitura suja, mas pode admitir leitura não repetível e fantasma.

D) impede leitura não repetível e admite apenas atualização perdida.

### S3D5Q217 — Repeatable Read no modelo clássico

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Considerando somente a referência conceitual clássica, Repeatable Read:

A) permite leitura suja e impede fantasma.

B) impede apenas atualização perdida.

C) é idêntico a Read Uncommitted.

D) impede leitura suja e não repetível, mas o fantasma ainda pode ocorrer.

### S3D5Q218 — Locks compartilhado e exclusivo

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Qual afirmação resume corretamente os locks apresentados?

A) Todo lock compartilhado bloqueia qualquer outra leitura.

B) Lock exclusivo é usado apenas para autenticar o usuário.

C) Locks compartilhados podem admitir leituras compatíveis; lock exclusivo protege escrita contra acessos incompatíveis.

D) A granularidade de lock é sempre a tabela inteira.

### S3D5Q219 — Limites do MVCC

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Sobre MVCC, assinale a alternativa correta.

A) Elimina locks de escrita e todos os conflitos entre escritores.

B) Garante que qualquer leitor veja sempre a versão mais recente.

C) Pode permitir snapshot consistente a leitores, mas não elimina conflito entre escritas incompatíveis.

D) Dispensa gestão e limpeza de versões em qualquer produto.

### S3D5Q220 — Ciclo de espera

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 mantém lock em A e espera B. T2 mantém lock em B e espera A. Qual ação e diagnóstico são compatíveis?

A) Há deadlock; o SGBD pode escolher uma vítima, desfazê-la e liberar recursos.

B) Há somente espera normal; ambas necessariamente concluirão sem intervenção.

C) Há starvation sem ciclo; conceder mais locks resolve.

D) Há leitura suja; basta elevar para Read Committed.

### S3D5Q221 — Espera transitória

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T2 espera um lock mantido por T1, mas T1 não espera nenhum recurso de T2 e pode confirmar. Esse quadro caracteriza, por si só:

A) deadlock de dois vértices.

B) bloqueio normal ou espera transitória, sem ciclo demonstrado.

C) atualização perdida já consumada.

D) livelock obrigatório.

### S3D5Q222 — Starvation

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Uma transação é repetidamente preterida e permanece sem obter o recurso, embora não exista ciclo fixo de espera. O fenômeno é:

A) starvation.

B) leitura fantasma.

C) deadlock, necessariamente.

D) durabilidade.

### S3D5Q223 — Prevenção de deadlock

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Duas rotinas alteram sempre os mesmos pares de unidades. Qual medida reduz a chance de deadlock sem proibir toda concorrência?

A) Aumentar indefinidamente a duração das transações.

B) Fazer cada rotina escolher ordem aleatória de locks.

C) Substituir locks por permissões administrativas.

D) Adquirir os recursos em uma ordem global consistente e manter a transação curta.

### S3D5Q224 — Serial e concorrente

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Qual proposição distingue corretamente execução serial e concorrente?

A) Concorrente significa que nenhuma operação pode esperar.

B) Serializável significa que as operações nunca se intercalam.

C) Execução serial termina uma transação antes de iniciar outra; a concorrente pode intercalar e ainda produzir resultado aceitável.

D) Execução serial exige MVCC e a concorrente exige apenas lock exclusivo.

### S3D5Q225 — Snapshot não é visão mais recente

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 lê um snapshot consistente enquanto T2 confirma uma alteração. A leitura de T1 não mostra imediatamente a nova versão. Isso prova falha do MVCC?

A) Sim, porque consistência exige sempre a versão mais nova.

B) Sim, porque todo commit invalida snapshots existentes.

C) Não; snapshot consistente pode preservar uma visão anterior conforme a garantia, sem prometer máxima atualidade.

D) Não; MVCC torna todas as escritas incompatíveis invisíveis para sempre.

### S3D5Q226 — Duração e contenção

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Por que uma transação longa tende a aumentar contenção?

A) Porque a duração, por si só, transforma qualquer espera unilateral em deadlock.

B) Porque todo SGBD eleva obrigatoriamente os locks para a tabela depois de um tempo fixo.

C) Porque os recursos são liberados ao fim de cada comando, o que impede espera entre transações.

D) Porque retém recursos e amplia a janela em que outras operações podem bloquear ou formar ciclos.

### S3D5Q227 — Nova tentativa da vítima

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Após detectar deadlock, o SGBD aborta T2. Qual tratamento de aplicação é adequado?

A) Registrar o evento e refazer T2 de modo controlado, considerando idempotência e possível repetição do conflito.

B) Considerar que T2 confirmou parcialmente porque chegou a obter locks.

C) Repetir indefinidamente sem limite, espera ou verificação.

D) Forçar T1 e T2 a cometerem para preservar todas as escritas.

### S3D5Q228 — Mesma linha ou novo membro

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

T1 primeiro relê a mesma linha e encontra valor alterado por T2; depois repete um predicado e encontra linha nova inserida por T3. As anomalias, na ordem, são:

A) leitura suja e atualização perdida.

B) leitura não repetível e fantasma.

C) fantasma e leitura não repetível.

D) deadlock e starvation.

### S3D5Q229 — Operação atômica sobre valor corrente

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Para reduzir o risco de duas vendas calcularem estoque a partir da mesma base desatualizada, qual ideia está alinhada ao estudo?

A) Ler em duas sessões e aceitar a última gravação.

B) Encerrar a transação logo após a leitura e gravar depois, sem validar se o estoque mudou.

C) Repetir o mesmo ciclo de ler, calcular e sobrescrever após conflito, sem versão ou trava apropriada.

D) Usar mecanismo que detecte conflito, validação de versão ou atualização atômica apropriada sobre o valor corrente.

### S3D5Q230 — Serializable e aborto

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

Uma transação em Serializable é abortada pelo SGBD devido a conflito de serialização. A melhor interpretação é:

A) O nível falhou, pois Serializable deve confirmar toda transação.

B) O produto executou necessariamente todas as transações uma por vez.

C) O aborto pode ser o mecanismo usado para impedir um resultado sem ordem serial equivalente.

D) O evento prova leitura suja confirmada.

### S3D5Q231 — Integridade de entidade

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Qual controle atende diretamente à integridade de entidade?

A) `GRANT SELECT` para a equipe de relatório.

B) Chave primária única e não nula para identificar cada linha.

C) Log de auditoria das exclusões.

D) Parâmetro preparado para o valor de login.

### S3D5Q232 — Integridade referencial

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma coluna `pagamento.profissional_id` deve apontar para profissional existente, salvo quando a relação puder ser nula. O controle central é:

A) chave estrangeira com a regra de nulidade apropriada.

B) role com privilégio de escrita.

C) checkpoint periódico.

D) lock compartilhado.

### S3D5Q233 — Integridade de domínio

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Impedir que o percentual receba 130 quando a faixa válida é de 0 a 100 é exemplo de:

A) integridade de domínio, implementável por tipo e `CHECK` adequados.

B) autenticação multifator.

C) isolamento serializável.

D) auditoria de comando.

### S3D5Q234 — Autenticação e autorização

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma usuária prova sua identidade, mas recebe somente leitura em uma view. Isso significa que:

A) a autorização falhou, porque autenticados devem escrever.

B) autenticação respondeu quem ela é; autorização limitou o que pode fazer.

C) a integridade referencial substituiu a permissão.

D) o MVCC retirou os privilégios de escrita.

### S3D5Q235 — Finalidade da auditoria

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Qual pergunta é respondida prioritariamente pela auditoria?

A) O valor pertence ao domínio permitido?

B) A transação é equivalente a uma execução serial?

C) Quem fez qual ação, quando e sobre qual objeto?

D) A chave estrangeira aponta para um pai existente?

### S3D5Q236 — Menor privilégio no relatório

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

A equipe precisa somente de totais por unidade e não deve ver CPF nem alterar registros. Qual desenho melhor aplica menor privilégio?

A) Conceder poderes administrativos e ocultar botões na interface.

B) Dar `SELECT` e `UPDATE` em todas as tabelas para evitar erros de permissão.

C) Compartilhar a conta do DBA somente durante o expediente.

D) Conceder a uma role `SELECT` sobre view limitada aos dados necessários, sem acesso direto mais amplo.

### S3D5Q237 — Efeito de REVOKE

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Foi executado `REVOKE SELECT` de uma concessão direta, mas o usuário continua consultando a tabela. Qual hipótese é compatível?

A) `REVOKE` aumenta privilégios antes de removê-los.

B) O acesso pode vir de outra role, herança, propriedade ou concessão ainda válida.

C) Toda consulta já aberta concede leitura permanente.

D) A chave primária substitui o privilégio revogado.

### S3D5Q238 — View e exposição residual

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Conceder `SELECT` em uma view sem CPF reduz exposição somente se:

A) a view usar `ORDER BY`.

B) o usuário também receber acesso administrativo à tabela base.

C) o CPF estiver apenas oculto pela interface da aplicação.

D) não houver outro privilégio direto mais amplo que permita contornar a view.

### S3D5Q239 — Valor parametrizado

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

A entrada de login contém `' OR 1=1 --`. Em uma API parametrizada corretamente, essa entrada:

A) é transmitida como valor e não passa a compor a estrutura lógica da instrução.

B) concede automaticamente a role pública.

C) vira nome de tabela seguro.

D) obriga o SGBD a desabilitar autorização.

### S3D5Q240 — Identificador dinâmico

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma tela permite escolher a coluna de ordenação. Por que não basta tratá-la como parâmetro de valor?

A) Porque parâmetros só aceitam números.

B) Porque toda ordenação dinâmica é proibida.

C) Porque nomes de coluna integram a estrutura; devem ser escolhidos por lista permitida e composição própria do produto.

D) Porque `ORDER BY` elimina injeção por definição.

### S3D5Q241 — Parâmetro não substitui autorização

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

Uma aplicação usa parâmetros em todas as consultas, mas sua conta possui privilégios administrativos desnecessários. Qual avaliação é correta?

A) O uso de parâmetros converte a conta em menor privilégio.

B) A autorização torna desnecessária a parametrização.

C) A injeção por valores foi reduzida, mas a superfície de dano continua ampliada pelos privilégios excessivos.

D) Privilégio administrativo impede qualquer entrada maliciosa.

### S3D5Q242 — Princípio write-ahead

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Qual ordem expressa o princípio write-ahead?

A) O registro de log pertinente deve alcançar armazenamento durável antes da página de dados correspondente ser considerada persistida.

B) A página de dados deve ser gravada e só depois o log pode registrar o evento.

C) O checkpoint substitui todos os registros anteriores antes de qualquer commit.

D) O backup deve ser concluído antes de cada `UPDATE`.

### S3D5Q243 — Função de redo

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

T1 confirmou, mas sua página ainda não refletia a alteração persistida quando houve queda. Na recuperação, a operação típica é:

A) undo de T1.

B) redo de T1, se necessário.

C) revogação dos privilégios de T1.

D) rollback de todo o checkpoint.

### S3D5Q244 — Função de undo

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

T2 alterou uma página, mas não confirmou antes da queda. Se o efeito não confirmado chegou ao armazenamento, a recuperação deve:

A) preservá-lo por durabilidade.

B) tratá-lo como backup mais recente.

C) transformá-lo em commit implícito.

D) desfazê-lo ou neutralizá-lo por undo, conforme o algoritmo.

### S3D5Q245 — Limites do checkpoint

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Assinale a interpretação correta do checkpoint.

A) Confirma automaticamente todas as transações ativas.

B) Garante que todas as páginas foram copiadas ao mesmo instante.

C) Substitui o log e a cópia autônoma.

D) Marca coordenação que reduz trabalho de recuperação, sem ser commit global nem prova isolada de confirmação.

### S3D5Q246 — Recuperação integrada

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Antes da queda, T1 confirmou e T2 não confirmou. Algumas páginas de ambas foram gravadas. Qual estado final é exigido?

A) Manter tudo que chegou à página, pois escrita física supera o log.

B) Desfazer T1 e confirmar T2 para equilibrar o sistema.

C) Garantir T1, com redo se necessário, e remover efeitos de T2, com undo se necessário.

D) Desfazer tudo desde o último checkpoint, sem consultar decisões.

### S3D5Q247 — Primeira fase do 2PC

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Na primeira fase do commit em duas fases, o coordenador:

A) solicita preparo e cada participante registra o necessário e vota se pode confirmar.

B) manda cada participante decidir sozinho entre commit e rollback.

C) replica automaticamente todos os dados entre os nós.

D) libera todos os recursos antes de conhecer os votos.

### S3D5Q248 — Decisão global no 2PC

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Três participantes votam “preparado”. No fluxo normal do 2PC, qual decisão pode ser tomada pelo coordenador?

A) Cada participante escolhe uma decisão local diferente.

B) Commit global, registrado e comunicado aos participantes.

C) Rollback obrigatório, porque unanimidade indica conflito.

D) Conversão da operação em replicação assíncrona.

### S3D5Q249 — Participante preparado e coordenador indisponível

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

A e B votaram preparado, mas o coordenador ficou indisponível antes de divulgar a decisão. Qual risco específico aparece?

A) Leitura suja inevitável em todos os bancos.

B) Os participantes podem ficar aguardando a decisão global e manter recursos, causando bloqueio.

C) Cada participante deve confirmar imediatamente para aumentar disponibilidade.

D) O log deixa de ser necessário porque houve voto.

### S3D5Q250 — O que o 2PC não oferece

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

Qual afirmação avalia corretamente o 2PC?

A) Busca atomicidade entre participantes, mas não replica dados nem garante maior disponibilidade ou velocidade.

B) Torna toda transação distribuída não bloqueante.

C) Substitui autorização, log local e controle de concorrência.

D) Permite commit parcial quando um participante não prepara.

## Questões extras — Dia 5

#### Extra Dia 5.1 — Lei e base da profissão

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Lei nº 4.769/1965
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Ao identificar no enunciado a disciplina e a base legal da profissão, qual fonte deve ser examinada primeiro?

A) Lei nº 4.769/1965.

B) RN CFA nº 651/2024.

C) RN CFA nº 671/2025.

D) Histórico de navegação do portal.

#### Extra Dia 5.2 — Regulamentação da lei

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Decreto nº 61.934/1967
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual instrumento foi associado à regulamentação da Lei nº 4.769/1965?

A) Código de Ética de 2025.

B) Regimento Interno do CRA-PR.

C) Decreto nº 61.934/1967.

D) Certificado digital do portal.

#### Extra Dia 5.3 — Organização interna do CRA-PR

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 651/2024
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Uma questão trata de órgãos e competências internas do CRA-PR. A primeira fonte do recorte é:

A) Lei nº 4.769/1965 apenas, sem consultar o regimento.

B) RN CFA nº 651/2024.

C) RN CFA nº 671/2025.

D) Decreto nº 61.934/1967 como se fosse o regimento interno.

#### Extra Dia 5.4 — Dever e sanção ética

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 671/2025
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Para item sobre dever, sigilo, infração ou sanção ética no recorte, deve-se identificar sujeito e conduta e consultar prioritariamente:

A) a Lei nº 4.769/1965, tratando-a como fonte única mesmo para a conduta ética específica.

B) a RN CFA nº 651/2024, voltada ao recorte de organização interna do CRA-PR.

C) o Decreto nº 61.934/1967, por regulamentar a lei de base da profissão.

D) a RN CFA nº 671/2025, após identificar o sujeito, a conduta e a consequência ética aplicável.

#### Extra Dia 5.5 — CFA nacional e CRA regional

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Âmbito de competência
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual divisão de atuação é compatível com a revisão?

A) O CRA-PR exerce toda orientação normativa nacional porque fiscaliza no Paraná.

B) O CFA orienta o sistema dentro da competência normativa; o CRA-PR registra e fiscaliza em sua jurisdição.

C) O CFA executa sozinho toda diligência local no Paraná.

D) Autonomia regional elimina a integração ao sistema.

#### Extra Dia 5.6 — Resolução posterior e lei

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Hierarquia normativa
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Uma resolução administrativa posterior contradiz diretamente a Lei nº 4.769/1965. Qual conclusão decorre do método estudado?

A) A resolução não afasta a lei apenas por ser mais recente; hierarquia e competência devem ser respeitadas.

B) A resolução revoga automaticamente a lei por critério cronológico.

C) O CRA-PR escolhe livremente a norma mais conveniente.

D) As duas fontes viram recomendações sem força.

#### Extra Dia 5.7 — Autonomia sem ruptura

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Autonomia regional
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

A autonomia regional do CRA-PR permite:

A) contrariar lei federal em matéria profissional.

B) substituir toda orientação nacional do CFA.

C) atuar fora de sua jurisdição sempre que houver interesse.

D) organizar e exercer suas competências próprias sem romper limites e normas superiores.

#### Extra Dia 5.8 — Roteiro de leitura institucional

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Método de resolução
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual roteiro reduz melhor o erro em casos institucionais?

A) Objeto → norma mais recente → conclusão, sem conferir hierarquia ou competência.

B) Território → órgão regional → atribuição de todas as funções, sem separar fonte e limite.

C) Objeto → fonte → sujeito → território → verbo de competência → limite.

D) Fonte → sanção → sujeito, sem verificar território nem verbo de competência.

#### Extra Dia 5.9 — Publicidade e sigilo

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Limites de transparência
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Qual formulação preserva o equilíbrio apresentado?

A) Publicidade institucional autoriza divulgar qualquer dado pessoal.

B) Sigilo permite omitir toda prestação de contas.

C) A publicidade não elimina sigilo legal ou proteção de dados, e o sigilo não extingue toda transparência devida.

D) Transparência e sigilo são incompatíveis em qualquer caso.

#### Extra Dia 5.10 — Caso integrado de competência

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, território e verbo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Um fato fiscalizatório ocorre no Paraná e envolve possível infração ética. Qual caminho é tecnicamente mais responsável?

A) Aplicar só a lei de criação e ignorar a conduta ética.

B) Identificar sujeito e conduta na norma ética e a atuação fiscalizatória do CRA-PR em sua jurisdição, sem atribuir-lhe toda competência normativa nacional.

C) Transferir automaticamente a diligência local ao CFA porque a norma é nacional.

D) Usar o regimento interno para afastar lei e código de ética.

#### Extra Dia 5.11 — Partes de uma URL

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** URL
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Em `https://portal.exemplo.br/servicos?id=7#prazo`, qual decomposição está correta?

A) `https` é host; `portal.exemplo.br` é fragmento.

B) `/servicos` é consulta; `id=7` é esquema.

C) `prazo` é caminho e `https` é cookie.

D) `https` é esquema; `portal.exemplo.br` é host; `/servicos` é caminho; `id=7` é consulta; `prazo` é fragmento.

#### Extra Dia 5.12 — Alcance do HTTPS

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** HTTPS e certificado
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

O cadeado de HTTPS permite concluir que:

A) o trânsito está protegido e o servidor é autenticado conforme a cadeia, mas o conteúdo e a intenção do site não se tornam automaticamente confiáveis.

B) a instituição dona da marca controla necessariamente o domínio acessado.

C) qualquer oferta exibida é legítima.

D) a conexão é anônima para provedor e site.

#### Extra Dia 5.13 — Cache, cookie, histórico e download

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Artefatos de navegação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Assinale a associação correta.

A) Cache registra apenas a lista cronológica de páginas; histórico acelera conteúdo.

B) Cache guarda cópia para acelerar; cookie mantém estado ou preferência; histórico registra navegação; download grava arquivo.

C) Cookie cifra todo o tráfego; download mantém sessão.

D) Histórico autentica certificado; cache concede anonimato.

#### Extra Dia 5.14 — Navegação privada

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Privacidade local e rede
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Sobre navegação privada, assinale a alternativa correta.

A) Torna o computador invisível ao site.

B) Impede a organização de observar tráfego de sua rede.

C) Substitui VPN e autenticação.

D) Reduz certos registros locais da sessão, mas não cria anonimato perante rede, provedor, organização ou site.

#### Extra Dia 5.15 — Domínio parecido com cadeado

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Phishing e verificação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

Um link leva a domínio parecido com o oficial, com certificado válido, e pede credencial. Qual conduta é adequada?

A) Não inserir a senha; conferir host completo, origem do link e canal oficial, pois o certificado pode autenticar o domínio falso acessado.

B) Inserir a senha porque o cadeado prova a titularidade institucional.

C) Confiar se as cores e o logotipo forem idênticos.

D) Ativar navegação privada e prosseguir, pois ela valida o destinatário.

#### Extra Dia 5.16 — Referente inequívoco

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coesão referencial
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Em “A administração explicou os critérios aos cidadãos, pois eles eram incompletos”, qual reescrita elimina a ambiguidade pretendendo afirmar que os critérios eram incompletos?

A) A administração explicou-os aos cidadãos, pois eles eram incompletos.

B) A administração explicou os critérios aos cidadãos, pois estes eram incompletos.

C) A administração explicou aos cidadãos os critérios utilizados, pois tais critérios eram incompletos.

D) A administração explicou aos cidadãos, pois os mesmos eram incompletos.

#### Extra Dia 5.17 — Relação do conector

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coerência entre orações
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

A frase deve admitir um benefício e, apesar dele, introduzir um risco. Qual conector realiza essa relação?

A) Portanto.

B) Porque.

C) Assim.

D) Embora.

#### Extra Dia 5.18 — Paralelismo em enumeração

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Paralelismo sintático
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Qual enumeração mantém paralelismo?

A) O plano exige medir resultados, transparência e que se protejam dados.

B) O plano exige medir resultados, explicar critérios e proteger dados.

C) O plano exige medição de resultados, explicar critérios e dados protegidos.

D) O plano exige que os resultados sejam medidos, transparência e proteger dados.

#### Extra Dia 5.19 — Força de termos absolutos

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Modalização
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Os dados disponíveis mostram melhoria em alguns serviços, sem controlar todas as variáveis. Qual conclusão tem força compatível?

A) O uso responsável de dados pode contribuir para melhorar serviços, desde que qualidade e contexto sejam avaliados.

B) Dados sempre eliminam ineficiência.

C) A melhoria prova que dados nunca geram riscos.

D) Qualquer coleta causa necessariamente o mesmo resultado.

#### Extra Dia 5.20 — Arquitetura do plano integral

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Planejamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

Qual plano atende ao treino sobre uso responsável de dados em serviços públicos?

A) Introdução sem tese; dois exemplos técnicos; conclusão com argumento novo.

B) Tese absoluta de que dados eliminam riscos; um desenvolvimento; lista de ferramentas.

C) Definições de SQL e índices, sem relação compreensível com o tema geral.

D) Problema e tese condicionada; desenvolvimento sobre benefício e qualidade; desenvolvimento sobre risco, transparência e proteção; conclusão que reformula a tese sem argumento novo.

## Gabarito — Dia 5

### Principais

| S3D5Q201 | S3D5Q202 | S3D5Q203 | S3D5Q204 | S3D5Q205 | S3D5Q206 | S3D5Q207 | S3D5Q208 | S3D5Q209 | S3D5Q210 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | D | A | B | A | D | B | C | C | A |

| S3D5Q211 | S3D5Q212 | S3D5Q213 | S3D5Q214 | S3D5Q215 | S3D5Q216 | S3D5Q217 | S3D5Q218 | S3D5Q219 | S3D5Q220 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | B | A | C | B | C | D | C | C | A |

| S3D5Q221 | S3D5Q222 | S3D5Q223 | S3D5Q224 | S3D5Q225 | S3D5Q226 | S3D5Q227 | S3D5Q228 | S3D5Q229 | S3D5Q230 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | A | D | C | C | D | A | B | D | C |

| S3D5Q231 | S3D5Q232 | S3D5Q233 | S3D5Q234 | S3D5Q235 | S3D5Q236 | S3D5Q237 | S3D5Q238 | S3D5Q239 | S3D5Q240 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | A | A | B | C | D | B | D | A | C |

| S3D5Q241 | S3D5Q242 | S3D5Q243 | S3D5Q244 | S3D5Q245 | S3D5Q246 | S3D5Q247 | S3D5Q248 | S3D5Q249 | S3D5Q250 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | B | D | D | C | A | B | B | A |

### Extras

| 5.1 | 5.2 | 5.3 | 5.4 | 5.5 | 5.6 | 5.7 | 5.8 | 5.9 | 5.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | C | B | D | B | A | D | C | C | B |

| 5.11 | 5.12 | 5.13 | 5.14 | 5.15 | 5.16 | 5.17 | 5.18 | 5.19 | 5.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | A | B | D | A | C | D | B | A | D |

## Comentários — Dia 5

### Comentário S3D5Q201

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Separa a unidade em commits incompatíveis com a obrigação única.
- **B)** Incorreta. Inclui relatórios independentes sem necessidade.
- **C)** Correta. Une débito e crédito conforme o requisito lógico.
- **D)** Incorreta. Usa quantidade de comandos como critério, o que é incorreto.

**Conceito:** Transação como unidade lógica.

**Pegadinha:** Tomar comando isolado como fronteira automática.

**Como pensar:** Identifique o conjunto que só é válido quando concluído por inteiro.

### Comentário S3D5Q202

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Savepoint não gera durabilidade.
- **B)** Incorreta. Rollback parcial não confirma o trecho preservado.
- **C)** Incorreta. Não nasce uma transação independente.
- **D)** Correta. O trecho continua ativo e depende do commit.

**Conceito:** Savepoint e rollback parcial.

**Pegadinha:** Confundir ponto de retorno com commit.

**Como pensar:** Separe o que foi desfeito do que já foi confirmado.

### Comentário S3D5Q203

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É o estado didático compatível antes da confirmação definitiva.
- **B)** Incorreta. Mensagem de comando não equivale a commit.
- **C)** Incorreta. Não houve falha ou aborto informado.
- **D)** Incorreta. Encerramento exige commit ou aborto e liberação do contexto.

**Conceito:** Estados transacionais.

**Pegadinha:** Interpretar linha afetada como confirmação.

**Como pensar:** Procure a decisão de commit, não apenas o término do comando.

### Comentário S3D5Q204

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Troca atomicidade por isolamento.
- **B)** Correta. Atomicidade evita metade; consistência caracteriza o estado válido.
- **C)** Incorreta. Atribui a consistência o mecanismo de desfazimento.
- **D)** Incorreta. Durabilidade não decide acesso nem evita por si o efeito parcial.

**Conceito:** Atomicidade versus consistência.

**Pegadinha:** Escolher propriedade pela palavra “falha”.

**Como pensar:** Pergunte separadamente se ficou metade e se o estado final é válido.

### Comentário S3D5Q205

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A decisão confirmada inaugura a garantia de durabilidade.
- **B)** Incorreta. Comando bem-sucedido ainda pode estar em transação ativa.
- **C)** Incorreta. Savepoint não torna dados permanentes.
- **D)** Incorreta. Duas leituras não provam confirmação.

**Conceito:** Durabilidade após commit.

**Pegadinha:** Confundir execução com permanência.

**Como pensar:** Localize a fronteira da decisão transacional.

### Comentário S3D5Q206

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Rollback posterior não reabre nem desfaz automaticamente o commit já concluído pelo autocommit.
- **B)** Incorreta. Autocommit não agrupa comandos por proximidade.
- **C)** Incorreta. Autocommit não cria savepoint compartilhado entre comandos confirmados separadamente.
- **D)** Correta. O primeiro comando pode persistir sozinho e romper a atomicidade.

**Conceito:** Autocommit em operação composta.

**Pegadinha:** Acreditar que comandos consecutivos são uma unidade.

**Como pensar:** Desenhe um commit depois de cada comando e verifique o requisito.

### Comentário S3D5Q207

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Ocultação é segurança, não atomicidade.
- **B)** Correta. Isolamento controla interferências concorrentes dentro da garantia.
- **C)** Incorreta. Consistência não exige visão global instantânea.
- **D)** Incorreta. Durabilidade não é sinônimo de backup histórico.

**Conceito:** Propriedades ACID.

**Pegadinha:** Usar associação intuitiva em vez da definição.

**Como pensar:** Transforme cada propriedade em sua pergunta central.

### Comentário S3D5Q208

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Savepoint não sobrevive como desfazimento de commit encerrado.
- **B)** Incorreta. Rollback simples atua sobre transação ativa.
- **C)** Correta. Efeito confirmado exige nova correção ou compensação.
- **D)** Incorreta. O SGBD não invalida sozinho toda regra errada.

**Conceito:** Limite do rollback.

**Pegadinha:** Tratar rollback como reversão ilimitada.

**Como pensar:** Primeiro determine se a transação ainda está ativa.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Rollback após commit”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q209

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Atomicidade pode existir mesmo com fórmula errada.
- **B)** Incorreta. Isolamento não corrige regra de negócio.
- **C)** Correta. A operação inteira pode levar a estado semanticamente inválido.
- **D)** Incorreta. Durabilidade não depende de backup antes do commit.

**Conceito:** Consistência e lógica da transação.

**Pegadinha:** Supor que ACID descobre regras não representadas.

**Como pensar:** Teste integralidade e validade em etapas diferentes.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Consistência e regra de negócio”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q210

**Nível:** Muito difícil

**Uso:** Essenciais

**Referência:** [Transação, estados e propriedades ACID](semana_03_estudo.md#s3-d5-transacoes-acid).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A decisão desconhecida deve ser verificada antes de nova tentativa.
- **B)** Incorreta. A queda da conexão não prova aborto.
- **C)** Incorreta. Sucesso do update não prova commit.
- **D)** Incorreta. Savepoint não consulta decisão após perda da conexão.

**Conceito:** Resultado transacional incerto.

**Pegadinha:** Converter ausência de resposta em certeza.

**Como pensar:** Busque evidência idempotente do resultado antes de repetir.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Conexão perdida antes da confirmação”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q211

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Nenhum conjunto por predicado mudou.
- **B)** Incorreta. Não houve sobrescrita de escrita.
- **C)** Incorreta. O valor lido não chegou a ser confirmado.
- **D)** Correta. T2 consumiu dado de T1 que depois foi abortado.

**Conceito:** Leitura suja.

**Pegadinha:** Nomear toda mudança como não repetível.

**Como pensar:** Pergunte se o valor lido chegou a ser confirmado.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Leitura suja”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q212

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A alteração de T2 foi confirmada.
- **B)** Correta. A mesma linha mudou entre duas leituras de T1.
- **C)** Incorreta. Não houve nova linha no conjunto.
- **D)** Incorreta. Não existe ciclo de espera.

**Conceito:** Leitura não repetível.

**Pegadinha:** Confundir linha alterada com fantasma.

**Como pensar:** Sublinhe “mesma linha”.

### Comentário S3D5Q213

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Uma nova linha passou a satisfazer o mesmo predicado.
- **B)** Incorreta. O dado foi confirmado, portanto não é sujo.
- **C)** Incorreta. Nenhuma escrita foi apagada.
- **D)** Incorreta. Não há adiamento indefinido.

**Conceito:** Fantasma.

**Pegadinha:** Olhar apenas para a contagem.

**Como pensar:** Compare os membros do conjunto nas duas execuções.

### Comentário S3D5Q214

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. As duas reduções deveriam resultar em 5.
- **B)** Incorreta. O valor-base pode ser confirmado.
- **C)** Correta. A última escrita apagou a redução de T1.
- **D)** Incorreta. Não houve entrada ou saída de linha.

**Conceito:** Atualização perdida.

**Pegadinha:** Aceitar a última gravação como soma dos efeitos.

**Como pensar:** Calcule o resultado serial esperado e compare.

### Comentário S3D5Q215

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Intercalação não exclui equivalência serial.
- **B)** Correta. O efeito pode equivaler à ordem T2→T1.
- **C)** Incorreta. Não é possível inferir Read Uncommitted.
- **D)** Incorreta. Isolamento forte ainda pode exigir rollback.

**Conceito:** Serializabilidade.

**Pegadinha:** Confundir serial com serializável.

**Como pensar:** Avalie o efeito, não apenas a ordem física.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Significado de serializável”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q216

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Read Committed impede leitura suja no quadro clássico.
- **B)** Incorreta. Não impede todas as anomalias.
- **C)** Correta. É a linha conceitual correta, com ressalva de produto.
- **D)** Incorreta. Não repetível ainda pode ocorrer.

**Conceito:** Read Committed clássico.

**Pegadinha:** Importar comportamento de um fornecedor.

**Como pensar:** Identifique primeiro se a cobrança é conceitual ou específica.

### Comentário S3D5Q217

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Leitura suja não é admitida.
- **B)** Incorreta. O nível protege mais de uma anomalia.
- **C)** Incorreta. Não se iguala a Read Uncommitted.
- **D)** Correta. Impede suja e não repetível; fantasma pode ocorrer no modelo clássico.

**Conceito:** Repeatable Read clássico.

**Pegadinha:** Responder pelo produto sem ler o enquadramento.

**Como pensar:** Use a tabela conceitual quando o enunciado assim delimitar.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Repeatable Read no modelo clássico”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q218

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Compartilhados podem admitir leituras compatíveis.
- **B)** Incorreta. Lock não autentica usuário.
- **C)** Correta. Distingue leitura compatível e proteção de escrita.
- **D)** Incorreta. Granularidade não é sempre tabela.

**Conceito:** Locks compartilhado e exclusivo.

**Pegadinha:** Ler lock como bloqueio total.

**Como pensar:** Verifique recurso e compatibilidade da operação.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Locks compartilhado e exclusivo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q219

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. MVCC não elimina conflito entre escritores.
- **B)** Incorreta. Snapshot não garante máxima atualidade.
- **C)** Correta. Leitores podem ter visão consistente sem acabar com disputa de escrita.
- **D)** Incorreta. Versões ainda exigem gestão conforme o produto.

**Conceito:** MVCC e seus limites.

**Pegadinha:** Tratar MVCC como ausência de locks.

**Como pensar:** Separe leitor–escritor de escritor–escritor.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Limites do MVCC”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q220

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O grafo T1→T2→T1 contém ciclo e pode exigir rollback da vítima.
- **B)** Incorreta. A espera não é unilateral nem garantidamente transitória.
- **C)** Incorreta. Há ciclo, portanto não é apenas starvation.
- **D)** Incorreta. Nenhuma leitura suja foi descrita.

**Conceito:** Deadlock.

**Pegadinha:** Chamar todo bloqueio de deadlock ou ignorar o ciclo.

**Como pensar:** Desenhe as arestas de espera.

### Comentário S3D5Q221

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Falta aresta de retorno para ciclo.
- **B)** Correta. T1 pode terminar e liberar o recurso.
- **C)** Incorreta. Nenhuma sobrescrita ocorreu.
- **D)** Incorreta. Não há atividade repetida sem progresso.

**Conceito:** Espera normal.

**Pegadinha:** Inferir ciclo de uma única dependência.

**Como pensar:** Procure caminho que retorne à transação inicial.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Espera transitória”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q222

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Adiamento indefinido sem ciclo obrigatório é starvation.
- **B)** Incorreta. Fantasma altera conjunto de predicado.
- **C)** Incorreta. Deadlock precisaria de ciclo.
- **D)** Incorreta. Durabilidade não trata escalonamento de oportunidade.

**Conceito:** Starvation.

**Pegadinha:** Usar deadlock para todo atraso longo.

**Como pensar:** Pergunte se ninguém progride por ciclo ou se um participante é sempre preterido.

### Comentário S3D5Q223

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Transação longa amplia retenção.
- **B)** Incorreta. Ordem aleatória favorece inversões.
- **C)** Incorreta. Privilégios não resolvem espera por dados.
- **D)** Correta. Ordem global e curta duração reduzem formação de ciclo.

**Conceito:** Prevenção de deadlock.

**Pegadinha:** Aplicar segurança a problema de concorrência.

**Como pensar:** Impeça aquisições em ordens opostas.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Prevenção de deadlock”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q224

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Concorrência pode envolver espera.
- **B)** Incorreta. Serializável não proíbe intercalação física.
- **C)** Correta. A distinção usa término completo versus intercalação aceita.
- **D)** Incorreta. Mecanismos não definem por si os escalonamentos.

**Conceito:** Serial e concorrente.

**Pegadinha:** Confundir mecanismo com definição.

**Como pensar:** Defina a cronologia física antes da equivalência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Serial e concorrente”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q225

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Consistência do snapshot não implica dado mais novo.
- **B)** Incorreta. Commit alheio não torna todo snapshot falho.
- **C)** Correta. Uma visão anterior pode ser estável dentro da garantia.
- **D)** Incorreta. A invisibilidade não é permanente nem universal.

**Conceito:** Snapshot e atualidade.

**Pegadinha:** Exigir última versão de todo snapshot.

**Como pensar:** Descubra qual visão foi prometida pelo nível e pelo produto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Snapshot não é visão mais recente”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q226

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Uma espera unilateral continua podendo ser transitória; deadlock exige ciclo.
- **B)** Incorreta. Escalonamento de lock depende do produto e da carga, não de um tempo universal.
- **C)** Incorreta. Se os recursos fossem liberados após cada comando, a duração não explicaria maior retenção.
- **D)** Correta. Maior retenção amplia espera e janela de ciclo.

**Conceito:** Transação longa e contenção.

**Pegadinha:** Ignorar o tempo de posse do recurso.

**Como pensar:** Marque quando o primeiro lock é adquirido e liberado.

### Comentário S3D5Q227

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A vítima foi abortada e deve ser refeita com política controlada.
- **B)** Incorreta. Locks obtidos não equivalem a confirmação parcial.
- **C)** Incorreta. Repetição cega pode amplificar conflito e efeitos externos.
- **D)** Incorreta. Commit forçado não é solução para um ciclo detectado.

**Conceito:** Retry após deadlock.

**Pegadinha:** Delegar todo tratamento ao SGBD.

**Como pensar:** Trate a vítima como operação não concluída e preserve idempotência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Nova tentativa da vítima”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q228

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Não há dado abortado nem escrita apagada.
- **B)** Correta. A mesma linha muda; depois muda o conjunto do predicado.
- **C)** Incorreta. A ordem dos conceitos está invertida.
- **D)** Incorreta. Nenhuma espera foi informada.

**Conceito:** Não repetível versus fantasma.

**Pegadinha:** Chamar ambos de “resultado diferente”.

**Como pensar:** Identifique se mudou valor de linha existente ou membros do conjunto.

### Comentário S3D5Q229

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Aceitar a última escrita causa perda da anterior.
- **B)** Incorreta. Separar leitura e gravação sem validar mudança amplia a janela de base desatualizada.
- **C)** Incorreta. Repetir o mesmo ciclo sem versão, lock ou operação atômica pode reproduzir a perda.
- **D)** Correta. Conflito, versão ou operação atômica preservam o valor corrente.

**Conceito:** Prevenção de atualização perdida.

**Pegadinha:** Mudar representação em vez de coordenar a escrita.

**Como pensar:** Exija que a gravação use ou valide a versão corrente.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Operação atômica sobre valor corrente”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q230

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Concorrência, isolamento, locks, MVCC e deadlock](semana_03_estudo.md#s3-d5-concorrencia).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Serializable não promete confirmar toda tentativa.
- **B)** Incorreta. Equivalência serial não exige execução física uma a uma.
- **C)** Correta. O aborto impede resultado incompatível com ordem serial.
- **D)** Incorreta. Leitura suja não foi demonstrada.

**Conceito:** Aborto de serialização.

**Pegadinha:** Tomar rollback como falha da garantia.

**Como pensar:** Pergunte qual resultado surgiria se ambas fossem confirmadas.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Serializable e aborto”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q231

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Grant trata autorização.
- **B)** Correta. Chave primária única e não nula identifica a entidade.
- **C)** Incorreta. Auditoria registra ações.
- **D)** Incorreta. Parâmetro protege a construção do comando.

**Conceito:** Integridade de entidade.

**Pegadinha:** Misturar integridade com segurança.

**Como pensar:** Procure o mecanismo que identifica cada ocorrência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Integridade de entidade”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q232

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. FK valida a relação com a linha pai.
- **B)** Incorreta. Role não prova existência do pai.
- **C)** Incorreta. Checkpoint pertence à recuperação.
- **D)** Incorreta. Lock não valida referência.

**Conceito:** Integridade referencial.

**Pegadinha:** Usar autorização para corrigir relação estrutural.

**Como pensar:** A expressão “aponta para existente” seleciona a FK.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Integridade referencial”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q233

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Tipo e check limitam o conjunto de valores.
- **B)** Incorreta. Autenticação valida identidade.
- **C)** Incorreta. Serializable controla concorrência.
- **D)** Incorreta. Auditoria evidencia, mas não define a faixa.

**Conceito:** Integridade de domínio.

**Pegadinha:** Trocar prevenção por registro posterior.

**Como pensar:** Escreva o conjunto permitido antes de escolher o controle.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Integridade de domínio”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q234

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Usuário autenticado não recebe poder total.
- **B)** Correta. Identidade e operações permitidas são controles distintos.
- **C)** Incorreta. FK não concede privilégios.
- **D)** Incorreta. MVCC não retira permissão.

**Conceito:** Autenticação e autorização.

**Pegadinha:** Tratar login válido como autorização ampla.

**Como pensar:** Faça as perguntas “quem?” e “pode fazer o quê?”.

### Comentário S3D5Q235

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Faixa válida pertence ao domínio.
- **B)** Incorreta. Equivalência serial pertence ao isolamento.
- **C)** Correta. Auditoria produz rastreabilidade de ação.
- **D)** Incorreta. Existência do pai pertence à referência.

**Conceito:** Auditoria.

**Pegadinha:** Esperar que auditoria impeça toda ação inválida.

**Como pensar:** Associe-a a evidência de quem, o quê, quando e objeto.

### Comentário S3D5Q236

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Poder administrativo não é neutralizado pela interface.
- **B)** Incorreta. Escrita e tabelas amplas excedem a necessidade.
- **C)** Incorreta. Compartilhar DBA amplia risco.
- **D)** Correta. Role e view limitam operações e dados à finalidade.

**Conceito:** Menor privilégio.

**Pegadinha:** Confundir ocultação visual com controle no banco.

**Como pensar:** Remova cada objeto e verbo que não seja necessário ao relatório.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Menor privilégio no relatório”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q237

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Revoke não concede temporariamente mais poder.
- **B)** Correta. Outro caminho de autorização pode manter o acesso.
- **C)** Incorreta. Consulta prévia não cria grant permanente.
- **D)** Incorreta. Chave primária não autoriza usuário.

**Conceito:** Privilégio efetivo.

**Pegadinha:** Avaliar apenas uma concessão direta.

**Como pensar:** Enumere roles, heranças, propriedade e outros grants.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Efeito de REVOKE”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q238

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Ordenação não limita acesso.
- **B)** Incorreta. Privilégio administrativo contorna o recorte.
- **C)** Incorreta. Interface não impede consulta direta.
- **D)** Correta. A view só limita de fato sem rota paralela mais ampla.

**Conceito:** View de acesso limitado.

**Pegadinha:** Esquecer privilégios diretos sobre a base.

**Como pensar:** Faça um mapa de todos os caminhos do usuário até os dados.

### Comentário S3D5Q239

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A entrada segue como valor literal separado da instrução.
- **B)** Incorreta. Parâmetro não concede role.
- **C)** Incorreta. Valor não vira identificador seguro.
- **D)** Incorreta. Autorização continua independente.

**Conceito:** Parâmetros e injeção.

**Pegadinha:** Imaginar mera concatenação com escape.

**Como pensar:** Separe canal de código e canal de valor.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Valor parametrizado”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q240

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Parâmetros aceitam também texto e outros tipos.
- **B)** Incorreta. Ordenação dinâmica pode ser feita com controle.
- **C)** Correta. Identificador muda a estrutura e pede allowlist.
- **D)** Incorreta. Order by não neutraliza entrada maliciosa.

**Conceito:** Identificador dinâmico seguro.

**Pegadinha:** Tratar nome de coluna como valor comum.

**Como pensar:** Se a entrada altera a gramática, escolha-a de lista fechada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Identificador dinâmico”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q241

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Integridade, segurança, roles e parametrização](semana_03_estudo.md#s3-d5-integridade-seguranca).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Parâmetro não modifica privilégios.
- **B)** Incorreta. Autorização não substitui construção segura.
- **C)** Correta. Um controle reduz injeção; o outro ainda amplia impacto.
- **D)** Incorreta. Poder administrativo não filtra entrada.

**Conceito:** Defesa em profundidade.

**Pegadinha:** Considerar um controle como substituto universal.

**Como pensar:** Avalie separadamente estrutura do SQL e alcance da conta.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Parâmetro não substitui autorização”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q242

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O log durável precede a página correspondente.
- **B)** Incorreta. A ordem inversa enfraquece a recuperação.
- **C)** Incorreta. Checkpoint não substitui os registros necessários.
- **D)** Incorreta. Backup não antecede cada update transacional.

**Conceito:** Write-ahead logging.

**Pegadinha:** Priorizar a página e registrar depois.

**Como pensar:** Garanta primeiro a evidência que permitirá undo ou redo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Princípio write-ahead”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q243

**Nível:** Médio

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. T1 confirmou e não deve ser desfeita.
- **B)** Correta. Redo reaplica o efeito confirmado ausente da página.
- **C)** Incorreta. Privilégio não recupera dado.
- **D)** Incorreta. Checkpoint não é transação a ser revertida.

**Conceito:** Redo.

**Pegadinha:** Desfazer o que ainda não estava na página.

**Como pensar:** Confirmada e ausente pede reaplicação.

### Comentário S3D5Q244

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Sem commit, durabilidade não protege o efeito.
- **B)** Incorreta. Página gravada não é backup nem decisão.
- **C)** Incorreta. Queda não produz commit implícito.
- **D)** Correta. Undo remove efeito de transação não confirmada.

**Conceito:** Undo.

**Pegadinha:** Confundir persistência física com confirmação lógica.

**Como pensar:** Classifique pelo registro de decisão.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Função de undo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q245

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Checkpoint não confirma ativas.
- **B)** Incorreta. Não garante fotografia de todas as páginas.
- **C)** Incorreta. Não elimina log nem cópia autônoma.
- **D)** Correta. Coordena e reduz trabalho sem decidir commits.

**Conceito:** Checkpoint.

**Pegadinha:** Interpretá-lo como “salvar tudo”.

**Como pensar:** Use-o para orientar recuperação, não para classificar transações sozinho.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Limites do checkpoint”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q246

**Nível:** Muito difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Página gravada não supera a decisão do log.
- **B)** Incorreta. A alternativa inverte confirmada e ativa.
- **C)** Correta. Redo preserva T1; undo remove T2.
- **D)** Incorreta. Checkpoint não invalida commits posteriores.

**Conceito:** Recuperação integrada.

**Pegadinha:** Usar estado físico como único critério.

**Como pensar:** Faça duas listas: commits que devem aparecer e ativas que não podem ficar.

### Comentário S3D5Q247

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A fase prepare coleta votos duráveis de capacidade.
- **B)** Incorreta. Decisão local divergente quebra atomicidade.
- **C)** Incorreta. 2PC não replica dados.
- **D)** Incorreta. Participante preparado pode manter recursos.

**Conceito:** Primeira fase do 2PC.

**Pegadinha:** Confundir prepare com commit.

**Como pensar:** Fase 1 pergunta; fase 2 decide e comunica.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Primeira fase do 2PC”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D5Q248

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Participantes não escolhem decisões divergentes.
- **B)** Correta. Unanimidade positiva permite commit global.
- **C)** Incorreta. Votos sim não obrigam rollback.
- **D)** Incorreta. O protocolo não vira replicação.

**Conceito:** Decisão global no 2PC.

**Pegadinha:** Tomar voto como decisão local definitiva.

**Como pensar:** Aplique unanimidade e uma decisão única.

### Comentário S3D5Q249

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Leitura suja não é consequência obrigatória.
- **B)** Correta. Sem decisão conhecida, preparados podem bloquear mantendo recursos.
- **C)** Incorreta. Commit unilateral ameaça atomicidade.
- **D)** Incorreta. Registro de preparo continua necessário.

**Conceito:** Bloqueio no 2PC.

**Pegadinha:** Associar distribuição a disponibilidade automática.

**Como pensar:** Pergunte o que o participante sabe depois de votar sim.

### Comentário S3D5Q250

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [Log, recuperação e transações distribuídas](semana_03_estudo.md#s3-d5-recuperacao-distribuidas).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. 2PC coordena atomicidade, sem prometer replicação, velocidade ou disponibilidade.
- **B)** Incorreta. O protocolo pode bloquear.
- **C)** Incorreta. Não substitui controles locais.
- **D)** Incorreta. Falha no preparo conduz a rollback global.

**Conceito:** Objetivo e limites do 2PC.

**Pegadinha:** Dar ao protocolo benefícios não relacionados.

**Como pensar:** Separe decisão atômica de desempenho, cópia e segurança.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “O que o 2PC não oferece”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.1

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Lei nº 4.769/1965
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É a fonte indicada para disciplina e base da profissão.
- **B)** Incorreta. Trata da organização interna no recorte.
- **C)** Incorreta. É a referência ética indicada.
- **D)** Incorreta. Histórico não é fonte normativa.

**Conceito:** Objeto e fonte normativa.

**Pegadinha:** Escolher pela data.

**Como pensar:** Identifique primeiro o objeto jurídico.

#### Comentário Extra Dia 5.2

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Decreto nº 61.934/1967
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. É norma ética, não regulamentadora.
- **B)** Incorreta. Regimento e decreto têm objetos distintos.
- **C)** Correta. É o decreto associado à regulamentação da lei.
- **D)** Incorreta. Certificado não regulamenta profissão.

**Conceito:** Lei e decreto.

**Pegadinha:** Confundir espécies infralegais.

**Como pensar:** Associe o verbo “regulamentar” ao decreto indicado.

#### Comentário Extra Dia 5.3

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 651/2024
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A lei é base, mas não esgota o objeto interno específico.
- **B)** Correta. É a norma indicada para organização e competência interna.
- **C)** Incorreta. A RN nº 671/2025 é ética.
- **D)** Incorreta. Decreto regulamentador não é regimento.

**Conceito:** Organização interna.

**Pegadinha:** Ignorar o complemento do objeto.

**Como pensar:** Sublinhe “órgãos e competências internas”.

#### Comentário Extra Dia 5.4

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** RN CFA nº 671/2025
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. A lei disciplina a profissão, mas não esgota a conduta ética específica cobrada.
- **B)** Incorreta. A RN nº 651/2024 trata do recorte de organização interna, não do código ético indicado.
- **C)** Incorreta. O decreto regulamenta a lei de base, mas não substitui a norma ética posterior do recorte.
- **D)** Correta. A RN nº 671/2025 é a fonte ética do recorte, aplicada depois de identificar sujeito, conduta e consequência.

**Conceito:** Regra ética.

**Pegadinha:** Pular direto para a sanção.

**Como pensar:** Faça sujeito → conduta → norma → consequência.

#### Comentário Extra Dia 5.5

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Âmbito de competência
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Fiscalização regional não transfere toda orientação nacional.
- **B)** Correta. A divisão respeita verbo, território e limite.
- **C)** Incorreta. CFA nacional não executa necessariamente toda diligência local.
- **D)** Incorreta. Autonomia não rompe a integração.

**Conceito:** CFA e CRA-PR.

**Pegadinha:** Confundir território com competência normativa total.

**Como pensar:** Separe órgão, verbo e âmbito.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “CFA nacional e CRA regional”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.6

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Hierarquia normativa
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Recência não supera sozinha lei e competência.
- **B)** Incorreta. Resolução não revoga lei automaticamente.
- **C)** Incorreta. Conveniência não é critério de validade.
- **D)** Incorreta. Conflito não transforma normas em meras recomendações.

**Conceito:** Hierarquia normativa.

**Pegadinha:** Aplicar cronologia isoladamente.

**Como pensar:** Compare hierarquia e competência antes da data.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Resolução posterior e lei”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.7

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Autonomia regional
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Autonomia não autoriza contrariar lei.
- **B)** Incorreta. O CRA não absorve toda orientação nacional.
- **C)** Incorreta. Jurisdição continua limitadora.
- **D)** Correta. A autonomia opera dentro das competências e normas superiores.

**Conceito:** Autonomia limitada.

**Pegadinha:** Confundir autonomia com soberania.

**Como pensar:** Complete a frase com competência e limite.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Autonomia sem ruptura”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.8

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Método de resolução
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Recência, sem hierarquia e competência, não resolve conflito entre fontes.
- **B)** Incorreta. O território não transfere ao órgão regional todas as funções do sistema.
- **C)** Correta. É a sequência de seis filtros ensinada.
- **D)** Incorreta. Começar pela sanção e omitir território e competência inverte o método.

**Conceito:** Roteiro institucional.

**Pegadinha:** Saltar do território para a resposta.

**Como pensar:** Preencha os seis campos antes de comparar alternativas.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Roteiro de leitura institucional”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.9

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Limites de transparência
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Publicidade não elimina proteção aplicável.
- **B)** Incorreta. Sigilo não apaga toda prestação de contas.
- **C)** Correta. A solução preserva ambos os deveres com limites.
- **D)** Incorreta. Não há incompatibilidade absoluta.

**Conceito:** Transparência e sigilo.

**Pegadinha:** Absolutizar um dos valores.

**Como pensar:** Procure compatibilização, não eliminação.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Publicidade e sigilo”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.10

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Legislação CRA/CFA
- **Assunto:** Fonte, território e verbo
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A lei de base não esgota a conduta ética.
- **B)** Correta. Combina norma ética, sujeito e atuação regional limitada.
- **C)** Incorreta. Alcance nacional não impõe execução direta de toda diligência.
- **D)** Incorreta. Regimento não afasta fontes superiores.

**Conceito:** Caso normativo integrado.

**Pegadinha:** Buscar uma única fonte para objetos distintos.

**Como pensar:** Separe regra da conduta e órgão de aplicação.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Caso integrado de competência”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.11

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** URL
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Troca esquema, host e fragmento.
- **B)** Incorreta. Inverte caminho e consulta.
- **C)** Incorreta. Fragmento e esquema foram mal classificados.
- **D)** Correta. Identifica corretamente todos os componentes.

**Conceito:** Componentes de URL.

**Pegadinha:** Ignorar delimitadores.

**Como pensar:** Corte a URL em `://`, `?` e `#`.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Partes de uma URL”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.12

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** HTTPS e certificado
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cifra trânsito e autentica host conforme cadeia, sem garantir honestidade do conteúdo.
- **B)** Incorreta. Domínio parecido pode ser de terceiro.
- **C)** Incorreta. TLS não valida toda oferta.
- **D)** Incorreta. HTTPS não cria anonimato.

**Conceito:** Limites do HTTPS.

**Pegadinha:** Usar cadeado como selo de legitimidade.

**Como pensar:** Confira qual host foi autenticado.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Alcance do HTTPS”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.13

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Artefatos de navegação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Troca cache e histórico.
- **B)** Correta. A sequência associa acelerar, estado, registro e arquivo.
- **C)** Incorreta. Cookie não cifra tráfego.
- **D)** Incorreta. Histórico e cache não têm essas funções.

**Conceito:** Cache, cookie, histórico e download.

**Pegadinha:** Chamar tudo de temporário.

**Como pensar:** Associe cada artefato a um verbo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Cache, cookie, histórico e download”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.14

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Privacidade local e rede
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. O site continua observando a conexão.
- **B)** Incorreta. A rede organizacional pode continuar visível.
- **C)** Incorreta. Modo privado não substitui túnel ou identidade.
- **D)** Correta. Reduz rastros locais sem gerar anonimato externo.

**Conceito:** Navegação privada.

**Pegadinha:** Confundir local com rede.

**Como pensar:** Liste separadamente dispositivo, rede, provedor e site.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Navegação privada”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.15

- **Dia:** Dia 5
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Phishing e verificação
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, Legislação CRA/CFA e internet](semana_03_estudo.md#s3-d5-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A conduta verifica domínio e canal antes de fornecer segredo.
- **B)** Incorreta. Cadeado não prova vínculo institucional esperado.
- **C)** Incorreta. A estética pode ser copiada.
- **D)** Incorreta. Modo privado não autentica destinatário.

**Conceito:** Verificação contra phishing.

**Pegadinha:** Confiar em aparência ou TLS isolado.

**Como pensar:** Valide o host por canal oficial independente.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Domínio parecido com cadeado”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.16

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coesão referencial
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. “Eles” continua ambíguo.
- **B)** Incorreta. “Estes” ainda pode retomar cidadãos.
- **C)** Correta. A repetição de “critérios” fixa o referente.
- **D)** Incorreta. “Os mesmos” não resolve a ambiguidade.

**Conceito:** Referente inequívoco.

**Pegadinha:** Trocar um pronome por outro.

**Como pensar:** Repita o núcleo nominal quando houver dois antecedentes.

#### Comentário Extra Dia 5.17

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Coerência entre orações
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. “Portanto” é conclusão.
- **B)** Incorreta. “Porque” é causa ou explicação.
- **C)** Incorreta. “Assim” é consequência.
- **D)** Correta. “Embora” introduz concessão.

**Conceito:** Conector concessivo.

**Pegadinha:** Escolher pelo som.

**Como pensar:** Parafraseie com “apesar de”.

#### Comentário Extra Dia 5.18

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Paralelismo sintático
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Mistura verbo, substantivo e oração.
- **B)** Correta. Coordena três infinitivos.
- **C)** Incorreta. Combina estruturas diferentes.
- **D)** Incorreta. Também rompe a equivalência formal.

**Conceito:** Paralelismo.

**Pegadinha:** Olhar apenas o sentido.

**Como pensar:** Compare o núcleo gramatical de cada membro.

#### Comentário Extra Dia 5.19

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Modalização
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A conclusão condicionada respeita evidência parcial.
- **B)** Incorreta. “Sempre” e “elimina” excedem os dados.
- **C)** Incorreta. Um resultado não prova ausência universal de risco.
- **D)** Incorreta. Generaliza causalidade sem controle.

**Conceito:** Força da conclusão.

**Pegadinha:** Usar termos absolutos com evidência limitada.

**Como pensar:** Ajuste modalizadores à força da prova.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Força de termos absolutos”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 5.20

- **Dia:** Dia 5
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Planejamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e plano integral da discursiva](semana_03_estudo.md#s3-d5-b5).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Faltam tese e progressão.
- **B)** Incorreta. A tese absoluta e a estrutura incompleta falham.
- **C)** Incorreta. Jargão técnico não sustenta o tema geral.
- **D)** Correta. Há problema, tese, dois eixos e conclusão sem novidade.

**Conceito:** Plano integral da discursiva.

**Pegadinha:** Confundir tecnicismo com argumento.

**Como pensar:** Confira uma função própria para cada parágrafo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Arquitetura do plano integral”; a extensão decorre dessa precisão técnica, não de pista formal.

---

# Dia 6 — Índices, otimização, SGBDs e Business Intelligence

As 70 questões abaixo são autorais e calibradas pelo perfil documentado do Instituto Consulplan. Nenhum item reproduz questão real. Resolva seis Essenciais em D0 e avance até dez somente quando couber correção integral.

## Questões principais — S3D6Q251 a S3D6Q300

### S3D6Q251 — Índice como caminho com custo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Um índice deve ser entendido como:

A) uma regra lógica que muda a resposta correta da consulta.

B) uma estrutura gratuita, sem efeito sobre escrita.

C) uma garantia de que o otimizador fará busca indexada.

D) uma estrutura auxiliar de acesso que pode reduzir leitura, mas consome espaço e manutenção.

### S3D6Q252 — B-tree e hash

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Qual comparação conceitual está correta?

A) Hash preserva ordem e atende faixas melhor que B-tree.

B) B-tree só pode ser usado para igualdade.

C) B-tree costuma apoiar igualdade e faixa; hash tende à igualdade da chave completa e não preserva ordem.

D) Hash criado pelo usuário possui sintaxe idêntica nos três SGBDs.

### S3D6Q253 — Prefixo à esquerda

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Dado o índice B-tree `(uf, status, nome)`, qual predicado usa um prefixo clássico de duas colunas?

A) `uf='PR' AND status='A'`.

B) `status='A' AND nome='Ana'`.

C) `nome='Ana'`.

D) `status='A'`.

### S3D6Q254 — Salto de coluna no índice composto

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Com índice `(uf, status, nome)`, a consulta filtra `uf='PR' AND nome='Ana'`, sem condição para `status`. Qual análise é responsável?

A) O índice é sempre impossível de ler.

B) `uf` oferece prefixo útil, mas o salto de `status` pode limitar o aproveitamento ordenado de `nome`; o plano final depende do custo.

C) Todas as três colunas formam busca de igualdade contínua.

D) O SGBD deve converter o índice em hash.

### S3D6Q255 — Cobertura depende da consulta

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Um índice contém todas as colunas necessárias para filtrar, juntar e retornar uma consulta específica. Nesse contexto, ele é:

A) clustered em qualquer produto.

B) cobridor para essa consulta, sem que isso implique cobrir todas as outras.

C) uma constraint de domínio.

D) obrigatoriamente escolhido pelo otimizador.

### S3D6Q256 — Baixa seletividade e scan

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Uma consulta retorna 96% de uma tabela larga ao filtrar `ativo='S'`. Qual decisão inicial é adequada?

A) Criar um índice isolado e forçar seu uso.

B) Preferir o índice porque a presença de qualquer `WHERE` torna a leitura seletiva.

C) Proibir índice nessa coluna em todos os cenários apenas por ela ter poucos valores distintos.

D) Comparar custos; um scan pode ser mais barato que percorrer índice e buscar quase todas as linhas.

### S3D6Q257 — Predicado sargável

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Em SQL conceitual com literal tipado — cuja escrita deve ser adaptada ao dialeto —, qual predicado tende a expor melhor a chave indexada `criado_em` para o ano de 2026?

A) `EXTRACT(YEAR FROM criado_em)=2026`.

B) `CAST(criado_em AS text) LIKE '2026%'`.

C) `criado_em >= DATE '2026-01-01' AND criado_em < DATE '2027-01-01'`.

D) `criado_em + INTERVAL '0 day' >= DATE '2026-01-01'`.

### S3D6Q258 — Limite superior exclusivo

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

No mesmo SQL conceitual, por que o filtro anual usa `criado_em < DATE '2027-01-01'` em vez de terminar em `2026-12-31` sem horário?

A) O limite exclusivo inclui todo o último dia independentemente da precisão de horário.

B) B-tree não aceita data de dezembro.

C) O limite transforma faixa em igualdade.

D) `BETWEEN` nunca funciona com datas.

### S3D6Q259 — Custo colateral de índice

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Adicionar um índice a uma tabela muito atualizada tende a:

A) acrescentar trabalho de manutenção em inserções, alterações e exclusões, além de espaço.

B) eliminar qualquer custo de escrita porque só armazena chaves.

C) dispensar estatísticas.

D) alterar a resposta lógica do `SELECT`.

### S3D6Q260 — Constraint e índice

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Qual afirmação distingue corretamente constraint e índice?

A) São sempre sinônimos, pois ambos ocupam páginas.

B) Índice define a regra institucional; constraint serve apenas ao desempenho.

C) Constraint só existe quando não há estrutura física.

D) Constraint expressa regra lógica; índice é mecanismo físico que o produto pode usar para garanti-la ou acelerar acesso.

### S3D6Q261 — B-tree e ordenação

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Por preservar ordenação de chaves, uma B-tree pode ajudar:

A) somente em inserções sem leitura.

B) em faixas e em certos `ORDER BY` compatíveis com a ordem do índice.

C) a converter qualquer predicado não sargável.

D) a executar hash join sem ler entradas.

### S3D6Q262 — Hash e faixa

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Para `valor BETWEEN 100 AND 200`, por que um índice hash conceitual não é o candidato natural?

A) Porque hash só armazena textos.

B) Porque toda faixa exige scan de tabela.

C) Porque hash não preserva ordem para percorrer intervalo; seu uso típico é igualdade da chave completa.

D) Porque B-tree não aceita igualdade.

### S3D6Q263 — Coluna pouco seletiva em composição

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Uma coluna de dois valores possui baixa seletividade isolada. Isso permite concluir que ela:

A) jamais pode aparecer em índice.

B) deve ser sempre a primeira coluna.

C) pode ainda colaborar em índice composto, cobertura, ordenação ou subconjunto específico; é preciso medir.

D) transforma automaticamente o índice em constraint.

### S3D6Q264 — Cobertura relativa

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Em um produto que suporte `INCLUDE`, o índice `(unidade_id, status) INCLUDE (total)` cobre a Consulta A, que usa apenas essas colunas. A Consulta B também retorna `observacao`. Qual conclusão é correta?

A) O índice pode cobrir A e não B, pois cobertura é relação entre estrutura e consulta.

B) Se cobre uma consulta, cobre a tabela inteira.

C) `INCLUDE` torna obrigatória a escolha do índice.

D) Cobertura elimina todo custo de escrita.

### S3D6Q265 — Ordem de índice por carga real

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

A consulta crítica filtra unidade e status por igualdade, restringe período e ordena por data; raramente busca apenas status. Qual candidato inicial é mais coerente?

A) `(status, criado_em, unidade_id)` apenas porque status aparece no `WHERE`.

B) `(criado_em, status, unidade_id)` porque data possui muitos valores.

C) `(status)` e um índice separado em cada coluna, sem medir.

D) `(unidade_id, status, criado_em)`, seguido de medição do plano, projeção e custo de escrita.

### S3D6Q266 — Conversão implícita e busca

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Uma coluna numérica indexada é comparada a entrada textual de tipo incompatível, levando o produto a converter a coluna em cada linha. O risco é:

A) a conversão sobre a coluna ser inofensiva apenas porque os valores representam números equivalentes.

B) a conversão sobre a coluna prejudicar sargabilidade e o caminho de busca convencional.

C) a existência do índice obrigar o otimizador a converter a entrada, preservando sempre a busca.

D) acrescentar a mesma coluna a outro índice eliminar a conversão aplicada no predicado.

### S3D6Q267 — Curinga inicial

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Qual padrão tende a dificultar a busca convencional pelo prefixo de uma B-tree em `nome`?

A) `nome = 'Ana'`.

B) `nome >= 'M'`.

C) `nome LIKE 'Ana%'`.

D) `nome LIKE '%ana'`.

### S3D6Q268 — Índice por expressão

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

A consulta precisa manter exatamente `EXTRACT(YEAR FROM criado_em)=2026`. Qual ressalva evita afirmar que toda função torna índice inútil?

A) Função sempre vira chave primária.

B) O otimizador ignora todas as expressões.

C) Um índice por expressão ou recurso equivalente, criado e compatível, pode oferecer caminho adequado.

D) Qualquer índice em outra coluna resolve.

### S3D6Q269 — Índice não garante uso

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

Existe índice compatível, mas a tabela tem 40 linhas e todas serão retornadas. O scan escolhido pelo otimizador:

A) pode ser correto, pois o custo de ler poucas páginas pode ser menor.

B) prova corrupção do índice.

C) deve ser substituído por dica sem medição.

D) altera a semântica da consulta.

### S3D6Q270 — Diagnóstico integrado de índice

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um relatório melhorou de 8 s para 900 ms após novo índice, mas a carga horária subiu de 20 s para 38 s. Qual decisão é tecnicamente completa?

A) Manter o índice porque qualquer leitura tem prioridade.

B) Avaliar frequência, criticidade, custo acumulado de escrita, espaço e alternativas antes de manter ou reverter.

C) Remover todas as constraints para compensar.

D) Declarar sucesso apenas pela menor latência do relatório.

### S3D6Q271 — Custo do otimizador

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

O número de custo mostrado em um plano deve ser lido como:

A) tempo garantido em milissegundos.

B) unidade interna comparativa usada para escolher entre planos, não cronômetro universal.

C) quantidade exata de linhas reais.

D) percentual de uso de CPU medido.

### S3D6Q272 — Estatísticas desatualizadas

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Estatísticas que não representam mais a distribuição podem levar o otimizador a:

A) manter necessariamente as mesmas cardinalidades, pois a distribuição não participa das estimativas.

B) afetar apenas o texto exibido no plano, sem influenciar a escolha de operadores.

C) substituir linhas reais por estimadas durante a execução, sem efeito sobre a ordem de junção.

D) estimar cardinalidades inadequadas e escolher ordem ou método de junção pouco apropriado.

### S3D6Q273 — Estimado versus real

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um nó estima 1 linha e produz 500 mil. Qual é o primeiro alvo do diagnóstico?

A) Entender a causa da estimativa incorreta antes de forçar operador aleatório.

B) Atualizar estatísticas e encerrar o diagnóstico sem conferir se a divergência desapareceu.

C) Forçar hash join apenas porque o volume real é grande, antes de localizar a origem da estimativa.

D) Criar índice para cada coluna do nó, sem analisar distribuição, correlação ou forma do predicado.

### S3D6Q274 — Nested loop contextual

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Quando um nested loop pode ser boa escolha?

A) Somente quando não há índice algum.

B) Sempre que as duas entradas são enormes.

C) Quando a entrada externa é pequena e há busca interna eficiente.

D) Apenas para condição sem igualdade.

### S3D6Q275 — Hash join

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual afirmação sobre hash join está correta?

A) Exige que exista índice hash nas duas tabelas.

B) Só funciona com dados previamente ordenados.

C) Pode ser adequado para igualdade e conjuntos relevantes, sem exigir índice hash criado pelo usuário.

D) É sempre superior a nested loop.

### S3D6Q276 — Merge join

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual cenário pode favorecer merge join?

A) Predicados sem condição compatível e entradas aleatórias obrigatoriamente.

B) Entradas já ordenadas ou ordenáveis de modo vantajoso e condição compatível.

C) Ausência total de relação entre tabelas.

D) Somente presença de índice hash.

### S3D6Q277 — Scan não é falha automática

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual situação justifica um scan?

A) Toda consulta com `WHERE`.

B) Somente tabela sem chave primária.

C) Apenas consulta não sargável.

D) Tabela pequena ou necessidade de grande parte das linhas, quando o custo global é menor.

### S3D6Q278 — Seek não garante rapidez

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um plano usa index seek/search, mas retorna milhões de linhas e executa acessos adicionais caros. Qual conclusão é correta?

A) O nome do operador não garante rapidez; é preciso avaliar cardinalidade, trabalho total e métricas.

B) Seek prova que o plano é ótimo.

C) O resultado lógico está errado.

D) Estatísticas deixam de ter importância.

### S3D6Q279 — Maior discrepância no plano

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Ao comparar plano estimado e real, qual pista merece prioridade?

A) Grande diferença entre linhas estimadas e reais em nó que influencia o restante da árvore.

B) O maior percentual de custo estimado, mesmo quando estimativa e execução desse nó coincidem.

C) A presença de qualquer scan, mesmo barato.

D) O último nó desenhado na ferramenta, por ser necessariamente a origem da primeira estimativa incorreta.

### S3D6Q280 — EXPLAIN nos três produtos

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Assinale a comparação correta.

A) SQL Server usa `EXPLAIN ANALYZE` como sintaxe T-SQL genérica.

B) PostgreSQL não executa a consulta com `EXPLAIN ANALYZE`.

C) PostgreSQL 18.4 e MySQL 9.7 LTS oferecem `EXPLAIN` e `EXPLAIN ANALYZE`; SQL Server 2025 17.x expõe planos estimado e real por suas ferramentas.

D) Os três apresentam plano real sem executar nada.

### S3D6Q281 — Plano real e DML

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Por que uma análise que executa DML deve ocorrer em ambiente controlado?

A) Porque DML nunca pode ter plano.

B) Porque obter métricas reais pode executar e modificar dados; reversão deve ser planejada quando apropriada.

C) Porque todo plano real concede `COMMIT` ao usuário.

D) Porque estatística desabilita rollback.

### S3D6Q282 — Protocolo de otimização

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual sequência representa o protocolo ensinado?

A) Criar índice → forçar plano → procurar consulta.

B) Escolher dica → mudar três fatores → medir outro parâmetro.

C) Medir depois → apagar estatísticas → aceitar.

D) Registrar cenário → obter plano → formular hipótese → mudar uma coisa → medir igual → comparar custos → decidir.

### S3D6Q283 — Uma mudança por vez

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual é a principal razão para alterar um fator por vez?

A) Reduzir a quantidade de alternativas do SQL padrão.

B) Garantir que toda mudança melhore.

C) Evitar a necessidade de plano real.

D) Atribuir o efeito observado à hipótese testada e permitir reversão com evidência.

### S3D6Q284 — Dicas de plano

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Por que uma dica não deve ser a primeira reação?

A) Pode envelhecer, esconder a causa da estimativa e piorar outros parâmetros.

B) Porque dicas sempre geram erro de sintaxe.

C) Porque nenhum SGBD possui recursos de controle de plano.

D) Porque a dica corrige automaticamente estatísticas.

### S3D6Q285 — Correlação entre colunas

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

O plano estima 50 mil linhas para `uf='PR' AND cidade='Curitiba'`, mas retorna 4 mil. A primeira hipótese responsável é:

A) As estatísticas estão necessariamente desatualizadas, ainda que não haja evidência de mudança recente nos dados.

B) Aumentar a amostra de estatísticas independentes sempre representa a dependência entre as duas colunas.

C) estatística ou modelo de seletividade que não representa a correlação entre UF e cidade.

D) Forçar o método de junção corrige por si a estimativa produzida no filtro correlacionado.

### S3D6Q286 — Tabela de 40 linhas

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Uma tabela de 40 linhas será lida integralmente. O otimizador escolhe scan. O que fazer?

A) Criar quatro índices até aparecer seek.

B) Aceitar que o scan pode ser o plano mais barato e verificar as métricas, sem “corrigir” pelo nome.

C) Forçar nested loop.

D) Desnormalizar a tabela.

### S3D6Q287 — Custo global do serviço

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Um índice melhora relatório diário, mas piora carga horária. Qual métrica deve orientar a decisão?

A) Somente o menor tempo do relatório.

B) Impacto acumulado, frequência, criticidade, espaço e estabilidade nos dois fluxos.

C) Somar apenas a quantidade de execuções, ignorando duração, escrita, espaço e criticidade.

D) Considerar somente o fluxo mais frequente, mesmo que o relatório tenha requisito crítico de prazo.

### S3D6Q288 — Fluxo do otimizador

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Em um modelo simplificado, depois de gerar caminhos e estimar custos, o otimizador:

A) altera a regra de negócio.

B) garante o menor tempo possível em qualquer parâmetro.

C) escolhe um plano, que na execução produzirá métricas reais comparáveis às estimativas.

D) descarta as estatísticas.

### S3D6Q289 — Parâmetros representativos

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Para comparar antes e depois de uma mudança, deve-se:

A) usar parâmetros extremos diferentes para favorecer a versão nova.

B) comparar ambientes e volumes distintos.

C) olhar apenas o custo estimado.

D) manter cenário e parâmetros representativos, registrando tempo, buffers e demais métricas pertinentes.

### S3D6Q290 — Decisão baseada em evidência

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

Qual registro encerra adequadamente um teste de otimização?

A) Hipótese, mudança única, medidas comparáveis, custo colateral e decisão de manter ou reverter.

B) “Ficou mais rápido” sem ambiente ou valor.

C) Um print do operador mais caro, sem contexto.

D) A quantidade de índices criados.

### S3D6Q291 — Comparação versionada

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Qual prática evita generalização incorreta ao comparar PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS?

A) Comparar nomes parecidos e presumir comportamento idêntico.

B) Usar a sintaxe de um produto como padrão dos demais.

C) Fixar versão, conceito, produto, configuração e engine quando relevante.

D) Ignorar documentação do fornecedor.

### S3D6Q292 — TOP e portabilidade

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

A afirmação “`SELECT TOP (10)` funciona sem mudança nos três SGBDs” é:

A) verdadeira, porque todos limitam linhas.

B) verdadeira apenas sem `ORDER BY`.

C) falsa porque nenhum dos três limita linhas.

D) falsa: `TOP` é T-SQL; PostgreSQL e MySQL normalmente usam `LIMIT`, com alternativas padronizadas conforme suporte.

### S3D6Q293 — Organização física principal

**Nível:** Médio

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Qual comparação corresponde ao quadro estudado?

A) Os três organizam obrigatoriamente os dados pela chave primária.

B) PostgreSQL usa heap com índices separados na forma comum; SQL Server pode ter heap ou clustered; no InnoDB, a PK definida é clustered, com fallback para `UNIQUE NOT NULL` adequado ou índice oculto quando ela não existe.

C) SQL Server não possui índice nonclustered.

D) InnoDB sempre usa heap sem relação com a chave primária.

### S3D6Q294 — Forma de obter plano

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Assinale a associação correta.

A) PostgreSQL e MySQL: `EXPLAIN [ANALYZE]`; SQL Server: planos estimado e real nas ferramentas.

B) SQL Server: apenas `EXPLAIN ANALYZE`; PostgreSQL: nenhum plano.

C) MySQL 9.7 LTS não oferece `EXPLAIN`.

D) Os três exigem a mesma sintaxe.

### S3D6Q295 — Engine no MySQL

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

Por que registrar o engine ao descrever comportamento do MySQL?

A) Porque concorrência, organização e outros recursos podem depender do mecanismo; não se deve atribuir a todo MySQL uma propriedade específica do InnoDB.

B) Porque o engine muda a semântica do SQL padrão em todos os comandos.

C) Porque versão deixa de importar quando o engine é conhecido.

D) Porque PostgreSQL e SQL Server usam obrigatoriamente InnoDB.

### S3D6Q296 — Definição de BI

**Nível:** Médio

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Business Intelligence é melhor definido como:

A) sinônimo de dashboard.

B) combinação de processos, dados, modelos, pessoas e ferramentas para apoiar análise e decisão.

C) um único SGBD operacional.

D) a etapa de carga de um ETL.

### S3D6Q297 — OLTP e OLAP

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Qual par de perguntas exemplifica, respectivamente, OLTP e OLAP?

A) “Como evoluiu por mês?” e “qual pedido está aberto agora?”.

B) “Qual é a tendência anual?” e “qual a média histórica?”.

C) “Qual é o estado deste pedido?” e “como o tempo médio evoluiu por unidade e mês?”.

D) “Qual dashboard existe?” e “qual tabela possui PK?”.

### S3D6Q298 — Grão antes das medidas

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Uma fonte possui várias interações por protocolo, mas o indicador deve contar atendimentos concluídos. Qual grão evita duplicidade?

A) Uma linha por arquivo recebido.

B) Uma linha por interação, somando todas como atendimento.

C) Uma linha por dimensão.

D) Uma linha por atendimento concluído, com medidas definidas nesse nível.

### S3D6Q299 — Média de médias

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

A unidade A tem 2 atendimentos com média de 10 min; B tem 18 com média de 20 min. A média global correta é:

A) 15 min, média simples das duas médias.

B) 19 min: `(2×10 + 18×20) / 20`.

C) 20 min, porque o maior grupo prevalece integralmente.

D) 30 min, soma das médias.

### S3D6Q300 — ETL e ELT

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

Qual distinção é correta?

A) ETL carrega antes de transformar; ELT transforma antes de carregar.

B) ETL e ELT são nomes do data warehouse.

C) ETL transforma antes da carga no destino analítico final; ELT carrega e transforma no destino.

D) ELT dispensa qualidade, linhagem e reconciliação.

## Questões extras — Dia 6

#### Extra Dia 6.1 — Negação de conjunção

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Leis de De Morgan
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

A consulta é rápida e o índice é pequeno. Qual é a negação lógica?

A) A consulta não é rápida e o índice não é pequeno.

B) A consulta é rápida ou o índice é pequeno.

C) A consulta não é rápida ou o índice não é pequeno.

D) Se a consulta é rápida, o índice não é pequeno.

#### Extra Dia 6.2 — Negação da implicação

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Implicação
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Negue: “Se o plano usa índice, então o tempo diminui”.

A) O plano usa índice e o tempo não diminui.

B) O plano não usa índice e o tempo diminui.

C) Se o tempo não diminui, o plano não usa índice.

D) O plano não usa índice ou o tempo diminui.

#### Extra Dia 6.3 — Negação do universal

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Quantificadores
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Qual é a negação de “Todo relatório possui fonte identificada”?

A) Nenhum relatório possui fonte identificada.

B) Todo relatório não possui fonte identificada.

C) Algum relatório possui fonte identificada.

D) Existe pelo menos um relatório que não possui fonte identificada.

#### Extra Dia 6.4 — União de conjuntos

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Inclusão-exclusão
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Em 80 consultas, 50 usam filtro por data, 35 usam filtro por status e 20 usam ambos. Quantas usam ao menos um dos dois filtros?

A) 105.

B) 65.

C) 45.

D) 85.

#### Extra Dia 6.5 — Percentuais sucessivos

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Porcentagem
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Um tempo de 100 ms aumenta 20% e depois diminui 20%. O resultado é:

A) 100 ms, porque os percentuais se anulam.

B) 96 ms, pois `100×1,20×0,80=96`.

C) 80 ms.

D) 104 ms.

#### Extra Dia 6.6 — Sugestão, comentário e edição

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Modos de colaboração
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Qual distinção é correta?

A) Comentário altera diretamente o texto; edição apenas discute.

B) Sugestão e edição são sempre idênticas.

C) Histórico de versões é um tipo de comentário.

D) Sugestão propõe mudança sujeita a aceite; comentário discute; edição altera diretamente.

#### Extra Dia 6.7 — Histórico de versões

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Versões e permissões
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

O histórico de versões permite:

A) localizar estados anteriores a quem possui permissão adequada.

B) mostrar apenas a versão atual, sem permitir comparação com estados anteriores.

C) localizar estado anterior somente quando cada versão tiver sido renomeada ou copiada manualmente.

D) restaurar automaticamente uma versão antiga para todos os colaboradores assim que o histórico é aberto.

#### Extra Dia 6.8 — Título semântico

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Estilos
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Por que aplicar estilo de título é diferente de apenas aumentar a fonte?

A) Porque fonte grande bloqueia edição.

B) Porque estilo remove o texto do histórico.

C) Porque o estilo cria estrutura semântica; tamanho isolado muda aparência.

D) Porque título não pode ter fonte grande.

#### Extra Dia 6.9 — Referência relativa

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Ao copiar de C2 para D3 uma fórmula que contém `A2`, a referência relativa torna-se:

A) `$A$2`.

B) `A2`.

C) `B2`.

D) `B3`.

#### Extra Dia 6.10 — Referência absoluta

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Ao copiar uma fórmula, qual referência mantém coluna A e linha 2 fixas?

A) `A2`.

B) `$A$2`.

C) `$A2`.

D) `A$2`.

#### Extra Dia 6.11 — Referência mista copiada

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referência mista
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Em C2, `=$A2*B$1` é copiada para D3. Qual fórmula resulta?

A) `=$B3*C$2`.

B) `=$A2*B$1`.

C) `=$A3*C$1`.

D) `=A3*$C1`.

#### Extra Dia 6.12 — Ordenação segura

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Ordenação de tabela
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Uma planilha possui nome, matrícula e nota na mesma linha. Para ordenar por nota sem romper os registros, deve-se:

A) selecionar o intervalo ou tabela completo e ordenar as linhas pela coluna de nota.

B) ordenar somente as células da coluna nota.

C) copiar as notas para outra aba e apagar a origem.

D) fixar todas as referências com cifrão.

#### Extra Dia 6.13 — Função e configuração regional

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Localização de fórmulas
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Ao interpretar fórmula de outra configuração regional, é correto lembrar que:

A) nome de função e separador podem variar; finalidade e referências devem ser analisadas.

B) toda fórmula usa obrigatoriamente vírgula.

C) referências relativas deixam de existir.

D) o resultado depende apenas do idioma do navegador.

#### Extra Dia 6.14 — HTTPS e navegação privada

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Transporte e privacidade
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Qual afirmação é correta?

A) HTTPS garante que todo conteúdo é legítimo.

B) Navegação privada oculta a conexão do site.

C) Modo privado substitui certificado.

D) HTTPS protege o transporte, e modo privado reduz certos registros locais; nenhum dos dois garante legitimidade total ou anonimato.

#### Extra Dia 6.15 — Credencial e host

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Verificação de destino
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

Um site visualmente idêntico ao oficial, em host diferente, pede senha e exibe cadeado. O usuário deve:

A) confiar no logotipo.

B) verificar host, origem e canal oficial antes de inserir credencial; TLS pode proteger conexão com o destinatário errado.

C) ativar histórico para validar a instituição.

D) limpar cache e inserir a senha.

#### Extra Dia 6.16 — Concordância com sujeito distante

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Concordância
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Assinale a frase com concordância adequada.

A) A análise dos indicadores demonstram avanços.

B) Os uso responsável dos dados melhora decisões.

C) A qualidade dos registros e a clareza dos critérios fortalecem a confiança.

D) Existe direitos que precisam ser preservado.

#### Extra Dia 6.17 — Crase e regência

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Regência e crase
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Assinale a frase adequada.

A) A política visa à melhorar os serviços.

B) A administração informou à todos os critérios.

C) Os gestores obedeceram as normas aplicáveis.

D) A instituição deu transparência às decisões e garantiu respeito aos direitos.

#### Extra Dia 6.18 — Vírgula entre sujeito e verbo

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Pontuação
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Qual frase evita separar indevidamente sujeito e verbo?

A) O uso responsável de dados pode elevar a eficiência sem reduzir a proteção de direitos.

B) A análise dos registros, permite corrigir falhas.

C) A transparência e a proteção, fortalecem a confiança.

D) Os critérios usados pela instituição, devem ser explicados.

#### Extra Dia 6.19 — Coerência e referência

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Progressão textual
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Qual reescrita mantém referente claro e relação de contraste?

A) A gestão ampliou a coleta, porque ela eliminou todo risco.

B) Os dados e a instituição melhoraram, pois eles era claros.

C) A coleta aumentou; contudo, esse aumento não dispensa critérios transparentes e proteção de direitos.

D) A gestão coletou dados, portanto eles talvez, mas nunca.

#### Extra Dia 6.20 — Conclusão da dissertação

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Fechamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

Qual conclusão atende ao protocolo do texto integral?

A) Introduz uma terceira tese sobre aquisição de servidores.

B) Retoma a tese condicionada, sintetiza eficiência, direitos e confiança e fecha sem argumento novo.

C) Lista comandos SQL para demonstrar conhecimento técnico.

D) Afirma que todo risco será eliminado definitivamente.

## Gabarito — Dia 6

### Principais

| S3D6Q251 | S3D6Q252 | S3D6Q253 | S3D6Q254 | S3D6Q255 | S3D6Q256 | S3D6Q257 | S3D6Q258 | S3D6Q259 | S3D6Q260 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D | C | A | B | B | D | C | A | A | D |

| S3D6Q261 | S3D6Q262 | S3D6Q263 | S3D6Q264 | S3D6Q265 | S3D6Q266 | S3D6Q267 | S3D6Q268 | S3D6Q269 | S3D6Q270 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | C | C | A | D | B | D | C | A | B |

| S3D6Q271 | S3D6Q272 | S3D6Q273 | S3D6Q274 | S3D6Q275 | S3D6Q276 | S3D6Q277 | S3D6Q278 | S3D6Q279 | S3D6Q280 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | C | C | B | D | A | A | C |

| S3D6Q281 | S3D6Q282 | S3D6Q283 | S3D6Q284 | S3D6Q285 | S3D6Q286 | S3D6Q287 | S3D6Q288 | S3D6Q289 | S3D6Q290 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | D | A | C | B | B | C | D | A |

| S3D6Q291 | S3D6Q292 | S3D6Q293 | S3D6Q294 | S3D6Q295 | S3D6Q296 | S3D6Q297 | S3D6Q298 | S3D6Q299 | S3D6Q300 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | D | B | A | A | B | C | D | B | C |

### Extras

| 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | 6.6 | 6.7 | 6.8 | 6.9 | 6.10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | D | B | B | D | A | C | D | B |

| 6.11 | 6.12 | 6.13 | 6.14 | 6.15 | 6.16 | 6.17 | 6.18 | 6.19 | 6.20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C | A | A | D | B | C | D | A | C | B |

## Comentários — Dia 6

### Comentário S3D6Q251

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Constraint é regra, não definição de índice.
- **B)** Incorreta. Índice também custa manutenção.
- **C)** Incorreta. A escolha continua baseada em custo.
- **D)** Correta. Estrutura auxiliar troca menor trabalho de certas leituras por custos próprios.

**Conceito:** Índice como caminho de acesso.

**Pegadinha:** Tratá-lo como gratuito ou obrigatório.

**Como pensar:** Avalie benefício de leitura e custo de manter a estrutura.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Índice como caminho com custo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q252

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Hash não preserva ordem para faixa.
- **B)** Incorreta. B-tree também atende igualdade.
- **C)** Correta. B-tree apoia igualdade/faixa; hash tipicamente igualdade completa.
- **D)** Incorreta. Disponibilidade e sintaxe de hash variam por produto.

**Conceito:** B-tree versus hash.

**Pegadinha:** Universalizar comportamento de fornecedor.

**Como pensar:** Pergunte se o acesso exige ordem ou apenas igualdade exata.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “B-tree e hash”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q253

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Usa as duas primeiras colunas contínuas do índice.
- **B)** Incorreta. Ignora a coluna mais à esquerda.
- **C)** Incorreta. Usa apenas a terceira coluna.
- **D)** Incorreta. Começa na segunda coluna.

**Conceito:** Prefixo à esquerda.

**Pegadinha:** Contar condições sem olhar a ordem física.

**Como pensar:** Leia o índice da esquerda até a primeira lacuna.

### Comentário S3D6Q254

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. O índice ainda pode oferecer algum caminho.
- **B)** Correta. Uf pode ajudar, e nome pode ter aproveitamento limitado; custo decide o plano.
- **C)** Incorreta. A lacuna em status quebra a continuidade completa.
- **D)** Incorreta. A estrutura não se converte automaticamente.

**Conceito:** Lacuna em índice composto.

**Pegadinha:** Declarar uso impossível ou completo em termos absolutos.

**Como pensar:** Separe ordem física útil de decisão final do otimizador.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Salto de coluna no índice composto”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q255

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Clustered depende do produto e não decorre da cobertura.
- **B)** Correta. Cobertura é relativa às colunas exigidas pela consulta.
- **C)** Incorreta. Não há regra de domínio.
- **D)** Incorreta. Cobrir não força o plano.

**Conceito:** Índice cobridor.

**Pegadinha:** Atribuir cobertura à tabela inteira.

**Como pensar:** Liste filtro, junção e saída daquela consulta.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Cobertura depende da consulta”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q256

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Forçar ignora custo e proporção.
- **B)** Incorreta. Um `WHERE` não torna o predicado seletivo; aqui ele preserva 96% das linhas.
- **C)** Incorreta. Baixa cardinalidade isolada não proíbe uso em composição, cobertura ou subconjunto raro.
- **D)** Correta. Ler quase tudo por scan pode custar menos que acessos dispersos.

**Conceito:** Seletividade e scan.

**Pegadinha:** Indexar toda coluna do where.

**Como pensar:** Estime a fração retornada e o custo para buscar a linha base.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Baixa seletividade e scan”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q257

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A função oculta a coluna na forma convencional.
- **B)** Incorreta. Conversão para texto também transforma a chave.
- **C)** Correta. No SQL conceitual, o intervalo expõe limites ordenados da coluna; a forma do literal deve ser adaptada ao dialeto.
- **D)** Incorreta. O cálculo ainda envolve a coluna.

**Conceito:** Sargabilidade por intervalo.

**Pegadinha:** Preservar função por parecer mais legível.

**Como pensar:** Reescreva o critério como limites inferior e superior da chave e alinhe seus tipos à sintaxe do produto.

### Comentário S3D6Q258

**Nível:** Médio

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O próximo ano exclusivo cobre todos os horários de 31/12 no tipo temporal delimitado, com sintaxe adaptada ao produto.
- **B)** Incorreta. B-tree aceita datas de qualquer mês.
- **C)** Incorreta. Faixa continua sendo faixa.
- **D)** Incorreta. Between funciona, mas um fim à meia-noite pode excluir horários.

**Conceito:** Limite superior exclusivo.

**Pegadinha:** Usar data final sem considerar tempo e precisão.

**Como pensar:** Feche o intervalo no primeiro instante que não pertence ao período e escreva o limite no tipo/dialeto correto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Limite superior exclusivo”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q259

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Cada escrita pode precisar manter a nova estrutura.
- **B)** Incorreta. Índice possui custo real.
- **C)** Incorreta. Estatísticas continuam relevantes.
- **D)** Incorreta. Índice não muda a semântica lógica correta.

**Conceito:** Custo de escrita do índice.

**Pegadinha:** Medir apenas select.

**Como pensar:** Inclua insert, update, delete, espaço e estatísticas na conta.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Custo colateral de índice”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q260

**Nível:** Difícil

**Uso:** Essenciais

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Os conceitos podem se relacionar sem serem sinônimos.
- **B)** Incorreta. Inverte regra lógica e mecanismo.
- **C)** Incorreta. Constraints podem ser apoiadas por índices.
- **D)** Correta. Distingue intenção lógica e implementação física.

**Conceito:** Constraint versus índice.

**Pegadinha:** Inferir equivalência porque o produto cria índice para unique.

**Como pensar:** Pergunte o que deve ser verdadeiro e qual estrutura ajuda a garantir.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Constraint e índice”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q261

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. B-tree também serve a leituras.
- **B)** Correta. Ordem das chaves pode apoiar faixa e ordenação compatível.
- **C)** Incorreta. Não corrige qualquer expressão automaticamente.
- **D)** Incorreta. Não executa join sem ler dados.

**Conceito:** Ordenação em B-tree.

**Pegadinha:** Reduzir B-tree a igualdade.

**Como pensar:** Compare a ordem solicitada com a ordem das chaves.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “B-tree e ordenação”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q262

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Hash não se limita a texto.
- **B)** Incorreta. Faixa pode usar B-tree.
- **C)** Correta. Sem ordem, não há percurso natural do intervalo.
- **D)** Incorreta. B-tree também aceita igualdade.

**Conceito:** Hash e intervalos.

**Pegadinha:** Associar hash a rapidez universal.

**Como pensar:** Faixa exige relação de ordem entre as chaves.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Hash e faixa”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q263

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Baixa seletividade não cria proibição eterna.
- **B)** Incorreta. Posição depende da carga.
- **C)** Correta. A coluna pode contribuir no contexto da consulta.
- **D)** Incorreta. Índice não vira constraint por cardinalidade.

**Conceito:** Seletividade contextual.

**Pegadinha:** Julgar coluna isoladamente.

**Como pensar:** Avalie combinação, cobertura, ordenação e subconjunto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Coluna pouco seletiva em composição”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q264

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Observação ausente do índice pode exigir acesso à tabela em B.
- **B)** Incorreta. Cobrir uma consulta não significa cobrir todas.
- **C)** Incorreta. Mesmo em produto que suporte `INCLUDE`, a cláusula não obriga a escolha do índice.
- **D)** Incorreta. A estrutura ainda custa na escrita.

**Conceito:** Cobertura relativa à projeção.

**Pegadinha:** Esquecer colunas de saída.

**Como pensar:** Compare toda necessidade de A e B com as colunas do índice.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Cobertura relativa”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q265

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Começa por status sem considerar o padrão informado.
- **B)** Incorreta. Faixa antes das igualdades pode limitar o prefixo.
- **C)** Incorreta. Vários índices isolados não equivalem ao composto nem dispensam medição.
- **D)** Correta. Igualdades primeiro e data depois formam candidato coerente, ainda sujeito a teste.

**Conceito:** Desenho de índice composto.

**Pegadinha:** Ordenar apenas por cardinalidade.

**Como pensar:** Parta das consultas reais: igualdades conjuntas, depois faixa/ordem.

### Comentário S3D6Q266

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Equivalência dos valores não impede que converter a coluna esconda a chave do caminho convencional.
- **B)** Correta. Converter a chave em cada linha pode impedir busca eficiente.
- **C)** Incorreta. A existência do índice não obriga o produto a mover a conversão para a entrada.
- **D)** Incorreta. Outro índice não remove a expressão aplicada à coluna no predicado.

**Conceito:** Conversão implícita e sargabilidade.

**Pegadinha:** Ignorar tipos no predicado.

**Como pensar:** Alinhe o tipo do parâmetro ao tipo da coluna indexada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Conversão implícita e busca”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q267

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Igualdade oferece busca precisa.
- **B)** Incorreta. Faixa pode aproveitar ordem.
- **C)** Incorreta. Prefixo conhecido pode ser buscável.
- **D)** Correta. Curinga inicial esconde o começo necessário ao percurso convencional.

**Conceito:** LIKE e prefixo.

**Pegadinha:** Tratar todos os padrões LIKE igualmente.

**Como pensar:** Veja se a parte inicial da chave é conhecida.

### Comentário S3D6Q268

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Função não cria chave primária.
- **B)** Incorreta. Expressões podem ter suporte específico.
- **C)** Correta. Índice compatível com a expressão muda o cenário.
- **D)** Incorreta. Índice alheio não resolve automaticamente.

**Conceito:** Índice por expressão.

**Pegadinha:** Aplicar a heurística como lei universal.

**Como pensar:** Pergunte se existe estrutura criada para exatamente aquela expressão.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Índice por expressão”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q269

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Índices, composição, seletividade e sargabilidade](semana_03_estudo.md#s3-d6-indices).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Poucas páginas e retorno total podem tornar scan mais barato.
- **B)** Incorreta. Escolha de scan não prova corrupção.
- **C)** Incorreta. Dica sem evidência é prematura.
- **D)** Incorreta. Plano físico não muda resposta lógica.

**Conceito:** Escolha baseada em custo.

**Pegadinha:** Eliminar qualquer scan visual.

**Como pensar:** Compare número de páginas e fração de linhas necessárias.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Índice não garante uso”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q270

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Uma leitura isolada não domina todo o serviço.
- **B)** Correta. A decisão deve ponderar frequência e custos dos dois fluxos.
- **C)** Incorreta. Remover constraints troca desempenho por invalidade potencial.
- **D)** Incorreta. Uma métrica não encerra a otimização.

**Conceito:** Trade-off leitura e escrita.

**Pegadinha:** Celebrar o melhor número isolado.

**Como pensar:** Calcule impacto acumulado por frequência e criticidade.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Diagnóstico integrado de índice”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q271

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Custo não é cronômetro universal.
- **B)** Correta. É valor comparativo interno entre alternativas.
- **C)** Incorreta. Estimativa não é linha real exata.
- **D)** Incorreta. Não representa diretamente CPU medida.

**Conceito:** Custo estimado.

**Pegadinha:** Ler custo como milissegundo.

**Como pensar:** Use custo para comparar planos no mesmo contexto.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Custo do otimizador”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q272

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Distribuição é insumo das estimativas; estatísticas antigas podem mudar cardinalidades previstas.
- **B)** Incorreta. O efeito não se limita à apresentação: estimativas orientam a escolha do plano.
- **C)** Incorreta. Linhas reais continuam sendo produzidas na execução; o problema está na previsão usada para planejar.
- **D)** Correta. Cardinalidade errada distorce ordem e método escolhidos.

**Conceito:** Estatísticas e estimativa.

**Pegadinha:** Olhar apenas para o operador final.

**Como pensar:** Rastreie de onde veio a primeira estimativa ruim.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Estatísticas desatualizadas”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q273

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A discrepância maciça pede investigar estatística, correlação ou predicado.
- **B)** Incorreta. Atualizar estatísticas é hipótese, não encerramento; a nova estimativa precisa ser conferida.
- **C)** Incorreta. Forçar hash join atua depois da estimativa e pode mascarar a causa sem corrigi-la.
- **D)** Incorreta. Índices indiscriminados não explicam nem necessariamente corrigem distribuição ou correlação.

**Conceito:** Estimado versus real.

**Pegadinha:** Forçar operador antes de corrigir a causa.

**Como pensar:** Comece no primeiro nó em que estimado e real divergem.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Estimado versus real”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q274

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Índice não é condição absoluta.
- **B)** Incorreta. Duas entradas enormes podem tornar o loop caro.
- **C)** Correta. Poucas linhas externas e acesso interno eficiente favorecem o método.
- **D)** Incorreta. Não se limita a condições sem igualdade.

**Conceito:** Nested loop contextual.

**Pegadinha:** Rotular loop como sempre lento.

**Como pensar:** Multiplique aproximadamente linhas externas pelo custo do acesso interno.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Nested loop contextual”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q275

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O operador pode construir sua própria estrutura em memória.
- **B)** Incorreta. Ordenação prévia caracteriza mais o merge.
- **C)** Correta. Igualdade e conjuntos relevantes podem favorecer hash sem índice hash.
- **D)** Incorreta. Nenhum método é sempre superior.

**Conceito:** Hash join.

**Pegadinha:** Confundir hash join com índice hash.

**Como pensar:** Separe estrutura transitória do operador e índice persistente.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Hash join”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q276

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Predicado incompatível não favorece o método.
- **B)** Correta. Ordem disponível e condição compatível podem torná-lo vantajoso.
- **C)** Incorreta. Sem relação não há junção significativa.
- **D)** Incorreta. Índice hash não é requisito.

**Conceito:** Merge join.

**Pegadinha:** Supor ordenação obrigatória durante toda execução.

**Como pensar:** Veja se as entradas já chegam na ordem necessária.

### Comentário S3D6Q277

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Where não torna índice obrigatório.
- **B)** Incorreta. Chave primária não impede scan.
- **C)** Incorreta. Sargabilidade não é o único fator.
- **D)** Correta. Tabela pequena ou retorno amplo podem favorecer leitura sequencial.

**Conceito:** Scan baseado em custo.

**Pegadinha:** Usar a palavra scan como diagnóstico completo.

**Como pensar:** Calcule tamanho e proporção visitada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Scan não é falha automática”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q278

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Operador seletivo no nome pode ainda processar volume e acessos caros.
- **B)** Incorreta. Seek não certifica plano ótimo.
- **C)** Incorreta. Plano físico não muda resultado lógico.
- **D)** Incorreta. Estatísticas continuam orientando estimativas.

**Conceito:** Seek e trabalho total.

**Pegadinha:** Avaliar plano por um único rótulo.

**Como pensar:** Siga linhas, loops e acessos até o custo acumulado.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Seek não garante rapidez”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q279

**Nível:** Médio

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A divergência cedo na árvore pode contaminar escolhas posteriores.
- **B)** Incorreta. Percentual estimado não supera uma divergência real que contamina os nós posteriores.
- **C)** Incorreta. Scan barato não é falha.
- **D)** Incorreta. Posição visual não garante que o nó seja a origem da primeira estimativa incorreta.

**Conceito:** Discrepância cardinal.

**Pegadinha:** Escolher operador visualmente chamativo.

**Como pensar:** Localize o primeiro grande desvio estimado-real.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Maior discrepância no plano”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q280

**Nível:** Difícil

**Uso:** Aprofundamento

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. SQL Server não usa essa sintaxe genérica como os outros.
- **B)** Incorreta. Analyze executa para produzir métricas no PostgreSQL.
- **C)** Correta. A comparação fixa PostgreSQL 18.4, MySQL 9.7 LTS e SQL Server 2025 17.x e preserva suas interfaces próprias.
- **D)** Incorreta. Plano real exige execução do trabalho medido.

**Conceito:** Planos nos três SGBDs.

**Pegadinha:** Transportar sintaxe entre dialetos.

**Como pensar:** Fixe produto e distinga estimativa de execução.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “EXPLAIN nos três produtos”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q281

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. DML pode ter plano.
- **B)** Correta. Métrica real pode executar a alteração; o teste precisa de controle.
- **C)** Incorreta. Plano não concede commit automaticamente.
- **D)** Incorreta. Estatística não elimina rollback.

**Conceito:** Cuidado com plano real de DML.

**Pegadinha:** Tratar análise como leitura inofensiva.

**Como pensar:** Antes de medir, determine se a ferramenta executará a instrução.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Plano real e DML”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q282

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Começa pela solução sem diagnóstico.
- **B)** Incorreta. Muda fatores demais e cenário.
- **C)** Incorreta. Mede tarde e destrói evidência.
- **D)** Correta. A sequência preserva linha de base, hipótese e comparação.

**Conceito:** Protocolo de otimização.

**Pegadinha:** Criar índice antes de formular hipótese.

**Como pensar:** Registre o antes, mude uma coisa e repita a mesma medida.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Protocolo de otimização”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q283

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não é objetivo reduzir a linguagem.
- **B)** Incorreta. Nenhuma mudança garante ganho.
- **C)** Incorreta. Plano real ainda é necessário.
- **D)** Correta. Isola causalidade operacional e facilita reversão.

**Conceito:** Mudança controlada.

**Pegadinha:** Aplicar pacote de alterações e atribuir ganho a uma delas.

**Como pensar:** Faça experimento com uma variável.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Uma mudança por vez”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q284

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Dica pode cristalizar escolha e esconder estimativa ruim.
- **B)** Incorreta. Dicas não são sempre erro sintático.
- **C)** Incorreta. Produtos possuem recursos diversos.
- **D)** Incorreta. Dica não atualiza estatística.

**Conceito:** Uso responsável de hints.

**Pegadinha:** Forçar o operador desejado pelo olhar.

**Como pensar:** Investigue a causa antes de restringir o otimizador.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Dicas de plano”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q285

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Sem indício de mudança recente, não se pode declarar desatualização como causa necessária.
- **B)** Incorreta. Maior amostra por coluna não representa automaticamente a dependência entre UF e cidade.
- **C)** Correta. Dependência entre cidade e UF pode invalidar independência assumida.
- **D)** Incorreta. Mudar o join não corrige a cardinalidade já estimada no filtro correlacionado.

**Conceito:** Correlação estatística.

**Pegadinha:** Atacar operador posterior.

**Como pensar:** Corrija a estimativa na origem e então reavalie o plano.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Correlação entre colunas”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q286

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Índices adicionais podem custar mais que ler poucas páginas.
- **B)** Correta. Aceita o plano quando os dados justificam.
- **C)** Incorreta. Nested loop não substitui scan da entrada.
- **D)** Incorreta. Desnormalização não é resposta à palavra scan.

**Conceito:** Scan de tabela pequena.

**Pegadinha:** Otimizar aparência do plano.

**Como pensar:** Compare páginas totais com acessos alternativos.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Tabela de 40 linhas”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q287

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Relatório isolado não mede custo total.
- **B)** Correta. Frequência e criticidade convertem latências em impacto real.
- **C)** Incorreta. Quantidade de execuções sem duração, escrita, espaço e criticidade não mede impacto acumulado.
- **D)** Incorreta. Frequência não elimina o SLA do fluxo menos frequente e potencialmente crítico.

**Conceito:** Custo global.

**Pegadinha:** Escolher a métrica que mais melhorou.

**Como pensar:** Pondere cada fluxo por frequência e importância.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Custo global do serviço”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q288

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Otimizador não redefine negócio.
- **B)** Incorreta. Estimativa não garante ótimo universal.
- **C)** Correta. Plano escolhido produz dados reais para comparação.
- **D)** Incorreta. Estatísticas continuam sendo insumo.

**Conceito:** Fluxo de otimização.

**Pegadinha:** Confundir escolha estimada com certeza.

**Como pensar:** Compare a expectativa do plano com a execução observada.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Fluxo do otimizador”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q289

**Nível:** Médio

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Parâmetros diferentes enviesam a comparação.
- **B)** Incorreta. Ambiente distinto destrói a linha de base.
- **C)** Incorreta. Custo estimado sozinho é insuficiente.
- **D)** Correta. Mesmo cenário e parâmetros tornam as métricas comparáveis.

**Conceito:** Experimento reproduzível.

**Pegadinha:** Mudar a carga junto da solução.

**Como pensar:** Congele o cenário antes e depois.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Parâmetros representativos”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q290

**Nível:** Difícil

**Uso:** Revisão

**Referência:** [Estatísticas, otimizador e EXPLAIN](semana_03_estudo.md#s3-d6-otimizacao).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. O registro liga hipótese, evidência, efeito lateral e decisão.
- **B)** Incorreta. Frase sem medida não é reprodutível.
- **C)** Incorreta. Um nó isolado perde contexto.
- **D)** Incorreta. Quantidade de índices não indica qualidade.

**Conceito:** Decisão documentada.

**Pegadinha:** Encerrar com sensação subjetiva.

**Como pensar:** Escreva por que manteve ou reverteu com números comparáveis.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Decisão baseada em evidência”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q291

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Nomes semelhantes podem esconder garantias diferentes.
- **B)** Incorreta. Sintaxe não é automaticamente portátil.
- **C)** Correta. Versão e contexto limitam a afirmação de modo responsável.
- **D)** Incorreta. Fonte primária continua necessária.

**Conceito:** Comparação versionada.

**Pegadinha:** Universalizar experiência de um produto.

**Como pensar:** Escreva sempre produto, versão, conceito e configuração relevante.

### Comentário S3D6Q292

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Finalidade comum não torna sintaxe comum.
- **B)** Incorreta. Order by não torna TOP portátil.
- **C)** Incorreta. Os produtos limitam linhas.
- **D)** Correta. TOP identifica T-SQL; LIMIT é usual nos outros dois.

**Conceito:** Portabilidade de limitação.

**Pegadinha:** Confundir função equivalente com mesma gramática.

**Como pensar:** Reconheça o dialeto antes de validar a instrução.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “TOP e portabilidade”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q293

**Nível:** Médio

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. A organização não é idêntica nos três.
- **B)** Correta. Resume heap comum, opção clustered e a regra completa do InnoDB: PK, `UNIQUE NOT NULL` adequado ou índice oculto.
- **C)** Incorreta. SQL Server possui nonclustered.
- **D)** Incorreta. InnoDB não é heap comum nesse sentido.

**Conceito:** Organização física comparada.

**Pegadinha:** Projetar o modelo clustered em todos.

**Como pensar:** Associe cada afirmação ao produto e ao engine e confira o fallback quando não houver PK explícita.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Organização física principal”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q294

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. É a associação versionada ensinada.
- **B)** Incorreta. PostgreSQL oferece explain e SQL Server possui planos.
- **C)** Incorreta. MySQL atual oferece explain.
- **D)** Incorreta. A sintaxe e ferramentas não são idênticas.

**Conceito:** Obtenção de planos.

**Pegadinha:** Copiar comando entre dialetos.

**Como pensar:** Compare o mesmo conceito por interfaces próprias.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Forma de obter plano”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q295

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [PostgreSQL 18.4, SQL Server 2025 17.x e MySQL 9.7 LTS](semana_03_estudo.md#s3-d6-sgbds).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. InnoDB possui comportamentos que não devem ser atribuídos a qualquer engine.
- **B)** Incorreta. Engine não muda todo SQL padrão universalmente.
- **C)** Incorreta. Versão e engine são dimensões complementares.
- **D)** Incorreta. Os outros produtos não usam InnoDB.

**Conceito:** Escopo de afirmação no MySQL.

**Pegadinha:** Dizer “MySQL faz” quando a propriedade é do engine.

**Como pensar:** Registre versão e mecanismo antes de comparar organização ou concorrência.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Engine no MySQL”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q296

**Nível:** Médio

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Dashboard é apenas uma possível interface.
- **B)** Correta. A definição inclui processo humano e técnico orientado à decisão.
- **C)** Incorreta. BI não é um banco operacional isolado.
- **D)** Incorreta. Carga é uma etapa, não o conceito inteiro.

**Conceito:** Business Intelligence.

**Pegadinha:** Reduzir BI à ferramenta visível.

**Como pensar:** Pergunte como dados se tornam análise útil para pessoas decidirem.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Definição de BI”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q297

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A ordem está invertida.
- **B)** Incorreta. Ambas são perguntas analíticas.
- **C)** Correta. Estado corrente é transacional; evolução agregada é analítica.
- **D)** Incorreta. As perguntas não distinguem as duas cargas.

**Conceito:** OLTP versus OLAP.

**Pegadinha:** Usar presença de banco como critério.

**Como pensar:** Classifique por registrar estado corrente ou analisar histórico.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “OLTP e OLAP”; a extensão decorre dessa precisão técnica, não de pista formal.

### Comentário S3D6Q298

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Arquivo não corresponde ao evento medido.
- **B)** Incorreta. Interações duplicariam atendimentos.
- **C)** Incorreta. Dimensão não define a ocorrência do fato.
- **D)** Correta. Uma linha por atendimento concluído estabiliza contagem e espera.

**Conceito:** Granularidade da fato.

**Pegadinha:** Escolher colunas antes do grão.

**Como pensar:** Complete “uma linha representa...” antes de criar medidas.

### Comentário S3D6Q299

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Média simples dá peso igual a grupos de tamanhos distintos.
- **B)** Correta. Somar tempos 20+360 e dividir por 20 resulta em 19.
- **C)** Incorreta. O maior grupo pesa mais, mas não substitui o menor.
- **D)** Incorreta. Somar médias não produz média global.

**Conceito:** Média ponderada pelo número de fatos.

**Pegadinha:** Tratar média como plenamente aditiva.

**Como pensar:** Recupere soma e contagem de cada grupo.

### Comentário S3D6Q300

**Nível:** Difícil

**Uso:** Simulado

**Referência:** [BI, modelagem dimensional e ETL/ELT](semana_03_estudo.md#s3-d6-bi).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. A ordem foi invertida.
- **B)** Incorreta. Processo e repositório são conceitos diferentes.
- **C)** Correta. T antes de L define ETL; L antes de T define ELT.
- **D)** Incorreta. Ambos exigem qualidade, linhagem e reconciliação.

**Conceito:** ETL versus ELT.

**Pegadinha:** Definir pelo nome da plataforma.

**Como pensar:** Marque fisicamente onde a transformação ocorre em relação à carga final.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “ETL e ELT”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.1

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Leis de De Morgan
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Essa é a conjunção das duas negações, não a negação de uma conjunção.
- **B)** Incorreta. Mantém os termos positivos.
- **C)** Correta. Negar P e Q resulta em não P ou não Q.
- **D)** Incorreta. Cria implicação inexistente.

**Conceito:** Negação de conjunção.

**Pegadinha:** Negar termos sem trocar o conectivo.

**Como pensar:** Troque `e` por `ou` e negue ambos.

#### Comentário Extra Dia 6.2

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Implicação
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. A implicação falha exatamente com antecedente verdadeiro e consequente falso.
- **B)** Incorreta. Não representa o caso de falha.
- **C)** Incorreta. É contraposição, não negação.
- **D)** Incorreta. Disjunção proposta equivale à implicação original.

**Conceito:** Negação da implicação.

**Pegadinha:** Negar os dois lados mecanicamente.

**Como pensar:** Use P e não Q.

#### Comentário Extra Dia 6.3

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Quantificadores
- **Nível:** Médio
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. “Nenhum” é mais forte que a negação necessária.
- **B)** Incorreta. Universal negativo também é excessivo.
- **C)** Incorreta. Afirma caso positivo e não nega o universal.
- **D)** Correta. Um contraexemplo basta para negar “todo”.

**Conceito:** Negação de universal.

**Pegadinha:** Trocar todo por nenhum.

**Como pensar:** Procure um elemento da classe que não tenha a propriedade.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Negação do universal”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.4

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Inclusão-exclusão
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Soma simples conta a interseção duas vezes.
- **B)** Correta. `50+35−20=65`.
- **C)** Incorreta. Subtrai a interseção duas vezes.
- **D)** Incorreta. Ultrapassa o total do universo.

**Conceito:** União de conjuntos.

**Pegadinha:** Somar os grupos sem descontar repetição.

**Como pensar:** Some A e B e retire uma cópia da interseção.

#### Comentário Extra Dia 6.5

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Raciocínio Lógico
- **Assunto:** Porcentagem
- **Nível:** Difícil
- **Uso:** Essenciais
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Percentuais usam bases diferentes.
- **B)** Correta. Os fatores multiplicam para 0,96.
- **C)** Incorreta. O desconto não incide sobre 100.
- **D)** Incorreta. 104 corresponderia a outra combinação.

**Conceito:** Percentuais sucessivos.

**Pegadinha:** Somar +20 e −20.

**Como pensar:** Aplique cada fator ao resultado anterior.

#### Comentário Extra Dia 6.6

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Modos de colaboração
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Comentário discute e não edita diretamente.
- **B)** Incorreta. Sugestão e edição têm efeitos diferentes.
- **C)** Incorreta. Histórico não é comentário.
- **D)** Correta. A alternativa separa proposta, discussão e alteração direta.

**Conceito:** Colaboração no Documentos.

**Pegadinha:** Confundir intenção com efeito no texto.

**Como pensar:** Pergunte se o conteúdo mudou, aguarda aceite ou apenas recebeu debate.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Sugestão, comentário e edição”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.7

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Versões e permissões
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Permissão adequada permite localizar estados anteriores.
- **B)** Incorreta. A função do histórico é justamente comparar estados anteriores, não exibir só o atual.
- **C)** Incorreta. O registro de versões não depende de renomear ou copiar manualmente cada estado.
- **D)** Incorreta. Abrir o histórico não restaura versão nem impõe mudança automática aos colaboradores.

**Conceito:** Histórico de versões.

**Pegadinha:** Imaginar acesso irrestrito a qualquer pessoa.

**Como pensar:** Considere a função e a permissão do usuário.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Histórico de versões”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.8

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Documentos
- **Assunto:** Estilos
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Fonte grande não bloqueia edição.
- **B)** Incorreta. Estilo não apaga histórico.
- **C)** Correta. Título cria estrutura; tamanho isolado é aparência.
- **D)** Incorreta. Título pode ter qualquer formatação compatível.

**Conceito:** Estilo semântico.

**Pegadinha:** Confundir visual com estrutura.

**Como pensar:** Veja se o recurso cria papel de título reconhecido.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Título semântico”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.9

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Médio
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Isso seria referência absoluta.
- **B)** Incorreta. A referência relativa deve se deslocar.
- **C)** Incorreta. Apenas a coluna mudou, faltando a linha.
- **D)** Correta. Uma coluna e uma linha adiante levam A2 a B3.

**Conceito:** Referência relativa.

**Pegadinha:** Mover só um componente.

**Como pensar:** Aplique ao endereço o mesmo deslocamento da cópia.

#### Comentário Extra Dia 6.10

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referências de célula
- **Nível:** Difícil
- **Uso:** Aprofundamento
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Nenhum componente está fixo.
- **B)** Correta. Os dois cifrões fixam coluna e linha.
- **C)** Incorreta. Fixa apenas a coluna.
- **D)** Incorreta. Fixa apenas a linha.

**Conceito:** Referência absoluta.

**Pegadinha:** Tratar referência mista como absoluta.

**Como pensar:** Leia cada cifrão somente para o componente seguinte.

#### Comentário Extra Dia 6.11

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Referência mista
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Move componentes que estavam fixos.
- **B)** Incorreta. Não move as partes relativas.
- **C)** Correta. A fica fixa, linha vira 3; B vira C, linha 1 fica fixa.
- **D)** Incorreta. Perde cifrões e desloca incorretamente.

**Conceito:** Cópia de referência mista.

**Pegadinha:** Mover tudo ou nada.

**Como pensar:** Resolva coluna e linha de cada termo separadamente.

#### Comentário Extra Dia 6.12

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Ordenação de tabela
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Ordenar o conjunto preserva a correspondência das linhas.
- **B)** Incorreta. Coluna isolada separa notas de nomes.
- **C)** Incorreta. Mover dados não é necessário.
- **D)** Incorreta. Cifrões afetam fórmulas, não proteção da ordenação.

**Conceito:** Ordenação de registros.

**Pegadinha:** Tratar coluna como lista independente.

**Como pensar:** Selecione todas as colunas que compõem cada registro.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Ordenação segura”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.13

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Google Planilhas
- **Assunto:** Localização de fórmulas
- **Nível:** Médio
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Configuração pode alterar nomes e separadores sem mudar a finalidade.
- **B)** Incorreta. Vírgula não é universal.
- **C)** Incorreta. Referências relativas continuam existindo.
- **D)** Incorreta. Idioma não é o único determinante do resultado.

**Conceito:** Localização de fórmulas.

**Pegadinha:** Julgar fórmula apenas pela grafia.

**Como pensar:** Interprete operação e referências antes do separador.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Função e configuração regional”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.14

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Transporte e privacidade
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. TLS não certifica honestidade do conteúdo.
- **B)** Incorreta. O site continua recebendo a conexão.
- **C)** Incorreta. Modo privado não substitui certificado.
- **D)** Correta. Delimita proteção de trânsito e redução de rastros locais.

**Conceito:** HTTPS e modo privado.

**Pegadinha:** Somar dois controles e inferir anonimato.

**Como pensar:** Especifique o que cada controle protege e perante quem.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “HTTPS e navegação privada”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.15

- **Dia:** Dia 6
- **Bloco:** Bloco 4
- **Matéria:** Internet
- **Assunto:** Verificação de destino
- **Nível:** Difícil
- **Uso:** Revisão
- **Referência:** [D+2, D+7, RLM, Google Documentos, Planilhas e internet](semana_03_estudo.md#s3-d6-b4).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Logotipo pode ser copiado.
- **B)** Correta. Host e canal oficial validam o destinatário esperado.
- **C)** Incorreta. Histórico não autentica instituição.
- **D)** Incorreta. Limpar cache não transforma domínio falso em oficial.

**Conceito:** Phishing e host.

**Pegadinha:** Confiar na aparência.

**Como pensar:** Cheque o domínio antes de qualquer segredo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Credencial e host”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.16

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Concordância
- **Nível:** Médio
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. O núcleo singular “análise” exige “demonstra”.
- **B)** Incorreta. Artigo e núcleo estão sem concordância.
- **C)** Correta. Sujeito composto plural concorda com “fortalecem”.
- **D)** Incorreta. Há erros em “existem” e “preservados”.

**Conceito:** Concordância verbal e nominal.

**Pegadinha:** Concordar com o termo plural mais próximo.

**Como pensar:** Localize os núcleos do sujeito antes do verbo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Concordância com sujeito distante”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.17

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Regência e crase
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** D.

**Análise das alternativas:**

- **A)** Incorreta. Não há crase antes de infinitivo nesse uso.
- **B)** Incorreta. “Todos” não admite artigo feminino.
- **C)** Incorreta. Obedecer rege preposição a: “às normas”.
- **D)** Correta. “Às decisões” recebe preposição e artigo; “respeito aos direitos” mantém a regência adequada.

**Conceito:** Regência e crase.

**Pegadinha:** Inserir acento grave diante de qualquer complemento.

**Como pensar:** Verifique primeiro a preposição exigida e depois o artigo.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Crase e regência”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.18

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Pontuação
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** A.

**Análise das alternativas:**

- **A)** Correta. Sujeito e verbo permanecem unidos.
- **B)** Incorreta. A vírgula separa “análise” de “permite”.
- **C)** Incorreta. Separa sujeito composto de “fortalecem”.
- **D)** Incorreta. Separa o sujeito longo de “devem” sem intercalação.

**Conceito:** Vírgula e estrutura sintática.

**Pegadinha:** Pausar oralmente e inserir vírgula entre sujeito e verbo.

**Como pensar:** Ache o verbo e seu sujeito antes de pontuar.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Vírgula entre sujeito e verbo”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.19

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Português
- **Assunto:** Progressão textual
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** C.

**Análise das alternativas:**

- **A)** Incorreta. Referente e absolutismo prejudicam a frase.
- **B)** Incorreta. Há erro de concordância e pronome ambíguo.
- **C)** Correta. “Esse aumento” fixa referente e “contudo” marca contraste.
- **D)** Incorreta. O período é truncado e sem relação lógica.

**Conceito:** Coesão e contraste.

**Pegadinha:** Preservar palavras sem preservar a lógica.

**Como pensar:** Cheque referente, conector e completude do período.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Coerência e referência”; a extensão decorre dessa precisão técnica, não de pista formal.

#### Comentário Extra Dia 6.20

- **Dia:** Dia 6
- **Bloco:** Bloco 5
- **Matéria:** Discursiva
- **Assunto:** Fechamento argumentativo
- **Nível:** Difícil
- **Uso:** Simulado
- **Referência:** [Português e texto integral manuscrito](semana_03_estudo.md#s3-d6-b5).

**Alternativa correta:** B.

**Análise das alternativas:**

- **A)** Incorreta. Abre argumento novo no fechamento.
- **B)** Correta. Retoma os três eixos do tema sem acrescentar razão inédita.
- **C)** Incorreta. Jargão técnico foge da função conclusiva.
- **D)** Incorreta. Promessa absoluta excede o que o texto pode sustentar.

**Conceito:** Conclusão da dissertação.

**Pegadinha:** Usar a conclusão para estrear ideia.

**Como pensar:** Reformule a tese e sintetize, sem inaugurar outro desenvolvimento.

**Justificativa de comprimento:** A alternativa correta precisa explicitar as condições de “Conclusão da dissertação”; a extensão decorre dessa precisão técnica, não de pista formal.

---
