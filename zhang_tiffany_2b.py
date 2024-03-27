print('It’s a warm, sunny morning, you decide to take a walk with your dog at a nearby park. As you continue on your walk, you stumble upon a hidden path tucked behind the bushes.\n')

answer1 = input('Would you like to take the hidden path? yes/no ')

if answer1 == 'yes':
    print('\nYou hear shuffling from nearby, and your dog starts to whimper. It turns out there is a deer and her fawn drinking water from the stream.')
    answer2 = input('\nWould you like to observe the deer and her fawn and or continue on the path? (continue/observe) ')
    if answer2 == 'continue':
        print('\nThe beauty of the path makes you smile. You reach a cave with a captivating blue aura, the light draws you in. ')
        answer3 = input('\nWould you want to enter the cave? (yes/no) ')
        if answer3 == 'yes':
            print('\nYou enter the cave and the air feels cooler. You see a steaming, hot spring with lily pads and water fountains. Your dog excitedly jumps in and you’re stunned by how the day went as you enjoy the spring.')
        else:
            print('\nYou quickly walk away from the cave and speed walk towards the path exit. You feel chills down your spine but can’t help but wonder what was in that cave as you leave the park.')
    else:
        print('\nYour dog sits patiently with you as you watch the deer interact. However, you start to feel itchy, there may be mosquitoes biting.')
        answer3 = input('\nWould you want to go back to the path? (yes/no) ')
        if answer3 == 'yes':
            print('\nYou feel itchy and gross as you continue on the path towards the park. You decide to go home and give your dog a bath, and notice that your bug bites are getting itchier and more swollen. Bummer.')
        else:
            print('\nYou withstand the itchiness and continue to observe the scenery. You hear ruffling nearby and suddenly a fox leaps out and attacks the fawn. You gasp in horror and flee the scene with your dog.')

else:
    print('\nYou ignore the path and continue on your walk. As you pass by other people who are also on their morning walk, you notice an ice cream truck parked by the kids playground.')
    answer2 = input('\nWould you like to get some ice cream? (yes/no) ')
    if answer2 == 'yes':
        print('\nYou purchase an ice cream from the truck. Then you go to the playground, and a kid wants to pet your dog.')
        answer3 = input('\nWould you let the kid pet your dog? (yes/no) ')
        if answer3 == 'yes':
            print("\nYou have successfully made someone's day better. You return home to cook lunch and feed your dog.")
        else:
            print('\nThe kid turns away with a slight frown on his face. You return home with a heavy feeling in your chest, wondering if the rest of the day will go well.')
    else:
        print('\nYou walk away from the ice cream truck. You notice a dog park in the distance filled with small dogs, perfect playmates for your dog.')
        answer2 = input('\nWould you take your dog to the dog park? (yes/no) ')
        if answer2 == 'yes':
            print('\nYou enter through the dog park gates and unleash your dog. He runs around playing with the other dogs with a big smile on his face, which makes your morning.')
        else: 
            print('\nOut of the corner of your eye, you notice your friend Alexa reading a book under a tree.')
            answer3 = input('\nWould you approach Alexa? (yes/no) ')
            if answer3 == 'yes':
                print('\nYou tap Alexa on the shoulder and engage in conversation with her, telling a few jokes here and there. You decide to make plans for next week and then return home for the day.')
            else:
                print('\nYou decide not to interrupt Alexa and continue on your walk. You stumble upon another group of friends who call you over and you join them for their picnic.')
            
