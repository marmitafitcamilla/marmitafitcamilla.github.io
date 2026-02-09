#!/usr/bin/env python3
"""
build.py - Gera páginas de redirecionamento personalizadas
Uso: python src/build.py
"""

import json
from pathlib import Path
import time
from paths import (CONFIG_PATH,
                   TEMPLATES_DIR,
                   REDIRECTS_DIR,
                   IMAGES_OG_DIR,
                   IMAGES_URL,
                   REDIRECTS_URL,
                   verify_paths
                   )

def load_config():
    """
    Carrega configuração do arquivo config.json
    """
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Configuração não encontrada: {CONFIG_PATH}")

    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_template(template_name="redirect.html"):
    """
    Carrega template HTML do diretório templates
    """
    template_path = TEMPLATES_DIR / template_name
    if not template_path.exists():
        raise FileNotFoundError(f"Template não encontrado: {template_path}")

    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def create_redirect(config: dict):
    """
    Cria uma página de redirecionamento baseada na configuração

    Args:
        config: dict com title, description, image, phone_number, etc.
    """
    # Nome do redirect (ex: "natal", "a", "b")
    redirect_name = config["output_path"].split("/")[-1]
    redirect_dir = REDIRECTS_DIR / redirect_name

    # Criar diretório se não existir
    redirect_dir.mkdir(parents=True, exist_ok=True)

    # Carregar template
    template = load_template()

    # Calcular caminhos
    image_filename = config["image"]
    image_path = IMAGES_OG_DIR / image_filename

    # Criando URL
    image_url = f"{IMAGES_URL}/og/{image_filename}"
    print(image_url)
    whatsapp_url = f"https://wa.me/{config['phone_number']}?text={config['message']}"
    redirect_url = f"{REDIRECTS_URL}/{redirect_name}"

    # Substituir variáveis no template
    html_content = template.replace("{{TITLE}}", config["title"])
    html_content = html_content.replace("{{DESCRIPTION}}", config["description"])
    html_content = html_content.replace("{{IMAGE_URL}}", image_url)
    html_content = html_content.replace("{{WHATSAPP_URL}}", whatsapp_url)
    html_content = html_content.replace("{{BUTTON_TEXT}}", config["button_text"])
    html_content = html_content.replace("{{PRIMARY_COLOR}}", config["primary_color"])
    html_content = html_content.replace("{{REDIRECT_URL}}", redirect_url)
    html_content = html_content.replace("{{IMAGE_LOGO}}", f"{IMAGES_URL}/og/og-logo.png")

    delay_seconds = config.get("redirect_delay", 2)
    meta_refresh_sec = max(0, int(delay_seconds))
    js_delay_ms = int(delay_seconds * 1000)
    timer_initial = max(1, int(delay_seconds))

    html_content = html_content.replace("{{REDIRECT_DELAY}}", str(meta_refresh_sec))
    html_content = html_content.replace("{{REDIRECT_DELAY_MS}}", str(js_delay_ms))
    html_content = html_content.replace("{{TIMER_INITIAL}}", str(timer_initial))

    # Arquivo de saída
    output_file = redirect_dir / "index.html"

    # Salvar arquivo
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Criado: {output_file}")
    print(f"  📱 WhatsApp: https://wa.me/{config['phone_number']}")
    print(f"  🌐 URL: {redirect_url}")

    return output_file

def main():
    """Função principal"""
    print("🍱 Marmita Fit - Gerador de Redirects\n")

    # Verificar caminhos
    verify_paths()

    # Carregar configuração
    config = load_config()

    print(f"📄 Configuração carregada: {config}")
    print()

    # Verificar se imagem existe
    image_path = IMAGES_OG_DIR / config["image"]
    if not image_path.exists():
        print(f"⚠️ Imagem não encontrada: {image_path}")
        print(f"   Usando imagem padrão...")

    # Criar redirect
    output_file = create_redirect(config)

    # Delay visual
    print(f"\n⏳ Aguardando {config['redirect_delay']:.1f}s para simular...")
    time.sleep(config['redirect_delay'])

    print(f"\n🎉 Pronto! Acesse: {REDIRECTS_URL}/{config['output_path']}")
    print(f"📁 Arquivo salvo em: {output_file}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
