<!-- audit
2026-05-19:
- rubber hose and bullwhip stats verified; P_WHIP skill (objects.h:374-376, 390-392, skills.h:49)
- bullwhip #apply can disarm (apply.c:3127-3174) and yank from a pit (apply.c:3069-3125)
- rubber hose does NOT damage shades: it's PLASTIC, shade_glare needs SILVER (artifact.c:555-562, weapon.c:307-308)
- rubber hose prob=0: never randomly spawns (objects.h:374-376 WEAPON row, probability field is 0)
- Archeologist starts with bullwhip +1 at Basic (apply.c:2992-2993)
- no whip artifacts
-->
#### 鞭 (Whip) {#whip}

軽量な片手近接武器であり、実用的な道具でもあります。鞭を `#apply`（使用）することで、隣接するモンスターの武器を叩き落としたり（武装解除）、落とし穴から自分自身を引き上げたりできます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| ゴムホース (rubber hose) | 1d4 / 1d3 | 20 | 3 | — | プラスチック | ジョーク武器。自然生成されることはない。キーストン・コップ（お巡りさん）が所持していることがある。 |
| 鞭 (bullwhip) | 1d2 / 1 | 20 | 4 | — | 革 | 考古学者（Archeologist）の初期装備。使用（apply）することで隣接モンスターの武器を叩き落としたり（相手が武器を装備している場合のみ）、落とし穴から脱出するために自身を引き上げることができる（近くの岩、家具、大型モンスターに巻き付ける）。 |

:::
