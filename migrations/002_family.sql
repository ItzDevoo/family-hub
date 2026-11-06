CREATE TABLE members (id TEXT PRIMARY KEY, name TEXT NOT NULL, user_id TEXT UNIQUE, parent INTEGER NOT NULL DEFAULT 0);
CREATE TABLE chores (id TEXT PRIMARY KEY, title TEXT NOT NULL, notes TEXT NOT NULL, member_id TEXT NOT NULL REFERENCES members(id), due TEXT NOT NULL, cents INTEGER NOT NULL CHECK(cents >= 0), status TEXT NOT NULL DEFAULT 'open', created_by TEXT NOT NULL, approved_by TEXT, paid_at INTEGER);
CREATE TABLE events (id TEXT PRIMARY KEY, title TEXT NOT NULL, category TEXT NOT NULL, starts INTEGER NOT NULL, ends INTEGER NOT NULL, location TEXT NOT NULL, notes TEXT NOT NULL, author_id TEXT NOT NULL);
CREATE INDEX events_start ON events(starts);
CREATE INDEX chores_member ON chores(member_id);
