init python:
    def CorkGunTrans(t, st, at):
        pass

transform half_size:
    zoom 0.5

transform spotlights:
    zoom 0.5
    blend "add"
    alpha 0.5

screen gun_minigame:
    image "mod_assets/minigame_assets/foreground.png" at half_size
    image "mod_assets/minigame_assets/background.png" at half_size
    image "mod_assets/minigame_assets/spotlights.png" at spotlights
    add cg_trans
    image "mod_assets/minigame_assets/score-bg.png" pos (10, 0) at half_size

label gun_start:

    stop music
    stop audio

    $ cg_image = Image("mod_assets/minigame_assets/gun.png")
    $ cg_size = (330 / 2, 384 / 2)
    $ cg_start_pos = (0, 0)
    $ cg_pos = (renpy.get_physical_size()[0] / 2 - cg_size[0] / 2, renpy.get_physical_size()[1] - cg_size[1] + 60)
    $ cg_trans = Transform(child=cg_image, zoom=0.5, pos=(cg_start_pos[0], cg_start_pos[1]))

    call screen gun_minigame