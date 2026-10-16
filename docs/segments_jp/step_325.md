#### 天使系 `A` (Angelic beings `A`) {#angelic-beings-a}

<!-- audit
2026-05-19:
- 5 rows at monsters.h:1206-1265 (couatl 1206, Aleax 1216, Angel 1225, ki-rin 1240, Archon 1252).
- All Angels have G_NOCORPSE; couatl leaves no corpse (MR_POISON still matters for combat).
- AD_MAGM ("magic") on Angel; AD_SPEL ("spell") on ki-rin/Archon.
- Ki-rin HI_GOLD = yellow; Archon HI_LORD = magenta (color.h:38,46).
- Archon has M1_REGEN, M1_SEE_INVIS, plus 5-attack chain (weapon, weapon, gaze, claw, spell).
-->

神に仕える聖なる使い。自身の属性と同じ天使を攻撃すると神の怒りを買います。アルコンや天使は強力な呪文と盲目攻撃を繰り出すため、敵対した際は最大級の警戒が必要です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コウアトル (couatl) | 緑色 | 8 | 10 | 5 | 30 | 噛みつき 2d4 毒 · 噛みつき 1d3 · 締め付け 2d4 巻きつき | 毒耐性. |
| アレアックス (Aleax) | 黄色 | 10 | 8 | 0 | 30 | 武器攻撃 1d6 ×2 · 蹴り 1d4 |  |
| 天使 (Angel) | 白色 | 14 | 10 | -4 | 55 | 武器攻撃 1d6 ×2 · 爪 1d4 · 呪文詠唱 2d6 魔法 |  |
| 麒麟 (ki-rin) | 黄色 | 16 | 18 | -5 | 90 | 蹴り 2d4 ×2 · 頭突き 3d6 · 呪文詠唱 2d6 spell |  |
| アルコン (Archon) | 赤紫 | 19 | 16 | -6 | 80 | 武器攻撃 2d4 ×2 · 凝視 2d6 盲目 · 爪 1d8 · 呪文詠唱 4d6 spell | 自動回復. |

:::
