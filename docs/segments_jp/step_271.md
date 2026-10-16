#### こん棒 (Club) {#club}
<!-- audit
2026-05-19:
- club and aklys stats verified (objects.h:371-373, 381-383)
- starting inventory uses blessorcurse(otmp, 10): roughly 10% chance any starter item is cursed (mkobj.c:876-885)
- club is a Caveman starter
- aklys returns when thrown only if wielded (W_WEP), with ~1% misfire (dothrow.c:30-34, 1710-1759)
-->

打撃系の片手近接武器。アキリスは革紐で繋がれており、主武器として手に持った状態で投擲すると手元に戻ってきます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| こん棒 (club) | 1d6 / 1d3 | 30 | 3 | — | 木 | 洞窟人（Caveman）の初期装備。 |
| アキリス (aklys) | 1d6 / 1d3 | 15 | 4 | — | 鉄 | 主武器として装備中に投げると手元に戻ってくる（紐付き）。ごく稀に投げ損ない（不発）が発生する。 |

:::
