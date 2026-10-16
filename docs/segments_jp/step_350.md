#### 人間およびエルフ `@` (Humans and elves `@`)

<!-- audit
2026-05-19:
- 43 human rows match monsters.h.
- Kops are class K, NOT @.
- Wizard of Yendor row: bright-magenta, L30 Spd12 AC-8 MR100, claw 2d12 steal-amulet + spell, flies/regen/sees-invis/fire-res/poison-res, covetous (monsters.h:2847-2858).
- Master of Thieves is the Rogue quest LEADER (Rog-strt.lua:106) AND the Tourist quest nemesis (Tou-goal.lua:117, monsters.h:3564), NOT the Rogue quest nemesis.
- Master Assassin is the primary Rogue quest nemesis (Rog-goal.lua:72), NOT a backup.
-->

`@` のシンボルだけで相手を判断してはなりません。平和的な店主、僧侶、番兵、クエストリーダーであることもあれば、メデューサ、各職業のネメシス、富豪クロイソス、あるいはイェンダーの魔法使いである可能性もあります。動く前に対象の名前を必ず確認してください。このクラスには兵士、忍者、ドッペルゲンガー、獣人、冒険者、そしてプレイヤー自身も含まれます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 人間 (human) | 白色 | 0 | 12 | 10 | 0 | 武器攻撃 1d6 |  |
| ねずみ人間 (wererat) | 茶色 | 2 | 12 | 10 | 10 | 武器攻撃 2d4 | 自動回復. 死体を残さない。 |
| ジャッカル人間 (werejackal) | 赤色 | 2 | 12 | 10 | 10 | 武器攻撃 2d4 | 自動回復. 死体を残さない。 |
| 狼人間 (werewolf) | 橙色 | 5 | 12 | 10 | 20 | 武器攻撃 2d4 | 自動回復. 死体を残さない。 |
| エルフ (elf) | 白色 | 0 | 12 | 10 | 2 | 武器攻撃 1d8 | sees-不可視. |
| Woodland-elf | 緑色 | 4 | 12 | 10 | 10 | 武器攻撃 2d4 | sees-不可視. |
| Green-elf | 明緑 | 5 | 12 | 10 | 10 | 武器攻撃 2d4 | sees-不可視. |
| Grey-elf | 灰色 | 6 | 12 | 10 | 10 | 武器攻撃 2d4 | sees-不可視. |
| elf-lord | 明青 | 8 | 12 | 10 | 20 | 武器攻撃 2d4 ×2 | sees-不可視. |
| Elvenking | 赤紫 | 9 | 12 | 10 | 25 | 武器攻撃 2d4 ×2 | sees-不可視. |
| ドッペルゲンガー (doppelganger) | 白色 | 9 | 12 | 5 | 20 | 武器攻撃 1d12 | shapeshifter. |
| 店主 (shopkeeper) | 白色 | 12 | 16 | 0 | 50 | 武器攻撃 4d4 ×2 | starts peaceful. Don't anger one. |
| 番兵 (guard) | 青色 | 12 | 12 | 10 | 40 | 武器攻撃 4d10 | starts peaceful. |
| 囚人 (prisoner) | 白色 | 12 | 12 | 10 | 0 | 武器攻撃 1d6 | starts peaceful. |
| 賢者 (Oracle) | 明青 | 12 | 0 | 0 | 50 | 反撃 13d4 魔法 | starts peaceful. |
| priest | 白色 | 12 | 12 | 10 | 50 | 武器攻撃 4d10 · 蹴り 1d4 · cast cleric | starts peaceful. Temple defenders. Convert their altars or sacrifice on them. |
| high priest | 白色 | 25 | 15 | 7 | 70 | 武器攻撃 4d10 · 蹴り 2d8 · cast 2d8 cleric ×2 | sees-不可視. Endgame altar guardian. Don't fight one head-on. |
| 兵士 (soldier) | 灰色 | 6 | 10 | 10 | 0 | 武器攻撃 1d8 | follows stairs. |
| 下士官 (sergeant) | 赤色 | 8 | 10 | 10 | 5 | 武器攻撃 2d6 | follows stairs. |
| 看護婦 (nurse) | 白色 | 11 | 6 | 0 | 0 | 爪 2d6 heal |  |
| 副官 (lieutenant) | 緑色 | 10 | 10 | 10 | 15 | 武器攻撃 3d4 ×2 | follows stairs. |
| 指揮官 (captain) | 青色 | 12 | 10 | 10 | 15 | 武器攻撃 4d4 ×2 | follows stairs. |
| 見張り (watchman) | 灰色 | 6 | 10 | 10 | 0 | 武器攻撃 1d8 | follows stairs, starts peaceful. |
| 見張りの隊長 (watch captain) | 緑色 | 10 | 10 | 10 | 15 | 武器攻撃 3d4 ×2 | follows stairs, starts peaceful. |
| メデューサ (Medusa) | 明緑 | 20 | 12 | 2 | 50 | 武器攻撃 2d4 · 爪 1d8 · 凝視 石化 · 噛みつき 1d6 毒 | 飛行, 遊泳, 水陸両用, 死体に毒あり. |
| イェンダーの魔法使い (Wizard of Yendor) | 明紫 | 30 | 12 | -8 | 100 | 爪 2d12 盗み-amulet · cast spell | 飛行, 自動回復, sees-不可視, 火炎耐性, poison-res. Covetous: テレポート to you in late Gehennom and on the planes. The final boss. |
| クロイソス (Croesus) | 赤紫 | 20 | 15 | 0 | 40 | 武器攻撃 4d10 | sees-不可視, follows stairs. Vault guardian on Fort Ludios. Wields a two-handed sword and hoards gold, gems, and magic items off the floor. |
| 考古学者 (archeologist) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 | tunnels. |
| 野蛮人 (barbarian) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| caveman | 白色 | 10 | 12 | 10 | 0 | 武器攻撃 2d4 |  |
| 治療師 (healer) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 |  |
| 騎士 (knight) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| 武闘家 (monk) | 白色 | 10 | 12 | 10 | 2 | 爪 1d8 · 蹴り 1d8 |  |
| priest | 白色 | 10 | 12 | 10 | 2 | 武器攻撃 1d6 · cast cleric | Temple defenders. Convert their altars or sacrifice on them. |
| レンジャー (ranger) | 白色 | 10 | 12 | 10 | 2 | 武器攻撃 1d4 |  |
| 盗賊 (rogue) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| 侍 (samurai) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d8 ×2 |  |
| 観光客 (tourist) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| ワルキューレ (valkyrie) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d8 ×2 |  |
| 魔法使い (wizard) | 白色 | 10 | 12 | 10 | 3 | 武器攻撃 1d6 · cast spell |  |
| カーナボン卿 (Lord Carnarvon) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 4d8 spell | tunnels, starts peaceful. Archeologist quest leader. |
| ペリアス (Pelias) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful. Barbarian quest leader. |
| 呪術師カルノフ (Shaman Karnov) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 2d8 cleric | starts peaceful. Cave Dweller quest leader. |
| ヒポクラテス (Hippocrates) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 1d6 · cast 3d8 cleric ×2 | starts peaceful. Healer quest leader. |
| アーサー王 (King Arthur) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful. Knight quest leader. Holds Excalibur if you didn't get it. |
| 総師範 (Grand Master) | 黒色 | 25 | 15 | 0 | 90 | 爪 4d10 · 蹴り 2d8 · cast 2d8 cleric ×2 | sees-不可視, starts peaceful. Monk quest leader. |
| 主席司祭 (Arch Priest) | 白色 | 25 | 15 | 7 | 90 | 武器攻撃 4d10 · 蹴り 2d8 · cast 2d8 cleric ×2 | sees-不可視, starts peaceful. Priest quest leader. |
| 勇者オリオン (Orion) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 4d8 spell | 遊泳, 水陸両用, sees-不可視, starts peaceful. Ranger quest leader. Bow user. |
| 盗賊の頭領 (Master of Thieves) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · 武器攻撃 2d6 · 爪 2d4 盗み-amulet | starts peaceful. Rogue quest leader; also Tourist quest nemesis. |
| 大名佐藤 (Lord Sato) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful. Samurai quest leader. |
| ツーフラワー (Twoflower) | 白色 | 20 | 15 | 10 | 90 | 武器攻撃 4d10 | starts peaceful. Tourist quest leader. |
| ノルン (Norn) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful, 冷気耐性. Valkyrie quest leader. |
| 緑のネフェレト (Neferet the Green) | 緑色 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 2d8 spell ×2 | starts peaceful. Wizard quest leader. |
| トート・アモン (Thoth Amon) | 赤紫 | 16 | 12 | 0 | 10 | 武器攻撃 1d6 · cast spell ×2 · 爪 1d4 盗み-amulet | follows stairs. Barbarian quest nemesis. |
| カエン (Master Kaen) | 赤紫 | 25 | 12 | -10 | 10 | 爪 16d2 ×2 · cast cleric · 爪 1d4 盗み-amulet | sees-不可視, follows stairs. Monk quest nemesis. |
| 暗殺者の頭領 (Master Assassin) | 赤紫 | 15 | 12 | 0 | 30 | 武器攻撃 2d6 毒 · 武器攻撃 2d8 · 爪 2d6 盗み-amulet | follows stairs. Rogue quest nemesis. |
| 足利尊氏 (Ashikaga Takauji) | 赤紫 | 15 | 12 | 0 | 40 | 武器攻撃 2d6 ×2 · 爪 2d6 盗み-amulet | follows stairs. Samurai quest nemesis. |
| 暗きもの (Dark One) | 黒色 | 15 | 12 | 0 | 80 | 武器攻撃 1d6 ×2 · 爪 1d4 盗み-amulet · cast spell | follows stairs. Wizard quest nemesis. |
| 学生 (student) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 | tunnels, starts peaceful. |
| 首領 (chieftain) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 | starts peaceful. |
| ネアンデルタール人 (neanderthal) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 2d4 | starts peaceful. |
| 随行員 (attendant) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 | starts peaceful. |
| 小姓 (page) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 ×2 | starts peaceful. |
| 師範 (abbot) | 白色 | 5 | 12 | 10 | 20 | 爪 8d2 · 蹴り 3d2 stun · cast cleric | starts peaceful. |
| 侍者 (acolyte) | 白色 | 5 | 12 | 10 | 20 | 武器攻撃 1d6 · cast cleric | starts peaceful. |
| ハンター (hunter) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d4 | sees-不可視, starts peaceful. |
| ちんぴら (thug) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 ×2 | starts peaceful. |
| 忍者 (ninja) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d8 ×2 |  |
| 浪士 (roshi) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d8 ×2 | starts peaceful. |
| ガイド (guide) | 白色 | 5 | 12 | 10 | 20 | 武器攻撃 1d6 · cast spell | starts peaceful. |
| 戦士 (warrior) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d8 ×2 | starts peaceful. |
| 実習生 (apprentice) | 白色 | 5 | 12 | 10 | 30 | 武器攻撃 1d6 · cast spell | starts peaceful. |

:::
