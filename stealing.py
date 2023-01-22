theTarget = Target.PromptTarget("Select your Stealing Item")
while Player.GetSkillValue('Stealing') < Player.GetSkillCap('Stealing'):  
    Items.UseItem(theTarget)
    Misc.Pause(1000)
