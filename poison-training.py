poison = Target.PromptTarget("Select your Poison Potions you want to use")
weapon = Target.PromptTarget("Select your weapon")

while Player.GetRealSkillValue("Poisoning") < Player.GetSkillCap("Poisoning"):
    Player.UseSkill("Poisoning")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(poison)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(weapon)
    Misc.Pause(10000)
    