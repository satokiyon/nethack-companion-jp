# NetHack Companion 本家更新追従・運用手順書

本書は、原著リポジトリ（[davidbau/nethack-companion](https://github.com/davidbau/nethack-companion.git)）で更新（パッチ、内容の改訂、追記等）が行われた際に、日本語版（`nethack-companion-jp`）へ差分を安全に追従・翻訳・反映するための運用手順書です。

---

## 1. 概要と追従の仕組み

本プロジェクトでは、本家リポジトリを Git の `upstream` リモートとして登録しており、以下のツールとファイル構造によって差分をセクション単位で特定します。

- **差分特定ツール**: `tools/check_upstream_diff.py`
- **セグメント管理台帳**: `docs/translation_progress.json`（全セクション・行番号をマッピング）
- **用語集・整合性検証**: `tools/check_glossary.py`
- **原本ファイル**: `spoilers/companion.md`
- **日本語原本**: `spoilers/companion.jp.md`

---

## 2. 定期更新チェック手順

### ステップ 1: upstream の最新情報を取得
PowerShell または Bash で以下を実行します。

```powershell
python tools/check_upstream_diff.py
```

- **差分がない場合**:
  「`✓ 本家 (upstream) との差分はありません。最新状態に追従しています。`」と表示されて終了します。
- **差分がある場合**:
  変更された行番号と、影響を受けるセグメント ID（例: `step_042`）、章・節の名前が出力されます。

---

## 3. 差分翻訳・更新の実行手順

本家で更新が検出された場合、以下の手順で安全に日本語版に反映します。

### ステップ 2: 本家の変更内容を確認する
Git diff コマンドで具体的な変更差分を確認します。

```powershell
git diff HEAD upstream/main -- spoilers/companion.md
```

### ステップ 3: 本家原本（companion.md）を更新する
本家の変更をマージします。

```powershell
git merge upstream/main -m "Sync: 本家の最新コミットを取り込み"
```

### ステップ 4: 対象セグメントのステータスを更新する
`docs/translation_progress.json` を開き、影響を受けたステップの `status` を `"pending"` に変更し、`notes` に本家更新による再翻訳が必要な旨を記載します。

```json
{
  "id": "step_042",
  "status": "pending",
  "notes": "upstream/main 更新追従: モンスター耐性データの変更"
}
```

### ステップ 5: 差分箇所の翻訳とレビュー
1. 用語集（`docs/glossary_references/` および `docs/glossary_custom.txt`）を参照して翻訳。
2. 誤訳・不自然な表現ナレッジ（`docs/translation_review_notes.md`）に違反していないかセルフレビュー。
3. 該当するセグメントファイル（`docs/segments_jp/step_*.md`）を書き換え、`python tools/assemble_companion.py` で `spoilers/companion.jp.md` を再生成します。
   - **アンカーID（`{#xxxxx}`）の保持・自動同期**: 見出しの表示文字列のみを日本語にし、アンカーIDは英語のまま維持します。万一新規見出し等で `{#xxxxx}` を省略しても、`assemble_companion.py` が原著 `spoilers/companion.md` の見出しから英語アンカーIDを自動算出して `step_*.md` と `companion.jp.md` に補完します。

### ステップ 6: 自動品質チェックの実行
修正後、用語集チェック、ASCIIマップチェック、および5重の完全性検証（アンカーID英語化・リンク切れゼロ検証を含む）を実行します。

```powershell
python tools/check_glossary.py spoilers/companion.jp.md
python spoilers/check_ascii_maps.py spoilers/companion.jp.md
python tools/verify_completion.py
```

問題がなければ、`docs/translation_progress.json` の該当ステップを `"reviewed"` に戻します。

---

## 4. ビルドと成果物確認

HTMLおよびPDFを再生成してレイアウトや表示を確認します。

```powershell
powershell -ExecutionPolicy Bypass -File spoilers/build.jp.ps1
```

- 生成された `spoilers/index.jp.html` をブラウザで開き、目次リンクやテーブル崩れがないか確認。
- PDF（`spoilers/companion.jp.pdf`）の組版を確認。

---

## 5. コミットとプッシュ

```powershell
git add docs/segments_jp/ spoilers/companion.jp.md spoilers/index.jp.html spoilers/companion.jp.pdf docs/translation_progress.json
git commit -m "docs: 本家 upstream の更新を追従翻訳 (step_042)"
```

