# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
from datetime import datetime
from datetime import timedelta
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
#     response.flash = T("Hello Subhash")
#     return dict(message=T('Welcome to web2py!'))
#     return {'message':'Welcome'}
#     return {'message1':'Welcome','test':'testing'}
#     return dict(message='My First App');
#     return auth.wiki()
#     session.a=session.get('a',0)+1;
#     form=SQLFORM.factory(Field('category',label=T("Category")),Field('parent_category'));
#     form=SQLFORM(db.categories);
#     rows= db().select(db.categories.ALL)
#     rows1= db().select(db.bid_items.ALL)
#     grid1=SQLFORM.grid(db.categories,orderby=db.categories.taxonomy)
#     grid2=SQLFORM.grid(db.bid_items)
#     if form.process().accepted:
#         response.flash = 'your category is posted'
#     return dict(message1='Welcome Subhash', noOfViews=session.a)
#     return dict(message='Welcome Subhash');
    redirect(URL('show_items'))
    return locals();

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
#     vars=form.vars;
    #mail.send(to="",subject="Welcome to bidme App",message="We hope you enjoy the experience.");
    return dict(form=auth())
#     return locals;


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_membership('admin')
def add_category():
    form=SQLFORM(db.categories,fields=['category_name','parent_category_id']);
    form.add_button('Back', URL('index'))
    if form.validate():
        if form.vars.parent_category_id==None:
            form.vars.taxonomy=form.vars.category_name
        else:
            row = db.categories(db.categories.taxonomy==form.vars.parent_category_id);
            form.vars.taxonomy= row.taxonomy+' > '+form.vars.category_name;
        form.vars.id = db.categories.insert(**dict(form.vars))
        redirect(URL('index'))
        response.flash = 'Category is added successfully'
#         response.flash = form.vars.parent_category_id
    elif form.errors:
        response.flash = 'Errors occured while adding category'
    return locals();

@auth.requires_membership('admin')
def remove_category():
    form=SQLFORM(db.categories,fields=['taxonomy']);
    form.add_button('Back', URL('index'))
    if form.validate():
        row = db.categories(db.categories.taxonomy==form.vars.taxonomy);
#         there should be no subcategories and there should be no items associated in this category
        db(db.categories,row).delete()
        redirect(URL('index'))
        response.flash = 'Category is removed successfully'
    elif form.errors:
        response.flash = 'Errors occured while removing category'
    return locals();

@auth.requires_membership('admin')
def list_categories():
#     db.categories.taxonomy.writable=False
    grid=SQLFORM.grid(db.categories,orderby=db.categories.taxonomy,paginate=10)
    return locals();
    
@auth.requires_login()
def add_item():
    form=SQLFORM(db.bid_items,fields=['item_name','category_id','image','min_bid_quote','time_of_expiry','bid_type','item_details']);
    form.add_button('Back', URL('index'))
    if form.validate():
        form.vars.owner_id=auth.user_id
        form.vars.id = db.bid_items.insert(**dict(form.vars))
        redirect(URL('index'))
        response.flash = 'Item is added successfully'
    elif form.errors:
        response.flash = 'Errors occured while adding item'
    return locals();


@auth.requires_membership('admin')
def list_items():
    db.categories.taxonomy.writable=False
    grid=SQLFORM.grid(db.bid_items,orderby=db.bid_items.item_name,paginate=10)
    return locals();


def show_items():
    if len(request.args)==1:
        items=db((db.bid_items.category_id==request.args[0]) & (db.bid_items.time_of_expiry>datetime.now()) & ((db.bid_items.bid_type=='Sell') | (db.bid_items.bid_type=='Both'))).select()
    else:
        items= db((db.bid_items.time_of_expiry>datetime.now()) & ((db.bid_items.bid_type=='Sell') | (db.bid_items.bid_type=='Both'))).select()
    return locals();


def show_rent_items():
    if len(request.args)==1:
        items=db((db.bid_items.category_id==request.args[0]) & (db.bid_items.time_of_expiry>datetime.now()) & ((db.bid_items.bid_type=='Rent') | (db.bid_items.bid_type=='Both'))).select()
    else:
        items= db((db.bid_items.time_of_expiry>datetime.now()) & ((db.bid_items.bid_type=='Rent') | (db.bid_items.bid_type=='Both'))).select()
    return locals();

@auth.requires_login()
def bid_for_item():
    args=request.args;
    form=SQLFORM(db.bids,fields=['bid_quote']);
    form.add_button('Back', URL('index'))
    if form.validate():
        form.vars.item_id=args[0];
        form.vars.user_id=auth.user_id;
        form.vars.id = db.bids.insert(**dict(form.vars));
    elif form.errors:
        response.flash = 'Errors occured while adding bid'
#     grid=SQLFORM.grid(db.bids,fields=[db.bids.bid_quote, db.bids.user_id],orderby=~db.bids.bid_quote,paginate=10,searchable=False,deletable=False,editable=False,details=False,create=False,links_in_grid=False);
    rows=db(db.bids.item_id==args[0]).select(db.bids.bid_quote,db.bids.user_id,orderby=~db.bids.bid_quote);
    return locals();

def getQuote():
    args=request.args;
    maxQuoteRecords= db((db.bids.item_id==args[0])).select(db.bids.bid_quote.max());
    maximumQuote=maxQuoteRecords[0]['MAX(bids.bid_quote)'];
    if maximumQuote==None:
        itemRecords= db((db.bid_items.id==args[0])).select(db.bid_items.min_bid_quote);
        maximumQuote=itemRecords[0].min_bid_quote;
    return {'quote':maximumQuote};

def getDetailsViaAjax():
    args=request.args;
    maxQuoteRecords= db((db.bids.item_id==args[0])).select(db.bids.bid_quote.max());
    maximumQuote=maxQuoteRecords[0]['MAX(bids.bid_quote)'];
    if maximumQuote==None:
        itemRecords= db((db.bid_items.id==args[0])).select(db.bid_items.min_bid_quote);
        maximumQuote=itemRecords[0].min_bid_quote;

    itemRecords= db((db.bid_items.id==args[0])).select();
    item=itemRecords[0];
    delta=item.time_of_expiry-datetime.now()
    delta=delta - timedelta(microseconds=delta.microseconds)
    isShowBid=0;
    if delta>timedelta(0):
        isShowBid=1;
    return {'quote':maximumQuote,'delta':delta,'isShowBid':isShowBid,'item_id':item.id};

@auth.requires_login()
def show_my_bids():
    items=db((db.bids.user_id==auth.user.id) & (db.bids.item_id==db.bid_items.id)).select(db.bid_items.id,db.bid_items.item_name,db.bid_items.image,distinct=True);
    return locals();

@auth.requires_login()
def show_my_items():
#     items=db((db.bid_items.owner_id==auth.user.id)).select(db.bid_items.id,db.bid_items.item_name,db.bid_items.image);
    grid=SQLFORM.grid(db.bid_items,orderby=db.bid_items.item_name,paginate=10)
    return locals();
