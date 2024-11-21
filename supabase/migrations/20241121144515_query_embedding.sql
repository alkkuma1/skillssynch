create trigger embed_query
  after insert on "public"."query"
  referencing new table as inserted
  for each statement
  execute procedure "public"."embed"(query, query_embedding, 10);