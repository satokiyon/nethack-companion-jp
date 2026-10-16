---

#### ゲヘナ (Gehennom) {#gehennom}

<!-- audit
2026-05-19:
- Asmodeus carries wands of cold AND fire (makemon.c:804-807)
- Asmodeus is fire-, cold-, AND poison-resistant: MR_FIRE|MR_COLD|MR_POISON (monsters.h:3124)
- Baalzebub: AT_BITE/AD_DRST (drain Str, poisonous) + AT_GAZE/AD_STUN (stun) — NO gas cloud, NO fly summons (monsters.h:3110-3119)
- Baalzebub's lair is beetle-shaped (mkmaze.c:471 baalz_fixup)
- demon-lord teleport blocked (teleport.c:21-34)
- Geryon/Dispater/Baalzebub/Asmodeus are the bribable major demons (MS_BRIBE) — minion.c:309-311 sets bribe price
- Vlad's throne effect rate: only rnd(6) > 4 (= 1/3 of sits) triggers anything; 4/13 of those are the wish (sit.c:45, 238-353)
- so unconditional wish rate is (1/3)·(4/13) = 4/39 ≈ 10%; ~10 sits average, ~7 bad effects absorbed
- Orcus drops magic lamp or magic marker, 50/50 (orcus.lua:107-111)
- Sanctum has noteleport + nommap (sanctum.lua:8)
- Valley of the Dead has noteleport + nommap + non-diggable walls (valley.lua:10, 74)
- strategy aligned with NetHackWiki Gehennom, Bribe, Demon lords and princes: prayer dead, bribery (gold in open inventory) for the lawful demon princes, Excalibur disables bribery, dig don't navigate (https://nethackwiki.com/wiki/Gehennom, https://nethackwiki.com/wiki/Bribe, https://nethackwiki.com/wiki/Demon_lords_and_princes)
- blessed scroll of genocide on class 'L' wipes lich/demilich/master lich/arch-lich (read.c:2638-3015 do_class_genocide, monsters.h:1864-1899 four S_LICH entries); Wizard of Yendor is S_HUMAN (monsters.h:2847-2858), not affected
-->

[城](#the-castle) の下層では、ダンジョンはその様相を一変させます。直線的な通路は迷路（メイズ）へと姿を変え、一般的なモンスターは凶悪な悪魔たちへと取って代わられます。何よりも恐ろしいのは、あなたの神が沈黙することです。ゲヘナでは祈りが一切通じず、ここから先は城で整えた所持品だけを頼りに生き延びなければなりません。
