#### ゴーレム `'` (Golems `'`) {#golems}

<!-- audit
2026-05-19:
- 11 golem rows at monsters.h:2509-2594 (straw 2509, paper, rope, gold, leather, wood, flesh, clay, stone, glass, iron 2587).
- Iron golem has G_NOCORPSE (monsters.h:2587); it leaves NO corpse, NOT a poisonous one.
- poly_when_stoned (mondata.c:80-85) covers ALL golems except stone golem.
- Iron golem AT_BREA/AD_DRST 4d6 poison breath at monsters.h:2592 — poison resistance critical.
- Clay golem inscription "ATHEIST" wears off via shatter_floor message; clay golem corpse grants nothing on eat.
-->

魔法で命を吹き込まれた人造人間です。藁、肉、土、石、鉄など様々な素材で作られ、素材に応じた耐性を持ちます。死体を残さず、鉄のゴーレムは強打を放ちます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 藁のゴーレム (straw golem) | 黄色 | 3 | 12 | 10 | 0 | 爪 1d2 ×2 | 冷気耐性. |
| 紙のゴーレム (paper golem) | 白色 | 3 | 12 | 10 | 0 | 爪 1d3 | 冷気耐性. |
| 紐のゴーレム (rope golem) | 茶色 | 4 | 9 | 8 | 0 | 爪 1d4 ×2 · 締め付け 6d1 |  |
| 金のゴーレム (gold golem) | 黄色 | 5 | 9 | 6 | 0 | 爪 2d3 ×2 | 酸耐性. |
| 皮のゴーレム (leather golem) | 茶色 | 6 | 6 | 6 | 0 | 爪 1d6 ×2 |  |
| 木のゴーレム (wood golem) | 茶色 | 7 | 3 | 4 | 0 | 爪 3d4 | 冷気耐性. |
| 肉のゴーレム (flesh golem) | 赤色 | 9 | 8 | 9 | 30 | 爪 2d8 ×2 | 火炎耐性、冷気耐性、電撃耐性. |
| 土のゴーレム (clay golem) | 茶色 | 11 | 7 | 7 | 40 | 爪 3d10 |  |
| 岩のゴーレム (stone golem) | 灰色 | 14 | 6 | 5 | 50 | 爪 3d8 | 石化耐性. |
| ガラスのゴーレム (glass golem) | 水色 | 16 | 6 | 1 | 50 | 爪 2d8 ×2 | 酸耐性. |
| 鉄のゴーレム (iron golem) | 水色 | 18 | 6 | 3 | 60 | 武器攻撃 4d10 · ブレス 4d6 毒 | 死体を残さない。火炎耐性、冷気耐性、電撃耐性. |

:::
