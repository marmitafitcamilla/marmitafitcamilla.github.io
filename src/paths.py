#!/usr/bin/env python3
"""
paths.py - Configuração de caminhos para o projeto Marmita Fit
"""

from pathlib import Path

# Diretório onde este script está (src/)
SCRIPT_DIR = Path(__file__).parent

# Diretório raiz do projeto (um nível acima de src/)
ROOT_DIR = SCRIPT_DIR.parent

# Diretórios principais
IMAGES_DIR = ROOT_DIR / "images"
REDIRECTS_DIR = ROOT_DIR / "redirects"
TEMPLATES_DIR = ROOT_DIR / "templates"

# Subdiretórios de imagens
BRANDING_DIR = IMAGES_DIR / "branding"
HERO_DIR = IMAGES_DIR / "hero"
IMAGES_OG_DIR = IMAGES_DIR / "og"
PRODUTOS_DIR = IMAGES_DIR / "produtos"

# Arquivo de configuração
CONFIG_PATH = SCRIPT_DIR / "config.json"

# URLs base (ajuste conforme seu domínio GitHub Pages)
BASE_URL = "https://marmitafitcamilla.github.io"
REDIRECTS_URL = f"{BASE_URL}/redirects"
IMAGES_URL = f"{BASE_URL}/images"
IMAGES_OG_URL = f"{IMAGES_URL}/og"

# Função para verificar caminhos
def verify_paths():
    """Verifica se todos os caminhos existem"""
    print("=== VERIFICAÇÃO DE CAMINHOS ===\n")

    paths = {
        "Script (src/)": SCRIPT_DIR,
        "Raiz do projeto": ROOT_DIR,
        "Images": IMAGES_DIR,
        "Redirects": REDIRECTS_DIR,
        "Templates": TEMPLATES_DIR,
        "Config": CONFIG_PATH,
        "OG Images": IMAGES_OG_DIR
    }

    for name, path in paths.items():
        status = "✓" if path.exists() else "✗"
        print(f"{status} {name}: {path}")

    print("\nSubdiretórios de imagens:")
    image_subs = {
        "Branding": BRANDING_DIR,
        "Hero": HERO_DIR,
        "OG": IMAGES_OG_DIR,
        "Produtos": PRODUTOS_DIR,
        "Redirects": REDIRECTS_DIR
    }

    for name, path in image_subs.items():
        status = "✓" if path.exists() else "✗"
        print(f"  {status} {name}: {path}")

    print()

# Variáveis de exportação (para import paths)
__all__ = [
    "ROOT_DIR", "SCRIPT_DIR",
    "IMAGES_DIR", "REDIRECTS_DIR", "TEMPLATES_DIR", "CONFIG_PATH",
    "BRANDING_DIR", "HERO_DIR", "IMAGES_OG_DIR", "PRODUTOS_DIR",
    "BASE_URL", "IMAGES_URL", "REDIRECTS_URL", "IMAGES_OG_URL",
    "verify_paths"
]
