#### ネコ科 `f` (Felines `f`) {#felines-f}

<!-- audit
2026-05-19:
- 8 rows (S_FELINE) sourced from monsters.h:381-444.
- kitten L2/Spd18/AC6 bite 1d6 (monsters.h:381-388).
- housecat L4/Spd16/AC5 bite 1d6 (monsters.h:389-396).
- large cat L6/Spd15/AC4 bite 2d4 (monsters.h:421-428).
- displacer beast L12/Spd12/AC-10 claw 4d4 + claw 4d4 + bite 2d10 (monsters.h:437-444).
- Tigers are M2_HOSTILE, difficulty 8: tameable only via charm-monster/scroll-of-taming/magic-flute, NOT tripe. (monsters.h:429-436 tiger has M2_HOSTILE only — no M2_DOMESTIC; befriend_with_obj at mondata.h:255-261 requires is_domestic for FOOD_CLASS items)
- Only Wizard guarantees a kitten (urole.petnum=PM_KITTEN per role.c:548); every role without a fixed pet rolls 50/50 kitten-or-dog (dog.c:90-101).
-->

野生のネコ科生物は素早く敵対的です。虎や幻影の獣は、何気ない通路での遭遇を命がけの戦いに変えてしまいます。魔法使いは必ず小猫を連れてスタートし、初期ペットが固定されていない職業は小猫か仔犬のいずれかを 50% の確率で連れて開始します。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| 小猫 (kitten) | 白色 | 2 | 18 | 6 | 0 | 噛みつき 1d6 | 手懐け可能。一般的なペット。 |
| 家猫 (housecat) | 白色 | 4 | 16 | 5 | 0 | 噛みつき 1d6 | 手懐け可能. |
| ジャガー (jaguar) | 茶色 | 4 | 15 | 6 | 0 | 爪 1d4 ×2 · 噛みつき 1d8 |  |
| 山猫 (lynx) | 水色 | 5 | 15 | 6 | 0 | 爪 1d4 ×2 · 噛みつき 1d10 |  |
| パンサー (panther) | 黒色 | 5 | 15 | 6 | 0 | 爪 1d6 ×2 · 噛みつき 1d10 |  |
| 大きな猫 (large cat) | 白色 | 6 | 15 | 4 | 0 | 噛みつき 2d4 | 手懐け可能. |
| 虎 (tiger) | 黄色 | 6 | 12 | 6 | 0 | 爪 2d4 ×2 · 噛みつき 1d10 |  |
| 幻影の獣 (displacer beast) | 青色 | 12 | 12 | -10 | 0 | 爪 4d4 ×2 · 噛みつき 2d10 |  |

:::
