#### 巨人 `H` (Giant humanoids `H`) {#giant-humanoids-h}

<!-- audit
2026-05-19:
- Frost giant and storm giant melee is AD_PHYS only; cold/shock resistance does NOT reduce damage (monsters.h frost/storm rows at 1748, 1772).
- Fire giant melee is AD_PHYS only; fire resistance does NOT make them weak offensively (monsters.h:1738).
- Cyclops is the Healer quest nemesis (Hea-goal.lua:74, monsters.h:1792-1800), NOT Caveman.
- Surtur does NOT carry Mjollnir (Mjollnir is a Valkyrie quest artifact, artilist.h).
- Ettin and minotaur are NOT M2_GIANT, so their corpses do not grant Str (eat.c:1345; monsters.h:1758, 1782).
- Minotaur roams Gehennom mazes (mkmaze.c:1112, makemon at maze fill), NOT vaults.
-->

巨岩を投げつけてくる怪力の人型生物です。火の巨人、霜の巨人、嵐の巨人はそれぞれの属性ダメージを扱い、その死体を食べることで火炎耐性、冷気耐性、電撃耐性や筋力上昇を獲得できるチャンスがあります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 巨人 (giant) | 赤色 | 6 | 6 | 0 | 0 | 武器攻撃 2d10 |  |
| 岩石巨人 (stone giant) | 灰色 | 6 | 6 | 0 | 0 | 武器攻撃 2d10 |  |
| 丘の巨人 (hill giant) | 水色 | 8 | 10 | 6 | 0 | 武器攻撃 2d8 |  |
| 炎の巨人 (fire giant) | 黄色 | 9 | 12 | 4 | 5 | 武器攻撃 2d10 | 火炎耐性。巨石投げ攻撃。 |
| 吹雪の巨人 (frost giant) | 白色 | 10 | 12 | 3 | 10 | 武器攻撃 2d12 | 冷気耐性。巨石投げ攻撃。 |
| エティン (ettin) | 茶色 | 10 | 12 | 3 | 0 | 武器攻撃 2d8 · 武器攻撃 3d6 |  |
| 雷の巨人 (storm giant) | 青色 | 16 | 12 | 3 | 10 | 武器攻撃 2d12 | 電撃耐性。巨石を投げて大ダメージを与える。 |
| タイタン (titan) | 赤紫 | 16 | 18 | -3 | 70 | 武器攻撃 2d8 · 攻撃呪文 | 飛行。マジックミサイルを放つ頑強な人型生物。呪文を詠唱。 |
| ミノタウロス (minotaur) | 茶色 | 15 | 15 | 6 | 0 | 爪 3d10 ×2 · 頭突き 2d8 | 2回の爪攻撃と頭突き。強打の持ち主でゲヘナの迷宮を徘徊。 |
| サイクロプス (Cyclops) | 灰色 | 18 | 12 | 0 | 0 | 武器攻撃 4d8 ×2 · 爪 2d6 盗み-魔除け | 階段を追跡、石化耐性。治療師のクエスト宿敵。 巨石投げ攻撃。 |
| 支配者スルト (Lord Surtur) | 赤紫 | 15 | 12 | 2 | 50 | 武器攻撃 2d10 ×2 · 爪 2d6 盗み-魔除け | 階段を追跡、火炎耐性、石化耐性。ワルキューレのクエスト宿敵。 |

:::
