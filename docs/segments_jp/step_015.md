### 最初の潜行 (Your First Descent) {#your-first-descent}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Jackal packs are 2-4, not "four to seven" (G_SGROUP -> m_initgrp n=3; makemon.c:29,105; monsters.h:199).
- Foxes (G_GENO|1) and dwarves (G_GENO|3) are solitary; removed from the group-spawn list. Killer bees (LGROUP), soldier ants & gnomes (SGROUP) do swarm.
- Verified correct: stair-fall rnd(3) HP (do.c:1797), corpse-rot thresholds (eat.c:1887-1939), supply-chest details (mklev.c:1026-1127), cheapest-price scroll/potion (objects.h).
-->
<!-- audit
2026-05-21:
- poison-resistance corpse list for Rule 6, all with MR_POISON in both mresists and mconveys: killer bee (monsters.h:100), cave spider (monsters.h:944), yellow mold (monsters.h:1636); black pudding glob also conveys MR_POISON via mconveys (monsters.h:2118)
- puddings carry G_NOCORPSE (monsters.h:2114) so there is no CORPSE object, but on death they drop a GLOB_OF_BLACK_PUDDING / GLOB_OF_BROWN_PUDDING / etc. food item (mon.c:715-734 mksobj_at)
- eating a glob takes the same intrinsic path as eating a corpse: `piece->otyp == CORPSE || piece->globby` both trigger cpostfx(corpsenm) which calls givit() for each conveyed property (eat.c:562, 2040, 2984)
- kicking a sink can summon a black pudding: 4/5 outcomes are klunk, otherwise 1/3 chance of black pudding (dokick.c:1201-1238) — the canonical beginner trick to roll cold+shock+poison resistance globs
- magic resistance and reflection have no intrinsic source for players in 5.0; both come only from extrinsics: GDSM (do_wear.c:806-883), amulet of reflection, cloak of MR, silver shield, silver/gray DSM
2026-05-18:
- stair-falling damage is 1-3 HP via rnd(3) (do.c:1780-1795)
- floating-eye paralysis (mhitu.c:2536-2557)
- pets step around their owner (dogmove.c:535)
- lizard and lichen corpses never rot (eat.c:58-61)
- killer bees: speed 18, G_LGROUP, M1_POIS sting AT_STNG/AD_DRST 1d3 (monsters.h:96-102)
- supply chests appear above Oracle: at most one per level (placed in a random fillable room); 2/3 chance per level; 2/3 chest vs 1/3 large box; 5/6 locked (mklev.c:1010-1119)
- prayer cooldown uses rnz(350), averaging about 450 turns but with a long tail (pray.c:1356)
- corpse safe within 30 turns; tainted past ~175 turns (eat.c:1887, 1939)
- strategy aligned with NetHackWiki Stoning, Prayer, Magic resistance: lizard corpse as petrification cure, prayer-when-in-Trouble cooldown, and MR/reflection/poison-resistance "big three" are canonical advice (https://nethackwiki.com/wiki/Stoning, https://nethackwiki.com/wiki/Prayer, https://nethackwiki.com/wiki/Magic_resistance)
-->

階段を降りる。空気は冷たく湿っている。目の前には通路が伸び、暗闇の中へと分岐している。傍らにはペットが足音を立ててついてくる。

ダンジョンへようこそ。

最初の数フロアは手加減してくれますが、それはあくまで相対的な話です。モンスターも弱いですが、あなたもまた、最低限の装備、低いHP、そして中盤以降の生存に不可欠な耐性を何ひとつ持たない最も脆弱な状態です。他のどの階層よりも地下1階から5階で命を落とす冒険者が圧倒的に多いのは、敵が強大だからではなく、こちらに対抗手段がほとんどないからです。
