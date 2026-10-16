#### ペットなし (Petless: 5.0新要素) {#petless-new-in-5.0}

<!-- audit
2026-05-19:
- pettype:none bypasses pet_type (dog.c:225-229)
- tamedog increments u.uconduct.pets across all taming paths
- the endgame angel preserves petless (minion.c:533-539)
- xlogfile achievement "petless" via add_achieveX (topten.c)
- "dairy to foocubi" is fabricated: befriend_with_obj gates on is_domestic, and foocubi aren't (mondata.h:255-261)
- foocubus + ring of adornment is pacification, not taming (mhitu.c doseduce only reads mon->mtame at 2263 and mon->mpeaceful at 2279; never sets mtame nor calls tamedog)
- food thrown at hostile dogs and cats IS a taming path that breaks petless (dothrow.c:2268-2269 routes to tamedog)
-->

いかなるペットも従えてはいけません。設定ファイルに `OPTIONS=pettype:none` を記述して初期の相棒を完全にスキップします（各職業の初期設定を上書きします）。その後、いかなるモンスターであっても手懐けられた（tame になった）瞬間に、このコンダクトは失格となります。ゲームがそれを止めることはありません。怪物を飼いならす巻物、魅了呪文、敵対的な犬や猫に肉を投げ与える行為、魔法の罠の暴発など、いずれもその場で「ペットなし」を破棄します。
