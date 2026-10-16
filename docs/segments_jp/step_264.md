<!-- audit
2026-05-19:
- 4 short sword rows verified: short 1d6/1d8, elven 1d8/1d8, orcish 1d5/1d8, dwarvish 1d7/1d8 (objects.h:244-255)
- all share P_SHORT_SWORD; scimitar uses P_SABER and is correctly excluded
- Rogue starter (u_init.c:134); Samurai "wakizashi" is a short sword aliased in objnam.c:106 (u_init.c:144)
- no artifact uses SHORT_SWORD as base type
-->
#### 小剣 (Short sword) {#short-sword}

片手持ち近接武器。脇差（wakizashi）と小剣（short sword）は職業による表示名が異なるだけで、同一の武器です。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 小剣 (short sword / wakizashi: 脇差) | 1d6 / 1d8 | 30 | 10 | — | 鉄 | 盗賊（Rogue）の初期装備。 |
| エルフの小剣 (elven short sword) | 1d8 / 1d8 | 30 | 10 | — | 木 |  |
| オークの小剣 (orcish short sword) | 1d5 / 1d8 | 30 | 10 | — | 鉄 |  |
| ドワーフの小剣 (dwarvish short sword) | 1d7 / 1d8 | 30 | 10 | — | 鉄 |  |

:::
