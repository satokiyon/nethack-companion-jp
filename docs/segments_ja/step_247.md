#### 文盲 (Illiterate)

<!-- audit
2026-05-19:
- only an "x" or "X" signature engrave is exempt; everything else breaks the conduct (engrave.c:1213)
- breaks: scrolls, spellbooks, fortune cookies, T-shirts, magic-marker writing (read.c:602, eat.c:2525, read.c:397, write.c:245)
- do NOT break: blank paper, unread novels, Book of the Dead, Hawaiian shirts, reading floor engravings (Elbereth)
- pet-on-scroll workaround for identifying scrolls is safe
- Wizard/Priest/Healer/Monk/Knight keep one pre-learned spell until it fades, ~20K turns (spell.h:17 KEEN)
- strategy aligned with NetHackWiki Illiterate: only an "x"-signature engrave is safe, scroll of scare monster is the rare exception that doesn't break the conduct (https://nethackwiki.com/wiki/Illiterate)
-->

いかなる文字も読んではいけません。巻物、魔法書、フォーチュンクッキー、Ｔシャツの文字を読むことは禁じられます。また、床に文字を刻む際も、伝統的な文盲の署名である単一の「x」または「X」以外の文字を刻むことは許されません（エルベレスを手動で刻むことはできません）。ただし、白紙の巻物や魔法書、アロハシャツ、死者の書、あるいは床に元から刻まれているメッセージを読む行為はセーフです。

巻物が読めないため、識別、武器・防具の強化、瞬間移動、解呪、虐殺といった強力な手段のほとんどが絶たれます。魔法書が読めないため、新しい呪文を学ぶことも古い呪文を再学習することもできず、初期習得呪文はやがて忘れ去られます。これにより、杖、薬、そして創意工夫に満ちた回避策への依存度が極限まで高まります。代表的な回避策は、**ペットの足踏みによるBUC判定**（犬がその上を歩くか？）と、**店主への売却価格による識別（価格識別）**（店主の提示価格を見ることは「読書」には含まれない）であり、これらを組み合わせることで識別の巻物の大半の役割を代行できます。

