#### エンチャント吸魔 (Enchantment Drain)
<!-- audit
2026-05-18:
- disenchanter generates only in Gehennom (G_HELL: monsters.h:2156, makemon.c:1935, 1998)
- active claw targets armor via some_armor (do_wear.c:2629, uhitm.c:3619)
- target order: cloak → body armor → shirt → 1/4 chance for helm/gloves/boots/shield (do_wear.c:2634-2652)
- if naked, rn2(5) picks ring/amulet/blindfold; never targets a wielded weapon (uhitm.c:3621-3640 mhitm_ad_ench cases 0-4 enumerate uright/uleft/uamul/ublindf only)
- active hit prints "Your X seems less effective" (uhitm.c:3641)
- weapon drain is passive-only: fires when you melee the disenchanter (mhitu.c:2508-2515)
- passive drain is silent
- obj_resists: 10% chance for ordinary, 90% for artifact (zap.c:1392-1394)
- Invocation items and Rider corpses always resist (zap.c:1462-1467)
- MC negates the active attack (uhitm.c:3613) but NOT the passive counter
- eating a disenchanter corpse strips a random intrinsic (eat.c:1270-1275)
- strategy aligned with NetHackWiki Disenchanter, Magic cancellation: MC armor blocks the active claw but not the passive counter; range-kill is the cleanest plan, and the corpse is not safe to eat (https://nethackwiki.com/wiki/Disenchanter, https://nethackwiki.com/wiki/Magic_cancellation)
-->

**吸魔の怪物 (Disenchanters)**（`R`、青色）は、[ゲヘナ](#gehennom) にのみ出現します。その爪は着用している装備の魔法強化を吸い取り、近接攻撃で殴りかかると手持ちの武器のエンチャントを削り取ってきます。

モンスターからの **能動的** な爪攻撃は、着用している防具のいずれか1つ（クロークが最優先、次いで鎧、シャツ、そして兜・小手・靴・盾が等確率）を選び、その強化値を1下げます。防具を一切着ていない場合は、指輪、魔除け、目隠しのいずれかを侵食します。**能動的な攻撃が手持ちの武器を標的にすることはありません**。攻撃が命中するたびに「あなたの〜の効果が薄れたようだ（Your ... seems less effective）」とメッセージが出るため、発生したことは分かります。

一方、プレイヤーの武器がエンチャント低下を被るのは、近接攻撃で吸魔の怪物を殴った際の **受動的** な反撃ダメージによるものだけです。3〜4回近接攻撃を当てるだけで、丹精込めて鍛えた+7の剣があっという間に+3にまで劣化します。しかもこの受動的ドレインはメッセージが出ず無音で進行します。遠距離攻撃で仕留めれば、両方の吸魔攻撃を完全に回避できます。

**防御策。** **魔法防御力（MC3）の防具** は、防具に対する能動的ドレインをほぼ遮断しますが、武器を劣化させる近接反撃を止めることはできません。争いの指輪やペットを使って他の標的へ誘導するのが有効です。アーティファクトは10回中9回の確率で吸魔に抵抗しますが、通常のアイテムは10回中1回しか抵抗できません。**死体は絶対に食べてはいけません**。ランダムに持っている内在能力を1つ奪い取られます。
