from search_alg import kmp_search, boyer_moore_search, rabin_karp_search
from typing import Callable
from timeit import timeit


def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()
    
def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f'from __main__ import {func.__name__}'
    statement = f'{func.__name__}(text, pattern)'
    return timeit(stmt=statement, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


def main():
    real_pattern = 'Література'
    fake_pattern = 'блохи курять бамбук'
    results = []

    speedy_alg = {}

    for article in ('article1.txt', 'article2.txt'):
        text = read_file(article)
        article_speed = []
        for pattern in (real_pattern, fake_pattern):
            time = benchmark(boyer_moore_search, text, pattern)
            results.append((article, boyer_moore_search.__name__, pattern, time))
            article_speed.append(time)
            article_speed.append('boyer_moore_search')
            
            time = benchmark(kmp_search, text, pattern)
            results.append((article, kmp_search.__name__, pattern, time))
            if article_speed[0] > time:
                article_speed[0] = time
                article_speed[1] = 'kmp_search'
            
            time = benchmark(rabin_karp_search, text, pattern)
            results.append((article, rabin_karp_search.__name__, pattern, time))
            if article_speed[0] > time:
                article_speed[0] = time
                article_speed[1] = 'rabin_karp_search'
            
            speedy_alg[article] = article_speed
    
    print()
    title = f"{'Стаття':^15} | {'Алгоритм':^20} | {'Строка пошуку':^20} | {'Час виконання, сек':^20}"
    print(title)
    print('-'*len(title))
    for result in results:
        print(f'{result[0]:^15} | {result[1]:<20} | {result[2]:<20} | {round(result[3],4):^20}')

    print('\nНайшвидші алгоритми:')
    article_result = speedy_alg['article1.txt'][1]
    if article_result != speedy_alg['article1.txt'][3]:
        article_result = article_result + ' та ' + speedy_alg['article1.txt'][3]
    print('Для статті 1: ', article_result)

    total_article_result = article_result

    article_result = speedy_alg['article2.txt'][1]
    if article_result != speedy_alg['article2.txt'][3]:
        article_result = article_result + ' та ' + speedy_alg['article1.txt'][3]
    print('Для статті 2: ', article_result)

    if article_result != total_article_result:
        total_article_result = total_article_result + ' та ' + article_result

    print('Найкащий алгоритм для обох статей: ', total_article_result)

if __name__ == '__main__':
    main()