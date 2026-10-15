#### 灰色石：4つの石、幸運は1つ (Gray Stones: Four Stones, One Lucky)
<!-- audit
2026-05-18:
- best mimic test here is SEARCH, not the pet: an explicit `s` adjacent to an object-mimic reveals it unconditionally — mfind0 (detect.c:1965) calls seemimic() for any M_AP_TYPE monster with NO rng roll (unlike SDOOR rnl(7-fund) / traps rnl(8)). the minend-1 mimics are appear_as="obj:..." => M_AP_OBJECT, so one search beside a suspect stone exposes it every time; a real stone stays a stone. reworked the prose to lead with search (consistent with the existing "A note on mimics" section, which already says search reveals mimics) instead of the fiddly pet-in-a-niche. search only flags mimics, so price-ID still separates the real luckstone from the cursed loadstone.
- "name it The Heart of Ahriman -> hand slips = it's the luckstone" is FAKE. restrict_name (artifact.c:575) builds sametype[] from shared description / shuffle-range; all four gray stones share descr "gray" and the o_ranges band (objects.h:1594-1604), so for ANY unidentified gray stone sametype includes luckstone -> naming it the Heart (SPFX_RESTR) trips the restriction -> "While engraving, your %s slips." (do_name.c:330-351) identically for luckstone/loadstone/touchstone/flint. the slip only confirms "unidentified gray stone," which you already know; it cannot single out the luckstone.
- other two layouts: minend-2 ("Gnome King's Wine Cellar") luckstone is at fixed (70,5) in a walled gem-pile vault, NO stone decoys. minend-3 ("Catacombs") luckstone (place[2]) + flint decoy (place[1]) are shuffled among 3 spots, and there is a level-teleport trap under BOTH (lines 89-90, "one-time annoyance") — stepping onto the prize can fling you off-level.
- BUC/pet-test note: the minend-1 decoy loadstone IS cursed on the floor (mksobj curses all loadstones, mkobj.c:978; des.object with no buc => curse_state 0 => no override in sp_lev.c:2234). so a pet registers it as cursed and won't step on it (cursed_object_at dogmove.c:145, "avoid cursed items unless starving" dogmove.c:535). the pet thus avoids all 4 mimics AND the loadstone; the one gray-stone square it will walk onto is the uncursed luckstone. "loadstone isn't cursed until picked up" is false for floor loadstones — that idea is really the freeinv re-curse (invent.c:1386), which only bites an uncursed (wished) loadstone on REMOVAL. caveat: luring a pet into a 1-tile dead-end niche is fiddly, so price-ID stays the clean fallback.
- luckstone default BUC: a luckstone is uncursed by default — GEM_CLASS in mksobj_init (mkobj.c:976-986) never calls blessorcurse for it, and mksobj zeroes the obj (mkobj.c:1185). so the Mine's End buc="not-cursed" (=> uncurse(), a no-op) yields an UNCURSED (not blessed) luckstone. "always uncursed" in the prose is accurate.
2026-08-13:
- fixed a loadstone claim in the 5.0-changes section (was "resist knockback ... a niche use if you can keep one uncursed"): m_is_steadfast (uhitm.c:5216) grants knockback immunity for carrying ANY loadstone via m_carrying(mtmp, LOADSTONE) with NO BUC check (line 5235) — cursed works too, including the welded one. only gate is being grounded (not Flying/Levitation, not air/cloud/bubble level, lines 5224-5228). corrected the "if you can keep one uncursed" qualifier.
-->

「灰色の石」の正体は、ゲームクリアまでずっと肌身離さず持ち歩くべき「幸せの石」から、一度拾うと絶対に手放せなくなる呪われた「重し」まで、天と地ほどの開きがあります。全部で4種類存在します：

| 価格 | 石の種類 | 効果 |
| ---: | --- | --- |
|    1 | 火打ち石 (flint) **または** 重し (loadstone) | 火打ち石はスリング用の弾薬です。重しは重量が500ユニットもあり、通常呪われており、一度拾うと捨てられなくなります。蹴りテストを行ってください（重しは滑りません）。 |
|   45 | 試金石 (touchstone) | 宝石を擦り付けると正体を識別できます。極めて有用です。 |
|   60 | 幸せの石 (luckstone) | 幸運値を維持します。ゲームクリアに必須の至宝です。 |

<div class="price-id-toolbar"></div>

見分けるための手順は以下の通りです：

**蹴りテスト（キックテスト）。** 床に落ちている未識別の灰色の石を蹴ってください（`Ctrl-D` または `k`）。通常通りスッと滑って転がれば、重しではありません。重しは異常に重いため、蹴られても転がることに抵抗してその場に留まります。テストする前に、力の小手や蹴り挙げ靴を脱いでおいてください。怪力で本物の重しを強引に吹き飛ばしてしまい、安全だと誤認する危険があるからです。

**拾いテスト。** 重しは生成された時点で呪われており、呪われた重しは床に置く（ドロップする）ことが一切できなくなります。ゲーム画面に「どういうわけか、石を手放すことができない！（For some reason, you cannot drop the stone!）」と表示され、荷物袋に居座り続けます。もし灰色の石を拾い上げて不審なほど過重になったら、床に置いてみてください。置くことができなければ、呪いを解く（聖水、解呪の巻物、祈り）まで呪われた重しを背負い続ける羽目になります。呪いを解いた後であれば、安全に捨てることができます。

**価格テスト。** 基本価格において、60ゴールドは「幸せの石」、45ゴールドは「試金石」、1ゴールドは「火打ち石」または「重し」です。ただし未識別アイテムのランダム割増（1/3）によって45ゴールドの試金石が60ゴールドと提示される場合があるため、一意に確定できるのは45ゴールドの提示のみです。

**擦りテスト。** 手持ちの宝石に灰色の石を適用（`a`）するか、宝石に対して `#rub` コマンドで擦り付けてください。試金石であれば色のついた筋（ストリーク）のメッセージが表示されます。さらに試金石が **祝福** されている場合（あるいはあなたが考古学者かノームであり呪われていない試金石を持っている場合）、その筋によって宝石の正式な正体が識別されます。他の灰色の石でも似たような擦り筋メッセージが出ることがあるため、単に筋がついただけでは試金石の証明にはなりません。「宝石の正式識別」が発生して初めて試金石と確定します。なお、呪われた試金石は擦った宝石を粉砕してしまうことがあります。

**フロア配置の手がかり。** [地下鉱山](#the-gnomish-mines) の最下層（鉱山最深部：Mine's End）にある幸せの石は確定生成であり、常に呪われていないです。そのため鉱山最深部で見つかる灰色の石は十中八九本物です。ただし、フロアバリエーションの1つ（minend-1）では巧妙な罠が仕掛けられており、4体の [ミミック](#a-note-on-mimics) が灰色の石に化けており、さらに本物の呪われた重しが1個配置されています。疑わしい石の隣で捜索（`s`）を行えば、ミミックの正体を100%確実に暴くことができます。その上で、残った2つの本物の石を価格識別（60ゴールドと1ゴールド）してください。狭い小部屋の窪みでは蹴りテストは壁にぶつかって判定が狂いやすいため、価格識別が最も安全です。

灰色の石を拾い上げる前に、必ず蹴って転がるか確認し、BUCをテストしてください。数秒のテストを惜しまないだけで、背中に溶接された500ユニットの呪われた重しに苦しめられる悲劇を完全に回避できます。
