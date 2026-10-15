#### 変身の制限 (Polymorph Restrictions)

<!-- audit
2026-05-19:
- no SCR_POLYMORPH exists in 5.0; "cursed scroll of polymorph" is not a thing (objects.h:1187-1265 scroll list has no polymorph entry; no SCR_POLYMORPH token anywhere in source)
- breaks: genetic engineer claw (AD_POLY -> polyself)
- breaks: eating chameleon, doppelganger, or mimic corpses (eat.c:1244-1263, eat.c:1199)
- breaks: green slime auto-poly (timeout.c:493)
- breaks: stone-golem auto-poly via poly_when_stoned (trap.c:3848)
- Unchanging blocks all polymorph; system shock does NOT break the conduct (polyself.c:483-495)
- sandestins are G_NOCORPSE; their corpses are unreachable (eat.c:1246)
- poly_when_stoned only fires if already polymorphed into a non-stone golem; normal characters die (mondata.c:80-86)
- strategy aligned with NetHackWiki Polymorph, Amulet of unchanging, Polypiling: Unchanging blocks every involuntary path, polypileless forfeits the polypile item-generation trick (https://nethackwiki.com/wiki/Polymorph, https://nethackwiki.com/wiki/Amulet_of_unchanging, https://nethackwiki.com/wiki/Polypiling)
-->

変身（ポリモーフ）に関する2つの独立したコンダクトがあります：

**自己変身(へんげ)なし (Polyselfless)。** 自分自身の姿をいかなる形態にも変身させてはいけません。分かりやすい発生源：へんげの薬や指輪、へんげの杖や呪文の被弾、変身(へんげ)の罠。分かりにくい発生源：遺伝子工学者の爪攻撃、カメレオンやドッペルゲンガーやミミックの死体の摂食、そしてスライム化の未治療（緑色スライムに変身して死亡）。耐へんげの魔除け（Amulet of unchanging）を身につけていれば、これらすべての意図しない変身を遮断できます。なお、変身失敗によるショック死（システムショック）はコンダクト違反にはなりません。このコンダクトを守ることは、マスターマインドフレア、ゾーン、各種ドラゴンといった強力なモンスター形態の恩恵をすべて放棄することを意味します。

**アイテム変身(へんげ)なし (Polypileless)。** アイテムを変身させてはいけません。へんげの杖をアイテム山に振ったり、へんげの薬にアイテムを浸したり、その他の手段でアイテムを別のアイテムへと変換する行為を禁じます。これにより、ダンジョン最強のアイテム錬成技である「ポリパイル」が封印されます。

