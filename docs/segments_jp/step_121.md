#### 判明した情報の名付け (Naming What You've Learned) {#naming-what-youve-learned}
<!-- audit
2026-05-21:
- mergable() requires identical otyp, enchantment (spe), BUC, erodeproof state, erosion (oeroded, oeroded2), greased state, oeaten/orotten for food; coins merge unconditionally (invent.c:4379-4460)
- on merge that propagates a previously-unknown property, the game prints "You learn more about your items by comparing them." (invent.c:938-942); guarded against LOST_THROWN to avoid spam when monsters strip ID
2026-05-18:
- `#name` and `#call` aliases at cmd.c:1773-1774
- class naming at do_name.c:571-588
- rename-by-overwrite at do_name.c:660-672
- N keystroke only works in number_pad mode; default vi-keys binds N to run-north — cross-layout shortcut is C for #call
-->

手がかりを集めたら、`#name`（または `#call`）コマンドを活用して判明した情報を記録しましょう。アイテムの種別クラス全体に対して、任意の名前を **呼び名（call）** として付けることができます。たとえば、「泡立つ薬」が200ゴールドの価格帯グループに属することが分かったら、忘れないように「泡立つ=200G」と名付けておきます。その後モンスターに投げつけて相手が加速したら、そのクラスの名前を「加速」へと上書き変更すればよいのです。

**スタック（同一枠まとめ）による識別。** アイテムを拾い上げた際、ゲームはそのアイテムが手持ちの既存アイテムと **完全に同一** である場合にのみ、同じスロットへと合体（スタック）させます：同じ種類、同じ強化値、同じBUC、同じ耐腐食加工などです。したがって、新しく拾ったアイテムが既知のアイテムとまとまるかどうかを見るだけで、無料で情報を得ることができます。合体によって実際に新たな知識が得られた場合、ゲームは明示的にメッセージを表示します：*「持ち物を比較して、より多くのことが分かった (You learn more about your items by comparing them.)」*。このメッセージが出たら、既知の特性（BUC、強化値、腐食状態など）が未知のアイテム側にも引き継がれた合図です。同じ外見でありながらスタックしないアイテムは、異なる薬であるか、BUCが異なるか、あるいは希釈・腐食されているかのいずれかです。
