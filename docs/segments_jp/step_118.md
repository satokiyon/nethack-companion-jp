#### 流し台テスト (The Sink Test (Rings))
<!-- audit
2026-05-18:
- dosinkring at do.c:498-650 — all 28 ring types give a sink message, BUT 13 only when sighted (second switch do.c:592+ gated on !Blind); 15 work even blind (first switch). Message is a hint via trycall, NOT makeknown/formal ID. Overlaps: protection & warning both "sink glows", teleportation & polymorph can both "sink vanishes", aggravate monster & meat ring near-identical fly message
- searching and slow digestion goto giveback, dropped back on the floor identified (do.c:507-516)
- other rings usually consumed: 1/20 backup chance, 1/5 buried chance (do.c:649-660)
-->

ダンジョン内で流し台（sink）を見つけたら、その中に指輪を落としてテストすることができます。指輪の種類ごとに固有の手がかりメッセージが発生します（ただしメッセージが重複するものもあり、目が見えている状態でなければ表示されないものもあるため、常に完全な正式識別になるとは限りません）。探索の指輪と[消化不良の指輪](#special-and-utility) は、落とした瞬間に手元へと跳ね返ってきて即座に識別されます。それ以外の指輪は、20分の1の確率で手元に戻り、5分の1の確率で流し台の下に埋没しますが、それ以外の場合は排水溝に飲み込まれて失われます。したがって、唯一の貴重な指輪ではなく、ダブった予備の指輪でのみ試してください。メッセージの詳細な一覧は [流し台](#sinks) を参照してください。

