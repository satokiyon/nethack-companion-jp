#### ノームの鉱山 (The Gnomish Mines) {#the-gnomish-mines}
<!-- audit
2026-05-18:
- Mines branch DL 2-4 (dungeon.lua:15-19; base=2 range=3)
- 7 Minetown variants (dungeon.lua:179-184); 1/7 picks Orcish Town (minetn-1.lua)
- gnomish PC lovemask MH_DWARF|MH_GNOME → gnomes and dwarves peaceful (role.c:654)
- Orcish Town: unaligned altar, no shops, no priest, iron-bar terrain (minetn-1.lua:18, 52, 79-88)
- Orcish Town scatters 7+ candles since Izchak's shop is absent (minetn-1.lua:98-105)
- candle shop present in minetn-2..7 (Izchak); absent only in minetn-1 (minetn-{2..7}.lua)
- all 3 Mine's End layouts place a not-cursed luckstone (minend-1.lua:77, minend-2.lua:116, minend-3.lua:67)
- minend-1 hides the luckstone among FOUR mimics (appear_as luckstone/loadstone/flint/touchstone, lines 59-71) plus a real cursed loadstone (74); search (`s`) exposes the mimics, price-ID sorts the two real stones — full mechanics in the Gray Stones section audit
- Minetown watchmen are peaceful=1 in non-orcish variants (minetn-2.lua:149)
- strategy aligned with NetHackWiki Gnomish Mines, Minetown, Mines' End, Standard strategy: Minetown described as the prime price-ID/BUC-test/priest-donation stop; guaranteed luckstone at Mine's End is canonical; Standard strategy recommends Sokoban-before-Mines as the default branch ordering for the reflection/BoH prize before tackling the Mines pack fights (https://nethackwiki.com/wiki/Gnomish_Mines, https://nethackwiki.com/wiki/Minetown, https://nethackwiki.com/wiki/Mines%27_End, https://nethackwiki.com/wiki/Standard_strategy)
-->

鉱山への入り口は、ダンジョンの地下2階から4階のどこかに下り階段として現れます。以下のマップ図のように、壁が荒削りの岩肌になり、通路がいびつに入り組んでいるため、鉱山に入ったことはすぐに分かります。

```
               ··└       ·······?└┘·└─┐
                ··└      ·G···········│
                ···      ┐·····*······└
                 ··└┐    │··`········
            ┌──┐ ┐··│┌─┐┌┘········
          ┌─┘··└┐│··└┘·└┘······┌
         ┌┘·····│┌─·`·······<·┌
         │······└┘·····)······└┐
     └───┘····┌┐····)··········└─┘  └┐
┐·············││·`········@··········│
└─┐······─┐·──┴┼─┐···················└
  └──┐·   │····└─┘···┌┐h··············└
     └┐   └──┐·······│└─┐···┌┐·········│
             └──┐····└  └───┘ ─┐·│····┌┘
```

鉱山には主にノームとドワーフが生息しており、深く潜るにつれて手強い上位種（ノームの領主、ドワーフの領主、そしてノームの王やドワーフの王）が現れます。プレイヤーがノームまたはドワーフの種族を選んでいる場合、彼らの大半は友好的であるため、鉱山は比較的快適な寄り道となります。それ以外の種族の場合は、敵対するノームやドワーフの絶え間ない猛攻を切り抜けていく必要があります。

また、鉱山には悪名高いサプライズゲストが存在します：鉱山街を除く任意のランダムな鉱山階層（鉱山最深部を含む）で、マインドフレイヤが生成される可能性があります。未探索の鉱山フロアで *"You sense a faint wave of psychic energy"*（精神エネルギーのかすかな波を感じる）という警告メッセージが出たら要注意です。マインドフレイヤは触手攻撃が命中するたびに知力を吸い取ってきます。序盤では兜による防護や安全に戦うための遠距離火力が不足していることが多いため、一度退却して準備を整えるか、この支流を後回しにするのが賢明です。

**鉱山街 (Minetown)** は、鉱山を数階層潜ったところに現れます。通常は店と寺院が並ぶ小さな居住地です。鉱山の敵集団を安定して撃退できるようになってから訪れるか、最初の挑戦で苦戦したなら倉庫番をクリアした後に再訪しましょう。店では不要なアイテムをゴールドに変えたり、役立つ装備を購入したりできます。寺院には祭壇（属性を確認してください）と常駐の司祭がいます。祭壇が自分の属性と一致していれば、アイテムをドロップして鑑定できる安全な拠点となります。また、鉱山街の司祭はACを永続的に強化してくれます。条件を満たした最初の寄付では、単なる1ポイントではなく2〜4ポイントの内在的防御値（プロテクション）が授けられます。金額と上限の基準は読み違えやすいため、[司祭への寄付 (Donating to Priests)](#donating-to-priests) の完全な表を参照してください。

ろうそくはゲーム進行中に十分な数が手に入ることが多いですが、後半で祈りの燭台（Candelabrum of Invocation）に立てるために7本確保する必要があります。鉱山街にある **イズチャックの照明店 (Izchak's lighting store)** が最も確実な調達先です。ここで7本まとめて買いましょう。店が生成されなかった場合（オークの町のマップ構成）、そのフロアのあちこちに7本以上のろうそくが散乱しています。蜜蝋のろうそくの方が獣脂のろうそくよりも長持ちしますが、どちらでも機能し、混ぜて使っても問題ありません。

ただし、7回に1回の確率で、鉱山街は **オークの町 (Orcish Town)** として生成されます。店も司祭も存在せず、入り口が鉄格子で塞がれた、オークたちに占拠された廃墟です。無属性の祭壇は残っていますが、買い物は一切できません。

また、鉱山街の警備員（町の警備隊）には十分注意してください。盗みを働く、友好的な生物を攻撃する、扉を破壊する、あるいは町の中で地面を掘削しない限り、警備員たちは友好的です。しかし1人でも怒らせると、警備隊全員が一斉に敵に回ります。

**鉱山最深部 (Mine's End)** はノームの鉱山の最深層です。3種類ある鉱山最深部のレイアウトのいずれにも、確定で（呪われていない）**幸せの石 (luckstone)** が1つ配置されているため、どのバリエーションに到達しても確実に手に入ります。幸せの石は幸運値を+3し、良い幸運が時間経過で自然減衰するのを防ぎます。聖水で祝福してゲームクリアまで常に持ち歩きましょう（[幸運の仕組み (How Luck Works)](#how-luck-works) を参照）。

幸せの石を見つけ出すには慎重な探索が必要です。ほとんどのレイアウトでは隠し部屋の中に配置されているため、迷路が行き止まりになり宝が見当たらない場合は、掘削耐性のある壁を無理に掘るのではなく、壁を捜索（`s`、`10s`）して隠し扉を探してください。隠し部屋が複数存在することもあるため、最初の1つで見つからなくても諦めてはいけません。（バリエーションの1つでは、灰色の石に擬態した4体の [**ミミック**](#a-note-on-mimics) と、見た目が全く同じで手持ちの荷物に呪い張り付く本物の **呪われた重し (loadstone)** の中に幸せの石が紛れ込まされています。怪しい石の隣で捜索（`s`）を行えば、ミミックはその場で正体を現します。本物の石は何の反応も示しません。これで幸せの石と重しの2択に絞られるため、あとは店に持ち込んで価格で識別します（幸せの石は60zm、重しは1zm）。ここでは石を蹴って判定する方法に頼ってはいけません。壁の隙間に挟まっていると、本物の幸せの石であっても重しのように鈍い音を立てて足の指を痛めることがあります。）
