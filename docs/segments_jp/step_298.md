### モンスター図鑑一覧表 (Bestiary Tables) {#bestiary-tables}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 monsters.h: no corrections. ~100% of the numeric columns (Lvl/Spd/AC/MR), color, and full attack lists verified across all ~55 tables, including the tricky cases (floating eye 0d70, black dragon disint, AD_DRST-as-poison stings, deferred/#if0 monsters correctly excluded).
-->

ダンジョンで遭遇しうるあらゆるモンスターをマップ記号ごとに分類した一覧です。**レベル (Lvl)**はモンスターの基本レベル、**速度 (Spd)**は移動速度（プレイヤーの標準速度は 12）、**AC**はアーマークラス（低いほど強固）、**MR**は魔法防御率（プレイヤーの呪文や魔法攻撃に抵抗する確率%）を表します。**攻撃方法 (Attacks)**は各攻撃の種別、ダメージダイス、追加効果を記載しており、`·` で区切られた攻撃は1ターン内にすべて連続して繰り出されます。**備考 (Notes)**には飛行能力、不可視視認、自動回復、死体に毒があるかなど、戦闘を一変させる重要な特性をまとめています。
