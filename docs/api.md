# API Documentation
## Contents
| **API** | **Endpoint**
| --- | ---|
| [Count](#Count) | `POST /wordcount` |

### Count

This function calculates word frequency from a page source. It accepts payload in JSON format.

* **URL:** `/wordcount`
* **Method:** `POST`
* **Authorization:** _TBD_
* **Request Body**

    | **Param Name** | **Type** | **Description**
    | --- | ---| --- |
    | word | string | The word we want to count from the page source
    | url | string | The website we want to extract the source text from

* **Success Response:**
  * **Code:** 200
  * **Content: _json_**

    | **Attribute** | **Type** | **Description**
    | --- | ---| --- |
    | count | int | The frequency of word from the page source
    | status | string | Returns "ok" if successful (code 200)

  * **Example:**

    ```
    {
          "count": 12,
          "status": "ok"
    }
    ```

* **Error Response:**

    | **Error** | **Message** |
    | --- | --- |
    |`400` | `Bad Request`
    |`404`| `Cannot be found`
    |`500`| `System Error`

    * **Example:**

    ```
    {
          "message": "Something went wrong",
          "status": 500
    }
    ```

### **Sample Usage**
* **Request**

  ```
  $ curl -X POST \
      -H "Content-type: application/json" \
      -d '{"word": "fit","url": "https://virtusize.jp"}' \
      "localhost:5000/wordcount"
  ```

* **Response**
  ```
  {
        "count": 12,
        "status": "ok"
  }
  ```
