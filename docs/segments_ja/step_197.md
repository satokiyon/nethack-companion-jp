#### 願いの構文 (Wish Syntax)

<!-- audit
2026-05-18:
- bare "gray dragon scale mail" keeps random spe and rolls BUC via blessorcurse(otmp,10): ~5% blessed / ~5% cursed / ~90% uncursed (objnam.c:5094-5096, 5258-5268)
- wished enchantment on armor/weapon/weptool/charged ring collapses to +0 if requested spe > rnd(5) (and > the item's random base spe): +1 always, +2 4/5, +3 3/5, +4 2/5, +5 1/5, +6+ never (objnam.c:5099-5105). Recommend +2. Roll is plain rnd(5), NOT luck-adjusted, so positive Luck gives no bonus.
- Luck < 0 sabotages wishes: "blessed" -> cursed (objnam.c:5263-5264), erodeproof/"fixed" fails to apply (objnam.c:5287), and spe > 2 flips negative (objnam.c:5104). Luck >= 0 is all that's needed; extra Luck does nothing. Wiki: +3 higher average, +2 less chancy and strictly better if enchanting further (https://nethackwiki.com/wiki/Wish).
- artifact wishes are probabilistic: oartifact && rn2(nartifact_exist())>1 (objnam.c:5374), scaled by TOTAL existing artifacts including bones
- u.uconduct.wisharti increments whether the wish is granted or denied (objnam.c:5364)
- only quest artifacts are absolutely blocked: restrict_name SPFX_NOGEN|SPFX_RESTR check (artifact.c:618)
- silent substitutes: Amulet of Yendor, Bell of Opening, Book of the Dead, Candelabrum, magic lamp → oil lamp (objnam.c:5003-5006)
- all gloves give +1 AC (objects.h:686-697); gauntlets of power give STR 25, not bonus AC (attrib.c:1214)
- Vlad's throne wish rate is 4/13 per effective sit (sit.c:241-256)
- magic lamp ≈27% wish-blessed: 1/3 djinni × 4/5 wish (apply.c:1817, potion.c:2833-2845)
- fountain water-demon wish (fountain.c:78, 314); Amulet-of-Yendor pickup wish (allmain.c:446-451)
- strategy aligned with NetHackWiki Wish, Gray dragon scale mail, Speed boots, Magic lamp: GDSM/SDSM as top wishes, speed boots and gauntlets of power as standard follow-ups, bare wishes risk cursed/random spe (https://nethackwiki.com/wiki/Wish, https://nethackwiki.com/wiki/Gray_dragon_scale_mail, https://nethackwiki.com/wiki/Speed_boots, https://nethackwiki.com/wiki/Magic_lamp)
-->

プロンプトが「何をお望みですか？」（"For what do you wish?"）と尋ねてきたら、具体的に指定してください。それぞれの修飾語が何をもたらすかを解説します：

- `blessed greased fixed +2 gray dragon scale mail`（祝福された 脂を塗った 防蝕の +2 灰色ドラゴンの鱗鎧）が標準的な完成形です。指定しないとBUCがランダムになるため `blessed`（祝福）を指定し、`greased`（脂塗り）は抱きつき、巻きつき、粘着攻撃、マインドフレアの触手を受け流すために付与し、`fixed`（または `rustproof` / `erodeproof`）で損耗を防ぐ防蝕加工を施し、`+2` で強化値を指定します。必要以上に高い強化値を欲張ってはいけません：防具や武器のプラス値を指定すると、裏で 1〜5 のダイスが振られ、指定した値がそのロール値を上回ると強化値は無慈悲にも **+0 にリセット（崩壊）** します。したがって +1 は 100% 成功、+2 は 5分の4（80%）で成功、+3 は 5分の3（60%）で成功、+6 以上は絶対に通りません。+3 の方が通ったときの期待値はわずかに高いですが、それでも **+2** を指定することを強く推奨します。結果がより安定し、後から強化の巻物で仕上げを行えば、+3 で願った場合と遜色ない値に安全に到達できます。
- 願う前に自身の幸運（Luck）を確認してください。幸運が 0 以上（マイナスでない）でありさえすれば十分であり、過剰に善運を溜め込んでも願いの判定にボーナスはありません。しかし、**負の幸運（マイナス）** は願い全体を毒牙にかけます：`blessed` を願っても呪われて生成され、`fixed` の防蝕加工は剥がれ、+2 を超えるプラス値はマイナスへと反転します。幸運が悪化している場合は、装備を願う前にまず幸運を回復させてください。
- 単に `gray dragon scale mail` とだけ願うと、BUCも強化値もダイス任せになり、最悪の場合呪われて出現します。せっかくの貴重な願いです。必ずBUCと強化値を明記してください。また、`scale` の単語を絶対に忘れないでください。`gray dragon mail` とだけ入力すると、代わりに「灰色の郵便の巻物」（scroll of mail）を渡されてしまいます。
- アーティファクトの願いは、世界に存在するアーティファクトの総数が増えるほど **成功率が低下** します。拒絶判定はダンジョン内に存在する総数（所持品、床落ち、ボーンズファイル内のものを含む）に応じて厳しくなり、出現しなかった場合でも「アーティファクト願いカウンター」は加算されます。なお、他職のクエストアーティファクトは絶対に生成されません（完全拒絶）。
- 一部の禁止アイテムを願うと、黙って無価値な日用品へとすり替えられます。**イェンダーの魔除け** は偽物の魔除けに、**開扉のベル** はただの鈴に、**死者の書** は白紙の本に、**祈りの燭台** は獣脂のろうそくになります。また **魔法のランプ** を願っても失敗し、単なる油つぼ（普通のランプ）を手渡されます。あんなに一生懸命ランプを擦ってきた後では、あまりにも残酷な仕打ちです。

