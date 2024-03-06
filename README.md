# codeforces-hack-companion
Helper to fetch submissions from a Contest and check for possible Hacks

## One-time setup

```
pip3 install bs4
```

## Preparation for hacks

* Populate input generators in `judge/generator.py`:

    * These are named `AlphaGenerator`, `BetaGenerator`, ..., `SigmaGenerator`.
    * Each generator has two methods, named `generate` and `validate`.
    * Use one Generator for one problem.

* Populate `metadata.json`:

    * Set contest to the current Contest ID.
    * Set timeout to the number of seconds you want to stress-test a single submission (30 is preferred).
    * Order your problems in decreasing order of their difficulty. This helps to complete checking hacks for at least harder problems. For example, choose "F", "E" as the first problem and "B", "A" as the last ones.
    * Populate names of the problems, time limit, and memory limit accordingly.
    * Choose the Generator for the problem.
    * Choose a reference submission for the problem. Reference submission is a submission from one of the top 10 participants, where the chances of it being wrong are nearly impossible.

## Run

```
source entry.sh
```

## How it works

1. The application retrieves the reference submissions, prepares them locally, and sets them ready for evaluation.
2. All the submissions made during the contest are retrieved using Codeforces API.
3. Fetched submissions are filtered for various conditions:
    - The problem to which the submission was made must be available in `metadata.json`.
    - Programming language used in the submission must be available in `constants/setup.json`.
    - Participant is eligible for hacks.
    - Submission passed the pre-tests.
4. Evaluation phase begins:
    - Submissions are ordered based on their problem index in `metadata.json`.
    - Each submission is compiled, stress-tested against the reference submission for `timeout` seconds.
    - If at any instance, both submissions fail to produce similar outputs, the tester treats it as a successful hacking attempt.
    - If the stress-test exits normally after `timeout` seconds, the tester treats it as a failed hacking attempt.
    - Either way, the result of the hack is logged to `<contest_id>_hack.log` file.
5. Manually identify the successful hacks made by the tester by referring to the log file. Get the seed and proceed to generate the input with the seed. Provide this input on the Codeforces hack page for the submission and submit.

## Improvements are welcomed