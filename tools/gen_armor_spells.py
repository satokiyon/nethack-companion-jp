# -*- coding: utf-8 -*-
"""
Generate segments for step_288 to step_297 (Armor and Spell Tables).
"""
import os

segments = {}

segments["step_288"] = """### 防具一覧表 (Armor Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h: no corrections. Every armor row (AC=10-macro-arg, MC, weight, material, slot) verified across ARMOR/HELM/CLOAK/SHIELD/GLOVES/BOOTS macros.
-->
<!-- audit
2026-05-19:
- body armor: AC/Wt/Cost via ARMOR() macros (objects.h:556-600); plate mail AC+7 wt450 cost600 (line 556-558).
- mithril coats: AC+6/+5, wt 150, cost 240, MITHRIL material (objects.h:571-576).
- shirts wt 5 (Hawaiian/T-shirt, objects.h:603-608); cloaks at objects.h:611-650.
- helmets at objects.h:445-487; gloves at objects.h:686-697; boots at objects.h:700-727.
- shields at objects.h:653-679; cloak of protection MC 3 (objects.h:637-640).
- helm of brilliance: adds spe to Int and Wis (literal enchantment), NO dice (do_wear.c:3328-3334 adj_abon).
- gauntlets of dexterity: adds spe to Dex, NO dice (do_wear.c adj_abon).
- dunce cap is NOT pre-cursed at generation: follows standard mkobj; auto-curses when worn (do_wear.c:475-491).
- 9/10-cursed-on-generation items: FUMBLE_BOOTS, LEVITATION_BOOTS, HELM_OF_OPPOSITE_ALIGNMENT, GAUNTLETS_OF_FUMBLING (mkobj.c:1086-1090).
- mithril DOES suffer casting penalty: MITHRIL is in is_metallic range, spelarmr applies (objclass.h:194-196, spell.c:2191-2193).
- blue dragon scale mail and scales give extrinsic Very_fast tier matching speed boots, NOT intrinsic Fast (do_wear.c:817-828 EFast).
- speed boots mechanic: free action on 2/3 of turns, NOT "+1 speed". (allmain.c:125-128 `if (Very_fast) { if (rn2(3) != 0) moveamt += NORMAL_SPEED; }`)
- levitation boots: Boots_off handles in-air removal (do_wear.c:300-310); the trap is the 9/10 curse.
- robe casting bonus cancels most of the metal-armor penalty (spell.c:2192-2195 spelarmr subtraction).
- chain mail: all iron mails are Mines drops (the "Dwarves drop these" framing is misleading).
- follow-ups: build_armor_appendix.py may be stale; "yellow dragon scale mail | Rare." not verified against 5.0 generation rules.
-->

**AC**はその防具が提供するアーマークラス補正値です（数値が大きいほど防御力が高く、画面上のAC表示からこの数値が減算されます）。**MC**は魔法防御能力レベル（1〜3）を表し、数値が高いほど敵の魔法攻撃を防ぐ確率が高まります。**重量 (Wt)**はユニット重量、**価格 (Cost)**は店での基本価格です。**備考**列には、装備中に付与される固有能力（耐性や特性）および戦術上の注意点をまとめています。防具は装備部位ごとに分類されています。ドラゴンの鱗鎧は終盤における圧倒的重要性から、個別の項目として取り上げています。一部の防具にある括弧内の名称は、侍（Samurai）プレイ時に表示される別名です（ゲーム内部では同一アイテム）。
"""

segments["step_289"] = """#### 胴鎧 (Body armor / suits)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 鋼鉄の鎧 (plate mail / tanko: 短甲) | +7 | 2 | 450 | 600 | 鉄 | 魔法詠唱ペナルティあり。 |
| 水晶の鎧 (crystal plate mail) | +7 | 2 | 415 | 820 | ガラス | 決して錆びない。魔法詠唱ペナルティあり。 |
| 青銅の鎧 (bronze plate mail) | +6 | 1 | 450 | 400 | 銅 |  |
| 鉄片の鎧 (splint mail) | +6 | 1 | 400 | 80 | 鉄 |  |
| 帯金の鎧 (banded mail) | +6 | 1 | 350 | 90 | 鉄 |  |
| ドワーフのミスリル服 (dwarvish mithril-coat) | +6 | 2 | 150 | 240 | ミスリル | 軽量だが金属製：魔法詠唱へのペナルティは鋼鉄の鎧と同等。 |
| エルフのミスリル服 (elven mithril-coat) | +5 | 2 | 150 | 240 | ミスリル | 軽量だが金属製：魔法詠唱へのペナルティは鋼鉄の鎧と同等。 |
| 鎖かたびら (chain mail) | +5 | 1 | 300 | 75 | 鉄 |  |
| オークの鎖かたびら (orcish chain mail) | +4 | 1 | 300 | 75 | 鉄 |  |
| 鱗の鎧 (scale mail) | +4 | 1 | 250 | 45 | 鉄 |  |
| 鋲付き革鎧 (studded leather armor) | +3 | 1 | 200 | 15 | 革 | 魔法詠唱ペナルティなし。 |
| 鉄環の鎧 (ring mail) | +3 | 1 | 250 | 100 | 鉄 |  |
| オークの鉄環の鎧 (orcish ring mail) | +2 | 1 | 250 | 80 | 鉄 |  |
| 革鎧 (leather armor) | +2 | 1 | 150 | 5 | 革 |  |
| 革の服 (leather jacket) | +1 | — | 30 | 10 | 革 |  |
| 灰色ドラゴンの鱗鎧 (gray dragon scale mail) | +9 | — | 40 | 1200 | ドラゴンの皮 | 魔法防御（Magic resistance）。終盤における最終目標の胴鎧。 |
| 銀色ドラゴンの鱗鎧 (silver dragon scale mail) | +9 | — | 40 | 1200 | ドラゴンの皮 | 反射（Reflection）。 |
| 黒色ドラゴンの鱗鎧 (black dragon scale mail) | +9 | — | 40 | 1200 | ドラゴンの皮 | 分解耐性（Disintegration resistance）＋吸命耐性（Drain resistance）。 |
| 黄色ドラゴンの鱗鎧 (yellow dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 酸耐性（Acid resistance）＋石化耐性（Stoning resistance）。 |
| 橙色ドラゴンの鱗鎧 (orange dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 睡眠耐性（Sleep resistance）＋自由行動（Free action）。 |
| 白色ドラゴンの鱗鎧 (white dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 冷気耐性（Cold resistance）＋消化遅延（Slow digestion）。 |
| 赤色ドラゴンの鱗鎧 (red dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 火炎耐性（Fire resistance）＋赤外線視覚（Infravision）。 |
| 緑色ドラゴンの鱗鎧 (green dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 毒耐性（Poison resistance）＋病気耐性（Sickness resistance）。 |
| 青色ドラゴンの鱗鎧 (blue dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 電撃耐性（Shock resistance）＋高速移動（韋駄天の靴と同等）。 |
| 金色ドラゴンの鱗鎧 (gold dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 幻覚耐性（Hallucination resistance）＋恒久光源（胴部位唯一の光源）。 |

:::
"""

segments["step_290"] = """#### ドラゴンの鱗 (Dragon scales)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 灰色ドラゴンの鱗 (gray dragon scales) | +3 | — | 40 | 700 | ドラゴンの皮 | 魔法防御。鎧作成の巻物で鱗鎧へアップグレード可能。 |
| 銀色ドラゴンの鱗 (silver dragon scales) | +3 | — | 40 | 700 | ドラゴンの皮 | 反射。 |
| 黒色ドラゴンの鱗 (black dragon scales) | +3 | — | 40 | 700 | ドラゴンの皮 | 分解耐性＋吸命耐性。 |
| 黄色ドラゴンの鱗 (yellow dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 酸耐性＋石化耐性。 |
| 橙色ドラゴンの鱗 (orange dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 睡眠耐性＋自由行動。 |
| 白色ドラゴンの鱗 (white dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 冷気耐性＋消化遅延。 |
| 赤色ドラゴンの鱗 (red dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 火炎耐性＋赤外線視覚。 |
| 緑色ドラゴンの鱗 (green dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 毒耐性＋病気耐性。 |
| 青色ドラゴンの鱗 (blue dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 電撃耐性＋高速移動（韋駄天の靴と同等）。 |
| 金色ドラゴンの鱗 (gold dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 幻覚耐性＋恒久光源。 |

:::
"""

segments["step_291"] = """#### シャツ (Shirts)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| アロハシャツ (Hawaiian shirt) | +0 | — | 5 | 3 | 布 | 観光客（Tourist）の初期装備。胴鎧の下に着用可能。 |
| Ｔシャツ (T-shirt) | +0 | — | 5 | 2 | 布 | 胴鎧の下に着用可能。 |

:::
"""

segments["step_292"] = """#### クローク (Cloaks)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| ミイラの包帯 (mummy wrapping) | +0 | 1 | 3 | 2 | 布 | 着用中は透明化（Invisibility）の効果を無効化する。 |
| エルフのクローク (elven cloak) | +1 | 1 | 10 | 60 | 布 | 忍び足（Stealth）。 |
| オークのクローク (orcish cloak) | +0 | 1 | 10 | 40 | 布 |  |
| ドワーフのクローク (dwarvish cloak) | +0 | 1 | 10 | 50 | 布 |  |
| 防水クローク (oilskin cloak) | +1 | 2 | 10 | 50 | 布 | 掴み攻撃や水濡れを防ぐ。 |
| ローブ (robe) | +2 | 2 | 15 | 50 | 布 | 魔法詠唱ボーナス。金属鎧による詠唱ペナルティの大半を相殺する。 |
| 錬金術の仕事着 (alchemy smock) | +1 | 1 | 10 | 50 | 布 | 毒耐性（Poison resistance）。 |
| 革のクローク (leather cloak) | +1 | 1 | 15 | 40 | 革 |  |
| 守りのクローク (cloak of protection) | +3 | 3 | 10 | 50 | 布 | クロークの中で最高の魔法防御能力（MC 3）を誇る。 |
| 透明のクローク (cloak of invisibility) | +1 | 1 | 10 | 60 | 布 | 透明化（Invisibility）。 |
| 魔法を防ぐクローク (cloak of magic resistance) | +1 | 1 | 10 | 60 | 布 | 魔法防御（Magic resistance）。最も軽量な魔法防御の供給源。 |
| 幻影のクローク (cloak of displacement) | +1 | 1 | 10 | 50 | 布 | 幻影（Displacement）。 |

:::
"""

segments["step_293"] = """#### 兜・帽子 (Helmets)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| エルフの革帽子 (elven leather helm) | +1 | — | 3 | 8 | 革 |  |
| オークの兜 (orcish helm) | +1 | — | 30 | 10 | 鉄 |  |
| ドワーフの鉄兜 (dwarvish iron helm) | +2 | — | 40 | 20 | 鉄 |  |
| フィドーラ (fedora) | +0 | — | 3 | 1 | 布 | 考古学者（Archeologist）の初期装備。同職業に幸運+1を付与。 |
| とんがり帽子 (cornuthaum) | +0 | 1 | 4 | 80 | 布 | 透視（Clairvoyance）。魔法使いのみ有効。魔法使い以外が被ると他の透視能力を阻害する。 |
| 道化の帽子 (dunce cap) | +0 | — | 4 | 1 | 布 | 知力と知恵が強制的に 6 に低下する。被ると自動的に呪われる。外すには呪い解除が必要。 |
| くぼんだ鍋 (dented pot) | +1 | — | 10 | 8 | 鉄 |  |
| 知性の兜 (helm of brilliance) | +1 | — | 40 | 50 | ガラス | 着用中、強化値が知力と知恵の両方に加算される（+3の兜なら知力+3、知恵+3）。 |
| 兜 (helmet / kabuto: 兜) | +1 | — | 30 | 10 | 鉄 |  |
| 警戒の兜 (helm of caution) | +1 | — | 50 | 50 | 鉄 | 警告（Warning）。 |
| 逆属性の兜 (helm of opposite alignment) | +1 | — | 50 | 50 | 鉄 | 着用中、属性が反転する。生成時に90%の確率で呪われている。 |
| テレパシーの兜 (helm of telepathy) | +1 | — | 50 | 50 | 鉄 | 目が見えているときは周囲8マス、盲目時はフロア全体のテレパシーを得る。 |

:::

逆属性の兜は基本的には罠アイテムですが、属性反転を意図的に利用できる局面もあります。異属性の祭壇で生贄を捧げる、反対属性のクエストアーティファクトを所持する、あるいは星界の面（Astral Plane）で魔除けを受け入れる祭壇の属性を変更する際などに活用されます。
"""

segments["step_294"] = """#### 小手・手袋 (Glovers)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 革の手袋 (leather gloves / yugake: ゆがけ) \* | +1 | — | 10 | 8 | 革 |  |
| お手玉の小手 (gauntlets of fumbling) \* | +1 | — | 10 | 50 | 革 | 頻繁に足をもつれさせる（お手玉状態）。生成時に90%の確率で呪われている。回避推奨。 |
| 力の小手 (gauntlets of power) \* | +1 | — | 30 | 50 | 鉄 | 筋力を強制的に 25 に設定する。 |
| 器用さの小手 (gauntlets of dexterity) \* | +1 | — | 10 | 50 | 革 | 着用中、強化値が器用さに加算される（+3の小手なら器用さ+3）。 |

:::

\* 印の付いたアイテムは、識別されるまで4種類の実見外見名（*古い手袋*、*パッド入り手袋*、*乗馬用手袋*、*フェンシング手袋*）のいずれかとして出現します（通常の革の手袋も含みます）。
"""

segments["step_295"] = """#### 靴 (Boots)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| かかとの低い靴 (low boots) | +1 | — | 10 | 8 | 革 |  |
| 鉄の靴 (iron shoes) | +2 | — | 50 | 16 | 鉄 |  |
| かかとの高い靴 (high boots) | +2 | — | 20 | 12 | 革 |  |
| 韋駄天の靴 (speed boots) \* | +1 | — | 20 | 50 | 革 | 高速移動（Very fast）。3ターンのうち2ターンで無料の追加行動を得られる。 |
| 水上歩行の靴 (water walking boots) \* | +1 | — | 15 | 50 | 革 | 水上や氷上を歩行可能。耐火加工された靴と火炎耐性があれば溶岩も渡れる。 |
| 跳躍の靴 (jumping boots) \* | +1 | — | 20 | 50 | 革 | `#jump` コマンドで近くの任意のマスへ跳躍できる。 |
| エルフの靴 (elven boots) \* | +1 | — | 15 | 8 | 革 | 忍び足（Stealth）。 |
| 蹴りの靴 (kicking boots) \* | +1 | — | 50 | 8 | 鉄 |  |
| お手玉の靴 (fumble boots) \* | +1 | — | 20 | 30 | 革 | 頻繁に足をもつれさせる。生成時に90%の確率で呪われている。回避推奨。 |
| 浮遊の靴 (levitation boots) \* | +1 | — | 15 | 30 | 革 | 浮遊（Levitation）。生成時に90%の確率で呪われている。呪われた靴は脱ぐことができないため致命的な罠となる。 |

:::

\* 印の付いたアイテムは、識別されるまで7種類の実見外見名（*戦闘用ブーツ*、*ジャングルブーツ*、*ハイキングブーツ*、*泥靴*、*バックル付きブーツ*、*乗馬用ブーツ*、*スノーブーツ*）のいずれかとして出現します。
"""

segments["step_296"] = """#### 盾 (Shields)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 小さな盾 (small shield) | +1 | — | 30 | 3 | 木 |  |
| 吸命耐性の盾 (shield of drain resistance) | +1 | — | 30 | 50 | 木 | 吸命耐性（Drain resistance）。 |
| 電撃耐性の盾 (shield of shock resistance) | +1 | — | 30 | 50 | 木 | 電撃耐性（Shock resistance）。 |
| エルフの盾 (elven shield) | +2 | — | 40 | 7 | 木 |  |
| ウルク＝ハイの盾 (Uruk-hai shield) | +1 | — | 50 | 7 | 鉄 |  |
| オークの盾 (orcish shield) | +1 | — | 50 | 7 | 鉄 |  |
| 大きな盾 (large shield) | +2 | — | 100 | 10 | 鉄 | 他のすべての盾と同様、両手持ち武器および二刀流戦闘を阻害する。 |
| ドワーフの丸盾 (dwarvish roundshield) | +2 | — | 100 | 10 | 鉄 |  |
| 反射の盾 (shield of reflection) | +2 | — | 50 | 50 | 銀 | 反射（Reflection）。胴鎧の装備枠を自由に選べるようになる。 |

:::
"""

segments["step_297"] = """### 呪文一覧表 (Spell Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h: no corrections. All 41 spell rows' level/school/type verified (incl. chain lightning lvl 2). Spell damage figures live in spell.c/zap.c, outside this table's source.
-->
<!-- audit
2026-05-19:
- 41 spells, sourced from objects.h SPELL() macros (P_ATTACK..P_MATTER); SPELL macro signature at objects.h:1277-1281, oc_level=oc_oc2.
- attack spells at objects.h:1297-1330 (force bolt/magic missile/drain life/cone of cold/fireball/finger of death/chain lightning).
- healing spells at objects.h:1313-1408 (healing/cure blindness/cure sickness/extra healing/stone to flesh/restore ability).
- divination spells at objects.h:1308-1384 (light/detect monsters/detect food/clairvoyance/detect unseen/identify/detect treasure/magic mapping).
- enchantment spells at objects.h:1305-1354 (confuse monster/slow monster/cause fear/sleep/charm monster).
- cleric spells at objects.h:1337-1400 (protection/create monster/remove curse/create familiar/turn undead).
- escape spells at objects.h:1355-1404 (jumping/haste self/invisibility/levitation/teleport away).
- matter spells at objects.h:1293-1407 (knock/wizard lock/dig/polymorph/cancellation/stone to flesh).
- Flame sphere and freeze sphere are `#if 0 DEFERRED` (objects.h:1413-1422), NOT shipped in 5.0.
- Chain lightning is level 2 per macro (objects.h:1409-1411); body table at line 4986 and What's New at 8585 still say L4: follow-up fix.
- Magic missile IS Antimagic-blocked (zap.c:4410-4419, "missiles bounce off!"), NOT unresistable.
- Finger of death: monster MR resists, but player gets no Antimagic check on death-ray instakill (zap.c:2885-2902).
- Clairvoyance gets a P_SKILLED upgrade detecting nearby monsters per pulse (spell.c:1572-1576).
- Fireball/cone of cold become aimed explosions at P_SKILLED (spell.c spelleffects).
- Remove curse/confuse monster/detect food/cause fear/identify/charm monster get blessed-scroll behavior at P_SKILLED.
- Haste self/detect treasure/detect monsters/levitation/restore ability get blessed-potion behavior at P_SKILLED.
- Protection doubles uspmtime at P_EXPERT (spell.c:1169); jumping distance scales with role_skill.
- Charm monster is untargeted (read.c:1679-1708 seffect_taming is area-centered-on-caster, no direction prompt).
- Charm monster area: 3×3 normal, 11×11 confused (`bd = confused ? 5 : 1`, -bd..bd inclusive), NOT 5×5. (read.c:1689 seffect_taming)
- Charm monster P_SKILLED upgrade is blessed-scroll reliability, NOT a radius bump. (spell.c:1524-1525 sets pseudo->blessed when role_skill >= P_SKILLED; read.c:1689 radius `bd` depends only on `confused`, not on blessed)
- Cause fear blessed and uncursed are identical (read.c:1454-1486); loop hits every visible monster on the level, not just nearby.
- Remove curse blessed branch uncurses every non-coin inventory item (read.c:1514-1577), NOT just worn/wielded.
-->

魔法書の完全カタログです。系統順、続いてレベル順に並んでいます。**レベル (Lvl)**は呪文レベル、**消費魔力 (Pw cost)**は常に「5×呪文レベル」です。**種別 (Type)**は呪文の目標指定方法を区分しています：

- **方向指定 (aimed):** 方向を指定し、その直線の1マスに命中します。
- **光線 (ray):** 術者から直線状に伸び、遮られるまで進むビームです。
- **目標不要 (untargeted):** 方向指定は不要で、自身、フロア全体、または固定範囲に効果が発現します。

**上位効果 (Upgrade)**はその系統のスキルが**熟練 (Skilled)**以上になった際の挙動変化です（防護の呪文のみエキスパートで発動し、跳躍の距離はランクに応じて連続的に拡大します）。

::: dense-table

| 呪文名 | 系統 | レベル | 種別 | 効果 | 上位効果 (Skilled以上) |
|-----------------|-------------|-----|------------|-------------------------------------|-------------------------------|
| 衝撃 (force bolt) | 攻撃 | 1 | 方向指定 | 2d12の魔法打撃ダメージ | — |
| 連鎖雷撃 (chain lightning) | 攻撃 | 2 | 目標不要 | 周囲のモンスターに電撃ダメージ | — |
| 生命力吸収 (drain life) | 攻撃 | 2 | 方向指定 | 対象から経験値レベルを1吸収 | — |
| マジックミサイル (magic missile) | 攻撃 | 2 | 光線 | (XL÷2 + 1)d6の衝撃ビーム（端数切捨て）。魔法防御で防がれる | — |
| 冷気 (cone of cold) | 攻撃 | 4 | 光線 | (XL÷2 + 1)d6の冷気ビーム（端数切捨て） | 目標指定の爆発 |
| 火炎 (fireball) | 攻撃 | 4 | 光線 | (XL÷2 + 1)d6の火炎ビーム（端数切捨て） | 目標指定の爆発 |
| 死の指 (finger of death) | 攻撃 | 7 | 光線 | 死の光線。敵の魔法防御で防がれるが、自身に反射・誤射した際は防御チェックを迂回して即死する | — |
| 回復 (healing) | 回復 | 1 | 方向指定 | HPを回復 | 盲目も治療 |
| 盲目治療 (cure blindness) | 回復 | 2 | 目標不要 | 盲目状態を回復 | — |
| 病気治療 (cure sickness) | 回復 | 3 | 目標不要 | 食中毒および病気を治療 | — |
| 完全回復 (extra healing) | 回復 | 3 | 方向指定 | より多くのHPを回復 | — |
| 石から肉へ (stone to flesh) | 回復 | 3 | 方向指定 | 石像を生きたモンスターに変える。石化を治療 | — |
| 能力回復 (restore ability) | 回復 | 4 | 目標不要 | 低下した能力値を1つ全快 | 低下したすべての能力値を全快 |
| 怪物探知 (detect monsters) | 予見 | 1 | 目標不要 | フロア上のモンスターを表示 | 効果時間が延長 |
| 明かり (light) | 予見 | 1 | 目標不要 | 現在の部屋を照らす | — |
| 食料探知 (detect food) | 予見 | 2 | 目標不要 | フロア上の食料を表示 | 有害な食事の前に警告 |
| 透視 (clairvoyance) | 予見 | 3 | 目標不要 | 周囲のマップを周期的に開拓視認 | 熟練：周期ごとに周囲のモンスターも探知 |
| 不可視探知 (detect unseen) | 予見 | 3 | 目標不要 | 不可視のモンスターや罠を表示 | — |
| 識別 (identify) | 予見 | 3 | 目標不要 | 所持品を1つ識別 | 複数の所持品を一括識別 |
| 宝探知 (detect treasure) | 予見 | 4 | 目標不要 | フロア上のすべてのアイテムを表示 | 探知したアイテムの種別を識別 |
| 地図化 (magic mapping) | 予見 | 5 | 目標不要 | フロア全体の地形を開拓表示 | — |
| 怪物混乱 (confuse monster) | 付与 | 1 | 目標不要 | 次の近接攻撃で対象を混乱させる | 複数回の攻撃分チャージされる |
| 怪物減速 (slow monster) | 付与 | 2 | 方向指定 | 対象モンスターの移動速度を低下 | — |
| 恐怖 (cause fear) | 付与 | 3 | 目標不要 | 視界内のモンスターを逃走させる | — |
| 睡眠 (sleep) | 付与 | 3 | 光線 | 射線上のモンスターを眠らせる | — |
| 魅了 (charm monster) | 付与 | 5 | 目標不要 | 周囲 3×3 エリアのモンスターを手懐ける | — |
| 防護 (protection) | 僧侶 | 1 | 目標不要 | 魔力を消費して一時的なACボーナスを得る | **エキスパート**: 効果時間が2倍 |
| 怪物作成 (create monster) | 僧侶 | 2 | 目標不要 | 近くにランダムなモンスターを召喚 | — |
| 呪い解除 (remove curse) | 僧侶 | 3 | 目標不要 | 装備中のアイテムの呪いを解く | 所持している全アイテムの呪いを解く |
| ペット作成 (create familiar) | 僧侶 | 6 | 目標不要 | 手懐けられたペットを召喚する | — |
| アンデッド退散 (turn undead) | 僧侶 | 6 | 方向指定 | アンデッドや悪魔にダメージを与えて逃走させる | — |
| 跳躍 (jumping) | 緊急脱出 | 1 | 目標不要 | 近くの指定したマスへ跳躍する | スキルランクに応じて跳躍距離が拡大 |
| 加速 (haste self) | 緊急脱出 | 3 | 目標不要 | 一時的な高速移動状態になる | 効果時間が延長 |
| 不可視 (invisibility) | 緊急脱出 | 4 | 目標不要 | 透明状態になる | — |
| 浮遊 (levitation) | 緊急脱出 | 4 | 目標不要 | 落とし穴や水面の上に浮かび上がる | `>` キーで任意に着地可能 |
| テレポート (teleport away) | 緊急脱出 | 6 | 方向指定 | 対象をフロアの別の場所へテレポートさせる | — |
| 開錠 (knock) | 物質操作 | 1 | 方向指定 | 扉を開け、錠前を解除する | — |
| 施錠 (wizard lock) | 物質操作 | 2 | 方向指定 | 扉を閉じて鍵をかける | — |
| 穴掘り (dig) | 物質操作 | 5 | 光線 | 壁、岩、床を掘り抜く | — |
| 変身 (polymorph) | 物質操作 | 6 | 方向指定 | 対象を変身させる | — |
| 変化消失 (cancellation) | 物質操作 | 7 | 方向指定 | 対象の魔法特性を打ち消す | — |

:::

光線系呪文（睡眠、マジックミサイル、死の指、および未熟練状態の冷気や火炎）の命中率も、スキルランクに応じて上昇します。
"""

for step_id, content in segments.items():
    filepath = os.path.join("docs", "segments_ja", f"{step_id}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Written {filepath}")

