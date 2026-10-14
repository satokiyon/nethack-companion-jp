# 翻訳品質レビュー ナレッジベース（translation_review_notes.md）

本書は、NetHackスポイラー書籍『A Traveler's Companion to the Mazes of Menace』の日本語翻訳において検出された誤訳、不自然な言い回し、注意すべき表現パターンを蓄積し、各ステップの翻訳およびレビューで再発を防止するためのナレッジベースです。

---

## 1. AI翻訳に共通する注意・是正パターン

| 分類 | 英語表現 / 原文 | 避けるべき不自然な訳（誤訳・悪文） | 推奨される自然な訳 | 理由・備考 |
| :--- | :--- | :--- | :--- | :--- |
| **モンスター** | Floating eye | 「浮遊する目」 | 「さまよう目」 | `mon_jp.txt` / NetHackJP の公式定訳。 |
| **モンスター** | Water nymph | 「水の精」 | 「水のニンフ」 | `mon_jp.txt` / NetHackJP の公式定訳。 |
| **モンスター** | Pony / Warhorse | 「子馬」「軍馬」 | 「仔馬」「戦闘用の馬」 | `mon_jp.txt` / NetHackJP の公式定訳。 |
| **モンスター** | Kitten | 「子猫」 | 「小猫」 | `mon_jp.txt` / NetHackJP の公式定訳。 |
| **役職 (Role)** | Barbarian | 「バーバリアン」 | 「野蛮人」 | NetHackJP `role.c` / `mon_jp.c` の公式表示名。 |
| **役職 (Role)** | Healer | 「治療者」 | 「治療師」 | NetHackJP `role.c` / `mon_jp.c` の公式表示名。 |
| **役職 (Role)** | Monk | 「修道士」 | 「武闘家」 | NetHackJP `role.c` / `mon_jp.c` の公式表示名。 |
| **役職 (Role)** | Priest | 「僧侶」 | 「司祭」 | NetHackJP `role.c` / `mon_jp.c` の公式表示名。 |
| **アイテム** | Touchstone | 「砥石」 | 「試金石」 | `obj_jp.txt` / NetHackJP の公式定訳。砥石は whetstone。 |
| **アイテム** | Bullwhip | 「革鞭」 | 「鞭」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Fedora | 「フェドーラ帽」 | 「フィドーラ」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Tinning kit | 「缶詰作成キット」 | 「缶詰作成道具」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Lock pick | 「鍵開け道具」 | 「鍵開け器具」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Cloak of displacement | 「変位のクローク」 | 「幻影のクローク」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Cloak of magic resistance | 「魔法耐性のクローク」 | 「魔法を防ぐクローク」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Ring mail / Splint mail | 「リングメイル」「短冊鎧」 | 「鉄環の鎧」「鉄片の鎧」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Quarterstaff / Flint | 「クオータースタッフ」「火打石」 | 「六尺棒」「火打ち石」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Wand of sleep | 「睡眠の杖」 | 「眠りの杖」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Scroll of magic mapping | 「魔法の地図の巻物」 | 「地図の巻物」 | `obj_jp.txt` / NetHackJP の公式定訳。 |
| **アイテム** | Carrot | 「ニンジン」「人参」 | 「にんじん」 | `obj_jp.txt` / NetHackJP の公式定訳（平仮名）。 |
| **呪文 (Spell)** | force bolt | 「力づくのボルト」 | 「衝撃」 | `spell_jp.c` / NetHackJP の公式定訳。 |
| **呪文 (Spell)** | magic mapping | 「魔法の地図」 | 「地図化」 | `spell_jp.c` / NetHackJP の公式定訳。 |
| **施設・地形** | fountain | 「噴水」 | 「泉」 | `src/fountain.c` / NetHackJP の公式定訳。 |
| **状態・負荷** | burdened | 「負担」 | 「重荷」 | `src/botl.c` / NetHackJP の公式ステータス表示。 |
| **状態・空腹** | fainting / fainted | 「気絶寸前」「気絶」 | 「失神寸前」「失神」 | `src/botl.c` / NetHackJP の公式ステータス表示。 |
| **指示代名詞・文体** | "You will want to..." | 「あなたは〜したいと思うでしょう」 | 「〜するとよい」「〜すべきである」 | 日本語の攻略・解説文として自然な助言調にする。二人称「あなた」の連呼を避ける。 |
| **文体** | "Make sure to..." | 「あなたが確実に〜することを確認してください」 | 「必ず〜すること」「忘れずに〜しよう」 | 冗長な直訳を避け、簡潔明瞭にする。 |
| **ゲーム用語** | "intrinsic" / "extrinsic" | 「本質的」「外在的」 | 「内在能力」「外在能力（装備・アイテムによる能力）」 | NetHackの定訳。耐性や能力の属性。 |
| **ゲーム用語** | "pet" | 「ペット」 | 「ペット（同伴モンスター）」 | 基本は「ペット」で良いが、文脈に応じて「同伴モンスター」等。 |
| **ゲーム用語** | "engrave" | 「彫る」「刻印する」 | 「（文字・Elberethを）刻む / 彫る」 | 床に文字を指や杖・ダガーで書く行為。 |
| **状態異常** | "burdened" / "stressed" | 「負担がかかった」「ストレスを受けた」 | 「負担(burdened)」「重荷(stressed)」 | ゲーム内の明示的ステータス表示に対応。 |
| **呪詛** | "blessed" / "uncursed" / "cursed" | 「祝福の」「非呪の」「呪われた」 | 「祝福された」「無呪の」「呪われた」 | JNetHack標準の「無呪（むじゅ）」を使用。 |
| **判定** | "save vs death" | 「死に対するセーブ」 | 「即死耐性判定 / 対死判定」 | TRPG・ローグライク用語。 |
| **施設** | "altar" / "temple" | 「祭壇」「寺院」 | 「祭壇」「神殿 / 寺院」 | 聖職者（僧侶）や神に関する施設。 |
| **操作** | "hit 'y'" | 「'y'を打つ」 | 「'y' を押す / 入力する」 | キー入力の自然な表現。 |
| **Markdown構造** | 表中の改行やパイプ | `\|` の欠落や不要なエスケープ | パイプ `\|` を正しく保持 | テーブル構造の崩壊防止。 |
| **コードブロック** | ASCIIマップ / コマンド | 半角空白の除去・インデント崩れ | 等幅フォント・スペースを完全保持 | ダンジョンマップの崩れ防止。 |

---

## 2. 蓄積されたレビュー検出事項と改善履歴
※各ステップの翻訳レビューで新たに検出された誤訳や改善表現を随時ここに追加・記録します。

### ステップ別記録
（自律実行中に検出された事項をここに随時追記）


- **固有名詞と役職**: `Rogue` → `『Rogue』または「盗賊」` (ゲーム名の場合は『Rogue』、プレイヤー役職の場合は「盗賊 (Rogue)」と訳し分ける)