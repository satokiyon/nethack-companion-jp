### 武器一覧表 (Weapons Tables)

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 objects.h + weapon.c: no corrections. Every weapon row (base/bonus dice, weight, cost, to-hit, material, two-handed/launcher/skill notes) verified, including composite-damage entries vs dmgval().
-->

ダメージは**小型に対するダメージ / 大型に対するダメージ (vs small / vs large)**として表記されており、強化値（強化・呪い）が加算される前、かつ銀や材質による追加ボーナスを除いた基本ダイス値です。**重量 (Wt)**はユニット重量、**価格 (Cost)**は店における未強化時の基本価格（Zm: ゾークミッド）、**命中 (Hit)**は武器自体に組み込まれている命中補正ボーナス（大半は 0）を表します。盾の装備や二刀流（二刀流戦闘）を阻害する両手持ち武器には、備考欄にフラグが付けられています。武器はスキルごとに分類されています。スキル枠（スロット）を投資する前に、[職業別のスキル上限一覧](#per-role-skill-caps)を確認してください。一部の武器に見られる括弧内の名称は、侍（Samurai）がプレイした際に画面上に表示される別名です（ゲーム内部では同一のアイテムとして処理されます）。
