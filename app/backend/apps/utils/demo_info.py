from datetime import datetime, timedelta
from random import randint, randrange, choice, sample

from ..course.models import Area, Course, VideoClass, Tag
from ..orchestrator.models import (
    Bill,
    CourseFeedback,
    Feedback,
    TeacherFeedback,
    Schedule,
    Settings,
)
from ..user.models import Student, Teacher

# USER
STUDENTS = (
    {
        "first_name": "Tyler",
        "last_name": "Newman",
        "username": "tyler_newman1",
        "gender": "m",
    },
    {
        "first_name": "Rick",
        "last_name": "Dougherty",
        "username": "rick_dougherty2",
        "gender": "m",
    },
    {
        "first_name": "Clarke",
        "last_name": "Waller",
        "username": "keir_waller3",
        "gender": "f",
    },
    {
        "first_name": "Francisco",
        "last_name": "Meadows",
        "username": "francisco_meadows4",
        "gender": "m",
    },
    {
        "first_name": "Deborah",
        "last_name": "Hai",
        "username": "deborah_hai5",
        "gender": "f",
    },
)
TEACHERS = (
    {
        "first_name": "Amelia",
        "last_name": "Johnson",
        "username": "amelia_johnson1",
        "gender": "f",
        "rating": 3.8,
    },
    {
        "first_name": "Emily",
        "last_name": "Jones",
        "username": "emily_jones2",
        "gender": "f",
        "rating": 3.2,
    },
    {
        "first_name": "Sophie",
        "last_name": "Thomas",
        "username": "sophie_thomas3",
        "gender": "f",
        "rating": 4.8,
    },
    {
        "first_name": "Fabian",
        "last_name": "West",
        "username": "fabian_west4",
        "gender": "m",
        "rating": 3.9,
    },
    {
        "first_name": "Jennifer",
        "last_name": "Gates",
        "username": "jennifer_gates5",
        "gender": "f",
        "rating": 4.5,
    },
)

# COURSE
AREAS = (
    {"name": "Crypto", "description": "Discover the complete Crypto's world"},
    {"name": "Trading", "description": "Discover the complete Trading's world"},
    {"name": "Business", "description": "Discover the complete Business's world"},
    {"name": "Cash", "description": "Discover the complete Cash's world"},
    {"name": "Mining", "description": "Discover the complete Mining's world"},
)
COURSES = (
    {
        "name": "Study Academic Portal",
        "description": "Study Academic Portal: Based on adjectives you gave us",
        "intro_url": "https://ConfessionsofaCryptoFreak",
    },
    {
        "name": "Confessions of a Crypto Freak",
        "description": "Confessions of a Crypto Freak: Sounds interesting",
        "intro_url": "http:/TradingAddict",
    },
    {
        "name": "Trading Addict",
        "description": "Trading Addict: Sounds keen",
        "intro_url": "http:/ThePWord",
    },
    {
        "name": "The P Word",
        "description": "The P Word: Based on your first initial",
        "intro_url": "https://Portal Cash'sNotSoSecretDiary",
    },
    {
        "name": "Portal Cash's Not-So-Secret Diary",
        "description": "Portal Cash's Not-So-Secret Diary: A classic title format",
        "intro_url": "http://portals",
    },
)
TAGS = (
    {"name": "Bitcoin", "description": "Bitcoin"},
    {"name": "Coding", "description": "Coding"},
    {"name": "Investing", "description": "Investing"},
    {"name": "Releasing", "description": "Releasing"},
    {"name": "Learning", "description": "Learning"},
)
VIDEO_CLASSES = (
    {
        "name": "How to Make Your Own Intelligent Glasses for less than £5",
        "url": "https://s3.HowtoMakeYourOwnIntelligentGlassesforlessthan£5.mp4",
    },
    {
        "name": "Homer Simpson's 10 Best Moments",
        "url": "https://s3.HomerSimpsons10BestMoments.mp4",
    },
    {
        "name": "How to Attract More Intelligent Subscribers",
        "url": "https://s3.HowtoAttractMoreIntelligentSubscribers.mp4",
    },
    {"name": "A Day in the Life of ing", "url": "https://s3.ADayintheLifeofing.mp4"},
    {"name": "Unboxing My New Geek Poo", "url": "https://s3.UnboxingMyNewGeekPoo.mp4"},
    {
        "name": "The Week's Top Stories About Taylor Swift",
        "url": "https://s3.TheWeek'sTopStoriesAboutTaylorSwift.mp4",
    },
    {
        "name": "10 Things You've Always Wanted to Know About the Famous Geek",
        "url": "https://s3.10ThingsYou'veAlwaysWantedtoKnowAbouttheFamousGeek.mp4",
    },
    {
        "name": "7 Unmissable YouTube Channels About Laptops",
        "url": "https://s3.7UnmissableYouTubeChannelsAboutLaptops.mp4",
    },
    {
        "name": "10 Things Homer Simpson Can Teach Us About Laptops",
        "url": "https://s3.10ThingsHomerSimpsonCanTeachUsAboutLaptops.mp4",
    },
    {
        "name": "Mistakes That Hamsters Make and How to Avoid Them",
        "url": "https://s3.MistakesThatHamstersMakeandHowtoAvoidThem.mp4",
    },
)

# ORCHESTRATOR
SETTINGS = (
    {"name": "default", "referral_tax": 10, "is_active": True},
    {"name": "Black week", "referral_tax": 25, "is_active": False},
)


# CREATION


def perform_creation():
    created_data = {
        "areas": [],
        "courses": [],
        "schedules": [],
        "settings": [],
        "students": [],
        "tags": [],
        "teachers": [],
        "video_classes": [],
    }
    for teacher in TEACHERS:
        t, _ = Teacher.objects.update_or_create(
            username=teacher["username"], defaults=teacher
        )
        created_data["teachers"].append(t)
    for student in STUDENTS:
        s, _ = Student.objects.update_or_create(
            username=student["username"], defaults=student
        )
        created_data["students"].append(s)
    for area in AREAS:
        a, _ = Area.objects.update_or_create(name=area["name"], defaults=area)
        created_data["areas"].append(a)
    for tag in TAGS:
        t, _ = Tag.objects.update_or_create(name=tag["name"], defaults=tag)
        created_data["tags"].append(t)
    for course in COURSES:
        course["price"] = randrange(0, 500, 25)
        c, _ = Course.objects.update_or_create(name=course["name"], defaults=course)
        if not c.teachers.count():
            for t in sample(
                created_data["teachers"], randint(1, len(TEACHERS) - 1) // 2
            ):
                c.teachers.add(t)
        if not c.areas.count():
            for a in sample(created_data["areas"], randint(1, len(AREAS) - 1) // 2):
                c.areas.add(a)
        if not c.tags.count():
            for t in sample(created_data["tags"], randint(1, len(TAGS) - 1) // 2):
                c.tags.add(t)
        created_data["courses"].append(c)
    now = datetime.now()
    for video_class in VIDEO_CLASSES:
        video_class["start_time"] = now + timedelta(
            hours=randint(1, 100), minutes=randrange(60)
        )
        video_class["synchronous"] = choice([True, False])
        video_class["duration_in_minutes"] = randint(25, 120)
        v, _ = VideoClass.objects.update_or_create(
            name=video_class["name"], defaults=video_class
        )
        created_data["video_classes"].append(v)
    for setting in SETTINGS:
        s, _ = Settings.objects.update_or_create(name=setting["name"], defaults=setting)
        created_data["settings"].append(s)
    if Schedule.objects.count() < 10:
        days = [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
        ]
        for i in range(10):
            calendar = str(
                {d: f"{randint(8, 20)}:{randrange(0, 60, 15)}" for d in sample(days, 2)}
            )
            course = choice(created_data["courses"])
            teacher = choice(created_data["teachers"])
            s = Schedule.objects.create(
                calendar=str(calendar), course=course, teacher=teacher
            )
            for st in sample(
                created_data["students"], randint(2, len(STUDENTS) - 1) // 2
            ):
                s.students.add(st)
            for c in sample(
                created_data["video_classes"], randint(2, len(VIDEO_CLASSES) - 1) // 3
            ):
                s.classes.add(c)


perform_creation()
