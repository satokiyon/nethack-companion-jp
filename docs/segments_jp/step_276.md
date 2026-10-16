#### 六尺棒 (Quarterstaff) {#quarterstaff}
<!-- audit
2026-05-19:
- quarterstaff: bimanual, 1d6/1d6, wt 40, cost 5, WOOD, P_QUARTERSTAFF (objects.h:377-379).
- Wizard starter weapon (u_init.c:168).
- bimanual: gets 3/2 Str damage bonus in melee (uhitm.c:1467).
- Expert caps: Wizard, Priest, Healer, Caveman (u_init.c:314,334,396,555 P_QUARTERSTAFF=P_EXPERT).
- No Knight or Rogue entry: P_QUARTERSTAFF absent from Skill_K and Skill_R (u_init.c:346-413).
-->

両手持ち近接武器。控えめな基本ダイス値にもかかわらず、筋力ダメージ 1.5 倍（3/2）ボーナスが適用されます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 六尺棒 (quarterstaff) | 1d6 / 1d6 | 40 | 5 | — | 木 | 両手持ちだが軽量。魔法使い（Wizard）の初期装備。 |

:::
