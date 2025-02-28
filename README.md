# AuthSync ChatDrive API 🚀

AuthSync ChatDrive is a web application that provides **authentication, file upload to Drive, and chat functionality**. This README contains setup instructions, API details, and Postman collection export.

## 🔗 Live URL  
**Base URL:** [AuthSync ChatDrive](https://authsync-chatdrive.onrender.com/)

---

## 📌 API Endpoints  

### 1️⃣ Authentication API  
**Endpoint:**  

Response Example:

json
Copy code
{
    "message": "Redirect to Google OAuth for authentication"
}
2️⃣ Drive Upload API
Endpoint:

http
Copy code
POST /drive/upload
Headers:

http
Copy code
Authorization: Bearer <YOUR_ACCESS_TOKEN>
Body (form-data):

file: (Upload a file)
📢 Response Example:

json
Copy code
{
    "message": "File uploaded successfully",
    "file_id": "123456abcdef"
}
3️⃣ Drive Connect API
Endpoint:

http
Copy code
POST /drive/connect
Headers:

http
Copy code
Authorization: Bearer <YOUR_ACCESS_TOKEN>
📢 Response Example:

json
Copy code
{
    "message": "Google Drive connected successfully"
}
4️⃣ Chat API
Endpoint:

http
Copy code
POST /chat
Headers:

http
Copy code
Authorization: Bearer <YOUR_ACCESS_TOKEN>
Body (JSON):

json
Copy code
{
    "message": "Hello, how are you?"
}
📢 Response Example:

json
Copy code
{
    "response": "I am good! How can I assist you?"
}
🛠️ How to Test in Postman
Step 1️⃣: Import Postman Collection
Open Postman.
Click Import → Select "AuthSync_ChatDrive.postman_collection.json" file.
Click Import.
Step 2️⃣: Run API Requests
Select the "AuthSync ChatDrive API" collection.
Choose an API (Auth, Drive Upload, Drive Connect, or Chat).
Click Send to test the API.
📂 Postman Collection
Download the Postman Collection: AuthSync_ChatDrive.postman_collection.json
(Upload this file in your GitHub repository)

⚙️ Deployment
This project is deployed on Render.

Hosting Provider: Render
Live URL: AuthSync ChatDrive
Backend: Django + Gunicorn
📜 License
This project is licensed under the MIT License.

📧 Contact
For any issues, contact:
✉️ Email: your-email@example.com
📌 GitHub Repo: AuthSync ChatDrive

✅ Now your API is fully documented and ready to use! 🚀

markdown
Copy code

### **Next Steps:**
1. **Save this as `README.md`** in your GitHub repository.
2. **Upload `AuthSync_ChatDrive.postman_collection.json`** to your repository.
3. Share the GitHub link for easy access.

🚀 **Now your project is fully documented with API details and Postman collection!**
