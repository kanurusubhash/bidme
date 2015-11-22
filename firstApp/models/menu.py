# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

# response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
#                   _class="navbar-brand",_href="http://www.web2py.com/",
#                   _id="web2py-logo")
response.logo = A(IMG(_src=URL('static', 'images/iiith_logo3.png'),
                     _href="http://www.web2py.com/")) 
# response.title = request.application.replace('_',' ').title()
response.title = 'IIIT-H Online Bidding Portal'
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Subhash Kanuru <subhash.kanuru@students.iiit.ac.in>'
response.meta.description = 'a cool new app for iiitH online bidding'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
categories=db().select(db.categories.id,db.categories.taxonomy,orderby=db.categories.taxonomy);
categoriesMenu=[]
if request.function=="show_rent_items":
    function="show_rent_items";
else:
    function="show_items";
for category in categories:
    categoriesMenu.append((category.taxonomy, False, URL('default', function,args=[category.id]), []));

response.menu = [
    (T('Categories'), False, '#', categoriesMenu),
]

response.menu += [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Rent Items'), False,URL(c='default', f='show_rent_items'))
]

DEVELOPMENT_MENU = False

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
          (T('This App'), False, '#', [
              (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
              LI(_class="divider"),
              (T('Controller'), False,
               URL(
               'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
              (T('View'), False,
               URL(
               'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
              (T('DB Model'), False,
               URL(
               'admin', 'default', 'edit/%s/models/db.py' % app)),
              (T('Menu Model'), False,
               URL(
               'admin', 'default', 'edit/%s/models/menu.py' % app)),
              (T('Config.ini'), False,
               URL(
               'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
              (T('Layout'), False,
               URL(
               'admin', 'default', 'edit/%s/views/layout.html' % app)),
              (T('Stylesheet'), False,
               URL(
               'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
              (T('Database'), False, URL(app, 'appadmin', 'index')),
              (T('Errors'), False, URL(
               'admin', 'default', 'errors/' + app)),
              (T('About'), False, URL(
               'admin', 'default', 'about/' + app)),
              ]),
          ('web2py.com', False, '#', [
             (T('Download'), False,
              'http://www.web2py.com/examples/default/download'),
             (T('Support'), False,
              'http://www.web2py.com/examples/default/support'),
             (T('Demo'), False, 'http://web2py.com/demo_admin'),
             (T('Quick Examples'), False,
              'http://web2py.com/examples/default/examples'),
             (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
             (T('Videos'), False,
              'http://www.web2py.com/examples/default/videos/'),
             (T('Free Applications'),
              False, 'http://web2py.com/appliances'),
             (T('Plugins'), False, 'http://web2py.com/plugins'),
             (T('Recipes'), False, 'http://web2pyslices.com/'),
             ]),
          (T('Documentation'), False, '#', [
             (T('Online book'), False, 'http://www.web2py.com/book'),
             LI(_class="divider"),
             (T('Preface'), False,
              'http://www.web2py.com/book/default/chapter/00'),
             (T('Introduction'), False,
              'http://www.web2py.com/book/default/chapter/01'),
             (T('Python'), False,
              'http://www.web2py.com/book/default/chapter/02'),
             (T('Overview'), False,
              'http://www.web2py.com/book/default/chapter/03'),
             (T('The Core'), False,
              'http://www.web2py.com/book/default/chapter/04'),
             (T('The Views'), False,
              'http://www.web2py.com/book/default/chapter/05'),
             (T('Database'), False,
              'http://www.web2py.com/book/default/chapter/06'),
             (T('Forms and Validators'), False,
              'http://www.web2py.com/book/default/chapter/07'),
             (T('Email and SMS'), False,
              'http://www.web2py.com/book/default/chapter/08'),
             (T('Access Control'), False,
              'http://www.web2py.com/book/default/chapter/09'),
             (T('Services'), False,
              'http://www.web2py.com/book/default/chapter/10'),
             (T('Ajax Recipes'), False,
              'http://www.web2py.com/book/default/chapter/11'),
             (T('Components and Plugins'), False,
              'http://www.web2py.com/book/default/chapter/12'),
             (T('Deployment Recipes'), False,
              'http://www.web2py.com/book/default/chapter/13'),
             (T('Other Recipes'), False,
              'http://www.web2py.com/book/default/chapter/14'),
             (T('Helping web2py'), False,
              'http://www.web2py.com/book/default/chapter/15'),
             (T("Buy web2py's book"), False,
              'http://stores.lulu.com/web2py'),
             ]),
          (T('Community'), False, None, [
             (T('Groups'), False,
              'http://www.web2py.com/examples/default/usergroups'),
              (T('Twitter'), False, 'http://twitter.com/web2py'),
              (T('Live Chat'), False,
               'http://webchat.freenode.net/?channels=web2py'),
              ]),
        ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
    

USER_MENU = False
if auth.user!=None:
    if auth.has_membership(4,auth.user.id):
        USER_MENU = True;

if USER_MENU:
    response.menu += [
        (T('Add Item'), False,URL(c='default', f='add_item')),
        (T('My Bids'), False,URL(c='default', f='show_my_bids')),
        (T('My Items'), False,URL(c='default', f='show_my_items'))
        ]

ADMIN_MENU = False;
if auth.user!=None:
    if auth.has_membership(2,auth.user.id):
        ADMIN_MENU = True

if ADMIN_MENU:
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (T('Manage Categories'), False, '#', [
                (T('View Categories'), False,URL(c='default', f='list_categories')),
                (T('Add Category'), False,URL(c='default', f='add_category')),
                (T('Update Category'), False,URL(c='default', f='update_category')),
                (T('Remove Category'), False,URL(c='default', f='remove_category'))]),
        (T('Administer Items'), False, URL(c='default', f='list_items'))]
