#### 二刀流戦闘 (Two-Weapon Combat)
<!-- audit
2026-05-19:
- Rogue and Samurai are the only roles reaching Expert in P_TWO_WEAPON_COMBAT (u_init.c skill tables).
- Valkyrie and Knight cap at Skilled (u_init.c skill tables).
- Barbarian caps at Basic (u_init.c skill tables).
- Ranger has no P_TWO_WEAPON_COMBAT entry, so two-weapon is untrainable (unskilled, -9 to-hit), NOT forbidden — can_twoweapon has no role check (wield.c:766).
- Penalty structure is a flat negative replacement per skill tier: to-hit -9/-7/-5/-3, damage -3/-1/0/+1.
- Penalties are not a "split" between the two weapons. (weapon.c:1576-1600 hit-bonus and 1676-1695 dam-bonus apply the same flat penalty per-strike — no halving)
-->

一部の役職は左右の両手に1本ずつ武器を持って戦うことができます。見た目にも華やかであり、1ターンに2回の攻撃を繰り出すことができます。それぞれの攻撃にはスキルランクに応じた一律の命中率およびダメージのペナルティが課されます（未熟＝命中−9／ダメ−3、入門＝−7／−1、熟練＝−5／0、達人＝−3／+1）。また、両手とも近接武器でなければなりません。盾、射撃武器、投擲武器との併用は不可能です。二刀流スキルで「達人 (Expert)」まで到達できるのは **盗賊 (Rogue)** と **侍 (Samurai)** のみです。ワルキューレと騎士は「熟練 (Skilled)」、野蛮人は「入門 (Basic)」が上限となります。レンジャー、治療師、武闘家、魔法使いはこの戦闘スタイルを習得できません。

**2撃目が利益を生む状況。** 2回目の追加攻撃がペナルティを補って余りある価値を発揮するのは、すでに基礎命中率が十分に高く、1撃あたりのダメージが十分に出ている場合に限られます。「達人」（−3/+1）のランクで十分に強化された武器を持ち、標準的なACの敵と対峙する場合、侍の「刀＋脇差」の二刀流は刀単体をほぼ毎ターン上回る総ダメージを叩き出します。「熟練」（−5/0）の段階では、計算上ほぼ五分五分（トントン）です。「熟練」未満ではペナルティが恩恵を食い潰してしまうため、騎士や野蛮人は1本の良質な武器に専念した方がはるかに有利です。二刀流スキルのない役職にとって、両手持ち武器による筋力ダメージ1.5倍ボーナスは極めて強力な対抗選択肢となります。

**二刀流のセットアップ手順。** 逆手（オフハンド）専用の装備コマンドは存在しません。スワップコマンドを使って「副装備スロット」に武器をセットすることで実現します。まず逆手に持ちたい武器を `w` で手に持ち、`x` キーを押してそれを副装備スロットへと退避させます。次にメインの主武器を `w` で手に持ち、最後に `X`（大文字、二刀流切り替えトグル）を押して二刀流戦闘を開始します。もう一度 `X` を押せば片手持ちに戻ります。逆手の武器は必ず片手持ち近接武器でなければなりません。逆手の武器が呪われている状態で二刀流を開始しようとすると、手から滑り落ちて床に落下します。
