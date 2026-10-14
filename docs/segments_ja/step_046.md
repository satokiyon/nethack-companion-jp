### 罠と危険 (Traps and Hazards)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source (domagictrap trap.c:4319-4453):
- Rewrote the magic-trap effects paragraph. It is fate=rnd(20): <10 blind+summon 1d4; 10 nothing; 11 toggle invis; 12 fire; 13-18 flavor; 19 tame+CHA+1; 20 UNCURSE inventory. Old text's "curse an item" was backwards; sleep/stun/vomiting/earthquake/HP/mana/mapping/lighting don't exist; CHA is +1 on ~1/20 (~+0.05/zap), not +1.4.
- Confused gold detection reveals ALL traps (trap_detect, read.c:2042), not just magical.
- "A rumbling stop abruptly" is a boulder hitting a teleport trap only (trap.c:3477); pits route through flooreffects.
- Verified correct: pit/spiked-pit damage, trapdoor cascade, bear-trap diagonal escape, anti-magic/cancellation blasts, iron-footwear protections.
-->
<!-- audit
2026-05-31:
- mktrap() places traps in rooms only (somexyspace(croom)) on standard dungeon levels; the MAZEFLAG path that allows corridor traps is set on maze levels (Gehennom mazes, etc.). Standard corridors do not generate traps (mklev.c:2032-2099, somexyspace usage at line 2093).
- display priority: monster > object > trap > floor. A corpse object on a trap square draws as `%` and hides the `^` glyph (display.c symbol layering).
- #untrap requires the trap to be visible (known) and the player to be adjacent (or on the trap). It then attempts to disarm based on trap type (trap.c untrap_object).
-->

たった1つの落とし扉によって、愛するペット、保管しておいた貴重な物資、そして利用するはずだった階段から一瞬にして分断されてしまうことがあります。罠は、自分で踏み抜くか、`s` キーで探知するか、あるいは他の手段で暴くまで目に見えません。発見されると、マップ上には `^` として表示されます。隣接するマスを1回捜索するごとに罠を発見できる独立した抽選が行われますが、その成功率は決して100%ではないため、怪しい場所では繰り返し粘り強く捜索を行う必要があります。ペットはあなたがすでに発見済みの罠しか避けてくれないため、ペットの挙動を眺めていても未発見の罠を察知することはできません。

覚えておくべき典型的な状況があります：部屋の床の上に理由もなく死体がポツンと転がっている場合、それはその冒険者を仕留めた罠の上に覆い被さっていることが多々あります。死体の記号 `%` は `^` の上に優先して描画されるため、本来なら視認できているはずの罠が隠されたままになります。その死体の下には持ち主が落とした装備品が重なっていることもあり、調べる価値は大いにあります。隣接するマスから周囲を捜索して罠を暴き、不用意に足を踏み入れる代わりに `#untrap` コマンドを使って罠の解除を試みましょう。

以下はダンジョンで遭遇する罠の一覧であり、踏み抜いたときの痛恨度（後悔の度合い）によって大まかに分類されています：

