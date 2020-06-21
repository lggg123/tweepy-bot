import tweepy
import time 

auth = tweepy.OAuthHandler("6G36Uzr38DxkPAHlarzZsD6gl",
                           "tkxcbKIJ1sF9vPZIpMUWEONWy8X6VI4BvaYMmif4BOI12orhxo")

auth.set_access_token(
    "481841999-pDdraMm5xu77AfSM2Kzo8zinltMCzghvhVluBP2U", "IPu9u420lrizB6P6gjjsDgWA8GfHT6N01J7pAqZ5cszBn")

api = tweepy.API(auth)

api.update_status(
    "Feeling very cody today #coder #ai #python #coding #twitter #hellohello #doingitbigonptyhon")
