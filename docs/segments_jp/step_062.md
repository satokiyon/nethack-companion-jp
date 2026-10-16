### 戦闘の技術 (The Art of Combat)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Armor donning: helmets/gloves 1 turn, boots 2, cloaks/shields 0 (per-item delay, objects.h BOOTS/SHIELD/CLOAK macros). Was "1 each".
- Speed table: gnome/kobold/dwarf are 6 (not 12); fire ant 18 (not 12); molds 0 and other fungi 1 (not 6); humans/elves are the 12 tier (monsters.h; NORMAL_SPEED=12, permonst.h:80).
- Encumbrance is applied AFTER the Fast/Very-Fast bonus, cutting the boosted total (allmain.c:121-149). Was "before".
- Samurai multishot bonus is ya+yumi (bow) only, not shuriken (dothrow.c:73-75).
- Nagas have no M1_REGEN; removed from the "regenerate every turn" list (monsters.h).
-->
<!-- audit
2026-05-20:
- waking a sleeping monster via attack invokes wakeup() (uhitm.c:250, 305, 1403, 1926, 5213, 5590, 5694, 5764, 5774); if the struck monster was sleeping AND not MS_SILENT AND not helpless, growl() fires (mon.c:4353-4356 wakeup)
- growl() calls wake_nearto(mtmp->mx, mtmp->my, mtmp->data->mlevel * 18) (sounds.c:421) — radius approx sqrt(mlevel * 18) in tiles
- Knight caitiff penalty: -1 alignment for attacking helpless or fleeing non-undead monsters when Lawful (uhitm.c:336-341)
- Samurai dishonor penalty: -1 alignment for attacking peacefuls (uhitm.c:342-345)
- Samurai poisoned-weapon penalty: -sgn(u.ualign.type) alignment (uhitm.c:1521)
- Quest entrance requires alignment record >= MIN_QUEST_ALIGN = 20 AND ulevel >= MIN_QUEST_LEVEL = 14 (quest.h:43-45)
2026-05-18:
- to-hit factors: XL, Str, Dex, Luck, enchantment, AC (find_roll_to_hit)
- abon includes both Strength AND Dexterity; Dex 25 yields +11 (weapon.c:950-988)
- dbon has a Strength cap: max +6 at STR 18/100 or higher (weapon.c:993-1015)
- two-handed weapons get a 3/2 Strength-bonus multiplier (weapon.c bhitval two-handed branch)
- conflict requires mutual sight and a Cha-vs-Lvl resist roll: resist_chance = min(19, Cha - m_lev + XL) (mondata.c:1607-1612)
- two-weapon and shield are mutually exclusive
- Expert two-weapon: Rogue and Samurai only (u_init.c skill tables)
- Rangers CAN two-weapon but only unskilled (-9 to-hit, weapon.c:1587); can_twoweapon has no role gate (wield.c:766). Skill_Ran lacks the entry so it's untrainable, not forbidden.
- two-weapon penalty is a flat table: -9/-7/-5/-3 to-hit, -3/-1/0/+1 damage
- Luck to-hit contribution is sgn(Luck)·((|Luck|+2)/3), capping at ±5 (uhitm.c:377); Luck itself ranges ±10, ±13 with luckstone
- monsters use m_move (phase 3) then mattacku/castmu (phase 4) on the same turn (monmove.c:911, 943-944, 971)
- no "free extra step" change exists; that earlier claim was fabricated
- strategy aligned with NetHackWiki Corridor, Movement tactics, Twoweapon: corridor chokepoint as the single biggest tactical principle, two-weapon penalty tied to skill rank (https://nethackwiki.com/wiki/Corridor, https://nethackwiki.com/wiki/Movement_tactics, https://nethackwiki.com/wiki/Twoweapon)
-->

迷宮における最も重要な戦闘技術は、「戦うべきではない状況を弁えること」です。2番目に重要な技術は、「いざ戦うと決めたら、確実に、そして痛烈無比な打撃を叩き込むこと」です。

