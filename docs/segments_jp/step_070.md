### あなたを殺す脅威 (Things That Will Kill You)

<!-- audit
2026-08-13:
- growl wake radius: growl() calls wake_nearto(x,y, mtmp->data->mlevel * 18) (sounds.c:421), and wake_nearto uses dist2 < distance (mon.c:4388), so mlevel*18 is a SQUARED radius. base gnome is m_lev 1 (monsters.h:1682) => sqrt(18) ≈ 4 squares, NOT 7. "seven squares for a level-3 gnome" was wrong (a gnome is level 1; a gnome LORD is level 3). fixed prose to "about four squares for a gnome, farther for larger creatures" (dwarf m_lev 2 => ~6, gnome lord m_lev 3 => ~7).
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Sleep resistance is from elf corpses only; an elven mummy drops an already-old elf corpse, so eating it risks food poisoning (mon.c:620-646; eat.c:908). Giants convey Str/elemental res.
- Floating-eye paralysis is d(3,70) ≈ 3-210, avg ~106 (uhitm.c:5887, 6042); "70" was the die size.
- Dragon breath vs items: yellow=acid, blue=lightning (monsters.h); shock destroys rings/wands, fire+cold destroy potions (zap.c). Rewrote to fire/frost.
-->
<!-- audit
2026-05-20:
- mines residents are class G (gnomes, S_GNOME) and h (humanoids incl. dwarves, S_HUMANOID); g is gremlins/gargoyles (defsym.h:295, 301, 303, 333)
- gnomish wizard has AT_MAGC AD_SPEL (monsters.h:1695-1698); its ONLY attack is spellcasting. CORRECTION (2026-08-13): the earlier "can cast sleep" was wrong. it casts from mon_wizard_spells (mcastu.c:32-36) which contains NO sleep spell, and at m_lev 3 spellval=rn2(3)∈{0,1,2} (mcastu.c:111) can only reach PSI_BOLT(0)/CURE_SELF(1)/HASTE_SELF(2). so it psi-bolts you (damage) and self-buffs; it CANNOT sleep, stun, or confuse you. STUN_YOU is level 3 (unreachable at rn2(3)). fixed the prose in Common Combat Deaths (2 spots) and the sleep-source list (replaced "gnomish wizard's sleep spell" with sleeping-gas trap).
- homunculus AT_BITE AD_SLEE 1d3 (monsters.h:551-558)
- soldier ant speed 18, AT_BITE 2d4 + AT_STNG AD_DRST 3d4 (monsters.h:103-110)
- water demon: S_DEMON class &, level 8, NOCORPSE NOGEN (monsters.h:2911-2919)
- rope golem AT_HUGS 6d1 grapple (monsters.h:2523-2529)
- iron golem level 18, speed 6, AT_WEAP 4d10 + AT_BREA AD_DRST 4d6 (poison gas, drains Strength), MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON (monsters.h:2586-2594); slow but heavy hitter, not a speedster
- bats and giant bats speed 22; raven and vampire bat speed 20 with two attacks each (monsters.h:1269-1294)
- steam/fire vortices speed 22; queen bee speed 24 (rare); air elemental speed 36 (monsters.h vortices, queen bee, air elemental rows)
- water demon wish: rnd(100) > (80 + level_difficulty()) — 20% chance at depth 0, drops to 0% past level_difficulty 20 (fountain.c:78)
- clay golem AT_CLAW AD_PHYS 3d10 single (monsters.h:2562-2569)
- stone golem AT_CLAW AD_PHYS 3d8 single (monsters.h:2570-2577)
- golems are class ' (apostrophe), not P (defsym.h:359)
2026-05-19:
- Very_fast = (HFast & ~INTRINSIC) || EFast (youprop.h:377)
- Blue DSM sets EFast |= W_ARM (do_wear.c:822); speed boots set EFast |= W_ARMF
- either alone reaches Very Fast; wearing both doesn't go faster
2026-05-18:
- mount slip damage 10-14 HP via rn1(5, 10) (steed.c:354)
- water demon spawn rate is 1 in 30 quaffs at fountain.c:247, 314
- bones items 80% cursed via rn2(5) gate (bones.c:290)
- all 9 DSM extrinsic properties verified at do_wear.c:806-883
- gold DSM permanent light radius 4/3/2 blessed/uncursed/cursed (light.c:881-911)
- gold DSM is the only body-slot light source (artifact.c:2264-2275)
- confused genocide hits your role: u.umonster ← gu.urole.mnum (read.c:2839, u_init.c:991)
- mumakil attack solo, not in packs; AT_BUTT 4d12 + AT_BITE 2d6 (monsters.h:838-845)
- shimmering DSM does not exist in 5.0 (#if 0 DEFERRED in objects.h:509-511, 536-538)
- strategy aligned with NetHackWiki Bones, Yet Another Stupid Death, Sleep, Golem: bones loot 80% cursed and dangerous, early-game pacing matters more than depth, sleep resistance recommended before Mines, iron golem and rope golem are the dangerous golems for the player (https://nethackwiki.com/wiki/Bones, https://nethackwiki.com/wiki/Yet_Another_Stupid_Death, https://nethackwiki.com/wiki/Sleep, https://nethackwiki.com/wiki/Golem)
-->

ダンジョン探索全体のうち、**昇天（ゲームクリア）に到達できるのはわずか約0.4%に過ぎません。**

**序盤のダンジョンこそが最も危険である。** 最も多くの冒険者を葬り去ってきたモンスターたちは、すべてダンジョン上層部に生息しています：ジャッカル、ドワーフ、兵隊蟻、ノームの領主、ドブネズミ、巨大コウモリ、[小さなミミック](#a-note-on-mimics)、ノーム、狐、水ヘビです。万全に準備の整った冒険者にとって、彼らの誰一人として本質的に危険な敵ではありません。彼らがあなたを殺せるのは、あなたのHP、AC、そして耐性がまだ整っておらず、しかも数で圧倒してくるからです。序盤の手番は、無理に深く潜ろうと急ぐのではなく、フロアを丁寧に掃討し、祭壇を見つけ出し、手に入れた武具のBUC（呪いの状態）を把握することに費やしましょう。

**探索ペースについて。** 戦闘の後は必ず足を止めて休息し、HP満タン（少なくとも90%以上）の状態で階段を降りてください。現在の階層と経験レベルを無理に一致させようとするよりも、最大HPの高さの方がはるかに生存率を正確に予測します。利用価値のあるものは探索すべきですが、下り階段が見つかった後は、空っぽの部屋を無意味にうろついたり実りのない捜索に貴重な食料を浪費してはいけません。遠距離攻撃の手段と、瞬間移動の巻物や瞬間移動の杖などの安全な離脱手段を必ず確保した上で次の階層へ降りましょう。階段を降りた直後の突然死の多くは、手負いの状態で逃走手段も持たずに新しいフロアへと踏み込んだことから始まっています。

