#### レイス `W` (Wraiths `W`) {#wraiths-w}

<!-- audit
2026-05-19:
- 3 wraith rows at monsters.h: barrow wight 2326, wraith 2336, Nazgul 2343-2353.
- Only plain wraith leaves an eatable corpse; barrow wight and Nazgul carry G_NOCORPSE.
- Wraith corpse grants experience-level gain (eat.c:1141-1142, pluslvl).
- Nazgul AT_BREA/AD_SLEE breath 2d25 sleep (monsters.h Nazgul row); sleep resistance trivializes.
-->

接触によってプレイヤーの経験値レベルを1段階吸い取ります。しかし、倒した後に残る新鮮なレイスの死体を食べれば、逆に経験値レベルが1上昇するという大きな見返りがあります。アンデッド退散や銀の武器が有効です。

すべてのレイスはアンデッドであり、階段の上り下りに追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| バロウ・ワイト (barrow wight) | 灰色 | 3 | 12 | 5 | 5 | 武器攻撃 エナジードレイン-XL · cast spell · 爪 1d4 · 接触 1d4 冷気 | 冷気耐性, 睡眠耐性, 毒耐性. |
| レイス (wraith) | 黒色 | 6 | 12 | 4 | 15 | 接触 1d6 エナジードレイン-XL | 飛行. |
| ナズグル (Nazgul) | 赤紫 | 13 | 12 | 0 | 25 | 武器攻撃 1d4 エナジードレイン-XL · ブレス 2d25 sleep | sees-不可視. |

:::
