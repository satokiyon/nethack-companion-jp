### 防具一覧表 (Armor Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h: no corrections. Every armor row (AC=10-macro-arg, MC, weight, material, slot) verified across ARMOR/HELM/CLOAK/SHIELD/GLOVES/BOOTS macros.
-->
<!-- audit
2026-05-19:
- body armor: AC/Wt/Cost via ARMOR() macros (objects.h:556-600); plate mail AC+7 wt450 cost600 (line 556-558).
- mithril coats: AC+6/+5, wt 150, cost 240, MITHRIL material (objects.h:571-576).
- shirts wt 5 (Hawaiian/T-shirt, objects.h:603-608); cloaks at objects.h:611-650.
- helmets at objects.h:445-487; gloves at objects.h:686-697; boots at objects.h:700-727.
- shields at objects.h:653-679; cloak of protection MC 3 (objects.h:637-640).
- helm of brilliance: adds spe to Int and Wis (literal enchantment), NO dice (do_wear.c:3328-3334 adj_abon).
- gauntlets of dexterity: adds spe to Dex, NO dice (do_wear.c adj_abon).
- dunce cap is NOT pre-cursed at generation: follows standard mkobj; auto-curses when worn (do_wear.c:475-491).
- 9/10-cursed-on-generation items: FUMBLE_BOOTS, LEVITATION_BOOTS, HELM_OF_OPPOSITE_ALIGNMENT, GAUNTLETS_OF_FUMBLING (mkobj.c:1086-1090).
- mithril DOES suffer casting penalty: MITHRIL is in is_metallic range, spelarmr applies (objclass.h:194-196, spell.c:2191-2193).
- blue dragon scale mail and scales give extrinsic Very_fast tier matching speed boots, NOT intrinsic Fast (do_wear.c:817-828 EFast).
- speed boots mechanic: free action on 2/3 of turns, NOT "+1 speed". (allmain.c:125-128 `if (Very_fast) { if (rn2(3) != 0) moveamt += NORMAL_SPEED; }`)
- levitation boots: Boots_off handles in-air removal (do_wear.c:300-310); the trap is the 9/10 curse.
- robe casting bonus cancels most of the metal-armor penalty (spell.c:2192-2195 spelarmr subtraction).
- chain mail: all iron mails are Mines drops (the "Dwarves drop these" framing is misleading).
- follow-ups: build_armor_appendix.py may be stale; "yellow dragon scale mail | Rare." not verified against 5.0 generation rules.
-->

**AC**はその防具が提供するアーマークラス補正値です（数値が大きいほど防御力が高く、画面上のAC表示からこの数値が減算されます）。**MC**は魔法防御能力レベル（1〜3）を表し、数値が高いほど敵の魔法攻撃を防ぐ確率が高まります。**重量 (Wt)**はユニット重量、**価格 (Cost)**は店での基本価格です。**備考**列には、装備中に付与される固有能力（耐性や特性）および戦術上の注意点をまとめています。防具は装備部位ごとに分類されています。ドラゴンの鱗鎧は終盤における圧倒的重要性から、個別の項目として取り上げています。一部の防具にある括弧内の名称は、侍（Samurai）プレイ時に表示される別名です（ゲーム内部では同一アイテム）。
