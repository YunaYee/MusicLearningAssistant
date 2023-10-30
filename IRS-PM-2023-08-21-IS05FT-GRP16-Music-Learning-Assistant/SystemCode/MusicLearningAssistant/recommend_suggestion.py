import openai

def read_audio_stereo(beat_score,onvel_score,pitch_score):
    openai.api_key = "your api" 

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "I get the score of my piano play, the maximum score is 10 points, my beat score is"+str(beat_score)+", my onvel score is"+str(onvel_score)+", my pitch score is"+str(pitch_score)+",please give me a comment."}]
    )

    print(completion)


    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "I get the score of my piano play, the maximum score is 10 points, my beat score is"+str(beat_score)+", my onvel score is"+str(onvel_score)+", my pitch score is"+str(pitch_score)+",Please recommend another book to me to improve my skills."}]
    )

    print(completion)