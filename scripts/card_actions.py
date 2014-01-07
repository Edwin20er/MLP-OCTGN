def playCard(card):
    action_modifiers = 0
	if card.type == "Friend":
		for c in table:		
			if c.targetedBy == me:		#Check to see if we have a card targeted
				if c.type == "Home":
					for d in table.home.me:                     # Check for modifiers to action costs.  Will have to be written later, but the framework is here.  
            													# Dunno yet if this is possible, but if table can have multiple groups of cards, 
					    										# we can iterate though all of the cards in a particular area to see if there are any modifiers.
                    if checkConditions(card, 0, 0) == 'true':   # For now we assume no mods to action/req cost, at least until we can see that everything else works.
   					    enterPlay(card, action_modifiers, x, y, table.home.me) # not sure about the syntax, but the ideas the important thing at this point. 
                                                                # x and y are as yet undefined, this is strictly to show that this can be moved to the correct spot on 
                                                                # the table once we know where that is.
					
			 		return
				if c.type == "Problem":                         
                    if c.owner == me:                           
                        # Here we get any effects, negative or positive that affect our playing friends to our problem.
                        for d in table.myProblem.me:
                            # Here we get any effects from any of our cards at this problem. 
                        for d in table.oppProblem.player(1):          
					        # Here we get any effects from any of our opponent's cards at this problem.
                        if checkConditions(card, 0, 0) == 'true':
                            enterPlay(card, action_modifiers, x, y, table.myProblem.me)
					
					return
		whisper("Please select a valid target for {}.".format(card.name))
		#Send Friend to a particular Problem or Home
		return
	elif card.type == "Resource":
		#Establish what the resource can target.  (Home, Problems, Friends, Troublemakers, other Resources, etc.)
		return
	elif card.type == "Event":
		#Establish what the resource can target.  (Home, Problems, Friends, Troublemakers, other Resources, etc.)
		return
	elif card.type == "Troublemaker":
		#Send troublemaker to a particular problem.
		return
	elif card.type == "Problem":
		#Send the card to your problem area to allow for the play of cards by yourself and opponents.
		return


def checkConditions(card, action_modifiers = 0, play_required_modifiers = 0):
	if me.counters[card.PlayRequiredElement] >= card.PlayRequiredPower:
		if me.counters['Actions'] >= card.cost:
			return 'true'
		else: 
	
