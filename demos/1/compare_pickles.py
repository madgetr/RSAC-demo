import pickle

good_pickle = pickle.load(open("good_pickle.pkl", "rb"))
print("Good pickle:", good_pickle)
bad_pickle = pickle.load(open("bad_pickle.pkl", "rb"))
print("Bad pickle:", bad_pickle)
worse_pickle = pickle.load(open("worse_pickle.pkl", "rb"))
print("Worse pickle:", worse_pickle)


print(f"good_pickle == bad_pickle: {good_pickle == bad_pickle}")
print(f"good_pickle == worse_pickle: {good_pickle == worse_pickle}")