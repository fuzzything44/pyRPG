import spells.fireball
import spells.first_aid
import spells.frostshot
import spells.heal
import spells.knockback
import spells.lifesteal
import spells.luckboost
import spells.spell

# Level at which a spell is gained
spell_gain_levels = [2, 5]

warrior_spells  = [\
    spell.spell(first_aid.manaCost, first_aid.FirstAid, first_aid.name, first_aid.icon),    # Level 2 spell, regeneration.
    spell.spell(knockback.manaCost, knockback.knockback, knockback.name, knockback.icon)    # Level 5 spell, AOE knockback
  ]

mage_spells     = [\
    spell.spell(fireball.manaCost, fireball.fireball, fireball.name, fireball.icon),        # Level 2 spell, big damage + DOT
    spell.spell(frostshot.manaCost, frostshot.frostshot, frostshot.name, frostshot.icon)    # Level 5 spell, damage + freeze
  ]

thief_spells    = [\
    spell.spell(lifesteal.manaCost, lifesteal.lifesteal, lifesteal.name, lifesteal.icon),   # Level 2 spell. Damage + heal, no aim.
    spell.spell(luckboost.manaCost, luckboost.luckboost, luckboost.name, luckboost.icon)    # Level 5 spell. +luck buff.
  ]

