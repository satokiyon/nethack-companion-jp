### 感覚と物音 (Feelings and Sounds) {#feelings-and-sounds}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- "monsters are aware of your presence" comes only from a monster casting MCAST_AGGRAVATION -> aggravate() (mcastu.c:826-828); removed the "cursed ring of aggravate monster" cause (worn rings give no message, do_wear.c:1266).
- "presence of evil" is only the fountain water demon while blind (fountain.c:74); removed "or other major demon".
- Verified correct: hypocrite/Elbereth alignment hit, stealth messages, pet-kill thunder -15, curse-items cast, summoning messages, resistance-absorb messages.
-->
<!-- audit
2026-05-18:
- vault sounds: "counting gold" means vault with gold; "searching" means empty vault (sounds.c:253-262)
- "Wow! ...great!" needs blessed restore-ability with zero unfixable troubles (potion.c:658-661)
- same string also fires from a blessed magic fountain (fountain.c:257)
- non-boot stealth gear gives "move very quietly"; boots give "walk very quietly" (do_wear.c:123-129)
- lycanthropy cure is quaffing holy water, not dipping (potion.c:728-737)
- quantum corpse toggles HFast on or off: "seem faster" or "seem slower" by current state (eat.c:1227-1235)
- dosounds() is silenced by Deaf, !flags.acoustics, u.uswallow, or Underwater (sounds.c:208-209)
- bugle reveille at muse.c:843-846 is gated only by !Deaf (not by dosounds)
- sad-feeling at mon.c:3100-3101 is NOT gated by Deaf — it's a feeling, not a sound
- oracle "strange wind" (sounds.c:190); shop "cursing shoplifters" (sounds.c:322)
- fountain "bubbling water" or "water falling on coins" (sounds.c:214-218)
-->

迷宮の何気ない環境描写（メッセージ）の中には、極めて重要な警告が隠されています。まずは最も重要な4つの緊急メッセージを覚え、より珍しいメッセージが表示されたら後述の表でその意味を確認できるようにしましょう。

（注意：**耳が聞こえない（聾・Deaf）**、モンスターに **丸呑みされている**、あるいは **水中** にいる間は、環境音に関するメッセージが一切届かなくなります。特に永久聾の縛りプレイでは、フロアの雰囲気から得られるあらゆる手掛かりを失うことになります。ただし、死体を食べたときに得られる感覚のメッセージはそのまま表示されます。）
