### ダンジョン生態系ガイド (Field Guide to Dungeon Fauna) {#field-guide-to-dungeon-fauna}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Displacer beast has no melee place-swap; removed the fabricated "50% chance to swap places." M3_DISPLACES only barges past other monsters when moving (mm_displacement, mon.c, monster-vs-monster). Corpse still grants temporary Displacement (eat.c:1265-1268).
- Verified correct: soldier ant/bat/centaur/jabberwock/mumak/xorn/gargoyle/naga stats, mind-flayer helmet block 7/8 (uhitm.c:3235), gremlin night-only intrinsic strip (uhitm.c:3040) & water split (mon.c:987).
-->
<!-- audit
2026-05-18:
- xan: AT_STNG AD_LEGS (sting cripples legs); xan is class `x`, not the engulfer `t` (S_TRAPPER) (monsters.h:1157-1159)
- leprechaun attack is AT_CLAW AD_SGLD (gold-steal claw), not a bite (monsters.h:660)
- long worms grow tail segments on a movement-driven wgrowtime timer, not per hit (worm.c:218-237)
- pudding split admits IRON|METAL weapons only (uhitm.c:1616-1618)
- there are no dragonhide weapons in 5.0; DRAGON_HIDE material is body-armor-only
- silver and wooden weapons are the actual pudding non-splitters (uhitm.c:1616-1620 admits IRON|METAL only)
- all other class-symbol mappings (defsym.h) and per-monster stats verified clean
- rothe ('q'-class fame): three attacks per turn (claw + two bites), the only Q-class monster lacking M2_STRONG, and the canonical early-q threat per NetHackWiki (https://nethackwiki.com/wiki/Rothe, https://nethackwiki.com/wiki/Quadruped)
2026-05-31 audit:
- homunculus (S_IMP class `i`) AT_BITE AD_SLEE 1d3, Level 2, speed 12, flies, sleep-resistant itself (monsters.h:551-558). The sleep effect on bite is a real early-game threat — sleep status + adjacent enemies is often lethal. Both the Field Guide summary at companion.md:905 and the bestiary intro at companion.md:10976 had previously described the `i` class as "annoying but not dangerous" / "none individually scary"; corrected to flag the homunculus specifically.
- water moccasin (M1_POIS, AD_DRST bite drains Str): poisonous corpse but also confers poison resistance (MR_POISON in both mresists and mconveys columns at monsters.h WATER_MOCCASIN row). Eating risks 1d4 Str + 1d15 HP on the 1-in-5 poison roll without resistance (eat.c:1928-1936); ~1-in-15 conferred-resistance grant per successful eat.
-->


迷宮には何百種ものモンスターが生息しており、アルファベットの文字で表される分類（クラス）に体系化されています。小文字は一般に小型または危険度の低いモンスターを示し、大文字はより大型または危険なモンスターを示します。さらに文字の色によって、同一分類内の個別の種が区別されます。

ここでは、各文字が何を意味するのか、おおむね序盤に出現する順に沿って手短に解説します。全モンスターの詳細なレベル、速度、AC、攻撃能力のデータについては、巻末の [モンスター図鑑 (Bestiary Tables)](#bestiary-tables) を参照してください。
