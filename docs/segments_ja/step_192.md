#### 職業別スキル上限表 (Per-Role Skill Caps)

<!-- audit
2026-05-19:
- All 13 role skill tables sourced from u_init.c (Skill_A through Skill_W); skills not in def_skill are P_UNSKILLED-locked. (u_init.c:257-569 tables Skill_A/B/C/H/K/Mon/P/R/Ran/S/T/V/W; weapon.c:1738-1781 skill_init defaults all to P_ISRESTRICTED then walks the def_skill list)
- All 494 cells (27 weapons + 4 fighting styles + 7 spell schools × 13 roles) exact-match against u_init.c:257-572.
- Scimitar omitted: no role has it in 5.0 (merged into saber per skills.h header note).
- P_MARTIAL_ARTS appears only in Skill_Mon (P_GRAND_MASTER) and Skill_S (P_MASTER); Monks have P_BARE_HANDED_COMBAT restricted (they get martial arts instead).
- Wizard and Monk are the only roles with all 7 spell schools listed in their def_skill table (Skill_W u_init.c:562-568 has all 7 P_*_SPELL entries; Skill_Mon u_init.c:380-386 has all 7). Other roles list a subset (Priest at u_init.c:408-410 has only 3, Healer at u_init.c:342 has only 1, etc.).
-->

以下に武器、戦闘スタイル、魔法系統の固定上限値を示す3つの表を掲載します。各職業の欄に記載されていないスキルは **制限（Restricted）** されており、1つの例外（神から生贄ギフトとして授かったアーティファクト武器は、その武器スキルを「入門」まで制限解除する）を除き、ランクは「未習熟」に固定されます。記号の凡例：**B**=入門 (Basic)、**S**=熟練 (Skilled)、**E**=エキスパート (Expert)、**M**=マスター (Master)、**GM**=総師範 (Grand Master) (Grand Master)、**—**=制限（未習熟固定）。

空欄（—）のスキルであっても使用不能というわけではなく、永遠に「未習熟」のままであることを意味します。治療師であっても衝撃の魔法書を読んで唱えることは可能ですし、魔法使いであっても長剣を振り回すことはできます。ただし、[スキル階梯](#the-skill-ladder) に記された未習熟のペナルティ（武器なら −4/−2、二刀流なら1打撃ごとに −9/−3、魔法系統なら高い詠唱失敗率）を常に支払い続け、成長の余地はありません。職業略称：Arc=考古学者、Bar=野蛮人、Cav=洞窟人、Hea=治療師、Kni=騎士、Mon=武闘家、Pri=司祭、Rog=盗賊、Ran=レンジャー、Sam=侍、Tou=観光客、Val=ワルキューレ、Wiz=魔法使い。

##### 武器スキル上限表 (Weapon Skill Caps)

::: dense-table

| 武器 | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 短剣 (dagger) | B | B | B | S | B | — | — | E | E | B | E | E | E |
| ナイフ (knife) | B | — | S | E | B | — | — | E | S | S | S | — | S |
| 斧 (axe) | — | E | S | — | S | — | — | — | S | — | B | E | S |
| つるはし (pick-axe) | E | S | B | — | B | — | — | — | B | — | B | S | — |
| 小剣 (short sword) | B | E | — | S | S | — | — | E | B | E | E | S | B |
| 幅広の剣 (broadsword) | — | S | — | — | S | — | — | S | — | S | B | S | — |
| 長剣 (long sword) | — | S | — | — | E | — | — | S | — | E | B | E | — |
| 両手剣 (two-handed sword) | — | E | — | — | S | — | — | B | — | E | B | E | — |
| サーベル (saber) | E | S | — | B | S | — | — | S | — | B | S | B | — |
| こん棒 (club) | S | S | E | S | B | — | E | S | — | — | — | — | S |
| メイス (mace) | — | S | E | B | S | — | E | S | — | — | B | — | B |
| モーニングスター (morning star) | — | S | B | — | S | — | E | B | B | — | B | — | — |
| フレイル (flail) | — | B | S | — | B | — | E | B | S | S | B | — | — |
| ハンマー (hammer) | — | E | S | — | B | — | E | B | B | — | B | E | — |
| 六尺棒 (quarterstaff) | S | B | E | E | — | B | E | — | B | B | B | B | E |
| 長柄武器 (polearms) | — | — | S | B | S | — | S | B | S | S | B | S | S |
| 槍 (spear) | — | S | E | B | S | B | S | B | E | S | B | E | B |
| トライデント (trident) | — | S | S | B | B | — | S | — | B | — | B | B | B |
| ランス (lance) | — | — | — | — | E | — | B | — | — | S | B | S | — |
| 弓 (bow) | — | B | S | — | B | — | B | — | E | E | B | — | — |
| スリング (sling) | S | — | E | S | — | — | B | — | E | — | B | B | S |
| クロスボゥ (crossbow) | — | — | — | — | S | B | B | E | E | — | B | — | — |
| 投げ矢 (dart) | B | — | — | E | — | — | B | E | E | — | E | — | E |
| 手裏剣 (shuriken) | — | — | — | S | — | B | B | S | S | E | B | — | B |
| ブーメラン (boomerang) | E | — | E | — | — | — | B | — | E | — | B | — | — |
| 鞭 (whip) | E | — | — | — | — | — | — | — | B | — | B | — | — |
| ユニコーンの角 (unicorn horn) | S | — | B | E | — | — | S | — | — | — | S | — | — |

:::

5.0 ではシミターはサーベルに統合されました。現在はどちらも同一のスキルを参照します。

##### 戦闘スタイル上限表 (Fighting Style Caps)

::: dense-table

| スタイル | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 素手格闘 (bare hands) | E | M | M | B | E | — | B | E | B | — | S | E | B |
| 二刀流 (two-weapon) | B | B | — | — | S | — | — | E | — | E | S | S | — |
| 騎乗 (riding) | B | B | — | — | E | — | — | B | B | S | B | S | B |
| 武術 (martial arts) | — | — | — | — | — | GM | — | — | — | M | — | — | — |

:::

武術を扱えるのは武闘家と侍だけであり、総師範 (Grand Master)に到達できるのは武闘家のみです。

##### 魔法系統上限表 (Spell School Caps)

::: dense-table

| 系統 | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 攻撃魔法 (Attack) | B | B | B | — | S | B | — | — | — | B | — | B | E |
| 回復魔法 (Healing) | B | — | — | E | S | E | E | — | B | — | — | — | S |
| 予見魔法 (Divination) | E | — | — | — | — | B | E | S | E | B | B | — | E |
| 付与魔法 (Enchantment) | — | — | — | — | — | B | — | — | — | — | B | — | S |
| 僧侶魔法 (Cleric) | — | — | — | — | S | S | E | — | — | S | — | — | S |
| 脱出魔法 (Escape) | — | B | — | — | — | S | — | S | B | — | S | B | E |
| 変化魔法 (Matter) | B | — | S | — | — | B | — | S | — | — | — | — | E |

:::

治療師は回復魔法をエキスパートまで極められますが、他のすべての魔法系統が制限されています。このような単一系統特化は治療師だけの特徴です。全7系統すべてにアクセスできるのは魔法使いと武闘家だけであり、そのうち4系統をエキスパートまで引き上げられるのは魔法使いだけです（武闘家がエキスパートになれるのは回復魔法のみ）。野蛮人とワルキューレは利用可能な2系統（攻撃と脱出）で入門が上限であり、他の5系統は制限されています。
