## 技术栈

语言： python

框架：flask

数据库：sqlite3

## 方案设计

### 需求拆分：
1. 登录注册
2. curd 板块， 其中里面有一个“提问” 板块
3. curd 话题， 其中 “提问” 板块有 已解决和未解决两种类型4. 发邮件
5. 评论
6. curd 用户

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



