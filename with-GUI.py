from time import *
from tkinter import *
import random 
def mistake(ptest,itest):
    error=0
    itest=itest.split()
    ptest=ptest.split()
    try:
        for i in range(len(ptest)):
            if ptest[i]!=itest[i]:
                error+=1
    except:
        error+=1
    return error

def tspeed(t1,t2,user_input):
    delay=t2-t1
    delay1=round(delay,1)/60
    word_count=len(user_input.split())
    return round((word_count/delay1),1)

def start_test():
    global start_time
    start_time=time()
    text_label.config(text=random.choice(tests),font=("Arial",11))
    input_box.delete(1.0,END)
    result_label.config(text="")    

def result():
    test_end_time = time()
    user_input = input_box.get("1.0", END).strip()  # Get user input
    test_string = text_label.cget("text")  # Get the test string
    speed = tspeed(start_time, test_end_time, user_input)
    errors = mistake(test_string, user_input)
    result_label.config(text=f"Speed: {speed} WPM\nErrors: {errors}")
    
tests=["Typing efficiently requires more than just speed. Its about finding a balance between accuracy and momentum",
      "A consistent typing practice can help improve both speed and accuracy.",
      "Every proficient typist understands the importance of maintaining good posture while typing.",
      "The evolution of typing has been remarkable, from the mechanical typewriters of the past"]
st=Tk()
st.title("Typing speed Test")
st.geometry("600x400")
st.config(bg="lightblue")
st.iconbitmap("D:/Github pushed/Typing-Speed-Calculator/images.ico")
text_label=Label(st,text="Press start to begin",font=("Arial",14),bg="lightblue",)
text_label.pack(pady=20)
input_box=Text(st,height=6,font=("Arial",12),wrap=WORD)
input_box.pack(pady=11)
start_button=Button(st,font=("Arial",14),text="Start Test",command=start_test)
start_button.pack(pady=10)
result_button=Button(st,font=("Arial",14),text="Calculate Result",command=result)
result_button.pack(pady=10)
result_label = Label(st, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

st.mainloop()
