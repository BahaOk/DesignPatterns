class CurrentUser:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


user1 = CurrentUser()
user1.username = "Baha"

user2 = CurrentUser()

print(user2.username)
print(user1 is user2)
"""
burada iki kullanıcınında adının Baha olması aktif kullanıcı temsil eden nesnenin tek olmasıdır 
singleton deseni ile bunu sağlarız.
"""