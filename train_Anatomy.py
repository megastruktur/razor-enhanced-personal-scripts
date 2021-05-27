
target = Target.PromptTarget("Select Mob")

def TrainAnatomy(target):
    Player.UseSkill("Anatomy")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(target)
    Misc.Pause(1000)
    
while Player.GetRealSkillValue("Anatomy") < 100:
    TrainAnatomy(target)