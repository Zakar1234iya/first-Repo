var allPizza = [];
function pizzaOven(sauce, cheese, toppings, vegetable, finish) {
    var pizza = {};
    pizza.sauce = sauce;
    pizza.cheese = cheese;
    pizza.toppings = toppings;
    pizza.vegetable = vegetable;
    pizza.finish =  finish;
    allPizza.push(pizza)
    return pizza 
}



var buffalo_pizza = pizzaOven("buffalo_sace","mozzarella","buffalo_chicken","none","ranch");
console.log(buffalo_pizza);

var mushroom_pizza = pizzaOven("mushroom_sauce",["mozzarella","gouda"],"none","mushroom",["parmesaan","chives"]);
console.log(mushroom_pizza);

var pepperoni_pizza = pizzaOven("marinara", "mozzarella", "pepperoni", "mushroom", "parmessan")
console.log (pepperoni_pizza)

var pepperoni_pizza = pizzaOven("marinara", "mozzarella", "none", ["mushroom","olive","onion","cherry_tomato"], "olive_oil")
console.log (pepperoni_pizza);





console.log(allPizza)


/*function getrandomPizza() {
    let sauces = ["none", "marinara", "mushrrom_sauce", "garlic_sauce", "buffalo_sauce"] ;
    let randomSauce = sauces[Math.floor(sauces.length * Math.random())];
    let cheese = ["none", "mozzarella", "cheddar", "gouda", ] ;
    let randomcheese = cheese[Math.floor(cheese.length * Math.random())];
    let toppings =["none", "pepperoni", "salami", "sausage", "buffalo_chicken", "chicken","beef", "shawarma"];
    let randomtoppings = toppings[Math.floor(toppings.length * Math.random())];
    let vegetable =["none", "olive", "kalamata_olive", "onion", "red-onion","mushroom", "arguala" , "pepper", "spinach"];
    let randomvegetable = vegetable[Math.floor(vegetable.length * Math.random())];
    let finish = ["none", "olive_oil", "parmessan", "blue_cheese", "basil","feta_cheese", "chives" ,"parsely" ,"ranch"];
    let randomfinish = finish[Math.floor(finish.length * Math.random())];
    let pizza = [randomSauce, randomcheese, randomtoppings, randomvegetable,randomfinish];
    console.log(pizza);
    return pizza 
}*/


//getrandomPizza();
//getrandomPizza();
//getrandomPizza();

