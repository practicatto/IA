<script lang="ts">
	type Contributor = {
		name: string;
		title: string;
		description: string;
		image: string;
		linkedin: string;
		github: string;
		twitter: string;
	};

	const contributors: Contributor[] = [
		{
			name: 'Joseph Avila',
			title: 'Estudiante de Inteligencia Artificial',
			description:
				'Estudiante de Ingenieria en ciencias computacionales en ESPOL con entusiasmo para crear soluciones a problemas que se presentan en el mundo de la computación.',
			image:
				'https://media-exp1.licdn.com/dms/image/C4D03AQE-ok0_SUbeRw/profile-displayphoto-shrink_800_800/0/1626554538215?e=1666828800&v=beta&t=GVhKnwdm_DU6MPoF-qk6JTl5Rt8o4IDxWMJCpsfzyA0',
			twitter: 'https://twitter.com/soyjosephavila',
			linkedin: 'https://www.linkedin.com/in/josephavilaalvarez/',
			github: 'https://www.github.com/eljosephavila123'
		},
		{
			name: 'Joangie Márquez',
			title: 'Estudiante de Inteligencia Artificial',
			description:
				'Estudiante de Ingenieria en ciencias computacionales en ESPOL con entusiasmo para crear soluciones a problemas que se presentan en el mundo de la computación.',
			image:
				'https://media-exp1.licdn.com/dms/image/C4D03AQESdO4SUNNv_Q/profile-displayphoto-shrink_400_400/0/1657399864834?e=1666828800&v=beta&t=6fftJ29nycVA4YD_hw-WawAYql_xqkwmILHg1kXCo2I',
			twitter: 'https://twitter.com/practicatto',
			linkedin: 'https://www.linkedin.com/in/joangie-marquez/?_l=en_US/',
			github: 'https://www.github.com/practicatto'
		},
		{
			name: 'Henry Siviachay',
			title: 'Estudiante de Inteligencia Artificial',
			description:
				'Estudiante de Ingenieria en ciencias computacionales en ESPOL con entusiasmo para crear soluciones a problemas que se presentan en el mundo de la computación.',
			image:
				'https://media-exp1.licdn.com/dms/image/C4D03AQHL51X0rwoQ5A/profile-displayphoto-shrink_400_400/0/1626747869162?e=1666828800&v=beta&t=MSB0iBCvz8VMTtxt8Hp0i7U3rRPCmZKzFSUi2oMEdfA',
			twitter: 'https://twitter.com/henrysiviachay',
			linkedin: 'https://www.linkedin.com/in/henry-siviachay-a8a8b1177/',
			github: 'https://www.github.com/henrysiviachay'
		}
	];
</script>

<div class="bg-white dark:bg-gray-800 dark:text-white-200">
	<div class="mx-auto py-12 px-4 max-w-7xl sm:px-6 lg:px-8 lg:py-24">
		<div class="space-y-12 lg:grid lg:grid-cols-3 lg:gap-8 lg:space-y-0">
			<div class="space-y-5 sm:space-y-4">
				<h2 class="text-3xl font-bold tracking-tight sm:text-4xl sm:tracking-tight">
					Grupo 8: J<sup>2</sup>H
				</h2>
				<p class="text-xl text-gray-500 dark:text-gray-300">
					Este proyecto no pudo ser posible sin la colaboración de estas personas. Adicionalmente
					agradecemos a aquellos que también nos ayudaron a hacer este proyecto con su
					retroalimentación.
				</p>
			</div>
			<div class="lg:col-span-2">
				<ul
					class="space-y-12 sm:divide-y sm:divide-gray-200 sm:space-y-0 sm:-mt-8 lg:gap-x-8 lg:space-y-0"
				>
					{#each contributors as contributor}
						<li class="sm:py-8">
							<div class="space-y-4 sm:grid sm:grid-cols-3 sm:items-start sm:gap-6 sm:space-y-0">
								<div class="aspect-w-3 aspect-h-2 sm:aspect-w-3 sm:aspect-h-4">
									<img
										class="rounded-full grayscale shadow-lg object-contain"
										src={contributor.image}
										alt=""
									/>
								</div>
								<div class="sm:col-span-2">
									<div class="space-y-4">
										<div class="text-lg leading-6 font-medium space-y-1">
											<h3>{contributor.name}</h3>
											<p class="text-teal-500 dark:text-teal-300">{contributor.title}</p>
										</div>
										<div class="text-lg">
											<p class="text-gray-500 dark:text-gray-300">
												{contributor.description}
											</p>
										</div>
										<ul class="flex space-x-5">
											<li>
												<a href={contributor.twitter} class="text-gray-400 hover:text-teal-500">
													<span class="sr-only">Twitter</span>
													<svg
														class="w-5 h-5"
														fill="currentColor"
														viewBox="0 0 20 20"
														aria-hidden="true"
													>
														<path
															d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 010 16.407a11.616 11.616 0 006.29 1.84"
														/>
													</svg>
												</a>
											</li>
											<li>
												<a href={contributor.linkedin} class="text-gray-400 hover:text-teal-500">
													<span class="sr-only">LinkedIn</span>
													<svg
														class="w-5 h-5"
														fill="currentColor"
														viewBox="0 0 20 20"
														aria-hidden="true"
													>
														<path
															fill-rule="evenodd"
															d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z"
															clip-rule="evenodd"
														/>
													</svg>
												</a>
											</li>
										</ul>
									</div>
								</div>
							</div>
						</li>
					{/each}
				</ul>
			</div>
		</div>
	</div>
</div>
