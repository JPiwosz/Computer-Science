countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
"Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast",
"Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea","Eswatini",
"Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia",
"Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia",
"Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome &Principe", "Senegal", "Seychelles",
"Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda",
"Zambia", "Zimbabwe" ]
#countries = ["algeria","angola","benin","botswana","burkina faso","burundi",
#"cabo verde","cameroon","central african republic","chad","comoros","ivory coast","djibouti","democratic republic of congo",
#"egypt","equatorial guinea","eritrea","eswatini","ethiopia","gabon","gambia","ghana","guinea","guinea-bissau","kenya",
#"lesotho","liberia","libya","madagascar","malawi","mali"
lenscorecomp = len(countries)
Start_Stop = input("Do you wish to start the game? Y = yes , N = No    \nNote: Case Sensative    ")
lives = 3
if Start_Stop == "Y":
    print("Game Starting.... \nYou have",lives,"lives")
    print("Countries of Afirca")
    score = 0
    while len(countries) > 0:
        print("Number of countries to guess")
        print(len(countries))
        print("Score =",score)
        country = input("Enter the name of a country   ")
        if country in countries:
            print("Good guess")
            score = score + 1
            print("Your score is now",score)
            countries.remove(country)
            if score == lenscorecomp:
                print("Congrats!! you guessed all 54 countries :) YOU WIN!!")
        else:
            print("Invalid guess")
            lives = lives - 1
            print("You have",lives,"lives left")
            if lives == 0:
                print("Game Over, you got a total of,",score,"points")
                break
if Start_Stop == "N":
    print("You will not play the game :(")
    

    

