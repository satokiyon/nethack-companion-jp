---

### 店の利用：信用・借金・トラブル {#shopping-and-shopkeeper-pricing}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- 22 gem prices, Mohs hardness, hard-gem threshold >=8 verified (objects.h, shk.c).
- Dunce cap and low-XL Tourist each multiply buy by 4/3.
- Angry-shopkeeper surcharge adds (price+2)/3 per billed item (~33%).
- Charisma price tiers: >18 halves, =18 2/3, 16-17 3/4, <=5 doubles, 6-7 3/2, 8-10 4/3.
- Touchstone full ID requires blessed (or non-cursed for Archeologist/Gnome); uncursed gives streak color.
-->

店は単に品物を売買するだけの場所ではありません：その価格設定システムは、ゲーム内で最も強力な未識別アイテムの判別ツールです。詳細なメカニズムと価格換算表については第4部の [価格識別法](#the-price-is-right) で解説しました。ここでは残る重要な要素である、預け金（クレジット）、借金、店主との戦闘、そして見落としがちな特殊ルールを網羅します。

何よりもまず、最大の致命的ミスを防ぐための鉄則：**「未払いの品物を持ったまま店の敷居を跨いではならない」**。店主は即座に敵対化し、出口を塞ぎ、キーストン・コップを召喚します。店を出る前に必ず `I` を押して `u`（未払い品）を確認し、代金を清算してください。後から代金を支払えば、追跡してくるキーストン・コップは全員撤収します。

