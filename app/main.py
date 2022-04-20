from app.services.key import key_present, gen_key

if not key_present():
    gen_key()
