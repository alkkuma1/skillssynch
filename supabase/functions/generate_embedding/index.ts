// Follow this setup guide to integrate the Deno language server with your editor:
// https://deno.land/manual/getting_started/setup_your_environment
// This enables autocomplete, go to definition, etc.

// Setup type definitions for built-in Supabase Runtime APIs
import "jsr:@supabase/functions-js/edge-runtime.d.ts"

// Function to process incoming HTTPS requests and send back responses
Deno.serve(async (req) => {
  const { chunk } = await req.json();

  // Generate the embedding from chunks
  const embedding = await session.run(chunk, {
    mean_pool: true,
    normalize: true,
  });

  // Return the embedding
  return new Response(
    JSON.stringify({ embedding }),
    { headers: { 'Content-Type': 'application/json' } }
  );
});
