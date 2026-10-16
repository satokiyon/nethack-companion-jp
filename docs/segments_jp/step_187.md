---

### スキルの向上 (Enhancing Skills) {#enhancing-skills}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Valkyrie two-weapon caps at Skilled, not Expert (Skill_V, u_init.c:544); the example's slot count corrected to eleven.
- Verified correct: practice thresholds level^2*20, slot costs, all to-hit/damage bonus tables, start-2/+1-per-level/+1-crowning, all 494 role skill-cap cells, training gates.
-->
<!-- audit
2026-05-18:
- skill ranks P_UNSKILLED through P_GRAND_MASTER; practice formula level²×20 (skills.h:92-106)
- cumulative practice thresholds: 20/80/180/320/500
- weapon slot costs 1/2/3 per rank; non-weapon costs 1/1/2/2/3
- two-weapon uses the WEAPON slot column (weapon.c:1141)
- bare-hand and martial-arts bonuses apply every hit (weapon.c:1611-1613)
- bare-hand 50% / martial-arts 75% rate is the practice-training check, not bonus gating (uhitm.c:847 `dmg = rnd(!martial_bonus() ? 2 : 4)`; uhitm.c:849 `train_weapon_skill = (dmg > 1)` — rnd(2)>1 is 1/2, rnd(4)>1 is 3/4)
- riding trains after 100 mounted squares (steed.c:393-396, u.urideturns >= 100)
- Knights start at Basic riding; target is Skilled (weapon.c:1787-1789)
- pickup/loot/dip/trap/engrave actions gated at Basic riding
- slot ceiling 32 for an XL-30 crowned hero: 2 starting + 29 level-ups + 1 crowning (u_init.c:884, pray.c:992-993)
- Ranger divination caps at Expert (u_init.c:461)
- Wizard restricted from long sword: no P_LONG_SWORD entry in Skill_W (u_init.c:548-569)
- spell schools start with a 20-use precredit at Basic
- Skilled cone-of-cold and fireball: cluster of 3×3 explosions (spell.c:1419-1452), not room-clearing
- Valkyrie 6+6+2 = 14 slot example math
- crown gives +1 slot
- strategy aligned with NetHackWiki Skill, Twoweapon: slot budget tied to XL + crowning, non-weapon skills cost half, restricted skills only unrestrict to Basic via artifact gift (https://nethackwiki.com/wiki/Skill, https://nethackwiki.com/wiki/Twoweapon)
2026-05-23:
- Wizard dagger Expert opening: Wizards are unrestricted in dagger (Skill_W u_init.c:548-569), cap at Expert; thrown daggers benefit from a class multishot bonus (dothrow.c:177-190); early Pw budget is tight at base regen (Wis+Int)/15+1 (allmain.c:605-607)
- six-slot Dagger Expert cost = 1+2+3 (weapon column, skills.h:92-106)
- citation: community Wizard opening guides on NetHackWiki Wizard strategy and Damerell, "How to play a Wizard" (https://nethackwiki.com/wiki/Wizard, https://www.steelypips.org/nethack/)
-->

多くの冒険者は、初めて **`#enhance`** コマンドを入力し、これまで何レベルにもわたって振り回してきた幅広の剣が、ついに「入門」から「熟練」へと昇格できる状態になっていることに気づいた瞬間に、このスキルシステムの存在を知ります。武器、戦闘スタイル、そして魔法系統はそれぞれ個別に熟練度を記録しており、貴重なスキルスロットを1枠ずつ消費して向上させていきます。

序盤のうちに1つの武器系統を定め、それに専念してください。スキルは武器の持ち替えをやめて初めて累積していきます。自分が「熟練（Skilled）」（命中率 +2）に達した武器は、「未習熟（Unskilled）」（命中率 −4 のペナルティ）のまま振るう基本攻撃力の高い武器よりもはるかに敵を圧倒します。したがって、訓練していないピカピカの新しい剣に乗り換えることは、通常は戦力ダウンにしかなりません。見つかった強そうな武器に次々と目移りしていては、あらゆる武器で未習熟のまま取り残されてしまいます。
