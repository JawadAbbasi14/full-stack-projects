
import matplotlib.pyplot as plt
import time

def bubble_sort_with_plot(arr):
    """
    Performs bubble sort on an array and visualizes the process
    using matplotlib.

    Args:
        arr (list): A list of numbers to be sorted.
    """
    n = len(arr)
    arr_copy = arr[:] # Work on a copy to preserve original if needed

    print(f"\nStarting bubble sort for array: {arr_copy}")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Bubble Sort Visualization", fontsize=16)
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.set_xticks(range(n))
    ax.set_ylim(min(arr_copy) - 5, max(arr_copy) + 5)

    def update_sort_plot(current_arr, i_idx=-1, j_idx=-1, status_message=""):
        ax.clear()
        ax.set_title(f"Bubble Sort Visualization - {status_message}", fontsize=16)
        ax.set_xlabel("Index", fontsize=12)
        ax.set_ylabel("Value", fontsize=12)
        ax.set_xticks(range(n))
        ax.set_ylim(min(arr_copy) - 5, max(arr_copy) + 5)

        colors = ['skyblue'] * n

        # Highlight elements being compared/swapped
        if i_idx != -1:
            # This highlights the section that is already sorted or the boundary of the unsorted part
            # For bubble sort, elements from n-1 down to n-1-i are sorted and stay in place.
            # So, n-1-i marks the last unsorted element's potential position.
            for k in range(n - i_idx, n): # Elements already in their final sorted position
                 colors[k] = 'lightgray' # Indicate sorted portion
            colors[n - 1 - (i_idx)] = 'purple' # The element that's being 'bubbled' to its place

        if j_idx != -1:
            colors[j_idx] = 'orange' # Current element in inner loop
            if j_idx + 1 < n:
                colors[j_idx + 1] = 'red' # Element being compared with j_idx

        bars = ax.bar(range(n), current_arr, color=colors, edgecolor='black')

        for k, bar in enumerate(bars):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, current_arr[k],
                    ha='center', va='bottom', fontsize=10)

        plt.pause(0.5) # Shorter pause for sorting steps

    # Initial plot
    update_sort_plot(arr_copy, status_message="Initial State")

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            update_sort_plot(arr_copy, i_idx=i, j_idx=j, status_message=f"Pass {i+1}: Comparing {arr_copy[j]} and {arr_copy[j+1]}")
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                swapped = True
                update_sort_plot(arr_copy, i_idx=i, j_idx=j, status_message=f"Pass {i+1}: Swapped {arr_copy[j+1]} and {arr_copy[j]}")
        if not swapped:
            break # Optimization: if no two elements were swapped by inner loop, array is sorted

    # Final plot for sorted array
    ax.clear()
    ax.set_title("Bubble Sort: Array Sorted!", fontsize=18, color='green')
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.set_xticks(range(n))
    ax.set_ylim(min(arr_copy) - 5, max(arr_copy) + 5)
    bars = ax.bar(range(n), arr_copy, color='lime', edgecolor='black')
    for k, bar in enumerate(bars):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, arr_copy[k],
                ha='center', va='bottom', fontsize=10)
    plt.pause(2)
    plt.show(block=False)
    print(f"Sorted array: {arr_copy}")
    return arr_copy

# Example Usage:
if __name__ == "__main__":
    # --- Bubble Sort Examples ---
    unsorted_array_1 = [64, 34, 25, 12, 22, 11, 90]
    print("\n--- Bubble Sort Example 1 ---")
    bubble_sort_with_plot(unsorted_array_1)
    plt.close()

    unsorted_array_2 = [5, 1, 4, 2, 8]
    print("\n--- Bubble Sort Example 2 ---")
    bubble_sort_with_plot(unsorted_array_2)
    plt.close()

    unsorted_array_3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("\n--- Bubble Sort Example 3 (Reverse Sorted) ---")
    bubble_sort_with_plot(unsorted_array_3)
    plt.close()
