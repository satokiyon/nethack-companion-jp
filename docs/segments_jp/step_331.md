#### ノーム `G` (Gnomes `G`) {#gnomes-g}

<!-- audit
2026-05-19:
- All four S_GNOME entries match monsters.h:1681-1709.
- Gnomish wizard has one AT_MAGC/AD_SPEL attack, "cast spell" (monsters.h:1697), NOT two spell attacks.
- No "deep gnome" exists in 5.0 (correctly omitted).
- Gnome PCs (Archeologist default) see most S_GNOME as peaceful via MH_GNOME lovemask (makemon.c:2283).
-->

ノームのPCにとってはノームの鉱山の住人の大半が友好的です。ノームの君主は通常種よりも高い攻撃力を持ち、ノームの魔法使いは強力な魔法攻撃を放ってきます。どちらも侮ってはなりません。

::: dense-table

| モンスター名 | 色 | レベル | 速度 | AC | MR | 攻撃方法 | 備考 |
|---|---|---|---|---|---|---|---|
| ノーム (gnome) | 茶色 | 1 | 6 | 10 | 4 | 武器攻撃 1d6 |  |
| gnome lord | 青色 | 3 | 8 | 10 | 4 | 武器攻撃 1d8 |  |
| ノームの魔法使い (gnomish wizard) | 明青 | 3 | 10 | 4 | 10 | cast spell |  |
| gnome king | 赤紫 | 5 | 10 | 10 | 20 | 武器攻撃 2d6 |  |

:::
