# Family Hub
By Jessa and devin.

## Getting started
Open Family Hub on Family Public. A server administrator (role level 80+) adds members in Family. Select an online account or enter an existing account ID. Leave the account blank for a child whose chores a parent manages. Parent access permits chore creation, approval, and payment tracking. All added accounts can read the family organizer and add calendar events. Public visitors cannot read the data.

## Chores and rewards
Parents assign chores and optional USD rewards. An assigned account or parent marks a chore done. Parents approve it or send it back for another try. Approved rewards become unpaid earnings; mark paid only after paying outside the app. Payment transitions are conditional to prevent duplicate payment records. Cancelled chores stay in history.

## Calendar
Everyone added can create events. Creators and parents can edit or delete them. Calendar times are displayed in each device's local timezone. Categories include Sports, Appointment, School, Family, and Other.

## Access
Administrators can remove account access while preserving a member's name and chore history. Server administrators always retain access. Members can view all family chores and rewards. This version has no automatic payments, recurring chores, or reminder notifications.

## Validation
Run `bun test tests`. Backend workflow checks use in-memory SQLite and a mocked runtime SDK. Frontend syntax: `node --check frontend/app.js`. Live runtime verification follows installation approval.
