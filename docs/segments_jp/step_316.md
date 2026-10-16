#### げっ歯類 `r` (Rodents `r`) {#rodents-r}

<!-- audit
2026-05-19:
- 6 rows (S_RODENT) sourced from monsters.h:889-936.
- Woodchuck color is brown (CLR_BROWN at monsters.h:936).
- Rock mole is M1_METALLIVORE: eats metal, including bag of gold and unattended weapons (mondata.c:561, hack.c:769-784).
-->

下水ネズミ、巨大ネズミ、岩モグラなどの小型哺乳類です。床に落ちている金属アイテムを食べる岩モグラや、木製の扉を齧るウッドチャックなどが含まれます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ドブネズミ (sewer rat) | 茶色 | 0 | 12 | 7 | 0 | 噛みつき 1d3 |  |
| 巨大ネズミ (giant rat) | 茶色 | 1 | 10 | 7 | 0 | 噛みつき 1d3 |  |
| 兇暴ネズミ (rabid rat) | 茶色 | 2 | 12 | 6 | 0 | 噛みつき 2d4 エナジードレイン-Co | 死体に毒あり、毒耐性. |
| ねずみ人間 (wererat) | 茶色 | 2 | 12 | 6 | 10 | 噛みつき 1d4 獣化 | 自動回復、毒耐性。死体を残さない。 |
| 岩もぐら (rock mole) | 灰色 | 3 | 3 | 0 | 20 | 噛みつき 1d6 | 穴掘り移動、床に落ちている金属製アイテムを捕食する。 |
| リス (woodchuck) | 茶色 | 3 | 3 | 0 | 20 | 噛みつき 1d6 | 遊泳、穴掘り移動. |

:::
