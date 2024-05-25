import jsonschema.exceptions
import requests
import config.routes as Urls
import jsonschema

class Controller:  
    def get_all(self):
        data = requests.get(Urls.BASE_URL + Urls.PRODUCTS_ENDPOINT)
        return data.json()

    def get(self, id):
        response = requests.get(Urls.BASE_URL + Urls.PRODUCTS_ENDPOINT)
        data = response.json()
        for product in data:
            if int(product['id']) == id:
                return product

        return None

    def create(self, product):
        data = requests.post(Urls.BASE_URL + Urls.ADD_PRODUCT_ENDPOINT, json=product)
        try:
            return data.json()
        except:
            return None
        
    def delete(self, id):
        data = requests.get(Urls.BASE_URL + Urls.DELETE_PRODUCT_ENDPOINT, params={'id': id})
        return data.json()   
     
    def edit(self, product):
        data = requests.post(Urls.BASE_URL + Urls.EDIT_PRODUCT_ENDPOINT, json=product)
        try:
            return data.json()
        except:
            return None

# def main():
#     controller = Controller()
#     all = controller.get_all()
#     print(all)

# if __name__ == '__main__':
#     main()