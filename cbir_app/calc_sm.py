from sklearn.metrics.pairwise import cosine_similarity
from numpy.linalg import norm

def sim_cal(queryVec,imgFeats):
    scores = cosine_similarity(queryVec.reshape(1, -1), imgFeats)
    return scores