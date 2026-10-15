#### 量子力学士 `Q` (Quantum mechanics `Q`)

<!-- audit
2026-05-19:
- Quantum mechanic teleports you (AD_TLPT, monsters.h:2127); genetic engineer polymorphs you (AD_POLY, monsters.h:2136, new in 5.0 per fixes5-0-0.txt:2696). NOT both teleporting.
- Both have speed 12 (NOT 24), poisonous corpses (M1_POIS), and self-teleport (M1_TPORT).
- Quantum corpse toggles Fast (eat.c:1227); genetic engineer corpse triggers polyself (eat.c:1247).
-->

特殊な爪攻撃を持つ2種類の生物です。**量子力学士 (Quantum mechanic)**は命中時にプレイヤーをランダムな場所へテレポートさせます。**遺伝子工学者 (Genetic engineer)**はプレイヤーを変身（変身(へんげ)）させます。不変（Unchanging）の魔除けや魔法防御がなければ、一撃で別の生物に変えられてしまいます。

両種とも自らランダムにテレポートし、毒のある死体を残します。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 量子物理学者 (quantum mechanic) | 水色 | 7 | 12 | 3 | 10 | 爪 1d4 teleport | Self-テレポート. Corpse toggles intrinsic Fast. |
| 遺伝子工学者 (genetic engineer) | 緑色 | 12 | 12 | 3 | 10 | 爪 1d4 polymorph | Self-テレポート. Corpse triggers polyself. |

:::
