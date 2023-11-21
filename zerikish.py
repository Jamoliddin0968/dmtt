def first_fit_decreasing(bin_size, items):
    items.sort(reverse=True)  # Sort items in descending order

    bins = [[]]  # Initialize the first bin
    for item in items:
        for bin in bins:
            if sum(bin) + item <= bin_size:  # Check if the item fits in the current bin
                bin.append(item)
                break
        else:
            # If the item doesn't fit in any bin, start a new bin
            bins.append([item])

    return bins


# Example usage:
bin_capacity = 10
pieces_to_cut = [4, 5, 6, 3, 2, 7, 5, 3]

result = first_fit_decreasing(bin_capacity, pieces_to_cut)

# Display the result
print("Bins:")
for index, bin_content in enumerate(result):
    print(f"Bin {index + 1}: {bin_content}")
