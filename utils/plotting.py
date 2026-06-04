import matplotlib.pyplot as plt

def subject_plot(os_m,
                 cd_m,
                 ml_m,
                 sd_m,):

    subjects = [
        "OS",
        "CD",
        "ML",
        "SD"
    ]

    marks = [
        os_m,
        cd_m,
        ml_m,
        sd_m
    ]

    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)

    plt.bar(subjects,
            marks)
    plt.title("Each subject marks")
    plt.xlabel("Subject" ,color="green")
    plt.ylabel("marks",color="black")
    plt.subplot(1,2,2)
    plt.scatter(subjects,marks)
    plt.grid()
    plt.tight_layout()

    

    plt.title("Subject Performance")

    plt.ylabel("Marks")

    return plt
