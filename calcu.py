def degree_to_zodiac(degree):
    # Convert degree to 30° scale
    
    degree = float(degree)
    if degree<0:
        degree = 360+degree
    degree_30 = degree % 30
    
    # Define zodiac signs and their degrees in 360° scale
    zodiacs = [
        ('Aries', (0, 30)),
        ('Taurus', (30, 60)),
        ('Gemini', (60, 90)),
        ('Cancer', (90, 120)),
        ('Leo', (120, 150)),
        ('Virgo', (150, 180)),
        ('Libra', (180, 210)),
        ('Scorpio', (210, 240)),
        ('Sagittarius', (240, 270)),
        ('Capricorn', (270, 300)),
        ('Aquarius', (300, 330)),
        ('Pisces', (330, 360))
    ]
    
    # Iterate through the zodiac signs and return the corresponding sign
    for zodiac in zodiacs:
        if zodiac[1][0] <= degree < zodiac[1][1]:
            return zodiac[0], degree_30
    
    # If degree is outside the 0-360 range, raise an error
    raise ValueError("Degree must be between 0 and 360")

def get_nakshatra(degrees):
    # Define the nakshatras and their starting degrees
    nakshatras = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha', 'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati']
    nakshatra_start_degrees = [0, 13.33333, 26.66667, 40, 53.33333, 66.66667, 80, 93.33333, 106.66667, 120, 133.33333, 146.66667, 160, 173.33333, 186.66667, 200, 213.33333, 226.66667, 240, 253.33333, 266.66667, 280, 293.33333, 306.66667, 320, 333.33333]

    # Calculate the nakshatra index based on the input degrees
    nakshatra_index = int(degrees // 13.3333333)

    # Get the nakshatra name based on the index
    nakshatra_name = nakshatras[nakshatra_index]

    pada_no = (degrees - nakshatra_index*13.333)//3.333 +1

    return nakshatra_name, pada_no



def trotosid(degree, year):
    miles = 24.18 #offset between tropical and sidereal in 2023 march
    celestial_offset = 0.01395714285714285714285714285714  #per year
    if year == 2023:
        return degree - miles
    elif year>2023:
         return degree-((year-2023)*celestial_offset + miles)  
    elif year<2023:
        return degree- (miles -(2023-year)*celestial_offset)
    

