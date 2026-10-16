#### ミミック `m` (Mimics `m`) {#mimics-m}

<!-- audit
2026-05-19:
- 3 rows (small/large/giant mimic) sourced from monsters.h:670-698.
- All carry M1_AMORPHOUS|M1_HIDE|MR_ACID; large/giant also have AD_STCK and M2_STRONG.
- Disguise via set_mimic_sym (makemon.c:2393-2472), including STRANGE_OBJECT in shops at sufficient depth.
- AD_STCK is MC-blocked (uhitm.c:3310/3324).
-->

扉、階段、金貨、あるいは貴重なアイテムに擬態して獲物を待ち伏せます。触れると貼り付かれて移動不能になり、噛みつき攻撃を受けます。不自然な位置にある階段や扉、未識別の高価なアイテムには遠距離攻撃で確認を入れるのが賢明です。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 小さなミミック (small mimic) | 茶色 | 7 | 3 | 7 | 0 | 爪 3d4 |  |
| 大きなミミック (large mimic) | 赤色 | 8 | 3 | 7 | 10 | 爪 3d4 sticky |  |
| 巨大なミミック (giant mimic) | 赤紫 | 9 | 3 | 7 | 20 | 爪 3d6 sticky ×2 |  |

:::
