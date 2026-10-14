#### 虐殺なし (No Genocide)

<!-- audit
2026-05-19:
- genocide is only prompted by scroll of genocide and by sitting on a regular throne; wishes never offer it (do_genocide callers: read.c:1735-1737 SCR_GENOCIDE and sit.c:131 throne only)
- uncursed scroll: single species; blessed scroll: whole class (do_class_genocide, read.c:2638)
- throne prompt is single-species only: case 8 of 13 in throne_sit_effect, calls do_genocide(5) (sit.c:125-132)
- Vlad's tower thrones take a different path with no genocide case (special_throne_effect, sit.c:63-66)
- on a cursed scroll, empty input re-prompts and rndmonst() creates monsters; type "none" to escape (read.c:2848-2871)
- end-of-game tracking counts G_GENOD species in mvitals[], not a u_conduct counter (insight.c:2951-2966 num_genocides)
- cursed-scroll monster-creation preserves the conduct (no species gets G_GENOD'd)
- strategy aligned with NetHackWiki Genocide, Throne: answer "none" at the prompt, throne genocides are always safe, Plane of Water class-`;` wipe is off-limits for genocideless (https://nethackwiki.com/wiki/Genocide, https://nethackwiki.com/wiki/Throne)
-->

いかなるモンスターも虐殺（ジェノサイド）してはいけません。虐殺のプロンプトが表示されるのは、**虐殺の巻物** を読んだとき（無呪は1種族、祝福はクラス全体）と、**通常の玉座に座ったとき**（13通りの結果のうちケース8で単一种族の虐殺を促される）の2つです。コンダクトを維持するには、対象を聞かれた際に **"none"** と入力してください（Enterキーだけを押すと再入力を求められるだけです）。呪われた巻物は入力した名前に応じたモンスターを逆虐殺（召喚）しますが、召喚自体は虐殺なしコンダクトを破棄しません。

これは、マスターリッチやアーチリッチ、マインドフレア、コカトリスといった、熟練冒険者が普段なら即座に根絶する凶悪なモンスターのすべてと正面から向き合い続けることを意味します。また、**水の面** においても、クラゲやウナギやクラーケン（`;` クラス）を一網打尽にする定石が使えないため、呼吸の魔除けを用意して海の怪物たちの間合いを警戒しながら正攻法で渡り切らなければなりません。

もっとも、これは比較的達成しやすいコンダクトの1つです。巻物を拾えず、玉座で虐殺を引かなかったために、意図せず自然にこのコンダクトを達成して昇天するプレイヤーも数多くいます。

