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

成体のドラゴンは各自の属性に応じた強烈なブレスを直線状に吐き出します。反射（Reflection）能力があれば、遠距離ブレスを跳ね返して逆に大ダメージを与えられます。**幼体（子ドラゴン）はブレスを吐きません**。

*クロマティック・ドラゴン (Chromatic Dragon)* を除き、すべてのドラゴンは飛行能力を持ちます。

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
| 灰色ドラゴン (gray dragon) | 灰色 | 15 | 9 | -1 | 20 | ブレス 4d6 魔法 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Anti-magic breath. Magic resistance helps; reflection doesn't. |
| 金色ドラゴン (gold dragon) | 黄色 | 15 | 9 | -1 | 20 | ブレス 4d6 火炎 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Fire breath. Drops gold-colored scales (light source). |
| 銀色ドラゴン (silver dragon) | 明水 | 15 | 9 | -1 | 20 | ブレス 4d6 冷気 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cold breath plus reflection scales: your reflection target. |
| 赤色ドラゴン (red dragon) | 赤色 | 15 | 9 | -1 | 20 | ブレス 6d6 火炎 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cone of fire. Get fire resistance before you meet one. |
| 白ドラゴン (white dragon) | 白色 | 15 | 9 | -1 | 20 | ブレス 4d6 冷気 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cone of cold. Cold resistance. |
| オレンジドラゴン (orange dragon) | 橙色 | 15 | 9 | -1 | 20 | ブレス 4d25 sleep · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Sleep ray. Sleep resistance trivialises. |
| 黒ドラゴン (black dragon) | 黒色 | 15 | 9 | -1 | 20 | ブレス 1d255 分解 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Disintegration breath. Disint resistance OR reflection. |
| 青ドラゴン (blue dragon) | 青色 | 15 | 9 | -1 | 20 | ブレス 4d6 電撃 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cone of lightning. Shock resistance. |
| 緑ドラゴン (green dragon) | 緑色 | 15 | 9 | -1 | 20 | ブレス 4d6 毒 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視, 死体に毒あり. Poison breath; poison resistance is enough. |
| 黄色ドラゴン (yellow dragon) | 黄色 | 15 | 9 | -1 | 20 | ブレス 4d6 酸 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Acid breath. |
| クロマティック・ドラゴン (Chromatic Dragon) | 赤紫 | 16 | 12 | 0 | 30 | ブレス 6d6 rnd-ブレス · cast spell · 爪 2d8 盗み-amulet · 噛みつき 4d8 ×2 · 毒針 1d6 | sees-不可視, 死体に毒あり, follows stairs. |
| イクソス (Ixoth) | 赤色 | 15 | 12 | -1 | 20 | ブレス 8d6 火炎 · 噛みつき 4d8 · cast spell · 爪 2d4 · 爪 2d4 盗み-amulet | sees-不可視, follows stairs. |

:::
