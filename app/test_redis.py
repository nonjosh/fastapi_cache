import pickle
import redis

def get_pickled_profile(profile_id):
    r = redis.Redis(host='localhost', port=6379, db=0)
    pickled_profile = r.get(f'profile_{profile_id}')

    if pickled_profile is not None:
        profile = pickle.loads(pickled_profile)
        return profile

    return None

# Replace with the actual profile id
profile_id = '0902a2e6-d683-4eb3-a4c8-8406d5758bac'
profile = get_pickled_profile(profile_id)
print(profile)
