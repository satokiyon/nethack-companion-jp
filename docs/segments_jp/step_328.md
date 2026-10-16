#### ドラゴン `D` (Dragons `D`) {#dragons-d}

<!-- audit
2026-05-19:
- 10 baby + 10 adult + Chromatic + Ixoth sourced from monsters.h:1325-1562; Ixoth at monsters.h:3642-3690.
- Shimmering dragon is `#if 0 DEFERRED`, NOT in 5.0 (monsters.h:1365-1374 baby and 1466-1482 adult shimmering dragon blocks are inside `#if 0 /* DEFERRED */`).
- Silver dragon color is CLR_BRIGHT_CYAN (color.h:54), NOT gray, for both baby and adult.
- Baby blue dragon has only bite 2d6; NO breath weapon (monsters.h:1408-1415, no AT_BREA). Babies don't breathe.
- Black dragon breath is AD_DISN 1d255 (instakill without reflection or disint-res), monsters.h:1494.
- Chromatic random-breath AT_BREA/AD_RBRE selects breath type per zap (mhitu.c).
-->

ダンジョン屈指の巨獣。属性に応じた強力なブレスを放ちます。倒して得られるドラゴンの死体や鱗からは、最高の防御性能と耐性を誇る「ドラゴンの鱗鎧」を作ることができます。

すべてのドラゴンは飛行能力と不可視視認能力を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 灰色ドラゴンの子供 (baby gray dragon) | 灰色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 金色ドラゴンの子供 (baby gold dragon) | 黄色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 銀色ドラゴンの幼体 (baby silver dragon) | 明水 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 赤色ドラゴンの子供 (baby red dragon) | 赤色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 白ドラゴンの子供 (baby white dragon) | 白色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| オレンジドラゴンの子供 (baby orange dragon) | 橙色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 黒ドラゴンの子供 (baby black dragon) | 黒色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 青ドラゴンの子供 (baby blue dragon) | 青色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 緑ドラゴンの子供 (baby green dragon) | 緑色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 | 死体に毒あり. |
| 黄色ドラゴンの子供 (baby yellow dragon) | 黄色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 灰色ドラゴン (gray dragon) | 灰色 | 15 | 9 | -1 | 20 | ブレス 4d6 魔法 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。反魔法ブレス。魔法防御が有効、反射は無効。 |
| 金色ドラゴン (gold dragon) | 黄色 | 15 | 9 | -1 | 20 | ブレス 4d6 火炎 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。火炎ブレス。金色の鱗（光源）をドロップ。 |
| 銀色ドラゴン (silver dragon) | 明水 | 15 | 9 | -1 | 20 | ブレス 4d6 冷気 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。冷気ブレス。反射の鱗を落とすため反射能力の獲得標的となる。 |
| 赤色ドラゴン (red dragon) | 赤色 | 15 | 9 | -1 | 20 | ブレス 6d6 火炎 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。火炎ブレス。遭遇する前に火炎耐性を得ておくこと。 |
| 白ドラゴン (white dragon) | 白色 | 15 | 9 | -1 | 20 | ブレス 4d6 冷気 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。冷気ブレス。冷気耐性で対処。 |
| オレンジドラゴン (orange dragon) | 橙色 | 15 | 9 | -1 | 20 | ブレス 4d25 sleep · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。睡眠光線。睡眠耐性があれば無力化できる。 |
| 黒ドラゴン (black dragon) | 黒色 | 15 | 9 | -1 | 20 | ブレス 1d255 分解 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。分解ブレス。分解耐性または反射が必須。 |
| 青ドラゴン (blue dragon) | 青色 | 15 | 9 | -1 | 20 | ブレス 4d6 電撃 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。電撃ブレス。電撃耐性で対処。 |
| 緑ドラゴン (green dragon) | 緑色 | 15 | 9 | -1 | 20 | ブレス 4d6 毒 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認、死体に毒あり。毒ブレス。毒耐性があれば十分。 |
| 黄色ドラゴン (yellow dragon) | 黄色 | 15 | 9 | -1 | 20 | ブレス 4d6 酸 · 噛みつき 3d8 · 爪 1d4 ×2 | 不可視視認。酸のブレス。 |
| クロマティック・ドラゴン (Chromatic Dragon) | 赤紫 | 16 | 12 | 0 | 30 | ブレス 6d6 rnd-ブレス · 攻撃呪文 · 爪 2d8 盗み-魔除け · 噛みつき 4d8 ×2 · 毒針 1d6 | 不可視視認、死体に毒あり、階段を追跡. |
| イクソス (Ixoth) | 赤色 | 15 | 12 | -1 | 20 | ブレス 8d6 火炎 · 噛みつき 4d8 · 攻撃呪文 · 爪 2d4 · 爪 2d4 盗み-魔除け | 不可視視認、階段を追跡. |

:::
