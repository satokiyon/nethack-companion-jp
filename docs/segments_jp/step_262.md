#### 短剣 (Dagger)
<!-- audit
2026-05-19:
- Expert Rogue dagger multishot caps at rnd(4) = 1-4: 1 base + 1 Expert + 1 Skilled + 1 class (dothrow.c:177-190, 63-67)
- athame engraving Elbereth does NOT dull the weapon, so no enchantment is consumed (engrave.c:1306-1307, 1361). Duration is unchanged
- silver weapons hurt demons, vampires, lycanthropes, shades, and imps (except tengu) per mon_hates_silver (mondata.c:524-528)
- silver does NOT hurt liches, zombies, mummies, wraiths, ghouls, or ghosts (none of those classes appear in hates_silver, mondata.c:524-528)
- silver damage bonus is rolled in mhitm/hmon, +1d20 vs hates_silver targets for silver weapons (uhitm.c:1376-1377)
-->

投擲および刺突。短剣はスタック（束ねて所持）可能で壊れにくく、盗賊（Rogue）は投擲時にマルチショット（連続投擲）ボーナスを得られます（エキスパート時には1ターンに最大4本投擲）。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 短剣 (dagger) | 1d4 / 1d3 | 10 | 4 | +2 | 鉄 | スタック可能。スキルがエキスパートの盗賊は1回の投擲で最大4本までマルチショット可能。 |
| エルフの短剣 (elven dagger) | 1d5 / 1d3 | 10 | 4 | +2 | 木 | スタック可能。アーティファクト形態はスティング (Sting)。 |
| オークの短剣 (orcish dagger) | 1d3 / 1d3 | 10 | 4 | +2 | 鉄 | スタック可能。 |
| 銀の短剣 (silver dagger) | 1d4 / 1d3 | 12 | 40 | +2 | 銀 | スタック可能。悪魔、吸血鬼、獣人、影、小悪魔（インプ）に対して銀特効ダメージ。盗賊や野伏（Ranger）の一般的な利き手以外の武器。 |
| アサメ (athame) | 1d4 / 1d3 | 10 | 4 | +2 | 鉄 | スタック可能。アサメで文字を刻んでも**刃先が鈍ることはない**（強化値が減少しない）。 |

:::
