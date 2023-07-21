class Order():
    '''
    new Order class
    '''
    def __init__(self,
                id,
                metal_id,
                size_id,
                style_id,
                metal,
                price,
                carets,
                size_price,
                style_name,
                style_price
                ):
        self.id = id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.metal = metal
        self.price = price
        self.carets = carets
        self.size_price = size_price
        self.style_name = style_name
        self.style_price = style_price
