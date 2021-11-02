#!/usr/bin/python3

## Problem 4 : A Toy AD implementation
class AutoDiffToy():

    def __init__(self,val, der = 1):
        self.val = val
        self.der = der
        
    def __mul__(self, other):
        #ry:
        value = self.val * other.val  # must do the value
        der = self.der * other.val + self.val * other.der # chain rule
        # except AttributeError:
        #     value = self.val * other # when you don't store the values
        #     der = self.der * other
        return AutoDiffToy(value,der)   # need to return the attributes so that the instance is updated
    
    def __rmul__(self, other):
        return self.__mul__(other) #to get the other order
    
    def __add__(self, other):
        #try:
        value = self.val + other.val
        der = self.der + other.der
        # except AttributeError:
        #     value = self.val + other
        #     der = self.der + 0
        return AutoDiffToy(value,der)

    
    def __radd__(self, other):
        return self.__add__(other)  #to get the other order

    def __pow__(self, other):
        #try:
        value  = self.val ** other.val
        der = other.val * self.val **(other.val - 1)
        # except AttributeError:
        #     value = self.val + other
        #     der = other * self.val **(other - 1)
        return AutoDiffToy(value, der)
        
    
    
    def __str__(self):
        s = f"Value: {self.val}"
        if hasattr(self, "der"):
            s += f", Derivative of f: {self.der}"
        return s

# How to do the sin/cos case
# add if statements for the different instances
# only did it here
    def sin(self, other):
        if isinstance(other,float) or isinstance(other, int):
            value = np.sin(other)
            der = np.cos(other)
        elif isinstance(other,dual):  # need to create the dual class
            value  = np.sin(self.val)
            # need to do chain rule
            der = np.cos(self.val)*self.der
        return AutoDiffToy(value, der)


# How to do the sin/cos case
    def cos(self):
        value  = np.cos(self.val)
        der = -1* np.sin(self.val)*self.der
        return AutoDiffToy(value, der)


    


        
