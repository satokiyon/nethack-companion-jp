#### 危険な罠 (Dangerous Traps)
<!-- audit
2026-05-20:
- random polymorph timer is rn1(500, 500) = 500-999 turns (polyself.c:813); decremented each turn until 0
- nohands or verysmall form on polymorph triggers break_armor() which dropx() drops worn gear to the floor (polyself.c:1248-1351)
2026-05-18:
- anti-magic implosion damage QUARTERED (not halved) for pass-walls: `dmgval2 = (dmgval2 + 3) / 4` (trap.c:2371-2372)
- max 4d4 raw damage caps at 4 after quartering (16+3)/4 = 4
- anti-magic damage composition: base 1d4 + 1d4 per half_physical/half_spell + 1d4 for wielding Magicbane + 1d4 for carrying first non-quest AD_MAGM artifact (trap.c:2351-2369; loop breaks on first match)
- cancellation on any magical trap detonates `20 + d(3,6)` at the square then removes trap (zap.c:3611-3621)
- ANTI_MAGIC counts as is_magical_trap (trap.h:121)
- polymorph trap is blocked entirely by Antimagic OR Unchanging (trap.c:2486-2489) — PolyControl only directs the change
- sleep gas: Sleep_resistance skips the fall_asleep branch in trapeffect_slp_gas_trap (trap.c:1570)
- iron footwear: blocks bear-trap leg damage (trap.c:1517-1518), blocks spiked-pit spikes (trap.c:1901-1903), blocks polymorph trap (trap.c:2478-2483)
- iron footwear absorbs an anti-magic drain by losing 1 enchantment, but only if spe>0 (trap.c:2328-2343)
- strategy aligned with NetHackWiki Fire trap, Anti-magic field, Polymorph trap: fire trap destroys scrolls/potions/spellbooks, MR makes anti-magic trap deal extra damage, MR/Unchanging block polymorph traps (https://nethackwiki.com/wiki/Fire_trap, https://nethackwiki.com/wiki/Anti-magic_field, https://nethackwiki.com/wiki/Polymorph_trap)
-->

| 罠の種類              | 効果                                        | 防御・軽減手段         |
| --------------------- | ------------------------------------------- | ---------------------- |
| 地雷 (Land mine)      | 爆発とアイテムの破損                        | 浮遊、または飛行       |
| 熊の罠 (Bear trap)    | その場に拘束される                          | 鉄製の履物で脚の怪我を防止 |
| 催眠ガスの罠 (Sleeping gas trap) | 数ターンの間無防備な睡眠状態になる   | 睡眠耐性               |
| 火炎の罠 (Fire trap)  | 炎でダメージを受け、露出した所持品が焼失する | 火炎耐性。巻物や薬は袋に入れる |
| 魔法の罠 (Magic trap) | ランダムな魔法効果（盲目とモンスター召喚等） | 汎用的な防御手段なし   |
| 反魔法フィールド (Anti-magic field) | 魔力を吸い取られる。ダメージを受けることもある | プラスに強化された鉄製の履物で吸収可能 |
| 変身の罠 (Polymorph trap) | ランダムな生物へと強制変身させられる    | 魔法防御、不変能力、または鉄製の履物 |
| 転がる巨石 (Rolling boulder) | 定められた軌道に沿って巨石が転がってくる | 軌道上から退避する     |

火炎の罠は、HPだけでなく手持ちの荷物全体を脅かします。炎そのもののダメージも痛いですが、最大の脅威はインベントリに起こる惨劇です：巻物は燃え尽き、薬の瓶は砕け散り、大事に溜め込んでいた20枚の「識別の巻物」の束が一瞬で灰と化します。[火炎耐性](#damage-resistances) は自身の肉体を守ってくれますが、**所持品までは守ってくれません**。普通の袋や防水袋の中に入れたアイテムは罠の火災から無事に生き残ります（袋自体が炎を吸収します）。[ゲヘナ (Gehennom)](#gehennom) は火炎の罠だらけの危険地帯ですので、消耗品は常に袋の中に退避させておきましょう。

[へんげ制御 (polymorph control)](#special-and-utility) を持っていれば、変身の罠を踏んでも変身後の姿を自分で選択できます。持っていない場合、罠が勝手に姿を決定し、装備品を何一つ身につけられないイモリに変えられてしまう恐れがあります。**[魔法防御 (Magic resistance)](#damage-resistances) および [不変 (Unchanging)](#special-and-utility) の内在能力は、どちらもこの強制変身を完全に遮断します。**

万が一、手のない生物へと強制変身させられてしまった場合、装備していた武具一式はその場（足元の床）にすべてドロップします。パニックにならず、むやみに動き回ってはいけません。ランダムな変身効果は数百ターンで自然に解けますし、大事な装備品は自分が立っているマスにまとまっています。可能であればそのマスを死守し、モンスターに追い詰められたら祈りを捧げ、元の姿に戻った瞬間にすべてを拾い直しましょう。（手持ちに変身の杖があるか呪文を習得していれば、自分自身に振りかけることで再抽選できますが、現在の形態が杖を使えるか呪文を唱えられる場合に限られます。）

催眠ガスは、モンスターの密集地帯では文字通り命取りになります。戦うことも、逃げることも、自発的に目を覚ますことすらできません。モンスターたちにとっては食べ放題のバイキングのように無抵抗なあなたに群がってきます。エルフの血統、オレンジドラゴンの鎧、あるいは適切な死体を食べて得る [睡眠耐性](#damage-resistances) によって完全に無力化できます。

魔法の罠は、20種類あるランダム効果のいずれかを引き起こします。半数弱の確率で危険な効果が発生します：閃光が放たれて一時的に盲目にされ、数体の敵対的モンスターが周囲に召喚されます。また、火炎に包まれる目もあります。それ以外の結果は無害か、むしろ有益です：単なる演出メッセージもあれば、透明状態のオン／オフを切り替えるもの、装備中の呪われたアイテムを解呪するもの、そして周囲のモンスターをペット化して魅了（カリスマ）を1上昇させるものもあります。この最後の効果を狙って、既知の魔法の罠を何度も踏んで魅了値と店の割引率を稼ぐプレイヤーもいますが、発生確率は約1/20に過ぎず、火災やモンスター召喚のリスクを考えると待機は危険を伴います。

熊の罠にかかると数ターンの間足止めされます。脱出を試みる際は、そのマスから **斜め方向** へ踏み出すようにしてください。直交方向よりも斜め移動の方が約5倍早く抜け出せます。開錠の杖やノック（解錠）の呪文を使えば、その場で瞬時に罠が外れます。

魔法防御はテレポートの罠を遮断します。もし罠を利用してテレポートしたい場合は、発見済みの罠の上に立った状態で `Ctrl+T` を押してください（他のマスから押しても何も起きません）。

**反魔法フィールドは、魔法防御を持っている冒険者にこそ手痛い打撃を与えます。** この罠は魔力（スペルエネルギー）を枯渇させるだけでなく、*魔法防御* を所持していると「反魔法の爆縮」を引き起こしてHPにダメージを与えてきます。ダメージは基本1d4に加え、物理半減または魔法半減の能力で+1d4、[マジックベイン (Magicbane)](#magicbane) を装備していると+1d4、そして魔法耐性アーティファクトを所持しているとさらに+1d4が加算されます（1つだけが対象となり、最初の合致で判定を終了します）。最悪の場合、4d4のダメージを受けますが、壁抜け能力があればダメージは1/4（切り上げ）に抑えられます。最大の防御策は、捜索によって事前に罠を発見し、迂回して通り過ぎることです。無力化の杖を魔法の罠に向かって振ると罠を消滅させることができますが、その際に罠のマスで20 + 3d6の大爆発を引き起こすため、静かな解除法とは言えません。

鉄製の履物（鉄の靴、または蹴り挙げ靴）は、5.0において驚くほど多くの罠ダメージを肩代わりしてくれます：熊の罠による脚のダメージを無効化し、トゲの落とし穴の杭を防ぎ、変身の罠による肉体の変異を遮断し（代わりに履いていた靴が変身します）、プラスに強化されていれば強化値を1失うことで反魔法フィールドの魔力ドレインを身代わりに吸収してくれます。まだ他に優れた靴を見つけていない段階では、身につけておく価値の非常に高い防護装備です。
