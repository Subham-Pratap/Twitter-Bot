import tweepy
import time
import random
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.


#Add your credentials here
twitter_keys = {
        'consumer_key':        'CEqmTRHa8BBdLideH1yH3QC6t',
        'consumer_secret':     'ouTXmEFz525M2opT8XJ7VYCNnRDH2Zq1emCCBc2ChQ27GvL8pZ',
        'access_token_key':    '1249597456993509378-1cFJLqd2l4cA2HTLJOKXfGP3l9A0zq',
        'access_token_secret': 'mc6pNz8eIegKSYAG5In384f3dLxloiRwrAjAfzPUrnPw5'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth, wait_on_rate_limit=True)

listt = ["You’re my favorite person besides every other person I’ve ever met.", 
         "No offense, but you make me want to staple my cunt shut.", 
         "I envy people who have never met you.",
         "Maybe if you eat all that makeup you will be beautiful on the inside.",
         "You’re kinda like Rapunzel except instead of letting down your hair, you let down everyone in your life.",
         "You’re impossible to underestimate.",
         "You’re not the dumbest person on the planet, but you sure better hope he doesn’t die.",
         "I’ll plant a mango tree in your mother’s cunt and fuck your sister in its shade.",
         "Those aren’t acne scars, those are marks from the coat hanger.",
         "You have more dick in your personality than you do in your pants.",
        "If you were an inanimate object, you’d be a participation trophy.",
        "You look like your father would be disappointed in you if he stayed.",
        "You’re not pretty enough to be that dumb.",
        "Your mother fucks for bricks so she can build your sister a whorehouse.",
         "I’m sorry your dad beat you instead of cancer.",
        "You were birthed out your mother’s ass because her cunt was too busy.",
        "You’re so stupid you couldn’t pour piss out of a boot if the directions were written on the heel.",
        "Take my lowest priority and put yourself beneath it.",
        "Such a shame your mother didn’t swallow you.",
        "The best part of you ran down your mom’s leg.",
        "You couldn’t organize a blowjob if you were in a Nevada brothel with a pocket full of hundred-dollar bills.",
        "You are a pizza burn on the roof of the world’s mouth.",
        "Does your ass ever get jealous of the shit that comes out of your mouth?",
        "People like you are the reason God doesn’t talk to us anymore.",
        "You’re so dense, light bends around you.",
        "I’d love to stay and chat but I’d rather have type-2 diabetes.",
        "You should put a condom on your head, because if you’re going to act like a dick you better dress like one, too.",
        "I bet you swim with a T-shirt on.",
        "How the fuck are you the sperm that won?",
"May your balls turn square and fester at the corners.",
"I hope your wife brings a date to your funeral.",
"If you were a potato you’d be a stupid potato.",
"Your face looks like it was set on fire and put out with chains.",
"You might want to get a colonoscopy for all that butthurt.",
"Your mother may have told you that you could be anything you wanted, but a douchebag wasn’t what she meant.",
"You are so ugly that when you were born, the doctor slapped your mother.",
"You look like two pounds of shit in a one-pound bag.",
"Ready to fail like your dad’s condom?",
"I’d call you a cunt, but you have neither the warmth or the depth.",
"If I wanted to commit suicide I’d climb to your ego and jump to your IQ.",
"You make me wish I had more middle fingers." ,
"If genius skips a generation, your children will be brilliant.",
"Everyone that has ever said they love you was wrong." ,
"You have the charm and charisma of a burning orphanage." ,
"If there was a single intelligent thought in your head it would have died from loneliness."
"I don’t have the time or the crayons to explain this to you.",
"The only difference between you and Hitler is Hitler knew when to kill himself." ,
"You’re dumber than I tell people." ,
"I hope you have beautiful children and that they all get cancer." ,        
"Your birth certificate is an apology letter from the condom factory." ,
"For years your mother and I wanted kids. Imagine our disappointment when you came along." ,
"Your face is so oily that I’m surprised America hasn’t invaded yet." ,
"Your father should’ve wiped you on the sheets." ,       
"If I wanted any shit out of you I’d take my dick out of your ass." ,
"I can explain it to you, but I can’t understand it for you." ,
"You’re the reason you mom swallows now." ,
"How did you crawl out of the abortion bucket?",
"If the road were paved with dicks, your mother would walk on her ass." ,
"You are the stone in the shoes of humanity." ,
"You could fuck up a wet dream." ,
"You’re not as dumb as you look.",
"Son, anyone who would fuck you ain’t worth fucking." ,
"This is why everyone talks about you as soon as you leave the room." ,
"The smartest thing that ever came out of your mouth was my dick."
"You know, people were right about you.",
"You’ve got a great body. Too bad there’s no workout routine for a face." ,        
"If you could suck your own dick then you would finally suck at everything." ,        
"I want you to be the pallbearer at my funeral so you can let me down one last time." ,
"Don’t make me have to smack the extra chromosome out of you.",
"You’ve gotta be two people, because no single person can be that stupid.",
"If you were any dumber, someone would have to water you twice a week." ,
"You’ll never be half the man your mother was." ,
"If you were on fire and I had a cup of my own piss, I’d drink it." ,
"I’ve forgotten more than you know.",
"You smell like you wipe back to front.",
"I could agree with you, but then we’d both be wrong." ,
"Shut your mouth, I can smell your Dad’s cock.",
"You look like something I drew with my left hand.",
"How do you even masturbate knowing whose dick you’re touching?"
"You are the human embodiment of an eight-dollar haircut."
"The only thing that will ever fuck you is life.",
"You suck dick at fucking pussy.",
"If you were twice as smart, you’d still be stupid. I can’t forget that day.",
"You look like a bag of mashed-up assholes.",
"You’re a huge bag of tiny cocks." ,
"You’re so inbred you’re a sandwich.",
"In a country where anyone can be anything, I will never understand why you chose to be mediocre." ,
"What’s a girl like you doing at a nice place like this?",
"You’re about as important as a white crayon.",
"Was your mother just in the bathroom? Because she forgot to flush your twin." ,
"If my dog had a face like you, I’d paint his ass and teach him to walk backwards." ,
"If your parents were to divorce, would they still be brother and sister?" ,
"You look like the kind of person that buys condoms on his way to a family reunion.",
"People will not only remember your death, they will celebrate it." ,
"You are a shit stain on the underpants of society." ,
"You look like you were poured into your clothes but someone forgot to say when to stop.",
"You’re about as useful as tits on a pigeon.",
"Why are you playing hard to get when you’re so hard to want?" ,
"I’d offer you a shit sandwich, but I hear you don’t like bread. TC mark" ]


FILE_NAME = 'haha.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = (f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return





#Make call on home timeline, print each tweets text
mentions = api.mentions_timeline()
for x in mentions:
    print(str(x.id)+ '  '+ x.text)
    
    
def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
   
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'insult' in mention.full_text.lower():
            print('found', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name + ' ' +
                    random.choice(listt), mention.id)
            
while True:
    reply_to_tweets()
    time.sleep(60)

