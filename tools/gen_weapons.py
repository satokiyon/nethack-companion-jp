# -*- coding: utf-8 -*-
"""
Generate segments for step_261 to step_287 (Weapons Tables).
"""
import os

segments = {}

segments["step_261"] = """### 武器一覧表 (Weapons Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h + weapon.c: no corrections. Every weapon row (base/bonus dice, weight, cost, to-hit, material, two-handed/launcher/skill notes) verified, including composite-damage entries vs dmgval().
-->

ダメージは**小型に対するダメージ / 大型に対するダメージ (vs small / vs large)**として表記されており、強化値（強化・呪い）が加算される前、かつ銀や材質による追加ボーナスを除いた基本ダイス値です。**重量 (Wt)**はユニット重量、**価格 (Cost)**は店における未強化時の基本価格（Zm: ゾークミッド）、**命中 (Hit)**は武器自体に組み込まれている命中補正ボーナス（大半は 0）を表します。盾の装備や二刀流（二刀流戦闘）を阻害する両手持ち武器には、備考欄にフラグが付けられています。武器はスキルごとに分類されています。スキル枠（スロット）を投資する前に、[職業別のスキル上限一覧](#per-role-skill-caps)を確認してください。一部の武器に見られる括弧内の名称は、侍（Samurai）がプレイした際に画面上に表示される別名です（ゲーム内部では同一のアイテムとして処理されます）。
"""

segments["step_262"] = """#### 短剣 (Dagger)
<!-- audit
2026-05-19:
- Expert Rogue dagger multishot caps at rnd(4) = 1-4: 1 base + 1 Expert + 1 Skilled + 1 class (dothrow.c:177-190, 63-67)
- athame engraving Elbereth does NOT dull the weapon, so no enchantment is consumed (engrave.c:1306-1307, 1361). Duration is unchanged
- silver weapons hurt demons, vampires, lycanthropes, shades, and imps (except tengu) per mon_hates_silver (mondata.c:524-528)
- silver does NOT hurt liches, zombies, mummies, wraiths, ghouls, or ghosts (none of those classes appear in hates_silver, mondata.c:524-528)
- silver damage bonus is rolled in mhitm/hmon, +1d20 vs hates_silver targets for silver weapons (uhitm.c:1376-1377)
-->

投擲および刺突。短剣はスタック（束ねて所持）可能で壊れにくく、盗賊（Rogue）は投擲時にマルチショット（連続投擲）ボーナスを得られます（エキスパート時には1ターンに最大4本投擲）。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 短剣 (dagger) | 1d4 / 1d3 | 10 | 4 | +2 | 鉄 | スタック可能。スキルがエキスパートの盗賊は1回の投擲で最大4本までマルチショット可能。 |
| エルフの短剣 (elven dagger) | 1d5 / 1d3 | 10 | 4 | +2 | 木 | スタック可能。アーティファクト形態はスティング (Sting)。 |
| オークの短剣 (orcish dagger) | 1d3 / 1d3 | 10 | 4 | +2 | 鉄 | スタック可能。 |
| 銀の短剣 (silver dagger) | 1d4 / 1d3 | 12 | 40 | +2 | 銀 | スタック可能。悪魔、吸血鬼、獣人、影、小悪魔（インプ）に対して銀特効ダメージ。盗賊や野伏（Ranger）の一般的な利き手以外の武器。 |
| アサメ (athame) | 1d4 / 1d3 | 10 | 4 | +2 | 鉄 | スタック可能。アサメで文字を刻んでも**刃先が鈍ることはない**（強化値が減少しない）。 |

:::
"""

segments["step_263"] = """<!-- audit
2026-05-19:
- 5 knife rows verified: P_KNIFE skill, scalpel METAL, knife/stiletto IRON, worm tooth/crysknife BONE (objects.h:215-233)
- scalpel is Healer's starter (u_init.c:77)
- crysknife reverts to worm tooth on drop via type-id swap, NOT poly (do.c:903-918)
- fixed (erodeproof) crysknife only reverts ~10% of drops (do.c:911)
-->
#### ナイフ (Knife)

主に近接戦闘用。ナイフはスタック可能で投擲もできますが、投擲ナイフによるマルチショットボーナスを得られる職業はありません。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| メス (scalpel) | 1d3 / 1d3 | 5 | 6 | +2 | 金属 | 医師（Healer）の初期装備。 |
| ナイフ (knife / shito: 刺刀) | 1d3 / 1d2 | 5 | 4 | — | 鉄 |  |
| スティレット (stiletto) | 1d3 / 1d2 | 5 | 4 | — | 鉄 |  |
| ワームの歯 (worm tooth) | 1d2 / 1d2 | 20 | 2 | — | 骨 |  |
| クリスナイフ (crysknife) | 1d10 / 1d10 | 20 | 100 | +3 | 骨 | 床に落としたり投げたりするとワームの歯に戻ってしまう。耐腐食（erodeproof）加工されたものは戻る確率が約10%に軽減される。 |

:::
"""

segments["step_264"] = """<!-- audit
2026-05-19:
- 4 short sword rows verified: short 1d6/1d8, elven 1d8/1d8, orcish 1d5/1d8, dwarvish 1d7/1d8 (objects.h:244-255)
- all share P_SHORT_SWORD; scimitar uses P_SABER and is correctly excluded
- Rogue starter (u_init.c:134); Samurai "wakizashi" is a short sword aliased in objnam.c:106 (u_init.c:144)
- no artifact uses SHORT_SWORD as base type
-->
#### 小剣 (Short sword)

片手持ち近接武器。脇差（wakizashi）と小剣（short sword）は職業による表示名が異なるだけで、同一の武器です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 小剣 (short sword / wakizashi: 脇差) | 1d6 / 1d8 | 30 | 10 | — | 鉄 | 盗賊（Rogue）の初期装備。 |
| エルフの小剣 (elven short sword) | 1d8 / 1d8 | 30 | 10 | — | 木 |  |
| オークの小剣 (orcish short sword) | 1d5 / 1d8 | 30 | 10 | — | 鉄 |  |
| ドワーフの小剣 (dwarvish short sword) | 1d7 / 1d8 | 30 | 10 | — | 鉄 |  |

:::
"""

segments["step_265"] = """#### サーベル (Saber)
<!-- audit
2026-05-19:
- 10 saber cells verified clean (objects.h)
- Grayswandir is a SILVER_SABER artifact, PHYS(5,0): +1d5 to-hit and double damage (artilist.h:170, artifact.c:1083-1086, 1106-1107)
- Werebane is also a silver saber artifact (artilist.h:166); +d5 vs lycanthropes via SPFX_DFLAG2 M2_WERE
- inline effects deferred to Artifacts chapter rather than duplicated
-->

片手持ち近接武器。銀のサーベルを母体とするアーティファクト形態（グレイスワンディール、獣の災い）は、ゲーム内屈指の強力な片手武器です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| シミター (scimitar) | 1d8 / 1d8 | 40 | 15 | — | 鉄 |  |
| 銀のサーベル (silver saber) | 1d8 / 1d8 | 40 | 75 | — | 銀 | 銀特効により悪魔、獣人、吸血鬼、小悪魔に追加ダメージ。アーティファクト形態：**グレイスワンディール (Grayswandir)** および **獣の災い (Werebane)**（[アーティファクト一覧](#artifacts)参照）。 |

:::
"""

segments["step_266"] = """#### 幅広の剣 (Broadsword)
<!-- audit
2026-05-19:
- Stormbringer's base item is RUNESWORD, NOT broadsword (artilist.h:93)
- runesword and broadsword share P_BROAD_SWORD skill and 1d4+1d4 / 1d6+1 dice, hence the confusion
- artifact details kept in the Artifacts chapter, not duplicated here
-->

片手持ち近接武器。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 幅広の剣 (broadsword / ninja-to: 忍者刀) | 1d4+1d4 / 1d6+1 | 70 | 10 | — | 鉄 |  |
| エルフの幅広の剣 (elven broadsword) | 1d6+1d4 / 1d6+1 | 70 | 10 | — | 木 |  |
| ルーンの剣 (runesword) | 1d4+1d4 / 1d6+1 | 40 | 300 | — | 鉄 | ストームブリンガー (Stormbringer) は混沌のアーティファクト形態。 |

:::
"""

segments["step_267"] = """#### 長剣 (Long sword)
<!-- audit
2026-05-19:
- long sword stats verified (objects.h:270-280)
- Excalibur dipping requires LONG_SWORD, XL >= 5, quan == 1, not already artifact, no extant Excalibur (fountain.c:404-408)
- dip roll: !rn2(6) for Knights, !rn2(30) otherwise (fountain.c:405)
- non-Lawfuls get the sword cursed, spe possibly decremented, oerodeproof cleared (fountain.c:411-421)
- LONG_SWORD artifacts: Excalibur, Frost Brand, Fire Brand, Giantslayer, Vorpal Blade, Sunsword (artilist.h:85, 149, 153, 174, 191, 209)
- Vorpal Blade is a LONG_SWORD artifact, NOT a two-handed sword (artilist.h:191)
- two-handed sword has no dedicated artifact (no TWO_HANDED_SWORD entries in artilist.h)
-->

片手持ち近接武器。秩序属性の長剣は、序盤で単一武器として最も大きな見返りを得られる「泉への浸しによるエクスカリバー入手」の対象となります。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 長剣 (long sword) | 1d8 / 1d12 | 40 | 15 | — | 鉄 | 経験レベル5以上で泉に浸すと、1/30の確率（騎士は1/6）で判定が行われる。成功時、秩序属性のキャラクターは**エクスカリバー (Excalibur)** を獲得する。それ以外の属性では剣が呪われる。アーティファクト形態：エクスカリバー、フロストブランド、ファイヤーブランド、巨人殺し、ヴォーパルブレード、サンソード。 |
| 刀 (katana) | 1d10 / 1d12 | 40 | 80 | +1 | 鉄 | 武器自体に+1の命中補正が組み込まれている。スニッカースニー (Snickersnee) がアーティファクト形態。 |

:::
"""

segments["step_268"] = """#### 両手剣 (Two-handed sword)
<!-- audit
2026-05-19:
- two-handed sword stats verified (objects.h:273-285)
- 5.0 bimanual weapons get 3/2 Str damage bonus, melee only (uhitm.c:1467-1468; gated on bimanual(uwep) + HMON_MELEE)
- bonus also applies to battle-axe, dwarvish mattock, bardiche
- Tsurugi is the two-handed sword artifact (artilist.h:285-289); Vorpal Blade is a LONG_SWORD (artilist.h:191), NOT the artifact form here
-->

両手持ち武器は 5.0 において**筋力ダメージに 1.5 倍（3/2）のボーナス**を受けます。筋力によるダメージ補正値が 1.5 倍されます。下記の高い基本ダイス値と合わさることで、盾の装備枠を放棄しなければならないにもかかわらず、両手剣が片手武器＋盾の構成に匹敵する大きな理由となっています。
このボーナスは戦斧、ドワーフのつるはし、バーディックなど、あらゆる両手持ち武器に適用されます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 両手剣 (two-handed sword) | 1d12 / 1d6+2d6 | 150 | 50 | — | 鉄 | 両手持ち（盾および利き手以外の武器の併用不可）。 |
| 大刀 (tsurugi) | 1d16 / 1d8+2d6 | 60 | 500 | +2 | 金属 | 両手持ち。村正の大刀 (The Tsurugi of Muramasa) がアーティファクト形態。 |

:::
"""

segments["step_269"] = """#### 斧 (Axe)
<!-- audit
2026-05-19:
- axe 1d6/1d4, battle-axe 1d8+1d4 small / 1d6+2d4 large with bonus dice (objects.h:236-241, weapon.c:251-289)
- both use P_AXE skill; battle-axe is bimanual and gets 3/2 Str damage bonus in melee (uhitm.c:1467-1468)
- Cleaver is the BATTLE_AXE artifact (artilist.h:114-116)
-->

近接武器。通常の斧は片手持ちです。戦斧（battle-axe）は両手持ち（筋力ダメージ 1.5 倍ボーナス適用）となります。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 斧 (axe) | 1d6 / 1d4 | 60 | 8 | — | 鉄 |  |
| 戦斧 (battle-axe) | 1d8+1d4 / 1d6+2d4 | 120 | 40 | — | 鉄 | 両手持ち（5.0の筋力ダメージ 1.5 倍ボーナス適用）。小型に+1d4、大型に+2d4。野蛮人（Barbarian）のクエストアーティファクトである**なた (Cleaver)** は戦斧が母体。 |

:::
"""

segments["step_270"] = """<!-- audit
2026-05-19:
- pick-axe: WEPTOOL, wt 100, cost 50, 1d6/1d3, iron (objects.h:1007-1009)
- mattock stats verified (objects.h:345-347)
- both share P_PICK_AXE skill and route through use_pick_axe (apply.c:4290-4292)
- mattock is bimanual: gets 3/2 Str damage bonus in melee (uhitm.c:1467-1468)
- dig-down creates a pit, then a hole (dig.c:432-433, 372-374)
-->
#### つるはし (Pick-axe)

近接武器かつ掘削道具。`a` (apply) キーで使用することで、任意の方向の壁や床を掘り進めることができます。ドワーフのつるはしも同様の機能を持ち、こちらは両手持ちです。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| つるはし (pick-axe) | 1d6 / 1d3 | 100 | 50 | — | 鉄 | 武器道具（Weapon-tool）。使用（apply）することで壁を掘り崩したり、床を掘り抜く（落とし穴、続いて穴を作成）ことができる。ドワーフのつるはしと同じ `pick-axe` スキル。 |
| ドワーフのつるはし (dwarvish mattock) | 1d12 / 1d8+2d6 | 120 | 50 | −1 | 鉄 | 両手持ち（筋力ダメージ 1.5 倍ボーナス適用）。つるはし同様に壁を掘り崩せる。わずかな命中ペナルティ（−1）。 |

:::
"""

segments["step_271"] = """#### こん棒 (Club)
<!-- audit
2026-05-19:
- club and aklys stats verified (objects.h:371-373, 381-383)
- starting inventory uses blessorcurse(otmp, 10): roughly 10% chance any starter item is cursed (mkobj.c:876-885)
- club is a Caveman starter
- aklys returns when thrown only if wielded (W_WEP), with ~1% misfire (dothrow.c:30-34, 1710-1759)
-->

打撃系の片手近接武器。アキリスは革紐で繋がれており、主武器として手に持った状態で投擲すると手元に戻ってきます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| こん棒 (club) | 1d6 / 1d3 | 30 | 3 | — | 木 | 洞窟人（Caveman）の初期装備。 |
| アキリス (aklys) | 1d6 / 1d3 | 15 | 4 | — | 鉄 | 主武器として装備中に投げると手元に戻ってくる（紐付き）。ごく稀に投げ損ない（不発）が発生する。 |

:::
"""

segments["step_272"] = """#### メイス (Mace)
<!-- audit
2026-05-19:
- mace stats verified (objects.h:355-361)
- Demonbane PHYS(5,0): +1d5 to-hit and double damage vs demons (artifact.c:1083-1085 spec_abon, 1106-1107 spec_dbon); also has banish invoke
- silver mace: +1d20 vs mon_hates_silver targets (uhitm.c:1376-1377)
- silver hates list: demons, weres, vampires, shades, most imps (mondata.c:524-528)
- silver does NOT hit "undead" or "shape-changers" generally (mummies, zombies, ghosts, chameleons excluded)
- Mjollnir is a war hammer, NOT a mace (artilist.h:109 `A("Mjollnir", WAR_HAMMER, ...)`)
-->

片手持ちの打撃系近接武器。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| メス (mace) | 1d6+1 / 1d6 | 30 | 5 | — | 鉄 | 僧侶（Priest）が生贄の捧げ物で最初に確定入手するアーティファクト「デーモンベイン (Demonbane)」の母体：悪魔に対して命中+1d5かつダメージ2倍の銀のメイス、さらに追放効果の発動（invoke）付き。 |
| 銀のメイス (silver mace) | 1d6+1 / 1d6 | 36 | 60 | — | 銀 | 悪魔、獣人、吸血鬼、影、大半の小悪魔に対して+1d20の追加ダメージ。 |

:::
"""

segments["step_273"] = """#### モーニングスター (Morning star)
<!-- audit
2026-05-19:
- morning star: 1d4+1d4 / 1d6+1, wt 120, cost 10, hit 0, iron (objects.h:363-365, weapon.c:225-289)
- P_MORNING_STAR is its own skill, distinct from P_MACE (skills.h:35)
- Trollsbane IS a MORNING_STAR artifact: regenerates while wielded, +d5 vs trolls (artilist.h:182-184)
-->

片手持ちの打撃系近接武器。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| モーニングスター (morning star) | 1d4+1d4 / 1d6+1 | 120 | 10 | — | 鉄 | 小型に+1d4、大型に+1。片手武器として堅実なダメージ力を誇る。 |

:::
"""

segments["step_274"] = """#### フレイル (Flail)
<!-- audit
2026-05-19:
- flail: base 1d6/1d4, +1 small (weapon.c:272-275), +1d4 large (weapon.c:239-243); objects.h:384-386
- grappling hook: 1d2/1d6, WEPTOOL that trains P_FLAIL (objects.h:1010-1012)
- grappling hook #apply pulls target toward you; range 4 (P_NONE/Basic), 5 (Skilled), 8 (Expert+) (apply.c:3686-3698)
- no flail artifact
-->

片手持ちの打撃系近接武器。同じスキルを修練できる実用的な道具として鍵縄（grappling hook）も含まれます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| フレイル (flail / nunchaku: ヌンチャク) | 1d6+1 / 1d4+1d4 | 15 | 4 | — | 鉄 | 小型に+1、大型に+1d4。片手持ち。 |
| 鍵縄 (grappling hook) | 1d2 / 1d6 | 30 | 50 | — | 鉄 | フレイルスキルを修練可能。使用（apply）すると2マス先のアイテムを引き寄せたり、超小型モンスターを引き寄せたり、自分自身を1歩引き寄せることができる。 |

:::
"""

segments["step_275"] = """#### ハンマー (Hammer)
<!-- audit
2026-05-19:
- war hammer stats verified (objects.h:367-369, weapon.c); +1 small bonus matches sdam/ldam fields
- Mjollnir can be gifted to ANY Valkyrie, not just Neutral: hack_artifacts fixes alignment to player's initalign (artifact.c:92-95)
- aklys uses P_CLUB and is correctly placed elsewhere
-->

片手持ちの打撃系近接武器。ワルキューレ（Valkyrie）のアーティファクトであるウォーハンマー「ミョルニル (Mjollnir)」は、投擲すると手元に戻ってきます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| ウォーハンマー (war hammer) | 1d4+1 / 1d4 | 50 | 5 | — | 鉄 | ミョルニル (Mjollnir) がアーティファクト形態（ワルキューレへの生贄の賜物。属性はプレイヤーの初期属性に一致する）。 |

:::
"""

segments["step_276"] = """#### 六尺棒 (Quarterstaff)
<!-- audit
2026-05-19:
- quarterstaff: bimanual, 1d6/1d6, wt 40, cost 5, WOOD, P_QUARTERSTAFF (objects.h:377-379).
- Wizard starter weapon (u_init.c:168).
- bimanual: gets 3/2 Str damage bonus in melee (uhitm.c:1467).
- Expert caps: Wizard, Priest, Healer, Caveman (u_init.c:314,334,396,555 P_QUARTERSTAFF=P_EXPERT).
- No Knight or Rogue entry: P_QUARTERSTAFF absent from Skill_K and Skill_R (u_init.c:346-413).
-->

両手持ち近接武器。控えめな基本ダイス値にもかかわらず、筋力ダメージ 1.5 倍（3/2）ボーナスが適用されます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 六尺棒 (quarterstaff) | 1d6 / 1d6 | 40 | 5 | — | 木 | 両手持ちだが軽量。魔法使い（Wizard）の初期装備。 |

:::
"""

segments["step_277"] = """#### 長柄武器 (Polearms)
<!-- audit
2026-05-19:
- 12 polearm rows verified: all two-handed, all P_POLEARMS, all iron (objects.h:294-341).
- per-row dice/weight/cost from objects.h:294-341 WEAPON() macros; +d4/+d6 vs-large bonuses applied in weapon.c dmgval.
- polearm reach is skill-dependent, NOT a fixed 2 squares (apply.c:3355-3382).
- use_pole has NO "empty intervening square" check (apply.c:3355-3382).
- polearms CAN bash an adjacent monster (uhitm.c:1467-1484).
- adjacent polearm bash: damage clamps to 1d2 base, no weapon-skill bonus, Strength still applies (uhitm.c:1075-1086, 1447-1469).
-->

すべての長柄武器は両手持ちです。離れた敵を攻撃するには、武器を手に持って通常攻撃するのではなく、`#apply`（使用）コマンドを使います。ベーシック（入門）スキルでは直線2マス先の敵を攻撃でき、熟練（エキスパート）になるとさらに攻撃可能な位置が広がります。長柄武器を持った状態で隣接するモンスターを通常攻撃することも可能ですが、強打（打撃）扱いとなり、ボーナス加算前の基本ダメージが 1d2 に制限され、武器スキルによるダメージボーナスも乗りません（筋力補正は適用されます）。この「間合い（リーチ）」こそが、長柄武器を持ち歩く最大の意義です。各武器の追加ダメージの詳細は下記の備考を参照してください。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| パルチザン (partisan) | 1d6 / 1d6+1 | 80 | 10 | — | 鉄 | リーチ攻撃可能。 |
| ランサー (ranseur) | 1d4+1d4 / 1d4+1d4 | 50 | 6 | — | 鉄 | 小型に+1d4、大型に+1d4。 |
| スペタム (spetum) | 1d6+1 / 1d6+1d6 | 50 | 5 | — | 鉄 | 小型に+1、大型に+1d6。 |
| グレイブ (glaive / naginata: 薙刀) | 1d6 / 1d10 | 75 | 6 | — | 鉄 | リーチ攻撃可能。 |
| ハルバード (halberd) | 1d10 / 1d6+1d6 | 150 | 10 | — | 鉄 | 大型に+1d6。 |
| バーディック (bardiche) | 1d4+1d4 / 1d4+2d4 | 120 | 7 | — | 鉄 | 小型に+1d4、大型に+2d4。 |
| ヴォウジェ (voulge) | 1d4+1d4 / 1d4+1d4 | 125 | 5 | — | 鉄 | 小型に+1d4、大型に+1d4。 |
| フォシャール (fauchard) | 1d6 / 1d8 | 60 | 5 | — | 鉄 | リーチ攻撃可能。 |
| ギザルム (guisarme) | 1d4+1d4 / 1d8 | 80 | 5 | — | 鉄 | 小型に+1d4。 |
| ビル・ギザルム (bill-guisarme) | 1d4+1d4 / 1d10 | 120 | 7 | — | 鉄 | 小型に+1d4。 |
| ルッツェルンハンマー (lucern hammer) | 1d4+1d4 / 1d6 | 150 | 7 | — | 鉄 | 小型に+1d4。 |
| ベック・ド・コルバン (bec de corbin) | 1d8 / 1d6 | 100 | 8 | — | 鉄 | リーチ攻撃可能。 |

:::
"""

segments["step_278"] = """#### 槍 (Spear)
<!-- audit
2026-05-19:
- 6 spear rows (spear/elven/orcish/dwarvish/silver/javelin) verified P_SPEAR (objects.h:174-191).
- silver spear: SILVER material, cost 40, +d20 vs silver-haters (objects.h:186-188; artifact.c spec_dbon).
- Valkyrie starts with a plain spear and trains to Expert (u_init.c:160-161, 537).
- spear kebab bonus: +2 to-hit vs xorns, dragons, jabberwocks, nagas, giants (weapon.c:71-73, 167-168, is_spear).
- trident uses P_TRIDENT, a separate skill from spears (objects.h:195 P_TRIDENT).
- +1 thrown-spear multishot belongs to Caveman (PM_CAVE_DWELLER), NOT Valkyrie (dothrow.c:47-52).
- Valkyrie has no class-specific spear multishot, only the generic Expert ceiling (dothrow.c).
-->

槍類はすべて同じスキルを共有します。トライデントは別のスキルを使用します（後述）。ワルキューレ（Valkyrie）は通常の槍を持ってスタートし、エキスパートまで鍛えることができます。槍の投擲マルチショットの真のスペシャリストは**洞窟人（Caveman）**です。洞窟人は投げた槍（通常の槍、銀の槍、ジャベリンのいずれでも）に対してマルチショット+1のボーナスを得るため、束ねたジャベリンは彼らにとって強力な遠距離攻撃手段となります。

槍は大型モンスター（ゾーン、ドラゴン、ジャバウォック、ナーガ、巨人）に対して**命中+2のボーナス**（串刺しボーナス / kebab bonus）を得られます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 槍 (spear) | 1d6 / 1d8 | 30 | 3 | — | 鉄 | 投擲可能。ワルキューレの初期装備。 |
| エルフの槍 (elven spear) | 1d7 / 1d8 | 30 | 3 | — | 木 |  |
| オークの槍 (orcish spear) | 1d5 / 1d8 | 30 | 3 | — | 鉄 |  |
| ドワーフの槍 (dwarvish spear) | 1d8 / 1d8 | 35 | 3 | — | 鉄 |  |
| 銀の槍 (silver spear) | 1d6 / 1d8 | 36 | 40 | — | 銀 | 悪魔や獣人に対して銀特効ダメージ。 |
| ジャベリン (javelin) | 1d6 / 1d6 | 20 | 3 | — | 鉄 | スタック可能な投擲武器。洞窟人は遠距離から連射できる。 |

:::
"""

segments["step_279"] = """#### トライデント (Trident)
<!-- audit
2026-05-19:
- trident stats verified (objects.h:195)
- the +1/+2d4 large-creature bonus is the universal land bonus, NOT trident-specific (weapon.c:251-276)
- trident's signature bonus: +4 to-hit vs swimmers in water, +2 vs eels and snakes (weapon.c:170-176 hitval, not dmgval)
-->

片手持ち近接武器で、槍とは異なる独立したスキルを使用します。水中で戦う際にその真価を発揮する特徴的なボーナスを備えています。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| トライデント (trident) | 1d6+1 / 1d4+2d4 | 25 | 5 | — | 鉄 | 片手持ち。**水中の遊泳モンスターに対して命中+4、ウナギやヘビに対して命中+2**：トライデント固有の特徴的なボーナス。水辺以外では標準的なサイドアームとして機能する。 |

:::
"""

segments["step_280"] = """<!-- audit
2026-05-19:
- lance: P_LANCE, one-handed, IRON, 1d6/1d8 (objects.h:349)
- on foot lance still hits and damages normally, just NO joust bonus
- mounted joust bonus: +2d10 primary, +2d2 off-hand (objects.h:351-352, uhitm.c:1546)
- shatter chance 1/250 per successful joust (uhitm.c:2123-2125, 1559)
-->
#### ランス (Lance)

騎乗戦闘に特化して作られた近接武器。馬などの騎乗中に命中させると、馬上槍試合（Joust）による強大な追加ダメージを与えるチャンスがあります。徒歩でも有用な間合い攻撃（リーチ）武器として機能し、2マス離れた敵に使用（apply）して攻撃できます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| ランス (lance) | 1d6 / 1d8 | 180 | 10 | — | 鉄 | 片手持ち。騎乗攻撃が命中すると馬上槍試合（Joust）判定が発生し、主武器なら+2d10、利き手以外の武器なら+2d2の追加ダメージを与える。成功した馬上攻撃の約1/250の確率でランスが砕け散る。徒歩でも長柄武器のような間合い攻撃は維持されるが、馬上ボーナスは得られない。 |

:::
"""

segments["step_281"] = """<!-- audit
2026-05-19:
- rubber hose and bullwhip stats verified; P_WHIP skill (objects.h:374-376, 390-392, skills.h:49)
- bullwhip #apply can disarm (apply.c:3127-3174) and yank from a pit (apply.c:3069-3125)
- rubber hose does NOT damage shades: it's PLASTIC, shade_glare needs SILVER (artifact.c:555-562, weapon.c:307-308)
- rubber hose prob=0: never randomly spawns (objects.h:374-376 WEAPON row, probability field is 0)
- Archeologist starts with bullwhip +1 at Basic (apply.c:2992-2993)
- no whip artifacts
-->
#### 鞭 (Whip)

軽量な片手近接武器であり、実用的な道具でもあります。鞭を `#apply`（使用）することで、隣接するモンスターの武器を叩き落としたり（武装解除）、落とし穴から自分自身を引き上げたりできます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| ゴムホース (rubber hose) | 1d4 / 1d3 | 20 | 3 | — | プラスチック | ジョーク武器。自然生成されることはない。キーストン・コップ（お巡りさん）が所持していることがある。 |
| 鞭 (bullwhip) | 1d2 / 1 | 20 | 4 | — | 革 | 考古学者（Archeologist）の初期装備。使用（apply）することで隣接モンスターの武器を叩き落としたり（相手が武器を装備している場合のみ）、落とし穴から脱出するために自身を引き上げることができる（近くの岩、家具、大型モンスターに巻き付ける）。 |

:::
"""

segments["step_282"] = """<!-- audit
2026-05-19:
- 5 PROJECTILE arrow rows (objects.h:141-154); 4 BOW launcher rows (objects.h:395-402).
- arrows: 1d6/1d6 (1d7/1d6 elven, 1d5/1d6 orcish, 1d6/1d6 silver) wt 1, cost 2 (objects.h:141-152).
- ya: 1d7/1d7, +1 hit, METAL, cost 4 (objects.h:153-154).
- yumi prob=0: Samurai-only, never randomly spawns (objects.h:401-402).
-->
#### 弓 (Bow)

片手持ちの発射具（ランチャー）。弓を手（主武器）に装備し、矢筒に矢を入れて `f` キーで発射します。エキスパートの射手はマルチショット（一斉射撃）が可能で、野伏（Ranger）と侍（Samurai）がそのスペシャリストです。弓は二刀流戦闘を阻害しますが、盾を装備することは可能です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 矢 (arrow) | 1d6 / 1d6 | 1 | 2 | — | 鉄 | すべての弓で使用可能。 |
| エルフの矢 (elven arrow) | 1d7 / 1d6 | 1 | 2 | — | 木 | エルフの弓から放つと最適（エルフの一斉射撃ボーナス）。 |
| オークの矢 (orcish arrow) | 1d5 / 1d6 | 1 | 2 | — | 鉄 | オークの弓から放つと最適（オークの一斉射撃ボーナス）。 |
| 銀の矢 (silver arrow) | 1d6 / 1d6 | 1 | 5 | — | 銀 | すべての弓で使用可能。悪魔や獣人に対して銀特効ダメージ。 |
| 竹矢 (ya) | 1d7 / 1d7 | 1 | 4 | +1 | 金属 | 和弓から放つと最適（侍の一斉射撃ボーナス）。 |
| 弓 (bow) | — | 30 | 60 | — | 木 | あらゆる矢を発射可能。 |
| エルフの弓 (elven bow) | — | 30 | 60 | — | 木 | エルフの矢と組み合わせると真価を発揮。 |
| オークの弓 (orcish bow) | — | 30 | 60 | — | 木 | オークの矢と組み合わせると真価を発揮。 |
| 和弓 (yumi) | — | 30 | 60 | — | 木 | 侍専用の弓。竹矢と組み合わせると最適。 |

:::
"""

segments["step_283"] = """<!-- audit
2026-05-19:
- crossbow bolt: 1d4 / 1d6, NO +1 bonus (objects.h:155-156 PROJECTILE)
- crossbows CAN multishot: requires Str 18 (Str 16 for gnomes), with +1 baseline gnome bonus (dothrow.c:225-231, 205-209)
- skill caps: Rogue Expert, Ranger Expert, Knight Skilled (u_init.c)
- Valkyries cap at Unskilled, NOT Skilled: Skill_V has no P_CROSSBOW entry (u_init.c:525-547)
-->
#### クロスボゥ (Crossbow)

片手持ちの発射具。弓よりも1発あたりの威力が高くなっていますが、リロードが遅く、完全なマルチショットを行うには筋力 18（ノームは筋力 16）が必要です。弓と同様、二刀流は阻害しますが盾の装備は可能です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| クロスボゥボルト (crossbow bolt) | 1d4+1 / 1d6+1 | 1 | 2 | — | 鉄 | スタック可能。 |
| クロスボゥ (crossbow) | — | 50 | 40 | — | 木 | ボルトは敵を貫通する。**筋力 18**（ノームは 16）以上でマルチショットが通常通りのダイス判定となる。それ未満の場合、ゲームは2回ロールして小さい方の連射数を採用する。またノームはマルチショット数に+1される。盗賊と野伏はエキスパート、騎士は熟練まで習得可能。 |

:::
"""

segments["step_284"] = """<!-- audit
2026-05-19:
- sling stats verified (objects.h:403)
- sling skill trains from hits while wielding a sling, NOT from picking up rocks (weapon.c:1750)
- sling launches rocks, flint stones, and gems
- Caveman starts with one sling
-->
#### スリング (Sling)

片手持ちの発射具。弾薬は床に落ちている（または持ち運んでいる）石や宝石なら何でも使えるため、弾薬費は実質的にゼロです。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| スリング (sling) | — | 3 | 20 | — | 革 | 石、火打石、宝石を発射可能。洞窟人（Caveman）の初期装備。 |

:::
"""

segments["step_285"] = """<!-- audit
2026-05-19:
- dart stats verified (objects.h:161)
- darts are poisonable (is_poisonable)
- Tourist starts with 21-40 darts via trquan() = 21+rn2(20), NOT ~25-60 (u_init.c:150-151)
-->
#### 投げ矢 (Dart)

投擲専用。大量にスタックでき、重量がほとんどなく、病気の薬から毒を塗布することができます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 投げ矢 (dart) | 1d3 / 1d2 | 1 | 2 | — | 鉄 | 毒を塗布可能。観光客（Tourist）は+2に強化された束（約21〜40本）を持ってスタートする。 |

:::
"""

segments["step_286"] = """<!-- audit
2026-05-19:
- shuriken: 1d8/1d6, wt 1, cost 5, +2 hit, iron, PIERCE missile, P_SHURIKEN (objects.h:163)
- is_poisonable (obj.h:264-268)
- Samurai trains to Expert (u_init.c:481)
-->
#### 手裏剣 (Shuriken)

投擲専用。修道士（Monk）は手裏剣投擲時にマルチショット+1のボーナスを得られます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 手裏剣 (shuriken) | 1d8 / 1d6 | 1 | 5 | +2 | 鉄 |  |

:::
"""

segments["step_287"] = """<!-- audit
2026-05-19:
- boomerang stats verified (objects.h:166-168)
- boomerang does NOT always return: 10-step curved path that stops on monster, wall, door, or sink hits (zap.c:4148-4220 boomhit; loop ct<10, breaks on isok, monster, ZAP_POS or closed_door)
- catching the return requires a Dex check, auto-fails if Fumbling; a missed catch hits the thrower
- enchanted boomerang hits (spe+1) times
- useless underwater
-->
#### ブーメラン (Boomerang)

投擲専用。放物線を描いて飛行し、途中の軌道が遮られていなければ投げた本人の手元へ戻ってきます。戻ってきたブーメランをキャッチするには器用さ（Dex）の判定が必要です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| ブーメラン (boomerang) | 1d9 / 1d9 | 5 | 20 | — | 木 | 障害物のない経路なら弧を描いて手元に戻る。モンスター、壁、扉、流し台（シンク）に当たると止まる。器用さが低いか、あるいは「お手玉（Fumbling）」状態のときは顔面に直撃してダメージを受ける。 |

:::
"""

# Write out the segments
for step_id, content in segments.items():
    filepath = os.path.join("docs", "segments_ja", f"{step_id}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Written {filepath}")

