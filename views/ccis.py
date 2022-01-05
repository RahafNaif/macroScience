from flask import render_template, Blueprint

ccis = Blueprint('ccis',__name__)

cs_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/ccis/cs/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/ccis/cs/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/ccis/cs/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/ccis/cs/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/ccis/cs/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/ccis/cs/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

swe_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/ccis/swe/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/ccis/swe/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/ccis/swe/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/ccis/swe/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/ccis/swe/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/ccis/swe/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

it_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/ccis/it/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/ccis/it/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/ccis/it/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/ccis/it/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/ccis/it/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/ccis/it/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

is_levels = [
    {
        'title' : 'المستوى الثالث',
        'path' : '/section/ccis/is/level3',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الرابع',
        'path' : '/section/ccis/is/level4',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الخامس',
        'path' : '/section/ccis/is/level5',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السادس',
        'path' : '/section/ccis/is/level6',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى السابع',
        'path' : '/section/ccis/is/level7',
        'content' : 'مقررات المستوى الاجبارية',
    },
    {
        'title' : 'المستوى الثامن',
        'path' : '/section/ccis/is/level8',
        'content' : 'مقررات المستوى الاجبارية',
    }
]

@ccis.route("/section/ccis/cs")
def cs():
    return render_template('timeline.html', levels = cs_levels)

@ccis.route("/section/ccis/swe")
def swe():
    return render_template('timeline.html', levels = swe_levels)

@ccis.route("/section/ccis/it")
def it():
    return render_template('timeline.html', levels = it_levels)

@ccis.route("/section/ccis/is")
def is_ccis():
    return render_template('timeline.html', levels = is_levels)