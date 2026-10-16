#### 窒息 (Choking)
<!-- audit
2026-05-18:
- eat-while-satiated death via done(CHOKING) (eat.c:248, 286); warning string at eat.c:3314
- "Continue eating?" prompt only with paranoid_confirmation:eating (default off)
- death only fires at u.uhunger >= 2000 with 1/20 escape; Breathless never choke (eat.c:258-266)
- amulet of strangulation generates 90% cursed (mkobj.c:1063); beginner can't just take it off
- escape: pray, or uncurse via holy water or remove curse
- strangulation is a timer death via done_timeout(DIED, STRANGLED), not an attack — MR has nothing to block (timeout.c:890-894)
-->

「満腹（Satiated）」の状態を超えて無理に食べ続けると、喉を詰まらせて窒息死する危険があります。ゲーム画面には警告として「飲み込むのが苦しくなってきた（You're having a hard time getting all of it down）」というメッセージが表示されます。設定で食事の警告確認（`paranoid_confirmation:eating`）を有効にしていれば、確認プロンプトも表示されます。一定の栄養値上限を超えると、20分の1の確率で生還できるか、「無呼吸（Breathless）」の特性を持っていない限り、その食事によって即座に絶命します。

**窒息死に至るもうひとつのルートは「絞殺の魔除け（amulet of strangulation）」です。** 身につけると首に短いカウントダウンが始まり、時間が切れた瞬間に死亡します。この魔除けは90%の確率で呪われた状態で生成されるため、大抵の場合は単に手で外すことができません。神に祈る（`#pray`）か、聖水や「解呪」の手段を用いて呪いを解いてください。「耐魔（魔法防御）」はこの効果を防ぐ役には立ちません。ただし、「無呼吸」のモンスターに変身していれば助かります。

**防御策：** 満腹状態のときは決して食事をしないでください。また、未識別の魔除けを不用意に首にかけることには極めて慎重であってください。

