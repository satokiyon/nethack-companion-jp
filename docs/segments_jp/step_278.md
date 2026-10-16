#### 槍 (Spear)
<!-- audit
2026-05-19:
- 6 spear rows (spear/elven/orcish/dwarvish/silver/javelin) verified P_SPEAR (objects.h:174-191).
- silver spear: SILVER material, cost 40, +d20 vs silver-haters (objects.h:186-188; artifact.c spec_dbon).
- Valkyrie starts with a plain spear and trains to Expert (u_init.c:160-161, 537).
- spear kebab bonus: +2 to-hit vs xorns, dragons, jabberwocks, nagas, giants (weapon.c:71-73, 167-168, is_spear).
- trident uses P_TRIDENT, a separate skill from spears (objects.h:195 P_TRIDENT).
- +1 thrown-spear multishot belongs to Caveman (PM_CAVE_DWELLER), NOT Valkyrie (dothrow.c:47-52).
- Valkyrie has no class-specific spear multishot, only the generic Expert ceiling (dothrow.c).
-->

槍類はすべて同じスキルを共有します。トライデントは別のスキルを使用します（後述）。ワルキューレ（Valkyrie）は通常の槍を持ってスタートし、エキスパートまで鍛えることができます。槍の投擲マルチショットの真のスペシャリストは**洞窟人（Caveman）**です。洞窟人は投げた槍（通常の槍、銀の槍、ジャベリンのいずれでも）に対してマルチショット+1のボーナスを得るため、束ねたジャベリンは彼らにとって強力な遠距離攻撃手段となります。

槍は大型モンスター（ゾーン、ドラゴン、ジャバウォック、ナーガ、巨人）に対して**命中+2のボーナス**（串刺しボーナス / kebab bonus）を得られます。

::: dense-table

| 武器名 | ダメージ (小/大) | 重量 | 価格 | 命中 | 材質 | 備考 |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| 槍 (spear) | 1d6 / 1d8 | 30 | 3 | — | 鉄 | 投擲可能。ワルキューレの初期装備。 |
| エルフの槍 (elven spear) | 1d7 / 1d8 | 30 | 3 | — | 木 |  |
| オークの槍 (orcish spear) | 1d5 / 1d8 | 30 | 3 | — | 鉄 |  |
| ドワーフの槍 (dwarvish spear) | 1d8 / 1d8 | 35 | 3 | — | 鉄 |  |
| 銀の槍 (silver spear) | 1d6 / 1d8 | 36 | 40 | — | 銀 | 悪魔や獣人に対して銀特効ダメージ。 |
| ジャベリン (javelin) | 1d6 / 1d6 | 20 | 3 | — | 鉄 | スタック可能な投擲武器。洞窟人は遠距離から連射できる。 |

:::
