label STORY:
    # "What is your gender?"
    # menu:
    #     "Male":
    #         $ persistent.he = "he"
    #         $ persistent.hes = "he's"
    #         $ persistent.him = "him"
    #     "Female":
    #         $ persistent.he = "she"
    #         $ persistent.hes = "she's"
    #         $ persistent.him = "her"
    #     "Other":
    #         $ persistent.he = "they"
    #         $ persistent.hes = "they"
    #         $ persistent.him = "them"
    
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
    s 1p "[heC] MIGHT DIE!!!{w=1}"
    show sayori 1u at t42 zorder 3
    m 3i "Sayori stop saying that or I'll put you in the same position [player] is in."
    show monika 3o at t41 zorder 1
    n 5v "{b}I SWEAR TO GOD SAYORI, YOU WERE ABOUT TO GIVE ME A HEARTATTACK!!..{/b}"
    "*One extremely long complaint at Sayori for overexaggerating later*{w=1}{nw}"
    show natsuki 2g at t43 zorder 2
    y 1v "Well... How's [he] doing?"
    show yuri 1u at t44 zorder 4
    m 3p "The doctor says [hes] in stable condition..."
    m 3p "They say they'll get back to us in the next 30 minutes."
    show monika 3o at t41 zorder 1
    scene black
    "Around 30 minutes later..."

    scene bg hospital_room with fade
    show monika doctor 1f at f43 zorder 1
    mc "Uh..."
    mc "Hey doctor."
    md 1g "Hello [player]."
    show monika doctor 1h at f43 zorder 1
    mc "So.. What seems to be the problem?"
    md 1g "Well.. do you wanna hear the good news or the bad news?"
    show monika doctor 1h at f43 zorder 1
    mc "Uhhh.."
    menu:
        "Good News":
            mc "The good news."
            md 1i "We can help stop the fainting with an antibiotic.."
            show monika doctor 1h at f43 zorder 1
            mc "And the bad news..?"
            show monika doctor 1h at f43 zorder 1
            md 1g "You have heart disease.."
            md 1g "..and it's close to killing you."
            show monika doctor 1h at f43 zorder 1
            mc "W-What??"
        "Bad News":
            mc "The bad news."
            show monika doctor 1h at f43 zorder 1
            md 1g "You have heart disease.."
            md 1g "..and it's close to killing you."
            show monika doctor 1h at f43 zorder 1
            mc "W-What??"
            mc "A-and the good news??!"
            md 1i "We can help stop the fainting with an antibiotic.."
            show monika doctor 1h at f43 zorder 1
    mc "HOW MANY DAYS DO I HAVE LEFT TO LIVE??!{w=1}{nw}"
    md 1i "7"
    show monika doctor 1h at f43 zorder 1
    mc "IS THERE A WAY TO STOP IT??!{w=1}{nw}"
    md 1i "There is - surgery - but it's very expensive.."
    show monika doctor 1h at f43 zorder 1
    "[playerC] calms [himself] down before replying.."
    mc "*sigh* How much?"
    md 1g "95 million yen.."
    show monika doctor 1h at f43 zorder 1
    "{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{nw}"
    mc "WHAT??!!"
    mc "I DON'T EVEN HAVE THAT MUCH!!{w=1}{nw}"
    md 1g "I understand you are under alot of pressure right now but I need you to make a descision on if I should tell your friends about the situation or not."
    show monika doctor 1h at f43 zorder 1
    mc "..."