### 食料と食事 (Provisions and Dining) {#provisions-and-dining}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Only yellow mold is poisonous to eat (M1_POIS); brown/red convey poison resistance but aren't poisonous, green is acidic (monsters.h). Was "most are poisonous".
- Verified correct: ration/lembas nutrition & weight, hunger thresholds, tin-open times, cannibalism -2..-5 + aggravate, corpse-intrinsic mappings.
-->
<!-- audit
2026-05-21:
- vegan classes: S_BLOB, S_JELLY, S_FUNGUS, S_VORTEX, S_LIGHT, S_ELEMENTAL (except stalker), S_GOLEM (except flesh/leather), and noncorporeal (S_GHOST) (mondata.h:232-238)
- vegetarian = vegan + S_PUDDING except black pudding (mondata.h:239-241); brown pudding and gray ooze are vegetarian, black pudding is not
- corpse_intrinsic picks one mconveys property uniformly at random per eat, then should_givit rolls mlevel/15 (or mlevel-vs-rn2(15)); killer bee/scorpion poison-res has a 25% boosted-chance branch (eat.c:961-989, 1351-1373)
2026-05-20:
- tin opening is an occupation; opentin is called per turn, gives up after svc.context.tin.usedtime >= 50 turns (eat.c:1710-1719, 1794)
- tin open time by tool: blessed tin opener wielded = 0; uncursed tin opener rn2(2); cursed rn2(3); dagger family = 3; axe/pick-axe = 6; bare hands = rn1(1 + 500/(Dex+Str), 10) which is ~11-26 at avg stats, up to the 50-turn cap (eat.c:1740-1786)
- tin of spinach grants +1 Str on eat (eat.c spinach branch)
2026-05-18:
- gelatinous cube corpse: fire/cold/shock/sleep only (not poison/acid/stoning) (monsters.h:160-162 mresists has MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON|MR_ACID|MR_STONE but mconveys row is MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP only)
- disenchanter corpse STRIPS an intrinsic, doesn't grant one (eat.c:1270-1275 PM_DISENCHANTER calls attrcurse)
- encumbrance kicks in at Stressed, not Burdened (eat.c:3197 near_capacity > SLT_ENCUMBER)
- fire giant corpse grants Str on eat via is_giant(ptr) (eat.c:1345-1352); separate row from fire ant
- red and brown mold corpses also grant poison resistance (monsters.h:1627-1659, MR_POISON defense)
- eggs count as vegetarian but not vegan (eat.c:585-597 violated_vegetarian and EGG handling)
- Weak status is -1 Str ATEMP, not slowed movement (attrib.c:471, eat.c:3455)
- blessed tin opens instantly only with a blessed tin opener (eat.c:1740-1745)
- ordinary tin opener on a blessed tin: 50/50 instant vs one turn via rn2(2)
- globs lose 1 weight per ~25 turns; a weight-20 glob lasts ~500 turns (mkobj.c:1487-1490)
- corpses stay safe to eat for ~30-50 turns before rotting (eat.c:1887-1939)
- strategy aligned with NetHackWiki Resistance, Poison resistance, Partial intrinsic: corpse-eating to bank resistances is canonical, gelatinous cube and dragon corpses are the highest-density sources (https://nethackwiki.com/wiki/Resistance, https://nethackwiki.com/wiki/Poison_resistance, https://nethackwiki.com/wiki/Partial_intrinsic)
- sprig of wolfsbane cures lycanthropy on eat via you_unwere (eat.c:2513-2516)
-->

空腹は、ダンジョンにおいて最も執拗にプレイヤーを追い詰めるタイマーです。行動するごとに毎ターン栄養が消費され、タンクが空になると失神が始まります。食事を取らずに失神を繰り返せば、やがて飢餓死するか、倒れ込んでいる隙に部屋にいたモンスターに撲殺されることになります。
