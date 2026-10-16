### アーティファクト (Artifacts) {#artifacts}

<!-- audit
2026-07-30 accuracy pass vs NetHack-5.0 source:
- Stormbringer is SPFX_INTEL: cross-alignment touch deals 4d10, not 4d4. (artilist.h:93-96 Stormbringer has SPFX_INTEL; artifact.c:953 `dmg = d((Antimagic ? 2 : 4), (self_willed ? 10 : 4))`)
- Grimtooth +d6 damage bonus applies to ALL targets, not just elves (artifact.c:1099-1102).
- Mitre of Holiness gives NO damage bonus vs undead; ATTK is NO_ATTK (artifact.c:1095-1098).
- M2_UNDEAD flag only enables shade_glare on weapons, not worn helms (artifact.c:554-571).
- Eye of the Aethiopica magic resistance requires worn, NOT carried (artilist.h:303-305, NO_CARY).
- Eye of the Aethiopica carry effects: energy regen, half spell damage (cspfx EREGEN, HSPDAM).
- strategy aligned with NetHackWiki Artifact weapon, Grayswandir, Magicbane, Mjollnir: Grayswandir/Magicbane/Mjollnir as the top wish artifacts; alignment-mismatched artifacts blast on touch (https://nethackwiki.com/wiki/Artifact_weapon, https://nethackwiki.com/wiki/Grayswandir, https://nethackwiki.com/wiki/Magicbane, https://nethackwiki.com/wiki/Mjollnir)
-->

迷宮の各地には、伝説に彩られた至宝が散らばっています：通常の装備では到底及ばない超絶な力を宿した、固有の名を持つ武器、魔除け、そして道具たちです。各アーティファクトは1回のゲームにつき世界に1つしか存在しません。それらを入手する手段は以下の通りです：

- **泉に剣を浸す**（秩序属性のキャラクターによるエクスカリバー）。
- **祭壇での生贄奉納**（自属性の神からギフトとして授けられる）。
- **クエストの完遂**（各職業固有のクエストアーティファクト）。
- **願い**（大半のアーティファクトは願うことができますが、自身の属性と一致しない場合は拒絶されることがあります）。
- **ランダム生成**（稀ですが、武器がアーティファクトとして自然生成される微小な確率があります）。
- **命名**（スティングおよびオークリストのみ。後述参照）。
