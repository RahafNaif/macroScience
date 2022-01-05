from flask import render_template, Blueprint

ccisLevels = Blueprint('ccisLevels', __name__)

#sweeeee
swe_3 = {
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

@ccisLevels.route("/section/ccis/swe/level3")
def sew3():
    return render_template('level.html', level= swe_3)

swe_4 = {
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

@ccisLevels.route("/section/ccis/swe/level4")
def sew4():
    return render_template('level.html', level= swe_4)

swe_5 = {
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

@ccisLevels.route("/section/ccis/swe/level5")
def sew5():
    return render_template('level.html', level= swe_5)

swe_6 = {
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

@ccisLevels.route("/section/ccis/swe/level6")
def swe6():
    return render_template('level.html', level= swe_6)

swe_7 = {
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

@ccisLevels.route("/section/ccis/swe/level7")
def sew7():
    return render_template('level.html', level= swe_7)

swe_8 = {
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

@ccisLevels.route("/section/ccis/swe/level8")
def sew8():
    return render_template('level.html', level= swe_8)

#css-------------------------------------------------------------

cs_3 = {
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

@ccisLevels.route("/section/ccis/cs/level3")
def cs3():
    return render_template('level.html')

cs_4 = {
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

@ccisLevels.route("/section/ccis/cs/level4")
def cs4():
    return render_template('level.html')

cs_5 = {
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

@ccisLevels.route("/section/ccis/cs/level5")
def cs5():
    return render_template('level.html')

cs_6 = {
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

@ccisLevels.route("/section/ccis/cs/level6")
def cs6():
    return render_template('level.html')

cs_7 = {
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

@ccisLevels.route("/section/ccis/cs/level7")
def cs7():
    return render_template('level.html')

cs_8 = {
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

@ccisLevels.route("/section/ccis/cs/level8")
def cs8():
    return render_template('level.html')

#it----------------------------------------------------------------------------------------------

it_3 = {
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

@ccisLevels.route("/section/ccis/it/level3")
def it3():
    return render_template('level.html')

it_4 = {
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

@ccisLevels.route("/section/ccis/it/level4")
def it4():
    return render_template('level.html')

it_5 = {
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

@ccisLevels.route("/section/ccis/it/level5")
def it5():
    return render_template('level.html')

it_6 = {
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

@ccisLevels.route("/section/ccis/it/level6")
def it6():
    return render_template('level.html')

it_7 = {
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

@ccisLevels.route("/section/ccis/it/level7")
def it7():
    return render_template('level.html')

it_8 = {
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

@ccisLevels.route("/section/ccis/it/level8")
def it8():
    return render_template('level.html')

#is----------------------------------------------------------------------------------------------

is_3 = {
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

@ccisLevels.route("/section/ccis/is/level3")
def is3():
    return render_template('level.html')

is_4 = {
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

@ccisLevels.route("/section/ccis/is/level4")
def is4():
    return render_template('level.html')

is_5 = {
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

@ccisLevels.route("/section/ccis/is/level5")
def is5():
    return render_template('level.html')

is_6 = {
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

@ccisLevels.route("/section/ccis/is/level6")
def is6():
    return render_template('level.html')

is_7 = {
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

@ccisLevels.route("/section/ccis/is/level7")
def is7():
    return render_template('level.html')

is_8 = {
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

@ccisLevels.route("/section/ccis/is/level8")
def is8():
    return render_template('level.html')
