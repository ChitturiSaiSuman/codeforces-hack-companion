import json
import logging

import bs4
import requests

import entities
from config import Constants


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
        all_submissions,
    )

    hackable_submissions = list(hackable_submissions)

    response_file = f'{contest_id}_api_resp.json'
    with open(response_file, 'w') as file:
        json.dump(hackable_submissions, file, indent=2)

    return hackable_submissions


def fetch_submission(submission: dict) -> dict:
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
    language = submission["programmingLanguage"]
    languages_allowed = Constants.setup["ALLOWED_LANGUAGES"]
    for lang_allowed in languages_allowed:
        if lang_allowed["LANGUAGE"] == language:
            language = lang_allowed

    # Source
    source = soup.find(id="program-source-text").get_text(strip=True)

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
        return {}

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
