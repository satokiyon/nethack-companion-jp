#### クエスト (The Quest)
<!-- audit
2026-05-18:
- quest portal Dlvl 11-16: Oracle DL 5-9 + base=6 range=2 chained off Oracle (dungeon.lua:62-64, 27-31)
- XL 14 required to descend (quest.h:45 MIN_QUEST_LEVEL, quest.c:149)
- friendly word with leader on first quest level (quest.c:97 Is_qstart → on_start)
- alignment-record refusal at MIN_QUEST_ALIGN below threshold (quest.c:164)
- 3 artifacts grant carried MR via CARY(AD_MAGM): Orb of Detection, Magic Mirror, PYEC (artilist.h:221, 257, 293)
- 3 artifacts grant wielded/worn MR via DFNS(AD_MAGM): Sceptre of Might, Eyes of Overworld, Eye of Aethiopica (artilist.h:234, 262, 305)
- nemesis gets Bell of Opening as starting inventory; drops on kill (makemon.c:1378-1379)
- quest artifact is placed under nemesis at level generation, NOT carried (Val-goal.lua:49,76; Wiz-goal.lua:73,96; etc.)
- return portal lives on Is_qstart (first quest level) only (quest.c:97, 191-204)
- "nemesis carries an amulet of life saving" is wiki-belief, not source-guaranteed; M2_COLLECT means they may pick one up (https://nethackwiki.com/wiki/Nemesis)
- strategy aligned with NetHackWiki Quest, Bell of Opening, Quest artifact: XL 14 + 20 alignment record gate, nemesis guards both artifact and Bell, return-portal only on the first quest level (https://nethackwiki.com/wiki/Quest, https://nethackwiki.com/wiki/Bell_of_Opening, https://nethackwiki.com/wiki/Quest_artifact)
2026-08-13:
- wraith corpse on graveyard levels: NOT "never" — LEVEL_SPECIFIC_NOCORPSE (mon.c:44-47) suppresses an undead's corpse only when (graveyard && is_undead && rn2(3)), i.e. 2/3 of the time, so ~1/3 still drop. off a graveyard a wraith always corpses (PM_WRAITH is in the unconditional-corpse case, mon.c:835). softened prose from "don't drop on graveyard levels" to "only about a third as often." lead-the-wraith-out advice still good (1/3 -> guaranteed).
- verified: MIN_QUEST_LEVEL 14 (quest.h:45); eating a wraith corpse => pluslvl(FALSE) guaranteed level gain (eat.c:1141).
-->

遅かれ早かれ、あなた自身の同胞から呼び出しがかかります。「クエスト」は、あなたの役職のためだけに用意された特別なダンジョン支流です。宿敵（ネメシス）があなたの役職に伝わる伝説のアーティファクトを強奪しており、リーダーはあなたを呼び出して力を証明させ、宿敵を打ち倒して至宝を取り戻す使命を与えます。ダンジョンの地下11階から16階のあたりで、魔法のポータルがその入り口へと導いてくれます。

適切なフロアに到達したかどうかはすぐに分かります。そのフロアに初めて足を踏み入れた瞬間、クエストリーダーからの微弱なテレパシーの呼びかけが頭の中に響き渡ります：

> *微弱なテレパシーによるメッセージを受信した .... 至急助けが必要だ .... ...ックな転送機を探せ。最後のメッセージはよく聞き取れなかった。*

これで探すべきものが「魔法のポータル」であることが分かります。発見するとマップ上に鮮やかな赤紫色の `^` として表示されます。他の罠と同様に、そのマスを踏む（同時に作動します）か、周囲を捜索するまで姿を隠しています。

クエストに本格的に乗り出すには、**経験レベル14** に到達し、かつ最上階（最初の階層）にいるクエストリーダーと友好的に会話を交わして階下への許可を得る必要があります。準備が整い、資格があると認められれば、リーダーは宿敵からクエストアーティファクトを取り戻す旅へと送り出してくれます。

中盤の経験値稼ぎは時間がかかるため、レベル14に到達する道のりとしては、いくつかの [レイスの死体](#a-note-on-wraiths) を食べる（1体につき経験レベルが1上昇します）か、祝福された「レベルアップの薬」を飲むのが定石です。（「死の谷」のような墓場フロアでは、アンデッドが死体を残す確率は通常の約1/3に低下するため、レベルアップを狙うならレイスを墓場の外へと誘導してから倒すのが賢明です。）

各役職には、固有のマップ、固有の宿敵、そして固有のアーティファクト報酬が用意されています。ワルキューレは [運命のオーブ (Orb of Fate)](#orb-of-fate) を求めてスルト卿（Lord Surtur）を狩ります。侍の道は [村正の剣 (Tsurugi of Muramasa)](#tsurugi-of-muramasa) を巡る足利尊氏との決闘で締めくくられます。魔法使いは [エチオピカの目 (Eye of the Aethiopica)](#eye-of-the-aethiopica) を取り戻すため闇の王の要塞へと潜入します。役職ごとの完全な一覧は [アーティファクト (Artifacts)](#artifacts) の章を参照してください。

大半のクエストアーティファクトは、ゲームクリアまで常に持ち歩くに値する至宝です。魔法防御、テレパシー、警告、反射、忍び足、幸運などの強力な能力を複合的にもたらしてくれます。その保護効果が「所持しているだけ」で発動するのか、それとも「手に持つ／身につける」必要があるのかを確認しておきましょう。

**宿敵の足元には、もう1つの極めて重要な至宝が待っています。** **開放の鐘 (Bell of Opening)** は宿敵の荷物の中にあり、倒した瞬間に床にドロップします。これは「開扉の3つのアイテム（Invocation items）」の1つであり、これなしにゲームをクリアすることは不可能です：[ゲヘナ (Gehennom)](#gehennom) の最深部、[モロクの聖域 (Moloch's Sanctum)](#molochs-sanctum) の直上にある「振動するマス」の上で、開放の鐘を鳴らし、祈りの燭台を灯し、死者の書を読み上げることで、イェンダーの魔除けが眠る聖域への扉が開かれます（儀式の完全な手順は [奪還作戦 (The Heist)](#the-heist) を参照）。一方、あなたのクエストアーティファクトは、フロア生成時に宿敵の足元に直接配置されています。立ち去る前に両方のアイテムを確実に回収してください。どちらもクエストダンジョン以外では手に入りません。

宿敵は道中で「命の魔除け」を拾って身につけていることがあるため、致命の一撃を与えても耐えられ、2回倒さなければならなくなっても動揺してはいけません。なお、メインダンジョンへ戻る脱出ポータルは **クエストの最初の階層にしか存在しません**。準備不足のまま深く潜り、途中で引き返す羽目になった場合、長い道のりを自力で登り直すことになります。

クエスト全体は、リーダーの認可にかかっています。経験レベルが14未満であるか、あるいは属性値（信仰実績）が不足している場合、自動的に追い出されます（問題を解決した後に再訪すれば受け入れてもらえます）。もしキャラクターの属性自体が変わってしまっていた場合、リーダーから永久に追放されてしまいます。クエストに挑む前に「逆属性の兜」を面白半分で試してはいけません。

