### 杖 (Wands)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Wand of Nothing is IMMEDIATE (directional), so its charge cap is 8, not 15 (read.c:739-741; mkobj.c:1123). Table said 15.
- No "cursed wand of digging zaps downward" mechanic; zap direction is BUC-independent (dig.c, zap.c). Removed.
- Recharge explosion table was off-by-one: first recharge is safe (0%), 100% is the eighth (n = previous recharges, read.c:752-768).
-->
<!-- audit
2026-05-18:
- wand of stasis: NODIR, $150, prob 45 — makes the level no-teleport for 10-30 turns; does NOT freeze monsters (objects.h:1460, zap.c:2559-2568; effect gated by stasis_until in teleport.c:43 noteleport_level, teleport.c:2269 u_teleport_mon, apply.c:530 magic whistle, do.c:2262 revive rloc)
- wand of nothing is IMMEDIATE, not NODIR (objects.h:1462)
- undead turning revives corpses to their original species via unturn_dead — NOT as zombies (zap.c:1156-1228 unturn_dead, zap.c:900 revive uses corpse->corpsenm; only cant_revive-rejected types fall back to zombie/doppelganger at zap.c:982-985)
- engrave-test: cancellation and make-invisible erase in place (engrave.c:618-633)
- engrave-test: teleportation moves the engraving elsewhere; polymorph rewrites it
- nothing, undead turning, opening, locking, probing produce NO engrave message (engrave.c:635-640)
- magic missile engraves "riddled by bullet holes" — distinctive (engrave.c:642-648)
- sleep and death share "the bugs on the <surface> stop moving" (engrave.c:651-656)
- striking message: "wand unsuccessfully fights your attempt to write" (engrave.c:602-605)
- slow/speed monster: distinctive "bugs slow down" / "speed up" (engrave.c:606-616)
- self-polymorph into a small form (sliparm) drops body armor (cursed or not) into inventory via Armor_gone+dropp (polyself.c:1198-1228); large forms (breakarm) destroy it instead (polyself.c:1162-1197)
- engrave-test ambiguity between cancellation, make-invisible, teleportation, polymorph can be resolved by zapping a known item: make-invisible turns it invisible; teleportation moves it; cancellation dulls it (zap.c:2313-2317); polymorph changes its type (zap.c:weffects branch)
- strategy aligned with NetHackWiki Wand, Engraving, Wand of wishing: engrave-test as the safest wand-ID method, $500 narrowed to death-or-wishing, wand of wishing recharge mechanics (https://nethackwiki.com/wiki/Wand, https://nethackwiki.com/wiki/Engraving, https://nethackwiki.com/wiki/Wand_of_wishing)
-->

杖は、振る（`z` を押して方向を指定）ことで指向性の効果を発揮する再利用可能な魔法のアイテムです。3つのタイプが存在します：壁で跳ね返る光線を放つ **光線（RAY）の杖**、直線上の対象に作用する **ビーム（BEAM）の杖**、そして自身の周囲に効果を及ぼす **無指向性（None）の杖** です。

光線は消滅するまでに 7〜13 マスを直進し、壁、岩、マップの端にぶつかると跳ね返ります。跳ね返った後も消滅するまで飛び続けるため、直線の一本道や数マス先の壁に向けて放つと、跳ね返った光線が自分自身に直撃し、モンスターに与えるのと全く同じ壊滅的なダメージを喰らうことになります。光線が自分から遠ざかる方向へと飛んでいくように照準を合わせてください。

杖のBUC（祝福・無呪・呪い）の状態は発動効果そのものを変えませんが、呪われた杖は振ったり試し書きしたりするたびに、約100分の1の確率で暴発して手の中で大爆発を起こします。爆風の威力は内部に残っているチャージ数に比例して増大するため、常用する杖（何よりも死の杖）は必ず呪いを解いてから使用してください。

