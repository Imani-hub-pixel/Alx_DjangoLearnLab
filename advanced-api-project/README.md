Advanced API Project - Book Views Documentation
BookListView:
GET /books/
    Description:
        Retrieves a list of all Book instances in the database.
        Supports search by 'title' or 'author__name'.
    Permissions:
        AllowAny - accessible to unauthenticated users.
    Custom Settings:
        - search_fields: Enables filtering books by title and author name using query parameters.
    Example:
        GET /books/?search=Things
BookDetailView:
GET /books/<id>/
    Description:
        Retrieves a single Book instance by its primary key (id).
    Permissions:
        AllowAny - accessible to unauthenticated users.
BookCreateView:
POST /books/create/
    Description:
        Allows authenticated users to create a new Book instance.
    Permissions:
        IsAuthenticated - only logged-in users can create books.
    Custom Hooks:
        - perform_create: Automatically sets the 'author' field to the logged-in user.
    Example Payload:
        {
            "title": "New Book",
            "publication_year": 2023
        }
BookUpdateView:
PUT/PATCH /books/<id>/update/
    Description:
        Allows authenticated users to update an existing Book instance.
    Permissions:
        IsAuthenticated - only logged-in users can update books.
    Custom Hooks:
        - perform_update: Can be overridden if you want to add custom logic on update.
BookDeleteView:
DELETE /books/<id>/delete/
    Description:
        Allows authenticated users to delete an existing Book instance.
    Permissions:
        IsAuthenticated - only logged-in users can delete books.