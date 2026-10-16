#### トロール `T` (Trolls `T`) {#trolls-t}

<!-- audit
2026-05-19:
- All 5 troll rows (troll, ice, rock, water, Olog-hai) match monsters.h:2225-2266.
- All carry M1_REGEN | M2_STALK; S_TROLL is is_reviver (mondata.h:170).
- Fire/water/force-bolt do NOT destroy corpses; burn_floor_objects only burns scrolls/spellbooks/slime.
- Trollsbane sets mkcorpstat_norevive (uhitm.c:1906, 4867; mhitm.c:1082).
- Stoning leaves a statue (mon.c:671), so no corpse to revive from.
-->

倒しても一定時間後に死体から自動復活します。確実にトロールの息の根を止めるには、**復活する前に死体を食べる**、缶詰作成道具で缶詰にする、あるいは火炎の杖や火炎の魔法で死体を焼き尽くす必要があります。

すべてのトロールは自動回復能力を持ち、階段の上り下りにも追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| トロル (troll) | 茶色 | 7 | 12 | 4 | 0 | 武器攻撃 4d2 · 爪 4d2 · 噛みつき 2d6 |  |
| 氷のトロル (ice troll) | 白色 | 9 | 10 | 2 | 20 | 武器攻撃 2d6 · 爪 2d6 冷気 · 噛みつき 2d6 | 冷気耐性. |
| 岩のトロル (rock troll) | 水色 | 9 | 12 | 0 | 0 | 武器攻撃 3d6 · 爪 2d8 · 噛みつき 2d6 |  |
| 水のトロル (water troll) | 青色 | 11 | 14 | 4 | 40 | 武器攻撃 2d8 · 爪 2d8 · 噛みつき 2d6 | 遊泳. |
| Olog-hai | 赤紫 | 13 | 12 | -4 | 0 | 武器攻撃 3d6 · 爪 2d8 · 噛みつき 2d6 |  |

:::
