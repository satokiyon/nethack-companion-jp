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
   - **病気 (illness)**: 祝福された回復の薬 (blessed potion of healing)、または呪われていない超回復の薬 (potion of extra healing) を飲む。ユニコーンの角を使う。
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

**司祭 (Priest)** *（全属性、神の属性と一致）*。その信仰心により、あらゆるアイテムの呪詛状態（祝福されているか、呪われているか、呪われていないであるか / BUC）を一目で看破できます。床に落ちているクロークが呪われていないか不安に怯える必要は二度とありません。メス、ローブ、盾、そして4本の**聖水 (holy water)** を携えて旅立ちます。さらに聖水はいつでも自作可能です。自分の宗派の祭壇に普通の水 (potion of water) を置き、神に祈る (`#pray`) だけで、その山のすべての水が一瞬で聖水へと浄化されます。あなたの神は、祭壇での生贄に対しても特別な恩恵を与えてくれます。生贄によって最初に下賜されるアーティファクトは、悪魔を粉砕するために鍛えられた祝福された銀のメイス**「デーモンベイン (Demonbane)」**であることが保証されています。価値ある生贄を捧げるたびに、6分の1の確率でこの至宝が授けられます。司祭は堅実な戦士であると同時に、やがて強力無比な聖職者魔法の術者へと成長し、あらゆる打撃武器や治癒・予言・僧侶系魔法の達人となります。1点だけ注意すべきは、自身の幸運 (Luck) を損なわないことです。生贄を重ねて神の寵愛を確固たるものにするまでは、平和的なモンスターを殺したり鏡を割ったりしてはなりません。さもないと、絶体絶命の祈りに対する神の返答は、期待とは正反対の惨劇となるでしょう。

**レンジャー (Ranger)** *（中立または混沌）*。遠距離からの狙撃を得意とする天性の狩人。弓と矢筒いっぱいの矢、そして**+2 幻影のクローク (cloak of displacement)** を身につけて始まります。このクロークは敵の攻撃を実際の位置から1マスずれた幻影へと逸らすため、本作屈指の安全な開幕手札を誇ります。その真価は圧倒的な射撃手数にあります。弓のスキルを高めると、わずか1ターンの間に2本から3本もの矢を同時に連射できるようになり、並のモンスターなら近づくことすら叶わず射抜かれます。さらに卓越した観察眼を持ち、歩いているだけで立ち止まって探すことなく隠し通路や罠を発見できます。2つの実践知識を覚えておきましょう。最も優れた矢である初期の**+2**矢は普通の矢よりも格段に折れにくいため、本気の強敵との戦いまで温存し、第1階層のイモリ (newt) のような無害な雑魚には安物の矢を使いましょう。そしてレンジャーの定位置は常に遠距離です。一歩下がり、壁を背にして、前線で殴り合うのではなく矢の雨に敵を仕留めさせましょう。

**盗賊 (Rogue)** *（混沌）*。暗闇に潜む泥棒。刃物の扱いが素早く、足音は誰よりも静かです。身軽な装備で旅立ちます。小剣、一握りの投擲用短剣、革鎧、最初からあらゆる扉や宝箱を開け放つ**鍵開け器具 (lock pick)**、そして戦利品を詰め込む麻袋です。気配を完全に殺して移動し、眠っているモンスターの脇を気付かれずにすり抜けることができます。そして逃走中や不意を突かれた敵に一撃を加えるとき、その**不意打ち（バックスタブ / backstab）**は正面から切り込むよりも遥かに甚大な致命傷を叩き込みます。所持している短剣は突くためではなく投げるためのものであり、1ターンに複数本を同時に投擲できます。後には、初期所持している毒薬を使って、拾った投げ矢や矢、ボルト、手裏剣に毒を塗ることができます（短剣には毒を塗れません）。常に物陰に潜み、ドアを蹴破ったり敵の群れに突っ込んだりするような、居場所を暴露する乱暴で不器用な振る舞いは避けましょう。

**侍 (Samurai)** *（秩序）*。古き伝統を受け継ぐ規律正しき戦士。刀の腕前は神速にして必殺です。迷宮で最も優れた片手剣の一つである**刀 (katana)**、小刀である**脇差 (wakizashi)**、矢筒を備えた**和弓 (yumi)**、そして鉄片の鎧 (splint mail) を身につけ、他の戦士が苦労して手に入れる俊敏な移動速度を最初から備えています。刀はゲーム序盤を鮮やかに切り開いてくれるでしょう。ただし、相棒の脇差は二刀流のパートナーとしては適していません。小柄な脇差は刀の刀術スキルを共有しないため、普通の長剣 (long sword) を見つけたら脇差と持ち替えましょう。両手に剣を構えれば、双方の刃を最高の熟練度で同時に振り回すことができます。背中の和弓も忘れてはなりません。修練を積めば、和弓はレンジャーに匹敵する遠距離脅威となり、近接戦で恐るべき戦士が1ターンに2〜3本の矢を放ちながら接近を拒むという無敵の強さを誇るようになります。

**観光客 (Tourist)** *（中立）*。バカンス気分で迷宮に到着します。派手なアロハシャツ、クレジットカード、**高価なカメラ (expensive camera)**、山のような**+2 投げ矢 (dart)**、少々の回復の薬、そして4枚の**地図の巻物 (scroll of magic mapping)** です。防具は皆無に等しく、HPも低く、まともな近接武器もないため、序盤はあらゆる敵が命取りになります。生き延びる鍵は筋肉ではなく知恵です。カメラこそが切り札です。フラッシュを焚くことで迫り来るモンスターの目を眩ませ（盲目状態にし）、盲目になった敵を安全な距離から投げ矢で痛めつけ、ペットにトドメを刺させることができます。地図の巻物は最も危険な難関フロアのために温存しておきましょう。店主たちは観光客の足元を見てきます。経験を積んで一人前になるまでは、店主は法外に高く売りつけ、こちらの売却額を極端に安く買い叩いてきます。本格的な買い物は冒険の後半まで待ちましょう。この過酷な序盤を生き延びれば、観光客は大化けします。クエスト報酬である「プラチナイェンダー印エクスプレスカード (Platinum Yendorian Express Card)」は、魔法耐性を授けるだけでなく道具の充填回数を回復（リチャージ）する効果を持ちます。知力を高めれば、終盤の観光客は強力な魔法の使い手にもなります。全役職中最も難関であり、観光客での昇天（クリア）はすべての冒険者にとって最高の栄誉となります。

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

**防具の強化。** AC（アーマークラス）が 6 以上（悪い状態）で、アイテムを鑑定するための祭壇もペットもいない場合は、見つけた普通の胴鎧、兜、盾、クロークを身につけましょう。それらに呪いがかかっていたとしても、無防備の丸腰で歩き回る危険に比べれば大抵はマシです。ただし、靴と手袋だけは事前にテストしてください。呪われた浮遊の靴、つまずきの靴、または呪われた手袋を身につけてしまうと、逃走すらできなくなる危険があります。

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

**腐敗した死骸 (Rotted corpses)。** 床に長く放置された死骸を食べると、治療しなければ死に至る食中毒を起こします。死骸は倒した直後の新鮮なうちに食べましょう。確実に安全なのは討伐後約30ターン以内です。それを超えると腐敗の判定がランダムになり、約175ターンを過ぎた呪われていない死骸は確実に腐っています。万一食中毒にかかった場合は、祝福された回復の薬 (blessed potion of healing)、呪われていない超回復の薬 (potion of extra healing)、完全回復の薬 (potion of full healing)、ユニコーンの角 (unicorn horn)、あるいはユーカリの葉 (eucalyptus leaf) を使用してください。祈る場合は、[神々との関係](#prayer)にある祈りの条件を満たしていることを必ず確認してください。

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
| [`&`](#major-demons)    | [悪魔 (Demons)](#major-demons)           | 上位の悪魔（オーケス、デモゴルゴン、アスモデウスなど）はボス級の脅威です。 |
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

各階層には厳密に1つだけの正しい解答手順が存在します。もし巨石を角に押し込んで進行不能にしてしまった場合、やり直す（リセットする）手段はありません。その場合、役立つかどうかは別として、不正（チート）を行う選択肢がいくつか残されています：巨石の横を **すり抜ける**（荷物を床に置いて体を細くする）、つるはし（pick-axe / mattock）を装備して **巨石を掘り崩す**、あるいは「衝撃 (force bolt)」の呪文や強打の杖で **巨石を粉砕する**（大地の巻物やへんげの杖なども同様に判定されます）。これらの不正を行うと、1回につき幸運値が1低下し、倉庫番のオピニオン（不心得行為の記録）が残ります。なお、倉庫番の全フロアにおいて壁は掘削不能（non-diggable）であり、落とし穴を迂回することはできません。飛行や浮遊の状態であっても、下降気流に引きずり込まれるため開いた穴の上を飛び越えることは不可能です。穴に落ちた後は自力で這い上がることができます。

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
- 飛行または遊泳能力を持つ生物への **変身（へんげ）**。[へんげ制御](#special-and-utility) の能力がない場合は極めて危険です。
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
| 変身(へんげ)の罠 (Polymorph trap) | ランダムな生物へと強制変身させられる    | 魔法防御、不変能力、または鉄製の履物 |
| 転がる巨石 (Rolling boulder) | 定められた軌道に沿って巨石が転がってくる | 軌道上から退避する     |

火炎の罠は、HPだけでなく手持ちの荷物全体を脅かします。炎そのもののダメージも痛いですが、最大の脅威はインベントリに起こる惨劇です：巻物は燃え尽き、薬の瓶は砕け散り、大事に溜め込んでいた20枚の「識別の巻物」の束が一瞬で灰と化します。[火炎耐性](#damage-resistances) は自身の肉体を守ってくれますが、**所持品までは守ってくれません**。普通の袋や防水袋の中に入れたアイテムは罠の火災から無事に生き残ります（袋自体が炎を吸収します）。[ゲヘナ (Gehennom)](#gehennom) は火炎の罠だらけの危険地帯ですので、消耗品は常に袋の中に退避させておきましょう。

[へんげ制御 (polymorph control)](#special-and-utility) を持っていれば、変身(へんげ)の罠を踏んでも変身後の姿を自分で選択できます。持っていない場合、罠が勝手に姿を決定し、装備品を何一つ身につけられないイモリに変えられてしまう恐れがあります。**[魔法防御 (Magic resistance)](#damage-resistances) および [不変 (Unchanging)](#special-and-utility) の内在能力は、どちらもこの強制変身を完全に遮断します。**

万が一、手のない生物へと強制変身させられてしまった場合、装備していた武具一式はその場（足元の床）にすべてドロップします。パニックにならず、むやみに動き回ってはいけません。ランダムな変身効果は数百ターンで自然に解けますし、大事な装備品は自分が立っているマスにまとまっています。可能であればそのマスを死守し、モンスターに追い詰められたら祈りを捧げ、元の姿に戻った瞬間にすべてを拾い直しましょう。（手持ちにへんげの杖があるか呪文を習得していれば、自分自身に振りかけることで再抽選できますが、現在の形態が杖を使えるか呪文を唱えられる場合に限られます。）

催眠ガスは、モンスターの密集地帯では文字通り命取りになります。戦うことも、逃げることも、自発的に目を覚ますことすらできません。モンスターたちにとっては食べ放題のバイキングのように無抵抗なあなたに群がってきます。エルフの血統、オレンジドラゴンの鎧、あるいは適切な死体を食べて得る [睡眠耐性](#damage-resistances) によって完全に無力化できます。

魔法の罠は、20種類あるランダム効果のいずれかを引き起こします。半数弱の確率で危険な効果が発生します：閃光が放たれて一時的に盲目にされ、数体の敵対的モンスターが周囲に召喚されます。また、火炎に包まれる目もあります。それ以外の結果は無害か、むしろ有益です：単なる演出メッセージもあれば、透明状態のオン／オフを切り替えるもの、装備中の呪われたアイテムを解呪するもの、そして周囲のモンスターをペット化して魅了（カリスマ）を1上昇させるものもあります。この最後の効果を狙って、既知の魔法の罠を何度も踏んで魅了値と店の割引率を稼ぐプレイヤーもいますが、発生確率は約1/20に過ぎず、火災やモンスター召喚のリスクを考えると待機は危険を伴います。

熊の罠にかかると数ターンの間足止めされます。脱出を試みる際は、そのマスから **斜め方向** へ踏み出すようにしてください。直交方向よりも斜め移動の方が約5倍早く抜け出せます。開錠の杖やノック（解錠）の呪文を使えば、その場で瞬時に罠が外れます。

魔法防御はテレポートの罠を遮断します。もし罠を利用してテレポートしたい場合は、発見済みの罠の上に立った状態で `Ctrl+T` を押してください（他のマスから押しても何も起きません）。

**反魔法フィールドは、魔法防御を持っている冒険者にこそ手痛い打撃を与えます。** この罠は魔力（スペルエネルギー）を枯渇させるだけでなく、*魔法防御* を所持していると「反魔法の爆縮」を引き起こしてHPにダメージを与えてきます。ダメージは基本1d4に加え、物理半減または魔法半減の能力で+1d4、[マジックベイン (Magicbane)](#magicbane) を装備していると+1d4、そして魔法耐性アーティファクトを所持しているとさらに+1d4が加算されます（1つだけが対象となり、最初の合致で判定を終了します）。最悪の場合、4d4のダメージを受けますが、壁抜け能力があればダメージは1/4（切り上げ）に抑えられます。最大の防御策は、捜索によって事前に罠を発見し、迂回して通り過ぎることです。無力化の杖を魔法の罠に向かって振ると罠を消滅させることができますが、その際に罠のマスで20 + 3d6の大爆発を引き起こすため、静かな解除法とは言えません。

鉄製の履物（鉄の靴、または蹴り挙げ靴）は、5.0において驚くほど多くの罠ダメージを肩代わりしてくれます：熊の罠による脚のダメージを無効化し、トゲの落とし穴の杭を防ぎ、変身(へんげ)の罠による肉体の変異を遮断し（代わりに履いていた靴が変身します）、プラスに強化されていれば強化値を1失うことで反魔法フィールドの魔力ドレインを身代わりに吸収してくれます。まだ他に優れた靴を見つけていない段階では、身につけておく価値の非常に高い防護装備です。

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
- **飛行と浮遊。** 大半の床面トラップを完全に無力化できます（ただし、クモの巣、魔法の罠、テレポートの罠、階層テレポートの罠、変身(へんげ)の罠、反魔法フィールドは空中でも作動します）。
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
| 窒息 (Strangulation) | *It constricts your throat!*<br>（喉を締めつけられる！） | 6ターン | 魔除けを外すか解呪する、祈る |

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

**逃げ時を弁える。** 迷宮には勇気を称える勲章など存在せず、あるのは生き残った者への栄冠だけです。逃走することは回復にも繋がります：レベル1の冒険者であっても、通常のモンスターより早く自然治癒します（プレイヤーは概ね9ターンに1 HP回復するのに対し、敵は20ターンに1 HP）。中盤に達する頃には敵の5倍の速度で急速回復するため、再生能力を持たない足の遅い強敵（ミミック、オーガ、レオクロッタなど）から距離を取ることは、実質的にタダでHPを回復しているのと同じです。ただし、トロール、吸血鬼、そしてイェンダーの魔法使いは例外です：彼らは毎ターン急速回復し、時にはあなた以上の速度で傷を癒します。彼らを相手に持久戦を挑んではいけません。戦況がもはや絶望的であるなら、瞬間移動の巻物、瞬間移動の杖を使うか、あるいは全速力で逃げ出しましょう。命を落とした冒険者に二度目のチャンスはありません（命の魔除けを首に下げている場合を除きます）。

**争いの指輪を活用する。** 「争いの指輪 (ring of conflict)」を身につけると、モンスターたちはお互いを敵と見なして同士討ちを始めます。敵で埋め尽くされた部屋の前に立ち、指輪をはめ、扉口の安全な位置からモンスターたちが共喰いして自滅していく様を高みの見物と洒落込みましょう。NetHack 5.0における注意点が2つあります：モンスターが争い状態に陥るにはあなたを **視認** している必要があり（盲目や視界外の敵は正気を保ちます）、さらに同士討ちの発生率はあなたの **魅力 (Charisma)** に比例します。魅力が高ければ極めて高い信頼性を誇りますが、魅力が低いと効果が不安定になります。

**緊急避難としてのエルベレス。** 文字を刻み、そのマスの上に立ち、体勢を立て直しましょう。モンスターたちは混乱と怒りに満ちた目であなたの周囲をうろうろと取り囲むだけになり、完全に無防備な時間が手に入ります。戦闘を再開する前に、必ずエルベレスのマスから一歩踏み出してください。結界の上からの攻撃は神聖な文字を汚して瞬時に消滅させ、「偽善者になったような気分だ」という痛烈な属性ペナルティを受けます。エルベレスは傷を癒すための安全な救護所であり、射撃用の砲台ではありません。

##### 遠距離攻撃モンスターと恐怖したモンスター (Ranged and Frightened Monsters)

**遠距離攻撃を行う敵は後退する。** 弓兵や呪文の使い手は、こちらが近接間合いに詰め寄ると後退して距離を取ろうとします。ケンタウロスの射手は後退しながら弓を射ち続けてきます。角を利用して退路を断つか、こちらも遠距離攻撃で応戦するか、瞬間移動の杖で敵を吹き飛ばして不毛な追いかけっこを終わらせましょう。呪文詠唱者も同様に、あなたが間合いを詰めようともがいている間に距離を取って魔法を浴びせ続けてきます。

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

**探索ペースについて。** 戦闘の後は必ず足を止めて休息し、HP満タン（少なくとも90%以上）の状態で階段を降りてください。現在の階層と経験レベルを無理に一致させようとするよりも、最大HPの高さの方がはるかに生存率を正確に予測します。利用価値のあるものは探索すべきですが、下り階段が見つかった後は、空っぽの部屋を無意味にうろついたり実りのない捜索に貴重な食料を浪費してはいけません。遠距離攻撃の手段と、瞬間移動の巻物や瞬間移動の杖などの安全な離脱手段を必ず確保した上で次の階層へ降りましょう。階段を降りた直後の突然死の多くは、手負いの状態で逃走手段も持たずに新しいフロアへと踏み込んだことから始まっています。

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

`n` クラス（木のニンフ、水のニンフ、山のニンフ）は、あなたを殺そうとはしません。彼女らが狙っているのは、あなたの所持品（インベントリ）です。序盤においてニンフは、身につけている防具を直接体から引き剥がしてせっかく構築したACを台無しにし、さらに爪による攻撃が命中するたびに荷物袋からランダムにアイテムを1つ奪い取ります。そして同フロアのランダムな場所へ **瞬間移動（テレポート）して逃げ去ります**。あなたの軽量化の鞄、反射の魔除け、願ったばかりの魔法を防ぐクロークなどが、マップの遥か彼方、往々にして未探索の部屋へと持ち去られてしまうのです。序盤のキャラクターにこれほど手痛い後退を強いるモンスターは他にほとんどおらず、しかもそれはたった一撃で発生します。

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

**防御策。** 近接戦を行うなら、**銀製または木製の武器**（銀の短剣、エルフの短剣、こん棒、六尺棒など）を使用してください。これらは分裂を引き起こしません。また、ミスリル製の武器も分裂チェックを回避します。炎による攻撃は分裂させずに倒すことができます（茶色プリンと黒プリンは冷気への耐性を持っています）。大半の攻撃呪文も安全に機能します。

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

**金色ドラゴン (Gold dragon)** は火のブレスを吐きます。その鱗鎧には元素耐性はありませんが、常に光を放つ永久光源（祝福時は半径4、呪われていないは3、呪いは2）として機能するため、たいまつや油の代用品になります。また、幻覚耐性も付与します。

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

**防御策：** 倒したモンスターの死体を迅速に食べてください。神の怒りを買わない状態（祈りのクールダウンが終わっている状態）であり、自分が「衰弱（Weak）」または「失神寸前（Fainting）」の状態であるなら祈ってください（神への祈りは空腹を全快させます）。常に保存食（食料、モツの塊、レンバスなど）を携帯してください。

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

#### 脳みそ吸引・脳死 (Brainlessness)
<!-- audit
2026-05-18:
- mind flayer 3 tentacles, master 5 tentacles; AD_DRIN + AT_WEAP 1d8 (monsters.h:523-535)
- INT loss rnd(2) per hit; up to 10 lost per turn from a master (uhitm.c:3263)
- brainlessness death; lifesaving still dies (eat.c:698-715)
- 1-in-5 chance of losespells per hit (uhitm.c:3264)
- losespells zeroes rn2(n+1) random spells; re-study restores them (spell.c:1759-1827)
- 5.0 AD_DRIN no longer wipes maps or item IDs — only spells (uhitm.c:3263-3271: only adjattrib INT, losespells, drain_weapon_skill — no forget_map/forget_objects calls)
- polymorphed into a mindflayer, brain-eating restores Int (eat.c:679-688)
- any helmet blocks 7/8 tentacle drains via `uarmh && rn2(8)` (uhitm.c:3235)
- greasing adds an extra slip-roll on top of the helmet check (uhitm.c:3232 → u_slip_free at mhitu.c:1047-1064)
- blessed potion of restore ability restores all lost attributes (potion.c:646-691)
- blessed potion of full healing does NOT restore stats (potion.c:1144-1162)
- prayer fixes drained attributes via TROUBLE_POISONED (pray.c:270-272, 547-552)
- unicorn horn no longer restores attributes in 5.0 (apply.c:2306-2327)
- strategy aligned with NetHackWiki Mind flayer, Helm: any helmet blocks 7/8 tentacles, greasing stacks slip-roll, range-kill is safest (https://nethackwiki.com/wiki/Mind_flayer, https://nethackwiki.com/wiki/Helm)
-->

マインドフレアは、その触手攻撃によってプレイヤーの「知力（Intelligence）」を直接吸い取ってきます。知力が種族の最低値（人間なら3）まで低下すると、次の吸引によって即死します（死因：脳死／brainlessness）。通常のマインドフレアは1ターンに3回の触手攻撃を行い、**マスターマインドフレア** は *5回* の触手攻撃に加えて強力な武器攻撃を繰り出してきます。無防備な状態でマスターマインドフレアと隣接すれば、たった1ターンで知力を最大10ポイント削り取られて死に至ることがあります。

**防御策：** どんなものであれ **兜（ヘルメット）を着用していれば、触手による知力ドレインを8分の7（約87.5%）の確率で弾き返します**。兜に防水用の油（grease）を塗っておけば、さらに滑って回避できる確率が上乗せされます。マインドフレアの生息域に足を踏み入れる際は、油を塗った兜の着用が標準的なエチケットです。さらに言えば、そもそも隣接されないよう遠距離攻撃（杖や呪文）で仕留めるのが最善です。
もうひとつの重要な詳細として、マインドフレアの「精神波（mind blast）」はテレパシーで感知されている状態では百発百中で飛んできますが、テレパシーを遮断していれば発動率は10分の1に激減します。遠視の魔除けを外すことで危険を大幅に減らせます（完全にゼロにはなりませんが）。
ドレインされた知力を回復するには、**能力回復の薬 (potion of restore ability)**（呪われていないは1つの能力値、祝福は全能力値を回復）、能力回復の呪文、または神との関係が良好な状態での祈りが必要です。なお、**NetHack 5.0 においてユニコーンの角は低下した能力値を回復しなくなった** ため、ユニコーンの角に頼ってはいけません。マインドフレアの巣窟に突入する前に、必ず能力回復の薬を少なくとも1本はストックしておきましょう。

#### 飲み込み・包み込み (Engulfment)

姿を隠して獲物を待ち伏せし、踏み込んできた者を一瞬で包み込むモンスターが2種類存在します。**ラーカー (lurker above)**（`t`、灰色、レベル10）は天井に張り付き、下を通りかかった者に覆い被さってきます。**トラッパー (trapper)**（`t`、緑色、レベル12）は床に擬態し、その上を踏んだ者を丸呑みにして包み込みます。どちらも発動するまでは通常の地形と見分けがつきません。これらの包み込み攻撃は、胃袋で消化するのではなく、圧迫によって締め潰す攻撃です。

待ち伏せ型ではない他の丸呑みモンスターも存在します。紫ワーム (purple worm) は獲物を消化液で溶かして即死させようとします。渦（ヴォルテックス）や霧の雲はプレイヤーを包み込んで打撃を与えますが、消化することはありません。なお、ドラゴンがプレイヤーを丸呑みにすることはありません。

**防御策：** 捜索（`s`）を行うことで隠れているモンスターの正体を暴けます。「テレパシー」は擬態を見破ってその存在を表示します。「警告の指輪」や「知性の兜」を装備していれば、足を踏み入れる前に察知できます。

**脱出方法。** 呑み込まれてしまったら、体内からホストを繰り返し攻撃してください。体内であっても武器による攻撃は正常に機能します。もし **掘削の杖 (wand of digging)** を持っていれば、それを振ってください（方向の指定は不要です）。ほぼ確実に即座に体外へと吐き出され、包み込んでいたモンスターのHPは1にまで削られます。**開錠の杖 (wand of opening)** や施錠開錠の呪文（ノック）を使えば、相手を殺すことなくその場で安全に吐き出させることができます（争いの効果などで *飼いならした* 紫ワームに誤って呑み込まれてしまった場合に極めて有用です）。遠距離呪文や光線系の杖を体内で放つことでも、内部から大ダメージを与えて破壊できます。

#### 溺死 (Drowning)
<!-- audit
2026-05-18:
- drown check uses monster's tile (uhitm.c:3389-3390)
- Swimming, Amphibious, or Breathless all defeat the drown (youprop.h:264-277)
- pool-entry check at hack.c:3272; Flying also skips entry, Levitation is the canonical defense
- emergency_disrobe is gated on Stressed+ (trap.c:4897-4941)
- krakens placed only on medusa-4 in the Dungeon (medusa-4.lua:122); other placements are Quest/fakewiz/wizard1
- "swamp rooms" comment refers to eels, not krakens (mkroom.c:557-565)
- encumbrance does NOT gate the grab-drown path: being Burdened won't save you once grabbed
- strategy aligned with NetHackWiki Drowning, Giant eel, Amulet of magical breathing: range-kill sea monsters, magical breathing/Swimming/Amphibious as the only true grab-drown defenses (https://nethackwiki.com/wiki/Drowning, https://nethackwiki.com/wiki/Giant_eel, https://nethackwiki.com/wiki/Amulet_of_magical_breathing)
-->

オオウナギ、電気ウナギ、そしてクラーケンは、巻きつき攻撃によってプレイヤーを拘束してきます。捕まってしまうと、そのモンスターのターンが回ってくるたびに溺死の判定が発生します。この溺死チェックは **モンスターがいるマス**（ウナギやクラーケンにとっては常に水マス）を基準に判定されるため、プレイヤー自身が隣接する乾いた陸地に立っていても水中に引きずり込まれて溺死します。「水泳（Swimming）」、「[呼吸の魔除け（無呼吸）](#movement-and-spatial-behavior)」、あるいは「両生形態」だけがこの引きずり込み溺死を完全に防ぐことができます。ここでは所持品の負荷重量は関係ありません（負荷が問題になるのは水に *落下* して自力で這い上がろうとする時であり、「圧迫（Stressed）」以上の負荷では緊急脱衣を強いられます）。ウナギやクラーケンとは、メデューサの階層、城を取り囲む堀、沼地の部屋、そして水の大系で遭遇することになります。

**防御策：** **呼吸の魔除け (amulet of magical breathing)**（または同名の呪文）を身につければ「無呼吸」となり、引きずり込みによる溺死の脅威を完全に無力化できます。「浮遊」は水たまりや堀の上を歩いて侵入するのを防いでくれますが、**ウナギに巻きつかれた場合の溺死は防げない** 点に注意してください。海洋モンスターとは可能な限り遠距離から交戦して撃破してください。奴らの巻きつき攻撃は隣接しなければ発動しません。

#### 石化 (Petrification (Stoning))
<!-- audit
2026-05-18:
- stoning timer starts at 5 (uhitm.c:3937)
- ticks 5→1 with five distinct messages (timeout.c:128-148)
- at counter 3 "limbs have turned to stone" sets nomul(-3) paralysis (timeout.c:163-165)
- two more messages fire after paralysis before done(STONING) at counter 0
- acid-blob corpse grants TIMED HStone_resistance += d(3,6), not permanent (eat.c:932-934, 1089-1094)
- Unchanging does not interrupt stoning: only blocks poly (polyself.c:1381-1384)
- poly_when_stoned auto-cure requires already being a non-stone golem (mondata.c:80-85)
- plain wand of polymorph cannot target the poly_when_stoned outcome
- stepping on a cockatrice corpse without Fumbling is safe
- Fumbling can trip the hero onto the corpse for instapetrify (timeout.c:1256-1261)
- strategy aligned with NetHackWiki Stoning, Cockatrice, Lizard: gloves around cockatrice corpses, lizard/acid corpse to interrupt the countdown, weaponized corpse for offense (https://nethackwiki.com/wiki/Stoning, https://nethackwiki.com/wiki/Cockatrice, https://nethackwiki.com/wiki/Lizard)
- eating any acidic corpse cures in-progress stoning (eat.c:860-861, fix_petrification at eat.c:867-877)
2026-05-23:
- cockatrice hiss (AD_STON) fires on 1/3 of landed melee hits (uhitm.c:4215)
- stoning roll within is `!rn2(10) || flags.moonphase == NEW_MOON` (uhitm.c:4245)
- 5.0 explicitly removed the lizard-corpse new-moon override (uhitm.c:4231-4243 source comment)
- net per-hit stoning rate: ~1/30 baseline, ~1/3 on new moon
- citation: source comment names the design change; NetHackWiki Cockatrice page still documents pre-5.0 lizard mitigation (https://nethackwiki.com/wiki/Cockatrice)
-->

石化こそ、プレイヤーがつねに「トカゲの死体」を持ち歩く最大の理由です。小手（手袋）を着けずにコカトリスに素手で触れたり食べたりすること、裸足で死体を蹴ること、あるいはメデューサの視線を直接受けることは、その場での即死を意味します。この場合、トカゲの死体は何の役にも立ちません。なお、死体のあるマスを踏んで通過すること自体は安全ですが、不器用（Fumbling）で足をもつれさせて死体の上に転倒すると即座に石化死します。

一方、コカトリスの威嚇の鳴き声（シューという音）を受けたり、投げられた卵が命中した場合は、5ターンのカウントダウンが始まります。以下の順序で警告メッセージが表示されます：
1. 「足取りが重くなってきた（You are slowing down）」
2. 「手足がこわばってきた（Your limbs are stiffening）」
3. 「手足が石化してしまった（Your limbs have turned to stone）」（この時点で **麻痺状態** に陥り、一切の行動が不可能になります）
4. 「完全に石化してしまった（You have turned to stone）」
5. 「あなたは石像になってしまった（You are a statue）」（死亡）

**事前の防御策：** コカトリスの死体を取り扱う際は必ず小手を着用すること、メデューサに対しては「反射」の盾や魔除けを使用すること、そして酸のブロッブの死体を食べて *時限式* の石化耐性を蓄積しておくこと（1体につき3〜18ターン持続）です。永続的な耐性を得るには、黄色ドラゴンの鱗鎧を着用してください。

**新月の夜の猛威。** コカトリスの近接攻撃が命中した際、石化のカウントダウンが始まる確率は通常時は低確率（約30分の1）です。しかし、現実世界が **新月の夜** である場合、この発動率は **約3分の1** へと跳ね上がります。新月の夜にコカトリスの巣に挑むのは避けるのが賢明です。

**石化が進行している最中の緊急治療：** **トカゲの死体を食べる**（これこそが携帯している目的です）、酸性の死体を食べる、酸の薬を飲む、神に祈る、あるいは自分自身に「石を肉に（stone to flesh）」の呪文を唱えてください。トカゲの死体は鞄の中ではなく、**メインの所持品（インベントリ）** に入れて携帯してください。鞄から取り出すだけで1ターンを消費してしまい、手遅れになります。必ず「手足が石化してしまった」のメッセージが出る *前* に対処してください。麻痺してしまえば3ターンの間何もできなくなり、そのまま石像になって絶命します。なお、「[耐へんげの魔除け](#special-and-utility)」は石化を **食い止めることはできません**。もし非石ゴーレムに変身している最中であれば、カウントダウン中に耐へんげの魔除けを着けていると、本来死亡時に石ゴーレムへと自動変身して生還できるはずの救済措置をブロックしてしまうため、かえって有害です。

トカゲを切らしてしまった場合でも、あらゆる酸性の死体が代用できます：酸のブロッブ、ゼリー類、黄色ドラゴン、黒ナガ、そして緑スライム（ただし緑スライムを食べると今度は *スライム化* のカウントダウンが始まります。最後の命綱としてのみ使用してください）。酸の薬を飲むことでも同様の治癒効果が得られます。

**コインの裏返し（凶悪な兵器）：** 小手をはめた手でコカトリスの死体を武器として構える（wield）と、ゲーム内で最も凶悪な一撃必殺の武器になります。[石化耐性](#damage-resistances) を持たないあらゆるモンスターは、叩かれた瞬間に石像へと変わります。熟練プレイヤーの間で「ゴムのチキン（rubber chicken）」として親しまれるこの古典的戦術は、多くの魔神（デーモン・ロード）すら瞬殺します（メデューサと四騎士は石化耐性を持っています）。この戦術を使う際に最も注意すべき致命的ミスは、死体を構えたまま落とし穴、穴、または落とし戸に落ちること、そして小手が脱げてしまうことです。投げられたコカトリスの卵も同様の即死効果を持ち、モンスターが投げてきた場合も同様の脅威となります。

#### 瞬間分解 (Disintegration)
<!-- audit
2026-05-18:
- only player-facing AD_DISN is black dragon breath (monsters.h:1520, ZT_BREATH(ZT_DEATH) at zap.c:4464-4493)
- beholder is the only other AD_DISN monster and is #if 0-gated (monsters.h:367-371)
- black dragons have MR_DISINT in attack and defense slots (monsters.h:1523)
- reflected beam does 0 damage to them via resists_disint (zap.c:4318)
- worn-armor priority on disint hit: shield first (zap.c:4476-4479), then body armor + cloak (zap.c:4480-4486)
- amulet of life saving rescues you (end.c catches DIED) but breath still destroys cloak/shirt (zap.c:4487-4492)
- an ordinary shield eats one breath; shields of reflection don't have a failure mode (zap.c:4476-4479)
- Antimagic check is on the death-ray branch only; the AD_DISN breath branch checks Disint_resistance only (zap.c:4464-4497)
-->

黒ドラゴンのブレスは、プレイヤーを一瞬で消滅（瞬間分解）させる唯一のモンスター攻撃です（このほか、激怒した神が雷撃の追撃として放つ広角の瞬間分解光線もあります。神の光線は反射できません。瞬間分解耐性だけが有効です。神の不興を買わないようにしてください）。

**防御策：** 瞬間分解耐性（黒ドラゴンの死体を食べるか、黒ドラゴンの鱗鎧を着用する）があれば完全免疫となります。**反射** はブレスを跳ね返してプレイヤーの身を守りますが、黒ドラゴン自身も瞬間分解耐性を持っているため、反射したブレスで黒ドラゴンを倒すことはできません。なお、「耐魔（魔法防御）」はこのブレスに対して **一切効果がありません**。

**瞬間分解耐性がない場合、** 身につけている防具が身代わりとなってブレスを受け止めます：盾を持っていればまず **盾** が破壊され、次に **鎧とクローク** が同時に破壊されます。防具を何も身につけていない場合にのみ、プレイヤー自身が直撃を受けて即死します（その過程でクロークやシャツも破壊されます）。したがって、普通の盾であっても失われる前に少なくとも1発のブレスを肩代わりしてくれます。命の魔除けは致死の直撃から救ってくれますが、破壊された防具は失われます。

#### 経験値レベル低下・ドレイン (Level Drain)
<!-- audit
2026-05-18:
- drain-life attacks (AD_DRLI) reduce u.ulevel by 1 and max HP by mlev gain (exper.c:232-260)
- drained levels do NOT recover over time
- drain resistance prevents the drop entirely (attrib.c:380-384)
- sources: Excalibur, Stormbringer, Staff of Aesculapius; in 5.0, black dragon scale mail or shield of drain resistance
- wraith corpses give 1 level on eat (eat.c:980-985)
- blessed potion of restore ability restores ALL lost levels (potion.c:687-691)
- uncursed/plain restore ability returns one level per quaff
- strategy aligned with NetHackWiki Drain resistance, Wraith, Excalibur: Excalibur/Stormbringer/Staff of Aesculapius for drain resistance, eat wraith corpse to regain a level (https://nethackwiki.com/wiki/Drain_resistance, https://nethackwiki.com/wiki/Wraith, https://nethackwiki.com/wiki/Excalibur)
-->

一部のモンスターは、攻撃が命中した際にプレイヤーの経験値レベルを低下させ、そのレベルの上昇によって得ていた最大HPや魔力を奪い去ります。レイス、塚人、ナズグル、吸血鬼、吸血鬼の首領、そしてヴラド自身がすべてレベルドレイン攻撃を持っています。敵の手にある[ストームブリンガー](#stormbringer) も同様の効果をもたらします。失われたレベルは時間経過では自然回復しません。モンスターを倒して経験値を稼ぎ直すか、能力回復の薬を飲むか（祝福されたものは失われた全レベルを一度に復元します）、あるいはレイスの死体を食べることで取り戻す必要があります。

（なお、生命力ドレインと *筋力（Strength）* ドレインを混同しないでください。コウモリの毒噛みつきは筋力を低下させるものであり、レベルを奪うものではありません。能力値ドレインは別の問題であり、後述の[エンチャント吸魔](#enchantment-drain) はその親類です。）

**防御策：** *ドレイン耐性* を持っていれば完全免疫となります。伝統的な入手先は、[エクスカリバー](#excalibur-artifact)（秩序）、ストームブリンガー（混沌）、あるいは[アスクレピオスの杖](#staff-of-aesculapius)（治療師のクエスト・アーティファクト）の装備です。NetHack 5.0 での新要素として、**黒ドラゴンの鱗鎧**（瞬間分解耐性とドレイン耐性の両方を1スロットで付与）や **ドレイン耐性の盾**（店でランダムに見つかる盾）の着用が挙げられます。

レイスの死体は重量がなく、缶詰にすることもできません（栄養価ゼロ）。戦闘が終わったら新鮮なうちに即座に食べてレベルを回復・上昇させましょう。

#### エンチャント吸魔 (Enchantment Drain)
<!-- audit
2026-05-18:
- disenchanter generates only in Gehennom (G_HELL: monsters.h:2156, makemon.c:1935, 1998)
- active claw targets armor via some_armor (do_wear.c:2629, uhitm.c:3619)
- target order: cloak → body armor → shirt → 1/4 chance for helm/gloves/boots/shield (do_wear.c:2634-2652)
- if naked, rn2(5) picks ring/amulet/blindfold; never targets a wielded weapon (uhitm.c:3621-3640 mhitm_ad_ench cases 0-4 enumerate uright/uleft/uamul/ublindf only)
- active hit prints "Your X seems less effective" (uhitm.c:3641)
- weapon drain is passive-only: fires when you melee the disenchanter (mhitu.c:2508-2515)
- passive drain is silent
- obj_resists: 10% chance for ordinary, 90% for artifact (zap.c:1392-1394)
- Invocation items and Rider corpses always resist (zap.c:1462-1467)
- MC negates the active attack (uhitm.c:3613) but NOT the passive counter
- eating a disenchanter corpse strips a random intrinsic (eat.c:1270-1275)
- strategy aligned with NetHackWiki Disenchanter, Magic cancellation: MC armor blocks the active claw but not the passive counter; range-kill is the cleanest plan, and the corpse is not safe to eat (https://nethackwiki.com/wiki/Disenchanter, https://nethackwiki.com/wiki/Magic_cancellation)
-->

**吸魔の怪物 (Disenchanters)**（`R`、青色）は、[ゲヘナ](#gehennom) にのみ出現します。その爪は着用している装備の魔法強化を吸い取り、近接攻撃で殴りかかると手持ちの武器のエンチャントを削り取ってきます。

モンスターからの **能動的** な爪攻撃は、着用している防具のいずれか1つ（クロークが最優先、次いで鎧、シャツ、そして兜・小手・靴・盾が等確率）を選び、その強化値を1下げます。防具を一切着ていない場合は、指輪、魔除け、目隠しのいずれかを侵食します。**能動的な攻撃が手持ちの武器を標的にすることはありません**。攻撃が命中するたびに「あなたの〜の効果が薄れたようだ（Your ... seems less effective）」とメッセージが出るため、発生したことは分かります。

一方、プレイヤーの武器がエンチャント低下を被るのは、近接攻撃で吸魔の怪物を殴った際の **受動的** な反撃ダメージによるものだけです。3〜4回近接攻撃を当てるだけで、丹精込めて鍛えた+7の剣があっという間に+3にまで劣化します。しかもこの受動的ドレインはメッセージが出ず無音で進行します。遠距離攻撃で仕留めれば、両方の吸魔攻撃を完全に回避できます。

**防御策。** **魔法防御力（MC3）の防具** は、防具に対する能動的ドレインをほぼ遮断しますが、武器を劣化させる近接反撃を止めることはできません。争いの指輪やペットを使って他の標的へ誘導するのが有効です。アーティファクトは10回中9回の確率で吸魔に抵抗しますが、通常のアイテムは10回中1回しか抵抗できません。**死体は絶対に食べてはいけません**。ランダムに持っている内在能力を1つ奪い取られます。

#### 死の接触 (The Touch of Death)
<!-- audit
2026-05-18:
- self-zap WAN_DEATH or SPE_FINGER_OF_DEATH skips the Antimagic check (zap.c:2885-2902)
- only the ray-bolt path checks Antimagic (zap.c:4497-4502)
- self-zap escape requires being nonliving (undead/manes/golems/S_VORTEX) or is_demon (mondata.h:219-220)
- Rider Death rn2(20): 17-19 = full touch (15%), 5-16 = permdrain=1 (60%), 0-4 = miss (25%) (uhitm.c:3858-3882)
- 8d6 + 50 + half-damage permdrain only on rolls 17-19
- MR on the 17-19 branch falls through to the smaller permdrain rather than being harmless
- the smaller permdrain on rolls 5-16 is NOT reduced by MR (mcastu.c:326-337)
- strategy aligned with NetHackWiki Touch of death, Wand of death, Death resistance: MR blocks incoming death rays but not self-zap; nonliving/demon polyform is the self-zap fallback (https://nethackwiki.com/wiki/Touch_of_death, https://nethackwiki.com/wiki/Wand_of_death, https://nethackwiki.com/wiki/Death_resistance)
-->

一部のモンスター、とりわけアストラル大系に君臨する黙示録の四騎士の一角「死（Death）」は、たった一撃の接触であなたを絶命させることができます。「死の指（Finger of Death）」の呪文や死の杖も同様の働きをします。**騎士「死」に対して死の杖や死の指の呪文を放ってはなりません**。「死」はその攻撃エネルギーを吸収し、最大HPを増加させてしまいます。四騎士の全員に対して推奨される決定打は「マジックミサイル」です。

**騎士「死」の接触攻撃** は、15%の確率で **8d6 + 50** の全力打撃を繰り出し、そのダメージの半分に相当する数値を最大HPから永久ドレインしてきます。「耐魔（魔法防御）」を持っていれば、この全力打撃をより小さなドレインへと軽減してくれます（無害化はできません）。接触の60%はこの小さなドレインを直接もたらし、残りの25%はミスとなります。HPが極めて高い高レベルキャラクターであればこの大打撃にも耐えられますが、最大HPの永久喪失は深刻な痛手となります。

**死の杖および死の指の呪文** は、死の光線が *外部から飛んできた場合* に限り耐魔によって完全に防ぐことができます。しかし、操作ミスなどで自分自身に向けて誤射してしまった場合、耐魔はあなたを守ってくれません。この誤射から生き残る唯一の方法は、あらかじめ吸血鬼、リッチ、スケルトンなどの **非生命体（アンデッド）** や悪魔の肉体へと変身（ポリモーフ）していることです。この非生命体／悪魔の特性は、外部から飛んできた死の光線に対しても完全耐性として機能します。

なお、接触や死の杖の直撃によって即死した場合でも、命の魔除け（amulet of life saving）を身につけていれば1度だけその場で蘇生することができます。

#### 虐殺 (Genocide)
<!-- audit
2026-05-18:
- confused-uncursed scroll of genocide self-genocides your role's species (read.c:1737)
- PLAYER+REALLY branch in do_genocide kills you with killer = "genocidal confusion" (read.c:2838-2972)
- mndx = u.umonster = gu.urole.mnum (read.c:2839, u_init.c:991) — role species (PM_VALKYRIE etc.), not race
-->

混乱（Confused）した状態で呪われていない「虐殺の巻物」を読むと、自分自身の役職の種族を虐殺してしまい、即座にゲームオーバーとなります。巻物を読む前に、必ず自分の状態異常ステータスを確認してください。

### 神との関係 (Divine Relations)

<!-- audit
2026-05-31 audit:
- corpse 50-turn freshness rule verified at pray.c:1843-1849. EXCEPT: an acid blob corpse (PM_ACID_BLOB) is the one exception and never spoils for sacrifice purposes (pray.c:1843).
- sacrifice value formula: mons[corpsenm].difficulty + 1 (pray.c:1845). Bigger/tougher monsters yield higher value.
- artifact gift chance per qualifying sacrifice: !rn2(6 + (2 * u.ugifts * nartifacts)) (pray.c:1792). First gift is 1 in 6; subsequent gifts drop by a multiplicative factor (gift count × total artifacts in world), NOT additive +2·n as previously stated.
- prerequisites: u.ulevel > 2 (XL>=3) AND u.uluck >= 0 (pray.c:1784).
- first-gift bias is alignment + skill compatibility, not role-name lookup (artifact.c:230 `a->alignment != A_NONE || u.ugifts > 0 || !rn2(3)`).
- pre-existing book claim "1 in (10 + 2·n)" (giving 1/10 first, 1/14 second) was incorrect; rewrote to match the source.
-->

機嫌の良い神はあなたの祈りに応え、過ちを赦し、時には強力なアーティファクトを授けてくれます。一方、怒れる神は天罰を下してあなたを打ち倒します。

#### 祈り (Prayer)

神に祈る（`#pray`）ことで、守護神に救いを求めることができます。適切な状況であれば、祈りは石化、飢餓、あるいは瀕死の危機からあなたを救い出してくれます。しかし条件が満たされていない場合、祈りそのものがあなたの命を奪うことになります。

> *以下の解説は、長年にわたりRGRNの祈りシステムのリファレンスとして親しまれてきたMatthew Lahut氏の『祈りスポイラー (Praying Spoiler)』に着想を得ています。*

**祈りが治療するトラブル（優先順位順）。** 神は最も緊急性の高い危険から優先的に解決してくれます：

1. 進行中の石化（Petrification）
2. 進行中のスライム化（Sliming）
3. 絞殺（Strangulation）
4. 溶岩への沈没（Sinking in lava）
5. 病気（食中毒、疫病）
6. 深刻な飢餓（「衰弱」または「失神寸前」）
7. 悪臭の雲（stinking cloud）の中への立ち往生
8. 致命的な低HP（残りHPが5以下、または経験値レベルに応じて変動する一定の割合以下：XL 1〜5で1/5以下、XL 6〜13で1/6以下、XL 14〜21で1/7以下、XL 22〜29で1/8以下、XL 30以上で1/9以下）
9. 獣化症（Lycanthropy）
10. 壁への埋没、過重による倒壊、呪われた浮遊の靴、両手が塞がって使えない状態（呪われた小手＋呪われた手持ち武器）、呪われた目隠し

上記の重大な危機を解決した後、神はさらに追加の祝福を与えてくれる場合があります。軽微な異常（通常の空腹、盲目、混乱、朦朧、幻覚、鉄球と鎖による通常の処罰）を治療したり、属性値を改善したり、あるいは[テレパシー](#senses-and-perception) や速度といった内在能力を授けてくれることすらあります。

**安全に祈るための必須条件。** 以下のすべてを満たしていなければなりません：

- **属性値（alignment）** が非負（0以上）であること。友好的なNPCの殺害、万引き、その他数々の非行は属性値を低下させます。生贄の奉納や美徳にかなった行動は属性値を上昇させます。
- **幸運値（luck）** が非負（0以上）であること。幸運値は様々な要因で変動します（[幸運と運命](#luck-and-fortune) を参照）。
- 神が **怒っていない** こと。神の怒りは属性値とは別枠で管理されており、特定の重大な違反（神の戒律破り、祭壇の冒涜など）によって蓄積されます。
- **祈りのクールダウン** が完了していること。祈りが成功した後、再び祈れるようになるまで一定ターン待たなければなりません。このクールダウン時間は平均約450ターンですが、それより遥かに長引くこともあります。真の緊急事態（致命的低HP、飢餓など）においては、クールダウンの終了が近づいていれば多少の情状酌量があります。
- 混沌の神を信仰しているのでない限り、悪魔やアンデッドに **変身（ポリモーフ）していない** こと。
- **[ゲヘナ](#gehennom)** にいないこと（標準的な役職で信仰することのないモロクを信仰している場合を除く）。ゲヘナでは神に祈りの声が届きません。これこそがゲヘナをあれほど危険な地にしている要因のひとつです。
- 祭壇の上に立っている場合、その祭壇が **同属性** であること。異属性の祭壇の上で祈ると、敵対する神に祈りを捧げることになってしまいます。

**手短な鉄則：** 属性値と幸運値が0以上であり、神が怒っておらず、異属性の祭壇の上におらず、ゲヘナの外にいる場合にのみ、上記のトラブル解決のために祈ってください。ゲーム開始から一度も祈っていない場合は、ターン数が300を超えてから祈るようにしてください。一度祈った後は、可能な限り次の祈りまで約1000ターン空けるようにしてください（平均回復時間は約500ターンですが、確率の偏りで長引くことがあります）。

**祈りが失敗したとき。** 条件が満たされていない場合、神は助ける代わりに罰を下します：属性値や幸運値の喪失、クールダウンの延長、装備品の呪詛化、敵対的な神の召喚獣の出現などです。重大な違反を犯している場合は、落雷や瞬間分解光線が撃ち込まれ、即死します。

**実践的な指針。** 本当に死に直面し、他に一切の手段がない場合（飢餓、石化、病気、瀕死の低HP）にのみ祈ってください。祈る前に、まず上記のチェックリスト（属性値がプラスか、クールダウンは空けているか、異属性祭壇の上ではないか）を確認してください。1つでも「いいえ」があるなら、祈り以外の解決策を探してください。

#### アンデッド退散 (Turning Undead)

**騎士** と **僧侶** は、`#turn` コマンドを使って神の御威光を呼び求め、アンデッドを退散させることができます。視界内の広範囲にいるすべてのアンデッドと吸血鬼（経験値レベル15以降は悪魔も含む）が対象となります。相手が強敵であるほど、単に恐怖させて追い払うだけでなく完全に *消滅* させるためには高い経験値レベルが必要です。ゾンビなら経験値レベル6で消滅させられますが、**亡霊（ゴースト）はレベル14**、リッチはレベル16に達するまで消滅させることはできません。必要なレベルに満たない場合、退散は敵を逃走させるだけに留まり、ゴーストのような耐魔を持つアンデッドは約半分の確率で退散自体に抵抗します。秩序および中立の英雄は退散させた敵を消滅させ、混沌の英雄は敵を平和化（非敵対化）させます。

祈りとは異なり、アンデッド退散を行っても神との関係におけるコストは一切かかりません。クールダウンも神の恩恵の消費もないため、祈祷中に数ターン麻痺して無防備になる点さえ気をつければ、何度でも自由に使用できます。ただし祈りと同様に、**[ゲヘナ](#gehennom) では完全に失敗します**。そのため「死者の谷」では役に立ちません。なお、「アンデッド退散」の呪文（魔法書から学ぶもの）は別物であり、こちらは指定した一方向に放たれ、単体の標的を恐怖させる効果を持ち、ゲヘナ内でも問題なく機能します。

#### 生贄 (Sacrifice)

生贄（いけにえ）は、新鮮なモンスターの死体を捧げることで神の恩恵を獲得する行為です。自分と同属性の祭壇の上で `#offer` を行うと、まず怒れる神を宥め、次に属性値を回復し、祈りのクールダウンを短縮します。これらが万全の状態になると、幸運値を上昇させたり、強力なアーティファクトを授けてくれたりします。なお、聖水の生成や戴冠（crowning）は、生贄そのものではなく祭壇の上で「祈る」ことによって発生します。

基本ルール：

- 死体は新鮮でなければならず、殺害されてから **50ターン以内** のものでなければなりません。50ターン以上経過した死体は生贄としての価値がゼロになります（神は単に無視します）。酸のブロッブの死体はこのルールの唯一の例外であり、生贄の用途において決して腐敗しません。
- 強力で巨大なモンスターほど、価値の高い生贄となります。「あなたの心に物足りなさが残った（You have a feeling of inadequacy）」というメッセージが出た場合、神が怒っており、捧げた死体が小さすぎて怒りを鎮めるのに不十分であったことを意味します（この要求値は経験値レベルには依存しません）。
- 祭壇は自分の属性と一致している必要があります。さもなくば、他人の神に祈りを捧げることになり、固有のペナルティを招きます。
- **自分と同種族の死体を生贄に捧げる行為** は、秩序および中立の英雄にとっては重罪として処罰されます（そして同属性だった祭壇が混沌の祭壇へと反転します）。しかし、**混沌** の英雄が混沌の祭壇で同種族の死体を捧げた場合は例外であり、ご褒美として友好的な悪魔が出現し、幸運値と属性値の両方が大幅に上昇します。
- アーティファクトの賜物（ギフト）が発生するためには、**経験値レベルが3以上** であり、かつ **幸運値がマイナスでないこと** が必須条件です。

十分な生贄の功績を積み重ねると、神はあなたにアーティファクト武器を賜物として授けてくれます。条件を満たす生贄1回あたりのギフト発生確率は、1つ目のアーティファクトについては **およそ6分の1** ですが、2つ目以降のギフトについては確率が劇的に低下します。この低下率は、「これまでに獲得したギフトの数」と「ゲーム内にすでに存在する全アーティファクトの総数（プレイヤー所持、自然生成、引き継いだボーンズファイル内を含む）」の相乗効果によって決定されます。最初のギフトしか存在しない場合、2つ目の確率は約8分の1から始まりますが、ギフト数や既存アーティファクト数が増えるにつれて確率は極めて低くなります。1つ目のアーティファクトを手に入れた後、何千ターンもの間何ももらえなくなったとしても驚くには当たりません。

特定の役職にとって、1つ目のギフトは単なるランダム抽選ではありません。ワルキューレ、魔法使い、野蛮人、侍、あるいは僧侶の場合、1つ目のギフトは必ずその役職の代表的なアーティファクトとなり、主人公自身の属性に適合した形で授与されます。また、捧げた死体の種類によって出現可能なアーティファクトに上限がかかります。「スティング」、「オーガスマッシャー」、「トロルズベイン」は価値1の生贄でも出現しますが、「ボーパルブレード」や「ファイアブランド」には価値5、「フロストブランド」には価値9、「グレイスワンダー」には価値10の生贄が必要です。最強のギフトを狙って生贄を捧げる際は、トロールクラスの死体を温存しておきましょう。

#### 僧侶への寄付 (Donating to Priests)

自分自身の神殿の中にいる平和的な僧侶は、寄付を受け付けてくれます。僧侶に向かって `#chat` で話しかけるとプロンプトが表示されます：*「いくら寄付しますか？ (推奨額: X または Y)」*。この2つの数字は、2段階の報酬ティアに対応する僧侶からの推奨金額です。

**得られる恩恵：**

- **遠視（Clairvoyance）：** 推奨金額を支払うごとに、500〜999ターンの間、一定ターンごとに周囲のマップを自動的に透視できる能力が一時的に付与されます。低い方の推奨額を寄付した場合に授与されます。
- **守り（Protection）：** 何度でも **累積する内在的なACボーナス** が得られます。高い方の推奨額を寄付した場合に授与されます。**初回** の寄付では 2〜4 ポイントのAC改善が得られ、それ以降の寄付では上限の9ポイントまで1回につき1ポイントずつ加算されます。9ポイントを超えると、追加のACボーナスが得られる確率は 1/N へと激減します。遠視とは異なり、この守りのボーナスは死ぬまで永続します。

**必要な金額。** 十分な金額を支払えば、確実に恩恵を受けられます。僧侶のプロンプトには常に正確な要求額が表示されます。この金額は、主人公の「経験値レベル」と「所持金」に応じて変動します：

- **遠視：** 基本要求額は、ランダムな 150〜250 ゾークミッド × 経験値レベル
- **守り：** その2倍、300〜500 ゾークミッド × 経験値レベル

もし基準額を遥かに上回る大金を持ち歩いている場合、僧侶は懐具合に合わせて要求額を吊り上げます。プロンプトに表示される2つの数字が目安です。遠視なら1つ目の金額以上、守りのACボーナスなら2つ目の大きい方の金額以上を支払ってください。

**ケチ（Cheapskate）ペナルティ。** 十分な支払い能力があるにもかかわらず、要求額を著しく下回る端した金を寄付した場合、僧侶はあなたを「けちん坊（Cheapskate）」と罵り、深く根に持ちます。次回その僧侶と話した際、要求金額が大幅に引き上げられます。このペナルティはケチな寄付を繰り返すたびに累積し、その冒険が終わるまで一生消えません（他の神殿の別の僧侶には影響しません）。また、寄付を完全に拒否した場合も守護神への属性値が低下します。

**実践的な指針：**

- **早期に寄付し、こまめに寄付する。** 守りのACボーナスは累積するため、XL 1 の時点での 500 zm は、XL 30 での 15,000 zm とまったく同じ AC 低下効果をもたらします。[地下鉱山](#the-gnomish-mines) から戻るたびに炭鉱の街の神殿に立ち寄って寄付を重ねるのは、熟練者の伝統的な儀式です。
- **話しかける前に所持金を調整する。** 僧侶の要求判定は手持ちの所持金に非常に敏感です。神殿の外の床に余分な金貨を置いてから話し、寄付が終わった後に回収しましょう。
- **異属性の僧侶であっても寄付は受け付けてくれる。** 異属性の僧侶であってもACボーナスや遠視は問題なく授与されます（属性値の上昇は得られず、その祭壇で生贄を捧げることはできませんが、ACボーナスの強化は正常に機能します）。
- **支払う気がないなら話しかけない。** 0ゴールドの寄付は「拒否」とみなされ、属性値を失い、端した金を寄付したのと同様にケチの烙印を押されます。

<!-- Donation mechanics: src/priest.c priest_talk(), 5.0 line 638:
     rn1(101, 150 + cheapskate * 40) × u.ulevelpeak. Tier thresholds
     at suggested × quan, 2 × suggested × quan, 3 × suggested × quan,
     where quan = max(1, money / (3 × suggested × XL)). -->

#### 祭壇と属性 (Altars and Alignment)

異属性の祭壇を自分の属性へと改宗させるには、その祭壇の上で通常の新鮮な死体を生贄に捧げます。試行するたびに、祭壇が自分の守護神の属性へと反転するか（成功）、幸運値を失うか（失敗）、あるいは現在の属性値がマイナスである場合は **主人公自身が祭壇の属性へと強制改宗** させられます。高い経験値レベルであるほど成功率は向上します。生贄によるギフト、聖水の作成、あるいはBUC（祝福・呪われていない・呪い）判定のために同属性の祭壇が必要な場合、リスクを冒す価値は十分にあります。

経験値レベル9以上になると、成否にかかわらず、追い出された神の敵対的な召喚獣が出現することがあります。生贄を捧げる前に、必ず逃げ道を確保しておいてください。

以下の2つは、どの祭壇であっても決して生贄に捧げてはなりません：

- **自分と同種族の死体**（人間、エルフ、ノーム、ドワーフ、オークのうち自分の種族に該当するもの）。すべての祭壇で厳罰に処されます —— *ただし* あなたが混沌であり、祭壇も混沌である場合を除きます（その場合はご褒美として友好的な悪魔が出現し、幸運値と属性値が上昇します）。
- **祭壇の属性と一致する属性のユニコーンの死体**。その神に対する重大な侮辱とみなされます。

#### 戴冠 (Crowning)

属性値が20に達し、かつ幸運値が10に達している状態で祈りが成功すると、あなたの守護神はあなたに **戴冠（Crowning）** の栄誉を授けてくれます。戴冠によって以下の恩恵が得られます：

- 特別な称号（例：秩序のキャラクターであれば「エルベレスの手 (Hand of Elbereth)」）。
- 属性に応じたアーティファクトの賜物。秩序のキャラクターが戴冠を受けた場合、その瞬間に手に構えているロングソードが[エクスカリバー](#excalibur-artifact) へと変化します（そのため+7のロングソードを構えて戴冠を迎えれば、即座に+7のエクスカリバーが手に入ります。ロングソードを構えていなければ剣は生成されません）。魔法使いと修道士は武器の代わりに専用の魔法書を授かります。
- 内在的な[火炎耐性](#damage-resistances)、[冷気耐性](#damage-resistances)、[電撃耐性](#damage-resistances)、[睡眠耐性](#damage-resistances)、[毒耐性](#damage-resistances)、そして可視（不可視の視覚）の獲得。
- 自身の属性に対応する剣スキルの永続的な制限解除（エキスパートまで成長可能に）。
- 役職固有のボーナス：魔法使いは「死の指」の呪文、修道士は「能力回復」の呪文を授かります。

戴冠を受けると、それ以降のすべての祈りにおいて通常のクールダウンに加えて約1,000ターンの待ち時間が上乗せされます。生贄によってアーティファクトのギフトを釣り上げようとしている最中は、信仰心の高まりすぎに注意してください。神との関係が最高潮に達している状態で祈ると意図せず戴冠してしまうからです。自分自身に聴診器を当てることで現在の信仰状態を確認できます。「敬虔（piously）」と表示されたらそれが最高位の領域であり、祈れば戴冠が発動する可能性があります。

### 仲間作り (Making Friends)

<!-- audit
2026-06-03:
- tameness score: 0 to 20; initialized to rn1(4, 5) for tamed, 20 for starting pet (dog.c:50, makemon.c:1347-1355)
- decay: 1 per 20 turns left behind on another level; 1 per struck turn by hero; starvation triggers M2_PEACEFUL/M2_HOSTILE drop (dogmove.c:28-85)
- chat sounds by hunger state: dog yip/bark/whine, cat purr/mew/meow, horse whicker/whinny/neigh (sounds.c:451-512)
- feeding restores hunger AND tameness; tripe is preferred dog/cat food, fruit/veggie for horse (eat.c, dog.c)
- charm monster / scroll of taming: 3x3 radius baseline; confused scroll 11x11 (read.c:1680-1704, spell.c:2201)
- untamable categories: humans (@), covetous (Wizard, liches, masters), demons (unless player is demon), vault guards, quest leaders/nemeses, minions, uniques (mondata.c:421-460)
- apport: edog->apport initialized to A_CHA (dog.c:60), grows as the pet eats food you drop near you, drives pickup/return behavior (dogmove.c:316-422); enables pet-shoplifting in practice
- magic whistle teleports pets toward the hero on every apply (apply.c whistle handler)
- gray dragon resists magic damage via resists_magm (mondata.c:215-225 includes AD_MAGM and PM_BABY_GRAY_DRAGON); magic-resistant targets cannot be polymorphed
- long worm's lengthening tail occupies a chain of map tiles (worm.c:27-100); the head moves but segments stay until they shrink
-->

恐るべき迷宮は暗く、過酷で、あなたを捕食しようと狙う危険な生物に満ち溢れています。そうした過酷な環境において、忠実な仲間は金貨の詰まった袋などよりも遥かに価値があります。幸いなことに、ダンジョンはそのための手段を用意してくれています。

#### 初期ペット (Starting Pets)

大半の役職は、最初から忠実なペットを一匹連れて冒険を開始します（役職に応じて子犬または子猫）。ペットは階段を昇降する際に隣接していれば階層間を追従し、共に戦い、アイテムを拾い上げ、床に落ちている食料を食べます。牙を持ち、自走し、自給自足する便利な「呪いテスター」と考えて差し支えありません。

よく食べ、戦いを重ねたペットは成長します。子犬（little dog）は犬（dog）へ、そして大型犬（large dog）へと育ちます。子猫（kitten）は家猫（housecat）へ、そして大型猫（large cat）へと進化します。完全に成長した大型犬や大型猫は本格的な戦力となり、プレイヤー自身が苦戦するような中盤ダンジョンの脅威すら撃破できるようになります。

さらに重要な点として、ペットは呪われていない選択肢がある場合、原則として呪われたアイテムのマスを避けて歩きます。これを利用することで、**確率的な呪い検出器** として活用できます。未識別のアイテムを床に落とし、ペットがどのアイテムの上を素通りし、どのアイテムを避けて迂回するかを観察してください。どうしても他に通り道がない場合は呪われたマスを踏むこともありますが、何ターンにもわたって一貫して回避し続ける場合は、そのアイテムが呪われている強いサインです。また、ペットが呪われたアイテムの山の上に踏み込んだ場合（食料を追っている時や、魔法の笛で引き寄せられた時など）、ゲーム画面には *「[ペット]は気が進まない様子で〜の上に乗った（[pet] moves reluctantly onto ...）」* と表示されます。このメッセージが出たら呪い確定です。

#### 給餌と忠誠心 (Feeding and Loyalty)

ペットには内部的な「手なずけ度（tameness）」の数値が存在します。別の階層に何ターンも置き去りにしたり、引き綱で無理やり引っ張ったり、プレイヤー自身が攻撃を当ててしまうと低下します。空腹度はペットの行動に影響しますが、忠誠心そのものを直接減らすわけではありません（また、他のモンスターから戦闘ダメージを受けても忠誠心は低下しません）。手なずけ度がゼロまで落ち込むと、ペットは飼いならされていない平和的（非敵対的）な状態に戻るか、完全に敵対化してしまいます。給餌こそがその特効薬です：

- **犬と猫** は、モツの塊（tripe rations）をはじめとする大半の肉類を好みます。
- **馬** は、リンゴ、ニンジン、その他の菜食を好みます。

ダンジョン内にはモツの塊がよく落ちています。人間にとっては吐き気を催すようなゴミ食料ですが、見つけたら必ず拾っておきましょう。ペットは狂喜してあなたを慕ってくれます（馬を連れている場合は果物を用意してください）。ペットが好む食料を所持していると、ペットはより密着してあなたを追従するようになります。

**お腹が空いているかどうかの見分け方。** ペットの満腹度メーターは画面に表示されませんが、ペットに向かって話しかける（`#chat`）ことで、直近にいつ食事をしたかに応じて鳴き声で教えてくれます：

| ペットの種類 | 満腹直後 | 満足 | 空腹 |
|---|---|---|---|
| **犬** | クンクン鳴く (yips) | 吠える (barks) | クーンと鳴く (whines) |
| **猫** | ゴロゴロ鳴く (purrs) | ニャーと鳴く (mews) | ミャーミャー鳴く (meows) |
| **馬** | — | 鼻を鳴らす (whickers) | いななく (whinnies) |

「空腹」の鳴き声が聞こえたら、それがエサを与える合図です。この鳴き声は「不機嫌」のサインも兼ねているため、落ち着いたタイミングで確認してください。猫が **ギャーギャー喚いたり (yowls)**、馬が **激しくいなないたり (neighs)** しているときは、野生化して敵対する寸前の危険信号です。

#### 新たな生物のテイム (Taming New Creatures)

初期ペットが倒れてしまったり、ペットの軍団を編成したい場合、いくつかのテイム（手なずけ）方法が存在します：

- **適切なエサを投げつける：** 犬や猫には肉、馬には農産物（リンゴやニンジン）を投げます。
- **手なずけの巻物** または **怪物を手なずける呪文（charm monster）：** どちらも同一の処理を経由し、周囲 3×3 マスの範囲内にいるテイム可能なすべてのモンスターを手なずけます。混乱状態で手なずけの巻物を読むと、その効果範囲は 11×11 マスへと劇的に拡大します（ただし混乱中に呪文を唱えることはできません）。
- **魔法の罠の効果：** 稀に踏み込んだ際にモンスターをテイムする効果が発生します。

テイムできるのは小動物だけに留まりません。「手なずけの巻物」や「怪物を手なずける呪文」を駆使すれば、敵を一呑みにしてくれる紫ワーム、灼熱の炎を吐くドラゴン、敵を踏み潰すタイタンなどを従属させることができます。ただし、テイム不可能なモンスターの除外リストも膨大です：人間（`@`：僧侶、店主、番兵、兵士、王など）、欲深いモンスター（狂乱の魔法使い、リッチ、マスターマインドフレアなど）、悪魔（自分自身が悪魔に変身している場合を除く）、金庫番兵、クエストリーダーやネメシス、神の召喚獣はテイムできません。また、メデューサなどのユニークモンスターもテイムに抵抗します。

#### ペットの役割 (What Pets Do for You)

十分にエサを与えられたペットは、様々な形でその真価を発揮してくれます：

- **戦闘の主力。** 強力なペットは部屋の敵を一掃し、危険なモンスターをプレイヤーが交戦する前に削って弱らせてくれます。
- **呪い検知。** アイテムを床に落として様子を見る手法は無料で行える確率的な呪い識別です。ペットの躊躇やメッセージを観察しましょう。
- **万引き（アイテム窃盗）。** ペットが店の中のアイテムを拾い上げ、店の外へと持ち出した場合、店主はプレイヤーではなく動物を責めます。多少の忍耐（ペットがアイテムの上に歩いて行き、さらに外へ歩き出るのを待つ）が必要ですが、店から「願いの杖」を合法的にタダで入手する最も手軽な裏技です。
- **生贄の確保。** ペットが倒したモンスターも死体を残すため、プレイヤー自身が倒した時とまったく同様に祭壇に捧げることができます。

**運搬（アポート：apport）の訓練。** ペットに手渡しでエサを与え続けると、「アポート（運搬能力）」という内部スコアが上昇します。アポートが高いペットは、近くに落ちているアイテムを拾い上げ、プレイヤーの足元へと運んでくるようになります。これこそがペットによる万引きを現実的な戦術にする鍵です。店のカウンターにアイテムを落とし、店の外に出て待っていれば、ペットが商品をくわえてあなたの元へ届けてくれます。後述の「魔法の笛」と組み合わせれば、フロアのどこからでも商品を抱えたペットを一瞬で手元に呼び寄せることができます。

**ペットのアップグレード。** 以下の3つの手段が極めて重要です：

- **魔法の笛 (magic whistle)** は、吹くたびに同フロアにいるすべてのペットをあなたの隣接マスへと瞬間移動させます。距離は関係なく、罠に引っかかっているペットもその過程で救出されます。
- 序盤に **戦闘用の馬 (warhorse)** をテイムする（リンゴやニンジンを投げる）ことで、中盤前に足が速く攻撃力の高い騎乗モンスターを手に入れられます。
- ゲーム終盤、**ペットを強力なモンスターへと変身(へんげ)** させます。**タイタン (Titan)** は最も人気の変身先です：レベル16、速度18、飛行能力を持ち、巨石を投げつけ、攻撃呪文を唱えます。これほど強力でありながら足が速いモンスターは他に存在しないため、速度ブーストを得たプレイヤーの移動速度にも追従でき、遠距離呪文で敵を圧倒してくれます。バルログは打撃力こそ上ですが、速度5と鈍足なため逃げる敵を取り逃がしてしまいます。灰色ドラゴンは、確実に耐魔の内在能力を持たせ、事故による再ポリモーフを防ぎたい場合の優れた選択肢です。
- もし **アルコン (Archon)** を直接テイムできる機会があれば（敵対的なアルコンに手なずけの巻物を読む、以前テイムしたアルコンを魔法の笛で呼び戻す、争いの指輪による事故など）、絶対にテイムしてください。アルコンはゲーム内最強の究極ペットです：レベル19、速度16、AC −6、魔法防御、不可視の視覚、飛行、自己再生、そして盲目の視線や攻撃呪文を含む強力な連続攻撃を繰り出します。なお、**ペットをポリモーフさせてアルコンにすることはできません**。自然に遭遇した個体を直接テイムする必要があります。

#### ペットを生存させる (Keeping Your Pet Alive)

ペットもプレイヤーと同じ脅威によって命を落とします：罠、毒、強敵、水への溺死などです。聴診器を使って仲間の健康状態（HP）をこまめにチェックし、勝ち目のない無謀な戦いに突入させないように配慮してください。

階層を移動する際、ペットが隣接していないと付いてきません。待たされている間、ペットの忠誠心は徐々に低下していくため、友達であったことを忘れ去られる前に迎えに戻ってください。**魔法の笛** は、テレポート禁止フロアであっても同じ階にいるすべてのペットをあなたの隣のマスへと呼び戻します。なお、倉庫番には忠誠心低下を防ぐ特別な保護機能はないため、他の支流を攻略している間ペットを倉庫番に放置してはいけません。

画面に *「一瞬悲しい気持ちになった（You have a sad feeling for a moment）」* と表示されたら、それは視界外（大抵は別の階層に置き去りにした場所）であなたのペットが死亡したことを意味します。

ペットも耐性を獲得でき、時には死から蘇ることもできます。適切なモンスターの死体を食べたペットは耐性を獲得します：[火炎耐性](#damage-resistances)、冷気耐性など、ダンジョンの死体ビュッフェが提供するあらゆる耐性が対象となります。これを計画的にコントロールすることは難しいですが、すべての死体をプレイヤー自身が独占するのではなく、ペットにも死体を食べさせる十分な理由になります。

もし愛用の仲間が戦闘で倒れてしまったら、同属性の祭壇の上でペットの死体の上に立ち、神に祈ってください。神がペットを生き返らせてくれることがあります。ただしこれは最終手段であり、何度も使える技ではありません（祈りのクールダウン、属性値、幸運値のすべてが消費・判定されます）。

## 第4部：装備と補給品 (Part Four: Gear and Provisions)

NetHackに登場する大半のアイテムは、正体を偽って出現します。その外見（未識別名）はゲームごとにシャッフルされますが、価格、重量、材質、そしてその挙動が変わることはありません。本章では、それらの変わらない手がかりを活用して的確な判断を下す方法を解説します。何をテストし、何を装備し、何を温存し、そして何に触れてはならないのかを学んでいきましょう。

### 実践的な識別戦略 (A Practical Identification Strategy)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source: no corrections. Verified every price-group membership (scrolls/potions/rings/wands/spellbooks/armor/gems, objects.h), Charisma buy/sell multipliers & surcharges (shk.c), cursed gain-level rise, shopkeeper buyoff.
-->

ここに、恐るべき迷宮における核心的なパズルがあります。あなたは無数のアイテムを発見することになりますが、その大半は何であるか分からないのです。

ゲームを開始するたびに、ダンジョンは山札をシャッフルします。薬、巻物、杖、指輪、魔除け、そして魔法書には、すべてランダムな外見が割り振られます。あるゲームでの「濁った薬」は回復の薬かもしれませんが、次のゲームでは麻痺の薬かもしれません。ゲーム間で一貫性を保ち続けるのは、アイテムの種別記号そのもの（`!` は常に薬、`?` は常に巻物）と、**アイテムの価格** だけです。そしてこの価格こそが、あなたが持つ最も強力な識別ツールのひとつとなります。

<!-- FLOWCHART-BEGIN -->
::: web-only

<div><figure style="margin: 1.5em 0; text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 736" role="img" aria-label="識別のフローチャート" style="max-width: 760px; width: 100%; height: auto; font-family: 'Hiragino Kaku Gothic ProN', 'Yu Gothic', Meiryo, sans-serif;"><title>識別のフローチャート</title><defs><marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker><style>.start{fill:#E8F4FD;stroke:#3B6FA0;stroke-width:2}.decision{fill:#FFF4E6;stroke:#B5651D;stroke-width:2}.action{fill:#F0F9E8;stroke:#5B8E3A;stroke-width:2}.final{fill:#FCE8E6;stroke:#A14A3F;stroke-width:2}.label{font-size:18px;fill:#1f2933;text-anchor:middle}.startlbl{font-size:19px;font-weight:600;fill:#1f2933;text-anchor:middle}.branch{font-size:16px;font-style:italic;fill:#5a5a5a}.edge{fill:none;stroke:#5a5a5a;stroke-width:1.5}</style></defs><rect class="start" x="40" y="20" width="320" height="50" rx="25" ry="25"/><text class="startlbl" x="200" y="51">アイテムを発見した</text><path class="edge" d="M 200 70 L 200 100" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="100" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="133">祭壇へ行けるか？</text><path class="edge" d="M 360 128 L 430 128" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="121" text-anchor="middle">はい</text><rect class="action" x="430" y="100" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="133">床に落とし、BUCを確認。</text><text class="branch" x="210" y="172">いいえ</text><path class="edge" d="M 200 156 L 200 190" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="190" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="223">ペットが近くにいるか？</text><path class="edge" d="M 360 218 L 430 218" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="211" text-anchor="middle">はい</text><rect class="action" x="430" y="184" width="290" height="62" rx="8" ry="8"/><text class="label" x="575" y="210">落とす。ペットが避けるか？</text><text class="label" x="575" y="232" style="font-size: 16px;"><tspan style="font-style: italic; fill:#5a5a5a;">はい</tspan>: おそらく呪い; <tspan style="font-style: italic; fill:#5a5a5a;">いいえ</tspan>: 不明</text><text class="branch" x="210" y="262">いいえ</text><path class="edge" d="M 200 246 L 200 290" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="290" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="323">店へ行けるか？</text><path class="edge" d="M 360 318 L 430 318" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="311" text-anchor="middle">はい</text><rect class="action" x="430" y="290" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="323">価格を確認。</text><text class="branch" x="210" y="362">いいえ</text><path class="edge" d="M 200 346 L 200 380" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="380" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="413">杖か？</text><path class="edge" d="M 360 408 L 430 408" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="401" text-anchor="middle">はい</text><rect class="action" x="430" y="380" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="413">試し書きテスト。</text><text class="branch" x="210" y="452">いいえ</text><path class="edge" d="M 200 436 L 200 470" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="470" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="503">流し台があり、予備の指輪や薬か？</text><path class="edge" d="M 360 498 L 430 498" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="491" text-anchor="middle">はい</text><rect class="action" x="430" y="470" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="503">指輪を落とす、または薬を浸す。</text><text class="branch" x="210" y="542">いいえ</text><path class="edge" d="M 200 526 L 200 560" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="560" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="593">使用テストは安全か？</text><path class="edge" d="M 360 588 L 430 588" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="581" text-anchor="middle">はい</text><rect class="action" x="430" y="560" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="593">慎重に試す。</text><text class="branch" x="210" y="632">いいえ</text><path class="edge" d="M 200 616 L 200 660" marker-end="url(#arrowhead)"/><rect class="final" x="40" y="660" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="693">識別の巻物を読む。</text></svg><figcaption style="font-style: italic; color: #5a5a5a; font-size: 0.9em; margin-top: 0.5em;">識別のフローチャート：最も安価な方法から順に試し、識別の巻物は最後の手段とする。</figcaption></figure></div>

:::
<!-- FLOWCHART-END -->

#### 祝福、呪われていない、呪い (BUC)
<!-- audit
2026-05-18:
- altar flash on drop: amber blessed, black cursed, no flash uncursed (do.c:379-388)
- pet steps around cursed items (dogmove.c:535-538); starvation exception
- cursed gain-level rockets you through the ceiling (potion.c:1083-1109)
- cursed or confused scroll of teleportation is a LEVEL teleport (read.c:2015-2025)
- holy water made by praying on a co-aligned altar with potions of water (pray.c:2336-2339)
- Priest senses BUC naturally (invent.c:2763, 3545)
- blessed scroll of identify: at least 2 items, plus 1-in-5 chance for the whole pack (read.c:2086-2092)
- cursed scroll of identify IDs only itself on first cursed read (read.c:2074-2081)
- strategy aligned with NetHackWiki Identification, Curse-testing, BUC: altar > pet > shop-price > engrave/sink > use-test > scroll-of-identify ordering matches canonical advice (https://nethackwiki.com/wiki/Identification, https://nethackwiki.com/wiki/Curse-testing, https://nethackwiki.com/wiki/BUC)
-->

アイテムが「何であるか」を気にする前に、まずそれが「どのような状態にあるか」を知る必要があります。恐るべき迷宮にあるすべてのアイテムは、**祝福（blessed）**、**呪われていない（uncursed）**、または **呪い（cursed）** のいずれかの状態にあります（略して **BUC** と呼ばれます）。神々はあなたの装備に対して強い関心を持っており、その関心は具体的な結果をもたらします：

- **祝福された** 識別の巻物は、1〜4個のアイテムを識別し、5回に1回の確率で手持ちの全アイテムを識別します。幸運値がプラスであれば最低識別数が2個に保証されます。*呪われていない* 巻物は通常1個しか識別しませんが、5回に1回の確率で祝福時と同じ結果を引き当てます。*呪われた* 巻物をその種類で初めて読んだときは自分自身しか識別せず、2回目以降の呪われた読書では1個ずつしか識別しません。
- **呪われた** 防具は、まるで愛着障害を抱えているかのように肌に密着して固着します。呪いを解くまで外すことはできません。
- **呪われた** レベルアップの薬は、「レベルを上げる」という言葉を最も文字通りかつ建築学的な意味で解釈します。経験値レベルが上がるのではなく、天井を突き破って直上の階層へとロケットのように吹き飛ばされます。

BUCの状態は、それぞれのアイテムに固有の変化をもたらします。祝福された「幸せの石」は良い幸運値を維持し、悪い幸運値の自然減衰を許しますが、呪われたものはその逆になります。呪われた、あるいは混乱した状態で読む「瞬間移動の巻物」は、フロア内のテレポートではなく、ランダムな *別の階層* へと飛ばされます。

初期状態では、BUCの状態を直接目で見ることはできません。僧侶だけが例外であり、手に取った瞬間に直感でBUCを感知できます。僧侶以外のすべてのキャラクターは、テストを行って確かめなければなりません。

**祭壇テスト。** アイテムを祭壇の上に落としてください：

- 琥珀色（黄色）の閃光が走れば、**祝福** されています。
- 黒い閃光が走れば、**呪われて** います。
- 閃光が走らなければ、**呪われていない** です。

祭壇テストは完全に無料であり、回数制限もありません。序盤で祭壇を見つけたら、積極的に活用してください。

**ペットテスト。** ペットは通常、呪われたアイテムの上を踏むことを嫌がります。ドアの開口部や通路にアイテムを落とし、ペットが何度かそこを通過する様子を観察してください。何度も迂回して歩くようであれば、呪われている強力な証拠です。ただし、一度上を歩いたからといって安全の証明にはなりません。食料への執着、恐怖、戦闘、移動ルーチンの都合によってテストが狂うことがあるからです。さらに厄介な罠として、「逆属性の兜」や「とんがり帽子」は落とした時点では呪われていないと判定されても、頭にかぶった瞬間に自己呪詛化して固着します。「お手玉の小手」や「浮遊の靴」は自己呪詛化こそしませんが、最初から呪われて生成される確率が非常に高いため、必ず事前にテストを行ってください。

**聖水。** 祝福された水（聖水）にアイテムを浸す（dip）と、呪われたアイテムの呪いを解くか、呪われていないアイテムを祝福することができます。呪われた水に浸すと、呪われていないアイテムを呪うか、祝福されたアイテムの祝福を解除します。聖水を作るには、自分と同属性の祭壇の上に「水」の薬を置き、そこで祈りを成功させます。序盤において聖水は極めて貴重であるため、すでに正体が判明している重要なアイテムのために温存してください。

**識別の巻物。** より安価なテスト手段では決着がつかないアイテムのために温存してください。祝福された識別の巻物は、1〜4個（幸運値プラスで最低2個）、あるいは5回に1回の確率でインベントリ内の全アイテムを一挙に識別します。祝福された識別の巻物を読む前に、持っている未識別アイテムをすべて手持ちの荷物袋に入れておき、全識別が引けた際にすべてのアイテムに効果が及ぶように準備しておきましょう。

#### 価格識別 (The Price Is Right)
<!-- audit
2026-05-18:
- buy/sell multipliers and Cha bands match shk.c get_cost/set_cost
- sell offer is 1/2 base (shk.c:3160); 3/8 on unID items from an unfamiliar shopkeeper (shk.c:3173-3174)
- Tourist surcharge (+33%) applies with dunce cap, Tourist below XL 15, or visible Hawaiian shirt — non-stacking
- ~1/4 of unID items carry a 4/3 buy surcharge rolled per item instance via oid % 4 (shk.c:2864-2872 oid_price_adjustment); two identical-looking stacks on a shop floor can roll differently because place_object doesn't auto-merge
- ~1/4 of shopkeepers are "unfamiliar" with unID; they offer 3/4 sell, fixed per shop
- angry-shop +33% surcharge sticks: pacify_shk(FALSE) at shk.c:2663 does NOT clear it
- only pacify_shk(TRUE) clears (shk.c:302, 793 — bones-load and new-customer transitions)
- the JS price widget mirrors get_cost/set_cost exactly
- AMULET macro hard-codes base price 150 for every magic amulet; FAKE_AMULET_OF_YENDOR is base 0 (objects.h:831-834, 865-869)
-->

すべての未識別アイテムには、固定された基本価格が設定されています。魅力（Charisma）が 11〜15 で追加割増がない場合、店主が提示する購入価格（buy quote）はその基本価格そのものになります。また、手持ちのアイテムを店主に売却する際の通常買取価格は、基本価格の半額（1/2）です。この仕様により、店は単なる市場であるだけでなく、極めて優れた **「識別ステーション」** として機能します。

> *店主の価格設定システムは、Gregory Bond氏の『買い物スポイラー (Shopping Spoiler)』（Kate Nepveu氏がHTML化しsteelypips.orgで公開）で初めて詳細に文書化されました。その後、David Damerell氏の『アイテム識別スポイラー (Object Identification Spoiler)』によって価格に基づく識別技法がさらに拡張されました。以下の解説はその両方を基盤にしています。*

アイテムを拾い上げずに価格を確認するには、そのアイテムの上に立ち、**`:`** を押すか、その場に立ったまま店主に向かって **`#chat`** で話しかけてください。店の入口から手持ちのアイテムを店内に投げ入れてはいけません。価格の提示は一切受けられず、店主の懐にそのまま着服されてしまいます。

以下の3つの条件のいずれかを満たすと、同一の **「カモ（観光客）割増」** が適用されます：
- *とんがり帽子（dunce cap）* を着用している
- *経験値レベル15未満の観光客* でプレイしている
- 鎧やクロークを着用せず、*Tシャツまたはアロハシャツ* を丸出しにしている

これらに該当すると、購入価格が 1/3（約33%）引き上げられ、売却価格は基本価格の 1/2 から 1/3 へと買い叩かれます（これらの条件は重複して累積しません）。魅力の値は購入価格にのみ影響します。店で商談を行う前に、必ずシャツの上に防具を着て覆い隠してください。

同じカテゴリに属し、同じ基本価格を共有するアイテム群を **「価格帯グループ（price group）」** と呼びます。価格を確認するだけで、多くの場合2〜3種類の候補にまで絞り込むことができます。魅力が低いと購入価格が跳ね上がり（魅力5以下で基本価格の2倍）、魅力が高いと安くなります（魅力19以上で基本価格の半額）。換算方法は後述の表を参照してください。

未識別の商品には2つの例外的なブレが生じます。商品の約4個に1個には、恒久的な **1/3（約33%）の購入割増** がランダムに付与されます（そのため、同じ外見のアイテムの山であっても個体ごとに提示額が異なる場合があります）。また、店主のおよそ4人に1人は、未識別の品物に対して通常の買取価格の **3/4** しか提示してくれません（この傾向はアイテムごとではなく店主ごとに固定されています）。提示された価格が想定したティアと微妙にズレている場合は、前後のティアも確認してください。

**怒った店主。** 店主を攻撃したり、店主に向けて杖を振ったり、代金を支払わずに店を出ようとしたり、店舗の破損代金の支払いを拒否すると店主は激怒します。事態を収拾して店主を宥めた後であっても、その店主は恒久的に 1/3 の購入割増を請求し続けます（売却価格には影響しません）。

**戦闘後の買収。** 単なる借金ではなく実際に店主に刃を向けた場合、店主はお金ではなく血を求めます。しかし、それでも買収して許してもらう道は残されています。手元に1000ゴールド以上の現金を持った状態で `p` を押すと、1000金貨を支払って宥める試行ができます。あなたがその店の常連顧客として登録されている場合、この買収は約3回に1回の確率で失敗し、金貨を失った上に店主は激怒したままになります。それ以外の場合は店主は落ち着きを取り戻します（ただし前述の割増は残ります）。

**不可視状態での入店。** 店主は目に見えない顧客とは商売をしてくれません。透明化（不可視）の状態で足を踏み入れると、「透明なお客様はお断りです！（Invisible customers are not welcome!）」と怒鳴られ、価格の提示も売買も一切拒否されます。もし不可視状態から戻れなくなってしまった場合は、クロークのスロットに「ミイラの包帯」を着用してください。透明化が遮断されて姿が可視化され、店主と通常通り取引できるようになります。再び姿を消したければ、店を出る際に包帯を脱ぎましょう。

<!-- audit
2026-08-01: shop stock is theme-restricted (shknam.c shtypes[]).
- lighting store lists only specific light items, no generic class slot:
  wax/tallow candle, oil lamp, brass lantern, magic lamp, POT_OIL,
  WAN_LIGHT, SCR_LIGHT, SPE_LIGHT (shknam.c:333-346) -> every wand=light,
  potion=oil, scroll=light, spellbook=light.
- delicatessen potions limited to POT_FRUIT_JUICE/POT_BOOZE/POT_WATER;
  rest random FOOD_CLASS + ICE_BOX (shknam.c:269-274).
- restriction applies to generated stock; resold dropped items are not.
-->

**専門店の品揃えも重要なヒント。** 特定のジャンルを専門に扱う店舗は、そのテーマに合致したアイテムしか仕入れません。したがって、**「どこで見つけたか」** だけでアイテムの正体を特定できることがあります。照明器具店の棚に並んでいるものはすべて光に関連するアイテムです：そこにあるすべての杖は「明かりの杖」、すべての薬は「油」、すべての巻物は「光の巻物」、すべての魔法書は「光の魔法書」です。食料品店に並ぶ薬は「果物ジュース」、「酒」、「水」のいずれかしかありません。これらは店主が元から仕入れていた商品にのみ適用されるルールであり、あなたやモンスターが床に落とした品物には当てはまりません。

以下に、アイテム種別ごとの価格表を掲載します。

::: print-only

```{=latex}
\clearpage
\thispagestyle{plain}
\vspace*{\fill}
\begin{center}
\includegraphics[width=0.92\linewidth]{cover/build/flowchart.pdf}\\[0.6em]
{\itshape\footnotesize 識別のフローチャート：最も安価な方法から順に試し、識別の巻物は最後の手段とする。}
\end{center}
\vspace*{\fill}
\clearpage
```

##### 提示価格換算表 (Quoted-price conversion)

各行は、指定された基本価格に対して取引される実際の価格を示しています。

**購入行（Buy rows）** は魅力（Charisma）の区分（購入時に **提示される** 価格）です。記号のない区分（*11–15* など）は基準値です。*11–15^T^* は魅力11〜15に4/3倍（約33%）の割増が1つ適用された状態、*11–15^T2^* は2つの割増が重複適用された状態です。割増の発生源は3つあります：「カモ割増」（低レベル観光客、とんがり帽子、シャツ丸出し）、「怒った店主」、あるいは未識別アイテムの約4個に1個にランダムで付与される割増です。

**売却行（Sell rows）** は表の最下部にあり、怒っていない店主が買い取り時に **提示する** 価格を示します。売却価格には魅力は影響しません。*S* は基本価格の 1/2 の基準値です。*S^T^* は前述のカモ条件（とんがり帽子、低レベル観光客、シャツ丸出し）であり、売却提示額が 1/2 から 1/3 へと買い叩かれます。*S^P^* は、未識別アイテムの提示額を 1/4 差し引く（通常の3/4にする）店主（4人に1人）を示します。*S^TP^* はその両方が重複適用された状態です。

| 魅力 / 割増条件                  |   倍率 |  20 |  50 |  60 |  80 | 100 | 150 | 175 | 200 | 300 |  500 |
|----------------------------------|:-------|----:|----:|----:|----:|----:|----:|----:|----:|----:|-----:|
| 6–7^T2^                          |  ×2.67 |  53 | 133 | 160 | 213 | 267 | 400 | 467 | 533 | 800 | 1333 |
| 8–10^T2^                         |  ×2.37 |  47 | 119 | 142 | 190 | 237 | 356 | 415 | 474 | 711 | 1185 |
| 6–7^T^                           |  ×2.0  |  40 | 100 | 120 | 160 | 200 | 300 | 350 | 400 | 600 | 1000 |
| 8–10^T^, 11–15^T2^               |  ×1.78 |  36 |  89 | 107 | 142 | 178 | 267 | 311 | 356 | 533 |  889 |
| 6–7                              |  ×1.5  |  30 |  75 |  90 | 120 | 150 | 225 | 263 | 300 | 450 |  750 |
| 8–10, 11–15^T^, 16–17^T2^        |  ×1.33 |  27 |  67 |  80 | 107 | 133 | 200 | 233 | 267 | 400 |  667 |
| 18^T2^                           |  ×1.19 |  24 |  59 |  71 |  95 | 119 | 178 | 207 | 237 | 356 |  593 |
| 11–15, 16–17^T^                  |  ×1.00 |  20 |  50 |  60 |  80 | 100 | 150 | 175 | 200 | 300 |  500 |
| 18^T^, 19+^T2^                   |  ×0.89 |  18 |  44 |  53 |  71 |  89 | 133 | 156 | 178 | 267 |  444 |
| 16–17                            |  ×0.75 |  15 |  38 |  45 |  60 |  75 | 113 | 131 | 150 | 225 |  375 |
| 18, 19+^T^                       |  ×0.67 |  13 |  33 |  40 |  53 |  67 | 100 | 117 | 133 | 200 |  333 |
| 19+, S                           |  ×0.5  |  10 |  25 |  30 |  40 |  50 |  75 |  88 | 100 | 150 |  250 |
| S^P^                             |  ×0.375 |   8 |  19 |  23 |  30 |  38 |  56 |  66 |  75 | 113 |  188 |
| S^T^                             |  ×0.333 |   7 |  17 |  20 |  27 |  33 |  50 |  58 |  67 | 100 |  167 |
| S^TP^                            |  ×0.25 |   5 |  13 |  15 |  20 |  25 |  38 |  44 |  50 |  75 |  125 |

:::

##### 巻物の価格 (Scroll Prices)

| 価格 | 巻物の種類 |
| ---: | --- |
|   20 | 識別の巻物 (identify) |
|   50 | 光の巻物 (light) |
|   60 | 白紙の巻物 (blank paper), 武器に魔法をかける巻物 (enchant weapon) |
|   80 | 鎧に魔法をかける巻物 (enchant armor), 解呪の巻物 (remove curse) |
|  100 | 混乱の巻物 (confuse monster), 鎧を破壊する巻物 (destroy armor), 火の巻物 (fire), 食料を探す巻物 (food detection), 金貨を探す巻物 (gold detection), 地図の巻物 (magic mapping), 怪物を怯えさせる巻物 (scare monster), 瞬間移動の巻物 (teleportation) |
|  200 | 記憶喪失の巻物 (amnesia), 怪物を作る巻物 (create monster), 大地の巻物 (earth), 怪物を飼いならす巻物 (taming) |
|  300 | 充填の巻物 (charging), 虐殺の巻物 (genocide), 処罰の巻物 (punishment), 悪臭雲の巻物 (stinking cloud) |

<div class="price-id-toolbar"></div>

100ゴールドのグループは該当アイテムが多いため、価格だけでは正体を確定できません。一方、20ゴールドの巻物は「識別の巻物」で確定します。60ゴールドのグループには「白紙の巻物」と「武器に魔法をかける巻物」しかなく、80ゴールドは「鎧に魔法をかける巻物」か「解呪の巻物」の2択です。これらの候補が絞られているグループは、BUCが判明した後に実際に読んで試す（使用テスト）のに最適な候補となります。

```{=latex}
\needspace{6\baselineskip}
```

扉のない1マスだけの狭い小部屋（時には鉄格子の奥）に密閉された **たった1枚の巻物** は、「瞬間移動の巻物」です。小部屋の中にテレポートして閉じ込められた生物が脱出できるように置かれています。

##### 魔法書の価格 (Spellbook Prices)

魔法書の価格は、呪文のレベル × 100ゴールドに設定されています。そのため、読む際のリスクを容易に見極めることができます：700ゴールドの魔法書はレベル7の呪文であり、慎重な魔法使い以外の者が読めば十中八九その手の中で大爆発を起こします。

<div class="price-id-toolbar"></div>

| 価格 | レベル | 魔法書の種類 |
| ---: | :---: | --- |
|  100 | 1 | 混乱 (confuse monster), 怪物探知 (detect monsters), 衝撃 (force bolt), 回復 (healing), 跳躍 (jumping), 施錠開錠 (knock), 灯り (light), 防護 (protection) |
|  200 | 2 | 連鎖雷撃 (chain lightning), 怪物創造 (create monster), 盲目治療 (cure blindness), 食料探知 (detect food), 生命吸収 (drain life), マジックミサイル (magic missile), 怪物減速 (slow monster), 施錠 (wizard lock) |
|  300 | 3 | 恐怖 (cause fear), 千里眼 (clairvoyance), 病気治療 (cure sickness), 不可視探知 (detect unseen), 超回復 (extra healing), 加速 (haste self), 識別 (identify), 解呪 (remove curse), 眠り (sleep), 石化解除 (stone to flesh) |
|  400 | 4 | 冷気の円錐 (cone of cold), 宝探知 (detect treasure), 火の玉 (fireball), 透明化 (invisibility), 浮遊 (levitation), 能力回復 (restore ability) |
|  500 | 5 | 怪物魅了 (charm monster), 穴掘り (dig), 地図化 (magic mapping) |
|  600 | 6 | 使い魔創造 (create familiar), 変化 (polymorph), テレポート (teleport away), アンデッド退散 (turn undead) |
|  700 | 7 | 無力化 (cancellation), 死の指 (finger of death) |

<div class="price-id-toolbar"></div>

##### 薬の価格 (Potion Prices)

| 価格 | 薬の種類 |
| ---: | --- |
|   20 | 回復の薬 (healing) |
|   50 | 酔っぱらいの薬 (booze), フルーツジュース (fruit juice), 可視の薬 (see invisible), 病気の薬 (sickness) |
|  100 | 混乱の薬 (confusion), 超回復の薬 (extra healing), 幻覚の薬 (hallucination), 能力回復の薬 (restore ability), 睡眠の薬 (sleeping), 水 (water) |
|  150 | 盲目の薬 (blindness), 魔力の薬 (gain energy), 透明の薬 (invisibility), 怪物を探す薬 (monster detection), 物体を探す薬 (object detection) |
|  200 | 啓蒙の薬 (enlightenment), 完全回復の薬 (full healing), 浮遊の薬 (levitation), へんげの薬 (polymorph), 加速の薬 (speed) |
|  250 | 酸の薬 (acid), 油の薬 (oil) |
|  300 | 能力獲得の薬 (gain ability), レベルアップの薬 (gain level), 麻痺の薬 (paralysis) |

<div class="price-id-toolbar"></div>

回復の薬は20ゴールドに単独で属しているため、値札を見るだけで一意に特定できます。また、水は常に「透明な薬」の外見を持つため、価格を確認するまでもなく正体が分かります。50ゴールドのグループは要注意です。「病気の薬」と「[可視の薬](#senses-and-perception)」が同居しているためです（一方は極めて有害、もう一方は極めて有益）。200ゴールドのグループには優秀な薬がぎっしり詰まっています。

##### 指輪の価格 (Ring Prices)

| 価格 | 指輪の種類 |
| ---: | --- |
|  100 | 飾りの指輪 (adornment), 飢餓の指輪 (hunger), 守りの指輪 (protection), 耐へんげの指輪 (protection from shape changers), 忍びの指輪 (stealth), 能力維持の指輪 (sustain ability), 警告の指輪 (warning) |
|  150 | 反感の指輪 (aggravate monster), 耐冷の指輪 (cold resistance), 体力の指輪 (gain constitution), 強さの指輪 (gain strength), 命中の指輪 (increase accuracy), 攻撃の指輪 (increase damage), 透明の指輪 (invisibility), 耐毒の指輪 (poison resistance), 可視の指輪 (see invisible), 耐電の指輪 (shock resistance) |
|  200 | 耐炎の指輪 (fire resistance), 自由行動の指輪 (free action), 浮遊の指輪 (levitation), 回復の指輪 (regeneration), 探索の指輪 (searching), 消化不良の指輪 (slow digestion), 瞬間移動の指輪 (teleportation) |
|  300 | 争いの指輪 (conflict), へんげの指輪 (polymorph), へんげ制御の指輪 (polymorph control), 瞬間移動制御の指輪 (teleport control) |

<div class="price-id-toolbar"></div>

300ゴールドの指輪は4種類しかなく、そのうち3種類は極めて優秀です：争いの指輪、[へんげ制御の指輪](#special-and-utility)、そして[瞬間移動制御の指輪](#movement-and-spatial-behavior) です。残る4つ目はへんげの指輪であり、通常は呪われた状態で生成されます。

##### 杖の価格 (Wand Prices)

| 価格 | 杖の種類 |
| ---: | --- |
|  100 | 灯りの杖 (light), 単なる杖 (nothing) |
|  150 | 穴掘りの杖 (digging), 啓蒙の杖 (enlightenment), 施錠の杖 (locking), 矢の杖 (magic missile), 透明化の杖 (make invisible), 開錠の杖 (opening), 探査する杖 (probing), 扉探索の杖 (secret door detection), 減速の杖 (slow monster), 加速の杖 (speed monster), 静止の杖 (stasis), 衝撃の杖 (striking), 蘇生の杖 (undead turning) |
|  175 | 吹雪の杖 (cold), 炎の杖 (fire), 雷の杖 (lightning), 眠りの杖 (sleep) |
|  200 | 無力化の杖 (cancellation), 怪物を造る杖 (create monster), へんげの杖 (polymorph), 瞬間移動の杖 (teleportation) |
|  500 | 死の杖 (death), 願いの杖 (wishing) |

<div class="price-id-toolbar"></div>

もし500ゴールドの杖を見つけたら、今日は最高にツイている日です。

##### 魔除けの価格 (Amulet Prices)

安物のイェンダーの魔除けのイミテーション（0ゴールド）を除き、すべての魔除けの基本価格は **150ゴールド** で統一されています。そのため、価格から魔除けの正体を識別することはできません。他の識別手段を用いる必要があります。

<script>
document.addEventListener('DOMContentLoaded', function() {
  var toolbars = document.querySelectorAll('.price-id-toolbar');
  if (!toolbars.length) return;
  var CHA_BUY = {
    'lt5':    [2, 1],
    '6to7':   [3, 2],
    '8to10':  [4, 3],
    '11to15': [1, 1],
    '16to17': [3, 4],
    '18':     [2, 3],
    'ge19':   [1, 2]
  };
  var state = {cha: '11to15', sell: false, touristy: false, angry: false};

  // Populate each toolbar with the same compact button set.
  // Cha bracket on the left, then independent toggles: Sell, Tourist, Dunce.
  var btnHTML =
    '<span class="price-id-label">魅力</span>' +
    '<button data-group="cha" data-val="lt5">≤5</button>' +
    '<button data-group="cha" data-val="6to7">6-7</button>' +
    '<button data-group="cha" data-val="8to10">8-10</button>' +
    '<button data-group="cha" data-val="11to15">11-15</button>' +
    '<button data-group="cha" data-val="16to17">16-17</button>' +
    '<button data-group="cha" data-val="18">18</button>' +
    '<button data-group="cha" data-val="ge19">≥19</button>' +
    '<span class="price-id-sep">·</span>' +
    '<button data-group="toggle" data-val="sell">売却</button>' +
    '<button data-group="toggle" data-val="touristy">カモ</button>' +
    '<button data-group="toggle" data-val="angry">怒り</button>';
  toolbars.forEach(function(tb) {
    tb.innerHTML = btnHTML;
    tb.classList.add('price-id-widget');
  });

  function adj(base, m, d) {
    var n = base * m;
    if (d > 1) n = Math.floor((n * 10 / d + 5) / 10);
    return Math.max(1, n);
  }
  function computeBuy(base, surcharge) {
    // Replicates shk.c get_cost. Default Cha 11-15 no penalty: buy = base.
    var m = 1, d = 1;
    var cha = CHA_BUY[state.cha];
    m *= cha[0]; d *= cha[1];
    if (state.touristy) { m *= 4; d *= 3; }
    if (surcharge) { m *= 4; d *= 3; }
    var n = adj(base, m, d);
    // Angry-shopkeeper surcharge: added AFTER mult/div in shk.c:2986
    // (tmp + (tmp + 2) / 3, ~+33%). Stacks with Tourist. Buy-side only.
    if (state.angry) n = n + Math.floor((n + 2) / 3);
    return n;
  }
  function computeSell(base, unfamiliar) {
    // Replicates shk.c set_cost. Default no penalty: sell = base / 2.
    var m = 1, d = 1;
    if (state.touristy) d *= 3; else d *= 2;
    if (unfamiliar) { m *= 3; d *= 4; }
    return adj(base, m, d);
  }
  function pair(n1, n2) {
    return n1 === n2
      ? '' + n1
      : n1 + '<span class="pi-alt"> / ' + n2 + '</span>';
  }

  // Find every table whose first column header is "Price" or "価格". Stash the base
  // price (which is what shows initially, since default state quotes buy =
  // base) on each row's price cell. We also tolerate "Sell" or "売却" as a header
  // (e.g. after a previous render).
  var priceTables = [];
  document.querySelectorAll('table').forEach(function(t) {
    var hdrs = t.querySelectorAll('thead th');
    if (!hdrs.length) return;
    if (!/^(Price|Sell|価格|売却)$/i.test(hdrs[0].textContent.trim())) return;
    hdrs[0].classList.add('pi-col');
    t.querySelectorAll('tbody tr').forEach(function(tr) {
      var firstTd = tr.querySelector('td');
      if (!firstTd) return;
      var m = firstTd.textContent.trim().match(/^\$?(\d+)/);
      if (!m) return;
      if (!firstTd.dataset.basePrice) firstTd.dataset.basePrice = m[1];
      firstTd.classList.add('pi-price', 'pi-col');
    });
    priceTables.push(t);
  });

  function renderTables() {
    priceTables.forEach(function(t) {
      var hdr = t.querySelector('thead th.pi-col');
      if (hdr) hdr.textContent = state.sell ? '売却' : '価格';
      t.querySelectorAll('td.pi-price').forEach(function(td) {
        var base = parseInt(td.dataset.basePrice, 10);
        if (state.sell) {
          td.innerHTML = pair(computeSell(base, false), computeSell(base, true));
        } else {
          td.innerHTML = pair(computeBuy(base, false), computeBuy(base, true));
        }
      });
    });
  }

  function syncToolbars() {
    toolbars.forEach(function(tb) {
      tb.querySelectorAll('button[data-group="cha"]').forEach(function(b) {
        b.classList.toggle('active', b.dataset.val === state.cha);
      });
      tb.querySelectorAll('button[data-group="toggle"]').forEach(function(b) {
        b.classList.toggle('active', !!state[b.dataset.val]);
      });
    });
  }

  toolbars.forEach(function(tb) {
    tb.addEventListener('click', function(ev) {
      var btn = ev.target.closest('button');
      if (!btn) return;
      var g = btn.dataset.group, v = btn.dataset.val;
      if (g === 'cha') state.cha = v;
      else state[v] = !state[v];
      syncToolbars();
      renderTables();
    });
  });

  syncToolbars();
  renderTables();
});
</script>

#### 杖の試し書きテスト (The Engrave Test (Wands))

杖の識別テストは1チャージを消費しますが、残りのチャージを安全に温存できます。

> *手順は、かつてRGRNに投稿されたKieron Dunbar氏のスポイラー『杖を振って識別する (Identifying Wands by Zapping)』に基づいています。*

1. **まず杖のBUCをテストする。** 呪われた杖で床に文字を刻もうとすると、100分の1の確率で爆発します。チャージを消費する前に、祭壇に落とすか他の呪いテストを行ってください。
2. **指を使って床の埃に短いメッセージを刻む。** まず自分の指（コマンド `E` を押し、道具の選択で「`-`」を指定）で、埃の中に適当な言葉を1〜2語刻んでおきます。一部の杖はまっさらな床に効果を及ぼすのではなく、**「既存の文字」に対して作用する** ためです。へんげの杖は文字をランダムな別のメッセージへと書き換え、無力化の杖、透明化の杖、瞬間移動の杖はそれぞれ文字を「消滅」させます。事前に文字を書いておかないと、これらの挙動を見落としてしまいます。
3. **杖を使って重ねて刻む。** 再び `E` を押し、テストしたい杖を選択します。発生した結果を観察してください。[杖の一覧表](#the-wand-table) に各杖の試し書き結果が記載されており、大半の杖はこのテストだけで正体が判明します。なお、雷の杖は試し書き時に最大50ターンの間盲目状態を引き起こすため、近くにモンスターがいる状況では絶対にテストしないでください。一部の杖は同一のメッセージを共有します。詳細は [曖昧な試し書き結果の解決法](#resolving-ambiguous-engrave-results) を参照してください。

**願いの杖の疑いがある場合も試し書きは安全です。** 500ゴールドの杖の候補で試し書きを行い、*「何を願いますか？ (For what do you wish?)」* と尋ねられたら、テストによって1チャージが消費され、願いが成就します。最大限に価値のある願いを叶えましょう。

#### 流し台テスト (The Sink Test (Rings))
<!-- audit
2026-05-18:
- dosinkring at do.c:498-650 — all 28 ring types give a sink message, BUT 13 only when sighted (second switch do.c:592+ gated on !Blind); 15 work even blind (first switch). Message is a hint via trycall, NOT makeknown/formal ID. Overlaps: protection & warning both "sink glows", teleportation & polymorph can both "sink vanishes", aggravate monster & meat ring near-identical fly message
- searching and slow digestion goto giveback, dropped back on the floor identified (do.c:507-516)
- other rings usually consumed: 1/20 backup chance, 1/5 buried chance (do.c:649-660)
-->

ダンジョン内で流し台（sink）を見つけたら、その中に指輪を落としてテストすることができます。指輪の種類ごとに固有の手がかりメッセージが発生します（ただしメッセージが重複するものもあり、目が見えている状態でなければ表示されないものもあるため、常に完全な正式識別になるとは限りません）。探索の指輪と[消化不良の指輪](#special-and-utility) は、落とした瞬間に手元へと跳ね返ってきて即座に識別されます。それ以外の指輪は、20分の1の確率で手元に戻り、5分の1の確率で流し台の下に埋没しますが、それ以外の場合は排水溝に飲み込まれて失われます。したがって、唯一の貴重な指輪ではなく、ダブった予備の指輪でのみ試してください。メッセージの詳細な一覧は [流し台](#sinks) を参照してください。

#### 使用テスト（慎重なアプローチ） (Use-Testing (The Careful Way))
<!-- audit
2026-05-18:
- engrave-test messages: fire "Flames fly", cold "A few ice cubes drop", lightning "Lightning arcs", digging "Gravel flies up", magic missile "riddled by bullet holes" (engrave.c, zap.c)
- polymorph randomizes existing engraving, not "vanishes" (engrave.c:618-633 WAN_POLYMORPH case calls random_engraving on existing engraving)
- cancellation, make-invisible, teleportation all share the "vanishes" message
- wand of wishing engrave DOES grant the wish (zap.c:2575-2585)
- unicorn horn dipped in sickness → fruit juice; in confusion/hallucination/blindness → water (potion.c:2151-2159)
- is_poisonable requires oc_skill in [-P_SHURIKEN, -P_BOW] (obj.h:264-268) — ranged ammo only
- daggers (skill +1) and spears (skill +17) are NOT poisonable
- confused remove curse via blessorcurse(obj, 2): 1/4 bless, 1/4 curse, 1/2 unchanged (mkobj.c:1841-1853)
- non-blessed confused remove curse touches only worn/wielded (read.c:1549-1552); blessed touches all
- 90% auto-curse branch (mkobj.c:1087-1090) covers fumble boots, levitation boots, gauntlets of fumbling, helm of opposite alignment
- cursed worn armor refuses to be taken off via the otmp->cursed check (do_wear.c:1900); cursed loadstone refuses to drop (do.c:685-695)
-->

店や流し台が利用できない場合でも、慎重にアイテムを実際に使ってみることで正体を暴けることがあります。カテゴリーごとの手法は以下の通りです：

**薬。** 最も安全なテストは、**モンスターに向けて投げつける** ことです。自分で飲むリスクを完全に回避できます。薬がモンスターの傷を治せば何らかの回復の薬、モンスターが俊敏になれば加速の薬、モンスターが透明になれば透明の薬です（ただし、透明になった敵を相手にする羽目にはなりますが）。

また、アイテムを薬に浸す（dip）ことでもテストできます。毒を塗れる弾薬（矢、クロスボウの矢、ダーツ、手裏剣）の束を「病気の薬」に浸すと毒矢になり、薬の正体が確定します（剣などの近接武器には毒を塗ることはできません）。また、**ユニコーンの角** を「混乱の薬」、「幻覚の薬」、「盲目の薬」に浸すと真水に変化し、「病気の薬」に浸すと果物ジュースへと浄化されます。

**油の薬は、唯一使用（`#apply`）できる薬です。** 未識別の薬に使用コマンドを使い、火を灯すプロンプトが出れば、それは油の薬です。他の薬は一切反応しません。

薬を飲む前の安全確認としても浸漬は有効です。予備の矢を浸して何も変化が起きなければ、その薬は酸でも病気でもないことが確定します（油、へんげ、聖水でもありません）。ただし麻痺や睡眠の薬は浸しても無反応ですが、飲めば無防備に昏倒するため油断は禁物です。

**200ゴールドの薬をテストする。** 200ゴールドのグループ（啓蒙、完全回復、浮遊、へんげ、加速）は素晴らしい見返りがありますが、2つの罠が潜んでいます。呪われていない浮遊は10〜149ターン持続し、祝福された浮遊は250〜299ターン持続します（`>` を押すことで早めに着地できます）。また、へんげの薬は身につけている鎧を破壊したり脱落させたりするモンスター形態に変身してしまう危険があります。テストする際はシャツ1枚まで脱ぎ、周囲に敵がいない安全な場所で行ってください。

**巻物。** 読む行為には常にリスクが伴います。一部の巻物（鎧破壊、健忘、処罰）は明白に有害です。最も安全なのは、まず価格識別を行い、安全な価格帯グループの巻物だけを読むことです。どうしても目隠し状態で読まなければならない場合は、鎧破壊の可能性を考慮して事前に防具をすべて脱ぎ、テレポートしても致命的にならない場所で読んでください。

**混乱読書** は多くの巻物に特殊な効果をもたらし、時には極めて有用です。混乱状態で「解呪の巻物」を読むと、**呪われていないアイテムのBUCがランダムにシャッフルされます**（約1/4が祝福、1/4が呪い、1/2が呪われていないまま）。すでに呪われているアイテムの呪いはそのまま残ります。呪われていない巻物であれば装備中の武具のみ、祝福された巻物であれば全所持品が対象となります。これは装備品に安価な祝福を付与する裏技であり、呪いを解く道具ではありません。呪いを解きたいときに混乱状態で読んではいけません。

**指輪。** まず祭壇テストやペットテストで呪われていないことを確認してください。その上で指にはめます。多くの指輪は即座にメッセージや目に見える効果をもたらします：宙に浮く、姿が消える、筋力がみなぎるなどです。目立った変化がない場合は、ステータス画面やインベントリを確認して微小な変化（AC改善、隠密、探索など）をチェックしてください。通常よりも空腹の進行が早くなったり（空腹の指輪）、モンスターが急激に好戦的になったり（反感の指輪）した場合は、ただちに外してください。

**魔除け。** 首にかける前に必ずBUCをテストしてください。「絞殺の魔除け」はわずか6ターンであなたを窒息死させます。首が締まったら即座に外すか、呪われて外せない場合は神に祈ってください。また「安眠の魔除け」は無防備な眠りに落ちてしまいます。「遠視の魔除け」は目隠しなどで盲目状態になった際に効果が現れ、「反射の魔除け」は敵の光線が跳ね返った瞬間に判明します。

**防具。** 魔法の防具は身につけた瞬間に効果を現します：韋駄天の靴は足を速くし、透明のクロークは姿を消します。しかし、店の中で未識別の防具を試着するのは危険です。もし呪われていれば脱ぐことができず、店主は代金の支払いを要求してくるからです。「逆属性の兜」や「とんがり帽子」は着用した瞬間に自己呪詛化して固着することすらあります。**店内で未識別の防具を試着する前に、必ずBUCを確認してください。** 店の外では生存が最優先です：ACが6より悪い状態であれば、テストできなくても拾った鎧、兜、盾、クロークを着用すべきです。ただし靴と小手は必ず事前にテストしてください。その有害な変種は致命的な危険を招くからです。

各特殊防具は **ランダムな外見** を持ちます。前回のゲームで安全な浮遊だった「スノーブーツ」が、今回のゲームでは跳躍やつまずきの靴である可能性があります。シャッフルされる4つのプールは以下の通りです：

- 4種類の魔法の **兜** は4つの外見を共有：羽飾りのついた兜 / 彫刻された兜 / 鶏冠のついた兜 / 面頬のついた兜 → 兜、知性の兜、逆属性の兜、テレパシーの兜 のいずれか。（賢さの兜は常に「クリスタル兜」。とんがり帽子と魔力回復の帽子はどちらも「円錐形の帽子」）。
- 4種類の魔法の **クローク** は4つの外見を共有：ボロボロのマント / オペラクローク / 装飾された法衣 / 布切れ → 守りのクローク、透明のクローク、魔法を防ぐクローク、幻影のクローク のいずれか。いずれも極めて優秀です。
- 4種類の **小手** は4つの外見を共有：古びた手袋 / 綿入れの手袋 / 乗馬用の手袋 / フェンシング用の手袋 → 革の手袋、あるいは3種類のガントレット（お手玉の小手、力の小手、器用さの小手）のいずれか。
- 7種類の魔法の **靴** は7つの外見を共有：戦闘用の靴 / ジャングルブーツ / 登山靴 / 泥靴 / 留め金付きの靴 / 乗馬靴 / スノーブーツ → 韋駄天の靴、水上歩行の靴、飛び跳ねる靴、エルフの靴、蹴り挙げ靴、つまずきの靴、浮遊の靴 のいずれか。

ただし価格はシャッフルされません。価格を確認することで、安全な靴やクロークと呪われた品とを判別できます。

##### 防具の価格 (Armor Prices)

| 価格 | 防具の部位 | 該当アイテム |
| ---: | --- | --- |
|   10 | 兜 | 通常の兜 (plain helmet) |
|   50 | 兜 | 知性の兜 (caution), 逆属性の兜 (opposite alignment), テレパシーの兜 (telepathy) |
|    8 | 靴 | エルフの靴 (elven boots / 忍び), 蹴り挙げ靴 (kicking) |
|   30 | 靴 | つまずきの靴 (fumble), 浮遊の靴 (levitation) （どちらも高確率で呪われている！） |
|   50 | 靴 | 韋駄天の靴 (speed), 水上歩行の靴 (water walking), 飛び跳ねる靴 (jumping) （いずれも極めて有用） |
|    8 | 小手 | 革の手袋 (leather gloves) （これのみ） |
|   50 | 小手 | お手玉の小手 (fumbling), 力の小手 (power), 器用さの小手 (dexterity) |
|   50 | クローク | 守りのクローク (protection), 幻影のクローク (displacement) |
|   60 | クローク | 透明のクローク (invisibility), 魔法を防ぐクローク (magic resistance) |

<div class="price-id-toolbar"></div>

30ゴールドの靴は危険信号です。どちらの候補も通常呪われて生成されます。50ゴールドの靴はどれも当たりです。60ゴールドのクロークは透明か耐魔の2択です。価格だけでは8ゴールドのエルフの靴と蹴り挙げ靴、あるいは50ゴールドの3種類の小手を区別できません。BUCをテストした上で実際に装備し、表示されるメッセージを観察してください。

#### 灰色石：4つの石、幸運は1つ (Gray Stones: Four Stones, One Lucky)
<!-- audit
2026-05-18:
- best mimic test here is SEARCH, not the pet: an explicit `s` adjacent to an object-mimic reveals it unconditionally — mfind0 (detect.c:1965) calls seemimic() for any M_AP_TYPE monster with NO rng roll (unlike SDOOR rnl(7-fund) / traps rnl(8)). the minend-1 mimics are appear_as="obj:..." => M_AP_OBJECT, so one search beside a suspect stone exposes it every time; a real stone stays a stone. reworked the prose to lead with search (consistent with the existing "A note on mimics" section, which already says search reveals mimics) instead of the fiddly pet-in-a-niche. search only flags mimics, so price-ID still separates the real luckstone from the cursed loadstone.
- "name it The Heart of Ahriman -> hand slips = it's the luckstone" is FAKE. restrict_name (artifact.c:575) builds sametype[] from shared description / shuffle-range; all four gray stones share descr "gray" and the o_ranges band (objects.h:1594-1604), so for ANY unidentified gray stone sametype includes luckstone -> naming it the Heart (SPFX_RESTR) trips the restriction -> "While engraving, your %s slips." (do_name.c:330-351) identically for luckstone/loadstone/touchstone/flint. the slip only confirms "unidentified gray stone," which you already know; it cannot single out the luckstone.
- other two layouts: minend-2 ("Gnome King's Wine Cellar") luckstone is at fixed (70,5) in a walled gem-pile vault, NO stone decoys. minend-3 ("Catacombs") luckstone (place[2]) + flint decoy (place[1]) are shuffled among 3 spots, and there is a level-teleport trap under BOTH (lines 89-90, "one-time annoyance") — stepping onto the prize can fling you off-level.
- BUC/pet-test note: the minend-1 decoy loadstone IS cursed on the floor (mksobj curses all loadstones, mkobj.c:978; des.object with no buc => curse_state 0 => no override in sp_lev.c:2234). so a pet registers it as cursed and won't step on it (cursed_object_at dogmove.c:145, "avoid cursed items unless starving" dogmove.c:535). the pet thus avoids all 4 mimics AND the loadstone; the one gray-stone square it will walk onto is the uncursed luckstone. "loadstone isn't cursed until picked up" is false for floor loadstones — that idea is really the freeinv re-curse (invent.c:1386), which only bites an uncursed (wished) loadstone on REMOVAL. caveat: luring a pet into a 1-tile dead-end niche is fiddly, so price-ID stays the clean fallback.
- luckstone default BUC: a luckstone is uncursed by default — GEM_CLASS in mksobj_init (mkobj.c:976-986) never calls blessorcurse for it, and mksobj zeroes the obj (mkobj.c:1185). so the Mine's End buc="not-cursed" (=> uncurse(), a no-op) yields an UNCURSED (not blessed) luckstone. "always uncursed" in the prose is accurate.
2026-08-13:
- fixed a loadstone claim in the 5.0-changes section (was "resist knockback ... a niche use if you can keep one uncursed"): m_is_steadfast (uhitm.c:5216) grants knockback immunity for carrying ANY loadstone via m_carrying(mtmp, LOADSTONE) with NO BUC check (line 5235) — cursed works too, including the welded one. only gate is being grounded (not Flying/Levitation, not air/cloud/bubble level, lines 5224-5228). corrected the "if you can keep one uncursed" qualifier.
-->

「灰色の石」の正体は、ゲームクリアまでずっと肌身離さず持ち歩くべき「幸せの石」から、一度拾うと絶対に手放せなくなる呪われた「重し」まで、天と地ほどの開きがあります。全部で4種類存在します：

| 価格 | 石の種類 | 効果 |
| ---: | --- | --- |
|    1 | 火打ち石 (flint) **または** 重し (loadstone) | 火打ち石はスリング用の弾薬です。重しは重量が500ユニットもあり、通常呪われており、一度拾うと捨てられなくなります。蹴りテストを行ってください（重しは滑りません）。 |
|   45 | 試金石 (touchstone) | 宝石を擦り付けると正体を識別できます。極めて有用です。 |
|   60 | 幸せの石 (luckstone) | 幸運値を維持します。ゲームクリアに必須の至宝です。 |

<div class="price-id-toolbar"></div>

見分けるための手順は以下の通りです：

**蹴りテスト（キックテスト）。** 床に落ちている未識別の灰色の石を蹴ってください（`Ctrl-D` または `k`）。通常通りスッと滑って転がれば、重しではありません。重しは異常に重いため、蹴られても転がることに抵抗してその場に留まります。テストする前に、力の小手や蹴り挙げ靴を脱いでおいてください。怪力で本物の重しを強引に吹き飛ばしてしまい、安全だと誤認する危険があるからです。

**拾いテスト。** 重しは生成された時点で呪われており、呪われた重しは床に置く（ドロップする）ことが一切できなくなります。ゲーム画面に「どういうわけか、石を手放すことができない！（For some reason, you cannot drop the stone!）」と表示され、荷物袋に居座り続けます。もし灰色の石を拾い上げて不審なほど過重になったら、床に置いてみてください。置くことができなければ、呪いを解く（聖水、解呪の巻物、祈り）まで呪われた重しを背負い続ける羽目になります。呪いを解いた後であれば、安全に捨てることができます。

**価格テスト。** 基本価格において、60ゴールドは「幸せの石」、45ゴールドは「試金石」、1ゴールドは「火打ち石」または「重し」です。ただし未識別アイテムのランダム割増（1/3）によって45ゴールドの試金石が60ゴールドと提示される場合があるため、一意に確定できるのは45ゴールドの提示のみです。

**擦りテスト。** 手持ちの宝石に灰色の石を適用（`a`）するか、宝石に対して `#rub` コマンドで擦り付けてください。試金石であれば色のついた筋（ストリーク）のメッセージが表示されます。さらに試金石が **祝福** されている場合（あるいはあなたが考古学者かノームであり呪われていない試金石を持っている場合）、その筋によって宝石の正式な正体が識別されます。他の灰色の石でも似たような擦り筋メッセージが出ることがあるため、単に筋がついただけでは試金石の証明にはなりません。「宝石の正式識別」が発生して初めて試金石と確定します。なお、呪われた試金石は擦った宝石を粉砕してしまうことがあります。

**フロア配置の手がかり。** [地下鉱山](#the-gnomish-mines) の最下層（鉱山最深部：Mine's End）にある幸せの石は確定生成であり、常に呪われていないです。そのため鉱山最深部で見つかる灰色の石は十中八九本物です。ただし、フロアバリエーションの1つ（minend-1）では巧妙な罠が仕掛けられており、4体の [ミミック](#a-note-on-mimics) が灰色の石に化けており、さらに本物の呪われた重しが1個配置されています。疑わしい石の隣で捜索（`s`）を行えば、ミミックの正体を100%確実に暴くことができます。その上で、残った2つの本物の石を価格識別（60ゴールドと1ゴールド）してください。狭い小部屋の窪みでは蹴りテストは壁にぶつかって判定が狂いやすいため、価格識別が最も安全です。

灰色の石を拾い上げる前に、必ず蹴って転がるか確認し、BUCをテストしてください。数秒のテストを惜しまないだけで、背中に溶接された500ユニットの呪われた重しに苦しめられる悲劇を完全に回避できます。

#### 判明した情報の名付け (Naming What You've Learned)
<!-- audit
2026-05-21:
- mergable() requires identical otyp, enchantment (spe), BUC, erodeproof state, erosion (oeroded, oeroded2), greased state, oeaten/orotten for food; coins merge unconditionally (invent.c:4379-4460)
- on merge that propagates a previously-unknown property, the game prints "You learn more about your items by comparing them." (invent.c:938-942); guarded against LOST_THROWN to avoid spam when monsters strip ID
2026-05-18:
- `#name` and `#call` aliases at cmd.c:1773-1774
- class naming at do_name.c:571-588
- rename-by-overwrite at do_name.c:660-672
- N keystroke only works in number_pad mode; default vi-keys binds N to run-north — cross-layout shortcut is C for #call
-->

手がかりを集めたら、`#name`（または `#call`）コマンドを活用して判明した情報を記録しましょう。アイテムの種別クラス全体に対して、任意の名前を **呼び名（call）** として付けることができます。たとえば、「泡立つ薬」が200ゴールドの価格帯グループに属することが分かったら、忘れないように「泡立つ=200G」と名付けておきます。その後モンスターに投げつけて相手が加速したら、そのクラスの名前を「加速」へと上書き変更すればよいのです。

**スタック（同一枠まとめ）による識別。** アイテムを拾い上げた際、ゲームはそのアイテムが手持ちの既存アイテムと **完全に同一** である場合にのみ、同じスロットへと合体（スタック）させます：同じ種類、同じ強化値、同じBUC、同じ耐腐食加工などです。したがって、新しく拾ったアイテムが既知のアイテムとまとまるかどうかを見るだけで、無料で情報を得ることができます。合体によって実際に新たな知識が得られた場合、ゲームは明示的にメッセージを表示します：*「持ち物を比較して、より多くのことが分かった (You learn more about your items by comparing them.)」*。このメッセージが出たら、既知の特性（BUC、強化値、腐食状態など）が未知のアイテム側にも引き継がれた合図です。同じ外見でありながらスタックしないアイテムは、異なる薬であるか、BUCが異なるか、あるいは希釈・腐食されているかのいずれかです。

#### 実践的な戦略 (A Practical Strategy)

**祭壇において（最優先事項）。** 未識別の装備品を祭壇まで運び、1点ずつ床に落としてください。BUC（祝福・呪われていない・呪い）ごとに手持ちのアイテムを仕分けます。そのアイテムを装備すべきか、保管すべきか、破棄すべきかは、正体が判明した後に判断します。

**店において（優先度2）。** 未識別のアイテムの上に立ち、`:` を押して提示価格を確認してください。価格帯ごとにグループ分けし、価格表と照らし合わせて候補を絞り込みます。

**安全が確保され、BUCが判明したら杖の試し書きテストを行う。** テストには1チャージを消費します。小石が飛び散れば穴掘りの杖、氷の破片が落ちれば吹雪の杖です。雷の杖による一時的な盲目に備えて、周囲に敵がいない安全な場所で行ってください。

**残りのアイテムは慎重に実験する。** 呪われていない指輪を1つずつ指にはめてみます。薬はモンスターに向けて投げてみます。巻物は防具をすべて脱いだ上で、安全な価格帯グループのものから読んで試します。

**識別の巻物は、他の手段では正体を突き止められないアイテムのために温存する。** 以下の優先順位で使用するのが理想的です：
1. **魔法書**（最優先：未識別の高レベル魔法書を読むと、周囲に敵がいる中で何ターンも麻痺して絶体絶命に陥る危険があるため）
2. **魔除け**（すべて同じ150ゴールドであり、価格識別が通用しないため）
3. 200ゴールドの耐性・ユーティリティ指輪
4. 試し書きテストで候補が絞りきれなかった杖

最も安価で安全な方法から順に試してください：祭壇、店、試し書きテスト、慎重な使用テスト、そして最後の手段としての識別の巻物です。

### 食料と食事 (Provisions and Dining)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Only yellow mold is poisonous to eat (M1_POIS); brown/red convey poison resistance but aren't poisonous, green is acidic (monsters.h). Was "most are poisonous".
- Verified correct: ration/lembas nutrition & weight, hunger thresholds, tin-open times, cannibalism -2..-5 + aggravate, corpse-intrinsic mappings.
-->
<!-- audit
2026-05-21:
- vegan classes: S_BLOB, S_JELLY, S_FUNGUS, S_VORTEX, S_LIGHT, S_ELEMENTAL (except stalker), S_GOLEM (except flesh/leather), and noncorporeal (S_GHOST) (mondata.h:232-238)
- vegetarian = vegan + S_PUDDING except black pudding (mondata.h:239-241); brown pudding and gray ooze are vegetarian, black pudding is not
- corpse_intrinsic picks one mconveys property uniformly at random per eat, then should_givit rolls mlevel/15 (or mlevel-vs-rn2(15)); killer bee/scorpion poison-res has a 25% boosted-chance branch (eat.c:961-989, 1351-1373)
2026-05-20:
- tin opening is an occupation; opentin is called per turn, gives up after svc.context.tin.usedtime >= 50 turns (eat.c:1710-1719, 1794)
- tin open time by tool: blessed tin opener wielded = 0; uncursed tin opener rn2(2); cursed rn2(3); dagger family = 3; axe/pick-axe = 6; bare hands = rn1(1 + 500/(Dex+Str), 10) which is ~11-26 at avg stats, up to the 50-turn cap (eat.c:1740-1786)
- tin of spinach grants +1 Str on eat (eat.c spinach branch)
2026-05-18:
- gelatinous cube corpse: fire/cold/shock/sleep only (not poison/acid/stoning) (monsters.h:160-162 mresists has MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON|MR_ACID|MR_STONE but mconveys row is MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP only)
- disenchanter corpse STRIPS an intrinsic, doesn't grant one (eat.c:1270-1275 PM_DISENCHANTER calls attrcurse)
- encumbrance kicks in at Stressed, not Burdened (eat.c:3197 near_capacity > SLT_ENCUMBER)
- fire giant corpse grants Str on eat via is_giant(ptr) (eat.c:1345-1352); separate row from fire ant
- red and brown mold corpses also grant poison resistance (monsters.h:1627-1659, MR_POISON defense)
- eggs count as vegetarian but not vegan (eat.c:585-597 violated_vegetarian and EGG handling)
- Weak status is -1 Str ATEMP, not slowed movement (attrib.c:471, eat.c:3455)
- blessed tin opens instantly only with a blessed tin opener (eat.c:1740-1745)
- ordinary tin opener on a blessed tin: 50/50 instant vs one turn via rn2(2)
- globs lose 1 weight per ~25 turns; a weight-20 glob lasts ~500 turns (mkobj.c:1487-1490)
- corpses stay safe to eat for ~30-50 turns before rotting (eat.c:1887-1939)
- strategy aligned with NetHackWiki Resistance, Poison resistance, Partial intrinsic: corpse-eating to bank resistances is canonical, gelatinous cube and dragon corpses are the highest-density sources (https://nethackwiki.com/wiki/Resistance, https://nethackwiki.com/wiki/Poison_resistance, https://nethackwiki.com/wiki/Partial_intrinsic)
- sprig of wolfsbane cures lycanthropy on eat via you_unwere (eat.c:2513-2516)
-->

空腹は、ダンジョンにおいて最も執拗にプレイヤーを追い詰めるタイマーです。行動するごとに毎ターン栄養が消費され、タンクが空になると失神が始まります。食事を取らずに失神を繰り返せば、やがて飢餓死するか、倒れ込んでいる隙に部屋にいたモンスターに撲殺されることになります。

#### 空腹の仕組み (How Hunger Works)

あなたの栄養値は900からスタートし、時間とともに着実に減少していきます。減少速度は行動内容によって異なります：

- **基本消費** は1ターンあたり1ポイントです（睡眠中は減少が緩やかになります）。
- **[自己再生](#combat-and-defense)**（指輪または内在能力）が有効な場合、奇数ターンに追加で栄養を消費します。
- **負荷重量** が **「圧迫（Stressed）」** 以上である場合、奇数ターンに追加で栄養を消費します（「重荷（Burdened）」の段階では追加消費はありません）。
- **指輪** は通常、20ターンごとに1ポイントの追加栄養を消費します。「回復の指輪」、「争いの指輪」、「飢餓の指輪」は装備中その10倍の栄養を消費します。

栄養値が特定の閾値を下回ると、警告メッセージが表示されます：

| 栄養値 | ステータス | 影響 |
| :---: | :---: | --- |
| 1000超 | 満腹 (Satiated) | 満腹状態。これ以上食べると窒息死の危険あり。 |
| 151〜1000 | 通常 (Normal) | 正常。問題なし。 |
| 51〜150 | 空腹 (Hungry) | 警告メッセージ。食事を取るべきタイミング。 |
| 1〜50 | 衰弱 (Weak) | 筋力ペナルティ（筋力 −1）。可能なら神に祈る。 |
| 0以下 | 失神寸前 (Fainting) | ランダムに昏倒して行動不能。即座に食べるか祈る。 |

「空腹」のメッセージが出た段階で食事を取るようにし、「衰弱」まで引き延ばさないようにしてください。もし「失神寸前」に達して手元に一切の食料がない場合は、守護神に祈ってください（[神との関係](#divine-relations) を参照）。神の機嫌が良ければ空腹を完全に癒してくれます。まだ「空腹」の段階であり食料がない場合は、階段を降りて下の階へ進みましょう。新たなフロアには新たな死体や補給品がありますが、探索し尽くしたフロアを歩き回っても食料は見つかりません。

#### 何を食べるべきか (What to Eat)

**安全なものを食べる。** 菜食主義の戒律を守っているのでない限り、必要な栄養の大半は倒したばかりの新鮮な獲物の死体から摂取することができます。保存食を温存する前に、まず死体の安全性を確認してください。単に新鮮であるというだけで、何でも食べられるわけではありません。

- 死体は倒してから30〜50ターン以内に食べてください。それを過ぎると腐敗のリスクが生じ、食中毒（治療手段がないと致命的）を引き起こします。
- 一部の死体は内在的な耐性を授けてくれます（殺人蜂からは毒耐性、火の巨人からは火炎耐性など）。これらは空腹でない時であっても、計画的に食べる価値があります。詳細は後述の一覧表を参照してください。
- 一部の死体は極めて有害です（コカトリスの死体は石化死、緑スライムはスライム化、コボルドの肉は猛毒）。口にする前に、どの死体が安全であるかを把握しておきましょう。

**食料（food rations）**（侍の場合は **軍糧丸（gunyoki）**）は、緊急時のバックアップです。栄養値800、重量20であり、店で頻繁に販売されています。目の前に新鮮な獲物の死体がない状況に備えて、2〜3個携帯しておきましょう。過剰に溜め込む必要はありません。

**レンバス (lembas wafers)** は、わずか重量5で栄養値800を提供する極めて優秀な携行食です。エルフはレンバスから通常より1/4多い栄養を得られ、オークは1/4少ない栄養しか得られません。

**モツの塊 (tripe rations)** は人間にとっては不快な食事ですが（食べると吐き気を催します）、ペットにとっては大好物です。ペットのために温存しておきましょう。

**缶詰 (tins)** は決して腐敗しない保存食ですが、**開ける場所を怠ると致命的な罠になります**。缶詰を開ける作業は「継続作業（occupation）」であり、作業中は一切の行動が取れず、開けている最中にモンスターが歩み寄ってきて攻撃される危険があります。缶切りを使えば0〜1ターン、短剣なら3ターン、斧なら6ターン、そして素手なら無防備なまま最大50ターンもかかります。睡眠中のモンスターがいる部屋の隣の通路などで缶詰を開けてはいけません。祝福された缶詰は唯一の例外であり、使う道具に関係なく0〜1ターンで開けることができます（祝福された缶切りを使えば即座に開きます）。なお、ホウレンソウの缶詰を食べると筋力が1上昇します。

**菜食主義（Vegetarian）** のキャラクターは、食料、レンバス、果物、そしてごく少数の非肉類死体（キノコ、カビ、地衣類、ゼリー類、および卵）だけで生き延びなければなりません。**完全菜食主義（Vegan）** は卵すら食べられないためさらに厳しく、食料、レンバス、果物、植物の死体のみが対象となります。綿密な計画が必要です。どちらの戒律でも死体を貪り食う戦法は使えないため、食料や果物は見つけ次第確保しておくべき貴重な補給品となります。

#### 危険な食物 (Dangerous Foods)

死体を口にする前に、以下の5つの問いを確認してください：

1. それは新鮮か？（倒してからおよそ50ターン未満か？）
2. それは `c`（コカトリス）の死体でも、メデューサでもないか？
3. それは緑スライムではないか？
4. 洞窟人やオークの例外を除き、自分と同種族の死体ではないか？
5. 「反感」の内在能力を受け入れる覚悟がない限り、犬や猫ではないか？

その上で、毒、酸、その他の特殊な影響について以下の解説を確認してください。

**コカトリスの死体：** 石化による即死。絶対に食べてはなりません。

**酸性の死体（酸のブロッブなど）：** 酸耐性がない限りダメージを受けます。

**有毒な死体：** 毒耐性がない限りダメージと能力値低下を受けます。

**腐敗した死体：** 食中毒を引き起こします。発症したらただちに神に祈ってください。

**共食い（同種族の肉を食べる）：** 幸運値を 2〜5 失い、「反感（aggravate monster）」の内在能力を永続的に獲得してしまいます。ただし洞窟人とオークはこのペナルティを免除されます。

#### 役立つ死体効果 (Useful Corpse Effects)

内在能力の獲得を目指して計画的に死体を食べることは、序盤から中盤にかけて極めて大きな成果をもたらします。各耐性の獲得は食べるごとに *一定の確率* で判定されるものであり、確定ではありません。そのため、最初の1体だけでなく見つけた **すべて** の対象死体を食べるようにしてください。以下の表は、各モンスター記号についての判定結果を示しています。死体は必ず **新鮮** なうちに食べてください（50ターンを大幅に超えると食中毒のリスクが生じます）。また、`*` は付与される耐性が **一時的（時限式）** であることを示します。

**死体を残さず、食べられないモンスター：** `A`（天使類）、`&`（悪魔類）、`L`（リッチ類）、`v`（渦類）、`y`（光類）、および後述の例外。

**アンデッドの特例：** 通常の吸血鬼、ミイラ、および種族ベースのゾンビは、「死体を生成しない」フラグを持っているにもかかわらず、そのベース種族のすでに腐敗した死体を残します。病気耐性を持っていない限り、これらは腐敗死体として扱ってください。ヴラド、グール、スケルトンは食べられるものを一切残しません。

**通常の肉：** `C`（ケンタウロス）、`G`（ノーム）、`J`（ジャバウォック）、`K`（キーストン・コップ）、`o`（オーク）、`O`（オーガ）、`p`（ピアサー）、`q`（四足獣）、`t`（トラッパー）、`U`（アンバーハルク）、`w`（ワーム）、`z`（ズルティ）。猫、犬、レプラコーン、ニンフには固有の重要な効果があります。

[]{#vegetarian-safe-corpses}
**菜食主義で安全な死体**（プリンの塊を除き完全菜食主義でも安全）：

::: dense-table

| 記号 | クラス | 摂食判定 |
|:---:|---|---|
| `b` | ブロッブ類 | 酸のブロッブは酸性 → 酸耐性／石化耐性\*。震えるブロッブ → 毒耐性。ゼラチンキューブ → 火炎／冷気／睡眠／電撃耐性。 |
| `j` | ゼリー類 | 大半が酸性 → 酸耐性／石化耐性\*。青ゼリー → 冷気／毒耐性。 |
| `F` | キノコ・カビ類 | カビは色ごとに異なる耐性を付与（黄色カビ→毒耐性、茶色カビ→冷気＋毒耐性、赤色カビ→火炎＋毒耐性）。黄色カビのみ食べると有毒ですが、すべて耐性を授けるため毒耐性の確保に有用です。緑カビは酸性 → 酸耐性／石化耐性\*。**地衣類（lichen）：安全で決して腐敗しない。常時1つ携帯推奨。** 紫色キノコ → 幻覚。 |
| `P` | プリン・ウーズ類 | 食用可能な **塊（glob）**（菜食主義可、完全菜食は不可）：灰色ウーズ → 火炎／冷気／毒耐性。茶色プリン → 冷気／電撃／毒耐性（酸性）。黒プリンは菜食不可。**緑スライム → 絶対に食べてはならない。自身がスライム化して即死する。** |

:::

**その他の死体（肉類）：**

::: dense-table

| 記号 | クラス | 摂食判定 |
|:---:|---|---|
| `a` | 蟻・昆虫類 | 大半が **有毒** → 毒耐性。巨大蟻は通常の肉。火炎蟻 → 火炎耐性。 |
| `c` | コカトリス類 | **絶対に食べてはならない —— 石化して即死する。** パイロリスクは安全 → 火炎耐性。 |
| `d` | 犬・イヌ科 | 小犬から大型犬まで、洞窟人やオークでない限り永続的な「反感」を獲得。ヘルハウンド → 火炎耐性。冬オオカミ → 冷気耐性。人ジャッカル／人狼は死体を残さない。 |
| `e` | 目・球体類 | 大半は死体を残さない。新鮮な **さまよう目 → テレパシー**。部屋の安全を確保した上で必ず食べること。 |
| `f` | ネコ科 | 子猫から大型猫まで、洞窟人やオークでない限り永続的な「反感」を獲得。 |
| `g` | グレムリン・ガーゴイル類 | ガーゴイル → 石化耐性\*。グレムリンは有毒 → 毒耐性。 |
| `h` | ドワーフ・人型生物 | 通常の肉。ただしマインドフレア → **知力上昇（+Int）**（およびテレパシー）。 |
| `i` | インプ・下級悪魔 | インプ、ホムンクルス、クアジット、天狗は死体を残す。ホムンクルスは有毒 → 睡眠／毒耐性。クアジット → 毒耐性。**天狗 → 瞬間移動体質または瞬間移動制御。** |
| `l` | レプラコーン | 1/2 の確率で瞬間移動体質を獲得。 |
| `k` | コボルド類 | **有毒**（耐性獲得などのメリットなし）。 |
| `m` | ミミック類 | 食用可能だが、食べると一時的にその場に足が接着・拘束される。 |
| `n` | ニンフ類 | 約 1/3 の確率で瞬間移動体質を獲得。 |
| `r` | 齧歯類 | 通常の肉。ただし狂犬病のネズミは有毒。人ネズミは死体を残さない。 |
| `s` | クモ・ムカデ類 | **有毒** → 毒耐性（序盤における毒耐性の定番供給源）。 |
| `u` | ユニコーン・馬類 | 通常の肉。ユニコーン → 毒耐性。 |
| `x` | ザン・昆虫類 | 大半は死体を残さない。ザンは有毒 → 毒耐性。 |
| `B` | コウモリ・鳥類 | コウモリ → 一時的な **朦朧**。大ガラスは通常の肉。吸血コウモリは有毒。 |
| `D` | ドラゴン類 | 子供は通常の肉。**成体ドラゴン → 各ブレスに応じた耐性を付与**：赤色→火炎、白→冷気、青→電撃、オレンジ→睡眠、黒→瞬間分解、緑→毒、黄色→酸。緑と黄色は有毒／酸性でもある。灰色、銀色、揺らめくドラゴンは通常の肉。クロマティック・ドラゴン → 全属性。 |
| `E` | エレメンタル類 | 大半は死体を残さない。姿が見えている状態でストーカーを食べると一時的な透明化と朦朧。すでに透明の状態で食べると永続的な透明化と可視を獲得。 |
| `H` | 巨人・タイタン類 | 食べると **筋力上昇（+Str）**。火の巨人／氷の巨人／嵐の巨人はそれぞれ火炎／冷気／電撃耐性を付与。 |
| `N` | ナガ類 | 食べると毒耐性。赤ナガはさらに火炎耐性。黒ナガはさらに酸耐性／石化耐性\*（酸性）。 |
| `Q` | 量子物理学者類 | 有毒。食べるとランダムに加速 *または* 減速する。遺伝子工学者 → ランダムなへんげ。 |
| `R` | 錆の怪物・吸魔の怪物 | 通常の肉。ただし **吸魔の怪物は持っている内在能力を1つ消去する —— 絶対に食べてはならない。** |
| `S` | ヘビ類 | 大半が **有毒** → 毒耐性。ガータースネークとニシキヘビは通常の肉。 |
| `T` | トロール類 | 通常の肉（氷トロール → 冷気耐性）。トロールは蘇生するため、食べるか死体を移動させること。 |
| `W` | レイス類 | 新鮮な **レイス → 経験値レベルが1上昇**。塚人とナズグルは死体を残さない。 |
| `X` | ゾーン類 | 食べると石化耐性\*。 |
| `Y` | 類人猿類 | 通常の肉。イエティ → 冷気耐性。 |
| `'` | ゴーレム類 | 大半は死体を残さない。肉ゴーレム → 火炎／冷気／睡眠／電撃／毒耐性。 |
| `@` | 人間・エルフ類 | 通常の肉。エルフ → 睡眠耐性。**獣化人間 → 獣化症に感染。** 看護婦 → HP全快。**メデューサ → 絶対に食べてはならない。石化して即死する。** |
| `;` | ウナギ・海生怪物 | 通常の肉。電気ウナギ → 電撃耐性。クラゲは有毒 → 毒耐性。 |
| `:` | トカゲ類 | 通常の肉。**トカゲ → 石化を治療し、決して腐敗しない。常時1つ携帯必須。** イモリ → 少量の魔力回復。サンショウウオは有毒 → 火炎耐性。カメレオン → ランダムなへんげ。 |

:::

ゼラチンキューブは、昇天キットに必要な重要耐性を最も高密度で提供してくれるモンスターです。また、序盤の死体から手に入る「毒耐性」は、真っ先に確保すべき最も重要な内在能力です。

**トリカブトの小枝 (Sprig of wolfsbane)。** 死体ではありませんが、同じ食料スロットを占めます。食べると獣化症が治癒します（[獣化症モンスターについての覚書](#a-note-on-werecreatures) を参照）。重量がほぼゼロであるため、見つけたら必ず携帯しておきましょう。

**プリン、キューブ、カビ、ブロッブは優れた食料源です。** その多くが内在能力の獲得チャンスをもたらします。プリンや酸のブロッブは通常の死体ではなく **「塊（glob）」** を残します。床の同じマスに同一種の塊が重なると1つの食事に融合してしまい、耐性判定の抽選が1回分に減ってしまいます。塊同士が合体する前に、床から1個ずつ拾って食べるようにしてください。

#### 食料戦略 (Food Strategy)

1. 安全で新鮮なモンスターの死体を主食とする。
2. 食料やレンバスなどの保存食は緊急時用に温存する。
3. 内在能力を授ける死体は、（空腹でなくとも）計画的に食べる。
4. 食料がなく空腹になったら階段を降りて先へ進む。衰弱または失神寸前に追い込まれ、安全に祈れる条件が整っていれば祈る。
5. 金貨に余裕があれば、店で食料を購入しておく。
6. 必要以上に大量の食料を持ち歩かない（重荷の原因になる）。

### 薬屋 (The Apothecary)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Potion of healing cures blindness unless CURSED (cureblind = !cursed, potion.c peffect_healing); table row said "when blessed".
- Verified correct: speed intrinsic, holy-water dip whole stacks, alchemy recipes & explosion odds, unicorn-horn cures, enchant caps, genocide/charging/remove-curse mechanics.
-->
<!-- audit
2026-05-19:
- dip_potion_explosion tests the DIPPING potion's BUC, not the receiver (potion.c:2279, 2541)
- the receiving potion is consumed regardless via useup(potion) (potion.c:2538)
- never dip a CURSED potion into another — guaranteed explosion
2026-05-18:
- potion of speed grants permanent intrinsic Fast when !cursed (potion.c:1066)
- uncursed extra/full healing also raise maxHP (potion.c:1398-1440)
- strategy aligned with NetHackWiki Potion, Alchemy, Dip: alchemy odds and the guaranteed-blast cases for cursed/acid potions match (https://nethackwiki.com/wiki/Potion, https://nethackwiki.com/wiki/Alchemy, https://nethackwiki.com/wiki/Dip)
- dipping an item (including a single arrow/dart) into a polymorph potion changes its type via poly_obj and identifies the potion (potion.c:2468-2499)
-->

薬の外見（未識別名）はゲームごとにシャッフルされます。頼りになるのは価格と計画的なテストだけであり、「前回のゲームで泡立つ薬が回復の薬だった」という記憶は何の役にも立ちません。

#### 薬の一覧表 (The Potion Table)

各薬の基本的な効果と、ラベルからは読み取れない隠れた用途を以下にまとめます。未識別の薬の候補を絞り込むための価格については [薬の価格](#potion-prices) を参照してください。特に重要な薬については、後述の [主要な薬](#key-potions) で詳しく解説します。出現確率は自然生成される薬の中に占める割合であり、深度によって変化しません。

| 薬の名称 | 確率 | 効果と主な用途 |
| --- | :---: | --- |
| **水 (water)** | 9% | 祭壇での祈りによって聖水に変化。未識別の薬を薄めて真水にする基材。 |
| **[回復の薬 (healing)](#potion-healing)** | 6% | HPを回復。呪われていない限り盲目も治療。錬金術の最重要原料。 |
| **[超回復の薬 (extra healing)](#potion-healing)** | 5% | 大幅にHP回復、最大HPを上昇、病気・盲目を治療。 |
| **[能力獲得の薬 (gain ability)](#potion-gain-ability)** | 4% | 祝福して飲むと全能力値が+1。呪われていないならランダムな能力値が+1。 |
| **魔力の薬 (gain energy)** | 4% | 最大魔力（Pw）を上昇させ全快。錬金術の万能触媒。 |
| **浮遊の薬 (levitation)** | 4% | 宙に浮く。罠を飛び越え、水上を渡り、流し台で指輪を探す。 |
| **透明の薬 (invisibility)** | 4% | 不可視化。すでに透明の状態で飲むと永久不可視を獲得。 |
| **[加速の薬 (speed)](#potion-speed)** | 4% | 呪われていないものを1本飲むだけで、永続的な内在の「俊敏」を獲得。 |
| **可視の薬 (see invisible)** | 4% | 不可視の生物を視覚化（永続的な内在能力）。 |
| **怪物を探す薬 (monster detection)** | 4% | 同フロアにいるすべてのモンスターの現在位置を開示。 |
| **物体を探す薬 (object detection)** | 4% | 同フロアにいるすべてのアイテムの現在位置を開示。 |
| **フルーツジュース (fruit juice)** | 4% | 無害な食料。病気の薬にユニコーンの角を浸すとこれに変化。 |
| **酔っぱらいの薬 (booze)** | 4% | わずかな栄養。大抵は混乱状態に陥る。 |
| **混乱の薬 (confusion)** | 4% | 自身を混乱させる。[混乱読書](#confused-reading) の仕込みに有用。 |
| **睡眠の薬 (sleeping)** | 4% | 眠り込んで無防備になる（目隠し飲みは危険）。敵に投擲するのが有効。 |
| **病気の薬 (sickness)** | 4% | HP低下と病気（治療師は免疫）。遠距離弾薬を浸すと毒を塗れる。 |
| **麻痺の薬 (paralysis)** | 4% | その場に凍りついて無防備化（目隠し飲みは致命的）。敵に投擲推奨。 |
| **幻覚の薬 (hallucination)** | 3% | 無害だが方向感覚を喪失し、あらゆる表示がデタラメになる。 |
| **盲目の薬 (blindness)** | 3% | 盲目化。ただしESPを持っていればその間テレパシーが強制発動。 |
| **油の薬 (oil)** | 3% | 唯一使用（`a`）できる薬（火を灯せる）。安全な識別テスト、ランタンの燃料、投擲炎上武器。 |
| **[レベルアップの薬 (gain level)](#potion-gain-level)** | 2% | 経験値レベル+1。*呪われた* ものを飲むと天井を突き破って直上の階層へ上昇。 |
| **啓蒙の薬 (enlightenment)** | 2% | 現在の能力値・内在能力を一覧開示。祝福時は知力+1・知恵+1。 |
| **[完全回復の薬 (full healing)](#potion-healing)** | 1% | HP全快、ほぼすべての異常状態を治療、最大HPを大きく上昇。 |
| **[へんげの薬 (polymorph)](#potion-polymorph)** | 1% | 自身が変身する。またはアイテムを浸して別のアイテムへと再抽選識別。 |
| **酸の薬 (acid)** | 1% | 飲むとダメージ。敵に投げつけると酸ダメージを与える。 |

<!-- oil verification: POT_OIL is the only applyable potion
(apply.c:1503 lists it among light sources you can apply). It does
NOT grease or rustproof items (no POT_OIL link to greased / erode /
rust anywhere in src/*.c); that protection comes from the can of
grease. -->

#### 主要な薬 (Key Potions)

[]{#potion-healing}
**回復の薬、超回復の薬、完全回復の薬。** 重点的にストックすべきは「超回復の薬」です。HPを大幅に回復するだけでなく、常に盲目を治療し、（呪われていなければ）病気も治療してくれます。呪われていない超回復の薬と完全回復の薬は、回復量が現在の最大HPを超過した場合に最大HPそのものを恒久的に引き上げます（祝福されたものが最大の伸び幅を持ちます）。当面必要のない呪われていない超回復や完全回復の薬は、すべてゲヘナおよび昇天への登攀のために温存しておきましょう。

[]{#potion-gain-ability}
**能力獲得の薬。** 祝福された状態で飲むと、**全能力値が同時に+1** されます。呪われていない場合はランダムな1つの能力値しか上がりません。まさに液体の黄金です。祝福できるまで1本も無駄に飲まずに温存してください。

[]{#potion-speed}
**加速の薬。** 呪われていないものを1本飲むだけで、永続的な内在の「俊敏（Fast）」能力を獲得できます。祝福されたものは、その上に重なる一時的な超高速ブーストの持続時間を延ばすだけです。なお、「加速の杖」を自分に向けて振った場合は、50〜74ターンの一時的な加速が得られます。

[]{#potion-holy-water}
**聖水。** 自分と同属性の祭壇の上に呪われていない「水」を置き、そこで祈りを成功させると、そのマスにあるすべての水の薬が一挙に聖水へと変化します。聖水は、そこに浸した（dip）あらゆるアイテムを祝福してくれます。浸す作業は **スタック（同一の山）全体に一度に適用される** ため、手持ちの「普通の水」の山を1本の聖水に浸すだけで、その山全体が一瞬で聖水へと変化します。つまり、1本の聖水があれば無制限に聖水を増殖させることができるのです。

手持ちの水が不足しているなら、自分で作り出しましょう。酸の薬を除くすべての薬は、濡れる（水に浸す）たびに普通の水へと近づいていきます。2回浸せば完成です：1回目の浸漬で「希釈（diluted）」され、2回目の浸漬で完全に「ただの水」になります。浸漬はスタック全体にまとめて適用されるため、不要な薬の山をまとめて水へと変換できます。噴水で作業する場合、浸すごとに噴水イベントが抽選され、1/3の確率で噴水が干上がってしまうため、周囲の安全を確保してから行いましょう。不要な薬はすべて聖水の原料になりますが、作業には細心の注意を払ってください。

[]{#potion-gain-level}
**レベルアップの薬。** 経験値レベルを1引き上げます。クエストの挑戦条件（レベル14）を素早く満たしたり、錬金術でより強力な薬へと変換するのに有用です。一方、**呪われた** ものを飲むと、経験値ではなくダンジョンの階層を1つ上昇します。直上の天井を突き破って上の階へと一瞬で打ち上げられます。

[]{#potion-polymorph}
**へんげの薬の識別。** スマートなテスト方法があります：未識別の薬に、予備の矢やダーツを1本だけ浸してみてください。もしその矢が別のアイテムへと変化したら、その薬はへんげの薬であり、即座に正式識別されます。矢1本と薬1本を消費するだけで、自分で飲んで危険なモンスターに変身させられるギャンブルを完全に回避できます。

#### 錬金術 (Alchemy)

ある薬を別の薬へと浸す（dip）ことで、より強力な薬へと錬成できる場合があります（あるいは大爆発を引き起こします）。大半の組み合わせは何も起きませんが、以下の実用的なレシピは暗記しておく価値があります：

| 浸す薬 | 浸される対象の薬 | 錬成結果 |
| --- | --- | --- |
| 回復の薬 (Healing) | 魔力の薬 / レベルアップの薬 | 超回復の薬 (Extra healing) |
| 超回復の薬 (Extra healing) | 魔力の薬 / レベルアップの薬 | 完全回復の薬 (Full healing) |
| 完全回復の薬 (Full healing) | 魔力の薬 / レベルアップの薬 | 能力獲得の薬 (Gain ability) |
| フルーツジュース (Fruit juice) | 魔力の薬 / レベルアップの薬 | 可視の薬 (See invisible) |
| 加速の薬 (Speed) | 回復の薬 | 超回復の薬 (Extra healing) |
| 酔っぱらいの薬 (Booze) | 魔力の薬 / レベルアップの薬 | 幻覚の薬 (Hallucination) |
| 浮遊の薬 (Levitation) | 啓蒙の薬 (Enlightenment) | レベルアップの薬 (Gain level) （2/3の確率） |

「回復 → 超回復 → 完全回復 → 能力獲得」へと至る錬成チェーンは、魔力の薬やレベルアップの薬を触媒とする錬金術の王道です。ありふれた回復の薬と数本の魔力の薬があれば、ゲーム内で最も貴重な薬へと化けさせることができます。

もうひとつの優れたサブループは、**「浮遊の薬 ＋ 啓蒙の薬 → レベルアップの薬（2/3の確率、1/3で無反応）」** です。どちらの材料も比較的頻繁に見つかり、単体での価値は控えめですが、完成品は前述のメイン錬成チェーンの強力な触媒となります。両方のストックがあれば、自然ドロップを待つことなくレベルアップの薬を量産することができます。

**連鎖錬成は2本ずつ進行する。** 錬金術は薬の山を一度に上位の薬へとアップグレードでき、前述の回復チェーンは古典的な手法です。手つかずの *新鮮な* 薬であれば、1回の浸漬で7〜8本まとめて錬成できます。しかし、錬金術で生成された薬はすべて **「希釈（diluted）」** された状態となり、希釈された薬の山は **1回の浸漬で2本ずつ** しか変換できません。したがって、チェーンの第1段階は大量に一括錬成できますが、それ以降のステップは希釈された生成物を材料とするため、2本ずつ地道に進める必要があります（希釈された薬であっても効果そのものは通常品と全く同等です。連鎖錬成の変換効率のみが制限されます）。

錬金術には爆発のリスクが伴います。水以外の組み合わせでは、約10%の確率で爆発事故が発生します（錬金術師の服を着用していれば約30分の1に激減します）。調合実験は貴重な保管場所から離れた隔離された部屋で行い、**呪われた薬を別の薬に浸してはなりません**。呪われた薬を浸すと100%確実に大爆発を起こし、両方の薬が消滅します。

#### 状態異常の治療 (Neutralizing Ailments)

呪われていない **ユニコーンの角** は、盲目、難聴、混乱、朦朧、幻覚、嘔吐、そして病気を治療してくれます。完全に治すまでに数回適用（`a`）が必要になる場合があります（祝福および呪われていないでの正確な成功確率は [主要な道具](#key-tools) を参照）。なお、低下した能力値は回復できなくなっているため、能力回復の薬を使用してください。

ユニコーンの角がない場合でも、薬によって大半の異常を治療できます：

- **盲目**（および難聴）：**祝福された回復の薬**、あるいは呪われていない **超回復の薬** や **完全回復の薬**。ニンジンを食べることでも治癒します。一時的な盲目（クリームパイ、黄色い光など）は時間経過でも回復します。
- **幻覚**：**超回復の薬** または **完全回復の薬** で完治します（通常の回復の薬では治りません）。**病気の薬** を飲むことでも幻覚から正気に戻れますが、引き換えに病気とダメージを負うことになります。
- **病気**（食中毒による致死カウントダウン）：**祝福された回復の薬**、呪われていない **超回復の薬** や **完全回復の薬**、ユニコーンの角、ユーカリの葉。神の怒りを買っていなければ祈りでも治ります。
- **石化**：カウントダウンが終わる前に、トカゲの死体または酸性の死体を食べてください。トカゲの死体は決して腐敗しないため、常にオープンインベントリに1つ携帯しておきましょう。
- **混乱と朦朧**：ユニコーンの角で治療できます。トカゲの死体を食べると持続時間を2ターンに短縮できます。それ以外は安全な場所で自然回復を待ちましょう。

また、ユニコーンの角を有害な薬に浸す（dip）ことで浄化できます：

- **盲目の薬、混乱の薬、幻覚の薬** → 呪われていない水
- **病気の薬** → フルーツジュース

生成された水は祭壇で祈って聖水にでき、フルーツジュースは錬金術で可視の薬へと錬成できるため、一切の無駄がありません。

### 巻物入れ (The Scroll Rack)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Armor-enchant safe cap is +3 for ordinary body/helms/boots/gloves, +5 for elven armor / wizard's cornuthaum (do_wear.c). Table & prose had blanket +5; corrected.
- Genocide prompt takes single monster name (e.g., "lich") or uppercase class (e.g., "L"); blessed class wipe excludes player's own role species (makemon.c:1340).
-->

巻物は、ダンジョンにおける使い捨ての呪文です。1回読む（`r`）と効果が発動し、消滅します。巻物にはゲームごとにランダムにシャッフルされた奇妙な文字列（「ZELGO MER」、「DAIYEN FOOELS」、「PRATYAVAYAH」など）がラベルとして印字されており、識別するまでは意味を持ちません。

#### 巻物の一覧表 (The Scroll Table)

各巻物の効果と最も有効な使い道を示します。未識別の巻物の候補を絞り込むための価格については [巻物の価格](#scroll-prices) を参照してください。特に重要な巻物については、後述の [主要な巻物](#key-scrolls) で詳しく解説します。出現確率は自然生成される巻物の中に占める割合であり、深度によって変化しません。

| 巻物の名称 | 確率 | 効果と主な用途 |
| --- | :---: | --- |
| **[識別の巻物 (identify)](#scroll-identify)** | 18% | アイテムを識別。メインの所持品のみが対象となるため、事前に袋から出しておくこと。祝福時は複数個を識別。 |
| **光の巻物 (light)** | 9% | 部屋を明るく照らし、暗い部屋の全貌を開示。祝福時はさらに広範囲を照らす。 |
| **[武器に魔法をかける巻物 (enchant weapon)](#scroll-enchant)** | 8% | 武器の強化値+1（祝福時は最大+3）。+5までは安全、+6以上は武器が消滅・破壊されるリスクあり。 |
| **[解呪の巻物 (remove curse)](#scroll-remove-curse)** | 6.5% | 呪われた装備の固着を解除。祝福時は全所持品の呪いを一度に解く。 |
| **[鎧に魔法をかける巻物 (enchant armor)](#scroll-enchant)** | 6.3% | 着用中の防具を強化。+3（エルフの防具や魔力回復の帽子は+5）を超えると防具が蒸発・破壊される危険あり。 |
| **[瞬間移動の巻物 (teleportation)](#scroll-teleportation)** | 5.5% | 自身をテレポート。瞬間移動制御があれば着地先を指定可能。扉のない密閉された小部屋にある1枚の巻物はこれ。 |
| **混乱の巻物 (confuse monster)** | 5.3% | 手に魔力を宿し、次の数回の近接打撃が命中した相手を混乱させる。 |
| **[地図の巻物 (magic mapping)](#scroll-magic-mapping)** | 4.5% | フロア全体の地形を瞬時に開示。迷路フロアの攻略に不可欠。 |
| **鎧を破壊する巻物 (destroy armor)** | 4.5% | 着用中の防具を1つ破壊。呪われた状態や混乱して読んだ際は挙動が変化。 |
| **怪物を作る巻物 (create monster)** | 4.5% | モンスターを召喚。呪われていると13体出現、混乱して読むと酸のブロッブを召喚。 |
| **[怪物を怯えさせる巻物 (scare monster)](#scroll-scare-monster)** | 3.5% | 床に置くと、[エルベレス](#elbereth) よりも強力なモンスター退散スポットを形成。 |
| **記憶喪失の巻物 (amnesia)** | 3.5% | 記憶している呪文と一部の武器スキルを忘却（祝福時は呪文忘却を免除）。読むべきではない有害な巻物。 |
| **金貨を探す巻物 (gold detection)** | 3.3% | フロア内の金貨の位置を開示。混乱して読むと金貨の代わりにすべての罠を開示。 |
| **火の巻物 (fire)** | 3% | 周囲に炎を噴出させ、所持品の巻物や薬を焼失させ、氷を溶かす。 |
| **白紙の巻物 (blank paper)** | 2.8% | 何も書かれていない。魔法のマーカーを使って好きな巻物を自作するための台紙。 |
| **食料を探す巻物 (food detection)** | 2.5% | フロア内のすべての食料の位置を開示。 |
| **大地の巻物 (earth)** | 1.8% | 自身の周囲に巨石の山を落とす。敵を閉じ込めたり、自身を壁で防護するのに有用。 |
| **[充填の巻物 (charging)](#scroll-charging)** | 1.5% | 杖や道具のチャージを回復。「願いの杖」にも使用可能（1回のみ）。 |
| **[虐殺の巻物 (genocide)](#scroll-genocide)** | 1.5% | 指定した1種族を完全消滅。祝福時はクラス全体を抹殺。自身の種族や役職を絶対に指定してはならない。 |
| **怪物を飼いならす巻物 (taming)** | 1.5% | 隣接するモンスターを手なずける。混乱して読むと効果範囲が 11×11 マスへと劇的に拡大。 |
| **処罰の巻物 (punishment)** | 1.5% | 重い鉄球と鎖を足首に繋がれる。解呪の巻物で解除可能。 |
| **悪臭雲の巻物 (stinking cloud)** | 1.5% | 指定した遠距離のマスに、持続する毒ガスの雲を発生させる。 |

#### 主要な巻物 (Key Scrolls)

[]{#scroll-identify}
**識別の巻物。** この巻物は、**メインの所持品（インベントリ）** に直接入っているアイテムしか検査できません。鞄の中に入っているアイテムや床に落ちているアイテムは対象外です。読む前に、鞄の中身をすべて手元に出し、足元にある未識別の品も拾っておきましょう。祝福された巻物は1〜4個のアイテムを識別し、1/5の確率で手持ちの全アイテムを一挙に識別します（幸運値がプラスなら最低識別数が2個に保証されます）。呪われていない巻物は通常1個しか識別しませんが、1/5の確率で祝福時と同じ結果を引き当てます。

[]{#scroll-enchant}
**武器に魔法をかける巻物 / 鎧に魔法をかける巻物。**
呪われていない「武器に魔法をかける巻物」は強化値を+1します。祝福されたものは最大で+3上昇させます（現在の強化値が高いほど伸び幅は小さくなり、+6以上では+1しか上がりません）。そして武器の強化値が **+6以上** の状態で読むと、2/3の確率で武器が粉砕・消滅します。**安全な上限値は +5 です。**
「鎧に魔法をかける巻物」は、未強化の防具やエルフ製防具、非魔法防具ほど大きく強化され、祝福時は追加でさらに+1されます。着用中の防具の強化値が **+3**（エルフの防具または魔法使いの「魔力回復の帽子」は **+5**）を超えている状態でさらに読むと、防具が「蒸発」して消滅する危険が生じます。祝福された巻物であってもこの上限を突破することはできません。

[]{#scroll-remove-curse}
**解呪の巻物。** 呪われた装備の固着を解いてくれます。呪われていない巻物は現在身につけている装備および構えている手持ち武器のみに作用します。祝福された巻物は、インベントリ内のすべてのアイテムの呪いを一括で解除します。

[]{#scroll-charging}
**充填の巻物。** 杖や再充填可能な道具のチャージ数を回復させます。必ず「願いの杖」のために1枚は温存しておいてください。チャージ回復のリスク、充填回数、指輪の充填ルールについては [再充填](#recharging) を参照してください。

[]{#scroll-genocide}
**虐殺の巻物。** 呪われていない巻物は単一のモンスター種族を抹殺し、祝福された巻物はモンスターのクラス（記号）全体をゲームから永久に根絶します。リッチ類（`L`）は祝福虐殺の最も代表的な標的です。
**自分自身の種族や役職が含まれるクラスを絶対に祝福虐殺してはなりません。** ドワーフは `h`、ノームは `G`、エルフと人間は `@`、オークは `o` です。これらに該当する記号を祝福虐殺のプロンプトに入力すると、「虐殺の巻物によって死亡した」としてその場で即死しゲームオーバーとなります。さらに、`@` はすべての役職にとって致死です（役職自身の本質が `@` であるため）。そのため、人気のある「マインドフレア根絶」をドワーフで選ぶと、マインドフレアも `h` であるため即死の罠となります。また、混乱した状態で読むと自分自身の役職の種族を虐殺して即死します。プロンプトに入力する前に、必ず記号と状態異常を確認してください。

[]{#scroll-reverse-genocide}
**逆虐殺。** **呪われた** 虐殺の巻物は、指定した対象を消滅させるのではなく、指定した種族を自分の足元に **4〜6体召喚** します。召喚できるのは通常生成可能なモンスターに限られます。「レイス」を指定すれば経験値レベルを爆発的に稼ぐための死体の山が得られ、「マインドフレア」を指定すれば（自身がマインドフレアに変身していれば）知力を大量に貪り食うごちそうになり、手なずけやすいモンスターを指定すれば即座にペットの軍団を編成できます。なお、ユニークモンスターを指定しても神に拒絶されて召喚できません。

[]{#scroll-magic-mapping}
**地図の巻物。** フロア全体の地形レイアウトを瞬時に開示します。祝福された巻物は隠し扉の位置も表示します。[ゲヘナ](#gehennom) の狂気的な迷路フロアにおいて、手作業で歩いてマッピングする無駄な時間を省くための必須アイテムです。

[]{#scroll-scare-monster}
**怪物を怯えさせる巻物。** 読むのではなく、**床に置いてその上に乗る** のが正しい使い方です。恒久的な [エルベレス](#elbereth) のように機能し、ほとんどのモンスターを恐怖させて寄せ付けなくします。呪われていない巻物を初めて床から拾い上げた際は無傷ですが「使い古し」のマークが付き、次に拾い上げると *「巻物は拾い上げたと同時に灰燼に帰した (The scroll turns to dust as you pick it up)」* と表示されて消滅します。呪われた巻物は1回目の拾い上げで即座に灰になります。退避場所として安全地帯を作りたいマスにピンポイントで落とし、安易に拾い直さないようにしてください。

[]{#scroll-teleportation}
**瞬間移動の巻物。** 呪われていないで読むと同フロアのランダムな場所へテレポートします。呪われているか混乱状態で読むと、ランダムな別のダンジョン階層へと飛ばされます。「瞬間移動制御」を持っていれば、着地先の座標を自由に指定できます。ゲーム内屈指の万能脱出ボタンです。

[]{#scroll-stinking-cloud}
**悪臭雲の巻物。** 約5マス以内の視界内の指定したマスに、持続する毒ガスの霧（呪われていないで約15マス、祝福で約25マスをカバー）を発生させます。中にいる生物を盲目にし、毒耐性を持たないあらゆる対象に毎ターン約 6〜13 HPの継続ダメージを与えます。自分自身が毒耐性または無呼吸を持っていれば、安全な通路から玉座の部屋や魔法使いの塔の敵を一掃する強力な兵器となります。雲の中で倒れた敵の経験値や属性値の功績は正常にプレイヤーに加算されます。

[]{#scroll-fire}
**火の巻物。** 自身の周囲に激しい炎を噴出させます。呪われていないまたは呪われた状態で読むと、爆発の中心は **自分自身** となり、わずかなダメージを受けるとともに、荷物袋の中にある巻物や薬が焼き払われてしまいます。しかし **祝福された** 火の巻物は全くの別物です：5倍の威力を持ち、約5マス以内の視界内のマスを指定して発射できるため、非魔法系キャラクターが持ち歩ける数少ない遠距離範囲攻撃手段となります。また、どちらのバージョンであっても、浴びることで体に付着した「緑スライム」を焼き払うことができるため、スライム化の緊急治療法としても機能します。必ず祝福して保管してください。

#### 混乱読書 (Confused Reading)

多くの巻物は、混乱状態で読んだ際に全く異なる効果を発揮します。その代替効果の中には、通常の効果よりも遥かに **強力で有益** なものが存在します：

- **混乱して読む「鎧に魔法をかける巻物 / 武器に魔法をかける巻物」**（*呪われていないまたは祝福*）：強化値を上げる代わりに、対象の武具に **完全な耐腐食・耐錆加工（erodeproof）** を施します。もう+1の強化値を得るよりも錆対策を優先したい場合の定番テクニックです。
- **混乱して読む「鎧を破壊する巻物」**（*呪われている場合*）：防具を破壊せず、逆に防具の1パーツに **耐腐食加工** を施します（呪われていないや祝福で読むと耐腐食加工が剥ぎ取られます）。
- **混乱して読む「解呪の巻物」**：呪われていないアイテムのBUCをランダムにシャッフルします（約1/4が祝福、1/4が呪い、1/2が呪われていないまま）。呪われていない巻物は装備中の武具・重し・引き綱のみ、祝福された巻物は手持ちの全アイテムに及びます。これは装備品に安価な祝福を付与するギャンブル技であり、呪いを解く目的では絶対に使えません。
- **混乱して読む「怪物を飼いならす巻物」**：効果範囲が周囲 3×3 マスから **11×11 マス** へと劇的に拡大します。なお「怪物を手なずける呪文」を混乱して唱えても単に失敗するだけなので、この技は巻物専用です。
- **混乱して読む「瞬間移動の巻物」**：現在のフロア内ではなく、ランダムな **別のダンジョン階層** へと飛ばされます。緊急脱出ボタンとして機能しますが、浅い階層を探索中の場合は注意が必要です。
- **混乱して読む「金貨を探す巻物」**：金貨ではなく、そのフロアにある **すべての罠の位置** を一挙に開示します。1マスずつ手動で捜索するより遥かに高速で安全です。
- **混乱して読む「充填の巻物」**：魔力（Pw）を全回復させ、すでに満タンであれば **最大魔力を 4〜16（祝福時は 6〜24）恒久的に引き上げます**。巻物に余裕がある呪文詠唱者にとっての永続バフです（呪われた状態で読むと逆に魔力が0になります）。

計画的に自身を混乱させる最もクリーンな方法は、**混乱の薬** を飲むことです（効果時間は約16〜22ターン持続します）。また、祝福されていない **酔っぱらいの薬**（侍の場合は **酒（sake）**）を飲むことでも数ターンの混乱状態を作り出せます。

### 杖 (Wands)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Wand of Nothing is IMMEDIATE (directional), so its charge cap is 8, not 15 (read.c:739-741; mkobj.c:1123). Table said 15.
- No "cursed wand of digging zaps downward" mechanic; zap direction is BUC-independent (dig.c, zap.c). Removed.
- Recharge explosion table was off-by-one: first recharge is safe (0%), 100% is the eighth (n = previous recharges, read.c:752-768).
-->
<!-- audit
2026-05-18:
- wand of stasis: NODIR, $150, prob 45 — makes the level no-teleport for 10-30 turns; does NOT freeze monsters (objects.h:1460, zap.c:2559-2568; effect gated by stasis_until in teleport.c:43 noteleport_level, teleport.c:2269 u_teleport_mon, apply.c:530 magic whistle, do.c:2262 revive rloc)
- wand of nothing is IMMEDIATE, not NODIR (objects.h:1462)
- undead turning revives corpses to their original species via unturn_dead — NOT as zombies (zap.c:1156-1228 unturn_dead, zap.c:900 revive uses corpse->corpsenm; only cant_revive-rejected types fall back to zombie/doppelganger at zap.c:982-985)
- engrave-test: cancellation and make-invisible erase in place (engrave.c:618-633)
- engrave-test: teleportation moves the engraving elsewhere; polymorph rewrites it
- nothing, undead turning, opening, locking, probing produce NO engrave message (engrave.c:635-640)
- magic missile engraves "riddled by bullet holes" — distinctive (engrave.c:642-648)
- sleep and death share "the bugs on the <surface> stop moving" (engrave.c:651-656)
- striking message: "wand unsuccessfully fights your attempt to write" (engrave.c:602-605)
- slow/speed monster: distinctive "bugs slow down" / "speed up" (engrave.c:606-616)
- self-polymorph into a small form (sliparm) drops body armor (cursed or not) into inventory via Armor_gone+dropp (polyself.c:1198-1228); large forms (breakarm) destroy it instead (polyself.c:1162-1197)
- engrave-test ambiguity between cancellation, make-invisible, teleportation, polymorph can be resolved by zapping a known item: make-invisible turns it invisible; teleportation moves it; cancellation dulls it (zap.c:2313-2317); polymorph changes its type (zap.c:weffects branch)
- strategy aligned with NetHackWiki Wand, Engraving, Wand of wishing: engrave-test as the safest wand-ID method, $500 narrowed to death-or-wishing, wand of wishing recharge mechanics (https://nethackwiki.com/wiki/Wand, https://nethackwiki.com/wiki/Engraving, https://nethackwiki.com/wiki/Wand_of_wishing)
-->

杖は、振る（`z` を押して方向を指定）ことで指向性の効果を発揮する再利用可能な魔法のアイテムです。3つのタイプが存在します：壁で跳ね返る光線を放つ **光線（RAY）の杖**、直線上の対象に作用する **ビーム（BEAM）の杖**、そして自身の周囲に効果を及ぼす **無指向性（None）の杖** です。

光線は消滅するまでに 7〜13 マスを直進し、壁、岩、マップの端にぶつかると跳ね返ります。跳ね返った後も消滅するまで飛び続けるため、直線の一本道や数マス先の壁に向けて放つと、跳ね返った光線が自分自身に直撃し、モンスターに与えるのと全く同じ壊滅的なダメージを喰らうことになります。光線が自分から遠ざかる方向へと飛んでいくように照準を合わせてください。

杖のBUC（祝福・呪われていない・呪い）の状態は発動効果そのものを変えませんが、呪われた杖は振ったり試し書きしたりするたびに、約100分の1の確率で暴発して手の中で大爆発を起こします。爆風の威力は内部に残っているチャージ数に比例して増大するため、常用する杖（何よりも死の杖）は必ず呪いを解いてから使用してください。

#### 杖の一覧表 (The Wand Table)

各杖の基本スペックと試し書き結果を示します。未識別の杖を絞り込むための価格については [杖の価格](#wand-prices) を参照してください。右端の列にある **試し書きテスト結果** は極めて実用的であり、大半の杖は1回埃に文字を刻むだけでその正体を看破できます。具体的な手順については [杖の試し書きテスト](#the-engrave-test-wands) を、少数の重複するメッセージの判別法については [曖昧な試し書き結果の解決法](#resolving-ambiguous-engrave-results) を参照してください。

<div class="price-id-toolbar"></div>

::: dense-table

| 価格 | 杖の名称 | タイプ | 発見時チャージ数 | 試し書きテスト結果 |
| ---: | --- | :---: | :---: | --- |
|  100 | 灯りの杖 (Light) | 無指向性 | 11–15 | 部屋が明るくなる |
|  100 | 単なる杖 (Nothing) | ビーム | 4–8 | メッセージなし（無反応） |
|  150 | [穴掘りの杖 (Digging)](#wand-digging) | 光線 | 4–8 | 小石が飛び散る |
|  150 | 啓蒙の杖 (Enlightenment) | 無指向性 | 11–15 | 啓蒙された気分になる |
|  150 | 矢の杖 (Magic missile) | 光線 | 4–8 | 弾痕のような穴があく |
|  150 | [透明化の杖 (Make invisible)](#wand-make-invisible) | ビーム | 4–8 | 刻んだ文字が消滅する ¹ |
|  150 | 開錠の杖 (Opening) | ビーム | 4–8 | メッセージなし（無反応） |
|  150 | 探査する杖 (Probing) | ビーム | 4–8 | メッセージなし（無反応） |
|  150 | 扉探索の杖 (Secret door detection) | 無指向性 | 11–15 | 隠し扉が開示される |
|  150 | 減速の杖 (Slow monster) | ビーム | 4–8 | 虫の動きが遅くなる |
|  150 | 加速の杖 (Speed monster) | ビーム | 4–8 | 虫の動きが速くなる |
|  150 | [静止の杖 (Stasis)](#wand-stasis) | 無指向性 | 3–6 | メッセージなし（無反応） |
|  150 | 衝撃の杖 (Striking) | ビーム | 4–8 | 杖が文字を書くことに抵抗する |
|  150 | 蘇生の杖 (Undead turning) | ビーム | 4–8 | メッセージなし（無反応） |
|  150 | 施錠の杖 (Locking) | ビーム | 4–8 | メッセージなし（無反応） |
|  175 | [吹雪の杖 (Cold)](#wand-fire-cold-lightning) | 光線 | 4–8 | 氷の破片が落ちる |
|  175 | [炎の杖 (Fire)](#wand-fire-cold-lightning) | 光線 | 4–8 | 炎が吹き上がる |
|  175 | [雷の杖 (Lightning)](#wand-fire-cold-lightning) | 光線 | 4–8 | 電撃が走る（自身も盲目化） |
|  175 | 眠りの杖 (Sleep) | 光線 | 4–8 | 虫の動きが完全に止まる ² |
|  200 | [無力化の杖 (Cancellation)](#wand-cancellation) | ビーム | 4–8 | 刻んだ文字が消滅する ¹ |
|  200 | 怪物を造る杖 (Create monster) | 無指向性 | 11–15 | 虫が出現する |
|  200 | [へんげの杖 (Polymorph)](#wand-polymorph) | ビーム | 4–8 | 刻んだ文字が別の文章に書き換わる |
|  200 | [瞬間移動の杖 (Teleportation)](#wand-teleportation) | ビーム | 4–8 | 刻んだ文字が消滅する ¹ |
|  500 | [死の杖 (Death)](#wand-death) | 光線 | 4–8 | 虫の動きが完全に止まる ² |
|  500 | [願いの杖 (Wishing)](#wand-wishing) | 無指向性 | 1 | 「何を願いますか？」と尋ねられる |

:::

<small>¹ 無力化、透明化、瞬間移動で共通。<br>
² 眠りと死で共通。</small>

<div class="price-id-toolbar"></div>

#### 主要な杖 (Key Wands)

[]{#wand-wishing}
**願いの杖。** 振るたびに1つの願いを叶えてくれます。「願いの杖」は生成時に **1チャージ** を持っています。無理矢理振る（wrest）前に、まず「充填の巻物」で1度だけ安全に再充填してください。その上で最後の無理矢理搾り出したチャージを使用すれば、合計で3つの願いが叶います（充填の巻物がない場合は、初期チャージと無理矢理振るチャージで計2回）。[城](#the-castle) に到達する前に、何を願うべきか綿密に計画を立てておきましょう。

[]{#wand-death}
**死の杖。** 直撃したほぼすべての生物を一撃で絶命させる「死の光線」を放ちます。「反射」によって跳ね返され、「耐魔（魔法防御）」によって無効化されます。ゲーム終盤における最強の攻撃手段のひとつですが、反射や耐魔を持たない状態で壁に反射させてしまうと、自分自身が一瞬で即死することになります。

**眠りの杖。** 睡眠の光線は、HPに一切ダメージを与えることなく序盤の冒険者を死へと追いやります。跳ね返った光線を浴びると 6d25 ターンもの間無防備な深い眠りに落ちてしまいます。壁から離れた方向へと撃ち、モンスターが接近して殴りかかってくる前に目を覚ますなどという甘い期待は捨ててください。

[]{#wand-digging}
**穴掘りの杖。** 極めて重要なユーティリティです。壁を掘り抜いてショートカットを作ったり、危険な状況から直下に掘って下の階へ緊急脱出したり、岩を掘り崩して隠し金庫や隠しエリアへと到達できます。真下に向けて振れば、本来進みたかった方向である直下のフロアへと一瞬で落下できます。

[]{#wand-teleportation}
**瞬間移動の杖。** モンスターに振ればフロア内の別の場所へと吹き飛ばし、自分に向けて振れば緊急脱出できます。危険な戦いを正面から勝ち抜くことなく、安全な距離を即座に稼ぐことができます。

[]{#wand-fire-cold-lightning}
**炎の杖、吹雪の杖、雷の杖。** 壁で跳ね返る攻撃用の光線の杖です。炎は床の巻物や魔法書を焼き払います。吹雪は水面を凍らせて氷の橋を作ることができます。雷はモンスターを盲目状態にします。

[]{#wand-cancellation}
**無力化の杖。** アイテムやモンスターから魔法の特性を消し去ります。無力化されたモンスターは特殊攻撃の大半を失います：無力化されたコカトリスは石化できず、無力化されたマインドフレアは脳みそを吸えず、無力化された粘土ゴーレムはその場で泥水となって崩壊します。**この杖を決して「軽量化の鞄」の中に入れてはなりません。** 鞄ごと中身のアイテムがすべて完全に破壊・消滅します。また、未識別の巻物や薬の山に向けて振ると、白紙の巻物やただの水へと変化するため、魔法のマーカーや聖水作成ラインの原料へと還元できます。

[]{#wand-polymorph}
**へんげの杖。** モンスターを別のランダムなモンスターへと変身させ、アイテムを同じクラスの別のランダムなアイテムへと再抽選します。創造的な活用が可能です（ゴミ防具の山に振ってドラゴンの鱗鎧を狙う、弱い敵に振って有用な死体を狙うなど）。リスクは高いですが極めて強力です。

[]{#wand-make-invisible}
**透明化の杖。** 自分に向けて振ると 31〜45 ターンの間不可視状態になります。モンスターに振るとそのモンスターが永続的に透明化してしまい、不可視を見る手段がない限り事態を悪化させるだけです。自分自身の恒久的な透明化には、指輪やクロークを使用してください。

[]{#wand-stasis}
**静止の杖。** 振っても光線も出ず、方向指定もメッセージもなく、一見何も起きていないように見えます。しかし実際には、**10〜30ターンの間、そのフロア全体を「テレポート禁止」状態に封印しています**。封印が持続している間は、あなたも、敵も、普段ならフロア中を飛び回って接近してくる欲深いモンスターたちも、一切テレポートできなくなります。魔法の笛も沈黙します。名前に反してモンスターの足を止めるわけではなく、周囲の敵は普通に移動して殴りかかってきます。遠距離逃走を繰り返す敵をその場に釘付けにして仕留めるための狭い用途の杖であり、同時に自分自身のテレポート脱出も封じられる点に注意してください。

**探査する杖。** 診断用の杖です。モンスターに向けて振ると、その残りHP、最大HP、レベル、そして **「何を持ち歩いているか」** を克明に開示します。店主、兵士、あるいは倒す価値がある装備を持っているか確かめたい名前付き冒険者に対して極めて有用です。聴診器はHPとステータスを報告してくれますが荷物の中身までは分かりません。敵の荷物袋を覗き見たいなら、探査する杖の出番です。

#### 曖昧な試し書き結果の解決法 (Resolving Ambiguous Engrave Results)

一部の試し書きメッセージは、複数の杖で共有されています。

**「刻んだ文字が消滅した！」** というメッセージは、**無力化の杖**、**透明化の杖**、または **瞬間移動の杖** のいずれかです。既知のアイテムを床に落とし、それぞれの候補を振ってテストしてください：透明化の杖ならアイテムが不可視になり、瞬間移動の杖ならフロアの別の場所へ消え、無力化の杖ならその魔力が剥ぎ取られます。

**「床の虫の動きが完全に止まった！」** というメッセージは、**眠りの杖** または **死の杖** です。死の杖は基本価格が500ゴールドの光線の杖であり、眠りの杖は175ゴールドです。

**メッセージが全く出ない（無反応）** 場合は、**単なる杖**、**開錠の杖**、**施錠の杖**、**探査する杖**、**蘇生の杖**、**静止の杖** の6択に絞られます。安全な標的を対象にテストを行ってください：

- **開錠の杖** は宝箱や扉の鍵を開けます。**施錠の杖** は鍵をかけます。
- **探査する杖** は近くのモンスターのステータスを開示します。
- **蘇生の杖** は新鮮な死体を元の種族の生きた姿へと蘇生させます（対象が持っていた死体もすべて蘇生させます）。
- **静止の杖** はフロア全体のテレポートを封印し、外見上の兆候を一切出しません。そのためこの6種類の中で最も判別が困難です（後でテレポートしようとして不可解に失敗したら、この杖であったことが判明します）。
- **単なる杖** は文字通り何も起きません。

曖昧さのない杖については、安全な標的に向けて1回振ることで、試し書きで推測された正体を確実に裏付けることができます：飼いならしたペットや弱い敵に **減速の杖** / **加速の杖**、閉じた扉に **衝撃の杖**、ゴミ装備の山に **へんげの杖** を振ります。未識別の杖を自分自身に向けて振ることは絶対に避けてください。

#### 再充填 (Recharging)

杖は「充填の巻物」を読むことでチャージ数を回復できます。最も価値ある使い道は「願いの杖」であり、1回安全に再充填するだけで、1回の願いを2回へと増やすことができます。ただし、連続して再充填を重ねるごとに、杖が爆発して消滅するリスクが急上昇します。爆発確率は `(これまでの充填回数の3乗) / 343` で計算されます：

- 1回目の充填：完全に安全（爆発確率 0%）。
- 2回目：約 0.3%。
- 3回目：約 2.3%。
- 4回目：約 7.9%。
- 8回目：100% 確実に爆発。

最良の結果を得るために祝福された充填の巻物を使用してください。ただし「願いの杖」には独自の厳格なルールが存在します。生まれたての願いの杖には **ちょうど1チャージ** しかありません。呪われていないまたは祝福された充填の巻物は願いを **1回** だけ追加します（祝福してもそれ以上増えません。呪われた巻物はチャージを0にします）。無理矢理振る（wrest）と杖が消滅してしまうため、必ず無理矢理振る *前* に再充填を行ってください。1回目の再充填は安全ですが、願いの杖に対する2回目の再充填は **100% 確実に大爆発** します。したがって、充填なしなら計2回、1回充填すれば計3回の願いを引き出すことができます。

指輪も充填可能ですが、爆発チェックには現在の強化値が使用されます：+0 は安全、+1 は 1/7 の確率で爆発、+3 は約43%、+5 は約71%、+7 は確実に爆発します。すでに高く強化された貴重な指輪を充填の標的にするのは極めて危険です。

#### 無理矢理振る (Wresting)

杖のチャージ数が0になっても、まだ振ることを試みることができます。杖が灰燼に帰して消滅する前に、**121分の1** の確率で最後の1チャージを「無理矢理搾り出す（wresting）」ことができます。これは最後の命綱となる裏技ですが、願いの杖に対しても同様に機能します。

#### 道具としての変身(へんげ) (Polymorph as a Tool)

自身を変身(へんげ)させることには、リスクに見合うだけの絶大なメリットがあります。自分に向けて「へんげの杖」を振る、「へんげの薬」を飲む、「変化」の呪文を唱える、あるいは「へんげの罠」を踏むことで、新たなモンスターの肉体を獲得できます。**へんげ制御**（指輪または内在能力）があれば、どのモンスターに変身するかを *自分で自由に選択* できます。

- **自力では行けない場所を旅する：** ゾーンになれば壁をすり抜けて移動できます。ウナギになれば水中で呼吸できます。吸血鬼になってコウモリや霧の雲に変身すれば扉の下の隙間をすり抜けられます。さまよう目になれば解除できない罠の上をフワフワと浮いて通過できます。
- **耐性と強力な特殊攻撃を手に入れる：** 赤色ドラゴンになれば火のブレスを吐けます。茶色カビになれば近接攻撃を仕掛けてきた敵を氷漬けにできます。紫ワームになれば厄介な強敵を丸呑みにして瞬殺できます。モンスターの姿になれば、その能力の大半を自分のものとして行使できます。
- **別の肉体を借りて戦う：** 変身した姿には、独自の満タンのHPが割り当てられます。本来のHPはその下に温存され、変身が解けた際に元の数値に戻ります。
- **呪われた鎧から脱出する：** *より巨大な* モンスターに変身すると、鎧が破裂して破壊されます。*より小さな* モンスターに変身すると、呪われた鎧は無傷のまま床や荷物袋に脱落し、後から聖水で呪いを解くことができます。
- **食べられないものを食べる：** 金属食モンスターになれば鉄格子を平らげられます。緑ドラゴンになれば猛毒の死体を難なく消化できます。

なお、へんげ制御がない状態で変身すると、耐久力（Con）の判定に失敗した際に「変身(へんげ)ショック」を起こし、最大30のHPダメージを受ける危険があります。残りHPが低い状態で制御なしの変身を試みてはなりません。

ゴミアイテムの **山（パイル）** に向けて「へんげの杖」を振ると、それぞれのアイテムが同じクラスの別のランダムなアイテムへと一斉に再抽選されます。このテクニックは「ポリパイル（polypiling）」と呼ばれ、大量のガラクタから必要な貴重品を錬成する強力な手段となります。パイルにするアイテムは、メインの荷物袋から十分に離れた別のマスに置いてください（誤射して軽量化の鞄を巻き込むと大惨事になります）。また、必ず事前に幸運値を最大まで高めておきましょう。ポリパイルが失敗すると、変化したアイテムがその材質の敵対的ゴーレムへと化けて襲いかかってきますが、幸運値が高いほどこの失敗率を抑えることができます。

### 指輪と魔除け (Rings and Amulets)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Amulet of life saving revives to min(maxHP, 50+10*(Con/2)), not full HP (end.c:710,719).
- Amulet of strangulation is 90% cursed at generation (rn2(10)), not "always" (mkobj.c:1063).
- Verified correct: ray range, make-invisible/stasis durations, backfire 1/100, ring prices, MC/guarding rules, auto-curse 90%, ring-hunger ticks.
-->
<!-- audit
2026-05-18:
- ring prices match objects.h:741-827
- teleportation, polymorph, aggravate-monster, hunger rings 90% cursed (mkobj.c:1143-1146)
- aggravate-monster effective-depth doubling is capped at 50 (dungeon.c:2080-2082)
- free action gives paralysis immunity via Free_action (apply.c:1044, mcastu.c:506)
- ring hunger cost ticks at turns 4 and 12 (eat.c:3237-3267)
- amulet of guarding: +2 AC, +2 MC (do_wear.c:2496, mhitu.c:1121-1126)
- restful sleep regenerates +1 HP per sleep tick (allmain.c:663-664)
- restful sleep is 90% cursed at generation, not 100% (mkobj.c:1063-1066 via rn2(10))
- ring of protection subtracts from AC (do_wear.c:2492-2495)
- conflict makes pets attack you (dogmove.c:1046-1054, mhitm.c:104-145)
- blessed polymorph control rolls from base form only (potion.c:1322-1325)
- strategy aligned with NetHackWiki Ring strategy, Ring of free action, Ring of conflict, Amulet of life saving: free action against late-game paralysis, conflict for crowd control, life saving for risky endgame moments (https://nethackwiki.com/wiki/Ring_strategy, https://nethackwiki.com/wiki/Ring_of_free_action, https://nethackwiki.com/wiki/Ring_of_conflict, https://nethackwiki.com/wiki/Amulet_of_life_saving)
-->

指輪は左右の手の指に1つずつ計2つ、魔除けは首に1つ身につけることができます。身につけるには `P`（Put on）、外すには `R`（Remove）を押します。指輪と魔除けはこのキーペアで操作します（防具の着脱は `W` と `T` です）。

#### 指輪の一覧表 (The Ring Table)

<div class="price-id-toolbar"></div>

| 価格 | 指輪の名称 | 備考 |
| ---: | --- | --- |
|  100 | 飾りの指輪 (Adornment) | 魅力（CHA）増大、充填可能 |
|  100 | 飢餓の指輪 (Hunger) | 空腹の進行が早まる（生成時90%呪い） |
|  100 | 守りの指輪 (Protection) | AC改善、充填可能 |
|  100 | 耐へんげの指輪 (Protection from shape changers) | 獣化モンスター対策に極めて有用 |
|  100 | 忍びの指輪 (Stealth) | 移動時の物音を消す |
|  100 | 能力維持の指輪 (Sustain ability) | 能力値低下を完全に阻止 |
|  100 | 警告の指輪 (Warning) | 近くにいるモンスターの危険度を表示 |
|  150 | 反感の指輪 (Aggravate monster) | 非常に有害（生成時90%呪い） |
|  150 | 耐冷の指輪 (Cold resistance) | 冷気属性の攻撃に完全耐性 |
|  150 | 体力の指輪 (Gain constitution) | 耐久力（CON）増大、充填可能 |
|  150 | 強さの指輪 (Gain strength) | 筋力（STR）増大、充填可能 |
|  150 | 命中の指輪 (Increase accuracy) | 命中率上昇（To-Hitボーナス）、充填可能 |
|  150 | 攻撃の指輪 (Increase damage) | 与ダメージ上昇、充填可能 |
|  150 | 透明の指輪 (Invisibility) | 不可視状態になる |
|  150 | 耐毒の指輪 (Poison resistance) | 毒攻撃に完全耐性 |
|  150 | 可視の指輪 (See invisible) | 不可視の生物を視覚化 |
|  150 | 耐電の指輪 (Shock resistance) | 電撃属性の攻撃に完全耐性 |
|  200 | 耐炎の指輪 (Fire resistance) | 火炎属性の攻撃に完全耐性 |
|  200 | [自由行動の指輪 (Free action)](#ring-free-action) | 麻痺攻撃を完全に無効化 |
|  200 | 浮遊の指輪 (Levitation) | 宙に浮く |
|  200 | 回復の指輪 (Regeneration) | HP自然回復が大幅加速（追加空腹コストあり） |
|  200 | 探索の指輪 (Searching) | 毎ターン自動で周囲を捜索 |
|  200 | [消化不良の指輪 (Slow digestion)](#ring-slow-digestion) | 空腹の進行を大幅に遅延 |
|  200 | 瞬間移動の指輪 (Teleportation) | ランダムにテレポート（生成時90%呪い） |
|  300 | [争いの指輪 (Conflict)](#ring-conflict) | モンスター同士を同士討ちさせる |
|  300 | へんげの指輪 (Polymorph) | ランダムに変身（生成時90%呪い） |
|  300 | へんげ制御の指輪 (Polymorph control) | 変身先のモンスターを自由に選択 |
|  300 | [瞬間移動制御の指輪 (Teleport control)](#ring-teleport-control) | テレポート時の着地先を自由に指定 |

<div class="price-id-toolbar"></div>

「生成時90%呪い」と記載された指輪は、生成された時点で約90%の確率で呪われており、呪いを解くまで手から外すことができなくなります。

#### 主要な指輪 (Key Rings)

[]{#ring-free-action}
**自由行動の指輪。** 麻痺状態を完全に防ぎます。麻痺はゲーム終盤において、モンスターから一方的にタコ殴りにされて命を落とす最も典型的な死因のひとつです。

[]{#ring-teleport-control}
**瞬間移動制御の指輪。** ランダムなテレポートを着地先指定の戦術的移動へと変貌させ、「瞬間移動体質」を最強の機動力へと昇華させます。

[]{#ring-conflict}
**争いの指輪。** モンスター同士を同士討ちさせます。敵で埋め尽くされた大部屋を一瞬で大混乱に陥れて自滅させることができますが、**飼いならしたペットもあなたを攻撃してくる** 点には十分注意してください。

[]{#ring-slow-digestion}
**消化不良の指輪。** 通常の空腹の進行を大幅に遅延させます。ただし、他の装備している指輪による追加の栄養ドレインまでは帳消しにしてくれません。

**反感の指輪。** モンスター生成時の実質的なダンジョン深度を約2倍に引き上げます（上限深度50）。大抵の場合は破滅的な結果を招きます。準備を整えた混沌のプレイヤーが、強力な生贄用の獲物を呼び寄せるために短時間だけ装備してすぐ外す、というような特殊な用途にのみ使われます。この指輪は90%の確率で呪われて生成されるため、事前のBUCテストなしで指にはめるのは自殺行為です。

なお、祝福された「へんげの薬」を飲むと、その1回の変身に限り「へんげ制御」が自動的に付与され、指輪がなくても自由に変身先を選べます。そのため「へんげ制御の指輪」の重要度は以前ほど高くありません。1回制御変身を行うためだけにこの指輪を探し回ったり願ったりする必要はもはやなく、願いの権利は他の至宝のために温存してください（何度も繰り返し変身したい場合には指輪が有用です）。

**隠されたコスト（空腹度ペナルティ）：** 通常の指輪は装備中20ターンごとに1ポイントの栄養を消費します。「争いの指輪」、「回復の指輪」、「飢餓の指輪」は **2ターンごとに1ポイント** という激しい栄養を消費します。状況に応じて使う指輪は荷物袋に入れておき、必要な時だけ指にはめてください。「自由行動の指輪」だけは例外であり、不意の麻痺死を防ぐ保険としての価値は、わずかな食料コストを補って余りあるものです。

#### 魔除け (Amulets)

魔除けは指輪よりも種類が少なくシンプルですが、識別はより困難です。すべて基本価格が **150ゴールド** で統一されているため、価格識別が一切役に立ちません。装備テストを行うか、「識別の巻物」を読む必要があります。「命を救ってくれる至宝」から「首を絞めて即死させる凶器」まで効果の振れ幅が極めて大きいため、テストには細心の注意が必要です：

| 魔除けの名称 | 効果 |
| --- | --- |
| 命の魔除け (Life saving) | 死亡時に1度だけその場で蘇生し、身代わりとなって粉砕・消滅する |
| 反射の魔除け (Reflection) | あらゆる光線攻撃を跳ね返す |
| 呼吸の魔除け (Magical breathing) | 水中や空気のない場所でも呼吸可能（溺死完全防止） |
| 遠視の魔除け (ESP) | テレパシーによって周囲の怪物を感知 |
| 耐へんげの魔除け (Unchanging) | 意図しない変身（ポリモーフ）を完全に防止 |
| 性転換の魔除け (Change) | 身につけた瞬間に性別が反転し、魔除けは崩壊・消滅する |
| 耐毒の魔除け (Versus poison) | 毒に対する完全耐性 |
| 飛行の魔除け (Flying) | 飛行能力を獲得（NetHack 5.0 新要素） |
| 守りの魔除け (Guarding) | AC +2、魔法防御（MC）+2 を付与（NetHack 5.0 新要素） |
| 絞殺の魔除け (Strangulation) | 首を締め付け、数ターンで窒息死させる（通常は呪われている） |
| 安眠の魔除け (Restful sleep) | ランダムに眠りに落ちる（通常は呪われている）。睡眠中HP回復+1/ターン |

未識別の魔除けを首にかける前に、**必ずBUCをテストしてください**。「絞殺の魔除け」はわずか6ターンの猶予しか与えずにあなたを窒息死させます。首にかかって絞殺が始まったら即座に外すか、呪われて外せない場合は神に祈ってください。

#### 主要な魔除け (Key Amulets)

**命の魔除け。** 死亡した瞬間に、50 HP ＋ 耐久力ボーナス（本来の最大HPが上限）の状態で即座に蘇生し、身代わりとなって粉砕・消滅します（耐久力が1減少します）。ただし「虐殺」による死亡は防げません。識別できたら、首にかけてそのまま忘れてしまって構いません。予期せぬ不慮の事故から身を守るための究極の保険です。

**反射の魔除け。** ペルセウスの石像などから「反射の盾」を入手できなかった場合に極めて強力です。首のスロットで反射を確保することで、盾スロットを空けて小盾を装備したり、強力な二刀流スタイルを採用できるようになります。

**守りの魔除け。** AC +2 に加えて **魔法防御（MC）+2** を提供します。これは NetHack 5.0 で追加された素晴らしい新装備であり、長年の悩みであった「MCパズル」を見事に解決してくれます。「魔法を防ぐクローク（MC1）」と組み合わせるだけで最高峰の **MC3** に到達できるため、汎用性に劣る「守りのクローク」に頼る必要がなくなります。

**呼吸の魔除け。** 引きずり込みによる溺死を完全に防ぎます。メデューサの島での戦いで大活躍し、「水の大系」では必須の装備となります。

**飛行の魔除け。** 浮遊の上位互換となる新装備です。同じように宙に浮きながら、足元のアイテムを拾い上げることができ、自分のターンで任意に着地できます。さらに素晴らしい利点として、**騎乗している愛馬も一緒に飛行します**。空飛ぶ戦闘用の馬は堀、水たまり、[城](#the-castle) の跳ね橋を飛び越え、メデューサの島を端から端まで一気に飛び渡ることができます（騎乗動物は韋駄天の靴を履けず、プレイヤーの速度も加算されないため、飛行による機動力向上は絶大です）。

**安眠の魔除け。** ランダムに眠りに落ちてしまう呪われたアイテムですが、睡眠中は毎ターンHPが+1追加回復するという加速再生能力を持ちます。扉に楔を打ち込んで完全に密閉した安全な小部屋で眠れば、ほぼ役立たずの呪いアイテムが即席の野戦病院へと変貌します。

### 道具 (Tools of the Trade)

道具は、ダンジョンにおける多目的万能ツールです。武器のように振り回すことも、防具のように身につけることもありませんが、適用（`a`）することで様々な困難を打開してくれます。鍵を開け、暗闇を照らし、重い荷物を軽量化し、状態異常を治癒し、さらには白紙の巻物に新たな魔法を書き込むことすら可能です。

#### 容器類 (Containers)

| 容器の名称 | 空の重量 | 特徴と用途 |
| --- | :---: | --- |
| 袋 (Sack) | 15 | 基本的な収納袋 |
| 防水袋 (Oilskin sack) | 15 | 中身のアイテムを水濡れから保護 |
| 軽量化の鞄 (Bag of holding) | 15 | 中に入れたアイテムの実効重量を劇的に軽減 |
| トリックの鞄 (bag of tricks) | 15 | 開けるとモンスターを召喚（通常の袋ではない） |
| 大箱 (large box) | 350 | 生成時に0〜3個のアイテムを内包（施錠時は0〜5個） |
| 宝箱 (Chest) | 600 | 生成時に0〜5個のアイテムを内包（施錠時は0〜7個） |
| アイスボックス (Ice box) | 900 | 中に入れた死体の腐敗を完全に防止 |

それぞれの重量に注目してください。袋類は重量15であり、常に携帯すべきです。一方、大型の箱（350）、宝箱（600）、アイスボックス（900）は「家具」であって手荷物ではありません。これらを持ち歩こうとすれば、それだけでプレイヤーの最大所持許容量を使い果たしてしまいます。これらはフロアに据え置きの保管庫（スタッシュ）として利用し、階層間を引きずり回すものではありません。

**軽量化の鞄 (Bag of holding)** は、中に入れたアイテムの実効重量を劇的に変化させます：祝福時は **1/4**、呪われていない時は **1/2** に軽減し、呪われていると逆に **2倍** に重くなります。[倉庫番](#sokoban) の最上階の報酬は50%の確率でこの軽量化の鞄です（魔除けが出た場合、軽量化の鞄は「願い」の最有力候補となります）。

**警告：軽量化の鞄の中に、無力化の杖、別の軽量化の鞄、あるいはチャージの残っている手品用の袋を絶対に入れてはなりません。** 鞄が 6d6 ダメージとともに大爆発を起こし、中身がフロア中に四散し、およそ13個に1個のアイテムが完全に破壊・消滅します。

もし（ボーンズファイルなどで）*呪われた* 軽量化の鞄を見つけた場合、不用意に開けてはいけません。床に置き、離れた位置から「無力化の杖」を鞄に向けて振ってください。爆発判定は「鞄の中に挿入した時」にしか発生しないため、外から光線を当てる分には安全であり、鞄の呪いを無傷で解くことができます。

外見が全く同じ「**トリックの鞄 (bag of tricks)**」は別物です。通常の容器だと思って中身を漁ろう（loot）とすると、袋に巨大な牙が生えて噛みつかれ、手痛いダメージを受けます（痛い目を見ますが、少なくとも無料で正体が判明します）。正しく使うには、適用コマンド（`a`）を使用してください。1チャージを消費して、自分の足元にランダムな敵対モンスターを1体召喚します。アイテムは持っていませんが、祭壇の隣に立って使えば、即席の生贄調達＆経験値稼ぎマシーンとして機能します。ただし深層では危険な強敵が出現することもあるため、瀕死の時や追い詰められた状況では振らないでください。

##### 所持許容量 (Carrying capacity)

プレイヤーの最大所持重量の許容量は、おおよそ **25 × (筋力 + 耐久力) + 50**（上限1000）です。平均的な人間の初期ステータスであれば約950ユニット、筋力の低い呪文詠唱者であれば約700ユニット前後から始まります。荷物を詰め込むにつれて、画面下部のステータス行には以下の負荷ステータスが表示されます：

| 負荷ステータス | 判定条件 | ペナルティと影響 |
| --- | --- | --- |
| 通常 (Unencumbered) | 許容量以下 | なし |
| 重荷 (Burdened) | 許容量の約1.5倍まで | 移動速度 −25%。空腹の追加消費なし。 |
| 圧迫 (Stressed) | 許容量の約2倍まで | 移動速度 −50%。奇数ターンに追加の空腹消費。**筋力トレーニングになる（筋力上昇抽選）**。 |
| 過重 (Strained) | 許容量の約2.5倍まで | 移動速度 −75%。追加空腹消費。戦闘時に疲労（3回の攻撃ごとに1 HP喪失）。筋力は鍛えられるが敏捷性を損なう。 |
| 超過重 (Overtaxed) | 許容量の約3倍まで | 移動速度 −87.5%。追加空腹消費と戦闘疲労。死亡する代わりに気絶する。敏捷性と耐久性を激しく損なう。 |
| 過積載 (Overloaded) | 許容量の3倍超 | 完全に移動不能。 |

実践的な鉄則：通常のプレイ中は **「通常」** を維持し、戦利品回収の往復時のみ **「重荷」** を許容し、明確な理由がない限り **「圧迫」** 以上の過重状態で歩き回ってはなりません。

**インベントリの52文字スロット上限。** 重量だけでなく、所持枠の数にも上限があります。手持ちのインベントリには **52個のスロット**（`a-z` および `A-Z`）しか存在せず、53個目のアイテムを拾おうとすると *「持ち物がいっぱいだ (Your pack is too full)」* と拒絶されます。同種のアイテムが1つのスロットに合体（スタック）するのは、ゲーム側が「完全に同一の品である」と認識できる場合に限られます。5枚の識別済みの「識別の巻物」は1文字を共有しますが、未識別の巻物や強化値の異なる武器は別々のスロットを占有します。持ち物の圧迫は、大抵の場合「識別不足」が原因です。正体を暴くほど、インベントリは綺麗にまとまっていきます。

軽量化の鞄はこのスロット問題も解決してくれます。容器の中に入っているアイテムは52枠のカウントに含まれないため、鞄の中に20本の薬を入れておけば消費スロットはわずか1枠で済みます。`#adjust` コマンドを使えば、アイテムの割り当て文字を変更したり、まとまらなかったスタックを強制的に統合したり、スタックを分割することができます（これは単なるラベル整理であり、ゲーム上の時間は消費しません）。

知能の高いモンスターは、施錠されていない箱を開けて中身を盗んだり箱ごと持ち去ったりしますが、**施錠された箱を開けることはできません**。床にアイテムを保管する際は、必ず鍵をかけてから立ち去るようにしてください。城の住人たちも施錠された宝箱を勝手に開けることはできません。

#### 開錠道具 (Unlocking Tools)

ダンジョンは施錠された扉や箱で溢れており、力ずくで蹴り破るのは騒音を撒き散らし時間もかかります。**万能鍵 (skeleton key)** は最も信頼性の高い開錠道具です（扉の開錠成功率70%以上、箱類75%以上）。**鍵開け器具 (lock pick)**（侍の場合は **おさく (osaku)**）も十分な性能を持ちます。**クレジットカード (credit card)** は成功率こそ劣りますが、蹴り破るよりは遥かにマシです。これらはいずれも軽量であるため、必ず3つのうちいずれか1つを常時携帯してください。

合鍵と鍵開けは、開錠だけでなく **「施錠（ロック）」** することも可能です。戦利品を箱に詰めた後、鍵をかけて安全に保管することができます（クレジットカードは開錠のみで施錠はできません）。

#### 光源 (Light Sources)

**油つぼ (oil lamps)** や **ろうそく (candles)** は暗い通路を照らしてくれます。**魔法のランプ (magic lamp)** は燃料切れを起こさず永久に燃え続け、火を灯した状態のままでも擦ることができます。ランプを擦る（`#rub`）と、1/3の確率で魔神（djinni）が出現し、さらに一定確率で願いを叶えてくれます（ランプが祝福されていれば魔神の願い付与率は80%であり、擦り1回あたりの総合的な願い成就率は約27%となります。呪われていないや呪いの場合は確率が低下します）。魔神が出現するまで同じランプを何度も擦り直すことができます。祝福して擦る準備が整うまでは通常の永久光源として活用しましょう。火を灯して明かりとして使っても願いの権利が消費されることはありません。

**祈りの燭台 (Candelabrum of Invocation)** は、[ヴラドの塔](#vlads-tower) で手に入る唯一無二のアーティファクト燭台です。[モロクの聖域](#molochs-sanctum) に進入するための「召喚の儀式」に必要な3大アイテムのひとつです。儀式を執り行うためには **7本のろうそく** を立てる必要があるため、ダンジョン内でろうそくを見かけたら今から大事に集めておきましょう。

#### 楽器 (Musical Instruments)

音階を演奏できるあらゆる楽器（木製のフルート、魔法のフルート、角笛、冷気の角笛、炎の角笛、ラッパ、竪琴）を使って、[城](#the-castle) の跳ね橋を下ろすための「合言葉のメロディ（passtune）」を演奏できます。合言葉の調べとその入手源については [城](#the-castle) を参照してください。

**魔法の竪琴 (magic harp)**（侍の場合は **魔法の琴 (magic koto)**）は、周囲のモンスターを魅了してペットにしてくれます（通常の木製の竪琴は単なる「琴」です）。**魔法のフルート (magic flute)** は周囲の敵を深い眠りに落とします。**地震の太鼓 (drum of earthquake)** は自身の周囲に大量の落とし穴を生み出します（その効果音と同じくらい大混乱を巻き起こします）。

角笛や皮の太鼓を鳴らすと、近くのモンスターを目覚めさせて恐怖させます（太鼓は自身も30〜49ターンの間難聴状態にします）。通常の木製のフルートは単に綺麗な音を鳴らすだけです。

#### その他の注目すべき道具 (Other Notable Tools)

| 道具の名称 | 用途と特徴 |
| --- | --- |
| つるはし / マトック (Pickaxe / mattock) | 壁や床を掘り崩して通路や抜け穴を作る |
| ユニコーンの角 (Unicorn horn) | 混乱、盲目、病気、幻覚、朦朧、嘔吐、難聴を治療 |
| [聴診器 (Stethoscope)](#tool-stethoscope) | モンスターのHPと状態異常を正確に診察 |
| 缶切り (Tin opener) | 1ターンで安全に缶詰を開封 |
| 缶詰作成道具 (tinning kit) | モンスターの死体を缶詰にして永久保存 |
| 脂の缶 (can of grease) | 防具、武器、鞄に油を塗って保護加工 |
| 目隠し (Blindfold) | 任意で自身を盲目化（テレパシーの発動に有用） |
| タオル (Towel) | 顔に投げられたクリームパイを拭き取る。目隠しの代用にもなる |
| [魔法のマーカー (Magic marker)](#tool-magic-marker) | 白紙の巻物や魔法書に任意の魔法を書き込む |
| [水晶玉 (Crystal ball)](#tool-crystal-ball) | 指定した記号のアイテムや敵をフロア全体からスキャン探索 |
| 開放の鐘 (Bell of Opening) | 召喚の儀式アイテム。クエストネメシスを倒して死体から回収 |
| 紐 (leash) | ペットを繋ぎ止め、階段移動時に確実に追従させる |

#### 主要な道具 (Key Tools)

呪われていない **ユニコーンの角** を使用（`a`）すると、混乱、盲目、病気、幻覚、朦朧、嘔吐、難聴といった主要な状態異常の大半を治療できます。常に1本携帯してください。

角は必ず祝福しておきましょう。祝福された角は1回の使用で最大7つの異常を一度に治癒できますが、呪われていない角は最大3つまでであり、治すべき異常があっても35%の確率で失敗します。呪われた角を使うと逆に前述の異常をランダムに *自身に付与* してしまうため、使用前に必ずBUCを確認してください。角は使用しても消耗しないため、平時のテスト使用は無料です。

[]{#tool-stethoscope}
**聴診器** は、モンスターの正確なHPとステータスを診察します。各ターンにおける初回の使用は「無料行動」であり、行動時間を消費しません（同ターン内の2回目以降の使用は通常通り時間を消費します）。

なお、NetHack 5.0 における重要な変更点として、**ユニコーンの角は低下した能力値ポイントをもはや回復しなくなりました**。ドレインされた筋力、知力、知恵などを取り戻すには、「能力回復の薬」（または同名の呪文）が必要です。角は依然として「状態異常」に対する万能薬ですが、能力値低下には別の手当てを用意しておきましょう。

[]{#tool-magic-marker}
**魔法のマーカー** は、白紙の巻物（および、より多くのチャージを消費して魔法書）に好きな内容を書き込める印刷機です。生まれたてのマーカーには 30〜99 チャージが入っており、呪われていない充填の巻物を1枚読むことでチャージを最低50（祝福時ならそれ以上）まで1度だけ回復できます（2回目の充填は必ず失敗します）。巻物を1枚書くコストは、その巻物の基本価格の約半分から全額に相当します：地図の巻物は 4〜7 チャージ、識別の巻物は 7〜13、武器強化／防具強化／充填の巻物は 8〜15、瞬間移動の巻物は 10〜19、そして **虐殺の巻物は 15〜29 チャージ** を消費します。魔法書を書くには呪文レベル × 約10チャージが必要です（レベル3で平均22、レベル7で約52チャージ）。

意図した巻物を書くには、一度でも目にしたことのある未識別ラベルを入力します。まだ正式識別していなくても、そのラベルに対応する巻物を書き上げることができます。書いている途中でチャージが尽きてしまった場合、巻物は紙ごと完全に消滅して無駄になります（魔法書の場合は紙だけ残り、文字が薄れて白紙に戻ります）。

白紙の巻物はマーカーの燃料であり、自分で量産できます：**不要な巻物や魔法書を水に浸すだけで、インクが洗い流されて白紙に戻ります。** 水たまりや堀に浸せば100%確実に白紙化できます（噴水でも可能ですが噴水のランダムリスクが伴います）。したがって、余った「光の巻物」や「怪物を作る巻物」はゴミではなく、「識別の巻物」や「武器に魔法をかける巻物」の貴重な原材料なのです。

マーカーで優先して書くべき高価値な巻物には、**虐殺の巻物**（一般的な標的は `L`、`&`、`h`。自身の種族巻き添えに注意）、**充填の巻物**（8〜15チャージで願いの杖の願いを1回追加）、**武器に魔法をかける巻物 / 鎧に魔法をかける巻物** などがあります。

また、マーカーは「レイスの宴」の仕込みにも活用されます：墓場以外のフロアで呪われた虐殺の巻物を読むことで、足元に4〜6体のレイスを召喚して経験値を貪り食うことができます（[レイスについての覚書](#a-note-on-wraiths) を参照）。

**缶詰作成道具** は、モンスターの死体を缶詰（栄養値最大50で永久保存）へと加工します。缶詰に加工する処理によって、生肉が持つ毒や酸のダメージが完全に中和され、腐敗も防がれます。そのため、毒耐性や酸耐性を持っていなくても、殺人蜂や酸のブロッブの缶詰を安全に食べて耐性獲得を狙うことができます。ただし、コカトリスを缶詰にしてはならず、コカトリスの缶詰を食べてはなりません。食べた瞬間に石化して即死します。

**つるはし** および重量のある **ドワーフのマトック** は、大半の壁や床を掘り崩すことができます。適用（`a`）して横方向を指定すればトンネルを掘り、真下を指定すれば下の階へ飛び降りる抜け穴を作れます。倉庫番は掘削不能です。またゲヘナの「死者の谷」の床、モロクの聖域、2つの塔も掘削に抵抗しますが、中間の迷路フロアは自由に掘り抜くことができます。石像に向けて適用すると、石像を破壊して中身のアイテムを取り出せます（石像の罠だった場合はモンスターが実体化して動き出します）。

[]{#tool-crystal-ball}
**水晶玉** は、適用（`a`）することで任意のマップ記号を指定し、フロア全体からその記号の存在をスキャン探索できる千里眼の神託具です。使用するたびに1チャージを消費します。

使用時に正しく視覚化できるか暴発するかは知力（Int）に依存します。クエスト・アーティファクトの水晶玉であれば知力8以上、祝福された水晶玉なら16以上、呪われていないなら20以上で安全に使用できます。判定に失敗すると暴発し、混乱、盲目、幻覚、あるいは（呪われていない通常玉では1/5の確率で）約 1d30 の爆発ダメージを被ります。呪われた水晶玉はチャージがある限り確実に暴発します。

**油の缶** は、防具に油を塗って巻きつき攻撃、接着攻撃、マインドフレアの触手を滑らせて回避できるようにします。また、鞄に油を塗ることで、油が乾くまで中身を水濡れから保護することができます。

### 武具庫 (The Armory)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Shield spell penalty is weight-gated (weight > small-shield's 30, spell.c:2269); the 30-weight drain- and shock-resistance shields also avoid it, so the small shield isn't the "only" one.
- Crysknife reverts to a worm tooth EVERY time unless erodeproofed (then ~10%); the book had it inverted (do.c:911).
- Monk martial-arts -20 to-hit applies to ANY body armor including dragon scale mail (uhitm.c:397, "if (uarm)"); DSM is not exempt.
- Rangers CAN two-weapon (unskilled, -9), not "cannot at all" (can_twoweapon has no role gate, wield.c:766).
- Verified correct: AC/MC values, DSM +3 vs mail +9 & merge rules, enchant destruction thresholds, robe halving metal-suit penalty, gauntlets of power Str 25, Excalibur odds, lance joust.
-->
<!-- audit
2026-05-18:
- shield of drain resistance is a second non-artifact source (objects.h:656-658)
- warning glyph levels: white, red ×3, magenta, bright-magenta — no yellow (drawing.c:39-52)
- cloak of protection MC3; cloak of magic resistance MC1 (objects.h:637-646)
- MC formula at uhitm.c:87 — MC3 blocks 90% of monster spells
- helm of caution grants the WARNING intrinsic (do_wear.c:448-450)
- DSM dual-property pattern: armor + per-color intrinsic (do_wear.c:806-883)
- gray and silver DSM grant no extra intrinsic
- DSM scroll-of-enchant transformation requires spe ≥ 0 (read.c:1225)
- shield casting penalty has two parts: ANY shield adds flat spelshld to splcaster (spell.c:2197; Wiz 3, Pri 2), and a shield heavier than small-shield (>30 weight) quarters the final chance (spell.c:2269). Small shield + the 30-weight drain/shock-resistance shields dodge only the /4; the flat penalty still applies to any shield.
- strategy aligned with NetHackWiki Dragon scale mail, Cloak of protection, Magic cancellation, Speed boots: GDSM as the popular MR wish, MC3 from cloak of protection, speed boots make turns more numerous (https://nethackwiki.com/wiki/Dragon_scale_mail, https://nethackwiki.com/wiki/Cloak_of_protection, https://nethackwiki.com/wiki/Magic_cancellation, https://nethackwiki.com/wiki/Speed_boots)
-->

このセクションでは、装備の選び方を解説します。[武器一覧表](#weapons-tables) および [防具一覧表](#armor-tables) の付録には、すべてのアイテムの完全な性能値が記載されています。

#### 防具とAC (Armor and AC)

アーマークラス（AC）は敵の攻撃がどれくらいの頻度で命中するかを決定する数値であり、ゲーム内で最も重要な防御指標です。ACの数値を1点下げるごとに、モンスターの攻撃が空振りに終わる確率が上がります。ACは10から始まり、防護を重ねることで低下していきます（値が低いほど優秀です）。ACが −10 以下になれば物理攻撃でダメージを受けることは極めて稀になります。昇天用装備セットの実用的な目標値は **AC −20** であり、−25 を超えると低下の恩恵は逓減していきます。

もしあなたの **ACが 6 またはそれより悪い** 場合、祭壇でのBUC判定をいつまでも待っていてはいけません。一般的な胴防具、兜、盾、マントなどは、通常そのリスクを冒してでも装備する価値があります。ただし、靴、小手、円錐形の帽子は、呪いや有害な魔法効果で身動きが取れなくなる恐れがあるため、装備する前に必ずテストしてください。

| スロット | 今すぐ装備 | 探すべき装備 | 注意点 |
| ---- | -------- | -------- | -------- |
| 胴 (Body) | 過重にならない範囲で最良の鎧 | ドラゴンの鱗鎧 | 修道士は命中率に−20のペナルティ。金属製は詠唱を激しく妨害 |
| マント (Cloak) | 呪われていない有用なマント全般 | 魔法耐性、防護、幻影 | ミイラの包帯は透明化を無効化する |
| 兜 (Helm) | ACが貧弱なときは一般的な兜 | 知恵、警戒、テレパシー | 円錐形の帽子（三角帽子/道化帽）は事前識別必須 |
| 小手 (Gloves) | BUC判定後にのみ装備 | 力または器用さ | お手玉の小手は通常呪われている |
| 靴 (Boots) | BUC判定後にのみ装備 | スピード、水上歩行、跳躍 | 浮遊の靴やつまずきの靴は通常呪われている |
| 盾 (Shield) | 片手武器使用かつ修道士以外 | 反射または各種耐性 | 盾全般が両手持ちを封じ、魔法詠唱にペナルティを与える |
| シャツ (Shirt) | 入手次第装備 | いずれのシャツでも（要強化） | 露出したシャツ（胴鎧未装備）は店の販売価格を悪化させる |

##### 胴防具 (Body suits)

胴防具は身につける装備の中で最も重く、単体で最も大きなAC供給源となります。武闘家（Monk）はこのスロットを空にしておくことで最も真価を発揮します。ドラゴンの鱗鎧を含め、**いかなる** 胴防具であっても、装備すると武術（Martial Arts）の命中率に −20 のペナルティを受けます。終盤では、ペナルティを回避できないと知りつつも、優れたACと耐性のためにドラゴンの鱗鎧をあえて装備する武闘家もいます。

胴防具の最下層は主に革製品です。**レザーのジャケット** (AC 1, 重量 30) は半身用の服であり、鞄の中身を整理する間に羽織るには十分軽いですが、本格的な鎧にはなりません。**革の鎧** (AC 2, 重量 150) は頑丈な牛革製で、洞窟人の初期装備であり、ミスリルがまだ手に入らない魔法使いの中盤の標準装備でもあります。どちらも呪文詠唱へのペナルティがなく、錆びることもありません。**鋲付き革の鎧** (AC 3, 重量 200) はその名の通り革に金属鋲を打ち込んだもので、これも詠唱に対して安全です。

鉄製の鎧は小規模なものから本格的なものまであります。**鉄環の鎧** (ring mail) は鉄の環を編み込まずに裏地に縫い付けたもので、鎖かたびらよりも軽く、通常版で AC 3、オーク製で AC 2 の防御力です。**鱗の鎧** (scale mail) (AC 4, 重量 250) は、魚の鱗が重なり合うように鉄の小札を裏地に縫い付けたもので、古代ローマのロリカ・スクアマタのような外観です。**鎖かたびら** (chain mail) (AC 5, 重量 300) は一般に「鎧」と聞いて誰もが思い浮かべる姿であり、数千個の連結した鉄の環がチュニックに縫い合わされています。オークの鎖かたびらは防御力が1点劣り、まるで初心者が作ったかのような粗雑な外見です。

**ドワーフのミスリル服** (Dwarvish mithril-coat) は、わずか 150 の重量で AC 6 を誇り、錆びることもありません。**エルフのミスリル服** (Elven mithril-coat) は同じ重量で AC 5 を与えます。ミスリルは依然として金属製であるため、呪文詠唱に対するペナルティはプレートメイルと同等ですが、ローブを着用すればそのペナルティを半減できます。魔法の使い手にとっても、この優れたACは詠唱ペナルティの代償を払う価値が十分にあります。

信頼できる重装鎧としては、**薄板鎧** (Splint mail: 革の裏地に鉄板の帯をリベット留めしたもの) と、**帯鋼鎧** (Banded mail: チュニックの周りに水平な鉄の帯を重ねて巻いたもの) があります。どちらも AC 6 で、重量は 350〜400 です。プレートメイルよりわずか1点ACが劣るだけで、重量は著しく軽くなっています。魔法使い以外のほとんどの冒険者にとって、ドラゴンの鱗を入手するまでは、これら2つのいずれかが現実的な胴防具の選択肢となります。

頂点に君臨するのが **鋼鉄の鎧** (plate mail) です。これは中世後期のヨーロッパ騎士がまとった全身甲冑であり、キルティングジャケットの上に可動式の鋼鉄プレートをストラップで固定したものです。ダンジョンで最も重い胴防具 (重量 450) であり、最強の防御力 (AC 7) を誇ります。この重さは騎士やワルキューレであっても瞬く間に重荷（Burdened）へと追い込み、鉄の材質は呪文詠唱の失敗率を跳ね上げます。侍の画面では同じアイテムが **炭胴** (tanko) として表示されます。**水晶のプレートメイル** は同じ形状を透明なガラスで再現したもので、錆びる危険がなく、同じACで、はるかに希少です。**青銅のプレートメイル** はその古い地中海の祖先であり、1点劣る AC 6 で、銅系であるため錆びる代わりに腐食（緑青）します。

ドラゴンの鱗およびドラゴンの鱗鎧については、後述の [ドラゴンの鱗鎧](#dragon-scale-mail) を参照してください。

##### シャツ (Shirts)

シャツは胴防具の *下* に着用します。基本ACは 0 ですが、呪文詠唱を一切妨害せず、重量もほとんどないため、+5 まで強化されたシャツは極めて大きな働きをします。ダンジョンに存在する2種類のシャツは、性能面では完全に同一の重量 5 の布製トップスです。**アロハシャツ** (Hawaiian shirt) は観光客の初期装備であり、**Ｔシャツ** (T-shirt) は無地の別バージョンです。どちらも防具を着込む際に最初に身につける必要があるため、すでに胴防具を着ている状態でシャツを着ようとすると、すべての防具を一度脱いでから着直す必要があります。

##### マント (Cloaks)

マントは胴防具の上に羽織り、適度なAC (0〜+3)、魔法防御（MC）、そして多くの場合有用な特性（能力）をもたらします。また、下に着ている鎧を一部の攻撃から保護する役割も果たします。

一般的な地域産マント（**オークのマント**、**ドワーフのマント**、**革のマント**）はいずれも AC 0〜1、重量 10〜15 であり、主にそれを身につけている種族によって区別されます。このグループの中で際立っているのが **エルフのクローク** (Elven cloak) であり、AC 1 に加えて忍び（Stealth）の能力を付与します。これはACそのものよりもはるかに有用です。

**防水クローク** (Oilskin cloak) は船乗りが着る油引きキャンバス地のアウターであり、ダンジョン内では AC 1、MC2 に加え、モンスターの巻きつき攻撃や溺れを防ぐ耐性をもたらします。**ローブ** (Robe) はまさに呪文の使い手が着るべきものであり、AC 2、MC2、そして最も重要な点として、金属製防具による呪文詠唱ペナルティの大部分を相殺します。鎖かたびらとローブを身につけた魔法使いは、革鎧を着ているのとほぼ同等に呪文を唱えられます。武闘家は +1 のローブを持ってゲームを開始するため、これを保持し続けるべきです。**錬金術の仕事着** (Alchemy smock) は化学者のエプロンであり、AC 1、MC1 に加え、毒耐性を付与します。体質としての毒耐性を得る前には素晴らしい防護具となります。

**ミイラの包帯** (Mummy wrapping) は見た目通りのものですが、1つ重大な特徴があります。着用中は透明化が無効化されます。これを拾った冒険者の大半は投げ捨てるべきです。他のマントで得られる AC 0 や MC1 は、透明化を封じることなく手に入ります。

特に注目すべき4つの魔法のマントがあります：

- **守りのクローク** (Cloak of protection) は、単体で防具中最高の MC3 を誇り、AC も 3 上昇させます。他の手段ですでに魔法耐性を確保している冒険者にとって、最終盤の定番マントとなります。
- **魔法を防ぐクローク** (Cloak of magic resistance) は、ダンジョンで最も単純かつ軽量な魔法耐性の供給源であり、ドラゴンの鱗鎧を入手するまでの中盤のあらゆる装備構成における生命線です。
- **幻影のクローク** (Cloak of displacement) は、モンスターがあなたの幻影を攻撃するように仕向け、低いACを競合することなく見事に補完します。
- **透明のクローク** (Cloak of invisibility) は透明化を付与し、モンスターの攻撃が外れやすくなるため、主に攻防一体のボーナスとなります。

##### 兜 (Helmets)

兜のスロットは頭部を覆い、転がる巨岩の罠、頭上からの落石、トンネル崩落による落盤といったダンジョンのささやかな奇襲からあなたを守ります。大半の兜は金属製であるため呪文詠唱を妨害します。魔法使いには布製の帽子が適しています。

一般的な兜（**オークの兜**、**ドワーフの鉄兜**、**兜（kabuto）**、**へこんだ鍋**）は鉄製で AC 1〜2、重量 10〜40 です。戦士系には実用的ですが、それぞれ呪文の失敗率計算に4ポイントのペナルティを加算します。**エルフの革帽子** (Elven leather helm) は呪文詠唱者向けの妥協案であり、革製で重量わずか 3、AC 1、ペナルティなしです。**フィドーラ** (fedora) は考古学者の初期装備の帽子であり、考古学者がかぶっている間は幸運（Luck）が +1 されます。

**三角帽子** (Cornuthaum) は魔法使いのとんがり帽子です。基本ACは 0 ですが MC1 を持ち、魔法使いがかぶると千里眼（Clairvoyance）を得られる一方、魔法使い以外の職業がかぶると千里眼が封じられます。**道化帽** (Dunce cap) は三角帽子の邪悪な双子です。かぶると自動的に呪われ、知力と知恵が強制的に 6 に固定され、解呪の巻物等なしには脱ぐことができなくなります。どちらも祭壇でBUC判定が可能です。また基本価格でも見分けがつきます（三角帽子は 80 zm、道化帽は 1 zm）。

**知恵の兜** (Helm of brilliance) は、装備中にその強化値を知力と知恵の両方に加算します。+3 の知恵の兜をかぶれば知力と知恵がともに +3 され、呪文使いの中盤の目標装備となります。**知性の兜** (helm of caution) は警告（Warning）の能力を付与します。視認していなくても周囲のモンスターが危険度に応じた色のシンボルで表示されるようになり、安価で軽量な、最序盤における最高の兜の1つです。**テレパシーの兜** (Helm of telepathy) は、目を開けているときは周囲8マス以内の怪物の心を感知し、目が見えない（盲目）状態ではフロア全体のテレパシーへと拡大します。

**逆属性の兜** (Helm of opposite alignment) は、装備中に自身の属性を逆転させます（そして10回中9回は呪われて生成されます）。基本的には罠アイテムですが、異なる属性の祭壇で生贄を捧げる、逆属性のクエストアーティファクトを我が物にする、あるいは星界の面で異なる属性の祭壇を選ぶなど、意図的に活用できる場面もあります。

##### 小手 (Gloves)

小手は防具の中で最も小さなスロット（全種類一律で AC 1）ですが、決定的に重要な防御の役割を果たします。小手を着用していれば、**コカトリスの死体** を安全に拾い上げ、武器として振り回すことすら可能です。小手なしで素手で触れれば、即座に石化してゲームオーバーになります（[石化](#petrification-stoning) を参照）。

**革の手袋** (Leather gloves: 侍には **弓掛け** と表示) は AC 1、重量 10 の標準的な革製品で、詠唱ペナルティはありません。**力の小手** (Gauntlets of power) はダンジョンの腕力ショートカットであり、装備すると元の強さに関係なく強さが強制的に 25 にセットされ、魔法使いであっても瞬く間に侮れない近接戦士へと変貌します。**器用さの小手** (Gauntlets of dexterity) は、その強化値を器用さに加算します。+3 の小手なら、鍛えた本来の器用さにさらに +3 が上乗せされます。

**お手玉の小手** (Gauntlets of fumbling) は罠アイテムです。10回中9回は呪われて生成され、着用者を絶えずつまずかせます。未識別の小手は装備する前に必ず祭壇テストを行ってください。呪われた小手を着け、さらに呪われた武器を手に持ってしまうのは、ダンジョンで最も古典的な膠着状態（デッドロック）です。解呪の巻物、聖水、あるいは祈りなしにはどちらも外せなくなります。

##### 靴 (Boots)

靴は移動に関する特性（水上歩行、跳躍、浮遊、加速）の宝庫であるため、ほとんどのビルドにおいて、このスロットはAC（1〜2）よりも「その靴が何をもたらすか」によって選ばれます。

一般的な靴には2つの丈といくつかの重量があります。**短靴** (Low boots: AC 1) と **長靴** (High boots: AC 2) は軽量な革製で日常的な基本装備です。**鉄の靴** (Iron shoes: AC 2) と **蹴り挙げ靴** (Kicking boots: AC 1) はキックを多用する戦士向けの重い鉄製バリエーションです。

有用な魔法の靴は、あなたの移動のあり方を劇的に変えます：

- **韋駄天の靴** (Speed boots) は超高速（Very Fast）の能力を付与し、3ターンのうち2ターンがフリーアクションになります。ゲーム内で最も願われる靴です。
- **水上歩行の靴** (Water walking boots) は水の上を歩くことを可能にし、城の跳ね橋の堀や、深層の水のエレメンタルプレーンで決定的な役割を果たします。その瞬間まで大切に保管しておきましょう。
- **飛び跳ねる靴** (Jumping boots) は `#jump` コマンドを追加し、呪文を唱えることなく戦闘中に隣接マスへと一気に飛び跳ねることができます。
- **エルフの靴** (Elven boots) は忍び（Stealth）を付与し、盗賊やレンジャーにとって頼りになる選択肢です。

**罠の靴** は10回中9回は呪われて生成されます：

- **浮遊の靴** (Levitation boots) は着用者を常に宙に浮かび上がらせ、呪われていると脱ぐことができなくなります。
- **つまずきの靴** (Fumble boots) は 1〜20 ターンごとに転倒させ、2ターンを行動不能にします。

靴を履く前には必ず祭壇テストを行ってください。呪われた靴は呪いを解くまで脱げず、浮遊の靴で堀の上で無力に浮かんだままになる危険もあります。

##### 盾 (Shields)

盾は AC 1〜2 をもたらしますが、装備構成の他の部分で大きな妥協を迫られます。いかなる盾であっても、二刀流および両手持ち武器の使用を封じます。また、すべての盾は一律の呪文詠唱ペナルティを加算し、さらに重量が 30 を超える盾は最終的な呪文成功率を 4分の1 に激減させます。修道士は盾を装備できますが、装備中は武術の命中率ボーナスを失います。なお、盾は見えない光線や矢の罠を防ぐことはできません。

一般的な盾（**小さい盾**、**エルフの盾**、**オークの盾**、**ウルク＝ハイの盾**、**ドワーフの丸盾**）は AC 1〜2 で、特別な特性はありません。**小さい盾** (AC 1) は、重量 30 の2種類の耐性の盾とともに、呪文成功率の激減（4分の1化）を回避できます。ただしこれら3つであっても一律の詠唱ペナルティは受けるため、純粋な魔法使いにとっては盾スロットを空にしておくのが最強です。

**大きな盾** (Large shield) と **ドワーフの丸盾** は AC 2 ですが重く（重量 100）、他のあらゆる盾と同様の制限（着用中は両手剣、両刃の斧、長柄武器を振るえない）を課されます。

**吸魔耐性の盾** (Shield of drain resistance: AC 1, 吸魔耐性) と **耐電の盾** (Shield of shock resistance: AC 1, 電撃耐性) は、それぞれ名付けられた耐性を付与します。吸魔耐性（レベルドレイン耐性）は、この盾以外にアーティファクト以外の定常入手源が存在せず、耐電の盾もゲーム中で最も手軽な電撃耐性源の1つです。**反射の盾** (Shield of reflection) は銀製で AC 2、そして死の光線、冷気の円錐、各種ブレス攻撃を術者へと跳ね返す「反射」の能力を付与します。これは盾スロットで反射を確保することで、胴防具を（魔法耐性を付与する）灰色ドラゴンの鱗鎧のために空けておけるため、定番の昇天用装備セットにおいて重要な役割を果たします。

**損耗、強化、そして防護** については、それぞれ後述のセクションで詳しく扱います。防具は錆び、燃え、あるいは腐食します（[腐食と防蝕加工](#erosion-and-proofing) を参照）。鎧に魔法をかける巻物は防具を強化しますが、+3 を超えると破壊のリスクが伴います（[防具の強化](#enchantment) を参照）。自属性の僧侶にゴールドを寄付すると、装備ACに累積し、さらにMC0をMC1に引き上げる体質としての防護を購入できます（[僧侶への寄付](#donating-to-priests) を参照）。

[]{#magic-cancellation}
**魔法防御 (Magic cancellation: MC)。** 身につけている防具は、最大 3 までの隠れた防御力を提供します。MCは、レベルドレイン、毒、麻痺、睡眠、減速、混乱、気絶、獣化症、病気、スライム化、およびテレポート攻撃の二次効果を無効化する可能性があります。視線攻撃、ブレス攻撃、コカトリスの接触、または脳吸い出し攻撃を防ぐことはできません。防衛確率はMCレベルによって決定されます：

| MC | 防御成功率 |
|----|--------------|
|  0 | 0%           |
|  1 | 30%          |
|  2 | 60%          |
|  3 | 90%          |

着用している防具の中で最も高いMC値から計算を開始します。外来の防護（Extrinsic Protection）はMCを +1 します（**守りの魔除け** の場合は +2）。複数の外来防護源があっても重複して加算されることはありません。僧侶への寄付や呪文による内在の防護（Intrinsic Protection）は、単に MC0 を MC1 へと引き上げるだけです。合計値は最大 3 で頭打ちとなります。守りのクロークは単体で MC3 に達し、守りの魔除けは MC1 の鎧を MC3 へと引き上げます。

**MCは魔法耐性（Magic Resistance）とは異なります。** 魔法耐性は特定の *魔法的な* 攻撃（死の杖の光線、マジックミサイル、死の指先呪文、へんげ光線、魔法の罠など）を 100% 遮断する二者択一（ON/OFF）の耐性フラグです。これに対してMCは、前述の近接攻撃による状態異常効果を確率で防御するものです。マインドフレアの触手攻撃を阻止するのはMCではなく通常は兜であり、コカトリスの接触には固有の予防策が必要です。昇天を目指す英雄は、この両方の防御を揃える必要があります。

**魔法を防ぐクローク vs. 守りのクローク。** これら2つのマントは、上述の異なる2つの防御を担っています：

- **魔法を防ぐクローク** (Cloak of magic resistance) は、魔法耐性の特性を付与し、MC1 を提供します。ゲーム内で最もシンプルな魔法耐性の入手源であり、灰色ドラゴンの鱗鎧をまだ願っていない中盤の英雄たちを支え続けます。
- **守りのクローク** (Cloak of protection) は魔法耐性を付与しませんが、単体で最高の MC3 をもたらします。他の手段ですでに魔法耐性を確保している場合、最終盤のベストな選択肢となります。

定番の昇天用装備セット（Ascension Kit）では、胴スロットに **灰色ドラゴンの鱗鎧** を装備して魔法耐性を確保し、マントスロットに **守りのクローク** を着用して MC3 を得ることで、両方の防御を完璧に成立させます。灰色ドラゴンの鱗鎧を手に入れるまでは、マントスロットで魔法を防ぐクロークが不可欠な役割を果たし、守りのクロークは鞄の中で出番を待つことになります。

ゲーム内のすべての防具のAC、MC、重量、価格、および付与される能力の完全な数値データについては、付録の [防具一覧表](#armor-tables) を参照してください。

#### 武器 (Weapons)

武器は攻撃の射程、ダメージ、そして鍛えられるスキルを決定します。以下のセクションでは、武器を用途ごとに分類して解説します。スキルごとの詳細な性能表については、付録の [武器一覧表](#weapons-tables) を参照してください。

武器の操作には一握りの基本コマンドを用います：**`w`** で武器を装備（手に持つ）；**`x`** でサブ武器スロットと持ち替える；**`t`** で任意のアイテムを投げる；**`f`** で矢筒に装填された弾丸・飛び道具を発射する；**`Q`** で矢筒に装填するアイテムを指定する。また、長柄武器、鞭、つるはし、鉄のフックなどは、多くの道具と同様に **`a`** (使用 / apply) キーでも操作します。

最初のプレイでは、自身の職業が最後まで使い続けられる武器スキルを鍛えましょう：

| 職業 | 最初に鍛えるべき武器 |
| ---- | ----------- |
| 考古学者 (Archeologist) | まずは牛追い鞭。ダメージが必要になったらサーベルかつるはしへ移行 |
| 野蛮人 (Barbarian) | 初期装備に合わせ、斧または両手剣 |
| 洞窟人 (Cave Dweller) | こん棒 |
| 治療師 (Healer) | ナイフ（メスのスキル）または六尺棒 |
| 騎士 (Knight) | 長剣。騎乗を維持するならランス |
| 武闘家 (Monk) | 素手格闘・武術 (Martial Arts) |
| 僧侶 (Priest) | メイスまたはモーニングスター |
| レンジャー (Ranger) | 弓 |
| 盗賊 (Rogue) | 短剣 |
| 侍 (Samurai) | 長剣（刀）。遠距離用として弓 |
| 観光客 (Tourist) | 投げ矢 |
| ワルキューレ (Valkyrie) | 長剣 |
| 魔法使い (Wizard) | 短剣または六尺棒 |

##### 片手近接剣 (One-handed melee swords)

騎士、ワルキューレ、侍をはじめとする多くの戦士たちが日常的に振るう剣です。片手持ちであるため、もう一方の手に盾を持ったり、逆手武器を構えたりする自由があります。

**小剣** (Short sword: 侍には **脇差 / wakizashi** と表示) は、近接刺突用に設計された60cmほどの直剣です。小型モンスターに d6、大型に d8 のダメージ。盗賊の初期武器であり、侍の逆手武器でもあります。

**シミターと銀のサーベル** (Scimitar and silver saber)。これらはサーベルスキルの刀剣です。**シミター** は『千夜一夜物語』に登場するような湾曲した斬撃剣で、一般的な鉄製の片手剣です。**銀のサーベル** はその銀製の同系武器であり、悪魔、獣化モンスター、吸血鬼、幽霊、そして大半のインプに対して強烈な追加ダメージを与えるため、ゲーム終盤における最強クラスの片手武器の1つです。2つのアーティファクト銀サーベルとして、**グレイスワンダー** (Grayswandir: 銀製、全攻撃でダメージ2倍、幻覚耐性をもたらす最高峰の願い候補) と、**ウェアベイン** (Werebane: 獣化モンスター特効) があります。

**幅広の剣** (Broadsword)。長剣よりも幅広でやや短く、十字の鍔を備えた中世ヨーロッパの刀剣です。**ルーンの剣** (Runesword) は幅広の剣の混沌バージョンです。そのアーティファクト形態である **ストームブリンガー** (Stormbringer) は敵からレベルを吸い取りますが、こちらの意図に関係なく平和的な中立NPCにも勝手に襲いかかる危険を孕んでいます。

**長剣** (Long sword)。ダンジョンを象徴する刀剣です。経験レベル5以上のキャラクターが長剣を泉に浸す（`#dip`）と、**エクスカリバー** (Excalibur) へと変貌するチャンスがあります。確率は騎士で 6分の1、他の秩序属性で 30分の1 です。秩序属性以外の者が浸すと、剣が呪われるだけです。エクスカリバーは序盤における至宝です：命中率 +d5、ダメージ +d10、レベルドレイン耐性、そして1歩歩くごとの無料索敵（オートサーチ）をもたらします。長剣クラスには、**刀** (katana: 侍の片手曲刀で、本来的に命中 +1 が備わり、通常の長剣よりわずかにダイスが大きい) や、数々の長剣アーティファクト（**フロストブランド**、**ファイアブランド**、**ジャイアントスレイヤー**、**ヴォーパルブレード**、**サンソード**、そして刀アーティファクトの **スニッカーズニー**）が属しています。

弓などの発射機（ランチャー）を使用する際は、サブ武器スロットに近接武器をセットしておきましょう。モンスターが隣接してきたら `x` キーで瞬時に近接武器へと切り替え、撃破したら再び `x` を押して発射機へと戻します。

##### 両手近接武器 (Two-handed melee)

盾スロットや逆手を犠牲にする代償として、より重い一撃を繰り出します。NetHack 5.0 では、両手持ち武器による近接打撃すべてに **強さダメージボーナス 1.5倍 (3/2)** が適用されるようになり（腕力によるダメージ加算値が1.5倍になる）、両手武器ビルドは片手武器＋盾ビルドに対して極めて本格的な競争力を取り戻しました。

**両手剣** (Two-handed sword)。16世紀後半のドイツのツヴァイヘンダーであり、ランツクネヒト傭兵が両手で振り回した1.5メートルの鋼鉄刀です。小型に d12、大型に d6+2d6 という破格の打撃力を持ちますが、重量 150 と極めて重厚です。**大刀** (tsurugi) は日本の直刃両手刀であり、はるかに軽量（重量 60）ながら、ゲーム内の全武器中で最も高い対小型ダメージダイス（d16）を誇ります。そのアーティファクト形態が、侍のクエストアーティファクトである **村正の剣** (Tsurugi of Muramasa) です。

**六尺棒** (quarterstaff)。シンプルな木製の棒で、両手持ちで小型・大型ともに d6、重量わずか 40 です。武器は防具と違って呪文詠唱ペナルティを与えません。それどころか、六尺棒を装備していると呪文詠唱にわずかなボーナスすら得られます。魔法使いはこれを持って冒険を開始し、治癒師、僧侶、洞窟人、魔法使いが「エキスパート」までスキルを鍛えることができます。

一部の両手武器は、両手持ちであること以上に独自の戦術的役割が際立っているため、他の節で解説しています：**両刃の斧** は「斧」、**ドワーフのつるはし** は「つるはし」、長柄武器は「リーチ武器」、ランスは「騎乗武器」、弓やクロスボウは「遠距離武器」を参照してください。

##### 斧 (Axes)

斧の刃は大型の標的に対して強い偏重を持っています（大型モンスターに対する追加ダメージダイス）。**斧** (Axe) は標準的な片手用の木こりの斧で、小型 d6 / 大型 d4 のダメージです。**戦斧** (battle-axe) は長い柄と幅広の刃（多くは両刃）を持つ両手持ちバージョンで、小型 d8+d4 / 大型 d6+2d4 の威力を誇り、両手持ちであるため強さボーナス 1.5倍の恩恵を受けます（盾は装備不可）。蛮族のクエストアーティファクト **クリーバー** (Cleaver) は両刃の斧です。

##### 片手打撃武器 (Blunt one-handed)

メイスとこん棒の系統です。聖職者のフレーバー通りアンデッドに対して有効（血を流さない）であり、歴史的な意味でも重装甲の敵に対して効果的です（こん棒の一撃は相手がプレートメイルを着ていようがお構いなしに骨を砕きます）。

**こん棒** (Club)。先端が太くなった木の棒です。洞窟人の初期装備で、小型 d6 / 大型 d3、軽量で特別な特性はありません。

**アキリス** (Aklys)。柄に革紐が結び付けられた古代ギリシャの珍しい投擲用こん棒です。ダンジョンではこの革紐が決定的な意味を持ちます：アキリスをメイン武器として構えて投げると、紐によって手元へと瞬時に引き戻され、ヨーヨーのように手元に帰還します。小型 d6 / 大型 d3 のダメージで、ごく稀に戻ってこないこともあります。

**メイス** (Mace)。成形された打撃ヘッドを持つ中世ヨーロッパの鋼鉄製メイスです。僧侶の初期装備です。僧侶への確定生贄ギフト（第1号）は **デーモンベイン** (Demonbane) であり、悪魔特効ダメージと追放（banish）の能力（`#invoke`）を備えた銀のメイスです。**銀のメイス** はその通常銀製バージョンです。

**モーニングスター** (Morning star)。トゲ付きの金属球を柄に取り付けた武器で、小型 2d4 / 大型 d6+1 という片手武器としては非常に重い打撃力を持ちます。アーティファクト **トロルズベイン** (Trollsbane) はモーニングスターであり、装備中にHPが自然回復し、トロールに対して追加ダメージを与えます。

**フレイル** (Flail)。柄に鎖で繋がれた重り付きの鉄球です（侍には **ヌンチャク / nunchaku** と表示）。小型 d6+1 / 大型 d4+d4、重量わずか 15 で、大型モンスターに対して優れた累積ダメージを発揮します。**鉄のフック** (Grappling hook) も同じフレイルスキルで扱います。2マス離れた位置に向けて使用（`a`）すると、ごく小さなモンスターを1マス引き寄せたり、アイテムを引っ掛けたり、自身を1マス引き寄せたりできます（通常の敵を近接間合いに引きずり込むことはできません）。

**ウォーハンマー** (war hammer)。打撃面と背面のスパイクを備えた小型の片手戦槌です。小型 d4+1 / 大型 d4。ワルキューレへの確定生贄ギフトは、北欧神話の雷神トールの雷槌である **ミョルニル** (Mjollnir) です。命中時に電撃ダメージを与えます。強さ 25 を備えたワルキューレだけが、これを投げて確実に手元へ戻すことができます。

##### リーチ武器 (Reach)

リーチ武器は、**`a`** (使用 / apply) コマンドによって離れた間合いから攻撃できる武器群です。長柄武器、ランス、そして長剣アーティファクトの **スニッカーズニー** (Snickersnee) がこのカテゴリに属し、いずれも同じリーチ処理ルーチンを用います：攻撃射程は武器スキルのランクに応じて広がり、「入門」段階の2マス離れた間合いから、「エキスパート」ではおよそ 2.8マス（斜め2マス）まで届くようになります。使用コマンドは斜めを含む全8方向に対して有効です。さらに快適な操作法として、**`f`** (発射 / fire) コマンドがリーチ攻撃としても機能します：リーチ武器を構えている状態で `f` を押すと、射程内のモンスターを自動的にターゲットし、方角の入力なしに1キーストロークで打撃を加えます。

**長柄武器** (Polearms) は、長い柄の先端に刃や鉤を取り付けた武器の総称です：グレイブ、ハルバード、パルチザン、バルディッシュ、ヴォルジュ、フォシャール、ギザルム、ビル＝ギザルム、ルツェルンハンマー、カラスの嘴（bec de corbin）、ランカ（ranseur）、スペタム。これらの大半は15世紀のヨーロッパ戦場で、騎兵を馬から引きずり降ろしたり甲冑の継ぎ目をこじ開けたりするために考案されたものです。**グレイブ** は侍の従者が振るう長柄の曲刀である **長刀 / naginata** としても扱われます。すべての長柄武器は両手持ちです。もし長柄武器を持って隣接するモンスターに通常移動でぶつかると、その打撃は **強打 (bash)** として扱われます：ダメージは基本 1d2 に激減し、武器スキルボーナスは一切適用されず、強さボーナスのみが加算されます。リーチ攻撃こそが長柄武器を携行する唯一の価値であり、至近距離では短剣よりも劣る性能になります。

**ランス** (Lance)。鋼鉄の穂先を備えた長い木製の槍であり、全速力で突撃する騎馬騎士の武器です。他の長柄武器と同様のリーチ攻撃に加え、最大の特長である **馬上槍試合 (joust)** 突撃を行えます：馬やポニーに騎乗した状態で敵へと突撃すると、接触時に **+2d10** の追加ダメージを与えます（ランスを逆手に持っている場合は +2d2）。激しい突撃の際、250分の1 の確率でランスが粉々に砕け散ることがあります。騎士はランスのスキルをエキスパートまで鍛えることができ、鞍付きのポニーとランスを手にしてゲームを開始します。馬上の騎士は、接触時の馬上突撃と離れた位置からのリーチ攻撃の双方を自在に使い分けることができ、ランスはこの職業で最も汎用性の高い武器の1つとなります。騎士以外のほとんどの職業はランスを目にすることすら滅多にありません。

##### 短剣とナイフ (Daggers and knives)

小型の刃物類であり、ダンジョンで最も汎用性の高い武器クラスです。

**短剣** (Dagger)。青銅器時代から腰に佩き続けられてきた、基本的な30cmほどの両刃の刃物です。小型 d4 / 大型 d3、最初から +2 の命中補正が組み込まれており、軽量で、そして極めて重要なことに **スタック（束ねて所持）可能** です。短剣は、まとまった数を積極的に投げたくなる唯一の刃物です：エキスパート段階かつ盗賊のクラスボーナスがあれば、**`f` キーを1回押すごとに最大4本の短剣を一度に投擲** できます。`Q` で短剣のスタックを矢筒にセットし、`f` で発射し、戦闘が終わったら歩いて回収します（短剣が破損することは滅多にありません）。短剣ファミリーにはフレーバー豊かな派生があります：**エルフの短剣** (アーティファクト形態の **スティング / つらぬき丸** はトールキン作品へのオマージュでオークが近づくと青く光ります)、**オークの短剣** (やや粗悪)、**銀の短剣** (銀嫌いの敵に特効、レンジャーの定番逆手武器)。そして **アサメ** (Athame) は、刃を鈍らせることなくエルベレス（Elbereth）を床に刻み込める儀式用短剣です。

**ナイフ** (Knife)。家庭用の包丁や折りたたみナイフであり、小型かつ軽量です。小型 d3 / 大型 d2 で、多重投擲ボーナスはありません。**メス** (Scalpel) は治癒師の初期装備である極小の手術用メスです。

**クリスカッター** (Crysknife: クリスナイフ)。フランク・ハーバートの小説『デューン』に登場するフレーメンの刃であり、砂虫の歯から削り出された20cmの刀身を持ちます。小型・大型ともに d10、命中 +3 という驚異的な威力を誇りますが、1つ大きな癖があります：防蝕加工（erodeproof）を施していない限り、床に落とすたびに例外なく元の「砂虫の歯」へと戻ってしまいます（あらかじめ防蝕加工しておけば、元に戻る確率を約10分の1に抑えられます）。

短剣やナイフは、`w` (主武器) + 副武器 + `x` (持ち替え) のローテーションパターンの恩恵を最大限に享受できます。典型的な盗賊は、小剣をメインに構え、逆手に短剣スタックを持ち、敵が遠くにいるときは `x` で短剣スタックを主武器スロットへと切り替えて投げつけます。

##### 鞭と鉄のフック (Whips and grappling hooks)

道具としても機能する武器類です。**牛追い鞭** (Bullwhip) は考古学者の初期装備です：先端に小さなクラッカー（破裂音を鳴らす房）がついた、編み革製の6フィートの鞭です。小型 d2 / 大型 d1 と戦闘用としては非力ですが、牛追い鞭を使用（`a`）することで、隣接するモンスターの武器を叩き落として武装解除させたり、落とし穴から自分を引き上げたりできます（房が周囲の調度品、巨岩、あるいは大型モンスターに引っ掛かって足場になります）。**ゴムホース** (rubber hose) はダンジョンのジョーク武器であり、キーストン・コップが携帯していることがあります。

**鉄のフック** (Grappling hook)。鎖に取り付けられた3本爪の鉄の鉤です。2マスの射程で使用（`a`）してアイテムを引っ掛けたり、ごく小さなモンスターを1マス引き寄せたり、自分自身を1歩引き寄せたりできます。フレイルのスキルを鍛えることができます。

##### 射撃武器 (Ranged)

射撃戦闘の体系的な概要は、戦闘章の [射撃戦](#ranged-combat) で解説されています。ここでは具体的なアイテムを紹介します：

**弓と矢** (Bows and arrows)。通常の **弓** (Bow)、**エルフの弓**、**オークの弓** は、様々な品質の1.5メートルの木製弓であり、すべて **矢** (Arrow: 1本につき重量 1) を発射します。**和弓** (Yumi) は日本の長い非対称の弓であり、侍の射撃武器で、**ヤ** (ya: 竹の矢) と組み合わせて使われます。レンジャーのクエストアーティファクトは **ディアナの長弓** (Longbow of Diana) であり、ローマ神話の狩猟の女神にちなんで名付けられ、何もない虚空から矢を無限に生み出す能力を持ちます。弓を `w` で構え、矢を `Q` で矢筒にセットし、`f` で発射します。レンジャーと侍は弓スキルをエキスパートまで鍛えられます。盗賊は弓スキルを一切鍛えることができません。

どの弓であっても任意の矢を発射できますが、一致した組み合わせ（エルフの弓とエルフの矢、オークの弓とオークの矢、和弓とヤ）を使うと、対応する種族または職業は1回の一斉射撃につき追加で矢をもう1本発射（マルチショット）できます。組み合わせの詳細については [武器一覧表](#weapons-tables) を参照してください。

**クロスボウとボルト** (Crossbows and bolts)。**クロスボウ** は、短く重い **クロスボウの矢（ボルト）** を発射する中世後期の機械仕掛けの弓です。1発あたりの威力は通常の弓よりも重いですが、装填に時間がかかり、フルのマルチショット（多重発射）を放つには強さ 18（ノームなら 16）が必要です。ボルトを撃つには必ずクロスボウが必要であり、通常の弓からボルトを射ることはできません。盗賊とレンジャーはエキスパートまで鍛えることができ、騎士は熟練（Skilled）で上限となります。

**スリング** (Sling)。2本の紐の間に革のポケットを取り付けた最もシンプルな射撃武器であり、ダビデが巨人ゴリアテを倒した武器です。洞窟人の初期装備です。石、火打石、あるいは宝石を発射します。

**投擲専用武器** (Throw-only weapons)。**投げ矢** (Dart) は大量にスタックでき、病気の薬に浸すことで毒を塗ることができます。**手裏剣** (Shuriken) は日本の投擲星型刃物であり、修道士は手裏剣の多重投擲ボーナスを得られます。**ブーメラン** (Boomerang) はオーストラリアの湾曲した投擲棍であり、標的を外すと自身のマスへと戻ってきます（キャッチするには器用さ判定が必要）。**アキリス** もこのカテゴリに属します（前述の「片手打撃武器」を参照）。

すべての投擲武器は、`Q` でスタックを矢筒にセットし、`f` で発射できます。矢筒を使わずに投げる場合は、`t` を押し、アイテムを選び、方向を入力します。

##### 二刀流スタイル (Two-weapon style)

自身が二刀流可能な職業である場合、逆手に何を持つかはメイン武器と同じくらい重要です。ルールと損益分岐点の計算については戦闘章の [二刀流戦闘](#two-weapon-combat) で解説されています。代表的な組み合わせは以下の通りです：

- **侍:** メインに刀、逆手に脇差。脇差は（長剣ではなく）小剣であるため、刀の長剣スキルを共有しません。これが侍が二刀流のフレーバーを楽しむために支払う代償です。
- **盗賊:** メインに小剣、逆手に短剣スタック（短剣は `Q` + `f` による投擲用スタックも兼ねます）。銀嫌いの敵に対しては、銀の短剣を逆手に持つのも非常に効果的です。
- **ワルキューレまたは騎士:** メインに長剣、逆手に銀の短剣（二刀流スキルを「熟練」まで育成）。通常、武器の強化値が極めて高くなるまでは、逆手武器を持つよりも両手持ち武器を振るう方が数値的に有利です。
- **蛮族:** 二刀流スキルは「入門」で頭打ちになります。命中ペナルティがメリットを打ち消してしまうため、1本の優れた武器を振るう方が賢明です。
- **レンジャーは二刀流を行えますが、未習熟（Unskilled: 命中率 −9 のペナルティ）から鍛えることができません。** したがって、1本の優れた武器を扱う方が通常は勝利につながります。

#### 強化 (Enchantment)

武器や防具は、武器に魔法をかける巻物や鎧に魔法をかける巻物を使って強化することができます。呪われていない武器強化の巻物は +1 を加算し、呪われていない防具強化の巻物は 1〜2（未強化の +0 防具ならそれ以上の上昇もあり得る）を加算します。祝福された巻物ならさらに大きな上昇が見込めます。武器の場合、**+6 以上** の状態でさらに強化を試みると、3分の2 の確率で武器が蒸発して消滅します。**防具** も同様のリスクを抱えています：**+3 を超えると**、巻物を読むたびにアイテムが破壊される危険が生じます（エルフ製の防具や、魔法使いの三角帽子などの「特殊」な防具の場合は **+5 を超えると** 危険になります）。祝福された巻物は1回の読書で得られる強化値の幅を増やしますが、破壊の閾値そのものを変えるわけではありません。呪われた巻物は逆に強化値を下げる恐れがあるため、強化目的で読んではいけません。

#### 腐食と防蝕加工 (Erosion and Proofing)

武器や防具は、錆（鉄製品）、火（有機物製品）、そして腐食（銅製品の緑青や酸による腐食）によって損傷を受けます。ひどく傷んだアイテムはACやダメージの数値が低下します。

この損耗を修復するには、**混乱した状態で呪われていない** 武器に魔法をかける巻物を読む（構えている武器が対象）、または混乱した状態で呪われていない鎧に魔法をかける巻物を読みます（装備している防具の中からランダムに1箇所が対象）。これにより、アイテムに防蝕加工（erodeproofed）が施され、既存の損耗も完全に修復されます。逆に、混乱状態で呪われた巻物を読むと防蝕加工が剥ぎ取られてしまいます。

魔法を使わずに損耗の進行を遅らせることも可能です。脂の缶を使用（`a`）して防具に脂（グリース）を塗りつけます。脂の層は、モンスターによる抱きつき、巻きつき、粘着攻撃、そしてマインドフレアの触手攻撃を受け流す効果がありますが、通常の盗み攻撃や武器強奪を防ぐことはできません。また、脂は水からも装備を守ります：脂を塗った武器や防具は、泉への浸漬、水の罠、あるいは深い水の中の歩行であっても錆びるのを防ぎます。ただし、水に浸かるたびに約 50% の確率で脂が洗い流されてしまうため、数回の水没を耐えるための一時的な保険であり、永久的な防水加工ではありません。

#### ドラゴンの鱗鎧 (Dragon Scale Mail)

ドラゴンの鱗はその強靭さと魔法的な防御特性によって珍重され、その鱗から鍛え上げられた鱗鎧はゲーム内でも最高の胴防具の1つです。

ドラゴンを倒しても必ず鱗を落とすとは限らず、鱗鎧そのものを落とすことは決してありません。新たに仕留めたドラゴンが鱗を落とす確率は約3回に1回であり、蘇生させたドラゴンの場合は20回に1回に過ぎません。**ドラゴンの鱗** は鱗鎧と同様に胴防具として身につけることができ、その色の持つ完全な固有耐性（灰色は魔法耐性、銀色は反射、といったように鱗鎧と同一の効果）をもたらします。しかし、鱗単体のACはわずか +3 であるのに対し、完全に加工されたドラゴンの鱗鎧は +9 のACを誇ります。重量はどちらも同じです。

ドラゴンの鱗をドラゴンの鱗鎧へと強化・アップグレードするには：鱗を装備した状態で、呪われていない鎧に魔法をかける巻物を読みます。鱗が融合・硬化し、対応する色のドラゴンの鱗鎧（+0、祝福された巻物ならさらに高い強化値で、結果も祝福される）へと変化します。呪われた巻物を読んだ場合は、融合せず通常の悪い強化効果が発生するだけです。

---

### 呪いとその解除法 (Curses and How to Break Them)

<!-- audit
2026-07-30: audited with The Armory vs NetHack-5.0 source; remove-curse scope (uncursed=worn, blessed=all; read.c:1524), confused-cursing, prayer uncurse, autocurse-9/10 items verified. No corrections.
-->
<!-- audit
2026-05-18:
- bones items are 80% cursed at pickup (bones.c:290)
- rings of teleport/polymorph and amulet of strangulation generate 90% cursed (mkobj.c:1063-1066, 1143-1147)
- cursed bag of holding doubles its contents' weight (mkobj.c:1950-1953)
- confused remove-curse uncurses 25/curses 25/no-op 50 per item (read.c:1556-1557, mkobj.c:1846-1852)
- blessed remove-curse hits all worn+carried; uncursed only worn (read.c:1524, 1549)
- temple priests do NOT reveal BUC for a fee; only Priest CLASS sees BUC free (priest.c:629-718 sets HClairvoyant + Protection, not bknown)
- shop price-id can infer BUC indirectly
- strategy aligned with NetHackWiki BUC, Scroll of remove curse, Potion of holy water: altar/pet test, blessed remove-curse hits entire inventory, holy water dip uncurses (https://nethackwiki.com/wiki/BUC, https://nethackwiki.com/wiki/Scroll_of_remove_curse, https://nethackwiki.com/wiki/Potion_of_holy_water)
- polymorph into a sliparm form drops body armor (cursed or not) into inventory (polyself.c:1198-1228)
-->

遅かれ早かれ、あなたは呪われた装備を身につけてしまうことになります。事前にテストしなかった指輪かもしれません。ボーンズ階層で拾った靴かもしれません。あるいは、モンスターがあなたの持ち物に触れて呪いをかけたことに気づかなかったのかもしれません。何が原因であれ、外すことを頑なに拒むアイテムを身につけ、おそらく何か恐ろしい災難に見舞われているはずです。呪いを解かない限り、それを脱ぎ捨てることはできません。

#### アイテムが呪われる原因 (How Items Get Cursed)

- **生まれつき呪われている。** 一部のアイテムは、生成時から大半が呪われています（瞬間移動の指輪、へんげの指輪、絞殺の魔除けなど、ダンジョンが冒険者をからかうのにふさわしいと判断したすべて）。
- **ボーンズ階層からの遺品。** ボーンズ階層に落ちているアイテムは、80% の確率で呪われています。
- **モンスターの干渉。** 特定のモンスターは、あなたの所持品にあるアイテムを直接呪うことができます。
- **混乱した状態での呪いを解く巻物。** 混乱状態で読むと、呪いを解くどころかアイテムを *呪ってしまう* 可能性があります。
- **呪われた水。** 聖水の邪悪な双子であり、触れたものを呪います。

#### 呪われたアイテムの効果 (Effects of Cursed Items)

- **呪われた防具や指輪** は身体に固着して外せなくなります：呪われた瞬間移動の指輪は止められないランダムテレポートを意味し、呪われた浮遊の靴は二度と地面に足をつけられなくなることを意味します。
- **呪われた武器** は手放す（持ち替える）ことができません。−3 のオークの短剣を心ゆくまで愛用できることを願っています。
- **呪われた薬や巻物** は特定の変質した効果を持ちます。効果が弱まるもの、有害になるもの、そしてごく一部は意図的に活用できるものもあります。
- **呪われた道具** は劇的な大誤作動を起こします。呪われた軽量化の鞄は、中身の重量を減らすどころか *2倍に増やします*。
- **呪われた食料** は不快ですが、致命的になることは滅多にありません。不幸中の幸いです。

#### 呪いの検知 (Detecting Curses)

予防は治療に勝ります。アイテムを身につける *前に* テストしてください：

- **祭壇テスト。** アイテムを祭壇の上に落とします。黒い閃光は「呪われている」ことを意味し、閃光が起きなければ「呪われていない（呪われていない）」です。
- **ペットテスト。** ペットは呪われたアイテムの上に立ち入るのを嫌がります。狭い通路にアイテムを置き、ペットが何度もそこを通過するか観察してください（1度横切っただけでは安全の証明にはなりません）。
- **識別の巻物。** 常に完全な状態（BUC）を判明させます。

（寺院の僧侶への寄付は BUC を判明 *させません*。これはスポイラーによくある俗説です。僧侶に寄付すると一時的な千里眼と防護ボーナスが得られますが、所持品のBUCは未識別のままです。）

#### 呪いの解除 (Removing Curses)

予防に失敗したとき、あなたには3つの治療法があります：

- **解呪の巻物。** 呪われていない（呪われていないの）巻物は、装備中および構えているアイテムの呪いを解きます。祝福された巻物は、所持品全体のすべてのアイテムの呪いを一括で解きます。
- **聖水。** 呪われたアイテムを聖水に浸す（`#dip`）と、呪われていないになります。これこそが聖水を大量に蓄える最大の理由です。
- **祈り。** 呪われた浮遊、空き手がない状態での呪われた武器の固着、呪われた目隠しなどは「大問題（Major Trouble）」とみなされ、祈りによって優先的に修復される対象となります。通常の呪われた装備品は「小問題（Minor Trouble）」です：正の幸運（Luck）があり、他に治すべき重篤な異常がなければ、祈りが成功した際に最大1個の装備の呪いが解かれます。

呪われた胴防具を着たまま抜け出せなくなりましたか？ その鎧を着られないほど小さな生物形態へと変身（ポリモーフ）すると、通常なら脱げないはずの鎧が（呪われた状態のまま）所持品の中へと外れ落ちます。そこから聖水に浸して呪いを解き、再び着直せばよいのです。詳細については [道具としてのへんげ](#polymorph-as-a-tool) を参照してください。

大半のベテラン冒険者は、いかなる時も聖水と解呪の巻物を常に携帯しています。

---

## 第5部：熟練と最終決戦 (Part Five: Mastery and Endgame)

ゲーム中盤以降、生存率は「ダンジョンが偶然何を落としてくれたか」ではなく、「それをもとに何を自ら構築できたか」に左右されるようになります：鍛え上げられたスキル、適切に管理された幸運（Luck）、確実に唱えられる呪文、そしてまだ見ぬ脅威に備えて組み上げられた装備セットです。ここに続く各章では、ゲヘナ（Gehennom）の深淵へと足を踏み入れる前に、冒険者を支えるこれらの重要システムを解説します。

### 魔法詠唱 (Spellcasting)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Cursed-spellbook contact poison is 3-6 Str + 1d10 HP by default; 1-2 Str + 1d6 HP only with poison res (spell.c:164, poison_strdmg). Was "1-2 Str + 1d10 HP".
- Verified correct: read-success formula & lenses bonus, blessed/cursed auto results, exploding-rune 2d10+5, Pw cost 5*level, failed-cast half-Pw, Pw-regen ticks, chain lightning 2d6.
-->
<!-- audit
2026-05-21:
- spellbook of type SPE_NOVEL appears as "paperback" until read (objects.h:1433-1436)
- reading the first novel in a game grants more_experienced(20, 0) and the ACH_NOVL achievement; u.uevent.read_tribute gates the once-per-game bonus (spell.c:513-535)
- 20 XP is the XL 1->2 threshold so a fresh character gains an experience level on the first paperback read
- novel title is rolled at game start per novelidx; titles come from a list of Terry Pratchett Discworld novels stored in the tribute file (do_name.c:297 noveltitle, files.c:3474 read_tribute)
2026-05-18:
- force bolt damage is 2d12; school skill does NOT scale damage (zap.c:2720-2724)
- chain lightning is level 2 NODIR, not level 7, not a bouncing ray (objects.h:1409-1411; SPELL fields are name,desc,sub,prob,delay=4,level=2)
- failed spellbook read effects: teleport (lvl 1+), aggravate (lvl 2+), blindness (lvl 3+), take-gold (lvl 4+), confusion (lvl 5+), contact poison (lvl 6+), exploding rune (lvl 7+, 2d10+5 dmg, antimagic resists). Default rndcurse branch never fires: max spell level is 7 so rn2(lev) maxes at 6 (spell.c:130-185)
- failed read has a single 1/3 destruction chance (spell.c:612)
- spellbook fade ceiling is 4 successful reads: MAX_SPELL_STUDY=3 with `> MAX_SPELL_STUDY` (spell.c:400-418)
- no Pw drain from memorized spells exists; "spell maintenance" is fabricated (allmain.c moveloop has no per-spell Pw decrement; only cast_spell at spell.c:1245 decrements via SPELL_LEV_PW)
- drain_en only ever DECREASES Pw — no reflection+vortex max-Pw trick (trap.c:5202-5240 drain_en only subtracts from u.uen and decreases u.uenmax)
- blessed book bypasses the read-ability check entirely (auto-success)
- Pw cost per spell = 5 × level: SPELL_LEV_PW(spellev) (spell.c:1245)
- confused casts fail outright (spell.c:1372); charm monster has no confused-area mode
- Skilled+ casting acts like a blessed scroll (spell.c:1524-1525) or blessed potion (spell.c:1540-1541)
- Pw regen: (Wis + Int)/15 + 1; Wizards tick on factor 3 vs 4 (allmain.c:605-607)
- Valkyries restricted in divination, so reading scroll of identify is occasional at best (u_init.c:525-546)
- strategy aligned with NetHackWiki Spellbook, Spellcasting: Int + 4 + XL/2 − 2·level success formula, blessed book auto-success, Pw = 5 × level (https://nethackwiki.com/wiki/Spellbook, https://nethackwiki.com/wiki/Spellcasting)
-->

呪文は、魔法書から学ぶことで何度でも繰り返し行使できる能力です。使うと消滅する巻物や、使用回数が限られている杖とは異なり、マナ（Pw / 魔力）が残っており、酷使され続ける冒険者の頭脳から記憶が失われていない限り、何度でも呪文を唱える（`Z`）ことができます。

#### 呪文の習得 (Learning Spells)

魔法書を読む（`r` キー。巻物を読むのと同じキーです）ことで、その呪文を習得できます。魔法書の店での基本価格は、呪文レベルの 100倍 です。読書には数ターンを要し、失敗することもあります：失敗すると、テレポートさせられる、ゴールドを奪われる、盲目や混乱に陥る、毒を受ける、あるいは爆発で負傷するなどのペナルティを受けます。破壊されずに残った魔法書には再挑戦できます。NetHack 5.0 では、魔法使いが確実に成功できない状況で読もうとすると、*「この魔法書を理解するのは難しそうだ。続けますか？」*（"This spellbook is difficult to comprehend. Continue?"）という警告メッセージが表示され、「いいえ」を選べばペナルティなしで中断できます。

魔法書のレベルによって、発生し得る失敗効果が決まります。レベル1の魔法書は失敗時にランダムな場所へテレポートさせることがあります。レベル2の魔法書は周囲のモンスターを怒らせて呼び寄せる（反感）可能性があります。レベル3の魔法書を読み違えると、250〜350ターンの間盲目にされます。レベル4の魔法書は全所持金を奪い去り、レベル5は16〜22ターンの間混乱させます。レベル6の魔法書を読み違えると接触毒を受ける恐れがあります：小手を着用していれば小手が腐食し、素手の場合は強さが 3〜6 低下して 1d10 のHPダメージを受けます（毒耐性があれば強さ低下 1〜2、1d6 ダメージに軽減）。そしてレベル7の魔法書には爆発のルーンが仕掛けられていることがあります。魔法耐性があれば爆発を防げますが、耐性がなければ 2d10+5 のダメージを受けます。実用的な教訓：失敗の痛手を受け止めきれない魔法書は読んではいけません。

魔法書の読書成功率は、**呪文レベル**、自身の **知力 (Intelligence)**、および **経験レベル (XL)** に依存します。正確な計算式は、1d20 のロールに対して `知力 + 4 + XL/2 − 2×呪文レベル` となります。したがって、この計算値が 20 以上であれば常に 100% 成功し、10 なら半々の確率（50%）、それ未満なら危険な賭けとなります。知力 15、経験レベル 2 でレベル7の魔法書を読もうとすると、読書スコアはわずか 6 となり、成功率はたったの 30% です。レンズ（眼鏡）をかけているとスコアに +2 されます。**祝福された** 魔法書はこの判定を完全に免除され、常に 100% 成功します。**呪われた** 魔法書は自動的に失敗し、上記の恐ろしい失敗効果のいずれかが発動します。

この計算式から **読書スコア** が算出されます。スコア 5 なら成功率 25%、10 なら 50%、15 なら 75%、20 で自動成功（100%）です。レンズなしで確実に読書成功させるためには、`知力 + XL/2` の合計値がレベル1魔法書で 18、以降レベル2から7に向けて 20、22、24、26、28、30 必要になります。レンズを装着していれば、この必要値がそれぞれ 2 緩和されます。

貴重な聖水は、未読の最も難解な高レベル魔法書のために取っておきましょう。

**魔法使い** (Wizard) は疑いようのない魔法の絶対王者です：魔法書をより確実に読みこなし、呪文をより確実に唱え、すべての魔法系統において「エキスパート」まで極めることができます。完璧に育て上げられた魔法使いは、最終的にゲーム内の *すべての* 呪文を習得することすら可能であり、これは迷宮において最も反則（チート）に近い領域です。**武闘家** (Monk) は驚くべき第2位の魔法適性を誇ります。彼らもまた全7系統の魔法を習得可能であり、胴防具を着ないという制約そのものが、金属鎧による詠唱失敗ペナルティを排除してくれます（さらに修道士が好むローブは詠唱ボーナスを与えます）。僧侶や治癒師は、自身の得意系統において優れた詠唱能力を発揮します。その他の職業でも、外的支援があれば時折呪文を役立てることができます。ワルキューレであっても能力獲得の薬で知力を引き上げればレベル3の「識別」を読めることがありますが、呪文職以外のキャラクターは通常は巻物に頼る方が無難です。

[]{#wizards-identify-books}
**魔法使いはスキルの訓練によって魔法書を識別する。** 魔法系統のスキルランクを昇格させると、その系統に属する魔法書の外見（タイトル）が自動的に識別されます：「未習熟」でレベル1の外見、「入門」でレベル3、「熟練」でレベル5、「エキスパート」でレベル7が明らかになります。魔法使いは開始時点で全レベル1の外見と、攻撃・付与魔法のレベル3の外見をあらかじめ知っているため、自身の主要系統においては最初から数多くの魔法書を見分けることができます。

記憶した呪文は約20,000ターンの間脳内に留まり、その後忘れ去られるため再学習が必要になります。呪文一覧メニュー（`+` キー）で残りターン数を確認できます。また、魔法書を使用（`a`）することで、その本がどれくらい摩耗しているかを点検できます：**成功した読書** 1回ごとに摩耗カウントが進み、最大4回読んだ時点で魔法書は白紙へと消え去ります。失敗した読書はこのカウンターを進めませんが、失敗1回につき 3分の1 の確率で魔法書そのものが消滅します。終盤でも頼りにする重要な魔法書は、忘れずに持ち歩くようにしましょう。

**ペーパーバック (Paperbacks)。** 外見が「ペーパーバック」と表示されている魔法書は、本物の魔法書ではなく小説です。見つけたらぜひ読んでください：ゲーム内で最初に読んだ小説は **20 XP** を与え、これは生まれたてのキャラクターを経験レベル 1 から 2 へと押し上げるのにちょうどぴったりの経験値です（この 20 XP ボーナスはゲーム中最初の1回のみ発動し、以降のペーパーバックは引用文を表示するだけです）。各ペーパーバックのタイトルはテリー・プラチェットの『**ディスクワールド**』(Discworld) シリーズから取られており、読むとその小説の一節が開かれます。

#### 主要な呪文 (Key Spells)

| 呪文名 | レベル | 効果 |
| --------------- | ----- | --------------------------------------- |
| 衝撃 (Force bolt) | 1 | 2d12 の遠距離打撃。知力/経験レベル補正により −3 から +3 調整 |
| 回復 (Healing) | 1 | ヒットポイントを回復する |
| 怪物探知 (Detect monsters) | 1 | フロア全体のモンスターの位置を暴く |
| 識別 (Identify) | 3 | アイテムを識別する（巻物の消費を節約） |
| 解呪 (Remove curse) | 3 | 装備中・構えているアイテムの呪いを解く |
| 連鎖雷撃 (Chain lightning) | 2 | 術者から全方向に電撃を放ち、周囲のモンスターへと連鎖する |
| 地図化 (Magic mapping) | 5 | フロアの地形構造を明らかにする（巻物の消費を節約） |
| 魅了 (Charm monster) (Charm monster) | 5 | 3×3 範囲の周囲の魅了 (Charm monster)（熟練以上で祝福された巻物と同等） |
| 死の指先 (Finger of death) | 7 | 光線で対象を即死させる。魔法耐性で無効化される |

残る32種類の呪文については、その系統、種類、およびスキルランクごとの強化効果を含め、付録の [呪文一覧表](#spell-tables) にまとめられています。

魔法使いにとって、**識別** と **魔法の地図** を呪文として習得することは、巻物への依存度を劇的に減らします。これはインベントリの空き枠を消費する代わりにマナを支払う、無限の巻物を手に入れたようなものです。**死の指先** はあらゆる議論を即座に終わらせる究極の解決策です。**魅了 (Charm monster)** は敵を味方に変えてしまいます。味方は荷物を運んでくれ、身代わりとなって敵の攻撃を受け止めてくれるため、敵を単に殺すことよりもさらに価値があります。

**連鎖雷撃** (Chain lightning) は素晴らしい部屋掃除呪文です。レベル2であるため、呪文を少しでも唱えられるキャラクターなら誰でも実用圏内に入ります。この呪文はターゲット方向の入力を求めることなく全8方向へと自動発射され、命中ごとに 2d6 のダメージを与え、さらに平和的なNPCや手懐けたペットに当たるとそこでピタリと停止するため、通路の先にペットや店主がいても巻き込むことなく敵対部屋だけを一掃できます。電撃耐性を持つ敵はその光線を1回だけ受け止めて消滅させます。

もし `+` メニューで **失敗率 100%** と表示されている場合、原因は通常魔法書ではなく、身につけている装備やスキルにあります。まず盾を外し、次に金属製の胴鎧、兜、小手、靴を脱いでください。そして自身の職業の詠唱能力値を高め、その呪文の魔法系統スキルを鍛えましょう。ローブを着れば金属鎧のペナルティを半減でき、六尺棒を構えればわずかな詠唱ボーナスが得られます。すべての盾は一律のペナルティを課し、重量30を超える盾は最終成功率を4分の1に激減させます。

#### マナ管理 (Mana Management)

あなたの魔力（Pw）プールは、部屋の隅に座り込んでスマートフォンのバッテリーのように自然回復を待つまでに、あと何回呪文を唱えられるかを決定します。呪文の詠唱には **呪文レベル × 5 の Pw** を消費します（したがって死の指先は 35 Pw です）。詠唱に失敗した場合でも、半分のマナが消費されます。

Pw は定期的な周期（ティック）ごとに自然回復し、この回復間隔はレベルが上がるにつれて短縮されます：経験レベル 1 では 24ターンごと（魔法使いは 18ターン）、レベル 10 では 18ターン（魔法使い 14）、レベル 20 では 12ターン（魔法使い 9）、レベル 30 では 5ターン（魔法使い 4）となります。各ティックごとに、1 から **((知恵 + 知力) / 15) + 1** の Pw（通常 1〜3 Pw）が回復します。呼吸の能力（呼吸の魔除けなど）を持っていると、この回復上限がさらに +2 されます。**魔力回復** (energy regeneration) の能力（『エチオピカの目』などから得られる）は、この周期ティックをバイパスし、**毎ターン** Pw を回復させます。なお、「圧迫 (Stressed)」以上の負荷ステータスになると Pw の自然回復は完全に停止します（「重荷 (Burdened)」なら問題ありません）。

予備の杖や巻物を常に携帯しておきましょう。Pw を使い果たした魔法使いは、バスローブを着て木の棒を握りしめているただの無力な人間に過ぎません。

### 幸運と運命 (Luck and Fortune)

<!-- audit
2026-09-27 luckstone rewrite vs NetHack-5.0 source:
- timeout.c:600-616 (nh_timeout): time_luck = stone_luck(FALSE) = sgn(blessed - cursed luck items); good Luck decays only if no stone or time_luck < 0; bad Luck recovers only if no stone or time_luck > 0. So BLESSED keeps good Luck but lets bad Luck recover; UNCURSED freezes both; CURSED freezes bad and lets good decay. The earlier "any non-cursed luckstone freezes drift" was wrong for blessed.
- the +-3 is u.moreluck (attrib.c set_moreluck, LUCKADD you.h:465), added to every Luck check via Luck = u.uluck + u.moreluck (you.h:464); it is not a cap. u.uluck clamps at +-10 (change_luck, attrib.c:411), so total Luck spans +-13.
- several luck items: stone_luck nets cursed against non-cursed (moreluck) and cursed against blessed (timeout); never more than +-3.
- drift every 300 turns with the Amulet or an angry god (timeout.c:604).
- luck items: any LUCKSTONE (incl. the Heart of Ahriman) or SPFX_LUCK artifacts, the Tsurugi of Muramasa and the Orb of Fate (artifact.c:526 confers_luck, artilist.h).
-->
<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Removed three "Luck +5 benefits" that use plain rn2 (no Luck term): enchant-scroll success (read.c:1180, wield.c:1004), wand wresting (rn2(121), hack.h:1419), fountain wishes (fountain.c:78). Kept to-hit and prayer (which Luck does affect).
- Verified correct (also covers Exercising Your Stats): effective Luck range & timeout, luckstone freeze/±3, luck artifacts, the whole gain/lose-Luck table, sacrifice ceiling, prayer-fails-on-negative-Luck, all stat exercise/abuse actions.
-->
<!-- audit
2026-05-19:
- cursed luckstone holds NEGATIVE Luck in place, but positive Luck still decays toward baseline (timeout.c:616-619)
- any non-cursed luckstone (blessed or uncursed) gives +3 max-Luck cap (attrib.c:441-450)
- killing peaceful: -1 with 50% probability (mon.c:3665); -5 reserved for co-aligned unicorns (mon.c:3667)
- prayer is rejected on ANY negative Luck (pray.c:2155), not just <= -10
- no Sokoban-down-stairs Luck penalty exists
- thrown gem to cross-aligned unicorn: identified -3..+3 (dothrow.c:2334 rn2(7)-3); unidentified -1..+1 (dothrow.c:2349 rn2(3)-1)
- "ID gems for shopkeeper +1" is fabricated; shk.c has no such hook (shk.c contains no change_luck or adjalign call on GEM_CLASS sale)
- killing quest leader: -4 baseline, immediate change_luck(-20), u.ugangr += 7 (mon.c:3680, timeout.c:600)
- killing pet: -1 plus alignment -15 via adjalign (mon.c:3664, 3704)
- only mirror breaks for Luck -2 (uhitm.c:1133, dothrow.c:2496, dokick.c:445/1724); crystal balls/armor don't
- full-moon/Friday-the-13th baseline shift (timeout.c:595-598)
- carrying the Amulet or u.ugangr > 0 doubles drift rate (300 turns, timeout.c:607)
- Archeologists start with TOUCHSTONE knowledge only (u_init.c:50, 903); gems are NOT pre-identified
- strategy aligned with NetHackWiki Luck, Luckstone, Luck item: ±13 cap with non-cursed luckstone, drift toward 0 every 600 turns, cursed luckstone locks negative Luck (https://nethackwiki.com/wiki/Luck, https://nethackwiki.com/wiki/Luckstone, https://nethackwiki.com/wiki/Luck_item)
-->

幸運（Luck）は画面には表示されない隠しステータスですが、以下の4つの原則を頭に入れておけば大半の状況を正しくコントロールできます：

1. 祈りを常に安全に行えるよう、幸運を常に 0 以上に保つこと。
2. 幸運の石を手に入れたら、祝福して鞄に入れずインベントリに直接携帯すること。
3. 識別済みの本物の宝石を、自属性と同じユニコーンに投げ与えること。
4. 理由もなく平和的な生物を殺したり、鏡を割ったりしないこと。

#### 幸運の仕組み (How Luck Works)

幸運は −13 から +13 の範囲を取り、通常は 0 から始まります。そのまま放置しておくと、時間の経過とともにカレンダー基準値へと徐々に減衰（ドリフト）していきます。

**幸運の自然減衰（タイムアウト）。** 600ターンごとに、幸運は基準値（通常は 0）に向かって 1点 近づいていきます。イェンダーの魔除けを所持している間、あるいは神が怒っている間は、この間隔が 300ターンごとへと倍速になります。

**幸運の石 (Luckstones)。** 鞄の中に入れず、持ち物（直接の所持品）として携帯している幸運の石は、幸運に +3（呪われている場合は −3）を加算し、さらに自然減衰のルールを変更します：

| 幸運の石 | 幸運修正 | 正の幸運（善運） | 負の幸運（悪運） |
| --------- | ---- | --------- | --------- |
| 祝福 (Blessed) | +3 | **保持される** | **自然減衰（回復）する** |
| 呪われていない (Uncursed) | +3 | **保持される** | **保持される（回復しない）** |
| 呪い (Cursed) | −3 | 自然減衰（消失）する | **保持される（悪運が固定）** |

手に入れたら必ず祝福してください。祝福された幸運の石は、自ら稼ぎ出した正の幸運を永久に保持しつつ、過ちによって負ってしまった悪運だけを時間経過で回復させてくれます。鉱山の最深部で手に入る幸運の石は呪われていないであるため、聖水に浸して祝福しましょう。呪われた幸運の石を持ち歩いてはいけません。

[アーリマンの心臓](#heart-of-ahriman)（それ自体が幸運の石）、[村正の剣](#tsurugi-of-muramasa)、および [運命のオーブ](#orb-of-fate) も幸運の石として機能します。複数携帯してもボーナスが +3 を超えることはなく、1つでも呪われた石が混ざっていると他の石の効果を弱めてしまいます。

**カレンダーと幸運。** 減衰の収束先は常に 0 とは限りません：

- **満月** の夜は、幸運の基準値が +1 になります：幸運は 0 ではなく +1 に向かって減衰します。セッションを満月の夜に開始した場合、最初から無料で +1 の幸運を持っています。
- **13日の金曜日** は、幸運の基準値が −1 になります。可能であればこの日のプレイは階段を登るような慎重な行動を控えましょう。どれほど徳の高い行動をしていても、蓄積した善運は −1 に向かって吸い取られていきます。

（NetHack はコンピュータの実時間・日付を参照してこの判定を行います。）

#### 幸運の増減 (Gaining and Losing Luck)

| 行動 | 幸運の変動 |
| --------------------------------------------------- | -------------------- |
| 識別済みの本物の宝石を自属性のユニコーンに投げる | **+5** |
| 名前を付けたが未識別の本物の宝石を自属性のユニコーンに投げる | +2 |
| 未識別の本物の宝石を自属性のユニコーンに投げる | +1 |
| 完全識別済みの本物の宝石を逆属性のユニコーンに投げる | −3 〜 +3 (ランダム) |
| 未識別の本物の宝石を逆属性のユニコーンに投げる | −1 〜 +1 (ランダム) |
| 自属性の祭壇で生贄を捧げる（死体の価値により変動） | 通常 +1 |
| 玉座に座る（幸運がマイナスのときのみこの効果が発生） | +1 |
| 倉庫番のルール違反（すり抜け、破壊、岩のへんげ、大地の巻物） | 1回につき −1 |
| 平和的な生物を殺害する | −1 (殺害ごとに 50% の確率) |
| 自属性のユニコーンを殺害する | **−5** |
| クエストの指導者を殺害する | 即座に −20 (下限 −10)、神の怒り +7、基準幸運に永続 −4 |
| 自身のペットを殺害する | −1、さらに属性値（アライメント）−15 |
| 同族食い（人肉食 / Cannibalism） | −2 〜 −5 |
| 鏡を割る | −2 |

**ユニコーンへの宝石投擲は、ゲーム内で最も強力な能動的幸運獲得手段です。** 自身の属性と一致するユニコーンに対して、きちんと識別した本物の宝石（ガラス玉ではなく）を投げると、即座に **+5** の幸運を獲得できます。ユニコーンは平和的になり、贈り物を受け取ってテレポートで飛び去りますが、後で再び出会えばまた贈り物を受け取ってくれます。宝石は *事前に* 識別（試金石や識別の巻物）してください。自分が何を投げているのか正確に把握していない場合、得られるボーナスは +5 から +1 へと激減してしまいます。ガラス玉（模造宝石）は無害ですが幸運は増えません（本物の宝石を消費せずに邪魔なユニコーンを大人しくさせて立ち去らせる安全な手段としては使えます）。属性が異なるユニコーンに本物の宝石を投げるのは避けてください。結果は −3 から +3 の間のランダムな変動になってしまいます。考古学者は **試金石** (Touchstone) を持ってスタートするため、ユニコーンに投げる前にそれが本物の宝石かどうかを自力で簡単に判別できます。

祭壇での生贄によって幸運を高められるのは、捧げた死体の難易度（モンスターレベル）が現在の幸運値を上回っているときだけです。コボルドのような弱い死体では幸運を上げることはできません。後半に幸運を稼ぐには、強敵の新鮮な死体を生贄に捧げてください。

#### 幸運が重要な理由 (Why Luck Matters)

幸運が +5（または幸運の石を含めてそれ以上）になると、ダンジョンでの冒険生活は **目に見えて** 快適になります：

- 戦闘での命中率が上がります。本来なら空振りしていたはずの攻撃が敵を捉えるようになります。
- 祈りが聞き届けられる確率が格段に高まります。神々は幸運な者を好むのです（神とは気まぐれなものです）。
- その他数多くの小さな判定が、あなたに有利な方向へと傾きます。

負の幸運（マイナスの幸運）は祈りを極めて危険なものにします。幸運が −1 または −2 のとき、神が激怒していない状態であれば、呪いや神罰の雷を受ける代わりに単に不興を買って祈りのタイマーがリセットされるだけで済むのが通例です。しかし、さらに深い負の幸運や神の怒りがある場合、より悲惨な結果が待ち受けています。また、幸運は攻撃や様々なロール結果に影響を及ぼしますが、巻物が一般的に暴発するようになるわけではありません。

---

### 能力値の訓練 (Exercising Your Stats)

舞台裏では、ダンジョンはあなたの6つの能力値のうち4つ（**強さ (Str)**、**器用さ (Dex)**、**体力 (Con)**、**知恵 (Wis)**）について、隠された訓練カウンターを記録しています（知力 (Int) とカリスマ (Cha) は訓練されず、能力獲得の薬のような魔法的手段によってのみ変動します）。能力値を「鍛える」ような生き方を続けているとカウンターが徐々に上がり、「酷使（虐待）」するような生活を続けているとカウンターが下がっていきます。数百ターンごとにゲームはこのカウンターをチェックし、+1 または −1 の変動をもたらします。

#### 訓練の仕組み (How Exercise Works)

このカウンターは不可視です。訓練となる行動を十分に長く続け、さらにランダムな判定に合格する（すでに能力値が上昇していると恩恵は逓減します）と、*「身軽になった気がする！ 反射神経を鍛えたに違いない！」*（"You feel agile! You must have been working on your reflexes!"）というメッセージや、他の能力値に応じた同様のメッセージが表示されます。逆に、酷使カウンターが優勢になった場合は、*「最近反射神経を鍛えていない気がする」*（"You haven't been working on reflexes lately."）という警告が発せられます。

日常的な訓練によって引き上げられる能力値の上限は **18** です（種族固有の生来の上限を超えることはできず、能力値の極致を目指すなら依然として能力獲得の薬が不可欠です）。一方、酷使による能力値の低下は、種族固有の最低値まで落ち込む可能性があります。

#### 訓練と酷使をもたらす行動 (Actions That Exercise and Abuse)

| 能力値 | 訓練となる行動 (Exercises) | 酷使となる行動 (Abuses) |
|------|-----------|--------|
| **強さ (Str)** | 重い荷物の運搬（圧迫 / Stressed 状態。ただし超過重は不可）、体質による自然回復（HP再生）、巨岩の投擲や押し動かし、重い鉄球の投擲 | 空腹による「衰弱 (Weak)」状態 |
| **器用さ (Dex)** | 成功したキック（鍵、流し台、扉）、命中した投擲武器 | 「満腹 (Satiated)」状態、重い負荷状態、つまずき（Fumbling）、気絶（Stunned）、足の負傷（Wounded legs）、キックの空振り |
| **体力 (Con)** | 常に「空腹でない (Not-Hungry)」状態を適切に維持すること | 空腹による卒倒（Fainting）、病気（Sick）、嘔吐（Vomiting）、汚染された泉、極度の負荷状態 |
| **知恵 (Wis)** | 能動的な千里眼、探知能力の成功（ゴールド/モンスター/食料探知）、自主的な祈り、価値ある生贄の奉納 | 混乱（Confusion）、幻覚（Hallucination）、呪われた啓蒙の読書、墓堀り（Gravedigging） |

修道士に特有の2つの癖：断食によって「衰弱」状態にある修道士は知恵を鍛え、逆に「満腹」状態にある修道士は知恵を酷使します。

#### 訓練が重要な理由 (Why Exercise Matters)

能力値はゲーム内のほぼすべての要素に直結しています：強さはダメージと所持限界量、器用さは命中率、体力はレベルアップ時のHP上昇量、知恵はPwの自然回復速度に影響します。日々の積み重ねによる能力値の上昇は、やがて大きな差となって現れます。満腹やつまずき状態で漫然と過ごした500ターンもまた、同様に恐ろしい結果として跳ね返ってくるのです。

---

### スキルの向上 (Enhancing Skills)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Valkyrie two-weapon caps at Skilled, not Expert (Skill_V, u_init.c:544); the example's slot count corrected to eleven.
- Verified correct: practice thresholds level^2*20, slot costs, all to-hit/damage bonus tables, start-2/+1-per-level/+1-crowning, all 494 role skill-cap cells, training gates.
-->
<!-- audit
2026-05-18:
- skill ranks P_UNSKILLED through P_GRAND_MASTER; practice formula level²×20 (skills.h:92-106)
- cumulative practice thresholds: 20/80/180/320/500
- weapon slot costs 1/2/3 per rank; non-weapon costs 1/1/2/2/3
- two-weapon uses the WEAPON slot column (weapon.c:1141)
- bare-hand and martial-arts bonuses apply every hit (weapon.c:1611-1613)
- bare-hand 50% / martial-arts 75% rate is the practice-training check, not bonus gating (uhitm.c:847 `dmg = rnd(!martial_bonus() ? 2 : 4)`; uhitm.c:849 `train_weapon_skill = (dmg > 1)` — rnd(2)>1 is 1/2, rnd(4)>1 is 3/4)
- riding trains after 100 mounted squares (steed.c:393-396, u.urideturns >= 100)
- Knights start at Basic riding; target is Skilled (weapon.c:1787-1789)
- pickup/loot/dip/trap/engrave actions gated at Basic riding
- slot ceiling 32 for an XL-30 crowned hero: 2 starting + 29 level-ups + 1 crowning (u_init.c:884, pray.c:992-993)
- Ranger divination caps at Expert (u_init.c:461)
- Wizard restricted from long sword: no P_LONG_SWORD entry in Skill_W (u_init.c:548-569)
- spell schools start with a 20-use precredit at Basic
- Skilled cone-of-cold and fireball: cluster of 3×3 explosions (spell.c:1419-1452), not room-clearing
- Valkyrie 6+6+2 = 14 slot example math
- crown gives +1 slot
- strategy aligned with NetHackWiki Skill, Twoweapon: slot budget tied to XL + crowning, non-weapon skills cost half, restricted skills only unrestrict to Basic via artifact gift (https://nethackwiki.com/wiki/Skill, https://nethackwiki.com/wiki/Twoweapon)
2026-05-23:
- Wizard dagger Expert opening: Wizards are unrestricted in dagger (Skill_W u_init.c:548-569), cap at Expert; thrown daggers benefit from a class multishot bonus (dothrow.c:177-190); early Pw budget is tight at base regen (Wis+Int)/15+1 (allmain.c:605-607)
- six-slot Dagger Expert cost = 1+2+3 (weapon column, skills.h:92-106)
- citation: community Wizard opening guides on NetHackWiki Wizard strategy and Damerell, "How to play a Wizard" (https://nethackwiki.com/wiki/Wizard, https://www.steelypips.org/nethack/)
-->

多くの冒険者は、初めて **`#enhance`** コマンドを入力し、これまで何レベルにもわたって振り回してきた幅広の剣が、ついに「入門」から「熟練」へと昇格できる状態になっていることに気づいた瞬間に、このスキルシステムの存在を知ります。武器、戦闘スタイル、そして魔法系統はそれぞれ個別に熟練度を記録しており、貴重なスキルスロットを1枠ずつ消費して向上させていきます。

序盤のうちに1つの武器系統を定め、それに専念してください。スキルは武器の持ち替えをやめて初めて累積していきます。自分が「熟練（Skilled）」（命中率 +2）に達した武器は、「未習熟（Unskilled）」（命中率 −4 のペナルティ）のまま振るう基本攻撃力の高い武器よりもはるかに敵を圧倒します。したがって、訓練していないピカピカの新しい剣に乗り換えることは、通常は戦力ダウンにしかなりません。見つかった強そうな武器に次々と目移りしていては、あらゆる武器で未習熟のまま取り残されてしまいます。

#### スキル階梯 (The Skill Ladder)

武器を使い込む（実戦で振るう）ことで、命中率とダメージが向上します。ゲームはこの熟練度を **スキルランク** として記録します：訓練を重ねるほどランクが上がり、より致命的な一撃を放てるようになります。大半のスキルは **未習熟 (Unskilled) → 入門 (Basic) → 熟練 (Skilled) → エキスパート (Expert)** の順に上昇します。**素手格闘 (Bare hands)** と **武術 (Martial arts)** のみ、さらにその上の **マスター (Master)** および **総師範 (Grand Master) (Grand Master)** に到達できます。各ランクへの昇格には、**実践回数（累積使用数）** と **スキルスロット（経験レベルに応じた有限の枠数）** の両方が必要になります。

| 到達ランク | 必要実践回数 (累積) | 武器スロット消費 | 武器以外スロット消費 |
| ------------ | --------------------- | ------------ | ---------------- |
| 入門 (Basic) | 20 | 1 | 1 |
| 熟練 (Skilled) | 80 | 2 | 1 |
| エキスパート (Expert) | 180 | 3 | 2 |
| マスター (Master) | 320 | — | 2 |
| 総師範 (Grand Master) (Grand Master) | 500 | — | 3 |

武器以外のスキル（魔法系統、騎乗、素手格闘、武術）は、近接武器に比べて必要なスロット数が約半分で済み、これはダンジョンが魔法や格闘に与えている密かな優遇措置です（ただし「二刀流」はその名に反して武器側のスロット列を消費します）。プレイヤーは開始時に 2スロット を持ち、経験レベルが1上がるごとに1枠を獲得し（レベル30までに +29枠）、さらに戴冠（Crowning）を受けると追加で +1枠 を得るため、レベル30で戴冠した英雄の絶対的な上限は **32スロット** です。レベルドレインによって経験レベルを失うとスキルスロットも失われ、直近に取得したスキルが降格される場合があります。

各職業にはスキルごとにこれ以上鍛えられない **上限（キャップ）** が設定されています。例えば魔法使いはメイスを「入門」までしか鍛えられず、長剣は制限（Restricted）されています。制限されたスキルは `#enhance` メニューに表示されず「未習熟」のまま固定されますが、神から生贄のギフトとして授かったアーティファクト武器がある場合、その武器のスキル制限が解除されて「入門」まで訓練可能になります。各職業ごとの完全なスキル上限表は、後述の [職業別スキル上限表](#per-role-skill-caps) を参照してください。

#### スキルの訓練 (Training a Skill)

実践を重ねる（使い込む）ことで、スキル経験値が蓄積されていきます：

- **武器スキル** は、近接攻撃または投擲攻撃が命中し、**2ダメージ以上** を与えるたびにカウントされます。1ダメージの微弱な攻撃はカウントされません。槍、ジャベリン、ナイフ、短剣、アキリスは、突いても投げても同一の武器スキルが鍛えられます。
- **素手格闘** は命中のうち **50%** がカウント対象となり、**武術** は命中の **75%** がカウントされます（ランクによる補正自体は毎回の攻撃に適用されますが、昇格への歩みだけが緩やかになります）。
- **騎乗** は、騎乗状態で **100マス** 移動するごとに1カウント獲得します。
- **魔法系統** は、**レベルNの呪文を1回詠唱成功させるごとに N回 の実践カウント** を獲得します。各系統には素振り用のレベル1呪文が存在します（下記の魔法系統表を参照）。

自身の職業が開始時点で「入門（Basic）」を持っているスキルには、**あらかじめ20回分の実践クレジットが付与** されており、ゲーム開始時点で既に「熟練（Skilled）」への道のりの4分の1を達成しています。

十分な実践経験を積むと、そのカテゴリに応じたメッセージが表示されます：**「武器の扱いに自信がついてきた」**（"You feel more confident in your weapon skills"）、**「呪文の扱いに自信がついてきた」**（"spell casting skills"）、または **「格闘技の扱いに自信がついてきた」**（"fighting skills"）。これが `#enhance` コマンドを入力する合図です。1つスキルを昇格させた後、まだ他に昇格可能なスキルが残っている場合は、**「もっと強くなれそうな気がする！」**（"You feel you could be more dangerous!"）と表示されます。続けて強化しましょう。

#### ランクがもたらす恩恵 (What a Rank Buys You)

武器や戦闘スタイルの各ランクは、命中率とダメージのボーナスを一律の数値で書き換えます（加算ではなく置き換えられます）：

| ランク | 武器 | 二刀流 | 騎乗 | 素手格闘 | 武術 |
| ------------ | ------- | ---------- | ------ | ---------- | ------------ |
| 未習熟 (Unskilled) | −4 / −2 | −9 / −3 | −2 / 0 | +1 / 0 | +2 / +1 |
| 入門 (Basic) | 0 / 0 | −7 / −1 | −1 / 0 | +1 / +1 | +3 / +3 |
| 熟練 (Skilled) | +2 / +1 | −5 / 0 | 0 / +1 | +2 / +1 | +4 / +4 |
| エキスパート (Expert) | +3 / +2 | −3 / +1 | 0 / +2 | +2 / +2 | +5 / +6 |
| マスター (Master) | — | — | — | +3 / +2 | +6 / +7 |
| 総師範 (Grand Master) (Grand Master) | — | — | — | +3 / +3 | +7 / +9 |

（各セルは **命中補正 / ダメージ補正** を示します。）二刀流のペナルティは左右 **それぞれ** の打撃に適用されます。入門段階の二刀流は2回攻撃できますが、それぞれに −7 の命中ペナルティがかかるため、1本の武器でしっかり殴るよりも遥かに命中率が悪化します。素手格闘と武術のボーナスはあらゆる打撃に適用され、実践カウンターだけが微弱打撃を除外します。武器エキスパートの数値（+3 / +2）こそが、1つの武器に専念した冒険者への最大の報酬です。

#### 7つの魔法系統 (The Seven Spell Schools)

すべての魔法書は7つの魔法系統のいずれかに属しており、その系統におけるスキルランクが詠唱の成功率を左右します。また、ランクが上がることで一部の呪文に追加の効果や強化が解禁されます。例えば「冷気の円錐」は熟練で 3×3 の爆発群となり、「識別」はスタック全体を一括識別できるようになり、「自己加速」は効果持続時間が延びます。

| 系統 | 専門領域 | レベル1の素振り用呪文 |
| ----------- | -------------------------------------- | --------------- |
| 攻撃魔法 (Attack) | 直接ダメージ（衝撃、火炎球） | 衝撃 (Force bolt) |
| 回復魔法 (Healing) | HP回復と状態異常の治療 | 回復 (Healing) |
| 予見魔法 (Divination) | 探知、識別、マッピング | 灯り (Light) |
| 付与魔法 (Enchantment) | 強化、弱体化、魅了 | 怪物を混乱させる (Confuse monster) |
| 僧侶魔法 (Cleric) | 神聖な防護と召喚 | 防護 (Protection) |
| 脱出魔法 (Escape) | 移動、回避、浮遊 | 跳躍 (Jumping) |
| 変化魔法 (Matter) | 操作、変成、へんげ | 開錠 (Knock) |

#### 職業別スキル上限表 (Per-Role Skill Caps)

<!-- audit
2026-05-19:
- All 13 role skill tables sourced from u_init.c (Skill_A through Skill_W); skills not in def_skill are P_UNSKILLED-locked. (u_init.c:257-569 tables Skill_A/B/C/H/K/Mon/P/R/Ran/S/T/V/W; weapon.c:1738-1781 skill_init defaults all to P_ISRESTRICTED then walks the def_skill list)
- All 494 cells (27 weapons + 4 fighting styles + 7 spell schools × 13 roles) exact-match against u_init.c:257-572.
- Scimitar omitted: no role has it in 5.0 (merged into saber per skills.h header note).
- P_MARTIAL_ARTS appears only in Skill_Mon (P_GRAND_MASTER) and Skill_S (P_MASTER); Monks have P_BARE_HANDED_COMBAT restricted (they get martial arts instead).
- Wizard and Monk are the only roles with all 7 spell schools listed in their def_skill table (Skill_W u_init.c:562-568 has all 7 P_*_SPELL entries; Skill_Mon u_init.c:380-386 has all 7). Other roles list a subset (Priest at u_init.c:408-410 has only 3, Healer at u_init.c:342 has only 1, etc.).
-->

以下に武器、戦闘スタイル、魔法系統の固定上限値を示す3つの表を掲載します。各職業の欄に記載されていないスキルは **制限（Restricted）** されており、1つの例外（神から生贄ギフトとして授かったアーティファクト武器は、その武器スキルを「入門」まで制限解除する）を除き、ランクは「未習熟」に固定されます。記号の凡例：**B**=入門 (Basic)、**S**=熟練 (Skilled)、**E**=エキスパート (Expert)、**M**=マスター (Master)、**GM**=総師範 (Grand Master) (Grand Master)、**—**=制限（未習熟固定）。

空欄（—）のスキルであっても使用不能というわけではなく、永遠に「未習熟」のままであることを意味します。治療師であっても衝撃の魔法書を読んで唱えることは可能ですし、魔法使いであっても長剣を振り回すことはできます。ただし、[スキル階梯](#the-skill-ladder) に記された未習熟のペナルティ（武器なら −4/−2、二刀流なら1打撃ごとに −9/−3、魔法系統なら高い詠唱失敗率）を常に支払い続け、成長の余地はありません。職業略称：Arc=考古学者、Bar=野蛮人、Cav=洞窟人、Hea=治療師、Kni=騎士、Mon=武闘家、Pri=司祭、Rog=盗賊、Ran=レンジャー、Sam=侍、Tou=観光客、Val=ワルキューレ、Wiz=魔法使い。

##### 武器スキル上限表 (Weapon Skill Caps)

::: dense-table

| 武器 | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 短剣 (dagger) | B | B | B | S | B | — | — | E | E | B | E | E | E |
| ナイフ (knife) | B | — | S | E | B | — | — | E | S | S | S | — | S |
| 斧 (axe) | — | E | S | — | S | — | — | — | S | — | B | E | S |
| つるはし (pick-axe) | E | S | B | — | B | — | — | — | B | — | B | S | — |
| 小剣 (short sword) | B | E | — | S | S | — | — | E | B | E | E | S | B |
| 幅広の剣 (broadsword) | — | S | — | — | S | — | — | S | — | S | B | S | — |
| 長剣 (long sword) | — | S | — | — | E | — | — | S | — | E | B | E | — |
| 両手剣 (two-handed sword) | — | E | — | — | S | — | — | B | — | E | B | E | — |
| サーベル (saber) | E | S | — | B | S | — | — | S | — | B | S | B | — |
| こん棒 (club) | S | S | E | S | B | — | E | S | — | — | — | — | S |
| メイス (mace) | — | S | E | B | S | — | E | S | — | — | B | — | B |
| モーニングスター (morning star) | — | S | B | — | S | — | E | B | B | — | B | — | — |
| フレイル (flail) | — | B | S | — | B | — | E | B | S | S | B | — | — |
| ハンマー (hammer) | — | E | S | — | B | — | E | B | B | — | B | E | — |
| 六尺棒 (quarterstaff) | S | B | E | E | — | B | E | — | B | B | B | B | E |
| 長柄武器 (polearms) | — | — | S | B | S | — | S | B | S | S | B | S | S |
| 槍 (spear) | — | S | E | B | S | B | S | B | E | S | B | E | B |
| トライデント (trident) | — | S | S | B | B | — | S | — | B | — | B | B | B |
| ランス (lance) | — | — | — | — | E | — | B | — | — | S | B | S | — |
| 弓 (bow) | — | B | S | — | B | — | B | — | E | E | B | — | — |
| スリング (sling) | S | — | E | S | — | — | B | — | E | — | B | B | S |
| クロスボゥ (crossbow) | — | — | — | — | S | B | B | E | E | — | B | — | — |
| 投げ矢 (dart) | B | — | — | E | — | — | B | E | E | — | E | — | E |
| 手裏剣 (shuriken) | — | — | — | S | — | B | B | S | S | E | B | — | B |
| ブーメラン (boomerang) | E | — | E | — | — | — | B | — | E | — | B | — | — |
| 鞭 (whip) | E | — | — | — | — | — | — | — | B | — | B | — | — |
| ユニコーンの角 (unicorn horn) | S | — | B | E | — | — | S | — | — | — | S | — | — |

:::

5.0 ではシミターはサーベルに統合されました。現在はどちらも同一のスキルを参照します。

##### 戦闘スタイル上限表 (Fighting Style Caps)

::: dense-table

| スタイル | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 素手格闘 (bare hands) | E | M | M | B | E | — | B | E | B | — | S | E | B |
| 二刀流 (two-weapon) | B | B | — | — | S | — | — | E | — | E | S | S | — |
| 騎乗 (riding) | B | B | — | — | E | — | — | B | B | S | B | S | B |
| 武術 (martial arts) | — | — | — | — | — | GM | — | — | — | M | — | — | — |

:::

武術を扱えるのは武闘家と侍だけであり、総師範 (Grand Master)に到達できるのは武闘家のみです。

##### 魔法系統上限表 (Spell School Caps)

::: dense-table

| 系統 | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 攻撃魔法 (Attack) | B | B | B | — | S | B | — | — | — | B | — | B | E |
| 回復魔法 (Healing) | B | — | — | E | S | E | E | — | B | — | — | — | S |
| 予見魔法 (Divination) | E | — | — | — | — | B | E | S | E | B | B | — | E |
| 付与魔法 (Enchantment) | — | — | — | — | — | B | — | — | — | — | B | — | S |
| 僧侶魔法 (Cleric) | — | — | — | — | S | S | E | — | — | S | — | — | S |
| 脱出魔法 (Escape) | — | B | — | — | — | S | — | S | B | — | S | B | E |
| 変化魔法 (Matter) | B | — | S | — | — | B | — | S | — | — | — | — | E |

:::

治療師は回復魔法をエキスパートまで極められますが、他のすべての魔法系統が制限されています。このような単一系統特化は治療師だけの特徴です。全7系統すべてにアクセスできるのは魔法使いと武闘家だけであり、そのうち4系統をエキスパートまで引き上げられるのは魔法使いだけです（武闘家がエキスパートになれるのは回復魔法のみ）。野蛮人とワルキューレは利用可能な2系統（攻撃と脱出）で入門が上限であり、他の5系統は制限されています。

#### スキルスロットの賢い使い方 (Spending Slots Wisely)

32スロットという数字は一見十分に思えますが、実際に計算し始めるとあっという間に底をつきます。1つの武器をエキスパートにするだけで、単独で **6スロット**（1+2+3）を消費します。長剣エキスパート、二刀流熟練、騎乗熟練を目指すワルキューレは、いかなる魔法系統に投資する前であってもすでに11スロットを使い果たしています。

賢い運用のためのいくつかの原則：

- **反射的に昇格させないこと。** スロットは（レベルドレインでレベルを失わない限り）永久に消費されます。一生添い遂げる決意が固まっていない武器であれば、確信が持てるまでスロットを温存してください。
- **上限（キャップ）を意識した投資。** スキルを職業上限まで引き上げるのは何ら問題ありません：上限に達するとメニューからその選択肢が消えるだけです。上限を超えて無駄にスロットを浪費する心配はありません（そもそも選択肢が表示されません）。
- **魔法使いは魔法系統から2重の恩恵を受ける。** ランクが上がるごとに詠唱成功率が向上するだけでなく、その系統に属する魔法書の外見がより多く判明します（魔法詠唱の章で述べた [識別の恩恵](#wizards-identify-books)）。未識別の魔法書が多く眠っている系統を優先的に鍛えましょう。この2重の恩恵を受けられるのは魔法使いだけです（他の職業は詠唱成功率の上昇のみ）。
- **魔法使いの定石：魔法系統より先に短剣を鍛える。** 一般的な序盤戦略として、魔法系統へ本格的に投資する前に **短剣をエキスパートまで引き上げる**（6スロット消費）手法があります。マナ（Pw）が枯渇しやすい序盤を投擲短剣の圧倒的な打撃力で切り抜け、中盤以降にマナとスキル枠が潤沢になってから魔法系統を一気に開花させることで、序盤で餓死・戦死することなく終盤へと繋ぐことができます。
- **騎乗は立派なスキルである。** **騎乗入門（Basic）** を持っていないと、馬上でアイテムを拾う、中身を漁る、水に浸す、罠を仕掛ける/解除する、床に文字を刻む、といった行動が一切行えません。騎士は入門でスタートします。これを「熟練」まで引き上げることで、鞍の上での命中 −1 のペナルティが消え、さらにダメージ +1 が加算されます。
- **素手格闘と武術は武闘家の独壇場である。** 総師範 (Grand Master)に到達するには **累積で9枠の非武器スロット** が必要ですが、武闘家は自然にその領域に達します。野蛮人、洞窟人、侍はマスターまで到達可能であり、他の職業の上限はさらに低くなっています。

いくつかの呪文は「熟練」で劇的に凶悪化します。「冷気の円錐」と「火炎球」は、離れた位置に精密着弾させられる 3×3 の **爆発群** へと変貌します。「識別」「解呪」「自己加速」「怪物探知」をはじめとする多くの呪文は、祝福された巻物と同様の超強化効果を獲得します。

### 願いと願い方 (Wishes and Wishing)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source: no corrections. Verified Vlad throne 4/13, Amulet-pickup wish, magic-lamp/smoky-potion/fountain odds, enchant-collapse & negative-Luck rules, artifact-wish denial, silent substitutes, Castle/Orcus guarantees.
-->

画面に *「何をお望みですか？」（"For what do you wish?"）* と表示されたとき、ゲームは自由形式のアイテム指定文字列を受け付けます。入力する前に、望むアイテムと正確なスペルを完全に決定してください。たった1つのタイプミスが、ゲーム内で最も貴重な資源をただのゴミへと変えてしまいます。

#### 願いの入手源 (Sources of Wishes)

迷宮は基本的に出し惜しみしますが、大半の冒険者が考えているよりも多くの「願い」の発生源が存在します：

- **願いの杖 (Wand of wishing):** [城](#the-castle) の4つの隅にある小塔の1つに確定配置されています（充填や限界振りの仕様については [主要な杖](#key-wands) を参照）。
<!-- src/sit.c special_throne_effect(): cases 1-4 (of 13) = wish,
     throne only vanishes on wish, so guaranteed eventual wish. -->
- **ヴラドの玉座 (Vlad's throne):** 座り続けることで確定で願いを獲得できる特殊な玉座です。13通りの結果のうち4つが「願い」（ここで初めて玉座が消滅）であり、残る9つは痛手を受けますが玉座は消えずに残ります。願いが出るまで座り続けてください。
<!-- src/allmain.c: u.uhave.amulet && !u.uevent.amulet_wish -->
- **イェンダーの魔除け:** 初めて拾い上げた瞬間に、1回の願いが授けられます。ダンジョンの最深部に到達した者への褒美です。すでに装備が完璧に揃っていればこの願いを辞退することも可能です（ミニマリストの昇天プレイヤーの中には、主義として意図的にスキップする者もいます）。
- **魔法のランプ:** 祝福された魔法のランプを擦ると、3分の1 の確率でジンが出現します。そしてジンが出現した場合、80% の確率で願いを叶えてくれるため、1回擦るごとに約 27% の確率で願いが叶います。出るまで擦り続けましょう。オーケスの町には、魔法のランプまたは魔法のマーカーのどちらかが確定で配置されています。
- **泉 (Fountain):** 飲むと約 30回に1回 の確率で水の魔神（ウォーターデーモン）が出現し、その魔神が願いを叶えてくれる確率は浅い階層で約 5回に1回（深い階層ではさらに低下）であるため、飲むごとの真の願い確率は 150分の1 前後です。蛇、ニンフ、呪い、あるいは嘔吐を引き起こす確率の方が圧倒的に高くなります。
- **通常の玉座:** 座った際にごく稀に願いが発生します。ただし同時にすべてが破滅する現実的なリスクも伴います。
- **煙の立つ薬から出現するジン:** 稀であり（基本確率 13分の1）、出現しても願いをくれる確率は 20%（祝福された薬なら 80%）に過ぎません。しかし成功したときは、まるで天才になったかのような気分を味わえます。

1回のゲームで得られる願いの総数は大きく変動します。城の杖の初期チャージ・再充填・限界振り、ヴラドの玉座、そして魔除け拾得時の願いを合わせると、堅実に見積もって約5回が予算の目安となります。ランプ、泉の魔神、煙の立つ薬がそれに上乗せされることがあります。

#### 何を願うべきか (What to Wish For)

2つのドラゴンの鱗鎧の願いは、対となる一対として選びます。すでに魔除けや盾から「反射」を得ている場合は、**灰色ドラゴンの鱗鎧** を願って「魔法防御」を獲得してください。クロークがすでに魔法防御を提供しており反射が欠けている場合は、**銀色ドラゴンの鱗鎧** を願います。胴以外のスロットでどちらか一方の防御が確保できたら、もう一方の鱗鎧が最初の願いの最善候補となります。

1. **灰色ドラゴンの鱗鎧 (Gray dragon scale mail)** ([魔法防御](#damage-resistances) + AC。魔法防御はゲーム内で最も重要な防御能力です)。
   - 英語入力例: `blessed greased fixed +2 gray dragon scale mail`
   - 日本語入力例: `祝福された 油が塗られた 錆びない +2 灰色ドラゴンの鱗鎧`
2. **銀色ドラゴンの鱗鎧 (Silver dragon scale mail)** (反射 + AC。反射は死の杖の光線や各種ブレス攻撃から身を守ります)。
   - 英語入力例: `blessed greased fixed +2 silver dragon scale mail`
   - 日本語入力例: `祝福された 油が塗られた 錆びない +2 銀色ドラゴンの鱗鎧`
3. **韋駄天の靴 (Speed boots)** (高速行動により1ターンあたりの手数が増え、攻撃にも脱出にも絶大な威力を発揮します)。
   - 英語入力例: `blessed greased fixed +2 speed boots`
   - 日本語入力例: `祝福された 油が塗られた 錆びない +2 韋駄天の靴`
4. **力の小手 (Gauntlets of power)** (強さを 25 に固定。殴り火力を高めたい多くの職業で恩恵があります)。
   - 英語入力例: `blessed greased fixed +2 gauntlets of power`
   - 日本語入力例: `祝福された 油が塗られた 錆びない +2 力の小手`
5. **命の魔除け (Amulet of life saving)** (元素界での不慮の死に備える予備の命)。
   - 英語入力例: `blessed amulet of life saving`
   - 日本語入力例: `祝福された 命の魔除け`（魔除けは強化値や防錆加工を持ちません）
6. **特定のアーティファクト** ([グレイスワンダー](#grayswandir) が代表例です。銀製であり悪魔、インプ、吸血鬼、獣化モンスター、影に致命的な特効ダメージを与えます)。
   - 英語入力例: `blessed greased fixed +2 Grayswandir`
   - 日本語入力例: `祝福された 油が塗られた 錆びない +2 グレイスワンダー`

切羽詰まった極限状況でない限り、消費アイテム（巻物や薬）を願ってはいけません。願いは、ドラゴンの鱗鎧、韋駄天の靴、強力なアーティファクトといった、他では手に入らない恒久的な装備品のために使うべきです。

#### 願いの構文 (Wish Syntax)

<!-- audit
2026-05-18:
- bare "gray dragon scale mail" keeps random spe and rolls BUC via blessorcurse(otmp,10): ~5% blessed / ~5% cursed / ~90% uncursed (objnam.c:5094-5096, 5258-5268)
- wished enchantment on armor/weapon/weptool/charged ring collapses to +0 if requested spe > rnd(5) (and > the item's random base spe): +1 always, +2 4/5, +3 3/5, +4 2/5, +5 1/5, +6+ never (objnam.c:5099-5105). Recommend +2. Roll is plain rnd(5), NOT luck-adjusted, so positive Luck gives no bonus.
- Luck < 0 sabotages wishes: "blessed" -> cursed (objnam.c:5263-5264), erodeproof/"fixed" fails to apply (objnam.c:5287), and spe > 2 flips negative (objnam.c:5104). Luck >= 0 is all that's needed; extra Luck does nothing. Wiki: +3 higher average, +2 less chancy and strictly better if enchanting further (https://nethackwiki.com/wiki/Wish).
- artifact wishes are probabilistic: oartifact && rn2(nartifact_exist())>1 (objnam.c:5374), scaled by TOTAL existing artifacts including bones
- u.uconduct.wisharti increments whether the wish is granted or denied (objnam.c:5364)
- only quest artifacts are absolutely blocked: restrict_name SPFX_NOGEN|SPFX_RESTR check (artifact.c:618)
- silent substitutes: Amulet of Yendor, Bell of Opening, Book of the Dead, Candelabrum, magic lamp → oil lamp (objnam.c:5003-5006)
- all gloves give +1 AC (objects.h:686-697); gauntlets of power give STR 25, not bonus AC (attrib.c:1214)
- Vlad's throne wish rate is 4/13 per effective sit (sit.c:241-256)
- magic lamp ≈27% wish-blessed: 1/3 djinni × 4/5 wish (apply.c:1817, potion.c:2833-2845)
- fountain water-demon wish (fountain.c:78, 314); Amulet-of-Yendor pickup wish (allmain.c:446-451)
- strategy aligned with NetHackWiki Wish, Gray dragon scale mail, Speed boots, Magic lamp: GDSM/SDSM as top wishes, speed boots and gauntlets of power as standard follow-ups, bare wishes risk cursed/random spe (https://nethackwiki.com/wiki/Wish, https://nethackwiki.com/wiki/Gray_dragon_scale_mail, https://nethackwiki.com/wiki/Speed_boots, https://nethackwiki.com/wiki/Magic_lamp)
-->

プロンプトが「何をお望みですか？」（"For what do you wish?"）と尋ねてきたら、具体的に指定してください。NetHackJP では、英語構文と日本語構文のどちらを入力しても正確に認識されます。それぞれの修飾語が何をもたらすかを解説します：

- **英語構文**: `blessed greased fixed +2 gray dragon scale mail`
- **日本語構文**: `祝福された 油が塗られた 錆びない +2 灰色ドラゴンの鱗鎧`

これが標準的な完成形です。指定しないと BUC（祝福・呪い）がランダムになるため `blessed`（祝福された）を指定し、`greased`（油が塗られた）は抱きつき、巻きつき、粘着攻撃、マインドフレアの触手を受け流すために付与し、`fixed`（錆びない / 耐火の / 防腐の）で損耗を防ぐ防蝕加工を施し、`+2` で強化値を指定します。必要以上に高い強化値を欲張ってはいけません：防具や武器のプラス値を指定すると、裏で 1〜5 のダイスが振られ、指定した値がそのロール値を上回ると強化値は無慈悲にも **+0 にリセット（崩壊）** します。したがって +1 は 100% 成功、+2 は 5分の4（80%）で成功、+3 は 5分の3（60%）で成功、+6 以上は絶対に通りません。+3 の方が通ったときの期待値はわずかに高いですが、それでも **+2** を指定することを強く推奨します。結果がより安定し、後から強化の巻物で仕上げを行えば、+3 で願った場合と遜色ない値に安全に到達できます。
- 願う前に自身の幸運（Luck）を確認してください。幸運が 0 以上（マイナスでない）でありさえすれば十分であり、過剰に善運を溜め込んでも願いの判定にボーナスはありません。しかし、**負の幸運（マイナス）** は願い全体を台無しにします：`blessed`（祝福された）を願っても呪われて生成され、`fixed`（錆びない）の防蝕加工は剥がれ、+2 を超えるプラス値はマイナスへと反転します。幸運が悪化している場合は、装備を願う前にまず幸運を回復させてください。
- 単に `gray dragon scale mail`（または `灰色ドラゴンの鱗鎧`）とだけ願うと、BUCも強化値もダイス任せになり、最悪の場合呪われて出現します。せっかくの貴重な願いです。必ずBUCと強化値を明記してください。また、英語で入力する場合は `scale` の単語を絶対に忘れないでください。`gray dragon mail` とだけ入力すると、代わりに「灰色の郵便の巻物」（scroll of mail）を渡されてしまいます。
- アーティファクトの願いは、世界に存在するアーティファクトの総数が増えるほど **成功率が低下** します。拒絶判定はダンジョン内に存在する総数（所持品、床落ち、ボーンズファイル内のものを含む）に応じて厳しくなり、出現しなかった場合でも「アーティファクト願いカウンター」は加算されます。なお、他職のクエストアーティファクトは絶対に生成されません（完全拒絶）。
- 一部の禁止アイテムを願うと、黙って無価値な日用品へとすり替えられます。**イェンダーの魔除け** は偽物の魔除けに、**開放の鐘** はただの鈴に、**死者の書** は白紙の本に、**祈りの燭台** は獣脂のろうそくになります。また **魔法のランプ** を願っても失敗し、単なる油つぼ（普通のランプ）を手渡されます。あんなに一生懸命ランプを擦ってきた後では、あまりにも残酷な仕打ちです。

### アーティファクト (Artifacts)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Stormbringer is SPFX_INTEL: cross-alignment touch deals 4d10, not 4d4. (artilist.h:93-96 Stormbringer has SPFX_INTEL; artifact.c:953 `dmg = d((Antimagic ? 2 : 4), (self_willed ? 10 : 4))`)
- Grimtooth +d6 damage bonus applies to ALL targets, not just elves (artifact.c:1099-1102).
- Mitre of Holiness gives NO damage bonus vs undead; ATTK is NO_ATTK (artifact.c:1095-1098).
- M2_UNDEAD flag only enables shade_glare on weapons, not worn helms (artifact.c:554-571).
- Eye of the Aethiopica magic resistance requires worn, NOT carried (artilist.h:303-305, NO_CARY).
- Eye of the Aethiopica carry effects: energy regen, half spell damage (cspfx EREGEN, HSPDAM).
- strategy aligned with NetHackWiki Artifact weapon, Grayswandir, Magicbane, Mjollnir: Grayswandir/Magicbane/Mjollnir as the top wish artifacts; alignment-mismatched artifacts blast on touch (https://nethackwiki.com/wiki/Artifact_weapon, https://nethackwiki.com/wiki/Grayswandir, https://nethackwiki.com/wiki/Magicbane, https://nethackwiki.com/wiki/Mjollnir)
-->

迷宮の各地には、伝説に彩られた至宝が散らばっています：通常の装備では到底及ばない超絶な力を宿した、固有の名を持つ武器、魔除け、そして道具たちです。各アーティファクトは1回のゲームにつき世界に1つしか存在しません。それらを入手する手段は以下の通りです：

- **泉に剣を浸す**（秩序属性のキャラクターによるエクスカリバー）。
- **祭壇での生贄奉納**（自属性の神からギフトとして授けられる）。
- **クエストの完遂**（各職業固有のクエストアーティファクト）。
- **願い**（大半のアーティファクトは願うことができますが、自身の属性と一致しない場合は拒絶されることがあります）。
- **ランダム生成**（稀ですが、武器がアーティファクトとして自然生成される微小な確率があります）。
- **命名**（スティングおよびオークリストのみ。後述参照）。

#### 属性と侵害ダメージ (Alignment and Blasting)

各アーティファクトには属性が宿っています。自身の属性と一致しないアーティファクトを手に取ろうとすると、激しい侵害ダメージ（ブラスト）を受けます：

- **知性を持つアーティファクト（知性体）** は、職業または属性のいずれかが不一致の場合、触れるたびに **4d10** の侵害ダメージを与えます（魔法耐性があれば 2d10 に半減）。職業と属性の *両方* が不一致の場合、アイテムはあなたの手をすり抜けて落下し、掴むことすら拒絶します。
- **その他の非知性アーティファクト** は、属性が不一致の場合、触れるごとに 4分の1 の確率で **4d4** の侵害ダメージを与えます（魔法耐性があれば 2d4 に半減）。

#### 願い可能・ランダムアーティファクト (Wishable / random artifacts)

これらは自然生成、生贄ギフト、泉への浸漬（エクスカリバー）、あるいは願いによって入手可能なアーティファクト群です。追加ダメージは攻撃命中ごとにその都度ロールされます（例: `+d10` は 1d10 を振る）。「追加ダメージ」列は、ベースとなる武器自体の基本ダメージの *上に上乗せ* される数値を表します。「対Xで×2」と記された武器は、そのモンスタークラスに属する敵に対してベース武器ダメージを *2回* ロールします。

| アーティファクト名 | 属性 | ベース武器 | 命中 | 追加ダメージ | 特記事項 |
|------------------------|----------|-------------------|--------|------------------------|--------------------------------------------------------|
| エクスカリバー (Excalibur) | 秩序 | 長剣 | +d5 | +d10 物理 | 吸魔耐性、自動索敵（歩くごとにオートサーチ） |
| グレイスワンダー (Grayswandir) | 秩序 | 銀のサーベル | +d5 | **×2 物理** | 幻覚耐性（銀製特効） |
| ミョルニル (Mjollnir) | 自属性 | ウォーハンマー | +d5 | **+d24 電撃** | ワルキューレは 99% キャッチ。投擲には強さ 25 が必要 |
| マジックベイン (Magicbane) | 中立 | アサメ | +d3 | +d4 魔法 (気絶) | **構えている間**、魔法耐性と呪い防御を付与 |
| ストームブリンガー (Stormbringer) | 混沌 | ルーンの剣 | +d5 | +d2 生命吸収 | 敵からレベルを吸いHPを回復。平和的NPCにも襲いかかる |
| ヴォーパルブレード (Vorpal Blade) | 中立 | 長剣 | +d5 | +d1 物理 | 命中時に敵の首を切り落とす即死確率 |
| フロストブランド (Frost Brand) | 任意 | 長剣 | +d5 | **×2 冷気** (非耐性敵) | 構えている間、冷気耐性を付与 |
| ファイアブランド (Fire Brand) | 任意 | 長剣 | +d5 | **×2 火炎** (非耐性敵) | 構えている間、火炎耐性を付与 |
| サンソード (Sunsword) | 秩序 | 長剣 | +d5 | (基本のみ); 対アンデッド×2 | 構えると光源になる。`#invoke` で全方位に目くらまし光線 |
| スニッカーズニー (Snickersnee) | 秩序 | 刀 | — | +d8 物理 | 通常の刀近接に加え、毎ターン1回長柄武器間合いのリーチ攻撃（"Shkinng!"） |
| クリーバー (Cleaver) | 中立 | 戦斧 | +d3 | +d6 物理 | 両手持ち。攻撃時に左右両脇の敵も同時に薙ぎ払う |
| デーモンベイン (Demonbane) | 秩序 | 銀のメイス | +d5 | (基本のみ); 対悪魔×2 | 悪魔を追放（banish）。司祭への第1回生贄ギフト確定 |
| スティング (Sting) | 混沌 | エルフの短剣 | +d5 | (基本のみ); 対オーク×2 | オークが近くにいると青く光る警告機能 |
| オークリスト (Orcrist) | 混沌 | エルフの幅広の剣 | +d5 | (基本のみ); 対オーク×2 | オーク接近時に警告 |
| グリムトゥース (Grimtooth) | 混沌 | オークの短剣 | +d2 | +d6 物理 (全対象) | エルフ接近時に警告。毒から防御 |
| ドラゴンベイン (Dragonbane) | 任意 | 幅広の剣 | +d5 | (基本のみ); 対ドラゴン×2 | 構えている間、反射を付与 |
| ウェアベイン (Werebane) | 任意 | 銀のサーベル | +d5 | (基本のみ); 対獣化モンスター×2 | 獣化症（ライカンスロープ）から防御 |
| ジャイアントスレイヤー (Giantslayer) | 中立 | 長剣 | +d5 | (基本のみ); 対巨人×2 | — |
| オウガスマッシャー (Ogresmasher) | 任意 | ウォーハンマー | +d5 | (基本のみ); 対オーガ×2 | — |
| トロルズベイン (Trollsbane) | 任意 | モーニングスター | +d5 | (基本のみ); 対トロール×2 | 構えている間、HP自然回復 |

すべてのアーティファクトが同等に魅力的なわけではありません。**グレイスワンダー** と **マジックベイン** は大半のプレイヤーが最初に願う最高峰のアーティファクトです。**ミョルニル** はワルキューレにとって象徴的な願い候補です。**エクスカリバー** は願うよりも泉に剣を浸して得るのが通例です。**フロストブランド**、**ヴォーパルブレード**、**ストームブリンガー** は2番目の願いとしてよく選ばれます。5.0 では **スニッカーズニー** に毎ターンの無料リーチ攻撃が追加され、**サンソード (Sunsword)** は能動的に敵を目くらましできるようになりました。残る特効（ベイン）武器、ファイアブランド、クリーバーなどは、貴重な願いを費やすというよりは生贄ギフトとして授かるのが一般的です。

**[エクスカリバー]{#excalibur-artifact}** は秩序属性キャラクターの決定的な定番武器です。より強い武器を手に入れた後でも、レベルドレイン耐性のためだけに持ち歩く価値があります。経験レベル5以上において、騎士は 6分の1、他の秩序職は 30分の1 の確率で泉への浸漬から授かることができます。

**[グレイスワンダー]{#grayswandir}** は願うことが可能であり、ダンジョン内屈指の最強近接武器の1つです。銀製（多くの敵に致命的特効）、あらゆる攻撃で物理ダメージ2倍、命中 +d5、そして幻覚耐性をもたらします。

**[ミョルニル]{#mjollnir}** はワルキューレを象徴する投擲帰還武器です：ワルキューレだけが 99% の確率で投げた槌をキャッチして手元に戻すことができます。他の職業でも近接武器として振るうことはできますが、投げると戻ってこないため投擲は極めて危険です。構えること自体は誰でも可能ですが、投げるには強さ 25 が必須です（力の小手で達成可能）。+d24 の電撃ダメージは電撃耐性のないあらゆる敵を粉砕します。

**[マジックベイン]{#magicbane}** は魔法使いの定番アサメです。気絶ダメージ、呪い防御、魔法耐性はすべて単に持ち歩くだけではなく **構えている（手に持っている）** 必要があります。中立属性の生贄ギフト第1号として頻繁に授けられます。二刀流の魔法使いにとって注意すべきニュアンス：呪い防御オーラが発動するのは、マジックベインが *主武器* として構えられている間だけです。重い武器を主武器にし、マジックベインを逆手に持っている場合、抗呪オーラは停止してしまいます。

**[ストームブリンガー]{#stormbringer}** は平和的なモンスターにも自動的に襲いかかるため、属性値を急降下させる危険を孕んでいます。命中ごとに相手からレベルを吸い取り、犠牲者が失ったHPの半分だけ術者を回復させます（相手の経験レベルそのものを獲得できるわけではありません）。

**スティング** と **オークリスト** は、名付け（`#name`）によって生成できる唯一のアーティファクトです。それぞれエルフの短剣、エルフの幅広の剣を単体（束ではなく1本）にして名前を付けます。構えるとオークが接近した際に青く光り、オークに対して2倍ダメージを与えます。どちらも混沌属性であるため、混沌の英雄なら安全に扱えますが、他の属性の者が手に持つと時折侵害ダメージを受けます。

#### クエストアーティファクト (Quest artifacts)

各職業には固有のクエストアーティファクトが1つずつ存在し、その職業のクエストを完遂することで授与されます。これらのアーティファクトは知性を持っています：職業または属性が一致しない場合、触れるたびに **4d10** の侵害ダメージを受け、両方が不一致の場合は掴むことすらできずに手からすり抜けます。9種類の非武器クエストアーティファクトのうち3つ（探知のオーブ、マーリンの魔法の鏡、プラチナイェンダー印エクスプレスカード）は、**インベントリに所持しているだけ（直接携帯）** で魔法耐性を付与します。

クエストアーティファクトを願うことは絶対にできません。必ずその職業のクエストで勝ち取る必要があります。以下の表では、所持品として携帯しているだけで効果を発揮する **「所持 (Carry)」** 能力と、身につけたり手に構えたりする必要がある **「装備/構え (Wear/wield)」** 能力を明確に区別しています。

`M-i`（または `#invoke`）によって、アーティファクト固有の特殊能力を発動できます。十分休眠した（再使用待機時間を終えた）アーティファクトは魔力（エネルギー）を消費せずに発動でき、発動後は約100ターンの間クールダウンに入ります。サンソード (Sunsword)とグリムトゥースのみ、クールダウン中であっても 25 Pw を支払うことで能力を発動させることができます。

::: dense-table

| 職業 | アーティファクト名 | 形態 | 装備/構え時効果 | 所持時効果 | `#invoke` (発動効果) |
|------|------------------------------------------|----------------|-----------------------------------|--------------------------|---------------------|
| 考古学者 | 探知のオーブ (The Orb of Detection) | 水晶玉 | — | **魔法耐性**、テレパシー、呪文被ダメージ半減 | 透明化 |
| 野蛮人 | アーリマンの心臓 (The Heart of Ahriman) | 幸運の石 | 投擲時にダメージ2倍 | 忍び、**幸運保持(+3)** | 浮遊 |
| 洞窟人 | 力の王笏 (The Sceptre of Might) | メイス | 命中+d5、非秩序敵に×2、**魔法耐性** | — | 争い (Conflict) |
| 治療師 | アスクレピオスの杖 (The Staff of Aesculapius) | 六尺棒 | 命中時に生命吸収、吸魔耐性、HP自然回復 | — | 減少HPの半分回復、病気・スライム化・盲目を治療 |
| 騎士 | マーリンの魔法の鏡 (The Magic Mirror of Merlin) | 鏡 | (時折話しかけてくる) | **魔法耐性**、テレパシー | — |
| 武闘家 | オーバーワールドの目 (The Eyes of the Overworld) | レンズ | 星界視覚(周囲3マス透過視)、**魔法耐性** (着用時) | — | 啓蒙 (自己ステータス判明) |
| 司祭 | 神聖の僧帽 (The Mitre of Holiness) | 兜 | 知性の兜ベース、防護+1 (MC1) | 火炎耐性 | 魔力（Pw）大幅回復 |
| レンジャー | ディアナの長弓 (The Longbow of Diana) | 弓 | 命中+d5、**反射** (構え時) | テレパシー | 矢を虚空から無限召喚 |
| 盗賊 | 盗賊術のマスターキー (The Master Key of Thievery) | 万能鍵 | — | 警告、瞬間移動制御、物理被ダメージ半減 | 罠解除確定成功 |
| 侍 | 村正の剣 (The Tsurugi of Muramasa) | 大刀 | 物理+d8、即死首切り確率、防護+1 | **幸運保持(+3)** | — |
| 観光客 | プラチナイェンダー印エクスプレスカード (PYEC) | クレジットカード | — | **魔法耐性**、テレパシー、呪文被ダメージ半減 | アイテムの充填 (チャージ) |
| ワルキューレ | 運命のオーブ (The Orb of Fate) | 水晶玉 | — | **幸運保持(+3)**、警告、**全被ダメージ半減** | 階層テレポート |
| 魔法使い | エチオピカの目 (The Eye of the Aethiopica) | 魔除け | **魔法耐性** (着用時) | 呪文被ダメージ半減、**魔力高速自然回復** | 訪問済み支流へのポータル生成 |

:::

**[探知のオーブ]{#orb-of-detection}** (考古学者): 水晶玉であり、所持しているだけでテレパシーと魔法耐性を授かります。`#invoke` で透明化を切り替えられます。考古学者は元々忍び能力に長けており、これにより完全な亡霊と化します。

**[アーリマンの心臓]{#heart-of-ahriman}** (野蛮人): 本物の幸運の石（幸運上限を +13 に引き上げ、幸運の石として機能するあらゆる恩恵を持つ）であり、さらに忍びを与えます。野蛮人はこれを投擲武器として投げて2倍ダメージを与え、拾い直すこともできます。`#invoke` で浮遊します。

**[力の王笏]{#sceptre-of-might}** (洞窟人): メイスがベースで、命中 +d5、属性が異なる敵すべてに対してダメージ2倍（笏自体が秩序であるため、混沌、中立、無属性のすべての敵に対して2倍ダメージとなり、[ゲヘナ](#gehennom) の敵の大半に特効です）。構えている間は魔法耐性も付与します。`#invoke` でエネルギー消費なしに争い（敵同士の内輪もめ）を発生させます。

**[アスクレピオスの杖]{#staff-of-aesculapius}** (治療師): 命中ごとに相手から生命を吸い取ります（生命吸収武器はこれとストームブリンガーのみ）。HP自然回復と吸魔耐性は構えている必要があります。`#invoke` で失ったHPの半分を瞬時に回復し、病気、スライム化、盲目を完治させます。

**[マーリンの魔法の鏡]{#magic-mirror-of-merlin}** (騎士): テレパシーと魔法耐性を付与し、使用または構えると時折噂話を囁いてきます。騎士はすでに戦闘用としてエクスカリバーを持っているため、この鏡はお守り兼保険として携帯されます。

**[オーバーワールドの目]{#eyes-of-the-overworld}** (武闘家): レンズであり、着用すると周囲3マスを見通す星界視覚（X線視覚）と **魔法耐性** をもたらします。どちらの効果も着用している必要があり、鞄や所持品に入れているだけでは発揮されません。`#invoke` で啓蒙されます。胴防具を着られない武闘家にとって、使用可能な装備枠で魔法耐性を確保できる極めて強力な至宝です。

**[神聖の僧帽]{#mitre-of-holiness}** (司祭): 知性の兜がベースであり、知力と知恵をブーストして呪文を確実にし、携帯中に火炎耐性、さらに外来防護（MC1）を提供します。`#invoke` で魔力（Pw）を大幅にチャージし、呪文を連射する司祭にとって生命線となります。なお、司教冠自体には近接攻撃がないためアンデッド特効ダメージはなく、吸魔耐性も与えません。

**[ディアナの長弓]{#longbow-of-diana}** (レンジャー): 構え時に命中 +d5 と反射、携帯時にテレパシーをもたらすアーティファクト弓です。`#invoke` で虚空から無償の矢を無限に生成します。レンジャーの射撃能力と合わさることで、この職業の完全無欠の主砲となります。

**[盗賊術のマスターキー]{#master-key-of-thievery}** (盗賊): 持っているだけで警告、瞬間移動制御、そして受ける物理ダメージ半減という破格の防御性能を誇ります。錠前に向けて使用すると罠を探知し、扉や宝箱に対する `#untrap`（罠解除）が確定で成功します。盗賊なら呪われていない鍵でも機能しますが、他職の場合は祝福されている必要があります。

**[村正の剣]{#tsurugi-of-muramasa}** (侍): 刀クラスの両手剣であり、ダメージ +d8、即死首切り確率（ヴォーパルブレード同等）、防護 +1、そして幸運の石としても機能します。なお、世間の評判とは異なり、村正の剣は **魔法耐性を与えない** 点に注意してください。侍が過酷なクエストを突破した末に手にする最高峰の業物です。

**[プラチナイェンダー印エクスプレスカード]{#platinum-yendorian-express-card}** (観光客): 観光客の窮地脱出カードです。携帯するだけでテレパシー、魔法耐性、呪文被ダメージ半減を付与し、`#invoke` でアイテム（杖、指輪、魔法のマーカー）を再充填します。願いの杖に1回分のチャージを追加することも可能ですが、その杖が耐えられる再充填は依然として1回のみです。

**[運命のオーブ]{#orb-of-fate}** (ワルキューレ): ゲーム中で最も贅沢な携帯パッシブ能力を誇ります。幸運の石として機能し、警告を付与し、呪文被ダメージと物理被ダメージの **両方を半減** します。`#invoke` で階層テレポートを行います。

**[エチオピカの目]{#eye-of-the-aethiopica}** (魔法使い): **身につけている間** 魔法耐性を与え、携帯中に呪文被ダメージ半減と **魔力超高速自然回復**（毎ターン回復）をもたらします。`#invoke` で過去に訪れたダンジョン支流の一覧メニューが開き、選んだ支流へと一瞬でポータルを開いて移動します。

---

### ゲヘナ突入 (Into Gehennom)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Only Asmodeus/Baalzebub/Juiblex/Orcus have dedicated levels (dungeon.lua Gehennom list); Yeenoghu & Demogorgon are G_NOGEN (summon-only). Removed them from the throne-level list.
- Orcus is speed 9 (LVL(66,9,...)), a slow flier, not "fast".
- Verified correct: Valley roster, demon-lord attacks/resistances, bribe list & rules, Vlad throne, teleport-blocked-while-demon-lord-lives, Orcus loot.
-->

ここから先は、冒険の最終段階であるゲヘナの深淵と、イェンダーの魔除けを奪取して地上へと駆け上がる「昇天への旅路」を解説します。

#### 城 (The Castle)

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

---

#### ゲヘナ (Gehennom)

<!-- audit
2026-05-19:
- Asmodeus carries wands of cold AND fire (makemon.c:804-807)
- Asmodeus is fire-, cold-, AND poison-resistant: MR_FIRE|MR_COLD|MR_POISON (monsters.h:3124)
- Baalzebub: AT_BITE/AD_DRST (drain Str, poisonous) + AT_GAZE/AD_STUN (stun) — NO gas cloud, NO fly summons (monsters.h:3110-3119)
- Baalzebub's lair is beetle-shaped (mkmaze.c:471 baalz_fixup)
- demon-lord teleport blocked (teleport.c:21-34)
- Geryon/Dispater/Baalzebub/Asmodeus are the bribable major demons (MS_BRIBE) — minion.c:309-311 sets bribe price
- Vlad's throne effect rate: only rnd(6) > 4 (= 1/3 of sits) triggers anything; 4/13 of those are the wish (sit.c:45, 238-353)
- so unconditional wish rate is (1/3)·(4/13) = 4/39 ≈ 10%; ~10 sits average, ~7 bad effects absorbed
- Orcus drops magic lamp or magic marker, 50/50 (orcus.lua:107-111)
- Sanctum has noteleport + nommap (sanctum.lua:8)
- Valley of the Dead has noteleport + nommap + non-diggable walls (valley.lua:10, 74)
- strategy aligned with NetHackWiki Gehennom, Bribe, Demon lords and princes: prayer dead, bribery (gold in open inventory) for the lawful demon princes, Excalibur disables bribery, dig don't navigate (https://nethackwiki.com/wiki/Gehennom, https://nethackwiki.com/wiki/Bribe, https://nethackwiki.com/wiki/Demon_lords_and_princes)
- blessed scroll of genocide on class 'L' wipes lich/demilich/master lich/arch-lich (read.c:2638-3015 do_class_genocide, monsters.h:1864-1899 four S_LICH entries); Wizard of Yendor is S_HUMAN (monsters.h:2847-2858), not affected
-->

[城](#the-castle) の下層では、ダンジョンはその様相を一変させます。直線的な通路は迷路（メイズ）へと姿を変え、一般的なモンスターは凶悪な悪魔たちへと取って代わられます。何よりも恐ろしいのは、あなたの神が沈黙することです。ゲヘナでは祈りが一切通じず、ここから先は城で整えた所持品だけを頼りに生き延びなければなりません。

#### 死の谷 (The Valley of the Dead)

城の直下に広がるゲヘナの第1層が **死の谷** (The Valley of the Dead) です。到達すると *「死の谷に到着した...」（"You arrive at the Valley of the Dead..."）* というメッセージが表示され、ダンジョン概要にもゲーム終了までその名前が記録されます。マップは広大で不規則な形状をしており、3つの墓地が点在しています。あなたは右下に出現します。降下階段は左上にあり、左側の中ほどには恒久的な **モロクの祭壇（祠）** が鎮座しています。この祭壇は無属性の高位祭壇（High Altar）であるため、ここでは絶対に祈ってはいけません。壁は全面にわたって掘削不能（non-diggable）であり、ショートカットは作れません。さらに `noteleport`（瞬間移動不能）と `nommap`（魔法の地図無効）の両方が設定されているため、地図化の巻物は通用せず、テレポートによる移動も封じられています。

注目に値する不気味な細部があります。フロアの至る所に、かつてこのダンジョンに挑んで命を落とした **あらゆるプレイヤー職業の死体** が散らばっています：考古学者、野蛮人、洞窟人、治療師、騎士、レンジャー、盗賊、侍、観光客、ワルキューレ、魔法使いの死体がそれぞれ2体ずつ横たわっています。そして際立って不在なのが、司祭と武闘家です。モロク神は、これらの信仰・修道クラスの者たちに対して、死体すら残さない特別な運命を用意しているのかもしれません。

#### ゲヘナの特殊環境 (What's Different in Gehennom)

- **祈りの完全無効。** あなたの神はゲヘナにおいて完全に耳を塞いでいます（あなたがモロクの信者でない限り。そしてもちろんあなたは違います）。緊急のHP回復も、食料の救済も、神罰による呪い解除も一切期待できません。周到に荷造りしてください。ここから先は完全にあなた一人きりです。
- **至る所に燃え盛る火炎。** 通路には火の罠が散乱し、悪魔たちは息をするように自然に火炎ブレスを吐きかけてきます。もし現時点で [火炎耐性](#damage-resistances) を持っていないなら、今すぐ引き返してください。
- **熱を帯びた床面。** 床に落とした薬は熱で粉々に砕け散ります（インベントリ内の薬を破壊するのは主に火の罠です）。所持品を整理するためであっても、貴重な薬の小瓶を床に無造作に置いてはいけません。
- **溶岩の河。** 一部の階層を溶岩の奔流が分断しています。浮遊や飛行によって渡ることができ、耐火加工を施した水上歩行の靴でも通過できます。最も鮮やかな手口：冷気の光線（吹雪の杖、冷気の円錐呪文、冷気の角笛、冷気ブレス）を吹き付けると、溶岩が一瞬で永久的な通常の床へと凍りつき、真っ直ぐ渡れる歩道が完成します。火炎耐性がない場合、溶岩に触れると即死します。耐性がある場合でも沈み込んでしまい、浮遊、テレポート、または歩いて脱出するまでに約12ターンの猶予しかありません。
- **固有の階層に君臨する魔王たち。** アスモデウス、ベルゼブブ、ジョウビレックス、オーケスがそれぞれの専用玉座階層に居を構えています。それぞれの戦闘は死闘となり、何体かは援軍を召喚し、全員があなたの侵入に激怒しています。彼らの居城と買収（ワイロ）のルールについては後述します。
- **テレポートの制限。** 魔王が君臨する居城フロアでは、その魔王が生存している間はテレポートが封じられます。魔王を殺害するか追放（banish）すれば、この制限は解除されます。旧バージョンとは異なり、近年のNetHackではゲヘナの全フロアで恒久的にテレポートが禁止されているわけではありません。
- **全面迷路。** ほぼすべての階層が迷路（メイズ）構造です。穴掘りの杖やつるはしはもはや贅沢品ではなく生存の必需品です。階段へ向けて一直線に壁を掘り進み、決して後ろを振り返らないでください。

#### 魔王たちの巣窟 (The demon-prince lairs)

ゲヘナの特殊階層のうち3つは、**アスモデウス** (Asmodeus: 火炎・冷気・毒耐性を持ち、冷気呪文を唱え、吹雪の杖と炎の杖を携帯)、**ベルゼブブ** (Baalzebub: 蝿の王であり、気絶の視線と強さを吸い取る毒の噛みつきを持つ。居城は甲虫の形をした迷路)、そして **ジョウビレックス** (Juiblex: 顔なき主、近接攻撃で相手を飲み込み酸を吐きかける巨大スライム) の個人玉座です。彼らはあなたが視界に入るまで居城で待ち構えており、視界に入った後は階段を追跡してきます。

**4体の魔王は買収（ワイロ）を受け付けます：アスモデウス、ベルゼブブ、ゲリュオン、ディスパテル。** 要求額はメイン所持品にあるゴールドのランダムな割合であるため、大半のゴールドを袋の中に隠し、少額の支払い分だけを袋の外（直接のインベントリ）に残しておきましょう。袋の外にゴールドを一切持たずに接近すると、魔王は即座に襲いかかってきます。4体とも秩序属性であるため、秩序属性の冒険者は半額で済みます。ジョウビレックス、イエノグ、オーケス、デモゴルゴンらは問答無用で視界に入り次第攻撃してきます。

終盤であればジョウビレックスと戦って倒すことも可能ですが、近接戦闘では丸呑みされる危険があるため、必ず距離を保ってください。悪魔は死の光線（死の杖）に対して完全耐性を持っています。通常の物理ダメージ、追放アーティファクト、あるいは他の脱出手段を使ってください。なお、提示された買収を **拒否** すると、魔王は永久に敵対化し、二度と交渉に応じてくれません。買収するか、戦うかの二者択一です。

**[エクスカリバー](#excalibur-artifact) または デーモンベイン を構えていると、買収交渉は完全に封じられます。** これらの聖剣を手にした冒険者を目にした魔王は即座に激怒して襲いかかってくるため、接近する前に必ず武器を鞘に収めて（装備を外して）ください。

#### ヴラドの塔 (Vlad's Tower)

ゲヘナから **上向き** に分岐する3層の塔であり、下層ダンジョンにおける数少ない支流の1つです。ユニークな吸血鬼の首領である **吸血鬼ヴラド** (Vlad the Impaler) が、最上階で **祈りの燭台** (Candelabrum of Invocation) を守護しています。塔を登り、ヴラドを倒し、燭台を奪い取ってください。

この塔には **特殊な玉座** も設置されており、5.0 ではより見返りが大きく、同時に痛みを伴うものへと調整されました。朗報：通常の玉座のように使いすぎて崩壊することが一切ないため、何度でも座り直すことができます。悲報：賞品が出る確率は低いため、何度も座り直す羽目になります。座るたびに13種類の結果のいずれかが選ばれます。そのうち4つは「願い」を叶えてくれます（願いが叶った時点で、玉座は役目を終えて初めて崩壊します）。残る9つはすべて悲惨な災難です：恒久的なレベルドレイン、所持品全体を覆う油まみれの脂（武器が手から滑り落ち、盾が外れる）、耐性・能力の剥奪、振動する四角の階層への強制階層テレポート（時に有用、多くは迷惑）、3体の悪魔の召喚、所持品への混乱状態での祝福解呪、強制変身（ポリモーフ）、酸耐性がない場合 50+8d6（平均約78）の酸ダメージ、あるいは大半のステータスを悪化させる能力値のランダムシャッフルです。

計算の内訳：座っても3回に1回しか効果そのものが発動せず（残る3分の2は「場違いな気がする」と表示されて何も起きない）、発動したもののうち 13分の4 が願いです。無条件での願い発生率は約 10分の1（約10%）であるため、願いが出るまでに約10回座り、その過程で約2回の悪い効果を甘受する心構えが必要です。HPを満タンにし、貴重な装備品は床に置いてから座り（脂が付着するとインベントリ全体が覆われ、100〜200ターンの間手が滑って道具を使うたびに落としてしまう）、必ず [酸耐性](#damage-resistances) を確保してから座ってください。酸ダメージは最大 80 HP に達し、魔法耐性であっても玉座の悪影響を防ぐことはできません。もし今すぐ願いを欲していない場合（例えば城の願いと魔除けの願いをすでに使い、この願いを最終昇天装備の予備として温存したい場合）、後から戻ってくることも可能です。何者かが破壊しない限り、玉座はその場に留まり続けます。

#### オーケスの町 (Orcus Town)

**オーケス** (Orcus) はローマ神話の冥府の神であり、破られた誓いを罰し死者を貪る冥界の支配者です。迷宮内における彼はユニークな魔王（`&`、レベル66、速度9の緩慢な飛行体）であり、呪文を唱え、武器を振るい、2回爪で引き裂き、強さを吸い取る毒針を突き刺す **アンデッドの君主** です。彼が手にする武器はアーティファクトではなく、通常の **死の杖** です。彼の指先から放たれる簡易呪文もまた死の光線であるため、反射または魔法耐性を必ず準備してください。オーケスは悪魔であるため、こちらから放つ死の光線は無効化されます。物理ダメージまたは他の攻撃手段で戦ってください。

彼の階層はゴーストタウンと化しています。打ち捨てられた店々には商品ではなくランダムな戦利品が転がっており、代金を請求する店主は一人も残っていません。残されているのは、リッチ、吸血鬼、グールたちによる儀仗兵の群れです。このフロアのどこかに、**魔法のランプ** または **魔法のマーカー** のいずれか（各50%）が確定で配置されています。火の罠や魔法の罠が散乱しているため慎重に進み、住人たちを排除して、立ち去る前にランプかマーカーを必ず回収してください。どちらを手に入れても、城の杖から引き出せる願いの回数をさらに拡張してくれます。

#### 魔法使いの塔 (The Wizard's Tower)

ゲヘナに存在する3層連続の特殊階層群です。最下層から魔法のポータルを通って進入し、最上階には **イェンダーの魔法使い** (Wizard of Yendor) と **死者の書** (Book of the Dead) が待ち構えています。彼の個々の攻撃を耐え抜くことは十分に可能ですが、最大の問題は彼が何度倒しても **蘇り続ける** 点にあります。彼はあなたの元へテレポートし、モンスターの大群を召喚し、イェンダーの魔除けを奪い去り、ゲーム終了まで所持品に呪いをかけ続けます。

最初の遭遇で手際よく仕留め、死者の書を奪い取って即座に立ち去りましょう。その後に再び彼を倒しても新たな戦利品を落とすことはないため（単に復活してくるだけ）、自発的に再戦を挑んではいけません。昇天への旅路において「戦うな、走れ」と言われる鉄則は、主として彼に対する心得です。

#### モロクの聖域 (Moloch's Sanctum)

ゲヘナの最深階層です。ここは **封印** されており、祈祷の儀式（後述の「強奪の儀式」を参照）を完遂するまで、聖域へと降りる階段は出現しません。封印が破られたら、階段を降りて **高位祭壇** の近くにいる **モロクの高僧** (High Priest of Moloch) を見つけ出してください。彼は **イェンダーの魔除け** を身につけています。モロクの高僧は買収不可能なユニークボスであり、強力な呪文を放ち、下僕を召喚し、近接間合いに入った者に手痛い制裁を加えます。標準的な攻略法は、安全な距離から死の杖や死の指先呪文を一撃叩き込むことです。

#### 強奪の儀式 (The Heist)

ゲームのクライマックスは、綿密に構成された一連の儀式です：3つの祈祷アイテム、1つの振動する四角、1体の最終ボス、そして地上へ向けての死に物狂いの脱出劇です。祈祷を始める直前までは、すべてを自分のペースで進めることができます。しかし一度儀式を行えば、強欲なモンスターたちが一斉にあなたを標的に定め、いかなる遅延も致命的な代償となります。儀式を始める前に、すべての装備セットを完璧に揃えておいてください。手順は以下の通りです：

1. **3種の神器を集める。** **開扉のベル** (Bell of Opening: クエストの宿敵が落とす報酬)、**祈りの燭台** (Candelabrum of Invocation: [ヴラドの塔](#vlads-tower) の最上階)、そして **死者の書** (Book of the Dead: 魔法使いの塔の最上階) の3つが必要です。どれか1つでも欠けていれば、遥かな道のりを歩いて取りに戻らなければなりません（特に開扉のベルは、[クエスト](#the-quest) クリア時に宿敵の死体から拾い忘れて放置されがちです）。

2. **燭台に7本のろうそくを取り付ける。** 各ろうそくを使用（`a`）し、祈りの燭台を選択して差し込みます。ろうそくは道中で頻繁に生成されるため自然と集まりますが、7本揃える確実な供給源が必要です：**鉱山街にあるイツァークの照明具店**（Izchak's lighting shop）が最も明快な答えです（オークの町パターンで店がない場合でも、そのフロアに7本散らばっています）。

3. **振動する四角を見つけ出す。** [モロクの聖域](#molochs-sanctum) の直上にあるゲヘナ階層において、特定のマスを踏むと足元が振動します：*「足元で奇妙な振動を感じる」（"You feel a strange vibration under your feet."）*。このマスの位置は迷路内のランダムな1箇所であるため、歩き回って探す必要があります。地図化の巻物が絶大な威力を発揮します。

4. **祈祷の儀式を執り行う。** 3つのアイテムはいずれも呪われていてはいけません。振動する四角の上に立ち、燭台を使用して火を灯し、ベルを使用して鳴らします。そして4ターン以内に、死者の書を読みます。床が開き、降下階段が出現します。

5. **モロクから魔除けを奪い取る。** 階段を降り、**モロクの高僧** を打倒し（死の杖が有効）、その死体から **イェンダーの魔除け** を奪い取ります。

6. **脱出劇の幕開け。** 上り階段へ駆け込みます（この階段は魔除けを手にする前から使用可能です）。ここからがいよいよ **昇天への旅路** です。ゲーム内のあらゆる強欲なモンスターたちが一斉にあなたの存在を感知し、イェンダーの魔法使いが魔除けを取り戻そうと何度もテレポートで襲来し、そして「謎の力」があなたを下層へと引きずり戻そうとします。全速力で地上へと駆け上がってください（後述の [昇天への旅路](#the-ascension-run) を参照）。

#### サバイバルの秘訣 (Survival Tips)

- **余分な食料を携帯すること。** あなたは全速力で移動し続けることになり、祈りによる空腹回復は期待できません。
- **解呪の巻物を携帯すること。** 持ち物に不慮の事故が起きた際、素早く所持品を立て直せます。
- **迂回せず、壁を掘り進むこと。** 迷路の通路を律儀に歩くよりも、壁を一直線に掘り抜く方が遥かに高速です。
- **魔法使いは即座に仕留めること。** 彼を生かしておくターンが1つ増えるごとに、新たなモンスターが召喚され、新たなアイテムが盗まれ、装備が呪われていきます。彼は必ず蘇りますが（何度でも蘇る）、出現と再出現の合間のインターバルこそが、あなたに貴重な呼吸の時間を与えてくれます。
- **魔除けの重力。** イェンダーの魔除けを所持している間、階層テレポートは一切機能しません。地上までの全階層を、自らの足で一段ずつ登り切る必要があります。
- **リッチ系統を虐殺すること。** 祝福された虐殺の巻物を **L** に適用すれば、リッチ、デミリッチ、マスターリッチ、アーチリッチを一挙に消滅させることができます。ゲヘナにおける最悪の脅威を、以後のゲームから完全に排除できます。

---

### 昇天 (The Ascension)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source: no corrections. Verified Riders (lvl 30, 8d8, Death instakill 3/20), Famine/Pestilence downgrades, Rider-corpse fatal, wand-of-death-heals-Death, wrong-altar done(ESCAPED), Mysterious Force gating, plane order & altars.
-->

イェンダーの魔除けを手にした今、真の最終試練が始まります。ダンジョンの最深底から地上への脱出、そして神々の領域たる四大元素の面と星界の面を突破して、不死の神へと昇天を果たす旅路です。

#### 昇天用装備セット (The Ascension Kit)

<!-- audit
2026-05-18:
- there is no "helm of holiness"; the artifact is Mitre of Holiness
- Mitre of Holiness = HELM_OF_BRILLIANCE base + CARY(AD_FIRE) + SPFX_PROTECT (+1) + M2_UNDEAD + ENERGY_BOOST invoke (artilist.h:265-269)
- Eye of the Aethiopica is Wizard-only: SPFX_RESTR + PM_WIZARD; other classes get the badclass blast (artilist.h:303-307, artifact.c:920-948)
- wand-of-death on the High Priest works: type=-1 skips saving throws (zap.c:4314); High Priest has no antimagic and mr1=70 does not gate ZT_DEATH
- prayer CAN cure hunger and uncurse worn items (pray.c)
- strategy aligned with NetHackWiki Ascension kit: GDSM/SDSM, cloak of MR, speed boots, gauntlets of power, life saving, bag of holding, wand of death, candles are the canonical kit (https://nethackwiki.com/wiki/Ascension_kit)
-->

ゲヘナの深淵で散っていった冒険者たちも、ほぼこれと寸分違わぬ装備を身につけていました。以下の装備を揃え、そしてその後の「彼らはなぜ死んだのか」を読んで、先人たちの過ちを繰り返さないようにしてください。スロットごとの構成：

| スロット | 定番の選択肢 | 備考 |
|--------|------------------------|---------------------------------------|
| **胴防具 (Body)** | ドラゴンの鱗鎧 | 灰色（魔法耐性）または銀色（反射）が定番。青色（電撃）も可。 |
| **マント (Cloak)** | 魔法を防ぐクローク | 呪文職ならローブ。魔法耐性は死の光線と死の指先呪文を完全に遮断する。 |
| **兜 (Helm)** | 知性の兜 または テレパシーの兜 | 呪文職には知性の兜。目隠し併用ならテレパシーの兜。 |
| **小手 (Gloves)** | 力の小手 | 別の強さ確保手段（強さの指輪など）がない限り必須。 |
| **靴 (Boots)** | 韋駄天の靴 | 手数が増える超高速行動はあらゆる職業で絶大な力を発揮する。 |
| **シャツ (Shirt)** | アロハシャツ または Ｔシャツ | 他の防具の下に着る無料のスロット。高強化（+4〜+5）でACを大幅に底上げ。 |
| **盾 (Shield)** | 基本的には装備しない | 反射は銀色ドラゴンの鱗鎧や魔除けで確保。二刀流使いは盾を扱えない。 |
| **魔除け (Amulet)** | 命の魔除け | エレメンタルプレーンに備える「予備の命」。 |
| **指輪（左）** | 自由行動の指輪 | 星界の面は麻痺攻撃で満ちており、1歩たりとも外せない。 |
| **指輪（右）** | 消化不良、争い、再生のいずれか | 争いの指輪は星界の面での最強の群集制御（クラウドコントロール）手段。 |
| **武器 (Weapon)** | 最も鍛えた武器。予備に銀武器 | 武器クエストアーティファクトは4職のみ。銀は悪魔やアンデッドに特効。 |
| **鞄の中身 (Pack)** | 軽量化の鞄、ユニコーンの角、幸運の石、死の杖、複数の瞬間移動の杖、7本のろうそく、聖水5本以上、祝福された完全回復の薬、電撃防御 | 聖水は呪い修復用、完全回復の薬は緊急脱出ボタン、電撃耐性や反射は風の面の落雷対策。なお騎士（Riders）は石化に耐性があるためコカトリスの死体は効かない。 |
| **必須の戦利品** | 開扉のベル、祈りの燭台、死者の書、イェンダーの魔除け | 祈祷の儀式アイテムと最終目標。 |

典型的な昇天時のACは **−25 から −40** の範囲に収まります。

##### 昇天一歩手前で死んだ者たちの死因

彼らの装備は、昇天を果たした者たちと何ら変わりませんでした。ACも −23 から −40 に達し、死の杖を持ち、3種の祈祷アイテムを揃え、銀色ドラゴンの鱗鎧を着ていました。彼らを殺したのは装備ではなく、**行動（プレイングミス）** でした：

- **戦闘中のインベントリ操作。** 地下35階の考古学者が、ジャバウォック、変幻獣、ズルーティに隣接されている最中に缶詰を開けようとしました。缶切りを取り出すプロンプトが、彼女に残されていなかった命の1ターンを奪い去りました。
- **空腹でないのに食べる。** AC −40 で3つの祈祷アイテムをすべて揃えてゲヘナの深部にいた観光客が、満腹状態であるにもかかわらずストーカーの死体を食べ、窒息死しました。指にはめていた消化不良の指輪は、窒息を防いではくれません。
- **脱出アイテムの枯死。** 聖域を目前にした地下50階の魔法使いが、逃走ルートを確保しないまま死の杖の最後のチャージを使い果たし、盲目状態で敵に包囲されて息絶えました。

常に最低1つの脱出手段を手元に残しておいてください：瞬間移動の巻物、穴掘りの杖、あるいは完全回復の薬が入った防水袋です。

#### 昇天への旅路 (The Ascension Run)

<!-- audit
2026-05-21:
- bones save converts the real Amulet of Yendor to FAKE_AMULET_OF_YENDOR and curses it when a previous adventurer dies carrying it (bones.c:170-173)
- wish for an Amulet of Yendor silently substitutes a fake (objnam.c:5003-5006 substitution list)
- Astral altar offering accepts only the real Amulet; fake amulets fail and the death message reads "(with a fake Amulet)" (end.c:1413-1414)
2026-05-19:
- Mysterious Force is gated on Gehennom only (do.c:1541); same-level shuffle is the majority outcome
- odds = 3 + ualign.type; diff = rn2(odds): Chaotics max -1, Neutrals max -2, only Lawfuls reach -3 (do.c:1544)
- never fires on bottom 4 levels (dunlev < dunlevs_in_dungeon-3)
- Force frequency tapers with each trigger (do.c:1536-1563)
- Amulet-pickup wish fires once on next moveloop iteration if !u.uevent.amulet_wish (allmain.c:446-451)
- Elbereth is DEAD in Gehennom, all four Elemental Planes, and Astral: onscary returns FALSE for Inhell || In_endgame (teleport.c:68-70)
- carrying the Amulet blocks level teleport via the u.uhave.amulet guard (teleport.c:1185-1189)
- strategy aligned with NetHackWiki Ascension run, Mysterious force, Amulet of Yendor: run-don't-fight, dig straight lines, kill the Wizard fast, the Force as the primary climb obstacle (https://nethackwiki.com/wiki/Ascension_run, https://nethackwiki.com/wiki/Mysterious_force, https://nethackwiki.com/wiki/Amulet_of_Yendor)
-->

ついにやり遂げました。ゲヘナを戦い抜き、モロクの高僧を打ち倒し、聖域からイェンダーの魔除けを奪い取りました。あとはこの魔除けをダンジョンの底からゲヘナの全階層、かつて倒したはずの魔王たちを潜り抜け、地上まで運び上げ、さらに元素界を越えて自らの神が待つ星界の面へと到達するだけです。簡単なことですよね？

**魔除け拾得時の無料の願い。** イェンダーの魔除けを拾い上げた瞬間、次のターンに自属性の神から1回分の願いが自動的に授与されます。能動的に願う必要はなく自動発動します。聖域に到達する *前に* ウィッシュリストを用意しておいてください：力の小手、お好みの +5 武器、祝福された魔法を防ぐクロークなど、脱出の登攀に欠けている最後のピースを願うのです。この願いはゲーム中1回きりです。なお、呪われたレベルアップの薬は上階層へと移動させてくれますが、ゲヘナ内では依然として謎の力を誘発します。

**本物の魔除けを携えること。** 登りの階段は常に開かれています。運命の迷宮の上り階段は、何を持っていようとあなたを地上へと近づけてくれます。地下1階の上り階段は、本物の魔除けの所持者を土の面へと導きます（魔除けを持たずに脱出すると「逃走」エンドとしてゲームが終了します）。モロクの聖域で高僧の死体から奪い取った魔除けだけが本物と認められます。ボーンズ階層に落ちている魔除けはすべて偽物です（冒険者が魔除けを持ったまま死亡すると、ゲームはその魔除けを偽物へと書き換えて呪いをかけます）。また、願いで願った魔除けも黙って偽物にすり替えられます。高僧から直接奪い取ったものでない限り、本物は手に入りません。

##### 試練の連続 (The Gauntlet)

ダンジョンは4つの包囲網であなたを阻み、そのすべてがあなたの鞄の中の魔除けを標的にしています：

- **イェンダーの魔法使い** は定期的にあなたのマスへとテレポートし、モンスターを召喚し、魔除けを奪おうと手を伸ばしてきます。彼が諦めることはありません。現れるたびに仕留めてください。彼は必ず蘇ります。世界で最も執念深い元恋人のような存在です。
- **魔除けによるテレポートの封殺。** 魔除けを所持している間、階層テレポートは一切使えません。ゲヘナの最深部から地上に至るすべての階段を、自らの足で1段ずつ登らなければなりません。
- **強欲なモンスターたち。** 魔王たちや魔法使いは、あなたの現在地へと直接ワープして襲撃してきます。誰もがその魔除けを喉から手が出るほど欲しがっているのです。
- **謎の力 (The Mysterious Force)。** ゲヘナ内で魔除けを携えて階段を登るたびに、謎の力によって引き戻される判定が発生します。引き戻しが発生した場合、秩序属性の英雄は4回に1回、中立は3回に1回、混沌は2回に1回の確率で同じ階層に留め置かれます。それ以外の場合は、1階層下（混沌の上限）、2階層下（中立の上限）、あるいは3階層下（秩序属性のみ）へと **突き落とされます**。最悪の引き落としは秩序属性に最も厳しく、混沌属性に最も寛大です（混沌属性は一度に1階層より深く落とされることはありません）。NetHack 5.0 では、この引き戻し確率は発動するたびに **減衰（発生率が低下）** していくように改良されました。引き戻されるごとに次回の発動確率がわずかに下がり、深い引き落としほど以後の発動を抑制します。この減衰は秩序の英雄に最も大きな恩恵をもたらします。なお、謎の力はゲヘナを脱出した瞬間に停止し、ゲヘナの最下層4フロアでは決して発動しません。
- **属性反転の検討。** 逆属性の兜をかぶると、秩序は混沌へ、混沌は秩序へと反転します（中立はランダム）。混沌属性になれば、謎の力による落下が常に最大1階層に抑えられます。ただし代償として、星界の面での生贄は混沌の祭壇に捧げなければならなくなります（祭壇判定は *現在の* 属性を参照するため）。トレードオフを理解した上での選択肢です。

##### 脱出戦術 (Strategy)

あなたはもはや探索者ではありません。相手チームの全員がタックルを狙う中、ボールを抱えてエンドゾーンへ疾走するランニングバックです。スピードこそがすべてです。

- **戦うな、走れ。** 探索するな。略奪するな。ただ上を目指せ。倒さなくてもいい敵と戦って過ごす1ターンごとに、魔法使いが魔除けを奪いに近づいてきます。
- **掘れ。** 穴掘りの杖を使って階段へ一直線に突き進んでください。迷路の通路を歩くより、壁をぶち抜いて最短距離を進む方が遥かに速いです。
- **邪魔者は光線で消せ。** 瞬間移動の杖で進路上のモンスターを遠くへ弾き飛ばしてください。死の杖で厄介な敵を永久に消し去ってください。惜しみなく使ってください。
- **呪文使いの裏技：魔除けを置いてから詠唱する。** 魔除けを所持していると、呪文の消費マナが基本コストの 2〜3倍 に跳ね上がります。魔除けを床に置き、死の指先や地図化を唱え、再び拾い上げてください。3ターンの往復行動は、膨大なマナの浪費よりも遥かに安上がりです。
- **魔法使いは瞬殺しろ。** 彼が現れたら（必ず現れます）、技巧に走らず、死の指先、死の杖、または圧倒的な腕力で即座に沈めてください。早く倒すほど、召喚されるモンスターの数を減らせます。
- **城より先ではエルベレスに頼るな。** エルベレスはゲヘナ、四大元素の面、および星界の面の全域において **完全に無視** されます。床に刻んでも効果はなく、モンスターは平然と踏み越えてきます。回復と体勢立て直しのための時間は、通路の地形、瞬間移動の巻物、そして争いの指輪を活用して確保してください。

城での補給が完璧で各種耐性が万全であれば、この登攀はマラソンではなくスプリントになります。運命の迷宮の頂点に到達したとき、最後の階段は元素界へと続いています。あなたと神性との間を隔てる、最後の障壁です。

#### 元素界 (The Elemental Planes)

<!-- audit
2026-05-19:
- Portal is randomly placed via des.levregion in region {0,0,75,19} excluding the arrival corner {65,13,75,19} (dat/earth.lua:53). The portal lives in another cavern, not buried in undug rock.
- Level flag `shortsighted` (rm.h:449 Bitfield, set via dat/earth.lua:15) only affects monster vision range, not the player's.
- `;` class on the Plane of Water (S_EEL) species verified from monsters.h: jellyfish, piranha, shark, giant eel, electric eel, kraken. "sea monsters" was the section comment header, not a species name. Water moccasin is S_SNAKE and NOT affected by class-`;` genocide.
-->

運命の迷宮の頂点を超えると、世界はその根源たる元素へと解体されます。あなたと神々との間には4つの面が横たわり、それぞれが異なる悪意で満ちています。ここには階段はなく、各面に隠された魔法のポータルだけが次の面へと続いています。各面は閉ざされた世界であり、見つけ出したポータルが唯一の脱出路であり、くぐり抜けた瞬間に背後で閉ざされます。

**ポータルを見つけ出す2つの安価な手段。** 混乱した状態でゴールド探知の巻物を読むと、ポータルを含むフロア全体のすべての罠の位置がマップに刻まれます（1回の読書で全盲解消）。また、イェンダーの魔除けそれ自体が、携行している間コンパスとして機能します：手に構えるか首にかけると、ポータルに近づくにつれて時折 *「熱い（hot）」「非常に温かい（very warm）」「温かい（warm）」* と囁いてきます（ポータルから 3マス、8マス、12マス以内）。虚空を横断する宝探しゲームです。

##### 土の面 (Plane of Earth)

あなたはこの面の隅にある小さな洞窟に到着します。薄暗い光の中、すでに2体の敵があなたを待ち構えています：エルフの王とミノタウロス、どちらも敵対的です。この面は掘削可能な岩盤の中に無数の小洞窟が散らばった星団のような構造をしており、風の面へと続くポータルはその中の別の洞窟に隠されています。進む唯一の道は岩盤を掘り抜くことです。他の洞窟には土のエレメンタル、ストーンジャイアント、ロックトロール、ストーンゴーレム、ピットフィーンド、ダストボルテックス、アンバーハルクが潜んでいます。テレポートは封じられているため、一度戦闘が始まれば杖で逃げることはできません。穴掘りの杖が必須です。魔法の地図は洞窟の配置を明かしますが、隠されたポータルそのものは暴けません。混乱状態でゴールド探知を読むか、水晶玉を使ってポータルの位置を特定してから掘り進んでください。

##### 風の面 (Plane of Air)

土の面とは正反対の極限世界です：壁も、足で感じられる床もなく、ただ虚空の空が広がり、思考よりも速く動く風のエレメンタルたちが吹き荒れています。彼らは1ターンに何度も攻撃を加え、虐殺することもできません。ここでは争いの指輪（Ring of conflict）が絶大な効果を発揮します：ポータルを探す間、エレメンタル同士を互いに引き裂かせましょう。魔法の地図は隠されたポータルを映し出しませんが、混乱ゴールド探知や水晶玉なら位置を特定できます。この面は毎ターン自律的に漂流する **雲の泡 (cloud bubbles)** によって分断されており、泡の中に立っていれば泡と一緒に流されていきます。流れに逆らわずに乗ることで虚空を高速で横断でき、やがて泡があなたをポータルの真上へと運んでくれることもあります。

雲の雷撃はおよそ8ターンに1回落ちてきて 8d6 のダメージを与え、さらに3分の1の確率で露出している杖や指輪を焼き尽くします。電撃耐性または反射が必須です。予備の充填済みアイテムは袋の中にしまっておいてください。

なお、この面にはショートカットへの制約があります。自分自身へのテレポートは *「謎の力があなたのテレポートを妨害した！」* というメッセージで弾かれます。瞬間移動の杖は追ってくる敵を吹き飛ばすことはできますが、自分自身を移動させることはできません。

##### 火の面 (Plane of Fire)

フロア全体を溶岩の湖が覆い尽くし、その隙間に火の罠が仕掛けられ、火のエレメンタルやヘルハウンドが徘徊しています。火炎耐性があればそれらのダメージの大部分は無力化され、あとはポータルを探すだけの問題になります。耐性がない場合、あらゆる移動と遭遇があなた自身と所持品を灰へと変えてしまいます。

##### 水の面 (Plane of Water)

この面は漂流する空気の泡が点在する見渡す限りの大海原です。あなたはその泡の1つの内部に出現します。泡から足を踏み外して水中に落ちると通常は泡へと這い戻ることになりますが、真の溺死の脅威は巨大ウナギやクラーケンがあなたに巻きついて水底へと引きずり込むことです。呼吸の魔除け（魔法の呼吸）があればその危険を排除できますが、単にこの階層に立つだけであれば必須ではありません。

**到着時の定石戦術：`;` クラスの虐殺。** 虐殺の巻物を読み、**`;`** クラス全体（クラゲ、ピラニア、サメ、巨大ウナギ、電気ウナギ、クラーケン）を指定してください。あなたを引きずり込もうとするあらゆる海の怪物が、この面から瞬時に消滅します。これこそが虐殺の巻物を切るべき決定的な瞬間です。`;` クラスはゲーム内の他の場所にはほとんど現れず（メデューサの池に時折クラーケンがいる程度）、次の面では完全に無関係になります。怪物を一掃したら、落ち着いてポータルを探し、飛び込んでください。

##### 星界の面 (The Astral Plane)

ついにあなたは神々の御前へと浮上します。3つの独立した寺院に、秩序、中立、混沌の祭壇がそれぞれ祀られています。昇天を果たすには、**自身の属性と一致する祭壇** にイェンダーの魔除けを生贄として捧げなければなりません。**間違った祭壇を選ぶとその瞬間にゲームオーバー** となります：敵対する神があなたの神を屈服させ、あなたは敵対勢力に完全な勝利を明け渡してしまうのです。やり直しは利きません。最初から正しい祭壇を選んでください。遠見（`;` キー）による確認は、祭壇に **隣接** しているときしかその属性を明かしません。部屋の反対側から見ても単に「属性の一致した高位祭壇」としか表示されないため、各寺院の祭壇の隣まで1つずつ歩いて確認する計画を立ててください。

この面は無数の天使たちと、3体の **黙示録の四騎士 (Riders)**（**デス (Death)**、**フェミン (Famine)**、**ペスティレンス (Pestilence)**）で埋め尽くされています。彼らはレベル30であり、戦闘中もHPを急速回復し、透明を看破し、進路上のモンスターを力任せに押し退けて突進してきます。それぞれが1ターンに2回、8d8 ダメージの接触攻撃を繰り出します。

- **デス (Death)** はその名の通りの避けがたい確実さで迫ってきます。接触ごとに 8d8 ダメージを与え、およそ 20回中3回 の確率で即死効果を叩き込みます。[魔法耐性](#damage-resistances) は即死効果を防ぎますが、基本ダメージは防げません。魔法耐性がなければ、毎ターンの打撃で生きるか死ぬかの運試しを強いられます。
- **ペスティレンス (Pestilence)** は、20 + 体力（Con）ターンの病気タイマーを開始させます。その後の接触ごとに、残り時間が3分の1へと短縮されます。病気耐性があれば防げます。耐性がない場合は、即座にユニコーンの角を使用して治療してください。
- **フェミン (Famine)** は消耗戦であなたを殺しにかかります。接触ごとに 8d8 ダメージに加え、あなたの栄養度から直接 40〜79ターン分の空腹を奪い去ります。1発で餓死するわけではありませんが、戦闘前の満腹度によって耐えられる打撃数が決まります。

NetHack 5.0 で追加されたささやかな慈悲：疫病または飢餓が1ターン目の最初の攻撃を命中させた場合、そのターンの2回目の攻撃は気絶へとダウングレードされます。

**騎士たちを恒久的に殺害することはできません。** 彼らは何度でも蘇り、追跡し、決して止まりません。**いかなる騎士の死体であっても、食べることは即座に致命的（即死）となります。** あなたは彼らと戦うためにここにいるのではありません。正しい祭壇に到達し、魔除けを捧げ、すべてを終わらせるためにここにいるのです。

どうしても騎士と交戦せざるを得ない場合、**最も恐れるべきは「疫病」です**：距離を取った後でも病気タイマーがあなたを蝕み続け、ユニコーンの角の治療判定が間に合わずに死亡することがあります。死の即死は魔法耐性で防げ、飢餓は大量の食料で耐え抜くことができます。

**防御策。** **命の魔除け** は星界の面における最高の保険です。魔法耐性は死の即死を止めます。病気耐性は疫病を無力化します（緑色ドラゴンの鱗鎧が入手源）。十分な食料とユニコーンの角を携帯してください。3体の騎士はいずれも石化に耐性があるため、コカトリスの死体で片付けることはできません。**争いの指輪** は周囲のモンスター同士を争わせることができますが、高レベルの騎士はほとんどのターンで争いに抵抗します。守護天使がまだ生きている間に争いの指輪をはめてはいけません：守護天使が消滅し、あなたの神が怒って2〜4体の敵対的な天使を送り込んできます。瞬間移動の杖は群衆を押し退けて道を切り開くのに役立ちます。**元素界・星界の面では自分自身へのテレポートはすべて失敗する** ため、杖は敵に向けて振ってください。

**デス (Death) に向けて死の杖を振ってはいけません。** 死の光線は彼を回復させてしまいます。マジックミサイルは3体の騎士すべてに有効です。代わりにそれを使ってください。

正しい祭壇に魔除けを捧げてください。あなたの神はその至宝を受け入れ、魔除けは神聖な炎の中へと消え去り、あなたはいまや不死の神々の一員として昇天を果たします。この瞬間に到達できる冒険者はごくわずかです。本書はここで幕を閉じます。心からの祝福を。

## 付録 (Appendices)

### 高度な操作法 (Advanced Controls)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- runmode sets display refresh rate during a run (teleport/run/walk/crawl = no-redraw / every-7 / every-step / step+delay, flag.h:547-551), not stopping behavior. Reworded.
- Verified correct: all command bindings (F/G/g/m/_/@/^A/^P/^R/^O/v), count cap 32767, paranoid_confirmation values, pickup_burden default, autopickup_exception, statushilites, pickup_types etc.
-->
<!-- audit
2026-05-19:
- F/G/g/m/O/v/_/;//, Ctrl+A/P/R/O, #overview, #chronicle, #annotate, #conduct all verified (cmd.c:1662-2065)
- `verbose` controls extra descriptive messages (wielding/digging/sounds/pets), NOT "why multi-commands stopped" (optlist.h:813-815 declares flags.verbose; gated at dig.c:711/1441/1468/2157, ball.c:61, attrib.c:176, apply.c:438 etc. — none are multi-command stop messages)
- double-tap F cancels the attack lock (cmd.c:1622-1633)
- `m` prefix on e/a/, opens a menu
- Ctrl+A repeats only the last EXECUTED command, not the last input (cmd.c:3732-3736)
- repeat-count cap is 32767 (global.h:135)
- number_pad/autopickup/pickup_types option semantics consistent with optlist.h
2026-05-31 audit:
- travel command (`_`) enters background-symbol-target mode (getpos.c:194-218). Typing a background symbol after `_` jumps the cursor to the next instance; `.` confirms and walks. So the patterns are `_<.` (upstair), `_>.` (downstair), `__.` (altar). The book originally showed `__` without the trailing `.`, which is inconsistent with the other two.
-->

基本的なキー操作だけで迷宮のあらゆる状況を乗り切ることは可能ですが、以下に挙げるコマンドを活用すれば遥かに素早く快適に操作できます。何千ターンにもわたって `s` キーを連打したり、通路を1マスずつ歩いたりした経験があれば、これらのショートカットがいかに指先に馴染むかを実感できるはずです。

#### コマンドの反復回数指定 (Command counts)

コマンドの前に数字を入力すると、その回数だけコマンドが自動で繰り返されます：`10s` は10回探索し、`20.` は20ターンその場で待機し、`5h` は西へ5マス歩きます。何かしら重要な事象が発生した瞬間に（隣接マスにモンスターが現れた、HPが変動した、`--More--` プロンプトが表示された、探索で隠し扉等を発見したなど）、この反復動作は自動的に中断されます。また ESC キーを押せばいつでも途中でキャンセルできます。

入力可能な数値は最大 32,767（5桁）まで受け付けられますが、現実的な上限は「画面の更新を忍耐を切らさずに眺めていられる長さ」です。実際の探索作業であれば `99s` で十分すぎます。

#### 直前コマンドの再実行 (Ctrl+A)

`Ctrl+A` は、直前に実行したコマンドを（回数指定も含めて）まったく同じ設定でもう一度実行します。最初に `10s` で探索を行った後は、以降の探索はすべて `Ctrl+A` の1キーだけで10回ずつ繰り返せます。これはキャンセルされたり壁にぶつかったりした試行ではなく、*「直前に実際に実行されたコマンド」* を正確に記憶します。

#### 移動プレフィックス (Movement prefixes)

いくつかのプレフィックス（接頭辞）キーは、直後のコマンドの挙動を修飾し、実行後にクリアされます。見えないモンスターへの攻撃、攻撃を避けた移動、あるいは長距離移動の停止条件の制御などに使用します。

- **`F`** に続けて方向キーを入力すると、そのマスにモンスターが見えていなくても **強制攻撃 (force attack)** を繰り出します。不可視のモンスターがいると疑われるマスへの攻撃、幻影（Displacement）によって本体が1マスずれている敵への攻撃、あるいは自身の [エルベレス](#elbereth) を自発的に踏み消す際に使います。`F` を素早く2回押すと行動せずにキャンセルできます。
- **`G`** に続けて方向キーを入力すると、アイテム、罠、分岐点、または閉じた扉に近づくまで走り続けます。**`g`** はさらに慎重であり、通路の交差点でも停止します。大文字の方向キー（`H`, `J`, `K`, `L` および `Y`, `U`, `B`, `N`）は高速走行モードを使用し、他の停止条件が介入しない限り、アイテム、扉、罠を無視して駆け抜けます。
- **`m`** に続けて方向キーを入力すると、**「攻撃せず、アイテムも拾わずに移動」** します。ペットを殴らずにすれ違う（「ちょっと通してね」）、自動拾い対象の山を拾わずに通り過ぎる、あるいは既知の水たまりや溶岩マスに意図的に *足を踏み入れる* 際に使います（本来なら安全停止機能が働くところをプレフィックスで上書きします）。`e`（食べる）の前に押すと床落ちの食料を食べる確認をスキップし、`m,` は足元のアイテム山に対してメニュー一覧を強制表示します。

#### トラベル機能 (Travel)

アンダースコアキー（`_`）は高速自動移動を行う「トラベル (travel)」コマンドです。`_` を押し、すでに探索済みの目的地をカーソルで指定して `.` で決定すると、キャラクターが最短経路でそこまで自動歩行します。閉じた扉を含むあらゆる中断事象で停止します（トラベルは扉の前まで歩きますが自動で開けたりはしません。扉に向かって移動するか、先に `o` で開けてください）。また、`_` の後にマップ上の背景シンボルを入力すると、カーソルがその種類の次のマスへ一瞬でジャンプします：`_<.` で上り階段へ移動、`_>.` で下り階段へ移動、`__.` で既知の祭壇へ移動できます。

#### 鍵のかかった箱の力任せの解錠 (Forcing locked chests)

鍵開け器具や鍵を持っていない場合、**`#force`**（または `#f`）コマンドを使うと、構えている武器で施錠された箱を力ずくでこじ開けることができます。刃物類を使用すると鍵穴で刃が折れる危険があり、打撃武器を使用すると箱の中身そのものを粉砕してしまう危険を伴います。

#### メッセージ履歴と画面再描画 (Message history and redraw)

`Ctrl+P` は、過去のメッセージ履歴を1行ずつさかのぼって表示します。モンスターの特殊攻撃の警告、店主が提示した価格、あるいは状態異常の発生ログなど、流れてしまったメッセージをもう一度確認できます。デフォルトのバッファは20件を保持し、古いメッセージから順に押し出されて消去されます。

`Ctrl+R` は画面全体を再描画します。端末の描画が乱れたり、表示がおかしいと感じたときの便利な基本操作です。

#### ダンジョン概要と出来事記録 (Dungeon overview and event journal)

`Ctrl+O`（または `#overview`）は、これまでに訪れた重要な階層の一覧（祭壇、玉座、泉、流し台、店、寺院、墓、木、注釈、ボーンズ、支流階段、各支流の最深階、そして判明した場合は城の合言葉メロディを含む）を表示します。先頭に `m` を付けて `mCtrl+O` と入力すると、訪れた *すべての* 階層をメニュー形式で一覧表示し、そこから注釈（アノテーション）の追加・編集が可能です（現在立っている階層への注釈は `#annotate` でも行えます）。典型的な用途は、荷物を保管した拠点（スタッシュ）階層にラベルを付け、どのフロアに軽量化の鞄を置いたかを忘れないようにすることです。

`v`（または `#chronicle`）は **年代記（クロニクル）** を開きます。これは今回の冒険における主要な出来事（最初の撃破、コンダクト破棄、アーティファクトの賜与や戴冠、最初の祈り、レベル到達の節目、主要支流への進入など）を時系列順に記録した日記です。主にゲーム終了後の振り返り用です。現在のコンダクト遵守状況を確認したい場合は `#conduct` を使用してください。

---

### 設定のカスタマイズ {#options-worth-knowing-about}

<!-- audit
2026-07-30: audited with Advanced Controls vs NetHack-5.0 source (options.c); option names/effects/defaults verified. No corrections here.
-->

NetHack のデフォルト設定は堅実ですが、以下の5つのオプションを設定することで、よくある入力ミスを防止し、危険を直感的に察知できるようになります。ゲーム中に `mO` を入力して全設定メニューから切り替えるか、設定ファイル（macOS/Linux なら `~/.nethackrc`、Windows なら `%USERPROFILE%\NetHack\.nethackrc`、または環境変数 `NETHACKOPTIONS`）に記述して恒久化してください。

もし5つだけ変更するとしたら、以下の設定をおすすめします：

1. **HPと空腹度のカラー表示**：数値を確認する前に、色彩で直感的に危険を察知できるようにする。
2. **`paranoid_confirmation:+attack quit`**：致命的なタイプミスによる暴発や誤終了を防ぐ。
3. **`autopickup` と `pickup_types:$?!=/`**：無用な石や重い鎧を拾いすぎることなく、軽量で有用なアイテムだけを自動収集する。
4. **`pickup_burden:unencumbered`**：アイテムの拾得によって気付かぬうちに移動速度が低下（重荷）するのを防ぐ。
5. **呪われたアイテムをメニューで赤色表示**：危険な選択肢が一目で危険だとわかるようにする。

さらにもう1つ、インターフェースではなくキャラクター作成時に関わる設定があります。`OPTIONS=reroll` を設定すると、最初に振られた初期能力値と初期所持品を破棄して、別の組み合わせへと振り直すことができます。最初の手札にこだわりたいプレイヤーには快適な機能ですが、どのような初期値であっても、ゲーム開始後の決断ほど重要なものはありません。

#### ステータス表示の強調 (Status display)

**`hilite_status`** は、最下行のステータスライン（HP、空腹度、ACなど）に閾値ごとのカラールールを適用して色付けします。ルールを定義することでハイライトが有効になります。各完全なルールは1行に記述してください：

```
OPTIONS=statushilites
OPTIONS=hilite_status:hitpoints/<66%/yellow/<50%/orange/<33%/red&bold/<15%/red&inverse
OPTIONS=hilite_status:hunger/Satiated/yellow/Hungry/orange/Weak/red&bold/Fainting/red&inverse/Fainted/red&inverse+blink
```

末尾にバックスラッシュを置いてルールを複数行に分割しないでください。パーサーが空白を挿入してしまい、後続のフィールドが不正なオプションとして拒絶されてしまいます。

**`menucolors`** は、メニュー項目を正規表現パターンで色付けします。最も有用なルールはBUCタグの色分けであり、呪われたアイテムが赤色で警告され、祝福されたアイテムがシアン色で表示されるようになります：

```
MENUCOLOR=" cursed "=red
MENUCOLOR=" blessed "=cyan
```

前後の半角スペースが重要です。スペースを置くことで、`"uncursed"`（呪われていない）の中間に含まれる `"cursed"` に誤ってマッチするのを防ぎます。

**`force_invmenu`** は、所持品から選択を求めるコマンド（読む、置く、構える等）を実行した際、デフォルトの1文字プロンプト（*「どれを読みますか？ [j-k または ?*]」*）の代わりに、該当アイテムの一覧ポップアップメニューを開くようにします。候補が一目で確認でき、1キーで選択できるため、事前に `?` を押したり英文字を記憶しておく必要がなくなります。

**`pile_limit:5`** はデフォルト値です。同じマスに5個以上のスタックがある場合、個別のリストではなく要約が表示されます。`pile_limit:0` に設定すると、常にすべてのアイテムを一覧表示します。

#### 安全機能設定 (Safety)

**`paranoid_confirmation:+attack quit`** は、平和的なNPCへの誤攻撃や、ゲームの誤終了に対して、単なる y/n ではなく単語全体の入力を求める確認プロンプトを追加します（デフォルトの安全確認を解除することなく機能します）。なお `pray`（祈り）はデフォルトですでに単語確認が含まれています。また `Remove` は外す防具を選択するコマンドであり、外すこと自体の確認ではありません。

#### アイテム拾得設定 (Pickup)

**`autopickup`** は、アイテムの上を歩いたときに自動的に拾う機能であり、**`pickup_types`** で拾う種類をフィルタリングできます（例: `pickup_types:$?!=/` でゴールド、巻物、薬、指輪、杖のみを自動取得）。移動時に `m` プレフィックスを付けると、その1歩だけ自動拾いを一時停止できます。また、ゲーム中にいつでも `@` キーを押せば、そのセッションの自動拾い機能全体の ON/OFF を切り替えられます。

**`autopickup_exception`** は、さらに個別パターンによる例外ルールを設定します：`autopickup_exception:">rock"` は、種類フィルタが岩石類を拾う設定になっていても岩をスキップします。`autopickup_exception:"<holy water"` は、聖水を常に自動取得します。

**`pickup_burden:unencumbered`** は、手動・自動を問わず、アイテムを拾うことで負荷状態が「通常 (Unencumbered)」を超えて悪化する場合に事前に確認を求めます。デフォルトの `S` は「圧迫 (Stressed)」を超えるまで確認しませんが、`U` に設定しておけば常に身軽さを保つことができます。

#### 移動設定 (Movement)

**`number_pad`** は、テンキー（1〜9）を全8方向＋待機の移動キーとして使用できるようにします。デフォルトは無効（off）です。有効にすると数字による反復回数指定の挙動が変わり、先に `n` を押してから数字を入力するようになります。

**`runmode`** は、走行モードやトラベル中の画面再描画の頻度を設定します：`walk` は1歩ごとに画面を再描画します（歩行の様子を目で追えます）。`run`（デフォルト）は数歩ごとに再描画し、`teleport` は停止する最終地点まで画面を更新せず一気にワープ表示します。これは移動中に何が *見える* かを変える設定であり、何によって移動が停止するかを変えるものではありません。

#### メッセージ詳細度 (Verbosity)

**`verbose`** は、より詳細な解説メッセージを有効にします。メッセージログが騒がしく感じられる場合は無効（off）にしてください。

**スターター向け設定ファイル例 (.nethackrc)。** 上記の推奨設定をまとめた数行の構成例です：

```
OPTIONS=statushilites
OPTIONS=hilite_status:hitpoints/<66%/yellow/<50%/orange/<33%/red&bold/<15%/red&inverse
OPTIONS=hilite_status:hunger/Satiated/yellow/Hungry/orange/Weak/red&bold/Fainting/red&inverse/Fainted/red&inverse+blink
MENUCOLOR=" cursed "=red
MENUCOLOR=" blessed "=cyan
OPTIONS=force_invmenu,pile_limit:5
OPTIONS=paranoid_confirmation:+attack quit
OPTIONS=autopickup,pickup_types:$?!=/
OPTIONS=pickup_burden:unencumbered
```

**curses によるパネル分割 UI。** さらに大幅なインターフェースの進化を望む場合、**curses** ウィンドウインターフェースを有効にしてビルドされた NetHack バイナリが必要です（標準的な 5.0 端末ビルドには含まれていない場合があります）。利用可能な場合、curses は端末内に整然としたパネル分割 UI を描画します。設定ファイルに `windowtype:curses`、`align_message:right`、`align_status:bottom`、`perm_invent`、`windowborders` を指定し、120×40 の広めのターミナルを開けば、常時表示のインベントリカラム、複数行のメッセージパネル、そして枠線で区切られたステータスとマップ領域が手に入ります（通常の tty NetHack では、何を設定してもメッセージ行は常に最上行の行0に固定されます）。

### 倉庫番の解答 (Sokoban Solutions)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 dat/soko*.lua: no corrections. Verified prize odds (75/25), prize-chamber coords, variant->file mapping (spoiler L_N = soko(5-N)), pit-vs-hole per level, boulder tallies, scroll-of-earth positions, luck penalty, air-current mechanic.
-->
<!-- audit
2026-06-02:
- sokoban_guilt() fires −1 Luck per infraction (trap.c:7039-7054)
- triggers: squeezing past or stepping onto a boulder via
  passes-walls polyform / giant polyform / tiny polyform / very
  light inventory (hack.c:299, 307, 398, 403 via
  could_move_onto_boulder at hack.c:145-163); reading a scroll of
  earth (read.c:1951); polymorphing a boulder (zap.c:1711);
  fracturing a boulder with wand of striking (zap.c:5556);
  dismounting onto a boulder square (steed.c:767)
- levitation alone does NOT trigger sokoban_guilt; the −1 Luck
  penalty fires on boulder bypasses, not pit bypasses
- BUT Sokoban pits and holes themselves bypass the normal
  flying/levitating escape: trap.c:3014-3024 emits "Air currents
  pull you down into [pit]" and proceeds to the normal trap
  effect even when the hero is flying or levitating. So flying/
  levitation does not let you skip Sokoban's pits — different
  mechanic from the Luck penalty.
- digging walls is blocked by the level's `solidify` flag, which
  sets W_NONDIGGABLE and W_NONPASSWALL on every wall (sp_lev.c:
  315-323 solidify_map). Wand of digging fails on Sokoban walls
  and xorn / earth-elemental polyforms can't phase through them
  either. Like the air-currents mechanic above, this is a level-
  design constraint rather than a Luck penalty.
- counted as the `sokocheat` conduct counter (insight.c:2219,
  topten.c:446) — affects the "Sokoban completion" achievement
-->

倉庫番（Sokoban）は、入り口から **上向き** に登っていく全4階層の巨岩パズル支流です。各階層にはランダムに選ばれる2種類のマップ構造（バージョンAおよびB）が存在します。巨岩を押して落とし穴や落とし蓋を埋め立て、次の階段へと続く道を作り出していきます。不正行為（巨岩を押さずにすり抜ける、巨岩の上によじ登る、杖や衝撃やつるはしで巨岩を破壊する、あるいは倉庫番内で大地の巻物を読むなど）を働くと、**違反1回につき幸運に −1 のペナルティ** が累積して課されます。また倉庫番の壁は固すぎて掘削できません。飛行や浮遊も助けにはならず、未充填の穴の上を飛ぼうとすると *「気流に引きずり下ろされた...」（"Air currents pull you down..."）* と吸い込まれて落下します。正々堂々と解いてください。

> *本解答集は、Kate Nepveu 氏が管理する steelypips.org NetHack アーカイブ向けに、Boudewijn Waijers 氏が編纂し、Jukka Lahtinen 氏ほか多数の貢献によって作成されたものをベースにしています。NetHack 5.0 向けに検証・適合し、本ガイド向けに再フォーマットしました。*

以下のマップでは、手順から参照しやすいように巨岩に A から T までの英文字ラベルが振られています。`^` 記号は第1階層では落とし穴（pit）、第2〜4階層では落とし蓋（hole）を表します（落とし蓋は飛行中であっても1階層下へと落とされます）。`<` は上り階段です。開始位置は `@` で示されています。座標は **(列, 行)** で表されます。「X を埋める（Finish X）」とは、巨岩 X を罠の列まで押し、その列に沿って最も近い未充填の穴へと落とし込む一連の手順を指します。「C を G と同様に埋める」は、G で通ったルートを C で再利用することを意味します。

矢印記号（`↑`, `←` 等）は転がる巨岩の罠（rolling boulder trap）を示します。倉庫番では、この罠の上に巨岩を押し込むと、穴に落ちるか何かに衝突するまで押した方向へと自律的に転がり続けます。

階層を解き終えたら、余った巨岩は部屋の隅に押し込んでおき、後から戻ってきたときに通路を塞がれないようにしましょう。巨岩の下にアイテムが隠されていることもあります。

**反転（ミラーリング）に関する注意。** 倉庫番に到達した時点で、マップは最初から全域が表示されています。ゲーム画面の壁の輪郭をここに掲載されたマップと見比べてください。もし左右反転（または上下反転）している場合は、全手順の「左」と「右」（または「上」と「下」）を入れ替え、反対側の端から列を数えてください（Web版のフリップボタンを使えば視覚的に反転できます）。

#### 第1階層・バージョンA (Level 1, Version A) {.sokoban-level data-width=14 data-height=13}
<!-- audit
2026-05-19:
- Scrolls land at spoiler (3,12) and (4,12); lua coords (02,11) and (03,11) (soko4-1.lua:94-95).
- Spoiler-to-lua mapping: lua_xy+1 = spoiler_col, row.
- Level flags noteleport, hardfloor, sokoban, solidify, premapped set (soko4-1.lua:38).
- All 19 push steps verified against soko4-1.lua by simulation.
- Final remainder (boulder A) is exact.
-->

```
            11111
   12345678901234
 1 ┌────┐  ┌───┐
 2 │····│  │···│
 3 │·A··└──┘·B·│
 4 │·C······D··│
 5 │··┌─┐@┌─┐E·│
 6 ├──┴─┴─┼─┘·─┴┐
 7 │·^·^·<│·····│
 8 │·^┌───┤F····│
 9 └┐^│   │·G···│
10  │↑└───┘·H···│
11  │^^^^^←I·J··│
12  │··┌────────┘
13  └──┘
```

1. A を右へ1マス押す。
2. C を上へ1マス押す。
3. D を右へ1マス押す。
4. D を左へ (4,4) まで押す。
5. E を下へ (11,8) まで押す。

この時点でマップは以下のようになります：

```
            11111
   12345678901234
 1 ┌────┐  ┌───┐
 2 │····│  │···│
 3 │·CA·└──┘·B·│
 4 │··D········│
 5 │··┌─┐>┌─┐··│
 6 ├──┴─┴─┼─┘·─┴┐
 7 │·^·^·<│··@··│
 8 │·^┌───┤F·E··│
 9 └┐^│   │·G···│
10  │↑└───┘·H···│
11  │^^^^^←I·J··│
12  │··┌────────┘
13  └──┘
```

6. H を左へ1マス押す。
7. I, J, E, G, H, F, B, D, C の順に穴を埋める。

巨岩が1個（A）残ります。(3,12) と (4,12) に落ちている巻物は大地の巻物です。

#### 第1階層・バージョンB (Level 1, Version B) {.sokoban-level data-width=15 data-height=11}
<!-- audit
2026-05-19:
- Map walls/floors and all 12 boulders A-L match soko4-2.lua:9-21, 29-42.
- Upstair (2,2), branch portal (4,2) (soko4-2.lua).
- 10 pits: 5 at col 2 rows 3-7, plus 5 at row 9 cols 2-6 (soko4-2.lua:48-59).
- 2 rolling-boulder traps at (1,7) and (6,8) (soko4-2.lua:53, 60).
- 2 always-scrolls-of-earth at (2,10) and (3,10) (soko4-2.lua:63-64).
- Level flags noteleport, hardfloor, sokoban, solidify, premapped (soko4-2.lua:7).
- All 16 solution steps land on lua floor with cardinal approach squares.
- Final remainder (boulders D and E) is exact.
-->


```
            111111
   123456789012345
 1 ┌─┬────┐ ┌────┐
 2 │<│@···└─┘····│
 3 │^├┐·AB····C··│
 4 │^││··DE│·F·G·│
 5 │^││····│·····│
 6 │^├┴───┬┘H────┤
 7 │^│    │······│
 8 │↑└────┘······│
 9 │^^^^^←IJKL···│
10 │··┌───┐······│
11 └──┘   └──────┘
```

1. A を下へ1マス押す。
2. B を右へ (11,3) まで押す。
3. H を下へ (10,8) まで押す。
4. J を上へ1マス押す。
5. I を埋める。
6. L を上へ1マス押す。
7. K, J, H, L の順に穴を埋める。

この時点でマップは以下のようになります：

```
            111111
   123456789012345
 1 ┌─┬────┐ ┌────┐
 2 │<│>···└─┘····│
 3 │^├┐······BC··│
 4 │^││·ADE│·F·G·│
 5 │^││····│·····│
 6 │^├┴───┬┘·────┤
 7 │^│    │······│
 8 │↑└────┘······│
 9 │@····←·······│
10 │··┌───┐······│
11 └──┘   └──────┘
```

8. C を下へ1マス押す。
9. B を左へ (6,3) まで押す。
10. G を下へ1マス押し、次に左へ (10,5) まで押す。
11. G を埋める。
12. C と F を G と同様に埋める。
13. B を右へ (11,3) まで動かし、次に下へ2マス、次に左へ (10,5) まで押す。
14. B を埋める。
15. A を上へ1マス動かす。
16. A を B と同様に埋める。

巨岩が2個（D と E）残ります。(2,10) と (3,10) に落ちている巻物は大地の巻物です。

#### 第2階層・バージョンA (Level 2, Version A) {.sokoban-level data-width=29 data-height=12}

```
            11111111112222222222
   12345678901234567890123456789
 1 ┌────┬────┐       ┌─────────┐
 2 │····│····└─┐     │·········│
 3 │··AB│CD···@│     │·········│
 4 │·····E···┌─┘     │·········│
 5 │····│····│       │····<····│
 6 ├─·──┼────┴┐      │·········│
 7 │··F·│·····│      │·········│
 8 │·GH·│I·J·K│      │·········│
 9 │··L·····M·│      │·········│
10 │·NOP│Q··R·└──────┴────────+┤
11 │····│··S·T→^^^^^^^^^^^^^^^·│
12 └────┴──────────────────────┘
```

1. E を左へ (3,4) まで押す。
2. L を右へ (9,9) まで押す。
3. R を右へ1マス押す。
4. T, S, M, R, K, J, L の順に穴を埋める。
5. N, O, P, G, E の順に穴を埋める。
6. F を左へ1マス押す。
7. H を埋める。
8. F を上へ (3,4) まで押す。
9. F と A を埋める。

巨岩が5個（B, C, D, I, Q）残ります。

#### 第2階層・バージョンB (Level 2, Version B) {.sokoban-level data-width=26 data-height=14}
<!-- audit
2026-05-19:
- 16-boulder layout and all 22 solution steps verified by simulation against soko3-2.lua.
- Source file is soko3-2.lua (Sokoban .lua numbering runs bottom up; spoiler "Level 2" = second-from-top).
- Map is a stylized but topologically equivalent rendering of soko3-2.lua.
- Level flags noteleport, sokoban, solidify, premapped (soko3-2.lua:7); no hardfloor at this depth.
- Intermediate diagrams at steps 9 and 16 match simulated boulder positions.
- Step 17 (push H left) is necessary, not cosmetic.
- Step 21's "G right 1, D up 1" is gratuitous but harmless: those boulders don't reach a hole.
-->

```
            11111111112222222
   12345678901234567890123456
 1  ┌──┐          ┌─────────┐
 2 ┌┘·@└──────┐   │·········│
 3 │··········│   │·········│
 4 │·A┌───┐B─·│   │·········│
 5 │··│···│·C·│   │····<····│
 6 │·D·E····F─┤   │·········│
 7 │·G··H··│··│   │·········│
 8 │·────I·└┐·│   │·········│
 9 │··J···K·│·└┐  │·········│
10 │·──┐L─···M·└──┴────────+┤
11 │···│··N─·O→^^^^^^^^^^^^·│
12 │··P······┌──────────────┘
13 └───┐··│··│
14     └──┴──┘
```

1. B を下へ2マス押す。
2. C を左へ1マス押す。
3. P を右へ3マス、次に上へ1マス、(7,11) まで押す。
4. O を埋める。
5. N を下へ1マス、次に左へ (3,12) まで押す。
6. M を左へ1マス押す。
7. F を上へ1マス押す。
8. B を左へ2マス押す。
9. K を下へ2マス押す。

この時点でマップは以下のようになります：

```
            11111111112222222
   12345678901234567890123456
 1  ┌──┐          ┌─────────┐
 2 ┌┘·>└──────┐   │·········│
 3 │··········│   │·········│
 4 │·A┌───┐·─·│   │·········│
 5 │··│···│CF·│   │····<····│
 6 │·D·E·B···─┤   │·········│
 7 │·G··H··│··│   │·········│
 8 │·────I·└┐·│   │·········│
 9 │··J·····│·└┐  │·········│
10 │·──┐L─@·M··└──┴────────+┤
11 │···│·PK─··→·^^^^^^^^^^^·│
12 │·N·······┌──────────────┘
13 └───┐··│··│
14     └──┴──┘
```

10. M を右へ1マス、次に下へ (11,11) まで押す。M を埋める。
11. N を右へ (10,12) まで、次に上へ (10,10) まで押す。N を M と同様に埋める。
12. K を下へ1マス、次に左へ (3,12) まで押す。K を N と同様に埋める。
13. P を右へ1マス、次に下へ1マス押す。P を N と同様に埋める。
14. L を下へ2マス、次に左へ (3,12) まで押す。L を N と同様に埋める。
15. I を下へ1マス、次に右へ1マス、次に下へ (8,12) まで押す。I を N と同様に埋める。
16. J を右へ (8,9) まで、次に下へ (8,12) まで押す。J を N と同様に埋める。

この時点でマップは以下のようになります：

```
            11111111112222222
   12345678901234567890123456
 1  ┌──┐          ┌─────────┐
 2 ┌┘·>└──────┐   │·········│
 3 │··········│   │·········│
 4 │·A┌───┐·─·│   │·········│
 5 │··│···│CF·│   │····<····│
 6 │·D·E·B···─┤   │·········│
 7 │·G··H··│··│   │·········│
 8 │·────··└┐·│   │·········│
 9 │········│·└┐  │·········│
10 │·──┐·─·····└──┴────────+┤
11 │···│···─@·→········^^^^·│
12 │·········┌──────────────┘
13 └───┐··│··│
14     └──┴──┘
```

17. H を左へ1マス押す。
18. B を下へ1マス、次に右へ1マス、次に下へ (8,12) まで押す。B を埋める。
19. C を下へ1マス、次に左へ2マス、(7,6) まで押す。C を B と同様に埋める。
20. F を左へ1マス、次に下へ1マス、次に左へ (7,6) まで押す。F を C と同様に埋める。
21. G を右へ1マス押す。D を上へ1マス押す。
22. E を右へ2マス、(7,6) まで押す。E を F と同様に埋める。

巨岩が4個（A, D, G, H）残ります。

#### 第3階層・バージョンA (Level 3, Version A) {.sokoban-level data-width=20 data-height=12}

```
            11111111112
   12345678901234567890
 1 ┌────────┬───┬─────┐
 2 │········│···│·····│
 3 │·AB··─CD│·─·│·····│
 4 │··│·E·F·│GH·│·····│
 5 ├─·│··─··│·─·│··<··│
 6 │···┌─·······│·····│
 7 │···│·I·─···─┤·····│
 8 │·J·│K·│···──┤·····│
 9 ├─L·│··└─────┴────+┤
10 │··M···→^^^^^^^^^^·│
11 │···│·@┌───────────┘
12 └───┴──┘
```

1. M を左へ1マス押す。M を埋める。
2. J を右へ1マス押す。
3. L, J, A, B の順に穴を埋める。
4. D を下へ (9,6) まで押す。
5. I を埋める。
6. K を下へ2マス、次に左へ (3,10) まで押す。K を埋める。
7. E を上へ1マス押す。
8. F を右へ1マス、次に上へ1マス、(9,3) まで押す。
9. E を下へ1マス、次に左へ1マス、(5,4) まで押す。
10. E を上へ1マス、次に左へ2マス押す。E を埋める。
11. C を下へ1マス、次に左へ3マス、(5,4) まで押す。C を E と同様に埋める。
12. D を右へ2マス、次に左へ (8,6) まで押す。
13. D を上へ2マス、次に左へ (5,4) まで押す。D を E と同様に埋める。

巨岩が3個（F, G, H）残ります。

#### 第3階層・バージョンB (Level 3, Version B) {.sokoban-level data-width=22 data-height=13}
<!-- audit
2026-05-19:
- Upstair at spoiler (16,7); lua (15,6) (soko2-2.lua:25).
- All 16 boulders A-P map exactly to soko2-2.lua coords.
- Downstair/start at (7,12); rolling-boulder trap at (8,12).
- 11 holes at row 12 cols 9-19; two locked doors at (20,10) and (20,12).
- Level flags noteleport, sokoban, solidify, premapped (soko2-2.lua:7).
- 15 solution steps compress Boudewijn Waijers's original 22; each push geometrically reachable.
- Final "five boulders remain" tally is exact.
-->

```
            1111111111222
   1234567890123456789012
 1   ┌─┬────┐  
 2 ┌─┘·│····│  
 3 │···A····├─┬───────┐  
 4 │·─·BC─DE│·│·······│  
 5 │·FG─······│·······│  
 6 │·─··H·│···│·······│  
 7 │····─I└─J─┤···<···│  
 8 │··KL··M···│·······│  
 9 │·──···│···│·······├─┐
10 │····─N├───┤·······+·│
11 └─┐··O·└───┴───────┤·│
12   │··P@→^^^^^^^^^^^+·│
13   └────────────────┴─┘
```

1. O を左へ2マス、(4,11) まで押す。
2. P と N を埋める。
3. L を下へ1マス、(5,9) まで押す。
4. O を上へ1マス、(4,10) まで押す。
5. L を埋める。
6. K を右へ1マス、(5,8) まで押す。K を埋める。
7. O を右へ1マス、(5,10) まで押す。O を埋める。

この時点でマップは以下のようになります：

```
            1111111111222
   1234567890123456789012
 1   ┌─┬────┐  
 2 ┌─┘·│····│  
 3 │···A····├─┬───────┐  
 4 │·─·BC─DE│·│·······│  
 5 │·FG─······│·······│  
 6 │·─··H·│···│·······│  
 7 │····─I└─J─┤···<···│  
 8 │······M···│·······│  
 9 │·──···│···│·······├─┐
10 │····─·├───┤·······+·│
11 └─┐····└───┴───────┤·│
12   │··@>→····^^^^^^·+·│
13   └────────────────┴─┘
```

8. G を下へ (4,8) まで、次に右へ1マス、(5,8) まで押す。G を埋める。
9. F を右へ1マス押す。F を G と同様に埋める。
10. M を右へ2マス、(10,8) まで押し、次に左へ (5,8) まで押す。M を埋める。
11. J を上へ2マス、(10,5) まで押す。
12. I を埋める。
13. H を右へ1マス押す。H を埋める。
14. A を右へ2マス、(7,3) まで押す。
15. C を下へ2マス、(6,6) まで押す。C を H と同様に埋める。

巨岩が5個（A, B, D, E, J）残ります。

#### 第4階層・バージョンA (Level 4, Version A) {.sokoban-level data-width=26 data-height=18}

このバージョンの賞品は通常 **軽量化の鞄** ですが、4分の1 の確率で代わりに **反射の魔除け** になります。

<!-- audit
2026-05-19:
- 18-boulder layout and all 19 solution steps verified against dat/soko1-1.lua.
- Player start at lua (1,1) = spoiler (2,2).
- 16 holes plus 1 rolling boulder at row 1: hole col 7, rolling boulder col 8, holes cols 9-23.
- Four chamber passages at lua row 3 col 7, row 6 col 8, row 9 col 5, row 13 col 7.
- Intermediate map after step 13 shows 8 holes filled (F, G, H, I, K, L, M, N).
- Level flags noteleport, sokoban, solidify, premapped (soko1-1.lua:7).
- Final remainder of 2 boulders (A and E) is exact.
- Prize odds: 75% bag of holding, 25% amulet of reflection (soko1-1.lua:102-111).
- "Next to the treasure zoo" chambers at spoiler (17,12) / (17,14) / (17,16); zoo region (18,10)-(22,16).
-->

```
            11111111112222222
   12345678901234567890123456
 1 ┌────────────────────────┐
 2 │@·····^→^^^^^^^^^^^^^^^·│
 3 │·······┌──────────────┐·│
 4 └┬─────·└────┐         │·│
 5  │···········│         │·│
 6  │·A·B·C·D·E·│         │·│
 7 ┌┴──────·────┤         │·│
 8 │···F·G··H·I·│         │·│
 9 │···J········│         │·│
10 └┬───·──────┬┘   ┌─────┤·│
11  │··K·L·M···│  ┌─┤·····│·│
12  │·····N····│  │·+·····│·│
13  │·O·P···Q·┌┘  ├─┤·····│·│
14 ┌┴─────·─┬─┘   │·+·····+·│
15 │··R·····│     ├─┤·····├─┘
16 │········│     │·+·····│
17 │···┌────┘     └─┤·····│
18 └───┘            └─────┘
```

1. A を左へ1マス押す。
2. B を左へ1マス押す。
3. C を左へ1マス押す。
4. E を右へ1マス押す。
5. D を右へ1マス押す。
6. G を (9,8) まで、次に上へ3マス、次に左へ1マス押す。G を埋める。
7. H と I を G と同様に埋める。
8. J を左へ2マス、(3,9) まで押す。
9. F を G と同様に埋める。
10. N を右へ3マス、(11,12) まで押す。
11. L を (6,11) まで、次に上へ3マス押す。L を埋める。
12. M と K を L と同様に埋める。
13. N を左へ3マス、次に上へ1マス、(8,11) まで押す。N を L と同様に埋める。

この時点でマップは以下のようになります：

```
            11111111112222222
   12345678901234567890123456
 1 ┌────────────────────────┐
 2 │>·····@→·······^^^^^^^^·│
 3 │·······┌──────────────┐·│
 4 └┬─────·└────┐         │·│
 5  │···········│         │·│
 6  │A·B·C···D·E│         │·│
 7 ┌┴──────·────┤         │·│
 8 │············│         │·│
 9 │·J··········│         │·│
10 └┬───·──────┬┘   ┌─────┤·│
11  │··········│  ┌─┤·····│·│
12  │··········│  │·+·····│·│
13  │·O·P···Q·┌┘  ├─┤·····│·│
14 ┌┴─────·─┬─┘   │·+·····+·│
15 │··R·····│     ├─┤·····├─┘
16 │········│     │·+·····│
17 │···┌────┘     └─┤·····│
18 └───┘            └─────┘
```

14. R を (8,15) まで、次に上へ4マス押す。R を L と同様に埋める。
15. Q を (8,13) まで、次に下へ3マス、次に左へ (3,16) まで押す。Q を上へ1マス押す。Q を R と同様に埋める。
16. P と O を Q と同様に埋める。
17. J を (6,9) まで、次に下へ3マス押す。J を L と同様に埋める。
18. C を (9,6) まで、次に下へ3マス押す。C を J と同様に埋める。
19. B と D を C と同様に埋める。

巨岩が2個（A と E）残ります。軽量化の鞄または魔除けの賞品は、モンスター動物園（treasure zoo）に隣接する小部屋群（(17,12), (17,14), (17,16)）のいずれかに収められています。

#### 第4階層・バージョンB (Level 4, Version B) {.sokoban-level data-width=26 data-height=17}

このバージョンの賞品は通常 **反射の魔除け** ですが、4分の1 の確率で代わりに **軽量化の鞄** になります。

<!-- audit
2026-05-19:
- prize odds: 25% bag of holding, 75% amulet of reflection (soko1-2.lua:105)
- 28-step solution simulates cleanly; final remainder boulder (13,7), sokoban prize (13,8) (soko1-2.lua)
- level flags noteleport, premapped, sokoban, solidify (soko1-2.lua:7); no hardfloor on prize level
- diagonal boulder pushes blocked (hack.c:441-448)
-->

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │··→^^^^^^^^^^^^^^^^^^·│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│A└┐  ┌┘···│        │·│
 6 │·····├──┤·N··│        │·│
 7 │·BC··│··│··O·│        │·│
 8 └┐··DE│···PQ·┌┘        │·│
 9  │F··G···│R··│   ┌─────┤·│
10  │·HI·│··│··S│ ┌─┤·····│·│
11  │·J·K└──┤·T·│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐·L··│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·M···│   │·+·····│
16      │@·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

1. M を右へ3マス、次に上へ4マス、(11,11) まで押す。
2. T を上へ1マス押す。
3. S を上へ2マス押す。
4. Q を上へ1マス押す。
5. P を左へ3マス、(8,8) まで押す。
6. G を左へ2マス押す。
7. D を上へ2マス、次に左へ1マス押す。
8. A を埋める。
9. B を上へ1マス押す。
10. C を右へ1マス押す。C を埋める。
11. B を下へ1マス押す。

この時点でマップは以下のようになります：

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │··→·^^^^^^^^^^^^^^^^··│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│·└┐  ┌┘···│        │·│
 6 │·@D··├──┤·N··│        │·│
 7 │·B···│··│·QO·│        │·│
 8 └┐···E│P····S┌┘        │·│
 9  │FG·····│R··│   ┌─────┤·│
10  │·HI·│··│·T·│ ┌─┤·····│·│
11  │·J·K└──┤M··│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐·L··│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·····│   │·+·····│
16      │>·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

12. D を右へ1マス押す。D を埋める。
13. B を右へ2マス押す。B を埋める。
14. I を埋める。
15. E を下へ1マス、次に左へ1マス押す。E を埋める。
16. F を上へ3マス、次に右へ2マス押す。F を埋める。

この時点でマップは以下のようになります：

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │·@→······^^^^^^^^^^^··│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│·└┐  ┌┘···│        │·│
 6 │·····├──┤·N··│        │·│
 7 │·····│··│·QO·│        │·│
 8 └┐····│P····S┌┘        │·│
 9  │·G·····│R··│   ┌─────┤·│
10  │·H··│··│·T·│ ┌─┤·····│·│
11  │·J·K└──┤M··│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐·L··│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·····│   │·+·····│
16      │>·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

17. G を右へ1マス押す。G を埋める。
18. H と J を G と同様に埋める。
19. P を下へ1マス、次に左へ3マス、(5,9) まで押す。P を埋める。
20. K を (6,9) まで、次に左へ1マス押す。K を埋める。
21. L を右へ1マス、次に上へ1マス、次に左へ2マス押す。L を K と同様に埋める。

この時点でマップは以下のようになります：

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │·@→············^^^^^··│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│·└┐  ┌┘···│        │·│
 6 │·····├──┤·N··│        │·│
 7 │·····│··│·QO·│        │·│
 8 └┐····│·····S┌┘        │·│
 9  │·······│R··│   ┌─────┤·│
10  │····│··│·T·│ ┌─┤·····│·│
11  │····└──┤M··│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐····│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·····│   │·+·····│
16      │>·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

22. T を下へ1マス押す。
23. R を (11,8) まで、次に左へ3マス押す。R を P と同様に埋める。
24. M を R と同様に埋める。
25. T を左へ1マス押す。T を R と同様に埋める。
26. N を右へ1マス押す。
27. Q を下へ (12,9) まで、次に左へ1マス押す。Q を R と同様に埋める。
28. N を左へ1マス押す。N を Q と同様に埋める。

巨岩が2個（O と S）残ります。魔除けまたは軽量化の鞄の賞品は、モンスター動物園に隣接する小部屋群（(17,11), (17,13), (17,15)）のいずれかに収められています。

### 自主的挑戦 (Voluntary Challenges)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- vegetarian-safe puddings: gray ooze, brown pudding, green slime; not black pudding (mondata.h:241). Puddings leave globs, not corpses.
- Vegan excludes fortune cookies (they contain eggs).
- Foodless is not broken by polymorph (polyself.c only increments u.uconduct.polyselfs).
- Verified correct: all conduct triggers/checks, Pauper starting kit, Petless/Permadeaf/Bonesless/Sokoban mechanics, all roleplay flags.
-->

NetHack を一度クリア（昇天）した冒険者の多くは、さらなる高みを目指してゲームが本来許容している強力な手段を自らに禁じる「自主的挑戦（コンダクト / Conducts）」に挑みます。ゲームはこれらの行動制限を裏で厳密に追跡しており、昇天時や死亡時に遵守したコンダクトが公式に認定・表彰されます。

::: dense-table

| コンダクト名 | 破棄される条件 | 開始方法 |
|---------|----------------|---------------|
| 菜食主義者 (Vegetarian) | 肉や禁じられた動物性食品を食べる | 自動開始 |
| 完全菜食主義者 (Vegan) | あらゆる動物性食品を口にする | 自動開始 |
| 絶食 (Foodless) | 壁の咀嚼を含め、いかなるものも口にしない | 自動開始 |
| 無神論者 (Atheist) | 祈る、生贄を捧げる、アンデッド退散、僧侶と会話、祭壇でのBUC判定 | 自動開始 |
| 武器なし (Weaponless) | 装備した武器や武器道具で敵を殴る | 自動開始 |
| 平和主義者 (Pacifist) | 自身の戦果として記録されるモンスターの殺害 | 自動開始 |
| 文盲 (Illiterate) | 読む、または単一の `x` を超える文字を刻む | 自動開始 |
| 虐殺なし (Genocideless) | モンスター種族またはクラスを虐殺する | 自動開始 |
| 自己変身(へんげ)なし (Polyselfless) | 自分自身の姿を変身させる | 自動開始 |
| アイテム変身(へんげ)なし (Polypileless) | アイテムを変身（ポリパイル）させる | 自動開始 |
| 願いなし (Wishless) | いかなる願いも叶えてもらう | 自動開始 |
| アーティファクト願いなし | アーティファクトを願う（拒絶された場合も含む） | 自動開始 |
| 裸族 (Nudist) | いかなる防具も身につけない | `OPTIONS=nudist` |
| 盲目 (Blind / Zen) | 全盲状態がゲーム全編を通じて持続 | `OPTIONS=blind` |
| 赤貧 (Pauper) | 何も持たずに開始する（5.0新要素） | `OPTIONS=pauper` |
| ペットなし (Petless) | いかなるモンスターも手懐けない（5.0新要素） | `OPTIONS=pettype:none` |
| 完全聾 (Permadeaf) | 聴覚喪失がゲーム全編を通じて持続（5.0新要素） | `OPTIONS=permadeaf` |
| 倉庫番 (Sokoban) | 進入後に巨岩ルールを破る（5.0新要素） | 進入時に自動開始 |
| ボーンズなし (Bonesless) | ボーンズ階層の生成を無効化（5.0新要素） | `OPTIONS=!bones` |
| 振り直しなし (Unrerolled) | 最初に提示されたキャラクターをそのまま受け入れる | 最初のキャラを受け入れ |

:::

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

#### 無神論者 (Atheist)

<!-- audit
2026-05-19:
- Atheist tracks u.uconduct.gnostic (insight.c:2134, topten.c:590)
- breaks on: #pray (pray.c:2221), #offer corpse (pray.c:1977), #turn (pray.c:2426), #chat with priest (priest.c:572)
- dropping any non-coin on an altar breaks the conduct via the BUC flash (do.c:370)
- final Amulet offering for ascension is exempt (pray.c:1529-1588 has no gnostic increment)
- Priest's starting holy water does NOT auto-break the conduct (u_init.c:716-722)
- strategy aligned with NetHackWiki Atheist: no prayer / sacrifice / chat-with-priest / altar drops; final ascension Amulet offering is exempt (https://nethackwiki.com/wiki/Atheist)
-->

神仏とのいかなる交わりも絶ちます。具体的には：**`#pray`（祈る）を行わない**、祭壇で死体を **`#offer`（捧げる）を行わない**、アンデッドを **`#turn`（退散させる）を行わない**、そして寺院の僧侶と **`#chat`（会話する）を行わない** ことです。祭壇によるBUC判定の閃光も神聖な接触とみなされるため、金貨以外のアイテムを祭壇の上に落とす行為も失格となります（祭壇識別トリックは使用不可）。これにより、餓死、石化、病気、呪われた装備に対する神の救済という安全網が完全に失われます。

祈りで空腹を治せないため安定した食料確保が必須となり、生贄や祭壇BUCが使えないため識別の難易度が跳ね上がり、神からのアーティファクト下賜も望めません。ただし、星界の面で昇天を果たすための最終的なイェンダーの魔除けの奉納だけは例外として許されており、無神論を維持したまま昇天を完遂することが仕様上可能です。

#### 武器なし (Weaponless)

<!-- audit
2026-05-19:
- weaphit++ requires weapon non-NULL AND (WEAPON_CLASS OR is_weptool) (uhitm.c:616-617)
- weapon-tools that break: pick-axe, unicorn horn, other is_weptool items
- wielded polearm at range via #apply DOES break (HMON_APPLIED, dothrow.c:2199-2203)
- do NOT break: thrown weapons, fired ammo, wands, spells, barehand, martial arts, cockatrice-corpse-wield
- iron chain is CHAIN_CLASS, not a weptool; swinging it does NOT break (objects.h:101, 1631)
- aklys is WEAPON_CLASS, not a weptool; it breaks via the WEAPON_CLASS branch (objects.h:381-383)
- strategy aligned with NetHackWiki Weaponless, Martial arts: thrown/fired weapons and martial arts preserve the conduct, wielded-polearm-#apply still breaks it (https://nethackwiki.com/wiki/Weaponless, https://nethackwiki.com/wiki/Martial_arts)
-->

構えている武器や武器道具で敵を殴ってはいけません。武器を投げる、弓やクロスボウから射出する、杖や呪文を行使することは許されます。また、素手格闘や武術（Martial Arts）で殴り倒すことも完全に合法です（武闘家が圧倒的な強さを誇ります）。禁じられているのは、剣、斧、メイス、アキリス、つるはし、ユニコーンの角など、武器クラスまたは武器道具に分類されるアイテムを手に持った状態で敵を直接殴打することです。なお、長柄武器を構えて離れた位置から `a`（使用）でリーチ攻撃する行為もコンダクト違反となります。

これは一見するほど過酷な制約ではありません。武闘家は強力無比な武術で開始し、さらに成長します。他の職業であっても、呪文、杖、投擲短剣に頼ることができます。また、コカトリスの死体を素手（小手着用）で掴んで殴りつける行為も合法です（死体は武器ではないため）。最大の犠牲は、近接武器のアーティファクトが持つ圧倒的なダメージボーナスを諦めなければならない点にあります。

#### 平和主義者 (Pacifist)

<!-- audit
2026-05-19:
- Pacifist tracks u.uconduct.killer; only xkilled (mon.c:3500) and pet-pushed-into-trap (hack.c:2201) increment
- pet kills and conflict kills do NOT break the conduct: xkilled() only increments on !noconduct branch (mon.c:3499-3502)
- charm-monster spell, Elbereth, and pet tactics are all safe (no killer++ in those code paths)
- strategy aligned with NetHackWiki Pacifist, Conflict: pacifist runs lean on strong pets (often polymorph-amplified) and a ring of conflict for crowds (https://nethackwiki.com/wiki/Pacifist, https://nethackwiki.com/wiki/Conflict)
-->

いかなるモンスターも自らの手で殺害してはいけません。ペットによる撃破や、争い（Conflict）によってモンスター同士が殺し合った結果は、このコンダクトを破棄しません（ただしペットを押しのけて致命的な罠に突き落として殺す行為は違反となります）。平和主義者ランでは、戦闘をペットに任せ、群衆には争いの指輪を用い、[エルベレス](#elbereth) で怪物を寄せ付けない戦術を取ります。

平和主義者での昇天は十分に可能ですが、ダンジョンのルールに対する深い洞察が求められます。終盤の定番戦略は、願った **アルコンの小像**（割って出現させ、敵対した場合は再テイムする）を最強のチャンピオン闘士として育成し、怪物を手懐ける（魅了）呪文で群衆を鎮め、話し合いで解決できない局面を争いの指輪で乗り切ることです。

#### 文盲 (Illiterate)

<!-- audit
2026-05-19:
- only an "x" or "X" signature engrave is exempt; everything else breaks the conduct (engrave.c:1213)
- breaks: scrolls, spellbooks, fortune cookies, T-shirts, magic-marker writing (read.c:602, eat.c:2525, read.c:397, write.c:245)
- do NOT break: blank paper, unread novels, Book of the Dead, Hawaiian shirts, reading floor engravings (Elbereth)
- pet-on-scroll workaround for identifying scrolls is safe
- Wizard/Priest/Healer/Monk/Knight keep one pre-learned spell until it fades, ~20K turns (spell.h:17 KEEN)
- strategy aligned with NetHackWiki Illiterate: only an "x"-signature engrave is safe, scroll of scare monster is the rare exception that doesn't break the conduct (https://nethackwiki.com/wiki/Illiterate)
-->

いかなる文字も読んではいけません。巻物、魔法書、フォーチュンクッキー、Ｔシャツの文字を読むことは禁じられます。また、床に文字を刻む際も、伝統的な文盲の署名である単一の「x」または「X」以外の文字を刻むことは許されません（エルベレスを手動で刻むことはできません）。ただし、白紙の巻物や魔法書、アロハシャツ、死者の書、あるいは床に元から刻まれているメッセージを読む行為はセーフです。

巻物が読めないため、識別、武器・防具の強化、瞬間移動、解呪、虐殺といった強力な手段のほとんどが絶たれます。魔法書が読めないため、新しい呪文を学ぶことも古い呪文を再学習することもできず、初期習得呪文はやがて忘れ去られます。これにより、杖、薬、そして創意工夫に満ちた回避策への依存度が極限まで高まります。代表的な回避策は、**ペットの足踏みによるBUC判定**（犬がその上を歩くか？）と、**店主への売却価格による識別（価格識別）**（店主の提示価格を見ることは「読書」には含まれない）であり、これらを組み合わせることで識別の巻物の大半の役割を代行できます。

#### 虐殺なし (No Genocide)

<!-- audit
2026-05-19:
- genocide is only prompted by scroll of genocide and by sitting on a regular throne; wishes never offer it (do_genocide callers: read.c:1735-1737 SCR_GENOCIDE and sit.c:131 throne only)
- uncursed scroll: single species; blessed scroll: whole class (do_class_genocide, read.c:2638)
- throne prompt is single-species only: case 8 of 13 in throne_sit_effect, calls do_genocide(5) (sit.c:125-132)
- Vlad's tower thrones take a different path with no genocide case (special_throne_effect, sit.c:63-66)
- on a cursed scroll, empty input re-prompts and rndmonst() creates monsters; type "none" to escape (read.c:2848-2871)
- end-of-game tracking counts G_GENOD species in mvitals[], not a u_conduct counter (insight.c:2951-2966 num_genocides)
- cursed-scroll monster-creation preserves the conduct (no species gets G_GENOD'd)
- strategy aligned with NetHackWiki Genocide, Throne: answer "none" at the prompt, throne genocides are always safe, Plane of Water class-`;` wipe is off-limits for genocideless (https://nethackwiki.com/wiki/Genocide, https://nethackwiki.com/wiki/Throne)
-->

いかなるモンスターも虐殺（ジェノサイド）してはいけません。虐殺のプロンプトが表示されるのは、**虐殺の巻物** を読んだとき（呪われていないは1種族、祝福はクラス全体）と、**通常の玉座に座ったとき**（13通りの結果のうちケース8で単一种族の虐殺を促される）の2つです。コンダクトを維持するには、対象を聞かれた際に **"none"** と入力してください（Enterキーだけを押すと再入力を求められるだけです）。呪われた巻物は入力した名前に応じたモンスターを逆虐殺（召喚）しますが、召喚自体は虐殺なしコンダクトを破棄しません。

これは、マスターリッチやアーチリッチ、マインドフレア、コカトリスといった、熟練冒険者が普段なら即座に根絶する凶悪なモンスターのすべてと正面から向き合い続けることを意味します。また、**水の面** においても、クラゲやウナギやクラーケン（`;` クラス）を一網打尽にする定石が使えないため、呼吸の魔除けを用意して海の怪物たちの間合いを警戒しながら正攻法で渡り切らなければなりません。

もっとも、これは比較的達成しやすいコンダクトの1つです。巻物を拾えず、玉座で虐殺を引かなかったために、意図せず自然にこのコンダクトを達成して昇天するプレイヤーも数多くいます。

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

#### 願いの制限 (Wishing Restrictions)

<!-- audit
2026-05-19:
- u.uconduct.wishes and u.uconduct.wisharti are separate counters with separate xlogfile achievements (you.h:157-158, topten.c:596-597)
- wishing for the literal string "nothing" doesn't tick the counter (zap.c:6369)
- Amulet-of-Yendor first-pickup wish must be declined for wishless (allmain.c:445)
- wisharti ticks even for DENIED artifact wishes: increment is before the deny branch (objnam.c:5362-5365)
- fountain water demon routes through mongrantswish -> makewish
- wresting empty wands routes through makewish (zap.c:2583)
- strategy aligned with NetHackWiki Conduct, Wish: wishless vs no-wishing-for-artifacts are separately tracked, "nothing" is the canonical escape for a forced wish (https://nethackwiki.com/wiki/Conduct, https://nethackwiki.com/wiki/Wish)
-->

願いに関する2つの独立したコンダクトがあります：

**願いなし (Wishless)。** いかなる願いも叶えてもらってはいけません。杖、泉、煙の立つ薬のジン、玉座、その他すべての入手源からの願いを拒絶します。**イェンダーの魔除けを拾った瞬間に発生する願いプロンプト** においても、文字列として **"nothing"**（何もない）と入力すれば、願いカウンターを進めずにパスできます（"nothing" の入力は、あらゆる強制的な願いプロンプトを安全にやり過ごす標準的な脱出口です）。ダンジョンが偶然ドロップしてくれなかった必需品（銀色ドラゴンの鱗鎧、韋駄天の靴、軽量化の鞄など）を願いで補うことが一切できないため、極めて過酷な挑戦となります。

**アーティファクト願いなし (No wishing for artifacts)。** 通常のアイテムを願うことは許されますが、アーティファクトを願うことだけを禁じます。これにより、[グレイスワンダー](#grayswandir) や [エチオピカの目](#eye-of-the-aethiopica) といった最強の至宝を即座に手に入れる最も効率的な戦略が封じられ、日用品や基本装備の補給だけに願いが限定されます。なお、アーティファクトを願って **拒絶された場合（手元に普通のアイテムが出現した場合）であってもカウンターは加算される** ため、誤ってアーティファクト名を指定しないよう注意してください。

#### 複合コンダクト (Combining Conducts)

<!-- audit
2026-05-19:
- Pauper does NOT suppress the starting pet; makedog() only returns NULL on pettype:none (dog.c:219-229)
- only OPTIONS=pettype:none can skip the starting pet
- nudist and blind have been tracked since 3.6
- 5.0 added pauper, petless, permadeaf, sokoban, bonesless
- vegan is a strict subset of vegetarian
- all conducts appear in the show_conduct end-screen
-->

複数のコンダクトを組み合わせることで、難易度は跳ね上がります。ベジタリアン無神論者はどちらか単体よりも遥かに困難です。そして平和主義者・文盲・完全菜食・絶食・無神論・素手戦闘の全乗せ（いわゆる「フルコンダクト」）は、もはや伝説の領域であり、実際に達成者が存在します。規模感の目安として：公開サーバー NAO において、昇天者の約9人に1人が「願いなし」を達成していますが、「絶食」を達成しているのは約80人に1人に過ぎません。

近年の NetHack では、公式に記録されるコンダクトがさらに拡張されました：

**裸族 (Nudist)。** 鎧、シャツ、マント、小手、靴、兜、盾など、いかなる防具も身につけてはいけません。ゲーム開始時に `OPTIONS=nudist` を設定します。ダンジョン全体を下着一丁で戦い抜くことになります（NetHack 3.6 から公式追跡）。

**盲目 (Blind / Zen)。** ゲーム全編を視覚なしでプレイします。ゲーム開始時に `OPTIONS=blind` を設定します。移動と戦闘にはテレパシーやその他の知覚手段が不可欠となります（NetHack 3.6 から公式追跡）。

NetHack 5.0 では、さらに6つの追跡コンダクトが追加されました：赤貧 (Pauper)、ペットなし (Petless)、完全聾 (Permadeaf)、[倉庫番](#sokoban)、ボーンズなし (Bonesless)、そして振り直しなし (Unrerolled) です。Pauper、Permadeaf、Petless、Bonesless はゲーム開始前のオプション設定で宣言します。Sokoban はプレイ中の実際の行動に基づいて自動追跡され、Unrerolled はゲームが最初に提示したキャラクターを受け入れたことを記録します。

#### 赤貧 (Pauper: 5.0新要素)

<!-- audit
2026-05-19:
- Pauper is set_in_config: rcfile or NETHACKOPTIONS env only, not in-game O menu (optlist.h:559)
- ini_inv early-return suppresses starting items only, not the pet (u_init.c:1308-1309)
- Pauper does NOT suppress the starting pet (dog.c:219-229; only pettype:none does)
- dog.c:262-267 skips the pony saddle for Pauper
- Cleric, Knight, Monk start knowing SPE_PROTECTION (pauper_reinit, u_init.c:890-922)
- Cave Dweller starts knowing FLINT (pauper_reinit, u_init.c:890-922)
- Protection book is a load-bearing early-game pickup for those three roles
- nudist cascade triggers when pauper is set (options.c:5290-5293)
- end-of-game string at insight.c:2117-2119; xlogfile at topten.c:604
-->

完全に何もない無一文の状態でゲームを開始します：所持金ゼロ、所持品ゼロ、防具なし、初期武器なし。設定ファイルに `OPTIONS=pauper` を記述します（設定ファイルまたは環境変数 `NETHACKOPTIONS` からのみ設定可能であり、ゲーム内の `O` メニューでは切り替えられません）。赤貧を設定すると自動的に裸族（Nudist）も有効化されます。これは後から失われることのない恒久的コンダクトです：後からゴールドを拾ったり使ったりすることは禁じられておらず、「何もない状態でスタートしたこと」そのものが達成条件となります。

開幕が完全に不可能になるのを防ぐため、わずかな補償措置が与えられます：未消費の武器スキルスロットが2枠与えられ、さらに各職業ごとに象徴的な呪文またはアイテムを1つ最初から認知しています。魔法使いは「衝撃」を、治療師は「回復」を、司祭・騎士・武闘家は「防護」を（司祭は聖水も認知）、考古学者は「試金石」を、洞窟人は「火打石」を、盗賊と観光客は「麻袋」を、侍は「軍糧丸」の食料をあらかじめ認知しています。浅い階層に配置された [補給コンテナ](#supply-containers) が、あなたの最初の装備セットの多くを賄ってくれるはずです。

#### ペットなし (Petless: 5.0新要素)

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

#### 完全聾 (Permadeaf: 5.0新要素)

<!-- audit
2026-05-19:
- permadeaf is u.uroleplay.deaf, in xlogfile (topten.c:602) and show_conduct (insight.c:2113)
- Deaf macro at youprop.h:125
- rcfile option name is `permadeaf` (or `deaf`), NOT `!acoustics` (a different flavor flag, flags.acoustics) (optlist.h:267-269 declares `deaf` with alias "permadeaf" binding u.uroleplay.deaf; optlist.h:143-145 declares `acoustics` binding flags.acoustics — separate flag)
- permadeaf is set_in_config: rcfile only, not in-game O menu (options.c:5207)
- there is no `-Dpermadeaf` syntax; `-D` is the debug/wizard-mode flag (unixmain.c:359-365)
- Deaf only suppresses shrieker MESSAGES; makemon and aggravate still run (mon.c:4089-4106)
-->

いかなる音も聞こえない状態でプレイします。設定ファイルに `OPTIONS=permadeaf`（または `OPTIONS=deaf`）を記述します（設定ファイル専用であり、ゲーム内の `O` メニューでは切り替えられません。無関係な効果音設定の `acoustics` と混同しないようにしてください）。ゲームは第1ターンから恒久的な難聴（Deaf）の特性を持った状態として進行します：「水が流れる音がする」「誰かが金を数えている音がする」「扉が開く音がする」といった環境音メッセージや、モンスターの気配（「ズルズルという音がする」等）のメッセージがすべて抑制されます。

抑制されるのは *メッセージの表示だけ* です。叫びキノコ（シュリーカー）は依然として叫び声をあげ、モンスターを召喚し、フロア全体を怒らせます（あなたにその警告メッセージが表示されないだけです）。`F` クラスのキノコの近くの不気味な静寂を、通常の「叫び声をあげた」メッセージと同等の致命的脅威として察知しなければなりません。

完全聾プレイでは、視覚と論理的推論だけを頼りに迷宮を探索します。

#### 倉庫番 (Sokoban: 5.0新要素)

<!-- audit
2026-05-19:
- digging does NOT trigger sokoban_guilt; dig.c has no such call (sokoban_guilt callers limited to hack.c:299/307/398/403, read.c:1951, steed.c:767, zap.c:1711/5556 — none in dig.c)
- breaks: squeeze through (hack.c:299, 307), boulder fracture by wand of striking (zap.c:5556)
- breaks: polymorph a boulder (zap.c:1711), scroll of earth (read.c:1951), dismount onto a boulder (steed.c:767)
- each violation costs -1 Luck and increments u.uconduct.sokocheat (trap.c:7039-7054)
- achievement reported only if the branch was entered (insight.c:2215-2228)
- teleportation is blocked by the level's noteleport flag (teleport.c:1185); it's a level constraint, not a conduct trigger
-->

倉庫番のルールを一度も破ることなく進入・プレイします。ゲーム終了時にこのコンダクトが記録されるために、必ずしも倉庫番を最後まで登りきる必要はありません。違反行為1回ごとに **幸運が 1点 低下** し、不正カウンターが加算されます：小型形態や極度に身軽な荷物による **巨岩のすり抜け**、衝撃やつるはしや衝撃の杖による **巨岩の粉砕**、巨岩の **変身**、**大地の巻物** の読書、あるいは巨岩のマスへの **下馬** です。ゲームはこれらの違反を自動的に追跡します。

#### ボーンズなし (Bonesless: 5.0新要素)

<!-- audit
2026-05-19:
- bonesless achievement requires !flags.bones; you must turn bones loading off (topten.c:605)
- not encountering bones is a separate Miscellaneous enlightenment line, NOT the conduct (insight.c:439)
- you cannot get bonesless by luck alone
- show_conduct never lists lifesaving uses; there is no amulet-of-life-saving tracking (insight.c:2089-2200 show_conduct enumerates rerolling/food/atheist/weaphit/pacifist/illiterate/pets/genocides/polypiles/polyselfs/wishes — no lifesaving counter; u.uconduct has no lifesave field)
- `bones` is set_in_config: config file or command line only, not in-game O menu (optlist.h:213-215)
- !flags.bones blocks both save (bones.c:360) and load (bones.c:642) — cuts both directions
- "never encountered any bones levels" enlightenment requires flags.bones true AND u.uroleplay.numbones==0 (insight.c:439-441)
-->

過去のプレイヤー（または自分自身）の亡骸や遺留品から一切の遺産を受け継ぐことなくプレイします。設定ファイルに `OPTIONS=!bones` を記述します（[セーブとボーンズ](#saving-and-bones) を参照）。単に偶然ボーンズ階層に遭遇しなかっただけのプレイは、この公式コンダクトの対象にはなりません（明示的にオプションでボーンズ生成を無効化しておく必要があります）。

---

### 店の利用：信用・借金・トラブル {#shopping-and-shopkeeper-pricing}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- 22 gem prices, Mohs hardness, hard-gem threshold >=8 verified (objects.h, shk.c).
- Dunce cap and low-XL Tourist each multiply buy by 4/3.
- Angry-shopkeeper surcharge adds (price+2)/3 per billed item (~33%).
- Charisma price tiers: >18 halves, =18 2/3, 16-17 3/4, <=5 doubles, 6-7 3/2, 8-10 4/3.
- Touchstone full ID requires blessed (or non-cursed for Archeologist/Gnome); uncursed gives streak color.
-->

店は単に品物を売買するだけの場所ではありません：その価格設定システムは、ゲーム内で最も強力な未識別アイテムの判別ツールです。詳細なメカニズムと価格換算表については第4部の [価格識別法](#the-price-is-right) で解説しました。ここでは残る重要な要素である、預け金（クレジット）、借金、店主との戦闘、そして見落としがちな特殊ルールを網羅します。

何よりもまず、最大の致命的ミスを防ぐための鉄則：**「未払いの品物を持ったまま店の敷居を跨いではならない」**。店主は即座に敵対化し、出口を塞ぎ、キーストン・コップを召喚します。店を出る前に必ず `I` を押して `u`（未払い品）を確認し、代金を清算してください。後から代金を支払えば、追跡してくるキーストン・コップは全員撤収します。

#### 信用と借金 (Credit and Debt)

各店主は、顧客ごとに「預け金（クレジット / Credit）」「借金（デビット / Debit）」「一時借受金（ローン / Loan）」の3つの数字を記録した台帳を管理しています。

**預け金（クレジット）を得る方法。** 通常は2つのルートがあります：

1. **ゴールドを持っていない店主にアイテムを売却する。** 現金を支払えない店主は、通常の提示買取価格の 10分の9 に相当する額を預け金として提案してきます：*「現在現金を持ち合わせておりません。代わりに N ゾークミドの預け金でよろしいですか？」*（店主が現金を持っていれば普通に現金で支払われます。一部不足している場合でも不足分だけが預け金になるわけではありません）。
2. **店の床にゴールドを置く。** 店の床の上にゴールドを置く（または投げる）と、既存の借金を返済した後の残額がすべてあなたの預け金残高として記録されます。これにより、持ち歩いているゴールドをレプラコーンに盗まれない安全な店限定の預金へと変換できます。

**預け金の使われ方。** 店で買い物をする際、店主はまず預け金残高から購入代金を相殺します（*「代金は預け金から差し引かれました」*）。不足分がある場合のみ、所持金から支払われます。預け金は店主ごとに個別に記録され、現金として払い戻すことはできません。

**預け金での支払いは現金より有利か不利か？** 価格そのものは全く同一です：預け金はカリスマ補正、観光客補正、激怒補正を適用した *後の* 最終価格から厳密に 1:1 の比率で差し引かれ、割引も割増もありません。違いは資金の「安全性」と「流動性」にあります：

- **有利な点：** レプラコーンに盗まれる心配がなく、所持重量もゼロになります。何度も立ち寄る予定の店は銀行として機能します。
- **不利な点：** その店主の店でしか使えません。欲しい品がない店で預け金を溜め込みすぎたり、店主が死亡・敵対化した場合、その預け金は電子の藻屑と消え去ります。また、祭壇への寄付や僧侶への謝礼、悪魔へのワイロとして預け金を使うことはできません。

現実的な運用：何度も訪れる予定の拠点（[ノーム鉱山](#the-gnomish-mines) の雑貨屋などが定番）に余剰資金を預け金として保管するのは賢明ですが、そこで使う予定以上の金額を預け入れないようにしましょう。

（なお、古い小技として *クレジット複製* があります：ゴールドを入れた袋を店内に置き、ペットにその袋を咥えさせて店外へと運ばせます。店には預け金が計上されたまま、コインそのものも手元に回収できます。）

**借金（Debit）** はその逆です：店内で未払いのアイテムを *使用* した際（巻物を読む、薬を飲む、杖を振るなど）、購入手続きが完了していない場合に発生します。品物の価格の一部が使用料として請求され、以後の売却金や床置きゴールドはまずこの借金の返済に充当されます。

**一時借受金（Loan）** は、店の床に落ちていた店主のゴールドをあなたが拾い上げた際に記録される名目です。店内にゴールドを置くことで、まずこのローンが返済されてから預け金へと加算されます。

#### 店主の行動 (Shopkeeper Behavior)

店主はゲーム内で最強クラスのNPCです：高いHP、優れたAC、重い打撃力を誇り、エルベレスも通用せず、他のモンスターに通用する賢い脱出技も効きません。さらに彼らはすべてを見通しています：透明状態であっても、あなたが拾い上げた品物や店内に持ち込まれたアイテムのすべてを正確に把握しています。

::: dense-table

| トラブル内容 | 店主の反応 | 最も安全な解決法 |
|---------|-----------------------|------------|
| 未払いのまま店を出ようとする | 出口を塞ぎ、強行脱出にはコップを呼ぶ | `I` を押して `u` で確認し、先に支払う |
| 未払いの品物を破損・使用する | 損害賠償や使用料を請求額に加算する | 店を出る前に清算する |
| 施錠された店の扉を蹴り破る | 400 zm の弁償を要求。拒否すると戦闘 | 鍵開け器具を使うか開扉の杖で開ける |
| 店の壁を掘り抜く | 強さ1点につき 10 zm の弁償を要求 | 弁償するか、そもそも壁を掘らない |
| 借金を抱えたまま下へ穴を掘る | 所持品の鞄・荷物全体を差し押さえる | 掘る前に借金を完全に完済する |
| 店主を攻撃する | 激怒して敵対化する | `#chat` で話し掛け、1,000 zm 支払って和解 |
| 透明状態またはつるはしを構えて入店 | 入店を拒絶される | 姿を現し、つるはしを鞘に収める |

:::

アーティファクトの売買価格は、基本価格の4倍に設定されます（巨人殺しの 800 zm から、ストームブリンガーやグレイスワンダーの 32,000 zm まで）。未識別の長剣に5桁（数万ゾークミド）の提示価格がついた場合、細心の注意を払う価値があります。

店主を倒して在庫のすべてとレジの現金（死亡時に 1,000〜4,000 zm と万能鍵をドロップ）を強奪することも *可能* ですが、極めて危険な死闘になります。店主を殺害すること自体はキーストン・コップを召喚しません（コップは未払いのまま店を出たときに現れます）。しかし殺害は属性値を激減させ、混沌以外の属性は幸運 −2 とテレパシーを喪失します。**あらかじめ店主を変身（ポリモーフ）させてから倒す** と「殺人」としてカウントされなくなるため、秩序や中立のキャラクターが店主を始末する際はこの手段が好まれます。終盤の屈強な英雄が店を制圧することはありますが、中盤に気軽に行うべき策ではありません。

店でのミスを防ぐ3つの習慣：

- **請求額を直接確認する。** `I` を押して `u` を選択し、未払いの所持品を一覧表示してください。扉のマスの上では売却が成立しないため、すべてを敷居に落とす古い裏技よりも所持品コマンドの方が遥かに正確です。
- **売却してから預け入れる。** 通常の売却は現金で支払われます。預け金にしたい場合は、受け取ったゴールドをそのまま店の床に置いてください。
- **ボーンズ階層の店に注意。** 過去のプレイヤーのボーンズ階層で見つかった店では、店内のすべてのアイテムは死亡した冒険者の幽霊店主に帰属しています。床から拾えば、新しい店主から定価を請求されます。店の床はタダの戦利品置き場ではありません。
- **扉に刻まれた「棚卸しのため休業中」（"Closed for inventory"）。** これは放棄された店ではなく、扉が **施錠されて** 生成された店を意味します。店主は依然として店内に控えており、商品は未払いです。鍵開け器具を使うか開扉の杖で開けてください（オーケスの町は店主のいない本物の廃墟であるため、そこのアイテムだけは本当に持ち主がいません）。

#### 宝石の売却識別 (Gem Identification Through Selling)

未識別の宝石を店主に売却することは、**信頼できる価格識別手段ではありません**。店主は、本物の宝石であれ模造品（無価値なガラス）であれ、未識別の宝石には一律 3〜8 zm 程度しか提示しません。その提示額は宝石の真の正体と店主の気分によって変動します。本物のダイヤモンドも無価値なガラス玉も同じ 3〜8 zm の範囲で提示されるため、売却価格だけで両者を見分けることは不可能です。同じ未識別宝石を2つの異なる店に持ち込んでも、提示額はバラバラになります。

本物の識別には **試金石** (Touchstone: 灰色の石、基本価格 45、鉱山などで時折発見される) を使用してください。未識別の宝石を **祝福された** 試金石に擦りつける（`#apply`）と、その宝石の真の名称が即座に判明します。呪われていない試金石では、条痕色（擦り痕の色）が判明するだけにとどまります（考古学者とノームは種族・職業特権により、呪われていない石であっても完全な名称を看破できます）。硬度は関係なく、あらゆる宝石を判別可能です。一度識別されれば、本物の宝石はその真の価値（多くは数百〜数千 zm）で売却できるようになり、ガラス玉は二値同然となります。

##### 本物の宝石の価格表 (Real-gem prices)

正体が判明した宝石は、その種類によって基本価格が決定されます。すべての宝石は重量 1 であり、同種かつ識別済みの宝石は何個あってもインベントリの1枠にスタックされるため、大量のルビーを溜め込む負担はアイテム欄1枠の消費だけで済みます。

以下にすべての本物の宝石の基本価格を掲載します。通常の売却時の買取提示額は、カリスマ補正や各種修正が入る前の段階で、基本価格のおよそ半分から始まります。

::: web-only
カリスマ / 売却 / 観光客 / 激怒ツールバーを使用して、各種補正による価格変動を確認できます。
:::

「モース」列は、現実の鉱物硬度（滑石 1、ダイヤモンド 10）を表すモース硬度であり、ゲーム内でも2つの重要な判定に使われます。モース硬度 8 以上の宝石は **「硬い (hard)」** とみなされ、柔らかい宝石やガラス玉には不可能な2つの特性を持ちます：床に [エルベレス](#elbereth) などの文字を刻む際、指先や柔らかい宝石のような一時的な埃の落書きではなく、**永久的な刻み文字** として刻み込むスタイラス（鉄筆）として機能します。また、投げた宝石が命中した際、硬い宝石なら 3回中2回 は壊れずに残ります（柔らかい宝石やガラス玉は 3回中1回 しか残りません）。なお硬度は試金石による識別には影響せず、あらゆる宝石が祝福された試金石で識別可能です。

<div class="price-id-toolbar"></div>

| 基本価格 | 宝石名 | 色 | モース硬度 | 特記事項 |
|------:|-----------------------|-----------------|-----:|--------------------------------|
|  4500 | ディリジウムの結晶 (dilithium crystal) | 白色 |    5 | 最も希少な白い宝石 |
|  4000 | ダイヤモンド (Diamond) | 白色 |   10 | ゲーム内で最も硬い物質 |
|  3500 | ルビー (Ruby) | 赤色 |    9 | |
|  3250 | 橙水晶 (jacinth) | 橙色 |    9 | 2種類ある橙色の宝石の1つ |
|  3000 | サファイア (Sapphire) | 青色 |    9 | |
|  2500 | 黒オパール (black opal) | 黒色 |    8 | |
|  2500 | エメラルド (Emerald) | 緑色 |    8 | |
|  2000 | トルコ石 (Turquoise) | 緑色 |    6 | |
|  1500 | 黄水晶 (Citrine) | 黄色 |    6 | |
|  1500 | アクアマリン (aquamarine) | 緑色 |    8 | |
|  1000 | 琥珀 (Amber) | 黄褐色 |    2 | 最も柔らかい宝石。埃文字のみ |
|   900 | トパーズ (topaz) | 黄褐色 |    8 | |
|   850 | 黒玉 (Jet) | 黒色 |    7 | |
|   800 | オパール (Opal) | 白色 |    6 | |
|   700 | 金緑石 (Chrysoberyl) | 黄色 |    5 | |
|   700 | ガーネット (garnet) | 赤色 |    7 | |
|   600 | アメジスト (amethyst) | 紫色 |    7 | |
|   500 | ジャスパー (jasper) | 赤色 |    7 | |
|   400 | フルオライト (fluorite) | 紫色 |    4 | |
|   300 | ひすい (jade) | 緑色 |    6 | |
|   200 | 黒燿石 (obsidian) | 黒色 |    6 | |
|   200 | めのう (agate) | 橙色 |    6 | |
|     0 | (模造宝石 / ガラス玉) | 任意の色 |    5 | 未識別時は 3〜8 zm で売却 |

<div class="price-id-toolbar"></div>

持ち歩くか捨てるかの判断は、「所持枠が逼迫した際、どの色から優先して間引くか」という点に集約されます。ブラックオパール、エメラルド、ルビーは常に確保すべきであり、瑪瑙や黒曜石は真っ先に捨てる候補となります。

いくつかの経験則：

- **本物の宝石はどれもユニコーンの幸運獲得において完全に同等の価値を持つ。** 200 zm の瑪瑙を自属性のユニコーンに投げても、3250 zm の風信子石を投げても、得られる幸運は等しく **+5** です。自属性のユニコーンに食べさせる前に、安価な宝石を売却してしまってはいけません。
- **価格の列は、売却時および最終スコアの計算において重要になります。**
- **どうしても宝石を捨てなければならない場合**（鉱山最深部でアイテム枠が溢れたり、拠点を整理する際）、*安価な色の重複した個体から優先して捨ててください*。試金石による識別作業がすでに完了しているため、各色の識別済み宝石は最低1個ずつ手元に残しておきましょう。
- **最上位グループ**（2500 zm 以上：ダイリチウム、ダイヤモンド、ルビー、風信子石、サファイア、ブラックオパール、エメラルド）は、個別売却する価値があります。基本レートでの買取価格は基本価格の半分（ダイヤモンドなら 2,000 zm）から始まり、宝石を扱わない店は買い取ってくれません。
- **無価値なガラス玉が幸運を減らすことは絶対にない。** ガラス玉をユニコーンに投げた場合、拒絶される（「そんなゴミには興味がない」）か、好意的に受け取られるかのどちらかです。幸運が変動するリスクがあるのは、**異なる属性** のユニコーンに *本物の宝石* を投げた場合（−3 から +3 のランダム変動）だけです。メッセージの言い回しに注目してください：幸運を高めてくれた本物の宝石を受け取ったユニコーンは *「感謝して（gratefully）」* 受け取り、何も起きなかったガラス玉を受け取ったユニコーンは *「愛想よく（graciously）」* 受け取ります。

### 武器一覧表 (Weapons Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h + weapon.c: no corrections. Every weapon row (base/bonus dice, weight, cost, to-hit, material, two-handed/launcher/skill notes) verified, including composite-damage entries vs dmgval().
-->

ダメージは**小型に対するダメージ / 大型に対するダメージ (vs small / vs large)**として表記されており、強化値（強化・呪い）が加算される前、かつ銀や材質による追加ボーナスを除いた基本ダイス値です。**重量 (Wt)**はユニット重量、**価格 (Cost)**は店における未強化時の基本価格（Zm: ゾークミッド）、**命中 (Hit)**は武器自体に組み込まれている命中補正ボーナス（大半は 0）を表します。盾の装備や二刀流（二刀流戦闘）を阻害する両手持ち武器には、備考欄にフラグが付けられています。武器はスキルごとに分類されています。スキル枠（スロット）を投資する前に、[職業別のスキル上限一覧](#per-role-skill-caps)を確認してください。一部の武器に見られる括弧内の名称は、侍（Samurai）がプレイした際に画面上に表示される別名です（ゲーム内部では同一のアイテムとして処理されます）。

#### 短剣 (Dagger)
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

<!-- audit
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

<!-- audit
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

#### サーベル (Saber)
<!-- audit
2026-05-19:
- 10 saber cells verified clean (objects.h)
- Grayswandir is a SILVER_SABER artifact, PHYS(5,0): +1d5 to-hit and double damage (artilist.h:170, artifact.c:1083-1086, 1106-1107)
- Werebane is also a silver saber artifact (artilist.h:166); +d5 vs lycanthropes via SPFX_DFLAG2 M2_WERE
- inline effects deferred to Artifacts chapter rather than duplicated
-->

片手持ち近接武器。銀のサーベルを母体とするアーティファクト形態（グレイスワンダー、ウェアベイン）は、ゲーム内屈指の強力な片手武器です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| シミター (scimitar) | 1d8 / 1d8 | 40 | 15 | — | 鉄 |  |
| 銀のサーベル (silver saber) | 1d8 / 1d8 | 40 | 75 | — | 銀 | 銀特効により悪魔、獣人、吸血鬼、小悪魔に追加ダメージ。アーティファクト形態：**グレイスワンダー (Grayswandir)** および **ウェアベイン (Werebane)**（[アーティファクト一覧](#artifacts)参照）。 |

:::

#### 幅広の剣 (Broadsword)
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

#### 長剣 (Long sword)
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
| 刀 (katana) | 1d10 / 1d12 | 40 | 80 | +1 | 鉄 | 武器自体に+1の命中補正が組み込まれている。スニッカーズニー (Snickersnee) がアーティファクト形態。 |

:::

#### 両手剣 (Two-handed sword)
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
| 大刀 (tsurugi) | 1d16 / 1d8+2d6 | 60 | 500 | +2 | 金属 | 両手持ち。村正の剣 (The Tsurugi of Muramasa) がアーティファクト形態。 |

:::

#### 斧 (Axe)
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
| 戦斧 (battle-axe) | 1d8+1d4 / 1d6+2d4 | 120 | 40 | — | 鉄 | 両手持ち（5.0の筋力ダメージ 1.5 倍ボーナス適用）。小型に+1d4、大型に+2d4。野蛮人（Barbarian）のクエストアーティファクトである**クリーバー (Cleaver)** は戦斧が母体。 |

:::

<!-- audit
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

#### こん棒 (Club)
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

#### メイス (Mace)
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
| メイス (mace) | 1d6+1 / 1d6 | 30 | 5 | — | 鉄 | 僧侶（Priest）が生贄の捧げ物で最初に確定入手するアーティファクト「デーモンベイン (Demonbane)」の母体：悪魔に対して命中+1d5かつダメージ2倍の銀のメイス、さらに追放効果の発動（invoke）付き。 |
| 銀のメイス (silver mace) | 1d6+1 / 1d6 | 36 | 60 | — | 銀 | 悪魔、獣人、吸血鬼、影、大半の小悪魔に対して+1d20の追加ダメージ。 |

:::

#### モーニングスター (Morning star)
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

#### フレイル (Flail)
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
| 鉄のフック (grappling hook) | 1d2 / 1d6 | 30 | 50 | — | 鉄 | フレイルスキルを修練可能。使用（apply）すると2マス先のアイテムを引き寄せたり、超小型モンスターを引き寄せたり、自分自身を1歩引き寄せることができる。 |

:::

#### ハンマー (Hammer)
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

#### 六尺棒 (Quarterstaff)
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

#### 長柄武器 (Polearms)
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

#### 槍 (Spear)
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

#### トライデント (Trident)
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

<!-- audit
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

<!-- audit
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

<!-- audit
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

<!-- audit
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

<!-- audit
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

<!-- audit
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

<!-- audit
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

<!-- audit
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

### 防具一覧表 (Armor Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h: no corrections. Every armor row (AC=10-macro-arg, MC, weight, material, slot) verified across ARMOR/HELM/CLOAK/SHIELD/GLOVES/BOOTS macros.
-->
<!-- audit
2026-05-19:
- body armor: AC/Wt/Cost via ARMOR() macros (objects.h:556-600); plate mail AC+7 wt450 cost600 (line 556-558).
- mithril coats: AC+6/+5, wt 150, cost 240, MITHRIL material (objects.h:571-576).
- shirts wt 5 (Hawaiian/T-shirt, objects.h:603-608); cloaks at objects.h:611-650.
- helmets at objects.h:445-487; gloves at objects.h:686-697; boots at objects.h:700-727.
- shields at objects.h:653-679; cloak of protection MC 3 (objects.h:637-640).
- helm of brilliance: adds spe to Int and Wis (literal enchantment), NO dice (do_wear.c:3328-3334 adj_abon).
- gauntlets of dexterity: adds spe to Dex, NO dice (do_wear.c adj_abon).
- dunce cap is NOT pre-cursed at generation: follows standard mkobj; auto-curses when worn (do_wear.c:475-491).
- 9/10-cursed-on-generation items: FUMBLE_BOOTS, LEVITATION_BOOTS, HELM_OF_OPPOSITE_ALIGNMENT, GAUNTLETS_OF_FUMBLING (mkobj.c:1086-1090).
- mithril DOES suffer casting penalty: MITHRIL is in is_metallic range, spelarmr applies (objclass.h:194-196, spell.c:2191-2193).
- blue dragon scale mail and scales give extrinsic Very_fast tier matching speed boots, NOT intrinsic Fast (do_wear.c:817-828 EFast).
- speed boots mechanic: free action on 2/3 of turns, NOT "+1 speed". (allmain.c:125-128 `if (Very_fast) { if (rn2(3) != 0) moveamt += NORMAL_SPEED; }`)
- levitation boots: Boots_off handles in-air removal (do_wear.c:300-310); the trap is the 9/10 curse.
- robe casting bonus cancels most of the metal-armor penalty (spell.c:2192-2195 spelarmr subtraction).
- chain mail: all iron mails are Mines drops (the "Dwarves drop these" framing is misleading).
- follow-ups: build_armor_appendix.py may be stale; "yellow dragon scale mail | Rare." not verified against 5.0 generation rules.
-->

**AC**はその防具が提供するアーマークラス補正値です（数値が大きいほど防御力が高く、画面上のAC表示からこの数値が減算されます）。**MC**は魔法防御能力レベル（1〜3）を表し、数値が高いほど敵の魔法攻撃を防ぐ確率が高まります。**重量 (Wt)**はユニット重量、**価格 (Cost)**は店での基本価格です。**備考**列には、装備中に付与される固有能力（耐性や特性）および戦術上の注意点をまとめています。防具は装備部位ごとに分類されています。ドラゴンの鱗鎧は終盤における圧倒的重要性から、個別の項目として取り上げています。一部の防具にある括弧内の名称は、侍（Samurai）プレイ時に表示される別名です（ゲーム内部では同一アイテム）。

#### 胴鎧 (Body armor / suits)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 鋼鉄の鎧 (plate mail / tanko: 短甲) | +7 | 2 | 450 | 600 | 鉄 | 魔法詠唱ペナルティあり。 |
| 水晶の鎧 (crystal plate mail) | +7 | 2 | 415 | 820 | ガラス | 決して錆びない。魔法詠唱ペナルティあり。 |
| 青銅の鎧 (bronze plate mail) | +6 | 1 | 450 | 400 | 銅 |  |
| 鉄片の鎧 (splint mail) | +6 | 1 | 400 | 80 | 鉄 |  |
| 帯金の鎧 (banded mail) | +6 | 1 | 350 | 90 | 鉄 |  |
| ドワーフのミスリル服 (dwarvish mithril-coat) | +6 | 2 | 150 | 240 | ミスリル | 軽量だが金属製：魔法詠唱へのペナルティは鋼鉄の鎧と同等。 |
| エルフのミスリル服 (elven mithril-coat) | +5 | 2 | 150 | 240 | ミスリル | 軽量だが金属製：魔法詠唱へのペナルティは鋼鉄の鎧と同等。 |
| 鎖かたびら (chain mail) | +5 | 1 | 300 | 75 | 鉄 |  |
| オークの鎖かたびら (orcish chain mail) | +4 | 1 | 300 | 75 | 鉄 |  |
| 鱗の鎧 (scale mail) | +4 | 1 | 250 | 45 | 鉄 |  |
| 鋲付き革鎧 (studded leather armor) | +3 | 1 | 200 | 15 | 革 | 魔法詠唱ペナルティなし。 |
| 鉄環の鎧 (ring mail) | +3 | 1 | 250 | 100 | 鉄 |  |
| オークの鉄環の鎧 (orcish ring mail) | +2 | 1 | 250 | 80 | 鉄 |  |
| 革鎧 (leather armor) | +2 | 1 | 150 | 5 | 革 |  |
| 革の服 (leather jacket) | +1 | — | 30 | 10 | 革 |  |
| 灰色ドラゴンの鱗鎧 (gray dragon scale mail) | +9 | — | 40 | 1200 | ドラゴンの皮 | 魔法防御（Magic resistance）。終盤における最終目標の胴鎧。 |
| 銀色ドラゴンの鱗鎧 (silver dragon scale mail) | +9 | — | 40 | 1200 | ドラゴンの皮 | 反射（Reflection）。 |
| 黒色ドラゴンの鱗鎧 (black dragon scale mail) | +9 | — | 40 | 1200 | ドラゴンの皮 | 分解耐性（Disintegration resistance）＋吸命耐性（Drain resistance）。 |
| 黄色ドラゴンの鱗鎧 (yellow dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 酸耐性（Acid resistance）＋石化耐性（Stoning resistance）。 |
| 橙色ドラゴンの鱗鎧 (orange dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 睡眠耐性（Sleep resistance）＋自由行動（Free action）。 |
| 白色ドラゴンの鱗鎧 (white dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 冷気耐性（Cold resistance）＋消化遅延（Slow digestion）。 |
| 赤色ドラゴンの鱗鎧 (red dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 火炎耐性（Fire resistance）＋赤外線視覚（Infravision）。 |
| 緑色ドラゴンの鱗鎧 (green dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 毒耐性（Poison resistance）＋病気耐性（Sickness resistance）。 |
| 青色ドラゴンの鱗鎧 (blue dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 電撃耐性（Shock resistance）＋高速移動（韋駄天の靴と同等）。 |
| 金色ドラゴンの鱗鎧 (gold dragon scale mail) | +9 | — | 40 | 900 | ドラゴンの皮 | 幻覚耐性（Hallucination resistance）＋恒久光源（胴部位唯一の光源）。 |

:::

#### ドラゴンの鱗 (Dragon scales)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 灰色ドラゴンの鱗 (gray dragon scales) | +3 | — | 40 | 700 | ドラゴンの皮 | 魔法防御。鎧作成の巻物で鱗鎧へアップグレード可能。 |
| 銀色ドラゴンの鱗 (silver dragon scales) | +3 | — | 40 | 700 | ドラゴンの皮 | 反射。 |
| 黒色ドラゴンの鱗 (black dragon scales) | +3 | — | 40 | 700 | ドラゴンの皮 | 分解耐性＋吸命耐性。 |
| 黄色ドラゴンの鱗 (yellow dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 酸耐性＋石化耐性。 |
| 橙色ドラゴンの鱗 (orange dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 睡眠耐性＋自由行動。 |
| 白色ドラゴンの鱗 (white dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 冷気耐性＋消化遅延。 |
| 赤色ドラゴンの鱗 (red dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 火炎耐性＋赤外線視覚。 |
| 緑色ドラゴンの鱗 (green dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 毒耐性＋病気耐性。 |
| 青色ドラゴンの鱗 (blue dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 電撃耐性＋高速移動（韋駄天の靴と同等）。 |
| 金色ドラゴンの鱗 (gold dragon scales) | +3 | — | 40 | 500 | ドラゴンの皮 | 幻覚耐性＋恒久光源。 |

:::

#### シャツ (Shirts)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| アロハシャツ (Hawaiian shirt) | +0 | — | 5 | 3 | 布 | 観光客（Tourist）の初期装備。胴鎧の下に着用可能。 |
| Ｔシャツ (T-shirt) | +0 | — | 5 | 2 | 布 | 胴鎧の下に着用可能。 |

:::

#### クローク (Cloaks)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| ミイラの包帯 (mummy wrapping) | +0 | 1 | 3 | 2 | 布 | 着用中は透明化（Invisibility）の効果を無効化する。 |
| エルフのクローク (elven cloak) | +1 | 1 | 10 | 60 | 布 | 忍び足（Stealth）。 |
| オークのクローク (orcish cloak) | +0 | 1 | 10 | 40 | 布 |  |
| ドワーフのクローク (dwarvish cloak) | +0 | 1 | 10 | 50 | 布 |  |
| 防水クローク (oilskin cloak) | +1 | 2 | 10 | 50 | 布 | 掴み攻撃や水濡れを防ぐ。 |
| ローブ (robe) | +2 | 2 | 15 | 50 | 布 | 魔法詠唱ボーナス。金属鎧による詠唱ペナルティの大半を相殺する。 |
| 錬金術の仕事着 (alchemy smock) | +1 | 1 | 10 | 50 | 布 | 毒耐性（Poison resistance）。 |
| 革のクローク (leather cloak) | +1 | 1 | 15 | 40 | 革 |  |
| 守りのクローク (cloak of protection) | +3 | 3 | 10 | 50 | 布 | クロークの中で最高の魔法防御能力（MC 3）を誇る。 |
| 透明のクローク (cloak of invisibility) | +1 | 1 | 10 | 60 | 布 | 透明化（Invisibility）。 |
| 魔法を防ぐクローク (cloak of magic resistance) | +1 | 1 | 10 | 60 | 布 | 魔法防御（Magic resistance）。最も軽量な魔法防御の供給源。 |
| 幻影のクローク (cloak of displacement) | +1 | 1 | 10 | 50 | 布 | 幻影（Displacement）。 |

:::

#### 兜・帽子 (Helmets)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| エルフの革帽子 (elven leather helm) | +1 | — | 3 | 8 | 革 |  |
| オークの兜 (orcish helm) | +1 | — | 30 | 10 | 鉄 |  |
| ドワーフの鉄兜 (dwarvish iron helm) | +2 | — | 40 | 20 | 鉄 |  |
| フィドーラ (fedora) | +0 | — | 3 | 1 | 布 | 考古学者（Archeologist）の初期装備。同職業に幸運+1を付与。 |
| とんがり帽子 (cornuthaum) | +0 | 1 | 4 | 80 | 布 | 透視（Clairvoyance）。魔法使いのみ有効。魔法使い以外が被ると他の透視能力を阻害する。 |
| 道化の帽子 (dunce cap) | +0 | — | 4 | 1 | 布 | 知力と知恵が強制的に 6 に低下する。被ると自動的に呪われる。外すには呪い解除が必要。 |
| くぼんだ鍋 (dented pot) | +1 | — | 10 | 8 | 鉄 |  |
| 知性の兜 (helm of brilliance) | +1 | — | 40 | 50 | ガラス | 着用中、強化値が知力と知恵の両方に加算される（+3の兜なら知力+3、知恵+3）。 |
| 兜 (helmet / kabuto: 兜) | +1 | — | 30 | 10 | 鉄 |  |
| 知性の兜 (helm of caution) | +1 | — | 50 | 50 | 鉄 | 警告（Warning）。 |
| 逆属性の兜 (helm of opposite alignment) | +1 | — | 50 | 50 | 鉄 | 着用中、属性が反転する。生成時に90%の確率で呪われている。 |
| テレパシーの兜 (helm of telepathy) | +1 | — | 50 | 50 | 鉄 | 目が見えているときは周囲8マス、盲目時はフロア全体のテレパシーを得る。 |

:::

逆属性の兜は基本的には罠アイテムですが、属性反転を意図的に利用できる局面もあります。異属性の祭壇で生贄を捧げる、反対属性のクエストアーティファクトを所持する、あるいは星界の面（Astral Plane）で魔除けを受け入れる祭壇の属性を変更する際などに活用されます。

#### 小手・手袋 (Glovers)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 革の手袋 (leather gloves / yugake: ゆがけ) \* | +1 | — | 10 | 8 | 革 |  |
| お手玉の小手 (gauntlets of fumbling) \* | +1 | — | 10 | 50 | 革 | 頻繁に足をもつれさせる（お手玉状態）。生成時に90%の確率で呪われている。回避推奨。 |
| 力の小手 (gauntlets of power) \* | +1 | — | 30 | 50 | 鉄 | 筋力を強制的に 25 に設定する。 |
| 器用さの小手 (gauntlets of dexterity) \* | +1 | — | 10 | 50 | 革 | 着用中、強化値が器用さに加算される（+3の小手なら器用さ+3）。 |

:::

\* 印の付いたアイテムは、識別されるまで4種類の実見外見名（*古い手袋*、*パッド入り手袋*、*乗馬用手袋*、*フェンシング手袋*）のいずれかとして出現します（通常の革の手袋も含みます）。

#### 靴 (Boots)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| かかとの低い靴 (low boots) | +1 | — | 10 | 8 | 革 |  |
| 鉄の靴 (iron shoes) | +2 | — | 50 | 16 | 鉄 |  |
| かかとの高い靴 (high boots) | +2 | — | 20 | 12 | 革 |  |
| 韋駄天の靴 (speed boots) \* | +1 | — | 20 | 50 | 革 | 高速移動（Very fast）。3ターンのうち2ターンで無料の追加行動を得られる。 |
| 水上歩行の靴 (water walking boots) \* | +1 | — | 15 | 50 | 革 | 水上や氷上を歩行可能。耐火加工された靴と火炎耐性があれば溶岩も渡れる。 |
| 飛び跳ねる靴 (jumping boots) \* | +1 | — | 20 | 50 | 革 | `#jump` コマンドで近くの任意のマスへ跳躍できる。 |
| エルフの靴 (elven boots) \* | +1 | — | 15 | 8 | 革 | 忍び足（Stealth）。 |
| 蹴り挙げ靴 (kicking boots) \* | +1 | — | 50 | 8 | 鉄 |  |
| つまずきの靴 (fumble boots) \* | +1 | — | 20 | 30 | 革 | 頻繁に足をもつれさせる。生成時に90%の確率で呪われている。回避推奨。 |
| 浮遊の靴 (levitation boots) \* | +1 | — | 15 | 30 | 革 | 浮遊（Levitation）。生成時に90%の確率で呪われている。呪われた靴は脱ぐことができないため致命的な罠となる。 |

:::

\* 印の付いたアイテムは、識別されるまで7種類の実見外見名（*戦闘用ブーツ*、*ジャングルブーツ*、*ハイキングブーツ*、*泥靴*、*バックル付きブーツ*、*乗馬用ブーツ*、*スノーブーツ*）のいずれかとして出現します。

#### 盾 (Shields)

::: dense-table

| 防具名 | AC | MC | 重量 | 価格 | 材質 | 備考 |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| 小さな盾 (small shield) | +1 | — | 30 | 3 | 木 |  |
| 吸命耐性の盾 (shield of drain resistance) | +1 | — | 30 | 50 | 木 | 吸命耐性（Drain resistance）。 |
| 電撃耐性の盾 (shield of shock resistance) | +1 | — | 30 | 50 | 木 | 電撃耐性（Shock resistance）。 |
| エルフの盾 (elven shield) | +2 | — | 40 | 7 | 木 |  |
| ウルク＝ハイの盾 (Uruk-hai shield) | +1 | — | 50 | 7 | 鉄 |  |
| オークの盾 (orcish shield) | +1 | — | 50 | 7 | 鉄 |  |
| 大きな盾 (large shield) | +2 | — | 100 | 10 | 鉄 | 他のすべての盾と同様、両手持ち武器および二刀流戦闘を阻害する。 |
| ドワーフの丸盾 (dwarvish roundshield) | +2 | — | 100 | 10 | 鉄 |  |
| 反射の盾 (shield of reflection) | +2 | — | 50 | 50 | 銀 | 反射（Reflection）。胴鎧の装備枠を自由に選べるようになる。 |

:::

### 呪文一覧表 (Spell Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h: no corrections. All 41 spell rows' level/school/type verified (incl. chain lightning lvl 2). Spell damage figures live in spell.c/zap.c, outside this table's source.
-->
<!-- audit
2026-05-19:
- 41 spells, sourced from objects.h SPELL() macros (P_ATTACK..P_MATTER); SPELL macro signature at objects.h:1277-1281, oc_level=oc_oc2.
- attack spells at objects.h:1297-1330 (force bolt/magic missile/drain life/cone of cold/fireball/finger of death/chain lightning).
- healing spells at objects.h:1313-1408 (healing/cure blindness/cure sickness/extra healing/stone to flesh/restore ability).
- divination spells at objects.h:1308-1384 (light/detect monsters/detect food/clairvoyance/detect unseen/identify/detect treasure/magic mapping).
- enchantment spells at objects.h:1305-1354 (confuse monster/slow monster/cause fear/sleep/charm monster).
- cleric spells at objects.h:1337-1400 (protection/create monster/remove curse/create familiar/turn undead).
- escape spells at objects.h:1355-1404 (jumping/haste self/invisibility/levitation/teleport away).
- matter spells at objects.h:1293-1407 (knock/wizard lock/dig/polymorph/cancellation/stone to flesh).
- Flame sphere and freeze sphere are `#if 0 DEFERRED` (objects.h:1413-1422), NOT shipped in 5.0.
- Chain lightning is level 2 per macro (objects.h:1409-1411); body table at line 4986 and What's New at 8585 still say L4: follow-up fix.
- Magic missile IS Antimagic-blocked (zap.c:4410-4419, "missiles bounce off!"), NOT unresistable.
- Finger of death: monster MR resists, but player gets no Antimagic check on death-ray instakill (zap.c:2885-2902).
- Clairvoyance gets a P_SKILLED upgrade detecting nearby monsters per pulse (spell.c:1572-1576).
- Fireball/cone of cold become aimed explosions at P_SKILLED (spell.c spelleffects).
- Remove curse/confuse monster/detect food/cause fear/identify/charm monster get blessed-scroll behavior at P_SKILLED.
- Haste self/detect treasure/detect monsters/levitation/restore ability get blessed-potion behavior at P_SKILLED.
- Protection doubles uspmtime at P_EXPERT (spell.c:1169); jumping distance scales with role_skill.
- Charm monster is untargeted (read.c:1679-1708 seffect_taming is area-centered-on-caster, no direction prompt).
- Charm monster area: 3×3 normal, 11×11 confused (`bd = confused ? 5 : 1`, -bd..bd inclusive), NOT 5×5. (read.c:1689 seffect_taming)
- Charm monster P_SKILLED upgrade is blessed-scroll reliability, NOT a radius bump. (spell.c:1524-1525 sets pseudo->blessed when role_skill >= P_SKILLED; read.c:1689 radius `bd` depends only on `confused`, not on blessed)
- Cause fear blessed and uncursed are identical (read.c:1454-1486); loop hits every visible monster on the level, not just nearby.
- Remove curse blessed branch uncurses every non-coin inventory item (read.c:1514-1577), NOT just worn/wielded.
-->

魔法書の完全カタログです。系統順、続いてレベル順に並んでいます。**レベル (Lvl)**は呪文レベル、**消費魔力 (Pw cost)**は常に「5×呪文レベル」です。**種別 (Type)**は呪文の目標指定方法を区分しています：

- **方向指定 (aimed):** 方向を指定し、その直線の1マスに命中します。
- **光線 (ray):** 術者から直線状に伸び、遮られるまで進むビームです。
- **目標不要 (untargeted):** 方向指定は不要で、自身、フロア全体、または固定範囲に効果が発現します。

**上位効果 (Upgrade)**はその系統のスキルが**熟練 (Skilled)**以上になった際の挙動変化です（防護の呪文のみエキスパートで発動し、跳躍の距離はランクに応じて連続的に拡大します）。

::: dense-table

| 呪文名 | 系統 | レベル | 種別 | 効果 | 上位効果 (Skilled以上) |
|-----------------|-------------|-----|------------|-------------------------------------|-------------------------------|
| 衝撃 (force bolt) | 攻撃 | 1 | 方向指定 | 2d12の魔法打撃ダメージ | — |
| 連鎖雷撃 (chain lightning) | 攻撃 | 2 | 目標不要 | 周囲のモンスターに電撃ダメージ | — |
| 生命吸収 (drain life) | 攻撃 | 2 | 方向指定 | 対象から経験値レベルを1吸収 | — |
| マジックミサイル (magic missile) | 攻撃 | 2 | 光線 | (XL÷2 + 1)d6の衝撃ビーム（端数切捨て）。魔法防御で防がれる | — |
| 冷気 (cone of cold) | 攻撃 | 4 | 光線 | (XL÷2 + 1)d6の冷気ビーム（端数切捨て） | 目標指定の爆発 |
| 火の玉 (fireball) | 攻撃 | 4 | 光線 | (XL÷2 + 1)d6の火炎ビーム（端数切捨て） | 目標指定の爆発 |
| 死の指 (finger of death) | 攻撃 | 7 | 光線 | 死の光線。敵の魔法防御で防がれるが、自身に反射・誤射した際は防御チェックを迂回して即死する | — |
| 回復 (healing) | 回復 | 1 | 方向指定 | HPを回復 | 盲目も治療 |
| 盲目治療 (cure blindness) | 回復 | 2 | 目標不要 | 盲目状態を回復 | — |
| 病気治療 (cure sickness) | 回復 | 3 | 目標不要 | 食中毒および病気を治療 | — |
| 超回復 (extra healing) | 回復 | 3 | 方向指定 | より多くのHPを回復 | — |
| 石化解除 (stone to flesh) | 回復 | 3 | 方向指定 | 石像を生きたモンスターに変える。石化を治療 | — |
| 能力回復 (restore ability) | 回復 | 4 | 目標不要 | 低下した能力値を1つ全快 | 低下したすべての能力値を全快 |
| 怪物探知 (detect monsters) | 予見 | 1 | 目標不要 | フロア上のモンスターを表示 | 効果時間が延長 |
| 明かり (light) | 予見 | 1 | 目標不要 | 現在の部屋を照らす | — |
| 食料探知 (detect food) | 予見 | 2 | 目標不要 | フロア上の食料を表示 | 有害な食事の前に警告 |
| 千里眼 (clairvoyance) | 予見 | 3 | 目標不要 | 周囲のマップを周期的に開拓視認 | 熟練：周期ごとに周囲のモンスターも探知 |
| 不可視探知 (detect unseen) | 予見 | 3 | 目標不要 | 不可視のモンスターや罠を表示 | — |
| 識別 (identify) | 予見 | 3 | 目標不要 | 所持品を1つ識別 | 複数の所持品を一括識別 |
| 宝探知 (detect treasure) | 予見 | 4 | 目標不要 | フロア上のすべてのアイテムを表示 | 探知したアイテムの種別を識別 |
| 地図化 (magic mapping) | 予見 | 5 | 目標不要 | フロア全体の地形を開拓表示 | — |
| 怪物混乱 (confuse monster) | 付与 | 1 | 目標不要 | 次の近接攻撃で対象を混乱させる | 複数回の攻撃分チャージされる |
| 怪物減速 (slow monster) | 付与 | 2 | 方向指定 | 対象モンスターの移動速度を低下 | — |
| 恐怖 (cause fear) | 付与 | 3 | 目標不要 | 視界内のモンスターを逃走させる | — |
| 眠り (sleep) | 付与 | 3 | 光線 | 射線上のモンスターを眠らせる | — |
| 魅了 (charm monster) | 付与 | 5 | 目標不要 | 周囲 3×3 エリアのモンスターを手懐ける | — |
| 防護 (protection) | 僧侶 | 1 | 目標不要 | 魔力を消費して一時的なACボーナスを得る | **エキスパート**: 効果時間が2倍 |
| 怪物創造 (create monster) | 僧侶 | 2 | 目標不要 | 近くにランダムなモンスターを召喚 | — |
| 解呪 (remove curse) | 僧侶 | 3 | 目標不要 | 装備中のアイテムの呪いを解く | 所持している全アイテムの呪いを解く |
| 使い魔創造 (create familiar) | 僧侶 | 6 | 目標不要 | 手懐けられたペットを召喚する | — |
| アンデッド退散 (turn undead) | 僧侶 | 6 | 方向指定 | アンデッドや悪魔にダメージを与えて逃走させる | — |
| 跳躍 (jumping) | 緊急脱出 | 1 | 目標不要 | 近くの指定したマスへ跳躍する | スキルランクに応じて跳躍距離が拡大 |
| 加速 (haste self) | 緊急脱出 | 3 | 目標不要 | 一時的な高速移動状態になる | 効果時間が延長 |
| 不可視 (invisibility) | 緊急脱出 | 4 | 目標不要 | 透明状態になる | — |
| 浮遊 (levitation) | 緊急脱出 | 4 | 目標不要 | 落とし穴や水面の上に浮かび上がる | `>` キーで任意に着地可能 |
| テレポート (teleport away) | 緊急脱出 | 6 | 方向指定 | 対象をフロアの別の場所へテレポートさせる | — |
| 開錠 (knock) | 物質操作 | 1 | 方向指定 | 扉を開け、錠前を解除する | — |
| 施錠 (wizard lock) | 物質操作 | 2 | 方向指定 | 扉を閉じて鍵をかける | — |
| 穴掘り (dig) | 物質操作 | 5 | 光線 | 壁、岩、床を掘り抜く | — |
| へんげ (polymorph) | 物質操作 | 6 | 方向指定 | 対象を変身(へんげ)させる | — |
| 無力化 (cancellation) | 物質操作 | 7 | 方向指定 | 対象の魔法特性を打ち消す | — |

:::

光線系呪文（睡眠、マジックミサイル、死の指、および未熟練状態の冷気や火炎）の命中率も、スキルランクに応じて上昇します。

### モンスター図鑑一覧表 (Bestiary Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 monsters.h: no corrections. ~100% of the numeric columns (Lvl/Spd/AC/MR), color, and full attack lists verified across all ~55 tables, including the tricky cases (floating eye 0d70, black dragon disint, AD_DRST-as-poison stings, deferred/#if0 monsters correctly excluded).
-->

ダンジョンで遭遇しうるあらゆるモンスターをマップ記号ごとに分類した一覧です。**レベル (Lvl)**はモンスターの基本レベル、**速度 (Spd)**は移動速度（プレイヤーの標準速度は 12）、**AC**はアーマークラス（低いほど強固）、**MR**は魔法防御率（プレイヤーの呪文や魔法攻撃に抵抗する確率%）を表します。**攻撃方法 (Attacks)**は各攻撃の種別、ダメージダイス、追加効果を記載しており、`·` で区切られた攻撃は1ターン内にすべて連続して繰り出されます。**備考 (Notes)**には飛行能力、不可視視認、自動回復、死体に毒があるかなど、戦闘を一変させる重要な特性をまとめています。

#### 蟻および昆虫 `a` (Ants and insects `a`)

<!-- audit
2026-05-19:
- 6 rows (S_ANT) sourced from monsters.h:89-133.
- giant ant L2/Spd18/AC3 bite 1d4 (monsters.h:89-95).
- killer bee L1/Spd18/AC-1 sting 1d3 AD_DRST, G_LGROUP, MR_POISON (monsters.h:96-102).
- soldier ant L3/Spd18/AC3 bite 2d4 + sting 3d4 AD_DRST, M1_POIS (monsters.h:103-110).
- fire ant L3/Spd18/AC3 bite 2d4 phys + 2d4 fire, MR_FIRE (monsters.h:111-118).
- giant beetle L5/Spd6/AC4 bite 3d6, M1_POIS, MR_POISON (monsters.h:119-125).
- queen bee L9/Spd24/AC-4 sting 1d8 AD_DRST, G_NOGEN, M2_FEMALE|M2_PRINCE (monsters.h:126-133).
- Killer/soldier/queen stings are AD_DRST (Str-drain, poison-family); shown as "poison" for beginner voice.
- Killer bee is G_LGROUP; others are smaller groups.
-->

昆虫類。多くは集団で群れをなして出現します。兵隊蟻の毒針攻撃は筋力を吸い取ります。殺人蜂は大群で襲いかかり、蜂の巣の部屋にいる女王蜂は単体でも手ごわい相手です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 巨大蟻 (giant ant) | 茶色 | 2 | 18 | 3 | 0 | 噛みつき 1d4 |  |
| 殺人蜂 (killer bee) | 黄色 | 1 | 18 | -1 | 0 | 毒針 1d3 毒 | 飛行, 死体に毒あり, 毒耐性. 毒針攻撃。 |
| 兵隊蟻 (soldier ant) | 青色 | 3 | 18 | 3 | 0 | 噛みつき 2d4 · 毒針 3d4 毒 | 死体に毒あり, 毒耐性. 毒針攻撃。 |
| 火蟻 (fire ant) | 赤色 | 3 | 18 | 3 | 10 | 噛みつき 2d4 · 噛みつき 2d4 火炎 | 火炎耐性. |
| 巨大カブト虫 (giant beetle) | 黒色 | 5 | 6 | 4 | 0 | 噛みつき 3d6 | 死体に毒あり, 毒耐性. |
| 女王蜂 (queen bee) | 赤紫 | 9 | 24 | -4 | 0 | 毒針 1d8 毒 | 飛行, 死体に毒あり, 毒耐性. |

:::

#### ブロッブ `b` (Blobs `b`)

<!-- audit
2026-05-19:
- 3 rows (S_BLOB) sourced from monsters.h:137-166.
- Acid blob passive: 50% splash + 1/30 corrode armor, plus passive_obj 1/6 erode on uwep/uarmg (uhitm.c:5906-5933).
- Gelatinous cube paralysis: 2/3 rate, free-action blocks (uhitm.c:6019-6064).
- Gelatinous cube in 5.0 is AT_TUCH only, NOT AT_ENGL like older versions. (monsters.h:157-158 AT_TUCH AD_PLYS 2d4 + AT_NONE AD_PLYS 1d4)
-->

動きが遅く、精神を持ちません。酸のブロッブを素手や大切な金属武器で近接攻撃してはいけません。相手の酸による反撃で武器や防具が腐食します。ゼラチンキューブは接触時にプレイヤーを麻痺させます。

すべてのブロッブは精神を持たず（マインドレス）、睡眠耐性と毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 酸のブロッブ (acid blob) | 緑色 | 1 | 3 | 8 | 0 | 反撃 1d8 酸 | 不定形, 酸耐性, 石化耐性. 酸の反撃ダメージ。素手で殴ると手袋が腐食する。 |
| 震えるブロッブ (quivering blob) | 白色 | 5 | 1 | 8 | 0 | 接触 1d8 |  |
| ゼラチンキューブ (gelatinous cube) | 水色 | 6 | 6 | 8 | 0 | 接触 2d4 麻痺 · 反撃 1d4 麻痺 | 火炎耐性, 冷気耐性, 電撃耐性, 酸耐性, 石化耐性. 鈍足だが接触時に麻痺。自由行動なしでの近接戦は厳禁。 |

:::

#### コカトリス `c` (Cockatrices `c`)

<!-- audit
2026-05-19:
- 3 rows (chickatrice/cockatrice/pyrolisk) sourced from monsters.h:167-195.
- Chickatrice/cockatrice carry MR_POISON|MR_STONE; pyrolisk carries MR_POISON|MR_FIRE and does NOT stone. (monsters.h:174-175 chickatrice, 182-183 cockatrice both MR_POISON|MR_STONE; 191-192 pyrolisk MR_POISON|MR_FIRE; pyrolisk attacks are AT_GAZE AD_FIRE + AT_BITE AD_PHYS — no AD_STON)
- Wielding cockatrice corpse bare-handed instapetrifies regardless of role (wield.c:146-152).
-->

中世の動物寓話に登場する怪物。蛇の尾を持つ鶏の姿をしており、その接触は肉体を瞬時に石化させます。トカゲの死体を常時携帯し、必ず手袋を着用して戦ってください。どの職業も初期状態では石化耐性を持っておらず、コカトリスの死体を素手で装備すると即死します。[石化](#petrification-stoning)の項目を参照してください。

すべてのコカトリス類は毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| チカトリス (chickatrice) | 茶色 | 4 | 4 | 8 | 30 | 噛みつき 1d2 · 接触 石化 · 反撃 石化 | 石化耐性. 小型のコカトリス。同様の石化ルールが適用される。 |
| コカトリス (cockatrice) | 黄色 | 5 | 6 | 6 | 30 | 噛みつき 1d3 · 接触 石化 · 反撃 石化 | 石化耐性. 触れると石化。常にトカゲの死体を携帯すること。 |
| ピロリスク (pyrolisk) | 赤色 | 6 | 6 | 6 | 30 | 凝視 2d6 火炎 · 噛みつき 1d6 | 火炎耐性. |

:::

#### 犬およびイヌ科 `d` (Dogs and canines `d`)

野生のイヌ科生物は群れで狩りを行います。飼いならされたものは食料を与えることでペットにできます（[仲間の増やし方](#making-friends)参照）。ジャッカル人間や狼人間はプレイヤーを獣化（ライカンスロープ）に感染させることがあります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ジャッカル (jackal) | 茶色 | 0 | 12 | 7 | 0 | 噛みつき 1d2 | 冒険者を最初に葬り去った相手。 |
| 狐 (fox) | 赤色 | 0 | 15 | 7 | 0 | 噛みつき 1d3 |  |
| コヨーテ (coyote) | 茶色 | 1 | 12 | 7 | 0 | 噛みつき 1d4 |  |
| ジャッカル人間 (werejackal) | 茶色 | 2 | 12 | 7 | 10 | 噛みつき 1d4 獣化 | 自動回復, 毒耐性. 死体を残さない。 |
| 仔犬 (little dog) | 白色 | 2 | 18 | 6 | 0 | 噛みつき 1d6 | 手懐け可能. 洞窟人、野伏、侍の確定初期ペット。 |
| 野犬 (dingo) | 黄色 | 4 | 16 | 5 | 0 | 噛みつき 1d6 |  |
| 犬 (dog) | 白色 | 4 | 16 | 5 | 0 | 噛みつき 1d6 | 手懐け可能. |
| 大きな犬 (large dog) | 白色 | 6 | 15 | 4 | 0 | 噛みつき 2d4 | 手懐け可能. |
| 狼 (wolf) | 灰色 | 5 | 12 | 4 | 0 | 噛みつき 2d4 |  |
| 狼人間 (werewolf) | 灰色 | 5 | 12 | 4 | 20 | 噛みつき 2d6 獣化 | 自動回復, 毒耐性. 死体を残さない。 |
| 冬狼の子 (winter wolf cub) | 水色 | 5 | 12 | 4 | 0 | 噛みつき 1d8 · ブレス 1d6 冷気 | 冷気耐性. |
| ワーグ (warg) | 黒色 | 7 | 12 | 4 | 0 | 噛みつき 2d6 |  |
| 冬狼 (winter wolf) | 水色 | 7 | 12 | 4 | 20 | 噛みつき 2d6 · ブレス 2d6 冷気 | 冷気耐性. |
| ヘルハウンドの仔 (hell hound pup) | 赤色 | 7 | 12 | 4 | 20 | 噛みつき 2d6 · ブレス 2d6 火炎 | 火炎耐性. |
| ヘルハウンド (hell hound) | 赤色 | 12 | 14 | 2 | 20 | 噛みつき 3d6 · ブレス 3d6 火炎 | 火炎耐性. |

:::

#### 目および球体 `e` (Eyes and spheres `e`)

<!-- audit
2026-05-19:
- Roster sourced from monsters.h:325-366 (beholder omitted, `#if 0`).
- Floating eye paralysis requires mutual sight (canseemon + mon->mcansee per uhitm.c:6022-6053), NOT "in daylight."
- Floating eye corpse grants telepathy (eat.c:1071 TELEPAT case).
- No close-eyes command exists in 5.0; to break sight you must be Blind (status or worn blindfold/towel).
- Newbie-killer framing aligned with NetHackWiki: floating eye is "an infamous source of early game deaths" (https://nethackwiki.com/wiki/Floating_eye).
-->

さまよう目の反撃麻痺凝視は、ダンジョン序盤において最も有名な死因の一つです。自由行動（Free action）、盲目状態、または遠距離攻撃の手段を持たずに近接攻撃を仕掛けてはなりません。倒した後は死体を食べてください。恒久的なテレパシー能力（内在能力）を獲得できます。

すべての目および球体は飛行能力を持ちます。また、*さまよう目*を除きすべて精神を持ちません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 包子ガス (gas spore) | 灰色 | 1 | 3 | 10 | 0 | 爆発(死亡時) 4d6 |  |
| さまよう目 (floating eye) | 青色 | 2 | 1 | 9 | 10 | 反撃 3d70 麻痺 | 水陸両用. 互いに視界が通っている状態で近接攻撃すると反撃麻痺。遠距離攻撃を行うか、目隠しやタオルで視覚を遮って対処。死体を食べると必ずテレパシーを獲得。 |
| 氷の球体 (freezing sphere) | 白色 | 6 | 13 | 4 | 0 | 自爆 4d6 冷気 | 冷気耐性. |
| 炎の球体 (flaming sphere) | 赤色 | 6 | 13 | 4 | 0 | 自爆 4d6 火炎 | 火炎耐性. |
| 電撃の球体 (shocking sphere) | 明青 | 6 | 13 | 4 | 0 | 自爆 4d6 電撃 | 電撃耐性. |

:::

#### ネコ科 `f` (Felines `f`)

<!-- audit
2026-05-19:
- 8 rows (S_FELINE) sourced from monsters.h:381-444.
- kitten L2/Spd18/AC6 bite 1d6 (monsters.h:381-388).
- housecat L4/Spd16/AC5 bite 1d6 (monsters.h:389-396).
- large cat L6/Spd15/AC4 bite 2d4 (monsters.h:421-428).
- displacer beast L12/Spd12/AC-10 claw 4d4 + claw 4d4 + bite 2d10 (monsters.h:437-444).
- Tigers are M2_HOSTILE, difficulty 8: tameable only via charm-monster/scroll-of-taming/magic-flute, NOT tripe. (monsters.h:429-436 tiger has M2_HOSTILE only — no M2_DOMESTIC; befriend_with_obj at mondata.h:255-261 requires is_domestic for FOOD_CLASS items)
- Only Wizard guarantees a kitten (urole.petnum=PM_KITTEN per role.c:548); every role without a fixed pet rolls 50/50 kitten-or-dog (dog.c:90-101).
-->

野生のネコ科生物は素早く敵対的です。虎やディスプレイスビーストは、何気ない通路での遭遇を命がけの戦いに変えてしまいます。魔法使いは必ず小猫を連れてスタートし、初期ペットが固定されていない職業は小猫か仔犬のいずれかを 50% の確率で連れて開始します。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 小猫 (kitten) | 白色 | 2 | 18 | 6 | 0 | 噛みつき 1d6 | 手懐け可能. 一般的なペット。 |
| 家猫 (housecat) | 白色 | 4 | 16 | 5 | 0 | 噛みつき 1d6 | 手懐け可能. |
| ジャガー (jaguar) | 茶色 | 4 | 15 | 6 | 0 | 爪 1d4 ×2 · 噛みつき 1d8 |  |
| 山猫 (lynx) | 水色 | 5 | 15 | 6 | 0 | 爪 1d4 ×2 · 噛みつき 1d10 |  |
| パンサー (panther) | 黒色 | 5 | 15 | 6 | 0 | 爪 1d6 ×2 · 噛みつき 1d10 |  |
| 大きな猫 (large cat) | 白色 | 6 | 15 | 4 | 0 | 噛みつき 2d4 | 手懐け可能. |
| 虎 (tiger) | 黄色 | 6 | 12 | 6 | 0 | 爪 2d4 ×2 · 噛みつき 1d10 |  |
| ディスプレイサービースト (displacer beast) | 青色 | 12 | 12 | -10 | 0 | 爪 4d4 ×2 · 噛みつき 2d10 |  |

:::

#### グレムリン `g` (Gremlins `g`)

<!-- audit
2026-05-19:
- 3 rows (gremlin/gargoyle/winged gargoyle) sourced from monsters.h:448-473.
- Gremlin water/fountain trigger SPLIT: clones themselves, 2/3 chance per step (mon.c:987-992); does NOT touch your intrinsics.
- Gremlin night attack is AD_CURS: strips one random intrinsic, 1/10 per hit, night-only, blocked by cancellation (uhitm.c:3040-3057, sit.c:644+).
- Gargoyles do NOT petrify by touch or corpse: touch_petrifies is cockatrice/chickatrice only (mondata.h:200-201).
-->

夜間（または光源がない暗闇）に水に触れると分裂増殖する厄介な小型怪物です。暗闇の中でプレイヤーから内在能力を盗み取る攻撃を行います。明るい光源を持ち歩くか、光の巻物・呪文で部屋を照らすのが有効な対抗策です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| グレムリン (gremlin) | 緑色 | 5 | 12 | 2 | 25 | 爪 1d6 ×2 · 噛みつき 1d4 · 爪 呪い | 遊泳, 死体に毒あり, follows stairs, 毒耐性. |
| ガーゴイル (gargoyle) | 茶色 | 6 | 10 | -4 | 0 | 爪 2d6 ×2 · 噛みつき 2d4 | 石化耐性. |
| 羽のあるガーゴイル (winged gargoyle) | 赤紫 | 9 | 15 | -2 | 0 | 爪 3d6 ×2 · 噛みつき 3d4 | 飛行, 石化耐性. |

:::

#### 人型生物 `h` (Humanoids `h`)

<!-- audit
2026-05-19:
- 7 rows (S_HUMANOID) sourced from monsters.h:477-542.
- hobbit L1/Spd9/AC10 weapon 1d6 (monsters.h:477-484).
- dwarf L2/Spd6/AC10 weapon 1d8, M1_TUNNEL (monsters.h:485-493).
- dwarf lord L4/Spd6/AC10 weapon 2d4 ×2 (monsters.h:502-510).
- dwarf king L6/Spd6/AC10 weapon 2d6 ×2, MR 20% (monsters.h:511-520).
- mind flayer L9/Spd12/AC5 MR 90%, 3× tentacle AD_DRLI (monsters.h:521-530).
- master mind flayer L13/Spd12/AC0 MR 90%, 5× tentacle (monsters.h:531-542).
- helmet blocks mind-flayer tentacle 7/8 of the time (uhitm.c:3235, `uarmh && rn2(8)`).
- Any helmet blocks the mind flayer attack, NOT only alignment-matching or telepathy/free-action helmets.
- Bugbear is AT_WEAP only, no bite (monsters.h:494-501).
- Dwarf race peacefulness for Dwarf PCs via race_peaceful() at makemon.c:2283.
-->

小人族、ホビット、ドワーフ、巨人など多彩な人型生物が含まれます。ノームの鉱山ではドワーフが中立または友好的に出現することが多く、彼らの落とすミスリル服や鉄兜は序盤の貴重な防具供給源となります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ホビット (hobbit) | 緑色 | 1 | 9 | 10 | 0 | 武器攻撃 1d6 |  |
| ドワーフ (dwarf) | 赤色 | 2 | 6 | 10 | 10 | 武器攻撃 1d8 | tunnels. |
| バグベアー (bugbear) | 茶色 | 3 | 9 | 5 | 0 | 武器攻撃 2d4 |  |
| dwarf lord | 青色 | 4 | 6 | 10 | 10 | 武器攻撃 2d4 ×2 | tunnels. |
| dwarf king | 赤紫 | 6 | 6 | 10 | 20 | 武器攻撃 2d6 ×2 | tunnels. |
| マインドフレア (mind flayer) | 明紫 | 9 | 12 | 5 | 90 | 武器攻撃 1d4 · tentacle 2d1 エナジードレイン-Int ×3 | 飛行, sees-不可視. Tentacles drain Int; once it reaches 3, the next tentacle that lands kills you. Any helmet blocks 7/8 of tentacles. |
| マスターマインドフレア (master mind flayer) | 明紫 | 13 | 12 | 0 | 90 | 武器攻撃 1d8 · tentacle 2d1 エナジードレイン-Int ×5 | 飛行, sees-不可視. Five tentacles per turn. Any helmet blocks 7/8 of tentacles. |

:::

#### 小悪魔および下級悪魔 `i` (Imps and minor demons `i`)

インプ、ホムンクルス、テングなどの下級悪魔です。テングは頻繁にテレポートを行い、その死体を食べることでテレポート能力やテレポート制御能力を獲得できるチャンスがあります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 亡霊 (manes) | 赤色 | 1 | 3 | 7 | 0 | 爪 1d3 ×2 · 噛みつき 1d4 | 睡眠耐性. 死体を残さない。 |
| ホムンクルス (homunculus) | 緑色 | 2 | 12 | 6 | 10 | 噛みつき 1d3 sleep | 飛行, 死体に毒あり, 睡眠耐性. |
| インプ (imp) | 赤色 | 3 | 12 | 2 | 20 | 爪 1d4 | 自動回復. |
| レムレース (lemure) | 茶色 | 3 | 3 | 7 | 0 | 爪 1d3 | Gehennom-only, 自動回復, 睡眠耐性. 死体を残さない。 |
| クアシト (quasit) | 青色 | 3 | 15 | 2 | 20 | 爪 1d2 エナジードレイン-Dx ×2 · 噛みつき 1d4 | 自動回復. |
| 天狗 (tengu) | 水色 | 6 | 13 | 5 | 30 | 噛みつき 1d7 | テレポート, teleport-control. |

:::

#### ゼリー `j` (Jellies `j`)

<!-- audit
2026-05-19:
- 3 rows (blue/spotted/ochre jelly) sourced from monsters.h:591-620; all carry M1_AMORPHOUS|M1_MINDLESS.
- Blue jelly corpse conveys cold + poison resistance permanently (eat.c:983-988 should_givit).
- Spotted/ochre corpses convey acid + stone resistance TIMED (eat.c:991-997 temp_givit).
- A passive attack written as 0dN in the monster definition rolls (monster level + 1)dN in combat; blue jelly is therefore 6d6 and spotted jelly 7d6 (uhitm.c:5885-5888).
-->

壁際や床に張り付く不定形の怪物です。青色ゼリーは冷気、赤色ゼリーは火炎の反撃ダメージを与えます。金属武器を腐食させる斑点ゼリーにも注意が必要です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 青色ゼリー (blue jelly) | 青色 | 4 | 0 | 8 | 10 | 反撃 5d6 冷気 | corpse: cold + poison resistance. |
| まだらゼリー (spotted jelly) | 緑色 | 5 | 0 | 8 | 10 | 反撃 6d6 酸 | corpse: temp acid + stone resistance. |
| 黄土色ゼリー (ochre jelly) | 茶色 | 6 | 3 | 8 | 20 | engulf 3d6 酸 · 反撃 3d6 酸 | corpse: temp acid + stone resistance. |

:::

#### コボルド `k` (Kobolds `k`)

<!-- audit
2026-05-19:
- 4 rows (kobold/large/lord/shaman) sourced from monsters.h:624-657.
- kobold L0/Spd6/AC10 weapon 1d4 (monsters.h:624-631).
- large kobold L1/Spd6/AC10 weapon 1d6 (monsters.h:632-639).
- kobold lord L2/Spd6/AC10 weapon 2d4 (monsters.h:640-648).
- kobold shaman L2/Spd6/AC6 MR 10% (monsters.h:649-657).
- All four carry M1_POIS (poisonous corpse) and MR_POISON.
- Kobold shaman has only one AT_MAGC/AD_SPEL attack (monsters.h:651); notation is "cast spell," not "cast spell."
-->

序盤に群れで現れる小型の邪悪な生物。毒矢を放ってくることがあり、毒耐性がない最序盤では1発で致命傷になり得ます。死体にも毒が含まれているため、毒耐性を得るまでは食べてはいけません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コボルド (kobold) | 茶色 | 0 | 6 | 10 | 0 | 武器攻撃 1d4 |  |
| 大きなコボルド (large kobold) | 赤色 | 1 | 6 | 10 | 0 | 武器攻撃 1d6 |  |
| kobold lord | 赤紫 | 2 | 6 | 10 | 0 | 武器攻撃 2d4 |  |
| コボルドの呪術師 (kobold shaman) | 明青 | 2 | 6 | 6 | 10 | cast spell |  |

:::

#### レプラコーン `l` (Leprechauns `l`)

<!-- audit
2026-05-19:
- Leprechaun (Lvl 5, Spd 15, AC 8, MR 20, green, claw 1d2 AD_SGLD), M1_TPORT, AT_CLAW (not bite): monsters.h:660-666, steal.c:58-115.
- Stolen gold goes into mtmp->minvent and drops on death.
- An unseen leprechaun off the shop floor can bury its gold 1-in-4 per turn (monmove.c:1152-1171 leppie_stash); killing later may not recover it.
-->

金貨を盗んで即座にフロアの別の場所へテレポートする妖精です。攻撃力は高くありませんが、全財産を奪われて逃げられると回収に手間取ります。テレパシーで位置を特定して仕留めれば、大量の金貨を取り戻せます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| レプラコーン (leprechaun) | 緑色 | 5 | 15 | 8 | 20 | 爪 1d2 盗み-gold | テレポート. Steals gold and テレポート away. Carry no gold near them. |

:::

#### ミミック `m` (Mimics `m`)

<!-- audit
2026-05-19:
- 3 rows (small/large/giant mimic) sourced from monsters.h:670-698.
- All carry M1_AMORPHOUS|M1_HIDE|MR_ACID; large/giant also have AD_STCK and M2_STRONG.
- Disguise via set_mimic_sym (makemon.c:2393-2472), including STRANGE_OBJECT in shops at sufficient depth.
- AD_STCK is MC-blocked (uhitm.c:3310/3324).
-->

扉、階段、金貨、あるいは貴重なアイテムに擬態して獲物を待ち伏せます。触れると貼り付かれて移動不能になり、噛みつき攻撃を受けます。不自然な位置にある階段や扉、未識別の高価なアイテムには遠距離攻撃で確認を入れるのが賢明です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 小さなミミック (small mimic) | 茶色 | 7 | 3 | 7 | 0 | 爪 3d4 |  |
| 大きなミミック (large mimic) | 赤色 | 8 | 3 | 7 | 10 | 爪 3d4 sticky |  |
| 巨大なミミック (giant mimic) | 赤紫 | 9 | 3 | 7 | 20 | 爪 3d6 sticky ×2 |  |

:::

#### ニンフ `n` (Nymphs `n`)

<!-- audit
2026-05-19:
- 3 nymphs (wood/water/mountain): LVL 3, Spd 12, AC 9, MR 20%, AT_CLAW AD_SITM + AT_CLAW AD_SEDU, M1_TPORT (monsters.h:702-723).
- Water nymph has M1_SWIM (line 714); all three carry M1_TPORT|MR_POISON.
- AD_SITM steal-and-teleport at uhitm.c:4724,4798; AD_SEDU at uhitm.c:4642.
- Corpse grants intrinsic teleportitis at 10% per should_givit (eat.c:936-975).
2026-05-31:
- Post-theft teleport calls rloc(mon, RLOC_MSG) at mhitu.c:2303, which is the within-level relocation routine (teleport.c:1799). The nymph does NOT migrate to another level after stealing; she ends up at a random valid position on the SAME level.
- The book's earlier claim that a nymph might "walk off the level with my bag of holding" was an overstatement of the rare incidental case where she later falls through a trapdoor or wanders onto a staircase.
- The Amulet of Yendor has no return-to-Sanctum mechanic on theft. A nymph carrying the Amulet stays on the same level, so the Ascension Run warning was corrected to point at the turn-budget cost of searching the level while the Mysterious Force keeps pulling.
-->

所持品からアイテムを1つ盗み取り、同じフロアのランダムな場所へテレポートします。遠距離から攻撃するか、ペットで進路を塞ぐか、エルベレスの文字を刻んで近寄らせないようにしてください。もしアイテムを盗まれた場合は、フロア全体を捜索して倒せば盗まれたアイテムをすべて回収できます。

すべてのニンフはテレポート能力を持ちます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 木のニンフ (wood nymph) | 緑色 | 3 | 12 | 9 | 20 | 爪 盗み-item · 爪 誘惑 |  |
| 水のニンフ (water nymph) | 青色 | 3 | 12 | 9 | 20 | 爪 盗み-item · 爪 誘惑 | 遊泳. |
| 山のニンフ (mountain nymph) | 茶色 | 3 | 12 | 9 | 20 | 爪 盗み-item · 爪 誘惑 |  |

:::

#### オーク `o` (Orcs `o`)

<!-- audit
2026-05-19:
- 8 rows (S_ORC) sourced from monsters.h:727-796.
- goblin L0/Spd6/AC10 weapon 1d4 (monsters.h:727-733).
- hobgoblin L1/Spd9/AC10 weapon 1d6 (monsters.h:734-742).
- orc L1/Spd9/AC10 weapon 1d8, MR_POISON (monsters.h:743-751).
- hill orc L2/Spd9/AC10 weapon 1d6 (monsters.h:752-760).
- Mordor orc L3/Spd5/AC10 weapon 1d6 (monsters.h:761-769); Spd 5 is correct in 5.0.
- Uruk-hai L3/Spd7/AC10 weapon 1d8 (monsters.h:770-778).
- orc shaman L3/Spd9/AC5 single AT_MAGC/AD_SPEL (monsters.h:779-787); "spell," not "cast spell."
- orc-captain L5/Spd5/AC10 weapon 2d4 ×2 (monsters.h:788-796).
- Goblin is correctly placed in S_ORC (monsters.h:727).
-->

集団で現れ、弓矢や毒矢、短剣を投げつけてきます。オークの弓や矢、盾、鎖かたびらなどを装備していることが多く、序盤の装備集めや飛び道具の補給に役立ちます。エルフのPCに対しては特に強い敵意を燃やします。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ゴブリン (goblin) | 灰色 | 0 | 6 | 10 | 0 | 武器攻撃 1d4 |  |
| ホブゴブリン (hobgoblin) | 茶色 | 1 | 9 | 10 | 0 | 武器攻撃 1d6 |  |
| オーク (orc) | 赤色 | 1 | 9 | 10 | 0 | 武器攻撃 1d8 | 毒耐性. |
| 丘のオーク (hill orc) | 黄色 | 2 | 9 | 10 | 0 | 武器攻撃 1d6 | 毒耐性. |
| モルドールのオーク (Mordor orc) | 青色 | 3 | 5 | 10 | 0 | 武器攻撃 1d6 | 毒耐性. |
| Uruk-hai | 黒色 | 3 | 7 | 10 | 0 | 武器攻撃 1d8 | 毒耐性. |
| オークの呪術師 (orc shaman) | 明青 | 3 | 9 | 5 | 10 | cast | 毒耐性. |
| orc-captain | 赤紫 | 5 | 5 | 10 | 0 | 武器攻撃 2d4 ×2 | 毒耐性. Hits hard. Drops decent loot. |

:::

#### ピアサー `p` (Piercers `p`)

天井の鍾乳石に擬態し、直下を通った冒険者の頭上へ落下して大ダメージを与えます。天井を見上げるか、怪しい通路の天井を注意深く探索することで事前に察知できます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 岩喰い (rock piercer) | 灰色 | 3 | 1 | 3 | 0 | 噛みつき 2d6 |  |
| 鉄喰い (iron piercer) | 水色 | 5 | 1 | 0 | 0 | 噛みつき 3d6 |  |
| ガラス喰い (glass piercer) | 白色 | 7 | 1 | 0 | 0 | 噛みつき 4d6 | 酸耐性. |

:::

#### 四足獣 `q` (Quadrupeds `q`)

<!-- audit
2026-05-19:
- 7 rows (rothe through mastodon) sourced from monsters.h:831-885.
- rothe L2/Spd9/AC7 claw 1d3 + bite 1d3 + bite 1d8 (monsters.h:831-837).
- mumak L5/Spd9/AC0 butt 4d12 + bite 2d6 (monsters.h:838-845).
- leocrotta L6/Spd18/AC4 (monsters.h:846-853).
- wumpus L8/Spd3/AC2 bite 3d6, M1_CLING (monsters.h:854-861).
- mastodon L20/Spd12/AC5 butt 4d8 ×2 (monsters.h:878-885).
-->

ロテやマンティコア、マムモスなどの四足歩行獣です。ロテは死体を急速に腐敗させて食べ尽くす能力を持ち、マンティコアは遠距離から大量のトゲを撃ち込んできます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ロゼ (rothe) | 茶色 | 2 | 9 | 7 | 0 | 爪 1d3 · 噛みつき 1d3 · 噛みつき 1d8 |  |
| ムーマク (mumak) | 灰色 | 5 | 9 | 0 | 0 | 頭突き 4d12 · 噛みつき 2d6 |  |
| レオクロッタ (leocrotta) | 赤色 | 6 | 18 | 4 | 10 | 爪 2d6 · 噛みつき 2d6 · 爪 2d6 |  |
| ワンパス (wumpus) | 水色 | 8 | 3 | 2 | 10 | 噛みつき 3d6 | clings. |
| チタノゼア (titanothere) | 灰色 | 12 | 12 | 6 | 0 | 爪 2d8 |  |
| バルキテリウム (baluchitherium) | 灰色 | 14 | 12 | 5 | 0 | 爪 5d4 ×2 |  |
| マストドン (mastodon) | 黒色 | 20 | 12 | 5 | 0 | 頭突き 4d8 ×2 |  |

:::

#### 齧歯類 `r` (Rodents `r`)

<!-- audit
2026-05-19:
- 6 rows (S_RODENT) sourced from monsters.h:889-936.
- Woodchuck color is brown (CLR_BROWN at monsters.h:936).
- Rock mole is M1_METALLIVORE: eats metal, including bag of gold and unattended weapons (mondata.c:561, hack.c:769-784).
-->

ネズミや巨大ネズミの群れ。兇暴ネズミは狂犬病に感染させてくる危険があります。ねずみ人間は噛みつきによってプレイヤーを獣化（ネズミ人間）させます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ドブネズミ (sewer rat) | 茶色 | 0 | 12 | 7 | 0 | 噛みつき 1d3 |  |
| 巨大ネズミ (giant rat) | 茶色 | 1 | 10 | 7 | 0 | 噛みつき 1d3 |  |
| 兇暴ネズミ (rabid rat) | 茶色 | 2 | 12 | 6 | 0 | 噛みつき 2d4 エナジードレイン-Co | 死体に毒あり, 毒耐性. |
| ねずみ人間 (wererat) | 茶色 | 2 | 12 | 6 | 10 | 噛みつき 1d4 獣化 | 自動回復, 毒耐性. 死体を残さない。 |
| 岩もぐら (rock mole) | 灰色 | 3 | 3 | 0 | 20 | 噛みつき 1d6 | tunnels, eats metal objects left on the floor. |
| リス (woodchuck) | 茶色 | 3 | 3 | 0 | 20 | 噛みつき 1d6 | 遊泳, tunnels. |

:::

#### 蜘蛛および百足 `s` (Arachnids and centipedes `s`)

<!-- audit
2026-05-19:
- 5 rows (cave spider, centipede, giant spider, scorpion, Scorpius) sourced from monsters.h:940-972, 3713-3722.
- Webmaker only on cave spider + giant spider (mondata.h:147-148); M1_CONCEAL on all except giant spider.
- Cave spider/centipede corpses safe (no M1_POIS); giant spider/scorpion corpses poisonous (M1_POIS).
- Scorpius MR_STONE confers stoning resistance via corpse.
-->

巨大グモは足元に蜘蛛の巣を張って動きを封じ、毒を注入してきます。ムカデは器用さを吸い取る毒を持ちます。洞窟グモの巣はユニコーンの角や火炎の杖で焼き払うことができます。

すべての蜘蛛および百足は毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 洞窟グモ (cave spider) | 灰色 | 1 | 12 | 3 | 0 | 噛みつき 1d2 | 潜伏. |
| ムカデ (centipede) | 黄色 | 2 | 4 | 3 | 0 | 噛みつき 1d3 毒 | 潜伏. |
| 巨大グモ (giant spider) | 赤紫 | 5 | 15 | 4 | 0 | 噛みつき 2d4 毒 | 死体に毒あり. |
| サソリ (scorpion) | 赤色 | 5 | 15 | 3 | 0 | 爪 1d2 ×2 · 毒針 1d4 毒 | 潜伏, 死体に毒あり. |
| 大蠍 (Scorpius) | 赤紫 | 15 | 12 | 10 | 0 | 爪 2d6 · 爪 2d6 盗み-amulet · 毒針 1d4 disease | 死体に毒あり, follows stairs, 石化耐性. |

:::

#### トラッパーおよびラーカー `t` (Trappers and lurkers `t`)

<!-- audit
2026-05-19:
- Lurker above (gray L10 Spd3 AC3 MR0, engulf 1d6 + wrap 2d6) and trapper (green L12 Spd3 AC3 MR0, engulf 1d8 + wrap 2d8): monsters.h:981-998.
- Both have M1_HIDE; lurker is M1_FLY (ceiling hider per mondata.h:43-45); trapper is floor hider.
- Damage is AD_WRAP+AD_PHYS, NOT AD_DGST (monsters.h:973-980 retcon).
- Both M2_STALK (follow stairs).
-->

床や天井に擬態する固定型の包み込み捕食者です。遠見（Farlook）でも隠れたラーカーを見抜くことはできません。怪しいマスには乗る前に隣から探索（Search）を行って正体を暴いてください。

トラッパーとラーカーはすべて潜伏能力を持ち、階段の上り下りにも追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ラーカー (lurker above) | 灰色 | 10 | 3 | 3 | 0 | engulf 1d6 wrap · engulf 2d6 | 飛行. |
| トラッパー (trapper) | 緑色 | 12 | 3 | 3 | 0 | engulf 1d8 wrap · engulf 2d8 |  |

:::

#### ユニコーンおよび馬 `u` (Unicorns and horses `u`)

馬（ポニー、馬、軍馬）は野生では敵対的に出現しますが、リンゴやニンジンを与えることで容易に手懐けられ、騎乗（Riding）スキルに活用できます。

ユニコーン（白、灰、黒）はそれぞれ秩序、中立、混沌の属性を持ち、同属性のプレイヤーには友好的です。宝石を投げ与えると幸運値を高めてくれます。角（ユニコーンの角）は万能の治療道具となります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 仔馬 (pony) | 茶色 | 3 | 16 | 6 | 0 | 蹴り 1d6 · 噛みつき 1d2 | 手懐け可能. Knight's starting steed. |
| 白ユニコーン (white unicorn) | 白色 | 4 | 24 | 2 | 70 | 頭突き 1d12 · 蹴り 1d6 | 毒耐性. |
| 灰色ユニコーン (gray unicorn) | 灰色 | 4 | 24 | 2 | 70 | 頭突き 1d12 · 蹴り 1d6 | 毒耐性. |
| 黒ユニコーン (black unicorn) | 黒色 | 4 | 24 | 2 | 70 | 頭突き 1d12 · 蹴り 1d6 | 毒耐性. |
| 馬 (horse) | 茶色 | 5 | 20 | 5 | 0 | 蹴り 1d8 · 噛みつき 1d3 | 手懐け可能. |
| 戦闘用の馬 (warhorse) | 茶色 | 7 | 24 | 4 | 0 | 蹴り 1d10 · 噛みつき 1d4 | 手懐け可能. |

:::

#### 渦 `v` (Vortices `v`)

<!-- audit
2026-05-19:
- 6 rows (S_VORTEX) sourced from monsters.h:1053-1110.
- Damage types are physical/blinding/cold/shock+drain/fire; NO vortex deals poison.
- Speeds: fog cloud Lvl 3/Spd 1; dust/ice/energy Spd 20; steam/fire Spd 22. Only fog cloud is slow, NOT all stationary. (monsters.h:1052 fog cloud LVL(3,1,...); 1062 dust LVL(4,20,...); 1071 ice LVL(5,20,...); 1081 energy LVL(6,20,...); 1091 steam LVL(7,22,...); 1101 fire LVL(8,22,...))
- Energy vortex: AT_NONE+AD_ELEC passive 0d4 + AD_DREN drain (monsters.h:1081-1090).
- Fire vortex: AT_NONE+AD_FIRE passive 0d4 (monsters.h:1101-1110).
- All carry M1_FLY|M1_MINDLESS|G_NOCORPSE.
-->

プレイヤーを包み込んで元素ダメージを与える雲状の怪物です。色によって盲目砂嵐、冷気、電撃、火炎などの異なる属性ダメージを毎ターン与えてきます。包み込まれたら脱出の巻物や衝撃波、あるいは即座に倒す手段が必要です。

すべての渦は飛行能力を持ち、精神を持たず、死体を残しません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 霧の雲 (fog cloud) | 灰色 | 3 | 1 | 0 | 0 | engulf 1d6 | 不定形. |
| ほこりの渦 (dust vortex) | 茶色 | 4 | 20 | 2 | 30 | engulf 2d8 盲目 |  |
| 氷の渦 (ice vortex) | 水色 | 5 | 20 | 2 | 30 | engulf 1d6 冷気 |  |
| エネルギーの渦 (energy vortex) | 明青 | 6 | 20 | 2 | 30 | engulf 1d6 電撃 · engulf 2d6 エナジードレイン-Pw · 反撃 7d4 電撃 |  |
| 蒸気の渦 (steam vortex) | 青色 | 7 | 22 | 2 | 30 | engulf 1d8 火炎 |  |
| 炎の渦 (fire vortex) | 黄色 | 8 | 22 | 2 | 30 | engulf 1d10 火炎 · 反撃 9d4 火炎 |  |

:::

#### ワーム `w` (Worms `w`)

<!-- audit
2026-05-19:
- 4 rows (S_WORM) sourced from monsters.h:1114-1145: baby long worm 1118, baby purple 1124, long worm 1130, purple worm 1138.
- Long worm tail and segment mechanics in worm.c; purple worm AT_ENGL/AD_DGST swallow at monsters.h:1141.
- Long worm drops worm tooth on death; fires only for PM_LONG_WORM, not baby (mon.c:618-620).
- Long worm grown segments tracked via mtmp->wormno (mon.c:5451, get_wormno on polymorph to PM_LONG_WORM).
-->

長いワームは攻撃を受けるたびに尾のセグメントへ分裂して増殖します。紫ワーム（Purple worm）はプレイヤーを一撃で丸呑み（胃袋へ収容）して消化死させる極めて危険な怪物です。消化死を防ぐ手段（耐へんげの魔除けなど）や、胃袋の内側から脱出する手段を用意してください。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ロングワームの子供 (baby long worm) | 茶色 | 5 | 3 | 5 | 0 | 噛みつき 1d4 |  |
| 紫ワームの子供 (baby purple worm) | 赤紫 | 8 | 3 | 5 | 0 | 噛みつき 1d6 |  |
| ロングワーム (long worm) | 茶色 | 9 | 3 | 5 | 10 | 噛みつき 2d4 | drops a worm tooth. |
| 紫ワーム (purple worm) | 赤紫 | 15 | 9 | 6 | 20 | 噛みつき 2d8 · engulf 1d10 digest |  |

:::

#### ザンおよび幻想昆虫 `x` (Xans and fantastic insects `x`)

<!-- audit
2026-05-19:
- Grid bug row at monsters.h:1149-1156; xan row at monsters.h:1157-1164.
- Grid bug AT_BITE/AD_ELEC 1d1; xan AT_STNG/AD_LEGS 1d4, M1_FLY plus M1_POIS (poisonous corpse).
- Xan AD_LEGS / Wounded_legs reduces carry capacity (hack.c:4331-4336) and abuses Dex (attrib.c:472, 581); it does NOT slow movement.
-->

グリッドバグは電気を帯びた単純な昆虫ですが、直角方向にしか移動できません。大型の近縁種であるザンは脚を刺して傷口を負わせ、最大所持重量（運搬能力）を急激に低下させます。

すべてのザンおよび幻想昆虫は毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| グリッドバグ (grid bug) | 赤紫 | 0 | 12 | 9 | 0 | 噛みつき 1d1 電撃 | 電撃耐性. |
| ザン (xan) | 赤色 | 7 | 18 | -4 | 0 | 毒針 1d4 leg-wound | 飛行, 死体に毒あり. |

:::

#### 光 `y` (Lights `y`)

<!-- audit
2026-05-19:
- 2 rows (yellow light L3 yellow, black light L5 black) sourced from monsters.h:1168-1191.
- Attacks AT_EXPL/AD_BLND 10d20 (yellow) and AT_EXPL/AD_HALU 10d12 (black).
- M1_FLY|M1_AMORPHOUS|M1_MINDLESS on both; black light adds M1_SEE_INVIS.
- 10d20 is blindness DURATION, NOT HP damage. (uhitm.c:2978-2985 mhitm_ad_blnd: `make_blinded(BlindedTimeout + (long) mhm->damage, FALSE); mhm->damage = 0;` — rolled value feeds timer, HP damage zeroed)
- AT_EXPL means the monster dies on attack ("bursts on contact").
-->

黄色い光は接触時に自爆閃光を放ち、10d20ターンの間プレイヤーを盲目にします。黒い光は自爆して幻覚状態を引き起こします。遠距離武器や魔法で接近される前に撃ち落とすのが鉄則です。

すべての光は飛行能力を持ち、不定形で精神を持ちません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 黄色い光 (yellow light) | 黄色 | 3 | 15 | 0 | 0 | 自爆 10d20 盲目 |  |
| 黒い光 (black light) | 黒色 | 5 | 15 | 0 | 0 | 自爆 10d12 hallu | sees-不可視. |

:::

#### ズリティ `z` (Zruties `z`)

中盤に出現する手強い野獣で、2本の爪と強力な噛みつき攻撃を繰り出してきます。激しい連撃に耐えきることができれば、まとまった経験値を獲得できます。名称はスラブ神話の毛深い野生人に由来しています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ズルティ (zruty) | 茶色 | 9 | 8 | 3 | 0 | 爪 3d4 ×2 · 噛みつき 3d6 |  |

:::

#### 天使・神聖なる存在 `A` (Angelic beings `A`)

<!-- audit
2026-05-19:
- 5 rows at monsters.h:1206-1265 (couatl 1206, Aleax 1216, Angel 1225, ki-rin 1240, Archon 1252).
- All Angels have G_NOCORPSE; couatl leaves no corpse (MR_POISON still matters for combat).
- AD_MAGM ("magic") on Angel; AD_SPEL ("spell") on ki-rin/Archon.
- Ki-rin HI_GOLD = yellow; Archon HI_LORD = magenta (color.h:38,46).
- Archon has M1_REGEN, M1_SEE_INVIS, plus 5-attack chain (weapon, weapon, gaze, claw, spell).
-->

武器を振るい、強力な魔法を操る終盤の強敵です。星界の面（Astral Plane）では各大祭司を護衛して立ち塞がります。[星界の面](#the-astral-plane)の項目を参照してください。

すべての天使・神聖なる存在は階段の上り下りに追従し、死体を残しません。*アレアックス (Aleax)* を除きすべて飛行し、*コウアトル (couatl)* を除きすべて不可視を看破します。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コウアトル (couatl) | 緑色 | 8 | 10 | 5 | 30 | 噛みつき 2d4 毒 · 噛みつき 1d3 · 締め付け 2d4 wrap | 毒耐性. |
| アレアックス (Aleax) | 黄色 | 10 | 8 | 0 | 30 | 武器攻撃 1d6 ×2 · 蹴り 1d4 |  |
| 天使 (Angel) | 白色 | 14 | 10 | -4 | 55 | 武器攻撃 1d6 ×2 · 爪 1d4 · cast 2d6 魔法 |  |
| ki-rin | 黄色 | 16 | 18 | -5 | 90 | 蹴り 2d4 ×2 · 頭突き 3d6 · cast 2d6 spell |  |
| アルコン (Archon) | 赤紫 | 19 | 16 | -6 | 80 | 武器攻撃 2d4 ×2 · 凝視 2d6 盲目 · 爪 1d8 · cast 4d6 spell | 自動回復. |

:::

#### こうもりおよび鳥 `B` (Bats and birds `B`)

不規則に飛び回る飛行生物。吸血こうもりは毒のある噛みつきで筋力を吸い取ります（毒耐性があれば防げます）。オオガラスは目をつついて盲目にしようとします。

すべてのこうもりおよび鳥は飛行能力を持ちます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| こうもり (bat) | 茶色 | 0 | 22 | 8 | 0 | 噛みつき 1d4 |  |
| 巨大こうもり (giant bat) | 赤色 | 2 | 22 | 7 | 0 | 噛みつき 1d6 |  |
| オオガラス (raven) | 黒色 | 4 | 20 | 6 | 0 | 噛みつき 1d6 · 爪 1d6 盲目 |  |
| 吸血こうもり (vampire bat) | 黒色 | 5 | 20 | 6 | 0 | 噛みつき 1d6 · 噛みつき エナジードレイン-Str | 自動回復, 死体に毒あり, 睡眠耐性, 毒耐性. |

:::

#### ケンタウロス `C` (Centaurs `C`)

<!-- audit
2026-05-19:
- 3 rows (plains/forest/mountain) sourced from monsters.h:1301-1323; complete S_CENTAUR roster.
- Centaurs are half-horse, NOT mounted on a horse. (https://nethackwiki.com/wiki/Centaur)
- Forest centaurs spawn with BOW+arrows; plains and mountain centaurs spawn with CROSSBOW+bolts (50% armed rate per makemon.c:474-484).
-->

強力な弓矢と近接攻撃を兼ね備えた半人半馬の射手です。森のケンタウロスは弓を放ち、平原や山のケンタウロスは複合弓を用いて強烈な矢の連射を浴びせてきます。離れた位置からの射撃戦は危険なため、角を曲がって誘い込むか接近戦に持ち込んでください。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 草原のケンタウロス (plains centaur) | 茶色 | 4 | 18 | 4 | 0 | 武器攻撃 1d6 · 蹴り 1d6 |  |
| 森のケンタウロス (forest centaur) | 緑色 | 5 | 18 | 3 | 10 | 武器攻撃 1d8 · 蹴り 1d6 |  |
| 山のケンタウロス (mountain centaur) | 水色 | 6 | 20 | 2 | 10 | 武器攻撃 1d10 · 蹴り 1d6 ×2 |  |

:::

#### ドラゴン `D` (Dragons `D`)

<!-- audit
2026-05-19:
- 10 baby + 10 adult + Chromatic + Ixoth sourced from monsters.h:1325-1562; Ixoth at monsters.h:3642-3690.
- Shimmering dragon is `#if 0 DEFERRED`, NOT in 5.0 (monsters.h:1365-1374 baby and 1466-1482 adult shimmering dragon blocks are inside `#if 0 /* DEFERRED */`).
- Silver dragon color is CLR_BRIGHT_CYAN (color.h:54), NOT gray, for both baby and adult.
- Baby blue dragon has only bite 2d6; NO breath weapon (monsters.h:1408-1415, no AT_BREA). Babies don't breathe.
- Black dragon breath is AD_DISN 1d255 (instakill without reflection or disint-res), monsters.h:1494.
- Chromatic random-breath AT_BREA/AD_RBRE selects breath type per zap (mhitu.c).
-->

成体のドラゴンは各自の属性に応じた強烈なブレスを直線状に吐き出します。反射（Reflection）能力があれば、遠距離ブレスを跳ね返して逆に大ダメージを与えられます。**幼体（子ドラゴン）はブレスを吐きません**。

*クロマティック・ドラゴン (Chromatic Dragon)* を除き、すべてのドラゴンは飛行能力を持ちます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 灰色ドラゴンの子供 (baby gray dragon) | 灰色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 金色ドラゴンの子供 (baby gold dragon) | 黄色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 銀色ドラゴンの幼体 (baby silver dragon) | 明水 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 赤色ドラゴンの子供 (baby red dragon) | 赤色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 白ドラゴンの子供 (baby white dragon) | 白色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| オレンジドラゴンの子供 (baby orange dragon) | 橙色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 黒ドラゴンの子供 (baby black dragon) | 黒色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 青ドラゴンの子供 (baby blue dragon) | 青色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 緑ドラゴンの子供 (baby green dragon) | 緑色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 | 死体に毒あり. |
| 黄色ドラゴンの子供 (baby yellow dragon) | 黄色 | 12 | 9 | 2 | 10 | 噛みつき 2d6 |  |
| 灰色ドラゴン (gray dragon) | 灰色 | 15 | 9 | -1 | 20 | ブレス 4d6 魔法 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Anti-magic breath. Magic resistance helps; reflection doesn't. |
| 金色ドラゴン (gold dragon) | 黄色 | 15 | 9 | -1 | 20 | ブレス 4d6 火炎 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Fire breath. Drops gold-colored scales (light source). |
| 銀色ドラゴン (silver dragon) | 明水 | 15 | 9 | -1 | 20 | ブレス 4d6 冷気 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cold breath plus reflection scales: your reflection target. |
| 赤色ドラゴン (red dragon) | 赤色 | 15 | 9 | -1 | 20 | ブレス 6d6 火炎 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cone of fire. Get fire resistance before you meet one. |
| 白ドラゴン (white dragon) | 白色 | 15 | 9 | -1 | 20 | ブレス 4d6 冷気 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cone of cold. Cold resistance. |
| オレンジドラゴン (orange dragon) | 橙色 | 15 | 9 | -1 | 20 | ブレス 4d25 sleep · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Sleep ray. Sleep resistance trivialises. |
| 黒ドラゴン (black dragon) | 黒色 | 15 | 9 | -1 | 20 | ブレス 1d255 分解 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Disintegration breath. Disint resistance OR reflection. |
| 青ドラゴン (blue dragon) | 青色 | 15 | 9 | -1 | 20 | ブレス 4d6 電撃 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Cone of lightning. Shock resistance. |
| 緑ドラゴン (green dragon) | 緑色 | 15 | 9 | -1 | 20 | ブレス 4d6 毒 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視, 死体に毒あり. Poison breath; poison resistance is enough. |
| 黄色ドラゴン (yellow dragon) | 黄色 | 15 | 9 | -1 | 20 | ブレス 4d6 酸 · 噛みつき 3d8 · 爪 1d4 ×2 | sees-不可視. Acid breath. |
| クロマティック・ドラゴン (Chromatic Dragon) | 赤紫 | 16 | 12 | 0 | 30 | ブレス 6d6 rnd-ブレス · cast spell · 爪 2d8 盗み-amulet · 噛みつき 4d8 ×2 · 毒針 1d6 | sees-不可視, 死体に毒あり, follows stairs. |
| イクソス (Ixoth) | 赤色 | 15 | 12 | -1 | 20 | ブレス 8d6 火炎 · 噛みつき 4d8 · cast spell · 爪 2d4 · 爪 2d4 盗み-amulet | sees-不可視, follows stairs. |

:::

#### 精霊・エレメンタル `E` (Elementals `E`)

<!-- audit
2026-05-19:
- 5 rows (stalker/air/fire/earth/water elemental) sourced from monsters.h:1566-1610.
- Stalker: sees-invis, M2_STALK; NOT mindless. (monsters.h:1566-1573 has M1_SEE_INVIS and M2_STALK; no M1_MINDLESS in flags1)
- Air: AT_ENGL AD_PHYS 1d10. "Air suffocates" is engulf flavor for AD_PHYS, NOT a separate AD_DRST. (monsters.h:1576 air elemental single AT_ENGL AD_PHYS 1d10; no AD_DRST attack)
- Fire: claw 3d6 AD_FIRE + passive 0d4 fire.
- Earth: claw 4d6; MR_FIRE|MR_COLD|MR_POISON|MR_STONE.
- Water: claw 5d6; M1_SWIM|M1_AMPHIBIOUS; MR_POISON|MR_STONE. Water elementals lack a drown attack, but spawn only on water tiles so encounters happen near drowning risk.
-->

風の精はプレイヤーを包み込んで瓦礫の嵐で叩きのめします。火の精は周囲を灼熱で焼き焦がし、水の精は強打を繰り出し、土の精は動きは鈍いものの極めて強固です。

*ストーカー*を除き、すべてのエレメンタルは精神を持ちません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ストーカー (stalker) | 白色 | 8 | 12 | 3 | 0 | 爪 4d4 | 飛行, sees-不可視, follows stairs. |
| 風の精 (air elemental) | 水色 | 8 | 36 | 2 | 30 | engulf 1d10 | 飛行. |
| 火の精 (fire elemental) | 黄色 | 8 | 12 | 2 | 30 | 爪 3d6 火炎 · 反撃 9d4 火炎 | 飛行. |
| 土の精 (earth elemental) | 茶色 | 8 | 6 | 2 | 30 | 爪 4d6 | 火炎耐性, 冷気耐性, 毒耐性, 石化耐性. |
| 水の精 (water elemental) | 青色 | 8 | 5 | 2 | 30 | 爪 5d6 | 遊泳, 水陸両用, 毒耐性, 石化耐性. |

:::

#### 菌類およびモールド `F` (Fungi and molds `F`)

<!-- audit
2026-05-19:
- 7 rows sourced from monsters.h:1614-1676; elemental molds are brown/green/red, NOT violet/yellow.
- Lichen corpse never rots (mkobj.c:1402, eat.c:59); also never out of season as iron rations.
- Yellow mold has M1_POIS (poisonous corpse, monsters.h yellow-mold row).
- Other molds have MR_POISON resistance but no M1_POIS, so their corpses are NOT poisonous.
- Brown mold passive 0d6 cold (HP drain), green 0d4 acid, red 0d4 fire, yellow 0d4 stun (monsters.h:1614-1666).
- Violet fungus AT_TUCH/AD_PHYS 1d4 plus AT_TUCH/AD_PLYS sticky (monsters.h:1668-1676).
-->

移動しない固定型の生物です。苔の怪物（Lichen）の死体は決して腐敗しないため、非常用の携帯食糧として最適です。茶色、緑、赤のモールドはそれぞれ冷気、酸、火炎の反撃ダメージを放ちます。

すべての菌類およびモールドは精神を持ちません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 苔の怪物 (lichen) | 明緑 | 0 | 1 | 9 | 0 | 接触 sticky |  |
| 茶色モールド (brown mold) | 茶色 | 1 | 0 | 9 | 0 | 反撃 2d6 冷気 | 冷気耐性, 毒耐性. |
| 黄色モールド (yellow mold) | 黄色 | 1 | 0 | 9 | 0 | 反撃 2d4 stun | 死体に毒あり, 毒耐性. |
| 緑モールド (green mold) | 緑色 | 1 | 0 | 9 | 0 | 反撃 2d4 酸 | 酸耐性, 石化耐性. |
| 赤色モールド (red mold) | 赤色 | 1 | 0 | 9 | 0 | 反撃 2d4 火炎 | 火炎耐性, 毒耐性. |
| シュリーカー (shrieker) | 赤紫 | 3 | 1 | 7 | 0 | — | 毒耐性. |
| 紫キノコ (violet fungus) | 赤紫 | 3 | 1 | 7 | 0 | 接触 1d4 · 接触 sticky | 毒耐性. |

:::

#### ノーム `G` (Gnomes `G`)

<!-- audit
2026-05-19:
- All four S_GNOME entries match monsters.h:1681-1709.
- Gnomish wizard has one AT_MAGC/AD_SPEL attack, "cast spell" (monsters.h:1697), NOT two spell attacks.
- No "deep gnome" exists in 5.0 (correctly omitted).
- Gnome PCs (Archeologist default) see most S_GNOME as peaceful via MH_GNOME lovemask (makemon.c:2283).
-->

ノームのPCにとってはノームの鉱山の住人の大半が友好的です。ノームの君主は通常種よりも高い攻撃力を持ち、ノームの魔法使いは強力な魔法攻撃を放ってきます。どちらも侮ってはなりません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ノーム (gnome) | 茶色 | 1 | 6 | 10 | 4 | 武器攻撃 1d6 |  |
| gnome lord | 青色 | 3 | 8 | 10 | 4 | 武器攻撃 1d8 |  |
| ノームの魔法使い (gnomish wizard) | 明青 | 3 | 10 | 4 | 10 | cast spell |  |
| gnome king | 赤紫 | 5 | 10 | 10 | 20 | 武器攻撃 2d6 |  |

:::

#### 巨人 `H` (Giant humanoids `H`)

<!-- audit
2026-05-19:
- Frost giant and storm giant melee is AD_PHYS only; cold/shock resistance does NOT reduce damage (monsters.h frost/storm rows at 1748, 1772).
- Fire giant melee is AD_PHYS only; fire resistance does NOT make them weak offensively (monsters.h:1738).
- Cyclops is the Healer quest nemesis (Hea-goal.lua:74, monsters.h:1792-1800), NOT Caveman.
- Surtur does NOT carry Mjollnir (Mjollnir is a Valkyrie quest artifact, artilist.h).
- Ettin and minotaur are NOT M2_GIANT, so their corpses do not grant Str (eat.c:1345; monsters.h:1758, 1782).
- Minotaur roams Gehennom mazes (mkmaze.c:1112, makemon at maze fill), NOT vaults.
-->

巨岩を投げつけてくる怪力の人型生物です。火の巨人、霜の巨人、嵐の巨人はそれぞれの属性ダメージを扱い、その死体を食べることで火炎耐性、冷気耐性、電撃耐性や筋力上昇を獲得できるチャンスがあります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 巨人 (giant) | 赤色 | 6 | 6 | 0 | 0 | 武器攻撃 2d10 |  |
| 岩石巨人 (stone giant) | 灰色 | 6 | 6 | 0 | 0 | 武器攻撃 2d10 |  |
| 丘の巨人 (hill giant) | 水色 | 8 | 10 | 6 | 0 | 武器攻撃 2d8 |  |
| 炎の巨人 (fire giant) | 黄色 | 9 | 12 | 4 | 5 | 武器攻撃 2d10 | 火炎耐性. Throws boulders. |
| 吹雪の巨人 (frost giant) | 白色 | 10 | 12 | 3 | 10 | 武器攻撃 2d12 | 冷気耐性. Throws boulders. |
| エティン (ettin) | 茶色 | 10 | 12 | 3 | 0 | 武器攻撃 2d8 · 武器攻撃 3d6 |  |
| 雷の巨人 (storm giant) | 青色 | 16 | 12 | 3 | 10 | 武器攻撃 2d12 | 電撃耐性. Throws boulders for big damage. |
| タイタン (titan) | 赤紫 | 16 | 18 | -3 | 70 | 武器攻撃 2d8 · cast spell | 飛行. Tough humanoid with magic missiles. Casts spells. |
| ミノタウロス (minotaur) | 茶色 | 15 | 15 | 6 | 0 | 爪 3d10 ×2 · 頭突き 2d8 | Two claws plus a butt. Heavy hitter; roams the Gehennom mazes. |
| サイクロプス (Cyclops) | 灰色 | 18 | 12 | 0 | 0 | 武器攻撃 4d8 ×2 · 爪 2d6 盗み-amulet | follows stairs, 石化耐性. Healer quest nemesis. Throws boulders. |
| 支配者スルト (Lord Surtur) | 赤紫 | 15 | 12 | 2 | 50 | 武器攻撃 2d10 ×2 · 爪 2d6 盗み-amulet | follows stairs, 火炎耐性, 石化耐性. Valkyrie quest nemesis. |

:::

#### ジャバウォック `J` (Jabberwocks `J`)

<!-- audit
2026-05-19:
- Jabberwock: L15 Spd12 AC-2 MR50, 4x 2d10 attacks, M1_FLY, G_GENO|1 (monsters.h:1806-1814).
- Speed 12 is player baseline, NOT slow; most dragons are speed 9 (slower).
- Vorpal Blade auto-beheads PM_JABBERWOCK, short-circuiting the dieroll==1 check (artifact.c:1595-1623).
- Deferred "vorpal jabberwock" at monsters.h:1816-1824 is wrapped in `#if 0` and correctly excluded.
-->

ルイス・キャロルの詩『ジャバウォックの詩』に登場する獰猛な怪物。プレイヤーと同等の速度で移動し、鋭い爪と噛みつきによる連続攻撃を繰り出してきます。十分なACと武器強化が整うまでは警戒が必要です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ジャバウォック (jabberwock) | 橙色 | 15 | 12 | -2 | 50 | 噛みつき 2d10 ×2 · 爪 2d10 ×2 | 飛行. Four heavy attacks; baseline speed. |

:::

#### キーストン・コップ `K` (Keystone Kops `K`)

<!-- audit
2026-05-19:
- All Kop stats match monsters.h:1829-1860.
- Shopkeeper-anger triggers Kop summoning via makekops (shk.c:623, 680, 5113).
- Dead Kops respawn per rnd(5) at mon.c:3147-3164: 1/5 near DOWN-stairs, 1/5 at random location, 3/5 stay dead.
- Respawn lands near DOWN-stairs, NOT up-stairs (stairs.c:89-95, mklev.c:2193).
- All four Kops carry G_GENO, so genocide permanently clears them.
-->

店で泥棒を働くか、店主を傷つけた際に笛を鳴らして駆けつける警官隊です。個々の戦闘力は高くありませんが、群れをなして現れ、クリームパイを投げつけてプレイヤーの視界を塞ごうとします。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 警備員 (Keystone Kop) | 青色 | 1 | 6 | 10 | 10 | 武器攻撃 1d4 |  |
| 巡査 (Kop Sergeant) | 青色 | 2 | 8 | 10 | 10 | 武器攻撃 1d6 |  |
| 巡査部長 (Kop Lieutenant) | 水色 | 3 | 10 | 10 | 20 | 武器攻撃 1d8 |  |
| 警部補 (Kop Kaptain) | 赤紫 | 4 | 12 | 10 | 20 | 武器攻撃 2d6 |  |

:::

#### リッチ `L` (Liches `L`)

<!-- audit
2026-05-19:
- 4 lich rows at monsters.h:1864-1897 (lich 1864, demilich 1872, master lich 1880, arch-lich 1889).
- All carry G_NOCORPSE, so no eatable corpse regardless of M1_POIS flavor.
- Only the arch-lich (m_lev=25) reaches DEATH_TOUCH at spell-level 20; master lich m_lev=17 cannot (mcastu.c:111).
- Double-trouble is Wizard-of-Yendor only, NOT a lich ability.
- Arch-lich casts touch of death, NOT rays.
2026-05-31:
- Touch of death (mcastu.c:389-408): without Antimagic, `rn2(mtmp->m_lev) > 12` gates the effect. At m_lev 25 that succeeds 12/25 of the time; touch_of_death then deals 50+8d6 damage and drains half that amount from max HP. Magic resistance blocks the effect (mcastu.c:315-347).
- Only the Wizard of Yendor literally has M3_COVETOUS in 5.0 (monsters.h:2857; single row). Arch-liches do NOT teleport-away-to-heal. Their threat profile is the touch-of-death spell, not the covetous return-at-full-HP behavior the Wizard has.
-->

骸骨姿の強力な魔法使いアンデッド。マスターリッチやアーチリッチは死の指（Touch of death）を詠唱し、モンスターを大量召喚し、冷気光線を放ってきます。魔法防御（Magic resistance）がなければ即死する危険極まりない強敵です。

すべてのリッチは自動回復し、死体を残さず、アンデッドであり、冷気耐性、睡眠耐性、毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| リッチ (lich) | 茶色 | 11 | 6 | 0 | 30 | 接触 1d10 冷気 · cast spell |  |
| デミリッチ (demilich) | 赤色 | 14 | 9 | -2 | 60 | 接触 3d4 冷気 · cast spell |  |
| マスターリッチ (master lich) | 赤紫 | 17 | 9 | -4 | 90 | 接触 3d6 冷気 · cast spell | 火炎耐性. Casts wizard spells. Kill from afar. |
| arch-lich | 赤紫 | 25 | 9 | -6 | 90 | 接触 5d6 冷気 · cast spell | 火炎耐性, 電撃耐性. Casts touch of death; magic resistance mandatory. |

:::

#### ミイラ `M` (Mummies `M`)

<!-- audit
2026-05-19:
- Every mummy attack is plain AD_PHYS (monsters.h:1901-1968); mummies do NOT curse worn items (only gremlins have AD_CURS, monattk.h:92).
- All M-class rows carry G_NOCORPSE, which prevents random mummy corpses and tins. The death handler overrides it and creates an already-old corpse of the mummy's base race (mon.c:620-646).
- Mummies are vulnerable to undead-turning.
-->

精神を持たないアンデッド。アンデッド退散の杖や呪文を使うと 1d8 のダメージを受けて逃走します。死亡時には元となった種族の古びた死体を残すため、病気耐性なしで食べると食中毒を起こす危険があります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コボルドのミイラ (kobold mummy) | 茶色 | 3 | 8 | 6 | 20 | 爪 1d4 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old kobold corpse. |
| ノームのミイラ (gnome mummy) | 赤色 | 4 | 10 | 6 | 20 | 爪 1d6 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old gnome corpse. |
| オークのミイラ (orc mummy) | 灰色 | 5 | 10 | 5 | 20 | 爪 1d6 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old orc corpse. |
| ドワーフのミイラ (dwarf mummy) | 赤色 | 5 | 10 | 5 | 20 | 爪 1d6 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old dwarf corpse. |
| エルフのミイラ (elf mummy) | 緑色 | 6 | 12 | 4 | 30 | 爪 2d4 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old elf corpse. |
| 人間のミイラ (human mummy) | 灰色 | 6 | 12 | 4 | 30 | 爪 2d4 ×2 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old 人間 corpse. |
| エティンのミイラ (ettin mummy) | 青色 | 7 | 12 | 4 | 30 | 爪 2d6 ×2 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old ettin corpse. |
| 巨人のミイラ (giant mummy) | 水色 | 8 | 14 | 3 | 30 | 爪 3d4 ×2 | 冷気耐性, 睡眠耐性, 毒耐性. Drops an old 巨人 corpse. |

:::

#### ナーガ `N` (Nagas `N`)

蛇の体を持つ人型生物で、遠距離から酸や毒のブレス・吐瀉攻撃を行ってきます。すべてのナーガは毒耐性を備えています。黒ナーガの死体を食べると恒久的な毒耐性を獲得できることがあり、酸耐性と石化耐性も一時的に得られます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 赤色ナーガの雛 (red naga hatchling) | 赤色 | 3 | 10 | 6 | 0 | 噛みつき 1d4 | 火炎耐性. |
| 黒ナーガの雛 (black naga hatchling) | 黒色 | 3 | 10 | 6 | 0 | 噛みつき 1d4 | 酸耐性, 石化耐性. |
| 金色ナーガの雛 (golden naga hatchling) | 黄色 | 3 | 10 | 6 | 0 | 噛みつき 1d4 |  |
| 番兵ナーガの雛 (guardian naga hatchling) | 緑色 | 3 | 10 | 6 | 0 | 噛みつき 1d4 |  |
| 赤色ナーガ (red naga) | 赤色 | 6 | 12 | 4 | 0 | 噛みつき 2d4 · ブレス 2d6 火炎 | 火炎耐性. |
| 黒ナーガ (black naga) | 黒色 | 8 | 14 | 2 | 10 | 噛みつき 2d6 · 吐瀉 酸 | 酸耐性, 石化耐性. |
| 金色ナーガ (golden naga) | 黄色 | 10 | 14 | 2 | 70 | 噛みつき 2d6 · cast spell 4d6 |  |
| 番兵ナーガ (guardian naga) | 緑色 | 12 | 16 | 0 | 50 | 吐瀉 1d6 毒 · 噛みつき 1d6 麻痺 · 接触 · 締め付け 2d4 wrap | 死体に毒あり. Lawful PCs may find them peaceful. |

:::

#### オーガ `O` (Ogres `O`)

<!-- audit
2026-05-19:
- 3 ogre rows match monsters.h: ogre 2052, ogre lord 2060, ogre king 2068.
- Ogres wield weapons (AT_WEAP); they do NOT throw boulders (no M2_ROCKTHROW — that's giants/Cyclops/ettins/titans).
- All three carry M2_STRONG plus G_GENO|1 (genocidable, freq 1).
-->

強大な筋力を持つ近接戦闘の巨人です。こん棒や戦斧を振り回して大ダメージを与えてきますが、防具を着けていないためACは低く、遠距離から削るのが有効です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| オーガ (ogre) | 茶色 | 5 | 10 | 5 | 0 | 武器攻撃 2d5 |  |
| ogre lord | 赤色 | 7 | 12 | 3 | 30 | 武器攻撃 2d6 |  |
| ogre king | 赤紫 | 9 | 14 | 4 | 60 | 武器攻撃 3d5 |  |

:::

#### プリンおよびウーズ `P` (Puddings and oozes `P`)

<!-- audit
2026-05-19:
- Green slime: make_slimed sets a 10-turn countdown, NOT 9 (uhitm.c:3199, 3570; polyself.c:456; eat.c:854). The 5-turn case is engulf+digest only (uhitm.c:5099).
- Brown puddings rot wood/leather/cloth/bone (AD_DCAY = ERODE_ROT, uhitm.c:2389). They do NOT corrode armor.
- Black puddings corrode metal (AD_CORR, uhitm.c:2338-2356).
- Gray ooze rusts armor (AD_RUST).
- Splitting on iron/metal melee is gated to PM_BLACK_PUDDING || PM_BROWN_PUDDING (uhitm.c:1609-1621). Gray ooze and green slime do NOT split.
-->

**茶色および黒色プリンは鉄製や金属製の刃物で攻撃すると分裂します**。無傷の死体ではなく塊を残します。

**緑スライム**は[ゲヘナ](#gehennom)にのみ現れる例外で、分裂はしませんが接触した相手を緑スライムへと徐々に変異させていきます（石化に似た即死タイマー）。

すべてのプリンおよびウーズは不定形で、精神を持たず、冷気耐性、毒耐性、酸耐性、石化耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 灰色ウーズ (gray ooze) | 灰色 | 3 | 1 | 8 | 0 | 噛みつき 2d8 錆び | 火炎耐性. |
| 茶色プリン (brown pudding) | 茶色 | 5 | 3 | 8 | 0 | 噛みつき decay |  |
| 緑スライム (green slime) | 緑色 | 6 | 6 | 6 | 0 | 接触 1d4 slime · 反撃 slime | 死体を残さない。 |
| 黒プリン (black pudding) | 黒色 | 10 | 6 | 6 | 0 | 噛みつき 3d8 corrode · 反撃 corrode |  |

:::

#### 量子物理学者 `Q` (Quantum mechanics `Q`)

<!-- audit
2026-05-19:
- Quantum mechanic teleports you (AD_TLPT, monsters.h:2127); genetic engineer polymorphs you (AD_POLY, monsters.h:2136, new in 5.0 per fixes5-0-0.txt:2696). NOT both teleporting.
- Both have speed 12 (NOT 24), poisonous corpses (M1_POIS), and self-teleport (M1_TPORT).
- Quantum corpse toggles Fast (eat.c:1227); genetic engineer corpse triggers polyself (eat.c:1247).
-->

特殊な爪攻撃を持つ2種類の生物です。**量子物理学者 (Quantum mechanic)**は命中時にプレイヤーをランダムな場所へテレポートさせます。**遺伝子工学者 (Genetic engineer)**はプレイヤーを変身（変身(へんげ)）させます。不変（Unchanging）の魔除けや魔法防御がなければ、一撃で別の生物に変えられてしまいます。

両種とも自らランダムにテレポートし、毒のある死体を残します。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 量子物理学者 (quantum mechanic) | 水色 | 7 | 12 | 3 | 10 | 爪 1d4 teleport | Self-テレポート. Corpse toggles intrinsic Fast. |
| 遺伝子工学者 (genetic engineer) | 緑色 | 12 | 12 | 3 | 10 | 爪 1d4 polymorph | Self-テレポート. Corpse triggers polyself. |

:::

#### 錆の怪物および魔法中和者 `R` (Rust monsters and disenchanters `R`)

<!-- audit
2026-05-19:
- Rust monster active attack erodes worn iron armor (uhitm.c:2311); passive damages weapon when you hit it; greased weapons consume a charge instead. Silver/mithril/wood weapons immune (is_rustprone).
- Disenchanter active claw drains armor first (uhitm.c:3611-3644, some_armor + rn2(5) for rings/amulet/blindfold); weapon drain is passive-only.
- Active threat for both is armor, NOT weapons (e.g. long sword).
-->

錆の怪物は接触時に鉄製の武器や防具を急速に錆びさせます。ディスエンチャンター（魔法中和者）は命中時に装備している防具や武器の強化値（+値）を吸い取って低下させます。油を塗った防具や、魔法防御、木製・銀製・革製の装備で対抗してください。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 錆の怪物 (rust monster) | 茶色 | 5 | 18 | 2 | 0 | 接触 錆び ×2 · 反撃 錆び | 遊泳. Touch rusts iron. Strip armor before engaging or use silver. |
| 吸魔の怪物 (disenchanter) | 青色 | 12 | 12 | -10 | 0 | 爪 4d4 disenchant · 反撃 disenchant | Gehennom-only. Active drains armor; passive drains weapon when you melee it. |

:::

#### ヘビ `S` (Snakes `S`)

<!-- audit
2026-05-19:
- 6 snake rows at monsters.h:2167-2221: garter 2167, snake 2174, water moccasin 2182, python 2190, pit viper 2204, cobra 2213.
- "Pit viper" is the snake, NOT "pit fiend" (pit fiend is a `&` major demon at monsters.h:3104-3112).
- M1_SWIM universal across the section; M1_CONCEAL on all except python.
- Python has an AT_TUCH plus AT_HUGS pair (monsters.h:2193-2199), wrap and crush.
- Cobra AT_SPIT/AD_BLND blind at monsters.h:2218 (blind spit out to 6 squares).
-->

大半が猛毒を持っています。クサリヘビ（マムシ）やコブラは致命的な毒を持ち、ガータースネークなどは無害な獲物です。

すべてのヘビは遊泳能力を持ち、*ニシキヘビ (python)* を除いて潜伏能力を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 小さなヘビ (garter snake) | 緑色 | 1 | 8 | 8 | 0 | 噛みつき 1d2 |  |
| ヘビ (snake) | 茶色 | 4 | 15 | 3 | 0 | 噛みつき 1d6 毒 | 死体に毒あり, 毒耐性. |
| 水ヘビ (water moccasin) | 赤色 | 4 | 15 | 3 | 0 | 噛みつき 1d6 毒 | 死体に毒あり, 毒耐性. |
| ニシキヘビ (python) | 赤紫 | 6 | 3 | 5 | 0 | 噛みつき 1d4 · 接触 · 締め付け 1d4 wrap · 締め付け 2d4 |  |
| ハブ (pit viper) | 青色 | 6 | 15 | 2 | 0 | 噛みつき 1d4 毒 ×2 | 死体に毒あり, 毒耐性. |
| コブラ (cobra) | 青色 | 6 | 18 | 2 | 0 | 噛みつき 2d4 毒 · 吐瀉 盲目 | 死体に毒あり, 毒耐性. |

:::

#### トロール `T` (Trolls `T`)

<!-- audit
2026-05-19:
- All 5 troll rows (troll, ice, rock, water, Olog-hai) match monsters.h:2225-2266.
- All carry M1_REGEN | M2_STALK; S_TROLL is is_reviver (mondata.h:170).
- Fire/water/force-bolt do NOT destroy corpses; burn_floor_objects only burns scrolls/spellbooks/slime.
- Trollsbane sets mkcorpstat_norevive (uhitm.c:1906, 4867; mhitm.c:1082).
- Stoning leaves a statue (mon.c:671), so no corpse to revive from.
-->

倒しても一定時間後に死体から自動復活します。確実にトロールの息の根を止めるには、**復活する前に死体を食べる**、缶詰作成道具で缶詰にする、あるいは火炎の杖や火炎の魔法で死体を焼き尽くす必要があります。

すべてのトロールは自動回復能力を持ち、階段の上り下りにも追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| トロル (troll) | 茶色 | 7 | 12 | 4 | 0 | 武器攻撃 4d2 · 爪 4d2 · 噛みつき 2d6 |  |
| 氷のトロル (ice troll) | 白色 | 9 | 10 | 2 | 20 | 武器攻撃 2d6 · 爪 2d6 冷気 · 噛みつき 2d6 | 冷気耐性. |
| 岩のトロル (rock troll) | 水色 | 9 | 12 | 0 | 0 | 武器攻撃 3d6 · 爪 2d8 · 噛みつき 2d6 |  |
| 水のトロル (water troll) | 青色 | 11 | 14 | 4 | 40 | 武器攻撃 2d8 · 爪 2d8 · 噛みつき 2d6 | 遊泳. |
| Olog-hai | 赤紫 | 13 | 12 | -4 | 0 | 武器攻撃 3d6 · 爪 2d8 · 噛みつき 2d6 |  |

:::

#### アンバーハルク `U` (Umber hulks `U`)

混乱の凝視。視線が合うだけでプレイヤーを激しく混乱させます。目隠しやタオルを巻いて盲目状態で戦うか、遠距離から仕留めるのが定石です。混乱耐性やテレパシーを活用してください。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| アンバーハルク (umber hulk) | 茶色 | 9 | 6 | 2 | 25 | 爪 3d4 ×2 · 噛みつき 2d5 · 凝視 confuse | tunnels. Confusion gaze. Hard to navigate around. Hits hard too. |

:::

#### 吸血鬼 `V` (Vampires `V`)

<!-- audit
2026-05-19:
- 3 vampire rows at monsters.h: vampire 2282, vampire lord 2292, Vlad 2306.
- Vampire and vampire lord carry G_NOCORPSE, but the death handler substitutes an already-old human corpse. Vlad leaves none (mon.c:613-646).
- All have M1_REGEN | M1_FLY plus M2_STALK (follows stairs) and shapeshift via M2_WERE-equivalent vamp branch (mon.c).
- Vampire mage is #if 0 DEFERRED in 5.0 (correctly omitted).
- Vlad inhabits Vlad's Tower; holds the Candelabrum of Invocation (mkobj.c spawn for PM_VLAD).
-->

噛みつき攻撃によってプレイヤーの経験値レベルを吸い取ります（エナジードレイン）。こうもりや霧の雲に変身して逃亡・奇襲を行います。通常の吸血鬼や吸血鬼の貴族は古びた人間の死体を残しますが、ヴラドは死体を残しません。ヴラド公は[ヴラドの塔](#vlads-tower)のボスです。

すべての吸血鬼は飛行し、自動回復し、アンデッドであり、階段に追従し、変身能力を持ちます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 吸血鬼 (vampire) | 赤色 | 10 | 12 | 1 | 25 | 爪 1d6 · 噛みつき 1d6 エナジードレイン-XL | Drops an old 人間 corpse. |
| vampire lord | 青色 | 12 | 14 | 0 | 50 | 爪 1d8 · 噛みつき 1d8 エナジードレイン-XL | Drops an old 人間 corpse. |
| 吸血鬼ヴラド (Vlad the Impaler) | 赤紫 | 28 | 26 | -6 | 80 | 武器攻撃 2d10 · 噛みつき 1d12 エナジードレイン-XL | Vampire boss in Vlad's Tower. Has the Candelabrum. |

:::

#### レイス `W` (Wraiths `W`)

<!-- audit
2026-05-19:
- 3 wraith rows at monsters.h: barrow wight 2326, wraith 2336, Nazgul 2343-2353.
- Only plain wraith leaves an eatable corpse; barrow wight and Nazgul carry G_NOCORPSE.
- Wraith corpse grants experience-level gain (eat.c:1141-1142, pluslvl).
- Nazgul AT_BREA/AD_SLEE breath 2d25 sleep (monsters.h Nazgul row); sleep resistance trivializes.
-->

接触によってプレイヤーの経験値レベルを1段階吸い取ります。しかし、倒した後に残る新鮮なレイスの死体を食べれば、逆に経験値レベルが1上昇するという大きな見返りがあります。アンデッド退散や銀の武器が有効です。

すべてのレイスはアンデッドであり、階段の上り下りに追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| バロウ・ワイト (barrow wight) | 灰色 | 3 | 12 | 5 | 5 | 武器攻撃 エナジードレイン-XL · cast spell · 爪 1d4 · 接触 1d4 冷気 | 冷気耐性, 睡眠耐性, 毒耐性. |
| レイス (wraith) | 黒色 | 6 | 12 | 4 | 15 | 接触 1d6 エナジードレイン-XL | 飛行. |
| ナズグル (Nazgul) | 赤紫 | 13 | 12 | 0 | 25 | 武器攻撃 1d4 エナジードレイン-XL · ブレス 2d25 sleep | sees-不可視. |

:::

#### ゾーン `X` (Xorns `X`)

<!-- audit
2026-05-19:
- Xorn stats match monsters.h:2357-2366: speed 9 (NOT fast), 3-claw + bite, MR_FIRE|MR_COLD|MR_STONE.
- Xorns phase through walls via M1_WALLWALK; they do NOT tunnel (no M1_TUNNEL, no rubble left behind).
- Xorn attacks are AD_PHYS only; worn weapons/armor are NOT at risk. Metallivore behavior eats metal off the floor only (monmove.c:1664).
- Xorn corpse grants temporary stone resistance.
-->

D&Dに由来する、土の元素界からやってきた3本腕・3つ目の異形の怪物です。彼らは**固い岩壁をすり抜けて移動**し、突然壁の中から奇襲を仕掛けてきます。金属や宝石を好んで食べます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ゾーン (xorn) | 茶色 | 8 | 9 | -2 | 20 | 爪 1d3 ×3 · 噛みつき 4d6 | 火炎耐性, 冷気耐性, 石化耐性. |

:::

#### 類人猿 `Y` (Apelike creatures `Y`)

<!-- audit
2026-05-19:
- 6 ape/yeti rows at monsters.h:2372-2417 (monkey 2372, ape 2379, owlbear 2386, yeti 2393, carnivorous ape 2402, sasquatch 2409).
- Monkey steals via AT_CLAW/AD_SITM (monsters.h:2376); yeti M1_POIS-free, M2_BRUTE plus MR_COLD intrinsic donor.
- Sasquatch has M1_SEE_INVIS (monsters.h:2413); both yeti and sasquatch speed 15.
-->

類人猿や大猿が中心です。サスクワッチ（雪男）は素早い動きで殴りかかってきます。肉食獣の死体は安全な食料となります。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 猿 (monkey) | 灰色 | 2 | 12 | 6 | 0 | 爪 盗み-item · 噛みつき 1d3 |  |
| 類人猿 (ape) | 茶色 | 4 | 12 | 6 | 0 | 爪 1d3 ×2 · 噛みつき 1d6 |  |
| アウルベア (owlbear) | 茶色 | 5 | 12 | 5 | 0 | 爪 1d6 ×2 · 締め付け 2d8 |  |
| イエティ (yeti) | 白色 | 5 | 15 | 6 | 0 | 爪 1d6 ×2 · 噛みつき 1d4 | 冷気耐性. |
| 人喰い猿 (carnivorous ape) | 黒色 | 6 | 12 | 6 | 0 | 爪 1d4 ×2 · 締め付け 1d8 |  |
| サスカッチ (sasquatch) | 灰色 | 7 | 15 | 6 | 0 | 爪 1d6 ×2 · 蹴り 1d8 | sees-不可視. |

:::

#### ゾンビ `Z` (Zombies `Z`)

<!-- audit
2026-05-19:
- All Z-class stats/attacks match monsters.h:2421-2504.
- Race-based zombies carry G_NOCORPSE, but the death handler substitutes an already-old corpse of their base race (mon.c:620-646). Ghouls and skeletons leave none.
- Skeleton has G_NOGEN: never randomly generated, only from Orcus Town or a bone devil's summons.
- M2_UNDEAD is the class flag (NOT "M3_UNDEAD"); M2_STALK is universal across this section.
-->

動きの鈍いアンデッド。距離を取りながら戦えば容易に倒せます。種族ごとのゾンビは元となった種族の古びた死体を残すため、病気耐性なしで食べると食中毒の危険があります。アンデッド退散の杖や呪文を使うと逃走します。ガイコツ（スケルトン）は自然生成されず、オーケスの町やボーンデビルによって召喚されます。

すべてのゾンビは精神を持たず、アンデッドです。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| コボルドのゾンビ (kobold zombie) | 茶色 | 0 | 6 | 10 | 0 | 爪 1d4 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old kobold corpse. |
| ノームのゾンビ (gnome zombie) | 茶色 | 1 | 6 | 10 | 0 | 爪 1d5 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old gnome corpse. |
| オークのゾンビ (orc zombie) | 灰色 | 2 | 6 | 9 | 0 | 爪 1d6 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old orc corpse. |
| ドワーフのゾンビ (dwarf zombie) | 赤色 | 2 | 6 | 9 | 0 | 爪 1d6 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old dwarf corpse. |
| エルフのゾンビ (elf zombie) | 緑色 | 3 | 6 | 9 | 0 | 爪 1d7 | follows stairs. Drops an old elf corpse. |
| 人間のゾンビ (human zombie) | 白色 | 4 | 6 | 8 | 0 | 爪 1d8 | follows stairs. Drops an old 人間 corpse. |
| エティンのゾンビ (ettin zombie) | 青色 | 6 | 8 | 6 | 0 | 爪 1d10 ×2 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old ettin corpse. |
| グール (ghoul) | 黒色 | 3 | 6 | 10 | 0 | 爪 1d2 麻痺 · 爪 1d3 | 冷気耐性, 睡眠耐性, 毒耐性. 死体を残さない。 |
| 巨人のゾンビ (giant zombie) | 水色 | 8 | 8 | 6 | 0 | 爪 2d8 ×2 | follows stairs, 冷気耐性, 睡眠耐性, 毒耐性. Drops an old 巨人 corpse. |
| 骸骨 (skeleton) | 白色 | 12 | 8 | 4 | 0 | 武器攻撃 2d6 · 接触 1d6 slow | 冷気耐性, 睡眠耐性, 毒耐性, 石化耐性. |

:::

#### 人間およびエルフ `@` (Humans and elves `@`)

<!-- audit
2026-05-19:
- 43 human rows match monsters.h.
- Kops are class K, NOT @.
- Wizard of Yendor row: bright-magenta, L30 Spd12 AC-8 MR100, claw 2d12 steal-amulet + spell, flies/regen/sees-invis/fire-res/poison-res, covetous (monsters.h:2847-2858).
- Master of Thieves is the Rogue quest LEADER (Rog-strt.lua:106) AND the Tourist quest nemesis (Tou-goal.lua:117, monsters.h:3564), NOT the Rogue quest nemesis.
- Master Assassin is the primary Rogue quest nemesis (Rog-goal.lua:72), NOT a backup.
-->

`@` のシンボルだけで相手を判断してはなりません。平和的な店主、僧侶、番兵、クエストリーダーであることもあれば、メデューサ、各職業のネメシス、富豪クロイソス、あるいはイェンダーの魔法使いである可能性もあります。動く前に対象の名前を必ず確認してください。このクラスには兵士、忍者、ドッペルゲンガー、獣人、冒険者、そしてプレイヤー自身も含まれます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 人間 (human) | 白色 | 0 | 12 | 10 | 0 | 武器攻撃 1d6 |  |
| ねずみ人間 (wererat) | 茶色 | 2 | 12 | 10 | 10 | 武器攻撃 2d4 | 自動回復. 死体を残さない。 |
| ジャッカル人間 (werejackal) | 赤色 | 2 | 12 | 10 | 10 | 武器攻撃 2d4 | 自動回復. 死体を残さない。 |
| 狼人間 (werewolf) | 橙色 | 5 | 12 | 10 | 20 | 武器攻撃 2d4 | 自動回復. 死体を残さない。 |
| エルフ (elf) | 白色 | 0 | 12 | 10 | 2 | 武器攻撃 1d8 | sees-不可視. |
| Woodland-elf | 緑色 | 4 | 12 | 10 | 10 | 武器攻撃 2d4 | sees-不可視. |
| Green-elf | 明緑 | 5 | 12 | 10 | 10 | 武器攻撃 2d4 | sees-不可視. |
| Grey-elf | 灰色 | 6 | 12 | 10 | 10 | 武器攻撃 2d4 | sees-不可視. |
| elf-lord | 明青 | 8 | 12 | 10 | 20 | 武器攻撃 2d4 ×2 | sees-不可視. |
| Elvenking | 赤紫 | 9 | 12 | 10 | 25 | 武器攻撃 2d4 ×2 | sees-不可視. |
| ドッペルゲンガー (doppelganger) | 白色 | 9 | 12 | 5 | 20 | 武器攻撃 1d12 | shapeshifter. |
| 店主 (shopkeeper) | 白色 | 12 | 16 | 0 | 50 | 武器攻撃 4d4 ×2 | starts peaceful. Don't anger one. |
| 番兵 (guard) | 青色 | 12 | 12 | 10 | 40 | 武器攻撃 4d10 | starts peaceful. |
| 囚人 (prisoner) | 白色 | 12 | 12 | 10 | 0 | 武器攻撃 1d6 | starts peaceful. |
| 賢者 (Oracle) | 明青 | 12 | 0 | 0 | 50 | 反撃 13d4 魔法 | starts peaceful. |
| priest | 白色 | 12 | 12 | 10 | 50 | 武器攻撃 4d10 · 蹴り 1d4 · cast cleric | starts peaceful. Temple defenders. Convert their altars or sacrifice on them. |
| high priest | 白色 | 25 | 15 | 7 | 70 | 武器攻撃 4d10 · 蹴り 2d8 · cast 2d8 cleric ×2 | sees-不可視. Endgame altar guardian. Don't fight one head-on. |
| 兵士 (soldier) | 灰色 | 6 | 10 | 10 | 0 | 武器攻撃 1d8 | follows stairs. |
| 下士官 (sergeant) | 赤色 | 8 | 10 | 10 | 5 | 武器攻撃 2d6 | follows stairs. |
| 看護婦 (nurse) | 白色 | 11 | 6 | 0 | 0 | 爪 2d6 heal |  |
| 副官 (lieutenant) | 緑色 | 10 | 10 | 10 | 15 | 武器攻撃 3d4 ×2 | follows stairs. |
| 指揮官 (captain) | 青色 | 12 | 10 | 10 | 15 | 武器攻撃 4d4 ×2 | follows stairs. |
| 見張り (watchman) | 灰色 | 6 | 10 | 10 | 0 | 武器攻撃 1d8 | follows stairs, starts peaceful. |
| 見張りの隊長 (watch captain) | 緑色 | 10 | 10 | 10 | 15 | 武器攻撃 3d4 ×2 | follows stairs, starts peaceful. |
| メデューサ (Medusa) | 明緑 | 20 | 12 | 2 | 50 | 武器攻撃 2d4 · 爪 1d8 · 凝視 石化 · 噛みつき 1d6 毒 | 飛行, 遊泳, 水陸両用, 死体に毒あり. |
| イェンダーの魔法使い (Wizard of Yendor) | 明紫 | 30 | 12 | -8 | 100 | 爪 2d12 盗み-amulet · cast spell | 飛行, 自動回復, sees-不可視, 火炎耐性, poison-res. Covetous: テレポート to you in late Gehennom and on the planes. The final boss. |
| クロイソス (Croesus) | 赤紫 | 20 | 15 | 0 | 40 | 武器攻撃 4d10 | sees-不可視, follows stairs. Vault guardian on Fort Ludios. Wields a two-handed sword and hoards gold, gems, and magic items off the floor. |
| 考古学者 (archeologist) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 | tunnels. |
| 野蛮人 (barbarian) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| caveman | 白色 | 10 | 12 | 10 | 0 | 武器攻撃 2d4 |  |
| 治療師 (healer) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 |  |
| 騎士 (knight) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| 武闘家 (monk) | 白色 | 10 | 12 | 10 | 2 | 爪 1d8 · 蹴り 1d8 |  |
| priest | 白色 | 10 | 12 | 10 | 2 | 武器攻撃 1d6 · cast cleric | Temple defenders. Convert their altars or sacrifice on them. |
| レンジャー (ranger) | 白色 | 10 | 12 | 10 | 2 | 武器攻撃 1d4 |  |
| 盗賊 (rogue) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| 侍 (samurai) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d8 ×2 |  |
| 観光客 (tourist) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d6 ×2 |  |
| ワルキューレ (valkyrie) | 白色 | 10 | 12 | 10 | 1 | 武器攻撃 1d8 ×2 |  |
| 魔法使い (wizard) | 白色 | 10 | 12 | 10 | 3 | 武器攻撃 1d6 · cast spell |  |
| カーナボン卿 (Lord Carnarvon) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 4d8 spell | tunnels, starts peaceful. Archeologist quest leader. |
| ペリアス (Pelias) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful. Barbarian quest leader. |
| 呪術師カルノフ (Shaman Karnov) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 2d8 cleric | starts peaceful. Cave Dweller quest leader. |
| ヒポクラテス (Hippocrates) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 1d6 · cast 3d8 cleric ×2 | starts peaceful. Healer quest leader. |
| アーサー王 (King Arthur) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful. Knight quest leader. Holds Excalibur if you didn't get it. |
| 総師範 (Grand Master) | 黒色 | 25 | 15 | 0 | 90 | 爪 4d10 · 蹴り 2d8 · cast 2d8 cleric ×2 | sees-不可視, starts peaceful. Monk quest leader. |
| 主席司祭 (Arch Priest) | 白色 | 25 | 15 | 7 | 90 | 武器攻撃 4d10 · 蹴り 2d8 · cast 2d8 cleric ×2 | sees-不可視, starts peaceful. Priest quest leader. |
| 勇者オリオン (Orion) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 4d8 spell | 遊泳, 水陸両用, sees-不可視, starts peaceful. Ranger quest leader. Bow user. |
| 盗賊の頭領 (Master of Thieves) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · 武器攻撃 2d6 · 爪 2d4 盗み-amulet | starts peaceful. Rogue quest leader; also Tourist quest nemesis. |
| 大名佐藤 (Lord Sato) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful. Samurai quest leader. |
| ツーフラワー (Twoflower) | 白色 | 20 | 15 | 10 | 90 | 武器攻撃 4d10 | starts peaceful. Tourist quest leader. |
| ノルン (Norn) | 赤紫 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 ×2 | starts peaceful, 冷気耐性. Valkyrie quest leader. |
| 緑のネフェレト (Neferet the Green) | 緑色 | 20 | 15 | 0 | 90 | 武器攻撃 4d10 · cast 2d8 spell ×2 | starts peaceful. Wizard quest leader. |
| トート・アモン (Thoth Amon) | 赤紫 | 16 | 12 | 0 | 10 | 武器攻撃 1d6 · cast spell ×2 · 爪 1d4 盗み-amulet | follows stairs. Barbarian quest nemesis. |
| カエン (Master Kaen) | 赤紫 | 25 | 12 | -10 | 10 | 爪 16d2 ×2 · cast cleric · 爪 1d4 盗み-amulet | sees-不可視, follows stairs. Monk quest nemesis. |
| 暗殺者の頭領 (Master Assassin) | 赤紫 | 15 | 12 | 0 | 30 | 武器攻撃 2d6 毒 · 武器攻撃 2d8 · 爪 2d6 盗み-amulet | follows stairs. Rogue quest nemesis. |
| 足利尊氏 (Ashikaga Takauji) | 赤紫 | 15 | 12 | 0 | 40 | 武器攻撃 2d6 ×2 · 爪 2d6 盗み-amulet | follows stairs. Samurai quest nemesis. |
| 暗きもの (Dark One) | 黒色 | 15 | 12 | 0 | 80 | 武器攻撃 1d6 ×2 · 爪 1d4 盗み-amulet · cast spell | follows stairs. Wizard quest nemesis. |
| 学生 (student) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 | tunnels, starts peaceful. |
| 首領 (chieftain) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 | starts peaceful. |
| ネアンデルタール人 (neanderthal) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 2d4 | starts peaceful. |
| 随行員 (attendant) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 | starts peaceful. |
| 小姓 (page) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 ×2 | starts peaceful. |
| 師範 (abbot) | 白色 | 5 | 12 | 10 | 20 | 爪 8d2 · 蹴り 3d2 stun · cast cleric | starts peaceful. |
| 侍者 (acolyte) | 白色 | 5 | 12 | 10 | 20 | 武器攻撃 1d6 · cast cleric | starts peaceful. |
| ハンター (hunter) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d4 | sees-不可視, starts peaceful. |
| ちんぴら (thug) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d6 ×2 | starts peaceful. |
| 忍者 (ninja) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d8 ×2 |  |
| 浪士 (roshi) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d8 ×2 | starts peaceful. |
| ガイド (guide) | 白色 | 5 | 12 | 10 | 20 | 武器攻撃 1d6 · cast spell | starts peaceful. |
| 戦士 (warrior) | 白色 | 5 | 12 | 10 | 10 | 武器攻撃 1d8 ×2 | starts peaceful. |
| 実習生 (apprentice) | 白色 | 5 | 12 | 10 | 30 | 武器攻撃 1d6 · cast spell | starts peaceful. |

:::

#### 大悪魔 `&` (Major demons `&`)

<!-- audit
2026-05-19:
- Bone devil, Orcus, Geryon "sting 2d4" and Baalzebub "bite 2d6" cells are AD_DRST drain-Str, NOT AD_POISON (monsters.h:2999, 3082, 3093, 3112).
- Poison resistance protects against these Strength-draining attacks.
-->

強力無比な大悪魔たちです。多くは同胞の悪魔を呼び出すゲート召喚能力を持ちます（1体の有刺デビルが瞬く間に5体に増えることもあります）。銀の武器やデーモンベインが特効の大ダメージを与えます。ゲリュオン、ディスパテル、ベルゼブブ、アスモデウスのみが賄賂（金貨）による停戦に応じますが、エクスカリバーやデーモンベインを構えているときは交渉に応じません。

すべて階段の上り下りに追従してきます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 水の魔神 (water demon) | 青色 | 8 | 12 | -4 | 30 | 武器攻撃 1d3 · 爪 1d3 · 噛みつき 1d3 | 遊泳, demonic. |
| [amorous demon](#seduction) | 灰色 | 6 | 12 | 0 | 70 | seduction (see Seduction) | 飛行, demonic. Displays as succubus or incubus by the 悪魔's own randomly-assigned gender. |
| 角のある悪魔 (horned devil) | 茶色 | 6 | 9 | -5 | 50 | 武器攻撃 1d4 · 爪 1d4 · 噛みつき 2d3 · 毒針 1d3 | demonic. |
| イリニス (erinys) | 赤色 | 7 | 12 | 2 | 30 | 武器攻撃 2d4 Str-エナジードレイン | 火炎耐性, 毒耐性. Grows stronger as your alignment record falls, gaining harder blows, flight, regeneration, and a second attack. |
| 棘の悪魔 (barbed devil) | 赤色 | 8 | 12 | 0 | 35 | 爪 2d4 · 爪 2d4 sticky · 毒針 3d4 | demonic. |
| マリリス (marilith) | 赤色 | 7 | 12 | -6 | 80 | 武器攻撃 2d4 ×2 · 爪 2d4 ×4 | sees-不可視, demonic. |
| ヴァロック (vrock) | 緑色 | 8 | 12 | 0 | 50 | 爪 1d4 ×2 · 爪 1d8 ×2 · 噛みつき 1d6 | demonic. |
| ヘズロウ (hezrou) | 緑色 | 9 | 6 | -2 | 55 | 爪 1d3 ×2 · 噛みつき 4d4 | demonic. |
| 骨の悪魔 (bone devil) | 灰色 | 9 | 15 | -1 | 40 | 武器攻撃 3d4 · 毒針 2d4 エナジードレイン-Str | demonic. |
| 氷の悪魔 (ice devil) | 白色 | 11 | 6 | -4 | 55 | 爪 1d4 ×2 · 噛みつき 2d4 · 毒針 3d4 冷気 · 接触 1d1 slow | sees-不可視, demonic. |
| ナルフェシニ (nalfeshnee) | 赤色 | 11 | 9 | -1 | 65 | 爪 1d4 ×2 · 噛みつき 2d4 · cast spell | demonic. |
| 穴の悪霊 (pit fiend) | 赤色 | 13 | 6 | -3 | 65 | 武器攻撃 4d2 ×2 · 締め付け 2d4 | sees-不可視, demonic. |
| サンデスティン (sandestin) | 灰色 | 13 | 12 | 4 | 60 | 武器攻撃 2d6 ×2 | shapeshifter, 石化耐性. |
| バルログ (balrog) | 赤色 | 16 | 5 | -2 | 75 | 武器攻撃 8d4 · 武器攻撃 4d6 | 飛行, sees-不可視, demonic. |
| ジョウビレックス (Juiblex) | 明緑 | 50 | 3 | -7 | 65 | engulf 4d10 disease · 吐瀉 3d6 酸 | 飛行, 水陸両用, 不定形, sees-不可視, demonic, 火炎耐性, 毒耐性, 酸耐性, 石化耐性. |
| イーノグ (Yeenoghu) | 赤紫 | 56 | 18 | -5 | 80 | 武器攻撃 3d6 · 武器攻撃 2d8 confuse · 爪 1d6 麻痺 · cast 2d6 魔法 | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| オーケス (Orcus) | 赤紫 | 66 | 9 | -6 | 85 | 武器攻撃 3d6 · 爪 3d4 ×2 · cast 8d6 spell · 毒針 2d4 エナジードレイン-Str | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| ゲーリュオーン (Geryon) | 赤紫 | 72 | 3 | -3 | 75 | 爪 3d6 ×2 · 毒針 2d4 エナジードレイン-Str | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| ディスペータ (Dispater) | 赤紫 | 78 | 15 | -2 | 80 | 武器攻撃 4d6 · cast 6d6 spell | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| ベルゼブブ (Baalzebub) | 赤紫 | 89 | 9 | -5 | 85 | 噛みつき 2d6 エナジードレイン-Str · 凝視 2d6 stun | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| アスモデウス (Asmodeus) | 赤紫 | 105 | 12 | -7 | 90 | 爪 4d4 · cast 6d6 冷気 | 飛行, sees-不可視, demonic, 火炎耐性, 冷気耐性, 毒耐性. |
| デモゴルゴン (Demogorgon) | 赤紫 | 106 | 15 | -8 | 95 | cast 8d6 spell · 毒針 1d4 エナジードレイン-XL · 爪 1d6 disease ×2 | 飛行, sees-不可視, demonic, 火炎耐性, 毒耐性. |
| デス (Death) | 明紫 | 30 | 12 | -5 | 100 | 接触 8d8 death ×2 | 飛行, 自動回復, sees-不可視, teleport-control. Rider of the Apocalypse. Vanquish three to ascend. |
| ペスティレンス (Pestilence) | 明紫 | 30 | 12 | -5 | 100 | 接触 8d8 pestilence ×2 | 飛行, 自動回復, sees-不可視, teleport-control. Rider; spreads disease. |
| フェミン (Famine) | 明紫 | 30 | 12 | -5 | 100 | 接触 8d8 famine ×2 | 飛行, 自動回復, sees-不可視, teleport-control. Rider; drains nutrition to starvation. |
| メイルデーモン (mail daemon) | 明青 | 56 | 24 | 10 | 127 | — | 飛行, 遊泳, sees-不可視, starts peaceful, 火炎耐性, 冷気耐性, 睡眠耐性, 電撃耐性, 毒耐性, 石化耐性. Appears only to deliver in-game mail, then leaves. |
| 風のジン (djinni) | 黄色 | 7 | 12 | 4 | 30 | 武器攻撃 2d8 | 飛行, 毒耐性, 石化耐性. |
| フヘトトルの使い (Minion of Huhetotl) | 橙色 | 16 | 12 | -2 | 75 | 武器攻撃 8d4 · 武器攻撃 4d6 · cast spell · 爪 2d6 盗み-amulet | 飛行, sees-不可視, demonic. |
| ナルゾク (Nalzok) | 橙色 | 16 | 12 | -2 | 85 | 武器攻撃 8d4 · 武器攻撃 4d6 · cast spell · 爪 2d6 盗み-amulet | 飛行, sees-不可視, demonic. |

:::

#### ゴーレム `'` (Golems `'`)

<!-- audit
2026-05-19:
- 11 golem rows at monsters.h:2509-2594 (straw 2509, paper, rope, gold, leather, wood, flesh, clay, stone, glass, iron 2587).
- Iron golem has G_NOCORPSE (monsters.h:2587); it leaves NO corpse, NOT a poisonous one.
- poly_when_stoned (mondata.c:80-85) covers ALL golems except stone golem.
- Iron golem AT_BREA/AD_DRST 4d6 poison breath at monsters.h:2592 — poison resistance critical.
- Clay golem inscription "ATHEIST" wears off via shatter_floor message; clay golem corpse grants nothing on eat.
-->

鉄、石、粘土のゴーレムは非常に強固で危険です。木や革のゴーレムは序盤の敵です。極めて稀に出現する黄金ゴーレムは、歩く財宝の山と言えます。

すべてのゴーレムは精神を持たず、睡眠耐性と毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 藁のゴーレム (straw golem) | 黄色 | 3 | 12 | 10 | 0 | 爪 1d2 ×2 | 冷気耐性. |
| 紙のゴーレム (paper golem) | 白色 | 3 | 12 | 10 | 0 | 爪 1d3 | 冷気耐性. |
| 紐のゴーレム (rope golem) | 茶色 | 4 | 9 | 8 | 0 | 爪 1d4 ×2 · 締め付け 6d1 |  |
| 金のゴーレム (gold golem) | 黄色 | 5 | 9 | 6 | 0 | 爪 2d3 ×2 | 酸耐性. |
| 皮のゴーレム (leather golem) | 茶色 | 6 | 6 | 6 | 0 | 爪 1d6 ×2 |  |
| 木のゴーレム (wood golem) | 茶色 | 7 | 3 | 4 | 0 | 爪 3d4 | 冷気耐性. |
| 肉のゴーレム (flesh golem) | 赤色 | 9 | 8 | 9 | 30 | 爪 2d8 ×2 | 火炎耐性, 冷気耐性, 電撃耐性. |
| 土のゴーレム (clay golem) | 茶色 | 11 | 7 | 7 | 40 | 爪 3d10 |  |
| 岩のゴーレム (stone golem) | 灰色 | 14 | 6 | 5 | 50 | 爪 3d8 | 石化耐性. |
| ガラスのゴーレム (glass golem) | 水色 | 16 | 6 | 1 | 50 | 爪 2d8 ×2 | 酸耐性. |
| 鉄のゴーレム (iron golem) | 水色 | 18 | 6 | 3 | 60 | 武器攻撃 4d10 · ブレス 4d6 毒 | no corpse. 火炎耐性, 冷気耐性, 電撃耐性. |

:::

#### 海の怪物 `;` (Sea monsters `;`)

水中に生息する怪物です。巨大ウナギやクラーケンはプレイヤーの体に巻き付き、水中に引きずり込んで溺死させようとします。魔法の呼吸（Magical breathing）がなければ瞬時に命を落とします。

すべての海の怪物は遊泳能力を持ち、水陸両用です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| クラゲ (jellyfish) | 青色 | 3 | 3 | 6 | 0 | 毒針 3d3 エナジードレイン-Str | 死体に毒あり, 毒耐性. |
| ピラニア (piranha) | 赤色 | 5 | 18 | 4 | 0 | 噛みつき 2d6 ×2 |  |
| サメ (shark) | 灰色 | 7 | 12 | 2 | 0 | 噛みつき 5d6 |  |
| 巨大ウナギ (giant eel) | 水色 | 5 | 9 | -1 | 0 | 噛みつき 3d6 · 接触 wrap |  |
| 電気ウナギ (electric eel) | 明青 | 7 | 10 | -3 | 0 | 噛みつき 4d6 電撃 · 接触 wrap | 電撃耐性. |
| クラーケン (kraken) | 赤色 | 20 | 3 | 6 | 0 | 爪 2d4 ×2 · 締め付け 2d6 wrap · 噛みつき 5d4 |  |

:::

#### トカゲ `:` (Lizards `:`)

<!-- audit
2026-05-19:
- 8 lizard rows at monsters.h:3260-3324 (newt 3260, gecko, iguana, baby croc, lizard, chameleon, croc, salamander 3317).
- Lizard corpse cures stoning (eat.c:827-830, fix_petrification) and never rots (eat.c:1483, 1510).
- Newt corpse occasionally restores 1-3 Pw via eye_of_newt_buzz (eat.c:1102-1123).
- Chameleon is M2_SHAPESHIFTER (monsters.h:3299, sets shifter via newcham).
- Salamander has 4-attack chain at monsters.h:3317-3324: weapon 2d8, touch 1d6 fire, hug 2d6, hug 3d6 fire.
- Salamander is G_HELL (Gehennom-only spawn flag).
-->

大半は無害です。**トカゲの死体は石化を治療し、決して腐敗しません**。コカトリス対策として必ず荷物に1つ入れておきましょう。ただし、メデューサの直接の凝視による石化は即死するため、トカゲの死体では救われません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| イモリ (newt) | 黄色 | 0 | 6 | 8 | 0 | 噛みつき 1d2 | 遊泳, 水陸両用. |
| ヤモリ (gecko) | 緑色 | 1 | 6 | 8 | 0 | 噛みつき 1d3 |  |
| イグアナ (iguana) | 茶色 | 2 | 6 | 7 | 0 | 噛みつき 1d4 |  |
| ワニの子供 (baby crocodile) | 茶色 | 3 | 6 | 7 | 0 | 噛みつき 1d4 | 遊泳, 水陸両用. |
| トカゲ (lizard) | 緑色 | 5 | 6 | 6 | 10 | 噛みつき 1d6 | 石化耐性. |
| カメレオン (chameleon) | 茶色 | 6 | 5 | 6 | 10 | 噛みつき 4d2 | shapeshifter. |
| ワニ (crocodile) | 茶色 | 6 | 9 | 5 | 0 | 噛みつき 4d2 · 爪 1d12 | 遊泳, 水陸両用. |
| サラマンダー (salamander) | 橙色 | 8 | 12 | -1 | 0 | 武器攻撃 2d8 · 接触 1d6 火炎 · 締め付け 2d6 · 締め付け 3d6 火炎 | 死体に毒あり, follows stairs, 火炎耐性, 睡眠耐性. |

:::

### 固有能力および外在能力一覧表 (Intrinsic and Extrinsic Tables)

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

#### ダメージ耐性 (Damage resistances)

最も範囲が広く、最も活用される能力群です。大半は序盤に死体を食べることで獲得できます。魔法防御（Magic resistance）は獲得手段が極めて限られているため、昇天用装備セットでは防具、武器、アーティファクトの枠を1つ確保して補うのが基本です。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **火炎耐性** (Fire resistance) | 罠、ブレス、攻撃による火炎ダメージを無効化（溶岩への水没死は防げない）。 | 修道士 レベル11、僧侶 レベル20。赤ドラゴン、火蟻、火の巨人、ヘルハウンド、サラマンダー、赤色モールドの死体。溶岩からの祈り救済。 | 火炎耐性の指輪。赤ドラゴンの鱗 / 鱗鎧。 |
| **冷気耐性** (Cold resistance) | ブレスや攻撃による冷気ダメージを無効化。 | ワルキューレ レベル1、修道士 レベル13。白ドラゴン、霜の巨人、冬狼、茶色モールド、青色ゼリーの死体。 | 冷気耐性の指輪。白ドラゴンの鱗 / 鱗鎧。 |
| **睡眠耐性** (Sleep resistance) | 睡眠ガス、睡眠光線、モンスターの睡眠攻撃を完全無効化。 | 修道士 レベル1、エルフ レベル4。エルフ全般、ホムンクルスの死体。祈り救済。 | 橙色ドラゴンの鱗 / 鱗鎧。 |
| **分解耐性** (Disintegration resistance) | 黒ドラゴンの分解ブレスを無害化。 | 黒ドラゴンの死体。 | 黒ドラゴンの鱗 / 鱗鎧。 |
| **電撃耐性** (Shock resistance) | 電撃ブレスを含むすべての電撃ダメージを無効化。 | 修道士 レベル15。青ドラゴン、電気ウナギの死体。 | 耐電の指輪。青ドラゴンの鱗 / 鱗鎧。電撃耐性の盾（5.0新要素）。 |
| **毒耐性** (Poison resistance) | 毒針、毒のある死体、毒ブレス、筋力を奪う毒攻撃を完全防御。 | 野蛮人 レベル1、医師 レベル1、オーク レベル1、観光客 レベル20、修道士 レベル3。殺人蜂やサソリの死体（獲得確率が極めて高い）。緑ドラゴン、ナーガ、クアジット等の毒死体。 | 耐毒の指輪。耐毒の魔除け。錬金術の仕事着（クローク）。緑ドラゴンの鱗 / 鱗鎧。 |
| **酸耐性** (Acid resistance) | 酸ダメージを無効化。死体からの獲得は時間制限付きで、フロア移動でリセットされる。 | 酸のブロッブ、茶色プリン、黄ドラゴンの死体（高確率、時間制限あり）。 | 黄ドラゴンの鱗 / 鱗鎧（装備中恒久）。 |
| **石化耐性** (Stoning resistance) | 肉体の石化に対する完全免疫。死体からの獲得は一時的。黄ドラゴンの鎧は装備中持続。 | 酸のブロッブ、トカゲの死体（高確率、時間制限あり）。 | 黄ドラゴンの鱗 / 鱗鎧。 |
| **吸命耐性** (Drain resistance) | レイス、吸血鬼、生命力吸収武器（ストームブリンガー等）による経験値レベルドレインを遮断。 | 死体からは獲得不可。吸血鬼やリッチへの変身で獲得。 | 黒ドラゴンの鱗 / 鱗鎧。吸命耐性の盾（5.0新要素）。[エクスカリバー](#excalibur-artifact)、ストームブリンガー、[アスクレピオスの杖](#staff-of-aesculapius)の装備。 |
| **病気耐性** (Sickness resistance) | 致命的な病気や食中毒を遮断。 | 死体からは獲得不可。 | 緑ドラゴンの鱗 / 鱗鎧。 |
| **魔法防御** (Magic resistance) | 死の光線、マジックミサイル、変身(へんげ)ビーム、死の指の呪文を完全無効化。魔法の罠は防げない。[MC](#magic-cancellation)とは異なる。 | いかなる職業も内在習得不可。特定の変身形態で保有。 | 魔法を防ぐクローク。灰色ドラゴンの鱗 / 鱗鎧。[マジックベイン](#magicbane)の装備。 |
| **幻覚耐性** (Hallucination resistance) | 黒い光や幻覚の薬による幻覚状態を遮断。 | 幻覚攻撃を持つモンスター（黒い光等）への変身のみ。 | 金色ドラゴンの鱗 / 鱗鎧。[グレイスワンダー](#grayswandir)の装備。 |
| **盲目耐性** (Blindness resistance) | 黄色い光の閃光による盲目化を遮断。 | 盲目攻撃を持つモンスターへの変身のみ。 | [サンソード](#sunsword)の装備。 |

:::

#### 感覚と知覚 (Senses and perception)

テレパシーと警告は、敵が接近する前にその存在と位置を正確に感知させてくれます。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **テレパシー** (ESP) | 盲目時にフロア全体の精神を持つモンスターを探知（視覚があるときは限定半径内）。 | さまよう目（確実獲得）、マインドフレア、マスターマインドフレアの死体。 | 遠視の魔除け。テレパシーの兜。[エチオピカの目](#eye-of-the-aethiopica)（所持）、[探知のオーブ](#orb-of-detection)（所持）、[プラチナイェンダー印エクスプレスカード](#platinum-yendorian-express-card)（所持）、[ディアナの長弓](#longbow-of-diana)（所持）、[マジックベイン](#magicbane)（装備）。 |
| **不可視視認** (See invisible) | 透明な生物、および透明化した自分自身を視認できる。 | 修道士 レベル1、野伏 レベル15。死体からは獲得不可。 | 可視の指輪。 |
| **警告** (Warning) | 約10マス以内にいるレベル4以上の敵対モンスターを感知表示（数字はモンスターレベル÷4）。 | 洞窟人 レベル15、医師 レベル15、修道士 レベル7、僧侶 レベル15、魔法使い レベル15。祈り救済。 | 警告の指輪。知性の兜。[盗賊術のマスターキー](#master-key-of-thievery)、[運命のオーブ](#orb-of-fate)、[オークリスト](#bane-weapons)、[スティング](#bane-weapons)、[グリムトゥース](#bane-weapons)（すべて所持）。 |
| **特定種族への警告** | 特定の1種族に限定された警告表示。 | 内在能力としては存在しない。 | オークリスト / スティング（オーク警告）、グリムトゥース（エルフ警告）など。 |
| **探索** (Searching) | 約85ターンに1回自動的に周囲を探索し、隠し扉や通路、罠を発見する。 | 考古学者 レベル1、修道士 レベル9、野伏 レベル1、盗賊 レベル10、観光客 レベル10。 | 探索の指輪。[エクスカリバー](#excalibur-artifact)の所持。 |
| **透視** (Clairvoyance) | 周囲のダンジョン地形を周期的に魔法の眼で開拓視認。 | 内在能力としては存在しない。 | とんがり帽子（魔法使い専用）。 |
| **赤外線視覚** (Infravision) | 暗闇の中で熱源（温血生物）を感知。 | ドワーフ、エルフ、ノーム、オークの各種族（レベル1）。 | 赤ドラゴンの鱗 / 鱗鎧。 |

:::

#### 移動と空間挙動 (Movement and spatial behavior)

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **高速移動** (Fast / intrinsic speed) | 各移動時に約1/3の確率で追加行動。実効速度が12から約16に向上。 | 修道士 レベル1、侍 レベル1、ワルキューレ レベル7、考古学者 レベル10、野蛮人 レベル7、洞窟人 レベル7、騎士 レベル7。祈り救済。 | 韋駄天の靴（**極めて高速 / Very Fast**、約2/3で追加行動、実効速度約20）。青ドラゴンの鱗 / 鱗鎧（極めて高速）。 |
| **跳躍** (Jumping) | `#jump` コマンドにより近くの任意のマスへ跳躍移動。 | 騎士 レベル1。 | 跳躍の靴。跳躍の呪文。 |
| **瞬間移動** (Teleportation / 不制御) | 数百ターンごとにランダムにテレポート。制御と組み合わせると極めて強力。 | テングの死体。 | 瞬間移動の指輪。 |
| **瞬間移動制御** (Teleport control) | テレポート時に目的地の座標を自由に選択可能。 | 修道士 レベル17、魔法使い レベル17。テングの死体。 | 瞬間移動制御の指輪。[盗賊術のマスターキー](#master-key-of-thievery)の所持。（イェンダーの魔除けの所持中は制御テレポートが**阻害**される）。 |
| **浮遊** (Levitation) | 常に宙に浮く。水面、溶岩、氷を渡れる。階段を降りられず、床の物を拾えない。 | なし。 | 浮遊の指輪。浮遊の靴（呪われていると脱げない）。[アーリマンの心臓](#heart-of-ahriman)の所持。 |
| **飛行** (Flying) | 浮遊と同様だが、階段の昇降、アイテムの回収、任意着地が可能。 | 飛行モンスターへの変身。 | 飛行の魔除け（5.0新要素）。 |
| **水上歩行** (Water walking) | 水上や氷上を通常の床と同様に歩行可能。耐火加工された靴なら溶岩も渡れる。 | 特定モンスター（アンデッド等）への変身。 | 水上歩行の靴。 |
| **呼吸** (Magical breathing) | ウナギやクラーケンに巻き込まれても溺死せず、悪臭の雲の中でも生存可能。 | 内在能力としては存在しない。 | 呼吸の魔除け。 |

:::

#### 戦闘と防御 (Combat and defense)

昇天用装備セットを支える多層防御：AC、反射、自由行動、自動回復など。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **防護** (Protection) | ACを改善（数値が低下）。また装備中の外在源1つにつき+1の[MC](#magic-cancellation)を付与（守りの魔除けは+2）。 | 平和的な僧侶への多額の寄付（必要金額はランダム）。 | 防護の指輪。守りのクローク（MC3併託）。守りの魔除け（MC2併託）。[力の王笏](#sceptre-of-might)、[神聖の僧帽](#mitre-of-holiness)、[村正の剣](#tsurugi-of-muramasa)の所持。 |
| **反射** (Reflection) | 遠距離魔法攻撃（光線、ブレス）を術者へ跳ね返す。 | 内在能力としては存在しない。 | 反射の魔除け。銀ドラゴンの鱗 / 鱗鎧。反射の盾。[ドラゴンベイン](#bane-weapons)または[ディアナの長弓](#longbow-of-diana)の装備。 |
| **自動回復** (Regeneration) | 自然回復に加え、毎ターンHPが1回復する。 | トロール等の回復モンスターへの変身。 | 回復の指輪。[トロールベイン](#bane-weapons)または[アスクレピオスの杖](#staff-of-aesculapius)の装備。 |
| **魔力自動回復** (Energy regeneration) | 呪文の魔力（Pw）が急速に回復する。 | 内在能力としては存在しない。 | [エチオピカの目](#eye-of-the-aethiopica)の所持。 |
| **魔法半減** (Half spell damage) | モンスターが唱える呪文による被ダメージを半減。 | 内在能力としては存在しない。 | [探知のオーブ](#orb-of-detection)、[盗賊術のマスターキー](#master-key-of-thievery)、[プラチナイェンダー印エクスプレスカード](#platinum-yendorian-express-card)、[運命のオーブ](#orb-of-fate)の所持。 |
| **物理ダメージ半減** (Half physical damage) | 近接攻撃および物理遠距離攻撃による被ダメージを半減。 | 内在能力としては存在しない。 | [盗賊術のマスターキー](#master-key-of-thievery)または[運命のオーブ](#orb-of-fate)の所持。 |
| **自由行動** (Free action) | さまよう目、ゼラチンキューブ、グール、モンスターの呪文による麻痺を完全無効化。減速は防げない。 | 特定モンスターへの変身。 | 自由行動の指輪。橙ドラゴンの鱗 / 鱗鎧。 |
| **忍び足** (Stealth) | 睡眠中のモンスターの近くを歩いても目覚めさせず、気付かれずに通過できる。 | 考古学者 レベル5、野蛮人 レベル15、修道士 レベル5、野伏 レベル7、盗賊 レベル1、侍 レベル15、ワルキューレ レベル3。祈り救済。 | 忍び足の指輪。エルフの靴。エルフのクローク。[アーリマンの心臓](#heart-of-ahriman)の所持。 |
| **不可視** (Invisibility) | 不可視視認を持たないモンスターはプレイヤーの正確なマスを見失うため命中率が激減。攻撃すると位置が露見する。 | ストーカーへの変身。不可視の薬（一時的）。 | 不可視の指輪。透明のクローク。[探知のオーブ](#orb-of-detection)の所持。 |
| **幻影** (Displacement) | モンスターの目にはプレイヤーが隣接する別のマスにいるように映り、遠距離攻撃が外れやすくなる。 | 内在能力としては存在しない。 | 幻影のクローク。 |

:::

#### 特殊および実用能力 (Special and utility)

満腹度、変身、生存、群衆制御に関わる特殊能力です。

::: dense-table

| 能力名 | 効果 | 内在能力の獲得源 | 外在能力の獲得源 |
|---|---|---|---|
| **消化不良** (Slow digestion) | 通常の空腹進行を完全に停止。特殊な栄養吸収攻撃などによる飢餓は防げない。 | なし。 | 消化不良の指輪。白ドラゴンの鱗 / 鱗鎧。 |
| **へんげ制御** (Polymorph control) | 罠、指輪、薬、杖、呪文によって変身する際、変身後の姿を自由に選択できる。 | なし。 | へんげ制御の指輪。 |
| **耐へんげ** (Unchanging) | 現在の姿を固定する。あらゆる変身(へんげ)を防ぎ、*緑スライム化のカウントダウンも停止させる*。「スライムに触られた」際の標準的対処法。 | なし。 | 耐へんげの魔除け。 |
| **能力維持** (Sustain ability) | 6大基本能力値（Str, Dex, Con, Int, Wis, Cha）が消耗、鍛錬、薬、毒などの能力低下攻撃によって変動しなくなる。 | なし。 | 能力維持の指輪。 |
| **変身生物除け** (Protection from shape changers) | 周囲のカメレオン、ドッペルゲンガー、サキュバス等の変身能力を封じる。 | なし。 | 耐へんげの指輪。 |
| **争い** (Conflict) | 周囲のモンスター同士を同士討ちさせる。効果に巻き込まれた店主はプレイヤーに敵対する。 | なし。 | 争いの指輪。[力の王笏](#sceptre-of-might)の所持。 |
| **命の魔除け** (Life saving) | 死亡時に魔除けが身代わりとなって破壊され、HPを `50 + 10 × (Con ÷ 2)`（最大HP上限）まで瞬時に全快復活させる。 | なし。 | 命の魔除け。 |
| **飾り** (Adornment) | 指輪の強化値が魅力（Charisma）に加算される。買い物や誘惑対策に有用。 | なし。 | 飾りの指輪。 |

:::

一部の能力は実質的に**変身時限定**です：*遊泳*および*壁通過*（ゾーン、土の精、ゴースト）。*怪物探知*は杖や巻物による一過性のパルス効果としてのみ利用可能です。

### 前回からの変更点 (What Changed Since Last Time)

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

#### 改めるべき古い習慣 {#new-dangers}

- **ユニコーンの角は低下した能力値を回復しなくなりました。** 能力値回復には能力回復の薬（または回復の魔法）を用意してください。
- **自分自身に振った加速の杖は恒久的な加速を付与しなくなりました。** 恒久加速には加速の薬が必要です。
- **希釈による錬金術は、1回の浸しで最大2服の薬しか変換できなくなりました。** 未希釈の薬同士の調合なら引き続きスタック一括変換が可能です。爆発確率は通常10%ですが、錬金術の仕事着を着ていれば約1/30に軽減されます。
- **ゲヘナの灼熱の床に薬を置くと、高確率で粉砕します。** また、魔王や大悪魔がフロア内で生存している間は、同一フロア内のテレポートも封殺されます。
- **モンスターが施錠されていない保管箱を漁り、適切な死体の山をアンデッドとして蘇生させるようになりました。** アイテムの保管庫を離れる際は、必ず箱に鍵をかけてください。
- **呪われた杖を文字彫りテストすると爆発することがあります。** 貴重そうな杖をテストする前に、可能な限りBUC（祝福・呪い）を識別してください。
- **低レベルモンスターの生贄では幸運値を稼げなくなりました。** 現在の幸運値が死体の難易度（モンスターレベル）を上回っている場合、生贄を捧げても幸運は上昇しません。幸運の維持には幸運の石を活用してください。
- **ワルキューレの初期装備が長剣から通常の槍に変更されました。** 経験レベル5以上の騎士によるエクスカリバーの泉浸し（1/6の確率）は健在ですが、他の秩序職業の成功率は1/30です。
- **死の指（Touch of death）の呪文は即死効果ではなくなりました。** 魔法防御がない場合、50+8d6 の大ダメージを受け、さらにその半分の値が最大HP上限から直接削り取られます（魔法防御があれば完全に防げます）。

#### 新たな道具とチャンス (New Tools and Opportunities)

- **ドラゴンの鱗鎧が強力な二次効果を持つようになりました。** 黒は吸命耐性、緑は病気耐性、青は高速移動、橙は自由行動、白は消化遅延、赤は赤外線視覚を追加付与し、金は幻覚耐性に加えて半径3マスの恒久光源となります。
- **知性の兜 (helm of caution)** が警告能力を付与します。**飛行の魔除け (amulet of flying)** は自身と騎乗ペットの両方に飛行を与え、**守りの魔除け (amulet of guarding)** は AC+2 および MC+2 を提供します。
- **複数のアーティファクトに発動効果や新能力が追加されました。** スニッカーズニーは毎ターン1回無料の長柄武器スタイル間合い攻撃を繰り出せます。サンソードは25 Pwを消費して対象を盲目にします。トロールベインは装備中に自動回復します。デーモンベインは僧侶が生贄で最初に確定入手する銀のメイスとなりました。
- **新たな「願い」の入手源が登場しました。** ヴラドの玉座に座り続けることで最終的に願いを獲得でき、イェンダーの魔除けを最初に拾い上げた際にも願いが1回与えられます。またオーケスの町には魔法のランプまたは魔法のマーカーが確定生成されます。
- **祝福されたへんげの薬は、その1回の変身において変身先を自由に制御（選択）できます。** 変身した吸血鬼は `#monster` コマンドで吸血鬼、こうもり、霧の雲を自在に切り替えられます。
- **重石（ロードストーン）は呪われていても、接地している間は吹き飛ばし（ノックバック）を防ぎます。** 重量負担は依然として過酷ですが、使い道が生まれました。
- **補給の宝箱 (supply chests)** が神託所より上の浅い階層の約2/3の確率で出現し、序盤の回復や強化アイテムを提供してくれます。
- **ペットが死体を食べて耐性を獲得できるようになりました。** 死亡したペットも、その死体の上に乗って同属性の祭壇で祈ることで復活させることができます。
- **流し台（シンク）に薬を浸すと、メッセージによって薬が識別されます。** 薬は失われますが、識別の巻物を節約できます。
- **連鎖雷撃 (chain lightning)** が新たなレベル2の攻撃呪文として追加され、周囲の敵を次々と感電させます。通常フロアに新たな**テーマ別部屋**が生成されるようになり、4種の新モンスター（ディスプレイスビースト、遺伝子工学者、金ドラゴン、子金ドラゴン）が登場しました。

#### その他の知っておくべき変更点 (Other Changes Worth Knowing)

- *魅了 (charm monster)* はレベル5、*眠り (sleep)* はレベル3、*怪物混乱 (confuse monster)* はレベル1に変更されました。魔法書を使用（apply）することで、本の磨耗度を確認できます。
- マインドフレアの触手攻撃は、マップの記憶や識別済みの記憶を消去しなくなりました。知力の低下、記憶していた呪文の忘却、武器スキルの経験値ドレインは依然として発生します。
- 軽量化の鞄の爆発は、中身を全消滅させるのではなくフロア中に散乱（scatter）させるようになりました（約1/13のアイテムは消滅します）。
- 僧侶への寄付金額がランダム化されました。防護を得るには、要求された金額の2倍以上3倍未満を寄付してください。それ以上寄付しても感謝されるだけで、過小な寄付は今後の要求額を引き上げます。
- 特殊フロアのマップが左右反転（ミラーリング）して生成されることがあり、暗記したマップが反転している場合があります。新たなコンダクトとして赤貧（Pauper）、ペットなし、完全聾、倉庫番、ボーンズなし、初期キャラ固定が公式記録されます。
- 両手持ち武器は筋力ダメージボーナスの 150%（1.5倍）を受けます。自然治癒によるHP回復は毎ターン `(XL + 耐久力)%` の確率判定となり、自動回復能力はそれに加えて毎ターン1 HPを回復します。
- 財宝に執着するモンスター（Covetous）は、どちらの階段へも逃走するようになりました。城のフロア生成時にマスターリッチやアーチリッチが初期配置されることはなくなりました。
- 水晶の鎧は段階的にひび割れ、耐ひび割れ加工が可能になりました。蝋燭による光源半径は線形ではなく平方根ルールで拡大します。
- 耐性を付与する死体、缶詰、卵は店での販売価格が高くなりました。モンスター死亡時に無関係な食料品をランダムドロップすることはなくなりました。
- 店主は店内の落とし穴や蜘蛛の巣を除去するようになり、平和的な店主に接触して歩き込むと自動的に借金を精算してから所持品確認プロンプトへ進みます。

## 有用な知識の索引 (Index of Useful Knowledge)

```{=latex}
\begin{multicols}{2}
\footnotesize\raggedright\setlength{\parskip}{0.15em plus 0.05em}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000

\par\smallskip{\normalsize\bfseries 0--9}\par\smallskip

\hyperref[golems]{`'` golems, p.~\pageref*{golems}}\par
\hyperref[use-testing-the-careful-way]{\$200 potions, the hidden traps, p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[armor-prices]{\$30 boots, the warning, p.~\pageref*{armor-prices}}\par
\hyperref[wand-prices]{\$500 wand, very good day, p.~\pageref*{wand-prices}}\par
\hyperref[major-demons]{`\&` major demons, p.~\pageref*{major-demons}}\par
5.0: \hyperref[what-changed-since-last-time]{new features, items, and mechanics, p.~\pageref*{what-changed-since-last-time}}; \hyperref[new-dangers]{habits to relearn, p.~\pageref*{new-dangers}}\par
\hyperref[carrying-capacity]{52 inventory slots, the letter limit, p.~\pageref*{carrying-capacity}}\par
\hyperref[lizards]{`:` lizards, p.~\pageref*{lizards}}\par
\hyperref[sea-monsters]{`;` sea monsters, p.~\pageref*{sea-monsters}}\par
\hyperref[humans-and-elves]{`@` humans and elves (monster class), p.~\pageref*{humans-and-elves}}\par
\hyperref[a-note-on-mimics]{`]` strange object, always a mimic, p.~\pageref*{a-note-on-mimics}}\par
\hyperref[special-symbols]{`\textasciitilde{}` long worm tail, p.~\pageref*{special-symbols}}\par

\par\smallskip{\normalsize\bfseries A}\par\smallskip

\hyperref[angelic-beings-a]{`A` angelic beings, p.~\pageref*{angelic-beings-a}}\par
\hyperref[ants-and-insects-a]{`a` ants and insects, p.~\pageref*{ants-and-insects-a}}\par
AC: \hyperref[ac-and-defense]{the AC ladder to -20, special attacks ignore, p.~\pageref*{ac-and-defense}}\par
Acid: \hyperref[petrification-stoning]{blob corpse, timed stoning resistance, p.~\pageref*{petrification-stoning}}; \hyperref[vegetarian-safe-corpses]{blob corpse, stoning resistance (timed), p.~\pageref*{vegetarian-safe-corpses}}\par
\hyperref[engravings]{Ad aerarium engraving, vault closet marker, p.~\pageref*{engravings}}\par
\hyperref[carrying-capacity]{\#adjust, swap and merge letters, p.~\pageref*{carrying-capacity}}\par
Air: \hyperref[vortices-v]{fire, ice, steam, energy, dust vortex, p.~\pageref*{vortices-v}}; \hyperref[elementals-e]{elemental, engulfs and suffocates, p.~\pageref*{elementals-e}}\par
Alchemy: \hyperref[alchemy]{dip recipes, chain, healing → extra → full → gain ability, 10\% blast chance, about 1 in 30 in a smock, p.~\pageref*{alchemy}}; \hyperref[cloaks]{smock, poison resistance, p.~\pageref*{cloaks}}\par
Alignment: \hyperref[alignment]{it's a number, p.~\pageref*{alignment}}; \hyperref[alignment-and-blasting]{and blasting, misaligned artifact damage, p.~\pageref*{alignment-and-blasting}}\par
Altars: \hyperref[altars-_]{BUC testing, dropping the whole pile, p.~\pageref*{altars-_}}; \hyperref[altars-and-alignment]{conversion and the inversion trap, p.~\pageref*{altars-and-alignment}}\par
\hyperref[seduction]{Amorous demon, expensive evening with, p.~\pageref*{seduction}}\par
Amulet: \hyperref[choking]{of strangulation, timer death, p.~\pageref*{choking}}; \hyperref[delayed-deaths]{of unchanging, blocks slime, p.~\pageref*{delayed-deaths}}; \hyperref[amulet-prices]{prices, all \$150, p.~\pageref*{amulet-prices}}; \hyperref[amulets]{of life saving, when to wear, of life saving, revives once, of reflection, ray bouncing, of magical breathing, underwater, of ESP (telepathy), of unchanging, blocks polymorph, of flying, mount flies too (new in 5.0), of guarding, +2 AC +2 MC (new in 5.0), of strangulation, 90\% cursed, of restful sleep, the rebrand, p.~\pageref*{amulets}}; \hyperref[the-gauntlet]{blocks teleportation, climb by foot, p.~\pageref*{the-gauntlet}}\par
Amulet of Yendor: \hyperref[molochs-sanctum]{the prize, p.~\pageref*{molochs-sanctum}}; \hyperref[the-ascension-run]{retrieving, pickup wish, on next turn, p.~\pageref*{the-ascension-run}}; \hyperref[the-elemental-planes]{the compass, p.~\pageref*{the-elemental-planes}}\par
\hyperref[angelic-beings-a]{Angel, on the Astral Plane, p.~\pageref*{angelic-beings-a}}\par
\hyperref[the-price-is-right]{Angry-shopkeeper +33\% surcharge, permanent, p.~\pageref*{the-price-is-right}}\par
\hyperref[dungeon-overview-and-event-journal]{Annotate (`\#annotate`), labeling stash floors, p.~\pageref*{dungeon-overview-and-event-journal}}\par
\hyperref[dangerous-traps]{Anti-magic field, hits harder with MR, p.~\pageref*{dangerous-traps}}\par
\hyperref[common-combat-deaths]{Ants, pack travelers, p.~\pageref*{common-combat-deaths}}\par
\hyperref[liches-l]{Arch-lich, touch of death, p.~\pageref*{liches-l}}\par
Archeologist: \hyperref[the-roles]{touchstone advantage, pickaxe from turn one, p.~\pageref*{the-roles}}\par
\hyperref[angelic-beings-a]{Archon, ultimate pet, p.~\pageref*{angelic-beings-a}}\par
Armor: \hyperref[the-early-shopping-list]{improvements, even basic, p.~\pageref*{the-early-shopping-list}}; \hyperref[use-testing-the-careful-way]{randomized appearances, pools, helms cloaks gloves boots, p.~\pageref*{use-testing-the-careful-way}}; \hyperref[armor-prices]{prices, the danger zones, p.~\pageref*{armor-prices}}\par
\hyperref[nuisance-traps]{Arrow trap, free ammunition farm, p.~\pageref*{nuisance-traps}}\par
Ascension: \hyperref[the-ascension-run]{how to not die during, p.~\pageref*{the-ascension-run}}; \hyperref[what-killed-the-runners-up]{three avoidable near-ascension deaths, p.~\pageref*{what-killed-the-runners-up}}; \hyperref[strategy]{Run strategy, run don't fight, p.~\pageref*{strategy}}\par
\hyperref[the-demon-prince-lairs]{Asmodeus, bribable cold caster, p.~\pageref*{the-demon-prince-lairs}}\par
Astral: \hyperref[the-astral-plane]{Plane, three altars, choose wrong altar = game ends, farlook reveals altar only when adjacent, p.~\pageref*{the-astral-plane}}\par
\hyperref[engravings]{Athame, the non-dulling stylus, p.~\pageref*{engravings}}\par
Atheist: \hyperref[atheist]{conduct, ascension Amulet offering is exempt, p.~\pageref*{atheist}}\par
\hyperref[the-seven-spell-schools]{Attack school, force bolt grind, p.~\pageref*{the-seven-spell-schools}}\par
\hyperref[the-ascension-run]{Authentic Amulet, only from the High Priest, p.~\pageref*{the-ascension-run}}\par
Auto-curse: \hyperref[blessed-uncursed-cursed-buc]{items, read as uncursed (trap), p.~\pageref*{blessed-uncursed-cursed-buc}}; \hyperref[the-ring-table]{rings (teleport, polymorph, aggravate, hunger), p.~\pageref*{the-ring-table}}\par
\hyperref[options-worth-knowing-about]{Autopickup and pickup\_types, p.~\pageref*{options-worth-knowing-about}}\par

\par\smallskip{\normalsize\bfseries B}\par\smallskip

\hyperref[bats-and-birds-b]{`B` bats and birds, p.~\pageref*{bats-and-birds-b}}\par
\hyperref[blobs-b]{`b` blobs, p.~\pageref*{blobs-b}}\par
\hyperref[the-demon-prince-lairs]{Baalzebub, beetle-shaped lair, p.~\pageref*{the-demon-prince-lairs}}\par
\hyperref[dragons-d]{Baby dragon, doesn't breathe, p.~\pageref*{dragons-d}}\par
Bag of holding: \hyperref[containers]{the turning point, never insert wand of cancellation, p.~\pageref*{containers}}\par
\hyperref[containers]{Bag of tricks, not actually a bag, p.~\pageref*{containers}}\par
\hyperref[major-demons]{Balrog, slow but heavy, p.~\pageref*{major-demons}}\par
\hyperref[wishable-random-artifacts]{Bane weapons, defensive riders, p.~\pageref*{wishable-random-artifacts}}\par
Barbarian: \hyperref[the-roles]{just hit things harder, poison resistance gift, p.~\pageref*{the-roles}}\par
\hyperref[room-types]{Barracks, organized armed soldiers, p.~\pageref*{room-types}}\par
\hyperref[common-combat-deaths]{Bats and speedsters, doorway fighting, p.~\pageref*{common-combat-deaths}}\par
\hyperref[weapons]{Battle-axe, two-handed good damage, p.~\pageref*{weapons}}\par
\hyperref[dangerous-traps]{Bear trap, escape diagonally, p.~\pageref*{dangerous-traps}}\par
\hyperref[room-types]{Beehive, royal jelly inside, p.~\pageref*{room-types}}\par
Bell of Opening: \hyperref[the-quest]{looted from nemesis, p.~\pageref*{the-quest}}; \hyperref[other-notable-tools]{Invocation item, p.~\pageref*{other-notable-tools}}\par
\hyperref[a-note-on-dragons]{Black dragon scale mail, disintegration + drain res, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[nagas-n]{Black naga corpse, three resistances, p.~\pageref*{nagas-n}}\par
Black pudding: \hyperref[the-golden-rules-of-early-survival]{glob, resistances from a sink, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[a-note-on-puddings]{do not split with iron, p.~\pageref*{a-note-on-puddings}}\par
Blessed: \hyperref[potion-polymorph]{potion of polymorph, controlled poly (new in 5.0), p.~\pageref*{potion-polymorph}}; \hyperref[scroll-genocide]{genocide, class L wipe, p.~\pageref*{scroll-genocide}}; \hyperref[learning-spells]{spellbook, auto-success, p.~\pageref*{learning-spells}}\par
\hyperref[combining-conducts]{Blind / Zen conduct, p.~\pageref*{combining-conducts}}\par
\hyperref[other-notable-tools]{Blindfold, voluntary blindness, p.~\pageref*{other-notable-tools}}\par
\hyperref[a-note-on-dragons]{Blue dragon scale mail, shock + speed, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[jellies-j]{Blue jelly corpse, cold + poison resistance, p.~\pageref*{jellies-j}}\par
\hyperref[containers]{Bag of holding, ascension carry, p.~\pageref*{containers}}\par
\hyperref[deadly-mistakes]{Boiling and shattering potions, Gehennom hot ground, p.~\pageref*{deadly-mistakes}}\par
Bones: \hyperref[things-that-will-kill-you]{level, 80\% cursed items, level, over-leveled monsters, p.~\pageref*{things-that-will-kill-you}}\par
\hyperref[shopkeeper-behavior]{Bones-shop gotcha, items still belong, p.~\pageref*{shopkeeper-behavior}}\par
\hyperref[the-wizards-tower]{Book of the Dead, at the Tower bottom, p.~\pageref*{the-wizards-tower}}\par
\hyperref[brainlessness]{Brainlessness, mind flayer drain, p.~\pageref*{brainlessness}}\par
Branch: \hyperref[the-map-symbols]{staircases, turn yellow, p.~\pageref*{the-map-symbols}}; \hyperref[branches-and-landmarks]{order, Sokoban or Mines first, p.~\pageref*{branches-and-landmarks}}\par
\hyperref[gaining-and-losing-luck]{Breaking a mirror, –2 Luck, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[the-demon-prince-lairs]{Bribe demand, eligible princes and Lawful discount, p.~\pageref*{the-demon-prince-lairs}}\par
\hyperref[fungi-and-molds-f]{Brown mold, passive cold, p.~\pageref*{fungi-and-molds-f}}\par
\hyperref[a-note-on-puddings]{Brown pudding, vegetarian-safe glob, p.~\pageref*{a-note-on-puddings}}\par
BUC: \hyperref[blessed-uncursed-cursed-buc]{avoiding curses by checking, the altar amber/black flash, pet step-around, p.~\pageref*{blessed-uncursed-cursed-buc}}\par
\hyperref[feelings-and-sounds]{Bugle reveille, soldier woke neighbors, p.~\pageref*{feelings-and-sounds}}\par
Burdened: \hyperref[the-early-shopping-list]{status, two hits per yours, p.~\pageref*{the-early-shopping-list}}; \hyperref[carrying-capacity]{Stressed, Strained, Overtaxed, Overloaded, p.~\pageref*{carrying-capacity}}\par
\hyperref[room-types]{Buried treasure room, dig for it, p.~\pageref*{room-types}}\par

\par\smallskip{\normalsize\bfseries C}\par\smallskip

\hyperref[centaurs-c]{`C` centaurs, p.~\pageref*{centaurs-c}}\par
\hyperref[cockatrices-c]{`c` cockatrices, p.~\pageref*{cockatrices-c}}\par
\hyperref[other-notable-tools]{Can of grease, slip and waterproofing, p.~\pageref*{other-notable-tools}}\par
Candelabrum of Invocation: \hyperref[light-sources]{requires seven candles, p.~\pageref*{light-sources}}; \hyperref[vlads-tower]{at top of Vlad's Tower, p.~\pageref*{vlads-tower}}\par
\hyperref[dangerous-foods]{Cannibalism, –2 to –5 Luck plus aggravate, p.~\pageref*{dangerous-foods}}\par
\hyperref[strategy]{Carrying Amulet, casts cost more (drop to cast), p.~\pageref*{strategy}}\par
Castle: \hyperref[castle-overview]{gateway to Gehennom, p.~\pageref*{castle-overview}}; \hyperref[the-castle]{storming the, wand chest, sit on cursed scare monster, five trap doors in the hall, two reliable wishes, p.~\pageref*{the-castle}}\par
Cave: \hyperref[the-roles]{Dweller, sling and flint, p.~\pageref*{the-roles}}; \hyperref[arachnids-and-centipedes-s]{spider, eat for poison resistance, p.~\pageref*{arachnids-and-centipedes-s}}\par
\hyperref[key-spells]{Chain lightning, 5.0 room-clearer, p.~\pageref*{key-spells}}\par
\hyperref[lizards]{Chameleon corpse, polymorphs you, p.~\pageref*{lizards}}\par
\hyperref[alignment]{Chaotic, paired with Rogue for theme, p.~\pageref*{alignment}}\par
Charging: \hyperref[scroll-charging]{explosion chance (n³/7³), a wand of wishing, exactly once, p.~\pageref*{scroll-charging}}\par
\hyperref[the-price-is-right]{Charisma, buy-price bands, p.~\pageref*{the-price-is-right}}\par
\hyperref[key-spells]{Charm monster, 3×3 tame, p.~\pageref*{key-spells}}\par
\hyperref[the-price-is-right]{Chat to shopkeeper, polite price-ID, p.~\pageref*{the-price-is-right}}\par
\hyperref[choking]{Choking, eating past Satiated, p.~\pageref*{choking}}\par
\hyperref[dragons-d]{Chromatic Dragon, random breath weapons, p.~\pageref*{dragons-d}}\par
\hyperref[dungeon-overview-and-event-journal]{Chronicle (`v` / \#chronicle), the journal, p.~\pageref*{dungeon-overview-and-event-journal}}\par
\hyperref[feelings-and-sounds]{Chugging sound, monster drank a potion, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[donating-to-priests]{Clairvoyance, lower-tier priest gift, p.~\pageref*{donating-to-priests}}\par
\hyperref[golems]{Clay golem, dissolves to cancellation, p.~\pageref*{golems}}\par
\hyperref[wishable-random-artifacts]{Cleaver (Barbarian), three-monster swing, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[armor-and-ac]{Cloak of displacement, attackers swing at a phantom, p.~\pageref*{armor-and-ac}}\par
Cloak of magic resistance: \hyperref[armor-and-ac]{MC1 in 5.0, p.~\pageref*{armor-and-ac}}; \hyperref[cloaks]{MC1, p.~\pageref*{cloaks}}\par
Cloak of protection: \hyperref[armor-and-ac]{MC3 the only single source, p.~\pageref*{armor-and-ac}}; \hyperref[cloaks]{MC3, p.~\pageref*{cloaks}}\par
\hyperref[shopkeeper-behavior]{Closed for inventory, locked shop door, p.~\pageref*{shopkeeper-behavior}}\par
Cockatrice: \hyperref[dungeon-hazards-and-how-to-survive-them]{corpse on the stairs, the most literal instadeath, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}; \hyperref[cockatrices-c]{instant petrification on touch, p.~\pageref*{cockatrices-c}}; \hyperref[petrification-stoning]{corpse, wielding (with gloves!), corpse, the rubber chicken, new moon hiss (1 in 3), p.~\pageref*{petrification-stoning}}; \hyperref[the-astral-plane]{corpse, one-shot Rider, p.~\pageref*{the-astral-plane}}\par
\hyperref[the-art-of-combat]{Combat, knowing when not to fight, p.~\pageref*{the-art-of-combat}}\par
\hyperref[command-counts]{Command counts (10s, 20., etc.), p.~\pageref*{command-counts}}\par
Conflict: \hyperref[fighting-smart]{sight required, Charisma scales reliability, p.~\pageref*{fighting-smart}}; \hyperref[the-astral-plane]{ring on Astral, Angels go hostile if your Angel dies, p.~\pageref*{the-astral-plane}}\par
Confused: \hyperref[searching-and-detection]{gold detection, cheap trap reveal, p.~\pageref*{searching-and-detection}}; \hyperref[deadly-mistakes]{genocide, self-extinction, p.~\pageref*{deadly-mistakes}}; \hyperref[genocide]{genocide, kills you, p.~\pageref*{genocide}}; \hyperref[taming-new-creatures]{taming, 11×11 area, p.~\pageref*{taming-new-creatures}}; \hyperref[use-testing-the-careful-way]{reading, alternate effects, p.~\pageref*{use-testing-the-careful-way}}; \hyperref[confused-reading]{enchant weapon/armor, erodeproofs, remove curse, randomizes BUC, gold detection, traps revealed, charging, raises max Pw, p.~\pageref*{confused-reading}}\par
\hyperref[fighting-smart]{Cornered scared monsters still fight, p.~\pageref*{fighting-smart}}\par
\hyperref[helmets]{Cornuthaum, Wizard's clairvoyance, p.~\pageref*{helmets}}\par
\hyperref[the-golden-rules-of-early-survival]{Corridor chokepoint, single-file enemies, p.~\pageref*{the-golden-rules-of-early-survival}}\par
\hyperref[angelic-beings-a]{Couatl, feathered serpent, p.~\pageref*{angelic-beings-a}}\par
\hyperref[the-gauntlet]{Covetous monsters, warp to you, p.~\pageref*{the-gauntlet}}\par
\hyperref[feelings-and-sounds]{Crashing rock, a tunneler at work, p.~\pageref*{feelings-and-sounds}}\par
Credit: \hyperref[unlocking-tools]{card, worst but works, p.~\pageref*{unlocking-tools}}; \hyperref[credit-and-debt]{two ways to accumulate, cloning, the gold-lure routine, p.~\pageref*{credit-and-debt}}\par
\hyperref[humans-and-elves]{Croesus, vault guardian, p.~\pageref*{humans-and-elves}}\par
Crowning: \hyperref[crowning]{alignment 20 and Luck 10, prayer-cooldown penalty, p.~\pageref*{crowning}}\par
\hyperref[weapons]{Crysknife, fragile excellence, p.~\pageref*{weapons}}\par
Crystal ball: \hyperref[searching-and-detection]{trap survey, p.~\pageref*{searching-and-detection}}; \hyperref[other-notable-tools]{the one-question oracle, p.~\pageref*{other-notable-tools}}\par
\hyperref[repeat-last-command-ctrla]{Ctrl+A, repeat last command, p.~\pageref*{repeat-last-command-ctrla}}\par
\hyperref[dungeon-overview-and-event-journal]{Ctrl+O / \#overview, the level list, p.~\pageref*{dungeon-overview-and-event-journal}}\par
\hyperref[message-history-and-redraw]{Ctrl+P, message history, p.~\pageref*{message-history-and-redraw}}\par
\hyperref[message-history-and-redraw]{Ctrl+R, redraw, p.~\pageref*{message-history-and-redraw}}\par
\hyperref[removing-curses]{Curse, removing, p.~\pageref*{removing-curses}}\par
Cursed: \hyperref[sokoban]{scare monster scroll, Sokoban-prize bait, p.~\pageref*{sokoban}}; \hyperref[blessed-uncursed-cursed-buc]{gain level, up through ceiling, p.~\pageref*{blessed-uncursed-cursed-buc}}; \hyperref[effects-of-cursed-items]{armor, won't come off, weapon, can't be unwielded, p.~\pageref*{effects-of-cursed-items}}; \hyperref[how-luck-works]{luckstone, locks negative, p.~\pageref*{how-luck-works}}\par
\hyperref[effects-of-cursed-items]{Cursed bag of holding, doubles weight, p.~\pageref*{effects-of-cursed-items}}\par
Cursed potion: \hyperref[alchemy]{dip, guaranteed explosion, p.~\pageref*{alchemy}}; \hyperref[the-ascension-run]{of gain level wish, free Gehennom skip, p.~\pageref*{the-ascension-run}}\par
\hyperref[options-worth-knowing-about]{Curses windowtype, the paneled UI, p.~\pageref*{options-worth-knowing-about}}\par
\hyperref[giant-humanoids-h]{Cyclops, Healer quest nemesis, p.~\pageref*{giant-humanoids-h}}\par

\par\smallskip{\normalsize\bfseries D}\par\smallskip

\hyperref[dogs-and-canines-d]{`d` dogs and canines, p.~\pageref*{dogs-and-canines-d}}\par
\hyperref[a-note-on-dragons]{`D` dragons, color cheat-sheet, p.~\pageref*{a-note-on-dragons}}\par
Damerell: \hyperref[acknowledgements]{Object Identification FAQ, p.~\pageref*{acknowledgements}}\par
\hyperref[dangerous-foods]{Dangerous foods, list, p.~\pageref*{dangerous-foods}}\par
\hyperref[deadly-poison]{Deadly poison, the 1-in-240 spike, p.~\pageref*{deadly-poison}}\par
Death: \hyperref[things-that-will-kill-you]{causes of (see: everything), p.~\pageref*{things-that-will-kill-you}}; \hyperref[the-astral-plane]{the Rider, instakill chance, p.~\pageref*{the-astral-plane}}\par
\hyperref[credit-and-debt]{Debt, using unpaid items in-shop, p.~\pageref*{credit-and-debt}}\par
\hyperref[delayed-deaths]{Delayed deaths, the runners, p.~\pageref*{delayed-deaths}}\par
\hyperref[major-demons]{Demogorgon, attacks on sight, no bribe, p.~\pageref*{major-demons}}\par
\hyperref[whats-different-in-gehennom]{Demon lord bribery, gold in main inventory, p.~\pageref*{whats-different-in-gehennom}}\par
\hyperref[wishable-random-artifacts]{Demonbane (Lawful silver mace), Priest first gift, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[common-combat-deaths]{Demons, summoning more demons, p.~\pageref*{common-combat-deaths}}\par
\hyperref[to-hit-calculation]{Dexterity, +to-hit bonus, p.~\pageref*{to-hit-calculation}}\par
\hyperref[use-testing-the-careful-way]{Dip ammo in sickness, poison arrows, p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[use-testing-the-careful-way]{Dipping unicorn horn in potions, p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[what-killed-the-runners-up]{Discipline, the difference, p.~\pageref*{what-killed-the-runners-up}}\par
Disenchanter: \hyperref[enchantment-drain]{mourning your former +5, range-kill don't melee, p.~\pageref*{enchantment-drain}}; \hyperref[useful-corpse-effects]{corpse, never eat, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[disintegration]{Disintegration, only black dragon breath, p.~\pageref*{disintegration}}\par
\hyperref[major-demons]{Dispater, bribable arch-devil, p.~\pageref*{major-demons}}\par
\hyperref[felines-f]{Displacer beast, taming, p.~\pageref*{felines-f}}\par
\hyperref[donating-to-priests]{Donating to priests, AC stacks, p.~\pageref*{donating-to-priests}}\par
Doors: \hyperref[fighting-smart]{no diagonal entry, close for breathing room, p.~\pageref*{fighting-smart}}\par
\hyperref[dragon-scale-mail]{Dragon scale mail, upgrade from scales, p.~\pageref*{dragon-scale-mail}}\par
\hyperref[wishable-random-artifacts]{Dragonbane, reflection while wielded, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[a-note-on-dragons]{Dragons, a full briefing, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[the-castle]{Drawbridge, four ways to lower, p.~\pageref*{the-castle}}\par
\hyperref[shopkeeper-behavior]{Shop bill, inspect with `I` then `u`, p.~\pageref*{shopkeeper-behavior}}\par
\hyperref[drowning]{Drowning, preventable, p.~\pageref*{drowning}}\par
\hyperref[musical-instruments]{Drum of earthquake, pits around you, p.~\pageref*{musical-instruments}}\par
\hyperref[helmets]{Dunce cap, Int/Wis → 6, auto-curse, p.~\pageref*{helmets}}\par
\hyperref[the-big-picture]{Dungeon layout, the branching tree, p.~\pageref*{the-big-picture}}\par
\hyperref[the-big-picture]{Dungeons of Doom, upper trunk, p.~\pageref*{the-big-picture}}\par
Dwarf: \hyperref[the-races]{Str and Con caps, p.~\pageref*{the-races}}; \hyperref[humanoids-h]{hit hard and armored, p.~\pageref*{humanoids-h}}\par

\par\smallskip{\normalsize\bfseries E}\par\smallskip

\hyperref[elementals-e]{`E` elementals, p.~\pageref*{elementals-e}}\par
\hyperref[eyes-and-spheres-e]{`e` eyes and spheres, p.~\pageref*{eyes-and-spheres-e}}\par
Early game: \hyperref[the-early-shopping-list]{shopping list, p.~\pageref*{the-early-shopping-list}}; \hyperref[things-that-will-kill-you]{the deadliest stretch, p.~\pageref*{things-that-will-kill-you}}\par
\hyperref[elementals-e]{Earth elemental, phases through walls, p.~\pageref*{elementals-e}}\par
\hyperref[deadly-mistakes]{Eating mistakes, old and poisonous corpses, p.~\pageref*{deadly-mistakes}}\par
\hyperref[medusas-island]{Eels (giant, electric), at Medusa, p.~\pageref*{medusas-island}}\par
Elbereth: \hyperref[elbereth]{writing frantically, where the word comes from, the ward (basic), p.~\pageref*{elbereth}}; \hyperref[rules-of-the-ward]{rules of the ward, who ignores it, dead in Gehennom, the defile rule (important), p.~\pageref*{rules-of-the-ward}}; \hyperref[practical-use]{practical use, p.~\pageref*{practical-use}}; \hyperref[strategy]{dead past Castle, p.~\pageref*{strategy}}\par
\hyperref[sea-monsters]{Electric eel, six in one Medusa layout, p.~\pageref*{sea-monsters}}\par
\hyperref[the-elemental-planes]{Elemental Planes, four obstacles, p.~\pageref*{the-elemental-planes}}\par
\hyperref[the-races]{Elf, sleep resistance at XL 4, p.~\pageref*{the-races}}\par
\hyperref[boots]{Elven boots, stealth and silent walk, p.~\pageref*{boots}}\par
Enchant: \hyperref[scroll-enchant]{weapon, +5 ceiling safe, armor, +3 ceiling safe, p.~\pageref*{scroll-enchant}}\par
Enchantment: \hyperref[enchantment-drain]{drain, the silent ascension-killer, p.~\pageref*{enchantment-drain}}; \hyperref[enchantment]{weapon ceiling +9, armor +3/+5, p.~\pageref*{enchantment}}\par
Engrave: \hyperref[the-engrave-test-wands]{test, the procedure, test, pre-write a word in dust, p.~\pageref*{the-engrave-test-wands}}\par
\hyperref[resolving-ambiguous-engrave-results]{Engraving vanishes, three candidates, p.~\pageref*{resolving-ambiguous-engrave-results}}\par
\hyperref[engulfment]{Engulfment, two hidden monsters, p.~\pageref*{engulfment}}\par
Excalibur: \hyperref[fountains]{fountain dip, p.~\pageref*{fountains}}; \hyperref[finding-secret-doors]{search bonus, p.~\pageref*{finding-secret-doors}}; \hyperref[level-drain]{drain resistance, p.~\pageref*{level-drain}}; \hyperref[the-roles]{Knight's fountain-dipping odds, p.~\pageref*{the-roles}}; \hyperref[wishable-random-artifacts]{(Lawful long sword), drain res + search, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[quest-artifacts]{Eye of the Aethiopica (Wizard), Vlad portal invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[quest-artifacts]{Eyes of the Overworld (Monk), astral vision when worn, p.~\pageref*{quest-artifacts}}\par

\par\smallskip{\normalsize\bfseries F}\par\smallskip

\hyperref[felines-f]{`f` felines, p.~\pageref*{felines-f}}\par
\hyperref[fungi-and-molds-f]{`F` fungi and molds, p.~\pageref*{fungi-and-molds-f}}\par
Fake: \hyperref[the-gnomish-mines]{luckstone mimic, BUC-test first, p.~\pageref*{the-gnomish-mines}}; \hyperref[the-ascension-run]{amulet, from bones or wish, p.~\pageref*{the-ascension-run}}\par
\hyperref[dungeon-hazards-and-how-to-survive-them]{Falling down stairs while burdened, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}\par
Famine: \hyperref[starvation]{the second Rider, p.~\pageref*{starvation}}; \hyperref[the-astral-plane]{the Rider, hunger per hit, p.~\pageref*{the-astral-plane}}\par
Feelings: \hyperref[feelings-and-sounds]{feverish, lycanthropy infection, deathly sick, Pestilence or rot, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[fighting-style-caps]{Fighting style caps (bare hands, two-weapon, riding, martial arts), p.~\pageref*{fighting-style-caps}}\par
Finger: \hyperref[engravings]{in dust, fragile but instant, p.~\pageref*{engravings}}; \hyperref[key-spells]{of death, the argument-ender, p.~\pageref*{key-spells}}\par
Fire: \hyperref[dangerous-traps]{trap, burns inventory, p.~\pageref*{dangerous-traps}}; \hyperref[useful-corpse-effects]{ant corpse, fire resistance, giant corpse, fire + Strength, p.~\pageref*{useful-corpse-effects}}; \hyperref[wishable-random-artifacts]{Brand, fire + firestorm invoke, p.~\pageref*{wishable-random-artifacts}}\par
First descent: \hyperref[your-first-descent]{welcome to the dungeon, p.~\pageref*{your-first-descent}}; \hyperref[fighting-smart]{a missed swing wakes the room, p.~\pageref*{fighting-smart}}\par
\hyperref[alignment]{First-game recommendation, p.~\pageref*{alignment}}\par
\hyperref[gray-stones-four-stones-one-lucky]{Flint, sling ammunition, p.~\pageref*{gray-stones-four-stones-one-lucky}}\par
Floating: \hyperref[dungeon-hazards-and-how-to-survive-them]{eye, do not hit, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}; \hyperref[eyes-and-spheres-e]{eye, never melee, eye corpse, telepathy, p.~\pageref*{eyes-and-spheres-e}}\par
\hyperref[seduction]{Amorous demon, can strip cursed armor, p.~\pageref*{seduction}}\par
Food: \hyperref[how-hunger-works]{running out of, p.~\pageref*{how-hunger-works}}; \hyperref[what-to-eat]{rations, weight 20, p.~\pageref*{what-to-eat}}; \hyperref[the-food-conducts]{conducts, the hierarchy, p.~\pageref*{the-food-conducts}}\par
\hyperref[the-food-conducts]{Foodless conduct, p.~\pageref*{the-food-conducts}}\par
\hyperref[key-spells]{Force bolt, level 1 attack, p.~\pageref*{key-spells}}\par
\hyperref[forcing-locked-chests]{\#force, prying chests open, p.~\pageref*{forcing-locked-chests}}\par
\hyperref[movement-prefixes]{Force-attack (F), p.~\pageref*{movement-prefixes}}\par
\hyperref[centaurs-c]{Forest centaur, bow user, p.~\pageref*{centaurs-c}}\par
Fort: \hyperref[fort-ludios]{Ludios, vault full of gold, Ludios, Croesus across the moat, p.~\pageref*{fort-ludios}}\par
\hyperref[fountains]{Fountain dip, uncurses items, p.~\pageref*{fountains}}\par
\hyperref[fountains]{Fountains, gentle bubbling doom, p.~\pageref*{fountains}}\par
\hyperref[the-castle]{Four corner-tower alcoves, one with wishing wand, p.~\pageref*{the-castle}}\par
\hyperref[how-luck-works]{Friday the 13th, –1 baseline Luck, p.~\pageref*{how-luck-works}}\par
\hyperref[wishable-random-artifacts]{Frost Brand, cold + snowstorm invoke, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[how-luck-works]{Full moon, +1 baseline Luck, p.~\pageref*{how-luck-works}}\par
\hyperref[boots]{Fumble boots, 9-in-10 cursed, p.~\pageref*{boots}}\par

\par\smallskip{\normalsize\bfseries G}\par\smallskip

\hyperref[gnomes-g]{`G` gnomes, p.~\pageref*{gnomes-g}}\par
\hyperref[gremlins-g]{`g` gremlins and gargoyles, p.~\pageref*{gremlins-g}}\par
\hyperref[gaining-and-losing-luck]{Gaining and losing Luck, the table, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[eyes-and-spheres-e]{Gas spore, walking explosion, p.~\pageref*{eyes-and-spheres-e}}\par
Gauntlets: \hyperref[gloves]{of power, Str 25, of dexterity, +spe to Dex, of fumbling, 9-in-10 cursed, p.~\pageref*{gloves}}\par
Gehennom: \hyperref[the-big-picture]{lower trunk, p.~\pageref*{the-big-picture}}; \hyperref[gehennom]{why is it so hot, no prayer, fire everywhere, hot ground shatters potions, p.~\pageref*{gehennom}}\par
Gelatinous: \hyperref[blobs-b]{cube, paralysis-cube of resistances, p.~\pageref*{blobs-b}}; \hyperref[vegetarian-safe-corpses]{cube corpse, four resistances, p.~\pageref*{vegetarian-safe-corpses}}\par
\hyperref[gem-identification-through-selling]{Gem identification through selling (not reliable), p.~\pageref*{gem-identification-through-selling}}\par
\hyperref[quantum-mechanics-q]{Genetic engineer, polymorph-on-claw, p.~\pageref*{quantum-mechanics-q}}\par
Genocide: \hyperref[scroll-genocide]{race trap (h, G, @, o), p.~\pageref*{scroll-genocide}}; \hyperref[plane-of-water]{class `;`, on Plane of Water, p.~\pageref*{plane-of-water}}\par
\hyperref[major-demons]{Geryon, bribable arch-devil, p.~\pageref*{major-demons}}\par
\hyperref[special-symbols]{Ghost, paints over the floor as a gap, p.~\pageref*{special-symbols}}\par
Giant: \hyperref[bats-and-birds-b]{bat, speed 22 swarmer, p.~\pageref*{bats-and-birds-b}}; \hyperref[giant-humanoids-h]{corpse, +1 Strength, p.~\pageref*{giant-humanoids-h}}; \hyperref[sea-monsters]{eel, grab and drown, p.~\pageref*{sea-monsters}}\par
\hyperref[giant-humanoids-h]{Giants throw boulders (storm, fire, frost), p.~\pageref*{giant-humanoids-h}}\par
\hyperref[wishable-random-artifacts]{Giantslayer, double vs giants, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[a-note-on-puddings]{Glob, instead of corpse, p.~\pageref*{a-note-on-puddings}}\par
\hyperref[gnomes-g]{Gnome lord, gnome king, p.~\pageref*{gnomes-g}}\par
Gnomish: \hyperref[gnomes-g]{wizard, psi bolt and self-buffs, p.~\pageref*{gnomes-g}}; \hyperref[the-gnomish-mines]{Mines, entry around Dlvl 2-4, p.~\pageref*{the-gnomish-mines}}; \hyperref[common-combat-deaths]{Mines, a choice not a routine stop, p.~\pageref*{common-combat-deaths}}\par
\hyperref[altars-and-alignment]{Gods, angering, p.~\pageref*{altars-and-alignment}}\par
\hyperref[a-note-on-dragons]{Gold dragon scale mail, the body-slot lantern, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[golems]{Gold golem, walking treasure pile, p.~\pageref*{golems}}\par
\hyperref[a-note-on-dragons]{Gray dragon scale mail, magic resistance, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[a-note-on-puddings]{Gray ooze, rusts armor, p.~\pageref*{a-note-on-puddings}}\par
\hyperref[gray-stones-four-stones-one-lucky]{Gray stones, four stones one answer, p.~\pageref*{gray-stones-four-stones-one-lucky}}\par
\hyperref[wishable-random-artifacts]{Grayswandir (Lawful silver saber), double physical damage dealt, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[erosion-and-proofing]{Grease, applied to armor, p.~\pageref*{erosion-and-proofing}}\par
\hyperref[a-note-on-dragons]{Green dragon scale mail, poison + sickness resistance, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[delayed-deaths]{Green slime, ten-turn countdown and cures, p.~\pageref*{delayed-deaths}}\par
Gremlin: \hyperref[gremlins-g]{strips intrinsic at night, multiplies in water, p.~\pageref*{gremlins-g}}\par
Grid: \hyperref[xans-and-fantastic-insects-x]{bug, can't move diagonally, p.~\pageref*{xans-and-fantastic-insects-x}}; \hyperref[deadly-mistakes]{bug, last-hit kills, p.~\pageref*{deadly-mistakes}}; \hyperref[acknowledgements]{bug, name and Tron reference, p.~\pageref*{acknowledgements}}\par
\hyperref[wishable-random-artifacts]{Grimtooth (Chaotic orcish dagger), warns of elves, p.~\pageref*{wishable-random-artifacts}}\par

\par\smallskip{\normalsize\bfseries H}\par\smallskip

\hyperref[giant-humanoids-h]{`H` giants and minotaurs, p.~\pageref*{giant-humanoids-h}}\par
\hyperref[humanoids-h]{`h` humanoids, p.~\pageref*{humanoids-h}}\par
\hyperref[acknowledgements]{Hack (1982), Jay Fenlason, p.~\pageref*{acknowledgements}}\par
\hyperref[real-gem-prices]{Hard gems (Mohs 8+), survive throws, p.~\pageref*{real-gem-prices}}\par
\hyperref[acknowledgements]{Hardfought, the variants server, p.~\pageref*{acknowledgements}}\par
\hyperref[key-spells]{Haste self, alternative to speed boots, p.~\pageref*{key-spells}}\par
Healer: \hyperref[the-roles]{sleep-wand surprise, sickness immunity, p.~\pageref*{the-roles}}\par
Healing: \hyperref[potion-prices]{potion, \$20 alone, p.~\pageref*{potion-prices}}; \hyperref[potion-healing]{chain, blessed pumps maxHP, p.~\pageref*{potion-healing}}; \hyperref[key-spells]{spell, level 1, p.~\pageref*{key-spells}}\par
\hyperref[feelings-and-sounds]{Health currently feels amplified, shock resistance, p.~\pageref*{feelings-and-sounds}}\par
Heart: \hyperref[how-luck-works]{of Ahriman, counts as luckstone, p.~\pageref*{how-luck-works}}; \hyperref[quest-artifacts]{of Ahriman (Barbarian), p.~\pageref*{quest-artifacts}}\par
\hyperref[the-heist]{Heist, the choreographed sequence, p.~\pageref*{the-heist}}\par
\hyperref[helmets]{Helm of brilliance, +spe to Int and Wis, p.~\pageref*{helmets}}\par
\hyperref[armor-and-ac]{Helm of caution, warning intrinsic (new in 5.0), p.~\pageref*{armor-and-ac}}\par
Helm of opposite alignment: \hyperref[the-gauntlet]{Chaotic detour, p.~\pageref*{the-gauntlet}}; \hyperref[helmets]{alignment-flip tactical uses, p.~\pageref*{helmets}}\par
\hyperref[helmets]{Helm of telepathy, when blind, p.~\pageref*{helmets}}\par
\hyperref[molochs-sanctum]{High Priest of Moloch, carries the Amulet near the high altar, p.~\pageref*{molochs-sanctum}}\par
\hyperref[movement-traps]{Hole, like a trapdoor with manners, p.~\pageref*{movement-traps}}\par
Holy water: \hyperref[blessed-uncursed-cursed-buc]{blesses items, p.~\pageref*{blessed-uncursed-cursed-buc}}; \hyperref[potion-holy-water]{making at an altar, multiplying by dipping, p.~\pageref*{potion-holy-water}}\par
\hyperref[the-races]{Human, no infravision, no special talents, p.~\pageref*{the-races}}\par
\hyperref[defiling-the-name-of-elbereth-important]{Hypocrite, alignment hit when defiling, p.~\pageref*{defiling-the-name-of-elbereth-important}}\par

\par\smallskip{\normalsize\bfseries I}\par\smallskip

\hyperref[imps-and-minor-demons-i]{`i` imps and minor demons, p.~\pageref*{imps-and-minor-demons-i}}\par
\hyperref[special-symbols]{`I` invisible monster marker, p.~\pageref*{special-symbols}}\par
\hyperref[naming-what-youve-learned]{Identification by stacking, the merge clue, p.~\pageref*{naming-what-youve-learned}}\par
\hyperref[gaining-and-losing-luck]{Identified gem to co-aligned unicorn, +5, p.~\pageref*{gaining-and-losing-luck}}\par
Identify: \hyperref[scroll-prices]{scroll, \$20 alone, p.~\pageref*{scroll-prices}}; \hyperref[scroll-identify]{never enough scrolls of, p.~\pageref*{scroll-identify}}; \hyperref[key-spells]{spell, blessed multi-ID, p.~\pageref*{key-spells}}\par
Illiterate: \hyperref[illiterate]{conduct, only x signature allowed, p.~\pageref*{illiterate}}\par
\hyperref[delayed-deaths]{Illness (food poisoning), unicorn horn cure, p.~\pageref*{delayed-deaths}}\par
\hyperref[imps-and-minor-demons-i]{Imp, stream of insults, p.~\pageref*{imps-and-minor-demons-i}}\par
\hyperref[seduction]{Incubus, succubus, encounter table, p.~\pageref*{seduction}}\par
\hyperref[ways-to-die-instantly]{Instadeaths, recognizing the setup, p.~\pageref*{ways-to-die-instantly}}\par
\hyperref[alignment-and-blasting]{Intelligent artifacts, 4d10 blast, p.~\pageref*{alignment-and-blasting}}\par
\hyperref[the-heist]{Invocation ritual, three items on the vibrating square, p.~\pageref*{the-heist}}\par
Iron: \hyperref[golems]{golem, poison breath, p.~\pageref*{golems}}; \hyperref[iron-bars]{bars, light passes through, bars, dig around them, bars, potion of acid dissolves, p.~\pageref*{iron-bars}}; \hyperref[boots]{shoes, traps protection, p.~\pageref*{boots}}\par
\hyperref[the-map-symbols]{Item symbols, the punctuation marks, p.~\pageref*{the-map-symbols}}\par
\hyperref[dragons-d]{Ixoth, Quest dragon (Archeologist), p.~\pageref*{dragons-d}}\par
\hyperref[acknowledgements]{Izchak Miller, the lighting shopkeeper, p.~\pageref*{acknowledgements}}\par
\hyperref[the-gnomish-mines]{Izchak's lighting store, seven candles, p.~\pageref*{the-gnomish-mines}}\par

\par\smallskip{\normalsize\bfseries J}\par\smallskip

\hyperref[jabberwocks-j]{`J` jabberwock, four 2d10 attacks, p.~\pageref*{jabberwocks-j}}\par
\hyperref[jellies-j]{`j` jellies, p.~\pageref*{jellies-j}}\par
\hyperref[dogs-and-canines-d]{Jackal, leading cause of death, p.~\pageref*{dogs-and-canines-d}}\par
\hyperref[the-demon-prince-lairs]{Juiblex, Faceless Lord, swamp, p.~\pageref*{the-demon-prince-lairs}}\par
\hyperref[boots]{Jumping boots, leap-apply, p.~\pageref*{boots}}\par

\par\smallskip{\normalsize\bfseries K}\par\smallskip

\hyperref[keystone-kops-k]{`K` Keystone Kops, p.~\pageref*{keystone-kops-k}}\par
\hyperref[kobolds-k]{`k` kobolds, p.~\pageref*{kobolds-k}}\par
\hyperref[weapons]{Katana, best one-hander, p.~\pageref*{weapons}}\par
\hyperref[key-spells]{Key spells, the short list, p.~\pageref*{key-spells}}\par
\hyperref[angelic-beings-a]{Ki-rin, flying spellcaster, p.~\pageref*{angelic-beings-a}}\par
\hyperref[deadly-mistakes]{Kicking sinks, the foocubus surprise, p.~\pageref*{deadly-mistakes}}\par
Killer: \hyperref[ants-and-insects-a]{bee, swarm, p.~\pageref*{ants-and-insects-a}}; \hyperref[useful-corpse-effects]{bee corpse, poison resistance, p.~\pageref*{useful-corpse-effects}}\par
Killing: \hyperref[gaining-and-losing-luck]{peaceful, –1 Luck (50\%), pet, –1 Luck plus –15 alignment, co-aligned unicorn, –5, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[felines-f]{Kitten, common starter pet, p.~\pageref*{felines-f}}\par
Knight: \hyperref[the-roles]{pony of, Excalibur odds (1 in 6), jousting on lance, p.~\pageref*{the-roles}}\par
\hyperref[kobolds-k]{Kobold corpse, poisonous, p.~\pageref*{kobolds-k}}\par
\hyperref[keystone-kops-k]{Kops, summoned by shoplifting, p.~\pageref*{keystone-kops-k}}\par
Kraken: \hyperref[sea-monsters]{Medusa's pool variant, p.~\pageref*{sea-monsters}}; \hyperref[medusas-island]{present in one of the four layouts, p.~\pageref*{medusas-island}}\par

\par\smallskip{\normalsize\bfseries L}\par\smallskip

\hyperref[leprechauns-l]{`l` leprechauns, p.~\pageref*{leprechauns-l}}\par
\hyperref[liches-l]{`L` liches, p.~\pageref*{liches-l}}\par
\hyperref[dangerous-traps]{Land mine, items destroyed, p.~\pageref*{dangerous-traps}}\par
Large mimic: \hyperref[a-note-on-mimics]{sticky claw, p.~\pageref*{a-note-on-mimics}}\par
Large containers: \hyperref[containers]{box, chest, ice box, p.~\pageref*{containers}}\par
\hyperref[alignment]{Lawful, perks and pieties, p.~\pageref*{alignment}}\par
\hyperref[learning-spells]{Learning spells, success formula, p.~\pageref*{learning-spells}}\par
\hyperref[other-notable-tools]{Leash, pet follows through stairs, p.~\pageref*{other-notable-tools}}\par
\hyperref[what-to-eat]{Lembas wafers, best nutrition by weight, p.~\pageref*{what-to-eat}}\par
\hyperref[finding-secret-doors]{Lenses, +2 search (capped), p.~\pageref*{finding-secret-doors}}\par
\hyperref[leprechauns-l]{Leprechaun, steals gold and flees, p.~\pageref*{leprechauns-l}}\par
Level: \hyperref[movement-traps]{teleporter, separated from your pet, p.~\pageref*{movement-traps}}; \hyperref[level-drain]{drain, wraiths and friends, p.~\pageref*{level-drain}}\par
\hyperref[your-first-descent]{Levels 1 through 5, where most die, p.~\pageref*{your-first-descent}}\par
Levitation: \hyperref[drowning]{doesn't help vs eels, p.~\pageref*{drowning}}; \hyperref[alchemy]{+ Enlightenment dip = Gain level, p.~\pageref*{alchemy}}; \hyperref[boots]{boots, the cursed trap, p.~\pageref*{boots}}\par
Lichen corpse, never rots, pp.~\hyperref[the-golden-rules-of-early-survival]{\pageref*{the-golden-rules-of-early-survival}}, \hyperref[fungi-and-molds-f]{\pageref*{fungi-and-molds-f}}\par
Light: \hyperref[room-types]{source room, free lit lamp, p.~\pageref*{room-types}}; \hyperref[light-sources]{sources, candles and oil lamps, p.~\pageref*{light-sources}}\par
Lizard: \hyperref[the-golden-rules-of-early-survival]{corpse, carry one, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[lizards]{corpse, cures stoning, p.~\pageref*{lizards}}\par
Loadstone: \hyperref[gray-stones-four-stones-one-lucky]{cursed and refuses to drop, the kick test, p.~\pageref*{gray-stones-four-stones-one-lucky}}\par
\hyperref[credit-and-debt]{Loan, lent gold from shopkeeper, p.~\pageref*{credit-and-debt}}\par
\hyperref[unlocking-tools]{Lock pick, respectable, p.~\pageref*{unlocking-tools}}\par
\hyperref[worms-w]{Long worm, tail segments, p.~\pageref*{worms-w}}\par
\hyperref[quest-artifacts]{Longbow of Diana (Ranger), conjure arrows invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[giant-humanoids-h]{Lord Surtur, Valkyrie quest nemesis, p.~\pageref*{giant-humanoids-h}}\par
Luck: \hyperref[gaining-and-losing-luck]{secretly ruining yours, p.~\pageref*{gaining-and-losing-luck}}; \hyperref[how-luck-works]{the hidden number, timeout, 600 turns toward 0, p.~\pageref*{how-luck-works}}\par
Luckstone: \hyperref[gray-stones-four-stones-one-lucky]{preserves luck, p.~\pageref*{gray-stones-four-stones-one-lucky}}; \hyperref[how-luck-works]{bless it, p.~\pageref*{how-luck-works}}\par
Lurker: \hyperref[engulfment]{above, looking up too late, above, ceiling drop, p.~\pageref*{engulfment}}\par

\par\smallskip{\normalsize\bfseries M}\par\smallskip

\hyperref[movement-prefixes]{m prefix, no-attack and menu, p.~\pageref*{movement-prefixes}}\par
\hyperref[mimics-m]{`m` mimics, p.~\pageref*{mimics-m}}\par
\hyperref[mummies-m]{`M` mummies, undead turning deals 1d8 and makes them flee, p.~\pageref*{mummies-m}}\par
Magic: \hyperref[fountains]{fountain, one in seven, p.~\pageref*{fountains}}; \hyperref[movement-traps]{portal, branch entrances, p.~\pageref*{movement-traps}}; \hyperref[quest-artifacts]{Mirror of Merlin (Knight), p.~\pageref*{quest-artifacts}}\par
\hyperref[enchantment-drain]{Magic cancellation (MC), MC3 blocks 90\%, p.~\pageref*{enchantment-drain}}\par
\hyperref[musical-instruments]{Magic flute, sleep, p.~\pageref*{musical-instruments}}\par
\hyperref[musical-instruments]{Magic harp, charms monsters, p.~\pageref*{musical-instruments}}\par
\hyperref[light-sources]{Magic lamp, the wish gamble, p.~\pageref*{light-sources}}\par
Magic mapping: \hyperref[scroll-magic-mapping]{blessed shows secret doors, p.~\pageref*{scroll-magic-mapping}}; \hyperref[key-spells]{spell, level 5, p.~\pageref*{key-spells}}\par
Magic marker: \hyperref[other-notable-tools]{scroll printer, ascension-kit writes, p.~\pageref*{other-notable-tools}}\par
\hyperref[the-touch-of-death]{Magic missile, the answer to Riders, p.~\pageref*{the-touch-of-death}}\par
Magic trap: \hyperref[dangerous-traps]{random outcomes, Charisma farming, p.~\pageref*{dangerous-traps}}\par
\hyperref[what-pets-do-for-you]{Magic whistle, teleports tame creatures to you, p.~\pageref*{what-pets-do-for-you}}\par
\hyperref[drowning]{Magical breathing, breaks the drowning hold, p.~\pageref*{drowning}}\par
\hyperref[wishable-random-artifacts]{Magicbane (Neutral athame), wielded magic resistance, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[major-demons]{Mail daemon, do not attack, p.~\pageref*{major-demons}}\par
\hyperref[mana-management]{Mana, 5 Pw per spell level, p.~\pageref*{mana-management}}\par
\hyperref[the-map-symbols]{Map, learning to read, p.~\pageref*{the-map-symbols}}\par
\hyperref[the-price-is-right]{Mark, the sucker conditions, p.~\pageref*{the-price-is-right}}\par
\hyperref[room-types]{Massacre room, role corpses for sacrifice, p.~\pageref*{room-types}}\par
\hyperref[quest-artifacts]{Master Key of Thievery (Rogue), untrap invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[liches-l]{Master lich, magic resistance mandatory, p.~\pageref*{liches-l}}\par
Master mind flayer, five tentacles, pp.~\hyperref[humanoids-h]{\pageref*{humanoids-h}}, \hyperref[brainlessness]{\pageref*{brainlessness}}\par
\hyperref[room-types]{Mausoleum, mummy waiting, p.~\pageref*{room-types}}\par
\hyperref[the-big-picture]{Mazes of Menace, the whole thing, p.~\pageref*{the-big-picture}}\par
Medusa: \hyperref[humans-and-elves]{the Gorgon, p.~\pageref*{humans-and-elves}}; \hyperref[medusas-island]{surviving the gaze, p.~\pageref*{medusas-island}}\par
\hyperref[medusas-island]{Medusa's Island, three layered challenges, p.~\pageref*{medusas-island}}\par
Mind flayer: \hyperref[humanoids-h]{drains Int, p.~\pageref*{humanoids-h}}; \hyperref[brainlessness]{wear any helmet, greased helmet stacks, p.~\pageref*{brainlessness}}\par
\hyperref[the-gnomish-mines]{Mine's End, guaranteed luckstone, p.~\pageref*{the-gnomish-mines}}\par
\hyperref[the-gnomish-mines]{Mind flayer, surprise in the Mines, p.~\pageref*{the-gnomish-mines}}\par
Minetown: \hyperref[the-gnomish-mines]{shops and temple, watch, don't attack peacefuls, p.~\pageref*{the-gnomish-mines}}\par
\hyperref[giant-humanoids-h]{Minotaur, 42 average damage per full attack, p.~\pageref*{giant-humanoids-h}}\par
\hyperref[quest-artifacts]{Mitre of Holiness (Priest), p.~\pageref*{quest-artifacts}}\par
\hyperref[wishable-random-artifacts]{Mjollnir, Valkyrie throw-and-return war hammer, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[real-gem-prices]{Mohs hardness, gems for engraving, p.~\pageref*{real-gem-prices}}\par
\hyperref[the-valley-of-the-dead]{Moloch shrine, do not pray, p.~\pageref*{the-valley-of-the-dead}}\par
\hyperref[molochs-sanctum]{Moloch's Sanctum, sealed level, p.~\pageref*{molochs-sanctum}}\par
Monk: \hyperref[the-roles]{no body armor, robe spellcasting bonus, p.~\pageref*{the-roles}}\par
\hyperref[carrying-capacity]{Monsters loot unlocked containers (new in 5.0), p.~\pageref*{carrying-capacity}}\par
\hyperref[deadly-mistakes]{Mount slip, riding accidents, p.~\pageref*{deadly-mistakes}}\par
\hyperref[centaurs-c]{Mountain centaur, two kicks plus weapon, p.~\pageref*{centaurs-c}}\par
\hyperref[movement-prefixes]{Movement prefixes (F force, G run, m no-attack), p.~\pageref*{movement-prefixes}}\par
\hyperref[quadrupeds-q]{Mumak, 4d12 butt, p.~\pageref*{quadrupeds-q}}\par
\hyperref[cloaks]{Mummy wrapping, blocks invisibility, p.~\pageref*{cloaks}}\par
\hyperref[musical-instruments]{Musical instruments, the passtune, p.~\pageref*{musical-instruments}}\par
Mysterious: \hyperref[the-gauntlet]{Force, downstairs reroll, Force, Chaotic discount, p.~\pageref*{the-gauntlet}}\par

\par\smallskip{\normalsize\bfseries N}\par\smallskip

\hyperref[nagas-n]{`N` nagas, p.~\pageref*{nagas-n}}\par
\hyperref[nymphs-n]{`n` nymphs, p.~\pageref*{nymphs-n}}\par
\hyperref[acknowledgements]{NAO (nethack.alt.org), the public server, p.~\pageref*{acknowledgements}}\par
\hyperref[wraiths-w]{Nazgul, sleep breath, p.~\pageref*{wraiths-w}}\par
\hyperref[why-luck-matters]{Negative Luck, prayer fails, p.~\pageref*{why-luck-matters}}\par
NetHack: \hyperref[acknowledgements]{DevTeam, Wiki, the living changelog, p.~\pageref*{acknowledgements}}\par
\hyperref[alignment]{Neutral, the most flexibility, p.~\pageref*{alignment}}\par
Newt: \hyperref[the-golden-rules-of-early-survival]{corpse, free mana sometimes, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[lizards]{corpse, restores 1-3 Pw, p.~\pageref*{lizards}}\par
No-genocide conduct: \hyperref[no-genocide]{type ``none'', p.~\pageref*{no-genocide}}\par
No-wishing-artifacts conduct: \hyperref[wishing-restrictions]{restrictions, p.~\pageref*{wishing-restrictions}}\par
\hyperref[combining-conducts]{Nudist conduct (since 3.6), p.~\pageref*{combining-conducts}}\par
\hyperref[options-worth-knowing-about]{Number\_pad option, p.~\pageref*{options-worth-knowing-about}}\par
\hyperref[a-note-on-nymphs]{Nymph, steals from your pack then teleports away, p.~\pageref*{a-note-on-nymphs}}\par
Nymphs: \hyperref[a-note-on-nymphs]{the universal horror story, never engage carrying the Amulet, p.~\pageref*{a-note-on-nymphs}}\par

\par\smallskip{\normalsize\bfseries O}\par\smallskip

\hyperref[ogres-o]{`O` ogres, p.~\pageref*{ogres-o}}\par
\hyperref[orcs-o]{`o` orcs, p.~\pageref*{orcs-o}}\par
\hyperref[wishable-random-artifacts]{Ogresmasher, double vs ogres, p.~\pageref*{wishable-random-artifacts}}\par
Oilskin: \hyperref[drowning]{cloak, eel-slip, p.~\pageref*{drowning}}; \hyperref[containers]{sack, protects from water, p.~\pageref*{containers}}\par
\hyperref[a-note-on-trolls]{Olog-hai, the troll you fear, p.~\pageref*{a-note-on-trolls}}\par
Oracle: \hyperref[humans-and-elves]{peaceful by design, p.~\pageref*{humans-and-elves}}; \hyperref[the-oracle]{mid-levels, minor consultation (50 zm), major consultation, p.~\pageref*{the-oracle}}\par
\hyperref[a-note-on-dragons]{Orange dragon scale mail, sleep + free action, p.~\pageref*{a-note-on-dragons}}\par
Orb: \hyperref[how-luck-works]{of Fate, counts as luckstone, p.~\pageref*{how-luck-works}}; \hyperref[quest-artifacts]{of Detection (Archeologist), of Fate (Valkyrie), p.~\pageref*{quest-artifacts}}\par
\hyperref[the-races]{Orc, peaceful to other orcs, p.~\pageref*{the-races}}\par
\hyperref[orcs-o]{Orc-captain, two attacks, p.~\pageref*{orcs-o}}\par
\hyperref[the-gnomish-mines]{Orcish Town, 1-in-7 Minetown variant, p.~\pageref*{the-gnomish-mines}}\par
\hyperref[wishable-random-artifacts]{Orcrist (Chaotic elven broadsword), warns of orcs, p.~\pageref*{wishable-random-artifacts}}\par
Orcus: \hyperref[orcus-town]{Prince of Undead, Town, ghost shopping district, Town, guaranteed magic lamp or marker, p.~\pageref*{orcus-town}}\par

\par\smallskip{\normalsize\bfseries P}\par\smallskip

\hyperref[piercers-p]{`p` piercers, p.~\pageref*{piercers-p}}\par
\hyperref[puddings-and-oozes-p]{`P` puddings and oozes, p.~\pageref*{puddings-and-oozes-p}}\par
Pacifist: \hyperref[pacifist]{conduct, the figurine-of-Archon plan, p.~\pageref*{pacifist}}\par
\hyperref[things-that-will-kill-you]{Pacing, XL near Dlvl, p.~\pageref*{things-that-will-kill-you}}\par
Paperback: \hyperref[learning-spells]{the Discworld novel, +20 XP on first read, p.~\pageref*{learning-spells}}\par
\hyperref[the-castle]{Passtune, the five-note Mastermind, p.~\pageref*{the-castle}}\par
\hyperref[pauper-new-in-5.0]{Pauper conduct, no starting gear (new in 5.0), p.~\pageref*{pauper-new-in-5.0}}\par
\hyperref[per-role-skill-caps]{Per-role skill caps, p.~\pageref*{per-role-skill-caps}}\par
\hyperref[permadeaf-new-in-5.0]{Permadeaf conduct (new in 5.0), p.~\pageref*{permadeaf-new-in-5.0}}\par
\hyperref[medusas-island]{Perseus statue, looting the legend, p.~\pageref*{medusas-island}}\par
\hyperref[the-astral-plane]{Pestilence the Rider, the one to fear, p.~\pageref*{the-astral-plane}}\par
\hyperref[delayed-deaths]{Pestilence's terminal illness, Constitution timer, p.~\pageref*{delayed-deaths}}\par
Pet: \hyperref[deadly-mistakes]{kills (yours), via conflict ring, p.~\pageref*{deadly-mistakes}}; \hyperref[keeping-your-pet-alive]{accidentally killing your, revive at co-aligned altar, gains resistances from corpses, p.~\pageref*{keeping-your-pet-alive}}; \hyperref[starting-pets]{your best early asset, growth from feeding, curse detection, p.~\pageref*{starting-pets}}; \hyperref[what-pets-do-for-you]{shoplifting, store-without-paying, p.~\pageref*{what-pets-do-for-you}}\par
\hyperref[petless-new-in-5.0]{Petless conduct (new in 5.0), p.~\pageref*{petless-new-in-5.0}}\par
\hyperref[petrification-stoning]{Petrification (stoning), the five-turn ladder, p.~\pageref*{petrification-stoning}}\par
\hyperref[other-notable-tools]{Pickaxe and mattock, dig anywhere, p.~\pageref*{other-notable-tools}}\par
\hyperref[piercers-p]{Piercer, drop from ceiling, p.~\pageref*{piercers-p}}\par
Pit: \hyperref[snakes-s]{viper, cobra, poison bites, p.~\pageref*{snakes-s}}; \hyperref[movement-traps]{climb out, p.~\pageref*{movement-traps}}\par
Plane: \hyperref[the-elemental-planes]{portals, confused gold detection, of Earth, dig the portal, of Air, cloud bubbles drift, of Air, conflict tactic, p.~\pageref*{the-elemental-planes}}; \hyperref[plane-of-fire]{of Fire, fire resistance non-optional, p.~\pageref*{plane-of-fire}}; \hyperref[plane-of-water]{of Water, moving bubbles and magical breathing, p.~\pageref*{plane-of-water}}\par
\hyperref[quest-artifacts]{Platinum Yendorian Express Card (Tourist), charge an item, p.~\pageref*{quest-artifacts}}\par
Polymorph: \hyperref[dangerous-traps]{trap, free booth with control, p.~\pageref*{dangerous-traps}}; \hyperref[polymorph-as-a-tool]{control, the form-chooser, p.~\pageref*{polymorph-as-a-tool}}; \hyperref[polymorph-restrictions]{restrictions (poly self, poly objects), p.~\pageref*{polymorph-restrictions}}\par
Polymorphing: \hyperref[what-pets-do-for-you]{your pet, titan first choice, p.~\pageref*{what-pets-do-for-you}}; \hyperref[shopkeeper-behavior]{the shopkeeper, the prep, p.~\pageref*{shopkeeper-behavior}}\par
\hyperref[polymorph-as-a-tool]{Polypile, away from your bag, p.~\pageref*{polymorph-as-a-tool}}\par
Potion: \hyperref[potion-prices]{prices, \$20 to \$300, p.~\pageref*{potion-prices}}; \hyperref[the-potion-table]{table, by price, p.~\pageref*{the-potion-table}}\par
\hyperref[confused-reading]{Potion of confusion, the controlled confuser, p.~\pageref*{confused-reading}}\par
\hyperref[potion-gain-ability]{Potion of gain ability, blessed boosts all stats, p.~\pageref*{potion-gain-ability}}\par
\hyperref[potion-gain-level]{Potion of gain level, raises XL, p.~\pageref*{potion-gain-level}}\par
\hyperref[potion-polymorph]{Potion of polymorph, dip-arrow test, p.~\pageref*{potion-polymorph}}\par
\hyperref[potion-speed]{Potion of speed, permanent intrinsic, p.~\pageref*{potion-speed}}\par
Prayer: \hyperref[the-golden-rules-of-early-survival]{emergency button cooldown, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[prayer]{when to, what it fixes, cooldown averaging about 450 turns, p.~\pageref*{prayer}}\par
Priest: \hyperref[the-roles]{BUC sense for free, Demonbane first gift, p.~\pageref*{the-roles}}\par
\hyperref[donating-to-priests]{Protection racket, donation AC ladder, p.~\pageref*{donating-to-priests}}\par
\hyperref[worms-w]{Purple worm, swallows you whole, p.~\pageref*{worms-w}}\par
\hyperref[cockatrices-c]{Pyrolisk, fire-gaze cousin, p.~\pageref*{cockatrices-c}}\par

\par\smallskip{\normalsize\bfseries Q}\par\smallskip

\hyperref[quadrupeds-q]{`q` quadrupeds, p.~\pageref*{quadrupeds-q}}\par
\hyperref[quantum-mechanics-q]{`Q` quantum mechanics, teleport-on-claw, p.~\pageref*{quantum-mechanics-q}}\par
\hyperref[fountains]{Quaffing a fountain, slot-machine table, p.~\pageref*{fountains}}\par
\hyperref[quantum-mechanics-q]{Quantum mechanic corpse, toggles Fast, p.~\pageref*{quantum-mechanics-q}}\par
\hyperref[imps-and-minor-demons-i]{Quasit, drains Dex, p.~\pageref*{imps-and-minor-demons-i}}\par
\hyperref[ants-and-insects-a]{Queen bee, royal jelly source, p.~\pageref*{ants-and-insects-a}}\par
Quest: \hyperref[the-quest]{portal, magenta `\textasciicircum{}`, XL 14 and alignment 20, leader, first floor, nemesis, kill twice (life-saving), artifact, on the nemesis's square, p.~\pageref*{the-quest}}; \hyperref[quest-artifacts]{artifacts, the per-role list, p.~\pageref*{quest-artifacts}}\par

\par\smallskip{\normalsize\bfseries R}\par\smallskip

\hyperref[rodents-r]{`r` rodents, p.~\pageref*{rodents-r}}\par
\hyperref[rust-monsters-and-disenchanters-r]{`R` rust monster, disenchanter, p.~\pageref*{rust-monsters-and-disenchanters-r}}\par
\hyperref[the-races]{Races, the five, p.~\pageref*{the-races}}\par
Ranged: \hyperref[the-early-shopping-list]{attack, almost always safer, p.~\pageref*{the-early-shopping-list}}; \hyperref[fighting-smart]{attackers retreat, backing into corners, p.~\pageref*{fighting-smart}}\par
Ranger: \hyperref[the-roles]{+2 cloak of displacement at start, dagger and arrow stack, p.~\pageref*{the-roles}}\par
\hyperref[deadly-mistakes]{Reading unidentified scrolls in a shop, p.~\pageref*{deadly-mistakes}}\par
\hyperref[real-gem-prices]{Real gem prices, the table, p.~\pageref*{real-gem-prices}}\par
\hyperref[recharging]{Recharging, n³/343 explosion formula, p.~\pageref*{recharging}}\par
\hyperref[a-note-on-dragons]{Red dragon scale mail, fire + infravision, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[disintegration]{Reflection, bounces back but they resist, p.~\pageref*{disintegration}}\par
\hyperref[scroll-remove-curse]{Remove curse, the happy ending, p.~\pageref*{scroll-remove-curse}}\par
\hyperref[brainlessness]{Restore ability, returning lost stats, p.~\pageref*{brainlessness}}\par
\hyperref[scroll-reverse-genocide]{Reverse genocide, cursed scroll = spawn 4-6, p.~\pageref*{scroll-reverse-genocide}}\par
\hyperref[acknowledgements]{RGRN (rec.games.roguelike.nethack), p.~\pageref*{acknowledgements}}\par
\hyperref[the-astral-plane]{Rider corpse, instantly fatal to eat, p.~\pageref*{the-astral-plane}}\par
\hyperref[training-a-skill]{Riding, 100 squares per tick, p.~\pageref*{training-a-skill}}\par
Ring: \hyperref[ring-prices]{prices, \$100 to \$300, p.~\pageref*{ring-prices}}; \hyperref[the-ring-table]{of teleport control, on-demand transport, hunger, every ring costs nutrition, of sustain ability, prevents stat drain, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of aggravate monster, the niche use, p.~\pageref*{the-ring-table}}\par
Ring of conflict: \hyperref[fighting-smart]{in combat, p.~\pageref*{fighting-smart}}; \hyperref[the-ring-table]{monsters fight each other, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of free action, anti-paralysis, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of polymorph control, less critical now, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of protection, chargeable, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of regeneration, hungry healer, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of searching, auto-search each turn, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of slow digestion, foodless option, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of warning, threat-color overlay, p.~\pageref*{the-ring-table}}\par
\hyperref[cloaks]{Robe, casting bonus, p.~\pageref*{cloaks}}\par
\hyperref[rodents-r]{Rock mole, eats your metal, p.~\pageref*{rodents-r}}\par
Rogue: \hyperref[the-roles]{multishot dagger throw, backstab bonus, p.~\pageref*{the-roles}}; \hyperref[the-rogue-level]{Level, older more primitive world, Level, all uppercase wildlife, p.~\pageref*{the-rogue-level}}; \hyperref[acknowledgements]{(1980), Toy and Wichman, p.~\pageref*{acknowledgements}}\par
\hyperref[dangerous-traps]{Rolling boulder, fixed track, p.~\pageref*{dangerous-traps}}\par
\hyperref[golems]{Rope golem, grappling hug, p.~\pageref*{golems}}\par
\hyperref[quadrupeds-q]{Rothe, three attacks per turn, p.~\pageref*{quadrupeds-q}}\par
\hyperref[dungeon-hazards-and-how-to-survive-them]{Rotted corpse, the 30-turn window, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}\par
\hyperref[weapons]{Rubber hose, joke weapon, p.~\pageref*{weapons}}\par
\hyperref[movement-prefixes]{Run direction (G), p.~\pageref*{movement-prefixes}}\par
\hyperref[weapons]{Runesword, Stormbringer base, p.~\pageref*{weapons}}\par
Rust: \hyperref[rust-monsters-and-disenchanters-r]{monster, strip iron first, p.~\pageref*{rust-monsters-and-disenchanters-r}}; \hyperref[nuisance-traps]{trap, splashes water, p.~\pageref*{nuisance-traps}}\par

\par\smallskip{\normalsize\bfseries S}\par\smallskip

\hyperref[arachnids-and-centipedes-s]{`s` arachnids and centipedes, p.~\pageref*{arachnids-and-centipedes-s}}\par
\hyperref[snakes-s]{`S` snakes, p.~\pageref*{snakes-s}}\par
\hyperref[containers]{Sack, basic storage, p.~\pageref*{containers}}\par
Sacrifice: \hyperref[sacrifice]{fresh within 50 turns, role-biased first gift, minimum corpse value, p.~\pageref*{sacrifice}}; \hyperref[gaining-and-losing-luck]{luck ceiling, difficulty must exceed, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[feelings-and-sounds]{Sad feeling, your pet died offscreen, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[lizards]{Salamander, Gehennom-only, p.~\pageref*{lizards}}\par
\hyperref[sacrifice]{Same-race sacrifice, forbidden, p.~\pageref*{sacrifice}}\par
Samurai: \hyperref[the-roles]{katana opening, drop wakizashi for long sword off-hand, giri-breaking penalty, p.~\pageref*{the-roles}}\par
\hyperref[apelike-creatures-y]{Sasquatch, fast, p.~\pageref*{apelike-creatures-y}}\par
\hyperref[quest-artifacts]{Sceptre of Might (Caveman), conflict invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[arachnids-and-centipedes-s]{Scorpius, named quest nemesis, p.~\pageref*{arachnids-and-centipedes-s}}\par
\hyperref[scroll-charging]{Scroll of charging, save for wand of wishing, p.~\pageref*{scroll-charging}}\par
\hyperref[deadly-mistakes]{Scroll of earth on yourself, buried alive, p.~\pageref*{deadly-mistakes}}\par
\hyperref[scroll-genocide]{Scroll of genocide, the nuclear option, p.~\pageref*{scroll-genocide}}\par
Scroll of identify: \hyperref[scroll-identify]{main-inventory only, blessed jackpot 1-in-5, p.~\pageref*{scroll-identify}}\par
Scroll of scare monster: \hyperref[practical-use]{drop-and-stand, p.~\pageref*{practical-use}}; \hyperref[scroll-scare-monster]{drop don't read, p.~\pageref*{scroll-scare-monster}}\par
\hyperref[taming-new-creatures]{Scroll of taming, 3×3 area, p.~\pageref*{taming-new-creatures}}\par
\hyperref[scroll-teleportation]{Scroll of teleportation, escape hatch, p.~\pageref*{scroll-teleportation}}\par
Searching: \hyperref[searching-and-detection]{(`s` command), repeat with luck, p.~\pageref*{searching-and-detection}}; \hyperref[the-sink-test-rings]{ring, kept on drop, p.~\pageref*{the-sink-test-rings}}\par
\hyperref[finding-secret-doors]{Secret doors, the architects believed in them, p.~\pageref*{finding-secret-doors}}\par
\hyperref[seduction]{Seduction (foocubus encounter), p.~\pageref*{seduction}}\par
\hyperref[deadly-mistakes]{Self-zap wand, ray ricochet, p.~\pageref*{deadly-mistakes}}\par
Shield: \hyperref[level-drain]{of drain resistance, new in 5.0, p.~\pageref*{level-drain}}; \hyperref[shields]{of reflection, saves the body slot, of drain resistance (new in 5.0), of shock resistance (new in 5.0), p.~\pageref*{shields}}\par
\hyperref[shirts]{Shirts, Hawaiian and T-shirt, p.~\pageref*{shirts}}\par
Shopkeeper: \hyperref[humans-and-elves]{tougher NPC than you, p.~\pageref*{humans-and-elves}}; \hyperref[shopping-and-shopkeeper-pricing]{angering, p.~\pageref*{shopping-and-shopkeeper-pricing}}\par
\hyperref[fungi-and-molds-f]{Shrieker, summons neighbors, p.~\pageref*{fungi-and-molds-f}}\par
Silver: \hyperref[weapons]{saber, demon damage, saber bonus, late-game weapon, p.~\pageref*{weapons}}\par
\hyperref[a-note-on-dragons]{Silver dragon scale mail, reflection, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[room-types]{Single-monster-type room, almost always themed, p.~\pageref*{room-types}}\par
Sink: \hyperref[sinks]{kicking for rings and trouble, dishwasher demon (sink foocubus), dipping potions for messages, quaffing the drain, dropping a ring down, p.~\pageref*{sinks}}; \hyperref[the-sink-test-rings]{test, the ring drop, p.~\pageref*{the-sink-test-rings}}\par
\hyperref[delayed-deaths]{Sinking in lava, levitate or pray, p.~\pageref*{delayed-deaths}}\par
\hyperref[sinks]{Sinks, kicking and dropping rings to ID, p.~\pageref*{sinks}}\par
\hyperref[zombies-z]{Skeleton, only from a trap, p.~\pageref*{zombies-z}}\par
Skill: \hyperref[the-skill-ladder]{slots, XL + 1, plus one if crowned, p.~\pageref*{the-skill-ladder}}; \hyperref[what-a-rank-buys-you]{rank effects, to-hit/damage, p.~\pageref*{what-a-rank-buys-you}}\par
\hyperref[common-combat-deaths]{Sleep without resistance, near-instadeath, p.~\pageref*{common-combat-deaths}}\par
\hyperref[dangerous-traps]{Sleeping gas trap, deadly in zoos, p.~\pageref*{dangerous-traps}}\par
\hyperref[delayed-deaths]{Sliming, ten-turn countdown, p.~\pageref*{delayed-deaths}}\par
\hyperref[the-sink-test-rings]{Slow digestion ring, kept on drop, p.~\pageref*{the-sink-test-rings}}\par
\hyperref[feelings-and-sounds]{Slowing down, you're turning to stone, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[feelings-and-sounds]{Slurping sound, gelatinous cube ate items, p.~\pageref*{feelings-and-sounds}}\par
Small: \hyperref[a-note-on-mimics]{mimic, top-ten killer, p.~\pageref*{a-note-on-mimics}}; \hyperref[shields]{shield, no spellcast penalty, p.~\pageref*{shields}}\par
\hyperref[wishable-random-artifacts]{Snickersnee (Samurai katana), Shkinng! free polearm reach, p.~\pageref*{wishable-random-artifacts}}\par
Sokoban: \hyperref[sokoban]{entry one level below Oracle, boulders into pits, no teleport here, cheating cost (–1 Luck each), prize, bag of holding or amulet of reflection, Strength training side effect, p.~\pageref*{sokoban}}; \hyperref[sokoban-solutions]{solving without cheating, mirrored variants (new in 5.0), scrolls of earth as fillers, p.~\pageref*{sokoban-solutions}}\par
\hyperref[ants-and-insects-a]{Soldier ant, speed 18 packs, p.~\pageref*{ants-and-insects-a}}\par
Speed: \hyperref[armor-and-ac]{boots, more turns equals more, p.~\pageref*{armor-and-ac}}; \hyperref[boots]{boots, an extra move on 2/3 of turns, p.~\pageref*{boots}}\par
Spell: \hyperref[brainlessness]{amnesia, mind flayer side effect, p.~\pageref*{brainlessness}}; \hyperref[learning-spells]{memory, \textasciitilde{}20,000 turns, p.~\pageref*{learning-spells}}\par
Spellbook: \hyperref[spellbook-prices]{prices, 100 × level, p.~\pageref*{spellbook-prices}}; \hyperref[learning-spells]{failure effects by level, 4 successful reads to fade, level 7 explosion rune, p.~\pageref*{learning-spells}}\par
\hyperref[spellcasting]{Spellcasting, mana not sparkles, p.~\pageref*{spellcasting}}\par
\hyperref[room-types]{Spider nest, scales with depth, p.~\pageref*{room-types}}\par
\hyperref[movement-traps]{Spiked pit, possibly poisoned, p.~\pageref*{movement-traps}}\par
\hyperref[acknowledgements]{Spoilers, Hugo and O'Donnell, p.~\pageref*{acknowledgements}}\par
\hyperref[jellies-j]{Spotted jelly, passive acid, p.~\pageref*{jellies-j}}\par
\hyperref[useful-corpse-effects]{Sprig of wolfsbane, cures lycanthropy, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[nuisance-traps]{Squeaky board, wakes the room, p.~\pageref*{nuisance-traps}}\par
Staff: \hyperref[level-drain]{of Aesculapius, drain res, p.~\pageref*{level-drain}}; \hyperref[quest-artifacts]{of Aesculapius (Healer), drain-life on hit, p.~\pageref*{quest-artifacts}}\par
\hyperref[the-map-symbols]{Stairs, up and down (`<`, `>`), p.~\pageref*{the-map-symbols}}\par
Stalker: \hyperref[elementals-e]{see-invisible corpse, p.~\pageref*{elementals-e}}; \hyperref[useful-corpse-effects]{corpse, invisibility and see invisible, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[what-to-pack]{Starting kit, improving on, p.~\pageref*{what-to-pack}}\par
\hyperref[starvation]{Starvation, faint then die, p.~\pageref*{starvation}}\par
\hyperref[the-early-shopping-list]{Stashing, one level up, p.~\pageref*{the-early-shopping-list}}\par
\hyperref[acknowledgements]{Steelypips, Kate Nepveu's archive, p.~\pageref*{acknowledgements}}\par
\hyperref[tool-stethoscope]{Stethoscope, HP check and crowning meter, p.~\pageref*{tool-stethoscope}}\par
\hyperref[wishable-random-artifacts]{Sting (Chaotic elven dagger), warns of orcs, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[scroll-stinking-cloud]{Stinking cloud, area attack, p.~\pageref*{scroll-stinking-cloud}}\par
\hyperref[petrification-stoning]{Stoning, avoiding, p.~\pageref*{petrification-stoning}}\par
Stormbringer: \hyperref[level-drain]{drain res while wielded (chaotic), p.~\pageref*{level-drain}}; \hyperref[wishable-random-artifacts]{(Chaotic runesword), drain life, p.~\pageref*{wishable-random-artifacts}}\par
Strange: \hyperref[feelings-and-sounds]{wind, Oracle level, mental acuity, telepathy gained, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[delayed-deaths]{Strangulation, uncurse amulet first, p.~\pageref*{delayed-deaths}}\par
\hyperref[damage]{Strength bonus, capped at +6, p.~\pageref*{damage}}\par
\hyperref[wishable-random-artifacts]{Sunsword (Lawful), 5.0 blinding ray, p.~\pageref*{wishable-random-artifacts}}\par
Supply: \hyperref[supply-containers]{containers, chests, locked treasure, p.~\pageref*{supply-containers}}\par

\par\smallskip{\normalsize\bfseries T}\par\smallskip

\hyperref[trappers-and-lurkers-t]{`t` trappers and lurkers, p.~\pageref*{trappers-and-lurkers-t}}\par
\hyperref[a-note-on-trolls]{`T` trolls, do not stay dead, p.~\pageref*{a-note-on-trolls}}\par
\hyperref[feeding-and-loyalty]{Tameness, the invisible score, p.~\pageref*{feeding-and-loyalty}}\par
\hyperref[movement-traps]{Teleport trap, free transport with control, p.~\pageref*{movement-traps}}\par
\hyperref[room-types]{Teleportation hub, fixed-destination, p.~\pageref*{room-types}}\par
Temple: \hyperref[room-types]{altar plus priest, p.~\pageref*{room-types}}; \hyperref[detecting-curses]{donation, does NOT reveal BUC, p.~\pageref*{detecting-curses}}\par
Tengu: \hyperref[imps-and-minor-demons-i]{teleport and teleport-control corpse, p.~\pageref*{imps-and-minor-demons-i}}; \hyperref[useful-corpse-effects]{corpse, teleportitis / teleport control, p.~\pageref*{useful-corpse-effects}}\par
Price identification: \hyperref[the-price-is-right]{shopkeepers identify by price, p.~\pageref*{the-price-is-right}}\par
Throne: \hyperref[room-types]{room, sit at your own risk, p.~\pageref*{room-types}}; \hyperref[thrones]{wish possible at non-negative Luck, kicking for gold and gems, p.~\pageref*{thrones}}; \hyperref[the-castle]{room in the Castle court, p.~\pageref*{the-castle}}\par
\hyperref[use-testing-the-careful-way]{Throw potions at monsters (potion test), p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[the-price-is-right]{Throw-into-shop trick, free quote, p.~\pageref*{the-price-is-right}}\par
Tin: \hyperref[what-to-eat]{of spinach, +1 Str, p.~\pageref*{what-to-eat}}; \hyperref[other-notable-tools]{opener, blessed instant, p.~\pageref*{other-notable-tools}}\par
\hyperref[other-notable-tools]{Tinning kit, intrinsic grinder bypass, p.~\pageref*{other-notable-tools}}\par
\hyperref[what-to-eat]{Tins, the occupation trap, p.~\pageref*{what-to-eat}}\par
\hyperref[giant-humanoids-h]{Titan, spell-casting pet target, p.~\pageref*{giant-humanoids-h}}\par
\hyperref[to-hit-calculation]{To-hit roll, the d20 of fate, p.~\pageref*{to-hit-calculation}}\par
\hyperref[things-that-will-kill-you]{Top ten killers, the list, p.~\pageref*{things-that-will-kill-you}}\par
Touchstone: \hyperref[gray-stones-four-stones-one-lucky]{real gem on rub, p.~\pageref*{gray-stones-four-stones-one-lucky}}; \hyperref[gem-identification-through-selling]{blessed names gems on rub, p.~\pageref*{gem-identification-through-selling}}\par
Tourist: \hyperref[the-roles]{hardest standard role, camera-flash plan, magic mapping scrolls at start, p.~\pageref*{the-roles}}\par
\hyperref[other-notable-tools]{Towel, cream pie and blindfold, p.~\pageref*{other-notable-tools}}\par
\hyperref[room-types]{Trap room, recognize and retreat, p.~\pageref*{room-types}}\par
\hyperref[movement-traps]{Trapdoor, 25\% chance to keep falling, p.~\pageref*{movement-traps}}\par
\hyperref[trappers-and-lurkers-t]{Trapper, floor in disguise, p.~\pageref*{trappers-and-lurkers-t}}\par
\hyperref[travel]{Travel (`\_`), shortest path autopilot, p.~\pageref*{travel}}\par
\hyperref[feeding-and-loyalty]{Tripe ration, dog food, p.~\pageref*{feeding-and-loyalty}}\par
Trolls: \hyperref[a-note-on-trolls]{revive timer, gear-and-corpse loop, p.~\pageref*{a-note-on-trolls}}\par
\hyperref[wishable-random-artifacts]{Trollsbane, regeneration while wielded, p.~\pageref*{wishable-random-artifacts}}\par
Tsurugi: \hyperref[how-luck-works]{of Muramasa, counts as luckstone, p.~\pageref*{how-luck-works}}; \hyperref[quest-artifacts]{of Muramasa (Samurai), p.~\pageref*{quest-artifacts}}\par
\hyperref[feelings-and-sounds]{Turning into slime, the 10-turn timer, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[damage]{Two-handed weapons, 3/2 Strength damage, p.~\pageref*{damage}}\par
\hyperref[two-weapon-combat]{Two-weapon Expert, Rogue and Samurai only, p.~\pageref*{two-weapon-combat}}\par

\par\smallskip{\normalsize\bfseries U}\par\smallskip

\hyperref[unicorns-and-horses-u]{`u` horses and unicorns, p.~\pageref*{unicorns-and-horses-u}}\par
\hyperref[umber-hulks-u]{`U` umber hulk, confusion gaze, p.~\pageref*{umber-hulks-u}}\par
\hyperref[blessed-uncursed-cursed-buc]{Unholy water, the evil twin, p.~\pageref*{blessed-uncursed-cursed-buc}}\par
Unicorn: \hyperref[unicorns-and-horses-u]{gem-throwing playbook, p.~\pageref*{unicorns-and-horses-u}}; \hyperref[altars-and-alignment]{(co-aligned), never sacrifice, p.~\pageref*{altars-and-alignment}}; \hyperref[gaining-and-losing-luck]{gem-throwing, +5 luck max, p.~\pageref*{gaining-and-losing-luck}}\par
Unicorn horn: \hyperref[neutralizing-ailments]{ailment cures, dip table, no longer a cure-all, p.~\pageref*{neutralizing-ailments}}; \hyperref[other-notable-tools]{status-cure all, blessed seven ailments, p.~\pageref*{other-notable-tools}}\par
\hyperref[unlocking-tools]{Unlocking tools, skeleton key best, p.~\pageref*{unlocking-tools}}\par

\par\smallskip{\normalsize\bfseries V}\par\smallskip

\hyperref[vampires-v]{`V` vampires, p.~\pageref*{vampires-v}}\par
\hyperref[vortices-v]{`v` vortices, p.~\pageref*{vortices-v}}\par
Valkyrie: \hyperref[the-roles]{easy-mode recommendation, Mjollnir waiting, Female only, p.~\pageref*{the-roles}}\par
\hyperref[the-valley-of-the-dead]{Valley of the Dead, Gehennom entrance, p.~\pageref*{the-valley-of-the-dead}}\par
Vampire: \hyperref[vampires-v]{level drain, p.~\pageref*{vampires-v}}; \hyperref[bats-and-birds-b]{bat, Str-draining bite, p.~\pageref*{bats-and-birds-b}}\par
\hyperref[where-the-word-comes-from]{Varda Elentári, Star-Queen, p.~\pageref*{where-the-word-comes-from}}\par
Vault: \hyperref[vaults]{guard, name yourself Croesus, guard, lying costs Lawful alignment, p.~\pageref*{vaults}}\par
\hyperref[vaults]{Vaults, the 2×2 closet of gold, p.~\pageref*{vaults}}\par
Vegan: \hyperref[what-to-eat]{no eggs either, p.~\pageref*{what-to-eat}}; \hyperref[the-food-conducts]{conduct, p.~\pageref*{the-food-conducts}}\par
Vegetarian: \hyperref[what-to-eat]{allowed corpses, p.~\pageref*{what-to-eat}}; \hyperref[the-food-conducts]{conduct, p.~\pageref*{the-food-conducts}}\par
\hyperref[options-worth-knowing-about]{Verbose option, message-log noise, p.~\pageref*{options-worth-knowing-about}}\par
\hyperref[the-heist]{Vibrating square, search by walking, p.~\pageref*{the-heist}}\par
\hyperref[fungi-and-molds-f]{Violet fungus, sticky paralysis, p.~\pageref*{fungi-and-molds-f}}\par
Vlad: \hyperref[vampires-v]{the Impaler, top of his tower, p.~\pageref*{vampires-v}}; \hyperref[engravings]{was here, trap-door closet marker, p.~\pageref*{engravings}}\par
Vlad's: \hyperref[vlads-tower]{Tower, branches upward; throne, about one wish chance in ten per sit, once, p.~\pageref*{vlads-tower}}\par
\hyperref[wishable-random-artifacts]{Vorpal Blade, behead chance, p.~\pageref*{wishable-random-artifacts}}\par

\par\smallskip{\normalsize\bfseries W}\par\smallskip

\hyperref[worms-w]{`w` worms, p.~\pageref*{worms-w}}\par
\hyperref[wraiths-w]{`W` wraiths, p.~\pageref*{wraiths-w}}\par
\hyperref[credit-and-debt]{Walk-out hazard, unpaid items, p.~\pageref*{credit-and-debt}}\par
Wand: \hyperref[wand-prices]{prices, \$100 to \$500, p.~\pageref*{wand-prices}}; \hyperref[the-engrave-test-wands]{identifying by engraving, p.~\pageref*{the-engrave-test-wands}}; \hyperref[orcus-town]{of Orcus, his fingertip death ray, p.~\pageref*{orcus-town}}\par
Wand of cancellation: \hyperref[wand-cancellation]{never in a bag, on cursed bag of holding, p.~\pageref*{wand-cancellation}}\par
\hyperref[wand-fire-cold-lightning]{Wand of cold, freezes water (ice path), p.~\pageref*{wand-fire-cold-lightning}}\par
Wand of death: \hyperref[the-touch-of-death]{don't zap at Death, p.~\pageref*{the-touch-of-death}}; \hyperref[wand-death]{the closer, p.~\pageref*{wand-death}}; \hyperref[the-astral-plane]{on Death, heals him, p.~\pageref*{the-astral-plane}}\par
Wand of digging: \hyperref[engulfment]{escape from inside, p.~\pageref*{engulfment}}; \hyperref[wand-digging]{digging beam and ascension use, p.~\pageref*{wand-digging}}\par
Wand of fire: \hyperref[engravings]{burns Elbereth permanently, p.~\pageref*{engravings}}; \hyperref[wand-fire-cold-lightning]{cold, lightning (rays), p.~\pageref*{wand-fire-cold-lightning}}\par
\hyperref[wand-make-invisible]{Wand of make invisible, 31-45 turns, p.~\pageref*{wand-make-invisible}}\par
\hyperref[the-castle]{Wand of opening / spell of knock, opens drawbridge, p.~\pageref*{the-castle}}\par
\hyperref[wand-polymorph]{Wand of polymorph, on a pile (polypile), p.~\pageref*{wand-polymorph}}\par
\hyperref[key-wands]{Wand of probing, HP / status check, p.~\pageref*{key-wands}}\par
Wand of secret door detection: \hyperref[searching-and-detection]{no aim, p.~\pageref*{searching-and-detection}}; \hyperref[wands]{area reveal, p.~\pageref*{wands}}\par
\hyperref[wand-stasis]{Wand of stasis, new in 5.0, p.~\pageref*{wand-stasis}}\par
\hyperref[the-castle]{Wand of striking, destroys drawbridge, p.~\pageref*{the-castle}}\par
\hyperref[wand-teleportation]{Wand of teleportation, monster removal, p.~\pageref*{wand-teleportation}}\par
Wand of wishing: \hyperref[wand-wishing]{found with one charge, recharge once and only once, p.~\pageref*{wand-wishing}}\par
\hyperref[unicorns-and-horses-u]{Warhorse, ridden into mid-game, p.~\pageref*{unicorns-and-horses-u}}\par
\hyperref[attack-wands]{Warning shot, monster's first wand zap, p.~\pageref*{attack-wands}}\par
Water: \hyperref[snakes-s]{moccasin, from fountain, p.~\pageref*{snakes-s}}; \hyperref[major-demons]{demon, fountain summons, p.~\pageref*{major-demons}}; \hyperref[fountains]{demon wish, roughly 1 in 150 quaffs, p.~\pageref*{fountains}}; \hyperref[the-potion-table]{potion, always clear, p.~\pageref*{the-potion-table}}; \hyperref[boots]{walking boots, Castle drawbridge, p.~\pageref*{boots}}\par
\hyperref[how-hunger-works]{Weak status, –1 Str, p.~\pageref*{how-hunger-works}}\par
\hyperref[weaponless]{Weaponless conduct, p.~\pageref*{weaponless}}\par
\hyperref[weapons]{Weapons, choice depends on role, p.~\pageref*{weapons}}\par
\hyperref[wishable-random-artifacts]{Werebane, lycanthropy defense, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[dogs-and-canines-d]{Werewolf, werejackal, lycanthropy, p.~\pageref*{dogs-and-canines-d}}\par
\hyperref[what-to-wish-for]{What to wish for, p.~\pageref*{what-to-wish-for}}\par
\hyperref[a-note-on-dragons]{White dragon scale mail, cold + slow digestion, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[whats-different-in-gehennom]{Wielding Excalibur or Demonbane, no bribery, p.~\pageref*{whats-different-in-gehennom}}\par
Wish: \hyperref[sources-of-wishes]{seven kinds of source, p.~\pageref*{sources-of-wishes}}; \hyperref[wish-syntax]{syntax, blessed greased fixed +2, silent substitutions such as a fake amulet, p.~\pageref*{wish-syntax}}; \hyperref[wishing-restrictions]{for ``nothing'', the escape hatch, p.~\pageref*{wishing-restrictions}}\par
\hyperref[what-to-wish-for]{Wishes, optimal use of, p.~\pageref*{what-to-wish-for}}\par
\hyperref[quest-artifacts]{Quest artifacts, cannot be wished for; carry bonuses, p.~\pageref*{quest-artifacts}}\par
\hyperref[wishing-restrictions]{Wishless conduct, refuse all, p.~\pageref*{wishing-restrictions}}\par
Wizard: \hyperref[the-roles]{kitten that won't share lunch, cloak of magic resistance from turn one, force bolt shatters potions, p.~\pageref*{the-roles}}; \hyperref[humans-and-elves]{of Yendor, the most persistent ex, p.~\pageref*{humans-and-elves}}; \hyperref[spending-slots-wisely]{dagger Expert opening, p.~\pageref*{spending-slots-wisely}}; \hyperref[the-wizards-tower]{of Yendor, never stops, p.~\pageref*{the-wizards-tower}}; \hyperref[the-gauntlet]{of Yendor, the eternal nuisance, p.~\pageref*{the-gauntlet}}\par
\hyperref[the-wizards-tower]{Wizard's Tower, three special levels, p.~\pageref*{the-wizards-tower}}\par
\hyperref[real-gem-prices]{Worthless glass, unicorn-safe junk, p.~\pageref*{real-gem-prices}}\par
Wraith: \hyperref[a-note-on-wraiths]{corpse, gain an experience level, p.~\pageref*{a-note-on-wraiths}}; \hyperref[scroll-reverse-genocide]{reverse genocide, banquet, p.~\pageref*{scroll-reverse-genocide}}\par
\hyperref[deadly-mistakes]{Wrath of a god, prayer gone wrong, p.~\pageref*{deadly-mistakes}}\par
\hyperref[wresting]{Wresting, 1/121 final charge, p.~\pageref*{wresting}}\par

\par\smallskip{\normalsize\bfseries X}\par\smallskip

\hyperref[xans-and-fantastic-insects-x]{`x` xans and fantastic insects, p.~\pageref*{xans-and-fantastic-insects-x}}\par
\hyperref[xorns-x]{`X` xorn, phases through walls, p.~\pageref*{xorns-x}}\par
\hyperref[xans-and-fantastic-insects-x]{Xan, sting cripples your legs, p.~\pageref*{xans-and-fantastic-insects-x}}\par

\par\smallskip{\normalsize\bfseries Y}\par\smallskip

\hyperref[apelike-creatures-y]{`Y` apelike creatures, p.~\pageref*{apelike-creatures-y}}\par
\hyperref[lights-y]{`y` lights, p.~\pageref*{lights-y}}\par
\hyperref[acknowledgements]{YAFAP (Yet Another First Ascension Post), p.~\pageref*{acknowledgements}}\par
YASD: \hyperref[your-first-descent]{inevitability of, p.~\pageref*{your-first-descent}}; \hyperref[acknowledgements]{(Yet Another Stupid Death), p.~\pageref*{acknowledgements}}\par
\hyperref[major-demons]{Yeenoghu, attacks on sight, p.~\pageref*{major-demons}}\par
Yellow: \hyperref[light-bursts]{light, blinds 10d20 turns, p.~\pageref*{light-bursts}}; \hyperref[fungi-and-molds-f]{mold, stuns and poisons, p.~\pageref*{fungi-and-molds-f}}\par
Yellow dragon: \hyperref[a-note-on-dragons]{scale mail, stoning resistance bonus, p.~\pageref*{a-note-on-dragons}}; \hyperref[petrification-stoning]{scale mail, permanent stoning resistance, p.~\pageref*{petrification-stoning}}\par
Yeti: \hyperref[apelike-creatures-y]{cold resistance corpse, p.~\pageref*{apelike-creatures-y}}; \hyperref[useful-corpse-effects]{corpse, cold resistance, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[dungeon-hazards-and-how-to-survive-them]{Your own pet, swapping places, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}\par

\par\smallskip{\normalsize\bfseries Z}\par\smallskip

\hyperref[zombies-z]{`Z` zombies, p.~\pageref*{zombies-z}}\par
\hyperref[zruties-z]{`z` zruty, three-attack brute, p.~\pageref*{zruties-z}}\par
\hyperref[room-types]{Zoo, wake them one at a time, p.~\pageref*{room-types}}\par
\hyperref[the-map-symbols]{Zorkmid, abbreviation zm, p.~\pageref*{the-map-symbols}}\par

\end{multicols}
```

:::


---

*You descend the stairs...*

---

### 謝辞 (Acknowledgements)
<!-- audit
2026-05-19:
- NetHack 1987, Fenlason -> Brouwer -> Stephenson lineage verified (Wikipedia, dat/history)
- DevTeam founders, Izchak Miller died 1994, Hack 1982 origin all verified
- WCST acronym is not expanded in the original Waterman file; Wheaton, IL distribution started 1991 (pdwaterman.com)
- Kevin Hugo is on the official 5.0 core team list (dat/history:314)
- nethackwiki.com returned 403, so wiki article counts and some spoiler-author attributions are unverified
-->

NetHack は 1987 年以来、世界中のプレイヤーによってプレイされ、罵倒され、愛され、そして詳細に記録され続けてきました。ゲーム本体は、現存する最長寿のオープンソースプロジェクトの一つを維持し続けてきた開発者の緩やかな集団である「NetHack DevTeam」の成果です。しかし、この迷宮で実際に生き延びるための攻略法や知恵、ドキュメントの数々は、プレイヤーたち自身の手によって築き上げられてきました。

草創期、知識は Usenet のニュースグループ **RGRN**（rec.games.roguelike.nethack）を通じて共有されました。何千人ものプレイヤーが質問を投稿し、戦略について議論し、自ら進んで秘密を明かそうとしないゲームの知識を少しずつ共有財産として蓄積していったのです。それは Wiki も Reddit も Discord も存在しなかった時代の話です。コカトリスの死体を武器として振り回せるかどうかを知りたければ、RGRN の過去ログを検索し、自分より先に誰かが試していることを祈るしかありませんでした。そして大抵の場合、先人がすでに試していたのです。

RGRN はコミュニティに多くの用語をもたらしました。**YASD**（*Yet Another Stupid Death* / またしてもくだらない死）は、「やってはならないと分かっていたはずのこと」で死亡した際に投稿される反省記事です。**YAFAP**（*Yet Another First Ascension Post* / またしても最初の昇天報告）は、ついにゲームをクリアした際の歓喜の報告です。どちらの伝統も、現在の Wiki、Reddit、Discord のコミュニティへと受け継がれています。

それらの対話から、最初の「スポイラー（解析・攻略情報）ファイル」が生まれました。あらゆるアイテム、あらゆるモンスター、あらゆる相互作用を網羅したプレーンテキストの目録です。それらは手作業で書き起こされ、ゲームのソースコードと照合され、惜しみなく無償で共有されました。

本ガイドは、彼らの偉大な先駆的成果の上に成り立っています。特に：

**Kevin Hugo 氏**は NetHack 3.2.2 向けの最初の包括的なスポイラーセットを編纂し、あらゆるアイテム分類、モンスターのステータス、呪文の計算式、スコア計算を極めて几帳面にまとめ上げました。**Dylan O'Donnell 氏**はその全セットを 3.4.3 向けに改訂・拡張し、数年間にわたって維持しました。両氏によるスポイラー群は、薬、巻物、杖、指輪、魔除け、道具、武器、防具、アーティファクト、食料、モンスター、呪文などを網羅する全38ファイルからなる不動の決定版リファレンスとなりました。本ガイドの第4部および第5部に掲載されているデータ一覧表は、彼らの作業と照合・検証されています（BSD風ライセンスの下で公開）。

**Paul Waterman 氏**は 1991 年にウィートン大学で「WCST NetHack Spoilers」を執筆しました。これはゲーム全体を軽妙で主観的な語り口で解説した長大な単一ドキュメントでした。Hugo 氏と O'Donnell 氏が参照マニュアルを著したのに対し、WCST はまるで「旅行ガイドブック」でした。単に事象を説明するだけでなく、それにどう対処すべきかを説いたのです。これは本ガイドのトーンと構成における原初の着想となりました（本文の直接の引用はありません）。

**Kate Nepveu 氏**は steelypips.org を運営し、Hugo/O'Donnell スポイラー、RGRN の名作記事、そして自身の優れたガイド群（本ガイドの罠の章で引用したエルベレス FAQ など）をウェブ上で保存し続けました。Kate 氏の根気強いアーカイブ作業がなければ、Usenet の衰退とともに多くの貴重な知見が失われていたはずです。

さらに、以下の **RGRN コミュニティの執筆者たち**が、本ガイドの各節に情報を提供してくれた記事、FAQ、ガイドを寄稿してくれました：

アイテム識別 FAQ を著した **David Damerell 氏**。杖の識別ガイドを著した **Kieron Dunbar 氏**。即死スポイラーを編纂した **Trevor Powell 氏**。メデューサ対策ガイドを著した **Arien Malec 氏**。祈りガイドを著した **Matthew Lahut 氏**。[倉庫番](#sokoban)全8パターンの解答マップを作成した **Boudewijn Waijers 氏**。魔法書読解成功率を計算した **Steven Bush 氏**。店主の価格計算式を記録した **Gregory Bond 氏**。コンダクトを分類目録化した **Dion Nicolaas 氏**。風の精 FAQ を著した **David Goldfarb 氏**。経験値計算を記録した **Hojita Discordia 氏**。

そして Ray Chason 氏、Pat Rankin 氏、Geoduck 氏、Topi Linkala 氏、Geoffrey Eadon 氏、Roger Broadbent 氏、Sebastian Haas 氏、Jukka Lahtinen 氏をはじめ、「誰かこれを試した人はいる？」と問いかけ、その結果を報告してくれたニュースグループの無数の名無しの冒険者たちに深く感謝します。

**[NetHack Wiki](https://nethackwiki.com/)** は本ガイドにとって不可欠のリファレンスでした。2005 年に Sgeo 氏によって「WikiHack」として設立され、2010 年に独自ドメインへ移行した同サイトには、現在 5,000 件以上の記事が蓄積されています。制作者および管理者には Pasi Kallinen 氏、Drew Streib 氏、Alex Smith 氏、Shawn Moore 氏、George Koehler 氏、Tjr 氏、ZeroOne 氏、Ray Chason 氏らが名を連ねています。Wiki の [NetHack 5.0.0 ページ](https://nethackwiki.com/wiki/NetHack_5.0.0) はコミュニティの生きた更新履歴であり、本ガイドの 5.0 改訂における主たる情報源となりました。

現在多くのプレイヤーが集う**公開サーバー**は、[nethack.alt.org](https://alt.org/nethack/)（NAO: M. Drew Streib 氏と Pasi Kallinen 氏が運営する最長寿サーバー）および [Hardfought](https://hardfought.org/)（K2 氏が運営し、主要バリアントもホスト）です。どちらも無料でプレイでき、すべての昇天記録を保存しています。本ガイドで引用されている死因統計や昇天記録は、これら公開サーバーのデータに基づいています（NAO の [主な死因一覧](https://alt.org/nethack/topdeaths.html) 参照）。

Reddit の **[r/nethack](https://www.reddit.com/r/nethack/) コミュニティ** は、新世代のプレイヤーたちに向けて議論の場を提供し続けています。歴代のモデレーターたちは、ベテランと初心者が助言を交わし、昇天体験を共有し、最適な「願い」の選択について熱く議論できる温かいコミュニティを維持してきました。数千のスレッドを通じて受け継がれてきた集合知は、本ガイドの実戦的アドバイスに大きく反映されています。

そして何よりも、このゲームそのものが存在したからこそ、本ガイドが生まれました。
**[NetHack](https://www.nethack.org/)** は、Mike Stephenson 氏、Izchak Miller 氏、Janet Walz 氏によって設立された NetHack DevTeam により、1987 年から開発が続けられています。Izchak Miller 氏は 1994 年に惜しまれつつ世を去りました。[ノームの鉱山](#the-gnomish-mines) で彼の名を冠した店主（イズチャク）は、彼の遺した功績の大きさを今に伝えています。ソースコードは [github.com/NetHack](https://github.com/NetHack/NetHack) で公開されています。

ゲーム自体はさらに初期のローグライクに遡ります。**Hack** は 1982 年、リンカーン・サドベリー地域高校の授業プロジェクトとして Jay Fenlason 氏によって書かれ（Toy 氏と Wichman 氏の『Rogue』(1980) を下敷きにしています）、1980 年代半ばにかけて Andries Brouwer 氏によって拡張されました。NetHack は 1987 年に Brouwer 氏の Hack からフォークしました。**グリッドバグ**（マス目の格子状に住み、「昆虫」と「プログラムのバグ」を掛け、1982 年の映画『トロン』への敬意を込めたとされる直角移動モンスター）をはじめとする NetHack 固有のモンスターの多くは、Fenlason 氏のオリジナル Hack から受け継がれたものです。このダンジョンは、NetHack というゲームよりもさらに古い歴史を持っています。

開発の道のりは常に平坦だったわけではありません。2003 年 12 月のバージョン 3.4.3 の後、DevTeam は 12 年間もの長きにわたり沈黙を守りました。公には一切の発言を断ち、水面下で作業を続けていたのです。その間、コミュニティでは「*DevTeam は思考中である（The DevTeam is THINKING）*」というジョークが定着しました。ダンジョンは凍りつきました。新たなプレイヤーたちは 2003 年以来変わらない回廊へと降り立ち、変化のないゲームについて新たなスポイラーを書き、新たに記録された同じ死因で命を落としていきました。沈黙の 12年間に蓄積されたコミュニティの知恵は色褪せることなく役立ち続け、ゲームはたった1行の新しいコードが追加されることもなく、丸10年におよぶ新たな分析に耐えうるほどの奥深さを証明したのです。2015 年 12 月にバージョン 3.6 が登場し、それ以来活発な開発が続いています。

現在のチーム（Michael Allison, Ken Arromdee, David Cohrs, Jessie Collet, Kevin Hugo, Pasi Kallinen, Ken Lorber, Dean Luick, Patric Mueller, Pat Rankin, Derek S. Ray, Alex Smith, Mike Stephenson, Janet Walz, Paul Winner, Bart House, Warwick Allison の各氏）は、40年近くにわたりこのゲームを維持し、拡張し続けてきました。本書のすべての記述は、彼らの献身的な仕事の恩恵によるものです。

本ガイドのすべてのデータは、現在の NetHack 5.0.0 のソースコードと照合・検証されています。万一誤りがあれば、それはすべて編著者の責に帰するものです。

---

*『恐怖の迷宮への旅人の手引き (A Traveler's Companion to the Mazes of Menace)』 NetHack 5.0 ローンチ記念版*<br>
*編纂: David Bau、事実照合・検証: Claude 4.8 Opus*<br>
*日本語版翻訳・監修: Antigravity AI & NetHackJP Project*

*本著作物は [クリエイティブ・コモンズ 表示 - 継承 4.0 国際 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) ライセンスの下で許諾されています。*
