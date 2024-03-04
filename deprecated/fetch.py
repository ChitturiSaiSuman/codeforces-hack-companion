import concurrent.futures
import logging

import bs4
import requests

from config import Constants


def fetch_submission(contest_id=None, submission_id=None, url=None) -> dict:
    """
    Return a submission from CF
    Example: {
        "defender": "<cf_handle>",
        "submission_id": "247461697",
        "contest_id": "<contest_id>",
        "lang": "Python 3",
        "source": "<source>"
    }
    """

    if url == None:
        assert contest_id != None and submission_id != None
        url = f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}"

    else:
        tokens = url.split("/")
        contest_id = tokens[-3]
        submission_id = tokens[-1]

    resp = requests.get(url)
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
    languages_allowed = Constants.languages["ALLOWED"]
    for lang_allowed in languages_allowed:
        if lang_allowed in resp.text:
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


def fetch_submissions_from_page(contest_id: str, problem: str, page: int) -> list:
    url = f"https://codeforces.com/contest/{contest_id}/status/{problem}/page/{page}"
    resp = requests.get(url)
    print(resp.status_code)
    logging.info(resp.status_code)
    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    submission_rows = soup.find_all("tr", {"data-submission-id": True})

    submissions_in_page = list()

    for row in submission_rows:
        try:
            submission_id = row["data-submission-id"]
            user = row.find("a", class_="rated-user").text.strip()
            # problem = row.find('a', href=lambda t: f'/contest/{contest_id}/problem/' in t.lower() if t else False).get_text(strip=True)
            lang = row.find("td", class_=None).get_text(strip=True)
            verdict = row.find(
                "span", class_=lambda t: "submissionVerdictWrapper" in t if t else False
            ).get_text(strip=True)

            submissions_in_page.append(
                (contest_id, problem, submission_id, user, lang, verdict)
            )

        except Exception as e:
            logging.warning(f"Ignoring exception for {submission_id}")
            continue

    return submissions_in_page


def fetch_all_submissions_for_problem(
    contest_id: str, problem: str, page_limit: int
) -> list:
    all_submissions_for_problem = list()

    def fetch_submissions_from_page_wrapper(page):
        return fetch_submissions_from_page(contest_id, problem, page)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Use executor.map to parallelize fetching submissions from different pages
        results = executor.map(
            fetch_submissions_from_page_wrapper, range(1, page_limit + 1)
        )

        # Extend the results to the main list
        for submissions_from_page in results:
            all_submissions_for_problem.extend(submissions_from_page)

    return all_submissions_for_problem


def fetch_all_submissions(contest_id: str, problems: list, page_limits: list) -> list:

    all_submissions = []

    for problem, page_limit in zip(problems, page_limits):
        logging.info(
            f"Fetching Submissions across {page_limit} pages for Problem {problem} in Contest {contest_id} ..."
        )
        submissions_for_problem = fetch_all_submissions_for_problem(
            contest_id, problem, page_limit
        )
        print(submissions_for_problem)
        logging.info(f"Done")
        all_submissions.extend(submissions_for_problem)

    return all_submissions
