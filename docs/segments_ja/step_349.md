#### ゾンビ `Z` (Zombies `Z`)

<!-- audit
2026-05-19:
- All Z-class stats/attacks match monsters.h:2421-2504.
- Race-based zombies carry G_NOCORPSE, but the death handler substitutes an already-old corpse of their base race (mon.c:620-646). Ghouls and skeletons leave none.
- Skeleton has G_NOGEN: never randomly generated, only from Orcus Town or a bone devil's summons.
- M2_UNDEAD is the class flag (NOT "M3_UNDEAD"); M2_STALK is universal across this section.
-->

動きの鈍いアンデッド。距離を取りながら戦えば容易に倒せます。種族ごとのゾンビは元となった種族の古びた死体を残すため、病気耐性なしで食べると食中毒の危険があります。アンデッド退散の杖や呪文を使うと逃走します。ガイコツ（スケルトン）は自然生成されず、オルクスの町やボーンデビルによって召喚されます。

すべてのゾンビは精神を持たず、アンデッドです。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コボルドのゾンビ (kobold zombie) | 茶色 | 0 | 6 | 10 | 0 | 爪 1d4 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old kobold corpse. |
| ノームのゾンビ (gnome zombie) | 茶色 | 1 | 6 | 10 | 0 | 爪 1d5 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old gnome corpse. |
| オークのゾンビ (orc zombie) | 灰色 | 2 | 6 | 9 | 0 | 爪 1d6 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old orc corpse. |
| ドワーフのゾンビ (dwarf zombie) | 赤色 | 2 | 6 | 9 | 0 | 爪 1d6 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old dwarf corpse. |
| エルフのゾンビ (elf zombie) | 緑色 | 3 | 6 | 9 | 0 | 爪 1d7 | follows stairs. Drops an old elf corpse. |
| 人間のゾンビ (human zombie) | 白色 | 4 | 6 | 8 | 0 | 爪 1d8 | follows stairs. Drops an old 人間 corpse. |
| エティンのゾンビ (ettin zombie) | 青色 | 6 | 8 | 6 | 0 | 爪 1d10 ×2 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old ettin corpse. |
| グール (ghoul) | 黒色 | 3 | 6 | 10 | 0 | 爪 1d2 麻痺 · 爪 1d3 | 冷気耐性, 睡眠耐性, 毒耐性. 死体を残さない。 |
| 巨人のゾンビ (giant zombie) | 水色 | 8 | 8 | 6 | 0 | 爪 2d8 ×2 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old 巨人 corpse. |
| 骸骨 (skeleton) | 白色 | 12 | 8 | 4 | 0 | 武器攻撃 2d6 · 接触 1d6 slow | 冷気耐性, 睡眠耐性, 毒耐性, 石化耐性. |

:::
