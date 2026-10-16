#### ジャバウォック `J` (Jabberwocks `J`) {#jabberwocks-j}

<!-- audit
2026-05-19:
- Jabberwock: L15 Spd12 AC-2 MR50, 4x 2d10 attacks, M1_FLY, G_GENO|1 (monsters.h:1806-1814).
- Speed 12 is player baseline, NOT slow; most dragons are speed 9 (slower).
- Vorpal Blade auto-beheads PM_JABBERWOCK, short-circuiting the dieroll==1 check (artifact.c:1595-1623).
- Deferred "vorpal jabberwock" at monsters.h:1816-1824 is wrapped in `#if 0` and correctly excluded.
-->

ルイス・キャロルの詩『ジャバウォックの詩』に登場する獰猛な怪物。プレイヤーと同等の速度で移動し、鋭い爪と噛みつきによる連続攻撃を繰り出してきます。十分なACと武器強化が整うまでは警戒が必要です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ジャバウォック (jabberwock) | 橙色 | 15 | 12 | -2 | 50 | 噛みつき 2d10 ×2 · 爪 2d10 ×2 | 飛行. Four heavy attacks; baseline speed. |

:::
