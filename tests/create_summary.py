# I know I have like 3 different names for the same function. Im sorry
from bot.utils import create_summary

# TODO: I'm kinda hardcoding this test data here. Maybe I could import it from a different file
test_data = 'WASHINGTON (AP) — President-elect Donald Trump has asked U.S. Rep. Michael Waltz, a retired Army National Guard officer and war veteran, to be his national security adviser, a person familiar with the matter said Monday. The nod came despite simmering concerns on Capitol Hill about Trump tapping members of the House, where the final tally is still uncertain and there are worries about pulling any GOP members from the chamber because that would force a new election to fill the empty seat. The person spoke on the condition of anonymity to discuss the matter before Trump made a formal announcement. The move would put Waltz at the forefront of a litany of national security crises — ranging from the ongoing effort to provide weapons to Ukraine and escalating worries about the growing alliance between Russia and North Korea to the persistent attacks in the Middle East by Iran proxies and the push for a cease-fire between Israel and Hamas and Hezbollah. Waltz, a three-term GOP congressman from east-central Florida, was the first Green Beret elected to the U.S. House, and easily won reelection last week. He has been chairman of the House Armed Services subcommittee on readiness and a member of the House Foreign Affairs Committee and the Permanent Select Committee on Intelligence. Waltz is an ardent Trump advocate who backed efforts to overturn the 2020 election. He is considered hawkish on China, and called for a U.S. boycott of the 2022 Winter Olympics in Beijing due to its involvement in the origin of COVID-19 and its ongoing mistreatment of the minority Muslim Uighur population.  He has been a sharp critic of the chaotic U.S. withdrawal from Afghanistan and has called on the U.S. to hold accountable those who bear responsibility for the deaths of the 13 U.S. service members at Abbey Gate and for “thousands of Americans and allies behind enemy lines.” He has also repeated Trump’s frequent complaints about a so-called “woke” military that the former president has derided as soft and too focused on diversity and equity programs. In a statement last year, Waltz said that as head of the readiness subcommittee: “I am ready to get to work to better equip our military and turn our focus away from woke priorities and back to winning wars. Our national security depends on it.” A graduate of Virginia Military Institute, Waltz was a Green Beret. He served in the active-duty Army for four years before moving to the Florida Guard. While in the Guard he did multiple combat tours in Afghanistan, the Middle East and Africa and was awarded four Bronze Stars, including two with valor. He also worked in the Pentagon as a policy adviser when Donald Rumsfeld and Robert Gates were defense chiefs. “President-Elect Trump will begin making decisions on who will serve in his second Administration soon,” said Karoline Leavitt, a spokesperson for the Trump transition. “Those decisions will be announced when they are made.” Richard Goldberg, who served at the National Security Council during Trump’s first term, called Waltz an impressive pick whose background as an elite U.S. service member and experience on Capitol Hill will be of great value to Trump. “With fires raging across the world right now, Waltz is well positioned to help the President put out those fires,” said Goldberg, who is now a senior adviser at the Foundation for Defense of Democracies in Washington. Waltz’s selection was first reported by The Wall Street Journal. — AP writers Jill Colvin in New York and Zeke Miller and Aamer Madhani in Washington contributed.'

res = create_summary(test_data)
print(res)