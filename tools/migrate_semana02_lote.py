from __future__ import annotations

import argparse
import re
from pathlib import Path


def level_for(number: int, extra: bool = False) -> str:
    if extra:
        return "Médio" if number <= 8 else "Difícil" if number <= 16 else "Muito difícil"
    return "Médio" if number <= 20 else "Difícil" if number <= 40 else "Muito difícil"


def use_for(number: int, extra: bool = False) -> str:
    if extra:
        return "Essenciais" if number <= 5 else "Aprofundamento" if number <= 10 else "Revisão" if number <= 15 else "Simulado"
    return "Essenciais" if number <= 10 else "Aprofundamento" if number <= 30 else "Revisão" if number <= 40 else "Simulado"


def clean_title(concept: str) -> str:
    concept = re.sub(r"\s+", " ", concept.strip()).rstrip(".")
    return concept[:1].upper() + concept[1:]


def migrate_day(text: str, day: int) -> str:
    start_match = re.search(rf"(?m)^# Dia {day} —", text)
    if not start_match:
        raise ValueError(f"Dia {day} não encontrado")
    next_match = re.search(rf"(?m)^# Dia {day + 1} —", text[start_match.end():]) if day < 6 else None
    end = start_match.end() + next_match.start() if next_match else len(text)
    prefix, block, suffix = text[:start_match.start()], text[start_match.start():end], text[end:]

    comment_data: dict[int, tuple[str, str]] = {}
    comment_matches = list(re.finditer(r"(?m)^#{3,4} Comentário da Questão (\d+)\s*$", block))
    for index, match in enumerate(comment_matches):
        number = int(match.group(1))
        cend = comment_matches[index + 1].start() if index + 1 < len(comment_matches) else len(block)
        section = block[match.end():cend]
        concept_match = re.search(r"(?m)^\*\*Conceito:\*\*\s*(.+)$", section)
        ref_match = re.search(r"(?m)^\*\*Referência:\*\*\s*(.+)$", section)
        if concept_match and ref_match:
            comment_data[number] = (clean_title(concept_match.group(1)), ref_match.group(1).strip())

    main_limit_match = re.search(r"(?m)^#### Extra Dia", block)
    if not main_limit_match:
        raise ValueError(f"Extras do Dia {day} não encontradas")
    main, rest = block[:main_limit_match.start()], block[main_limit_match.start():]

    def replace_main(match: re.Match[str]) -> str:
        number = int(match.group(1))
        if number not in comment_data:
            raise ValueError(f"Comentário/referência ausente no Dia {day}, Questão {number}")
        title, reference = comment_data[number]
        global_id = (day - 1) * 50 + number
        return (
            f"### S2D{day}Q{global_id:03d} — {title}\n\n"
            f"**Nível:** {level_for(number)}\n\n"
            f"**Uso:** {use_for(number)}\n\n"
            f"**Referência:** {reference}\n"
        )

    main = re.sub(r"(?m)^### Questão (\d+)\s*$", replace_main, main)
    block = main + rest

    def replace_comment(match: re.Match[str]) -> str:
        number = int(match.group(1))
        global_id = (day - 1) * 50 + number
        return (
            f"### Comentário S2D{day}Q{global_id:03d}\n\n"
            f"**Nível:** {level_for(number)}\n\n"
            f"**Uso:** {use_for(number)}"
        )

    block = re.sub(r"(?m)^#{3,4} Comentário da Questão (\d+)\s*$", replace_comment, block)

    def add_extra_use(match: re.Match[str]) -> str:
        number = int(match.group(1))
        body = match.group(2)
        if re.search(r"(?m)^- \*\*Uso:\*\*", body):
            return match.group(0)
        body = re.sub(
            r"(?m)^(- \*\*Nível:\*\* .+)$",
            rf"\1\n- **Uso:** {use_for(number, extra=True)}",
            body,
            count=1,
        )
        return f"#### Extra Dia {day}.{number}\n{body}"

    extra_pattern = rf"(?ms)^#### Extra Dia {day}\.(\d+)\s*\n(.*?)(?=^#### Extra Dia {day}\.\d+\s*$|^## Gabarito do Dia {day}\s*$)"
    block = re.sub(extra_pattern, add_extra_use, block)

    def add_extra_comment_use(match: re.Match[str]) -> str:
        number = int(match.group(1))
        body = match.group(2)
        if re.search(r"(?m)^\*\*Uso:\*\*", body):
            return match.group(0)
        body = re.sub(
            r"(?m)^(\*\*Nível:\*\* .+)$",
            rf"\1\n\n**Uso:** {use_for(number, extra=True)}",
            body,
            count=1,
        )
        return f"#### Comentário Extra Dia {day}.{number}\n{body}"

    extra_comment_pattern = rf"(?ms)^#### Comentário Extra Dia {day}\.(\d+)\s*\n(.*?)(?=^#### Comentário Extra Dia {day}\.\d+\s*$|^---\s*$|^# Dia {day + 1} —|\Z)"
    block = re.sub(extra_comment_pattern, add_extra_comment_use, block)
    return prefix + block + suffix


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--days", nargs="+", type=int, required=True)
    args = parser.parse_args()
    text = args.path.read_text(encoding="utf-8")
    for day in sorted(args.days, reverse=True):
        text = migrate_day(text, day)
    args.path.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
