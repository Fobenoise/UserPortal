class RolesDBRouter:
    """
    A router to control database operations on models for the 'roles' app.
    All models in the 'roles' app should go to the 'roles_db' database.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'roles':
            return 'roles_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'roles':
            return 'roles_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'roles' or obj2._meta.app_label == 'roles':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'roles':
            return db == 'roles_db'
        return None