#### 溺死 (Drowning)
<!-- audit
2026-05-18:
- drown check uses monster's tile (uhitm.c:3389-3390)
- Swimming, Amphibious, or Breathless all defeat the drown (youprop.h:264-277)
- pool-entry check at hack.c:3272; Flying also skips entry, Levitation is the canonical defense
- emergency_disrobe is gated on Stressed+ (trap.c:4897-4941)
- krakens placed only on medusa-4 in the Dungeon (medusa-4.lua:122); other placements are Quest/fakewiz/wizard1
- "swamp rooms" comment refers to eels, not krakens (mkroom.c:557-565)
- encumbrance does NOT gate the grab-drown path: being Burdened won't save you once grabbed
- strategy aligned with NetHackWiki Drowning, Giant eel, Amulet of magical breathing: range-kill sea monsters, magical breathing/Swimming/Amphibious as the only true grab-drown defenses (https://nethackwiki.com/wiki/Drowning, https://nethackwiki.com/wiki/Giant_eel, https://nethackwiki.com/wiki/Amulet_of_magical_breathing)
-->

オオウナギ、電気ウナギ、そしてクラーケンは、巻きつき攻撃によってプレイヤーを拘束してきます。捕まってしまうと、そのモンスターのターンが回ってくるたびに溺死の判定が発生します。この溺死チェックは **モンスターがいるマス**（ウナギやクラーケンにとっては常に水マス）を基準に判定されるため、プレイヤー自身が隣接する乾いた陸地に立っていても水中に引きずり込まれて溺死します。「水泳（Swimming）」、「[呼吸の魔除け（無呼吸）](#movement-and-spatial-behavior)」、あるいは「両生形態」だけがこの引きずり込み溺死を完全に防ぐことができます。ここでは所持品の負荷重量は関係ありません（負荷が問題になるのは水に *落下* して自力で這い上がろうとする時であり、「圧迫（Stressed）」以上の負荷では緊急脱衣を強いられます）。ウナギやクラーケンとは、メデューサの階層、城を取り囲む堀、沼地の部屋、そして水の大系で遭遇することになります。

**防御策：** **呼吸の魔除け (amulet of magical breathing)**（または同名の呪文）を身につければ「無呼吸」となり、引きずり込みによる溺死の脅威を完全に無力化できます。「浮遊」は水たまりや堀の上を歩いて侵入するのを防いでくれますが、**ウナギに巻きつかれた場合の溺死は防げない** 点に注意してください。海洋モンスターとは可能な限り遠距離から交戦して撃破してください。奴らの巻きつき攻撃は隣接しなければ発動しません。
