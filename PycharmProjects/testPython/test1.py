# -*encoding:utf-8 *-
# m1 = ''
#m1 = {'id': ''}.items()
# if not m1:
#     print "the tuple is null"
# else:
#     print "the tuple is not null"

# if m1:
#     print ("the tuple is null")
# else:
#     print "the tuple is not null"


# ids = [1,4,3,3,4,2,3,4,5,6,1]
# print set(ids)
# ids = list(set(ids))
# print ids

ids = [1,4,3,3,4,2,3,4,5,6,1]
news_ids = list(set(ids))
news_ids.sort(key=ids.index)
print news_ids
