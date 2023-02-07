def menu_function(main_items, side_items, topping_items):
  choice = "yes"
  while choice == "yes":
    list = []
    first_choice = input(f"Welcome! Please decide what you would like to order and we will calculate the final price. What would you like as your main dish? Your options are: {main_items}.\n").lower()
    
    second_choice = input(f"What would you like as a side? Your options are: {side_items}., or none.\n").lower()
    third_choice = input(f"What would you like as a topping? Your options are: {topping_items}, or none.\n").lower()
  
    if first_choice == 'steak': 
      list.append(15)
    elif first_choice == 'chicken':
      list.append(10)
    elif first_choice == 'lamb':
      list.append(17)
    elif first_choice == 'salmon':
      list.append(7)
    elif first_choice == 'pork':
      list.append(7)
    else:
      print("Please enter a valid option")
      first_choice()
      
  
  
    if second_choice == 'fried potatoes':
      list.append(5)
    elif second_choice == 'mashed potatoes':
      list.append(3)
    elif second_choice == 'salad':
      list.append(7)
    elif second_choice == 'soup':
      list.append(6)
    elif second_choice == "none":
      list.append(0)
    else:
      print("Please enter a valid option")
  
    if third_choice == 'hot sauce':
      list.append(3)
    elif third_choice == 'lemon butter sauce':
      list.append(3)
    elif third_choice == 'red wine sauce':
      list.append(5)
    elif third_choice == 'none':
      list.append(0)
    else:
      print("Please enter a valid option")
    final_price = sum(list)
    print(f"Your final price is ${final_price}, thank you for choosing us!")
    choice = input("Would you like to order something else? (yes/no)").lower()
    if choice == yes:
      menu_function(main_items, side_items, topping_items):