<!-- audit
2026-05-19:
- crossbow bolt: 1d4 / 1d6, NO +1 bonus (objects.h:155-156 PROJECTILE)
- crossbows CAN multishot: requires Str 18 (Str 16 for gnomes), with +1 baseline gnome bonus (dothrow.c:225-231, 205-209)
- skill caps: Rogue Expert, Ranger Expert, Knight Skilled (u_init.c)
- Valkyries cap at Unskilled, NOT Skilled: Skill_V has no P_CROSSBOW entry (u_init.c:525-547)
-->
#### クロスボゥ (Crossbow)

片手持ちの発射具。弓よりも1発あたりの威力が高くなっていますが、リロードが遅く、完全なマルチショットを行うには筋力 18（ノームは筋力 16）が必要です。弓と同様、二刀流は阻害しますが盾の装備は可能です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| クロスボゥボルト (crossbow bolt) | 1d4+1 / 1d6+1 | 1 | 2 | — | 鉄 | スタック可能。 |
| クロスボゥ (crossbow) | — | 50 | 40 | — | 木 | ボルトは敵を貫通する。**筋力 18**（ノームは 16）以上でマルチショットが通常通りのダイス判定となる。それ未満の場合、ゲームは2回ロールして小さい方の連射数を採用する。またノームはマルチショット数に+1される。盗賊と野伏はエキスパート、騎士は熟練まで習得可能。 |

:::
