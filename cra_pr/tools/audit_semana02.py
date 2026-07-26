from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parents[1]
study = (root / "Analista de sistemas/semana_02/semana_02_estudo.md").read_text(encoding="utf-8")
bank = (root / "Analista de sistemas/semana_02/semana_02_questoes.md").read_text(encoding="utf-8")
super_text = (root / "Analista de sistemas/semana_02/semana_02_super_simulado.md").read_text(encoding="utf-8")
journey = (root / "Analista de sistemas/semana_02/semana_02_jornada.md").read_text(encoding="utf-8")
discursive = (root / "Analista de sistemas/semana_02/semana_02_dissertacoes.md").read_text(encoding="utf-8")
errors: list[str] = []


def expect(label: str, actual: int, wanted: int) -> None:
    if actual != wanted:
        errors.append(f"{label}: {actual}, esperado {wanted}")


expect("principais", len(re.findall(r"^### S2D[1-6]Q\d{3} —", bank, re.M)), 300)
expect("comentários principais", len(re.findall(r"^### Comentário S2D[1-6]Q\d{3}$", bank, re.M)), 300)
expect("extras", len(re.findall(r"^#### Extra Dia [1-6]\.\d+$", bank, re.M)), 120)
expect("comentários extras", len(re.findall(r"^#### Comentário Extra Dia [1-6]\.\d+$", bank, re.M)), 120)
expect("super", len(re.findall(r"^### S2S\d{3} —", super_text, re.M)), 60)
expect("comentários super", len(re.findall(r"^### Comentário S2S\d{3}$", super_text, re.M)), 60)
expect("dias da jornada", len(re.findall(r"^## Dia [1-6]\b", journey, re.M)), 6)
expect("sessões A operacionais na jornada", len(re.findall(r"^### Sessão A$", journey, re.M)), 6)
expect(
    "sessões B operacionais na jornada",
    len(re.findall(r"^### Sessão B(?: ajustada)?$", journey, re.M)),
    6,
)
expect("etapas discursivas", len(re.findall(r'^<a id="s2-disc-d[1-6]"></a>$', discursive, re.M)), 6)
expect("alternativas do banco", len(re.findall(r"^[A-D]\) ", bank, re.M)), 420 * 4)
expect("alternativas do super", len(re.findall(r"^[A-D]\) ", super_text, re.M)), 60 * 4)
if re.search(r"(?m)^E\)\s+", bank + "\n" + super_text):
    errors.append("alternativa E encontrada")
expect("análises A-D do banco", len(re.findall(r"^- \*\*[A-D]\)\*\*", bank, re.M)), 420 * 4)
expect("análises A-D do super", len(re.findall(r"^- \*\*[A-D]\)\*\*", super_text, re.M)), 60 * 4)

levels = Counter(re.findall(r"^(?:- )?\*\*Nível:\*\* (Médio|Difícil|Muito difícil)$", bank, re.M))
expect("rótulos válidos de nível no banco", sum(levels.values()), 420 * 2)

super_levels = Counter(re.findall(r"^\*\*Nível:\*\* (Médio|Difícil|Muito difícil)$", super_text, re.M))
expect("rótulos válidos de nível no super", sum(super_levels.values()), 60 * 2)

uses = Counter(
    re.findall(r"^(?:- )?\*\*Uso:\*\* (Essenciais|Aprofundamento|Revisão|Simulado)$", bank, re.M)
)
expect("rótulos válidos de uso no banco", sum(uses.values()), 420 * 2)
super_uses = Counter(re.findall(r"^\*\*Uso:\*\* (Simulado)$", super_text, re.M))
expect("rótulos válidos de uso no super", sum(super_uses.values()), 60 * 2)

answers = re.findall(r"\*\*Alternativa correta:\s*([A-D])\.\*\*", bank)
expect("gabaritos nos comentários do banco", len(answers), 420)
super_answers = re.findall(r"\*\*Alternativa correta:\s*([A-D])\.\*\*", super_text)
expect("gabaritos nos comentários do super", len(super_answers), 60)

for seq_name, seq in (("banco", answers), ("super", super_answers)):
    if any(seq[i] == seq[i + 1] == seq[i + 2] for i in range(len(seq) - 2)):
        errors.append(f"{seq_name}: sequência de três gabaritos iguais")

    motif_hits: list[tuple[int, str]] = []
    for width in range(2, 5):
        for start in range(len(seq) - 3 * width + 1):
            motif = seq[start : start + width]
            if seq[start : start + 3 * width] == motif * 3:
                motif_hits.append((start + 1, "".join(motif)))
    if motif_hits:
        preview = ", ".join(f"posição {start}: {motif}" for start, motif in motif_hits[:5])
        errors.append(f"{seq_name}: motivo curto repetido três vezes ({preview})")

    for width in range(2, len(seq) // 3 + 1):
        if len(seq) % width == 0 and seq == seq[:width] * (len(seq) // width):
            errors.append(
                f"{seq_name}: gabarito inteiro é um bloco de {width} letras repetido {len(seq) // width} vezes"
            )
            break


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    text = re.sub(r"[^a-z0-9 _-]", "", text).strip().replace(" ", "-")
    return re.sub(r"-+", "-", text)


anchors = set(re.findall(r'<a id="([^"]+)"', study))
anchors.update(slug(value) for value in re.findall(r"^#{1,6}\s+(.+)$", study, re.M))
for source_name, source in (("banco", bank), ("super", super_text), ("jornada", journey)):
    fragments = re.findall(r"semana_02_estudo\.md#([a-zA-Z0-9_.-]+)", source)
    missing = sorted({fragment for fragment in fragments if fragment not in anchors})
    if missing:
        errors.append(f"{source_name}: âncoras ausentes: {', '.join(missing[:10])}")

discursive_anchors = set(re.findall(r'<a id="([^"]+)"', discursive))
journey_discursive_fragments = set(
    re.findall(r"semana_02_dissertacoes\.md#([a-zA-Z0-9_.-]+)", journey)
)
missing_discursive = sorted(journey_discursive_fragments - discursive_anchors)
if missing_discursive:
    errors.append(f"jornada: âncoras discursivas ausentes: {', '.join(missing_discursive)}")

bank_main_ids = set(re.findall(r"(?m)^### (S2D[1-6]Q\d{3})\b", bank))
journey_question_ids = set(re.findall(r"\bS2D[1-6]Q\d{3}\b", journey))
missing_journey_ids = sorted(journey_question_ids - bank_main_ids)
if missing_journey_ids:
    errors.append(f"jornada: IDs de questões ausentes: {', '.join(missing_journey_ids)}")


def minutes_in_table(source: str, start_heading: str, end_heading: str) -> int:
    match = re.search(
        rf"(?ms)^{re.escape(start_heading)}\s*$.*?(?=^{re.escape(end_heading)}\s*$)",
        source,
    )
    if not match:
        errors.append(f"jornada: trecho de tempo ausente: {start_heading}")
        return -1
    return sum(int(value) for value in re.findall(r"\|\s*(\d+) min\s*\|", match.group(0)))


if minutes_in_table(journey, "### Sessão A - 2h50", "### Sessão B - 2h50") != 170:
    errors.append("jornada: Sessão A não soma 170 minutos")
if minutes_in_table(journey, "### Sessão B - 2h50", "### Consolidação - 20 min") != 170:
    errors.append("jornada: Sessão B não soma 170 minutos")
if minutes_in_table(journey, "### Sessão B ajustada", "## D+2 que vence depois dos seis dias") != 170:
    errors.append("jornada: Sessão B ajustada do Dia 6 não soma 170 minutos")

for day in range(1, 7):
    day_match = re.search(
        rf"(?ms)^# Dia {day}\b.*?(?=^# Dia {day + 1}\b|\Z)",
        study,
    )
    if not day_match:
        errors.append(f"estudo: Dia {day} ausente")
        continue
    section = day_match.group(0)
    markers = (
        "## Exemplos práticos e resolvidos",
        "## Prática guiada",
        f"## Blocos 4–6 programados do Dia {day}",
        f"## Tabela de revisão rápida do Dia {day}",
        "## Checklist",
    )
    positions = [section.find(marker) for marker in markers]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append(f"estudo: ordem física inválida no Dia {day}: {positions}")

if any(label in study for label in ("Data D1:", "Data D7:", "Data D30:")):
    errors.append("estudo: ciclo legado D1/D7/D30 encontrado")

for day in range(1, 7):
    if f"Extra Dia {day}.1–{day}.5" not in journey:
        errors.append(f"jornada: faixa de extras Essenciais do Dia {day} ausente no D+7")

discursive_requirements = (
    "Vale 20 pontos",
    "20 a 30 linhas",
    "no mínimo 12 pontos",
    "tempo total de 4 horas",
    "## Dia 6 - Texto completo, 45 minutos",
    "| **Total** | **20** |",
    "somente a Folha de Texto Definitivo é avaliada",
    "até a 30ª posição de cada lista",
)
for requirement in discursive_requirements:
    if requirement not in discursive:
        errors.append(f"discursiva: requisito ausente: {requirement}")


def indexed_sections(source: str, heading_pattern: str) -> dict[str, str]:
    matches = list(re.finditer(rf"(?m)^#{{3,4}} {heading_pattern}.*$", source))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        item_id = match.group(1)
        if item_id in result:
            errors.append(f"seção duplicada: {item_id}")
        result[item_id] = source[match.start():end]
    return result


def metadata(section: str, label: str) -> str | None:
    match = re.search(
        rf"(?m)^(?:- )?\*\*{re.escape(label)}:\*\*\s*([^\r\n]+)",
        section,
    )
    if not match:
        return None
    return match.group(1).strip().rstrip(".")


def compare_metadata(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
    fields: tuple[str, ...] = ("Nível", "Uso", "Referência"),
) -> None:
    if set(items) != set(comments):
        errors.append(f"{label}: IDs de itens e comentários não coincidem")
        return
    for item_id in sorted(items):
        for field_name in fields:
            left = metadata(items[item_id], field_name)
            right = metadata(comments[item_id], field_name)
            if left is None or right is None:
                errors.append(f"{label} {item_id}: campo {field_name} ausente")
            elif left != right:
                errors.append(f"{label} {item_id}: campo {field_name} divergente")


compare_metadata(
    "principal",
    indexed_sections(bank, r"(S2D[1-6]Q\d{3})\b"),
    indexed_sections(bank, r"Comentário (S2D[1-6]Q\d{3})\b"),
)
compare_metadata(
    "extra",
    indexed_sections(bank, r"(Extra Dia [1-6]\.\d+)\b"),
    indexed_sections(bank, r"Comentário (Extra Dia [1-6]\.\d+)\b"),
)
compare_metadata(
    "super",
    indexed_sections(super_text, r"(S2S\d{3})\b"),
    indexed_sections(super_text, r"Comentário (S2S\d{3})\b"),
)


def exact_sections(source: str, heading_pattern: str) -> dict[str, str]:
    matches = list(re.finditer(rf"(?m)^#{{3,4}} {heading_pattern}.*$", source))
    result: dict[str, str] = {}
    for match in matches:
        next_heading = re.search(r"(?m)^#{2,4} .+$", source[match.end():])
        end = match.end() + next_heading.start() if next_heading else len(source)
        result[match.group(1)] = source[match.start():end]
    return result


def validate_negative_commands(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
) -> None:
    for item_id, section in items.items():
        prompt = section.split("\nA)", 1)[0]
        if re.search(r"\b(?:incorreta|exceto)\b", prompt, re.I) or re.search(
            r"\bNÃO\b",
            prompt,
        ):
            comment = comments.get(item_id, "")
            if not re.search(r"(?m)^\*\*Observação:\*\*", comment):
                errors.append(f"{label} {item_id}: comando negativo sem Observação explícita")


bank_items = exact_sections(bank, r"(S2D[1-6]Q\d{3}|Extra Dia [1-6]\.\d+)\b")
bank_comments = exact_sections(
    bank,
    r"Comentário (S2D[1-6]Q\d{3}|Extra Dia [1-6]\.\d+)\b",
)
super_items = exact_sections(super_text, r"(S2S\d{3})\b")
super_comments = exact_sections(super_text, r"Comentário (S2S\d{3})\b")
validate_negative_commands("banco", bank_items, bank_comments)
validate_negative_commands("super", super_items, super_comments)

for day in range(1, 7):
    very_hard = sum(
        metadata(section, "Nível") == "Muito difícil"
        for item_id, section in bank_items.items()
        if item_id.startswith(f"S2D{day}Q")
    )
    if very_hard == 0:
        errors.append(f"banco: Dia {day} sem principal Muito difícil e sem exceção aceita")


def validate_options(label: str, items: dict[str, str]) -> None:
    for item_id, section in items.items():
        options = re.findall(r"(?m)^([A-D])\)\s+(.+)$", section)
        letters = [letter for letter, _ in options]
        if letters != list("ABCD"):
            errors.append(f"{label} {item_id}: alternativas não formam A-D em ordem")
            continue
        normalized = [" ".join(text.casefold().split()).rstrip(".") for _, text in options]
        if len(set(normalized)) != 4:
            errors.append(f"{label} {item_id}: alternativas duplicadas")


validate_options("banco", bank_items)
validate_options("super", super_items)


def normalized_stem(section: str) -> str | None:
    match = re.search(
        r"(?ms)^(?:- )?\*\*Referência:\*\*[^\r\n]+\r?\n\r?\n(.+?)\r?\n\r?\nA\)\s+",
        section,
    )
    if not match:
        return None
    value = re.sub(r"[`*_~]", "", match.group(1)).casefold()
    return " ".join(value.split())


def validate_unique_stems(
    label: str,
    groups: tuple[dict[str, str], ...],
) -> None:
    seen: dict[str, str] = {}
    for sections in groups:
        for item_id, section in sections.items():
            stem = normalized_stem(section)
            if not stem:
                errors.append(f"{label} {item_id}: enunciado não reconhecido")
                continue
            if stem in seen:
                errors.append(
                    f"{label}: enunciado literal duplicado em {seen[stem]} e {item_id}"
                )
            else:
                seen[stem] = item_id


validate_unique_stems("banco/super", (bank_items, super_items))


def validate_option_lengths(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
) -> None:
    for item_id, section in items.items():
        options = {
            letter: len(re.sub(r"[`*_~]", "", text).strip())
            for letter, text in re.findall(r"(?m)^([A-D])\)\s+(.+)$", section)
        }
        answer = answer_of(comments.get(item_id, ""))
        if answer is None or set(options) != set("ABCD"):
            continue
        correct = options[answer]
        distractors = [length for letter, length in options.items() if letter != answer]
        if correct > 1.30 * max(distractors) or correct < 0.70 * min(distractors):
            comment = comments.get(item_id, "")
            justification = re.search(
                r"(?m)^\*\*Justificativa de comprimento:\*\*\s*(\S.+)$",
                comment,
            )
            if not justification or len(justification.group(1).strip()) < 30:
                errors.append(
                    f"{label} {item_id}: alerta de comprimento sem revisão justificada "
                    f"({answer}={correct}; alternativas={options})"
                )


def validate_comment_letters(label: str, comments: dict[str, str]) -> None:
    for item_id, section in comments.items():
        letters = re.findall(r"(?m)^- \*\*([A-D])\)\*\*", section)
        if letters != list("ABCD"):
            errors.append(f"{label} {item_id}: comentário não analisa A-D em ordem")


validate_comment_letters("banco", bank_comments)
validate_comment_letters("super", super_comments)


def answer_of(section: str) -> str | None:
    match = re.search(r"\*\*Alternativa correta:\s*([A-D])\.\*\*", section)
    return match.group(1) if match else None


def validate_answer_balance(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
) -> None:
    for level in ("Médio", "Difícil", "Muito difícil"):
        counts: Counter[str] = Counter()
        for item_id, section in items.items():
            if metadata(section, "Nível") != level:
                continue
            answer = answer_of(comments.get(item_id, ""))
            if answer:
                counts[answer] += 1
        values = [counts[letter] for letter in "ABCD"]
        if max(values, default=0) - min(values, default=0) > 1:
            errors.append(
                f"{label}: gabarito desequilibrado no nível {level}: "
                + ", ".join(f"{letter}={counts[letter]}" for letter in "ABCD")
            )


validate_option_lengths("banco", bank_items, bank_comments)
validate_option_lengths("super", super_items, super_comments)
validate_answer_balance("banco", bank_items, bank_comments)
validate_answer_balance("super", super_items, super_comments)


for day in range(1, 7):
    day_match = re.search(
        rf"(?ms)^# Dia {day}\b.*?(?=^# Dia {day + 1}\b|\Z)",
        bank,
    )
    if not day_match:
        errors.append(f"banco: Dia {day} ausente")
        continue
    day_text = day_match.group(0)
    key_match = re.search(
        rf"(?ms)^## Gabarito do Dia {day}\s*$.*?(?=^## Comentários do Dia {day}\s*$)",
        day_text,
    )
    if not key_match:
        errors.append(f"banco: gabarito do Dia {day} ausente")
        continue
    rows = re.findall(r"(?m)^\| (\d+(?:\.\d+)?) \| ([A-D]) \|$", key_match.group(0))
    expect(f"linhas do gabarito do Dia {day}", len(rows), 70)
    for local, table_answer in rows:
        if "." in local:
            item_id = f"Extra Dia {local}"
        else:
            item_id = f"S2D{day}Q{(day - 1) * 50 + int(local):03d}"
        comment_answer = answer_of(bank_comments.get(item_id, ""))
        if comment_answer != table_answer:
            errors.append(f"banco {item_id}: tabela e comentário divergem")

    # Os Dias 3 a 5 preservam também uma tabela de respostas imediatamente
    # depois das questões extras. Valide todas as ocorrências para impedir que
    # essa cópia operacional fique obsoleta após uma permutação de gabarito.
    all_rows = re.findall(r"(?m)^\| (\d+(?:\.\d+)?) \| ([A-D]) \|$", day_text)
    expect(
        f"todas as linhas de gabarito do Dia {day}",
        len(all_rows),
        90 if day in (3, 4, 5) else 70,
    )
    occurrences: Counter[str] = Counter()
    for local, table_answer in all_rows:
        if "." in local:
            item_id = f"Extra Dia {local}"
        else:
            item_id = f"S2D{day}Q{(day - 1) * 50 + int(local):03d}"
        occurrences[item_id] += 1
        comment_answer = answer_of(bank_comments.get(item_id, ""))
        if comment_answer != table_answer:
            errors.append(f"banco {item_id}: cópia de tabela e comentário divergem")
    for item_id in [
        *(
            f"S2D{day}Q{number:03d}"
            for number in range((day - 1) * 50 + 1, day * 50 + 1)
        ),
        *(f"Extra Dia {day}.{number}" for number in range(1, 21)),
    ]:
        wanted = 2 if item_id.startswith("Extra") and day in (3, 4, 5) else 1
        if occurrences[item_id] != wanted:
            errors.append(
                f"banco {item_id}: aparece {occurrences[item_id]} vez(es) nas tabelas; "
                f"esperado {wanted}"
            )

super_key = re.search(r"(?ms)^## Gabarito\s*$.*?(?=^## Comentários\s*$)", super_text)
if not super_key:
    errors.append("super: tabela de gabarito ausente")
else:
    rows = re.findall(r"(?m)^\| (\d+) \| ([A-D]) \|$", super_key.group(0))
    expect("linhas do gabarito do super", len(rows), 60)
    numbers = [int(local) for local, _ in rows]
    if numbers != list(range(1, 61)):
        errors.append("super: tabela de gabarito não contém 1–60 exatamente uma vez e em ordem")
    for local, table_answer in rows:
        item_id = f"S2S{int(local):03d}"
        comment_answer = answer_of(super_comments.get(item_id, ""))
        if comment_answer != table_answer:
            errors.append(f"super {item_id}: tabela e comentário divergem")

coverage_match = re.search(
    r"(?ms)^## Cobertura programática auditada\s*$.*?(?=^## Bloco 1\b)",
    super_text,
)
if not coverage_match:
    errors.append("super: tabela de cobertura programática ausente")
else:
    coverage_rows = re.findall(
        r"(?m)^\| ([1-6]) \| [^|]+ \| ((?:S2S\d{3}(?:, )?)+) \|$",
        coverage_match.group(0),
    )
    expect("linhas da cobertura do super", len(coverage_rows), 6)
    covered_ids: list[str] = []
    for day_text, ids_text in coverage_rows:
        ids = re.findall(r"S2S\d{3}", ids_text)
        if len(ids) != 10:
            errors.append(f"super: Dia {day_text} contém {len(ids)} itens na cobertura; esperado 10")
        covered_ids.extend(ids)
    expected_super_ids = [f"S2S{number:03d}" for number in range(1, 61)]
    if sorted(covered_ids) != expected_super_ids:
        errors.append("super: mapa de cobertura não contém S2S001–S2S060 exatamente uma vez")

if "Confunde função, camada, garantia ou limite técnico do caso" in super_text:
    errors.append("super: comentário genérico legado encontrado")

generic_bank_phrases = (
    "Não preserva a regra ou a relação técnica indicada no enunciado.",
    "trocar a função do componente por outra função de protocolo, controle ou mecanismo próximo.",
    "identifique primeiro o objetivo técnico solicitado e descarte opções que mudam camada, finalidade ou garantia.",
)
for phrase in generic_bank_phrases:
    occurrences = bank.count(phrase)
    if occurrences:
        errors.append(f"banco: roteiro genérico proibido encontrado {occurrences} vez(es): {phrase}")

for field in ("Pegadinha", "Como pensar"):
    values = re.findall(rf"^\*\*{re.escape(field)}:\*\*\s*(.+)$", bank, re.M)
    normalized = [" ".join(value.casefold().split()) for value in values]
    expect(f"campos {field} do banco", len(normalized), 420)
    if len(set(normalized)) != 420:
        errors.append(
            f"banco: campo {field} tem {len(set(normalized))} textos distintos em 420 itens"
        )

if "o ponto recuperado deve ser, no máximo, de:" in bank:
    errors.append("banco S2D6Q277: formulação ambígua do RPO reapareceu")

for source_name, heading in (("item", "S2D2Q100"), ("comentário", "Comentário S2D2Q100")):
    reference = re.search(
        rf"(?ms)^### {re.escape(heading)}\b.*?^\*\*Referência:\*\*\s*([^\r\n]+)",
        bank,
    )
    if not reference or "s2-d2-arp" not in reference.group(1):
        errors.append(f"banco S2D2Q100: referência a ARP ausente no {source_name}")

for item_id, fragment in (
    ("S2D3Q150", "s2-d3-proxy"),
    ("S2D6Q300", "s2-d6-recuperacao-dependencias"),
):
    for source_name, heading in (("item", item_id), ("comentário", f"Comentário {item_id}")):
        reference = re.search(
            rf"(?ms)^### {re.escape(heading)}\b.*?^\*\*Referência:\*\*\s*([^\r\n]+)",
            bank,
        )
        if not reference or fragment not in reference.group(1):
            errors.append(f"banco {item_id}: referência {fragment} ausente no {source_name}")

# Regressões do super simulado: a primeira migração usava similaridade lexical
# para escolher referências e repetia o mesmo roteiro em todos os comentários.
# Essas verificações não substituem leitura humana, mas impedem que o defeito
# volte a passar como se fosse uma validação semântica.
generic_phrases = (
    "no caso, a regra decisiva",
    "aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado",
    "isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa",
)
folded_super = " ".join(super_text.casefold().split())
for phrase in generic_phrases:
    if phrase.casefold() in folded_super:
        errors.append(f"super: roteiro genérico proibido encontrado: {phrase}")


def normalized_fields(label: str) -> list[str]:
    values = re.findall(rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$", super_text, re.M)
    return [" ".join(value.casefold().split()) for value in values]


for field in ("Pegadinha", "Como pensar"):
    values = normalized_fields(field)
    expect(f"campos {field} do super", len(values), 60)
    if len(set(values)) != 60:
        errors.append(f"super: campo {field} não foi individualizado nos 60 itens")

question_part, comment_part = super_text.split("## Comentários", 1)


def item_section(source: str, heading: str, next_heading: str) -> str:
    match = re.search(
        rf"(?ms)^### {re.escape(heading)}\b.*?(?=^### (?:{next_heading})\b|\Z)",
        source,
    )
    return match.group(0) if match else ""


# Referências que falharam na auditoria humana de 19/07/2026. O fragmento
# correto deve aparecer tanto no item quanto no respectivo comentário.
semantic_regressions = {
    "007": "s2-d2-gateway",
    "010": "s2-d2-pdus",
    "025": "s2-d4-resposta-incidentes",
    "041": "s2-d4-resposta-incidentes",
    "050": "s2-d1-dominios",
    "053": "s2-d2-gateway",
    "056": "s2-d4-resposta-incidentes",
    "060": "s2-d2-ipv6",
}
for number, fragment in semantic_regressions.items():
    question = item_section(question_part, f"S2S{number}", r"S2S\d{3}")
    comment = item_section(comment_part, f"Comentário S2S{number}", r"Comentário S2S\d{3}")
    if fragment not in question:
        errors.append(f"super S2S{number}: referência semântica ausente no item ({fragment})")
    if fragment not in comment:
        errors.append(f"super S2S{number}: referência semântica ausente no comentário ({fragment})")

if errors:
    print("FALHOU")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

def level_distribution(items: dict[str, str]) -> str:
    counts = Counter(metadata(section, "Nível") for section in items.values())
    return ", ".join(
        f"{level}={counts[level]}" for level in ("Médio", "Difícil", "Muito difícil")
    )


main_items = {item_id: section for item_id, section in bank_items.items() if item_id.startswith("S2D")}
extra_items = {item_id: section for item_id, section in bank_items.items() if item_id.startswith("Extra")}
print("OK: 420 questões + 60 do super simulado; metadados, alternativas, comentários, gabaritos e âncoras validados.")
print(f"Principais: {level_distribution(main_items)}")
print(f"Extras: {level_distribution(extra_items)}")
print(f"Banco: {level_distribution(bank_items)}")
print(f"Super: {level_distribution(super_items)}")
