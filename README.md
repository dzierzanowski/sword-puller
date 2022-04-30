# Sword Puller

The video game "[The one who pulls out the sword will be crowned king](https://store.steampowered.com/app/1865370/The_one_who_pulls_out_the_sword_will_be_crowned_king/)"
is a fun, brainless time waster, which requires nothing more of you than to hold LMB
and move the mouse up, resulting in an abnormal wear of your mouse switch and
mousepad surface, as well as minor loss of your brain cells.

To prevent damages to equipment and gray tissue, while still receiving
the achievements, you may use this handy tool, which will do the work
for you.

## Requirements
- Python 3
- `pip install pynput`

## Usage
Clone this repository and run program in the console with `python run.py`, then switch to the game.

Point at the sword and press `P` to pull it up.

Once you're done, press `P` again to stop the pull.

Switch back to the terminal and press `Ctrl+C` to exit.

## Troubleshooting
If you drop the sword early, exit the program. Edit `run.py` and slightly
decrease numbers in lines 11 and 12, save the file and try again.

To reset to default values, run `git reset --hard origin/master` in the repo.

## Caution
The `P` hotkey will function outside the game as well, possibly messing your
things up. Exit program before typing anything.
