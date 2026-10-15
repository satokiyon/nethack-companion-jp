<!-- audit
2026-05-19:
- boomerang stats verified (objects.h:166-168)
- boomerang does NOT always return: 10-step curved path that stops on monster, wall, door, or sink hits (zap.c:4148-4220 boomhit; loop ct<10, breaks on isok, monster, ZAP_POS or closed_door)
- catching the return requires a Dex check, auto-fails if Fumbling; a missed catch hits the thrower
- enchanted boomerang hits (spe+1) times
- useless underwater
-->
#### ブーメラン (Boomerang)

投擲専用。放物線を描いて飛行し、途中の軌道が遮られていなければ投げた本人の手元へ戻ってきます。戻ってきたブーメランをキャッチするには器用 (Dex) の判定が必要です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| ブーメラン (boomerang) | 1d9 / 1d9 | 5 | 20 | — | 木 | 障害物のない経路なら弧を描いて手元に戻る。モンスター、壁、扉、流し台（シンク）に当たると止まる。器用さが低いか、あるいは「お手玉（Fumbling）」状態のときは顔面に直撃してダメージを受ける。 |

:::
