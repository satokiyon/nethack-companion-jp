### 自主的挑戦 (Voluntary Challenges)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- vegetarian-safe puddings: gray ooze, brown pudding, green slime; not black pudding (mondata.h:241). Puddings leave globs, not corpses.
- Vegan excludes fortune cookies (they contain eggs).
- Foodless is not broken by polymorph (polyself.c only increments u.uconduct.polyselfs).
- Verified correct: all conduct triggers/checks, Pauper starting kit, Petless/Permadeaf/Bonesless/Sokoban mechanics, all roleplay flags.
-->

NetHack を一度クリア（昇天）した冒険者の多くは、さらなる高みを目指してゲームが本来許容している強力な手段を自らに禁じる「自主的挑戦（コンダクト / Conducts）」に挑みます。ゲームはこれらの行動制限を裏で厳密に追跡しており、昇天時や死亡時に遵守したコンダクトが公式に認定・表彰されます。

::: dense-table

| コンダクト名 | 破棄される条件 | 開始方法 |
|---------|----------------|---------------|
| 菜食主義者 (Vegetarian) | 肉や禁じられた動物性食品を食べる | 自動開始 |
| 完全菜食主義者 (Vegan) | あらゆる動物性食品を口にする | 自動開始 |
| 絶食 (Foodless) | 壁の咀嚼を含め、いかなるものも口にしない | 自動開始 |
| 無神論者 (Atheist) | 祈る、生贄を捧げる、アンデッド退散、僧侶と会話、祭壇でのBUC判定 | 自動開始 |
| 武器なし (Weaponless) | 装備した武器や武器道具で敵を殴る | 自動開始 |
| 平和主義者 (Pacifist) | 自身の戦果として記録されるモンスターの殺害 | 自動開始 |
| 文盲 (Illiterate) | 読む、または単一の `x` を超える文字を刻む | 自動開始 |
| 虐殺なし (Genocideless) | モンスター種族またはクラスを虐殺する | 自動開始 |
| 自己変身なし (Polyselfless) | 自分自身の姿を変身させる | 自動開始 |
| アイテム変身なし (Polypileless) | アイテムを変身（ポリパイル）させる | 自動開始 |
| 願いなし (Wishless) | いかなる願いも叶えてもらう | 自動開始 |
| アーティファクト願いなし | アーティファクトを願う（拒絶された場合も含む） | 自動開始 |
| 裸族 (Nudist) | いかなる防具も身につけない | `OPTIONS=nudist` |
| 盲目 (Blind / Zen) | 全盲状態がゲーム全編を通じて持続 | `OPTIONS=blind` |
| 赤貧 (Pauper) | 何も持たずに開始する（5.0新要素） | `OPTIONS=pauper` |
| ペットなし (Petless) | いかなるモンスターも手懐けない（5.0新要素） | `OPTIONS=pettype:none` |
| 完全聾 (Permadeaf) | 聴覚喪失がゲーム全編を通じて持続（5.0新要素） | `OPTIONS=permadeaf` |
| 倉庫番 (Sokoban) | 進入後に巨岩ルールを破る（5.0新要素） | 進入時に自動開始 |
| ボーンズなし (Bonesless) | ボーンズ階層の生成を無効化（5.0新要素） | `OPTIONS=!bones` |
| 振り直しなし (Unrerolled) | 最初に提示されたキャラクターをそのまま受け入れる | 最初のキャラを受け入れ |

:::

