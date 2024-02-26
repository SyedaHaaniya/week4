class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.num_bids = 0
        self.highest_bid = 0

    def record_bid(self, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.num_bids += 1
            return True
        else:
            return False


def setup_auction():
    auction_items = []
    for i in range(10):
        print(f"\nItem {i+1}:")
        item_number = input("Enter item number: ")
        description = input("Enter item description: ")
        reserve_price = float(input("Enter reserve price: "))
        item = AuctionItem(item_number, description, reserve_price)
        auction_items.append(item)
    return auction_items


def buyer_bids(auction_items):
    while True:
        item_number = input("Enter item number you want to bid on (Enter 'q' to quit): ")
        if item_number.lower() == 'q':
            break
        item = next((item for item in auction_items if item.item_number == item_number), None)
        if item:
            print(f"Item Description: {item.description}")
            print(f"Current Highest Bid: {item.highest_bid}")
            buyer_number = input("Enter your buyer number: ")
            bid_amount = float(input("Enter your bid amount: "))
            if item.record_bid(bid_amount):
                print("Bid recorded successfully.")
            else:
                print("Your bid must be higher than the current highest bid.")
        else:
            print("Item not found.")


def end_of_auction(auction_items):
    total_fee = 0
    items_sold = 0
    items_not_meeting_reserve = 0
    items_with_no_bids = 0

    print("\nEnd of Auction Results:")
    for item in auction_items:
        if item.num_bids == 0:
            print(f"Item {item.item_number} received no bids.")
            items_with_no_bids += 1
        elif item.highest_bid >= item.reserve_price:
            print(f"Item {item.item_number} sold for ${item.highest_bid}.")
            total_fee += 0.1 * item.highest_bid
            items_sold += 1
        else:
            print(f"Item {item.item_number} did not meet reserve price. Final bid: ${item.highest_bid}.")
            items_not_meeting_reserve += 1

    print("\nTotal fee for all sold items:", total_fee)
    print("Number of items sold:", items_sold)
    print("Number of items that did not meet reserve price:", items_not_meeting_reserve)
    print("Number of items with no bids:", items_with_no_bids)


def main():
    print("Task 1: Auction setup")
    auction_items = setup_auction()

    print("\nTask 2: Buyer bids")
    buyer_bids(auction_items)

    print("\nTask 3: End of auction")
    end_of_auction(auction_items)


if __name__ == "__main__":
    main()
