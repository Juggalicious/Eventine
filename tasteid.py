theTarget = Target.PromptTarget("Select your Taste target")

while Player.GetSkillValue('Taste ID') < Player.GetSkillCap('Taste ID'):  
    Player.UseSkill("Taste ID")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(theTarget)
    Misc.Pause(1000)