# NetHack スポイラー

```{=html}
<p style="text-align: center; font-size: 1.25em; margin: 0.2em 0 1.4em;">脅威の迷宮への旅人の手引き (A Traveler's Companion to the <span class="nobr">Mazes of Menace</span>)</p>
```

```{=html}
<p style="text-align: center; font-style: italic; margin: 1.5em 0;">誰かがあなたを助けてくれているような気がする。(You feel like someone is helping you.)</p>
```

NetHack は、現在も活発に開発・保守が続けられている最古のコンピュータゲームの一つであり、そのコードは40年以上にわたって継続的に開発されています。そのルーツは、Michael Toy と Glenn Wichman が『ダンジョンズ＆ドラゴンズ』に着想を得て1980年に開発したゲーム『Rogue』にまで遡ります。『Rogue』では、ダンジョンはランダムに生成され、通常のテキスト文字で描かれていました。プレイヤーの主人公は `@`、モンスターはアルファベットの文字で表され、死は絶対（パーマデス）でした。Ken Arnold が開発した curses ライブラリ上に構築され、バークレーの BSD Unix に同梱されて世界中に広まった『Rogue』は、当時の大学キャンパスで最も人気のあるゲームとなり、「ローグライク (roguelike)」と呼ばれる一連の同系ゲームジャンルを生み出すきっかけとなりました。

NetHack の歴史が始まったのは、マサチューセッツ州リンカーン・サドベリー地域高校の3年生だった Jay Fenlason が、自分専用のカスタム版『Rogue』を作りたいと考えたことでした。『Rogue』のソースコードは不正行為を防ぐために厳重に保護されていたため、彼はゼロから開発を始めなければなりませんでした。彼の学校では生徒たち自身の手によって維持されていた Unix ミニコンピュータが稼働しており、そこで彼はクラスメイトの Kenny Woodland、Mike Thome、Jon Payne とともに『Hack』を作り上げました。これは固有の名前を持つモンスターが登場し、杖から光線が放たれ、プレイヤーが通り過ぎた各階層の状態が記憶されるゲームでした。彼の恩師である Brian Harvey が1982年にこれを USENIX テープに収録して配布した際、Jay は README に「僕の最初の学期プログラミング課題」と記し、自宅の電話番号を書き添えていました。

『Hack』の歩みはそこで終わっていたかもしれませんが、オープンソースであったため、プログラマからプログラマへと自由に受け継がれていきました。1984年、オランダの数学者 Andries Brouwer がこれを大幅に書き直し、誰でも自由に利用できるように『Hack 1.0』として Usenet に投稿しました。彼はプレイヤーの役職（ロール）、階段を降りる際についてくるペット、そして店主を追加しました。こうして初期のインターネット全体に、どの作者も把握しきれないほどの速度で複製や派生版が広がっていきました。

1987年、Mike Stephenson はそれら散在していたバージョンを再び集め、Izchak Miller、Janet Walz、そして広がりつつあったボランティアの仲間たちとともに、ひとつのゲームへと統合しました。彼らはその共同作業を可能にしたネットワークにちなんでゲームを「NetHack」と名付け、自らを「DevTeam」と称しました。彼らは今もなお活動を続けています。**2026年5月、バージョン5.0がリリースされました。** 40年以上の歳月をかけて、DevTeam は NetHack を最も容赦なく入り組んだ、ローグライクを象徴する金字塔へと育て上げ、ゲームそのものの枠を超えた活気ある楽しいコミュニティ文化を育んできました。その文化の多くは、1990年代の rec.games.roguelike.nethack ニュースグループで形作られ、今日では NetHack Wiki、r/nethack フォーラム、Discord や IRC チャンネル、そして nethack.alt.org や hardfought.org などのパブリックサーバーで息づいています。本書は、彼らの長年にわたる貢献の上に成り立っています。

NetHack の素晴らしいところの一つは、あまりにも奥深く、あまりにも緻密であるため、スポイラー（ネタバレ情報）を知ったとしてもゲームの面白さが決して損なわれないことです。その秘密を知れば知るほど、このゲームはさらに奥深く、魅力的なものになります。そうした精神のもと、この新しい 5.0 スポイラー集が、新世代のプレイヤーたちに NetHack の楽しさを届ける助けとなることを願っています。

NetHack の世界へようこそ！

---

## 読み進める前に

**警告。** 本書を読むことで、あなたが「脅威の迷宮」で得るゲーム体験は大きく変わることになります。さまよう目 (floating eye) を見つめるだけで麻痺してしまうという事実をひとたび知ってしまえば、それを「知らなかった頃」に戻ることは二度とできません。周到な準備の安心感よりも、自らの手で発見するスリルを好む冒険者もいます。もしあなたがそうであるなら、今すぐ本書を閉じ、痛い目を見ながら自力で学んでいくべきです。それもまた、このゲームの真の醍醐味なのですから。

**公式マニュアルをお探しですか？** ネタバレなしの操作コマンド一覧、アイテムリスト、基礎的なゲームシステムを知りたい場合は、ゲームに付属している公式ガイド**[脅威の迷宮案内記 (Guide to the Mazes of Menace)](../guidebook/)**を参照してください。あなたが今読んでいる本書は「戦略ガイド」です。すでに基本的な操作方法を理解しており、いかにして「生き残るか」を知りたい冒険者を対象としています。

度重なる水のニンフ (water nymph) に所持品を根こそぎ奪われたことがある方、[ノームの鉱山](#the-gnomish-mines)をどうしても突破できない方、あるいはダンジョン地下4階で食料が尽き、神に見捨てられて餓死することにうんざりしている方は、ぜひこの先をお読みください。あなたが生き延びられるよう、全力を尽くして手引きします。

### 本書の使い方

初めて潜る際は、まず[持ち物の準備](#what-to-pack)、[序盤の黄金律](#the-golden-rules-of-early-survival)、そして[差し迫った死から身を守る方法](#delayed-deaths)をお読みください。各種データ表や終盤の攻略章は、ダンジョン内で必要に迫られるまでは後回しで構いません。

プレイ中は、目次や索引をフィールドマニュアル（実用手引書）として活用してください。目の前に現れたモンスター、画面に表示された見慣れないメッセージ、これから使おうとしているアイテムなどをその都度引くとよいでしょう。アイテムの各章では、実戦でよく遭遇する有用なケースを優先して解説しています。正確な売買価格や詳細な数値が必要になったときは、巻末の各種データ表を参照してください。

**表記規則。** `@` や `#pray` などの等幅フォントテキストは、ゲーム画面に表示される文字や、プレイヤーがキーボードで入力するコマンドを表します。**太字**は覚えておくべき重要な鉄則・指針です。*Dlvl* はダンジョンの深度（地下階数）を、*XL* はキャラクターの経験レベルを表します。通貨単位はゾークミッド（*zm*）です。**5.0の新要素**と記された項目は、NetHack 3.6以前のバージョンで学んだプレイヤーにとって特に重要です。久しぶりにプレイする復帰冒険者は、まず[前回からの変更点](#what-changed-since-last-time)から読み始めるのもおすすめです。

#### ダンジョン緊急時チェックリスト

状況が一変して絶体絶命の危機に陥ったときは、**キーボードを叩くのを直ちに止め、画面上部に表示されたメッセージをもう一度よく読み直してください。**

1. **ステータス確認**: 現在のHP、空腹度、荷物の重量負荷（重荷/burdened など）、そして画面下に表示されているすべての状態異常（盲目、混乱、失神、毒など）を確認する。
2. **即時退路の確保**: 上り階段、閉められる扉、または1ターンで逃げ込める安全地帯がないか周囲を見回す。インベントリからアイテムを探すのは、目に見える退路を確認した後です。
3. **Elberethの活用**: 歩いて逃げられないときは、敵が隣接する前に床の埃に指で `Elbereth` と刻む（engrave）。時間に余裕があるなら、アサメなどの刃物で恒久的に刻む。
4. **神への祈り**: 属性信仰値と幸運 (Luck) が正常であり、前回の祈りから十分なターン数が経過していれば、神への祈り (`#pray`) で致命的な危機から救済される。ただしゲヘナ (Gehennom) では神の加護はほとんど期待できない。
5. **即死カウントダウンの対処法**:
   - **石化 (stoning)**: 直ちにトカゲの死骸 (lizard corpse) を食べる。
   - **スライム化 (sliming)**: 炎の杖や炎の巻物など、炎（火）を使って身を焼く。
   - **病気 (illness)**: 祝福された回復の薬 (blessed potion of healing)、または無呪の超回復の薬 (potion of extra healing) を飲む。ユニコーンの角を使う。
   - **窒息・首吊り (strangulation)**: 直ちに首飾り（絞殺の魔除け / amulet of strangulation）を外すか、神に祈る。
6. **死の記録**: 持ち物のすべてを尽くしても助からないときは、その死の経緯をメモに残しておく。NetHack は、プレイヤーが二度と同じ過ちを繰り返さないよう痛烈な教訓を刻み込むのが実に得意なゲームです。

::: web-only

<aside class="download-box">
<strong>オフラインで読みたい場合:</strong> 日本語版の印刷・閲覧用PDF（<a href="companion.ja.pdf">companion.ja.pdf</a>）をご利用いただけます。
</aside>

:::

---

## 目次

**第1部: 旅立ちの前に (Part One: Before You Set Out)**

1. [遠征の選択](#choosing-your-expedition) — 役職、種族、そして属性
2. [持ち物の準備](#what-to-pack) — 初期装備と序盤の優先事項
3. [最初の潜行](#your-first-descent) — ダンジョン序盤の生存戦略

**第2部: ダンジョンの光景 (Part Two: Dungeon Sights)**

4. [迷宮の地形と構造](#the-lay-of-the-land) — 部屋、通路、ダンジョンの特徴（マップ付き）
5. [ダンジョン生態系フィールドガイド](#field-guide-to-dungeon-fauna) — モンスター系統の一覧
6. [注目の名所・設備](#points-of-interest) — 泉、祭壇、玉座、流し台
7. [分岐とランドマーク](#branches-and-landmarks) — 鉱山、倉庫番、そしてその先へ
8. [罠と危険](#traps-and-hazards) — ダンジョンが仕掛ける数々の罠
9. [感覚と物音](#feelings-and-sounds) — 何が起きたかを伝える謎めいたメッセージ

**第3部: 生存の知恵 (Part Three: Survival)**

10. [差し迫った死から身を守る方法](#delayed-deaths) — 警告メッセージと即座に取るべき対処法
11. [刻み文字とエルベレス](#engravings) — 床に文字を刻んで結界を作る
12. [戦闘の技術](#the-art-of-combat) — 命中率、ダメージ計算、そして戦術
13. [冒険者を殺すもの](#things-that-will-kill-you) — 死因ワースト10、典型的な死、ミミック、ドラゴン
14. [セーブと亡霊（ボーンズファイル）](#saving-and-bones) — 冒険の中断・再開と、倒れた先人たちが遺すもの
15. [即死の数々](#ways-to-die-instantly) — 即死トラップのパターンと見分け方
16. [神々との関係](#divine-relations) — 祈り、生贄、そして祭壇
17. [友を作る](#making-friends) — ペット、手懐け、そして平和的共存

**第4部: 装備と糧食 (Part Four: Gear and Provisions)**

18. [実践的なアイテム識別戦略](#a-practical-identification-strategy) — 未知のアイテムを見分ける方法（フローチャート付き）
19. [食糧と食事](#provisions-and-dining) — 食べ物、栄養価、そして死骸の摂食
20. [薬師の手引き](#the-apothecary) — 薬（ポーション）とその多彩な効能
21. [巻物棚](#the-scroll-rack) — 巻物の効果と、混乱状態での読書
22. [杖](#wands) — 魔法の杖（ワンド）
23. [指輪と魔除け](#rings-and-amulets) — 運命を左右する装飾品
24. [冒険の七つ道具](#tools-of-the-trade) — つるはしから魔法のランプまで
25. [武器庫と防具庫](#the-armory) — 武器、防具、そして攻撃のメカニズム
26. [呪いとその解法](#curses-and-how-to-break-them) — 呪いの見抜き方、解呪、そして対処法

**第5部: 熟達と終局 (Part Five: Mastery and Endgame)**

27. [呪文の詠唱](#spellcasting) — 学びを重んじる冒険者のための魔法
28. [幸運と運命](#luck-and-fortune) — 冒険者の運命を形作る隠された数値
29. [能力値の鍛錬](#exercising-your-stats) — 腕力・知力・賢さ・器用度・体質・魅力を育てる日常の行動
30. [スキルの熟達](#enhancing-skills) — 戦闘スタイルと魔法技能の強化
31. [願いと祈願](#wishes-and-wishing) — 望むものを手に入れる究極の力
32. [アーティファクト](#artifacts) — 伝説の武具とその入手方法
33. [ゲヘナへの突入](#into-gehennom) — 城の関所と深淵の世界
34. [昇天（アセンション）](#the-ascension) — 最終装備を整え、地上へと脱出する

**付録 (Appendices)**

35. [上級操作コマンド](#advanced-controls) — 繰り返し回数指定、プレフィックス、効率化テクニック
36. [設定カスタマイズ](#options-worth-knowing-about) — 知っておくべき重要オプション設定 (.nethackrc)
37. [倉庫番の完全解法](#sokoban-solutions) — 全8パターンの完全攻略法
38. [自発的挑戦（コンダクト）](#voluntary-challenges) — 厳しい誓いと自己制限プレイ
39. [商店: クレジット、借金、そしてトラブル](#shopping-and-shopkeeper-pricing) — ダンジョン内の商取引と店主価格
40. [武器データ表](#weapons-tables)
41. [防具データ表](#armor-tables)
42. [呪文データ表](#spell-tables)
43. [モンスター図鑑データ表](#bestiary-tables)
44. [内在・外在能力データ表](#intrinsic-and-extrinsic-tables) — 獲得できる能力とその付与源
45. [前回からの変更点](#what-changed-since-last-time) — 3.6.x と 5.0 の違いと対策
46. [謝辞](#acknowledgements) — 巨人の肩の上に立って

## 第1部: 旅立ちの前に (Part One: Before You Set Out)

<!-- audit
2026-05-22 community-strategy additions citation index:
- 本監査パスでは、コミュニティで培われた攻略戦略を精選して本書に統合しました。各追加項目は、計画文書 `strategy-audit.md` 内で出典URLと相互参照されています。主な情報源は NetHackWiki (https://nethackwiki.com/wiki/)、そのFandomミラー (https://nethack.fandom.com/wiki/)、David Damerell による識別および祈りスポイラー (chiark.greenend.org.uk)、Kate Nepveu による Steelypips RGRN アーカイブ (https://www.steelypips.org/nethack/) です。
- 個々の引用エントリについては strategy-audit.md を参照してください。
-->

### 遠征の選択

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Rogue backstab is melee-only; removed "counts even at range" (uhitm.c:960 gates on hmd->hand_to_hand: "multi-shot throwing is too powerful here").
- Healer has no Sick_resistance (hea_abil = poison-res@1, warning@15; attrib.c:41-43); tainted food still sickens (eat.c:1904,1939). Narrowed "cannot be made sick" to the potion of sickness, which is Healer-cased (potion.c:969,977).
- Verified correct: all 13 roles' intrinsic-gain XLs (attrib.c:26-89), alignment/race availability (role.c), race stat caps (role.c:597-678), starting kits (u_init.c:42-178), Archeologist scroll-decipher on pickup (invent.c:1036), Barbarian HP-advance 10 (role.c:102), Excalibur gates (fountain.c:404-410).
-->
<!-- audit
2026-05-21:
- Archeologist starts with touchstone (u_init.c:50) and knows_object(TOUCHSTONE) so the tool itself is identified (u_init.c:660-662); does NOT have knows_class(GEM_CLASS) — gems are NOT pre-identified; touchstone identifies gems by rubbing per apply.c:2678-2707 (Ken Arnold)
- Healer starts with wand of sleep, 4 potions of healing, 4 potions of extra healing, and 3 blessed spellbooks (healing, extra healing, stone-to-flesh) (u_init.c:81-90); the spellbooks are always blessed so reading them always succeeds
- Tourist starts with 4 scrolls of magic mapping, 2 potions of extra healing, 21-40 +2 darts, Hawaiian shirt, expensive camera, credit card, and 10 random food items (u_init.c:150-159)
2026-05-18:
- Knight starts with +1 long sword and +1 lance (u_init.c:91-92)
- Cave Dweller gains Fast at XL 7 (attrib.c:37)
- Knight gains Fast at XL 7 (attrib.c:45)
- Healer starts with poison resistance at XL 1 (attrib.c:41)
- Ranger gains Searching XL 1, Stealth XL 7, See Invisible XL 15 (attrib.c:63-66)
- Elf gains sleep resistance at XL 4 (attrib.c:95)
- Cave Dweller starts with sling + flint stones (u_init.c:68-71)
- Ranger starts with +2 cloak of displacement (u_init.c:128)
- Wizard starts with cloak of MR + wand + rings + potions + scrolls + books + marker (u_init.c:167-176)
- Knight has intrinsic jumping from XL 1 (u_init.c:691)
- amethyst converts booze (not sickness) to fruit juice (potion.c:2161-2163)
- unicorn horn converts sickness to fruit juice (potion.c:2151-2154)
- Mjollnir is the Valkyrie sacrifice gift; needs a co-aligned altar (artilist.h:109)
- Knight code penalizes attacks on fleeing or helpless monsters (uhitm.c:336-339); peaceful kill is Samurai's giri
- all 13 role alignment/race availabilities (role.c)
- race stat caps (Str/Int/Wis/Dex/Con/Cha): Human {STR18(100),18,18,18,18,18} (role.c:597-598); Elf {18,20,20,18,16,18} (role.c:617-618); Dwarf {STR18(100),16,16,20,20,16} (role.c:637-638); Gnome {STR18(50),19,18,18,18,18} (role.c:657-658); Orc {STR18(50),16,16,18,18,16} (role.c:677-678)
- race stat FLOORS are uniformly {3,3,3,3,3,3} for every race (role.c:597, 617, 637, 657, 677)
- race intrinsic tables (attrib.c:91-105): hum_abil=none; dwa_abil=Infravision@XL1; elf_abil=Infravision@XL1+Sleep_resistance@XL4; gno_abil=Infravision@XL1; orc_abil=Infravision+Poison_resistance both@XL1
- initial roll distributes 75 points starting from role attrbase, clipped by race ATTRMAX, floor ATTRMIN=3 (attrib.c:723-737, init_attr_role_redist at 699-718); initial values typically land well below the race cap
- strategy aligned with NetHackWiki Valkyrie, Excalibur: Valkyrie is widely cited as the easiest beginner role; Knight 1-in-6 Excalibur dip at XL 5+ confirmed (https://nethackwiki.com/wiki/Valkyrie, https://nethackwiki.com/wiki/Excalibur)
-->

迷宮へ足を踏み入れる前に、まずは**役職 (role)**、**種族 (race)**、そして**属性 (alignment)** を選択します。この3つの組み合わせによって、初期装備、固有能力、信仰する神々、そして安全に扱えるアーティファクトが決まります。

初めての冒険なら、**「秩序」の「人間」または「ドワーフ」の「ワルキューレ」**を選ぶのがおすすめです。初期能力値と装備が強力で、最初から冷気耐性を持ち、序盤から強力な武器を入手する確実なルートが存在します。もちろん、他に興味を惹かれる役職があれば、迷わずそちらを選んでください。最初の数回の死は、キャラクター選択画面の解説文の何倍もの教訓を与えてくれるはずです。

#### 役職 (The Roles)

| 役職 (Role) | 属性 (Alignments) | 種族 (Races) | 序盤の強み (Early edge) | 主な難点 (Main difficulty) |
|---|---|---|---|---|
| 考古学者 (Archeologist) | 秩序、中立 | 人間、ドワーフ、ノーム | 採掘道具およびアイテム識別手段 | 近接白兵戦が脆弱 |
| 野蛮人 (Barbarian) | 中立、混沌 | 人間、オーク | 圧倒的な高HPと毒耐性 | 有用な魔法が極めて少ない |
| 洞窟人 (Cave Dweller) | 秩序、中立 | 人間、ドワーフ、ノーム | 頑強でシンプル、強力な射撃武器スタート | 初期耐性が皆無 |
| 治療師 (Healer) | 中立 | 人間、ノーム | 回復魔法、眠りの杖、毒耐性 | 貧弱な武器と防具 |
| 騎士 (Knight) | 秩序 | 人間 | 優れた鎧、仔馬、ランス、長剣 | 騎乗操作や騎士道戒律の違反リスク |
| 武闘家 (Monk) | すべて | 人間 | 移動速度、各種耐性、素手格闘術 | 重鎧の禁止と菜食（食事制限） |
| 司祭 (Priest) | すべて | 人間、エルフ | 一目でアイテムの呪詛状態 (BUC) が判明 | 序盤の攻撃力が中途半端 |
| レンジャー (Ranger) | 中立、混沌 | 人間、エルフ、ノーム、オーク | 弓、矢、幻影のクローク | 戦うには敵との距離が必要 |
| 盗賊 (Rogue) | 混沌 | 人間、オーク | 複数の短剣、隠密性、鍵開け器具 | 防具が軽装 |
| 侍 (Samurai) | 秩序 | 人間 | 高速行動、充実した武具、優れた和弓 | 義理や武士道戒律によるペナルティ |
| 観光客 (Tourist) | 中立 | 人間 | 投げ矢、カメラ、地図の巻物 | 序盤が極めて脆弱 |
| ワルキューレ (Valkyrie) | 秩序、中立 | 人間、ドワーフ | 優れた盾と最初からの冷気耐性 | 後半に魔法防御を自力確保する必要あり |
| 魔法使い (Wizard) | 中立、混沌 | 人間、エルフ、ノーム、オーク | 魔法防御と充実した初期アイテム群 | 低HPかつ初期食料なし |

各役職と種族のレベルごとの詳細な獲得能力については、[内在・外在能力データ表](#intrinsic-and-extrinsic-tables)を参照してください。

選んだ役職によって、初期インベントリ、成長時に獲得する内在能力、スキルの上限、そして固有のクエストが決定されます。これらの違いが、同じダンジョンを攻略する際のアプローチを根本から変えることになります。ワルキューレなら序盤から真っ向から殴り合い、魔法使いなら遠距離から仕留め、考古学者なら壁を掘り進んで戦闘を回避することができるのです。

**考古学者 (Archeologist)** *（秩序または中立）*。脅威の迷宮におけるインディ・ジョーンズ。つるはし、鞭 (bullwhip)、食料を保存するための缶詰作成道具 (tinning kit)、宝石を識別するための試金石 (touchstone)、そして幸運のフィドーラ (fedora) を身につけて出発します。戦士ではなく探検家の装備です。つるはしは武器としても道具としても使える特別なアイテムです。戦闘で振り回すだけでなく、迷宮そのものを掘り進むためにも使えます。新たな通路を切り開き、金貨が眠る閉ざされた隠し宝物庫の壁を破り、あるいは真下の階層へと一直線に竪穴を掘り抜くこともできます。試金石で擦るだけで本物の宝石とガラス玉を一瞬で見分けられ、その専門知識ゆえに巻物を拾い上げた瞬間にその銘を解読して自動識別できます。最初は打たれ弱いため、序盤の階層では正面から殴り合うよりも忍耐と隠密性が報われます。しかし頭脳明晰で、生まれつき天性の魔法使いに匹敵する知力と賢さを持っています。初期状態では魔法を使えませんが、呪文の書を入手するにつれて魔法の才能を開花させていきます。やがてつるはしやサーベルの達人となり、フロア全体の構造を一瞬で暴く「地図化 (magic mapping)」をはじめとする予言系の呪文を自在に操れるようになります。考古学者が心に刻むべき鉄則が一つあります。それは**「歴史的彫像を決して破壊してはならない」**ということです。どの石像が歴史的価値を持つかを見抜けるのは考古学者だけですが、過去の遺産を破壊することは神の怒りを買い、属性信仰値を大きく損なうことになります。

**野蛮人 (Barbarian)** *（中立または混沌）*。純粋な筋肉の塊であり、全役職中最大のヒットポイントを誇ります。その戦法は、力任せに敵を叩き潰し、相手の反撃よりも長く耐え抜くことです。序盤の迷宮における大半の脅威は、重武器の一撃を数回叩き込むだけで粉砕できます。最初から**[毒への完全耐性](#damage-resistances)**を備えており、序盤の死因のかなりの割合を占める毒死を完全に無力化できます。巨大な両手持ち武器（両手剣または戦斧）、予備の片手武器、鉄環の鎧 (ring mail)、そして食料を携えて始まります。ゲーム序盤は、ただ敵の群れに突進して武器を振り回すだけで軽快に進めるでしょう。問題が生じるのは、中盤に差しかかり、筋肉を一切意に介さない魔法攻撃を操るモンスターと遭遇し始めてからです。早い段階から魔法防御（最も確実なのは灰色ドラゴンの鱗鎧 / gray dragon scale mail）の確保を目指しましょう。なお毒が一切効かないため、普通の冒険者なら命を落とすような怪しい薬や危険な死骸の「味見テスト」ができる点も大きな強みです。

**洞窟人 (Cave Dweller / Caveman)** *（秩序または中立）*。本作で最もシンプルで、余計な複雑さに悩まされることなくダンジョンのイロハを学ぶのに最適な役職です。原始的ですが極めて頑丈です。こん棒、投げつけるための火打ち石 (flint stones) の山とスリング、革鎧、そして成長とともに気前よく伸びていく豊富なHPを持っています。学ぶべき呪文の書も、初期の呪文も一切ありません。洞窟人を際立たせているのは「持っていないもの」です。初期耐性が一切ありません。他の役職が最初から火、冷気、あるいは毒に対する保護を与えられているのに対し、洞窟人は適切なモンスターの死骸を喰らうことで、その一つひとつを自力で勝ち取っていかなければなりません。火蟻 (fire ant) を食べれば火耐性が、殺人蜂 (killer bee) を食べれば毒耐性が得られます。戦闘面ではこん棒、メイス、六尺棒 (quarterstaff)、槍、スリングの達人になれるほか、野蛮人と同様に素手格闘の達人にもなれるため、武器を失っても強烈な打撃を繰り出せます。初期の知力が低く呪文スキルも限定的なため、魔法書よりも巻物に頼るのが賢明です。最前線での重厚な白兵戦を楽しみたいなら、種族には人間またはドワーフを選ぶとよいでしょう。

**治療師 (Healer)** *（中立）*。迷宮の医師。戦争ではなく医療のための装備を身につけて到着します。聴診器、小さな外科手術用のメス (scalpel)、回復の薬を手一杯に携え、読んだ瞬間に爆発しないよう最初から祝福された3冊の回復魔法の書、そして何より**眠りの杖 (wand of sleep)** です。この杖こそが序盤最大の防御手段です。第1〜第5階層に現れるモンスターの大半は睡眠への耐性を持っておらず、危険な強敵であっても一筋の光線でその場に昏倒させることができます。他の安全な手段で倒せない強敵のために杖の充填回数（チャージ）を温存しておきましょう。聴診器は1ターン目から大活躍します。モンスターに当てれば残りHPが正確に把握でき、自分自身に当てれば隠れた状態異常や病気を察知できます。生まれつき2つの恩恵を持っています。毒に対する完全耐性と、病気の薬 (potion of sickness) の効果を受けない耐性です。未知の謎の薬を飲んでも、毒死したり病気にかかったりすることはありません（ただし麻痺や睡眠は防げません）。殴り合いの乱闘向きではないため、序盤は眠りの杖に頼り、中盤以降は自らの治癒魔法を駆使して戦います。やがて短剣、六尺棒 (quarterstaff)、投げ矢、そしてユニコーンの角の扱いに熟達し、中盤以降は「回復の薬を飲む冒険者」から「回復魔法を唱えて戦う術者」へと劇的に進化します。

<!-- audit
2026-08-01: lance-on-foot corrected. is_pole() includes P_LANCE (obj.h:228),
so a wielded lance reaches distance 2 via #apply like any polearm (apply.c
use_pole gates on is_pole(uwep)). Only the joust is mounted-only (joust()
needs a steed, uhitm.c). Prior "dead weight on foot" was wrong; it keeps reach.
Riding a strong steed (pony/horse/warhorse all M2_STRONG, monsters.h) forces
carrcap=MAX_CARR_CAP (hack.c weight_cap), so riding raises carrying capacity.
-->
**騎士 (Knight)** *（秩序）*。馬上の騎士道精神。騎士道の名誉ある戒律と、頼もしい相棒を連れて戦場へ赴きます。1ターン目から**鞍を置いた仔馬 (saddled pony)** が傍らに寄り添い、長剣、**ランス (lance)**、そして全身を包む鎧、兜、盾、手袋を装備しています。徒歩の状態でもランスは2マス離れた敵を突く間合い武器（長柄武器）として活用できますが、馬に乗った状態で敵へ突進する「馬上槍試合（ジャウスト / joust）」を繰り出せば、他のどの役職も真似できない圧倒的な壊滅的ダメージを叩き出せます。これほどランスを巧みに扱える役職は他にいません。愛馬に騎乗している間は所持重量の上限も大幅に増加します。ただし、馬の背に飛び乗る行為は見た目以上に危険を伴います。乗馬に失敗して落馬すると10〜14ポイントもの大ダメージを受け、序盤の騎士ならそれだけで瀕死に陥りかねません。序盤は落馬確率が5割近くに達するため、無理に乗馬を急ぐのは禁物です。まずは仔馬にりんごを与えて大きく育て、馬、そして戦闘用の馬へと成長させ、成功率が十分に上がってから鞍に跨がりましょう。騎士団には2つの重要な掟と特権があります。秩序の騎士が長剣を手にして**泉 (fountain)** に入ると、ゲーム内で最も高い確率で伝説の聖剣**[エクスカリバー (Excalibur)](#excalibur-artifact)** を引き当てることができます。一方で、騎士道の戒律により、逃走中、睡眠中、または無力な状態の敵を攻撃することは固く禁じられており、違反すると神の信認を失います。仔馬にはりんごを与え、にんじんは自らの盲目を治すために温存し、常に名誉ある戦いを選びましょう。

**武闘家 (Monk)** *（全属性）*。素手で戦い始め、他の役職が到達できない究極の素手格闘術を極めることができます。やがてその拳は名だたる名剣をも凌駕する破壊力を帯びるようになります。冒険の最初から[不可視の視認](#senses-and-perception)能力を持ち、睡眠攻撃を寄せ付けず、並外れた高速移動が可能です。さらに他のどの役職よりも早いペースで新たな内在能力を習得していきます。この強力な格闘ボーナスを維持するには、常に身軽で荷物負荷（重荷/burdened など）のない状態を保たなければなりません。胴鎧を着ると命中率に20ポイントもの大ペナルティを受け、盾を構えると格闘ボーナスが消失し、頭・手・足に金属製防具をつけると魔法詠唱が阻害されます。そのため、初期装備である**ローブ (robe)** 以外はほとんど何も身につけずに戦うのが最も効果的です（ローブは魔法詠唱を鈍らせるどころか鋭敏にしてくれます）。ローブを大切に扱い、菜食主義（ベジタリアン）の食事制限を守り抜いて誓約（コンダクト）を維持しましょう。

**司祭 (Priest)** *（全属性、神の属性と一致）*。その信仰心により、あらゆるアイテムの呪詛状態（祝福されているか、呪われているか、無呪であるか / BUC）を一目で看破できます。床に落ちているクロークが呪われていないか不安に怯える必要は二度とありません。メス、ローブ、盾、そして4本の**聖水 (holy water)** を携えて旅立ちます。さらに聖水はいつでも自作可能です。自分の宗派の祭壇に普通の水 (potion of water) を置き、神に祈る (`#pray`) だけで、その山のすべての水が一瞬で聖水へと浄化されます。あなたの神は、祭壇での生贄に対しても特別な恩恵を与えてくれます。生贄によって最初に下賜されるアーティファクトは、悪魔を粉砕するために鍛えられた祝福された銀のメイス**「デーモンベイン (Demonbane)」**であることが保証されています。価値ある生贄を捧げるたびに、6分の1の確率でこの至宝が授けられます。司祭は堅実な戦士であると同時に、やがて強力無比な聖職者魔法の術者へと成長し、あらゆる打撃武器や治癒・予言・僧侶系魔法の達人となります。1点だけ注意すべきは、自身の幸運 (Luck) を損なわないことです。生贄を重ねて神の寵愛を確固たるものにするまでは、平和的なモンスターを殺したり鏡を割ったりしてはなりません。さもないと、絶体絶命の祈りに対する神の返答は、期待とは正反対の惨劇となるでしょう。

**レンジャー (Ranger)** *（中立または混沌）*。遠距離からの狙撃を得意とする天性の狩人。弓と矢筒いっぱいの矢、そして**+2 幻影のクローク (cloak of displacement)** を身につけて始まります。このクロークは敵の攻撃を実際の位置から1マスずれた幻影へと逸らすため、本作屈指の安全な開幕手札を誇ります。その真価は圧倒的な射撃手数にあります。弓のスキルを高めると、わずか1ターンの間に2本から3本もの矢を同時に連射できるようになり、並のモンスターなら近づくことすら叶わず射抜かれます。さらに卓越した観察眼を持ち、歩いているだけで立ち止まって探すことなく隠し通路や罠を発見できます。2つの実践知識を覚えておきましょう。最も優れた矢である初期の**+2**矢は普通の矢よりも格段に折れにくいため、本気の強敵との戦いまで温存し、第1階層のイモリ (newt) のような無害な雑魚には安物の矢を使いましょう。そしてレンジャーの定位置は常に遠距離です。一歩下がり、壁を背にして、前線で殴り合うのではなく矢の雨に敵を仕留めさせましょう。

**盗賊 (Rogue)** *（混沌）*。暗闇に潜む泥棒。刃物の扱いが素早く、足音は誰よりも静かです。身軽な装備で旅立ちます。小剣、一握りの投擲用短剣、革鎧、最初からあらゆる扉や宝箱を開け放つ**鍵開け器具 (lock pick)**、そして戦利品を詰め込む麻袋です。気配を完全に殺して移動し、眠っているモンスターの脇を気付かれずにすり抜けることができます。そして逃走中や不意を突かれた敵に一撃を加えるとき、その**不意打ち（バックスタブ / backstab）**は正面から切り込むよりも遥かに甚大な致命傷を叩き込みます。所持している短剣は突くためではなく投げるためのものであり、1ターンに複数本を同時に投擲できます。後には、初期所持している毒薬を使って、拾った投げ矢や矢、ボルト、手裏剣に毒を塗ることができます（短剣には毒を塗れません）。常に物陰に潜み、ドアを蹴破ったり敵の群れに突っ込んだりするような、居場所を暴露する乱暴で不器用な振る舞いは避けましょう。

**侍 (Samurai)** *（秩序）*。古き伝統を受け継ぐ規律正しき戦士。刀の腕前は神速にして必殺です。迷宮で最も優れた片手剣の一つである**刀 (katana)**、小刀である**脇差 (wakizashi)**、矢筒を備えた**和弓 (yumi)**、そして鉄片の鎧 (splint mail) を身につけ、他の戦士が苦労して手に入れる俊敏な移動速度を最初から備えています。刀はゲーム序盤を鮮やかに切り開いてくれるでしょう。ただし、相棒の脇差は二刀流のパートナーとしては適していません。小柄な脇差は刀の刀術スキルを共有しないため、普通の長剣 (long sword) を見つけたら脇差と持ち替えましょう。両手に剣を構えれば、双方の刃を最高の熟練度で同時に振り回すことができます。背中の和弓も忘れてはなりません。修練を積めば、和弓はレンジャーに匹敵する遠距離脅威となり、近接戦で恐るべき戦士が1ターンに2〜3本の矢を放ちながら接近を拒むという無敵の強さを誇るようになります。

**観光客 (Tourist)** *（中立）*。バカンス気分で迷宮に到着します。派手なアロハシャツ、クレジットカード、**高価なカメラ (expensive camera)**、山のような**+2 投げ矢 (dart)**、少々の回復の薬、そして4枚の**地図の巻物 (scroll of magic mapping)** です。防具は皆無に等しく、HPも低く、まともな近接武器もないため、序盤はあらゆる敵が命取りになります。生き延びる鍵は筋肉ではなく知恵です。カメラこそが切り札です。フラッシュを焚くことで迫り来るモンスターの目を眩ませ（盲目状態にし）、盲目になった敵を安全な距離から投げ矢で痛めつけ、ペットにトドメを刺させることができます。地図の巻物は最も危険な難関フロアのために温存しておきましょう。店主たちは観光客の足元を見てきます。経験を積んで一人前になるまでは、店主は法外に高く売りつけ、こちらの売却額を極端に安く買い叩いてきます。本格的な買い物は冒険の後半まで待ちましょう。この過酷な序盤を生き延びれば、観光客は大化けします。クエスト報酬である「白金のエンドール急行カード (Platinum Yendorian Express Card)」は、魔法耐性を授けるだけでなく道具の充填回数を回復（リチャージ）する効果を持ちます。知力を高めれば、終盤の観光客は強力な魔法の使い手にもなります。全役職中最も難関であり、観光客での昇天（クリア）はすべての冒険者にとって最高の栄誉となります。

**ワルキューレ (Valkyrie)** *（秩序または中立、女性専用）*。最初の昇天（クリア）を目指すすべてのプレイヤーに推奨される王道の役職であり、それには十分な理由があります。開幕から圧倒的に強く、死ににくく、プレイングが極めてシンプルです。北方の戦乙女であるワルキューレは、槍、短剣、頑丈な**+3 小さな盾**を装備し、最初から**冷気耐性**を備え、序盤のダンジョンに真っ向から立ち向かえる優れた戦闘能力値を誇ります。神々もまた、終盤の勝利を手厚く約束してくれています。属性を問わず、生贄によって最初に確実に授けられる神の恩寵品は、雷鳴轟く伝説の戦槌**[ミョルニル (Mjollnir)](#mjollnir)** です。腕力を25まで高めたワルキューレなら、ミョルニルを敵へ投擲し、ブーメランのように手元へと自動回収することができます。ほぼすべての武器を高い熟練度で扱えるようになります。唯一警戒すべきは油断です。自慢の筋肉は中盤まで大いに助けになりますが、ゲヘナ (Gehennom) の悪魔たちが放つ魔法は鎧もHPも一切無視して襲いかかります。ゲヘナへ足を踏み入れる前に、必ず魔法耐性（魔法を防ぐクロークや灰色ドラゴンの鱗鎧など）と反射能力を揃えておきましょう。

**魔法使い (Wizard)** *（中立または混沌）*。大半の冒険者がゲーム全体を通じて血眼になって探し求める至宝を、最初から羽織って旅立ちます。すなわち**魔法を防ぐクローク (cloak of magic resistance)** です。1ターン目から凶悪な即死魔法の数々を完全に無力化できます。さらに六尺棒 (quarterstaff)、杖、2つの指輪、一握りの薬と巻物、魔法のマーカー、そして接近するあらゆる敵を吹き飛ばす**衝撃 (force bolt)** の呪文を携えています。最も脆いのは序盤です。肉体は打たれ弱く、魔法エネルギー (PW) も乏しいため、拳で殴り合うのではなく、杖と衝撃の呪文を駆使して慎重に戦わなければなりません。魔法の各系統を学ぶにつれ、呪文の書を一目で識別できるようになります。充実した魔法の書庫を手に入れた中盤の魔法使いは、あらゆる戦闘に対して完璧な解答を持っています。呪文を唱えるときは六尺棒を手に持っておきましょう（呪文詠唱の成功率を安定させてくれます）。そして2つの注意点があります。初期食料を持たず、分け前を譲ってくれない**小猫 (kitten)** を連れていること、そして衝撃の呪文は床に落ちている薬を粉砕してしまうことです（詳細は[呪文の詠唱](#spellcasting)を参照）。

#### 種族 (The Races)

種族は、キャラクターの初期能力値、能力値の最大上限、そして最初から持っている内在能力に影響を与えます。いかなる能力値も 3 未満には下がりません。以下の表は、各種族が到達できる各能力値の最大上限値を示しています。

| 種族 (Race) | 腕力 (Str) | 知力 (Int) | 賢さ (Wis) | 器用度 (Dex) | 体質 (Con) | 魅力 (Cha) | 内在能力 (Intrinsics) |
|---|---|---|---|---|---|---|---|
| 人間 (Human) | 18/100 | 18 | 18 | 18 | 18 | 18 | なし |
| エルフ (Elf) | 18 | 20 | 20 | 18 | 16 | 18 | 赤外線視覚、XL 4で睡眠耐性 |
| ドワーフ (Dwarf) | 18/100 | 16 | 16 | 20 | 20 | 16 | 赤外線視覚 |
| ノーム (Gnome) | 18/50 | 19 | 18 | 18 | 18 | 18 | 赤外線視覚 |
| オーク (Orc) | 18/50 | 16 | 16 | 18 | 18 | 16 | 赤外線視覚、毒耐性 |

**人間 (Human)**。[赤外線視覚](#senses-and-perception)も毒耐性も特殊な天賦の才も持ちません。しかし、すべての役職を選択できる唯一の種族です。ノームやオークは依然として敵対的であり、人間だからといって鉱山が友好的になることはありません。

**ドワーフ (Dwarf)**。屈強な戦士であり、器用度と体質の上限値は全種族中最高を誇り、腕力の上限も人間に匹敵します。レベル1から赤外線視覚を持ち、レベルアップ時のHP上昇量は全種族中最高です。さらにつるはしによる採掘速度が通常の2倍になり、足元に埋まっている財宝を直感で感知できます。何よりノームの鉱山の住人たちの多くが平和的（中立）に接してくれます。選択可能役職: 考古学者、洞窟人、ワルキューレ。

**エルフ (Elf)**。赤外線視覚に加え、経験レベル4 (XL 4) で[睡眠耐性](#damage-resistances)を獲得します。HPは低めですが、知力と賢さの上限値が最高であり、レベルごとの魔法エネルギー (PW) 成長率も全種族トップです。さらに生まれつきの弓ボーナス（あらゆる弓で命中+1、エルフの弓なら命中+2）を持ち、普段弓を使わない役職でもこの恩恵を受けられます。エルフの司祭と魔法使いは初期装備として楽器が付属します。選択可能役職: 司祭、レンジャー、魔法使い。

**ノーム (Gnome)**。レベル1から赤外線視覚を持ち、知力の上限が人間よりわずかに高めです。ノームの鉱山に棲むノームやドワーフの大半が最初から平和的（非敵対）であり、序盤の難所である鉱山が肉挽き器から安全な買い物ツアーへと一変します。さらに**試金石 (touchstone)** が祝福されていなくても擦るだけで宝石を識別できます。ノームのレンジャーは腕力16でクロスボウの連射が可能になります（通常は腕力18が必要）。選択可能役職: 考古学者、洞窟人、治療師、レンジャー、魔法使い。

**オーク (Orc)**。レベル1からの毒耐性が極めて有用で、毒を持つコボルド (kobold) の死骸を安全に平らげることができます（序盤の貴重な無料の栄養源になります）。また、同族食い（共食い）のペナルティを受けることなく、倒した他のオークの死骸を食べることができます。全体的な能力値上限は低めで、人間・エルフ・ドワーフからは種族的に敵視されがちです。ただし、普段から平和的な店主、司祭、監視員などは敵対化しません（他のオークも自動的に仲間になるわけではありません）。選択可能役職: 野蛮人、レンジャー、盗賊、魔法使い。

#### 属性 (Alignment)

秩序 (Lawful)、中立 (Neutral)、混沌 (Chaotic) という3つの属性を、一般的な「善・中庸・悪」と捉えてしまいがちですが、NetHack はそうした道徳的な善悪でプレイヤーを裁くわけではありません。本作における属性とは、**「自分が信仰する神の教義や戒律をどれほど忠実に守り抜いているか」を測る客観的な数値（属性信仰値）**なのです。

敵対的なモンスターを討ち倒せば、通常はこの数値が上昇します。逆に、平和的な（友好的・中立的な）モンスターを殺害すると、どの属性であっても属性値が即座に5ポイント削られ、理不尽な虐殺は幸運 (Luck) の喪失という重い罰を招きます。一部の役職にはさらに固有の厳しい戒律が存在します。騎士が無力な敵を攻撃すると騎士道違反として評価を失い、侍が平和的な者に斬りかかれば武士の義理を欠いたとして手痛いペナルティを受けます。傷ついた属性値は、通常の敵対モンスターを討伐することや、祭壇に新鮮な[生贄](#sacrifice)を捧げることで回復できます。

属性はまた、信仰する神、挑むべき固有のクエスト、そして触れても安全なアーティファクトを決定づけます。秩序のキャラクターは経験レベル5 (XL 5) 以上で**泉 (fountain)** からエクスカリバーを引き抜く資格を得ます。盗賊は常に混沌であり、ドワーフは常に秩序です。祭壇に関する詳細なルールについては、[祭壇と属性](#altars-and-alignment)を参照してください。

---

<!-- audit
2026-05-18:
- tripe rations are dog food for typical PCs (eat.c:2138-2145)
- orcs and carnivores enjoy tripe (eat.c:2132-2136)
- altar BUC flash is amber/black and sets bknown (do.c:363-389)
- pets avoid cursed items (dogmove.c:535-536, 1065-1067)
- touchstone identifies gems (apply.c:2658-2696)
- floating-eye paralysis fires on melee against the eye (uhitm.c:5853, 6022)
- Burdened status label (botl.c:12)
- food ration weight and nutrition (objects.h:1110)
- strategy aligned with NetHackWiki Curse-testing, Altar: altar amber/black flash and pet step-avoidance are confirmed canonical curse-testing techniques (https://nethackwiki.com/wiki/Curse-testing, https://nethackwiki.com/wiki/Altar)
-->

### 持ち物の準備 (What to Pack)

初期装備（スターティングキット）は役職ごとにあらかじめ決まっており、それぞれの強みに適したものが揃っていますが、すぐに強化していく必要があります。ゲーム序盤に階層を下りていく際は、以下に挙げるアイテムに常に目を光らせておきましょう。大半の役職の弱点を劇的に補ってくれます。

#### 序盤の買い物・調達リスト (The Early Shopping List)

**食料の確保。** 冒険者は必ず空腹になります。それは想像以上の早さで訪れます。しかし、主な食料源は持ち物袋の中に入っているレーションではありません。菜食主義の役職をプレイしているのでない限り、**序盤のダンジョンにおける主食は、自分が倒した敵の死骸です。** 倒したばかりの新鮮な死骸をその場で食べながら進めば（`e` を押して足元の死骸を選択）、食料レーションは主食ではなく非常用の備蓄食料となります。見かけた食料（food ration）はもちろんすべて拾うべきですが、持ち歩くのは2〜3個で十分です。溜め込む必要はありません。トライペの食料 (tripe ration) はペットのためのものであり、あなたが食べるものではありません。

**アイテムの識別手段。** ゲーム序盤における主な識別手段は、祭壇（アイテムを置いて祝福/呪いの光を確認する）、ペット（呪われたアイテムに乗るのを嫌がる）、そして試行錯誤です。**識別の巻物 (scroll of identify)** は貴重ですが、しばらく手に入らないこともあります。**試金石 (touchstone)**（宝石を識別する灰色の石）も役に立ちます。商店では、価格によって一部のアイテムを見分けることができます。最も安い巻物は識別の巻物であり、最も安い薬は回復の薬 (potion of healing) です。詳細な識別テクニックは、[実践的なアイテム識別戦略](#a-practical-identification-strategy)を参照してください。
<!-- price-ID verification (objects.h): scroll of identify base
cost 20 (objects.h:1213, SCROLL cost field = 5th arg per macro at
1182) is the cheapest scroll; potion of healing base cost 20
(objects.h:1145, POTION cost = 6th arg per macro at 1121) is the
cheapest potion. Each is the unique 20-zm item in its class; the
next cheapest are scroll of light (50) and potions of booze / fruit
juice / see invisible / sickness (50). -->

**防具の強化。** AC（アーマークラス）が 6 以上（悪い状態）で、アイテムを鑑定するための祭壇もペットもいない場合は、見つけた普通の胴鎧、兜、盾、クロークを身につけましょう。それらに呪いがかかっていたとしても、無防備の丸腰で歩き回る危険に比べれば大抵はマシです。ただし、靴と手袋だけは事前にテストしてください。呪われた浮遊の靴、不器用の靴、または呪われた手袋を身につけてしまうと、逃走すらできなくなる危険があります。

**武器の選定。** 大半の役職は、最初から持っている初期武器を使い続けるべきです。それはあなたの最も得意なスキルと一致しており、使い続けることで[`#enhance`](#enhancing-skills) コマンドを通じてスキルを高めることができます。また、武器を持ち替えると、初期装備に付与されていたかもしれないプラスの強化値（エンチャント）を捨てることになります。武器の持ち替えを検討すべきなのは、貧弱な初期武器しか持たない観光客、洞窟人、治療師である場合、自分の得意スキルに合致する強力な武器を見つけた場合、あるいは**銀製 (silver)** の武器である場合です（銀は獣人、吸血鬼、悪魔、影、小悪魔に対して強烈な追加ダメージを与えます。なお通常のゾンビやミイラには効果がありません）。盾を構える選択肢を残したいなら、片手武器を優先しましょう。

**投擲武器の準備。** 短剣、投げ矢、槍、あるいは弓矢を、袋の奥底に仕舞い込まずいつでも投げられるよう手元に準備しておきましょう。**さまよう目 (floating eye)** を相手に近接攻撃を挑んでは決してなりません。ロゼ (rothe)、ホムンクルス (homunculus)、殺人蜂 (killer bee)、兵隊蟻 (soldier ant) なども、敵が隣接する前に遠距離から削っておくほうが遥かに安全です。

**自制心（荷物の整理）。** 初心者の冒険者は見つけたものを何でも拾い集めます。歴戦の熟練者は必要なものだけを拾います。その差は約40ポンドの重量差となり、ノームの領主 (gnome lord) から逃げ切れるかどうかの生死の境目となります。ステータス行に**「重荷 (Burdened)」**と表示されているなら、使い切れないほどの荷物を抱え込んでいます。移動速度が落ち、モンスターによってはあなたが1回行動する間に2回殴りかかってくるようになります。荷物が重くなりすぎたら、必須でないものは潔く捨てましょう。ただし、置き去りにするアイテムには注意してください。モンスターは落ちているアイテムを拾い、箱を漁る知能を持っています。不要な荷物は1つ上の階層に置いてくるとよいでしょう。モンスターが階層を越えて荷物を運ぶことはありません。

---

### 最初の潜行 (Your First Descent)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Jackal packs are 2-4, not "four to seven" (G_SGROUP -> m_initgrp n=3; makemon.c:29,105; monsters.h:199).
- Foxes (G_GENO|1) and dwarves (G_GENO|3) are solitary; removed from the group-spawn list. Killer bees (LGROUP), soldier ants & gnomes (SGROUP) do swarm.
- Verified correct: stair-fall rnd(3) HP (do.c:1797), corpse-rot thresholds (eat.c:1887-1939), supply-chest details (mklev.c:1026-1127), cheapest-price scroll/potion (objects.h).
-->
<!-- audit
2026-05-21:
- poison-resistance corpse list for Rule 6, all with MR_POISON in both mresists and mconveys: killer bee (monsters.h:100), cave spider (monsters.h:944), yellow mold (monsters.h:1636); black pudding glob also conveys MR_POISON via mconveys (monsters.h:2118)
- puddings carry G_NOCORPSE (monsters.h:2114) so there is no CORPSE object, but on death they drop a GLOB_OF_BLACK_PUDDING / GLOB_OF_BROWN_PUDDING / etc. food item (mon.c:715-734 mksobj_at)
- eating a glob takes the same intrinsic path as eating a corpse: `piece->otyp == CORPSE || piece->globby` both trigger cpostfx(corpsenm) which calls givit() for each conveyed property (eat.c:562, 2040, 2984)
- kicking a sink can summon a black pudding: 4/5 outcomes are klunk, otherwise 1/3 chance of black pudding (dokick.c:1201-1238) — the canonical beginner trick to roll cold+shock+poison resistance globs
- magic resistance and reflection have no intrinsic source for players in 5.0; both come only from extrinsics: GDSM (do_wear.c:806-883), amulet of reflection, cloak of MR, silver shield, silver/gray DSM
2026-05-18:
- stair-falling damage is 1-3 HP via rnd(3) (do.c:1780-1795)
- floating-eye paralysis (mhitu.c:2536-2557)
- pets step around their owner (dogmove.c:535)
- lizard and lichen corpses never rot (eat.c:58-61)
- killer bees: speed 18, G_LGROUP, M1_POIS sting AT_STNG/AD_DRST 1d3 (monsters.h:96-102)
- supply chests appear above Oracle: at most one per level (placed in a random fillable room); 2/3 chance per level; 2/3 chest vs 1/3 large box; 5/6 locked (mklev.c:1010-1119)
- prayer cooldown uses rnz(350), averaging about 450 turns but with a long tail (pray.c:1356)
- corpse safe within 30 turns; tainted past ~175 turns (eat.c:1887, 1939)
- strategy aligned with NetHackWiki Stoning, Prayer, Magic resistance: lizard corpse as petrification cure, prayer-when-in-Trouble cooldown, and MR/reflection/poison-resistance "big three" are canonical advice (https://nethackwiki.com/wiki/Stoning, https://nethackwiki.com/wiki/Prayer, https://nethackwiki.com/wiki/Magic_resistance)
-->

階段を降りる。空気は冷たく湿っている。目の前には通路が伸び、暗闇の中へと分岐している。傍らにはペットが足音を立ててついてくる。

ダンジョンへようこそ。

最初の数フロアは手加減してくれますが、それはあくまで相対的な話です。モンスターも弱いですが、あなたもまた、最低限の装備、低いHP、そして中盤以降の生存に不可欠な耐性を何ひとつ持たない最も脆弱な状態です。他のどの階層よりも地下1階から5階で命を落とす冒険者が圧倒的に多いのは、敵が強大だからではなく、こちらに対抗手段がほとんどないからです。

#### 序盤生存の黄金律 (The Golden Rules of Early Survival)

**鉄則 1: 勝てない相手とは戦うな。** 最初の交戦（1発殴り合った直後）で撤退するかどうかを決断してください。残りHPが数ポイントに削られてからでは手遅れです。可能なら上り階段へ逃げ込みましょう。それが無理なら、閉められる扉、そして一本道の通路へと退避します。どうしても退路がない場合は、モンスターが隣接する前に、`E` を押して `-`（指）を選択し、床の埃に `Elbereth` と刻みましょう。

```
  危険: 開けた部屋での乱戦         有効: 通路での隘路（1対1）

  ┌─────·──────┐                  ┌─────·──────┐
  │·o··Z·······│                  │·o···Z······│
  │··k·@·G·Z···│                  │··k··G······│
  │····o·······│                  │·o··········+##@
  │··G·········│                  │··G·········│
  └────────────┘                  └────────────┘

  四方を包囲されて即死。          1体ずつおびき寄せて各個撃破。
```

**鉄則 2: よく分からないものは食べるな。** モンスターの死骸は強力な内在能力を授けてくれることもありますが、毒に冒されたり、食中毒を起こしたり、あるいはそれ以上の惨劇をもたらすこともあります。その死骸の効果を熟知するまでは、床に放置しておくのが無難です（例えばコボルド `k` の肉は猛毒であり、何の能力も得られません）。例外として、食料 (food ration)、レンバス (lembas wafer)、クラムの食料 (cram ration)、そして果物は常に安全に食べられます。**苔の怪物 (lichen)** の死骸は安全で、絶対に腐敗しません。**トカゲ (lizard)** の死骸も安全で腐らず、さらに石化を治療してくれます。トカゲの死骸は袋に入れず、手元のインベントリに持っておきましょう。コカトリス (cockatrice) に触られたとき、噛んで飲み込むまでに残された猶予はわずか2ターンです。**イモリ (newt)** の死骸も安全で、時に魔法エネルギー (PW) を1〜3ポイント回復してくれます。これは駆け出しの術者にとって序盤で最初に手に入る持続可能なマナ回復源となります。

**鉄則 3: ペットは最高の友である。** 初期ペットはあなたの傍らで戦ってくれるだけでなく、アイテムを拾い上げてくれます（ペットは呪われたアイテムを踏むのを嫌がるため、安全確認のテストとして極めて有用です）。さらに訓練次第で商店から泥棒させることすら可能です。トライペの食料 (tripe ration) や死骸を足元に落として、こまめにエサを与えておきましょう。

**鉄則 4: 神への祈りを学べ。** 死の危機（HPの危険な激減、食料がない極度の衰弱、石化の進行）に直面したときは、神に祈る (`#pray`) ことができます。序盤において、十分な属性信仰値とマイナスでない幸運 (Luck) があれば、祈りはほぼ確実にあなたを救ってくれます。ただし、最初の300ターン以内には決して祈ってはなりません。一度祈ったら、安全のために約1000ターンは間隔を空けましょう（実際の回復は平均約500ターンですが、大きくブレることがあります）。不適切なタイミング（神が怒っているとき、[ゲヘナ](#gehennom)にいるとき、あるいは前回の祈りから時間が経っていないとき）に祈ると、事態はさらに致命的に悪化します。軽微なトラブルで祈りを浪費してはなりません（詳細なシステムは[神々との関係](#divine-relations)を参照）。属性信仰値を失ってしまった場合は、敵対的なモンスターを討伐しましょう。中立のキャラクターであっても、コボルドやオークを倒すことは有効な信仰値回復になります。

**鉄則 5: 徹底的に探索し、目的を持って移動せよ。** あらゆる行動ターンは栄養を消費します。何百ターンも無駄に足踏みしていれば餓死してしまいますが、かといって部屋を素通りして駆け抜ければ必要な物資を見落とします。各フロアを隅々まで探索し（部屋を調べ、扉を開け、`s` または `10s` で隠し通路を探す）、そのフロアが提供するものを回収したら先へ進みましょう。下り階段の場所が分かったら、壁を叩くのに何百ターンも費やしてはなりません。もし「空腹 (Hungry)」状態でフロアに食料が残っていないなら、迷わず階段を降りましょう。

**鉄則 6: 防御を固めよ。** ゲーム前半における最大の目標は、財宝集めではなく、終盤を生き抜くための耐性を揃えることです。最も重要な3大防御は、**[魔法耐性](#damage-resistances)**、**反射**、そして**[毒耐性](#damage-resistances)** です。毒耐性は適切な死骸を喰らうことで内在能力として得られます。殺人蜂 (killer bee)、巨大グモ (giant spider)、黄色モールド (yellow mold)、あるいは流し台 (sink) を蹴って出現する[黒いプリン](#a-note-on-puddings)などです。魔法耐性と反射は装備品から得られます。ドラゴン鱗鎧（魔法耐性なら灰色ドラゴンの鱗鎧、反射なら銀色ドラゴンの鱗鎧）、魔法を防ぐクローク、反射の魔除け、銀の盾、あるいは神からの下賜品、[クエスト](#the-quest)、願いによって手に入れます。

**鉄則 7: キー入力は慎重に、キーリピートは厳禁。** キーを1回押すごとに1ターンが消費されます。移動キーを押しっぱなしにしてオートリピートさせると、キャラクターは盲目的に前進し、予期せぬ強敵との遭遇、現れたばかりの罠、あるいは誤って泉 (fountain) の水を飲むなどして命を落とします。キーは1回ずつ押し、状況を確認してください。1マスずつキーを叩かずに長い通路を移動するには、**Shift＋方向キー**のショートカットを活用しましょう。大文字の `H J K L Y U B N` はアイテムや扉を通り過ぎて走り、前方にモンスターが現れるか攻撃を受けたときに自動停止します。さらに慎重に進むなら `G`＋方向キーを使いましょう。モンスター、アイテム、扉の隣で確実に停止します。オートリピートにはそうした安全機能は一切ありません。

#### ダンジョンの危険と生き残り術 (Dungeon Hazards and How to Survive Them)

序盤に多発する典型的な死因と、その防止策を以下にまとめます。

**飢餓 (Starvation)。** 「衰弱 (Weak)」や「失神寸前 (Fainting)」に追い込まれてからではなく、ステータスに「空腹 (Hungry)」が表示された時点で食事をとってください。食料がない状態で「空腹」になったら、ためらわずに下の階層へ降りましょう。探索済みのフロアに新しい食料が生えてくることはありません。「衰弱」はすでに神への祈りの緊急事態（祈りの対象）とみなされます。「失神寸前」になったら、直ちに何かを食べるか祈らなければ命はありません。

**さまよう目 (Floating eye)。** マップ上では青い `e` で表示されます。小さく、一見無害に見えます。しかし**絶対に近接攻撃で殴ってはなりません**。直接殴ると強烈な麻痺を受け、その場に氷のように固まったあなたの肉体へ、周囲のあらゆるモンスターが一方的に無料の連続攻撃を叩き込んできます。遠距離攻撃で倒すか、無視して迂回しましょう。さまよう目の移動速度は極めて鈍重です。

**腐敗した死骸 (Rotted corpses)。** 床に長く放置された死骸を食べると、治療しなければ死に至る食中毒を起こします。死骸は倒した直後の新鮮なうちに食べましょう。確実に安全なのは討伐後約30ターン以内です。それを超えると腐敗の判定がランダムになり、約175ターンを過ぎた無呪の死骸は確実に腐っています。万一食中毒にかかった場合は、祝福された回復の薬 (blessed potion of healing)、無呪の超回復の薬 (potion of extra healing)、完全回復の薬 (potion of full healing)、ユニコーンの角 (unicorn horn)、あるいはユーカリの葉 (eucalyptus leaf) を使用してください。祈る場合は、[神々との関係](#prayer)にある祈りの条件を満たしていることを必ず確認してください。

**荷物の持ちすぎによる階段転落。** 過剰な荷物を抱えた状態で階段を使うと、足を踏み外して転落し、1〜3 HP のダメージを受けます。手持ちの荷物袋に入っているコカトリス (cockatrice) の死骸は安全ですが、もし手に武器として装備していた場合、転落した拍子に死骸に触れて自ら石化死してしまいます。

**開けた部屋での群れによる包囲。** ジャッカル (jackal) の噛みつきダメージは1体あたり 1d2 に過ぎませんが、上層階では2〜4頭の小群れで出現し、開けた部屋の中で四方から冒険者を包囲します。殺人蜂 (killer bee)、兵隊蟻 (soldier ant)、ノーム (gnome) も同様に群れをなして押し寄せてきます。2体以上の敵に狙われた兆候が見えたら、即座に出入口の扉や一本道の通路へと退却してください。敵がまだ距離を取っているなら、その場で待ち構えて敵に接近のターンを消費させましょう。群れに向かってこちらから前進するのは、敵に余計な攻撃ターンをプレゼントするようなものです。

**[ノームの鉱山](#the-gnomish-mines)への無謀な早急突入。** 鉱山町 (Minetown) より深い鉱山フロアには、重厚な防具をまとったドワーフやノームの領主 (gnome lord) がひしめいています。強固な防具を持つ敵の集団と白兵戦を繰り広げる準備が整っていないなら、深入りせずに運命の迷宮のメインルートへと引き返し、装備が充実してから再挑戦しましょう。

#### 補給用の箱 (Supply Containers)

**NetHack 5.0の新要素:** 誰かがダンジョン内に親切な救援物資（ケアパッケージ）を配置してくれています。

[賢者 (Oracle) の神託所](#the-oracle)より上のすべての階層には、3分の2の確率で「補給用の宝箱（サプライチェスト）」が出現します。通常は宝箱 (chest)（たまに大きな箱 / large box）で、大抵は鍵がかかっており、冒険者の生存を助けるアイテムが少なくとも1つ必ず入っています。中身の抽選プールは以下の通りです。

- **回復の薬 (potion of healing)**（各チェストごとに約50%の確率、2本入っていることもあります）
- **超回復の薬 (potion of extra healing)**、**加速の薬 (potion of speed)**、**魔力の薬 (potion of gain energy)**
- **武器に魔法をかける巻物 (scroll of enchant weapon)**、**鎧に魔法をかける巻物 (scroll of enchant armor)**、**怪物を混乱させる巻物 (scroll of confuse monster)**、**怪物を怯えさせる巻物 (scroll of scare monster)**
- **穴掘りの杖 (wand of digging)**
- **回復の魔法書 (spellbook of healing)**

さらに3分の2の確率で、低レベルの魔法書を中心とした追加のランダムアイテムが1個含まれます。なお、ノームの鉱山の入口がある階層では中身が異なり、食料 (food ration)、クラムの食料 (cram ration)、またはレンバス (lembas wafer) が確定で手に入ります。

外見は普通の宝箱や箱と全く同じで、特別な目印はありません。神託所より上のフロアでは、見かけたすべての宝箱や大きな箱を必ず調べましょう。施錠されている箱は、クレジットカード、鍵、開錠の杖 (wand of opening)、あるいは `#force` コマンドでこじ開けることができます。こじ開ける際は可能な限り短剣 (dagger) などの刃物を使いましょう。刃物は折れる心配が極めて少なく、逆に鈍器で無理やり叩き割ると、箱そのものと中に入っていた貴重な回復の薬を粉々に破壊してしまいます。

---

## 第2部: ダンジョンの光景 (Part Two: Dungeon Sights)

マップはさまざまな記号で埋め尽くされていますが、本当に立ち止まって警戒すべき記号はごく一部です。ダンジョン内の施設や設備を見つけたときは[注目の名所・設備](#points-of-interest)を、見慣れない階段を降りる前には[分岐とランドマーク](#branches-and-landmarks)を参照してください。生態系フィールドガイドは辞書のように引くためのものです。アルファベットを見つけたら、短い警告だけでは不十分な場合にリンク先を追ってください。

```{=latex}
\vspace*{0.6in}
```

```{=latex}
% The map follows immediately after this opening page. Lower the
% chapter opener so TeX has less room to stretch the short paragraphs.
\vspace*{0.4in}
```

### 迷宮の地形と構造 (The Lay of the Land)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source: no corrections. Verified DoD depths, all branch placements, Gehennom & Elemental Planes ordering (dungeon.lua), Sokoban/Orcus prizes, Big Room 40%, map symbols.
-->
<!-- audit
2026-05-21:
- branch staircases render with the S_brupstair / S_brdnstair symbols in CLR_YELLOW (defsym.h:124-125)
- the brupstair / brdnstair glyph is only selected after known_branch_stairs is true: the stair leads to a different dungeon AND the hero has traversed it (stairs.c:180-183, display.c:2347-2354)
2026-05-18:
- DoD is 25-29 levels (rn1(5,25) = rn2(5)+25) (dungeon.lua:10-11, hack.h:1535)
- Gnomish Mines branch DL 2-4 (dungeon.lua:15-19)
- Oracle DL 5-9 (dungeon.lua:60-66)
- Sokoban entry is one level above the Oracle, going up (dungeon.lua:20-25)
- 4 Sokoban levels with 2 fixed variants each (dat/soko*.lua)
- Big Room 40% chance, DL 10-12 (dungeon.lua:66-73)
- Quest portal DL 11-16 (dungeon.lua:26-31; chainlevel oracle base=6 range=2)
- Rogue Level DL 15-18 (dungeon.lua:52-58)
- Fort Ludios portal placed at any DL 11 up to just above Medusa, 1/3 per qualifying level (mklev.c:2647-2651)
- Medusa DL ~21-25 (dungeon.lua:74-80)
- Castle at bottom of DoD, DL ~27 (dungeon.lua:81-83)
- Mine's End: 3 variants, all guarantee a not-cursed luckstone (minend-1.lua:77, minend-2.lua:116, minend-3.lua:67)
- 7 Minetown variants; 1-in-7 is Orcish Town (minetn-1.lua, dungeon.lua:179-184)
- 5.0 sink glyph is white `{`, shared with bright-blue fountain (defsym.h:133, fixes5-0-0.txt:827)
- Travel/farlook matches on displayed symbol; `#` no longer cycles to sinks (getpos.c:1046-1062)
- Trap room places 1 randomly chosen trap type from 8 (themerms.lua:101-114)
- Teleportation hub places 2-4 fixed-destination teleporters (themerms.lua:264-279)
- Fake Delphi is a geometric joke: empty room within an Oracle-shaped room, no monsters (themerms.lua:291-305)
- Light source room places exactly one lit oil lamp (themerms.lua:204-210)
- Massacre places 5-25 role corpses only — no wraith (themerms.lua:172-189)
- Mausoleum places one waiting M/V/L/Z monster or one @ corpse (themerms.lua:419-443)
-->

脅威の迷宮の構造はゲームごとに毎回新しく生成されますが、各分岐ダンジョン、特殊フロア、そして大まかな階層の深さは常に一定です。その全体の骨格を把握していれば、次に何が待ち受けているかを常に予測することができます。

#### 全体像 (The Big Picture)

ダンジョンは、主幹となる本流といくつかの支流（分岐ダンジョン）を持つ樹形図のような構造になっています。正確な深度はゲームごとに多少変動しますが、以下の図が典型的な全貌を示しています。

**運命の迷宮 (Dungeons of Doom)** は上半分を占め、おおよそ地下1階から27階まで広がっています。途中の分岐からは、**[ノームの鉱山 (Gnomish Mines)](#the-gnomish-mines)**（*[幸せの石 (luckstone)](#luck-and-fortune)* や *[店 (shops)](#shopping-and-shopkeeper-pricing)* があります）、**[倉庫番 (Sokoban)](#sokoban)**（最上階にご褒美がある *[パズル](#sokoban)*）、あなたの **[クエスト (Quest)](#the-quest)** ダンジョン（自分の役職のリーダーから貴重なアーティファクトを取り戻す任務を課されます）、そして時には **ルディオスの要塞 (Fort Ludios)**（ゴールドが詰まった宝物庫）へと通じています。主幹の終点は **城 (The Castle)** であり、ここは [ゲヘナ (Gehennom)](#gehennom) への玄関口となっています。

**ゲヘナ (Gehennom)** は下半分です。溶岩に満ちた迷路階層と悪魔の君主たちが待ち受け、最深部の [モロクの聖域 (Moloch's Sanctum)](#molochs-sanctum) に **イェンダーの魔除け (Amulet of Yendor)** が安置されています。魔除けを手に入れたら、今度は **属性の諸平面 (Elemental Planes)** を登って **霊界 (Astral Plane)** を目指します。そこではあなたの神が捧げ物を待っています。

<!-- DMAP-BEGIN -->
<div><figure style="margin: 1.5em 0; text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 611" role="img" aria-label="Dungeons of Doom map" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;font-feature-settings:'liga' 0, 'dlig' 0;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><line x1="380" y1="55" x2="380" y2="611" stroke="#B5651D" stroke-width="2.5" fill="none"/><rect x="40" y="0" width="680" height="39" rx="4" fill="#B5651D"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">DUNGEONS OF DOOM</text><line x1="150" y1="140" x2="150" y2="246" stroke="#5B8E3A" stroke-width="2" fill="none"/><line x1="630" y1="166" x2="630" y2="194" stroke="#B58A1A" stroke-width="2" fill="none"/><line x1="630" y1="305" x2="630" y2="343" stroke="#3B6FA0" stroke-width="2" fill="none"/><rect x="290" y="55" width="180" height="40" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="72" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">The Dungeon Entrance</text><text x="380" y="89" font-size="12" font-style="italic" fill="#555" text-anchor="middle">up-stair to exit</text><rect x="60" y="108" width="180" height="32" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="129" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Gnomish Mines</text><rect x="60" y="168" width="180" height="40" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="185" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Minetown</text><text x="150" y="202" font-size="12" font-style="italic" fill="#555" text-anchor="middle">shops, temple</text><rect x="60" y="246" width="180" height="40" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="263" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Mine's End</text><text x="150" y="280" font-size="12" font-style="italic" fill="#555" text-anchor="middle">luckstone</text><rect x="290" y="163" width="180" height="40" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="180" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">The Oracle</text><text x="380" y="197" font-size="12" font-style="italic" fill="#555" text-anchor="middle">paid hints</text><rect x="540" y="126" width="180" height="40" rx="6" fill="#FFF4CC" stroke="#B58A1A" stroke-width="1.5"/><text x="630" y="143" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Sokoban prize</text><text x="630" y="160" font-size="12" font-style="italic" fill="#555" text-anchor="middle">bag of holding/amulet of reflection</text><rect x="540" y="194" width="180" height="32" rx="6" fill="#FFF4CC" stroke="#B58A1A" stroke-width="1.5"/><text x="630" y="215" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Sokoban entry</text><rect x="290" y="269" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="290" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle"><tspan>Q</tspan>uest portal</text><rect x="540" y="265" width="180" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="630" y="282" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle"><tspan>Q</tspan>uest entry</text><text x="630" y="299" font-size="12" font-style="italic" fill="#555" text-anchor="middle">your role's dungeon</text><rect x="540" y="343" width="180" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="630" y="360" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle"><tspan>Q</tspan>uest goal</text><text x="630" y="377" font-size="12" font-style="italic" fill="#555" text-anchor="middle"><tspan font-style="normal">★ </tspan>Bell of Opening, role artifact</text><rect x="290" y="329" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="350" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Big Room (40%)</text><rect x="290" y="389" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="410" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Rogue Level</text><rect x="60" y="420" width="180" height="40" rx="6" fill="#FFD966" stroke="#B5891A" stroke-width="1.5"/><text x="150" y="437" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Fort Ludios</text><text x="150" y="454" font-size="12" font-style="italic" fill="#555" text-anchor="middle">vault of gold</text><rect x="290" y="479" width="180" height="32" rx="6" fill="#B8D4F0" stroke="#2E5C8E" stroke-width="1.5"/><text x="380" y="500" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Medusa's Island</text><rect x="230" y="539" width="300" height="58" rx="8" fill="#FFFFFF" stroke="#B5891A" stroke-width="2.5"/><text x="380" y="565" font-size="17" font-weight="600" fill="#1f2933" text-anchor="middle">THE CASTLE</text><text x="380" y="582" font-size="14" font-style="italic" fill="#7A5A0A" text-anchor="middle">wand of wishing</text><line x1="380" y1="124" x2="240" y2="124" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="380" y1="210" x2="540" y2="210" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="470" y1="285" x2="540" y2="285" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="380" y1="440" x2="240" y2="440" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><text x="275" y="120" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">down</text><text x="500" y="206" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">up</text><text x="505" y="281" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portal</text><text x="275" y="436" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portal</text><circle cx="380" cy="124" r="4" fill="#B5651D"/><circle cx="380" cy="210" r="4" fill="#B5651D"/><circle cx="380" cy="440" r="4" fill="#B5651D"/><circle cx="380" cy="104.0" r="4" fill="#B5651D"/><circle cx="380" cy="114.0" r="4" fill="#B5651D"/><circle cx="150" cy="149.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="159.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="217.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="227.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="237.0" r="4" fill="#5B8E3A"/><circle cx="380" cy="134.0" r="4" fill="#B5651D"/><circle cx="380" cy="144.0" r="4" fill="#B5651D"/><circle cx="380" cy="154.0" r="4" fill="#B5651D"/><circle cx="630" cy="175.0" r="4" fill="#B58A1A"/><circle cx="630" cy="185.0" r="4" fill="#B58A1A"/><circle cx="380" cy="220.0" r="4" fill="#B5651D"/><circle cx="380" cy="230.0" r="4" fill="#B5651D"/><circle cx="380" cy="240.0" r="4" fill="#B5651D"/><circle cx="380" cy="250.0" r="4" fill="#B5651D"/><circle cx="380" cy="260.0" r="4" fill="#B5651D"/><circle cx="630" cy="314.0" r="4" fill="#3B6FA0"/><circle cx="630" cy="324.0" r="4" fill="#3B6FA0"/><circle cx="630" cy="334.0" r="4" fill="#3B6FA0"/><circle cx="380" cy="310.0" r="4" fill="#B5651D"/><circle cx="380" cy="320.0" r="4" fill="#B5651D"/><circle cx="380" cy="370.0" r="4" fill="#B5651D"/><circle cx="380" cy="380.0" r="4" fill="#B5651D"/><circle cx="380" cy="430.0" r="4" fill="#B5651D"/><circle cx="380" cy="450.0" r="4" fill="#B5651D"/><circle cx="380" cy="460.0" r="4" fill="#B5651D"/><circle cx="380" cy="470.0" r="4" fill="#B5651D"/><circle cx="380" cy="520.0" r="4" fill="#B5651D"/><circle cx="380" cy="530.0" r="4" fill="#B5651D"/></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 681" role="img" aria-label="Gehennom map" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;font-feature-settings:'liga' 0, 'dlig' 0;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><line x1="380" y1="0" x2="380" y2="39" stroke="#B5651D" stroke-width="2.5" fill="none"/><line x1="380" y1="0" x2="380" y2="625" stroke="#A14A3F" stroke-width="2.5" fill="none"/><rect x="40" y="0" width="680" height="39" rx="4" fill="#A14A3F"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">GEHENNOM</text><line x1="150" y1="288" x2="150" y2="306" stroke="#6B4E96" stroke-width="2" fill="none"/><rect x="290" y="53" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="70" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Valley of the Dead</text><text x="380" y="87" font-size="12" font-style="italic" fill="#555" text-anchor="middle">Gehennom's entrance</text><rect x="290" y="141" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="162" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Asmodeus's Lair</text><rect x="290" y="191" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="212" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Juiblex's Swamp</text><rect x="290" y="251" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="272" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Baalzebub's Lair</text><rect x="60" y="248" width="180" height="40" rx="6" fill="#E3D8F0" stroke="#6B4E96" stroke-width="1.5"/><text x="150" y="265" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Vlad the Impaler</text><text x="150" y="282" font-size="12" font-style="italic" fill="#555" text-anchor="middle"><tspan font-style="normal">★ </tspan>Candelabrum</text><rect x="60" y="306" width="180" height="32" rx="6" fill="#E3D8F0" stroke="#6B4E96" stroke-width="1.5"/><text x="150" y="327" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Vlad's Tower</text><rect x="290" y="351" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="368" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Orcus Town</text><text x="380" y="385" font-size="12" font-style="italic" fill="#555" text-anchor="middle">Wand of Orcus · magic lamp/marker</text><rect x="290" y="419" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="440" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Wizard's Tower</text><rect x="290" y="469" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="486" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Wizard of Yendor</text><text x="380" y="503" font-size="12" font-style="italic" fill="#555" text-anchor="middle"><tspan font-style="normal">★ </tspan>Book of the Dead</text><rect x="230" y="567" width="300" height="58" rx="8" fill="#2D2D2D" stroke="#FFC857" stroke-width="2.5"/><text x="380" y="593" font-size="17" font-weight="600" fill="#FFC857" text-anchor="middle">Moloch's Sanctum</text><text x="380" y="610" font-size="14" font-style="italic" fill="#FFE680" text-anchor="middle">the Amulet of Yendor</text><line x1="380" y1="322" x2="240" y2="322" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><text x="275" y="318" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">up</text><circle cx="380" cy="322" r="4" fill="#A14A3F"/><circle cx="380" cy="102.0" r="4" fill="#A14A3F"/><circle cx="380" cy="112.0" r="4" fill="#A14A3F"/><circle cx="380" cy="122.0" r="4" fill="#A14A3F"/><circle cx="380" cy="132.0" r="4" fill="#A14A3F"/><circle cx="380" cy="182.0" r="4" fill="#A14A3F"/><circle cx="380" cy="232.0" r="4" fill="#A14A3F"/><circle cx="380" cy="242.0" r="4" fill="#A14A3F"/><circle cx="380" cy="292.0" r="4" fill="#A14A3F"/><circle cx="380" cy="302.0" r="4" fill="#A14A3F"/><circle cx="380" cy="312.0" r="4" fill="#A14A3F"/><circle cx="150" cy="297.0" r="4" fill="#6B4E96"/><circle cx="380" cy="332.0" r="4" fill="#A14A3F"/><circle cx="380" cy="342.0" r="4" fill="#A14A3F"/><circle cx="380" cy="400.0" r="4" fill="#A14A3F"/><circle cx="380" cy="410.0" r="4" fill="#A14A3F"/><circle cx="380" cy="460.0" r="4" fill="#A14A3F"/><circle cx="380" cy="518.0" r="4" fill="#A14A3F"/><circle cx="380" cy="528.0" r="4" fill="#A14A3F"/><circle cx="380" cy="538.0" r="4" fill="#A14A3F"/><circle cx="380" cy="548.0" r="4" fill="#A14A3F"/><circle cx="380" cy="558.0" r="4" fill="#A14A3F"/><line x1="380" y1="631" x2="380" y2="681" stroke="#5B8E3A" stroke-width="2.5" stroke-dasharray="7,5" fill="none"/><text x="400" y="661" font-size="15" font-weight="600" font-style="italic" fill="#5B8E3A">now go <tspan style="font-weight:800;font-size:17px">ALL</tspan> the way back up...</text></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 299" role="img" aria-label="Elemental Planes and Ascension" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;font-feature-settings:'liga' 0, 'dlig' 0;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><rect x="40" y="0" width="680" height="39" rx="4" fill="#5D3C8E"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">THE ELEMENTAL PLANES</text><rect x="68" y="89" width="120" height="40" rx="6" fill="#E8DDC8" stroke="#8B6F47" stroke-width="1.5"/><text x="128" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Earth</text><rect x="236" y="89" width="120" height="40" rx="6" fill="#E0F4FA" stroke="#3B9FA8" stroke-width="1.5"/><text x="296" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Air</text><rect x="404" y="89" width="120" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="464" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Fire</text><rect x="572" y="89" width="120" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="632" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Water</text><rect x="260" y="179" width="240" height="42" rx="6" fill="#D8C6F0" stroke="#5D3C8E" stroke-width="1.5"/><text x="380" y="197" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Astral Plane</text><text x="380" y="213" font-size="12" font-style="italic" fill="#555" text-anchor="middle">three altars · pick yours</text><rect x="230" y="239" width="300" height="50" rx="10" fill="#FFE680" stroke="#B5891A" stroke-width="2.5"/><text x="380" y="262" font-size="18" font-weight="700" fill="#7A5A0A" text-anchor="middle" letter-spacing="0.1em">ASCENSION</text><text x="380" y="281" font-size="11" font-style="italic" fill="#7A5A0A" text-anchor="middle">offer the Amulet at your altar</text><path d="M 380 39 C 380 53 128 53 128 67 L 128 89" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="188" y1="109" x2="236" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><text x="212" y="105" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portals</text><line x1="356" y1="109" x2="404" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="524" y1="109" x2="572" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><path d="M 632 129 C 632 143 380 143 380 157 L 380 179" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="380" y1="221" x2="380" y2="239" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/></svg><figcaption style="font-style: italic; color: #5a5a5a; font-size: 0.9em; margin-top: 0.5em;">支流は主幹の左右へと延びています。丸印（小さな色付きの点）はおおよそのフロア数を示します。★ はモロクの聖域に入り、魔除けを手に入れるために必要な3つの開扉のアイテム（開放の鐘、燭台、死者の書）を示しています。</figcaption></figure></div>
<!-- DMAP-END -->

#### マップの記号 (The Map Symbols)

ダンジョン内のすべてのものは、画面上では記号で表現されます。
一目で判別できるように覚えておきましょう：

| 記号     | 意味                          |
| -------- | ----------------------------- |
| `.`      | 床（部屋）                    |
| `#`      | 通路、木、または雲            |
| `-`  `│` | 壁（水平、垂直）              |
| `+`      | 閉まった扉（または魔法書）    |
| `<`      | 上り階段                      |
| `>`      | 下り階段                      |
| `{`      | 泉（明るい青）または流し台（白） |
| `_`      | 祭壇                          |
| `\`      | 玉座                          |
| `^`      | 罠（発見後）                  |
| `@`      | あなた（または人間系モンスター） |
| `` ` ``  | 巨石                          |
| `}`      | 水または溶岩                  |

アルファベット文字はモンスターを表します。犬なら `d`、ドラゴンなら `D`、ゾンビなら `Z` です。色はその分類内の個別の種類を識別するのに役立ちます。例えば赤い `D` は赤ドラゴン（レッドドラゴン）であり、灰色の `D` は灰色ドラゴン（グレイドラゴン）です（[ダンジョン生態系ガイド (Field Guide to Dungeon Fauna)](#field-guide-to-dungeon-fauna) を参照）。

**色のメモ：分岐の階段は黄色に変わる。** 支流（ノームの鉱山や倉庫番）へと通じる階段は、一度通ると黄色で表示されるようになります。通常の主幹フロアの階段はデフォルト色のままなので、複数の階段が存在するフロアでも、黄色い階段を目印にすれば支流へと迷わず戻ることができます。

アイテムの記号は句読点や記号類です：

| 記号 | アイテム分類       |
| ---- | ------------------ |
| `)`  | 武器               |
| `[`  | 防具               |
| `%`  | 食料               |
| `!`  | 薬                 |
| `?`  | 巻物               |
| `/`  | 杖                 |
| `=`  | 指輪               |
| `"`  | 魔除け             |
| `(`  | 道具               |
| `+`  | 魔法書             |
| `*`  | 宝石および石       |
| `$`  | ゴールド（ゾークミッド、略称 **zm**） |

#### 部屋の種類 (Room Types)

ダンジョンのほとんどの部屋はありふれた通常の部屋で、何もないか、いくつかのアイテムやモンスターが点在している程度です。しかし、中には特殊な部屋もあります：

```
   A shop:                 A zoo:                 A throne room:
   ┌───────┐               ┌────────┐             ┌────────┐
   │[?!=/("│               │Z··Z$Z··│             │··Z·Z·Z·│
   │)%*[?!(│               │$Z···$Z·│             │·Z·\··Z·│
   │··@····│               │·Z$Z··Z$│             │··Z·Z···│
   └──+────┘               └───+────┘             └───+────┘
      #                        #                      #
   @ = shopkeeper          Z = sleeping           \ = throne
   Items for sale.         $ = gold piles         Monsters guard.
```

**店 (Shops)。** 内部にいる店主（通常は扉の近く）によって識別されます。店は特定の種類のアイテムを販売しています：雑貨屋、防具屋、武器屋、巻物屋、薬屋などがあります。店内の床にあるアイテムは店主の所有物です。拾い上げると価格が提示されます。手持ちのアイテムを売ることもできます。店主は戦闘において極めて強力なため、周到な計画がない限り盗みを働いてはいけません。

**寺院 (Temples)。** 祭壇があり、司祭または女司祭が管理している部屋です。祭壇の属性が重要となります：自分の属性と一致していれば、ここで捧げ物（犠牲）を捧げることで恩恵を得られます。一致していない場合、常駐の司祭はあなたの試みに対して友好的には応じてくれません。また、司祭にゴールドを寄付することで、透視能力や永続的なACボーナスを得ることもできます。[司祭への寄付 (Donating to Priests)](#donating-to-priests) を参照してください。

**玉座の部屋 (Throne rooms)。** [*玉座* (`\`)](#thrones) があり、玉座には眠れる統治者が座り、周囲には護衛のモンスター群がひしめいている部屋です。玉座に座るとランダムな効果が生じ、時には素晴らしい幸運をもたらし、時には悲惨な結果を招きます。

**動物園 (Zoos)。** 眠っているモンスターとゴールドで埋め尽くされた部屋です。10マス以内からあなたを視界に捉えられる睡眠中のモンスターは、毎ターン1/7の確率で目を覚まします。「忍び足（ステルス）」があれば覚醒を防げます。部屋の中に踏み込まず、扉口から戦うことで、一度に相手にするモンスターを1〜2体に絞りましょう。

**兵舎 (Barracks)。** 兵士たちで満たされた部屋です。彼らは統率が取れており武装していますが、同時に優れた装備を所持しています。戦いに耐えられる実力があるなら、掃討する価値は大いにあります。

**蜂の巣 (Beehives)。** 殺人蜂とローヤルゼリーでいっぱいの部屋です。蜂は群れをなすと非常に危険ですが、ローヤルゼリーは極めて優れた食料です。

**テーマのある部屋 (Themed rooms)。** ダンジョンには、形状（柱の林立、二重構造の部屋）や配置された内容が一風変わった部屋が何十種類も存在します。注意すべき主な部屋は以下の通りです：

- **光源の部屋 (Light source rooms)。** 高い確率で火のついたオイルランプが落ちています。タダで手に入る光源です。
- **埋もれた財宝 (Buried treasure)。** 床のどこかに *"Dig 3 east 2 south"*（東に3、南に2掘れ、などの指示）と焼かれた刻み文字があり、埋められた宝箱と3〜12個のランダムなアイテムの場所を示しています。ここでは「つるはし」がその重さ以上の価値を発揮します。
- **大虐殺 (Massacre)。** 人間の冒険者の死体が床一面に散乱しています。これらを食べても内在能力（耐性等）は得られません。人間が食べると共喰い（カニバリズム）のペナルティを受け、混沌以外のキャラクターが祭壇に捧げると重大な罪となります。
- **霊廟 (Mausoleum)。** 内部の小さな玄室に、1体の待ち構えるモンスター（ミイラ、吸血鬼、リッチ、ゾンビ）または人間の死体が配置されています。扉は慎重に開けましょう。
- **蜘蛛の巣、埋もれたゾンビ、罠部屋、テレポートのハブ (Spider nest, buried zombies, trap room, teleportation hub)。** これらは危険な罠として扱ってください。蜘蛛の巣や埋もれたゾンビは階層の深さに応じて強化されるため、一度退却して適切な対策を用意してから戻りましょう。罠部屋には、矢の罠から反魔法フィールド、地雷まで様々な罠が仕掛けられています。
- **柱のある部屋・分割された部屋 (Pillared and divided rooms)。** 柱が立ち並ぶ部屋、奥の小部屋、あるいは中央が遮蔽された部屋です。これらの角（コーナー）を利用して [エルベレス (Elbereth)](#elbereth) の文字を安全に保護したり、長柄武器（ポールアーム）の間合いを保って戦うことができます。

テーマのある部屋は通常の部屋の中に混ざって生成されます。1つのフロアに複数存在することもあります。

---

### ダンジョン生態系ガイド (Field Guide to Dungeon Fauna)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Displacer beast has no melee place-swap; removed the fabricated "50% chance to swap places." M3_DISPLACES only barges past other monsters when moving (mm_displacement, mon.c, monster-vs-monster). Corpse still grants temporary Displacement (eat.c:1265-1268).
- Verified correct: soldier ant/bat/centaur/jabberwock/mumak/xorn/gargoyle/naga stats, mind-flayer helmet block 7/8 (uhitm.c:3235), gremlin night-only intrinsic strip (uhitm.c:3040) & water split (mon.c:987).
-->
<!-- audit
2026-05-18:
- xan: AT_STNG AD_LEGS (sting cripples legs); xan is class `x`, not the engulfer `t` (S_TRAPPER) (monsters.h:1157-1159)
- leprechaun attack is AT_CLAW AD_SGLD (gold-steal claw), not a bite (monsters.h:660)
- long worms grow tail segments on a movement-driven wgrowtime timer, not per hit (worm.c:218-237)
- pudding split admits IRON|METAL weapons only (uhitm.c:1616-1618)
- there are no dragonhide weapons in 5.0; DRAGON_HIDE material is body-armor-only
- silver and wooden weapons are the actual pudding non-splitters (uhitm.c:1616-1620 admits IRON|METAL only)
- all other class-symbol mappings (defsym.h) and per-monster stats verified clean
- rothe ('q'-class fame): three attacks per turn (claw + two bites), the only Q-class monster lacking M2_STRONG, and the canonical early-q threat per NetHackWiki (https://nethackwiki.com/wiki/Rothe, https://nethackwiki.com/wiki/Quadruped)
2026-05-31 audit:
- homunculus (S_IMP class `i`) AT_BITE AD_SLEE 1d3, Level 2, speed 12, flies, sleep-resistant itself (monsters.h:551-558). The sleep effect on bite is a real early-game threat — sleep status + adjacent enemies is often lethal. Both the Field Guide summary at companion.md:905 and the bestiary intro at companion.md:10976 had previously described the `i` class as "annoying but not dangerous" / "none individually scary"; corrected to flag the homunculus specifically.
- water moccasin (M1_POIS, AD_DRST bite drains Str): poisonous corpse but also confers poison resistance (MR_POISON in both mresists and mconveys columns at monsters.h WATER_MOCCASIN row). Eating risks 1d4 Str + 1d15 HP on the 1-in-5 poison roll without resistance (eat.c:1928-1936); ~1-in-15 conferred-resistance grant per successful eat.
-->


迷宮には何百種ものモンスターが生息しており、アルファベットの文字で表される分類（クラス）に体系化されています。小文字は一般に小型または危険度の低いモンスターを示し、大文字はより大型または危険なモンスターを示します。さらに文字の色によって、同一分類内の個別の種が区別されます。

ここでは、各文字が何を意味するのか、おおむね序盤に出現する順に沿って手短に解説します。全モンスターの詳細なレベル、速度、AC、攻撃能力のデータについては、巻末の [モンスター図鑑 (Bestiary Tables)](#bestiary-tables) を参照してください。

#### 序盤によく遭遇するモンスター (Common Early Encounters)

| 記号   | 分類                   | 備考                                                                       |
| ------ | ---------------------- | -------------------------------------------------------------------------- |
| [`a`](#ants-and-insects-a)    | [蟻と昆虫類 (Ants)](#ants-and-insects-a)      | 兵隊蟻は序盤の頻出キラーです：速度18、1ターンに2回攻撃（噛みつき＋筋力を低下させる毒針）を行い、群れで移動します。殺人蜂、巨大蟻、火蟻も同様に警戒すべき脅威です。 |
| [`b`](#blobs-b)    | [ブロブ (Blobs)](#blobs-b)     | 酸性またはゼラチン状の軟体生物です。酸のブロブはこちらから能動的に攻撃してくることはありません。*こちらが* 攻撃を *当てた* ときにのみ、1d8の酸の飛沫を浴びせ、武器を腐食させる恐れがあります。遠距離から倒しましょう。死体を食べれば [耐性](#useful-corpse-effects) が得られます。 |
| [`B`](#bats-and-birds-b)    | [コウモリと鳥類 (Bats)](#bats-and-birds-b)      | その俊敏さが最大の脅威です。コウモリや巨大コウモリは基本速度12のプレイヤーに対して速度22で動くため、プレイヤーが1回攻撃を振る間にほぼ2回噛みついてきます。巨大コウモリの1d6の噛みつきは駆け出しのキャラクターをあっという間に消耗させます。吸血コウモリは筋力を低下させる噛みつきも併せ持ちます。 |
| [`d`](#dogs-and-canines-d)    | [犬とイヌ科動物 (Dogs and other canines)](#dogs-and-canines-d) | ジャッカルの噛みつきダメージは1d2に過ぎませんが、地下数階層においてはその群れが他のどの脅威よりも多くの冒険者を葬っています。狐の噛みつきは1d3でより素早いですが、単独で出現します。飼い慣らした犬や猫は他のあらゆる敵との戦いで頼もしい助けになります。 |
| [`e`](#eyes-and-spheres-e)    | [目と球体 (Eyes)](#eyes-and-spheres-e)      | **さまよう目** を近接攻撃で殴ると麻痺してしまいます。飛び道具を使うか、戦わずに迂回しましょう。包子ガスは倒すと爆発して4d6のダメージを与えるため、必ず2マス以上離れて撃ちましょう。炎の球体、氷の球体、電撃の球体も近距離で爆発します。 |
| [`f`](#felines-f)    | [ネコ科動物 (Cats)](#felines-f)      | 犬と同様に、初期のペットとしてよく選ばれます。家猫は腐肉（トリップミート）で飼い慣らすことができますが、野生のネコ科動物を従わせるには魔法が必要です。 |
| [`G`](#gnomes-g)    | [ノーム (Gnomes)](#gnomes-g)    | 鉱山に無数に出現します。ノームやドワーフのプレイヤーに対してはほとんどが友好的です。領主や王はより強力ですが、特別な対処法は必要ありません。 |
| [`h`](#humanoids-h)    | [人型生物 (Humanoids)](#humanoids-h) | ドワーフ、バグベア、マインドフレイヤなどです。つるはし（mattock）を持ったドワーフは1d8＋1d12の一撃を繰り出し、レベル1のキャラクターなら2振りで撲殺されます。遠距離から対処しましょう。 |
| [`i`](#imps-and-minor-demons-i)    | [インプと小悪魔 (Imps)](#imps-and-minor-demons-i)      | ほとんどは軽微な厄介者に過ぎませんが、ホムンクルスの噛みつきはプレイヤーを眠らせてしまいます。睡眠耐性がない場合は、遠距離から倒してください。 |
| [`j`](#jellies-j)    | [ゼリー (Jellies)](#jellies-j)   | 移動しません。横を通り抜けて迂回しましょう。近接攻撃を仕掛けると受動的な酸ダメージを受けることがあります。 |
| [`k`](#kobolds-k)    | [コボルド (Kobolds)](#kobolds-k)   | 非力ですが、すべてのコボルドの死体には毒があります。ごく稀に毒矢を持っている個体がいます。 |
| [`o`](#orcs-o)    | [オーク (Orcs)](#orcs-o)      | 数が多く、1対1なら手頃な強さですが、集団になると危険です。迷宮上層では丘オークとモルドールオークが代表的な変種です。 |
| [`r`](#rodents-r)    | [げっ歯類 (Rodents)](#rodents-r)   | ネズミや岩モグラです。岩モグラは金属製のアイテムを食べるため、装備を守りましょう。 |
| [`s`](#arachnids-and-centipedes-s)    | [蜘蛛とムカデ (Spiders)](#arachnids-and-centipedes-s)   | 洞窟グモは弱いです（毒耐性を得るために食べましょう）。巨大グモは毒を持ちます。 |
| [`x`](#xans-and-fantastic-insects-x)    | [グリッドバグと幻虫 (Grid bugs)](#xans-and-fantastic-insects-x) | ゲーム中で最弱のモンスターです。斜め移動すらできません。死体は残りません。また `x` 分類には、ずっと深い階層に現れる **ザン** も含まれ、その針で刺されると足を不自由にされます（治癒するまで移動速度が大幅に低下します）。 |
| [`:`](#lizards)    | [トカゲ類 (Lizards)](#lizards)   | イモリ、ヤモリ、イグアナは単体では非力です。この分類の重要性は主にその死体にあります。**トカゲの死体は [石化 (petrification)](#petrification-stoning) を治療します**（コカトリス保険として常に1つ携帯しましょう）。また、イモリの死体はMP（魔力）を1〜3回復させることがあります。 |

#### 中層の脅威 (Mid-Dungeon Threats)

| 記号   | 分類              | 備考                                                                                                 |
| ------ | ----------------- | ---------------------------------------------------------------------------------------------------- |
| [`A`](#angelic-beings-a)    | [天使系 (Angels)](#angelic-beings-a)            | 強力で、通常は属性を持ちます。自分の信仰神と同じ属性の天使とは戦ってはいけません。 |
| [`C`](#centaurs-c)    | [ケンタウロス (Centaurs)](#centaurs-c)          | 高速（速度18〜20）です。半数が弓またはクロスボウを持って生成されますが、近接戦に持ち込んでも武器攻撃と蹴りを繰り出してきます。山のケンタウロスの打撃が最も強烈で、1ターンに1d10の武器攻撃に加えて *2回* の1d6蹴りを放ちます。 |
| [`E`](#elementals-e)    | [エレメンタル (Elementals)](#elementals-e)        | 倒すのが困難です。風のエレメンタルは [丸呑み](#engulfment) し、土のエレメンタルは壁をすり抜けて移動します。 |
| [`f`](#felines-f)    | [ディスプレイサービースト (Displacer beast)](#felines-f)   | 猫（ネコ科）分類ですが極めて狂暴です：AC −10を誇り、痛烈な3回連続近接攻撃を仕掛けてきます。死体を食べると一時的に内在能力「幻影（変位）」が得られます。 |
| [`F`](#fungi-and-molds-f)    | [菌類とモールド (Fungi)](#fungi-and-molds-f)             | モールドは移動しないため、迂回して通り過ぎましょう。シュリーカーは他のモンスターを呼び寄せます。 |
| [`g`](#gremlins-g)    | [グレムリンとガーゴイル (Gremlins / gargoyles)](#gremlins-g)   | 重い鉤爪に加えて特殊能力を持ちます。グレムリンは **夜間に攻撃が当たるとランダムに内在能力を1つ奪い**、**水に濡れると分裂・増殖します**（絶対に泉の中へ蹴り飛ばしてはいけません）。ガーゴイルは鈍足ですが重装甲（AC −4）で3連撃を繰り出します。翼のあるガーゴイルは飛行します。 |
| [`'`](#golems)    | [ゴーレム (Golems)](#golems)            | 人造の怪物です。鉄のゴーレムは強打を放ち、ほぼすべての攻撃に耐性を持ちます。粘土、石、木のゴーレムはそれよりも柔らかいです。ガラスのゴーレムは倒すと宝石をドロップします。 |
| [`H`](#giant-humanoids-h)    | [巨人 (Giants)](#giant-humanoids-h)            | 強烈な近接打撃を放ち、巨石を投げ、宝石を所持しています。死体を食べると筋力を上昇させることがあります。 |
| [`J`](#jabberwocks-j)    | [ジャバウォック (Jabberwock)](#jabberwocks-j)        | 1ターンに4回の2d10攻撃を行い、全段命中すると約44もの大ダメージを受けます。 |
| [`K`](#keystone-kops-k)    | [キーストン・コップ (Keystone Kops)](#keystone-kops-k)     | 店主が呼び出す警官隊です。万引き、代金未払い、あるいは店主を怒らせたときに出現します。1体1体は非力ですが大群で押し寄せ、あなたをあざ笑います。 |
| [`l`](#leprechauns-l)    | [レプラコーン (Leprechauns)](#leprechauns-l)       | ゴールドを盗んでテレポートで逃走します。たった1回の鉤爪攻撃で所持金の *全額* を奪われることもあります。ゴールドを袋の中に隠すか、別の場所に置いておくか、遠距離から倒しましょう。 |
| [`L`](#liches-l)    | [リッチ (Liches)](#liches-l)            | 呪文の使い手です。アーチリッチは死の指（即死の接触呪文）を唱えてくるため、ゲーム中で最も危険なモンスターの1つです。 |
| [`m`](#mimics-m)    | [ミミック (Mimics)](#mimics-m)            | アイテム、壁、扉、泉、祭壇、あるいは巨石に擬態しています。[ミミックに関する注意点 (A note on mimics)](#a-note-on-mimics) を参照してください。 |
| [`M`](#mummies-m)    | [ミイラ (Mummies)](#mummies-m)           | 物理的な鉤爪攻撃を繰り出す好戦的なアンデッドです。元の種族の腐った死体を残しますが、老化効果はありません。クロークとして身につけた「ミイラの包帯」は透明状態を遮断するため、店主が接客を拒否してきた際に役立ちます。 |
| [`n`](#nymphs-n)    | [ニンフ (Nymphs)](#nymphs-n)            | [インベントリからアイテムを盗み、テレポートで逃走します](#a-note-on-nymphs)。遠距離から戦いましょう。 |
| [`N`](#nagas-n)    | [ナガ (Nagas)](#nagas-n)             | 大型の蛇の体を持つ怪物です。赤ナガは火炎の息を吐き、黒ナガは酸を吐き、金ナガは呪文を唱え、番人ナガは筋力を低下させる毒を吐き、麻痺させる噛みつきを行います。タフで速度は12〜16です。 |
| [`O`](#ogres-o)    | [オーガ (Ogres)](#ogres-o)             | 迷宮上層における強打者であり、集団で移動します。オーガの君主やオーガの王はさらに強力な打撃を与えてきます。包囲されないように注意してください。 |
| [`p`](#piercers-p)    | [ピアサー (Piercers)](#piercers-p)          | 鍾乳石に擬態し、天井から落下して2d6ダメージ（鉄のピアサーは3d6、ガラスのピアサーは4d6）を与えてきます。硬い兜をかぶっていれば一撃を防げます。ACが優れていれば回避できることもあります。 |
| [`P`](#puddings-and-oozes-p)    | [プリンとウーズ (Puddings)](#puddings-and-oozes-p)          | [黒プリンや茶色プリンは、鉄製または金属製の武器で近接攻撃を受けると分裂します](#a-note-on-puddings)（メスやツルギも金属製に含まれます）。死体を食べて [内在能力](#useful-corpse-effects) を得るのに適しています。 |
| [`q`](#quadrupeds-q)    | [四足獣 (Quadrupeds)](#quadrupeds-q)        | 中盤に現れる連続攻撃の巨獣たちです。**ロゼ** は特に有名で（鈍足の速度9ですが1ターンに3回攻撃を行い、群れをなすと極めて危険です）、ムーマクは単独で強烈な2段攻撃を繰り出す巨獣です（4d12の突き刺し＋2d6の噛みつき）。 |
| [`R`](#rust-monsters-and-disenchanters-r)    | [錆の怪物 (Rust monster)](#rust-monsters-and-disenchanters-r) | 錆の怪物の攻撃を受けると装備中の鉄の鎧が腐食し、こちらが攻撃を当てると手に持った鉄の武器が腐食します。ミスリル製、銀製、木製の武具を使うか、戦う前に鉄製装備を脱ぎましょう。吸魔の怪物はゲヘナにのみ出現します。[強化値ドレイン (Enchantment Drain)](#enchantment-drain) を参照してください。 |
| [`S`](#snakes-s)    | [ヘビ (Snakes)](#snakes-s)            | コブラやクサリヘビは毒を持ちます。水ヘビは泉から飛び出してきます。 |
| [`t`](#trappers-and-lurkers-t)    | [トラッパーとラーカー (Trappers / lurkers above)](#trappers-and-lurkers-t) | 床や天井に完全に同化して潜み、その上を踏むか下を歩いたときに [丸呑み](#engulfment) してきます。 |
| [`T`](#trolls-t)    | [トロール (Trolls)](#trolls-t)            | [急速再生能力を持ちます。死体を食べるか缶詰にしない限り、死から復活します](#a-note-on-trolls)。 |
| [`u`](#unicorns-and-horses-u)    | [馬とユニコーン (Horses / unicorns)](#unicorns-and-horses-u) | 野生の馬は敵対して出現しますが、飼い慣らして乗馬することができます。ユニコーンの色は属性を表します：自分と同じ属性の個体は友好的に生成されます。敵対的なユニコーンには宝石を投げましょう。[幸運と運命 (Luck and Fortune)](#luck-and-fortune) を参照してください。 |
| [`U`](#umber-hulks-u)    | [アンバーハルク (Umber hulk)](#umber-hulks-u)        | 視界に捉えるだけで、その凝視により混乱させられます。目隠しをすれば凝視を無効化できます。 |
| [`v`](#vortices-v)    | [渦 (Vortices)](#vortices-v)          | 高速で [丸呑み](#engulfment) してくる雲のような怪物です（足の遅い霧の雲を除く）。ほこりの渦は盲目を引き起こし、氷の渦は凍結させ、エネルギーの渦は電撃を与えて魔力を吸い取り、蒸気の渦と炎の渦は火傷を負わせます。遠距離から倒しましょう。 |
| [`w`](#worms-w)    | [ワーム (Worms)](#worms-w)             | 長いワームは移動するにつれて尾の節が伸びていき、それ自体が通路を塞ぐ一本の障害物になります。 |
| [`W`](#wraiths-w)    | [レイス (Wraiths)](#wraiths-w)           | [攻撃を受けるとレベルを吸い取られます（レベルドレイン）](#level-drain)。しかし [その死体を食べるとレベルが上がります](#a-note-on-wraiths)。腐敗する前に新鮮なうちに食べましょう。 |
| [`y`](#lights-y)    | [黄色い光と黒い光 (Yellow/black lights)](#lights-y) | 隣接すると自爆します。黄色い光は盲目を引き起こし、黒い光は幻覚をもたらします。黒い光は「不可視の視覚」がないと目に見えません。遠距離から撃破しましょう。 |
| [`Y`](#apelike-creatures-y)    | [イエティ (Yetis)](#apelike-creatures-y)             | 白くて巨大な野獣です。イエティの死体を食べると、約1/3の確率で冷気耐性が得られます。 |
| [`z`](#zruties-z)    | [ズルティ (Zruty)](#zruties-z)             | 動きは遅いですが、毎ターン2回の3d4鉤爪攻撃と3d6の噛みつきを繰り出してきます。 |
| [`Z`](#zombies-z)    | [ゾンビ (Zombies)](#zombies-z)           | 鈍足で数が多いです。死者退散（アンデッドの退散）の杖や呪文を使うと1d8ダメージを与えて逃走させることができます。種族ベースのゾンビは、その基礎種族のすでに腐敗した死体をドロップします。 |

#### 極めて危険なモンスター (Very Dangerous Monsters)

| 記号   | 分類             | 備考                                                                                                     |
| ------ | ---------------- | -------------------------------------------------------------------------------------------------------- |
| [`c`](#cockatrices-c)    | [コカトリス (Cockatrices)](#cockatrices-c)      | **接触＝[即座に石化 (instant petrification)](#petrification-stoning)。** 素手で殴ることは絶対に避けてください。手袋をはめた状態でその死体を持てば、凶悪な武器として振るうことができます。 |
| [`D`](#dragons-d)    | [ドラゴン (Dragons)](#dragons-d)          | [色ごとに固有のブレス攻撃、耐性、および鱗鎧の特性を持ちます](#a-note-on-dragons)。下記の注記を参照してください。 |
| [`h`](#humanoids-h)    | [マインドフレイヤ (Mind flayers)](#humanoids-h)     | [攻撃が命中するたびに知力を吸い取られます（知能喪失）](#brainlessness)。**知力が3の状態で次の触手攻撃を受けると即死します。** 兜をかぶっていれば触手攻撃の7/8を防ぐことができます。必ず遠距離から倒しましょう。 |
| [`V`](#vampires-v)    | [吸血鬼 (Vampires)](#vampires-v)         | [レベルを吸い取ってきます（レベルドレイン）](#level-drain)。吸血鬼の貴族（吸血鬼の領主）は飛行し、高速で動きます。 |
| [`w`](#worms-w)    | [紫ワーム (Purple worms)](#worms-w)     | 超巨大なワームです：[命中すると丸呑みされ、体内で消化されます](#engulfment)。内側から刃物で切り裂いて脱出しましょう。 |
| [`X`](#xorns-x)    | [ゾーン (Xorn)](#xorns-x)             | 壁をすり抜けて移動します。毎ターン3回の鉤爪攻撃と1回の噛みつきを放ち、待ち伏せも逃亡も困難です。 |
| [`;`](#sea-monsters)    | [海の怪物 (Sea monsters)](#sea-monsters)     | [溺死は即死です](#drowning)。確実な対策（計画）がないまま水中で戦ってはいけません。 |
| [`&`](#major-demons)    | [悪魔 (Demons)](#major-demons)           | 上位の悪魔（オルクス、デモゴルゴン、アスモデウスなど）はボス級の脅威です。 |
| [`@`](#humans-and-elves)    | [人間（敵対的） (Humans (hostile))](#humans-and-elves) | ゲーム中最も執拗で厄介な敵である「イェンダーの魔法使い」が含まれます。 |
| [`Q`](#quantum-mechanics-q)    | [量子物理学者と遺伝子工学者 (Quantum mechanics / genetic engineers)](#quantum-mechanics-q) | 量子物理学者は攻撃が命中した対象をテレポートさせ、遺伝子工学者（5.0で新登場）は対象を変身（ポリモーフ）させます。 |

#### 特殊な記号 (Special Symbols)

マップ上の表示の中には、一般的な意味でのモンスターではないものの、画面上に出現しその意味を把握しておくべき記号がいくつか存在します。

| 記号   | 対象                     | 備考                                                                                                 |
| ------ | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| `I`    | 不可視モンスターの目印   | 目に見えない何かを最後に感知した位置をゲームが記憶しています。あなたがぶつかるかそのマスを踏むまで `I` は表示され続けますが、通常そのモンスターはすでに別の場所へ移動しています。 |
| `~`    | 長いワームの尾の節       | 長いワームの体の一部です。尾を攻撃するとワーム本体にダメージが入り、尾の連なりが短くなります。頭部（`w`）を攻撃すると通常の近接戦闘になります。 |
| `]`    | 奇妙な物体               | **常に [ミミック](#a-note-on-mimics) です。** 通常のアイテムが `]` と表示されることは決してありません（防具の `[` の鏡像です）。 |
| `⎕`<br>`\newline`{=latex}(スペース) | 亡霊                     | 骨ファイル（過去の冒険者の亡骸）から生成された亡霊です。この記号は文字通りの半角スペースであり、下の床を上書きして塗りつぶします：部屋の中では、本来 `.` があるべき床に1マス分の *空白（隙間）* として現れます。その空白マスに踏み込むことで正体を確認できます。 |

---

### 注目の施設・地形 (Points of Interest)


<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Throne positive-Luck kick gives 300-500 gold, not 201-500: rn1(201,300)=rn2(201)+300 (dokick.c:1036; rn1 macro hack.h:1543).
- Verified correct: magic fountain 1/7 restore-all+1, water demon 1/30 & wish-gate, Excalibur dip, altar BUC flashes, all throne effects, the full 28-ring sink table & 19/20 loss, sink kick/quaff/dip tables, vault-guard timer.
-->
<!-- audit
2026-05-22 fountains fact-check:
- magic-fountain placement: mklev.c:2297 mkfountain() rolls !rn2(7) — 1/7 of *randomly placed* fountains; predefined fountains via lua des.feature("fountain",x,y) call lspo_feature (sp_lev.c:4904) which sets FOUNTAIN typ + looted/warned only, never blessedftn — so Minetown, Mine's End, Oracle, Big Room (bigrm-4), Castle, Juiblex's swamp are never magic
- magic-fountain gate: mgkftn && u.uluck >= 0 && fate >= 10 (fountain.c:254); fires on 21/30 quaffs at Luck ≥ 0; "Wow! This makes you feel great!" at fountain.c:257; AMAX restore loop fountain.c:259-263; +1 attr 264-272; flag consumed at fountain.c:275
- sink-kicked fountain blessedftn=0 explicit (do.c:421)
- dipfountain has no blessedftn check; dryup() at fountain.c:232 clears it — dipping a magic fountain can waste the charge if the fountain dries
- curse-some-items (case 24, "This water's no good!"): iterates gi.invent only (fountain.c:312-320), so container contents (bag interior) are safe
- poisonous water (case 21, "The water is contaminated!"): poison_strdmg if no Poison_resistance else losehp(rnd(4),"unrefrigerated sip of juice") (fountain.c:300-307)
- scare-monsters (case 29, "bad breath"): iterates fmon entire-level, monflee each (fountain.c:367-381)
- water demon 1 in 30 (case 23); wish gate rnd(100) > 80 + level_difficulty() (fountain.c:78); level_difficulty in DoD == depth(&u.uz) (dungeon.c:2027); at DL ≥ 20, threshold 100, rnd(100) never > 100, so 0% wish
- Elbereth scares water demons in DoD: onscary excludes only Rodney/lawful-minions/Angels/Riders (monmove.c:243-271); Elbereth disabled in Gehennom/Planes (Inhell || In_endgame, monmove.c:295-302); musical instruments use the auditory_scare=(x=0,y=0) path which BYPASSES the Inhell/In_endgame check (works in Gehennom)
- Wizard random starting items: u_init.c:167-178 has 3 random scrolls (may roll SCR_TAMING) and 1 random spellbook (may roll SPE_CHARM_MONSTER); Wizards do NOT roll random tools so cannot start with magic harp / tooled horn / leather drum
- strategy refs:
  + https://nethackwiki.com/wiki/Fountain — general mechanics; never-magic-fountain list
  + https://nethackwiki.com/wiki/Talk:Water_demon — "double-Elbereth" survival strategy (~97.95% survivable per wiki claim)
  + https://nethackwiki.com/wiki/Fountain_quaffing — early-game wish-fishing strategy, risk discussion
  + http://www.chiark.greenend.org.uk/~damerell/games/magicfountain.txt — Damerell statistical defense; drop items on the fountain tile to avoid make-pool curse; sack interior protected
  + https://www.steelypips.org/nethack/331/foun-331.html — Steelypips fountain spoiler

2026-05-18:
- Fountain quaff: 7 case branches in rnd(30) (fountain.c:286-387)
- Water demon spawn rate: 1 in 30 quaffs (fountain.c:247, 314)
- Shallow wish odds: water demon × rnd(100) > 80 + level_difficulty() ≈ 1/150 (fountain.c:78, 247)
- Wish odds drop to zero past DL 20 (fountain.c:78 level_difficulty term)
- Excalibur dip: lawful + XL ≥ 5 + long sword + quan=1, 1/6 Knight or 1/30 other (fountain.c:404-405)
- Non-lawful Excalibur dip curses the sword and consumes the fountain (fountain.c:411-424)
- Fountain dip cases 17-20 UNCURSE the dipped item (NOT bless) (fountain.c:464-475)
- Altar BUC flash: amber=blessed, black=cursed, no flash=uncursed (do.c:379-389)
- Altar conversion via cross-race sacrifice can flip the altar (pray.c:1717-1736)
- Throne trigger: rnd(6) > 4 = 1 in 3 chance of any effect (sit.c:45)
- Throne effect chosen from rnd(13) outcomes (sit.c:46, 68-209)
- Throne wish (case 6) requires u.uluck + rn2(5) ≥ 0, i.e. non-negative Luck (sit.c:106-110)
- Throne ID: identify_pack(rn2(5)) — 4/5 chance of 1-4 items, 1/5 chance of entire pack (sit.c:198, invent.c:2721)
- Throne can vanish "in a puff of logic" on rn2(3), even when nothing happens (sit.c:224-233)
- Vlad's throne: cases 1-4 grant wish + destroy throne; 5-13 are negatives (sit.c:241-353)
- Kicking sink: 4/5 klunk, else 1/3 black pudding, 1/3 amorous demon, 1/3 ring backup (dokick.c:1201-1238)
- Each kick outcome gated by S_LPUDDING / S_LDWASHER / S_LRING (once per sink) (dokick.c:1209-1232)
- Dip potion of polymorph: sink → fountain/throne/altar/grave (do.c:404-454)
- Grave case may fail and print "The sink vanishes." (engrave.c:1691-1693)
- Dip POT_OBJECT_DETECTION: "You sense a ring lost down the drain" while S_LRING unset (fountain.c:771-776)
- Dip POT_LEVITATION: drops a ring once per sink (fountain.c:767-770, 804-826)
- Dip POT_ACID: "The drain seems less clogged" (fountain.c:755-766)
- Drop ring in sink: searching + slow-digestion are returned to inventory; all others consumed (do.c:507-516)
- Ring of hunger vanishes ALL items on the sink square (do.c:556-570)
- Ring of teleportation moves the sink to a fresh ROOM tile (do.c:575-580)
- Rotten food in fountains is slime molds, not fruit (objnam.c:414-427)
- VAULT_GUARD_TIME = 30 turns (hack.h:69) before the guard appears; "Croesus", "Kroisos", "Creosote" all dismiss the guard if Croesus is still alive (vault.c:513-543); lying with a Lawful character loses one alignment (vault.c:507-511)
2026-05-31:
- Real-name answer: guard demands "Please drop that gold and follow me." then opens a temporary corridor in the wall (the fake-corridor system in vault.c), leads the player out, and re-seals the wall behind. Player loses all carried gold (vault.c:551-585).
- Croesus answer (with Croesus alive): guard says "Oh, yes, of course. Sorry to have disturbed you." and `mongone(guard)` removes him (vault.c:513-543). No corridor opens. Player keeps gold but stays sealed inside.
- Croesus answer with Croesus dead: guard goes hostile and attacks (vault.c:525-540).
- Implication: lying keeps the gold but requires the player to have an independent way out (wand of digging, scroll of teleportation, level teleport, etc.). Truth-telling guarantees escape at the cost of the gold.

地下深くへと潜っていく中で、特別なランドマーク（固定施設）に立ち寄る時間を作りましょう。フロアの随所に散らばるこれらの建造物は、好奇心旺盛な探索者に多大な報酬を与え、時には手痛い罰を下します。

#### 泉 (Fountains) `{`

ああ、泉。その穏やかなせせらぎの音は、冷たく心地よい喉の潤いを約束しながら、どんな罠よりも多くの冒険者を破滅へと誘惑してきました。

ランダムに配置された泉のうち、幸運（Luck）の値にかかわらず約1/7の確率で **魔法の泉 (magic fountain)** が存在します。飲むまで普通の泉と見分けはつきません。幸運が0以上（非負）の状態で魔法の水を飲むと、*「おお！ 素晴らしい気分だ！ (Wow! This makes you feel great!)」* と表示され、すべての能力値が最大値まで回復した上で、全能力値が1ずつ上昇します。これにより泉の魔法の力は消費されます。（鉱山街や [賢者 (Oracle)](#the-oracle) のあるフロアにあらかじめ配置されている固定の泉や、他の地形から生成された泉が魔法の泉になることは決してありません。また、浸す行為では魔法の泉の恩恵は得られませんが、魔法の力を消費してしまう可能性があります。）

**普通の泉から水を飲むこと (Quaffing)** は、以下のような数十種類ものランダム効果を秘めた危険なスロットマシンのようなものです：

| 結果              | 効果                                                  |
| ----------------- | ----------------------------------------------------- |
| 水の魔神          | 水の魔神が出現し、敵対します                          |
| 水のニンフ        | **水のニンフ** が出現し、アイテムを盗もうとします     |
| 水ヘビ            | ヘビの大群（水ヘビ）が出現します                      |
| アイテムの呪い    | 「この水はまずい！ (This water's no good!)」（メインインベントリ内のアイテムが呪われることがあります。袋の中に入れたアイテムは安全です） |
| 毒の水            | 「水が汚染されている！ (The water is contaminated!)」 筋力ダメージを受けます（毒耐性があれば最悪の事態を防げます） |
| 不可視の視覚      | 目に見えない生物を視認する能力（透明視）を得ます      |
| モンスター感知    | フロア内の全モンスターが一瞬だけ表示されます          |
| 自己知識          | 自身の現在の状態（内在能力等）が手短に表示されます    |
| モンスター恐怖    | ひどい口臭を放ち、フロア内の全モンスターがパニックになって逃走します |
| 何も起きない      | 「冷たい水に喉の渇きがいやされた。(The cool draught refreshes you.)」または「このぬるま湯には味がない。(This tepid water is tasteless.)」 |

ほとんどの場合は何も起きません。魔神が出現する確率は約1/30です。浅い階層では攻撃してくる代わりに願いを叶えてくれることがあり、これは水を飲む試行約150回につき1回の願いに相当しますが、地下20階を過ぎると願いの確率はゼロになります。このリスクを冒すなら：アイテムを袋の中に退避させ（呪い対策）、[エルベレス (Elbereth)](#elbereth) を地面に刻み（魔神が間合いを取ります）、魔神が現れた場合に備えてモンスター魅了や恐怖の効果を用意しておきましょう。

**泉にアイテムを浸すこと (Dipping)** は、秩序（Lawful）のキャラクターが名剣エクスカリバーを入手するための手段です。経験レベル（XL）が5以上であれば、長剣を泉に浸すことでダンジョン屈指の名剣 [エクスカリバー (Excalibur)](#excalibur-artifact) へと変化する可能性があります。騎士なら1回の浸漬につき1/6という破格の高確率で成功し、他の役職では1/30の低確率となります。それ以外の場合、浸すことで装備が錆びたり、敵対的な水棲生物を呼び出したり、あるいは稀に浸したアイテムの呪いが解けたり（解呪）します。

レベル5に達した秩序の騎士が長剣を持っているなら、エクスカリバーが出るまであらゆる泉に浸すべきです。1回浸すごとに約1/3の確率で泉が干上がってしまうため、1つの泉だけで成功することは稀です。その過程で長剣が錆びても心配いりません。剣がエクスカリバーへと変貌した瞬間、それまでの錆は完全に消え去り、刀身は永久に錆耐性（防錆）を得ます。注意点が2つあります：鉱山街の泉には手を出さないでください。町の泉を干上がらせると警備員隊に襲われます。また、秩序以外の属性のキャラクターは絶対に浸してはいけません。湖の乙女は剣を呪うだけです。他の秩序の役職でも試す価値はありますが、確率1/30ですので相当の忍耐力が必要です。

#### 祭壇 (Altars) `_`

祭壇は清められた石造りの聖壇で、マップ上では `_` と表示され、3つの神のいずれかの属性に属しています。手に入れた装備品を祭壇の上に置くことで、祝福されているか呪われているかを一目で判別でき、新鮮な死体を捧げることで信仰する神の寵愛を得ることができます。

**祭壇にアイテムを置く（ドロップする）こと**（1個なら `d`、複数を一度に置くなら `D`）で、アイテムのBUC状態（祝福・非呪・呪縛）が瞬時に判明します。**琥珀色の閃光** → 祝福。**閃光なし** → 非呪（呪われていない）。**黒い閃光** → 呪縛（呪われている）。

これには何のコストもかからず、回数制限もありません。そのため、身元不明の装備品を手に入れたら、実際に装備する前に最初に見つけた祭壇まで運んで確認しましょう。（山のようにまとめて一度にドロップすれば、アイテム1個につき1回ずつ閃光が表示されます。）

**祭壇でモンスターの死体を捧げること（生贄）**（祭壇の上に立ち `#offer`）は、あなたの神の寵愛を得る手段です。古びて傷んだ死体は何の効果も生みません。新鮮で強力なモンスターの死体ほど高い価値を持ちます。十分な生贄を捧げると、神はあなたの主義・属性に合致したアーティファクト武器をご褒美として授けてくれることがあります。初期ペットを生贄にしてはいけません。属性値の大幅な低下を招き、モンスターを怒らせて引き寄せる不吉な内在能力がゲーム終了まで消えずに残ってしまいます。神学に関する全容は [神との関係 (Divine Relations)](#divine-relations) を参照してください。

**祭壇の改宗（属性変換）** は極めてリスクが高いため、仕組みを正しく把握しておく必要があります。属性値が0以上（非負）であれば、異属性の死体を捧げることで祭壇の属性を反転（改宗）させるか、幸運が1低下します。どちらの結果でも敵対的な神の使いが召喚されることがあります。属性値がマイナスの場合、祭壇は逆に *あなた自身* の属性を強制的に変えてしまいます。試みる前に [祭壇と属性 (Altars and Alignment)](#altars-and-alignment) を熟読してください。

#### 玉座 (Thrones) `\`

玉座は華麗な王の座席で、記号 `\` で表され、専用の部屋に時折現れます。玉座に座る（`#sit`）ことは、迷宮における最も純粋なギャンブルです。起こりうる結果の一覧は、まるで願いのリストと暗殺命令書を混ぜ合わせたような内容です：

- 願い（幸運が0以上であれば確実に叶います）
- 1種類のモンスターの虐殺（ジェノサイド）
- 手持ちのアイテム1〜4個（1/5の確率で全インベントリ）の無料識別
- 能力値の上昇、または能力値の低下
- 感電（電撃ショック）
- 全回復
- あなたを楽しませるために召喚された、敵対的モンスターの群れ
- 混乱
- 最大6個の所持アイテムへの呪い（幸運がプラスの場合は、代わりに長時間の盲目と幸運の低下）
- そのフロアの地図化（マジックマッピング）
- [不可視の視覚 (See invisible)](#senses-and-perception)
- 所持ゴールドの全消失
- テレポート（幸運が悪いと、代わりにフロア中の全モンスターが覚醒）

約1/3の確率で何かが起こりますが、帳簿のどちら側の欄が適用されるかは事前にはわかりません。この表の最悪の行に直面しても生き延びられる実力がついてから座るようにしましょう。幸運が-1でも願いが出る可能性はありますが、非負（0以上）であれば願いの目が引かれた際に確実に好ましい結果が得られます。たとえ何も起きなくても、玉座は理屈の煙（a puff of logic）とともに消滅してしまうことがあるため、何度も試せることもあれば一度きりで消えることもあります。（ヴラドの塔にあるヴラドの玉座は特別で、最初に願いを叶えるまでは決して消滅しません。）玉座を蹴る（キックする）のはまた別の賭けです。玉座1つにつき1回限り、1/3の確率で300〜500ゴールドと最大6個の宝石が転がり出ます。失敗したキックのうち1/4は、落とし扉から下の階へ落とされます。
<!-- Throne mechanics: src/sit.c throne_sit_effect(), rnd(6)>4 for 1/3
     activation, rnd(13) for effect, !rn2(3) for vanishing.
     Vlad's throne: special_throne_effect(), cases 1-4 grant wish and
     destroy throne, cases 5-13 are negative but throne survives. -->

#### 流し台 (Sinks) `{`

ことわざに「流し台（キッチンのシンク）以外は何でも揃っている」と言いますが、恐怖の迷宮（Mazes of Menace）にはキッチンの流し台まで存在します。マップ上では白い `{` で表示され、便利な設備というよりは多彩な危険物と言えます。蹴る、飲む、物を投げ入れるといったアクションが可能で、いくつかの小技は実を結びますが、大半は無駄に終わり、中には命に関わる被害をもたらすものもあります。

**流し台を蹴ること（キック）** は、通常は無害な *ゴツン！ (Klunk!)* という音を立てるだけです。5回のうち4回は何も起きません。成功すると指輪が転がり落ちてくるか、[黒プリン (black pudding)](#a-note-on-puddings)（危険ですが、その肉片は [3重の耐性を得られる軽食](#useful-corpse-effects) になります）が這い出してくるか、「皿洗い」を装った *情熱的な悪魔*（[誘惑遭遇](#seduction) と同じインキュバス／サキュバス）が呼び出されるか、あるいは単に足の指をぶつけて痛めるだけです。足の指をぶつける以外の結果は、1つの流し台につき最大1回しか発生しません。這い出してきたものを何であれ返り討ちにできる自信がある場合に限り、序盤に試す価値があります。

**流し台に指輪を落とすこと** は、指輪の種類に応じた固有のメッセージを表示します。全28種類の指輪それぞれに専用のメッセージが割り当てられており、下記の表で解読できます。「探索の指輪」と「消化不良の指輪」は落としても即座に手元に戻ってきます。その他の指輪は、1/20の確率で手元に戻り、戻らなかったもののうち1/5は流し台の下の床に埋まり（つるはしで掘り出せます）、残りは完全に下水へ消え去ります。この方法は、余分なスペアの指輪がある場合や、餓死寸前で未知の指輪が「消化不良の指輪」であることに賭けたい場合に最も役立ちます。それ以外の用途であれば、価格識別、祭壇でのBUC判定、識別の巻物を使った方が指輪を失わずに確実に判明させられます。

| メッセージ                                           | 該当する指輪 (Ring)   | 指輪は残るか？ |
|------------------------------------------------------|-----------------------|----------------|
| *"You thought your ring got lost in the sink, but there it is!"*<br>（指輪を流し台に落としたと思ったが、そこにあった！） | 探索の指輪 (searching) | **残る**       |
| *"The ring is regurgitated!"*<br>（指輪が逆流して吐き出された！） | 消化不良の指輪 (slow digestion) | **残る**       |
| *"The sink quivers upward for a moment."*<br>（流し台が一瞬上に向かって震えた。） | 浮遊の指輪 (levitation) | 失われる       |
| *"You smell rotten slime molds."* (または設定した果物)<br>（腐ったスライムモールドの臭いがする。） | 耐毒の指輪 (poison resistance) | 失われる       |
| *"Several flies buzz angrily around the sink."*<br>（何匹かのハエが流し台の周りを怒ったように飛び回っている。） | 反感の指輪 (aggravate monster) | 失われる       |
| *"Static electricity surrounds the sink."*<br>（静電気が流し台を取り囲んでいる。） | 耐電の指輪 (shock resistance) | 失われる       |
| *"You hear loud noises coming from the drain."*<br>（排水口から大きな物音が聞こえる。） | 争いの指輪 (conflict) | 失われる       |
| *"The water flow seems fixed."*<br>（水の流れが一定になったようだ。） | 能力維持の指輪 (sustain ability) | 失われる       |
| *"The water flow seems stronger/weaker now."*<br>（水の勢いが強くなった／弱くなったようだ。） | 強さの指輪 (gain strength) | 失われる       |
| *"The water flow seems greater/lesser now."*<br>（水量が豊富になった／少なくなったようだ。） | 体力の指輪 (gain constitution) | 失われる       |
| *"The water flow hits/misses the drain."*<br>（水流が排水口に命中している／外れている。） | 命中の指輪 (increase accuracy) | 失われる       |
| *"The water's force seems greater/smaller now."*<br>（水の圧力が強くなった／小さくなったようだ。） | 攻撃の指輪 (increase damage) | 失われる       |
| *"Suddenly, [items] vanish from the sink!"*<br>（突然、アイテムが流し台から消え去った！ ※流し台のマスにある他のアイテムもすべて消滅） | 飢餓の指輪 (hunger) | 失われる |
| *"The sink vanishes."*<br>（流し台が消滅した。 ※流し台が別の部屋へ移動する） | 瞬間移動の指輪 (teleportation) | 失われる |
| *"The sink transforms into a fountain/throne/altar/grave!"*<br>（流し台が泉／玉座／祭壇／墓に変形した！ ※墓の生成に失敗すると稀に「流し台が消滅した」となる） | へんげの指輪 (polymorph) | 失われる |
| *"The faucets flash brightly for a moment."*<br>（蛇口が一瞬眩しく輝いた。） | 飾りの指輪 (adornment) | 失われる |
| *"The sink looks as good as new."*<br>（流し台が新品同様に見える。） | 回復の指輪 (regeneration) | 失われる |
| *"The sink glows silver (or black) for a moment."*<br>（流し台が一瞬銀色（または黒）に光った。） | 守りの指輪 (protection) | 失われる |
| *"The sink glows white for a moment."*<br>（流し台が一瞬白く光った。） | 警告の指輪 (warning) | 失われる |
| *"The sink seems to blend into the floor for a moment."*<br>（流し台が一瞬床と同化したように見えた。） | 忍びの指輪 (stealth) | 失われる |
| *"You don't see anything happen to the sink."*<br>（流し台には何の変化も見られない。） | 透明の指輪 (invisibility) | 失われる |
| *"You see some air in the sink."*<br>（流し台の中に空気が見える。） | 可視の指輪 (see invisible) | 失われる |
| *"You see the ring slide right down the drain!"*<br>（指輪が排水口へまっすぐ滑り落ちていくのが見えた！） | 自由行動の指輪 (free action) | 失われる |
| *"The hot water faucet flashes brightly for a moment."*<br>（お湯の蛇口が一瞬明るく輝いた。） | 耐炎の指輪 (fire resistance) | 失われる |
| *"The cold water faucet flashes brightly for a moment."*<br>（水の蛇口が一瞬明るく輝いた。） | 耐冷の指輪 (cold resistance) | 失われる |
| *"The sink looks like it is being beamed aboard somewhere."*<br>（流し台がどこかへ転送されているように見える。） | 瞬間移動制御の指輪 (teleport control) | 失われる |
| *"The sink momentarily looks like a regularly erupting geyser."*<br>（流し台が一瞬定期的に噴出する間欠泉のように見えた。） | へんげ制御の指輪 (polymorph control) | 失われる |
| *"The sink looks nothing like a fountain."*<br>（流し台は泉とは似ても似つかないように見える。） | 耐へんげの指輪 (protection from shape changers) | 失われる |

**流し台から水を飲むこと (Quaffing)** は、20種類あるランダム効果のいずれかを抽選しますが、大半は何の効果もありません。良い効果はごく僅かです：約1/20の確率で足元に指輪が出現する（流し台1つにつき1回限り）、同じく1/20前後の確率でランダムな薬が喉に流し込まれる（薬自体の効果もギャンブルです）程度です。悪い効果ははるかに悲惨です：1/20の確率で制御不能な変身（へんげ）を強制され、別の1/20で水のエレメンタルが解き放たれ（序盤では致命的な戦闘になります）、その他にも熱湯を浴びせられたり、ガスを吸い込んだり、病気に冒されたりします。全体として見れば恩恵よりも危険の方がはるかに大きく、それをスリルとして楽しむのでない限り頼るべきではありません。万一飲む場合は、十分なHPと脱出手段を必ず確保しておきましょう。

**流し台に薬を注ぎ入れること（浸す／ディップ）** は、独特の現象を引き起こし、実際に飲むリスクを冒すことなく薬の種類を絞り込むための賢い手段となります。以下の5つの薬は、流し台専用の固有メッセージを表示します：

| 流し台のメッセージ                                           | 該当する薬         |
| ------------------------------------------------------------ | ------------------ |
| *"The sink transforms into a fountain/throne/altar/grave!"* (または *"The sink vanishes."*) | へんげの薬 (polymorph) |
| *"Muddy waste pops up from the drain..."*（流し台1つにつき初回のみ指輪も出現） | 浮遊の薬 (levitation) |
| *"It leaves an oily film on the basin."*                     | 油の薬 (oil)       |
| *"The drain seems less clogged."*（盲目時: *"a sucking sound"*）| 酸の薬 (acid)      |
| *"You sense a ring lost down the drain."*（流し台1つにつき1回限り） | 物体を探す薬 (object detection) |

他の大半の薬を注ぐと、流し台は代わりに *"A wisp of vapor rises up..."*（一筋の蒸気が立ち上った…）と表示し、薬の瓶が割れて蒸気を吸い込んだ時と同じ効果をもたらします：この副作用によって薬を識別できます。睡眠や麻痺は1〜5ターンの間無防備になり、幻覚は一瞬の幻視をもたらします。水、果汁、レベルアップの薬、エナジーの薬、怪物を探す薬を注ぐのは無駄になります。これらはすべて単に *"nothing seems to happen."*（何も起きないようだ）と表示されるだけです。

#### 宝物庫 (Vaults)

宝物庫は、フロアの他の場所と一切接続されていない2×2マスの壁で遮断された小部屋です。どの宝物庫にもゴールドの山が眠っています。通常、岩を掘り進めるか、テレポートで偶然飛び込むことで発見されます。フロアに *"ad aerarium"* という刻み文字があれば、近くに宝物庫が存在する目印です（[刻み文字 (Engravings)](#engravings) を参照）。金貨を探す巻物（または物体を探す薬）を使えば壁越しに金貨の山を特定でき、地図化の魔法を使えばその隠し部屋の輪郭が直接明らかになります。

扉はなく、一見したところ脱出路もありません。内部でおよそ30ターン過ごすと、番兵（宝物庫の衛兵）が現れて *「お前は誰だ？ (Who are you?)」* と尋ねてきます。現実的な回答は2通りあります。

**真実（本名）を答える。** 番兵は所持しているゴールドをすべて落とすよう命じ、仮設の通路を開いてあなたを外へと案内し、背後の壁を再び密閉します。硬貨は1枚残らず失いますが、無事に脱出できます。

***Croesus*（クロイソス）と答える**（*Kroisos* や *Creosote* でも可）。番兵は宝物庫の主の名前と信じ込み、礼儀正しく立ち去ります。嘘をついたペナルティとして、秩序のキャラクターは属性値を1失います。ゴールドは手元に残りますが、財宝とともに部屋の中に一人きりで閉じ込められたままになります。

自力で壁を掘り進めるかテレポートで脱出する手段がない限り、餓死を避けるためには番兵に従ってゴールドを手放すのが賢明です。（ルディオスの要塞ですでにクロイソスを倒している場合、*Croesus* と答えると番兵が激怒して襲いかかってきます。その際は本名を名乗るルートを選んでください。）

#### 石像 (Statues)

石像はモンスターを模した石の彫刻であり、時折その場で石化させられた本物の生物であることもあります。ほとんどの石像は（つるはし、強打の杖、あるいは「衝撃」の呪文によって）破壊して内部のアイテムを取り出すことができますが、中には殴ったり上に乗ったりすると彫刻されたモンスターが生命を得て動き出す「石像の罠」もあります。
考古学者にとって、歴史的価値のある重要な石像にはその名前に *historic（歴史的な）* という単語が付きます。これを破壊すると属性値を1ポイント失います。

---

### 支流とランドマーク (Branches and Landmarks)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Mine's End luckstone-decoy variant (minend-1.lua) has FOUR mimics (appear_as luckstone/loadstone/flint/touchstone, lines 59-71) plus one real cursed loadstone (74) near the real luckstone (77); corrected "a mimic".
- Verified correct: Mines/Oracle/Sokoban/Quest depths, Fort Ludios contents & treasury, Castle wand-of-wishing chest, Medusa loot & layouts, Sokoban 75/25 prize weighting.
-->

ダンジョンの主幹はまっすぐ地下深奥へと続いていますが、大きな報酬の大半は、主幹から枝分かれした支流ダンジョンや、以下に順を追って解説する名高きランドマークで待ち構えています。

#### 進行ルートの目安 (The Route)

祭壇などの呪いを判別する確実な手段が見つかるまでは、運命の迷宮の上層を探索しましょう。ノームの鉱山の入り口は地下2〜4階に出現しますが、場所を記憶にとどめておき、準備が整うまでは先へ進むのが賢明です。挑戦の目安としては、経験レベル（XL）5程度、AC 5以下、HP満タン、投擲武器の束、そして脱出用アイテムが揃っている状態です。賢者（オラクル）のいるフロアの近くでは、上り階段の分岐から倉庫番へと向かい、軽量化の鞄または反射の魔除けを手に入れましょう。その後で鉱山街を訪れ、敵の集団を捌ける強さがついたら鉱山の最深部を攻略します。そしてレベル14になったらメインダンジョンへ戻ってクエストを達成し、メデューサの島を突破して城を目指しましょう。

**[倉庫番 (Sokoban)](#sokoban) と鉱山のどちらを先に行くべきか？** 通常は鉱山の入り口に先に出遭いますが（地下2〜4階）、初心者に対する *戦略的な推奨* は「倉庫番を先に攻略する」ことです。倉庫番は管理されたパズル主体のフロア群であり、出現するモンスターも大半は手頃です。そして最上階で手に入るご褒美（反射の魔除け、または軽量化の鞄）は、その後の [ノームの鉱山 (the Gnomish Mines)](#the-gnomish-mines) 攻略に直結して役立ちます。倉庫番を先にクリアしてご褒美を手に入れ、経験レベルを少し上げてから鉱山に挑む方が、遥かに安全で対等な戦いができます。

#### ノームの鉱山 (The Gnomish Mines)
<!-- audit
2026-05-18:
- Mines branch DL 2-4 (dungeon.lua:15-19; base=2 range=3)
- 7 Minetown variants (dungeon.lua:179-184); 1/7 picks Orcish Town (minetn-1.lua)
- gnomish PC lovemask MH_DWARF|MH_GNOME → gnomes and dwarves peaceful (role.c:654)
- Orcish Town: unaligned altar, no shops, no priest, iron-bar terrain (minetn-1.lua:18, 52, 79-88)
- Orcish Town scatters 7+ candles since Izchak's shop is absent (minetn-1.lua:98-105)
- candle shop present in minetn-2..7 (Izchak); absent only in minetn-1 (minetn-{2..7}.lua)
- all 3 Mine's End layouts place a not-cursed luckstone (minend-1.lua:77, minend-2.lua:116, minend-3.lua:67)
- minend-1 hides the luckstone among FOUR mimics (appear_as luckstone/loadstone/flint/touchstone, lines 59-71) plus a real cursed loadstone (74); search (`s`) exposes the mimics, price-ID sorts the two real stones — full mechanics in the Gray Stones section audit
- Minetown watchmen are peaceful=1 in non-orcish variants (minetn-2.lua:149)
- strategy aligned with NetHackWiki Gnomish Mines, Minetown, Mines' End, Standard strategy: Minetown described as the prime price-ID/BUC-test/priest-donation stop; guaranteed luckstone at Mine's End is canonical; Standard strategy recommends Sokoban-before-Mines as the default branch ordering for the reflection/BoH prize before tackling the Mines pack fights (https://nethackwiki.com/wiki/Gnomish_Mines, https://nethackwiki.com/wiki/Minetown, https://nethackwiki.com/wiki/Mines%27_End, https://nethackwiki.com/wiki/Standard_strategy)
-->

鉱山への入り口は、ダンジョンの地下2階から4階のどこかに下り階段として現れます。以下のマップ図のように、壁が荒削りの岩肌になり、通路がいびつに入り組んでいるため、鉱山に入ったことはすぐに分かります。

```
               ··└       ·······?└┘·└─┐
                ··└      ·G···········│
                ···      ┐·····*······└
                 ··└┐    │··`········
            ┌──┐ ┐··│┌─┐┌┘········
          ┌─┘··└┐│··└┘·└┘······┌
         ┌┘·····│┌─·`·······<·┌
         │······└┘·····)······└┐
     └───┘····┌┐····)··········└─┘  └┐
┐·············││·`········@··········│
└─┐······─┐·──┴┼─┐···················└
  └──┐·   │····└─┘···┌┐h··············└
     └┐   └──┐·······│└─┐···┌┐·········│
             └──┐····└  └───┘ ─┐·│····┌┘
```

鉱山には主にノームとドワーフが生息しており、深く潜るにつれて手強い上位種（ノームの領主、ドワーフの領主、そしてノームの王やドワーフの王）が現れます。プレイヤーがノームまたはドワーフの種族を選んでいる場合、彼らの大半は友好的であるため、鉱山は比較的快適な寄り道となります。それ以外の種族の場合は、敵対するノームやドワーフの絶え間ない猛攻を切り抜けていく必要があります。

また、鉱山には悪名高いサプライズゲストが存在します：鉱山街を除く任意のランダムな鉱山階層（鉱山最深部を含む）で、マインドフレイヤが生成される可能性があります。未探索の鉱山フロアで *"You sense a faint wave of psychic energy"*（精神エネルギーのかすかな波を感じる）という警告メッセージが出たら要注意です。マインドフレイヤは触手攻撃が命中するたびに知力を吸い取ってきます。序盤では兜による防護や安全に戦うための遠距離火力が不足していることが多いため、一度退却して準備を整えるか、この支流を後回しにするのが賢明です。

**鉱山街 (Minetown)** は、鉱山を数階層潜ったところに現れます。通常は店と寺院が並ぶ小さな居住地です。鉱山の敵集団を安定して撃退できるようになってから訪れるか、最初の挑戦で苦戦したなら倉庫番をクリアした後に再訪しましょう。店では不要なアイテムをゴールドに変えたり、役立つ装備を購入したりできます。寺院には祭壇（属性を確認してください）と常駐の司祭がいます。祭壇が自分の属性と一致していれば、アイテムをドロップして鑑定できる安全な拠点となります。また、鉱山街の司祭はACを永続的に強化してくれます。条件を満たした最初の寄付では、単なる1ポイントではなく2〜4ポイントの内在的防御値（プロテクション）が授けられます。金額と上限の基準は読み違えやすいため、[司祭への寄付 (Donating to Priests)](#donating-to-priests) の完全な表を参照してください。

ろうそくはゲーム進行中に十分な数が手に入ることが多いですが、後半で祈りの燭台（Candelabrum of Invocation）に立てるために7本確保する必要があります。鉱山街にある **イズチャックの照明店 (Izchak's lighting store)** が最も確実な調達先です。ここで7本まとめて買いましょう。店が生成されなかった場合（オークの町のマップ構成）、そのフロアのあちこちに7本以上のろうそくが散乱しています。蜜蝋のろうそくの方が獣脂のろうそくよりも長持ちしますが、どちらでも機能し、混ぜて使っても問題ありません。

ただし、7回に1回の確率で、鉱山街は **オークの町 (Orcish Town)** として生成されます。店も司祭も存在せず、入り口が鉄格子で塞がれた、オークたちに占拠された廃墟です。無属性の祭壇は残っていますが、買い物は一切できません。

また、鉱山街の警備員（町の警備隊）には十分注意してください。盗みを働く、友好的な生物を攻撃する、扉を破壊する、あるいは町の中で地面を掘削しない限り、警備員たちは友好的です。しかし1人でも怒らせると、警備隊全員が一斉に敵に回ります。

**鉱山最深部 (Mine's End)** はノームの鉱山の最深層です。3種類ある鉱山最深部のレイアウトのいずれにも、確定で（呪われていない）**幸せの石 (luckstone)** が1つ配置されているため、どのバリエーションに到達しても確実に手に入ります。幸せの石は幸運値を+3し、良い幸運が時間経過で自然減衰するのを防ぎます。聖水で祝福してゲームクリアまで常に持ち歩きましょう（[幸運の仕組み (How Luck Works)](#how-luck-works) を参照）。

幸せの石を見つけ出すには慎重な探索が必要です。ほとんどのレイアウトでは隠し部屋の中に配置されているため、迷路が行き止まりになり宝が見当たらない場合は、掘削耐性のある壁を無理に掘るのではなく、壁を捜索（`s`、`10s`）して隠し扉を探してください。隠し部屋が複数存在することもあるため、最初の1つで見つからなくても諦めてはいけません。（バリエーションの1つでは、灰色の石に擬態した4体の [**ミミック**](#a-note-on-mimics) と、見た目が全く同じで手持ちの荷物に呪い張り付く本物の **呪われた重し (loadstone)** の中に幸せの石が紛れ込まされています。怪しい石の隣で捜索（`s`）を行えば、ミミックはその場で正体を現します。本物の石は何の反応も示しません。これで幸せの石と重しの2択に絞られるため、あとは店に持ち込んで価格で識別します（幸せの石は60zm、重しは1zm）。ここでは石を蹴って判定する方法に頼ってはいけません。壁の隙間に挟まっていると、本物の幸せの石であっても重しのように鈍い音を立てて足の指を痛めることがあります。）

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

#### 賢者 (The Oracle)

運命の迷宮の中層（地下5階から9階のあたり）のどこかに、デルフィの賢者（神託所）が佇む特別な部屋が存在します。周囲はケンタウロスの石像（中は空っぽです）と4つの泉に囲まれています。古代以来のあらゆる神託の例に漏れず、彼女は謎めいた言葉を語り、先払いで代金を要求してきます。

彼女が提供するサービスは2種類あります：

- **些細な相談（Minor consultation）** は安価（50ゾークミッド）で、フォーチュンクッキーに似たメッセージを授けてくれます。これらは「真実の噂」のリストから選ばれるため、多くは雰囲気作りの言葉ですが、時折非常に有用な助言を含んでいます。
- **重要な相談（Major consultation）** は高価（500 + 50 × 経験レベル）ですが、支払ったゴールドに見合うだけの価値ある情報をもたらしてくれます：モンスター、アイテム、特殊なゲームルールに関する貴重なヒントです。

賢者は友好的であり、決して自ら攻撃してくることはありません。部屋の中は一息つくのに安全な休息場所となりますが、4つの泉には通常の泉と同じリスクが伴う点には注意してください。

それぞれの相談は、初回利用時に限り経験値（XP）を与えてくれます。もし生涯で最初の相談として「重要な相談」を選んだ場合、50〜100 XP（プレイヤーのレベルに応じて増加）が手に入ります。最初に「些細な相談」を受けるとわずか5 XPしか得られず、その後に受ける重要な相談の獲得XPも減少してしまいます。2回目以降の相談では経験値は得られません。

#### クエスト (The Quest)
<!-- audit
2026-05-18:
- quest portal Dlvl 11-16: Oracle DL 5-9 + base=6 range=2 chained off Oracle (dungeon.lua:62-64, 27-31)
- XL 14 required to descend (quest.h:45 MIN_QUEST_LEVEL, quest.c:149)
- friendly word with leader on first quest level (quest.c:97 Is_qstart → on_start)
- alignment-record refusal at MIN_QUEST_ALIGN below threshold (quest.c:164)
- 3 artifacts grant carried MR via CARY(AD_MAGM): Orb of Detection, Magic Mirror, PYEC (artilist.h:221, 257, 293)
- 3 artifacts grant wielded/worn MR via DFNS(AD_MAGM): Sceptre of Might, Eyes of Overworld, Eye of Aethiopica (artilist.h:234, 262, 305)
- nemesis gets Bell of Opening as starting inventory; drops on kill (makemon.c:1378-1379)
- quest artifact is placed under nemesis at level generation, NOT carried (Val-goal.lua:49,76; Wiz-goal.lua:73,96; etc.)
- return portal lives on Is_qstart (first quest level) only (quest.c:97, 191-204)
- "nemesis carries an amulet of life saving" is wiki-belief, not source-guaranteed; M2_COLLECT means they may pick one up (https://nethackwiki.com/wiki/Nemesis)
- strategy aligned with NetHackWiki Quest, Bell of Opening, Quest artifact: XL 14 + 20 alignment record gate, nemesis guards both artifact and Bell, return-portal only on the first quest level (https://nethackwiki.com/wiki/Quest, https://nethackwiki.com/wiki/Bell_of_Opening, https://nethackwiki.com/wiki/Quest_artifact)
2026-08-13:
- wraith corpse on graveyard levels: NOT "never" — LEVEL_SPECIFIC_NOCORPSE (mon.c:44-47) suppresses an undead's corpse only when (graveyard && is_undead && rn2(3)), i.e. 2/3 of the time, so ~1/3 still drop. off a graveyard a wraith always corpses (PM_WRAITH is in the unconditional-corpse case, mon.c:835). softened prose from "don't drop on graveyard levels" to "only about a third as often." lead-the-wraith-out advice still good (1/3 -> guaranteed).
- verified: MIN_QUEST_LEVEL 14 (quest.h:45); eating a wraith corpse => pluslvl(FALSE) guaranteed level gain (eat.c:1141).
-->

遅かれ早かれ、あなた自身の同胞から呼び出しがかかります。「クエスト」は、あなたの役職のためだけに用意された特別なダンジョン支流です。宿敵（ネメシス）があなたの役職に伝わる伝説のアーティファクトを強奪しており、リーダーはあなたを呼び出して力を証明させ、宿敵を打ち倒して至宝を取り戻す使命を与えます。ダンジョンの地下11階から16階のあたりで、魔法のポータルがその入り口へと導いてくれます。

適切なフロアに到達したかどうかはすぐに分かります。そのフロアに初めて足を踏み入れた瞬間、クエストリーダーからの微弱なテレパシーの呼びかけが頭の中に響き渡ります：

> *微弱なテレパシーによるメッセージを受信した .... 至急助けが必要だ .... ...ックな転送機を探せ。最後のメッセージはよく聞き取れなかった。*

これで探すべきものが「魔法のポータル」であることが分かります。発見するとマップ上に鮮やかな赤紫色の `^` として表示されます。他の罠と同様に、そのマスを踏む（同時に作動します）か、周囲を捜索するまで姿を隠しています。

クエストに本格的に乗り出すには、**経験レベル14** に到達し、かつ最上階（最初の階層）にいるクエストリーダーと友好的に会話を交わして階下への許可を得る必要があります。準備が整い、資格があると認められれば、リーダーは宿敵からクエストアーティファクトを取り戻す旅へと送り出してくれます。

中盤の経験値稼ぎは時間がかかるため、レベル14に到達する道のりとしては、いくつかの [レイスの死体](#a-note-on-wraiths) を食べる（1体につき経験レベルが1上昇します）か、祝福された「レベルアップの薬」を飲むのが定石です。（「死の谷」のような墓場フロアでは、アンデッドが死体を残す確率は通常の約1/3に低下するため、レベルアップを狙うならレイスを墓場の外へと誘導してから倒すのが賢明です。）

各役職には、固有のマップ、固有の宿敵、そして固有のアーティファクト報酬が用意されています。ワルキューレは [運命のオーブ (Orb of Fate)](#orb-of-fate) を求めてスルト卿（Lord Surtur）を狩ります。侍の道は [村正の剣 (Tsurugi of Muramasa)](#tsurugi-of-muramasa) を巡る足利尊氏との決闘で締めくくられます。魔法使いは [エチオピカの目 (Eye of the Aethiopica)](#eye-of-the-aethiopica) を取り戻すため闇の王の要塞へと潜入します。役職ごとの完全な一覧は [アーティファクト (Artifacts)](#artifacts) の章を参照してください。

大半のクエストアーティファクトは、ゲームクリアまで常に持ち歩くに値する至宝です。魔法防御、テレパシー、警告、反射、忍び足、幸運などの強力な能力を複合的にもたらしてくれます。その保護効果が「所持しているだけ」で発動するのか、それとも「手に持つ／身につける」必要があるのかを確認しておきましょう。

**宿敵の足元には、もう1つの極めて重要な至宝が待っています。** **開放の鐘 (Bell of Opening)** は宿敵の荷物の中にあり、倒した瞬間に床にドロップします。これは「開扉の3つのアイテム（Invocation items）」の1つであり、これなしにゲームをクリアすることは不可能です：[ゲヘナ (Gehennom)](#gehennom) の最深部、[モロクの聖域 (Moloch's Sanctum)](#molochs-sanctum) の直上にある「振動するマス」の上で、開放の鐘を鳴らし、祈りの燭台を灯し、死者の書を読み上げることで、イェンダーの魔除けが眠る聖域への扉が開かれます（儀式の完全な手順は [奪還作戦 (The Heist)](#the-heist) を参照）。一方、あなたのクエストアーティファクトは、フロア生成時に宿敵の足元に直接配置されています。立ち去る前に両方のアイテムを確実に回収してください。どちらもクエストダンジョン以外では手に入りません。

宿敵は道中で「命の魔除け」を拾って身につけていることがあるため、致命の一撃を与えても耐えられ、2回倒さなければならなくなっても動揺してはいけません。なお、メインダンジョンへ戻る脱出ポータルは **クエストの最初の階層にしか存在しません**。準備不足のまま深く潜り、途中で引き返す羽目になった場合、長い道のりを自力で登り直すことになります。

クエスト全体は、リーダーの認可にかかっています。経験レベルが14未満であるか、あるいは属性値（信仰実績）が不足している場合、自動的に追い出されます（問題を解決した後に再訪すれば受け入れてもらえます）。もしキャラクターの属性自体が変わってしまっていた場合、リーダーから永久に追放されてしまいます。クエストに挑む前に「逆属性の兜」を面白半分で試してはいけません。

#### ローグ階層 (The Rogue Level)
<!-- audit
2026-05-18:
- Rogue Level appears DL 15-18 per base=15 range=4 (dungeon.lua:54-58)
- welcome message "older, more primitive world" (do.c:1913)
- uppercase-only monsters via Is_rogue_level (makemon.c:1672)
- symbol swaps: armor `]`, amulet `,`, food `:`, gold same as gems (drawing.c:73-79)
- doors forced D_NODOOR — no closed doors (mklev.c:647-648)
- no fountains/sinks/altars/shops/graves via skip_nonrogue (mklev.c:988-989)
- rogueprobs item pool: weapon/armor/food/potion/scroll/wand/ring only — no spellbooks/tools/amulets/gems/coins (mkobj.c:58-64)
- tile mode disabled in Qt, X11, win32, curses ports (win/X11/winmap.c:1009, win/Qt/qt_map.cpp:145, 228)
- engraving has no rogue-level guard — Elbereth works as usual (engrave.c)
-->

ダンジョン中層のどこかで、1フロア限りの歴史保存地区に迷い込むことになります。
*「あなたはより古く、より原始的な世界に入り込んだようだ。(You enter what seems to be an older, more primitive world.)」*
このエリアは、ダンジョン探索ゲームといえば誰もが **『Rogue』** のことしか知らなかった古き良き時代の姿のまま残されており、いくつかの特徴がその時代を物語っています：

- 出現する生物（モンスター）の記号はすべて英大文字です：小文字の種族はまだ発明されていませんでした。
- 防具は `]`、食料は `:`、魔除けは `,` で表示され、ゴールドは宝石と同じ記号を共有します（当時のRogueでは同じ扱いでした）。
- 扉は閉まりません。蝶番の概念は後から導入されたものです。
- タイル表示モードは自動的に無効化され、飾り気のないプレーンなASCII文字表示へと切り替わります。
- 泉、流し台、祭壇、店主、司祭は一切存在せず、フロアに自然生成されるアイテムからも魔法書、道具、魔除けが排除されています。これらはすべてRogue以降に考案された要素だからです。

ただし、プレイヤー側の現代的な技術は依然として機能します。ハック（Hack）時代に追加された [エルベレス (Elbereth)](#elbereth) の文字をここに刻むことも可能です。ささやかな時代錯誤（アナクロニズム）と言えるでしょう。

#### ルディオスの要塞 (Fort Ludios)
<!-- audit
2026-05-19:
- portal placed Dlvl 11 up to just above Medusa, 1/3 chance per qualifying level (mklev.c:2647-2651)
- portal always inside a sealed vault (mklev.c:1322-1331 calls mk_knox_portal from add_room VAULT)
2026-05-18:
- level is non-diggable: des.non_diggable over full level (knox.lua:35)
- noteleport flag blocks intra-level teleport AND scroll of plain teleport — only LEVEL teleport escapes (teleport.c:854, 1502, knox.lua:9)
- garrison: 16 soldiers + 1 lieutenant (knox.lua:126-142)
- 4 D-class dragons in storerooms (knox.lua:146-149); 4 giant eels in moat (knox.lua:151-154); 1 stone giant (knox.lua:144)
- 4 corner-tower gem caches: diamond, emerald, ruby, amethyst (knox.lua:156-167)
- treasury is 15×4=60 tiles; each holds 600+rnd(0,300) gold and 1/3 of them are trapped (knox.lua:57-69)
- treasury gold totals 36k-54k (60 × 600 = min, 60 × 900 = max)
- Croesus is L20 / 4d10 weapon / MS_GUARD (monsters.h:2861-2863)
- Croesus is NOT M3_COVETOUS — his only mflags3 is M3_INFRAVISIBLE (monsters.h:2865-2868)
- only Wizard of Yendor has M3_COVETOUS; Vlad has M3_WANTSCAND; Riders use their own logic
- alarm sounds on arrival and every revisit until Croesus dies (do.c:1893-1904)
- alarm wakes existing soldiers; it doesn't spawn new ones
- soldiers carry K_RATION / C_RATION (makemon.c:694-700)
- strategy aligned with NetHackWiki Fort Ludios, Croesus: bag-of-holding-for-gold and shoot-Croesus-across-the-moat are canonical (https://nethackwiki.com/wiki/Fort_Ludios, https://nethackwiki.com/wiki/Croesus)
-->

ルディオスの要塞はクロイソス（Croesus）の本拠地です。攻略は任意（オプショナル）であり、見落としやすい隠しダンジョンです：ポータルは地下11階からメデューサの島の直前までの階層に生成され、常に閉鎖された宝物庫の内部に配置されるため、壁を掘るか扉を突破して見つけ出す必要があります。突入と同時に警報が鳴り響き、駐屯する16人の兵士と1人の中尉が目を覚まします。4体のドラゴンが貯蔵庫を守り、1体の岩巨人と4体の巨大ウナギが堀を警備しています。クロイソスは玉座で待ち構えており、その近接攻撃は非常に痛烈であるため、堀越しに矢弾を撃ち込むか杖の光線を浴びせて倒すのが賢明です。

このフロアは全域が掘削不能（non-diggable）であり、同一フロア内での通常のテレポートも封じられています。脱出するには入ってきたポータルを使うか、階層テレポート（レベルテレポート）を用います。宝物庫には60マスにわたって36,000〜54,000 zmもの莫大なゴールドが敷き詰められていますが、その約1/3のマスには地雷やトゲの落とし穴が潜んでいます。四隅の角塔にはダイヤモンド、エメラルド、ルビー、アメジストが保管されており、兵士たちは携帯食糧（レーション）と十分な武器を所持しています。クリアに必須のアイテムは何一つありません。ここを訪れる最大の理由は純粋にゴールドであり、それは司祭への寄付を通じてAC（防御力）の大幅な恒久強化へと化けます。

#### メデューサの島 (Medusa's Island)
<!-- audit
2026-05-19:
- Perseus loot is per-layout — not uniform: shield 75% in medusa-1/3/4 but 25% in medusa-2 (medusa-2.lua:58-63)
- boots are 25% in medusa-1/3/4 but 75% in medusa-2 — swapped with the shield
2026-05-18:
- Medusa DL 20-29: base=-5 range=4 from DoD bottom 25-29 (dungeon.lua:75-81)
- four layouts (medusa-1.lua through medusa-4.lua); all use des.stair("down") — no ladder
- scimitar blessed +2 at 50% and sack at 50% are constant across all four layouts (medusa-1.lua:70, 73)
- shield is cursed in every layout (medusa-1.lua:64 and matching lines in others)
- gaze reflection stones Medusa via ureflects → killed(mtmp) (mhitu.c:1721-1745)
- stone resistance also blocks the gaze (mhitu.c:1747-1748) — rarely attainable pre-Medusa
- eel grab drown uses eel's tile, not yours: is_pool(magr->mx, magr->my) (uhitm.c:3389-3401)
- levitation/water-walking on adjacent dry land does NOT save you once grabbed
- medusa-2 has six electric eels (not giant eels), AD_ELEC bite (medusa-2.lua:99-104, monsters.h:3239-3247)
- kraken only on medusa-4 (medusa-4.lua:122)
- strategy aligned with NetHackWiki Medusa, Reflection, Perseus: reflection/blindfold against the gaze, levitation/water-walking to cross, Perseus statue as a backup reflection source (https://nethackwiki.com/wiki/Medusa, https://nethackwiki.com/wiki/Reflection, https://nethackwiki.com/wiki/Perseus)
-->

メデューサのフロアは運命の迷宮の最深部に近い地下25階前後に位置しています。広大な水域とあちこちに散乱する石像（かつて冒険者だった者たち）を見れば、そこがメデューサの島であることは一目瞭然です。

> *2000年代初頭、Arien Malec氏がPat Rankin氏、Geoduck氏、Topi Linkala氏らの助言を得て、RGRNの投稿者たちから渡河戦術を収集・整理しました。以下はそのガイドの要約版です。*

このフロアには1つの島に3つの試練が集約されています：島を取り囲む **水域の横断**、その水中に潜む **巨大ウナギ**（1つのマップ構成では電気ウナギ）、そして視線が合った者を石に変える **メデューサ自身** です。それぞれについて以下で個別に解説します。もし倉庫番から「反射の魔除け」を持ち帰っているなら、3つ目の問題はすでに解決しています。

島の中央には、[城 (The Castle)](#the-castle) へと続く下り階段が存在します。この階層には4種類のマップレイアウトが存在するため、1つの地図を暗記することに頼ってはいけません。

**ペルセウスの石像。** 島にある石像の1つには **ペルセウス (Perseus)** という名が刻まれています。鏡の盾を使ってメデューサを討ち取った神話の英雄です。「衝撃」の呪文、強打の杖、またはつるはしでこの石像を破壊すると、（呪われた）**反射の盾 (shield of reflection)**（4つのレイアウトのうち3つで75%、残りの1つで25%の確率）、祝福された+2の **シミター**（50%）、**浮遊の靴 (levitation boots)**（3つのレイアウトで25%、盾の確率が低いレイアウトでは75%）、そしてこれらを収納する **袋**（50%）が手に入ります。反射の盾は呪われているため、装備する前に解呪の手段を用意しておきましょう。なお、このフロアにある他の石像の中身はすべて空っぽです。

**メデューサの視線を生き延びる方法。** 彼女の階層に降りる前に、以下のいずれかの対策を必ず用意してください：

- **反射 (Reflection)**（魔除け、盾、または銀色ドラゴンの鱗鎧）。メデューサの視線が反射して跳ね返り、彼女自身を石化させます。これが最も安全かつ確実な解決策であり、大半のプレイヤーが採用する方法です。
- **目隠し、またはタオル。** 彼女の視界に入る前に装着します。盲目状態で移動・索敵するために [テレパシー](#senses-and-perception) や怪物を探す手段が必要になります。視線対策としては完璧に機能しますが、フロアの探索は格段に難しくなります。
- **鏡。** 目を覚ましているメデューサに対し、遮るもののない直線上の任意の位置から鏡を「適用（`a`）」します。どのマップ構成でも彼女は初期状態で眠っているため、まずは安全な距離から起こす必要があります。
- **一撃必殺。** 死の杖や「死の指」の呪文なら、相手に行動のターンを与えることなく即死させられます。なお、メデューサ自身は石化耐性を持つため、コカトリスの死体は効きません。
  どのような方法で倒したとしても、**彼女の死体を絶対に食べてはいけません**。彼女はゴルゴンであり、その死肉を口にした者は即座に全身が石化してゲームオーバーになります。

**水域の横断。** 島は深い水で囲まれています。安全な順から絶望的な順に並べた選択肢は以下の通りです：

- **浮遊 (Levitation)**（指輪、靴、薬、または呪文）。最も安全かつ容易な渡河手段です。ただし、隣接する水マスからウナギに引きずり込まれる危険は残ります（[即死の危険](#ways-to-die-instantly) の [溺死](#drowning) を参照）。
- **水上歩行の靴 (Water walking boots)**。水面の上を歩いて渡れます。こちらも隣接する水中にいるウナギの巻きつき攻撃は防げません。
- **冷気の杖 (Wand of cold)**。水面に向かって杖を振り、氷の道を凍らせて作ります。1マス進むごとに足を滑らせて2ターン行動不能になるリスクがあり、火炎によって氷が再び溶けてしまうこともありますが、渡り切ることは可能です。
- **大地の巻物 (Scroll of earth)**。頭上から落下した巨石が水没し、飛び石の橋が完成します。時間はかかりますが、他に手段がない場合には有効です。
- 飛行または遊泳能力を持つ生物への **変身（へんげ）**。[変身制御](#special-and-utility) の能力がない場合は極めて危険です。
- **飛び跳ねる靴 (Jumping boots)、または騎士の跳躍能力**。幅の狭い水路を跳び越えることができますが、慎重な位置取りが求められます。

**ウナギの脅威を切り抜ける。** 水中には巨大ウナギ（4種類あるマップ構成のうち1つではクラーケン）が潜んでおり、巻きついて水中に引きずり込み溺死させてきます。以下の重要ルールを徹底してください：

- **防水クローク (oilskin cloak)** を羽織るか、防具に **油（グリース）を塗っておく** と、ウナギが巻きついてきた際に滑り落とすことができます。グリースは時間経過で剥がれるため完全な信頼は置けませんが、防水クロークの効果は永続します。
- **[呼吸の魔除け (amulet of magical breathing)](#movement-and-spatial-behavior)**（または変身による水中呼吸）があれば、巻きつかれて水中に引きずり込まれても溺死を防ぐことができます。
- ウナギは可能な限り **遠距離から撃破してください**。杖、呪文、投擲武器のいずれも有効です。水中にいるウナギに不用意に近接戦闘を挑んではいけません。
- 浮遊や水上歩行の状態であっても、隣接する水マスにいるウナギからの巻きつき攻撃は **防げません**。溺死判定はプレイヤーの足元ではなく *ウナギのいるマス* を基準に行われるためです。防水クローク／グリース、呼吸の魔除け、あるいは接近される前に遠距離から倒すことだけが確実な防御策です。

#### 城の概要 (The Castle) {#castle-overview}
<!-- audit
2026-05-18:
- Castle is the last DoD level: base=-1 (dungeon.lua:7-12, 82-85)
- fortified structure surrounded by a moat with a drawbridge (castle.lua:25-41)
- defenders: soldiers in barracks, dragons in storerooms, court of high-letter monsters in throne room (castle.lua:54, 60, 180, 185, 195-221)
- wand of wishing in a locked chest in one of the four corner towers (castle.lua:48-52, 142-149)
- Gehennom branches off the Castle; the stairs do not return (dungeon.lua:39-43)
-->

城（The Castle）は、光ある通常ダンジョンの壮大なフィナーレであり、その下に広がるさらなる深淵への玄関口です。周囲を堀で囲まれた石造りの要塞であり、唯一の侵入口は跳ね橋となっています。内部には強大な守備隊が待ち構えています：兵舎の兵士たち、貯蔵庫を警備するドラゴンたち、そして玉座の間にひしめく大文字の強敵モンスターたちの一団です。この危険な攻城戦を挑むに値する最大の報酬は、四隅の角塔のいずれかにある鍵のかかった宝箱の中に眠っています。ゲーム中最も貴重なアイテムである **願いの杖 (wand of wishing)** です。

また城は、[ゲヘナ (Gehennom)](#gehennom) への進入口としての役割も果たします。跳ね橋を降ろして侵入する方法や、城内での立ち回りについての詳細は、第5部の [城 (The Castle)](#the-castle) を参照してください。

---

### 罠と危険 (Traps and Hazards)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source (domagictrap trap.c:4319-4453):
- Rewrote the magic-trap effects paragraph. It is fate=rnd(20): <10 blind+summon 1d4; 10 nothing; 11 toggle invis; 12 fire; 13-18 flavor; 19 tame+CHA+1; 20 UNCURSE inventory. Old text's "curse an item" was backwards; sleep/stun/vomiting/earthquake/HP/mana/mapping/lighting don't exist; CHA is +1 on ~1/20 (~+0.05/zap), not +1.4.
- Confused gold detection reveals ALL traps (trap_detect, read.c:2042), not just magical.
- "A rumbling stop abruptly" is a boulder hitting a teleport trap only (trap.c:3477); pits route through flooreffects.
- Verified correct: pit/spiked-pit damage, trapdoor cascade, bear-trap diagonal escape, anti-magic/cancellation blasts, iron-footwear protections.
-->
<!-- audit
2026-05-31:
- mktrap() places traps in rooms only (somexyspace(croom)) on standard dungeon levels; the MAZEFLAG path that allows corridor traps is set on maze levels (Gehennom mazes, etc.). Standard corridors do not generate traps (mklev.c:2032-2099, somexyspace usage at line 2093).
- display priority: monster > object > trap > floor. A corpse object on a trap square draws as `%` and hides the `^` glyph (display.c symbol layering).
- #untrap requires the trap to be visible (known) and the player to be adjacent (or on the trap). It then attempts to disarm based on trap type (trap.c untrap_object).
-->

たった1つの落とし扉によって、愛するペット、保管しておいた貴重な物資、そして利用するはずだった階段から一瞬にして分断されてしまうことがあります。罠は、自分で踏み抜くか、`s` キーで探知するか、あるいは他の手段で暴くまで目に見えません。発見されると、マップ上には `^` として表示されます。隣接するマスを1回捜索するごとに罠を発見できる独立した抽選が行われますが、その成功率は決して100%ではないため、怪しい場所では繰り返し粘り強く捜索を行う必要があります。ペットはあなたがすでに発見済みの罠しか避けてくれないため、ペットの挙動を眺めていても未発見の罠を察知することはできません。

覚えておくべき典型的な状況があります：部屋の床の上に理由もなく死体がポツンと転がっている場合、それはその冒険者を仕留めた罠の上に覆い被さっていることが多々あります。死体の記号 `%` は `^` の上に優先して描画されるため、本来なら視認できているはずの罠が隠されたままになります。その死体の下には持ち主が落とした装備品が重なっていることもあり、調べる価値は大いにあります。隣接するマスから周囲を捜索して罠を暴き、不用意に足を踏み入れる代わりに `#untrap` コマンドを使って罠の解除を試みましょう。

以下はダンジョンで遭遇する罠の一覧であり、踏み抜いたときの痛恨度（後悔の度合い）によって大まかに分類されています：

#### 軽微な罠 (Nuisance Traps)
<!-- audit
2026-05-18:
- arrow trap empty-click is 1/15 once `trap->once && trap->tseen` (trap.c:1199, 1228)
- dart trap 1/6 chance the dart is poisoned (trap.c:1273)
- squeaky board skipped by Levitation OR Flying unless forcetrap (trap.c:1419)
- squeaky board wakes monsters: wake_nearby for player, wake_nearto range 40 for monster (trap.c:1436, 1473)
- rust trap default branch (40% via cases 3,4 of rn2(5)) douses lamplit items then cloak else suit else shirt (trap.c:1610, 1632-1643)
- rust trap cases 0/1/2 hit helm, then left-arm chain (shield→weapon→gloves), then right-arm (weapon→gloves) (trap.c:1611-1627)
- missed arrows and darts land via place_object + stackobj — can be farmed (trap.c:1217-1220, 1288-1291)
- mounted player: steed absorbs the hit 50% of the time (trap.c:1211, 1276)
-->

| 罠の種類        | 効果                                                |
| --------------- | --------------------------------------------------- |
| 矢の罠 (Arrow trap)      | あなたに向けて矢を撃ち出す（軽微なダメージ）        |
| ダーツの罠 (Dart trap)   | ダーツを撃ち出す（毒が塗られている場合あり）        |
| 軋む床 (Squeaky board)   | 大きな軋み音を立て、周囲のモンスターを目覚めさせる  |
| 錆の罠 (Rust trap)       | 水を浴びせかける：装備中の鉄製防具を錆びさせ、クローク／鎧／シャツを濡らし、火のついたランプを消火する |

厄介ではありますが、致命傷になることは稀です。不幸中の幸いとして、矢の罠やダーツの罠はタダで投擲・射撃用の弾薬を供給してくれるため、あえて安全に踏み抜いて弾薬をストックするテクニックもあります。

#### 移動系の罠 (Movement Traps)
<!-- audit
2026-05-18:
- trapdoor cascade: dlevel++ per loop iteration, `if (rn2(4)) break` = 25%/level chance to keep falling (trap.c:442-453)
- holes use the same hole_destination cascade as trapdoors (trap.c:519-522, 442-453)
- pit base damage 1d6 (trap.c:1950, rnd(adj_pit ? 3 : 6))
- spiked pit base damage 1d10 with 1/6 chance of poison (trap.c:1925, 1938-1945)
- Levitation OR Flying skip pit/hole/trapdoor, gated `!Sokoban && ...` (trap.c:633-639, 1850)
- in Sokoban the skip is disabled — pits suck you in regardless
-->

| 罠の種類         | 効果                                                       |
| ---------------- | ---------------------------------------------------------- |
| 落とし穴 (Pit)   | 中に落下し、軽微なダメージを受けます。自力で這い上がれます |
| トゲの落とし穴 (Spiked pit) | 落とし穴と同様ですが、底に杭が敷かれています（より大きなダメージ、毒の危険あり） |
| 落とし扉 (Trapdoor) | ダンジョンの竪穴から下の階層へ落とされます。通常は1階層ですが、階ごとに25%の確率で落下が連鎖し、数階層下まで一気に落ちることがあります |
| テレポートの罠 (Teleport trap) | フロア内のランダムなマスへとテレポートさせられます |
| 階層テレポートの罠 (Level teleporter) | ランダムなダンジョン階層へとテレポートさせられます |
| 穴 (Hole)        | 落とし扉と似ていますが、最初から穴として目に見えています |
| 魔法のポータル (Magic portal) | 別の支流ダンジョンへと転送されます（各支流の入り口） |

落とし扉と階層テレポートの罠は、探索のリズムを最も狂わせる厄介な罠です：たった一歩の踏み外しで、ペット、保管しておいた貴重な物資、そして念入りに探索したフロア地図から強制的に分断されてしまいます。しかし、アイテムや内在能力によって [瞬間移動制御 (teleport control)](#movement-and-spatial-behavior) を得ていれば、テレポートの罠はタダで利用できる便利な長距離移動手段へと変わります。また、**浮遊や飛行** の状態であれば、落とし穴、穴、落とし扉のすべてを完全に無効化して上空を通過できます。ただし、パズルの厳格なルールにより無効化が無効化され、下降気流で問答無用に吸い込まれる [倉庫番 (Sokoban)](#sokoban) だけは例外です。

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

#### 捜索と探知 (Searching and Detection)
<!-- audit
2026-05-18:
- dosearch0 search mechanics at detect.c:2016-2093
- rnl applies a Luck bias (good Luck → 0, bad Luck → x-1) (rnd.c:112-128)
- SDOOR/SCORR roll is rnl(7 - fund); fund capped at +5 (detect.c:2026-2032, 2042-2054)
- trap-detection roll is rnl(8) with NO fund bonus (detect.c:2079) — Excalibur+lenses don't speed trap-finding
- Excalibur is the only SPFX_SEARCH artifact (artilist.h:85-86)
- wand of secret door detection is NODIR; findit reveals SDOOR/SCORR/traps/trapped chests/trapped doors/hidden mimics/hiders (detect.c:1639-1718, zap.c:2552-2558)
- wand area is a circle of radius BOLT_LIM=8 (vision.c:27-45 circle_data, hack.h:49) gated by couldsee() line of sight (vision.c:2144)
- Flying/Levitation skip most floor traps but NOT magic/teleport/anti-magic (trap.c:1061-1082 floor_trigger list omits MAGIC_TRAP/TELEP_TRAP/ANTI_MAGIC; trap.c:3026 check_in_air bypass gated by floor_trigger)
-->

罠に対する最大の防御は、罠に踏み込む前に自ら発見することです：

- **捜索（`s`）を繰り返す。** 1回捜索するごとに、隣接するマスにある未発見の罠を暴く独立した確率があり、幸運（Luck）が高いほど発見率が向上します。（アーティファクトや目玉レンズによる探索ボーナスは、隠し扉や隠し通路の発見速度を高めるだけであり、罠の発見率には影響しません。）
- **扉探索の杖 (wand of secret door detection)。** 自分を中心とする半径約8マスの円形エリア（視線が通る範囲）に存在するすべての隠蔽物を一網打尽に暴き出します：隠し扉、隠し通路、罠、罠付きの宝箱、そして姿を隠したモンスターを一度に露わにします。方向指定は不要です。
- **水晶玉 (Crystal ball)。** フロア全体のすべての罠を一度に探知することができます。
- **飛行と浮遊。** 大半の床面トラップを完全に無力化できます（ただし、クモの巣、魔法の罠、テレポートの罠、階層テレポートの罠、変身の罠、反魔法フィールドは空中でも作動します）。
- **混乱状態で「金貨を探す巻物」を読む。** 通常の金貨探知が *罠探知* へと変化します：そのフロアに存在するすべての罠が一瞬でマップ上に点灯して判明します。混乱状態での金貨探知は、ゲヘナ突入前にフロア全体の罠を安全に把握するための最も経済的な手段です。

捜索を行うべき絶好のタイミングは、ダンジョンがすでに「何かがおかしい」という違和感のヒントを発しているときです：他に何もない部屋の中央に転がる不審な死体、床に散乱した矢やダーツ、あるいは隠された危険がギミックとなっているテーマのある部屋に遭遇したときがそれに当たります。

#### 隠し扉の発見 (Finding Secret Doors)
<!-- audit
2026-05-19:
- ring of searching auto-calls dosearch0(1) each turn unless level is noautosearch (allmain.c:342-344)
- Excalibur enchantment feeds `fund = uwep->spe` only if SPFX_SEARCH (detect.c:2026-2027, artilist.h:85-86)
- lenses add +2 to fund if worn and not Blind (detect.c:2029-2030)
- fund is capped at +5 — a +5 Excalibur alone hits the cap; lenses only help if enchantment is <+3 (detect.c:2031-2032)
- per-square reveal roll is rnl(7 - fund) for SDOOR/SCORR (detect.c:2042-2054)
- blessed scroll of magic mapping converts every SDOOR to a visible door (read.c:2121-2130)
- +0 Excalibur contributes nothing because fund = spe = 0
-->

運命の迷宮の設計者たちは、「すべての部屋には、壁を10分間叩き続けなければ見つからない非常口を1つ設けるべきだ」と信じていた節があります。隠し扉や隠し通路は、「お前の探索はまだ *徹底的* ではない」とゲームが突きつけてくる無言のメッセージです。

**隠し要素を捜索すべきタイミング：**

- **不自然に行き止まりになっている通路。** 通路が唐突に途切れ、目的のものが見当たらない場合、周囲の壁のどこかに扉が隠されている可能性が極めて高いです。
- **出口が1つもない不審な空き部屋。** 出口は必ず存在します。巧妙に壁に見せかけて偽装されているだけです。
- **目に見える選択肢をすべて調べ尽くした後。** 到達可能な場所をすべて踏破したにもかかわらず下り階段が見つからないなら、うろつき回るのをやめて壁を叩き始める潮時です。

**体系的な捜索手順：**

その場で `20s` と入力して20回連続で捜索します。平均的な幸運値を持つ駆け出しのキャラクターの場合、隠し扉を確実に暴き出すには15〜22回の捜索が必要です。1回だけ捜索して通り過ぎるのは、「迷子のままで構わない」と宣言しているようなものです。

壁に沿って3マス移動し、再び20回捜索します。1回の捜索は全方位1マスに届くため、3歩刻みで進めば隙間を作らず、かつ無駄な重複捜索を避けて壁一面を完全にカバーできます。紙の上では退屈な作業に見えますし、*実際* に退屈ですが、地下1階に永久に閉じ込められることに比べれば退屈さなど安いコストです。

レンジャーや考古学者のキャラクターなら、この苦労の大半から解放されます：どちらも最初から自動捜索（オートサーチ）の能力を持っており（エクスカリバーを手に持っているキャラクターも同様です）、1歩進むごとに隣接する全マスを自動で調べるため、壁沿いを歩くだけで隠し要素を次々と暴き出します。ただし頑固な扉に対しては、足を止めて数回捜索する必要があるかもしれません。

**役立つアイテム：**

- **探索の指輪 (Ring of searching)**：身につけている間、毎ターン自動的に捜索を行います。
- **[エクスカリバー (Excalibur)](#excalibur-artifact)**（または探索オーラを持つアーティファクト）：手に装備すると、その強化値が探索ボーナスに加算されます（泉から拾い上げたばかりの+0ではボーナスは付きません）。
- **目玉レンズ (Lenses)**：装着中（盲目でない限り）、探索ボーナスに+2されます。
- **扉探索の杖 (Wand of secret door detection)**：周囲の一定半径内にある隠し要素を瞬時にすべて暴き出します。
- **祝福された地図の巻物 (Blessed scroll of magic mapping)**：フロア内のすべての隠し扉を通常扉へと変えて可視化します（祝福された巻物限定の効果です）。

すでに下り階段が見つかっているなら、迷わず階段を降りましょう。壁叩きは出口や特殊な部屋が見つからないフロアでのみ行うべき手段であり、すべての階層で義務的に行う儀式ではありません。

#### 鉄格子 (Iron Bars)
<!-- audit
2026-05-18:
- passes_bars uses verysmall() = msize < MZ_SMALL = TINY only (mondata.c:552-563)
- grid bug / bat / sewer rat are MZ_TINY (monsters.h:889, 1149, 1269); kitten and little dog are MZ_SMALL and stay out
- acid (ray/breath/spit) corrodes bars unconditionally (zap.c:5347-5369)
- lightning shares the acid branch but is gated `rn2(10) break` — melts on roughly 1 zap in 10 (zap.c:5349)
- striking and force bolt have NO IRONBARS handler — they pass through harmlessly
- rock moles eat bars via the metallivorous arm (hack.c:769-784)
- xorns and earth elementals pass walls and so pass bars
- bars sit on a room-wall tile (mklev.c:783); niche payload one square further into stone
- scroll of teleportation placed in niche only when `!noteleport` on the level (mklev.c:790-792)
-->

鉄格子は一見すると侵入を阻む頑丈な防壁に見えますが、完全な固体ではありません：光は通り抜け、ごく小型の生物（グリッドバグ、コウモリ、ネズミなど）は格子の隙間をすり抜けることができます（ただし小猫以上の大きさの生物は遮られます）。つるはしは弾かれ、採掘の杖は不発に終わり、強打の杖や「衝撃」の呪文は格子を素通りして無害に通過します。鉄格子を破壊できるのは「酸」です：黄色ドラゴンのブレスや、格子に叩きつけて割った「酸の薬」が有効です。特に酸の薬は手軽で重宝します。手に装備して格子に向かって強制戦闘（`F`）を仕掛ければ、酸の飛沫が鉄格子を跡形もなく溶かして消し去ってくれます。また、もし重い鉄球に鎖で繋がれているなら、その鉄球を手に持って格子を力任せに殴打して破壊することも可能ですが、およそ25回もの打撃が必要です。

最も一般的な対処法は、格子の周囲の壁を掘ることです。鉄格子は部屋の壁をくり抜いた壁龕（ニッチ）に設置されているため、斜めの壁を掘るか背後の壁を回り込んで掘削すれば、格子に触れることなく奥の部屋へ到達できます。格子の奥に隠されているアイテムは、たいてい「瞬間移動の巻物」です。

---

### 感覚と物音 (Feelings and Sounds)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- "monsters are aware of your presence" comes only from a monster casting MCAST_AGGRAVATION -> aggravate() (mcastu.c:826-828); removed the "cursed ring of aggravate monster" cause (worn rings give no message, do_wear.c:1266).
- "presence of evil" is only the fountain water demon while blind (fountain.c:74); removed "or other major demon".
- Verified correct: hypocrite/Elbereth alignment hit, stealth messages, pet-kill thunder -15, curse-items cast, summoning messages, resistance-absorb messages.
-->
<!-- audit
2026-05-18:
- vault sounds: "counting gold" means vault with gold; "searching" means empty vault (sounds.c:253-262)
- "Wow! ...great!" needs blessed restore-ability with zero unfixable troubles (potion.c:658-661)
- same string also fires from a blessed magic fountain (fountain.c:257)
- non-boot stealth gear gives "move very quietly"; boots give "walk very quietly" (do_wear.c:123-129)
- lycanthropy cure is quaffing holy water, not dipping (potion.c:728-737)
- quantum corpse toggles HFast on or off: "seem faster" or "seem slower" by current state (eat.c:1227-1235)
- dosounds() is silenced by Deaf, !flags.acoustics, u.uswallow, or Underwater (sounds.c:208-209)
- bugle reveille at muse.c:843-846 is gated only by !Deaf (not by dosounds)
- sad-feeling at mon.c:3100-3101 is NOT gated by Deaf — it's a feeling, not a sound
- oracle "strange wind" (sounds.c:190); shop "cursing shoplifters" (sounds.c:322)
- fountain "bubbling water" or "water falling on coins" (sounds.c:214-218)
-->

迷宮の何気ない環境描写（メッセージ）の中には、極めて重要な警告が隠されています。まずは最も重要な4つの緊急メッセージを覚え、より珍しいメッセージが表示されたら後述の表でその意味を確認できるようにしましょう。

（注意：**耳が聞こえない（聾・Deaf）**、モンスターに **丸呑みされている**、あるいは **水中** にいる間は、環境音に関するメッセージが一切届かなくなります。特に永久聾の縛りプレイでは、フロアの雰囲気から得られるあらゆる手掛かりを失うことになります。ただし、死体を食べたときに得られる感覚のメッセージはそのまま表示されます。）

#### 緊急事態 (Emergencies)

| メッセージ | 意味と対処法 |
|------------|--------------|
| *"You feel feverish."*<br>（熱っぽく感じる。） | 獣人（ウェアモンスター）からの獣化症（ライカンスロープ）感染です。聖水を *飲む*、トリカブトを食べる、または祈り（`#pray`）を捧げましょう。 |
| *"You are slowing down."*<br>（体の動きが鈍くなってきた。） | 肉体が石へと変化しています（石化進行中）。即座にトカゲの死体を食べる、酸の薬を飲む、または祈り（`#pray`）を捧げてください。 |
| *"You are turning into a green slime."*<br>（体が緑色のスライムに変化しつつある。） | 緑のスライムによるスライム化感染です。火で焼き払う（火の巻物を読む、自身に火球の呪文を唱える、あるいは火の杖を自分に振る）、または祈り（`#pray`）を捧げてください。 |
| *"You feel deathly sick."*<br>（死ぬほど気分が悪い。） | 致死性の病気（ペスティレンスやデモゴルゴン等による攻撃）です。超回復の薬を飲む、ユーカリの葉を食べる、病気治療の呪文を唱える、または祈り（`#pray`）を捧げてください。 |

#### フロアの環境音 (Level Ambience)

| メッセージ                                       | 意味                                                                     |
|--------------------------------------------------|--------------------------------------------------------------------------|
| *"You have a sad feeling for a moment, then it passes."*<br>（一瞬悲しい気分になり、やがて消え去った。） | 視界外でペットが命を落としました。                                       |
| *"You hear bubbling water."*<br>*"You hear water falling on coins."*<br>（水の泡立つ音が聞こえる／硬貨の上に水が落ちる音が聞こえる） | このフロアに泉が存在します。                                             |
| *"You hear someone cursing shoplifters."*<br>*"You hear the chime of a cash register."*<br>（万引き犯を罵倒する声が聞こえる／レジのチャイムが聞こえる） | このフロアに店が存在します。                                             |
| *"You hear someone counting gold coins."*<br>*"You hear the footsteps of a guard on patrol."*<br>*"You hear someone searching."*<br>（金貨を数える音が聞こえる／見回りの足音が聞こえる／何かを探す音が聞こえる） | このフロアに宝物庫が存在します。「数えている」は中にゴールドが残っている証拠であり、「探している」は宝物庫がすでに空であることを示します。 |
| *"You hear a wolf howling at the moon."* (またはジャッカル)<br>（月に吠える狼の遠吠えが聞こえる） | このフロアのどこかに獣人（ウェアクリーチャー）が生息しています。         |
| *"You hear crashing rock."*<br>（岩が崩れ落ちる音が聞こえる。） | 穴掘り生物（ドワーフ、岩モグラ、アンバーハルク）が岩壁を掘削しました。   |
| *"You hear rumbling nearby."* (または *in the distance*)<br>（近くで／遠くでゴロゴロと鳴る音が聞こえる） | 視界外で転がる巨石の罠が作動しました。*"You hear a rumbling stop abruptly."*（ゴロゴロという音が唐突に止まった）は、巨石がテレポートの罠に吸い込まれたことを意味します。 |
| *"You hear a chugging sound."*<br>（ゴクゴクと音を立てて飲む音が聞こえる。） | モンスターが薬を飲みました（通常は自らの傷の回復）。                     |
| *"You hear a nearby zap."*<br>（近くでバチッという発射音が聞こえる。） | モンスターが視界外の何かに向けて杖を振りました。                         |
| *"You hear a strange wind."*<br>（奇妙な風の音が聞こえる。） | このフロアに賢者（オラクル）がいます。                                   |
| *"You hear a slurping sound."*<br>（ジュルジュルという吸い込む音が聞こえる。） | ゼラチンキューブがフロアの床に落ちているアイテムを捕食しました。         |
| *"You hear a crunching sound."*<br>（バリバリと噛み砕く音が聞こえる。） | 錆の怪物、岩モグラ、またはその他の金属食生物が金属アイテムを食べました。 |
| *"You hear a bugle playing reveille!"*<br>（ラッパが起床ラッパを奏でるのが聞こえる！） | 兵士がラッパを吹いて周囲の兵士たちを起こしました。戦闘を警戒してください。 |

#### 内在能力と死体効果 (Intrinsics and Corpse Effects)

| メッセージ | 意味 |
|------------|------|
| *"You feel healthy."*<br>（健康になった気がする。） | 死体を食べて「毒耐性」の内在能力を獲得しました。 |
| *"You feel a momentary chill."*<br>（一瞬寒気を感じた。） | 死体を食べて「火炎耐性」の内在能力を獲得しました。 |
| *"You feel full of hot air."*<br>（熱気配に満たされた気がする。） | 死体を食べて「冷気耐性」の内在能力を獲得しました。 |
| *"Your health currently feels amplified!"*<br>（健康が増幅されたように感じる！） | 死体を食べて「電撃耐性」の内在能力を獲得しました。 |
| *"You feel wide awake."*<br>（目がパッチリと冴えた気がする。） | 死体を食べて「睡眠耐性」の内在能力を獲得しました。 |
| *"You feel very firm."*<br>（体が非常に引き締まった気がする。） | 死体を食べて「分解耐性」の内在能力を獲得しました。 |
| *"You feel a strange mental acuity."*<br>（奇妙な精神の冴えを感じる。） | 死体を食べて「テレパシー」の内在能力を獲得しました。 |
| *"You seem faster."*<br>（足が速くなったようだ。） | 量子物理学者の死体を食べて「高速（スピード）」の内在能力を獲得しました。（すでにスピードを持っていた場合は代わりに *"seem slower"*（足が遅くなったようだ）となり、量子物理学者の死体はオン／オフを切り替えます。） |
| *"You feel a mild buzz."*<br>（かすかな刺激を感じる。） | イモリの死体を食べてMP（魔力）が1〜3回復しました。 |
| *"You see an image of someone stalking you. But it disappears."*<br>（盲目時: *"You feel very self-conscious. Then it passes."*） | 泉の水を飲んで永続的な「不可視の視覚（透明視）」を獲得しました。幸運な一口でした。 |

#### 識別と状態変化 (Identification and Status Changes)

| メッセージ | 意味 |
|------------|------|
| *"A feeling of loss comes over you."*<br>（喪失感に襲われた。） | 泉にアイテムを浸して解呪の結果を引きましたが、そのアイテムは呪われていませんでした。何も起きておらず、文面とは裏腹に何かを失ったわけではありません。 |
| *"You have a feeling of loss."*<br>（喪失感を覚えた。） | 「充填の巻物」を読みましたが、充填できないアイテムを選択してしまいました（杖、指輪、および一部の道具のみが充填可能です）。巻物は無駄に消費されました。 |
| *"You sense a lack of food nearby."*<br>（近くに食料が存在しない気配を感じる。） | 「食料を探す巻物」を読みましたが、フロア内に食料が存在しません。 |
| *"You feel materially poor."*<br>（物質的に貧しくなった気がする。） | 「金貨を探す巻物」を読みましたが、フロア内にゴールドが存在しません。 |
| *"You feel like someone is helping you."*<br>（誰かが助けてくれているような気がする。） | 「解呪の巻物」を読みました。装備中の呪われたアイテムの呪いが解けました。 |
| *"Your hands begin to glow red."*<br>（両手が赤く輝き始めた。） | 「モンスター混乱」の巻物を読んだか呪文を唱えました。次の近接攻撃が命中すると相手を混乱させます。（すでに混乱している状態で読むと紫色に光ります。） |
| *"You feel guilty."*<br>（罪悪感を覚えた。） | 祝福された、または混乱状態で「罰の巻物」を読みました。鉄球と鎖は取り付けられませんでしたが、巻物は識別されました。 |
| *"Who was that Maud person anyway?"*<br>*"As your mind turns inward…"* | 「健忘の巻物」を読みました。記憶していた呪文の一部を忘れてしまいました（祝福された巻物なら忘れずに済みます）。 |
| *"You have an uneasy feeling…"*<br>（不安な気分になった…） | 呪われた「啓蒙の薬」を飲んだか、上昇できない場所で呪われた「レベルアップの薬」を飲みました。薬は識別され、それ以外の悪影響はありません（啓蒙の薬の場合は知恵のエクササイズ値が少し下がります）。 |
| *"You feel like a hypocrite."*<br>（偽善者になったような気分だ。） | エルベレス（Elbereth）の上に立った状態でモンスターを攻撃しました。刻み文字は消滅し、属性値にペナルティを受けました（実績値が十分に高ければ一律−5、低ければ−1〜−5）。 |
| *"You feel that monsters are aware of your presence."*<br>（モンスターたちがあなたの存在に気づいた気配がする。） | モンスターがモンスター怒号（反感）の呪文を唱え、フロア中のモンスターを目覚めさせてあなたに向かわせました。 |
| *"You feel that monsters have difficulty pinpointing your location."*<br>（モンスターたちがあなたの位置を正確に捉えにくくなった気がする。） | 「幻影のクローク」の効果が発動しました。*「…no longer have difficulty…」* は効果が切れたことを意味します。 |
| *"You hear the rumble of distant thunder…"*<br>（遠くで雷鳴が轟くのが聞こえる…） | 自分のペット（または飼い慣らした生物）を殺害しました：属性値−15、幸運値−1。属性値がプラスに戻るまで祈りは失敗します。 |
| *"You feel as if you need some help."*<br>（誰かの助けが必要な気がする。） | 近くのモンスターがアイテム呪詛の呪文を唱えました：インベントリ内のいずれかのアイテムがランダムに呪われました。使用する前に祭壇などでBUCを確認してください。 |
| *"You feel the presence of evil."*<br>（悪の気配を感じる。） | 泉から敵対的な「水の魔神」が召喚されましたが、まだ視界に入っていません。接近してきています。 |
| *"You hear someone summoning something, and…"* (および *"…summoning <something>"*) | 司祭系モンスターが視界外で昆虫やヘビを召喚しました。魔法使い系モンスターの召喚では *"Monsters appear from nowhere!"*（どこからともなくモンスターが現れた！）と表示されます。 |
| *"You feel mildly hot."* / *"You feel mildly chilly."* | 火炎（または冷気）攻撃を受けましたが、自身が持つ内在耐性がそれを吸収しました。自分が思っている通りの耐性を実際に持っていることを確認できる貴重な手がかりです。 |
| *"You feel rather itchy under your mummy wrapping."* | 透明の巻物、杖、または呪文を使用しましたが、装備中の「ミイラの包帯」が透明化を遮断しました。透明にはなっていませんが、その巻物／杖が透明化であることを確認できました。 |
| *"You feel less paranoid."*<br>（被害妄想が薄らいだ気がする。） | 扉探索の効果によって、マップ上の古い不可視マーカー `I` が消去されました。モンスターがどこへ移動したかまでは分かりません。 |
| *"You feel agile! You must have been working on your reflexes!"* (および力／知恵／体力の各種) | 隠されたエクササイズ（鍛錬）システムによって能力値が上昇しました。何が鍛錬に当たるかは [能力値のエクササイズ (Exercising Your Stats)](#exercising-your-stats) を参照してください。逆に *"You haven't been working on reflexes lately"* は不摂生（アビュース）が続いたときに表示されます。 |
| *"You move very quietly."*<br>（非常に静かに移動できる。） | 「忍びの指輪」またはエルフのクロークを装備しました。（エルフの靴の場合は *"You walk very quietly"* となります。） |
| *"Wow! This makes you feel good!"*<br>（おお！ 気分が良くなった！） | 呪われていない「能力回復の薬」を飲み、低下していた能力値が1つ回復しました。 |
| *"Wow! This makes you feel great!"*<br>（おお！ 素晴らしい気分だ！） | 祝福された「能力回復の薬」を飲んですべての能力値が回復したか、あるいは魔法の泉の水を飲みました。 |

---

## 第3部：生存戦略 (Part Three: Survival)

危険なターンでゲームが一時停止したときは、まず [迫り来る死から生還する方法 (Saving Yourself from Imminent Death)](#delayed-deaths) を確認してください。通常の戦闘における鉄則は極めてシンプルです：常にHP満タンで交戦に入り、初撃の攻防を交わした段階で自分が勝てそうかどうかを冷静に判断し、勝てそうにない場合に逃げ込むべき階段や扉の場所を常に把握しておくことです。[エルベレス (Elbereth)](#elbereth) は、神への祈りや回復の薬と同じように、思考のツールキットとして常に手元に用意しておくべき奥の手です。モンスターに隣接される前に刻みましょう。

### 迫り来る死から生還する方法 (Saving Yourself from Imminent Death) {#delayed-deaths}
<!-- audit
2026-05-19:
- sliming timer is 10, not 9: make_slimed(10L,...) (uhitm.c:3199, eat.c:854, polyself.c:456, uhitm.c:3570)
- the "9-turn" impression came from the t/2 message cadence (timeout.c:391)
- cancellation prevents new infections (uhitm.c:3556-3560) but does NOT clear a running Slimed timer
- polymorph cure requires flaming() or PM_GREEN_SLIME (polyself.c:842)
- vomiting cures only SICK_VOMITABLE; Pestilence's SICK_NONVOMITABLE is unaffected (eat.c:3745-3746)
- rotted-corpse food poisoning is gated by Sick_resistance, NOT poison resistance (eat.c:1904-1914)
- Fire_resistance survives lava damage but still gets trapped: lava_effects sets utrap TT_LAVA on the fire-res branch (trap.c:6964-6968)
-->

すべての致命的な脅威が即死をもたらすわけではありません。警告メッセージを見れば、あと何ターンの猶予が残されており、どのアイテムに手を伸ばすべきかが分かります。

| 脅威 | 警告メッセージ | 猶予ターン数 | 確実な対処法 |
|---|---|---:|---|
| 石化 (Stoning) | *You are slowing down*<br>（体の動きが鈍くなってきた） | 5ターン（3ターン後に行動不能） | トカゲまたは酸性生物の死体を食べる、酸の薬を飲む、祈る（`#pray`） |
| スライム化 (Sliming) | *You are turning into a green slime*<br>（体が緑色のスライムに変化しつつある） | 約10ターン | 火で焼く、病気治療の呪文、適切な姿への変身、祈る（ゲヘナ外のみ） |
| 食中毒 (Food poisoning) | *You feel deathly sick*<br>（死ぬほど気分が悪い） | 10〜19ターン | 呪われていない超回復の薬／完全回復の薬、祝福された回復の薬、ユーカリの葉、ユニコーンの角、祈る |
| 溶岩（火炎耐性なし） | 溶岩の中に落ちた | 0ターン（即死） | 浮遊や飛行で事前に予防する |
| 溶岩（火炎耐性あり） | 溶岩の中に沈んでいく | 約12ターン | 浮遊する、テレポートする、歩いて脱出する、祈る |
| ウナギ／クラーケンの巻きつき | モンスターがあなたに巻きついてきた | 次の巻きつき攻撃が命中すると溺死 | 呼吸の魔除け、モンスターを倒すかテレポートさせる |
| 絞殺 (Strangulation) | *It constricts your throat!*<br>（喉を締めつけられる！） | 6ターン | 魔除けを外すか解呪する、祈る |

**スライム化。** 緑のスライムの攻撃を受けるか、その肉片を食べると、約10ターンのスライム化カウントダウンが始まります。**治療法：** 火でスライムを焼き払う（火の杖を自分に振る、火の巻物を自分に向かって読む、火炎の罠を踏む、赤ドラゴンの火炎ブレスを浴びる）、炎の肉体を持つモンスターやスライム耐性のある生物に変身する、あるいは「病気治療」の呪文を唱えます。**耐へんげの魔除け (amulet of unchanging)** はスライム化の感染を完全に遮断し、すでに進行中の変身をも即座に中止させます。緑のスライムを無力化（キャンセル）すると新たな感染は防げますが、すでにカウントダウンが始まっているタイマーを止めることはできません。祈りでも治療できますが、緑のスライムは祈りが神に届かないゲヘナに生息しているため、祈りを当てにしてはいけません。

**病気（食中毒）。** 腐敗した死体や古くなった死体を食べると食中毒を発症し、10〜19ターンで死に至ります（*"You feel deathly sick."*）。**治療法：** 呪われていない超回復の薬または完全回復の薬、祝福された回復の薬を飲む、ユニコーンの角を使用する（`#apply`）、祈る、あるいはユーカリの葉を食べます。毒耐性があっても食中毒は防げません。食中毒を防ぐのは「病気耐性（Sick resistance）」という独立した内在能力です。

**ペスティレンスの致死性の病気。** 食中毒よりもさらに手強い病気です：吐き戻し（嘔吐）では治癒せず、猶予ターン数は体力（Con）の値に依存します（約20＋Conターン）。**有効な治療法：** ユニコーンの角、祈り、ユーカリの葉のいずれかです。

**溶岩への沈没。** 火炎耐性がない場合、溶岩に触れた瞬間に即死し、手持ちの荷物が真っ先に燃え尽きます。火炎耐性がある場合、即死は免れますが徐々に沈んでいき、脱出までに約12ターンの猶予があります。浮遊する、テレポートする、歩いて岸へ上がる、あるいは祈りを捧げましょう。火炎耐性は火傷を防ぐだけであり、沈没そのものを止めるわけではありません。

**溺死（巻きつき拘束）。** 水中でウナギやクラーケンに巻きつかれた場合、次の巻きつき攻撃が命中すると水底に引きずり込まれて溺死します。溺死判定はウナギのマスを基準に行われるため、一度捕まってしまうと浮遊や水上歩行、荷物の重さなどは無関係になります。**生還策：** 呼吸の魔除け（または変身による水中呼吸）、水中に引きずり込まれる前にウナギを倒すかテレポートで吹き飛ばす、あるいはそもそも水域に一切近寄らないことです。詳細は前述の [溺死 (Drowning)](#drowning) を参照してください。

**絞殺。** 絞殺の魔除けを首にかけると、わずか6ターンで窒息死します。呪われていなければ即座に外してください。呪われている場合は、解呪の巻物や聖水で呪いを解くか、神に祈りを捧げましょう。

### 刻み文字とエルベレス (Engravings and Elbereth) {#engravings}

刻むコマンド（`E`）を使うことで、ダンジョンの床に文字を書き記すことができます。刻み文字にはいくつかの実践的な目的があります：**エルベレス (Elbereth)** を刻んで身を守る（次節で解説）、未識別の杖を床に試し書きして識別する（杖の章で解説）、あるいは自分の骨ファイルを見つける未来の冒険者に向けて遺言を残すことです。ここで解説する仕組みは、エルベレスに限らず *あらゆる* 刻み文字に共通して適用されます。

**筆記手段・速度・耐久性。** 何を使って文字を書くかによって、書き終えるまでの所要時間、刻み文字の消えにくさ（耐久度）、そして筆記具の摩耗の有無が決まります。

| 筆記手段                  | 所要時間      | 耐久度         | 備考                              |
| ------------------------- | ------------- | -------------- | --------------------------------- |
| 指（埃に書く）           | 即座 (Instant)| 脆弱 (Fragile) | モンスターが踏むと文字がかすれる  |
| 呪われていないアサメ      | 即座 (Instant)| 半恒久         | 刀身が鈍らない（呪われたアサメは鈍る） |
| その他の刃物武器          | 数ターン      | 半恒久         | 中断される恐れあり。強化値が−3まで低下する。+0の刃物では「Elberet」で止まり、+1以上なら最後まで書き終えられる |
| 硬い宝石、またはダイヤモンド | 数ターン   | 半恒久         | 中断される恐れあり                |
| 採掘の杖                  | 即座 (Instant)| 半恒久         | 扱いやすくバランスが良い          |
| 火の杖、または雷の杖      | 即座 (Instant)| 恒久 (Permanent)| 床に文字を焼き付ける              |

3段階の耐久度は、通常の摩耗に対して文字がどれだけ耐えられるかに対応しています：

- **脆弱（埃・砂塵）。** モンスターがそのマスを踏むたびに、文字が1文字ずつかすれて消えていきます。埃に書いたエルベレスは、そのマスにモンスターが踏み込まない限り持続します。
- **半恒久（床に削り刻んだ文字）。** モンスターが踏むごとに1/26の確率で文字が欠けます。埃よりもはるかに長持ちしますが、永久ではありません。
- **恒久（焼き付けた文字）。** 通常の状況下では決して自然摩耗しません。氷のマスや魔法攻撃によってのみ損傷を受けます。

**手作業での彫刻は中断されるリスクがある。** 複数ターンを要する手作業の筆記手段（アサメ以外の刃物、宝石など）は、1文字書くごとに1ターンを消費します。もし文字の途中で何か（敵の攻撃、モンスターの視界への侵入、地震の発生など）によって作業が中断された場合、中途半端に残された未完成の文字列は何の効果も発揮しません。即座に完了する手段（各種の杖、埃への指書き、呪われていないアサメ）であれば、たった1回のアクションで安全に書き終えることができます。

**状態異常と書き損じ。** 盲目、混乱、気絶、または幻覚の状態にあるときは、文字ごとにスペルミス（誤字）を起こす確率が生じます。この文字の乱れは、火の杖による焼き付けを含む *あらゆる* 筆記手段に適用されます。（硬い筆記具で免除されるのは、埃や血の表面かすれ判定だけです。）綴りを間違えた刻み文字には何の魔力も宿りません。これはエルベレスを刻む際に最も致命的な問題となります。

**上書きと追記。** すでに存在する刻み文字に文章を追記することは可能ですが、エルベレスのような特定の聖句の魔力を発揮させるには、床の文字列が *厳密に* その単語のみでなければなりません。そのため、文字を追記すると結界としての効果は失われてしまいます。効果を更新したい場合は、そのマスを上書きするか、別の新しいマスを選んで刻んでください。

**覚えておくべき2つの特別な刻み文字。** ダンジョン内で見つかる刻み文字の大半は、ランダムな雰囲気描写（落書き、過去の冒険者が残した「elbereth」など）です。しかし、以下の2つの特定のメッセージは、ダンジョン生成時に配置された **罠の目印 (trap markers)** です。*"Ad aerarium"*（ラテン語で「宝物庫へ」の意）は、**宝物庫テレポート** または **階層テレポート** の罠が潜む隠し小部屋の目印です。宝物庫テレポートは、同一フロアにあるクロイソスの2×2マスのゴールド部屋へと転送してくれる使い切りの罠です。金貨を回収し、番兵が現れる前に脱出しましょう。階層テレポートはランダムな深さの階層へ飛ばされるため、瞬間移動制御がないと危険です。*"Vlad was here"*（ヴラド参上）は、**落とし扉** が仕掛けられた隠し小部屋の目印です。どちらのメッセージもメッセージログで見落としやすいため、見かけたら慎重に調査し、罠の向こう側で待ち受ける事態に備えましょう。

#### エルベレス (Elbereth)
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

##### 単語の由来 (Where the word comes from)

*Elbereth*（エルベレス）はシンダール語で「星々の女王」を意味し、J.R.R.トールキンの『シルマリルの物語』に登場する最高位のヴァラであり天上に星々を撒き散らした **ヴァルダ・エレンターリ (Varda Elentári)** のエルフ名です。『指輪物語』において、エルフたちは邪悪に対する聖なる守護を求めて彼女の御名を呼び唱えます。フロドは風見荘で「オ・エルベレス！ ギルソニエル！」と叫んで魔王を後退させ、サムはシェロブの暗黒の巣窟でガラドリエルの玻璃瓶の光を輝かせるために彼女の名に祈りを捧げました。NetHackはこの設定をそのままゲームに採用しています：ダンジョンの床にヴァルダの名を刻みつけることは、絶対安全な聖域を求めて上位の超越者へと救いを求める行為なのです。

> *以下の仕組みは、Kate Nepveu氏の「Elbereth FAQ」に着想を得ています。Kate氏は、数十年におよぶコミュニティのスポイラーを保存し続けてきた長期アーカイブ「steelypips.org」の管理者でもありました。*

##### 聖なる結界 (The ward)

床に **Elbereth** の文字を刻むことで、強力な防護結界が生成されます。エルベレスが刻まれたマスの上にプレイヤーが立っている限り、大半のモンスターは近接攻撃を仕掛けてくることができず、苛立ちながら周囲をうろうろと彷徨うだけになります。この結界は、自分で書いたものであっても、最初から床に書かれていたものであっても同様に機能します。また、書いた手法（埃、削り傷、焼き付け）は結界の防護力自体には一切影響せず、文字がどれだけ長く残り続けるか（耐久度）の違いに過ぎません。

##### 結界の絶対ルール (Rules of the ward)

- **マスの上に立っている間だけ効果がある。** マスから一歩でも足を踏み出せば防護は途切れます。再びそのマスの上に戻れば結界の効果が復活します。
- **厳密に完全な単語でなければならない。** "Elbereth" の8文字きっかりでなければならず、文字の不足や余計な文字は一切許されません。状態異常による誤字や、他の文字列が追記されたものは無効となります。
- **一部のモンスターは結界を完全に無視する。** `@` で表されるすべての存在（人間、エルフ、プレイヤー系キャラクター）、霊界の死の騎士（Riders）、天使、ミノタウロス、固有の固有名を持つモンスター（クエストの宿敵、ヴラド、魔法使い）、店主、番兵、および **盲目のモンスター** は、結界を意に介さず平然と踏み越えて攻撃してきます。また、逃げ道のない袋小路に追い詰められたモンスターも同様です：逃げ場を失った怪物は、無抵抗で立ち尽くすくらいなら死に物狂いで反撃してきます。
- **ゲヘナ、属性の諸平面、霊界では機能しない。** [城 (The Castle)](#the-castle) より下の階層では、エルベレスの神聖な力は届かず、すべて自分の実力だけで切り抜ける必要があります。

##### エルベレスの御名を汚すこと（極めて重要）(Defiling the name of Elbereth (important))

もしエルベレスの上に立った状態でモンスターに対して何らかの攻撃を行った場合（近接攻撃、投擲武器、あるいは杖の発射を問わず）、その対象が結界を恐れるはずのモンスターであったり友好的な生物であったなら、刻み文字は **どのように書かれたものであっても即座に完全消滅します。** 火の杖で床に恒久的に焼き付けたエルベレスであっても、たった一振りの攻撃で跡形もなく消え去ります。同時にプレイヤーは「偽善者になったような気分だ (You feel like a hypocrite)」というメッセージとともに **属性値に手痛いペナルティを受け**、*"The engraving beneath you fades."*（足元の刻み文字が薄れて消えた）と表示されます。属性値の実績が十分に高ければ一律で−5、そうでなければランダムに−1〜−5の低下を被ります。

耐久度の表にこの例外は書かれていません。「恒久」や「半恒久」とは、あくまで足踏みや風化といった *受動的な摩耗* に対する耐性のことです。プレイヤー自身の敵対行動は、どんな耐久度の文字であっても一瞬で消滅させます。したがって、エルベレスは **完全に防御専用の結界** として使う必要があります。体力を回復する、薬を飲む、巻物を読む、装備を整え直す、体勢を立て直すといった時間稼ぎに活用してください。結界の上からの攻撃は禁忌であるため、反撃に転じる際は必ずマスから一歩踏み出してから戦いましょう。

##### 実践的な活用法 (Practical use)

緊急事態に陥ったら、まずは指を使って埃の中に素手で Elbereth と書きましょう。アイテムを消費せずに行えますが、1回の手番（アクション）を消費するため、モンスターに接触される前に書く必要があります。大半のモンスターは怯えて距離を取り、落ち着いて次の行動を選ぶ猶予が生まれます。目先の危機を脱したら、埃の結界を次回のために温存する（モンスターがそのマスを踏まない限り文字は残ります）か、より耐久性の高い手段で書き直しましょう。

アイテムの保管場所、安全な休息用の中継地点、あるいは通路での迎撃拠点として恒久的な安全地帯を作りたい場合は、火の杖や雷の杖を使って床に文字を焼き付けましょう。1ターンで完了し、敵に中断されるリスクがなく、通常の足踏みで消えることもありません。ただし、盲目、混乱、気絶、幻覚の状態にあると綴りを書き損じる恐れがあります。半恒久的な彫刻（アサメ、通常の武器、宝石、採掘の杖）は中間の選択肢です：耐久性はありますが、時間のかかる手作業の方法は文字の途中で中断される危険があります。

浮遊している間は、指や武器を使って床に文字を書くことはできません。しかし、火、雷、冷気、採掘の杖であれば、空中からでも下を向いて床に刻むことができます。「足元の床に向かって身振りをした」というメッセージが出ますが、焼き付けは正常に完了します。

**祭壇や墓の上には絶対に文字を刻んではいけません。** 祭壇の上で何かを書こうとすると（エルベレスであっても）、**文字は一切刻まれず**、神を冒涜して激怒させます：自分の祭壇なら知恵と属性値を失い、他の祭壇なら幸運を失います。祭壇の上でモンスターに追い詰められたからといって、反射的にエルベレスを床に殴り書きしてはいけません。必ず一歩降りてから書きましょう。また、荒らされていない墓の上で武器や杖を使って文字を彫ると墓荒らしとなり、グールが召喚されます（素手の指なら墓石の表面を汚すだけで済みます）。なお、泉のあるマスには最初から文字を刻むことはできません。

床に置かれた **怪物を怯えさせる巻物 (scroll of scare monster)** は、エルベレスのさらに強力な上位互換として機能します。その巻物の上に立つだけで大半のモンスターは間合いを取って接近できなくなりますが、エルベレスに対して以下の3つの決定的な優位性を持っています：エルベレスが無効化されるゲヘナや霊界でも問題なく機能すること、エルベレスを平然と通過してくるミノタウロスや盲目の敵をも退けること、そして刻み文字ではないため **巻物の上に立ったまま自由に攻撃を仕掛けても消滅せず、偽善者の属性ペナルティも一切受けないこと** です。巻物は自然摩耗せず、自分がマスから離れてもそのマスは敵の進入禁止エリアとして残り続けます。唯一の弱点は「拾い上げ」にあります：床から拾おうとすると高確率で崩壊して消滅します（呪われた巻物は1回目、呪われていない巻物は2回目で灰になります）。そのため、安全地帯として固定したい場所に置いて使用してください。城の「願いの杖」が入った宝箱の真下に呪われた怪物を怯えさせる巻物が敷かれているのは、まさにこの防衛機能のためです。また、店の中でも識別テクニックとして利用できます：未識別の巻物の上に乗り、連れているペットが嫌がって後ずさりしたら、それは怪物を怯えさせる巻物であり、拾い上げるリスクなしに安全に識別できます。

### 戦闘の技術 (The Art of Combat)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Armor donning: helmets/gloves 1 turn, boots 2, cloaks/shields 0 (per-item delay, objects.h BOOTS/SHIELD/CLOAK macros). Was "1 each".
- Speed table: gnome/kobold/dwarf are 6 (not 12); fire ant 18 (not 12); molds 0 and other fungi 1 (not 6); humans/elves are the 12 tier (monsters.h; NORMAL_SPEED=12, permonst.h:80).
- Encumbrance is applied AFTER the Fast/Very-Fast bonus, cutting the boosted total (allmain.c:121-149). Was "before".
- Samurai multishot bonus is ya+yumi (bow) only, not shuriken (dothrow.c:73-75).
- Nagas have no M1_REGEN; removed from the "regenerate every turn" list (monsters.h).
-->
<!-- audit
2026-05-20:
- waking a sleeping monster via attack invokes wakeup() (uhitm.c:250, 305, 1403, 1926, 5213, 5590, 5694, 5764, 5774); if the struck monster was sleeping AND not MS_SILENT AND not helpless, growl() fires (mon.c:4353-4356 wakeup)
- growl() calls wake_nearto(mtmp->mx, mtmp->my, mtmp->data->mlevel * 18) (sounds.c:421) — radius approx sqrt(mlevel * 18) in tiles
- Knight caitiff penalty: -1 alignment for attacking helpless or fleeing non-undead monsters when Lawful (uhitm.c:336-341)
- Samurai dishonor penalty: -1 alignment for attacking peacefuls (uhitm.c:342-345)
- Samurai poisoned-weapon penalty: -sgn(u.ualign.type) alignment (uhitm.c:1521)
- Quest entrance requires alignment record >= MIN_QUEST_ALIGN = 20 AND ulevel >= MIN_QUEST_LEVEL = 14 (quest.h:43-45)
2026-05-18:
- to-hit factors: XL, Str, Dex, Luck, enchantment, AC (find_roll_to_hit)
- abon includes both Strength AND Dexterity; Dex 25 yields +11 (weapon.c:950-988)
- dbon has a Strength cap: max +6 at STR 18/100 or higher (weapon.c:993-1015)
- two-handed weapons get a 3/2 Strength-bonus multiplier (weapon.c bhitval two-handed branch)
- conflict requires mutual sight and a Cha-vs-Lvl resist roll: resist_chance = min(19, Cha - m_lev + XL) (mondata.c:1607-1612)
- two-weapon and shield are mutually exclusive
- Expert two-weapon: Rogue and Samurai only (u_init.c skill tables)
- Rangers CAN two-weapon but only unskilled (-9 to-hit, weapon.c:1587); can_twoweapon has no role gate (wield.c:766). Skill_Ran lacks the entry so it's untrainable, not forbidden.
- two-weapon penalty is a flat table: -9/-7/-5/-3 to-hit, -3/-1/0/+1 damage
- Luck to-hit contribution is sgn(Luck)·((|Luck|+2)/3), capping at ±5 (uhitm.c:377); Luck itself ranges ±10, ±13 with luckstone
- monsters use m_move (phase 3) then mattacku/castmu (phase 4) on the same turn (monmove.c:911, 943-944, 971)
- no "free extra step" change exists; that earlier claim was fabricated
- strategy aligned with NetHackWiki Corridor, Movement tactics, Twoweapon: corridor chokepoint as the single biggest tactical principle, two-weapon penalty tied to skill rank (https://nethackwiki.com/wiki/Corridor, https://nethackwiki.com/wiki/Movement_tactics, https://nethackwiki.com/wiki/Twoweapon)
-->

迷宮における最も重要な戦闘技術は、「戦うべきではない状況を弁えること」です。2番目に重要な技術は、「いざ戦うと決めたら、確実に、そして痛烈無比な打撃を叩き込むこと」です。

#### 命中判定の計算 (To-Hit Calculation)

武器を振るうたびに20面ダイス（d20）が振られ、白兵戦において重要となるあらゆる要素によって修正されます：

- あなたの経験レベル（高レベルほど多くの修羅場をくぐり抜けています）
- 武器の強化値（+7の [エクスカリバー (Excalibur)](#excalibur-artifact) は目に見えて命中率が跳ね上がります）
- あなたの幸運（世界が味方します。幸運値自体の範囲はもっと広いですが、命中への寄与はおよそ±5で頭打ちになります）
- 筋力と敏捷性のボーナス（筋骨隆々たるパワーと身のこなしの俊敏さ、両方が影響します）
- モンスターのAC（相手のACが低いほど、攻撃を当てるのが難しくなります）

基本値の1に、経験レベル（XL）、筋力と敏捷性のボーナス、幸運値の約1/3、武器の強化値と武器スキルを足し合わせ、さらに標的のACを加算します。d20の出目がその合計値 *未満* であれば攻撃が命中します。相手のACがマイナス（良質）であるほど命中目標値が引き下げられるため、地下深くに潜るにつれて武器の強化値と武器スキルの重要性が飛躍的に高まります。

#### ダメージの計算 (Damage)

基本ダメージは、使用する武器の種類と、標的となるモンスターのサイズ（小型か大型か）によって決定されます。多くの武器はどちらかのサイズに特化したダメージ設定を持っています：コボルドには短い刀剣、オーガには両手持ちの大武器が効果的です。基本ダメージに以下の補正値が加算されます：

- 武器の強化値（1ポイントにつき+1）
- 筋力ボーナス（両手持ち武器の倍率適用前で最大+6）
- 武器スキルボーナス（習熟度ランクによる）
- 特殊ボーナス（銀製武器による銀ダメージ、アーティファクトの固有ボーナスなど）
- **両手持ち武器** は、筋力によるダメージ加算分に50%のボーナス（1.5倍）を得られるため、盾のスロットを犠牲にするだけの絶大な見返りがあります。

筋力が18/100に達している場合、両手剣では通常の筋力ボーナス+6が+9へと跳ね上がります。強化値や武器スキルを加味する前の素の状態で、両手剣のd12+9は長剣のd8+6よりも1撃あたり平均約5ポイント高い強烈なダメージを叩き出します。

#### ACと防御力 (AC and Defense)

あなたのAC（アーマークラス・防御指数）は、モンスターの攻撃が *あなたに* どれだけ命中しやすいかを決定します。ACは10（防具を一切身につけていない無防備な状態）から始まり、防具を装備するにつれて数値が下がっていきます。数値が低ければ低いほど（マイナスが大きいほど）強固です。「ノームに殴り倒される」初心者段階から「あらゆる物理攻撃を寄せ付けない」段階への道のりは以下のようになります：

| 段階           | 典型的なAC | 防御水準                |
| -------------- | ---------- | ----------------------- |
| ゲーム開始直後 | 8〜10      | 気合と根性のみ          |
| 迷宮序盤       | 2〜5       | 基本的な防具一式を装備  |
| 迷宮中盤       | -5〜0      | 強化された鎧＋クローク  |
| 迷宮終盤       | -20〜-10   | 歩く戦車                |

マイナスのACは攻撃を受けるたびに個別にダイスロールされ、モンスターのレベルも命中率に加算されます。AC -20であってもオーガの攻撃は約1/4の確率で命中し、レベル15の強力なモンスターなら約2/3の確率で当ててきます。さらに終盤の多くの脅威（ブレス攻撃、呪文、凝視攻撃など）はACを完全に無視して襲いかかってきます。どれほど強固な鎧で身を固めていても、吸魔の怪物（ディスエンチャンター）に出遭えば一瞬で装備の強化値を吸い取られて台無しにされます。

**7つの部位、数値を下げる4つの道。** 同時に身につけられる防具スロットは7つあります：鎧（スーツ）、クローク、兜、手袋、靴、盾、シャツです。すべてのスロットを通常の防具で埋めるだけで、AC 10からおおよそAC 0前後まで下げることができます。そこからさらにマイナスのACへと進む道は、防具の強化（巻物によるエンチャント）、通常の防具から魔法の防具への換装（多くの魔法防具はAC補正に加えて内在能力も付与してくれます）、そして司祭から購入する外在的防御（プロテクション）です。部位ごとの詳しい解説は [防具とAC (Armor and AC)](#armor-and-ac) を参照してください。

**危険な部位から先にテストする。** 靴と手袋は、装備する前に祭壇の上に置くか、ペットが嫌がって踏むのを避けるか確認してください。ACが6より悪く、呪いの鑑定手段が手元にない状況であれば、通常の鎧、兜、盾、クロークは未鑑定のまま装備してしまっても構いません。呪われて脱げなくなるリスクよりも、防具を着けずに無防備でいるリスクの方がはるかに高いからです。詳しい手順は [実践的識別戦略 (A Practical Identification Strategy)](#a-practical-identification-strategy) を参照してください。

**防具の着脱にはターン数を要し、重ね着の順序がある。** 防具は `W` キーで着用し、`T` キーで脱ぎます。シャツが最内層、次が鎧、一番外側がクロークという順序になっているため、内側の防具を着脱するには上に重ね着している防具を先に脱ぐ必要があります。金属製の鎧は着脱に **5ターン** を要します。革鎧は3ターン、ミスリル鎧は1ターンです。兜と手袋はそれぞれ1ターン、靴は2ターンかかります。クローク、盾、シャツは即座（0ターン）で着脱できます。アロハシャツからクロークまで全身を着替えると6ターンも完全に無防備になり、その間モンスターから一方的に攻撃を受けるため、着替えは安全な部屋の中や背後を通路で塞いだ安全地帯で行ってください。

#### 速度 (Speed)

**交戦する前に速度比を計算せよ。** 戦闘において最も実用的な指標は、「モンスターの速度」を「あなたの実効速度」で割った比率です。この比率こそが、あなたが1回行動する間に相手が何回行動できるかを表しています。基本速度12の主人公が速度18のケンタウロスと対峙した場合、比率は 18 / 12 = 1.5 となります。つまり、あなたが2回攻撃を振る間に相手は3回攻撃を叩き込んでくるため、正面からの近接殴り合いでは確実に撃ち負けます。しかし「韋駄天の靴 (speed boots)」（実効速度約20）を履けば比率は 0.9 に逆転し、こちらが主導権を握る戦いになります。速度36の風のエレメンタルに対しては、加速なしで3.0、韋駄天の靴を履いていても1.8であり、徒歩での殴り合いは依然として無謀です。遠距離攻撃で倒すか、戦わずに逃げるべきです。速度比が1.0を超える相手との戦いは、開幕の猛攻で瞬殺できない限りジリ貧の消耗戦になります。比率が1.0未満の相手なら「引き撃ち（カイト）」が可能ですので、通路へと後退しながら相手が歩み寄る隙に攻撃を当てましょう。自分より素早いモンスターを即座に倒せない場合、開けた広い部屋で逃げ回ってはいけません。追いつかれて背後から殴られ続けるだけです。扉口、閉じた扉、あるいは階段を使って、同時に攻撃してくる敵の数を1体に絞り込みましょう。

**速度の内部メカニズム。** あなたの基本速度は **12** であり、あらゆる行動コストも12です。各生物は内部カウンターを持っており、誰も行動コストを支払えない状態になると、全生物のカウンターが各自の「速度」分だけ加算されます。誰かが行動可能になるまでこの加算が繰り返されます。足の速い生物ほどカウンターが頻繁に上限に達するため、前述の速度比がそのまま行動回数の差として現れるのです。モンスターの基本速度は図鑑に記載されています：ゾンビは6、人間は12、ケンタウロスは18、吸血コウモリは20、風のエレメンタルは36です。

**加速は確率的に追加行動を付与する。** 一部の死体を食べて得る「高速 (Fast)」は、3回に1回ほどの割合で内部カウンターに+12のボーナスを付与し、平均実効速度は約16になります。「超高速 (Very Fast)」（韋駄天の靴、スピードの薬、自己加速の呪文）は、3回に2回の割合で同様のボーナスを付与し、平均実効速度は約20に達します。この抽選は時間枠（アロケーション）ごとに行われるため、緊張感ある特定の1ターンで必ず追加行動が得られるとは限りませんが、連続した多くの行動全体で見れば極めて正確に平均値通りに機能します。「超高速」は「高速」と重複加算されず、より優れた状態（超高速）が優先されます。韋駄天の靴は最も手軽で永続的な加速源です：一度履くだけで、薬や魔力を加速のために消費し続ける必要がなくなります。

**荷物の重さ（負荷）は割り当てポイントを直接削る。** 負荷状態になると、内在ボーナスを加算した後の行動ポイントが直接減算され、実効速度が低下します：

| 負荷状態      | 基本ポイント | 実効速度        |
| ------------- | ------------ | --------------- |
| 負荷なし (Unencumbered) | 12           | 100% (通常)     |
| 重荷 (Burdened)         | 9            | −25%            |
| 圧迫 (Stressed)         | 6            | −50%            |
| 過重 (Strained)         | 3            | −75%            |
| 超過重 (Overtaxed)      | 2            | −83%            |

「圧迫」の状態では、たとえ「高速」の内在能力を持っていても、何も背負っていない通常のキャラクターよりも足が遅くなります。「圧迫」になると速度6のゾンビと同速になり、「過重」になるとゾンビがあなたの1歩に対して2回行動してきます。理想的には「軽量化の鞄」を活用して、常に「負荷なし」の状態を維持しましょう。

```{=latex}
\needspace{10\baselineskip}
```

**代表的なモンスターの速度一覧。**

| 速度  | 段階                 | 代表的なモンスター                                |
| ----- | -------------------- | ------------------------------------------------- |
| 0〜1  | 這うような鈍足       | モールド、大半の菌類（キノコ）                    |
| 6     | 遅い                 | ゾンビ、ノーム、コボルド、ドワーフ                |
| 12    | 通常（プレイヤー基本）| 人間、エルフ、インキュバス／サキュバス            |
| 18    | 速い                 | ケンタウロス、キリン、兵隊蟻、火蟻                |
| 20    | 超高速               | カラス、吸血コウモリ                              |
| 22    | 超高速               | コウモリ、巨大コウモリ、蒸気の渦、炎の渦          |
| 24    | 極めて速い           | 女王蜂                                            |
| 36    | 徒歩では追いつけない | 風のエレメンタル                                  |

韋駄天の靴は、俊足モンスターたちに対抗する上でそのスロットに見合う絶大な価値を発揮します。速度6のゾンビ相手なら速度比は0.5から0.3に縮まる程度ですが、速度18のケンタウロスに対しては1.5から0.9へと激変し、追撃されて討ち死にするか、決闘を制して勝利するかの決定的な差となります。

#### 二刀流戦闘 (Two-Weapon Combat)
<!-- audit
2026-05-19:
- Rogue and Samurai are the only roles reaching Expert in P_TWO_WEAPON_COMBAT (u_init.c skill tables).
- Valkyrie and Knight cap at Skilled (u_init.c skill tables).
- Barbarian caps at Basic (u_init.c skill tables).
- Ranger has no P_TWO_WEAPON_COMBAT entry, so two-weapon is untrainable (unskilled, -9 to-hit), NOT forbidden — can_twoweapon has no role check (wield.c:766).
- Penalty structure is a flat negative replacement per skill tier: to-hit -9/-7/-5/-3, damage -3/-1/0/+1.
- Penalties are not a "split" between the two weapons. (weapon.c:1576-1600 hit-bonus and 1676-1695 dam-bonus apply the same flat penalty per-strike — no halving)
-->

一部の役職は左右の両手に1本ずつ武器を持って戦うことができます。見た目にも華やかであり、1ターンに2回の攻撃を繰り出すことができます。それぞれの攻撃にはスキルランクに応じた一律の命中率およびダメージのペナルティが課されます（未熟＝命中−9／ダメ−3、入門＝−7／−1、熟練＝−5／0、達人＝−3／+1）。また、両手とも近接武器でなければなりません。盾、射撃武器、投擲武器との併用は不可能です。二刀流スキルで「達人 (Expert)」まで到達できるのは **盗賊 (Rogue)** と **侍 (Samurai)** のみです。ワルキューレと騎士は「熟練 (Skilled)」、野蛮人は「入門 (Basic)」が上限となります。レンジャー、治療師、武闘家、魔法使いはこの戦闘スタイルを習得できません。

**2撃目が利益を生む状況。** 2回目の追加攻撃がペナルティを補って余りある価値を発揮するのは、すでに基礎命中率が十分に高く、1撃あたりのダメージが十分に出ている場合に限られます。「達人」（−3/+1）のランクで十分に強化された武器を持ち、標準的なACの敵と対峙する場合、侍の「刀＋脇差」の二刀流は刀単体をほぼ毎ターン上回る総ダメージを叩き出します。「熟練」（−5/0）の段階では、計算上ほぼ五分五分（トントン）です。「熟練」未満ではペナルティが恩恵を食い潰してしまうため、騎士や野蛮人は1本の良質な武器に専念した方がはるかに有利です。二刀流スキルのない役職にとって、両手持ち武器による筋力ダメージ1.5倍ボーナスは極めて強力な対抗選択肢となります。

**二刀流のセットアップ手順。** 逆手（オフハンド）専用の装備コマンドは存在しません。スワップコマンドを使って「副装備スロット」に武器をセットすることで実現します。まず逆手に持ちたい武器を `w` で手に持ち、`x` キーを押してそれを副装備スロットへと退避させます。次にメインの主武器を `w` で手に持ち、最後に `X`（大文字、二刀流切り替えトグル）を押して二刀流戦闘を開始します。もう一度 `X` を押せば片手持ちに戻ります。逆手の武器は必ず片手持ち近接武器でなければなりません。逆手の武器が呪われている状態で二刀流を開始しようとすると、手から滑り落ちて床に落下します。

#### 遠距離戦闘 (Ranged Combat)

離れた間合いから攻撃することは、迷宮における最大の戦術的アドバンテージの1つです。モンスターが距離を詰めるために費やすターンは、すべてあなたが安全な位置から敵のHPを削るためのターンになります。レンジャーや侍は弓矢を主軸として生きていますが、どの役職であっても矢筒（クィヴァー）を設定して `f` キーに手を伸ばすことができます。そのツールキットは以下の通りです：

**発射・投擲・スワップのコマンド。**

- **`t`** は **投擲 (throw)**：インベントリからアイテムを選び、方向を指定して投げます。
- **`f`** は **発射 (fire)**：**矢筒 (quiver)** に装填されているアイテムを、確認プロンプトなしで即座に撃ち出します。一度設定すれば、`f` を連打することが最も素早い遠距離攻撃手段となります。
- **`Q`** は **矢筒の設定 (quiver)**：デフォルトで撃ち出す矢弾の束を選択します（レンジャーなら矢、盗賊なら短剣、侍なら和矢や手裏剣）。ゲーム開始時に一度設定しておきましょう。
- **`x`** は主武器と副武器の **スワップ (swap)**：弓を手に持ち、近接武器を副装備スロットにセットしておけば、`x` を押すだけで両者を瞬時に切り替えることができます。レンジャーの典型的な立ち回りは、「離れた距離から射撃し、敵が接近したら `x` で短剣に切り替えて刺し、敵が倒れたら再び `x` で弓に戻す」という流れるような連係です。

**射撃武器と弾薬。** 弓類（普通の弓、エルフの弓、オークの弓、和弓）は矢を射ちます。クロスボウはボルトを射ちます（1発あたりの威力は高いですが発射が遅く、連射ボーナスを得るには筋力18、ノームなら筋力16が必要です）。スリングは石や宝石を投石します。長柄武器（ポールアーム）は `a`（適用）コマンドを使うことで、2マス離れた間合いから攻撃できます。また、短剣、ダーツ、手裏剣、投槍、ブーメランなどは発射具なしで直接素手で投擲できます。

**射線を確保する。** 飛び道具は直線状にまっすぐ飛ぶため、角を曲がって飛ぶことや、閉じた扉口を斜めにすり抜けて飛ぶことはできません。モンスターがジグザグに通路を曲がって進んでくる場合は、射線が開けるマスまで少し前進して待ち構えましょう。飛び道具は弾道上にある最初の固形物に命中して止まります：もしあなたと敵の間にペットが挟まっていた場合、ペットに矢が刺さってしまいます。同じルールが杖の光線や呪文の光線にも適用されます。

**連射（マルチショット）。** 適切なスキルランクと役職条件を満たしていれば、たった1回の `f` コマンドで1ターンに複数の飛び道具を同時に撃ち出すことができます。レンジャーは短剣以外のあらゆる射撃武器で+1発、盗賊は投擲短剣で+1発、侍は和弓と和矢の組み合わせで+1発のボーナスを得られます。スキルが「熟練」なら+1発、「達人」なら+2発が追加され、手に装備した「ディアナの長弓 (Longbow of Diana)」はさらに+1発を加算します。「達人」かつ合致する役職であれば、ゲームは1発から最大発射数までの間でランダムに弾数を決定します。達人レンジャーなら1ターン平均約2.5発の矢を放ちます。

**矢弾の節約。** 矢やボルトは命中するたびに破損する確率を持っています：+0の矢弾はおよそ67%の確率で壊れ、+2まで強化された矢弾なら破損率は約25%まで激減します。普段の連射スキルの鍛錬には拾った安い矢を使い、+2に強化された貴重な矢弾は強敵との決戦のために温存しましょう。ダンジョン上層を抜ける段階で30本ほどの破損しない+2の矢を確保できたレンジャーは、長引くボス戦でも弾切れを起こさずに優位を維持できます。

#### 賢い戦い方 (Fighting Smart)

ダンジョンは臆病さ、狡猾さ、そして器物損壊に対して惜しみない報酬を与えます。戦いが始まる前に、あらかじめ勝負を不公平なものにしておきましょう。

##### 接触前の位置取り (Position before contact)

**通路を活用する。** 通路の中では、モンスターは1体ずつしかあなたに接近できません。近くに一本道の狭路（チョークポイント）があるなら、開けた広い部屋で大群を相手に戦ってはいけません。

**接触する前に戦うマスを決める。** 広い部屋を横切ってくるモンスターを見かけたら、敵に向かって歩いてはいけません。自分が迎撃拠点にしたい通路や扉口に向かって後退してください。敵よりも1ターン早くそのチョークポイントに陣取れば、自分の土俵で迎え撃つことができます。

**角（コーナー）を曲がる。** 接近してくるモンスターは、角を曲がるために1回のアクションを消費します。あなたの隣のマスに曲がり込んできたモンスターはその手番内では攻撃を繰り出せないため、必ずあなたが先制攻撃を加えることができます。

**交戦前に速度を比較する。** 相手の速度をあなたの速度で割れば、あなたが1回行動する間に相手が何回動くかが分かります（[速度 (Speed)](#speed) を参照）。比率が1.0を超える場合、長期戦になれば確実に不利になるため、速攻で叩き伏せるか、杖を撃ち込むか、あるいは接触される前に逃げてください。比率が1.0未満なら、あなたのあらゆる歩みがタダの追加行動となります。

**背後に必ず退路を確保しておく。** 階段、安全が確認された通路、エルベレスを刻んだマスなど、退避先へ通じるマスを背後に少なくとも1つ常に空けておきましょう。階段はその中でも最高の退避場所です。大半のモンスターは階上へ追ってきませんが、兵士、警備員、吸血鬼、トロール、レイス、インプなどは隣接していると階段を昇って追撃してくることがあります。なお、階段を降りて元のフロアに戻る際は、残りの敵集団が階段の周囲で待ち構えていることを想定しておきましょう。

**扉と斜め移動。** 扉口を斜めにすり抜けて移動することはできません。出入りは必ず縦横（直交方向）に行う必要があります。**扉を閉める**（`c`＋方向）ことで、扉を開ける知恵や手を持たないモンスター（大半の動物系を含む）の追撃を完全に遮断できます。背後の扉を閉めれば、追ってきた猛獣は向こう側に閉じ込められ、その間にゆっくり休息して体力を回復できます。また、扉を閉めることでペットの追従を一時的に遮断し、1ターンだけ単独で行動したい場合にも便利です。

**跳躍手段があるなら跳ぶ。** 跳躍の呪文、飛び跳ねる靴、あるいは騎士固有の跳躍能力があれば、`#jump` コマンドで1ターンに数マスを一気に跳び越えることができます。自分より足の速いモンスターから逃げる、敵の機会攻撃を受けずに通路やエルベレスのマスへ退避する、既知の罠を飛び越える（火炎の罠やレベルポータル、倉庫番の穴を除く）、内在能力を得られる死体を食べる前に「満腹 (Satiated)」状態を急いで消費する、あるいはメデューサの島の水路を跳び越える際に極めて重宝します。

##### 戦闘中の立ち回り (During the fight)

**算定が成り立つときだけ殴り合う。** あなたがそのモンスターを倒すのに何ラウンド必要か、そして相手があなたを倒すのに何ラウンド必要かを瞬時に見積もってください。あなたのターン数の方が少なければ殴り合いましょう。相手のターン数の方が少ないなら、即座に退却してください：後退に費やす1ターンは、死ぬことに比べれば遥かに安いコストです。

**間合いを詰められる前に痛めつける。** 接近戦での火蟻は恐ろしい脅威です。しかし、接近される前にすでに遠距離から杖で3回撃ち抜かれた火蟻は、ただの温かい死体に過ぎません。具体的な遠距離攻撃の手段は [遠距離戦闘 (Ranged Combat)](#ranged-combat) を参照してください。

**ペットの射線を塞がない。** モンスターの隣にペットが陣取れば、敵の攻撃の一部を引きつけてくれ、さらにペット自身の攻撃も加わります。ペットの接近ルートを塞いでしまうのではなく、ペットが戦闘に参加できるように位置を調整しましょう。

**眠っている部屋は決して安全ではない。** あなたを視界に捉えているモンスターは、毎ターン1/7の確率で目を覚まします。犬系や人間系モンスターは視界に入った瞬間に即座に覚醒します。「忍び足（ステルス）」があればこの自然覚醒を防ぐことができます。1体の敵を攻撃すると標的は目を覚まし、その威嚇の咆哮（growl）によって周囲の眠っているモンスターも次々と目を覚まします（ノームなら約4マス、より大型のモンスターならさらに広範囲に届きます）。敵が密集した部屋では、2撃目を振る頃には部屋全体を巻き込んだ大乱闘に発展します。まずは通路へと **後退して** 敵を1列に並ばせて1体ずつ各個撃破するか、[エルベレス (Elbereth)](#elbereth) を刻んで群がる敵を結界の周囲に釘付けにしましょう。その上で、結界から一歩踏み出して1体ずつ始末してください（刻み文字の上から攻撃するとエルベレスが汚されて消滅します）。

##### 戦況が悪化したとき (When the fight goes badly)

**逃げ時を弁える。** 迷宮には勇気を称える勲章など存在せず、あるのは生き残った者への栄冠だけです。逃走することは回復にも繋がります：レベル1の冒険者であっても、通常のモンスターより早く自然治癒します（プレイヤーは概ね9ターンに1 HP回復するのに対し、敵は20ターンに1 HP）。中盤に達する頃には敵の5倍の速度で急速回復するため、再生能力を持たない足の遅い強敵（ミミック、オーガ、レオクロッタなど）から距離を取ることは、実質的にタダでHPを回復しているのと同じです。ただし、トロール、吸血鬼、そしてイェンダーの魔法使いは例外です：彼らは毎ターン急速回復し、時にはあなた以上の速度で傷を癒します。彼らを相手に持久戦を挑んではいけません。戦況がもはや絶望的であるなら、瞬間移動の巻物、テレポートの杖を使うか、あるいは全速力で逃げ出しましょう。命を落とした冒険者に二度目のチャンスはありません（命の魔除けを首に下げている場合を除きます）。

**争いの指輪を活用する。** 「争いの指輪 (ring of conflict)」を身につけると、モンスターたちはお互いを敵と見なして同士討ちを始めます。敵で埋め尽くされた部屋の前に立ち、指輪をはめ、扉口の安全な位置からモンスターたちが共喰いして自滅していく様を高みの見物と洒落込みましょう。NetHack 5.0における注意点が2つあります：モンスターが争い状態に陥るにはあなたを **視認** している必要があり（盲目や視界外の敵は正気を保ちます）、さらに同士討ちの発生率はあなたの **魅力 (Charisma)** に比例します。魅力が高ければ極めて高い信頼性を誇りますが、魅力が低いと効果が不安定になります。

**緊急避難としてのエルベレス。** 文字を刻み、そのマスの上に立ち、体勢を立て直しましょう。モンスターたちは混乱と怒りに満ちた目であなたの周囲をうろうろと取り囲むだけになり、完全に無防備な時間が手に入ります。戦闘を再開する前に、必ずエルベレスのマスから一歩踏み出してください。結界の上からの攻撃は神聖な文字を汚して瞬時に消滅させ、「偽善者になったような気分だ」という痛烈な属性ペナルティを受けます。エルベレスは傷を癒すための安全な救護所であり、射撃用の砲台ではありません。

##### 遠距離攻撃モンスターと恐怖したモンスター (Ranged and Frightened Monsters)

**遠距離攻撃を行う敵は後退する。** 弓兵や呪文の使い手は、こちらが近接間合いに詰め寄ると後退して距離を取ろうとします。ケンタウロスの射手は後退しながら弓を射ち続けてきます。角を利用して退路を断つか、こちらも遠距離攻撃で応戦するか、テレポートの杖で敵を吹き飛ばして不毛な追いかけっこを終わらせましょう。呪文詠唱者も同様に、あなたが間合いを詰めようともがいている間に距離を取って魔法を浴びせ続けてきます。

**袋小路に追い詰められた恐怖モンスターは反撃してくる。** エルベレスによる撃退戦術は、モンスターに逃げ道がある場合にのみ機能します。恐怖して逃走しようとしているモンスターであっても、逃げ場のない袋小路に追い詰められると、無抵抗に殴り倒されるくらいなら死に物狂いで反転攻勢に出てきます。通路にエルベレスを刻んでモンスターを追いつめる際は、敵の背後に必ず逃走用の退路が残されていることを確認してください。

**友好的な生物に対する属性ペナルティ。** 騎士と侍は、無防備な敵、逃走中の敵、あるいは友好的な生物を攻撃すると特別な属性値ペナルティを受けます（騎士は卑劣漢としてのペナルティ、侍は義理を欠いた不名誉のペナルティ）。クエストの入り口を通過するには、経験レベル14に加えて **属性値の実績が最低20以上** 必要です。失った属性値は敵対的なモンスターを討伐することで取り戻せますが、ペナルティによってクエストへの突入が遅れてしまう恐れがあります。

---

### あなたを殺す脅威 (Things That Will Kill You)

<!-- audit
2026-08-13:
- growl wake radius: growl() calls wake_nearto(x,y, mtmp->data->mlevel * 18) (sounds.c:421), and wake_nearto uses dist2 < distance (mon.c:4388), so mlevel*18 is a SQUARED radius. base gnome is m_lev 1 (monsters.h:1682) => sqrt(18) ≈ 4 squares, NOT 7. "seven squares for a level-3 gnome" was wrong (a gnome is level 1; a gnome LORD is level 3). fixed prose to "about four squares for a gnome, farther for larger creatures" (dwarf m_lev 2 => ~6, gnome lord m_lev 3 => ~7).
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Sleep resistance is from elf corpses only; an elven mummy drops an already-old elf corpse, so eating it risks food poisoning (mon.c:620-646; eat.c:908). Giants convey Str/elemental res.
- Floating-eye paralysis is d(3,70) ≈ 3-210, avg ~106 (uhitm.c:5887, 6042); "70" was the die size.
- Dragon breath vs items: yellow=acid, blue=lightning (monsters.h); shock destroys rings/wands, fire+cold destroy potions (zap.c). Rewrote to fire/frost.
-->
<!-- audit
2026-05-20:
- mines residents are class G (gnomes, S_GNOME) and h (humanoids incl. dwarves, S_HUMANOID); g is gremlins/gargoyles (defsym.h:295, 301, 303, 333)
- gnomish wizard has AT_MAGC AD_SPEL (monsters.h:1695-1698); its ONLY attack is spellcasting. CORRECTION (2026-08-13): the earlier "can cast sleep" was wrong. it casts from mon_wizard_spells (mcastu.c:32-36) which contains NO sleep spell, and at m_lev 3 spellval=rn2(3)∈{0,1,2} (mcastu.c:111) can only reach PSI_BOLT(0)/CURE_SELF(1)/HASTE_SELF(2). so it psi-bolts you (damage) and self-buffs; it CANNOT sleep, stun, or confuse you. STUN_YOU is level 3 (unreachable at rn2(3)). fixed the prose in Common Combat Deaths (2 spots) and the sleep-source list (replaced "gnomish wizard's sleep spell" with sleeping-gas trap).
- homunculus AT_BITE AD_SLEE 1d3 (monsters.h:551-558)
- soldier ant speed 18, AT_BITE 2d4 + AT_STNG AD_DRST 3d4 (monsters.h:103-110)
- water demon: S_DEMON class &, level 8, NOCORPSE NOGEN (monsters.h:2911-2919)
- rope golem AT_HUGS 6d1 grapple (monsters.h:2523-2529)
- iron golem level 18, speed 6, AT_WEAP 4d10 + AT_BREA AD_DRST 4d6 (poison gas, drains Strength), MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON (monsters.h:2586-2594); slow but heavy hitter, not a speedster
- bats and giant bats speed 22; raven and vampire bat speed 20 with two attacks each (monsters.h:1269-1294)
- steam/fire vortices speed 22; queen bee speed 24 (rare); air elemental speed 36 (monsters.h vortices, queen bee, air elemental rows)
- water demon wish: rnd(100) > (80 + level_difficulty()) — 20% chance at depth 0, drops to 0% past level_difficulty 20 (fountain.c:78)
- clay golem AT_CLAW AD_PHYS 3d10 single (monsters.h:2562-2569)
- stone golem AT_CLAW AD_PHYS 3d8 single (monsters.h:2570-2577)
- golems are class ' (apostrophe), not P (defsym.h:359)
2026-05-19:
- Very_fast = (HFast & ~INTRINSIC) || EFast (youprop.h:377)
- Blue DSM sets EFast |= W_ARM (do_wear.c:822); speed boots set EFast |= W_ARMF
- either alone reaches Very Fast; wearing both doesn't go faster
2026-05-18:
- mount slip damage 10-14 HP via rn1(5, 10) (steed.c:354)
- water demon spawn rate is 1 in 30 quaffs at fountain.c:247, 314
- bones items 80% cursed via rn2(5) gate (bones.c:290)
- all 9 DSM extrinsic properties verified at do_wear.c:806-883
- gold DSM permanent light radius 4/3/2 blessed/uncursed/cursed (light.c:881-911)
- gold DSM is the only body-slot light source (artifact.c:2264-2275)
- confused genocide hits your role: u.umonster ← gu.urole.mnum (read.c:2839, u_init.c:991)
- mumakil attack solo, not in packs; AT_BUTT 4d12 + AT_BITE 2d6 (monsters.h:838-845)
- shimmering DSM does not exist in 5.0 (#if 0 DEFERRED in objects.h:509-511, 536-538)
- strategy aligned with NetHackWiki Bones, Yet Another Stupid Death, Sleep, Golem: bones loot 80% cursed and dangerous, early-game pacing matters more than depth, sleep resistance recommended before Mines, iron golem and rope golem are the dangerous golems for the player (https://nethackwiki.com/wiki/Bones, https://nethackwiki.com/wiki/Yet_Another_Stupid_Death, https://nethackwiki.com/wiki/Sleep, https://nethackwiki.com/wiki/Golem)
-->

ダンジョン探索全体のうち、**昇天（ゲームクリア）に到達できるのはわずか約0.4%に過ぎません。**

**序盤のダンジョンこそが最も危険である。** 最も多くの冒険者を葬り去ってきたモンスターたちは、すべてダンジョン上層部に生息しています：ジャッカル、ドワーフ、兵隊蟻、ノームの領主、ドブネズミ、巨大コウモリ、[小さなミミック](#a-note-on-mimics)、ノーム、狐、水ヘビです。万全に準備の整った冒険者にとって、彼らの誰一人として本質的に危険な敵ではありません。彼らがあなたを殺せるのは、あなたのHP、AC、そして耐性がまだ整っておらず、しかも数で圧倒してくるからです。序盤の手番は、無理に深く潜ろうと急ぐのではなく、フロアを丁寧に掃討し、祭壇を見つけ出し、手に入れた武具のBUC（呪いの状態）を把握することに費やしましょう。

**探索ペースについて。** 戦闘の後は必ず足を止めて休息し、HP満タン（少なくとも90%以上）の状態で階段を降りてください。現在の階層と経験レベルを無理に一致させようとするよりも、最大HPの高さの方がはるかに生存率を正確に予測します。利用価値のあるものは探索すべきですが、下り階段が見つかった後は、空っぽの部屋を無意味にうろついたり実りのない捜索に貴重な食料を浪費してはいけません。遠距離攻撃の手段と、瞬間移動の巻物やテレポートの杖などの安全な離脱手段を必ず確保した上で次の階層へ降りましょう。階段を降りた直後の突然死の多くは、手負いの状態で逃走手段も持たずに新しいフロアへと踏み込んだことから始まっています。

#### よくある戦死の原因 (Common Combat Deaths)

死因の上位10種以外にも、階層の深さや外見から受ける印象以上に多くの初心者を死に至らしめる敵の系統が存在します。彼らは大群で押し寄せるか、プレイヤーを上回る超高速で移動するか、あるいは一撃でも喰らえば致命傷となる凶悪な特殊攻撃を秘めています。

**[ノームの鉱山 (Gnomish Mines)](#the-gnomish-mines) は最大の死地。** 鉱山の最大の危険はその地形構造にあります：鉱山の部屋は広大な開けた洞窟であり、4〜5体の武装した敵が容易にあなたを取り囲めるだけの十分な空間があります。遠距離攻撃を活用するか、洞窟の壁が狭まっている自然の狭路（ボトルネック）を探しましょう。ドワーフはノームよりも重い打撃を放ち、ノームの魔法使い（最初に出遭う魔法詠唱モンスター）はサイコボルトの光線を浴びせ、自己治癒や自己加速を駆使してきます。さらに深く潜ると、異なる色の `G` や `h` で表される領主や王が出現します。鉱山の第1階層を軽く下見するのは構いませんが、本格的な探索は経験レベル（XL）5前後、AC 5以下、HP満タン、投擲武器の束、そして確実な脱出用アイテムが揃ってから挑みましょう。睡眠耐性があれば非常に心強いですが、耐性が手に入るまで永久に先送りにする必要はありません。

**耐性のない状態での睡眠はほぼ即死を意味する。** ホムンクルス（`i`）の噛みつき、催眠ガスの罠、そして中盤以降のオレンジドラゴンのブレスやナズグルの吐息は、あなたを数ターンの間強制的に眠らせて無防備にします。通路で1対1の状況であれば数ラウンドの被弾で済むこともありますが、周囲を他のモンスターに取り囲まれている場合、動けない無防備なあなたに対して周囲の敵全員が一斉に一方的なタコ殴りを加えてきます。睡眠耐性は、エルフのキャラクターがレベル4に達するか、オレンジドラゴンの鎧を装備するか、あるいは適切な死体を食べることで得られます。魔法使いの「魔法を防ぐクローク」もレンジャーの「幻影のクローク」も、睡眠耐性は付与してくれません。

**コウモリをはじめとする超高速モンスター群 (`B`)。** コウモリや巨大コウモリは、初期速度12のプレイヤーのほぼ倍に相当する **速度22** で飛び回ります。あなたが1回武器を振る間に彼らは2回攻撃を仕掛けてくるため、2倍のペースで繰り出される1d4の噛みつきは、低いHPを瞬く間に削り落とします。カラスや吸血コウモリは速度20でそれぞれ2回攻撃を行い、吸血コウモリの2撃目の噛みつきは筋力を直接吸い取ってきます。包囲されないように扉口から戦うか、接近される前に遠距離攻撃で仕留めましょう。中盤以降に現れるケンタウロス（速度18〜20）や各種の渦も、全く同様のスピードの脅威を突きつけてきます。

**蟻をはじめとする群れをなす敵 (`a`)。** 兵隊蟻は速度18を誇り、1ターンに2回攻撃（噛みつき＋筋力を低下させる毒針）を行い、常に集団で行動します。殺人蜂、巨大蟻、火蟻も同種の危険な集団です。未探索のフロアでカサカサと蠢く音や羽音が聞こえたら、集団に包囲される前に即座に通路へと後退し、一本道の迎撃地点を確保する合図だと判断してください。

**四足獣 (`q`)。** **ロゼ** は鈍足の速度9ですが、1ターンに3回攻撃を繰り出す集団ハンターです：1頭だけであれば逃げるのは容易ですが、部屋の中に3頭いれば複数の死闘が同時に重なることになります。ムーマクは単独で強烈な2段攻撃を繰り出す巨獣であり（4d12の突き刺し＋2d6の噛みつき）、ダンジョン上層のあらゆる敵の中で最も重い打撃力を誇ります。どちらも中層の部屋を徘徊しています。

**ゴーレム (`'`)。** 大半のゴーレムは足が遅いですが、数種類は身体の大きさに比例しない桁外れの打撃力を持ちます。ロープゴーレムは抱え込み（hugs）攻撃であなたを拘束し、その場に縫い止めて周囲の敵の餌食にします。粘土のゴーレムと石のゴーレムは、たった1回の鉤爪攻撃でそれぞれ3d10、3d8という破格のダメージを与えてきます。鉄のゴーレムはその中でも最悪の脅威です：レベル18、4d10の武器攻撃に加えて筋力を奪う4d6の毒ガスブレスを吐き、火炎、冷気、電撃、睡眠、毒のすべてに完全耐性を持ちます。大半のゴーレムは死体を残さないため、食べて内在能力を得ることはできません。遠距離から素早く倒しましょう。

**泉から湧き出る水の魔神 (`&`)。** 泉の水を飲むと、およそ30回に1回の確率で「水の魔神」が召喚されます。魔神が出現した瞬間に願いの判定が行われます：運良く友好的な魔神であれば即座に願いを叶えて消滅しますが、そうでなければレベル8の魔神として襲いかかってきます。階層が深くなるほど願いの発生率は低下するため、深く潜ってからの安易な水飲みは割に合いません。「魔法防御」や「反射」、あるいは明確な退路が確保できるまでは、泉から水を飲んではいけません。

**さまよう目 (`e`)。** 近接攻撃で殴ってしまうと、3〜210ターン（平均約100ターン）もの間、完全に麻痺して行動不能になります。その昏睡の間に通りかかったモンスターによって、なす術もなく殴り殺されます。必ず飛び道具や杖で遠距離から仕留め、その後に死体を食べて [テレパシー](#senses-and-perception) を獲得しましょう。

**ミノタウロス (`H`)。** [城 (The Castle)](#the-castle) や [ゲヘナ (Gehennom)](#gehennom) の迷路階層に出現します。1ターンに3回攻撃（2回の3d10鉤爪と1回の2d8頭突き）を放ち、毎ターン平均約42ダメージを叩き出してきます。終盤の守護者である死の騎士（Riders）を除けば、物理攻撃力において最強のモンスターです。眠りの杖を使うか、麻痺の薬を投げつけるか（[自由行動](#combat-and-defense) が必要）、あるいは接近される前に下に向かって地面を掘り抜いて逃走しましょう。ミノタウロスはエルベレスを無視して踏み越えてきます。

**上位の悪魔はさらなる上位悪魔を召喚する。** 上位の悪魔（Major demons）は、攻撃手番ごとに1/16の確率（ゲヘナ内部では1/10の確率）で別の大悪魔を呼び寄せます。

#### 命取りとなる過ち (Deadly Mistakes)

珍しい即死トラップよりも、日常的な不注意や過ちによって命を落とす冒険者の方がはるかに多数を占めます。以下はサーバーの死亡統計に基づく、警戒すべき典型的なミスの実態です。

**飲食のミス。** 古くなった死体は食中毒を引き起こし、毒を持つ死体（[致死毒](#deadly-poison)）は急激にHPを奪い去り、満腹（Satiated）状態での食事は [窒息死（喉詰まり）](#choking) を招きます。巨大な重い死体を食べる前には必ず現在の栄養状態を確認し、誤って危険なものを口にしてしまった場合は即座に神に祈りを捧げましょう。

**店内で未識別の巻物を読む。** 混乱状態や呪われた「瞬間移動の巻物」を読むと、未払いの商品を抱えたまま店外（別の階層）へとテレポートしてしまい、店主から万引き犯と見なされて敵対されます。「火の巻物」を読めば店の商品を焼き払ってしまい、莫大な損害賠償を請求されます。価格識別セッションは店の外で行いましょう。

**乗馬の落馬事故。** 乗馬する際、あなたの経験レベルと愛馬の懐き度（馴れ具合）に基づいた判定が行われ、失敗すると10〜14 HPの落下ダメージを受けます。特に危険なのは呪われた鞍や油を塗った鞍です（ほぼ確実に落馬し大ダメージを受けます）。混乱、つまずき、または手が滑る状態での騎乗はさらに成功率が落ち、レベル2の駆け出し冒険者では新しいペットに20回中9回振り落とされ、懐き度の低い乗騎なら20回中17回も振り落とされます。

**ペットによる撲殺。** 小猫、小犬、家猫、仔馬など、初期ペットたちが死亡ログに名を連ねることがあります。その原因のほぼ100%は、プレイヤーが「争いの指輪」を装備したまま外し忘れたことにあります。愛馬やペットの元へ戻る前に、必ず指輪を外してください。

**薬の沸騰と破裂。** ゲヘナの煮え滾る灼熱の床に薬を落とすと、約半分の確率で破裂しますが無害です。本当に危険なのは、手持ちの荷物の中にある薬に火炎が届いた場合です：薬が沸騰・破裂し、致命的な大爆発を引き起こします。薬や巻物は常に袋の中に退避させておくのが賢明です：火炎の罠や赤ドラゴンの火炎ブレスは露出した巻物や薬を一瞬で焼き払い、白ドラゴンの冷気ブレスは露出した薬の瓶を粉々に砕きます。

**敵の手に渡った杖。** モンスターは拾った攻撃の杖を容赦なく使ってきますし、放たれた光線は壁で跳ね返ってあなたの顔面に直撃することがあります。「反射」と「魔法防御」はゲヘナ突入よりはるか前の中盤から不可欠です。未識別の杖は、生きている生物に向けて振る前に必ず床に試し書きして識別してください。

**グリッドバグによる撲殺。** ゲーム中最弱のモンスターであるグリッドバグが、強敵との死闘をHP 2で生き延びて歩いていた冒険者や、隣接されたターンに呑気に巻物を読もうとした冒険者に最後の一撃を加えて息の根を止めます。敵の脅威に晒されている最中に無防備に巻物を読んではいけません。

**蹴り（キック）による事故死。** 流し台を蹴ると [黒プリン](#a-note-on-puddings) や夢魔（インキュバス／サキュバス）、あるいはそれ以上の凶悪な敵が呼び出されます。扉を蹴っても失敗時は *ドスン！ (Whammm!)* と鈍い音がするだけですが、壁を蹴ると足を骨折して大ダメージを受けます。罠付きの宝箱を蹴るのも別の自殺行為です。何が起きても対処できる余裕があるときにだけ蹴りましょう。

**神の怒り。** まだ神が応えてくれる準備ができていない（祈りのクールダウン中）にもかかわらず祈ってしまった場合です。神罰や祈りのインターバル、どのような状態が祈るに値する「危機」なのかについては、[神との関係 (Divine Relations)](#divine-relations) を参照してください。

**混乱状態での「虐殺の巻物」。** 混乱した状態で虐殺の巻物を読むと、あなた自身の役職の種族（ワルキューレ、魔法使い、侍など）が世界から完全に消滅します。あなた自身が虐殺の対象となるのです。すでに正体が判明している巻物でない限り、混乱中に巻物を読んではいけません。

**頭上に落とす「大地の巻物」。** 狭い空間で大地の巻物を読み、自分自身の頭上に呼び出した巨石の山に押し潰されて生き埋めになる事故です。

序盤の死の大半は、引くべき戦闘で「もう1手番だけ」と欲張って殴り合いを続けた結果として発生しています。

#### ニンフについての覚書 (A Note on Nymphs)

`n` クラス（木のニンフ、水のニンフ、山のニンフ）は、あなたを殺そうとはしません。彼女らが狙っているのは、あなたの所持品（インベントリ）です。序盤においてニンフは、身につけている防具を直接体から引き剥がしてせっかく構築したACを台無しにし、さらに爪による攻撃が命中するたびに荷物袋からランダムにアイテムを1つ奪い取ります。そして同フロアのランダムな場所へ **瞬間移動（テレポート）して逃げ去ります**。あなたの軽量化の鞄、反射の魔除け、願ったばかりの耐魔のクロークなどが、マップの遥か彼方、往々にして未探索の部屋へと持ち去られてしまうのです。序盤のキャラクターにこれほど手痛い後退を強いるモンスターは他にほとんどおらず、しかもそれはたった一撃で発生します。

**盗みのみを行う。** 両手の爪は同一の攻撃処理を行います。すなわち、荷物袋の中のアイテムを奪うか、身につけている装備品を剥ぎ取るかのいずれかです。彼女らはあなたのHPを削るのではなく、装備やアイテムを奪っていくのです。

**防御策。** ニンフを決して近接攻撃の間合いに入れてはならない、というのが鉄則です。遠距離から仕留めてください（ダーツ、フォースボルト、あらゆる攻撃の杖）。[**エルベレス (Elbereth)** を刻む](#elbereth) のも極めて有効です。ニンフはエルベレスを尊重して退散します。あるいは、接近する前に絶対に失いたくない最も貴重なアイテムを床に置いておくという手もあります。荷物袋に入っていなければ盗まれることはありません。ニンフはHPへの直接ダメージを与えないため、全裸で防具を一切着けず、荷物も完全に空にしたキャラクターであれば、完全に安全な状態でニンフと素手で殴り合うことすら可能です。攻撃が当たるたびにニンフがパッと別の場所へテレポートするのは防げませんが、もはや奪われるものは何もありません。

**すでに盗まれてしまったら？** ニンフは死ぬまで奪ったアイテムを保持し続けるため、追跡して仕留めなければなりません。盗まれた戦利品はニンフの死体からドロップします。盗みを働いたニンフは、落とし戸から下の階に落ちたり階段を歩いて移動したりしない限り同じフロアに留まります（階段などを移動されると、アイテムを持ったまま別フロアへ持ち去られてしまいます）。

**昇天への登攀（Ascension Run）の最中、イェンダーの魔除けを所持した状態でニンフと交戦してはなりません。** もし魔除けを盗まれれば、登攀を一時中断してニンフを追跡・殺害しなければならず、その捜索中も「謎の力（mysterious force）」による妨害が止まることはありません。

#### ミミックについての覚書 (A Note on Mimics)

ミミックは、出現する深度から受ける印象よりもはるかに強敵です。その爪の一撃は低レベルのキャラクターを一撃死させるのに十分な威力を持ち、小さなミミックは死因ランキングのトップ10に名を連ねています。唯一の救いは、**すべてのミミックが鈍足である**（速度3、プレイヤーの基本速度の半分未満）という点です。もし擬態を暴いて相手にするのが危険だと感じたら、単に歩いて立ち去り、強くなってから戻ってくれば問題ありません。逃げ足が遅いミミックがどこかへ行ってしまう心配はありません。

遭遇する場所の大半は **店** です。一般的な店では通路に1〜2体のミミックが商品に化けて鎮座しており、ダンジョンを深く潜るほどその数は増えます。

**視覚的な見分け方。** 総称的な「奇妙な物体」として出現しているミミックは、マップ上で `]` として描画されます。これは防具（アーマークラス）を表す `[` の鏡像反転です。本物のアイテムで `]` と表示されるものはゲーム内に一切存在しないため、**マップ上のどこであれ `]` は常にミミック** です。

**安全に正体を暴く方法。** 隣接するマスを捜索（`s`）すると、隠れているミミックの正体が暴かれます。疑わしいマスに安価なアイテムを投げつけるのも有効です。ミミックが姿を現し、投げたアイテムは無害に足元に落ちます。そのマスに聴診器を適用することでも正体を暴けます。テレパシー、ESP、アストラル視覚、そして扉探索の杖は擬態を見破り、ミミックを `m` として表示します。また、ペットはミミックがいるマスを決して踏もうとしません。

**捕まる前に大きなミミックを見分ける。** いったん `m` として正体が現れると、その色で判別できます。小さなミミックは茶色、大きなミミックは赤、巨大なミミックは赤紫（マゼンタ）です。ダンジョンの深度も目安になります。大きなミミックや巨大なミミックは通常ダンジョン中盤以降にならないと出現しないため、浅い階層で見かけるミミックはほぼすべて、3d4の爪攻撃を持つ小さなミミックです。

**粘着。** **小さなミミックは強打してきますが、プレイヤーを拘束することはありません**（いつでも歩いて離脱できます）。一方、**大きなミミックや巨大なミミックは、爪攻撃が命中するとプレイヤーをその場に接着・拘束します**。移動できず、階段も昇降できず、落とし戸に落ちることもできなくなります。そしていったん接着されると、ミミックが起きている間に振りほどくチャンスは **毎ターンおよそ13分の1** しかありません。相手を倒すか（鈍足です）、テレポートで脱出するか、あるいは睡眠状態にさせてから脱出してください。最大の自衛策は拘束自体を受けないことです。拘束は近接攻撃でしか発生しないため、**店の中を移動する際にこまめに捜索（`s`）を行う** ことで、隣接マスを踏み込む前に大きなミミックや巨大なミミックを発見できます。正体を看破されたミミックが不意打ちで拘束してくることはありません。

**死体を食べる。** ミミックの死体を食べると、その体の大きさに応じて20 / 40 / 50ターンの間、金貨の山（幻覚症状の時はオレンジ）に変化します。何らかのモンスターが「あなた」を拾い上げようとすると、この変身の術が解けます。

#### 獣化症モンスターについての覚書 (A Note on Werecreatures)

**人ジャッカル、人ネズミ、人狼** からの噛みつき攻撃を受けると、**獣化症（lycanthropy）** に感染する危険があります。そして噛みつきそのものよりも、この感染こそが真の脅威です。感染すると、およそ60〜80ターンごと（夜間はさらに高頻度）にランダムに獣の姿へと変身してしまいます。変身するたびに身につけている防具が強制的に脱げてしまいます。人狼に変身した場合は鎧とシャツが破壊され（クロークだけは無傷で床に落ちます）、脆弱な野獣の肉体に放り出されます。時間経過で自然と元の姿に戻りますが、戦闘の真っ只中に変身が起きると、最悪のタイミングで丸裸に剥ぎ取られてしまいます。

獣化症モンスターが「助けを呼んだ（summons help）」ときは、ただちにエルベレスを刻んでください。召喚された動物たちはエルベレスを尊重して逃げますが、獣化症モンスター自身の人型（`@`）形態はエルベレスを無視して前進してくるため、必ず退路も確保しておきましょう。

**治療法。** **聖水** を飲むか、**`#pray`（祈る）** を行うか、あるいは **トリカブトの小枝（sprig of wolfsbane）** を食べてください。ただし、治療する前にペットの軍隊を召喚しておくという裏技があります。野獣形態の間に数ターンを費やして `#monster` コマンドで同胞を呼び出すと、オオカミ（あるいはネズミやジャッカル）が召喚されます。この召喚獣たちは **獣化症を治療した後もずっと友好的（ペット）のまま残る** ため、無料の群れを手に入れ、後でへんげの罠を使ってより強力な凶悪モンスターへと育成することができます。

なお、感染中にへんげの薬を飲むか「へんげの罠」を踏んだ場合、ランダムなモンスターではなく自分自身の「獣化形態」に変身し、感染そのものは治癒しません。

#### プリンについての覚書 (A Note on Puddings)

プリンは、ダンジョンを代表する自己増殖型モンスターであり、その倒した後に残る「塊（glob）」はゲーム中で見つかる最高の食料のひとつでもあります。このクラスはダンジョン中盤およびゲヘナに生息しています。**茶色プリンと黒プリンは、鉄製または金属製の武器で殴ると分裂します**。1体が2体に、2体が4体へと増殖し、ロングソードを振り回して狩るつもりが、たちまち大群に包囲される事態に陥ります。さらに **黒プリンは、受動的な反撃攻撃によって手持ちの武器を腐食・錆びさせます**。そのため分裂させるごとに、愛用の刃がボロボロに錆びていくことになります。

**防御策。** 近接戦を行うなら、**銀製または木製の武器**（銀の短剣、エルフの短剣、棍棒、クオータースタッフなど）を使用してください。これらは分裂を引き起こしません。また、ミスリル製の武器も分裂チェックを回避します。炎による攻撃は分裂させずに倒すことができます（茶色プリンと黒プリンは冷気への耐性を持っています）。大半の攻撃呪文も安全に機能します。

**灰色ウーズ** は分裂しませんが、攻撃を受けると着用中の防具を錆びさせます。回避できる状況であれば、初期装備の鉄の鎧を着た状態で不用意に交戦しないでください。

**塊を食べる。** プリンは通常の死体ではなく **「塊（glob）」** を残します。この塊はゲーム屈指の優れた栄養源です。通常の死体とは異なり、塊を祭壇に捧げて生贄にすることはできないため、プリンを奉納稼ぎに利用することはできません。塊は約500ターンの間可食状態を保ち、極めて優秀な耐性を授けてくれます。茶色プリンの塊を繰り返し食べることで **冷気耐性、電撃耐性、毒耐性** が獲得できます。灰色ウーズの塊は **火炎耐性、冷気耐性、毒耐性** を授けます。黒プリンの塊も同様に **冷気耐性、電撃耐性、毒耐性** を付与します。茶色プリンと灰色ウーズは *菜食主義者* でも安全に食べられますが、黒プリンは菜食には該当しません。なお、同じ種類の塊が床の同一マスに重なると1つの大きな食事に融合してしまい、耐性判定の抽選が1回分にまとまってしまうため、塊同士が合体する前に床から1つずつ拾って食べるようにしてください。死体による内在能力獲得の詳細な一覧は、[役立つ死体効果 (Useful Corpse Effects)](#useful-corpse-effects) を参照してください。

#### ドラゴンについての覚書 (A Note on Dragons)

ドラゴンには詳細な事前ブリーフィングが必要です。体色ごとに異なるブレス攻撃、耐性、ドラゴンブレス、そして鱗鎧の特性を持ち、何よりプレイヤーを殺そうとする執念の強さもそれぞれ異なります。以下はその要約です：

**灰色ドラゴン (Gray dragon)** の鱗鎧は、ゲーム内で最も重要な防御能力である「耐魔（魔法防御）」を付与します。灰色ドラゴンは、その皮を手に入れるためにプレイヤーが最も倒したいと願う相手であると同時に、挑戦したことを最も後悔させられやすい相手でもあります。

**銀色ドラゴン (Silver dragon)** の鱗鎧は「反射」を付与し、ほとんどの光線・遠距離属性攻撃を跳ね返します。

**黒ドラゴン (Black dragon)** は、あなたの魔法防御ごと身につけているあらゆる装備を瞬間分解（disintegrate）してあなたを消滅させます。黒ドラゴンの生息域に乗り込む前に、反射の能力を身につけるか、あるいは十分な数の黒ドラゴンを食べて[瞬間分解耐性](#damage-resistances) を獲得しておかなければなりません。黒ドラゴンの鱗鎧は、瞬間分解耐性に加えて貴重な外部特性である[ドレイン耐性](#damage-resistances) も付与します。

**黄色ドラゴン (Yellow dragon)** の鱗鎧は、その説明以上の恩恵をもたらします。表記上の能力は酸耐性ですが、それに加えて酸のブロッブの死体を食べた際と同じ完全免疫である **「石化耐性」** を付与します。もし黄色ドラゴンを見かけ、まだ石化耐性を持っていないなら、遠出してでも倒しに行く価値があります。黄色ドラゴンは他の色のドラゴンと出現率は変わりません。

**オレンジドラゴン (Orange dragon)** の鱗鎧は、睡眠耐性と **自由行動**（自由行動の指輪と同等の効果）の2つを1スロットで同時に付与します。

**白ドラゴン (White dragon)** の鱗鎧は、冷気耐性と **消化不良**（長旅における空腹の進行を遅らせる効果）を付与します。

**赤色ドラゴン (Red dragon)** の鱗鎧は、火炎耐性と **赤外線視覚**（エルフの種族能力や赤外線視覚の指輪と同じ効果）を付与します。

**緑ドラゴン (Green dragon)** の鱗鎧は、毒耐性と **病気耐性** の両方を付与し、毒と病気の両方の脅威をカバーします。

**青ドラゴン (Blue dragon)** の鱗鎧は、電撃耐性と内在的な **速度**（韋駄天の靴と同等クラス）を付与します（韋駄天の靴と同時に装備してもそれ以上速くはなりませんが、単体で「超高速（Very Fast）」に達します）。この組み合わせにより、青は非常に優れた汎用装備候補となります。

**金色ドラゴン (Gold dragon)** は火のブレスを吐きます。その鱗鎧には元素耐性はありませんが、常に光を放つ永久光源（祝福時は半径4、無呪は3、呪いは2）として機能するため、たいまつや油の代用品になります。また、幻覚耐性も付与します。

すべてのドラゴンの鱗鎧はドラゴンの皮製で、胴体スロットを占め、着用時の基本ACは+9です。ドラゴンの皮は錆、腐食、火炎に対して完全な耐性を持ちますが、吸魔（エンチャント低下）は防げません。どの色を狙うべきかは、通常「どのドラゴンの生息域に安全に到達できるか」で決まります。成長した成体ドラゴンを倒すと約3分の1の確率でドラゴンの鱗を落とします。これをそのまま身につけることもできますし、身につけた状態で呪われていない防具強化の巻物を読むことでドラゴンの鱗鎧へと仕立て直すことができます。

#### トロールについての覚書 (A Note on Trolls)

`T` クラスは、一度倒しただけでは死んだままになってくれません。トロールを倒した後の死体は、床に数ターンの間横たわった後、怒り狂った完全回復（全HP）の状態で再び立ち上がってきます。およそ4体中3体のトロールの死体は、50ターン以内に蘇生します。

**蘇生を阻止する方法。** 死体を食べる、缶詰にする、ペットに食べさせる、あるいは溶岩の中に蹴り込んでください。テレポートさせても同じフロアの別の場所へ死体が移動するだけであり、打撃を加えても死体を完全に破壊することはできません。

**トロールは死ぬと装備を落とす。** 蘇生したトロールは以前持っていた装備を拾い直すため、「復活と拾い直し」のサイクルを繰り返すと、同じマスに様々なトロール装備と死体が積み重なることになります。起き上がる前に床の装備を拾っておきましょう。どちらにせよ、その戦利品はあなたのものです。

**クラスの構成員。** トロール（通常のトロール）、氷トロール、岩トロール、水トロール、そして終盤に出現するオログ＝ハイです。すべてが復活し、どの変種であっても死体の復活挙動は同じです。最も恐るべき変種はオログ＝ハイで、レベル13で3回攻撃を繰り出してきます。

#### レイスについての覚書 (A Note on Wraiths)

`W` クラスは、接触攻撃によって **経験値レベルを1低下（レベルドレイン）** させてきます。これは本作においてキャラクターが被る数少ない「不可逆的な後退」のひとつです。最大HP、エナジー（魔力）、そして直近に取得したスキル枠を失います（ただし能力値ポイントは低下しません）。失ったレベルは「能力回復の薬 (potion of restore ability)」を飲むことで元に戻すことができます。レイスは放置すれば何度でもこの接触攻撃を繰り出してくるため、部屋の反対側から遠距離で仕留める計画を立ててください。

**死体を食べるとレベルが上がる。** レベルドレイン攻撃は近接攻撃の間合いでしか発生しないため、距離を取るか、距離感をコントロールできる一本道の通路内から交戦してください。レイスの死体は通常の速度で腐敗するため、部屋の安全を確保した上で、死体が新鮮なうちに速やかに食べてください。

**レイス養殖。** 中盤から終盤のプレイヤーは、経験値レベルを稼ぐためにクエスト上層やゲヘナ全域でレイスを狩り集めます。「レイス」を指定して **呪われた虐殺の巻物** を読むと、自分の足元に4〜6体の生まれたてのレイスが逆虐殺（召喚）され、出現したターンに即座に倒せる戦力があれば即席のごちそうに早変わりします。古典的な戦法は、階段の上に陣取り（危険になったら即座に階を移動して逃げられるようにするため）、呪われた巻物の束を床に置き、1枚ずつ読んで経験値を貪り食うというものです。昇天を果たした勇者たちの中には、ゲヘナを乗り切るための経験値レベルをこの「レイス爆食」によって稼ぎ出したと語る者が少なくありません。

#### 誘惑についての覚書 (A Note on Seduction) {#seduction}
<!-- audit
2026-05-18:
- could_seduce at mhitu.c:1980 requires opposite-sex genagr/gendef; same-sex foocubus just claws
- demon's succubus/incubus form is randomly assigned at generation, not based on player gender (makemon.c:1278-1279 `mtmp->female = femaleok ? rn2(2) : 0`; mhitu.c:1988-1989 doseduce reads Mgender(mon) not player)
- stripped items go to inventory, not dropped on the floor (mhitu.c:2351 calls remove_worn_item which just unequips into inventory, steal.c:213)
- level-drain outcome is fatal at XL 1 — do not farm a foocubus at low level (exper.c:232-238 losexp at u.ulevel==1 with non-null drainer calls done(DIED))
-->

**愛欲の悪魔**（`&`、灰色）は、男性主人公に対しては **サキュバス**、女性主人公に対しては **インキュバス** として現れます。同性の悪魔（foocubus）は単に爪で引っ掻いてくるだけで、誘惑のプロセスを開始することはありません。この遭遇は「魅力（Cha）＋知力（Int）」のギャンブルであり、5つの悪い結果と5つの良い結果、それに支払いフェーズが存在します。対応を誤ればレベル低下、能力値低下、6〜15のHPダメージを被りますが、うまく利用すればレベル上昇、能力値上昇、HP完全回復、最大魔力（Pw）増加の恩恵を得られます。

**メカニズム。** 悪魔は主人公と隣接しており、クールダウン中でない必要があります。悪魔はあなたが身につけている防具を1枚ずつ順番に脱がせていきます（クローク、鎧、靴、小手、盾、兜、シャツ）。脱がされたアイテムは荷物袋（インベントリ）に回収され、奪われたり床に落とされたりすることはありません。脱衣によって失うのは、遭遇の残りのターンにおけるそのスロットの防御力だけです。
各パーツが脱げる前に、Cha/20 の確率で「はい/いいえ（y/n）」の確認プロンプトが表示されます（つまり魅力18なら約10回中9回、魅力10なら約半分の確率で拒否の選択肢が出ます）。**脱衣処理が終わった時点でまだ鎧かクロークを着用したままである場合、遭遇はその場で終了し**、悪魔は立ち去ります。脱ぎにくい鎧（呪われていない頑丈な鎧など）を着ておくことが最もシンプルな防御策です。

行為にまで至った場合、その結果はあなたの「魅力＋知力」の合計値（上限32）に基づいて判定されます。上限値（32）での悪い結果の発生確率は約6%ですが、Cha+Intが20のときは約40%、10のときは約70%にも跳ね上がります。誘惑を受け入れる前に必ず自分のステータスを確認してください。

| 悪い結果 (Cha+Int が低い場合) | 良い結果 (Cha+Int が高い場合) |
|---|---|
| 魔力（エナジー）ドレイン (Pwが0になり、最大Pw −1d10) | 最大Pw +1d5、エナジー全快 |
| 耐久力 −1 | 耐久力 +1 |
| 知恵 −1 | 知恵 +1 |
| 経験値レベル 1 低下（ドレイン耐性で阻止可能） | 経験値レベル 1 上昇 |
| 6〜15のHPダメージ | HP全快 |

その後、悪魔は500以上のゾークミッド（金貨）を請求してきます（魅力が高ければ支払いを拒否可能。友好的な悪魔は5分の1の請求）。睡眠中やその他の無反応な状態である場合は、誘惑の試行自体が保留されます。

**戦術的メモ。** 魅力と知力が高いキャラクターにとって、この遭遇は期待値が大きくプラスになります。また、脱衣のプロセスでは **「呪われた」着用装備であっても強制的に脱がせてくれる** ため、愛欲の悪魔はダンジョンで最も安上がりな呪い解除手段になり得ます。経験値や能力値を稼ぐために悪魔を生かして養殖するプレイヤーもいます。ただし、経験値レベル1のときにこれを試してはなりません。レベルドレインの結果が出た瞬間に即死します。

#### 光の炸裂についての覚書 (A Note on Light Bursts) {#light-bursts}
<!-- audit
2026-05-18:
- yellow light: AT_EXPL/AD_BLND, monster level 3 (monsters.h:1169-1191, mhitu.c:1623-1650)
- black light: AT_EXPL/AD_HALU, monster level 5; perminvis (makemon.c:1317-1320)
- both die in their own explosion
- telepathy does NOT reveal black lights (M1_MINDLESS at monsters.h:1188-1189); only warning does
- warning detects only at adjacent range — exactly when they explode, so it helps less than it looks
- plain potion of healing cures blindness only when blessed (potion.c:1994-2004); extra/full always do
-->

**黄色い光**（`y`、レベル3）と **黒い光**（`y`、レベル5）は、あなたが隣接した瞬間に自爆して攻撃してきます。黄色い光は 10d20 ターンの間 **あなたを盲目状態にします**（*祝福された* 回復の薬、あるいはあらゆる超回復の薬／完全回復の薬、ユニコーンの角で治癒可能）。黒い光は 10d12 ターンの間 **あなたを幻覚状態にします**（ユニコーンの角で治癒、または時間経過で回復）。どちらの光も自爆によって死亡します。危険なのは爆発そのものではなく、その後に続く盲目や幻覚の異常状態です。**防御策：** 杖、投げ短剣、あるいはブレス攻撃などを用いて遠距離から仕留めてください。「警告」能力は不可視状態の黒い光であっても感知できますが、「テレパシー」では感知できません（精神を持たないため）。

### セーブとボーンズ (Saving and Bones)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Bones LOADING is a flat 1/3 (bones.c:646), not depth-scaled; the depth-scaling (up to ~4/5) governs bones CREATION (bones.c:377). Corrected the conflation.
- Verified correct: 80% bones-item curse rate (rn2(5), bones.c:290).
-->
<!-- audit
2026-06-02:
- save deletes file on load: anti-scum design (restore.c, save.c)
- explore mode (-X or #exploremode): death optional ("Die?" prompt, end.c:1104-1115 gated on wizard||discover), save persists, "discover game" tag, all objects revealed at end. Only extra command is #terrain full-map reveal (doterrain cmd.c:1136, reveal_terrain is display-only/no game time). Does NOT unlock WIZMODECMD commands (wish/genesis/identify/map/levelport) — those need wizard (-D)
- Friday-13th sampled at session start: allmain.c:64-66 flags.friday13 = friday_13th(); insight.c:672-680 comments confirm it persists across the session even if real clock changes
- moonphase sampled at session start: allmain.c sets flags.moonphase; insight.c:653-659 explicit comment that the value is at start of session, not real-time
- bones generation chance = floor(depth/4) / (floor(depth/4) + 1); never above DL 4 (wiki/Bones)
- bones-ineligible levels: branch-stair levels, Mines' End, Sokoban, Quest home/goal, Fort Ludios, Medusa, Castle, top/bottom of Vlad's, top/bottom of Wizard's Tower, vibrating square, Sanctum, all planes
- items in bones: 4/5 cursed; artifacts revert to base items; quest artifacts stripped; Amulet of Yendor replaced with "cheap plastic imitation"; Candelabrum, Bell, Book of the Dead similarly replaced (bones.c)
- unique monsters (Wizard, Medusa, Vlad, quest leader, quest nemesis) removed from saved bones; their statues become doppelgangers
- monster type substitution at death: ghost (default), vampire (V kills), wraith (W kills), ghoul (ghoul kills), mummy of race (mummy kills), green slime (sliming death), statue (cockatrice death) (wiki/Bones)
- bones=false rcfile option blocks both creation and loading; required for Bonesless conduct (insight.c:439-441)
-->

NetHackの1回の冒険は、複数のプレイスッションにまたがることがよくあります。そのセッション間を橋渡しする仕組みとして、セッション間でゲームを保存する **「セーブ（Save）」** と、倒れた冒険者の階層を保存して将来の英雄が足を踏み入れられるようにする **「ボーンズファイル（Bones files）」** の2つが存在します。

**セーブ。** `S` キーを押して確認すると、ゲームをセーブして終了します。再開するには、同じキャラクター名でNetHackを起動します。ゲームはセーブデータを読み込み、**その処理の過程でセーブファイルを削除します**。死亡した後にリロードすることはできません。ゲーム外でセーブファイルをコピーしてバックアップし、死後に復元する行為は「セーブスカム（savescumming）」と呼ばれ、NetHackコミュニティでは明確なチートとみなされています。

安全に練習や実験を行いたい場合は、**探索モード（Explore mode）**（起動時オプション `-X`、またはゲーム内で `#exploremode`）を使用してください。探索モードでは、死亡時に「死にますか？（Die?）」という確認プロンプトが表示され、死を拒否してその場で復活することができます。セーブデータも削除されず何度でもリロード可能であり、さらに `#terrain` コマンドでフロア全体のマップを瞬時に開示できます。探索モードではスコア記録が無効化され、ゲーム終了時の記録には「発見ゲーム（discover game）」のタグが付くため、真剣勝負の本番プレイ記録と混ざることはありません。

**ボーンズ階（Bones levels）。** 特定の階層（迷宮の地下4階以降の通常のフロア、炭鉱の街、クエストの中間フロアなど。ただし倉庫番、鉱山の最下層、城、ヴラドの塔の全フロア、各大系を除く）で冒険者が死亡すると、ゲームはそのフロア全体を **ボーンズファイル** として保存します。将来のゲームにおいて、そのフロアをゼロから自動生成する代わりにボーンズファイルを読み込む確率は **一律3分の1（約33%）** です（この確率は深度によって上昇しません。深度が深くなるにつれて上がるのは「ボーンズファイルが生成・遺棄される確率」です）。ダンジョンの概況には「〜の終焉の地」と記録されます。「見覚えのある場所のようだ……（This place looks familiar...）」という進入メッセージは、そのボーンズが自分自身の過去のキャラクターのものである場合にのみ表示されます。

ボーンズ階は元のフロアの地形、罠、アイテムを保持しますが、以下のようないくつかの変更が加えられます：

- 死亡した英雄は、その *名前付きの残滓* を残します。通常は **亡霊（ゴースト）** ですが、吸血鬼に倒された場合は **吸血鬼**、レイスに倒された場合は **レイス**、ミイラに倒された場合は **ミイラ**、スライム化で死んだ場合は **緑スライム**、コカトリスによって石化された場合は **石像** となります。英雄自身の死体も倒れた場所にそのまま残ります。
- 英雄が直接所持していたアーティファクト以外のアイテムは、**80%の確率で呪われた状態になります**。容器（鞄や箱）の中に入っていたアイテムには呪いはかかりません。装備したり武器として構えたりする前に、必ずペットによる呪い識別（ペットテスト）や祭壇での識別を行ってください。
- アーティファクトは通常のベースアイテムへと還元され、*クエスト・アーティファクト* は完全に消滅します。
- イェンダーの魔除けや3大召喚アイテム（開放の鐘、祈りの燭台、死者の書）を所持していた場合、それらは呪われた粗悪なイミテーションへとすり替えられます（「安っぽいプラスチックのイミテーション」の魔除け、白紙の魔法書、使いかけの蜜蝋のろうそく、ただの鐘など）。
- そのフロアに本来存在するはずのユニークモンスター（狂乱の魔法使い、メデューサ、ヴラド、クエストリーダーやネメシスなど）は除去され、ユニークモンスターの石像が存在した場合は同等のドッペルゲンガーへと置き換えられます。

**ボーンズ階の危険性。** 80%という高い呪い率は明白な危険ですが、より狡猾な脅威は「ボーンズ階のモンスターが、そのフロアの通常の難易度を遥かに超越している場合がある」という点です。前の冒険者を血祭りにあげた凶悪なモンスターがそのままフロアをうろついていることが多く、その深度には不釣り合いな強敵であることが多々あります。ボーンズ階で本来の出現深度を大きく超えるモンスターを見かけたら、交戦するのではなく退却の合図と捉えてください。勝てる準備が整うまで別の階へ退避し、後から戻ってきましょう。

**ボーンズを無効化する。** 設定ファイル（rcfile）に `OPTIONS=bones=false` を記述すれば、ボーンズのないクリーンな冒険が楽しめます。これにより、ボーンズの「生成（自分の死によってファイルが作られること）」と「読み込み（過去のボーンズ階を引き継ぐこと）」の両方が完全に遮断されます。自力達成の戒律である **ボーンズ不使用（Bonesless）** の導きを達成するためには、この設定が必須です。

### 即死の危険 (Ways to Die Instantly)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Food poisoning is from eating old/rotten corpses; giant ants are AD_PHYS only (monsters.h). Disease attacks (AD_DISE) belong to Juiblex/Demogorgon/Scorpius. Removed the giant-ant example.
- Verified correct: poison 6+d(4,6) extra HP & fatal-at-30, Famine drain rn1(40,40), touch_of_death 8d6+50, stoning/slime timers, disintegration armor order, reverse-genocide 4-6.
-->

迷宮には、現在の残りHPがどれほどあろうとも、たった1手でキャラクターを死に至らしめる要素がいくつか存在します。プレイヤーたちはこれらを「即死（instadeaths）」と呼びます。しかし、何に注意すべきかさえ知っていれば、ほぼすべての即死要因には1〜2ターン前の事前警告が存在します。

> *以下に掲載する即死カタログは、Dylan O'Donnell氏のRGRNファイルをもとにまとめたTrevor Powell氏の『即死スポイラー (Instadeath Spoiler)』に着想を得ています。Trevor氏は即死を「プレイヤーのヒットポイントが0まで削られる過程を伴わずに発生する、たった1手での死亡」と定義し、その分類体系は今日までスタンダードなリファレンスとして使われ続けています。*

#### 攻撃の杖 (Attack Wands)
<!-- audit
2026-05-18:
- mwandexp gates the first-zap warning miss (muse.c:1830-1860)
- buzz_force_miss is the dispatch path for the warning shot (muse.c:1815, 1834)
- 6 beam wands trigger the warning: death, sleep, fire, cold, lightning, magic missile (muse.c:1842-1847)
- the visible warning shot identifies the wand to the player
- late-game zones spawn monsters with mwandexp=TRUE — no warning shot (makemon.c:1290-1293)
- late-game zones: Stronghold, Knox, Quest, Gehennom, Vlad's Tower, endgame
-->

強力な杖による攻撃を受けることは、即死を意味する場合があります。死の杖や「死の指」の呪文は、適切な防御手段を持たないキャラクターを一瞬で絶命させます。また、冷気、炎、電撃、マジックミサイルの光線系の杖も、即死級の壊滅的なダメージを叩き出すことがあります。

**防御策：** 「反射」の能力はあらゆる光線を跳ね返します。「耐魔（魔法防御）」は死の光線およびマジックミサイルの光線を無効化します。通常、大半のモンスターがプレイヤーに対して光線系の杖（死、睡眠、炎、冷気、電撃、マジックミサイル）を最初に振る際、その初弾は必ず外れる仕様（警告射撃）になっています。モンスターが視界内にいれば、その瞬間に何の杖であるかが自動識別されるため、何が自分に向けて発射されたかを把握し、次の命中弾が飛んでくる前に対処するための1ターンの猶予が与えられます。ただし、城、要塞リュディオス、クエスト、ゲヘナ、ヴラドの塔、各大系などに自生する終盤のモンスターたちは、この初弾ミスの手加減をしてくれません。

#### 窒息 (Choking)
<!-- audit
2026-05-18:
- eat-while-satiated death via done(CHOKING) (eat.c:248, 286); warning string at eat.c:3314
- "Continue eating?" prompt only with paranoid_confirmation:eating (default off)
- death only fires at u.uhunger >= 2000 with 1/20 escape; Breathless never choke (eat.c:258-266)
- amulet of strangulation generates 90% cursed (mkobj.c:1063); beginner can't just take it off
- escape: pray, or uncurse via holy water or remove curse
- strangulation is a timer death via done_timeout(DIED, STRANGLED), not an attack — MR has nothing to block (timeout.c:890-894)
-->

「満腹（Satiated）」の状態を超えて無理に食べ続けると、喉を詰まらせて窒息死する危険があります。ゲーム画面には警告として「飲み込むのが苦しくなってきた（You're having a hard time getting all of it down）」というメッセージが表示されます。設定で食事の警告確認（`paranoid_confirmation:eating`）を有効にしていれば、確認プロンプトも表示されます。一定の栄養値上限を超えると、20分の1の確率で生還できるか、「無呼吸（Breathless）」の特性を持っていない限り、その食事によって即座に絶命します。

**窒息死に至るもうひとつのルートは「絞殺の魔除け（amulet of strangulation）」です。** 身につけると首に短いカウントダウンが始まり、時間が切れた瞬間に死亡します。この魔除けは90%の確率で呪われた状態で生成されるため、大抵の場合は単に手で外すことができません。神に祈る（`#pray`）か、聖水や「解呪」の手段を用いて呪いを解いてください。「耐魔（魔法防御）」はこの効果を防ぐ役には立ちません。ただし、「無呼吸」のモンスターに変身していれば助かります。

**防御策：** 満腹状態のときは決して食事をしないでください。また、未識別の魔除けを不用意に首にかけることには極めて慎重であってください。

#### 飢餓 (Starvation)

飢餓は厳密には「即死」ではありませんが、体感としては即死に極めて近いものです。栄養値が0まで落ち込むと、失神します。失神している間に何も食べられなければ、そのまま死亡します。食料供給の基盤が確立していないゲーム序盤において、飢餓は常に迅速な対応を迫られる命に関わる問題です。

**防御策：** 倒したモンスターの死体を迅速に食べてください。神の怒りを買わない状態（祈りのクールダウンが終わっている状態）であり、自分が「衰弱（Weak）」または「失神寸前（Fainting）」の状態であるなら祈ってください（神への祈りは空腹を全快させます）。常に保存食（食料、トリップフン、レンバスなど）を携帯してください。

ゲーム終盤、アストラル大系に出現する黙示録の四騎士の一角 **「飢餓（Famine）」** は、一撃ごとに40〜80の栄養値を直接削り取って急速にプレイヤーを飢餓死に追い込んできます。これを防ぐ外部装備は存在しません。アストラル大系には「満腹」の状態で突入し、決戦の最中も大量の携帯食糧を常時ストックしておいてください。さもなくば「飢餓」の一撃を受けた直後に失神寸前に追い込まれてしまいます。

#### 致死毒 (Deadly Poison)
<!-- audit
2026-05-19:
- AD_DRST extra-damage roll is ~1/240 per qualifying hit: rn2(8) × rn2(30) (uhitm.c:3154, attrib.c:362)
- poison death is purely `u.uhp <= loss`, no carrycap term (attrib.c:366) — burden is irrelevant
- poison resistance grants full immunity (attrib.c:338-343)
- Famine corpse is instantly fatal (eat.c:831-838)
-->

一部のモンスター（クサリヘビ、殺人蜂、コブラ、一部の蜘蛛など）は、通常の打撃ダメージに加えて 10〜30 もの追加HPダメージを与える猛毒攻撃の判定を持っています。最大HPが高い状態であれば耐えられることが多いですが、低レベルや手負いの状態では一撃で命を落とします。この「追加致死ダメージ」の抽選は、該当する毒攻撃が命中するごとにおよそ240分の1の確率で発生します。また、黙示録の四騎士（死、ペスト、飢餓）の死体を食べた場合、残りHPに関係なくその場で即死します。

**防御策：** [毒耐性](#damage-resistances) を持っていれば完全免疫となります。大半のキャラクターは、序盤に毒持ちモンスターの死体を適切に食べることで毒耐性を獲得できます。これはゲーム開始直後に真っ先に確保すべき最重要の内在能力のひとつです。
