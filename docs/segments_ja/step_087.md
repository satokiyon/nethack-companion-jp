#### 致死毒 (Deadly Poison)
<!-- audit
2026-05-19:
- AD_DRST extra-damage roll is ~1/240 per qualifying hit: rn2(8) × rn2(30) (uhitm.c:3154, attrib.c:362)
- poison death is purely `u.uhp <= loss`, no carrycap term (attrib.c:366) — burden is irrelevant
- poison resistance grants full immunity (attrib.c:338-343)
- Famine corpse is instantly fatal (eat.c:831-838)
-->

一部のモンスター（クサリヘビ、殺人蜂、コブラ、一部の蜘蛛など）は、通常の打撃ダメージに加えて 10〜30 もの追加HPダメージを与える猛毒攻撃の判定を持っています。最大HPが高い状態であれば耐えられることが多いですが、低レベルや手負いの状態では一撃で命を落とします。この「追加致死ダメージ」の抽選は、該当する毒攻撃が命中するごとにおよそ240分の1の確率で発生します。また、黙示録の四騎士（死、ペスト、飢餓）の死体を食べた場合、残りHPに関係なくその場で即死します。

**防御策：** [毒耐性](#damage-resistances) を持っていれば完全免疫となります。大半のキャラクターは、序盤に毒持ちモンスターの死体を適切に食べることで毒耐性を獲得できます。これはゲーム開始直後に真っ先に確保すべき最重要の内在能力のひとつです。

