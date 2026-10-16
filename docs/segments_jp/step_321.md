#### ワーム `w` (Worms `w`) {#worms-w}

<!-- audit
2026-05-19:
- 4 rows (S_WORM) sourced from monsters.h:1114-1145: baby long worm 1118, baby purple 1124, long worm 1130, purple worm 1138.
- Long worm tail and segment mechanics in worm.c; purple worm AT_ENGL/AD_DGST swallow at monsters.h:1141.
- Long worm drops worm tooth on death; fires only for PM_LONG_WORM, not baby (mon.c:618-620).
- Long worm grown segments tracked via mtmp->wormno (mon.c:5451, get_wormno on polymorph to PM_LONG_WORM).
-->

長いワームは攻撃を受けるたびに尾のセグメントへ分裂して増殖します。紫ワーム（Purple worm）はプレイヤーを一撃で丸呑み（胃袋へ収容）して消化死させる極めて危険な怪物です。消化死を防ぐ手段（耐へんげの魔除けなど）や、胃袋の内側から脱出する手段を用意してください。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ロングワームの子供 (baby long worm) | 茶色 | 5 | 3 | 5 | 0 | 噛みつき 1d4 |  |
| 紫ワームの子供 (baby purple worm) | 赤紫 | 8 | 3 | 5 | 0 | 噛みつき 1d6 |  |
| ロングワーム (long worm) | 茶色 | 9 | 3 | 5 | 10 | 噛みつき 2d4 | drops a worm tooth. |
| 紫ワーム (purple worm) | 赤紫 | 15 | 9 | 6 | 20 | 噛みつき 2d8 · engulf 1d10 digest |  |

:::
