init python:
    def UpdateGun(t, st, at):
        global cgStartPos
        global cgPos

        mousePos = renpy.get_mouse_pos()

        if mousePos[0] - cgSize[0] / 2 <= renpy.get_physical_size()[0] - cgSize[0] and mousePos[0] >= cgSize[0] / 2:
            cgPos = (int(mousePos[0] - cgSize[0] / 2), cgStartPos[1])
        
        t.xpos = cgPos[0]

        cgPos = (cgPos[0], cgStartPos[1] + int((mousePos[1] - config.screen_height / 2) / 7))
        t.ypos = cgPos[1]

        return 0

    def TargetSetup():
        targetStartX = 280
        targetR1Y = 37
        targetR2Y = 285
        targetR3Y = 460
        targetSpacing = 100
        
        targetDownTime = (0.0, 2.0)
        targetUpTime = 2.0

        currentColumn = 0
        for i in range(12):
            if i < 3:
                targetTrans = Transform(child="mod_assets/minigame_assets/tg-down.png", zoom=targetR1Z)
                targetSprites.append(targetSM.create(targetTrans))

                targetSprites[-1].row = 1
                targetSprites[-1].downTime = random.uniform(targetDownTime[0], targetDownTime[1])
                targetSprites[-1].x = targetStartX + (targetSizes["Top"][0] * i) + (targetSpacing * i)

                targetSprites[-1].y = targetR1Y
            elif i < 7:
                targetTrans = Transform(child="mod_assets/minigame_assets/tg-down.png", zoom=targetR2Z)
                targetSprites.append(targetSM.create(targetTrans))

                targetSprites[-1].row = 2
                targetSprites[-1].downTime = random.uniform(targetDownTime[0], targetDownTime[1])
                targetSprites[-1].x = targetStartX + (targetSizes["Middle"][0] * currentColumn) + (targetSpacing * currentColumn)

                targetSprites[-1].y = targetR2Y

                currentColumn += 1
            elif i < 12:
                targetTrans = Transform(child="mod_assets/minigame_assets/tg-down.png", zoom=targetR3Z)
                targetSprites.append(targetSM.create(targetTrans))

                targetSprites[-1].row = 3
                targetSprites[-1].downTime = random.uniform(targetDownTime[0], targetDownTime[1])
                if i == 7:
                    currentColumn = 0
                else:
                    currentColumn += 1
                targetSprites[-1].x = targetStartX + (targetSizes["Bottom"][0] * currentColumn) + (targetSpacing * currentColumn)

                targetSprites[-1].y = targetR3Y

                currentColumn += 1
            
            targetSprites[-1].idleDir = "Up"
            targetSprites[-1].currentFrame = 5
            targetSprites[-1].animTime = 0.0
            targetSprites[-1].hit = False
            targetSprites[-1].upTime = targetUpTime
    
    def UpdateTarget(st):
        for li, target in enumerate(targetSprites):
            if target.hit == True:
                if target.currentFrame == 1:
                    i = Image("mod_assets/minigame_assets/tg-falling-1.png")
                    if target.row == 1:
                        target.animTime = 0
                        t = Transform(child=i, zoom=targetR1Z)
                    elif target.row == 2:
                        t = Transform(child=i, zoom=targetR2Z)
                    elif target.row == 3:
                        t = Transform(child=i, zoom=targetR3Z)
                    target.currentFrame = 2
                    target.set_child(t)
                elif target.currentFrame == 2:
                    i = Image("mod_assets/minigame_assets/tg-falling-2.png")
                    if target.row == 1:
                        t = Transform(child=i, zoom=targetR1Z)
                    elif target.row == 2:
                        t = Transform(child=i, zoom=targetR2Z)
                    elif target.row == 3:
                        t = Transform(child=i, zoom=targetR3Z)
                    target.currentFrame = 3
                    target.set_child(t)
                elif target.currentFrame == 3 and target.animTime >= 0.1:
                    i = Image("mod_assets/minigame_assets/tg-down.png")
                    if target.row == 1:
                        t = Transform(child=i, zoom=targetR1Z)
                    elif target.row == 2:
                        t = Transform(child=i, zoom=targetR2Z)
                    elif target.row == 3:
                        t = Transform(child=i, zoom=targetR3Z)
                    target.currentFrame = 4
                    target.set_child(t)
                elif target.currentFrame == 4 and target.animTime >= 0.12:
                    i = Image("mod_assets/minigame_assets/tg-falling-2.png")
                    if target.row == 1:
                        t = Transform(child=i, zoom=targetR1Z)
                    elif target.row == 2:
                        t = Transform(child=i, zoom=targetR2Z)
                    elif target.row == 3:
                        t = Transform(child=i, zoom=targetR3Z)
                    target.currentFrame = 5
                    target.set_child(t)
                elif target.currentFrame == 5 and target.animTime >= 0.13:
                    i = Image("mod_assets/minigame_assets/tg-down.png")
                    if target.row == 1:
                        t = Transform(child=i, zoom=targetR1Z)
                    elif target.row == 2:
                        t = Transform(child=i, zoom=targetR2Z)
                    elif target.row == 3:
                        t = Transform(child=i, zoom=targetR3Z)
                    target.currentFrame = 5
                    target.animTime = 0
                    target.hit = False
                    target.set_child(t)
            else:
                if target.idleDir == "Up":
                    if target.animTime >= target.downTime:
                        if target.currentFrame == 5:
                            i = Image("mod_assets/minigame_assets/tg-falling-2.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                                target.currentFrame = 3
                                target.set_child(t)
                        elif target.currentFrame == 3 and target.animTime >= target.downTime + 0.1:
                            i = Image("mod_assets/minigame_assets/tg-falling-1.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                            target.currentFrame = 2
                            target.set_child(t)
                        elif target.currentFrame == 2 and target.animTime >= target.downTime + 0.12:
                            i = Image("mod_assets/minigame_assets/tg-idle.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                            target.currentFrame = 1
                            target.idleDir = "Down"
                            target.animTime = 0
                            target.set_child(t)
                elif target.idleDir == "Down":
                    if target.animTime >= target.upTime:
                        if target.currentFrame == 1:
                            i = Image("mod_assets/minigame_assets/tg-falling-1.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                            target.currentFrame = 2
                            target.set_child(t)
                        elif target.currentFrame == 2:
                            i = Image("mod_assets/minigame_assets/tg-falling-2.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                            target.currentFrame = 3
                            target.set_child(t)
                        elif target.currentFrame == 3 and target.animTime >= target.upTime + 0.1:
                            i = Image("mod_assets/minigame_assets/tg-down.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                            target.currentFrame = 4
                            target.set_child(t)
                        elif target.currentFrame == 4 and target.animTime >= target.upTime + 0.12:
                            i = Image("mod_assets/minigame_assets/tg-falling-2.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                            target.currentFrame = 5
                            target.set_child(t)
                        elif target.currentFrame == 5 and target.animTime >= target.upTime + 0.13:
                            i = Image("mod_assets/minigame_assets/tg-down.png")
                            if target.row == 1:
                                t = Transform(child=i, zoom=targetR1Z)
                            elif target.row == 2:
                                t = Transform(child=i, zoom=targetR2Z)
                            elif target.row == 3:
                                t = Transform(child=i, zoom=targetR3Z)
                            target.currentFrame = 5
                            target.idleDir = "Up"
                            target.animTime = 0
                            target.hit = False
                            target.set_child(t)
            
            target.animTime += 0.01
        
        return 0

transform half_size:
    zoom 0.5

transform spotlights:
    zoom 0.5
    blend "add"
    alpha 0.5

screen gun_minigame:
    image "mod_assets/minigame_assets/background.png" at half_size
    add targetSM
    image "mod_assets/minigame_assets/foreground.png" at half_size
    image "mod_assets/minigame_assets/spotlights.png" at spotlights
    add cgTrans
    image "mod_assets/minigame_assets/score-bg.png" pos (10, 0) at half_size

label gun_start:
    $ cgImage = Image("mod_assets/minigame_assets/gun.png")
    $ cgSize = (330 / 2, 384 / 2)
    $ cgStartPos = (int((config.screen_width / 2) - (cgSize[0] / 2)), config.screen_height - cgSize[1] + 60)
    $ cgPos = (0, 0)
    $ cgTrans = Transform(child=cgImage, zoom=0.5, pos=(cgStartPos[0], cgStartPos[1]), function=UpdateGun)

    $ targetSM = SpriteManager(update=UpdateTarget)
    $ targetR1Z = 0.5
    $ targetR2Z = 0.3
    $ targetR3Z = 0.2
    $ targetSizes = {"Top": (376 * targetR1Z, 455 * targetR1Z),
                    "Middle": (376 * targetR2Z, 455 * targetR2Z),
                    "Bottom": (376 * targetR3Z, 455 * targetR3Z)}
    $ targetSprites = []
    $ TargetSetup()

    call screen gun_minigame with fade
    return