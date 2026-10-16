#### 軽微な罠 (Nuisance Traps) {#nuisance-traps}
<!-- audit
2026-05-18:
- arrow trap empty-click is 1/15 once `trap->once && trap->tseen` (trap.c:1199, 1228)
- dart trap 1/6 chance the dart is poisoned (trap.c:1273)
- squeaky board skipped by Levitation OR Flying unless forcetrap (trap.c:1419)
- squeaky board wakes monsters: wake_nearby for player, wake_nearto range 40 for monster (trap.c:1436, 1473)
- rust trap default branch (40% via cases 3,4 of rn2(5)) douses lamplit items then cloak else suit else shirt (trap.c:1610, 1632-1643)
- rust trap cases 0/1/2 hit helm, then left-arm chain (shield→weapon→gloves), then right-arm (weapon→gloves) (trap.c:1611-1627)
- missed arrows and darts land via place_object + stackobj — can be farmed (trap.c:1217-1220, 1288-1291)
- mounted player: steed absorbs the hit 50% of the time (trap.c:1211, 1276)
-->

| 罠の種類        | 効果                                                |
| --------------- | --------------------------------------------------- |
| 矢の罠 (Arrow trap)      | あなたに向けて矢を撃ち出す（軽微なダメージ）        |
| ダーツの罠 (Dart trap)   | ダーツを撃ち出す（毒が塗られている場合あり）        |
| 軋む床 (Squeaky board)   | 大きな軋み音を立て、周囲のモンスターを目覚めさせる  |
| 錆の罠 (Rust trap)       | 水を浴びせかける：装備中の鉄製防具を錆びさせ、クローク／鎧／シャツを濡らし、火のついたランプを消火する |

厄介ではありますが、致命傷になることは稀です。不幸中の幸いとして、矢の罠やダーツの罠はタダで投擲・射撃用の弾薬を供給してくれるため、あえて安全に踏み抜いて弾薬をストックするテクニックもあります。
