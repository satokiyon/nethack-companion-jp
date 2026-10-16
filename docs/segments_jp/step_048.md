#### 移動系の罠 (Movement Traps) {#movement-traps}
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
