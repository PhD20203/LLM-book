import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from deep_translator import GoogleTranslator

def load_csv_file():
    try:
        dfrme = pd.read_csv('agro_environmental_dataset.csv')
        return dfrme
    except FileNotFoundError as e:
        # If file not found ,Program stopped
        print(f"Error : {e}")
        exit()

df = load_csv_file()

# Necessary Parameters required for predicting Nitrogen Deficiency i.e. Target
parameter = [
    'bulk_density',
    'organic_matter_pct',
    'cation_exchange_capacity',
    'salinity_ec',
    'buffering_capacity',
    'soil_moisture_pct',
    'soil_temp_c',
    'air_temp_c',
    'light_intensity_par',
    'soil_ph'
]

# Target Parameter to predict
target = 'nitrogen_ppm'

#Stores the values of all parameters other than target's
x = df[parameter]
#Stores the values of target's parameters
y = df[target]

# random_state used to control randomness of the model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Training prediction model by using Random Forest Regressor ")

model = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=1)
model.fit(x_train, y_train)

def shap(model, target, bg_data, no=50):
    # Stores all the necessary Parameters
    para_names = list(target.index)
    # Store nos. of parameters
    no_para = len(para_names)

    # Creating a new dictionary of each parameter and setting to zero
    d = {f: 0.0 for f in para_names}

    #Stores the target's parameter's values
    target_v = target.values

    #Store all the other parameter's values
    bg_val = bg_data.values

    for _ in range(no):
        #Randomly choosing an index from all lists
        index = np.random.choice(len(bg_val))
        #Store the values of parameter from the chosen no.
        ref_v = bg_val[index]

        permutation = np.random.permutation(no_para)

        v_with = ref_v.copy()
        v_without = ref_v.copy()

        for idx in permutation:
            f_name = para_names[idx]
            v_with[idx] = target_v[idx]

            pred_with = model.predict(pd.DataFrame([v_with], columns=para_names))[0]
            pred_without = model.predict(pd.DataFrame([v_without], columns=para_names))[0]

            # Calculation the difference in predicted & actual values and stores it in dictionary
            d[f_name] += (pred_with - pred_without)
            v_without[idx] = target_v[idx]

    #It stores an average values
    dt = {f: d[f] / no for f in d}
    return dt

def get_recommendation(p_val, target):
    #As the names of the parameters names are separated by underscores ,it replaces with spaces
    name = target.replace('_', ' ').title()

    # Actions to take when a Parameter is chosen
    template = {
        'Organic Matter Pct': "Apply organic compost, manure, or implement cover-cropping.",
        'Soil Ph': "Apply lime if too acidic, or sulfur/gypsum if too alkaline, to balance nutrient intake.",
        'Soil Moisture Pct': "Fix field drainage system to prevent water logging, or optimize irrigation.",
        'Salinity Ec': "Put water to replace salts(Leaching) and ensure proper surface drainage.",
        'Soil Temp C': "Apply pre-emergent herbicide and reduce nitrogen rich fertilizer "
    }

    #If an Action is not present in the template ,it will use this default statement
    default_template = "Ensure standard balanced NPK fertilization practices and rotate crops with legumes."

    selected_action = template.get(name, default_template)

    headline = f"Alert: Nitrogen Deficiency Detected! Predicted level is {p_val:.1f} ppm (Optimal threshold is 100+ ppm)."
    reason = f"Root Cause Analysis: Your '{name}' value is the primary constraint holding down soil Nitrogen levels."
    action = f"Action Plan: {selected_action}"

    return headline, reason, action

def predict_to_data(indx):
    # Selected a data row of position "indx" for prediction
    target = x_test.iloc[indx]

    p_val = model.predict(target.to_frame().T)[0]

    #Gives random 100 sample datasets
    bg_sample = x_train.sample(100, random_state=42)

    #It will give a dictionary of parameter and its values
    #'no' specifies how many data points we have to compare
    scores = shap(model, target, bg_sample, no=40)

    sorted_scores = sorted(scores.items(), key=lambda a: a[1])

    neg_para, lowest_score = sorted_scores[0]

    print(f"\n DATA REPRESENTATION :-\n")
    for i, j in sorted_scores:
        #It tells how much the target varies from the model data
        bar = ("-" * int(abs(j) // 2) if j < 0 else "+" * int(j // 2))
        print(f"{i:<25} | Value: {target[i]:<8.2f} | Impact: {j:<7.2f} {bar}")

    headline, reason, action = get_recommendation(p_val, neg_para)

    try:
        # Translate English to Hindi
        hi_headline = GoogleTranslator(source='en', target='hi').translate(headline)
        hi_reason = GoogleTranslator(source='en', target='hi').translate(reason)
        hi_action = GoogleTranslator(source='en', target='hi').translate(action)

        # Translate English to Telugu
        te_headline = GoogleTranslator(source='en', target='te').translate(headline)
        te_reason = GoogleTranslator(source='en', target='te').translate(reason)
        te_action = GoogleTranslator(source='en', target='te').translate(action)

        print("\nHINDI REPORT :")
        print(f"शीर्षक: {hi_headline}")
        print(f"कारण: {hi_reason}")
        print(f"सलाह: {hi_action}")

        print("\nTELUGU REPORT :")
        print(f"శీర్షిక: {te_headline}")
        print(f"కారణం: {te_reason}")
        print(f"సలహా: {te_action}")

    #If the Translation failed ,it will print it in English
    except Exception as e:
        print(f"\nERROR : {e}")
        print("\nENGLISH REPORT :")
        print(f"Headline: {headline}")
        print(f"Reason: {reason}")
        print(f"Action: {action}")

def main():
    predict_to_data(2)

if __name__ == "__main__":
    main()