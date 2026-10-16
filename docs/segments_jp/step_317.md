#### 蜘蛛およびサソリ `s` (Spiders and scorpions `s`) {#arachnids-and-centipedes-s}

<!-- audit
2026-05-19:
- 5 rows (cave spider, centipede, giant spider, scorpion, Scorpius) sourced from monsters.h:940-972, 3713-3722.
- Webmaker only on cave spider + giant spider (mondata.h:147-148); M1_CONCEAL on all except giant spider.
- Cave spider/centipede corpses safe (no M1_POIS); giant spider/scorpion corpses poisonous (M1_POIS).
- Scorpius MR_STONE confers stoning resistance via corpse.
-->

洞窟グモや大蠍など、毒針や巣を扱う節足動物です。大蠍の毒針は筋力を急速に低下させるため、解毒手段がない序盤は近接戦を避けるべきです。

すべての蜘蛛およびサソリは毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 洞窟グモ (cave spider) | 灰色 | 1 | 12 | 3 | 0 | 噛みつき 1d2 | 潜伏. |
| ムカデ (centipede) | 黄色 | 2 | 4 | 3 | 0 | 噛みつき 1d3 毒 | 潜伏. |
| 巨大グモ (giant spider) | 赤紫 | 5 | 15 | 4 | 0 | 噛みつき 2d4 毒 | 死体に毒あり. |
| サソリ (scorpion) | 赤色 | 5 | 15 | 3 | 0 | 爪 1d2 ×2 · 毒針 1d4 毒 | 潜伏、死体に毒あり. |
| 大蠍 (Scorpius) | 赤紫 | 15 | 12 | 10 | 0 | 爪 2d6 · 爪 2d6 盗み-魔除け · 毒針 1d4 disease | 死体に毒あり、階段を追跡、石化耐性. |

:::
