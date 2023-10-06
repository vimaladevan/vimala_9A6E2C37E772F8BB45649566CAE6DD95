'''Implement a class called player that represents a cricket player . The player class  should have a method called play{} which prints " player is playing cricket.Derive  two classes,Batsman and Bowler, from the prayer class.override the play() method in each dervied class to print "The batsman is batting "and "The bowler is blowiny", respectively.write a program to create objects of both the Batsman and Bowler classes and call the play () method for each objects.'''


#Define the bese class player
class player:

  def play (self):
    print ("The player is playing cricket.")


#Define the derived class Batsman 
class Batsman (player ):

  def play(self):
    print ("The bowler is bowling.") 


#Define the dervied class Bowler
class Bowler(player ):

   def play (self):
     print ("The bowler is bowling.")


#create objects of Batsman and Bowler classes 
batsman=Batsman()
bowler= Bowler ()
#call the play () method for each object 
batsman.play()
bowler.play()