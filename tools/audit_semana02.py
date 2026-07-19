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
expect("alternativas do banco", len(re.findall(r"^[A-D]\) ", bank, re.M)), 420 * 4)
expect("alternativas do super", len(re.findall(r"^[A-D]\) ", super_text, re.M)), 60 * 4)
expect("análises A-D do banco", len(re.findall(r"^- \*\*[A-D]\)\*\*", bank, re.M)), 420 * 4)
expect("análises A-D do super", len(re.findall(r"^- \*\*[A-D]\)\*\*", super_text, re.M)), 60 * 4)

levels = Counter(re.findall(r"^(?:- )?\*\*Nível:\*\* (Médio|Difícil|Muito difícil)$", bank, re.M))
for name, wanted in (("Médio", 168 * 2), ("Difícil", 168 * 2), ("Muito difícil", 84 * 2)):
    expect(f"rótulos {name}", levels[name], wanted)

super_levels = Counter(re.findall(r"^\*\*Nível:\*\* (Médio|Difícil|Muito difícil)$", super_text, re.M))
for name, wanted in (("Médio", 48), ("Difícil", 48), ("Muito difícil", 24)):
    expect(f"rótulos super {name}", super_levels[name], wanted)

answers = re.findall(r"\*\*Alternativa correta:\s*([A-D])\.\*\*", bank)
expect("gabaritos nos comentários do banco", len(answers), 420)
super_answers = re.findall(r"\*\*Alternativa correta:\s*([A-D])\.\*\*", super_text)
expect("gabaritos nos comentários do super", len(super_answers), 60)

for seq_name, seq in (("banco", answers), ("super", super_answers)):
    if any(seq[i] == seq[i + 1] == seq[i + 2] for i in range(len(seq) - 2)):
        errors.append(f"{seq_name}: sequência de três gabaritos iguais")


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    text = re.sub(r"[^a-z0-9 _-]", "", text).strip().replace(" ", "-")
    return re.sub(r"-+", "-", text)


anchors = set(re.findall(r'<a id="([^"]+)"', study))
anchors.update(slug(value) for value in re.findall(r"^#{1,6}\s+(.+)$", study, re.M))
for source_name, source in (("banco", bank), ("super", super_text)):
    fragments = re.findall(r"semana_02_estudo\.md#([a-zA-Z0-9_.-]+)", source)
    missing = sorted({fragment for fragment in fragments if fragment not in anchors})
    if missing:
        errors.append(f"{source_name}: âncoras ausentes: {', '.join(missing[:10])}")

if "Confunde função, camada, garantia ou limite técnico do caso" in super_text:
    errors.append("super: comentário genérico legado encontrado")

if errors:
    print("FALHOU")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("OK: 420 questões + 60 do super simulado; metadados, alternativas, comentários, gabaritos e âncoras validados.")
