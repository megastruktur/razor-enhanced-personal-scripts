from Scripts.utilities.colors import colors

skillname = "Magic Resist"
spells = dict()
'''
spells = {
    55: {
            "name": "Clumsy",
            "timeout": 1000
        },
    65: {
            "name": "Mana Drain",
            "timeout": 5000
        },
    100: {
            "name": "Mana Vampire",
            "timeout": 5000
        },
}
'''
spells[55] = {
            "name": "Clumsy",
            "timeout": 1000
        }
spells[65] = {
            "name": "Mana Drain",
            "timeout": 5000
        }
spells[100] = {
            "name": "Mana Vampire",
            "timeout": 5000
        }

def TrainResistingSpells():
    
    while Player.GetSkillValue(skillname) < 100:
    
        '''
        for skill_value in spells:
            Misc.SendMessage(skill_value)
            if Player.GetSkillValue(skillname) > skill_value:
                continue
            else:
                pause = spells[skill_value]["timeout"]
                Spells.CastMagery(spells[skill_value]["name"])
                break
        '''
                
        Spells.CastMagery("Clumsy")
        Target.WaitForTarget(10000, False)
        Target.Self()
        pause = 1000
        Misc.Pause(pause)
        
                        
TrainResistingSpells()
