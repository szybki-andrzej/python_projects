
class Fraction:
    
    def __init__(self, num, dem):
        """Initializing function."""
        self.num = num
        self.dem = dem
        self.fraction = self.reduction()

    def nwd(self,a,b):
        """Returns the the greatest common divisor."""
        if b > 0:
            return self.nwd(b, a%b)
        return a

    def nww(self,a,b):
        """Returns the smallest commmon multiplicity."""
        return (a*b)/self.nwd(a,b)

    def reduction(self):
        """Reduct the fraction to simplest form."""
        if self.dem == 0:
            raise ValueError("You can't divide by 0.")

        elif type(self.num)!=int or type(self.dem)!=int:
            raise ValueError("Use only integer numbers.")
        
        elif self.dem > 0 and self.num >= 0:
            nwd = self.nwd(self.num,self.dem)
            self.num = int(self.num/nwd)
            self.dem = int(self.dem/nwd)
            return self.num,self.dem
        elif self.dem < 0 and self.num <= 0:
            nwd = self.nwd(-self.num,-self.dem)
            self.num = int(-self.num/nwd)
            self.dem = int(-self.dem/nwd)
            return self.num,self.dem
        elif self.dem > 0 and self.num <= 0:
            nwd = self.nwd(-self.num,self.dem)
            self.num = int(self.num/nwd)
            self.dem = int(self.dem/nwd)
            return self.num,self.dem
        elif self.dem < 0 and self.num >= 0:
            nwd = self.nwd(self.num,-self.dem)
            self.num = int(-self.num/nwd)
            self.dem = int(-self.dem/nwd)
            return self.num,self.dem

    def __str__(self):
        """Makes fraction's representation."""
        return str(self.num) + "/" + str(self.dem)

    def __add__(self,other):
        """Makes addition formula."""
        nww = self.nww(self.dem,other.dem)
        num1 = (nww/self.dem)*self.num
        num2 = (nww/other.dem)*other.num
        return Fraction(int(num1+num2),int(nww))
        
    def __sub__(self,other):
        """Makes subtraction formula."""
        nww = self.nww(self.dem,other.dem)
        num1 = (nww/self.dem)*self.num
        num2 = (nww/other.dem)*other.num
        return Fraction(int(num1-num2),int(nww))

    def __mul__(self, other):
        """Makes multiplication formula."""
        return Fraction(int(self.num*other.num),int(self.dem*other.dem))

    def __truediv__(self,other):
        """Makes division formula."""
        return Fraction(int(self.num*other.dem),int(self.dem*other.num))
    
    def __lt__(self,other):
        """Supports the "<" operator."""
        nww = self.nww(self.dem,other.dem)
        cou1 = (nww/self.dem)*self.num
        cou2 = (nww/other.dem)*other.num
        return cou1<cou2

    def __gt__(self,other):
        """Supports the ">" operator."""
        nww = self.nww(self.dem,other.dem)
        cou1 = (nww/self.dem)*self.num
        cou2 = (nww/other.dem)*other.num
        return cou1>cou2

    def __le__(self,other):
        """Supports the "<=" operator."""
        nww = self.nww(self.dem,other.dem)
        cou1 = (nww/self.dem)*self.num
        cou2 = (nww/other.dem)*other.num
        return cou1<=cou2

    def __ge__(self,other):
        """Supports the ">=" operator."""
        nww = self.nww(self.dem,other.dem)
        cou1 = (nww/self.dem)*self.num
        cou2 = (nww/other.dem)*other.num
        return cou1>=cou2

    def __eq__ (self,other):
        """Supports the "==" operator."""
        nww = self.nww(self.dem,other.dem)
        cou1 = (nww/self.dem)*self.num
        cou2 = (nww/other.dem)*other.num
        return cou1==cou2

    def __ne__(self,other):
        """Supports the "!=" operator."""
        nww = self.nww(self.dem,other.dem)
        cou1 = (nww/self.dem)*self.num
        cou2 = (nww/other.dem)*other.num
        return cou1!=cou2

    def getNum(self):
        """Returns the numerator of the fraction."""
        return self.num

    def getDem(self):
        """Returns the denominator of the fraction."""
        return self.dem


def main():
    a = Fraction(-6, -3)
    b = Fraction(14, 18)
    c = Fraction(7, -3)
    d = Fraction(-7, 14)
    print(a)
    print(b)
    print(c)
    print(d)
    print(a+b)
    print(a+c)
    print(a*b)
    print(c-d)
    print(c/d)
    print(c == d)
    print(c < a)
    print(a.getNum())
    print(b.getDem())


if __name__ == "__main__":
    main()