#### 長柄武器 (Polearms) {#polearms}
<!-- audit
2026-05-19:
- 12 polearm rows verified: all two-handed, all P_POLEARMS, all iron (objects.h:294-341).
- per-row dice/weight/cost from objects.h:294-341 WEAPON() macros; +d4/+d6 vs-large bonuses applied in weapon.c dmgval.
- polearm reach is skill-dependent, NOT a fixed 2 squares (apply.c:3355-3382).
- use_pole has NO "empty intervening square" check (apply.c:3355-3382).
- polearms CAN bash an adjacent monster (uhitm.c:1467-1484).
- adjacent polearm bash: damage clamps to 1d2 base, no weapon-skill bonus, Strength still applies (uhitm.c:1075-1086, 1447-1469).
-->

すべての長柄武器は両手持ちです。離れた敵を攻撃するには、武器を手に持って通常攻撃するのではなく、`#apply`（使用）コマンドを使います。ベーシック（入門）スキルでは直線2マス先の敵を攻撃でき、熟練（エキスパート）になるとさらに攻撃可能な位置が広がります。長柄武器を持った状態で隣接するモンスターを通常攻撃することも可能ですが、強打（打撃）扱いとなり、ボーナス加算前の基本ダメージが 1d2 に制限され、武器スキルによるダメージボーナスも乗りません（筋力補正は適用されます）。この「間合い（リーチ）」こそが、長柄武器を持ち歩く最大の意義です。各武器の追加ダメージの詳細は下記の備考を参照してください。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| パルチザン (partisan) | 1d6 / 1d6+1 | 80 | 10 | — | 鉄 | リーチ攻撃可能。 |
| ランサー (ranseur) | 1d4+1d4 / 1d4+1d4 | 50 | 6 | — | 鉄 | 小型に+1d4、大型に+1d4。 |
| スペタム (spetum) | 1d6+1 / 1d6+1d6 | 50 | 5 | — | 鉄 | 小型に+1、大型に+1d6。 |
| グレイブ (glaive / naginata: 薙刀) | 1d6 / 1d10 | 75 | 6 | — | 鉄 | リーチ攻撃可能。 |
| ハルバード (halberd) | 1d10 / 1d6+1d6 | 150 | 10 | — | 鉄 | 大型に+1d6。 |
| バーディック (bardiche) | 1d4+1d4 / 1d4+2d4 | 120 | 7 | — | 鉄 | 小型に+1d4、大型に+2d4。 |
| ヴォウジェ (voulge) | 1d4+1d4 / 1d4+1d4 | 125 | 5 | — | 鉄 | 小型に+1d4、大型に+1d4。 |
| フォシャール (fauchard) | 1d6 / 1d8 | 60 | 5 | — | 鉄 | リーチ攻撃可能。 |
| ギザルム (guisarme) | 1d4+1d4 / 1d8 | 80 | 5 | — | 鉄 | 小型に+1d4。 |
| ビル・ギザルム (bill-guisarme) | 1d4+1d4 / 1d10 | 120 | 7 | — | 鉄 | 小型に+1d4。 |
| ルッツェルンハンマー (lucern hammer) | 1d4+1d4 / 1d6 | 150 | 7 | — | 鉄 | 小型に+1d4。 |
| ベック・ド・コルバン (bec de corbin) | 1d8 / 1d6 | 100 | 8 | — | 鉄 | リーチ攻撃可能。 |

:::
