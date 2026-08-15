# CLI Card Dealer & Deck Simulator

A Python command-line utility that constructs, shuffles, and deals playing cards from a standard 52-card deck. Features robust user input validation and dynamic deck tracking to report remaining card counts post-deal.

## Technical Highlights

* **Procedural Deck Generation:** Constructs a complete 52-card deck using nested iterations over custom rank and suit data structures.
* **In-Place Randomization:** Utilizes Python's `random.shuffle()` algorithm to ensure unbiased sequence distribution before dealing.
* **Input Bounds Checking:** Implements a state-managed input loop with integer conversion and range enforcement ($1 \le N \le 52$) to prevent array index out-of-bounds exceptions.
* **Dynamic Inventory Tracking:** Computes real-time remaining deck counts post-draw using list length evaluations (`len(deck) - num_cards`).

## Technical Requirements

* **Python Version:** Built using pure standard Python 3.x (uses built-in `random` module—zero external `pip` dependencies required).

## Usage

```bash
python main.py
