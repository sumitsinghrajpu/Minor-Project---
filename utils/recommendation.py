def subject_analysis(os_marks,
                     cd_marks,
                     ml_marks,
                     sd_marks):

    subjects = {
        "Operating System": os_marks,
        "Compiler Design": cd_marks,
        "Machine Learning": ml_marks,
        "System Design": sd_marks
    }

    strong = max(subjects,
                 key=subjects.get)

    weak = min(subjects,
               key=subjects.get)

    return strong, weak