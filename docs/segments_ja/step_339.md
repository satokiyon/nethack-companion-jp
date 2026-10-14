#### プリンおよびウーズ `P` (Puddings and oozes `P`)

<!-- audit
2026-05-19:
- Green slime: make_slimed sets a 10-turn countdown, NOT 9 (uhitm.c:3199, 3570; polyself.c:456; eat.c:854). The 5-turn case is engulf+digest only (uhitm.c:5099).
- Brown puddings rot wood/leather/cloth/bone (AD_DCAY = ERODE_ROT, uhitm.c:2389). They do NOT corrode armor.
- Black puddings corrode metal (AD_CORR, uhitm.c:2338-2356).
- Gray ooze rusts armor (AD_RUST).
- Splitting on iron/metal melee is gated to PM_BLACK_PUDDING || PM_BROWN_PUDDING (uhitm.c:1609-1621). Gray ooze and green slime do NOT split.
-->

**茶色および黒色プリンは鉄製や金属製の刃物で攻撃すると分裂します**。無傷の死体ではなく塊を残します。

**緑スライム**は[ゲヘナ](#gehennom)にのみ現れる例外で、分裂はしませんが接触した相手を緑スライムへと徐々に変異させていきます（石化に似た即死タイマー）。

すべてのプリンおよびウーズは不定形で、精神を持たず、冷気耐性、毒耐性、酸耐性、石化耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 灰色ウーズ (gray ooze) | 灰色 | 3 | 1 | 8 | 0 | 噛みつき 2d8 錆び | 火炎耐性. |
| 茶色プリン (brown pudding) | 茶色 | 5 | 3 | 8 | 0 | 噛みつき decay |  |
| 緑スライム (green slime) | 緑色 | 6 | 6 | 6 | 0 | 接触 1d4 slime · 反撃 slime | 死体を残さない。 |
| 黒プリン (black pudding) | 黒色 | 10 | 6 | 6 | 0 | 噛みつき 3d8 corrode · 反撃 corrode |  |

:::
