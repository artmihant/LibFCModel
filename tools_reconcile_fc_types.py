import re
import ast
from pathlib import Path


def extract_spec_map(spec_md: str) -> dict:
    # Ограничиваем парсинг секцией elem_types
    start_marker = "\n#### elem_types"
    end_marker = "\n### materials"
    start = spec_md.find(start_marker)
    if start != -1:
        end = spec_md.find(end_marker, start)
        segment = spec_md[start:end if end != -1 else None]
    else:
        segment = spec_md
    pattern = re.compile(r"^\s*(\d+)\s*=\s*([A-Z0-9_]+)\s*,?\s*$", re.M)
    return {int(m.group(1)): m.group(2) for m in pattern.finditer(segment)}


def extract_constants_map(constants_py: str) -> dict:
    m = re.search(r"FC_ELEMENT_TYPES\s*:[^{=]+\=\s*\{", constants_py)
    if not m:
        raise RuntimeError("FC_ELEMENT_TYPES not found in constants.py")
    start = m.end() - 1
    depth = 0
    end = None
    for i, ch in enumerate(constants_py[start:], start=start):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end is None:
        raise RuntimeError("Failed to parse FC_ELEMENT_TYPES braces")
    dict_src = constants_py[start:end]
    data = ast.literal_eval(dict_src)
    return {int(k): v['name'] for k, v in data.items()}


def main() -> Path:
    root = Path(__file__).resolve().parent
    spec_md = (root / "docs" / "FidesysCase.md").read_text(encoding="utf-8")
    constants_py = (root / "constants.py").read_text(encoding="utf-8")

    spec_map = extract_spec_map(spec_md)
    const_map = extract_constants_map(constants_py)

    missing_in_consts = {k: spec_map[k] for k in sorted(set(spec_map) - set(const_map))}
    missing_in_spec = {k: const_map[k] for k in sorted(set(const_map) - set(spec_map))}
    name_mismatch = {k: (spec_map[k], const_map[k]) for k in sorted(set(spec_map) & set(const_map)) if spec_map[k] != const_map[k]}

    lines = ["## Сверка FC_ELEMENT_TYPES со спецификацией", ""]
    if missing_in_consts:
        lines.append("### Отсутствуют в constants.py (есть в спецификации)")
        lines += [f"- {k}: {v}" for k, v in missing_in_consts.items()]
    if missing_in_spec:
        lines.append("")
        lines.append("### Отсутствуют в спецификации (есть в constants.py)")
        lines += [f"- {k}: {v}" for k, v in missing_in_spec.items()]
    if name_mismatch:
        lines.append("")
        lines.append("### Несовпадения имён по одинаковым кодам")
        lines += [f"- {k}: spec={s} vs code={c}" for k, (s, c) in name_mismatch.items()]

    out = root / "docs" / "FCElementTypes_Reconciliation.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    print(main())


