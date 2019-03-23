---
title: Web Applications Frameworks
---

### Context
#### 1. What is Web Server Gateway Interface (WSGI)?
WSGI is a **standard interface** between **web servers** and **Python web** application frameworks.

<br>  

#### 2. What does WSGI do?
By **standardizing behavior and communication** between web servers and Python web frameworks, WSGI makes it **possible to write portable Python web code** that can be deployed in any WSGI-compliant web server. WSGI is documented in PEP 3333.

<br>  

#### 3. What is a Framework?
A web framework consists of:
 * a set of libraries
 * a main handler within which you can build custom code to implement a web application (i.e. an interactive web site).  

 <br>  

#### 4. What does a Framework do?
Most web frameworks include å**patterns and utilities** to accomplish at least the following:
 * ##### URL Routing
   * Matches an incoming HTTP request to a particular piece of Python code to be invoked
   * Request and Response Objects
   * Encapsulates the information received from or sent to a user’s browser
 * ##### Template Engine
   * Allows for separating Python code implementing an application’s logic from the HTML (or other) output that it produces
 * ##### Development Web Server
   * Runs an HTTP server on development machines to enable rapid development; often automatically reloads server-side code when files are updated

 <br>  

#### 5. How to choose a Framework?
#### Popular
 * ##### Django  
    * A **batteries included** web application framework
    * An excellent choice for creating **content-oriented websites**.
    * By providing **many utilities and patterns** out of the box, Django aims to make it possible to build **complex, database-backed** web applications quickly, while encouraging best practices in code written using it.
    * Django has a large and active community, and many pre-built re-usable modules that can be incorporated into a new project as-is, or customized to fit your needs.
    * The majority of new Python web applications today are built with Django.

 * ##### Flask
    * A “microframework” for Python
    * An excellent choice for building **smaller** applications, APIs, and web services.
    * Building an app with Flask is a lot **like writing standard Python modules**, except some functions have routes attached to them. It’s really beautiful.
    * Flask implements the **most commonly-used core components** of a web application framework, like URL routing, request and response objects, and templates.
    * Developers are able to choose other extensions components (e.g. database access or form generation and validation)
    * Flask is default choice for any Python web application that isn’t a good fit for Django

#### Sounds cool
* ##### FastAPI
    * A modern web framework for building APIs with **Python 3.6+**.
    * It has very **high performance** as it is based on Starlette and Pydantic.

    * FastAPI takes advantage of **standard Python type declarations** in **function parameters** to **declare request parameters and bodies**
    * perform **data conversion** (serialization, parsing), **data validation**, and **automatic API documentation** with OpenAPI 3 (including JSON Schema).
    * It includes **tools and utilities** for **security and authentication** (including OAuth2 with JWT tokens), a dependency injection system, automatic generation of interactive API documentation, and other features.

* ##### Falcon
    * It is a **reliable, high-performance** Python web framework for building **large-scale app backends and microservices**.
    * Encourages the **REST architectural style** of mapping URIs to resources, trying to **do as little** as possible while remaining **highly effective**.
    * When your goal is to build **RESTful API microservices** that are fast and scalable.
    * Falcon highlights four main focuses: speed, reliability, flexibility, and debuggability.
    * It implements HTTP through “responders” such as on_get(), on_put(), etc. These responders receive intuitive request and response objects. (Who doesn't?)

* ##### Masonite
   * Masonite is a modern and **developer centric**, **“batteries included”**, web framework.
   * The Masonite framework follows the MVC (Model-View-Controller) architecture pattern
   * Heavily inspired by frameworks such as Rails and Laravel, so if you are coming to Python from a **Ruby or PHP background** then you will feel right at home!
   * Masonite comes with a lot of **functionality out of the box** including a powerful **IOC container** with auto **resolving dependency injection**, **craft** command line tools, and the Orator active record style ORM.
  * Masonite is perfect for **beginners or experienced developers** alike and works hard to be fast and easy from install through to deployment. Try it once and you’ll fall in love.

#### Less Popular
* ##### Tornado
    * Tornado is an **asynchronous** web framework for Python that has its own event loop.
    * This allows it to natively **support WebSockets**, for example. Well-written Tornado applications are known to have excellent performance characteristics.

    I **do not recommend** using Tornado unless you think you need it.

* ##### Pyramid

    * Pyramid is a very **flexible** framework with a heavy focus on **modularity**.
    * It comes with **a small number of libraries** (“batteries”) built-in, and encourages users to **extend its base functionality**.
    * A set of provided cookiecutter templates helps making new project decisions for users.
    * It powers one of the most important parts of **python infrastructure PyPI**.
    * Pyramid does not have a large user base, unlike Django and Flask. It’s a **capable** framework, but **not a very popular** choice for new Python web applications today.


<br>
---
#### Reference
Text adapted from [The Hitchhiker's Guide to Python: Web Applications & Frameworks](https://docs.python-guide.org/scenarios/web/)
