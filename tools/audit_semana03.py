"""Auditoria estrutural e de consistência do material da Semana 3.

O script não declara correção pedagógica por conta própria. Ele bloqueia erros
mecânicos e deixa uma trilha objetiva para a revisão semântica humana.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Analista de sistemas" / "semana_03"
STUDY_PATH = WEEK / "semana_03_estudo.md"
BANK_PATH = WEEK / "semana_03_questoes.md"
SUPER_PATH = WEEK / "semana_03_super_simulado.md"
JOURNEY_PATH = WEEK / "semana_03_jornada.md"
DISCURSIVE_PATH = WEEK / "semana_03_dissertacoes.md"
README_PATH = WEEK / "README.md"
ACCEPTANCE_PATH = WEEK / "relatorio_aceite.md"
OFFICIAL_PATH = ROOT / "Analista de sistemas" / "questoes_oficiais" / "semana_03.md"
PROJECT_README_PATH = ROOT / "README.md"
ANALYST_README_PATH = ROOT / "Analista de sistemas" / "README.md"
GUIDE_PATH = ROOT / "GUIA_MESTRE_DO_PROJETO.md"
PLAN_PATH = ROOT / "Analista de sistemas" / "planejamento" / "plano_mestre_cra_pr_2026.md"
STANDARD_PATH = ROOT / "Analista de sistemas" / "planejamento" / "padrao_semanal.md"
SEMANTIC_REPORT_PATHS = [
    WEEK / "revisao_semantica_dias_01_02.md",
    WEEK / "revisao_semantica_dias_03_04.md",
    WEEK / "revisao_semantica_dias_05_06.md",
    WEEK / "revisao_semantica_super_simulado.md",
    WEEK / "revisao_semantica_super_simulado_independente.md",
    WEEK / "revisao_pedagogica_teoria_jornada.md",
]

ERRORS: list[str] = []
WARNINGS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def expect(label: str, actual: int, wanted: int) -> None:
    if actual != wanted:
        error(f"{label}: {actual}; esperado {wanted}")


def read(path: Path) -> str:
    if not path.is_file():
        error(f"arquivo ausente: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


study = read(STUDY_PATH)
bank = read(BANK_PATH)
super_text = read(SUPER_PATH)
journey = read(JOURNEY_PATH)
discursive = read(DISCURSIVE_PATH)
readme = read(README_PATH)
acceptance = read(ACCEPTANCE_PATH)
official = read(OFFICIAL_PATH)
project_readme = read(PROJECT_README_PATH)
analyst_readme = read(ANALYST_README_PATH)
guide = read(GUIDE_PATH)
plan = read(PLAN_PATH)
standard = read(STANDARD_PATH)
semantic_reports = {path: read(path) for path in SEMANTIC_REPORT_PATHS}


def validate_local_links(path: Path, source: str) -> None:
    for raw_target in re.findall(r"\[[^\]]*\]\((<[^>]+>|[^)\s]+)", source):
        target = raw_target.strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if "semana_XX" in target or "#sX-" in target:
            continue  # localizador ilustrativo do próprio padrão semanal
        file_part = target.split("#", 1)[0]
        if not file_part:
            continue
        resolved = (path.parent / file_part).resolve()
        if not resolved.exists():
            error(f"link local quebrado em {path.relative_to(ROOT)}: {target}")


for link_path, link_source in (
    (STUDY_PATH, study),
    (BANK_PATH, bank),
    (SUPER_PATH, super_text),
    (JOURNEY_PATH, journey),
    (DISCURSIVE_PATH, discursive),
    (README_PATH, readme),
    (ACCEPTANCE_PATH, acceptance),
    (OFFICIAL_PATH, official),
    (PROJECT_README_PATH, project_readme),
    (ANALYST_README_PATH, analyst_readme),
    (GUIDE_PATH, guide),
    (PLAN_PATH, plan),
    (STANDARD_PATH, standard),
    *semantic_reports.items(),
):
    validate_local_links(link_path, link_source)


def heading_sections(source: str, pattern: str) -> dict[str, str]:
    """Recorta seções identificadas por heading até o próximo heading <= nível."""
    rx = re.compile(rf"(?m)^(?P<marks>#{{1,6}}) {pattern}\s*$")
    result: dict[str, str] = {}
    matches = list(rx.finditer(source))
    all_headings = list(re.finditer(r"(?m)^(#{1,6}) .+$", source))
    for match in matches:
        key = match.group(2)
        end = len(source)
        for candidate in all_headings:
            if candidate.start() <= match.start():
                continue
            end = candidate.start()
            break
        if key in result:
            error(f"seção duplicada: {key}")
        result[key] = source[match.start():end]
    return result


MAIN_ITEMS = heading_sections(bank, r"(S3D[1-6]Q\d{3})\s+(?:—|-)\s+.+")
MAIN_COMMENTS = heading_sections(bank, r"Comentário (S3D[1-6]Q\d{3})")
EXTRA_ITEMS = heading_sections(bank, r"(Extra Dia [1-6]\.\d+)(?:\s+(?:—|-)\s+.+)?")
EXTRA_COMMENTS = heading_sections(bank, r"Comentário (Extra Dia [1-6]\.\d+)")
SUPER_ITEMS = heading_sections(super_text, r"(S3S\d{3})\s+(?:—|-)\s+.+")
SUPER_COMMENTS = heading_sections(super_text, r"Comentário (S3S\d{3})")

expect("questões principais", len(MAIN_ITEMS), 300)
expect("comentários principais", len(MAIN_COMMENTS), 300)
expect("questões extras", len(EXTRA_ITEMS), 120)
expect("comentários extras", len(EXTRA_COMMENTS), 120)
expect("questões do super simulado", len(SUPER_ITEMS), 60)
expect("comentários do super simulado", len(SUPER_COMMENTS), 60)

expected_main = {
    f"S3D{day}Q{number:03d}"
    for day in range(1, 7)
    for number in range((day - 1) * 50 + 1, day * 50 + 1)
}
expected_extras = {f"Extra Dia {day}.{number}" for day in range(1, 7) for number in range(1, 21)}
expected_super = {f"S3S{number:03d}" for number in range(1, 61)}


def compare_sets(label: str, actual: set[str], wanted: set[str]) -> None:
    missing = sorted(wanted - actual)
    unexpected = sorted(actual - wanted)
    if missing:
        error(f"{label}: IDs ausentes: {', '.join(missing[:12])}")
    if unexpected:
        error(f"{label}: IDs inesperados: {', '.join(unexpected[:12])}")


compare_sets("principais", set(MAIN_ITEMS), expected_main)
compare_sets("comentários principais", set(MAIN_COMMENTS), expected_main)
compare_sets("extras", set(EXTRA_ITEMS), expected_extras)
compare_sets("comentários extras", set(EXTRA_COMMENTS), expected_extras)
compare_sets("super", set(SUPER_ITEMS), expected_super)
compare_sets("comentários do super", set(SUPER_COMMENTS), expected_super)


def metadata(section: str, label: str) -> str | None:
    match = re.search(rf"(?m)^(?:- )?\*\*{re.escape(label)}:\*\*\s*([^\r\n]+)", section)
    return match.group(1).strip().rstrip(".") if match else None


def answer(section: str) -> str | None:
    match = re.search(
        r"(?:\*\*Alternativa correta:\*\*\s*([A-D])\.?|\*\*Alternativa correta:\s*([A-D])\.?\*\*)",
        section,
    )
    return next((value for value in match.groups() if value), None) if match else None


def expected_use(item_id: str) -> str:
    if item_id.startswith("Extra"):
        local = int(item_id.rsplit(".", 1)[1])
        limits = ((5, "Essenciais"), (10, "Aprofundamento"), (15, "Revisão"), (20, "Simulado"))
    else:
        absolute = int(item_id[-3:])
        local = (absolute - 1) % 50 + 1
        limits = ((10, "Essenciais"), (30, "Aprofundamento"), (40, "Revisão"), (50, "Simulado"))
    return next(label for limit, label in limits if local <= limit)


def validate_pair(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
    *,
    force_simulado: bool = False,
) -> None:
    for item_id, section in items.items():
        comment = comments.get(item_id, "")
        for field in ("Nível", "Uso", "Referência"):
            left = metadata(section, field)
            right = metadata(comment, field)
            if left is None:
                error(f"{label} {item_id}: {field} ausente no item")
            if right is None:
                error(f"{label} {item_id}: {field} ausente no comentário")
            if left is not None and right is not None and left != right:
                error(f"{label} {item_id}: {field} diverge entre item e comentário")

        level = metadata(section, "Nível")
        if level not in {"Médio", "Difícil", "Muito difícil"}:
            error(f"{label} {item_id}: nível inválido: {level!r}")
        use = metadata(section, "Uso")
        wanted_use = "Simulado" if force_simulado else expected_use(item_id)
        if use != wanted_use:
            error(f"{label} {item_id}: uso {use!r}; esperado {wanted_use!r}")

        options = re.findall(r"(?m)^([A-D])\)\s+(.+)$", section)
        if [letter for letter, _ in options] != list("ABCD"):
            error(f"{label} {item_id}: alternativas não formam A–D em ordem")
        normalized_options = [" ".join(text.casefold().split()).rstrip(".") for _, text in options]
        if len(normalized_options) == 4 and len(set(normalized_options)) != 4:
            error(f"{label} {item_id}: há alternativas literais duplicadas")

        analyses = re.findall(r"(?m)^- \*\*([A-D])\)\*\*", comment)
        if analyses != list("ABCD"):
            error(f"{label} {item_id}: comentário não analisa A–D em ordem")
        correct_answer = answer(comment)
        if correct_answer is None:
            error(f"{label} {item_id}: alternativa correta ausente")
        for field in ("Pegadinha", "Como pensar"):
            value = metadata(comment, field)
            if value is None or len(value) < 10:
                error(f"{label} {item_id}: campo {field} ausente ou superficial")

        stem = section.split("\nA)", 1)[0]
        # Os comandos negativos da coleção são destacados em caixa alta. Manter
        # a busca sensível a maiúsculas evita classificar como comando o uso
        # meramente descritivo de “incorreta” dentro de um enunciado positivo.
        negative_command = bool(
            re.search(r"\b(?:INCORRETA|EXCETO)\b", stem)
            or re.search(r"\bNÃO\b", stem)
        )
        if negative_command:
            observation = metadata(comment, "Observação")
            if observation is None:
                error(f"{label} {item_id}: comando negativo sem Observação")
            else:
                stated = re.search(r"\b([A-D])\s+é o gabarito\b", observation)
                if stated and stated.group(1) != correct_answer:
                    error(f"{label} {item_id}: Observação e alternativa correta divergem")


validate_pair("principal", MAIN_ITEMS, MAIN_COMMENTS)
validate_pair("extra", EXTRA_ITEMS, EXTRA_COMMENTS)
validate_pair("super", SUPER_ITEMS, SUPER_COMMENTS, force_simulado=True)


def validate_option_lengths(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
) -> None:
    for item_id, section in items.items():
        lengths = {
            letter: len(re.sub(r"[`*_~]", "", text).strip())
            for letter, text in re.findall(r"(?m)^([A-D])\)\s+(.+)$", section)
        }
        correct = answer(comments.get(item_id, ""))
        if correct is None or set(lengths) != set("ABCD"):
            continue
        correct_length = lengths[correct]
        distractors = [length for letter, length in lengths.items() if letter != correct]
        if correct_length > 1.30 * max(distractors) or correct_length < 0.70 * min(distractors):
            justification = metadata(comments.get(item_id, ""), "Justificativa de comprimento")
            if justification is None or len(justification) < 30:
                error(
                    f"{label} {item_id}: alerta de comprimento sem revisão justificada "
                    f"({correct}={correct_length}; {lengths})"
                )


validate_option_lengths("principal", MAIN_ITEMS, MAIN_COMMENTS)
validate_option_lengths("extra", EXTRA_ITEMS, EXTRA_COMMENTS)
validate_option_lengths("super", SUPER_ITEMS, SUPER_COMMENTS)

for label, comments in (
    ("banco", {**MAIN_COMMENTS, **EXTRA_COMMENTS}),
    ("super", SUPER_COMMENTS),
):
    for field in ("Pegadinha", "Como pensar"):
        values = [metadata(section, field) for section in comments.values()]
        normalized = [" ".join((value or "").casefold().split()) for value in values]
        if len(set(normalized)) != len(normalized):
            error(f"{label}: campo {field} não foi individualizado em todos os itens")


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    text = re.sub(r"[^a-z0-9 _-]", "", text).strip().replace(" ", "-")
    return re.sub(r"-+", "-", text)


anchors = set(re.findall(r'<a id="([^"]+)"', study))
anchors.update(slug(value) for value in re.findall(r"(?m)^#{1,6}\s+(.+)$", study))
expect("âncoras HTML únicas", len(re.findall(r'<a id="([^"]+)"', study)), len(set(re.findall(r'<a id="([^"]+)"', study))))

for source_name, source in (
    ("banco", bank),
    ("super", super_text),
    ("jornada", journey),
    ("README", readme),
):
    fragments = re.findall(r"semana_03_estudo\.md#([a-zA-Z0-9_.-]+)", source)
    missing = sorted(set(fragments) - anchors)
    if missing:
        error(f"{source_name}: âncoras de estudo ausentes: {', '.join(missing[:15])}")

for label, items, comments in (
    ("principal", MAIN_ITEMS, MAIN_COMMENTS),
    ("extra", EXTRA_ITEMS, EXTRA_COMMENTS),
    ("super", SUPER_ITEMS, SUPER_COMMENTS),
):
    for item_id, section in items.items():
        for side, value in (("item", section), ("comentário", comments.get(item_id, ""))):
            reference = metadata(value, "Referência") or ""
            if "semana_03_estudo.md#" not in reference:
                error(f"{label} {item_id}: referência local ausente no {side}")


def normalized_stem(section: str) -> str:
    before_options = section.split("\nA)", 1)[0]
    lines = [
        line
        for line in before_options.splitlines()
        if not line.startswith(("#", "**Nível:", "**Uso:", "**Referência:", "- **"))
    ]
    value = re.sub(r"[`*_~]", "", " ".join(lines)).casefold()
    return " ".join(value.split())


seen_stems: dict[str, str] = {}
for item_id, section in {**MAIN_ITEMS, **EXTRA_ITEMS, **SUPER_ITEMS}.items():
    stem = normalized_stem(section)
    if not stem:
        error(f"{item_id}: enunciado não reconhecido")
    elif len(stem) >= 60 and stem in seen_stems:
        error(f"enunciado literal duplicado: {seen_stems[stem]} e {item_id}")
    else:
        seen_stems[stem] = item_id


def plain_title(value: str) -> str:
    return " ".join(re.sub(r"[`*_~]", "", value).casefold().split())


# As filas de D0/D+2 são localizadores pedagógicos, não meras listas de IDs.
# O título exibido na teoria deve continuar sendo o título real da questão.
for day in range(1, 7):
    for local in range(1, 11):
        absolute = (day - 1) * 50 + local
        item_id = f"S3D{day}Q{absolute:03d}"
        item_section = MAIN_ITEMS.get(item_id, "")
        heading = re.search(
            rf"(?m)^### {re.escape(item_id)}\s+(?:—|-)\s+(.+)$",
            item_section,
        )
        row = re.search(
            rf"(?m)^\|\s*{local}\s*\|\s*{re.escape(item_id)}\s*\|\s*(.+?)\s+(?:—|-)\s+\[[^]]+\]\([^)]*\)\s*\|",
            study,
        )
        if heading is None:
            error(f"fila Dia {day}: título da questão {item_id} ausente")
        elif row is None:
            error(f"fila Dia {day}: localizador de {item_id} ausente ou sem título real")
        elif plain_title(heading.group(1)) != plain_title(row.group(1)):
            error(
                f"fila Dia {day}: título de {item_id} diverge "
                f"({row.group(1)!r} != {heading.group(1)!r})"
            )


def validate_answer_sequence(label: str, sequence: list[str]) -> None:
    for index in range(len(sequence) - 2):
        if sequence[index] == sequence[index + 1] == sequence[index + 2]:
            error(f"{label}: três gabaritos iguais a partir da posição {index + 1}")
            break

    for width in range(2, 5):
        for start in range(len(sequence) - 3 * width + 1):
            motif = sequence[start : start + width]
            if sequence[start : start + 3 * width] == motif * 3:
                error(
                    f"{label}: motivo curto {''.join(motif)} repetido três vezes "
                    f"a partir da posição {start + 1}"
                )
                return

    counts = Counter(sequence)
    values = [counts[letter] for letter in "ABCD"]
    if sequence and max(values) - min(values) > 3:
        error(f"{label}: gabarito global desequilibrado: {dict(sorted(counts.items()))}")


ordered_bank_answers: list[str] = []
for day in range(1, 7):
    day_ids = [
        *(f"S3D{day}Q{number:03d}" for number in range((day - 1) * 50 + 1, day * 50 + 1)),
        *(f"Extra Dia {day}.{number}" for number in range(1, 21)),
    ]
    day_answers = [
        value
        for item_id in day_ids
        if (value := answer(({**MAIN_COMMENTS, **EXTRA_COMMENTS}).get(item_id, "")))
    ]
    validate_answer_sequence(f"banco Dia {day}", day_answers)
    ordered_bank_answers.extend(day_answers)
validate_answer_sequence("banco completo", ordered_bank_answers)

ordered_super_answers = [
    value
    for number in range(1, 61)
    if (value := answer(SUPER_COMMENTS.get(f"S3S{number:03d}", "")))
]
validate_answer_sequence("super", ordered_super_answers)


def validate_balance_by_level(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
) -> None:
    for level in ("Médio", "Difícil", "Muito difícil"):
        counts: Counter[str] = Counter()
        for item_id, section in items.items():
            if metadata(section, "Nível") != level:
                continue
            value = answer(comments.get(item_id, ""))
            if value:
                counts[value] += 1
        values = [counts[letter] for letter in "ABCD"]
        if max(values, default=0) - min(values, default=0) > 1:
            error(
                f"{label}: gabarito desequilibrado no nível {level}: "
                + ", ".join(f"{letter}={counts[letter]}" for letter in "ABCD")
            )


validate_balance_by_level(
    "banco",
    {**MAIN_ITEMS, **EXTRA_ITEMS},
    {**MAIN_COMMENTS, **EXTRA_COMMENTS},
)
validate_balance_by_level("super", SUPER_ITEMS, SUPER_COMMENTS)


def answer_distribution_by_level(
    items: dict[str, str],
    comments: dict[str, str],
) -> dict[str, dict[str, int]]:
    """Retorna evidência legível do equilíbrio que já é validado acima."""
    result: dict[str, dict[str, int]] = {}
    for level in ("Médio", "Difícil", "Muito difícil"):
        counts: Counter[str] = Counter(
            value
            for item_id, section in items.items()
            if metadata(section, "Nível") == level
            if (value := answer(comments.get(item_id, "")))
        )
        result[level] = {letter: counts[letter] for letter in "ABCD"}
    return result


def raw_length_outlier_count(
    items: dict[str, str],
    comments: dict[str, str],
) -> int:
    """Conta alertas formais, ainda que tenham justificativa editorial."""
    total = 0
    for item_id, section in items.items():
        lengths = {
            letter: len(re.sub(r"[`*_~]", "", option).strip())
            for letter, option in re.findall(r"(?m)^([A-D])\)\s+(.+)$", section)
        }
        correct = answer(comments.get(item_id, ""))
        if correct is None or set(lengths) != set("ABCD"):
            continue
        distractors = [length for letter, length in lengths.items() if letter != correct]
        if lengths[correct] > 1.30 * max(distractors) or lengths[correct] < 0.70 * min(distractors):
            total += 1
    return total


def table_answers(section: str, *, day: int | None = None) -> dict[str, str]:
    lines = section.splitlines()
    result: dict[str, str] = {}
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue

        vertical = re.fullmatch(
            r"\|\s*(S3(?:D[1-6]Q|S)\d{3})\s*\|\s*([A-D])\s*\|",
            stripped,
        )
        if vertical:
            result[vertical.group(1)] = vertical.group(2)
            continue
        if day is not None:
            vertical_extra = re.fullmatch(
                rf"\|\s*({day}\.\d+)\s*\|\s*([A-D])\s*\|",
                stripped,
            )
            if vertical_extra:
                result[f"Extra Dia {vertical_extra.group(1)}"] = vertical_extra.group(2)
                continue
            vertical_local = re.fullmatch(
                r"\|\s*(\d{1,2})\s*\|\s*([A-D])\s*\|",
                stripped,
            )
            if vertical_local:
                local = int(vertical_local.group(1))
                if 1 <= local <= 50:
                    absolute = (day - 1) * 50 + local
                    result[f"S3D{day}Q{absolute:03d}"] = vertical_local.group(2)
                    continue

        ids = re.findall(r"S3(?:D[1-6]Q|S)\d{3}", line)
        if len(ids) >= 2 and index + 2 < len(lines):
            values = re.findall(r"(?<=\|)\s*([A-D])\s*(?=\|)", lines[index + 2])
            if len(values) == len(ids):
                result.update(zip(ids, values, strict=True))
            continue

        if day is not None:
            locals_ = re.findall(rf"(?<=\|)\s*({day}\.\d+)\s*(?=\|)", line)
            if len(locals_) >= 2 and index + 2 < len(lines):
                values = re.findall(r"(?<=\|)\s*([A-D])\s*(?=\|)", lines[index + 2])
                if len(values) == len(locals_):
                    result.update(
                        (f"Extra Dia {local}", value)
                        for local, value in zip(locals_, values, strict=True)
                    )
    return result


for day in range(1, 7):
    day_match = re.search(
        rf"(?ms)^# Dia {day}\b.*?(?=^# Dia {day + 1}\b|\Z)",
        bank,
    )
    if not day_match:
        error(f"banco: seção do Dia {day} ausente")
        continue
    key_match = re.search(
        r"(?ms)^## Gabarito[^\r\n]*\s*$.*?(?=^## Coment)",
        day_match.group(0),
    )
    if not key_match:
        error(f"banco: gabarito do Dia {day} ausente")
        continue
    table = table_answers(key_match.group(0), day=day)
    expect(f"banco: linhas de gabarito do Dia {day}", len(table), 70)
    wanted_ids = {
        *(f"S3D{day}Q{number:03d}" for number in range((day - 1) * 50 + 1, day * 50 + 1)),
        *(f"Extra Dia {day}.{number}" for number in range(1, 21)),
    }
    compare_sets(f"gabarito do Dia {day}", set(table), wanted_ids)
    all_comments = {**MAIN_COMMENTS, **EXTRA_COMMENTS}
    for item_id, table_value in table.items():
        if answer(all_comments.get(item_id, "")) != table_value:
            error(f"banco {item_id}: tabela e comentário divergem")

super_key = re.search(
    r"(?ms)^## Gabarito\s*$.*?(?=^## Coment)",
    super_text,
)
if not super_key:
    error("super: tabela de gabarito ausente")
else:
    table = table_answers(super_key.group(0))
    expect("super: linhas de gabarito", len(table), 60)
    compare_sets("gabarito do super", set(table), expected_super)
    for item_id, table_value in table.items():
        if answer(SUPER_COMMENTS.get(item_id, "")) != table_value:
            error(f"super {item_id}: tabela e comentário divergem")

for day in range(1, 7):
    day_main = {key: value for key, value in MAIN_ITEMS.items() if key.startswith(f"S3D{day}Q")}
    day_extra = {key: value for key, value in EXTRA_ITEMS.items() if key.startswith(f"Extra Dia {day}.")}
    expect(f"Dia {day}: principais", len(day_main), 50)
    expect(f"Dia {day}: extras", len(day_extra), 20)
    uses_main = Counter(metadata(section, "Uso") for section in day_main.values())
    uses_extra = Counter(metadata(section, "Uso") for section in day_extra.values())
    wanted_main = {"Essenciais": 10, "Aprofundamento": 20, "Revisão": 10, "Simulado": 10}
    wanted_extra = {"Essenciais": 5, "Aprofundamento": 5, "Revisão": 5, "Simulado": 5}
    if uses_main != Counter(wanted_main):
        error(f"Dia {day}: usos principais {dict(uses_main)}; esperado {wanted_main}")
    if uses_extra != Counter(wanted_extra):
        error(f"Dia {day}: usos extras {dict(uses_extra)}; esperado {wanted_extra}")
    # A matriz de dificuldade orienta a redação inicial, mas não impõe cota
    # diária. A leitura semântica pode legitimamente deixar um dia sem item
    # "Muito difícil" quando nenhum enunciado exige três filtros reais.

    study_positions = []
    for block in range(1, 7):
        marker = f'<a id="s3-d{day}-b{block}"></a>'
        position = study.find(marker)
        if position < 0:
            error(f"estudo: âncora ausente {marker}")
        study_positions.append(position)
    if study_positions != sorted(study_positions):
        error(f"estudo: Blocos 1–6 fora de ordem no Dia {day}")
    for tail in ("mini-revisao", "checklist", "fila"):
        marker = f'<a id="s3-d{day}-{tail}"></a>'
        position = study.find(marker)
        if position < max(study_positions):
            error(f"estudo: {tail} ausente ou antes do Bloco 6 no Dia {day}")


expect("dias no estudo", len(re.findall(r"(?m)^# Dia [1-6]\b", study)), 6)
expect("dias na jornada", len(re.findall(r"(?m)^## Dia [1-6]\b", journey)), 6)
for date in ("27/07/2026", "28/07/2026", "29/07/2026", "30/07/2026", "31/07/2026", "01/08/2026"):
    if date not in journey:
        error(f"jornada: data ausente {date}")
for term in ("360 minutos", "D+2", "D+7", "D+21", "Semana 2"):
    if term not in journey:
        error(f"jornada: requisito ausente: {term}")
for term in ("questão 35, p. 13", "questão 36, p. 14", "questão 32, p. 12", "substitui"):
    if term not in journey:
        error(f"jornada: calibração oficial ausente: {term}")

discursive_anchors = set(re.findall(r'<a id="([^"]+)"', discursive))
for day in range(1, 7):
    if f"s3-disc-d{day}" not in discursive_anchors:
        error(f"discursiva: âncora s3-disc-d{day} ausente")
for term in ("20 pontos", "20 a 30 linhas", "12 pontos", "4 horas", "Folha de Texto Definitivo"):
    if term not in discursive:
        error(f"discursiva: requisito ausente: {term}")

coverage = re.search(r"(?ms)^## Cobertura programática auditada\s*$.*?(?=^## )", super_text)
if coverage is None:
    error("super: seção de cobertura programática auditada ausente")
else:
    final_super_counts = Counter(metadata(section, "Nível") for section in SUPER_ITEMS.values())
    for fragment in (
        f"{final_super_counts['Médio']} médias",
        f"{final_super_counts['Difícil']} difíceis",
        f"{final_super_counts['Muito difícil']} muito difíceis",
    ):
        if fragment not in coverage.group(0):
            error(f"super: cabeçalho não registra a distribuição final: {fragment}")
    all_covered: list[str] = []
    for day in range(1, 7):
        row = re.search(rf"(?m)^\|\s*{day}\s*\|[^\n]+$", coverage.group(0))
        if not row:
            error(f"super: linha de cobertura do Dia {day} ausente")
            continue
        row_text = row.group(0)
        ranges = re.findall(r"S3S(\d{3})\s*[–-]\s*S3S(\d{3})", row_text)
        if ranges:
            ids = [
                f"S3S{number:03d}"
                for start, end in ranges
                for number in range(int(start), int(end) + 1)
            ]
        else:
            ids = re.findall(r"S3S\d{3}", row_text)
        expect(f"super: cobertura do Dia {day}", len(ids), 10)
        all_covered.extend(ids)
    if Counter(all_covered) != Counter(expected_super):
        error("super: cobertura não contém S3S001–S3S060 exatamente uma vez")

for source_name, source in (("estudo", study), ("banco", bank), ("super", super_text), ("jornada", journey), ("discursiva", discursive)):
    for token in ("TODO", "TBD", "PREENCHER", "PLACEHOLDER", "Lorem ipsum"):
        if re.search(rf"\b{re.escape(token)}\b", source):
            error(f"{source_name}: marcador provisório encontrado: {token}")
    if re.search(r"(?m)^E\)\s+", source):
        error(f"{source_name}: alternativa E encontrada")

if "32 / p. 12" not in official or "35 / p. 13" not in official or "36 / p. 14" not in official:
    error("índice oficial: paginação conferida do caderno Tipo 4 não está registrada corretamente")
for term in ("gabarito oficial pós-recursos", "anulada após recurso", "gabarito alterado após recurso"):
    if term not in official:
        error(f"índice oficial: requisito ausente: {term}")

for source_name, source in (
    ("README da semana", readme),
    ("apostila", study),
    ("banco", bank),
    ("jornada", journey),
    ("discursiva", discursive),
):
    if "Material aprovado para execução" not in source:
        error(f"{source_name}: status final de material aprovado ausente")
    if "Em produção" in source:
        error(f"{source_name}: status provisório ainda presente")

for term in ("98/100", "sem falha eliminatória", "Execução pelo candidato", "Pendente"):
    if term not in acceptance:
        error(f"relatório de aceite: evidência final ausente: {term}")

approved_week3_rows = re.findall(
    r"(?m)^\| Semana 3 \| Dia [1-6] \|.*\| Material aprovado para execução \|",
    plan,
)
expect("Plano Mestre: dias da Semana 3 aprovados", len(approved_week3_rows), 6)
for term in (
    "Banco de dados avançado: administração de dados",
    "Coberto e auditado na Semana 3",
    "SQL avançado e SGBD",
    "Uma semana só deve ser considerada **material aprovado para execução** quando",
    "O status **Concluído** exige",
):
    if term not in plan:
        error(f"Plano Mestre: fechamento de cobertura ausente: {term}")

report_requirements = {
    "revisao_semantica_dias_01_02.md": "Fechamento dos achados",
    "revisao_semantica_dias_03_04.md": "Fechamento dos achados",
    "revisao_semantica_dias_05_06.md": "Fechamento dos achados",
    "revisao_semantica_super_simulado.md": "Parecer final",
    "revisao_semantica_super_simulado_independente.md": "Fechamento dos achados",
    "revisao_pedagogica_teoria_jornada.md": "Fechamento dos bloqueios de integração",
}
for path, source in semantic_reports.items():
    required = report_requirements[path.name]
    if required not in source:
        error(f"{path.name}: seção de fechamento ausente: {required}")

if ERRORS:
    print("FALHOU")
    for message in ERRORS:
        print(f"- {message}")
    if WARNINGS:
        print("AVISOS")
        for message in WARNINGS:
            print(f"- {message}")
    sys.exit(1)

main_levels = Counter(metadata(section, "Nível") for section in MAIN_ITEMS.values())
extra_levels = Counter(metadata(section, "Nível") for section in EXTRA_ITEMS.values())
super_levels = Counter(metadata(section, "Nível") for section in SUPER_ITEMS.values())
bank_items = {**MAIN_ITEMS, **EXTRA_ITEMS}
bank_comments = {**MAIN_COMMENTS, **EXTRA_COMMENTS}
print("OK: estrutura integral da Semana 3 validada.")
print(f"Banco: 300 principais + 120 extras; níveis principais={dict(main_levels)}; extras={dict(extra_levels)}")
print(f"Super simulado: 60 itens; níveis={dict(super_levels)}")
print(
    "Equilíbrio A-D por nível: "
    f"banco={answer_distribution_by_level(bank_items, bank_comments)}; "
    f"super={answer_distribution_by_level(SUPER_ITEMS, SUPER_COMMENTS)}"
)
print(
    "Alertas formais brutos de comprimento: "
    f"banco={raw_length_outlier_count(bank_items, bank_comments)}; "
    f"super={raw_length_outlier_count(SUPER_ITEMS, SUPER_COMMENTS)}"
)
