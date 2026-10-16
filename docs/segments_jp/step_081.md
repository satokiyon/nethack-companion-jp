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

