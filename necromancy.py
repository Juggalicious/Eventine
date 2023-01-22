while Player.GetSkillValue('Necromancy') < Player.GetSkillCap('Necromancy'):
    if Player.GetSkillValue('Necromancy') >= 0 and Player.GetSkillValue('Necromancy') < 20:
        Spells.CastNecro('Curse Weapon')
    elif Player.GetSkillValue('Necromancy') >= 20 and Player.GetSkillValue('Necromancy') < 50:
        Spells.CastNecro('Wraith Form')
    elif Player.GetSkillValue('Necromancy') >= 50 and Player.GetSkillValue('Necromancy') < 70:
        Spells.CastNecro('Horrific Beast')
    elif Player.GetSkillValue('Necromancy') >= 70 and Player.GetSkillValue('Necromancy') < 80:
        Spells.CastNecro('Wither')
    elif Player.GetSkillValue('Necromancy') >= 80 and Player.GetSkillValue('Necromancy') < 100:
        Spells.CastNecro('Lich Form')
    elif Player.GetSkillValue('Necromancy') >= 100 and Player.GetSkillValue('Necromancy') < 1200:
        Spells.CastNecro('Vampiric Embrace')
    Misc.Pause(4000)