#### 吸血鬼 `V` (Vampires `V`) {#vampires-v}

<!-- audit
2026-05-19:
- 3 vampire rows at monsters.h: vampire 2282, vampire lord 2292, Vlad 2306.
- Vampire and vampire lord carry G_NOCORPSE, but the death handler substitutes an already-old human corpse. Vlad leaves none (mon.c:613-646).
- All have M1_REGEN | M1_FLY plus M2_STALK (follows stairs) and shapeshift via M2_WERE-equivalent vamp branch (mon.c).
- Vampire mage is #if 0 DEFERRED in 5.0 (correctly omitted).
- Vlad inhabits Vlad's Tower; holds the Candelabrum of Invocation (mkobj.c spawn for PM_VLAD).
-->

アンデッドの貴族。噛みつき攻撃でプレイヤーの経験値レベル（XL）を直接吸い取ります。ヴラドの塔の最上階に君臨するヴラドは、昇天に必要な重要アイテム「燭台」を持っています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 吸血鬼 (vampire) | 赤色 | 10 | 12 | 1 | 25 | 爪 1d6 · 噛みつき 1d6 レベル吸収 | 古い人間の死体を残す。 |
| ヴァンパイアの長 (vampire lord) | 青色 | 12 | 14 | 0 | 50 | 爪 1d8 · 噛みつき 1d8 レベル吸収 | 古い人間の死体を残す。 |
| 吸血鬼ヴラド (Vlad the Impaler) | 赤紫 | 28 | 26 | -6 | 80 | 武器攻撃 2d10 · 噛みつき 1d12 レベル吸収 | ヴラドの塔の吸血鬼ボス。燭台を所持。 |

:::
