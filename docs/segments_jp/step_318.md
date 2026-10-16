#### 罠生物 `t` (Trappers and lurkers `t`) {#trappers-and-lurkers-t}

<!-- audit
2026-05-19:
- Lurker above (gray L10 Spd3 AC3 MR0, engulf 1d6 + wrap 2d6) and trapper (green L12 Spd3 AC3 MR0, engulf 1d8 + wrap 2d8): monsters.h:981-998.
- Both have M1_HIDE; lurker is M1_FLY (ceiling hider per mondata.h:43-45); trapper is floor hider.
- Damage is AD_WRAP+AD_PHYS, NOT AD_DGST (monsters.h:973-980 retcon).
- Both M2_STALK (follow stairs).
-->

床に擬態するトラッパーと、天井に擬態するラーカーが含まれます。不用意に踏み込むと丸呑み（圧搾）され、脱出するまで毎ターンダメージを受け続けます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ラーカー (lurker above) | 灰色 | 10 | 3 | 3 | 0 | engulf 1d6 巻きつき · engulf 2d6 | 飛行. |
| トラッパー (trapper) | 緑色 | 12 | 3 | 3 | 0 | engulf 1d8 巻きつき · engulf 2d8 |  |

:::
