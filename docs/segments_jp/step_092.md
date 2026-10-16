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

