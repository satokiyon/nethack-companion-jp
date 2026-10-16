#### 人型生物 `h` (Humanoids `h`)

<!-- audit
2026-05-19:
- 7 rows (S_HUMANOID) sourced from monsters.h:477-542.
- hobbit L1/Spd9/AC10 weapon 1d6 (monsters.h:477-484).
- dwarf L2/Spd6/AC10 weapon 1d8, M1_TUNNEL (monsters.h:485-493).
- dwarf lord L4/Spd6/AC10 weapon 2d4 ×2 (monsters.h:502-510).
- dwarf king L6/Spd6/AC10 weapon 2d6 ×2, MR 20% (monsters.h:511-520).
- mind flayer L9/Spd12/AC5 MR 90%, 3× tentacle AD_DRLI (monsters.h:521-530).
- master mind flayer L13/Spd12/AC0 MR 90%, 5× tentacle (monsters.h:531-542).
- helmet blocks mind-flayer tentacle 7/8 of the time (uhitm.c:3235, `uarmh && rn2(8)`).
- Any helmet blocks the mind flayer attack, NOT only alignment-matching or telepathy/free-action helmets.
- Bugbear is AT_WEAP only, no bite (monsters.h:494-501).
- Dwarf race peacefulness for Dwarf PCs via race_peaceful() at makemon.c:2283.
-->

小人族、ホビット、ドワーフ、巨人など多彩な人型生物が含まれます。ノームの鉱山ではドワーフが中立または友好的に出現することが多く、彼らの落とすミスリル服や鉄兜は序盤の貴重な防具供給源となります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ホビット (hobbit) | 緑色 | 1 | 9 | 10 | 0 | 武器攻撃 1d6 |  |
| ドワーフ (dwarf) | 赤色 | 2 | 6 | 10 | 10 | 武器攻撃 1d8 | tunnels. |
| バグベアー (bugbear) | 茶色 | 3 | 9 | 5 | 0 | 武器攻撃 2d4 |  |
| dwarf lord | 青色 | 4 | 6 | 10 | 10 | 武器攻撃 2d4 ×2 | tunnels. |
| dwarf king | 赤紫 | 6 | 6 | 10 | 20 | 武器攻撃 2d6 ×2 | tunnels. |
| マインドフレア (mind flayer) | 明紫 | 9 | 12 | 5 | 90 | 武器攻撃 1d4 · tentacle 2d1 エナジードレイン-Int ×3 | 飛行, sees-不可視. Tentacles drain Int; once it reaches 3, the next tentacle that lands kills you. Any helmet blocks 7/8 of tentacles. |
| マスターマインドフレア (master mind flayer) | 明紫 | 13 | 12 | 0 | 90 | 武器攻撃 1d8 · tentacle 2d1 エナジードレイン-Int ×5 | 飛行, sees-不可視. Five tentacles per turn. Any helmet blocks 7/8 of tentacles. |

:::
