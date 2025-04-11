from modules.srp_module import UserManager

manager = UserManager()

u1 = manager.create_user("Саша", "alex@gmail.com")
u2 = manager.create_user("Ігор", "igor@gmail.com")

for u in manager.get_users():
    print(u.name, u.email, "\n")

manager.update_user(u2, email="newigor@gmail.com")


manager.delete_user(u1)

print()

for u in manager.get_users():
    print(u.name, u.email, "\n")
