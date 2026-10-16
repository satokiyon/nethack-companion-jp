#### 識別と状態変化 (Identification and Status Changes)

| メッセージ | 意味 |
|------------|------|
| *"A feeling of loss comes over you."*<br>（喪失感に襲われた。） | 泉にアイテムを浸して解呪の結果を引きましたが、そのアイテムは呪われていませんでした。何も起きておらず、文面とは裏腹に何かを失ったわけではありません。 |
| *"You have a feeling of loss."*<br>（喪失感を覚えた。） | 「充填の巻物」を読みましたが、充填できないアイテムを選択してしまいました（杖、指輪、および一部の道具のみが充填可能です）。巻物は無駄に消費されました。 |
| *"You sense a lack of food nearby."*<br>（近くに食料が存在しない気配を感じる。） | 「食料を探す巻物」を読みましたが、フロア内に食料が存在しません。 |
| *"You feel materially poor."*<br>（物質的に貧しくなった気がする。） | 「金貨を探す巻物」を読みましたが、フロア内にゴールドが存在しません。 |
| *"You feel like someone is helping you."*<br>（誰かが助けてくれているような気がする。） | 「解呪の巻物」を読みました。装備中の呪われたアイテムの呪いが解けました。 |
| *"Your hands begin to glow red."*<br>（両手が赤く輝き始めた。） | 「モンスター混乱」の巻物を読んだか呪文を唱えました。次の近接攻撃が命中すると相手を混乱させます。（すでに混乱している状態で読むと紫色に光ります。） |
| *"You feel guilty."*<br>（罪悪感を覚えた。） | 祝福された、または混乱状態で「罰の巻物」を読みました。鉄球と鎖は取り付けられませんでしたが、巻物は識別されました。 |
| *"Who was that Maud person anyway?"*<br>*"As your mind turns inward…"* | 「健忘の巻物」を読みました。記憶していた呪文の一部を忘れてしまいました（祝福された巻物なら忘れずに済みます）。 |
| *"You have an uneasy feeling…"*<br>（不安な気分になった…） | 呪われた「啓蒙の薬」を飲んだか、上昇できない場所で呪われた「レベルアップの薬」を飲みました。薬は識別され、それ以外の悪影響はありません（啓蒙の薬の場合は賢明のエクササイズ値が少し下がります）。 |
| *"You feel like a hypocrite."*<br>（偽善者になったような気分だ。） | エルベレス（Elbereth）の上に立った状態でモンスターを攻撃しました。刻み文字は消滅し、属性値にペナルティを受けました（実績値が十分に高ければ一律−5、低ければ−1〜−5）。 |
| *"You feel that monsters are aware of your presence."*<br>（モンスターたちがあなたの存在に気づいた気配がする。） | モンスターがモンスター怒号（反感）の呪文を唱え、フロア中のモンスターを目覚めさせてあなたに向かわせました。 |
| *"You feel that monsters have difficulty pinpointing your location."*<br>（モンスターたちがあなたの位置を正確に捉えにくくなった気がする。） | 「幻影のクローク」の効果が発動しました。*「…no longer have difficulty…」* は効果が切れたことを意味します。 |
| *"You hear the rumble of distant thunder…"*<br>（遠くで雷鳴が轟くのが聞こえる…） | 自分のペット（または飼い慣らした生物）を殺害しました：属性値−15、幸運値−1。属性値がプラスに戻るまで祈りは失敗します。 |
| *"You feel as if you need some help."*<br>（誰かの助けが必要な気がする。） | 近くのモンスターがアイテム呪詛の呪文を唱えました：インベントリ内のいずれかのアイテムがランダムに呪われました。使用する前に祭壇などでBUCを確認してください。 |
| *"You feel the presence of evil."*<br>（悪の気配を感じる。） | 泉から敵対的な「水の魔神」が召喚されましたが、まだ視界に入っていません。接近してきています。 |
| *"You hear someone summoning something, and…"* (および *"…summoning <something>"*) | 司祭系モンスターが視界外で昆虫やヘビを召喚しました。魔法使い系モンスターの召喚では *"Monsters appear from nowhere!"*（どこからともなくモンスターが現れた！）と表示されます。 |
| *"You feel mildly hot."* / *"You feel mildly chilly."* | 火炎（または冷気）攻撃を受けましたが、自身が持つ内在耐性がそれを吸収しました。自分が思っている通りの耐性を実際に持っていることを確認できる貴重な手がかりです。 |
| *"You feel rather itchy under your mummy wrapping."* | 透明の巻物、杖、または呪文を使用しましたが、装備中の「ミイラの包帯」が透明化を遮断しました。透明にはなっていませんが、その巻物／杖が透明化であることを確認できました。 |
| *"You feel less paranoid."*<br>（被害妄想が薄らいだ気がする。） | 扉探索の効果によって、マップ上の古い不可視マーカー `I` が消去されました。モンスターがどこへ移動したかまでは分かりません。 |
| *"You feel agile! You must have been working on your reflexes!"* (および筋力／知力／賢明／器用／耐久／魅力の各種) | 隠されたエクササイズ（鍛錬）システムによって能力値が上昇しました。何が鍛錬に当たるかは [能力値のエクササイズ (Exercising Your Stats)](#exercising-your-stats) を参照してください。逆に *"You haven't been working on reflexes lately"* は不摂生（アビュース）が続いたときに表示されます。 |
| *"You move very quietly."*<br>（非常に静かに移動できる。） | 「忍びの指輪」またはエルフのクロークを装備しました。（エルフの靴の場合は *"You walk very quietly"* となります。） |
| *"Wow! This makes you feel good!"*<br>（おお！ 気分が良くなった！） | 呪われていない「能力回復の薬」を飲み、低下していた能力値が1つ回復しました。 |
| *"Wow! This makes you feel great!"*<br>（おお！ 素晴らしい気分だ！） | 祝福された「能力回復の薬」を飲んですべての能力値が回復したか、あるいは魔法の泉の水を飲みました。 |

---

