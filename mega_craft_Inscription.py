#Misc.Inspect()

inscriptionToolType = 0x0FBF
inscriptionGump = 2066278152

def TrainInscription():
    

    while Player.GetSkillValue("Inscription") < 100:

        inscriptionTool = getByItemID(inscriptionToolType, Player.Backpack.Serial)
        Items.UseItem(inscriptionTool)
        Misc.Pause(500)
        Gumps.WaitForGump(inscriptionGump, 10000)
        Gumps.SendAction(inscriptionGump, 4)
        
        Misc.Pause(2000)
        

        if Player.Mana < 35:
            Misc.SendMessage("Waiting for mana to regenerate...")
            Player.UseSkill("Meditation")
            while Player.Mana < 130:
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