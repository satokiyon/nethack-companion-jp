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
