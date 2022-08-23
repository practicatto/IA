<script>
	import '../app.css';
	import Header from '$lib/components/layout/Header.svelte';
</script>

<Header />

<div class="container mx-auto my-6 max-w">
	<slot />
</div>
