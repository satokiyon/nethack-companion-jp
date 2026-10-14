#### 第1階層・バージョンB (Level 1, Version B) {.sokoban-level data-width=15 data-height=11}
<!-- audit
2026-05-19:
- Map walls/floors and all 12 boulders A-L match soko4-2.lua:9-21, 29-42.
- Upstair (2,2), branch portal (4,2) (soko4-2.lua).
- 10 pits: 5 at col 2 rows 3-7, plus 5 at row 9 cols 2-6 (soko4-2.lua:48-59).
- 2 rolling-boulder traps at (1,7) and (6,8) (soko4-2.lua:53, 60).
- 2 always-scrolls-of-earth at (2,10) and (3,10) (soko4-2.lua:63-64).
- Level flags noteleport, hardfloor, sokoban, solidify, premapped (soko4-2.lua:7).
- All 16 solution steps land on lua floor with cardinal approach squares.
- Final remainder (boulders D and E) is exact.
-->


```
            111111
   123456789012345
 1 ┌─┬────┐ ┌────┐
 2 │<│@···└─┘····│
 3 │^├┐·AB····C··│
 4 │^││··DE│·F·G·│
 5 │^││····│·····│
 6 │^├┴───┬┘H────┤
 7 │^│    │······│
 8 │↑└────┘······│
 9 │^^^^^←IJKL···│
10 │··┌───┐······│
11 └──┘   └──────┘
```

1. A を下へ1マス押す。
2. B を右へ (11,3) まで押す。
3. H を下へ (10,8) まで押す。
4. J を上へ1マス押す。
5. I を埋める。
6. L を上へ1マス押す。
7. K, J, H, L の順に穴を埋める。

この時点でマップは以下のようになります：

```
            111111
   123456789012345
 1 ┌─┬────┐ ┌────┐
 2 │<│>···└─┘····│
 3 │^├┐······BC··│
 4 │^││·ADE│·F·G·│
 5 │^││····│·····│
 6 │^├┴───┬┘·────┤
 7 │^│    │······│
 8 │↑└────┘······│
 9 │@····←·······│
10 │··┌───┐······│
11 └──┘   └──────┘
```

8. C を下へ1マス押す。
9. B を左へ (6,3) まで押す。
10. G を下へ1マス押し、次に左へ (10,5) まで押す。
11. G を埋める。
12. C と F を G と同様に埋める。
13. B を右へ (11,3) まで動かし、次に下へ2マス、次に左へ (10,5) まで押す。
14. B を埋める。
15. A を上へ1マス動かす。
16. A を B と同様に埋める。

巨岩が2個（D と E）残ります。(2,10) と (3,10) に落ちている巻物は大地の巻物です。

