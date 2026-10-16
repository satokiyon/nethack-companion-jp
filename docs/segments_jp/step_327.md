#### ケンタウロス `C` (Centaurs `C`) {#centaurs-c}

<!-- audit
2026-05-19:
- 3 rows (plains/forest/mountain) sourced from monsters.h:1301-1323; complete S_CENTAUR roster.
- Centaurs are half-horse, NOT mounted on a horse. (https://nethackwiki.com/wiki/Centaur)
- Forest centaurs spawn with BOW+arrows; plains and mountain centaurs spawn with CROSSBOW+bolts (50% armed rate per makemon.c:474-484).
-->

上半身が人間、下半身が馬の俊足狩人です。遠距離から弓矢を連射してくるため、通路に誘い込んで射線を切るか、接近して近接戦に持ち込みましょう。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 草原のケンタウロス (plains centaur) | 茶色 | 4 | 18 | 4 | 0 | 武器攻撃 1d6 · 蹴り 1d6 |  |
| 森のケンタウロス (forest centaur) | 緑色 | 5 | 18 | 3 | 10 | 武器攻撃 1d8 · 蹴り 1d6 |  |
| 山のケンタウロス (mountain centaur) | 水色 | 6 | 20 | 2 | 10 | 武器攻撃 1d10 · 蹴り 1d6 ×2 |  |

:::
