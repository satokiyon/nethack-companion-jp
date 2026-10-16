#### ニンフ `n` (Nymphs `n`) {#nymphs-n}

<!-- audit
2026-05-19:
- 3 nymphs (wood/water/mountain): LVL 3, Spd 12, AC 9, MR 20%, AT_CLAW AD_SITM + AT_CLAW AD_SEDU, M1_TPORT (monsters.h:702-723).
- Water nymph has M1_SWIM (line 714); all three carry M1_TPORT|MR_POISON.
- AD_SITM steal-and-teleport at uhitm.c:4724,4798; AD_SEDU at uhitm.c:4642.
- Corpse grants intrinsic teleportitis at 10% per should_givit (eat.c:936-975).
2026-05-31:
- Post-theft teleport calls rloc(mon, RLOC_MSG) at mhitu.c:2303, which is the within-level relocation routine (teleport.c:1799). The nymph does NOT migrate to another level after stealing; she ends up at a random valid position on the SAME level.
- The book's earlier claim that a nymph might "walk off the level with my bag of holding" was an overstatement of the rare incidental case where she later falls through a trapdoor or wanders onto a staircase.
- The Amulet of Yendor has no return-to-Sanctum mechanic on theft. A nymph carrying the Amulet stays on the same level, so the Ascension Run warning was corrected to point at the turn-budget cost of searching the level while the Mysterious Force keeps pulling.
-->

所持品からアイテムを1つ盗み取り、同じフロアのランダムな場所へテレポートします。遠距離から攻撃するか、ペットで進路を塞ぐか、エルベレスの文字を刻んで近寄らせないようにしてください。もしアイテムを盗まれた場合は、フロア全体を捜索して倒せば盗まれたアイテムをすべて回収できます。

すべてのニンフはテレポート能力を持ちます。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 森のニンフ (wood nymph) | 緑色 | 3 | 12 | 9 | 20 | 爪 盗み-item · 爪 誘惑 |  |
| 水のニンフ (water nymph) | 青色 | 3 | 12 | 9 | 20 | 爪 盗み-item · 爪 誘惑 | 遊泳. |
| 山のニンフ (mountain nymph) | 茶色 | 3 | 12 | 9 | 20 | 爪 盗み-item · 爪 誘惑 |  |

:::
