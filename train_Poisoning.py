from Scripts.utilities.colors import colors

path = "Data/Plugins/Razor-Enhanced-0.7.7.19/Scripts/poisoningSuccess.txt"
poison_flask_id = 0x0F0A
#kegSerial = 0x40065089

# Prompt and get Target Weapon serial.
def _getTargetWeapon():
    
    if not Misc.CheckSharedValue( 'targetWeaponSerial' ):
        targetWeapon = Target.PromptTarget( 'Select target weapon' )
        Misc.SetSharedValue( 'targetWeaponSerial', targetWeapon )

    return Misc.ReadSharedValue( 'targetWeaponSerial' )
    

def _setTargetKeg():
    
    targetKeg = Target.PromptTarget( 'Select target keg' )
    Misc.SetSharedValue( 'targetKegSerial', targetKeg )

    return Misc.ReadSharedValue( 'targetKegSerial' )
    
# The Main function
def trainPoisoning():
    
    # Save starting skill for Log purpose.
    skillStarted = Player.GetRealSkillValue('Poisoning')
    Misc.SendMessage('Starting with Poisoning: ' + str(skillStarted), colors['yellow'])
    
    weapon = _getTargetWeapon()
    stop = False
    bottleCounter = 0
    
    #_setTargetKeg()
    
    while Player.GetSkillValue('Poisoning') <= 100 and stop != True:
        
        #_GetFromKeg()
        
        poisonPotionSerial = _getByItemID(poison_flask_id, Player.Backpack.Serial)
        
        
        if poisonPotionSerial != False:
            
            bottleCounter += 1
            
            # ... and use poison
            Player.UseSkill("Poisoning")
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(poisonPotionSerial)
        
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(weapon)
            
            
            while Player.Poisoned == True:
                Misc.SendMessage( 'I am Poisoned! Trying to cure.', colors['red'] )
                Spells.CastMagery( 'Cure' )
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( Player.Serial )
            
            Misc.Pause(10000)
        else:
            Misc.SendMessage('No Potion found. Stopping.', colors['red'])
            stop = True

    # Write Log and Disconnect after the job is done.
    skillEnded = Player.GetRealSkillValue('Poisoning')
    _WriteSkillSuccess(skillStarted, skillEnded, bottleCounter)
    #Misc.Disconnect( )
    
# Get Potions from keg
def _GetFromKeg():
    Items.UseItem( Misc.ReadSharedValue( 'targetKegSerial' ) )
    Misc.Pause(1000)
    
# Write log to file.
def _WriteSkillSuccess(started, ended, potionsUsed):
    
    f = open(path, "a")
    textToWrite = "\nStarted: " + str(started) + ' | Ended: ' + str(ended) + ' | Progress: ' + str(ended - started) + ' | Potions used: ' + str(potionsUsed)
    f.write(textToWrite)
    f.close()
    
            
def _getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
    return False
    
trainPoisoning()
