#### ゾーン `X` (Xorns `X`) {#xorns-x}

<!-- audit
2026-05-19:
- Xorn stats match monsters.h:2357-2366: speed 9 (NOT fast), 3-claw + bite, MR_FIRE|MR_COLD|MR_STONE.
- Xorns phase through walls via M1_WALLWALK; they do NOT tunnel (no M1_TUNNEL, no rubble left behind).
- Xorn attacks are AD_PHYS only; worn weapons/armor are NOT at risk. Metallivore behavior eats metal off the floor only (monmove.c:1664).
- Xorn corpse grants temporary stone resistance.
-->

D&Dに由来する、土の元素界からやってきた3本腕・3つ目の異形の怪物です。彼らは**固い岩壁をすり抜けて移動**し、突然壁の中から奇襲を仕掛けてきます。金属や宝石を好んで食べます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ゾーン (xorn) | 茶色 | 8 | 9 | -2 | 20 | 爪 1d3 ×3 · 噛みつき 4d6 | 火炎耐性, 冷気耐性, 石化耐性. |

:::
