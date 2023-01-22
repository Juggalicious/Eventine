while Player.GetRealSkillValue('Tracking') < Player.GetSkillCap('Tracking'):
    Player.UseSkill("Tracking")
    Gumps.WaitForGump(2976808305, 10000)
    Gumps.SendAction(2976808305, 3)
    Gumps.WaitForGump(993494147, 10000)
    Gumps.SendAction(993494147, 0)
    Misc.Pause(5000)
    Gumps.SendAction(993494147, 0)
    Misc.Pause(5000)