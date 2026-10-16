#### 脳みそ吸引・脳死 (Brainlessness) {#brainlessness}
<!-- audit
2026-05-18:
- mind flayer 3 tentacles, master 5 tentacles; AD_DRIN + AT_WEAP 1d8 (monsters.h:523-535)
- INT loss rnd(2) per hit; up to 10 lost per turn from a master (uhitm.c:3263)
- brainlessness death; lifesaving still dies (eat.c:698-715)
- 1-in-5 chance of losespells per hit (uhitm.c:3264)
- losespells zeroes rn2(n+1) random spells; re-study restores them (spell.c:1759-1827)
- 5.0 AD_DRIN no longer wipes maps or item IDs — only spells (uhitm.c:3263-3271: only adjattrib INT, losespells, drain_weapon_skill — no forget_map/forget_objects calls)
- polymorphed into a mindflayer, brain-eating restores Int (eat.c:679-688)
- any helmet blocks 7/8 tentacle drains via `uarmh && rn2(8)` (uhitm.c:3235)
- greasing adds an extra slip-roll on top of the helmet check (uhitm.c:3232 → u_slip_free at mhitu.c:1047-1064)
- blessed potion of restore ability restores all lost attributes (potion.c:646-691)
- blessed potion of full healing does NOT restore stats (potion.c:1144-1162)
- prayer fixes drained attributes via TROUBLE_POISONED (pray.c:270-272, 547-552)
- unicorn horn no longer restores attributes in 5.0 (apply.c:2306-2327)
- strategy aligned with NetHackWiki Mind flayer, Helm: any helmet blocks 7/8 tentacles, greasing stacks slip-roll, range-kill is safest (https://nethackwiki.com/wiki/Mind_flayer, https://nethackwiki.com/wiki/Helm)
-->

マインドフレアは、その触手攻撃によってプレイヤーの「知力（Intelligence）」を直接吸い取ってきます。知力が種族の最低値（人間なら3）まで低下すると、次の吸引によって即死します（死因：脳死／brainlessness）。通常のマインドフレアは1ターンに3回の触手攻撃を行い、**マスターマインドフレア** は *5回* の触手攻撃に加えて強力な武器攻撃を繰り出してきます。無防備な状態でマスターマインドフレアと隣接すれば、たった1ターンで知力を最大10ポイント削り取られて死に至ることがあります。

**防御策：** どんなものであれ **兜（ヘルメット）を着用していれば、触手による知力ドレインを8分の7（約87.5%）の確率で弾き返します**。兜に防水用の油（grease）を塗っておけば、さらに滑って回避できる確率が上乗せされます。マインドフレアの生息域に足を踏み入れる際は、油を塗った兜の着用が標準的なエチケットです。さらに言えば、そもそも隣接されないよう遠距離攻撃（杖や呪文）で仕留めるのが最善です。
もうひとつの重要な詳細として、マインドフレアの「精神波（mind blast）」はテレパシーで感知されている状態では百発百中で飛んできますが、テレパシーを遮断していれば発動率は10分の1に激減します。遠視の魔除けを外すことで危険を大幅に減らせます（完全にゼロにはなりませんが）。
ドレインされた知力を回復するには、**能力回復の薬 (potion of restore ability)**（呪われていないは1つの能力値、祝福は全能力値を回復）、能力回復の呪文、または神との関係が良好な状態での祈りが必要です。なお、**NetHack 5.0 においてユニコーンの角は低下した能力値を回復しなくなった** ため、ユニコーンの角に頼ってはいけません。マインドフレアの巣窟に突入する前に、必ず能力回復の薬を少なくとも1本はストックしておきましょう。
