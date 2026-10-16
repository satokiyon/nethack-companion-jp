#### トカゲ類 `:` (Lizards `:`): {#lizards}

<!-- audit
2026-05-19:
- 8 lizard rows at monsters.h:3260-3324 (newt 3260, gecko, iguana, baby croc, lizard, chameleon, croc, salamander 3317).
- Lizard corpse cures stoning (eat.c:827-830, fix_petrification) and never rots (eat.c:1483, 1510).
- Newt corpse occasionally restores 1-3 Pw via eye_of_newt_buzz (eat.c:1102-1123).
- Chameleon is M2_SHAPESHIFTER (monsters.h:3299, sets shifter via newcham).
- Salamander has 4-attack chain at monsters.h:3317-3324: weapon 2d8, touch 1d6 fire, hug 2d6, hug 3d6 fire.
- Salamander is G_HELL (Gehennom-only spawn flag).
-->

ヤモリ、カメレオン、ワニ、サラマンダーなど。通常のトカゲ（Lizard）の死体は決して腐敗せず、食べると石化の進行を即座に中断させることができるため、全プレイヤー必携の救命アイテムです。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| イモリ (newt) | 黄色 | 0 | 6 | 8 | 0 | 噛みつき 1d2 | 遊泳、水陸両用. |
| ヤモリ (gecko) | 緑色 | 1 | 6 | 8 | 0 | 噛みつき 1d3 |  |
| イグアナ (iguana) | 茶色 | 2 | 6 | 7 | 0 | 噛みつき 1d4 |  |
| ワニの子供 (baby crocodile) | 茶色 | 3 | 6 | 7 | 0 | 噛みつき 1d4 | 遊泳、水陸両用. |
| トカゲ (lizard) | 緑色 | 5 | 6 | 6 | 10 | 噛みつき 1d6 | 石化耐性. |
| カメレオン (chameleon) | 茶色 | 6 | 5 | 6 | 10 | 噛みつき 4d2 | シェイプシフター. |
| ワニ (crocodile) | 茶色 | 6 | 9 | 5 | 0 | 噛みつき 4d2 · 爪 1d12 | 遊泳、水陸両用. |
| サラマンダー (salamander) | 橙色 | 8 | 12 | -1 | 0 | 武器攻撃 2d8 · 接触 1d6 火炎 · 締め付け 2d6 · 締め付け 3d6 火炎 | 死体に毒あり、階段を追跡、火炎耐性、睡眠耐性. |

:::
