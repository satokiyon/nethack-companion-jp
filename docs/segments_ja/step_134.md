### 巻物入れ (The Scroll Rack)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Armor-enchant safe cap is +3 for ordinary body/helms/boots/gloves, +5 for elven armor / wizard's cornuthaum (do_wear.c). Table & prose had blanket +5; corrected.
- Genocide prompt takes single monster name (e.g., "lich") or uppercase class (e.g., "L"); blessed class wipe excludes player's own role species (makemon.c:1340).
-->

巻物は、ダンジョンにおける使い捨ての呪文です。1回読む（`r`）と効果が発動し、消滅します。巻物にはゲームごとにランダムにシャッフルされた奇妙な文字列（「ZELGO MER」、「DAIYEN FOOELS」、「PRATYAVAYAH」など）がラベルとして印字されており、識別するまでは意味を持ちません。

