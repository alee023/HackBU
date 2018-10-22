def getCharMap( string ) :
    string_dict = {}
    for c in string:
        if c in string_dict :
            string_dict[c] += 1
        else:
            string_dict[c] = 1

    return( string_dict ) 

# print( getCharMap( "Hello" ))

'''
OPTIONAL INPUTS
def fxnname( num = 4 ) : <=== an actual number

    this will take any input the user provides, but if none is given, will use 4
'''


'''
Classes group your data with possible actions it may perform '''


# is self like "this" in java? => YES!
'''
unlike java, the variables dont have to put before the init function. think of
init as a constructor
'''
class Student :
    def __init__( self, name: str, b_number: str, major: str, position: str) -> None :
        self.name = name
        # etc, etc...
        self.position = position
        self.go_to_class( position )

    def go_to_class(self, class_location: str) -> None :
        self.position = class_location


tom = Student( "Tom", "B1001001", "CS", "EB G7" )
print( tom.position )
tom.go_to_class( "Fine Arts 212" )
print( tom.position )


class Dog :
    def __init__( self, name: str, breed: str, yrOB: int ) -> None :
        self.name = name
        self.breed = breed
        self.yrOB = yrOB

    def bark( self ) :
        print( "Woof" )

aDog = Dog( "Barky", "lab", 2000 )
aDog.bark()
