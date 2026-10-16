#### レイス `W` (Wraiths `W`) {#wraiths-w}

<!-- audit
2026-05-19:
- 3 wraith rows at monsters.h: barrow wight 2326, wraith 2336, Nazgul 2343-2353.
- Only plain wraith leaves an eatable corpse; barrow wight and Nazgul carry G_NOCORPSE.
- Wraith corpse grants experience-level gain (eat.c:1141-1142, pluslvl).
- Nazgul AT_BREA/AD_SLEE breath 2d25 sleep (monsters.h Nazgul row); sleep resistance trivializes.
-->

実体を持たない亡霊アンデッドです。攻撃でレベルを吸い取ってきますが、死体を食べると確実に経験値レベルが1上昇するため、プレイヤーにとって最も歓迎されるモンスターの一つです。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| バロウ・ワイト (barrow wight) | 灰色 | 3 | 12 | 5 | 5 | 武器攻撃 レベル吸収 · 攻撃呪文 · 爪 1d4 · 接触 1d4 冷気 | 冷気耐性、睡眠耐性、毒耐性. |
| レイス (wraith) | 黒色 | 6 | 12 | 4 | 15 | 接触 1d6 レベル吸収 | 飛行. |
| ナズグル (Nazgul) | 赤紫 | 13 | 12 | 0 | 25 | 武器攻撃 1d4 レベル吸収 · ブレス 2d25 sleep | 不可視視認. |

:::
