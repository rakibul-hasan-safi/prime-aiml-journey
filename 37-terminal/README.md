# 37 · Terminal

Moving around and managing files from the command line instead of Finder. This is the groundwork for Git (Section 38), pip, and running Python scripts.

No code in this section; it's all commands. The cheat sheet below is the part worth keeping.

## Lessons · 11 videos · 51 min

| # | Lesson | Length |
|---|--------|--------|
| 1 | What will we learn? | 01:44 |
| 2 | What is the Terminal? | 04:42 |
| 3 | Different Terms related to Terminal | 05:48 |
| 4 | (Windows Users Only) Installing Git Bash | 02:46 |
| 5 | Basic Commands | 05:25 |
| 6 | Navigation Commands | 05:57 |
| 7 | Paths in Navigation | 04:43 |
| 8 | Making Directories | 04:35 |
| 9 | What are Flags? | 06:47 |
| 10 | Touch Command | 02:37 |
| 11 | Deleting Files & Folders | 06:14 |

## Key terms

| Term | Meaning |
|------|---------|
| Terminal | The window/app where you type commands |
| Shell | The program that runs those commands (zsh on macOS, bash on most Linux servers) |
| CLI vs GUI | Typing commands vs clicking windows |
| Flag | Changes how a command behaves, e.g. `ls -l` |
| Git Bash | A bash terminal for Windows (not needed on Mac) |

## Cheat sheet

| Task | Command |
|------|---------|
| Where am I? | `pwd` |
| What's here? | `ls` · `ls -la` (including hidden files) |
| Go into a folder | `cd name` |
| Go up one / two levels | `cd ..` · `cd ../..` |
| Go home | `cd ~` |
| Back to the previous folder | `cd -` |
| New folder(s) | `mkdir name` · `mkdir -p a/b/c` |
| New file | `touch file.txt` |
| Delete a file | `rm file.txt` |
| Delete an empty folder | `rmdir name` |
| Delete a folder and its contents | `rm -rf name` ⚠️ |
| Manual for a command | `man ls` (press `q` to quit) |
| Clear the screen | `clear` · Cmd + K |
| Open this folder in Finder / VS Code | `open .` · `code .` |

## Paths

- **Absolute** paths start at the root: `/Users/rhs/Desktop/Python`. They work from anywhere.
- **Relative** paths start from where you are: `Desktop/Python`, `../notes`.
- `~` = home, `.` = current folder, `..` = parent folder.
- Names with spaces need quotes: `cd "Apna College"`, or let Tab-completion escape them.

## Flags

```bash
ls -l    # long format: permissions, owner, size, date, name
ls -a    # all files, including hidden ones like .git and .gitignore
ls -la   # both; flags can be stacked
```

## Things to remember

- `rmdir` only removes **empty** folders and fails with `Directory not empty` otherwise.
- `rm` and `rm -rf` **don't use the Trash** and can't be undone. Run `pwd` and `ls` before deleting.
- **Tab** autocompletes names, **↑** recalls earlier commands, and **Ctrl + C** stops a running program.
