#### 虐殺 (Genocide)
<!-- audit
2026-05-18:
- confused-uncursed scroll of genocide self-genocides your role's species (read.c:1737)
- PLAYER+REALLY branch in do_genocide kills you with killer = "genocidal confusion" (read.c:2838-2972)
- mndx = u.umonster = gu.urole.mnum (read.c:2839, u_init.c:991) — role species (PM_VALKYRIE etc.), not race
-->

混乱（Confused）した状態で呪われていない「虐殺の巻物」を読むと、自分自身の役職の種族を虐殺してしまい、即座にゲームオーバーとなります。巻物を読む前に、必ず自分の状態異常ステータスを確認してください。
