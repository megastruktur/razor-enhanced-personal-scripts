from Scripts.utilities.colors import colors

def AgroMob():
    
    while True:
        mob = Target.GetTargetFromList('nearest_mob')
        Player.Attack(mob)
        Misc.Pause(100)
    
AgroMob()