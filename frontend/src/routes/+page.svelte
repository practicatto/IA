<script lang="ts">
	import Icon from '$lib/components/Icon.svelte';
	import cloud from '$lib/assets/icons/cloud.svg?raw';
	import Canvas from '$lib/components/Canvas.svelte';
	let fileVar: any;
	let isLoading = false;
	let msg: any;

	async function submitForm() {
		isLoading = true;
		const data = new FormData();
		data.append('file', fileVar[0]);
		//console.log(JSON.stringify(data));
		//console.log(fileVar);
		//console.log(JSON.stringify(fileVar));

		const res = await fetch('http://127.0.0.1:8000/upload', {
			method: 'POST',
			body: data
		});
		isLoading = false;
		msg = await res.json();
	}

	async function getHello() {
		const res = await fetch(`http://127.0.0.1:8000/`);
		const text = await res.text();

		if (res.ok) {
			return text;
		} else {
			throw new Error(text);
		}
	}
</script>

<div>
	<div class="md:grid md:grid-cols-3 md:gap-6 ">
		<div class="md:col-span-1 flex items-center">
			<div class="px-4 sm:px-0">
				<h2 class="text-4xl font-bold sm:text-3xl md:text-3xl lg:text-5xl xl:text-4xl">
					¡Bienvenido!
				</h2>
				<p class="mt-1  dark:text-gray-300 text-gray-600">Algo sobre el proyecto</p>
			</div>
		</div>
		<div class="mt-5 md:mt-0 md:col-span-2">
			<form class="space-y-8 divide-y">
				<div class="flex justify-center items-center w-full">
					<label
						for="dropzone-file"
						class="flex flex-col justify-center items-center w-full h-64 bg-gray-50 rounded-lg border-2 border-gray-300 border-dashed cursor-pointer dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
					>
						<div class="flex flex-col justify-center items-center pt-5 pb-6 ">
							<div class="text-gray-200">
								<Icon class="mx-auto h-28 w-full" fill="currentColor" data={cloud} />
							</div>

							<p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
								<span class="font-semibold"
									>Haz click para subir una secuencia de medios porosos</span
								>
							</p>
							<p class="text-xs text-gray-500 dark:text-gray-400">.ZIP or .npy</p>
						</div>
						<input id="dropzone-file" type="file" class="hidden" required />
					</label>
				</div>
			</form>
		</div>
	</div>
</div>

<form class="my-12" on:submit|preventDefault={submitForm}>
	<input
		value="Predecir Cortes"
		type="submit"
		class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-teal-500 hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500"
	/>
</form>

{#if isLoading}
	<div class="text-center">
		<p>... cargando</p>
	</div>
{/if}

{#if msg}
	<div class="text-center">
		<p>{JSON.stringify(msg)}</p>
	</div>
{/if}

<Canvas />
