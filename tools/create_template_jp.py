#!/usr/bin/env python3
import os

with open('spoilers/template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 日本語化の置換
html = html.replace('<html lang="en">', '<html lang="ja">')
html = html.replace(
    "<title>NetHack Spoilers: A Traveler's Companion to the Mazes of Menace</title>",
    "<title>NetHack スポイラー: 脅威の迷宮への旅人の手引き (5.0対応版)</title>"
)

# Google Fonts に Noto Serif JP を追加
html = html.replace(
    'family=EB+Garamond',
    'family=Noto+Serif+JP:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&family=EB+Garamond'
)

html = html.replace('<div class="sidebar-title">Contents</div>', '<div class="sidebar-title">目次</div>')
html = html.replace('<div class="sidebar-title">Search</div>', '<div class="sidebar-title">検索</div>')
html = html.replace('placeholder="Search the guide..."', 'placeholder="ガイド内を検索..."')
html = html.replace('<span class="page-fold-text">New!<br>Updated for 5.0</span>', '<span class="page-fold-text">5.0対応<br>完全改訂</span>')

with open('spoilers/template.jp.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("spoilers/template.jp.html generated successfully.")

