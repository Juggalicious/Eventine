target = Target.PromptTarget("Select your target")
while Player.GetSkillValue('Animal Lore') < Player.GetSkillCap('Animal Lore') or Player.GetSkillValue('Animal Taming') < Player.GetSkillCap('Animal Taming'):
    Mobiles.UseMobile(target)
    Misc.WaitForContext(target, 10000)
    Misc.ContextReply(target, 0)
    Misc.Pause(14000)
