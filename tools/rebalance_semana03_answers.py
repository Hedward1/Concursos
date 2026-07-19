"""Permuta alternativas da Semana 3 sem alterar o conteúdo semântico.

O alvo é equilibrado dentro de cada nível e rejeita trincas e motivos curtos.
Questão, comentário A–D e tabela de gabarito são atualizados juntos. Execute
somente depois de todos os lotes de questões estarem fechados.
"""

from __future__ import annotations

import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Analista de sistemas" / "semana_03"
BANK_PARTS = [
    WEEK / "partes" / "questoes_dias_01_02.md",
    WEEK / "partes" / "questoes_dias_03_04.md",
    WEEK / "partes" / "questoes_dias_05_06.md",
]
SUPER_PATH = WEEK / "semana_03_super_simulado.md"


@dataclass(frozen=True)
class Item:
    item_id: str
    level: str
    answer: str
    path: Path
    order: int


def section_spans(source: str, pattern: str) -> dict[str, tuple[int, int]]:
    rx = re.compile(rf"(?m)^(?P<marks>#{{1,6}}) {pattern}\s*$")
    matches = list(rx.finditer(source))
    headings = list(re.finditer(r"(?m)^(#{1,6}) .+$", source))
    result: dict[str, tuple[int, int]] = {}
    for match in matches:
        end = len(source)
        for heading in headings:
            if heading.start() <= match.start():
                continue
            end = heading.start()
            break
        result[match.group(2)] = (match.start(), end)
    return result


def metadata(section: str, label: str) -> str:
    match = re.search(rf"(?m)^(?:- )?\*\*{re.escape(label)}:\*\*\s*([^\r\n]+)", section)
    if not match:
        raise ValueError(f"campo {label} ausente")
    return match.group(1).strip().rstrip(".")


def answer_match(section: str) -> re.Match[str]:
    match = re.search(
        r"(?m)^\*\*Alternativa correta:\*\*\s*([A-D])\.?\s*$|^\*\*Alternativa correta:\s*([A-D])\.?\*\*\s*$",
        section,
    )
    if not match:
        raise ValueError("campo Alternativa correta ausente")
    return match


def answer_value(match: re.Match[str]) -> str:
    return next(value for value in match.groups() if value)


def load_items(paths: list[Path], super_mode: bool = False) -> tuple[list[Item], dict[Path, str]]:
    sources = {path: path.read_text(encoding="utf-8") for path in paths}
    items: list[Item] = []
    order = 0
    if super_mode:
        item_pattern = r"(S3S\d{3})\s+(?:—|-)\s+.+"
    else:
        item_pattern = r"(S3D[1-6]Q\d{3})\s+(?:—|-)\s+.+|((?:Extra Dia [1-6]\.\d+))(?:\s+(?:—|-)\s+.+)?"
    for path, source in sources.items():
        spans = section_spans(source, item_pattern) if super_mode else {}
        if super_mode:
            comment_spans = section_spans(source, r"Comentário (S3S\d{3})")
        else:
            comment_spans = {
                **section_spans(source, r"Comentário (S3D[1-6]Q\d{3})"),
                **section_spans(source, r"Comentário (Extra Dia [1-6]\.\d+)"),
            }
        # A expressão possui dois grupos no modo banco; normalize a chave vazia.
        if not super_mode:
            fixed: dict[str, tuple[int, int]] = {}
            rx = re.compile(r"(?m)^(#{1,6}) ((S3D[1-6]Q\d{3})|((?:Extra Dia [1-6]\.\d+)))(?:\s+(?:—|-)\s+.+)?\s*$")
            headings = list(re.finditer(r"(?m)^(#{1,6}) .+$", source))
            for match in rx.finditer(source):
                end = len(source)
                for heading in headings:
                    if heading.start() <= match.start():
                        continue
                    end = heading.start()
                    break
                fixed[match.group(3) or match.group(4)] = (match.start(), end)
            spans = fixed
        for item_id, (start, end) in spans.items():
            level = metadata(source[start:end], "Nível")
            if item_id not in comment_spans:
                raise ValueError(f"{item_id}: comentário ausente")
            comment_start, comment_end = comment_spans[item_id]
            current = answer_value(answer_match(source[comment_start:comment_end]))
            items.append(Item(item_id, level, current, path, order))
            order += 1
    return items, sources


def has_forbidden_pattern(sequence: list[str]) -> bool:
    if any(sequence[index] == sequence[index + 1] == sequence[index + 2] for index in range(len(sequence) - 2)):
        return True
    for width in range(2, 5):
        for start in range(len(sequence) - 3 * width + 1):
            motif = sequence[start : start + width]
            if sequence[start : start + 3 * width] == motif * 3:
                return True
    return False


def target_answers(items: list[Item], base_seed: int) -> dict[str, str]:
    ordered = sorted(items, key=lambda value: value.order)
    levels: dict[str, list[Item]] = defaultdict(list)
    for item in ordered:
        levels[item.level].append(item)

    level_names = ("Médio", "Difícil", "Muito difícil")
    quota_options: list[list[Counter[str]]] = []
    for level in level_names:
        size = len(levels.get(level, []))
        base = Counter({letter: size // 4 for letter in "ABCD"})
        options: list[Counter[str]] = []
        for remainder_letters in combinations("ABCD", size % 4):
            counts = base.copy()
            for letter in remainder_letters:
                counts[letter] += 1
            options.append(counts)
        quota_options.append(options)

    current_global = Counter(item.answer for item in ordered)

    def quota_score(choice: tuple[Counter[str], ...]) -> tuple[int, int, tuple[tuple[int, ...], ...]]:
        aggregate = Counter(
            {
                letter: sum(counts[letter] for counts in choice)
                for letter in "ABCD"
            }
        )
        distance = sum(abs(aggregate[letter] - current_global[letter]) for letter in "ABCD")
        spread = max(aggregate.values(), default=0) - min(aggregate.values(), default=0)
        signature = tuple(tuple(counts[letter] for letter in "ABCD") for counts in choice)
        return distance, spread, signature

    chosen_quotas = min(product(*quota_options), key=quota_score)
    desired = dict(zip(level_names, chosen_quotas, strict=True))

    item_days: dict[str, int] = {}
    for item in ordered:
        match = re.match(r"S3D([1-6])Q|Extra Dia ([1-6])\.", item.item_id)
        if match:
            item_days[item.item_id] = int(match.group(1) or match.group(2))

    def local_pattern(sequence: list[str], position: int) -> bool:
        for start in range(max(0, position - 2), min(position, len(sequence) - 3) + 1):
            if sequence[start] == sequence[start + 1] == sequence[start + 2]:
                return True
        for width in range(2, 5):
            span = 3 * width
            low = max(0, position - span + 1)
            high = min(position, len(sequence) - span)
            for start in range(low, high + 1):
                motif = sequence[start : start + width]
                if sequence[start : start + span] == motif * 3:
                    return True
        return False

    # Começar pelo gabarito já auditado conserva a naturalidade por dia. Cada
    # tentativa faz apenas as trocas necessárias para corrigir o equilíbrio
    # dentro dos níveis recalibrados.
    for attempt in range(2_000):
        rng = random.Random(base_seed + attempt)
        sequence = [item.answer for item in ordered]
        targets = {item.item_id: item.answer for item in ordered}
        level_counts: dict[str, Counter[str]] = {
            level: Counter(targets[item.item_id] for item in group)
            for level, group in levels.items()
        }
        global_counts = Counter(sequence)
        day_counts: dict[int, Counter[str]] = defaultdict(Counter)
        for item in ordered:
            if item.item_id in item_days:
                day_counts[item_days[item.item_id]][targets[item.item_id]] += 1

        remaining = sum(
            abs(level_counts[level][letter] - desired[level][letter])
            for level in desired
            for letter in "ABCD"
        )
        steps = 0
        while remaining and steps < 2_000:
            steps += 1
            candidates: list[tuple[int, str]] = []
            indices = list(range(len(ordered)))
            rng.shuffle(indices)
            for index in indices:
                item = ordered[index]
                current = targets[item.item_id]
                counts = level_counts[item.level]
                if counts[current] <= desired[item.level][current]:
                    continue
                wanted = [
                    letter
                    for letter in "ABCD"
                    if counts[letter] < desired[item.level][letter]
                ]
                rng.shuffle(wanted)
                for target in wanted:
                    global_counts[current] -= 1
                    global_counts[target] += 1
                    day = item_days.get(item.item_id)
                    if day is not None:
                        day_counts[day][current] -= 1
                        day_counts[day][target] += 1
                    sequence[index] = target

                    global_ok = max(global_counts[letter] for letter in "ABCD") - min(
                        global_counts[letter] for letter in "ABCD"
                    ) <= 3
                    day_ok = day is None or (
                        max(day_counts[day][letter] for letter in "ABCD")
                        - min(day_counts[day][letter] for letter in "ABCD")
                        <= 3
                    )
                    pattern_ok = not local_pattern(sequence, index)

                    sequence[index] = current
                    if day is not None:
                        day_counts[day][target] -= 1
                        day_counts[day][current] += 1
                    global_counts[target] -= 1
                    global_counts[current] += 1
                    if global_ok and day_ok and pattern_ok:
                        candidates.append((index, target))
                        if len(candidates) >= 80:
                            break
                if len(candidates) >= 80:
                    break

            if not candidates:
                break
            index, target = rng.choice(candidates)
            item = ordered[index]
            current = targets[item.item_id]
            targets[item.item_id] = target
            sequence[index] = target
            level_counts[item.level][current] -= 1
            level_counts[item.level][target] += 1
            global_counts[current] -= 1
            global_counts[target] += 1
            day = item_days.get(item.item_id)
            if day is not None:
                day_counts[day][current] -= 1
                day_counts[day][target] += 1
            remaining -= 2

        if remaining == 0 and not has_forbidden_pattern(sequence):
            return targets

    raise RuntimeError("não foi possível equilibrar o gabarito preservando os recortes diários")


def replace_section(
    section: str,
    item_id: str,
    target: str,
    *,
    comment: bool,
) -> str:
    if comment:
        current_match = answer_match(section)
        current = answer_value(current_match)
        line_rx = re.compile(r"(?m)^- \*\*([A-D])\)\*\*\s*(.+)$")
    else:
        current = ""
        line_rx = re.compile(r"(?m)^([A-D])\)\s+(.+)$")

    lines = list(line_rx.finditer(section))
    if len(lines) != 4 or [match.group(1) for match in lines] != list("ABCD"):
        raise ValueError(f"{item_id}: linhas A–D não reconhecidas no {'comentário' if comment else 'item'}")
    if not comment:
        return section  # a permutação depende da resposta, conhecida no comentário

    # Troca mínima: a alternativa correta atual vai para o alvo; a alternativa
    # que ocupava o alvo passa para a posição antiga.
    source_for_position = {letter: letter for letter in "ABCD"}
    source_for_position[current], source_for_position[target] = target, current
    original = {match.group(1): match.group(2) for match in lines}

    replacements: list[tuple[int, int, str]] = []
    for match in lines:
        position = match.group(1)
        replacements.append(
            (match.start(), match.end(), f"- **{position})** {original[source_for_position[position]]}")
        )
    answer_letter_start = current_match.start(1) if current_match.group(1) else current_match.start(2)
    replacements.append((answer_letter_start, answer_letter_start + 1, target))
    for start, end, value in sorted(replacements, reverse=True):
        section = section[:start] + value + section[end:]
    if current != target:
        section = re.sub(
            rf"(?m)^(\*\*Observação:\*\*[^\r\n]*?\b){current}(\s+é o gabarito\b)",
            rf"\g<1>{target}\2",
            section,
        )
    return section


def swap_item_options(section: str, item_id: str, current: str, target: str) -> str:
    lines = list(re.finditer(r"(?m)^([A-D])\)\s+(.+)$", section))
    if len(lines) != 4 or [match.group(1) for match in lines] != list("ABCD"):
        raise ValueError(f"{item_id}: alternativas A–D não reconhecidas")
    source_for_position = {letter: letter for letter in "ABCD"}
    source_for_position[current], source_for_position[target] = target, current
    original = {match.group(1): match.group(2) for match in lines}
    replacements = [
        (match.start(), match.end(), f"{match.group(1)}) {original[source_for_position[match.group(1)]]}")
        for match in lines
    ]
    for start, end, value in sorted(replacements, reverse=True):
        section = section[:start] + value + section[end:]
    return section


def update_tables(source: str, targets: dict[str, str]) -> str:
    lines = source.splitlines()
    current_day: int | None = None
    for index, line in enumerate(lines):
        day_heading = re.match(r"^# Dia ([1-6])\b", line)
        if day_heading:
            current_day = int(day_heading.group(1))
        if not line.lstrip().startswith("|"):
            continue

        # Linha vertical: | S3... | A |
        vertical = re.fullmatch(r"\|\s*(S3(?:D[1-6]Q|S)\d{3})\s*\|\s*([A-D])\s*\|", line.strip())
        if vertical and vertical.group(1) in targets:
            lines[index] = f"| {vertical.group(1)} | {targets[vertical.group(1)]} |"
            continue
        vertical_extra = re.fullmatch(
            r"\|\s*([1-6]\.\d+)\s*\|\s*([A-D])\s*\|",
            line.strip(),
        )
        if vertical_extra:
            item_id = f"Extra Dia {vertical_extra.group(1)}"
            if item_id in targets:
                lines[index] = f"| {vertical_extra.group(1)} | {targets[item_id]} |"
            continue
        vertical_local = re.fullmatch(r"\|\s*(\d{1,2})\s*\|\s*([A-D])\s*\|", line.strip())
        if vertical_local and current_day is not None:
            local = int(vertical_local.group(1))
            item_id = f"S3D{current_day}Q{((current_day - 1) * 50 + local):03d}"
            if item_id in targets:
                lines[index] = f"| {local} | {targets[item_id]} |"
            continue

        ids = re.findall(r"S3(?:D[1-6]Q|S)\d{3}", line)
        if len(ids) >= 2:
            if index + 2 >= len(lines):
                raise ValueError("tabela horizontal truncada")
            # Faixas como ``S3S001–S3S010`` também contêm dois IDs, mas
            # não são cabeçalhos de uma tabela horizontal de gabarito.
            if not re.fullmatch(r"\|(?:\s*:?-{3,}:?\s*\|)+", lines[index + 1].strip()):
                continue
            values = re.findall(r"(?<=\|)\s*([A-D])\s*(?=\|)", lines[index + 2])
            if len(values) != len(ids):
                raise ValueError(f"tabela horizontal inválida para {ids[0]}")
            lines[index + 2] = "| " + " | ".join(targets[item_id] for item_id in ids) + " |"
            continue

        locals_ = re.findall(r"(?<=\|)\s*([1-6]\.\d+)\s*(?=\|)", line)
        if len(locals_) >= 2:
            if index + 2 >= len(lines):
                raise ValueError("tabela horizontal de extras truncada")
            item_ids = [f"Extra Dia {value}" for value in locals_]
            values = re.findall(r"(?<=\|)\s*([A-D])\s*(?=\|)", lines[index + 2])
            if len(values) != len(item_ids):
                raise ValueError(f"tabela horizontal de extras inválida para {item_ids[0]}")
            lines[index + 2] = "| " + " | ".join(targets[item_id] for item_id in item_ids) + " |"
    return "\n".join(lines) + ("\n" if source.endswith("\n") else "")


def apply_targets(paths: list[Path], targets: dict[str, str], super_mode: bool = False) -> None:
    for path in paths:
        source = path.read_text(encoding="utf-8")
        if super_mode:
            item_spans = section_spans(source, r"(S3S\d{3})\s+(?:—|-)\s+.+")
            comment_spans = section_spans(source, r"Comentário (S3S\d{3})")
        else:
            item_spans = {}
            item_rx = re.compile(r"(?m)^(#{1,6}) ((S3D[1-6]Q\d{3})|(Extra Dia [1-6]\.\d+))(?:\s+(?:—|-)\s+.+)?\s*$")
            headings = list(re.finditer(r"(?m)^(#{1,6}) .+$", source))
            for match in item_rx.finditer(source):
                end = len(source)
                for heading in headings:
                    if heading.start() > match.start():
                        end = heading.start()
                        break
                item_spans[match.group(3) or match.group(4)] = (match.start(), end)
            comment_spans = {
                **section_spans(source, r"Comentário (S3D[1-6]Q\d{3})"),
                **section_spans(source, r"Comentário (Extra Dia [1-6]\.\d+)"),
            }

        replacements: list[tuple[int, int, str]] = []
        for item_id, (item_start, item_end) in item_spans.items():
            if item_id not in targets:
                continue
            if item_id not in comment_spans:
                raise ValueError(f"{item_id}: comentário ausente")
            comment_start, comment_end = comment_spans[item_id]
            comment_section = source[comment_start:comment_end]
            old = answer_value(answer_match(comment_section))
            target = targets[item_id]
            item_section = swap_item_options(source[item_start:item_end], item_id, old, target)
            comment_section = replace_section(comment_section, item_id, target, comment=True)
            replacements.extend(
                [(item_start, item_end, item_section), (comment_start, comment_end, comment_section)]
            )

        for start, end, value in sorted(replacements, reverse=True):
            source = source[:start] + value + source[end:]
        source = update_tables(source, targets)
        path.write_text(source, encoding="utf-8", newline="\n")


def main() -> None:
    bank_items, _ = load_items(BANK_PARTS)
    if len(bank_items) != 420:
        raise SystemExit(f"banco incompleto: {len(bank_items)} itens; esperado 420")
    bank_targets = target_answers(bank_items, base_seed=30_720_126)
    apply_targets(BANK_PARTS, bank_targets)

    super_items, _ = load_items([SUPER_PATH], super_mode=True)
    if len(super_items) != 60:
        raise SystemExit(f"super incompleto: {len(super_items)} itens; esperado 60")
    super_targets = target_answers(super_items, base_seed=60_720_126)
    apply_targets([SUPER_PATH], super_targets, super_mode=True)

    print("Gabaritos permutados e sincronizados; equilíbrio por nível e anti-padrão validados.")


if __name__ == "__main__":
    main()
