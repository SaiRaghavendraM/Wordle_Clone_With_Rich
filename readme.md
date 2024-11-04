
# Word Guessing Game

A simple, interactive word-guessing game built in Python. The program challenges players to guess a randomly selected word within a limited number of tries. Feedback is provided on each guess, showing correct letters in the correct positions and highlighting misplaced letters.

## Features

- **Random Word Selection**: Selects a random word from a list for each game.
- **Feedback on Guesses**: Displays correct letters and positions using color-coded hints.
- **Console-based UI**: Enhanced with the `rich` library for an engaging experience.

## Requirements

- Python 3.x
- [rich](https://pypi.org/project/rich/) (for colorful console output)

Install dependencies with:
```bash
pip install rich
```

## Usage

1. Prepare a `wordlist.txt` file containing potential words for the game (one word per line).
2. Run the game:
   ```bash
   python word_game.py
   ```
3. Follow the prompts to guess the word within the allowed attempts.

## File Structure

- **word_game.py**: Main game logic.
- **wordlist.txt**: List of words used in the game.

## Example

```plaintext
Guess 1
_____
Guess word: APPLE
*Feedback on guess is displayed here*
```

## License

This project is open-source and available under the MIT License