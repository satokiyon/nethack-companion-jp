#### 願いの制限 (Wishing Restrictions)

<!-- audit
2026-05-19:
- u.uconduct.wishes and u.uconduct.wisharti are separate counters with separate xlogfile achievements (you.h:157-158, topten.c:596-597)
- wishing for the literal string "nothing" doesn't tick the counter (zap.c:6369)
- Amulet-of-Yendor first-pickup wish must be declined for wishless (allmain.c:445)
- wisharti ticks even for DENIED artifact wishes: increment is before the deny branch (objnam.c:5362-5365)
- fountain water demon routes through mongrantswish -> makewish
- wresting empty wands routes through makewish (zap.c:2583)
- strategy aligned with NetHackWiki Conduct, Wish: wishless vs no-wishing-for-artifacts are separately tracked, "nothing" is the canonical escape for a forced wish (https://nethackwiki.com/wiki/Conduct, https://nethackwiki.com/wiki/Wish)
-->

願いに関する2つの独立したコンダクトがあります：

**願いなし (Wishless)。** いかなる願いも叶えてもらってはいけません。杖、泉、煙の立つ薬のジン、玉座、その他すべての入手源からの願いを拒絶します。**イェンダーの魔除けを拾った瞬間に発生する願いプロンプト** においても、文字列として **"nothing"**（何もない）と入力すれば、願いカウンターを進めずにパスできます（"nothing" の入力は、あらゆる強制的な願いプロンプトを安全にやり過ごす標準的な脱出口です）。ダンジョンが偶然ドロップしてくれなかった必需品（銀色ドラゴンの鱗鎧、韋駄天の靴、軽量化の鞄など）を願いで補うことが一切できないため、極めて過酷な挑戦となります。

**アーティファクト願いなし (No wishing for artifacts)。** 通常のアイテムを願うことは許されますが、アーティファクトを願うことだけを禁じます。これにより、[グレイスワンダー](#grayswandir) や [エチオピカの目](#eye-of-the-aethiopica) といった最強の至宝を即座に手に入れる最も効率的な戦略が封じられ、日用品や基本装備の補給だけに願いが限定されます。なお、アーティファクトを願って **拒絶された場合（手元に普通のアイテムが出現した場合）であってもカウンターは加算される** ため、誤ってアーティファクト名を指定しないよう注意してください。

