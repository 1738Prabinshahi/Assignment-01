height =float (input('enter your height in meter: '))
weight =float( input ('enter your weight in kg: '))

def BMI(height, weight):
    bmi= weight/(height**2)
    if( bmi<18.5):
        return 'Underweight',bmi
    elif (bmi>=18.5 and bmi<=24.9):
      return 'Normal',bmi
    elif (bmi>=25 and bmi<=29.9):
     return 'Overweight',bmi
    elif (bmi>=30):
      return 'Obesity',bmi
prabin,bmi=BMI(height,weight)
print('your bmi is :{} and you are:{}' .format (bmi,prabin))







