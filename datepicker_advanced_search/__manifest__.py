# -*- coding: utf-8 -*-
{
    'name': 'Datepicker And Expand Search Option',
    'version': '1.1',
    'description': """
                    Datepicker For Date or Datetime Data Type With Expanded Search View
                    """,
    'summary': """Datepicker For Date or Datetime Type And Always Expand Search View""",
    'category': 'Web',
    'license': 'LGPL-3',
    'author': "Knacktechs Solutions",
    'website': "http://knacktechs.com/",
    'depends': ['web'],
    'data': [
        'views/template.xml',

    ],
    'images': [
        'static/description/date_lable.png'
    ],
      'qweb': ['static/src/xml/date_picker.xml'],
    'installable': True,
    'application': True,
}
