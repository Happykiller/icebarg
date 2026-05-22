#!/usr/bin/env python3
"""
generate.py — Packager le livrable Claude.ai de fiscal-fr

Usage : python3 claude/claude-code/skills/generate-claudeai-package/generate.py
        (à appeler depuis la racine du projet)

Ce script :
  1. Vérifie que les 3 fichiers source existent dans claude/claudeai/
  2. Lit la version depuis VERSION (ou fallback date du jour)
  3. Crée claude/claudeai/fiscal-fr-claudeai-vX.Y.Z.zip (tracké git)
  4. Affiche checksum SHA256 + instructions
"""

import hashlib
import json
import os
import sys
import zipfile
from datetime import date
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────

def _find_project_root() -> Path:
    """Remonte l'arbre jusqu'à trouver VERSION (marqueur racine projet)."""
    p = Path(__file__).resolve().parent
    for _ in range(8):
        if (p / "VERSION").exists():
            return p
        p = p.parent
    raise RuntimeError("Racine projet introuvable (VERSION absent)")

PROJECT_ROOT = _find_project_root()
DIST_DIR     = PROJECT_ROOT / "claude" / "claudeai"
OUTPUT_DIR   = PROJECT_ROOT / "claude" / "claudeai"

REQUIRED_FILES = ["SKILL.md", "REFERENCE.md", "README.md"]

MCP_URL = "https://kalifa.happykiller.net/mcp"


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_version() -> str:
    """Lit la version depuis VERSION, sinon package.json, sinon date du jour."""
    ver_file = PROJECT_ROOT / "VERSION"
    if ver_file.exists():
        v = ver_file.read_text().strip()
        if v:
            return v
    pkg = PROJECT_ROOT / "package.json"
    if pkg.exists():
        try:
            return json.loads(pkg.read_text())["version"]
        except (KeyError, json.JSONDecodeError):
            pass
    return date.today().strftime("%Y.%m.%d")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def check_sources() -> list[str]:
    """Retourne la liste des fichiers manquants."""
    missing = []
    for f in REQUIRED_FILES:
        if not (DIST_DIR / f).exists():
            missing.append(f)
    return missing


def validate_skill_md() -> list[str]:
    """Vérifie les contraintes du SKILL.md (frontmatter, description ≤ 200 chars)."""
    warnings = []
    skill_path = DIST_DIR / "SKILL.md"
    if not skill_path.exists():
        return warnings

    content = skill_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    if not content.startswith("---"):
        warnings.append("SKILL.md : frontmatter YAML manquant (doit commencer par ---)")
        return warnings

    # Extraire le frontmatter
    end_fm = content.find("---", 3)
    if end_fm == -1:
        warnings.append("SKILL.md : frontmatter YAML non fermé")
        return warnings

    frontmatter = content[3:end_fm]
    if "name:" not in frontmatter:
        warnings.append("SKILL.md : champ 'name' manquant dans le frontmatter")
    if "description:" not in frontmatter:
        warnings.append("SKILL.md : champ 'description' manquant dans le frontmatter")
    else:
        # Vérifier longueur description
        for line in frontmatter.splitlines():
            if line.strip().startswith("description:"):
                desc = line.split("description:", 1)[1].strip().strip('"').strip("'")
                if len(desc) > 200:
                    warnings.append(
                        f"SKILL.md : description trop longue ({len(desc)} chars, max 200) — "
                        "Claude.ai tronquera automatiquement"
                    )
                break

    # Vérifier disclaimer
    if "disclaimer" not in content.lower() and "expert-comptable" not in content.lower():
        warnings.append(
            "SKILL.md : pas de disclaimer trouvé — "
            "recommandé pour un assistant fiscal"
        )

    # Vérifier placeholders non remplacés
    placeholders = [p for p in ["{{VERSION}}", "{{DATE_ISO}}", "{{ORCHESTRATION_SEQUENCES}}"]
                    if p in content]
    if placeholders:
        warnings.append(
            f"SKILL.md : placeholders non remplacés : {', '.join(placeholders)}"
        )

    return warnings


def validate_reference_md() -> list[str]:
    warnings = []
    ref_path = DIST_DIR / "REFERENCE.md"
    if not ref_path.exists():
        return warnings

    content = ref_path.read_text(encoding="utf-8")

    required_sections = ["Barème IR", "Plafonds", "Dates clés"]
    for section in required_sections:
        if section not in content:
            warnings.append(f"REFERENCE.md : section '{section}' manquante")

    # Détecter valeurs placeholder non remplacées
    import re
    unset = re.findall(r"\{\{[A-Z_]+\}\}", content)
    if unset:
        warnings.append(
            f"REFERENCE.md : {len(unset)} valeurs à compléter : {', '.join(set(unset))}"
        )

    return warnings


def build_zip(version: str) -> Path:
    """Crée le ZIP et retourne son chemin."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_name = f"fiscal-fr-claudeai-v{version}.zip"
    zip_path = OUTPUT_DIR / zip_name

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in REQUIRED_FILES:
            src = DIST_DIR / fname
            zf.write(src, fname)    # stocké à la racine du ZIP

    return zip_path


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("\n🔧 fiscal-fr — Générateur de package Claude.ai")
    print("=" * 52)

    # 1. Vérifier les sources
    missing = check_sources()
    if missing:
        print(f"\n❌ Fichiers manquants dans claude/claudeai/ :")
        for f in missing:
            print(f"   • {f}")
        print("\n💡 Lance d'abord la Skill : /generate-claudeai-package")
        print("   Elle génère ces fichiers avant que ce script les packette.")
        sys.exit(1)

    # 2. Validation qualité
    all_warnings = validate_skill_md() + validate_reference_md()

    # 3. Lire la version
    version = get_version()

    # 4. Statistiques des fichiers
    stats = {}
    for fname in REQUIRED_FILES:
        path = DIST_DIR / fname
        lines = len(path.read_text(encoding="utf-8").splitlines())
        size  = path.stat().st_size
        stats[fname] = {"lines": lines, "size": size}

    # 5. Créer le ZIP
    zip_path = build_zip(version)
    checksum = sha256_file(zip_path)
    zip_size = zip_path.stat().st_size

    # 6. Rapport
    print(f"\n✅ Package généré : {zip_path.relative_to(PROJECT_ROOT)}")
    print(f"   Taille : {zip_size / 1024:.1f} Ko")
    print(f"   SHA256 : {checksum[:16]}…")

    print(f"\n📦 Contenu :")
    for fname, s in stats.items():
        print(f"   • {fname:<15} {s['lines']:>4} lignes  ({s['size'] / 1024:.1f} Ko)")

    if all_warnings:
        print(f"\n⚠️  Points d'attention ({len(all_warnings)}) :")
        for w in all_warnings:
            print(f"   • {w}")
    else:
        print("\n✅ Validation qualité : aucun problème détecté")

    print(f"\n📋 Distribution :")
    print(f"   1. Uploader dans Claude.ai > Personnaliser > Compétences")
    print(f"   2. MCP URL à partager : {MCP_URL}")
    print(f"   3. Pour GitHub Releases : git tag v{version} && git push --tags")
    print()


if __name__ == "__main__":
    main()