while Player.GetSkillValue('Ninjitsu') < 55:
    if Player.Mana >= 10 and Player.Followers < 5:
        Spells.CastNinjitsu('Mirror Image')
        Misc.Pause(4000)