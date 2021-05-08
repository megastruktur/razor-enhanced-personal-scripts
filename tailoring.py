# Train Necro
#def trainTailoring():
    
    #while Player.GetSkillValue('Tailoring') < 100.0:
        #Misc.Pause(20000)
            
        #trainTailoring()
        
# Scissors
#Items.UseItem(0x400A4C2A)
#Target.WaitForTarget(10000, False)
# Bolt of Clothes
#Target.TargetExecute(0x400A8AC8)

# Use Sewing Kit
#Items.UseItem(0x400A8AC9)
#Gumps.WaitForGump(2066278152, 10000)

# Get Item Details
#t = Target.PromptTarget('Select Kit')
#item = Items.FindBySerial(t)
#Player.HeadMessage(123123,t.Name)


craftToolType = 0xF9D # sewing kit
sewingGumpId = 2066278152
buttonId_Boots = 29
buttonId_FurBoots = 9
salvageBagId = 3702

def getItemDetails():
  t = Target.PromptTarget('Select Item')
  item = Items.FindBySerial(t)
  Player.HeadMessage(123123, str(item))

def tailoringTraining():
    

    sewingTool = getByItemID(craftToolType, Player.Backpack.Serial)
    
    Items.UseItem(sewingTool)
    Gumps.WaitForGump(sewingGumpId, 10000)

    #Gumps.SendAction(sewingGumpId, buttonId_Boots)
    #Gumps.WaitForGump(sewingGumpId, 10000)

    # Craft Fur Boots
    #Gumps.SendAction(sewing_gump_id, buttonId_FurBoots)

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()

def countByItemID(itemid):
    # Count the number of items found in backpack by the ItemID
    count = 0
    for item in Player.Backpack.Contains:
        if item.ItemID == itemid:
            count = count + 1
        else:
            Misc.NoOperation()
    Misc.SendMessage('%i items found' % (count))
    return count
    
#tailoringTraining()
#getItemDetails()
salvageBag = getByItemID(salvageBagId, Player.Backpack.Serial)
Items.UseItem(salvageBag)
