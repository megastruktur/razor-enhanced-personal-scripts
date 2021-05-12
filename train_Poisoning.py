from Scripts.utilities.colors import colors

poison_flask_ids = {
    'lesser': 0x0F0A,
    'default': 0x0F0A
}

# Prompt and get Target Weapon serial.
def getTargetWeapon():
    
    targetWeaponSerial = 'targetWeaponSerial'
    if not Misc.CheckSharedValue( targetWeaponSerial ):
        targetWeapon = Target.PromptTarget( 'Select target weapon' )
        Misc.SetSharedValue( targetWeaponSerial, targetWeapon )

    return Misc.ReadSharedValue( targetWeaponSerial )
    


def trainPoisoning():
    
    weapon = getTargetWeapon()
    
    while Player.GetSkillValue('Poisoning') <= 100:
        Player.UseSkill("Poisoning")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(getFlaskTypeSerial())
    
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(weapon)
        
        
        while Player.Poisoned == True:
            Misc.SendMessage( 'I am Poisoned! Trying to cure.', colors['red'] )
            Spells.CastMagery( 'Cure' )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( Player.Serial )
        
        Misc.Pause(10000)
    
# Get flask type depending on skill value.
def getFlaskTypeSerial():
    
    if Player.GetSkillValue('Poisoning') <= 40:
        type = 'lesser'
    else:
        type = 'default'
    
    return getByItemID(poison_flask_ids[type], Player.Backpack.Serial)

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
    
trainPoisoning()

