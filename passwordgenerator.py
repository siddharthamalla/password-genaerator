import random
integer1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
integer2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
integer3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
integer4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
print(random.choice(integer1) + random.choice(integer2) + random.choice(integer1) + random.choice(integer3) + random.choice(integer4))