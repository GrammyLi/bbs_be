## 技术栈

语言： python

框架：flask

数据库：sqlite3

## 方案设计

### 需求拆分


登录注册

1. 登录接口

2. 注册接口

3. 获取用户详情

4. 更新用户信息

5。 删除用户

CRUD 板块

1. 创建板块

2. 获取板块列表

3. 更新板块

4. 删除板块

CRUD 话题

1. 创建话题

2. 获取话题列表

3. 更新话题

4. 删除话题

邮件

1. 发送邮件

2. 获取邮件列表

3. 更新邮件状态

评论

1. 创建评论

2. 获取评论列表

3. 更新评论

4. 删除评论

CRUD 用户

1. 获取用户列表

2. 更新用户角色

3. 删除用户


### 数据库设计

 

### 用户表 (`user`)

| 字段名         | 类型         | 描述                     |
| -------------- | ------------ | ------------------------ |
| id             | INT          | 主键，自增               |
| ct             | DATETIME     | 创建时间                 |
| ut             | DATETIME     | 更新时间                 |
| status         | ENUM         | 状态（下线、上线）       |
| username       | VARCHAR(255) | 用户名                   |
| email          | VARCHAR(255) | 邮箱                     |
| password       | VARCHAR(255) | 密码                     |
| session_id     | INT          | 关联的会话ID             |
| role           | ENUM         | 角色（普通用户、管理员） |
| signature      | TEXT         | 签名                     |
| avatar         | VARCHAR(255) | 头像URL                  |
| phone_number   | VARCHAR(20)  | 电话号码                 |
| last_login     | DATETIME     | 最后登录时间             |
| email_verified | BOOLEAN      | 邮箱是否验证             |
| bio            | TEXT         | 个人简介                 |

### 会话表 (`session`)

| 字段名     | 类型         | 描述               |
| ---------- | ------------ | ------------------ |
| id         | INT          | 主键，自增         |
| ct         | DATETIME     | 创建时间           |
| ut         | DATETIME     | 更新时间           |
| status     | ENUM         | 状态（下线、上线） |
| token      | VARCHAR(255) | 会话令牌           |
| user_id    | INT          | 关联的用户ID       |
| expires_at | DATETIME     | 会话过期时间       |

### 板块表 (`board`)

| 字段名      | 类型         | 描述               |
| ----------- | ------------ | ------------------ |
| id          | INT          | 主键，自增         |
| ct          | DATETIME     | 创建时间           |
| ut          | DATETIME     | 更新时间           |
| status      | ENUM         | 状态（下线、上线） |
| title       | VARCHAR(255) | 标题               |
| description | TEXT         | 板块描述           |

### 话题表 (`topic`)

| 字段名        | 类型         | 描述               |
| ------------- | ------------ | ------------------ |
| id            | INT          | 主键，自增         |
| ct            | DATETIME     | 创建时间           |
| ut            | DATETIME     | 更新时间           |
| status        | ENUM         | 状态（下线、上线） |
| is_top        | BOOLEAN      | 是否置顶           |
| user_id       | INT          | 关联的用户ID       |
| board_id      | INT          | 关联的板块ID       |
| views         | INT          | 浏览量             |
| title         | VARCHAR(255) | 标题               |
| content       | TEXT         | 内容               |
| resolved      | BOOLEAN      | 是否解决           |
| last_reply_at | DATETIME     | 最后回复时间       |
| reply_count   | INT          | 回复数量           |

### 回复表 (`reply`)

| 字段名     | 类型     | 描述               |
| ---------- | -------- | ------------------ |
| id         | INT      | 主键，自增         |
| ct         | DATETIME | 创建时间           |
| ut         | DATETIME | 更新时间           |
| status     | ENUM     | 状态（下线、上线） |
| user_id    | INT      | 关联的用户ID       |
| topic_id   | INT      | 关联的话题ID       |
| content    | TEXT     | 内容               |
| like_count | INT      | 点赞数量           |

### 邮件表 (`mail`)

| 字段名      | 类型         | 描述                    |
| ----------- | ------------ | ----------------------- |
| id          | INT          | 主键，自增              |
| ct          | DATETIME     | 创建时间                |
| ut          | DATETIME     | 更新时间                |
| status      | ENUM         | 状态（下线、上线）      |
| title       | VARCHAR(255) | 标题                    |
| content     | TEXT         | 内容                    |
| sender_id   | INT          | 发件人ID                |
| receiver_id | INT          | 收件人ID                |
| read        | BOOLEAN      | 是否已读                |
| attachments | TEXT         | 附件（JSON 或 VARCHAR） |




### 接口设计

  接口设计

#### 1. 用户接口

##### 登录接口

- **URL**: `/user/login`

- **方法**: `POST`

- 请求参数  :

  ```json
  {
      "email": "user@example.com",
      "password": "password123"
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "登录成功",
      "code": 200,
      "data": {
          "token": "session_token",
          "user": {
              "id": 1,
              "email": "user@example.com",
              "username": "username",
              "avatar": "avatar_url",
              "role": "普通用户"
          }
      }
  }
  ```

##### 注册接口

- **URL**: `/user/register`

- **方法**: `POST`

- 请求参数  :

  ```  json
  {
      "email": "user@example.com",
      "password": "password123",
      "username": "username"
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "注册成功",
      "code": 201,
      "data": {
          "user": {
              "id": 1,
              "email": "user@example.com",
              "username": "username",
              "avatar": "avatar_url",
              "role": "普通用户"
          }
      }
  }
  ```

##### 获取用户详情

- **URL**: `/user/detail`

- **方法**: `GET`

- 请求参数  :

  - Headers: `Authorization: Bearer {token}`

- 响应参数  :

  ```  json
  {
      "msg": "获取成功",
      "code": 200,
      "data": {
          "user": {
              "id": 1,
              "email": "user@example.com",
              "username": "username",
              "avatar": "avatar_url",
              "role": "普通用户",
              "signature": "签名",
              "phone_number": "1234567890",
              "bio": "个人简介"
          }
      }
  }
  ```

##### 更新用户信息

- **URL**: `/user/update`

- **方法**: `PUT`

- 请求参数  :

  ```  json
  {
      "username": "new_username",
      "avatar": "new_avatar_url",
      "signature": "new_signature",
      "phone_number": "new_phone_number",
      "bio": "new_bio"
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "更新成功",
      "code": 200,
      "data": {
          "user": {
              "id": 1,
              "email": "user@example.com",
              "username": "new_username",
              "avatar": "new_avatar_url",
              "signature": "new_signature",
              "phone_number": "new_phone_number",
              "bio": "new_bio"
          }
      }
  }
  ```

##### 删除用户

- **URL**: `/user/delete`

- **方法**: `DELETE`

- 请求参数  :

  - Headers: `Authorization: Bearer {token}`

- 响应参数  :

  ```  json
  {
      "msg": "删除成功",
      "code": 200
  }
  ```

#### 2. 板块接口

##### 创建板块

- **URL**: `/board/create`

- **方法**: `POST`

- 请求参数  :

  ```  json
  {
      "title": "板块标题",
      "description": "板块描述"
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "创建成功",
      "code": 201,
      "data": {
          "board": {
              "id": 1,
              "title": "板块标题",
              "description": "板块描述"
          }
      }
  }
  ```

##### 获取板块列表

- **URL**: `/board/list`

- **方法**: `GET`

- **请求参数**: 无

- 响应参数  :

  ```  json
  {
      "msg": "获取成功",
      "code": 200,
      "data": {
          "boards": [
              {
                  "id": 1,
                  "title": "板块标题",
                  "description": "板块描述"
              }
          ]
      }
  }
  ```

##### 更新板块

- **URL**: `/board/update/{board_id}`

- **方法**: `PUT`

- 请求参数  :

  ```  json
  {
      "title": "新板块标题",
      "description": "新板块描述"
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "更新成功",
      "code": 200,
      "data": {
          "board": {
              "id": 1,
              "title": "新板块标题",
              "description": "新板块描述"
          }
      }
  }
  ```

##### 删除板块

- **URL**: `/board/delete/{board_id}`

- **方法**: `DELETE`

- **请求参数**: 无

- 响应参数  :

  ```  json
  {
      "msg": "删除成功",
      "code": 200
  }
  ```

#### 3. 话题接口

##### 创建话题

- **URL**: `/topic/create`

- **方法**: `POST`

- 请求参数  :

  ```  json
  {
      "title": "话题标题",
      "content": "话题内容",
      "board_id": 1
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "创建成功",
      "code": 201,
      "data": {
          "topic": {
              "id": 1,
              "title": "话题标题",
              "content": "话题内容",
              "board_id": 1,
              "user_id": 1,
              "is_top": false,
              "views": 0,
              "resolved": false
          }
      }
  }
  ```

##### 获取话题列表

- **URL**: `/topic/list`

- **方法**: `GET`

- **请求参数**: 无

- 响应参数  :

  ```  json
  {
      "msg": "获取成功",
      "code": 200,
      "data": {
          "topics": [
              {
                  "id": 1,
                  "title": "话题标题",
                  "content": "话题内容",
                  "board_id": 1,
                  "user_id": 1,
                  "is_top": false,
                  "views": 100,
                  "resolved": false
              }
          ]
      }
  }
  ```

##### 更新话题

- **URL**: `/topic/update/{topic_id}`

- **方法**: `PUT`

- 请求参数  :

  ```  json
  {
      "title": "新话题标题",
      "content": "新话题内容",
      "is_top": true,
      "resolved": true
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "更新成功",
      "code": 200,
      "data": {
          "topic": {
              "id": 1,
              "title": "新话题标题",
              "content": "新话题内容",
              "is_top": true,
              "resolved": true
          }
      }
  }
  ```

##### 删除话题

- **URL**: `/topic/delete/{topic_id}`

- **方法**: `DELETE`

- **请求参数**: 无

- 响应参数  :

  ```  json
  {
      "msg": "删除成功",
      "code": 200
  }
  ```

#### 4. 邮件接口

##### 发送邮件

- **URL**: `/mail/send`

- **方法**: `POST`

- 请求参数  :

  ```  json
  {
      "title": "邮件标题",
      "content": "邮件内容",
      "receiver_id": 2
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "发送成功",
      "code": 201,
      "data": {
          "mail": {
              "id": 1,
              "title": "邮件标题",
              "content": "邮件内容",
              "sender_id": 1,
              "receiver_id": 2,
              "read": false
          }
      }
  }
  ```

##### 获取邮件列表

- **URL**: `/mail/list`

- **方法**: `GET`

- **请求参数**: 无

- 响应参数  :

  ```  json
  {
      "msg": "获取成功",
      "code": 200,
      "data": {
          "mails": [
              {
                  "id": 1,
                  "title": "邮件标题",
                  "content": "邮件内容",
                  "sender_id": 1,
                  "receiver_id": 2,
                  "read": false
              }
          ]
      }
  }
  ```

##### 更新邮件状态

- **URL**: `/mail/update/{mail_id}`

- **方法**: `PUT`

- 请求参数  :

  ```  json
  {
      "read": true
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "更新成功",
      "code": 200,
      "data": {
          "mail": {
              "id": 1,
              "title": "邮件标题",
              "content": "邮件内容",
              "sender_id": 1,
              "receiver_id": 2,
              "read": true
          }
      }
  }
  ```

#### 5. 评论接口

##### 创建评论

- **URL**: `/reply/create`

- **方法**: `POST`

- 请求参数  :

  ```  json

  {
      "topic_id": 1,
      "content": "评论内容"
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "评论成功",
      "code": 201,
      "data": {
          "reply": {
              "id": 1,
              "topic_id": 1,
              "user_id": 1,
              "content": "评论内容",
              "like_count": 0
          }
      }
  }
  ```

##### 获取评论列表

- **URL**: `/reply/list`

- **方法**: `GET`

- 请求参数  :

  ```  json
  {
      "topic_id": 1
  }
  ```

- 响应参数  :

  ```  json
  {
      "msg": "获取成功",
      "code": 200,
      "data": {
          "replies": [
              {
                  "id": 1,
                  "topic_id": 1,
                  "user_id": 1,
                  "content": "评论内容",
                  "like_count": 0
              }
          ]
      }
  }
  ```

##### 更新评论

- **URL**: `/reply/update/{reply_id}`

- **方法**: `PUT`

- 请求参数:

  ```  json
  {
      "content": "更新后的评论内容"
  }
  ```

- 响应参数  :

  ```json
  {
      "msg": "更新成功",
      "code": 200,
      "data": {
          "reply": {
              "id": 1,
              "content": "更新后的评论内容"
          }
      }
  }
  ```

##### 删除评论

- **URL**: `/reply/delete/{reply_id}`

- **方法**: `DELETE`

- **请求参数**: 无

- 响应参数:

 ```json
   
  {
      "msg": "删除成功",
      "code": 200
  }
  ```

#### 6. 用户管理接口

##### 获取用户列表

- **URL**: `/user/list`

- **方法**: `GET`

- **请求参数**: 无

- 响应参数:

  ```json
  {
      "msg": "获取成功",
      "code": 200,
      "data": {
          "users": [
              {
                  "id": 1,
                  "email": "user@example.com",
                  "username": "username",
                  "avatar": "avatar_url",
                  "role": "普通用户",
                  "signature": "签名",
                  "phone_number": "1234567890",
                  "bio": "个人简介"
              }
          ]
      }
  }
  ```

##### 更新用户角色

- **URL**: `/user/update-role/{user_id}`

- **方法**: `PUT`

- 请求参数:

  ```json
   {
      "role": "管理员"
  }
  ```

- 响应参数:

  ```json
   
  {
      "msg": "角色更新成功",
      "code": 200,
      "data": {
          "user": {
              "id": 1,
              "role": "管理员"
          }
      }
  }
  ```

##### 删除用户

- **URL**: `/user/delete/{user_id}`

- **方法**: `DELETE`

- **请求参数**: 无

- 响应参数:

  ```
  {
      "msg": "删除成功",
      "code": 200
  }
  ```

### 