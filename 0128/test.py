# 0. import
import requests
from pprint import pprint

# 1. URL 및 요청변수 설정
# https://developers.themoviedb.org/3/movies/get-popular-movies
# http://api.themoviedb.org/3/search/movie?api_key=e53010cbbbc91dcb3b26e8894f6a8116&region=KR&language=ko&query=title


# 영화검색 (Search Movies) 요청을 보내고, id를 받아옴.
def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        # 내 api_key
        'api_key': 'e53010cbbbc91dcb3b26e8894f6a8116',
        'query' : title,  # => title을 보냄.
        'region': 'KR',
        'language': 'ko'
    }

    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL+path, params=params)
    # print(response.status_code, response.url)
    data = response.json()



    
    params2 = {
        # 내 api_key
        'api_key': 'e53010cbbbc91dcb3b26e8894f6a8116',
        'language': 'ko'
    }
    # 영화제목에 해당하는 값이 있다면
    if data.get('results'):
        # movie_id를 추출
        result = data.get('results')[0].get('id')
        
    else:
        return None
################################################################################################
    BASE = 'https://api.themoviedb.org/3'
    path = '/movie/'+str(result)+'/recommendations'
    params = {
        'api_key' : '599d9943faf8858722e82a75833aa6b0',
        'region' : 'KR',
        'language' : 'ko',
    }

    response = requests.get(BASE+path,params=params)
    print(response)



if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
