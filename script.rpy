#TODO: REPLACE ALL INSTANCES OF MC WITH THE CHARACTER'S NAME!!!!

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#if you ever wanna try out that tales thing, feel free to use this! https://www.renpy.org/doc/html/quickstart.html#positions

score = 0
#you can change font color of text here using "color=#<Color in hex here>"
define e = Character("Eileen")
#prospective names: Ashton, 
define mc = Character("MC", color="#e74e4eff")

define g = Character("Spirit", color="#8f8585c4")

define l = Character("Lynne" color="#ffee00ff")

define n = Character("Narrator", color="#508f20")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    #TODO: make sprite for this, and hook it up!
    scene bg devroom
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #change to my sprite!
    show eileen happy

    # These display lines of dialogue.
    scene black
    e "Welcome to my little VN!"

    e "This is my first time adventuring out into this kinda stuff, so sorry if it doesn't meet your expectations :/"

    e "I hope you enjoy it nonetheless though!"

    scene bg entrywayNight

    mc "11:30. That was the time that I get back from my tutoring session at Mrs. Pertholder's house."
    mc "It had just started to drizzle, and the moon was full, and shining its dull light over the streets."
    mc "It was getting worringly close to exam season, so my parents thought that it'd be a good idea to get some tutoring."
    mc "Mrs. Pertholder was a good family friend of ours too, so she agreed to take care of it to sooth my parent's feelings about my exams."

    scene bg LivingroomNight
    mc "As I walked through the living room on my way to the kitchen, I took note of how melancholic everything felt."
    #TODO: Might be a good addition to add in some stock images to fade in that relate to what MC is talking about 
    mc "Typically, as soon as I walked through the door, I'd be saddled with countless chores to take care of, varying from taking care of the dishes, and doing some laundry"
    #add in second image here
    mc "To cooking dinner, and doing some maintence on Dad's car."

    mc "It was a nice change of pace."

    scene fridgeNight
    with fade
    mc "Hmm, what should I get to eat? I'm still pretty hungry since I wasn't able to eat all too much while I was at Mrs. Pertholder's."
    
    with hpunch

    mc "What was that!?"

    scene bg LivingroomNight
    with fade
    mc "Sounds like it came from the side of the house, I should go make sure that there's nothing weird going on!"

    scene bg entrywayNight
    with fade
    n "MC rushes out, only stopping to grab a umbrella on the off-chance that the rain started to pick up."

    mc "Alright, let's go check out the side of the house."

    n "A loud shriek pierces the soft tranquility of the night."

    "???" "AAAAAAAaaaaa......"

    mc "Alright, that definetly did not come from the side of the house... I should probably still check up on whatever that was though."

    #TODO:Make choice to either head back, or keep going. both choices result in him going deeper.



    mc "alright, lets go take a look then... \n It's not like i'd be able to get sleep if I ignore this..."

    scene bg cemetetary
    with fade

    n "As mc continues to follow the noise, he eventually arrives at the local cemetetary."

    mc "Yeah no. I'm not doing this."

    mc "There is no way that i'm ever going to go into that old, unsettling graveyard at god-knows what time at night."

    "???" "Well, its a good thing you won't have to ~"

    mc "HUH??? WHAT WAS THAT???"

    n "A cold chill envelops mc's body, reaching all the way down to the bone."

    mc "SCREW THIS"
    scene bg middletown
    with fade
    n "mc makes a mad dash back towards his house, however..."

    #make reaper sprite show up in the middle of the screen

    mc "WHAT THE F*** IS THAT?????"

    "???" "I beckon thee, join me in the world that comes afte-"

    mc "OUT OF THE WAY!"
    with hpunch
    #play punch sfx, and slide reaper off screen

    n "mc continues to make a mad dash for his house."


    scene  bg entrywayNight with fade
    mc"*pant* *pant* *pant*"
    mc"WHat was that???"
    mc" You know what? screw this, I'm going to bed"

    scene bg bedroomNight with fade
    mc "Maybe I'll be able to make sense of this tommorow morning."    
    scene bg black with fade
    n"End of day one."
    
    #add save prompt
    call screen confirm("Do you want to save?", yes_action=[ShowMenu('save'), return()], no_action=return())

    n"Start of day 2."

    scene bg bedroomDay 
    mc "Yawwwwn"
    n "He rubs his eyes."
    #TODO: maybe add sprite of MC yawning?
    mc "Man, that was a stupid weird dream I had."
    
    mc "But lets disregard that for now, I gotta start getting ready for school!"

    n "He gets up, and starts getting ready."

    #cg of him brushing his teeth

    mc "hmm hm hm hmmm"

    #cg if him making breakfast

    #cg of him sitting down to eat
    mc "Alright, time to dig in!"

    "???" "That looks pretty good if I do say so myself~"

    mc "Huh?"

    "???" "Oh, don't you dare \"huh\" me!"

    "???" "And besides, its a little rude to not look at someone whenever they're talking, isn't it?"
    scene mindscape with pixellate

    mc "What?"

    mc "WHAT THE H*** IS GOING ON???"

    "???" "You're rather foul-mouthed, aren't you? I've barely known you for even a day, and I've already heard you curse three times~"

    "???" "Doesn't really fit your whole \"Family guy \" persona all too well, does it?"

    #TODO: maybe implement a sprite of MC sighing?


    #TODO: these are the MC's thoughts. make sure to make them a different color to indicate that
    mc "I still have no idea whats going on in the slightest..."

    mc "I guess this means that last night wasn't a dream either..."

    "???" "HEY! ARE YOU LISTENING TO ME AT ALL? Dumb mortals, not even able to do something as simple as pay attention to others when they're being spoken to."

    mc "Alright you.. whatever you are. What are you exactly, and what am I doing here?"

    "???" "How rude! You can't even bother to refer to me by my name!"
    #MC deadpan
    mc "Well, its not like I know it or anything...."

    "???" "Well, in that case, I might was well introduce myself. Consider it an honor, since you are nothing more than a lowly mortal."
    
    "???" "I am _____, and I am what you mortals might refer to as a spirit."

    mc "A spirit?"

    g "Yes, you buffon! a spirit, a ghost, a poltergeist, or whatever you mortals call us now!"

    #confused
    mc "Okayyyy? And this concerns me how???"

    g "Well, I was in a hint of trouble yesteryear, and you happened to show up at an opportune time for me to... cohabitate with you."

    mc "Alright, I have two questions."

    mc "First off, when you say that you were in trouble yesterday, are you talking about that large figure that I was running away from yesterday?"

    g "Yes, I am reffering to that. You were also extraordinarily undignified while doing so."

    mc "What was that thing anyways?"

    g "Us spirits refer to them as \"Reapers\". They are tasked with rounding up wayward souls in any way possible."

    g "The one that was after you yesterday was attempting to reclaim my soul. "

    mc "And secondly, what exactly do you mean by \"Cohabitate\"?"

    g "I mean that we're currently sharing a body, you dunce!"

    g "And now that I'm \"Cohabiting\" with you, It'll need to kill you to get to me."
    
    #Mc shock
    with vpunch
    mc "AND WHAT MADE YOU THINK THAT I'D AGREE WITH THAT!!!"
    

    g "Oh calm down! I'm not cruel enough to act out for no reason, or get you killed!"

    g "And I promise not to, on one condition."

    mc "What is it?"

    g "You help me regain something of mine."

    mc "What exactly do you want me to find for you?"

    g "Good lord. Are all you mortals this annoying? "

    g "I'm looking for an old pendant of mine."
    
    g "Legends say that once a spirit has gained its most prized possesion, It is allowed to continue roaming around the earth, and choose to swap between the afterlife and the mortal plane whenever they wish."
    
    g "Now, don't you have something to be doing?"

    scene tableDay
    n "With a snap, MC is returned back to the waking world, and after gaining his bearings, glances at the clock over at the corner"

    mc "Crud, I'm gonna be late!"

    n "He then subsequently bolts out the door."

    scene schoolentry with fade
    mc "Can't afford to dawdle, it looks like class starts in 2 minutes!"

    scene classroom with fade
    #this is a thought, mark that out 
    mc "Thank goodness I made it on time!"

    n "After that close call, mc managed to make it through the rest of the day no problem."
    n "He mostly focused on reviewing for his exams, but he did manage to spend some time with his friends during lunch."
    n "Naturally, he hadn't mentioned what had happened that morning to anyone, out of fear of becoming a social pariah, or just outright being insane."

    n "And as was usual, he headed off to Mrs. Pertholder's house after he had finished with class."

    n "After a few hours of studying, they decided to do one last quick review."
    #quiz time!
    "Mrs. Pertholder" "Alright, so let's do one last quick review before we call it for tonight."
    "Mrs. Pertholder" "We'll begin with some simple stuff first."
    "Mrs. Pertholder" "We'll do a simple factoring question first."
    "Mrs. Pertholder" "A quick reminder on how to factor: First, you want to take the constants from the a, and c. Then, multiply them together, and find which factors add up to b. Flip the signs for the answers that you got, and you now know what x is equal to."
    "Mrs. Pertholder" "So, what are the factors of the expression x^2 + -3x + 4?"
    menu:
        "The factors are (x + 4) and (x - 1)":
            "That's correct!"
            score = score + 1
        "The factors are (x - 4) and (x + 1)":
            "Not quite..."
        "The factors are (x - 2) and (x + 1)":
            "Not quite..."
    "Mrs. Pertholder" "Alright, now we'll do a bit of English."
    "Mrs. Pertholder" "The words affect and effect are often confused with one another. If you want to easily know which one to use, all you need to know is what type of speech each word is."
    "Mrs. Pertholder" "Effect is a noun tha is used to show when something happens, while affect is a verb that is used to show how something had something else done to it. "
    "Mrs. Pertholder" "So, what word fits in the blank: Construction will _____ traffic in the area."
    menu: 
        "It's Effect!":
            "Not quite...."
        "It's Affect!":
            "That's correct!"
    "Mrs. Pertholder" "Alright, lets move on to some logic questions next."
    "Mrs. Pertholder" "De Morgan's Laws are a common logical concept."
    "Mrs. Pertholder" "They are based off the idea of negation."
    "Mrs. Pertholder" "For our purposes, we'll use programming syntax to visualize it. ! will stand for not, & will stand for and, and || will stand for or."
    "Mrs. Pertholder" "Now, which one of these statements is correct?"
    menu:
        "!a & !b = !(a || b)":
            "That's correct!"
        "!a & !b = !(a & b)":
            "Not quite..."
        "!(a || b) != (a & b)":
            "Not quite..."
    n "At this point, it was starting to get rather late, and mc decided that it'd be a good time to start heading home."

    g "Your life is pretty boring now that I've experienced it first hand."

    g "Seriously, how do you mortals put up with this?"

    mc "Well, it isn't all boring... ᵉˢᵖᵉᶜᶦᵃˡˡʸ ʷʰᵉⁿ ᶦ ᵍᵉᵗ ᵐʸ ᵇᵒᵈʸ ʰᶦ⁻ʲᵃᶜᵏᵉᵈ......"

    g "First off, rude. Secondly, we're in the same body. Anything you try to hide from me, save your thoughts ends up being something that I hear too. So don't bother trying to keep secrets or anything."

    mc "Great. Just great. Now I don't have any privacy either..."

    mc "And anyways, it isn't always this boring. I usually do other things."

    mc "I'm just stuck studying all day since my parents are expecting me to take care of them as soon as I graduate and get a job. And since it's exam week, they're not exactly gonna get off my case, are they?"

    g "Pardon me if I'm wrong here, but isn't it supposed to be the other way around?"

    mc "Nah, you hit the nail on the head. The only reason why I'm an abnormality is because my parents decided to spend their highschool years doing nothing, and get minimum wage jobs as soon as they dropped out."

    mc "After that, they had the ABSOLUTELY WONDERFUL idea of adopting some kid and forcing him to be their glorified slave."

    mc "Guess which lucky kid they picked."

    #g "lol. lmao even"

    g"man, sucks to be you."

    mc "f**k you."

    g"That makes four times that i've heard you curse now. Any more, and i'll have to get you a swear jar~"

    scene bg street with fade

    n "The two (or rather one?) arrive at a street not too far from Mc's house"
    
    
    "???" "HEY! YOU THERE!"

    mc "Huh?"

    g "God, you're just infatuated with that word, aren't you?"

    mc "Shhhh! I need to act normal!"

    g "You're all such sim-"

    "???" "YEAH, YOU! DO YOU MIND COMING OVER HERE FOR A SEC!"

    #shock
    g"She cut me off."

    mc "Mc walks up to the booth"

    "???" "Hey, thanks for coming over!"

    "???" "I was wondering if you'd mind if you could help me out with something. "

    "???" "My name is Lynne, by the way."

    l "Anyways, I wanted to ask if you were willing to help me out with moving some stuff around. I know its kinda late, but my family just arrived."

    l "We'd be willing to compensate you, of course!"

    mc "Sure, why not!"

    g "You moron! You can't be staying out this late! The reapers- "

    mc "I SAID shush."

    l "Huh? Did you say something?"

    mc "No, I didn't say anything. Anyways, where's the stuff you need moved?"

    l "Oh, it's right over there."

    n"She points over to some boxes on the curb."

    l "And our house is right across the street from there. Sorry about it being kinda inconvient, it was a mistake on the mover's part."

    mc "It's fine, a bit of extra work never hurt anyone."

    n "For the next 30 minutes, Lynne, Mc, and Lynne's parents helped move the boxes across the street, and into their house."

    mc "I think that's the last of it."

    l "Yup, looks like it!"

    "Lynne's Mother" "Would you like to come in and eat with us? We got some food delivered while we were hauling in the stuff."
    
    mc "Sure, that sounds nice!"

    l "Alright, go wash up then. I'll get some stuff out so we can eat."

    mc "Thanks!"

    scene bg Bathroom with fade

    mc "Alright, time to wash my hands."

    g "You need to get home NOW."

    mc "What's this about? You yourself said that my life was stupid boring, and now here you are, raining on the first semi-interesting thing thats happened today."

    g "That's not why you need to head home, you dunce!"

    g "The reapers come out at midnight! If you don't start heading home soon, they'll chase us through the streets!"

    mc "And? I easily outran them the first time I had to deal with them."

    g "That was because I was still settling into your body! Now that I've been here for a whole day, they're going to be much more agressive!"

    mc "Stop fearmongering. Everything is gonna be fine."

    mc "This is the first good thing to happen to me in a while, and i'm not gonna let some stupid paranoid ghoul ruin it for me!"

    g "Please... Just listen to me. Just this once, mc."

    mc "I am not going to repeat myself. I am going to enjoy eating dinner with Lynne's family before I head home, and that's final."

    n "mc turns off the water, and dries his hands."

    mc "AND FOR THE FINAL TIME, STOP BOTHERING ME WHILE I'M AROUND OTHER PEOPLE!"
    #sadge
    g"....."
    scene bg DiningTable with fade
    mc "Alright, I'm ready to eat!"

    l "Alright, I'll bring out the food."

    "Lynne's Mother" "So, I'm assuming that you go to school around here?"

    mc "Yeah, I actually go to the school up the street from here. "

    mc "Its exam season right now, so I've beem studying nonstop actually"

    "Lynne's Father" "Oh, sorry for taking you away from your studies then."

    mc "Oh, you don't have to apologize. I needed a break from studying anyways."

    l "I got the food! Lets dig in!"
    # This ends the game.

    return
