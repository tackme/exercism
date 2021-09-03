def round_scores(student_scores):
    '''
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    '''

    return [round(l) for l in reversed(student_scores)]


def count_failed_students(student_scores):
    '''
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    '''

    return len([l for l in student_scores if l <= 40])

def above_threshold(student_scores, threshold):
    '''
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    '''

    return [l for l in student_scores if l >= threshold]

def letter_grades(highest):
    '''
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    '''
    threshold = 41

    return list(range(threshold, highest, round((highest - threshold) / 4)))

def student_ranking(student_scores, student_names):
    '''
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     '''

    return [f"{index+1}. {name}: {score}" for index, (score, name) in enumerate(zip(student_scores, student_names))]

def perfect_score(student_info):
    '''
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    '''
    for l in student_info:
        if l[1] == 100:
            return l

    return "No perfect score."
