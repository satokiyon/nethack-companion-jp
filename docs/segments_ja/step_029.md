### 注目の施設・地形 (Points of Interest)


<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Throne positive-Luck kick gives 300-500 gold, not 201-500: rn1(201,300)=rn2(201)+300 (dokick.c:1036; rn1 macro hack.h:1543).
- Verified correct: magic fountain 1/7 restore-all+1, water demon 1/30 & wish-gate, Excalibur dip, altar BUC flashes, all throne effects, the full 28-ring sink table & 19/20 loss, sink kick/quaff/dip tables, vault-guard timer.
-->
<!-- audit
2026-05-22 fountains fact-check:
- magic-fountain placement: mklev.c:2297 mkfountain() rolls !rn2(7) — 1/7 of *randomly placed* fountains; predefined fountains via lua des.feature("fountain",x,y) call lspo_feature (sp_lev.c:4904) which sets FOUNTAIN typ + looted/warned only, never blessedftn — so Minetown, Mine's End, Oracle, Big Room (bigrm-4), Castle, Juiblex's swamp are never magic
- magic-fountain gate: mgkftn && u.uluck >= 0 && fate >= 10 (fountain.c:254); fires on 21/30 quaffs at Luck ≥ 0; "Wow! This makes you feel great!" at fountain.c:257; AMAX restore loop fountain.c:259-263; +1 attr 264-272; flag consumed at fountain.c:275
- sink-kicked fountain blessedftn=0 explicit (do.c:421)
- dipfountain has no blessedftn check; dryup() at fountain.c:232 clears it — dipping a magic fountain can waste the charge if the fountain dries
- curse-some-items (case 24, "This water's no good!"): iterates gi.invent only (fountain.c:312-320), so container contents (bag interior) are safe
- poisonous water (case 21, "The water is contaminated!"): poison_strdmg if no Poison_resistance else losehp(rnd(4),"unrefrigerated sip of juice") (fountain.c:300-307)
- scare-monsters (case 29, "bad breath"): iterates fmon entire-level, monflee each (fountain.c:367-381)
- water demon 1 in 30 (case 23); wish gate rnd(100) > 80 + level_difficulty() (fountain.c:78); level_difficulty in DoD == depth(&u.uz) (dungeon.c:2027); at DL ≥ 20, threshold 100, rnd(100) never > 100, so 0% wish
- Elbereth scares water demons in DoD: onscary excludes only Rodney/lawful-minions/Angels/Riders (monmove.c:243-271); Elbereth disabled in Gehennom/Planes (Inhell || In_endgame, monmove.c:295-302); musical instruments use the auditory_scare=(x=0,y=0) path which BYPASSES the Inhell/In_endgame check (works in Gehennom)
- Wizard random starting items: u_init.c:167-178 has 3 random scrolls (may roll SCR_TAMING) and 1 random spellbook (may roll SPE_CHARM_MONSTER); Wizards do NOT roll random tools so cannot start with magic harp / tooled horn / leather drum
- strategy refs:
  + https://nethackwiki.com/wiki/Fountain — general mechanics; never-magic-fountain list
  + https://nethackwiki.com/wiki/Talk:Water_demon — "double-Elbereth" survival strategy (~97.95% survivable per wiki claim)
  + https://nethackwiki.com/wiki/Fountain_quaffing — early-game wish-fishing strategy, risk discussion
  + http://www.chiark.greenend.org.uk/~damerell/games/magicfountain.txt — Damerell statistical defense; drop items on the fountain tile to avoid make-pool curse; sack interior protected
  + https://www.steelypips.org/nethack/331/foun-331.html — Steelypips fountain spoiler

2026-05-18:
- Fountain quaff: 7 case branches in rnd(30) (fountain.c:286-387)
- Water demon spawn rate: 1 in 30 quaffs (fountain.c:247, 314)
- Shallow wish odds: water demon × rnd(100) > 80 + level_difficulty() ≈ 1/150 (fountain.c:78, 247)
- Wish odds drop to zero past DL 20 (fountain.c:78 level_difficulty term)
- Excalibur dip: lawful + XL ≥ 5 + long sword + quan=1, 1/6 Knight or 1/30 other (fountain.c:404-405)
- Non-lawful Excalibur dip curses the sword and consumes the fountain (fountain.c:411-424)
- Fountain dip cases 17-20 UNCURSE the dipped item (NOT bless) (fountain.c:464-475)
- Altar BUC flash: amber=blessed, black=cursed, no flash=uncursed (do.c:379-389)
- Altar conversion via cross-race sacrifice can flip the altar (pray.c:1717-1736)
- Throne trigger: rnd(6) > 4 = 1 in 3 chance of any effect (sit.c:45)
- Throne effect chosen from rnd(13) outcomes (sit.c:46, 68-209)
- Throne wish (case 6) requires u.uluck + rn2(5) ≥ 0, i.e. non-negative Luck (sit.c:106-110)
- Throne ID: identify_pack(rn2(5)) — 4/5 chance of 1-4 items, 1/5 chance of entire pack (sit.c:198, invent.c:2721)
- Throne can vanish "in a puff of logic" on rn2(3), even when nothing happens (sit.c:224-233)
- Vlad's throne: cases 1-4 grant wish + destroy throne; 5-13 are negatives (sit.c:241-353)
- Kicking sink: 4/5 klunk, else 1/3 black pudding, 1/3 amorous demon, 1/3 ring backup (dokick.c:1201-1238)
- Each kick outcome gated by S_LPUDDING / S_LDWASHER / S_LRING (once per sink) (dokick.c:1209-1232)
- Dip potion of polymorph: sink → fountain/throne/altar/grave (do.c:404-454)
- Grave case may fail and print "The sink vanishes." (engrave.c:1691-1693)
- Dip POT_OBJECT_DETECTION: "You sense a ring lost down the drain" while S_LRING unset (fountain.c:771-776)
- Dip POT_LEVITATION: drops a ring once per sink (fountain.c:767-770, 804-826)
- Dip POT_ACID: "The drain seems less clogged" (fountain.c:755-766)
- Drop ring in sink: searching + slow-digestion are returned to inventory; all others consumed (do.c:507-516)
- Ring of hunger vanishes ALL items on the sink square (do.c:556-570)
- Ring of teleportation moves the sink to a fresh ROOM tile (do.c:575-580)
- Rotten food in fountains is slime molds, not fruit (objnam.c:414-427)
- VAULT_GUARD_TIME = 30 turns (hack.h:69) before the guard appears; "Croesus", "Kroisos", "Creosote" all dismiss the guard if Croesus is still alive (vault.c:513-543); lying with a Lawful character loses one alignment (vault.c:507-511)
2026-05-31:
- Real-name answer: guard demands "Please drop that gold and follow me." then opens a temporary corridor in the wall (the fake-corridor system in vault.c), leads the player out, and re-seals the wall behind. Player loses all carried gold (vault.c:551-585).
- Croesus answer (with Croesus alive): guard says "Oh, yes, of course. Sorry to have disturbed you." and `mongone(guard)` removes him (vault.c:513-543). No corridor opens. Player keeps gold but stays sealed inside.
- Croesus answer with Croesus dead: guard goes hostile and attacks (vault.c:525-540).
- Implication: lying keeps the gold but requires the player to have an independent way out (wand of digging, scroll of teleportation, level teleport, etc.). Truth-telling guarantees escape at the cost of the gold.

地下深くへと潜っていく中で、特別なランドマーク（固定施設）に立ち寄る時間を作りましょう。フロアの随所に散らばるこれらの建造物は、好奇心旺盛な探索者に多大な報酬を与え、時には手痛い罰を下します。
