import random

print ("\nYou failed to achieve your goal(s) today. How disappointing.\nAs punishment, you must...\n")

Punishment_Choice = random.randint(1,20)
	
def punishment_generator():
	if Punishment_Choice == 1:
		print ("Wash all the dishes in the apartment for seven days.")
	elif Punishment_Choice == 2:
		print ("Run 4 miles. Send photo to confirm with other party.")
	elif Punishment_Choice == 3:
		print ("Not consume boba for seven days.")
	elif Punishment_Choice == 4:
		print ("Wear business attire for the day. If people ask why, you must reply, 'I feel professional.' No mention of the punishment is allowed while wearing professional attire.")
	elif Punishment_Choice == 5:
		print ("Buy a snack for everyone in the apartment. You have to watch everyone eat. Taunting is allowed.")
	elif Punishment_Choice == 6:
		print ("Wall-sit for 2 minute daily for seven days. Other person must confirm they are done.")
	elif Punishment_Choice == 7:
		print ("Do 20 jumping jacks before using the bathroom for seven days. If you ever get caught forgetting, you have to add 10 push-ups.")
	elif Punishment_Choice == 8:
		print ("Make both beds for seven days.")
	elif Punishment_Choice == 9:
		print ("Not use your cellphone in the apartment for a day, unless special circumstances arise.")
	elif Punishment_Choice == 10:
		print ("Send a really stupid Snapchat to 10 people of the other person's choosing. No mercy.")
	elif Punishment_Choice == 11:
		print ("Allow your roommate to style your hair however she pleases.")
	elif Punishment_Choice == 12:
		print ("Serve as your roommate's errand girl for one request.")
	elif Punishment_Choice == 13:
		print ("Wear a shirt inside out or backwards for the whole day. Must be obvious.")
	elif Punishment_Choice == 14:
		print ("Finish your readings in the bathroom. You may only leave if you're done/other people need to use the bathroom.")
	elif Punishment_Choice == 15:
		print ("Not wear makeup for seven days (Aileen); Wear makeup for seven days (Audrey). The works - eyeliner, eyeshadow, mascara.")
	elif Punishment_Choice == 16:
		print ("Allow your roommate to dress you for the day.")
	elif Punishment_Choice == 17:
		print ("Set your Facebook profile picture to a photo of the roommate's choosing.")
	else:
		print ("Do nothing. Lucky you.")

a = punishment_generator()

print ("\nTry to achieve your goal(s) next time!\n")


#If you fail to complete your punishment within 3 days of issue, you must contribute
#$20 to the "Apartment Fund." You may only retrieve your $20 if you commit to your daily goals
#for seven consecutive days following the payment.

#EFFECTIVE 9/11/2013