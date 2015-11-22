# -*- coding: utf-8 -*-
db.define_table('categories',
                Field('category_name'),
                Field('parent_category_id',label=T('Parent Category')),
                Field('taxonomy'),
                format = '%(taxonomy)s')
db.categories.parent_category_id.requires=IS_EMPTY_OR(IS_IN_DB(db, 'categories.taxonomy'))

db.define_table('bid_items',
                Field('item_name'),
                Field('category_id',label=T('Category'),type='reference categories'),
                Field('image',type='upload'),
                Field('min_bid_quote',type='integer'),
                Field('time_of_expiry',type='datetime'),
                Field('bid_type',requires=IS_IN_SET(('Sell','Rent','Both'))),
                Field('item_details'),
                Field('owner_id'),
                format = '%(item_name)s')

db.define_table('bids',
                Field('bid_quote'),
                Field('item_id'),
                Field('user_id'))
