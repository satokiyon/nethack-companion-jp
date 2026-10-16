#### メイス (Mace)
<!-- audit
2026-05-19:
- mace stats verified (objects.h:355-361)
- Demonbane PHYS(5,0): +1d5 to-hit and double damage vs demons (artifact.c:1083-1085 spec_abon, 1106-1107 spec_dbon); also has banish invoke
- silver mace: +1d20 vs mon_hates_silver targets (uhitm.c:1376-1377)
- silver hates list: demons, weres, vampires, shades, most imps (mondata.c:524-528)
- silver does NOT hit "undead" or "shape-changers" generally (mummies, zombies, ghosts, chameleons excluded)
- Mjollnir is a war hammer, NOT a mace (artilist.h:109 `A("Mjollnir", WAR_HAMMER, ...)`)
-->

片手持ちの打撃系近接武器。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| メイス (mace) | 1d6+1 / 1d6 | 30 | 5 | — | 鉄 | 僧侶（Priest）が生贄の捧げ物で最初に確定入手するアーティファクト「デーモンベイン (Demonbane)」の母体：悪魔に対して命中+1d5かつダメージ2倍の銀のメイス、さらに追放効果の発動（invoke）付き。 |
| 銀のメイス (silver mace) | 1d6+1 / 1d6 | 36 | 60 | — | 銀 | 悪魔、獣人、吸血鬼、影、大半の小悪魔に対して+1d20の追加ダメージ。 |

:::
