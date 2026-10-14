<!-- audit
2026-05-19:
- 5 knife rows verified: P_KNIFE skill, scalpel METAL, knife/stiletto IRON, worm tooth/crysknife BONE (objects.h:215-233)
- scalpel is Healer's starter (u_init.c:77)
- crysknife reverts to worm tooth on drop via type-id swap, NOT poly (do.c:903-918)
- fixed (erodeproof) crysknife only reverts ~10% of drops (do.c:911)
-->
#### ナイフ (Knife)

主に近接戦闘用。ナイフはスタック可能で投擲もできますが、投擲ナイフによるマルチショットボーナスを得られる職業はありません。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| メス (scalpel) | 1d3 / 1d3 | 5 | 6 | +2 | 金属 | 医師（Healer）の初期装備。 |
| ナイフ (knife / shito: 刺刀) | 1d3 / 1d2 | 5 | 4 | — | 鉄 |  |
| スティレット (stiletto) | 1d3 / 1d2 | 5 | 4 | — | 鉄 |  |
| ワームの歯 (worm tooth) | 1d2 / 1d2 | 20 | 2 | — | 骨 |  |
| クリスナイフ (crysknife) | 1d10 / 1d10 | 20 | 100 | +3 | 骨 | 床に落としたり投げたりするとワームの歯に戻ってしまう。耐腐食（erodeproof）加工されたものは戻る確率が約10%に軽減される。 |

:::
