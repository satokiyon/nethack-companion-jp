#### 精霊・エレメンタル `E` (Elementals `E`)

<!-- audit
2026-05-19:
- 5 rows (stalker/air/fire/earth/water elemental) sourced from monsters.h:1566-1610.
- Stalker: sees-invis, M2_STALK; NOT mindless. (monsters.h:1566-1573 has M1_SEE_INVIS and M2_STALK; no M1_MINDLESS in flags1)
- Air: AT_ENGL AD_PHYS 1d10. "Air suffocates" is engulf flavor for AD_PHYS, NOT a separate AD_DRST. (monsters.h:1576 air elemental single AT_ENGL AD_PHYS 1d10; no AD_DRST attack)
- Fire: claw 3d6 AD_FIRE + passive 0d4 fire.
- Earth: claw 4d6; MR_FIRE|MR_COLD|MR_POISON|MR_STONE.
- Water: claw 5d6; M1_SWIM|M1_AMPHIBIOUS; MR_POISON|MR_STONE. Water elementals lack a drown attack, but spawn only on water tiles so encounters happen near drowning risk.
-->

風の精はプレイヤーを包み込んで瓦礫の嵐で叩きのめします。火の精は周囲を灼熱で焼き焦がし、水の精は強打を繰り出し、土の精は動きは鈍いものの極めて強固です。

*ストーカー*を除き、すべてのエレメンタルは精神を持ちません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ストーカー (stalker) | 白色 | 8 | 12 | 3 | 0 | 爪 4d4 | 飛行, sees-不可視, follows stairs. |
| 風の精 (air elemental) | 水色 | 8 | 36 | 2 | 30 | engulf 1d10 | 飛行. |
| 火の精 (fire elemental) | 黄色 | 8 | 12 | 2 | 30 | 爪 3d6 火炎 · 反撃 9d4 火炎 | 飛行. |
| 土の精 (earth elemental) | 茶色 | 8 | 6 | 2 | 30 | 爪 4d6 | 火炎耐性, 冷気耐性, 毒耐性, 石化耐性. |
| 水の精 (water elemental) | 青色 | 8 | 5 | 2 | 30 | 爪 5d6 | 遊泳, 水陸両用, 毒耐性, 石化耐性. |

:::
