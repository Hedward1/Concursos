"""Monta os arquivos consolidados da Semana 3 a partir de lotes auditáveis.

Os lotes permanecem separados durante a produção para respeitar o limite de dois
dias por checkpoint. A consolidação é mecânica: não transforma conteúdo, IDs,
âncoras, gabaritos ou comentários.
"""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Analista de sistemas" / "semana_03"
PARTS = WEEK / "partes"

TARGETS = {
    "study": (
        WEEK / "semana_03_estudo.md",
        [
            PARTS / "estudo_preambulo.md",
            PARTS / "estudo_dias_01_02.md",
            PARTS / "estudo_dias_03_04.md",
            PARTS / "estudo_dias_05_06.md",
        ],
    ),
    "questions": (
        WEEK / "semana_03_questoes.md",
        [
            PARTS / "questoes_preambulo.md",
            PARTS / "questoes_dias_01_02.md",
            PARTS / "questoes_dias_03_04.md",
            PARTS / "questoes_dias_05_06.md",
        ],
    ),
}


def build(name: str) -> None:
    target, sources = TARGETS[name]
    missing = [source for source in sources if not source.is_file()]
    if missing:
        joined = "\n".join(f"- {path.relative_to(ROOT)}" for path in missing)
        raise SystemExit(f"Lotes ausentes para {name}:\n{joined}")

    chunks = [source.read_text(encoding="utf-8").rstrip() for source in sources]
    target.write_text("\n\n".join(chunks) + "\n", encoding="utf-8", newline="\n")
    print(f"Montado: {target.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "component",
        choices=["study", "questions", "all"],
        default="all",
        nargs="?",
    )
    args = parser.parse_args()

    names = TARGETS if args.component == "all" else [args.component]
    for name in names:
        build(name)


if __name__ == "__main__":
    main()
