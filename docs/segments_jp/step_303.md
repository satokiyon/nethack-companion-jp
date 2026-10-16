#### 目および球体 `e` (Eyes and spheres `e`)

<!-- audit
2026-05-19:
- Roster sourced from monsters.h:325-366 (beholder omitted, `#if 0`).
- Floating eye paralysis requires mutual sight (canseemon + mon->mcansee per uhitm.c:6022-6053), NOT "in daylight."
- Floating eye corpse grants telepathy (eat.c:1071 TELEPAT case).
- No close-eyes command exists in 5.0; to break sight you must be Blind (status or worn blindfold/towel).
- Newbie-killer framing aligned with NetHackWiki: floating eye is "an infamous source of early game deaths" (https://nethackwiki.com/wiki/Floating_eye).
-->

さまよう目の反撃麻痺凝視は、ダンジョン序盤において最も有名な死因の一つです。自由行動（Free action）、盲目状態、または遠距離攻撃の手段を持たずに近接攻撃を仕掛けてはなりません。倒した後は死体を食べてください。恒久的なテレパシー能力（内在能力）を獲得できます。

すべての目および球体は飛行能力を持ちます。また、*さまよう目*を除きすべて精神を持ちません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 包子ガス (gas spore) | 灰色 | 1 | 3 | 10 | 0 | 爆発(死亡時) 4d6 |  |
| さまよう目 (floating eye) | 青色 | 2 | 1 | 9 | 10 | 反撃 3d70 麻痺 | 水陸両用. 互いに視界が通っている状態で近接攻撃すると反撃麻痺。遠距離攻撃を行うか、目隠しやタオルで視覚を遮って対処。死体を食べると必ずテレパシーを獲得。 |
| 氷の球体 (freezing sphere) | 白色 | 6 | 13 | 4 | 0 | 自爆 4d6 冷気 | 冷気耐性. |
| 炎の球体 (flaming sphere) | 赤色 | 6 | 13 | 4 | 0 | 自爆 4d6 火炎 | 火炎耐性. |
| 電撃の球体 (shocking sphere) | 明青 | 6 | 13 | 4 | 0 | 自爆 4d6 電撃 | 電撃耐性. |

:::
