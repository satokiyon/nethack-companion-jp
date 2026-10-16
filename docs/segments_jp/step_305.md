#### グレムリン `g` (Gremlins `g`)

<!-- audit
2026-05-19:
- 3 rows (gremlin/gargoyle/winged gargoyle) sourced from monsters.h:448-473.
- Gremlin water/fountain trigger SPLIT: clones themselves, 2/3 chance per step (mon.c:987-992); does NOT touch your intrinsics.
- Gremlin night attack is AD_CURS: strips one random intrinsic, 1/10 per hit, night-only, blocked by cancellation (uhitm.c:3040-3057, sit.c:644+).
- Gargoyles do NOT petrify by touch or corpse: touch_petrifies is cockatrice/chickatrice only (mondata.h:200-201).
-->

夜間（または光源がない暗闇）に水に触れると分裂増殖する厄介な小型怪物です。暗闇の中でプレイヤーから内在能力を盗み取る攻撃を行います。明るい光源を持ち歩くか、光の巻物・呪文で部屋を照らすのが有効な対抗策です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| グレムリン (gremlin) | 緑色 | 5 | 12 | 2 | 25 | 爪 1d6 ×2 · 噛みつき 1d4 · 爪 呪い | 遊泳, 死体に毒あり, follows stairs, 毒耐性. |
| ガーゴイル (gargoyle) | 茶色 | 6 | 10 | -4 | 0 | 爪 2d6 ×2 · 噛みつき 2d4 | 石化耐性. |
| 羽のあるガーゴイル (winged gargoyle) | 赤紫 | 9 | 15 | -2 | 0 | 爪 3d6 ×2 · 噛みつき 3d4 | 飛行, 石化耐性. |

:::
