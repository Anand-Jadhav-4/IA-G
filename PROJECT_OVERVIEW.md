# Project Overview: IA-G ("Interesting Code - for Fun")

## What is this project?

`IA-G` is a community-style, open-source **collection of small, unrelated code snippets and mini projects** written for fun and learning. It is not a single application. There is no build system, no package manifest, and no shared entry point. Each file is standalone.

- Upstream repo: https://github.com/akasumitlamba/IA-G
- Workspace location: `c:\GIT\GITHubTest\IA-G`
- Languages: Python (majority), HTML/CSS/JavaScript, C++, Jupyter notebooks, one Windows batch file
- Stated purpose: let anyone share interesting snippets, experiments or small projects (the repo is Hacktoberfest-friendly)

## Folder structure

```
GITHubTest/
├── PROJECT_OVERVIEW.md      <- this file
└── IA-G/                    <- flat folder, ~89 files, no subfolders
    ├── README.md, contributing.md, CodeOfConduct.md
    ├── leetcode*.py         (53 LeetCode solutions)
    ├── *.html               (browser mini-apps/pages)
    ├── *.py                 (games, utilities, NLP, crypto)
    ├── *.cpp                (algorithm snippets)
    ├── *.ipynb              (notebooks)
    └── open.bat, Number Quest output.jpg
```

## Contents by category

### 1. LeetCode solutions (largest group, 53 files)
Python solutions named `leetcode_<n>.py` or `leetcode<n>.py`. Each usually has the problem title or statement in a docstring or comment, then a `class Solution`.

| Group | Example problems |
|---|---|
| Classic (older) | 41 First Missing Positive, 42-60 range (Trapping Rain Water, Permutations, N-Queens, Spiral Matrix, Merge Intervals, Permutation Sequence...), 145, 407, 417, 564, 590, 592, 664, 778, 947, 992 |
| Mid-range | 1488, 1514, 1518, 1716, 2011, 2040, 2081, 2138, 2200, 2273, 2300, 2311 |
| Recent | 3085, 3100, 3147, 3289, 3321, 3347, 3397, 3443, 3461, 3539, 3607 (Power Grid Maintenance) |

Related algorithm files:
- `uniqueOccurence.py`: check whether each element's occurrence count is unique, without built-ins
- `sortedlist.py`: sorted-list exercise
- `Maximize_Array Value_After_Rearrangement.py`: array rearrangement problem
- `circularSubArray.cpp`: maximum circular subarray sum (C++, Kadane-style)
- `N_Fibonacci.cpp`: Fibonacci in C++

### 2. Notebooks (concept demos)
- `FibonacciFourWays.ipynb`: Fibonacci implemented four different ways
- `binrayTree.ipynb`: binary tree basics (the filename has a typo, "binray")
- `hashing_table.ipynb`: hash table implementation/demo

### 3. Terminal games and puzzles (Python)
- `hangman2.py`, `hangman_art.py`, `hangman_words.py`: step-by-step Hangman. `hangman2.py` is the main file, and the other two hold ASCII art and the word list.
- `Number_Quest.py`: digit-manipulation puzzle with ASCII-art banner. Its output screenshot is `Number Quest output.jpg`.
- `windows_destroyer_game.py`: **DANGEROUS, see warning below**

### 4. Utilities and "AI/data" scripts (Python)
- `documentSummarization.py`: extractive text summarizer using IDF-weighted cosine similarity between sentences, then a `networkx` graph (TextRank style). Needs `nltk`, `numpy`, `networkx`.
- `aes_gcm.py`: AES-256-GCM encrypt/decrypt CLI with a PBKDF2-HMAC-SHA256 password-derived key. **Currently has a syntax error, see "Known issues".**
- `saveInput.py`: reads lines from the user until an empty line, then saves them to `user_input.txt`
- `rickroll.py`: opens a YouTube link in the browser
- `cleaning_pipeline.py`: placeholder only (`print("hello world")`, with the original code removed)

### 5. HTML mini-apps (open directly in a browser)

| File | Page title / what it does |
|---|---|
| `game.html` | Guess the Number game |
| `discoLights.html` | Disco Lights Party animation |
| `colorChangingSwitch.html` | "Cool Switch" toggle with color change |
| `bouncingButtons.html` | Registration form with bouncing buttons |
| `3passwordPage.html` | User Registration (password form) |
| `cameraChecker.html` | Camera feed (webcam access) |
| `multiFrameCam.html` | Camera feed, multi-frame variant |
| `locationOnMap.html` | Shows location on a map |
| `yourDeviceInfo.html` | Displays user laptop/device info |
| `githubForm.html` | GitHub details form |
| `socialMediaDetails.html` | Social media handles page |
| `socialMediaInfoDark.html` | Dark-theme version of the above |
| `footer.html` | Reusable footer snippet |

### 6. Misc
- `open.bat`: Windows batch script that opens LinkedIn, Facebook, GitHub, Hacktoberfest, YouTube and Google in the browser

### 7. Community docs
- `README.md`: intro and contribution steps (fork, clone, branch, add, PR)
- `contributing.md`: detailed contribution guidelines
- `CodeOfConduct.md`: code of conduct

## How to run things

| Type | How to run |
|---|---|
| Python script | `python <file>.py` (Python 3). Install extras only where needed, for example `pip install nltk numpy networkx` for `documentSummarization.py` and `pip install cryptography` for `aes_gcm.py`. |
| LeetCode `.py` files | These are class-only solutions. They need `from typing import List`, and they are meant to be pasted into LeetCode, not run directly. |
| C++ | `g++ circularSubArray.cpp -o out && ./out` (uses `bits/stdc++.h`, so GCC or MinGW) |
| HTML | Double-click, or open in a browser. Camera and location pages need browser permission and usually `https` or `localhost`. |
| Notebooks | `jupyter notebook`, or open in VS Code or Cursor |
| `open.bat` | Double-click, or run in `cmd` |

## Known issues and warnings

1. **`windows_destroyer_game.py` is harmful.** If the user guesses wrong, it tries to delete `C:\Windows\System32`. Do **not** run it. Consider deleting it or turning it into a harmless demo, because it conflicts with the repo's "fun and educational" intent.
2. **`aes_gcm.py` does not run.** Its imports and helper functions (`encrypt`, `decrypt`, `b64e`, `b64d`) are missing. A stray `")` on line 10 causes `SyntaxError: unterminated string literal`. It needs to be restored.
3. **`cleaning_pipeline.py`** is only a placeholder ("code deleted").
4. **Inconsistent naming.** The LeetCode files mix `leetcode_41.py` and `leetcode3607.py`. There are typos (`binrayTree`, `uniqueOccurence`) and filenames with spaces (`Number Quest output.jpg`, `Maximize_Array Value_After_Rearrangement.py`).
5. **Broken link.** `contributing.md` links to `CODE_OF_CONDUCT.md`, but the file is named `CodeOfConduct.md`.
6. **No tests, dependency file, or folder organization.** Everything sits in one flat directory.

## Suggested improvements

- Group files into folders: `leetcode/`, `games/`, `web/`, `notebooks/`, `utils/`, `cpp/`
- Add a `requirements.txt` (`nltk`, `numpy`, `networkx`, `cryptography`)
- Rename files consistently, for example `leetcode_0041.py`
- Fix or remove `aes_gcm.py`, `cleaning_pipeline.py` and `windows_destroyer_game.py`
- Fix the `CODE_OF_CONDUCT.md` link in `contributing.md`
- Add `from typing import List` to the LeetCode files so they run standalone

## Contributing (summary)

1. Fork https://github.com/akasumitlamba/IA-G and clone it
2. Create a branch: `git checkout -b your-branch-name`
3. Add your snippet with a short description and usage notes
4. `git add . && git commit -m "Add my awesome code"`
5. `git push origin your-branch-name`, then open a Pull Request

Guidelines: keep code well-documented, avoid heavy dependencies, and be respectful.
