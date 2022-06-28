from datetime import datetime, timedelta
from random import randint, randrange, choice, sample, uniform

from django.contrib.auth.hashers import make_password

from backend.apps.utils.constants import PAYMENT_STATUSES
from backend.apps.course.models import Area, Course, VideoClass, Tag
from backend.apps.orchestrator.models import (
    Invoice,
    CourseFeedback,
    Feedback,
    TeacherFeedback,
    Schedule,
    Settings,
)
from backend.apps.user.models import Student, Teacher

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
        "username": "clarke_waller3",
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
    },
    {
        "first_name": "Emily",
        "last_name": "Jones",
        "username": "emily_jones2",
        "gender": "f",
    },
    {
        "first_name": "Sophie",
        "last_name": "Thomas",
        "username": "sophie_thomas3",
        "gender": "f",
    },
    {
        "first_name": "Fabian",
        "last_name": "West",
        "username": "fabian_west4",
        "gender": "m",
    },
    {
        "first_name": "Jennifer",
        "last_name": "Gates",
        "username": "jennifer_gates5",
        "gender": "f",
    },
)

# COURSE
AREAS = (
    {"name": "Crypto", "description": "Discover the complete Crypto's world"},
    {"name": "Trading", "description": "Discover the complete Trading's world"},
    {"name": "Business", "description": "Discover the complete Business's world"},
    {"name": "Mining", "description": "Discover the complete Mining's world"},
    {"name": "GoArbit", "description": "Discover the complete GoArbit's world"},
)
COURSES = (
    {
        "name": "Study Academic Portal",
        "description": "Study Academic Portal: Based on adjectives you gave us",
    },
    {
        "name": "Confessions of a Crypto Freak",
        "description": "Confessions of a Crypto Freak: Sounds interesting",
    },
    {"name": "Trading Addict", "description": "Trading Addict: Sounds keen"},
    {"name": "The P Word", "description": "The P Word: Based on your first initial"},
    {
        "name": "Portal Cash's Not-So-Secret Diary",
        "description": "Portal Cash's Not-So-Secret Diary: A classic title format",
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
        "invoices": [],
        "courses": [],
        "schedules": [],
        "settings": [],
        "students": [],
        "tags": [],
        "teachers": [],
        "video_classes": [],
    }
    for teacher in TEACHERS:
        teacher["rating"] = uniform(3, 5)
        teacher["password"] = make_password("123")
        t, _ = Teacher.objects.update_or_create(
            username=teacher["username"], defaults=teacher
        )
        created_data["teachers"].append(t)
    for student in STUDENTS:
        student["password"] = make_password("123")
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
        course["price"] = randrange(99900, 999900, 50000)
        pre = ["Working with ", "Relating ", ""]
        pos = [" importance.", " relation.", " meaning.", "."]
        course[
            "intro_url"
        ] = "https://productsimgs.s3.us-east-2.amazonaws.com/Sony+4K+Demo_+Another+World.mp4"
        course["thumbnail"] = choice(
            [
                "https://revistabyte.es/wp-content/uploads/2018/10/back-to-the-future-696x392.jpg.webp",
                "https://www.edx.org/static/9f3ff114d126f7b248ed5bd72adc5dbb/Aprende_trading.jpg",
                "https://assets.iproup.com/cdn-cgi/image/w=880,f=webp/https://assets.iproup.com/assets/jpg/2021/09/22155.jpg",
                "https://www.noticiasconfirmadas.com/wp-content/uploads/2022/02/74c03414-1ed9-4703-a287-2f521a2b7177_alta-libre-aspect-ratio_default_0.jpg",
            ]
        )
        content = [
            f"{choice(pre)}{choice(AREAS)['name']} and his {choice(TAGS)['name']}{choice(pos)}"
            for i in range(10)
        ]
        c, _ = Course.objects.update_or_create(
            name=course["name"], content=content, defaults=course
        )
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
            start_time = now + timedelta(hours=randint(1, 100), minutes=randrange(60))
            s = Schedule.objects.create(
                calendar=str(calendar),
                course=course,
                teacher=teacher,
                start_time=start_time,
            )
            created_data["schedules"].append(s)
            for st in sample(
                created_data["students"], randint(2, len(STUDENTS) - 1) // 2
            ):
                s.students.add(st)
            for c in sample(
                created_data["video_classes"], randint(2, len(VIDEO_CLASSES) - 1) // 3
            ):
                s.classes.add(c)
    else:
        created_data["schedules"] = Schedule.objects.all()
    if Invoice.objects.count() < 10:
        payment_methods = [
            "Efectivo",
            "Tarjeta de crédito",
            "Transferencia bancaria",
            "Bitcoin",
        ]
        for i in range(10):
            buyer = choice(created_data["students"])
            schedule = choice(created_data["schedules"])
            amount = schedule.course.price
            payment_status = choice(PAYMENT_STATUSES)[0]
            payment_method = choice(payment_methods)
            reference = f"reference-{i}"
            wompi_id = f"wompi_id-{i}"
            b = Invoice.objects.create(
                buyer=buyer,
                schedule=schedule,
                amount=amount,
                payment_status=payment_status,
                payment_method=payment_method,
                reference=reference,
                wompi_id=wompi_id,
            )
            created_data["invoices"].append(b)
