#### 斧 (Axe)
<!-- audit
2026-05-19:
- axe 1d6/1d4, battle-axe 1d8+1d4 small / 1d6+2d4 large with bonus dice (objects.h:236-241, weapon.c:251-289)
- both use P_AXE skill; battle-axe is bimanual and gets 3/2 Str damage bonus in melee (uhitm.c:1467-1468)
- Cleaver is the BATTLE_AXE artifact (artilist.h:114-116)
-->

近接武器。通常の斧は片手持ちです。戦斧（battle-axe）は両手持ち（筋力ダメージ 1.5 倍ボーナス適用）となります。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 斧 (axe) | 1d6 / 1d4 | 60 | 8 | — | 鉄 |  |
| 戦斧 (battle-axe) | 1d8+1d4 / 1d6+2d4 | 120 | 40 | — | 鉄 | 両手持ち（5.0の筋力ダメージ 1.5 倍ボーナス適用）。小型に+1d4、大型に+2d4。野蛮人（Barbarian）のクエストアーティファクトである**なた (Cleaver)** は戦斧が母体。 |

:::
