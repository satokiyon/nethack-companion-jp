#### 大悪魔 `&` (Major demons `&`)

<!-- audit
2026-05-19:
- Bone devil, Orcus, Geryon "sting 2d4" and Baalzebub "bite 2d6" cells are AD_DRST drain-Str, NOT AD_POISON (monsters.h:2999, 3082, 3093, 3112).
- Poison resistance protects against these Strength-draining attacks.
-->

強力無比な大悪魔たちです。多くは同胞の悪魔を呼び出すゲート召喚能力を持ちます（1体の有刺デビルが瞬く間に5体に増えることもあります）。銀の武器やデーモンベインが特効の大ダメージを与えます。ゲリュオン、ディスパテル、ベルゼブブ、アスモデウスのみが賄賂（金貨）による停戦に応じますが、エクスカリバーやデーモンベインを構えているときは交渉に応じません。

すべて階段の上り下りに追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 水の魔神 (water demon) | 青色 | 8 | 12 | -4 | 30 | 武器攻撃 1d3 · 爪 1d3 · 噛みつき 1d3 | 遊泳, demonic. |
| [amorous demon](#seduction) | 灰色 | 6 | 12 | 0 | 70 | seduction (see Seduction) | 飛行, demonic. Displays as succubus or incubus by the 悪魔's own randomly-assigned gender. |
| 角のある悪魔 (horned devil) | 茶色 | 6 | 9 | -5 | 50 | 武器攻撃 1d4 · 爪 1d4 · 噛みつき 2d3 · 毒針 1d3 | demonic. |
| イリニス (erinys) | 赤色 | 7 | 12 | 2 | 30 | 武器攻撃 2d4 Str-エナジードレイン | 火炎耐性, 毒耐性. Grows stronger as your alignment record falls, gaining harder blows, flight, regeneration, and a second attack. |
| 棘の悪魔 (barbed devil) | 赤色 | 8 | 12 | 0 | 35 | 爪 2d4 · 爪 2d4 sticky · 毒針 3d4 | demonic. |
| マリリス (marilith) | 赤色 | 7 | 12 | -6 | 80 | 武器攻撃 2d4 ×2 · 爪 2d4 ×4 | sees-不可視, demonic. |
| ヴァロック (vrock) | 緑色 | 8 | 12 | 0 | 50 | 爪 1d4 ×2 · 爪 1d8 ×2 · 噛みつき 1d6 | demonic. |
| ヘズロウ (hezrou) | 緑色 | 9 | 6 | -2 | 55 | 爪 1d3 ×2 · 噛みつき 4d4 | demonic. |
| 骨の悪魔 (bone devil) | 灰色 | 9 | 15 | -1 | 40 | 武器攻撃 3d4 · 毒針 2d4 エナジードレイン-Str | demonic. |
| 氷の悪魔 (ice devil) | 白色 | 11 | 6 | -4 | 55 | 爪 1d4 ×2 · 噛みつき 2d4 · 毒針 3d4 冷気 · 接触 1d1 slow | sees-不可視, demonic. |
| ナルフェシニ (nalfeshnee) | 赤色 | 11 | 9 | -1 | 65 | 爪 1d4 ×2 · 噛みつき 2d4 · cast spell | demonic. |
| 穴の悪霊 (pit fiend) | 赤色 | 13 | 6 | -3 | 65 | 武器攻撃 4d2 ×2 · 締め付け 2d4 | sees-不可視, demonic. |
| サンデスティン (sandestin) | 灰色 | 13 | 12 | 4 | 60 | 武器攻撃 2d6 ×2 | shapeshifter, 石化耐性. |
| バルログ (balrog) | 赤色 | 16 | 5 | -2 | 75 | 武器攻撃 8d4 · 武器攻撃 4d6 | 飛行, sees-不可視, demonic. |
| ジョウビレックス (Juiblex) | 明緑 | 50 | 3 | -7 | 65 | engulf 4d10 disease · 吐瀉 3d6 酸 | 飛行, 水陸両用, 不定形, sees-不可視, demonic, 火炎耐性, 毒耐性, 酸耐性, 石化耐性. |
| イーノグ (Yeenoghu) | 赤紫 | 56 | 18 | -5 | 80 | 武器攻撃 3d6 · 武器攻撃 2d8 confuse · 爪 1d6 麻痺 · cast 2d6 魔法 | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| オーケス (Orcus) | 赤紫 | 66 | 9 | -6 | 85 | 武器攻撃 3d6 · 爪 3d4 ×2 · cast 8d6 spell · 毒針 2d4 エナジードレイン-Str | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| ゲーリュオーン (Geryon) | 赤紫 | 72 | 3 | -3 | 75 | 爪 3d6 ×2 · 毒針 2d4 エナジードレイン-Str | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| ディスペータ (Dispater) | 赤紫 | 78 | 15 | -2 | 80 | 武器攻撃 4d6 · cast 6d6 spell | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| ベルゼブブ (Baalzebub) | 赤紫 | 89 | 9 | -5 | 85 | 噛みつき 2d6 エナジードレイン-Str · 凝視 2d6 stun | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| アスモデウス (Asmodeus) | 赤紫 | 105 | 12 | -7 | 90 | 爪 4d4 · cast 6d6 冷気 | 飛行, sees-不可視, demonic, 火炎耐性, 冷気耐性, 毒耐性. |
| デモゴルゴン (Demogorgon) | 赤紫 | 106 | 15 | -8 | 95 | cast 8d6 spell · 毒針 1d4 エナジードレイン-XL · 爪 1d6 disease ×2 | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| デス (Death) | 明紫 | 30 | 12 | -5 | 100 | 接触 8d8 death ×2 | 飛行, 自動回復, sees-不可視, teleport-control. Rider of the Apocalypse. Vanquish three to ascend. |
| ペスティレンス (Pestilence) | 明紫 | 30 | 12 | -5 | 100 | 接触 8d8 pestilence ×2 | 飛行, 自動回復, sees-不可視, teleport-control. Rider; spreads disease. |
| フェミン (Famine) | 明紫 | 30 | 12 | -5 | 100 | 接触 8d8 famine ×2 | 飛行, 自動回復, sees-不可視, teleport-control. Rider; drains nutrition to starvation. |
| メイルデーモン (mail daemon) | 明青 | 56 | 24 | 10 | 127 | — | 飛行, 遊泳, sees-不可視, starts peaceful, 火炎耐性, 冷気耐性, 睡眠耐性, 電撃耐性, 毒耐性, 石化耐性. Appears only to deliver in-game mail, then leaves. |
| 風のジン (djinni) | 黄色 | 7 | 12 | 4 | 30 | 武器攻撃 2d8 | 飛行, 毒耐性, 石化耐性. |
| フヘトトルの使い (Minion of Huhetotl) | 橙色 | 16 | 12 | -2 | 75 | 武器攻撃 8d4 · 武器攻撃 4d6 · cast spell · 爪 2d6 盗み-amulet | 飛行, sees-不可視, demonic. |
| ナルゾク (Nalzok) | 橙色 | 16 | 12 | -2 | 85 | 武器攻撃 8d4 · 武器攻撃 4d6 · cast spell · 爪 2d6 盗み-amulet | 飛行, sees-不可視, demonic. |

:::
