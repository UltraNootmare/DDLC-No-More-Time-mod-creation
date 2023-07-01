init python:
    def cork-gunTransform(t, st, at):
        pass

transform half_size:
    zoom 0.5
    
screen scene_1:

screen shooting_gallery:
    image "mod_assets/minigames/backdrop.png" at half_size
    add cork-gun_transform 



label start:
    $ cork-gun_image = Image ("mod_assets/minigames/cork-gun.png")
    $ cork-gun_size = (330 / 2, 384 / 2)
    $ cork-gun_pos = (0, 0)
    $ cork-gun_opos = (renpy.get_physical_size()[0] / 2 - cork-gun_size[0] / 2, renpy.get_physical_size()[1] - cork-gun_size[1] + 60)
    $ cork-gun_transform = Transform(child - cork-gun_image, zoom = 0.5, pos = (cork-gun_opos[0], cork-gun_opos[1]), function = cork-gunTransform)
    return