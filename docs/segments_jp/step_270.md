<!-- audit
2026-05-19:
- pick-axe: WEPTOOL, wt 100, cost 50, 1d6/1d3, iron (objects.h:1007-1009)
- mattock stats verified (objects.h:345-347)
- both share P_PICK_AXE skill and route through use_pick_axe (apply.c:4290-4292)
- mattock is bimanual: gets 3/2 Str damage bonus in melee (uhitm.c:1467-1468)
- dig-down creates a pit, then a hole (dig.c:432-433, 372-374)
-->
#### つるはし (Pick-axe)

近接武器かつ掘削道具。`a` (apply) キーで使用することで、任意の方向の壁や床を掘り進めることができます。ドワーフのつるはしも同様の機能を持ち、こちらは両手持ちです。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| つるはし (pick-axe) | 1d6 / 1d3 | 100 | 50 | — | 鉄 | 武器道具（Weapon-tool）。使用（apply）することで壁を掘り崩したり、床を掘り抜く（落とし穴、続いて穴を作成）ことができる。ドワーフのつるはしと同じ `pick-axe` スキル。 |
| ドワーフのつるはし (dwarvish mattock) | 1d12 / 1d8+2d6 | 120 | 50 | −1 | 鉄 | 両手持ち（筋力ダメージ 1.5 倍ボーナス適用）。つるはし同様に壁を掘り崩せる。わずかな命中ペナルティ（−1）。 |

:::
