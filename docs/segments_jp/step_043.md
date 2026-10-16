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

