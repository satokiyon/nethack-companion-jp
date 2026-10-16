#### トラッパーおよびラーカー `t` (Trappers and lurkers `t`) {#trappers-and-lurkers-t}

<!-- audit
2026-05-19:
- Lurker above (gray L10 Spd3 AC3 MR0, engulf 1d6 + wrap 2d6) and trapper (green L12 Spd3 AC3 MR0, engulf 1d8 + wrap 2d8): monsters.h:981-998.
- Both have M1_HIDE; lurker is M1_FLY (ceiling hider per mondata.h:43-45); trapper is floor hider.
- Damage is AD_WRAP+AD_PHYS, NOT AD_DGST (monsters.h:973-980 retcon).
- Both M2_STALK (follow stairs).
-->

床や天井に擬態する固定型の包み込み捕食者です。遠見（Farlook）でも隠れたラーカーを見抜くことはできません。怪しいマスには乗る前に隣から探索（Search）を行って正体を暴いてください。

トラッパーとラーカーはすべて潜伏能力を持ち、階段の上り下りにも追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ラーカー (lurker above) | 灰色 | 10 | 3 | 3 | 0 | engulf 1d6 wrap · engulf 2d6 | 飛行. |
| トラッパー (trapper) | 緑色 | 12 | 3 | 3 | 0 | engulf 1d8 wrap · engulf 2d8 |  |

:::
