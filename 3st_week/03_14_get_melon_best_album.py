#내 풀이
# class LinkedTuple:
#     def __init__(self):
#         self.items = []
#
#     def add(self, key, value):
#         self.items.append((key, value))
#
#     def get(self, key):
#         for k, v in self.items:
#             if k == key:
#                 return v
#
#     # def __len__(self):  # len() 호출할 때 사용됨
#     #     return len(self.items)
#
#
# class LinkedDict:
#     def __init__(self):
#         self.items = {}
#
#     def put(self, genres_key, play_index, play_count):
#         self.items[genres_key].add(play_index, play_count)
#
#     def get(self, genres_key, play_index):
#         return self.items[genres_key].get(play_index)
#
# def get_melon_best_album(genre_array, play_array):
#     genres_length = len(genre_array)
#     #일단 해시테이블 => 딕셔너리에 튜플형태로 넣는다
#     origin_linked_dict = LinkedDict()
#     sum_linked_dict = {}
#     for i in range(genres_length):
#         origin_linked_dict.items[genre_array[i]] = LinkedTuple()
#
#     for i in range(genres_length):
#         origin_linked_dict.put(genre_array[i], i, play_array[i])
#
#     print(repr(origin_linked_dict))
#
#     # 같은 키끼리 더해서 새로운 딕셔너리 만든다
#     for key in genre_array:
#         current_key_length = len(origin_linked_dict.items[key].items)
#         current_sum = 0
#         for j in range(current_key_length):
#             current_sum += origin_linked_dict.items[key].get(j)
#
#         sum_linked_dict[key] = current_sum
#
#     print(sum_linked_dict)
#
#     #정렬을 한다
#     return []

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# -> genre_array에서 genre별로 재생횟수를 모두 모아서 비교해준다 그리고 가장 많이 재생된 장르 별로 노래를 2곡씩 넣어준다
# ->어떤 장르가 올지 모른다
# ->총 음악 재생횟수를 딕셔너리
#
# 2. 장르 내에서 많이 재생된 노래를 먼저 넣어줘야 한다
# -> 많이 재생된 장르 별로 2곡을 넣어줄 때, 많이 재생된 노래먼저 넣어줘야 한다
# {"classic":[(0,500), (2, 150)]} => 내가 생각한게 맞았다 구현을 못해서 그렇지...

# 3. 장르내에서 재생횟수가 같다면, 인덱스가 낮은 노래 먼저 수록해야한다
def get_melon_best_album(genre_array, play_array):
    #1.dict에 장르별로 얼마나 재생횟수를 가지고 있는가
    #2. dict에 장르별로 어느 인덱스에 몇번 재생횟수를 가지고 있는가
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        #만약에 기존에 있는 장르가 키 값으로 존재한다면
        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
    print(genre_total_play_dict)
    print(genre_index_play_array_dict)

    #튜플이 담긴 배열 형태로 만든다
    print(genre_total_play_dict.items())
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key= lambda item:item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        #print(genre, total_play)
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)

        #장르별로 제일 잘나가는 2곡만 넣어라
        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break

            #print(index, play)
            result.append(index)
            genre_song_count += 1

    return result

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))