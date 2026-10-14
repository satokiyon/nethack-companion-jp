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
