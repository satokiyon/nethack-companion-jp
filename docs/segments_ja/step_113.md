#### 価格識別 (The Price Is Right)
<!-- audit
2026-05-18:
- buy/sell multipliers and Cha bands match shk.c get_cost/set_cost
- sell offer is 1/2 base (shk.c:3160); 3/8 on unID items from an unfamiliar shopkeeper (shk.c:3173-3174)
- Tourist surcharge (+33%) applies with dunce cap, Tourist below XL 15, or visible Hawaiian shirt — non-stacking
- ~1/4 of unID items carry a 4/3 buy surcharge rolled per item instance via oid % 4 (shk.c:2864-2872 oid_price_adjustment); two identical-looking stacks on a shop floor can roll differently because place_object doesn't auto-merge
- ~1/4 of shopkeepers are "unfamiliar" with unID; they offer 3/4 sell, fixed per shop
- angry-shop +33% surcharge sticks: pacify_shk(FALSE) at shk.c:2663 does NOT clear it
- only pacify_shk(TRUE) clears (shk.c:302, 793 — bones-load and new-customer transitions)
- the JS price widget mirrors get_cost/set_cost exactly
- AMULET macro hard-codes base price 150 for every magic amulet; FAKE_AMULET_OF_YENDOR is base 0 (objects.h:831-834, 865-869)
-->

すべての未識別アイテムには、固定された基本価格が設定されています。魅力（Charisma）が 11〜15 で追加割増がない場合、店主が提示する購入価格（buy quote）はその基本価格そのものになります。また、手持ちのアイテムを店主に売却する際の通常買取価格は、基本価格の半額（1/2）です。この仕様により、店は単なる市場であるだけでなく、極めて優れた **「識別ステーション」** として機能します。

> *店主の価格設定システムは、Gregory Bond氏の『買い物スポイラー (Shopping Spoiler)』（Kate Nepveu氏がHTML化しsteelypips.orgで公開）で初めて詳細に文書化されました。その後、David Damerell氏の『アイテム識別スポイラー (Object Identification Spoiler)』によって価格に基づく識別技法がさらに拡張されました。以下の解説はその両方を基盤にしています。*

アイテムを拾い上げずに価格を確認するには、そのアイテムの上に立ち、**`:`** を押すか、その場に立ったまま店主に向かって **`#chat`** で話しかけてください。店の入口から手持ちのアイテムを店内に投げ入れてはいけません。価格の提示は一切受けられず、店主の懐にそのまま着服されてしまいます。

以下の3つの条件のいずれかを満たすと、同一の **「カモ（観光客）割増」** が適用されます：
- *とんがり帽子（dunce cap）* を着用している
- *経験値レベル15未満の観光客* でプレイしている
- 鎧やクロークを着用せず、*Tシャツまたはアロハシャツ* を丸出しにしている

これらに該当すると、購入価格が 1/3（約33%）引き上げられ、売却価格は基本価格の 1/2 から 1/3 へと買い叩かれます（これらの条件は重複して累積しません）。魅力の値は購入価格にのみ影響します。店で商談を行う前に、必ずシャツの上に防具を着て覆い隠してください。

同じカテゴリに属し、同じ基本価格を共有するアイテム群を **「価格帯グループ（price group）」** と呼びます。価格を確認するだけで、多くの場合2〜3種類の候補にまで絞り込むことができます。魅力が低いと購入価格が跳ね上がり（魅力5以下で基本価格の2倍）、魅力が高いと安くなります（魅力19以上で基本価格の半額）。換算方法は後述の表を参照してください。

未識別の商品には2つの例外的なブレが生じます。商品の約4個に1個には、恒久的な **1/3（約33%）の購入割増** がランダムに付与されます（そのため、同じ外見のアイテムの山であっても個体ごとに提示額が異なる場合があります）。また、店主のおよそ4人に1人は、未識別の品物に対して通常の買取価格の **3/4** しか提示してくれません（この傾向はアイテムごとではなく店主ごとに固定されています）。提示された価格が想定したティアと微妙にズレている場合は、前後のティアも確認してください。

**怒った店主。** 店主を攻撃したり、店主に向けて杖を振ったり、代金を支払わずに店を出ようとしたり、店舗の破損代金の支払いを拒否すると店主は激怒します。事態を収拾して店主を宥めた後であっても、その店主は恒久的に 1/3 の購入割増を請求し続けます（売却価格には影響しません）。

**戦闘後の買収。** 単なる借金ではなく実際に店主に刃を向けた場合、店主はお金ではなく血を求めます。しかし、それでも買収して許してもらう道は残されています。手元に1000ゴールド以上の現金を持った状態で `p` を押すと、1000金貨を支払って宥める試行ができます。あなたがその店の常連顧客として登録されている場合、この買収は約3回に1回の確率で失敗し、金貨を失った上に店主は激怒したままになります。それ以外の場合は店主は落ち着きを取り戻します（ただし前述の割増は残ります）。

**不可視状態での入店。** 店主は目に見えない顧客とは商売をしてくれません。透明化（不可視）の状態で足を踏み入れると、「透明なお客様はお断りです！（Invisible customers are not welcome!）」と怒鳴られ、価格の提示も売買も一切拒否されます。もし不可視状態から戻れなくなってしまった場合は、クロークのスロットに「ミイラの包帯」を着用してください。透明化が遮断されて姿が可視化され、店主と通常通り取引できるようになります。再び姿を消したければ、店を出る際に包帯を脱ぎましょう。

<!-- audit
2026-08-01: shop stock is theme-restricted (shknam.c shtypes[]).
- lighting store lists only specific light items, no generic class slot:
  wax/tallow candle, oil lamp, brass lantern, magic lamp, POT_OIL,
  WAN_LIGHT, SCR_LIGHT, SPE_LIGHT (shknam.c:333-346) -> every wand=light,
  potion=oil, scroll=light, spellbook=light.
- delicatessen potions limited to POT_FRUIT_JUICE/POT_BOOZE/POT_WATER;
  rest random FOOD_CLASS + ICE_BOX (shknam.c:269-274).
- restriction applies to generated stock; resold dropped items are not.
-->

**専門店の品揃えも重要なヒント。** 特定のジャンルを専門に扱う店舗は、そのテーマに合致したアイテムしか仕入れません。したがって、**「どこで見つけたか」** だけでアイテムの正体を特定できることがあります。照明器具店の棚に並んでいるものはすべて光に関連するアイテムです：そこにあるすべての杖は「明かりの杖」、すべての薬は「油」、すべての巻物は「光の巻物」、すべての魔法書は「光の魔法書」です。食料品店に並ぶ薬は「果物ジュース」、「酒」、「水」のいずれかしかありません。これらは店主が元から仕入れていた商品にのみ適用されるルールであり、あなたやモンスターが床に落とした品物には当てはまりません。

以下に、アイテム種別ごとの価格表を掲載します。

::: print-only

