def replace_domain(email, old_domain, new_domain):
    if "@"+old_domain in email:
        index=email.index("@"+old_domain)
        new_email=email[:index+1]+new_domain
        return new_email
    return email # if the email dont contain old domain, just return email.