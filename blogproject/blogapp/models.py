from django.db import models
from accounts.models import myUser

#Blog객체 만들기
class Blog(models.Model): #models안의Model을 상속해야함
    title = models.CharField(max_length=200)  #뒤에 어떤타입인지도 명시
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    writer = models.ForeignKey(myUser, null = True, on_delete = models.CASCADE)
    #자동으로 지금시간 추가하겠다는 말
    
    def __str__(self): ##str 소문자로 해줘야함
        return self.title   #주소/admin 으로 들어간곳에서 Blog라는 란 에서 작성한글의
                            #제목이 title 이 되도록 설정하는
                            
class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post2 = models.ForeignKey(myUser, null = True, on_delete=models.CASCADE)
    # 어느 게시물에 달려있는 댓글인지    //참조하는 대상이 삭제되면 댓글도모두삭제
    
    def __str__(self): #이런건 DB자체를 변경시키는게 아니라 migration 필요x
        return self.comment  