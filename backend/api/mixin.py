from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class StaffEditotoPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]