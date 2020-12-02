import numpy as np 


def match_acc(base, queries, dist):
    '''
    dist: euclidean/hamming
    '''
    if dist == 'euclidean':
        sum_of_match = 0
        for query_key in queries:
            min_dist_key = query_key
            min_dist = np.linalg.norm(base[min_dist_key], queries[query_key])
            for img_key in base:
                tmp_dist = np.linalg.norm(base[img_key], queries[query_key])
                if min_dist > tmp_dist:
                    min_dist = tmp_dist
                    min_dist_key = img_key
            if min_dist_key == query_key:
                sum_of_match += 1
        return sum_of_match / len(base)

    elif dist == 'hamming':
        sum_of_match = 0
        for query_key in queries:
            min_dist_key = query_key
            min_dist = base[query_key] - queries[query_key]

            for img_key in base:
                tmp_dist = base[img_key] - queries[query_key]
                
                if min_dist > tmp_dist:
                    min_dist = tmp_dist
                    min_dist_key = img_key
            if min_dist_key == query_key:
                sum_of_match += 1
            # print(query_key, min_dist_key)
        return sum_of_match / len(base)

    return None