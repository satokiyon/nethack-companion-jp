### 固有能力および外在能力一覧表 (Intrinsic and Extrinsic Tables) {#intrinsic-and-extrinsic-tables}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Sleep res: dropped "dark one" (G_NOCORPSE). Shock res: dropped "shocking sphere" (G_NOCORPSE). Teleport: dropped "homunculus" (no M1_TPORT). All leave no corpse / don't convey.
- Magic resistance: no role grants it intrinsically; removed "Wizard XL 17" (that's teleport control, attrib.c:86-88).
- Teleport control: carrying the Amulet of Yendor BLOCKS controlled teleport (teleport.c:1185), it doesn't grant it.
- Verified correct: all other role/race intrinsic gain levels, ring/amulet/dragon-scale grants.
-->
<!-- audit
2026-06-01:
- property list from include/prop.h:14-93 (68 enum entries; we cover the player-attainable subset and skip trouble states and INVULNERABLE)
- role intrinsic gain levels from src/attrib.c:23-105 (innate structs per role: arc/bar/cav/hea/kni/mon/pri/ran/rog/sam/tou/val/wiz)
- race intrinsic gain levels from src/attrib.c:91-103 (dwa_abil, elf_abil, gno_abil, orc_abil)
- corpse intrinsic conferral logic at src/eat.c:903-951 (intrinsic_possible() — mconveys & MR_X check per resistance)
- give-rate formula at src/eat.c:961-997 (chance=15 standard; chance=4 for killer-bee/scorpion poison; chance=1 telepathy; chance=10 teleport; chance=12 teleport control; chance=6 stone temp; chance=3 acid temp; (ptr->mlevel > rn2(chance)) gates the grant)
- prayer-conferred intrinsics at src/pray.c:814,817,1321-1325 (HFire_resistance / HSleep_resistance / HFast / HStealth |= FROMOUTSIDE)
- dragon scale base property at include/objects.h:497-553 (DRGN_ARMR macros — each color's primary granted property; gold has no power, shimmering is DEFERRED)
- dragon scale special secondary effects at src/do_wear.c:798-884 (dragon_armor_handling switch: black=drain res, blue=fast, green=sick res, red=infravision, orange=free action, yellow=stone res, white=slow digestion, gold=affects hallucination state)
- ring grants at include/objects.h:741-827 (RING macro 3rd arg = granted property)
- amulet grants at include/objects.h:835-862 (AMULET macro 3rd arg = granted property)
- helm of caution grants WARNING (objects.h:479-481)
- helm of telepathy grants TELEPAT (objects.h:485-487)
- cornuthaum grants CLAIRVOYANT to Wizard role only (objects.h:457-461)
- alchemy smock grants POISON_RES (objects.h:630-632)
- elven boots grant STEALTH (objects.h:715-717); elven cloak grants STEALTH (objects.h:615-617)
- jumping boots grant JUMPING (objects.h:712-714)
- water walking boots grant WWALKING (objects.h:709-711)
- speed boots grant FAST (objects.h:707-709)
- levitation boots grant LEVITATION (objects.h:725-727)
- shield of reflection grants REFLECTING (objects.h:677-679)
- shield of drain resistance NEW in 5.0 (objects.h:656-658)
- shield of shock resistance NEW in 5.0 (objects.h:659-661)
- cloak of protection grants PROTECTION + MC3 (objects.h:637-641)
- cloak of magic resistance grants ANTIMAGIC + MC1 (objects.h:644-646)
- cloak of invisibility grants INVIS (objects.h:641-643)
- cloak of displacement grants DISPLACED (objects.h:648-650)
- amulet of guarding grants PROTECTION + MC2 (objects.h:855-856)
- amulet of magical breathing grants MAGICAL_BREATHING (objects.h:852-854)
- amulet of life saving grants LIFESAVED (objects.h:838-839)
- amulet of unchanging grants UNCHANGING (objects.h:848-849)
- amulet of reflection grants REFLECTING (objects.h:850-851)
- amulet of ESP grants TELEPAT (objects.h:835-836)
- amulet of flying grants FLYING (objects.h:859-860)
- amulet versus poison grants POISON_RES (objects.h:844-845)
- Sunsword: extrinsic BLND_RES when wielded (artilist.h:209-212; youprop.h:160 EBlnd_resist comment)
- Magicbane grants ANTIMAGIC + ESP + stun while wielded (artilist.h:145-147; src/artifact.c handlers)
- Grayswandir grants HALLUC_RES via SPFX_HALRES (artilist.h:170; src/artifact.c:787)
- Dragonbane grants REFLECTING via SPFX_REFLECT (artilist.h:157-160; artifact.c:867)
- Eye of the Aethiopica grants ENERGY_REGENERATION + ESP carried (artilist.h:303-307; artifact.c:841)
- Heart of Ahriman grants LEVITATION + STEALTH (artilist.h:225-230)
- Sceptre of Might grants PROTECTION + CONFLICT (artilist.h:232-235)
- Orb of Detection grants HALF_SPDAM + ESP + INVIS (artilist.h:219-223)
- Master Key of Thievery grants TELEPORT_CONTROL + WARN + HALF_SPDAM + HALF_PHDAM (artilist.h:279-283)
- Platinum Yendorian Express Card grants ESP + HALF_SPDAM (artilist.h:291-295)
- Orb of Fate grants WARN + HALF_SPDAM + HALF_PHDAM (artilist.h:297-301)
- Longbow of Diana grants ESP + REFLECTING (artilist.h:271-274)
- Mitre of Holiness grants PROTECTION (artilist.h:265-269)
- Tsurugi of Muramasa grants PROTECTION (artilist.h:285-289)
- Trollsbane grants REGENERATION (artilist.h:182-184)
- Staff of Aesculapius grants REGENERATION + drain res (artilist.h:248-253)
- Orcrist warns of orcs via SPFX_WARN + M2_ORC (artilist.h:134-136)
- Sting warns of orcs (artilist.h:138-140)
- Grimtooth warns of elves via SPFX_WARN + M2_ELF (artilist.h:123-126)
- ANTIMAGIC and HALLUC_RES are separate properties in prop.h (12 vs 24); magic resistance doesn't automatically block hallucination
- BLND_RES intrinsic comes only from polyform into AD_BLND attack monsters per src/polyself.c:108; no corpse-grant path
- HALLUC_RES intrinsic comes only from polyform into AD_HALU attack monsters per src/polyself.c:88; no corpse-grant path
- SEE_INVIS not conveyed by any corpse per src/eat.c:1356 (intrinsic_possible returns false)
- PASSES_WALLS, SWIMMING, DETECT_MONSTERS: polyform-only, no player-attainable persistent source
-->

NetHack はプレイヤーに対して 68 種類もの特性（プロパティ）を追跡・管理しています。そのうち冒険者が積極的に獲得を目指すべき有用な能力は、大きく 5 つの系統（ダメージ耐性、感覚と知覚、移動と空間挙動、戦闘と防御、特殊・実用機能）に分類されます。下記の表は各能力の効果、および信頼できるすべての獲得源を**内在能力（Intrinsic: 死体の摂食、レベル上昇、種族、祈りから獲得）**と**外在能力（Extrinsic: 装備、所持品から獲得）**に分けて網羅したものです。

表を見るにあたり、4つの重要な基本ルールを把握しておきましょう：

- **死体からの獲得確率は通常、モンスターのレベルに比例して高くなる。** さまよう目は確実にテレパシーを付与します。また、酸耐性や石化耐性は標準的な耐性判定よりも有利な確率が設定されています。これらの有用な例外は表中で個別に明記しています。
- **内在能力と外在能力は重複（スタック）しない。** 同一の耐性を両方から得ていても、効果が2倍になるわけではありません。しかし両方を揃えておくことは**冗長性（バックアップ）**として極めて有用です。例えばクロークを脱いでも、内在能力があれば守られ続けます。
- **修道士（Monk）は全職業中最も幅広い耐性獲得ラダーを持つ。** レベル 1 から 17 にかけて 11 種類もの内在能力を自力で習得します。
- **ドラゴンの鱗鎧はあらゆるアイテムの中で最も多くの重要能力を網羅する。** 各色ごとに1つの基本耐性を備え、さらに複数の色が強力な*二次的効果*（黒は分解＋吸命耐性、青は電撃＋高速移動など）を併せ持ちます。完全な対応関係は表を参照してください。
