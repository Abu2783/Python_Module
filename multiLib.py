class multiLib():
    def Subfields():
        print("Sub-fields in AI are: ")
        message = "Sub-fields in AI are: "
        print("Machine Learning")
        message = "Machine Learning: "
        print("Neural Networks")
        message = "Neural Networks: "
        print("Vision")
        message = "Vision: "
        print("Robotics")
        message = "Robotics: "
        print("Speech Processing")
        message = "Speech Processing: "
        print("Natural Language Processing")
        message = "Natural Language Processing: "
        return message

    def OddEven():
        num=int(input("Enter the number : "))
        if((num%2)==1):
            print(num, end=" is Odd number\n")
            message = " is Odd number\n"
        else:
            print(num, end="is Even number")
            message = " is Even number\n"
            return message

    def Elegible():
        str1=str(input("Your gender :"))
        age=int(input("Your age :"))
        if(str1=="Male"):
                if(age<25):
                    print("You are not eligible")
                    message = " You are not eligible\n"
                else:
                    print("You are eligible")
                    message = " You are eligible\n"
        elif(str1=="Female"):
                   if(age<21):
                        print("You are not eligible")
                        message = " You are eligible\n"
                   else:
                        print("You are eligible")
                        message = " You are not eligible\n"

    def percentage():
            sub1=int(input("Subject1 :"))
            sub2=int(input("Subject2 :"))
            sub3=int(input("Subject3 :"))
            sub4=int(input("Subject4 :"))
            sub5=int(input("Subject5 :"))
            total = sub1+sub2+sub3+sub4+sub5
            print("Total : ",total)
            per = total/5
            print("Percentage : ",per)

    def triangle():
            h=int(input("Height :"))
            b=int(input("Breadth :"))
            print("Area formula: (Height*Breadth)/2")
            str =(h*b)/2
            print("Area of Triangle: ", str)
            h1=int(input("Height1 :"))
            h2=int(input("Height2 :"))
            b1=int(input("Breadth :"))
            print("Perimeter formula: Height1+Height2+Breadth")
            str1 =(h1+h2+b1)
            print("Perimeter of Triangle: ", str1)
       