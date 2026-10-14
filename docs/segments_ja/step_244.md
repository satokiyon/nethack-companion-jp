#### 無神論者 (Atheist)

<!-- audit
2026-05-19:
- Atheist tracks u.uconduct.gnostic (insight.c:2134, topten.c:590)
- breaks on: #pray (pray.c:2221), #offer corpse (pray.c:1977), #turn (pray.c:2426), #chat with priest (priest.c:572)
- dropping any non-coin on an altar breaks the conduct via the BUC flash (do.c:370)
- final Amulet offering for ascension is exempt (pray.c:1529-1588 has no gnostic increment)
- Priest's starting holy water does NOT auto-break the conduct (u_init.c:716-722)
- strategy aligned with NetHackWiki Atheist: no prayer / sacrifice / chat-with-priest / altar drops; final ascension Amulet offering is exempt (https://nethackwiki.com/wiki/Atheist)
-->

神仏とのいかなる交わりも絶ちます。具体的には：**`#pray`（祈る）を行わない**、祭壇で死体を **`#offer`（捧げる）を行わない**、アンデッドを **`#turn`（退散させる）を行わない**、そして寺院の僧侶と **`#chat`（会話する）を行わない** ことです。祭壇によるBUC判定の閃光も神聖な接触とみなされるため、金貨以外のアイテムを祭壇の上に落とす行為も失格となります（祭壇識別トリックは使用不可）。これにより、餓死、石化、病気、呪われた装備に対する神の救済という安全網が完全に失われます。

祈りで空腹を治せないため安定した食料確保が必須となり、生贄や祭壇BUCが使えないため識別の難易度が跳ね上がり、神からのアーティファクト下賜も望めません。ただし、星界の面で昇天を果たすための最終的なイェンダーの魔除けの奉納だけは例外として許されており、無神論を維持したまま昇天を完遂することが仕様上可能です。

