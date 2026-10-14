#### 倉庫番 (Sokoban)

最上階で手に入るご褒美は、通常は **軽量化の鞄 (bag of holding)**、さもなくば **反射の魔除け (amulet of reflection)** です。どちらも鉱山の戦いが本格的に厳しくなる前に、装備に関する重大な課題を解決してくれます。

倉庫番への入り口となる階段は、ダンジョンの地下6階から10階のどこか（[賢者 (Oracle)](#the-oracle) のフロアの1階層下）に現れ、上り階段となっています。倉庫番は全4階層からなるパズルフロアで構成されており、巨石（ボルダー）を押して落とし穴を埋めたり所定の位置に収めたりして道を開いていきます。ここではテレポートは機能せず、入り口のフロアから下に向かって地面を掘り進むこともできません（床が補強されているためです）。

各階層のパズルは固定されています（各フロアにつき2種類のバリエーションがあり、ランダムにどちらかが選ばれます）。
<!-- audit
2026-05-19:
- in Sokoban, pit traps suck you in regardless of flying/levitation (trap.c:1850 gates on !Sokoban; trap.c:3014-3023 "Air currents pull you down")
- Sokoban walls are W_NONDIGGABLE on every soko level (non_diggable in each soko*.lua); dig_check fails (dig.c:228-230)
2026-05-18:
- entrance DL 6-10: Oracle base 5 range 5 + Sokoban one level up (dungeon.lua:21-24, 60-66)
- 4 levels × 2 fixed variants (dat/soko*.lua)
- noteleport on every Sokoban level (soko1-1.lua:7 and matching line in each soko*.lua)
- hardfloor only on the entrance; blocks dig-down off entrance (soko4-1.lua:38, soko4-2.lua:7)
- sokoban_guilt = change_luck(-1) + u.uconduct.sokocheat++ (trap.c:7039-7054)
- guilt triggers: squeeze past boulder (hack.c:299, 307, 398, 403)
- guilt triggers: dismount onto boulder (steed.c:767)
- guilt triggers: polymorph boulder (zap.c:1710-1711), fracture by striking (zap.c:5555-5556)
- guilt triggers: scroll of earth (read.c:1951)
- bare-hand force-fight on boulder is harmless (hack.c:2287, 2318-2321)
- pick-axe/mattock force-fight digs the boulder (hack.c:2269-2275)
- levitation also blocks pushing boulders: "not enough leverage" (hack.c:415-425)
- prize: 75/25 weighted bag of holding vs amulet of reflection (soko1-1.lua:103-107, soko1-2.lua:105-109)
- cursed scroll of scare monster placed under the prize as bait (soko1-1.lua:111, soko1-2.lua:113)
- conduct only reported once the branch is entered (insight.c:2215-2228)
- strategy aligned with NetHackWiki Sokoban, Amulet of reflection: prize/cheat-luck-penalty mechanics and the "solve honestly for the prize" advice match (https://nethackwiki.com/wiki/Sokoban, https://nethackwiki.com/wiki/Amulet_of_reflection)
- pushing a boulder exercises Strength via exercise(A_STR, TRUE) (hack.c boulder push handler); Stressed encumbrance exercises Str too but applies HP cost via near_capacity checks (attrib.c, eat.c:3197+)
-->

各階層には厳密に1つだけの正しい解答手順が存在します。もし巨石を角に押し込んで進行不能にしてしまった場合、やり直す（リセットする）手段はありません。その場合、役立つかどうかは別として、不正（チート）を行う選択肢がいくつか残されています：巨石の横を **すり抜ける**（荷物を床に置いて体を細くする）、つるはし（pick-axe / mattock）を装備して **巨石を掘り崩す**、あるいは「衝撃 (force bolt)」の呪文や強打の杖で **巨石を粉砕する**（大地の巻物や変身の杖なども同様に判定されます）。これらの不正を行うと、1回につき幸運値が1低下し、倉庫番のオピニオン（不心得行為の記録）が残ります。なお、倉庫番の全フロアにおいて壁は掘削不能（non-diggable）であり、落とし穴を迂回することはできません。飛行や浮遊の状態であっても、下降気流に引きずり込まれるため開いた穴の上を飛び越えることは不可能です。穴に落ちた後は自力で這い上がることができます。

最上階のご褒美は **軽量化の鞄** または **反射の魔除け** のいずれかで、どちらも極めて貴重なアイテムです。各バリエーションにおける75/25の出現比率は巻末の [倉庫番の解法 (Sokoban Solutions)](#sokoban-solutions) に記載されています。なお、ご褒美の真下には罠のエサとして呪われた「怪物を怯えさせる巻物」が敷かれています。軽量化の鞄は、中に入れたアイテムの重量を軽減して持ち運べる荷物の上限を大幅に増やしてくれます。反射の魔除けは、浴びせられた光線攻撃を相手にそのまま反射して跳ね返します。

不正を働いてペナルティを受けた後であっても、ご褒美自体は問題なく受け取ることができます。失われた幸運は階層をクリアしても自動的には回復しません。未祝福の幸せの石を所持していない限り、600ターンごとに1ポイントずつゼロに向かって自然回復していきます。

**巨石の向こうのモンスター。** 巨石の背後に閉じ込められたモンスターはあなたに接近できませんが、こちらから攻撃することは可能です：**投げた短剣やダーツは巨石の頭上をまっすぐ飛び越えて命中します**。また、大半の攻撃呪文（マジックミサイル、冷気の円錐など）も巨石の上を通過します。ただし、巨石を邪魔だからといって **「衝撃」の呪文や強打の杖で排除してはいけません**。巨石が粉砕されて幸運を失うだけでなく、パズルの解答に必要な石を失ってしまいます。

正攻法で巨石を1マス押すごとに、筋力が鍛えられます（筋力エクササイズ）。圧迫（Stressed）の状態で無理に歩き回るリスクを冒さずとも、このパズルを解くだけで十分な筋力トレーニングができます。

全8種類のフロアバリエーションの完全な解法手順については、巻末付録の [倉庫番の解法 (Sokoban Solutions)](#sokoban-solutions) を参照してください。

<!-- audit
2026-05-18:
- Oracle DL 5-9 (dungeon.lua:60-66, dungeon.c:405-411)
- 4 fountains in the delphi sub-room (oracle.lua:19-22)
- 8 centaur statues flank the Oracle (oracle.lua:9-16)
- minor consultation costs 50 zm (rumors.c:699)
- major consultation costs 500 + 50 × u.ulevel (rumors.c:699)
- minor consults ALWAYS pull from the true-rumor pool (rumors.c:747, 151-156)
- Sokoban branch goes up from the Oracle level (dungeon.lua:20-25)
- Oracle is M2_PEACEFUL with AT_NONE; she never attacks (monsters.h:2738-2745)
- strategy aligned with NetHackWiki Oracle (level), List of major consultations: paying for a major consultation is a recognized wisdom-and-intel investment (https://nethackwiki.com/wiki/Oracle_(level), https://nethackwiki.com/wiki/List_of_major_consultations)
-->
