### 薬屋 (The Apothecary) {#the-apothecary}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Potion of healing cures blindness unless CURSED (cureblind = !cursed, potion.c peffect_healing); table row said "when blessed".
- Verified correct: speed intrinsic, holy-water dip whole stacks, alchemy recipes & explosion odds, unicorn-horn cures, enchant caps, genocide/charging/remove-curse mechanics.
-->
<!-- audit
2026-05-19:
- dip_potion_explosion tests the DIPPING potion's BUC, not the receiver (potion.c:2279, 2541)
- the receiving potion is consumed regardless via useup(potion) (potion.c:2538)
- never dip a CURSED potion into another — guaranteed explosion
2026-05-18:
- potion of speed grants permanent intrinsic Fast when !cursed (potion.c:1066)
- uncursed extra/full healing also raise maxHP (potion.c:1398-1440)
- strategy aligned with NetHackWiki Potion, Alchemy, Dip: alchemy odds and the guaranteed-blast cases for cursed/acid potions match (https://nethackwiki.com/wiki/Potion, https://nethackwiki.com/wiki/Alchemy, https://nethackwiki.com/wiki/Dip)
- dipping an item (including a single arrow/dart) into a polymorph potion changes its type via poly_obj and identifies the potion (potion.c:2468-2499)
-->

薬の外見（未識別名）はゲームごとにシャッフルされます。頼りになるのは価格と計画的なテストだけであり、「前回のゲームで泡立つ薬が回復の薬だった」という記憶は何の役にも立ちません。
