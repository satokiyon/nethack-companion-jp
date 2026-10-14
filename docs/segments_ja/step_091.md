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
