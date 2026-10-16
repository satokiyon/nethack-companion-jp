#### 光および幻影 `y` (Lights and phantoms `y`) {#lights-y}

<!-- audit
2026-05-19:
- 2 rows (yellow light L3 yellow, black light L5 black) sourced from monsters.h:1168-1191.
- Attacks AT_EXPL/AD_BLND 10d20 (yellow) and AT_EXPL/AD_HALU 10d12 (black).
- M1_FLY|M1_AMORPHOUS|M1_MINDLESS on both; black light adds M1_SEE_INVIS.
- 10d20 is blindness DURATION, NOT HP damage. (uhitm.c:2978-2985 mhitm_ad_blnd: `make_blinded(BlindedTimeout + (long) mhm->damage, FALSE); mhm->damage = 0;` — rolled value feeds timer, HP damage zeroed)
- AT_EXPL means the monster dies on attack ("bursts on contact").
-->

黄色光や黒色光など、視界や精神を惑わす発光生物です。触れると自爆して盲目や混乱を引き起こします。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 黄色い光 (yellow light) | 黄色 | 3 | 15 | 0 | 0 | 自爆 10d20 盲目 |  |
| 黒い光 (black light) | 黒色 | 5 | 15 | 0 | 0 | 自爆 10d12 hallu | 不可視視認. |

:::
