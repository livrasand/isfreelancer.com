![Banner](https://github.com/user-attachments/assets/9022ae95-4b2f-4ad8-8590-731b35ac83a2)


## Who we are
We are a free subdomain service who provide sweet-looking `.isfreelancer.com` subdomains for freelancers!

## Why use us?
- We support many types of records
- Quick PR response times*
- Fast support for issues

###### *Response times may vary based on the amount of PRs we are receiving.

## Register
1. [Fork](https://github.com/livrasand/isfreelancer.com) and star this repository
2. In the `subdomains` folder, create a JSON file named `subdomain.json` and include the following information to register your subdomain:
   
    **Name:** The hostname or prefix of your subdomain (without the `.isfreelancer.com`). For example, `blog` or `store`. The name must follow these rules:

   - It can include a period (`.`) but not as the first or last character.
   - It cannot contain ellipses (`...`).
   - It cannot start or end with a hyphen (`-`).
   - It cannot be the `@` symbol.
   - It must not already be in use by another record.
   - It must have no more than 63 characters per label (separated by periods).
   
    Example: `63characters.63characters.goodexample.com`.
    The total length must not exceed 255 characters.

```json
{
  "username": "your-github-username",
  "subdomain": "your-subdomain",
  "email": "your-email",
  "url": "your-domain-or-ip"
}
```
This will register `your-subdomain.isfreelancer.com`.
3. Your pull request will be reviewed and merged. *Make sure to keep an eye on it incase we need you to make any changes!*
4. After the pull request is merged, please allow up to 24 hours for the changes to propagate
5. Enjoy your new `.isfreelancer.com` domain!
