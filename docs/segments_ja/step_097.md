### 神との関係 (Divine Relations)

<!-- audit
2026-05-31 audit:
- corpse 50-turn freshness rule verified at pray.c:1843-1849. EXCEPT: an acid blob corpse (PM_ACID_BLOB) is the one exception and never spoils for sacrifice purposes (pray.c:1843).
- sacrifice value formula: mons[corpsenm].difficulty + 1 (pray.c:1845). Bigger/tougher monsters yield higher value.
- artifact gift chance per qualifying sacrifice: !rn2(6 + (2 * u.ugifts * nartifacts)) (pray.c:1792). First gift is 1 in 6; subsequent gifts drop by a multiplicative factor (gift count × total artifacts in world), NOT additive +2·n as previously stated.
- prerequisites: u.ulevel > 2 (XL>=3) AND u.uluck >= 0 (pray.c:1784).
- first-gift bias is alignment + skill compatibility, not role-name lookup (artifact.c:230 `a->alignment != A_NONE || u.ugifts > 0 || !rn2(3)`).
- pre-existing book claim "1 in (10 + 2·n)" (giving 1/10 first, 1/14 second) was incorrect; rewrote to match the source.
-->

機嫌の良い神はあなたの祈りに応え、過ちを赦し、時には強力なアーティファクトを授けてくれます。一方、怒れる神は天罰を下してあなたを打ち倒します。
