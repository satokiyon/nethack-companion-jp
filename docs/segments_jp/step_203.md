#### 城 (The Castle) {#the-castle}

<!-- audit
2026-05-18:
- no minotaur or internal maze in castle.lua; minotaurs live in earth/fire/hellfill
- wand chest is locked at creation (castle.lua:144); monsters cannot unlock chests (muse.c:2273 mloot_container bails on olocked)
- Elbereth + cursed scroll target food-eaters, not shopkeepers (castle.lua:150 author comment)
- throne room is filled with random court monsters (L/N/E/H/M/O/R/T/X/Z), not soldiers (castle.lua:54, 195-221)
- soldiers and lieutenant guard the entry hall and tower corners
- five trap doors at columns 40/44/48/52/55 (gaps 4/4/4/3), not strictly even (castle.lua:156-160)
- trap door always sends you to Valley of the Dead (dlevel=1), not a random Gehennom level (trap.c:669-670, dungeon.c:1949-1953)
- storerooms hold four D-class dragons; moat holds sea monsters; fountain present (castle.lua:60, 180, 185)
- drawbridge passtune is 5 notes A-G, Mastermind-style miss feedback (music.c:793, 836-884)
- any instrument can attempt the passtune; flutes/horns/bugle require can_blow, harp and drums don't (music.c:769-771)
- wand of striking DESTROYS the drawbridge; wand of locking/spell of wizard lock closes it (zap.c:3290-3305)
- wand of opening or spell of knock opens the drawbridge (zap.c:3263-3273, 2184)
- strategy aligned with NetHackWiki Castle, Passtune, Drawbridge, Wand of wishing: passtune-as-Mastermind, wand-of-opening/spell-of-knock alternatives, wand of striking destroys, bring conflict for crowd control, plan a small wishlist, secure MR/reflection/fire-res/poison-res before descending (https://nethackwiki.com/wiki/Castle, https://nethackwiki.com/wiki/Passtune, https://nethackwiki.com/wiki/Drawbridge, https://nethackwiki.com/wiki/Wand_of_wishing)
2026-05-31 audit:
- Castle has NO conventional down-stair to Gehennom. The Gehennom branch is flagged `branchtype = "no_down"` in dungeon.lua, so the branch connection point gets no automatic `>` stair. The five trap doors in the central hallway at columns 40/44/48/52/55 (castle.lua:156-160) are the only way to descend into Gehennom.
- The Castle level is one of only two levels that opt out of random mirroring via `noflipx`/`noflipy` in its .lua definition; the other is bigrm-12.lua (Big Room variant 12). All other special levels — Sokoban, Oracle, Mines branch, Quest levels, Medusa, Valley of the Dead, the four Elemental Planes, demon lord lairs, Vlad's Tower, Orcus Town, Wizard's Tower, Moloch's Sanctum, Astral Plane — can flip on either axis via sp_lev.c:967 flip_level_rnd with allow_flips default 3.
- ★ glyph on the dungeon map figure (Quest goal, Vlad the Impaler, Wizard of Yendor) is rendered upright on otherwise-italic detail lines via a tspan font-style:normal override in dungeon_map.py.
-->

城（The Castle）は運命の迷宮（Dungeons of Doom）の終点であり、ゲヘナ（Gehennom）へと続く唯一のルートを守護しています。ここを一大補給基地として攻略してください：ここに配置された願いの杖と宝物庫は、貧弱な装備構成を立て直す最後の確実なチャンスです。

最初の難関は跳ね橋です。これを下ろす手段は4つあります：

- **合言葉のメロディを演奏する。** 音程のある楽器（木製のフルート、魔法のフルート、角笛、冷気や炎の角笛、ラッパ、竪琴）で5音のメロディを奏でると跳ね橋が開きます。メロディはゲームごとにランダムです。様々な音階を試すことで特定できます：ゲームはマスターマインドのように、試行ごとに何音が合っていたかを教えてくれます。メロディを機能させるには、跳ね橋が周囲8マスのいずれかにある必要があります。跳ね橋の真上や城門のマスに立って演奏してはいけません。橋が動いた瞬間に押し潰されて即死します。音階は A〜G（ラ〜ソ）です（ドイツ音名表記の "H" も受け付けられ、シ / B を意味します）。
- **開扉の杖** を跳ね橋に向けて振る。
- **開錠の呪文 (Knock)** を跳ね橋に向けて唱える。
- **衝撃の杖** で跳ね橋を完全に **破壊する**。橋桁が崩落して堀の水に戻ります。破壊後はメロディも効かなくなるため、堀を渡る別の手段を用意してください。

橋を渡ると、城の内部には以下の施設が広がっています：

- **玉座の間:** 玉座と、高レベルモンスターの宮廷（リッチ、ニンフ、目玉、巨人など）が待ち構えています。玉座に座るのは魅力的ですが危険も伴います。玉座の間にはランダムな戦利品が入った **宝箱** も置かれています（これは願いの杖の箱ではなく、副賞に過ぎません）。
- **兵舎:** 優秀な装備品を持った兵士たちで溢れています。彼らを片付ければ、それらの装備はすべてあなたのものになります。
- **4つの四隅の小塔:** そのうちの1つ（ランダムで1箇所のみ）の施錠された宝箱の中に、**願いの杖** が収められています。*すべての小塔を捜索する* か、中庭から物体探知の薬を飲んでどの塔に宝箱があるかを特定し、他の3つを無視してください。この宝箱には **レベルアップの薬** も一緒に入っています。宝箱のマスは床に刻まれた *[エルベレス (Elbereth)](#elbereth)* の文字で守られ、さらに呪われた怪物を怯えさせる巻物で封印されています。これらの結界は、ゼラチナス・キューブのような食料を貪る怪物が宝箱に近づくのを防ぐためのものです。呪われた巻物は罠でもあるため、気軽に読もうとしてはいけません。施錠された宝箱は、力任せの破壊、鍵、または開扉の杖で開けられます。
- **4つの貯蔵庫:** 北壁と南壁に沿って配置され、それぞれドラゴン（`D` クラス）が守護しています。隅の小塔と混同しないでください。防具、武器、宝石、食料が部屋ごとに分類されて収められています。
- **5つの落とし蓋が並ぶ中央廊下:** 踏むと死の谷へと真っ逆さまに落下します。この段階ではまだ望まない事態です。足元を注意深く確認してください。なお、この落とし蓋は城から下層へと降りる **唯一の手段** でもあります。この階層にはゲヘナへと続く通常の降下階段（`>`）が存在しないため、ゲヘナへ突入する準備が整ったら、意図的にこの落とし蓋の1つを踏んで落下します。
- **流し台と泉:** 堀沿いの通路にあり、緊急時には使えますが、願いの杖を危険に晒してまで試す価値はありません。
- **堀:** 要塞を取り囲んでおり、巨大ウナギや時折サメが潜んでいます。

攻略戦術：城は慎重に制圧してください。争いの指輪（Ring of conflict）を身につければ、兵士や警備兵同士が勝手に殺し合ってくれます：足を踏み入れ、指輪をはめ、兵士たち自身にモンスター問題を解決させましょう。すべてを略奪し尽くしたら、願いの杖を使って装備の致命的な欠落を埋めてください（灰色ドラゴンの鱗鎧、銀色ドラゴンの鱗鎧、力の小手、韋駄天の靴など、足りないものすべて）。

施錠された城の願いの杖の宝箱は、**一時的に放置しても安全** です：NetHack 5.0 のモンスターは *開いている* 容器を拾い上げて中身を漁ることができ、鍵を使って扉を開けることもできますが、宝箱を解錠することはできません。生成時から施錠されている宝箱は、あなたや開扉の杖が介入しない限り施錠されたまま保たれます。

城の杖単体から得られる願いは実質2回（初期チャージ＋限界振りの1回）であるため、*コンパクトな* ウィッシュリストを計画し、それ以上の願いは他の入手源（ヴラドの玉座、魔除け拾得時、オーケスの町のランプ、泉の幸運）から得るものと割り切ってください。

完全装備を整えたら、ゲヘナへ飛び降りる前に一息つきましょう。座って、軽食を取り、所持品を二重三重に点検してください。あなたの鞄には、**[魔法耐性](#damage-resistances)**、**反射**、**火炎耐性**、**[毒耐性](#damage-resistances)**、**穴掘りの杖**、**ユニコーンの角**、潤沢な食料、聖水、テレポートと識別の巻物、そして **クエストアーティファクト** が揃っていなければなりません。
