### 魔法詠唱 (Spellcasting)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Cursed-spellbook contact poison is 3-6 Str + 1d10 HP by default; 1-2 Str + 1d6 HP only with poison res (spell.c:164, poison_strdmg). Was "1-2 Str + 1d10 HP".
- Verified correct: read-success formula & lenses bonus, blessed/cursed auto results, exploding-rune 2d10+5, Pw cost 5*level, failed-cast half-Pw, Pw-regen ticks, chain lightning 2d6.
-->
<!-- audit
2026-05-21:
- spellbook of type SPE_NOVEL appears as "paperback" until read (objects.h:1433-1436)
- reading the first novel in a game grants more_experienced(20, 0) and the ACH_NOVL achievement; u.uevent.read_tribute gates the once-per-game bonus (spell.c:513-535)
- 20 XP is the XL 1->2 threshold so a fresh character gains an experience level on the first paperback read
- novel title is rolled at game start per novelidx; titles come from a list of Terry Pratchett Discworld novels stored in the tribute file (do_name.c:297 noveltitle, files.c:3474 read_tribute)
2026-05-18:
- force bolt damage is 2d12; school skill does NOT scale damage (zap.c:2720-2724)
- chain lightning is level 2 NODIR, not level 7, not a bouncing ray (objects.h:1409-1411; SPELL fields are name,desc,sub,prob,delay=4,level=2)
- failed spellbook read effects: teleport (lvl 1+), aggravate (lvl 2+), blindness (lvl 3+), take-gold (lvl 4+), confusion (lvl 5+), contact poison (lvl 6+), exploding rune (lvl 7+, 2d10+5 dmg, antimagic resists). Default rndcurse branch never fires: max spell level is 7 so rn2(lev) maxes at 6 (spell.c:130-185)
- failed read has a single 1/3 destruction chance (spell.c:612)
- spellbook fade ceiling is 4 successful reads: MAX_SPELL_STUDY=3 with `> MAX_SPELL_STUDY` (spell.c:400-418)
- no Pw drain from memorized spells exists; "spell maintenance" is fabricated (allmain.c moveloop has no per-spell Pw decrement; only cast_spell at spell.c:1245 decrements via SPELL_LEV_PW)
- drain_en only ever DECREASES Pw — no reflection+vortex max-Pw trick (trap.c:5202-5240 drain_en only subtracts from u.uen and decreases u.uenmax)
- blessed book bypasses the read-ability check entirely (auto-success)
- Pw cost per spell = 5 × level: SPELL_LEV_PW(spellev) (spell.c:1245)
- confused casts fail outright (spell.c:1372); charm monster has no confused-area mode
- Skilled+ casting acts like a blessed scroll (spell.c:1524-1525) or blessed potion (spell.c:1540-1541)
- Pw regen: (Wis + Int)/15 + 1; Wizards tick on factor 3 vs 4 (allmain.c:605-607)
- Valkyries restricted in divination, so reading scroll of identify is occasional at best (u_init.c:525-546)
- strategy aligned with NetHackWiki Spellbook, Spellcasting: Int + 4 + XL/2 − 2·level success formula, blessed book auto-success, Pw = 5 × level (https://nethackwiki.com/wiki/Spellbook, https://nethackwiki.com/wiki/Spellcasting)
-->

呪文は、魔法書から学ぶことで何度でも繰り返し行使できる能力です。使うと消滅する巻物や、使用回数が限られている杖とは異なり、マナ（Pw / 魔力）が残っており、酷使され続ける冒険者の頭脳から記憶が失われていない限り、何度でも呪文を唱える（`Z`）ことができます。

