#### レプラコーン `l` (Leprechauns `l`) {#leprechauns-l}

<!-- audit
2026-05-19:
- Leprechaun (Lvl 5, Spd 15, AC 8, MR 20, green, claw 1d2 AD_SGLD), M1_TPORT, AT_CLAW (not bite): monsters.h:660-666, steal.c:58-115.
- Stolen gold goes into mtmp->minvent and drops on death.
- An unseen leprechaun off the shop floor can bury its gold 1-in-4 per turn (monmove.c:1152-1171 leppie_stash); killing later may not recover it.
-->

金貨を盗んで即座にフロアの別の場所へテレポートする妖精です。攻撃力は高くありませんが、全財産を奪われて逃げられると回収に手間取ります。テレパシーで位置を特定して仕留めれば、大量の金貨を取り戻せます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| レプラコーン (leprechaun) | 緑色 | 5 | 15 | 8 | 20 | 爪 1d2 盗み-gold | テレポート。金貨を盗んでテレポート逃走。近くでは金貨を持ち歩かないこと。 |

:::
