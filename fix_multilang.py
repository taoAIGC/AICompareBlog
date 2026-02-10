#!/usr/bin/env python3
# -*- coding: utf-8 -*-

files = {
    "113-bn-Professional-Email-Writing.md": "Chrome প্লাগইন ডাউনলোড",
    "113-hi-Professional-Email-Writing.md": "Chrome एक्सटेंशन डाउनलोड करें",
    "113-ru-Professional-Email-Writing.md": "Скачать расширение Chrome",
}

for filename, text in files.items():
    filepath = f"/root/.openclaw/workspace/AICompareBlog/articles/{filename}"
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 在最后一个 --- 之后、相关搜索之前插入插件下载链接
    parts = content.rsplit("\n---\n", 1)
    if len(parts) == 2:
        before, after = parts
        new_content = f"{before}\n\n---\n\n**{text}**：\n> [AI Compare - Chrome Web Store](https://chrome.google.com/webstore/detail/multi-ai/dkhpgbbhlnmjbkihoeniojpkggkabbbl)\n\n{after}"
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {filename}")
