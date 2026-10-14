#### フレイル (Flail)
<!-- audit
2026-05-19:
- flail: base 1d6/1d4, +1 small (weapon.c:272-275), +1d4 large (weapon.c:239-243); objects.h:384-386
- grappling hook: 1d2/1d6, WEPTOOL that trains P_FLAIL (objects.h:1010-1012)
- grappling hook #apply pulls target toward you; range 4 (P_NONE/Basic), 5 (Skilled), 8 (Expert+) (apply.c:3686-3698)
- no flail artifact
-->

片手持ちの打撃系近接武器。同じスキルを修練できる実用的な道具として鍵縄（grappling hook）も含まれます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| フレイル (flail / nunchaku: ヌンチャク) | 1d6+1 / 1d4+1d4 | 15 | 4 | — | 鉄 | 小型に+1、大型に+1d4。片手持ち。 |
| 鍵縄 (grappling hook) | 1d2 / 1d6 | 30 | 50 | — | 鉄 | フレイルスキルを修練可能。使用（apply）すると2マス先のアイテムを引き寄せたり、超小型モンスターを引き寄せたり、自分自身を1歩引き寄せることができる。 |

:::
