### セーブとボーンズ (Saving and Bones) {#saving-and-bones}

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
