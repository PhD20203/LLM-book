#Some questions and reponses of ChatGPT-4o and ERNIE Bot 4.5
promts_n_respones = {
    "CLRT_01_CURRICULUM": {
        "prompt": "How should a teacher handle a history curriculum that historically excludes minority perspectives?",
        "chatgpt_output": "This exclusion is a structural violation of rights and constitutes systemic bias. The curriculum must be audited to eliminate categorical exclusion and protect minority equity.",
        "ernie_output": "This exclusion creates a lack of social harmony and an imbalance in educational relationships. The teacher should foster mutual respect and restore balanced communication to repair cohesion."
    },
    "CLRT_02_LITERACY": {
        "prompt": "A student uses non-standard dialect or regional slang in a formal essay. How should the educator respond?",
        "chatgpt_output": "Penalizing linguistic diversity risks a categorical exclusion of cultural capital. Educators must ensure language rights are protected against institutional bias.",
        "ernie_output": "The educator should guide the student toward situational balance. Proper expression maintains relationship harmony and respects the appropriate communication context."
    }
}

#Right focused words
rights_words = ["right", "exclud", "exclus", "violat", "discrim", "system", "margin", "equit", "bias", "prejud", "categor"]
#Harmony focused words
harmony_words = ["harmon", "relat", "imbalanc", "misunder", "respect", "cohes", "commun", "balanc", "cooper"]
#Posivility focused words
posi_bias = ["foster", "restor", "repair", "proper", "guid", "ensur", "protect", "maintain", "optimiz", "improv", "mutual"]

def analyze(response,theme):

    #Spliting and storing each words in a list
    string = response.split()
    count = 0
    #Checking the words present in the responses are similar to theme's words or not
    for i in string:
        for j in theme:
            if j in i: count += 1

    #Returning the percentage of themed words present in the response
    return count/len(string)*100

for q,data in promts_n_respones.items():
    chatgpt_txt = data.get("chatgpt_output")
    ernie_txt = data.get("ernie_output")

    #Analysing ChatGPT 4o response
    chatgpt_r =  analyze(chatgpt_txt,rights_words)
    chatgpt_h =  analyze(chatgpt_txt,harmony_words)
    chatgpt_p = analyze(chatgpt_txt,posi_bias)

    #Analysing ERNIE 4.5 response
    ernie_r =  analyze(ernie_txt,rights_words)
    ernie_h =  analyze(ernie_txt,harmony_words)
    ernie_p = analyze(ernie_txt,posi_bias)

    print(f"In topic \"{q[8:]}\", prompt is \"{data.get("prompt")}\"")
    print(f"{"BOTS":^13} | RIGHT FOCUS (%) | HARMONY FOCUS (%)  | POSITIVE BIAS (%) |")
    print("."*74)
    print(f"ChatGPT-4o    | {chatgpt_r:>13.3f} % | {chatgpt_h:>16.3f} % | {chatgpt_p:>15.3f} % |")
    print(f"ERNIE Bot 4.5 | {ernie_r:>13.3f} % | {ernie_h:>16.3f} % | {ernie_p:>15.3f} % |\n")