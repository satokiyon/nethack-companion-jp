#### 菌類およびモールド `F` (Fungi and molds `F`) {#fungi-and-molds-f}

<!-- audit
2026-05-19:
- 7 rows sourced from monsters.h:1614-1676; elemental molds are brown/green/red, NOT violet/yellow.
- Lichen corpse never rots (mkobj.c:1402, eat.c:59); also never out of season as iron rations.
- Yellow mold has M1_POIS (poisonous corpse, monsters.h yellow-mold row).
- Other molds have MR_POISON resistance but no M1_POIS, so their corpses are NOT poisonous.
- Brown mold passive 0d6 cold (HP drain), green 0d4 acid, red 0d4 fire, yellow 0d4 stun (monsters.h:1614-1666).
- Violet fungus AT_TUCH/AD_PHYS 1d4 plus AT_TUCH/AD_PLYS sticky (monsters.h:1668-1676).
-->

移動しない固定型の生物です。苔の怪物（Lichen）の死体は決して腐敗しないため、非常用の携帯食糧として最適です。茶色、緑、赤のモールドはそれぞれ冷気、酸、火炎の反撃ダメージを放ちます。

すべての菌類およびモールドは精神を持ちません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 苔の怪物 (lichen) | 明緑 | 0 | 1 | 9 | 0 | 接触 sticky |  |
| 茶色モールド (brown mold) | 茶色 | 1 | 0 | 9 | 0 | 反撃 2d6 冷気 | 冷気耐性, 毒耐性. |
| 黄色モールド (yellow mold) | 黄色 | 1 | 0 | 9 | 0 | 反撃 2d4 stun | 死体に毒あり, 毒耐性. |
| 緑モールド (green mold) | 緑色 | 1 | 0 | 9 | 0 | 反撃 2d4 酸 | 酸耐性, 石化耐性. |
| 赤色モールド (red mold) | 赤色 | 1 | 0 | 9 | 0 | 反撃 2d4 火炎 | 火炎耐性, 毒耐性. |
| シュリーカー (shrieker) | 赤紫 | 3 | 1 | 7 | 0 | — | 毒耐性. |
| 紫キノコ (violet fungus) | 赤紫 | 3 | 1 | 7 | 0 | 接触 1d4 · 接触 sticky | 毒耐性. |

:::
