# # Day17
#
# class User:
#
#     def __int__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "anthony")
# user_2 = User("002", "ivana")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

class Question:
    def __int__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


newQ = Question("asdfg", "False")
newQ.text
