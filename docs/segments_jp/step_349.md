#### ゾンビおよび骸骨 `Z` (Zombies and skeletons `Z`) {#zombies-z}

<!-- audit
2026-05-19:
- All Z-class stats/attacks match monsters.h:2421-2504.
- Race-based zombies carry G_NOCORPSE, but the death handler substitutes an already-old corpse of their base race (mon.c:620-646). Ghouls and skeletons leave none.
- Skeleton has G_NOGEN: never randomly generated, only from Orcus Town or a bone devil's summons.
- M2_UNDEAD is the class flag (NOT "M3_UNDEAD"); M2_STALK is universal across this section.
-->

死霊術によって動かされるアンデッドです。動きは遅いですが、元となった種族の死体を残すため食中毒に注意してください。骸骨は武器を持って攻撃してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コボルドのゾンビ (kobold zombie) | 茶色 | 0 | 6 | 10 | 0 | 爪 1d4 | 階段を追跡、冷気耐性、睡眠耐性、毒耐性。古いコボルドの死体を残す。 |
| ノームのゾンビ (gnome zombie) | 茶色 | 1 | 6 | 10 | 0 | 爪 1d5 | 階段を追跡、冷気耐性、睡眠耐性、毒耐性。古いノームの死体を残す。 |
| オークのゾンビ (orc zombie) | 灰色 | 2 | 6 | 9 | 0 | 爪 1d6 | 階段を追跡、冷気耐性、睡眠耐性、毒耐性。古いオークの死体を残す。 |
| ドワーフのゾンビ (dwarf zombie) | 赤色 | 2 | 6 | 9 | 0 | 爪 1d6 | 階段を追跡、冷気耐性、睡眠耐性、毒耐性。古いドワーフの死体を残す。 |
| エルフのゾンビ (elf zombie) | 緑色 | 3 | 6 | 9 | 0 | 爪 1d7 | 階段を追跡。古いエルフの死体を残す。 |
| 人間のゾンビ (human zombie) | 白色 | 4 | 6 | 8 | 0 | 爪 1d8 | 階段を追跡。古い人間の死体を残す。 |
| エティンのゾンビ (ettin zombie) | 青色 | 6 | 8 | 6 | 0 | 爪 1d10 ×2 | 階段を追跡、冷気耐性、睡眠耐性、毒耐性。古いエティンの死体を残す。 |
| グール (ghoul) | 黒色 | 3 | 6 | 10 | 0 | 爪 1d2 麻痺 · 爪 1d3 | 冷気耐性、睡眠耐性、毒耐性。死体を残さない。 |
| 巨人のゾンビ (giant zombie) | 水色 | 8 | 8 | 6 | 0 | 爪 2d8 ×2 | 階段を追跡、冷気耐性、睡眠耐性、毒耐性。古い巨人の死体を残す。 |
| 骸骨 (skeleton) | 白色 | 12 | 8 | 4 | 0 | 武器攻撃 2d6 · 接触 1d6 減速 | 冷気耐性、睡眠耐性、毒耐性、石化耐性. |

:::
