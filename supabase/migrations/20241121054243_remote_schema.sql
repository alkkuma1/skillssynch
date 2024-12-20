create extension if not exists "vector" with schema "extensions";


drop function if exists "public"."embed"();

create table "public"."documentdata" (
    "id" bigint generated by default as identity not null,
    "created_at" timestamp with time zone not null default now(),
    "chunk" text not null,
    "filename" text not null,
    "URL" text not null,
    "metadata" text,
    "chunk_embedding" vector,
    "page_number" numeric
);


CREATE UNIQUE INDEX documentdata_pkey ON public.documentdata USING btree (id);

alter table "public"."documentdata" add constraint "documentdata_pkey" PRIMARY KEY using index "documentdata_pkey";

grant delete on table "public"."documentdata" to "anon";

grant insert on table "public"."documentdata" to "anon";

grant references on table "public"."documentdata" to "anon";

grant select on table "public"."documentdata" to "anon";

grant trigger on table "public"."documentdata" to "anon";

grant truncate on table "public"."documentdata" to "anon";

grant update on table "public"."documentdata" to "anon";

grant delete on table "public"."documentdata" to "authenticated";

grant insert on table "public"."documentdata" to "authenticated";

grant references on table "public"."documentdata" to "authenticated";

grant select on table "public"."documentdata" to "authenticated";

grant trigger on table "public"."documentdata" to "authenticated";

grant truncate on table "public"."documentdata" to "authenticated";

grant update on table "public"."documentdata" to "authenticated";

grant delete on table "public"."documentdata" to "service_role";

grant insert on table "public"."documentdata" to "service_role";

grant references on table "public"."documentdata" to "service_role";

grant select on table "public"."documentdata" to "service_role";

grant trigger on table "public"."documentdata" to "service_role";

grant truncate on table "public"."documentdata" to "service_role";

grant update on table "public"."documentdata" to "service_role";


