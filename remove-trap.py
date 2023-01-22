theTarget = Target.PromptTarget("Select your trap box")
while Player.GetRealSkillValue('Remove Trap') < Player.GetSkillCap('Remove Trap'):
    Items.UseItem(theTarget)
    Misc.Pause(1500)
    Player.UseSkill("Remove Trap")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(theTarget)
    Misc.Pause(12000)
