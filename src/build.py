import os
import json

# ----------------------------------------
# 1) Carregar config.json
# ----------------------------------------
CONFIG_FILE = "config.json"

with open(CONFIG_FILE, "r", encoding="utf8") as f:
    config = json.load(f)

title = config["title"]
description = config["description"]
image_name = config["image"]        # ex: "marmita_fit.jpg"
base_url = config["url"]            # ex: "https://victor-ocn.github.io/marmitafit/"
phone = config["phone_number"]
message = config["message"].replace(" ", "%20")
button_text = config["button_text"]
primary_color = config["primary_color"]
redirect_delay = config["redirect_delay"]
path = config["path"]

# URL final da página (url + path)
full_url = base_url + path

# Arquivo de imagem dentro de /images
local_image_path = os.path.join("images", image_name)

# URL completa da imagem
image_full_url = base_url + "images/" + image_name


# ----------------------------------------
# 2) Validar se a imagem existe em /images
# ----------------------------------------
if not os.path.exists(local_image_path):
    print("❌ ERRO: A imagem definida no config.json não foi encontrada.")
    print(f"Procurado em: {local_image_path}")
    print("Certifique-se de colocar a imagem dentro do diretório /images/")
    exit(1)
else:
    print(f"🖼️ Imagem encontrada em /images: {local_image_path}")


# ----------------------------------------
# 3) Criar diretório de destino (path)
# ----------------------------------------
if not os.path.exists(path):
    os.makedirs(path)
    print(f"📁 Diretório criado: {path}")
else:
    print(f"📁 Diretório já existe: {path}")


# ----------------------------------------
# 4) Criar index.html utilizando a URL da imagem em /images
# ----------------------------------------
whatsapp_link = f"https://wa.me/{phone}?text={message}"

html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- 🔒 Meta tags OG -->
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{image_full_url}" />
  <meta property="og:url" content="{full_url}" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />

  <title>{title}</title>

  <style>
    body {{
      text-align: center;
      font-family: "Segoe UI", Roboto, sans-serif;
      background-color: #fff;
      margin: 0;
      padding: 50px 20px;
      color: #333;
    }}
    img {{
      max-width: 300px;
      border-radius: 16px;
      margin-bottom: 20px;
    }}
    h1 {{
      margin-bottom: 10px;
    }}
    p {{
      font-size: 18px;
      margin: 10px 0;
    }}
    a.button {{
      display: inline-block;
      margin-top: 30px;
      padding: 15px 35px;
      color: white;
      text-decoration: none;
      border-radius: 12px;
      font-size: 20px;
      font-weight: bold;
      background-color: {primary_color};
    }}
  </style>
</head>

<body>

  <img src="{image_full_url}" alt="Imagem" />

  <h1>{title}</h1>

  <p>{description}</p>

  <a class="button" href="{whatsapp_link}">{button_text}</a>

  <script>
    setTimeout(() => {{
      window.location.href = "{whatsapp_link}";
    }}, {redirect_delay});
  </script>

</body>
</html>
"""

output_file = os.path.join(path, "index.html")

with open(output_file, "w", encoding="utf8") as f:
    f.write(html_content)

print(f"✅ index.html criado: {output_file}")
print("🎉 Finalizado com sucesso!")

