#### 経験値レベル低下・ドレイン (Level Drain)
<!-- audit
2026-05-18:
- drain-life attacks (AD_DRLI) reduce u.ulevel by 1 and max HP by mlev gain (exper.c:232-260)
- drained levels do NOT recover over time
- drain resistance prevents the drop entirely (attrib.c:380-384)
- sources: Excalibur, Stormbringer, Staff of Aesculapius; in 5.0, black dragon scale mail or shield of drain resistance
- wraith corpses give 1 level on eat (eat.c:980-985)
- blessed potion of restore ability restores ALL lost levels (potion.c:687-691)
- uncursed/plain restore ability returns one level per quaff
- strategy aligned with NetHackWiki Drain resistance, Wraith, Excalibur: Excalibur/Stormbringer/Staff of Aesculapius for drain resistance, eat wraith corpse to regain a level (https://nethackwiki.com/wiki/Drain_resistance, https://nethackwiki.com/wiki/Wraith, https://nethackwiki.com/wiki/Excalibur)
-->

一部のモンスターは、攻撃が命中した際にプレイヤーの経験値レベルを低下させ、そのレベルの上昇によって得ていた最大HPや魔力を奪い去ります。レイス、塚人、ナズグル、吸血鬼、吸血鬼の首領、そしてヴラド自身がすべてレベルドレイン攻撃を持っています。敵の手にある[ストームブリンガー](#stormbringer) も同様の効果をもたらします。失われたレベルは時間経過では自然回復しません。モンスターを倒して経験値を稼ぎ直すか、能力回復の薬を飲むか（祝福されたものは失われた全レベルを一度に復元します）、あるいはレイスの死体を食べることで取り戻す必要があります。

（なお、生命力ドレインと *筋力（Strength）* ドレインを混同しないでください。コウモリの毒噛みつきは筋力を低下させるものであり、レベルを奪うものではありません。能力値ドレインは別の問題であり、後述の[エンチャント吸魔](#enchantment-drain) はその親類です。）

**防御策：** *ドレイン耐性* を持っていれば完全免疫となります。伝統的な入手先は、[エクスカリバー](#excalibur-artifact)（秩序）、ストームブリンガー（混沌）、あるいは[アスクレピオスの杖](#staff-of-aesculapius)（治療師のクエスト・アーティファクト）の装備です。NetHack 5.0 での新要素として、**黒ドラゴンの鱗鎧**（瞬間分解耐性とドレイン耐性の両方を1スロットで付与）や **ドレイン耐性の盾**（店でランダムに見つかる盾）の着用が挙げられます。

レイスの死体は重量がなく、缶詰にすることもできません（栄養価ゼロ）。戦闘が終わったら新鮮なうちに即座に食べてレベルを回復・上昇させましょう。
