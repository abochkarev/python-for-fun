def get_score(series):
    d = {'a':0, 'b':0, 'c':0, 'd': 0, 'e': 0}
    for l in series:
        d[l.lower()] += -1 if l.isupper() else 1
    print(sorted(d.items(), key=lambda x: x[1], reverse=True))

if __name__ == '__main__':
    get_score('EbAAdbBEaBaaBBdAccbeebaec')
