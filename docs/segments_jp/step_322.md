#### その他原生生物 `x` (Xan and miscellaneous `x`) {#xans-and-fantastic-insects-x}

<!-- audit
2026-05-19:
- Grid bug row at monsters.h:1149-1156; xan row at monsters.h:1157-1164.
- Grid bug AT_BITE/AD_ELEC 1d1; xan AT_STNG/AD_LEGS 1d4, M1_FLY plus M1_POIS (poisonous corpse).
- Xan AD_LEGS / Wounded_legs reduces carry capacity (hack.c:4331-4336) and abuses Dex (attrib.c:472, 581); it does NOT slow movement.
-->

ザンやジャガーノートなど、分類不能な異形の生物群です。ザンの刺突は傷口を化膿させて手足を麻痺させます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| グリッドバグ (grid bug) | 赤紫 | 0 | 12 | 9 | 0 | 噛みつき 1d1 電撃 | 電撃耐性. |
| ザン (xan) | 赤色 | 7 | 18 | -4 | 0 | 毒針 1d4 leg-wound | 飛行、死体に毒あり. |

:::
