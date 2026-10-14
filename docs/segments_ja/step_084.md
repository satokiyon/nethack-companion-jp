#### 攻撃の杖 (Attack Wands)
<!-- audit
2026-05-18:
- mwandexp gates the first-zap warning miss (muse.c:1830-1860)
- buzz_force_miss is the dispatch path for the warning shot (muse.c:1815, 1834)
- 6 beam wands trigger the warning: death, sleep, fire, cold, lightning, magic missile (muse.c:1842-1847)
- the visible warning shot identifies the wand to the player
- late-game zones spawn monsters with mwandexp=TRUE — no warning shot (makemon.c:1290-1293)
- late-game zones: Stronghold, Knox, Quest, Gehennom, Vlad's Tower, endgame
-->

強力な杖による攻撃を受けることは、即死を意味する場合があります。死の杖や「死の指」の呪文は、適切な防御手段を持たないキャラクターを一瞬で絶命させます。また、冷気、炎、電撃、マジックミサイルの光線系の杖も、即死級の壊滅的なダメージを叩き出すことがあります。

**防御策：** 「反射」の能力はあらゆる光線を跳ね返します。「耐魔（魔法防御）」は死の光線およびマジックミサイルの光線を無効化します。通常、大半のモンスターがプレイヤーに対して光線系の杖（死、睡眠、炎、冷気、電撃、マジックミサイル）を最初に振る際、その初弾は必ず外れる仕様（警告射撃）になっています。モンスターが視界内にいれば、その瞬間に何の杖であるかが自動識別されるため、何が自分に向けて発射されたかを把握し、次の命中弾が飛んでくる前に対処するための1ターンの猶予が与えられます。ただし、城、要塞リュディオス、クエスト、ゲヘナ、ヴラドの塔、各大系などに自生する終盤のモンスターたちは、この初弾ミスの手加減をしてくれません。

