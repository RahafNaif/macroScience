from flask import render_template, Blueprint, url_for

home = Blueprint('home', __name__)

ccis_list = [
    {
        'major': 'علوم الحاسب',
        'content': 'cs cs  ghyjgj',
        'img': 'img/coding.svg',
        'path': 'ccis/cs'
    },
    {
        'major': 'هندسة البرمجيات',
        'content': 'cs cs  ghyjgj',
        'img': 'img/coding.svg',
        'path': 'ccis/swe'
    },
    {
        'major': 'نظم المعلومات',
        'content': 'cs cs  ghyjgj',
        'img': 'img/coding.svg',
        'path': 'ccis/is'
    },
    {
        'major': 'تقنية المعلومات',
        'content': 'cs cs  ghyjgj',
        'img': 'img/coding.svg',
        'path': 'ccis/it'
    }
]

sc_list = [
    {
        'major': 'الرياضيات الاكتوارية ',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/actu'
    },
    {
        'major': 'كيمياء حيوية',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/bch'
    },
    {
        'major': 'نبات',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/bot'
    },
    {
        'major': 'كيمياء',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/chem'
    },
    {
        'major': 'رياضيات',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/math'
    },
    {
        'major': 'الاحياء الدقيقة',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/mbio'
    },
    {
        'major': 'فيزياء',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/phys'
    },
    {
        'major': 'إحصاء',
        'content': 'cs cs  ghyjgj',
        'img': 'img/science.svg',
        'path': 'science/stat'
    }
]

arc_list = [
    {
        'major': 'العمارة وعلوم البناء',
        'content': 'cs cs  ghyjgj',
        'img': 'img/blueprint.svg',
        'path': 'arch/arch'
    },
    {
        'major': 'التخطيط العمراني',
        'content': 'cs cs  ghyjgj',
        'img': 'img/blueprint.svg',
        'path': 'arch/plan'
    }
]


@home.route("/")
def homepage():
    return render_template("home.html")

@home.route("/section/ccis")
def ccis():
    return render_template('sections.html', ccis=ccis_list, stylee='col-lg-3 col-md-6')

@home.route("/section/science")
def sc():
    return render_template('sections.html', ccis=sc_list, stylee='col-lg-3 col-md-6')

@home.route("/section/architecture")
def arc():
    return render_template('sections.html', ccis=arc_list, stylee='col-md-6')