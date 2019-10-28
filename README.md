
# PizzaHive

_ _Pizza ordering website inspired by [pinnochio's](http://www.pinocchiospizza.net/menu.html) pizza and subs menu_ _
__My understanding of the menu__

_ _Since the menu was somehow complicated this is what I understood from it_ _

- Toppings can only be applied to specific items (Pizzas and Subs)
- Some Subs do not go with toppings except the steak and cheese sub which allows three types of toppings
- Customers cannot select more than three toppings
- Not all items have sizes like small or large

### Models

#### Item

__Has attributes:__

- name: The item's name
- category : The category it belongs to
- image
- has_size: Boolean value - true if the item has small and large sizes false if it has only one size
- has_topping: Boolean Value - true if toppings can be applied to that item
  
#### Sub

_ _Sub is also an item but I decided to make it a separate model because it has one extra field_ _:available_toppings_ _
__Has attributes:__

- name : Char
- image
- has_topping: Boolean - True if that sub has available toppings in this case there is only one sub that accepts toppings
- available_toppings_comma: List of toppings applicable separated by a comma
- price_small: price of the small version
- price_large: Price of the large Version

#### Topping

_ _All toppings_ _
__Has attributes:__

- name

#### Orders

_ _All toppings_ _
__Has attributes:__

- username: Username of the person who ordered
- name: Customer's full name
- items: items ordered
- total: how much the items cost

### Where am I getting the prices

_ _Oh they are in a separate model, with foreign keys pointing to the item they represent_ _

### Personal Touches

- A page to manage orders only visible to staff or super users aka admins
- Orders can be deleted from both admin end and customer end
- Images for every menu item
- Customers cannot select more than 3 toppings
- Cart dictionary clears automatically after order is placed
- Simple UI
