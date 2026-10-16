### 遠征の選択 {#choosing-your-expedition}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Rogue backstab is melee-only; removed "counts even at range" (uhitm.c:960 gates on hmd->hand_to_hand: "multi-shot throwing is too powerful here").
- Healer has no Sick_resistance (hea_abil = poison-res@1, warning@15; attrib.c:41-43); tainted food still sickens (eat.c:1904,1939). Narrowed "cannot be made sick" to the potion of sickness, which is Healer-cased (potion.c:969,977).
- Verified correct: all 13 roles' intrinsic-gain XLs (attrib.c:26-89), alignment/race availability (role.c), race stat caps (role.c:597-678), starting kits (u_init.c:42-178), Archeologist scroll-decipher on pickup (invent.c:1036), Barbarian HP-advance 10 (role.c:102), Excalibur gates (fountain.c:404-410).
-->
<!-- audit
2026-05-21:
- Archeologist starts with touchstone (u_init.c:50) and knows_object(TOUCHSTONE) so the tool itself is identified (u_init.c:660-662); does NOT have knows_class(GEM_CLASS) — gems are NOT pre-identified; touchstone identifies gems by rubbing per apply.c:2678-2707 (Ken Arnold)
- Healer starts with wand of sleep, 4 potions of healing, 4 potions of extra healing, and 3 blessed spellbooks (healing, extra healing, stone-to-flesh) (u_init.c:81-90); the spellbooks are always blessed so reading them always succeeds
- Tourist starts with 4 scrolls of magic mapping, 2 potions of extra healing, 21-40 +2 darts, Hawaiian shirt, expensive camera, credit card, and 10 random food items (u_init.c:150-159)
2026-05-18:
- Knight starts with +1 long sword and +1 lance (u_init.c:91-92)
- Cave Dweller gains Fast at XL 7 (attrib.c:37)
- Knight gains Fast at XL 7 (attrib.c:45)
- Healer starts with poison resistance at XL 1 (attrib.c:41)
- Ranger gains Searching XL 1, Stealth XL 7, See Invisible XL 15 (attrib.c:63-66)
- Elf gains sleep resistance at XL 4 (attrib.c:95)
- Cave Dweller starts with sling + flint stones (u_init.c:68-71)
- Ranger starts with +2 cloak of displacement (u_init.c:128)
- Wizard starts with cloak of MR + wand + rings + potions + scrolls + books + marker (u_init.c:167-176)
- Knight has intrinsic jumping from XL 1 (u_init.c:691)
- amethyst converts booze (not sickness) to fruit juice (potion.c:2161-2163)
- unicorn horn converts sickness to fruit juice (potion.c:2151-2154)
- Mjollnir is the Valkyrie sacrifice gift; needs a co-aligned altar (artilist.h:109)
- Knight code penalizes attacks on fleeing or helpless monsters (uhitm.c:336-339); peaceful kill is Samurai's giri
- all 13 role alignment/race availabilities (role.c)
- race stat caps (Str/Int/Wis/Dex/Con/Cha): Human {STR18(100),18,18,18,18,18} (role.c:597-598); Elf {18,20,20,18,16,18} (role.c:617-618); Dwarf {STR18(100),16,16,20,20,16} (role.c:637-638); Gnome {STR18(50),19,18,18,18,18} (role.c:657-658); Orc {STR18(50),16,16,18,18,16} (role.c:677-678)
- race stat FLOORS are uniformly {3,3,3,3,3,3} for every race (role.c:597, 617, 637, 657, 677)
- race intrinsic tables (attrib.c:91-105): hum_abil=none; dwa_abil=Infravision@XL1; elf_abil=Infravision@XL1+Sleep_resistance@XL4; gno_abil=Infravision@XL1; orc_abil=Infravision+Poison_resistance both@XL1
- initial roll distributes 75 points starting from role attrbase, clipped by race ATTRMAX, floor ATTRMIN=3 (attrib.c:723-737, init_attr_role_redist at 699-718); initial values typically land well below the race cap
- strategy aligned with NetHackWiki Valkyrie, Excalibur: Valkyrie is widely cited as the easiest beginner role; Knight 1-in-6 Excalibur dip at XL 5+ confirmed (https://nethackwiki.com/wiki/Valkyrie, https://nethackwiki.com/wiki/Excalibur)
-->

迷宮へ足を踏み入れる前に、まずは**役職 (role)**、**種族 (race)**、そして**属性 (alignment)** を選択します。この3つの組み合わせによって、初期装備、固有能力、信仰する神々、そして安全に扱えるアーティファクトが決まります。

初めての冒険なら、**「秩序」の「人間」または「ドワーフ」の「ワルキューレ」**を選ぶのがおすすめです。初期能力値と装備が強力で、最初から冷気耐性を持ち、序盤から強力な武器を入手する確実なルートが存在します。もちろん、他に興味を惹かれる役職があれば、迷わずそちらを選んでください。最初の数回の死は、キャラクター選択画面の解説文の何倍もの教訓を与えてくれるはずです。
