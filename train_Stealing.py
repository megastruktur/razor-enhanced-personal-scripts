'''
1. Rent a pack horse or a pack lama
2. Go to Felucca (e.g. Buckanner's Den)
3. Put Empty Bottles or Ingots or etc into the pack horse's inventory
4. Start the script.

The skill becomes harder to upgrade after 98+ so I replaced Ingots with Dyeing Tube.
'''

import Misc, Player, Items, Target, Mobiles
from Scripts.utilities.colors import colors

# Select the Targets
pack_horse_mobile_serial = Target.PromptTarget('Select the pack horse')
pack_horse_mobile = Mobiles.FindBySerial(pack_horse_mobile_serial)

_item_to_steal_serial = Target.PromptTarget('Select the item to steal inside container')
item_to_steal = Items.FindBySerial(_item_to_steal_serial)

# Get the item type to search through the backpack.
item_to_steal_ID = item_to_steal.ItemID

# Get Item by its ID.
def _getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
    Misc.SendMessage("Not Found!", colors['red'])

def TrainStealing():
    
    while Player.GetRealSkillValue('Stealing') < 100:
    
        Mobiles.UseMobile(pack_horse_mobile_serial)
        
        # What to steal
        stealableAtHorse = _getByItemID(item_to_steal_ID, pack_horse_mobile.Backpack.Serial)
        
        # Pack horse can untame so use this to update it's loyalty.
        Player.ChatSay(colors['red'], "all guard me")
        
        Player.UseSkill("Stealing")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(stealableAtHorse.Serial)
        
        Misc.Pause(1000)
        # What to move Back
        stealableAtBackpack = _getByItemID(item_to_steal_ID, Player.Backpack.Serial)
        if stealableAtBackpack:
            Items.Move(stealableAtBackpack.Serial, pack_horse_mobile_serial, 0)
            Misc.SendMessage("Moving items back to " + pack_horse_mobile.Name, colors['green'])
        
        Misc.Pause(9000)
    
    
TrainStealing()

