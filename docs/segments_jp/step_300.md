#### ブロッブ `b` (Blobs `b`) {#blobs-b}

<!-- audit
2026-05-19:
- 3 rows (S_BLOB) sourced from monsters.h:137-166.
- Acid blob passive: 50% splash + 1/30 corrode armor, plus passive_obj 1/6 erode on uwep/uarmg (uhitm.c:5906-5933).
- Gelatinous cube paralysis: 2/3 rate, free-action blocks (uhitm.c:6019-6064).
- Gelatinous cube in 5.0 is AT_TUCH only, NOT AT_ENGL like older versions. (monsters.h:157-158 AT_TUCH AD_PLYS 2d4 + AT_NONE AD_PLYS 1d4)
-->

動きが遅く、精神を持ちません。酸のブロッブを素手や大切な金属武器で近接攻撃してはいけません。相手の酸による反撃で武器や防具が腐食します。ゼラチンキューブは接触時にプレイヤーを麻痺させます。

すべてのブロッブは精神を持たず（マインドレス）、睡眠耐性と毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 酸のブロッブ (acid blob) | 緑色 | 1 | 3 | 8 | 0 | 反撃 1d8 酸 | 不定形、酸耐性、石化耐性。酸の反撃ダメージ。素手で殴ると手袋が腐食する。 |
| 震えるブロッブ (quivering blob) | 白色 | 5 | 1 | 8 | 0 | 接触 1d8 |  |
| ゼラチンキューブ (gelatinous cube) | 水色 | 6 | 6 | 8 | 0 | 接触 2d4 麻痺 · 反撃 1d4 麻痺 | 火炎耐性、冷気耐性、電撃耐性、酸耐性、石化耐性。鈍足だが接触時に麻痺。自由行動なしでの近接戦は厳禁。 |

:::
