# pip install instaloader
import instaloader
loader = instaloader.Instaloader()
post = instaloader.Post.from_shortcode(loader.context, "SHORTCODE_HERE")
loader.download_post(post, target="downloaded_post")
print("Instagram post downloaded successfully")
