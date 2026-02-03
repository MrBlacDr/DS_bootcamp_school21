def format_date: split("T")[0];

["id", "created_at", "name", "has_test", "alternate_url"],
(.items[] | [
  .id,
  (.created_at | format_date),
  .name,
  .has_test,
  .alternate_url
])
| @csv