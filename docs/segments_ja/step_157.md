### 武具庫 (The Armory)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Shield spell penalty is weight-gated (weight > small-shield's 30, spell.c:2269); the 30-weight drain- and shock-resistance shields also avoid it, so the small shield isn't the "only" one.
- Crysknife reverts to a worm tooth EVERY time unless erodeproofed (then ~10%); the book had it inverted (do.c:911).
- Monk martial-arts -20 to-hit applies to ANY body armor including dragon scale mail (uhitm.c:397, "if (uarm)"); DSM is not exempt.
- Rangers CAN two-weapon (unskilled, -9), not "cannot at all" (can_twoweapon has no role gate, wield.c:766).
- Verified correct: AC/MC values, DSM +3 vs mail +9 & merge rules, enchant destruction thresholds, robe halving metal-suit penalty, gauntlets of power Str 25, Excalibur odds, lance joust.
-->
<!-- audit
2026-05-18:
- shield of drain resistance is a second non-artifact source (objects.h:656-658)
- warning glyph levels: white, red ×3, magenta, bright-magenta — no yellow (drawing.c:39-52)
- cloak of protection MC3; cloak of magic resistance MC1 (objects.h:637-646)
- MC formula at uhitm.c:87 — MC3 blocks 90% of monster spells
- helm of caution grants the WARNING intrinsic (do_wear.c:448-450)
- DSM dual-property pattern: armor + per-color intrinsic (do_wear.c:806-883)
- gray and silver DSM grant no extra intrinsic
- DSM scroll-of-enchant transformation requires spe ≥ 0 (read.c:1225)
- shield casting penalty has two parts: ANY shield adds flat spelshld to splcaster (spell.c:2197; Wiz 3, Pri 2), and a shield heavier than small-shield (>30 weight) quarters the final chance (spell.c:2269). Small shield + the 30-weight drain/shock-resistance shields dodge only the /4; the flat penalty still applies to any shield.
- strategy aligned with NetHackWiki Dragon scale mail, Cloak of protection, Magic cancellation, Speed boots: GDSM as the popular MR wish, MC3 from cloak of protection, speed boots make turns more numerous (https://nethackwiki.com/wiki/Dragon_scale_mail, https://nethackwiki.com/wiki/Cloak_of_protection, https://nethackwiki.com/wiki/Magic_cancellation, https://nethackwiki.com/wiki/Speed_boots)
-->

このセクションでは、装備の選び方を解説します。[武器一覧表](#weapons-tables) および [防具一覧表](#armor-tables) の付録には、すべてのアイテムの完全な性能値が記載されています。

