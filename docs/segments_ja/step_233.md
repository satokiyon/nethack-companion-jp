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

倉庫番（Sokoban）は、入り口から **上向き** に登っていく全4階層の巨岩パズル支流です。各階層にはランダムに選ばれる2種類のマップ構造（バージョンAおよびB）が存在します。巨岩を押して落とし穴や落とし蓋を埋め立て、次の階段へと続く道を作り出していきます。不正行為（巨岩を押さずにすり抜ける、巨岩の上によじ登る、杖や力のボルトやつるはしで巨岩を破壊する、あるいは倉庫番内で大地の巻物を読むなど）を働くと、**違反1回につき幸運に −1 のペナルティ** が累積して課されます。また倉庫番の壁は固すぎて掘削できません。飛行や浮遊も助けにはならず、未充填の穴の上を飛ぼうとすると *「気流に引きずり下ろされた...」（"Air currents pull you down..."）* と吸い込まれて落下します。正々堂々と解いてください。

> *本解答集は、Kate Nepveu 氏が管理する steelypips.org NetHack アーカイブ向けに、Boudewijn Waijers 氏が編纂し、Jukka Lahtinen 氏ほか多数の貢献によって作成されたものをベースにしています。NetHack 5.0 向けに検証・適合し、本ガイド向けに再フォーマットしました。*

以下のマップでは、手順から参照しやすいように巨岩に A から T までの英文字ラベルが振られています。`^` 記号は第1階層では落とし穴（pit）、第2〜4階層では落とし蓋（hole）を表します（落とし蓋は飛行中であっても1階層下へと落とされます）。`<` は上り階段です。開始位置は `@` で示されています。座標は **(列, 行)** で表されます。「X を埋める（Finish X）」とは、巨岩 X を罠の列まで押し、その列に沿って最も近い未充填の穴へと落とし込む一連の手順を指します。「C を G と同様に埋める」は、G で通ったルートを C で再利用することを意味します。

矢印記号（`↑`, `←` 等）は転がる巨岩の罠（rolling boulder trap）を示します。倉庫番では、この罠の上に巨岩を押し込むと、穴に落ちるか何かに衝突するまで押した方向へと自律的に転がり続けます。

階層を解き終えたら、余った巨岩は部屋の隅に押し込んでおき、後から戻ってきたときに通路を塞がれないようにしましょう。巨岩の下にアイテムが隠されていることもあります。

**反転（ミラーリング）に関する注意。** 倉庫番に到達した時点で、マップは最初から全域が表示されています。ゲーム画面の壁の輪郭をここに掲載されたマップと見比べてください。もし左右反転（または上下反転）している場合は、全手順の「左」と「右」（または「上」と「下」）を入れ替え、反対側の端から列を数えてください（Web版のフリップボタンを使えば視覚的に反転できます）。

