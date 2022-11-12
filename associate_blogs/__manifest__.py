# -*- coding: utf-8 -*-
{
    'name': "associate_blogs",
    'summary': """Associate blogs and posts to company""",
    'description': """
        To be able to associate a blog to a single company and that the news 
        associated with that blog inherits the company of the blog to which 
        they belong
    """,
    'author': "jsan-95",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'website_blog'
    ],
    'data': [
        'security/associate_blogs_security.xml',
        'views/website_blog_views.xml',
    ],
}
