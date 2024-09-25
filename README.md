![Banner](https://github.com/user-attachments/assets/9022ae95-4b2f-4ad8-8590-731b35ac83a2)


## Who we are
We are a free subdomain service who provide sweet-looking `.isfreelancer.com` subdomains for freelancers!

## Why use us?
- We support many types of records
- Quick PR response times*
- Fast support for issues

###### *Response times may vary based on the amount of PRs we are receiving.

## Register
- [Fork](https://github.com/livrasand/isfreelancer.com) and star this repository
- **Edit** the `subdomains.json` file and add the following fragment to register your subdomain:
```json
 {
   "username": "your-github-username",
   "subdomain": "your-subdomain"
 },
```
This will register `your-subdomain.isfreelancer.com`.
- Your pull request will be reviewed and merged. *Make sure to keep an eye on it incase we need you to make any changes!*
- After the pull request is merged, please allow up to 24 hours for the changes to propagate
- Enjoy your new `.isfreelancer.com` domain!

## Use
The subdomains, being CNAME records, can be used to point to a specific server or hosting service. Below are instructions on how to use your subdomains:

### Option A: Using the subdomain with GitHub Pages

If a user wants to host their content on **GitHub Pages**, they can point their subdomain `username.isfreelancer.com` to their GitHub Pages site (e.g., `username.github.io`).

#### Steps:

1. **Create a GitHub Pages repository**:
   - The user needs to have a repository named `username.github.io` in their GitHub account.
   - Make sure that **GitHub Pages** is enabled in the repository settings.

2. **Add the subdomain in GitHub Pages**:
   - In the `username.github.io` repository, create a file called `CNAME` at the root of the repository and add the subdomain, for example: `username.isfreelancer.com`.

3. **Verify DNS**:
   - Since the CNAME record for the subdomain has already been created pointing to `username.github.io`, the subdomain `username.isfreelancer.com` should now point to the GitHub Pages site.

### Option B: Using the subdomain with any other Hosting

Subdomains can be used to direct traffic to any hosting service or server. Users need to ensure the CNAME record points correctly to the desired service.

#### Steps:

1. **Ensure the hosting service supports CNAME**:
   - The user must ensure that the hosting service where the website will be hosted supports **CNAME** records and allows mapping a subdomain to its IP address or URL.

2. **Configure the hosting service**:
   - Depending on the hosting service used (e.g., **Netlify**, **Vercel**, **DigitalOcean**, etc.), users need to configure their subdomain in the service's domain settings.
   - In most cases, the user will only need to add the subdomain `username.isfreelancer.com` in the service's configuration, and the traffic will be automatically routed to their site.
