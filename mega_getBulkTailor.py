#Misc.Inspect()
import re

# Colors
red = 0xd0312d


# Bulk Vendor abstract Class
class BulkVendor:
  serial = None
  speciality = None
  
  def __init__ (self, serial, speciality):
    self.serial = serial
    self.speciality = speciality


# Bulk Order Vendors
bulkVendors = {
    'tailor': BulkVendor(
      serial = 0x00002044,
      speciality = 'tailor'
    ),
    'blacksmith': BulkVendor(
      serial = 0x00001967,
      speciality = 'blacksmith'
    ),
}

#tailorSerial = 0x00002044
#blacksmithSerial = 0x00001967

def getBulkOrderContext(vendorSerial):
    bulkVendor = Mobiles.FindBySerial(vendorSerial)
    #Mobiles.UseMobile(bulkVendor)
    Mobiles.Message(bulkVendor,0x000000,'Hello there!')
    Misc.WaitForContext(bulkVendor, 1000)
    Misc.ContextReply(bulkVendor, 1)
    
    # Wait for Gump
    
    # If no Gump - get Wait Time
    minutesToWait = getMinutesToWait(vendorSerial)


# Returns the amount of minutes to wait until Bulk Order
def getMinutesToWait(vendorSerial):
    
    Misc.Pause(1000)
    text = Journal.GetTextBySerial(tailorSerial)
    
    latestSay = text[len(text) - 1]
    minutes = re.findall(r'\d+', latestSay)[0]

    Misc.SendMessage("Need to wait {} minutes".format(minutes), red)
    
    return minutes
    

def getToVendor(serial):
    bulkVendor = Mobiles.FindBySerial(serial)
    path = PathFinding.GetPath(bulkVendor.Position.X, bulkVendor.Position.Y, 0)
    PathFinding.RunPath(path,10,0,1)

def getBulk(vendor):
    getToVendor(vendor.serial)
    getBulkOrderContext(vendor.serial)

# Start the program
for name, vendor in bulkVendors.items():
    getBulk(vendor)
    
    
#Misc.Inspect()