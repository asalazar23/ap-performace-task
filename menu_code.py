def menu_function(main_items, side_items, topping_items):
  total_price = [1]
  first_choice = input(f"Welcome! Please decide what you would like to order and we will calculate the final price. What would you like as your main dish? Your options are: {main_items}.\n").lower()
  print(total_price)
  second_choice = input(f"What would you like as a side? Your options are: {side_items}.").lower()
  third_choice = input(f"What would you like as a topping? Your options are: {topping_items}.").lower()

  if first_choice == 'steak': 
    total_price.insert(0, 12)
    
  elif first_choice == 'chicken':
    pass
  elif first_choice == 'lamb':
    pass
  elif first_choice == 'salmon':
    pass
  elif first_choice == 'salmon':
    pass
  elif first_choice == 'pork':
    pass


  if second_choice == 'fried potatoes':
    pass
  elif second_choice == 'mashed potatoes':
    pass
  elif second_choice == 'salad':
    pass
  elif second_choice == 'soup':
    pass
  

  if third_choice == 'hot sauce':
    pass
  if third_choice == 'lemon butter sauce':
    pass
  if third_choice == 'red wine sauce':
    pass

  # topping_items = ['hot sauce', 'lemon butter sauce', 'red wine sauce']

