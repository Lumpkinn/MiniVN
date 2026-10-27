#TODO: REPLACE ALL INSTANCES OF MC WITH THE CHARACTER'S NAME!!!!

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#if you ever wanna try out that tales thing, feel free to use this! https://www.renpy.org/doc/html/quickstart.html#positions


#you can change font color of text here using "color=#<Color in hex here>"
define e = Character("Eileen")

define mc = Character("MC")

define g = character ("Spirit")

define N = Character("Narrator", color="#508f20")
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



    mc "alright, lets go take a look then... \n It's not like i'd be able to get "
    # This ends the game.

    return
