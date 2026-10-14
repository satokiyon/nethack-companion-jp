#### 吸血鬼 `V` (Vampires `V`)

<!-- audit
2026-05-19:
- 3 vampire rows at monsters.h: vampire 2282, vampire lord 2292, Vlad 2306.
- Vampire and vampire lord carry G_NOCORPSE, but the death handler substitutes an already-old human corpse. Vlad leaves none (mon.c:613-646).
- All have M1_REGEN | M1_FLY plus M2_STALK (follows stairs) and shapeshift via M2_WERE-equivalent vamp branch (mon.c).
- Vampire mage is #if 0 DEFERRED in 5.0 (correctly omitted).
- Vlad inhabits Vlad's Tower; holds the Candelabrum of Invocation (mkobj.c spawn for PM_VLAD).
-->

噛みつき攻撃によってプレイヤーの経験値レベルを吸い取ります（エナジードレイン）。こうもりや霧の雲に変身して逃亡・奇襲を行います。通常の吸血鬼や吸血鬼の貴族は古びた人間の死体を残しますが、ヴラドは死体を残しません。ヴラド公は[ヴラドの塔](#vlads-tower)のボスです。

すべての吸血鬼は飛行し、自動回復し、アンデッドであり、階段に追従し、変身能力を持ちます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 吸血鬼 (vampire) | 赤色 | 10 | 12 | 1 | 25 | 爪 1d6 · 噛みつき 1d6 エナジードレイン-XL | Drops an old 人間 corpse. |
| vampire lord | 青色 | 12 | 14 | 0 | 50 | 爪 1d8 · 噛みつき 1d8 エナジードレイン-XL | Drops an old 人間 corpse. |
| 吸血鬼ヴラド (Vlad the Impaler) | 赤紫 | 28 | 26 | -6 | 80 | 武器攻撃 2d10 · 噛みつき 1d12 エナジードレイン-XL | Vampire boss in Vlad's Tower. Has the Candelabrum. |

:::
