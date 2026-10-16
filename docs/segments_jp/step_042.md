#### ローグ階層 (The Rogue Level) {#the-rogue-level}
<!-- audit
2026-05-18:
- Rogue Level appears DL 15-18 per base=15 range=4 (dungeon.lua:54-58)
- welcome message "older, more primitive world" (do.c:1913)
- uppercase-only monsters via Is_rogue_level (makemon.c:1672)
- symbol swaps: armor `]`, amulet `,`, food `:`, gold same as gems (drawing.c:73-79)
- doors forced D_NODOOR — no closed doors (mklev.c:647-648)
- no fountains/sinks/altars/shops/graves via skip_nonrogue (mklev.c:988-989)
- rogueprobs item pool: weapon/armor/food/potion/scroll/wand/ring only — no spellbooks/tools/amulets/gems/coins (mkobj.c:58-64)
- tile mode disabled in Qt, X11, win32, curses ports (win/X11/winmap.c:1009, win/Qt/qt_map.cpp:145, 228)
- engraving has no rogue-level guard — Elbereth works as usual (engrave.c)
-->

ダンジョン中層のどこかで、1フロア限りの歴史保存地区に迷い込むことになります。
*「あなたはより古く、より原始的な世界に入り込んだようだ。(You enter what seems to be an older, more primitive world.)」*
このエリアは、ダンジョン探索ゲームといえば誰もが **『Rogue』** のことしか知らなかった古き良き時代の姿のまま残されており、いくつかの特徴がその時代を物語っています：

- 出現する生物（モンスター）の記号はすべて英大文字です：小文字の種族はまだ発明されていませんでした。
- 防具は `]`、食料は `:`、魔除けは `,` で表示され、ゴールドは宝石と同じ記号を共有します（当時のRogueでは同じ扱いでした）。
- 扉は閉まりません。蝶番の概念は後から導入されたものです。
- タイル表示モードは自動的に無効化され、飾り気のないプレーンなASCII文字表示へと切り替わります。
- 泉、流し台、祭壇、店主、司祭は一切存在せず、フロアに自然生成されるアイテムからも魔法書、道具、魔除けが排除されています。これらはすべてRogue以降に考案された要素だからです。

ただし、プレイヤー側の現代的な技術は依然として機能します。ハック（Hack）時代に追加された [エルベレス (Elbereth)](#elbereth) の文字をここに刻むことも可能です。ささやかな時代錯誤（アナクロニズム）と言えるでしょう。
