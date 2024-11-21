create trigger embed_document_sections
  after insert on "public"."documentdata"
  referencing new table as inserted
  for each statement
  execute procedure "public"."embed"(chunk, chunk_embedding, 10);