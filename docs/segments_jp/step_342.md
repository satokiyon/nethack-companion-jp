#### ヘビ `S` (Snakes `S`) {#snakes-s}

<!-- audit
2026-05-19:
- 6 snake rows at monsters.h:2167-2221: garter 2167, snake 2174, water moccasin 2182, python 2190, pit viper 2204, cobra 2213.
- "Pit viper" is the snake, NOT "pit fiend" (pit fiend is a `&` major demon at monsters.h:3104-3112).
- M1_SWIM universal across the section; M1_CONCEAL on all except python.
- Python has an AT_TUCH plus AT_HUGS pair (monsters.h:2193-2199), wrap and crush.
- Cobra AT_SPIT/AD_BLND blind at monsters.h:2218 (blind spit out to 6 squares).
-->

大半が猛毒を持っています。クサリヘビ（マムシ）やコブラは致命的な毒を持ち、ガータースネークなどは無害な獲物です。

すべてのヘビは遊泳能力を持ち、*ニシキヘビ (python)* を除いて潜伏能力を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 小さなヘビ (garter snake) | 緑色 | 1 | 8 | 8 | 0 | 噛みつき 1d2 |  |
| ヘビ (snake) | 茶色 | 4 | 15 | 3 | 0 | 噛みつき 1d6 毒 | 死体に毒あり、毒耐性. |
| 水ヘビ (water moccasin) | 赤色 | 4 | 15 | 3 | 0 | 噛みつき 1d6 毒 | 死体に毒あり、毒耐性. |
| ニシキヘビ (python) | 赤紫 | 6 | 3 | 5 | 0 | 噛みつき 1d4 · 接触 · 締め付け 1d4 巻きつき · 締め付け 2d4 |  |
| ハブ (pit viper) | 青色 | 6 | 15 | 2 | 0 | 噛みつき 1d4 毒 ×2 | 死体に毒あり、毒耐性. |
| コブラ (cobra) | 青色 | 6 | 18 | 2 | 0 | 噛みつき 2d4 毒 · 吐瀉 盲目 | 死体に毒あり、毒耐性. |

:::
