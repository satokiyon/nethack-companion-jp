#### 長剣 (Long sword)
<!-- audit
2026-05-19:
- long sword stats verified (objects.h:270-280)
- Excalibur dipping requires LONG_SWORD, XL >= 5, quan == 1, not already artifact, no extant Excalibur (fountain.c:404-408)
- dip roll: !rn2(6) for Knights, !rn2(30) otherwise (fountain.c:405)
- non-Lawfuls get the sword cursed, spe possibly decremented, oerodeproof cleared (fountain.c:411-421)
- LONG_SWORD artifacts: Excalibur, Frost Brand, Fire Brand, Giantslayer, Vorpal Blade, Sunsword (artilist.h:85, 149, 153, 174, 191, 209)
- Vorpal Blade is a LONG_SWORD artifact, NOT a two-handed sword (artilist.h:191)
- two-handed sword has no dedicated artifact (no TWO_HANDED_SWORD entries in artilist.h)
-->

片手持ち近接武器。秩序属性の長剣は、序盤で単一武器として最も大きな見返りを得られる「泉への浸しによるエクスカリバー入手」の対象となります。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 長剣 (long sword) | 1d8 / 1d12 | 40 | 15 | — | 鉄 | 経験レベル5以上で泉に浸すと、1/30の確率（騎士は1/6）で判定が行われる。成功時、秩序属性のキャラクターは**エクスカリバー (Excalibur)** を獲得する。それ以外の属性では剣が呪われる。アーティファクト形態：エクスカリバー、フロストブランド、ファイヤーブランド、巨人殺し、ヴォーパルブレード、サンソード。 |
| 刀 (katana) | 1d10 / 1d12 | 40 | 80 | +1 | 鉄 | 武器自体に+1の命中補正が組み込まれている。スニッカーズニー (Snickersnee) がアーティファクト形態。 |

:::
