wodTarget = Target.PromptTarget("Select Word of Death Target")
    
while Player.GetRealSkillValue('Spell Weaving') < Player.GetSkillCap('Spell Weaving'):  
    if Player.GetSkillValue('Spell Weaving') < 33:
        Spells.CastSpellweaving("Immolating Weapon")
        Misc.Pause(3000)
    elif Player.GetSkillValue('Spell Weaving') >= 33 and Player.GetSkillValue('Spell Weaving') < 60:
        Spells.CastSpellweaving("Reaper Form")
        Misc.Pause(4000)
    elif Player.GetSkillValue('Spell Weaving') >= 60 and Player.GetSkillValue('Spell Weaving') < 83:
        Spells.CastSpellweaving("Essence Of Wind")
        Misc.Pause(3000)
    elif Player.GetSkillValue('Spell Weaving') >= 83 and Player.GetSkillValue('Spell Weaving') < 120:
        Spells.CastSpellweaving("Word Of Death")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(wodTarget)
        Misc.Pause(2000)
    if Player.GetSkillValue('Meditation') > 60:
        if Player.Mana < 30:
            Player.UseSkill('Meditation')
            Misc.Pause(15000)
    if Player.Hits < Player.HitsMax:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(2000)






