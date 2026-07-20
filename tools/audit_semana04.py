"""Auditoria mecânica e de rastreabilidade do material da Semana 4.

O script não substitui leitura semântica. Ele bloqueia falhas estruturais,
divergências entre item e comentário, referências quebradas e padrões de
gabarito que poderiam viciar o treino.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Analista de sistemas" / "semana_04"
STUDY = WEEK / "semana_04_estudo.md"
BANK = WEEK / "semana_04_questoes.md"
SUPER = WEEK / "semana_04_super_simulado.md"
JOURNEY = WEEK / "semana_04_jornada.md"
DISCURSIVE = WEEK / "semana_04_dissertacoes.md"
README = WEEK / "README.md"
ACCEPTANCE = WEEK / "relatorio_aceite.md"
OFFICIAL = ROOT / "Analista de sistemas" / "questoes_oficiais" / "semana_04.md"
SEMANTIC_REPORTS = [
    WEEK / "revisao_semantica_dia_01.md",
    WEEK / "revisao_semantica_dia_02.md",
    WEEK / "revisao_semantica_dias_01_02.md",
    WEEK / "revisao_semantica_dias_03_04.md",
    WEEK / "revisao_semantica_dia_05.md",
    WEEK / "revisao_semantica_dia_06.md",
    WEEK / "revisao_semantica_dias_05_06.md",
    WEEK / "revisao_semantica_super_simulado.md",
    WEEK / "revisao_semantica_super_simulado_independente.md",
    WEEK / "revisao_operacional_jornada_dissertacao.md",
    WEEK / "revisao_pedagogica_teoria_jornada.md",
]

ERRORS: list[str] = []
WARNINGS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def warn(message: str) -> None:
    WARNINGS.append(message)


def read(path: Path, *, required: bool = True) -> str:
    if not path.is_file():
        if required:
            error(f"arquivo ausente: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


study = read(STUDY)
bank = read(BANK)
super_text = read(SUPER)
journey = read(JOURNEY)
discursive = read(DISCURSIVE)
readme = read(README)
acceptance = read(ACCEPTANCE)
official = read(OFFICIAL)
semantic_reports = {path: read(path) for path in SEMANTIC_REPORTS}


def expect(label: str, actual: int, expected: int) -> None:
    if actual != expected:
        error(f"{label}: {actual}; esperado {expected}")


def validate_local_links(path: Path, source: str) -> None:
    for raw in re.findall(r"\[[^\]]*\]\((<[^>]+>|[^)\s]+)", source):
        target = raw.strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        file_part = target.split("#", 1)[0]
        if file_part and not (path.parent / file_part).resolve().exists():
            error(f"link local quebrado em {path.relative_to(ROOT)}: {target}")


for path, source in (
    (STUDY, study),
    (BANK, bank),
    (SUPER, super_text),
    (JOURNEY, journey),
    (DISCURSIVE, discursive),
    (README, readme),
    (ACCEPTANCE, acceptance),
    (OFFICIAL, official),
    *semantic_reports.items(),
):
    validate_local_links(path, source)


def heading_sections(source: str, pattern: str) -> dict[str, str]:
    rx = re.compile(rf"(?m)^(?P<marks>#{{1,6}}) {pattern}\s*$")
    matches = list(rx.finditer(source))
    headings = list(re.finditer(r"(?m)^(#{1,6}) .+$", source))
    result: dict[str, str] = {}
    for match in matches:
        end = len(source)
        for heading in headings:
            if heading.start() <= match.start():
                continue
            end = heading.start()
            break
        key = next(value for value in match.groups()[1:] if value is not None)
        if key in result:
            error(f"seção duplicada: {key}")
        result[key] = source[match.start():end]
    return result


MAIN_ITEMS = heading_sections(bank, r"(S4D[1-6]Q\d{3})\s+(?:—|-)\s+.+")
MAIN_COMMENTS = heading_sections(bank, r"Comentário (S4D[1-6]Q\d{3})")
EXTRA_ITEMS = heading_sections(bank, r"(Extra Dia [1-6]\.\d+)(?:\s+(?:—|-)\s+.+)?")
EXTRA_COMMENTS = heading_sections(bank, r"Comentário (Extra Dia [1-6]\.\d+)")
SUPER_ITEMS = heading_sections(super_text, r"(S4S\d{3})\s+(?:—|-)\s+.+")
SUPER_COMMENTS = heading_sections(super_text, r"Comentário (S4S\d{3})")

expect("questões principais", len(MAIN_ITEMS), 300)
expect("comentários principais", len(MAIN_COMMENTS), 300)
expect("questões extras", len(EXTRA_ITEMS), 120)
expect("comentários extras", len(EXTRA_COMMENTS), 120)
expect("questões do super", len(SUPER_ITEMS), 60)
expect("comentários do super", len(SUPER_COMMENTS), 60)

EXPECTED_MAIN = {
    f"S4D{day}Q{number:03d}"
    for day in range(1, 7)
    for number in range((day - 1) * 50 + 1, day * 50 + 1)
}
EXPECTED_EXTRA = {f"Extra Dia {day}.{number}" for day in range(1, 7) for number in range(1, 21)}
EXPECTED_SUPER = {f"S4S{number:03d}" for number in range(1, 61)}


def compare_ids(label: str, actual: set[str], expected: set[str]) -> None:
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing:
        error(f"{label}: ausentes {', '.join(missing[:12])}")
    if unexpected:
        error(f"{label}: inesperados {', '.join(unexpected[:12])}")


compare_ids("principais", set(MAIN_ITEMS), EXPECTED_MAIN)
compare_ids("comentários principais", set(MAIN_COMMENTS), EXPECTED_MAIN)
compare_ids("extras", set(EXTRA_ITEMS), EXPECTED_EXTRA)
compare_ids("comentários extras", set(EXTRA_COMMENTS), EXPECTED_EXTRA)
compare_ids("super", set(SUPER_ITEMS), EXPECTED_SUPER)
compare_ids("comentários do super", set(SUPER_COMMENTS), EXPECTED_SUPER)


def metadata(section: str, label: str) -> str | None:
    match = re.search(rf"(?m)^(?:- )?\*\*{re.escape(label)}:\*\*\s*([^\r\n]+)", section)
    if not match:
        match = re.search(rf"(?m)^(?:- )?\*\*{re.escape(label)}:\s*([^*\r\n]+)\*\*", section)
    return match.group(1).strip().rstrip(".") if match else None


def answer(section: str) -> str | None:
    match = re.search(
        r"\*\*(?:Alternativa correta|Gabarito):\*\*\s*([A-D])\.?"
        r"|\*\*(?:Alternativa correta|Gabarito):\s*([A-D])(?:\b|\.)[^*]*\*\*",
        section,
    )
    return next((value for value in match.groups() if value), None) if match else None


def expected_use(item_id: str) -> str:
    if item_id.startswith("Extra"):
        local = int(item_id.rsplit(".", 1)[1])
        limits = ((5, "Essenciais"), (10, "Aprofundamento"), (15, "Revisão"), (20, "Simulado"))
    else:
        local = (int(item_id[-3:]) - 1) % 50 + 1
        limits = ((10, "Essenciais"), (30, "Aprofundamento"), (40, "Revisão"), (50, "Simulado"))
    return next(value for limit, value in limits if local <= limit)


def validate_pair(
    label: str,
    items: dict[str, str],
    comments: dict[str, str],
    *,
    extra: bool = False,
    force_simulado: bool = False,
) -> None:
    common_fields = ("Nível", "Uso", "Referência")
    extra_fields = ("Dia", "Bloco", "Matéria", "Assunto") if extra else ()
    for item_id, section in items.items():
        comment = comments.get(item_id, "")
        for field in (*extra_fields, *common_fields):
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
            error(f"{label} {item_id}: nível inválido {level!r}")
        wanted_use = "Simulado" if force_simulado else expected_use(item_id)
        if metadata(section, "Uso") != wanted_use:
            error(f"{label} {item_id}: uso deveria ser {wanted_use}")

        options = re.findall(r"(?m)^([A-D])\)\s+(.+)$", section)
        if [letter for letter, _ in options] != list("ABCD"):
            error(f"{label} {item_id}: alternativas não formam A–D")
        normalized = [" ".join(text.casefold().split()).rstrip(".") for _, text in options]
        if len(normalized) == 4 and len(set(normalized)) != 4:
            error(f"{label} {item_id}: alternativa literal duplicada")

        analyses = re.findall(r"(?m)^- \*\*([A-D])\)\*\*", comment)
        if analyses != list("ABCD"):
            error(f"{label} {item_id}: comentário não analisa A–D em ordem")
        correct = answer(comment)
        if correct is None:
            error(f"{label} {item_id}: alternativa correta ausente")
        for field in ("Conceito", "Pegadinha", "Como pensar"):
            value = metadata(comment, field)
            if value is None or len(value) < 10:
                error(f"{label} {item_id}: {field} ausente ou superficial")

        stem = section.split("\nA)", 1)[0]
        if re.search(r"\b(?:INCORRETA|EXCETO|NÃO)\b", stem) and metadata(comment, "Observação") is None:
            error(f"{label} {item_id}: comando negativo sem Observação")


validate_pair("principal", MAIN_ITEMS, MAIN_COMMENTS)
validate_pair("extra", EXTRA_ITEMS, EXTRA_COMMENTS, extra=True)
validate_pair("super", SUPER_ITEMS, SUPER_COMMENTS, force_simulado=True)

for label, source in (("banco", bank), ("super", super_text)):
    if re.search(r"(?m)^(?:E\)|- \*\*E\)\*\*)", source):
        error(f"{label}: alternativa ou análise E encontrada")


def slug(text: str) -> str:
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"[^a-z0-9 _-]", "", value).strip().replace(" ", "-")
    return re.sub(r"-+", "-", value)


html_anchors = re.findall(r'<a id="([^"]+)"', study)
expect("âncoras HTML únicas", len(html_anchors), len(set(html_anchors)))
anchors = set(html_anchors)
anchors.update(slug(title) for title in re.findall(r"(?m)^#{1,6}\s+(.+)$", study))
for source_name, source in (("banco", bank), ("super", super_text), ("jornada", journey)):
    fragments = re.findall(r"semana_04_estudo\.md#([a-zA-Z0-9_.-]+)", source)
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
            if "semana_04_estudo.md#" not in reference:
                error(f"{label} {item_id}: referência local ausente no {side}")


def normalized_stem(section: str) -> str:
    lines = [
        line
        for line in section.split("\nA)", 1)[0].splitlines()
        if not line.startswith(("#", "**Nível:", "**Uso:", "**Referência:", "**Dia:", "**Bloco:", "**Matéria:", "**Assunto:"))
    ]
    return " ".join(re.sub(r"[`*_~]", "", " ".join(lines)).casefold().split())


seen: dict[str, str] = {}
for item_id, section in {**MAIN_ITEMS, **EXTRA_ITEMS, **SUPER_ITEMS}.items():
    stem = normalized_stem(section)
    if not stem:
        error(f"{item_id}: enunciado não reconhecido")
    elif len(stem) >= 60 and stem in seen:
        error(f"enunciado literal duplicado: {seen[stem]} e {item_id}")
    else:
        seen[stem] = item_id


def forbidden_pattern(label: str, sequence: list[str]) -> None:
    for index in range(len(sequence) - 2):
        if len(set(sequence[index:index + 3])) == 1:
            error(f"{label}: três gabaritos iguais a partir da posição {index + 1}")
            break
    for width in range(2, 5):
        for start in range(len(sequence) - 3 * width + 1):
            motif = sequence[start:start + width]
            if sequence[start:start + 3 * width] == motif * 3:
                error(f"{label}: motivo {''.join(motif)} repetido três vezes")
                return


bank_items = {**MAIN_ITEMS, **EXTRA_ITEMS}
bank_comments = {**MAIN_COMMENTS, **EXTRA_COMMENTS}
ordered_bank: list[str] = []
for day in range(1, 7):
    ids = [
        *(f"S4D{day}Q{number:03d}" for number in range((day - 1) * 50 + 1, day * 50 + 1)),
        *(f"Extra Dia {day}.{number}" for number in range(1, 21)),
    ]
    values = [value for item_id in ids if (value := answer(bank_comments.get(item_id, "")))]
    forbidden_pattern(f"banco Dia {day}", values)
    counts = Counter(values)
    if values and max(counts[letter] for letter in "ABCD") - min(counts[letter] for letter in "ABCD") > 3:
        error(f"banco Dia {day}: gabarito desequilibrado {dict(counts)}")
    ordered_bank.extend(values)
forbidden_pattern("banco completo", ordered_bank)

ordered_super = [
    value
    for number in range(1, 61)
    if (value := answer(SUPER_COMMENTS.get(f"S4S{number:03d}", "")))
]
forbidden_pattern("super", ordered_super)


def balance_by_level(label: str, items: dict[str, str], comments: dict[str, str]) -> None:
    for level in ("Médio", "Difícil", "Muito difícil"):
        counts = Counter(
            value
            for item_id, section in items.items()
            if metadata(section, "Nível") == level
            if (value := answer(comments.get(item_id, "")))
        )
        values = [counts[letter] for letter in "ABCD"]
        if values and max(values) - min(values) > 1:
            error(f"{label}: respostas desequilibradas em {level}: {dict(counts)}")


balance_by_level("banco", bank_items, bank_comments)
balance_by_level("super", SUPER_ITEMS, SUPER_COMMENTS)


def length_alerts(items: dict[str, str], comments: dict[str, str]) -> list[str]:
    alerts: list[str] = []
    for item_id, section in items.items():
        options = {
            letter: len(re.findall(r"\w+", text, flags=re.UNICODE))
            for letter, text in re.findall(r"(?m)^([A-D])\)\s+(.+)$", section)
        }
        correct = answer(comments.get(item_id, ""))
        if correct is None or len(options) != 4:
            continue
        other_lengths = [value for letter, value in options.items() if letter != correct]
        average = sum(other_lengths) / len(other_lengths)
        if options[correct] >= max(other_lengths) + 3 and options[correct] > 1.30 * average:
            alerts.append(item_id)
    return alerts


BANK_LENGTH_ALERTS = length_alerts(bank_items, bank_comments)
SUPER_LENGTH_ALERTS = length_alerts(SUPER_ITEMS, SUPER_COMMENTS)

for day in range(1, 7):
    expect(
        f"principais do Dia {day}",
        sum(item_id.startswith(f"S4D{day}") for item_id in MAIN_ITEMS),
        50,
    )
    expect(
        f"extras do Dia {day}",
        sum(item_id.startswith(f"Extra Dia {day}.") for item_id in EXTRA_ITEMS),
        20,
    )
    start = (day - 1) * 10 + 1
    expect(
        f"super do Dia-base {day}",
        sum(f"S4S{number:03d}" in SUPER_ITEMS for number in range(start, start + 10)),
        10,
    )

for label, source in (
    ("apostila", study),
    ("banco", bank),
    ("jornada", journey),
    ("discursiva", discursive),
    ("super", super_text),
    ("README", readme),
):
    if re.search(r"(?im)^\s*(?:-\s*)?\*\*Status:\*\*\s*\*\*?conclu[ií]d[oa]", source):
        error(f"{label}: status presume execução concluída")

if "20 a 30 linhas" not in discursive or "12 pontos" not in discursive:
    error("discursiva: limites ou nota mínima do edital não reconhecidos")
if "360 minutos" not in journey or "170 minutos" not in journey or "20 minutos" not in journey:
    error("jornada: estrutura 170 + 170 + 20 não reconhecida")
if "gabarito pós-recursos" not in official.casefold():
    error("índice oficial: gabarito pós-recursos não identificado")


def level_counts(items: dict[str, str]) -> dict[str, int]:
    return dict(Counter(metadata(section, "Nível") or "ausente" for section in items.values()))


if WARNINGS:
    print("AVISOS")
    for message in WARNINGS:
        print(f"- {message}")

if ERRORS:
    print("FALHAS")
    for message in ERRORS:
        print(f"- {message}")
    raise SystemExit(1)

print("AUDITORIA MECÂNICA APROVADA")
print(f"Banco: 300 principais + 120 extras; níveis={level_counts(bank_items)}")
print(f"Super: 60 itens; níveis={level_counts(SUPER_ITEMS)}")
print("IDs, metadados, comentários A–D, referências, links, anti-padrão e carga conferidos.")
print(
    "Alertas formais brutos de comprimento: "
    f"banco={len(BANK_LENGTH_ALERTS)}; super={len(SUPER_LENGTH_ALERTS)}."
)
