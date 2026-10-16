### 幸運と運命 (Luck and Fortune) {#luck-and-fortune}

<!-- audit
2026-09-27 luckstone rewrite vs NetHack-5.0 source:
- timeout.c:600-616 (nh_timeout): time_luck = stone_luck(FALSE) = sgn(blessed - cursed luck items); good Luck decays only if no stone or time_luck < 0; bad Luck recovers only if no stone or time_luck > 0. So BLESSED keeps good Luck but lets bad Luck recover; UNCURSED freezes both; CURSED freezes bad and lets good decay. The earlier "any non-cursed luckstone freezes drift" was wrong for blessed.
- the +-3 is u.moreluck (attrib.c set_moreluck, LUCKADD you.h:465), added to every Luck check via Luck = u.uluck + u.moreluck (you.h:464); it is not a cap. u.uluck clamps at +-10 (change_luck, attrib.c:411), so total Luck spans +-13.
- several luck items: stone_luck nets cursed against non-cursed (moreluck) and cursed against blessed (timeout); never more than +-3.
- drift every 300 turns with the Amulet or an angry god (timeout.c:604).
- luck items: any LUCKSTONE (incl. the Heart of Ahriman) or SPFX_LUCK artifacts, the Tsurugi of Muramasa and the Orb of Fate (artifact.c:526 confers_luck, artilist.h).
-->
<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Removed three "Luck +5 benefits" that use plain rn2 (no Luck term): enchant-scroll success (read.c:1180, wield.c:1004), wand wresting (rn2(121), hack.h:1419), fountain wishes (fountain.c:78). Kept to-hit and prayer (which Luck does affect).
- Verified correct (also covers Exercising Your Stats): effective Luck range & timeout, luckstone freeze/±3, luck artifacts, the whole gain/lose-Luck table, sacrifice ceiling, prayer-fails-on-negative-Luck, all stat exercise/abuse actions.
-->
<!-- audit
2026-05-19:
- cursed luckstone holds NEGATIVE Luck in place, but positive Luck still decays toward baseline (timeout.c:616-619)
- any non-cursed luckstone (blessed or uncursed) gives +3 max-Luck cap (attrib.c:441-450)
- killing peaceful: -1 with 50% probability (mon.c:3665); -5 reserved for co-aligned unicorns (mon.c:3667)
- prayer is rejected on ANY negative Luck (pray.c:2155), not just <= -10
- no Sokoban-down-stairs Luck penalty exists
- thrown gem to cross-aligned unicorn: identified -3..+3 (dothrow.c:2334 rn2(7)-3); unidentified -1..+1 (dothrow.c:2349 rn2(3)-1)
- "ID gems for shopkeeper +1" is fabricated; shk.c has no such hook (shk.c contains no change_luck or adjalign call on GEM_CLASS sale)
- killing quest leader: -4 baseline, immediate change_luck(-20), u.ugangr += 7 (mon.c:3680, timeout.c:600)
- killing pet: -1 plus alignment -15 via adjalign (mon.c:3664, 3704)
- only mirror breaks for Luck -2 (uhitm.c:1133, dothrow.c:2496, dokick.c:445/1724); crystal balls/armor don't
- full-moon/Friday-the-13th baseline shift (timeout.c:595-598)
- carrying the Amulet or u.ugangr > 0 doubles drift rate (300 turns, timeout.c:607)
- Archeologists start with TOUCHSTONE knowledge only (u_init.c:50, 903); gems are NOT pre-identified
- strategy aligned with NetHackWiki Luck, Luckstone, Luck item: ±13 cap with non-cursed luckstone, drift toward 0 every 600 turns, cursed luckstone locks negative Luck (https://nethackwiki.com/wiki/Luck, https://nethackwiki.com/wiki/Luckstone, https://nethackwiki.com/wiki/Luck_item)
-->

幸運（Luck）は画面には表示されない隠しステータスですが、以下の4つの原則を頭に入れておけば大半の状況を正しくコントロールできます：

1. 祈りを常に安全に行えるよう、幸運を常に 0 以上に保つこと。
2. 幸運の石を手に入れたら、祝福して鞄に入れずインベントリに直接携帯すること。
3. 識別済みの本物の宝石を、自属性と同じユニコーンに投げ与えること。
4. 理由もなく平和的な生物を殺したり、鏡を割ったりしないこと。
