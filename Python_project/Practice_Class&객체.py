class User:
    pass


user1 = User()
user2 = User()

print(type(user1))
# #객체의 속성을 인스턴스 변수로 저장하는 방법
# user1.name = "박재선"
# user1.email = "ddorri83@naver.com"
# user1.password = "020803"

# user2.name = "규현"
# user2.email = "kkh@naver.com"
# user2.password = "0212"
# #인스턴스 안에 독립적으로 저장된 변수를 인스턴스 변수라고 함.
# #여기 박재선, 김가나, 0212같은걸 인스턴스 변수라고 함
# print(user1.email)
# print(user2.password)
# print(user1.age)





#인스턴스 메소드
# class User:
#     def say_hello(some_user):
#         print(f"안녕하세요! 저는 {some_user.name}입니다!")


# user1 = User()
# user2 = User()

# user1.name = "박재선"
# user1.email = "ddorri83@naver.com"
# user1.password = "020803"

# user2.name = "김가나"
# user2.email = "kkh@naver.com"
# user2.password = "0212"

#클래스이름.메소드이름()
# User.say_hello(user1)
# user1.say_hello() #클래스가 아닌 인스턴스 메소드를 출력하면 따로 코드를 쓰지 않아도 인스턴스가 메소드의 첫번째 argument로 자동 전달된다




#04.인스턴스 메소드 활용
# class User:
#     def say_hello(self):
#         print(f"안녕하세요! 저는 {self.name}입니다!")

#     def login(self, email, password):
#         if self.email == email and self.password == password:
#             print("로그인 성공, 환영합니다")
#             self.say_hello()
#         else:
#             print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")



# user1 = User()
# user2 = User()

# user1.name = "박재선"
# user1.email = "ddorri83@naver.com"
# user1.password = "020803"

# user2.name = "김가나"
# user2.email = "kkh@naver.com"
# user2.password = "0212"

# print(user1.name, user1.email, user1.password)
# print(user2.name, user2.email, user2.password)





#05. 인스턴스 변수 초기화
# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def say_hello(self):
#         print(f"안녕하세요! 저는 {self.name}입니다!")

#     def login(self, email, password):
#         if self.email == email and self.password == password:
#             print("로그인 성공, 환영합니다")
#             self.say_hello()
#         else:
#             print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")



# user1 = User("박재선","ddorri83@naver.com","0208")
# user2 = User("김가나","kkh@naver.com","0212")


# print(user1.name, user1.email, user1.password)
# print(user2.name, user2.email, user2.password)

# initialize와 __init__메소드
# user1.User()
# user1.initialize("가나","kkh@naver.com","0212")
# #위의것과 아래것은 같은 결과가 나온다. 따라서, __init__을 사용하는게 파이썬에서는 더 편한 방법
# user1.__init__("가나","kkh@naver.com","0212")


#06.__str__()메소드
# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def say_hello(self):
#         print(f"안녕하세요! 저는 {self.name}입니다!")

#     def login(self, email, password):
#         if self.email == email and self.password == password:
#             print("로그인 성공, 환영합니다")
#             self.say_hello()
#         else:
#             print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

#     def __str__(self):
#         #문자열로 형변환 할때 사용됨
#         return f"사용자: {self.name}, 이메일: {self.email}"


# user1 = User("박재선","ddorri83@naver.com","0208")
# user2 = User("김가나","kkh@naver.com","0212")


# print(str(user1))
# #python의 print함수는 안의 argument를 print하기전에 안에 있는 argument를 문자열로 자동 형변환을 하기 때문에
# #문자열을 따로 다루는게 아니라 지금처럼 출력만 하는 거라면 string함수를 직접 호출하는 부분은 삭제할 수 있다
# #이렇게
# print(user1)
# #string메소드에 정의한 것 처럼 인스턴스가 읽기쉬운 문자열로 변한것을 확인할 수 있다

# print(str(user2))












#맞팔해요 practice
# class User:
#     # 인스턴스 변수 설정
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#         self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
#         self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

#     # 팔로우
#     def follow(self, another_user):
#         self.following_list.append(another_user)
#         another_user.followers_list.append(self)
#     # 내가 몇 명을 팔로우하는지 리턴
#     def num_following(self):
#         return len(self.following_list)

#     # 나를 몇 명이 팔로우하는지 리턴
#     def num_followers(self):
#         return len(self.followers_list)
    

# # 유저들 생성
# user1 = User("Jung", "Jung@naver.com", "123456")
# user2 = User("wook", "wook@naver.com", "abcdef")
# user3 = User("kyu", "kyu@naver.com", "123abc")
# user4 = User("Lisa", "lisa@naver.com", "abc123")

# # 유저마다 서로 관심 있는 유저를 팔로우
# user1.follow(user2)
# user1.follow(user3)
# user2.follow(user1)
# user2.follow(user3)
# user2.follow(user4)
# user4.follow(user1)

# # 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
# print(user1.name, user1.num_followers(), user1.num_following())
# print(user2.name, user2.num_followers(), user2.num_following())
# print(user3.name, user3.num_followers(), user3.num_following())
# print(user4.name, user4.num_followers(), user4.num_following())




#메뉴만들기
# class MenuItem:
#     # 음식 메뉴를 나타내는 클래스
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} 가격: {self.price}"

# # 메뉴 인스턴스 생성
# burger = MenuItem("햄버거", 4000)
# coke = MenuItem("콜라", 1500)
# fries = MenuItem("후렌치 후라이", 1500)

# # 메뉴 인스턴스 출력
# print(burger)
# print(coke)
# print(fries)




#게임 캐릭터 만들기
# class GameCharacter:
#     # 게임 캐릭터 클래스
#     def __init__(self, name, hp, power):
#         self.name = name
#         self.hp = hp
#         self.power = power

#     def is_alive(self):
#         # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
#         if self.hp > 0:
#             return True
#         else:
#             return False
#     def get_attacked(self, damage):
#         """
#         게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
#         조건:    
#             1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
#             2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
#         """
#         if not self.is_alive():
#             print("{}님은 이미 죽었습니다.".format(self.name))
#         else:
#             if self.hp < damage:
#                 self.hp = 0
#             else:
#                 self.hp -= damage

#     def attack(self, other_character):
#         # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다
#         if self.is_alive():
#             other_character.get_attacked(self.power)
#             #other_character에게 self.power만큼 공격한걸 깍는거네. 앞에 만들어 놓은 get_attacked메소드를 사용하는거고
            
#     def __str__(self):
#         # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다
#         return f"{self.name}님의 hp는 {self.hp}만큼 남았습니다."
# # 게임 캐릭터 인스턴스 생성                        
# character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
# character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# # 게임 캐릭터 인스턴스들 서로 공격
# character_1.attack(character_2)
# character_2.attack(character_1)
# character_2.attack(character_1)
# character_2.attack(character_1)
# character_2.attack(character_1)
# character_2.attack(character_1)

# # 게임 캐릭터 인스턴스 출력
# print(character_1)
# print(character_2)







#블로그 유저 만들기
#Post할때마다 사용되는 클래스네.
# class Post:
#     # 게시글 클래스
#     def __init__(self, date, content):
#         # 게시글은 속성으로 작성 날짜와 내용을 갖는다
#         self.date = date
#         self.content = content

#     def __str__(self):
#         # 게시글의 정보를 문자열로 리턴하는 메소드
#         return "작성 날짜: {}\n내용: {}".format(self.date, self.content)
    
    
# class BlogUser:
#     # 블로그 유저 클래스
#     def __init__(self, name):
#         """
#         블로그 유저는 속성으로 이름, 게시글들을 갖는다
#         posts는 빈 배열로 초기화한다
#         """
#         self.name = name
#         self.posts = []

#     def add_post(self, date, content):
#         # 새로운 게시글 추가
#         new_post = Post(date,content)
#         self.posts.append(new_post)
#     def show_all_posts(self):
#         # 블로그 유저의 모든 게시글 출력
#         for post in self.posts:
#             print(post)
#     def __str__(self):
#         # 간단한 인사와 이름을 문자열로 리턴
#         return f"안녕하세요 {self.name}입니다.\n"
           
    

# # 블로그 유저 인스턴스 생성
# blog_user_1 = BlogUser("박재선")

# # 블로그 유저 인스턴스 출력(인사, 이름)
# print(blog_user_1) 

# # 블로그 유저 게시글 2개 추가
# blog_user_1.add_post("2024년 4월 16일", """
# 어제 하체 운동을 했다.
# 오늘 하루 벌써 걷기가 힘들다
# 그래도 뿌듯하다.
# 오늘 하루도 아름답게 보내보자
# """)

# blog_user_1.add_post("2024년 4월 16일", """
# 오늘도 출근을 한다.
# 아직 출근 4시간전이지만, 
# 벌써 집에 가고싶다.
# """)

# # 블로그 유저의 모든 게시글 출력
# blog_user_1.show_all_posts()






#11.클래스 변수
# class User:

#     count = 0


#     def __init__(self, name, email, password):
#         #유저 instance가 생성될때마다 count값을 늘려간다
#         #Class의 instace가 생성될때마다 init메소드가 자동으로 실행되므로 count값을 여기에 넣어주면될듯
#         self.name = name
#         self.email = email
#         self.password = password

#         User.count += 1 


#     def say_hello(self):
#         print(f"안녕하세요! 저는 {self.name}입니다!")

#     def login(self, email, password):
#         if self.email == email and self.password == password:
#             print("로그인 성공, 환영합니다")
#             self.say_hello()
#         else:
#             print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

#     def __str__(self):
#         #문자열로 형변환 할때 사용됨
#         return f"사용자: {self.name}, 이메일: {self.email}"

#     #파이썬 데코레이터
#     @classmethod
#     def print_number_of_users(cls):
#         print(f"총 유저 수는: {cls.count}입니다.")

        


# user1 = User("박재선","ddorri83@naver.com","0208")
# user2 = User("김가나","kkh@naver.com","0212")
# user3 = User("차학연","acha@naver.com","0630")

# User.print_number_of_users()



#14.다양한 데이터로 인스턴스 만들기
# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     @classmethod
#     def from_string(cls, string_params):
#         name, email, password = string_params.split(',')
#         return cls(name, email, password)
#     @classmethod
#     def from_list(cls, list_params):
#         name, email, password = list_params
#         return cls(name, email, password)

# # 유저 생성 및 초기값 설정
# jaeseon = User.from_string("박재선,ddorri83@naver.com,0208")
# kyu = User.from_list(["김가나", "kkh@naver.com", "0212"])

# print(jaeseon.name, jaeseon.email, jaeseon.password)
# print(kyu.name, kyu.email, kyu.password)





#16.정적 메소드
# class User:

#     count = 0


#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#         User.count += 1 


#     def say_hello(self):
#         print(f"안녕하세요! 저는 {self.name}입니다!")

#     def login(self, email, password):
#         if self.email == email and self.password == password:
#             print("로그인 성공, 환영합니다")
#             self.say_hello()
#         else:
#             print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

#     def __str__(self):
#         return f"사용자: {self.name}, 이메일: {self.email}"

#     #파이썬 데코레이터
#     @classmethod
#     def print_number_of_users(cls):
#         print(f"총 유저 수는: {cls.count}입니다.")

#     #정적 메소드는 데코레이터를 사용해야하므로 @staticmethod를 사용한다
#     @staticmethod
#     def valid_email(email):
#         return "@" in email
    
# print(User.valid_email("jaeseon@naver.com"))

#20. 플레이리스트 합치기
# class Song:
# 	def __init__(self, title, artist, year):
# 		self.title = title
# 		self.artist = artist
# 		self.year = year

# 	def __str__(self):
# 		return f"{self.title} - {self.artist} ({self.year})"


# class PlayList:
# 	def __init__(self, songs):
# 		self.songs = songs

# 	def __str__(self):
# 		result = f"플레이리스트 안 노래들:\n\n"
# 		for song in self.songs:
# 			result += f"{song}\n"
# 		return result

# 	def __add__(self, other):
# 	    return PlayList(self.songs + other.songs)

# # 실행 코드
# rolling_in_the_deep = Song("Rolling in the Deep", "Adele", 2011)
# call_me_maybe = Song("Call Me Maybe", "Carly Rae Jepsen", 2012)
# get_lucky = Song("Get Lucky", "Daft Punk", 2013)
# uptown_funk = Song("Uptown Funk", "Mark Ronson", 2015)

# palette = Song("Pallete(팔레트)", "아이유", 2017)
# chained_up = Song("사슬", "빅스", 2015)
# tt = Song("TT", "트와이스", 2016)

# us_pop_2010s = PlayList([rolling_in_the_deep, call_me_maybe, get_lucky, uptown_funk])
# k_pop_2010s = PlayList([palette, chained_up, tt])

# pop_2010s = us_pop_2010s + k_pop_2010s
# print(pop_2010s)




