from fastapi import APIRouter, FastAPI, Depends, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera', 'phone']

@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products

@router.get('/all')
def get_all_products():
    # return products
    data = " ".join(products) 
    response = PlainTextResponse(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value='test_cookie_value')
    return response

@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: Optional[str] = Header(None),
    test_cookie: Optional[str] = Cookie(None)
    ):
    if custom_header:
        response.headers['custom_response_header'] = ", ".join(custom_header)  
    return {
        'data' : products,
        'custom_header' : custom_header,
        'my_cookie' : test_cookie
        }


@router.get('/{id}', responses={
    200: {
        "content": {
            "text/html": {
                "example" : "<div>Product</div>"
            }
        },
        "description" : "returns the html for an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example" : "product not available"
            }
        },
        "description" : "error message"
    }
})
def get_product(id: int):
    if id > len(products):
        out = "product not available"
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    product = products[id]
    out = f"""
    <head>
        <style>
        .product {{
            width: 500px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
        }}
        </style>
    </head>
    <div class="product">{product}</div>
    """
    return HTMLResponse(content=out, media_type="text/html")
