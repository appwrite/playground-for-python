# Appwrite's Python Playground 🎮

Appwrite playground is a simple way to explore the Appwrite API & Appwrite Python SDK. Use the source code of this repository to learn how to use the different Appwrite Python SDK features.

**Work in progress**

## System Requirements
* A system with Python 3+ or Docker installed.
* An Appwrite instance.
* An Appwrite project created in the console.
* An Appwrite API key created in the console.

### Installation
1. Clone this repository.
2. `cd` into the repository.
3. Open the playground.py file found in the root of the cloned repository.
4. Copy Project ID, endpoint and API key from Appwrite console into `playground.py`
5. Run the playground:
    Python:
        - Install dependencies using pip `pip install -r requirements.txt`
        - Execute the command `python playground.py`
    Docker:
        - Execute the command `docker compose up`
6. You will see the JSON response in the console.

### API's Covered

- Database
    * Create Collection
    * List Collections
    * Add Document
    * List Documents
    * Delete Document
    * Delete Collection

- Storage
    * Create Bucket
    * List Buckets
    * Upload File
    * List Files
    * Delete File
    * Delete Bucket

- Users
    * Create User
    * List Users
    * Delete User

- Functions
    * Create Function
    * List Functions
    * Delete Function

### YouTube Video

[Interact with appwrite using python : YouTube](https://youtu.be/TbIJUwTTTyc)

### Jupyter Notebook

[Jupyter Notebook](./appwrite_test.ipynb)

## Contributing

All code contributions - including those of people having commit access - must go through a pull request and approved by a core developer before being merged. This is to ensure proper review of all the code.

We truly ❤️ pull requests! If you wish to help, you can learn more about how you can contribute to this project in the [contribution guide](https://github.com/appwrite/appwrite/blob/master/CONTRIBUTING.md).

## Security

For security issues, kindly email us [security@appwrite.io](mailto:security@appwrite.io) instead of posting a public issue in GitHub.

## Follow Us

Join our growing community around the world! Follow us on [Twitter](https://twitter.com/appwrite), [Facebook Page](https://www.facebook.com/appwrite.io), [Facebook Group](https://www.facebook.com/groups/appwrite.developers/) or join our [Discord Server](https://appwrite.io/discord) for more help, ideas and discussions.
