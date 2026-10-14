#### 第1階層・バージョンA (Level 1, Version A) {.sokoban-level data-width=14 data-height=13}
<!-- audit
2026-05-19:
- Scrolls land at spoiler (3,12) and (4,12); lua coords (02,11) and (03,11) (soko4-1.lua:94-95).
- Spoiler-to-lua mapping: lua_xy+1 = spoiler_col, row.
- Level flags noteleport, hardfloor, sokoban, solidify, premapped set (soko4-1.lua:38).
- All 19 push steps verified against soko4-1.lua by simulation.
- Final remainder (boulder A) is exact.
-->

```
            11111
   12345678901234
 1 ┌────┐  ┌───┐
 2 │····│  │···│
 3 │·A··└──┘·B·│
 4 │·C······D··│
 5 │··┌─┐@┌─┐E·│
 6 ├──┴─┴─┼─┘·─┴┐
 7 │·^·^·<│·····│
 8 │·^┌───┤F····│
 9 └┐^│   │·G···│
10  │↑└───┘·H···│
11  │^^^^^←I·J··│
12  │··┌────────┘
13  └──┘
```

1. A を右へ1マス押す。
2. C を上へ1マス押す。
3. D を右へ1マス押す。
4. D を左へ (4,4) まで押す。
5. E を下へ (11,8) まで押す。

この時点でマップは以下のようになります：

```
            11111
   12345678901234
 1 ┌────┐  ┌───┐
 2 │····│  │···│
 3 │·CA·└──┘·B·│
 4 │··D········│
 5 │··┌─┐>┌─┐··│
 6 ├──┴─┴─┼─┘·─┴┐
 7 │·^·^·<│··@··│
 8 │·^┌───┤F·E··│
 9 └┐^│   │·G···│
10  │↑└───┘·H···│
11  │^^^^^←I·J··│
12  │··┌────────┘
13  └──┘
```

6. H を左へ1マス押す。
7. I, J, E, G, H, F, B, D, C の順に穴を埋める。

巨岩が1個（A）残ります。(3,12) と (4,12) に落ちている巻物は大地の巻物です。

