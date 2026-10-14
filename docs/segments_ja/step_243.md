#### 食料コンダクト (The Food Conducts)

<!-- audit
2026-05-19:
- vegetarian-safe puddings: gray ooze, brown pudding, green slime; not black pudding (mondata.h:241)
- no yellow pudding exists (monsters.h:2081-2113)
- puddings are G_NOCORPSE and leave globs, not corpses
- shriekers are S_FUNGUS, already covered by "all F (fungi and molds)"
- vegan-violating VEGGY foods: eggs, pancakes, royal jelly, cream pies, candy bars, fortune cookies (eat.c:3016-3018)
- fortune cookies contain eggs, so they break vegan
- ghosts are G_NOCORPSE; ghost corpses don't exist (monsters.h:2888,2897)
- watch out for: yellow mold, violet fungus, acid blob — vegetarian-by-macro but unsafe to eat (yellow mold M1_POIS monsters.h:1638; violet fungus AT_TUCH AD_STCK monsters.h:1670; acid blob AD_ACID monsters.h:139; eat.c:1303-1308 violet fungus corpse hallucinates)
- polymorph does NOT break foodless: polyself.c has no u.uconduct.food increment (polyself.c:750-751 only increments u.uconduct.polyselfs)
- prayer cures hunger at Hungry/Weak/Fainting (pray.c:275, uhs >= HUNGRY)
- wishing for slow digestion is a viable foodless route
- Monk: vegetarian is nearly free
- strategy aligned with NetHackWiki Conduct, Foodless, Veggy: vegetarian/vegan/foodless hierarchy and the slow-digestion / prayer / stone-to-flesh strategy for foodless are canonical (https://nethackwiki.com/wiki/Conduct, https://nethackwiki.com/wiki/Foodless, https://nethackwiki.com/wiki/Veggy)
-->

食料コンダクトには厳格な階層構造があります：絶食はヴィーガンより厳しく、ヴィーガンはベジタリアンより厳格です。

**菜食主義者 (Vegetarian)。** 肉を口にしてはいけません。具体的には、肉食性・動物性モンスターの死体を避け、動物由来の食品（ジャーキー、肉食生物の卵など）を食べないことです。実践上は、許容された植物性・無生物性の死体や粘塊（glob）を食べて生活します。地衣類、ゼリー、菌類・カビ類、灰色ウーズや茶色プリンの粘塊はすべて安全です。フォーチュンクッキー、レンバス、床に落ちている野菜類も食べられます。緑色スライムは定義上は菜食対象ですが、食べるとスライム化して即座に死亡します。菜食対象モンスターは多岐にわたります：すべての `b`（ブロッブ）、すべての `j`（ゼリー）、すべての `F`（菌類とカビ）、すべての `v`（ボルテックス）、すべての `y`（光）、ストーカーを除くすべての `E`（エレメンタル）、肉と革を除くすべての `'`（ゴーレム）です。多くの菜食死体が有用な耐性を授けてくれます。ただし「菜食規定上セーフ」と「毒性的に安全」は別物です。黄色モールドは毒を持ち、紫色キノコは幻覚を引き起こし、酸ブロブは喉を焼きます。武闘家（修道士）は元々肉を食べると属性ペナルティを受けるため、ベジタリアンに最も適した職業です。

**完全菜食主義者 (Vegan)。** ベジタリアンの全制限に加え、卵、パンケーキ、ローヤルゼリー、クリームパイ、キャンディバー、そして **フォーチュンクッキー** を口にしてはいけません（フォーチュンクッキーには生地に卵が含まれているため、ベジタリアンでは許容されてもヴィーガンでは失格となります）。このコンダクトは「食べる」ことのみに適用されるため、動物由来のアイテムを携行・使用することは許されます（蝋燭に火を灯す、革防具を着る、角笛を吹くなどはセーフです）。またヴィーガンではプリンの粘塊も除外されます。

**絶食 (Foodless)。** あらゆる食物を一切口にしてはいけません。現実的な解決策は、祈り（「空腹」ステータス以降ならいつでも空腹を満たしてくれる）と、消化不良の指輪（通常の空腹進行を完全に停止させる）の2つです。岩を肉に変える魔法でミートボールを作れますが、それを食べるとコンダクト違反になります。大半の絶食ランは、序盤に消化不良の指輪を拾うか、出るまで祈りで空腹を凌ぐ戦略を取ります。願いの杖や魔法のランプが出現した際、消化不良の指輪を願うのが定石です。なお、壁を掘り進む際に岩を咀嚼して食べる行為も絶食違反となります。

