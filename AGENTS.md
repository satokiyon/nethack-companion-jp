<!-- Modified by NetHackJP contributor @satokiyon; latest change date: 2026-10-17. -->
# NetHack Companion JP 開発・翻訳ルール

## 1. 原本セグメント駆動編集の原則
- `spoilers/companion.jp.md`、`spoilers/index.jp.html`、`spoilers/companion.jp.pdf` を直接手動編集してはなりません。
- すべての文章修正・翻訳修正は、大元のセグメントファイル（`docs/segments_jp/step_*.md`）に対して行い、修正後に必ず以下の手順で再生成・ビルドしてください。
  1. `python tools/assemble_companion.py` で `spoilers/companion.jp.md` を再生成（原著 `companion.md` からの見出し英語アンカーID自動同期を含む）。
  2. `python tools/build_jp.py` で HTML (`index.jp.html`) および PDF (`companion.jp.pdf`) をビルド。
  3. `python tools/verify_completion.py` で5重の完全性検証（セグメント整合・定訳準拠・見出し構造・ASCIIマップ・英語アンカー＆リンク切れゼロ）を実行。

## 2. NetHackJP 公式C実装（Single Source of Truth）への準拠
- モンスター名、アイテム名、アーティファクト名、呪文名、役職名、状態異常名などは、独自訳や直訳を用いず、必ず `NetHackJP` リポジトリの公式C実装（`src/obj_jp.c`, `src/mon_jp.c`, `src/spell_jp.c`, `src/botl.c`, `src/role.c` 等）および `docs/glossary_custom.txt` に厳密に準拠してください。
- 用語の変更や新たな定訳を確定した際は、`docs/glossary_custom.txt` にも必ず追記・同期してください。
- ドキュメント側の読みやすさを優先してC実装側と齟齬が生じる場合（例：「魔法のマーカー」等）は、独断で別訳を放置せず、NetHackJPのC実装側（表示名および願いエイリアス）と相互に整合させてください。

## 3. Markdown アンカーIDおよびリンク構造の保全
- アンカー（`#xxxxx`）には日本語（非ASCII文字）を一切混ぜず、日本語にするのは画面に表示される文字列のみに限定してください。
- 原著 `spoilers/companion.md` で `{#...}` が省略されている見出しであっても、日本語版（`docs/segments_jp/step_*.md` および `spoilers/companion.jp.md`）の全見出し（H1〜H6）には、原著から Pandoc が生成する英語アンカーIDと完全一致する `{#english-slug}` を必ず明示してください（同名見出しの `-1` 連番や `5.0` のドット保持を含む）。
- 見出しに既存の属性ブロック（例: `{.sokoban-level data-width=14 data-height=13}`）がある場合は、`{...}` を2つ並べず `{#level-1-version-a .sokoban-level data-width=14 data-height=13}` のように単一ブロック内に統合してください。
- 本文中のインラインアンカー（例: `**[サンソード]{#sunsword}**`）や内部リンク（例: `[...](#wand-magic-missile)`）も欠落させることなく英語スラッグを完全保持してください。

## 4. リポジトリ・コミットのクリーンアップ方針
- 監査や一括置換のために作成した作業用スクリプト（例: `tools/check_*.py`, `tools/apply_*.py` 等）は、最終コミット前に必ず削除し、ワーキングツリーを本質的な成果物のみに保ってください。

<!-- agent-ninja-START -->
## Agent Skills

> **IMPORTANT**: Prefer skill-led reasoning over pre-training-led reasoning.
> See [Agent Skills](.github/skills/README.md) before working on tasks covered by these skills.

<!-- agent-ninja-END -->
