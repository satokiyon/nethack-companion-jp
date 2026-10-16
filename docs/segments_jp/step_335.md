#### リッチ `L` (Liches `L`)

<!-- audit
2026-05-19:
- 4 lich rows at monsters.h:1864-1897 (lich 1864, demilich 1872, master lich 1880, arch-lich 1889).
- All carry G_NOCORPSE, so no eatable corpse regardless of M1_POIS flavor.
- Only the arch-lich (m_lev=25) reaches DEATH_TOUCH at spell-level 20; master lich m_lev=17 cannot (mcastu.c:111).
- Double-trouble is Wizard-of-Yendor only, NOT a lich ability.
- Arch-lich casts touch of death, NOT rays.
2026-05-31:
- Touch of death (mcastu.c:389-408): without Antimagic, `rn2(mtmp->m_lev) > 12` gates the effect. At m_lev 25 that succeeds 12/25 of the time; touch_of_death then deals 50+8d6 damage and drains half that amount from max HP. Magic resistance blocks the effect (mcastu.c:315-347).
- Only the Wizard of Yendor literally has M3_COVETOUS in 5.0 (monsters.h:2857; single row). Arch-liches do NOT teleport-away-to-heal. Their threat profile is the touch-of-death spell, not the covetous return-at-full-HP behavior the Wizard has.
-->

骸骨姿の強力な魔法使いアンデッド。マスターリッチやアーチリッチは死の指（Touch of death）を詠唱し、モンスターを大量召喚し、冷気光線を放ってきます。魔法防御（Magic resistance）がなければ即死する危険極まりない強敵です。

すべてのリッチは自動回復し、死体を残さず、アンデッドであり、冷気耐性、睡眠耐性、毒耐性を備えています。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| リッチ (lich) | 茶色 | 11 | 6 | 0 | 30 | 接触 1d10 冷気 · cast spell |  |
| デミリッチ (demilich) | 赤色 | 14 | 9 | -2 | 60 | 接触 3d4 冷気 · cast spell |  |
| マスターリッチ (master lich) | 赤紫 | 17 | 9 | -4 | 90 | 接触 3d6 冷気 · cast spell | 火炎耐性. Casts wizard spells. Kill from afar. |
| arch-lich | 赤紫 | 25 | 9 | -6 | 90 | 接触 5d6 冷気 · cast spell | 火炎耐性, 電撃耐性. Casts touch of death; magic resistance mandatory. |

:::
