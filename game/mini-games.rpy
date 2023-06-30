init python:
    def CanonTransform(t, st, at):
        pass

transform half_size:
    zoom 0.5
    
screen scene_1:
    image "mod_assets/minigames/backdrop.png" at half_size
    imagebutton idle Solid("FFFFFF00") hover "mod_assets/minigames/sghover.jpg" align (0.7, 0.3) at half_size action Show("shooting_gallery")


label start:
    $ canon_image = Image ("mod_assets/minigames/canon.png")
    $ canon_size = (330 / 2, 384 / 2)
    $ canon_pos = (0, 0)
    $ canon_opos = (renpy.get_physical_size()[0] / 2 - canon_size[0] / 2, renpy.get_physical_size()[1] - canon_size[1] + 60)
    $ canon_transform = Transform(child - canon_image, zoom = 0.5, pos = (canon_opos[0], canon_opos[1]), function = CanonTransform)
    return