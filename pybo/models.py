from pybo import db

class RootUser(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)



#---------------------------------------------------------------
# index 부분도 db로 만들어주기




#---------------------------------------------------------------
# MEMBERS -> Current Students inform
class MemberCurrent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # korean name
    kname = db.Column(db.String(30),nullable=True)
    # english name
    ename = db.Column(db.String(30),nullable=True)
    # degree
    degree = db.Column(db.String(15),nullable=False)
    # e-mail
    email = db.Column(db.String(80),nullable=False)
    # create_date
    create_date = db.Column(db.DateTime(), nullable=False)
    # img file
    image_path = db.Column(db.String(255),nullable=True)
    # folder
    folder = db.Column(db.String(30),nullable=True)
    # modify date
    modify_date = db.Column(db.DateTime(),nullable=True)


# MEMBERS -> Alumni inform
class MemberAlumni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # korean name
    kname = db.Column(db.String(30),nullable=True)
    # english name
    ename = db.Column(db.String(30),nullable=True)
    # degree
    degree = db.Column(db.String(15),nullable=False)
    # company
    company = db.Column(db.String(50),nullable=True)
    # create_date
    create_date = db.Column(db.DateTime(), nullable=False)
    # img file
    image_path = db.Column(db.String(255),nullable=True)
    # folder
    folder = db.Column(db.String(30),nullable=True)
    # modify date
    modify_date = db.Column(db.DateTime(),nullable=True)

# MEMBERS -> Professor inform
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # professor's name
    name = db.Column(db.String(50),nullable=False)
    # professor's department
    department = db.Column(db.String(30),nullable=False)
    # Phone number
    phone = db.Column(db.String(20),nullable=True)
    # email
    email = db.Column(db.String(30),nullable=True)
    # office phone number
    office_phone = db.Column(db.String(30),nullable=True)
    # address korean
    kaddress = db.Column(db.String(50),nullable=True)
    # address english
    eaddress = db.Column(db.String(100),nullable=True)
    # Education 을 가져올 변수
    educations = db.relationship('Education',backref='professor',lazy=True)
    # Career 를 가져올 변수
    career = db.relationship('Career',backref='professor',lazy=True)
    # Research pages 를 가져올 변수
    research = db.relationship('ResearchPage',backref='professor',lazy=True)
    # img file
    image_path = db.Column(db.String(255),nullable=True)
    # folder
    folder = db.Column(db.String(30),nullable=True)
    # modify date
    modify_date = db.Column(db.DateTime(),nullable=True)


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer,db.ForeignKey('professor.id'),nullable=False)
    period = db.Column(db.String(20),nullable=False)
    edegree = db.Column(db.String(20),nullable=False)
    kdegree = db.Column(db.String(80),nullable=False)
    edegreeDetail = db.Column(db.String(100),nullable=False)

class Career(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer,db.ForeignKey('professor.id'),nullable=False)
    period = db.Column(db.String(20),nullable=False)
    # position in english
    eposition = db.Column(db.String(30),nullable=False)
    # position in korean
    kposition = db.Column(db.String(30),nullable=False)
    # position in english detail
    epositionDetail = db.Column(db.String(127),nullable=False)

class ResearchPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer,db.ForeignKey('professor.id'),nullable=False)
    # professor's research pages url_path
    url_path = db.Column(db.String(255),nullable=False)
    # prfessor's research pages detail
    page = db.Column(db.String(30),nullable=True)


#---------------------------------------------------------------
# NEWS inform -> image 부분 바꿔주기(다른 db로) -> 완료
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # activity date
    activity_date = db.Column(db.String(30),nullable=False)
    # activity
    activity = db.Column(db.Text(),nullable=False)
    # View text
    content = db.Column(db.Text(), nullable=True)
    # View img -> img path 삭제해주기!!!, 기존에 있는 데이터 삭제후
    # image_path = db.Column(db.String(255),nullable=True) 삭제용 주석
    # create_date
    create_date = db.Column(db.DateTime(), nullable=False)
    # images 관계 맺어주기
    images = db.relationship('NewsImg',backref='news',lazy=True)
    # modify date
    modify_date = db.Column(db.DateTime(),nullable=True)
    

# NEWS img를 저장할 클래스
class NewsImg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    # news_id
    news_id = db.Column(db.Integer,db.ForeignKey('news.id'),nullable=False)
    # news_img_path
    image_path = db.Column(db.String(255),nullable=False)
    # folder
    folder = db.Column(db.String(30),nullable=False)


#---------------------------------------------------------------
# PROJECTS inform -> period를 기준으로 Current와 Past 나눠주기
class Projects(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    # title
    title = db.Column(db.String(511),nullable=False)
    # Project duration & Agency
    duration = db.Column(db.String(30),nullable=False)
    Agency = db.Column(db.String(50),nullable=False)
    # image
    image_path = db.Column(db.String(255),nullable=False)
    # Past or Current
    period = db.Column(db.String(20),nullable=False)
    # create_date
    create_date = db.Column(db.DateTime(), nullable=False)
    # img file
    image_path = db.Column(db.String(255),nullable=True)
    # folder
    folder = db.Column(db.String(30),nullable=True)
    # modify date
    modify_date = db.Column(db.DateTime(),nullable=True)

#---------------------------------------------------------------
# PUBLICATIONS -> 한번에 다하고 category에 따라서 IC, IJ IP등 나눠주기
class Publications(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    # date
    date = db.Column(db.String(20),nullable=False)
    # title
    title = db.Column(db.String(255),nullable=False)
    # Authors
    author = db.Column(db.String(127),nullable=False)
    # read more -> link
    read_more = db.Column(db.String(127),nullable=True)
    # category
    category = db.Column(db.String(30),nullable=False)
    # create_date
    create_date = db.Column(db.DateTime(),nullable=False)
    # modify date
    modify_date = db.Column(db.DateTime(),nullable=True)


#---------------------------------------------------------------
# CONTACT inform






