# Mini Challenge 2

## User authentication and authorization

### Aceptance Criteria
1. As an end user I should be able to sign up so that I can start collaborating on issues.
2. As an end user I should be able to log in so that I can interact with the board.
3. As an end user I should be able to log out to avoid someone using my account.
4. As an end user I should be able to change my password if it no longer feels secure.
5. As an end user I would like to be able to reset my password in case I've forgotten it.

### Note
This is an exercise to practice `overriding templates`
### Phase 2
1. As an end user, when I sign up I should be able to specify my team so I can jump directly to my team's board.
2. As an end user, when I sign up, I should be able to specify my role so that I can gain access to special functions based on my role.

### Note for phase 2
This is an exercise in `custom migrations`. Prepopulate the `Team` and the `Role` model(s) in `accounts/models.py` so that there are at least 3 entries for each model whenever our application is deployed.

### Suggestions for teams:
Alpha, Bravo, Charlie (NATO phonetic alphabet)

### Roles
Based off of scrum, we need the following 3 roles:
1. developer - team members who execute the work defined in issues
2. scrum master - the team's coach
3. product owner - the person on the team who defines what is built