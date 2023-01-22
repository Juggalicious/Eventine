while Player.GetSkillValue('Ninjitsu') < 87.5:
    if Player.Mana >= 15:
        preJumpY = Player.Position.Y
        Spells.CastNinjitsu("Shadowjump")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(Player.Position.X, (Player.Position.Y + 2) ,Player.Position.Z)
        Misc.Pause(3000)
        if preJumpY != Player.Position.Y:
            if Player.Visible == True:
                Player.UseSkill('Hiding')
                Misc.Pause(500)
            Player.Walk("North")
            Misc.Pause(200)
            Player.Walk("North")
            Misc.Pause(200)
            Player.Walk("North")
            Misc.Pause(200)