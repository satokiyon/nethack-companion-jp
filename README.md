# NetHack Companion 日本語版 (A Traveler's Companion to the Mazes of Menace)

NetHack 5.0 対応の世界的名スポイラー『A Traveler's Companion to the Mazes of Menace』（David Bau 著）の(非公式)日本語翻訳プロジェクトです。

---

## 概要

本プロジェクトは、NetHack 5.0 のコードベースに完全に照合・監査された [スポイラー](https://davidbau.github.io/nethack-companion/spoilers/) を日本語化したものです。用語は [NetHackJP](https://github.com/satokiyon/NetHackJP) に準拠する方針としています。

- **Web版（HTML）**: `spoilers/index.ja.html`
- **印刷・閲覧用PDF版**: `spoilers/companion.ja.pdf`
- **原本Markdown**: `spoilers/companion.ja.md`
- LaTeX版は日本語化していません

---

## 本家更新への追従システム

本リポジトリは、原著リポジトリ（[davidbau/nethack-companion](https://github.com/davidbau/nethack-companion.git)）の更新にいつでも追従できるように設計されています。

運用手順の詳細は **[本家更新追従・運用手順書 (docs/upstream_sync_guide.md)](docs/upstream_sync_guide.md)** をご覧ください。

### クイックコマンド
```powershell
# 本家 (upstream) との差分を自動チェック
python tools/check_upstream_diff.py

# 用語集・構文・テーブル整合性チェック
python tools/check_glossary.py spoilers/companion.ja.md

# 日本語 HTML および PDF をビルド
python tools/build_ja.py
```

---

## ビルド要件

- **Python 3.10+**
- **Pandoc 3.0+** (`winget install JohnMacFarlane.Pandoc`)
- **Microsoft Edge** または **Google Chrome**（PDF出力用、ヘッドレス印刷機能を使用）

---

## ライセンス・帰属表示 (License & Attribution)

本プロジェクトの本文、画像、およびビルド成果物は、原著と同様に **クリエイティブ・コモンズ 表示 - 継承 4.0 国際 (CC BY-SA 4.0)** の下でライセンスされています。

- **原著者**: David Bau ([davidbau/nethack-companion](https://github.com/davidbau/nethack-companion))
- **日本語翻訳**: nethack-companion-jp プロジェクト
- **NetHack の権利**: NetHack は NetHack DevTeam の著作物であり、NetHack General Public License (NGPL) の下でライセンスされています。

