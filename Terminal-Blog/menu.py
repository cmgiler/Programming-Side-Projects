from models.blog import Blog
from database import Database

__author__ = 'cmgiler'

class Menu(object):
    def __init__(self):
        # Ask user for author name
        self.user = raw_input('Enter your author name: ')

        # Check if they've already got an account
        if self._user_has_account():        # Private method
            print('Welcome back {}'.format(self.user))
        else:
            # If not, prompt them to create one
            self._prompt_user_for_account() # Private method

    def _user_has_account(self):
        blog =  Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        # Start a blog
        title = raw_input('Enter blog title: ')
        description = raw_input('Enter blog description: ')
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # User read or write blogs?
        read_or_write = raw_input('Do you want to read (R) or write (W) blogs? ')

        # if read:
        if read_or_write.lower() == 'r':
            # list blogs in database
            self._list_blogs()
            # allow user to pick one
            self._view_blog()
            # display posts
            pass
        # if write:
        elif read_or_write.lower() == 'w':
            # check if user has a blog
            # if they do, prompt to write a post
            # if not, prompt to create a new blog
            self.user_blog.new_post()

        else:
            print 'Thank you for blogging!'

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print('ID: {}, Title: {}, Author: {}'.format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = raw_input('Enter the ID of the blog you''d like to read: ')
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print('Date: {}, title: {}\n\n{}'.format(post['created_date'], post['title'], post['content']))
