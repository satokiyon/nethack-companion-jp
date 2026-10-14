# -*- coding: utf-8 -*-
"""
Generate segments for step_355 to step_364 (Intrinsics & Extrinsics, What Changed).
"""
import os

segments = {}

segments["step_355"] = """### 固有能力および外在能力一覧表 (Intrinsic and Extrinsic Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Sleep res: dropped "dark one" (G_NOCORPSE). Shock res: dropped "shocking sphere" (G_NOCORPSE). Teleport: dropped "homunculus" (no M1_TPORT). All leave no corpse / don't convey.
- Magic resistance: no role grants it intrinsically; removed "Wizard XL 17" (that's teleport control, attrib.c:86-88).
- Teleport control: carrying the Amulet of Yendor BLOCKS controlled teleport (teleport.c:1185), it doesn't grant it.
- Verified correct: all other role/race intrinsic gain levels, ring/amulet/dragon-scale grants.
-->
<!-- audit
2026-06-01:
- property list from include/prop.h:14-93 (68 enum entries; we cover the player-attainable subset and skip trouble states and INVULNERABLE)
- role intrinsic gain levels from src/attrib.c:23-105 (innate structs per role: arc/bar/cav/hea/kni/mon/pri/ran/rog/sam/tou/val/wiz)
- race intrinsic gain levels from src/attrib.c:91-103 (dwa_abil, elf_abil, gno_abil, orc_abil)
- corpse intrinsic conferral logic at src/eat.c:903-951 (intrinsic_possible() — mconveys & MR_X check per resistance)
- give-rate formula at src/eat.c:961-997 (chance=15 standard; chance=4 for killer-bee/scorpion poison; chance=1 telepathy; chance=10 teleport; chance=12 teleport control; chance=6 stone temp; chance=3 acid temp; (ptr->mlevel > rn2(chance)) gates the grant)
- prayer-conferred intrinsics at src/pray.c:814,817,1321-1325 (HFire_resistance / HSleep_resistance / HFast / HStealth |= FROMOUTSIDE)
- dragon scale base property at include/objects.h:497-553 (DRGN_ARMR macros — each color's primary granted property; gold has no power, shimmering is DEFERRED)
- dragon scale special secondary effects at src/do_wear.c:798-884 (dragon_armor_handling switch: black=drain res, blue=fast, green=sick res, red=infravision, orange=free action, yellow=stone res, white=slow digestion, gold=affects hallucination state)
- ring grants at include/objects.h:741-827 (RING macro 3rd arg = granted property)
- amulet grants at include/objects.h:835-862 (AMULET macro 3rd arg = granted property)
- helm of caution grants WARNING (objects.h:479-481)
- helm of telepathy grants TELEPAT (objects.h:485-487)
- cornuthaum grants CLAIRVOYANT to Wizard role only (objects.h:457-461)
- alchemy smock grants POISON_RES (objects.h:630-632)
- elven boots grant STEALTH (objects.h:715-717); elven cloak grants STEALTH (objects.h:615-617)
- jumping boots grant JUMPING (objects.h:712-714)
- water walking boots grant WWALKING (objects.h:709-711)
- speed boots grant FAST (objects.h:707-709)
- levitation boots grant LEVITATION (objects.h:725-727)
- shield of reflection grants REFLECTING (objects.h:677-679)
- shield of drain resistance NEW in 5.0 (objects.h:656-658)
- shield of shock resistance NEW in 5.0 (objects.h:659-661)
- cloak of protection grants PROTECTION + MC3 (objects.h:637-641)
- cloak of magic resistance grants ANTIMAGIC + MC1 (objects.h:644-646)
- cloak of invisibility grants INVIS (objects.h:641-643)
- cloak of displacement grants DISPLACED (objects.h:648-650)
- amulet of guarding grants PROTECTION + MC2 (objects.h:855-856)
- amulet of magical breathing grants MAGICAL_BREATHING (objects.h:852-854)
- amulet of life saving grants LIFESAVED (objects.h:838-839)
- amulet of unchanging grants UNCHANGING (objects.h:848-849)
- amulet of reflection grants REFLECTING (objects.h:850-851)
- amulet of ESP grants TELEPAT (objects.h:835-836)
- amulet of flying grants FLYING (objects.h:859-860)
- amulet versus poison grants POISON_RES (objects.h:844-845)
- Sunsword: extrinsic BLND_RES when wielded (artilist.h:209-212; youprop.h:160 EBlnd_resist comment)
- Magicbane grants ANTIMAGIC + ESP + stun while wielded (artilist.h:145-147; src/artifact.c handlers)
- Grayswandir grants HALLUC_RES via SPFX_HALRES (artilist.h:170; src/artifact.c:787)
- Dragonbane grants REFLECTING via SPFX_REFLECT (artilist.h:157-160; artifact.c:867)
- Eye of the Aethiopica grants ENERGY_REGENERATION + ESP carried (artilist.h:303-307; artifact.c:841)
- Heart of Ahriman grants LEVITATION + STEALTH (artilist.h:225-230)
- Sceptre of Might grants PROTECTION + CONFLICT (artilist.h:232-235)
- Orb of Detection grants HALF_SPDAM + ESP + INVIS (artilist.h:219-223)
- Master Key of Thievery grants TELEPORT_CONTROL + WARN + HALF_SPDAM + HALF_PHDAM (artilist.h:279-283)
- Platinum Yendorian Express Card grants ESP + HALF_SPDAM (artilist.h:291-295)
- Orb of Fate grants WARN + HALF_SPDAM + HALF_PHDAM (artilist.h:297-301)
- Longbow of Diana grants ESP + REFLECTING (artilist.h:271-274)
- Mitre of Holiness grants PROTECTION (artilist.h:265-269)
- Tsurugi of Muramasa grants PROTECTION (artilist.h:285-289)
- Trollsbane grants REGENERATION (artilist.h:182-184)
- Staff of Aesculapius grants REGENERATION + drain res (artilist.h:248-253)
- Orcrist warns of orcs via SPFX_WARN + M2_ORC (artilist.h:134-136)
- Sting warns of orcs (artilist.h:138-140)
- Grimtooth warns of elves via SPFX_WARN + M2_ELF (artilist.h:123-126)
- ANTIMAGIC and HALLUC_RES are separate properties in prop.h (12 vs 24); magic resistance doesn't automatically block hallucination
- BLND_RES intrinsic comes only from polyform into AD_BLND attack monsters per src/polyself.c:108; no corpse-grant path
- HALLUC_RES intrinsic comes only from polyform into AD_HALU attack monsters per src/polyself.c:88; no corpse-grant path
- SEE_INVIS not conveyed by any corpse per src/eat.c:1356 (intrinsic_possible returns false)
- PASSES_WALLS, SWIMMING, DETECT_MONSTERS: polyform-only, no player-attainable persistent source
-->

NetHack はプレイヤーに対して 68 種類もの特性（プロパティ）を追跡・管理しています。そのうち冒険者が積極的に獲得を目指すべき有用な能力は、大きく 5 つの系統（ダメージ耐性、感覚と知覚、移動と空間挙動、戦闘と防御、特殊・実用機能）に分類されます。下記の表は各能力の効果、および信頼できるすべての獲得源を**内在能力（Intrinsic: 死体の摂食、レベル上昇、種族、祈りから獲得）**と**外在能力（Extrinsic: 装備、所持品から獲得）**に分けて網羅したものです。

表を見るにあたり、4つの重要な基本ルールを把握しておきましょう：

- **死体からの獲得確率は通常、モンスターのレベルに比例して高くなる。** さまよう目は確実にテレパシーを付与します。また、酸耐性や石化耐性は標準的な耐性判定よりも有利な確率が設定されています。これらの有用な例外は表中で個別に明記しています。
- **内在能力と外在能力は重複（スタック）しない。** 同一の耐性を両方から得ていても、効果が2倍になるわけではありません。しかし両方を揃えておくことは**冗長性（バックアップ）**として極めて有用です。例えばクロークを脱いでも、内在能力があれば守られ続けます。
- **修道士（Monk）は全職業中最も幅広い耐性獲得ラダーを持つ。** レベル 1 から 17 にかけて 11 種類もの内在能力を自力で習得します。
- **ドラゴンの鱗鎧はあらゆるアイテムの中で最も多くの重要能力を網羅する。** 各色ごとに1つの基本耐性を備え、さらに複数の色が強力な*二次的効果*（黒は分解＋吸命耐性、青は電撃＋高速移動など）を併せ持ちます。完全な対応関係は表を参照してください。
"""

segments["step_356"] = """#### ダメージ耐性 (Damage resistances)

最も範囲が広く、最も活用される能力群です。大半は序盤に死体を食べることで獲得できます。魔法防御（Magic resistance）は獲得手段が極めて限られているため、昇天用装備セットでは防具、武器、アーティファクトの枠を1つ確保して補うのが基本です。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **火炎耐性** (Fire resistance) | 罠、ブレス、攻撃による火炎ダメージを無効化（溶岩への水没死は防げない）。 | 修道士 レベル11、僧侶 レベル20。赤ドラゴン、火蟻、火の巨人、ヘルハウンド、サラマンダー、赤色モールドの死体。溶岩からの祈り救済。 | 火炎耐性の指輪。赤ドラゴンの鱗 / 鱗鎧。 |
| **冷気耐性** (Cold resistance) | ブレスや攻撃による冷気ダメージを無効化。 | ワルキューレ レベル1、修道士 レベル13。白ドラゴン、霜の巨人、冬狼、茶色モールド、青色ゼリーの死体。 | 冷気耐性の指輪。白ドラゴンの鱗 / 鱗鎧。 |
| **睡眠耐性** (Sleep resistance) | 睡眠ガス、睡眠光線、モンスターの睡眠攻撃を完全無効化。 | 修道士 レベル1、エルフ レベル4。エルフ全般、ホムンクルスの死体。祈り救済。 | 橙色ドラゴンの鱗 / 鱗鎧。 |
| **分解耐性** (Disintegration resistance) | 黒ドラゴンの分解ブレスを無害化。 | 黒ドラゴンの死体。 | 黒ドラゴンの鱗 / 鱗鎧。 |
| **電撃耐性** (Shock resistance) | 電撃ブレスを含むすべての電撃ダメージを無効化。 | 修道士 レベル15。青ドラゴン、電気ウナギの死体。 | 電撃耐性の指輪。青ドラゴンの鱗 / 鱗鎧。電撃耐性の盾（5.0新要素）。 |
| **毒耐性** (Poison resistance) | 毒針、毒のある死体、毒ブレス、筋力を奪う毒攻撃を完全防御。 | 野蛮人 レベル1、医師 レベル1、オーク レベル1、観光客 レベル20、修道士 レベル3。殺人蜂やサソリの死体（獲得確率が極めて高い）。緑ドラゴン、ナーガ、クアジット等の毒死体。 | 毒耐性の指輪。毒の魔除け。錬金術の仕事着（クローク）。緑ドラゴンの鱗 / 鱗鎧。 |
| **酸耐性** (Acid resistance) | 酸ダメージを無効化。死体からの獲得は時間制限付きで、フロア移動でリセットされる。 | 酸のブロッブ、茶色プリン、黄ドラゴンの死体（高確率、時間制限あり）。 | 黄ドラゴンの鱗 / 鱗鎧（装備中恒久）。 |
| **石化耐性** (Stoning resistance) | 肉体の石化に対する完全免疫。死体からの獲得は一時的。黄ドラゴンの鎧は装備中持続。 | 酸のブロッブ、トカゲの死体（高確率、時間制限あり）。 | 黄ドラゴンの鱗 / 鱗鎧。 |
| **吸命耐性** (Drain resistance) | レイス、吸血鬼、生命力吸収武器（ストームブリンガー等）による経験値レベルドレインを遮断。 | 死体からは獲得不可。吸血鬼やリッチへの変身で獲得。 | 黒ドラゴンの鱗 / 鱗鎧。吸命耐性の盾（5.0新要素）。[エクスカリバー](#excalibur-artifact)、ストームブリンガー、[アスクレピオスの杖](#staff-of-aesculapius)の装備。 |
| **病気耐性** (Sickness resistance) | 致命的な病気や食中毒を遮断。 | 死体からは獲得不可。 | 緑ドラゴンの鱗 / 鱗鎧。 |
| **魔法防御** (Magic resistance) | 死の光線、マジックミサイル、変身ビーム、死の指の呪文を完全無効化。魔法の罠は防げない。[MC](#magic-cancellation)とは異なる。 | いかなる職業も内在習得不可。特定の変身形態で保有。 | 魔法を防ぐクローク。灰色ドラゴンの鱗 / 鱗鎧。[マジックベイン](#magicbane)の装備。 |
| **幻覚耐性** (Hallucination resistance) | 黒い光や幻覚の薬による幻覚状態を遮断。 | 幻覚攻撃を持つモンスター（黒い光等）への変身のみ。 | 金色ドラゴンの鱗 / 鱗鎧。[グレイスワンディール](#grayswandir)の装備。 |
| **盲目耐性** (Blindness resistance) | 黄色い光の閃光による盲目化を遮断。 | 盲目攻撃を持つモンスターへの変身のみ。 | [サンソード](#sunsword)の装備。 |

:::
"""

segments["step_357"] = """#### 感覚と知覚 (Senses and perception)

テレパシーと警告は、敵が接近する前にその存在と位置を正確に感知させてくれます。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **テレパシー** (ESP) | 盲目時にフロア全体の精神を持つモンスターを探知（視覚があるときは限定半径内）。 | さまよう目（確実獲得）、マインドフレア、マスターマインドフレアの死体。 | ESPの魔除け。テレパシーの兜。[アイソピアの目](#eye-of-the-aethiopica)（所持）、[探知の宝珠](#orb-of-detection)（所持）、[ヤンドールのExpressカード](#platinum-yendorian-express-card)（所持）、[ディアナの長弓](#longbow-of-diana)（所持）、[マジックベイン](#magicbane)（装備）。 |
| **不可視視認** (See invisible) | 透明な生物、および透明化した自分自身を視認できる。 | 修道士 レベル1、野伏 レベル15。死体からは獲得不可。 | 不可視視認の指輪。 |
| **警告** (Warning) | 約10マス以内にいるレベル4以上の敵対モンスターを感知表示（数字はモンスターレベル÷4）。 | 洞窟人 レベル15、医師 レベル15、修道士 レベル7、僧侶 レベル15、魔法使い レベル15。祈り救済。 | 警告の指輪。警戒の兜。[盗賊の合鍵](#master-key-of-thievery)、[運命の宝珠](#orb-of-fate)、[オクリスト](#bane-weapons)、[スティング](#bane-weapons)、[グリムトゥース](#bane-weapons)（すべて所持）。 |
| **特定種族への警告** | 特定の1種族に限定された警告表示。 | 内在能力としては存在しない。 | オクリスト / スティング（オーク警告）、グリムトゥース（エルフ警告）など。 |
| **探索** (Searching) | 約85ターンに1回自動的に周囲を探索し、隠し扉や通路、罠を発見する。 | 考古学者 レベル1、修道士 レベル9、野伏 レベル1、盗賊 レベル10、観光客 レベル10。 | 探索の指輪。[エクスカリバー](#excalibur-artifact)の所持。 |
| **透視** (Clairvoyance) | 周囲のダンジョン地形を周期的に魔法の眼で開拓視認。 | 内在能力としては存在しない。 | とんがり帽子（魔法使い専用）。 |
| **赤外線視覚** (Infravision) | 暗闇の中で熱源（温血生物）を感知。 | ドワーフ、エルフ、ノーム、オークの各種族（レベル1）。 | 赤ドラゴンの鱗 / 鱗鎧。 |

:::
"""

segments["step_358"] = """#### 移動と空間挙動 (Movement and spatial behavior)

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **高速移動** (Fast / intrinsic speed) | 各移動時に約1/3の確率で追加行動。実効速度が12から約16に向上。 | 修道士 レベル1、侍 レベル1、ワルキューレ レベル7、考古学者 レベル10、野蛮人 レベル7、洞窟人 レベル7、騎士 レベル7。祈り救済。 | 韋駄天の靴（**極めて高速 / Very Fast**、約2/3で追加行動、実効速度約20）。青ドラゴンの鱗 / 鱗鎧（極めて高速）。 |
| **跳躍** (Jumping) | `#jump` コマンドにより近くの任意のマスへ跳躍移動。 | 騎士 レベル1。 | 跳躍の靴。跳躍の呪文。 |
| **テレポート** (Teleportation / 不制御) | 数百ターンごとにランダムにテレポート。制御と組み合わせると極めて強力。 | テングの死体。 | テレポートの指輪。 |
| **テレポート制御** (Teleport control) | テレポート時に目的地の座標を自由に選択可能。 | 修道士 レベル17、魔法使い レベル17。テングの死体。 | テレポート制御の指輪。[盗賊の合鍵](#master-key-of-thievery)の所持。（イェンダーの魔除けの所持中は制御テレポートが**阻害**される）。 |
| **浮遊** (Levitation) | 常に宙に浮く。水面、溶岩、氷を渡れる。階段を降りられず、床の物を拾えない。 | なし。 | 浮遊の指輪。浮遊の靴（呪われていると脱げない）。[アリマンの心臓](#heart-of-ahriman)の所持。 |
| **飛行** (Flying) | 浮遊と同様だが、階段の昇降、アイテムの回収、任意着地が可能。 | 飛行モンスターへの変身。 | 飛行の魔除け（5.0新要素）。 |
| **水上歩行** (Water walking) | 水上や氷上を通常の床と同様に歩行可能。耐火加工された靴なら溶岩も渡れる。 | 特定モンスター（アンデッド等）への変身。 | 水上歩行の靴。 |
| **魔法の呼吸** (Magical breathing) | ウナギやクラーケンに巻き込まれても溺死せず、悪臭の雲の中でも生存可能。 | 内在能力としては存在しない。 | 魔法の呼吸の魔除け。 |

:::
"""

segments["step_359"] = """#### 戦闘と防御 (Combat and defense)

昇天用装備セットを支える多層防御：AC、反射、自由行動、自動回復など。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **防護** (Protection) | ACを改善（数値が低下）。また装備中の外在源1つにつき+1の[MC](#magic-cancellation)を付与（守護の魔除けは+2）。 | 平和的な僧侶への多額の寄付（必要金額はランダム）。 | 防護の指輪。守りのクローク（MC3併託）。守護の魔除け（MC2併託）。[力の笏](#sceptre-of-might)、[神聖なる司教帽](#mitre-of-holiness)、[村正の大刀](#tsurugi-of-muramasa)の所持。 |
| **反射** (Reflection) | 遠距離魔法攻撃（光線、ブレス）を術者へ跳ね返す。 | 内在能力としては存在しない。 | 反射の魔除け。銀ドラゴンの鱗 / 鱗鎧。反射の盾。[ドラゴンベイン](#bane-weapons)または[ディアナの長弓](#longbow-of-diana)の装備。 |
| **自動回復** (Regeneration) | 自然回復に加え、毎ターンHPが1回復する。 | トロール等の回復モンスターへの変身。 | 回復の指輪。[トロールベイン](#bane-weapons)または[アスクレピオスの杖](#staff-of-aesculapius)の装備。 |
| **魔力自動回復** (Energy regeneration) | 呪文の魔力（Pw）が急速に回復する。 | 内在能力としては存在しない。 | [アイソピアの目](#eye-of-the-aethiopica)の所持。 |
| **魔法半減** (Half spell damage) | モンスターが唱える呪文による被ダメージを半減。 | 内在能力としては存在しない。 | [探知の宝珠](#orb-of-detection)、[盗賊の合鍵](#master-key-of-thievery)、[ヤンドールのExpressカード](#platinum-yendorian-express-card)、[運命の宝珠](#orb-of-fate)の所持。 |
| **物理ダメージ半減** (Half physical damage) | 近接攻撃および物理遠距離攻撃による被ダメージを半減。 | 内在能力としては存在しない。 | [盗賊の合鍵](#master-key-of-thievery)または[運命の宝珠](#orb-of-fate)の所持。 |
| **自由行動** (Free action) | さまよう目、ゼラチンキューブ、グール、モンスターの呪文による麻痺を完全無効化。減速は防げない。 | 特定モンスターへの変身。 | 自由行動の指輪。橙ドラゴンの鱗 / 鱗鎧。 |
| **忍び足** (Stealth) | 睡眠中のモンスターの近くを歩いても目覚めさせず、気付かれずに通過できる。 | 考古学者 レベル5、野蛮人 レベル15、修道士 レベル5、野伏 レベル7、盗賊 レベル1、侍 レベル15、ワルキューレ レベル3。祈り救済。 | 忍び足の指輪。エルフの靴。エルフのクローク。[アリマンの心臓](#heart-of-ahriman)の所持。 |
| **不可視** (Invisibility) | 不可視視認を持たないモンスターはプレイヤーの正確なマスを見失うため命中率が激減。攻撃すると位置が露見する。 | ストーカーへの変身。不可視の薬（一時的）。 | 不可視の指輪。透明のクローク。[探知の宝珠](#orb-of-detection)の所持。 |
| **幻影** (Displacement) | モンスターの目にはプレイヤーが隣接する別のマスにいるように映り、遠距離攻撃が外れやすくなる。 | 内在能力としては存在しない。 | 幻影のクローク。 |

:::
"""

segments["step_360"] = """#### 特殊および実用能力 (Special and utility)

満腹度、変身、生存、群衆制御に関わる特殊能力です。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **消化遅延** (Slow digestion) | 通常の空腹進行を完全に停止。特殊な栄養吸収攻撃などによる飢餓は防げない。 | なし。 | 消化遅延の指輪。白ドラゴンの鱗 / 鱗鎧。 |
| **変身制御** (Polymorph control) | 罠、指輪、薬、杖、呪文によって変身する際、変身後の姿を自由に選択できる。 | なし。 | 変身制御の指輪。 |
| **不変** (Unchanging) | 現在の姿を固定する。あらゆる変身を防ぎ、*緑スライム化のカウントダウンも停止させる*。「スライムに触られた」際の標準的対処法。 | なし。 | 不変の魔除け。 |
| **能力維持** (Sustain ability) | 6大基本能力値（Str, Dex, Con, Int, Wis, Cha）が消耗、鍛錬、薬、毒などの能力低下攻撃によって変動しなくなる。 | なし。 | 能力維持の指輪。 |
| **変身生物除け** (Protection from shape changers) | 周囲のカメレオン、ドッペルゲンガー、サキュバス等の変身能力を封じる。 | なし。 | 変身生物除けの指輪。 |
| **紛争** (Conflict) | 周囲のモンスター同士を同士討ちさせる。効果に巻き込まれた店主はプレイヤーに敵対する。 | なし。 | 紛争の指輪。[力の笏](#sceptre-of-might)の所持。 |
| **命の救済** (Life saving) | 死亡時に魔除けが身代わりとなって破壊され、HPを `50 + 10 × (Con ÷ 2)`（最大HP上限）まで瞬時に全快復活させる。 | なし。 | 命の救済の魔除け。 |
| **装飾** (Adornment) | 指輪の強化値が魅力（Charisma）に加算される。買い物や誘惑対策に有用。 | なし。 | 装飾の指輪。 |

:::

一部の能力は実質的に**変身時限定**です：*遊泳*および*壁通過*（ゾーン、土の精、ゴースト）。*怪物探知*は杖や巻物による一過性のパルス効果としてのみ利用可能です。
"""

segments["step_361"] = """### 前回からの変更点 (What Changed Since Last Time)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- No "minimum sacrifice value" gate; value only caps artifact quality (pray.c:1784, artifact.c:195). Reworded.
- Sunsword #invoke costs 25 Pw (SPELL_LEV_PW(5)), not 5 (artifact.c:2095).
- "DSM gives two resistances" overstates: only black/green/yellow give two resistances; others give one + a perk (do_wear.c:806-883). Reworded.
- Crystal ball is a TOOL (objects.h:938); is_crackable needs ARMOR_CLASS (objclass.h:201), so it still shatters. Only crystal plate mail cracks.
- Gold DSM light radius is 3 (uncursed), not 2 (light.c:899-907).
- Verified correct: spell-level changes, touch-of-death rework, HP-regen formula, two-handed 3/2, Excalibur 1/30-vs-1/6, priest-donation randomization, unicorn-horn no-restore, BoH scatter, candle sqrt light, new monsters/conducts/shop mechanics.
-->
<!-- audit
2026-05-19:
- chain lightning is level 2 NODIR (objects.h:1409-1411 SPELL("chain lightning",..., P_ATTACK_SPELL, prob 25, delay 4, level 2, mgc 1, NODIR))
- "mummy withering" was fabricated; no such mechanic in 5.0
- Elbereth -5 alignment penalty is NOT a 5.0 change (engrave.c writeable_engrave, predates 5.0)
- supply chests appear strictly above the Oracle (mklev.c:1037 `u.uz.dlevel < oracle_level.dlevel`), not "the first ten levels"
- mind flayer: spell loss (uhitm.c:3266 losespells) and skill drain (uhitm.c:3270 drain_weapon_skill) persist; map/ID amnesia is gone (no forget_map call in eat_brains, eat.c:603)
- sink dipping is for potions only: non-potions just take water_damage (fountain.c:716-733)
- touch of death still has a binary success gate: without Antimagic, rn2(m_lev) > 12 applies the effect; Antimagic produces "Lucky for you, it didn't work!" (mcastu.c:391-407)
- the 5.0 change is the unprotected result: 50+8d6 damage plus half that amount drained from max HP instead of the old instadeath (mcastu.c:315-347; fixes5-0-0.txt:538)
- iron bars were added in 3.3.0, not 3.6 (fixes3-3-0.txt:349)
- gold dragon scale mail grants only hallucination resistance + innate light, not two resistances (do_wear.c:846-851, objects.h:505 DRGN_ARMR slot 0)
- bag-of-holding explosion scatters contents via scatter() rather than destroying them all; only 1/13 items vanish per is_boh_item_gone (pickup.c:2509-2532)
- death drops delobj() any rolled FOOD_CLASS item unless the monster has M2_COLLECT — corpses are still left (mon.c:3597-3604)
-->

NetHack 5.0.0 は 2026 年 5 月 2 日にリリースされました。旧バージョン（3.6.x 以前）の経験者の方は、まず以下の最初のグループから確認してください。これらは古い習慣や反射的行動がそのまま命取りとなる変更点です。
"""

segments["step_362"] = """#### 改めるべき古い習慣 {#new-dangers}

- **ユニコーンの角は低下した能力値を回復しなくなりました。** 能力値回復には能力回復の薬（または回復の魔法）を用意してください。
- **自分自身に振った加速の杖は恒久的な加速を付与しなくなりました。** 恒久加速には加速の薬が必要です。
- **希釈による錬金術は、1回の浸しで最大2服の薬しか変換できなくなりました。** 未希釈の薬同士の調合なら引き続きスタック一括変換が可能です。爆発確率は通常10%ですが、錬金術の仕事着を着ていれば約1/30に軽減されます。
- **ゲヘナの灼熱の床に薬を置くと、高確率で粉砕します。** また、魔王や大悪魔がフロア内で生存している間は、同一フロア内のテレポートも封殺されます。
- **モンスターが施錠されていない保管箱を漁り、適切な死体の山をアンデッドとして蘇生させるようになりました。** アイテムの保管庫を離れる際は、必ず箱に鍵をかけてください。
- **呪われた杖を文字彫りテストすると爆発することがあります。** 貴重そうな杖をテストする前に、可能な限りBUC（祝福・呪い）を識別してください。
- **低レベルモンスターの生贄では幸運値を稼げなくなりました。** 現在の幸運値が死体の難易度（モンスターレベル）を上回っている場合、生贄を捧げても幸運は上昇しません。幸運の維持には幸運の石を活用してください。
- **ワルキューレの初期装備が長剣から通常の槍に変更されました。** 経験レベル5以上の騎士によるエクスカリバーの泉浸し（1/6の確率）は健在ですが、他の秩序職業の成功率は1/30です。
- **死の指（Touch of death）の呪文は即死効果ではなくなりました。** 魔法防御がない場合、50+8d6 の大ダメージを受け、さらにその半分の値が最大HP上限から直接削り取られます（魔法防御があれば完全に防げます）。
"""

segments["step_363"] = """#### 新たな道具とチャンス (New Tools and Opportunities)

- **ドラゴンの鱗鎧が強力な二次効果を持つようになりました。** 黒は吸命耐性、緑は病気耐性、青は高速移動、橙は自由行動、白は消化遅延、赤は赤外線視覚を追加付与し、金は幻覚耐性に加えて半径3マスの恒久光源となります。
- **警戒の兜 (helm of caution)** が警告能力を付与します。**飛行の魔除け (amulet of flying)** は自身と騎乗ペットの両方に飛行を与え、**守護の魔除け (amulet of guarding)** は AC+2 および MC+2 を提供します。
- **複数のアーティファクトに発動効果や新能力が追加されました。** スニッカースニーは毎ターン1回無料の長柄武器スタイル間合い攻撃を繰り出せます。サンソードは25 Pwを消費して対象を盲目にします。トロールベインは装備中に自動回復します。デーモンベインは僧侶が生贄で最初に確定入手する銀のメイスとなりました。
- **新たな「願い」の入手源が登場しました。** ヴラドの玉座に座り続けることで最終的に願いを獲得でき、イェンダーの魔除けを最初に拾い上げた際にも願いが1回与えられます。またオルクスの町には魔法のランプまたは魔法のマーカーが確定生成されます。
- **祝福された変身の薬は、その1回の変身において変身先を自由に制御（選択）できます。** 変身した吸血鬼は `#monster` コマンドで吸血鬼、こうもり、霧の雲を自在に切り替えられます。
- **重石（ロードストーン）は呪われていても、接地している間は吹き飛ばし（ノックバック）を防ぎます。** 重量負担は依然として過酷ですが、使い道が生まれました。
- **補給の宝箱 (supply chests)** が神託所より上の浅い階層の約2/3の確率で出現し、序盤の回復や強化アイテムを提供してくれます。
- **ペットが死体を食べて耐性を獲得できるようになりました。** 死亡したペットも、その死体の上に乗って同属性の祭壇で祈ることで復活させることができます。
- **流し台（シンク）に薬を浸すと、メッセージによって薬が識別されます。** 薬は失われますが、識別の巻物を節約できます。
- **連鎖雷撃 (chain lightning)** が新たなレベル2の攻撃呪文として追加され、周囲の敵を次々と感電させます。通常フロアに新たな**テーマ別部屋**が生成されるようになり、4種の新モンスター（ディスプレイスビースト、遺伝子工学者、金ドラゴン、子金ドラゴン）が登場しました。
"""

segments["step_364"] = """#### その他の知っておくべき変更点 (Other Changes Worth Knowing)

- *魅了 (charm monster)* はレベル5、*睡眠 (sleep)* はレベル3、*怪物混乱 (confuse monster)* はレベル1に変更されました。魔法書を使用（apply）することで、本の磨耗度を確認できます。
- マインドフレアの触手攻撃は、マップの記憶や識別済みの記憶を消去しなくなりました。知力の低下、記憶していた呪文の忘却、武器スキルの経験値ドレインは依然として発生します。
- 軽量化の鞄の爆発は、中身を全消滅させるのではなくフロア中に散乱（scatter）させるようになりました（約1/13のアイテムは消滅します）。
- 僧侶への寄付金額がランダム化されました。防護を得るには、要求された金額の2倍以上3倍未満を寄付してください。それ以上寄付しても感謝されるだけで、過小な寄付は今後の要求額を引き上げます。
- 特殊フロアのマップが左右反転（ミラーリング）して生成されることがあり、暗記したマップが反転している場合があります。新たなコンダクトとして赤貧（Pauper）、ペットなし、完全聾、倉庫番、ボーンズなし、初期キャラ固定が公式記録されます。
- 両手持ち武器は筋力ダメージボーナスの 150%（1.5倍）を受けます。自然治癒によるHP回復は毎ターン `(XL + 耐久力)%` の確率判定となり、自動回復能力はそれに加えて毎ターン1 HPを回復します。
- 財宝に執着するモンスター（Covetous）は、どちらの階段へも逃走するようになりました。城のフロア生成時にマスターリッチやアーチリッチが初期配置されることはなくなりました。
- 水晶の鎧は段階的にひび割れ、耐ひび割れ加工が可能になりました。蝋燭による光源半径は線形ではなく平方根ルールで拡大します。
- 耐性を付与する死体、缶詰、卵は店での販売価格が高くなりました。モンスター死亡時に無関係な食料品をランダムドロップすることはなくなりました。
- 店主は店内の落とし穴や蜘蛛の巣を除去するようになり、平和的な店主に接触して歩き込むと自動的に借金を精算してから所持品確認プロンプトへ進みます。
"""

# Write out the segments
for step_id, content in segments.items():
    filepath = os.path.join("docs", "segments_ja", f"{step_id}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Written {filepath}")

