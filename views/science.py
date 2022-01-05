from flask import render_template, Blueprint

science = Blueprint('science',__name__)

math_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/math/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/math/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/math/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/math/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/math/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/math/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

actu_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/actu/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/actu/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/actu/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/actu/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/actu/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/actu/level8',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى التاسع',
        'path' : '/section/science/actu/level9',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

chem_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/chem/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/chem/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/chem/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/chem/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/chem/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/chem/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

bch_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/bch/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/bch/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/bch/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/bch/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/bch/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/bch/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

bot_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/bot/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/bot/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/bot/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/bot/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/bot/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/bot/level8',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى التاسع',
        'path' : '/section/science/bot/level9',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

mbio_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/mbio/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/mbio/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/mbio/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/mbio/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/mbio/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/mbio/level8',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى التاسع',
        'path' : '/section/science/mbio/level9',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

stat_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/stat/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/stat/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/stat/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/stat/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/stat/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/stat/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

phys_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/science/phys/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/science/phys/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/science/phys/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/science/phys/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/science/phys/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/science/phys/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

@science.route("/section/science/phys")
def phys():
    return render_template('timeline.html', levels=phys_levels)

@science.route("/section/science/math")
def math():
    return render_template('timeline.html', levels=math_levels)

@science.route("/section/science/actu")
def actu():
    return render_template('timeline.html', levels=actu_levels)

@science.route("/section/science/bot")
def bot():
    return render_template('timeline.html', levels=bot_levels)

@science.route("/section/science/stat")
def stat():
    return render_template('timeline.html', levels=stat_levels)

@science.route("/section/science/chem")
def chem():
    return render_template('timeline.html', levels=chem_levels)

@science.route("/section/science/bch")
def bch():
    return render_template('timeline.html', levels=bch_levels)

@science.route("/section/science/mbio")
def mbio():
    return render_template('timeline.html', levels=mbio_levels)