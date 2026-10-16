---

### 呪いとその解除法 (Curses and How to Break Them) {#curses-and-how-to-break-them}

<!-- audit
2026-07-30: audited with The Armory vs NetHack-5.0 source; remove-curse scope (uncursed=worn, blessed=all; read.c:1524), confused-cursing, prayer uncurse, autocurse-9/10 items verified. No corrections.
-->
<!-- audit
2026-05-18:
- bones items are 80% cursed at pickup (bones.c:290)
- rings of teleport/polymorph and amulet of strangulation generate 90% cursed (mkobj.c:1063-1066, 1143-1147)
- cursed bag of holding doubles its contents' weight (mkobj.c:1950-1953)
- confused remove-curse uncurses 25/curses 25/no-op 50 per item (read.c:1556-1557, mkobj.c:1846-1852)
- blessed remove-curse hits all worn+carried; uncursed only worn (read.c:1524, 1549)
- temple priests do NOT reveal BUC for a fee; only Priest CLASS sees BUC free (priest.c:629-718 sets HClairvoyant + Protection, not bknown)
- shop price-id can infer BUC indirectly
- strategy aligned with NetHackWiki BUC, Scroll of remove curse, Potion of holy water: altar/pet test, blessed remove-curse hits entire inventory, holy water dip uncurses (https://nethackwiki.com/wiki/BUC, https://nethackwiki.com/wiki/Scroll_of_remove_curse, https://nethackwiki.com/wiki/Potion_of_holy_water)
- polymorph into a sliparm form drops body armor (cursed or not) into inventory (polyself.c:1198-1228)
-->

遅かれ早かれ、あなたは呪われた装備を身につけてしまうことになります。事前にテストしなかった指輪かもしれません。ボーンズ階層で拾った靴かもしれません。あるいは、モンスターがあなたの持ち物に触れて呪いをかけたことに気づかなかったのかもしれません。何が原因であれ、外すことを頑なに拒むアイテムを身につけ、おそらく何か恐ろしい災難に見舞われているはずです。呪いを解かない限り、それを脱ぎ捨てることはできません。
