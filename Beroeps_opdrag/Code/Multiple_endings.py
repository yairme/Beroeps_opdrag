import time
import sys



# veriables

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nPLease use A, B, or C\n")
required_Y_N = ("\nPlease use Yes or No\n")

E = ("\nPress ENTER to continue...")

def cool_print(str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)


def Ending_print(str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.001)
    
def Dialog(text, choice_type):
    cool_print(text)
    time.sleep(1)
    if choice_type == "Multi":
        choice = input("\n>>> ")
        if choice in answer_A:
            return "A"
        elif choice in answer_B:
            return "B"
        elif choice in answer_C:
            return "C"
        else:
            print(required)
    elif choice_type == "Y/N":
        choice = input("\n>>> ")
        if choice in yes:
            return "yes"
        elif choice in no:
            return "no"
        else:
            print(required_Y_N)
            
            
            
def The_end():
    Ending_print("""
        ████████████████████████████      ████        ████      ████████████████  
    ████████████████████████████████  ████████    ████████  ████████████████████
    ░░████████████████████████████████  ████████    ████████  ████████████████████
    ░░████████████████████████████████  ████████    ████████  ██████████████████  
        ████████████████████████████    ████████    ████████  ██████████          
                ████████████            ████████    ████████  ██████████          
                ████████████            ████████    ████████  ██████████          
                ████████████            ████████████████████  ██████████████████  
                ████████████            ████████████████████  ████████████████████
                ████████████            ████████████████████  ████████████████████
                ████████████            ████████████████████  ██████████████████  
                ████████████            ████████████████████  ██████████          
                ████████████            ████████    ████████  ██████████          
                ████████████            ████████    ████████  ██████████          
                ████████████            ████████    ████████  ██████████████████  
                ████████████            ████████    ████████  ████████████████████
                ████████              ████████    ████████  ████████████████████
                                        ████        ████      ████████████████  
                                            ░░          ░░      ░░░░░░░░░░░░░░░░  
                                                                                
                                                                                
                                                                                
            ██████████████                                                        
        ██████████████████      ████            ████        ██████              
        ██████████████████    ████████        ████████    ██████████            
        ████████████████      ██████████      ████████    ████████████          
        ██████████            ████████████    ████████    ██████████████        
        ██████████            ██████████████  ████████    ██████  ████████      
        ████████████████      ████████████████████████    ██████  ████████      
        ██████████████████    ████████████████████████    ██████  ████████      
        ██████████████████    ████████████████████████    ██████  ████████      
        ████████████████      ████████████████████████    ██████  ████████      
        ██████████            ████████████████████████    ██████  ████████      
        ██████████            ██████████    ██████████    ██████  ████████      
        ████████████████      ████████        ████████    ██████████████        
        ██████████████████    ██████            ██████    ████████████          
        ██████████████████    ██████            ██████    ██████████            
        ████████████████        ████            ████      ████████              
                                                            ████      """)


def ending():
    cool_print("When I got to the Netherlands I was relieved to not be In Syria any more, but at the same time anxious what if they don’t let me stay? \nWhat if they send us back? But I knew there was no turning back, I had to take the risk, hope for them to let me stay.")
    input(E)
    cool_print("After getting there it took a month for my application to be accepted, but I was able to stay and live here in the Netherlands, it was a \ntraumatic experience, but I am glad I was able to share it with you all, hope you enjoyed reading it but now I have to go.")
    time.sleep(1)
    The_end()


History = Dialog("Are you ready to start.(Y)", "Y/N")
if History == "yes":
    cool_print("\rThe civil uprising phase of the Syrian Civil War, or as it was sometimes called by the media, the Syrian Revolution, was an early \nstage of protests – with subsequent violent reaction by the Syrian Arab Republic – lasting from March to 28 July 2011. The uprising, \ninitially demanding democratic reforms, evolved from initially minor protests, beginning as early as January 2011 and transformed \ninto massive protests in March.")
    input(E)
    cool_print("\rThe uprising was marked by massive anti-government opposition demonstrations against the Ba'athist government led by Bashar al-Assad, meeting \nwith police and military violence, massive arrests and a brutal crackdown, resulting in hundreds of deaths and thousands of wounded.")
    input(E)
    cool_print("\rDespite Bashar al-Assad's attempts to stop the protests with the massive crackdown and use of censorship on one hand and concessions on the \nother, by the end of April it became clear the situation was getting out of his control and his government deployed numerous troops on the \nground.")
    input(E)
    cool_print("\rThe civil uprising phase led to the emergence of militant opposition movements and massive defections from the Syrian Army, which \ngradually transformed the conflict from a civil uprising to an armed rebellion, and later a full-scale civil war. The rebel Free \nSyrian Army was created on 29 July 2011, marking the transition into armed insurgency.")
    input(E)
    cool_print("\rAs you can see our reasoning is valid, we had to leave I didn’t want to end up dead in a cell, besides I didn’t have much of an option, \na group of freedom fighters came to the prison I was held at, I was young at that time, I was one of the students that got arrested for making \npolitical graffiti, I don’t regret it one bit… but that’s besides the point, now I had to run with the group of freedom fighters to get me out \nof Syria, if I didn’t I would be dead.")
    time.sleep(1)
    Understand = Dialog("\nDo you understand our reasoning?", "Y/N")
    time.sleep(1)
    if Understand == "yes" or "no":
        cool_print("It doesn’t matter if you do or don’t, I had to run. That night I was so scared I was young I was shaking in fear of death, I didn’t want to lose my life, so I just kept running through the screams not looking back. There was one of the freedom fighters leading the way for me, her name was Liliana, but she said to call her Lily, she was kind she kept me calm as I was scared, that for sure I was at that moment I didn’t know what \nto do, I would have died without her help.")
        input(E)
        cool_print("Travelling through the streets at night was hard, but it was harder when there was gunshot everywhere, but following Lily helped to calm me down as we travelled. I was glad someone like her was helping me, I thought I would be able to get through this with her help… But… When we were \ncrossing the road there was a flash of light, it was really bright, the last thing I heard was to....")
        First_C = Dialog("\n[A]I heard to run. \n[B]I heard to take cover.", "Multi")
        time.sleep(1)
        if First_C == "A":
            cool_print("I hear the words run… so I did I had my arms on my face as I kept running straight into the alleyway, there was an explosion behind me, I didn’t hear it I felt the shock wave as I ran. I reached the hallway panting as I was exhausted, my heart rate pounded fast I couldn’t see anything, I \nleaned on a wall meanwhile my vision came back.")
            input(E)
            cool_print("When my eyesight was back I was able to look around, as I looked back at the street, I saw her… I saw Lily on the floor… I stood up and screamed as I was going to run to her, but I was held back by someone else, I was dragged away I didn’t want to leave her, but it was too late for her \nalready.")
            input(E)
            cool_print("My memory wasn’t the best I didn’t remember much of  what happened after that, that was a scar in my memory that will never erase. But I do \nremember I was at a base where they took me to a room where there was some stuff for me, food some tools and some clothes for me, I set them in a bag each some food in a bag with clothes and the tools in a separate bag with some clothes in that one as well.")
            input(E)
            cool_print("We staid in the shelter for a whole month before we got told what was the plan for us, we were supposed to get on a boat in a few days, but it \ndidn’t turn out as planned, as the hideout was found and was bombed and attacked in the panic they told us to run get out and run, but we did \nhave much time to grab supplies to go with…")
            time.sleep(1)
            Boat = Dialog("\n[A]Do I grab the bag with food? \n[B]Do I grab the bag with tools?", "Multi")
            time.sleep(1)
            if Boat == "A":
                cool_print("So I choose the bag of food it was the logical options, without food we couldn’t last long, so I choose it and started to run with the group. We moved through the country going up north, not able to take the boat as we were far from the water, we had to camp up there for a few months, it \nwasn't enjoyable the  cold of winter wasn’t easy to get through without the right clothing, luckily we had some extra food, it was smart to grab the bag.")
                input(E)
                cool_print("As the seasons passed we lost the track of the militia letting us travel back down to the water edge where we are able to get on the boat. \nIt was a nightmare on the boat as it was cramp there was no space for us to move, I was hell, but at least we still lived.")
                input(E)
                cool_print("We travelled for a few hours, it was difficult on to be kicked or slapped accidentally by the others as no-one could stay still for so long, it \nwas painful.")
                input(E)
                cool_print("But after a few hours we landed on the shore of France, where we got into trucks, we were split into groups. The way the hid us in the front of the \ntruck, with boxes and items in the back blocking us from view, it was pretty smart the way they hid us, but still it was cramp for a bit.")
                input(E)
                cool_print("After a while we reached Paris, where we caught a train, Oh yeah I forgot to say this, when I was in the camp I was told we were going to the \nNetherlands the said at the Netherlands they would understand our situation and let us get residency as fast as possible. So that’s where the \ntrain took us.")
                input(E)
                ending()
            elif Boat == "B":
                cool_print("So I choose the tools, I don’t know why I decided to choose that, but I did. When we had to run we travelled up north, trying to get away from \nthe militia as if they found out of the plan they had for us, we would never be able to escape. The planned for us to go on boat towards France, but after this attacked changed everything.")
                input(E)
                cool_print("When we were setting camp, up north my tools were useful in helping, but it didn’t do much more than that. We had to stay hidden for almost a \nyear as we lost the militia. The Winter was a hard time to pass, but luckily having my tool, someone was able to use them to make blankets for us and helps us get through the cold.")
                input(E)
                cool_print("By the time we were able to start to get back to the shore, our food ration were getting low as most of it was destroyed in the attack. We \ntravelled for a few hours on the boat, it was difficult on to be kicked or slapped accidentally by the others as no-one could stay still for so \nlong, it was painful. But after a few hours we landed on the shore of Italy.")
                input(E)
                cool_print("Where we had to find a job, we needed to get enough money to get on a plane and fly to the Netherlands, that was our goal as it was the only \nlocation where us, the runaways were accepted and given a home, it was the place where most people went after running away.")
                input(E)
                cool_print("After getting the money and a fake passport, oh yeah that was something I didn’t say, I needed to get a fake passport to be able to get on the \nplane, it was stressful as many of the fellow runaways were caught and sent to prison, but I got lucky I wasn’t stopped and I got through.")
                input(E)
                ending()
        elif First_C == "B":
            cool_print("At that moment I heard the shouts of someone saying to take cover, as I heard that I jumped down onto the ground, I didn’t know what was going \non I couldn’t see, I felt someone jump on me, almost as if they were covering me, an explosion was heard really close to us, a loud ringing noisewas in my ears. I was scared I didn’t know what I was doing, I felt a liquid drip on me, it was thick, I didn’t know what it was at that moment.")
            input(E)
            cool_print("After a little the ringing stopped as I was gaining my sight, I got out from under the person that was on me as I realized, it was Lily, she… \nshe was dead, she sacrificed herself to protect me. I held her close, tears started to run down my eyes as I didn’t want to accept that she was \ndead, she helped me a lot, it might not of been a long time I knew her, but she did a lot for me.")
            input(E)
            cool_print("Not long after someone ran up to us… me and grabbed me, I tried to not let go of Lily, I didn’t want to let go, but I was forced to. We ran for \na while that night, I don’t remember much I do remember I was a wreck, seeing how Lily died for me, I will never forget that not even a second ofit.")
            input(E)
            cool_print("I do remember reaching an abandon train station, it was the place we stayed there for a few days, waiting for the militia to stop looking for us.In that time I overheard that a different group of the refugees were attacked delaying their travel.")
            input(E)
            cool_print("One day a train was brought to the station, I didn’t know where it came from, but hell I didn’t care it was our ticket out of here, I didn’t wantto be in the hellhole of Syria any more. When we got on we were separated in different cars, having us hidden well enough that no-one could see \nus, but that left us with the only light being the roof light, I was lucky I was set in a cart with one of those, some carts didn’t, can’t \nimagine travelling so long in a dark room not able to see anything or anyone.")
            input(E)
            cool_print("After a few days of travel, we reached Pollen, where they told us we had to get off or risk being caught in Germany.")
            time.sleep(1)
            Train = Dialog("\n[A]Do I get off the train? \n[B]Do I risk it?", "Multi")
            time.sleep(1)
            if Train == "A":
                cool_print("Because I didn’t want to risk being caught, I choose to get off at Pollen, where we got directed to a bus, where it was a normal method of \ntransportation, lucky for us the fair wasn’t that expensive, and we were able to get off a bus into a new bus reaching to our destination.")
                input(E)
                cool_print("The travel wasn’t much, but we did get an update that the ones that were on the train were locked up and send to prison, I was lucky I decided toget off, it might have been longer travel to the Netherlands but better than being locked up and send back to Syria")
                input(E)
                ending()
            elif Train == "B":
                cool_print("I didn’t want to wait much more, I needed to get to the Netherlands, so I choose to stay on the train and risk it…")
                input(E)
                cool_print("I regret that decision, we travelled for a while before we got stopped getting all the train carts checked, we were caught and send to prison, itwas hard being in prison, we had to stay in there for six months.")
                input(E)
                cool_print("In those six months I feared for my life, I never knew when someone was going to try and kill me, or maybe poison my food, it was a \nterrible experience I never want to go back into prison, never again.")
                input(E)
                cool_print("But we were lucky, at least they didn’t send us back to Syria, I was let go with the only condition being we needed to leave the country in a \ncertain amount of time, so I did, I found myself transport to the Netherlands, it wasn’t easy but I did.")
                input(E)
                ending()
elif History == "no":
    The_end()

        

