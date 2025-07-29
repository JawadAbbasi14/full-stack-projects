
import matplotlib.pyplot as plt
import time

def binary_search_with_plot(arr, target):
    """
    Performs binary search on a sorted array and visualizes the process
    using matplotlib.

    Args:
        arr (list): A sorted list of numbers.
        target (int): The number to search for.
    """
    low = 0
    high = len(arr) - 1
    found_index = -1

    print(f"Starting binary search for target: {target} in array: {arr}")

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"Binary Search Visualization (Target: {target})", fontsize=16)
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.set_xticks(range(len(arr)))
    ax.set_ylim(min(arr) - 5, max(arr) + 5) # Adjust y-axis limits for better visualization

    # Function to update the plot
    def update_plot(current_low, current_high, current_mid, status_message=""):
        ax.clear() # Clear previous plot
        ax.set_title(f"Binary Search Visualization (Target: {target}) - {status_message}", fontsize=16)
        ax.set_xlabel("Index", fontsize=12)
        ax.set_ylabel("Value", fontsize=12)
        ax.set_xticks(range(len(arr)))
        ax.set_ylim(min(arr) - 5, max(arr) + 5)

        colors = ['skyblue'] * len(arr) # Default color for all elements

        # Highlight the current search range
        for i in range(current_low, current_high + 1):
            if i >= 0 and i < len(arr):
                colors[i] = 'lightgreen' # Color for elements in current range

        # Highlight low, high, and mid pointers
        if current_low >= 0 and current_low < len(arr):
            colors[current_low] = 'blue' # Low pointer
            ax.text(current_low, arr[current_low] + 2, 'Low', ha='center', color='blue', fontsize=10, fontweight='bold')
        if current_high >= 0 and current_high < len(arr):
            colors[current_high] = 'red' # High pointer
            ax.text(current_high, arr[current_high] + 2, 'High', ha='center', color='red', fontsize=10, fontweight='bold')
        if current_mid >= 0 and current_mid < len(arr):
            colors[current_mid] = 'orange' # Mid pointer
            ax.text(current_mid, arr[current_mid] + 2, 'Mid', ha='center', color='orange', fontsize=10, fontweight='bold')

        # Plot the bars
        bars = ax.bar(range(len(arr)), arr, color=colors, edgecolor='black')

        # Add value labels on top of bars
        for i, bar in enumerate(bars):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, arr[i],
                    ha='center', va='bottom', fontsize=10)

        plt.pause(1.5) # Pause for 1.5 seconds to visualize each step

    # Initial plot
    update_plot(low, high, -1, "Initial State")

    while low <= high:
        mid = low + (high - low) // 2 # Calculate mid to prevent overflow for very large arrays

        # Update plot before comparison
        update_plot(low, high, mid, f"Comparing {arr[mid]} with {target}")

        if arr[mid] == target:
            found_index = mid
            # Final plot for found element
            colors = ['skyblue'] * len(arr)
            colors[found_index] = 'lime' # Bright green for found element
            ax.clear()
            ax.set_title(f"Target {target} Found at Index {found_index}!", fontsize=18, color='green')
            ax.set_xlabel("Index", fontsize=12)
            ax.set_ylabel("Value", fontsize=12)
            ax.set_xticks(range(len(arr)))
            ax.set_ylim(min(arr) - 5, max(arr) + 5)
            bars = ax.bar(range(len(arr)), arr, color=colors, edgecolor='black')
            for i, bar in enumerate(bars):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, arr[i],
                        ha='center', va='bottom', fontsize=10)
            plt.pause(2)
            plt.show(block=False) # Keep plot open but allow script to continue
            print(f"Target {target} found at index {found_index}")
            return found_index
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target}. Moving to right half.")
            low = mid + 1
        else:
            print(f"{arr[mid]} > {target}. Moving to left half.")
            high = mid - 1

    # If target is not found
    ax.clear()
    ax.set_title(f"Target {target} Not Found!", fontsize=18, color='red')
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.set_xticks(range(len(arr)))
    ax.set_ylim(min(arr) - 5, max(arr) + 5)
    ax.bar(range(len(arr)), arr, color='lightgray', edgecolor='black')
    for i, val in enumerate(arr):
        ax.text(i, val + 0.5, val, ha='center', va='bottom', fontsize=10)
    plt.pause(2)
    plt.show(block=False)
    print(f"Target {target} not found in the array.")
    return -1

# Example Usage:
if __name__ == "__main__":
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    print("\n--- Searching for 23 ---")
    binary_search_with_plot(sorted_array, 23)
    plt.close() # Close the plot after the search

    print("\n--- Searching for 72 ---")
    binary_search_with_plot(sorted_array, 72)
    plt.close()

    print("\n--- Searching for 100 (not in array) ---")
    binary_search_with_plot(sorted_array, 100)
    plt.close()

    print("\n--- Searching for 2 (first element) ---")
    binary_search_with_plot(sorted_array, 2)
    plt.close()

    print("\n--- Searching for 91 (last element) ---")
    binary_search_with_plot(sorted_array, 91)
    plt.close()
