#### コカトリス `c` (Cockatrices `c`)

<!-- audit
2026-05-19:
- 3 rows (chickatrice/cockatrice/pyrolisk) sourced from monsters.h:167-195.
- Chickatrice/cockatrice carry MR_POISON|MR_STONE; pyrolisk carries MR_POISON|MR_FIRE and does NOT stone. (monsters.h:174-175 chickatrice, 182-183 cockatrice both MR_POISON|MR_STONE; 191-192 pyrolisk MR_POISON|MR_FIRE; pyrolisk attacks are AT_GAZE AD_FIRE + AT_BITE AD_PHYS — no AD_STON)
- Wielding cockatrice corpse bare-handed instapetrifies regardless of role (wield.c:146-152).
-->

中世の動物寓話に登場する怪物。蛇の尾を持つ鶏の姿をしており、その接触は肉体を瞬時に石化させます。トカゲの死体を常時携帯し、必ず手袋を着用して戦ってください。どの職業も初期状態では石化耐性を持っておらず、コカトリスの死体を素手で装備すると即死します。[石化](#petrification-stoning)の項目を参照してください。

すべてのコカトリス類は毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| チカトリス (chickatrice) | 茶色 | 4 | 4 | 8 | 30 | 噛みつき 1d2 · 接触 石化 · 反撃 石化 | 石化耐性. 小型のコカトリス。同様の石化ルールが適用される。 |
| コカトリス (cockatrice) | 黄色 | 5 | 6 | 6 | 30 | 噛みつき 1d3 · 接触 石化 · 反撃 石化 | 石化耐性. 触れると石化。常にトカゲの死体を携帯すること。 |
| ピロリスク (pyrolisk) | 赤色 | 6 | 6 | 6 | 30 | 凝視 2d6 火炎 · 噛みつき 1d6 | 火炎耐性. |

:::
