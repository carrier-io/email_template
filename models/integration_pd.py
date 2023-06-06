from typing import List

from pydantic import BaseModel, EmailStr, validator


class SmtpIntegrationField(BaseModel):
    id: int
    project_id: int | None = None


class IntegrationModel(BaseModel):
    _default_template = 'PGRpdj5EZWZhdWx0IHRlbXBsYXRlPC9kaXY+'

    smtp_integration: SmtpIntegrationField
    template: str | None = _default_template

    @staticmethod
    def check_connection():
        return True

    @validator('*', pre=True)
    def validate_template(cls, value):
        if value == '':
            return cls._default_template
        return value


class SecurityTestModel(BaseModel):
    id: int
    recipients: List[EmailStr]


class PerformanceBackendTestModel(SecurityTestModel):
    ...


class PerformanceUiTestModel(SecurityTestModel):
    ...


class TaskSettingsModel(IntegrationModel):
    galloper_url: str = '{{secret.galloper_url}}'
    token: str = '{{secret.auth_token}}'
    project_id: int
