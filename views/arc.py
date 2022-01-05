from flask import render_template, Blueprint

arc = Blueprint('arc',__name__)

arc_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/arch/arch/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/arch/arch/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/arch/arch/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/arch/arch/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/arch/arch/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/arch/arch/level8',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى التاسع',
        'path' : '/section/arch/arch/level9',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى العاشر',
        'path' : '/section/arch/arch/level10',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

plan_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/arch/plan/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/arch/plan/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/arch/plan/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/arch/plan/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/arch/plan/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/arch/plan/level8',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى التاسع',
        'path' : '/section/arch/plan/level9',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى العاشر',
        'path' : '/section/arch/plan/level10',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

@arc.route("/section/arch/plan")
def arch():
    return render_template("timeline.html", levels= plan_levels)

@arc.route("/section/arch/arch")
def archPlan():
    return render_template("timeline.html", levels= arc_levels)

#arch----------------------------------------------------------------------------------------------

arch_3 = {
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

@arc.route("/section/arch/arch/level3")
def arch3():
    return render_template('level.html')

arch_4 = {
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

@arc.route("/section/arch/arch/level4")
def arch4():
    return render_template('level.html')

arch_5 = {
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

@arc.route("/section/arch/arch/level5")
def arch5():
    return render_template('level.html')

arch_6 = {
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

@arc.route("/section/arch/arch/level6")
def arch6():
    return render_template('level.html')

arch_7 = {
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

@arc.route("/section/arch/arch/level7")
def arch7():
    return render_template('level.html')

arch_8 = {
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

@arc.route("/section/arch/arch/level8")
def arch8():
    return render_template('level.html')

#plan----------------------------------------------------------------------------------------------

plan_3 = {
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

@arc.route("/section/arch/plan/level3")
def plan3():
    return render_template('level.html')

plan_4 = {
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

@arc.route("/section/arch/plan/level4")
def plan4():
    return render_template('level.html')

plan_5 = {
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

@arc.route("/section/arch/plan/level5")
def plan5():
    return render_template('level.html')

plan_6 = {
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

@arc.route("/section/arch/plan/level6")
def plan6():
    return render_template('level.html')

plan_7 = {
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

@arc.route("/section/arch/plan/level7")
def plan7():
    return render_template('level.html')

plan_8 = {
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

@arc.route("/section/arch/plan/level8")
def plan8():
    return render_template('level.html')
