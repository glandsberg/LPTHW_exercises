# Learning to speak Object-Oriented

	

| command       | meaning       |
| ------------- |:-------------:|
| class      | tells python to  make a new type of thing |
| object      | two meanings - the most basic type of thing, and any instance of some thing      |
| instance | what you get when you tell python to create a class      |
| def	| how you define a function inside a class 	|
| self  | inside the functions in a class, self is a variable for the instance/object being accessed |
| inheritance 	| the concept that one class can inherit traits from another class, much like you and your parents 	|
| composition 	| the concept that a class can be composed of other classes as parts, much like how a car has wheels 	|
| attribute 	| a property classes have that are from composition and are usually variables 	|
| is-a	| a phrase to say that something inherits from another, as in a "salmon" is-a "fish." 	|
| has-a	| a phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mouth."	|



"""
These are python code snippets on the left, and then English sentences for them on the right:

"""
| code snippet      | meaning       |
| ------------- |:-------------:|
| classX(Y)	| "make a class named X that is-a Y."	|
| classX(object): def__init__(self,J)	| "class X has-a___init__ that takes self and J parameters" 	|
| classX(object): def M(self, J)	| "class X has-a function named M that takes self and J parameters."	|
| foo = X() 	| "set foo to an instance of class X."	|
| foo.M(J) 	| "from foo, get the M function, and call it with parameters self, J."	|
|foo.K = Q 	| "from foo, get the K attribute, and set it to Q."	|
