            #JAVA STYLE
# class Rectangle :
#     def __init__(self,width, height):
#         self.set_width(width)
#         self.set_height(height)
    # def getWidth(self):
    #     return self.__width
    
    # def getHeight(self):
    #     return self.__height
    
    # def set_width(self, width):
    #     self.__width = width
    
    # def set_height(self, height):
    #     self.__height = height
# a = Rectangle(10,20)
# a.set_width(40) #set new width
# print(a.getWidth()) #getvalue in getWidth
    
            #PYTHON STYLE
        #getter
    # @property
    # def set_width(self): 
    #     return self._width
    # @property
    # def set_height(self):
    #     return self._height
    
    #setter
    # @set_width.setter 
    # def set_width(self, width):
        # self._width = width
    # @set_height.setter
    # def set_height(self, height):
    #     self._height = height
class Rectangle :
    def __init__(self,width, height):
        self.set_width(width)
        self.set_height(height)

    def __repr__(self):
        return "{}(width={}, height={})".format(self.__class__.__name__,self._width,self._height) 


    def set_width(self, width):
        self._width = width
        
    def set_height(self, height):
        self._height = height
    
    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return 2 * self._width + 2* self._height
    
    def get_diagonal(self):
        return (self._width **2 + self._height **2) ** .5
    
    def get_picture(self):
        picture =""
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        else:
            for line in range(self._height):
                picture += "*" * self._width +"\n"
            return picture
    
    def get_amount_inside(self , shape):
        amount_inside = (self._width//shape._width) * (self._height//shape._height)
        if amount_inside < 1: 
            return 0
        return int(amount_inside)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)
        
    
    def __repr__(self):
        return "{}(side={})".format(self.__class__.__name__,self._width) 
    
    def set_side(self, side):
        self._height = side
        self._width = side
        
        


if __name__ == "__main__":
    s = Square(3)
    s.set_side(5)
    print(s)