#!/usr/bin/env python3
import os
import re

files = [
    ("113-ar-Professional-Email-Writing.md", "**تحميل إضافة Chrome**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-bn-Professional-Email-Writing.md", "**Chrome প্লাগইন ডাউনলোড**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-de-Professional-Email-Writing.md", "**Chrome-Erweiterung Herunterladen**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-en-Professional-Email-Writing.md", "**Download Chrome Extension**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-es-Professional-Email-Writing.md", "**Descargar Extensión de Chrome**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-hi-Professional-Email-Writing.md", "**Chrome एक्सटेंशन डाउनलोड करें**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-ja-Professional-Email-Writing.md", "**Chrome 拡張機能をダウンロード**：", "https://chrome.google.com/webstore/detail/mkhpgbbhlnmjbkihoeniojulti-ai/dpkggkabbbl"),
    ("113-pt-Professional-Email-Writing.md", "**Baixar Extensão do Chrome**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-ru-Professional-Email-Writing.md", "**Скачать расширение Chrome**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
    ("113-vi-Professional-Email-Writing.md", "**Tải Tiện Ích Chrome**：", "https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl"),
]

for filename, download_text, url in files:
    filepath = os.path.join("/root/.openclaw/workspace/AICompareBlog/articles", filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 在 --- 和 **Related Searches 之前插入下载链接
    pattern = r'(\n---\n)(\*\*[^}]+\*\*:[^*]+\*)'
    replacement = r'\1\n' + download_text + r'\n> [AI Compare - Chrome Web Store](' + url + r')\n\n\2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated: {filename}")
