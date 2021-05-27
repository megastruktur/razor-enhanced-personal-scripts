path = "Data/Plugins/Razor-Enhanced-0.7.7.19/Scripts/demofile2.txt"

bulkOrderBookGumpId = 1036400804
bulkOrderBookNextPage = 3

# Is it material or not.
materials = ["Spined", "Horned", "Barbed", "Leather", "Cloth", "Iron", "Agapite", "Verite", "Valorite", "Gold"]
def isMaterial(material_name):
    return material_name in materials

    
    
    
# Get BOD content
def getSmallBODContent(bulk_type_line_number):
    
    global bulks_amount
    bulks_amount += 1
    
    ### CANT GET GLOBAL?!!
    price_all_line = FindPriceAllLine(lines)
    
    name = lines[bulk_type_line_number + 1]
    quality = lines[bulk_type_line_number + 2]
    
    # price_all_line NOT GLOBAL!
    material = ""
    if isMaterial(lines[bulk_type_line_number + 3]):
        material = lines[bulk_type_line_number + 3]
    
    done_todo = lines[bulks_amount + price_all_line]
    Misc.SendMessage("----- DONE TODO LINE: " + str(bulks_amount + price_all_line + 1), 1100)
    Misc.SendMessage("----- DONE TODO: " + str(done_todo), 1100)
    
    done, todo = lines[bulks_amount + price_all_line + 2].split(' / ')
    
    return BulkOrderDeedSmall(name, quality, material, done, todo)
    
    
    
    
# Get Large Bulk content
def getLargeBulkContent(bulk_type_line_number):
    
    # We need to add to counter as there is Separate Price for a large Bulk
    global bulks_amount
    bulks_amount += 1
    
    global price_all_line
    b = BulkOrderDeedLarge()
    
    step = 2
    
    # If 3-rd field is material - skip 3.
    if isMaterial(lines[bulk_type_line_number + 1]):
        step = 3
    
    for i in range(bulk_type_line_number + 1, lines_amount, step):
        
        # Proceed with other Bulks if a new one if found.
        if lines[i] == "Large" or lines[i] == "Small" or "Price all" in lines[i]:
            break
        b.content.append(getSmallBODContent(i-1))
        
    return b

##### Class for Bulk Order    
class BulkOrderDeed(object):
    
    type = "" # Small or Large

## Large BOD
class BulkOrderDeedLarge(BulkOrderDeed):
    
    content = [] # if Large - array of BODs
    
    def __init__(self):
        self.type = "Large"
        self.content = []
        
## Small BOD
class BulkOrderDeedSmall(BulkOrderDeed):
    
    name = ""
    quality = ""
    items_todo = 0
    items_done = 0
    material = ""
    
    def __init__(self, name, quality, material = "", done = 0, todo = 0):
        self.type = "Small"
        self.name = name
        self.quality = quality
        self.items_todo = todo
        self.items_done = done
        self.material = material
        

##### Main Parser
def Parse():
    
    global bulks
    global lines
    global lines_amount
    global price_all_line
    global bulks_amount
    
    bulks = []
    lines = Gumps.LastGumpGetLineList()
    lines_amount = len(lines)
    price_all_line = FindPriceAllLine(lines)
    bulks_amount = 0
    
    # A line with Price all. Separator.
    price_all_line = 0

    for line in range(lines_amount):
        
        if lines[line] == "Small":
            # we take line with type
            bulks.append(getSmallBODContent(line))
            
        elif lines[line] == "Large":
            # Add current big bulk to array.
            bulks.append(getLargeBulkContent(line))
            
        # Cancel iteration if Price All.
        elif "Price all" in lines[line]:
            price_all_line = line
            break
    
    # Verify parsed Bulks and add done-todo amounts
    for bulk in bulks:
       
        Misc.SendMessage("-----------", 52)
        
        if bulk.type == "Large":
            for sb in bulk.content:
                
                Misc.SendMessage("Bulk Name: " + sb.name)
                Misc.SendMessage("Bulk Quality: " + sb.quality)
        else:
            
            Misc.SendMessage("Bulk Name: " + bulk.name)
            Misc.SendMessage("Bulk Quality: " + bulk.quality)
            Misc.SendMessage("Bulk Quality: " + bulk.material)
            Misc.SendMessage("Bulk Done: " + bulk.done)
            Misc.SendMessage("Bulk Todo: " + bulk.todo)
         
# Get line number of a separator.
def FindPriceAllLine(lines):
    for line in range(len(lines)):
        if "Price all" in lines[line]:
            return line
        
##### Main Parser
def LinePrinter():
    
    bulks = []
    lines = Gumps.LastGumpGetLineList()
    lines_amount = len(lines)

    for line in range(lines_amount):
       Misc.SendMessage(str(line) + ": " + lines[line])
       

#Gumps.WaitForGump(bulkOrderBookGumpId, 10000)
#Gumps.SendAction(1036400804, 3)
 
LinePrinter()
Parse()