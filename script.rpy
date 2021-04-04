define r = Character("Ru")
define q = Character("???")
define m = Character("You")

label start:
    $ opinion = 0

    scene bg titlescreen
    with fade
    pause (1.0)
    scene bg blackscreen
    with fade
    $ name = (renpy.input("What is your name?"))
    "Hello, [name]"

    play sound "alarmclock.mp3"
    pause (4.0)
    scene bg bedroom
    with fade
    show mc:
        yalign 0.85
        xalign 0.075
    "You turn off the alarm and slowly open your eyes to see sunlight pouring into your room."
    play music "backgroundmusic.mp3" fadein 2.0
    "After the long winter season, you're not quite used to waking up to daylight yet."
    "The clock on your bedside table reads 6:00 am. You have about thirty minutes to get ready before you need to head off to school, so you reluctantly get out of bed and head into the kitchen."
    scene bg kitchen
    with fade
    show mc:
        yalign 0.9
        xalign 0.8
    "You start the coffee maker, and then get dressed and brush your teeth."
    "Your coffee is ready when you return, and you drink it as you eat a bowl of cereal."
    "Just as you're sipping the last dregs of your coffee, you hear a loud crashing noise outside."
    play sound "crash.mp3"
    "It sounds like it came from the woods behind your house."
    menu:
        "Do you investigate the noise?":
            jump investigate
        "Or do you ignore it and go on with your day?":
            jump ignore

label ignore:
    "You shrug and don't really think anything of it."
    "You finish up with breakfast and then head off to school."
    scene bg hallway
    with fade
    show mc:
        yalign 0.9
        xalign 0.2
    show friends:
        yalign 0.6
        xalign 0.7
    "At school, you stop at your locker to put some stuff away and you see some of your friends down the hallway."
    "You had a few questions to ask your teacher about an assignemnt, but that could always wait."
    menu:
        "Do you go to class early to talk to your teacher?":
            scene bg classroom
            with fade
            show mc:
                yalign 0.8
                xalign 0.5
            "You head into your first period classroom and ask your teacher a few questions you'd had about an assignment."
            "She answers them and you feel more confident about your school work. A minute later, the bell rings and the rest of the class files in."
            jump firstprd
        "Or do you hang out with your friends before class?":
            "You wave to your friends and they come over to you."
            show friends big:
                yalign 0.9
                xalign 0.5
            "You all talk about your plans for the weekend until the bell rings and you head off to class."
            scene bg classroom
            with fade
            jump firstprd
label firstprd:
    show mc:
        yalign 1.0
        xalign 1.0
    "A moment later, class begins."
    menu:
        "Do you pay attention in class?":
            "You listen to the lecture and jot down notes every now and then."
            "Just as your teacher is wrapping up the lesson, the bell rings."
            jump lunch
        "Or do you zone out?":
            "You try your best to pay attention, but you find your attention being drawn out the window."
            "The class passes by without you really noticing, and before you know it, the bell rings."
            jump lunch

label lunch:
    "You go to a few more classes, and then it's time for lunch"
    menu:
        "Do you eat lunch outside with your friends?":
            scene bg outside
            with fade
            "You and your friends decide to spend your lunch break out in the spring sunshine, so you get your food and then head outside."
            "You all chat about classes and plans for after school until you're finished eating and the bell rings."
            jump endofday
        "Or do you all eat in the cafeteria?":
            scene bg cafeteria
            with fade
            "You and your friends decide to stay inside to eat lunch, so you get your food and then sit at the nearest empty table."
            "You all chat about classes and plans for after school until you're finished eating and the bell rings."
            jump endofday

label endofday:
    scene bg hallway
    with fade
    "The rest of your classes pass by smoothly, and soon the final bell rings, signalling the end of the school day."
    scene bg kitchen
    with fade
    show mc:
        yalign 0.9
        xalign 0.8
    "Not too long later, you're back home."
    "As you settle into your evening routine, you remember the noise you heard that morning."
    "You wonder if you perhaps should have gone to see what happened."
    "But what's done is done, you think with a shrug, and a moment later, the thought fades away, replaced by something new."
    scene bg titlescreen
    with fade
    jump credits
    return

label investigate:
    "Your curiousity gets the better of you, and you put on a pair of shoes and head out the back door towards the woods."
    scene bg forest ufo
    with fade
    show mc small:
        yalign 0.5
        xalign 0.8
    "In the forest, you find the source of the crashing noise: a strange, metal object you can't really place the name of lying in a patch of dirt."
    "The bushes around the object have all been disturbed, some with branches and leaves ripped off. A bird sits on a low branch, tweeting in a disgruntled sort of way."
    "Between the leaves of bushes and trees, you can see something yellow moving around the object."
    "Feeling somewhat nervous, you decide what to do next."
    menu:
        "Do you pick up a stick and get ready to defend yourself?":
            $ opinion -= 3
            jump defense
        "Or do you hide behind a tree and wait to see what happens?":
            jump wait
label defense:
    "You look on the ground and see a large stick around the size and thickness of a baseball bag. You pick it up and wait."
    "A moment later, the yellow figure moves into the clearing."
    show ru:
        yalign 0.8
        xalign 0.25
    "Without thinking, you run into the clearing waving the stick above your head."
    show mc small:
        yalign 0.9
        xalign 0.5
    show ru white:
        yalign 0.8
        xalign 0.15
    "The animal...lizard...alien...whatever it is suddenly turns white and takes a step backwards."
    menu:
        "Do you stop?":
            $ opinion += 1
            jump stopscaring
            return
        "Or do you continue?":
            $ opinion -= 4
            jump continuescaring
label wait:
    show mc small:
        yalign 0.6
        xalign 0.7
    "You hide behind a big tree and watch. A moment later..."
    show ru:
        yalign 0.8
        xalign 0.25
    "...the yellow figure moves into the clearing."
    "You watch for a while as it looks around at its surroundings. It seems wary to leave its car...or plane...you aren't really sure what it is, still."
    "Unaware of your presence, it travels on its four little legs closer to you than it had before and you instinctively take a step back."
    play sound "branchsnap.mp3"
    "CRUNCH"
    "You feel your breath get caught somewhere in your throat at the noise. You look down and see that you stepped on a dry branch, snapping it in half."
    "Nervously, you peer around the tree and see the yellow creature staring at you."
    menu:
        "Do you run away?":
            jump runaway2
        "Or do you face the creature?":
            $ opinion += 2
            jump faceru

label stopscaring:
    "You freeze, realizing you've scared the creature more than it scared you in the first place. Slowly you lower the stick to the ground."
    m "Sorry. I didn't mean to scare you."
    "The creatu -- you're not an idiot, it's clearly an alien unless biologists were wildly incorrect about the types of amphibians native to where you live -- doesn't say anything, but slowly turns yellow again."
    show ru:
        yalign 0.8
        xalign 0.15
    jump intros

label continuescaring:
    show ru white:
        yalign 0.8
        xalign 0.1
    "You keep chasing the creature, only stopping when it skitters on its four little legs into the woods."
    hide ru white
    "You take several deep breaths, feeling the panic in your chest start to subside."
    "You turn to walk back to your house. If you hurry, you can make it to school with time to spare. You can tell your friends about the weird animal you chased away from your house."
    "You make it halfway out of the woods, and then you hear a booming sound and feel the ground shake. You wonder if it's thunder until it happens again."
    "You hear the trees rustling behind you and turn just in time to see the source of the sound"
    show ru redbig:
        yalign 0.8
        xalign 0.05
    "The creature must have tripled in size, and turned a deep shade of red, and now it's heading right for you."
    show ru redbig:
        yalign 0.8
        xalign 0.23
    menu:
        "Do you run?":
            $ opinion += 1
            jump runaway1
        "Or do you stand your ground?":
            $ opinion += 2
            jump standground

label standground:
    "You turn around, your heart pounding in your chest, and shout,"
    m "WHAT DO YOU WANT?"
    "The alien stops."
    q "RU WANTINGS TO GO TO HOME!"
    "You stop. So does the alien - Ru, you thought he'd said."
    "He wants to go home?"
    m "You want to go home?"
    show ru red:
        yalign 0.8
        xalign 0.23
    "Ru returned to his normal size."
    r "Yes. I has to crashed here on my way to home and my ship is the broken."
    m "Oh."
    m "Can you fix it?"
    r "Yes. I was to trying fixing it before you to running at me."
    show ru orange:
        yalign 0.8
        xalign 0.15
    "Without waiting for a response, Ru returned to his ship."
    show ru orange:
        yalign 0.8
        xalign 0.15
    "You notice that instead of red, he is a slighly more pleasant shade of orange. You decide that's probably a good sign, although you admit you can't be entirely sure."
    "You stand and wait as Ru tinkers with his ship. You begin to feel bad about your initial reaction. You regret running at Ru and trying to scare him away."
    "You didn't know anything about him or why he was there. You think about apologizing for what you did."
    menu:
        "Do you say nothing to Ru?":
            $ opinion -= 1
            "You choose to not say anything. You do feel sorry, but at the same time, you just want the alien to leave without anything else happening."
            "A while later, Ru has returned to his normal shade of yellow, and seemed to have finished fixing the ship."
            scene bg fixedufo
            show ru:
                yalign 0.8
                xalign 0.2
            show mc small:
                yalign 0.6
                xalign 0.7
            m "Did you fix it?"
            r "It is not perfectly, but it is goodly enough. It will to get me home."
            m "Okay."
            jump end
        "Or do you apologize?":
            $ opinion += 3
            "You decided to say sorry. You know it may not help, but you'll feel better, and maybe he'll feel better too."
            m "Ru?"
            r "Yes?"
            "You take a deep breath."
            m "I'm sorry...for what I did. I didn't know who you were or why you were here and I was scared, but I didn't consider what you were feeling."
            m "I shouldn't have tried to run you off, and I'm sorry."
            show ru:
                yalign 0.8
                xalign 0.15
            "Ru doesn't turn away from working on the ship, but he returns to his normal shade of yellow."
            r "I understanding. I to know my kind is not to found on this terrain."
            "You nod. You aren't really sure how to respond, but Ru doesn't seem to be waiting for one, so leave it at that."
            "A little while later, his ship appears to be fixed."
            scene bg fixedufo
            show ru:
                yalign 0.8
                xalign 0.2
            show mc small:
                yalign 0.6
                xalign 0.7
            m "Will it work?"
            r "It is not perfectly, but it is goodly enough. It will to get me home."
            m "That's good."
            jump end

label runaway1:
    "Without thinking, you turn and run as fast as you can back to your house."
    scene bg kitchen
    with fade
    show mc:
        yalign 0.9
        xalign 0.8
    "As soon as you're inside, you lock the door behind you. You back away from the windows, breathing heavily."
    "The clock above the stove tells you that if you don't leave for school right now, you'll be late, but you know for sure that you're not going anywhere."
    "You don't really know what to do. You debate calling your parents, but if you told them that you got chased out of the woods by an alien, they definitely wouldn't believe you."
    "Which is fair."
    "You decided to go upstairs to your bedroom. There's a window that looks out to the edge of the woods, so maybe you'll see something."
    scene bg bedroomview
    with fade
    show mc:
        yalign 0.9
        xalign 0.8
    "You go your window and look outside. A moment later, you see the alien come out of the trees."
    "It's no longer large and red, but back to its normal yellow color and small size. It stands at the edge of the forest for a moment, looking around."
    "Then it starts to skitter across your yard, heading for the toolshed next to your house. You watch it open the door and start rummaging through the stuff inside."
    menu:
        "Do you shoo away the alien?":
            $ opinion -= 3
            "You nervously head back downstairs."
            scene bg kitchen
            with fade
            show mc:
                yalign 0.9
                xalign 0.8
            "You look out the window on your back door and see the alien is still looking around in your toolshed. You take a deep breath, undo the lock, and head out the door."
            jump shoo
        "Or do you go to see what it wants?":
            $ opinion += 3
            "You nervously head back downstairs."
            scene bg kitchen
            with fade
            show mc:
                yalign 0.9
                xalign 0.8
            "You look out the window on your back door and see the alien is still looking around in your toolshed. You take a deep breath, undo the lock, and head out the door."
            jump toolshedtwo
label runaway2:
    "Without thinking, you turn and run as fast as you can back to your house."
    scene bg kitchen
    with fade
    show mc:
        yalign 0.9
        xalign 0.8
    "As soon as you're inside, you lock the door behind you. You back away from the windows, breathing heavily."
    "The clock above the stove tells you that if you don't leave for school right now, you'll be late, but you know for sure that you're not going anywhere."
    "You don't really know what to do. You debate calling your parents, but if you told them that you just ran away from a small alien and its UFO, they definitely wouldn't believe you."
    "Which is fair."
    "You decided to go upstairs to your bedroom. There's a window that looks out to the edge of the woods, so maybe you'll see something."
    scene bg bedroomview
    with fade
    show mc:
        yalign 0.9
        xalign 0.8
    "You go your window and look outside. A moment later, you see the alien come out of the trees."
    "It stands at the edge of the forest for a moment, looking around."
    "Then it starts to skitter across your yard, heading for the toolshed next to your house. You watch it open the door and start rummaging through the stuff inside."
    menu:
        "Do you shoo away the alien?":
            $ opinion -= 3
            "You nervously head back downstairs."
            scene bg kitchen
            with fade
            show mc:
                yalign 0.9
                xalign 0.8
            "You look out the window on your back door and see the alien is still looking around in your toolshed. You take a deep breath, undo the lock, and head out the door."
            jump shoo
        "Or do you go to see what it wants?":
            $ opinion += 3
            "You nervously head back downstairs."
            scene bg kitchen
            with fade
            show mc:
                yalign 0.9
                xalign 0.8
            "You look out the window on your back door and see the alien is still looking around in your toolshed. You take a deep breath, undo the lock, and head out the door."
            jump toolshedtwo
label faceru:
    show mc small:
        yalign 0.9
        xalign 0.5
    "You step out from behind the tree and slowly walk towards the creature - you're not an idiot. It's clearly an alien unless biologists were wildly incorrect about the types of amphibians native to where you live."
    "You're feeling unsure and a little frightened, but the alien doesn't seem to be acting aggressive, so you don't let your fear overcome you."
    jump intros

label intros:
    "You feel like you should say something, but you're not even sure the alien would understand you"
    m "Do you have a language?"
    q "Ioc, y fubo u rumtauto"
    "Your eyebrow furrows as you pause. You don't have any idea what the alien said, but he must have understood what you said because he gave a response."
    "You ask a different question:"
    m "Do you understand my language?"
    "There is no answer for a moment."
    q "Yes."
    m "My name is [name]. Do you have a name?"
    q "Ru."
    m "Nice to meet you, Ru. Where did you come from?"
    "Ru lifts an arm up towards the sky."
    m "Did you come here on that?"
    "You point to the fallen UFO."
    r "Yes"
    m "Were you trying to land here? On Earth?"
    r "No. To going home."
    m "You want to go home?"
    show ru blue:
        yalign 0.8
        xalign 0.15
    r "Yes. But my ship is the broken. Until I to fix it, I cannot to go home."
    "You think for a minute. There's a shed in the backyard that has all sorts of tools in it. You want to help Ru fix his spaceship, but you also aren't sure you want an alien near your house."
    menu:
        "Do you bring Ru to the toolshed so he can see if you have what he needs?":
            $ opinion += 3
            jump toolshed
        "Or do you see if the UFO can be fixed with what's already here?":
            jump stay
label toolshedtwo:
    scene bg toolshed
    show ru:
        yalign 0.8
        xalign 0.2
    show mc small:
        yalign 0.8
        xalign 0.05
    m "Hey."
    show ru white:
        yalign 0.8
        xalign 0.2
    "The alien jumps slighly and turns white as it looks up at you."
    m "No, it's okay. Are you looking for tools to fix your ship?"
    q "Yes."
    "You raise your eyebrows. You didn't expect a response - at least, not one you'd understand."
    m "Okay. Take what you need."
    "You watch for a while as the alien searches through the tools in the shed. Then you decide to introduce yourself (you might as well at this point, you're letting him borrow a wrench)."
    m "My name is [name]. Do you have a name?"
    q "Ru."
    "You nod."
    m "Where did you come from?"
    "Ru lifts an arm up towards the sky."
    m "Were you trying to land here? On Earth?"
    r "No. To going home."
    m "You want to go home?"
    r "Yes. But my ship is the broken. Until I to fix it, I cannot to go home."
    "You nod again, but say nothing more."
    "A few minutes later, Ru has apparently found everything he needs, because he heads back towards the forest. You follow him from a few feet behind."
    scene bg forest ufo
    show ru:
        yalign 0.8
        xalign 0.15
    show mc small:
        yalign 0.6
        xalign 0.7
    "Ru quickly starts to tinker with his ship. He works quickly, and sooner than you anticipated, he is finished."
    scene bg fixedufo
    show ru:
        yalign 0.8
        xalign 0.2
    show mc small:
        yalign 0.6
        xalign 0.7
    m "Did you fix it?"
    r "Yes. It is not perfectly, but it is closely. Your tools to made the job quickly. Thanking you."
    m "You're welcome. I want you to get home safe."
    jump end
label shoo:
    scene bg toolshed
    show ru:
        yalign 0.8
        xalign 0.2
    show mc small:
        yalign 0.8
        xalign 0.05
    m "Hey!"
    show ru white:
        yalign 0.8
        xalign 0.2
    "The alien jumps slighly and turns white as it looks up at you."
    m "You can't be here! You have to go back!"
    show ru:
        yalign 0.8
        xalign 0.5
    "The alien drops the tools it was holding and starts scurrying back towards the woods."
    show ru:
        yalign 0.8
        xalign 0.7
    show mc small:
        yalign 0.8
        xalign 0.5
    "You follow it, mostly to make sure it stays away from your home, but also so you can watch it leave. You want to be sure it's gone."
    show ru:
        yalign 0.8
        xalign 0.9
    show mc small:
        yalign 0.8
        xalign 0.7
    scene bg forest ufo
    show ru:
        yalign 0.8
        xalign 0.15
    show mc small:
        yalign 0.6
        xalign 0.7
    m "Go back to where you came from, this place isn't for you."
    "The alien starts quickly tinkering with the crashed ship. You stand fairly far away - close enough to see what it's doing, but far enough to give you a headstart if it tries anything."
    "A while later - it felt like longer than it probably actually was - the alien steps away from the ship."
    scene bg fixedufo
    show ru:
        yalign 0.8
        xalign 0.2
    show mc small:
        yalign 0.6
        xalign 0.7
    jump end
label toolshed:
    m "Do you need tools or anything to fix it?"
    r "I has most, but I might to need more."
    m "I have some tools in my shed that you could use. Follow me!"
    "You lead Ru out of the woods to the toolshed next to your house."
    scene bg toolshed
    show ru:
        yalign 0.8
        xalign 0.5
    show mc small:
        yalign 0.8
        xalign 0.05
    "You open the door so Ru can see inside. His eyes roam over the items in the shed, and a moment later, he moves closer."
    show ru:
        yalign 0.8
        xalign 0.2
    "Ru reaches for some tools and a few minutes later, he appears to be done."
    r "Thanking you. These are the tools exactly I to need."
    m "You're welcome."
    "Ru heads back towards the forest and you follow him."
    scene bg forest ufo
    show ru:
        yalign 0.8
        xalign 0.15
    show mc small:
        yalign 0.6
        xalign 0.7
    "Ru quickly starts to tinker with his ship. He works quickly, and sooner than you anticipated, he is finished."
    scene bg fixedufo
    show ru:
        yalign 0.8
        xalign 0.2
    show mc small:
        yalign 0.6
        xalign 0.7
    m "Did you fix it?"
    r "Yes. It is not perfectly, but it is closely. Your tools to made the job quickly. Thanking you again."
    m "Of course. I want you to get home safe."
    jump end

label stay:
    m "I'm sorry about your ship. Will you be able to fix it?"
    r "It will to be hard, but I can to do it."
    m "That's good."
    show ru:
        yalign 0.8
        xalign 0.15
    "As Ru starts to tinker with his ship and you lean against a nearby tree and wait."
    show mc small:
        yalign 0.6
        xalign 0.7
    "It takes a while, and you feel a little guilty knowing that it probably would take less time if you'd let him use tools from your shed, but eventually he is finished."
    scene bg fixedufo
    show ru:
        yalign 0.8
        xalign 0.2
    show mc small:
        yalign 0.6
        xalign 0.7
    m "Did you fix it?"
    r "It is not perfectly, but it is goodly enough. It will to get me home."
    m "That's good."
    jump end

label end:
    if opinion >= 0:
        jump goodending
    elif -4 <= opinion <= 0:
        jump neutralending
    else:
        jump badending

label goodending:
    r "It's timely for me to go to home now."
    m "That's good."
    show ru pink:
        yalign 0.8
        xalign 0.2
    r "Thanking you for your kindliness. I was scaredly when I to landed on this terrain. Your to help made it betterly."
    m "You're welcome, I'm glad I could help."
    r "Before I to leave, do you to want to go to space?"
    "You feel a little nervous. Space? That would be cool, but you wonder how safe it is? And what about coming back?"
    m "Is that safe?"
    r "Yes. I to am good at flying."
    m "And will you bring me back home?"
    r "Of course."
    "You think about it for a moment."
    menu:
        "Do you go with him?":
            m "Okay!"
            "Ru leads you to the entrance to the spaceship and you follow him inside"
            hide ru
            hide mc small
            play sound "spaceship.mp3"
            "You hear a strange metallic sound and feel the fllor start to shake as the ship starts up, and then a moment later, the ship lifts off the ground."
            "Nervous, you close your eyes."
            scene bg blackscreen
            with fade
            "Everything goes black on the ship as it shoots higher up into the sky."
            "A while later, the shaking stops and the ship slows down."
            r "You can to open your eyes."
            scene bg spaceship
            with fade
            show ru:
                yalign 0.9
                xalign 0.2
            show mc small:
                yalign 0.9
                xalign 0.7
            "You are taken aback for a moment at the sight of outerspace from the windows of the spaceship."
            "You feel grateful that you had an extra-terrestrial encounter and were not only left unscathed, but had a great experience - you're in outerspace!"
            "You wish for a second to talk about this with someone, but you push the idea away."
            "You know that even if you tried to tell anyone about what you just experienced, they probably wouldn't believe you."
            "Not that it would matter. You knew that this, and Ru the alien, was something you would never forget."
            scene bg blackscreen
            with fade
            jump credits
        "Or do you decline?":
            m "No thanks. It sounds like fun, but you should get home."
            r "Okay."
            jump takeoff

label neutralending:
    r "It's timely for me to go to home now."
    m "That's good."
    jump takeoff

label takeoff:
    hide ru
    "You watch as Ru gets into his spaceship."
    play sound "spaceship.mp3"
    "You hear a strange metallic sound as the ship starts up, and then a moment later, the ship lifts off the ground."
    $ renpy.movie_cutscene("terrainmovie.webm")
    scene bg forest
    "You let out a long exhale."
    "A part of you feels grateful that you had an extra-terrestrial encounter and were left unscathed, but another part of you wonders if you made the right choices."
    "Maybe treating Ru differently would have led to a different outcome. You wish for a second to talk about this with someone, but you push the idea away."
    "You know that even if you tried to tell anyone about what you just experienced, they probably wouldn't believe you."
    "Not that it would matter. You knew that this, and Ru the alien, was something you would never forget."
    scene bg blackscreen
    with fade
    jump credits

label badending:
    r "This terrain is not been to explored by my kind before."
    r "My superiors to will want information about what it is to like here."
    "The alien's eyes narrow."
    "Before you can do anything to stop it, the alien is dragging you onto the ship. You try to scream, but no sounds come out."
    scene bg blackscreen
    with fade
    "You hear a strange metallic sound and feel the cold floor beneath you shake as the space ship starts up, and then a moment later, the ship lifts off the ground."
    "You start to wonder if you made the right choices."
    "Maybe treating Ru differently would have led to something different - not this. You had assumed the alien would be hostile and violent, so you acted the same way."
    "Maybe if you had been kinder, it wouldn't have mattered."
    "A while later, the shaking stops and the ship slows down. You open your eyes."
    scene spaceship
    with fade
    show ru:
        yalign 0.8
        xalign 0.2
    show mc small:
        yalign 0.6
        xalign 0.7
    "You are taken aback for a moment at the sight of outerspace from the windows of the spaceship."
    "The feeling fades away though, as you see Earth getting smaller and smaller, and you know that you will never see your home again."
    scene bg blackscreen
    with fade
    jump credits

label credits:
    $ credits_speed = 40
    scene black
    show credits_image at Move((0.5, 1.0), (0.5, -1.0), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10)
    scene bg titlescreen
    with fade
    return
