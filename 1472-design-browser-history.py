"""
You have a browser of one tab where you start on the homepage and you can
visit another url, get back in the history number of steps or move forward in
the history number of steps.

Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage
    of the browser.

    void visit(string url) Visits url from the current page. It clears up all
    the forward history.

    string back(int steps) Move steps back in history. If you can only return
    x steps in the history and steps > x, you will return only x steps. Return
    the current url after moving back in history at most steps.

    string forward(int steps) Move steps forward in history. If you can only
    forward x steps in the history and steps > x, you will forward only x steps.
    Return the current url after forwarding in history at most steps.

Constraints:
    1 <= homepage.length <= 20
    1 <= url.length <= 20
    1 <= steps <= 100
    homepage and url consist of  '.' or lower case English letters.
    At most 5000 calls will be made to visit, back, and forward.
"""


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page = 0

    def visit(self, url: str) -> None:
        self.history = self.history[: self.current_page + 1]
        self.history.append(url)
        self.current_page += 1

    def back(self, steps: int) -> str:
        self.current_page = max(0, self.current_page - steps)
        return self.history[self.current_page]

    def forward(self, steps: int) -> str:
        self.current_page = min(len(self.history) - 1, self.current_page + steps)
        return self.history[self.current_page]


browserHistory = BrowserHistory("leetcode.com")

browserHistory.visit("google.com")  # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")  # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com")  # You are in "facebook.com". Visit "youtube.com"

assert browserHistory.back(1) == "facebook.com"
assert browserHistory.back(1) == "google.com"
assert browserHistory.forward(1) == "facebook.com"

browserHistory.visit("linkedin.com")

assert browserHistory.forward(2) == "linkedin.com"
assert browserHistory.back(2) == "google.com"
assert browserHistory.back(7) == "leetcode.com"
