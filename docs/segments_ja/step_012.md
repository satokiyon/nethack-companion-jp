#### 属性 (Alignment)

秩序 (Lawful)、中立 (Neutral)、混沌 (Chaotic) という3つの属性を、一般的な「善・中庸・悪」と捉えてしまいがちですが、NetHack はそうした道徳的な善悪でプレイヤーを裁くわけではありません。本作における属性とは、**「自分が信仰する神の教義や戒律をどれほど忠実に守り抜いているか」を測る客観的な数値（属性信仰値）**なのです。

敵対的なモンスターを討ち倒せば、通常はこの数値が上昇します。逆に、平和的な（友好的・中立的な）モンスターを殺害すると、どの属性であっても属性値が即座に5ポイント削られ、理不尽な虐殺は幸運 (Luck) の喪失という重い罰を招きます。一部の役職にはさらに固有の厳しい戒律が存在します。騎士が無力な敵を攻撃すると騎士道違反として評価を失い、侍が平和的な者に斬りかかれば武士の義理を欠いたとして手痛いペナルティを受けます。傷ついた属性値は、通常の敵対モンスターを討伐することや、祭壇に新鮮な[生贄](#sacrifice)を捧げることで回復できます。

属性はまた、信仰する神、挑むべき固有のクエスト、そして触れても安全なアーティファクトを決定づけます。秩序のキャラクターは経験レベル5 (XL 5) 以上で噴水からエクスカリバーを引き抜く資格を得ます。盗賊は常に混沌であり、ドワーフは常に秩序です。祭壇に関する詳細なルールについては、[祭壇と属性](#altars-and-alignment)を参照してください。

---

<!-- audit
2026-05-18:
- tripe rations are dog food for typical PCs (eat.c:2138-2145)
- orcs and carnivores enjoy tripe (eat.c:2132-2136)
- altar BUC flash is amber/black and sets bknown (do.c:363-389)
- pets avoid cursed items (dogmove.c:535-536, 1065-1067)
- touchstone identifies gems (apply.c:2658-2696)
- floating-eye paralysis fires on melee against the eye (uhitm.c:5853, 6022)
- Burdened status label (botl.c:12)
- food ration weight and nutrition (objects.h:1110)
- strategy aligned with NetHackWiki Curse-testing, Altar: altar amber/black flash and pet step-avoidance are confirmed canonical curse-testing techniques (https://nethackwiki.com/wiki/Curse-testing, https://nethackwiki.com/wiki/Altar)
-->

