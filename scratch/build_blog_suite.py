import os

blog_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours\blog"

# Common Header template for pages in blog/ directory
def get_header(title, active_page="blog"):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    '''

# Script to build full blog suite
print("Building blog pages generator...")
