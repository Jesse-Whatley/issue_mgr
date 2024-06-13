# Mini Challenge 3

## Issue Management

### Acceptance Criteria

## Phase 1
1. Create a custom migration for Status such that you have the following statuses:
1.1. to do - an issue for which work has not yet begun
1.2. in progress - an issue actively being worked on
1.3. done - an issue for which work has been completed
2. Run migrations.
3. Create a view that powers a "board" allowing users to see issues categories based on the statuses mentioned in criteria 1 of this list.
4. Create a detail view to see issues in more detail.
Messages addressed to "Meeting Group Chat" will also appear in the meeting group chat in Team Chat

Rafael GPL 1:07 PM
## Phase 2
1. As a product owner I should be able to create issues to represent work that needs doing.
1.1. Only the product owner can create new issues.
2. As a developer, I should be able to update the status for my issue so that I can represent what I am working on.
2.1. Only developers can update status from to do, to in progress or done (in that order).
3. As a scrum master, I would like to be able to reset issues from done to to do, so that I can return work that has not been completed correctly.
3.1. Only scrum masters can reset an issue from done to to do.
4. As a logged in user I should be able to update an issue that belongs to my team so that I can represent scope changes.
5. As a team member, I should be able to view the board (and issues) that correspond solely to my team.