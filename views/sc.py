from flask import render_template, Blueprint

sc = Blueprint('sc', __name__)

#math------------------------------------------------------------------------------
math_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/math/level3")
def math3():
    return render_template('level.html')

math_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/math/level4")
def math4():
    return render_template('level.html', level= swe_4)

math_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/math/level5")
def math5():
    return render_template('level.html')

math_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/math/level6")
def math6():
    return render_template('level.html')

math_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/math/level7")
def math7():
    return render_template('level.html')

math_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/math/level8")
def math8():
    return render_template('level.html')

#chem-------------------------------------------------------------

chem_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/chem/level3")
def chem3():
    return render_template('level.html')

chem_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/chem/level4")
def chem4():
    return render_template('level.html')

chem_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/chem/level5")
def chem5():
    return render_template('level.html')

chem_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/chem/level6")
def chem6():
    return render_template('level.html')

chem_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/chem/level7")
def chem7():
    return render_template('level.html')

chem_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/chem/level8")
def chem8():
    return render_template('level.html')

#bch----------------------------------------------------------------------------------------------

bch_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bch/level3")
def bch3():
    return render_template('level.html')

bch_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bch/level4")
def bch4():
    return render_template('level.html')

bch_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bch/level5")
def bch5():
    return render_template('level.html')

bch_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bch/level6")
def bch6():
    return render_template('level.html')

bch_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/science/ccis/bch/level7")
def bch7():
    return render_template('level.html')

bch_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bch/level8")
def bch8():
    return render_template('level.html')

#bot----------------------------------------------------------------------------------------------

bot_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bot/level3")
def bot3():
    return render_template('level.html')

bot_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bot/level4")
def bot4():
    return render_template('level.html')

bot_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bot/level5")
def bot5():
    return render_template('level.html')

bot_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bot/level6")
def bot6():
    return render_template('level.html')

bot_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bot/level7")
def bot7():
    return render_template('level.html')

bot_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bot/level8")
def bot8():
    return render_template('level.html')

bot_9 = {
    'title' : 'المستوى التاسع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/bot/level9")
def bot9():
    return render_template('level.html')

#mbio----------------------------------------------------------------------------------------------

mbio_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/mbio/level3")
def mbio3():
    return render_template('level.html')

mbio_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ': (علم الفيروسات العام (٢٥٠حدق',
            'content' : 'المادة باللغة العربية و تتكلم عن الصفات العامة للفيروسات، تركيبها، طرق تنميتها، طرق تصنيفها،     الفصائل ودورة التض<br>اعف (أكثر شيء ركزوا عليه \rواكتبوا \rملاحظات لأنه يخربط بس مره مهم)، الفيروسات البكتيرية، الإصابة الفيروسية، مكافحة الامراض الفيروسية، المضادات الفيروسية والعملي سهل بس في كم تجربة يبيلها تركيز طريقة المذاكرة: المادة\r دسمة وفيها معلومات \r كثير تحتاج مذاكرة اول بأول اكتبوا كل شيءوحاولوا ما تغيبون',
            'link':'#',
        },
        {
            'name': ':(علم البكتيريا العام (٢٦٠حدق',
            'content' : 'hhhhhjhhh',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/mbio/level4")
def mbio4():
    return render_template('level.html', level=mbio_4)

mbio_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/mbio/level5")
def mbio5():
    return render_template('level.html')

mbio_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/mbio/level6")
def mbio6():
    return render_template('level.html')

mbio_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/mbio/level7")
def mbio7():
    return render_template('level.html')

mbio_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/mbio/level8")
def mbio8():
    return render_template('level.html')

mbio_9 = {
    'title' : 'المستوى التاسع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/mbio/level9")
def mbio9():
    return render_template('level.html')

#phys----------------------------------------------------------------------------------------------

phys_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/phys/level3")
def phys3():
    return render_template('level.html')

phys_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/phys/level4")
def phys4():
    return render_template('level.html')

phys_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/phys/level5")
def phys5():
    return render_template('level.html')

phys_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/phys/level6")
def phys6():
    return render_template('level.html')

phys_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/phys/level7")
def phys7():
    return render_template('level.html')

phys_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/phys/level8")
def phys8():
    return render_template('level.html')

#stat----------------------------------------------------------------------------------------------

stat_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/stat/level3")
def stat3():
    return render_template('level.html')

stat_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/stat/level4")
def stat4():
    return render_template('level.html')

stat_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/stat/level5")
def stat5():
    return render_template('level.html')

stat_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/stat/level6")
def stat6():
    return render_template('level.html')

stat_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/stat/level7")
def stat7():
    return render_template('level.html')

stat_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/stat/level8")
def stat8():
    return render_template('level.html')

#actu----------------------------------------------------------------------------------------------

actu_3 = {
    'title' : 'المستوى الثالث',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/actu/level3")
def actu3():
    return render_template('level.html')

actu_4 = {
    'title' : 'المستوى الرابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/actu/level4")
def actu4():
    return render_template('level.html')

actu_5 = {
    'title' : 'المستوى الخامس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/actu/level5")
def actu5():
    return render_template('level.html')

actu_6 = {
    'title' : 'المستوى السادس',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/actu/level6")
def actu6():
    return render_template('level.html')

actu_7 = {
    'title' : 'المستوى السابع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/actu/level7")
def actu7():
    return render_template('level.html')

actu_8 = {
    'title' : 'المستوى الثامن',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/actu/level8")
def actu8():
    return render_template('level.html')

actu_9 = {
    'title' : 'المستوى التاسع',
    'course' : [
        {
            'name': ':عال ١١١ ',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        },
        {
            'name': ':ريض ١٠٦',
            'content' : 'gfffffffffggggggggggggggggggggggg',
            'link':'#',
        }
    ],
}

@sc.route("/section/science/actu/level9")
def actu9():
    return render_template('level.html')

