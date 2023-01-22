theTarget = Target.PromptTarget("Select your target")
    
while Player.GetRealSkillValue('Mysticism') < Player.GetSkillCap('Mysticism'):
    if Player.GetSkillValue('Mysticism') < 33:
        Spells.CastMysticism('Nether Bolt')
        Target.WaitForTarget(8000, False)
        Target.TargetExecute(theTarget)
        Misc.Pause(2000)
    elif Player.GetSkillValue('Mysticism') >= 33 and Player.GetSkillValue('Mysticism') < 62:
        Spells.CastMysticism('Stone Form')
        Misc.Pause(5000)
    elif Player.GetSkillValue('Mysticism') >= 62 and Player.GetSkillValue('Mysticism') < 80:
        Spells.CastMysticism('Cleansing Winds')
        Target.WaitForTarget(8000, False)
        Target.Self()
        Misc.Pause(2000)
    elif Player.GetSkillValue('Mysticism') >= 80 and Player.GetSkillValue('Mysticism') < 95:
        Spells.CastMysticism('Spell Plague')
        Target.WaitForTarget(8000, False)
        Target.TargetExecute(theTarget)
        Misc.Pause(2000)
    elif Player.GetSkillValue('Mysticism') >= 95:
        Spells.CastMysticism('Nether Cyclone')
        Target.WaitForTarget(8000, False)
        Target.Self()
        Misc.Pause(2000)
        
        
        
        
        
