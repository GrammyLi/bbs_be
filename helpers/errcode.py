class ErrCode:
    ERROR_SUCCESS = 200

    ERROR_VALIDATION_ERROR = 4000
    ERROR_WRONG_PASSWORD = 4001
    ERROR_EMAIL_ALREADY_EXISTS = 4002
    ERROR_USER_NOT_EXISTS = 4003
    ERROR_USER_NOT_LOGGED_IN = 4004

    ERROR_TOKEN_EXPIRED = 4010
    ERROR_TOKEN_INVALID = 4011
    ERROR_AUTHORIZATION_REQUIRED = 4012
    ERROR_TOKEN_REVOKED = 4013

    ERROR_INTERNAL_SERVER_ERROR = 500

    ERROR_MESSAGES = {
        ERROR_SUCCESS: "",
        ERROR_INTERNAL_SERVER_ERROR: "Internal Server Error",
        ERROR_VALIDATION_ERROR: "请求参数有误",
        ERROR_WRONG_PASSWORD: "密码错误",
        ERROR_EMAIL_ALREADY_EXISTS: "邮箱已使用",
        ERROR_USER_NOT_EXISTS: "用户不存在",
        ERROR_USER_NOT_LOGGED_IN: "用户未登陆",
        ERROR_TOKEN_EXPIRED: "Token已过期",
        ERROR_TOKEN_INVALID: "Token验证失败",
        ERROR_AUTHORIZATION_REQUIRED: "未授权",
        ERROR_TOKEN_REVOKED: "Token已被注销",
    }

    @classmethod
    def get_error_message(cls, error_code):
        return cls.ERROR_MESSAGES.get(error_code, "Unknown Error")
