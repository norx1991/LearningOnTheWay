import json
import urllib3

http = urllib3.PoolManager()
difficulty_table = {1: 'Easy', 2: 'Medium', 3: 'Hard'}


def get_problem_link(problem):
    title_slug = problem['stat']['question__title_slug']
    url = 'https://leetcode.com/problems/' + title_slug
    return url


def get_difficulty(problem):
    return difficulty_table[problem['difficulty']['level']]


def get_problem_summary(problem):
    url = get_problem_link(problem)
    problem_id = problem['stat']['question_id']
    difficulty = get_difficulty(problem)
    title = problem['stat']['question__title']
    return f'<{difficulty}> ({problem_id}) {title}: {url}'


if __name__ == "__main__":
    url = 'https://leetcode.com/api/problems/algorithms/'
    resp = http.request('GET', url)
    data = json.loads(resp.data.decode('utf-8'))
    ntotal = data['num_total']
    alg_list = data['stat_status_pairs'][::-1]

    items = []
    for problem in alg_list:
        url = get_problem_link(problem)
        problem_id = problem['stat']['frontend_question_id']
        difficulty = get_difficulty(problem)
        title = problem['stat']['question__title']
        items.append((problem_id, title, url, difficulty))

    items.sort()

    for problem_id, title, url, difficulty in items:
        print((f'[{problem_id}. {title.replace(" ", " ")}]({url}) ({difficulty})  '))
