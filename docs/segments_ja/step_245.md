#### 武器なし (Weaponless)

<!-- audit
2026-05-19:
- weaphit++ requires weapon non-NULL AND (WEAPON_CLASS OR is_weptool) (uhitm.c:616-617)
- weapon-tools that break: pick-axe, unicorn horn, other is_weptool items
- wielded polearm at range via #apply DOES break (HMON_APPLIED, dothrow.c:2199-2203)
- do NOT break: thrown weapons, fired ammo, wands, spells, barehand, martial arts, cockatrice-corpse-wield
- iron chain is CHAIN_CLASS, not a weptool; swinging it does NOT break (objects.h:101, 1631)
- aklys is WEAPON_CLASS, not a weptool; it breaks via the WEAPON_CLASS branch (objects.h:381-383)
- strategy aligned with NetHackWiki Weaponless, Martial arts: thrown/fired weapons and martial arts preserve the conduct, wielded-polearm-#apply still breaks it (https://nethackwiki.com/wiki/Weaponless, https://nethackwiki.com/wiki/Martial_arts)
-->

構えている武器や武器道具で敵を殴ってはいけません。武器を投げる、弓やクロスボウから射出する、杖や呪文を行使することは許されます。また、素手格闘や武術（Martial Arts）で殴り倒すことも完全に合法です（武闘家が圧倒的な強さを誇ります）。禁じられているのは、剣、斧、メイス、アキリス、つるはし、ユニコーンの角など、武器クラスまたは武器道具に分類されるアイテムを手に持った状態で敵を直接殴打することです。なお、長柄武器を構えて離れた位置から `a`（使用）でリーチ攻撃する行為もコンダクト違反となります。

これは一見するほど過酷な制約ではありません。武闘家は強力無比な武術で開始し、さらに成長します。他の職業であっても、呪文、杖、投擲短剣に頼ることができます。また、コカトリスの死体を素手（小手着用）で掴んで殴りつける行為も合法です（死体は武器ではないため）。最大の犠牲は、近接武器のアーティファクトが持つ圧倒的なダメージボーナスを諦めなければならない点にあります。

