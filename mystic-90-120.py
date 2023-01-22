#requires you to be attacking something, and using the mysticism mastery
item = Target.PromptTarget("Select your training weapon")
self_pack = Player.Backpack.Serial
while True:
    Items.Move(item, self_pack, 0)
    Misc.Pause(2000)
    Player.EquipItem(item)
    Spells.CastMastery("Mystic Weapon")
    Misc.Pause(600000)