### 迷宮の地形と構造 (The Lay of the Land) {#the-lay-of-the-land}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source: no corrections. Verified DoD depths, all branch placements, Gehennom & Elemental Planes ordering (dungeon.lua), Sokoban/Orcus prizes, Big Room 40%, map symbols.
-->
<!-- audit
2026-05-21:
- branch staircases render with the S_brupstair / S_brdnstair symbols in CLR_YELLOW (defsym.h:124-125)
- the brupstair / brdnstair glyph is only selected after known_branch_stairs is true: the stair leads to a different dungeon AND the hero has traversed it (stairs.c:180-183, display.c:2347-2354)
2026-05-18:
- DoD is 25-29 levels (rn1(5,25) = rn2(5)+25) (dungeon.lua:10-11, hack.h:1535)
- Gnomish Mines branch DL 2-4 (dungeon.lua:15-19)
- Oracle DL 5-9 (dungeon.lua:60-66)
- Sokoban entry is one level above the Oracle, going up (dungeon.lua:20-25)
- 4 Sokoban levels with 2 fixed variants each (dat/soko*.lua)
- Big Room 40% chance, DL 10-12 (dungeon.lua:66-73)
- Quest portal DL 11-16 (dungeon.lua:26-31; chainlevel oracle base=6 range=2)
- Rogue Level DL 15-18 (dungeon.lua:52-58)
- Fort Ludios portal placed at any DL 11 up to just above Medusa, 1/3 per qualifying level (mklev.c:2647-2651)
- Medusa DL ~21-25 (dungeon.lua:74-80)
- Castle at bottom of DoD, DL ~27 (dungeon.lua:81-83)
- Mine's End: 3 variants, all guarantee a not-cursed luckstone (minend-1.lua:77, minend-2.lua:116, minend-3.lua:67)
- 7 Minetown variants; 1-in-7 is Orcish Town (minetn-1.lua, dungeon.lua:179-184)
- 5.0 sink glyph is white `{`, shared with bright-blue fountain (defsym.h:133, fixes5-0-0.txt:827)
- Travel/farlook matches on displayed symbol; `#` no longer cycles to sinks (getpos.c:1046-1062)
- Trap room places 1 randomly chosen trap type from 8 (themerms.lua:101-114)
- Teleportation hub places 2-4 fixed-destination teleporters (themerms.lua:264-279)
- Fake Delphi is a geometric joke: empty room within an Oracle-shaped room, no monsters (themerms.lua:291-305)
- Light source room places exactly one lit oil lamp (themerms.lua:204-210)
- Massacre places 5-25 role corpses only — no wraith (themerms.lua:172-189)
- Mausoleum places one waiting M/V/L/Z monster or one @ corpse (themerms.lua:419-443)
-->

脅威の迷宮の構造はゲームごとに毎回新しく生成されますが、各分岐ダンジョン、特殊フロア、そして大まかな階層の深さは常に一定です。その全体の骨格を把握していれば、次に何が待ち受けているかを常に予測することができます。
