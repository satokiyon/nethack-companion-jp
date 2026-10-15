<!-- Modified by NetHackJP contributor @satokiyon; latest change date: 2026-10-15. -->
# NetHack Companion JP 開発・翻訳ルール

## 1. 原本セグメント駆動編集の原則
- `spoilers/companion.ja.md`、`spoilers/index.ja.html`、`spoilers/companion.ja.pdf` を直接手動編集してはなりません。
- すべての文章修正・翻訳修正は、大元のセグメントファイル（`docs/segments_ja/step_*.md`）に対して行い、修正後に必ず以下の手順で再生成・ビルドしてください。
  1. `python tools/assemble_companion.py` で `spoilers/companion.ja.md` を再生成。
  2. `python tools/build_ja.py` で HTML (`index.ja.html`) および PDF (`companion.ja.pdf`) をビルド。

## 2. NetHackJP 公式C実装（Single Source of Truth）への準拠
- モンスター名、アイテム名、アーティファクト名、呪文名、役職名、状態異常名などは、独自訳や直訳を用いず、必ず `NetHackJP` リポジトリの公式C実装（`src/obj_jp.c`, `src/mon_jp.c`, `src/spell_jp.c`, `src/botl.c`, `src/role.c` 等）および `docs/glossary_custom.txt` に厳密に準拠してください。
- 用語の変更や新たな定訳を確定した際は、`docs/glossary_custom.txt` にも必ず追記・同期してください。
- ドキュメント側の読みやすさを優先してC実装側と齟齬が生じる場合（例：「魔法のマーカー」等）は、独断で別訳を放置せず、NetHackJPのC実装側（表示名および願いエイリアス）と相互に整合させてください。

## 3. Markdown アンカーIDおよびリンク構造の保全
- 見出しや用語に設定されているアンカー識別子（例: `{#wand-magic-missile}`, `{#orb-of-detection}`）や、リンク（例: `[...](#wand-magic-missile)`）のスラッグは、目次やWeb/PDF連携の互換性を保つため、英語のまま維持してください。修正は日本語の表示テキスト部分のみに限定してください。

## 4. リポジトリ・コミットのクリーンアップ方針
- 監査や一括置換のために作成した作業用スクリプト（例: `tools/check_*.py`, `tools/apply_*.py` 等）は、最終コミット前に必ず削除し、ワーキングツリーを本質的な成果物のみに保ってください。
