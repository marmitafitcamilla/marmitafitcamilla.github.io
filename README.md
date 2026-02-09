# 🌱 Marmita Fit da Camilla

Repositório oficial do site Marmita Fit da Camilla e links de marketing para redirecionamento de contato com whatsapp.

O arquivo index.html contém todas as informações estáticas de forma simples para garantir o hospedagem gratuita via **GitHub Pages**.

Algumas configurações adicionais de design são orinundas do arquivo templates > template.html

---

## 💡 Links de Marketing

Os redirecionamentos (redirects) são htmls simples (`index.html`) com uma imagem vinculada.
O objetivo é permitir que, ao postar o link em **grupos de WhatsApp**, o preview mostre **imagem, título e descrição**, e que ao clicar o usuário seja levado diretamente para uma conversa para o contato de WhatsApp.

O HTML contém:
- **Tags Open Graph (`og:`)** → controlam o preview mostrado no WhatsApp (título, descrição e imagem).
- **Redirecionamento automático** → após 2 segundos, o visitante é levado para o WhatsApp.
- **Botão manual** → usado como alternativa caso o redirecionamentos automático seja bloqueado pelo aplicativo.
- **Fallback `<noscript>`** → garante o redirecionamento mesmo se o navegador tiver JavaScript desativado.


### 🧭 Comportamento inteligente
| Ambiente | O que acontece |
|-----------|----------------|
| **WhatsApp (app mobile)** | Mostra o site e permite clicar no botão para abrir o chat. |
| **Navegador comum (PC ou celular)** | Redireciona automaticamente após 2 segundos. |
| **WhatsApp Web / Desktop** | Redireciona normalmente para o WhatsApp Web. |
| **JavaScript desativado** | Usa fallback automático (`<noscript>`). |

---
## Como criar novos links de redirecionamento?
É preciso alterar o arquivo de configuração src/config.json e rodar o script /src/build.py na máquina local.
Depois basta submeter o caminho do novo HTML para o GitHub.

---
## Estrutura do projeto
.
├── index.html
├── favicon.png
├── README.md
├── src
│   ├── build.py
│   ├── config.json
│   ├── paths.py
├── redirects
├── images
│   ├── branding
│   ├── hero
│   ├── og
│   └── produtos
└── templates
    ├── redirect.html
    └── template.html
