# University Student Management API

This is a simple FastAPI-based application designed to manage student information for a university. It provides endpoints to retrieve student details, register new students, and update student email addresses.

---

## Assignment Details

This project is part of an assignment given by **Naveed Sarwar**, who is the CEO of **Techloset** and an instructor at **SMIT (Saylani Mass IT Training Program)**. The goal of this assignment is to demonstrate the use of FastAPI for building a RESTful API to manage student data.

---

## Features

- **Retrieve Student Information**: Fetch student details by providing a student ID.
- **Register New Student**: Register a new student with their name, age, email, and courses.
- **Update Student Email**: Update the email address of an existing student.

---

## API Endpoints

### 1. Retrieve Student Information

- **Endpoint**: `GET /students/{student_id}`
- **Description**: Retrieve student details by providing a valid student ID.
- **Parameters**:
  - `student_id` (int): The ID of the student (must be between 1000 and 9999).
  - `include_grade` (bool): Whether to include grade information (not implemented in this version).
  - `semester` (str, optional): The semester for which details are requested.
- **Example Request**:
  ```bash
  GET /students/1234?include_grade=true&semester=Fall2023
  ```
- **Example Response**:
  ```json
  {
    "student_id": 1234
  }
  ```

### 2. Register New Student

- **Endpoint**: `POST /students/register`
- **Description**: Register a new student with their details.
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "age": 21,
    "email": "john.doe@example.com",
    "course": ["Computer Science", "Mathematics"]
  }
  ```
- **Example Response**:
  ```json
  {
    "name": "John Doe",
    "age": 21,
    "email": "john.doe@example.com",
    "course": ["Computer Science", "Mathematics"]
  }
  ```

### 3. Update Student Email

- **Endpoint**: `PUT /students/{student_id}/{email}`
- **Description**: Update the email address of an existing student.
- **Parameters**:
  - `student_id` (int): The ID of the student (must be between 1000 and 9999).
  - `email` (str): The new email address.
- **Example Request**:
  ```bash
  PUT /students/1234/john.new@example.com
  ```
- **Example Response**:
  ```json
  {
    "student_id": 1234,
    "email": "john.new@example.com",
    "message": "Email Updated Successfully"
  }
  ```

---

## Error Handling

The API handles invalid student IDs (outside the range 1000-9999) and other exceptions gracefully, returning appropriate error messages.

---

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: A lightning-fast ASGI server for serving the FastAPI app.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request or contact on shadowhighwayyt@gmail.com.
