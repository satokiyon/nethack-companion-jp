#### 複合コンダクト (Combining Conducts) {#combining-conducts}

<!-- audit
2026-05-19:
- Pauper does NOT suppress the starting pet; makedog() only returns NULL on pettype:none (dog.c:219-229)
- only OPTIONS=pettype:none can skip the starting pet
- nudist and blind have been tracked since 3.6
- 5.0 added pauper, petless, permadeaf, sokoban, bonesless
- vegan is a strict subset of vegetarian
- all conducts appear in the show_conduct end-screen
-->

複数のコンダクトを組み合わせることで、難易度は跳ね上がります。ベジタリアン無神論者はどちらか単体よりも遥かに困難です。そして平和主義者・文盲・完全菜食・絶食・無神論・素手戦闘の全乗せ（いわゆる「フルコンダクト」）は、もはや伝説の領域であり、実際に達成者が存在します。規模感の目安として：公開サーバー NAO において、昇天者の約9人に1人が「願いなし」を達成していますが、「絶食」を達成しているのは約80人に1人に過ぎません。

近年の NetHack では、公式に記録されるコンダクトがさらに拡張されました：

**裸族 (Nudist)。** 鎧、シャツ、マント、小手、靴、兜、盾など、いかなる防具も身につけてはいけません。ゲーム開始時に `OPTIONS=nudist` を設定します。ダンジョン全体を下着一丁で戦い抜くことになります（NetHack 3.6 から公式追跡）。

**盲目 (Blind / Zen)。** ゲーム全編を視覚なしでプレイします。ゲーム開始時に `OPTIONS=blind` を設定します。移動と戦闘にはテレパシーやその他の知覚手段が不可欠となります（NetHack 3.6 から公式追跡）。

NetHack 5.0 では、さらに6つの追跡コンダクトが追加されました：赤貧 (Pauper)、ペットなし (Petless)、完全聾 (Permadeaf)、[倉庫番](#sokoban)、ボーンズなし (Bonesless)、そして振り直しなし (Unrerolled) です。Pauper、Permadeaf、Petless、Bonesless はゲーム開始前のオプション設定で宣言します。Sokoban はプレイ中の実際の行動に基づいて自動追跡され、Unrerolled はゲームが最初に提示したキャラクターを受け入れたことを記録します。
