from django.shortcuts import render
from polls.models import My_car
import joblib
def performance(request):
    mydata =  My_car.objects.all()
    khan = []
    
    for data in mydata:
        khan.append(data.Number_of_brakes)
    # print(khan)

    khang = list(map(int, khan))
    max_valuev = max(khang)
    min_valuev = min(khang)
    
    khang.reverse()
    print('This max valuen as :',max_valuev)
    print('This min valuen as :',min_valuev)
    print('The last element of list using reverse :', str(khang[0]))
    last_match = str(khang[0])
    
    # # check_this = str(khan[0])
    
    # # def checkType(a_list):
    # #     for element in a_list:
    # #         if isinstance(element, int):
    # #             print("It's an Integer")
    # #         if isinstance(element, str):
    # #             print("It's an string")
    # #         if isinstance(element, float):
    # #             print("It's an floating number")

    # # numbers = check_this
    # # checkType(numbers)


    # importing reduce()
    from functools import reduce

    def Average(lst):
        return reduce(lambda a, b: a + b, lst) / len(lst)

    # Driver Code
    lst = khang
    average = Average(lst)

    # Printing average of the list
    
    print("Average of the list =", round(average, 2))

    # Printing average of the list
    dic_content = {'max':max_valuev, 'min':min_valuev, 'avg':average, 'last_match':last_match}    
    return render(request, 'polls/performance.html', dic_content)  
    
