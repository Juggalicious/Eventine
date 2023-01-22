while Player.GetRealSkillValue('Magery') < Player.GetSkillCap('Magery'):
    if Player.GetSkillValue('Magery') >= 0 and Player.GetSkillValue('Magery') < 45:
        Spells.CastMagery('Bless')
        Target.WaitForTarget(10000,False)
        Target.Self()
    elif Player.GetSkillValue('Magery') >= 45 and Player.GetSkillValue('Magery') < 55:
        Spells.CastMagery('Greater Heal')
        Target.WaitForTarget(10000,False)
        Target.Self()
    elif Player.GetSkillValue('Magery') >= 55 and Player.GetSkillValue('Magery') < 65:
        Spells.CastMagery('Paralyze')
        Target.WaitForTarget(4000,False)
        Target.Self()
        Misc.Pause(2000)
    elif Player.GetSkillValue('Magery') >= 65 and Player.GetSkillValue('Magery') < 75:
        Spells.CastMagery('Invisibility')
        Target.WaitForTarget(4000,False)
        Target.Self()
    elif Player.GetSkillValue('Magery') >= 75 and Player.GetSkillValue('Magery') < 90:
        Spells.CastMagery('Mass Dispel')
        Target.WaitForTarget(4000,False)
        Target.Self()
    elif Player.GetSkillValue('Magery') >= 90 and Player.GetSkillValue('Magery') < 120:
        Spells.CastMagery('Earthquake')
        Misc.Pause(2000)
    Misc.Pause(3000)