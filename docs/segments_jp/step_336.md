#### ミイラ `M` (Mummies `M`)

<!-- audit
2026-05-19:
- Every mummy attack is plain AD_PHYS (monsters.h:1901-1968); mummies do NOT curse worn items (only gremlins have AD_CURS, monattk.h:92).
- All M-class rows carry G_NOCORPSE, which prevents random mummy corpses and tins. The death handler overrides it and creates an already-old corpse of the mummy's base race (mon.c:620-646).
- Mummies are vulnerable to undead-turning.
-->

精神を持たないアンデッド。アンデッド退散の杖や呪文を使うと 1d8 のダメージを受けて逃走します。死亡時には元となった種族の古びた死体を残すため、病気耐性なしで食べると食中毒を起こす危険があります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コボルドのミイラ (kobold mummy) | 茶色 | 3 | 8 | 6 | 20 | 爪 1d4 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old kobold corpse. |
| ノームのミイラ (gnome mummy) | 赤色 | 4 | 10 | 6 | 20 | 爪 1d6 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old gnome corpse. |
| オークのミイラ (orc mummy) | 灰色 | 5 | 10 | 5 | 20 | 爪 1d6 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old orc corpse. |
| ドワーフのミイラ (dwarf mummy) | 赤色 | 5 | 10 | 5 | 20 | 爪 1d6 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old dwarf corpse. |
| エルフのミイラ (elf mummy) | 緑色 | 6 | 12 | 4 | 30 | 爪 2d4 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old elf corpse. |
| 人間のミイラ (human mummy) | 灰色 | 6 | 12 | 4 | 30 | 爪 2d4 ×2 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old 人間 corpse. |
| エティンのミイラ (ettin mummy) | 青色 | 7 | 12 | 4 | 30 | 爪 2d6 ×2 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old ettin corpse. |
| 巨人のミイラ (giant mummy) | 水色 | 8 | 14 | 3 | 30 | 爪 3d4 ×2 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old 巨人 corpse. |

:::
