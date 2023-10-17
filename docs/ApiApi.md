# swagger_client.ApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](ApiApi.md#create_address) | **POST** /api/addresses/ | 
[**create_customer**](ApiApi.md#create_customer) | **POST** /api/customers/ | 
[**create_order**](ApiApi.md#create_order) | **POST** /api/orders/ | 
[**create_product**](ApiApi.md#create_product) | **POST** /api/products/ | 
[**create_review**](ApiApi.md#create_review) | **POST** /api/reviews/ | 
[**destroy_address**](ApiApi.md#destroy_address) | **DELETE** /api/addresses/{id}/ | 
[**destroy_customer**](ApiApi.md#destroy_customer) | **DELETE** /api/customers/{id}/ | 
[**destroy_order**](ApiApi.md#destroy_order) | **DELETE** /api/orders/{id}/ | 
[**destroy_product**](ApiApi.md#destroy_product) | **DELETE** /api/products/{id}/ | 
[**destroy_review**](ApiApi.md#destroy_review) | **DELETE** /api/reviews/{id}/ | 
[**list_address**](ApiApi.md#list_address) | **GET** /api/addresses/ | 
[**list_customers**](ApiApi.md#list_customers) | **GET** /api/customers/ | 
[**list_orders**](ApiApi.md#list_orders) | **GET** /api/orders/ | 
[**list_products**](ApiApi.md#list_products) | **GET** /api/products/ | 
[**list_reviews**](ApiApi.md#list_reviews) | **GET** /api/reviews/ | 
[**partial_update_address**](ApiApi.md#partial_update_address) | **PATCH** /api/addresses/{id}/ | 
[**partial_update_customer**](ApiApi.md#partial_update_customer) | **PATCH** /api/customers/{id}/ | 
[**partial_update_order**](ApiApi.md#partial_update_order) | **PATCH** /api/orders/{id}/ | 
[**partial_update_product**](ApiApi.md#partial_update_product) | **PATCH** /api/products/{id}/ | 
[**partial_update_review**](ApiApi.md#partial_update_review) | **PATCH** /api/reviews/{id}/ | 
[**retrieve_address**](ApiApi.md#retrieve_address) | **GET** /api/addresses/{id}/ | 
[**retrieve_customer**](ApiApi.md#retrieve_customer) | **GET** /api/customers/{id}/ | 
[**retrieve_order**](ApiApi.md#retrieve_order) | **GET** /api/orders/{id}/ | 
[**retrieve_product**](ApiApi.md#retrieve_product) | **GET** /api/products/{id}/ | 
[**retrieve_review**](ApiApi.md#retrieve_review) | **GET** /api/reviews/{id}/ | 
[**update_address**](ApiApi.md#update_address) | **PUT** /api/addresses/{id}/ | 
[**update_customer**](ApiApi.md#update_customer) | **PUT** /api/customers/{id}/ | 
[**update_order**](ApiApi.md#update_order) | **PUT** /api/orders/{id}/ | 
[**update_product**](ApiApi.md#update_product) | **PUT** /api/products/{id}/ | 
[**update_review**](ApiApi.md#update_review) | **PUT** /api/reviews/{id}/ | 

# **create_address**
> Address create_address(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Address() # Address |  (optional)

try:
    api_response = api_instance.create_address(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)|  | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer**
> Customer create_customer(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Customer() # Customer |  (optional)

try:
    api_response = api_instance.create_customer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> Order create_order(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Order() # Order |  (optional)

try:
    api_response = api_instance.create_order(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)|  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_product**
> Product create_product(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Product() # Product |  (optional)

try:
    api_response = api_instance.create_product(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_review**
> Review create_review(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Review() # Review |  (optional)

try:
    api_response = api_instance.create_review(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Review**](Review.md)|  | [optional] 

### Return type

[**Review**](Review.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_address**
> destroy_address(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this address.

try:
    api_instance.destroy_address(id)
except ApiException as e:
    print("Exception when calling ApiApi->destroy_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this address. | 

### Return type

void (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_customer**
> destroy_customer(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this customer.

try:
    api_instance.destroy_customer(id)
except ApiException as e:
    print("Exception when calling ApiApi->destroy_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this customer. | 

### Return type

void (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_order**
> destroy_order(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this order.

try:
    api_instance.destroy_order(id)
except ApiException as e:
    print("Exception when calling ApiApi->destroy_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this order. | 

### Return type

void (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_product**
> destroy_product(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this product.

try:
    api_instance.destroy_product(id)
except ApiException as e:
    print("Exception when calling ApiApi->destroy_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this product. | 

### Return type

void (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_review**
> destroy_review(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this review.

try:
    api_instance.destroy_review(id)
except ApiException as e:
    print("Exception when calling ApiApi->destroy_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this review. | 

### Return type

void (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address**
> list[Address] list_address()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_address()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list_address: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Address]**](Address.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> list[Customer] list_customers()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_customers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list_customers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[Order] list_orders()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_orders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list_orders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Order]**](Order.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> list[Product] list_products()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_products()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list_products: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Product]**](Product.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reviews**
> list[Review] list_reviews()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_reviews()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list_reviews: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Review]**](Review.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_address**
> Address partial_update_address(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this address.
body = swagger_client.Address() # Address |  (optional)

try:
    api_response = api_instance.partial_update_address(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->partial_update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this address. | 
 **body** | [**Address**](Address.md)|  | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_customer**
> Customer partial_update_customer(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this customer.
body = swagger_client.Customer() # Customer |  (optional)

try:
    api_response = api_instance.partial_update_customer(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->partial_update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this customer. | 
 **body** | [**Customer**](Customer.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_order**
> Order partial_update_order(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this order.
body = swagger_client.Order() # Order |  (optional)

try:
    api_response = api_instance.partial_update_order(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->partial_update_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this order. | 
 **body** | [**Order**](Order.md)|  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_product**
> Product partial_update_product(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this product.
body = swagger_client.Product() # Product |  (optional)

try:
    api_response = api_instance.partial_update_product(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->partial_update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this product. | 
 **body** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_review**
> Review partial_update_review(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this review.
body = swagger_client.Review() # Review |  (optional)

try:
    api_response = api_instance.partial_update_review(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->partial_update_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this review. | 
 **body** | [**Review**](Review.md)|  | [optional] 

### Return type

[**Review**](Review.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_address**
> Address retrieve_address(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this address.

try:
    api_response = api_instance.retrieve_address(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->retrieve_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this address. | 

### Return type

[**Address**](Address.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_customer**
> Customer retrieve_customer(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this customer.

try:
    api_response = api_instance.retrieve_customer(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->retrieve_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this customer. | 

### Return type

[**Customer**](Customer.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_order**
> Order retrieve_order(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this order.

try:
    api_response = api_instance.retrieve_order(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->retrieve_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this order. | 

### Return type

[**Order**](Order.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_product**
> Product retrieve_product(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this product.

try:
    api_response = api_instance.retrieve_product(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->retrieve_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this product. | 

### Return type

[**Product**](Product.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_review**
> Review retrieve_review(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this review.

try:
    api_response = api_instance.retrieve_review(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->retrieve_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this review. | 

### Return type

[**Review**](Review.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> Address update_address(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this address.
body = swagger_client.Address() # Address |  (optional)

try:
    api_response = api_instance.update_address(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this address. | 
 **body** | [**Address**](Address.md)|  | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> Customer update_customer(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this customer.
body = swagger_client.Customer() # Customer |  (optional)

try:
    api_response = api_instance.update_customer(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this customer. | 
 **body** | [**Customer**](Customer.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> Order update_order(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this order.
body = swagger_client.Order() # Order |  (optional)

try:
    api_response = api_instance.update_order(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->update_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this order. | 
 **body** | [**Order**](Order.md)|  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> Product update_product(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this product.
body = swagger_client.Product() # Product |  (optional)

try:
    api_response = api_instance.update_product(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this product. | 
 **body** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_review**
> Review update_review(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenAuthentication
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique integer value identifying this review.
body = swagger_client.Review() # Review |  (optional)

try:
    api_response = api_instance.update_review(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->update_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this review. | 
 **body** | [**Review**](Review.md)|  | [optional] 

### Return type

[**Review**](Review.md)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

