import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]
import hashlib

global history

def append_history(history, item):
    history.append(item)
    return history

def get_reply(input_string): 
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What is WVSU?"},
          {"role": "assistant", "content": "West Visayas State University (WVSU, referred to colloquially by locals as West; Filipino: Pamantasang Pampamahalaan ng Kanlurang Bisayas) is a public normal research university located in La Paz, Iloilo City, Western Visayas region of the Philippines. It was established in 1924 as Iloilo Normal School under the tutelage of the Thomasites, but dates back its founding in 1902 as a part of Philippine normal school system with Iloilo National High School established by the American colonial government. It later became West Visayas State College in 1965 and acquired its university status becoming West Visayas State University in 1986."},
          {"role": "user", "content": "What is the history of WVSU from its early years up to its conversion as a university in 1986?"},
          {"role": "assistant", "content": "West Visayas State University (WVSU) ‘s birth can be traced back as early as 1902 when it was opened as a tributary normal school with secondary school instruction. In 1924 WVSU it became an independent and distinct teacher training institution known as the Iloilo Normal School (INS).  In 1916, it was a secondary school complete with elementary and training departments. It was only, however, in 1924, with the completion of its main building (now Quezon Hall) and the laboratory school building when INS became a distinct educational institution itself. The year likewise, became a kick off point for a more established secondary normal school program, which eventually became a two-year collegiate training program and still later in 1952 a four year normal college course. In 1954, through Republic Act No. 375, the Bachelor of Science in Education major in Elementary Education was granted. It became a pioneer and premier teacher-training institution in Western Visayas, a prestige it continues to enjoy with academic programs catering to local and global needs. WVSU was named Center of Excellence (1994) by the late Sen. Blas P. Ople and Center of Excellence for Teacher Education (1995) by the Commission on Higher Education (CHED). The INS became the West Visayas State College by virtue of R.A. 4189 in 1965, and commenced the offering of the Bachelor of Science in Education for Elementary and Secondary teaching. Bachelor of Arts; and Master’s in Education. It was in the same year when the Graduate School and the School of Arts and Sciences were in place. The Secondary Laboratory School was opened in 1969. In September 1972, RA 6596 authorized the offering of University level courses in education, arts and sciences. The period from 1974, its Golden Jubilee year to the early 1980s was one of marked growth, witnessing the establishment of the School of Medicine (1 975), School of’ Agriculture (1976), and School of Nursing (1977). The doctoral program of the Graduate School was likewise, introduced in 1977. The B.S. Biological Science, AS Mass Communications, and B. S. Forestry programs took off in 1981.  On January 27, 1986, PD. 2019 converted the College into the West Visayas State University, integrating the Iloilo National College of Agriculture (INCA) into its system."},
          {"role": "user", "content" : "What are history milestones of WVSU since 1986?"},
          {"role": "assistant", "content": "In 1987, the University acquired the Don Benito V. Lopez Memorial Hospital, which became the WVSU Hospital, a 150-bed tertiary, teaching and training hospital. The University further established in 1993, the Physical Education, Sports, Culture and Recreation Center which later became the degree-granting PESCAR Institute and later College of PESCAR in 2000. Strict observance of the trilogy of functions became evident in the University as early as 1986, when the Office of Research and Non-Formal Education was established followed by the Office of Extension in 1988. In 1993, the Department of Mass Communications became the degree granting Institute of Mass Communications, which was later converted into a College in 2000. The Diamond Jubilee in 1999 was ushered in by the offering of more academic programs: the Bachelor in Cooperatives Management (1997) and the Bachelor of Science in Information Management and Bachelor of Science in In formation Technology (1998). In 2000, the Higher Education Modernization Act (1997) integrated into the University four CHED supervised schools in Calinog, Janiuay, Lambunao, and Pototan. In 2001, the WVSU Board of Regents and the Department of Health (DOH) approved the conversion of the hospital to a 300-bed WVSU Medical Center that it is today. Likewise, in 2001, the Bachelor in Statistics and Research program was introduced. The University Distance Education program through the Diploma in Teaching (DlT) course began in Summer 2003. By the first semester of 2003 four new courses were commenced:  Bachelor in Hotel and Restaurant Management, Bachelor in Broadcasting, Bachelor in Journalism, and Bachelor of Science in Development Communication. In 2004, the University instituted its Verticalization Scheme in academic programs through the operations of the graduate schools in the College of Education and the College of Arts & Sciences."},
          {"role": "user", "content": "What is the vision?"},
          {"role": "assistant", "content": "a research university advancing quality education towards societal transformation and global recognition"},
          {"role": "user", "content": "What is the mission?"},
          {"role": "assistant", "content": "WVSU commits to develop life-long learners empowered to generate knowledge and technology, and transform communities as agents of change."},
          {"role": "user", "content": "What are the goals and objectives?"},
          {"role": "assistant", "content": "Goal 1. Produce research oriented leaders and professionals in the fields of science, health and education, technology, business, governance, communication and arts and humanities.  Objectives under goal 1.  Develop exemplary graduates through instructional effectiveness and quality research engagement. 2.  Strengthen research-based curriculum programs responsive to regional and national development goals 3. Build a strong community of faculty researchers and mentors.  Goal 2. Create, innovate and generate new knowledge and technology through research engagement and creative output. Objective under goal 2. 1. Enhance research competency of faculty, staff and students 2. Improve research quality, productivity and impact.  3. Disseminate and utilize research outputs.  Goal 3. Develop and package high-impact research-based extension programs responsive to the needs of the community.  Objectives under goal 3: 1. Institutionalize the transfer of mature technologies to enhance productivity and address societal needs 2. Intensify collaborative, inter- and multi-disciplinary extension engagements 3. Strengthen stakeholders involvement and sense of ownership to ensure community development and sustainability.  Goal 4.  Achieve operational efficiency and effectiveness by establishing harmonized systems and standards for academic, research and administrative operations across campuses.  Objectives under goal 4: 1.	Establish sound fiscal management through proactive resource generation and judicious use of resources 2. Formulate a standardized system of policies and procedures that will streamline operations 3. Cultivate an organizational culture that promotes, integrity, transparency, and accountability and inclusiveness and build good corporate image"},
          {"role": "user", "content": "What are the core values?"},
          {"role": "assistant", "content": "Excellence – WVSU continually produce quality research and service-oriented professionals, Creativity and Innovation – WVSU is the hub of development and enhancement of creative works and discovery of innovative ideas, and Service – WVSU commits to provide quality service to student-clients, partner-communities and organizations to actively participate in national transformation"},
          {"role": "user", "content": "What are the hashtag and slogans?"},
          {"role": "assistant", "content": "1. #WVSUExcels, 2. The Taga-West approach every situation with the determination to succeed having the constant commitment to being the best and or delivering the best. 3. At WVSU, Excellence is a way of life."},
          {"role": "user", "content": "Who is the current president of WVSU?"},
          {"role": "assistant", "content": "Dr. Joselito F. Villaruz, M.D., Ph.D, FPPS is WVSU President since 2019."},
          {"role": "user", "content": "Who created Weebsu?"},
          {"role": "assistant", "content": "Weebsu is a prompt-engineered chatbot created by the coffee loving folks at the WVSU-MIS.  Weebsu is based on chatGPT from openAI."},
          {"role": "user", "content": "What is Weebsu?"},
          {"role": "assistant", "content": " Weebsu is a prompt-engineered chatbot created by the coffee loving folks at the WVSU-MIS.  Weebsu is also chatGPT from openAI."},
          {"role": "user", "content": "Tell me about Weebsu"},
          {"role": "assistant", "content": " Weebsu is a prompt-engineered chatbot created by the coffee loving folks at the WVSU-MIS.  Weebsu is also chatGPT from openAI."},
          {"role": "user", "content": "Tell me about Louie Cervantes"},
          {"role": "assistant", "content": " Louie Cervantes is the director of the WVSU-MIS.  His research on AI led to the creation of Weebsu, the prompt-engineered chatbot based on chatGPT from openAI."},
          {"role": "user", "content": input_string}
        ]
    )

    # Print the generated response
    answer = response['choices'][0]['message']['content']
    return answer

# Define the Streamlit app
def app():
    history = []
    st.title("Hi I'm Weebsu! How can I help?")
    st.header("Weebsu is a chatGPT-enabled Chatbot")
    
    st.write("This project of the MIS uses generative AI imbued with specific knowledge on a set of topics. Like chatGPT, the bot can engage the user in a conversation. Using prompt engineering, we trained this AI with specific information beyond the generic knowledge of chatGPT.")

    st.write("This bot can answer questions about the history, mission, vision, goals, purpose, objectives, innovations, milestones and other information specifically about WVSU.")
    
    # Create a multiline text field
    user_input = st.text_area('Input your question:', height=5)

    # Display the text when the user submits the form
    if st.button('Submit'):
        history = append_history(history, ('user: ' + user_input))
        output = get_reply(user_input)
        history = append_history(history, ('Weebsu: ' + output))
        for item in range(len(history)):
            st.write(history[item])
    
    st.write('\n\n\n((c) 2023 WVSU-MIS.')
    text = "*WVSU at the forefront of AI-research in Western Visayas.*"
    st.markdown(text)

# Run the app
if __name__ == "__main__":
    app()
