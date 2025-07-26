{
    "name": "POS Partner Input as Number",
    "version": "1.0",
    "category": "Point of Sale",
    "summary": "Change customer search input to number type in POS",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_partner_input_number/static/src/xml/partner_input.xml",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
