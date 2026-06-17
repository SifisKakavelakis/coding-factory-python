def main():
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Watermelons"}
    store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Melons"}

    # Find common products (intersection) available in both stores
    common_products = store_a_products & store_b_products
    print("Products available in both Store A and B:", common_products)

    common_products_2 = store_a_products.intersection(store_b_products)
    print("Products available in both Store A and B:", common_products)

    # Find all unique products (union) across both stores
    all_products = store_a_products | store_b_products
    print("All unique products across Store A and Store B:", all_products)

    all_products_2 = store_a_products.union(store_b_products)
    print("All unique products across Store A and Store B:", all_products_2)

    # Find products available in Store A but not in Store B (difference)
    store_a_exclusive = store_a_products - store_a_exclusive
    print("Products available only in Store A:", store_a_exclusive)

    store_a_exclusive_2 = store_a_products.difference(store_b_products)
    print("Products available only in Store A:", store_a_exclusive)

    # Find products available in Store B but in Store A (difference)
    store_b_exclusive = store_b_products - store_a_products
    store_b_exclusive_2 = store_b_products.difference(store_a_products)

    # Find products that are in either Store A or Store B but not in both (symetric differnce)
    unique_to_either_store = store_a_products ^ store_b_products
    print("Products available in either Store A or Store B but not in both:", unique_to_either_store)

    unique_to_either_store_2 = store_a_products.symmetric_difference(store_b_products)
    print("Products available in either Store A or Store B but not in both:", unique_to_either_store)

if __name__ == "__main__":
    main()