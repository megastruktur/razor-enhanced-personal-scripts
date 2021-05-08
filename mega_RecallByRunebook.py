runebook_serial = 0x4002E606

#Misc.Inspect()

######
class RuneBookTeleport:
    
    runebook_serial = 0
    runebook_gump_id = 89
    search_rune = ""
    found_rune_number = 0
    runes_amount = 0
    
    start_action_recall = 49
    start_action_sacred_journey = 74
    start_action_gate = 99
    
    
    def __init__(self, runebook_serial, search_rune):
        self.runebook_serial = runebook_serial
        self.search_rune = search_rune.lower()
        self.getRunesAmount()
        self.getRuneNumberByName()
        
        if self.found_rune_number == 0:
            Misc.SendMessage("No rune found",0xff0000)
            Gumps.CloseGump(self.runebook_gump_id)
    
    # Get the amount of runes in book
    def getRunesAmount(self):

        Items.UseItem(self.runebook_serial)
        Gumps.WaitForGump(self.runebook_gump_id, 10000)
        data = Gumps.LastGumpGetLineList()
        data_length = len(data)
        if data_length > 21:
            self.runes_amount = (data_length - 85)/3
    
    # Get found rune number.      
    def getRuneNumberByName(self):
        
        first_line = 53 + 2 * self.runes_amount
        for i in range(self.runes_amount):
            #Gumps.LastGumpGetLine(i).lower()
            
            if self.search_rune == Gumps.LastGumpGetLine(first_line + i).lower():
                self.found_rune_number = i + 1
                break
        
    def recall(self):
        if self.found_rune_number != 0:
            Gumps.SendAction(89, self.start_action_recall + self.found_rune_number)


def recallByName():    
    all_text = Journal.GetTextBySerial(Player.Serial)
    rune_text = all_text[len(all_text) - 1]
    rbt = RuneBookTeleport(runebook_serial, rune_text)
    rbt.recall()
    
recallByName()