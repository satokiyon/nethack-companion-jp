#### 錆の怪物および魔法中和者 `R` (Rust monsters and disenchanters `R`) {#rust-monsters-and-disenchanters-r}

<!-- audit
2026-05-19:
- Rust monster active attack erodes worn iron armor (uhitm.c:2311); passive damages weapon when you hit it; greased weapons consume a charge instead. Silver/mithril/wood weapons immune (is_rustprone).
- Disenchanter active claw drains armor first (uhitm.c:3611-3644, some_armor + rn2(5) for rings/amulet/blindfold); weapon drain is passive-only.
- Active threat for both is armor, NOT weapons (e.g. long sword).
-->

錆の怪物は接触時に鉄製の武器や防具を急速に錆びさせます。ディスエンチャンター（吸魔の怪物）は命中時に装備している防具や武器の強化値（+値）を吸い取って低下させます。油を塗った防具や、魔法防御、木製・銀製・革製の装備で対抗してください。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 錆の怪物 (rust monster) | 茶色 | 5 | 18 | 2 | 0 | 接触 錆び ×2 · 反撃 錆び | 遊泳。接触で鉄を錆びさせる。戦う前に鎧を脱ぐか銀製武器を使用すること。 |
| 吸魔の怪物 (disenchanter) | 青色 | 12 | 12 | -10 | 0 | 爪 4d4 disenchant · 反撃 disenchant | ゲヘナ限定出現。能動攻撃で防具が劣化し、近接攻撃を仕掛けると反撃で武器が劣化する。 |

:::
