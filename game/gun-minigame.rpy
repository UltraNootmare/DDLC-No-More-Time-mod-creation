init python:
    def CorkGunTrans(t, st, at):
        pass

transform half_size:
    zoom 0.5

screen gun_minigame:
    image "mod_assets/minigame_assets/foreground.png"
    image "mod_assets/minigame_assets/background.png"

label gun_start:
    ## Cork Gun Init ##

    $ cg_image = Image("mod_assets/minigame_assets/gun.png")
    $ cg_size = (330 / 2, 384 / 2)
    $ cg_start_pos = (0, 0)
    $ cg_pos = (renpy.get_physical_size()[0] / 2 - cg_size[0] / 2, renpy.get_physical_size()[1] - cg_size[1] + 60)
    $ cg_transform = Transform(child=cg_image, zoom=0.5, pos=(cg_start_pos[0], cg_start_pos[1]))

    