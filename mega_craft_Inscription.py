#Misc.Inspect()

from Scripts.utilities.colors import colors

inscriptionToolType = 0x0FBF
inscriptionGump = 2066278152
gump_CraftLast = 4
gump_LastTen = 28
manaStartRegen = 45

def TrainInscription():

    while Player.GetSkillValue("Inscription") < 100:

        if Player.Hits * 100 / Player.HitsMax < 30:
            Player.UseSkill( 'Spirit Speak' )
            Misc.Pause(2000)
    
        inscriptionTool = getByItemID(inscriptionToolType, Player.Backpack.Serial)
        Items.UseItem(inscriptionTool)
        Misc.Pause(1000)
        
        Gumps.WaitForGump(inscriptionGump, 10000)
        Gumps.SendAction(inscriptionGump, gump_LastTen)
        Misc.Pause(500)
        Gumps.WaitForGump(inscriptionGump, 10000)
        Gumps.SendAction(inscriptionGump, gump_CraftLast)
        
        Misc.Pause(2500)
        

        if Player.Mana < manaStartRegen:
            Misc.SendMessage("Waiting for mana to regenerate...", colors['yellow'])
            Player.UseSkill("Meditation")
            while Player.Mana * 100/Player.ManaMax < 80:
                Misc.Pause(1000)
        else:
            Gumps.WaitForGump(inscriptionGump, 10000)

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
            
TrainInscription()
