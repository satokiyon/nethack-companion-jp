### 前回からの変更点 (What Changed Since Last Time)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- No "minimum sacrifice value" gate; value only caps artifact quality (pray.c:1784, artifact.c:195). Reworded.
- Sunsword #invoke costs 25 Pw (SPELL_LEV_PW(5)), not 5 (artifact.c:2095).
- "DSM gives two resistances" overstates: only black/green/yellow give two resistances; others give one + a perk (do_wear.c:806-883). Reworded.
- Crystal ball is a TOOL (objects.h:938); is_crackable needs ARMOR_CLASS (objclass.h:201), so it still shatters. Only crystal plate mail cracks.
- Gold DSM light radius is 3 (uncursed), not 2 (light.c:899-907).
- Verified correct: spell-level changes, touch-of-death rework, HP-regen formula, two-handed 3/2, Excalibur 1/30-vs-1/6, priest-donation randomization, unicorn-horn no-restore, BoH scatter, candle sqrt light, new monsters/conducts/shop mechanics.
-->
<!-- audit
2026-05-19:
- chain lightning is level 2 NODIR (objects.h:1409-1411 SPELL("chain lightning",..., P_ATTACK_SPELL, prob 25, delay 4, level 2, mgc 1, NODIR))
- "mummy withering" was fabricated; no such mechanic in 5.0
- Elbereth -5 alignment penalty is NOT a 5.0 change (engrave.c writeable_engrave, predates 5.0)
- supply chests appear strictly above the Oracle (mklev.c:1037 `u.uz.dlevel < oracle_level.dlevel`), not "the first ten levels"
- mind flayer: spell loss (uhitm.c:3266 losespells) and skill drain (uhitm.c:3270 drain_weapon_skill) persist; map/ID amnesia is gone (no forget_map call in eat_brains, eat.c:603)
- sink dipping is for potions only: non-potions just take water_damage (fountain.c:716-733)
- touch of death still has a binary success gate: without Antimagic, rn2(m_lev) > 12 applies the effect; Antimagic produces "Lucky for you, it didn't work!" (mcastu.c:391-407)
- the 5.0 change is the unprotected result: 50+8d6 damage plus half that amount drained from max HP instead of the old instadeath (mcastu.c:315-347; fixes5-0-0.txt:538)
- iron bars were added in 3.3.0, not 3.6 (fixes3-3-0.txt:349)
- gold dragon scale mail grants only hallucination resistance + innate light, not two resistances (do_wear.c:846-851, objects.h:505 DRGN_ARMR slot 0)
- bag-of-holding explosion scatters contents via scatter() rather than destroying them all; only 1/13 items vanish per is_boh_item_gone (pickup.c:2509-2532)
- death drops delobj() any rolled FOOD_CLASS item unless the monster has M2_COLLECT — corpses are still left (mon.c:3597-3604)
-->

NetHack 5.0.0 は 2026 年 5 月 2 日にリリースされました。旧バージョン（3.6.x 以前）の経験者の方は、まず以下の最初のグループから確認してください。これらは古い習慣や反射的行動がそのまま命取りとなる変更点です。
