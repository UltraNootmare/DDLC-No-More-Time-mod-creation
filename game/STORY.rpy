label STORY:
    
    play music t9g fadein 1.0
    mc "Ugh, what happened?"
    mc "My head is throbbing..."
    scene bg club_day with fade
    show sayori 1u at f32 zorder 2
    show monika 2o at f33 zorder 1 
    s 1w "Are you okay?"
    show sayori 1u at t32 zorder 2
    mc "Yeah"
    mc "What even happened?"
    m 2r "You collapsed all of a sudden and hit your head off the edge of a desk."
    mc "{b}What??!{/b}"
    m 2n "How do you not remember that? {w=1} You even said 'make sure to catch me' and 'everythings going black' before you fell!"
    show monika 2o at t33 zorder 1 
    mc "I don't really remember anything from today.."
    mc "If I was hurt that bad why didn't you call an ambulance?"
    m 2n "Hehe"
    show monika 2o at t33 zorder 1 
    mc "Well can you call one now?"
    m 2n "Why? I thought Sayori bandaged you up and stopped the bleeding"
    show monika 1horrified at t33 zorder 1 
    show sayori 1horrified at f32 zorder 2
    mc "I taste.. colours?{w=1}{nw}"
    scene black
    play sound "sfx/fall2.ogg"
    "{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{nw}"
    "Okay I get it, we'll continue with the story{w=1}{nw}"
    
    scene bg hospital with fade
    show monika 3o at t41 zorder 1
    show sayori 1u at t42 zorder 3
    "Monika and Sayori are sitting in the waiting room until-"
    show yuri 1u at t44 zorder 4
    show natsuki 2p at t43 zorder 2
    y 1v "Ehm I heard about what happened to [player]-{w=1}{nw}"
    show yuri 1p at t44 zorder 4
    show natsuki 2horrified at t43 zorder 2
    s 1p "HE MIGHT DIE!!!{w=1}"
    show sayori 1u at t42 zorder 3
    y 3i "Sayori stop saying that or I'll put you in the same position [player] is in."
    show monika 3o at t41 zorder 1
    n 5v "{b}I SWEAR TO GOD SAYORI, YOU WERE ABOUT TO GIVE ME A HEARTATTACK!!..{/b}"
    "*One extremely long complaint at Sayori for overexaggerating later*{w=1}{nw}"
    show natsuki 2g at t43 zorder 2
    if persistent.gender == "Other":
        y 1v "Well... How are he doing?"
    else:
        y 1v "Well... How's he doing?"
    show yuri 1u at t44 zorder 4
    m 3p "The doctor says he's in stable condition..."
    m 3p "They say they'll get back to us in the next 30 minutes."
    show monika 3o at t41 zorder 1
    scene black
    "Around 30 minutes later..."

    scene bg hospital_room with fade
    show monika doctor 1o at f43 zorder 1
    mc "Uh..."
    mc "Hey doctor."
    md doctor 1g "Hello [player]."
    show monika doctor 1h at f43 zorder 1
    mc "So.. What seems to be the problem?"
    md doctor 1g "Well.. do you wanna hear the good news or the bad news?"
    show monika doctor 1h at f43 zorder 1
    mc "Uhhh.."
    menu:
        "Good News":
            mc "The good news."
            md doctor 1i "We can help stop the fainting with an antibiotic.."
            show monika doctor 1o at f43 zorder 1
            mc "And the bad news..?"
            show monika doctor 1o at f43 zorder 1
            md doctor 1g "You have heart disease.."
            md doctor 1g "..and it's close to killing you."
            show monika doctor 1o at f43 zorder 1
            mc "W-What??"
        "Bad News":
            mc "The bad news."
            show monika doctor 1o at f43 zorder 1
            md doctor 1g "You have heart disease.."
            md doctor 1g "..and it's close to killing you."
            show monika doctor 1o at f43 zorder 1
            mc "W-What??"
            mc "A-and the good news??!"
            md doctor 1i "We can help stop the fainting with an antibiotic.."
            show monika doctor 1o at f43 zorder 1
    mc "HOW MANY DAYS DO I HAVE LEFT TO LIVE??!{w=1}{nw}"
    md doctor 1p "7"
    show monika doctor 1o at f43 zorder 1
    mc "IS THERE A WAY TO STOP IT??!{w=1}{nw}"
    md doctor 1p "There is - surgery - but it's very expensive.."
    show monika doctor 1o at f43 zorder 1
    "[playerC] calms himself down before replying.."
    mc "*sigh* How much?"
    md doctor 1p "95 million yen.."
    show monika doctor 1o at f43 zorder 1
    "{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{nw}"
    mc "WHAT??!!"
    mc "I DON'T EVEN HAVE THAT MUCH!!{w=1}{nw}"
    md doctor 1p "I know you're under pressure right now. Should I tell your friends?"
    show monika doctor 1o at f43 zorder 1
    mc "..."
    menu:
        "Yes":
            $ tell_friends = True
            mc "Tell them the news."
            md doctor 1p "You made a good choice."
        "No":
            $ tell_friends = False
            mc "Don't tell them."
            md doctor 1p "Are you sure?"
            mc "Yes."
            md doctor 1p "Alright then.."
    if tell_friends:
        scene bg hospital with fade
        show monika doctor 1o at t41 zorder 4
        show yuri 3o at t42 zorder 1
        show sayori 1u at t43 zorder 3
        show natsuki 2p at t44 zorder 2
        md doctor 1p "Hello Monika"
        show monika doctor 1o at t41 zorder 4
        y 3i "Hello Doctor"
        y 3g "So what's the problem??"
        show yuri 3o at t42 zorder 1
        md doctor 1p "[player] has heart disease and will not live to see next week.."
        show monika doctor 1o at t41 zorder 4
        "{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{nw}"
        show yuri 1horrified at t42 zorder 1
        show sayori 2horrified at t43 zorder 3
        show natsuki 1horrified at t44 zorder 2
        n 1v "WHAT DO YOU MEAN HE WON'T LIVE TO SEE NEXT WEEK??!"
        show natsuki 1horrified at t44 zorder 2
        md doctor 2r "[heC] can live if he gets surgery-{nw}"
        show monika doctor 1q at t41 zorder 4
        show yuri 1horrified at t42 zorder 1
        show sayori 2p at t43 zorder 3
        show natsuki 1v at t44 zorder 2
        d "HOW MUCH IS IT??!"
        show yuri 1horrified at t42 zorder 1
        show sayori 2horrified at t43 zorder 3
        show natsuki 1horrified at t44 zorder 2
        md doctor 2r "95 million yen..."
        show yuri 1horrified at t42 zorder 1
        show sayori 2p at t43 zorder 3
        show natsuki 1v at t44 zorder 2
        show monika doctor 1q at t41 zorder 4
        d "HUH?!"
        show yuri 1o at t42 zorder 1
        show sayori 2k at t43 zorder 3
        show natsuki 1n at t44 zorder 2
        md doctor 2p "[playerC] had the same reaction.. heh"
        show monika doctor 1q at t41 zorder 4
        n 1q "Well can we see [persistent.him]??"
        show natsuki 1n at t44 zorder 2
        md doctor 2p "Its cute how much you care for him..."
        show monika doctor 1q at t41 zorder 4
        n 1p "DON'T CALL ME CUTE..!"
        show natsuki 1n at t44 zorder 2
        md doctor 2p "You can go in and see him."

        scene bg hospital_room with fade
        "Monika, Sayori, Natsuki and Yuri rush into the room and before [player] can talk they all hug him..."
        show sayori 1u at t43 zorder 3
        show natsuki 1u at t44 zorder 2
        show yuri 1u at t42 zorder 4
        mc "So did you guys hear the news?"
        y 1o "Y-yes we-uh did.."
        show yuri 1u at t42 zorder 4
        show natsuki 1u at t44 zorder 2
        s 1w "I DON'T WANT YOU TO DIE!!!"
        scene cg sayorihospital with fade
        "Sayori hugs [player] with tears running down her face..."
        

    else:
        scene bg hospital with fade
        "Bad ending"
            
