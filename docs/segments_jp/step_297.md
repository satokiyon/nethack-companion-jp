### 呪文一覧表 (Spell Tables) {#spell-tables}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h: no corrections. All 41 spell rows' level/school/type verified (incl. chain lightning lvl 2). Spell damage figures live in spell.c/zap.c, outside this table's source.
-->
<!-- audit
2026-05-19:
- 41 spells, sourced from objects.h SPELL() macros (P_ATTACK..P_MATTER); SPELL macro signature at objects.h:1277-1281, oc_level=oc_oc2.
- attack spells at objects.h:1297-1330 (force bolt/magic missile/drain life/cone of cold/fireball/finger of death/chain lightning).
- healing spells at objects.h:1313-1408 (healing/cure blindness/cure sickness/extra healing/stone to flesh/restore ability).
- divination spells at objects.h:1308-1384 (light/detect monsters/detect food/clairvoyance/detect unseen/identify/detect treasure/magic mapping).
- enchantment spells at objects.h:1305-1354 (confuse monster/slow monster/cause fear/sleep/charm monster).
- cleric spells at objects.h:1337-1400 (protection/create monster/remove curse/create familiar/turn undead).
- escape spells at objects.h:1355-1404 (jumping/haste self/invisibility/levitation/teleport away).
- matter spells at objects.h:1293-1407 (knock/wizard lock/dig/polymorph/cancellation/stone to flesh).
- Flame sphere and freeze sphere are `#if 0 DEFERRED` (objects.h:1413-1422), NOT shipped in 5.0.
- Chain lightning is level 2 per macro (objects.h:1409-1411); body table at line 4986 and What's New at 8585 still say L4: follow-up fix.
- Magic missile IS Antimagic-blocked (zap.c:4410-4419, "missiles bounce off!"), NOT unresistable.
- Finger of death: monster MR resists, but player gets no Antimagic check on death-ray instakill (zap.c:2885-2902).
- Clairvoyance gets a P_SKILLED upgrade detecting nearby monsters per pulse (spell.c:1572-1576).
- Fireball/cone of cold become aimed explosions at P_SKILLED (spell.c spelleffects).
- Remove curse/confuse monster/detect food/cause fear/identify/charm monster get blessed-scroll behavior at P_SKILLED.
- Haste self/detect treasure/detect monsters/levitation/restore ability get blessed-potion behavior at P_SKILLED.
- Protection doubles uspmtime at P_EXPERT (spell.c:1169); jumping distance scales with role_skill.
- Charm monster is untargeted (read.c:1679-1708 seffect_taming is area-centered-on-caster, no direction prompt).
- Charm monster area: 3×3 normal, 11×11 confused (`bd = confused ? 5 : 1`, -bd..bd inclusive), NOT 5×5. (read.c:1689 seffect_taming)
- Charm monster P_SKILLED upgrade is blessed-scroll reliability, NOT a radius bump. (spell.c:1524-1525 sets pseudo->blessed when role_skill >= P_SKILLED; read.c:1689 radius `bd` depends only on `confused`, not on blessed)
- Cause fear blessed and uncursed are identical (read.c:1454-1486); loop hits every visible monster on the level, not just nearby.
- Remove curse blessed branch uncurses every non-coin inventory item (read.c:1514-1577), NOT just worn/wielded.
-->

魔法書の完全カタログです。系統順、続いてレベル順に並んでいます。**レベル (Lvl)**は呪文レベル、**消費魔力 (Pw cost)**は常に「5×呪文レベル」です。**種別 (Type)**は呪文の目標指定方法を区分しています：

- **方向指定 (aimed):** 方向を指定し、その直線の1マスに命中します。
- **光線 (ray):** 術者から直線状に伸び、遮られるまで進むビームです。
- **目標不要 (untargeted):** 方向指定は不要で、自身、フロア全体、または固定範囲に効果が発現します。

**上位効果 (Upgrade)**はその系統のスキルが**熟練 (Skilled)**以上になった際の挙動変化です（防護の呪文のみエキスパートで発動し、跳躍の距離はランクに応じて連続的に拡大します）。

::: dense-table

| 呪文名 | 系統 | レベル | 種別 | 効果 | 上位効果 (Skilled以上) |
|-----------------|-------------|-----|------------|-------------------------------------|-------------------------------|
| 衝撃 (force bolt) | 攻撃 | 1 | 方向指定 | 2d12の魔法打撃ダメージ | — |
| 連鎖雷撃 (chain lightning) | 攻撃 | 2 | 目標不要 | 周囲のモンスターに電撃ダメージ | — |
| 生命吸収 (drain life) | 攻撃 | 2 | 方向指定 | 対象から経験値レベルを1吸収 | — |
| マジックミサイル (magic missile) | 攻撃 | 2 | 光線 | (XL÷2 + 1)d6の衝撃ビーム（端数切捨て）。魔法防御で防がれる | — |
| 冷気 (cone of cold) | 攻撃 | 4 | 光線 | (XL÷2 + 1)d6の冷気ビーム（端数切捨て） | 目標指定の爆発 |
| 火の玉 (fireball) | 攻撃 | 4 | 光線 | (XL÷2 + 1)d6の火炎ビーム（端数切捨て） | 目標指定の爆発 |
| 死の指 (finger of death) | 攻撃 | 7 | 光線 | 死の光線。敵の魔法防御で防がれるが、自身に反射・誤射した際は防御チェックを迂回して即死する | — |
| 回復 (healing) | 回復 | 1 | 方向指定 | HPを回復 | 盲目も治療 |
| 盲目治療 (cure blindness) | 回復 | 2 | 目標不要 | 盲目状態を回復 | — |
| 病気治療 (cure sickness) | 回復 | 3 | 目標不要 | 食中毒および病気を治療 | — |
| 超回復 (extra healing) | 回復 | 3 | 方向指定 | より多くのHPを回復 | — |
| 石化解除 (stone to flesh) | 回復 | 3 | 方向指定 | 石像を生きたモンスターに変える。石化を治療 | — |
| 能力回復 (restore ability) | 回復 | 4 | 目標不要 | 低下した能力値を1つ全快 | 低下したすべての能力値を全快 |
| 怪物探知 (detect monsters) | 占術 | 1 | 目標不要 | フロア上のモンスターを表示 | 効果時間が延長 |
| 灯り (light) | 占術 | 1 | 目標不要 | 現在の部屋を照らす | — |
| 食料探知 (detect food) | 占術 | 2 | 目標不要 | フロア上の食料を表示 | 有害な食事の前に警告 |
| 千里眼 (clairvoyance) | 占術 | 3 | 目標不要 | 周囲のマップを周期的に開拓視認 | 熟練：周期ごとに周囲のモンスターも探知 |
| 不可視探知 (detect unseen) | 占術 | 3 | 目標不要 | 不可視のモンスターや罠を表示 | — |
| 識別 (identify) | 占術 | 3 | 目標不要 | 所持品を1つ識別 | 複数の所持品を一括識別 |
| 宝探知 (detect treasure) | 占術 | 4 | 目標不要 | フロア上のすべてのアイテムを表示 | 探知したアイテムの種別を識別 |
| 地図化 (magic mapping) | 占術 | 5 | 目標不要 | フロア全体の地形を開拓表示 | — |
| 怪物混乱 (confuse monster) | 付与 | 1 | 目標不要 | 次の近接攻撃で対象を混乱させる | 複数回の攻撃分チャージされる |
| 怪物減速 (slow monster) | 付与 | 2 | 方向指定 | 対象モンスターの移動速度を低下 | — |
| 恐怖 (cause fear) | 付与 | 3 | 目標不要 | 視界内のモンスターを逃走させる | — |
| 眠り (sleep) | 付与 | 3 | 光線 | 射線上のモンスターを眠らせる | — |
| 魅了 (charm monster) | 付与 | 5 | 目標不要 | 周囲 3×3 エリアのモンスターを手懐ける | — |
| 防護 (protection) | 聖職 | 1 | 目標不要 | 魔力を消費して一時的なACボーナスを得る | **エキスパート**: 効果時間が2倍 |
| 怪物創造 (create monster) | 聖職 | 2 | 目標不要 | 近くにランダムなモンスターを召喚 | — |
| 解呪 (remove curse) | 聖職 | 3 | 目標不要 | 装備中のアイテムの呪いを解く | 所持している全アイテムの呪いを解く |
| 使い魔創造 (create familiar) | 聖職 | 6 | 目標不要 | 手懐けられたペットを召喚する | — |
| アンデッド退散 (turn undead) | 聖職 | 6 | 方向指定 | アンデッドや悪魔にダメージを与えて逃走させる | — |
| 跳躍 (jumping) | 離脱 | 1 | 目標不要 | 近くの指定したマスへ跳躍する | スキルランクに応じて跳躍距離が拡大 |
| 加速 (haste self) | 離脱 | 3 | 目標不要 | 一時的な高速移動状態になる | 効果時間が延長 |
| 透明化 (invisibility) | 離脱 | 4 | 目標不要 | 透明状態になる | — |
| 浮遊 (levitation) | 離脱 | 4 | 目標不要 | 落とし穴や水面の上に浮かび上がる | `>` キーで任意に着地可能 |
| テレポート (teleport away) | 離脱 | 6 | 方向指定 | 対象をフロアの別の場所へテレポートさせる | — |
| 開錠 (knock) | 物質操作 | 1 | 方向指定 | 扉を開け、錠前を解除する | — |
| 施錠 (wizard lock) | 物質操作 | 2 | 方向指定 | 扉を閉じて鍵をかける | — |
| 穴掘り (dig) | 物質操作 | 5 | 光線 | 壁、岩、床を掘り抜く | — |
| 変化 (polymorph) | 物質操作 | 6 | 方向指定 | 対象を変身(へんげ)させる | — |
| 無力化 (cancellation) | 物質操作 | 7 | 方向指定 | 対象の魔法特性を打ち消す | — |

:::

光線系呪文（睡眠、マジックミサイル、死の指、および未熟練状態の冷気や火炎）の命中率も、スキルランクに応じて上昇します。
