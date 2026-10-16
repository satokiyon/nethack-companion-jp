#### 渦 `v` (Vortices `v`) {#vortices-v}

<!-- audit
2026-05-19:
- 6 rows (S_VORTEX) sourced from monsters.h:1053-1110.
- Damage types are physical/blinding/cold/shock+drain/fire; NO vortex deals poison.
- Speeds: fog cloud Lvl 3/Spd 1; dust/ice/energy Spd 20; steam/fire Spd 22. Only fog cloud is slow, NOT all stationary. (monsters.h:1052 fog cloud LVL(3,1,...); 1062 dust LVL(4,20,...); 1071 ice LVL(5,20,...); 1081 energy LVL(6,20,...); 1091 steam LVL(7,22,...); 1101 fire LVL(8,22,...))
- Energy vortex: AT_NONE+AD_ELEC passive 0d4 + AD_DREN drain (monsters.h:1081-1090).
- Fire vortex: AT_NONE+AD_FIRE passive 0d4 (monsters.h:1101-1110).
- All carry M1_FLY|M1_MINDLESS|G_NOCORPSE.
-->

火炎、冷気、電撃、あるいは蒸気の渦です。プレイヤーを内部に巻き込み、属性ダメージを連続して与えてきます。魔法防御や対応する属性耐性がないと極めて危険です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 霧の雲 (fog cloud) | 灰色 | 3 | 1 | 0 | 0 | engulf 1d6 | 不定形. |
| ほこりの渦 (dust vortex) | 茶色 | 4 | 20 | 2 | 30 | engulf 2d8 盲目 |  |
| 氷の渦 (ice vortex) | 水色 | 5 | 20 | 2 | 30 | engulf 1d6 冷気 |  |
| エネルギーの渦 (energy vortex) | 明青 | 6 | 20 | 2 | 30 | engulf 1d6 電撃 · engulf 2d6 エナジードレイン-Pw · 反撃 7d4 電撃 |  |
| 蒸気の渦 (steam vortex) | 青色 | 7 | 22 | 2 | 30 | engulf 1d8 火炎 |  |
| 炎の渦 (fire vortex) | 黄色 | 8 | 22 | 2 | 30 | engulf 1d10 火炎 · 反撃 9d4 火炎 |  |

:::
