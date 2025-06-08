# CRUD operations with Python

In this lab, you will learn how to create a Product's list using a Flask server. Your application should allow you to add a product, retrieve the products, retrieve a specific product with its id, update a specific product with its id, and delete a product with its id. All these operations will be achieved through the REST API endpoints in your Flask server.

You will create an application with API endpoints to perform Create, Retrieve, Update, and Delete operations on the above data using a Flask server.

You will use cURL and POSTMAN to test the implemented endpoints.

## Learning Objectives:
- Create API endpoints to perform Create, Retrieve, Update, and Delete operations on transient data with a Flask server.
- Create REST API endpoints, and use POSTMAN to test your REST APIs.

---

# Creating a Swagger documentation for REST API

In this lab, you will understand how to create a Swagger documentation for your REST APIs.

## Learning Objectives:
- Use the Swagger Editor to create Swagger documentation for REST API
- Use SwaggerUI to access the REST API endpoints of an application
- Generate code with the Swagger documentation

---

# Querying with GraphQL

In this lab, you will become familiar with using GraphQL to query the APIs served through a GraphQL service running on a server using Postman.

## Learning Objectives:
- Use GraphQL with Postman to access GraphQL Service
- Structure queries to access APIs to get selective information that you need

### Examples:
{
    cities {
        city
        state
        }
}
{
    cities(state:"Florida") {
        city
    }
}

### Task:
- Construct a query to return all the cities in the state of “Ohio”, along with the state name.
 {
    cities(state:"Ohio") {
        city
        state
    }
}