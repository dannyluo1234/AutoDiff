### Introduction
​    Differentiation is a giant part of mathematics, engineering, and computer science. It is important to have a systematic way to solve complex differentiation problems through the use of software instead of doing it by hand, which our Automatic Differentiation package works to accomplish. Automatic Differentiation (AD) is a series of computational techniques to evaluate the derivatives of functions that are specified for computers. AD can be completed either using the fast-forward method, which we will be implementing, or the reverse method. The overall goal of AD is to numerically differentiate a function through the use of point values and formulas, in order to get a numerical value that does not have any approximation error. The fast forward method divides a complex function into a series of elementary derivatives that eventually build up to the final function.
​    Our library will provide clients the ability to run fast-forward Automatic differentiation as well as another expansion. This package contains all the necessary dependencies that a client will need as well as any documentation to help correctly utilize the program. It also contains mathematical background information in case any clients are not familiar with calculations that are used in AD. This package will be available through PyPI and can be easily downloaded through the website pypi.org

#### Background

​    Automatic differentiation relies on the fundamental building block of calculus, which is the chain rule. A derivative essentially captures the rate of change of a function with respect to a variable and the chain rule states that for three variables x, y and z, knowing the rate of change of x with respect to y (dx/dy) and y with respect to z (dy/dz) allows us to calculate the rate of change of x with respect to z as the product of the two rates of changes dx/dy and dy/dz. In other words, dx/dz = (dx/dy)(dy/dz). We can generalize this to an arbitrary number of variables and dimensions with the gradient operator.

​    There is a certain ordering associated with the chain rule, where the derivative of the outermost function can be obtained if you evaluate the derivatives of the nested functions from inside out. These intermediate results can be stored as nodes of a graph, which we call the computational graph. For instance, the input to the innermost function can be considered as x and placed at the left end of the graph and the ordering of differentiation operations (as part of the chain rule) can be visualised as the order of the nodes following x, until we reach the final node on the right which will be the final derivative we are seeking.

​     This constructs the graph in the forward direction from the input x to the derivative of our function f. The reverse mode encompasses the construction of this graph in the opposite direction. The intermediate results we obtain are defined as dependent variables while the original coordinates we begin with (in our case x, which is a vector) are called independent variables. This is because we differentiate with respect to our independent variables, to find the rate of change of the dependent variables.Thus, we can conclude that the forward mode computes the gradient of the function f with respect to the independent variable by traversing forward and the reverse mode computes the sensitivity of the function f with respect to both independent and dependent variables by traversing backward.

#### How to use cs107-creativename

​    The user will use `pip` to install the package. When users install the package, its dependencies will automatically be added as well so that the only thing that the user needs to import is our library (similar to how numpy is a dependency of pandas, but users only need to `import pandas` to use all of its functionality).
​    To instantiate an AD object, the user will just call the AD function within the library with the function to be differentiated. By passing in additional optional methods, the user can customize the AD process. After creating the differentiated function, the user can then call this function with the value to be evaluated in the form of a Variable class within our library. For example, a typical use case can look like this:

<img width="623" alt="Screen Shot 2021-11-02 at 1 32 34 PM" src="https://user-images.githubusercontent.com/89878381/139916239-c6ae447f-3ccb-4d6f-b77d-71a6f0c24257.png">



#### Software Organization

​    The overall structure will have multiple levels that all read from a main program that performs the AD process. There will be separate pathways that will solve different mathematical derivatives (i.e. separating derivatives of exponentials and trigonometric ones). We will include multiple packages that are loaded into the program that the client will have access to when downloading our library. The two main modules that we will have is a Dual class and our fast forward auto differentiation. The Dual class will be used to represent complex numbers that can be entered into our auto differentiation function. The auto differentiation function implements a forward mode auto differentiation by taking advantage of the chain rule.Our program will be tested live using both TravisCI and CodeCov, and those tests can be seen on the software’s GitHub. The software can also be downloaded from PyPi.org. We do not plan to use a framework to package our program. 
Here is what the structure of our program will look like:

<img width="361" alt="Screen Shot 2021-11-02 at 1 33 00 PM" src="https://user-images.githubusercontent.com/89878381/139916322-8401d920-e278-4b2c-b774-eef25fed85a9.png">




#### Implementation

​    The core data structure is the dual number. It will have its own rule of addition, multiplication, etc. We will implement a class called “dual” to realize this dual data structure. We will also implement the main function for Forward mode which will utilize the dual class. The dual class will have functions like __add__, __mul__, __sub__, __truediv__, __pow__ to overload the elementary operators. We will also have functions like, sin, cos which we use instead of the default math library functions. We will rely on functions and methods in packages, such as NumPy and math. We can use NumPy and math to evaluate the true value and value of the derivative for each node in our AD process. For example, we can use np.cos to evaluate a cosine function that is given as well as use it to evaluate the derivative if a sine function is give. Since there are no dunder methods designed for those math functions, we will write them in our dual class and ask the user to use our function instead of the ones in math or numpy. Within the dual class, we will implement functions; such as sin, sqrt, log, exp, etc. which will take in function arguments of type dual or float and return the corresponding evaluated value.

The computational graph will tentatively be implemented as an adjacency list, wherein each node has a value and points to the next node in the graph. We will implement two functions, which add vertices and edges to the graph, respectively. We intend to store the entire computational graph in memory for the duration of the Forward mode differentiation.  

#### License

​    For the license of our project, we decided to go with the MIT License. We want the fruit of our labor to be able to help the work of others and potentially contribute to bigger and better projects, commercial or not. But in the meantime, we definitely do not want to be held liable for continuing the service of the software. We believe the MIT license allows us to do both.





-------------------------------------------------------------------------------------------------------------------------------
### Feedback
What will the directory structure look like?
What modules do you plan on including? What is their basic functionality?

Modules: 
Dual class: a custom class capable of representing complex numbers to be entered into our autodiff functions
Forward mode auto differentiating: a module that implements forward mode auto differentiation by taking advantage of the chain rule. 


<img width="361" alt="Screen Shot 2021-11-02 at 1 33 00 PM" src="https://user-images.githubusercontent.com/89878381/139916322-8401d920-e278-4b2c-b774-eef25fed85a9.png">

