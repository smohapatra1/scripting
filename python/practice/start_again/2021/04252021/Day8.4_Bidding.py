#Bidding program 

bidding_finished = False
bids= {}
def biddings(record_bid):
    highest_bid = 0 
    winner=""
    for bidders in record_bid:
        bid_amount=record_bid[bidders]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidders 
    print (f"Higest bidder is {winner} and price is {price}")

while not bidding_finished:
    name=input("Enter bidder name: ")
    price = int(input("Enter your bidding price: $ "))
    bids[name] = price
    should_continue = input("Are there more bidders, 'yes' or 'no' ?")
    if should_continue == "no":
        bidding_finished = True
        biddings(bids)
    elif should_continue == "yes":
        print ("Bidder done")