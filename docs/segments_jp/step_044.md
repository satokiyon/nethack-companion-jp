#### メデューサの島 (Medusa's Island) {#medusas-island}
<!-- audit
2026-05-19:
- Perseus loot is per-layout — not uniform: shield 75% in medusa-1/3/4 but 25% in medusa-2 (medusa-2.lua:58-63)
- boots are 25% in medusa-1/3/4 but 75% in medusa-2 — swapped with the shield
2026-05-18:
- Medusa DL 20-29: base=-5 range=4 from DoD bottom 25-29 (dungeon.lua:75-81)
- four layouts (medusa-1.lua through medusa-4.lua); all use des.stair("down") — no ladder
- scimitar blessed +2 at 50% and sack at 50% are constant across all four layouts (medusa-1.lua:70, 73)
- shield is cursed in every layout (medusa-1.lua:64 and matching lines in others)
- gaze reflection stones Medusa via ureflects → killed(mtmp) (mhitu.c:1721-1745)
- stone resistance also blocks the gaze (mhitu.c:1747-1748) — rarely attainable pre-Medusa
- eel grab drown uses eel's tile, not yours: is_pool(magr->mx, magr->my) (uhitm.c:3389-3401)
- levitation/water-walking on adjacent dry land does NOT save you once grabbed
- medusa-2 has six electric eels (not giant eels), AD_ELEC bite (medusa-2.lua:99-104, monsters.h:3239-3247)
- kraken only on medusa-4 (medusa-4.lua:122)
- strategy aligned with NetHackWiki Medusa, Reflection, Perseus: reflection/blindfold against the gaze, levitation/water-walking to cross, Perseus statue as a backup reflection source (https://nethackwiki.com/wiki/Medusa, https://nethackwiki.com/wiki/Reflection, https://nethackwiki.com/wiki/Perseus)
-->

メデューサのフロアは運命の迷宮の最深部に近い地下25階前後に位置しています。広大な水域とあちこちに散乱する石像（かつて冒険者だった者たち）を見れば、そこがメデューサの島であることは一目瞭然です。

> *2000年代初頭、Arien Malec氏がPat Rankin氏、Geoduck氏、Topi Linkala氏らの助言を得て、RGRNの投稿者たちから渡河戦術を収集・整理しました。以下はそのガイドの要約版です。*

このフロアには1つの島に3つの試練が集約されています：島を取り囲む **水域の横断**、その水中に潜む **巨大ウナギ**（1つのマップ構成では電気ウナギ）、そして視線が合った者を石に変える **メデューサ自身** です。それぞれについて以下で個別に解説します。もし倉庫番から「反射の魔除け」を持ち帰っているなら、3つ目の問題はすでに解決しています。

島の中央には、[城 (The Castle)](#the-castle) へと続く下り階段が存在します。この階層には4種類のマップレイアウトが存在するため、1つの地図を暗記することに頼ってはいけません。

**ペルセウスの石像。** 島にある石像の1つには **ペルセウス (Perseus)** という名が刻まれています。鏡の盾を使ってメデューサを討ち取った神話の英雄です。「衝撃」の呪文、強打の杖、またはつるはしでこの石像を破壊すると、（呪われた）**反射の盾 (shield of reflection)**（4つのレイアウトのうち3つで75%、残りの1つで25%の確率）、祝福された+2の **シミター**（50%）、**浮遊の靴 (levitation boots)**（3つのレイアウトで25%、盾の確率が低いレイアウトでは75%）、そしてこれらを収納する **袋**（50%）が手に入ります。反射の盾は呪われているため、装備する前に解呪の手段を用意しておきましょう。なお、このフロアにある他の石像の中身はすべて空っぽです。

**メデューサの視線を生き延びる方法。** 彼女の階層に降りる前に、以下のいずれかの対策を必ず用意してください：

- **反射 (Reflection)**（魔除け、盾、または銀色ドラゴンの鱗鎧）。メデューサの視線が反射して跳ね返り、彼女自身を石化させます。これが最も安全かつ確実な解決策であり、大半のプレイヤーが採用する方法です。
- **目隠し、またはタオル。** 彼女の視界に入る前に装着します。盲目状態で移動・索敵するために [テレパシー](#senses-and-perception) や怪物を探す手段が必要になります。視線対策としては完璧に機能しますが、フロアの探索は格段に難しくなります。
- **鏡。** 目を覚ましているメデューサに対し、遮るもののない直線上の任意の位置から鏡を「適用（`a`）」します。どのマップ構成でも彼女は初期状態で眠っているため、まずは安全な距離から起こす必要があります。
- **一撃必殺。** 死の杖や「死の指」の呪文なら、相手に行動のターンを与えることなく即死させられます。なお、メデューサ自身は石化耐性を持つため、コカトリスの死体は効きません。
  どのような方法で倒したとしても、**彼女の死体を絶対に食べてはいけません**。彼女はゴルゴンであり、その死肉を口にした者は即座に全身が石化してゲームオーバーになります。

**水域の横断。** 島は深い水で囲まれています。安全な順から絶望的な順に並べた選択肢は以下の通りです：

- **浮遊 (Levitation)**（指輪、靴、薬、または呪文）。最も安全かつ容易な渡河手段です。ただし、隣接する水マスからウナギに引きずり込まれる危険は残ります（[即死の危険](#ways-to-die-instantly) の [溺死](#drowning) を参照）。
- **水上歩行の靴 (Water walking boots)**。水面の上を歩いて渡れます。こちらも隣接する水中にいるウナギの巻きつき攻撃は防げません。
- **冷気の杖 (Wand of cold)**。水面に向かって杖を振り、氷の道を凍らせて作ります。1マス進むごとに足を滑らせて2ターン行動不能になるリスクがあり、火炎によって氷が再び溶けてしまうこともありますが、渡り切ることは可能です。
- **大地の巻物 (Scroll of earth)**。頭上から落下した巨石が水没し、飛び石の橋が完成します。時間はかかりますが、他に手段がない場合には有効です。
- 飛行または遊泳能力を持つ生物への **変身（へんげ）**。[へんげ制御](#special-and-utility) の能力がない場合は極めて危険です。
- **飛び跳ねる靴 (Jumping boots)、または騎士の跳躍能力**。幅の狭い水路を跳び越えることができますが、慎重な位置取りが求められます。

**ウナギの脅威を切り抜ける。** 水中には巨大ウナギ（4種類あるマップ構成のうち1つではクラーケン）が潜んでおり、巻きついて水中に引きずり込み溺死させてきます。以下の重要ルールを徹底してください：

- **防水クローク (oilskin cloak)** を羽織るか、防具に **油（グリース）を塗っておく** と、ウナギが巻きついてきた際に滑り落とすことができます。グリースは時間経過で剥がれるため完全な信頼は置けませんが、防水クロークの効果は永続します。
- **[呼吸の魔除け (amulet of magical breathing)](#movement-and-spatial-behavior)**（または変身による水中呼吸）があれば、巻きつかれて水中に引きずり込まれても溺死を防ぐことができます。
- ウナギは可能な限り **遠距離から撃破してください**。杖、呪文、投擲武器のいずれも有効です。水中にいるウナギに不用意に近接戦闘を挑んではいけません。
- 浮遊や水上歩行の状態であっても、隣接する水マスにいるウナギからの巻きつき攻撃は **防げません**。溺死判定はプレイヤーの足元ではなく *ウナギのいるマス* を基準に行われるためです。防水クローク／グリース、呼吸の魔除け、あるいは接近される前に遠距離から倒すことだけが確実な防御策です。
