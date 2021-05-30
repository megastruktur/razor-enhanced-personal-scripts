# Cures and Heals to max

from Scripts.utilities.colors import colors

def CureHeal():
    
    mobileTargetSerial = Target.PromptTarget('Select Your Target')
    mobileTarget = Mobiles.FindBySerial(mobileTargetSerial)
    
    while mobileTarget.Hits < mobileTarget.HitsMax or mobileTarget.Poisoned:
        
        # Fast Cure
        if mobileTarget.Poisoned:
            Spells.Cast("Cure")
            
        else:
            # Lower 40% - use Greater Heal
            if (float(mobileTarget.Hits) / float(mobileTarget.HitsMax)) < 0.4:
                Spells.Cast("Greater Heal")
            else:
                Spells.Cast("Heal")
                
         
        Target.WaitForTarget(1500)
        Target.TargetExecute(mobileTarget)
        
    Misc.SendMessage('Max HP, bro', colors['green'])
        
CureHeal()