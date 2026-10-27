#### エルベレス (Elbereth) {#elbereth}
<!-- audit
2026-05-19:
- while levitating, finger and weapon engraving refused (engrave.c:1003-1006)
- but wand engraving falls through after "gesture toward floor"; ptext=TRUE wands (fire, lightning, cold, digging) still complete the engraving (engrave.c:1007-1011, 1099-1104, 1186-1189)
- v2 "no actual writing happens" claim was wrong for BURN wands — corrected
2026-05-18:
- hypocrite alignment hit: adjalign((u.ualign.record > 5) ? -5 : -rnd(5)) — flat −5 only with healthy alignment, else rnd(5) avg −3 (mon.c:4280)
- defile rule: del_engr_at fires unconditionally — burned Elbereth wiped too (mon.c:4267-4285)
- strict-match Elbereth: full engr_txt must equal "Elbereth" (engrave.c:256)
- Elbereth dead in Gehennom and the endgame planes (monmove.c:302, In_hell || In_endgame)
- onscary lives at monmove.c:241 (not teleport.c as old comment claimed)
- ignored by S_HUMAN + unique_corpstat (quest nemeses, named monsters) (monmove.c:259-261)
- ignored by Riders, Angels, lawful minions, Wizard of Yendor (monmove.c:251-253)
- ignored by minotaur (monmove.c:301)
- blind and peaceful monsters pass through (monmove.c:299-300)
- cornered ALLOW_SSM step-through (mon.c:2278-2282)
- strategy aligned with NetHackWiki Elbereth, Engraving: exact-spelling rule, defile-and-hypocrite penalty, ward dead in Gehennom/endgame, burn-with-wand-of-fire for permanence (https://nethackwiki.com/wiki/Elbereth, https://nethackwiki.com/wiki/Engraving)
2026-05-23:
- defile rule fires for any attack with via_attack=TRUE: melee (uhitm.c:1293,1302,1403,6398), thrown weapons via dothrow.c:1965,2230,2282 → wakeup(mon, TRUE) → setmangry(mtmp, TRUE) (mon.c:4350-4355), and wand zaps via zap.c:4948,5495
- "kill at range from Elbereth" is therefore a 4.x-era piece of advice; in 5.0 it defiles too
- Rogue "Elbereth in the doorway, daggers from beyond" cannot work in 5.0: throwing from Elbereth defiles it; standing off Elbereth means Elbereth doesn't protect anything (monmove.c:295-302 requires u_at(x,y))
-->

##### 単語の由来 (Where the word comes from) {#where-the-word-comes-from}

*Elbereth*（エルベレス）はシンダール語で「星々の女王」を意味し、J.R.R.トールキンの『シルマリルの物語』に登場する最高位のヴァラであり天上に星々を撒き散らした **ヴァルダ・エレンターリ (Varda Elentári)** のエルフ名です。『指輪物語』において、エルフたちは邪悪に対する聖なる守護を求めて彼女の御名を呼び唱えます。フロドは風見荘で「オ・エルベレス！ ギルソニエル！」と叫んで魔王を後退させ、サムはシェロブの暗黒の巣窟でガラドリエルの玻璃瓶の光を輝かせるために彼女の名に祈りを捧げました。NetHackはこの設定をそのままゲームに採用しています：ダンジョンの床にヴァルダの名を刻みつけることは、絶対安全な聖域を求めて上位の超越者へと救いを求める行為なのです。

> *以下の仕組みは、Kate Nepveu氏の「Elbereth FAQ」に着想を得ています。Kate氏は、数十年におよぶコミュニティのスポイラーを保存し続けてきた長期アーカイブ「steelypips.org」の管理者でもありました。*

##### 聖なる結界 (The ward) {#the-ward}

床に **Elbereth** の文字を刻むことで、強力な防護結界が生成されます。エルベレスが刻まれたマスの上にプレイヤーが立っている限り、大半のモンスターは近接攻撃を仕掛けてくることができず、苛立ちながら周囲をうろうろと彷徨うだけになります。この結界は、自分で書いたものであっても、最初から床に書かれていたものであっても同様に機能します。また、書いた手法（埃、削り傷、焼き付け）は結界の防護力自体には一切影響せず、文字がどれだけ長く残り続けるか（耐久度）の違いに過ぎません。

##### 結界の絶対ルール (Rules of the ward) {#rules-of-the-ward}

- **マスの上に立っている間だけ効果がある。** マスから一歩でも足を踏み出せば防護は途切れます。再びそのマスの上に戻れば結界の効果が復活します。
- **厳密に完全な単語でなければならない。** "Elbereth" の8文字きっかりでなければならず、文字の不足や余計な文字は一切許されません。状態異常による誤字や、他の文字列が追記されたものは無効となります。
- **一部のモンスターは結界を完全に無視する。** `@` で表されるすべての存在（人間、エルフ、プレイヤー系キャラクター）、霊界の死の騎士（Riders）、天使、ミノタウロス、固有の固有名を持つモンスター（クエストの宿敵、ヴラド、魔法使い）、店主、番兵、および **盲目のモンスター** は、結界を意に介さず平然と踏み越えて攻撃してきます。また、逃げ道のない袋小路に追い詰められたモンスターも同様です：逃げ場を失った怪物は、無抵抗で立ち尽くすくらいなら死に物狂いで反撃してきます。
- **ゲヘナ、属性の諸平面、霊界では機能しない。** [城 (The Castle)](#the-castle) より下の階層では、エルベレスの神聖な力は届かず、すべて自分の実力だけで切り抜ける必要があります。

##### エルベレスの御名を汚すこと（極めて重要）(Defiling the name of Elbereth (important)) {#defiling-the-name-of-elbereth-important}

もしエルベレスの上に立った状態でモンスターに対して何らかの攻撃を行った場合（近接攻撃、投擲武器、あるいは杖の発射を問わず）、その対象が結界を恐れるはずのモンスターであったり友好的な生物であったなら、刻み文字は **どのように書かれたものであっても即座に完全消滅します。** 火の杖で床に恒久的に焼き付けたエルベレスであっても、たった一振りの攻撃で跡形もなく消え去ります。同時にプレイヤーは「偽善者になった気分だ。」というメッセージとともに **属性値に手痛いペナルティを受け**、「足元の刻印が薄れていく。」と表示されます。属性値の実績が十分に高ければ一律で−5、そうでなければランダムに−1〜−5の低下を被ります。

耐久度の表にこの例外は書かれていません。「恒久」や「半恒久」とは、あくまで足踏みや風化といった *受動的な摩耗* に対する耐性のことです。プレイヤー自身の敵対行動は、どんな耐久度の文字であっても一瞬で消滅させます。したがって、エルベレスは **完全に防御専用の結界** として使う必要があります。体力を回復する、薬を飲む、巻物を読む、装備を整え直す、体勢を立て直すといった時間稼ぎに活用してください。結界の上からの攻撃は禁忌であるため、反撃に転じる際は必ずマスから一歩踏み出してから戦いましょう。

##### 実践的な活用法 (Practical use) {#practical-use}

緊急事態に陥ったら、まずは指を使って埃の中に素手で Elbereth と書きましょう。アイテムを消費せずに行えますが、1回の手番（アクション）を消費するため、モンスターに接触される前に書く必要があります。大半のモンスターは怯えて距離を取り、落ち着いて次の行動を選ぶ猶予が生まれます。目先の危機を脱したら、埃の結界を次回のために温存する（モンスターがそのマスを踏まない限り文字は残ります）か、より耐久性の高い手段で書き直しましょう。

アイテムの保管場所、安全な休息用の中継地点、あるいは通路での迎撃拠点として恒久的な安全地帯を作りたい場合は、火の杖や雷の杖を使って床に文字を焼き付けましょう。1ターンで完了し、敵に中断されるリスクがなく、通常の足踏みで消えることもありません。ただし、盲目、混乱、気絶、幻覚の状態にあると綴りを書き損じる恐れがあります。半恒久的な彫刻（アサメ、通常の武器、宝石、採掘の杖）は中間の選択肢です：耐久性はありますが、時間のかかる手作業の方法は文字の途中で中断される危険があります。

浮遊している間は、指や武器を使って床に文字を書くことはできません。しかし、火、雷、冷気、採掘の杖であれば、空中からでも下を向いて床に刻むことができます。「足元の床に向かって身振りをした」というメッセージが出ますが、焼き付けは正常に完了します。

**祭壇や墓の上には絶対に文字を刻んではいけません。** 祭壇の上で何かを書こうとすると（エルベレスであっても）、**文字は一切刻まれず**、神を冒涜して激怒させます：自分の祭壇なら賢明と属性値を失い、他の祭壇なら幸運を失います。祭壇の上でモンスターに追い詰められたからといって、反射的にエルベレスを床に殴り書きしてはいけません。必ず一歩降りてから書きましょう。また、荒らされていない墓の上で武器や杖を使って文字を彫ると墓荒らしとなり、グールが召喚されます（素手の指なら墓石の表面を汚すだけで済みます）。なお、泉のあるマスには最初から文字を刻むことはできません。

床に置かれた **怪物を怯えさせる巻物 (scroll of scare monster)** は、エルベレスのさらに強力な上位互換として機能します。その巻物の上に立つだけで大半のモンスターは間合いを取って接近できなくなりますが、エルベレスに対して以下の3つの決定的な優位性を持っています：エルベレスが無効化されるゲヘナや霊界でも問題なく機能すること、エルベレスを平然と通過してくるミノタウロスや盲目の敵をも退けること、そして刻み文字ではないため **巻物の上に立ったまま自由に攻撃を仕掛けても消滅せず、偽善者の属性ペナルティも一切受けないこと** です。巻物は自然摩耗せず、自分がマスから離れてもそのマスは敵の進入禁止エリアとして残り続けます。唯一の弱点は「拾い上げ」にあります：床から拾おうとすると高確率で崩壊して消滅します（呪われた巻物は1回目、呪われていない巻物は2回目で灰になります）。そのため、安全地帯として固定したい場所に置いて使用してください。城の「願いの杖」が入った宝箱の真下に呪われた怪物を怯えさせる巻物が敷かれているのは、まさにこの防衛機能のためです。また、店の中でも識別テクニックとして利用できます：未識別の巻物の上に乗り、連れているペットが嫌がって後ずさりしたら、それは怪物を怯えさせる巻物であり、拾い上げるリスクなしに安全に識別できます。
