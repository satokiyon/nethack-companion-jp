#### 両手剣 (Two-handed sword) {#two-handed-sword}
<!-- audit
2026-05-19:
- two-handed sword stats verified (objects.h:273-285)
- 5.0 bimanual weapons get 3/2 Str damage bonus, melee only (uhitm.c:1467-1468; gated on bimanual(uwep) + HMON_MELEE)
- bonus also applies to battle-axe, dwarvish mattock, bardiche
- Tsurugi is the two-handed sword artifact (artilist.h:285-289); Vorpal Blade is a LONG_SWORD (artilist.h:191), NOT the artifact form here
-->

両手持ち武器は 5.0 において**筋力ダメージに 1.5 倍（3/2）のボーナス**を受けます。筋力によるダメージ補正値が 1.5 倍されます。下記の高い基本ダイス値と合わさることで、盾の装備枠を放棄しなければならないにもかかわらず、両手剣が片手武器＋盾の構成に匹敵する大きな理由となっています。
このボーナスは戦斧、ドワーフのつるはし、バーディックなど、あらゆる両手持ち武器に適用されます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 両手剣 (two-handed sword) | 1d12 / 1d6+2d6 | 150 | 50 | — | 鉄 | 両手持ち（盾および利き手以外の武器の併用不可）。 |
| 大刀 (tsurugi) | 1d16 / 1d8+2d6 | 60 | 500 | +2 | 金属 | 両手持ち。村正の剣 (The Tsurugi of Muramasa) がアーティファクト形態。 |

:::
