#pip : python index package
# instaloader to get instagram profile pic by entering only instagram id
import instaloader

name = input("Enter instagaram username: ")
insta = instaloader.Instaloader()

insta.download_profile(name,profile_pic_only=True)