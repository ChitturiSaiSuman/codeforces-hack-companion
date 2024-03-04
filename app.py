import logging
from datetime import datetime

import fetch
from hack import Hacker
import UTIL

if __name__ == "__main__":

    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    log_file = f"{timestamp}.log"

    logging.basicConfig(
        format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
        level=logging.INFO,
        filename=log_file,
        filemode="w",
    )

    metadata = UTIL.get_metadata()
    contest = metadata["contest"]
    problems = UTIL.prepare(metadata)
    hackable_submissions = fetch.fetch_all_hackable_submissions_using_api(contest)

    hacker = Hacker(metadata, problems, hackable_submissions)

    hacker.run()