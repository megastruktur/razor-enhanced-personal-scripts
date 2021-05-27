from Scripts.utilities.colors import colors

def TrainSpellweaving():

    while Player.GetSkillValue("Spellweaving") < 100:

        ManaRegen()
    
        if Player.GetSkillValue("Spellweaving") < 35:
            Spells.CastSpellweaving("Immolating Weapon")
            Misc.Pause(700)
            
        elif Player.GetSkillValue("Spellweaving") >= 35 and Player.GetSkillValue("Spellweaving") < 48:
            Spells.CastSpellweaving("Reaper Form")
            Misc.Pause(2500)

      
# Manaregen      
def ManaRegen():
    
    manaStartRegen = 22
    if Player.Mana < manaStartRegen:
        Misc.SendMessage("Waiting for mana to regenerate...", colors['yellow'])
        Player.UseSkill("Meditation")
        while Player.Mana * 100/Player.ManaMax < 80:
            Misc.Pause(1000)
    
TrainSpellweaving()
