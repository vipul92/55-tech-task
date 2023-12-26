## 55-tech-task

#### Problem Statement
Let’s implement the code for a supermarket checkout that calculates the total price of a number of items.
An item has the following attributes:
- SKU
- Unit Price

Our goods are priced individually. Some items are multi-priced: buy n of them, and they’ll cost
you less than buying them individually. For example, item ‘A’ might cost $50 individually, but this
week we have a special offer: buy three ‘A’s and they’ll cost you $130.
Here is an example of prices:
SKU Unit Price Special Price
- A $50 3 for $130
- B $30 2 for $45
- C $20
- D $15

Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll
recognize the two B’s and price them at 45 (for a total price so far of 95). Because the pricing
changes frequently, we need to be able to pass in a set of pricing rules each time we start
handling a checkout transaction.

The interface to the checkout should look like:

co = new CheckOut(pricing_rules);
co.scan(item);
co.scan(item);
price = co.total();

#### Assumption
For simplicity of the application, pricing rules is assumed to be a dictionary having key: `sku`, `price` and `quantity`.
In code, rules are being added using `rule_json` which is a list of dictionaries. `rule_json` can also be populated by taking input from user interactively.
Example Price Rules:
```
{
    "A": 50,
    "AAA": 130,
    "B": 30,
    "BB": 45,
    "C": 20,
    "D": 15
}
```

#### Execution
To start the application, execute the `main.py` file
`python main.py`

Now enter the SKU you want to scan or press enter to finish adding products.
Please note that the SKUs are case sensitive and will not be accounted for if pricing rules does not have them.

After you finish added products, the total price will be displayed.
![image](https://github.com/vipul92/55-tech-task/assets/23123259/519bcbda-9e36-4ddf-b298-9e73923a843c)

