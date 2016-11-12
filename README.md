# todoist.py
http://pytodoist.readthedocs.io/en/latest/modules.html

https://developers.google.com/identity/protocols/OAuth2UserAgent

https://docs.python.org/3/library/configparser.html


Todoist.py
--A Python & pytodoist bred CLI application that allows you to manage 
your todo-list from your system shell.

Feature Todo:
-Get list of tasks
-Create new tasks
-Mark created tasks as complete

Basic usage will center around CRUD commands:
-Create (mk, create)
-Read (ls, read)
-Update (edit)
-Delete (rm, delete)
--With a utility interface for user and application settings.

Entities:

Login:
-Parent of User


User:
-add_filter, add_label, add_project, clear_reminder_locations, delete,
disable_email_notifications, disable_karma, disable_push_notifications,
..., get_archived_projects, get_completed_tasks, get_filter, 
get_filters, get_label, get_labels, get_notes, get_productivity_stats, 
get_project, get_projects, get_reminders, get_tasks, 
get_uncompleted_tasks, search_tasks, sync, update (user details), 


Filter:
-delete, update, add_filter
-id, name, query, color, item_order, owner
Label:
-delete, update, add_label
-id, uid, name, color, owner, is_deleted

Project:
-Child of User
-add_note, add_task, archive, collapse, delete, delete_collaborator,
get_completed_tasks, get_notes, get_tasks, get_uncompleted_tasks, share,
take_ownership, unarchive, update
-id, name, color, collapsed, owner, last_updated, user_id, cache_count,
item_order, indent, is_deleted, is_archived, archived_date, 
archived_timestamp, inbox_project

Task:
-Child of Project
-add_date_reminder, add_location_reminder, add_note, complete, delete, 
get_notes, get_reminders, move, uncomplete, update
Note:
--Child of Task
--delete, update, add_note
--id, content, item_id, task, posted, is_deleted, is_archived, 
posted_uid, uids_to_notify
Priority:
--Attribute of Task
--NO, LOW, NORMAL, HIGH, VERY_HIGH
Reminder:
--delete
--id, item_id, service, due_date_utc, date_string, date_lang, notify_uid
, task


Query:
-Child of User?
-search_tasks(attribute)
