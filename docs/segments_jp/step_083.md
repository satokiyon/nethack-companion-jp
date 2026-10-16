### 即死の危険 (Ways to Die Instantly) {#ways-to-die-instantly}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Food poisoning is from eating old/rotten corpses; giant ants are AD_PHYS only (monsters.h). Disease attacks (AD_DISE) belong to Juiblex/Demogorgon/Scorpius. Removed the giant-ant example.
- Verified correct: poison 6+d(4,6) extra HP & fatal-at-30, Famine drain rn1(40,40), touch_of_death 8d6+50, stoning/slime timers, disintegration armor order, reverse-genocide 4-6.
-->

迷宮には、現在の残りHPがどれほどあろうとも、たった1手でキャラクターを死に至らしめる要素がいくつか存在します。プレイヤーたちはこれらを「即死（instadeaths）」と呼びます。しかし、何に注意すべきかさえ知っていれば、ほぼすべての即死要因には1〜2ターン前の事前警告が存在します。

> *以下に掲載する即死カタログは、Dylan O'Donnell氏のRGRNファイルをもとにまとめたTrevor Powell氏の『即死スポイラー (Instadeath Spoiler)』に着想を得ています。Trevor氏は即死を「プレイヤーのヒットポイントが0まで削られる過程を伴わずに発生する、たった1手での死亡」と定義し、その分類体系は今日までスタンダードなリファレンスとして使われ続けています。*
