### 指輪と魔除け (Rings and Amulets) {#rings-and-amulets}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Amulet of life saving revives to min(maxHP, 50+10*(Con/2)), not full HP (end.c:710,719).
- Amulet of strangulation is 90% cursed at generation (rn2(10)), not "always" (mkobj.c:1063).
- Verified correct: ray range, make-invisible/stasis durations, backfire 1/100, ring prices, MC/guarding rules, auto-curse 90%, ring-hunger ticks.
-->
<!-- audit
2026-05-18:
- ring prices match objects.h:741-827
- teleportation, polymorph, aggravate-monster, hunger rings 90% cursed (mkobj.c:1143-1146)
- aggravate-monster effective-depth doubling is capped at 50 (dungeon.c:2080-2082)
- free action gives paralysis immunity via Free_action (apply.c:1044, mcastu.c:506)
- ring hunger cost ticks at turns 4 and 12 (eat.c:3237-3267)
- amulet of guarding: +2 AC, +2 MC (do_wear.c:2496, mhitu.c:1121-1126)
- restful sleep regenerates +1 HP per sleep tick (allmain.c:663-664)
- restful sleep is 90% cursed at generation, not 100% (mkobj.c:1063-1066 via rn2(10))
- ring of protection subtracts from AC (do_wear.c:2492-2495)
- conflict makes pets attack you (dogmove.c:1046-1054, mhitm.c:104-145)
- blessed polymorph control rolls from base form only (potion.c:1322-1325)
- strategy aligned with NetHackWiki Ring strategy, Ring of free action, Ring of conflict, Amulet of life saving: free action against late-game paralysis, conflict for crowd control, life saving for risky endgame moments (https://nethackwiki.com/wiki/Ring_strategy, https://nethackwiki.com/wiki/Ring_of_free_action, https://nethackwiki.com/wiki/Ring_of_conflict, https://nethackwiki.com/wiki/Amulet_of_life_saving)
-->

指輪は左右の手の指に1つずつ計2つ、魔除けは首に1つ身につけることができます。身につけるには `P`（Put on）、外すには `R`（Remove）を押します。指輪と魔除けはこのキーペアで操作します（防具の着脱は `W` と `T` です）。
