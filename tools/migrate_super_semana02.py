from __future__ import annotations

import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPER = ROOT / "Analista de sistemas/semana_02/semana_02_super_simulado.md"
BANK = ROOT / "Analista de sistemas/semana_02/semana_02_questoes.md"


def tokens(value: str) -> set[str]:
    value = unicodedata.normalize("NFKD", value.lower()).encode("ascii", "ignore").decode()
    words = re.findall(r"[a-z0-9/]+", value)
    stop = {"de", "da", "do", "das", "dos", "e", "em", "para", "com", "por", "no", "na", "um", "uma", "entre", "como"}
    return {word for word in words if len(word) > 2 and word not in stop}


def level(number: int) -> str:
    return "Médio" if number <= 24 else "Difícil" if number <= 48 else "Muito difícil"


def title(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip()).rstrip(".")
    return value[:1].upper() + value[1:]


bank = BANK.read_text(encoding="utf-8")
anchors: list[tuple[str, str]] = []
for match in re.finditer(r"(?ms)^### Comentário S2D\dQ\d+.*?^\*\*Conceito:\*\*\s*(.+?)\s*$.*?^\*\*Referência:\*\*\s*(.+?)\s*$", bank):
    anchors.append((match.group(1).strip(), match.group(2).strip()))


def best_reference(concept: str) -> str:
    source = tokens(concept)
    ranked = []
    for candidate, reference in anchors:
        target = tokens(candidate)
        union = source | target
        score = len(source & target) / len(union) if union else 0
        ranked.append((score, reference))
    ranked.sort(reverse=True)
    return ranked[0][1]


text = SUPER.read_text(encoding="utf-8")
comments_start = text.index("## Comentários")
question_part, comment_part = text[:comments_start], text[comments_start:]

comments: dict[int, tuple[str, str, str]] = {}
matches = list(re.finditer(r"(?m)^### Comentário da Questão (\d+)\s*$", comment_part))
for index, match in enumerate(matches):
    number = int(match.group(1))
    end = matches[index + 1].start() if index + 1 < len(matches) else len(comment_part)
    section = comment_part[match.end():end]
    answer = re.search(r"\*\*Alternativa correta:\s*([A-D])\.\*\*", section).group(1)
    concept = re.search(r"(?m)^\*\*Conceito:\*\*\s*(.+)$", section).group(1).strip()
    comments[number] = (answer, concept, best_reference(concept))


question_matches = list(re.finditer(r"(?m)^### Questão (\d+)\s*$", question_part))
question_data: dict[int, dict[str, str]] = {}
for index, match in enumerate(question_matches):
    number = int(match.group(1))
    end = question_matches[index + 1].start() if index + 1 < len(question_matches) else len(question_part)
    section = question_part[match.end():end]
    options = {letter: body.strip() for letter, body in re.findall(r"(?m)^([A-D])\)\s*(.+)$", section)}
    if len(options) != 4:
        raise ValueError(f"Questão {number}: alternativas não reconhecidas")
    question_data[number] = options


def replace_question(match: re.Match[str]) -> str:
    number = int(match.group(1))
    _, concept, reference = comments[number]
    return (
        f"### S2S{number:03d} — {title(concept)}\n\n"
        f"**Nível:** {level(number)}\n\n"
        f"**Uso:** Simulado\n\n"
        f"**Referência:** {reference}\n"
    )


question_part = re.sub(r"(?m)^### Questão (\d+)\s*$", replace_question, question_part)


def replace_comment(match: re.Match[str]) -> str:
    number = int(match.group(1))
    answer, concept, reference = comments[number]
    options = question_data[number]
    lines = [
        f"### Comentário S2S{number:03d}",
        "",
        f"**Alternativa correta: {answer}.**",
        "",
        f"**Nível:** {level(number)}",
        "",
        "**Uso:** Simulado",
        "",
        "**Análise das alternativas:**",
        "",
    ]
    correct_rule = options[answer].rstrip(".")
    for letter in "ABCD":
        option = options[letter].rstrip(".")
        if letter == answer:
            reason = f"Correta. {option}. A proposição aplica o ponto decisivo de {concept}."
        else:
            reason = f"Incorreta. A opção sustenta que {option}; no caso, a regra decisiva é: {correct_rule}."
        lines.append(f"- **{letter})** {reason}")
    lines.extend([
        "",
        f"**Conceito:** {concept}",
        "",
        "**Pegadinha:** aceitar uma afirmação tecnicamente próxima sem conferir a função, a camada, a condição ou o limite indicado no enunciado.",
        "",
        "**Como pensar:** isole a condição do cenário, elimine opções que mudam a finalidade do mecanismo e teste a regra técnica contra cada alternativa.",
        "",
        f"**Referência:** {reference}",
        "",
    ])
    return "\n".join(lines)


comment_part = re.sub(
    r"(?ms)^### Comentário da Questão (\d+)\s*$.*?(?=^### Comentário da Questão \d+\s*$|\Z)",
    replace_comment,
    comment_part,
)

SUPER.write_text(question_part + comment_part, encoding="utf-8", newline="\n")
