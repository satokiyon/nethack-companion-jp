#### 倉庫番 (Sokoban: 5.0新要素) {#sokoban-new-in-5.0}

<!-- audit
2026-05-19:
- digging does NOT trigger sokoban_guilt; dig.c has no such call (sokoban_guilt callers limited to hack.c:299/307/398/403, read.c:1951, steed.c:767, zap.c:1711/5556 — none in dig.c)
- breaks: squeeze through (hack.c:299, 307), boulder fracture by wand of striking (zap.c:5556)
- breaks: polymorph a boulder (zap.c:1711), scroll of earth (read.c:1951), dismount onto a boulder (steed.c:767)
- each violation costs -1 Luck and increments u.uconduct.sokocheat (trap.c:7039-7054)
- achievement reported only if the branch was entered (insight.c:2215-2228)
- teleportation is blocked by the level's noteleport flag (teleport.c:1185); it's a level constraint, not a conduct trigger
-->

倉庫番のルールを一度も破ることなく進入・プレイします。ゲーム終了時にこのコンダクトが記録されるために、必ずしも倉庫番を最後まで登りきる必要はありません。違反行為1回ごとに **幸運が 1点 低下** し、不正カウンターが加算されます：小型形態や極度に身軽な荷物による **巨岩のすり抜け**、衝撃やつるはしや衝撃の杖による **巨岩の粉砕**、巨岩の **変身**、**大地の巻物** の読書、あるいは巨岩のマスへの **下馬** です。ゲームはこれらの違反を自動的に追跡します。
