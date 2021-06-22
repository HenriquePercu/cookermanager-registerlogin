import bcrypt


# realiza a criptografia da senha
def encrypt(password):
    # get a hash password with a random salt
    return bcrypt.hashpw(password, bcrypt.gensalt())
