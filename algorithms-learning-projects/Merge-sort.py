import matplotlib.pyplot as plt
import time

def merge_sort_with_plot(arr):
    """
    Performs merge sort on an array and visualizes the process
    using matplotlib.

    Args:
        arr (list): A list of numbers to be sorted.
    """
    n = len(arr)
    arr_copy = arr[:] # Work on a copy to preserve original if needed

    print(f"\nStarting merge sort for array: {arr_copy}")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Merge Sort Visualization", fontsize=16)
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.set_xticks(range(n))
    ax.set_ylim(min(arr_copy) - 5, max(arr_copy) + 5)

    def update_plot(current_arr, highlight_indices=None, status_message=""):
        """
        Updates the plot with the current state of the array and highlights.
        """
        ax.clear()
        ax.set_title(f"Merge Sort Visualization - {status_message}", fontsize=16)
        ax.set_xlabel("Index", fontsize=12)
        ax.set_ylabel("Value", fontsize=12)
        ax.set_xticks(range(n))
        ax.set_ylim(min(arr_copy) - 5, max(arr_copy) + 5)

        colors = ['skyblue'] * n # Default color

        if highlight_indices:
            for idx in highlight_indices:
                if 0 <= idx < n:
                    colors[idx] = 'orange' # Highlight elements being processed

        bars = ax.bar(range(n), current_arr, color=colors, edgecolor='black')

        for k, bar in enumerate(bars):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, current_arr[k],
                    ha='center', va='bottom', fontsize=10)

        plt.pause(0.5) # Pause for visualization

    def merge_sort_recursive(sub_arr, start_idx, end_idx):
        """
        Recursive function for merge sort with visualization.
        """
        if start_idx >= end_idx:
            return

        mid_idx = (start_idx + end_idx) // 2

        # Visualize splitting
        update_plot(arr_copy, list(range(start_idx, mid_idx + 1)), f"Splitting Left: {arr_copy[start_idx:mid_idx+1]}")
        update_plot(arr_copy, list(range(mid_idx + 1, end_idx + 1)), f"Splitting Right: {arr_copy[mid_idx+1:end_idx+1]}")
        time.sleep(0.5) # A small pause after showing both splits

        merge_sort_recursive(sub_arr, start_idx, mid_idx)
        merge_sort_recursive(sub_arr, mid_idx + 1, end_idx)

        # Merge step
        left_half = arr_copy[start_idx:mid_idx + 1]
        right_half = arr_copy[mid_idx + 1:end_idx + 1]

        i = j = 0
        k = start_idx

        # Visualize merging
        update_plot(arr_copy, list(range(start_idx, end_idx + 1)), f"Merging: {left_half} and {right_half}")
        time.sleep(0.5)

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr_copy[k] = left_half[i]
                i += 1
            else:
                arr_copy[k] = right_half[j]
                j += 1
            k += 1
            # Visualize element placement during merge
            update_plot(arr_copy, list(range(start_idx, k)), f"Merging: Placing {arr_copy[k-1]}")
            time.sleep(0.2) # Shorter pause for individual element placement

        while i < len(left_half):
            arr_copy[k] = left_half[i]
            i += 1
            k += 1
            update_plot(arr_copy, list(range(start_idx, k)), f"Merging: Placing remaining {arr_copy[k-1]}")
            time.sleep(0.2)

        while j < len(right_half):
            arr_copy[k] = right_half[j]
            j += 1
            k += 1
            update_plot(arr_copy, list(range(start_idx, k)), f"Merging: Placing remaining {arr_copy[k-1]}")
            time.sleep(0.2)

        # Final state after merge of this segment
        update_plot(arr_copy, list(range(start_idx, end_idx + 1)), f"Merged segment: {arr_copy[start_idx:end_idx+1]}")
        time.sleep(0.5)

    # Initial plot
    update_plot(arr_copy, status_message="Initial State")

    merge_sort_recursive(arr_copy, 0, n - 1)

    # Final plot for sorted array
    ax.clear()
    ax.set_title("Merge Sort: Array Sorted!", fontsize=18, color='green')
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
    unsorted_array_1 = [38, 27, 43, 3, 9, 82, 10]
    print("\n--- Merge Sort Example 1 ---")
    merge_sort_with_plot(unsorted_array_1)
    plt.close()

    unsorted_array_2 = [5, 1, 4, 2, 8]
    print("\n--- Merge Sort Example 2 ---")
    merge_sort_with_plot(unsorted_array_2)
    plt.close()

    unsorted_array_3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("\n--- Merge Sort Example 3 (Reverse Sorted) ---")
    merge_sort_with_plot(unsorted_array_3)
    plt.close()
