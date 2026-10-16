#### ハンマー (Hammer)
<!-- audit
2026-05-19:
- war hammer stats verified (objects.h:367-369, weapon.c); +1 small bonus matches sdam/ldam fields
- Mjollnir can be gifted to ANY Valkyrie, not just Neutral: hack_artifacts fixes alignment to player's initalign (artifact.c:92-95)
- aklys uses P_CLUB and is correctly placed elsewhere
-->

片手持ちの打撃系近接武器。ワルキューレ（Valkyrie）のアーティファクトであるウォーハンマー「ミョルニル (Mjollnir)」は、投擲すると手元に戻ってきます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| ウォーハンマー (war hammer) | 1d4+1 / 1d4 | 50 | 5 | — | 鉄 | ミョルニル (Mjollnir) がアーティファクト形態（ワルキューレへの生贄の賜物。属性はプレイヤーの初期属性に一致する）。 |

:::
