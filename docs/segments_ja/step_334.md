#### キーストン・コップ `K` (Keystone Kops `K`)

<!-- audit
2026-05-19:
- All Kop stats match monsters.h:1829-1860.
- Shopkeeper-anger triggers Kop summoning via makekops (shk.c:623, 680, 5113).
- Dead Kops respawn per rnd(5) at mon.c:3147-3164: 1/5 near DOWN-stairs, 1/5 at random location, 3/5 stay dead.
- Respawn lands near DOWN-stairs, NOT up-stairs (stairs.c:89-95, mklev.c:2193).
- All four Kops carry G_GENO, so genocide permanently clears them.
-->

店で泥棒を働くか、店主を傷つけた際に笛を鳴らして駆けつける警官隊です。個々の戦闘力は高くありませんが、群れをなして現れ、クリームパイを投げつけてプレイヤーの視界を塞ごうとします。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 警備員 (Keystone Kop) | 青色 | 1 | 6 | 10 | 10 | 武器攻撃 1d4 |  |
| 巡査 (Kop Sergeant) | 青色 | 2 | 8 | 10 | 10 | 武器攻撃 1d6 |  |
| 巡査部長 (Kop Lieutenant) | 水色 | 3 | 10 | 10 | 20 | 武器攻撃 1d8 |  |
| 警部補 (Kop Kaptain) | 赤紫 | 4 | 12 | 10 | 20 | 武器攻撃 2d6 |  |

:::
