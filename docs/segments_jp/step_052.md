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

