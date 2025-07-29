# Python Binary Search Visualizer

A Python implementation of binary search algorithm with matplotlib visualization for educational purposes.

## Overview

This tool visualizes the binary search algorithm step-by-step using matplotlib, showing how the algorithm efficiently finds elements in sorted arrays through divide-and-conquer approach.

## Features

- Real-time visualization of binary search process
- Color-coded elements showing current search range
- Visual pointers for Low, High, and Mid positions
- Step-by-step console output
- Multiple test cases included

## Requirements

```bash
pip install matplotlib
```

## Usage

```python
from binary_search_visualizer import binary_search_with_plot

# Example usage
sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
result = binary_search_with_plot(sorted_array, 23)
```

## Running the Examples

```bash
python binary_search_visualizer.py
```

This will run 5 different search scenarios:
- Searching for 23 (middle element)
- Searching for 72 (right side)
- Searching for 100 (not found)
- Searching for 2 (first element)
- Searching for 91 (last element)

## Algorithm Details

**Time Complexity**: O(log n)
**Space Complexity**: O(1)

The visualization shows:
- **Blue bars**: Low pointer position
- **Red bars**: High pointer position  
- **Orange bars**: Mid pointer (current comparison)
- **Light green**: Current search range
- **Lime**: Found element

## Color Coding

| Color | Meaning |
|-------|---------|
| Sky Blue | Default elements |
| Light Green | Current search range |
| Blue | Low pointer |
| Red | High pointer |
| Orange | Mid pointer |
| Lime | Found element |
| Light Gray | Not found state |

## Customization

You can modify the visualization timing by changing the pause duration:

```python
plt.pause(1.5)  # Change to desired seconds
```

## Educational Use

Perfect for:
- Learning binary search algorithm
- Understanding time complexity
- Visualizing divide-and-conquer approach
- Algorithm comparison studies

## Author

**Jawad Abbasi**
- Email: jawadabbasi1107@gmail.com
- GitHub: [@JawadAbbasi14](https://github.com/JawadAbbasi14)

## License

MIT License - see LICENSE file for details.
