import json
import logging
import time

import bs4
import re
import requests

import UTIL
from config import Constants

last_time = time.time()
minimum_gap = 5


def fetch_all_hackable_submissions_using_api(contest_id: str) -> list:
    url = f"https://codeforces.com/api/contest.status?contestId={contest_id}"

    resp_from_api = requests.get(url)
    response = json.loads(resp_from_api.text)

    if response["status"] != "OK":
        raise Exception(f"Failed to fetch submissions for Contest {contest_id}")

    all_submissions = response["result"]
    hackable_submissions = filter(
        lambda submission: submission["author"]["participantType"]
        in Constants.setup["ALLOWED_PARTIES"],
        all_submissions,
    )

    allowed_languages = Constants.setup["ALLOWED_LANGUAGES"]
    lang_symbols = [lang["LANGUAGE"] for lang in allowed_languages]

    hackable_submissions = filter(
        lambda submission: submission["programmingLanguage"] in lang_symbols,
        hackable_submissions,
    )

    hackable_submissions = filter(
        lambda submission: 'verdict' in submission and submission['verdict'] == 'OK',
        hackable_submissions
    )

    metadata = UTIL.get_metadata()
    allowed_problems = [problem['code'] for problem in metadata['problems']]

    hackable_submissions = filter(
        lambda submission: submission["problem"]["index"] in allowed_problems,
        hackable_submissions
    )

    hackable_submissions = list(hackable_submissions)
    hackable_submissions.sort(key=lambda submission: allowed_problems.index(submission['problem']['index']))

    response_file = f'{contest_id}_api_resp.json'
    with open(response_file, 'w') as file:
        json.dump(hackable_submissions, file, indent=2)

    return hackable_submissions


def fetch_submission(submission: dict) -> dict:
    global last_time, minimum_gap
    while time.time() - last_time < minimum_gap:
        logging.info('Sleeping for 1 second')
        time.sleep(1)

    last_time = time.time()

    submission_id = submission["id"]
    contest_id = submission["contestId"]
    url = f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}"

    logging.info(f"Currently Fetching {url} ...")

    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, "html.parser")

    # Fetch attributes one by one:

    # Problem Link
    problem = submission["problem"]["index"]

    # Owner
    owner = submission["author"]["members"][0]["handle"]

    # Language
    language = UTIL.get_langauge(submission["programmingLanguage"])

    # Source
    source = soup.find(id="program-source-text").get_text(strip=True)
    if language['EXTENSION'] == '.java':
        source = re.sub(r'\bpublic\s+class\b', 'class', source)

    # Verdict
    verdict = submission["verdict"]

    return {
        "submission_id": submission_id,
        "problem": problem,
        "contest_id": contest_id,
        "owner": owner,
        "language": language,
        "source": source,
        "verdict": verdict,
    }


def fetch_reference_submission(url: str) -> dict:
    tokens = url.split("/")
    contest_id = tokens[-3]
    submission_id = tokens[-1]

    logging.info(f"Currently Fetching {url} ...")

    resp = requests.get(url)
    
    if resp.status_code != 200:
        logging.error(f'Cannot fetch submission from {url}')
        exit(0)

    soup = bs4.BeautifulSoup(resp.text, "html.parser")

    # Fetch attributes one by one:

    # Problem Link
    problem = soup.find(
        "a", href=lambda t: contest_id in t and "problem" in t if t else False
    ).get("href")[1:]

    # Owner
    profile_link = soup.find(
        "a", href=lambda t: "profile" in t.lower() if t else False
    ).get("href")
    owner = profile_link.split("/")[-1]

    # Language
    language = None
    languages_allowed = Constants.setup["ALLOWED_LANGUAGES"]
    for lang_allowed in languages_allowed:
        if lang_allowed["LANGUAGE"] in resp.text:
            language = lang_allowed

    if language == None:
        logging.error(f"Unable to identify the Programming Language in the submission {url}")
        exit(0)

    # Source
    source = soup.find(id="program-source-text").get_text(strip=True)

    # Verdict
    verdict = soup.find(
        "span", class_=lambda t: "verdict" in t if t else False
    ).get_text()

    return {
        "submission_id": submission_id,
        "problem": problem,
        "contest_id": contest_id,
        "owner": owner,
        "language": language,
        "source": source,
        "verdict": verdict,
    }
