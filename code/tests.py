from tuples import tuple_count, tuple_bound, binned_count

def test_count():
    #p = 1020137
    p = 1020293
    g = 11
    v = 2
    t = 7
    c,l,u = tuple_count(t, g, p, v)
    print("Count = {}, \nmin = {}, \nmax ={} \nlength {}".format(c, l, u, len(c.values()) ))
    print("bounds = {}".format(tuple_bound(t,g,p,v)))
    print("Binned: {}".format(binned_count(t,g,p,v,10)))

