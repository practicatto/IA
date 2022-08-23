<script lang="ts">
	import { fade } from 'svelte/transition';
	import { Popover, PopoverButton, PopoverPanel } from '@rgossiaux/svelte-headlessui';
	import menu from '$lib/assets/icons/menu.svg?raw';
	import x from '$lib/assets/icons/x.svg?raw';
	import Icon from '$lib/components/Icon.svelte';
	import Theme from '$lib/Theme.svelte';
	import porosdark from '$lib/assets/logo/porosdark.svg';
	import poroslight from '$lib/assets/logo/poroslight.svg';
	const navigation = [
		{ text: 'Home', url: '/' },
		{ text: 'Contribuidores', url: '/contributors' },
		{ text: 'Repo', url: 'https://github.com/eljosephavila123/porous-medium-prediction' }
	];
</script>

<Popover class="relative">
	<div class="flex items-center justify-between px-4 py-6 sm:px-6 md:justify-start md:space-x-10">
		<div class="flex justify-start lg:w-0 lg:flex-1">
			<a href="/">
				<img class="w-52 h-32 hidden dark:inline" src={porosdark} alt="logo" />
				<img class="w-52 h-32 dark:hidden" src={poroslight} alt="logo" />
			</a>
		</div>
		<div class="-my-2 -mr-2 md:hidden">
			<PopoverButton
				class="inline-flex items-center justify-center rounded-md p-2 text-teal-500 hover:bg-teal-500 hover:text-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-teal-500"
			>
				<span class="sr-only">Open menu</span>
				<Icon data={menu} fill="currentColor" aria-hidden="true" />
			</PopoverButton>
		</div>
		<nav class="hidden space-x-10 md:flex">
			{#each navigation as item}
				<a
					href={item.url}
					class="text-base font-medium dark:text-teal-400 text-teal-600 active:text-teal-600 hover:text-teal-700"
				>
					{item.text}
				</a>
			{/each}
		</nav>

		<div class="items-center justify-end md:flex md:flex-1 lg:w-0">
			<Theme />
		</div>

		<PopoverPanel
			focus
			class="absolute inset-x-0 top-0 origin-top-right transform p-2 transition md:hidden"
		>
			<div
				transition:fade={{ duration: 100 }}
				class="divide-y-2 divide-gray-200 rounded-lg bg-teal-50 shadow-lg ring-1 ring-white ring-opacity-5"
			>
				<div class="px-5 pt-5 pb-6">
					<div class="flex items-center justify-between">
						<div>
							<div class="aspect-square h-8 bg-teal-500" />
						</div>
						<div class="-mr-2">
							<PopoverButton
								class="inline-flex items-center justify-center rounded-md p-2 text-teal-500 hover:bg-teal-700 hover:text-teal-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-teal-500"
							>
								<Icon data={x} fill="currentColor" aria-hidden="true" />
							</PopoverButton>
						</div>
					</div>
				</div>
				<div class="py-6 px-5">
					<div class="grid grid-cols-2 gap-4">
						{#each navigation as item}
							<a href={item.url} class="text-base font-medium text-teal-500 hover:text-teal-700">
								{item.text}
							</a>
						{/each}
					</div>
				</div>
			</div>
		</PopoverPanel>
	</div></Popover
>
