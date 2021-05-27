from Scripts.utilities.colors import colors
from Scripts.organizer_restock_reagents import RestockReagent

tool_id = 0x0E9B
alchemy_gump = 2066278152

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
    return False
            
def AlchemyLast():
    
    while True:
        tool = getByItemID(tool_id, Player.Backpack.Serial)
        
        if tool != False:
            Items.UseItem(tool)
            Misc.Pause(1000)
            Gumps.WaitForGump(alchemy_gump, 10000)
            Gumps.SendAction(alchemy_gump, 4)
            Misc.Pause(1000)
        else:
            Misc.SendMessage("No tools found. Script ended.", colors['red'])
            break
    
AlchemyLast()
    