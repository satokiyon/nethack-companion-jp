#### 平和主義者 (Pacifist)

<!-- audit
2026-05-19:
- Pacifist tracks u.uconduct.killer; only xkilled (mon.c:3500) and pet-pushed-into-trap (hack.c:2201) increment
- pet kills and conflict kills do NOT break the conduct: xkilled() only increments on !noconduct branch (mon.c:3499-3502)
- charm-monster spell, Elbereth, and pet tactics are all safe (no killer++ in those code paths)
- strategy aligned with NetHackWiki Pacifist, Conflict: pacifist runs lean on strong pets (often polymorph-amplified) and a ring of conflict for crowds (https://nethackwiki.com/wiki/Pacifist, https://nethackwiki.com/wiki/Conflict)
-->

いかなるモンスターも自らの手で殺害してはいけません。ペットによる撃破や、争い（Conflict）によってモンスター同士が殺し合った結果は、このコンダクトを破棄しません（ただしペットを押しのけて致命的な罠に突き落として殺す行為は違反となります）。平和主義者ランでは、戦闘をペットに任せ、群衆には争いの指輪を用い、[エルベレス](#elbereth) で怪物を寄せ付けない戦術を取ります。

平和主義者での昇天は十分に可能ですが、ダンジョンのルールに対する深い洞察が求められます。終盤の定番戦略は、願った **アルコンの小像**（割って出現させ、敵対した場合は再テイムする）を最強のチャンピオン闘士として育成し、怪物を手懐ける（魅了）呪文で群衆を鎮め、話し合いで解決できない局面を争いの指輪で乗り切ることです。

