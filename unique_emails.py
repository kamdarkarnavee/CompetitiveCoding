def numUniqueEmails(emails):
    emails_set = set()

    for e in emails:
        local, domain = e.split('@')
        local = local.replace('.', '')
        local = local.split('+')[0]
        emails_set.add(''.join([local, '@', domain]))
    return len(emails_set)


emails = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
print(numUniqueEmails(emails))
