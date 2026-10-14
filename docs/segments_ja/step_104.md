### 仲間作り (Making Friends)

<!-- audit
2026-06-03:
- tameness score: 0 to 20; initialized to rn1(4, 5) for tamed, 20 for starting pet (dog.c:50, makemon.c:1347-1355)
- decay: 1 per 20 turns left behind on another level; 1 per struck turn by hero; starvation triggers M2_PEACEFUL/M2_HOSTILE drop (dogmove.c:28-85)
- chat sounds by hunger state: dog yip/bark/whine, cat purr/mew/meow, horse whicker/whinny/neigh (sounds.c:451-512)
- feeding restores hunger AND tameness; tripe is preferred dog/cat food, fruit/veggie for horse (eat.c, dog.c)
- charm monster / scroll of taming: 3x3 radius baseline; confused scroll 11x11 (read.c:1680-1704, spell.c:2201)
- untamable categories: humans (@), covetous (Wizard, liches, masters), demons (unless player is demon), vault guards, quest leaders/nemeses, minions, uniques (mondata.c:421-460)
- apport: edog->apport initialized to A_CHA (dog.c:60), grows as the pet eats food you drop near you, drives pickup/return behavior (dogmove.c:316-422); enables pet-shoplifting in practice
- magic whistle teleports pets toward the hero on every apply (apply.c whistle handler)
- gray dragon resists magic damage via resists_magm (mondata.c:215-225 includes AD_MAGM and PM_BABY_GRAY_DRAGON); magic-resistant targets cannot be polymorphed
- long worm's lengthening tail occupies a chain of map tiles (worm.c:27-100); the head moves but segments stay until they shrink
-->

恐るべき迷宮は暗く、過酷で、あなたを捕食しようと狙う危険な生物に満ち溢れています。そうした過酷な環境において、忠実な仲間は金貨の詰まった袋などよりも遥かに価値があります。幸いなことに、ダンジョンはそのための手段を用意してくれています。
