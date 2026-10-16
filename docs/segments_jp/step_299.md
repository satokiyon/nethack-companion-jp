#### 蟻および昆虫 `a` (Ants and insects `a`) {#ants-and-insects-a}

<!-- audit
2026-05-19:
- 6 rows (S_ANT) sourced from monsters.h:89-133.
- giant ant L2/Spd18/AC3 bite 1d4 (monsters.h:89-95).
- killer bee L1/Spd18/AC-1 sting 1d3 AD_DRST, G_LGROUP, MR_POISON (monsters.h:96-102).
- soldier ant L3/Spd18/AC3 bite 2d4 + sting 3d4 AD_DRST, M1_POIS (monsters.h:103-110).
- fire ant L3/Spd18/AC3 bite 2d4 phys + 2d4 fire, MR_FIRE (monsters.h:111-118).
- giant beetle L5/Spd6/AC4 bite 3d6, M1_POIS, MR_POISON (monsters.h:119-125).
- queen bee L9/Spd24/AC-4 sting 1d8 AD_DRST, G_NOGEN, M2_FEMALE|M2_PRINCE (monsters.h:126-133).
- Killer/soldier/queen stings are AD_DRST (Str-drain, poison-family); shown as "poison" for beginner voice.
- Killer bee is G_LGROUP; others are smaller groups.
-->

昆虫類。多くは集団で群れをなして出現します。兵隊蟻の毒針攻撃は筋力を吸い取ります。殺人蜂は大群で襲いかかり、蜂の巣の部屋にいる女王蜂は単体でも手ごわい相手です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 巨大蟻 (giant ant) | 茶色 | 2 | 18 | 3 | 0 | 噛みつき 1d4 |  |
| 殺人蜂 (killer bee) | 黄色 | 1 | 18 | -1 | 0 | 毒針 1d3 毒 | 飛行、死体に毒あり、毒耐性。毒針攻撃。 |
| 兵隊蟻 (soldier ant) | 青色 | 3 | 18 | 3 | 0 | 噛みつき 2d4 · 毒針 3d4 毒 | 死体に毒あり、毒耐性。毒針攻撃。 |
| 火蟻 (fire ant) | 赤色 | 3 | 18 | 3 | 10 | 噛みつき 2d4 · 噛みつき 2d4 火炎 | 火炎耐性. |
| 巨大カブト虫 (giant beetle) | 黒色 | 5 | 6 | 4 | 0 | 噛みつき 3d6 | 死体に毒あり、毒耐性. |
| 女王蜂 (queen bee) | 赤紫 | 9 | 24 | -4 | 0 | 毒針 1d8 毒 | 飛行、死体に毒あり、毒耐性. |

:::
