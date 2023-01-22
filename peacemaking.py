instrumentItemId = 0x0EB3 #Lutes
while Player.GetRealSkillValue('Peacemaking') < Player.GetSkillCap('Peacemaking') :
    Player.UseSkill("Peacemaking")
    Target.WaitForTarget(10000, False)
    if Journal.Search('hat instrument') == True:
        Journal.Clear()
        Target.TargetExecute(Items.FindByID (instrumentItemId,-1,Player.Backpack.Serial))
        Target.WaitForTarget(10000, False)
    Target.TargetExecute(Player.Serial)
    Misc.Pause(12000)