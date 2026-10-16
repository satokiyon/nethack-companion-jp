#### ゼリー `j` (Jellies `j`) {#jellies-j}

<!-- audit
2026-05-19:
- 3 rows (blue/spotted/ochre jelly) sourced from monsters.h:591-620; all carry M1_AMORPHOUS|M1_MINDLESS.
- Blue jelly corpse conveys cold + poison resistance permanently (eat.c:983-988 should_givit).
- Spotted/ochre corpses convey acid + stone resistance TIMED (eat.c:991-997 temp_givit).
- A passive attack written as 0dN in the monster definition rolls (monster level + 1)dN in combat; blue jelly is therefore 6d6 and spotted jelly 7d6 (uhitm.c:5885-5888).
-->

壁際や床に張り付く不定形の怪物です。青色ゼリーは冷気、赤色ゼリーは火炎の反撃ダメージを与えます。金属武器を腐食させる斑点ゼリーにも注意が必要です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 青色ゼリー (blue jelly) | 青色 | 4 | 0 | 8 | 10 | 反撃 5d6 冷気 | 死体：冷気耐性・毒耐性獲得。 |
| まだらゼリー (spotted jelly) | 緑色 | 5 | 0 | 8 | 10 | 反撃 6d6 酸 | 死体：一時的な酸耐性・石化耐性獲得。 |
| 黄土色ゼリー (ochre jelly) | 茶色 | 6 | 3 | 8 | 20 | engulf 3d6 酸 · 反撃 3d6 酸 | 死体：一時的な酸耐性・石化耐性獲得。 |

:::
