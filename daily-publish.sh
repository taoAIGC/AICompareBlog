#!/bin/bash
# AICompare Blog Daily Publisher - 支持88篇文章循环
REPO_DIR="/root/clawd/AICompareBlog"
cd "$REPO_DIR" || exit 1

# 获取今天是今年的第几天
DAY_OF_YEAR=$(date +%j)
ARTICLE_NUM=$(( (DAY_OF_YEAR - 1) % 88 + 13 ))

# 查找文章文件
shopt -s nullglob
FILES=(articles/${ARTICLE_NUM}-*.md)
if [ ${#FILES[@]} -eq 0 ]; then
    echo "未找到文章: $ARTICLE_NUM"
    exit 1
fi

TARGET_FILE="${FILES[0]}"
FILENAME=$(basename "$TARGET_FILE")

# 获取标题
TITLE=$(head -n 1 "$TARGET_FILE" | sed 's/^# //')

# 复制到根目录
cp "$TARGET_FILE" "$REPO_DIR/$FILENAME"

# Git操作
git add "$FILENAME"
git commit -m "feat: $(date '+%Y-%m-%d') - $TITLE"

# 推送
git push origin main

echo "[$(date)] 已推送: $TITLE"
